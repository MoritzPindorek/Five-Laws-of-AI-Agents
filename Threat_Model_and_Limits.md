# Reference Gateway Threat Model and Non-Claims

## What the demo does

- Enumerates all 243 five-tri-state judgment combinations and returns ALLOW only for five YES judgments.
- Restricts a mock action by agent, tool, subject, stated purpose, parent-scope filter, mandate epoch and expiration.
- Accumulates budget across calls under a single-process lock; denies a privacy-reidentification pattern across multiple locally permissible outputs.
- Tests revocation and stale epochs, duplicate replay, unknown review, mock-tool error rollback, and a simple hash-chain of record dictionaries.

## What the demo cannot do

- Authenticate the external world or prove reviewer competence. Anyone able to call `set_mandate` inside the Python process controls a simulated authority change.
- Secure a real Python process against a hostile co-resident attacker. `MockTool._token` is a Python object, not a cryptographic capability or kernel boundary.
- Secure a log against an attacker who can rewrite both events and trusted chain head; the hash chain is neither signed nor externally anchored, and timestamps are stipulated.
- Prevent cross-process tool bypass, network effects, unauthorized accounts, data exfiltration, prompt injection against true tool schemas, or side effects the `disclosure_tags` model misses.
- Establish moral correctness of five externally supplied flags; no jurist or ethics panel has validated the labels.
- Prove actual operations meet legally mandated delay thresholds or accessibility requirements.

## Required steps before operational claims

Implement a separate process policy enforcement point with no alternate tool path; protected principal and policy registry; independently signed/revocable mandates; formal replay protection; atomic durable effects recording; real tool-adapter integration tests; audit log anchoring and red-team testing; human-rights and privacy impact assessment; institutional conflict-of-interest controls and domain-specific emergency mandate. Independent auditors must attempt bypass and demonstrate both *blocked* and *permitted* actions end-to-end.

## Round-3 executable integrity disclosure

The test suite now deliberately invokes `g.tool.apply(proposal, g.tool._token)` inside the same Python process and **succeeds without a `Gateway.submit` event**. This proves the mock object cannot be a security perimeter. `Gateway` records `MANDATE_UPDATE` events and proposal-context digests, and rejects client-submitted timestamps inconsistent with an injected deterministic clock. Neither mechanism proves authentic time, external principal authorization, or tamper-proof recording. The default clock returns 5 solely for reproducible fictional fixtures. No deployed tool actions occur.
