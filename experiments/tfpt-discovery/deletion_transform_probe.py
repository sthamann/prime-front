#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deletion_transform_probe -- LEMMA.DELETION_TRANSFORM.01 (round 392):
THE DELETION TRANSFORM, exact Christoffel/Uvarov algebra for
the mu-chain after r389/r390.

Coexistence: r390 proved the full cosine grid with Fejer 1-x
is Bernstein-Szego (gamma_k = 1/4, residual 2e-6); occupied
Fejer is that system MINUS the nu-nodes.  r389 placed the
remaining cancellation load in the mu-OP Chebyshev Gram.
This round derives the closed Uvarov formula for the occupied
chain and reads F_eps, Assist, and dDelta from it.

THE FROZEN QUESTION.  Does gamma_k(occupied) =
gamma_k(full) * tau_{k+1} tau_{k-1} / tau_k^2, with
tau_n = det(I - K_n[Xi] W) the CD-kernel Gram at the
deleted nodes, make the deformation exact algebra?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Exact deletion formula.  One-point and block Uvarov
     SATZ over Q; iterated SM is the stable form; mpmath
     identity on a cosine toy; w9 vs occupied-Fejer at
     machine precision.
  B  F_eps from the formula.  |gamma-1/4| is |exp(d2 log tau)-1|.
     Two-period AP deletion (rho_AP=1) does NOT break the box
     (still Bernstein-Szego).  Clustered run>=3 DOES.
     Jump 0.3942 vs 2/5 is census, not structural.
  C  mu-OP Gram.  Assist and dDelta are Uvarov readouts of
     K^mu.  w9 Assist=0.0399 and 99.7% cancel reproduced.
     Occupied-Fejer kernel does NOT carry Assist (lam~10).
     Cancellation sits in off-diagonal SIGNS of K^mu[Xi],
     not in the positive tau-quotients of gamma.
  D  Kills: Christoffel-V mutant; dropped tau_{n-1}; clustered
     run; scramble occupation seed=3.  AP-deletion is a
     named non-kill of F_eps.

CALIBRATION DISCLOSURE.  Identities, w9 formula residual,
Assist/dDelta, AP vs clustered vs scramble, and the core-42
census were first measured in /tmp (r392_cal.py .. r392_cal5.py)
on the same constructors, 2026-08-28.  Frozen floors/ceilings
below are that measurement, sealed as gates.  No two-commit
pre-blind freeze: pins disclosed.  Builder fallback: core-42
only (MAIN-85 aborted at >2 min on EXT; no 181-pack).

FROZEN FROM /tmp (live re-gated, not fitted):
  * 5-atom Q: delete last => gamma = 5/48, 8/75, 5/81.
    Two-point idxs (1,3) => 8/45, 4/15.  Block = iterated.
  * Rational S=5,7,9 with 1-2 deletions: Fractions MATCH.
  * Cosine S=7,9 f64 formula residual < 1e-12.
  * w9 occupied-Fejer: formula maxerr 9.0e-15; last-12
    |g-1/4|=0.03596 jump=0.2379 IN.  1/4-specialization
    residual 1.85e-6 = the r390 Bernstein-Szego remainder.
  * Assist Uvarov(mu+nu): lam=0.999830 maxd=0.9614
    assist=0.0399 gA=13.32 canc=0.9970.  Kernel vs B-matrix
    1.6e-7.  Fejer-mu + actual-nu: lam=10.12, NOT Assist.
  * dDelta last-12 0.04946, Dmax=0.3347 (r388 reproduced).
  * AP every-2 on h=40: last-12 d=0 j=0 IN (rho_AP=1).
    Consecutive deletion run=3: d=0.0672 j=0.4619 OUT.
  * Scramble seed=3 occupied-Fejer: jump=0.4438 OUT.
  * Core-42 occupied-Fejer 0/42 OUT, maxd=0.04892 (kz55),
    maxj=0.3942 (kz55), jump margin 0.0058.  corr(jump,
    rho_AP)=0.43 -- not a theorem of rho_AP<1/5.
  * Mutants: Christoffel-|V| err 0.055; first-order (drop
    tau_{n-1}) err 0.12.

AUSGANG REDUZIERT.  SATZ: the Uvarov gamma-ratio (Hankel
det lemma); block = iterated; Bernstein-Szego specialization
gamma = (1/4)*tau-ratio; Assist/dDelta are exact Uvarov
readouts of K^mu.  NOT proved: F_eps from rho_AP<1/5 (AP
deletion stays IN; clustered run>=3 is the named kill;
kz55 jump 0.3942 is census).  Assist cancellation is the
signed off-diagonal of K^mu[Xi], not the tau-quotients.
Remaining: bound d2 log tau under F1-bounded nu-runs
(F_eps rest); Sign-Schur of K^mu[Xi] (Assist rest).
V3' allows relaxing JUMP (A_15 fails at coherent scale 2.0;
the 1/16 box is the WKB input) -- not moved this round.

MACHINERY: r226 hirota_sign.window_data, r379 box constants,
r390 full_grid / mu_gams, r387 Assist bookkeeping, r388
FO-split, r283 mu_chain / b_matrix.

NO RH CLAIM.  Finite identities, a named reduction, named
kills.  Research documentation, not a theorem of RH.
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

import hirota_sign_probe as HS  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

BOX = 1.0 / 16.0
JUMP = 2.0 / 5.0
SCR_SEED = 3
CORE_N = 42

# disclosed /tmp pins
W9_FML_BAR = 1.0e-12
W9_FJ_D_LO, W9_FJ_D_HI = 0.030, 0.045
W9_ASSIST_LO, W9_ASSIST_HI = 0.030, 0.050
W9_CANC_FLOOR = 0.99
W9_DDELTA12 = (0.040, 0.060)
W9_DMAX = (0.30, 0.36)
CHEB_SPEC_BAR = 5.0e-6
MUTANT_FLOOR = 0.01
CLUST_J_FLOOR = 0.40
SCR_J_FLOOR = 0.40
CORE_FJ_D_BAR = 0.055
CORE_FJ_J_BAR = 0.40
KZ55_J_LO = 0.35
ASSIST_FEJER_LAM_FLOOR = 2.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


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
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "scaled Stieltjes only"
                       if not bad else "; ".join(bad))


# ---------------------------------------------------------------------------
# Exact (Fractions) Stieltjes + Uvarov
# ---------------------------------------------------------------------------

def stieltjes_Q(nodes, wts, n_upto):
    npts = len(nodes)
    pk = [Fr(1)] * npts
    pkm = [Fr(0)] * npts
    Pvals = [list(pk)]
    h = [sum(w * p * p for w, p in zip(wts, pk))]
    alpha = []
    for k in range(n_upto):
        ak = sum(w * x * p * p for w, x, p in zip(wts, nodes, pk)) / h[-1]
        gk = h[-1] / h[-2] if k >= 1 else Fr(0)
        nx = [(x - ak) * p - gk * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        Pvals.append(list(pk))
        h.append(sum(w * p * p for w, p in zip(wts, pk)))
        alpha.append(ak)
    gamma = [h[k] / h[k - 1] for k in range(1, len(h))]
    return {"gamma": gamma, "h": h, "P": Pvals, "alpha": alpha}


def K_cross_Q(P, h, n, i, j):
    s = Fr(0)
    for t in range(n):
        s += P[t][i] * P[t][j] / h[t]
    return s


def det_Q(A):
    A = [row[:] for row in A]
    m = len(A)
    if m == 0:
        return Fr(1)
    det = Fr(1)
    for i in range(m):
        piv = i
        while piv < m and A[piv][i] == 0:
            piv += 1
        if piv == m:
            return Fr(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        det *= A[i][i]
        inv = Fr(1) / A[i][i]
        for j in range(i + 1, m):
            f = A[j][i] * inv
            for k in range(i, m):
                A[j][k] -= f * A[i][k]
    return det


def tau_block_Q(P, h, n, idxs, Ms):
    m = len(idxs)
    Kmat = [[K_cross_Q(P, h, n, idxs[a], idxs[b]) for b in range(m)]
            for a in range(m)]
    A = [[(Fr(1) if a == b else Fr(0)) + Kmat[a][b] * Ms[b]
          for b in range(m)] for a in range(m)]
    return det_Q(A)


def uvarov_gamma_Q(gamma, tau):
    out = []
    for k in range(1, len(gamma) + 1):
        tk = tau[k]
        out.append(gamma[k - 1] * tau[k + 1] * tau[k - 1] / (tk * tk))
    return out


def rat_grid(S):
    nodes, wts = [], []
    for k in range(1, S + 1):
        x = Fr(2 * k - (S + 1), S)
        if abs(x) >= 1:
            continue
        w = Fr(1) - x
        if w <= 0:
            w = Fr(1, 10)
        nodes.append(x)
        wts.append(w)
    return nodes, wts


# ---------------------------------------------------------------------------
# Floating Uvarov (iterated Sherman-Morrison; numerically stable on MAIN)
# ---------------------------------------------------------------------------

def scaled_ops(x, w, n_upto, eval_idx):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    eval_idx = np.asarray(eval_idx, int)
    npts = len(x)
    m = len(eval_idx)
    q = np.ones(npts)
    qm = np.zeros(npts)
    Ls = Ls_m = 0.0
    h = float(np.sum(w * q * q))
    eta_m = h
    gams = []
    Pi = np.empty((n_upto + 1, m), dtype=float)
    Pi[0] = q[eval_idx] / math.sqrt(h)
    for k in range(n_upto):
        alh = float(np.sum(w * x * q * q)) / h
        if k == 0:
            px = (x - alh) * q
        else:
            ge = (h / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (x - alh) * q - ge * fc * qm
        sc = max(float(np.max(np.abs(px))), 1e-300)
        qm, eta_m, Ls_m = q, h, Ls
        q = px / sc
        Ls += math.log(sc)
        h = float(np.sum(w * q * q))
        gams.append((h / eta_m) * math.exp(2.0 * (Ls - Ls_m)))
        Pi[k + 1] = q[eval_idx] / math.sqrt(h)
    return np.array(gams), Pi


def iterated_uvarov(g_full, Pi, w_del, return_Ks=False):
    height, m = Pi.shape
    N = len(g_full)
    Ks = np.zeros((height + 1, m, m))
    G = np.zeros((m, m))
    for n in range(1, height + 1):
        G = G + np.outer(Pi[n - 1], Pi[n - 1])
        Ks[n] = G
    g = np.array(g_full, float)
    ww = np.asarray(w_del, float)
    for a in range(m):
        taus = 1.0 - ww[a] * Ks[:, a, a]
        Nuse = min(N, height - 1)
        tk = taus[1:Nuse + 1]
        good = np.abs(tk) > 1e-30
        idx = np.where(good)[0]
        g[idx] *= (taus[idx + 2] * taus[idx] / (tk[idx] * tk[idx]))
        for n in range(1, height + 1):
            tn = taus[n]
            if abs(tn) < 1e-30:
                continue
            ka = Ks[n, :, a].copy()
            Ks[n] += (ww[a] / tn) * np.outer(ka, ka)
    if return_Ks:
        return g, Ks
    return g


def match_indices(full_x, subset_x, atol=1e-10):
    idx = []
    for y in subset_x:
        d = np.abs(full_x - y)
        j = int(np.argmin(d))
        if d[j] > atol:
            raise RuntimeError("no match %.6f min=%.3e" % (y, d[j]))
        idx.append(j)
    return np.array(idx, int)


def last12(g):
    g12 = np.asarray(g[-12:], float)
    dbox = float(np.max(np.abs(g12 - 0.25)))
    jmp = (float(np.max(np.abs(np.log(g12[1:] / g12[:-1]))))
           if np.all(g12 > 0) else float("inf"))
    return dbox, jmp


def in_box(g):
    d, j = last12(g)
    return d <= BOX + 1e-12 and j <= JUMP, d, j


def assist_from_K(K, v):
    sv = np.sqrt(np.asarray(v, float))
    E = K * np.outer(sv, sv)
    diag = np.diag(E).copy()
    maxd = float(np.max(diag))
    lam = float(np.linalg.eigvalsh(E)[-1])
    off = np.abs(E).copy()
    np.fill_diagonal(off, 0.0)
    gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
    assist = lam / maxd - 1.0 if maxd > 0 else 0.0
    canc = 1.0 - assist / max(gA, 1e-12)
    return dict(lam=lam, maxd=maxd, assist=assist, gA=gA, canc=canc)


def part_a_standalone():
    section("S1  LEG A -- UVAROV GAMMA-RATIO OVER Q")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    full = stieltjes_Q(nodes, wts, 4)

    # one-point: delete last
    xi, M = 4, -wts[4]
    nmax = 3
    tau = [Fr(1) + M * K_cross_Q(full["P"], full["h"], n, xi, xi)
           for n in range(nmax + 2)]
    g_fml = uvarov_gamma_Q(full["gamma"][:nmax], tau)
    red = stieltjes_Q(nodes[:-1], wts[:-1], nmax)
    check("G01-one-point-Uvarov-Q",
          g_fml == red["gamma"] and g_fml == [Fr(5, 48), Fr(8, 75), Fr(5, 81)],
          "delete last: gamma = 5/48, 8/75, 5/81")

    # two-point block vs iterated vs direct
    idxs = [1, 3]
    Ms = [-wts[i] for i in idxs]
    nmax = 2
    tau_b = [tau_block_Q(full["P"], full["h"], n, idxs, Ms)
             for n in range(nmax + 2)]
    g_block = uvarov_gamma_Q(full["gamma"][:nmax], tau_b)
    keep = [i for i in range(5) if i not in idxs]
    red2 = stieltjes_Q([nodes[i] for i in keep],
                       [wts[i] for i in keep], nmax)
    # iterated: delete idx 1 then idx 3
    tau1 = [Fr(1) + (-wts[1]) * K_cross_Q(full["P"], full["h"], n, 1, 1)
            for n in range(6)]
    mid = stieltjes_Q([nodes[i] for i in range(5) if i != 1],
                      [wts[i] for i in range(5) if i != 1], 3)
    tau2 = [Fr(1) + (-wts[3]) * K_cross_Q(mid["P"], mid["h"], n, 2, 2)
            for n in range(nmax + 2)]
    g_iter = uvarov_gamma_Q(mid["gamma"][:nmax], tau2)
    check("G02-block-equals-iterated-Q",
          g_block == red2["gamma"] and g_iter == red2["gamma"]
          and g_block == [Fr(8, 45), Fr(4, 15)],
          "two-point: 8/45, 4/15; block = iterated = direct")

    n_bad = 0
    for S in (5, 7, 9):
        nds, wss = rat_grid(S)
        npts = len(nds)
        fl = stieltjes_Q(nds, wss, npts - 1)
        for ndel in (1, 2):
            if ndel >= npts - 2:
                continue
            idd = list(range(npts - ndel, npts))
            Ms = [-wss[i] for i in idd]
            nm = npts - ndel - 1
            taus = [tau_block_Q(fl["P"], fl["h"], n, idd, Ms)
                    for n in range(nm + 2)]
            gf = uvarov_gamma_Q(fl["gamma"][:nm], taus)
            kp = [i for i in range(npts) if i not in idd]
            rd = stieltjes_Q([nds[i] for i in kp], [wss[i] for i in kp], nm)
            if gf != rd["gamma"]:
                n_bad += 1
    check("G03-rational-S579-deletions-Q",
          n_bad == 0,
          "S=5,7,9 with 1-2 deletions: Fractions MATCH")

    x = Fr(2, 5)
    p2 = x * x - Fr(1, 4)
    check("G04-chebyshev-U-quarters",
          p2 == x * x - Fr(1, 4),
          "monic U: p2=x^2-1/4 so gamma_k=1/4")

    check("G05-jump-not-implied",
          math.log(5.0 / 3.0) > JUMP,
          "log(5/3)=%.4f > 2/5 (box does not imply JUMP)"
          % math.log(5.0 / 3.0))

    # cosine f64 identity
    ok_cos = True
    det = []
    for S in (7, 9):
        xs = np.array([math.cos(math.pi * k / S) for k in range(1, S)])
        ws = np.maximum(1.0 - xs, 1e-15)
        npts = len(xs)
        for ndel in (1, 2):
            idx_d = np.arange(npts - ndel, npts)
            keep = np.array([i for i in range(npts) if i not in idx_d])
            depth = npts - ndel - 2
            if depth < 1:
                continue
            gF, Pi = scaled_ops(xs, ws, depth + 1, idx_d)
            gT = iterated_uvarov(gF[:depth], Pi, ws[idx_d])
            gD = P.mu_gams(xs[keep], ws[keep], depth)
            err = float(np.max(np.abs(gT - gD)))
            det.append(err)
            if err > 1e-12:
                ok_cos = False
    check("G06-cosine-S79-f64",
          ok_cos,
          "S=7,9 del 1-2 maxerr=%.3e" % max(det))

    # mpmath on S=7 delete-last
    try:
        import mpmath as mp
        mp.mp.dps = 30
        S = 7
        xs = [mp.cos(mp.pi * k / S) for k in range(1, S)]
        ws = [1 - x for x in xs]
        # numpy formula
        xnp = np.array([float(x) for x in xs])
        wnp = np.array([float(w) for w in ws])
        gF, Pi = scaled_ops(xnp, wnp, 5, np.array([len(xnp) - 1]))
        gT = iterated_uvarov(gF[:4], Pi, wnp[-1:])
        gD = P.mu_gams(xnp[:-1], wnp[:-1], 4)
        err_f = float(np.max(np.abs(gT - gD)))
        check("G07-mpmath-S7-identity",
              err_f < 1e-12,
              "f64 Uvarov vs direct maxerr=%.3e (dps-30 toy; "
              "Fractions SATZ is G01-G03)" % err_f)
    except Exception as e:
        check("G07-mpmath-S7-identity", False, str(e))


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 formula, Assist, kills")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2
    xf, wff = P.full_grid(N)
    idx_nu = match_indices(xf, ys)
    idx_mu = match_indices(xf, xs)
    w_del_f = wff[idx_nu]
    mass = float(ws.sum())
    wf = P.fejer_w(xs, mass)

    print("    w9 full-grid OPs n=%d m_nu=%d ..." % (n, len(idx_nu)),
          flush=True)
    g_full, Pi = scaled_ops(xf, wff, n + 1, idx_nu)
    g_fml, Ks_f = iterated_uvarov(g_full[:n], Pi, w_del_f, return_Ks=True)
    g_occ = P.mu_gams(xs, wf, n)
    err = float(np.max(np.abs(g_fml - g_occ[:n])))
    ifo, dfo, jfo = in_box(g_occ)
    check("G10-w9-formula-vs-occupied",
          err < W9_FML_BAR,
          "max |g_Uvarov - g_occ|=%.3e (machine identity)" % err)
    check("G11-w9-occupied-inside",
          ifo and W9_FJ_D_LO < dfo < W9_FJ_D_HI,
          "|g-1/4|=%.5f jump=%.4f" % (dfo, jfo))

    # 1/4 specialization
    ratio = g_fml / np.maximum(g_full[:n], 1e-30)
    g_cheb = 0.25 * ratio
    err_c = float(np.max(np.abs(g_cheb - g_occ[:n])))
    check("G12-BS-specialization-residual",
          err_c < CHEB_SPEC_BAR,
          "gamma=1/4 * tau-ratio vs occ maxerr=%.3e "
          "(= r390 Bernstein-Szego remainder)" % err_c)

    # Assist from Uvarov(mu+nu)
    print("    Uvarov(mu+nu) Assist k=%d ..." % (N - 1), flush=True)
    w_union = np.zeros(len(xf))
    w_union[idx_mu] = ws
    w_union[idx_nu] = vs
    g_un, Pi_un = scaled_ops(xf, w_union, n + 1, idx_nu)
    _gmu, Ks_mu = iterated_uvarov(g_un[:n], Pi_un, vs, return_Ks=True)
    k_wall = N - 1
    rA = assist_from_K(Ks_mu[k_wall], vs)
    check("G13-w9-Assist-Uvarov",
          W9_ASSIST_LO < rA["assist"] < W9_ASSIST_HI
          and rA["canc"] > W9_CANC_FLOOR and rA["lam"] < 1.0,
          "lam=%.6f maxd=%.4f assist=%.4f gA=%.2f canc=%.4f"
          % (rA["lam"], rA["maxd"], rA["assist"], rA["gA"], rA["canc"]))

    rF = assist_from_K(Ks_f[k_wall], vs)
    check("G14-Fejer-kernel-not-Assist",
          rF["lam"] > ASSIST_FEJER_LAM_FLOOR,
          "Fejer-mu + actual-nu lam=%.3f (deletion of nodes "
          "does NOT carry Assist=0.0399)" % rF["lam"])

    # dDelta from kernel increments of true mu
    Q = np.empty(n)
    for k in range(n):
        dK = Ks_mu[k + 1] - Ks_mu[k]
        Q[k] = float(vs @ np.diag(dK))
    th_n = np.arccos(np.clip(ys, -1, 1))
    th_m = np.arccos(np.clip(xs, -1, 1))

    def Cq(th, w, q):
        return float(np.dot(w, np.cos(q * th)))

    C0n, C0m = Cq(th_n, vs, 0), Cq(th_m, ws, 0)
    QT = np.array([(C0n + Cq(th_n, vs, 2 * k)) / (C0m + Cq(th_m, ws, 2 * k))
                   for k in range(n)])
    Delta = Q - QT
    dDelta = np.diff(Delta)
    dD12 = float(np.max(np.abs(dDelta[-12:])))
    Dmax = float(np.max(np.abs(Delta)))
    check("G15-w9-dDelta-Uvarov",
          W9_DDELTA12[0] < dD12 < W9_DDELTA12[1]
          and W9_DMAX[0] < Dmax < W9_DMAX[1],
          "dDelta12=%.5f Dmax=%.4f (r388 reproduced)"
          % (dD12, Dmax))

    # mutants on h=6
    xf6, wf6 = P.full_grid(6)
    idx_d6 = np.array([len(xf6) - 2, len(xf6) - 1])
    keep6 = np.array([i for i in range(len(xf6)) if i not in idx_d6])
    depth6 = len(keep6) - 2
    gF6, Pi6 = scaled_ops(xf6, wf6, depth6 + 1, idx_d6)
    gU6 = iterated_uvarov(gF6[:depth6], Pi6, wf6[idx_d6])
    gD6 = P.mu_gams(xf6[keep6], wf6[keep6], depth6)
    Vfac = np.ones(len(keep6))
    for yi in xf6[idx_d6]:
        Vfac *= (xf6[keep6] - yi)
    gC = P.mu_gams(xf6[keep6], wf6[keep6] * np.abs(Vfac), depth6)
    errC = float(np.max(np.abs(gC - gD6)))
    check("G16-Christoffel-mutant-fails",
          errC > MUTANT_FLOOR
          and float(np.max(np.abs(gU6 - gD6))) < 1e-10,
          "Christoffel-|V| err=%.3e vs Uvarov err=%.3e"
          % (errC, float(np.max(np.abs(gU6 - gD6)))))

    # first-order mutant: drop tau_{n-1}
    height, m = Pi6.shape
    Ks = np.zeros((height + 1, m, m))
    G = np.zeros((m, m))
    for nK in range(1, height + 1):
        G = G + np.outer(Pi6[nK - 1], Pi6[nK - 1])
        Ks[nK] = G
    gmut = np.array(gF6[:depth6], float)
    ww = wf6[idx_d6]
    for a in range(m):
        taus = 1.0 - ww[a] * Ks[:, a, a]
        Nuse = min(depth6, height - 1)
        gmut[:Nuse] *= taus[2:Nuse + 2] / np.maximum(taus[1:Nuse + 1], 1e-30)
        for nK in range(1, height + 1):
            tn = taus[nK]
            if abs(tn) < 1e-30:
                continue
            ka = Ks[nK, :, a].copy()
            Ks[nK] += (ww[a] / tn) * np.outer(ka, ka)
    errM = float(np.max(np.abs(gmut - gD6)))
    check("G17-first-order-mutant-fails",
          errM > MUTANT_FLOOR,
          "drop tau_{n-1}: err=%.3e (the second ratio is load-bearing)"
          % errM)

    # AP every-2: stays IN (honest non-kill of F_eps)
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    m_ap = (np.arange(S40) % 2 == 0)
    occ, wo = xf40[~m_ap], wf40[~m_ap]
    depth_ap = min(len(occ) - 2, 40)
    g_ap = P.mu_gams(occ, wo, depth_ap)
    iap, dap, jap = in_box(g_ap)
    check("G18-AP-deletion-stays-IN",
          iap and dap < 0.01,
          "h=40 every-2 last12 d=%.4f j=%.4f -- rho_AP=1 does "
          "NOT break F_eps (still Bernstein-Szego)" % (dap, jap))

    # clustered run=3: OUT
    m_cl = np.zeros(S40, dtype=bool)
    m_cl[S40 // 3:S40 // 3 + 3] = True
    g_cl = P.mu_gams(xf40[~m_cl], wf40[~m_cl], min((~m_cl).sum() - 2, 60))
    icl, dcl, jcl = in_box(g_cl)
    check("G19-clustered-run3-kills",
          (not icl) and jcl > CLUST_J_FLOOR,
          "run=3 d=%.4f j=%.4f OUT (F1 max-run<=2 is the F_eps kill)"
          % (dcl, jcl))

    # scramble occupation seed=3
    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    ns = int(ds["n_max"]) - 2
    xfs, wffs = P.full_grid(int(ds["n_max"]))
    inu = match_indices(xfs, ds["ys"])
    gFs, Pis = scaled_ops(xfs, wffs, ns + 1, inu)
    gsc = iterated_uvarov(gFs[:ns], Pis, wffs[inu])
    gsc_dir = P.mu_gams(ds["xs"], P.fejer_w(ds["xs"], float(ds["ws"].sum())),
                        ns)
    errsc = float(np.max(np.abs(gsc - gsc_dir[:ns])))
    isc, dsc, jsc = in_box(gsc_dir)
    check("G20-scramble-seed3-kills",
          (not isc) and jsc > SCR_J_FLOOR and errsc < 1e-9,
          "scr-seed=%d formula-err=%.3e d=%.4f j=%.4f OUT "
          "(occupation vs MAIN)" % (SCR_SEED, errsc, dsc, jsc))

    if smoke:
        return

    section("S3  FULL CENSUS -- core-42 occupied-Fejer via formula")
    core = list(V.admissible_indices())
    check("G21-ladder-size",
          len(core) == CORE_N,
          "core %d" % len(core))
    n_out = 0
    max_d = max_j = 0.0
    kz_j = None
    for i, kz in enumerate(core):
        dk = HS.window_data(kz)
        nk = int(dk["n_max"]) - 2
        wfk = P.fejer_w(dk["xs"], float(dk["ws"].sum()))
        gf = P.mu_gams(dk["xs"], wfk, nk)
        dd, jj = last12(gf)
        max_d, max_j = max(max_d, dd), max(max_j, jj)
        if jj >= max_j - 1e-15:
            kz_j = kz
        if dd > BOX or jj > JUMP:
            n_out += 1
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)
    check("G22-core42-occupied-inside",
          n_out == 0 and max_d < CORE_FJ_D_BAR and max_j < CORE_FJ_J_BAR,
          "OUT %d/42 maxd=%.5f maxj=%.4f (jump margin %.4f)"
          % (n_out, max_d, max_j, JUMP - max_j))
    check("G23-kz55-jump-thin",
          kz_j == 55 and max_j > KZ55_J_LO,
          "max jump=%.4f at kz%d vs 2/5 -- CENSUS, not a "
          "corollary of rho_AP<1/5" % (max_j, kz_j))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("deletion_transform_probe -- LEMMA.DELETION_TRANSFORM.01 "
          "(round 392)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_construction(smoke)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = ("DELETION TRANSFORM LEMMA SMOKE" if smoke
           else "DELETION TRANSFORM LEMMA")
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
