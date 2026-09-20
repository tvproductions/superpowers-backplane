# Session handoff

- Format: superpowers-backplane-handoff/v1
- Creation time: VERIFIED — 2026-09-20T20:20:21Z. Evidence: UTC clock observed during CREATE.
- Repository identity: VERIFIED — https://github.com/tvproductions/superpowers-backplane.git, with the standalone repository root verified by git rev-parse --show-toplevel. Evidence: git remote get-url origin and git rev-parse --show-toplevel.
- Branch: VERIFIED — main. Evidence: git branch --show-current.
- HEAD: VERIFIED — 4a06e1606b20555c3261e0fd3420aab9fc9628a9 before CREATE. Evidence: git rev-parse HEAD and clean git status.
- Incoming purpose: VERIFIED — reconcile completed Claude Code setup issue #18, then orient the next session without assuming a successor was selected. Evidence: the operator requested a fresh handoff and Git sync after #18 closure.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/18, CLOSED/COMPLETED, updatedAt 2026-09-20T20:07:23Z; successor #19 is OPEN/backplane:backlog at updatedAt 2026-09-20T01:29:21Z and is not selected. Evidence: complete native gh issue view intake and operator conversation.
- Specification: VERIFIED — docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md at tracked blob a790d953691d178f711757e9164afb60932eb65a; docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md at tracked blob e1e42d0b89bf950b988b05097dd011c6490aefe6. Evidence: git ls-files -s.
- Plan: VERIFIED — completed #18 plan docs/superpowers/plans/2026-09-20-claude-code-setup-and-upstream-adoption.md at tracked blob e77d53b3261f7b499fadcd6f51f197c6dda9e15a; #19 has no plan in its current issue body. Evidence: git ls-files -s and complete #19 intake.
- Superpowers derivation provenance: VERIFIED — active Codex skill catalog and .agents/skills/superpowers junction expose the clean obra/superpowers checkout at 5bf4e78011075bcfc0dc295f0724994cd123ee71. Inspected superpowers:using-superpowers at .agents/superpowers/skills/using-superpowers/SKILL.md, SHA-256 82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA; superpowers:brainstorming at .agents/superpowers/skills/brainstorming/SKILL.md, SHA-256 A32D2255354775AA124855AA7100CF276BEA096FFF4EBB3A0EDF57BE216E6C72; superpowers:writing-plans at .agents/superpowers/skills/writing-plans/SKILL.md, SHA-256 0BC3D36590F7B2C323ED3EC18FF77E9F8ED57AF42F5680A02B11A2D20DE265CF; superpowers:executing-plans at .agents/superpowers/skills/executing-plans/SKILL.md, SHA-256 F38E8F2DDCF079F65493ADC713C1FED78421DFAF5F4DBF6B3A6B2B1D95466E71. Evidence: active discovery path, installed skill reads, Get-FileHash, upstream checkout Git identity and status, and current upstream README installation section retrieved through gh (README blob cf80400690849b37861f39d396d231ea89ac693b).
- Predecessors: VERIFIED — docs/superpowers/handoffs/20260920T160331Z-post-issue-17-host-continuation.md at tracked blob af51bb57f615b23192a9585adf70856459d53256, then its predecessor docs/superpowers/handoffs/20260920T015816Z-remaining-host-installation-leaves.md at tracked blob 3049d51a94992525b2c673ccae2a600e20a8ceca. Evidence: inspected identity blocks, canonical path containment, and git ls-files -s.
- Storage location: VERIFIED — docs/superpowers/handoffs/20260920T202021Z-post-issue-18-claude-setup-continuation.md, a project-local append-only artifact. Evidence: canonical parent containment, ancestor reparse checks, collision check, and exclusive CreateNew write.

## Incoming purpose

VERIFIED — Start from #18's integrated and closed state, explain its limited scope clearly, and reconcile any proposed next issue against current authority before work begins. Evidence: operator request and current native issue intake.

## Authority anchors

VERIFIED — AGENTS.md at blob 154a3dce1f4b18c77f944cab2ede362b17b8ead0, HANDOFF.md at blob 56132e0dbe45bc9402d38cc79eabf4c77b003c94, SUPERPOWERS.md at blob f8f9790da406c3a4fdc18ff27cfae9bf92a1b861, the specification and plan identities above, and live GitHub issue fields govern continuation. Evidence: git ls-files -s, inspected project instructions, and native issue intake. This handoff is advisory.

VERIFIED — #18 is the completed work item; #19 owns Claude Code lifecycle and conformance, and #11 owns final integrated Claude Code acceptance. Evidence: current #18, #19, and #11 bodies and native dependency edges.

## Verified current state

VERIFIED — Before CREATE, local main and published origin main both resolved to 4a06e1606b20555c3261e0fd3420aab9fc9628a9; the worktree was clean with zero ahead and behind commits. Evidence: git status, git rev-parse HEAD, git ls-remote origin refs/heads/main, and git rev-list counts.

VERIFIED — #18 is CLOSED/COMPLETED with no lifecycle label and no linked closing pull request. #19 is OPEN/backplane:backlog with closed blocker #18; #11 is OPEN/backplane:backlog and remains blocked by #19. Evidence: complete native gh issue view intake.

VERIFIED — Published tests/scenarios/2026-09-20-claude-code-setup.md at tracked blob 15bdae55b28116a6a1292ada53b3d3fd6edecd19 records three supported setup modes and twelve failure rows as PASS. Its issue-state snapshot is dated to execution before closure. Evidence: git ls-files -s and inspected scenario acceptance crosswalk.

## Live implementation thread

VERIFIED — The operator authorized publishing #18 work and closing #18, then asked for a fresh handoff and Git sync. No next issue was selected in this request. Evidence: conversation and current #18 state.

VERIFIED — #18 implementation commits were fast-forwarded into local main and pushed directly. PR #30 merged the plan earlier; it was not an implementation PR. Evidence: git first-parent log after PR #30, matching published main, and empty #18 closedByPullRequestsReferences.

VERIFIED — The operator expressed frustration that cross-referenced issues obscured whether #18 was done. A concise status should distinguish completed #18 from separate successor work without treating the entire Claude Code surface as complete. Evidence: conversation and #18/#19/#11 native scopes.

## Corrections to durable artifacts

VERIFIED — HANDOFF.md's host-rescope passage still says all eight new issues are open; treat it as a dated checkpoint. The live #18 issue is now CLOSED/COMPLETED. Evidence: inspected HANDOFF.md and current #18 intake.

VERIFIED — The #18 scenario records an OPEN/backplane:active issue snapshot during its probes; that is historical test evidence, while current issue state is CLOSED/COMPLETED. Evidence: scenario issue-state row and current gh issue view.

## Decisions and provenance

VERIFIED — The operator authorized the #18 push and completion transition, and explicitly requested this handoff and Git sync. Evidence: conversation and published Git/issue state.

INFERRED — Keep #19 and #11 visible as separate backlog obligations, without selecting or relabeling either. Evidence and reasoning: current native dependency chain, backlog labels, and #19/#11 plan fields.

## Negative results

VERIFIED — No implementation PR or linked closing PR exists for #18; PR #30 covers the plan. Do not describe #18 as merged through an implementation PR without new GitHub evidence. Evidence: #18 closedByPullRequestsReferences and git first-parent log.

VERIFIED — No #19 execution plan is recorded in its current body. Do not begin #19 execution or infer readiness from #18 closure alone. Evidence: complete #19 intake and its backplane:backlog label.

## Deferred obligations

VERIFIED — #19 still owns repeat install, pinned update, rollback, Backplane-only uninstall, five conformance checks, and authorized issue-state scenarios. #11 still owns final integrated Claude Code acceptance after #19. Evidence: current issue bodies and dependency edges.

## Risks and unknowns

UNVERIFIED — The next selected work item and priority are unknown. Required probe: refresh native intake and obtain operator selection or an applicable project priority policy.

UNVERIFIED — The post-sync handoff commit and remote alignment are unknown at CREATE. Required probe: after committing and pushing, compare local HEAD with the live remote main and inspect worktree status.

UNVERIFIED — A future Claude Code disposable profile's authentication and package inputs may differ from #18's recorded host run. Required probe: for any selected #19 work, check the current isolated profile, guide, upstream source, and package revisions at its verification seam.

## Proposed next steps

INFERRED — First invoke RESUME on this exact artifact, then re-read current project instructions, Git state, #18, #19, and #11. Preconditions: artifact is available and the active Superpowers installation can be confirmed. Verification seam: canonical artifact path, current Git identities, issue revisions, and native dependency fields. Evidence and reasoning: handoff and backlog contracts.

INFERRED — If the operator selects #19, reconcile its current body and approved design, create and approve an issue-specific Superpowers plan, then follow the required worktree, execution, review, and verification flow. Preconditions: explicit selection, current issue intake, and an approved plan before execution. Verification seam: #19 acceptance and five named conformance checks. Evidence and reasoning: #19 current backlog label, missing plan, and AGENTS.md workflow.

INFERRED — Address #11 only after #19's integrated evidence satisfies its native dependency and #11's current acceptance gates. Preconditions: completed #19 and current #11 intake. Verification seam: every mandatory Claude Code installation matrix row. Evidence and reasoning: #11 current blockedBy and body.

## Suggested skills

VERIFIED — Installed and applicable on RESUME: managing-superpowers-handoffs, managing-superpowers-backlog, superpowers:using-superpowers, superpowers:brainstorming, superpowers:writing-plans, superpowers:using-git-worktrees, superpowers:executing-plans, superpowers:requesting-code-review, and superpowers:verification-before-completion as the selected stage requires. Evidence: active skill catalog and inspected installed upstream checkout.

## Resume instruction

VERIFIED — Invoke managing-superpowers-handoffs RESUME with exact project-local path docs/superpowers/handoffs/20260920T202021Z-post-issue-18-claude-setup-continuation.md before selecting the next action. Evidence: this artifact's append-only CreateNew destination and handoff contract.
