#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""source_potapov_probe --
PRIME.RDAGGER.SOURCE_POTAPOV_FACTOR.01 (round 431,
reviewer discovery 1 of 2): a source-pure rational
transfer Theta_k = Theta_inf star prod_{p <= 2^{2k}}
Theta_{p,k} whose finite Pick matrix on the canonical
nodes is congruent to I - T0* T0 (GraphResolvent).

THE CONSTRUCTOR (no target leak).  Each prime-power
atom n = p^r contributes a unipotent 2x2 J-factor
    E(z; x, w) = [[1, 0], [w/(x-z), 1]]
built only from the source tuple (p, r, x=fold(r log p)
or a rational stand-in, w from Lambda / dual weight,
Fold, Tent, Arch, Border).  Theta_{p,k} is the
Redheffer/chain product of those E over r; Theta_inf
is the Arch/completion atom.  The star is 2x2 matrix
multiplication.  FORBIDDEN in the constructor:
eig(C), SVD of T0, target Schur complements, Z_loc,
post-hoc fit.

LEGS.
  A  Q-exact toys (2-3 primes, small r).  The product
     equals the Cauchy m-function of the X-measure
     (abelian).  At kdim=0 the Lagrange S0 is the
     Cauchy-Pick of the pi_Y(X)^2-dressed X-measure
     (named congruence).  Gate 3: that Pick is NOT
     congruent to I-T*T on a nneg=1 toy.
  B  w9 + kz15 + kz18: Cauchy-Pick of X at Y is PD
     (kappa=0); I-T*T has nneg=1.  Machine Gate 3 fail.
  C  Index anatomy for R432: (i) source-ordered
     growing-Y Uvarov on w9 has ZERO negative pivots
     (min 3.25e-7) -- the one square is not a prime
     prefix; (ii) lag-local interpolants fold(c^P_p)
     have nneg 15-19, NOT simpler than the full
     operator (stop rule 3).
  D  Kills: Lambda-permute / jitter / scramble inflate
     nneg(I-T*T); the Euler product stays kappa=0
     (index-blind).  Twin keeps nneg=1.

CALIBRATION DISCLOSURE.  Q identities, w9/kz15/kz18
Pick mismatch, source-order Uvarov, lag-local nneg,
permute/jitter/scramble/twin first measured in /tmp
(r431_cal.py, r431_cal2.py, r431_cal3.py) on the r409
constructors, 2026-08-30.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall < 5 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Q: E-product = sum_X w/(x-z) EXACT (z=7/3 gives
    -7471/22950).  product_p Theta_p = Theta_tot.
  * Q kdim=0: S0 = Delta^{-1} PXpi Delta^{-1} EXACT;
    D0 nneg=1 (D11=-1744/2025); PX nneg=0.
  * w9: ||T0||=1.08014 nneg(I-TT)=1; Cauchy-Pick
    nneg=0 evmin=8.677.  kz15 ||T||=1.10672 nneg=1
    vs PX nneg=0; kz18 ||T||=1.24966 nneg=1 vs PX 0.
  * Source-order Uvarov: 0/104 negative pivots,
    min=3.248e-7.  Position-order (r409) has one
    negative at index 36 -- order-dependent, not a
    prime-block localization.
  * Lag-local T_p (fold of that prime's tents, global
    X/Y mask): p=2 nneg=18, p=3 nneg=19, p=5 nneg=15,
    Arch nneg=9 -- NOT simpler than nneg=1.
  * PERM nneg=20 ||T||=7.42; JITTER 19 ||T||=1.97;
    SCRAMBLE 21 ||T||=16.66.  TWIN nneg=1,
    ||T|| bit-near 1.08014.

AUSGANG SOURCE_FACTOR_NOT_FOUND.
SATZ: the unipotent Redheffer product is the Cauchy
m-function of X; the Cauchy-pi identity for Lagrange
S0 at kdim=0.  REFUTED: Pick(product) congruent to
I-T*T (kappa 0 vs 1 on every one-defect window).
CENSUS: the one negative square of GraphResolvent is
the interpolant residual D0 = W_Y - S0, not an Euler
factor; source-ordered Uvarov does not isolate it;
lag-local prime interpolants have larger index.
R432 (Krein-Langer index one) is blocked (FACTOR_EXACT
not met).  Does not move the mincut.  No RH claim.

MACHINERY: r409 B.S0_Q / toy_dual / pack_graph /
source_T0_cls / seq_innov / dual_split; r407 DI
pack_C (control only); r403 P1.reweight; r398 HM
scramble; r226 V build_measures / prime_lags /
arch_lags; r356 dual_weights; r289 twin via TR/AKD.

NO RH CLAIM.  Finite identities, one named refutation,
one named anatomy.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from collections import OrderedDict
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import twin_resolution_probe as TR  # noqa: E402
import arch_kernel_diophantine_probe as AKD  # noqa: E402
import minimal_firewall_probe as MF  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"

FORMULA_HI = 1.0e-8
W9_OP_LO, W9_OP_HI = 1.05, 1.12
KZ15_OP_LO, KZ15_OP_HI = 1.09, 1.13
KZ18_OP_LO, KZ18_OP_HI = 1.20, 1.30
W9_PX_EMIN_LO = 1.0
SRC_PIV_MIN_LO = 1.0e-8
PERM_NNEG_LO, SCR_NNEG, JIT_NNEG_LO = 15, 21, 2
LAG_NNEG_LO = 5
M_TOY = Fr(-7471, 22950)
D11_K0 = Fr(-1744, 2025)
Z_TEST = Fr(7, 3)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("elem_mass_Q", "chain_product_Q", "cauchy_pick_Q",
                "prime_blocks_Q", "s0_from_cauchy_pi_Q")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; unipotent "
                       "Redheffer / Cauchy-Pick / S0_Q only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def scope_audit(funcname):
    """TARGET_LEAK: factor constructors must not read
    eig(C), SVD of T0, pack_C/pack_graph, Z_loc, Cholesky."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"eigvalsh", "eigh", "svd", "cholesky", "pack_C",
              "chain_C", "pack_graph", "r_nm3", "aug_rung",
              "norm"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def nneg_sym(A, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (np.asarray(A, float)
                                   + np.asarray(A, float).T))
    return int(np.sum(ev < -floor)), ev


def inertia_fr(M):
    n = len(M)
    A = [row[:] for row in M]
    npos = nneg = nzer = 0
    for k in range(n):
        piv = A[k][k]
        if piv == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                nzer += 1
                continue
            A[k], A[sw] = A[sw], A[k]
            for i in range(n):
                A[i][k], A[i][sw] = A[i][sw], A[i][k]
            piv = A[k][k]
        if piv > 0:
            npos += 1
        else:
            nneg += 1
        for i in range(k + 1, n):
            if A[i][k] == 0:
                continue
            f = A[i][k] / piv
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    return npos, nneg, nzer


# ---------- source-pure factor constructors (AST-audited) ----------
def elem_mass_Q(z, x, w):
    """Unipotent 2x2 of a point mass.  Only (z, x, w)."""
    return [[Fr(1), Fr(0)], [w / (x - z), Fr(1)]]


def matmul2_Q(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def chain_product_Q(atoms, z):
    """Redheffer star = 2x2 product of elem_mass, source order."""
    T = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    for x, w in atoms:
        T = matmul2_Q(T, elem_mass_Q(z, x, w))
    return T


def m_of_chain_Q(T):
    return T[1][0] / T[0][0]


def cauchy_pick_Q(xs, ws, ys):
    """P_ij = sum_a w_a / ((x_a-y_i)(x_a-y_j)).  Source Cauchy kernel."""
    n = len(ys)
    P = [[Fr(0) for _ in range(n)] for _ in range(n)]
    for x, w in zip(xs, ws):
        d = [x - y for y in ys]
        for i in range(n):
            for j in range(n):
                P[i][j] += w / (d[i] * d[j])
    return P


def prime_blocks_Q(labeled, z):
    """labeled = list of (p, r, x, w), source order.
    Returns (product_p Theta_p, dict p -> Theta_p)."""
    by_p = OrderedDict()
    for p, r, x, w in labeled:
        by_p.setdefault(p, []).append((x, w))
    tot = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    blocks = OrderedDict()
    for p, atoms in by_p.items():
        Tp = chain_product_Q(atoms, z)
        blocks[p] = Tp
        tot = matmul2_Q(tot, Tp)
    return tot, blocks


def s0_from_cauchy_pi_Q(xs, ws, ys):
    """Lagrange S0 = Delta^{-1} (C Pi W Pi C^T) Delta^{-1}.
    pi(x)=prod (x-y), Delta=diag(pi'(y)).  No T0, no eig."""
    nY, nX = len(ys), len(xs)
    C = [[Fr(1) / (xs[a] - ys[i]) for a in range(nX)]
         for i in range(nY)]
    pi_X = [B.P_Y_Q(x, ys) for x in xs]
    pi_pr = []
    for j, yj in enumerate(ys):
        pr = Fr(1)
        for k, yk in enumerate(ys):
            if k != j:
                pr *= (yj - yk)
        pi_pr.append(pr)
    Pi = B.fr_diag(pi_X)
    W = B.fr_diag(ws)
    import borodin_dual_hole_probe as BDH
    Wpi = BDH.fr_mul(Pi, BDH.fr_mul(W, Pi))
    PXpi = BDH.fr_mul(C, BDH.fr_mul(Wpi, B.fr_T(C)))
    Di = B.fr_diag([Fr(1) / p for p in pi_pr])
    return BDH.fr_mul(Di, BDH.fr_mul(PXpi, Di))


# ---------- toys / windows (measurement, not constructors) ----------
def prime_toy():
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    labels = [(2, 1), (2, 2), (3, 1), (5, 1), ("inf", 0)]
    return xs, u, ud, iX, iY, d0, labels


def dressed_ITT_Q(xs, ud, iX, iY, d0):
    S0, kdim = B.S0_Q(xs, ud, iX, iY, d0, kind="mono")
    wY = [ud[i] for i in iY]
    D0 = B.fr_sub(B.fr_diag(wY), S0)
    sY = [B.fr_sqrt_pos(w) for w in wY]
    n = len(wY)
    ITT = [[D0[i][j] / (sY[i] * sY[j]) for j in range(n)]
           for i in range(n)]
    return S0, D0, ITT, kdim, wY


def cauchy_pick_f64(xX, wX, ys):
    C = 1.0 / (np.asarray(xX)[None, :] - np.asarray(ys)[:, None])
    return (C * np.asarray(wX)[None, :]) @ C.T


def factor_PP(n):
    n = int(n)
    if n < 2:
        return 1, 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            r = 0
            while n % p == 0:
                n //= p
                r += 1
            return (p, r) if n == 1 else (1, 0)
        p += 1 if p == 2 else 2
    return n, 1


def window_pick_row(kz):
    mz = V.build_measures(kz)
    g = B.pack_graph(mz)
    PX = cauchy_pick_f64(g["xp"], g["wX"], g["yn"])
    nPX, evPX = nneg_sym(PX, 1e-12)
    nITT, evITT = nneg_sym(np.eye(len(g["yn"])) - g["TT"], 1e-12)
    return dict(g=g, mz=mz, nPX=nPX, nITT=nITT,
                evPX0=float(evPX[0]), evITT0=float(evITT[0]))


def prime_lags_p(alpha, M, D, p_only):
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1e-14, side="right"))
    c = np.zeros(M)
    for u_j, m_j, n in zip(V.U[:ka], V.W_VM[:ka], V.PP[:ka]):
        pp, _r = factor_PP(int(n))
        if pp != p_only:
            continue
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= m_j * 0.5 * v
    return c


def fold_c(c, L):
    d = V.spectral_density(c)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    return x, wt


def lag_local_nneg(mz, g, p_only):
    """Diagnostic: interpolant of fold(c^P_p), not a constructor."""
    alpha, M, L, _Nw, D = V.window_shape(9)
    c = prime_lags_p(alpha, M, D, p_only)
    xf, wt = fold_c(c, L)
    o = np.argsort(xf)
    xs, ws = xf[o], wt[o]
    xu = np.asarray(mz["xu"], float)
    ud, *_ = B.BDH.dual_weights(xu, np.abs(mz["wu"]),
                               int(mz["S"]), int(mz["L"]))
    iY = np.searchsorted(xu, g["yn"])
    iX = np.searchsorted(xu, g["xp"])
    scale = np.abs(ws) / (np.abs(mz["wu"]) + 1e-300)
    wXloc = ud[iX] * scale[iX]
    wYloc = ud[iY] * scale[iY]
    mX = wXloc > 1e-18
    mY = wYloc > 1e-18
    T = B.source_T0_cls(g["xp"][mX], wXloc[mX],
                        g["yn"][mY], wYloc[mY], g["d0"])
    return nneg_sym(np.eye(T.shape[1]) - T.T @ T, 1e-10)[0]


# ---------- parts ----------
def part_satz():
    section("S1  LEG A -- REDHEFFER / CAUCHY-PI / GATE 3 OVER Q")
    xs, u, ud, iX, iY, d0, labels = prime_toy()
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    labeled_X = [(labels[i][0], labels[i][1], xs[i], ud[i]) for i in iX]
    tot, blocks = prime_blocks_Q(labeled_X, Z_TEST)
    m_prod = m_of_chain_Q(tot)
    m_sum = sum(ud[i] / (xs[i] - Z_TEST) for i in iX)
    check("G1-redheffer-equals-cauchy-Q",
          m_prod == m_sum == M_TOY,
          "m=%s at z=7/3" % m_prod)
    tot2 = chain_product_Q(list(zip(xX, wX)), Z_TEST)
    check("G2-product-p-equals-tot-Q",
          tot == tot2 and set(blocks) == {2, "inf"},
          "Theta_2 star Theta_inf = tot; p=3,5 are Y-only")
    S0pi = s0_from_cauchy_pi_Q(xX, wX, ys)
    S0k0, D0k0, ITTk0, k0, _wY = dressed_ITT_Q(xs, ud, iX, iY, 2)
    check("G3-cauchy-pi-S0-Q",
          k0 == 0 and S0pi == S0k0,
          "S0 = Delta^{-1} PXpi Delta^{-1} at kdim=0")
    PX = cauchy_pick_Q(xX, wX, ys)
    innD, innP = inertia_fr(D0k0), inertia_fr(PX)
    check("G4-gate3-fail-Q",
          innD[1] == 1 and innP[1] == 0
          and D0k0[1][1] == D11_K0,
          "D0 nneg=1 (D11=%s) PX nneg=0 -- Pick(product) "
          "NOT congruent to I-T*T" % D11_K0)
    _S01, D01, ITT1, k1, _ = dressed_ITT_Q(xs, ud, iX, iY, d0)
    check("G5-kdim1-toy-PD",
          k1 == 1 and inertia_fr(D01)[1] == 0
          and inertia_fr(ITT1)[1] == 0,
          "r409 toy is PD; mismatch lives on the nneg=1 slice")
    return xs, ud, iX, iY, d0, PX, D0k0


def part_windows(smoke):
    section("S2  LEG B -- w9 + TWO WINDOWS: PICK vs GRAPHRESOLVENT")
    w9 = window_pick_row(9)
    g = w9["g"]
    check("G10-w9-graph-pin",
          W9_OP_LO <= g["opnorm"] <= W9_OP_HI and w9["nITT"] == 1
          and g["nneg"] == 1,
          "||T0||=%.5f nneg(I-TT)=%d" % (g["opnorm"], w9["nITT"]))
    check("G11-w9-gate3-fail",
          w9["nPX"] == 0 and w9["evPX0"] >= W9_PX_EMIN_LO
          and w9["nITT"] == 1 and w9["evITT0"] < 0,
          "PX nneg=0 evmin=%.3e; ITT nneg=1 evmin=%.3e"
          % (w9["evPX0"], w9["evITT0"]))
    if smoke:
        check("G12-extra-windows-smoke-skip", True,
              "kz15/kz18 deferred to full")
        return w9
    r15 = window_pick_row(15)
    r18 = window_pick_row(18)
    check("G12-kz15-kz18-gate3-fail",
          r15["nITT"] == 1 and r15["nPX"] == 0
          and r18["nITT"] == 1 and r18["nPX"] == 0
          and KZ15_OP_LO <= r15["g"]["opnorm"] <= KZ15_OP_HI
          and KZ18_OP_LO <= r18["g"]["opnorm"] <= KZ18_OP_HI,
          "kz15 ||T||=%.5f nITT/nPX %d/%d; kz18 ||T||=%.5f %d/%d"
          % (r15["g"]["opnorm"], r15["nITT"], r15["nPX"],
             r18["g"]["opnorm"], r18["nITT"], r18["nPX"]))
    return w9


def part_anatomy(w9, smoke):
    section("S3  LEG C -- INDEX ACCUMULATION / STOP RULE 3")
    g, mz = w9["g"], w9["mz"]
    alpha, M, L, _Nw, D = V.window_shape(9)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1e-14, side="right"))
    i_lag = np.clip(np.rint(V.U[:ka] / D).astype(int), 0, M - 1)
    x_pp = np.cos(2.0 * math.pi * np.clip(i_lag, 1, L // 2) / L)
    attr = []
    for y in g["yn"]:
        j = int(np.argmin(np.abs(x_pp - y)))
        p, r = factor_PP(int(V.PP[j]))
        attr.append((p, r))
    ord_idx = sorted(range(len(attr)),
                     key=lambda i: (attr[i][0], attr[i][1], i))
    piv = B.seq_innov(g["xp"], g["wX"], g["yn"][ord_idx],
                      g["wY"][ord_idx], g["d0"])
    nneg_p = int(np.sum(piv < 0))
    pmin = float(np.min(piv))
    check("G20-source-order-uvarov-no-neg",
          nneg_p == 0 and pmin >= SRC_PIV_MIN_LO,
          "nneg pivots=%d min=%.3e (defect is not a prime prefix)"
          % (nneg_p, pmin))
    if smoke:
        nn2 = lag_local_nneg(mz, g, 2)
        check("G21-lag-local-not-simpler-smoke",
              nn2 >= LAG_NNEG_LO,
              "p=2 lag-local nneg=%d >= %d (stop rule 3)"
              % (nn2, LAG_NNEG_LO))
        return
    nn2 = lag_local_nneg(mz, g, 2)
    nn3 = lag_local_nneg(mz, g, 3)
    nn5 = lag_local_nneg(mz, g, 5)
    check("G21-lag-local-not-simpler",
          nn2 >= LAG_NNEG_LO and nn3 >= LAG_NNEG_LO
          and nn5 >= LAG_NNEG_LO,
          "lag-local nneg p2/p3/p5 = %d/%d/%d vs full nneg=1 "
          "-- source product is NOT simpler"
          % (nn2, nn3, nn5))


def part_kills(w9, smoke):
    section("S4  LEG D -- PERMUTE / JITTER / SCRAMBLE / TWIN")
    mz, g = w9["mz"], w9["g"]
    mzP = P1.reweight(mz, "permute", 1000)
    gP = B.pack_graph(mzP)
    mzG = P1.reweight(mz, "gauss", 431)
    gG = B.pack_graph(mzG)
    mzS = HM.scramble_mz()
    gS = B.pack_graph(mzS)
    check("G30-kills-target-index",
          gP["nneg"] >= PERM_NNEG_LO and gS["nneg"] == SCR_NNEG
          and gG["nneg"] >= JIT_NNEG_LO,
          "PERM nneg=%d SCR nneg=%d JIT nneg=%d "
          "(I-T*T jumps; Euler product stays kappa=0)"
          % (gP["nneg"], gS["nneg"], gG["nneg"]))
    if smoke:
        check("G31-twin-smoke-skip", True, "twin deferred to full")
        return
    uuc, mmc = TR.base_comb(9)
    mzD = TR.build_world(9, uuc, mmc)
    gapsc = MF.local_gaps(uuc)
    u2c, m2c, _dn, _du = AKD.twin_rational(
        uuc, mmc, gapsc, mzD["D"], 1.0e-8)
    mzT = TR.build_world(9, u2c, m2c)
    gT = B.pack_graph(mzT)
    check("G31-twin-stable",
          gT["nneg"] == g["nneg"] == 1
          and abs(gT["opnorm"] - g["opnorm"]) <= FORMULA_HI,
          "TWIN nneg=%d ||T||=%.6f (MAIN %.6f)"
          % (gT["nneg"], gT["opnorm"], g["opnorm"]))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("source_potapov_probe -- "
          "PRIME.RDAGGER.SOURCE_POTAPOV_FACTOR.01 (round 431)")
    print("SPEC_SHA %s   (B %s / DI %s / HM %s / P1 %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], DI.SPEC_SHA[:16],
             HM.SPEC_SHA[:16], P1.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (w9 + kz15 + kz18 + lag-local + twin)"))
    print("=" * 78)

    section("S0  FIREWALL + TARGET_LEAK")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / DI %s / HM %s / P1 %s"
          % (B.SPEC_SHA[:8], DI.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], P1.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))
    leak = []
    for fn in CONSTRUCTORS:
        leak.extend(scope_audit(fn))
    check("G00d-constructor-no-target",
          leak == [],
          "elem_mass / chain / Cauchy / prime_blocks / Cauchy-pi "
          "clean (no eig/SVD/pack_C/Z_loc)"
          if not leak else "; ".join(leak))

    part_satz()
    w9 = part_windows(smoke)
    part_anatomy(w9, smoke)
    part_kills(w9, smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    verd = "SOURCE_FACTOR_NOT_FOUND"
    check("G40-verdict",
          prev_ok,
          verd + ": Redheffer=Cauchy SATZ; Pick(product) "
          "not congruent to I-T*T; one square is interpolant "
          "residual not an Euler factor.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("SOURCE POTAPOV %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("SOURCE POTAPOV FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
