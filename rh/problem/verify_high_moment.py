#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_high_moment.py -- machine check of every numbered
lemma in rh/problem/high_moment_inertia.tex (round 398,
high-moment kill-test of P1, KILL_FAIL).

PART A (STANDALONE):
  G1  Fractions pointwise bound [2(1-2/5)]^4 = 1296/625 >= 1
  G2  nopref mutant (1-r)^4 = 81/625 < 1
  G3  odd-power mutant on R=diag(2/5, 2) fails as a majorant
  G4  cycle-sum: Fractions tr(A^2) = 35/72
  G5  registered d-set is {2,3,4,6,8}

PART B (CONSTRUCTION PINS):
  G10 w9 contraction + FTI residual 0 + nneg=1
  G11 w9 moments all >= 2, near-1/2 cluster
  G12 scramble nneg=21 and M_d explodes
  G13 two-period nneg>=4, M2>=40
  G14 dead chi3-15 M_d >= 2
  G15 living chi3-9 nneg=0 yet M2>=20 (not a P1 test)

Exit: per-gate PASS/FAIL and the final line
"HIGH MOMENT VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named kill-test.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import high_moment_inertia_probe as H  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

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
    section("PART A  INEQUALITY / MUTANTS / CYCLE-SUM")
    r = Fr(2, 5)
    rhs = (2 * (1 - r)) ** 4
    npr = (1 - r) ** 4
    check("G1-Fractions-bound",
          rhs == Fr(1296, 625) and rhs >= 1,
          "[2(1-2/5)]^4 = %s" % rhs)
    check("G2-nopref-mutant",
          npr == Fr(81, 625) and npr < 1,
          "(1-r)^4 = %s < 1" % npr)
    odd_sum = sum((2 * (1 - ri)) ** 5
                  for ri in (Fr(2, 5), Fr(2)))
    even_sum = sum((2 * (1 - ri)) ** 4
                   for ri in (Fr(2, 5), Fr(2)))
    check("G3-odd-mutant",
          odd_sum < 1 and even_sum >= 1,
          "odd p=5 sum=%s; even p=4 sum=%s" % (odd_sum, even_sum))
    A2 = ((Fr(1, 2), Fr(1, 4)), (Fr(1, 4), Fr(1, 3)))
    tr2 = (A2[0][0] * A2[0][0] + A2[1][1] * A2[1][1]
           + 2 * A2[0][1] * A2[1][0])
    check("G4-cycle-sum-Q",
          tr2 == Fr(35, 72),
          "tr(A^2)=%s = 35/72" % tr2)
    check("G5-d-set-frozen",
          H.DS == (2, 3, 4, 6, 8),
          "DS=%s (no N-growing d)" % (H.DS,))
    A = np.array([[0.3, 0.1, 0.05],
                  [0.1, 0.4, 0.02],
                  [0.05, 0.02, 0.2]])
    A = 0.5 * (A + A.T)
    check("G4b-cycle-sum-k4",
          abs(H.tr_power(A, 4) - H.cycle_walk_sum(A, 4)) <= 1e-14,
          "tr vs walks dev=%.1e"
          % abs(H.tr_power(A, 4) - H.cycle_walk_sum(A, 4)))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    p = H.row_mz(mz, "MAIN-9")
    i1, i2 = PX.pair_select(mz["yn"])
    o = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                      mz["Nw"], mz["S"], mz["L"], i1, i2, keep=True)
    R2 = o["A0"] + 0.5 * np.eye(o["A0"].shape[0])
    dev = float(np.max(np.abs(p["R"] - R2)))
    check("G10-w9-contract-fti",
          p["contract"] and p["nneg"] == 1 and o["nneg"] == 1
          and dev == 0.0 and p["n"] == 104,
          "n=%d nneg=%d residual=%.1e" % (p["n"], p["nneg"], dev))
    check("G11-w9-moments-fail",
          all(not p["moms"][d]["pass_"] for d in H.DS)
          and abs(p["moms"][2]["M"] / H.W9_M[2] - 1.0) <= H.REL
          and p["near"] == dict(H.W9_NEAR),
          "M2=%.4g near %s" % (p["moms"][2]["M"], p["near"]))

    mz_s = H.scramble_mz()
    ps = H.row_mz(mz_s, "SCR")
    check("G12-scramble",
          ps["nneg"] == 21 and ps["moms"][2]["M"] >= H.SCR_M2_FLOOR
          and ps["moms"][8]["M"] >= H.SCR_M8_FLOOR,
          "nneg=%d M2=%.4g M8=%.4g" % (
              ps["nneg"], ps["moms"][2]["M"], ps["moms"][8]["M"]))
    tp = H.row_mz(H.two_period_mz(21, 2.0 / 3.0), "2PER")
    check("G13-two-period",
          tp["nneg"] >= 4 and tp["moms"][2]["M"] >= H.TP21_M2_FLOOR
          and all(not tp["moms"][d]["pass_"] for d in H.DS),
          "nneg=%d M2=%.4g" % (tp["nneg"], tp["moms"][2]["M"]))
    mz_d = H.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    pd = H.row_mz(mz_d, "DEAD15")
    check("G14-dead-chi",
          all(not pd["moms"][d]["pass_"] for d in H.DS),
          "dead chi3-15 M2=%.4g" % pd["moms"][2]["M"])
    p3 = H.row_mz(H.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3), "CHI3-9")
    check("G15-live-chi-not-P1",
          p3["nneg"] == 0 and p3["moms"][2]["M"] >= 20.0
          and all(not p3["moms"][d]["pass_"] for d in H.DS),
          "chi3-9 nneg=0 M2=%.4g (cluster kills the bound)"
          % p3["moms"][2]["M"])


def main():
    print("=" * 72)
    print("verify_high_moment.py -- round 398")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("HIGH MOMENT VERIFIED")
        return 0
    print("HIGH MOMENT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
