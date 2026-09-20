# Host Installation Leaf Rescoping Design

- **Status:** Revised draft after plan review; written approval pending.
- **Scope:** Issues #11 and #12, eight new implementation leaves, and verification ownership.
- **Functional authority:** docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md.
- **Observed issue revisions:** #11 2026-09-19T14:11:46Z; #12 2026-09-19T14:11:57Z; pilot #6 2026-08-23T13:55:24Z.

## Problem and decision

Issue #3 bundled packaging, setup modes, failure handling, lifecycle operations,
conformance, and integration. #11 repeats that scope for Claude Code and #12
adds two OpenCode variants. The work needs smaller review and verification
boundaries without weakening the approved v0.1 host contract.

Keep #11 and #12 as executable final acceptance leaves under release parent #1.
Create eight sibling implementation leaves under #1. Native blockers put the
smaller work before its host acceptance leaf. This preserves the existing
backplane:ready-to-active and backplane:review-to-completed path for #11 and
#12; making them non-executable parents would conflict with the current issue
contract's leaf eligibility and completion transitions. Pilot #6 continues to
be blocked by #11 and #12.

## Functional invariants

- The canonical Backplane skill text stays in root skills/. Host metadata and
  the one shared OpenCode adapter point there. Do not copy Backplane or upstream
  Superpowers skill text.
- Upstream Superpowers remains a separate installation with its own update and
  removal path. The active host's documented stable channel governs acquisition
  when upstream is absent; the default branch is an explicit edge choice.
- Claude Code, OpenCode V1 1.18.29+, and OpenCode V2 2.0.4+ retain fresh
  three-skill discovery, provenance, gh preflight, preservation, clean and
  repeat install, setup, update, rollback, Backplane-only uninstall, all five
  named conformance checks, and authorized issue-state scenarios.
- V1 below 1.18.29 and V2 below 2.0.4 remain unsupported negative cases.
- Host authentication is a prerequisite for live checks. An absent session
  blocks that check; do not retry sign-in repeatedly or borrow user credentials.
- No host implementation, upstream update, external pilot, release, extra
  harness, project runtime, GitHub Project, or IssueOps system is part of the
  redistribution itself.

## Native issue graph

Every new issue below is a child of #1 and starts with exactly one
backplane:backlog label. Titles are unique creation keys. Their issue bodies
hold bounded scope and observable acceptance; native links own parentage and
blocking relationships.

| Key | Exact new issue title | Reviewable output |
|---|---|---|
| C1 | Package and document Claude Code plugin installation | Native manifest and marketplace point to canonical skills; pinned install guide and one disposable clean-install/fresh-discovery smoke run with compatible preinstalled upstream. |
| C2 | Verify Claude Code setup and upstream adoption | Native package, sibling checkout, and absent-upstream setup; provenance, gh capability, fresh discovery, and unknown/versionless/duplicate/dirty/conflict preservation. |
| C3 | Verify Claude Code lifecycle and conformance | Repeat install, pinned update and rollback, Backplane-only uninstall, verified guide commands, per-operation preservation, five checks, and authorized issue-state scenarios from the installed package. |
| O1 | Build and document the shared OpenCode V1/V2 adapter | One entry point and guide for V1 plugin and V2 plugins configuration; basic discovery smoke on both supported variants with compatible preinstalled upstream. |
| O2 | Verify OpenCode V1 setup and compatibility failures | V1 1.18.29+ upstream modes, provenance and gh preflight, fresh discovery, failure preservation, and below-floor rejection. |
| O3 | Verify OpenCode V1 lifecycle and conformance | V1 repeat install, pinned update/rollback/uninstall guide replay, per-operation preservation, five checks, and authorized issue-state scenarios. |
| O4 | Verify OpenCode V2 setup and compatibility failures | V2 2.0.4+ upstream modes, provenance and gh preflight, fresh discovery, failure preservation, and below-floor rejection. |
| O5 | Verify OpenCode V2 lifecycle and conformance | V2 repeat install, pinned update/rollback/uninstall guide replay, per-operation preservation, five checks, and authorized issue-state scenarios. |

C1 and O1 provide package and guide scaffolding, with no unverified lifecycle
claim. C2, O2, and O4 own setup and compatibility failures. C3, O3, and O5
own lifecycle and conformance on the installed candidate. Reuse earlier
evidence only while its package, guide, host, and upstream inputs remain
unchanged; rerun the affected seam after a relevant change.

## Dependencies and final leaves

- C1 blocks C2, C2 blocks C3, and C3 blocks #11.
- O1 blocks O2 and O4; O2 blocks O3; O4 blocks O5; O3 and O5 block #12.
  V1 and V2 may progress independently after O1.
- Keep #11 and #12 as children of #1, keep their historical blocker #2,
  and keep their outgoing pilot blocker edges to #6. Do not add duplicate
  #6 edges from every new sibling.
- Narrow #11 to final Claude Code integrated acceptance: C1-C3 closed as
  completed, every mandatory installed-package check PASS, required evidence
  reachable from integrated source, and a current plan for #11. An unresolved
  FAIL or UNKNOWN blocks acceptance.
- Narrow #12 to final OpenCode acceptance: O1-O5 closed as completed, every
  mandatory V1 and V2 check PASS, both below-floor cases producing the
  expected unsupported result, evidence reachable from integrated source,
  and a current plan for #12. An unresolved FAIL or UNKNOWN blocks acceptance.
- #11/#12 stay at backplane:backlog during this redistribution. Each new leaf
  also remains backlog until its own design authority and current plan are
  approved. No issue is selected, marked ready, or closed in this rescope.

The full Claude, V1, and V2 matrices are satisfied across their prerequisite
leaves and final host acceptance leaves. A final leaf verifies integration and
evidence consistency; it need not repeat an unchanged live test. It reruns any
test whose relevant input changed after that test's child closed.

## Verification ownership and documentation

The existing v0.1 specification remains functional authority. Revise only
its implementation ownership sentences after the native graph exists;
preserve issue #2's completion contract and the no-publication rule. In
tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md, revise the
Required checks introduction for collective prerequisite ownership and final
acceptance. Move the original #11/#12 assignment and GREEN observations under
a dated historical heading, then make one current owner table authoritative.
Claude final acceptance remains #11, OpenCode V1 and V2 prerequisite evidence
lives at O2/O3 and O4/O5, and final cross-variant acceptance remains #12.
V1 and V2 negative floor cases belong to O2 and O4. Correct the historical
statement that #3 is open; #3 is closed/completed. An ownership assignment
is not a passing live host run.

## Redistribution acceptance

1. Eight unique new issues exist under native parent #1 with complete issue
   contracts, one backlog label each, and no premature plan/readiness claim.
2. The native blocker graph matches the sequences above; #11 and #12 remain
   executable leaves, still block #6, and retain unrelated labels and fields.
3. The revised #11/#12 bodies specify narrow final acceptance rather than
   repeating their prerequisite implementation work.
4. The approved functional specification and current ownership matrix agree
   with the live graph without losing any host or failure requirement.
5. Fresh gh intake of #1, #6, #11, #12, and the eight new issues proves
   parentage, blockers, labels, body headings, and the unchanged pilot gate.
