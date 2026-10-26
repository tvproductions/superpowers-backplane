# Carrying verified authorization through a workflow

The current installed-package language-neutral conformance response correctly
described most required transitions but added: "Only the start transition is
covered by what you've asked so far." It required a new go-ahead for submission,
although the exact scenario explicitly asks to start and submit after
implementation. Closure was requested as an explanation, so actual closure
correctly needs its own authority in this scenario.

The operator had independently flagged the same unnecessary approval behavior
in this session. The approved adoption design already states that explicitly
starting/preparing/submitting work authorizes its evidence-gated transition
without redundant confirmation. The native mutation reference did not make the
scope/carry-forward rule explicit alongside its mechanical mutation sequence.

## RED

`check_authorization_scope.py` rejected the actual current-candidate response
from `conformance-current/language-neutral-verification-response.md`. Its
assertion records that the prompt authorizes both start and submission, not just
start. The earlier response and exact prompt must remain available in the
tracked conformance transcript; the five legacy language-neutral expectations
alone do not detect this extra approval gate.

## Minimal reference correction

The native issue contract now resolves each intended action into its verified
operator authority and current evidence gate. An explicit start-and-submit
instruction covers both once their conditions hold. Explaining closure does
not authorize closing; project publication/integration/release rules remain in
force. Timing alone does not invalidate existing verified scope.

This is a missing contract-definition/reference application correction, not a
new lifecycle or an instruction to ignore permission boundaries. It applies the
already approved design. The writing-skills workflow was loaded before editing.
The conditional is keyed to an observable request/approval; no frontmatter,
discovery trigger, name or output-style change is introduced.

## GREEN and installed regression gate

The exact original language-neutral scenario was replayed in a fresh context
with the full current skill source and its required references. Session
`137a7e99-8c9a-4128-8f82-3d7372d46a9a` actually read the revised contract and
explicitly carried authority for start and submission, while treating closure
as explanation only. The unedited response and source digest are in
`2026-10-26-issue-11-authorization-reference.json`.

This reference application result is separate from installed-package acceptance.
Install the immutable revised package and rerun the affected conformance before
claiming final candidate verification. The old extra-approval response remains
an observed failure, even though its legacy rubric entries otherwise passed.
