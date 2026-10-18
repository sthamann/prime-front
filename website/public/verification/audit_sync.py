#!/usr/bin/env python3
"""Audit Prime Front runner/registry/ledger and generated script surfaces.

This is a source consistency check. It executes no mathematical proof or Lean
build, and does not promote a conditional or finite result to an RH proof.
"""
from pathlib import Path
import ast
import csv
import hashlib
import json
import re
import sys
import make_script_index

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "verification"


def main():
    registry = make_script_index.load_registry()
    clusters = make_script_index.load_clusters()
    errors = make_script_index.validate(registry, clusters)
    registered = {r["script"] for r in registry}
    scope = json.loads((HERE / "split_scope.json").read_text())
    support = set(scope["dependency_only_modules"])
    present = {p.stem for p in HERE.glob("v[0-9]*_*.py")}
    for m in sorted(registered - present):
        errors.append(f"registered module missing: {m}")
    for m in sorted(present - registered - support):
        errors.append(f"unregistered/unscoped module: {m}")
    for p in HERE.glob("*.py"):
        try:
            ast.parse(p.read_text(), filename=str(p))
        except SyntaxError as exc:
            errors.append(f"{p.name}: {exc}")
    rows = list(csv.DictReader((HERE / "status_ledger.csv").open()))
    ids = [r["claim_id"] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ledger claim IDs")
    for row in rows:
        pinned = scope["claim_status_sha256"].get(row["claim_id"])
        actual = hashlib.sha256((row["status"]+"\0"+row["canonical_status"]+"\0"+row["active"]).encode()).hexdigest()
        if pinned != actual:
            errors.append(f"claim status changed from extraction scope: {row['claim_id']}")
        for script in re.findall(r"v\d+_[A-Za-z0-9_]+", row["script"]):
            if script not in registered:
                errors.append(f"ledger {row['claim_id']} references nonregistered {script}")
    for target, content in make_script_index.build().items():
        if not target.exists() or target.read_text() != content:
            errors.append(f"generated output stale: {target.relative_to(ROOT)}")
    for error in errors:
        print("[FAIL]", error)
    print(f"Prime Front source audit: {len(registered)} modules, {len(rows)} claim rows, {len(errors)} errors")
    print("AUDIT OK" if not errors else "AUDIT FAILED")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
