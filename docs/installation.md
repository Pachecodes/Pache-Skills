# Installation

[Back to README](../README.md#preview-first-install-only-by-choice)

## Non-destructive, opt-in installation

1. Read the selected skill, provenance, [SECURITY.md](../SECURITY.md), and all bundled scripts before trusting them.
2. Validate locally: `python3 scripts/validate.py`.
3. Preview selected copies into an explicitly chosen skills directory: `python3 scripts/install.py --dest <chosen-skills-directory> --skill pache-artifact-first`.
4. Add `--apply` only after approving the displayed destinations. No default directory, overwrite, deletion, global configuration, scheduler, or hooks are provided.
5. Inspect copied files and load one skill through your runtime's actual supported mechanism. A successful copy is not automatic-discovery or runtime acceptance.

Use a disposable destination first. Do not point a test at a real home. Determine your agent's supported destination from its current official documentation rather than guessing from another agent's layout. Prefixes reduce collisions but do not make installation safe by themselves. Removal is manual: remove only directories you explicitly installed after checking ownership.
