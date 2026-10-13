The sequence is **invalid → review → active → blocked → active**, provided the evidence gates below pass. These are hypothetical command shapes; no live queries or mutations were performed.

Under the [native issue contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md), every open tracked issue must have exactly one lifecycle label.

Before each authorized repair or transition, fetch the complete issue and reconcile its `updatedAt` against the consumed revision:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read comments when needed for review requests, approval, or blocker evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

For actual operation, require authenticated `gh`, operational independent Superpowers, and supported required fields. Before first lifecycle use, inspect `gh label list --repo example/widgets` and verify all six lifecycle labels and their meanings. Missing labels require separately authorized repair.

1. **Repair the invalid initial state first.** Two lifecycle labels are invalid: fail closed on ordinary transitions. The supplied facts identify `backplane:active` as accidental, so restore the evidence-supported review state:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Re-fetch and verify exactly `security` and `backplane:review` before proceeding. This is a repair, distinct from returning to rework.

2. **Return review to active rework.** The implementation-change request supplies the `review → active` exit evidence. Re-read, reconcile revisions, and confirm the approved design/current plan still covers the requested changes:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Reference the review request in a concise comment if existing review/native/committed evidence does not already establish it. Continue Superpowers execution, appropriate TDD, review, and verification. If changed scope invalidates design or plan, resolve that authority through the applicable workflow before implementation.

3. **Enter blocked when the external condition stops rework.** Record the concrete blocker, its owner/reference, the prior valid state, and observable release evidence. Substitute actual facts for the placeholders:

   ```sh
   gh issue comment 24 --repo example/widgets \
     --body 'Blocked: <concrete external condition and owner/reference>.
   Resume target: backplane:active
   Release condition: <specific evidence required to permit rework>.'
   ```

   Then apply the lifecycle change:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

   Preserve native dependency relationships as authoritative when a blocker issue exists.

4. **Resume only after resolution and revalidation.** Verify the recorded release condition, all native blockers, current issue semantics, approved design/current plan, and every entry gate for active rework. Record resolution evidence if it is not already represented:

   ```sh
   gh issue comment 24 --repo example/widgets \
     --body 'Blocker resolved: <evidence reference>. Recorded resume target backplane:active revalidated against <current issue/design/plan revisions and entry evidence>.'

   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   If active is no longer valid, reconcile to `designing` or `backlog` according to current facts; never guess the former state.

After every edit, repeat the full intake query and verify **exactly one expected lifecycle label and unchanged unrelated labels**, including `security`. Use targeted additions/removals; never replace the entire label set.

Fail closed when the lifecycle is invalid until repaired; required context, authority, references, or evidence is missing; revision drift is unreconciled; required CLI fields or permissions are unavailable; the resume target/release condition is unknown; or target entry gates cannot be revalidated. A failed post-edit verification stops further transitions.

The one-hour deadline, maintainer pressure, and day already invested do not waive these gates. “Merged-ready” is not completion: requested changes require rework, and eventual completed closure requires accepted integration and fresh project verification under the [Superpowers binding](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md).