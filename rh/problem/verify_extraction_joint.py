#!/usr/bin/env python3
"""Verify r473 extraction-joint redesign.  NO RH CLAIM."""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "extraction_joint_probe.py"
)
NOTE = os.path.join(os.path.dirname(__file__), "extraction_joint.tex")
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
    frequent = read("FrequentlySelected.lean")
    note = open(NOTE, encoding="utf-8").read()

    check("poly-bridge-proved",
          "theorem selectedACapPsdImpliesPolynomialReads" in inner
          and "theorem fullRead_weilForm_gap_eq_arch" in inner
          and "\n  sorry" not in inner)
    check("named-approx-and-joint",
          "def SelectedPolynomialApproximatesGrid" in inner
          and "def FrequentlySelectedPolynomialJoint" in frequent
          and "theorem weilForm_ge_neg_two_archError_of_joint" in frequent)
    check("historical-endpoint-retained",
          "theorem internal_weil_nonneg_of_frequently_selected" in frequent
          and "def SelectedReadQuadraticRepresentation" in inner)
    check("note-states-artefact",
          "ARTEFACT" in note
          and "0.0769078530458283" in note
          and "SelectedPolynomialApproximatesGrid" in note)

    census = sorry_census()
    print("SORRY CENSUS:", ", ".join(f"{name}:{line}" for name, line in census))
    check("r638L-sorry-census-5", len(census) == 5)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("numeric-and-text-probe",
          run.returncode == 0
          and "EXTRACTION JOINT PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("EXTRACTION JOINT VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
