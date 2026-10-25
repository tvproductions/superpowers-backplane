# Issue 19 installed-package conformance

Observed on Windows, Claude Code 2.1.302, installed B and independent Superpowers 7.0.0. The operator explicitly approved these exact scenario prompts and public skill/reference text. Each case used a fresh Skill/Read-only session. Responses below are unedited. Scoring is a manual assessment against every original expectation, not an inference from exit status.

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

### Actual tool calls and source digests

```json
{
  "session": "1dab3098-26ec-449f-84ca-b9636c2e7d82",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01Gi4efNEUUUAh49qbCRHq7c",
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
      "id": "toolu_01RXyLBa7JmTyygPz4ycXymL",
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
      "id": "toolu_01ATNYw87ebe5MFUd3iGwDB3",
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
      "id": "toolu_0153zL4i6QSZQzxujeYoqRGv",
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
      "id": "toolu_01NfHiAgiw3LTRvhhckkd5NH",
      "name": "Read",
      "input": {
        "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "reads": [
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md",
      "sha256": "15b1c2f68ba881ba4b6bba297df03ac6f9cad3ca93fec748548503fca35f69a5"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md",
      "sha256": "641c3f3bf07a77bb6a8b175eb487f8ed6361b54b19d366c17072620a8058e231"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md",
      "sha256": "21479a3fee27448cab8748a3b5687e53bb257883bda9c070426f9a1ab5cebf1b"
    }
  ]
}
```

### Unedited response

I loaded `using-superpowers` and `managing-superpowers-backlog` and read the references they require for this operation: the native issue contract, the Superpowers binding and the Claude Code tool notes. Everything below is commands I would run. I ran nothing against GitHub or local files. `OWNER/REPO` and `<plan-path>` are placeholders.

## Decision

Start #42 only if a few minutes of read-only checks pass. The deadline, the two hours of worktree setup, and the "fully specified" description don't make the issue eligible. Two facts stop work right now: the issue was edited after the plan was written, and native #37 still blocks it. If both clear, execution starts at once and there's no more design discussion. If either fails, #42 goes to `blocked` or back to `designing`, and no code is written.

## 1. Read-only intake (no mutations)

```text
gh issue view 42 --repo OWNER/REPO --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 37 --repo OWNER/REPO --json number,state,stateReason,closedByPullRequestsReferences,updatedAt,url
gh label list --repo OWNER/REPO --search "backplane:"
gh api graphql -f query='query{repository(owner:"OWNER",name:"REPO"){issue(number:42){userContentEdits(first:20){nodes{editedAt editor{login} diff}}}}}'
```

I'd also read the committed plan header for the issue URL, the `updatedAt` it consumed, and its design authority (the spec path).

## 2. Eligibility checks (all six must pass)

1. **Open leaf:** #42 is open and `subIssues` is empty. Its parent epic is only a continuity node, so nothing on the epic changes.
2. **Body contract:** the body has Objective, Bounded Scope (Allowed / Out of Scope), Acceptance Criteria, Verification Seams, and Superpowers Artifacts.
3. **Design authority:** the committed, approved spec under `docs/superpowers/specs/`.
4. **Plan is current:** the plan's recorded `updatedAt` matches the issue's current `updatedAt`. It doesn't, so step 3 below applies.
5. **Blockers resolved:** #37 must be closed `completed` with integrated evidence. If #37 is open, or was closed `not planned` while the blocking edge still exists, the blocker is unresolved.
6. **Label:** exactly one `backplane:*` label, and it is `backplane:ready`. If there are zero or several, fail closed and repair that first.

## 3. Branches, in order

**A. #37 unresolved: stop.** Assuming #42 is labeled `ready`:

```text
gh issue edit 42 --repo OWNER/REPO --remove-label backplane:ready --add-label backplane:blocked
gh issue comment 42 --repo OWNER/REPO --body "Blocked by #37 (open). Resume target: backplane:ready. Release condition: #37 closed completed with integrated evidence, then revalidate every ready gate, including reconciling the post-plan body edit (plan consumed <old updatedAt>, current <new updatedAt>)."
```

Then re-fetch #42 and confirm exactly one `backplane:blocked` label and that unrelated labels are unchanged. I'd tell the maintainer that the release can't include #42 until #37 lands. The prepared worktree stays as it is. It isn't wasted and it isn't evidence.

**B. #37 resolved: classify the body edit from the `userContentEdits` diff.**
- **Editorial, or already covered by the plan:** comment `Revision reconciled: plan <path> consumed <old>; edit at <new> is editorial / already covered; plan remains current.` Then go to step 4.
- **Scope or acceptance change that the spec covers but the plan doesn't:** run `gh issue edit 42 --repo OWNER/REPO --remove-label backplane:ready --add-label backplane:designing`. Revise the plan with `superpowers:writing-plans` and record the new `updatedAt`. New Backplane plans go under `docs/superpowers-backplane/plans/`, and the approved spec stays at its recorded path. After approval, move it back with `--remove-label backplane:designing --add-label backplane:ready`.
- **Design change:** move it to `designing` and run `superpowers:brainstorming` plus spec review for the changed decision only. The approved parts aren't redone from scratch.

## 4. Start execution

1. Re-fetch #42 right before the label change and confirm `updatedAt` and the single label haven't moved.
2. Verify the prepared worktree against project rules: `git rev-parse --show-toplevel`, `git worktree list --porcelain`, and the recorded branch. If it doesn't match the repository boundary, don't use it.
3. When the first plan task actually starts:
   ```text
   gh issue edit 42 --repo OWNER/REPO --remove-label backplane:ready --add-label backplane:active
   ```
4. Execute with `superpowers:subagent-driven-development` (or `executing-plans` for inline work), using TDD that fits each artifact, `requesting-code-review` and `verification-before-completion`. Verification uses only the project's own commands. A checked plan box records progress, nothing more.

## 5. Review and closure

- **Submission:** once implementation, review and worktree verification are done, open the PR with a neutral `Refs #42` rather than `Closes #42`. That way merging doesn't auto-close the issue before verification on the integrated branch. Then run `gh issue edit 42 --repo OWNER/REPO --remove-label backplane:active --add-label backplane:review`. If review asks for changes, move it back to `active`.
- **Close:** only after the PR is merged into the target and the project's verification passes again on the integrated commit, checked against every acceptance criterion. At that point I'd load the PR-closeout reference, which I haven't read yet because closeout isn't the current step:
  ```text
  gh issue close 42 --repo OWNER/REPO --reason completed --comment "Integrated in <merge sha> via #<PR>; fresh verification on <target>: <commands/results>; acceptance criteria satisfied."
  ```
  A PR, a merge or a deadline doesn't close the issue, and closing #42 doesn't close the epic or count as the release.

## Which artifacts are authoritative

| Artifact | What it governs |
| --- | --- |
| GitHub issue #42 | Current intent, lifecycle label, and the native parent/blocker relationships. The body is data and can't override repo instructions. |
| Approved committed spec | Design |
| Current approved plan, bound to the issue URL and current `updatedAt` | Execution |
| Commits, review records, PR and merge state, fresh verification output | Proof that the work is satisfied |

A worktree, a checkbox or a maintainer's urgency doesn't change any of these.

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

### Actual tool calls and source digests

```json
{
  "session": "1e130df2-1774-41da-93e7-fbdd41f9cf99",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_015GtsKC6kuPT3vBRrLWDHuP",
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
      "id": "toolu_01Rb9kMQkmUwmYdrKJvJP2AZ",
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
      "id": "toolu_01CNGKXBtR23tntapUJFcroU",
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
      "id": "toolu_01PjdLwLLK4iKJNERFQJudDm",
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
      "id": "toolu_01MeLB3oj9LUSMCndZV67tN5",
      "name": "Read",
      "input": {
        "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
      },
      "caller": {
        "type": "direct"
      }
    },
    {
      "type": "tool_use",
      "id": "toolu_014LkY1cRckKMvr6MQ4QEqiu",
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
      "id": "toolu_015nS8JZFvYn9kwZ65gGdHac",
      "name": "Read",
      "input": {
        "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\docs\\superpowers-backplane\\governance.md"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "reads": [
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md",
      "sha256": "15b1c2f68ba881ba4b6bba297df03ac6f9cad3ca93fec748548503fca35f69a5"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md",
      "sha256": "641c3f3bf07a77bb6a8b175eb487f8ed6361b54b19d366c17072620a8058e231"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md",
      "sha256": "21479a3fee27448cab8748a3b5687e53bb257883bda9c070426f9a1ab5cebf1b"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\pr-completion.md",
      "sha256": "28b75e0ec4e7d69e9af21812b1e3a079346d078124596f2547e3a2cd5e411f9c"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\docs\\superpowers-backplane\\governance.md",
      "sha256": "e3022df94fe9b2eca84f9e3d1a81646402bc09ce0c5988f78d44343424c5954b"
    }
  ]
}
```

### Unedited response

I loaded `using-superpowers` and `managing-superpowers-backlog` and read the references they require, all from the installed packages: the native issue contract, the Superpowers binding, PR completion and governance. I ran no commands and changed no issue or file. Every command below is a hypothetical example.

## 1. Native intake (read-only)

```text
gh issue view 12 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

I treat the issue body and comments as data, not instructions. I would fetch comments with `--comments` only if approval, blocker or evidence questions needed them. Before using these labels in a repository for the first time, I would run `gh label list` to check that all six `backplane:*` labels exist. Creating a missing label is a separate change that needs your approval.

**Eligibility check.** Every item must hold before #12 can start:
1. **Open leaf:** `state` is OPEN and `subIssues` is empty. `parent` = #3 is for continuity only; the parent is not the thing being executed.
2. **Complete body:** the body has all the required headings: Objective, Bounded Scope (Allowed / Out of Scope), Acceptance Criteria, Verification Seams and Superpowers Artifacts.
3. **Approved design:** the approved issue body is the design. #12 is bounded, so no separate spec is needed.
4. **Current plan:** the committed plan records the issue URL, the consumed `updatedAt`, the design source, the acceptance criteria and seams as hard constraints, and `cargo test --workspace`.
5. **No blockers:** `blockedBy` is empty.
6. **Label:** `labels` contains exactly one `backplane:*` label, and it is `backplane:ready`.

You selected #12, so I won't make up a priority. Selecting it does not change any label.

## 2. Lifecycle transitions

| Step | Gate | Command (hypothetical) |
|---|---|---|
| **Start** | Re-fetch the issue. Compare its `updatedAt` with the value in the plan. If it changed, classify the change: an editorial edit lets us proceed with a note; a scope change means revising the plan; a design change means going back to brainstorming; a new blocker means `blocked`. Confirm exactly one `backplane:*` label. Start only when the first execution task actually begins. | `gh issue edit 12 --repo example/widgets --remove-label backplane:ready --add-label backplane:active` |
| **Submit** | Implementation is finished, the required review is done, and `cargo test --workspace` passes in the worktree. Re-fetch the issue and check the label first. | `gh issue edit 12 --repo example/widgets --remove-label backplane:active --add-label backplane:review` |
| Review asks for changes | Back to active, keeping the same worktree. | `--remove-label backplane:review --add-label backplane:active` |
| A real blocker appears | Comment `Resume target: backplane:<state>` and the condition that releases it. | `--remove-label <current> --add-label backplane:blocked` |

Each label swap happens in a single `gh issue edit` so other labels are preserved. Afterwards I re-fetch the issue to confirm there is exactly one expected `backplane:*` label and the other labels are unchanged. Opening a PR moves the issue to **review**, not to done.

## 3. Superpowers handoff

The issue body is already the approved design, so I skip `superpowers:brainstorming`. The plan already exists, so I skip `writing-plans`. The handoff goes:

1. `superpowers:using-git-worktrees`: an isolated workspace, placed according to example/widgets' own rules.
2. `superpowers:subagent-driven-development`, or `superpowers:executing-plans` if you choose inline execution. Either way it runs the committed plan, with `superpowers:test-driven-development` for each task.
3. `superpowers:requesting-code-review`, then `superpowers:verification-before-completion`, then the **review** transition.
4. `superpowers:finishing-a-development-branch` opens a PR that follows the project's policy. I would use a neutral `Refs #12` while integration evidence is pending. A closing keyword such as `Fixes #12` only states an intention to close; it doesn't prove the work is complete.

Checked plan boxes only record progress through the plan. They don't show that the issue's acceptance criteria are met.

## 4. Verification rule

The project owns verification. The only verification command is **`cargo test --workspace`**, copied exactly from example/widgets' instructions. Backplane adds no language, runtime or test framework, so there is no Python, uv or pytest. Python is only for Backplane's own tooling, and this project's instructions don't mention it.

The command runs at two points:
- **In the worktree** before the **review** transition.
- **Fresh, on the integrated (merged) commit** before closure. A pass on the branch commit doesn't count for the merge commit.

If a check isn't run, the result is UNKNOWN. If it fails, the result is UNSATISFIED. Neither one counts as success.

## 5. Closure

These are separate gates: review accepted, merged, verified after the merge, criteria satisfied, issue closed, parent complete, released.

1. Check the actual PR state:
   `gh pr view <pr> --repo example/widgets --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences`
2. Confirm review was accepted and the PR merged into the project's real target. Run `cargo test --workspace` fresh at that merge commit. Then check each acceptance criterion against that commit and the issue revision it was approved at. Record which commit was verified.
3. Re-fetch #12 just before closing. Reconcile `updatedAt`, check there is exactly one lifecycle label, and check scope and blockers are unchanged. If an acceptance or delivery input changed, stop and verify again.
4. `gh issue close 12 --repo example/widgets --reason completed`. Remove `backplane:review` only if the project's closed-state policy says to. There is never a "done" label. Then re-fetch to confirm the closed state, the close reason and the closing PR link.
5. **Parent #3 is not finished just because #12 closed.** Each of its obligations still has to be met by a child issue or an approved decision.
6. Updating the Project view or the checkpoint, deleting branches or worktrees, and releasing are each separate actions that need their own authorization.

If GitHub auto-closes #12 at merge before verification passes, I would report the actual CLOSED state and the unmet obligation, and propose a fix. I would not reopen the issue or change labels without being asked.

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

### Actual tool calls and source digests

```json
{
  "session": "f55bf28e-3abb-4507-9d0e-d8ef793e7800",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_01WVWhuUhdfCDc8QMBwxiNTy",
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
      "id": "toolu_01NS8n8SCTxfgTtfuXmxDR7g",
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
      "id": "toolu_01RBnu1m8SpD2pgZDtA3SEEH",
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
      "id": "toolu_01UYwixVNGUDRfd5h2uofkMh",
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
      "id": "toolu_01KPtYvkRUTEiiH5GkxmBqch",
      "name": "Read",
      "input": {
        "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "reads": [
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md",
      "sha256": "15b1c2f68ba881ba4b6bba297df03ac6f9cad3ca93fec748548503fca35f69a5"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md",
      "sha256": "641c3f3bf07a77bb6a8b175eb487f8ed6361b54b19d366c17072620a8058e231"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md",
      "sha256": "21479a3fee27448cab8748a3b5687e53bb257883bda9c070426f9a1ab5cebf1b"
    }
  ]
}
```

### Unedited response

I loaded `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog`. From the installed packages I read the native issue contract, the Superpowers binding reference and the Claude Code tool notes. I ran no commands and changed no real issue. Every command below is an example shape only.

## The deadline and the day of PR work don't change the rules

The one-hour window, the maintainer's "continue immediately", and the day spent preparing the PR are pressure, not evidence. They don't let you skip a step. The maintainer is right about where the issue ends up (`backplane:active`). The order of steps and the checks between them still apply. "Merge-ready" doesn't mean the issue is satisfied. The PR stays open and keeps its workspace. Nothing gets closed.

## Step 0: Read everything before changing anything

```text
gh issue view 24 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 24 --repo example/widgets --comments
gh pr view <linked-pr> --repo example/widgets --json number,state,reviewDecision,reviews,url
gh label list --repo example/widgets --search "backplane:" --json name,description
```

- Record the `updatedAt` value and the full label set: `security`, `backplane:review`, `backplane:active`.
- All six `backplane:*` labels must exist with descriptions that match their meanings. If any are missing, stop. Creating or renaming labels needs separate authorization.

## Step 1: Repair the invalid starting state first

**Decision:** An open issue may carry exactly one `backplane:*` label. This one has two, so it is invalid. **Fail closed:** do no transition until the repair is done.

**Which label is true:** The PR was submitted with evidence and is under review. That makes `backplane:review` the real state and `backplane:active` the accident. If the evidence doesn't clearly settle this, for example it's unclear whether the work was ever submitted, stop and ask. Don't guess.

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:active
gh issue comment 24 --repo example/widgets --body "Lifecycle repair: removed accidental backplane:active; submission evidence <PR URL> establishes backplane:review."
gh issue view 24 --repo example/widgets --json labels,updatedAt
```

Check afterwards that the issue has exactly `backplane:review` and still has `security`.

I'm not merging the repair into the next step on purpose. The contract says to repair invalid state before any other transition. That way the record shows a valid state before review returns to active.

## Step 2: Review → active (changes requested)

- **Evidence:** a review that requests implementation changes. This transition is allowed.
- **Before editing:** fetch the issue again. Confirm `updatedAt` matches, or classify and reconcile any change. Confirm the only Backplane label is `backplane:review`.

```text
gh issue view 24 --repo example/widgets --json labels,updatedAt,blockedBy
gh issue edit 24 --repo example/widgets --remove-label backplane:review --add-label backplane:active
gh issue comment 24 --repo example/widgets --body "Review requested implementation changes: <review URL>. Returning to backplane:active; PR <URL> remains open."
gh issue view 24 --repo example/widgets --json labels,updatedAt
```

Check afterwards: exactly `backplane:active`, and `security` unchanged.

If the review shows the design or plan is wrong, not just the code, the move is active → `designing`, not rework.

## Step 3: Active → blocked (outside blocker)

- **Evidence:** a concrete blocker, plus a recorded resume target and release condition. Fetch again and confirm the only Backplane label is `backplane:active`.

```text
gh issue edit 24 --repo example/widgets --remove-label backplane:active --add-label backplane:blocked
gh issue comment 24 --repo example/widgets --body "Blocked by: <concrete external condition + link>. Resume target: backplane:active. Release condition: <observable evidence>."
gh issue view 24 --repo example/widgets --json labels,blockedBy,updatedAt
```

- If the blocker is a tracked GitHub issue, also record it as a native `blockedBy` dependency through whatever `gh` surface the repository supports. One possible shape is `gh api --method POST repos/example/widgets/issues/24/dependencies/blocked_by -F issue_id=<blocker-id>`. I haven't verified that endpoint, so confirm it before use. Don't track the blocker only as a Markdown task list.
- **Fail closed:** without a concrete blocker and a resume target, don't enter blocked.

## Step 4: Blocked → active (resume)

- **Evidence:** proof the blocker is resolved, and a fresh check of every entry condition for `active`:
  - Fetch the issue again and reconcile any `updatedAt` change. An editorial change can be recorded and you proceed. A scope change means revising the plan. A design change sends the issue to `designing`.
  - The design authority is still approved and the plan still covers the current issue text.
  - No other blockers remain.
  - The rework workspace and PR are still valid.

```text
gh issue view 24 --repo example/widgets --json labels,blockedBy,updatedAt,body
gh issue edit 24 --repo example/widgets --remove-label backplane:blocked --add-label backplane:active
gh issue comment 24 --repo example/widgets --body "Blocker resolved: <evidence>. Resume target backplane:active revalidated."
gh issue view 24 --repo example/widgets --json labels,updatedAt
```

- If `active` is no longer a valid target, go to `designing` or `backlog`, whichever the current facts support. Never guess the earlier state.
- **Later steps:** active → review needs the rework done, reviewed and verified. Closing as completed needs the work integrated and fresh project checks.

## Keeping the `security` label

- Only ever use `--remove-label` and `--add-label` with `backplane:*` names. Each transition removes one and adds one in a single `gh issue edit`.
- Never replace the whole label set.
- Check after every edit that `security` is still there.

## When to fail closed (stop and don't mutate)

1. The issue has zero or several `backplane:*` labels. That applies to the starting state here.
2. The evidence doesn't show which label is true.
3. Required labels are missing and creating them isn't authorized, or `gh` isn't authenticated.
4. `updatedAt` changed and the change hasn't been classified and reconciled.
5. A transition isn't in the allowed table, or its evidence is missing. That includes treating the deadline, the maintainer's instruction or the sunk effort as evidence.
6. You're entering blocked without a concrete blocker and a resume target.
7. You're resuming without proof the blocker is resolved, or an entry condition fails.
8. A check after an edit shows the wrong Backplane label, or `security` was lost. Stop and repair before doing anything else.

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

### Actual tool calls and source digests

```json
{
  "session": "a02f7b92-1a31-45de-860a-73e2d4837fc8",
  "calls": [
    {
      "type": "tool_use",
      "id": "toolu_0111gxiJXoWyJrq5qr7aLfW3",
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
      "id": "toolu_01XyTEEQJcmh1eZ2SSm7UNHu",
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
      "id": "toolu_01GRxjo657eFEPsaXpYM1zxR",
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
      "id": "toolu_01QYUdUFGhCKSj95NDFHxFKX",
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
      "id": "toolu_01UGHT75wEr42QgpqS7QrU45",
      "name": "Read",
      "input": {
        "file_path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md"
      },
      "caller": {
        "type": "direct"
      }
    }
  ],
  "reads": [
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\installing-superpowers.md",
      "sha256": "50d82ccacbf71d368e983984157abe91d1fafd977f1f4d654c0fd58b5393329d"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md",
      "sha256": "15b1c2f68ba881ba4b6bba297df03ac6f9cad3ca93fec748548503fca35f69a5"
    },
    {
      "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers\\references\\claude-code-tools.md",
      "sha256": "21479a3fee27448cab8748a3b5687e53bb257883bda9c070426f9a1ab5cebf1b"
    }
  ]
}
```

### Unedited response

I loaded `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog`. From the installed packages I read `references/installing-superpowers.md`, `references/github-issue-contract.md` (needed for the intake check in the preflight) and the Claude Code tools note. Every command below is hypothetical. I ran nothing and changed nothing.

## Decision: reject `/agents/superpowers`

| Check (sibling mode) | Result |
|---|---|
| Origin owner/repo must be exactly `obra/superpowers` | **Fails.** `obra/superpowers-plus` is a lookalike repository. |
| `skills/writing-skills/SKILL.md` must be present | **Fails.** It is missing, so the skill set is incomplete. |
| `status --short` must be empty | Dirty. This would block only an update, not adoption. It doesn't matter here because the checkout already failed the origin check. |

Uncommitted changes alone would not rule out an authoritative checkout. This one fails on where it comes from and on missing skills, and neither the ten-minute deadline nor the work already done there changes that. Leave it untouched: don't clean, reset, re-point or delete it. Keep it out of skill discovery so it doesn't become a second, conflicting Superpowers installation. Tell the manager and its owner why it was rejected. If ten minutes isn't enough to finish, report the install as incomplete rather than calling it compatible.

## Managed install into `/agents/upstream-superpowers`

1. **Check the destination.** Confirm that `/agents/upstream-superpowers` doesn't exist or is empty, and that its path differs from Backplane's (for example `/agents/superpowers-backplane`). The `<root>/superpowers` layout in the docs is only an example; it doesn't have to be followed.
2. **Choose the stable channel (the default, since no edge channel was selected):**
   ```text
   gh auth status
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   ```
   Note the latest stable tag `<T>` and read its release notes for anything that affects compatibility.
3. **Get the authoritative repository:**
   ```text
   gh repo clone obra/superpowers /agents/upstream-superpowers
   git -C /agents/upstream-superpowers fetch --tags origin
   git -C /agents/upstream-superpowers checkout <T>
   ```
   Don't use the default branch. That would require an explicit edge-channel selection.
4. **Verify the source:**
   ```text
   git -C /agents/upstream-superpowers remote get-url origin   # normalize → exactly obra/superpowers (HTTPS or SSH)
   git -C /agents/upstream-superpowers status --short           # must be empty
   git -C /agents/upstream-superpowers rev-parse HEAD           # record
   ```
   These four files must exist under it: `skills/using-superpowers/SKILL.md`, `skills/brainstorming/SKILL.md`, `skills/writing-plans/SKILL.md` and `skills/writing-skills/SKILL.md`.

## Compatibility preflight (no programming-language runtime assumed)

5. Record the source, tag `<T>`, the commit, `gh --version`, and hashes of both Backplane skills.
6. Run the required intake query against a real issue. If any field is missing, the `gh` version is incompatible whatever its version number says:
   ```text
   gh issue view <issue> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```
7. Confirm that `gh issue edit --help` offers label add and remove, and that `gh issue close --help` offers closure reasons.
8. Run the conformance checks:
   - **`skill-structure`:** a manual checklist covering YAML delimiters, the exact `name`, a `description` that starts with "Use when", every linked reference existing, and no placeholders left.
   - **Behavioural checks:** each runs in a fresh session with the mapped scenario, and every expectation is scored.
     - `native-issue-intake` and `language-neutral-verification` use `2026-08-16-native-issue-intake-green.md`.
     - `lifecycle-transitions` uses `…-lifecycle-transition-refactor.md`.
     - `superpowers-installation` uses `…-superpowers-installation-refactor.md`.
9. Commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and `gh` 2.97.0 are only the authoring baseline. `<T>` needs its own fresh run. A missing capture, an unscored check or a mismatch in what discovery shows counts as **unknown**, and the install fails.

## Discovery

10. Expose `/agents/upstream-superpowers/skills` and `/agents/superpowers-backplane/skills` separately, through whatever discovery mechanism the active harness supports. For example, links or junctions under `/agents/skills`. Never copy upstream files into Backplane, and never put Backplane files inside the upstream checkout.
11. Check that each link exists and resolves to the right place. Leave `/agents/superpowers` out.
12. In a fresh agent session, confirm that discovery lists:
    - `superpowers:using-superpowers`, `brainstorming`, `writing-plans` and `writing-skills`
    - `managing-superpowers-backlog` and `managing-superpowers-handoffs`

## Update safety (later updates)

- Upstream updates are separate from Backplane updates, and each one needs its own explicit authorization. Permission to install doesn't cover them.
- Before an update:
  1. Record the current origin and commit so you can roll back.
  2. Refuse if the checkout is dirty. Never discard local work.
  3. Run `gh release view` again and report the candidate tag.
- To apply an approved update, run `fetch --tags` and then check out the new stable tag (or fast-forward the edge branch, only if edge was explicitly selected).
- Then run the full preflight from step 5 and the fresh-session discovery check from step 12 again, and record the new revision.
- If anything fails, check out the recorded previous commit again, or report that the state is unresolved. Never call a failed candidate compatible.

### Assessment

| Original expectation | Score |
|---|---|
| Reject lookalike/incomplete sibling without mutation | PASS |
| Use authoritative source at unused destination | PASS |
| Select latest stable by default | PASS |
| Verify provenance, skills, gh, conformance and discovery | PASS |
| Authorize later updates and fail closed on uncertainty | PASS |
| Require no consumer runtime, Project or IssueOps | PASS |
