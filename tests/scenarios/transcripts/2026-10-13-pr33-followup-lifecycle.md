The sequence is **repair to `review` → `active` → `blocked` → recorded `active` resume target**, preserving `security` throughout. These are hypothetical command shapes; none were executed.

The [native issue contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md) requires repair before any transition. The [Superpowers binding](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md) requires evidence for rework and resumption. The deadline, maintainer’s urgency, and day already spent preparing the PR waive no gates.

Before first lifecycle use, inspect label definitions:

```sh
gh label list --repo example/widgets
```

All six lifecycle labels must exist with matching meanings. Missing labels require separately authorized creation.

Before **each write**, fetch the complete issue context:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read comments when needed for approval, blockers, or evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

Compare against the expected revision and reconcile any `updatedAt` drift semantically. After each edit, repeat the full query and verify the expected lifecycle label and unchanged unrelated labels.

1. **Repair the invalid initial state.** Two lifecycle labels are invalid. Stop ordinary transitions; use the supplied fact that `active` was accidental and the implementation was submitted for review to restore exactly one label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Verify labels are now `security` and `backplane:review`. This repair is separate from returning to rework. Record the repair rationale in a comment if existing evidence does not already explain it.

2. **Return review to implementation rework.** Review’s request for implementation changes supports `review → active`, provided current design and plan remain valid:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Remove and add in the same invocation; removing `review` alone would leave zero lifecycle labels. Keep the issue open, preserve the implementation workspace, and follow the applicable Superpowers rework, TDD, review, and verification discipline. If the requested change invalidates design or plan authority, reconcile that authority instead of proceeding immediately.

3. **Enter blocked when the external condition stops progress.** Record the concrete blocker, release condition, and prior valid state:

   ```sh
   gh issue comment 24 --repo example/widgets --body \
   'Blocked: <actual external condition and owner/reference>.
   Resume target: backplane:active
   Release condition: <specific required resolution evidence>.'
   ```

   Use native dependency relationships when an actual blocking issue exists; prose does not replace those edges. Re-read after the comment, reconcile its revision change, then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

4. **Resume only after resolution and gate revalidation.** Verify acceptable resolution evidence and every entry gate for the recorded target: current approved design/plan, reconciled issue semantics, executable scope, resolved native blockers, and authority to continue execution. Record resolution evidence when it is not already represented natively or in committed artifacts:

   ```sh
   gh issue comment 24 --repo example/widgets --body \
   'Blocker resolved: <evidence reference>.
   Revalidated active resume gates: <current authority and revision references>.'
   ```

   Re-read and reconcile again, then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   Resolution alone does not trigger automatic resumption. If `active` is no longer valid, choose `designing` or `backlog` from supported current facts; never guess a former state.

**Fail closed** on zero or multiple lifecycle labels until an evidence-supported repair is established; missing required references, intake fields, permissions, approval, or gate evidence; unreconciled revision drift; an unknown resume target; or a post-edit verification mismatch. An unresolved blocker keeps the issue blocked. This read-only probe authorizes no real writes.

Every edit targets only lifecycle labels, leaving `security` untouched. “Merged-ready” does not establish completion: accepted integration and fresh project-owned verification are still required before completed closure, and release publication has separate authority.