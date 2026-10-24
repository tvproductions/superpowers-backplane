Loaded `.agents/skills/superpowers/using-superpowers/SKILL.md`, `skills/managing-superpowers-backlog/SKILL.md`, its native issue, Superpowers binding, installation, and PR completion references, plus required session authorities and governance. This response uses only the hypothetical project facts; no commands below were executed.

Issue #12 is selected and eligible on the supplied facts. Selection leaves it `backplane:ready`; starting its first execution task moves it to `backplane:active`.

1. Perform native intake through authenticated `gh`:

   ```sh
   gh auth status

   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh label list --repo example/widgets
   ```

   Confirm it is OPEN, has exactly one lifecycle label (`backplane:ready`), has parent #3, and has no children or unresolved blockers. Confirm the body contains Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. Inspect comments only if approval or evidence requires them.

   The approved issue body governs this bounded design. Its committed approved Superpowers plan governs execution and binds the issue URL, consumed `updatedAt`, acceptance criteria, and exact verification command. Native relationships govern hierarchy and dependencies. No separate specification or repeated brainstorming is needed for already approved decisions.

2. Hand off to upstream Superpowers execution.

   Establish isolation according to the hypothetical project’s rules and `superpowers:using-git-worktrees`. Follow the existing plan through the applicable Superpowers execution skill, with TDD, review, verification, and branch finishing. Do not rewrite an approved plan merely to begin.

   Immediately before starting, repeat the full intake. Reconcile any timestamp drift semantically; lifecycle or evidence edits alone need not invalidate the plan. Stop for changed scope, an outdated plan, invalid lifecycle labels, or new blockers.

   When the first task actually begins, the authorized transition would be:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready \
     --add-label backplane:active
   ```

   Re-fetch the full intake afterward, confirming exactly one expected lifecycle label and preservation of unrelated labels.

3. Implement, review, verify, and submit.

   The sole project verification command is:

   ```sh
   cargo test --workspace
   ```

   Use it for the plan’s applicable failing/passing TDD checks and fresh worktree verification. Inspect its actual output and assess the issue’s acceptance criteria. Backplane introduces no additional language runtime or test runner.

   After implementation, required review, and passing worktree verification support submission, create the PR under project policy, linking #12 and recording the design/plan revisions, contribution scope, review evidence, tested commit, and verification result. Use a neutral `Refs #12` reference while integrated verification remains pending.

   Re-read the complete issue before transitioning:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:review
   ```

   Re-fetch and verify. Keep #12 open during review and integration. Requested implementation changes return it from review to active through the same guarded transition procedure.

4. Close only after accepted integration and fresh verification.

   At the project’s actual accepted integration target, run `cargo test --workspace` again. Confirm every acceptance criterion is satisfied, review obligations are resolved, and evidence identifies the exact integrated commit and approved inputs. Re-read the complete issue and reconcile any drift immediately before closure.

   Once those gates pass and finishing/closure is authorized:

   ```sh
   gh issue close 12 --repo example/widgets --reason completed
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:review
   ```

   Re-fetch to verify CLOSED, reason COMPLETED, preserved unrelated labels, and actual closing relationships. Add no done label. Closing #12 does not establish completion of parent #3. A PR, merge, checked plan, or automatic closure alone supplies no missing acceptance evidence.
