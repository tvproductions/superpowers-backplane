# Independent whole-change review

Reviewer: fresh gpt-6-astra, max reasoning, read-only; Git range 82fa208cd81b1ae33a6b24e869220f90c9558312..1fd90dffd2de585520677c414d8e99b29b55dc41.

The authority, decomposition, PR, lifecycle, and preservation guidance is consistent with D1–D8. It distinguishes historical evidence, current satisfaction, native closure, checkpoint acceptance, and publication. All40 recorded prompt/response hashes and final source hashes match. Approved authorities remain unchanged;18 recorded validator outcomes reproduce in memory;K0/K1 contain only the invented pair.

Critical: None. Important: None (reviewer grades; executor regrades below).

Minor1: Specify terminal-cursor normalization. checkpoint-format.md:47 retains observed GraphQL cursor identities, while the captured validator requires final cursor_out=null. It does not distinguish raw endCursor from continuation derived from hasNextPage. An adopter may reject a complete nonempty collection or normalize it inconsistently. Define mapping and add a nonempty multiple-page positive fixture. The reviewer's in-memory non-null terminal-cursor fixture was rejected.

Minor2: Reconcile unavailable collections with declared types. checkpoint-format.md:57 requires arrays for labels/relationships;line68 requires unavailable fields null and forbids converting denied queries to empty arrays. Permission-limited diagnostics lack an unambiguous conforming representation. The validator rejects labels:null even with partial status and a limitation. Define nullable collections or precise availability convention and demonstrate denial.

Minor3: Keep disposable validator acceptance narrowly scoped. checkpoint-validation.json:230 accepts integrated Project data without Project collection/page records when Satisfaction matches;also accepts complete status with unavailable issue body. Operational guidance correctly rejects these. This is a verification gap, not a shipped runtime defect. Add negatives or explicitly identify unimplemented constraints beside acceptable.

ReviewFocus1–3 have clear source rules/supporting behavioral responses;Focus4 has the minor representation/validation gaps;Focus5 is supported by helper prohibition, preserved upstream, narrow ignore rule and file/Git exercise.

Declined to judge:
- Live multipage GitHub/Project capture, permission behavior and concurrent drift: no complete live capture;#31 observation covers empty terminal connections.
- Production recovery: invented test paths establish exercised file/index/tree behavior.
- Remote integration, other-host arrival, integrated satisfaction and release: none occurred.
- Other harnesses and bundle compatibility: scope is the recorded Codex tuple.
- Windows completion: predecessor evidence unavailable.
- General production validator: outside skills-only scope;disposable validator assessed only as evidence.
- Finishing/submission/post-integration closeout: subsequent gates.

Reviewer assessment: Ready to merge: Yes, with minor follow-ups recorded. No Critical/Important blocker. Resolve format ambiguities before first real checkpoint capture.

Optional live-query limitation: network failed;automatic approval review rejected escalation of read-only gh api graphql targeting tvproductions/superpowers-backplane issue1/subIssues(first:100){totalCount,pageInfo{hasNextPage,endCursor},nodes{number}}. Stated reason: prohibition on live queries and unrelated issue/repository target. No retry/alternative live path;local artifacts sufficient for reviewed scope.

Executor disposition:
- Findings1/2 regraded Important by adopter impact: a valid complete nonempty capture can be rejected, and required denied-source diagnostics cannot conform without ambiguity. They enter one TDD fix pass;no re-review is dispatched.
- Finding3 stays Minor/deferred: this is explicitly disposable evidence, no shipped production validator. Its18 exercised outcomes do not prove all schema/semantic constraints. In particular, complete status with unavailable body and missing Project paging are outside its enforced constraints. Operational full capture guards still apply;never use this source as a production acceptance engine.
- All declined items remain proof limits. Local fixture/support evidence is enough for the authorized skills-only slice;none is promoted to live/remote/bundle/Windows verification. Finishing remains required;submission/integration/release need authority. Cost if wrong: a future real capture/integration requires its own current evidence before acceptance, and must fail closed on these unverified conditions.


## One-pass resolution

The two regraded Important findings are fixed. Frozen native-edge fixtures
reproduced both failures before changes. Explicit has_next_page preserves native
terminal endCursor; nullable collections preserve denial with partial metadata.
The candidate passes original18 plus5 edge outcomes,23/23. The unchanged full
suite passes64 governance/freshness and23 existing expectations at one corrected
bundle, with structural checks and source/authority/preservation audits passing.
Observed test verification closes the one fix pass; no second reviewer is used.
The broader disposable-validator coverage gap remains deferred and explicitly
scoped. Local reviewed implementation is ready for the finishing decision;
submission/integration/closeout are subsequent authorized operations.
