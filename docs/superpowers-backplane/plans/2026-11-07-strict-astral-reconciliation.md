# Strict Astral Reconciliation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make strict Astral/Python compliance binding and establish a reproducible,
verified Backplane development baseline without claiming unobserved acceptance.

**Architecture:** A non-distributable uv development project owns pinned Python
tools, effective configuration and a locked environment. Existing skills and the
minimal native JavaScript adapter remain the product; no Python runtime package
or product CLI is invented. Policy, pre-commit, CI and acceptance evidence agree.

**Tech Stack:** Managed Python 3.14.10, uv 0.13.7, Ruff 0.17.4, ty 0.0.99,
pre-commit 4.7.0, unittest, existing Node adapter regression suite.

**Spec:** User's explicit strict-compliance execution direction; the bounded
engineering requirements and applicability are in `docs/engineering/python.md`.
The broader release-doctrine proposal is context only, outside this execution.

## Global Constraints

- User directed execution, not another policy-only acknowledgment. Execute this
  bounded prerequisite inline; full release-doctrine implementation remains out.
- Preserve root drafts, upstream installations, other repositories and profiles.
- Use `.sp-bp/work/strict-astral-20261107/` for execution records, never `.superpowers/`.
- No pytest, optional compliance, silent exemptions, push, issue mutation or release.
- Existing commands govern until their replacements are installed and verified.
- Full conformance cannot be claimed with required FAIL/UNKNOWN rows, including
  hosted CI. Record actual local results and supported platforms separately.

## Review Focus

- A tooling-only project must not become a fake Python product distribution.
- Locked execution must fail stale declarations and resolve tools locally.
- Existing Markdown Python examples and canonical skill references must remain valid.
- Hook installation in a linked worktree must not modify shared normal hooks.
- Historical records keep their original commands/runtime identities.

### Task 1: Burn in the mandatory engineering contract

**Files:** Modify `AGENTS.md`, `README.md`, `HANDOFF.md`; create `docs/engineering/python.md`.
**Interfaces:** Consumes approved strictness; produces scope, canonical commands,
applicability/exception rules and acceptance gates for Tasks2–3.

- [ ] Replace current no-project/ad-hoc installation guidance with locked project
  commands; preserve historical evidence. Declare strict conformance a MUST and
  full applicable acceptance prerequisite to new Python feature work.
- [ ] State non-package scope, mandatory future src/uv_build/installed-artifact
  requirements, Python-only owner boundary and separate native-host acceptance.
- [ ] Review links and instruction consistency. No prose-mirroring tests.

### Task 2: Establish the locked quality gate

**Files:** Create `pyproject.toml`, owning-tool `uv.lock`, `.pre-commit-config.yaml`,
`.github/workflows/check.yml`, `tests/test_repository.py`; modify `.gitignore`.
**Interfaces:** Consumes Task1 policy; produces exact dev environment, four
routine checks, native adapter regression and repeatable cross-platform CI.

- [ ] Use uv project metadata with `package=false`, Python >=3.14,<3.15, managed
  interpreter, minimum uv compatibility and exact dev tool selections.
- [ ] Write unittest asset checks for broken canonical references, inconsistent
  native metadata/skill inventory and invalid Python guide examples. Demonstrate
  negative controls in owned fixtures; do not mutate shipped source/upstream.
- [ ] Generate lock via uv, exact-sync the intended `.venv`, run Ruff/format/ty,
  unittest and all nine Node adapter tests. No shell-dependent orchestration.
- [ ] Configure precisely four local system pre-commit hooks and reviewed pinned
  checkout/setup-uv actions. CI runs the same gate on Linux/macOS/Windows.
- [ ] Exercise hooks using an isolated hook directory, not shared `.git/hooks`;
  compare actual tool/interpreter origins and effective settings.

### Task 3: Prove acceptance and retain remaining gaps

**Files:** Create `tests/scenarios/2026-11-07-strict-astral-acceptance.md` and JSON.
**Interfaces:** Consumes Tasks1–2; produces A01–A18 scoped acceptance and receipts.

- [ ] Inspect uv/Ruff/ty effective configuration, pins, dependency intent and
  source freshness; run clean locked sync, provenance, full gate and stale-lock
  refusal control. Preserve logs and hashes supporting current claims.
- [ ] Record A01–A18 PASS/FAIL/UNKNOWN/N/A with reasons. Python package build,
  installed API, workspace and special-source rows require reasoned applicability,
  not blanket passes. Hosted CI remains UNKNOWN until actually observed.
- [ ] Obtain one fresh whole-change review and correct material findings. Run
  owning checks again as needed, then make the reviewed local result available
  in the main workspace without overwriting unrelated drafts. No publication.
- [ ] Report exact workspace/source scope, checks, compliance status and first
  remaining prerequisite. Keep strict acceptance distinct from policy adoption.

### Full-compliance continuation authorized by the user

The user subsequently requested full compliance, expressly including the missing
hosted CI, deeper analysis and active-guide quality. Preserve the initial
incomplete checkpoint; complete its rows with the supplemental full-verification
record. Pin/run applicable analyzers, review findings without suppressions,
repair active guide quality and verify semantic preservation. Use the canonical
policy's independent-evidence cognitive route for this small source corpus and
obtain fresh independent review. Publish the reviewed compliance candidate to a
dedicated verification branch for exact-commit CI; this supersedes the earlier
no-push boundary only for that bounded verification. No release or unrelated
proposal publication is included.

### Verified execution disposition — November 7, 2026

Tasks 1–3 and the authorized full-compliance continuation are complete for the
assessed non-package Python development scope. The initial incomplete receipt
is preserved. The [current acceptance record](../../../tests/scenarios/2026-11-07-strict-astral-full-verification.md)
records all applicable rows PASS, reasoned N/A rows and no exception.
Source candidate 57ac0cd passed the installed Git hook and hosted run 42402031031
on Linux, macOS and Windows. The subsequent evidence-only commit records those
observations and is verified separately. Remote main integration, product
release, broader release-doctrine implementation and native-host acceptance
remain outside this execution. The native worktree and owned fixture evidence
are retained; tracked receipts preserve the sources and results needed to resume.
