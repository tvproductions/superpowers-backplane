# Claude Code setup and upstream adoption evidence for #18

## Task 1 — current baseline (RED)

Observed 2026-09-20 on `issue/18-claude-setup` at base `4c94aa627e4b59da5e7c942e9d42c04edac56158`. This baseline does not score a live #18 setup run. The integrated #17 package and guide match published and tested commit `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a` by `git diff --exit-code` over `.claude-plugin`, `README.md`, the Claude guide, and both canonical skills. `gh api` resolved that exact published SHA. The pinned detached clone is clean at `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane`, with exact `https://github.com/tvproductions/superpowers-backplane.git` origin.

The current guide has the #17 published-commit clone, one Backplane installation, complete read-only issue intake, setup request, and three-skill discovery. It lacks distinct native upstream, sibling checkout, and absent-upstream operator procedures and the full #18 failure/recovery table. Neither this scenario nor its transcript existed before Task 1. Those are the RED gaps for the guide and host evidence; #17's smoke is historical context, not a #18 result.

### Current host and sources

| Check | Observed baseline |
|---|---|
| Claude Code | `2.1.241 (Claude Code)`; `claude plugin marketplace list --help` and `claude plugin list --help` expose `--json`; `claude plugin install --help` exposes `plugin@marketplace` and `--scope`. |
| Default Claude profile | `claude auth status --json`: `loggedIn: false`, `authMethod: none` (command exit 1). It is not used for live checks. |
| Disposable Claude profile | `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-241ec92c05e84296bc7a2df74be839d3`; `loggedIn: true`, `authMethod: claude.ai`. Only `CLAUDE_CONFIG_DIR` in child process scope was changed. No auth values were copied or recorded. |
| Disposable Backplane | One enabled `superpowers-backplane@superpowers-backplane` v0.1.0, user scope; marketplace `superpowers-backplane` is the clean pinned clone above. |
| Disposable upstream | One enabled `superpowers@superpowers-dev` v6.4.1, user scope; marketplace is the separately installed `.agents/superpowers` checkout. This is an authoritative development marketplace, not the official absent-upstream channel. |
| Project Git | Root `C:/Users/Jeff/source/repos/agents/superpowers-backplane`; origin `https://github.com/tvproductions/superpowers-backplane.git`; clean issue branch at base commit above. |
| Upstream Git | Exact `https://github.com/obra/superpowers.git` origin, clean `v6.4.1` checkout at `5bf4e78011075bcfc0dc295f0724994cd123ee71`. Manifest version `6.4.1`; `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills` files present. |
| GitHub CLI | `gh auth status` succeeded as `ahuimanu`; complete 15-field read-only #18 intake succeeded. `gh issue edit --help` exposes `--add-label` and `--remove-label`; `gh issue close --help` exposes `--reason completed`. |
| Issue state | #18 OPEN, `backplane:active`, parent #1, #17 CLOSED blocker, #19 OPEN successor; observed revision `2026-09-20T17:29:58Z`. No setup probe has changed it. |

Package SHA-256: `.claude-plugin/plugin.json` `32BBD2859083522CF3FC040B45864A1DE6FC1FCD370C5BF30C21F87086486565`; `.claude-plugin/marketplace.json` `E9903B166D7FE302A51280A75D613D019A8945D8BEE23A77819BB2E2AE839DA1`; current guide `4409A700BFF6DB77C7CB852B747C36EEF7F095BB015BC6513EFE7385D35EC8B5`.

Authoritative documentation rechecked: [Claude plugin structure](https://code.claude.com/docs/en/plugins), [marketplace CLI and JSON inventory](https://code.claude.com/docs/en/plugin-marketplaces), [native installation](https://code.claude.com/docs/en/discover-plugins), [configuration environment](https://code.claude.com/docs/en/env-vars), and the installed upstream README Claude Code section. Upstream lists `/plugin install superpowers@claude-plugins-official` as its official marketplace path and `obra/superpowers-marketplace` as an alternative. `--plugin-dir` is a session-scoped local plugin input. `CLAUDE_CONFIG_DIR` isolates Claude configuration.

### Supported setup modes

| Mode | Input/source | Expected result | Actual result | Preservation evidence | Score |
|---|---|---|---|---|---|
| Native upstream package | Authenticated #17 disposable profile with separate `superpowers@superpowers-dev` and pinned Backplane plugin | Authoritative source/version, `gh` preflight, and three direct fresh skill invocations | Pending Task 3 | Baseline inventories and source revisions above; compare after | UNKNOWN |
| Sibling checkout | Same pinned Backplane, authoritative `.agents/superpowers` via session `--plugin-dir` | No upstream relocation or update; fresh three-skill discovery | Pending Task 3 | Record checkout HEAD/status and plugin inventory before/after | UNKNOWN |
| Absent upstream | Second authenticated disposable Backplane-only profile | Setup installs official stable native upstream in the same session; fresh discovery | Pending Task 5 | Record second-profile inventory and unrelated state before/after | UNKNOWN |

### Failure and recovery probes

| Case | Input/source | Expected result | Actual result | Preservation evidence | Score |
|---|---|---|---|---|---|
| Unknown or versionless native source | Disposable fixture without observable authoritative revision | Stay UNKNOWN; give source/version repair | Pending Task 4 | Plugin config and issue-state comparison required | UNKNOWN |
| Duplicate effective Backplane | Second disposable marketplace identity | Stop and identify conflicting ID/scope | Pending Task 4 | Both marketplace/plugin inventories before/after | UNKNOWN |
| Dirty authoritative checkout adoption | Dirty disposable `obra/superpowers` clone | Adopt in place without update | Pending Task 4 | Fixture HEAD/status/hashes before/after | UNKNOWN |
| Dirty checkout update refusal | Same dirty authoritative clone, explicit update request | Refuse update before mutation | Pending Task 4 | Fixture HEAD/status/hashes before/after | UNKNOWN |
| Occupied checkout path | Disposable occupied destination | Stop; choose unused path without deletion | Pending Task 4 | Destination hash before/after | UNKNOWN |
| Missing `gh` auth | Named temporary CLI fixture | Stop with auth repair | Pending Task 4 | Plugin and issue-state comparison | UNKNOWN |
| Missing `gh` intake field | Named temporary CLI fixture | Stop with compatible `gh` repair | Pending Task 4 | Plugin and issue-state comparison | UNKNOWN |
| Missing `gh` label capability | Named temporary CLI fixture | Stop with compatible `gh` repair | Pending Task 4 | Plugin and issue-state comparison | UNKNOWN |
| Missing `gh` closure reason | Named temporary CLI fixture | Stop with compatible `gh` repair | Pending Task 4 | Plugin and issue-state comparison | UNKNOWN |
| Incompatible upstream skill/source | Disposable incompatible fixture | Stop with compatible authoritative source repair | Pending Task 4 | Upstream fixture and plugin comparison | UNKNOWN |
| Unauthenticated disposable profile | Signed-out isolated profile | Stay UNKNOWN; request one authentication | Default profile observed signed out; dependent live probe pending | Normal and disposable profile inventories remain separate | UNKNOWN |

`UNKNOWN` here means not yet observed for #18. Each later PASS requires actual host output plus before/after preservation evidence in the linked transcript; a model's final assertion alone does not establish discovery or preservation.