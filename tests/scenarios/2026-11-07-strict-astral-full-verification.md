# Strict Astral full-verification candidate

Date: November 7, 2026. **Local analysis passes; hosted CI
is pending.** This supplements the preserved
[initial incomplete checkpoint](2026-11-07-strict-astral-acceptance.md).
No full-compliance claim is made before the remaining observations complete.

## Scope and authority

The user explicitly requested full compliance, including the previously missing
hosted CI, deeper checks and guide quality. Execution reuses the registered native
worktree206f at baseline `0aa0cc007db63449455a1c4f9b6d92cb60c5d29a`.
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
A09 still requires observed hosted CI on the exact candidate, including the
configured Linux/macOS/Windows routine matrix and actual local hook evidence.

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

## Hosted verification boundary

Publish only the reviewed compliance unit on a dedicated verification branch to
obtain hosted CI; keep earlier release-design/scope drafts local and preserve
unrelated work. A pushed candidate is not a product release. Record source,
tested commit, branch, CI jobs and later evidence-storage identity separately.
Only actual passing CI plus accepted independent evidence can close the remaining
rows and lift the Python-feature gate for the assessed candidate.
