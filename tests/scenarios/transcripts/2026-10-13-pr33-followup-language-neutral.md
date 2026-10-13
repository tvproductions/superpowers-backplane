Using the designated candidate and its required intake, binding, closeout, and governance references, I would use this workflow. Commands below are illustrative; none were run.

1. **Intake and validate #12.**

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh label list --repo example/widgets
   ```

   Fetch comments only if approval, discussion, blockers, or evidence requires them. Validate all six lifecycle label definitions and exactly one lifecycle label on #12: `backplane:ready`, preserving unrelated labels.

   Confirm the executable body contains Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. Use native `parent` for epic #3 and native relationships for children and dependencies. Execute leaf #12; its parent is a continuity node.

   The supplied facts support eligibility. Maintainer selection alone changes no label.

2. **Bind the existing authorities and start execution.**

   Use the approved issue body as bounded design authority. The current approved committed plan must record the issue URL, consumed `updatedAt`, design authority, acceptance criteria, verification seams, and exact command `cargo test --workspace`. Do not repeat approved design or planning.

   Re-read the complete issue immediately before starting. Timestamp drift requires semantic reconciliation: covered editorial changes may proceed with a record; scope or acceptance changes may require plan approval; design changes return to brainstorming; new blockers require blocking.

   When the first execution task actually begins:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Re-fetch and verify the expected lifecycle label and preserved unrelated labels.

3. **Hand off to Superpowers and submit.**

   Follow project isolation rules, then the applicable Superpowers execution workflow, TDD, review, verification, and branch finishing. Backplane supplies issue continuity; the approved plan supplies execution authority.

   After implementation, required review, and passing worktree verification support submission, submit a PR naming #12, the approved design/plan revisions, criterion contributions, review evidence, and verification result. Use neutral `Refs #12` while integrated verification remains pending.

   Re-read and reconcile the issue before transitioning:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   Re-fetch afterward. Requested implementation changes move `review → active`. A concrete blocker moves any open state to `blocked`, with a recorded resume target and release condition; resumption revalidates every target entry gate.

4. **Verify integration before closure.**

   The sole project verification command is:

   ```sh
   cargo test --workspace
   ```

   Run it before submission and freshly at the accepted integrated target before completion. Inspect actual output and acceptance evidence, recording the tested commit. Introduce no Python or pytest requirement.

   Inspect actual PR facts:

   ```sh
   gh pr view <PR_NUMBER> --repo example/widgets \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   `review → closed/completed` requires accepted review, accepted integration, and fresh passing evidence for every applicable obligation, under applicable closure authority. A PR, merge, closing keyword, or automatic closure alone proves no satisfaction.

   Failed checks mean **UNSATISFIED**; missing checks or acceptance evidence mean **UNKNOWN**. Report premature automatic closure accurately and propose authorized recovery. Completing #12 does not automatically complete epic #3; its remaining obligations need separate accounting. Checkpoint capture, cleanup, and release retain their separate authorization gates.