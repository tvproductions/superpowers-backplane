# Session handoff

- Format: superpowers-backplane-handoff/v1
- Creation time: VERIFIED — 2026-10-11T17:23:08Z. Evidence: UTC clock at write.
- Repository identity: VERIFIED — C:/Users/Jeff/source/repos/agents/superpowers-backplane; origin https://github.com/tvproductions/superpowers-backplane.git. Evidence: git rev-parse --show-toplevel and git remote get-url origin.
- Branch: VERIFIED — plan/issue-19-claude-lifecycle-draft. Evidence: git status --short --branch.
- HEAD: VERIFIED — 27679be948042cf2f6a698508ea34b19648eae71. Evidence: git rev-parse HEAD.
- Incoming purpose: VERIFIED — Continue discussion of cohesive GitHub work management and possible FDAU requirements/feature management for skills-first projects. Evidence: operator conversation.
- Work item: UNVERIFIED — No work item identified for this new discussion. Required probe: establish whether an existing issue covers it before backlog changes.
- Specification: VERIFIED — Existing bootstrap background at docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md, tracked blob 6eca807ada7e356c643ad6700715820a61609f69. Evidence: git rev-parse HEAD:path; read this session. No new hybrid specification was approved.
- Plan: VERIFIED — Existing bootstrap background at docs/superpowers/plans/2026-08-16-superpowers-backplane-bootstrap.md, tracked blob ccedeba886d76462a74339fa7d077e65a61104c4. Evidence: git rev-parse HEAD:path; read this session. No new hybrid implementation plan exists from this conversation.
- Superpowers derivation provenance: VERIFIED — Active-discovered .agents/skills/superpowers/{using-superpowers,brainstorming,writing-plans,executing-plans}/SKILL.md read; junction resolves to .agents/superpowers/skills at bb92a77741419a4ab5f06e711a283343f1ada0c3. Evidence: active skill inventory, reads, junction inspection, and upstream HEAD. Installation guidance: .agents/superpowers/README.md, Codex sections.
- Predecessors: VERIFIED — None designated for this discussion. Evidence: conversation; existing issue-19 handoffs were not selected as predecessors.
- Storage location: VERIFIED — C:/Users/Jeff/source/repos/agents/superpowers-backplane/docs/superpowers/handoffs/20261011T172308Z-github-fdau-scope-discussion.md. Evidence: canonical containment and append-only write checks.

## Incoming purpose

VERIFIED — Discuss how GitHub work items, FDAU's requirements approach, and Backplane/Superpowers execution can work cohesively for skills-first projects. Evidence: operator direction.

## Authority anchors

VERIFIED — AGENTS.md, SUPERPOWERS.md, the bootstrap artifacts above, and skills/managing-superpowers-backlog/references/github-issue-contract.md remain current project guidance. Evidence: inspected documents. This handoff is advisory and does not approve a new design.

## Verified current state

VERIFIED — The independent local Superpowers checkout is on stable v7.0.0 at bb92a77741419a4ab5f06e711a283343f1ada0c3. Evidence: fresh upstream HEAD probe.

VERIFIED — This session ran all five required compatibility checks and separate fresh discovery, with results and transcripts in tests/scenarios/2026-10-11-superpowers-v7.0.0-compatibility.md. Evidence: captured responses, rubric scoring, and zero-exit session results.

VERIFIED — HANDOFF.md and SUPERPOWERS.md are modified; the compatibility report and five 2026-10-11-v7 transcripts are untracked. Evidence: fresh git status. No commit or publication was performed during this session.

## Live implementation thread

VERIFIED — Discussion covered issues, types, hierarchy, dependencies, ownership, lifecycle labels, saved Views, Projects, Milestones, and PR/verification evidence. Evidence: conversation.

INFERRED — A useful division is requirements/features authority connected to GitHub-owned work items, with Backplane binding work to Superpowers and handoffs. Evidence and reasoning: operator wants cohesion; the exact mapping remains undecided.

## Corrections to durable artifacts

VERIFIED — Dependency records were synchronized to v7.0.0 after compatibility scoring. Evidence: local diff and verification. Existing optional-Projects policy was discussed but not changed.

## Decisions and provenance

VERIFIED — Operator states GitHub can own work items and wants to explore FDAU's requirements/features approach, potentially a hybrid. Evidence: direct conversation.

VERIFIED — Operator explicitly ruled: "we will NOT copy gzkit". Evidence: direct operator instruction. Do not treat gzkit as a blueprint or introduce it as a dependency.

VERIFIED — The operator prefers examining GitHub's feature inventory rather than starting with a generic workflow pain question. Evidence: correction in conversation.

## Negative results

VERIFIED — Default-sandbox GitHub requests failed against the restricted proxy; approved escalated read-only checks succeeded. Evidence: tool outputs. Do not repeat the same restricted network request expecting a different result.

VERIFIED — Upstream .codex/INSTALL.md and docs/README.codex.md were absent; current Codex installation instructions were found in upstream README.md. Evidence: path probes and README read. Use current documentation rather than presumed legacy paths.

## Deferred obligations

UNVERIFIED — FDAU requirements implementation has not been reviewed. Required probe: read project guidance and relevant requirements/features material at C:/Users/Jeff/source/repos/xp/xplane-fdau before proposing adoption.

VERIFIED — Dependency changes and this handoff remain local and uncommitted. Evidence: session actions and git status; transport/integration is a later decision.

## Risks and unknowns

UNVERIFIED — Requirement identifiers, satisfaction links, change control, milestone policy, Project fields, and saved View conventions remain undecided. Required probe: examine FDAU and agree an explicit authority/traceability design.

VERIFIED — The current branch belongs to issue-19 planning; the new management discussion is a separate thread. Evidence: branch identity and operator conversation. Do not execute issue #19 merely because it is the checked-out branch.

## Proposed next steps

1. INFERRED — Resume this exact handoff and reconcile Git state first. Evidence and reasoning: preserve local dependency changes and distinguish the current discussion from issue #19.
2. INFERRED — With this exploratory scope, inspect FDAU requirements/features material read-only. Evidence and reasoning: operator proposed exploring it; verify findings against actual sources.
3. INFERRED — Discuss the mapping of requirements/features to GitHub work items, hierarchy, dependencies, labels, Views, Projects, Milestones, and delivery evidence. Evidence and reasoning: operator's requested inventory; produce a design only after decisions are clear.
4. INFERRED — Treat dependency-update integration as a separate maintenance decision. Evidence and reasoning: evidence is ready locally, but no publication was requested.

## Suggested skills

VERIFIED — Observed relevant skills: superpowers:using-superpowers, superpowers:brainstorming, superpowers-backplane:managing-superpowers-backlog, superpowers-backplane:managing-superpowers-handoffs; use superpowers:writing-plans only after approved design. Evidence: active inventory and source reads.

## Resume instruction

INFERRED — Invoke superpowers-backplane:managing-superpowers-handoffs RESUME against C:/Users/Jeff/source/repos/agents/superpowers-backplane/docs/superpowers/handoffs/20261011T172308Z-github-fdau-scope-discussion.md before selecting the next action. Evidence and reasoning: explicit artifact preserves this discussion; current authority must be reconciled.
