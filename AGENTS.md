# Agent Instructions

## Session Entry

- Read `HANDOFF.md` before taking project action.
- Read `SUPERPOWERS.md` for the installed upstream dependency channel and
  resolved revision.
- Read the complete design at
  `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md`.
- Read the current plan at
  `docs/superpowers/plans/2026-08-16-superpowers-backplane-bootstrap.md`.
- Before any Git mutation, establish the intended repository identity. Project
  source changes belong in this standalone repository or a verified registered
  worktree sharing its Git directory. Disposable verification repositories are
  governed by the verification-workspace rules below. Never accidentally mutate
  an enclosing repository or an unrelated checkout.
- Treat this project as a companion fitted to upstream Superpowers in every
  workflow decision. It is not a standalone generic backlog framework.

## Verification Workspaces

- An approved task or implementation plan authorizes the reversible local
  operations needed to test it: disposable clones/repositories, fixture commits
  and branches, deliberately dirty or incomplete fixture files, fixture remote
  configuration, and isolated native-host installation/lifecycle checks. Do not
  request a new exception for each fixture or require plan publication before
  local execution. Publication and release retain their separate authorization.
- Put disposable repositories, profiles, catalogs and native execution records
  under ignored `.sp-bp/work/<work-item-or-plan>/`. Verify ignore coverage and
  canonical containment before use, accounting for links and junctions. A fixture
  must not resolve to the project root, an existing installation or unrelated
  user data. Inspect occupied paths; do not adopt or overwrite unknown contents.
- Before creating a fixture repository, verify its existing parent is inside the
  recorded fixture area. After creation, record its canonical root, origin,
  starting revision and purpose in the execution ledger. Before later Git
  mutations, require `git rev-parse --show-toplevel` for that target to match its
  recorded fixture root. For intentional provenance or dirty-state tests, record
  the planned deviation and compare against it rather than the real upstream.
- Prefer native worktree creation when the selected workflow calls for a
  worktree. Verify its canonical root, registration, shared Git directory and
  branch/detached identity against this repository before project mutations;
  record the identity in the execution ledger. No issue-specific exception is
  needed for a worktree authorized by the selected workflow.
- Shipped upstream installations remain read-only. Tests may modify independently
  created disposable copies whose source and identity were verified. Local clones
  must not share writable object stores or use alternates pointing at protected
  repositories; use `git clone --no-hardlinks` for local fixture clones. Do not
  place Backplane artifacts in real upstream checkouts or installed plugin caches.
  Native host operations may manage their own caches in isolated test profiles.
- Use child-scoped configuration for disposable host profiles. Reuse verified
  authorized authentication where the host supports it; never copy credentials
  or silently fall back to a normal profile. Installing a missing dependency in
  an isolated test profile is included when required by the approved test; changing
  an existing development/normal-profile upstream installation is separate work.
- Keep helpers, briefs, append-only progress and review packages in the plan's
  `.sp-bp/work/` area using native file operations when upstream helpers would
  write to `.superpowers/`. Preserve task order, TDD appropriate to the artifact,
  verification, fresh review and branch finishing. Do not patch shipped helpers.
- Treat fixture results as tests, not product changes or publication. Keep
  fixture-only versions and deliberately broken data out of product source and
  releases. Retain supporting evidence in tracked project records. Before any
  cleanup, verify the exact owned paths and containment; never remove unknown
  work, the standalone repository, an upstream installation or another task's
  fixtures. Follow the platform's filesystem safety rules.

## Runtime and Tool Boundary

- Keep consuming-project workflows language-neutral; their own instructions
  govern their runtime and verification tools.
- Use Python for Backplane-owned cross-platform tooling. Use Astral products
  strictly and thoroughly for all Python needs: `uv` for Python versions,
  environments, dependencies, tool installation, and execution; Ruff for
  linting and formatting; and `ty` for type checking.
- Use uv-managed Python 3.14 for this repository's tooling and `.venv`.
  `.python-version` records the verified patch; keep it and the environment
  aligned. Preserve historical verification records at their original runtimes.
  Create the environment with `uv venv --managed-python .venv` and execute
  Python through `uv run --no-project python` from this repository root.
- Keep orchestration portable across Windows, macOS, and Linux: use Python
  paths, explicit text encodings, and shell-free subprocess argument lists.
  Limit shell-specific code to adapters for an explicitly tested shell surface.
- **NO pytest. EVER.** Do not add, suggest, or assume pytest.
- Require GitHub CLI (`gh`) for GitHub operations. Assume Git because
  Superpowers itself requires Git workflows.
- Use native GitHub issue hierarchy, dependencies, issue types, labels, linked
  pull requests, and closure relationships. Do not require GitHub Projects or
  introduce IssueOps.

## Companion Starter Guidance

- [gz-skills-first-starter](https://github.com/tvproductions/gz-skills-first-starter)
  is the authoritative shared engineering and release policy alignment source.
  Follow [docs/release-policy.md](docs/release-policy.md): check the source before
  release preparation, at scoped policy/tooling maintenance and when notified of
  relevant changes. Record the reviewed revision, applicability, decisions and
  approved exceptions; local summaries must not silently redefine source policy.
- Adopt its SemVer, coherent minor-release bundling and prospective newly written
  PRD requirement for every Backplane major, including 1.0.0. Keep Backplane's
  issue-bound release acceptance and publication authority.
- Backplane owns requirements tracking, labeling, backlog/release monitoring,
  handoffs and [lite/heavy mode definitions](docs/superpowers-backplane/modes.md).
  The starter refers to these authorities and supplies no competing lifecycle.
  Distinguish intended mode capabilities from verified implementation.
- Do not directly adopt the starter or bootstrap its bundle into Backplane:
  the starter directs adopters to this project, so doing so would create a
  circular adoption relationship. Do not claim formal starter conformance.
- Apply useful practices through explicit Backplane-owned decisions, preserving
  independent component ownership. Keep consuming-project workflows language-neutral;
  this repository's Python/Astral tooling policy does not become an adopter requirement.
- Record applicable policy differences with evidence, maintainer approval, an
  owner and a dated revisit condition. This explicit release-policy alignment
  does not silently upgrade runtime, packaging or dependencies, or certify full
  starter conformance. Portable workflows retain each consumer's policy.

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
- Cross-machine recovery: at a machine or harness handoff, commit a
  tracked execution summary and the evidence supporting its verified claims.
  Keep disposable scratch under ignored `.sp-bp/work/`; do not rely on it as
  the sole resume source. Record exact plan/spec/probe and issue revisions,
  workspace identity, task dispositions, evidence/commit identities, unresolved
  findings, and the first task requiring revalidation. Verify authorized
  transport and arrival before claiming another host can resume. Missing
  predecessor evidence remains unknown. Preserve the approved plan/spec bytes.
