#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_lambdastar03.py -- machine check of
rh/problem/lambdastar03.tex (round 479,
PRIME.RDAGGER.LAMBDASTAR_03_KEYSTONE.01,
REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, t_c / Higham / remainder pins.

Exit: "LAMBDASTAR03 VERIFIED -- REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import lambdastar03_probe as S  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72, flush=True)


def part_a() -> None:
    section("PART A  NOTE / TYPE")
    path = os.path.join(REPO, "rh", "problem", "lambdastar03.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED($\kappa_{\mathrm{high}}\le1.79\cdot10^{-2}$ at $t_*=8,N=5$)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        r"\mathrm{Re}\,\psi",
        "7a234db34c2ec6f0",
        "Yoshida--Bombieri",
        "interlacing",
        r"\kappa_{\mathrm{high}}",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          S.VERDICT_KIND.startswith("REDUCED")
          and S.T_C_LO_PIN.startswith("6.2898359888369"),
          "REDUCED + t_c pin")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "lambdastar03_probe --smoke")
    check("G11-tc-floor",
          float(S.T_C_LO_PIN) > 6.28
          and float(S.T_C_HI_PIN) < 6.30,
          "t_c bracket around 6.2898")
    check("G12-remainder",
          float(S.KAPPA_HIGH_NEED) < 0.02
          and float(S.HIGHAM3_PIN) > 0.002,
          "kappa_high budget < 0.02")


def main() -> int:
    print("=" * 72)
    print("verify_lambdastar03.py -- round 479")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("LAMBDASTAR03 VERIFIED -- "
              "REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)")
        return 0
    print("LAMBDASTAR03 FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
