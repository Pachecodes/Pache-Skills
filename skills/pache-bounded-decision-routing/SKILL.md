---
name: pache-bounded-decision-routing
description: "Use when evaluating bounded routing with shadow calibration."
---

# Bounded Decision Routing

## When to use
Use for choosing among known workflow/model options or freshly observed interface candidates. It is not a permission system or a generative content workflow.

## Prerequisites and authority
Require a finite option set, labeled examples, an existing authorized adapter if a decision model is used, and independent outcome measurement. Do not install hooks, buy access, or change live routing just because this skill is invoked.

## Procedure
1. Build a deterministic rule or lexical baseline first. Fixed ownership and access policy are configuration, not model judgments.
2. Ask one atomic question using mutually exclusive options and an abstain/none choice. Independent questions can be batched; dependent questions require refreshed state.
3. Minimize inputs to privacy-safe structured facts. Compute counts and timing with code; omit secrets, raw identities, private paths, and full conversations.
4. Inspect the actual adapter/provider schema. Pin the evaluated model and validate enums, finite numbers, and malformed responses. Missing capabilities mean advisory unavailable, not an invented recommendation.
5. Measure accuracy, false allows/blocks, fallback frequency, latency, usage, and verified downstream completion on labeled cases. Compare against the deterministic baseline.
6. Replay offline, then shadow without changing actual permissions or behavior. Test label removal/flips, injected instructions, missing input, and distribution changes. Confidence is not correctness.
7. For UI selection, obtain candidates from current observation, deterministically remove forbidden/destructive actions, and reject stale candidates before execution. Reobserve after every mutation.
8. Activate only with explicit approval and meaningful measured benefit. Preserve deterministic authorization and a rollback path. A model may recommend a choice but cannot authorize spending, deletion, publication, access, or completion.

## Acceptance and delivery
Return recommendation, abstention/uncertainty, calibration evidence, baseline comparison, and activation status. When calibration is absent, preserve current/manual routing and report NOT ACTIVATED.

## Example prompt
“Evaluate this finite router offline against labeled cases and a rule baseline; shadow only, with no permission or production-routing changes.”
