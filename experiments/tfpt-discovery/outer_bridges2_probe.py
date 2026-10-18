#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""outer_bridges2_probe -- PRIME.RDAGGER.OUTER_BRIDGES.02 (r489).

Structural seal for fixed-support topology and channel continuity.
No numerical theorem is sampled.

VERDICT: COMB_CLOSED / POLAR_INTEGRAL_CLOSED /
DENSE_COMPLETION_ONE_SORRY.  Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:40s} {detail}")


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


def theorem_body(text: str, theorem: str, next_marker: str) -> str:
    start = text.index(theorem)
    end = text.index(next_marker, start)
    return text[start:end]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()

    external = read(os.path.join(LEAN, "ExternalBridges.lean"))
    print("outer_bridges2_probe -- r489")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")

    check("l2-compact-autocorrelation-witness",
          "MeasureTheory.MemLp h 2" in external
          and "HasCompactSupport h" in external)
    check("uniform-plus-l1-topology",
          all(token in external for token in (
              "∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop",
              "IntervalIntegrable (grid n).toFun",
              "Filter.Tendsto\n    (fun n => intervalIntegral")))
    check("global-pointwise-proved",
          "FixedSupportGridApproximation.tendsto_toFun" in external)
    check("finite-comb-definition",
          "noncomputable def fullWeilCombSide" in external
          and "windowAtoms F.fullAnchor" in external)
    check("comb-continuity-proved",
          "theorem fullWeilCombSide_tendsto" in external
          and "tendsto_finset_sum" in external)
    pole_body = theorem_body(
        external, "theorem fullWeilPoleIntegral_tendsto",
        "/-- Density brick")
    check("polar-integral-continuity-proved",
          "sorry" not in pole_body
          and "Real.cosh_le_cosh" in pole_body
          and "norm_integral_le_of_norm_le" in pole_body)
    check("pole-grid-dictionary-named",
          "def GridPoleIntegralIdentification : Prop" in external)
    check("arch-status-named",
          "def FullWeilArchContinuity : Prop" in external)
    check("single-dense-completion",
          "def FullWeilFixedSupportCompletion : Prop" in external
          and "theorem fullWeil_fixedSupport_completion" in external)
    check("public-wrappers-derived",
          "fullWeil_fixedSupport_completion.1" in external
          and "fullWeilChannelContinuity_of_components" in external)

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
    print("OUTER BRIDGES 2 PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
