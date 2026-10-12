# Issue #31 Mac execution checkpoint

Observed: 2026-10-12T23:44:14Z. This tracked execution summary is separate from
ignored scratch and from the unimplemented product checkpoint format. It
records setup and the first unsupported task, not recovered Windows completion.
The storage commit is the commit containing this file and its evidence; it is
not embedded in its own contents. Local commit acceptance and remote transport
remain distinct.

## Authority and inputs

- Work item: https://github.com/tvproductions/superpowers-backplane/issues/31
- Observed issue revision: `2026-10-12T01:29:48Z`; OPEN/Feature,
  exactly `backplane:active`, no native parent/children/blockers/closing PRs.
- Approved plan: `2026-10-11-github-governance-bridges-implementation.md`,
  SHA-256 `ae05361badc5be68474b4fc5ea19de01f806b31e245c5f9e88be99e1da3e72f1`.
- Approved specification: `../specs/2026-10-11-fdau-github-governance-design.md`,
  SHA-256 `677bcc5ce2707781f0ee05c15306bd1be0587a801ca48699fba195722681bdb0`.
- Frozen probe contract: `2026-10-11-governance-probe-contract.md`, version
  `governance-probes/v1`, SHA-256
  `fc23cbae20160535f0836eff9920649c0dc78fe50b17ac3082904f2b38710f81`.
- The original approved files remain unchanged. The prior recovery assessment
  records their published Git identities and the known Windows continuity gap.
- Current operator direction: Mac setup and recovery in this conversation.
  The October 11 native-inline execution and protected-namespace exceptions
  remain in AGENTS.md; this record does not authorize publication or release.

## Actual Mac isolation identity

- Source repository: `/Users/jeff/Documents/Code/superpowers-backplane`.
- Native creation operation: `e4300ecb-c9ae-4e9b-ae44-3f7828c1e4fa`.
- Exact returned workspace:
  `/Users/jeff/.codex/worktrees/d181/superpowers-backplane`.
- Shared Git directory:
  `/Users/jeff/Documents/Code/superpowers-backplane/.git`.
- Starting HEAD: `82fa208cd81b1ae33a6b24e869220f90c9558312`.
- Branch state: detached HEAD, managed by the native harness.
- Root, registration, shared directory, clean starting state, and detached
  identity were independently verified before workspace mutations. The identity
  was first recorded in an external provisional ledger, then copied into the
  ignored workspace after its ignore rule was established.
- Root remains on `main`; the native worktree is retained for further work.
  A Mac path is not an alias for the unavailable Windows worktree.

Upstream is the separate development checkout at the source root's
`.agents/superpowers`, authoritative origin `obra/superpowers`, stable v7.0.0,
commit `bb92a77741419a4ab5f06e711a283343f1ada0c3`. The worktree's ignored
`.agents/superpowers` link adopts that existing source; local Backplane links
resolve to this worktree's own `skills/` tree. No upstream file is modified.

## Evidence and task disposition

[Mac setup evidence](../../../tests/scenarios/2026-10-12-mac-superpowers-v7.0.0-setup.md)
contains all five existing conformance results and fresh discovery. The five
complete captured responses are tracked with it. This is evaluated setup
behavior, not the new governance baseline or task completion.

| Task | Current disposition | Required next evidence |
| --- | --- | --- |
| 1: Negative controls and doctrine | needs-revalidation; no supported governance baseline or doctrine completion | Frozen seven-case baseline, full rubric scoring, separately versioned freshness baseline if added, and reviewed doctrine |
| 2: Product planning/intake bridge | unverified/not reached on Mac | Task 1 outputs and task-specific fresh evidence |
| 3: PR closeout bridge | unverified/not reached on Mac | Prior outputs and PR/changed-evidence probes |
| 4: Product checkpoint contract | unverified/not reached on Mac | Validated example pair and preservation/recovery cases |
| 5: Review and finishing | unverified/not reached on Mac | All task evidence, fresh regression and whole-change review |

No prior Windows result is promoted to verified. Its execution ledger and
implementation state remain unavailable. The earlier fixture receipt remains
fixture evidence only; it does not prove a live checkpoint commit or Task 1.
There are no currently verified implementation tasks or known implementation
commits from the prior workspace.

## Portable execution procedure

This issue-specific correction uses the existing handoff approach and leaves
scratch under ignored `.sp-bp/work/`. At an interruption or machine/harness
handoff, preserve a tracked execution summary together with the evidence needed
to support every claimed verified task. Record plan/spec/probe and issue
revisions, actual workspace identity, input and evidence digests, implementation
commit identities where present, unresolved findings, and the first unsupported
task. An evidence pointer to ignored machine-local scratch is unavailable to
another host and cannot alone support a portable verified claim.

A local checkpoint is durable in Git only after its summary and necessary
supporting evidence are committed together. Before claiming another host can
resume, transport that commit through an authorized operation and verify arrival.
Do not confuse a proposed commit, uncommitted file, local accepted commit, and
remotely integrated checkpoint. Keep the source/verification identity separate
from the later checkpoint storage commit.

On another host, use current instructions, Git/GitHub state, artifact hashes,
and transported evidence to reconcile this summary. A path, branch, approval,
or result does not become current merely because it appears here. Missing or
changed inputs require revalidation; an unreadable predecessor stays unknown.
Never copy scratch into upstream or write to `.superpowers/`.

## Start here

The setup prerequisite passes for the evaluated Mac tuple. Recheck this
worktree's identity and current issue/artifact revisions, load writing-skills
and its required TDD background, then begin Task 1's frozen baseline. Capture
and score every original case before changing skill behavior. The old plan's
historical Windows preservation and unpublished-artifact statements are drifted;
the approved design, task order, immutable probes, review, and verification
contracts remain binding. Use native bookkeeping under the recorded exception.
