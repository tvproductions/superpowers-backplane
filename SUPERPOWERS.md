# Upstream Superpowers Dependency

- Upstream: `https://github.com/obra/superpowers.git`
- Channel: stable
- Release: `v7.0.0`
- Published: `2026-10-10T00:28:58Z`
- Resolved commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
- Local checkout: `.agents/superpowers`
- Discovery surface: `.agents/skills/superpowers`

The checkout and discovery junction are intentionally ignored. This document
records the resolved dependency for diagnosis; it is not an indefinite pin.

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
