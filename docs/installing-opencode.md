# Initial Backplane installation in OpenCode

This guide covers the shared native package and initial skill discovery for
OpenCode V1 and V2. Backplane is a companion to independently installed
[Superpowers](https://github.com/obra/superpowers). Its authored skills live
in this package's root `skills/` tree; the adapter registers that tree through
the active host's native API.

OpenCode adoption is still being verified. Issue #20 owns this initial smoke
surface; setup/failure coverage belongs to #21/#23, lifecycle coverage to
#22/#24, and final integrated acceptance to #12. This guide does not establish
update, rollback, uninstall, all upstream setup modes or full conformance.
No Backplane release or published adapter source is implied by a local test.

## Prerequisites

- OpenCode V1 1.18.29 or later, or V2 2.0.4 or later. The selected smoke hosts
  are V1 1.18.31 and V2 2.1.4; other versions require their own observations.
- A compatible, operational Superpowers installation with known source and
  revision, installed separately according to its current OpenCode guide.
- Git and authenticated GitHub CLI (`gh`) for subsequent backlog operations.
  Initial package loading does not authorize any issue mutation.
- An authenticated model provider in OpenCode for the fresh-session load check.
  A Codex or Claude login does not establish an OpenCode login.

The JavaScript runtime belongs to OpenCode. Backplane imposes no Python or
Node.js installation on the consuming project. GitHub Projects and IssueOps
are not required.

## Choose an immutable source

Use a reviewed full 40-character commit SHA available from the selected Git
source. Record it before changing configuration. Do not replace it with a
moving branch or assume a `v0.1.0` tag exists.

The public-source package form is:

```text
git+https://github.com/tvproductions/superpowers-backplane.git#FULL_COMMIT_SHA
```

`FULL_COMMIT_SHA` is a substitution marker, not an executable package target.
Before using a hosted SHA, verify it has actually been published and contains
`package.json`, `index.js` and both canonical skill folders. The local #20 test
uses an independent fixture Git source and an exact local commit; it does not
prove hosted installation or publish that commit.

A local development/test Git source uses the equivalent
`git+file:///ABSOLUTE_REPOSITORY_PATH#FULL_COMMIT_SHA` form. On Windows the URI
includes the drive, for example `git+file:///C:/fixtures/backplane#FULL_COMMIT_SHA`.
This asks the native resolver to install a Git package. Configuring the source
directory itself is a different development seam and does not prove this path.

## Configure the package

Preserve all existing configuration and unrelated plugin entries. Add the
pinned package string to the applicable array in `opencode.json` or
`opencode.jsonc`; do not replace the array or add a separate Backplane skills
path. Keep upstream Superpowers' existing entry unchanged.

V1 uses singular `plugin`:

```json
{
  "plugin": [
    "EXISTING_SUPERPOWERS_ENTRY",
    "git+https://github.com/tvproductions/superpowers-backplane.git#FULL_COMMIT_SHA"
  ]
}
```

V2 uses plural `plugins`:

```json
{
  "plugins": [
    "EXISTING_SUPERPOWERS_ENTRY",
    "git+https://github.com/tvproductions/superpowers-backplane.git#FULL_COMMIT_SHA"
  ]
}
```

Replace both markers with the verified existing upstream entry and published
Backplane SHA. The examples illustrate additions, not complete replacement
configuration. Native startup resolves and caches the package. A failed fetch,
plugin error or absent skill means installation has not been verified; preserve
existing files and report the observed error before attempting recovery.

## Start a fresh session and verify

Start OpenCode in the intended consuming project after changing configuration.
Use a fresh session, then send:

```text
Use the native skill tool to load using-superpowers, managing-superpowers-backlog, and managing-superpowers-handoffs. Report each tool result and its source path. Do not query GitHub, mutate any issue or file, run setup, or delegate. Stop after reporting discovery.
```

The upstream bootstrap may already supply `using-superpowers`; verify its
actual source. Both Backplane skills must successfully load from the native
installed package, with upstream from its independent installation. Discovery
through a repository-local link or copied skill tree is insufficient. Preserve
unrelated plugin entries and user files. Record host version, pinned source,
three skill paths and hashes, upstream source/revision, and any failed check.

V2 loads plugins asynchronously. An immediate empty API list is not proof of a
missing plugin: inspect readiness in the same intended server/location before
scoring discovery. A test using `--standalone` must not treat the normal user's
background service as its private test server.

Installation alone does not complete Backplane setup. Follow the canonical
[dependency/preflight contract](../skills/managing-superpowers-backlog/references/installing-superpowers.md)
before backlog operations. Unsupported provenance, unavailable authentication,
or missing load evidence remains unverified. No issue state changes are part
of this initial installation check.

## Later operations

Update, rollback and Backplane-only removal remain pending the owning OpenCode
verification leaves. Do not infer these operations from the initial smoke test
or remove upstream Superpowers as part of Backplane maintenance.
