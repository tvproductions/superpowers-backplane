# Agent Instructions

## Session Entry

- Read `HANDOFF.md` before taking project action.
- Read `SUPERPOWERS.md` for the installed upstream dependency channel and
  resolved revision.
- Read the complete design at
  `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md`.
- Read the current plan at
  `docs/superpowers/plans/2026-08-16-superpowers-backplane-bootstrap.md`.
- Before any Git mutation, require `git rev-parse --show-toplevel` to resolve
  exactly to this repository root. If it resolves elsewhere or fails, stop and
  establish the standalone repository boundary first.
- Issue #31 execution exception, expressly approved by the operator: the exact
  workspace returned by the authorized native worktree creation may also be
  mutated after its root, registration, shared Git directory, and recorded
  branch/detached identity are verified against this repository. No other
  worktree is authorized by this exception. Record the returned identity in
  the execution ledger before mutations there.
- Treat this project as a companion fitted to upstream Superpowers in every
  workflow decision. It is not a standalone generic backlog framework.

## Runtime and Tool Boundary

- Remain language-neutral. Do not assume Python, Node.js, or another project
  runtime.
- **NO pytest. EVER.** Do not add, suggest, or assume pytest.
- Require GitHub CLI (`gh`) for GitHub operations. Assume Git because
  Superpowers itself requires Git workflows.
- Use native GitHub issue hierarchy, dependencies, issue types, labels, linked
  pull requests, and closure relationships. Do not require GitHub Projects or
  introduce IssueOps.

## Superpowers Dependency

- Use `.agents/superpowers` as the upstream Superpowers checkout when working
  on this repository.
- Keep the upstream checkout independently identifiable and updateable; do not
  copy upstream Superpowers files into this repository's tracked source.
- Treat shipped Superpowers contents as read-only for Backplane work, including
  `.agents/superpowers`, installed plugin caches, and discovery links that resolve
  into them. Never place Backplane documents, configuration, or generated state
  inside those installations. A separately authorized upstream update is distinct
  from writing project artifacts.
- Backplane installation must adopt a compatible, separately installed
  Superpowers plugin or sibling checkout, or obtain upstream through the
  active harness's documented channel.
- Favor following new compatible upstream releases over indefinite pinning.
- Use the stable upstream release channel by default. Use the upstream default
  branch only after an explicit edge-channel selection.

## Workflow

- Minimize skill overhead. Invoke only skills whose procedures are needed for
  the current request; do not chain through generally related skills.
- Treat Git sync as bidirectional: fetch and reconcile remote changes, include
  explicitly authorized local artifacts, and verify remote arrival. Do not call
  a sync complete while requested local artifacts remain untracked or unpushed.
- Routine Git synchronization and small documentation/evidence publication need
  only guarded Git/file operations and verification. Do not invoke the full
  brainstorming, planning, worktree, execution, TDD, review, or branch-finishing
  sequence unless the request actually involves that work.
- For substantive design or implementation work, follow upstream Superpowers in
  order: brainstorming, isolated worktree when applicable, writing-plans,
  execution, TDD appropriate to the artifact, review, verification, and branch
  finishing.
- Use `superpowers:writing-skills` before creating or changing a skill.
- Store new Backplane designs under `docs/superpowers-backplane/specs/` and plans
  under `docs/superpowers-backplane/plans/`. Existing `docs/superpowers/`
  authorities remain at their recorded paths; that directory is project-owned,
  not the upstream installation.
- Use `superpowers-backplane` or `sp-bp` for Backplane-owned artifact namespaces.
  Never write anything to `.superpowers/`, including through invoked upstream
  scripts or helpers. Read existing contents only when needed. If a Superpowers
  workflow requires writing there, stop that write and reconcile a supported
  alternative outside the reserved directory; do not patch shipped upstream
  files to redirect it. Use `.sp-bp/` for any later approved
  Backplane-local working state and `docs/superpowers-backplane/` for documents.
- Do not publish, create a remote repository, or release without explicit user
  authorization.
- Issue #31 native inline bookkeeping exception, expressly approved by the
  operator: use native file operations for briefs, append-only progress, and
  the final review package under `.sp-bp/work/2026-10-11-github-governance-bridges-implementation/`.
  Ignore `.sp-bp/work/` before use; keep the checkpoint pair trackable. Replace
  only upstream helper invocation, preserving task order, TDD, rulings,
  verification, fresh whole-change review, and branch finishing. Never invoke
  a helper that writes to `.superpowers/` or patch upstream to redirect it.
- Issue #31 cross-machine recovery: at a machine or harness handoff, commit a
  tracked execution summary and the evidence supporting its verified claims.
  Keep disposable scratch under ignored `.sp-bp/work/`; do not rely on it as
  the sole resume source. Record exact plan/spec/probe and issue revisions,
  workspace identity, task dispositions, evidence/commit identities, unresolved
  findings, and the first task requiring revalidation. Verify authorized
  transport and arrival before claiming another host can resume. Missing
  predecessor evidence remains unknown. Preserve the approved plan/spec bytes.
