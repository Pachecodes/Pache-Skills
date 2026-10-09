#!/usr/bin/env python3
"""Copy explicitly selected skills; preview by default, never overwrite."""
import argparse
import json
from pathlib import Path
import shutil
import sys
from validate import NAME, validate

ROOT = Path(__file__).resolve().parents[1]

def no_symlinks(path):
    path = Path(path).absolute()
    for parent in [path, *path.parents]:
        if parent.is_symlink():
            raise ValueError('symlink destination/source refused')

def install(root, dest, names, apply=False):
    root, dest = Path(root).absolute(), Path(dest).absolute()
    no_symlinks(root)
    no_symlinks(dest)
    result = validate(root)
    if result['errors']:
        raise ValueError('pack validation failed')
    if not names or len(set(names)) != len(names):
        raise ValueError('select unique explicit skill names')
    if dest.exists() and not dest.is_dir():
        raise ValueError('destination is not a directory')
    planned = []
    for name in names:
        if not NAME.fullmatch(name):
            raise ValueError('invalid skill name')
        source = root / 'skills' / name
        target = dest / name
        no_symlinks(source)
        if not (source / 'SKILL.md').is_file():
            raise ValueError('skill not found')
        if target.exists() or target.is_symlink():
            raise FileExistsError('existing skill refused: ' + name)
        planned.append((source, target))
    output = {'mode': 'apply' if apply else 'preview', 'skills': [x.name for _, x in planned], 'destinations': [str(x) for _, x in planned]}
    if not apply:
        return output
    # Preflight all selections before writing. Refuse concurrent/adversarial writers.
    dest.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for source, target in planned:
            target.mkdir(exist_ok=False)
            created.append(target)
            for item in source.iterdir():
                if item.is_dir():
                    shutil.copytree(item, target / item.name)
                else:
                    shutil.copy2(item, target / item.name)
    except Exception:
        # Roll back only directories this invocation exclusively created.
        for target in created:
            shutil.rmtree(target)
        raise
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, type=Path)
    parser.add_argument('--skill', action='append', required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(install(ROOT, args.dest, args.skill, args.apply), indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
