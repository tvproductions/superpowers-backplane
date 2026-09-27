# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-09-27T16:56:20Z. Evidence: UTC clock observed immediately before CREATE.
- Repository identity: VERIFIED — `https://github.com/tvproductions/superpowers-backplane.git` at standalone root `C:/Users/Jeff/source/repos/agents/superpowers-backplane`. Evidence: `git remote get-url origin`, `git rev-parse --show-toplevel`, and canonical path resolution.
- Branch: VERIFIED — `plan/issue-19-claude-lifecycle-draft`, tracking `origin/plan/issue-19-claude-lifecycle-draft`. Evidence: `git status --porcelain=v1 --branch`.
- HEAD: VERIFIED — `00edce9ea901bfd3a3e00a924d7fb1d7e1deaa16` before CREATE. Evidence: `git rev-parse HEAD`.
- Incoming purpose: VERIFIED — resume review of Claude Code lifecycle issue #19 and reconcile the draft plan with the operator's fixture decisions before seeking plan approval or implementation. Evidence: operator conversation and request for a fresh handoff before Git sync.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/19, OPEN with `backplane:designing`, `updatedAt` `2026-09-27T14:09:57Z`; closed #18 blocks it and it blocks open #11. Evidence: complete native `gh issue view 19` intake.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` at tracked blob `a790d953691d178f711757e9164afb60932eb65a`; `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` at tracked blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: `git ls-files -s` and inspected design boundaries.
- Plan: VERIFIED — draft `docs/superpowers/plans/2026-09-27-claude-code-lifecycle-and-conformance.md` at tracked blob `a98238588e8bea8f4017edabeeaa8e31297aa8d5`; not approved or linked in #19's issue body. Evidence: `git ls-files -s`, staged-diff review before commit, and current issue intake.
- Superpowers derivation provenance: VERIFIED — current upstream installation README at blob `cf80400690849b37861f39d396d231ea89ac693b` documents separate harness installation; active `.agents/skills/superpowers` junction resolves the `obra/superpowers` checkout at `5bf4e78011075bcfc0dc295f0724994cd123ee71`. Inspected `superpowers:using-superpowers` at `.agents/superpowers/skills/using-superpowers/SKILL.md` (SHA-256 `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA`), `superpowers:brainstorming` at `.agents/superpowers/skills/brainstorming/SKILL.md` (`A32D2255354775AA124855AA7100CF276BEA096FFF4EBB3A0EDF57BE216E6C72`), and `superpowers:writing-plans` at `.agents/superpowers/skills/writing-plans/SKILL.md` (`0BC3D36590F7B2C323ED3EC18FF77E9F8ED57AF42F5680A02B11A2D20DE265CF`). Evidence: current README via `gh api`, active skill discovery, inspected skill files, checkout origin/HEAD, and `Get-FileHash`.
- Predecessors: VERIFIED — `docs/superpowers/handoffs/20260920T202021Z-post-issue-18-claude-setup-continuation.md` at tracked blob `1afb451b46229d80703f4a6ffb73110c7da8fe03`, then `docs/superpowers/handoffs/20260920T160331Z-post-issue-17-host-continuation.md` at `af51bb57f615b23192a9585adf70856459d53256`, then `docs/superpowers/handoffs/20260920T015816Z-remaining-host-installation-leaves.md` at `3049d51a94992525b2c673ccae2a600e20a8ceca`. Evidence: inspected predecessor identity and lineage, canonical in-repository path resolution, and `git ls-files -s`.
- Storage location: VERIFIED — `docs/superpowers/handoffs/20260927T165620Z-issue-19-claude-lifecycle-plan-review.md`, an append-only project-local artifact. Evidence: canonical root/parent resolution, ancestor reparse checks, and destination collision check immediately before CREATE.

## Incoming purpose

VERIFIED — Finish the #19 design and plan review from the selected issue and approved fixture constraints; do not treat this handoff or the saved draft as implementation approval. Evidence: operator conversation, current issue label, and draft-plan handoff section.

## Authority anchors

VERIFIED — `AGENTS.md`, `HANDOFF.md`, `SUPERPOWERS.md`, the two tracked specifications and draft plan above, and current native issue #19 fields govern continuation; this handoff is advisory. Evidence: inspected repository instructions, blob identities, and `gh` intake.

## Verified current state

VERIFIED — The draft plan was committed as `00edce9` and pushed to its dedicated branch. Immediately before CREATE, local and tracked remote refs matched at ahead 0/behind 0 and the worktree was clean. Evidence: post-push fetch, explicit-ref `git rev-list --left-right --count`, matching `git rev-parse` IDs, and `git status`.

VERIFIED — The draft-plan save point passed `git diff --cached --check` and `claude plugin validate --strict .`; no #19 lifecycle test was run. Evidence: observed command exits and validation output during Git sync.

VERIFIED — Current official upstream installation guidance was read through `gh api`; the project checkout has authoritative `https://github.com/obra/superpowers.git` origin and recorded stable `v6.4.1` revision. Evidence: current upstream README, `SUPERPOWERS.md`, and checkout Git queries.

## Live implementation thread

VERIFIED — The operator selected #19, agreed to a disposable GitHub issue in this repository, and conditionally accepted a temporary unreleased `0.1.1` test branch if Claude's real update path requires a hosted source. Evidence: conversation; current Claude CLI help and official marketplace documentation show local-directory plugins load changed files in place.

VERIFIED — The operator's longer-term product target is `1.0.0` through normal SemVer progression, with no release candidate; the current native release parent still targets `v0.1.0`. Evidence: operator conversation and issue #19 parent intake.

UNVERIFIED — The operator has not yet answered the final shared-understanding question for the #19 plan; the draft remains unapproved. Required probe: present the corrected, concrete plan for review and obtain the operator's response before execution.

## Corrections to durable artifacts

VERIFIED — Draft plan Task 2 currently changes only version fields in the candidate; add a distinguishable fixture content identity so a successful update proves candidate bytes, while keeping it unreleased. Evidence: inspected tracked plan and discussion of the required update evidence.

VERIFIED — Draft plan Task 4 currently proposes an arbitrary dated line for the disposable issue; replace it with a useful documentation change that goes through ordinary review, integration, and verified closure. Evidence: inspected tracked plan and operator's acceptance of the recommended fixture location and completion path.

VERIFIED — #19's issue body still says `Plan: not yet created`; after plan approval, reconcile its current `updatedAt` and link the approved plan through the backlog workflow. Evidence: current issue body and tracked draft-plan blob.

## Decisions and provenance

VERIFIED — The operator approved a disposable issue fixture in the Backplane repository and accepted a temporary test branch only if needed for the hosted Claude update check. Evidence: conversation; these are fixture decisions, not approval of the whole implementation plan.

VERIFIED — The operator explicitly invoked Git sync; the draft was saved on a dedicated branch rather than merged to `main`, and the operator then requested this handoff followed by another sync. Evidence: conversation, commit `00edce9`, branch and remote state.

INFERRED — Preserve the release-skill discussion as separate future work rather than folding it into #19. Evidence and reasoning: #19's bounded lifecycle scope and the operator's separate request to discuss a reusable release skill.

## Negative results

VERIFIED — A local-directory Claude marketplace plugin reads edited files directly and therefore cannot, by itself, prove the hosted `plugin update` path. Do not substitute that observation for the pinned update result. Evidence: current Claude marketplace documentation and installed CLI help.

VERIFIED — The first post-push alignment commands using unquoted Git `@{upstream}` syntax failed in PowerShell parsing; explicit remote-ref commands then showed matching SHAs and ahead 0/behind 0. Use the explicit remote ref in PowerShell. Evidence: observed command outputs during prior Git sync.

## Deferred obligations

VERIFIED — The operator reported duplicated gz-skills in this environment. A local check found one cached `gz-skills` version (`0.5.0`) and no `gzs-*` directories in the inspected personal or project skill directories; the displayed duplication was not explained or changed. Evidence: operator comment and directory inspection.

VERIFIED — Release workflow planning remains separate; no reusable Backplane release skill or `1.0.0` release plan was created in this thread. Evidence: operator conversation and #19 bounded scope.

## Risks and unknowns

UNVERIFIED — Claude's authenticated disposable profile, installed Backplane/upstream identities, and hosted update behavior may have changed since #18. Required probe: inspect the selected isolated `CLAUDE_CONFIG_DIR`, `claude auth status --json`, plugin inventories, and version/source evidence before lifecycle tests.

UNVERIFIED — A future fixture branch's reachability and cleanup strategy have not been tested; deleting it may impair replay. Required probe: before publication, review how the exact candidate SHA and fixture bytes will remain auditable after testing.

UNVERIFIED — This handoff's eventual commit and remote alignment are not known at CREATE. Required probe: after the requested Git sync, fetch and compare local HEAD to the tracked remote branch, ahead/behind counts, and worktree status.

## Proposed next steps

INFERRED — First RESUME this exact artifact and reconcile its repository, branch, plan blob, and issue revision against live evidence. Preconditions: active Superpowers and project-local artifact are available. Verification seam: canonical path, Git state, and complete native issue intake. Evidence and reasoning: handoff and backlog contracts.

INFERRED — Revise the draft plan on its branch to reflect the approved fixture decisions and distinguishable update evidence, then review it with the operator. Preconditions: current issue/spec reconciliation and clear fixture source strategy. Verification seam: plan audit against #19 acceptance and the two tracked specifications. Evidence and reasoning: inspected draft and conversation; no execution approval has been given.

INFERRED — After explicit plan approval, follow the applicable Superpowers execution, review, and verification workflow; keep any actual release or upstream update outside #19. Preconditions: approved current plan and verified disposable Claude profile. Verification seam: every mandatory #19 lifecycle and conformance row scored `PASS`. Evidence and reasoning: `AGENTS.md`, current issue, and approved design.

## Suggested skills

VERIFIED — Current discovery exposes `superpowers:using-superpowers`, `superpowers:brainstorming`, `superpowers:writing-plans`, and the Backplane `managing-superpowers-handoffs` and `managing-superpowers-backlog` skills. Evidence: active skill catalog, junction checks, and inspected skills. Apply review and execution skills only at their later stages.

## Resume instruction

VERIFIED — Invoke `managing-superpowers-handoffs` RESUME with exact project-local path `docs/superpowers/handoffs/20260927T165620Z-issue-19-claude-lifecycle-plan-review.md` before selecting the next action. Evidence: this append-only CREATE destination and handoff contract.
