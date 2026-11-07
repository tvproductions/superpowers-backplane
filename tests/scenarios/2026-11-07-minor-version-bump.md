# Minor development version decision — November 7, 2026

The maintainer explicitly selected a minor increment for the strict Astral
compliance work alone. Advance declared development version 0.1.0 to 0.2.0.
The coherent bundle is mandatory Python engineering policy, a reproducible
locked toolchain, enforced local/hosted quality gates, corrected guide quality
and retained full acceptance evidence. It introduces baseline obligations and
verification capabilities, beyond a compatible repair-only patch.

## Scope and policy

Native package/plugin/marketplace metadata and the non-package Python tooling
project agree at 0.2.0. uv regenerated its lock; parsed comparison proves that
only the virtual project's version changed. All 71 dependency resolutions,
selected Python/tools, implementation and guide-helper bodies remain unchanged.
The [changelog](../../CHANGELOG.md) marks this version unreleased. Earlier
untagged development is not retroactively a 0.1.0 release.

Canonical starter review: `a483e382146c6082e590e31494c07d1812645014`, rechecked
unchanged on November 7. Reviewed `docs/versioning.md`, `CHANGELOG.md` and
`docs/engineering/python.md`. Minor bundling, independent component versions,
unreleased notes and uv-owned lock regeneration apply; no major PRD is needed.
Current main contains unreleased Python-policy/minimum-uv guidance already
reconciled in the preceding Backplane engineering work; no tool selection changes.
The canonical first-public-release rule remains 0.1.0. Before first publication,
the maintainer must reconcile that rule and the earlier 0.1.0 scope proposal
with this explicitly approved 0.2.0 development selection. Owner: maintainer;
revisit: before the first release tag. This change authorizes neither a first
publication exception nor a tag/release. No issue, pilot or host acceptance is
closed or rescaled by this version decision.

## Verification and evidence continuity

On managed Python 3.14.10: `uv lock`, `uv sync --locked --all-groups` and
`uv lock --check` pass. All five version declarations agree. The four routine
pre-commit checks (Ruff lint, Ruff format, ty, five unittest checks), all nine
Node adapter tests and `git diff --check` pass. No new behavior test is needed
for this metadata-only increment.

[Strict acceptance](2026-11-07-strict-astral-full-verification.md) remains the
historical evidence for implementation/dependency measurements at source 57ac0cd
and its evidence-only successor cf427e1. The changed metadata hashes below
reconcile the bump; dependency-lock equality and unchanged implementation make
that deeper evidence reusable. Native host acceptance and release publication
remain separate. Exact-commit CI for this version increment is observed after
its commit; it is not implied by earlier passing runs.

| Current path | SHA-256 |
| --- | --- |
| `package.json` | `f0ef253f53ce84f8cf459bd22c9127aca824bcd8318534f95bb5a9c636ba71a3` |
| `plugin.json` | `4b589e0e69e6fcebefc3e4b2d1019d1af8e2d7ac4cebc90d00050f326ea81e6b` |
| `.claude-plugin/plugin.json` | `26498ccf94e063ae8b2ef02cc86e67156ba9c3e43bf365e4c21708adb9e20627` |
| `.claude-plugin/marketplace.json` | `745fde8e4945c0b6247be9fbb0bf1003cf3cac316e7ce5b791c31f5bb8b2d7b7` |
| `pyproject.toml` | `f23be63da2eab32270a0e6c9fca29bd2e9b08e37624e3e152d360ede9a83bb86` |
| `uv.lock` | `27955e82c7f88fff3bfca3959352f8ab52aba9b395d8d2ea197aded8e43d915d` |
