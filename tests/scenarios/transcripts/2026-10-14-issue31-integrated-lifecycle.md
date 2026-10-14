The sequence is **invalid → review → active → blocked → active**, provided each gate is supported. The release deadline, maintainer’s urgency, and day already spent preparing the PR do not waive those gates. These are hypothetical command shapes; none were executed.

The governing rules are the candidate’s [native issue contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md) and [Superpowers binding](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md).

Before an authorized real operation, require authenticated, compatible `gh`, operational independent Superpowers, and inspect the repository’s six lifecycle labels:

```sh
gh auth status
gh label list --repo example/widgets
```

Before every mutation, fetch the complete contract and reconcile `updatedAt` against the consumed revision. Repeat this query afterward to verify the resulting state and preserved unrelated labels:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read comments when needed for review instructions, approval, blockers, or evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

1. **Repair the invalid initial state first.** Two lifecycle labels are invalid. Stop ordinary transitions. The supplied facts identify `review` as the valid state and `active` as accidental, so an authorized repair removes only the accidental label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Verify the labels are exactly `security` and `backplane:review` before proceeding. Do not combine repair with the subsequent transition.

2. **Return review to implementation rework.** The review’s requested implementation changes support `review → active`:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Removing `review` alone would leave another invalid state. Preserve the implementation workspace and continue the approved plan with appropriate TDD, review, and verification. If the requested changes invalidate design or plan semantics, reconcile those authorities instead of immediately implementing under the old plan.

3. **Enter blocked when the external condition stops progress.** Record the concrete blocker, release condition, and prior valid state. Substitute actual facts into this comment:

   ```sh
   gh issue comment 24 --repo example/widgets --body \
   'Blocked: <concrete external condition>.
   Resume target: backplane:active
   Release condition: <specific required resolution evidence>.'
   ```

   Re-read after the comment, reconcile its revision change, then replace the lifecycle label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

   Use native dependency relationships when the blocker is represented by an issue; comments do not replace those relationships.

4. **Resume only after resolution and gate revalidation.** Revalidate the recorded `active` target: current approved design and plan, complete executable issue contract, reconciled revisions, resolved native blockers, and authorized continuation of execution. Then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   If `active` is no longer valid, use `designing` for required design/plan work or `backlog` for deferral, according to evidence. Never guess the resume state.

Every ordinary transition removes and adds lifecycle labels in **one edit invocation**. None of these commands removes `security`; verify it and all other unrelated labels remain unchanged.

**Fail closed** on zero or multiple lifecycle labels until repaired; ambiguous repair authority or intended state; missing required references, contract fields, authentication, compatibility, or evidence; unreconciled revision drift; unresolved blockers; missing resume target or release condition; or failed target-entry gates. A failed post-write verification also stops further transitions.

The fixture does not supply the complete contract or approvals, so these are conditional decisions, not a verified execution authorization. “Merge-ready,” PR preparation, or a deadline does not establish satisfaction: completed closure requires accepted integration and fresh project-owned verification.