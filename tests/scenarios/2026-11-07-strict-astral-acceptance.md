# Strict Astral reconciliation — November 7, 2026

Historical initial checkpoint. The subsequent [full-verification record](2026-11-07-strict-astral-full-verification.md) owns the current disposition; the original observations below are preserved.

**Policy adopted; local development baseline established; strict acceptance is
INCOMPLETE.** Hosted CI and outstanding wider engineering evidence remain
UNKNOWN. No exception was invented to call this conformant, and new Python
feature work remains gated. Corrective compliance work may continue.

## Authority and scope

The maintainer explicitly directed “do it, burn it in” and made strict Astral
compliance a MUST. This implements that bounded prerequisite, not the remaining
release-doctrine feature or the OpenCode acceptance plans. The operative rule
is now in [AGENTS](../../AGENTS.md) and
[the engineering contract](../../docs/engineering/python.md), with a README
entry and [implementation plan](../../docs/superpowers-backplane/plans/2026-11-07-strict-astral-reconciliation.md).

Execution began in verified native detached worktree
`/Users/jbabb/.codex/worktrees/206f/superpowers-backplane`, sharing the standalone
Git directory and baseline `0aa0cc007db63449455a1c4f9b6d92cb60c5d29a`.
Ignored execution state is scoped to `.sp-bp/work/strict-astral-20261107/`.
The standalone root's earlier release-review drafts remain separate. No upstream
installation, other repository, native profile, issue, tag or release changed.

The product remains skills plus a minimal JavaScript native adapter. Python is
a non-distributable tooling project, not a newly invented package or CLI.
Applicable packaging requirements must be reconsidered when runtime Python is
introduced. There is no Python build/install artifact to falsely certify now.

## Selected tooling and source review

Python remains managed 3.14.10, with metadata/Ruff/ty/CI all targeting 3.14.
Official source checks on November 7 selected uv 0.13.7, Ruff 0.17.4,
ty 0.0.99 and pre-commit 4.7.0. uv's compatible minimum is >=0.13.5 without an
upper bound, separately from tested/dev/CI selection. No machine-wide upgrade
was performed; scoped uv execution provisions the locked project environment.

- [Python 3.14.10](https://www.python.org/downloads/release/python-31410/)
- [uv 0.13.7](https://github.com/astral-sh/uv/releases/tag/0.13.7)
- [Ruff 0.17.4](https://github.com/astral-sh/ruff/releases/tag/0.17.4)
- [ty 0.0.99](https://github.com/astral-sh/ty/releases/tag/0.0.99)
- [pre-commit 4.7.0](https://github.com/pre-commit/pre-commit/releases/tag/v4.7.0)

Reviewed starter `4f8bb09633655473cd6aab9e1ddc60963c487bb1` retains the strict
Astral acceptance and newer minimum-uv guidance. The later source delta from
`e918dbb` records dependency scan evidence; it does not relax this contract.
No starter self-adoption, copied skill tree or consumer Python requirement is
introduced. Official uv configuration/locking guidance supports non-package
projects and exact sync; locked runs alone do not prove exact environment state.

## Local verification and negative controls

uv generated `uv.lock` and exact-synced the worktree `.venv`. Actual Python base
is uv-managed 3.14.10; uv/Ruff/ty/pre-commit executables resolve inside that
environment. No uv/Ruff/ty environment override was observed other than uv's
own recursion marker. Competing root/ancestor/user configuration probes were
absent in the observed scope. Ruff settings identify pyproject; ty indexes the
actual current Python source rather than an empty selected directory.

Ruff lint/format, ty, four unittest resource/syntax checks, all four pre-commit
checks, the existing nine Node adapter regressions, strict Claude manifest
validation, lock freshness and whitespace checks pass locally. Native validator
icon/README directory advice remains nonblocking and does not certify listing.

Owned negative controls demonstrate refusal of a missing canonical reference,
conflicting native product version, invalid Python guide syntax and a stale
lock. Each fails with the deliberately broken input and passes after restoring
only the owned fixture. Original skills, guide bytes and native manifests remain
unchanged. These controls test local gates, not new installed-host acceptance.

Ruff's current default formatter also discovers Markdown fences. Its first
whole-tree run exposed formatting findings in 14 existing Markdown files,
including immutable historical transcripts and approved plans. The explicit
routine scope is now executable Python/notebooks/pyproject, preserving those
recorded bytes. Unittest compiles active guide examples. This scope decision
does not erase the previously recorded active-guide lint/format findings from
the [October31 refresh](2026-10-31-tooling-refresh.md), nor claim guide execution
or guide-quality acceptance. Wider reconciliation remains A18 below.

## A01–A18 disposition

| Row | Result | Applicability and evidence |
| --- | --- | --- |
| A01 | PASS | Verified standalone/native-worktree identity, baseline, protected root drafts and bounded migration; no destructive rollback operation |
| A02 | N/A | No runtime Python package/CLI; uv development project explicitly non-package; future runtime introduction must use installed src layout |
| A03 | N/A | No Python distribution/build backend; uv_build becomes mandatory for applicable pure-Python packaging |
| A04 | PASS locally | Central pyproject, explicit lint/format language scope, actual Ruff settings/ty discovery and nonsecret configuration inventory |
| A05 | PASS locally | Managed 3.14.10, exact .python-version, >=3.14,<3.15 metadata and matching Ruff/ty/CI declarations |
| A06 | PASS for selected routine scope | Dated official release/notes review and actual selected tool versions; not broader unperformed analyzer freshness |
| A07 | PASS locally | uv-generated lock, exact intended-environment sync, fresh-lock pass and stale-lock refusal control |
| A08 | PASS locally | Intended local executable origins, strict selected Ruff families, formatting, ty, unittest and native adapter regression |
| A09 | UNKNOWN overall | Four hook commands pass and three-platform CI is configured; exact-commit hosted execution remains unobserved. Hook installation is recorded separately in the receipt |
| A10 | PASS locally | No product runtime dependency added; exact development group and generated resolution preserve product dependency intent |
| A11 | N/A | No Python wheel/sdist release product; native plugin distribution remains governed by its separate acceptance authorities |
| A12 | N/A | No installed Python runtime API to test; this is not a claim of clean installed native-host acceptance |
| A13 | N/A | No typed library, namespace or published Python dependency support range |
| A14 | N/A | Standalone tooling project; no uv workspace or cross-family member resolution |
| A15 | N/A | Standard public package resolution, no private/special runtime sources or copied credentials |
| A16 | N/A | No Python deployment, native extension, container or embedded-host product introduced |
| A17 | PASS for bootstrap tool scope | Exact scoped uv 0.13.7 tool selection, then project-local locked tools; no PEP723 export or separate application tool environment |
| A18 | UNKNOWN | Full wider Python-engineering applicability/analysis qualification and active-guide lint/format reconciliation are not established by this migration; no waiver or full compliance claim |

PASS labels above are bounded local observations. A09/A18 prevent strict
acceptance. Configured cross-platform CI is not Windows/Linux evidence.

## A18 named-check applicability

This is the explicit applicability assessment, not a completed deeper-analysis
gate. Missing tools/results below are UNKNOWN, not exemptions. The current
Python source is the repository asset-check unittest harness; runtime package
and operational Python implementation are absent.

| Requirement | Applicability / result | Next evidence |
| --- | --- | --- |
| Version-aware Python review | Applicable; current tests use stdlib paths, explicit UTF-8 and straightforward Python, without a demonstrated need for 3.14-specific concurrency/template/introspection APIs | Preserve bounded code review and assess actual new runtime code against versioned documentation |
| Ruff C901 | Applicable; PASS on tests under default ceiling10, stricter than policy20 | Retained scoped command/result; do not add to routine hooks |
| Qualified cognitive scoring | Applicable to owned Python logic; UNKNOWN, no selected/qualified shared engine supplied | Qualify the approved upstream engine before measuring; no private scorer or inherited starter exception |
| Lizard function/module/overall complexity | Applicable to owned test/helper logic; UNKNOWN | Select current compatible tool and reviewed counting scope, run and assess results |
| Class cohesion | Test harness class exists; UNKNOWN, no measurement claimed | Assess the unittest-specific responsibilities and metric applicability with actual tool proof; do not invent a threshold |
| Interrogate | Applicable Python docstring presence/usefulness; UNKNOWN | Actual pinned measurement plus human usefulness review |
| Vulture | Applicable owned Python dead-code review; UNKNOWN | Actual scan and review of framework discovery/entry points |
| Bandit | Applicable test/helper source review; UNKNOWN | Actual scan with reviewed dynamic-compilation context, without blanket suppression |
| Coverage.py | N/A to runtime behavior: no Python product implementation is shipped; tests themselves are the harness, not the coverage target | Reassess when a runtime/tool implementation is introduced; Node adapter has its own behavior tests |
| Cosmic Ray | N/A to this change's product: no Python implementation target distinct from the test harness | Select/prove a bounded mutation scope when Python implementation exists; no fake score from mutating tests |
| deptry | N/A to runtime dependency checking: no runtime package/dependencies; new test imports are stdlib | Reassess on package or non-stdlib runtime imports |
| pip-audit | Applicable exact resolved development environment; UNKNOWN | Audit reviewed exact resolution and retain limitations, findings and disposition |
| Import Linter | N/A: no Python application packages or domain/adapters import boundary | Define real contracts if packages are introduced; do not invent architecture to obtain a pass |

No analysis listed as UNKNOWN has been accepted by exception. Complete those
required checks/decisions before strict acceptance, alongside CI and guide
quality reconciliation. Installing an analyzer or quoting another project's
passing receipt does not close a row.

## Remaining prerequisite

Finish the wider engineering applicability/findings assessment, resolve required
active-guide findings without altering historical evidence, and obtain observed
exact-candidate CI under authorized transport. Native host readiness and release
acceptance remain separate. Keep the new-feature gate in force until all required
rows are accepted. The [structured receipt](2026-11-07-strict-astral-acceptance.json)
retains actual command outputs, source identities and later hook/root results.
