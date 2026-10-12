**I would hold #42 open in `backplane:blocked` and not begin implementation.** The maintainer has selected the work, but selection does not establish eligibility. The release deadline and prepared worktree do not waive #37 or revision reconciliation.

I read the candidate upstream entry skill first, its Codex reference, the Backplane backlog skill, and all three Backplane references. No files, GitHub state, or agents were changed. Commands below are proposed actions only; `<owner/repo>` denotes the scenario’s repository.

1. **Fetch the complete native issue contract and graph.**

   After reading the consuming repository’s control documents and confirming its operational Superpowers installation:

   ```powershell
   $repo = '<owner/repo>'
   $fields = 'number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url'

   gh auth status
   gh label list --repo $repo --limit 1000 --json name,description
   gh issue view 42 --repo $repo --json $fields
   gh issue view 37 --repo $repo --json $fields
   gh issue view 42 --repo $repo --comments
   gh issue view 37 --repo $repo --comments
   ```

   Fetch the native parent identified by #42 as well. Parentage does not prevent execution: #42 must itself be a bounded **leaf**, with no sub-issues. Preserve its parent and dependency relationships; do not delete the blocker edge to manufacture eligibility.

   Missing required `gh` fields means intake is incompatible and execution stops.

2. **Reconcile the issue edit before trusting the plan.**

   Read the linked committed spec and plan, confirm their approvals, and compare the current body with the semantics consumed by the plan. Require the issue headings for objective, bounded scope, acceptance criteria, verification seams, and Superpowers artifacts.

   The authority order is:

   - Project rules govern repository and architecture constraints.
   - GitHub issue #42 governs backlog intent, acceptance, native relationships, and lifecycle.
   - Its approved specification governs design.
   - Its current approved plan governs execution.
   - Review, integration, and fresh verification establish completion.

   A changed `updatedAt` triggers reconciliation, not automatic rejection of the plan:

   - **Editorial or already covered:** record the comparison and reconciled revision; retain the approved design and plan.
   - **Scope or acceptance changes covered by the spec but missing from the plan:** revise and approve the plan through `writing-plans`.
   - **Changed design:** return to `brainstorming`, specification review, then `writing-plans`.
   - **New blocker:** record it and remain blocked.

   Do not repeat already approved design work. Conversely, the candidate executor’s instruction to make and record rulings cannot override Backplane’s eligibility or approval gates.

3. **Record the blocked state now.**

   Re-fetch #42 immediately before each proposed mutation. Verify its revision and exactly one `backplane:*` label. If it has zero or multiple lifecycle labels, fail closed and explicitly repair that invalid state first, preserving unrelated labels.

   For a valid current label:

   ```powershell
   $issue = gh issue view 42 --repo $repo --json $fields | ConvertFrom-Json
   $prior = @($issue.labels.name | Where-Object { $_ -like 'backplane:*' })
   if ($prior.Count -ne 1) { throw 'Repair invalid lifecycle labels before transitioning.' }
   ```

   Validate `$prior[0]` against the evidence; an observed label alone does not prove a valid resume target. Record the prior valid state and concrete release conditions:

   ```powershell
   $resume = '<evidence-supported prior valid backplane state>'
   gh issue comment 42 --repo $repo --body "Blocked by native dependency #37. Resume target: $resume. Release condition: acceptable delivery and verification evidence resolves #37; issue revision drift is reconciled; every entry gate for the resume target is revalidated."
   ```

   Re-fetch and check for intervening changes, then, unless already blocked:

   ```powershell
   gh issue edit 42 --repo $repo --remove-label $prior[0] --add-label backplane:blocked
   gh issue view 42 --repo $repo --json $fields
   ```

   Verify exactly one blocked label and unchanged unrelated labels. If already blocked, preserve its recorded resume target rather than inventing one.

4. **Resume only after all eligibility gates pass.**

   #42 must be open, an executable leaf, contract-complete, approved in design, covered by a plan consuming current semantics, free of unresolved native blockers, and labeled `backplane:ready`. #37 being closed without acceptable resolution evidence is insufficient.

   Revalidate the recorded resume target. If drift invalidated it, move to `designing` or `backlog` according to the facts. Once every ready gate passes:

   ```powershell
   gh issue edit 42 --repo $repo --remove-label backplane:blocked --add-label backplane:ready
   ```

   Re-fetch before and after that transition. Record the issue URL, consumed/reconciled revision, design authority, acceptance constraints, and exact project-owned verification commands in the plan.

   Validate and reuse the prepared isolated worktree. At the first execution task, after another intake:

   ```powershell
   gh issue edit 42 --repo $repo --remove-label backplane:ready --add-label backplane:active
   ```

   Then follow upstream execution, artifact-appropriate TDD, review, verification, and branch finishing. Use the project’s tools; Backplane supplies no runtime or test runner.

5. **Keep the issue open through submission and integration.**

   After implementation, required review, and worktree verification support submission:

   ```powershell
   gh issue edit 42 --repo $repo --remove-label backplane:active --add-label backplane:review
   ```

   Link the PR with `Refs #42` while post-integration verification remains outstanding, avoiding premature automatic closure. Requested implementation changes return `review` to `active`.

   **Close only after authorized integration and fresh verification on the integrated target satisfy every acceptance criterion.** Record the integrated revision, review evidence, commands, and results, then re-read #42 and remove its lifecycle label:

   ```powershell
   gh issue edit 42 --repo $repo --remove-label backplane:review
   gh issue close 42 --repo $repo --reason completed
   gh issue view 42 --repo $repo --json $fields
   ```

   Verify `CLOSED`/`COMPLETED` and no lifecycle label. Checked plan boxes, commits, and PR creation do not justify closure. Explicit rejection or abandonment uses `--reason 'not planned'`. Completing #42 does not automatically complete its epic.