# Issue #5 context-aware native recommendation

The corrected native probe passes the scoped checks for recommendation-only
state preservation, no invented priority or selection, and recognizing that
approved local fixture verification does not require plan publication. This is
supplemental evidence, not accepted completion of #5 or a new lifecycle run.

## Authority and tested fixture

After automatic approval review rejected the initial launch, the operator
explicitly approved sending public `AGENTS.md` and public GitHub issue context
to Anthropic through the retained isolated Claude profile. Claude Code 2.1.311
ran in the owned neutral fixture using that profile; no credentials were copied
and no normal profile was used. Tested main was
`24991b7157dcf6db954cb95ebf6d28582da37f47`.

The first attempt omitted the session-only upstream plugin argument used by the
previous passing discovery test. It correctly reported `Unknown skill` for
upstream, while loading Backplane and answering the local-verification question.
That attempt remains a failed prerequisite fixture, not complete installed-stack
acceptance. Its state and protected-file comparisons nevertheless passed.

The distinct corrected attempt added only session-scoped
`--plugin-dir .agents/superpowers`, using the independently verified clean
`obra/superpowers` checkout at stable 7.0.1,
`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. No persistent plugin setting or
shipped upstream file was changed. Actual native Skill calls loaded
`superpowers:using-superpowers` and
`superpowers-backplane:managing-superpowers-backlog` from separate roots.

## Observed behavior and preservation

The corrected response made no selection and invented no priority. It correctly
reported zero ready-labelled issues, kept the current backlog labels separate
from approved local-verification authority, and explicitly answered that local,
unpublished approval can authorize reversible fixture verification under the
supplied `AGENTS.md`. It did not treat a handoff as authorization or completion.

Whole before/after REST issue pages, full #5 native intake and the captured
protected-file hashes are identical for both attempts. The successful shell
commands were public `gh issue list` and `gh issue view` reads. Glob and compound
shell-loop requests were denied; plain single-issue reads subsequently succeeded
within the original allowlist. No permissions were widened. This is evidence
about those observed calls and snapshots, not a blanket claim about every file
on the machine. No remote issue mutation, fixture issue, lifecycle transition,
publication, closure or release occurred.

## Limits of the readiness advice

Accept the narrow local-verification answer. The corrected response additionally
asserts that an unpublished plan cannot serve as a native artifact link and
therefore cannot meet issue eligibility gates. The hypothetical did not establish
whether a usable approved authority reference was already present; do not adopt
that assertion as a universal publication requirement. Other incomplete-context
advice, such as the native body not recording the selected license, is not a new
project finding: the integrated license and verified operator decision remain
governed by the existing source and receipts.

The new runs do not prove why the original context-free probe added a publication
gate. Project instructions, current remote plan bindings and fixture inputs
differ from that historical run. No skill text changed, and a skill rewrite is
not demonstrated as necessary by this test. Broader readiness advice remains
subject to the current contract and independent review, rather than becoming
authority through a model response.

## Current graph and retained evidence

Fresh complete native intake covers all 23 repository issues, excluding PRs.
All 12 open issues have exactly one valid lifecycle label; all closed issues
have none. Native connection node counts match totals, #1 has 17 children with
8 closed, parent relationships are reciprocal, and all 22 dependency edges
have reciprocal blocking entries. These intakes match the unchanged issue set
and revisions captured immediately around the probe. #4/#5 remain OPEN/backlog
at `2026-11-01T22:00:15Z` and `2026-11-01T22:00:18Z`.

The canonical `skills/` diff from #11's accepted delivery `7359019` to the
tested head is empty. The prior #11/#34 lifecycle evidence therefore retains
its previously assessed bounded applicability; no historical host or lifecycle
acceptance was repeated. The original #5 assessment and approved plan bytes
remain unchanged at their original identities.

Fresh package tests pass 9/9, evidence-helper tests 23/23, and the four existing
helper/test files pass Ruff, formatting and ty. The
[screened native receipt](transcripts/2026-11-01-issue-5-context-recommendation.json),
[first capture source](transcripts/2026-11-01-issue-5-resume-acceptance-probe.py.txt),
[corrected capture source](transcripts/2026-11-01-issue-5-resume-acceptance-upstream-probe.py.txt), and
[quality output](transcripts/2026-11-01-issue-5-context-quality-gate.txt)
preserve the new claims. This report does not resolve Codex discovery or #4's
remaining operation-specific and OpenCode acceptance gaps.

Fresh [review and fix disposition](2026-11-01-issue-5-context-review.md) found one
Important evidence-retention gap. The corrected receipt now retains actual
successful Skill results, verified by an assertion-level RED/GREEN control.
The full existing quality gate passed again after that evidence-only fix.
No review finding remains unresolved. No second independent review is claimed.
