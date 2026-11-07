# Changelog

## 0.2.0 — November 7, 2026

The maintainer selected this coherent minor bundle on November 7, 2026:
strict Astral/Python development compliance and its verified enforcement.

- Make strict Astral compliance mandatory for Backplane-owned Python development
  in every mode; preserve consuming projects' independent runtime policies.
- Establish uv-managed Python 3.14.10, locked development and analysis tools,
  Ruff lint/format, ty and unittest; replace conflicting no-project guidance.
- Enforce four local pre-commit checks and the routine quality gate in hosted
  Linux, macOS and Windows CI.
- Repair active Python guide quality and add routine syntax/lint/format guards.
  Retain independently reviewed deeper checks, cognitive measurements, dependency
  audit and guide-helper behavior coverage/mutation evidence.

This adds engineering baseline obligations and enforcement capabilities, which
warrant the maintainer-approved minor increment rather than a repair-only patch.
See the [strict acceptance record](tests/scenarios/2026-11-07-strict-astral-full-verification.md)
and [version-bump record](tests/scenarios/2026-11-07-minor-version-bump.md).

Contributor impact: synchronize the declared environment with
`uv sync --locked --all-groups` and use the repository's locked commands. Native
product behavior and consumer runtime requirements are unchanged by this bundle.
This engineering-baseline release leaves the complete adoption milestone and
its operations, external-pilot and OpenCode obligations open. Historical native
acceptance retains its original scope. The maintainer explicitly selected 0.2.0
as the first publication; no historical 0.1.0 release is asserted. See the
[release authority and scope](docs/superpowers-backplane/releases/2026-11-07-v0.2.0.md).
