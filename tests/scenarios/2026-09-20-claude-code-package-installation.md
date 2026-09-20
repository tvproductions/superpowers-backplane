# Claude Code package and installation evidence for #17

## Task 1 — package metadata

### Host contract

- Observed on 2026-09-20: `claude --version` returned `2.1.241 (Claude Code)`.
- `claude plugin marketplace add --help` accepts a URL, path, or GitHub repository and supports user, project, and local scopes.
- `claude plugin install --help` accepts `plugin@marketplace` and `--scope user`.
- `claude plugin validate --help` supports `--strict`.
- Current official docs reviewed: [plugin format](https://code.claude.com/docs/en/plugins), [marketplace sources](https://code.claude.com/docs/en/plugin-marketplaces), and [native installation](https://code.claude.com/docs/en/discover-plugins). They place `plugin.json` inside `.claude-plugin/`, skills at plugin root, and resolve a relative marketplace source from the marketplace root. A local-directory relative source loads the plugin in place.
- No observed host-contract change requires a different root package layout.

### RED before metadata

- `Test-Path .claude-plugin/plugin.json` → `False`.
- `Test-Path .claude-plugin/marketplace.json` → `False`.
- The root package cannot supply a Claude marketplace until those files exist.
- Root `plugin.json` version: `0.1.0`.
- Canonical skill files exist at `skills/managing-superpowers-backlog/SKILL.md` and `skills/managing-superpowers-handoffs/SKILL.md`.

### GREEN after metadata

- `claude plugin validate --strict .` and `claude plugin validate --strict .claude-plugin/plugin.json` both exited 0 with `Validation passed` after the two metadata fields were added.
- PowerShell `ConvertFrom-Json` parsed both Claude files and root `plugin.json`. Names and versions match `superpowers-backplane` and `0.1.0`; the marketplace has one plugin whose source is `./`, resolving to the repository root.
- Each canonical `SKILL.md` has one tracked source path, and no `.claude-plugin/skills` copy exists.
- `git status --short --untracked-files=all` listed only the two intended Claude JSON files and this scenario record.

### Native strict-validation RED

- `claude plugin validate --strict .` exited 1. Claude Code 2.1.241 reported two warnings: missing marketplace `description` and missing plugin `author`.
- Both fields are supported optional metadata in the current official Claude docs. Strict validation is the plan's gate, so this candidate cannot pass unchanged.
