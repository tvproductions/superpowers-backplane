# PR33 checkpoint review follow-ups

The operator requested both findings from the fresh PR33 review be fixed.
The pre-fix source is 945108ab610fe2bb927d33be31d92d036f953b6d.
Approved issue31 spec/plan/probe authorities remain unchanged.

## Corrections

- PullRequest.closing_issue_ids now permits null with a field-specific limitation,
  partial capture, incomplete closingIssuesReferences collection and unavailable
  graph observation. Known empty membership remains an observed terminal [].
  Current examples now include their known-empty PR closing collection.
- FieldValue now includes option_id. An observed single-select ID resolves within
  its own field's options and agrees with observed display text. Text/unset values
  use explicit null as applicable; unavailable values cannot establish complete
  capture. The readable template retains relevant Project identities.

## Verification

[Fixed fixture inputs](2026-10-13-checkpoint-review-followup-fixtures.json) were
saved before edits. [Baseline](2026-10-13-checkpoint-review-followup-baseline.json)
rejects both required representations. The fresh baseline application response
likewise identifies both exact-format gaps.

[Candidate](2026-10-13-checkpoint-review-followup-candidate.json) passes 38/38
native JSON/type/semantic outcomes: all 23 earlier outcomes replayed with current
fields and known-empty PR collection metadata, both new positives, and 13 guards
for incomplete PR observations, missing terminal metadata, missing/unknown/mismatched
selection IDs, text/unset values and unavailable selections.

The [probe manifest](2026-10-13-pr33-review-followup-runs.json) retains exact
prompts, verbatim responses, source hashes, exits and per-assertion grading.
The new reference application passes 6/6 assertions; original governance cases
pass 56/56; existing behavioral conformance passes 23/23. All completed sessions
exit zero; exits alone are not scoring evidence. Source hashes remain unchanged
during probes. Both skill frontmatters and all 10 direct links pass structural
checks; current JSON artifacts parse and changed paths pass git diff --check.
249 actual completed command executions were inspected: only reads,
no live queries, mutations, helpers or agent dispatch.

The unrelated freshness case supports 7/8 assertions in two complete responses:
stable-default ownership is not explicit, so R1 remains UNKNOWN. Both responses
are preserved; the unchanged canonical stable-default rule is not replaced or
treated as newly verified by these responses. Earlier 8/8 evidence remains
historical at its original source identity. This is a current behavioral proof
limit, not a failure of either requested representation fix.

The disposable validator remains fixture evidence, not a production acceptance
engine. Full live Project pagination, unavailable-body enforcement, production
capture/recovery, integrated satisfaction, other harnesses/bundle/host arrival
and release are not established. Prior scoped file/Git evidence is retained at
its original identities, not rerun as a production operation.

Root12/upstream238 preservation checks pass; both reserved .superpowers paths
remain absent and upstream is clean at bb92a77741419a4ab5f06e711a283343f1ada0c3.
No environment or runtime dependency was created or added. Temporary interpreter
helpers were removed after the operator questioned their necessity.

## Publication

Use the existing authorized PR33 source branch, feat/issue-31-governance-bridges.
Verify the containing commit and source hashes at the remote head after transport.
Issue31 remains OPEN with backplane:review; main integration, closure and release
remain subsequent gates. Preserve the externally managed native worktree.
