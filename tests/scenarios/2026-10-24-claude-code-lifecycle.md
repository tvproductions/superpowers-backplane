# Claude Code lifecycle preflight and source identity block for #19

## Scope

This file is the Task 1 baseline evidence shell for issue #19
(`Verify Claude Code lifecycle and conformance`), observed 2026-10-24 in the
verified worktree
`/Users/jeff/.local/share/opencode/worktree/1fb07c/issue-19-claude-lifecycle`
on `feat/issue-19-claude-lifecycle` at
`89e3f60841de27e689fc824cb9f5a07b7174a66e`, repository origin exactly
`https://github.com/tvproductions/superpowers-backplane.git`. Issue #19 is
OPEN with exactly one lifecycle label, `backplane:designing`, at revision
`2026-09-27T14:09:57Z`; no GitHub issue state was changed by this task.
Upstream Superpowers is the clean `v7.0.1` checkout at `.agents/superpowers`
(resolved at `/Users/jeff/Documents/Code/superpowers-backplane/.agents/superpowers`,
the ignored independent checkout; the feature worktree does not materialize
ignored upstream), commit
`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`, origin
`https://github.com/obra/superpowers.git`. The disposable Claude profile is
`/private/var/folders/7y/cvcpqqnj2_52yy4wl780kmqc0000gn/T/opencode/backplane-claude-19-9f1f8fbf7049931c`,
used only through `CLAUDE_CONFIG_DIR` for child commands.

**No lifecycle result is claimed yet.** No install, repeat install, pinned
update, rollback, Backplane-only uninstall, fresh-session discovery, or
conformance behavior has been run or scored in this scenario. Every such
check remains `UNKNOWN` until a later task records fresh host evidence.

**Task 1 is BLOCKED on the candidate source identity.** The approved plan and
the task brief name the published Backplane candidate as
`b0d702f919f3afdbede1710ec3ca109164523ff9`. That exact commit does not exist
on GitHub, in a fresh clone of the repository, or in any local object store
(verified below). No substitute revision was adopted: no candidate checkout,
`claude plugin validate --strict`, or pinned-file SHA-256 recording was
performed, and nothing in this file authorizes a later task input. The
disposition section names the exact ruling required before Task 2.

## Host and source identities (brief step 1)

Observed 2026-10-24, all read-only:

| Check | Observed |
|---|---|
| Claude Code | `claude --version` → `2.1.310 (Claude Code)`, exit 0 |
| Upstream HEAD | `git -C .agents/superpowers rev-parse HEAD` → `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` |
| Upstream origin | `git -C .agents/superpowers remote get-url origin` → `https://github.com/obra/superpowers.git` (authoritative) |
| Upstream status | `git -C .agents/superpowers status --porcelain=v1` → empty output, exit 0 (clean) |
| Upstream release (supplemental) | `git -C .agents/superpowers describe --tags --exact-match` → `v7.0.1` at HEAD |
| GitHub CLI | `gh auth status` → github.com, logged in as `ahuimanu` (keyring), active account, HTTPS Git protocol, scopes `gist, read:org, repo, workflow`, exit 0 |

Complete issue #19 native intake
(`gh issue view 19 --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`,
run from the verified worktree) exited 0 and returned all fifteen requested
fields:

- `number` 19; `title` `Verify Claude Code lifecycle and conformance`;
  `state` OPEN; `stateReason` empty (open issue); `issueType` null.
- `labels` exactly `[backplane:designing]`; no second lifecycle label.
- `parent` #1; `subIssues` totalCount 0 with no nodes;
  `subIssuesSummary` completed 0 of total 0.
- `blockedBy` exactly one node: #18 `Verify Claude Code setup and upstream
  adoption`, CLOSED. `blocking` exactly one node: #11 `Deliver and verify the
  Claude Code plugin installation surface`, OPEN.
- `closedByPullRequestsReferences` empty.
- `updatedAt` `2026-09-27T14:09:57Z` (the revision recorded by the approved
  plan); `url`
  `https://github.com/tvproductions/superpowers-backplane/issues/19`.
- Identity digests of the intake: SHA-256 of the complete returned JSON file
  `7e15799de773555bfe2ac572dee5c1878c8d5f8fb014e1564e6a264e72c08dbe`;
  SHA-256 of the `jq -r .body` field
  `79d181a4a992cb632fc046115b4dad2b5d5474b823d1650a4e6af1303c1d8c22`.

These identities match the approved plan's expectations for Claude Code
operation, upstream placement, authentication, and the #19 open/designing
state. They are baseline observations only; they do not score any lifecycle
check.

## Disposable Claude profile (brief step 2)

The profile directory
`/private/var/folders/7y/cvcpqqnj2_52yy4wl780kmqc0000gn/T/opencode/backplane-claude-19-9f1f8fbf7049931c`
did not previously exist and was created empty under the approved temporary
workspace on 2026-10-24. It was used only as `CLAUDE_CONFIG_DIR` for child
commands. No credential value was copied, read, or recorded.

Initial inventory, captured before any other profile use:

- `claude plugin marketplace list --json` → `[]`, exit 0.
- `claude plugin list --json` → `[]`, exit 0.
- `claude auth status --json` → `loggedIn: false`, `authMethod: none`,
  `apiProvider: firstParty`, `configDirectory` at the profile path, exit 1.
  The profile is therefore unauthenticated: no credentials were transferred
  from the normal profile. Any later authentication is a separately recorded
  host action by the task that needs it.

Re-checked after the step 3 probes, the profile still reports `[]`
marketplaces and `[]` plugins; it contains only host-generated state
(`.claude.json` and a `backups/` copy of it). No plugin or marketplace was
installed into it by this task.

Normal Claude profile (`~/.claude`) preservation, hashed before the first
`claude` command and re-checked after the last one:

| File | SHA-256 (before = after) |
|---|---|
| `settings.json` | `b6cfd9420f69fec8e5a56591820136da8e2e5dccd80939dfc37b85ef48c41581` |
| `plugins/installed_plugins.json` | `3238f139f77c8a7dd90d3d1018862c9f4c3b99808e7d26c7ce0fee6f1557f507` |
| `plugins/known_marketplaces.json` | `9cbdcf550a4ed248f5ee04cf02b5f371aaa278e30dce1de926c6e65a6c911b3e` |

All three hashes are unchanged, so the normal profile was not mutated by any
child command in this task.

## Pinned Backplane source and identity block (brief step 3)

The clone parent
`/private/var/folders/7y/cvcpqqnj2_52yy4wl780kmqc0000gn/T/opencode/backplane-claude-19-source-9f1f8fbf7049931c`
did not previously exist and was created for this task. Observed, in order:

1. `gh repo clone tvproductions/superpowers-backplane <parent>/superpowers-backplane`
   → exit 0. The clone's origin is exactly
   `https://github.com/tvproductions/superpowers-backplane.git`, its default
   branch is `main` at `b0d702f8821d6d29184118410ec6ff2d8fb63438`, and
   `git status --porcelain=v1` is empty (clean). `git ls-remote origin` in
   the clone reports remote `HEAD` and `refs/heads/main` both at
   `b0d702f8821d6d29184118410ec6ff2d8fb63438`.
2. `git -C <backplane-checkout> checkout --detach b0d702f919f3afdbede1710ec3ca109164523ff9`
   → `fatal: unable to read tree (b0d702f919f3afdbede1710ec3ca109164523ff9)`,
   exit 128. The pinned detach failed.
3. `git -C <backplane-checkout> cat-file -t b0d702f919f3afdbede1710ec3ca109164523ff9`
   → `fatal: git cat-file: could not get object info`, exit 128. The fresh
   clone contains no such object.
4. `gh api repos/tvproductions/superpowers-backplane/commits/b0d702f919f3afdbede1710ec3ca109164523ff9 --jq .sha`
   → HTTP 422
   `{"message":"No commit found for SHA: b0d702f919f3afdbede1710ec3ca109164523ff9",...}`,
   exit 1. GitHub does not serve that commit anywhere in the repository.
5. Local repository cross-checks
   (`/Users/jeff/Documents/Code/superpowers-backplane`, which additionally
   holds the feature branch):
   `git cat-file -e b0d702f919f3afdbede1710ec3ca109164523ff9` exits 1;
   `git rev-parse --disambiguate=b0d702f9` returns no object at all, while
   `git rev-parse --disambiguate=b0d702f882` returns exactly
   `b0d702f8821d6d29184118410ec6ff2d8fb63438`
   (`docs: sync issue 31 assessment and agent workflow`, the current remote
   `main` tip).
6. The unique published commit matching the plan's seven-character
   `b0d702f` prefix is therefore `b0d702f8821d6d29184118410ec6ff2d8fb63438`,
   confirmed independently by
   `gh api repos/tvproductions/superpowers-backplane/commits/b0d702f --jq .sha`
   → `b0d702f8821d6d29184118410ec6ff2d8fb63438`, by the fresh clone's
   `rev-parse`, and by `git ls-remote origin`.
7. The plan's Task 3 prior revision
   `d774361919f3afdbede1710ec3ca109164523ff9` is a real published commit
   (`docs: hand off adoption readiness after issue 31`), verified through
   the same `gh api` commits endpoint and the local log. The blocked
   candidate value is exactly `b0d702f` followed by the 33-character tail of
   that `d774361…` full SHA, which is the observed construction error: the
   plan's 40-character candidate string is not the full SHA of the commit
   its own seven-character prefix selects.

Because the exact required candidate identity is unverifiable, the remaining
brief step 3 actions were **not run**: no candidate detach was completed, no
`claude plugin validate --strict <backplane-checkout>` was executed, and no
SHA-256 values were recorded for `.claude-plugin/plugin.json`,
`.claude-plugin/marketplace.json`, `docs/installing-claude-code.md`, or the
two canonical `SKILL.md` files. Those records stay `UNKNOWN` here rather than
being fabricated against an unverified revision. The temporary clone remains
at its clean default-branch tip `b0d702f8821d6d29184118410ec6ff2d8fb63438`;
that state is an observation for the identity ruling, not an adopted
candidate.

## Preservation

- GitHub: only read-only operations (`gh auth status`, `gh issue view`,
  `gh repo clone`, `gh api` GET); no issue, label, PR, release, or repository
  mutation occurred. Issue #19 remains OPEN/`backplane:designing` at
  `2026-09-27T14:09:57Z`.
- Upstream: only read commands ran against `.agents/superpowers`; its HEAD,
  origin, and clean status are unchanged, and it was not updated or
  relocated.
- No write occurred under `.superpowers/` (verified absent at the main
  repository root, inside the upstream checkout, and in the feature worktree),
  and no shipped upstream file was modified. No helper that writes there was
  invoked.
- Normal Claude profile unchanged (hash table above); the disposable profile
  is isolated, still empty, and unauthenticated.
- The feature worktree changes only the two evidence files named by the task
  brief; `git status --porcelain=v1` was empty before they were created.

## Disposition

Task 1 baseline: steps 1 and 2 of the brief are complete with the expected
identities recorded above. Task 1 is **BLOCKED** at brief step 3: the
pinned candidate commit `b0d702f919f3afdbede1710ec3ca109164523ff9` does not
exist on GitHub, in a fresh clone, or locally, while the unique published
commit matching the plan's `b0d702f` prefix is
`b0d702f8821d6d29184118410ec6ff2d8fb63438`. Resuming requires an explicit
ruling that either corrects the plan/brief candidate revision or
authorizes the resolved identity; until then, every later task input in this
scenario remains `UNKNOWN` and no lifecycle success is claimed.
