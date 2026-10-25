# Upstream Superpowers Dependency

- Upstream: `https://github.com/obra/superpowers.git`
- Channel: stable
- Release: `v7.0.1`
- Published: `2026-10-21T21:05:11Z`
- Resolved commit: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`
- Local checkout: `.agents/superpowers`
- Discovery surface: `.agents/skills/superpowers`

The checkout and discovery junction are intentionally ignored. This document
records the resolved dependency for diagnosis; it is not an indefinite pin.

On 2026-10-25 the operator explicitly authorized aligning the Windows checkout
with this recorded 7.0.1 revision. The independent checkout and disposable Claude
upstream registration now match it. All five named checks and the affected
Backplane lifecycle/discovery seams passed in fresh Windows Claude sessions;
the existing 7.0.0 evidence retains its original scope. See
`tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.md` for exact inputs,
results and the unperformed fresh Codex probe's approval limitation. No Backplane
release or complete-stack acceptance is implied by this maintenance.

On 2026-10-24 the operator-authorized stable update passed all five Backplane
conformance checks and fresh local Codex discovery. The repository-scoped
OpenCode V2 configuration pins the independent upstream plugin to `v7.0.1`;
OpenCode reports that package active at the same resolved commit. Evidence and
scope limits are in
`tests/scenarios/2026-10-24-superpowers-v7.0.1-compatibility.md`.
This is direct Backplane compatibility evidence, not complete-stack gz-skills
integration or issue #31 satisfaction. The previous `v7.0.0` commit remains
`bb92a77741419a4ab5f06e711a283343f1ada0c3` for a separately authorized rollback.

The 2026-10-11 local Codex update passed all five Backplane conformance checks
and fresh-session discovery. Evidence and the prior revision for rollback are in
`tests/scenarios/2026-10-11-superpowers-v7.0.0-compatibility.md`.

On 2026-10-12 the missing Mac development checkout was restored from the
authoritative source at the same stable release/commit. Repository-local
symlinks expose upstream and both Backplane skills independently. Fresh Mac
CLI discovery and all five existing Backplane conformance checks passed;
evidence is in `tests/scenarios/2026-10-12-mac-superpowers-v7.0.0-setup.md`.
This is local evidence until its commit is transported and verified at the
integration target; it does not recover Windows issue-31 execution progress.

Before advancing the dependency, inspect the latest stable release, review
compatibility changes, obtain explicit authorization, run the Backplane
compatibility preflight and all five conformance checks, then update this record
to the verified revision. The upstream default branch is an explicit edge-
channel choice, never the implicit update target.
