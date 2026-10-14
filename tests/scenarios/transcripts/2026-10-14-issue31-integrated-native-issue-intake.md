**I would keep #42 open, treat it as blocked, and reconcile the issue edit before implementation.** The deadline, maintainer’s instruction, and prepared worktree do not establish eligibility.

I used the [designated candidate skill](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/SKILL.md) and its required references. Everything below is proposed; no live queries or mutations were performed.

1. **Establish the complete issue contract.**

   In the actual workflow, I would use these commands, with `OWNER/REPO` replaced by the established repository identity:

   ```sh
   sp_bp_repo='OWNER/REPO'
   sp_bp_fields='number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url'

   gh auth status
   gh label list --repo "$sp_bp_repo" --limit 1000 \
     --json name,description

   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   gh issue view 37 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   gh issue view "$sp_bp_epic_number" --repo "$sp_bp_repo" \
     --json "$sp_bp_fields"

   gh issue view 42 --repo "$sp_bp_repo" --comments
   gh issue view 37 --repo "$sp_bp_repo" --comments
   ```

   The epic number comes from native `parent`, not body prose. I would complete any truncated relationship collections before relying on them.

   I would verify that #42 is open and has no children. Being a child of an epic does not itself establish that it is an executable leaf. Its body must contain Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

   The supplied scenario omits its current label, exact revisions, and blocker-resolution evidence. Those remain unknown; “fully specified” does not supply them.

2. **Reconcile the edited body against the approved authorities.**

   Authority is divided as follows:

   | Concern | Authority |
   |---|---|
   | Current intent, scope, acceptance, lifecycle | GitHub issue |
   | Parentage and execution dependencies | Native GitHub relationships |
   | Approved behavior | Committed approved specification |
   | Execution | One current approved issue-bound Superpowers plan |
   | Satisfaction | Accepted evidence against exact requirements and delivery revisions |

   I would read the complete linked spec and plan at their committed identities, including approval evidence. The plan must identify the issue URL, consumed `updatedAt`, design authority, acceptance constraints, and exact project verification commands.

   The later edit triggers semantic comparison:

   - **Editorial and already covered:** record reconciliation; retain the approved spec and plan.
   - **Changed scope or acceptance covered by the spec but missing from the plan:** revise and obtain approval for the plan through `superpowers:writing-plans`.
   - **Changed design:** return to `superpowers:brainstorming` for the changed decisions, specification review, and a revised approved plan.
   - **New blocker:** record it and remain blocked.

   I would not repeat settled design work or assume the old plan covers an unseen edit. A conflict between issue scope and specification needs explicit reconciliation.

3. **Record the blocker without starting execution.**

   Eligibility requires all six conditions: open executable leaf, complete body contract, approved design, plan matching current semantics, every native blocker resolved with acceptable evidence, and `backplane:ready`.

   **#42 currently fails the blocker gate.** I would preserve its native relationship to #37 and the epic. Closing #37 alone would not prove that its prerequisite was acceptably delivered.

   Before a simulated transition, I would re-fetch #42, reconcile drift, and require exactly one lifecycle label. Zero or multiple labels require evidence-based repair before another transition; missing repository labels are not silently created.

   With the observed current label and supported resume target established:

   ```sh
   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"

   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_label" \
     --add-label backplane:blocked

   gh issue comment 42 --repo "$sp_bp_repo" --body \
   "Blocked by native dependency #37. Resume target: $sp_bp_resume_label. Release condition: accepted evidence resolves #37's prerequisite, issue revision reconciliation is complete, and every entry gate for the resume target is revalidated."

   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   ```

   I would skip the label edit if already blocked, preserve unrelated labels, and verify the resulting label set. The resume target is the prior valid state supported by evidence; I would not invent `ready` merely because a worktree exists. The fixture does not supply that target.

4. **Resume only after the gates pass.**

   Once #37’s prerequisite is resolved, I would re-read the graph and revision inputs, then revalidate the recorded target. If revision reconciliation requires design or planning, resume in `designing`; if deferred, use `backlog`. Otherwise, return to `ready` after all readiness gates pass.

   I would retain and verify the existing worktree’s identity, ownership, branch, and project baseline instead of recreating it. Project Git boundaries and artifact namespaces still apply; an issue-specific exception for #31 supplies no authorization for #42.

   Selection alone changes no label. When eligible #42 actually begins its first execution task:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Then follow the approved Superpowers execution approach, TDD, required review, verification, and branch finishing. Use project-owned commands without assuming a runtime. Prohibited helper writes must be reconciled through a supported project route.

5. **Keep it open through review and integration; close on verified satisfaction.**

   Implementation, required review, and passing worktree verification support submission and `active → review`. Requested implementation changes produce `review → active`.

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:active --add-label backplane:review

   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Each transition uses the same re-read, reconciliation, and post-write verification procedure. I would use neutral `Refs #42` contribution wording while completion evidence is pending.

   Close #42 only after accepted review, accepted integration at the project’s actual target, and fresh project checks establish every applicable acceptance criterion against the reconciled inputs and exact delivery commit. Preserve immutable evidence and, where governance participation is declared, update its evaluation pointers.

   ```sh
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   gh issue view 42 --repo "$sp_bp_repo" --json "$sp_bp_fields"
   ```

   Apply the project’s closed-label policy without adding a done label. Epic completion requires accounting for every parent obligation; child closure does not establish it. `not planned` requires explicit rejection or abandonment authority. Release publication remains separately authorized.

   A PR, merge, checkbox, or automatic closure cannot substitute for satisfaction. If automation closes #42 prematurely, report its actual state and outstanding obligations, and propose authorized recovery without silently reopening it.