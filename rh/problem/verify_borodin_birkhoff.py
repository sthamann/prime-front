#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_borodin_birkhoff.py -- machine check of every numbered
lemma in rh/problem/borodin_birkhoff_intertwiner.tex (round 409,
Borodin--Birkhoff intertwiner, ONE_DEFECT_TRANSPORT_CENSUS).

PART A (STANDALONE OVER Q):
  G1  three bases give identical S0; ker dim = d0-|Y|
  G2  dressed (W+S0)^{-1} = Hankel CD = C(I+C)^{-1}
  G3  Woodbury Theta = 22/29, eta = 9/11
  G4  u^vee = 1/u without P'^2 breaks exactness
  G5  d0 +/- 1 breaks S0

PART B (CONSTRUCTION PINS):
  G10 w9 graph vs r407 chain; inertia; ||T0|| pin
  G11 SEQ innovation pin (index 36, value -0.5117)
  G12 Pi_K=0 and Euler-direct must-fails
  G13 permute / scramble / jitter (algebra holds, signature breaks)
  G14 Phi literal miss; Krein unfitted miss
  G15 T^dagger = r362 graph factor; virtual spread; chi3-15 flip

Exit: per-gate PASS/FAIL and the final line
"BORODIN BIRKHOFF VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named census,
named refutations.
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

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402

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
    section("PART A  QUOTIENT / GRAPH / WOODBURY OVER Q")
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    S0s = {}
    for kind in ("mono", "newton", "cheb"):
        S0s[kind], kdim = B.S0_Q(xs, ud, iX, iY, d0, kind=kind)
    check("G1-three-basis-ker-Q",
          S0s["mono"] == S0s["newton"] == S0s["cheb"] and kdim == 1,
          "kdim=%d" % kdim)
    wY = [ud[i] for i in iY]
    WSi = B.BDH.fr_inv(B.fr_add(B.fr_diag(wY), S0s["mono"]))
    sY = [B.fr_sqrt_pos(w) for w in wY]
    Rw = [[sY[i] * WSi[i][j] * sY[j] for j in range(2)]
          for i in range(2)]
    Rh = B.hankel_dual_R_Q(xs, ud, iY, d0)
    Rc = B.R_from_C_Q(B.C_plus_Q(xs, ud, iX, iY, d0))
    check("G2-graph-equals-dual-CD-Q", Rw == Rh == Rc)
    H = [[Fr(3), Fr(1)], [Fr(1), Fr(4)]]
    e = [Fr(1), Fr(-1)]
    Hi = B.BDH.fr_inv(H)
    He = [Hi[0][0] * e[0] + Hi[0][1] * e[1],
          Hi[1][0] * e[0] + Hi[1][1] * e[1]]
    eta = He[0] * e[0] + He[1] * e[1]
    Th = Fr(1) / (Fr(1) / Fr(2) + eta)
    check("G3-woodbury-Q",
          eta == Fr(9, 11) and Th == Fr(22, 29),
          "Theta=%s eta=%s" % (Th, eta))
    ud_bad = [Fr(1) / u[j] for j in range(5)]
    S0b, _ = B.S0_Q(xs, ud_bad, iX, iY, d0, kind="mono")
    check("G4-mustfail-uvee", S0b != S0s["mono"])
    S0m, _ = B.S0_Q(xs, ud, iX, iY, d0 - 1, kind="mono")
    S0p, _ = B.S0_Q(xs, ud, iX, iY, d0 + 1, kind="mono")
    check("G5-mustfail-d0",
          S0m != S0s["mono"] and S0p != S0s["mono"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    g = B.pack_graph(mz)
    pk = DI.pack_C(mz)
    check("G10-w9-graph-inertia",
          B.relres(g["Rg"], pk["R"]) <= B.FORMULA_HI
          and g["nneg"] == pk["nneg"] == 1
          and B.W9_OP_LO <= g["opnorm"] <= B.W9_OP_HI,
          "||Rg-R||=%.3e nneg=%d ||T0||=%.5f"
          % (B.relres(g["Rg"], pk["R"]), g["nneg"], g["opnorm"]))
    piv = B.seq_innov(g["xp"], g["wX"], g["yn"], g["wY"], g["d0"])
    ineg = np.where(piv < 0)[0]
    check("G11-seq-pin",
          len(ineg) == 1 and int(ineg[0]) == B.W9_SEQ_IDX
          and abs(float(piv[ineg[0]]) - B.W9_SEQ_VAL) <= B.W9_SEQ_VAL_TOL,
          "idx=%d val=%.4f" % (int(ineg[0]), float(piv[ineg[0]])))
    Tpi0 = B.source_T0_cls(g["xp"], g["wX"], g["yn"], g["wY"],
                           len(g["yn"]))
    r0 = B.relres(np.linalg.solve(np.eye(len(g["yn"])) + Tpi0.T @ Tpi0,
                                 np.eye(len(g["yn"]))), pk["R"])
    import one_defect_gram_probe as OG
    A0 = pk["R"] - 0.5 * np.eye(len(g["yn"]))
    rE = B.relres(OG.euler_F(mz, g["yn"]) @ OG.euler_F(mz, g["yn"]).T, A0)
    check("G12-mustfail-PiK-and-euler",
          r0 >= B.PI0_LO and rE >= B.EULER_A0_LO,
          "PiK=0 rest=%.3f Euler-A0 rel=%.1f" % (r0, rE))
    mzP = P1.reweight(mz, "permute", 1000)
    gP, pP = B.pack_graph(mzP), DI.pack_C(mzP)
    mzS = HM.scramble_mz()
    gS, pS = B.pack_graph(mzS), DI.pack_C(mzS)
    mzG = P1.reweight(mz, "gauss", 409)
    gG, pG = B.pack_graph(mzG), DI.pack_C(mzG)
    check("G13-kills",
          B.relres(gP["Rg"], pP["R"]) <= 1e-8
          and gP["nneg"] >= B.PERM_NNEG_LO
          and gS["nneg"] == B.SCR_NNEG
          and B.relres(gG["Rg"], pG["R"]) <= B.FORMULA_HI
          and gG["nneg"] >= B.JITTER_NNEG_LO,
          "PERM nneg=%d SCR nneg=%d JIT nneg=%d"
          % (gP["nneg"], gS["nneg"], gG["nneg"]))
    Fx = OG.euler_F(mz, g["xp"])
    Gpos = (g["T0"].T @ Fx) @ (g["T0"].T @ Fx).T
    dsm = HS.window_data(9, comb=PB.smooth_comb(float(V.window_shape(9)[0])))
    td = B.source_Tdag(mz, dsm, Bm=PX.build_rung(9)["B"])
    i1, i2 = td["j1"], td["j2"]
    Sm = td["ZI"].shape[0] - 1
    idx = np.array([i1, i2, Sm])
    rest = np.array([i for i in range(Sm + 1) if i not in set(idx)])
    M = td["ZI"]
    Th = M[np.ix_(idx, idx)] - M[np.ix_(idx, rest)] @ np.linalg.solve(
        M[np.ix_(rest, rest)], M[np.ix_(rest, idx)])
    evTh = np.sort(np.linalg.eigvalsh(Th))
    evPhi = np.sort(np.array([-2.813229172977194, -0.06648163247724746,
                              1.8039076348414458]))
    mis = float(np.linalg.norm(evTh - evPhi)) / (
        float(np.linalg.norm(evPhi)) + 1e-30)
    check("G14-phi-and-krein-miss",
          B.nneg_sym(Gpos)[0] == 0
          and B.relres(Gpos, g["D0"]) >= 1.0
          and mis >= B.PHI_EV_MISMATCH_LO,
          "posGram nneg=0 rel(D0)=%.2f; Phi mismatch rel=%.2f"
          % (B.relres(Gpos, g["D0"]), mis))
    G = td["Tdag"].T @ td["Tdag"]
    n = G.shape[0]
    Rg = np.linalg.solve(np.eye(n) + G, np.eye(n))
    lamRd = float(B.nneg_sym(td["Rdag"])[1][0])
    mzc, dsmc = B.chi_border_rung(15, DMF.Q_CHI3, DMF.LPQ3)
    tdc = B.source_Tdag(mzc, dsmc)
    lamc = float(B.nneg_sym(tdc["Rdag"])[1][0])
    check("G15-tdag-and-dead-chi",
          B.relres(G, td["ZI"]) <= B.TDAG_REL_HI
          and B.relres(Rg, td["Rdag"]) <= B.TDAG_REL_HI
          and td["opnorm"] < B.TDAG_MAIN_HI and lamRd > 0.5
          and td["spread"] >= B.VIRT_SPREAD_LO
          and tdc["opnorm"] > 1.0 and lamc < 0.5,
          "||T*T-ZI||=%.3e spread=%.2f; chi15 ||T^d||=%.6f"
          % (B.relres(G, td["ZI"]), td["spread"], tdc["opnorm"]))


def main():
    print("=" * 72)
    print("verify_borodin_birkhoff.py -- round 409")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("BORODIN BIRKHOFF VERIFIED")
        return 0
    print("BORODIN BIRKHOFF FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
