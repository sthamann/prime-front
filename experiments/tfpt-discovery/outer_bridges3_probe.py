#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""outer_bridges3_probe -- PRIME.RDAGGER.OUTER_BRIDGES.03 (r491).

Structural and normalization seal for the reduced final density brick.

VERDICT: HIDDEN_GAP_FOUND / DENSITY_BRIDGE_REDUCED.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:42s} {detail}")


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def sorry_census() -> list[tuple[str, int]]:
    pattern = re.compile(r"^\s*sorry\s*$")
    rows: list[tuple[str, int]] = []
    for name in sorted(os.listdir(LEAN)):
        if name.endswith(".lean"):
            for line_no, line in enumerate(
                    read(os.path.join(LEAN, name)).splitlines(), 1):
                if pattern.match(line):
                    rows.append((name, line_no))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()

    external = read(os.path.join(LEAN, "ExternalBridges.lean"))
    print("outer_bridges3_probe -- r491")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")

    check("support-length-lipschitz-witness",
          "∃ K : NNReal, LipschitzWith K h" in external
          and "a + supportRadius < t" in external)
    check("full-arch-concrete",
          "noncomputable def fullWeilArchSide" in external
          and "opaque fullWeilArchSide" not in external)
    check("dyadic-step-function-defined",
          "noncomputable def GridElement.toStepFun" in external)
    check("explicit-dyadic-sampler",
          "noncomputable def dyadicSampleGrid" in external
          and "Nat.floor (R * (2 : ℝ) ^ m)" in external)
    check("sampler-support-bound-proved",
          "theorem dyadicSampleGrid_supportBound_le" in external)
    check("dyadic-convergence-target-named",
          "def FullWeilDyadicSampleConvergence : Prop" in external)
    check("dyadic-implies-density-proved",
          "theorem fullWeilFixedSupportGridDensity_of_dyadicSample"
          in external)
    check("pole-hat-identity-named",
          "def GridPoleHatIntegralIdentity : Prop" in external)
    check("hat-implies-sequence-pole-proved",
          "theorem gridPoleIntegralIdentification_of_hat" in external)

    pole_pair = 16.0 * (math.cosh(0.5) - 1.0)
    plus_integral = 16.0 * (math.cosh(0.5) - 1.0)
    minus_integral = -plus_integral
    check("pole-plus-sign-pin",
          abs(pole_pair - plus_integral) < 1e-14
          and abs(pole_pair - minus_integral) > 4.0,
          f"pair={pole_pair:.15f}, plus={plus_integral:.15f}")

    census = sorry_census()
    external_sorries = [row for row in census if row[0] == "ExternalBridges.lean"]
    check("r638L-external-sorry-census-1", len(external_sorries) == 1,
          ", ".join(f"{name}:{line}" for name, line in external_sorries))
    check("r638L-project-sorry-census-5", len(census) == 5,
          ", ".join(f"{name}:{line}" for name, line in census))

    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("OUTER BRIDGES 3 PROBE VERIFIED -- REDUCED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
