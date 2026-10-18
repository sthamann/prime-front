#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_source_potapov.py -- machine check of every
numbered lemma in rh/problem/source_potapov.tex
(round 431, SOURCE_FACTOR_NOT_FOUND).

PART A (STANDALONE OVER Q):
  G1  Redheffer product of unipotent mass matrices
      equals the Cauchy m-function of X
  G2  Cauchy-pi identity for Lagrange S0 at kdim=0
  G3  Gate 3 fails: D0 nneg=1, Cauchy-Pick nneg=0
  G4  constructor audit (no eig/SVD/pack_C/Z_loc)

PART B (CONSTRUCTION PINS):
  G10 w9 ||T0|| pin; Cauchy-Pick PD vs I-T*T nneg=1
  G11 kz15/kz18 same mismatch; source-order Uvarov
      has 0 negative pivots
  G12 permute/scramble/jitter inflate nneg(I-T*T);
      twin keeps nneg=1

Exit: "SOURCE POTAPOV VERIFIED" iff every gate passed.
NO RH CLAIM.  Finite identities, one named refutation.
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

import source_potapov_probe as S  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import twin_resolution_probe as TR  # noqa: E402
import arch_kernel_diophantine_probe as AKD  # noqa: E402
import minimal_firewall_probe as MF  # noqa: E402
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
    section("PART A  REDHEFFER / CAUCHY-PI / GATE 3 OVER Q")
    xs, u, ud, iX, iY, d0, labels = S.prime_toy()
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    labeled = [(labels[i][0], labels[i][1], xs[i], ud[i]) for i in iX]
    tot, _bl = S.prime_blocks_Q(labeled, S.Z_TEST)
    m_prod = S.m_of_chain_Q(tot)
    m_sum = sum(ud[i] / (xs[i] - S.Z_TEST) for i in iX)
    check("G1-redheffer-Q",
          m_prod == m_sum == S.M_TOY,
          "m=%s" % m_prod)
    S0pi = S.s0_from_cauchy_pi_Q(xX, wX, ys)
    S0k0, D0k0, _ITT, k0, _ = S.dressed_ITT_Q(xs, ud, iX, iY, 2)
    check("G2-cauchy-pi-Q",
          k0 == 0 and S0pi == S0k0)
    PX = S.cauchy_pick_Q(xX, wX, ys)
    check("G3-gate3-fail-Q",
          S.inertia_fr(D0k0)[1] == 1
          and S.inertia_fr(PX)[1] == 0
          and D0k0[1][1] == S.D11_K0,
          "D0 nneg=1 PX nneg=0")
    leak = []
    for fn in S.CONSTRUCTORS:
        leak.extend(S.scope_audit(fn))
    check("G4-constructor-clean",
          leak == [],
          "no eig/SVD/pack_C/Z_loc" if not leak else "; ".join(leak))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w9 = S.window_pick_row(9)
    g = w9["g"]
    check("G10-w9-gate3",
          S.W9_OP_LO <= g["opnorm"] <= S.W9_OP_HI
          and w9["nITT"] == 1 and w9["nPX"] == 0
          and w9["evPX0"] >= S.W9_PX_EMIN_LO,
          "||T0||=%.5f nITT=%d nPX=%d" % (
              g["opnorm"], w9["nITT"], w9["nPX"]))
    r15 = S.window_pick_row(15)
    r18 = S.window_pick_row(18)
    alpha, M, L, _Nw, D = V.window_shape(9)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1e-14, side="right"))
    i_lag = np.clip(np.rint(V.U[:ka] / D).astype(int), 0, M - 1)
    x_pp = np.cos(2.0 * np.pi * np.clip(i_lag, 1, L // 2) / L)
    attr = []
    for y in g["yn"]:
        j = int(np.argmin(np.abs(x_pp - y)))
        p, r = S.factor_PP(int(V.PP[j]))
        attr.append((p, r))
    ord_idx = sorted(range(len(attr)),
                     key=lambda i: (attr[i][0], attr[i][1], i))
    piv = B.seq_innov(g["xp"], g["wX"], g["yn"][ord_idx],
                      g["wY"][ord_idx], g["d0"])
    check("G11-windows-and-uvarov",
          r15["nITT"] == 1 and r15["nPX"] == 0
          and r18["nITT"] == 1 and r18["nPX"] == 0
          and int(np.sum(piv < 0)) == 0
          and float(np.min(piv)) >= S.SRC_PIV_MIN_LO,
          "kz15/18 mismatch; source-order nneg pivots=0 min=%.3e"
          % float(np.min(piv)))
    mzP = P1.reweight(w9["mz"], "permute", 1000)
    gP = B.pack_graph(mzP)
    mzG = P1.reweight(w9["mz"], "gauss", 431)
    gG = B.pack_graph(mzG)
    mzS = HM.scramble_mz()
    gS = B.pack_graph(mzS)
    uuc, mmc = TR.base_comb(9)
    mzD = TR.build_world(9, uuc, mmc)
    gapsc = MF.local_gaps(uuc)
    u2c, m2c, _dn, _du = AKD.twin_rational(
        uuc, mmc, gapsc, mzD["D"], 1.0e-8)
    gT = B.pack_graph(TR.build_world(9, u2c, m2c))
    check("G12-kills-and-twin",
          gP["nneg"] >= S.PERM_NNEG_LO and gS["nneg"] == S.SCR_NNEG
          and gG["nneg"] >= S.JIT_NNEG_LO
          and gT["nneg"] == 1
          and abs(gT["opnorm"] - g["opnorm"]) <= S.FORMULA_HI,
          "PERM %d SCR %d JIT %d TWIN nneg=%d" % (
              gP["nneg"], gS["nneg"], gG["nneg"], gT["nneg"]))


def main():
    print("=" * 72)
    print("verify_source_potapov.py -- source_potapov.tex")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("SOURCE POTAPOV VERIFIED")
        return 0
    print("SOURCE POTAPOV FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
