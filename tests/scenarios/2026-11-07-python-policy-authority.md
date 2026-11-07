# Independent Python authority — November 7, 2026

The maintainer directed cross-repository correction and reaffirmed current
policy: Python 3.14 for ordinary projects, 3.12 for X-Plane/XPPython3-bound code.
Backplane owns its own implementation/tooling policy, not consuming-project
runtime choices. Its October 25 independent 3.14 decision and October 31 exact
3.14.10 selection already establish the correct family. This change makes
that ownership explicit to avoid fallback drift from supporting skills.

Source authority reviewed: starter
`4f8bb09633655473cd6aab9e1ddc60963c487bb1`, including baseline/Python/versioning
policy, AGENTS and the gz-skills mapping. No formal template adoption occurs.
No XPPython3 loading boundary applies to Backplane's own tooling.

At investigation, `.python-version`, `.venv/pyvenv.cfg` and actual execution
agreed on managed Python 3.14.10. A separate ongoing strict Astral reconciliation
then added the existing non-package pyproject/lock, routine hooks, CI and
engineering contract. Its family declaration is `>=3.14,<3.15`, Ruff target
py314, ty 3.14, with uv compatibility minimum >=0.13.5. These changes belong to
that work and are preserved, not credited as implementation of this correction.
Earlier no-project command evidence retains its historical runtime/context.

The separate gz-skills candidate removes the competing fallback family/tool/
package standard and resolves each consuming project's authority. Backplane
keeps its own family and verification contract; unrelated consumers do not
inherit a blanket Python mandate. Installed gz-skills 0.8.3 remains immutable
until a separately reviewed release/update. Do not claim installed correction
from source edits or development metadata alone.

Preserve all pre-existing release-doctrine/scope and strict-Astral working-tree
changes. This correction adds a narrow AGENTS clarification, this receipt and
an appended release binding. It changes no runtime pin, dependencies, profile,
shipped skill, native plugin installation, issue state, commit or publication.
Verification must use the current project-owned locked commands, record actual
runtime/tool provenance and preserve the strict acceptance matrix's UNKNOWNs.

## Verification of this correction

Current `uv lock --check` passes. `uv run --locked python` reports managed
3.14.10 from this repository's `.venv`, with uv resolving from that environment.
All four current routine hooks pass and the separate native OpenCode adapter
suite passes 9/9. This verifies applicable local checks for the documentation
clarification, not full strict-Astral acceptance or new native host readiness.
The existing acceptance matrix's wider UNKNOWNs remain explicit.

No declared family, exact pin, lock or shipped skill is changed by this task.
The pre-existing `docs/release-policy.md` content is preserved as an unchanged
prefix before this task's appended section. Strict-Astral and release-doctrine
work remain uncommitted and separately attributable.

## Authorized scoped synchronization

The maintainer requested Git sync after the correction. Reviewed starter
source is committed at `a483e382146c6082e590e31494c07d1812645014` and verified on its remote main. Stage only
this receipt, the four-line AGENTS authority clarification and the independent
Python-family section of the binding. Existing strict-Astral/release-scope work
remains uncommitted. Its locally passing hooks do not establish that pending
configuration on the committed tree. There is no configured project-quality CI
in the intended commit; report that limitation separately from remote alignment.
