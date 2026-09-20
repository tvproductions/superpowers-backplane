# Install Superpowers Backplane in Claude Code

Backplane is a companion to [upstream Superpowers](https://github.com/obra/superpowers). Install the two Claude Code plugins independently. Backplane supplies the backlog and handoff skills; upstream supplies `superpowers:using-superpowers` and the development workflow.

## Requirements

- Claude Code with native plugin support, Git, and authenticated GitHub CLI (`gh`).
- A reviewed, published 40-character Backplane commit. Use a stable release commit when one exists. Do not use moving `main` as the selected installation revision.
- An existing issue in the GitHub repository where you intend to use Backplane. Setup uses it for read-only native issue intake; it never changes that issue just to check compatibility.
- An authenticated Claude Code session for the fresh discovery check.

## Clone and inspect the reviewed Backplane revision

Run this PowerShell block from an unused parent directory. Enter the exact reviewed commit from the Backplane pull request or release. The script refuses an occupied checkout path, an unexpected GitHub origin, and an unpublished revision.

```powershell
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI authentication is required' }
$backplaneRevision = Read-Host 'Reviewed 40-character Backplane commit'
if ($backplaneRevision -cnotmatch '^[0-9a-f]{40}$') { throw 'Use a full lowercase commit SHA' }
$backplaneCheckout = Join-Path (Get-Location) 'superpowers-backplane'
if (Test-Path -LiteralPath $backplaneCheckout) { throw "Checkout path already exists: $backplaneCheckout" }
gh repo clone tvproductions/superpowers-backplane $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Backplane clone failed' }
git -C $backplaneCheckout checkout --detach $backplaneRevision
if ($LASTEXITCODE -ne 0) { throw 'Reviewed revision is not in the clone' }
$origin = git -C $backplaneCheckout remote get-url origin
if ($LASTEXITCODE -ne 0 -or -not $origin) { throw 'Backplane origin is unavailable' }
$origin = $origin.Trim()
$acceptedOrigins = @(
  'https://github.com/tvproductions/superpowers-backplane',
  'https://github.com/tvproductions/superpowers-backplane.git',
  'git@github.com:tvproductions/superpowers-backplane',
  'git@github.com:tvproductions/superpowers-backplane.git',
  'ssh://git@github.com/tvproductions/superpowers-backplane',
  'ssh://git@github.com/tvproductions/superpowers-backplane.git'
)
if ($origin -notin $acceptedOrigins) { throw "Unexpected Backplane origin: $origin" }
$resolvedRevision = git -C $backplaneCheckout rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $resolvedRevision.Trim() -ne $backplaneRevision) { throw 'Checkout is at the wrong revision' }
$publishedRevision = gh api "repos/tvproductions/superpowers-backplane/commits/$backplaneRevision" --jq .sha
if ($LASTEXITCODE -ne 0 -or $publishedRevision.Trim() -ne $backplaneRevision) { throw 'Revision is not published at the expected origin' }
$dirty = git -C $backplaneCheckout status --porcelain
if ($LASTEXITCODE -ne 0 -or $dirty) { throw 'Reviewed checkout is not clean' }
$claudeManifest = Get-Content -LiteralPath (Join-Path $backplaneCheckout '.claude-plugin/plugin.json') -Raw | ConvertFrom-Json
$marketplace = Get-Content -LiteralPath (Join-Path $backplaneCheckout '.claude-plugin/marketplace.json') -Raw | ConvertFrom-Json
if ($claudeManifest.name -ne 'superpowers-backplane' -or $marketplace.name -ne 'superpowers-backplane' -or
    $marketplace.plugins.Count -ne 1 -or $marketplace.plugins[0].name -ne 'superpowers-backplane' -or
    $marketplace.plugins[0].source -ne './' -or $marketplace.plugins[0].version -ne $claudeManifest.version) {
  throw 'Claude package identity or root source is unexpected'
}
foreach ($skill in @('managing-superpowers-backlog', 'managing-superpowers-handoffs')) {
  if (-not (Test-Path -LiteralPath (Join-Path $backplaneCheckout "skills/$skill/SKILL.md"))) {
    throw "Canonical skill is missing: $skill"
  }
}
claude plugin validate --strict $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Claude package validation failed' }
```

Inspect both Claude manifests and the two root `skills/*/SKILL.md` files in that checkout before installing. Record `$backplaneRevision` and the checkout path. The marketplace source `./` resolves to the repository root, so Claude Code uses the canonical skill folders there.

## Install the Backplane plugin

First inspect `claude plugin marketplace list` and `claude plugin list`. If Backplane is already configured, resolve its source and version before adding another copy. For a clean installation, run:

```powershell
claude plugin marketplace add $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Backplane marketplace registration failed' }
claude plugin install superpowers-backplane@superpowers-backplane --scope user
if ($LASTEXITCODE -ne 0) { throw 'Backplane plugin installation failed' }
claude plugin list
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect installed plugins' }
```

A marketplace added from a local directory loads its relative-path plugin in place. Keep this checkout at the recorded revision until a separately verified update; changing its files changes the effective plugin. Installing Backplane alone does not run setup.

## Check the target issue and request setup

Provide an existing issue number in the target repository. This command checks read-only access and the complete native issue fields Backplane needs. Replace the prompts with the real repository and issue; do not use a production issue as mutation test data.

```powershell
$targetRepo = Read-Host 'Target GitHub owner/repo'
$targetIssue = Read-Host 'Existing issue number in that repository'
gh issue view $targetIssue --repo $targetRepo --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
if ($LASTEXITCODE -ne 0) { throw 'Cannot read the target issue with complete native fields' }
gh issue edit --help
gh issue close --help
```

Check that the edit help exposes label addition and removal and the close help exposes a closure reason. A displayed `gh` version alone does not establish compatibility.

Start a new Claude Code session. Tell Claude the target repository and existing issue number, then send this exact request:

> Set up Superpowers Backplane in this Claude Code session.

### Setup preflight in the Claude session

Use the target issue for read-only intake only. Setup must leave GitHub issue state unchanged. Follow this order before reporting compatibility:

1. Run `claude plugin marketplace list --json` and `claude plugin list --json` in the active Claude profile. Resolve marketplace sources and enabled plugin IDs. Require exactly one effective `superpowers-backplane` plugin at the reviewed revision, with `managing-superpowers-backlog` and `managing-superpowers-handoffs` from its canonical `skills/` tree. If another user, project, local, or session plugin supplies Backplane, report the conflict before adding anything.
2. Classify upstream Superpowers as an installed native plugin, a supplied sibling Git checkout loaded for this session with `--plugin-dir`, or absent. Do not treat a skill name alone as package provenance.
3. For an installed native package, identify its authoritative marketplace or documented source, installed version or resolved commit, and effective plugin ID. For a sibling checkout, verify its exact `https://github.com/obra/superpowers.git` origin, HEAD, clean or dirty status, and Claude plugin identity. In either case, require `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills` from that independent source. A source without observable version or revision stays `UNKNOWN` even when its skills load. Keep any existing upstream installation in place; a dirty authoritative checkout may be adopted without updating it.
4. Run `gh auth status`, the complete read-only `gh issue view ... --json` command above, `gh issue edit --help`, and `gh issue close --help`. Require all 15 issue fields, label addition and removal, and a closure reason. A displayed CLI version alone is insufficient.
5. Start a fresh Claude session with the same upstream mode and invoke `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs` separately with harmless read-only requests. Record the actual Skill tool loads and package roots. An inventory entry or the model's final statement alone is insufficient.

### Select the upstream source

**Already installed native package.** Leave it installed. Inspect its enabled plugin ID, source marketplace, installed version or resolved revision, and required skills. An authoritative `obra/superpowers` package source or upstream-documented Claude channel is acceptable. Record Backplane and upstream identities separately, run the preflight above, then start fresh sessions for the three direct skill checks. Do not refresh, replace, or remove upstream during setup.

**Compatible sibling checkout.** Resolve an independently managed checkout before launch. Require an exact `obra/superpowers` HTTPS or SSH origin, a recorded full HEAD, the upstream Claude plugin manifest, and all four required skill files. Record `git status --porcelain=v1`; a dirty checkout can be adopted in place, but an update request must stop until its owner resolves those changes. From the target project, pass the same resolved path to the setup session and each fresh discovery session:

```powershell
$upstreamCheckout = (Resolve-Path -LiteralPath (Read-Host 'Existing Superpowers checkout') -ErrorAction Stop).Path
$upstreamOrigin = git -C $upstreamCheckout remote get-url origin
if ($LASTEXITCODE -ne 0 -or -not $upstreamOrigin) { throw 'Superpowers origin is unavailable' }
$acceptedUpstreamOrigins = @(
  'https://github.com/obra/superpowers',
  'https://github.com/obra/superpowers.git',
  'git@github.com:obra/superpowers',
  'git@github.com:obra/superpowers.git',
  'ssh://git@github.com/obra/superpowers',
  'ssh://git@github.com/obra/superpowers.git'
)
if ($upstreamOrigin.Trim() -cnotin $acceptedUpstreamOrigins) { throw 'Choose the authoritative obra/superpowers checkout' }
$upstreamRevision = git -C $upstreamCheckout rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $upstreamRevision.Trim() -cnotmatch '^[0-9a-f]{40}$') { throw 'Superpowers revision is unavailable' }
$upstreamStatus = git -C $upstreamCheckout status --porcelain=v1
if ($LASTEXITCODE -ne 0) { throw 'Superpowers checkout status is unavailable' }
foreach ($skill in @('using-superpowers','brainstorming','writing-plans','writing-skills')) {
  if (-not (Test-Path -LiteralPath (Join-Path $upstreamCheckout "skills/$skill/SKILL.md"))) { throw "Missing upstream skill: $skill" }
}
claude --plugin-dir $upstreamCheckout
```

In that session, send the setup request above with the target issue. Launch every fresh skill-check session with `claude --plugin-dir $upstreamCheckout` as well. Record the checkout path, full HEAD, status, and loaded skill roots. This flag does not relocate or update the checkout. If your selected upstream origin uses another transport, first establish its authoritative `obra/superpowers` identity; do not silently accept a lookalike URL.

**Upstream absent.** Start the setup request in an authenticated disposable Claude profile with Backplane installed and no upstream plugin or sibling `--plugin-dir`. Keep normal host permissions so the session can request approval. The setup workflow reads [upstream's current Claude installation instructions](https://github.com/obra/superpowers#claude-code), identifies the current compatible stable release and official `claude-plugins-official` channel, and asks for the exact host commands before running them. If the official marketplace is not already available and current Claude documentation calls for registration, review and approve `claude plugin marketplace add anthropics/claude-plugins-official` first. Then approve `claude plugin install superpowers@claude-plugins-official --scope user` in that same setup session. Inspect the resulting marketplace source, installed plugin version or resolved revision, and four required upstream skills before fresh three-skill discovery. If the host cannot expose a version or revision, report `UNKNOWN`. Do not select upstream's default branch unless the operator explicitly chooses the edge channel; do not change this repository's `.agents/superpowers` checkout.

### Stop and recovery rules

A failed preflight must leave user files, unrelated marketplaces and plugins, the existing upstream source, and GitHub issue state intact. Report the failed check, observed identity, and the next safe repair action.

| Check that failed | Result and recovery |
|---|---|
| Unknown or lookalike upstream source; native package without observable version or revision | `UNKNOWN`. Establish an authoritative upstream source and observable installed version or full revision before claiming compatibility. Skill names alone do not resolve it. |
| More than one effective Backplane package | Stop. Name each conflicting plugin ID and scope; review which one to keep before removing only the selected duplicate. Preserve unrelated plugin entries. |
| Dirty authoritative sibling checkout | Adoption without an update may proceed if provenance and skills pass. Refuse an update until the checkout owner resolves its changes. Never reset or overwrite it during setup. |
| Occupied checkout destination | Stop before clone or file changes. Choose an unused path; preserve the occupant without deletion. |
| Missing `gh` authentication, native issue field, label add/remove, or closure-reason capability | Stop. Authenticate or repair `gh`, then repeat the failed capability check and complete read-only intake. Do not change the issue to test a capability. |
| Missing upstream skill, incompatible Claude host, or incompatible source | Stop. Select or install a compatible authoritative upstream release through the documented host channel, then repeat preflight. Preserve the old installation. |
| Unauthenticated Claude session | `UNKNOWN`. Authenticate the disposable profile once, then restart the dependent fresh-session checks. Do not copy credentials from a normal profile. |

The setup agent follows the [Backplane installation and compatibility reference](../skills/managing-superpowers-backlog/references/installing-superpowers.md). It must find exactly one effective Backplane plugin and both canonical skills, then adopt a separate operational upstream Superpowers plugin with an authoritative source and observable version or revision. If upstream is absent, use [upstream Superpowers' current Claude Code installation channel](https://github.com/obra/superpowers#claude-code) and its compatible stable release. Do not replace or update an existing upstream installation as a side effect.

The response must identify the Backplane plugin and revision, independent upstream package and source/version or commit, authenticated `gh` with complete read-only intake of the target issue and label/closure capabilities, and the three skill identities. If any result cannot be established, report `UNKNOWN` with the failed check and a recovery action. Setup must not change GitHub issue state.

Start another fresh Claude Code session. In `/help`, inspect Custom commands for `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. Invoke each with a harmless read-only request and verify that the two packages remain separate. Package installation or a model's unverified statement alone is not discovery evidence.

## Later lifecycle work

Pinned update, rollback, and Backplane-only uninstall instructions are pending verification in [issue #19](https://github.com/tvproductions/superpowers-backplane/issues/19). Follow upstream Superpowers' own installation and update channel for upstream changes; Backplane does not manage that package.
