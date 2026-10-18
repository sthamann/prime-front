#!/usr/bin/env python3
"""Verify r475 arch identity isolation and tent rate.  NO RH CLAIM."""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "arch_rate_probe.py"
)
NOTE = os.path.join(os.path.dirname(__file__), "arch_rate.tex")
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
    note = open(NOTE, encoding="utf-8").read()

    check("weil-side-concrete-and-gauss-named",
          "noncomputable def weilArchSide" in elementwise
          and "opaque weilArchSide" not in elementwise
          and "def GaussDigammaIntegralRepresentation" in elementwise)
    check("rate-proved-from-named",
          "theorem productionArchDelta_tendsto_atTop" in inner
          and "def SelectedArchErrorQuadraticRate" in inner
          and "theorem selectedArchError_tendsto_zero_of_rate" in inner
          and "\n  sorry" not in inner)
    check("exact-identity-unasserted-r638L",
          "def ArchGaussMellinDigammaIdentity" in elementwise
          and "theorem arch_gauss_mellin_digamma_identity" not in elementwise
          and "(hArch : ArchGaussMellinDigammaIdentity)" in elementwise)
    check("note-states-rate",
          "IDENTITY_ISOLATED" in note
          and "3.9893" in note
          and "SelectedArchErrorQuadraticRate" in note)

    census = sorry_census()
    print("SORRY CENSUS:", ", ".join(f"{name}:{line}" for name, line in census))
    check("r638L-sorry-census-5", len(census) == 5)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("numeric-and-text-probe",
          run.returncode == 0
          and "ARCH RATE PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("ARCH RATE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
