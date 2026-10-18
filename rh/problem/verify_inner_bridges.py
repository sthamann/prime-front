#!/usr/bin/env python3
"""Verify r464 internal Lean bridge reduction.  NO RH CLAIM."""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "inner_bridges_probe.py"
)
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
    elementwise = read("Elementwise.lean")
    inner = read("InnerBridges.lean")
    frequent = read("FrequentlySelected.lean")
    root = open(
        os.path.join(REPO, "rh", "lean", "RH.lean"), encoding="utf-8"
    ).read()

    check("inner-bridge-module-imported", "import RH.InnerBridges" in root)
    check("finite-psd-half-sorry-free",
          "theorem selectedACapPsdImpliesPlainReads_of_representation" in inner
          and "dotProduct_mulVec_nonneg" in inner
          and "\n  sorry" not in inner)
    check("exact-channel-remainder",
          "def SelectedReadQuadraticRepresentation" in inner
          and "SelectedReadQuadraticRepresentation" in frequent)
    check("original-target-not-weakened",
          "def SelectedACapPsdImpliesPlainReads" in inner
          and "f.meshExp ≤ selectedMesh k" in inner)
    check("productive-arch-lags",
          "noncomputable def productionArchLag" in elementwise
          and "opaque productionArchLag" not in elementwise
          and "def productionArchLagNear" in elementwise
          and "def productionArchLagFar" in elementwise)
    check("arch-contract-unasserted-r638L",
          "def ArchGaussMellinDigammaIdentity" in elementwise
          and "theorem arch_gauss_mellin_digamma_identity" not in elementwise
          and "(hArch : ArchGaussMellinDigammaIdentity)" in elementwise)

    census = sorry_census()
    print("SORRY CENSUS:", ", ".join(f"{name}:{line}" for name, line in census))
    check("r638L-sorry-census-5", len(census) == 5)
    check("elementwise-sorry-free",
          not any(name == "Elementwise.lean" for name, _ in census)
          and elementwise.count("\n  sorry") == 0)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("numeric-and-text-probe",
          run.returncode == 0
          and "INNER BRIDGES PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("INNER BRIDGES VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
