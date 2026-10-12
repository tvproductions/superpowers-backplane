Read the inventory’s installed `using-superpowers`, its Codex reference, and `managing-superpowers-backlog` with all three references: `github-issue-contract.md`, `superpowers-binding.md`, and `installing-superpowers.md`. I also read the applicable execution, TDD, review, verification, and branch-finishing skills. Only skill sources were inspected; no commands below were executed.

1. **Native intake and eligibility**

   Hypothetical preflight:

   ```sh
   gh auth status
   gh label list --repo example/widgets --json name,description
   gh issue edit --help
   gh issue close --help
   ```

   Authentication, required CLI capabilities, and upstream installation provenance/version/compatibility are **unknown** in this probe. Active skill discovery does not establish those facts. Missing intake fields would fail closed rather than be inferred from prose.

   Fetch #12 using the complete native contract:

   ```sh
   gh issue view 12 --repo example/widgets \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Fetch comments only if approval, discussion, blockers, or evidence requires them:

   ```sh
   gh issue view 12 --repo example/widgets --comments
   ```

   Validate that #12 is open, has exactly one lifecycle label (`backplane:ready`), native parent #3, no children, and no unresolved blockers. Its executable body must contain Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

   On the supplied facts, #12 is covered, eligible, and explicitly selected. Parent #3 provides product continuity; #12 is the execution unit.

2. **Start and hand off to Superpowers**

   Immediately before starting, repeat the complete intake query and compare `updatedAt` with the plan’s consumed revision. A difference requires semantic reconciliation: editorial changes may remain covered; scope or acceptance changes may require plan approval; design changes require brainstorming; new blockers require blocking.

   The approved issue body is sufficient design authority for bounded work without new architectural, cross-cutting, or breaking decisions. Do not repeat already-approved brainstorming. Confirm the committed plan binds:

   - `https://github.com/example/widgets/issues/12`
   - The consumed `updatedAt`
   - The approved issue-body design
   - Acceptance criteria and verification seams
   - Exact command: `cargo test --workspace`

   Follow Superpowers through appropriate workspace isolation, plan execution, TDD, review, verification, and branch finishing. Workspace placement, branch identity, and integration target are unspecified and remain unknown.

   When the first execution task actually begins:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:ready --add-label backplane:active
   ```

   Re-fetch afterward to verify exactly one expected lifecycle label and unchanged unrelated labels. Use that read–validate–edit–verify sequence for every transition.

3. **Verification and submission**

   The sole project-owned verification command is:

   ```sh
   cargo test --workspace
   ```

   Use it for the baseline, TDD failure/pass evidence, submission verification, and fresh verification of the integrated target. Inspect output and exit status; require acceptance evidence as well as passing tests. Do not infer a Python dependency or introduce another test runner.

   After implementation, required review, resolution of significant findings, and fresh worktree verification, submit a PR against the established target. For example:

   ```sh
   gh pr create --repo example/widgets \
     --base '<verified-target>' --head '<implementation-branch>' \
     --title '<change-summary>' --body-file '<prepared-review-package>'
   ```

   The review package would identify #12, its design and plan, implementation/review evidence, and verification results. No package is created during this probe.

   Re-read #12, then transition:

   ```sh
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active --add-label backplane:review
   ```

   Requested implementation changes return `review → active`. A concrete blocker moves any open state to `blocked`, with a recorded `Resume target: backplane:<state>` and release condition. Resume only after revalidating that target’s gates.

4. **Closure**

   Submission leaves #12 open in review. Commits, checked plan boxes, and PR creation do not establish completion.

   Inspect native integration evidence:

   ```sh
   gh pr view '<pr-number>' --repo example/widgets \
     --json url,state,mergedAt,mergeCommit,baseRefName,closingIssuesReferences
   ```

   Once delivery is integrated into the verified target, satisfies acceptance, and passes a **fresh** `cargo test --workspace`, re-read #12 and conditionally close:

   ```sh
   gh issue close 12 --repo example/widgets --reason completed
   ```

   Re-fetch to confirm `state=CLOSED` and `stateReason=COMPLETED`. Coordinate automatic closing keywords with this verification gate; avoid premature auto-closure. Add no done label, and do not automatically close parent #3. Explicit rejection or abandonment instead uses reason `not planned`.