# Strict Astral full-verification candidate

Date: November 7, 2026. **Strict acceptance PASS for the assessed Backplane
Python development-tooling scope. All applicable A01–A18 rows pass; remaining
rows have evidenced N/A dispositions. No exception was used.** This supersedes
the preserved [initial incomplete checkpoint](2026-11-07-strict-astral-acceptance.md).
New Python feature work may proceed under the mandatory ongoing contract.

## Scope and authority

The user explicitly requested full compliance, including the previously missing
hosted CI, deeper checks and guide quality. Execution reuses the registered native
worktree 206f at baseline `0aa0cc007db63449455a1c4f9b6d92cb60c5d29a`.
The user-facing product remains two skills plus the minimal native adapter;
Python is a locked non-package development project. No release, issue mutation,
upstream installation change or migration of other projects is included.

Source scope is `tests/test_repository.py` plus the nine current Python guide
blocks, concatenated in their documented shared-session order. The extracted
module is derived verification input under ignored `.sp-bp/work/`; its hash
and derivation are in the [receipt](2026-11-07-strict-astral-full-verification.json).
Historical transcripts and approved plan bytes remain unchanged.

## Local results

| Check | Observed result / interpretation |
| --- | --- |
| Locked routine gate | Ruff lint/format, ty, five unittest checks and nine native-adapter regressions pass; guide syntax and Ruff checks are now routine guards |
| Guide repair | Sorted the same standard-library imports, formatted nine blocks, and added meaningful module/helper docstrings. AST comparison preserves control flow/native commands except documentation/import ordering. The session-launch guidance now follows project-owned execution policy |
| Ruff C901 | Pass under its default10 ceiling, stricter than policy20 |
| Lizard1.25.1 | Seven functions; max10, highest module mean8, overall weighted mean4.5714, all below20. Literal boundary controls measure20 and21 and distinguish acceptance |
| Cognitive ceiling15 | Independent manual ledger covers the complete seven-function corpus, max6; independent review PASS. This is independent evidence permitted by canonical policy, not a qualified-engine claim |
| Cohesion1.2.0 | Test class0% shared attributes retained and reviewed. Independent unittest cases own no domain state; no universal threshold exists and no artificial state was introduced |
| Interrogate1.7.0 | 100% documentation coverage; usefulness reviewed separately. Initial66.7% result is corrected by documenting the two helpers and session module |
| Vulture2.16 | No findings in actual source scope; framework-discovered test methods preserved |
| Bandit1.9.4 | Only low-severity B404/B603 findings. Reviewed resolved-executable argument lists, shell=False, fixed guide/test operation sources and explicit return checks. No suppression, ignored finding or lowered threshold |
| pip-audit2.10.1 | 71 exact resolved dependencies audited; zero skipped and zero known vulnerabilities at the checked time. uv exported the hashed input; no pip resolver/fix changed the environment |
| Coverage.py7.17.2 | Eleven actual guide-helper behavior tests; 42/42 statements and 14/14 branches covered, no excluded lines |
| Cosmic Ray8.7.0 | Passing original baseline; 135 mutants: 128 killed, seven reviewed equivalent/JSON-whitespace survivors; no timeout, tool error or unreviewed survivor |
| Python3.14 review | Managed3.14.10, explicit encodings/paths, shell-free subprocess arguments. No demonstrated benefit from adding concurrency, templates or annotation-introspection APIs to this small harness |

The latest stable PyPI selections for the eight deeper tools were checked before
uv added exact pins in the separate `hygiene` group. Deeper checks remain on-demand,
outside the four routine hooks and CI. No private cognitive scorer, extracted
engine package or inherited starter exception was introduced.

The canonical Python policy explicitly permits “qualified replacement or
independent evidence” for cognitive acceptance. The independent ledger names
each function, exact source hash, score and increment derivation. The shared
engine's broader qualification remains a separate unimplemented capability; this
candidate does not claim it is installed or qualified.

## Applicability and remaining observations

A01 and A04–A08/A10/A17 require the retained current identities, effective config,
managed interpreter/tool origins, fresh lock and exact sync. A18 requires the
actual results and reviewed findings above, plus completed independent cognitive review.
A09 now passes: the installed local Git hook ran all four checks during the
candidate commit, and exact-commit hosted CI completed successfully on Linux,
macOS and Windows.

A02/A03/A11/A12/A13 are N/A to Python runtime distribution because none exists;
this is not a fake build/install pass. A14 is N/A to workspaces; A15 to private
runtime sources; A16 to Python deployment/native-extension products. Coverage and mutation are applicable to the two operational guide helpers, even
though no Python runtime package is shipped. An owned fixture extracts the exact
function bodies and tests actual ownership, preservation, atomic-write and
child-process behavior, mocking only native process/network boundaries. Measurements
and mutant dispositions are retained in the structured receipt. deptry and
import-layer checks remain N/A because no runtime package/dependency boundary
exists; reassess when such implementation appears. Native installed-host/release acceptance is separate.

The new guide-quality guard was proven against valid syntax containing an
unused import: it refuses the lint defect and passes the restored fixture.
This complements the earlier missing-resource/version/syntax/stale-lock controls.
No native guide operation was executed as a lint or documentation check.

## Current A01–A18 acceptance

| Row | Result | Evidence / applicability |
| --- | --- | --- |
| A01 | PASS | Verified standalone root/native worktree and guarded reconciliation; tracked candidate and remote arrival identities separate. |
| A02 | N/A | No runtime Python package/CLI; non-distributable uv tooling project; reassess src layout when introduced. |
| A03 | N/A | No Python distribution/build backend; uv_build mandatory when applicable. |
| A04 | PASS | Central pyproject and retained effective Ruff/ty discovery and configuration inventory; guide cells checked separately. |
| A05 | PASS | Actual uv-managed Python 3.14.10 matches .python-version, metadata, Ruff/ty and passing three-platform CI. |
| A06 | PASS | Dated official selection review for routine tools and eight deeper tools with actual pinned versions and compatibility results. |
| A07 | PASS | uv-generated fresh lock, exact intended-environment sync, stale-lock refusal control and clean CI sync. |
| A08 | PASS | Actual intended interpreter/tool origins, Ruff lint/format, ty, five unittest checks and nine Node regressions pass. |
| A09 | PASS | Installed local hook executes all four checks at candidate commit; observed exact-commit Linux/macOS/Windows CI success. |
| A10 | PASS | No runtime dependencies; separate exact dev/hygiene groups and owning-tool lock preserve dependency intent. |
| A11 | N/A | No Python wheel/sdist release product; native-plugin release acceptance is distinct. |
| A12 | N/A | No installed Python runtime API; native-host acceptance is separate. |
| A13 | N/A | No typed Python library, namespace or published Python support range. |
| A14 | N/A | Standalone uv tooling project, no workspace. |
| A15 | N/A | Public resolution only; no private/special runtime sources or credential handling. |
| A16 | N/A | No Python deployment/native extension/container/embedded-host product. |
| A17 | PASS | Reviewed uv minimum compatibility and exact tested/project-local tool selection; no standalone application/PEP723 tool. |
| A18 | PASS | All applicable deeper checks performed and reviewed, current guide quality repaired and guarded, independent cognitive evidence accepted, real helper coverage/mutation measured; documented N/A remains bounded. |

## Hosted verification boundary

Publish only the reviewed compliance unit on a dedicated verification branch to
obtain hosted CI; keep earlier release-design/scope drafts local and preserve
unrelated work. A pushed candidate is not a product release. Record source,
tested commit, branch, CI jobs and later evidence-storage identity separately.
Only actual passing CI plus accepted independent evidence can close the remaining
rows and lift the Python-feature gate for the assessed candidate.

Observed tested candidate: `57ac0cde90b93e32d2b5fb9332c0a885fd149f56` on
`chore/strict-astral-compliance`. [Hosted run 42402031031](https://github.com/tvproductions/superpowers-backplane/actions/runs/42402031031)
completed successfully with all three jobs passing. The structured receipt
retains job identities, steps and timestamps. The following evidence-only commit
records that observation; its own CI is observed separately to avoid a
self-referential receipt. This does not merge the branch into remote main.
