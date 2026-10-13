**I would keep #42 open and block execution now.** Its unresolved dependency on #37 makes it ineligible. The later issue-body edit also requires reconciliation with the approved spec and plan. The release deadline and prepared worktree do not change those gates.

I read the designated candidate, its required operation references, and the applicable upstream workflow instructions. All commands below are **proposed only**; no live queries or mutations were performed.

1. **Establish the current issue contract before interpreting “fully specified.”**

   In the hypothetical workflow, I would use:

   ```sh
   sp_bp_repo='OWNER/REPO'

   gh auth status
   gh label list --repo "$sp_bp_repo" --limit 1000 \
     --json name,description

   gh issue view 42 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view 37 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view 42 --repo "$sp_bp_repo" --comments
   gh issue view 37 --repo "$sp_bp_repo" --comments
   ```

   Comments supply approval, revision, or blocker evidence where needed. I would also read the native parent identified by the query.

   Being an epic’s child does not establish that #42 is a leaf: it must have no executable children. Its body must contain Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. Missing fields, inaccessible relationships, or incomplete pagination prevent an eligibility claim.

2. **Reconcile the edited body against the plan’s consumed revision.**

   Read the committed approved spec and plan, their exact revisions, and approval evidence. The plan must bind to #42’s URL and consumed `updatedAt`, design authority, acceptance criteria, and exact project-owned verification commands.

   | Change established by comparison | Decision |
   |---|---|
   | Editorial and already covered | Record semantic equivalence; retain approved spec and plan. |
   | Acceptance/scope change covered by the spec but absent from the plan | Revise and approve the plan before execution. |
   | Changed design | Return to Superpowers brainstorming and specification review, then update and approve the plan. |
   | New unresolved dependency | Block execution and record release evidence. |
   | Consumed revision or comparison evidence unavailable | Freshness remains unknown; do not execute. |

   A changed timestamp triggers comparison; it does not itself invalidate the plan. I would avoid repeating approved design work unnecessarily.

3. **Represent the actual blocker with `backplane:blocked`.**

   First validate that the open issue has exactly one Backplane lifecycle label. Zero or multiple labels require an evidence-supported repair before another transition; preserve unrelated labels.

   Immediately before an authorized write, repeat the full intake, reconcile any new drift, and then use one label-edit invocation:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_label" \
     --add-label backplane:blocked

   gh issue comment 42 --repo "$sp_bp_repo" \
     --body "Resume target: backplane:${sp_bp_resume_state}. Blocked by native dependency #37. Release condition: acceptable evidence resolves #37's prerequisite, and the contract, current issue/spec/plan semantics, approvals, and target entry gates are revalidated before resumption."
   ```

   These variables must come from evidence. The prompt supplies neither the current lifecycle label nor the prior valid state, so I would not invent them. Preserve an established ready resume target only if valid; reconciliation requiring design/plan work routes through designing. An already-blocked issue keeps its substantiated resume record.

   Re-fetch the full issue afterward and verify the expected single lifecycle label and preserved unrelated labels. Do not remove the dependency edge, close #37, or close #42 to meet the deadline.

4. **Start only after eligibility is established.**

   #42 needs all six conditions: open, executable leaf, complete contract, approved design, current approved plan, resolved native blockers with acceptable evidence, and `backplane:ready`.

   After #37 resolves, revalidate the recorded resume target. Where plan/design work remains:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:blocked --add-label backplane:designing
   ```

   Once approvals, contract, and blockers satisfy readiness:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:designing --add-label backplane:ready
   ```

   A valid ready resume target can instead transition directly from blocked to ready. Each write uses the same re-read and post-write verification procedure.

   Reuse the prepared worktree after verifying isolation, repository identity, branch, and a fresh project baseline. Selection alone changes no label. At the first implementation task:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Follow the approved Superpowers execution method, task order, appropriate TDD, review, and verification. Use project-owned tools and commands; do not invent a runtime or bypass project namespace restrictions with an upstream helper.

5. **Submit, integrate, verify, then close.**

   Implementation, required review, and worktree verification support submission:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:active --add-label backplane:review
   ```

   Keep the issue open through review and integration. Requested implementation changes return review to active. Use neutral `Refs #42` while completion evidence is pending.

   Inspect actual delivery state:

   ```sh
   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Close only after accepted integration at the project’s actual target and fresh project-owned checks establish every applicable acceptance obligation against reconciled current requirements. Preserve immutable evidence and the verified delivery commit. Under applicable closeout authority:

   ```sh
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   ```

   Re-fetch state, reason, labels, and closing relationships; apply the project’s closed-label policy without adding a done label. Reconcile parent obligations separately: completing #42 does not complete its epic. Checkpoint capture, workspace cleanup, and release publication retain their own authorization.

The native issue owns current intent and lifecycle; the approved spec owns design; the current approved issue-bound plan owns execution; accepted evidence establishes satisfaction. None of the deadline, worktree, checked tasks, PR, merge, or automatic closure replaces that evidence.