Both current `SATISFIED` claims on fixture outcome #101 are unsupported at commit C. The supported assessment is **UNKNOWN for AC1 and AC2**, rather than UNSATISFIED: no applicable failing result is supplied.

| Criterion | Current mapping | Accepted historical evidence | Assessment at C |
|---|---|---|---|
| AC1 | R1/S2 | E1 passed R1/S1 at A | **UNKNOWN.** Neither the requirement revision nor delivery identity matches; C also changes relevant behavior. |
| AC2 | R1/S2 + R2/S1 | E2 passed those inputs at B | **UNKNOWN.** Requirement inputs match, but the behavior-changing B→C delta affects AC2. |

Preserve E1 and E2 as accepted historical passes against their original inputs. Do not retarget them to S2/C. PR #201 contributes part of R1; #202 contributes the remainder and R2. That establishes declared contribution coverage, not accepted satisfaction. Their actual review, merge, integration target, and closure intent are unavailable. The fixture reports #101 OPEN with empty closing-PR references.

The independent **S2e scenario at B** changes the assessment:

- **AC2 can retain SATISFIED within the fixture:** E2 evaluated R1/S2 and R2/S1 at B, implementation remains B, and the approver explicitly recorded S2e’s semantic equivalence to S2. Preserve E2’s original identity and reference the equivalence decision.
- **AC1 remains UNKNOWN:** E1 evaluated S1 at A. S2e’s equivalence to S2 supplies neither S1→S2 reconciliation nor AC1 evidence applicable at B. E2’s AC2 pass cannot be reassigned to AC1 merely because both reference R1.
- Consequently, the whole outcome is still **UNKNOWN**, since every applicable criterion needs accepted current evidence.

Under the [governance contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers-backplane/governance.md):

- **#101’s `Coverage and Satisfaction` section** owns current criterion-to-requirement mappings, bounded PR contributions, accepted evaluation pointers, applicability, and gaps.
- **Accepted evaluations** belong in immutable project-owned evidence recording exact approved inputs, tested integration/delivery identity, method, observed results, acceptance, evidence availability, and remaining obligations. The mutable issue claim is an index to that evidence.
- **Project displays and checkpoint records** derive their satisfaction from reconciled evidence. They should disclose the issue’s raw `SATISFIED` claims alongside the supported UNKNOWN assessment at C. Parent summaries reference child evaluations.
- The checkpoint pair, `.sp-bp/state.md` and `.sp-bp/github-state.json`, is a dated account. Its later storage commit must remain distinct from the tested delivery commit; capture completeness and product satisfaction are separate conclusions.

Missing inputs include criterion and requirement wording, full authority/approval records, precise PR contribution boundaries and combined-result owner, complete evaluation artifacts, exact commit identities and relevant deltas, project verification seams, PR review/integration facts, lifecycle labels, and any declared Project/checkpoint scope and mode. These prevent adequacy, eligibility, closeout, or complete-capture claims; they do not erase the fixture-supported historical passes.

**Permissible now:** read-only reconciliation of supplied records and drafting proposed corrections in this response. Proposed follow-up is to obtain the missing inputs, revalidate both affected criteria against current approved requirements at C, and obtain accepted immutable results. For S2e/B, retain AC2’s reconciled evidence and resolve AC1’s separate gap.

Issue edits, Project refreshes, checkpoint writes/commits, execution, and closure require a separately authorized operation and their applicable gates. This probe authorizes none of them. No live queries, agents, helpers, or state changes were used.