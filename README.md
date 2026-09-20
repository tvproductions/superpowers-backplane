# superpowers-backplane

`superpowers-backplane` supplies backlog-level product continuity for projects
that use upstream Superpowers. It follows native GitHub Issues for identity,
hierarchy, dependencies, lifecycle, and delivery evidence, then binds those
work items to Superpowers specifications and plans.

The project is language-neutral. Its required command-line dependency is
GitHub CLI (`gh`); Git is assumed by the Superpowers workflow. GitHub Projects
are optional visualization only and never authoritative. IssueOps is not used.

This repository is in bootstrap state. Start with `HANDOFF.md`.

For Codex, follow the [installation and setup guide](docs/installing-codex.md).
For Claude Code, follow the [installation and setup guide](docs/installing-claude-code.md).

The local installation obtains the stable upstream Superpowers release under
the ignored `.agents/superpowers` checkout and records its resolved revision in
`SUPERPOWERS.md`.
