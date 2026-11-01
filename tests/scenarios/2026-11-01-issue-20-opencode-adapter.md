# Issue #20 local OpenCode adapter verification — 2026-11-01

## Result and identities

The shared adapter and initial-install guide are implemented locally. Native
OpenCode V1 1.18.31 and V2 2.1.4 install the exact Git-package candidate and
discover both canonical Backplane skills from their own caches. Overall smoke
acceptance remains **UNKNOWN**: neither isolated profile completed model
provider authentication, so successful fresh-session skill-tool loads have
not been observed. The final evidence gate exits 1; no fully passing gate,
ready-to-merge state or completed issue is claimed.

Product candidate: `bc6d30e54621c8a1747a0f2baa0551f25080b06a`.
Base: `337aa19cc13aa6480c13cb347c8bdfef5c656472`.
Approved plan commit: `bb884f82819426e2d1a5c42b956153fd270c4b7d`, blob
`e8b35178b048c618801513d57bb14d51164672c8`. Approved plan bytes are unchanged.
The native worktree is
`C:/Users/Jeff/.codex/worktrees/fc58/superpowers-backplane`, detached and
registered with the standalone repository's common Git directory. Its later
evidence-storage commits do not replace the tested product identity.

The [structured receipt](2026-11-01-issue-20-opencode-adapter.json) retains
host executable hashes, installed paths/raw hashes/normalized Git identities,
source pins, before/after snapshots, final check results and exact limitations.
Raw SDK/CLI captures and OAuth/server logs remain ignored; they can contain
upstream bodies or temporary authentication values and are not publication
artifacts. Screened helper sources are captured beside existing transcripts.

## Criterion assessment

| #20 criterion | Observation | Result |
| --- | --- | --- |
| One entry point supports both contracts and canonical skills | Named V1/server hook plus guarded V2 setup; both actual hosts discover the two installed canonical paths | PASS for selected native versions |
| V1/V2 guide, pinned Git source and replay | Config key differences documented; disposable profiles resolve full-SHA local Git packages through native resolvers | PASS for local Git transport; hosted source untested |
| Fresh session sees three independent skills; later lifecycle claims pending | Native registries identify upstream plus both Backplane skills, but no authenticated model session has successfully loaded them | UNKNOWN; blocks #20 acceptance |

The package contains 67 files at the final candidate. All declared files match
candidate Git blob identities after Git's normal text conversion in both
installed caches. Windows checkout CRLF produces different raw hashes from LF
Git blobs; both identities remain explicit. No copied authored skill tree or
upstream bootstrap is added. Root Codex/Claude metadata is unchanged.

## Verification

- Full current `node --test` suite: 9 passed, 0 failed. Behavior cases were
  observed RED before implementation; malformed/missing/quoted metadata and
  V1 rejection-before-config-mutation each had failing negative controls.
- Receipt/environment unittest suite: 11 passed, 0 failed, including four
  additional review-reproducer cases observed RED before the correction.
- Ruff lint/format and ty pass on all five owned Python helper files.
- Guide/README links and both JSON examples pass. No Python or PowerShell
  examples were added to this guide.
- Both native caches contain the pinned package and required skill identities.
  V2 reports upstream, Backplane and the unrelated sentinel active.
- Corrected final verification recomputes current package/working-source
  identities, capture hashes, guide/runtime-reference links, authoritative
  upstream origin/revision/path, executable identity, configuration-source
  containment and current protected-state snapshots. All these checks pass in
  both variants. The passing-smoke/schema gate remains false because required
  authentication/session/load evidence is absent.

These observations do not repeat setup/failure/lifecycle/conformance acceptance
owned by #21–#24, or final integrated acceptance under #12. Hosted installation,
merge, push, publication, release, issue closure and cleanup were not performed.

## Fresh review and corrections

A fresh independent reviewer inspected `337aa19..bc6d30e` and the fixture
scorer. No adapter source defect was identified. Two Important findings were
confirmed: provenance/isolation assertions could be accepted without adequate
binding, and final verification merely reclassified stored results. Four new
negative controls reproduced untrusted origin/path, non-Boolean evidence,
unpinned/local-directory package targets and capture-integrity gaps. One fix
pass made the full 11-case suite green and implemented the current-file checks
listed above. There were no Critical/Minor findings and nothing declined for
judgment. No second independent review is claimed.

## Execution rulings and negative results

- Reserved `.superpowers` helpers were replaced with native project-owned
  bookkeeping under ignored `.sp-bp/work/issue-20/`; upstream remains read-only.
- Receipt/environment tests ran before Task 1 helper implementation because
  the runner controls safe host launch. This changes test ordering, not scope.
- V1 project-config disabling alone still discovered ancestor `.agents`
  Backplane skills before package installation. That baseline is excluded.
  An independently initialized fixture Git root bounded traversal; the corrected
  baseline had upstream and no Backplane skills before installation.
- Short-lived V2 API commands exited before asynchronous plugin activation.
  A bounded owned loopback private server with condition polling supplies the
  accepted inventory. An initial bare HTTP diagnostic returned 401; later
  requests use a child-generated secret without recording its value publicly.
- The planned bare fixture mirror was replaced by a non-bare independent clone
  so AGENTS' `show-toplevel` guards remain usable. `--no-hardlinks`, origin,
  starting SHA, clean state, canonical root and absence of alternates were
  checked. Additional disk usage is the only intended cost.
- Git's long-path file-open failure was avoided by hashing installed bytes via
  `git hash-object --stdin --path`, without writing Git objects or changing
  global configuration. Raw Windows hashes remain separately recorded.
- Both V2 OAuth attempts expired without completing sign-in. Do not restart
  automatically or copy a normal-profile credential. The operator can use the
  foreground launcher below when ready.

## First required revalidation

Revalidate worktree registration/common Git directory, exact product files,
approved plan bytes, native #20 semantics and each existing profile's marker,
paths, upstream provenance and auth inventory. Ignored profiles may be missing
on another host; reconstruct only from screened helper sources in a verified
owned area. Their captured machine paths require revalidation before execution.

From the standalone repository on this Windows host, these foreground commands
start separate native provider sign-ins without copying credentials:

```text
uv run --no-project python .sp-bp/work/issue-20/login.py --variant v2
uv run --no-project python .sp-bp/work/issue-20/login.py --variant v1
```

After login, verify `gpt-6.1-sol` (the observed Codex configuration preference)
is actually available in each OpenCode model catalog before running the planned
fresh prompt. A missing model requires an operator decision; no silent fallback.
Rebuild both receipts and rerun the full final gate after successful native
loads. Restore an issue's active resume target only after the blocker and its
entry conditions have been revalidated. Integration/publication/closure remain
separate decisions. #4/#5 plans were not approved or implemented by this task.

## Login launcher correction and operator boundary

The operator reported that no browser opened. Reproduction showed V1 was
waiting at its Login method selector; the original launcher did not select a
method or open a browser itself. The operator explicitly rejected desktop
control. All desktop/browser UI automation stopped, and the owned browser-mode
login was canceled via its terminal session. No sign-in completed.

The V1 launcher now explicitly selects `ChatGPT Pro/Plus (headless)`, leaving
URL/code entry to the operator in their own browser. Argument parsing/process
launch is import-safe. Two regression tests were observed RED, then GREEN; the
combined helper suite passes 13 tests, and changed helpers pass Ruff/format/ty.
No new login was started to claim end-to-end success. Native authentication
and model-backed acceptance remain UNKNOWN. Do not use desktop/browser UI
automation to overcome this prerequisite on resume.
