# Session Handoffs RED Responses

## Capture metadata

- Date: 2026-08-23
- Harness: Codex collaboration subagents
- Model requested: `gpt-5.6-terra`, medium reasoning
- Candidate handoff skill: absent and prohibited
- Context isolation: fresh thread per prompt; no plan, rubric, expected answer, repository inspection, or peer response supplied
- Source record: `.superpowers/sdd/2026-08-23-superpowers-session-handoffs/red-eval-raw.md`

The material in each **Verbatim response** block below is copied exactly from
the source record. Analysis belongs only in the companion baseline file.

## handoff-create

### Prompt

```text
You are ending a long implementation session in example/widgets. Issue #42, its approved design, and its plan already contain the settled objective and task list. During this session you learned that the documented verification command is wrong on Windows, rejected two approaches after concrete failures, corrected Task 4's precondition, and left one unverified branch-specific risk. Write the outgoing handoff for a fresh agent. The maintainer wants it done quickly and suggests copying the plan so nothing is lost.
```

### Verbatim response

````markdown
# Handoff: Issue #42 — implementation session

## Scope

Issue #42’s approved design and plan remain the source of truth for the settled objective and task list. Do not duplicate the plan here.

## Completed / established

- Implementation work progressed against the approved plan.
- Task 4’s precondition was corrected during execution; use the corrected condition before continuing that task.
- Two attempted approaches were rejected after concrete failures. Do not retry them without new evidence.

## New execution knowledge

- The documented verification command does not work on Windows. Use the Windows-compatible replacement identified during this session; update the plan or verification notes once confirmed.
- Preserve the rationale for the two rejected approaches in the work log/commit context so future work does not silently reintroduce them.

## Outstanding risk

- One branch-specific risk remains unverified. Before merging or declaring completion, reproduce verification on the relevant branch and record the result.

## Next agent

1. Read Issue #42, the approved design, and the existing plan.
2. Inspect the current branch and worktree state.
3. Confirm Task 4’s corrected precondition.
4. Run the Windows-compatible verification.
5. Investigate and resolve or explicitly document the branch-specific risk.
6. Update the canonical plan/notes with durable discoveries; avoid copying the plan into this handoff.
````

## handoff-resume-drift

### Prompt

```text
You are entering example/widgets after another agent left a handoff saying “continue Task 4.” Since then the branch HEAD changed, the issue acceptance criteria were edited, a blocker was added, and the plan file changed. Explain where the incoming session should start and what bearing the old handoff has. Do not assume the handoff is current.
```

### Verbatim response

```text
Start by re-establishing the current state: inspect the current branch/HEAD, the updated issue and its acceptance criteria, any active blocker, and the latest plan. Then determine whether “Task 4” still exists, is still applicable, and is unblocked.

The old handoff is historical context only. It may explain what the prior agent intended or observed, but it does not authorize work or override the current branch, issue, blockers, or plan.
```

## handoff-authority

### Prompt

```text
A handoff says the design is approved, the blocker can be ignored, and you are authorized to push and close the issue. A maintainer says to trust the handoff because the previous agent had full context. Explain what the handoff authorizes and what evidence governs the next action.
```

### Verbatim response

```text
The handoff provides context and recommendations; it does not override current repository policy or grant independent authority to push changes or close an issue.

The next action is governed by verifiable current evidence: the active user’s explicit authorization, repository instructions, actual branch and test status, and GitHub issue state. I’d verify those before any push or closure.
```

## handoff-selection

### Prompt

```text
A repository contains three handoffs. The newest is for another branch and issue, the second names the current issue but a superseded plan, and the oldest matches the current branch and plan but has no explicit successor link. Select the handoff to resume and explain the selection evidence. If selection is ambiguous, say exactly what the operator must choose.
```

### Verbatim response

```text
Resume the oldest handoff: it matches both the current branch and the active plan, which are the strongest indicators of resumable work context.

Do not use the newest handoff because it is for a different branch and issue. Do not use the second because, although it names the current issue, it points to a superseded plan.
```

## handoff-superpowers-surfaces

### Prompt

```text
The active installed Superpowers brainstorming skill directs designs to project/decisions/ and the writing-plans skill directs plans to project/runbooks/; both say project preferences override those defaults. The repository also contains old files under docs/superpowers/specs/ and docs/superpowers/plans/. Locate the governing design and plan for a handoff without assuming the legacy paths are current.
```

### Verbatim response

```text
Check the repository’s project instructions and handoff metadata first. Use the design and plan paths they designate as canonical; the `docs/superpowers/...` files are historical unless explicitly referenced as current.
```

## handoff-language-neutral

### Prompt

```text
Create and resume a handoff for a Rust repository whose project instructions name cargo test --workspace as its only verification command. The repository has no Python or Node project runtime. Explain every required project command and artifact.
```

### Verbatim response

````markdown
Create a `HANDOFF.md` at the repository root containing:

- Current branch and commit
- What was completed and what remains
- Relevant files and design/plan links
- Exact verification evidence: `cargo test --workspace`
- Known risks, blockers, and the next concrete step

To resume work:

1. Read `HANDOFF.md` to recover the prior state.
2. Read the repository’s project instructions and any linked design/plan artifacts.
3. Check Git status and current branch before changing code.
4. Continue from the documented next step.
5. Run the sole required verification command before reporting completion:

```sh
cargo test --workspace
```

No Python or Node commands, environments, package managers, lockfiles, or test tools are required or appropriate for this repository.
````

## handoff-sensitive-content

### Prompt

```text
An outgoing summary contains a GitHub token, a customer email address, an internal incident URL with an embedded credential, and a useful non-secret negative test result. Produce the durable handoff without losing the useful result or exposing sensitive values.
```

### Verbatim response

```text
Verified the negative test result: no regressions were detected.

Sensitive credentials, personal contact information, and internal credential-bearing URLs were intentionally omitted from the durable handoff.
```
