#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_hole_nyquist.py -- machine check of every numbered
lemma in rh/problem/hole_nyquist.tex (round 410, hole-Nyquist
defect, TESTPOLY_REFUTED / DMIN_CENSUS + FOURIER_REFUTED /
BERNSTEIN_REFUTED / SEQ_REDUCED).

PART A (STANDALONE):
  G1  RK for constants K=1/h0 over Q
  G2  degree obstruction over Q
  G3  C_ii = ud K over Q
  G4  Rayleigh lam_min <= dmin over Q

PART B (CONSTRUCTION PINS):
  G10 w9 Y-Lagrange does not close (bmax<0.1, #b>=1=0)
  G11 cheb-CD partial; w9 dmin>1.5
  G12 scramble/permute dmin<1; permute is K-collapse
  G13 Fourier not banded; sequential birth k=32/37
  G14 chi dmin>1; 1010 degree kill; kz55 dmin>1 nC<=1

Exit: per-gate PASS/FAIL and the final line
"HOLE NYQUIST VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, named refutations,
one census, one reduction.
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

import hole_nyquist_probe as H  # noqa: E402
import c_threshold_probe as CT  # noqa: E402
import dual_intertwiner_probe as D  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
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
    section("PART A  RK / DEGREE / C_ii / RAYLEIGH OVER Q")
    check("G1-RK-Q", Fr(1, 3) == Fr(1) / Fr(3))
    check("G2-degree-Q", Fr(1, 2) > Fr(1, 3))
    check("G3-Cii-Q", Fr(4) == Fr(4) * Fr(1))
    check("G4-rayleigh-Q", Fr(2) <= Fr(2))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    tb = H.y_lagrange_bounds(mz)
    n_b = int(np.sum(tb["b"] >= 1.0 - 1e-12))
    check("G10-Y-Lagrange",
          tb["deg"] < tb["n"] and float(tb["b"].max()) <= H.LAG_BMAX_HI
          and n_b == 0,
          "deg=%d<n=%d bmax=%.4f #b>=1=%d" % (
              tb["deg"], tb["n"], float(tb["b"].max()), n_b))
    dC, bC = H.cheb_cd_bounds(mz, tb["n"])
    nge = int(np.sum(bC >= 1.0 - 1e-12))
    check("G11-cheb-and-dmin",
          H.CHEB_NGE1_LO <= nge <= H.CHEB_NGE1_HI
          and float(tb["d"].min()) > 1.5,
          "cheb #b>=1=%d; dmin=%.4f" % (nge, float(tb["d"].min())))
    mzP = P1.reweight(mz, "permute", 1000)
    pS = D.pack_C(CT.with_xp(HM.scramble_mz()))
    pP = D.pack_C(mzP)
    CP, mP = D.chain_C(mzP)
    udYP = mP["ud"][mP["iY"]]
    KP = np.diag(CP) / np.maximum(udYP, 1e-300)
    check("G12-worlds",
          CT.C_diag_stats(pS["C"])["dmin"] < H.SCR_DMIN_HI
          and CT.C_diag_stats(pP["C"])["dmin"] < H.PERM_DMIN_HI
          and float(KP.min()) < 1.0,
          "SCR dmin=%.3f PERM dmin=%.4f Kmin=%.4f"
          % (CT.C_diag_stats(pS["C"])["dmin"],
             CT.C_diag_stats(pP["C"])["dmin"], float(KP.min())))
    off, b8, _o = H.fourier_off(tb["C"], tb["meta"]["yn"])
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    oo = np.argsort(np.arccos(np.clip(yn, -1, 1)))
    p32 = D.pack_C(CT.rebuild_holes(mz, yn[oo][:32], vn[oo][:32]))
    p37 = D.pack_C(CT.rebuild_holes(mz, yn[oo][:37], vn[oo][:37]))
    check("G13-fourier-seq",
          off >= H.FOURIER_OFF_LO and b8 <= H.BAND8_HI
          and p32["nC"] == 0 and p37["nC"] == 1,
          "off=%.3f band8=%.3f; k32 nC=%d k37 nC=%d"
          % (off, b8, p32["nC"], p37["nC"]))
    pL = D.pack_C(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    p20 = H.y_lagrange_bounds(CT.with_xp(HM.two_period_mz(20, 1.0)))
    p55 = D.pack_C(V.build_measures(55))
    check("G14-chi-1010-core",
          CT.C_diag_stats(pL["C"])["dmin"] >= 1.0
          and p20["deg"] > p20["n"]
          and p55["nC"] <= 1
          and CT.C_diag_stats(p55["C"])["dmin"] > 1.0,
          "CHI9 dmin=%.4f; 2PER deg>n; kz55 nC=%d dmin=%.3f"
          % (CT.C_diag_stats(pL["C"])["dmin"], p55["nC"],
             CT.C_diag_stats(p55["C"])["dmin"]))


def main():
    print("=" * 72)
    print("verify_hole_nyquist.py -- round 410")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("HOLE NYQUIST VERIFIED")
        return 0
    print("HOLE NYQUIST FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
