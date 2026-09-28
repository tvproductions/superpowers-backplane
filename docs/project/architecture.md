# Superpowers Backplane 1.0 Architecture

**Status:** Approved by the named approver in the 2026-09-27 operator review; integration and implementation are pending. Reviewed draft SHA-256: `0F590D1053A1342F0E553349DE479F65873B7D99DFA67EF27F774B474CE0F3CA` before this annotation. The [heavy SDD ADR](../superpowers/specs/2026-09-27-heavy-sdd-backplane-adr.md) records the governing decision; the [project PRD](prd.md) owns requirement wording and approval.

## Goals and constraints

Backplane makes a GitHub issue graph and approved project documents readable and verifiable across sessions and supported agent harnesses. Its catalog, issue reconciliation, traceability, V&V, view and release logic, CLI/helpers, and tests share one Python core. Host-specific adapters stay thin. It must keep upstream Superpowers independently installed, use `gh` for GitHub operations, avoid GitHub Projects and IssueOps authority, and leave the adopting project's application language and test runner to that project. The same canonical skill tree serves all native host packages. Freshness and release decisions fail closed on unknown or inconsistent inputs.

## Context

The adopting project supplies approved governing documents, human approvers, public compatibility promises, verification commands, and declared harnesses. `gz-skills` handles lite/heavy selection and MPAS adaptations. Upstream Superpowers handles feature brainstorming, specifications, plans, execution, test-first work, and review. SP-BP reads those authorities and manages its own GitHub issue-backed catalog, trace, projections, V&V and release records. GitHub is the external mutable issue service; Git is the source and integration history.

## Building blocks and interfaces

| Block | Responsibility | Consumes | Produces |
| --- | --- | --- | --- |
| Native issue reader | Complete `gh` intake, pagination, relationship and revision observations | Repository identity, issue URLs, `gh` auth | Versioned raw issue observations or explicit error |
| Record validator | Kind/status/ID/link checks; distinction between native and semantic edges | Issue observations, approved PRD ID registry, schema | Validated graph or specific missing/conflict/stale findings |
| Trace reconciler | Forward/reverse requirement, outcome, ADR, SP artifact, evidence, and release links | Validated graph, approved document revisions, integrated source identity | Current/stale/unknown edge decisions and V&V coverage |
| View projector | Deterministic roadmap/backlog rendering and freshness check | Validated snapshot with input hash | `ROADMAP.md`, `BACKLOG.md`, byte and hash comparison result |
| Release gate | Candidate and publication preconditions | Selected outcomes, trace, V&V, compatibility review, exact human decision | Blocked/candidate/approved/published record decision |
| Skills and native packages | Human and agent workflow around the above contracts | Active harness, installed SP, `gh`, project rules | Discoverable guidance on Codex, Claude Code, and OpenCode |

These are responsibility boundaries, not a mandate to create six executable modules. Small, portable contract/reference files remain appropriate where a validated agent workflow suffices. The [approved view-helper ADR](../superpowers/specs/2026-09-27-heavy-view-generator-decision.md) authorizes one read-only packaged helper for snapshot validation and generated views, subject to installed-host proof; no consuming-project runtime is assumed.

## Data and control flow

1. `gz-skills` records a project's profile choice. For heavy use, SP-BP checks approved governing documents and compatible installed components; pending readiness is reported, not fabricated.
2. The PRD supplies approved requirement IDs and revisions. `gh` supplies complete issue records and native edges. The validator checks `## Backplane Record` metadata and builds an issue-address-to-semantic-ID map. Invalid or ambiguous records stop dependent trace and release claims.
3. SP specifications and plans link to bounded executable outcomes. The trace reconciler follows typed links in both directions, ties evidence to requirement/outcome and integrated-source revisions, and separates verification from intended-use validation.
4. The view projector collects a consistent source snapshot, canonicalizes and hashes inputs, renders both Markdown views, then rechecks the source before publication. A changed source triggers retry; unknown freshness is reported as unknown.
5. A release record selects outcomes. The gate checks integrated evidence, current trace, validation, compatibility and SemVer review, native blockers, view freshness, and the named human's exact-candidate authorization. Publishing a tag and GitHub release is a later authorized act.

## Runtime and deployment views

The authored Backplane skills live only in this repository's root `skills/`. Native host metadata points there. Upstream SP is a separate native plugin or independently identifiable checkout. `gh` and Git are operational dependencies. GitHub issues remain the delivery system of record; approved project documents and committed SP artifacts live in the adopting repository. Generated views are committed outputs and carry source identities and freshness status.

The present v0.1 package has no standalone Backplane executable. The 1.0 design uses a Python core and bundled CLI/helpers for catalog, reconciliation, trace, V&V, snapshot, view, and read-only release assessment, per the [Python core ADR](../superpowers/specs/2026-09-27-python-core-adr.md). Its installed invocation and runtime distribution mechanism remain open pending proof; Python source does not automatically impose a consuming-project runtime. Until the helper passes local and installed-host proof, the architecture does not claim automated projection or gate assessment.

## Evolution and migration

The [migration map](../superpowers/migrations/2026-09-27-v01-to-v1-issue-map.md) starts with a full read-only issue snapshot. Existing issue numbers, native history, linked PRs, closed outcomes, and v0.1 specifications remain intact. Review maps each to a heavy kind, semantic ID if enduring, approved PRD links, evidence currency, and disposition. The old six-label contract stays operational for unconverted issues; a heavy reader identifies legacy state rather than silently interpreting it. The current #19 plan branch is separate and remains unapproved until reconciled.

Hexagonal boundaries are useful around external `gh` data, local approved documents, projection, and publication commands. The Python identity, trace, V&V, projection, and gate rules must not depend on one host adapter. The CLI separates its GitHub collection adapter from pure validation and rendering so snapshot-race tests can inject issue revisions without network calls. Python assesses the release gate from validated evidence; the named human authorizes publication, and the CLI does not publish on its own.
