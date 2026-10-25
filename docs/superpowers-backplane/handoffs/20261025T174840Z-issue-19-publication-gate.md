# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-10-25T17:48:40.183514+00:00. Evidence: UTC clock at CREATE.
- Repository identity: VERIFIED — standalone `U:/repos/agents/superpowers-backplane`, origin `https://github.com/tvproductions/superpowers-backplane.git`. Evidence: guarded Git root/origin and canonical containment.
- Branch: VERIFIED — `recovery/issue-19-windows`. Evidence: current Git probe.
- HEAD: VERIFIED — `157d6dfc21afb56c60efe5b2d543f8a8229ef1a1` before handoff storage. Evidence: Git HEAD; storage/transport commits are distinct.
- Incoming purpose: VERIFIED — finish #19 through #34's PR/integration gate, then whole-change review and integrated closeout; preserve progress across the context boundary. Evidence: selected #19 work and operator handoff/sync request.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/19 OPEN/active, revision `2026-10-25T16:21:35Z`; fixture #34 OPEN/blocked, revision `2026-10-25T17:07:58Z`. Evidence: fresh full native intake.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` blob `a790d953691d178f711757e9164afb60932eb65a`; `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: current tracked objects.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-10-24-issue-19-claude-lifecycle-recovery.md` blob `9f8d251b13067da3ed9ae3d893fbc7a7bad5a850`. Fixture plan is on `test/issue-19-doc-lifecycle`, blob `6b33d68ad02066e2a1dfd576235b890e3a5267cf`, at reviewed head `22c5b8d917a09f275c23d99bd9c9645d6c1d2e35`; it is absent from the recovery working tree until incorporation. Evidence: tracked Git objects.
- Superpowers derivation provenance: VERIFIED — independent clean v7.0.1 at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`; active advertised discovery junction and actual skill reads succeed. Sources: `.agents/skills/superpowers/using-superpowers/SKILL.md` SHA-256 `82c5c8866ad7f5dd4440ce66bd7806ba48a2f13771beae5cf112e53f08fe36ba`; `.agents/skills/superpowers/brainstorming/SKILL.md` SHA-256 `61a7ef918652108c76a3fd01e02dd92d39996c6b46d4cb2819cbd03f6c45e46a`; `.agents/skills/superpowers/writing-plans/SKILL.md` SHA-256 `a6c67c1900064347c2a329990dd3c555657c51c3ec53b259a08aa01a2c26139a`; `.agents/skills/superpowers/executing-plans/SKILL.md` SHA-256 `e4649e59880ef2643d1da128e3d607e87e3f969410d72095a5bf65811b6036dc`. Current upstream README installation guidance was retrieved and decoded through gh; it documents separate harness installation. Fresh Claude verification passed; fresh Codex model verification is unverified.
- Predecessors: VERIFIED — known issue-19 and context lineage paths below exist and canonically resolve in this repository; this confirms their availability, not every underlying historical claim. Evidence: containment/existence probes.
- `docs/superpowers/handoffs/20260927T165620Z-issue-19-claude-lifecycle-plan-review.md`
- `docs/superpowers/handoffs/20260920T202021Z-post-issue-18-claude-setup-continuation.md`
- `docs/superpowers/handoffs/20260920T160331Z-post-issue-17-host-continuation.md`
- `docs/superpowers/handoffs/20260920T015816Z-remaining-host-installation-leaves.md`
- `docs/superpowers-backplane/handoffs/20261024T225444Z-adoption-readiness-after-issue-31.md`
- `docs/superpowers-backplane/handoffs/20261014T084025Z-issue-31-assessment-and-prompt-preference.md`
- `docs/superpowers-backplane/handoffs/20261014T080251Z-issue-31-remote-satisfaction.md`
- `docs/superpowers/handoffs/20261011T172308Z-github-fdau-scope-discussion.md`
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261025T174840Z-issue-19-publication-gate.md`, project-owned namespace override. Evidence: canonical parent checks, exclusive creation and immediate recheck.

## Incoming purpose

VERIFIED — Continue the selected #19 implementation at its remaining integration gates. Evidence: current plan, native issues and committed execution summaries. Do not restart completed tests, select a different backlog item, merge the update-version fixture, or release from this handoff.

## Authority anchors

VERIFIED — Current AGENTS, SUPERPOWERS, native issues and approved design/plan govern; this handoff advises rather than authorizes. Evidence: current reads and issue intake. The latest operator request authorizes handoff plus bidirectional Git sync of the owned recovery/fixture artifacts; PR integration and release were not approved by that request.

## Verified current state

VERIFIED — The recovery checkpoint is `157d6dfc21afb56c60efe5b2d543f8a8229ef1a1`; reviewed fixture head is `22c5b8d917a09f275c23d99bd9c9645d6c1d2e35`, tree `13a0093f73eadbdb9abbb2db409f2b2100f5ab5e`. Origin main is `b0d702f8821d6d29184118410ec6ff2d8fb63438` after fresh fetch. Evidence: current Git probes and recorded native main check. No PR or Backplane release was observed.

VERIFIED — #19 baseline/preflight, native package lifecycle and all five named conformance checks pass in recorded Windows Claude scope. Separate 7.0.1 verification scored 23/23 behavioral expectations, nine exact Python lifecycle blocks, ten snapshots and five actual discovery sessions; B is restored. Evidence: `tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.{md,json}` and its transcript. Earlier 7.0.0 evidence remains at its original identity.

VERIFIED — #34 has actual status/selection zero-mutation evidence, designing/ready/active, review-to-rework and blocked transitions. One real Important paragraph finding was fixed and the same independent fixture reviewer accepted it. Evidence: `tests/scenarios/2026-10-25-issue-19-live-fixture.json` and transcript. Resume, actual PR integration and verified closure remain pending; fixture review is not whole-#19 review.

## Live implementation thread

VERIFIED — B is `b0d702f8821d6d29184118410ec6ff2d8fb63438`; F is test-only `5e01704fcdda13eefeeac52d8892da26e7164ffd`. Do not merge/tag/release F's version/README marker. Real guide, policy and evidence changes are intended release content. Evidence: approved recovery plan and exact source receipts.

VERIFIED — The useful fixture changes only one guide paragraph and its issue-bound plan. Its correction requires installed commit/version/hash matches to the selected immutable source and treats mismatches as failure. Evidence: reviewed fixture head and native review transcript. Its PR/integration is the next concrete gate; the broader #19 recovery still needs incorporation, affected final-guide checks and fresh whole-change review.

## Corrections to durable artifacts

VERIFIED — Operator-directed Python/Astral policy is recorded in AGENTS: portable Python orchestration through uv, Ruff, ty; consumer workflows remain language-neutral; the existing test-framework prohibition remains. PowerShell is only an adapter for unchanged legacy guide examples. Evidence: commit `da7b8e6` and current AGENTS. Historical PowerShell scratch is retired.

VERIFIED — The old Mac recovery paths and draft status are historical; current authorized root is the supplied Windows repository, with native bookkeeping under `.sp-bp/work/issue-19/`. Explicit 7.0.1 maintenance supersedes the earlier preserve-7.0.0 ruling for future execution only. Evidence: current operator directions, committed continuation summary and maintenance record.

## Decisions and provenance

VERIFIED — The operator approved the conformance payload and exact documentation fixture creation/exercise, then explicitly requested 7.0.1 maintenance, and now handoff/Git sync. Evidence: this session's explicit replies. Do not infer tag/release or PR merge approval from sync.

VERIFIED — GitHub operations use gh; necessary Git transport uses the gh credential helper with process-only settings. No persistent credential/configuration change or credential copying was performed. Evidence: observed fetch/update commands. The new sync should publish exact existing commits, not reconstruct different commits through the earlier unexecuted gh Git Data proposal.

## Negative results

VERIFIED — Native Backplane update initially attempted SSH and failed publickey authentication; B and protected state survived. Repository-specific child-only HTTPS rewrite corrected the update. Evidence: lifecycle transcripts. Do not repeat unsupported SSH transport without new authentication evidence.

VERIFIED — PowerShell timestamp conversion, colon filenames and JSON property-order comparison caused orchestration failures; Python replaced the harness. The 7.0.1 initializer initially used an older pre-reinstall timestamp anchor, then proved preservation using the immediately preceding snapshot. Evidence: continuation and maintenance records. Do not treat these intermediate failures as current package defects or rerun obsolete scratch helpers.

VERIFIED — Automatic approval review rejected an optional additional fresh Codex skill-text transfer before execution. No bypass or retry occurred. Evidence: this session's tool rejection and maintenance record. Do not run that extra external transfer without its explicit approval; already approved Claude results remain separately scoped.

## Deferred obligations

VERIFIED — #34's resume/integration/closure and #19's final whole-change review, target verification and closeout remain incomplete. #11 remains separately gated by #19. Licensing #4, self-hosting #5, OpenCode #20–24/#12, external pilot #6 and release #7 remain separate backlog work. Evidence: current native intake. The release parent has 5/17 completed children; no next issue is selected by priority policy.

## Risks and unknowns

UNVERIFIED — Remote arrival of this new handoff storage commit and the two newly synced branch tips is pending at CREATE. Required probe: after authorized push, compare both gh branch refs to local full SHAs and the remote handoff blob to its tracked blob; verify again on RESUME.

UNVERIFIED — The disposable authenticated Claude profile and ignored scratch are host-local, not transported. Required probe: on the receiving host, explicitly scope profile authentication/inventory and provenance; never copy credentials or fall back to a normal profile. Captured portable helper source is `tests/scenarios/transcripts/2026-10-25-issue-19-python-harness-source.md`, untracked at CREATE with SHA-256 `57a33fcc51dfee0c6da36f014eaf96e9d477c3fb13524bf00aadf6a209f05ee6`; it is included in this authorized sync. Rehydrate only needed helpers, and preserve old evidence/output phases.

UNVERIFIED — Fresh Codex model discovery, other hosts/harnesses, complete-stack and release acceptance are not established by the Windows Claude results. Required probe: their separately authorized applicable checks. No missing historical pass is inferred.

## Proposed next steps

INFERRED — Resume against this exact handoff; verify current origin/root, published recovery/fixture refs, issue semantics, 7.0.1 source and profile prerequisites first. Evidence and reasoning: context boundary and mutable external state require reconciliation, not repeated implementation.

INFERRED — After sync, reconcile #34's local-only artifact paragraph to the now-published immutable fixture plan while preserving native graph/labels/scope, within an authorized backlog operation. Obtain the still-pending PR/integration decision; sync authorization alone does not release the integration blocker. Then use the existing published fixture branch for gh PR creation, resume active only after its real release condition holds, verify integrated bytes and close #34. Evidence and reasoning: reviewed contribution exists but main integration does not.

INFERRED — Incorporate the verified fixture contribution into recovery, rerun affected final-guide seams with 7.0.1, obtain the one fresh whole-#19 review and complete authorized integration/verification/closeout. Only then assess #11 or other dependency-clear planning candidates; do not release until #7's gates hold. Evidence and reasoning: approved plan and current native graph.

## Suggested skills

VERIFIED — Available and purpose-relevant: `superpowers-backplane:managing-superpowers-handoffs` RESUME, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:executing-plans`, `superpowers:requesting-code-review`, and `superpowers:verification-before-completion`. Evidence: advertised inventory and actual source reads. Use only procedures needed for the current step; administrative sync needs no full implementation workflow.

## Resume instruction

VERIFIED — Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261025T174840Z-issue-19-publication-gate.md` before selecting the next action. Evidence: this append-only artifact and its explicit incoming purpose.
