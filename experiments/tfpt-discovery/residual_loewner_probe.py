#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""residual_loewner_probe --
PRIME.RDAGGER.INTERPOLATION_RESIDUAL_LOEWNER_BEZOUT.01
(round 439, reviewer DCCCIV, one discovery round):
is the interpolant residual D0 = W_Y - S0 a
Loewner/Bezout object, so that its inertia is
zero-structure of a rational pair rather than a
norm?

THE OBJECT.  D0 lives on the hole nodes Y at
interpolating depth d0 (pack_graph / r409).  At
kdim = d0-|Y| = 0 the Cauchy-pi formula of r431
gives S0 = Delta^{-1} C Pi W_X Pi C^T Delta^{-1}
and the one negative square of the bulk sits in
D0.  This round asks whether D0 is Loewner/Bezout.

LEGS (binding order).
  L1  Displacement gate rank(Y D0 - D0 Y) <= 2
      with Y = diag(y_i).  Exact over Q on the two
      r431 toys (5-atom kdim=0 and the 6-node
      window); mpmath on w9 + kz15 + kz18.  No
      tolerance rank: sigma_3,4,... must be true
      zeros (ratio sigma_3/sigma_2).
  L2  Off-diagonal reconstruction
      (y_i-y_j)(D0)_ij = f(y_i)-f(y_j) (consistency
      over all pairs).  Diagonal: D0_ii = f'(y_i)
      OR D0 = L_f + diag(Delta) -- THE OLD TRAP
      (displacement-2 determines only the
      off-diagonal; the wall was Loewner PLUS a
      source-side diagonal).  Delta is a named
      source object.  SATZ: S0 = K_{YY}^{-1} with
      K the RKHS kernel of P_<d0> on the X-measure
      (exact over Q); at kdim=0 additionally
      Delta D0 Delta = L_{-m-tilde} + diag(w_Y (P_Y')^2)
      with m-tilde(z) = sum_X w pi_Y(x)^2 / (x-z)
      the Cauchy-pi generating function.
  B1  Bezout congruence D0 = S^T Bez(P_Y, Q_k) S
      with Q_k from the Birkhoff/interpolation formula
      (numerator of a P_Y-denominator continuation
      rational).  NEVER from eigendata of D0.
  B2  If B1: CInd_R(Q/P_Y) = ind_-(D0) and the
      worlds census in zero language.
  Edge (small): if B1, last Sturm pivot vs
      delta = 1-q^dagger (r433).  Measurement only.

CALIBRATION DISCLOSURE.  Displacement rank, ones-
Loewner residual, dressed identity, S0 = K^{-1},
Bezout-congruence miss, residue signs, and the
window sigma_3/sigma_2 first measured in /tmp
(r439_cal.py, r439_cal2.py, r439_cal3.py,
r439_cal4_sturm.py) on the r409/r431 constructors,
2026-08-30.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall of the three
windows + chi + kills is pack_graph (r409), < 60 s.

FROZEN FROM /tmp (live re-gated, not fitted):
  * 5-atom kdim=0: rank(disp)=2 EXACT; Cauchy-pi;
    S0 = K_YY^{-1} EXACT; Delta D0 Delta =
    L_{-m-tilde} + diag(w Delta^2) EXACT; D0 inertia
    (1,1,0) D11=-1744/2025; ones-Loewner residual of
    D0 is 0 (nY=2, one pair); poly-extension L_f has
    nneg=0 while diag(Delta) has nneg=1 (the old
    trap, nY=2 only).  Residue signs of m-tilde/P'
    = [+1,-1] = nneg(D0).
  * 6-node kdim=0: rank(disp)=2 EXACT; ones-Loewner
    residual of D0 = 40073273/275164890 != 0 (D0
    is NOT classical ones-Loewner); S0 = K^{-1}
    EXACT; dressed identity EXACT; D0 inertia
    (1,2,0); L_{-m-tilde} nneg=3 (ND), diag(w Delta^2)
    nneg=0 (PD); residue signs [-1,+1,-1] nneg=2
    matches D0.
  * B1: three source Q (poly-part of P_Y m_X,
    P' m_X, interpolant of m-tilde) -- none gives
    D0 = S^T Bez(P_Y,Q) S for S in {V^{-1},
    Delta^{-1} V^{-1}, V, Delta^{-1}}.  CD pair of
    P_<d0> represents K, not D0.  Last Sturm
    constant of (P_Y, Q_m-tilde) on the 5-atom is
    -7466971/10681442 != 187/450 = 1-q^dagger.
  * w9: n=104 d0=181 kdim=77 nneg(D0)=1 ||T||=1.08014;
    numpy/mpmath sigma_3/sigma_2 = 9.42e-15;
    S0 vs K_YY^{-1} rel 1.05e-12; ones-res of D0
    0.011 (not Loewner); nneg_res(m-tilde/P')=52
    != nneg(D0)=1.  kz15: 1.08e-14 nneg=1.
    kz18: 4.41e-15 nneg=1.
  * PERM nneg=20; JITTER 19; SCRAMBLE 21.
    CHI3-9 nneg=0; CHI3-15 nneg=1.
    Displacement rank 2 SURVIVES the kills
    (sigma_3/sigma_2 < 1e-13).

AUSGANG RESIDUAL_LOEWNER_PLUS_CONTROLLED_DIAGONAL.
SATZ: displacement rank 2; S0 = K_YY^{-1};
kdim=0 dressed Loewner of -m-tilde plus the source
diagonal w_Y (P_Y')^2.  B1 FAIL for Bez(P_Y, Q):
the Cauchy-pi rational is m-artig with P_X poles,
not P_Y.  P1 problem: nneg(W_Y - K_YY^{-1}) <= 1.
Does not move the mincut.  No RH claim.

MACHINERY: r409 B.S0_Q / toy_dual / pack_graph /
chebV / fr_*; r431 S.cauchy-pi / prime_toy /
dressed_ITT_Q; r431-audit A.second_toy; r403 P1
reweight; r398 HM scramble / chi_mz; r226 V
build_measures.

NO RH CLAIM.  Finite identities, a named Bezout
miss, a named P1 problem.  Research documentation,
not a theorem of RH.  No L* claim.  No R-dagger
claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import r431_audit_probe as A  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
P1_SHA_PREFIX = "ba6817f5"
HM_SHA_PREFIX = "bb1dcf6a"

D11_K0 = Fr(-1744, 2025)
ONES_RES_6 = Fr(40073273, 275164890)
STURM_LAST_5 = Fr(-7466971, 10681442)
QDAG_TOY = Fr(187, 450)
W9_OP_LO, W9_OP_HI = 1.05, 1.12
KZ15_OP_LO, KZ15_OP_HI = 1.09, 1.13
KZ18_OP_LO, KZ18_OP_HI = 1.20, 1.30
RATIO_HI = 1.0e-12
KINV_REL = 1.0e-9
PERM_NNEG_LO, SCR_NNEG, JIT_NNEG_LO = 15, 21, 2
CHI3_9_NNEG, CHI3_15_NNEG = 0, 1
W9_NNEG_RES_LO, W9_NNEG_RES_HI = 40, 70

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("kernel_YY_Q", "m_tilde_Q", "m_tilde_prime_Q",
                "loewner_Q", "Q_nodal_mtilde")


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
    return (not bad), ("NO zero/prime oracles; Cauchy-pi / "
                       "K_YY / displacement / Loewner only"
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
              "chain_C", "pack_graph", "r_nm3", "aug_rung"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def qdiag(d):
    n = len(d)
    return [[d[i] if i == j else Fr(0) for j in range(n)]
            for i in range(n)]


def qmul(A, B):
    n, p, m = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(p))
             for j in range(m)] for i in range(n)]


def qT(A):
    return [list(c) for c in zip(*A)]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j]
               for i in range(len(A)) for j in range(len(A)))


def mat_maxabs(A, B):
    m = Fr(0)
    for i in range(len(A)):
        for j in range(len(A)):
            d = A[i][j] - B[i][j]
            if d < 0:
                d = -d
            if d > m:
                m = d
    return m


def pi_pr_Q(ys):
    out = []
    for j, yj in enumerate(ys):
        pr = Fr(1)
        for k, yk in enumerate(ys):
            if k != j:
                pr *= (yj - yk)
        out.append(pr)
    return out


def disp_Q(D, ys):
    n = len(ys)
    return [[(ys[i] - ys[j]) * D[i][j] for j in range(n)]
            for i in range(n)]


def ones_loewner_residual(D, ys):
    n = len(ys)
    f = [(ys[i] - ys[0]) * D[i][0] for i in range(n)]
    res = Fr(0)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = (f[i] - f[j]) - (ys[i] - ys[j]) * D[i][j]
            if d < 0:
                d = -d
            if d > res:
                res = d
    return f, res


def poly_loewner_diag(ys, fvals):
    n = len(ys)
    pr = pi_pr_Q(ys)
    qp = []
    for i in range(n):
        ell_i_p = sum((Fr(1) / (ys[i] - ys[k]))
                     for k in range(n) if k != i)
        s = fvals[i] * ell_i_p
        for j in range(n):
            if j == i:
                continue
            s += fvals[j] * (pr[i] / ((ys[i] - ys[j]) * pr[j]))
        qp.append(s)
    return qp


# ---------- source-pure constructors (AST-audited) ----------
def kernel_YY_Q(xX, wX, ys, d0):
    """RKHS kernel of P_<d0> on the X-measure, at Y.
    Monomial basis.  Only (x,w,Y,d0).  No D0, no eig."""
    G = [[Fr(0) for _ in range(d0)] for _ in range(d0)]
    for x, w in zip(xX, wX):
        xa = [Fr(1)]
        for _ in range(d0 - 1):
            xa.append(xa[-1] * x)
        for a in range(d0):
            for b in range(d0):
                G[a][b] += w * xa[a] * xa[b]
    Gi = BDH.fr_inv(G)
    PhiY = []
    for y in ys:
        row = [Fr(1)]
        for _ in range(d0 - 1):
            row.append(row[-1] * y)
        PhiY.append(row)
    return qmul(PhiY, qmul(Gi, qT(PhiY)))


def m_tilde_Q(xX, wX, ys, z):
    """Cauchy-pi generating function.  Only (x,w,Y,z)."""
    s = Fr(0)
    for x, w in zip(xX, wX):
        pi = B.P_Y_Q(x, ys)
        s += (pi * pi * w) / (x - z)
    return s


def m_tilde_prime_Q(xX, wX, ys, z):
    s = Fr(0)
    for x, w in zip(xX, wX):
        pi = B.P_Y_Q(x, ys)
        s += (pi * pi * w) / ((x - z) * (x - z))
    return s


def loewner_Q(ys, fvals, fprimes):
    n = len(ys)
    L = [[Fr(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][i] = fprimes[i]
            else:
                L[i][j] = (fvals[i] - fvals[j]) / (ys[i] - ys[j])
    return L


def Q_nodal_mtilde(xX, wX, ys):
    """Source Q: nodal values of m-tilde at Y (Lagrange
    interpolant of the Cauchy-pi generator).  No eig(D0)."""
    return [m_tilde_Q(xX, wX, ys, y) for y in ys]


def poly_coeffs_from_nodes(ys, vals):
    n = len(ys)
    V = [[ys[a] ** i for i in range(n)] for a in range(n)]
    c = BDH.fr_mul(BDH.fr_inv(V), [[v] for v in vals])
    return [row[0] for row in c]


def P_Y_coeffs(ys):
    c = [Fr(1)]
    for y in ys:
        nc = [Fr(0)] * (len(c) + 1)
        for i, a in enumerate(c):
            nc[i] -= a * y
            nc[i + 1] += a
        c = nc
    return c


def bezout_from_generating(P_coeff, Q_coeff):
    n = len(P_coeff) - 1
    Qc = Q_coeff + [Fr(0)] * (n + 1 - len(Q_coeff))

    def peval(coeff, t):
        s, p = Fr(0), Fr(1)
        for c in coeff:
            s += c * p
            p *= t
        return s

    def pder(coeff, t):
        s, dp = Fr(0), Fr(1)
        for k, c in enumerate(coeff):
            if k == 0:
                continue
            s += Fr(k) * c * dp
            dp *= t
        return s

    xs = [Fr(k) for k in range(n)]
    G = [[Fr(0) for _ in range(n)] for _ in range(n)]
    for a, x in enumerate(xs):
        for b, y in enumerate(xs):
            px, py = peval(P_coeff, x), peval(P_coeff, y)
            qx, qy = peval(Qc, x), peval(Qc, y)
            if x == y:
                G[a][b] = pder(P_coeff, x) * qy - px * pder(Qc, x)
            else:
                G[a][b] = (px * qy - py * qx) / (x - y)
    V = [[xs[a] ** i for i in range(n)] for a in range(n)]
    Vi = BDH.fr_inv(V)
    return qmul(Vi, qmul(G, qT(Vi)))


def toy_bundle(xs, ud, iX, iY, d0):
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    ys = [xs[i] for i in iY]
    wY = [ud[i] for i in iY]
    S0, kdim = B.S0_Q(xs, ud, iX, iY, d0, kind="mono")
    D0 = B.fr_sub(qdiag(wY), S0)
    return dict(xX=xX, wX=wX, ys=ys, wY=wY, S0=S0, D0=D0,
                kdim=kdim, pr=pi_pr_Q(ys))


def poly_divmod(a, b):
    a, b = list(a), list(b)
    while a and a[-1] == 0:
        a.pop()
    while b and b[-1] == 0:
        b.pop()
    if not b:
        raise ZeroDivisionError("sturm")
    q = [Fr(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        k = len(a) - len(b)
        f = a[-1] / b[-1]
        q[k] = f
        for i, c in enumerate(b):
            a[i + k] -= f * c
        while a and a[-1] == 0:
            a.pop()
    return q, a


def sturm_last_const(P, Q):
    chain = [list(P), list(Q)]
    while True:
        _q, r = poly_divmod(chain[-2], chain[-1])
        if not r or all(c == 0 for c in r):
            last = chain[-1]
            return last[0] if last else Fr(0)
        chain.append([-c for c in r])


def kernel_YY_f64(xp, wX, yn, d0):
    PhiX = B.chebV(xp, d0)
    PhiY = B.chebV(yn, d0)
    sX = np.sqrt(np.maximum(wX, 0.0))
    G = (sX[:, None] * PhiX).T @ (sX[:, None] * PhiX)
    return PhiY @ np.linalg.pinv(G, rcond=1e-14) @ PhiY.T


def svd_ratio_mp(D, ys, dps=40):
    import mpmath as mp
    mp.mp.dps = dps
    n = len(ys)
    A = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            A[i, j] = (mp.mpf(str(ys[i])) - mp.mpf(str(ys[j])))
            A[i, j] *= mp.mpf(str(D[i, j]))
    AtA = A.T * A
    ev = mp.eigsy(AtA, eigvals_only=True)
    ev = sorted([mp.fabs(e) for e in ev], reverse=True)
    sig = [mp.sqrt(e) for e in ev]
    return sig


# ---------- parts ----------
def part_toys():
    section("S1  L1/L2 OVER Q -- 5-ATOM + 6-NODE")
    xs, u, ud, iX, iY, d0, _lab = S.prime_toy()
    t5 = toy_bundle(xs, ud, iX, iY, 2)
    disp5 = disp_Q(t5["D0"], t5["ys"])
    check("G01-5atom-disp-rank-2",
          B.fr_rank(disp5) == 2 and t5["kdim"] == 0,
          "rank(Y D0-D0 Y)=2 EXACT; kdim=0")
    S0pi = S.s0_from_cauchy_pi_Q(t5["xX"], t5["wX"], t5["ys"])
    check("G02-5atom-cauchy-pi",
          mat_eq(t5["S0"], S0pi),
          "S0 = Delta^{-1} C Pi W Pi C^T Delta^{-1}")
    K5 = kernel_YY_Q(t5["xX"], t5["wX"], t5["ys"], 2)
    Kinv5 = BDH.fr_inv(K5)
    check("G03-5atom-S0-is-Kinv",
          mat_eq(t5["S0"], Kinv5),
          "S0 = K_YY^{-1} EXACT (RKHS of P_<d0> on X)")
    mt = [m_tilde_Q(t5["xX"], t5["wX"], t5["ys"], y) for y in t5["ys"]]
    mtp = [m_tilde_prime_Q(t5["xX"], t5["wX"], t5["ys"], y)
           for y in t5["ys"]]
    Lm = loewner_Q(t5["ys"], mt, mtp)
    Lnm = [[-a for a in row] for row in Lm]
    dshift = [t5["wY"][i] * t5["pr"][i] * t5["pr"][i]
              for i in range(len(t5["ys"]))]
    dD0d = [[t5["D0"][i][j] * t5["pr"][i] * t5["pr"][j]
             for j in range(len(t5["ys"]))]
            for i in range(len(t5["ys"]))]
    rhs = B.fr_add(Lnm, qdiag(dshift))
    check("G04-5atom-dressed-loewner",
          mat_eq(dD0d, rhs)
          and S.inertia_fr(Lnm)[1] == 2
          and S.inertia_fr(qdiag(dshift))[1] == 0,
          "Delta D0 Delta = L_{-m-tilde} + diag(w (P')^2); "
          "L ND, diag PD")
    inn5 = S.inertia_fr(t5["D0"])
    check("G05-5atom-inertia",
          inn5 == (1, 1, 0) and t5["D0"][1][1] == D11_K0,
          "D0 inertia (1,1,0) D11=%s" % D11_K0)
    f5, res5 = ones_loewner_residual(t5["D0"], t5["ys"])
    qp5 = poly_loewner_diag(t5["ys"], f5)
    Delta5 = [t5["D0"][i][i] - qp5[i] for i in range(2)]
    Lf5 = loewner_Q(t5["ys"], f5, qp5)
    check("G06-5atom-old-trap",
          res5 == 0 and Delta5[0] != 0 and Delta5[1] != 0
          and S.inertia_fr(Lf5)[1] == 0
          and S.inertia_fr(qdiag(Delta5))[1] == 1,
          "nY=2: ones-Loewner res=0, L_f nneg=0, "
          "diag(Delta) carries nneg=1 (old trap)")

    xs2, ud2, iX2, iY2 = A.second_toy()
    t6 = toy_bundle(xs2, ud2, iX2, iY2, 3)
    disp6 = disp_Q(t6["D0"], t6["ys"])
    f6, res6 = ones_loewner_residual(t6["D0"], t6["ys"])
    check("G10-6node-disp-rank-2",
          B.fr_rank(disp6) == 2 and t6["kdim"] == 0,
          "rank=2 EXACT on the second Q-window")
    check("G11-6node-not-ones-loewner",
          res6 == ONES_RES_6 and res6 != 0,
          "ones-Loewner residual %s != 0 (nY=3)" % res6)
    K6 = kernel_YY_Q(t6["xX"], t6["wX"], t6["ys"], 3)
    Kinv6 = BDH.fr_inv(K6)
    mt6 = [m_tilde_Q(t6["xX"], t6["wX"], t6["ys"], y) for y in t6["ys"]]
    mtp6 = [m_tilde_prime_Q(t6["xX"], t6["wX"], t6["ys"], y)
            for y in t6["ys"]]
    Lm6 = loewner_Q(t6["ys"], mt6, mtp6)
    Lnm6 = [[-a for a in row] for row in Lm6]
    dsh6 = [t6["wY"][i] * t6["pr"][i] * t6["pr"][i]
            for i in range(3)]
    dD6 = [[t6["D0"][i][j] * t6["pr"][i] * t6["pr"][j]
            for j in range(3)] for i in range(3)]
    rhs6 = B.fr_add(Lnm6, qdiag(dsh6))
    check("G12-6node-S0-Kinv-dressed",
          mat_eq(t6["S0"], Kinv6) and mat_eq(dD6, rhs6)
          and S.inertia_fr(Lnm6)[1] == 3
          and S.inertia_fr(qdiag(dsh6))[1] == 0,
          "S0=K^{-1}; dressed Loewner EXACT; L nneg=3, "
          "diag nneg=0")
    check("G13-6node-inertia",
          S.inertia_fr(t6["D0"]) == (1, 2, 0),
          "D0 inertia (1,2,0) -- kdim=0 residual")
    return t5, t6


def part_bezout(t5, t6):
    section("S2  B1 -- BEZOUT CONGRUENCE OF (P_Y, Q)")
    miss = []
    for tag, t in (("5atom", t5), ("6node", t6)):
        Pc = P_Y_coeffs(t["ys"])
        qy = Q_nodal_mtilde(t["xX"], t["wX"], t["ys"])
        Qc = poly_coeffs_from_nodes(t["ys"], qy)
        Bez = bezout_from_generating(Pc, Qc)
        n = len(t["ys"])
        V = [[t["ys"][a] ** i for i in range(n)] for a in range(n)]
        Vi = BDH.fr_inv(V)
        Di = qdiag([Fr(1) / p for p in t["pr"]])
        M1 = qmul(qT(Vi), qmul(Bez, Vi))
        M2 = qmul(Di, qmul(M1, Di))
        M3 = qmul(V, qmul(Bez, qT(V)))
        diffs = (mat_maxabs(M1, t["D0"]), mat_maxabs(M2, t["D0"]),
                 mat_maxabs(M3, t["D0"]))
        miss.append((tag, diffs, S.inertia_fr(Bez)))
    ok = all(all(d != 0 for d in diffs) for _t, diffs, _i in miss)
    check("G20-B1-bezout-not-D0",
          ok,
          "Q=interp(m-tilde) source-first; no S in "
          "{V^{-1}, Delta^{-1}V^{-1}, V} gives D0 "
          "(5atom diffs %s; 6node %s; Bez inertia %s/%s)"
          % (miss[0][1], miss[1][1], miss[0][2], miss[1][2]))
    P5 = P_Y_coeffs(t5["ys"])
    q5 = Q_nodal_mtilde(t5["xX"], t5["wX"], t5["ys"])
    last = sturm_last_const(P5, poly_coeffs_from_nodes(t5["ys"], q5))
    check("G21-edge-sturm-not-qdag",
          last == STURM_LAST_5 and last != QDAG_TOY,
          "last Sturm of (P_Y, Q_m-tilde)=%s != 1-q^d=%s "
          "(B1 not met; R437 not opened)" % (last, QDAG_TOY))
    return miss


def window_row(kz):
    mz = V.build_measures(kz)
    g = B.pack_graph(mz)
    D = np.asarray(g["D0"], float)
    ys = np.asarray(g["yn"], float)
    wY = np.asarray(g["wY"], float)
    n = len(ys)
    disp = (ys[:, None] - ys[None, :]) * D
    sig = np.linalg.svd(disp, compute_uv=False)
    ratio = float(sig[2] / sig[1]) if n > 2 and sig[1] > 0 else 0.0
    S0 = np.diag(wY) - D
    K = kernel_YY_f64(g["xp"], g["wX"], ys, g["d0"])
    Kinv = np.linalg.pinv(K, rcond=1e-14)
    rel = float(np.linalg.norm(S0 - Kinv)
                / (np.linalg.norm(S0) + 1e-30))
    nneg = S.nneg_sym(D, 1e-10)[0]
    pr = np.array([np.prod(ys[i] - np.delete(ys, i)) for i in range(n)])
    piX = np.array([np.prod(x - ys) for x in g["xp"]])
    c = (piX ** 2) * np.asarray(g["wX"], float)
    C = 1.0 / (np.asarray(g["xp"])[None, :] - ys[:, None])
    mt = C @ c
    nneg_res = int(np.sum((mt / pr) < 0))
    return dict(g=g, mz=mz, n=n, d0=g["d0"], nneg=nneg,
                op=g["opnorm"], ratio=ratio, sig=sig, rel=rel,
                nneg_res=nneg_res, D=D, ys=ys)


def part_windows(smoke):
    section("S3  WINDOWS -- DISPLACEMENT + K^{-1}")
    w9 = window_row(9)
    check("G30-w9-disp-ratio",
          w9["nneg"] == 1
          and W9_OP_LO <= w9["op"] <= W9_OP_HI
          and w9["ratio"] < RATIO_HI,
          "nneg=1 ||T||=%.5f sigma3/sigma2=%.3e (n=%d d0=%d kdim=%d)"
          % (w9["op"], w9["ratio"], w9["n"], w9["d0"],
             w9["d0"] - w9["n"]))
    check("G31-w9-S0-Kinv",
          w9["rel"] < KINV_REL,
          "S0 vs K_YY^{-1} rel=%.3e" % w9["rel"])
    check("G32-w9-CInd-not-nneg",
          W9_NNEG_RES_LO <= w9["nneg_res"] <= W9_NNEG_RES_HI
          and w9["nneg_res"] != w9["nneg"],
          "nneg_res(m-tilde/P')=%d != nneg(D0)=1 -- CInd of "
          "the kdim=0 interpolant is NOT P1 on windows"
          % w9["nneg_res"])
    if smoke:
        check("G33-extra-windows-smoke-skip", True,
              "kz15/kz18 + mpmath deferred to full")
        return w9
    r15 = window_row(15)
    r18 = window_row(18)
    check("G33-kz15-kz18-disp",
          r15["nneg"] == 1 and r18["nneg"] == 1
          and r15["ratio"] < RATIO_HI and r18["ratio"] < RATIO_HI
          and KZ15_OP_LO <= r15["op"] <= KZ15_OP_HI
          and KZ18_OP_LO <= r18["op"] <= KZ18_OP_HI,
          "kz15 ||T||=%.5f s3/s2=%.3e; kz18 ||T||=%.5f s3/s2=%.3e"
          % (r15["op"], r15["ratio"], r18["op"], r18["ratio"]))
    sig = svd_ratio_mp(w9["D"], w9["ys"], dps=40)
    mp_ratio = float(sig[2] / sig[1])
    check("G34-w9-mpmath-sigma",
          mp_ratio < RATIO_HI and float(sig[2]) < 1e-12,
          "mpmath dps40 sigma=[%.5f, %.5f, %.3e, ...] "
          "s3/s2=%.3e (true zeros after the pair)"
          % (float(sig[0]), float(sig[1]), float(sig[2]), mp_ratio))
    return w9


def part_kills(w9, smoke):
    section("S4  KILLS / CHI CENSUS")
    if smoke:
        check("G40-kills-smoke-skip", True, "permute/scramble/chi deferred")
        return
    mz, g = w9["mz"], w9["g"]
    mzP = P1.reweight(mz, "permute", 1000)
    gP = B.pack_graph(mzP)
    mzG = P1.reweight(mz, "gauss", 431)
    gG = B.pack_graph(mzG)
    mzS = HM.scramble_mz()
    gS = B.pack_graph(mzS)
    check("G40-kills-nneg",
          gP["nneg"] >= PERM_NNEG_LO and gS["nneg"] == SCR_NNEG
          and gG["nneg"] >= JIT_NNEG_LO,
          "PERM nneg=%d SCR nneg=%d JIT nneg=%d "
          "(P1 count jumps; displacement rank stays 2)"
          % (gP["nneg"], gS["nneg"], gG["nneg"]))
    ysP = np.asarray(gP["yn"], float)
    DP = np.asarray(gP["D0"], float)
    sigP = np.linalg.svd((ysP[:, None] - ysP[None, :]) * DP,
                         compute_uv=False)
    check("G41-kills-disp-stays-2",
          float(sigP[2] / sigP[1]) < 1e-12,
          "PERM still sigma3/sigma2=%.3e -- rank-2 is "
          "structural, not MAIN-specific" % (sigP[2] / sigP[1]))
    mz3 = HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)
    mz15 = HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    g3 = B.pack_graph(mz3)
    g15 = B.pack_graph(mz15)
    check("G42-chi-census",
          g3["nneg"] == CHI3_9_NNEG and g15["nneg"] == CHI3_15_NNEG,
          "CHI3-9 nneg=%d (PD, world-separating); "
          "CHI3-15 nneg=%d (one square lives)"
          % (g3["nneg"], g15["nneg"]))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("residual_loewner_probe -- "
          "PRIME.RDAGGER.INTERPOLATION_RESIDUAL_LOEWNER_BEZOUT.01 "
          "(round 439)")
    print("SPEC_SHA %s   (B %s / P1 %s / HM %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], P1.SPEC_SHA[:16],
             HM.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (w9 + kz15 + kz18 + mpmath + kills + chi)"))
    print("=" * 78)

    section("S0  FIREWALL + TARGET_LEAK")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / P1 %s / HM %s"
          % (B.SPEC_SHA[:8], P1.SPEC_SHA[:8], HM.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))
    leak = []
    for fn in CONSTRUCTORS:
        leak.extend(scope_audit(fn))
    check("G00d-constructor-no-target",
          leak == [],
          "K_YY / m-tilde / Loewner / Q_nodal clean "
          "(no eig/SVD/pack_C/pack_graph)"
          if not leak else "; ".join(leak))

    t5, t6 = part_toys()
    part_bezout(t5, t6)
    w9 = part_windows(smoke)
    part_kills(w9, smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    verd = "RESIDUAL_LOEWNER_PLUS_CONTROLLED_DIAGONAL"
    check("G60-verdict",
          prev_ok,
          verd + ": disp rank 2 SATZ; S0=K_YY^{-1} SATZ; "
          "kdim=0 dressed Loewner + source diag SATZ; "
          "B1 Bez(P_Y,Q) FAIL.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("RESIDUAL LOEWNER %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("RESIDUAL LOEWNER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
