Loaded `.agents/skills/superpowers/using-superpowers/SKILL.md`, repository session authorities, `skills/managing-superpowers-backlog/SKILL.md`, and its native issue, Superpowers binding, installation, PR completion, and governance references. The following is hypothetical; no commands or mutations were performed.

**I would keep #42 open and stop implementation now.** Its unresolved blocker and unreconciled issue revision prevent eligibility. The deadline and prepared worktree do not satisfy either gate.

1. **Fetch the complete native issue context.**

   Substitute the hypothetical repository for `<owner/repo>`:

   ```sh
   gh auth status
   gh label list --repo <owner/repo>

   gh issue view 42 --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view 37 --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Fetch #42’s returned parent with the same fields. Fetch comments if needed to establish approvals, the blocker’s release evidence, or revision history:

   ```sh
   gh issue view 42 --repo <owner/repo> --comments
   gh issue view 37 --repo <owner/repo> --comments
   ```

   Unavailable required fields or incomplete relationships leave eligibility unknown and prevent starting.

2. **Validate authority and reconcile the edit.**

   Project instructions govern constraints, tools, isolation, verification, and integration. The issue owns current scope, acceptance criteria, native relationships, and lifecycle. The approved specification governs design; the current approved plan governs execution. Commits, accepted reviews, and verification establish delivery evidence.

   Compare #42’s current semantics with the issue revision consumed by the committed plan:

   - Editorial change already covered: record explicit reconciliation.
   - Changed acceptance or scope covered by the specification but missing from the plan: revise and approve the plan.
   - Changed design: return to Superpowers brainstorming and specification approval, then revise the plan.
   - Conflicting issue/specification authority: resolve the discrepancy before execution.

   A changed `updatedAt` triggers this comparison; it does not by itself invalidate the plan.

3. **Represent the concrete blocker without guessing the prior state.**

   Require exactly one existing Backplane lifecycle label and preserve unrelated labels. Zero or multiple lifecycle labels require evidence-based repair before any further transition.

   If #37 remains unresolved and #42 is not already blocked, I would simulate the following transition after re-reading #42. `<current-label>` and `<resume-state>` must come from validated facts:

   ```sh
   gh issue comment 42 --repo <owner/repo> \
     --body 'Blocked by native dependency #37. Resume target: backplane:<resume-state>. Release conditions: acceptable evidence resolves #37; reconcile the post-plan issue edit and obtain any required design/plan approval; revalidate every entry gate for the resume target.'

   gh issue edit 42 --repo <owner/repo> \
     --remove-label '<current-label>' \
     --add-label backplane:blocked
   ```

   Remove and add lifecycle labels in one edit, then re-fetch the full issue to verify the expected label, preserved unrelated labels, revision, and relationships. If already blocked, retain that state and reconcile its recorded release conditions. Do not remove the dependency or close #37 merely to permit execution.

4. **Resume only when eligibility is established.**

   #42 must be open, an executable leaf despite its epic parentage, and contain the complete executable issue contract. Its approved design and current approved plan must cover the reconciled issue semantics, every native blocker must have acceptable resolution evidence, and it must carry `backplane:ready`.

   After those gates pass, re-read #42 immediately before starting. Use or validate the prepared worktree according to project isolation rules. At the first execution task:

   ```sh
   gh issue edit 42 --repo <owner/repo> \
     --remove-label backplane:ready \
     --add-label backplane:active
   ```

   Follow upstream Superpowers execution and appropriate TDD, then required review and project-owned verification. Use the project’s exact verification commands; none are supplied by this hypothetical.

5. **Submit, integrate, verify, then close.**

   When implementation, required review, and worktree verification support submission:

   ```sh
   gh issue edit 42 --repo <owner/repo> \
     --remove-label backplane:active \
     --add-label backplane:review
   ```

   Link the PR as contribution evidence, using neutral `Refs #42` while completion remains unproved. Keep the issue open through review and integration. Requested implementation changes return `review` to `active`.

   Close only after accepted integration at the project’s actual target, fresh project verification, and evidence satisfying every current acceptance criterion. Re-fetch and reconcile the full issue immediately before closure:

   ```sh
   gh issue close 42 --repo <owner/repo> --reason completed
   gh issue edit 42 --repo <owner/repo> \
     --remove-label backplane:review
   ```

   Verify actual state, closure reason, labels, and closing relationships afterward. Preserve unrelated labels and add no done label. Child completion does not establish epic completion, and issue closure does not authorize a release. GitHub Projects and IssueOps are not prerequisites.
