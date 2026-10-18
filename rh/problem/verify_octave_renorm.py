#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_octave_renorm.py -- machine check of every numbered
lemma in rh/problem/octave_renorm.tex (round 468,
OCTAVE_NOT_CAUCHY / EDGE_TWO_POINTS / REDUCTION_ALIAS).

PART A (STANDALONE):
  G1  verdicts
  G2  r-sequence (9->10 intra; edges 9 and 16)
  G3  isolated-octave pin 10->11
  G4  psi bound grows

PART B (CONSTRUCTION PINS):
  G10 k=5 q and ka_active=17
  G11 8->9 block dq
  G12 k=8 Delta = 2 * k=9 Delta

Exit: "OCTAVE RENORM VERIFIED" iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import math
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import octave_renorm_probe as S  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def part_a():
    section("PART A  VERDICTS / SEQUENCE")
    check("G1-verdicts",
          S.VERDICT_A == "OCTAVE_NOT_CAUCHY"
          and S.VERDICT_B == "EDGE_TWO_POINTS"
          and S.VERDICT_C == "REDUCTION_ALIAS",
          "%s / %s / %s" % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    check("G2-r-seq",
          S.r_of(8) == 2 and S.r_of(9) == 3 and S.r_of(10) == 3
          and S.r_of(16) == 4,
          "9->10 intra; edges at 9 and 16")
    check("G3-isol",
          S.DQ_OCT_1011 > 0.2 and abs(S.DQ_PIN[(10, 11)]) < 0.02,
          "isol 10->11 = %.5f" % S.DQ_OCT_1011)
    check("G4-bound-grows",
          S.W_OCT_14 > 20 * S.W_OCT_5,
          "W 4.31 -> 105.7")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    rows, _ = S.rows_lp(1024)
    r5 = S.q_window(5, rows)
    check("G10-k5",
          r5["live"] and r5["ka"] == 17
          and abs(r5["qM"] - S.Q_FLOAT[5]) < 1e-12,
          "q=%.12f ka=%d" % (r5["qM"], r5["ka"]))
    r8 = S.q_window(8, rows)
    r9 = S.q_window(9, rows)
    dq = r9["qM"] - r8["qM"]
    check("G11-edge-89",
          abs(dq - S.DQ_PIN[(8, 9)]) < 1e-12 and dq > 0,
          "dq=%+.12f" % dq)
    d8 = S.S458.lean_shape(8)["D"]
    d9 = S.S458.lean_shape(9)["D"]
    check("G12-delta-half",
          abs(d8 - 2 * d9) < 1e-15,
          "D8=%.16f D9=%.16f" % (d8, d9))


def main():
    print("=" * 72)
    print("verify_octave_renorm.py -- round 468")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("OCTAVE RENORM VERIFIED")
        return 0
    print("OCTAVE RENORM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
