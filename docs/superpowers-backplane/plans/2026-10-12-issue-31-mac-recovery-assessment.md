# Issue #31 Mac recovery assessment

Observed: 2026-10-12T09:35:57Z. This is a diagnostic reconciliation record,
not an execution ledger, completed session handoff, or accepted product
checkpoint. It supplies no new execution, installation, or publication
authority. GitHub and the approved specification/plan retain their authority.

Selected handoff: No execution handoff was recovered. The October 11 scope
discussion handoff predates issue #31 and its approved implementation plan;
it is historical discussion context, not an execution successor.

Current anchors: Repository `/Users/jeff/Documents/Code/superpowers-backplane`,
origin `https://github.com/tvproductions/superpowers-backplane.git`, branch
`main`, HEAD `387f6e475624ba70c4c1f9bd3d71f85e55977a50`.
[Issue #31](https://github.com/tvproductions/superpowers-backplane/issues/31)
was observed at `updatedAt=2026-10-12T01:29:48Z`, OPEN/Feature with exactly one
`backplane:active` label, no parent, children, blockers, blocking edges, or
closing PRs.

Confirmed claims: The local approved plan and specification match the issue's
recorded SHA-256 identities exactly. Their files and the frozen probe contract
were published through [PR #32](https://github.com/tvproductions/superpowers-backplane/pull/32).
The Windows source commit is available locally and is an ancestor of current
HEAD. These observations recover planning authority, not execution progress.

Drifted claims: The issue and plan still describe the planning artifacts as
unpublished; PR #32 now contains them. Historical Windows roots, the dirty-root
preservation assumptions, and the recorded native worktree are not this Mac's
observed execution environment. Historical compatibility evidence does not
establish current Mac discovery or workflow compatibility.

Unverified claims: No task completion, implementation commit, baseline probe,
review result, or accepted execution checkpoint from the Windows worktree was
recovered. The operator confirmed that the execution records remain on that
machine and this session is on a Mac. Their contents remain unknown; neither
the active label nor missing Mac files proves that Windows work did not occur.

Next-step assessment: Recovery of the approved planning inputs succeeds.
Execution resumption does not: the prior task evidence and an operational
project Superpowers installation are unavailable. Task 1 is the first task
without supported completion evidence here, not a verified claim about where
the Windows execution stopped.

Bearing: VERIFY

Start here because: Preserve the matching approved inputs, correct the
cross-machine continuity gap, and establish Mac prerequisites and a separately
recorded execution identity before fresh task validation. Do not silently
recreate the Windows worktree or mark its work complete.

## Recovered artifact identities

Paths below are relative to the repository root and tracked at current HEAD.

| Artifact | Git blob | SHA-256 |
| --- | --- | --- |
| `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md` | `52998773470537fc0e921132d610c7687911ff3a` | `677bcc5ce2707781f0ee05c15306bd1be0587a801ca48699fba195722681bdb0` |
| `docs/superpowers-backplane/plans/2026-10-11-github-governance-bridges-implementation.md` | `738fd8f43c1d02a9843dab743a211787c429e610` | `ae05361badc5be68474b4fc5ea19de01f806b31e245c5f9e88be99e1da3e72f1` |
| `docs/superpowers-backplane/plans/2026-10-11-governance-probe-contract.md` | `9472b0f36020e4ff7935bb05bac5ac434001c61e` | `fc23cbae20160535f0836eff9920649c0dc78fe50b17ac3082904f2b38710f81` |

The plan's consumed issue revision is `2026-10-12T00:53:44Z`. The live revision
adds the recorded approval/workspace identities and the SP freshness ownership
clarification already present in the approved specification. Preserve the
approved files unchanged; reconcile their historical entry assumptions before
any execution. The disposition above is a current observation, not a rewrite of
their approval record.

## Recovery probes and limits

- `git status --porcelain=v1` was empty before this assessment's edits;
  `git worktree list --porcelain` registered only the Mac root on `main`.
- Native `list_worktrees` returned `data=[]`, `nextCursor=null`. No worktree
  creation was attempted.
- Full native issue intake, all remote branch pages, and PR history were read
  through authenticated `gh`. No issue-31 execution branch or PR was found.
- The current tracked tree contains the planning artifacts and compatibility
  records, but no governance implementation deliverables, execution ledger,
  or `.sp-bp/` checkpoint pair.
- Local Code/worktree file discovery and the local Codex thread inventory found
  no Windows execution records. Transcript matches for the recorded Windows
  worktree were from this current Mac session, not a recovered predecessor.
  These probes do not inspect the Windows filesystem or prove its files absent.
- Recorded Windows identity: native worktree
  `C:/Users/Jeff/.codex/worktrees/3a89/superpowers-backplane`, initially detached
  at `27679be948042cf2f6a698508ea34b19648eae71`. That exact workspace is not
  registered or accessible here. Do not reinterpret its path as a Mac alias.
- `.agents/superpowers`, `.agents/skills`, `.sp-bp/`, and `.superpowers/` were
  absent here. No files were written to them or to installed plugin caches.

## Superpowers prerequisite

UNMET SUPERPOWERS PREREQUISITE: The project checkout/discovery recorded in
`SUPERPOWERS.md` is absent. The separate cached
`superpowers@gzfactory-development` package is version 7.0.0, with its catalog
source `https://github.com/obra/superpowers.git` at
`bb92a77741419a4ab5f06e711a283343f1ada0c3`, but its current user configuration
has `enabled=false`. Its cached files are inspectable; that is not operational
active discovery or fresh conformance evidence.

Current upstream installation guidance was read through `gh api` from
[the upstream README](https://github.com/obra/superpowers#installation).
The handoff skill explicitly says, "Do not install, repair, or claim
compatibility" when its prerequisite is unmet. Formal RESUME therefore stops
with VERIFY; this diagnostic does not claim successful RESUME or supply a new
handoff target. No upstream repair was performed.

## Portability gap and proposed correction

The approved implementation procedure puts `progress.md`, task briefs, and
review packets under ignored `.sp-bp/work/`. Its resume rule depends on that
progress/evidence, yet no execution-boundary transport was recorded. The
product checkpoint pair planned for Task 4 has not been implemented and is
not a substitute for the missing task execution records. The existing handoff
contract also explicitly states that creating a handoff does not transport it.

The narrow correction is to use the existing handoff workflow at machine or
harness boundaries and require an explicitly transported, tracked execution
summary with its claim-supporting evidence references. Keep disposable scratch
under ignored `.sp-bp/work/`; do not turn it into the sole recovery source.
The summary must retain plan/spec/probe identities, issue revision, actual
source/workspace identity, task status and evidence digests, unresolved findings,
and the first task requiring revalidation. Evidence that has not been transported
must remain UNVERIFIED. Local tracking alone does not establish availability on
another host; transport and arrival verification are separate steps.

Demonstrate recovery from a second clean checkout with no predecessor's ignored
workspace. A changed input or missing evidence must require revalidation, while
the transported summary must identify the supported next step without access
to the original machine. This is a proposed execution-procedure correction,
not an approved change to the immutable plan or a new general handoff system.

For this Mac, a recovery decision may explicitly establish fresh execution from
the matching approved inputs, preserving all prior Windows task results as
unknown. Restore/confirm operational Superpowers through the documented
channel and applicable project authority, then establish an authorized Mac
isolation identity and revalidate Task 1 before claiming further progress.
Do not automatically reuse the Windows worktree exception for a new Mac path.

No Git commit, push, issue mutation, skill change, installation, implementation
probe, or worktree mutation was performed during this assessment.
