# Backplane release policy binding

## Authority

The operator designated
[gz-skills-first-starter](https://github.com/tvproductions/gz-skills-first-starter)
as the authoritative shared engineering and release policy alignment source.
Its [versioning policy](https://github.com/tvproductions/gz-skills-first-starter/blob/main/docs/versioning.md)
owns SemVer classification, 0.x treatment, coherent minor-release bundles,
compatible patches, newly written PRDs for every major including 1.0.0,
independent component versions and immutable release identities.
This document binds that source to this repository; it is not a competing policy.

Apply the rules prospectively to Backplane's own releases, including a newly
written PRD for 1.0.0. Preserve the existing issue-bound acceptance authorities,
host verification, external pilot and release gates. A closed issue or merged PR
does not authorize publication. A source policy binding establishes neither
release readiness nor implementation of the proposed release-monitoring system.

The source's engineering guidance must be checked for applicability during
scoped maintenance. This release-policy alignment does not certify broader
Python/tooling conformance or authorize dependency/runtime changes.
Local departures require evidence, maintainer approval, an owner and dated revisit.

## Check in with the source

Before release preparation, during scoped policy/tooling maintenance, and when
notified of relevant starter changes:

1. Read the canonical starter's current versioning policy, changelog and relevant
   baseline/engineering guidance. Resolve and record the exact source revision;
   distinguish published release policy from unreleased development guidance.
2. Compare with the previous reviewed source and this repository's instructions,
   release documents and applicable acceptance evidence. Record the date, paths,
   source SHA, applicability, differences and adopt/defer decisions in the
   existing release or handoff record.
3. Reconcile applicable differences before claiming consistency. An unavailable
   source or unresolved difference remains an explicit gap. Record approved
   exceptions with evidence, owner and dated revisit; local silence is no waiver.
4. Recheck final source identity before a published-alignment claim. For an
   operator-authorized working-tree review, record the base SHA plus content
   hashes, and identify the edits as uncommitted/unreleased.

This is an on-demand responsibility, not an automatic schedule or an automatic
update. Independent versions and release dates remain independent.

## Workflow boundary

[Backplane owns lite/heavy definitions](https://github.com/tvproductions/superpowers-backplane/blob/main/docs/superpowers-backplane/modes.md),
requirements tracking, labeling, backlog/release monitoring and handoffs.
Superpowers owns feature development. gz-skills provides portable procedures,
including release preparation/publication verification and handoff primitives,
beneath the active project workflow; it does not become the lifecycle owner.

Do not bootstrap the starter bundle into either companion repository. Policy
flows from the starter to repository bindings; workflow ownership does not
create a reverse policy dependency. Shipped skills remain usable by unrelated
projects under those projects' own policy. No blanket consumer PRD, Python,
tooling or installation requirement follows from this repository's alignment.

## Initial local review — October 26, 2026

The reviewed starter is development version 0.7.0, with base commit
`eef2e858bba709988eb859b17739d2989d8825ab` plus the operator-authorized
working-tree policy changes. The base commit alone does not contain this binding.
Source inputs: `docs/versioning.md`, `docs/baseline-policy.md`,
`docs/architecture.md`, `templates/AGENTS.skills-first.md` and `CHANGELOG.md`.
The exact edited input hashes are recorded below.

Adopted: source authority, SemVer/release planning and prospective major PRDs,
source consistency checks, and Backplane ownership of modes/product continuity.
No release-policy exception is taken. Broader engineering conformance, end-to-end
mode readiness, remote publication and installed discovery are not established
by this documentation review. Reconcile the final committed source before the
next release preparation. No shipped skill, version pin, tag or release is changed.

| Source path | SHA-256 of reviewed working-tree content |
| --- | --- |
| docs/versioning.md | d2a293779e80811c08f1311c8bf54961abe9f1638967ed6a71b3babe4a0d54eb |
| docs/baseline-policy.md | fcb2ae18dc19f80043709286270ea200bc17721b89a5e484c9e24f255738b660 |
| docs/architecture.md | 645a929b00bbfaaf0f7ef4e188e936e44682f1989ddccb21228374ce824663b0 |
| templates/AGENTS.skills-first.md | 4cd3bf70359a5e888a317a28232be86cf0233af423f5bc413a426fdcffa86322 |
| CHANGELOG.md | 515f78f591d2326205619da9352e45f02002593f8c2208729c29bfd71ff4d8b0 |

## Committed source reconciliation — October 26, 2026

The operator authorized Git synchronization of all three repositories. The
reviewed source policy is now committed and verified on the starter's remote main
at [`35ac0578dab0c7b603a9545d9b6b630ee006e551`](https://github.com/tvproductions/gz-skills-first-starter/commit/35ac0578dab0c7b603a9545d9b6b630ee006e551).
The five policy inputs above retain their recorded hashes in that commit;
the initial working-tree review is reconciled to this immutable source identity.
Development version 0.7.0 remains unreleased. This record verifies source-policy
alignment; release acceptance, installation and native readiness remain separate.

## Source review and tooling refresh — October 31, 2026

Reviewed starter main at
[`fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281`](https://github.com/tvproductions/gz-skills-first-starter/commit/fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281),
rechecked unchanged after review. The latest published starter is `v0.7.1`,
whose annotated tag resolves to `27594dbaec853e6bde037b0aaf3f0427a3f053f9`.
This supersedes the earlier source's unreleased-version observation without
rewriting its historical evidence. Reviewed versioning, baseline, architecture,
adopter guidance, Python policy and changelog, including the diff from the
previous reviewed source. Input hashes and verification are in the
[tooling refresh receipt](../tests/scenarios/2026-10-31-tooling-refresh.json)
and [report](../tests/scenarios/2026-10-31-tooling-refresh.md).

The SemVer, coherent minor bundles, prospective major PRDs and Backplane-owned
mode/lifecycle authorities remain consistent. The source now permits scheduled
scans and reviewed update PRs, leaving adoption and timing to each project.
No schedule or scanning service is selected here. Starter-specific cognitive
engine exceptions do not become Backplane exceptions or acceptance evidence.

The new direct Git/gh guidance is unreleased at the reviewed main revision;
adopt it explicitly in AGENTS.md while retaining Backplane's existing
`uv run --no-project python` execution command. The starter's locked-project
command does not apply to this repository, which has no Python package project
or lock. This preserves the existing Backplane-owned runtime decision rather
than adopting the starter bundle or claiming formal conformance.

The operator authorized updating the assessed tooling: keep the approved Python
3.14 family, advance its exact pin to 3.14.10 and provision the ignored local
environment with Ruff 0.17.3 and ty 0.0.95. No new release-policy exception is
taken. No source package, consumer runtime requirement, plugin revision or
release is changed. Retain newer-family Python 3.15 as a separate compatibility
decision. Record current guide-format findings separately from runtime and
manifest validation; this maintenance does not repeat historical host acceptance.

## Bounded release-scope review — November 7, 2026

The operator requested a comparison of the existing four-host first release
with a Codex/Claude initial bundle and later OpenCode minor. The
[proposal](superpowers-backplane/specs/2026-11-07-release-scope-review.md) records
the assessed scope, evidence gaps, proposed obligation transfers, conditional
window and manual review cadence. Scope changes and the cadence remain proposed;
this source review does not approve or publish them.

Reviewed canonical starter main
[`8d090f88bf45b9a755808a62c1445beeb005daff`](https://github.com/tvproductions/gz-skills-first-starter/commit/8d090f88bf45b9a755808a62c1445beeb005daff)
against prior review `fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281`.
Published `v0.8.0` resolves to `e0b752fcc13b87ec7868fe0b0f85badefdb6bf52`;
reviewed main is one commit later, containing unreleased Windows scope-fix work.
The versioning, changelog, baseline, architecture and Python-engineering input
blob identities are in the
[review receipt](../tests/scenarios/2026-11-07-release-scope-review.json).

Applicable release guidance explicitly identifies 0.1.0 as the first substantive
public commitment. Existing untagged work therefore belongs in the initial
bundle; supported OpenCode adoption after that baseline would be a minor
addition. Coherent bundles, compatible patches, new major PRDs and independent
versions remain consistent with this binding. No policy exception is proposed.

The source also strengthens adopter activation-scope guidance. Reconcile native
installation/update preservation with the selected tuple during #4 acceptance;
do not certify that evidence from this document review. Starter implementation
changes and its Python-only adopter baseline are not adopted into Backplane or
its consumers. Existing project tooling and consumer language neutrality remain
authoritative. Full release-specific freshness, engineering applicability and
exact-candidate qualification remain outstanding. No runtime/plugin update,
formal starter conformance, new automatic schedule or release authorization is
implied. Recheck the source before final release alignment claims.

## Independent Python family alignment — November 7, 2026

The maintainer explicitly directed fixing alignment across the three repositories
and reaffirmed the current rule: Python 3.14 unless X-Plane/XPPython3-bound,
then supported 3.12. Reviewed starter authority is
`4f8bb09633655473cd6aab9e1ddc60963c487bb1`, especially baseline/Python policy,
versioning, AGENTS and the gz-skills workflow mapping. Its Python-family rule
is distinct from the new minimum-only uv compatibility requirement.

Backplane independently owns its ordinary Python tooling choice: 3.14, exact
managed 3.14.10. No XPPython3 exception applies to Backplane itself. Its own
AGENTS establishes this without circular starter adoption. The independent
strict-Astral tooling metadata remains separate pending work in this checkout.
Portable workflows, including gz-skills, consume that policy and do not supply an alternative runtime or tool baseline. Consuming
projects remain language-neutral and retain their own approved standards.

The existing strict Astral reconciliation is separate, already-changing work;
this authority correction preserves its files and acceptance gaps. The earlier
no-project commands describe the committed baseline; the separate pending
reconciliation supplies locked commands in this worktree. This narrow save point
does not publish that tooling migration. Keep unverified evidence explicit.
No installed cache, plugin,
GitHub issue, tag, release or independent source revision is changed here.

The maintainer subsequently authorized ordinary Git synchronization. The exact
committed starter source is `a483e382146c6082e590e31494c07d1812645014`,
verified on its origin/main. This narrow save point publishes only the independent Python-authority clarification and
receipt; separate release-scope and strict-Astral changes remain in the worktree.
The committed tree has no project quality CI; a pending workflow is not hosted
execution evidence. No release, native install or broader acceptance is implied.

See [the scoped authority receipt](../tests/scenarios/2026-11-07-python-policy-authority.md).

## Discussion save point after v0.2.0 — November 7, 2026

The bounded scope review above predates the maintainer-selected, published
v0.2.0 engineering release. Its proposed 0.1.0/0.2.0 host allocation and dates
remain historical planning inputs, not current publication status or completed
native scope transfers. Read the [verified publication receipt](../tests/scenarios/2026-11-07-v0.2.0-publication.md)
for the actual first release and its explicit version-policy decision.

The [release-doctrine discussion](superpowers-backplane/specs/2026-11-07-release-doctrine-alignment-design.md)
is saved for reappraisal; publication of the document does not activate the
proposed ownership transfer or starter enforcement. Its earlier incomplete
Astral checkpoint is historical: the separate [full acceptance](../tests/scenarios/2026-11-07-strict-astral-full-verification.md)
and v0.2.0 publication supersede that prerequisite's status. Current engineering
compliance does not implement the remaining release doctrine. The design's
current discussion-3 identity and earlier gap-review-2 receipt remain distinct.
