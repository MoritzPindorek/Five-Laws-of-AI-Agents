"""Executable checks for the educational gate (unittest, Python standard library)."""
import itertools, json, unittest
from dataclasses import replace
from concurrent.futures import ThreadPoolExecutor
from reference_gate import Tri, Verdict, Judgments, Mandate, Proposal, Gateway, decision
YES = Judgments(*(Tri.YES,)*5)

def mandate(**opts):
    d=dict(mandate_id='M-1',principal='mock hospital',agent='agent1',tools=frozenset({'read','write'}),purposes=frozenset({'audit'}),subjects=frozenset({'s1'}),resource_budget=100,valid_from=0,expires_at=100,epoch=3)
    d.update(opts);return Mandate(**d)

def proposal(i='q1',**opts):
    d=dict(id=i,agent='agent1',tool='read',purpose='audit',subject='s1',cost=10,when=5,policy_epoch=3,judgments=YES)
    d.update(opts);return Proposal(**d)

class DecisionTable(unittest.TestCase):
    def test_exhaustive_243(self):
        counts={x:0 for x in Verdict}
        for x in itertools.product(Tri,repeat=5):
            counts[decision(Judgments(*x))]+=1
        self.assertEqual(counts,{Verdict.ALLOW:1,Verdict.DENY:211,Verdict.REVIEW:31})
    def test_missing_remedy_must_review(self):
        self.assertEqual(decision(replace(YES,remedy_justified=Tri.UNKNOWN)),Verdict.REVIEW)
    def test_adverse_reviewer_must_deny(self):
        self.assertEqual(decision(replace(YES,process_complete=Tri.NO)),Verdict.DENY)
    def test_unknown_never_overrides_no(self):
        self.assertEqual(decision(replace(YES,process_complete=Tri.NO,hard_clear=Tri.UNKNOWN)),Verdict.DENY)

class MockEnforcement(unittest.TestCase):
    def test_authorized_executes_once(self):
        g=Gateway(mandate());self.assertEqual(g.submit(proposal())[0],Verdict.ALLOW)
        self.assertEqual(len(g.tool.effects),1);self.assertEqual(g.spent,10)
    def test_out_of_scope(self):
        g=Gateway(mandate());self.assertEqual(g.submit(proposal(tool='export'))[1],'OUT_OF_SCOPE')
        self.assertEqual(g.tool.effects,[])
    def test_parent_must_bound_child(self):
        g=Gateway(mandate(parent_scope=frozenset({'read'})))
        self.assertEqual(g.submit(proposal(tool='write'))[1],'PARENT_SCOPE')
    def test_purpose_binding(self):
        g=Gateway(mandate());self.assertEqual(g.submit(proposal(purpose='sell'))[1],'OUT_OF_SCOPE')
    def test_expiry(self):
        g=Gateway(mandate());self.assertEqual(g.submit(proposal(when=100))[1],'TIME_OUT_OF_SCOPE')
    def test_revocation(self):
        g=Gateway(mandate(revoked=True));self.assertEqual(g.submit(proposal())[1],'REVOKED_OR_STALE_EPOCH')
    def test_stale_epoch_after_update(self):
        g=Gateway(mandate());g.set_mandate(mandate(epoch=4))
        self.assertEqual(g.submit(proposal())[1],'REVOKED_OR_STALE_EPOCH')
    def test_negative_cost(self):
        g=Gateway(mandate());self.assertEqual(g.submit(proposal(cost=-10))[1],'NEGATIVE_COST')
    def test_budget_across_calls(self):
        g=Gateway(mandate());g.submit(proposal('a',cost=70));self.assertEqual(g.submit(proposal('b',cost=40))[1],'AGGREGATE_BUDGET')
        self.assertEqual(g.spent,70)
    def test_composed_disclosure(self):
        g=Gateway(mandate(), banned_disclosure_sets=[{'zipcode','age','name'}])
        self.assertEqual(g.submit(proposal('a',disclosure_tags=frozenset({'zipcode','age'})))[0],Verdict.ALLOW)
        self.assertEqual(g.submit(proposal('b',disclosure_tags=frozenset({'name'})))[1],'COMPOSED_DISCLOSURE')
    def test_duplicate_replay(self):
        g=Gateway(mandate());g.submit(proposal());self.assertEqual(g.submit(proposal())[1],'DUPLICATE_ID')
    def test_tool_failure_does_not_spend(self):
        g=Gateway(mandate());g.tool.fail_next=True
        self.assertEqual(g.submit(proposal())[1],'SIMULATED_TOOL_FAILED')
        self.assertEqual(g.spent,0)
    def test_direct_mock_call_is_rejected(self):
        g=Gateway(mandate());
        with self.assertRaises(PermissionError):g.tool.apply(proposal())
    def test_log_tamper_detected(self):
        g=Gateway(mandate());g.submit(proposal());self.assertTrue(g.verify_history())
        g.events[0]['verdict']='DENY';self.assertFalse(g.verify_history())
        with self.assertRaises(ValueError):g.reconstruct()
    def test_event_reconstruction(self):
        g=Gateway(mandate());g.submit(proposal('a'));g.submit(proposal('b',tool='invalid'))
        summary=g.reconstruct();self.assertEqual(summary['allowed_count'],1)
        self.assertEqual(summary['event_count'],2)
    def test_concurrent_spend_cannot_exceed_budget(self):
        g=Gateway(mandate(resource_budget=100))
        with ThreadPoolExecutor(max_workers=8) as ex:
            results=list(ex.map(lambda i:g.submit(proposal(f'concurrent-{i}',cost=25)),range(30)))
        self.assertEqual(sum(v==Verdict.ALLOW for v,_ in results),4)
        self.assertEqual(g.spent,100)
    def test_tristate_review_never_executes(self):
        g=Gateway(mandate());v,_=g.submit(proposal(judgments=replace(YES,contest_resolved=Tri.UNKNOWN)))
        self.assertEqual(v,Verdict.REVIEW);self.assertEqual(g.tool.effects,[])

if __name__=='__main__':
    unittest.main(verbosity=2)
