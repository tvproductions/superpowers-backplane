# Claude Code lifecycle preflight baseline for #19

## Scope

This file is the Task 1 baseline evidence shell for issue #19
(`Verify Claude Code lifecycle and conformance`), observed 2026-10-24 in the
verified worktree
`/Users/jeff/.local/share/opencode/worktree/1fb07c/issue-19-claude-lifecycle`
on `feat/issue-19-claude-lifecycle`, repository origin exactly
`https://github.com/tvproductions/superpowers-backplane.git`. Observation
spanned two rounds: the initial round at base
`89e3f60841de27e689fc824cb9f5a07b7174a66e` (brief steps 1–2 plus the
candidate-identity diagnosis below) and the resumed round after the
candidate-revision ruling, at `2aa4ef0090011d68352e61e0004254d67a770987`
(corrected plan) on top of the blocked evidence commit `0e3a048`. Issue #19
is OPEN with exactly one lifecycle label, `backplane:designing`, at revision
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
check remains `UNKNOWN` until a later task records fresh host evidence. This
file records only identities, preflight probes, and preservation.

## Candidate revision provenance

The originally dispatched brief and plan named the candidate as
`b0d702f919f3afdbede1710ec3ca109164523ff9`. That 40-character string matches
no commit: `gh api .../commits/b0d702f919f3afdbede1710ec3ca109164523ff9`
returned HTTP 422 `No commit found for SHA`, a fresh clone could neither
detached-checkout nor `cat-file` it, and
`git rev-parse --disambiguate=b0d702f9` returned no object at all locally.
The value was the plan's own seven-character prefix `b0d702f` joined to the
33-character tail of the real prior revision
`d774361919f3afdbede1710ec3ca109164523ff9`; the full blocked diagnosis is
preserved at commit `0e3a048`. The dispatcher ruled the mangled string
invalid and corrected the plan (commit `2aa4ef0`, replacing all four
occurrences). The only valid candidate is
`b0d702f8821d6d29184118410ec6ff2d8fb63438` — the published remote `main`
tip — and the mangled string must not be used anywhere in this scenario.

## Host and source identities (brief step 1)

Observed 2026-10-24, all read-only, identical in both rounds:

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
fields, re-run with identical values in both rounds:

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
- Identity digest of the intake: SHA-256 of the complete returned JSON file
  `7e15799de773555bfe2ac572dee5c1878c8d5f8fb014e1564e6a264e72c08dbe`.

These identities match the plan's expectations for Claude Code operation,
upstream placement, authentication, and the #19 open/designing state. They
are baseline observations only; they do not score any lifecycle check.

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

Re-checked after every step 3 probe (including `claude plugin validate
--strict`), the profile still reports `[]` marketplaces and `[]` plugins;
it contains only host-generated state (`.claude.json` and a `backups/` copy
of it). No plugin or marketplace was installed into it by this task. The
profile is retained in place as the durable input for Tasks 2–6.

Normal Claude profile (`~/.claude`) preservation, hashed before the first
`claude` command of each round and re-checked after the last one:

| File | SHA-256 (before = after, both rounds) |
|---|---|
| `settings.json` | `b6cfd9420f69fec8e5a56591820136da8e2e5dccd80939dfc37b85ef48c41581` |
| `plugins/installed_plugins.json` | `3238f139f77c8a7dd90d3d1018862c9f4c3b99808e7d26c7ce0fee6f1557f507` |
| `plugins/known_marketplaces.json` | `9cbdcf550a4ed248f5ee04cf02b5f371aaa278e30dce1de926c6e65a6c911b3e` |

All three hashes are unchanged, so the normal profile was not mutated by any
child command in either round.

## Pinned Backplane source verification (brief step 3)

Verified 2026-10-24 against the corrected candidate
`b0d702f8821d6d29184118410ec6ff2d8fb63438` in the unused temporary parent
`/private/var/folders/7y/cvcpqqnj2_52yy4wl780kmqc0000gn/T/opencode/backplane-claude-19-source-7b44fc2e7a0108a6`
(the superseded blocked-round clone parent was removed after the ruling; it
was scratch and never an input). Observed, in order:

1. `gh repo clone tvproductions/superpowers-backplane <parent>/superpowers-backplane`
   → exit 0.
2. `git -C <backplane-checkout> checkout --detach b0d702f8821d6d29184118410ec6ff2d8fb63438`
   → `HEAD is now at b0d702f docs: sync issue 31 assessment and agent
   workflow`, exit 0.
3. Origin is exactly
   `https://github.com/tvproductions/superpowers-backplane.git`; HEAD is
   `b0d702f8821d6d29184118410ec6ff2d8fb63438`; `git status --porcelain=v1`
   is empty (clean), re-confirmed after validation.
4. `gh api repos/tvproductions/superpowers-backplane/commits/b0d702f8821d6d29184118410ec6ff2d8fb63438 --jq .sha`
   → `b0d702f8821d6d29184118410ec6ff2d8fb63438`, exit 0; the same endpoint's
   commit message is `docs: sync issue 31 assessment and agent workflow`.
5. `claude plugin validate --strict <backplane-checkout>`, run with the
   disposable profile as `CLAUDE_CONFIG_DIR` → `✔ Validation passed`,
   exit 0. The validator also printed advisory plugin-directory findings
   that it explicitly stated do not change the strict verdict: a
   submission-level `LICENSE_MISSING` refusal, an `ICON_MISSING` warning,
   and a README install-line suggestion. Those advisories are pre-existing
   repository facts recorded here verbatim in summary; nothing was changed
   in response to them by this task, and no package manifest, guide, or
   skill byte was modified.
6. Pinned-file SHA-256 values at the detached candidate:

| File | SHA-256 |
|---|---|
| `.claude-plugin/plugin.json` | `32bbd2859083522cf3fc040b45864a1de6fc1fcd370c5bf30c21f87086486565` |
| `.claude-plugin/marketplace.json` | `e9903b166d7fe302a51280a75d613d019a8945d8bee23a77819bb2e2ae839da1` |
| `docs/installing-claude-code.md` | `eb7650b312cf64a7cbe07ee0ca14bc19d77dcf40a18f6720a0717b827c117dbd` |
| `skills/managing-superpowers-backlog/SKILL.md` | `168d5dffa43e89fae7249859f5758f3a46e53f03ea72e9bf1686983d49808f16` |
| `skills/managing-superpowers-handoffs/SKILL.md` | `a6052755128be9c7d268d71241dd389b9bf1c720834e47e61cbf9535f4ca92de` |

Consistency cross-checks: the `plugin.json`, `marketplace.json`, and both
`SKILL.md` digests equal the values previously published in
`tests/scenarios/2026-09-20-claude-code-setup.md` (the two manifests) and
`tests/scenarios/2026-10-24-superpowers-v7.0.1-compatibility.md` (both
skills). The `docs/installing-claude-code.md` digest differs from the #18
record's guide hash because the guide has legitimately evolved since; it is
the value at this candidate revision.

The pinned source is therefore published, clean, detached exactly at the
selected candidate revision, and passes strict plugin validation. The
clone is retained in place, still detached at the candidate, as the
marketplace source input for Tasks 2–4.

## Preservation

- GitHub: only read-only operations (`gh auth status`, `gh issue view`,
  `gh repo clone`, `gh api` GETs); no issue, label, PR, release, or
  repository mutation occurred. Issue #19 remains OPEN/`backplane:designing`
  at `2026-09-27T14:09:57Z`.
- Upstream: only read commands ran against `.agents/superpowers`; its HEAD,
  origin, and clean status are unchanged, and it was not updated or
  relocated.
- No write occurred under `.superpowers/` (verified absent at the main
  repository root, inside the upstream checkout, and in the feature
  worktree), and no shipped upstream file was modified. No helper that
  writes there was invoked.
- Normal Claude profile unchanged (hash table above); the disposable
  profile is isolated, still empty, and unauthenticated.
- No credential value was copied or recorded at any point.
- The feature worktree changes only the two evidence files named by the
  task brief; `git status --porcelain=v1` was clean before each round's
  edits.

## Disposition

Task 1 is complete: brief steps 1–4 are satisfied with the expected
identities, the corrected candidate
`b0d702f8821d6d29184118410ec6ff2d8fb63438`, the empty disposable profile,
and the pinned source verification recorded above. Baseline inputs
produced for Tasks 2–6: the disposable profile path, the pinned clone path
(detached at the candidate), and the five pinned-file SHA-256 values.
Consistent with the plan, no lifecycle result is claimed yet, and no
issue-state change, publication, release, or upstream mutation occurred.
