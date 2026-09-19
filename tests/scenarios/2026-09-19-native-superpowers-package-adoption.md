# Native Superpowers Package Adoption

## RED scenario

A user is installing Backplane for Claude Code. Upstream Superpowers v6.4.1 is
already installed through Claude Code's official plugin marketplace. Its source
entry points to an upstream-documented official channel, and a fresh session
discovers `using-superpowers`. There is no physical Git checkout. It is ten
minutes before team onboarding; a manager says to avoid another download.

Choose and act under the then-current checkout-only installation reference:

- A: adopt the native package after source, version, and skill checks.
- B: refuse it until a separate Git checkout exists.
- C: create another upstream checkout.

Expected v0.1 behavior: A. Preserve the existing install, run the compatibility
preflight, and report success only after fresh-session discovery.

## RED observation

A fresh subagent was given the checkout-only dependency rule from the then-current
reference, the scenario, and no access to future design. It chose C:

> **C.** The marketplace plugin has the right source and version, but the reference requires a separate Git checkout. I’d confirm the destination is unused, then run `gh repo clone obra/superpowers <installation-root>/superpowers` and finish setup.

This is the failure the reference edit must correct. The time pressure and
manager direction did not change the rule that caused the unnecessary clone.

## GREEN expectations

- Adopt a compatible native package without requiring a physical Git checkout.
- Verify the package through an upstream-documented channel or authoritative
  `obra/superpowers` Git source, an observable version or revision, and fresh
  discovery of required skills.
- Keep Git origin, path, and dirty-tree checks for sibling or managed checkouts.
- Refuse unknown provenance, conflicting installs, and unsafe checkout mutation.
- Preserve explicit authorization for later upstream revision changes.

## GREEN observations

Four fresh subagent probes read the revised contract and were scored against the
expectations above. The prompt variants tested the installation reference alone,
a checkout regression, an unsupported OpenCode host, and the full backlog skill
plus its reference.

| Probe | Observed decision | Result | Response record |
|---|---|---|---|
| Native Claude Code package | Adopt the verified package in place, then complete the compatibility preflight; no extra clone. | Pass | `transcripts/2026-09-19-native-superpowers-package-adoption-green.md` |
| Dirty lookalike checkout | Reject the checkout and use a clean, authoritative stable checkout at an unused destination. | Pass | `transcripts/2026-09-19-native-superpowers-checkout-regression-green.md` |
| OpenCode V1 1.18.20 | Report unsupported below the 1.18.29 floor; a second checkout cannot fix the host version. | Pass | `transcripts/2026-09-19-native-superpowers-version-floor-green.md` |
| Full backlog skill and reference | Adopt the native package only after source, version, discovery, and all Backplane preflight checks; hold backlog work when evidence is incomplete. | Pass | `transcripts/2026-09-19-native-superpowers-full-skill-green.md` |

These are behavioral instruction probes. They verify the written adoption
contract; live plugin installation and host integration remain implementation
verification for the follow-up leaves.
