# Issue 19 final branch verification before whole-change review

Inputs: approved recovery plan blob `9f8d251b13067da3ed9ae3d893fbc7a7bad5a850`,
issue #19 semantic criteria unchanged at `updatedAt=2026-10-25T16:21:35Z`,
B `b0d702f8821d6d29184118410ec6ff2d8fb63438`, test-only F
`5e01704fcdda13eefeeac52d8892da26e7164ffd`, and clean independent upstream
7.0.1 `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`.
The tested combined guide is at recovery merge
`737af3f01bba8c5dd0e200cba1f8fa66655151fc`; later evidence storage does not
replace that delivery identity. Windows Claude scope only.

## Acceptance and verification mapping

| Current issue obligation | Observed evidence | Disposition |
| --- | --- | --- |
| One effective repeat install, real pinned update, exact rollback, Backplane-only uninstall | `2026-10-25-issue-19-python-lifecycle.json` and separate `2026-10-25-windows-superpowers-v7.0.1.json`: exact B/F source, 21 source blobs, marker and fresh discovery | PASS in recorded Windows sessions |
| Exact guide commands, failed candidate preservation and concrete recovery | All nine exact Python blocks replayed with ten snapshots in 7.0.1 evidence; final combined guide has byte-identical executable blocks | Retained PASS with unchanged inputs; no new full-replay claim |
| Fresh separate upstream and two Backplane skill discovery | Final fresh session `45cb8ac5-d818-43d1-916d-0fc7e8ae17bc`, actual three Skill calls; final-guide JSON and transcript | PASS |
| All five named conformance checks | Skill structure including ten relative links, plus 23/23 original expectations in 7.0.1 receipt; canonical skills/manifests unchanged from B | Retained PASS with exact unchanged installed inputs |
| Actual status/selection/design/ready/execution/blocked/resume/review/verified completion | Original live-fixture receipt plus `2026-10-25-issue-19-fixture-closeout.json` and transcript | PASS for real authorized #34, not simulation |
| Immediate unrelated-plugin, normal-profile, user-sentinel, upstream, history and #19 preservation | Original lifecycle snapshots and final before/after snapshots: 21 exact installed source blobs; authorized ref delta separately reconciled | PASS; intentionally changed owned refs are recorded |
| Current strict package, guide parse, bounded scope and Python checks | Final-guide receipt: strict validation, nine Python blocks compile, four unchanged legacy blocks parse, Ruff, ty, five regression tests | PASS |
| Full change whitespace check | Two historical transcript exceptions below; all other paths pass | Known exceptions; not an unconditional full-check pass |
| Whole-change review, final #19 target integration and integrated closeout | Not yet performed | PENDING; #19 remains open |

## Fixture integration and completion

The operator explicitly approved the presented #34 PR creation, merge after fresh
verification, integrated-byte checks and completed closure in the resumed session.
PR #35 merged reviewed head `22c5b8d917a09f275c23d99bd9c9645d6c1d2e35`
into main at `29efac8c41c8978650fe492b6111293ecb28302d`.
Fresh local and gh-served blob checks match reviewed guide
`db631c32aa4b9edd39b712bce845ae80fe52290a` and plan
`6b33d68ad02066e2a1dfd576235b890e3a5267cf`.
The corrected paragraph and all four unchanged parsed legacy blocks passed there.

Three fresh installed-package Claude sessions observed blocked-to-active resume,
PR submission to review, and actual completion after verification. Final #34 is
CLOSED/COMPLETED at `2026-10-25T17:57:19Z`, with only `documentation` and its
unchanged empty native hierarchy/dependency graph. The neutral PR reference did
not auto-close it. Independent fixture review and focused correction acceptance
are retained; they are not whole-#19 review. The immutable native evaluation is
https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6401129294 .

## Rulings and limitations for final review

- Preserve historical evidence and original approved plan bytes. The old draft
  status, Mac paths and earlier pending fixtures remain historical; native approval,
  continuation and current receipts govern current applicability.
- Retain the full 7.0.1 replay because all nine executable guide blocks, installed B
  and canonical skill inputs match. The newly integrated paragraph adds no code;
  its exact bytes, parsing, fresh discovery and preservation were freshly checked.
  Cost if wrong: a changed executable input could inherit invalid old evidence;
  exact block comparison and unchanged package diff are the controls.
- `git diff --check main...HEAD` detects trailing whitespace in the verbatim
  historical SSH failure at transcript `2026-10-25-issue-19-python-lifecycle.md:147`
  and a blank EOF in the earlier harness-source capture. Keep these exact captured
  artifacts rather than silently edit evidence. All remaining paths pass with only
  those two files excluded. Cost: two disclosed formatting defects remain;
  they do not affect executable blocks or package behavior.
- A GitHub read timed out before mutation; retry succeeded. The issue-body edit's
  initial exact-string check rejected CRLF versus LF; normalized text comparison
  proved equivalence with all other native fields unchanged. No second body edit.
- Final capture setup initially omitted its neutral directory, so process creation
  failed before a Claude session ran. Creating that directory allowed the approved
  probe to run. A console CP1252 output failure occurred after strict validation;
  explicit UTF-8 output corrected capture. Neither is a product failure.
- Source/profile provenance was checked on this host; credentials were never copied.
  Optional fresh Codex model verification remains unperformed after its earlier
  approval-review rejection. No cross-platform execution or complete-stack claim.
- No #19 or #11 closure, final #19 PR/merge authorization, release, tag, Project
  change, branch deletion or worktree cleanup is implied by #34's approval.

Supporting JSON and transcripts are current branch artifacts pending storage
commit/publication. Earlier published evidence keeps its original identities.
