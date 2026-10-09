---
name: pache-artifact-first
description: "Use when creating a verified explanation or decision artifact."
---

# Artifact First

## When to use
Use when a user explicitly asks for an artifact, visual explanation, comparison, or working demonstration. Do not generate files for an advice-only question.

## Prerequisites and authority
Know the audience, decision, evidence, output location, and available rendering/test capability. A request to explain does not authorize publication, paid generation, external transmission, or deployment. Use synthetic inputs. If the requested renderer is unavailable, deliver a labeled draft and a precise blocker, not a fictional render.

## Procedure
1. State the question the artifact must answer and identify observed facts, assumptions, and proposed behavior.
2. Choose one format: clear text for instructions; a rendered diagram for relationships; interactive HTML for comparisons or calculations; narrated media only when movement or narration materially helps. Avoid producing every format.
3. Write short steps with consistent terms. Preserve qualifications and safety conditions. Plain language is not certification to a controlled-language standard.
4. Produce editable source and the requested usable output. A screenshot is not a working calculator; source markup is not a rendered diagram; a storyboard is not a video.
5. Check calculations with executable assertions independent of visual appearance. Include units, empty input, invalid input, limits, and representative expected results.
6. Render and inspect the output. Exercise controls, reset, reload, keyboard navigation, narrow screens, and error states for interactive content. Check actual labels and arrows for diagrams. Check duration, frames, captions, and audio for media.
7. Inspect dependency and data disclosure risks. Keep private assets out of externally hosted previews. Never embed credentials in a self-contained artifact.

## Acceptance and delivery
Return the artifact location, editable source, evidence, actual checks, assumptions, and limitations. Mark each required check PASS, FAIL, BLOCKED, or NOT TESTED. A prototype remains a prototype even when its demonstration passes.

## Example prompt
“Use artifact-first to compare these synthetic options in a local interactive page; test invalid inputs and do not publish.”
