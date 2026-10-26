# Issue #11 whole-change review

Reviewer: fresh `gpt-6-astra`, high reasoning; read-only review of
`66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4..80b54e2ae8104ea694c66f797446ac40df05232b`.
The reviewer received the approved specifications/plan, all five Review Focus
items, original run identities, excluded observations and execution rulings.
No review subagents, fixture mutations or credential-store reads were used.

## Reviewer result

**Ready to merge: with one evidence fix.**

The product corrections are narrowly scoped and consistent with the approved
contract. Retaining C's lifecycle mechanism is justified by unchanged
guide/manifests and fresh E payload checks. Historical #34 transitions are
honestly distinguished from current behavioral runs.

**Critical:** None.

**Important:** The acceptance matrix marked unauthenticated-host rerun/PASS,
but setup-auth.json lacked observed host version, command and timestamp.
Authenticated candidate verification cannot establish this changed-host seam.
Capture fresh current-host auth-status and pre-model refusal in a new owned,
never-authenticated profile, with preservation; otherwise leave it UNKNOWN.
No login, credential copying or remote lifecycle fixture is needed.

**Minor:** None.

Reviewer verification: branch whitespace check; acceptance verifier (39 rows,
evidence hashes, nine compiled blocks); independent comparison of all eight
final conformance preservation snapshots; selected source-blob comparisons;
bounded credential-pattern scan of changed artifacts, with no matches.

## Declined to judge and executor dispositions

- Final integrated-target acceptance and closure: pending authorized integration
  and subsequent verification. Accepted; this contribution claims local
  candidate verification only.
- Other hosts, release and external-pilot readiness: outside #11. Accepted;
  no result or lifecycle state is implied for them.
- Cause of excluded normal-profile catalogue change: evidence cannot establish
  causality. Accepted; excluded from preservation claims without attribution.
- Ignored raw streams and credential-store contents: intentionally excluded.
  Accepted; publishable derived observations preserve tool/result identities
  without credential reads or upstream document bodies.

## Important finding disposition

The old receipt failed the new evidence-completeness assertion (RED). A fresh
owned profile on Claude 2.1.311 returned auth-status exit 1, loggedIn false and
authMethod none. A real no-tool request returned authentication_failed from a
synthetic local response: zero API duration, model usage, cost and tokens.
Protected before/after snapshots matched (GREEN). See
[current signed-out evidence](2026-10-26-issue-11-unauthenticated-final.json).
No login, credential copy, plugin install or normal-profile fallback occurred.

The first test adapter incorrectly required zero SDK turns; Claude counts its
synthetic authentication error as one turn. That failed attempt is retained in
ignored scratch with its before snapshot. The corrected new-profile attempt
asserts the actual no-model indicators, rather than treating SDK turn count as
proof of inference. No passing observation from that first adapter is invented.

The final matrix uses the current receipt and keeps the initial signed-out
receipt as historical evidence. This is the single focused fix pass; no product
source changed. Focused reviewer confirmation and final checks follow in a
later append. No deferred minors were reported.

## Focused confirmation

The same reviewer confirmed the Important finding resolved after inspecting
the new receipt, corrected source and current matrix. Claude 2.1.311 identity,
signed-out status, synthetic refusal, zero inference usage and unchanged
protected snapshots are established. The recorded response supports the
corrected SDK turn-count interpretation. The reviewer reran the 39-row/nine-
compilation evidence verifier and whitespace checks; both pass.

**Final verdict:** no remaining review findings; ready for authorized
publication/integration. Final integrated acceptance remains pending.
