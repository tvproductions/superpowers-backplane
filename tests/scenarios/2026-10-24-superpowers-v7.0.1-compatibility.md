# Superpowers v7.0.1 local compatibility

## Scope and recovery

The operator requested repository-only OpenCode installation, the stable
Superpowers 7.0.1 update, and README confirmation that gz-skills, Superpowers,
and Backplane are separate projects intended to work together. The original
OpenCode session was `ses_e91ea0382ffeoKz9CsAjO7pYTw`. Its recovered user
messages include: “Yes, do what you need to do to bring sp up to 7.0.1”.
The subsequent Codex recovery session
`01a16e2b-0f76-7bd1-834c-c19ec7343a7c` captured three fresh exact-prompt
responses before another interruption. This continuation inspected those
captures and ran the missing installation and discovery probes. Earlier
reformatted OpenCode prompts are not substituted for exact-prompt evidence.

Backplane is at `/Users/jbabb/Documents/Devel/superpowers-backplane`, `main`,
HEAD `c6f0b4a518e3742053618a613d8d858f0e37e9cd`; expected origin is
`https://github.com/tvproductions/superpowers-backplane.git`. `git ls-remote`
confirmed remote main at that commit. README, OpenCode configuration, and three
probe pairs were already unfinished on entry. No Git mutation, push, release,
or issue mutation was performed in this continuation.

## Candidate and preflight

- Prior recorded stable: `v7.0.0`, `bb92a77741419a4ab5f06e711a283343f1ada0c3`.
- Candidate: `v7.0.1`, `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`.
- `gh release view` identified 7.0.1 as latest stable on 2026-10-24, published
  `2026-10-21T21:05:11Z`.
- Release notes and the upstream 7.0.0-to-7.0.1 diff were reviewed. Changes
  refine brainstorming and move lengthy skill guidance to references; they do
  not change Backplane's native issue authority or verification ownership.
- Upstream origin is exactly `https://github.com/obra/superpowers.git`;
  `.agents/superpowers` is an independent, clean detached checkout. Peeled
  `v7.0.1` equals HEAD. All four required upstream skill files exist.
- Current upstream README installation guidance was retrieved through `gh api`.
  Installed OpenCode instructions document V2 `plugins` and tag-pinned package
  specs. Existing repository discovery links remain independently resolved.
- Observed tools: Git `2.54.0 (Apple Git-157)`, gh `2.103.2`, Codex `0.164.0`,
  OpenCode `2.1.4`. No machine tool was upgraded by this continuation.
- `gh auth status` succeeded. Complete native intake of issue #31 returned
  all 15 required fields: OPEN, Feature, exactly `backplane:review`, no parent,
  children, blockers, blocking issues, or closing PRs; revision remains
  `2026-10-13T07:27:56Z`.
- `gh issue edit --help` exposes add/remove label flags; `gh issue close
  --help` exposes closure reasons.
- Both Backplane skills pass YAML delimiters, exact names, `Use when`
  descriptions, all directly linked reference existence checks, and a scoped
  placeholder scan. No additional runtime is required by the project.
- `.superpowers/` and `.agents/superpowers/.superpowers/` are absent; no helper
  invocation or upstream file edit occurred in this continuation.

## Fresh conformance and scores

All four saved scenario prompts have exactly the original fenced prompt bytes.
The first three responses were recovered from separate fresh Codex probe
sessions earlier on 2026-10-24; they were read and scored in this continuation.
They are retained evidence, not newly executed responses in this continuation.
The installation probe ran in fresh ephemeral Codex session
`01a16e3c-7de0-74f2-8046-be1d9055da44`; discovery ran in
`01a16e3c-8360-7033-9b83-41318f73b14c`. Both exited zero, using effective
`gpt-6.1-sol`, medium effort, read-only sandbox, hooks and multi-agent disabled.
The behavioral preamble permitted instruction/skill reads and prohibited live
queries, mutation, helpers, and spawning; the original fixture followed verbatim.
No skill source changed between the recovered and new probes.

| Check | Scored expectations | Result and capture |
| --- | --- | --- |
| skill-structure | Both names/frontmatter, links, placeholders | PASS, preflight above |
| native-issue-intake | Complete graph/PR intake; blocked and drifted execution refusal; layered authority; native lifecycle without Project/IssueOps authority; project-owned verification/release; integrated acceptance before closure | PASS 6/6, [response](transcripts/2026-10-24-v701-native-issue-intake.md) |
| language-neutral-verification | Only supplied cargo command; no added runtime/test workflow; native graph/revision binding; upstream sequence; open review until integrated verification | PASS 5/5, [response](transcripts/2026-10-24-v701-language-neutral.md) |
| lifecycle-transitions | Invalid cardinality fails closed; unrelated labels preserved; review repair before rework; recorded active resume target; target revalidation; atomic swaps with re-fetch | PASS 6/6, [response](transcripts/2026-10-24-v701-lifecycle.md) |
| superpowers-installation | Reject unsafe sibling unchanged; unused authoritative destination; latest stable default; provenance/capabilities/all checks/discovery; later authorization and unknown fails closed; no runtime/Project/IssueOps requirement | PASS 6/6, [response](transcripts/2026-10-24-v701-installation.md) |

Fresh [Codex discovery](transcripts/2026-10-24-v701-discovery.md) found and read
using-superpowers, brainstorming, writing-plans, writing-skills, and both
Backplane skills from the advertised inventory. It resolved the discovery links,
verified distinct source trees, and confirmed the candidate revision and clean
checkout. Read-only Git returned zero despite macOS temporary-cache warnings;
the unrestricted controller independently confirmed clean upstream status.

## Prompt and response identities

Prompt files are stored beside their response with `.prompt.txt` in place of
`.md`. Discovery has its own saved prompt. The original four scenario prompts
match the historical exact-prompt digests in the October12 setup record.

| Case | Exact prompt SHA-256 | Response SHA-256 |
| --- | --- | --- |
| native-issue-intake | `2ac27ec011624d4b096fb157a0ef55be865dd39f07e2e2c264d0c9d3adf768fc` | `5e828357256bb0631f29913a86f02f9d151a74772c967c7c081a4fa553709980` |
| language-neutral | `2857f664741ec21781b3f6e05c54666624d4dcdd14452817051335612bb7e6cb` | `1433893f49b3e9d6ef451e4bd0c5945348b2530a25f01737e612c157186279b6` |
| lifecycle | `63c4844cae4b191bad34415ec19e4445b7c844f60301106526877dacbd95160d` | `ab914a9274abeddfed13dd5c8a366d4bc68d8efc5888d81c1de134d0231f1f0e` |
| installation | `6894bfb8deb9277196b6d00d8177587db54371d0bd85cdb8885d4dc1573bce99` | `b9438546edd50c2011bd8389ede77359cf66bc0115e5157cab65904a8695e3cd` |
| discovery | `d2e51c9f56246029647e4f0d2f9ccacd6260b796e3f2c21ebc52dcb38c8aec98` | `c92951cd235420c96217020fb3d13d89d29641ef5580ee3caa1047cf40f08213` |

Evaluated backlog skill SHA-256:
`168d5dffa43e89fae7249859f5758f3a46e53f03ea72e9bf1686983d49808f16`.
Handoff skill SHA-256:
`a6052755128be9c7d268d71241dd389b9bf1c720834e47e61cbf9535f4ca92de`.
Installation reference SHA-256:
`50d82ccacbf71d368e983984157abe91d1fafd977f1f4d654c0fd58b5393329d`.

## OpenCode observation and boundary

`opencode.jsonc` uses V2 `plugins` with only the native Superpowers package
spec pinned to `#v7.0.1`, and `skills: ["./skills"]`. It configures no gz-skills
package. The current native API request was:

```text
opencode api get /api/plugin --header x-opencode-directory:/Users/jbabb/Documents/Devel/superpowers-backplane
```

The returned location is this repository. Its `superpowers` package reports
`state.status=active`, the pinned package target, and version
`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. An initial `--param directory=...`
query returned the home location instead; that result is excluded from the
repository installation claim. Do not reuse it as project evidence.

The five checks establish direct Backplane compatibility with this independent
upstream checkout and the tested Codex configuration. The OpenCode API confirms
the repository plugin is active; the exact-prompt behavioral evidence above is
Codex evidence, not a fresh OpenCode behavioral suite. Complete-stack gz-skills
integration, other harnesses, and issue #31 satisfaction are not established by
this maintenance. Evidence remains local until separately authorized transport.
