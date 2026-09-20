# Host Installation Leaf Rescoping Design

- **Status:** Draft for written review; the eight-child split was approved in conversation on 2026-09-19.
- **Scope:** GitHub issues #11 and #12 and their verification ownership.
- **Functional authority:** docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md.
- **Observed issue revisions:** #11 2026-09-19T14:11:46Z; #12 2026-09-19T14:11:57Z; pilot #6 2026-08-23T13:55:24Z.

## Problem and intended outcome

Issue #3 combined packaging, documentation, multiple setup modes, failure probes,
lifecycle operations, conformance, and integration. Issues #11 and #12 currently
repeat that shape; #12 additionally combines OpenCode V1 and V2. Both have zero
sub-issues and no implementation plan. Give each remaining host task one
reviewable deliverable while preserving every v0.1 acceptance obligation. This
rescope changes ownership and order, not the supported hosts or package design.

## Invariants

- The canonical Backplane skills remain under the repository root skills/
  directory. Claude Code metadata and one shared OpenCode adapter refer to
  those skills; neither copies upstream Superpowers or Backplane skill text.
- Upstream Superpowers is installed and updated independently. Default
  acquisition follows the active host's documented stable channel.
- Claude Code, OpenCode V1 1.18.29+, and OpenCode V2 2.0.4+ retain the complete
  installation, provenance, preservation, fresh discovery, lifecycle, and five
  named conformance obligations from the approved v0.1 contract.
- The OpenCode variants share one adapter but own separate live verification.
  V1 below 1.18.29 and V2 below 2.0.4 remain unsupported negative cases.
- An absent authenticated host session is a prerequisite gap for the affected
  live check. Do not retry login repeatedly, copy user credentials, or claim
  a package check passed from repository-discovered skills.
- No release, pilot execution, new harness, generic runtime, GitHub Project,
  IssueOps system, or upstream update is part of this rescope.

## Target native hierarchy

Keep #11 and #12 as children of release parent #1. They become continuity
parents for the following executable grandchildren. The titles below are
stable creation keys; check for duplicates before creating any issue.

| Key | Parent | Proposed child title | Independently reviewable outcome |
|---|---|---|---|
| C1 | #11 | Package and document Claude Code plugin installation | Native manifest and marketplace point to canonical skills; pinned install guide and one disposable clean-install/fresh-discovery smoke run with compatible preinstalled upstream. Lifecycle claims remain pending. |
| C2 | #11 | Verify Claude Code setup and upstream adoption | Native package, authoritative sibling, and absent-upstream setup paths; provenance, gh capability, fresh discovery, and fail-closed unknown, versionless, duplicate, dirty, and conflict preservation evidence. |
| C3 | #11 | Verify Claude Code lifecycle and conformance | Repeat install, pinned update, rollback, Backplane-only uninstall, verified guide commands, per-operation preservation, five named checks, authorized issue-state scenarios, and integrated installed-package verification. |
| O1 | #12 | Build and document the shared OpenCode V1/V2 adapter | One entry point and guide for V1 plugin and V2 plugins configuration; basic install/discovery smoke on both supported variants with compatible preinstalled upstream. |
| O2 | #12 | Verify OpenCode V1 setup and compatibility failures | V1 1.18.29+ upstream modes, provenance and gh preflight, fresh discovery, unknown/versionless/duplicate/dirty/conflict preservation, and below-floor rejection. |
| O3 | #12 | Verify OpenCode V1 lifecycle and conformance | V1 repeat install, pinned update, rollback, Backplane-only uninstall, per-operation preservation, five checks, and integrated installed-package verification. |
| O4 | #12 | Verify OpenCode V2 setup and compatibility failures | V2 2.0.4+ upstream modes, provenance and gh preflight, fresh discovery, unknown/versionless/duplicate/dirty/conflict preservation, and below-floor rejection. |
| O5 | #12 | Verify OpenCode V2 lifecycle and conformance | V2 repeat install, pinned update, rollback, Backplane-only uninstall, per-operation preservation, five checks, and integrated installed-package verification. |

Each child gets the standard executable issue headings: Objective, Bounded
Scope with Allowed and Out of Scope, Acceptance Criteria, Verification Seams,
and Superpowers Artifacts. The approved v0.1 functional specification and this
rescoping design are design authorities. Its own Superpowers implementation
plan is created only when that child is selected; until then it stays at
backplane:backlog and its artifact section says Plan: not yet created. Each child must name the host revision, Backplane revision,
upstream identity, gh capability result, installed skill identities, and
PASS/FAIL/UNKNOWN outcome for its owned check.

C1 owns package and guide scaffolding, not unverified update or rollback
instructions. C2 may correct setup instructions against observed host behavior.
C3 finalizes only lifecycle instructions it has actually replayed. O1 owns
shared adapter architecture and initial guide. O2 and O4 own variant-specific
setup and failure behavior; O3 and O5 own variant-specific lifecycle and
conformance. Previous child evidence is reused when its tested inputs have not
changed; a changed package or guide seam is rerun in the owning child.

## Native dependencies and continuity

- C1 blocks C2; C2 blocks C3.
- O1 blocks O2 and O4; O2 blocks O3; O4 blocks O5. V1 and V2 may progress
  independently after O1.
- Keep the existing #2-to-#11/#12 historical blocker edges and the #11/#12-to-#6
  pilot blocker edges. Do not replace them with prose or add duplicate pilot
  edges from every grandchild.
- #11 is complete only after C1-C3 close as completed and Claude's integrated
  installation matrix passes. #12 is complete only after O1-O5 close as
  completed and both OpenCode variant matrices pass. Parent completion needs
  aggregate evidence; child completion alone does not close a parent.
- Parents retain exactly one lifecycle label while open. They remain backlog
  during redistribution; future design, execution, review, and completion
  transitions require their normal evidence gates. The rescope plan does not
  mark either parent or child ready.

The parent bodies should become concise continuity contracts: objective,
child-owned scope, aggregate acceptance, verification of native sub-issues,
and artifact links. They must not duplicate the children's implementation
steps. Pilot #6 remains blocked by #11 and #12, along with its other existing
blockers. Codex #3 remains completed and unchanged.

## Verification ownership

Revise tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md after
the native child URLs exist. Keep the original assignment observation as
historical evidence and add the new owner mapping. Claude's final host score
belongs to C3, OpenCode V1 to O3, and OpenCode V2 to O5. C1/C2/O1/O2/O4 own the
prerequisite package and setup evidence. The V1 and V2 negative floor rows move
to O2 and O4 respectively. The final V1 and V2 child leaves satisfy #1's distinct host-variant leaf gate.
The matrix must never imply that an ownership assignment is a live host PASS.

## Redistribution acceptance

1. Eight uniquely titled open children exist with the stated native parents,
   exactly one backplane:backlog label each, complete bounded issue contracts,
   and no premature implementation plan or readiness claim.
2. Native blocking edges match the sequences above. The #1 parentage and all
   existing #6 blockers remain unchanged.
3. #11 and #12 bodies describe aggregate continuity rather than one executable
   host leaf. Their labels and unrelated issue metadata survive.
4. The functional v0.1 specification points to this design only for revised
   issue ownership; its host and lifecycle requirements stay intact. The
   verification matrix names the actual new issue URLs and correct owners.
5. Fresh gh intake of #1, #6, #11, #12, and all eight children proves the graph,
   label cardinality, body headings, and unchanged pilot gate. Repository
   evidence records observed revisions and any deviation.
