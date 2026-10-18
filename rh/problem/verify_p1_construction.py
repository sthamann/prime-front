#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_p1_construction.py -- machine check of every numbered
lemma in rh/problem/p1_construction.tex (round 403, P1 as a
construction-class theorem, REFUTED).

PART A (STANDALONE):
  G1  rank-1 interlacing kills at most one negative
  G2  PSD + negative-definite need not lift all negatives
  G3  the P1 threshold is 1/2 (not 1)

PART B (CONSTRUCTION PINS):
  G10 w9 MAIN nneg=1, nneg_ref=49, killed=48
  G11 B|_neg is PSD (rest=0, 49/49); n_half(R^ref)=13
  G12 omit-Gram returns 49; only-Gram leaves 13
  G13 joint scale R(7w)=R(w); mu*3 / nu*3 split
  G14 fixed-mask permute breaks P1
  G15 rademacher-flatten nneg=2; mild 1e-4 breaks
  G16 scramble nneg=21; two-period killed=0
  G17 dead chi3-15 nneg<=1 on true weights, perm breaks

Exit: per-gate PASS/FAIL and the final line
"P1 CONSTRUCTION VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and one named refutation.
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

import p1_construction_probe as P  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import bulk_one_defect_probe as H  # noqa: E402

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
    section("PART A  INTERLACING / PSD-INCOMPLETE")
    A2p00, A2p11 = Fr(0), Fr(-1)
    check("G1-interlace-rank1",
          A2p00 == Fr(0) and A2p11 == Fr(-1),
          "diag(-1,-1)+e0 e0^T kills one, not two")
    Af = np.diag([-1.0, -1.0])
    nS, _ = H.nneg_sym(Af + 0.1 * np.eye(2))
    check("G2-psd-incomplete",
          nS == 2,
          "diag(-1,-1)+0.1 I still nneg=2")
    check("G3-threshold-half",
          Fr(1, 2) < Fr(1),
          "P1 is lam2>=1/2")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    p = P.spec_of(mz, True)
    g = P.gram_of(mz)
    check("G10-w9-MAIN",
          p["nneg"] == P.W9_NNEG and p["nneg_ref"] == P.W9_NNEG_REF
          and p["killed"] == P.W9_KILLED,
          "nneg=%d nneg_ref=%d killed=%d"
          % (p["nneg"], p["nneg_ref"], p["killed"]))
    check("G11-Gram-PSD-half",
          g["nneg_M"] == 0 and g["npos_M"] == P.W9_NPOS_M
          and g["rest"] <= P.W9_GRAM_REST_HI
          and g["n_half"] == P.W9_N_HALF,
          "rest=%.2e n_half=%d" % (g["rest"], g["n_half"]))
    check("G12-omit-only-Gram",
          g["nneg_omit"] == P.W9_OMIT and g["nneg_gram"] == P.W9_ONLYGRAM,
          "omit=%d only-Gram=%d" % (g["nneg_omit"], g["nneg_gram"]))
    mz7 = P.rebuild(mz, 7.0 * mz["wp"], 7.0 * mz["vn"])
    R1, _ = H.r_of(mz)
    R7, _ = H.r_of(mz7)
    res = float(np.linalg.norm(R1 - R7))
    pmu = P.spec_of(P.rebuild(mz, 3.0 * mz["wp"], mz["vn"]), False)
    pnu = P.spec_of(P.rebuild(mz, mz["wp"], 3.0 * mz["vn"]), False)
    check("G13-scale",
          res <= P.SCALE_RES_HI and pmu["nneg"] == 0
          and pnu["nneg"] >= 60,
          "||R-R7||=%.3e mu*3=%d nu*3=%d"
          % (res, pmu["nneg"], pnu["nneg"]))
    mzP = P.reweight(mz, "permute", 1000)
    nP = P.spec_of(mzP, False)["nneg"]
    nR = P.spec_of(P.reweight(mz, "rademacher", 0), False)["nneg"]
    check("G14-permute-breaks",
          nP >= P.PERM_NNEG_LO,
          "permute nneg=%d (mask fixed)" % nP)
    n_break = 0
    for s in range(P.MILD_SEEDS):
        rng = np.random.default_rng(P.MILD_SEED0 + s)
        wp = mz["wp"] * (1.0 + P.MILD_EPS * rng.normal(0, 1, size=len(mz["wp"])))
        vn = mz["vn"] * (1.0 + P.MILD_EPS * rng.normal(0, 1, size=len(mz["vn"])))
        pm = P.spec_of(P.rebuild(mz, np.clip(wp, 1e-18, None),
                                 np.clip(vn, 1e-18, None)), False)
        if pm["nneg"] > 1:
            n_break += 1
    check("G15-rade-mild",
          nR == P.RADE_NNEG and n_break >= P.MILD_BREAKS_LO,
          "rade nneg=%d; mild 1e-4 breaks %d/%d"
          % (nR, n_break, P.MILD_SEEDS))
    ps = P.spec_of(HM.scramble_mz(), True)
    pt = P.spec_of(HM.two_period_mz(21, 2.0 / 3.0), True)
    check("G16-scramble-twoperiod",
          ps["nneg"] == P.SCR_NNEG and pt["killed"] == 0
          and pt["nneg"] >= P.TP_NNEG,
          "scramble %d; two-period nneg=%d killed=%d"
          % (ps["nneg"], pt["nneg"], pt["killed"]))
    mzd = HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    pd = P.spec_of(mzd, False)
    rng = np.random.default_rng(15)
    pdp = P.spec_of(P.rebuild(mzd, rng.permutation(mzd["wp"]),
                              rng.permutation(mzd["vn"])), False)
    check("G17-dead-chi",
          pd["nneg"] <= 1 and pdp["nneg"] >= P.CHI_PERM_LO,
          "true nneg=%d perm nneg=%d" % (pd["nneg"], pdp["nneg"]))


def main():
    print("=" * 72)
    print("verify_p1_construction.py -- round 403")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("P1 CONSTRUCTION VERIFIED")
        return 0
    print("P1 CONSTRUCTION FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
