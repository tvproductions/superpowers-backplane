This is a hypothetical walkthrough using the designated [skill](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/SKILL.md) and its contracts. No live queries, mutations, helpers, or agent dispatch occurred.

1. **Intake and validate #12.** The native intake command would be:

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Validate the executable body’s Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. From the fixture, #12 is an open ready leaf under epic #3, with no children or blockers, approved issue-body design, and a current approved committed plan. The maintainer has selected it; selection alone changes no label. Do not invent unspecified field values.

2. **Start execution.** Re-read the full intake immediately before starting. Compare `updatedAt` with the revision consumed by the plan. Timestamp drift requires semantic reconciliation: editorial changes may proceed after reconciliation; changed scope, acceptance, or design requires the appropriate approval; a new blocker prevents execution.

   When the first execution task actually begins:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Preserve unrelated labels, record necessary evidence, and re-fetch to verify exactly one expected lifecycle label. Preparing a worktree does not establish `active`.

3. **Hand off to Superpowers.** Supply issue URL `https://github.com/example/widgets/issues/12`, its consumed revision, the approved issue-body design, committed plan identity, acceptance criteria, and exact verification command. Reuse the approved design and plan; repeat brainstorming or planning only if reconciliation exposes missing or changed authority.

   Follow project-governed isolation, plan execution, TDD with observed RED→GREEN→refactor, required review, verification-before-completion, and branch finishing. The maintainer’s submission request already selects PR submission. Preserve the implementation workspace for review fixes.

4. **Verify and submit.** The sole project verification command is:

   ```sh
   cargo test --workspace
   ```

   Use it for baseline and implementation verification, before submission, and freshly on the accepted integrated target before completed closure. Inspect output and exit status, and evaluate every acceptance criterion. A previous pass or checked plan box supplies no fresh evidence. No Python toolchain is implied.

   Once implementation, required review, and passing worktree verification support submission, submit through `gh pr create`, with issue/design/plan identities, criterion contributions, review disposition, and verification evidence. Then transition:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   Use `Refs #12` while integrated evidence is pending. Review-requested implementation changes return `review → active`. A concrete blocker moves work to `blocked`, with its resume target and release condition recorded.

5. **Explain closure.** Submission leaves #12 open in `review`. Completed closure requires accepted review, actual integration into the project’s target, fresh passing `cargo test --workspace`, and accepted evidence satisfying every applicable criterion against current approved inputs.

   Immediately before an authorized closing write, re-fetch and reconcile revisions and relationships. Close with reason `completed`, remove lifecycle labels while preserving unrelated labels, and verify actual state/reason and closing relationships. No done label is added.

   Merge or automatic closure alone proves no satisfaction. Missing verification remains `UNKNOWN`; a known failed applicable check is `UNSATISFIED`. Closing #12 also does not establish completion of epic #3. The request to start and submit authorizes those steps; explaining closure does not itself authorize merging or closing.