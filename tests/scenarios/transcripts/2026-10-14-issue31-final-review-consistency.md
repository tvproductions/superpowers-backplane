**A is valid for distinct recheck kinds and invalid for a repeated pair. B must stop at closeout step 4. C’s shipped rechecks are internally consistent; neither supports an unchanged result.**

**A — Structural validity**

The documented Recheck identity is **`(kind, id)`**, rather than `id` alone. [Identity rule](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:18)

| Candidate | Validity under that rule |
| --- | --- |
| One `issue` and one `delivery` recheck for `example/governance-fixture#101`, each with its own observation revisions | **Valid.** Their identities differ by kind. The complete shipped example uses this arrangement. |
| A candidate repeating the identical `issue`/`example/governance-fixture#101` pair | **Invalid.** Different revisions would not make the repeated pair unique. |

This establishes validity under the identity rule only; all other format and semantic constraints still apply.

**B — Apply the documented closeout sequence**

The canonical [numbered procedure](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/pr-completion.md:75) gives these steps:

1. Re-read the issue and native relationships; reconcile revisions and inputs, validate exactly one open lifecycle label, and preserve unrelated labels.
2. Confirm accepted review and integration at the actual project target. Run the exact project-owned verification commands there, inspect current outputs against acceptance criteria, and record immutable scope and limitations.
3. Update `Coverage and Satisfaction` mappings/evaluation pointers within authorized scope, preserving immutable accepted evidence and prior identities. **This is the completed pointer edit in the observation.**
4. **Immediately before closure, re-fetch the full native issue contract and relationships after those edits.** Reconcile `updatedAt`, lifecycle, scope, criteria, blockers, and evidence applicability against evaluated inputs. Record the pointer-only editorial edit as semantic reconciliation; timestamp movement alone establishes no equivalence.

   The other actor’s acceptance-criterion edit triggers the explicit instruction to **stop the closing write and refresh the affected approved inputs, review, and verification before rechecking closure eligibility**. The prior pass remains evidence for its original inputs; it does not establish the edited criterion’s satisfaction.

   Closure becomes permitted only after all current applicable obligations pass under explicit applicable authority and the existing lifecycle. Preserve unrelated labels, remove lifecycle labels according to project closed-state policy without adding a done label, then re-fetch actual state/reason, labels, and native closing relationships.
5. Reconcile parent `Obligation Dispositions` and child-evaluation references; child closure alone does not complete the parent.
6. Refresh authorized Project projections from canonical records and evaluations, preserving access limitations.
7. Request checkpoint capture and validate/accept its pair under its separate transaction and commit authority.
8. Preserve the workspace for pending review fixes and follow project/upstream finishing and cleanup ownership.

**Required evidence:** approved current criterion/design/plan inputs, accepted applicable review, exact integrated delivery identity, fresh passing verification, available immutable evidence, and no outstanding applicable obligations. The invented observation supplies no refreshed evidence after the criterion edit, so **closing remains prevented**.

**Exact procedural limit:** step 4 specifies refresh followed by rechecking eligibility, but does not name a numbered restart point. It also supplies no atomic revision-conditioned closing mechanism. Neither should be invented.

**C — Render the shipped observations**

These are excerpts of the existing `sp-bp-checkpoint/v1` records, preserving their exact field values.

| Field | Partial example: E1 | Stale example: issue observation |
| --- | --- | --- |
| `capture.id` | `fixture-C1-partial` | `fixture-C1-stale` |
| `capture.status` | `partial` | `stale` |
| `kind` | `evidence` | `issue` |
| `id` | `E1` | `example/governance-fixture#101` |
| `initial_revision` | `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb` | `2026-10-01T12:00:00Z` |
| `final_revision` | `null` | `2026-10-01T12:10:30Z` |
| `result` | `unavailable` | `changed` |
| `approval_ids` | `[]` | `[]` |
| `details` | “Required evidence E1 is unavailable; its final revision could not be checked.” | “Issue revision changed during capture; its body and native relationships require reconciliation.” |

Sources: [partial E1 recheck](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-partial-example.json:56), [stale issue recheck](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-stale-example.json:11).

For the readable account:

- **Partial:** E1 has `availability=unavailable` and `content=null`; its final identity was not observed. EV1 is **UNKNOWN / unreconciled**. Missing issue page 2 independently prevents complete capture.
- **Stale:** the issue observation changed during capture. No semantic reconciliation approval is recorded. EV1 is **UNKNOWN / unreconciled**, while the original S1/B evidence remains preserved.

**There is no contradiction between these shipped rechecks’ results, revisions, and details.** Both examples retain a raw issue-body SATISFIED claim that conflicts with their supported UNKNOWN evaluations. The [readable contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-state-template.md) requires disclosing both, without promoting the body claim into accepted satisfaction.

Neither diagnostic may replace the accepted pair as complete/current. The deadline and prior approval supply no missing observation, reconciliation, or verification evidence. No live queries or mutations were performed.