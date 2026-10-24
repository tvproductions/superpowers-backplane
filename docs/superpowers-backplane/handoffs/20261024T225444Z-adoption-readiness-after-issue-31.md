# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-10-24T22:54:44Z. Evidence: UTC clock command during CREATE preparation.
- Repository identity: VERIFIED — standalone `/Users/jbabb/Documents/Devel/superpowers-backplane`, origin `https://github.com/tvproductions/superpowers-backplane.git`. Evidence: current Git root and origin probes.
- Branch: VERIFIED — `main`. Evidence: current Git status.
- HEAD: VERIFIED — `fc5c59434362779b4c5608c41e5176371cbd7004` before CREATE. Evidence: current Git HEAD; the later handoff storage commit is distinct.
- Incoming purpose: INFERRED — Resume the remaining Backplane adoption/release work after completed issue #31, using current companion guidance without importing its Python policy. Evidence and reasoning: operator wants other projects to use Backplane and requested end-of-day handoff/sync; no next issue is selected.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/31 is CLOSED/COMPLETED, no labels, observed `updatedAt=2026-10-24T14:24:11Z`. Evidence: fresh complete native intake. No successor work item is selected.
- Specification: VERIFIED — `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md`, tracked blob `52998773470537fc0e921132d610c7687911ff3a`. Evidence: current `git rev-parse HEAD:path`; this governs the completed #31 slice, not a new selected task.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-10-11-github-governance-bridges-implementation.md`, tracked blob `738fd8f43c1d02a9843dab743a211787c429e610`. Evidence: current Git blob probe; no successor execution plan is approved by this handoff.
- Superpowers derivation provenance: VERIFIED — active `.agents/skills/superpowers/{using-superpowers,brainstorming,writing-plans,executing-plans}/SKILL.md` resolves into the independent checkout at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (v7.0.1). Evidence: active inventory and skill reads, current upstream HEAD/status, and source digests recorded below. Current upstream README Codex installation guidance was fetched through `gh api` before CREATE.
- Predecessors: VERIFIED — immediate `docs/superpowers-backplane/handoffs/20261014T084025Z-issue-31-assessment-and-prompt-preference.md`; earlier `docs/superpowers-backplane/handoffs/20261014T080251Z-issue-31-remote-satisfaction.md`; historical `docs/superpowers/handoffs/20261011T172308Z-github-fdau-scope-discussion.md`. Evidence: tracked lineage and canonical path resolution within this repository. October24 session recovery also used local OpenCode/Codex history, summarized in the committed compatibility report; those machine-local histories are not required resume artifacts.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261024T225444Z-adoption-readiness-after-issue-31.md`. Evidence: canonical repository/storage containment and immediate collision check; AGENTS.md overrides the skill's default document namespace.

## Incoming purpose

INFERRED — Reconcile current release/adoption obligations and select the next bounded Backplane work item. Evidence and reasoning: #31 is finished; the operator's broader goal is usable adoption in other projects. Do not restart #31 or invent priority among remaining issues.

## Authority anchors

VERIFIED — Current AGENTS.md, SUPERPOWERS.md, native issues, and the selected issue's approved authorities govern. Evidence: session reads and live intake. The #31 authorities above retain their exact approved bytes. This handoff advises continuation and grants no new execution, issue mutation or release authority.

VERIFIED — Source convention SHA-256 values are: using-superpowers `82c5c8866ad7f5dd4440ce66bd7806ba48a2f13771beae5cf112e53f08fe36ba`; brainstorming `61a7ef918652108c76a3fd01e02dd92d39996c6b46d4cb2819cbd03f6c45e46a`; writing-plans `a6c67c1900064347c2a329990dd3c555657c51c3ec53b259a08aa01a2c26139a`; executing-plans `e4649e59880ef2643d1da128e3d607e87e3f969410d72095a5bf65811b6036dc`. Evidence: fresh source hashing at the active locators above. Successful discovery and reads do not establish every harness's compatibility.

## Verified current state

VERIFIED — `main` and freshly fetched `origin/main` agree at `fc5c59434362779b4c5608c41e5176371cbd7004`, zero ahead/behind, clean before CREATE. Evidence: root/origin/status, `git fetch origin`, and `git rev-list --left-right --count origin/main...main` returning `0 0`.

VERIFIED — Publication and #31 closure are complete. Evidence: `tests/scenarios/2026-10-24-issue-31-closeout.{md,json}` and fresh full native intake. Commit `17bd123ccb523e62c95b6008b363095800dbf087` publishes 7.0.1 maintenance and the scoped assessment; `fc5c594` stores closeout evidence. Both have verified remote arrival. The verified #31 delivery remains `c6f0b4a518e3742053618a613d8d858f0e37e9cd`, distinct from evidence storage.

VERIFIED — Independent upstream is clean at stable v7.0.1. Evidence: current HEAD/status and `tests/scenarios/2026-10-24-superpowers-v7.0.1-compatibility.md`. All five named conformance checks and fresh Codex discovery passed in their recorded scopes; the repository's OpenCode V2 native plugin was observed active at the same upstream commit.

## Live implementation thread

VERIFIED — No implementation task remains active in this session. Evidence: clean starting status and completed #31 closeout. Remaining release work was assessed through native #1/#6 and #19 intake earlier today; exact current selection/readiness must be refreshed before execution.

VERIFIED — The operator clarified that the uv initialization discussion belonged to gz-skills-first-starter, and directed that updated starter guidance be re-read and re-evaluated for its implications. Evidence: current conversation. Do not turn language neutrality into a reason to ignore companion guidance; assess its actual ownership and applicability before proposing Backplane changes.

VERIFIED — The separate starter was read at `731495876ef131c1a0795d38ad69116b77a594ca`, matching its remote main; it was clean and remained unmodified here. Evidence: Git identity/status/ls-remote plus reads of AGENTS.md, README.md, adoption-workflow, architecture, structure, updating, adoption-0.5, Astral alignment, and session-close handoff. Canonical repository: https://github.com/tvproductions/gz-skills-first-starter. This external source is not a Backplane handoff predecessor or a new mandatory dependency.

VERIFIED — The starter explicitly owns strict Python/tool preferences and asks that SP, gz-skills and SP-BP remain agnostic. Its development guidance already distinguishes initialization by existing pyproject metadata, preserves existing metadata, checks workspace membership and separates initialization from migration/acceptance. Evidence: starter `AGENTS.md:138` and `docs/engineering/astral-alignment.md:30` at the reviewed commit. No Backplane onboarding change was made or is required by that discussion alone.

## Corrections to durable artifacts

VERIFIED — October14 handoffs' pending #31 satisfaction/closure step is superseded by the published October24 assessment and closeout. Evidence: the closeout records and live CLOSED/COMPLETED state. Preserve predecessor artifacts unchanged as historical context.

VERIFIED — The earlier conversational suggestion that missing uv onboarding belonged in Backplane was withdrawn after the starter review. Evidence: the starter's explicit ownership policy and the operator's correction. Its precise new initialization paragraph and brownfield decision table exist on development main but not in published v0.6.0. Do not advertise them as released guidance.

## Decisions and provenance

VERIFIED — The operator authorized publication/closeout earlier and now requested handoff plus Git sync. Evidence: current conversation. This authorizes the scoped handoff commit/push, not a tag, release, starter migration or new issue execution.

VERIFIED — Current full-access runtime permissions and persistent user configuration were established during this session after approval-prompt friction. Evidence: effective runtime instructions and successful non-escalated GitHub commands. User configuration is host-local; this is not a transported repository setting. Recheck effective permissions on the receiving session rather than repeating permission advice from stale context.

VERIFIED — The operator prefers concise ready-to-send next prompts when useful. Evidence: prior handoff and current response practice. A displayed prompt is not execution authority.

## Negative results

VERIFIED — Searching `/Users/jbabb/Documents/Devel/gz-skills-starter` failed because that directory does not exist here; the correct separate checkout is `gz-skills-first-starter`. Evidence: path failure followed by verified Git origin. Do not infer the starter's location from its conversational shorthand on another host.

VERIFIED — The OpenCode plugin API with `--param directory=...` returned the home location, not the repository; the explicit `x-opencode-directory` header returned the correct repository and active package. Evidence: committed v7.0.1 report. Do not reuse the former response as repository installation evidence.

VERIFIED — `gh run list` for `fc5c594` returned an empty array. Evidence: current query. This is no observed workflow run, not a CI pass; use the repository's recorded skill/fixture checks and report any later CI separately.

## Deferred obligations

VERIFIED — The current v0.1 arc still includes host acceptance (#11/#12 with their implementation leaves), licensing/operations (#4), self-hosting (#5), external pilot (#6), and release review/publication (#7). Evidence: today's full native parent/pilot intake and committed #31 assessment. No next issue or priority was selected. Closing #31 supplies none of these unrelated completion results.

VERIFIED — Starter Backplane activation remains deferred pending readiness and explicit adoption. Evidence: reviewed starter README/adoption contracts. Do not activate its catalog pin merely because #31 closed; complete-stack and adopter acceptance are separate.

## Risks and unknowns

UNVERIFIED — Arrival of this handoff's later storage commit is pending at CREATE. Required probe: after authorized sync, compare local/remote main, containing commit and exact artifact bytes; on resume verify ancestry/availability again.

UNVERIFIED — Current next-issue readiness, approved plan and priority are not established. Required probe: fresh complete native intake of #1 and relevant children, current plans/approvals and operator selection before implementation.

UNVERIFIED — Complete-stack integration, other-harness acceptance, live full-graph/Project capture, production checkpoint recovery and missing Windows predecessor progress remain outside the established evidence. Required probe: the applicable separately scoped acceptance work. The retained 98 scoped expectations are not 98 new final-byte or v7.0.1 executions.

UNVERIFIED — The separate starter's future updates, release acceptance and receiving-host availability remain unknown. Required probe: re-read its current self-described entry points and exact reviewed revision when an update is reported; distinguish release guidance from development main and evaluate effects without silently adopting its policies.

## Proposed next steps

INFERRED — First invoke RESUME against this exact handoff, establish current repository/upstream/issue state and verify remote arrival. Evidence and reasoning: session boundary and published closeout make reconciliation the first action.

INFERRED — Then assess/select one remaining adoption work item through complete native intake; use its existing approved design/plan where available. Evidence and reasoning: no live implementation task remains and no priority policy selects a successor. Re-read updated starter guidance when relevant, preserving ownership; obtain any missing issue-specific approval before implementation.

## Suggested skills

VERIFIED — Observed applicable skills are `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:using-superpowers`, and `superpowers:verification-before-completion`; use brainstorming/planning/execution skills only as the next selected work requires. Evidence: active inventory and session skill reads.

## Resume instruction

VERIFIED — Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261024T225444Z-adoption-readiness-after-issue-31.md` before selecting the next action. Evidence: this explicit append-only handoff and the handoff contract.
