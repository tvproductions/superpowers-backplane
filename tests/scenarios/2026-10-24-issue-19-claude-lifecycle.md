# Issue 19 native recovery execution record

## Authority and identity

Operator approved the corrected recovery plan and native inline execution with a fresh final reviewer on 2026-10-25 in this conversation. Approved plan: `docs/superpowers-backplane/plans/2026-10-24-issue-19-claude-lifecycle-recovery.md`, SHA-256 `06542f5d4bb9856256f5a70ad63f35802c3315a774b37379d0940b139de316cd`. The approval does not publish a fixture, create its GitHub issue, integrate or release anything.

Authorized execution root: `/Users/jeff/Documents/Code/superpowers-backplane`. Recovery branch: `recovery/issue-19-native`, initially at `851d081e75be8ae4beb82b2cc4d353fc60dbe259`; baseline B remains published `b0d702f8821d6d29184118410ec6ff2d8fb63438`.

## Recovered work and correction

The existing branch `feat/issue-19-claude-lifecycle` is registered to `/Users/jeff/.local/share/opencode/worktree/1fb07c/issue-19-claude-lifecycle`. Its five commits are preserved as ancestors of this recovery branch: `89e3f60`, `0e3a048`, `2aa4ef0`, `51c2e9c`, and `851d081`. That worktree was observed clean and was read only; no mutation there is authorized by this recovery.

The earlier recovery examined main and the September27 draft but missed this unmerged October24 thread. Its statements that no #19 lifecycle observations were recorded were incomplete. `tests/scenarios/2026-10-24-claude-code-lifecycle.md` at `851d081` records local-directory install/repeat-install and preservation observations. The two `.prompt.txt` artifacts contain command records, not fresh Claude session responses. Preserve them unchanged at their recorded identities. Their unauthenticated profile and local-directory source do not establish hosted update, rollback, fresh discovery, conformance or completed #19 acceptance under this recovery plan.

The recovered plan also records and corrects an invalid concatenated candidate SHA. Only B is used here. Historical worktree/clone mutations remain historical claims; they are not repeated or retroactively authorized.

## Current preflight

- Fresh complete native #19 intake on 2026-10-25: OPEN, exactly `backplane:designing`, parent #1, closed blocker #18, blocks #11, no children or closing PRs, `updatedAt=2026-09-27T14:09:57Z`. Acceptance and scope match the approved recovery plan. The live body still says `Plan: not yet created`; publication and authorized artifact-link reconciliation remain pending.
- `gh auth status` succeeds using the existing keyring account. GitHub's commit endpoint resolves B exactly.
- Independent `.agents/superpowers` remains clean at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (v7.0.1); it is not changed by this work.
- PowerShell is absent from PATH and standard inspected install paths. A portable Microsoft release under ignored scratch will be digest-verified before use; no global installation is planned.
- New disposable profile: `.sp-bp/work/issue-19/profile`, scoped only through `CLAUDE_CONFIG_DIR`. The old OpenCode profile remains untouched. Authentication must be observed before any fresh model-session acceptance result.

## Task dispositions

| Recovery task | State | Evidence limit |
|---|---|---|
| 1 baseline/preflight | IN PROGRESS | Host/auth/tool and publication prerequisites remain |
| 2 hosted update | NOT RUN | Prior local-directory repeat-install is separately retained |
| 3 rollback/failure/uninstall | NOT RUN | No current recovery result |
| 4 conformance/lifecycle | NOT RUN | No fresh skill-tool transcript or authorized issue fixture |
| 5 integration/closeout | NOT RUN | No final review, integration or acceptance claim |

## Rulings

- Use a new recovery branch in the authorized root because the planned name is already checked out by OpenCode; preserve its commits and leave its worktree untouched.
- Use native file bookkeeping under ignored `.sp-bp/work/issue-19/` per the approved plan; never invoke reserved-namespace helpers.
- Treat previous install evidence as historical, source-specific observations. No previous task checkbox is translated into a new recovery-task pass.

No source/package/guide changes, GitHub mutation, publication, release, or completion is claimed by this record.

## Fresh prerequisite observations

New-profile `claude auth status --json` returned `loggedIn: false`, `authMethod: none`; initial plugin and marketplace inventories were both empty arrays. No login was attempted automatically and no credential was copied. The operator received the exact profile-scoped login command. These observations establish an unmet fresh-session prerequisite, not a conformance failure.

Microsoft PowerShell v7.6.8 arm64 portable archive was downloaded from `PowerShell/PowerShell` release v7.6.8 into ignored scratch. GitHub release API advertised SHA-256 `c16a3f433966c6fd5a9c8a660a95c92cb5dbc4b1813416501d1ba30ca160da32`; local `shasum -a 256 -c` returned OK before extraction. No system-wide install or PATH change was made.

RED guide observation: the guide's final section says pinned update, rollback and uninstall instructions are pending #19. This was observed before any guide edit; existing install/setup blocks are parsed only, not executed again.

Portable `pwsh -NoLogo -NoProfile` reports version `7.6.8`. All four existing guide PowerShell blocks were extracted verbatim and passed `[System.Management.Automation.Language.Parser]::ParseFile` with zero parse errors. No block was executed. This resolves the local parser prerequisite; the future lifecycle blocks still need actual replay.
