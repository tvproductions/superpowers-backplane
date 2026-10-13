**I would not start implementation of #42.** I would keep it open and place or retain it in `backplane:blocked`. Issue #37 is an unresolved prerequisite, and the later body edit needs semantic reconciliation before the approved plan can authorize execution. The deadline and prepared worktree do not satisfy either gate.

I used the [designated candidate skill](skills/managing-superpowers-backlog/SKILL.md) and its operation references. Everything below is a proposed command or decision; no live queries or mutations were performed.

1. **Establish the complete issue context.**

   In the real workflow, I would run:

   ```sh
   sp_bp_repo='OWNER/REPO'

   gh auth status
   gh label list --repo "$sp_bp_repo" --json name,description

   sp_bp_read_issue() {
     gh issue view "$1" --repo "$sp_bp_repo" \
       --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   }

   sp_bp_read_issue 42
   sp_bp_read_issue 37

   gh issue view 42 --repo "$sp_bp_repo" --comments
   gh issue view 37 --repo "$sp_bp_repo" --comments
   ```

   Comments are relevant here to approvals and dependency-release evidence. I would also inspect the native parent and any additional dependency endpoints revealed by intake, completing truncated relationship collections before relying on them.

   Being an epic’s child does **not** establish that #42 is a leaf. Its own `subIssues` must establish that. “Fully specified” must be checked against the required Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts sections.

   Missing required fields or evidence remain unknown and prevent eligibility. I would not silently create labels, infer native edges from checkboxes, or introduce a Project prerequisite.

2. **Reconcile the issue edit with the committed authorities.**

   The issue owns current intent and lifecycle; the approved specification owns approved behavior; the current approved issue-bound plan owns execution; accepted evidence establishes satisfaction. Repository instructions govern the workflow. An edited body cannot silently amend approved scope.

   I would compare the current body with the issue revision consumed by the plan, checking the plan’s issue URL, consumed `updatedAt`, design authority, acceptance constraints, and exact project verification commands.

   - **Editorial and already covered:** record semantic equivalence and the reconciled revision; retain the approved spec and plan.
   - **Scope or acceptance changed, covered by the spec but absent from the plan:** revise and obtain approval for the plan.
   - **Design changed or conflicts with approved authority:** use upstream brainstorming and specification review for the changed decision, then update and approve the plan.
   - **Comparison evidence unavailable:** keep reconciliation unresolved.

   I would not repeat settled brainstorming merely because the timestamp changed.

3. **Record the blocker without inventing the current label or resume target.**

   The fixture does not supply #42’s actual lifecycle label. Before a transition, I would re-read it and require exactly one `backplane:*` label. Zero or multiple labels must be repaired under applicable authority before another transition.

   If #42 is already blocked, retain that state and validate its recorded release condition. Otherwise, after checking the expected revision and relationships:

   ```sh
   sp_bp_read_issue 42

   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label "$sp_bp_current_label" \
     --add-label backplane:blocked

   gh issue comment 42 --repo "$sp_bp_repo" \
     --body "$sp_bp_blocking_record"

   sp_bp_read_issue 42
   ```

   Here `$sp_bp_current_label` is the observed sole lifecycle label. The comment would name #37 and contain:

   ```text
   Resume target: backplane:<evidence-supported prior valid state>
   Release condition: #37's prerequisite is resolved with acceptable evidence,
   and #42's edited body is reconciled with its approved design/current plan.
   ```

   I would preserve unrelated labels and verify them afterward. A formerly ready issue with editorial drift can record `ready`; invalidated design or planning requires `designing` on recovery. I would not guess an undocumented former state, close #37, or remove its dependency edge to expedite #42.

4. **Resume only through the readiness gates.**

   #42 becomes eligible only when it is an **open executable leaf**, has a complete contract, approved design and a current approved plan, every native blocker is resolved with acceptable evidence, and it carries `backplane:ready`.

   When the blocker clears, revalidate every entry gate for the recorded target. If that target is no longer valid, return to `designing` or `backlog` according to the facts.

   Selection alone changes no label. Only when eligible, selected, freshly re-read, and beginning the first execution task would I run:

   ```sh
   gh issue edit 42 --repo "$sp_bp_repo" \
     --remove-label backplane:ready \
     --add-label backplane:active
   ```

   Preserve and validate the prepared worktree, then follow upstream execution, artifact-appropriate TDD, review, verification, and branch finishing under project rules.

5. **Close only after accepted integrated delivery passes fresh checks.**

   Move `active → review` when implementation, required review, and worktree verification support submission. Requested implementation changes mean `review → active`.

   At closeout, inspect actual PR evidence:

   ```sh
   gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
     --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
   ```

   Confirm accepted review and integration at the project’s target, then execute the plan’s exact project-owned checks there. Record criterion results against the reconciled approved inputs and exact delivery commit. Missing evidence is `UNKNOWN`; a failed applicable check is `UNSATISFIED`.

   Only with all applicable obligations satisfied and applicable closure authority:

   ```sh
   sp_bp_read_issue 42
   gh issue close 42 --repo "$sp_bp_repo" --reason completed
   sp_bp_read_issue 42
   ```

   No done label. Reconcile the epic’s obligations separately; completing one child does not complete its parent. Any checkpoint, cleanup, or release follows its own authority. If automation closes #42 before verification, report its actual closed state and outstanding obligations, and propose authorized recovery. Merge or automatic closure does not establish satisfaction.