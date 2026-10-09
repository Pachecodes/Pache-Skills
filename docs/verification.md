# Verification

[Back to README](../README.md#guides-and-evidence)

`python3 -m unittest discover -s tests -v` exercises validation failures and installation in disposable fake homes, including collision refusal, explicit apply, traversal rejection, symlink refusal, and byte-for-byte copies. Tests make no agent/API calls. Privacy regex checks are a heuristic, not a proof of anonymity or legal ownership. Releases require independent content, privacy, and provenance review; passing the validator alone is not a release approval.

Run from the repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks do not install into live agent directories, exercise automatic skill discovery, or establish production acceptance. The tests use disposable copies and fake homes.

The unchanged validator permits text formats only; standalone SVG files are rejected. The overview is therefore stored as SVG source inside a Markdown document. Render its fenced SVG locally for visual inspection; do not add generated images to the pack without a separately approved format-policy change.
