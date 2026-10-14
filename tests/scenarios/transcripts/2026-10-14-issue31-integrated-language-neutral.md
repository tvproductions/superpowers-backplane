Using the designated candidate’s intake, binding, installation, governance, and PR-completion references, I would follow this sequence. Commands below are illustrative; none were run.

1. **Intake and eligibility.** Require authenticated `gh` and operational, independent Superpowers. Fetch all 15 native fields:

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Confirm #12 is open, carries exactly one lifecycle label—`backplane:ready`—and has a complete executable body: Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. Validate the approved design and current approved plan. Parent #3 expresses decomposition; it is not a blocker. Empty children and resolved blockers support leaf eligibility.

   Before first repository use, inspect `gh label list` for all six lifecycle labels and their meanings; do not silently create missing labels. Fetch comments only if needed for approval or evidence.

2. **Selection and start.** The maintainer has selected #12. Selection alone changes no label. Re-read the full intake before execution and compare `updatedAt` with the plan’s recorded revision. Drift requires semantic reconciliation: covered editorial changes can proceed with a record; missing scope/acceptance work requires plan revision and approval; design changes return to brainstorming; new blockers require blocking.

   When the first execution task actually begins:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Re-fetch to confirm exactly one expected lifecycle label and preserved unrelated labels.

3. **Superpowers handoff.** Use `superpowers:using-superpowers`, then the applicable isolation and execution workflow. Pass the issue URL/revision, approved issue-body design, committed approved plan, acceptance criteria, and exact verification command. Execute through Superpowers execution, appropriate TDD, review, verification, and branch finishing. Existing approved decisions do not require repeated brainstorming or rewriting the plan. Missing or changed design does.

4. **Implementation and submission.** Use the project’s sole verification command:

   ```sh
   cargo test --workspace
   ```

   Inspect its output and establish acceptance-criterion coverage. Add no Python runtime or substitute test framework. Once implementation, required review, and worktree verification support submission, create the PR through `gh` and transition:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   Apply the same re-read/reconciliation/re-fetch safeguards. Requested implementation changes return `review → active`. A concrete blocker enters `blocked` with its release condition and recorded resume target.

5. **Closure.** Submission leaves #12 open in review. Accepted review, actual integration at the project’s target, fresh `cargo test --workspace` there, and accepted evidence for every applicable criterion must precede justified completion. Record exact requirement, plan, delivery commit, and evidence identities.

   Under applicable closure authorization:

   ```sh
   gh issue close 12 --repo example/widgets --reason completed
   ```

   Verify actual state, reason, labels, and closing relationships. Add no done label. PR creation, merge, and automatic closure alone do not prove satisfaction; missing evidence is `UNKNOWN`, and a known failed applicable check is `UNSATISFIED`. Closing #12 does not establish epic #3’s completion. With the hypothetical’s current facts, implementation and completion remain unverified.