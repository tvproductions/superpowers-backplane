The shipped references contain three consistency problems: duplicate recheck identities, a missing pre-closure revision checkpoint in the numbered procedure, and contradictory example explanations. This probe used only permitted file reads; no live queries, writes, Git mutations, helpers, or agents.

**A. Structural validity**

The [format contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:81) says: “IDs are unique in each object collection.” It also prohibits duplicate IDs in arrays. It defines no `(kind, id)` uniqueness exception.

| Candidate | Validity under the written rule |
| --- | --- |
| One `kind=issue` and one `kind=delivery`, both with `id=example/governance-fixture#101` | **Structurally invalid:** the `rechecks` collection repeats an ID. Different kinds and separate observation revisions do not satisfy ID uniqueness. |
| Repeated identical `kind=issue` / `id` pair | **Structurally invalid:** it repeats the ID and the same observation identity. |

The shipped complete example contains the first arrangement. Therefore, its presentation as a complete example conflicts with the written uniqueness constraint. A composite `(kind, id)` rule would distinguish the first candidate from the second, but **that rule is unavailable in the documentation**; I cannot invent it.

**B. Closeout after the body update and concurrent criterion edit**

Applying the [authorized closeout sequence](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/pr-completion.md:77), retaining its numbering:

1. **Re-read and reconcile inputs.** The initial reconciliation establishes the inputs before the closeout writes. Validate exactly one open lifecycle label and preserve unrelated labels.
2. **Confirm review/integration and run fresh project verification.** The invented observation supplies a verified result for the previously evaluated criteria and delivery.
3. **Update `Coverage and Satisfaction`.** This has occurred and changes `updatedAt`. Preserve immutable accepted evaluations and their original identities.
4. **Close completed only once all obligations pass under applicable authority.** **The closing write is currently prevented.** Another actor’s criterion edit means the earlier evaluation has not been shown applicable to the current criterion. Authorization to close does not supply that missing evidence. The step’s prescribed re-fetch occurs **after** closure and cannot establish the pre-write condition.
5. **Reconcile parent dispositions and child-evaluation references** after justified closure; child closure alone cannot complete the parent.
6. **Refresh derived Project fields** under their authorized scope; denied access remains a limitation.
7. **Request and separately validate/accept the checkpoint operation.** Closure does not establish checkpoint completeness.
8. **Preserve the workspace for pending fixes and follow finishing ownership.** Release, cleanup, and reopening retain their separate authority requirements.

The governing [issue revision rules](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md:125) require fetching again **before mutation**, reconciling timestamp drift, and verifying the expected revision. That guard requires inspecting the current body and relationships before the closing write. The closeout’s own body edit cannot be assumed to explain every intervening change.

Evidence that could permit closure is:

- For an editorial change: recorded, explicit semantic equivalence and unchanged relevant delivery inputs, with matching accepted evidence.
- For changed acceptance behavior: reconciled approved criterion/design/plan inputs and accepted review plus fresh verification covering every affected obligation at the actual integration target.
- In either case: current revision/lifecycle/relationship observations and applicable closure authority.

Until applicability is established, affected current satisfaction is **UNKNOWN**. A known failed applicable check is **UNSATISFIED**. Preserve the earlier pass against its original inputs.

**Exact procedural gap:** the numbered procedure does not specify a pre-close re-read after step 3, advancement of the expected revision following its own edit, or a numbered reconciliation/revalidation loop for an intervening edit. The general contract supplies the guard, but the requested exact numbered continuation is unavailable. I cannot silently insert “step 3½” or declare an undocumented restart procedure canonical.

**C. Rendering the shipped rechecks**

These are diagnostic excerpts using the shipped readable field names, not validated replacement checkpoint pairs.

[Partial example](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-partial-example.json:56):

```text
Mode / capture status / origin: issues-only / partial / invented-fixture
Scope and completeness: Incomplete; issue page 2 is omitted.
Recheck kind=evidence, id=E1:
  initial_revision: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
  final_revision: null
  result: unavailable
  approval_ids: []
  details: Embedded fixture evidence unchanged.
```

Supporting explanation: E1’s evidence record is unavailable, its content is null, and its limitation states that required verification material is unavailable. Consequently, EV1 is recorded as **UNKNOWN / unreconciled**.

**Contradictions:** the recheck’s `details` claims unchanged evidence despite an unavailable final observation. The graph recheck also claims all selected connections were enumerated and compared despite the missing page. Preserve these discrepancies; neither statement establishes completeness. The raw issue’s SATISFIED claim must remain distinguishable from EV1’s supported UNKNOWN result.

[Stale example](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-stale-example.json:11):

```text
Mode / capture status / origin: issues-only / stale / invented-fixture
Scope and completeness: scope.complete=false; issue reconciliation outstanding.
Recheck kind=issue, id=example/governance-fixture#101:
  initial_revision: 2026-10-01T12:00:00Z
  final_revision: 2026-10-01T12:10:30Z
  result: changed
  approval_ids: []
  details: Fixture full body/native relationships unchanged.
```

Supporting explanation: the example records changed issue observation, a stale capture, and EV1 as **UNKNOWN / unreconciled**, with changed-source reconciliation outstanding.

**Contradiction and evidence gap:** `result=changed` and the stale-source limitation conflict with the unchanged-body/relationships explanation. Different timestamps establish revision drift, but do not identify a semantic change. No available reconciliation approval or changed criterion content resolves that tension. Report the recorded changed result and contradictory explanation together; do not convert it to unchanged or invent the missing delta.

Both diagnostics also inherit A’s duplicate-recheck-ID conflict. Required unavailable evidence, unreconciled drift, and contradictory readable claims prevent accepting either as a complete/current replacement. Retain the last accepted pair. The deadline and prior approval do not resolve these reference gaps.