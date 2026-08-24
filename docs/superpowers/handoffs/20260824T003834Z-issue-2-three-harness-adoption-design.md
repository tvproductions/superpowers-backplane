# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — `2026-08-24T00:38:34Z`. Evidence: UTC creation observation immediately before destination derivation.
- Repository identity: VERIFIED — `https://github.com/tvproductions/superpowers-backplane.git` at canonical root `C:\Users\Jeff\source\repos\agents\superpowers-backplane`. Evidence: `git remote get-url origin`, `git rev-parse --show-toplevel`, and canonical path resolution.
- Branch: VERIFIED — `main`. Evidence: `git branch --show-current`.
- HEAD: VERIFIED — `c9c578b11107e835e77ddf96efbb34894423d72a`. Evidence: `git rev-parse HEAD`.
- Incoming purpose: VERIFIED — resume architectural design for issue #2, reconcile the three-harness scope with issues #3 and #8, and bring the adoption contract through reviewed specification and planning. Evidence: operator direction in the creating session and current issue #2 contract.
- Work item: VERIFIED — `https://github.com/tvproductions/superpowers-backplane/issues/2`, observed `updatedAt` `2026-08-24T00:35:15Z`. Evidence: complete native `gh issue view` intake during CREATE.
- Specification: UNVERIFIED — no issue #2 specification exists under `docs/superpowers/specs/`; the issue identifies `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md` only as background. Required probe: complete and approve the active architectural brainstorming, then create the issue-specific specification.
- Plan: UNVERIFIED — no issue #2 plan exists under `docs/superpowers/plans/`. Required probe: after the written specification is approved, invoke `superpowers:writing-plans` and bind the plan to the then-current issue revision.
- Superpowers derivation provenance: VERIFIED — installed upstream revision `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` from `https://github.com/obra/superpowers.git`; `superpowers:using-superpowers` at `.agents/superpowers/skills/using-superpowers/SKILL.md`, SHA-256 `30F2AB78E20DDC27EE7158AE8D4A2ABE161C360981C7CC3548070913142D3DC3`; `superpowers:brainstorming` at `.agents/superpowers/skills/brainstorming/SKILL.md`, SHA-256 `74EDF03EA6D24EF53DB48677B93558D14A979BDF052CA3F57ECDCA0C66791608`; `superpowers:writing-plans` at `.agents/superpowers/skills/writing-plans/SKILL.md`, SHA-256 `48508F44BBFD7D24B029FBF3A314F3CD14C9615599059366E922F47B8DC08CF2`. Evidence: installed checkout origin and revision plus fresh file hashes during CREATE.
- Predecessors: VERIFIED — none were supplied and no project-local handoff directory existed before this artifact. Evidence: incoming request and `Test-Path`/file-discovery observation.
- Storage location: VERIFIED — `docs/superpowers/handoffs/20260824T003834Z-issue-2-three-harness-adoption-design.md`. Evidence: canonical parent, prospective storage root, destination containment, and collision checks immediately before writing.

## Incoming purpose

- VERIFIED — Continue issue #2 from architectural brainstorming, preserving the operator-approved support boundary and lifecycle policy while resolving remaining backlog and installation-contract decisions. Evidence: issue #2 body and operator rulings recorded below.

## Authority anchors

- VERIFIED — Repository instructions are `AGENTS.md` at blob `cc8a76a0c37609b3979e23e9a329dfaace25ea36`; re-entry guidance is `HANDOFF.md` at blob `55f79650f77889e038425850ad4a6f32e92e22f8`; dependency state is `SUPERPOWERS.md` at blob `8772d2ffbf012f75b7aa3f667ffbd5c6eba09fb3`. Evidence: `git ls-files --stage` at the recorded HEAD.
- VERIFIED — Background design authority is `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md` at blob `6eca807ada7e356c643ad6700715820a61609f69`. Evidence: `git ls-files --stage` at the recorded HEAD.
- VERIFIED — GitHub issue #2 owns the current objective, three-harness bounded scope, acceptance criteria, verification seams, and lifecycle state. Evidence: complete native intake at `updatedAt` `2026-08-24T00:35:15Z`.
- VERIFIED — This handoff is advisory and grants no design, execution, Git, GitHub, publication, or closure authority. Evidence: `managing-superpowers-handoffs` and the handoff artifact contract.

## Verified current state

- VERIFIED — The worktree was clean on `main`, tracking `origin/main`, before CREATE. Evidence: `git status --short --branch` returned only `## main...origin/main`.
- VERIFIED — Issue #2 is open, is an executable leaf, has no native blockers, carries exactly `backplane:designing`, and natively blocks issues #3 and #5. Evidence: complete native issue intake.
- VERIFIED — Issue #2's body now supports exactly Codex, Claude Code, and OpenCode; requires one canonical Backplane `skills/` tree with thin harness adapters; keeps Superpowers separate and independently updateable; and requires workflow-scoped lifecycle tracking. Evidence: current issue body.
- VERIFIED — No issue #2 specification or plan was found in the current durable artifact directories. Evidence: scoped `rg` search returned `NO_ISSUE_2_SPEC_OR_PLAN_MATCH`.
- VERIFIED — The installed upstream Superpowers checkout is operationally observable through this session's active skill discovery, its authoritative origin, current revision, and readable `using-superpowers`, `brainstorming`, and `writing-plans` skills. Evidence: active skill list, file reads, origin check, revision check, and hashes above.

## Live implementation thread

- VERIFIED — No implementation has begun; the active Superpowers stage is architectural brainstorming. Evidence: issue lifecycle is `backplane:designing`, no issue-specific spec or plan exists, and no implementation changes were present before CREATE.
- VERIFIED — The next unresolved backlog decision is whether issue #8 should close as not planned because its post-Codex expansion scope is now absorbed by issue #2. Evidence: issue #8 remains open as `backplane:backlog`, still titled `Expand Backplane support beyond Codex`, and the operator had not answered the closure question before requesting this checkpoint.
- VERIFIED — Issue #3 remains titled `Deliver and document the Codex installation surface` and is blocked by issue #2, so its scope no longer covers the approved three-harness contract. Evidence: current native intake for issue #3.
- INFERRED — The likely implementation shape is one shared root `skills/` tree plus `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and an OpenCode-native discovery adapter that avoids duplicating skill content. Evidence and reasoning: current primary harness documentation and upstream Superpowers' installed harness layouts; the final adapter choice still requires specification approval.

## Corrections to durable artifacts

- VERIFIED — Issue #2 was corrected during this session from Codex-first scope to exactly Codex, Claude Code, and OpenCode, and its acceptance and verification contract was updated accordingly. Evidence: current issue body and reconciliation comment.
- VERIFIED — Issue #8 now overlaps issue #2 and needs explicit backlog reconciliation; it was intentionally left unchanged because closing as not planned requires operator authority. Evidence: current issue #8 state and the recorded issue #2 reconciliation comment.
- VERIFIED — Issue #3 needs scope reconciliation or decomposition before implementation planning because its Codex-only title and body no longer represent the complete approved installation surface. Evidence: current issue #2 and #3 contracts.

## Decisions and provenance

- VERIFIED — The operator selected issue #2 for design, authorizing its transition from `backplane:backlog` to `backplane:designing`. Evidence: operator direction and verified issue label.
- VERIFIED — The operator rejected globally read-only lifecycle behavior and approved evidence-based label changes as work status changes. Evidence: operator statements in the creating session.
- VERIFIED — Status, orientation, and recommendation-only requests remain non-mutating, while explicitly selected, started, resumed, submitted, or finished work receives evidence-gated lifecycle transitions without redundant confirmation. Evidence: operator approval and the reconciled issue #2 contract.
- VERIFIED — The supported harness set is exactly Codex, Claude Code, and OpenCode. Evidence: explicit operator direction and the reconciled issue #2 contract.
- INFERRED — The operator's acknowledgment accepted one canonical Backplane skill source with thin harness-specific adapters. Evidence and reasoning: the architecture was presented immediately before the operator confirmed the three-harness support set; the written specification must still present this section for explicit approval.
- VERIFIED — Upstream Superpowers remains a separate installation for each harness and must not be copied or vendored into Backplane. Evidence: repository instructions, bootstrap design, and issue #2 contract.

## Negative results

- VERIFIED — Direct canonical resolution of `docs/superpowers/handoffs` initially failed because the directory did not exist. Evidence: `Resolve-Path` returned a missing-path error. Do not retry direct resolution before creation; use the verified nearest-existing-parent and prospective-root procedure.
- VERIFIED — A fully read-only Backplane lifecycle was considered and rejected because it would allow lifecycle labels to become stale. Evidence: operator discussion and subsequent issue #2 contract change.
- VERIFIED — Codex-only v0.1 scope was superseded by explicit operator direction supporting Codex, Claude Code, and OpenCode. Evidence: current issue #2 contract.

## Deferred obligations

- UNVERIFIED — Issue #8 disposition remains undecided. Required probe: ask the operator whether its absorbed scope should close as not planned or be rewritten for a distinct post-v0.1 purpose, then use the backlog workflow for any mutation.
- UNVERIFIED — Issue #3 decomposition remains undecided. Required probe: after the issue #2 design fixes adapter boundaries, decide whether #3 becomes one three-harness implementation leaf or a continuity node with harness-specific children.
- UNVERIFIED — The issue-specific architectural specification is absent. Required probe: finish the brainstorming approaches and sectioned design, obtain operator approval, write the spec under `docs/superpowers/specs/`, self-review it, commit it, and request written-spec review.
- UNVERIFIED — The issue-specific implementation plan is absent. Required probe: only after spec approval, invoke `superpowers:writing-plans` and record the current issue URL and `updatedAt`.

## Risks and unknowns

- UNVERIFIED — Harness-native dependency behavior for installing or adopting Superpowers alongside Backplane is not yet fixed for all three harnesses. Required probe: specify detection, authorization, supported installation channel, version compatibility, update, rollback, and uninstall behavior per harness.
- UNVERIFIED — Current Codex, Claude Code, and OpenCode documentation may change before implementation. Required probe: re-fetch primary documentation while finalizing the specification and again during implementation verification.
- UNVERIFIED — The OpenCode adapter may need more than native skill discovery to deliver the required session bootstrap behavior. Required probe: compare Backplane's skills-only needs with the installed upstream Superpowers OpenCode plugin and run a fresh-session discovery probe before approving the adapter.
- UNVERIFIED — No fresh three-harness conformance evidence exists for the revised scope. Required probe: define and execute exact clean-install and fresh-session checks in the future implementation plan.

## Proposed next steps

1. VERIFIED — Invoke RESUME on this exact handoff before choosing an action. Evidence: handoff contract. Preconditions: operational Superpowers and repository identity match. Verification seam: the eight-field RESUME assessment reconciles current Git, issue, spec, and plan state.
2. UNVERIFIED — Resolve issue #8's disposition with explicit operator authority. Required probe: re-fetch issues #2 and #8 and ask the pending closure-or-repurpose question. Preconditions: issue semantics remain unchanged. Verification seam: complete native intake after any authorized mutation.
3. UNVERIFIED — Reconcile issue #3 with the approved three-harness contract. Required probe: decide its one-leaf versus parent-and-children structure after adapter boundaries are designed. Preconditions: issue #2 design direction is stable. Verification seam: native hierarchy and blocker edges match the resulting decomposition.
4. UNVERIFIED — Continue `superpowers:brainstorming` by comparing installation/dependency approaches, presenting the recommended architecture in sections, and obtaining explicit approval. Required probe: resume the dialogue from the decisions and unknowns above. Preconditions: current primary harness documentation is rechecked. Verification seam: operator approval of each design section.
5. UNVERIFIED — Write and self-review the issue-specific specification, then request operator review. Required probe: complete step 4. Preconditions: approved architectural design. Verification seam: no placeholders, contradictions, scope gaps, or ambiguous requirements.
6. UNVERIFIED — After specification approval, invoke `superpowers:writing-plans`. Required probe: re-fetch issue #2 and record its current `updatedAt`. Preconditions: approved committed specification. Verification seam: the plan binds all acceptance criteria and exact project-owned verification commands.

## Suggested skills

- VERIFIED — `managing-superpowers-handoffs` for RESUME. Evidence: active Backplane skill discovery.
- VERIFIED — `managing-superpowers-backlog` for issues #2, #3, and #8 intake or authorized reconciliation. Evidence: active Backplane skill discovery.
- VERIFIED — `superpowers:using-superpowers` and `superpowers:brainstorming` to continue the current design stage. Evidence: active upstream discovery and readable installed skills.
- VERIFIED — `superpowers:writing-plans` only after the written specification is approved. Evidence: installed upstream skill and current brainstorming gate.

## Resume instruction

- VERIFIED — Invoke `managing-superpowers-handoffs` RESUME against `docs/superpowers/handoffs/20260824T003834Z-issue-2-three-harness-adoption-design.md` before selecting or mutating the next action. Evidence: this artifact's verified storage location and the handoff contract.
