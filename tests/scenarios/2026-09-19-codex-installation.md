# Codex Installation Surface: Issue #3

- Issue: https://github.com/tvproductions/superpowers-backplane/issues/3
- Approved design: `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`
- Approved plan: `docs/superpowers/plans/2026-09-19-codex-installation-surface.md`
- Execution branch: `feat/codex-installation-surface`
- Task 1 package commit: `8bfba888599568cc8f729ba6f0c030ace8e6377f`
- Issue #3 ready to active transition: `2026-09-19T19:37:32Z`

## Task 1: Root package and marketplace

### RED expectations

1. The repository must expose one root `plugin.json` with ID `superpowers-backplane`, version `0.1.0`, and the canonical `skills/` tree.
2. `.agents/plugins/marketplace.json` must be tracked while the independent upstream checkout and discovery junction remain ignored.
3. Codex must resolve exactly one `superpowers-backplane@superpowers-backplane` selector from this repository.

### RED observations (2026-09-19)

- Host: `codex-cli 0.155.1` on Windows PowerShell 7.6.6.
- `git check-ignore -v .agents/plugins/marketplace.json` returned `.gitignore:1:.agents/`, so the marketplace path was hidden.
- `plugin.json` and `.agents/plugins/marketplace.json` were absent.
- `codex plugin list --available --json` filtered to the Backplane selector returned `matching=0`.
- That catalog command exited 0 but warned that a remote plugin catalog request to `chatgpt.com` failed. The RED result establishes local absence only; the later GREEN check must inspect local resolution directly.
- Current canonical authored skills: `managing-superpowers-backlog` and `managing-superpowers-handoffs`.

### GREEN evidence

- Portable `plugin.json` and repository marketplace JSON parsed; names, version `0.1.0`, `./` source, `AVAILABLE`/`ON_USE` policy, and two canonical authored skill folders matched the plan.
- `.agents/superpowers` and `.agents/skills/superpowers` remained ignored. `git check-ignore -q .agents/plugins/marketplace.json` exited 1, and `git status --short --untracked-files=all` showed the marketplace file.
- `codex plugin list --available --json` from the repo root still returned `matching=0`. The current CLI considered only four already configured marketplaces; it did not automatically register this repository marketplace. This invalidated the plan's implicit CLI discovery assertion, not the package metadata.
- In disposable `CODEX_HOME=.superpowers/sdd/2026-09-19-codex-installation-surface/task1-codex-state`, `codex plugin marketplace list --json` initially listed no marketplaces. `codex plugin marketplace add <this repository root> --json` returned `marketplaceName=superpowers-backplane`, `alreadyAdded=false`, and the exact repository root. A following `codex plugin list --available --json` found exactly one `superpowers-backplane@superpowers-backplane` at version `0.1.0`.
- An attempted `Start-Process` probe with redirected stdout exited 1 with `stdout is not a terminal`; the successful disposable probe set `CODEX_HOME` only inside its PowerShell process and invoked `codex` directly. Task 3 must use a terminal-compatible isolated invocation for fresh sessions.

## Task 2: Codex install and setup guide

### RED documentation expectations (2026-09-19)

| Expectation | README observation | Result |
|---|---|---|
| Pinned Backplane installation command | README has no Codex package selector, Git ref, or install guide link. | FAIL |
| Explicit setup request | README does not tell the adopter to request Backplane setup in a Codex session. | FAIL |
| Upstream provenance check | README mentions only this repository's ignored development checkout, not an adopter's independently installed upstream package or sibling checkout. | FAIL |
| Fresh three-skill discovery | README has no new-session check for upstream `using-superpowers` and both Backplane skills. | FAIL |

The install guide does not yet exist. These four failures are documentation gaps before Task 2 edits.

### GREEN documentation evidence

- README links `docs/installing-codex.md`, which has an origin-checked Backplane checkout, a published SHA check through `gh api`, and pinned `codex plugin marketplace add ... --ref` plus the exact plugin selector.
- The guide states that package installation does not run setup, gives the exact Codex setup request, and requires independent upstream provenance plus fresh discovery of all three skills.
- The PowerShell install block parsed without errors. Running only its preflight on unpublished feature commit `8bfba888599568cc8f729ba6f0c030ace8e6377f` stopped before plugin mutation with `Backplane commit is not published at the expected origin` (GitHub HTTP 422).
- Read-only `gh` checks passed: authenticated account, 15/15 native issue fields on #3, label add/remove flags, and closure-reason flag. The installed development upstream checkout was `obra/superpowers` at tag `v6.4.1`, commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`, with all four required upstream skills; the latest stable release query also returned `v6.4.1`.
- The current user Codex profile listed no installed Superpowers plugin. This development checkout does not prove native package adoption; Task 3 must run that mode in an isolated profile.

## Task 3: Lifecycle evidence and open gates

- The user approved pushing `feat/codex-installation-surface` for immutable Git ref tests. GitHub resolved package commit `8bfba888599568cc8f729ba6f0c030ace8e6377f` and guide commit `6c26f0354b0bf231172a13327e2dc898b8b772b5`; neither is a release.
- The disposable archive and isolated Codex states are recorded in [host lifecycle](transcripts/2026-09-19-codex-host-lifecycle.md). CLI install, repeat install, fixture-only `0.1.1` update, `0.1.0` rollback, pinned Git ref switch and restore, and Backplane-only uninstall passed.
- The exact lifecycle commands in `docs/installing-codex.md` were run in a fresh disposable `state-guide`: preflight, candidate SHA, restored SHA, and uninstall passed. Both published refs declare `0.1.0`; installed cache contents, marketplace Git HEAD, and config ref established the actual revision change.
- A negative guide replay found that the first update preflight accepted a sole Backplane plugin from a different marketplace. The corrected guide requires the exact installed selector and uses reviewed-SHA placeholders. The same negative input now fails before mutation, and the positive guide blocks still pass with upstream and an unrelated plugin present.
- Independent [failure probes](transcripts/2026-09-19-codex-failure-probes.md) established duplicate, dirty, lookalike, and collision fixture facts without issue mutation. Their setup-agent responses remain untested.
- `codex login --device-auth` could not complete because the account disables device-code authorization. An initial regular browser OAuth attempt was canceled; a new regular OAuth attempt is waiting in isolated `state-native`. No credential was copied from the normal profile. Native fresh-session discovery and installed-plugin behavioral conformance remain `UNKNOWN`.
- Issue #3 remained open at `backplane:active`, `updatedAt=2026-09-19T19:37:32Z`, after the disposable checks.

## Codex acceptance matrix

| Case | Status | Evidence and remaining check |
|---|---|---|
| Clean install | UNKNOWN | CLI installed `0.1.0`; fresh session discovery pending. |
| Compatible upstream native adoption | UNKNOWN | Authoritative v6.4.1 package and skill files verified; setup response pending. |
| Compatible upstream sibling adoption | UNKNOWN | Exact upstream origin/commit and skill files verified; setup response pending. |
| Upstream absent, stable setup | UNKNOWN | Stable v6.4.1 obtained in isolated Codex state; setup response pending. |
| Repeat install | PASS | Exactly one effective Backplane plugin after a second `plugin add` in disposable state. |
| Compatibility preflight | UNKNOWN | Real `gh` native fields and lifecycle flags passed; agent preflight response pending. |
| Version change and rollback | PASS | Fixture-only `0.1.1` candidate and restored `0.1.0`; sentinel and user-file hashes unchanged. |
| Pinned remote Git ref restoration | PASS for CLI; UNKNOWN for fresh session | Published SHAs switched and restored installed cache content; fresh discovery pending. |
| Backplane-only uninstall | PASS | `plugin remove` left sentinel and shared marketplace configured in disposable state. |
| Preservation and failure probes | UNKNOWN | CLI/fixture facts and fresh repository-skill hypothetical refusal/recovery passed; authenticated native setup probes remain pending. |
| Three-skill fresh discovery | UNKNOWN | Native plugin auto-discovery in an authenticated isolated profile was not run; a junction-only probe was excluded from acceptance. |
| Authorized lifecycle and five conformance checks | UNKNOWN | Five named checks passed with repository skills; isolated installed-plugin conformance and disposable native lifecycle mutations remain pending. |

## Task 4: Interim conformance evidence

- Static `skill-structure` PASS: two canonical Backplane `SKILL.md` files, five direct references, exact names and frontmatter, four upstream skill hashes matching the independent checkout and installed cache. The corrected installation reference SHA-256 is `50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D`.
- Fresh repository-skill sessions captured exact prompts and responses for `native-issue-intake` (6/6), `language-neutral-verification` (5/5), `lifecycle-transitions` (5/5), and `superpowers-installation` (6/6 after a RED/GREEN correction). These runs used the normal authenticated Codex profile and repository-discovered skills; they do not prove discovery from the isolated installed plugin.
- The installation RED response incorrectly used Backplane `.agents/skills` as the package source. The reference now names canonical root `skills/`, and an exact-prompt rerun used the correct path. A six-case failure probe then found and corrected a conflated dirty-checkout adoption/update decision; its rerun passed A-F. Exact captures are in the Task 4 transcripts.
- Read-only issue #3 status and selection returned `OPEN`, exactly `backplane:active`, parent #1, blocker #2 closed, blocking #6 open, and unchanged `updatedAt=2026-09-19T19:37:32Z`. No issue mutation occurred in that probe.
- Native installed-plugin setup, three-skill fresh discovery, and the remaining authorized lifecycle transitions stay `UNKNOWN` until run. These are acceptance gates, so this interim evidence does not complete issue #3.