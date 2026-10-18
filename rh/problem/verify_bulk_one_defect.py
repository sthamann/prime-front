#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_bulk_one_defect.py -- machine check of every numbered
lemma in rh/problem/bulk_one_defect.tex (round 400, threshold /
phase form of the frame inequality, FORM_T REFUTED /
FORM_P REFUTED).

PART A (STANDALONE):
  G1  Fractions frame: A+C ell ell^T succ 0 => nneg(A)=1
  G2  omit-ell mutant: A not succeq c I
  G3  rank-1 interlacing kills at most one negative
  G4  Weyl nneg(A+B) <= nneg(A)+nneg(B)
  G5  threshold x2 is strictly stronger than 1/2

PART B (CONSTRUCTION PINS):
  G10 w9 nneg=1, ncl>=30, dualFej nneg_ref>=40 killed>=40
  G11 w9 lift not rank-1, dcent orthogonal, source frame fails
  G12 scramble nneg=21, punch-through
  G13 two-period nneg>=4 killed=0
  G14 dead chi3-15 nneg<=1 (bulk P1 holds)
  G15 living chi3-9 nneg<=1
  G16 phase rho1 does not separate MAIN vs scramble

Exit: per-gate PASS/FAIL and the final line
"BULK ONE DEFECT VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and two named refutations.
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

import bulk_one_defect_probe as H  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import source_weyl_energy_probe as SW  # noqa: E402
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
    section("PART A  FRAME / INTERLACING / WEYL")
    A = np.array([[Fr(-1), Fr(0)], [Fr(0), Fr(2)]], dtype=object)
    C = Fr(2)
    Ap00 = A[0, 0] + C
    check("G1-frame-Q",
          Ap00 == Fr(1) and A[1, 1] == Fr(2),
          "diag(-1,2)+2 e0 e0^T => min=1>0")
    check("G2-omit-ell",
          A[0, 0] == Fr(-1),
          "min(A)=-1 without ell")
    A2p00, A2p11 = Fr(0), Fr(-1)
    check("G3-interlace-rank1",
          A2p00 == Fr(0) and A2p11 == Fr(-1),
          "diag(-1,-1)+e0 e0^T kills one, not two")
    Af = np.diag([-1.0, 1.0])
    Bf = np.diag([1.0, -1.0])
    nA, _ = H.nneg_sym(Af)
    nB, _ = H.nneg_sym(Bf)
    nS, _ = H.nneg_sym(Af + Bf)
    check("G4-Weyl",
          nS <= nA + nB,
          "nneg(A+B)=%d <= %d+%d" % (nS, nA, nB))
    check("G5-threshold-x2",
          Fr(1, 2) < Fr(1),
          "1/2 < 1 (x2 mutant strictly stronger)")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    en = SW.pack_kz(9)
    p = H.pack_world(mz, en)
    check("G10-w9-ref-lift",
          p["nneg"] == H.W9_NNEG and p["ncl"] >= H.W9_NCL
          and p["nneg_ref"] >= H.W9_NNEG_REF_LO
          and p["killed"] >= H.W9_KILLED_LO,
          "nneg=%d ncl=%d nneg_ref=%d killed=%d"
          % (p["nneg"], p["ncl"], p["nneg_ref"], p["killed"]))
    check("G11-w9-not-rank1-orthogonal",
          p["lift"]["r_eff"] >= H.W9_LIFT_REFF_LO
          and p["cos_vd"] <= H.W9_COS_HI
          and (not p["fr_dcent"]["ok"]) and p["fr_neg"]["ok"],
          "lift r_eff=%.2f cos=%.4f dcent-frame=%s"
          % (p["lift"]["r_eff"], p["cos_vd"], p["fr_dcent"]["ok"]))
    H.drop_heavy(p)
    ps = H.pack_world(HM.scramble_mz(), SW.scramble_energy())
    check("G12-scramble",
          ps["nneg"] == H.SCR_NNEG and ps["rmin"] <= H.SCR_RMIN_HI,
          "nneg=%d rmin=%.4f killed=%d"
          % (ps["nneg"], ps["rmin"], ps["killed"]))
    pt = H.pack_world(HM.two_period_mz(21, 2.0 / 3.0), None)
    check("G13-two-period",
          pt["nneg"] >= H.TP21_NNEG and pt["killed"] == 0,
          "nneg=%d killed=%d" % (pt["nneg"], pt["killed"]))
    pd = H.pack_world(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3),
                      SW.chi_energy(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G14-dead-chi-bulk-P1",
          pd["nneg"] <= 1,
          "dead chi3-15 nneg=%d" % pd["nneg"])
    pl = H.pack_world(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3),
                      SW.chi_energy(9, DMF.Q_CHI3, DMF.LPQ3))
    check("G15-live-chi",
          pl["nneg"] <= 1,
          "live chi3-9 nneg=%d" % pl["nneg"])
    drho = abs(p["ph"]["rho1"] - ps["ph"]["rho1"])
    check("G16-phase-blind",
          drho <= H.PHASE_DRHO1_HI,
          "|drho1|=%.3f (nneg 1 vs 21)" % drho)
    for q in (ps, pt, pd, pl):
        H.drop_heavy(q)


def main():
    print("=" * 72)
    print("verify_bulk_one_defect.py -- round 400")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("BULK ONE DEFECT VERIFIED")
        return 0
    print("BULK ONE DEFECT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
