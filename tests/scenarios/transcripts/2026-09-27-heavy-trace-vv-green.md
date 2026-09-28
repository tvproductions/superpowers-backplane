# Heavy trace and V&V GREEN response

Read-only agent replay on 2026-09-27 after adding `heavy-trace-and-evidence.md`. It read the edited backlog skill and its issue, heavy-record, and trace references, but not the scenario expectations or ADR. No file or GitHub mutation occurred.

## Verbatim response

This is a **provisional trace**. The prompt supplies the delivery claims, but not the issue URLs, record revisions, artifact locators, or approved revision for R-1. I therefore cannot certify any link or evidence as `current`.

| Forward trace from requirement | Claimed outcome | Link and evidence finding |
|---|---|---|
| R-1, approved PRD revision **unknown** | C2.3 | The `satisfies` claim is stated. G1 is stated to pass on integrated source for this pair, but its exact revisions, artifact, method, and acceptance are **unknown**. Its currency remains unknown. |
| R-2, approved **P2** | C2.3 | The `satisfies` claim is stated. Current passing evidence for this pair is **missing**. Any link or supporting artifact tied to P1 is **stale** until reviewed against P2. |
| R-2, approved **P2** | C2.4 | The `satisfies` claim is stated. Its known P1 evidence is **stale** for P2; current passing evidence is **missing**. |

The reverse view is **C2.3 → R-1 and R-2** and **C2.4 → R-2**. For each edge, the actual `satisfies` link, requirement anchor URL, outcome issue URL and revision, and release selection are **unknown** until the records are checked. E-1/E-2 and T-1/T-2 exist, but their assignment to these edges, reviewed revisions, and `exemplified_by`/`tested_by` links are **unknown**. They define behavior and checks; they are not passing evidence. R-2’s `anchored_in_prd` link must point to approved P2 at its exact revision; a P1 link is stale.

**C2.3 is not verified:** its R-2 claim lacks current passing verification, and current evidence for its own acceptance criteria has not been established. **The release is not validated:** U-1 has not occurred, so there is no separate passing intended-use validation artifact.

Each evidence artifact needs an immutable locator and revision plus one `## Backplane Evidence` JSON record with `schema: "backplane-evidence/v1"`, `kind`, named `method`, actual `result`, UTC `observed_at`, exact `integrated_source` commit or immutable build, covered requirements with their **exact approved PRD revisions**, covered outcomes with issue URLs and **consumed issue revisions**, applicable PRD `success_criteria`, `users` for validation, and the project’s named `accepted_by` person. G1 must name only claims it actually checked; “passing integrated” alone does not fill its unknown fields. A future U-1 record would need a stakeholder or intended-use method, result, PRD user group and success criterion, integrated source, and human acceptance. An editable issue comment alone is insufficient evidence.

The P1→P2 change requires a reviewed impact analysis across **both** R-2 outcomes, their examples, tests, designs, plans, evidence, derived views, and release. An `impact_review` record must identify old and new PRD revisions, affected edges and evidence, applicability decisions and rationale, and its accepting person. Preserve P1 evidence as history. Reuse it for P2 only if that reviewed impact record explicitly establishes applicability; otherwise obtain new P2 verification. No issues or documents were edited.
