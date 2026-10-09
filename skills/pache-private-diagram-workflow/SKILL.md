---
name: pache-private-diagram-workflow
description: "Use when rendering evidence-backed private diagrams."
---

# Private Diagram Workflow

## When to use
Use for an architecture, process, sequence, or state diagram where factual grounding and renderer privacy matter. This is a general procedure, not a bundled renderer or vendor API client.

## Prerequisites and authority
Require source evidence, audience, authorized output location, and a vetted local/private renderer or explicit authorization for public-source transmission. A public diagram service receives source. Encoded share links are reversible, not encrypted.

## Procedure
1. Identify the question, boundaries, components, and relationships from evidence. Mark observed versus proposed elements; do not invent connectivity to fill whitespace.
2. Choose notation and renderer based on installed capabilities. Verify its actual command/API contract, include behavior, network access, license, and source handling before use.
3. Keep private identities, endpoints, source paths, and credentials out of diagrams. If sensitive structure itself must remain private, use an approved local/private renderer. Missing capability yields a labeled source draft and BLOCKED render, never a silent public fallback.
4. Write editable source with stable aliases, concise labels, directional relationship verbs, and trust/ownership boundaries. Provide an accessible text equivalent.
5. Avoid remote includes or fetched icon libraries without review. Their licensing, network disclosure, and executable/include behavior are separate from the renderer license.
6. Check syntax, then render the actual source. Verify output status and media type. An error response renamed as an image is not an artifact; treat SVG as potentially active content.
7. Inspect the real output for clipping, labels, arrows, scale, and readability. Reconcile every important relationship with evidence. Split complex systems into overview and detail views.
8. Keep editable source with the verified output. Validate final physical readability when embedding in documents; preserve unrelated original pages.

## Acceptance and delivery
Deliver source, render, text equivalent, evidence/assumptions, renderer privacy classification, and actual checks. Rendering proves syntax/runtime, not architectural truth. Source-only delivery is unfinished unless explicitly requested.

## Example prompt
“Make a diagram from these generic facts using an available local renderer, inspect the output, and do not send source to a public service.”
