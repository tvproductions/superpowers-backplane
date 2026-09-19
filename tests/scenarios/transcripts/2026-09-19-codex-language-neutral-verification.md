# Codex language-neutral verification — 2026-09-19

Fresh Codex CLI session, read-only, ephemeral; Backplane project skills available from repository. Isolated native plugin discovery is tracked separately.

## Score

| Expectation | Result |
|---|---|
| Use only cargo test --workspace as project verification | PASS |
| Introduce no Python or pytest workflow | PASS |
| Preserve native issue graph and revision binding | PASS |
| Preserve Superpowers planning, execution, review, and verification | PASS |
| Keep issue open through review and close only after integrated verification | PASS |

## Exact prompt

```text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires. Do not inspect or rely on the current working repository; this
is a self-contained hypothetical project. Do not mutate any real GitHub issue
or file.

A Superpowers project at example/widgets has a ready executable issue #12 with
an approved issue-body design and committed Superpowers plan. Its parent epic
is #3, it has no sub-issues or blockers, and its plan records the current issue
updatedAt. The project instructions say its sole verification command is
cargo test --workspace; they say nothing about Python. The maintainer selects
#12 and asks you to start it, submit it after implementation, and explain
closure. Show the native gh intake fields, lifecycle transitions, Superpowers
handoff, and verification rule you would use.
```

## Exact final response

````text
## 1. Native GitHub intake

Immediately before starting, fetch the complete native issue contract:

```bash
gh issue view 12 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Fetch comments only if approval or evidence is not already represented:

```bash
gh issue view 12 --repo example/widgets --comments
```

Validate:

- Issue is open.
- Body contains Objective, bounded scope, acceptance criteria, verification seams, and Superpowers artifacts.
- `parent` is issue `#3`.
- `subIssues` is empty, so `#12` is an executable leaf.
- `blockedBy` is empty.
- The issue has exactly one lifecycle label: `backplane:ready`.
- Design authority is the approved issue body.
- The committed plan records the issue URL and the same current `updatedAt`.
- The maintainer explicitly selected `#12`.

Thus `#12` is captured, covered, eligible, and selected. Its position under epic `#3` does not establish priority; the maintainer’s selection does.

## 2. Starting work

The transition occurs when the first execution task actually begins:

```bash
gh issue edit 12 --repo example/widgets \
  --remove-label backplane:ready \
  --add-label backplane:active
```

Then repeat the full intake command and verify:

- Exactly one `backplane:*` label remains.
- It is `backplane:active`.
- Unrelated labels are unchanged.
- Parent, blocker, and revision facts remain valid.

If `updatedAt` had changed, I would first reconcile the change:

- Editorial and already covered: record the reconciliation and proceed.
- Scope or acceptance change missing from the plan: revise and approve the plan.
- Design change: return to brainstorming/designing.
- New blocker: enter `backplane:blocked` and record `Resume target: backplane:ready` plus the release condition.

No reconciliation is needed in this scenario because the plan records the current revision.

## 3. Superpowers handoff

The approved issue body is sufficient design authority because the prompt establishes that it is approved and executable. I would not repeat blank-slate brainstorming unless implementation exposed a new architectural, breaking, or cross-cutting decision.

The current plan must bind:

- Issue URL for `example/widgets#12`.
- Consumed `updatedAt`.
- Design authority: approved issue body.
- Acceptance criteria and verification seams.
- Exact verification command: `cargo test --workspace`.

Execution then follows the committed plan in an isolated worktree, with test-first RED → GREEN → REFACTOR cycles. The plan is execution authority; its checked boxes do not prove backlog completion.

The project’s sole verification rule is:

```bash
cargo test --workspace
```

I would use that command for the clean baseline, task or whole-suite gates required by the plan, pre-submission verification, and fresh integrated-target verification. I would not run or suggest pytest merely because another workflow example mentions it.

## 4. Submission

After implementation:

1. Obtain the required code review against the issue, plan, acceptance criteria, and implementation range.
2. Resolve all Critical and Important findings using test-first fixes.
3. Run a fresh worktree verification:

   ```bash
   cargo test --workspace
   ```

4. Confirm exit status zero and read the complete result.
5. Create the PR using `gh`, following the repository’s branch and PR rules.
6. Transition the still-open issue:

   ```bash
   gh issue edit 12 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:review
   ```

7. Re-fetch the full intake fields and verify the label and relationships.

The PR should reference `#12`. It may use `Closes #12` only when the repository’s merge process verifies the actual integrated result before GitHub performs automatic closure. Otherwise, reference the issue without a closing keyword, merge it, verify the integrated target, and close the issue explicitly afterward.

PR creation is submission evidence. It does not by itself make `#12` complete.

## 5. Integration and closure

Keep `#12` open with `backplane:review` while review and integration are pending.

If review requests changes:

```bash
gh issue edit 12 --repo example/widgets \
  --remove-label backplane:review \
  --add-label backplane:active
```

After fixing, reviewing, and verifying again, return it to `backplane:review`.

For successful closure:

1. Confirm the linked PR is merged or otherwise integrated into the intended target.
2. Run fresh verification against that integrated target:

   ```bash
   cargo test --workspace
   ```

3. Check every acceptance criterion against the integrated result.
4. Close with the terminal success reason:

   ```bash
   gh issue close 12 --repo example/widgets --reason completed
   ```

5. Re-fetch the issue and verify `state=CLOSED`, `stateReason=COMPLETED`, the expected relationship to `#3`, and the delivery evidence.

There is no `backplane:done` label. `closed/completed` is the terminal success state. Issue `#3` remains a separate continuity node; closing leaf `#12` does not automatically prove the epic complete.
````
