#!/usr/bin/env python3
"""Verify r489 fixed-support channel reduction.  NO RH CLAIM."""
from __future__ import annotations

import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROBE = os.path.join(
    REPO, "experiments", "tfpt-discovery", "outer_bridges2_probe.py"
)
EXTERNAL = os.path.join(REPO, "rh", "lean", "RH", "ExternalBridges.lean")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def main() -> int:
    with open(EXTERNAL, encoding="utf-8") as handle:
        external = handle.read()

    check("uniform-fixed-support-topology",
          "∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop" in external)
    check("compact-l2-witness",
          "MeasureTheory.MemLp h 2" in external
          and "HasCompactSupport h" in external)
    check("comb-closed",
          "theorem fullWeilCombSide_tendsto" in external
          and "tendsto_finset_sum" in external)
    check("polar-integral-closed",
          "theorem fullWeilPoleIntegral_tendsto" in external
          and "norm_integral_le_of_norm_le" in external)
    check("r638L-one-external-brick",
          external.count("\n  sorry") == 1
          and "theorem fullWeil_fixedSupport_completion" in external
          and "theorem standard_explicit_formula_identification :" not in external)

    run = subprocess.run(
        [sys.executable, PROBE, "--smoke"],
        cwd=REPO, text=True, capture_output=True, timeout=60, check=False,
    )
    check("outer-bridges2-probe",
          run.returncode == 0
          and "OUTER BRIDGES 2 PROBE VERIFIED" in run.stdout)

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} checks PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        if run.stdout:
            print(run.stdout)
        if run.stderr:
            print(run.stderr)
        return 1
    print("OUTER BRIDGES 2 VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
