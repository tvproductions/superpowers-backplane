# Initial Backplane installation in OpenCode

This guide covers the native package and setup checks for OpenCode V2.
Backplane is a companion to independently installed
[Superpowers](https://github.com/obra/superpowers). Its authored skills live
in this package's root `skills/` tree; the adapter registers that tree through
the active host's native API.

Issue #20 verified the shared adapter's initial package and discovery. V2
setup and failure verification belongs to #23, lifecycle verification to #24,
and integrated OpenCode acceptance to #12. The V1 configuration example records
the earlier #20 smoke scope. Current Backplane support is V2 only.

## Prerequisites

- OpenCode V2 2.0.4 or later. Run `opencode --version` before changing any
  settings. If the observed V2 version is below 2.0.4, stop and use a supported
  host release. Record the exact version used for verification.
- An independent [Superpowers installation](https://github.com/obra/superpowers/blob/main/.opencode/INSTALL.md)
  with attributable source and revision, or a stable release selected through
  the upstream OpenCode channel when no installation exists.
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

The historical V1 example uses singular `plugin`:

```json
{
  "plugin": [
    "EXISTING_SUPERPOWERS_ENTRY",
    "git+https://github.com/tvproductions/superpowers-backplane.git#FULL_COMMIT_SHA"
  ]
}
```

For V2, add Backplane to the plural `plugins` array:

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

V2 loads plugins asynchronously. Wait for the expected package revisions and
skill sources to appear in the intended server and working directory before
scoring discovery. For an isolated CLI verification, `opencode run --standalone`
uses a private server. Keep the working directory and configuration inside
the test profile so discovery cannot inherit skills from a parent checkout.

Installation alone does not complete Backplane setup. Follow the canonical
[dependency/preflight contract](../skills/managing-superpowers-backlog/references/installing-superpowers.md)
before backlog operations. Unsupported provenance, unavailable authentication,
or missing load evidence remains unverified. No issue state changes are part
of this initial installation check.

## Verify V2 setup

Choose the setup path that matches the observed upstream installation:

- **Native package.** Keep the existing Superpowers entry. Confirm it belongs
  to `obra/superpowers` or an official channel named by upstream. Record the
  installed package identity and its observed version or resolved revision.
- **Sibling checkout.** Verify the canonical checkout path, the exact
  `obra/superpowers` Git origin, the revision, and the required upstream skills.
  OpenCode V2 can load the verified checkout directory containing `index.js` as
  a local plugin. Use its directory path in `plugins` if it needs to be exposed.
  Keep the checkout read-only and retain its independent update path.
- **Upstream absent.** Use the current upstream V2 installation documentation
  to select the latest compatible stable release. Append its pinned native Git
  package entry to `plugins`, preserve the existing entries, then restart and
  verify the resolved revision. Record the stable tag and exact source commit.

With Backplane and the intended upstream source available to V2, send this
request in OpenCode. Substitute a repository and issue you are authorized to
read for `OWNER/REPO#ISSUE`.

```text
Set up Backplane in OpenCode V2. Verify that this host is supported, that exactly one Backplane package is effective, and that upstream Superpowers is independent and has known provenance and a visible version or revision. Use the existing native package or compatible sibling checkout when available. If upstream is absent, follow its documented V2 stable installation channel and preserve unrelated configuration. Run gh auth status and read OWNER/REPO#ISSUE using the complete native intake from the Backplane issue contract. Check the gh issue edit label flags and gh issue close reason flag through help. Report the host version, package sources and revisions, and which checks passed, failed, or remain unknown. For a failure, identify the failed check and recovery action. Preserve user files, unrelated plugins, existing upstream and GitHub issue state. Stop after setup and these read-only checks.
```

After setup, open a new session and run the discovery request above. Record
three completed native Skill results and attribute their source paths. On V2
the Skill tool names its target in `input.id`. An assistant summary or an
installed plugin list alone leaves actual load evidence unverified.

| Observation | Recovery |
| --- | --- |
| Unknown or versionless upstream, missing skill, or a lookalike origin | Keep the installed state. Verify the documented channel and obtain observable source and revision evidence before resuming. |
| Duplicate Backplane, conflicting plugin, or an occupied destination | Identify each source and its owner. Reconcile only the identified Backplane entry or choose a separate unused destination. |
| Dirty upstream checkout or incompatible release | Preserve the checkout. A verified, compatible dirty checkout can be used read-only. Obtain a separate compatible installation or have the owner resolve its state before an update. |
| `gh` authentication, native intake, label or closure-reason capability is missing | Reauthenticate through the host's supported account flow or use a `gh` release that supplies the failed capability. Stop before issue writes. |
| OpenCode model authentication is unavailable or package loads remain pending | Verify authentication in the intended profile or wait for readiness there, then retry the fresh-session discovery check. |

## Maintain OpenCode V2

Record the full Git commit of the currently verified Backplane package before
editing `plugins`. Keep the prior source available until the candidate passes
a fresh discovery check. Keep the independent Superpowers entry, unrelated
plugins and other settings in place.

Before applying a new pin, check that GitHub resolves the exact candidate commit:

```text
gh api repos/tvproductions/superpowers-backplane/commits/FULL_COMMIT_SHA --jq .sha
```

Compare the returned SHA with the proposed pin. If the lookup fails or the
returned identity differs, keep the verified configuration and record the
preflight failure.

| Operation | Edit and verify |
| --- | --- |
| Install or repeat install | Extend `plugins` with one Backplane Git entry pinned to its full commit. If that entry is already configured, reuse it. Wait for one effective Backplane package and run the fresh-session discovery request above. |
| Update | Confirm the candidate commit is available from the same trusted repository. Replace only the Backplane pin with the candidate's full commit. Restart in the intended configuration, confirm the resolved revision, and load all three skills from their installed sources. |
| Roll back | Replace the Backplane pin with the recorded verified prior commit and restart. Confirm the restored revision and repeat fresh discovery. |
| Recover from an unavailable source or failed verification | Record the failed source or discovery check before any repair. Keep the verified prior pin when the candidate is unavailable at preflight. If a candidate was already applied, restore the previous Backplane pin and prove the prior revision and all three skill loads again. Report recovery as unverified if the previous source or its loads cannot be confirmed. |
| Remove Backplane | Remove only the Backplane entry and restart. Confirm that both Backplane skills are absent and that the independently installed Superpowers skill still loads. |
| Restore a disposable test profile | Restore its original Backplane entry and verify its revision and all three skill loads again. |

This shows the single entry to change inside the existing V2 configuration:

```json
{
  "plugins": [
    "EXISTING_SUPERPOWERS_ENTRY",
    "git+https://github.com/tvproductions/superpowers-backplane.git#FULL_COMMIT_SHA"
  ]
}
```

Use a new session at each stage. Verify the actual package and skill sources in
the same OpenCode server and working directory after the expected inventory is
ready. Preserve unrelated files, plugin entries, upstream and GitHub issue
state.

### V2 lifecycle verification evidence

See the [V2 lifecycle verification record](https://github.com/tvproductions/superpowers-backplane/blob/203c5730c15617b9780e7767c6b201b8642b02fd/tests/scenarios/2026-11-01-issue-24-opencode-acceptance.md#task-1--native-package-operations)
for the tested revisions and observed results.
