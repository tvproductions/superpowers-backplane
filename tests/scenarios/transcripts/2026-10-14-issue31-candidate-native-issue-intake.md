**I would not start implementation of #42. Its immediate disposition is blocked by #37, with revision reconciliation also required before execution.** The deadline, maintainer’s request, and prepared worktree do not satisfy those gates.

This follows the designated [candidate skill](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/SKILL.md) and its references. No live queries, mutations, helpers, or agent dispatch were performed. Every command below is proposed only; variables represent values established from the actual repository and evidence.

1. **Read the complete native issue context before any transition.**

   In the real workflow, I would verify authentication and existing lifecycle labels, then retrieve #42, #37, and the native epic parent:

   ```sh
   gh auth status
   gh label list --repo "$sp_bp_repo" \
     --json name,description,color

   gh issue view 42 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view 37 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view "$sp_bp_parent_number" --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Retrieve necessary approval or blocker discussion with `gh issue view … --comments`. Missing fields or incomplete relationships remain unknown; do not substitute Markdown checklists for native edges.

   Being an epic’s child does not establish that #42 is an executable leaf. Verify that it has no children and contains Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

2. **Reconcile the body edit against the approved spec and plan.**

   Read both committed artifacts and their approval identities. Compare the current issue semantics with the issue URL and `updatedAt` consumed by the plan:

   | Edit classification | Decision |
   |---|---|
   | Editorial and already covered | Record semantic equivalence; retain the approved plan. |
   | Acceptance/scope change covered by the spec but absent from the plan | Revise and obtain approval for the plan. |
   | Design change | Return to Superpowers brainstorming and specification approval, then revise the plan. |
   | New blocker | Record it and maintain blocked state. |

   A changed timestamp triggers comparison; it neither automatically invalidates the plan nor establishes equivalence. I would reuse settled approved design rather than repeat brainstorming.

   The fixture does not supply the edit’s content or current label, so I would not invent either.

3. **Propose `backplane:blocked`, preserving native relationships and unrelated labels.**

   For an open issue, first require exactly one valid lifecycle label. Zero or multiple lifecycle labels require authorized repair before another transition.

   Re-read #42 immediately before the write and reconcile any further drift. For a valid non-blocked current label:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_label" \
     --add-label backplane:blocked

   gh issue comment 42 --repo "$sp_bp_repo" --body \
   "Blocked by native dependency #37.
   Resume target: $sp_bp_resume_label
   Release condition: acceptable evidence resolves #37, the post-plan issue edit is reconciled with approved design and a current approved plan, and every entry gate for the resume target is revalidated."
   ```

   `$sp_bp_resume_label` must name the last evidenced valid state. I would not assume it was ready. If reconciliation invalidates that target, use designing or backlog according to the established facts. If #42 is already correctly blocked, retain the label and reconcile its recorded release conditions.

   Re-fetch the full issue afterward and verify the expected lifecycle label, preserved unrelated labels, and unchanged native parent/dependency edges. Do not remove the #37 edge merely to start sooner.

4. **Begin execution only after all eligibility gates pass.**

   #42 must be open, an executable leaf, contract-complete, governed by approved design and a current approved plan, free of unresolved blockers, and carry `backplane:ready`. #37’s closure alone is insufficient without acceptable prerequisite evidence.

   Once those gates pass:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:blocked \
     --add-label backplane:ready
   ```

   This command applies only when ready is the revalidated resume target. Otherwise return to designing/backlog first.

   Selection alone changes no label. Re-read again, verify the prepared workspace’s identity, authorization and clean baseline, then transition **when the first execution task actually begins**:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:ready \
     --add-label backplane:active
   ```

   Follow the approved Superpowers execution method, artifact-appropriate TDD, review, verification, and branch finishing. Use exact project-owned checks; no runtime or test framework is inferred. Preserve the prepared worktree while blocked. This repository’s #31-only worktree/bookkeeping exceptions do not authorize #42 mutations or helpers writing to `.superpowers/`.

5. **Submit to review; close only after verified integration.**

   Implementation, required review, and passing worktree verification support submission:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:active \
     --add-label backplane:review
   ```

   Use neutral `Refs #42` while integrated evidence is pending. Review-requested implementation changes return review → active. Inspect the actual PR:

   ```sh
   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Close only after accepted integration at the project’s actual target, fresh required checks there, and accepted evidence satisfying every applicable criterion against reconciled inputs. Record exact delivery, requirement, review, and evidence identities; immediately re-read #42 before closure.

   ```sh
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:review
   ```

   Then verify actual state/reason, labels, and native closing relationships. Add no done label. Automatic closure ahead of verification must be reported as actual tracker state with outstanding obligations; it does not prove satisfaction or authorize unrequested reopening.

Project rules govern constraints; the issue owns current scope and lifecycle; the approved spec owns design; the current issue-bound plan owns execution; accepted immutable evidence establishes satisfaction. Closing #42 does not automatically complete its epic or authorize a release.