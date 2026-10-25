# Claude Code Lifecycle and Conformance Recovery Implementation Plan

> **For agentic workers:** Use `superpowers:executing-plans` for native execution after operator review and execution-method selection. Apply upstream review and verification gates; never invoke bookkeeping helpers that write into reserved namespaces.

**Goal:** Complete issue #19 with observed repeat-install, pinned-update, rollback, Backplane-only uninstall, preservation, five-check conformance, and native lifecycle evidence.

**Architecture:** Test the canonical Backplane package in one authenticated disposable Claude profile with independently installed upstream Superpowers. Use two immutable Backplane source revisions for update/rollback and a separate useful documentation contribution for issue-lifecycle verification. Keep fixture-only version changes out of integrated product source.

**Tech Stack:** Markdown, Git, GitHub CLI, Claude Code native plugin CLI; PowerShell only for replaying the existing installation guide. No consuming-project runtime is introduced.

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` (blob `a790d953691d178f711757e9164afb60932eb65a`) and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` (blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`).

**Status:** DRAFT FOR REVIEW. Replaces the September27 draft only after approval. No execution, fixture publication, GitHub mutation, integration, or release is authorized by saving this document.

## Recovery anchors

- Work item: https://github.com/tvproductions/superpowers-backplane/issues/19; live intake on 2026-10-24: OPEN, `backplane:designing`, `updatedAt=2026-09-27T14:09:57Z`, parent #1, closed blocker #18, blocks #11, no closing PRs. Acceptance and scope match the original draft.
- Preserved draft: `docs/superpowers/plans/2026-09-27-claude-code-lifecycle-and-conformance.md`, blob `a98238588e8bea8f4017edabeeaa8e31297aa8d5`.
- Recovery source: `docs/superpowers/handoffs/20260927T165620Z-issue-19-claude-lifecycle-plan-review.md`. It reports conditional fixture decisions and pending plan approval; those assertions do not supply current mutation authority.
- Observed planning workspace: `/Users/jeff/Documents/Code/superpowers-backplane`, clean `main` at `b0d702f8821d6d29184118410ec6ff2d8fb63438` before this draft; independent upstream clean at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (v7.0.1), active discovery through `.agents/skills/superpowers`.
- Active convention source: `.agents/skills/superpowers/writing-plans/SKILL.md`, SHA-256 `a6c67c1900064347c2a329990dd3c555657c51c3ec53b259a08aa01a2c26139a`. Current upstream README installation guidance was read via `gh api`; discovery and skill reads succeed. These observations do not establish Claude installed-package conformance.
- Claude Code 2.1.310 is available. Update help requires restart; marketplace-add accepts URL/path/GitHub sources; strict validation is available. PowerShell was not found on PATH. Disposable-profile authentication and source-pinning behavior remain unverified.

## Global Constraints

- Follow current AGENTS.md and the approved specifications. Remain language-neutral; preserve native issue hierarchy/dependencies and use `gh` for GitHub operations. No Projects, IssueOps, additional runtime, or release work.
- Before every Git mutation, verify `git rev-parse --show-toplevel` equals `/Users/jeff/Documents/Code/superpowers-backplane`. The #31 worktree exception does not apply to #19. Use the branch sequence below in this authorized standalone root; no additional Git checkout or worktree is needed. Do not silently reuse an old Windows path or mutate another checkout.
- Never write to `.superpowers/` or directly edit shipped upstream, discovery targets, or installed plugin-cache files. Native Claude package operations may manage only their own Backplane cache inside the disposable profile; upstream remains unchanged. Use native file bookkeeping. Disposable non-Git scratch belongs under ignored `.sp-bp/work/issue-19/`; tracked plans belong under `docs/superpowers-backplane/plans/`.
- Package commands run only with an explicitly selected disposable `CLAUDE_CONFIG_DIR`; record its resolved path on every invocation. Do not copy credentials or fall back to the normal profile. Authentication is an external prerequisite; no repeated sign-in loops.
- Keep upstream separately identifiable and unchanged throughout Backplane lifecycle operations. Record its source, observable version/revision, required skills, and before/after preservation.
- Prior and candidate installation identities are immutable full 40-character commits verified through the expected GitHub repository. A temporary branch is transport only; never treat its moving name as the selected installed revision.
- Before publishing a fixture or creating a disposable issue, show the exact local diff/body, immutable source strategy, retained-evidence strategy and cleanup scope for operator approval. Conditional historical assertions are insufficient. No tags, releases, or remote repository creation.
- Record PASS/FAIL/UNKNOWN for each criterion and seam. A required FAIL or UNKNOWN blocks submission/completion. Keep historical results at their original identities; no inferred predecessor completion.
- One current Backplane label on each open tracked test issue; preserve unrelated labels. Status and selection are read-only. Package operations preserve all GitHub issue state.
- #19 does not close #11 or establish complete-stack/external-adopter acceptance.

## Fixed source, workspace and update decisions

### Source identities and final applicability

- Baseline **B** is `b0d702f8821d6d29184118410ec6ff2d8fb63438`, the current published integration source at plan recovery. Verify its remote availability and record the canonical skills/references and three package-manifest hashes before testing. An old #18 profile is reusable as an authenticated container only: install and verify B before collecting any #19 evidence.
- Fixture **F** is one commit directly based on B, with only the three product-version changes to `0.1.1` and the README marker specified in Task 2. Record F's actual full SHA after creation; no invented SHA. B and F have identical canonical skills/references and upstream inputs. The update assertion proves F; rollback and full conformance prove B.
- Delivery **D** contains only the approved recovery plan, reviewed guide, fixture-plan and evidence changes on top of B. No canonical skills/references, package manifests, host configuration or upstream input may change under this plan. Compare their hashes at final integration. If any changes, invalidate the affected evidence and revise the test matrix before acceptance. Guide-only changes require final exact-command replay, not an unsupported claim that every file in D was previously tested as B.
- The receipt must separately identify B, F, the tested guide commit, the documentation-fixture integration commit and final D. A change to unrelated documents does not by itself invalidate unchanged installed-skill evidence.

### Branch sequence inside the authorized root

All branch changes below occur at `/Users/jeff/Documents/Code/superpowers-backplane`, after exact-root validation and a clean tracked worktree. Use new branch names only after checking for collisions; never overwrite an existing ref. Before switching, commit only the current slice's bounded files. Keep profile/catalog scratch under ignored `.sp-bp/work/issue-19/`, which survives switches.

1. Create `feat/issue-19-claude-lifecycle` from B. Save the approved recovery plan and tracked progress/evidence there. Keep this branch as the implementation thread.
2. From a clean saved implementation branch, create `test/issue-19-update-fixture` directly at B in the same root. Apply only the prescribed version/README patch, validate, commit F, then switch back to `feat/issue-19-claude-lifecycle`. Record `git diff B F` as a tracked patch under `tests/scenarios/fixtures/issue-19-update.patch` and the F identity in the evidence. Do not merge/cherry-pick F onto implementation or main. Publish F only after exact-diff approval. Retain its local and authorized remote branch for replay; deletion is separately scoped cleanup, never automatic.
3. Run Tasks 2–3 with Claude fetching B/F from GitHub into its disposable cache. These are host-managed copies, not agent-mutated Git workspaces. Root working files remain on the implementation branch.
4. At Task 4, commit all implementation work before switching. Create `test/issue-19-doc-lifecycle` from current verified main (which must contain B), in this same root. Commit only the useful paragraph and its bounded fixture plan there; no unfinished implementation evidence or F bytes. Obtain review and authorized integration for this small contribution, verify arrival, then close its disposable issue.
5. Switch back to the implementation branch and merge the verified documentation-fixture integration commit, preserving earlier evidence identities. Resolve any guide conflict by retaining the reviewed paragraph plus the tested lifecycle commands, then replay the resulting lifecycle blocks and parse all guide blocks. Complete #19's separate review and integration from the implementation branch. Keep all branches until accepted finishing/cleanup decisions.

### Exact hosted-plugin pinning route

Use a dedicated local catalog at `.sp-bp/work/issue-19/catalog/.claude-plugin/marketplace.json`; it is configuration for this disposable test profile, not the repository's shipped catalog. Set `name` to `superpowers-backplane`, `description` to `Issue 19 pinned hosted-plugin lifecycle fixture`, `owner.name` to `tvproductions`, and one plugin entry with `name` `superpowers-backplane`, description `Pinned Backplane lifecycle fixture`, and this source object:

```json
{
  "source": "github",
  "repo": "tvproductions/superpowers-backplane",
  "sha": "b0d702f8821d6d29184118410ec6ff2d8fb63438"
}
```

Omit catalog plugin `version`: the fetched package manifest owns it. Initially `sha` is B; change only that value to F for update and back to B for rollback. Validate each catalog state and archive its exact JSON/digest in tracked evidence. The local catalog contains no plugin files and cannot satisfy a package-content check by loading edited root files; the plugin source must be fetched from GitHub at the selected SHA. Keep the shipped `.claude-plugin/marketplace.json` at `source: "./"` unchanged in B and D. The consumer guide must explain this explicit pinned hosted-source route separately from its existing local-directory installation.

Run the following sequence with the selected disposable `CLAUDE_CONFIG_DIR` set in the process environment; resolve the catalog path before invocation. Never register this test catalog in the normal profile. If a reused disposable profile already has the same marketplace name, choose a fresh profile rather than remove unknown shared state.

1. Validate the B catalog with `claude plugin validate --strict <absolute-catalog-root>`; register with `claude plugin marketplace add <absolute-catalog-root> --scope user`; install with `claude plugin install superpowers-backplane@superpowers-backplane --scope user`. Record fetched B identity and preservation snapshots. Repeat the install command to test idempotence; no duplicate registration is required.
2. After F is published and verified, set catalog `source.sha` to F and validate. Run `claude plugin marketplace update superpowers-backplane`, then `claude plugin update superpowers-backplane@superpowers-backplane --scope user`. Restart and prove F's installed source/version, README marker, expected file hashes and actual fresh skill loads. A local catalog refresh alone is not a package update. Capture any no-op or source-resolution failure before repair; do not silently replace this route with local file loading.
3. Restore catalog `source.sha` to B and validate, then refresh the named marketplace. For rollback use explicit Backplane-only uninstall followed by install from the B-pinned catalog: `claude plugin uninstall superpowers-backplane@superpowers-backplane --scope user`, then `claude plugin install superpowers-backplane@superpowers-backplane --scope user`. Snapshot after uninstall and after reinstall separately; restart and prove B restoration. Do not depend on the update command supporting a version downgrade.
4. For the distinct uninstall row, uninstall Backplane again, verify absence and preservation, then reinstall from the still B-pinned catalog as explicit test restoration. Retain the catalog and unrelated marketplace entries. No marketplace removal is needed.

This is a selected documented strategy, not a claimed live-host pass. Any failure of this exact route is recorded against the responsible operation before a reviewed correction. Primary contract: https://code.claude.com/docs/en/plugins/marketplace-reference (separate marketplace and plugin sources; GitHub plugin `sha` pins a full commit).

## Review Focus

1. A successful update exit with unchanged content must fail the update row. Task 2 checks version, full source SHA, content marker, skill digests, and fresh discovery.
2. An unavailable prior revision must stop replacement. Tasks 1 and 3 establish its availability and prove restored identity rather than version alone.
3. Shared marketplace entries and unrelated plugins must survive removal. Tasks 1 and 3 include preservation sentinels and immediate comparisons.
4. CLI or source-pinning drift must be resolved before live operations. Tasks 1 and 2 verify help, current primary docs, catalog source resolution and exact installed bytes; unavailable pinning stays UNKNOWN.
5. A simulated lifecycle or premature issue closure must not count as observed completion. Task 4 captures actual native states and requires review, integration and fresh verification before closure.

## Files and evidence

- Modify `docs/installing-claude-code.md`: only lifecycle commands proved by replay, plus the useful fixture clarification below.
- Create `tests/scenarios/2026-10-24-issue-19-claude-lifecycle.md`: per-criterion score matrix, source identities, preservation results, review dispositions and integration receipt.
- Create `tests/scenarios/fixtures/issue-19-update.patch`: exact B-to-F fixture delta, retaining commit identity in the scenario receipt.
- Create `tests/scenarios/transcripts/2026-10-24-issue-19-claude-lifecycle.md`: exact redacted command/prompt/response observations; split into referenced companion files if necessary.
- Create `docs/superpowers-backplane/plans/2026-10-24-issue-19-lifecycle-fixture.md`: bounded authority for the disposable documentation issue, after its actual URL/revision exists.
- Scratch body/snapshots: `.sp-bp/work/issue-19/`. Never rely on ignored scratch as the sole recovery record.

### Task 1: Establish the baseline and executable host contract

**Interfaces:** consumes #17/#18 package, guide and setup evidence; produces an authenticated isolated baseline, exact prior SHA and preservation inventory for Tasks 2–4.

- [ ] Refresh complete native #19 intake with all fields from `skills/managing-superpowers-backlog/references/github-issue-contract.md`. Reconcile timestamp/body/graph drift. After plan approval, link the approved plan and its consumed revision through the authorized backlog workflow before readiness/execution transitions.
- [ ] Establish the guarded feature-branch workspace. Verify `.sp-bp/work/` is ignored before using it. Record branch, HEAD, origin and root in tracked evidence.
- [ ] Read current official Claude installation, marketplace, manifest and CLI documentation. Capture `claude --version`, marketplace/update/uninstall/validate help, `gh auth status`, full native intake, and label/closure help. Resolve syntax differences before package mutation.
- [ ] Select an existing authorized disposable profile only if its current path, auth and inventory are verified; otherwise prepare an isolated profile and report the authentication prerequisite. Record normal-profile preservation without exposing credentials.
- [ ] Install and verify baseline B through the exact catalog route above; reject an older profile revision as the test baseline. Resolve one installed Backplane identity and an independent authoritative upstream package. Record plugin IDs/scopes/sources, exact prior Backplane SHA/version, upstream version/revision, loaded skill roots and digests. Verify the prior SHA remains available through `gh api` before replacement.
- [ ] Capture immediate baseline inventories, unrelated plugin/marketplace entries and user-file sentinel hashes, upstream state, repository refs/history and complete #19 JSON. Account for host session metadata explicitly. Snapshot after each later operation before repair.
- [ ] Record the RED observation: the guide currently leaves lifecycle paths pending and no #19 scored lifecycle evidence exists. Require PowerShell for parsing existing guide blocks and executing the new lifecycle blocks; the current host lacks `pwsh` on PATH. Resolve that prerequisite before the first live lifecycle operation. Do not execute the existing clone/checkout bootstrap blocks in another Git root: those installation/setup seams belong to #17/#18 and are not claimed as freshly replayed here. The new lifecycle route uses the disposable catalog and native host-managed fetches only.

### Task 2: Prove repeat installation and a real pinned update

**Interfaces:** consumes Task 1 baseline; produces distinct prior/candidate installed identities and replayed guide commands.

- [ ] Replay repeat install in the isolated profile using current supported commands. Require one effective Backplane identity, unchanged skill hashes, separate upstream, immediate preservation comparison, and actual three-skill tool loads in fresh Claude sessions.
- [ ] Prepare a local reviewable fixture patch: change only product versions in `plugin.json`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` from verified baseline `0.1.0` to fixture `0.1.1`, plus append `Issue-19 update fixture: candidate content identity.` to the fixture source's `README.md`. Keep canonical skills and their references unchanged. The packaged README marker supplies distinguishable content without altering skill behavior.
- [ ] Verify all actual product-version locations before patching; keep schema versions unchanged. Run `claude plugin validate --strict <fixture-path>`, inspect the complete fixture diff and digest set, and prepare its source/pin/rollback commands. Construct F on the same-root fixture branch defined above; never create or mutate another Git root.
- [ ] Present the exact fixture diff and publication/retention strategy for approval. After authorized transport, verify remote full-SHA availability. Retain the exact fixture commit and supporting patch/digests for audit; never merge or tag its fixture-only bytes. Deleting a branch cannot be the sole retention strategy.
- [ ] Execute the exact B-to-F catalog sequence above. Record both catalog JSON states and fetched package identities. A source-resolution failure stops this row for a bounded correction; it does not authorize choosing another installation mechanism during execution.
- [ ] Refresh the Backplane marketplace, run `claude plugin update superpowers-backplane@superpowers-backplane --scope user`, and restart as required by observed help. Require candidate SHA/version, the exact packaged README marker, all expected installed digests and fresh direct loads of upstream using-superpowers and both Backplane skills. A local-directory in-place edit or version-only observation is insufficient.
- [ ] On cache/version/content mismatch, record FAIL before repair, preserve/restore the baseline, and investigate the failing resolution step. Write only observed successful commands to the guide and replay them from the documented baseline.

### Task 3: Prove rollback, failure preservation and removal

**Interfaces:** consumes the installed candidate and baseline; produces verified restored identity, preservation results and replayed recovery/removal guide sections.

- [ ] Restore B using the catalog SHA reset, named marketplace refresh, explicit uninstall and reinstall sequence above. Restart; require exact baseline version/digests, absence of the fixture marker, and fresh three-skill loads. Compare upstream, unrelated entries/files, history and issue state immediately.
- [ ] Stage an unverifiable candidate source in disposable scratch and run the guide's preflight. Require rejection before verified installation changes. If host replacement precedes failure, record that fact and execute the documented restoration path; prove the prior identity and fresh discovery before continuing.
- [ ] Run Backplane-only uninstall in the isolated profile. Require Backplane absent in inventory and fresh discovery, upstream still available, unrelated plugins/marketplace entries and files unchanged. Remove a marketplace only when it owns no unrelated entry. Reinstall the recorded prior as a separate restoration and recheck three-skill discovery.
- [ ] Write and replay the exact rollback, failed-candidate and uninstall commands in the guide. Parse all guide PowerShell blocks and execute the actual new lifecycle blocks through the verified replay route; do not rerun the separate clone/checkout bootstrap. Mark unsupported or unobserved outcomes UNKNOWN rather than substituting narrative.

### Task 4: Prove installed-package conformance and useful issue lifecycle

**Interfaces:** consumes restored installed package; produces five named scores and observed native lifecycle evidence for a separately reviewed documentation fixture.

- [ ] Inspect installed skills and references for structure, names, resolvable links, canonical source identity and placeholders; score `skill-structure`.
- [ ] Run the existing exact prompts/rubrics from `2026-08-16-native-issue-intake-green.md`, `2026-08-16-lifecycle-transition-refactor.md`, and `2026-08-16-superpowers-installation-refactor.md` in fresh Claude sessions. Capture actual skill tool loads and unedited responses; score every expectation for `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions` and `superpowers-installation`. Missing observations remain UNKNOWN.
- [ ] Run status and selection against an existing issue with full native before/after JSON comparisons. Require zero mutation and no invented priority. Include changed-updatedAt reconciliation that cannot silently approve a stale plan.
- [ ] Prepare the useful fixture body locally with the complete leaf headings. Objective: add an `Installation source and update verification` paragraph to `docs/installing-claude-code.md` explaining that local-directory file loading does not prove hosted update, and that update/rollback evidence must include immutable source identity and post-restart discovery. Allowed scope: that paragraph plus its fixture plan; no package/version changes. Acceptance: reviewed paragraph on integrated main, consistent with observed Task 2/3 behavior. Verification: exact integrated paragraph bytes and the supporting source-resolution observations. Present the exact body/diff before fixture creation.
- [ ] After explicit fixture authorization, create the disposable issue with `gh issue create --body-file .sp-bp/work/issue-19/fixture-body.md`, documentation and backlog labels. Capture actual URL/revision/native relationships. Write and review its bounded fixture plan before readiness; do not fabricate an issue number or approval. Use the same-root documentation-fixture branch sequence above; integrate this small contribution before final #19 review, keeping its immutable contribution identity distinct from final D.
- [ ] In fresh Claude sessions exercise actual designing, ready, active, blocked/resume, review, and requested-change return. Use a real recorded blocker/release condition and a real review correction to the paragraph. Capture full before/after native intake at each step; require one lifecycle label while open and preservation of documentation label. Dry runs do not count.
- [ ] Review and integrate the useful documentation contribution through the authorized branch workflow. Freshly verify its integrated bytes and applicable checks before completed closure; fetch and record actual closed reason and absence of lifecycle labels. Keep #19 and #11 open for their independent gates.

### Task 5: Review, integrate and assess #19

**Interfaces:** consumes Task 1–4 evidence; produces reviewed integrated #19 acceptance, leaving #11 final acceptance separate.

- [ ] Map every live #19 acceptance criterion and verification seam to exact evidence/transcript identities and PASS/FAIL/UNKNOWN. Include each lifecycle operation's immediate preservation results, five named scores and every native-state scenario. Any mandatory FAIL/UNKNOWN blocks submission.
- [ ] Run strict package validation, all-guide-block parsing and new-lifecycle-block replay, `git diff --check`, full #19 intake and scope review. Verify no upstream/reserved-namespace changes and no fixture-only version/marker in the integration change. Commit only bounded source/docs/evidence after root validation.
- [ ] Obtain fresh whole-change review through the selected execution workflow; resolve Important/Critical findings and rerun affected seams. Record lower-severity dispositions explicitly. Submit/transition to review only when evidence supports it; publication/integration remain subject to operator authority.
- [ ] After authorized integration, reconcile the exact tested package/guide/evidence bytes with integrated main. Rerun affected seams for changed inputs; require fresh strict validation, guide parsing, full intake and installed-package three-skill discovery. Historical unaffected evidence must name its source identity and applicability limit.
- [ ] Apply PR-closeout/satisfaction guidance to integrated #19. Close completed only when every required row passes and publication/arrival is verified. Leave #11 open; no release or broader adoption-readiness claim.

## Plan review and execution handoff

Local planning validation: the exact B-pinned catalog above passed `claude plugin validate --strict` on Claude Code 2.1.310 in a temporary non-Git directory; no marketplace was registered and no plugin was installed. The corrected draft passed whitespace validation. These are schema/document checks, not update/rollback execution results.

Re-audit of the three recovery findings: the catalog schema and explicit update/rollback sequence replace the deferred mechanism; all agent Git mutations use named branches in the authorized root; B/F/D identities and final applicability checks replace the unspecified existing baseline. Native package behavior still requires live execution, and authentication/PowerShell remain explicit prerequisites.

Self-review: all three #19 acceptance criteria map to Tasks 2–4; preservation and identity seams map to Tasks 1–3; native labels/closure and five checks map to Task 4; accepted integration maps to Task 5. The five review-focus conditions each have an explicit check. The old draft and predecessor evidence are preserved unchanged.

Review this corrected plan and select an execution approach before live work. Native inline execution is recommended because package operations share one evolving disposable profile; a fresh whole-change reviewer still checks the resulting delivery. Approval must identify whether it also authorizes the proposed hosted fixture transport and disposable-issue lifecycle; exact fixture bytes and commands must be reviewable before those actions. No approval is inferred from time elapsed or historical handoff assertions.

Primary sources checked during recovery: https://github.com/obra/superpowers#installation ; https://code.claude.com/docs/en/plugin-marketplaces ; https://code.claude.com/docs/en/plugins-reference . Recheck current host command/source contracts at Task 1 before mutation.
