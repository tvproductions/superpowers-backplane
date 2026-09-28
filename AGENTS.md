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
- Treat this project as a companion fitted to upstream Superpowers in every
  workflow decision. It is not a standalone generic backlog framework.

## Runtime and Tool Boundary

- Implement Backplane's 1.0 catalog, issue reconciliation, traceability, V&V,
  generated views, release logic, CLI/helpers, and tests in Python under
  `docs/superpowers/specs/2026-09-27-python-core-adr.md`. Keep host-specific
  adapters thin. Do not build or maintain a parallel Go core. Remain neutral
  about an adopting project's language and test runner. The Python source alone
  does not approve an adopter runtime requirement; prove and document the
  installed invocation before claiming heavy readiness.
- Use only Astral's `uv`/`uvx` for Python environment and package tooling,
  `ruff` for lint/format, and `ty` for type checking. Run standard-library
  `unittest` through `uv run`. Keep the declared Python and tool versions in
  `.python-version`, `pyproject.toml`, and `uv.lock` coherent.
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
- Backplane installation must adopt a compatible, separately installed
  Superpowers plugin or sibling checkout, or obtain upstream through the
  active harness's documented channel.
- Favor following new compatible upstream releases over indefinite pinning.
- Use the stable upstream release channel by default. Use the upstream default
  branch only after an explicit edge-channel selection.

## Workflow

- Follow upstream Superpowers in order: brainstorming, isolated worktree when
  applicable, writing-plans, execution, TDD appropriate to the artifact,
  review, verification, and branch finishing.
- Use `superpowers:writing-skills` before creating or changing a skill.
- Store designs under `docs/superpowers/specs/` and plans under
  `docs/superpowers/plans/`.
- Do not publish, create a remote repository, or release without explicit user
  authorization.
