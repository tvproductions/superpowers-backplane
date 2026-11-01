# superpowers-backplane

`superpowers-backplane` supplies backlog-level product continuity for projects
that use upstream Superpowers. It follows native GitHub Issues for identity,
hierarchy, dependencies, lifecycle, and delivery evidence, then binds those
work items to Superpowers specifications and plans.

The project is language-neutral. Its required command-line dependency is
GitHub CLI (`gh`); Git is assumed by the Superpowers workflow. Native GitHub Projects are the normal proposed governance interface, with
explicit Issues-only compatibility; native issues and Backplane labels remain
authoritative. IssueOps is not used.

Read the [governance doctrine](docs/superpowers-backplane/governance.md) for
product decomposition, coverage and satisfaction, PR closeout, and portable
repository checkpoints.

Backplane owns [lite/heavy mode definitions](docs/superpowers-backplane/modes.md):
requirements tracking, classification/lifecycle labels, backlog and release
monitoring, and handoffs belong here. The mode document separates intended
scope from verified capability. The starter refers to these workflows.

For this project's own releases, [the release-policy binding](docs/release-policy.md)
adopts gz-skills-first-starter as the authoritative shared policy source,
including SemVer, new major-release PRDs and source consistency checks.
This is policy alignment without circular template adoption.

This repository is in development. Manifest versions do not establish a published release. For development continuity, read `HANDOFF.md`.

Backplane is licensed under the [MIT license](LICENSE). Start with the
[adopter operations guide](docs/adopter-operations.md) for prerequisites,
verified support limits, recovery and authorization guidance.

For Codex, follow the [installation and setup guide](docs/installing-codex.md).
For Claude Code, follow the [installation and setup guide](docs/installing-claude-code.md).
For OpenCode V1/V2, see the [initial installation guide](docs/installing-opencode.md);
setup, lifecycle and final integrated acceptance remain pending.

Codex and Claude Code have native acceptance at the exact versions, platforms
and source revisions linked in the operations guide. OpenCode has initial
installation smoke evidence only; update, rollback and removal are not yet
verified. Other harnesses are outside the approved v0.1 scope. GitHub Projects
are optional; IssueOps is not required, and no consuming-project runtime is imposed.

Upstream Superpowers supplies the development workflow; this Backplane adds
native GitHub backlog and product continuity around that workflow. gz-skills
is a separate, optional companion, installed and configured independently.
The three projects are meant to work together. For development here, this
repository enables the released gz-skills `v0.8.3` plugin through repository
configuration for Codex, Claude Code and OpenCode V2. This is a development
tool choice, not a dependency imposed on Backplane adopters or adoption of the
starter bundle. Superpowers and Backplane retain their workflow authority;
gz-skills procedures support that workflow. Skill trees are not vendored.
This repository obtains the stable upstream Superpowers release
independently under the ignored `.agents/superpowers` checkout and records that resolved
revision in `SUPERPOWERS.md`.

For repository-scoped OpenCode V2 use, `opencode.jsonc` pins the native
Superpowers plugin to `v7.0.1`, gz-skills to `v0.8.3`, and exposes this
repository's own `./skills`. Codex uses `.agents/plugins/marketplace.json`
with `.codex/config.toml`; Claude Code uses `.claude/settings.json` at project
scope. Native plugin managers own their caches; these settings do not enable
gz-skills account-wide. Restart an existing session to refresh its skill list.
