#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""r431_audit_probe -- PRIME.RDAGGER.SOURCE_POTAPOV_FACTOR
adversarial focus-audit (round 431-AUDIT) of the sealed
verdict SOURCE_FACTOR_NOT_FOUND.

THE THREE QUESTIONS (reviewer DCCXCVII / DCCC).
  Q1  Strawman of the factor class?  R431 multiplies
      additive unipotent E(z;x,w)=[[1,0],[w/(x-z),1]],
      which commute and collapse to m_X.  Independently
      build (i) Blaschke-Potapov J-factors B_alpha with
      alpha from source (x,w) and prime-dependent
      generating vectors (non-commuting), (ii) the
      genuine 2x2 scattering Redheffer star.  Can THAT
      Pick carry a negative square, or does the
      Herglotz/J-contractive collapse hold for every
      source-pure positive-mass J-product?
  Q2  Independent number check of the R431 pins:
      Q-toy m_X(7/3)=-7471/22950, D0 inertia (1,1,0)
      with D0[1,1]=-1744/2025, P_X inertia (2,0,0);
      w9 lam_min(P_X)=8.677 and ind_-(I-T*T)=1;
      source-order Uvarov 0 negative pivots, min
      3.25e-7, vs r409 index-36; lag-local ind_-
      18/19/15 for p=2/3/5.
  Q3  Cauchy-pi S0 = Delta^{-1} C Pi W_X Pi C^T
      Delta^{-1} exact over Q, and the structure
      (negative square = interpolant residual W_Y-S0,
      not an Euler object) on a SECOND independent
      Q-window.

INDEPENDENCE.  Does not import source_potapov_probe.
Q-arithmetic, Cauchy-pi, Blaschke-Potapov, Redheffer
star, and Pick kernels are local.  Window objects
(toy_dual / pack_graph / seq_innov / S0_Q as a
named comparator) come from r409, the object under
measurement, not the audited constructor.

CALIBRATION.  Numbers recomputed in this probe
(2026-08-30).  Existing R431 artefacts are READ-ONLY.
FROZEN FROM THIS RUN:
  * Q-toy: m_X(7/3)=-7471/22950 EXACT; D0 inertia (1,1,0)
    with D0[1,1]=-1744/2025; P_X inertia (2,0,0).
    Cauchy-pi = Lagrange = r409 S0_Q at kdim=0.
  * BP (source alpha=x+i|w|, u=(2,x)): ||[B0,B1]||=5.561e-2;
    J-unitary on R 2.7e-16; product J-contractive at i
    (lam_min=4.125e-2); J-kernel Pick nneg=0
    (lam_min=4.679e-3); associated m Pick nneg=0.
    Unipotent Redheffer star = mass sum (residual 0).
    Star = chain product 6.0e-17.  Inverse-Blaschke of
    the Arch atom: J-kernel nneg=2, rel vs D0=0.777
    (S_1 is not the interpolant residual).
  * Second 6-node Q-window: Cauchy-pi=Lagrange; D0
    inertia (1,2,0); P_X (3,0,0); BP J-kernel nneg=0.
  * w9: lam_min(P_X)=8.67731; ind_-(I-T*T)=1;
    source-order Uvarov 0/104 min=3.248e-7;
    position-order 1 negative at index 36;
    lag-local ind_-=18/19/15 for p=2/3/5.

AUSGANG CONFIRMED (NOT_FOUND stands, including the
non-commutative check).  No RH claim.  No L* claim.
No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()

M_TOY = Fr(-7471, 22950)
D11_K0 = Fr(-1744, 2025)
Z_TEST = Fr(7, 3)
J22 = np.array([[1.0, 0.0], [0.0, -1.0]], float)
W9_PX_LO, W9_PX_HI = 8.67, 8.685
SRC_PIV_MIN_LO, SRC_PIV_MIN_HI = 1.0e-8, 5.0e-6
W9_SEQ_IDX = 36
LAG_NNEG = {2: 18, 3: 19, 5: 15}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


# ---------- firewall / independence ----------
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
    return (not bad), ("clean" if not bad else "; ".join(bad))


def imports_source_potapov():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if "source_potapov" in a.name:
                    hits.append(a.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            if "source_potapov" in node.module:
                hits.append(node.module)
    return hits


# ---------- Q linear algebra (local) ----------
def qmul(A, B):
    n, p, m = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(p))
             for j in range(m)] for i in range(n)]


def qT(A):
    return [list(c) for c in zip(*A)]


def qdiag(d):
    n = len(d)
    return [[d[i] if i == j else Fr(0) for j in range(n)]
            for i in range(n)]


def qsub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


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


def nneg_sym(A, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (np.asarray(A, float)
                                   + np.asarray(A, float).T))
    return int(np.sum(ev < -floor)), ev


# ---------- unipotent / Cauchy (local, Q) ----------
def elem_uni_Q(z, x, w):
    return [[Fr(1), Fr(0)], [w / (x - z), Fr(1)]]


def matmul2_Q(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def chain_uni_Q(atoms, z):
    T = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    for x, w in atoms:
        T = matmul2_Q(T, elem_uni_Q(z, x, w))
    return T


def pi_Y_Q(x, ys):
    p = Fr(1)
    for y in ys:
        p *= (x - y)
    return p


def cauchy_pick_Q(xs, ws, ys):
    n = len(ys)
    P = [[Fr(0) for _ in range(n)] for _ in range(n)]
    for x, w in zip(xs, ws):
        d = [x - y for y in ys]
        for i in range(n):
            for j in range(n):
                P[i][j] += w / (d[i] * d[j])
    return P


def cauchy_pi_S0_Q(xs, ws, ys):
    """S0 = Delta^{-1} C Pi W Pi C^T Delta^{-1}, local."""
    nY, nX = len(ys), len(xs)
    C = [[Fr(1) / (xs[a] - ys[i]) for a in range(nX)]
         for i in range(nY)]
    pi_X = [pi_Y_Q(x, ys) for x in xs]
    pi_pr = []
    for j, yj in enumerate(ys):
        pr = Fr(1)
        for k, yk in enumerate(ys):
            if k != j:
                pr *= (yj - yk)
        pi_pr.append(pr)
    Pi = qdiag(pi_X)
    W = qdiag(ws)
    Di = qdiag([Fr(1) / p for p in pi_pr])
    Wpi = qmul(Pi, qmul(W, Pi))
    PXpi = qmul(C, qmul(Wpi, qT(C)))
    return qmul(Di, qmul(PXpi, Di))


def lagrange_S0_Q(xs, ws, ys):
    nX, nY = len(xs), len(ys)
    L = []
    for x in xs:
        row = []
        for j, yj in enumerate(ys):
            num, den = Fr(1), Fr(1)
            for k, yk in enumerate(ys):
                if k == j:
                    continue
                num *= (x - yk)
                den *= (yj - yk)
            row.append(num / den)
        L.append(row)
    S = [[Fr(0) for _ in range(nY)] for _ in range(nY)]
    for a in range(nX):
        for i in range(nY):
            for j in range(nY):
                S[i][j] += ws[a] * L[a][i] * L[a][j]
    return S


def dual_weights_Q(xs, u):
    n = len(xs)
    Pprime = []
    for j, xj in enumerate(xs):
        pr = Fr(1)
        for k, xk in enumerate(xs):
            if k != j:
                pr *= (xj - xk)
        Pprime.append(pr)
    return [Fr(1) / (u[j] * Pprime[j] * Pprime[j]) for j in range(n)]


def second_toy():
    """Independent 6-node kdim=0 window, not the r409 five-atom toy."""
    xs = [Fr(-3, 2), Fr(-1), Fr(-1, 3), Fr(1, 5), Fr(2, 3), Fr(3, 2)]
    u = [Fr(1), Fr(4), Fr(9), Fr(16), Fr(25), Fr(36)]
    iX, iY = [0, 2, 5], [1, 3, 4]
    ud = dual_weights_Q(xs, u)
    return xs, ud, iX, iY


# ---------- Blaschke-Potapov / Redheffer (local, C) ----------
def j_proj(u):
    u = np.asarray(u, complex).reshape(2)
    ju = J22.astype(complex) @ u
    nrm = np.vdot(u, ju)
    if abs(nrm) < 1e-18:
        raise ValueError("J-neutral generating vector")
    return np.outer(u, np.conjugate(ju)) / nrm


def blaschke_hp(z, alpha, inverse=False):
    a = complex(alpha)
    z = complex(z)
    if inverse:
        return (z - np.conjugate(a)) / (z - a)
    return (z - a) / (z - np.conjugate(a))


def potapov_factor(z, alpha, u, inverse=False):
    P = j_proj(u)
    b = blaschke_hp(z, alpha, inverse=inverse)
    return np.eye(2, dtype=complex) + (b - 1.0) * P


def chain_potapov(atoms, z, inverse_mask=None):
    T = np.eye(2, dtype=complex)
    for i, (alpha, u) in enumerate(atoms):
        inv = bool(inverse_mask and inverse_mask[i])
        T = T @ potapov_factor(z, alpha, u, inverse=inv)
    return T


def source_bp_atoms(xX, wX):
    """Source-pure: alpha = x + i|w|, u = (2, x) so J-positive
    (4-x^2 >= 3 on [-1,1]) and directions differ with x."""
    atoms = []
    for x, w in zip(xX, wX):
        xf, wf = float(x), float(w)
        alpha = xf + 1j * abs(wf)
        u = np.array([2.0, xf], float)
        atoms.append((alpha, u))
    return atoms


def j_inner_resid(T):
    Th = T.conj().T
    M = Th @ J22.astype(complex) @ T - J22.astype(complex)
    return float(np.linalg.norm(M, "fro"))


def j_kernel_pick(atoms, zs, inverse_mask=None):
    """Hermitian Pick of the J-kernel of the product, sampled
    at zs subset C+.  Block 2x2, overall 2n x 2n."""
    n = len(zs)
    Thetas = [chain_potapov(atoms, z, inverse_mask) for z in zs]
    Jc = J22.astype(complex)
    K = np.zeros((2 * n, 2 * n), complex)
    for i, zi in enumerate(zs):
        for j, zj in enumerate(zs):
            den = -1j * (zi - np.conjugate(zj))
            blk = (Jc - Thetas[i] @ Jc @ Thetas[j].conj().T) / den
            K[2 * i:2 * i + 2, 2 * j:2 * j + 2] = blk
    H = 0.5 * (K + K.conj().T)
    return H


def associated_m(T):
    return T[1, 0] / T[0, 0]


def scalar_pick_m(atoms, ys, eps, inverse_mask=None):
    zs = [complex(float(y), eps) for y in ys]
    ms = [associated_m(chain_potapov(atoms, z, inverse_mask)) for z in zs]
    n = len(zs)
    P = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            P[i, j] = ((ms[i] - np.conjugate(ms[j]))
                       / (zs[i] - np.conjugate(zs[j])))
    return 0.5 * (P + P.conj().T)


def chain_to_scatter(T):
    """Homma port stacking: chain [a2; b1] = Theta [a1; b2]
    pairs with scattering [b1; b2] = S [a1; a2] and with
    the 2x2 Redheffer star used by r433.  Pivot is Theta11."""
    t11, t12 = T[0, 0], T[0, 1]
    t21, t22 = T[1, 0], T[1, 1]
    if abs(t11) < 1e-18:
        raise ZeroDivisionError("chain Theta11=0")
    inv = 1.0 / t11
    return np.array([[t21 * inv, t22 - t21 * inv * t12],
                     [inv, -inv * t12]], complex)


def scatter_to_chain(S):
    s11, s12 = S[0, 0], S[0, 1]
    s21, s22 = S[1, 0], S[1, 1]
    if abs(s21) < 1e-18:
        raise ZeroDivisionError("scatter S21=0")
    t11 = 1.0 / s21
    t12 = -s22 / s21
    t21 = s11 / s21
    t22 = s12 - s11 * s22 / s21
    return np.array([[t11, t12], [t21, t22]], complex)


def redheffer_star_2x2(S, T):
    """Scattering Redheffer star S star T (1x1 blocks)."""
    A, B, C, D = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    P, Q, R, Sblk = T[0, 0], T[0, 1], T[1, 0], T[1, 1]
    den = 1.0 - P * D
    if abs(den) < 1e-14:
        raise ZeroDivisionError("Redheffer pivot I-S22 T11 = 0")
    W = 1.0 / den
    A2 = A + B * W * P * C
    B2 = B * W * Q
    C2 = R * (1.0 / (1.0 - D * P)) * C
    D2 = Sblk + R * D * W * Q
    return np.array([[A2, B2], [C2, D2]], complex)


def redheffer_product(Thetas):
    S = chain_to_scatter(Thetas[0])
    for T in Thetas[1:]:
        S = redheffer_star_2x2(S, chain_to_scatter(T))
    return scatter_to_chain(S)


def j_contractive_at(T, z_unused=None):
    """J - Theta^* J Theta  ⪰  0  (J-contractive)."""
    Th = T.conj().T
    M = J22.astype(complex) - Th @ J22.astype(complex) @ T
    H = 0.5 * (M + M.conj().T)
    ev = np.linalg.eigvalsh(H.real)
    return float(ev[0]), ev


# ---------- window helpers (measurement, not R431 constructors) ----------
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
def part_q_numbers():
    section("Q1/Q2/Q3  Q-TOY NUMBERS + CAUCHY-PI (independent)")
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    wY = [ud[i] for i in iY]
    atoms = list(zip(xX, wX))
    tot = chain_uni_Q(atoms, Z_TEST)
    m_prod = tot[1][0] / tot[0][0]
    m_sum = sum(w / (x - Z_TEST) for x, w in atoms)
    E0 = elem_uni_Q(Z_TEST, xX[0], wX[0])
    E1 = elem_uni_Q(Z_TEST, xX[1], wX[1])
    comm = matmul2_Q(E0, E1) == matmul2_Q(E1, E0)
    check("A1-unipotent-commute-and-sum",
          comm and m_prod == m_sum == M_TOY,
          "m=%s commute=%s" % (m_prod, comm))
    S0pi = cauchy_pi_S0_Q(xX, wX, ys)
    S0lag = lagrange_S0_Q(xX, wX, ys)
    S0ref, kdim = B.S0_Q(xs, ud, iX, iY, 2, kind="mono")
    check("A2-cauchy-pi-equals-lagrange-and-S0_Q",
          S0pi == S0lag == S0ref and kdim == 0,
          "kdim=0 exact")
    D0 = qsub(qdiag(wY), S0pi)
    PX = cauchy_pick_Q(xX, wX, ys)
    innD, innP = inertia_fr(D0), inertia_fr(PX)
    check("A3-D0-PX-inertia-and-D11",
          innD == (1, 1, 0) and innP == (2, 0, 0)
          and D0[1][1] == D11_K0,
          "D0 %s D11=%s PX %s" % (innD, D0[1][1], innP))
    return xs, ud, iX, iY, xX, wX, ys, wY, D0, PX


def part_noncommutative(xX, wX, ys, D0):
    section("Q1  NON-COMMUTING BLASCHKE-POTAPOV + REDHEFFER STAR")
    atoms = source_bp_atoms(xX, wX)
    z0 = 1j
    B0 = potapov_factor(z0, atoms[0][0], atoms[0][1])
    B1 = potapov_factor(z0, atoms[1][0], atoms[1][1])
    comm_res = float(np.linalg.norm(B0 @ B1 - B1 @ B0, "fro"))
    check("B1-factors-do-not-commute",
          comm_res > 1e-6,
          "||B0 B1 - B1 B0||=%.3e" % comm_res)
    resid_real = []
    for z in (-0.7, 0.13, 0.8):
        T = potapov_factor(z, atoms[0][0], atoms[0][1])
        resid_real.append(j_inner_resid(T))
    check("B2-J-unitary-on-the-line",
          max(resid_real) < 1e-10,
          "max ||Theta^* J Theta - J||=%.3e" % max(resid_real))
    evmin_c, _ = j_contractive_at(chain_potapov(atoms, z0))
    check("B3-product-J-contractive-in-C+",
          evmin_c >= -1e-10,
          "lam_min(J-Theta^* J Theta)=%.3e at z=i" % evmin_c)
    zs = [complex(float(y), 0.11) for y in ys]
    H = j_kernel_pick(atoms, zs)
    nnegH, evH = nneg_sym(H.real, 1e-10)
    check("B4-J-kernel-Pick-PD",
          nnegH == 0 and float(evH[0]) > 0,
          "inertia nneg=%d lam_min=%.3e (2n=%d)"
          % (nnegH, float(evH[0]), H.shape[0]))
    Pm = scalar_pick_m(atoms, ys, 0.11)
    nnegM, evM = nneg_sym(Pm.real, 1e-10)
    check("B5-associated-m-Pick-PD",
          nnegM == 0 and float(evM[0]) > 0,
          "scalar Pick nneg=%d lam_min=%.3e" % (nnegM, float(evM[0])))
    z_r = Fr(1, 3)
    m0 = float(wX[0] / (xX[0] - z_r))
    m1 = float(wX[1] / (xX[1] - z_r))
    U0 = np.array([[1.0, 0.0], [m0, 1.0]], complex)
    U1 = np.array([[1.0, 0.0], [m1, 1.0]], complex)
    Ustar = redheffer_product([U0, U1])
    Usum = np.array([[1.0, 0.0], [m0 + m1, 1.0]], complex)
    uni_res = float(np.linalg.norm(Ustar - Usum, "fro"))
    check("B6-unipotent-Redheffer-is-mass-sum",
          uni_res < 1e-12,
          "star residual %.3e (genuine star still abelian)" % uni_res)
    Thetas = [potapov_factor(z0, a, u) for a, u in atoms]
    T_chain = Thetas[0]
    for T in Thetas[1:]:
        T_chain = T_chain @ T
    T_star = redheffer_product(Thetas)
    star_res = float(np.linalg.norm(T_chain - T_star, "fro"))
    check("B7-Redheffer-star-equals-chain-product",
          star_res < 1e-10,
          "||chain-star||=%.3e at z=i" % star_res)
    # inverse-Blaschke of the Arch atom (last): S_1, not positive-mass
    mask = [False] * (len(atoms) - 1) + [True]
    Hinv = j_kernel_pick(atoms, zs, inverse_mask=mask)
    nnegI, evI = nneg_sym(Hinv.real, 1e-10)
    D0f = np.array([[float(D0[i][j]) for j in range(len(D0))]
                    for i in range(len(D0))], float)
    PmI = scalar_pick_m(atoms, ys, 0.11, inverse_mask=mask)
    # 2x2 D0 vs 2x2 scalar Pick: not a scalar multiple
    a = PmI.real.reshape(-1)
    b = D0f.reshape(-1)
    # best least-squares scale
    scale = float(np.dot(a, b) / (np.dot(a, a) + 1e-30))
    rel = float(np.linalg.norm(b - scale * a)
                / (np.linalg.norm(b) + 1e-30))
    check("B8-inverse-Blaschke-not-the-residual",
          nnegI >= 1 and rel > 0.05,
          "S1 nneg=%d lam_min=%.3e; rel-mismatch vs D0=%.3f"
          % (nnegI, float(evI[0]), rel))
    return nnegH, nnegI, rel, comm_res


def part_second_window():
    section("Q3  SECOND Q-WINDOW: residual, not Euler")
    xs, ud, iX, iY = second_toy()
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    wY = [ud[i] for i in iY]
    S0pi = cauchy_pi_S0_Q(xX, wX, ys)
    S0lag = lagrange_S0_Q(xX, wX, ys)
    check("C1-second-window-cauchy-pi",
          S0pi == S0lag,
          "6-node kdim=0 Cauchy-pi = Lagrange")
    D0 = qsub(qdiag(wY), S0pi)
    PX = cauchy_pick_Q(xX, wX, ys)
    innD, innP = inertia_fr(D0), inertia_fr(PX)
    check("C2-second-window-structure",
          innD[1] >= 1 and innP[1] == 0,
          "D0 inertia %s (has a negative square); P_X inertia %s (PD)"
          % (innD, innP))
    # BP product on this window still PD
    atoms = source_bp_atoms(xX, wX)
    zs = [complex(float(y), 0.11) for y in ys]
    H = j_kernel_pick(atoms, zs)
    nnegH, evH = nneg_sym(H.real, 1e-10)
    check("C3-second-window-BP-still-PD",
          nnegH == 0,
          "BP J-kernel nneg=%d lam_min=%.3e" % (nnegH, float(evH[0])))
    return innD, innP


def part_w9(smoke):
    section("Q2  w9 NUMBERS + ANATOMY")
    mz = V.build_measures(9)
    g = B.pack_graph(mz)
    PX = cauchy_pick_f64(g["xp"], g["wX"], g["yn"])
    nPX, evPX = nneg_sym(PX, 1e-12)
    nITT, evITT = nneg_sym(np.eye(len(g["yn"])) - g["TT"], 1e-12)
    check("D1-w9-PX-and-ITT",
          nPX == 0 and nITT == 1
          and W9_PX_LO <= float(evPX[0]) <= W9_PX_HI
          and float(evITT[0]) < 0,
          "lam_min(P_X)=%.5f nPX=%d; ind_-(I-TT)=%d lam=%.3e"
          % (float(evPX[0]), nPX, nITT, float(evITT[0])))
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
    piv_src = B.seq_innov(g["xp"], g["wX"], g["yn"][ord_idx],
                          g["wY"][ord_idx], g["d0"])
    nneg_src = int(np.sum(piv_src < 0))
    pmin = float(np.min(piv_src))
    check("D2-source-order-Uvarov",
          nneg_src == 0
          and SRC_PIV_MIN_LO <= pmin <= SRC_PIV_MIN_HI,
          "nneg=0/%d min=%.3e" % (len(piv_src), pmin))
    piv_pos = B.seq_innov(g["xp"], g["wX"], g["yn"], g["wY"], g["d0"])
    ineg = np.where(piv_pos < 0)[0]
    check("D3-position-order-index-36",
          len(ineg) == 1 and int(ineg[0]) == W9_SEQ_IDX,
          "nneg=%d at index %s" % (len(ineg),
                                  int(ineg[0]) if len(ineg) else None))
    if smoke:
        nn2 = lag_local_nneg(mz, g, 2)
        check("D4-lag-local-p2-smoke",
              nn2 == LAG_NNEG[2],
              "p=2 ind_-=%d (full 2/3/5 deferred)" % nn2)
        return dict(evPX0=float(evPX[0]), nITT=nITT, pmin=pmin,
                    nneg_src=nneg_src, lag=None)
    lag = {}
    for p in (2, 3, 5):
        lag[p] = lag_local_nneg(mz, g, p)
    check("D4-lag-local-2-3-5",
          lag[2] == LAG_NNEG[2] and lag[3] == LAG_NNEG[3]
          and lag[5] == LAG_NNEG[5],
          "ind_- p2/p3/p5=%d/%d/%d" % (lag[2], lag[3], lag[5]))
    # BP on a 4-node Y-sample of w9 (full |Y|~104 is 208x208, fine,
    # but 4 nodes already test the class; keep smoke-budget)
    ys4 = g["yn"][:: max(1, len(g["yn"]) // 4)][:4]
    atoms = source_bp_atoms(g["xp"][:8], g["wX"][:8])
    zs = [complex(float(y), 0.11) for y in ys4]
    H = j_kernel_pick(atoms, zs)
    nnegH, evH = nneg_sym(H.real, 1e-9)
    check("D5-w9-BP-prefix-J-kernel-PD",
          nnegH == 0,
          "8 source BP factors, 4 Y-nodes: nneg=%d lam_min=%.3e"
          % (nnegH, float(evH[0])))
    return dict(evPX0=float(evPX[0]), nITT=nITT, pmin=pmin,
                nneg_src=nneg_src, lag=lag)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("r431_audit_probe -- adversarial audit of "
          "SOURCE_FACTOR_NOT_FOUND")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL + INDEPENDENCE")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    leak = imports_source_potapov()
    check("G00b-no-import-source-potapov",
          leak == [],
          "independent constructors"
          if not leak else "; ".join(leak))

    _xs, _ud, _iX, _iY, xX, wX, ys, _wY, D0, _PX = part_q_numbers()
    nnegH, nnegI, rel, comm_res = part_noncommutative(xX, wX, ys, D0)
    innD2, innP2 = part_second_window()
    w9 = part_w9(smoke)

    section("S5  VERDICT")
    q_ok = all(ok for n, ok in CHECKS if n.startswith("A"))
    nc_ok = all(ok for n, ok in CHECKS
                if n.startswith("B") and n != "B8-inverse-Blaschke-not-the-residual")
    # B8 is extra anatomy; Q1 is about POSITIVE-mass factors (B1-B7)
    w_ok = all(ok for n, ok in CHECKS if n.startswith("D") or n.startswith("C"))
    pos_mass_pd = (nnegH == 0)
    numbers_ok = q_ok and w_ok
    if not numbers_ok:
        verd = "NUMBERS_BUG"
    elif (not nc_ok) or (not pos_mass_pd):
        verd = "STRAWMAN"
    else:
        verd = "CONFIRMED"
    prev = all(ok for _n, ok in CHECKS)
    check("G40-verdict",
          prev and verd == "CONFIRMED",
          "%s: positive-mass J-products stay kappa=0 "
          "(non-commuting BP + Redheffer star); "
          "R431 numbers reproduced; residual is W_Y-S0.  "
          "no RH / L* / R-dagger" % verd)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    print("  Q1 non-commute ||[B0,B1]||=%.3e  J-kernel nneg=%d  "
          "S1-vs-D0 rel=%.3f" % (comm_res, nnegH, rel))
    print("  Q2 lam_min(P_X)=%.5f  nITT=%d  src-Uvarov min=%.3e"
          % (w9["evPX0"], w9["nITT"], w9["pmin"]))
    print("  Q3 second-window D0 %s  P_X %s" % (innD2, innP2))
    if n_fail == 0:
        print("R431 AUDIT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("R431 AUDIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
