# Mac Superpowers 7.0.0 setup and conformance

## Identity and scope

On 2026-10-12 the operator requested the next Mac recovery step. The separate
development checkout was restored at `.agents/superpowers` from authoritative
`https://github.com/obra/superpowers.git`, stable `v7.0.0`, resolved commit
`bb92a77741419a4ab5f06e711a283343f1ada0c3`. `gh release view` confirmed this
was the latest published stable release at setup time, published
`2026-10-10T00:28:58Z`. The release is an annotated tag; its tag object is not
the checkout commit. This restores the recorded revision without advancing it.

The Backplane source was `main` at
`82fa208cd81b1ae33a6b24e869220f90c9558312`, initially clean, with origin
`https://github.com/tvproductions/superpowers-backplane.git`.
Observed host/tool versions: Darwin `25.6.0 arm64`, Git `2.54.0 (Apple Git-157)`,
`gh 2.102.0`, Codex CLI `0.162.1`. No machine tool or cached plugin was updated.

The cached `superpowers@gzfactory-development` plugin remains disabled. The
development checkout is separate, has its own Git directory and authoritative
origin, and is clean after verification. No shipped upstream file was edited.

## Discovery and preflight

Current upstream README installation guidance and official Codex
[local skill discovery documentation](https://learn.chatgpt.com/docs/build-skills)
were read before setup. Codex supports repository `.agents/skills` discovery
and follows symlink targets. The ignored discovery links are:

| Link | Target |
| --- | --- |
| `.agents/skills/superpowers` | `../superpowers/skills` |
| `.agents/skills/managing-superpowers-backlog` | `../../skills/managing-superpowers-backlog` |
| `.agents/skills/managing-superpowers-handoffs` | `../../skills/managing-superpowers-handoffs` |

A fresh read-only session found and loaded all six requested skills through
its advertised inventory: using-superpowers, brainstorming, writing-plans,
writing-skills, managing-superpowers-backlog, and managing-superpowers-handoffs.
It verified the independent upstream origin/commit and separate source trees.
[Discovery capture](transcripts/2026-10-12-mac-v7-discovery.md).

Authenticated full native intake of issue #31 returned all 15 required fields.
Observed `updatedAt=2026-10-12T01:29:48Z`, OPEN, one `backplane:active` label,
and no native blockers. `gh issue edit --help` exposes `--add-label` and
`--remove-label`; `gh issue close --help` exposes closure reasons.

Structural inspection passed for both Backplane skills: YAML delimiters, exact
names, descriptions beginning `Use when`, readable references, and no unresolved
TBD/TODO/FIXME/PLACEHOLDER markers. No runtime validator was required.

A sixth fresh read-only session independently confirmed the native Mac
worktree's advertised skill discovery, canonical source separation, exact root,
registration, shared Git directory, starting commit, and detached identity.
[Worktree discovery capture](transcripts/2026-10-12-mac-v7-worktree-discovery.md).
Backplane locators resolve to the native worktree's own `skills/`; upstream
locators resolve to the existing independent development checkout. This checks
isolation/discovery, not additional governance behavior.

## Fresh behavioral method

Each original prompt was extracted verbatim from its mapped scenario's fenced
text block and sent to a separate ephemeral read-only `codex exec` session.
No model override was supplied; the exact effective model identity was not
captured. This is CLI/default-profile evidence, not a model-wide guarantee.
All six sessions exited zero. Process-only overrides disabled hooks and
multi-agent dispatch; no persistent user configuration was changed. Hook
execution, other harnesses, and the issue-31 governance bridges were not tested.

The common probe preamble required reading installed using-superpowers and
the requested Backplane skill/references, allowed project reads only for skill
sources and required instructions, and prohibited live issue queries, writes,
Git mutations, installation changes, agent spawning, and bookkeeping helpers.
The following original prompt and fixture bytes were unchanged:

| Case | Source | Exact-prompt SHA-256 |
| --- | --- | --- |
| native-issue-intake | Primary prompt in `2026-08-16-native-issue-intake-green.md` | `2ac27ec011624d4b096fb157a0ef55be865dd39f07e2e2c264d0c9d3adf768fc` |
| language-neutral | Variation in the same file | `2857f664741ec21781b3f6e05c54666624d4dcdd14452817051335612bb7e6cb` |
| lifecycle | `2026-08-16-lifecycle-transition-refactor.md` | `63c4844cae4b191bad34415ec19e4445b7c844f60301106526877dacbd95160d` |
| installation | `2026-08-16-superpowers-installation-refactor.md` | `6894bfb8deb9277196b6d00d8177587db54371d0bd85cdb8885d4dc1573bce99` |

Actual probe command events were inspected: they contain source/instruction
reads and read-only checks, not Git/GitHub mutations or bookkeeping helper
execution. Complete final responses are retained below; the original rubrics,
not process exit codes, determine the following scores.

## Scored expectations

| Check | Original expectations scored | Result and evidence |
| --- | --- | --- |
| skill-structure | Both exact skill names/frontmatter, linked references, placeholder scan | PASS, structural inspection above |
| native-issue-intake | Complete graph/PR fields; blocked/drifted execution refusal; layered authority; Backplane lifecycle without Project authority/IssueOps; project-owned verification/release rules; integrated acceptance and fresh checks before closure | PASS, 6/6; [capture](transcripts/2026-10-12-mac-v7-native-issue-intake.md) |
| language-neutral-verification | Only the supplied `cargo test --workspace`; no additional language/test workflow; native graph/revision binding; upstream sequence; open review until integrated verification | PASS, 5/5; [capture](transcripts/2026-10-12-mac-v7-language-neutral.md) |
| lifecycle-transitions | Invalid label cardinality fails closed; unrelated `security` preserved; evidence-based repair to review then active; recorded active resume target; target gates revalidated; atomic swaps with re-fetch verification | PASS, 6/6 acceptance expectations; [capture](transcripts/2026-10-12-mac-v7-lifecycle.md) |
| superpowers-installation | Reject lookalike/incomplete sibling without modification; unused authoritative destination; latest stable default; provenance/skills/capabilities/all checks/fresh discovery; authorized later changes and unknown fails closed; no required runtime/Project/IssueOps | PASS, 6/6; [capture](transcripts/2026-10-12-mac-v7-installation.md) |

Each expectation listed in the four original behavioral rubrics passed after
manual reading of its complete response. These are 23 scored expectations in
addition to structural verification and six-skill discovery. No RED finding
is fabricated for an unchanged skill reinstall.

## Evaluated Backplane identities

| File | SHA-256 |
| --- | --- |
| `skills/managing-superpowers-backlog/SKILL.md` | `739a16fcdf2ee5adab0514f5a44db0629dcce558985fe5a31d71dd2606ac1e81` |
| `references/github-issue-contract.md` | `d6dd8b8c2d1ea5836848fdac90aecf7002ab865dae612e94a560ebe7800d3121` |
| `references/installing-superpowers.md` | `50d82ccacbf71d368e983984157abe91d1fafd977f1f4d654c0fd58b5393329d` |
| `references/superpowers-binding.md` | `703435e24308513482da2ca7148de383b14305e3063abff08372b0e36ef7e6d6` |
| `skills/managing-superpowers-handoffs/SKILL.md` | `a6052755128be9c7d268d71241dd389b9bf1c720834e47e61cbf9535f4ca92de` |

The three reference paths in the table are relative to the backlog skill.
These hashes match the unchanged source used during the probes; neither skill
was modified. The Windows October 11 compatibility record remains historical.

| Captured response | SHA-256 |
| --- | --- |
| root discovery | `77cff5c21248cbd4bff665002adc2120b3e429ba1a487842c343bf7140662845` |
| native issue intake | `53878abe7b1af1fc3b3b124e75e7f02e04fbb8df5a7dd3161f247396c0d4d936` |
| language neutrality | `96084d1079e312aa2c821fe225cd82f40a3af356415ed0cefbcf1235713a8a3b` |
| lifecycle transitions | `102d5c510be0f56b3860e049156b36398bbedbd27059910bdba47469eea7fc40` |
| upstream installation | `f22b0699a0a147041d23090a0b3233cf8104801279c20af6f534106760c47617` |
| worktree discovery | `a8c4cb5eeaba94d5ffdfd230201a73afbfafe709394cd449bf345d4719b090e8` |

## Result

The restored Mac development checkout passes the five existing Backplane
conformance checks and fresh CLI discovery. This establishes the local setup
prerequisite for this evaluated tuple and process configuration. It does not
recover Windows execution progress, verify issue #31's new governance behavior,
complete its Task 1, or establish Claude Code/OpenCode compatibility.

The report and captures are local until committed and transported through an
authorized Git operation. No GitHub issue state was changed during verification.
