# Heavy release gate read-only scenario response

**Run:** 2026-09-27, fresh skill-guided subagent reading the heavy issue, trace, snapshot, and release references. No files or GitHub records were changed by the scenario agent. This is a bounded behavior check, not an integrated release gate implementation. The structural RED control was the absence of a dedicated release procedure before the edit; a behavioral no-guidance failure was not demonstrated.

## Observed answer

> REL-A (#100), target 1.0.0, is not ready for approval or publication. Its selected set is C2.3 and C2.4 through `included_in`. The gate's recorded state, integrated source, PRD revision, issue revisions, and native blockers were not supplied, so those facts remain unknown.

| Mandatory input | Result | Observed reason |
| --- | --- | --- |
| C2.3 verification | FAIL | One of two claimed requirements lacks current passing verification; closure and one green test do not cover it. |
| C2.4 verification | UNKNOWN | G1 was stated, but exact evidence and revision match need checking. |
| Intended-use validation | FAIL | Demonstration lacks accepting person and checked PRD criterion. |
| Public-contract/SemVer review | FAIL | No reviewed compatibility artifact. |
| Trace/views | FAIL | H1 became stale when an issue changed to H2. |
| Gate inputs/native blockers | UNKNOWN | Current records and revisions were not supplied. |
| Human authorization | FAIL | Agent comment is not a human decision. |

The response retained REL-A, C2.3, and C2.4 through a target slip to 1.1.0, kept `released_in` absent until publication, invalidated old authorization after candidate change, required an exact human decision record, and treated an existing tag as observation rather than approval. It made no publication action.

## Scoring and correction

Assertions 1–4 and 6: PASS for this read-only fixture. Assertion 5: PARTIAL before refactor; the agent correctly required a reason and reviewed return from failure, but identified that the reference did not distinguish `pending` for missing/unknown evidence from `failed` for observed adverse results. The release reference was tightened accordingly. Candidate digest and full snapshot validation remain unimplemented; the agent explicitly refused a machine-checked candidate claim.

The focused recheck after the correction classified G-1 as `pending` for the supplied missing/stale inputs, `pending -> failed` only after an observed current failing verification, `failed -> pending` after reviewed correction and a new check, and `pending -> satisfied` only when all checks pass at one snapshot. No records changed.
