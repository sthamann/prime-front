#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_mean_tau.py -- machine check of every numbered
lemma in rh/problem/mean_tau_index.tex (round 440,
IDENTITIES_EXACT / COLLAR_BOSS_QUANTIFIED /
BLOCK_MEAN_CENSUS / UNCONDITIONAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  2x2 T1: G=diag(2,1/2), ind_-(R-1/2 I)=1,
      zeros of tau at {1/2, 2}
  G2  T2 winding of that tau about (0,1) equals 1
  G3  r409 5-atom toy: C pin, kappa=0, G=C^{-1}
  G4  MI2 linearity on two 2x2 Grams

PART B (CONSTRUCTION PINS):
  G10 w9 T1 three-way kappa=0; dictionary residuals
  G11 collar: no zeros in (0,0.9); r=0.40 winds 0;
      r=0.499 fractional
  G12 source: CD + cyclic TT* + Dirichlet diagonal
  G13 dead CHI3-15 kappa=1; living CHI3-9 kappa=0;
      trG/M2 blind

Exit: "MEAN TAU INDEX VERIFIED" iff every gate passed.
NO RH CLAIM.
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

import mean_tau_index_probe as S  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
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
    section("PART A  T1 / T2 / TOY / MI2 OVER Q")
    t = S.q_kappa1()
    check("G1-Q-T1-kappa1",
          t["M"][0][0] == Fr(-1, 6)
          and t["M"][1][1] == Fr(1, 6)
          and t["zeros"][0] == Fr(1, 2)
          and t["kappa"] == 1,
          "ind_-=1; tau zeros {1/2, 2}")
    Gf = np.array([[2.0, 0.0], [0.0, 0.5]])
    w = S.winding_circle(Gf, 0.5, 0.49, n=128)
    check("G2-Q-T2-winding",
          abs(w.real - 1.0) < 1e-12,
          "winding=%.12f" % w.real)
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    C = B.C_plus_Q(xs, ud, iX, iY, d0)
    Ci = BDH.fr_inv(C)
    xp = np.array([float(xs[i]) for i in iX])
    wX = np.array([float(ud[i]) for i in iX])
    yn = np.array([float(xs[i]) for i in iY])
    wY = np.array([float(ud[i]) for i in iY])
    T0m = B.source_T0_cls(xp, wX, yn, wY, d0)
    G0 = T0m.T @ T0m
    Cinv = np.array([[float(Ci[i][j]) for j in range(2)]
                     for i in range(2)])
    res = float(np.linalg.norm(G0 - Cinv) / (np.linalg.norm(G0) + 1e-30))
    check("G3-Q-toy-kappa0",
          C[0][0] == Fr(97) and C[1][1] == Fr(125, 16)
          and res < 1e-12,
          "C pin; G=C^{-1} res=%.2e" % res)
    G2 = np.diag([0.4, 0.3])  # both lambda<1, kappa=0
    Gs = [Gf, G2]
    w1 = S.winding_circle(Gf, 0.5, 0.40, n=64)
    w2 = S.winding_circle(G2, 0.5, 0.40, n=64)
    wm = S.winding_mean(Gs, 0.5, 0.40, n=64)
    check("G4-MI2-linearity-Q",
          abs(wm - 0.5 * (w1 + w2)) < 1e-12
          and abs(w1.real - 1.0) < 1e-8
          and abs(w2.real) < 1e-8,
          "mean winds=%.6f avg-integrand=%.6f"
          % ((w1.real + w2.real) / 2, wm.real))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    td, mz = S.tdag_main(9)
    p = S.pack_tau(td)
    check("G10-w9-T1-dictionary",
          p["kappa_G"] == 0 and p["kappa_R"] == 0
          and p["nzeros01"] == 0
          and p["res_RG"] < S.ID_RES and p["res_M"] < S.ID_RES
          and p["n"] == S.W9_N,
          "kappa=0 three-way; n=%d res_RG=%.2e"
          % (p["n"], p["res_RG"]))
    w40 = S.winding_circle(p["G"], 0.5, 0.40, n=128)
    w99 = S.winding_circle(p["G"], 0.5, 0.499, n=256)
    check("G11-collar-boss",
          abs(w40.real) < S.WIND_BAR and abs(w99.real) > 0.2
          and p["n_half"] == S.W9_NHALF
          and int(np.sum((p["zeros"] > 0) & (p["zeros"] < 0.9))) == 0,
          "r=0.40 wind=%.4f; r=0.499 wind=%.4f n_half=%d"
          % (w40.real, w99.real, p["n_half"]))
    d0u = int(mz["Nw"]) - 3
    _Gu, _Ku, _wY, res_cd, _T = S.cd_unaug(mz, d0u)
    H = 0.5 * (p["T"] @ p["T"].T + (p["T"] @ p["T"].T).T)
    s = 0.37
    dlog_G = S.dlog_tau(p["G"], s)
    dlog_H = S.dlog_tau(H, s)
    check("G12-source-form",
          res_cd < S.CD_RES and abs(dlog_G - dlog_H) < S.CYC_RES,
          "CD res=%.2e; cyclic dlog diff=%.2e"
          % (res_cd, abs(dlog_G - dlog_H)))
    mzc, dsmc = B.chi_border_rung(15, DMF.Q_CHI3, DMF.LPQ3)
    pD = S.pack_tau(B.source_Tdag(mzc, dsmc))
    mzl, dsml = B.chi_border_rung(9, DMF.Q_CHI3, DMF.LPQ3)
    pL = S.pack_tau(B.source_Tdag(mzl, dsml))
    check("G13-dead-live-soft-kill",
          pD["kappa_G"] == 1 and pL["kappa_G"] == 0
          and p9_trG_ok(p) and pD["trG"] > 20.0
          and p["M2"] > 20.0 and pD["M2"] > 20.0,
          "dead15 kappa=1 live9 kappa=0; trG %.2f vs %.2f "
          "(soft mutants blind)"
          % (p["trG"], pD["trG"]))


def p9_trG_ok(p):
    return abs(p["trG"] - S.W9_TRG) / S.W9_TRG < 0.02


def main():
    print("=" * 72)
    print("verify_mean_tau.py -- round 440")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("MEAN TAU INDEX VERIFIED")
        return 0
    print("MEAN TAU INDEX FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
