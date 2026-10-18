#!/usr/bin/env python3
"""Verify r470 quadratic-representation obstruction.  NO RH CLAIM."""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "quadrep_probe.py"
)
NOTE = os.path.join(os.path.dirname(__file__), "quadrep.tex")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def read(name: str) -> str:
    with open(os.path.join(LEAN, name), encoding="utf-8") as handle:
        return handle.read()


def sorry_census() -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    pattern = re.compile(r"^\s*sorry\s*$")
    for name in sorted(os.listdir(LEAN)):
        if not name.endswith(".lean"):
            continue
        for number, line in enumerate(read(name).splitlines(), 1):
            if pattern.match(line):
                rows.append((name, number))
    return rows


def main() -> int:
    inner = read("InnerBridges.lean")
    note = open(NOTE, encoding="utf-8").read()

    check("original-channel-unweakened",
          "def SelectedReadQuadraticRepresentation" in inner
          and "f.meshExp ≤ selectedMesh k" in inner)
    check("quantifier-witness-proved",
          "theorem exists_mesh_compatible_steps_gt_cap" in inner
          and "selectedMesh_five" in inner
          and "\n  sorry" not in inner)
    check("signed-obstruction-named",
          "def SelectedOnsetCompatibleNegativeRead" in inner
          and "theorem quadraticRepresentation_refuted_of_negative_read"
          in inner)
    check("note-states-obstruction",
          "SelectedOnsetCompatibleNegativeRead" in note
          and "OBSTRUCTION_SEALED" in note
          and "0.042885425277" in note)

    census = sorry_census()
    print("SORRY CENSUS:", ", ".join(f"{name}:{line}" for name, line in census))
    check("r638L-sorry-census-5", len(census) == 5)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("numeric-and-text-probe",
          run.returncode == 0
          and "QUADREP PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("QUADREP VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
