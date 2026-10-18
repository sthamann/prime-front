#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_r431_audit.py -- machine check of every numbered
lemma in rh/problem/r431_audit.tex (round 431-AUDIT,
CONFIRMED).

PART A (STANDALONE OVER Q / C):
  G1  unipotent product = Cauchy m_X = -7471/22950
  G2  Cauchy-pi = Lagrange; D0 inertia (1,1,0),
      D11=-1744/2025; P_X inertia (2,0,0)
  G3  BP factors do not commute; J-kernel Pick PD
  G4  Homma Redheffer star = chain product; unipotent
      star is the mass sum
  G5  second Q-window: Cauchy-pi exact; D0 has a
      negative square; P_X PD

PART B (CONSTRUCTION PINS):
  G10 w9 lam_min(P_X) in [8.67, 8.685], ind_-(I-TT)=1
  G11 source-order Uvarov 0 negative pivots; position
      order one negative at index 36

Exit: "R431 AUDIT NOTE VERIFIED" iff every gate passed.
NO RH CLAIM.  Finite identities, one named closure lemma.
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

import r431_audit_probe as A  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
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
    section("PART A  LEMMA + Q IDENTITIES + NON-COMMUTING CLASS")
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    wY = [ud[i] for i in iY]
    tot = A.chain_uni_Q(list(zip(xX, wX)), A.Z_TEST)
    m_prod = tot[1][0] / tot[0][0]
    m_sum = sum(w / (x - A.Z_TEST) for x, w in zip(xX, wX))
    check("G1-cauchy-sum-Q",
          m_prod == m_sum == A.M_TOY,
          "m=%s" % m_prod)
    S0pi = A.cauchy_pi_S0_Q(xX, wX, ys)
    S0lag = A.lagrange_S0_Q(xX, wX, ys)
    D0 = A.qsub(A.qdiag(wY), S0pi)
    PX = A.cauchy_pick_Q(xX, wX, ys)
    check("G2-cauchy-pi-and-inertia-Q",
          S0pi == S0lag
          and A.inertia_fr(D0) == (1, 1, 0)
          and A.inertia_fr(PX) == (2, 0, 0)
          and D0[1][1] == A.D11_K0)
    atoms = A.source_bp_atoms(xX, wX)
    z0 = 1j
    B0 = A.potapov_factor(z0, atoms[0][0], atoms[0][1])
    B1 = A.potapov_factor(z0, atoms[1][0], atoms[1][1])
    comm = float(np.linalg.norm(B0 @ B1 - B1 @ B0, "fro"))
    zs = [complex(float(y), 0.11) for y in ys]
    H = A.j_kernel_pick(atoms, zs)
    nnegH, evH = A.nneg_sym(H.real, 1e-10)
    check("G3-BP-noncommute-Pick-PD",
          comm > 1e-6 and nnegH == 0,
          "comm=%.3e nneg=%d" % (comm, nnegH))
    Thetas = [A.potapov_factor(z0, a, u) for a, u in atoms]
    T_chain = Thetas[0]
    for T in Thetas[1:]:
        T_chain = T_chain @ T
    T_star = A.redheffer_product(Thetas)
    z_r = A.Fr(1, 3)
    m0 = float(wX[0] / (xX[0] - z_r))
    m1 = float(wX[1] / (xX[1] - z_r))
    Ustar = A.redheffer_product([
        np.array([[1.0, 0.0], [m0, 1.0]], complex),
        np.array([[1.0, 0.0], [m1, 1.0]], complex),
    ])
    check("G4-Redheffer-star",
          float(np.linalg.norm(T_chain - T_star, "fro")) < 1e-10
          and abs(Ustar[1, 0] - (m0 + m1)) < 1e-12)
    xs2, ud2, iX2, iY2 = A.second_toy()
    xX2 = [xs2[i] for i in iX2]
    wX2 = [ud2[i] for i in iX2]
    ys2 = [xs2[i] for i in iY2]
    wY2 = [ud2[i] for i in iY2]
    S0b = A.cauchy_pi_S0_Q(xX2, wX2, ys2)
    D02 = A.qsub(A.qdiag(wY2), S0b)
    PX2 = A.cauchy_pick_Q(xX2, wX2, ys2)
    check("G5-second-window",
          S0b == A.lagrange_S0_Q(xX2, wX2, ys2)
          and A.inertia_fr(D02)[1] >= 1
          and A.inertia_fr(PX2)[1] == 0)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    g = B.pack_graph(mz)
    PX = A.cauchy_pick_f64(g["xp"], g["wX"], g["yn"])
    nPX, evPX = A.nneg_sym(PX, 1e-12)
    nITT, evITT = A.nneg_sym(np.eye(len(g["yn"])) - g["TT"], 1e-12)
    check("G10-w9-PX-ITT",
          nPX == 0 and nITT == 1
          and A.W9_PX_LO <= float(evPX[0]) <= A.W9_PX_HI
          and float(evITT[0]) < 0,
          "lam_min=%.5f nITT=%d" % (float(evPX[0]), nITT))
    alpha, M, L, _Nw, D = V.window_shape(9)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1e-14, side="right"))
    i_lag = np.clip(np.rint(V.U[:ka] / D).astype(int), 0, M - 1)
    x_pp = np.cos(2.0 * np.pi * np.clip(i_lag, 1, L // 2) / L)
    attr = []
    for y in g["yn"]:
        j = int(np.argmin(np.abs(x_pp - y)))
        p, r = A.factor_PP(int(V.PP[j]))
        attr.append((p, r))
    ord_idx = sorted(range(len(attr)),
                     key=lambda i: (attr[i][0], attr[i][1], i))
    piv_src = B.seq_innov(g["xp"], g["wX"], g["yn"][ord_idx],
                          g["wY"][ord_idx], g["d0"])
    piv_pos = B.seq_innov(g["xp"], g["wX"], g["yn"], g["wY"], g["d0"])
    ineg = np.where(piv_pos < 0)[0]
    check("G11-Uvarov-orders",
          int(np.sum(piv_src < 0)) == 0
          and float(np.min(piv_src)) >= A.SRC_PIV_MIN_LO
          and len(ineg) == 1 and int(ineg[0]) == A.W9_SEQ_IDX,
          "src min=%.3e pos idx=%d"
          % (float(np.min(piv_src)), int(ineg[0])))


def main():
    print("=" * 72)
    print("verify_r431_audit.py -- r431_audit.tex")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("R431 AUDIT NOTE VERIFIED")
        return 0
    print("R431 AUDIT NOTE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
