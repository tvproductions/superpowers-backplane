This is a hypothetical workflow only. I read the designated candidate, its directly linked references, and the required governance source. No live queries, helpers, agents, or mutations were used.

1. **Intake and eligibility**

   I would require authenticated `gh` and operational, independently installed Superpowers, then fetch all 15 native fields:

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Confirm an open executable leaf, native parent #3, no sub-issues or unresolved blockers, and exactly one lifecycle label: `backplane:ready`. Preserve unrelated labels. Before first use, inspect `gh label list` for the six lifecycle labels and their meanings; do not silently create missing labels.

   Validate the body’s Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts sections. Confirm the plan is approved and binds the issue URL, consumed `updatedAt`, approved issue-body design, acceptance criteria, and exact verification command. Unavailable required fields prevent eligibility validation.

2. **Selection and start**

   The maintainer has selected #12; selection alone changes no label. Re-fetch before starting and reconcile any timestamp drift semantically. Editorial changes already covered can proceed with recorded reconciliation; changed scope/design requires renewed planning/design approval; a concrete blocker requires `blocked`.

   When the first execution task actually begins, the illustrative transition is:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Re-fetch afterward to verify the expected lifecycle and preserved unrelated labels.

3. **Superpowers handoff**

   Use the approved issue body as bounded design authority and the existing approved plan as execution authority. Do not repeat settled brainstorming or create a replacement specification.

   Follow applicable Superpowers isolation, inline `executing-plans`, TDD, review, verification, and branch-finishing workflows under the hypothetical project’s rules. New design questions return to brainstorming; implementation changes must remain within the approved scope.

4. **Verification and submission**

   The sole verification command is:

   ```sh
   cargo test --workspace
   ```

   Use project-appropriate TDD and inspect current command output. Add no Python dependency or alternative verification framework.

   After implementation, required review, and passing worktree verification support submission:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   Submit the PR with issue/design/plan revisions, criterion contributions, review evidence, verification results, and tested commit identity. Use neutral `Refs #12` while integrated verification is pending. Review-requested implementation changes return `review → active`.

5. **Closure**

   Keep #12 open through review and integration. Completion requires accepted review, integration at the project’s actual target, satisfied acceptance criteria, and a fresh `cargo test --workspace` pass there, tied to the exact integrated commit.

   Only then, under applicable closure authority, close with reason `completed` and re-fetch the actual state, reason, labels, and native closing relationships. PR creation, merge, or automatic closure alone proves no satisfaction. Missing verification is `UNKNOWN`; a known failed check is `UNSATISFIED`.

   Closing #12 does not complete epic #3: every parent obligation needs separate accounting. A blocker records its concrete release condition and `Resume target: backplane:<state>`; resumption revalidates that state’s gates.