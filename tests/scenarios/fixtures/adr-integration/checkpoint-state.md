# Backplane checkpoint — invented ADR qualification fixture

Format: sp-bp-checkpoint/v1
Capture ID: invented-adr-capture-20261115
JSON SHA-256: a4aa1651edab56d412818258e039018b5bbbf1b4e399c54867f9e4d8b5c0c167
Observation window: 2026-11-15T22:00:00Z to 2026-11-15T22:18:23.593214Z
Mode / status / origin: issues-only / complete / invented-fixture
Repository: example/governance-fixture; Project: observed absent in explicitly selected issues-only fixture mode.
Source commit: f242185f2332885382a421b57d516e0db1900205; verified delivery: b3b0c71f897bd265185baf2cfcc22269fc44d8f1; future pair storage/acceptance identity remains external.

## Product hierarchy and native work

- example/governance-fixture#101: Preserve an existing valid installation; state OPEN, parent None, children [], blockers [], blocking [], closing PRs []; labels ['backplane:review']; milestone None. Native closure progress supplies no parent satisfaction.

## Approved obligations, dispositions and coverage

- R1@S1: Preserve an existing valid installation. @ S1/f242185f2332885382a421b57d516e0db1900205
- example/governance-fixture#101:AC1: Preserve the existing valid installation.; requirements ['R1@S1']; authority S1/f242185f2332885382a421b57d516e0db1900205; delivery b3b0c71f897bd265185baf2cfcc22269fc44d8f1.
Dispositions: []; coverage: [{"id": "COV1", "issue_id": "example/governance-fixture#101", "criterion_id": "example/governance-fixture#101:AC1", "requirement_ids": ["R1@S1"], "contribution_issue_ids": ["example/governance-fixture#101"], "pr_ids": ["example/governance-fixture!201"], "combined_result_owner": "fixture-owner", "scope": "The sole fixture criterion is covered by preservation contribution PR201."}]

## Evaluated satisfaction and evidence

- EV1: SATISFIED / current; criterion example/governance-fixture#101:AC1; verified b3b0c71f897bd265185baf2cfcc22269fc44d8f1; method Fixture preservation verification; ADR edition/content/approval and local manifest ownership alignment checked in invented fixture; observed PASS supplied by the invented fixture.; evidence ['E1', 'RV1', 'EADR-REVIEWED', 'EADR-CURRENT', 'EADR-APPROVAL']; review approvals ['A2']; remaining []; limitations [].

## Authority and evidence availability

- Authority S1 (specification), available, fixture:spec/S1 @ f242185f2332885382a421b57d516e0db1900205; approvals ['A1', 'AADR'], approver None, scope None, limitations []. Content: R1: Preserve an existing valid installation. AC1 implements R1. ADR-0001 edition 1 retains project installation-manifest authority and preservation of unrelated valid entries under R1/AC1. Immutable source f242185f2332885382a421b57d516e0db1900205:ADR-0001-001-retain-project-installation-authority.md; reviewed bytes EADR-REVIEWED SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc, administrative Current record EADR-CURRENT, actual staged response EADR-APPROVAL and approval authority AADR.
- Authority A1 (approval), available, fixture:approval/A1 @ 2026-10-01T12:00:00Z; approvals [], approver fixture-approver, scope R1/AC1 at S1, limitations []. Content: Fixture approver approved R1 and AC1 at S1.
- Authority A2 (approval), available, fixture:review/A2 @ 2026-10-01T12:00:00Z; approvals [], approver fixture-reviewer, scope AC1 at S1/B, limitations []. Content: Fixture reviewer accepted AC1 at S1 and delivery B.
- Authority AADR (approval), available, fixture:approval/approval.txt @ f242185f2332885382a421b57d516e0db1900205; approvals [], approver fictional fixture operator, scope ADR-0001 edition 1 retains project installation-manifest authority and preservation of unrelated valid entries under R1/AC1., limitations []. Content: FICTIONAL EVALUATION INPUT. Fixture operator, 2026-11-15, separately responds: Approve ADR-0001 edition 1 as written. Reviewed bytes SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc; source context: invented separate architectural review, not spec/plan/release assent. Scope: project-owned installation manifest and R1/AC1 preservation.
 ADR-0001 edition 1 retains project installation-manifest authority and preservation of unrelated valid entries under R1/AC1. Immutable source f242185f2332885382a421b57d516e0db1900205:ADR-0001-001-retain-project-installation-authority.md; reviewed bytes EADR-REVIEWED SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc, administrative Current record EADR-CURRENT, actual staged response EADR-APPROVAL and approval authority AADR.
- Evidence E1 (verification), available, fixture:verification/E1 @ b3b0c71f897bd265185baf2cfcc22269fc44d8f1, SHA256 None, verified b3b0c71f897bd265185baf2cfcc22269fc44d8f1, limitations []. Content: Invented fixture result: AC1 passed preservation verification against S1 and B.
- Evidence RV1 (review), available, fixture:review/RV1 @ b3b0c71f897bd265185baf2cfcc22269fc44d8f1, SHA256 None, verified b3b0c71f897bd265185baf2cfcc22269fc44d8f1, limitations []. Content: Invented fixture review accepted AC1 at S1/B.
- Evidence EADR-REVIEWED (other), available, fixture:adr/ADR-0001-001-reviewed.txt @ f242185f2332885382a421b57d516e0db1900205, SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc, verified None, limitations []. Content: # Proposed ADR-0001 edition 1: retain project installation authority

The project owns its installation manifest and preserves unrelated existing valid entries. This constrains fixture requirement R1 and criterion AC1. Alternatives: project ownership or a remote service owning writes. Project ownership preserves the existing product contract. No remote operation, runtime, approval store or publication is introduced.

- Evidence EADR-CURRENT (other), available, fixture:adr/ADR-0001-001-retain-project-installation-authority.md @ f242185f2332885382a421b57d516e0db1900205, SHA256 4be6c42ef5a643b136911a9a70db740bde445675075a1a9e54f0f58997b07ef0, verified None, limitations []. Content: ---
id: ADR-0001
title: Retain project installation authority
revision: 1
state: Current
decision_date: 2026-11-15
revision_date: 2026-11-15
approved_by: fictional fixture operator
approved_revision: 1
approval_ref: approval.txt
---

# Proposed ADR-0001 edition 1: retain project installation authority

The project owns its installation manifest and preserves unrelated existing valid entries. This constrains fixture requirement R1 and criterion AC1. Alternatives: project ownership or a remote service owning writes. Project ownership preserves the existing product contract. No remote operation, runtime, approval store or publication is introduced.

Administrative approval capture only; decision unchanged. Original reviewed proposal is ADR-0001-001-reviewed.txt at SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc. Fictional input, not actual publisher approval.

- Evidence EADR-APPROVAL (approval), available, fixture:adr/approval.txt @ f242185f2332885382a421b57d516e0db1900205, SHA256 7dfcfe2ebe61c4a4ddbaebc0f43fea47cb5483be4ee80756c251de23323b7463, verified None, limitations []. Content: FICTIONAL EVALUATION INPUT. Fixture operator, 2026-11-15, separately responds: Approve ADR-0001 edition 1 as written. Reviewed bytes SHA256 4d6375c792aefeb7aa8c61f22460d5cbc6b2dedf6f8759ed355202b9a30085dc; source context: invented separate architectural review, not spec/plan/release assent. Scope: project-owned installation manifest and R1/AC1 preservation.


## Scope, release targets and next reconciliation

Captured issue IDs ['example/governance-fixture#101']; excluded []; external []; native collections have explicit terminal pages and matching totals. Rechecked original inputs and added ADR/approval/evidence at their exact fixture revisions.
Whole-capture limitations: []. No milestone/release target or publication authority is observed. All approvals, native graph and SATISFIED results here are invented fixture inputs, not actual publisher approval or live product acceptance. Offline interpretation requires current native rechecks before live mutation. Exact pair acceptance and later publication must be observed separately.
