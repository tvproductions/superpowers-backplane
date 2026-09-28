# Superpowers Backplane 1.0 Project PRD

**Status:** Approved by the named approver in the 2026-09-27 operator review; the operator subsequently clarified Python as SP-BP's implementation language without changing the twelve requirement IDs or wording. Integration and issue-anchor migration are pending. Reviewed draft SHA-256: `F6429F8618DE98B953CB0E5A432CB56236DF2138F46A354AB9361EEB74CA9050` before this annotation. The IDs and wording below are approved for the planned 1.0 migration, while live v0.1 issues remain under their current contract until reconciled.

**Named approver:** Jeffry Babb (`ahuimanu`), confirmed in the 2026-09-27 operator review.

**Target:** `1.0.0`, not yet approved for publication. This target does not rewrite historical `0.1.0` package fixtures or verification records.

## Purpose, users, and success

An adopting repository should be able to use Superpowers for feature design and implementation while retaining a trustworthy, navigable product arc in GitHub Issues. Repository maintainers need stable requirement and outcome identity, current traces and generated views, and a release decision grounded in observed behavior. Contributors need a bounded issue and current Superpowers plan without a second mutable backlog. Release approvers need to distinguish specification verification, intended-use validation, compatibility, and their own publication authorization.

Success is demonstrated by one self-hosted migration of this repository and one external adopting-project pilot that exercise the complete 1.0 contract on the declared harnesses, with fresh evidence and no unreviewed issue or user-file loss.

## Scope and assumptions

The heavy profile is selected through `gz-skills` setup; lite remains a standalone portable-skill mode. SP-BP owns the heavy issue catalog, graph, traces, views, evidence, and releases. Its implementation, CLI/helpers, and tests use Python with thin host adapters; this does not choose an adopting project's application language. Superpowers remains the feature design and execution spine. The adopting project names its approvers, commands, compatibility promise, and supported harnesses. Git and authenticated `gh` are available. GitHub Projects, IssueOps, gzkit's full lifecycle machinery, and an undisclosed consuming-project runtime are outside scope. The installed Python invocation must be proved and any runtime dependency disclosed before heavy readiness.

The initial supported harnesses are Codex, Claude Code, and OpenCode V1/V2. A project verifies only the harnesses it declares. Existing v0.1 host installation work is historical evidence and is reassessed for the 1.0 contract; it is not automatically sufficient for it.

## Proposed stable requirements

| ID | Requirement wording | Measurable success criterion |
| --- | --- | --- |
| `BP-R001` | A heavy adopter shall have an approved constitution, project PRD, and current architecture description, with a named human approver, before feature approval is claimed. | `gz-skills` routes profile setup; an SP-BP heavy operation reports readiness only after document approval and compatible gz-skills, SP, and SP-BP are verified on each declared harness, naming pending inputs. |
| `BP-R002` | The project PRD shall own each approved requirement's stable ID, exact wording, approval, intended users, and success criteria; a GitHub issue shall anchor and track the requirement without superseding its wording. | Changing an issue alone leaves requirement approval unchanged; a PRD change is detected and affected traces/evidence are re-evaluated. |
| `BP-R003` | SP-BP shall distinguish requirement, capability, outcome, epic, milestone, gate, boundary, release, and incidental issue kinds, with state rules appropriate to each kind. Incidental intake needs no semantic ID or record block until promotion. | Contract checks reject a non-executable issue forced into the six-label execution ladder, reject an executable outcome missing its one valid label, and accept an unpromoted incidental issue with only its GitHub identity. |
| `BP-R004` | Approved planned nodes and requirements shall have never-reused semantic IDs independent of GitHub issue numbers and release versions. | Family moves preserve IDs; a semantic change creates a new ID with an explicit historical link; duplicate and dangling IDs fail validation. |
| `BP-R005` | SP-BP shall represent many-to-many typed relationships among requirements, outcomes, decisions, SP artifacts, evidence, and releases while preserving native hierarchy and blocking edges. | A validator produces both forward and reverse links, detects conflicting or missing targets, and never treats typed prose as a native blocker. |
| `BP-R006` | SP-BP shall reconcile each claimed requirement-to-outcome trace against current approved PRD and issue revisions and flag missing, ambiguous, or stale links and evidence. | An outcome cannot be marked verified when any claimed governing requirement lacks current evidence; a changed requirement invalidates later-release use of affected evidence while retaining history. |
| `BP-R007` | SP-BP shall distinguish verification of specified requirements from validation of intended use and stakeholder needs. | The release gate requires separately identified verification and validation evidence with methods, results, source revisions, and accepting person; neither substitutes for the other. |
| `BP-R008` | `ROADMAP.md` and `BACKLOG.md` shall be generated readable views of a validated issue and approved-document snapshot, not editing surfaces. | The generation/check process records an input hash, rechecks revisions, reproduces identical bytes for unchanged inputs, and refuses a current claim after concurrent change, missing data, or an unverified offline snapshot. |
| `BP-R009` | A release shall have a stable record and issue anchor independent of its mutable target version, selected outcomes, immutable published inclusion, and separate gate and publication states. | A slipped target version does not rename semantic IDs; `released_in` cannot change after publication without a new corrective record. |
| `BP-R010` | Publication shall require verified included outcomes on integrated source, current traces, distinct intended-use validation, a review against the project's declared public compatibility contract and SemVer, and explicit human authorization for the exact candidate. | A missing or unknown input blocks publication; agent-authored approval, plan completion, PR creation, issue closure, or tag existence alone does not satisfy the human decision. |
| `BP-R011` | Backplane 1.0 shall support native plugin adoption and independent upstream Superpowers discovery on Codex, Claude Code, and OpenCode V1/V2 without loss of unrelated user state. | Each declared host variant passes fresh-session discovery and its installation, update, rollback, uninstall, provenance, and relevant conformance checks from installed packages. |
| `BP-R012` | This repository's v0.1 issue graph and evidence shall migrate deliberately to the 1.0 model without silently changing historical meaning. | A reviewed before/after map covers every existing issue, preserves native links and completed evidence, records dispositions and revision reconciliation, and leaves unresolved links visible. |

## Public compatibility contract

Backplane's public promises are the discoverable skill names and their documented behavior; the canonical heavy issue-record schema and typed link meanings; the generated view formats and freshness semantics; and the release-gate decision contract. Host plugin identifiers and documented installation lifecycle are public surfaces. Repository-local plan paths, transient test fixtures, and internal generation implementation details are not public compatibility promises unless a release document explicitly adds them.

Before `1.0.0`, the project may revise these draft surfaces with documented migration. Publishing `1.0.0` fixes a baseline against which compatible features, fixes, and breaking changes are judged. The version itself is never a requirement or outcome ID.

## Approval and trace rule

Approval records the exact reviewed revision of this PRD and the named human decision. Requirement anchors are created or reconciled only afterward. A changed approved requirement triggers an impact review of linked outcomes, evidence, generated views, and later releases; previous published evidence remains historical. A GitHub issue may discuss a requirement change but does not approve it.
