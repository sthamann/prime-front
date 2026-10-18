#!/usr/bin/env python3
"""Verify r463 Lean fidelity repair artefacts.  NO RH CLAIM."""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
PROBE = os.path.join(REPO, "experiments", "tfpt-discovery",
                     "lean_fidelity_probe.py")
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
    faithful = read("FaithfulFold.lean")
    elementwise = read("Elementwise.lean")
    frequent = read("FrequentlySelected.lean")
    external = read("ExternalBridges.lean")
    root = open(os.path.join(REPO, "rh", "lean", "RH.lean"),
                encoding="utf-8").read()

    check("faithful-production-dimensions",
          "def productionL" in faithful and "2 * productionM m - 2" in faithful)
    check("lag-density-fold-signsplit",
          all(token in faithful for token in (
              "def exactPrimeLag", "def exactSpectralDensity",
              "def exactSignedFoldWeight", "def exactPositiveFoldWeight",
              "def exactNegativeFoldWeight")))
    check("arch-read-concrete",
          "noncomputable def archRead" in elementwise
          and "opaque archRead" not in elementwise)
    check("compound-mincut-visible",
          "def FrequentlySelectedInternalMincut" in frequent
          and "SelectedACapPsdImpliesPlainReads" in frequent)
    check("endpoint-internal",
          "theorem internal_weil_nonneg_of_frequently_selected" in frequent
          and re.search(r"^theorem rh_of_frequently_selected\b",
                        frequent, re.MULTILINE) is None)
    check("external-bridges-imported",
          "import RH.ExternalBridges" in root
          and external.count("\n  sorry") == 1
          and "def StandardExplicitFormulaIdentification" in external
          and "theorem standard_explicit_formula_identification :" not in external)
    check("mathlib-zeta-interface",
          "Mathlib.NumberTheory.LSeries.RiemannZeta" in external
          and "RiemannHypothesis" in external)

    census = sorry_census()
    print("SORRY CENSUS:", ", ".join(f"{name}:{line}" for name, line in census))
    check("r638L-sorry-census-5", len(census) == 5)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("numeric-k5-k9-k10",
          run.returncode == 0 and "LEAN FIDELITY VERIFIED" in run.stdout
          and all(f"k{k}-lean-vs-python" in run.stdout for k in (5, 9, 10)))

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("LEAN FIDELITY REPAIR VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
