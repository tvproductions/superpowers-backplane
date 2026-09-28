# Heavy derived-view freshness scenario

**Status:** RED for a released generator/checker. The candidate and approved ADR require generated `ROADMAP.md` and `BACKLOG.md`; this repository has neither a snapshot contract nor a project-owned generation/check command. The probes below establish what a passing implementation must demonstrate.

## Inputs and expected behavior

1. A fixture contains approved PRD revision `P1`, 105 issue records spanning more than one API page, native parent/blocker edges, a family move retaining outcome ID `C2.3`, and one outcome satisfying two requirements. Collection must include all 105 issues and both graph directions, irrespective of page boundaries or API order. Compare the collected issue count with an independent GitHub total or equivalent completion proof.
2. During collection, issue `#53` changes from revision `I1` to `I2`. The first collection must be discarded; after a bounded retry, the committed views must describe one coherent revision set. A change detected at the prepublication recheck prevents publication of those candidate bytes. Changes after that recheck are detected by the next freshness check; no GitHub read can guarantee that remote issues stay unchanged indefinitely. A timestamp alone is a revision detector, not evidence that the semantic field changed.
3. Duplicate semantic ID `C2.3`, a dangling required target, a malformed record, or a missing approved requirement anchor must fail validation. Neither view may silently omit the bad item.
4. A GitHub permission error, rate limit, incomplete page, or offline connection makes freshness `UNKNOWN`; cached bytes may be read as historical, but cannot be republished or reported current.
5. PRD revision `P2` changes one approved requirement. Both views and the trace change their input identity even when issue `updatedAt` values do not. Evidence linked to `P1` remains historical and is marked stale pending impact review.
6. With unchanged approved documents, complete issue records, native edges, and linked artifacts, repeating generation produces byte-identical views and the same source hash. A deliberate source change makes the project-owned freshness check fail until regeneration.

## Observed GitHub CLI probes on this repository

On 2026-09-27, authenticated `gh` 2.101.0 returned 21 issues with `gh issue list --state all --limit 100000 --json ... --jq 'sort_by(.number) | {count:length, first:.[0].number, last:.[-1].number}'`; an independent GraphQL `issues.totalCount` returned 21. REST `gh api ... --paginate --jq` traversed the current three five-item pages and emitted 21 issue rows. The installed `gh` rejected `--paginate --slurp --jq` with `the --slurp option is not supported with --jq or --template`. These are useful small-repository collection probes, not proof of a validated 105-record snapshot or source-race handling.

## Proof gate

The generator/checker must run from an installed SP-BP package on Codex, Claude Code, and both declared OpenCode variants, with Git and `gh` as the only required consuming-project tools. It must validate the full issue-and-document graph, record a canonical source hash, recheck source revisions before publication, retry or refuse on drift, reproduce bytes, and make the failure cases above observable. Until this is demonstrated, `ROADMAP.md` and `BACKLOG.md` are not generated or called current.
