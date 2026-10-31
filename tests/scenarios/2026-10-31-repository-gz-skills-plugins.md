# Repository-scoped gz-skills plugin installation

The operator requested the gz-skills plugin for Codex, Claude Code and OpenCode,
explicitly restricted to this repository. The selected published release is
`v0.8.3`, commit `d6acc26e28ca1c4f43e5bb46d8973021d7d006c3`.
The [verification receipt](2026-10-31-repository-gz-skills-plugins.json) records
the observed native state and scope checks at base commit `c0a0a48`.

## Configuration and ownership

- Codex: the repository marketplace adds a Git source pinned to `v0.8.3`;
  `.codex/config.toml` enables `gz-skills@superpowers-backplane`. This replaces
  an existing reference to the unavailable `gzfactory-development` catalog.
- Claude Code: native marketplace declaration and installation used
  `--scope project`. `.claude/settings.json` enables `gz-skills@gz-skills`
  and declares the upstream marketplace at `v0.8.3`.
- OpenCode V2: `opencode.jsonc` adds the Git package at `#v0.8.3`, preserving
  the existing Superpowers pin and Backplane skill discovery.

Superpowers retains feature-workflow authority; Backplane retains backlog,
lifecycle and handoff authority. gz-skills supplies supporting procedures.
This installs neither the starter bundle nor a consuming-project requirement.
No profile setup or `.gz-skills/settings.json` was needed.

Native managers use shared host caches. Enablement remains repository-scoped;
no user/account configuration was changed. Codex CLI 0.166.0's native install
implementation writes enablement into its user config, so its cache installation
used an isolated `CODEX_HOME` under ignored `.sp-bp/work/gz-skills-plugin-install/`.
That installer's `plugins` directory linked to the normal host's plugin cache,
and command-scoped marketplace configuration pointed to this repository. The
native installer wrote its enablement only into the isolated config. The normal
profile reads the tracked repository enablement and the installed cache. Scratch
is not required for subsequent discovery. No installed skill source was edited.

## Verification

- Fresh Codex app-server `plugin/list` with this repository in `cwds` reports
  exactly one gz-skills plugin, installed and enabled at 0.8.3. Fresh
  `skills/list` reports 20 enabled `gz-skills:gzs-*` skills without load errors.
- Claude native `plugin list --json` reports 0.8.3 at project scope for this
  exact repository. `plugin details` inventories all 20 skills. Other project
  installation identities and revisions are unchanged; current-project enabled
  flags are contextual and are not treated as other projects' settings.
- After configuration reload and background installation, OpenCode's native
  `/api/plugin` with the explicit repository directory header reports gz-skills
  active at the release commit, alongside unchanged Superpowers 7.0.1.
  `/api/skill` exposes all 20 gz-skills workflows.
- All 44 files under the released canonical `skills/` tree match the GitHub
  release-tree blob identities in each of the three installed caches.
- Codex plugin and skill discovery outside the repository contains no gz-skills.
  OpenCode plugin discovery outside it also contains no gz-skills. Claude's
  outside-repository listing has no gz-skills project enablement.
- User-level Codex, Claude and OpenCode configuration hashes (including absent
  files) match the pre-install snapshot. Codex's outside-repository plugin list
  is unchanged. `git diff --check` passes.

This verifies installation, source identity and discovery. It does not establish
a fresh behavioral suite, full ecosystem integration, or release readiness.
The current conversation needs a new session to refresh its initial skill list.
Changes remain local and uncommitted; no push, tag or release occurred.

## Sources

- [Released installation contract](https://github.com/tvproductions/gz-skills/blob/v0.8.3/README.md)
- [Released OpenCode adapter instructions](https://github.com/tvproductions/gz-skills/blob/v0.8.3/.opencode/INSTALL.md)
- [Official Codex marketplace metadata](https://developers.openai.com/plugins/build/plugins#marketplace-metadata)
- [Codex 0.166.0 native installation behavior](https://github.com/openai/codex/blob/rust-v0.166.0/codex-rs/core-plugins/src/manager.rs)
- Native `claude plugin install --help` and `marketplace add --help` for project scope.
