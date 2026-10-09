#!/usr/bin/env python3
"""Validate the pack's intentionally constrained YAML and portable references."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

NAME = re.compile(r"pache-[a-z0-9]+(?:-[a-z0-9]+)*\Z")
PATTERNS = {
    "absolute-user-path": r"/(?:Users|home)/[^\s/]+|[A-Za-z]:\\(?:Users|apps)\\",
    "private-ip": r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b",
    "email": r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
    "credential-marker": r"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)",
    "secret-assignment": r"(?im)^\s*(?:api_key|password|access_token|client_secret)\s*[:=]\s*[\"']?[^\s\"'<>]{8,}",
}
TEXT_SUFFIXES = {'.md', '.py', '.json', '.txt', '.yml', '.yaml'}

def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    if len(lines) < 5 or lines[0] != '---':
        raise ValueError('frontmatter must start at byte zero')
    try:
        end = lines.index('---', 1)
    except ValueError as exc:
        raise ValueError('missing frontmatter terminator') from exc
    fields = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(':')
        if not sep or key not in {'name', 'description'} or key in fields:
            raise ValueError('expected unique name/description scalars only')
        value = value.strip()
        if key == 'description':
            value = json.loads(value)
        fields[key] = value
    name, desc = fields.get('name'), fields.get('description')
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        raise ValueError('invalid skill name')
    if name != path.parent.name:
        raise ValueError('name/directory mismatch')
    if not isinstance(desc, str) or not desc.strip() or len(desc) >= 1024:
        raise ValueError('description must be nonempty and under 1024 characters')
    return fields

def validate(root, deny_terms=()):
    root = Path(root).resolve()
    errors, count, links = [], 0, 0
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if any(part in {'.git', '__pycache__'} for part in rel.parts):
            continue
        if path.is_symlink():
            errors.append(f'{rel}: symlink forbidden')
            continue
        if not path.is_file():
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {'LICENSE', '.gitignore'}:
            errors.append(f'{rel}: unexpected/binary file')
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            errors.append(f'{rel}: unreadable UTF-8')
            continue
        for label, pattern in PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f'{rel}: privacy pattern {label}')
        for term in deny_terms:
            if term.strip() and term.casefold() in text.casefold():
                errors.append(f'{rel}: private deny-list match (value withheld)')
        if path.name == 'SKILL.md':
            count += 1
            try:
                frontmatter(path)
            except (ValueError, TypeError) as exc:
                errors.append(f'{rel}: {exc}')
        if path.suffix == '.json':
            try:
                json.loads(text)
            except ValueError:
                errors.append(f'{rel}: invalid JSON')
        if path.suffix != '.md':
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            target = unquote(target.split('#', 1)[0])
            if not target:
                continue
            if re.match(r'https?://', target):
                continue
            links += 1
            candidate = (path.parent / target).resolve()
            boundary = root
            if rel.parts[0] == 'skills' and len(rel.parts) > 2:
                boundary = root / 'skills' / rel.parts[1]
            if Path(target).is_absolute() or not candidate.is_relative_to(boundary) or not candidate.is_file():
                errors.append(f'{rel}: missing/escaping local reference')
    if count == 0:
        errors.append('no skills found')
    expected = list((root / 'skills').glob('*/SKILL.md'))
    if len(expected) != count:
        errors.append('unexpected nested skill layout')
    return {'status': 'FAIL' if errors else 'PASS', 'skills': count, 'local_links': links, 'errors': errors}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--deny-file', type=Path, help='Private, external newline-separated terms; never bundled')
    args = parser.parse_args()
    terms = args.deny_file.read_text().splitlines() if args.deny_file else ()
    result = validate(args.root, terms)
    print(json.dumps(result, indent=2))
    return bool(result['errors'])

if __name__ == '__main__':
    sys.exit(main())
