# Contributing

Submit one broadly reusable workflow at a time. State its trigger, prerequisites, authority limits, procedure, deterministic acceptance, failure modes, and example prompt. Prefer substantive standalone procedures over incident diaries or empty skeletons.

Provide provenance: original author/steward, source identifier where applicable, permission/license, and transformation. Do not contribute imported skills with superficial renaming, private client narratives, credentials, hostnames, local paths, or proprietary media. Generic concepts may overlap other work; do not assert exclusive invention.

Use a `pache-` lowercase-hyphenated directory/name and byte-zero YAML frontmatter with a non-empty description. For this pack use only plain name plus JSON-quoted description scalars; the dependency-free validator intentionally accepts this constrained YAML subset. Keep descriptions under 1024 characters. Link local support files explicitly and keep all dependencies within the individual skill for portable installation.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. Add negative tests for tooling changes. Review capability assumptions, privacy scan findings, link closure, and source rights independently. Never weaken a privacy check without a documented reason and independent approval. No test may write to an actual agent home or invoke paid/live providers.

Keep the public repository free of execution transcripts. Reports from private curation/review belong outside it. Publication and pushes require separate owner approval after review.
