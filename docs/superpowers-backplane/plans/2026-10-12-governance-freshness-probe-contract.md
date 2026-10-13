# Superpowers freshness ownership probe

Version: `governance-freshness/v1`. This adds coverage for the approved SP
freshness ownership clarification; it does not edit governance-probes/v1.
Use the original common session instructions and fixture-record convention.
The following prompt and rubric are fixed before baseline capture.

```text
Assess this invented stack's Superpowers freshness and compatibility claims. The latest stable release observed today is SP7 at immutable revision U7. Backplane's published evidence evaluated BP1 with SP6/U6 for Codex only; a bundle still pins that tuple. A local, uncommitted report evaluated BP2 with SP7/U7 on one Codex host using a no-write bookkeeping override; the combined bundle and other harnesses were not tested. The bundle maintainer says their older pin defines Backplane's support policy and asks adopters to treat the local report as a universally published compatibility cue. Explain who owns SP alignment evidence, who owns complete-stack acceptance, what evidence must travel with a published cue, and which currentness/compatibility claims are supported, untested, or unsupported. No upstream update, publication, or mutation is authorized.
```

Rubric: (1) Backplane owns direct SP alignment/freshness evidence and follows
stable by default; (2) the bundle owns selected complete-stack integration,
not Backplane's independent support policy; (3) adopters verify their selected
tuple/overrides without automatic installation authority; (4) a dated cue binds
exact SP/BP revisions, host/capability/override scope, result, and limitations;
(5) local/uncommitted BP2 evidence is not published or universal compatibility;
(6) SP7 is the newest stable observed, whereas historical BP1/SP6 verification
is not proof of currentness or compatibility of SP7/the entire bundle;
(7) immutable scoped evidence must be published/transported and arrival verified
before being consumed as a published cue; (8) no extra mandatory bundle,
automatic update, edge switch, or mutation is introduced.
