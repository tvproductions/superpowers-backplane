The sequence is **repair to review → active rework → blocked → active**, provided each gate holds. The one-hour deadline, maintainer pressure, and day already spent preparing the PR do not waive those gates. These decisions follow the designated [native issue contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md) and [Superpowers binding](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md).

All commands below are hypothetical shapes; none were executed.

Before real operations, require authenticated `gh`, operational independent Superpowers, and all six lifecycle labels with their defined meanings:

```sh
gh auth status
gh label list --repo example/widgets
```

Before **each mutation**, and again afterward, fetch the complete issue:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Compare the expected revision and relationships; reconcile changed `updatedAt` against the approved design and current plan. After each edit, verify exactly one expected lifecycle label and unchanged unrelated labels.

1. **Repair the invalid initial state first.** Two lifecycle labels are invalid: fail closed against ordinary transitions. The fixture identifies `active` as accidental and establishes submitted work under review, so retain `review` and remove only the accidental label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Expected labels: `security`, `backplane:review`. This is a repair, separate from the subsequent rework transition.

2. **Return review to active rework.** The review’s request for implementation changes supplies the transition evidence. Remove and add in one invocation:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Expected labels: `security`, `backplane:active`. Do not merely remove `review` and leave zero lifecycle labels. Preserve the implementation workspace and follow Superpowers review reception, execution, TDD, and verification. If the request changes approved scope or design, reconcile and approve the affected authorities before implementing.

3. **Enter blocked when the external condition stops progress.** Record the concrete reason, explicit resume target, and observable release condition. The fixture does not name the blocker, so these slots must be filled from actual evidence:

   ```sh
   gh issue comment 24 --repo example/widgets --body 'Blocked: <concrete external condition preventing rework>.
   Resume target: backplane:active
   Release condition: <specific evidence required to establish resolution>.'
   ```

   Re-fetch after the comment, reconcile its revision change, then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

   Expected labels: `security`, `backplane:blocked`. Keep native dependency relationships authoritative when applicable.

4. **Resume only after resolution and gate revalidation.** Verify the recorded release condition, all native blockers, current issue/design/plan semantics and approvals, and every entry gate for resuming authorized active execution. Record resolution evidence if it is not already represented by native relationships or committed evidence. Then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   Expected labels: `security`, `backplane:active`. If `active` is no longer valid, use `designing` or `backlog` according to established facts; never guess the former state.

**Fail closed** when lifecycle state is invalid before repair; repair intent is ambiguous; required references, fields, permissions, authority, or evidence are unavailable; revision drift remains unreconciled; the blocker’s release condition is unproven; resume target or target gates are unverified; or post-edit verification fails. Stop further transitions and reconcile.

Every command changes only named lifecycle labels, preserving `security`. The issue remains open through rework. “Merged-ready” does not establish completion: completed closure requires accepted integration, satisfied acceptance criteria, and fresh project-owned verification.