# ADR-0001 edition 1: actual approval capture

Agent transcription of the actual human interaction in the current GZ Starter
release conversation, November 15, 2026. No retrievable conversation URL is
available; none is invented. Approver identity: project maintainer in this
conversation. A source/content reference identifies reviewed bytes; the actual
human response below supplies approval.

## Exact reviewed content

- Owning repository: `tvproductions/superpowers-backplane`.
- Identified decision/edition: **ADR-0001, edition 1**.
- [Reviewed proposal](https://github.com/tvproductions/superpowers-backplane/blob/335bd2575eeaae92ce094582cd11dccf18f37b41/docs/superpowers-backplane/specs/proposals/ADR-0001-001-reference-decisions-through-existing-checkpoints.md).
- Exact preserved bytes: [ADR-0001-001-reviewed.txt](ADR-0001-001-reviewed.txt).
- SHA-256: `5a39dcb0db8553af4a30d4acdbd57461c9a62d9a2f72da285caa57ceb0630d7b`.
- [Associated design](https://github.com/tvproductions/superpowers-backplane/blob/335bd2575eeaae92ce094582cd11dccf18f37b41/docs/superpowers-backplane/specs/2026-11-15-architectural-decision-integration-design.md); design approval remains a separate act.

## Actual approval interaction

The assistant presented a separate approval prompt explicitly naming this
repository's ADR-0001 edition 1, linking the immutable proposal above and
summarizing the choice. It stated that this architectural approval was separate
from design approval and required before implementation.

The human responded verbatim:

> Approve Backplane ADR-0001 edition 1 as written

Source context: `request_user_input_async`, call
`call_7f0c8bd7210a4775811665fe08360a35`, question item
`2`, delivered as a user `send_user_message_question_reply`.
The separate design answer was “Approve both designs as written”. Neither that
answer nor a release request is being substituted for the architectural answer.

## Main-conversation review and subsequent direction

After those responses the maintainer said review should happen in the main
conversation, rather than side questions. The assistant stopped implementation
and reviewed the responsibility split and design there. The maintainer accepted
the split (“ok”) and the gz-skills design (“yes”), then requested the remote
GZKit drydock naming precedent. The assistant inspected its exact current source
and proposed the H5 width/slug clarification. The maintainer then said:

> proceed with that design

These later responses establish the requested design/review continuation; they
are not treated as new architectural approval. The earlier explicit named-edition
architectural response remains separately preserved above, and no implementation
was used to skip the requested main-conversation review. The added naming citation
clarifies the design's existing decision/edition convention; it does not replace
the original approved architectural choice or import GZKit machinery.

## Administrative capture

The Current decision is derived from the exact original proposal above. Blank
administrative metadata, draft labels and pending approval text are reconciled;
the decision's architecture is unchanged. Relative design links are repaired for
the authoritative location. Later draft naming commentary remains attributable
to the design review and is not falsely presented as part of the earlier reviewed
proposal bytes. No implementation, behavior qualification or publication result
is asserted by this approval record. Implementation-plan review remains pending.
