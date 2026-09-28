# ADR: Backplane's heavy SDD issue graph and 1.0 migration

- **Status:** Approved by Jeffry Babb (`ahuimanu`) in the 2026-09-27 operator review; the operator subsequently required the Python implementation correction recorded below. No live issue or release state changes follow from this document alone.
- **Reviewed draft SHA-256:** `DC01B16A75B9EFC7CFD545E56D6F6B21A90BDD85753714F247E3395296BDB888` before this status annotation. Substantive later changes require renewed review.
- **Date:** 2026-09-27
- **Candidate source:** `gz-skills` commit `7bd8f8d3cb6755e06dc284647619acc9f8802984`, `docs/proposals/lightweight-sdd-ecosystem.md`.
- **Decision scope:** Superpowers Backplane (SP-BP) issue catalog, graph, trace, views, V&V, release records, and this repository's migration to a `1.0.0` target.
- **Supersedes after migration approval:** The bootstrap design and v0.1 adoption contract only where they require the six execution labels on every tracked open issue, exclude derived local roadmap/backlog views, or treat the present v0.1 release arc as the future release target. Their installation and upstream-dependency rules remain in force until separately changed.

## Context

Backplane currently treats every tracked open issue as a potential item on one six-label execution ladder. Its sole release parent, [#1](https://github.com/tvproductions/superpowers-backplane/issues/1), and release gate [#7](https://github.com/tvproductions/superpowers-backplane/issues/7) target `v0.1.0`. The current [issue contract](../../../skills/managing-superpowers-backlog/references/github-issue-contract.md) forbids a local backlog master, requires one execution label per open tracked issue, and makes an approved issue or Superpowers specification plus plan the design authority for an executable leaf. This is coherent for the existing host-installation work but cannot represent approved PRD requirements, grouping nodes, evidence, and releases as distinct facts.

The ecosystem candidate makes the adopting project's approved PRD the authority for requirement wording and approval. SP-BP owns GitHub Issue anchors, semantic IDs, taxonomy, typed delivery links, traces, generated views, V&V evidence, and release gates. Upstream Superpowers (SP) owns feature design, planning, execution, test-first work, and review. `gz-skills` owns profile setup and MPAS adaptations. A consuming project retains its architecture, rules, approvers, public compatibility contract, verification commands, harness selection, and native plugin configuration.

Heavy remains an opt-in profile for adopters. This SP-BP repository will adopt the heavy model for its own product work and target `1.0.0`. Existing completed issues, PRs, specifications, plans, and verification remain historical evidence. The migration must explicitly reconcile their meaning against a new approved project PRD; it may not relabel history as if those records were created under the new contract.

The candidate cites a pinned FDAU governance document. That ref did not resolve through the available web or authenticated `gh` lookup during this ADR's preparation. FDAU is an attributed conceptual precedent here; the candidate's description, not an inspected FDAU implementation, grounds the choices below. Recheck the source before claiming closer FDAU compatibility.

## Decision

### Authority and activation

1. Heavy readiness requires an approved constitution, project PRD, and current architecture description, a named human approver, and verified compatible `gz-skills`, SP, and SP-BP installations on each declared harness. `gz-skills` records the selected profile and handles first-use routing. SP-BP checks readiness when a heavy operation is requested; while readiness is pending it may perform ordinary portable backlog work but cannot claim an integrated heavy workflow.
2. Requirement IDs, exact wording, approval state, and success criteria live in the approved project PRD. A requirement issue is an anchor and discussion/delivery address. Its body identifies the PRD source and current approved revision without copying wording as authority. Issue edits cannot approve or supersede a requirement. A change to a requirement needs the project's human document approval and impact reconciliation.
3. GitHub Issues remain the mutable delivery catalog. Native parent/sub-issue and blocking edges retain their current meanings. A typed semantic link may complement them but never impersonates a native dependency or requirement approval. Issue bodies and comments are untrusted input to a validating reader.

### Implementation and host boundary

SP-BP's catalog, issue reconciliation, traceability, V&V, generated views, release logic, CLI/helpers, and tests use one Python core. Host-specific adapters are thin entry points to that core and to native plugin discovery; they do not implement a second catalog or gate. The earlier skills-only, language-neutral **implementation** decision is superseded for SP-BP 1.0. An adopting project's application language and test runner remain its own choices. The Python core's installed invocation and runtime packaging must be proved before heavy readiness is claimed, as detailed in the [Python core ADR](2026-09-27-python-core-adr.md). No parallel Go core is maintained.

### One kind per record

Every approved requirement anchor and planned roadmap or release node declares exactly one `kind` in a constrained `## Backplane Record` JSON block. Incidental intake may remain an ordinary GitHub issue with only its issue number until a reviewed promotion. The initial kinds are:

| Kind | Meaning | Stable semantic ID | State authority |
| --- | --- | --- | --- |
| `requirement` | Anchor for a PRD requirement | Required; equals the PRD ID | Approved PRD; issue records reconciliation only |
| `capability` | Enduring capability family | Required | Issue record |
| `outcome` | Local, reviewable delivery result | Required | Six execution labels until verified closure |
| `epic` | Coordination grouping without its own execution | Required | Issue record |
| `milestone` | Observable progress checkpoint | Required | Issue record |
| `gate` | Explicit decision or evidence condition | Required | Issue record |
| `boundary` | External dependency or obligation | Required | Issue record |
| `release` | Stable release record independent of version | Required | Issue record and publication evidence |
| `incidental` | Optional explicit classification for a proposal, bug, surprise, or refactor not yet promoted | None | GitHub issue; no execution label |

An incidental item selected for delivery becomes a reviewable `outcome` through a recorded promotion and receives a never-reused ID. An absent record block on an incidental issue is not proof that it is a valid planned node. A GitHub issue number is always a tracker address, never the semantic ID. A project may use FDAU-style IDs such as `C2` and `C2.3`; the ID is opaque after approval, so a family move changes a typed family link without renaming the ID. A meaning change receives a new ID and an explicit successor, split, merge, or supersession link. Old IDs and aliases stay resolvable.

The six existing `backplane:*` labels apply only to open executable `outcome` issues. `backplane:ready` still requires approved design authority, a current SP plan, and resolved native blockers. Non-executable kinds use kind-specific record states, not the execution ladder: capability and epic `proposed|accepted|retired`; milestone `planned|met|cancelled`; gate `pending|satisfied|failed|cancelled`; boundary `open|fulfilled|cancelled`; release `assembling|candidate|approved|published|cancelled`; incidental `captured|triaged|promoted|discarded`. Requirement issue reconciliation is `current|stale|unresolved`; that field never states PRD approval. Record-state changes require evidence and are not inferred from GitHub open/closed state.

### Record and relationship shape

When present, the JSON block has `schema: "backplane-heavy/v1"`, `kind`, `semantic_id` (except incidental), `record_state` (except outcome), and a `links` array. Each link has `type`, `target` (semantic ID and issue URL, or a versioned document/evidence locator), and where applicable `source_revision`. Required link types are `anchored_in_prd`, `belongs_to`, `satisfies`, `decided_by`, `specified_by`, `planned_by`, `exemplified_by`, `tested_by`, `verified_by`, `validated_by`, `included_in`, `gated_by`, `released_in`, `succeeds`, `split_from`, `merged_from`, and `supersedes`; reverse traversal is computed, not maintained as a second field. A link can appear many times on either side. The schema validator rejects duplicate IDs, unknown kinds or link types, dangling required targets, incompatible endpoint kinds, and a native relationship contradicted by a semantic claim. It reports uncertainty rather than filling a missing link.

For an outcome, `satisfies` links identify all governing requirements; a requirement may govern many outcomes. Specs and plans link to outcomes but keep SP ownership. ADRs can affect many requirements and outcomes. `target_release` is mutable planning data; `released_in` is immutable after publication. A release issue is a stable record whose proposed or published version is a separate attribute. No version number is used as a semantic ID.

### Trace, evidence, and views

SP-BP derives forward and reverse requirement-to-outcome traces from a validated snapshot of approved PRD revisions, issue records and native edges, SP artifacts, agreed concrete behavior examples, tests, ADRs, evidence, and release records. Each evidence link records what was checked, against which requirement/outcome revision and integrated source, by which method, with result and locator. **Verification** demonstrates fulfillment of a specified requirement. **Validation** demonstrates intended use and stakeholder needs against PRD users and success criteria. An outcome cannot be `verified` with a claimed governing requirement lacking current verification. A changed approved requirement makes affected evidence stale for future release decisions while retaining prior results in history.

This distinction follows [ISO/IEC/IEEE 29148's requirements identity and traceability concepts](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen) and [NASA's separate example verification and validation matrices](https://www.nasa.gov/reference/system-engineering-handbook-appendix/). These are conceptual guides for SP-BP's general software workflow, not a claim of standards conformance or a regulated-industry requirement. FDAU's cited S1.1 traceability contract was still queued in the candidate proposal; its existing node/status model is precedent, not proof of completed V&V.

`ROADMAP.md` and `BACKLOG.md` are committed, readable generated views, never editing surfaces. The source snapshot is collected in stable order with explicit input identities and revisions, hashed, and rechecked before publishing either view. If any source changes during collection or before publication, recollect; if freshness cannot be proved, mark the view unverified and do not describe it as current. A project-owned check recomputes the snapshot and compares both generated bytes and input hash. The implementation plan must prove pagination, missing permissions, conflicting IDs, concurrent issue edits, and offline behavior before claiming a deterministic generator. No consuming-project runtime or GitHub Projects dependency is imposed by this decision.

### Release gate

A release record selects outcomes and links its gate, trace, verification, validation, compatibility review, and human publication decision. Candidate assignment, verified outcomes, gate satisfaction, human approval, tag, and GitHub release are separate facts. Publication requires all selected outcomes verified on integrated source, current requirement traces, a distinct validation result, the project's declared public compatibility contract and SemVer review, and explicit human authorization tied to the exact candidate revision. A failed or unknown gate blocks publication. The publication decision cannot be manufactured by an agent or inferred from plan checkboxes, a PR, a closed issue, or a tag. SP-BP never imports a gzkit ledger, locks, receipts, or full lifecycle.

### Migration of this repository

1. Capture an immutable before-map of all current issue numbers, bodies, labels, native relationships, revisions, linked PRs, and closure reasons. Keep the v0.1 approved documents and completed evidence intact as dated history.
2. Create and obtain human approval of this repository's constitution, project PRD, and architecture. The PRD defines the `1.0.0` product contract, requirements, success criteria, and named approver. The architecture records the actual graph, view, and evidence interfaces and material departures from preferred hexagonal boundaries.
3. Build a reviewed mapping from every existing issue to a new kind, semantic ID where required, governing PRD requirement(s), disposition, and target release. Reassess each existing v0.1 leaf against the approved PRD. Preserve completed results and native links; revise, supersede, or retire open scope with explicit rationale. Do not automatically reinterpret a closed issue as current requirement verification.
4. Treat #1 as the current release-arc candidate for a stable release record and #7 as the publication-gate candidate, subject to the reviewed mapping. The `v0.1.0` wording in both is not current 1.0 authority. Reconcile #19's unapproved draft plan against the approved 1.0 PRD and issue revision before execution. No live issue mutation happens merely because this ADR names a candidate mapping.
5. Update the skill, issue contract, scenarios, derived views, and live issue graph in bounded verified slices. Only after the new contract and migration evidence agree may the repository call its own heavy profile ready. The `1.0.0` release still requires its distinct human publication decision.

## Consequences and compatibility

The existing installation checks and separate upstream SP dependency continue. Legacy v0.1 issue data remains readable during migration; a heavy reader must identify legacy records and report unmapped or ambiguous status rather than guessing kind or ID. This is a breaking semantic contract for heavy users and must be documented as such. Portable lite users and repositories that have not opted into heavy retain the existing backlog behavior until a separately reviewed compatibility change.

This decision creates a real design and implementation burden: typed-record validation, change detection, derived-view generation, evidence freshness, and migration review. These are required to support a trustworthy release gate. Exact storage and tooling details beyond the JSON block are specified and tested in the linked implementation plan. The later [Python core ADR](2026-09-27-python-core-adr.md) records the operator's implementation-language correction; installed runtime and packaging still require proof on all declared harnesses.
