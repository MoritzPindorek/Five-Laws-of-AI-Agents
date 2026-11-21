"""Educational delegated-action gateway; NOT a security boundary or moral oracle.

All authority, prohibition, dispute, process and remedy inputs are externally
supplied assertions. This mock never authenticates real-world authority.
Python >= 3.10. Standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from threading import RLock
from typing import Dict, FrozenSet, Optional, Tuple, List, Callable
import json

class Tri(str, Enum):
    YES = "YES"
    NO = "NO"
    UNKNOWN = "UNKNOWN"

class Verdict(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REVIEW = "REVIEW"

@dataclass(frozen=True)
class Judgments:
    authority: Tri
    hard_clear: Tri
    contest_resolved: Tri
    process_complete: Tri
    remedy_justified: Tri

    def as_dict(self):
        return {k: getattr(self, k).value for k in self.__dataclass_fields__}

def decision(flags: Judgments) -> Verdict:
    vals = list(flags.as_dict().values())
    if 'NO' in vals:
        return Verdict.DENY
    if 'UNKNOWN' in vals:
        return Verdict.REVIEW
    return Verdict.ALLOW

@dataclass(frozen=True)
class Mandate:
    mandate_id: str
    principal: str
    agent: str
    tools: FrozenSet[str]
    purposes: FrozenSet[str]
    subjects: FrozenSet[str]
    resource_budget: int
    valid_from: int
    expires_at: int
    epoch: int
    parent_scope: FrozenSet[str] = frozenset()
    revoked: bool = False

    def __post_init__(self):
        if type(self.resource_budget) is not int or self.resource_budget < 0:
            raise ValueError('Resource budget must be a nonnegative integer')
        if any(type(x) is not int for x in (self.valid_from,self.expires_at,self.epoch)):
            raise ValueError('Time and epoch fields must be integers')
        if self.valid_from >= self.expires_at:
            raise ValueError('Invalid mandate time window')
        if not self.mandate_id or not self.principal or not self.agent:
            raise ValueError('Mandate identity cannot be empty')

@dataclass(frozen=True)
class Proposal:
    id: str
    agent: str
    tool: str
    purpose: str
    subject: str
    cost: int
    when: int
    policy_epoch: int
    judgments: Judgments
    disclosure_tags: FrozenSet[str] = frozenset()
    # e.g. third query combines with prior safe queries into disallowed identity disclosure

class MockTool:
    """A simulated tool that can be invoked only with its gateway-held object token.

    NOT a genuine security boundary: Python process memory is not an isolation
    or authentication mechanism. No external side effects are performed.
    """
    def __init__(self):
        self._token = object()
        self.effects = []
        self.fail_next = False

    def apply(self, proposal: Proposal, token=None):
        if token is not self._token:
            raise PermissionError('Mock tool requires gateway dispatch token')
        if self.fail_next:
            self.fail_next = False
            raise RuntimeError('Simulated tool failure')
        self.effects.append({'id': proposal.id, 'tool': proposal.tool, 'subject': proposal.subject, 'cost': proposal.cost})

class Gateway:
    """Single-process, atomic mock gateway with chained *integrity* receipts.

    A hash chain detects post-hoc accidental edits relative to a trusted head;
    it is NOT a digital signature, independent attestation, secure log store, or
    evidence that a real third party authorized the mandate.
    """
    def __init__(self, mandate: Mandate, *, banned_disclosure_sets=(), clock: Optional[Callable[[], int]]=None):
        self._lock = RLock()
        # Default clock is a deliberately fixed test fixture, NOT a real trusted clock.
        # Production would require independent trusted time and protected dispatch.
        self.clock = clock if clock is not None else (lambda: 5)
        self.mandate = mandate
        self.tool = MockTool()
        self.spent = 0
        self.observed_tags = frozenset()
        self.banned_disclosure_sets = tuple(frozenset(x) for x in banned_disclosure_sets)
        self.events: List[dict] = []
        self._head = '0'*64
        self._handled = set()

    @staticmethod
    def _digest(payload: dict) -> str:
        return sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(',',':')).encode()).hexdigest()

    def _append_event(self, fields: dict):
        core = {'sequence': len(self.events)+1, 'previous_hash': self._head, **fields}
        event = dict(core, event_hash=self._digest(core))
        self.events.append(event)
        self._head = event['event_hash']

    def _record(self, proposal: Proposal, verdict: Verdict, reason: str, now: int):
        proposal_core = {
            'id': proposal.id, 'agent': proposal.agent, 'tool': proposal.tool,
            'purpose': proposal.purpose, 'subject': proposal.subject, 'cost': proposal.cost,
            'when': proposal.when, 'policy_epoch': proposal.policy_epoch,
            'disclosure_tags': sorted(proposal.disclosure_tags),
            'judgments': proposal.judgments.as_dict(),
        }
        fields = {'event_type':'PROPOSAL', 'checked_at':now,
                'proposal_digest':self._digest(proposal_core),
                'proposal_id': proposal.id, 'tool': proposal.tool, 'epoch': proposal.policy_epoch,
                'verdict': verdict.value, 'reason': reason, 'spent_after': self.spent,
                'judgments': proposal.judgments.as_dict()}
        self._append_event(fields)

    def set_mandate(self, new_mandate: Mandate):
        """Simulated externally authorized mandate update. Caller is trusted in this demo."""
        with self._lock:
            if new_mandate.epoch <= self.mandate.epoch:
                raise ValueError('Epoch must strictly increase')
            old=self.mandate
            self.mandate = new_mandate
            self._append_event({'event_type':'MANDATE_UPDATE','old_epoch':old.epoch,
                'new_epoch':new_mandate.epoch, 'mandate_id':new_mandate.mandate_id,
                'revoked':new_mandate.revoked,
                'mandate_digest':self._digest({'id':new_mandate.mandate_id,
                    'principal':new_mandate.principal,'agent':new_mandate.agent,
                    'tools':sorted(new_mandate.tools),'purposes':sorted(new_mandate.purposes),
                    'subjects':sorted(new_mandate.subjects),'budget':new_mandate.resource_budget,
                    'parent_scope':sorted(new_mandate.parent_scope),
                    'valid_from':new_mandate.valid_from,'expires_at':new_mandate.expires_at,
                    'epoch':new_mandate.epoch,'revoked':new_mandate.revoked})})

    def submit(self, proposal: Proposal) -> Tuple[Verdict, str]:
        with self._lock:  # serializes epoch check, budget check and mock side effect
            m = self.mandate
            now = self.clock()  # injected fixture; the proposal timestamp is NOT trusted.
            if type(now) is not int:
                raise ValueError('Clock fixture must return integer seconds')
            if proposal.id in self._handled:
                verdict, reason = Verdict.DENY, 'DUPLICATE_ID'
            elif type(proposal.cost) is not int or proposal.cost < 0:
                verdict, reason = Verdict.DENY, 'NEGATIVE_COST'
            elif now < m.valid_from or now >= m.expires_at or proposal.when < m.valid_from or proposal.when >= m.expires_at:
                verdict, reason = Verdict.DENY, 'TIME_OUT_OF_SCOPE'
            elif proposal.when != now:
                verdict, reason = Verdict.DENY, 'UNTRUSTED_TIMESTAMP'
            elif m.revoked or proposal.policy_epoch != m.epoch:
                verdict, reason = Verdict.DENY, 'REVOKED_OR_STALE_EPOCH'
            elif proposal.agent != m.agent or proposal.tool not in m.tools or proposal.purpose not in m.purposes or proposal.subject not in m.subjects:
                verdict, reason = Verdict.DENY, 'OUT_OF_SCOPE'
            elif m.parent_scope and proposal.tool not in m.parent_scope:
                verdict, reason = Verdict.DENY, 'PARENT_SCOPE'
            elif self.spent + proposal.cost > m.resource_budget:
                verdict, reason = Verdict.DENY, 'AGGREGATE_BUDGET'
            elif any(b.issubset(self.observed_tags | proposal.disclosure_tags) for b in self.banned_disclosure_sets):
                verdict, reason = Verdict.DENY, 'COMPOSED_DISCLOSURE'
            else:
                verdict = decision(proposal.judgments)
                reason = {'ALLOW':'ALL_CHECKS_YES','REVIEW':'UNKNOWN_REQUIREMENT', 'DENY':'NEGATIVE_REQUIREMENT'}[verdict.value]
                if verdict == Verdict.ALLOW:
                    try:
                        # Side effect occurs in same mock critical section as all checks
                        self.tool.apply(proposal, self.tool._token)
                    except RuntimeError:
                        verdict, reason = Verdict.DENY, 'SIMULATED_TOOL_FAILED'
                    else:
                        self.spent += proposal.cost
                        self.observed_tags |= proposal.disclosure_tags
            self._handled.add(proposal.id)
            self._record(proposal, verdict, reason, now)
            return verdict, reason

    def verify_history(self) -> bool:
        previous='0'*64
        for index, event in enumerate(self.events, 1):
            core = {k:v for k,v in event.items() if k!='event_hash'}
            if event['sequence'] != index or core['previous_hash'] != previous:
                return False
            if self._digest(core) != event['event_hash']:
                return False
            previous = event['event_hash']
        return previous == self._head

    def reconstruct(self) -> dict:
        if not self.verify_history():
            raise ValueError('History hash mismatch')
        allowed=[e for e in self.events if e.get('event_type')=='PROPOSAL' and e.get('verdict')=='ALLOW']
        control_events=sum(e.get('event_type')=='MANDATE_UPDATE' for e in self.events)
        return {'control_events':control_events,'event_count':len(self.events), 'allowed_count':len(allowed),
                'last_recorded_spent':next((e['spent_after'] for e in reversed(self.events) if e.get('event_type')=='PROPOSAL'), 0),
                'chain_head': self._head}
