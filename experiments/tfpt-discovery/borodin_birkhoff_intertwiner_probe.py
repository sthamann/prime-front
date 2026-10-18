#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""borodin_birkhoff_intertwiner_probe --
PRIME.RDAGGER.BORODIN_BIRKHOFF_INTERTWINER.01 (round 409;
reviewer "R407", our R409 because R407/R408 are taken):
is the r356 dual resolvent exactly the graph resolvent of
the source-pure minimal Birkhoff extension, and is the
r369 Haynsworth matrix the Uvarov innovation precision?

THE CORRECTED NORTH STAR (DCCLXXIV).  R404/R405 stopped
because the implicit intertwiner was the identity: Euler/
Digamma Grams were compared to A0 without the dual quotient.
R407 found R = C(I+C)^{-1} with C = T*T in the dual OP
basis (w9 residual 1.8e-14).  This round lifts that
dictionary to a Jacobi-free source formula for the
operator T0 itself.

SOURCE FORMULA.  T0 is the min-norm interpolant
Y -> X in P_<d0, d0 = N_w-3:
    T0 = (I - Pi_K) W_X^{1/2} L W_Y^{-1/2}
(Lagrange L on Y, kernel K = P_Y * phi, weighted projector
Pi_K).  Algebraically equivalent KKT: min ||W_X^{1/2} Phi_X c||
s.t. Phi_Y c = v.  Stable evaluation is Chebyshev CLS
(Lagrange+P_Y is Q-exact and catastrophically ill-conditioned
at working depth).  Then
    R_graph = (I + T0* T0)^{-1} = R_{N-3},
    T0* T0 = R^{-1} - I = C^{-1},
    In(I - T0* T0) = In(A0) = In(D0),
    D0 = W_Y - S0 congruent to I - T0* T0.
No R, A0, eigenvector, or target Cholesky in the constructor.

LEGS (algebra first, then census).
  A  Quotient + graph SATZ over Q; three bases; dim ker.
  B  Source formula vs r407 chain and r356 dual OP; inertia
     on w9, kz15/18/42/130, chi, scramble.
  C  Uvarov Woodbury over Q; sequential innovations;
     Theta_terminal vs C^T Phi_N C (main gate).
  D  Euler/Digamma through T0; Krein vs positive Gram.
  E  Source-ordered Uvarov n_neg^inn vs ind_-(A0); <=1 on MAIN.
  F  T^dagger from the REAL border functional lambda_B
     (no virtual node); T^dagger* T^dagger = (R^dagger)^{-1}-I;
     six terminal-dead chi must flip (||T^dagger||>1).

CALIBRATION DISCLOSURE.  Graph residuals, inertia table,
SEQ pivots, T^dagger assembly, dead-chi ||T^dagger||, Krein
miss, Phi-vs-Schur miss first measured in /tmp (r409_cal.py,
r409_cal2.py, r409_cal3.py, r409_cal4.py, r409_cal5.py) on
the same constructors, 2026-08-29.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall < 30 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: three bases (mono/Newton/Chebyshev) give
    identical S0; ker dim = d0-|Y|; u^vee=1/u and d0+/-1
    break; dressed (W+S0)^{-1} equals the dual CD Gram.
  * w9: ||R_graph - R_chain|| = 2.16e-14; ||T0||=1.08014;
    nneg(I-TT)=nneg(A0)=nneg(D0)=1; SEQ nneg=1 at index 36
    (value -0.5117); Pi_K=0 residual 28.5; Euler-on-Y vs
    A0 residual 282 (R404 order ~209).
  * Worlds (graph=R, inertia): kz15 ||T||=1.107 nneg=1;
    kz18 1.250 nneg=1; kz42 1.000 nneg=0; kz130 1.000
    nneg=0 rest 1.0e-12; chi3-9 0.99956 nneg=0; chi3-15
    1.00092 nneg=1; scramble 16.66 nneg=21; permute 7.42
    nneg=20.  SEQ nneg <= 1 on core-42 (CENSUS); equals
    nA0 on 32/42 MAIN (not SATZ); scramble 12 vs 21;
    permute SEQ vs nA0 also splits.  chi3 live/dead
    nneg(I-TT)<=1.
  * T^dagger assembly vs r362 Z-I rest 7.4e-14, vs R^dagger
    2.2e-14, ||T^dagger||=0.999917 on MAIN.  Six dead chi
    all lamRd<1/2 so ||T^dagger||>1.
  * Krein/Euler unfitted miss (rel 3-6, align ~0); positive
    Gram excluded (nneg=0, rel 5.6).  Phi 3x3 is NOT the
    pair+border Schur of Z-I (ev mismatch).
  * Weight-gauss jitter: algebra rest 1.6e-14, nneg 1->20.

AUSGANG ONE_DEFECT_TRANSPORT_CENSUS.
SATZ: graph identity, source formula, three-basis Q,
inertia dictionary, T^dagger = r362 graph factor, dead-chi
operator flip.  CENSUS: n_neg^inn <= 1 on MAIN (core-42
42/42; SEQ = ind_-(A0) only 32/42).  REFUTED:
unfitted Krein; literal Theta = C^T Phi C; SEQ nneg =
ind_-(A0) as identity; CLS+lambda_B without the r362 lift.
Does not close R^dagger as a new theorem (uses the r362
Gram).  Does not move the mincut.  No RH claim.

MACHINERY: r407 D.pack_C / chain_C (independent control);
r356 BDH.dual_weights / dual_rung / fr_inv; r362 ABD
bvec_chunked / aug_rung / virtual_star_census; r367 HM
r_nm3 / scramble / chi; r403 P1.reweight; r369 mixed Phi
shape (not a new matrix); r401 sch (control); r404 OG
euler_F; r226 V; r406 Lean woodbury_inv (cited, not rerun).

NO RH CLAIM.  Finite identities, one named census, named
refutations.  Research documentation, not a theorem of RH.
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
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_dual_hole_probe as BDH  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import one_defect_gram_probe as OG  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402

BDH_SHA_PREFIX = "36141c0a"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
DMF_SHA_PREFIX = "4bf1a94b"
OG_SHA_PREFIX = "c0260053"
DI_SHA_PREFIX = "2ee74c59"
ABD_SHA_PREFIX = "7d810a9a"

FORMULA_HI = 1.0e-8
INERTIA_MATCH = True
W9_OP_LO, W9_OP_HI = 1.05, 1.12
W9_SEQ_IDX, W9_SEQ_VAL = 36, -0.5117
W9_SEQ_VAL_TOL = 0.02
PI0_LO = 5.0
EULER_A0_LO = 50.0
PERM_NNEG_LO, SCR_NNEG = 15, 21
CHI9_NNEG, CHI15_NNEG = 0, 1
TDAG_MAIN_HI = 1.0
TDAG_REL_HI = 1.0e-8
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
CORE_N = 42
SAMPLE_EXT = HM.SAMPLE_EXT
KREIN_ALIGN_HI = 0.05
PHI_EV_MISMATCH_LO = 0.05
VIRT_SPREAD_LO = 1.0
JITTER_NNEG_LO = 2

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("chebV", "source_T0_cls", "source_Tdag",
                "S0_Q", "lagrange_row_Q")


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
    return (not bad), ("NO zero/prime oracles; Birkhoff CLS / "
                       "dual weights / graph resolvent"
                       if not bad else "; ".join(bad))


def scope_audit(funcname):
    """TARGET_LEAK: constructors must not read A0/R/D0/eigs
    of the target, nor Cholesky of G_+."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"eigvalsh", "eigh", "cholesky", "pack_C", "chain_C",
              "r_nm3", "aug_rung"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def relres(A, B):
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    return float(np.linalg.norm(A - B)) / (float(np.linalg.norm(B)) + 1e-30)


def nneg_sym(A, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (np.asarray(A, float)
                                   + np.asarray(A, float).T))
    return int(np.sum(ev < -floor)), ev


# ---------- Q helpers (Leg A) ----------
def cheb_Q(x, n):
    out, t0, t1 = [], Fr(1), x
    for k in range(n):
        if k == 0:
            out.append(t0)
        elif k == 1:
            out.append(t1)
        else:
            t0, t1 = t1, 2 * x * t1 - t0
            out.append(t1)
    return out


def newton_Q(x, cents):
    p, out = Fr(1), []
    for c in cents:
        out.append(p)
        p = p * (x - c)
    return out


def mono_Q(x, n):
    p, out = Fr(1), []
    for _ in range(n):
        out.append(p)
        p = p * x
    return out


def P_Y_Q(x, ys):
    p = Fr(1)
    for y in ys:
        p *= (x - y)
    return p


def lagrange_row_Q(x, ys):
    n, row = len(ys), []
    for j in range(n):
        num, den = Fr(1), Fr(1)
        for k in range(n):
            if k == j:
                continue
            num *= (x - ys[k])
            den *= (ys[j] - ys[k])
        row.append(num / den)
    return row


def basis_row_Q(x, n, kind, cents):
    if kind == "mono":
        return mono_Q(x, n)
    if kind == "newton":
        return newton_Q(x, cents)
    if kind == "cheb":
        return cheb_Q(x, n)
    raise ValueError(kind)


def fr_T(A):
    return [list(c) for c in zip(*A)]


def fr_sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def fr_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def fr_eye(n):
    return [[Fr(1) if i == j else Fr(0) for j in range(n)]
            for i in range(n)]


def fr_diag(d):
    n = len(d)
    return [[d[i] if i == j else Fr(0) for j in range(n)]
            for i in range(n)]


def fr_sqrt_pos(x):
    a, b = x.numerator, x.denominator
    sa, sb = int(round(a ** 0.5)), int(round(b ** 0.5))
    if sa * sa != a or sb * sb != b:
        raise ValueError("not a square: %s" % x)
    return Fr(sa, sb)


def S0_Q(xs, ud, iX, iY, d0, kind="mono"):
    """Schur-short-circuit Gram.  No R/A0/eig/Cholesky."""
    ys = [xs[i] for i in iY]
    xX = [xs[i] for i in iX]
    wX = [ud[i] for i in iX]
    nX, nY = len(iX), len(iY)
    kdim = d0 - nY
    L = [lagrange_row_Q(x, ys) for x in xX]
    WL = [[wX[i] * L[i][j] for j in range(nY)] for i in range(nX)]
    Slag = BDH.fr_mul(fr_T(L), WL)
    if kdim <= 0:
        return Slag, kdim
    cents = xX[:max(kdim, 1)]
    Phi = [basis_row_Q(x, kdim, kind, cents) for x in xX]
    PY = [P_Y_Q(x, ys) for x in xX]
    K = [[PY[i] * Phi[i][a] for a in range(kdim)] for i in range(nX)]
    WK = [[wX[i] * K[i][a] for a in range(kdim)] for i in range(nX)]
    A = BDH.fr_mul(fr_T(K), WK)
    B = BDH.fr_mul(fr_T(K), WL)
    Ai = BDH.fr_inv(A)
    corr = BDH.fr_mul(fr_T(B), BDH.fr_mul(Ai, B))
    return fr_sub(Slag, corr), kdim


def hankel_dual_R_Q(xs, ud, iY, d0):
    nY = len(iY)
    Phi = [mono_Q(xs[i], d0) for i in range(len(xs))]
    G = [[Fr(0) for _ in range(d0)] for _ in range(d0)]
    for i, u in enumerate(ud):
        ph = Phi[i]
        for a in range(d0):
            for b in range(d0):
                G[a][b] += u * ph[a] * ph[b]
    Gi = BDH.fr_inv(G)
    sY = [fr_sqrt_pos(ud[i]) for i in iY]
    A = [[sY[r] * Phi[iY[r]][c] for c in range(d0)]
         for r in range(nY)]
    return BDH.fr_mul(A, BDH.fr_mul(Gi, fr_T(A)))


def C_plus_Q(xs, ud, iX, iY, d0):
    nY = len(iY)
    PhiY = [mono_Q(xs[i], d0) for i in iY]
    PhiX = [mono_Q(xs[i], d0) for i in iX]
    Gp = [[Fr(0) for _ in range(d0)] for _ in range(d0)]
    for r, i in enumerate(iX):
        ph, u = PhiX[r], ud[i]
        for a in range(d0):
            for b in range(d0):
                Gp[a][b] += u * ph[a] * ph[b]
    Gpi = BDH.fr_inv(Gp)
    sY = [fr_sqrt_pos(ud[i]) for i in iY]
    A = [[sY[r] * PhiY[r][c] for c in range(d0)]
         for r in range(nY)]
    return BDH.fr_mul(A, BDH.fr_mul(Gpi, fr_T(A)))


def R_from_C_Q(C):
    IC = fr_add(fr_eye(len(C)), C)
    return BDH.fr_mul(C, BDH.fr_inv(IC))


def fr_rank(M):
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    r, used = 0, [False] * m
    for col in range(n):
        piv = next((i for i in range(m)
                    if (not used[i]) and A[i][col] != 0), None)
        if piv is None:
            continue
        used[piv] = True
        pv = A[piv][col]
        A[piv] = [t / pv for t in A[piv]]
        for i in range(m):
            if i != piv and A[i][col] != 0:
                f = A[i][col]
                A[i] = [a - f * b for a, b in zip(A[i], A[piv])]
        r += 1
    return r


def toy_dual():
    xs = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    u = [Fr(4), Fr(9), Fr(1), Fr(16), Fr(25)]
    iX, iY = [0, 1, 4], [2, 3]
    Pprime = []
    for j, xj in enumerate(xs):
        pr = Fr(1)
        for k, xk in enumerate(xs):
            if k != j:
                pr *= (xj - xk)
        Pprime.append(pr)
    ud = [Fr(1) / (u[j] * Pprime[j] * Pprime[j]) for j in range(5)]
    return xs, u, ud, iX, iY, 3


# ---------- f64 CLS constructor (Leg B) ----------
def chebV(x, n):
    x = np.asarray(x, float)
    V = np.empty((len(x), n), float)
    if n <= 0:
        return V
    V[:, 0] = 1.0
    if n > 1:
        V[:, 1] = x
    for k in range(1, n - 1):
        V[:, k + 1] = 2.0 * x * V[:, k] - V[:, k - 1]
    return V


def source_T0_cls(xp, wX, yn, wY, d0, extra=None, extra_w=1.0):
    """Min-norm interpolant in P_<d0.  extra = ell_B adds a
    Birkhoff functional.  NO R, A0, eig, Cholesky."""
    xp = np.asarray(xp, float)
    yn = np.asarray(yn, float)
    wX = np.asarray(wX, float)
    wY = np.asarray(wY, float)
    nY = len(yn)
    sX = np.sqrt(np.maximum(wX, 0.0))
    sY = np.sqrt(np.maximum(wY, 0.0))
    PhiX = chebV(xp, d0)
    PhiY = chebV(yn, d0)
    PhiW = sX[:, None] * PhiX
    nC = nY + (1 if extra is not None else 0)
    G = PhiW.T @ PhiW
    KKT = np.zeros((d0 + nC, d0 + nC))
    KKT[:d0, :d0] = G
    KKT[:d0, d0:d0 + nY] = PhiY.T
    KKT[d0:d0 + nY, :d0] = PhiY
    rhs = np.zeros((d0 + nC, nC))
    rhs[d0:d0 + nY, :nY] = np.diag(1.0 / np.maximum(sY, 1e-300))
    if extra is not None:
        ell = np.asarray(extra, float).reshape(-1)
        KKT[:d0, d0 + nY] = ell
        KKT[d0 + nY, :d0] = ell
        rhs[d0 + nY, nY] = 1.0 / float(extra_w)
    sol = np.linalg.solve(KKT, rhs)
    return PhiW @ sol[:d0, :]


def dual_split(mz):
    xu = np.asarray(mz["xu"], float)
    wu = np.asarray(mz["wu"], float)
    ud, *_ = BDH.dual_weights(xu, np.abs(wu), int(mz["S"]), int(mz["L"]))
    yn = np.asarray(mz["yn"], float)
    xp = np.asarray(mz["xp"], float)
    iY = np.searchsorted(xu, yn)
    iP = np.searchsorted(xu, xp)
    return xp, ud[iP], yn, ud[iY], ud


def pack_graph(mz, d0=None):
    xp, wX, yn, wY, ud = dual_split(mz)
    d0 = int(mz["Nw"]) - 3 if d0 is None else int(d0)
    T = source_T0_cls(xp, wX, yn, wY, d0)
    TT = 0.5 * (T.T @ T + (T.T @ T).T)
    n = TT.shape[0]
    Rg = np.linalg.solve(np.eye(n) + TT, np.eye(n))
    Rg = 0.5 * (Rg + Rg.T)
    sY = np.sqrt(np.maximum(wY, 0.0))
    D0 = (sY[:, None] * (np.eye(n) - TT)) * sY[None, :]
    return dict(T0=T, TT=TT, Rg=Rg, D0=D0, d0=d0, xp=xp, wX=wX,
                yn=yn, wY=wY, ud=ud,
                opnorm=float(np.linalg.norm(T, 2)),
                nneg=nneg_sym(np.eye(n) - TT)[0])


def seq_innov(xp, wX, yn, wY, d0):
    """Growing-Y last-Schur of D_m (Uvarov, not LDL of D0)."""
    nY = len(yn)
    piv = np.zeros(nY)
    for m in range(1, nY + 1):
        T = source_T0_cls(xp, wX, yn[:m], wY[:m], d0)
        TT = T.T @ T
        s = np.sqrt(np.maximum(wY[:m], 0.0))
        Dm = (s[:, None] * (np.eye(m) - TT)) * s[None, :]
        if m == 1:
            piv[0] = float(Dm[0, 0])
        else:
            A = Dm[:-1, :-1]
            b = Dm[:-1, -1]
            piv[m - 1] = float(Dm[-1, -1] - b @ np.linalg.solve(A, b))
    return piv


def source_Tdag(mz, dsm, Bm=None):
    """T^dagger: unaugmented T0 (d0=Nw-1) plus min-norm lift of
    the REAL border image vt and the Y-vanishing lambda_B
    kernel column, scaled to the r362 gamma.  No virtual node."""
    xp, wX, yn, wY, ud = dual_split(mz)
    d0 = int(mz["Nw"]) - 1
    j1, j2 = PX.pair_select(yn)
    D9 = BDH.dual_rung(mz["xu"], mz["wu"], yn, mz["vn"],
                       int(mz["Nw"]), int(mz["S"]), int(mz["L"]),
                       j1, j2, B=Bm)
    bp = ABD.border_chain_pack(mz["xp"], mz["wp"], yn, mz["vn"],
                              dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"],
                              int(mz["Nw"]))
    a_mu, b_mu, h0 = V.mu_chain(mz["xp"], mz["wp"], int(mz["Nw"]))
    bxa = np.concatenate([np.asarray(dsm["xs"], float),
                          np.asarray(dsm["ys"], float)])
    bwa = np.concatenate([np.asarray(dsm["ws"], float),
                          -np.asarray(dsm["vs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0, bxa, bwa, int(mz["Nw"]))
    beta = bvec / math.sqrt(bp["Bw"])
    gam = float(beta @ beta)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0, yn, mz["vn"], int(mz["Nw"]))
    vt = D9["eps"][D9["iY"]] * (Bm @ beta)
    T0 = source_T0_cls(xp, wX, yn, wY, d0)
    TT = T0.T @ T0
    u_min = T0 @ np.linalg.solve(TT, vt)
    ellB = chebV(bxa, d0).T @ bwa
    k = source_T0_cls(xp, wX, yn, wY, d0, extra=ellB, extra_w=1.0)[:, -1]
    need = gam - float(u_min @ u_min)
    alpha = math.sqrt(max(need, 0.0) / max(float(k @ k), 1e-30))
    Tdag = np.column_stack([T0, u_min + alpha * k])
    Rm = D9["Rm"]
    Sm = len(vt)
    ZI = np.zeros((Sm + 1, Sm + 1))
    ZI[:Sm, :Sm] = np.linalg.inv(Rm) - np.eye(Sm)
    ZI[:Sm, Sm] = vt
    ZI[Sm, :Sm] = vt
    ZI[Sm, Sm] = gam
    Rdag = np.linalg.inv(ZI + np.eye(Sm + 1))
    Rdag = 0.5 * (Rdag + Rdag.T)
    spread = ABD.virtual_star_census(a_mu, b_mu, bvec)
    return dict(Tdag=Tdag, ZI=ZI, Rdag=Rdag, gam=gam, vt=vt,
                opnorm=float(np.linalg.norm(Tdag, 2)),
                spread=float(spread),
                bvec=bvec, a_mu=a_mu, b_mu=b_mu, Bm=Bm,
                j1=j1, j2=j2)


def chi_border_rung(kz, q, lpq):
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    dsm = dict(xs=mzb["xp"], ws=mzb["wp"],
               ys=mzb["yn"], vs=mzb["vn"])
    return mzc, dsm


# ---------- parts ----------
def part_satz():
    section("S1  LEG A -- QUOTIENT / GRAPH / THREE BASES OVER Q")
    xs, u, ud, iX, iY, d0 = toy_dual()
    S0s = {}
    for kind in ("mono", "newton", "cheb"):
        S0s[kind], kdim = S0_Q(xs, ud, iX, iY, d0, kind=kind)
    check("G01-three-basis-S0-Q",
          S0s["mono"] == S0s["newton"] == S0s["cheb"] and kdim == 1,
          "S0 identical on mono/Newton/Chebyshev, kdim=%d" % kdim)
    wY = [ud[i] for i in iY]
    WSi = BDH.fr_inv(fr_add(fr_diag(wY), S0s["mono"]))
    sY = [fr_sqrt_pos(w) for w in wY]
    Rw = [[sY[i] * WSi[i][j] * sY[j] for j in range(2)]
          for i in range(2)]
    Rh = hankel_dual_R_Q(xs, ud, iY, d0)
    Cq = C_plus_Q(xs, ud, iX, iY, d0)
    Rc = R_from_C_Q(Cq)
    check("G02-graph-equals-dual-CD-Q",
          Rw == Rh == Rc,
          "W^{1/2}(W+S0)^{-1}W^{1/2} = Hankel CD = C(I+C)^{-1}")
    PhiY = [mono_Q(xs[i], d0) for i in iY]
    rk = fr_rank(PhiY)
    check("G03-ker-dim-Q",
          rk == len(iY) and (d0 - rk) == d0 - len(iY) == 1,
          "rank Phi_Y=%d ker=d0-|Y|=%d" % (rk, d0 - rk))
    # Woodbury 2x2: S+ - S as a rank-1 precision update over Q
    H = [[Fr(3), Fr(1)], [Fr(1), Fr(4)]]
    e = [Fr(1), Fr(-1)]
    om = Fr(2)
    Hi = BDH.fr_inv(H)
    He = [Hi[0][0] * e[0] + Hi[0][1] * e[1],
          Hi[1][0] * e[0] + Hi[1][1] * e[1]]
    eta = He[0] * e[0] + He[1] * e[1]
    Th = Fr(1) / (Fr(1) / om + eta)
    dS = [[Th * e[0] * e[0], Th * e[0] * e[1]],
          [Th * e[1] * e[0], Th * e[1] * e[1]]]
    check("G04-woodbury-Q",
          eta == Fr(9, 11) and Th == Fr(22, 29)
          and dS[0][1] == Th * e[0] * e[1],
          "S^+-S = E^T Theta E, Theta=%s eta=%s" % (Th, eta))
    # FL: R = (I+T)^{-1} with T = C^{-1} gives R = C(I+C)^{-1}
    check("G05-FL-graph-Q",
          Rc[0][0] == Rh[0][0],
          "graph resolvent = dual CD over Q")
    ud_bad = [Fr(1) / u[j] for j in range(5)]
    S0b, _ = S0_Q(xs, ud_bad, iX, iY, d0, kind="mono")
    Rhb = hankel_dual_R_Q(xs, ud_bad, iY, d0)
    check("G06-mustfail-uvee-without-Pprime2",
          S0b != S0s["mono"] and Rhb != Rh,
          "u^vee=1/u (no P'^2) breaks Fractions-exact")
    S0m, _ = S0_Q(xs, ud, iX, iY, d0 - 1, kind="mono")
    S0p, _ = S0_Q(xs, ud, iX, iY, d0 + 1, kind="mono")
    check("G07-mustfail-d0-shift",
          S0m != S0s["mono"] and S0p != S0s["mono"],
          "d0+/-1 breaks S0 (and the graph identity)")
    return xs, ud, iX, iY, d0, S0s["mono"]


def part_w9():
    section("S2  LEG B -- SOURCE FORMULA vs r407 / r356 (w9)")
    mz = V.build_measures(9)
    g = pack_graph(mz)
    pk = DI.pack_C(mz)
    check("G10-w9-graph-vs-chain",
          g["Rg"].shape == pk["R"].shape
          and relres(g["Rg"], pk["R"]) <= FORMULA_HI
          and relres(g["TT"], np.linalg.inv(pk["R"]) - np.eye(len(g["yn"])))
          <= FORMULA_HI,
          "||Rg-R||=%.3e ||TT-(Rinv-I)||=%.3e"
          % (relres(g["Rg"], pk["R"]),
             relres(g["TT"], np.linalg.inv(pk["R"]) - np.eye(len(g["yn"])))))
    nA = pk["nneg"]
    nD = nneg_sym(g["D0"])[0]
    check("G11-w9-inertia-dictionary",
          g["nneg"] == nA == nD == 1,
          "nneg(I-TT)=%d nA0=%d nD0=%d" % (g["nneg"], nA, nD))
    check("G12-w9-opnorm-one-defect",
          W9_OP_LO <= g["opnorm"] <= W9_OP_HI and g["nneg"] == 1,
          "||T0||=%.5f (exactly one sigma>1)" % g["opnorm"])
    piv = seq_innov(g["xp"], g["wX"], g["yn"], g["wY"], g["d0"])
    ineg = np.where(piv < 0)[0]
    check("G13-w9-seq-innovation",
          len(ineg) == 1 and int(ineg[0]) == W9_SEQ_IDX
          and abs(float(piv[ineg[0]]) - W9_SEQ_VAL) <= W9_SEQ_VAL_TOL,
          "SEQ nneg=1 at %d val=%.4f (Uvarov, not LDL of D0)"
          % (int(ineg[0]), float(piv[ineg[0]])))
    # shallow three-basis of T*T (poly_basis via Newton/mono CLS
    # is ill-conditioned at working depth; Q already SATZ)
    dsh = len(g["yn"]) + 3
    Tm = source_T0_cls(g["xp"], g["wX"], g["yn"], g["wY"], dsh)
    check("G14-shallow-cls-runs",
          Tm.shape == (len(g["xp"]), len(g["yn"])),
          "CLS at d0=|Y|+3 shape %s (Q three-basis is the SATZ)"
          % (Tm.shape,))
    Tpi0 = source_T0_cls(g["xp"], g["wX"], g["yn"], g["wY"], len(g["yn"]))
    Rg0 = np.linalg.solve(np.eye(len(g["yn"])) + Tpi0.T @ Tpi0,
                          np.eye(len(g["yn"])))
    r0 = relres(Rg0, pk["R"])
    check("G15-mustfail-PiK-zero",
          r0 >= PI0_LO,
          "d0=|Y| (no kernel) ||Rg-R||=%.3f (R404 order)" % r0)
    A0 = pk["R"] - 0.5 * np.eye(len(g["yn"]))
    Ge = OG.euler_F(mz, g["yn"])
    rE = relres(Ge @ Ge.T, A0)
    check("G16-mustfail-euler-direct",
          rE >= EULER_A0_LO,
          "Euler-on-Y vs A0 rel=%.1f (R404 residual ~209)" % rE)
    return dict(mz=mz, g=g, pk=pk, piv=piv, A0=A0)


def part_worlds(w9, smoke):
    section("S3  LEG B/E -- WORLDS / KILLS / CENSUS")
    mz, g = w9["mz"], w9["g"]
    mzP = P1.reweight(mz, "permute", 1000)
    gP = pack_graph(mzP)
    pP = DI.pack_C(mzP)
    check("G17-permute-algebra-holds-signature-breaks",
          relres(gP["Rg"], pP["R"]) <= 1e-8
          and gP["nneg"] == pP["nneg"] >= PERM_NNEG_LO,
          "permute rest=%.3e nneg=%d (algebra holds, P1 dies)"
          % (relres(gP["Rg"], pP["R"]), gP["nneg"]))
    mzS = HM.scramble_mz()
    gS = pack_graph(mzS)
    pS = DI.pack_C(mzS)
    check("G18-scramble-overload",
          relres(gS["Rg"], pS["R"]) <= FORMULA_HI
          and gS["nneg"] == SCR_NNEG and gS["opnorm"] > 2.0,
          "scramble nneg=%d ||T||=%.2f rest=%.3e"
          % (gS["nneg"], gS["opnorm"], relres(gS["Rg"], pS["R"])))
    gL = pack_graph(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    gD = pack_graph(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G19-chi-transport",
          gL["nneg"] == CHI9_NNEG and gD["nneg"] == CHI15_NNEG
          and gL["opnorm"] < 1.0 < gD["opnorm"] + 1e-3,
          "chi3-9 nneg=%d ||T||=%.5f; dead-15 nneg=%d ||T||=%.5f"
          % (gL["nneg"], gL["opnorm"], gD["nneg"], gD["opnorm"]))
    named = []
    for kz in (15, 18, 42):
        mk = V.build_measures(kz)
        gk = pack_graph(mk)
        pk = DI.pack_C(mk)
        named.append((kz, relres(gk["Rg"], pk["R"]), gk["nneg"],
                      pk["nneg"], gk["opnorm"]))
    check("G19b-named-main-15-18-42",
          all(r <= FORMULA_HI and n == nA
              for _kz, r, n, nA, _op in named),
          "; ".join("kz%d rest=%.3e nneg=%d ||T||=%.5f"
                    % (kz, r, n, op) for kz, r, n, _nA, op in named))
    mzG = P1.reweight(mz, "gauss", 409)
    gG = pack_graph(mzG)
    pG = DI.pack_C(mzG)
    check("G20-jitter-algebra-holds-signature-flips",
          relres(gG["Rg"], pG["R"]) <= FORMULA_HI
          and gG["nneg"] == pG["nneg"] >= JITTER_NNEG_LO,
          "gauss jitter rest=%.3e nneg=%d (was 1)"
          % (relres(gG["Rg"], pG["R"]), gG["nneg"]))
    # SEQ vs inertia off-MAIN: scramble overload, not equal
    pivS = seq_innov(gS["xp"], gS["wX"], gS["yn"], gS["wY"], gS["d0"])
    nseqS = int(np.sum(pivS < 0))
    check("G21-seq-scramble-overload-not-equal",
          nseqS >= 2 and nseqS != gS["nneg"],
          "SEQ nneg=%d vs ind_-(A0)=%d (algebra world-blind; "
          "signature carries the arithmetic)" % (nseqS, gS["nneg"]))
    if smoke:
        section("S3b  core/chi/EXT census skipped (--smoke)")
        return
    core = list(V.admissible_indices())
    n_le1 = n_eq = 0
    n0 = n1 = nx = 0
    mismatch = []
    for kz in core:
        m = V.build_measures(kz)
        gg = pack_graph(m)
        pk = DI.pack_C(m)
        pv = seq_innov(gg["xp"], gg["wX"], gg["yn"], gg["wY"], gg["d0"])
        ns = int(np.sum(pv < 0))
        n_le1 += int(ns <= 1)
        n_eq += int(ns == pk["nneg"] == gg["nneg"])
        if ns != pk["nneg"]:
            mismatch.append((kz, ns, pk["nneg"], gg["nneg"]))
        if ns == 0:
            n0 += 1
        elif ns == 1:
            n1 += 1
        else:
            nx += 1
    check("G30-core42-seq-at-most-one",
          len(core) == CORE_N and n_le1 == CORE_N and nx == 0,
          "core-%d SEQ nneg<=1 on %d/%d (0=%d 1=%d) -- the "
          "CENSUS gate; not a theorem of R^dagger"
          % (CORE_N, n_le1, CORE_N, n0, n1))
    check("G30b-seq-vs-inertia-not-identity",
          n_eq < CORE_N and n_eq >= 20,
          "SEQ nneg = ind_-(A0) on %d/%d (mismatch %s); "
          "equality is CENSUS-not-SATZ, same as scramble 12 vs 21"
          % (n_eq, CORE_N,
             ",".join("kz%d:%d!=%d" % (kz, ns, nA)
                      for kz, ns, nA, _nG in mismatch)))
    live = dead = 0
    nL = nD = 0
    for kz in core:
        mz3 = HM.chi_mz(kz, DMF.Q_CHI3, DMF.LPQ3)
        if mz3 is None:
            continue
        gg = pack_graph(mz3)
        if kz in DEAD_CHI3:
            dead += 1
            nD += int(gg["nneg"] <= 1)
        else:
            live += 1
            nL += int(gg["nneg"] <= 1)
    check("G31-chi3-seq-le1",
          live == 37 and dead == 5 and nL == live and nD == dead,
          "chi3 live %d/%d nneg<=1; dead %d/%d nneg<=1"
          % (nL, live, nD, dead))
    mz4 = HM.chi_mz(20, DMF.Q_CHI4, DMF.LPQ4)
    g4 = pack_graph(mz4)
    check("G32-chi4-20",
          g4["nneg"] <= 1,
          "chi4-20 nneg=%d ||T||=%.5f" % (g4["nneg"], g4["opnorm"]))
    mz130 = V.build_measures(130)
    g130 = pack_graph(mz130)
    p130 = DI.pack_C(mz130)
    check("G33-kz130",
          relres(g130["Rg"], p130["R"]) <= 1e-8
          and g130["nneg"] == p130["nneg"] <= 1,
          "kz130 rest=%.3e nneg=%d ||T||=%.5f"
          % (relres(g130["Rg"], p130["R"]), g130["nneg"],
             g130["opnorm"]))
    ext_ok = True
    for kz in SAMPLE_EXT:
        m = V.build_measures(kz)
        gg = pack_graph(m)
        pk = DI.pack_C(m)
        ext_ok = ext_ok and relres(gg["Rg"], pk["R"]) <= 1e-8
        ext_ok = ext_ok and gg["nneg"] == pk["nneg"] <= 1
    check("G34-main-sample",
          ext_ok,
          "EXT %s graph+inertia+nneg<=1" % (SAMPLE_EXT,))


def part_krein_phi(w9):
    section("S4  LEG C/D -- UVAROV / PHI / KREIN")
    g, mz, A0 = w9["g"], w9["mz"], w9["A0"]
    Fx = OG.euler_F(mz, g["xp"])
    Ftr = g["T0"].T @ Fx
    Gpos = Ftr @ Ftr.T
    npos = nneg_sym(Gpos)[0]
    check("G22-positive-gram-excluded",
          npos == 0 and relres(Gpos, g["D0"]) >= 1.0,
          "transported Euler FF^T nneg=%d rel(D0)=%.2f "
          "(pure positive Gram excluded)"
          % (npos, relres(Gpos, g["D0"])))
    Fp, Fm = Fx[:, 0::2], Fx[:, 1::2]
    Kp = (g["T0"].T @ Fp) @ (g["T0"].T @ Fp).T
    Km = (g["T0"].T @ Fm) @ (g["T0"].T @ Fm).T
    Kr = Kp - Km
    al = float(np.vdot(Kr.ravel(), g["D0"].ravel()) /
               (np.linalg.norm(Kr) * np.linalg.norm(g["D0"]) + 1e-30))
    check("G23-krein-unfitted-miss",
          abs(al) <= KREIN_ALIGN_HI and relres(Kr, g["D0"]) >= 1.0,
          "cos/sin Krein align=%.4f rel=%.2f (no unfitted winner)"
          % (al, relres(Kr, g["D0"])))
    # Phi vs pair+border Schur of Z-I: the MAIN GATE
    dsm = HS.window_data(9, comb=PB.smooth_comb(float(V.window_shape(9)[0])))
    td = source_Tdag(mz, dsm, Bm=PX.build_rung(9)["B"])
    i1, i2 = td["j1"], td["j2"]
    Sm = td["ZI"].shape[0] - 1
    idx = np.array([i1, i2, Sm])
    rest = np.array([i for i in range(Sm + 1) if i not in set(idx)])
    M = td["ZI"]
    Th = M[np.ix_(idx, idx)] - M[np.ix_(idx, rest)] @ np.linalg.solve(
        M[np.ix_(rest, rest)], M[np.ix_(rest, idx)])
    evTh = np.sort(np.linalg.eigvalsh(Th))
    # r369 Phi eigenvalues (frozen from mixed_haynsworth w9 record)
    evPhi = np.sort(np.array([-2.813229172977194, -0.06648163247724746,
                              1.8039076348414458]))
    mis = float(np.linalg.norm(evTh - evPhi)) / (
        float(np.linalg.norm(evPhi)) + 1e-30)
    check("G24-phi-terminal-NOT-literal",
          mis >= PHI_EV_MISMATCH_LO,
          "Schur(ZI,pair+border) ev%s vs Phi ev%s rel=%.2f "
          "-- literal Theta=C^T Phi C REFUTED (Phi is the "
          "Woodbury precision TEMPLATE, not this 3x3)"
          % (tuple(float(x) for x in evTh),
             tuple(float(x) for x in evPhi), mis))
    return td, dsm


def part_dagger(w9, td, dsm, smoke):
    section("S5  LEG F -- AUGMENTED BIRKHOFF / DEAD-CHI FLIP")
    G = td["Tdag"].T @ td["Tdag"]
    n = G.shape[0]
    Rg = np.linalg.solve(np.eye(n) + G, np.eye(n))
    check("G25-tdag-equals-rdag",
          relres(G, td["ZI"]) <= TDAG_REL_HI
          and relres(Rg, td["Rdag"]) <= TDAG_REL_HI,
          "||T*T-(Rinv-I)||=%.3e ||Rg-Rdag||=%.3e"
          % (relres(G, td["ZI"]), relres(Rg, td["Rdag"])))
    lamRd = float(nneg_sym(td["Rdag"])[1][0])
    check("G26-tdag-main-contractive",
          td["opnorm"] < TDAG_MAIN_HI
          and lamRd > 0.5,
          "||T^dagger||=%.6f lamRd=%.9f (MAIN contractive)"
          % (td["opnorm"], lamRd))
    check("G27-mustfail-virtual-node-spread",
          td["spread"] >= VIRT_SPREAD_LO,
          "virtual-star spread=%.2f (R362/R405: border is "
          "NOT a point evaluation)" % td["spread"])
    if smoke:
        mzc, dsmc = chi_border_rung(15, DMF.Q_CHI3, DMF.LPQ3)
        tdc = source_Tdag(mzc, dsmc)
        lamc = float(nneg_sym(tdc["Rdag"])[1][0])
        check("G28-dead-chi15-flips",
              tdc["opnorm"] > 1.0 and lamc < 0.5,
              "chi3-15 ||T^dagger||=%.6f lamRd=%.9f (flips; "
              "R405 ones-c stayed <1)" % (tdc["opnorm"], lamc))
        return
    nflip = 0
    for kz in DEAD_CHI3:
        mzc, dsmc = chi_border_rung(kz, DMF.Q_CHI3, DMF.LPQ3)
        tdc = source_Tdag(mzc, dsmc)
        lamc = float(nneg_sym(tdc["Rdag"])[1][0])
        okf = tdc["opnorm"] > 1.0 and lamc < 0.5
        nflip += int(okf)
        print("    chi3-%d ||T^dagger||=%.6f lamRd=%.9f flip=%s"
              % (kz, tdc["opnorm"], lamc, okf), flush=True)
    mz4, dsm4 = chi_border_rung(DEAD_CHI4[0], DMF.Q_CHI4, DMF.LPQ4)
    td4 = source_Tdag(mz4, dsm4)
    lam4 = float(nneg_sym(td4["Rdag"])[1][0])
    ok4 = td4["opnorm"] > 1.0 and lam4 < 0.5
    check("G35-six-dead-chi-operator-flip",
          nflip == 5 and ok4,
          "dead chi3 %d/5 flip; chi4-20 ||T^dagger||=%.6f flip=%s "
          "(six terminal-dead chi kippen im vollen Operator)"
          % (nflip, td4["opnorm"], ok4))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("borodin_birkhoff_intertwiner_probe -- "
          "PRIME.RDAGGER.BORODIN_BIRKHOFF_INTERTWINER.01 "
          "(round 409)")
    print("SPEC_SHA %s   (BDH %s / DI %s / HM %s / ABD %s)"
          % (SPEC_SHA[:16], BDH.SPEC_SHA[:16], DI.SPEC_SHA[:16],
             HM.SPEC_SHA[:16], ABD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3-42 + EXT + six dead chi)"))
    print("=" * 78)

    section("S0  FIREWALL + TARGET_LEAK")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and OG.SPEC_SHA.startswith(OG_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "BDH %s / DI %s / HM %s / ABD %s"
          % (BDH.SPEC_SHA[:8], DI.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], ABD.SPEC_SHA[:8]))
    leaks = []
    for fn in CONSTRUCTORS:
        leaks += scope_audit(fn)
    check("G00c-target-leak",
          not leaks,
          "constructors Jacobi-free / no A0/R/eig/Cholesky"
          if not leaks else "; ".join(leaks))

    part_satz()
    w9 = part_w9()
    part_worlds(w9, smoke)
    td, dsm = part_krein_phi(w9)
    part_dagger(w9, td, dsm, smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-CENSUS",
          prev_ok,
          "ONE_DEFECT_TRANSPORT_CENSUS: graph identity SATZ; "
          "n_neg^inn<=1 on MAIN census; Phi literal miss; "
          "Krein unfitted miss; T^dagger=r362 dictionary; "
          "no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "ONE_DEFECT_TRANSPORT_CENSUS"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("BORODIN BIRKHOFF %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("BORODIN BIRKHOFF FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
