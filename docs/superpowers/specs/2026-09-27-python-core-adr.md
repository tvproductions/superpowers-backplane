# ADR: Python implementation for the Backplane 1.0 core

- **Status:** Operator-required implementation correction on 2026-09-27; runtime distribution policy remains open for proof.
- **Date:** 2026-09-27
- **Related decisions:** [Heavy SDD Backplane ADR](2026-09-27-heavy-sdd-backplane-adr.md), [bundled view helper ADR](2026-09-27-heavy-view-generator-decision.md), and [project architecture](../../project/architecture.md).
- **Supersedes:** The bootstrap and v0.1 language-neutrality instructions only as they prohibit choosing Python for SP-BP's own implementation. The adopting project's freedom to use any language, build tool, or test framework remains intact. The existing prohibition on pytest remains intact.

## Context

The exact committed ecosystem candidate at gz-skills `7bd8f8d3cb6755e06dc284647619acc9f8802984` did not specify SP-BP's implementation language. Subsequent gz-skills working-copy design text, observed on 2026-09-27 but not yet committed, states that SP-BP's catalog, reconciliation, views, release logic, and tests are a Python project and excludes a Go core. The operator directly challenged the unapproved Go choice and identified this as a Python project. The exploratory Go files were removed before any commit or release.

SP-BP's earlier `AGENTS.md`, README, bootstrap design, and v0.1 adoption specification say the product is language-neutral and must not assume Python or another adopting-project runtime. Those statements were appropriate for a skills-only v0.1 package. The 1.0 design now requires deterministic parsing, graph validation, freshness checking, and projections, which need a testable implementation. The approved helper decision allows a bundled read-only helper but did not authorize Go or decide how adopters obtain its runtime.

## Decision

Implement SP-BP's 1.0 catalog, issue reconciliation, traceability, V&V, generated views, release logic, CLI/helpers, and tests in **one Python core**, using the standard library unless a bounded dependency is separately justified. Use Astral `uv`/`uvx` for Python project and package tooling, Ruff for lint/format, ty for type checks, the `uv_build` backend, and standard-library `unittest` through `uv run`; never introduce pytest. The development floor is Python 3.13 in `.python-version` and `pyproject.toml`, with versions resolved in `uv.lock`. Keep `gh` and Git as the GitHub and source-history interfaces. Keep pure identity, trace, V&V, projection, and release decisions independent of the `gh` collection adapter so source-race and offline cases can be tested without live GitHub calls. Host-specific adapters stay thin and may use the minimal language required by a host; they must not reproduce a parallel catalog, trace, view, or gate core. Do not maintain a Go core or service.

This decision chooses SP-BP's **implementation language**, not an adopting project's application language. It does not by itself make Python an undisclosed consuming-project requirement. The exact supported Python version, installation route, bundled versus interpreter-backed invocation, packaging size, and cross-host compatibility must be decided and proved in the implementation plan before heavy views are declared ready. Until then, an installed host without a proved invocation path reports view capability `UNKNOWN`.

## Considered paths

| Path | Result |
| --- | --- |
| Keep skills-only and compose `gh`/Git output through agent instructions | Does not yet prove deterministic graph validation, source-race handling, and byte-reproducible views. |
| Go core with platform binaries | Explored briefly, but absent from the committed candidate and inconsistent with the operator's Python direction; removed before commit. |
| Python core with a tested distribution path | Matches the operator's direction and the ecosystem's existing Python expertise while leaving consuming-project runtime policy for explicit proof. Selected. |

## Consequences and proof

Add a Python project layout, typed data shapes, fixtures, and `unittest` cases for family moves, splits, many-to-many requirement links, changed PRD revisions, stale evidence, pagination and source races, offline behavior, view reproduction, and release slips. Test the exact installed invocation on Codex, Claude Code, and both OpenCode variants that this repository declares. Do not claim the helper is shipped or require Python in an adopter merely because source tests pass locally. `AGENTS.md`, README, the active ADR, and implementation plan must state the Python ownership now; installation guidance and exact runtime claims follow only after packaging proof.
