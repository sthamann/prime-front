#!/usr/bin/env python3
"""Verify preserved source bytes and the independent project mirrors (stdlib)."""
import ast
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
errors = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

count = 0
for manifest in sorted((ROOT / 'provenance').glob('*source-manifest.json')):
    for row in json.loads(manifest.read_text())['files']:
        rel = row.get('source', row.get('path'))
        candidates = [ROOT / row.get('archive', rel), ROOT / 'provenance/tfpt-source' / rel]
        if not any(p.is_file() and sha(p) == row['sha256'] for p in candidates):
            errors.append(f'Original bytes missing or altered: {rel} ({manifest.name})')
        count += 1
print(f'Preserved source rows: {count}; mismatches: {len(errors)}')

# The original sealed inventory is an independent check; do not refresh pins.
p = ROOT / 'rh/verification/run_rh.py'
spec = importlib.util.spec_from_file_location('rh_integrity', p)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
suite = module.Suite()
module.check_integrity(suite)
errors.extend(name + ': ' + detail for name, _, detail in suite.failures)

registry = list(csv.DictReader((ROOT / 'verification/script_registry.csv').open()))
modules = re.findall(r'\("(v\d+_[A-Za-z0-9_]+)"', (ROOT / 'verification/run_all.py').read_text())
if set(modules) != {r['script'] for r in registry}:
    errors.append('Registry / runner module mismatch')
for name in modules:
    path = ROOT / 'verification' / (name + '.py')
    if not path.is_file():
        errors.append('Missing active verification: ' + name)
    else:
        ast.parse(path.read_text(), filename=str(path))
    mirror = ROOT / 'website/public/verification' / (name + '.py')
    if not mirror.is_file() or sha(path) != sha(mirror):
        errors.append('Verification website mirror mismatch: ' + name)
for path in ROOT.glob('*.pdf'):
    mirror = ROOT / 'website/public/papers' / path.name
    if not mirror.is_file():
        errors.append('Missing PDF website mirror: ' + path.name)
    elif sha(path) != sha(mirror):
        errors.append('PDF website mirror mismatch: ' + path.name)
for error in errors:
    print('FAIL:', error)
print(f'PRIME FRONT MIGRATION: {"FAIL" if errors else "PASS"} ({len(modules)} active modules)')
sys.exit(bool(errors))
