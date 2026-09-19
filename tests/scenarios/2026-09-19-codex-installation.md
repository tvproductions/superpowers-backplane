# Codex Installation Surface: Issue #3

- Issue: https://github.com/tvproductions/superpowers-backplane/issues/3
- Approved design: `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`
- Approved plan: `docs/superpowers/plans/2026-09-19-codex-installation-surface.md`
- Execution branch: `feat/codex-installation-surface`

## Task 1: Root package and marketplace

### RED expectations

1. The repository must expose one root `plugin.json` with ID `superpowers-backplane`, version `0.1.0`, and the canonical `skills/` tree.
2. `.agents/plugins/marketplace.json` must be tracked while the independent upstream checkout and discovery junction remain ignored.
3. Codex must resolve exactly one `superpowers-backplane@superpowers-backplane` selector from this repository.

### RED observations (2026-09-19)

- Host: `codex-cli 0.155.1` on Windows PowerShell 7.6.6.
- `git check-ignore -v .agents/plugins/marketplace.json` returned `.gitignore:1:.agents/`, so the marketplace path was hidden.
- `plugin.json` and `.agents/plugins/marketplace.json` were absent.
- `codex plugin list --available --json` filtered to the Backplane selector returned `matching=0`.
- That catalog command exited 0 but warned that a remote plugin catalog request to `chatgpt.com` failed. The RED result establishes local absence only; the later GREEN check must inspect local resolution directly.
- Current canonical authored skills: `managing-superpowers-backlog` and `managing-superpowers-handoffs`.

### GREEN evidence

- Portable `plugin.json` and repository marketplace JSON parsed; names, version `0.1.0`, `./` source, `AVAILABLE`/`ON_USE` policy, and two canonical authored skill folders matched the plan.
- `.agents/superpowers` and `.agents/skills/superpowers` remained ignored. `git check-ignore -q .agents/plugins/marketplace.json` exited 1, and `git status --short --untracked-files=all` showed the marketplace file.
- `codex plugin list --available --json` from the repo root still returned `matching=0`. The current CLI considered only four already configured marketplaces; it did not automatically register this repository marketplace. This invalidated the plan's implicit CLI discovery assertion, not the package metadata.
- In disposable `CODEX_HOME=.superpowers/sdd/2026-09-19-codex-installation-surface/task1-codex-state`, `codex plugin marketplace list --json` initially listed no marketplaces. `codex plugin marketplace add <this repository root> --json` returned `marketplaceName=superpowers-backplane`, `alreadyAdded=false`, and the exact repository root. A following `codex plugin list --available --json` found exactly one `superpowers-backplane@superpowers-backplane` at version `0.1.0`.
- An attempted `Start-Process` probe with redirected stdout exited 1 with `stdout is not a terminal`; the successful disposable probe set `CODEX_HOME` only inside its PowerShell process and invoked `codex` directly. Task 3 must use a terminal-compatible isolated invocation for fresh sessions.

## Codex acceptance matrix

| Case | Status | Evidence |
|---|---|---|
| Clean install | PENDING | Task 3 |
| Compatible upstream native adoption | PENDING | Task 3 |
| Compatible upstream sibling adoption | PENDING | Task 3 |
| Upstream absent, stable setup | PENDING | Task 3 |
| Repeat install | PENDING | Task 3 |
| Compatibility preflight | PENDING | Tasks 2–4 |
| Version change and rollback | PENDING | Task 3 |
| Pinned remote Git ref restoration | PENDING | Task 4 |
| Backplane-only uninstall | PENDING | Task 3 |
| Preservation and failure probes | PENDING | Task 3 |
| Three-skill fresh discovery | PENDING | Tasks 3–4 |
| Authorized lifecycle and five conformance checks | PENDING | Task 4 |
