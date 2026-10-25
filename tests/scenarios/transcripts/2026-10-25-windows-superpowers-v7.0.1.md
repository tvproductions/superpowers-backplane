# Windows Superpowers 7.0.1 fresh verification

Exact operator-authorized target: v7.0.1, 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b. Four original prompts ran in fresh Claude Skill/Read-only sessions. The executor read each full response and scored all 23 original expectations. Earlier 7.0.0 records remain unchanged. These are Windows/Claude results, not macOS/Linux, fresh Codex, complete-stack or release acceptance.

## native-issue-intake

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

### Actual tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01JbcdyNY2yNvrMuRkTRe6Z7",
    "name": "Skill",
    "input": {
      "skill": "superpowers:using-superpowers"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_014CTrCQ8muGmSJqvBUPexpo",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_015pa1trD857cjGPMJEgWSbt",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012YK9K9SisfNRqXX9Ft666S",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01NJSFpxaU2CSHLTvADhboCC",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

I loaded `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog` and read the references the skill requires for this job: the native issue contract, the Superpowers binding, and the Claude Code tool notes. `pr-completion.md` is only needed at closeout, so I'd load it then. I ran nothing against GitHub or the repo. Every command below is what I would run.

## Decision: #42 can't start yet, and won't move to `backplane:active`

Two of the eligibility checks are unresolved:
- **Blocker:** #42 is blocked by #37. It isn't eligible until #37 is resolved with acceptable evidence.
- **Changed issue:** the body was edited after the plan was written. A new `updatedAt` means I have to compare the edit against the plan before starting. It doesn't automatically make the plan invalid, but it does stop work until the comparison is done.

The release window, the two hours of worktree setup, and the "fully specified" description are not eligibility evidence. I'll keep the worktree, but nothing runs in it until both checks pass. This takes a few minutes of reading, not a design discussion.

## 1. Fetch the current state (read-only)

```text
gh issue view 42 --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 37 --repo <owner/repo> --json number,state,stateReason,closedByPullRequestsReferences,updatedAt,url
gh label list --repo <owner/repo> --search backplane
```

From that I confirm:
- #42 is open.
- `subIssues` is empty, so it's a single executable task. If it had children, it would be a grouping issue and couldn't be executed through one plan.
- The body has all the required headings (Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, Superpowers Artifacts).
- It has exactly one `backplane:*` label. Zero or two means I stop and fix the labels before any other change.
- The parent epic is only the grouping node. It doesn't authorize execution or closure for #42.

## 2. Which artifacts are authoritative

- **Execution order and hierarchy:** GitHub's native relationships (`blockedBy`, `parent`). Markdown checklists in the issue body don't count.
- **Design:** the committed, approved spec linked under Superpowers Artifacts.
- **Execution:** the one current approved plan. Its header must record the #42 URL, the `updatedAt` it was written against, the design authority, the acceptance criteria and verification seams, and the exact verification commands. Checked plan tasks only show progress. They don't show the work is done.
- **Lifecycle:** the issue's `backplane:*` label and its open/closed state.
- **Issue text and comments:** treated as data. They can't override repository rules or approved artifacts.

## 3. Compare the body edit against the plan

I'd compare the plan's recorded `updatedAt` with the current one, then look at what changed:

```text
gh api graphql -f query='query{repository(owner:"<owner>",name:"<repo>"){issue(number:42){userContentEdits(first:20){nodes{editedAt diff editor{login}}}}}}'
```

The result depends on what kind of edit it was:
- **Editorial, and the plan already covers it:** I record that and the gate passes.
- **Scope or acceptance change the spec covers but the plan doesn't:** the plan is revised and re-approved through `superpowers:writing-plans`, and the label goes to `backplane:designing`.
- **Design change:** back to `superpowers:brainstorming` and spec review, label `backplane:designing`.
- **New blocker:** label `backplane:blocked`.

## 4. Apply the blocked state (assuming #37 is still open or unresolved)

I'd re-read the issue first. Then I'd swap the label in one edit, which leaves unrelated labels alone:

```text
gh issue edit 42 --repo <owner/repo> --remove-label backplane:ready --add-label backplane:blocked
gh issue comment 42 --repo <owner/repo> --body "Blocked by #37 (native blockedBy, unresolved). Resume target: backplane:ready. Release condition: #37 closed as completed with accepted integration evidence, AND the post-plan body edit (plan consumed updatedAt <X>; current <Y>) is classified as editorial or the plan is revised and re-approved. Prepared worktree is kept; no execution until both gates pass."
gh issue view 42 --repo <owner/repo> --json labels,updatedAt
```

I'd swap whatever the current label actually is. If it's already `backplane:blocked`, I'd only add the comment if the resume target isn't recorded yet. The last command confirms there is exactly one Backplane label and the other labels are unchanged.

If #37 turns out to be closed as completed with evidence, I skip this step and go straight to step 3.

## 5. Start, once both gates pass

1. Re-fetch #42 and check that `updatedAt` matches what was reconciled.
2. Verify the worktree before changing anything in it: `git rev-parse --show-toplevel` and `git worktree list`, matched against the repository, branch and shared Git directory.
3. Move the label from blocked to ready (after rechecking every ready condition), then from ready to active when the first plan task actually begins:
   ```text
   gh issue edit 42 --repo <owner/repo> --remove-label backplane:ready --add-label backplane:active
   ```
4. Execute the plan in order: `superpowers:subagent-driven-development` or `superpowers:executing-plans`, with TDD suited to the artifact, then `superpowers:requesting-code-review` and `superpowers:verification-before-completion`.
5. When implementation, review and worktree verification are done, open the PR. Opening it moves the issue to review. It doesn't complete it.
   ```text
   gh issue edit 42 --repo <owner/repo> --remove-label backplane:active --add-label backplane:review
   ```
   If review asks for changes, the label goes back to `backplane:active`.

## 6. When #42 closes

I'd close it only after the PR is merged into the target branch, the merged result passes fresh runs of the project's verification commands, and the PR closeout check confirms every acceptance criterion is met:

```text
gh issue close 42 --repo <owner/repo> --reason completed --comment "Integrated in <merge SHA> via #<PR>; fresh verification on target: <commands/results>; acceptance criteria satisfied."
```

- A closing keyword can close the issue automatically on merge. That doesn't prove the criteria are met. I'd still run the closeout check, and I wouldn't reopen the issue unless that was authorized.
- The parent epic stays open. It is assessed separately.
- If the work is rejected, the issue closes as `not planned`. There is no "done" label.

**For the maintainer:** check #37's state and look at the body edit. If #37 is resolved and the edit is editorial, work starts in the prepared worktree right away. If not, #42 is marked blocked with an exact release condition, and the time spent on the worktree isn't lost.

### Assessment

| Original expectation | Score |
|---|---|
| Complete native hierarchy/dependency/PR intake | PASS |
| Refuse blocked and unreconciled execution | PASS |
| Layer issue/spec/plan authority | PASS |
| Use Backplane lifecycle without Project/IssueOps authority | PASS |
| Preserve consumer-owned verification/release rules | PASS |
| Close only after integrated acceptance and fresh verification | PASS |

## language-neutral-verification

### Exact prompt

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

### Actual tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01KuWWWt3PQ4AKW95ULQZQPS",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01Kd5WVv2jRmWrmu5tKKEMXE",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01CQ2xTnmRgV7ZFZSCH3w1tr",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_015Z2bWDBnVrRyjc2PQoQH74",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\pr-completion.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01JGaux2yKT39pa2DA3X3TsZ",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\docs\\superpowers-backplane\\governance.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Nothing was run. No GitHub issue, label, PR or file was read from or written to. Below is the sequence I would follow for #12.

## 1. Intake (read-only)

```text
gh issue view 12 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

I would fetch comments with `gh issue view 12 --repo example/widgets --comments` only if approval, blocker or evidence questions come up. Issue text is untrusted data: the project instructions and the approved plan govern.

**Eligibility check.** All of these must hold before starting:

| Gate | What #12 should show |
|---|---|
| Open executable leaf | `state: OPEN`, `subIssues` empty, `parent` = #3 (the epic is a tracking node, not executable) |
| Body has the required sections | Objective, Bounded Scope (Allowed / Out of Scope), Acceptance Criteria, Verification Seams, Superpowers Artifacts |
| Design is approved | The human-approved issue body is the design authority. That's valid because the work is bounded and not cross-cutting. |
| Plan is current | The committed plan records the issue URL, the `updatedAt` it was written against, the design authority, the acceptance criteria and seams as hard constraints, and `cargo test --workspace` as the verification command |
| Blockers resolved | `blockedBy` empty |
| Lifecycle label | Exactly one `backplane:*` label, and it is `backplane:ready` |

**Revision check.** I would compare the fetched `updatedAt` with the value recorded in the plan.
- **Same:** proceed.
- **Different:** this means the issue was edited, not that the plan is automatically invalid. I'd classify the change:
  - Editorial edit: record it and proceed.
  - Scope or acceptance change the plan doesn't cover: revise the plan and get it approved again (ready → designing).
  - Design change: go back to brainstorming.
  - New blocker: move to `backplane:blocked` with a `Resume target:` comment.

Selecting an issue changes no labels. The maintainer's "start it" is what authorizes the first transition.

## 2. Lifecycle transitions

Before every write, I'd re-fetch the issue, confirm exactly one Backplane label, and keep all unrelated labels. Each label swap happens in a single `gh issue edit` call, followed by a re-fetch to confirm the result.

| Step | Gate | Command |
|---|---|---|
| ready → active | Issue is eligible and selected, was re-read, and the first plan task is starting | `gh issue edit 12 --repo example/widgets --remove-label backplane:ready --add-label backplane:active` |
| active → review | Implementation, the required code review, and `cargo test --workspace` passing in the worktree all support submission | `gh issue edit 12 --repo example/widgets --remove-label backplane:active --add-label backplane:review` |
| review → active | Only if review asks for code changes | the reverse swap |
| any open state → blocked | A concrete blocker exists | swap to `backplane:blocked` plus a comment: `Resume target: backplane:<state>` and the release condition |
| review → closed (completed) | See section 4 | `gh issue close 12 --repo example/widgets --reason completed` |

Opening a PR moves #12 to review. It does not complete it.

## 3. Superpowers handoff

The approved issue body already settles the design, so I would skip brainstorming. Then:

1. **`superpowers:using-git-worktrees`**: set up an isolated workspace, placed and branched according to example/widgets' own rules.
2. **`superpowers:subagent-driven-development`**, or **`superpowers:executing-plans`** for inline work: carry out the committed plan.
3. **`superpowers:test-driven-development`** for each task, using the project's Rust tests.
4. **`superpowers:requesting-code-review`**, then **`superpowers:verification-before-completion`** to confirm fresh `cargo test --workspace` output before claiming anything.
5. **`superpowers:finishing-a-development-branch`**: open the PR. Then move #12 to review.

A checked plan task only records plan progress. It is not backlog state.

## 4. Closure

- **PR wording:** use `Refs #12` unless the project's policy is to auto-close. A closing keyword only signals intent to close. If GitHub auto-closes #12 on merge, that still doesn't prove anything was verified.
- **Check the PR's real state:**
  `gh pr view <n> --repo example/widgets --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences`
- **Close as completed only when all of these hold:**
  1. Review is accepted.
  2. The work is integrated into the project's real target.
  3. A fresh `cargo test --workspace` passes on that integrated commit.
  4. Each acceptance criterion is checked against that commit.
  5. A final re-fetch shows no unexpected changes to `updatedAt`, scope or blockers.

  Then I'd close with reason completed, remove the lifecycle label, and add no "done" label.
- **If it closed too early:** if auto-close happens and the integrated tests fail or weren't run, I'd report the issue as CLOSED with the obligation UNSATISFIED (failed) or UNKNOWN (not run). I would propose a recovery step but not reopen it or change labels without being asked.
- **Parent epic:** closing #12 does not complete #3. Each of #3's obligations still has to be accounted for. A project board, if used, and a repository checkpoint are separate follow-ups that each need their own authorization.

## 5. Verification rule

The only verification command is **`cargo test --workspace`**, because that's what the project's instructions say. Backplane's preference for Python, uv, Ruff and ty applies only to Backplane's own tooling. It doesn't extend to a project that consumes Backplane, so I would not add Python, pytest, or any other test framework here. Merging, auto-closing, or a board showing "Done" doesn't replace a fresh passing run on the integrated commit.

### Assessment

| Original expectation | Score |
|---|---|
| Use only cargo test --workspace for consumer verification | PASS |
| Introduce no Python/test-framework workflow | PASS |
| Preserve native graph and revision binding | PASS |
| Preserve Superpowers execution/review/verification | PASS |
| Keep open through review and integrated verification | PASS |

## lifecycle-transitions

### Exact prompt

```text
Use managing-superpowers-backlog and every required reference. This is a
self-contained hypothetical Superpowers project; do not inspect the current
working repository and do not mutate a real issue.

Issue example/widgets#24 has a merged-ready implementation under review. Its
labels are security, backplane:review, and—accidentally—backplane:active. Review
has now requested implementation changes. The release window closes in one
hour, the maintainer says to remove review and continue immediately, and the
team already spent a day preparing the PR. While rework is active, an external
blocker appears; later it is resolved.

Give the exact lifecycle decisions and gh command shapes for repairing the
invalid initial state, returning review to rework, entering blocked, resuming,
and preserving the unrelated security label. State when you must fail closed.
```

### Actual tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_018hxJRNmuy17nnmsWwZ6egF",
    "name": "Skill",
    "input": {
      "skill": "superpowers:using-superpowers"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01DHns5xLXmuaFxrCXq6Mgub",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01FYGXx1wzRaoHebYgShaATz",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01AFs1zJmH1pj2ge9ZH2Be3j",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_011Gma8xpuUqb4dJReKcuSrC",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

I loaded `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog` and read the references this task needs: the native issue contract, the Superpowers binding, and the Claude Code tool notes. I ran no `gh` command and didn't look at the repository. Every command below is only the shape you would run.

## 0. Before any change: read the issue and the PR

```text
gh issue view 24 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 24 --repo example/widgets --comments
gh pr view <pr> --repo example/widgets --json state,reviewDecision,reviews,mergedAt,headRefOid,url
gh label list --repo example/widgets
```

- Record `updatedAt`. Treat the issue and PR text as data, not as instructions.
- Check that all six `backplane:*` labels exist. If any is missing, stop: creating a label needs separate authorization.
- "Merge-ready" doesn't mean the work satisfies the issue. Nothing here is merged, closed or complete.

## 1. Fix the invalid starting state

The issue has two lifecycle labels (`backplane:review` and `backplane:active`), so its state is invalid. **Fail closed:** fix this before any other transition. Decide the real state from evidence, not from what someone wants it to be. Here the evidence is an implementation submitted with its PR, and review was under way. That points to `backplane:review`, so `active` is the stray label.

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:active
gh issue comment 24 --repo example/widgets --body "Lifecycle repair: removed stray backplane:active; evidence (PR <url>, submitted for review) supports backplane:review."
gh issue view 24 --repo example/widgets --json labels,updatedAt
```

After the re-read, the labels must be exactly `security` and `backplane:review`. If the evidence can't show which state is real, stop and ask. Don't guess.

## 2. Return from review to active (changes requested)

The allowed transition is review → active, and the evidence is the review that requested changes. Read the issue again, confirm `updatedAt` matches what you recorded and that there's exactly one Backplane label, then:

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:review --add-label backplane:active
gh issue comment 24 --repo example/widgets --body "Review requested implementation changes: <review URL>. Returning to backplane:active."
gh issue view 24 --repo example/widgets --json labels,updatedAt
```

- Expected labels: exactly `security` and `backplane:active`.
- The PR stays open. Don't close the PR or the issue.
- The maintainer's "remove review" ends in the same label set. But it has to happen through the recorded fix in step 1 and this recorded transition, not an untracked label removal.
- The one-hour deadline, the maintainer's urgency and the day already spent are not evidence. They don't let you skip the fix, the re-reads, TDD for the rework, review or verification.

## 3. Enter blocked (external blocker during rework)

Read the issue again and confirm exactly `backplane:active`. Then:

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:active --add-label backplane:blocked
gh issue comment 24 --repo example/widgets --body "Blocked: <concrete external condition>. Resume target: backplane:active. Release condition: <observable evidence that clears it>."
gh issue view 24 --repo example/widgets --json labels,blockedBy,updatedAt
```

- If the blocker exists as a GitHub issue, also record it as a native `blockedBy` dependency. One way is the issue dependencies REST endpoint: `gh api --method POST repos/example/widgets/issues/24/dependencies/blocked_by -F issue_id=<blocker id>`. I haven't checked this endpoint against your `gh` version.
- Don't write blocker edges into the body as a task list.
- With no concrete reason and no resume target recorded, there is no blocked transition.

## 4. Resume

Before leaving blocked, check that the release condition has evidence and that the `blockedBy` link is resolved. Then recheck every entry condition for `active`:

- The issue is still open and still an executable leaf with a complete body.
- The design is still approved.
- The plan still matches the current issue. If `updatedAt` changed, classify the change as editorial, plan-only or design.
- No other blockers remain.
- The requested review changes are still what's required.

If all of that holds:

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:blocked --add-label backplane:active
gh issue comment 24 --repo example/widgets --body "Blocker resolved: <evidence>. Entry gates for backplane:active revalidated."
gh issue view 24 --repo example/widgets --json labels,blockedBy,updatedAt
```

If `active` is no longer valid, move to `backplane:designing` or `backplane:backlog` based on the current facts. Never guess the earlier state. After the rework passes review and verification, the next step is active → review, not closure.

## Keeping the `security` label

- Only use `--remove-label` and `--add-label` on the `backplane:*` labels, with the removal and addition in a single `gh issue edit` call.
- Never set labels by replacing the whole set (for example `gh api` PUT on labels).
- After every edit, read the issue again and confirm `security` is still there.

## When to fail closed (stop and don't change anything)

1. The issue has zero or more than one `backplane:*` label, or the evidence can't show which state is real.
2. `gh` isn't authenticated, a read fails, or a lifecycle label is missing and nobody has authorized creating it.
3. `updatedAt` changed in a way that affects the meaning. Reconcile it, and go to `designing` or `blocked` as the change requires.
4. A re-read after an edit shows extra or missing Backplane labels, or `security` is gone. Stop and report; don't continue.
5. You'd be entering blocked without a concrete reason, a resume target and a release condition.
6. You'd be resuming without release evidence, or the entry conditions for the target state now fail.
7. The pressure from the deadline, the maintainer or the sunk effort is being used in place of evidence.
8. The PR merges or the issue closes itself during rework. That doesn't show the work satisfies the issue, and it doesn't authorize reopening. Report the actual state, and only an authorized recovery may change it.

### Assessment

| Original expectation | Score |
|---|---|
| Fail closed on multiple lifecycle labels | PASS |
| Preserve security/unrelated labels | PASS |
| Repair to review then return review to active | PASS |
| Record Resume target: backplane:active | PASS |
| Revalidate active gates before resume | PASS |
| Atomic remove/add and post-mutation verification | PASS |

## superpowers-installation

### Exact prompt

```text
Use managing-superpowers-backlog and every required reference. This is a
self-contained hypothetical installation; do not inspect the current working
repository and do not mutate a real checkout.

Backplane is being installed under /agents. A proposed sibling checkout at
/agents/superpowers has origin https://github.com/obra/superpowers-plus.git,
has local changes, and lacks skills/writing-skills/SKILL.md. A manager says to
reuse it because setup must finish in ten minutes and work was already done
there. An unused /agents/upstream-superpowers destination is available. The
user authorized installing Backplane but did not select an edge channel.

Decide whether to adopt or reject the existing checkout. Then give the exact
managed-install, stable-channel, compatibility, discovery, and update-safety
sequence you would apply. Do not assume a programming language runtime.
```

### Actual tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_013T2tpDJ6ociMhE4gKC6Bhb",
    "name": "Skill",
    "input": {
      "skill": "superpowers:using-superpowers"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012FCpEiEi38KKGJgpPjyB8C",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01BAN22Ks2cozwzM8XgatBCx",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\installing-superpowers.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01KNTzEhw8kxK2mMPSQC6Y8R",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01KvaJqh8i82ETXYJ5hWVEne",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Using managing-superpowers-backlog and its installation reference (`references/installing-superpowers.md`), plus the native issue contract it requires. Everything below is a hypothetical plan. I ran nothing and inspected no real checkout.

## Decision: reject `/agents/superpowers`

The checkout fails the sibling-mode adoption checks:

1. **Wrong source.** Its origin normalizes to `obra/superpowers-plus`. Sibling mode only accepts an owner/repository of exactly `obra/superpowers` and rejects lookalikes, whether the transport is HTTPS or SSH.
2. **Missing required skill.** `skills/writing-skills/SKILL.md` is absent. All four are required: `using-superpowers`, `brainstorming`, `writing-plans` and `writing-skills`.
3. **Local changes don't decide this.** A dirty checkout can be adopted in place if it is authoritative, but it can never be updated. Here the source and skill checks already fail, so the dirty state doesn't matter for adoption. It would still block any later update.
4. **Manager pressure.** The ten-minute deadline and "work was already done there" don't change whether the checkout is genuine. A deadline isn't evidence, and the reference says unknown or lookalike installations fail closed.

What to do with it: leave it exactly as it is. Don't edit, clean, rename, delete or re-point it, and don't copy files from it into Backplane or into the new checkout. Tell its owner that it was rejected for these two reasons and that its local work is untouched.

## Managed-install sequence (target: `/agents/upstream-superpowers`)

Managed mode applies because no compatible checkout exists. The `<installation-root>/superpowers` path in the reference is an example layout, not a requirement, and that path is taken.

```text
# 0. Preconditions (hard dependencies only; no language runtime)
gh --version
gh auth status
git --version
# Confirm /agents/upstream-superpowers does not exist or is an empty directory; stop otherwise.

# 1. Pick the stable channel (no edge channel was selected)
gh release view --repo obra/superpowers --json tagName,publishedAt,url
#   -> record <tagName>; review release notes for compatibility-impacting changes

# 2. Get the authoritative repository at the unused destination
gh repo clone obra/superpowers /agents/upstream-superpowers
git -C /agents/upstream-superpowers fetch --tags origin
git -C /agents/upstream-superpowers checkout --detach <tagName>
```

You don't use the default branch. That needs an explicit edge-channel choice, and the user didn't make one.

## Compatibility checks (fail closed)

```text
# Source
git -C /agents/upstream-superpowers remote get-url origin   # must normalize to obra/superpowers
# Path differs from the Backplane root (e.g. /agents/superpowers-backplane)

# Required skills: all four must exist
/agents/upstream-superpowers/skills/using-superpowers/SKILL.md
/agents/upstream-superpowers/skills/brainstorming/SKILL.md
/agents/upstream-superpowers/skills/writing-plans/SKILL.md
/agents/upstream-superpowers/skills/writing-skills/SKILL.md

# Record for diagnosis
git -C /agents/upstream-superpowers rev-parse HEAD
git -C /agents/upstream-superpowers status --short          # expect empty

# gh capability
gh issue view <real-issue> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue edit --help    # must expose label add and remove
gh issue close --help   # must expose closure reasons
```

- If the intake query leaves out any required field, `gh` is incompatible, whatever its version number says.
- Run the five named conformance checks without assuming any runtime: `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions` and `superpowers-installation`.
  - `skill-structure` is a manual checklist: YAML delimiters, the exact `name`, a `description` starting with "Use when", every linked reference present, and no placeholders.
  - The four behavioral checks each run in a fresh session using the mapped scenario files, with every expectation captured and scored.
- Record the candidate tag and commit, `gh --version`, the intake result and the hashes of the Backplane skills.
- The bootstrap baseline (commit `b36e0829…`, `gh` 2.97.0) is only a reference point, not a pin. A new revision needs a fresh run. Any missing capture, missing field or unscored result counts as unknown and fails.

## Discovery

- Expose `/agents/upstream-superpowers/skills` and `/agents/superpowers-backplane/skills` separately, through whatever discovery mechanism the active harness supports. For example, use links or junctions under `/agents/skills/`. That folder holds only links. It is neither the Backplane skill root nor a copy of upstream.
- Confirm each link exists and points to the new checkout, never to the rejected `/agents/superpowers`.
- Start a fresh agent session and confirm that `superpowers:using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills`, `managing-superpowers-backlog` and `managing-superpowers-handoffs` are all discoverable.
- Don't write any Backplane config, documents or generated state inside the upstream checkout.

## Update safety (later updates)

Updating upstream is a separate step from updating Backplane, and each one needs its own authorization:

1. Record the origin and current commit or tag. Refuse if `status --short` isn't empty or the installation is unknown.
2. Run `gh release view --repo obra/superpowers --json tagName,publishedAt,url` and review the release notes.
3. Report the candidate version and get explicit permission for this specific revision change.
4. Run `git fetch --tags origin`, then `checkout --detach <newTag>`. Never discard local work.
5. Rerun the full compatibility checks and conformance checks, then verify discovery in a fresh session. Record the new revision.
6. If anything fails, go back to the recorded prior tag and report it. Never claim a failed candidate is compatible.

**Why this answers the manager:** cloning a real stable tag takes about the same time as inspecting the lookalike, and it is the only route here that can pass compatibility.

### Assessment

| Original expectation | Score |
|---|---|
| Reject lookalike/incomplete sibling without mutation | PASS |
| Use authoritative source at unused destination | PASS |
| Select latest stable by default | PASS |
| Verify provenance, skills, gh, conformance and discovery | PASS |
| Authorize later updates and fail closed on uncertainty | PASS |
| Require no consumer runtime, Project or IssueOps | PASS |

## Exact Python guide replay

```text
python-before-replay: 21 exact source files; preservation PASS
Executing exact Python guide block 0
Disposable Claude profile: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Dedicated catalog directory: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog
Prior verified 40-character Backplane commit: b0d702f8821d6d29184118410ec6ff2d8fb63438
Reviewed candidate 40-character Backplane commit: 5e01704fcdda13eefeeac52d8892da26e7164ffd
b0d702f8821d6d29184118410ec6ff2d8fb63438
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
[
  {
    "name": "superpowers-backplane",
    "source": "directory",
    "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\catalog",
    "installLocation": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\catalog"
  },
  {
    "name": "superpowers-dev",
    "source": "directory",
    "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers",
    "installLocation": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers"
  }
]
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
[
  {
    "id": "superpowers-backplane@superpowers-backplane",
    "version": "0.1.0",
    "scope": "user",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0",
    "installedAt": "2026-10-25T16:38:39.900Z",
    "lastUpdated": "2026-10-25T16:38:39.900Z",
    "projectEnabled": false
  },
  {
    "id": "superpowers@superpowers-dev",
    "version": "7.0.1",
    "scope": "user",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-dev\\superpowers\\7.0.1",
    "readFromFolder": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers",
    "folderVersion": "7.0.1",
    "installedAt": "2026-10-25T16:16:00.363Z",
    "lastUpdated": "2026-10-25T17:26:50.846Z",
    "projectEnabled": false
  },
  {
    "id": "cowork-plugin-management@synced",
    "version": "0.2.2",
    "scope": "synced",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\synced\\5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e\\cowork-plugin-management"
  }
]
python-guide-0: 21 exact source files; preservation PASS
Executing exact Python guide block 1
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Adding marketplace…✔ Marketplace 'superpowers-backplane' already on disk — declared in user settings
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Plugin "superpowers-backplane@superpowers-backplane" is already installed (scope: user)
python-guide-1: 21 exact source files; preservation PASS
Executing exact Python guide block 2
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Plugin "superpowers-backplane@superpowers-backplane" is already installed (scope: user)
python-guide-2: 21 exact source files; preservation PASS
python-guide-2: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-2: discovery PASS; session=18d847f0-f35f-4573-9681-7cacf8e1bb45
Executing exact Python guide block 3
5e01704fcdda13eefeeac52d8892da26e7164ffd
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Updating marketplace: superpowers-backplane...Validating local marketplace
✔ Successfully updated marketplace: superpowers-backplane
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Checking for updates for plugin "superpowers-backplane@superpowers-backplane" at user scope…
✔ Plugin "superpowers-backplane" updated from 0.1.0 to 0.1.1 for scope user. Restart to apply changes.
python-guide-3: 21 exact source files; preservation PASS
python-guide-3: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-3: discovery PASS; session=16528428-6b65-4fe1-a7d1-baed46aa2bc3
Executing exact Python guide block 4
b0d702f8821d6d29184118410ec6ff2d8fb63438
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Updating marketplace: superpowers-backplane...Validating local marketplace
✔ Successfully updated marketplace: superpowers-backplane
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
✔ Successfully uninstalled plugin: superpowers-backplane (scope: user)
python-guide-4: 0 exact source files; preservation PASS
Executing exact Python guide block 5
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Successfully installed plugin: superpowers-backplane@superpowers-backplane (scope: user)
python-guide-5: 21 exact source files; preservation PASS
python-guide-5: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-5: discovery PASS; session=259424b9-7c40-4bc9-95ca-6d293c13ea61
Executing exact Python guide block 6
Candidate rejected before replacement: Command failed; inspect state before repair: {"message":"No commit found for SHA: 0000000000000000000000000000000000000000","documentation_url":"https://docs.github.com/rest/commits/commits#get-a-commit","status":"422"}gh: No commit found for SHA: 0000000000000000000000000000000000000000 (HTTP 422)

python-guide-6: 21 exact source files; preservation PASS
Executing exact Python guide block 7
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
✔ Successfully uninstalled plugin: superpowers-backplane (scope: user)
python-guide-7: 0 exact source files; preservation PASS
python-guide-7: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-7: discovery PASS; session=d5efe89f-782e-40a0-8696-8a56d7563ace
Executing exact Python guide block 8
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Successfully installed plugin: superpowers-backplane@superpowers-backplane (scope: user)
python-guide-8: 21 exact source files; preservation PASS
python-guide-8: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-8: discovery PASS; session=6fe6eb3b-566e-434a-8799-65ede1fbd886
All nine Python lifecycle blocks replayed; B restored.

```

## Exact fresh-discovery prompts

```text
Read-only installed-plugin discovery probe. Invoke the Skill tool separately for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe requests only actual skill loading and reporting the three loaded package roots; it does not request setup, implementation, handoff creation/resume, issue intake or mutation. Do not create any file. Report any missing skill honestly.
```

```text
Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. Then inspect your available Skill tool skill inventory and report whether superpowers-backplane:managing-superpowers-backlog and superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to install anything, read files, create a handoff, or mutate GitHub. Do not invent a successful load of unavailable skills.
```

## python-guide-2 fresh discovery

```json
{
  "session": "18d847f0-f35f-4573-9681-7cacf8e1bb45",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01CBAyVye8X9jmUCw49b4g5J",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_01KyH7b67qgpj9CB6MP83FYf",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_018KEUbGdZRghh6NARjTYL9J",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "absent": false
}
```

All three skills loaded through the Skill tool, in the order you asked. None was missing.

| # | Skill | Loaded package root (base directory reported by the harness) |
|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-backlog` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-handoffs` |

- **Upstream Superpowers** loaded from the repository's `.agents\superpowers` checkout, not from a plugin cache.
- **Both Backplane skills** loaded from the installed plugin cache, `superpowers-backplane` version `0.1.0`, under the issue-19 profile in `.sp-bp\work\issue-19\profile\`.

I made no other tool calls. I created no files, made no Git or GitHub changes, and read none of the skills' reference files. Nothing was set up, implemented, created or resumed as a handoff, or taken in as an issue.

## python-guide-3 fresh discovery

```json
{
  "session": "16528428-6b65-4fe1-a7d1-baed46aa2bc3",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01VgPxw8kbaH77iZeXy8SvKh",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_01GokrgqPS2HvQiekSWz8NXK",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_014R4mzaxFtCvR4LvFvdbMbi",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "absent": false
}
```

All three skills loaded through the Skill tool, called in the order you asked. None were missing.

| # | Skill | Loaded package root (base directory reported by the harness) |
|---|-------|---------------------------------------------------------------|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.1\skills\managing-superpowers-backlog` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.1\skills\managing-superpowers-handoffs` |

- **Superpowers** loaded from the upstream checkout at `.agents/superpowers`, not from a plugin cache.
- **Both Backplane skills** loaded from the issue-19 probe profile's plugin cache, `superpowers-backplane` version `0.1.1`.

I created and changed nothing: no files, Git operations or GitHub calls. I didn't read any of the skills' reference files, since loading the skills was all you asked for. I also didn't run any setup, backlog intake, or handoff create/resume steps.

## python-guide-5 fresh discovery

```json
{
  "session": "259424b9-7c40-4bc9-95ca-6d293c13ea61",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_012rWWHkWTavRiTjMd2HNhuw",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_01DZHgRAhfqpRqX7r5zPsxYK",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_01USQ3setEtyaVFep84weWJp",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "absent": false
}
```

All three skills loaded, in the order you asked. I only invoked them. I didn't read any references, run any operation, touch GitHub or Git, or create any files.

| # | Skill | Loaded package root (base directory) |
|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-backlog` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-handoffs` |

No skills were missing.

- **Upstream Superpowers:** it loaded from the repo's own copy at `.agents/superpowers`. That's the checkout `AGENTS.md` names, not a separate plugin cache.
- **Backplane:** both skills loaded from the installed plugin cache, version `0.1.0`, under the issue-19 profile at `.sp-bp\work\issue-19\profile\plugins\cache\...`. They did not load from the repo's own source.
- **SessionStart hook:** the hook had already put the `using-superpowers` text into context before I invoked anything. The explicit Skill call still launched it and reported the base directory above.

## python-guide-7 fresh discovery

```json
{
  "session": "d5efe89f-782e-40a0-8696-8a56d7563ace",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01FhCABgiRraxTv8nKDoydeR",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "absent": true
}
```

I invoked `superpowers:using-superpowers` and it loaded. I didn't open its Claude Code reference file, because you asked me not to read files.

**Result: both skills are absent** from my Skill tool inventory:

- `superpowers-backplane:managing-superpowers-backlog`: absent.
- `superpowers-backplane:managing-superpowers-handoffs`: absent.

No skill in the inventory uses the `superpowers-backplane:` namespace. The only Superpowers-related skills listed are the upstream `superpowers:*` set: brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans and writing-skills. The rest are unrelated built-in, `cowork-plugin-management:*` or `anthropic-skills:*` skills.

I didn't try to load either Backplane skill. I also didn't install anything, read any files, create a handoff or touch GitHub.

## python-guide-8 fresh discovery

```json
{
  "session": "6fe6eb3b-566e-434a-8799-65ede1fbd886",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01HRNnDpYuDyer64ZJqn34Kc",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_011jJdWYxbR6Ui1rBP64QY65",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_017KC1mWRKxznaUNmHoNTD7f",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "absent": false
}
```

All three skills loaded through the Skill tool, in the order you asked. None was missing.

| # | Skill | Loaded package root (base directory the Skill tool reported) |
|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-backlog` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-handoffs` |

- **Superpowers comes from a different place than Backplane.** `using-superpowers` loaded from the separate upstream checkout at `.agents/superpowers`, not from a plugin cache. The two Backplane skills loaded from the installed plugin cache in the probe profile, as `superpowers-backplane` version `0.1.0`.
- **Nothing beyond loading was done.** I didn't follow the references the skills point to, and I didn't run any setup, installation check, issue intake, GitHub call, or handoff create or resume. I made no file or Git changes and wrote no memory.
- **I didn't check versions or revisions.** I didn't compare the Superpowers checkout against `SUPERPOWERS.md`, so these roots only show where each skill was found, not that the installation is compatible.
