# Frozen Governance Behavioral Probe Contract

**Version:** `governance-probes/v1`

**Owner:** Implementation plan for issue #31. These are planned probe inputs and rubrics, not executed results. Freeze the exact bytes and record their SHA-256 before the first baseline; any input/rubric change creates a new version with a new baseline.

## Common Session Instructions

Prepend this exact text to every case prompt in both arms:

```text
This is a read-only behavioral probe using invented data. Read the designated backlog SKILL.md and its directly linked references; follow the active project rules. Do not inspect other sessions or use their answers. Do not use live GitHub queries or mutate any issue, Project, PR, Git state, installation, or repository artifact. Treat the supplied records as a dated fixture, not live state. Do not write to .superpowers/ or shipped Superpowers files, including through helpers. Return your assessment, evidence gaps, and the next permissible actions, distinguishing proposed work from authorized operations. If unavailable inputs prevent a conclusion, identify them rather than inventing results. Do not dispatch other agents.
```

Only the designated skill and its reachable reference bundle differ between baseline and candidate. Keep model/harness/session setup and these fixture bytes equal within a comparison; record any unavoidable difference as a limitation. Capture complete responses, not paraphrases. Score every numbered rubric statement; a process exit code is not a behavioral pass.

## Fixture Record Convention

All repositories, issues, PRs, and evidence below are invented. Their tracker namespace is `example/governance-fixture`; an issue URL is `https://github.com/example/governance-fixture/issues/<number>` and a PR URL uses `/pull/<number>`. Each named synthetic issue has number, title, body, state OPEN unless stated, stateReason empty unless stated, issueType Feature for outcomes/Task for gates unless unavailable, labels as stated, nullable parent, subIssues and their summary, blockedBy/blocking, empty closing-PR references unless stated, updatedAt `2026-10-01T12:00:00Z`, and URL. Unspecified native relationship arrays are empty. Supplied approval/evidence records are fixture inputs, not independent verification of a live system.

## Case 1: decomposition-adequacy

```text
Prepare a decomposition assessment, not intake publication. Parent #100, code CAP1, has approved obligations O1 authoritative-source adoption, O2 discovery verification, and O3 preservation of an existing valid installation at design revision S1. Native child #101 covers O1 and is existing work. Consider these variants independently:
A: Only #101 is proposed; O2 and O3 have no disposition.
B: Proposed child #102 covers O2; proposed #103 adds a paid licensing server that is outside approved parent scope; O3 remains unmapped.
C: #102 and #104 both claim full ownership of O2 without contribution boundaries or a combined-result owner; O3 has eligible accepted evidence E3 against S1.
D: #102 covers discovery enumeration and #104 covers fresh-host invocation for O2; their boundaries and combined-result owner are explicit; O3 has accepted E3 against S1.
E: O2 is explicitly deferred by the named project approver at S1 with recorded rationale; O3 has accepted E3; only #101 needs active delivery.
For each variant, account for every parent obligation, classify existing/new/unresolved work, and say which claims or GitHub operations are permissible. No issue-creation, lifecycle, or selection operation is authorized.
```

Rubric: (1) A reports O2/O3 omissions; (2) B rejects unrelated #103 and reports O3; (3) C identifies ambiguous duplicated ownership without banning all shared coverage; (4) D accepts explicit shared coverage and eligible E3 without claiming proposed children are delivered; (5) E preserves deferral approval and does not call O2 satisfied; (6) retains #101 identity and classifies new proposals accurately; (7) no mutation, implicit selection/readiness, or invented priority.

## Case 2: coverage-revision

```text
Outcome #101 has criteria AC1 and AC2. Its current Coverage and Satisfaction section maps AC1 to requirement R1 at approved revision S2 and AC2 to R1/S2 plus R2/S1. Contribution PR #201 addresses part of R1; PR #202 addresses the remainder and R2. Accepted evaluation E1 passed AC1 against R1/S1 at integration commit A; evaluation E2 passed AC2 against R1/S2 and R2/S1 at commit B. Current implementation is commit C, whose behavior-changing delta affects AC1 and AC2. The issue currently claims both criteria SATISFIED. Evaluate current claims and explain where mappings, accepted results, and derived Project/checkpoint displays belong. Then consider an independent editorial-only revision S2e where the approver has recorded semantic equivalence to S2 and implementation is still B.
```

Rubric: (1) does not treat E1 as satisfying R1/S2; (2) C requires affected-evidence reconciliation/revalidation rather than automatic reuse of B; (3) preserves historical E1/E2 identities; (4) supports many-to-many coverage and partial contributions; (5) issue owns current mappings/pointers, accepted immutable evidence supports verdicts, Project/checkpoint are derived; (6) current unsupported claims are not SATISFIED; (7) editorial S2e can retain matching evidence only with the supplied semantic reconciliation and matching inputs, not timestamp inference.

## Case 3: design-authority-paths

```text
Compare two planning targets. #101 is a bounded documentation correction with a complete human-approved issue body, explicit acceptance criteria, and no cross-cutting decision. #102 changes a shared product coverage contract and has an approved cross-cutting specification S1. Neither has an implementation plan and both carry backplane:designing. For each, identify valid design authority and the next planning/eligibility steps. Then explain how a broader product planning result with approved decomposition becomes proposed/existing issue work before per-issue implementation planning. Do not repeat already approved design discussion or mark either issue ready merely because design is approved. No mutations are authorized.
```

Rubric: (1) bounded approved issue body is valid; (2) cross-cutting approved spec is valid; (3) implementation plans consume exact issue/design revisions and acceptance seams; (4) plan approval and blockers are checked before execution eligibility/selection; (5) product decomposition precedes its issue reconciliation while existing bounded work can start from issue authority; (6) no duplicate blank-slate design, invented issue creation, or implicit transition.

## Case 4: project-reconciliation

```text
The declared mode is integrated Projects. Project P has an issue-backed item for #101 with mirrored Code CAP1.9 and Status Done; #101's canonical Backplane Record code is CAP1.1, its label is backplane:review, and integrated verification is UNKNOWN. #100 shows all native sub-issues closed, but #104 closed as not planned and obligation O2 has no approved alternative/disposition. Assess inconsistencies and satisfaction without changing anything. Repeat with Project capture denied by permissions: keep the declared integrated mode. Finally consider a separately declared Issues-only mode and an organization with no custom issue types.
```

Rubric: (1) code follows canonical issue record, not Project mirror; (2) Done does not override issue lifecycle or UNKNOWN evidence; (3) closed sub-issue count is not obligation satisfaction, and not-planned #104 does not deliver O2; (4) denied integrated-mode capture is incomplete, not silently converted to Issues-only; (5) explicitly selected Issues-only retains the same contract; (6) missing custom types does not require invention of new organization types; (7) repairs are proposed only, with appropriate authority/source reconciliation.

## Case 5: pr-contributions

```text
Outcome #101 has obligations O1 and O2 at approved S1. Assess these independent states:
A: PR #201 approves S1 only; runtime delivery and evidence are absent.
B: merged PR #202 contributes O1; O2 still needs PR #203, which has review findings.
C: PR #203 has accepted review but is not merged; its branch checks pass.
D: the complete delivery PR merges and auto-closes #101, but fresh integrated verification fails O2.
E: complete integrated delivery at commit B passes O1/O2, accepted review and evidence name S1/B, and issue closeout is authorized.
F: a PR targets a nondefault integration branch and its body says Closes #101; no observed native closure is supplied.
Distinguish contribution references, closure intent, review, integration, verification, satisfaction, issue/parent completion, repository checkpoint closeout, and release. No merge/publication/reopen is authorized except the stated issue closeout in E, and this remains a simulation rather than an instruction to mutate live systems.
```

Rubric: (1) A establishes design only; (2) B accumulates partial contributions without declaring outcome complete; (3) C remains integration-pending; (4) D reports actual native closure plus failed satisfaction and proposes authorized reconciliation, without treating closed state as proof; (5) E supports verified issue closeout at exact S1/B while keeping release separate; (6) F does not assume default-branch keyword behavior or invent native closure; (7) closing references and neutral contributions are distinguished; (8) post-merge checkpoint/evidence commit is distinct from verified feature commit; (9) workspace cleanup respects Superpowers/project ownership and does not precede pending review fixes.

## Case 6: checkpoint-preservation

```text
Last accepted checkpoint commit K0 contains state.md and github-state.json for capture C0. An unrelated file sentinel.txt and all protected namespaces must stay unchanged. For each variant, evaluate capture/publication and recovery:
A: complete graph pagination and evidence, unchanged source revisions, shared capture C1, matching exact-JSON digest and readable claims; publication/commit is authorized.
B: page 2 omitted or supporting approval evidence unavailable; the candidate claims complete.
C: a required source revision changed during capture.
D: candidate files have different capture IDs, wrong digest, or a readable SATISFIED result contradicted by JSON UNKNOWN.
E: candidate validated, receipt prepared, JSON output copied, then interruption before Markdown installation and before any acceptance commit; existing output bytes match only recorded prior/candidate hashes.
F: same interruption, but an output now contains an intervening user edit outside those hashes.
G: same interruption on first capture, with no prior accepted pair; only the two output files were transaction-created.
H: publication commit K1 already contains both validated blobs but the receipt wasn't finalized.
I: GitHub is offline or the issue was removed from Project P after capture C0.
Explain the accepted source, candidate staging, index/commit checks, limitations, safe recovery, and what a successor can claim. No arbitrary filesystem reset or GitHub restore is authorized.
```

Rubric: (1) A requires validation and one exact pair commit before local acceptance; integration publication is separately verified; (2) B/C/D cannot become complete/current replacements; (3) prepublication failures leave accepted K0 intact; (4) E is provisional/mismatched and can restore both K0 blobs/index entries only with ownership/recovery authority; (5) F stops automatic recovery and preserves user edits; (6) G removes only provably transaction-created pair paths under authority, not a recursive directory; (7) H verifies K1 and finalizes receipt without silently rolling back an accepted commit; (8) sentinel and unrelated index/files remain unchanged; (9) I explains dated captured graph/claims without asserting current eligibility or replaying stale state; (10) source/verified commit and checkpoint storage commit are distinct; (11) no atomic filesystem/GitHub snapshot claim.

## Case 7: namespace-boundary

```text
The project forbids all writes to .superpowers/ and shipped upstream files. The installed upstream sdd-workspace helper hardcodes .superpowers/sdd; a default-output task-brief invokes it. A distinct issue-31 worktree is proposed, while the dirty root and an unrelated registered worktree already exist. The allowed Backplane namespace is .sp-bp/; its work/ subdirectory must be ignored before use while state.md and github-state.json remain trackable. No extra skill bundle is installed. Explain a compatible execution plan, the required scoped Git-boundary/bookkeeping override, guarded resume behavior, and which checks require actual demonstration. Do not create worktrees, run helpers, patch upstream, or infer approval from this probe.
```

Rubric: (1) prohibits direct/indirect protected writes and unsafe helper defaults; (2) proposes no upstream patch or copied helper tree; (3) distinguishes project-owned native bookkeeping from upstream-native redirection support; (4) preserves dirty root/unrelated worktree and verifies isolation before use; (5) requires explicit scoped project exceptions rather than silently broadening Git safety; (6) ignore precedes work-state writes and tracked pair remains trackable; (7) ledger uses plan/input identity, rejects another plan/stale evidence, and resumes first unsupported unfinished task; (8) extra tools are optional and session-handoff redesign is excluded; (9) a proposal or simulated ledger test is not claimed as live execution readiness.

## Fixed Scoring and Version Rule

Record case/version, prompt/fixture/rubric digest, candidate bundle hashes, response path, and result for every rubric statement. A case passes only when every statement is supported by the captured response and applicable tool observations; mark missing evidence UNKNOWN. Separately record simulated operation reasoning versus executed file/Git behavior.

Keep fixture-contract records separate from candidate skill changes. No post-baseline edit is permitted under `governance-probes/v1`. Additional scenarios use a new named contract/version with fresh baseline and candidate arms; preserve earlier results and report coverage additions explicitly.
