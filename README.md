# Pache-Skills

A curated pack of eight original, generalized agent procedures by Pachecodes / Jesus Pacheco / Akitá Labs. These are opt-in instructions, not a running service, sandbox, approval grant, vendor plugin, or replacement for agent policy. No client artifacts, upstream skill library, vendor adapters, media, or credentials are included.

## Catalog and prompts

See [CATALOG.md](CATALOG.md) for triggers and example prompts. Each skill is a self-contained directory under `skills/`, with standard `name` and `description` frontmatter. The feature-loop template travels with its skill. [PROVENANCE.md](PROVENANCE.md) records source identifiers, authorship evidence limits, and transformations; it does not claim authorship of the general engineering concepts.

## Capabilities, not universal tool names

| Runtime | How to adapt |
| --- | --- |
| Hermes | Use the installed skill loader or explicitly read SKILL.md; map file/process/delegation/verification steps to enabled tools. Home/profile selection is installation-specific. |
| Claude Code | Use the installed release's supported skill discovery or explicitly read SKILL.md; inspect current help/docs for scope and permission options before using them. |
| Codex | Use the installed release's supported skill discovery or explicitly read SKILL.md; inspect current help/docs for sandbox and worker support. |

All three can use the documents as instructions when file reading is available. Automatic discovery and invocation syntax depend on release and configuration; they were not tested in this pack. No particular subagent, browser, scheduler, mobile tool, or API is universally available. Missing capabilities produce a precise blocker. Never simulate unavailable execution or call a sequential self-review independent review.

Prerequisites: an instruction-following agent with authorized file reads; relevant workflow-specific execution/observation tools; project runtime and isolated fixtures for software checks. Repository validation and the optional copy installer need Python 3.10+ only, with no third-party packages or network.

## Non-destructive, opt-in installation

1. Read the selected skill, provenance, [SECURITY.md](SECURITY.md), and all bundled scripts before trusting them.
2. Validate locally: `python3 scripts/validate.py`.
3. Preview selected copies into an explicitly chosen skills directory: `python3 scripts/install.py --dest <chosen-skills-directory> --skill pache-artifact-first`.
4. Add `--apply` only after approving the displayed destinations. No default directory, overwrite, deletion, global configuration, scheduler, or hooks are provided.
5. Inspect copied files and load one skill through your runtime's actual supported mechanism. A successful copy is not automatic-discovery or runtime acceptance.

Use a disposable destination first. Do not point a test at a real home. Determine your agent's supported destination from its current official documentation rather than guessing from another agent's layout. Prefixes reduce collisions but do not make installation safe by themselves. Removal is manual: remove only directories you explicitly installed after checking ownership.

## Verification and limitations

`python3 -m unittest discover -s tests -v` exercises validation failures and installation in disposable fake homes, including collision refusal, explicit apply, traversal rejection, symlink refusal, and byte-for-byte copies. Tests make no agent/API calls. Privacy regex checks are a heuristic, not a proof of anonymity or legal ownership. Releases require independent content, privacy, and provenance review; passing the validator alone is not a release approval.

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md). License: [MIT original pack content](LICENSE).
