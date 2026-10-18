#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_residual_loewner.py -- machine check of every
numbered lemma in rh/problem/residual_loewner.tex
(round 439, RESIDUAL_LOEWNER_PLUS_CONTROLLED_DIAGONAL).

PART A (STANDALONE OVER Q):
  G1  5-atom: disp rank 2, Cauchy-pi, S0 = K_YY^{-1}
  G2  5-atom dressed Loewner + inertia (1,1,0)
  G3  6-node: rank 2, ones-residual, S0 = K^{-1}
  G4  B1 miss + Sturm last != 1-q^dagger
  G5  constructor audit (no eig/SVD/pack_C/pack_graph)

PART B (CONSTRUCTION PINS):
  G10 w9 nneg=1, sigma3/sigma2, S0 vs K^{-1}
  G11 permute/scramble/chi census; rank-2 survives

Exit: "RESIDUAL LOEWNER VERIFIED" iff every gate passed.
NO RH CLAIM.  Finite identities, a named Bezout miss.
"""
from __future__ import annotations

import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import residual_loewner_probe as R  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
import r431_audit_probe as A  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

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
    section("PART A  DISPLACEMENT / K^{-1} / DRESSED / B1 OVER Q")
    xs, u, ud, iX, iY, d0, _ = S.prime_toy()
    t5 = R.toy_bundle(xs, ud, iX, iY, 2)
    disp5 = R.disp_Q(t5["D0"], t5["ys"])
    S0pi = S.s0_from_cauchy_pi_Q(t5["xX"], t5["wX"], t5["ys"])
    K5 = R.kernel_YY_Q(t5["xX"], t5["wX"], t5["ys"], 2)
    check("G1-5atom-rank-pi-Kinv",
          B.fr_rank(disp5) == 2 and R.mat_eq(t5["S0"], S0pi)
          and R.mat_eq(t5["S0"], BDH.fr_inv(K5)),
          "rank=2; Cauchy-pi; S0=K^{-1}")
    mt = [R.m_tilde_Q(t5["xX"], t5["wX"], t5["ys"], y)
          for y in t5["ys"]]
    mtp = [R.m_tilde_prime_Q(t5["xX"], t5["wX"], t5["ys"], y)
           for y in t5["ys"]]
    Lm = R.loewner_Q(t5["ys"], mt, mtp)
    Lnm = [[-a for a in row] for row in Lm]
    dsh = [t5["wY"][i] * t5["pr"][i] * t5["pr"][i]
           for i in range(2)]
    dD = [[t5["D0"][i][j] * t5["pr"][i] * t5["pr"][j]
           for j in range(2)] for i in range(2)]
    rhs = B.fr_add(Lnm, R.qdiag(dsh))
    check("G2-5atom-dressed-inertia",
          R.mat_eq(dD, rhs)
          and S.inertia_fr(t5["D0"]) == (1, 1, 0)
          and t5["D0"][1][1] == R.D11_K0,
          "dressed Loewner; D0 (1,1,0) D11=%s" % R.D11_K0)
    xs2, ud2, iX2, iY2 = A.second_toy()
    t6 = R.toy_bundle(xs2, ud2, iX2, iY2, 3)
    _f, res6 = R.ones_loewner_residual(t6["D0"], t6["ys"])
    K6 = R.kernel_YY_Q(t6["xX"], t6["wX"], t6["ys"], 3)
    check("G3-6node-rank-residual-Kinv",
          B.fr_rank(R.disp_Q(t6["D0"], t6["ys"])) == 2
          and res6 == R.ONES_RES_6
          and R.mat_eq(t6["S0"], BDH.fr_inv(K6))
          and S.inertia_fr(t6["D0"]) == (1, 2, 0),
          "rank=2; ones-res=%s; S0=K^{-1}; inertia (1,2,0)"
          % res6)
    Pc = R.P_Y_coeffs(t5["ys"])
    qy = R.Q_nodal_mtilde(t5["xX"], t5["wX"], t5["ys"])
    Qc = R.poly_coeffs_from_nodes(t5["ys"], qy)
    Bez = R.bezout_from_generating(Pc, Qc)
    n = 2
    V = [[t5["ys"][a] ** i for i in range(n)] for a in range(n)]
    Vi = BDH.fr_inv(V)
    M1 = R.qmul(R.qT(Vi), R.qmul(Bez, Vi))
    last = R.sturm_last_const(Pc, Qc)
    check("G4-B1-miss-sturm",
          R.mat_maxabs(M1, t5["D0"]) != 0
          and last == R.STURM_LAST_5 and last != R.QDAG_TOY,
          "Bez not D0; Sturm last=%s != 1-q^d" % last)
    leak = []
    for fn in R.CONSTRUCTORS:
        leak.extend(R.scope_audit(fn))
    check("G5-constructor-clean",
          leak == [],
          "no eig/SVD/pack_C/pack_graph"
          if not leak else "; ".join(leak))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w9 = R.window_row(9)
    check("G10-w9-disp-Kinv",
          w9["nneg"] == 1 and w9["ratio"] < R.RATIO_HI
          and w9["rel"] < R.KINV_REL
          and R.W9_OP_LO <= w9["op"] <= R.W9_OP_HI,
          "nneg=1 ||T||=%.5f s3/s2=%.3e Kinv rel=%.3e"
          % (w9["op"], w9["ratio"], w9["rel"]))
    mzP = P1.reweight(w9["mz"], "permute", 1000)
    gP = B.pack_graph(mzP)
    mzS = HM.scramble_mz()
    gS = B.pack_graph(mzS)
    g3 = B.pack_graph(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    g15 = B.pack_graph(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    ysP = np.asarray(gP["yn"], float)
    DP = np.asarray(gP["D0"], float)
    sigP = np.linalg.svd((ysP[:, None] - ysP[None, :]) * DP,
                         compute_uv=False)
    check("G11-kills-chi",
          gP["nneg"] >= R.PERM_NNEG_LO and gS["nneg"] == R.SCR_NNEG
          and g3["nneg"] == R.CHI3_9_NNEG
          and g15["nneg"] == R.CHI3_15_NNEG
          and float(sigP[2] / sigP[1]) < 1e-12,
          "PERM %d SCR %d CHI3-9/15 %d/%d; PERM s3/s2=%.3e"
          % (gP["nneg"], gS["nneg"], g3["nneg"], g15["nneg"],
             sigP[2] / sigP[1]))


def main():
    print("=" * 72)
    print("verify_residual_loewner.py -- residual_loewner.tex")
    print("SPEC_SHA %s" % R.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("RESIDUAL LOEWNER VERIFIED")
        return 0
    print("RESIDUAL LOEWNER NOTE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
