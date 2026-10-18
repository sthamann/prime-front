#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_sign_schur.py -- machine check of every numbered
lemma in rh/problem/sign_schur.tex (round 394, Sign-Schur
reduced).

PART A (STANDALONE):
  G1  Dirichlet sign identity on cosine grids
  G2  Dirichlet envelope |D_n| <= min(2n+1, 1/|sin(a/2)|)
  G3  Chebyshev-CD = Dirichlet combination
  G4  2x2 Z-matrix: lambda = 1+c > maxdiag (hoped M-bound false)
  G5  bookkeeping lambda = maxdiag*(1+assist)
  G6  checkerboard S_ij = (-1)^{i-j} is rank-1
  G7  cosine mesh step = pi/S

PART B (CONSTRUCTION PINS):
  G10 w9 assist 0.0399, canc > 0.99, lam < 1
  G11 w9 Chebyshev mass-agree ww in (0.78, 0.85)
  G12 w9 checkerboard ww in (0.45, 0.56) -- coin, REFUTED
  G13 w9 lambda(|E|) in (1.50, 1.90) > 1
  G14 two-period k=22: NN all positive and lam>1
  G15 scramble seed=1: Cheb ww > 0.70 and lam > 2
  G16 two-period k=40: -CB agree = 1 (too late)

Exit: per-gate PASS/FAIL and the final line
"SIGN SCHUR VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, named counterexamples, and
construction pins only.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import sign_schur_probe as P  # noqa: E402
import coherence_assist_probe as CA  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402

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
    section("PART A  DIRICHLET SIGNS, ENVELOPE, Z-MATRIX")
    check("G1-Dirichlet-sign-identity",
          P.dirichlet_sign_ok(16, 7) and P.dirichlet_sign_ok(12, 5))
    ok_env, mxrel = P.dirichlet_envelope_ok()
    check("G2-Dirichlet-envelope",
          ok_env and mxrel < P.ENV_BAR,
          "max(abs/env-1)=%.3e" % mxrel)
    ok_cd = True
    for n, th, ph in ((5, 0.3, 1.1), (12, 0.7, 0.7), (8, 0.0, math.pi)):
        if abs(CA.cheb_K_closed(n, th, ph) - CA.cheb_K_sum(n, th, ph)) > P.CHEB_BAR:
            ok_cd = False
    check("G3-Chebyshev-CD-Dirichlet", ok_cd)
    c = 0.4
    A = np.array([[1.0, -c], [-c, 1.0]])
    lam = float(np.linalg.eigvalsh(A)[-1])
    check("G4-Z-matrix-bound-false",
          abs(lam - (1.0 + c)) < 1e-12 and lam > 1.0,
          "lambda=1+c=%.2f" % lam)
    E = np.array([[2.0, 1.0], [1.0, 2.0]])
    gs = P.gram_stats(E)
    check("G5-bookkeeping",
          abs(gs["lam"] - gs["maxd"] * (1.0 + gs["assist"])) < 1e-12)
    Scb, s = P.checkerboard(6)
    ok_cb = all(Scb[i, j] == (-1) ** (i - j)
                for i in range(6) for j in range(6) if i != j)
    check("G6-checkerboard-rank1", ok_cb)
    S = 16
    j = np.array([3, 4])
    th = np.arccos(np.cos(P.PI * j / S))
    check("G7-mesh-step-pi-over-S",
          abs(abs(th[1] - th[0]) - P.PI / S) < 1e-14)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(P.MAIN_KZ)
    N = int(mz["Nw"])
    depth = N - 1
    print("    w9 n=%d ..." % N, flush=True)
    B = CA.make_B(mz, depth)
    th, yn, vn, B = P.order_by_theta(mz["yn"], mz["vn"], B)
    E = P.E_from_B(B, depth)
    pw = P.sign_pack(E, th, depth)
    gs = pw["gs"]
    check("G10-w9-wall-assist",
          P.W9_ASSIST_LO < gs["assist"] < P.W9_ASSIST_HI
          and gs["canc"] > P.W9_CANC_FLOOR and gs["lam"] < 1.0,
          "assist=%.4f canc=%.4f" % (gs["assist"], gs["canc"]))
    check("G11-w9-Cheb-mass-agree",
          P.W9_CHEB_WW[0] < pw["ww_c"] < P.W9_CHEB_WW[1],
          "ww=%.3f" % pw["ww_c"])
    check("G12-w9-checkerboard-coin",
          P.W9_CB_WW[0] < pw["ww_b"] < P.W9_CB_WW[1],
          "CB ww=%.3f" % pw["ww_b"])
    check("G13-w9-absE-mutant",
          P.W9_LAMABS[0] < gs["lam_abs"] < P.W9_LAMABS[1],
          "lambda(|E|)=%.3f" % gs["lam_abs"])

    mz23 = CA.two_period(81, P.C_FLANK)
    B23 = CA.make_B(mz23, 40)
    th23, yn23, vn23, B23 = P.order_by_theta(mz23["yn"], mz23["vn"], B23)
    p22 = P.sign_pack(P.E_from_B(B23, 22), th23, 22)
    check("G14-two-period-in-phase",
          p22["nn_neg"] == 0 and p22["gs"]["lam"] > 1.0,
          "NN pos/neg=%d/%d lam=%.4f" % (p22["nn_pos"], p22["nn_neg"],
                                         p22["gs"]["lam"]))

    ds = HS.window_data(9, scramble_seed=P.SCR_SEED)
    ns = int(ds["n_max"]) - 1
    a, b, h0 = V.mu_chain(ds["xs"], ds["ws"], ns)
    Bsc = V.b_matrix(a, b, h0, ds["ys"], ds["vs"], ns)
    ths, yns, vns, Bsc = P.order_by_theta(ds["ys"], ds["vs"], Bsc)
    psc = P.sign_pack(P.E_from_B(Bsc, min(ns, depth)), ths, min(ns, depth))
    check("G15-scramble-envelope",
          psc["ww_c"] > P.SCR_WW_LO and psc["gs"]["lam"] > P.SCR_LAM_FLOOR,
          "Cheb ww=%.3f lam=%.3e" % (psc["ww_c"], psc["gs"]["lam"]))

    uw_ncb, _ww = P.mass_agree(P.E_from_B(B23, 40),
                               -P.checkerboard(B23.shape[0])[0])
    p40 = P.sign_pack(P.E_from_B(B23, 40), th23, 40)
    check("G16-two-period-antiCB-too-late",
          abs(uw_ncb - 1.0) < 1e-12 and p40["gs"]["lam"] > 1.0,
          "-CB agree=%.3f lam=%.3f" % (uw_ncb, p40["gs"]["lam"]))


def main():
    print("=" * 72)
    print("verify_sign_schur.py -- round 394")
    print("=" * 72)
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("SIGN SCHUR VERIFIED")
        return 0
    print("SIGN SCHUR FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
