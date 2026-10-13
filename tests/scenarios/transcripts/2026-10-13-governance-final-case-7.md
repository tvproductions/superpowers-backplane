The proposed execution is compatible **only with a narrowly scoped worktree and native-bookkeeping exception**. The installed helper’s hardcoded `.superpowers/sdd` writes make it impermissible here. Redirecting a task brief’s visible output would not remove its indirect writes.

This probe authorizes assessment only. I performed file reads; I made no GitHub queries, mutations, helper invocations, worktree creation, or agent dispatches. Repository handoff history is not evidence for the invented `example/governance-fixture` state.

The governing distinction comes from the [backlog skill](skills/managing-superpowers-backlog/SKILL.md) and [governance contract](docs/superpowers-backplane/governance.md): project rules control paths and isolation, while Backplane preserves upstream Superpowers’ execution discipline.

**Proposed compatible execution sequence**

1. **Establish execution authority and inputs.** Obtain the complete synthetic issue-31 record, approved specification and current issue-bound plan, their exact revisions, approval scope, and project verification commands. Preserve approved plan/spec bytes. Resolve new design questions through brainstorming without repeating already approved decisions.
2. **Establish isolation.** Inspect the executing workspace’s identity before deciding whether creation is needed. An unrelated registered worktree is neither the selected workspace nor authorization to reuse it. If a distinct issue-31 workspace is required, use authorized native creation from the verified repository root. A creation failure does not authorize implementation in the dirty root.
3. **Verify the returned workspace.** Confirm its canonical top-level path, worktree registration, shared Git directory, starting commit, and recorded branch or detached identity against the originating repository. Record that returned identity before task or Git mutations there.
4. **Prepare permitted bookkeeping.** Ignore only `.sp-bp/work/` before use, while keeping `.sp-bp/state.md` and `.sp-bp/github-state.json` trackable. Validate path containment and reject links into protected installations. Use native file operations under `.sp-bp/work/2026-10-11-github-governance-bridges-implementation/`.
5. **Execute inline in plan order.** Create task briefs manually from the approved plan, including its global constraints and interfaces. Record each task’s BASE commit, observed verification results, completion evidence, and rulings in append-only progress. Preserve artifact-appropriate RED→GREEN checks. Do not invoke `sdd-workspace`, default-output task-brief, or another helper with prohibited indirect writes.
6. **Review and finish.** Prepare the whole-change review package natively. Preserve a fresh whole-change review gate; this probe performs none. Future review arrangements must respect the applicable agent restriction rather than silently substitute author self-review. Integration, publication, cleanup, and closure remain separately gated.

**Required exception scope**

A concrete execution authorization should identify:

- Native worktree creation from the exact verified repository root.
- Mutation permission for **only the exact returned workspace**, after identity verification; no permission for the unrelated worktree.
- Native replacement of helper bookkeeping at the exact scratch path above.
- Preservation of task order, TDD, rulings, verification, fresh review, and branch finishing.
- Continued prohibition on `.superpowers/` and shipped upstream writes.

The supplied AGENTS.md records issue-31 exceptions, but this read-only probe does not exercise them or extend them to an invented workspace. No extra skill bundle is required, and none should be installed to resolve the helper conflict.

**Guarded resume**

Resume must reconcile current instructions, issue semantics, approved artifact identities, workspace identity, commits, and supporting evidence. A ledger completion line is usable only when its plan identity, commit range, and evidence remain applicable. Missing predecessor evidence stays **UNKNOWN**; begin with the first task requiring revalidation instead of guessing prior progress.

At a machine or harness boundary, preserve a tracked execution summary and supporting evidence containing exact issue/plan/spec/probe revisions, workspace identity, task dispositions, commit identities, unresolved findings, and the first revalidation task. Ignored scratch cannot be the sole recovery source. Authorized transport and exact arrival must be demonstrated before claiming another host can resume.

Checkpoint recovery has separate guards: inspect receipts, HEAD, index, and both literal output paths. Verify an already accepted pair commit rather than rolling it back. Before acceptance, restore only transaction-owned pair files and index entries under recovery authority; intervening user edits or unexplained identity changes stop automatic recovery.

**Evidence gaps and checks requiring demonstration**

| Check | Present assessment |
|---|---|
| Issue eligibility and plan binding | No complete named synthetic issue-31 record or approved execution artifacts were supplied; eligibility cannot be established. |
| Workspace boundary | Requires actual root, registration, common-Git-directory, HEAD, and branch/detached observations. |
| Ignore and containment behavior | Requires actual checks proving scratch is ignored, the checkpoint pair remains trackable, and resolved paths stay permitted. |
| Task completion and compatibility | Requires observed project checks, operational discovery, and applicable conformance evidence; installed-version text is insufficient. |
| Checkpoint acceptance/recovery | Requires demonstrated validation, pair-only commit scope, interruption handling, user-edit preservation, and unrelated-state preservation. |
| Cross-machine continuity | Requires verified transport, arrival, and inspectable supporting evidence. |

The next permissible actions **within this probe** are read-only refinement and assessment of additional supplied fixture evidence. Worktree creation, bookkeeping writes, execution, commits, checkpoint installation or recovery, GitHub changes, and publication remain proposed operations. No satisfaction, readiness, or successful resume conclusion is supported yet.