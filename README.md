# superpowers-backplane

`superpowers-backplane` supplies backlog-level product continuity for projects
that use upstream Superpowers. It follows native GitHub Issues for identity,
hierarchy, dependencies, lifecycle, and delivery evidence, then binds those
work items to Superpowers specifications and plans.

Backplane's 1.0 catalog, issue reconciliation, traceability, V&V, generated
views, release logic, CLI/helpers, and tests are a Python project. Host-specific
adapters stay thin. Adopting projects may use any application language or test
runner. GitHub CLI (`gh`) and Git remain required interfaces; the installed
Python wheel entry point has passed a local `uvx --offline` read-only preflight;
installed generation and checking of heavy views still need proof. GitHub
Projects are optional visualization only and never authoritative. IssueOps is
not used. The repository targets `1.0.0`; it has not published that release.

Python development uses Astral tooling (`uv`, `uvx`, Ruff, and ty), a locked
Python 3.13 project environment, and standard-library `unittest`:

```text
uv sync --locked
uv run --locked python -m unittest discover -s tests/unit -v
uv run --locked ruff check src tests/unit
uv run --locked ruff format --check src tests/unit
uv run --locked ty check src tests/unit
```

These commands verify the current source; they do not prove the installed heavy
workflow or authorize a release.

The 1.0 migration is in progress. Start with `HANDOFF.md`.

For Codex, follow the [installation and setup guide](docs/installing-codex.md).
For Claude Code, follow the [installation and setup guide](docs/installing-claude-code.md).

The local installation obtains the stable upstream Superpowers release under
the ignored `.agents/superpowers` checkout and records its resolved revision in
`SUPERPOWERS.md`.
