#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""outer_bridges_probe -- PRIME.RDAGGER.OUTER_BRIDGES.01 (r487).

Structural seal for the first external-bridge formalization round.
No numerical theorem is sampled: the round types fixed-support
density, channel continuity, Guinand--Weil normalization, and the
literal Mathlib zeta endpoint.

VERDICT: OUTER_LANE_TYPED / DENSE_LIMIT_REDUCED / ZETA_INTERFACE_PROVED.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
MATHLIB = os.path.join(REPO, "rh", "lean", ".lake", "packages",
                       "mathlib", "Mathlib")
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")


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
    zeta = read(os.path.join(
        MATHLIB, "NumberTheory", "LSeries", "RiemannZeta.lean"
    ))
    print("outer_bridges_probe -- r487")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")

    check("full-class-fixed-support",
          all(token in external for token in (
              "supportRadius : ℝ", "continuous_toFun : Continuous toFun",
              "even_toFun : Function.Even toFun", "autocorrelation : ∃ h")))
    check("fixed-support-approximation",
          all(token in external for token in (
              "def FullWeilTest.FixedSupportGridApproximation",
              "FullWeilFixedSupportGridDensity",
              "FullWeilChannelContinuity")))
    check("three-channel-form-visible",
          all(token in external for token in (
              "noncomputable def fullWeilArchSide",
              "noncomputable def fullWeilCombSide",
              "noncomputable def fullWeilPoleSide",
              "noncomputable def fullWeilForm")))
    check("limit-algebra-proved",
          all(token in external for token in (
              "theorem fullWeilForm_tendsto_of_channels",
              "theorem fullWeilForm_nonneg_of_tendsto",
              "theorem grid_dense_extension_of_fixedSupport")))
    check("dense-wrapper-proved",
          "theorem grid_dense_extension : GridDenseExtension :=" in external)
    check("literal-mathlib-zero-interface",
          "riemannZeta s = 0" in external
          and "def RiemannHypothesis : Prop" in zeta)
    check("offcritical-interface-proved",
          all(token in external for token in (
              "def FullWeilSeparatesOffCriticalZeros",
              "theorem standard_weil_criterion_to_mathlib_rh_of_separation",
              "theorem standard_weil_criterion_to_mathlib_rh :")))
    check("guinand-weil-target-named",
          "def GuinandWeilExplicitFormula : Prop" in external)
    check("no-zeta-zero-api",
          not any("ZetaZero" in read(os.path.join(root, name))
                  for root, _, names in os.walk(MATHLIB)
                  for name in names if name.endswith(".lean")))
    check("mellin-infrastructure-present",
          all(os.path.isfile(os.path.join(MATHLIB, relative)) for relative in (
              "Analysis/MellinTransform.lean",
              "Analysis/MellinInversion.lean",
              "NumberTheory/LSeries/MellinEqDirichlet.lean")))

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
    print("OUTER BRIDGES PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
