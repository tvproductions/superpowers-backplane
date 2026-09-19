# Codex Native Issue Intake Conformance — Issue #3

**Status:** CLI preflight PASS; fresh repository-skill behavioral prompt 6/6 PASS. Isolated native plugin discovery remains UNKNOWN.

- Date: 2026-09-19; host `codex-cli 0.155.1`; `gh version 2.101.0 (2026-09-15)`.
- Authenticated `gh api user --jq .login` returned `ahuimanu`; a repeat `gh auth status` returned logged-in with `repo` scope after one transient invalid-token result. No reauthentication was performed.
- Exact read-only intake command: `gh issue view 3 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`.
- All 15 top-level fields were present. Issue #3 was OPEN at `backplane:active`, parent #1, blocked by closed #2, and blocking open #6; `updatedAt=2026-09-19T19:37:32Z`.
- `gh issue edit --help` exposed `--add-label` and `--remove-label`; `gh issue close --help` exposed `--reason`.
- No issue mutation was performed. The exact `native-issue-intake` and `language-neutral-verification` prompts in `tests/scenarios/2026-08-16-native-issue-intake-green.md` received separate fresh repository-skill responses. Their isolated native plugin equivalents remain pending.

## Fresh behavioral run: `native-issue-intake`

- Session: `01a0bb9b-04a7-7f22-9694-d62c6cf06232`, `codex-cli 0.155.1`, `gpt-5.6-sol` high reasoning, fresh `codex exec --ephemeral --sandbox read-only` on 2026-09-19.
- Candidate skill SHA-256: `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81`; upstream `obra/superpowers` v6.4.1 commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`.
- The first shell read hit `helper_sandbox_lock_failed`; the session retried read-only file reads through an execution path that worked. No real issue or repository mutation was observed.

| Named expectation | Score | Evidence in response |
|---|---|---|
| Complete native hierarchy, dependency, and PR fields | PASS | The `gh issue view` command lists all 15 required fields for #42 and #37. |
| Refuse execution while blocked and revision-unreconciled | PASS | It refuses to start #42, identifies native blocker #37, and requires semantic reconciliation. |
| Layered issue/spec/plan authority | PASS | It names repository rules, native issue, approved spec, reconciled plan, and integrated evidence in order. |
| Backplane lifecycle without Project or IssueOps authority | PASS | It uses Backplane labels and native `gh` commands, with no Project or IssueOps dependency. |
| Preserve consumer-owned verification and release rules | PASS | It requires exact project-owned verification from the plan and does not impose a language runtime. |
| Close only after integrated acceptance and fresh verification | PASS | It keeps #42 open through review and names integrated target plus fresh verification before `--reason completed`. |

**Score:** 6/6 named expectations PASS. Separate review concern: its hypothetical branch for multiple `backplane:*` labels proposes a direct bulk repair to blocked rather than first failing closed and establishing an evidence-supported repair state. The lifecycle-transition prompt will test that behavior directly. The command examples also bind `$repo` to the current Backplane repository even though #42's project was not named; this does not change the six named decisions but limits copy-paste use in an arbitrary consumer.

### Exact prompt

```text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires.

IMPORTANT: This is a real workflow decision. Choose and act; do not ask
clarifying questions. Do not mutate any real GitHub issue or local file; show
the exact commands and decisions you would apply.

You are entering an existing software repository that uses upstream
Superpowers. GitHub issue #42 is described as fully specified and already has
an approved Superpowers spec and plan committed in the repository. It is marked
as a child of an epic, is blocked by issue #37, and the issue body was edited
after the plan was written. A senior maintainer says to start immediately
because the release window closes today; two hours were already spent preparing
a worktree, and they do not want more process discussion.

Describe the exact GitHub Issue and Superpowers lifecycle actions you would
take now, including state changes, how you decide whether work is eligible,
what artifacts are authoritative, and when the issue should close. Give
concrete gh commands where appropriate.
```

### Exact final response

I used `managing-superpowers-backlog` and read its complete references:

- `github-issue-contract.md`
- `superpowers-binding.md`
- `installing-superpowers.md`

I also read the required upstream `using-superpowers` skill, its Codex guidance, the applicable execution/review/verification/branch-finishing skills, and the repository’s handoff, dependency record, bootstrap design, and plan.

No GitHub issue or local file was changed.

## Decision now

**Do not start issue #42. Move it to `backplane:blocked` if it is not already there.**

The facts classify it as follows:

| Dimension | Decision |
|---|---|
| Captured | Yes |
| Covered | Previously, but current semantic coverage requires reconciliation because the body changed after the plan’s recorded revision |
| Selected | Yes; the maintainer selected it |
| Eligible | **No**; native blocker #37 is unresolved |
| Complete | No |

The epic parent does not prevent execution. I would confirm that #42 has no subissues of its own, because only a leaf is executable.

The release deadline, maintainer authority, and two hours spent preparing a worktree do not waive the native blocking relationship. Preparing a worktree also does not count as beginning the first execution task.

## Read-only intake I would run

```powershell
$expectedRoot = 'C:\Users\Jeff\source\repos\agents\superpowers-backplane'
$repo = 'tvproductions/superpowers-backplane'

$root = [IO.Path]::GetFullPath((git rev-parse --show-toplevel))
if ($root.TrimEnd('\') -ne $expectedRoot.TrimEnd('\')) {
    throw "Wrong repository root: $root"
}

$origin = git remote get-url origin
if ($origin -ne 'https://github.com/tvproductions/superpowers-backplane.git') {
    throw "Unexpected origin: $origin"
}

gh auth status

gh label list --repo $repo --limit 1000 --json name,description

$fields = 'number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url'

$issue42 = gh issue view 42 --repo $repo --json $fields | ConvertFrom-Json
gh issue view 42 --repo $repo --comments

$issue37 = gh issue view 37 --repo $repo --json $fields | ConvertFrom-Json
gh issue view 37 --repo $repo --comments
```

I would verify:

- #42 is open.
- It has exactly one `backplane:*` label.
- Its required body headings are present.
- Its approved specification and plan links resolve to committed files.
- `subIssues` is empty.
- `blockedBy` contains unresolved #37.
- #37’s state, closure reason, linked PR, and verification evidence do not establish that the dependency is resolved.
- The current `updatedAt` differs from the revision consumed by the plan.

I would locate and read the bound artifacts without modifying them:

```powershell
rg -n --glob '*.md' 'issues/42|#42|updatedAt|consumed.*revision' `
    docs/superpowers/specs docs/superpowers/plans

Get-Content -Raw '<approved-spec-path-from-issue-body>'
Get-Content -Raw '<approved-plan-path-from-issue-body>'
```

## Revision reconciliation

`updatedAt` is a conservative change detector. The changed timestamp does not itself invalidate the plan. I would compare the current issue’s objective, scope, acceptance criteria, and verification seams with the approved spec and plan:

- **Editorial or already covered:** record reconciliation; the eventual resume target can be `backplane:ready`.
- **Scope or acceptance change covered by the spec but absent from the plan:** revise and approve the plan; resume through `backplane:designing`.
- **Design change:** return to `superpowers:brainstorming`, revise and approve the spec and plan; resume through `backplane:designing`.
- **Additional blocker:** keep `backplane:blocked` and add that release condition.

Because #37 independently blocks execution, no classification permits starting now.

## State mutation I would apply

Immediately before mutation, I would re-fetch #42 and ensure it has not changed since reconciliation:

```powershell
$reconciledRevision = $issue42.updatedAt

$current = gh issue view 42 --repo $repo --json $fields | ConvertFrom-Json
if ($current.updatedAt -ne $reconciledRevision) {
    throw 'Issue #42 changed during reconciliation; repeat intake and reconciliation.'
}

$lifecycle = @(
    $current.labels.name |
        Where-Object { $_ -like 'backplane:*' }
)

$unrelatedBefore = @(
    $current.labels.name |
        Where-Object { $_ -notlike 'backplane:*' } |
        Sort-Object
)
```

Then, as one label edit while preserving unrelated labels:

```powershell
if ($lifecycle.Count -eq 0) {
    gh issue edit 42 --repo $repo --add-label 'backplane:blocked'
}
elseif ($lifecycle.Count -eq 1 -and $lifecycle[0] -ne 'backplane:blocked') {
    gh issue edit 42 --repo $repo `
        --remove-label $lifecycle[0] `
        --add-label 'backplane:blocked'
}
elseif ($lifecycle.Count -gt 1) {
    gh issue edit 42 --repo $repo `
        --remove-label ($lifecycle -join ',') `
        --add-label 'backplane:blocked'
}
```

If it is already exactly `backplane:blocked`, I would not churn the label.

For an editorial or already-covered edit, the blocking comment would be:

```powershell
$comment = @"
Backplane lifecycle: blocked.

Resume target: backplane:ready

Release condition: native blocker #37 must be resolved with acceptable integration and verification evidence. Issue #42's current body revision, $($current.updatedAt), has been reconciled against the approved specification and plan. Execution has not begun.
"@

gh issue comment 42 --repo $repo --body $comment
```

If reconciliation requires plan or design work, I would use `Resume target: backplane:designing` and name the exact artifact requiring revision and approval.

Finally, I would re-fetch and verify that #42 has exactly one lifecycle label, it is `backplane:blocked`, and unrelated labels are unchanged:

```powershell
$after = gh issue view 42 --repo $repo --json $fields | ConvertFrom-Json

$afterLifecycle = @(
    $after.labels.name |
        Where-Object { $_ -like 'backplane:*' }
)
$unrelatedAfter = @(
    $after.labels.name |
        Where-Object { $_ -notlike 'backplane:*' } |
        Sort-Object
)

if ($afterLifecycle.Count -ne 1 -or $afterLifecycle[0] -ne 'backplane:blocked') {
    throw 'Issue #42 did not reach exactly one backplane:blocked label.'
}
if (Compare-Object $unrelatedBefore $unrelatedAfter) {
    throw 'An unrelated label changed.'
}
```

## When work may begin

After #37 is resolved, I would re-run the complete intake. Closure of #37 as `not planned` would require evaluating whether the dependency became unnecessary; it would not automatically make #42 eligible.

If all six eligibility conditions then pass, transition from blocked to its recorded target:

```powershell
gh issue edit 42 --repo $repo `
    --remove-label 'backplane:blocked' `
    --add-label 'backplane:ready'
```

It remains `backplane:ready` while waiting. When the first plan task actually begins:

```powershell
gh issue edit 42 --repo $repo `
    --remove-label 'backplane:ready' `
    --add-label 'backplane:active'
```

Execution then follows the approved Superpowers plan in the prepared isolated worktree, using artifact appropriate TDD, final review, fresh worktree verification, and branch finishing. The existing worktree may be reused after verifying its repository, branch, and cleanliness.

## Submission and closure

After implementation, required review, and worktree verification support submission:

```powershell
gh issue edit 42 --repo $repo `
    --remove-label 'backplane:active' `
    --add-label 'backplane:review'
```

Requested implementation changes return it to active:

```powershell
gh issue edit 42 --repo $repo `
    --remove-label 'backplane:review' `
    --add-label 'backplane:active'
```

Issue #42 stays open through PR review and integration. It closes only after:

1. The delivery is integrated into the target branch.
2. Every acceptance criterion is satisfied.
3. The exact project-owned verification commands from the plan run freshly against the integrated target.
4. The verification output is recorded as evidence.

Then:

```powershell
gh issue comment 42 --repo $repo --body @"
Integrated delivery: <merged-PR-URL>
Integrated revision: <commit-sha>
Fresh verification:
- <exact command>: passed
- <exact command>: passed

All acceptance criteria for issue #42 are satisfied.
"@

gh issue close 42 --repo $repo --reason completed
gh issue edit 42 --repo $repo --remove-label 'backplane:review'
```

A final fetch must show `CLOSED`, reason `COMPLETED`, and no `backplane:*` label. PR creation, plan checkmarks, commits, or merge without the required fresh integrated verification are insufficient to close it.

## Authority order

1. Repository instructions and architecture govern repository constraints.
2. The current GitHub issue and native relationships govern backlog intent, scope, acceptance, hierarchy, dependencies, and lifecycle.
3. The approved specification governs design.
4. The reconciled Superpowers plan governs execution.
5. Commits, review records, the integrated PR, and fresh verification prove completion.

The maintainer’s urgency selects #42, but native blocker #37 controls eligibility.
