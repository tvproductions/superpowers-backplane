**I would keep #42 open and blocked, and reconcile the body edit before starting implementation.** The release deadline, maintainer seniority, and prepared worktree do not establish eligibility.

This applies the designated [candidate skill](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/SKILL.md), its native issue contract, Superpowers binding, and completion references. All commands below are proposed; none were executed.

1. **Read the complete native issue context.**

   In the hypothetical repository, first read project instructions and confirm authenticated `gh` and an operational independent Superpowers installation. Then:

   ```sh
   sp_bp_repo='OWNER/REPO'
   sp_bp_fields='number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url'

   gh auth status
   gh label list --repo "$sp_bp_repo" --json name,description

   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   gh issue view 37 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   gh issue view 42 --repo "$sp_bp_repo" --comments
   ```

   Read the epic using its actual native parent identity, and inspect approval or dependency evidence where necessary. Missing required fields or incomplete relationship collections prevent an eligibility claim.

   Being an epic’s child does not prove #42 is a leaf. Confirm it has no children and contains Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

2. **Reconcile the edited body against the committed approved artifacts.**

   Read the complete linked specification and plan at their exact approved revisions. Compare the current issue against the issue URL and consumed `updatedAt` recorded by the plan.

   | Observed change | Action |
   |---|---|
   | Editorial and already covered | Record semantic equivalence; retain the approved spec and plan. |
   | Scope or acceptance change covered by the spec but missing from the plan | Revise through `superpowers:writing-plans` and obtain approval of the revised plan before execution. |
   | Design change or conflict with approved authority | Return to `superpowers:brainstorming`, reconcile and approve the specification, then update and approve the plan. |
   | New blocker | Record it and keep execution blocked. |

   I would preserve already approved decisions and avoid repeating blank-slate design. Until the comparison is performed, the plan’s current applicability is **unknown**.

   Authority remains layered: project rules govern constraints; the issue owns current scope, acceptance and lifecycle; the approved spec governs design; the current approved issue-bound plan governs execution; accepted evidence establishes satisfaction. A body edit cannot silently amend approved design.

3. **Record the concrete block without starting execution.**

   #37 remains an unresolved prerequisite on the supplied facts. I would preserve the native dependency and epic relationship.

   Before any transition, re-fetch #42, reconcile revision drift, and verify exactly one Backplane lifecycle label. Zero or multiple lifecycle labels require repair before another transition; preserve unrelated labels throughout. Verify the repository’s six lifecycle labels exist and have correct meanings without silently creating them.

   For an existing single label other than `backplane:blocked`:

   ```sh
   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"

   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_label" \
     --add-label 'backplane:blocked'

   gh issue comment 42 --repo "$sp_bp_repo" --body \
   "Blocked by #37. Resume target: backplane:${sp_bp_resume_state}. Release condition: acceptable evidence resolves #37 and every entry gate for the resume target is revalidated, including reconciliation of the later #42 body edit."

   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   ```

   Here, `sp_bp_current_label` and `sp_bp_resume_state` must come from observed state and evidence of the prior valid state; the prompt does not supply them. I would not invent a former `ready` or `active` state. If already blocked, retain that label and reconcile the recorded reason/resume target.

   After #37 resolves, material revision changes route #42 to `designing`; an unchanged, fully approved contract can return to `ready`. Closure of #37 alone is insufficient if its prerequisite outcome lacks acceptable evidence.

4. **Begin execution only after all eligibility gates pass.**

   Require #42 to be open, an executable leaf, contract-complete, approved in design, covered by a current approved plan, free of unresolved blockers, and labeled `backplane:ready`. The request identifies #42 as the intended work item; selection itself changes no label.

   Preserve and verify the existing worktree’s identity, isolation and baseline instead of recreating it. Before Git mutations, enforce the project’s repository boundary. Execute the approved plan in order using upstream Superpowers and project-owned TDD and verification commands.

   Immediately before the first execution task:

   ```sh
   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"

   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label 'backplane:ready' \
     --add-label 'backplane:active'

   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   ```

5. **Submit, integrate, verify, then close.**

   After implementation, required review and worktree verification support submission, transition `active → review` using the same re-read/edit/re-fetch discipline. Requested implementation changes return `review → active`.

   Inspect actual PR state:

   ```sh
   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Keep #42 open through review and integration. Prefer `Refs #42` while integrated acceptance remains pending. After accepted integration at the project’s actual target, run the exact project-owned checks there and evaluate every current acceptance criterion. Preserve immutable evidence identifying approved inputs, tested delivery commit, results and outstanding obligations.

   **Only when all obligations pass and closeout is authorized:**

   ```sh
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   ```

   Apply the project’s closed-label policy without adding a done label. Reconcile the epic’s obligations separately; closing #42 does not complete the epic. Automatic closure, merge or checked plan tasks cannot supply missing satisfaction evidence. Release publication remains separately authorized.