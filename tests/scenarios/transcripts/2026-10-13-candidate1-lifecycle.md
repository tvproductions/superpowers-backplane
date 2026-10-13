The sequence is **repair to review → active → blocked → active**, provided each gate is supported. The deadline, maintainer’s urgency, and preparation already spent do not waive those gates. All commands below are hypothetical; none were executed.

The designated [native issue contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md) requires exactly one lifecycle label on an open tracked issue.

Before any authorized repair or transition, fetch the complete issue:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Fetch discussion when needed to establish review requests, approvals, or blocker evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

Before first lifecycle use in the repository, inspect `gh label list --repo example/widgets` and verify all six lifecycle labels and their meanings. Do not silently create missing labels.

1. **Repair the invalid initial state first.** Both `backplane:review` and `backplane:active` are invalid together. The supplied facts identify active as accidental and review as the prior valid state. Remove only the accidental label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Re-fetch and verify the labels are exactly `security` and `backplane:review`. Record the repair rationale if existing evidence does not already establish it. Do not collapse this repair into the subsequent rework transition.

2. **Return review to active for implementation changes.** The review request supplies the transition evidence. Re-read and reconcile the revision, then swap labels in one invocation:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Do not merely remove review: that would leave zero lifecycle labels. Keep the issue open and preserve its implementation workspace. Continue under the current approved design and plan; changed scope or design requires reconciliation and the appropriate planning workflow.

3. **Enter blocked when the external condition stops rework.** Record the concrete blocker, the prior valid state, and the observable release condition. The placeholders below require actual facts:

   ```sh
   gh issue comment 24 --repo example/widgets --body 'Blocked: <concrete external condition and evidence>.
   Resume target: backplane:active
   Release condition: <observable condition and required evidence>.'
   ```

   Preserve native dependency relationships when the blocker is represented by another issue. After re-reading and reconciling the comment’s revision change:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

4. **Resume only after resolution and gate revalidation.** Re-read the complete issue and native blockers. Verify release evidence and every entry gate for the recorded active target: executable leaf contract, approved current design and plan, selection/execution authority, and resolved blockers.

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   Record resolution and revalidation evidence when it is not already represented by native relations or committed artifacts. If active is no longer valid, use **designing or backlog according to current facts**; never guess a former state.

Before each mutation, reconcile `updatedAt` drift against consumed issue/design/plan revisions. After each mutation, re-fetch and verify exactly one expected lifecycle label and unchanged unrelated labels. These targeted edits preserve `security` throughout.

**Fail closed** on zero or multiple lifecycle labels until an evidence-supported repair is established; missing required fields, references, approvals, or compatible capabilities; unresolved revision drift; unclear mutation authority; unresolved blockers; or failed resume gates. A failed post-edit verification also stops further transitions.

This probe supplies lifecycle facts but not the complete issue contract or revision evidence, so these are conditional command shapes, not a claim that real execution is eligible. “Merged-ready” does not establish completion: accepted integration and fresh project verification remain required before closing completed.