# ADR: Packaged deterministic snapshot and view helper

- **Status:** A bounded bundled helper was approved by Jeffry Babb (`ahuimanu`) in the 2026-09-27 operator review. The Go recommendation in the reviewed draft was challenged and withdrawn before implementation; the [Python core ADR](2026-09-27-python-core-adr.md) records the operator's corrected direction. Reviewed proposal SHA-256: `04A2F85686223357EA31C958FFFD2536263A19DD537D173EFF675071FD9FD15C` before this annotation. No generator, packaged executable, or view has been released.
- **Date:** 2026-09-27
- **Related approved design:** [Heavy SDD Backplane ADR](2026-09-27-heavy-sdd-backplane-adr.md), [project architecture](../../project/architecture.md), and [freshness scenario](../../../tests/scenarios/2026-09-27-heavy-view-freshness.md).
- **Decision needed:** The approved design requires validated, byte-reproducible views and a freshness check without requiring an adopting project's language runtime. The v0.1 design excluded a standalone Backplane executable. This ADR would explicitly supersede that exclusion for one bounded helper if its installed-package proof passes.

## Context and observed constraints

`gh` and Git are the existing required adopter tools. On this repository, authenticated `gh` 2.101.0 fetched all 21 issues with `gh issue list --state all --limit 100000 --json ...`, and an independent GraphQL total also returned 21. `gh api --paginate --jq` traversed the current multiple REST pages, but `gh api --paginate --slurp --jq` is rejected by the installed CLI. These observations prove useful collection primitives, not complete record parsing, cross-page uniqueness checks, document hashing, revision-race retries, or byte-identical projections. A high `--limit` is not proof that a larger repository was fully collected.

The heavy contract requires record-schema validation, typed endpoint checks, approved PRD reconciliation, forward/reverse trace, evidence currency, a canonical input hash, prepublication recheck, offline failure, and two generated files. Implementing those as an agent-composed sequence of `gh` formatting expressions would leave the exact algorithm and shell encoding behavior hard to verify across Codex, Claude Code, Windows, macOS, and Linux. Requiring Python, Node.js, `jq`, or a project test runner would violate the approved language-neutral adopter boundary.

## Recommended decision

Package one small SP-BP-owned, read-only Python snapshot/view/check helper with the Backplane plugin, using the same Python catalog, reconciliation, trace, and V&V core as the release logic. Its installed invocation and runtime packaging must pass the declared-host proof before release. The helper invokes authenticated `gh` and Git, reads approved local documents, validates untrusted issue records, builds a canonical snapshot, rechecks source revisions, emits `ROADMAP.md` and `BACKLOG.md` to temporary files, and replaces the pair only when both validate. A `check` mode performs a fresh collection and byte comparison without writes. It does not edit issues, approve documents, select work, authorize releases, publish tags, or become a central lifecycle CLI. Its identity and version are part of the Backplane compatibility preflight and installed-host conformance. Thin host adapters invoke this core without parallel business rules. An adopter runtime requirement, if any, must be explicitly disclosed and reviewed rather than inferred from the Python source.

This is a narrow exception to the older no-standalone-executable decision. It leaves the three-component ecosystem intact: the helper is an SP-BP package artifact, not a fourth plugin. It also leaves SP feature workflows and gz-skills profile setup untouched.

## Alternatives considered

| Option | Finding |
| --- | --- |
| Skill-only `gh`/Git instructions | Smallest package, but the complete validator, canonicalizer, race retry, and generated-byte check would rely on agent and shell interpretation. The current CLI probes do not demonstrate the required invariant across hosts. Keep as fallback only if a full executable conformance proof can be produced. |
| Require Python, Node.js, or external `jq` in every adopter | Easier scripting, but adds a consuming-project runtime/tool dependency that the approved architecture forbids. |
| Hosted action, GitHub Projects, or IssueOps | Moves authority or execution outside the approved local GitHub Issue model. |
| Packaged read-only helper | Adds release artifacts and platform testing, but makes the source algorithm and failure behavior independently testable without imposing a project runtime. Recommended. |

## Proof before acceptance

Build fixture tests for 105 paginated issues, family move, split, many-to-many links, PRD change, stale evidence, malformed records, missing permissions, issue change during collection, offline mode, and a release slip. Check stable bytes on unchanged inputs and failing freshness after a source change. Exercise the installed helper on each declared operating system and Codex, Claude Code, and OpenCode variant used by this repository; a build artifact alone is not installation proof. Record package size, checksums or source identity, provenance, update/rollback behavior, and failure preservation. If a platform lacks a working helper, its heavy view capability remains `UNKNOWN` and 1.0 readiness is blocked there.

No live GitHub issue or release mutation follows from accepting this implementation decision. A later reviewed issue mapping can promote #9's old helper-evaluation address into a bounded 1.0 outcome or create a new outcome while retaining #9 as historical decision context.

## Bounded implementation observation

A local Windows `uv build` wheel now exposes a read-only `backplane preflight` entry point. It ran through Astral `uvx --offline` from the separate repository root and reported the 21 live issues with heavy readiness `UNKNOWN`; see [the exact transcript](../../../tests/scenarios/transcripts/2026-09-27-python-uvx-local-preflight.md). This proves package invocation on one prepared host only. It does not establish a clean-adopter Python supply route or the required generate/check, macOS, Linux, Claude Code, and OpenCode conformance. `uvx` is the proposed Astral invocation path; any required `uvx` installation and interpreter acquisition must be disclosed before heavy profile readiness.
