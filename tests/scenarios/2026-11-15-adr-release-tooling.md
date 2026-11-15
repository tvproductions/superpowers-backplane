# ADR release tooling — partial maintenance checkpoint

Date: 2026-11-15. This is a preserved work checkpoint, not completed Task 2,
strict baseline acceptance, ADR integration or release readiness.

The approved ADR integration plan authorizes current-stable prerequisite
maintenance. The [read-only official inventory](2026-11-15-adr-release-tooling-before.json)
checked all 71 locked registry projects before modification. uv's owning upgrade
changed ten selections: uv 0.13.7 -> 0.13.8, Ruff 0.17.4 -> 0.17.5, ty 0.0.99 ->
0.0.104, Cosmic Ray 8.7.0 -> 8.9.0, coverage 7.17.2 -> 7.17.3, Lizard 1.25.1 ->
1.26.0, plus anybadge 1.16.0 -> 1.18.0, filelock 4.2.9 -> 4.2.10,
markdown-it-py 4.2.0 -> 4.3.0 and stevedore 5.9.1 -> 5.10.0. Other exact pins
are retained. uv lock --upgrade generated the lock; locked all-group sync and
all four routine pre-commit checks passed on managed Python 3.14.10. CI's uv
reference is 0.13.8; its Python and two pinned Actions remain current. The
minimum-only uv compatibility contract is unchanged. No product Python package
or consumer runtime requirement is introduced.

The actual installed Git-hook path was absent at inspection. The configured four
checks ran explicitly; this checkpoint does not claim an installed-hook proof.
Complete that acceptance observation before final integration/release. No hook
was disabled or bypassed. Deeper changed-tool compatibility, structured Cosmic
Ray worker outcomes, current advisory audit and complete A01-A18 reconciliation
remain required; passing routine checks do not substitute.

An isolated read-only Superpowers 7.0.2 source checkout resolves to
`22f0b463e7a5e579904dd6211a520321035526f7`. Existing installed upstreams and
project native activation were not changed. Four fresh native conformance
responses and source/input hashes are preserved in the companion archive below.
CLI exit zero is not a scored conformance verdict; full rubric scoring, five-check
acceptance, final native selections and the pre-authorship ADR checkpoint baseline
remain pending. Product ADR references have not been authored. Existing
SUPERPOWERS.md/native declarations retain their previous selections; do not claim
that an isolated candidate advances them.

Owner issue [#37](https://github.com/tvproductions/superpowers-backplane/issues/37)
was created under the approved exact intake payload, with one designing lifecycle
label. Last full intake observed at 2026-11-15T18:53:19Z; re-read before transitions.
The approved design/plan and separate real ADR-0001 approval remain intact.
No lifecycle transition, checkpoint schema change, CLI implementation, tag or
release occurs in this checkpoint. Backplane 0.3.0 remains the planned finite
ADR-integration minor from published 0.2.0.

Preserve original dirty checkout and this registered detached worktree. The
portable guidance owner has synchronized reviewed source at
`77ad2c792e0df39782271639c317e2c812b5a48e`, still unreleased while its current
OpenCode channel is unverified. Starter propagation and both publishers' release
acceptance remain separate. Continue the approved plan in order; do not invent
completion from this tooling checkpoint or start the separately planned CLI.

## Completed maintenance and conformance — resumed November 15

Current tooling/source prerequisite checks now pass; ADR behavioral baseline and
integration authorship remain next. Fresh native issue #37 intake still has its
unchanged 2026-11-15T18:53:19Z body, OPEN/designing, no children/blockers, complete
fifteen fields and identical approved bounded criteria. Designing permits this
preparatory maintenance; no execution eligibility or lifecycle transition is inferred.
The preserved actual ADR-0001 edition-1 approval hash still matches.

The 71 registry selections in current uv.lock exactly match the latest stable
targets in today's official PyPI inventory. Python remains managed 3.14.10; uv
0.13.8 meets the minimum-only rule. Live official stable CI Actions remain
checkout 7.0.1 and setup-uv 10.3.3 at their selected immutable SHAs. SP 7.0.2
release notes were reviewed: questionnaire/bootstrap/helper guards change, not
Backplane's native issue or checkpoint schema. The independent clean source is
22f0b463e7a5e579904dd6211a520321035526f7. Project-owned SP/gz-skills declarations
now select 7.0.2 / released 0.13.0; enablement and duplicate selections are unchanged.
The continuation worktree exposes its independent source at .agents/superpowers;
original checkouts, normal plugin caches and user settings were preserved.
No package/backend/product runtime exists; no fake distribution is introduced.

All five SP compatibility checks are scored PASS against the preserved four
native responses and exact existing rubrics:

| Check | Assertion-level assessment |
| --- | --- |
| skill-structure | Exact names and Use when descriptions, canonical entry points, required linked resources and real content pass existing public resource checks. |
| native-issue-intake | All six expectations pass: complete native fields, blocked/revision reconciliation, layered authority, one lifecycle, consumer verification ownership, accepted integration before closure. |
| language-neutral-verification | All five pass: only cargo test --workspace, no Python workflow, native graph/revisions, upstream execution/review, no premature closure. |
| lifecycle-transitions | Every listed expectation passes: dual-label detection/repair, security preservation, review-to-active, explicit blocked resume target, revalidation, atomic transitions and post-write checks. |
| superpowers-installation | Every listed expectation passes: rejects lookalike/dirty/incomplete sibling without mutation, authoritative unused destination/stable source, complete preflight/discovery, separate update authority, no consumer runtime/Project/IssueOps requirement. |

Fresh Codex 0.169.0 discovery separately reads independent SP using-superpowers,
brainstorming, writing-plans and writing-skills plus both Backplane entry points,
resolving 7.0.2 and unchanged Backplane 5904713. Actual model identity is UNKNOWN;
observed scope is Windows Codex. This is discovery/conformance evidence, not ADR
integration behavior or normal-profile native installation proof. Existing raw
four-case captures remain in 2026-11-15-adr-tooling-captures.zip; new discovery,
current audit and structured changed-tool evidence are in the companion archive.

Changed-tool compatibility is measured, not inferred from versions:

- Reconstructed the exact hash-verified retained helper/test fixture from the
  November 7 structured receipt. Only the absolute project path in its existing
  Cosmic Ray configuration changed. Helper function ASTs match current guides.
- Coverage 7.17.3: all eleven retained behavior tests pass; 42/42 statements and
  14/14 branches, no exclusions or missing branches.
- Lizard 1.26.0: seven functions, max 10, test-module mean 3.2, helper-module mean
  8 and overall 4.5714, all below ceiling 20.
- Cosmic Ray 8.9.0: 135 structured NORMAL workers, 128 KILLED, seven SURVIVED;
  every exact survivor diff matches the previously independently reviewed
  equivalent/JSON-whitespace disposition. No tool error or timeout. Coverage's
  actual passing baseline and retained worker records supplement CLI exit status.
- Current locked hashed-export pip-audit: 71 packages, zero known vulnerabilities
  and zero skipped registry packages. Task-local cache avoids the previously
  observed host cache boundary. Generic hash advice is retained as a warning.

Unchanged static analyzer and independent manual cognitive evidence retain only
their exact original source/AST scope; no shared cognitive engine is installed or
qualified. Current source is the same seven-function corpus. Python 3.14's newer
concurrency/templates/introspection APIs offer no demonstrated gain for these
small helpers; retain explicit paths/encodings and shell-free process boundaries.
No consumer Python requirement or additional analyzer framework is added.

A01/A04-A08/A10/A17 retain actual root/config/managed-runtime/tool/lock/dependency
proof; A09's inspected absent shared pre-commit hook is now installed using the
project's pinned pre-commit, preserving all four configured checks. Its real
execution is observed at the maintenance commit. A02/A03/A11-A16 retain the
reasoned non-package/non-library/non-workspace/public-source/non-deployment N/A
scope. A18 has current changed-tool/audit proof and explicitly bounded unchanged
source evidence. Exact final integration CI remains T5's gate, not inferred from
prior 5904713 CI. Full ADR/release/native-combination acceptance remains unfinished.
