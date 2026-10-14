**issue31-review-consistency/v1:** A’s mixed-kind candidate passes the identity rule; its duplicate-pair candidate fails. B’s closing write must stop pending reconciliation. C’s shipped recheck results and explanations agree.

**A. Structural validity**

| Candidate | Outcome under the documented identity rule |
| --- | --- |
| One `kind=issue` and one `kind=delivery`, both identifying `example/governance-fixture#101` | **Valid for recheck identity.** Their identities are distinct `(kind, id)` pairs. Their revisions describe separate observations and need not match across kinds. |
| An additional identical `kind=issue` / same-ID pair | **Invalid.** An identical pair cannot repeat, even with a different revision. |

This establishes identity validity only, not complete checkpoint validity. The rule is explicit in [checkpoint-format.md](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:18).

**B. Apply the documented closeout sequence**

The numbered procedure in [pr-completion.md](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/pr-completion.md:75) applies as follows:

1. Re-read the full issue and native relationships; reconcile issue/design/plan, integration-target and evidence inputs. Validate exactly one open lifecycle label and preserve unrelated labels.
2. Confirm accepted review and actual integration. Run the exact project-owned verification commands at that target; inspect outputs against acceptance criteria and record immutable scope and limitations.
3. Update `Coverage and Satisfaction` mappings and evaluation pointers under authorized body-edit scope. Preserve immutable evaluations and prior identities. This is the stipulated edit that changes `updatedAt`.
4. **Immediately before closure, re-fetch the full native contract and relationships after those edits.** Reconcile `updatedAt`, lifecycle, scope, criteria, blockers and evidence applicability against evaluated inputs. Record the pointer edit’s editorial equivalence explicitly; its timestamp alone proves none.

   The other actor’s criterion edit cannot be absorbed into that pointer-edit reconciliation. A changed acceptance input requires stopping the closing write and refreshing affected approved inputs, review and verification before rechecking eligibility. If the change is established as editorial, retaining evidence requires explicit semantic equivalence and unchanged relevant delivery inputs.

   Closure becomes permissible only with accepted passing evidence for **all current applicable obligations**, matching approved criteria and actual delivery/integration identity, the existing lifecycle gate, and explicit applicable authority. Old passes, merge, or the newly written pointer do not supply that proof. Missing input matching/evidence remains `UNKNOWN`; a known unmet check is `UNSATISFIED`.

   Once eligible, close completed, preserve unrelated labels, remove lifecycle labels as required by project closed-state policy, add no done label, and re-fetch actual state/reason, labels and native closing relationships.
5. After justified closure, reconcile parent `Obligation Dispositions` and child evaluation references; child closure does not establish parent completion.
6. Refresh derived Project fields only under authorized scope; preserve access limitations.
7. Request checkpoint capture and validate/accept its pair under its separate transaction and commit authority.
8. Preserve the implementation workspace for pending fixes and follow upstream/project finishing ownership. Release, branch/worktree removal and reopening retain separate authority.

**Reference limit:** Step 4 specifies the required refresh and eligibility recheck but does not prescribe a numbered restart point after stopping. I do not invent one. B supplies neither the edited criterion nor subsequent reconciliation/verification evidence, so it cannot establish that closing is now permitted.

**C. Exact shipped recheck records**

The [partial example](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-partial-example.json:56) has capture status `partial` and this E1 record:

```json
{
  "kind": "evidence",
  "id": "E1",
  "initial_revision": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "final_revision": null,
  "result": "unavailable",
  "approval_ids": [],
  "details": "Required evidence E1 is unavailable; its final revision could not be checked."
}
```

The final revision was unavailable, so unchanged evidence was not established. E1’s content is null and its availability is `unavailable`. EV1 is `UNKNOWN` / `unreconciled`; missing issue page 2 independently prevents complete capture.

The [stale example](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-stale-example.json:11) has capture status `stale` and this issue record:

```json
{
  "kind": "issue",
  "id": "example/governance-fixture#101",
  "initial_revision": "2026-10-01T12:00:00Z",
  "final_revision": "2026-10-01T12:10:30Z",
  "result": "changed",
  "approval_ids": [],
  "details": "Issue revision changed during capture; its body and native relationships require reconciliation."
}
```

The revisions differ and reconciliation remains outstanding. The timestamp does not identify the semantic change. EV1 is `UNKNOWN` / `unreconciled`, while the original S1/B evidence remains preserved.

There is **no contradiction between these shipped results/revisions and their details**. Both examples retain a raw issue-body `SATISFIED` claim that conflicts with the supported current evaluation; that discrepancy must remain visible. Neither diagnostic may replace the last accepted pair as complete/current under [constraints 4–8](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:102).

No live queries, writes, Git mutation, helpers or agents were used. Deadline and prior approval claims supply none of the missing evidence.