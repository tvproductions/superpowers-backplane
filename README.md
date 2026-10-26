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

This repository is in bootstrap state. Start with `HANDOFF.md`.

For Codex, follow the [installation and setup guide](docs/installing-codex.md).
For Claude Code, follow the [installation and setup guide](docs/installing-claude-code.md).

Upstream Superpowers supplies the development workflow; this Backplane adds
native GitHub backlog and product continuity around that workflow. gz-skills
is a separate, optional companion, installed and configured independently.
The three projects are meant to work together. This repository does not
install, vendor, or configure gz-skills. It obtains the stable upstream release
independently under the ignored `.agents/superpowers` checkout and records that resolved
revision in `SUPERPOWERS.md`.

For repository-scoped OpenCode V2 use, `opencode.jsonc` pins the native
Superpowers plugin to `v7.0.1` and exposes this repository's own `./skills`.
Restart OpenCode in this repository after changing that configuration.
