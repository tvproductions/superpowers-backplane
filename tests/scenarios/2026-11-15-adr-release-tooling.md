# ADR release tooling — partial maintenance checkpoint

Date: 2026-11-15. This is a preserved work checkpoint, not completed Task 2,
strict baseline acceptance, ADR integration or release readiness.

The approved ADR integration plan authorizes current-stable prerequisite
maintenance. The [read-only official inventory](2026-11-15-adr-release-tooling-before.json)
checked all 71 locked registry projects before modification. uv's owning upgrade
changed ten selections: uv 0.13.7 -> 0.13.8, Ruff 0.17.4 -> 0.17.5, ty 0.0.99 ->
0.0.104, Cosmic Ray 8.7.0 -> 8.9.0, coverage 7.17.2 -> 7.17.3, Lizard 1.25.1 ->
1.26.0, plus anybadge 1.16.0 -> 1.18.0, filelock 4.2.9 -> 4.2.10,
markdown-it-py 4.2.0 -> 4.3.0 and stevedore 5.9.1 -> 5.10.0. Other exact pins
are retained. uv lock --upgrade generated the lock; locked all-group sync and
all four routine pre-commit checks passed on managed Python 3.14.10. CI's uv
reference is 0.13.8; its Python and two pinned Actions remain current. The
minimum-only uv compatibility contract is unchanged. No product Python package
or consumer runtime requirement is introduced.

The actual installed Git-hook path was absent at inspection. The configured four
checks ran explicitly; this checkpoint does not claim an installed-hook proof.
Complete that acceptance observation before final integration/release. No hook
was disabled or bypassed. Deeper changed-tool compatibility, structured Cosmic
Ray worker outcomes, current advisory audit and complete A01-A18 reconciliation
remain required; passing routine checks do not substitute.

An isolated read-only Superpowers 7.0.2 source checkout resolves to
`22f0b463e7a5e579904dd6211a520321035526f7`. Existing installed upstreams and
project native activation were not changed. Four fresh native conformance
responses and source/input hashes are preserved in the companion archive below.
CLI exit zero is not a scored conformance verdict; full rubric scoring, five-check
acceptance, final native selections and the pre-authorship ADR checkpoint baseline
remain pending. Product ADR references have not been authored. Existing
SUPERPOWERS.md/native declarations retain their previous selections; do not claim
that an isolated candidate advances them.

Owner issue [#37](https://github.com/tvproductions/superpowers-backplane/issues/37)
was created under the approved exact intake payload, with one designing lifecycle
label. Last full intake observed at 2026-11-15T18:53:19Z; re-read before transitions.
The approved design/plan and separate real ADR-0001 approval remain intact.
No lifecycle transition, checkpoint schema change, CLI implementation, tag or
release occurs in this checkpoint. Backplane 0.3.0 remains the planned finite
ADR-integration minor from published 0.2.0.

Preserve original dirty checkout and this registered detached worktree. The
portable guidance owner has synchronized reviewed source at
`77ad2c792e0df39782271639c317e2c812b5a48e`, still unreleased while its current
OpenCode channel is unverified. Starter propagation and both publishers' release
acceptance remain separate. Continue the approved plan in order; do not invent
completion from this tooling checkpoint or start the separately planned CLI.
