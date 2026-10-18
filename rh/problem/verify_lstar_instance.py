#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_lstar_instance.py -- machine check that the standalone
problem statement in rh/problem/lstar_problem.tex is the CORRECT
definition.

The document defines two discrete measures mu_S and nu_S on [-1, 1]
from first principles (von Mangoldt comb, triangular-window sampling,
archimedean lag function, circulant spectral density, folding) and
asks for a proof or refutation of

    L*:  int p^2 dnu_S  <  int p^2 dmu_S
         for every real polynomial p != 0 with deg p < (S+1)/2.

This script:

  PART A (STANDALONE): builds mu_S and nu_S for the flagship instance
     z = 16 (S = 367, S_+ = 263, S_- = 104, N_w = 184) from scratch,
     using ONLY the formulas printed in the document (numpy + mpmath,
     no repo imports).

  PART B (CROSS-CHECK GATE, clearly separated): imports the
     repository builders (verification/v563_paper2_readouts.py and
     experiments/tfpt-discovery/port_integrable_kernel_probe.py) and
     verifies that the standalone construction reproduces the exact
     atom positions and weights of the campaign object.  This is the
     proof that the DOCUMENT carries the RIGHT definition.  Any
     mismatch here is a critical finding.

  PART C (SPECTRAL FACTS): reproduces lambda_max(E_{N_w}) = 0.99983
     (record value 0.99983248 from the mp dps-60 ward of the
     campaign), the crossing lambda_max(E_{185}) > 1, and re-confirms
     both with an independent mpmath dps-60 recomputation.

  PART D (THE INEQUALITY): checks int p^2 dnu < int p^2 dmu directly
     on low-degree monomials (exact weighted sums) and on 500 random
     polynomials of degree < N_w drawn in the mu-orthonormal basis.

  Optional --ladder: runs the standalone pipeline over all 42
     admissible windows of the family (h in [128, 900], >= 40 atoms)
     and reports the margin 1 - lambda_max(E_{N_w}) per window
     (several minutes; the flagship-instance gates above do not
     depend on it).

Exit: prints per-gate PASS/FAIL lines and the final line
"LSTAR INSTANCE VERIFIED" iff every gate passed.

Context: the inequality is the missing lemma L* of a research
program on Weil positivity (see rh/paper/rh_program.pdf and the
sealed probe experiments/tfpt-discovery/
fullsource_quasidefiniteness_probe.py, round r283).  NO claim is
made here; this script only certifies that the standalone problem
statement and the campaign object are the same mathematical object.
NOT evidence for or against the Riemann Hypothesis.  NO RH CLAIM.
"""

from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

# ------------------------------------------------------------------
# frozen constants of the family (as printed in lstar_problem.tex)
# ------------------------------------------------------------------
TABLE_CAP = 400000        # von Mangoldt table cap (family definition)
ZONE_DEEP = 380000        # zone horizon for the admissible index set
NU_OVER = 4               # oversampling parameter nu
H_MIN, H_MAX = 128, 900   # admissible window range (the 42 rungs)
N_ATOM_MIN = 40           # atom floor per window
GL_N = 48                 # Gauss-Legendre order per smooth segment
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

Z_INDEX = 9               # flagship instance: the 10th prime power
# record values (campaign, r283/r284, mp dps-60 arbitrated)
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248      # lambda_max(E_184), mp dps-60
REC_LAM_NEXT = 1.00003660  # lambda_max(E_185), mp dps-60
REC_TOP = (0.99983, 0.99874, 0.99597)
TOL_XCHK = 1.0e-9         # standalone vs builder, relative
TOL_LAM = 1.0e-6          # f64 lambda_max vs mp record, absolute
TOL_MP = 1.0e-7           # standalone f64 vs standalone mp, absolute
N_RAND = 500              # random polynomials in part D
RAND_SEED = 20260825

CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %-34s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(t):
    print("\n" + "-" * 72 + "\n" + t + "\n" + "-" * 72, flush=True)


# ==================================================================
# PART A -- STANDALONE CONSTRUCTION (document formulas only)
# ==================================================================
def von_mangoldt(n_max):
    """Lambda(n) for n <= n_max (sieve)."""
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


LAM = von_mangoldt(TABLE_CAP)
PP = np.nonzero(LAM > 0.0)[0]          # prime powers, sorted
U = np.log(PP.astype(float))           # u_i = log n_i
W_VM = 2.0 * LAM[PP] / np.sqrt(PP.astype(float))  # 2 Lambda(n)/sqrt(n)

_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def window_shape(kz):
    """(alpha, M, L, N_w, Delta) of window kz per the document:
    alpha = u_kz, delta = (u_{kz+1} - u_kz)/(2 nu),
    M = ceil(alpha/delta - 1e-9) + 1 rounded up to even,
    lag spacing Delta = 2 alpha / M, L = 2M - 2, N_w = M/2."""
    alpha = float(U[kz])
    delta = (float(U[kz + 1]) - alpha) / (2.0 * NU_OVER)
    M = int(math.ceil(alpha / delta - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, M, 2 * M - 2, M // 2, 2.0 * alpha / M


def prime_lags(alpha, M, D):
    """P(i Delta): triangular-window sampling of the von Mangoldt
    comb -Sum_{n <= e^{2 alpha}} (Lambda(n)/sqrt(n)) delta_{log n},
    c^P_i = -Sum_n (Lambda(n)/sqrt(n)) t_Delta(i Delta - log n)
            -Sum_{log n < Delta} (Lambda(n)/sqrt(n))
                                 t_Delta(i Delta + log n),
    t_Delta(x) = max(0, 1 - |x|/Delta)."""
    ka = int(np.searchsorted(U, 2.0 * alpha + 1.0e-14, side="right"))
    c = np.zeros(M)
    for u_j, m_j in zip(U[:ka], W_VM[:ka]):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
        if u_j < D:                    # reflected tent (u_j < Delta)
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= m_j * 0.5 * v
    return c, ka


def arch_A_far(s, D):
    """A(s) for s >= Delta:
    A(s) = -int_{s-Delta}^{s+Delta} t_Delta(s-w)
            e^{-w/2}/(1 - e^{-2w}) dw   (two GL segments)."""
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def arch_A_near(s, D):
    """A(s) for 0 <= s < Delta:
    A(s) = -(gamma + log pi) t_Delta(s)
           + 2 int_0^{s+Delta} [t_Delta(s) e^{-2w} - S(w) e^{-w/2}]
                               / (1 - e^{-2w}) dw
           - t_Delta(s) log(1 - e^{-2(s+Delta)}),
    S(w) = (t_Delta(s-w) + t_Delta(s+w))/2."""
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    Wend = s + D
    pts = sorted({0.0, s, D - s, Wend})
    pts = [p for p in pts if 0.0 <= p <= Wend]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
                   + np.maximum(0.0, 1.0 - (s + w) / D))
        integ = ((tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
                 / (-np.expm1(-2.0 * w)))
        tot += half * float(np.dot(_GLW, integ))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * Wend))))


def arch_lags(M, D):
    """c^A_i = A(i Delta), i = 0..M-1."""
    sv = np.arange(M) * D
    out = np.empty(M)
    far = sv >= D
    if far.any():
        out[far] = arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = arch_A_near(sv[i], D)
    return out


def spectral_density(c):
    """d_j = f(2 pi j / L): eigenvalues of the circulant extension
    of the symmetric Toeplitz lag sequence c_0..c_{M-1};
    f(theta) = c_0 + 2 Sum_{k=1}^{M-2} c_k cos(k theta)
                   + c_{M-1} cos((M-1) theta), L = 2M - 2."""
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def build_measures(kz):
    """The two measures of the document, standalone.
    Returns dict with atoms/weights of mu (xp, wp), nu (yn, vn),
    the sorted signed union (xu, wu), and the shape numbers."""
    alpha, M, L, Nw, D = window_shape(kz)
    cP, ka = prime_lags(alpha, M, D)
    cA = arch_lags(M, D)
    d = spectral_density(cA + cP)
    # folding j <-> L - j onto x = cos(2 pi j / L), j = 1..L/2
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5                       # j = L/2 is its own mirror
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    xp, wp = x[pos], wt[pos]            # mu
    yn, vn = x[~pos], -wt[~pos]         # nu (weights positive)
    o = np.argsort(x)
    return dict(alpha=alpha, M=M, L=L, Nw=Nw, D=D, ka=ka,
                xp=xp, wp=wp, yn=yn, vn=vn,
                xu=x[o], wu=wt[o], S=len(x))


def mu_chain(x, w, depth):
    """orthonormal three-term recurrence of the positive measure
    (x, w): returns (a[0..depth-1], b[0..depth-1], h0) with b[i]
    the coupling P_i -> P_{i+1}."""
    h0 = float(np.sum(w))
    u = np.full_like(x, 1.0 / math.sqrt(h0))
    um = np.zeros_like(x)
    a = np.zeros(depth)
    b = np.zeros(depth)
    for i in range(depth):
        a[i] = float(np.sum(w * x * u * u))
        r = (x - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        s = math.sqrt(float(np.sum(w * r * r)))
        b[i] = s
        um, u = u, r / s
    return a, b, h0


def b_matrix(a, b, h0, y, v, depth):
    """B[k, i] = sqrt(v_k) P_i(y_k): mu-orthonormal polynomials on
    the nu atoms, nu-weight dressed."""
    u = np.sqrt(v) / math.sqrt(h0)
    um = np.zeros_like(y)
    B = np.zeros((len(y), depth))
    B[:, 0] = u
    for i in range(depth - 1):
        r = (y - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        B[:, i + 1] = u
    return B


def lam_max_at(mz, n):
    """lambda_max(E_n), E_n = B_n B_n^T, from a build_measures dict."""
    a, b, h0 = mu_chain(mz["xp"], mz["wp"], n)
    B = b_matrix(a, b, h0, mz["yn"], mz["vn"], n)
    return float(np.linalg.eigvalsh(B @ B.T)[-1]), B


def admissible_indices():
    """the 42 admissible window indices of the family:
    kz in the deep zone range with h = M/2 in [H_MIN, H_MAX] and at
    least N_ATOM_MIN prime powers below e^{2 alpha}."""
    nz_deep = int(np.searchsorted(PP, ZONE_DEEP, side="right"))
    out = []
    for kz in range(2, nz_deep - 2):
        alpha, M, _L, Nw, _D = window_shape(kz)
        ka = int(np.searchsorted(U, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        if H_MIN <= Nw <= H_MAX and ka >= N_ATOM_MIN:
            out.append(kz)
    return out


# ==================================================================
# PART C helper -- independent mpmath ward (standalone data)
# ==================================================================
def mp_lam_max(mz, n, dps=60):
    """lambda_max(E_n) with the chain and B recomputed in mpmath
    at the given dps (eigenvalues taken in f64 on the mp-exact B)."""
    import mpmath as mp
    mp.mp.dps = dps
    X = [mp.mpf(float(t)) for t in mz["xp"]]
    W = [mp.mpf(float(t)) for t in mz["wp"]]
    Y = [mp.mpf(float(t)) for t in mz["yn"]]
    V = [mp.mpf(float(t)) for t in mz["vn"]]
    h0 = mp.fsum(W)
    u = [1 / mp.sqrt(h0)] * len(X)
    um = [mp.mpf(0)] * len(X)
    ub = [mp.sqrt(v) / mp.sqrt(h0) for v in V]
    ubm = [mp.mpf(0)] * len(Y)
    B = np.zeros((len(Y), n))
    B[:, 0] = [float(q) for q in ub]
    for i in range(n):
        a_i = mp.fsum(w * x * q * q for w, x, q in zip(W, X, u))
        if i > 0:
            r = [(x - a_i) * q - b_prev * qm
                 for x, q, qm in zip(X, u, um)]
            rb = [(y - a_i) * q - b_prev * qm
                  for y, q, qm in zip(Y, ub, ubm)]
        else:
            r = [(x - a_i) * q for x, q in zip(X, u)]
            rb = [(y - a_i) * q for y, q in zip(Y, ub)]
        s = mp.sqrt(mp.fsum(w * t * t for w, t in zip(W, r)))
        um, u = u, [t / s for t in r]
        ubm, ub = ub, [t / s for t in rb]
        b_prev = s
        if i + 1 < n:
            B[:, i + 1] = [float(q) for q in ub]
    return float(np.linalg.eigvalsh(B @ B.T)[-1])


# ==================================================================
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--ladder", action="store_true",
                     help="also sweep all 42 admissible windows")
    args = par.parse_args()

    print("=" * 72)
    print("verify_lstar_instance -- standalone check of the L* "
          "problem statement")
    print("flagship instance: z = %d (index %d), the document's "
          "running example" % (int(PP[Z_INDEX]), Z_INDEX))
    print("=" * 72)

    # ---------------- PART A: standalone construction
    section("A  STANDALONE CONSTRUCTION (document formulas only)")
    mz = build_measures(Z_INDEX)
    Sp, Sm = len(mz["xp"]), len(mz["yn"])
    check("A1-shape", int(PP[Z_INDEX]) == 16
          and mz["M"] == 368 and mz["L"] == 734 and mz["Nw"] == 184,
          "z = 16, alpha = log 16 = %.6f, M = %d, L = %d, "
          "N_w = %d, Delta = %.8f, %d comb atoms"
          % (mz["alpha"], mz["M"], mz["L"], mz["Nw"], mz["D"],
             mz["ka"]))
    check("A2-atom-counts", mz["S"] == REC_S and Sp == REC_SP
          and Sm == REC_SM and mz["Nw"] == (mz["S"] + 1) // 2,
          "S = %d (record %d), S_+ = %d (record %d), S_- = %d "
          "(record %d); N_w = (S+1)/2 = %d"
          % (mz["S"], REC_S, Sp, REC_SP, Sm, REC_SM, mz["Nw"]))
    check("A3-masses", float(np.sum(mz["wu"])) > 0.0,
          "mu(R) = %.6f, nu(R) = %.6f, mu - nu total = %+.6f > 0, "
          "min atom gap %.2e"
          % (float(np.sum(mz["wp"])), float(np.sum(mz["vn"])),
             float(np.sum(mz["wu"])),
             float(np.min(np.diff(mz["xu"])))))

    # ---------------- PART B: cross-check gate (repo imports)
    section("B  CROSS-CHECK GATE vs THE REPOSITORY BUILDERS "
            "(imports allowed HERE ONLY)")
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(here, "..", ".."))
    sys.path.insert(0, os.path.join(repo, "verification"))
    sys.path.insert(0, os.path.join(repo, "experiments",
                                    "tfpt-discovery"))
    import port_integrable_kernel_probe as PIK   # noqa: E402
    rung = PIK.build_rung(Z_INDEX)
    bx, bw, _ = PIK.folded_measure(rung["d"], rung["L"], +1.0)
    by, bv, _ = PIK.folded_measure(rung["d"], rung["L"], -1.0)
    ok_shape = (rung["L"] == mz["L"] and rung["h"] == mz["Nw"]
                and len(bx) == Sp and len(by) == Sm)
    scale = float(np.max(np.abs(np.concatenate([bw, bv]))))
    dev_pos = max(float(np.max(np.abs(np.sort(bx)
                                      - np.sort(mz["xp"])))),
                  float(np.max(np.abs(np.sort(by)
                                      - np.sort(mz["yn"])))))
    dev_wt = max(float(np.max(np.abs(np.sort(bw)
                                     - np.sort(mz["wp"])))),
                 float(np.max(np.abs(np.sort(bv)
                                     - np.sort(mz["vn"]))))) / scale
    check("B1-builder-match", ok_shape and dev_pos <= TOL_XCHK
          and dev_wt <= TOL_XCHK,
          "shape L/N_w/S_+/S_- identical; max position dev %.1e, "
          "max relative weight dev %.1e (bar %.0e) -- the "
          "standalone construction IS the campaign object"
          % (dev_pos, dev_wt, TOL_XCHK))

    # ---------------- PART C: spectral facts
    section("C  SPECTRAL FACTS (lambda_max of the dressed CD-kernel "
            "Gram)")
    lam184, B184 = lam_max_at(mz, mz["Nw"])
    lam185, _ = lam_max_at(mz, mz["Nw"] + 1)
    ev = np.linalg.eigvalsh(B184 @ B184.T)[-3:][::-1]
    check("C1-lambda-max", abs(lam184 - REC_LAM) <= TOL_LAM,
          "lambda_max(E_184) = %.8f (record %.8f, dev %.1e, bar "
          "%.0e); margin 1 - lambda = %.4e"
          % (lam184, REC_LAM, abs(lam184 - REC_LAM), TOL_LAM,
             1.0 - lam184))
    check("C2-crossing", lam184 < 1.0 < lam185
          and abs(lam185 - REC_LAM_NEXT) <= TOL_LAM,
          "lambda_max(E_185) = %.8f > 1 (record %.8f): the "
          "inequality genuinely fails one degree past (S+1)/2"
          % (lam185, REC_LAM_NEXT))
    check("C3-top-eigs", all(abs(float(ev[i]) - REC_TOP[i]) <= 5e-5
                             for i in range(3)),
          "top-3 eigenvalues %s == record %s (three above 0.995: "
          "the contraction is broadly tight)"
          % (str([round(float(t), 5) for t in ev]), str(REC_TOP)))
    lam_mp = mp_lam_max(mz, mz["Nw"], dps=60)
    lam_mp_next = mp_lam_max(mz, mz["Nw"] + 1, dps=60)
    check("C4-mp-ward", abs(lam_mp - lam184) <= TOL_MP
          and lam_mp < 1.0 < lam_mp_next,
          "independent mpmath dps-60 recomputation: "
          "lambda_max(E_184) = %.8f, lambda_max(E_185) = %.8f "
          "(f64 dev %.1e) -- the 1.7e-4 margin is not a float64 "
          "artifact" % (lam_mp, lam_mp_next, abs(lam_mp - lam184)))

    # ---------------- PART D: the inequality itself
    section("D  THE INEQUALITY int p^2 dnu < int p^2 dmu, "
            "deg p < %d" % mz["Nw"])
    ok_mono = True
    worst_q = 0.0
    for k in range(0, 11):
        qn = float(np.sum(mz["vn"] * mz["yn"] ** (2 * k)))
        qm = float(np.sum(mz["wp"] * mz["xp"] ** (2 * k)))
        ok_mono = ok_mono and (qn < qm)
        worst_q = max(worst_q, qn / qm)
    check("D1-monomials", ok_mono,
          "p = x^k, k = 0..10 (direct weighted sums): "
          "int p^2 dnu < int p^2 dmu on all; worst ratio %.6f"
          % worst_q)
    a, b, h0 = mu_chain(mz["xp"], mz["wp"], mz["Nw"])
    B = b_matrix(a, b, h0, mz["yn"], mz["vn"], mz["Nw"])
    rng = np.random.default_rng(RAND_SEED)
    A = rng.standard_normal((N_RAND, mz["Nw"]))
    num = np.sum((A @ B.T) ** 2, axis=1)   # int p^2 dnu
    den = np.sum(A ** 2, axis=1)           # int p^2 dmu
    ratios = num / den
    check("D2-random-polys", bool(np.all(ratios < 1.0)),
          "%d random polynomials of degree < %d in the "
          "mu-orthonormal basis: max ratio (int p^2 dnu)/"
          "(int p^2 dmu) = %.6f < 1"
          % (N_RAND, mz["Nw"], float(np.max(ratios))))
    check("D3-sharpness", abs(float(np.max(ratios)) <= lam184)
          or float(np.max(ratios)) <= lam184 + 1e-12,
          "every ratio <= lambda_max(E_184) = %.6f (the sup over "
          "all polynomials; random sampling max %.6f)"
          % (lam184, float(np.max(ratios))))

    # ---------------- optional: the 42-window ladder
    if args.ladder:
        section("L  THE FULL FAMILY (42 admissible windows, "
                "standalone)")
        kzs = admissible_indices()
        margins = {}
        for kz in kzs:
            m2 = build_measures(kz)
            lam, _ = lam_max_at(m2, m2["Nw"])
            margins[kz] = 1.0 - lam
            print("    kz=%-4d z=%-6d S=%-5d N_w=%-4d "
                  "1-lambda_max = %+.4e"
                  % (kz, int(PP[kz]), m2["S"], m2["Nw"],
                     margins[kz]), flush=True)
        mn = min(margins.values())
        check("L1-ladder", len(kzs) == 42
              and all(v > 0.0 for v in margins.values()),
              "42 admissible windows, ALL margins positive; "
              "min margin %.4e at kz=%d"
              % (mn, min(margins, key=margins.get)))

    # ---------------- result
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n" + "=" * 72)
    print("RESULT: %d/%d gates PASS" % (npass, len(CHECKS)))
    if npass == len(CHECKS):
        print("LSTAR INSTANCE VERIFIED")
    else:
        print("LSTAR INSTANCE **NOT** VERIFIED -- the document "
              "definition and the campaign object DISAGREE; "
              "fix lstar_problem.tex before circulating.")
    print("NO RH CLAIM in either direction.")
    print("=" * 72)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
