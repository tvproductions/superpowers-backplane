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

## Task 2 — pinned guide

### Documentation RED

- `README.md` links the Codex guide but has no Claude Code guide link.
- `docs/installing-claude-code.md` does not exist.
- No adopter-facing Claude instructions yet provide a reviewed 40-character source commit, origin/publication preflight, native marketplace and plugin commands, an existing target-repository issue for read-only native intake, a setup request, or three-skill fresh-session discovery.

### Documentation GREEN

- `README.md` links `docs/installing-claude-code.md`.
- The guide requires a reviewed 40-character published commit, checks the exact clone origin and resolved SHA, inspects both Claude manifests and root skills, and validates the native package before installation.
- It shows `claude plugin marketplace add $backplaneCheckout`, `claude plugin install superpowers-backplane@superpowers-backplane --scope user`, and `claude plugin list` for one canonical Backplane package.
- It accepts an existing target-repository issue, shows the complete read-only native intake fields, and requests setup in a new Claude session.
- It names all three fresh-session skill identities and defers pinned update, rollback, and Backplane-only uninstall to #19. It does not change issues during setup or require a consuming-project runtime or edits to `.agents/superpowers`.
- Verification: 14 required guide strings were present; PowerShell parsed all three command blocks with zero syntax errors; the README link and forbidden-command scan passed. Full pinned-source replay remains Task 3.

## Task 3 — isolated published-source smoke (in progress)

### Isolation and capability preflight

- Disposable Claude configuration: `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-241ec92c05e84296bc7a2df74be839d3`. It was unused when created. `CLAUDE_CONFIG_DIR` was set only around child Claude commands; no credentials were copied.
- Initial `claude auth status --json` reported `loggedIn: false` (exit 1). The operator was asked to authenticate this disposable profile; live-session discovery remains `UNKNOWN` pending that prerequisite.
- Initial isolated inventory: no marketplaces and no plugins. The normal Claude profile inventory was saved separately for a later preservation comparison.
- Host: Claude Code `2.1.241`. `gh auth status` passed; the full #17 intake returned all 15 required native fields, and `gh issue edit --help` and `gh issue close --help` expose label add/remove and closure reason.

### Independent upstream source

- Repository checkout: `.agents/superpowers`; origin `https://github.com/obra/superpowers.git`; stable release `v6.4.1` at `5bf4e78011075bcfc0dc295f0724994cd123ee71`.
- The upstream Claude manifest names `superpowers` version `6.4.1`; its own marketplace names `superpowers-dev` with one `superpowers` entry. The required upstream skill files exist. Native installation into the disposable profile is pending authentication.

### Published Backplane source

- Published feature commit: `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a`; `gh api repos/tvproductions/superpowers-backplane/commits/<SHA> --jq .sha` returned that exact SHA.
- Disposable clone: `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane`. Replayed `gh repo clone tvproductions/superpowers-backplane` and `git -C <checkout> checkout --detach <SHA>`. Its origin is `https://github.com/tvproductions/superpowers-backplane.git`, HEAD equals the published SHA, and the checkout is clean.
- Both Claude manifests and both root skills exist in that pinned clone. `claude plugin validate --strict <checkout>` passed.
- Published `managing-superpowers-backlog` skill SHA256: `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81`.
- Published `managing-superpowers-handoffs` skill SHA256: `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE`.
- Overall clean-install and discovery result: `UNKNOWN` until upstream and Backplane are installed and a fresh authenticated Claude session proves all three skills.

### Authenticated isolated installation and fresh discovery

- On resumption, `claude auth status --json` in the disposable `CLAUDE_CONFIG_DIR` reported `loggedIn: true`, `authMethod: claude.ai`. No credentials were copied. The authenticated profile still had no marketplaces and no plugins before installation.
- From the verified upstream checkout at `5bf4e78011075bcfc0dc295f0724994cd123ee71`, `claude plugin marketplace add <upstream checkout>` succeeded, followed by `claude plugin install superpowers@superpowers-dev --scope user`. Intermediate inventory showed one marketplace, `superpowers-dev`, and one enabled plugin, `superpowers@superpowers-dev` version `6.4.1`.
- The published Backplane clone remained clean and detached at `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a`, with the expected origin; `gh api` still returned that SHA. From an empty neutral project, the guide's `claude plugin marketplace add $backplaneCheckout` and `claude plugin install superpowers-backplane@superpowers-backplane --scope user` both succeeded.
- Final isolated inventory had exactly the `superpowers-dev` and `superpowers-backplane` marketplaces and exactly the enabled `superpowers@superpowers-dev` version `6.4.1` and `superpowers-backplane@superpowers-backplane` version `0.1.0` plugins. No unrelated marketplace entry existed before installation, so none was displaced.
- Installed Backplane skill SHA-256 hashes match the published checkout: backlog `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81`, handoffs `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE`. Installed upstream `using-superpowers` matches its independent checkout at `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA`.
- The exact setup request ran in a fresh isolated session with read-only plan permissions and target issue #17 as context. Its 12-turn run gathered evidence and invoked both Backplane skills, then stopped at the turn limit without a final answer. A tools-disabled continuation in the same session produced the unedited setup report in the linked transcript. The report identifies the two packages, both sources and revisions, authenticated `gh`, all 15 native issue fields, label and closure capabilities, and three skill identities. No issue mutation was requested or observed.
- A fresh noninteractive `/help` request returned `/help isn't available in this environment.` The terminal UI opened first-run theme and login-method onboarding, so it was closed without another sign-in. The host command listing is `UNKNOWN`. Three separate fresh noninteractive sessions instead invoked the actual `Skill` tool for `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`, all with `PASS`. The session JSONL files show the three exact Skill tool calls, and the loaded base directories identify the independent upstream and pinned Backplane sources. See [the unedited responses and prompts](transcripts/2026-09-20-claude-code-discovery.md).
- The neutral project directory remained empty. The normal Claude profile retained its two marketplaces and had no Backplane installation. Its `gz-skills` version changed from `0.2.0` in the 14:05 UTC preflight snapshot to `0.3.2` with a recorded 14:18 UTC update, before the isolated live install began. The cause is unproven; no normal-profile rollback was attempted.
- Scored #17 clean-install and fresh skill-discovery smoke: `PASS`. The `/help` listing is `UNKNOWN`; direct host Skill invocation plus installed-cache hashes provide the three required discovery observations. This does not score #18 setup modes or #19 lifecycle and conformance.

## Task 4 — integrated source verification

- Implementation PR [#28](https://github.com/tvproductions/superpowers-backplane/pull/28) merged at `c03c4e4b52272fddd336c040d339b1285d552d0c` on 2026-09-20T15:42:03Z. `git ls-remote origin refs/heads/main` returned that SHA; local `main` was fast-forwarded to it and matched `origin/main`.
- Reviewed feature commit `39e3b071849a3867e6bac1769c3ab170fee91d5a` is an ancestor of integrated `main`. `git diff --exit-code d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a main -- .claude-plugin README.md docs/installing-claude-code.md skills/managing-superpowers-backlog/SKILL.md skills/managing-superpowers-handoffs/SKILL.md` exited 0. The integrated package, guide, README link, and canonical skill bytes are the tested pinned bytes; no reinstall seam changed.
- `claude plugin validate --strict .` passed on integrated `main` with the disposable `CLAUDE_CONFIG_DIR`. The guide checker again passed 14 requirements and three parsed PowerShell blocks. Local `main` and `origin/main` were aligned, with a clean worktree before this separate evidence branch.
- One fresh session in the same authorized disposable profile from the empty neutral project invoked the actual `Skill` tool for `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. Session `5e4b06f7-06c1-48db-a9dd-c04691f27ba2` returned `is_error: false` and `subtype: success`; its JSONL has exactly those three Skill calls, matching `Launching skill` results, and injected base directories under separate upstream and pinned Backplane sources. The exact prompt, unedited response, and compact host excerpts are in [the discovery transcript](transcripts/2026-09-20-claude-code-discovery.md).
- Integrated #17 result: `PASS` for the package, guide, and fresh discovery scope. The interactive `/help` listing remains `UNKNOWN` as recorded above; direct host invocations supply the three identity checks. #18 setup modes, #19 lifecycle and conformance, and #11 final host acceptance remain separate.
