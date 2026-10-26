# Native relationship interpretation correction

During #11's real closure-capability failure probe, the installed skill's setup
response reported `2 sub-issues`. The captured native issue result contains
`subIssues: {nodes: [], totalCount: 0}`. Its jq summary used `.subIssues|length`,
counting the connection object's two keys instead of its zero issue entries.
The same response miscounted blocking relationships. Setup did stop at the
missing closure capability, and the before/after state was preserved; that
correct refusal does not make its graph summary accurate.

## RED

`uv run --no-project python .sp-bp/work/issue-11/check_relationship_counts.py tests/scenarios/2026-10-26-issue-11-gh-closure-failure.json`
failed with `Native sub-issue count must be 0, not object-key count [2]`.
The existing receipt retains the actual prompt, tool calls, result and native
JSON. This is an observed agent failure with the earlier reference, not a
constructed narrative or a failing document-string check.

## Minimal correction

The native issue reference now explains how to interpret arrays and connection
objects: traverse issue entries or `nodes`, compare with `totalCount`, retrieve
missing pages, and leave unverifiable relationships unknown. This implements
the existing complete-native-graph requirement; it changes no lifecycle,
public API, package identity or approved functional design.

`superpowers:writing-skills` was read before the edit. This is a reference
application failure, so conditional JSON-shape guidance is used; discipline
pressure combinations and behavioral-shaping wording micro-tests are not the
applicable test type. No SKILL frontmatter, discovery trigger or name changes.

## GREEN and remaining gate

The full current reference was read in fresh Claude session
`d7bea11d-5e37-45de-8be2-586c9f5c0826`. On the actual native snapshot it returned
exactly zero children, two blockers, one dependent, leaf=true and zero unresolved
blockers. The companion `2026-10-26-issue-11-relationship-reference.json` records
the prompt, actual Read call, expected/observed values and source digest.

This green application test is not installed-package acceptance. The revised
reference must be included in the selected immutable local candidate, installed
through the native package path and covered by the affected setup/conformance
checks before #11 acceptance. Existing C lifecycle observations remain at C;
the correction affects graph interpretation rather than native plugin lifecycle
commands. Final applicability and whole-change review must keep that distinction.
