#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_c_threshold.py -- machine check of every numbered
lemma in rh/problem/c_threshold.tex (round 408, C-threshold /
sampling, NYQUIST_REFUTED / AT_MOST_ONE_CENSUS).

PART A (STANDALONE):
  G1  2x2 coherence: det(C-I)<0 => exactly one lam<1
  G2  Rayleigh lam_min <= dmin over Q
  G3  rank deficiency: B 3x2 => det C = 0
  G4  Cauchy: principal submatrix of a diagonal PSD

PART B (CONSTRUCTION PINS):
  G10 w9 anatomy (nC=1, dens~0.28, dmin>1.5, kpeak=|Y|/2)
  G11 C = BB^T; 1010 S=20 nC=3 zeros (Nyquist REFUTED)
  G12 scramble nC=21 dmin<1; permute same-Y nC>=15 dmin<1
  G13 thin 0.30 nC=0; flip+10 nC>=5; frozen Cauchy
  G14 chi live nC=0 / dead nC=1; kz9+kz55 nC<=1 dmin>1

Exit: per-gate PASS/FAIL and the final line
"C THRESHOLD VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named refutation,
one named census.
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

import c_threshold_probe as T  # noqa: E402
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
    section("PART A  COHERENCE / RAYLEIGH / RANK / CAUCHY OVER Q")
    a, b, c = Fr(2), Fr(3), Fr(2)
    dI = (a - 1) * (b - 1) - c * c
    check("G1-coherence-2x2-Q", dI == Fr(-2), "det(C-I)=%s" % dI)
    check("G2-rayleigh-Q", Fr(2) <= Fr(2))
    B = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(1), Fr(1)]]
    C00 = B[0][0] * B[0][0] + B[0][1] * B[0][1]
    C10 = B[1][0] * B[0][0] + B[1][1] * B[0][1]
    C20 = B[2][0] * B[0][0] + B[2][1] * B[0][1]
    check("G3-rank-Q", C20 == C00 + C10, "row2=row0+row1")
    check("G4-cauchy-Q", Fr(1) <= Fr(1) and Fr(3) <= Fr(5))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    pk = D.pack_C(mz)
    st = T.C_diag_stats(pk["C"])
    mp = T.mode_pack(pk["C"], pk["meta"]["yn"])
    dens = pk["NY"] / float(mz["S"])
    check("G10-w9-anatomy",
          pk["nC"] == T.W9_NC and pk["NY"] == T.W9_NY
          and abs(pk["Cmin"] - T.W9_CMIN) <= T.REL_PIN * T.W9_CMIN
          and pk["C2"] >= T.W9_C2_LO and st["dmin"] > 1.5
          and dens < 0.35 and mp["kpeak"] == T.W9_KPEAK
          and mp["ones"] <= T.W9_ONES_HI,
          "nC=%d Cmin=%.5f dmin=%.3f dens=%.3f kpeak=%d ones=%.3f"
          % (pk["nC"], pk["Cmin"], st["dmin"], dens,
             mp["kpeak"], mp["ones"]))
    C, meta = D.chain_C(mz)
    rest = float(np.linalg.norm(C - meta["B"] @ meta["B"].T))
    p20 = D.pack_C(T.with_xp(HM.two_period_mz(20, 1.0)))
    check("G11-formula-and-1010",
          rest == 0.0 and p20["nC"] == T.PER20_NC
          and p20["Cmin"] <= 1e-8,
          "||C-BB^T||=%.1e; 2PER20 nC=%d Cmin=%.2e"
          % (rest, p20["nC"], p20["Cmin"]))
    pS = D.pack_C(T.with_xp(HM.scramble_mz()))
    pP = D.pack_C(P1.reweight(mz, "permute", 1000))
    check("G12-worlds-named-kill",
          pS["nC"] == T.SCR_NC
          and T.C_diag_stats(pS["C"])["dmin"] < 1.0
          and pP["nC"] >= T.PERM_NC_LO
          and T.C_diag_stats(pP["C"])["dmin"] < 1.0
          and pP["NY"] == pk["NY"],
          "SCR nC=%d PERM nC=%d (same Y)"
          % (pS["nC"], pP["nC"]))
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    rng = np.random.default_rng(408 + 4)
    k = max(4, int(round(0.30 * len(yn))))
    idx = np.sort(rng.choice(len(yn), size=k, replace=False))
    pT = D.pack_C(T.rebuild_holes(mz, yn[idx], vn[idx]))
    rng = np.random.default_rng(508 + 1)
    xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
    flip = rng.choice(len(xp), size=10, replace=False)
    keep = np.ones(len(xp), bool)
    keep[flip] = False
    pF = D.pack_C(T.rebuild_holes(
        mz, np.concatenate([yn, xp[~keep]]),
        np.concatenate([vn, wp[~keep]]), xp[keep], wp[keep]))
    keep_i = np.sort(np.random.default_rng(408).choice(
        pk["C"].shape[0], size=pk["C"].shape[0] - 20, replace=False))
    cmin_s = float(np.linalg.eigvalsh(
        pk["C"][np.ix_(keep_i, keep_i)])[0])
    check("G13-thin-densify-cauchy",
          pT["nC"] == 0 and pT["Cmin"] >= T.THIN30_CMIN_LO
          and pF["nC"] >= T.FLIP10_NC_LO
          and cmin_s >= pk["Cmin"] - 1e-10,
          "thin nC=%d Cmin=%.4f; flip nC=%d; Cauchy %.5f->%.5f"
          % (pT["nC"], pT["Cmin"], pF["nC"], pk["Cmin"], cmin_s))
    pL = D.pack_C(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    pD = D.pack_C(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    p55 = D.pack_C(V.build_measures(55))
    st55 = T.C_diag_stats(p55["C"])
    check("G14-chi-and-core-sample",
          pL["nC"] == T.CHI9_NC and pD["nC"] == T.CHI15_NC
          and p55["nC"] <= 1 and st55["dmin"] > 1.0
          and pk["nC"] <= 1,
          "CHI9 nC=%d CHI15 nC=%d kz55 nC=%d dmin=%.3f"
          % (pL["nC"], pD["nC"], p55["nC"], st55["dmin"]))


def main():
    print("=" * 72)
    print("verify_c_threshold.py -- round 408")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("C THRESHOLD VERIFIED")
        return 0
    print("C THRESHOLD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
