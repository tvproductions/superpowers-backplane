This is a simulation: no live queries, mutations, helpers, or agents. I read the designated candidate plus its native issue contract, Superpowers binding, PR completion, governance, and installation references.

1. **Intake and eligibility**

   The proposed native intake is:

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Fetch comments only if approval, discussion, blockers, or evidence requires them. Before first lifecycle use, inspect `gh label list --repo example/widgets` for the six prescribed labels and their meanings; do not silently create labels.

   Validate that #12 is open, has exactly one lifecycle label (`backplane:ready`), has parent #3, has no children or unresolved blockers, and has the complete executable body: Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

   Its approved body supplies bounded design authority. Confirm that its current approved plan records the issue URL, consumed `updatedAt`, design authority, acceptance criteria, and exact verification command. The maintainer has selected #12; selection alone changes no label.

2. **Start and Superpowers handoff**

   Re-read #12 immediately before execution. Timestamp drift requires semantic reconciliation: editorial changes may be recorded as covered; changed scope or acceptance may require plan approval; changed design returns to brainstorming; a new blocker requires a blocked transition.

   Hand off the approved issue design and committed plan to upstream Superpowers. Preserve the approved decisions without repeating brainstorming. Follow project isolation rules, then the applicable execution skill, TDD, review, verification, and branch finishing. Do not introduce a runtime or testing framework.

   When the first execution task actually begins, the proposed transition is:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Every transition requires a fresh read, revision reconciliation, preservation of unrelated labels, and a re-fetch confirming the resulting label state.

3. **Implement and submit**

   The sole project verification command is:

   ```sh
   cargo test --workspace
   ```

   Run it freshly in the implementation worktree and inspect its output before claiming a pass. Submission also requires acceptance evidence and the relevant Superpowers review.

   Once those gates support submission:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   The PR records issue/design/plan revisions, criterion contributions, review evidence, and verification results. Use neutral `Refs #12` while integrated evidence is pending. Requested implementation changes return `review → active`. A concrete blocker uses `blocked`, recording the resume target and release condition.

4. **Closure**

   Submission does not complete #12. Require accepted review, actual integration at the project’s target, satisfied acceptance criteria, and a fresh passing `cargo test --workspace` at that integrated commit. Bind evidence to the exact approved inputs and tested commit.

   Only then, under applicable closure authority, use:

   ```sh
   gh issue close 12 --repo example/widgets --reason completed
   ```

   Re-fetch actual state, reason, labels, and closing relationships. Add no done label. Closing #12 does not complete epic #3; assess its remaining obligations separately. Missing checks mean UNKNOWN, failed checks mean UNSATISFIED, and automatic closure proves neither satisfaction nor authorization to reopen.