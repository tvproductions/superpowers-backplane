# Mandatory Backplane Python/Astral engineering

Strict Astral/Python compliance is a **MUST** for Backplane-owned development
tooling and Python implementation. The maintainer explicitly adopted this
requirement on November 7, 2026. It is not optional guidance, a mode-dependent
preference or permission to defer reconciliation until another feature needs it.

Backplane remains nonconformant until every applicable acceptance requirement
has passing evidence or an explicitly accepted, evidenced exception. Required
FAIL/UNKNOWN results prohibit a strict-compliance claim and new Python feature
work. Configuration alone never establishes compliance. Keep corrective tooling
work possible so an incomplete baseline can be reconciled.

## Authority and applicability

This is a Backplane-owned decision aligned with the canonical starter's
[Astral alignment](https://github.com/tvproductions/gz-skills-first-starter/blob/4f8bb09633655473cd6aab9e1ddc60963c487bb1/docs/engineering/astral-alignment.md),
[acceptance contract](https://github.com/tvproductions/gz-skills-first-starter/blob/4f8bb09633655473cd6aab9e1ddc60963c487bb1/docs/engineering/astral-acceptance.md)
and applicable Python engineering policy. Review exact source revisions during
scoped maintenance and release preparation. Follow current adopted uv minimum
compatibility guidance, rather than older conflicting exact-executable wording.
Adoption does not install the starter bundle or certify starter conformance.

This repository presently ships skills and a minimal native JavaScript adapter,
not a Python runtime package. `superpowers-backplane-dev` is a non-distributable
uv tooling project (`package=false`). Python package layout, build backend,
installed imports and artifact requirements are N/A only while no such product
exists. Do not invent an empty package or CLI to earn a pass. Reassess on any
Python runtime/package introduction: use `src/`, declared metadata/entry points,
uv_build for pure Python, source-independent build and isolated installed-artifact
proof. Host-required adapter code stays minimal; new Backplane core logic is
Python. None of this imposes a runtime or test framework on consuming projects.

## Required project contract

- Use uv for managed Python, environments, dependencies, lock generation and
  execution. `pyproject.toml` is the metadata/configuration authority and
  `uv.lock` is committed, owning-tool-generated resolution. Do not edit locks.
- Keep uv-managed Python 3.14; `.python-version` records the verified exact patch.
  Align metadata, actual interpreter, Ruff, ty and CI. Preserve historic evidence
  at its original runtime. Family migrations require explicit review.
- Select a verified minimum compatible uv without an upper bound, separately
  from its exact tested/dev/CI selection. Freshness requires live official-source
  review and compatibility evidence; a minimum or installed version is not proof.
- Use exact selected dev tools, Ruff lint/format, ty and unittest. **No pytest.**
  Review lint families; do not suppress findings or relax checks to pass.
  Routine Ruff scope is executable Python/notebooks and pyproject, not rewriting
  approved historical Markdown transcripts. Unittest compiles current guide
  examples and checks their combined per-guide Python with Ruff lint/format,
  without executing native operations. Preserve historical findings and record
  their corrective evidence; compilation alone never proves guide quality.
- Exact-sync only the intended project `.venv`. Routine checks use `--locked`;
  never use `--no-project`, `--frozen`, ad hoc `--with` overlays, manual pip
  installs or external PATH fallbacks as substitutes for baseline proof.
- Inspect effective root/ancestor/user/system settings and relevant overrides
  without dumping credentials or whole environments. Record actual interpreter
  and executable origins. Configuration discovery must cover each source scope.
- Local commands, four routine pre-commit hooks and CI must implement the same
  reviewed contract. Hook configuration, installed hooks, local execution and
  exact-commit hosted CI are separate observations. Missing CI remains UNKNOWN.
- Use explicit encodings, Python paths and shell-free subprocess argument lists
  for substantive tooling. Use Git/gh directly for routine repository operations.
- Assess Python-version idioms, deprecations and applicable deeper engineering
  checks at scoped change/adoption/release acceptance. Keep those checks outside
  routine hooks/CI. No application/source scope needs a reasoned N/A; absence of
  a configured analyzer is never an automatic pass.

## Canonical commands

From the verified repository or registered worktree root:

```text
uv sync --locked --all-groups
uv lock --check
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked ty check
uv run --locked python -m unittest discover -s tests -p test_*.py -v
uv run --locked pre-commit run --all-files
node --test tests/opencode-adapter.test.mjs
git diff --check
```

Create a missing environment with `uv venv --managed-python .venv`, then exact
sync. Review an existing environment's ownership before a sync that removes
extra distributions. For approved dependency changes use uv's owning commands,
regenerate the lock and run the full applicable gate. Preserve unrelated pins.

If the caller lacks the tested uv, use an authorized supported selection such
as `uv tool run --from uv==0.13.7 uv ...`; do not change a machine-wide install
as an incidental baseline repair. Nested tools must still resolve to the
intended selection. Record actual provenance and changed behavior verification.

Install hooks only after inspecting the intended Git hook path and existing
contents. Native linked worktrees may share hooks with the primary checkout;
do not overwrite unknown hooks or silently change another task's setup.

```text
uv run --locked pre-commit install
```

When a Python distribution becomes applicable, additionally require
`uv build --no-sources`, wheel/sdist metadata/resource checks and clean installed
behavior outside source. A locked dev run does not supply that proof.

## Acceptance and exceptions

Maintain an A01–A18 evidence matrix under `tests/scenarios/`: actual command,
scope/identity, result, supporting evidence and open gap for each applicable row.
Record reasoned N/A separately from PASS. Inspect actual packaged product and
development source before deciding applicability. Broader deeper-analysis gaps,
host integration and release readiness remain explicit.

An exception needs a demonstrated constraint, affected requirement/scope,
evidence, authorized approval, owner and dated revisit. Convenience, existing
layout, available tools or a passing local script are not exceptions. Accepted
exceptions yield conditional acceptance, never a strict passing claim. Keep
profile selection, Python baseline, native discovery, publication and remote
arrival distinct. Reconcile final candidate changes before reusing evidence.
