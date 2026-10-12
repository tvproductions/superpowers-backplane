All commands below are hypothetical; I performed only skill and reference reads.

1. **Intake and eligibility.** Require authenticated `gh` and an operational, compatible Superpowers installation. Use the prescribed native intake:

   ```text
   gh issue view 12 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Fetch comments only if approval or evidence needs clarification. Verify the complete executable issue contract: Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

   Confirm #12 is open, has exactly one lifecycle label—`backplane:ready`—has native parent #3, no children, and no unresolved blockers. Its approved design and current committed plan make it covered; these gates make it eligible; the maintainer’s choice makes it selected. Parent #3 remains the product continuity node.

   Before first use, inspect `gh label list --repo example/widgets` for all six correctly described lifecycle labels. Missing labels require separately authorized repair.

2. **Start and Superpowers handoff.** Re-fetch #12 immediately before transitioning and compare `updatedAt` with the plan’s consumed revision. Reconcile any drift semantically; a timestamp change alone does not invalidate the plan.

   For bounded work without architectural, cross-cutting, or breaking decisions, retain the approved issue body as design authority. Do not repeat already approved brainstorming. The plan must bind the issue URL, consumed revision, design authority, acceptance criteria, verification seams, and exact command.

   Follow Superpowers workspace isolation, plan execution, TDD, review, verification, and branch finishing. At the first execution task:

   ```text
   gh issue edit 12 --repo example/widgets --remove-label backplane:ready --add-label backplane:active
   ```

3. **Submit.** After implementation, required review, and fresh worktree verification support submission, use `gh` to create the linked PR under the project’s branch policy, then transition:

   ```text
   gh issue edit 12 --repo example/widgets --remove-label backplane:active --add-label backplane:review
   ```

   Submission is already requested; merging is a separate integration decision. Re-fetch before each mutation and afterward verify exactly one expected lifecycle label and unchanged unrelated labels. Preserve committed implementation, review, PR, and verification evidence.

4. **Verification rule.** Use exactly:

   ```text
   cargo test --workspace
   ```

   Run the full command freshly, inspect its output and exit status, and report failures. Use it for the baseline, relevant TDD runs, submission verification, and fresh verification of the integrated target. Check acceptance criteria separately. No Python runtime or additional test framework is implied.

5. **Closure and exceptions.** PR creation leaves #12 open in review. Close as `completed` only after delivery is integrated, acceptance criteria are satisfied, and the integrated target passes fresh verification:

   ```text
   gh issue close 12 --repo example/widgets --reason completed
   ```

   Coordinate automatic PR closure so it cannot bypass that gate. Do not add a done label or automatically close epic #3.

   Review changes return `review → active`. A concrete blocker moves any open state to `blocked`, recording its resume target and release condition; resume only after revalidating the target’s gates. Invalidated design returns to `designing`. Explicit rejection or abandonment uses closure reason `not planned`.