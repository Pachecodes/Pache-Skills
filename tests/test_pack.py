import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate import frontmatter, validate
from install import install

class PackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pache-test-', dir=os.getenv('TMPDIR'))
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.fake_home = self.base / 'fake-home'
        self.fake_home.mkdir()
        self.pack = self.base / 'pack'
        shutil.copytree(ROOT, self.pack, ignore=shutil.ignore_patterns('__pycache__', '.git'))
        self.name = 'pache-artifact-first'
        self.skill = self.pack / 'skills' / self.name / 'SKILL.md'
        self.dest = self.fake_home / 'opt-in-skills'

    def test_valid_pack(self):
        result = validate(self.pack)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['skills'], 8)

    def test_frontmatter_name_mismatch(self):
        self.skill.write_text(self.skill.read_text().replace('name: '+self.name, 'name: pache-other', 1))
        self.assertTrue(validate(self.pack)['errors'])

    def test_frontmatter_byte_zero(self):
        self.skill.write_text('\ufeff' + self.skill.read_text())
        self.assertTrue(validate(self.pack)['errors'])

    def test_description_required(self):
        text = self.skill.read_text().splitlines()
        self.skill.write_text('\n'.join(line for line in text if not line.startswith('description:')))
        self.assertTrue(validate(self.pack)['errors'])

    def test_description_length(self):
        lines = self.skill.read_text().splitlines()
        lines[2] = 'description: ' + json.dumps('x' * 1024)
        self.skill.write_text('\n'.join(lines))
        self.assertTrue(validate(self.pack)['errors'])

    def test_duplicate_frontmatter(self):
        self.skill.write_text(self.skill.read_text().replace('\n---\n\n#', '\nname: '+self.name+'\n---\n\n#', 1))
        self.assertTrue(validate(self.pack)['errors'])

    def test_missing_reference(self):
        self.skill.write_text(self.skill.read_text() + '\n[Missing](references/absent.md)\n')
        self.assertTrue(validate(self.pack)['errors'])

    def test_reference_cannot_escape_skill(self):
        self.skill.write_text(self.skill.read_text() + '\n[Escape](../../README.md)\n')
        self.assertTrue(validate(self.pack)['errors'])

    def test_privacy_patterns(self):
        probes = ['/'+'Users'+'/'+'fixture'+'/file', '.'.join(['192','168','7','9']), 'fixture'+'@'+'example.invalid', 'sk-'+'a'*24, 'password'+': '+'x'*12]
        original = self.skill.read_text()
        for probe in probes:
            with self.subTest(probe=probes.index(probe)):
                self.skill.write_text(original + '\n' + probe)
                self.assertTrue(validate(self.pack)['errors'])
        self.skill.write_text(original)

    def test_external_deny_terms(self):
        self.assertTrue(validate(self.pack, ['artifact-first'])['errors'])

    def test_symlink_source(self):
        (self.pack / 'skills' / self.name / 'linked.md').symlink_to(self.pack / 'README.md')
        self.assertTrue(validate(self.pack)['errors'])
        with self.assertRaises(ValueError):
            install(self.pack, self.dest, [self.name], True)

    def test_preview_no_writes(self):
        result = install(self.pack, self.dest, [self.name])
        self.assertEqual(result['mode'], 'preview')
        self.assertFalse(self.dest.exists())

    def test_full_fake_home_install_and_readback(self):
        names = sorted(p.parent.name for p in (self.pack / 'skills').glob('*/SKILL.md'))
        result = install(self.pack, self.dest, names, True)
        self.assertEqual(len(result['skills']), 8)
        for name in names:
            source = self.pack / 'skills' / name
            target = self.dest / name
            self.assertEqual(frontmatter(target / 'SKILL.md')['name'], name)
            source_files = {p.relative_to(source):p.read_bytes() for p in source.rglob('*') if p.is_file()}
            target_files = {p.relative_to(target):p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertEqual(source_files, target_files)
        self.assertTrue((self.dest / 'pache-bounded-feature-loop' / 'templates' / 'task-packet.json').is_file())
        self.assertFalse((self.fake_home / '.hermes').exists())
        self.assertFalse((self.fake_home / '.claude').exists())

    def test_collision_preflight_non_destructive(self):
        install(self.pack, self.dest, [self.name], True)
        marker = self.dest / self.name / 'owned.txt'
        marker.write_text('keep')
        with self.assertRaises(FileExistsError):
            install(self.pack, self.dest, ['pache-completion-verification', self.name], True)
        self.assertEqual(marker.read_text(), 'keep')
        self.assertFalse((self.dest / 'pache-completion-verification').exists())

    def test_traversal_duplicate_unknown_refused(self):
        for names in [['../escape'], [self.name, self.name], ['pache-unknown']]:
            with self.subTest(names=names), self.assertRaises(ValueError):
                install(self.pack, self.dest, names, True)
        self.assertFalse(self.dest.exists())

    def test_symlink_destination_refused(self):
        self.dest.symlink_to(self.fake_home, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(self.pack, self.dest, [self.name], True)
        self.assertFalse((self.fake_home / self.name).exists())

    def test_cli_fake_home_opt_in(self):
        env = {**os.environ, 'HOME': str(self.fake_home), 'PYTHONDONTWRITEBYTECODE': '1'}
        script = self.pack / 'scripts' / 'install.py'
        cmd = [sys.executable, str(script), '--dest', str(self.dest), '--skill', self.name]
        preview = subprocess.run(cmd, env=env, capture_output=True, text=True)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse(self.dest.exists())
        applied = subprocess.run(cmd + ['--apply'], env=env, capture_output=True, text=True)
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual((self.dest / self.name / 'SKILL.md').read_bytes(), self.skill.read_bytes())
        collision = subprocess.run(cmd + ['--apply'], env=env, capture_output=True, text=True)
        self.assertNotEqual(collision.returncode, 0)

if __name__ == '__main__':
    unittest.main()
