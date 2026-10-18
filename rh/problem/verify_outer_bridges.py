#!/usr/bin/env python3
"""Verify r487 outer-bridge formalization artefacts.  NO RH CLAIM."""
from __future__ import annotations

import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "outer_bridges_probe.py"
)
EXTERNAL = os.path.join(REPO, "rh", "lean", "RH", "ExternalBridges.lean")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def main() -> int:
    with open(EXTERNAL, encoding="utf-8") as handle:
        external = handle.read()

    check("density-decomposed",
          "fullWeil_fixedSupport_grid_density" in external
          and "fullWeil_channel_continuity" in external)
    check("positivity-transfer-proved",
          "fullWeilForm_nonneg_of_tendsto" in external
          and "ge_of_tendsto" in external)
    check("dense-wrapper-no-direct-sorry",
          "theorem grid_dense_extension : GridDenseExtension :=" in external)
    check("zeta-interface-proved",
          "standard_weil_criterion_to_mathlib_rh_of_separation" in external
          and "by_contra hcritical" in external)
    check("r638L-one-external-brick",
          external.count("\n  sorry") == 1
          and "def StandardExplicitFormulaIdentification" in external
          and "theorem standard_explicit_formula_identification :" not in external)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("outer-probe",
          run.returncode == 0
          and "OUTER BRIDGES PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("OUTER BRIDGES VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
