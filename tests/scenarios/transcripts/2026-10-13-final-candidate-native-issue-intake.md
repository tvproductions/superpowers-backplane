**I would keep #42 open and blocked, and would not start implementation.** The unresolved dependency on #37 prevents eligibility. The later body edit also requires semantic reconciliation with the approved spec and plan. The deadline and prepared worktree do not satisfy either gate.

This is a simulation: no queries or mutations below were executed. I read the designated [skill](skills/managing-superpowers-backlog/SKILL.md) and its directly linked references.

1. **Establish the complete issue contract before interpreting readiness.**

   In the real workflow, I would require authenticated `gh` and operational, independently installed Superpowers, then run:

   ```sh
   gh auth status

   gh label list --repo "$sp_bp_repo" \
     --json name,description

   gh issue view 42 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue view 37 --repo "$sp_bp_repo" \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   I would fetch the returned epic using the same complete query, and inspect comments where needed to establish approval, dependency resolution, or evidence:

   ```sh
   gh issue view 42 --repo "$sp_bp_repo" --comments
   gh issue view 37 --repo "$sp_bp_repo" --comments
   ```

   Being a child of an epic does not prove #42 is a leaf; its own `subIssues` must establish that. Its body must contain Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

   Missing fields or incomplete relationships remain unknown and prevent execution. An open tracked issue must have exactly one lifecycle label. Zero or multiple labels require evidence-based repair before another transition; I would not silently create labels.

2. **Reconcile the body edit with the approved authorities.**

   Authority is divided as follows:

   - The native issue owns current intent, scope, acceptance, hierarchy, dependencies, and lifecycle.
   - The approved committed specification owns the design.
   - One current approved, issue-bound Superpowers plan owns execution.
   - Accepted immutable evidence establishes satisfaction.

   I would inspect the committed artifacts and approval evidence, comparing the plan’s consumed issue URL and `updatedAt` with the current body. The plan must also bind the design authority, acceptance criteria, verification seams, and exact project verification commands.

   The timestamp change triggers comparison; it does not automatically invalidate approval:

   | Actual change | Decision |
   |---|---|
   | Editorial, already covered | Record semantic equivalence; retain the approved spec and plan. |
   | Scope/acceptance covered by the spec but missing from the plan | Revise and approve the plan through `superpowers:writing-plans`. |
   | Changed or missing design | Return to `superpowers:brainstorming`, specification review, then planning. |
   | New blocker | Record the blocker and release condition. |

   I would preserve previously approved decisions rather than repeat blank-slate brainstorming. An unapproved body edit cannot silently amend the approved design.

3. **Represent the unresolved blocker accurately.**

   After reconciliation and an immediate re-read, I would move the observed valid lifecycle label to `backplane:blocked`, preserving unrelated labels:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_lifecycle" \
     --add-label backplane:blocked
   ```

   If it is already blocked, I would retain that label and validate its recorded resume target. The comment would identify the **evidence-supported** target and concrete release condition:

   ```sh
   gh issue comment 42 --repo "$sp_bp_repo" --body \
   "Resume target: $sp_bp_resume_target
   Blocker: native dependency #37 remains unresolved.
   Release condition: acceptable evidence resolves #37; reconcile the post-plan issue-body edit and revalidate every entry gate for the resume target."
   ```

   `$sp_bp_resume_target` is determined from observed state and reconciliation—not guessed. For example, `backplane:ready` is appropriate when its other gates remain valid; `backplane:designing` is appropriate when design or plan work is required. The hypothetical omits the actual label and edit content, so literal values cannot honestly be supplied.

   I would re-fetch the complete contract after the proposed edit and verify the expected label and preservation of unrelated labels. I would preserve the native dependency and epic relationship.

4. **Start only after every eligibility gate passes.**

   #42 must be open, a bounded executable leaf, contract-complete, backed by approved design and a current approved plan, have every blocker resolved with acceptable evidence, and carry `backplane:ready`. Merely closing #37 is insufficient evidence of its prerequisite outcome.

   Once the recorded resume gate is revalidated, I would restore that state. Selection alone changes no label. After selection and another re-read, **when the first execution task actually begins**, I would run:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:ready \
     --add-label backplane:active
   ```

   I would validate the existing worktree under project rules, then follow upstream execution, appropriate TDD, review, verification, and branch finishing. A prepared worktree creates no readiness entitlement.

5. **Keep completion separate from submission and merge.**

   Supported submission moves `active → review`; requested implementation changes move `review → active`. I would inspect actual PR state:

   ```sh
   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Close #42 only after accepted review, integration at the project’s actual target, and fresh project-owned verification establish every applicable criterion at the reconciled requirement revision and exact delivery commit:

   ```sh
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   ```

   I would then re-fetch state, reason, labels, and closing relationships. No `done` label. A checkbox, PR, merge, or automatic closure supplies no missing acceptance evidence. Child completion does not close the epic; its remaining obligations require separate accounting. Release publication remains separately authorized.