#!/usr/bin/env python3
"""Verify r491 outer-bridge reduction and sign repair.  NO RH CLAIM."""
from __future__ import annotations

import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "outer_bridges3_probe.py"
)
EXTERNAL = os.path.join(REPO, "rh", "lean", "RH", "ExternalBridges.lean")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def main() -> int:
    with open(EXTERNAL, encoding="utf-8") as handle:
        external = handle.read()

    check("polar-sign-corrected",
          "fullWeilPoleWeight (u : ℝ) : ℝ :=\n  2 * Real.cosh" in external)
    check("full-arch-concrete",
          "noncomputable def fullWeilArchSide" in external)
    check("explicit-dyadic-construction",
          "noncomputable def dyadicSampleGrid" in external)
    check("support-bound-proved",
          "theorem dyadicSampleGrid_supportBound_le" in external)
    check("pole-hat-seam-exact",
          "def GridPoleHatIntegralIdentity : Prop" in external
          and "gridPoleIntegralIdentification_of_hat" in external)
    check("r638L-one-external-brick",
          external.count("\n  sorry") == 1
          and "theorem standard_explicit_formula_identification :" not in external)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("outer-bridges3-probe",
          run.returncode == 0
          and "OUTER BRIDGES 3 PROBE VERIFIED -- REDUCED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("OUTER BRIDGES 3 VERIFIED -- REDUCED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
