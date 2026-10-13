# Issue #31 setup checkpoint portability verification

This verifies transport of the Mac setup checkpoint, not governance Task 1 or
the planned product checkpoint format. The evaluated checkpoint commit is
`8685658f22ac81282c1af9f482cb8605ddd16720`. This later evidence record does not
claim its own future storage commit was already evaluated.

## Observed failure before the correction

`git archive 82fa208cd81b1ae33a6b24e869220f90c9558312
docs/superpowers-backplane/plans/2026-10-12-issue-31-mac-execution-checkpoint.md`
failed with `pathspec ... did not match any files`. That committed baseline
contains the approved planning inputs but lacks this execution summary. The
actual earlier Mac recovery also found no transported Windows execution ledger.
This does not prove Windows work was never performed.

## Observed committed export

A fresh empty directory under `/private/tmp` received the full tree through
`git archive 8685658f22ac81282c1af9f482cb8605ddd16720 | tar -x -C <directory>`.
The following actual checks passed with zero exit status:

- Ignored `.sp-bp/work/` and the ignored upstream installation were absent.
- `cmp` verified the exported execution summary was byte-identical to the
  committed workspace summary.
- Six separate `cmp` checks verified all captured response records were present
  and byte-identical to the evaluated setup/discovery responses.
- SHA-256 of the exported approved plan, specification, and frozen probe
  contract exactly matched their recorded approval/input identities:
  `ae05361badc5be68474b4fc5ea19de01f806b31e245c5f9e88be99e1da3e72f1`,
  `677bcc5ce2707781f0ee05c15306bd1be0587a801ca48699fba195722681bdb0`, and
  `fc23cbae20160535f0836eff9920649c0dc78fe50b17ac3082904f2b38710f81`.
- The summary explains Task 1 as the first unsupported task and preserves the
  unknown Windows results; its setup evidence is inspectable without scratch.
- The actual upstream checkout and committed native worktree remained clean.

Result: PASS for Git-tree portability of the setup summary, required source
inputs, and supporting captures. An ignored execution ledger is no longer the
only local continuity source for this setup milestone.

## Limits

This was a clean Git export on the current Mac, not a remote clone, another
machine's execution, or a live GitHub state capture. No remote publication or
arrival was tested. The export does not make upstream operational on another
host; that host must establish its own installation/discovery and reconcile
current instructions, Git/GitHub state, and evidence before execution.
No Windows task completion, new governance behavior, or product checkpoint
acceptance is inferred. The local native workspace remains detached and retained.
