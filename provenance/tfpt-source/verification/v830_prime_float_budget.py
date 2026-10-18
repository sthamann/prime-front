#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v830 -- PRIME.FLOOR.BUDGET.01: the rigorous Higham-linear float budget closes the citation-grade family gate at FULL sieve depth (alpha* ~ 11 was an artifact of the frozen quadratic convention), and the certified family sum acquires its exact closed form with the envelope constant made explicit (c_cert = 4.335) -- the remaining proof blocker typed honestly, ONE module from two probes (10/10 + 19 checks with the FIVE preregistered-honest asymptotic FAILs A7/A8/A9/A10/S2.EXP; discovery probes prime_float_budget_probe.py BUDGET-LINEAR-CLOSES-ALL and prime_envelope_analytic_probe.py ENVELOPE-ASYMPTOTIC-PARTIAL, 2026-08-07, re-run identically at promotion).  PART 1, THE BUDGET (v829's named blocker removed): the deployed v818 float convention eps_f = 100 eps |A2|_F^2 is QUADRATIC in the norm (calibrated on the old ladder at |A2| ~ 300; at the deep rungs |A2| ~ 1.3e5 it reaches 1.7e-4 while the true zero-tail term is 4.3e-8).  The frozen replacement is a fully explicit Higham-grade norm-LINEAR chain (Accuracy & Stability ch. 3-4): compensated banded accumulation with bincount partials bounded to N_SUB = 2^16 contributions and TwoSum (Knuth) folding (gC = (2^16+32) eps), the irreducible atom-position term eps X/D on the accumulated tent mass, explicit per-contribution constants C_ATOM = C_T = 8, GL-96 |integrand| quadrature bounds, exact fsum dots, and dps-40 mpmath spot anchoring of the components (caps a factor >= 10 above the measured spot deviations, C_SPOT = 10) -- per-rung budgets 7x (X = 18.375) to 171x (X = 25.5) TIGHTER than the quadratic blanket, growing with depth exactly as diagnosed.  THE RE-CERTIFICATION (frozen deep reference, gates recomputed here): the citation-grade family gate pert_new < cert100 - dcert closes 6/6 deep rungs (old convention: 3/6) -- CITATION GRADE NOW EXTENDS TO alpha = 12.75, FULL SIEVE DEPTH; lambda_min(A2 - M2) becomes float-resolvable on 1/6 (was 0/6).  CONVENTION NOTE (the deliverable): the deployed v818 convention stays FROZEN in the existing suite; the Higham-linear budget above is registered as the convention for NEW modules only.  PART 2, THE ANALYTIC ENVELOPE (run near-verbatim, ~1 min): the certified family sum is EXACT at every finite h in Dirichlet closed form -- X(gamma) = 2 sqrt(w)[S_1 p_2 - S_2 p_1], w = D csinc^2(gamma D/2) -- reproducing the component-based certified sums on ALL 73 battery frames (67 v818 rungs + 6 deep tower rungs) at rel 3.6e-11; the algebra of the asymptotic is sympy-PROVEN (the Piece-2 identity, the large-u law, the deep-alpha law 192 pi^4 (4 gamma^2 + 1)/gamma^2, the alias-weight cancellation sin^2(pi m + d/2) == sin^2(d/2)); the pole-leg and pair limits verify numerically (A5/A6, 1/h rate exact); PHASE CONSPIRACY EXCLUDED: the family-sum dip floor over 1076 alphas is 0.170 >> 0.03 (the SOS over 22491 zeros never conspires to near-zero); and THE EXPLICIT CERTIFIED ENVELOPE: rho >= rho_certfam >= c_cert h^{-3/2} with c_cert = 4.335 holds on 73/73 points with the certified envelope non-decaying (slope +0.199) -- the contract constant made explicit on the certified route.  THE PROOF BLOCKER (the five expected FAILs, typed): the random-phase alias law E[X^2|cell m] ~ 1/m^2 predicts tau ~ h^{-1} but the D = 1/64 tower measures tau_zero ~ h^{-2.5} (A9) and the alias-cell census carries phase correlations the random-phase model misses (A7/A8/A10, S2.EXP: predicted rho ~ h^{-0.58} vs measured h^{-1.36}) -- the asymptotic derivation reaches PARTIAL: exponent/constant derived at the alias level, uniformity blocked by alias phase correlations; the envelope stands CERTIFIED-EXPLICIT, not proven.  Controls fire (exact-bin re-enumeration margins 3.5e4-8.6e4x inside the gC budget; |A2_fsum - A2_plain| <= dA2; the old-budget regression reproduces the cited table and closure set {1176, 1326, 1414}; the seed-7 scramble still refused at -3.8e3).  Feeds PRIME.FLOOR.RATIO.01 [O] (the alpha-coverage caveat of v829 removed at citation grade; the envelope now carries an explicit certified constant; the proof blocker named).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes prime_float_budget_probe.py (2026-08-07,
10/10 checks, ~18 min incl. the 1010-s instrumented sieve to 1.19e11,
verdict BUDGET-LINEAR-CLOSES-ALL) and prime_envelope_analytic_probe.py
(2026-08-07, 19 checks with the FIVE preregistered-honest asymptotic
FAILs A7.ALIAS / A8.HLAW / A9.TOWER / A10.SHAPE / S2.EXP, ~1 min,
verdict ENVELOPE-ASYMPTOTIC-PARTIAL); both re-run identically at
promotion (logs in experiments/tfpt-discovery/).  DOWNSCOPING
(predeclared): part 1 re-runs the complete instrumented budget
pipeline live at the first deep rung X = 18.375 (compensated sieve,
parity ward at M = 896, budget terms, mpmath spot anchors, citation
gate, resolvability, exact-bin + fsum + regression + scramble
controls) and carries the five deeper rungs as FROZEN REFERENCE with
the closure gates recomputed; part 2 runs near-VERBATIM (zero-side,
no sieve): the sympy algebra, the 73-frame closed-form ward, the
numeric limit wards with their five expected FAILs, the phase scan
and the certified-envelope ward, with only the A9 tower thinned
h = 588..816 step 12 (the fit is unchanged; predeclared).  The deep
tower frames enter by their frozen cited normalizations exactly as in
the probe.  Original probe docstrings and frozen protocols live in
the two probe files verbatim.

FIREWALL: v563 / v755 / v823 / v824 / v825 / v829 READ-ONLY; mpmath
VALUES only; NO zetazero()/nzeros() calls in this module
(AST-checked); zero values used openly (on-line by computation
<= 2e4 via the v823 RS scan; citation horizon 3e12 Platt-Trudgian in
the tail chain); RNG only in the declared scramble control (seed 7).
NO RH claim.
"""
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v823_prime_lagrange_floor as pp         # noqa: E402 (READ-ONLY)
import v824_prime_floor_skeleton as ft         # noqa: E402 (READ-ONLY)
import v825_prime_exclusion_ladder as xl       # noqa: E402 (READ-ONLY)
import v829_prime_floor_depth as fd            # noqa: E402 (READ-ONLY)
from mpmath import mp, mpf, mpc, expj as mexpj, exp as mexp, \
    sin as msin, sqrt as msqrt, re as mre      # noqa: E402 (VALUES)

T0 = time.time()
FAILS = []
N_CHK = 0
fsum = math.fsum

# ------------------------------------------------- frozen bars / constants
EPS = float(np.finfo(float).eps)
N_SUB = 1 << 16
G_C = (N_SUB + 32) * EPS
C_ATOM = 8.0
C_T = 8.0
G_Q = 400.0 * EPS
C_SPOT = 10.0
MP_DPS = 40
RES_FAC = 2.0
K_FAM = ft.K_FAM
T_VER = 3.0e12
DGRID = fd.DGRID
SEED_SCRAMBLE = 7
CHAIN_FAC_OLD = 100.0
REG_TOL = 2.0e-2
# frozen regression targets at the live rung (prime_family_depth):
CITED_1176 = dict(rho=1.959e-3, cert=1.52e-1, lam_r=2.81e-7,
                  pert_o=2.47e-3, epsf_o=3.22e-7, tail=2.77e-9)
# FROZEN DEEP REFERENCE (float-budget probe, 2026-08-07):
# M -> (alpha, dfloat = dA2+dM2, epsf_old, pert_new, cert100, dcert,
#       close_old, close_new, resolvable)
BUDGET_REF = {
    1176: (9.19, 4.33e-8, 3.22e-7, 3.50e-4, 1.52e-1, 3.17e-10,
           True, True, True),
    1326: (10.36, 1.21e-7, 2.56e-6, 2.75e-3, 2.98e-1, 7.28e-10,
           True, True, False),
    1414: (11.05, 2.24e-7, 8.62e-6, 9.22e-3, 4.49e-1, 6.20e-10,
           True, True, False),
    1504: (11.75, 4.19e-7, 2.98e-5, 3.19e-2, 7.27e-1, 1.30e-9,
           False, True, False),
    1588: (12.41, 7.52e-7, 9.50e-5, 1.02e-1, 1.21e0, 2.12e-9,
           False, True, False),
    1632: (12.75, 1.02e-6, 1.74e-4, 1.86e-1, 1.62e0, 4.09e-9,
           False, True, False),
}
# part-2 constants (envelope-analytic probe, frozen protocol):
CF_BAR = 1.0e-5
CITED_BAR = 2.0e-2
PAIR_CITED_BAR = 5.0e-2
LIM_H = 1 << 15
LIM_ALPHA = 4.489
A5_REL, A5_KCONS = 5.0e-3, 1.0e-3
A6_DEV, A6_RATIO = 0.10, (1.5, 2.5)
A7_SLOPE, A7_COUNT = 0.40, 0.20
A7_M_RANGE, A7_MIN_CELL = (2, 45), 8
A8_HS = (512, 1024, 2048, 4096, 8192, 16384)
A8_EXP = 0.10
A9_SLOPE = (-1.35, -0.65)
A9_STEP = 12                          # thinned (predeclared)
A10_ALPHA_MIN, A10_KSLOPE, A10_R2 = 4.5, 0.25, 0.85
ENV_SLOPE_MIN = -0.02
PHASE_H, PHASE_N = 512, 1076
PHASE_RANGE = (2.0, 12.75)
PHASE_FLOOR = 0.03
C_CONTRACT = 4.85
C_CERT_REF = 4.335                    # frozen (73-point minimum)
DEEP_MS = (1176, 1326, 1414, 1504, 1588, 1632)
CITED_DEEP = {
    1176: dict(rho=1.959e-3, cert=1.52e-1, rho_cf=1.915e-3,
               rho_cp=4.876e-5),
    1326: dict(rho=1.773e-3, cert=2.98e-1, rho_cf=1.733e-3,
               rho_cp=3.243e-5),
    1414: dict(rho=1.684e-3, cert=4.49e-1, rho_cf=1.645e-3,
               rho_cp=1.765e-5),
    1504: dict(rho=1.683e-3, cert=7.27e-1, rho_cf=1.646e-3,
               rho_cp=2.502e-6),
    1588: dict(rho=1.770e-3, cert=1.21e0, rho_cf=1.735e-3,
               rho_cp=4.378e-6),
    1632: dict(rho=1.855e-3, cert=1.62e0, rho_cf=1.820e-3,
               rho_cp=1.830e-5),
}
EXPECTED_FAILS_P2 = ("A7.ALIAS", "A8.HLAW", "A9.TOWER", "A10.SHAPE",
                     "S2.EXP")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ols_loglog(x, y):
    lx = np.log(np.asarray(x, float))
    ly = np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


# --------------------------------------- compensated banded accumulation
def twosum_add(c, e, x):
    s = c + x
    b = s - c
    e += (c - (s - b)) + (x - b)
    c[:] = s


def tent_accumulate_comp(st, Mpad, D, u, mu, chunk=4000000,
                         nsub=N_SUB):
    assert float(u.min(initial=np.inf)) > D or u.size == 0
    c, e, Tm = st["c"], st["e"], st["T"]
    for s in range(0, u.size, chunk):
        uu, mm = u[s:s + chunk], mu[s:s + chunk]
        i0 = np.floor(uu / D).astype(np.int64)
        for off in (-2, -1, 0, 1, 2):
            idx = i0 + off
            ok = (idx >= 0) & (idx < Mpad)
            if not ok.any():
                continue
            v = 1.0 - np.abs(idx[ok] * D - uu[ok]) / D
            pos = v > 0.0
            if not pos.any():
                continue
            ii = idx[ok][pos]
            ww = mm[ok][pos] * 0.5 * v[pos]
            tt = mm[ok][pos] * 0.5
            for s2 in range(0, ii.size, nsub):
                part = np.bincount(ii[s2:s2 + nsub],
                                   weights=ww[s2:s2 + nsub],
                                   minlength=Mpad)
                twosum_add(c, e, -part)
            Tm += np.bincount(ii, weights=tt, minlength=Mpad)


def sieve_comp(M):
    """Compensated + instrumented sieve to e^{M D} (single band)."""
    nmax = xl.nmax_of_M(M)
    st = dict(c=np.zeros(M + 3), e=np.zeros(M + 3),
              T=np.zeros(M + 3))
    cnt = 0
    masses = []
    bp = xl.base_primes(int(math.isqrt(nmax)))
    for lo in range(0, nmax + 1, xl.SEG_ASC):
        hi = min(lo + xl.SEG_ASC, nmax + 1)
        sv = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            sv[:2] = False
        for p in bp:
            p = int(p)
            stt = max(p * p, ((lo + p - 1) // p) * p)
            if stt < hi:
                sv[stt - lo::p] = False
        nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
        if nn.size == 0:
            continue
        lgn = np.log(nn)
        mu = 2.0 * lgn / np.sqrt(nn)
        tent_accumulate_comp(st, M + 3, DGRID, lgn, mu)
        cnt += int(nn.size)
        masses.append(mu.copy())
    for p in bp:
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= nmax:
            u1 = np.array([math.log(q)])
            m1 = np.array([2.0 * lp / math.sqrt(q)])
            tent_accumulate_comp(st, M + 3, DGRID, u1, m1)
            cnt += 1
            masses.append(m1.copy())
            q *= p
    return st, cnt, np.concatenate(masses), nmax


# ------------------------------------------------ arch |integrand| bound
_GX96, _GW96 = np.polynomial.legendre.leggauss(ft.GL_FINE)


def arch_A_abs(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        s = sv[far].reshape(-1, 1)
        acc = np.zeros(s.shape[0])
        for lo, hi in ((s - D, s), (s, s + D)):
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96[None, :]
            val = np.abs((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
                         / (-np.expm1(-2.0 * w)))
            acc += half[:, 0] * (val @ _GW96)
        out[far] = acc
    for i in np.nonzero(~far)[0]:
        s = float(sv[i])
        tri_s = max(0.0, 1.0 - s / D)
        W = s + D
        pts = sorted({0.0, s, D - s, W})
        pts = [p for p in pts if 0.0 <= p <= W]
        tot = 0.0
        for lo, hi in zip(pts[:-1], pts[1:]):
            if hi <= lo:
                continue
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96
            tri = np.maximum(0.0, 1.0 - np.abs(s - w) / D)
            trr = np.maximum(0.0, 1.0 - np.abs(s + w) / D)
            val = np.abs((tri_s * np.exp(-2.0 * w)
                          - 0.5 * (tri + trr) * np.exp(-0.5 * w))
                         / (-np.expm1(-2.0 * w)))
            tot += half * float(np.dot(_GW96, val))
        out[i] = (abs(core.EULER + core.LOG_PI) * tri_s + 2.0 * tot
                  + tri_s * abs(-math.log1p(-math.exp(-2.0 * W))))
    return out


def wabs_of(f):
    fa = np.abs(f)
    ac = np.correlate(fa, fa, "full")[len(f) - 1:]
    w = 2.0 * ac
    w[0] = ac[0]
    return w


def fsum_dot(x, y):
    return fsum((x * y).tolist())


# ---------------------------------------------------- mpmath anchoring
def mp_zero_legs(f1, f2, D, Mz, g):
    mp.dps = MP_DPS
    Dm = mpf(D)
    gm = mpf(repr(float(g)))
    q = mexpj(Dm * gm)
    ph = mpc(1, 0)
    F1 = mpc(0, 0)
    F2 = mpc(0, 0)
    for j in range(Mz):
        F1 += mpf(repr(float(f1[j]))) * ph
        F2 += mpf(repr(float(f2[j]))) * ph
        ph *= q
    rot = mexpj(-(Mz - 1) * Dm * gm / 2) * mpc(0, "0.5")
    hw = Dm * gm / 2
    wg = Dm * (msin(hw) / hw) ** 2
    sq = 2 * msqrt(wg)
    return float(sq * mre(rot * F1)), float(sq * mre(rot * F2))


def mp_pole_legs(f1, f2, D, Mz):
    mp.dps = MP_DPS
    Dm = mpf(D)
    qd = mexp(-Dm / 2)
    qg = mexp(Dm / 2)
    pd = mpf(1)
    pg = mpf(1)
    Fp = {"1": mpf(0), "2": mpf(0)}
    Fm = {"1": mpf(0), "2": mpf(0)}
    for j in range(Mz):
        c1 = mpf(repr(float(f1[j])))
        c2 = mpf(repr(float(f2[j])))
        Fp["1"] += c1 * pd
        Fp["2"] += c2 * pd
        Fm["1"] += c1 * pg
        Fm["2"] += c2 * pg
        pd *= qd
        pg *= qg
    cs = (mexp(Dm / 4) - mexp(-Dm / 4)) / 2 / (Dm / 4)
    pref = cs * cs * Dm / 2
    P = {}
    for (i, j), (fa, fb) in {(0, 0): ("1", "1"), (1, 1): ("2", "2"),
                             (0, 1): ("1", "2")}.items():
        P[(i, j)] = P[(j, i)] = -pref * (Fp[fa] * Fm[fb]
                                         + Fp[fb] * Fm[fa])
    mid = (P[(0, 0)] + P[(1, 1)]) / 2
    rad = msqrt(((P[(0, 0)] - P[(1, 1)]) / 2) ** 2 + P[(0, 1)] ** 2)
    lmax = mid + rad
    v0, v1 = P[(0, 1)], lmax - P[(0, 0)]
    nrm = msqrt(v0 * v0 + v1 * v1)
    sq = msqrt(lmax if lmax > 0 else mpf(0))
    return float(sq * v0 / nrm), float(sq * v1 / nrm)


# ---------------------------------------- tail-probe machinery (verbatim)
def S_closed_c(k, h, phi):
    N = 2 * h + 1
    om = 2.0 * math.pi * k / N
    out = np.zeros_like(phi, dtype=complex)
    for sgn in (1.0, -1.0):
        s = om + sgn * phi
        c = om - sgn * (h - 0.5) * phi
        out += sgn * (np.cos(c + 0.5 * s * (h - 1.0))
                      * np.sin(0.5 * h * s) / np.sin(0.5 * s))
    return out / math.sqrt(N)


def q_rvm(t):
    return 0.112 * math.log(t) + 0.278 * math.log(math.log(t)) + 3.4


def sh_sum(T):
    main = (math.log(T / (2.0 * math.pi)) + 1.0) \
        / (2.0 * math.pi * T)
    return main + (2.0 * q_rvm(T) + 0.2) / (T * T)


def num_sup(h, D, delta_max, n_u=65536, n_delta=33):
    u = (np.arange(n_u) + 0.31) * (4.0 * math.pi / n_u)
    dl = np.linspace(0.0, delta_max, n_delta)
    phi = u[None, :] + 1j * (D * dl)[:, None]
    s1 = np.abs(S_closed_c(1, h, phi))
    s2 = np.abs(S_closed_c(2, h, phi))
    pref = (np.sin(0.5 * u[None, :]) ** 2
            + np.sinh(0.5 * D * dl)[:, None] ** 2)
    return float(np.max(pref * 4.0 * np.maximum(
        np.maximum(s1 * s1, s2 * s2), s1 * s2))) * 1.35


def pert_of(env, s1n):
    return env * s1n + 2.0 * env * env


# ------------------------------------- part-2 closed forms (verbatim)
def s_vec(k, h, phi):
    out = S_closed_c(k, h, np.asarray(phi, dtype=complex))
    outr = np.real(out)
    bad = ~np.isfinite(outr)
    if bad.any():
        for i in np.nonzero(bad)[0]:
            outr[i] = ft.S_closed(k, h, 1.0, float(phi[i]))
    return outr


def fam_closed(h, D, gam):
    phi = D * gam
    wg = D * np.real(fd.csinc(np.asarray(phi, complex) / 2.0) ** 2)
    S1 = s_vec(1, h, phi)
    S2 = s_vec(2, h, phi)
    rt = 2.0 * np.sqrt(np.maximum(wg, 0.0))
    av, bv = rt * S1, rt * S2
    jj = np.arange(h)
    ee = np.sinh((h - jj - 0.5) * D / 2.0)
    sp1 = float(ft.parity_t(1, h) @ ee)
    sp2 = float(ft.parity_t(2, h) @ ee)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * sp1, cp * sp2
    Xv = av * p2 - bv * p1
    return Xv, av, bv, p1, p2


def m2_closed(h, D, gam):
    Xv, av, bv, p1, p2 = fam_closed(h, D, gam)
    M2 = np.array([[float(av @ av) + p1 * p1,
                    float(av @ bv) + p1 * p2],
                   [float(av @ bv) + p1 * p2,
                    float(bv @ bv) + p2 * p2]])
    lam, tau = fd.eig2(M2)
    return Xv, M2, lam, tau


def shape_of(h, D):
    m_max = int(math.floor(2.0e4 * D / (2.0 * math.pi)))
    if m_max < 1:
        return float("nan")
    mm = np.arange(1, m_max + 1, dtype=float)
    return (2.0 / (math.pi ** 2 * (2 * h + 1))) \
        * float(np.sum(np.log(mm / D) / mm ** 2))


def gp_k(k, al):
    return math.pi * k * math.sinh(al / 2.0) \
        / (math.pi ** 2 * k * k + al * al / 4.0)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v830 -- PRIME.FLOOR.BUDGET.01: the Higham-linear float "
          "budget + the analytic envelope")
    print("(two probes: BUDGET-LINEAR-CLOSES-ALL + ENVELOPE-"
          "ASYMPTOTIC-PARTIAL with the five")
    print(" expected asymptotic FAILs; downscoping predeclared in "
          "PROVENANCE; NO RH claim)")
    print("=" * 78)

    # ============================================= PART 1: the budget
    print("\nP1 -- the frozen budget live at X = 18.375 (compensated "
          "instrumented sieve)")
    check("P1.AST no zeta-zero generator call in this module",
          xl.ast_zero_firewall(__file__))
    gam, n_rvm = pp.zero_list()
    check("P1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    n_z = len(gam)
    # parity ward at M = 896 (compensated path vs deployed)
    n_pw = xl.nmax_of_M(896)
    lam_tab = core.von_mangoldt_table(n_pw)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_pw = np.log(nn0.astype(float))
    mu_pw = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    c_slow, _ = core.atom_lags_at(0.5 * 896 * DGRID, 896, u_pw,
                                  mu_pw)
    st_pw, cnt_pw, _, _ = sieve_comp(896)
    dev_pw = float(np.max(np.abs(
        (st_pw["c"] + st_pw["e"])[:896] - c_slow)))
    check("P1.PARITY compensated banded assembly == deployed T115 "
          "path at M = 896 (%d atoms): max |dc| = %.2e <= 5e-9"
          % (cnt_pw, dev_pw),
          cnt_pw == len(u_pw) and dev_pw <= 5.0e-9)

    st, cnt, masses_scr, nmax = sieve_comp(1176)
    c_at = (st["c"] + st["e"])[:1176]
    dw = fd.deep_window(1176, c_at)
    cc = dw["c_ar"] + dw["c_at"]
    A2f = np.empty((2, 2))
    A2p = np.empty((2, 2))
    for (i, j), W in {(0, 0): dw["W11"], (1, 1): dw["W22"],
                      (0, 1): dw["W12"]}.items():
        A2f[i, j] = A2f[j, i] = fsum_dot(cc, W)
        A2p[i, j] = A2p[j, i] = float(cc @ W)
    lamA, tauA = fd.eig2(A2f)
    wd = dict(f1=fd.odd_ext(dw["t1"], 1176),
              f2=fd.odd_ext(dw["t2"], 1176), D=DGRID, M=1176, h=588)
    a, b, meta = pp.components_of(wd, gam)
    wg = meta["wg"]
    x_pz = a[:-1] * b[-1] - b[:-1] * a[-1]
    order = np.argsort(x_pz ** 2)[::-1]
    cert = fsum((x_pz[order[:K_FAM]] ** 2).tolist())
    M2 = np.array([[fsum_dot(a, a), fsum_dot(a, b)],
                   [fsum_dot(a, b), fsum_dot(b, b)]])
    lam_r = ft.eig2_min(A2f - M2)
    rho = tauA / fd.eig2(np.array(
        [[dw["c_ar"] @ dw["W11"], dw["c_ar"] @ dw["W12"]],
         [dw["c_ar"] @ dw["W12"], dw["c_ar"] @ dw["W22"]]])
        - fd.pnt_S_of(*fd.pnt_cells(
            dw["W11"], dw["W22"], dw["W12"], DGRID, 1176,
            1176 * DGRID + 1e-9,
            2.0 * math.log(5.3722 / 4.0)), 1176 * DGRID))[1]

    # mpmath spot anchoring (predeclared density)
    sf1 = fsum(np.abs(wd["f1"]).tolist())
    sf2 = fsum(np.abs(wd["f2"]).tolist())
    acap = np.sqrt(np.maximum(wg, 0.0)) * sf1
    bcap = np.sqrt(np.maximum(wg, 0.0)) * sf2
    spots = sorted(set([int(k) for k in order[:4]] + [0]
                       + [n_z // 8, n_z // 4, n_z // 2,
                          (3 * n_z) // 4]))
    spot_z, spot_p = 0.0, 0.0
    for k in spots:
        am, bm = mp_zero_legs(wd["f1"], wd["f2"], DGRID, 1176,
                              gam[k])
        spot_z = max(spot_z, abs(am - a[k]) / max(acap[k], 1e-300),
                     abs(bm - b[k]) / max(bcap[k], 1e-300))
    vp0m, vp1m = mp_pole_legs(wd["f1"], wd["f2"], DGRID, 1176)
    if vp0m * a[-1] + vp1m * b[-1] < 0.0:
        vp0m, vp1m = -vp0m, -vp1m
    nvp = math.hypot(a[-1], b[-1])
    spot_p = max(abs(vp0m - a[-1]) / nvp, abs(vp1m - b[-1]) / nvp)
    c_absF = max(C_SPOT * spot_z, 1176 * EPS)
    c_pole = max(C_SPOT * spot_p, 1176 * EPS)
    print("    spot anchors (%d zero + 1 pole): zero %.2e, pole "
          "%.2e; caps c_absF = %.2e, c_pole = %.2e"
          % (len(spots), spot_z, spot_p, c_absF, c_pole))

    # the budget terms at the live rung
    S_abs = np.abs(dw["c_at"])
    Tm = st["T"][:1176]
    A_abs = arch_A_abs(np.arange(1176) * DGRID, DGRID)
    C_abs = S_abs + np.abs(dw["c_ar"])
    cc_abs = np.abs(cc)
    wab1 = wabs_of(wd["f1"])
    wab2 = wabs_of(wd["f2"])
    wabp = wabs_of(wd["f1"] + wd["f2"])
    wab12 = 0.5 * (wabp + wab1 + wab2)
    dA2 = {}
    for (i, j), (W, wab) in {(0, 0): (dw["W11"], wab1),
                             (1, 1): (dw["W22"], wab2),
                             (0, 1): (dw["W12"], wab12)}.items():
        Wa = np.abs(W)
        t_sum = G_C * float(S_abs @ Wa)
        t_read = (EPS * 18.375 / DGRID + C_ATOM * EPS) \
            * float(Tm @ Wa)
        t_arch = G_Q * float(A_abs @ Wa)
        t_w = (1176 + C_T) * EPS * float(C_abs @ wab)
        t_dot = EPS * float(cc_abs @ Wa) + EPS * abs(A2f[i, j])
        dA2[(i, j)] = t_sum + t_read + t_arch + t_w + t_dot
    dA2_max = max(dA2.values())
    Ea = np.concatenate([c_absF * acap, [c_pole * abs(a[-1])]])
    Eb = np.concatenate([c_absF * bcap, [c_pole * abs(b[-1])]])
    aa, bb = np.abs(a), np.abs(b)
    dM2 = {}
    for (i, j), (x, y, Ex, Ey) in {(0, 0): (aa, aa, Ea, Ea),
                                   (1, 1): (bb, bb, Eb, Eb),
                                   (0, 1): (aa, bb, Ea, Eb)}.items():
        gabs = fsum_dot(x, y)
        dM2[(i, j)] = fsum_dot(x, Ey) + fsum_dot(y, Ex) \
            + 4.0 * EPS * gabs
    dM2_max = max(dM2.values())
    ap, bp = abs(a[-1]), abs(b[-1])
    idx = order[:K_FAM]
    dx = (bp * Ea[idx] + aa[idx] * Eb[-1] + ap * Eb[idx]
          + bb[idx] * Ea[-1]
          + 4.0 * EPS * (aa[idx] * bp + bb[idx] * ap))
    xk = np.abs(x_pz[idx])
    dcert = fsum((2.0 * xk * dx + dx * dx).tolist()) + EPS * cert
    epsf_old = CHAIN_FAC_OLD * EPS * float(np.linalg.norm(A2f)) ** 2
    dfloat = dA2_max + dM2_max
    print("    live budget: dA2 = %.2e, dM2 = %.2e, dcert = %.2e, "
          "epsf_old = %.2e (ratio %.0fx)"
          % (dA2_max, dM2_max, dcert, epsf_old, epsf_old / dfloat))
    check("P1.LINEAR the new budget is norm-linear at the live rung: "
          "dfloat = %.2e < epsf_old = %.2e (x%.0f tighter; frozen "
          "reference x7)" % (dfloat, epsf_old, epsf_old / dfloat),
          dfloat < epsf_old and epsf_old / dfloat >= 4.0)

    # the citation gate + resolvability live
    s1n = (abs(A2f[0, 0]) + abs(A2f[1, 1]) + 2.0 * abs(A2f[0, 1]))
    num_c = num_sup(588, DGRID, 0.5)
    tail_term = (4.0 / DGRID) * num_c * sh_sum(T_VER)
    dc = ft.arch_A_fine(np.arange(1176) * DGRID, DGRID) \
        - np.asarray(core.arch_lags(1176, DGRID), float)
    eps_arch = ft.ARCH_SLACK * max(
        abs(float(dc @ dw["W11"])), abs(float(dc @ dw["W22"])),
        abs(float(dc @ dw["W12"])))
    pert_old = pert_of(tail_term + epsf_old, s1n)
    pert_new = pert_of(tail_term + eps_arch + dfloat, s1n) \
        * (1.0 + 1e-10)
    gate = cert - dcert
    res_bud = RES_FAC * dfloat
    check("P1.GATE the citation-grade family gate live: pert_new = "
          "%.2e < cert100 - dcert = %.2e (old pert %.2e also "
          "closes at this alpha); lambda_min(A2 - M2) = %.2e > "
          "%.2e -- float-RESOLVABLE under the linear budget (it was "
          "NOT under the quadratic blanket)"
          % (pert_new, gate, pert_old, lam_r, res_bud),
          pert_new < gate and lam_r > res_bud)
    # regression ward vs the frozen cited table (live rung)
    reg_ok = (abs(rho - CITED_1176["rho"]) / CITED_1176["rho"]
              <= REG_TOL
              and abs(cert - CITED_1176["cert"]) / CITED_1176["cert"]
              <= REG_TOL
              and abs(epsf_old - CITED_1176["epsf_o"])
              / CITED_1176["epsf_o"] <= REG_TOL
              and abs(pert_old - CITED_1176["pert_o"])
              / CITED_1176["pert_o"] <= REG_TOL
              and abs(tail_term - CITED_1176["tail"])
              / CITED_1176["tail"] <= REG_TOL)
    check("P1.REG old-budget regression at the live rung: rho / "
          "cert100 / eps_f_old / pert_old / tail reproduce the "
          "cited table (rel <= %.2f); lambda_min(R) = %.2e vs cited "
          "%.2e" % (REG_TOL, lam_r, CITED_1176["lam_r"]),
          reg_ok
          and abs(lam_r - CITED_1176["lam_r"]) / CITED_1176["lam_r"]
          <= 0.25)

    # controls (live)
    bw_ok = True
    for ib in (1175, (7 * 1176) // 8):
        u_lo, u_hi = (ib - 1) * DGRID, (ib + 1) * DGRID
        a_n = max(2, int(math.floor(math.exp(u_lo))) + 1)
        b_n = min(nmax, int(math.floor(math.exp(u_hi))))
        bp_ = xl.base_primes(int(math.isqrt(b_n)))
        vals = []
        for lo in range(a_n, b_n + 1, xl.SEG_ASC):
            hi = min(lo + xl.SEG_ASC, b_n + 1)
            sv = np.ones(hi - lo, dtype=bool)
            for p in bp_:
                p = int(p)
                stt = max(p * p, ((lo + p - 1) // p) * p)
                if stt < hi:
                    sv[stt - lo::p] = False
            nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
            if nn.size == 0:
                continue
            un = np.log(nn)
            v = 1.0 - np.abs(ib * DGRID - un) / DGRID
            m = v > 0.0
            vals.append((2.0 * un[m] / np.sqrt(nn[m])) * 0.5 * v[m])
        for p in bp_:
            p = int(p)
            q = p * p
            while q <= b_n:
                if q >= a_n:
                    uq = math.log(q)
                    vq = 1.0 - abs(ib * DGRID - uq) / DGRID
                    if vq > 0.0:
                        vals.append(np.array(
                            [2.0 * math.log(p) / math.sqrt(q)
                             * 0.5 * vq]))
                q *= p
        w_all = np.sort(np.concatenate(vals))
        ref = -float(np.sum(w_all))
        got = float(dw["c_at"][ib])
        bud_i = G_C * abs(got)
        bw_ok = bw_ok and abs(got - ref) <= bud_i
    check("P1.CT1 budget wards: exact-bin re-enumerations inside "
          "the gC S_abs budget AND |A2_fsum - A2_plain| = %.1e <= "
          "dA2 = %.1e AND the spot caps a factor >= %.0f above the "
          "measured deviations"
          % (float(np.max(np.abs(A2f - A2p))), dA2_max, C_SPOT),
          bw_ok and float(np.max(np.abs(A2f - A2p))) <= dA2_max
          and c_absF >= C_SPOT * spot_z * (1.0 - 1e-12))
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    xl.tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    ccs = dw["c_ar"] + c_scr
    A2s = np.array([[ccs @ dw["W11"], ccs @ dw["W12"]],
                    [ccs @ dw["W12"], ccs @ dw["W22"]]])
    lam_scr = ft.eig2_min(A2s - M2)
    check("P1.CT3 [must-fire] scramble at M = 1176 (SAME %d masses, "
          "seed %d): lambda_min(A2_scr - M2) = %.3e < 0"
          % (masses_scr.size, SEED_SCRAMBLE, lam_scr), lam_scr < 0.0)

    # the frozen deep reference (gates recomputed)
    print("\nR1 -- THE BUDGET TABLE (frozen deep reference; gates "
          "recomputed)")
    print("  %5s %6s | %9s %9s %6s | %9s %9s | %5s %5s %6s"
          % ("M", "alpha", "dfloat", "epsf_old", "ratio", "pert_new",
             "gate", "old", "new", "resol"))
    for M in sorted(BUDGET_REF):
        al, dfl, efo, pn, c100, dc_, co, cn, rs = BUDGET_REF[M]
        print("  %5d %6.2f | %9.2e %9.2e %6.0f | %9.2e %9.2e | "
              "%5s %5s %6s"
              % (M, al, dfl, efo, efo / dfl, pn, c100 - dc_,
                 "yes" if co else "NO", "YES" if cn else "NO",
                 "yes" if rs else "NO"))
    ratios = [BUDGET_REF[M][2] / BUDGET_REF[M][1]
              for M in sorted(BUDGET_REF)]
    n_new = sum(1 for M in BUDGET_REF if BUDGET_REF[M][7])
    n_old = sum(1 for M in BUDGET_REF if BUDGET_REF[M][6])
    gates_ok = all(BUDGET_REF[M][3] < BUDGET_REF[M][4]
                   - BUDGET_REF[M][5] for M in BUDGET_REF)
    check("R1.CLOSE the citation gate closes %d/6 under the linear "
          "budget (old convention %d/6; pert_new < cert100 - dcert "
          "recomputed on every frozen row); improvement %.0f..%.0fx "
          "GROWING with depth; alpha* ~ 11 was a float-convention "
          "artifact -- citation grade extends to alpha = 12.75, "
          "FULL SIEVE DEPTH => BUDGET-LINEAR-CLOSES-ALL"
          % (n_new, n_old, min(ratios), max(ratios)),
          n_new == 6 and n_old == 3 and gates_ok
          and all(r1 < r2 for r1, r2 in zip(ratios[:-1],
                                            ratios[1:])))
    print("    CONVENTION NOTE (deliverable): the deployed v818 "
          "quadratic convention stays FROZEN in the existing suite; "
          "the Higham-linear budget above is registered as the "
          "convention for NEW modules only.")

    # ============================================= PART 2: the envelope
    print("\nP2 -- the analytic envelope (near-verbatim; the five "
          "asymptotic FAILs are EXPECTED)")
    import sympy as sp
    u, al, g, d = sp.symbols("u alpha gamma delta", positive=True)
    m_i = sp.Symbol("m", integer=True, positive=True)
    G1 = sp.pi * sp.sin(u) / (sp.pi ** 2 - u ** 2)
    G2 = 2 * sp.pi * sp.sin(u) / (4 * sp.pi ** 2 - u ** 2)
    Gp1 = sp.pi * sp.sinh(al / 2) / (sp.pi ** 2 + al ** 2 / 4)
    Gp2 = 2 * sp.pi * sp.sinh(al / 2) / (4 * sp.pi ** 2
                                         + al ** 2 / 4)
    br = (1 / ((sp.pi ** 2 - u ** 2)
               * (4 * sp.pi ** 2 + al ** 2 / 4))
          - 1 / ((4 * sp.pi ** 2 - u ** 2)
                 * (sp.pi ** 2 + al ** 2 / 4)))
    a1 = sp.simplify(8 * al * (G1 * Gp2 - G2 * Gp1)
                     - 16 * al * sp.pi ** 2 * sp.sin(u)
                     * sp.sinh(al / 2) * br)
    check("A1.SYM the Piece-2 identity 8a[G1 Gp2 - G2 Gp1] == "
          "16 a pi^2 sin(u) sinh(a/2)[bracket] (exact algebra)",
          a1 == 0)
    a2 = sp.limit(br * u ** 2, u, sp.oo)
    a2_ref = 3 * sp.pi ** 2 / ((sp.pi ** 2 + al ** 2 / 4)
                               * (4 * sp.pi ** 2 + al ** 2 / 4))
    check("A2.SYM u^2 [bracket] -> 3 pi^2/((pi^2+a^2/4)"
          "(4pi^2+a^2/4)) (large-u law)",
          sp.simplify(a2 - a2_ref) == 0)
    a3 = sp.limit(16 * al ** 6 * sp.pi ** 2 * g ** 2
                  * br.subs(u, al * g), al, sp.oo)
    a3_ref = 192 * sp.pi ** 4 * (4 * g ** 2 + 1) / g ** 2
    check("A3.SYM the deep-alpha law -> 192 pi^4 (4 g^2 + 1)/g^2 "
          "(exact iterated limit)", sp.simplify(a3 - a3_ref) == 0)
    a4 = sp.simplify(sp.expand_trig(
        sp.sin(sp.pi * m_i + d / 2) ** 2) - sp.sin(d / 2) ** 2)
    check("A4.SYM the alias weight sin^2(pi m + d/2) == sin^2(d/2), "
          "m integer (the csinc-null cancellation)", a4 == 0)

    # the 73-point battery (67 v818 rungs + 6 deep tower rungs)
    g1 = float(gam[0])
    t0 = time.time()
    rows = []
    from mpmath import zeta as _zeta, diff as _diff
    c_th = float(-2 * _diff(lambda s: _zeta(s), 0.5) / _zeta(0.5))
    u0 = 2.0 * math.log(-c_th / 4.0)
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        lam, tau = fd.eig2(rr["Ah"])
        edges, reads = fd.pnt_cells(rr["W11"], rr["W22"], rr["W12"],
                                    rr["D"], rr["M"],
                                    2.0 * rr["alpha"] + 1e-9, u0)
        Sp = fd.pnt_S_of(edges, reads, 2.0 * rr["alpha"])
        _, tau_p = fd.eig2(rr["B"] - Sp)
        rows.append(dict(h=rr["h"], M=rr["M"], D=rr["D"],
                         alpha=rr["alpha"], t1=rr["t1"],
                         t2=rr["t2"], lam=lam, tau=tau,
                         tau_pnt=tau_p, rho=tau / tau_p, deep=False))
    rows.sort(key=lambda w: w["alpha"])
    check("S1.SET the deployed 67-rung ladder rebuilt (%d windows, "
          "%.0f s); e1 range [%.2f, %.1f] vs promoted [4.85, 24.2]"
          % (len(rows), time.time() - t0,
             min(w["rho"] * w["h"] ** 1.5 for w in rows),
             max(w["rho"] * w["h"] ** 1.5 for w in rows)),
          len(rows) == 67
          and abs(min(w["rho"] * w["h"] ** 1.5 for w in rows)
                  - 4.85) <= 0.02
          and abs(max(w["rho"] * w["h"] ** 1.5 for w in rows)
                  - 24.2) <= 0.1)
    for M in DEEP_MS:
        h = M // 2
        Tb = core.parity_basis(h, 2)
        ct = CITED_DEEP[M]
        rows.append(dict(h=h, M=M, D=DGRID, alpha=h * DGRID,
                         t1=Tb[0].copy(), t2=Tb[1].copy(),
                         lam=float("nan"), tau=float("nan"),
                         tau_pnt=float("nan"), rho=ct["rho"],
                         deep=True))
    worst_cf, worst_c100 = 0.0, 0.0
    t0 = time.time()
    for w in rows:
        h, D, M = w["h"], w["D"], w["M"]
        Xv, M2z, lamz, tauz = m2_closed(h, D, gam)
        x2 = Xv ** 2
        order_z = np.argsort(x2)[::-1]
        w.update(fam_cf=float(np.sum(x2)),
                 cert_cf=float(np.sum(x2[order_z[:K_FAM]])),
                 x2_g1=float(x2[0]), lam_z=lamz, tau_z=tauz,
                 Xv=Xv)
        wdz = dict(f1=fd.odd_ext(w["t1"], M),
                   f2=fd.odd_ext(w["t2"], M), D=D, M=M)
        az, bz, _ = pp.components_of(wdz, gam)
        x_num = (az[:-1] * bz[-1] - bz[:-1] * az[-1]) ** 2
        fam_num = float(np.sum(x_num))
        c100_num = float(np.sum(np.sort(x_num)[::-1][:K_FAM]))
        worst_cf = max(worst_cf,
                       abs(w["fam_cf"] - fam_num) / fam_num)
        worst_c100 = max(worst_c100,
                         abs(w["cert_cf"] - c100_num) / c100_num)
    print("    closed form vs components on all 73 frames: %.0f s, "
          "worst rel %.1e" % (time.time() - t0,
                              max(worst_cf, worst_c100)))
    check("W1.CF the analytic (Dirichlet closed-form) family "
          "reproduces the component-based certified sums on ALL 73 "
          "frames: worst rel %.1e <= %.0e"
          % (max(worst_cf, worst_c100), CF_BAR),
          max(worst_cf, worst_c100) <= CF_BAR)
    cited_dev, pair_dev = 0.0, 0.0
    for w in rows[67:]:
        ct = CITED_DEEP[w["M"]]
        cited_dev = max(cited_dev,
                        abs(w["cert_cf"] - ct["cert"]) / ct["cert"])
        x2g1_cited = ct["rho_cp"] * ct["cert"] / ct["rho_cf"]
        pair_dev = max(pair_dev,
                       abs(w["x2_g1"] - x2g1_cited) / x2g1_cited)
    check("W1.CITED the deep cert100 reproduce the frozen cited "
          "values (rel %.1e <= %.0e) and the closed-form fixed pair "
          "matches the cited pair chain (rel %.1e <= %.0e)"
          % (cited_dev, CITED_BAR, pair_dev, PAIR_CITED_BAR),
          cited_dev <= CITED_BAR and pair_dev <= PAIR_CITED_BAR)

    # numeric limit wards (A5-A10; the expected FAILs)
    hL, aL = LIM_H, LIM_ALPHA
    DL = aL / hL
    jj = np.arange(hL)
    ee = np.sinh((hL - jj - 0.5) * DL / 2.0)
    cp = 2.0 * math.sqrt(DL) * (math.sinh(DL / 4.0) / (DL / 4.0))
    r_k = [cp * float(ft.parity_t(k, hL) @ ee) / gp_k(k, aL)
           for k in (1, 2)]
    norm = 2.0 * math.sqrt(2.0 * aL)
    a5_rel = max(abs(r / norm - 1.0) for r in r_k)
    a5_kc = abs(r_k[0] - r_k[1]) / abs(r_k[0])
    check("A5.POLE p_k / (2 sqrt(2 alpha)) -> Gp_k(alpha) at h = %d: "
          "rel %.1e <= %.0e, k-consistency %.1e <= %.0e"
          % (hL, a5_rel, A5_REL, a5_kc, A5_KCONS),
          a5_rel <= A5_REL and a5_kc <= A5_KCONS)
    x2_h, _ = ft.pair_x2_closed(aL, hL, g1)
    x2_h2, _ = ft.pair_x2_closed(aL, 2 * hL, g1)
    xi2 = ft.x_inf(aL, g1) ** 2
    dev1 = abs(x2_h / xi2 - 1.0)
    rat = dev1 / max(abs(x2_h2 / xi2 - 1.0), 1e-300)
    check("A6.PAIR X^2 -> X_inf^2 at alpha = %.3f: dev %.1e <= %.1f "
          "and h-doubling ratio %.2f in [%.1f, %.1f] (the 1/h law)"
          % (aL, dev1, A6_DEV, rat, *A6_RATIO),
          dev1 <= A6_DEV and A6_RATIO[0] <= rat <= A6_RATIO[1])
    wD = rows[-1]
    x2D = wD["Xv"] ** 2
    m_idx = np.round(gam * DGRID / (2.0 * math.pi)).astype(int)
    ms, mean_m, cnt_m, cnt_pred = [], [], [], []
    for m in range(A7_M_RANGE[0], A7_M_RANGE[1] + 1):
        sel = m_idx == m
        n_m = int(sel.sum())
        if n_m < A7_MIN_CELL:
            continue
        ms.append(m)
        mean_m.append(float(np.mean(x2D[sel])))
        cnt_m.append(n_m)
        cnt_pred.append(math.log(m / DGRID) / DGRID)
    ms = np.array(ms, float)
    sl_m, _, r2_m = ols_loglog(ms, np.array(mean_m) * ms ** 2)
    cnt_dev = float(np.median(np.abs(np.array(cnt_m, float)
                                     / np.array(cnt_pred) - 1.0)))
    check("A7.ALIAS [EXPECTED FAIL -- the alias phase correlations] "
          "cell-mean X^2 vs the derived 1/m^2 law: fit slope %+.2f "
          "(bar |.| <= %.1f, R^2 %.2f), cell counts median dev %.2f "
          "<= %.1f" % (sl_m, A7_SLOPE, r2_m, cnt_dev, A7_COUNT),
          abs(sl_m) <= A7_SLOPE and cnt_dev <= A7_COUNT)
    f_hs = []
    for h_s in A8_HS:
        Xs, _, _, _, _ = fam_closed(h_s, aL / h_s, gam)
        f_hs.append(float(np.sum(Xs ** 2)))
    sl_f, _, _ = ols_loglog(A8_HS, f_hs)
    check("A8.HLAW [EXPECTED FAIL] F(h, alpha = %.3f) h-exponent "
          "%+.3f (bar |.| <= %.1f)" % (aL, sl_f, A8_EXP),
          abs(sl_f) <= A8_EXP)
    hs_t = list(range(588, 817, A9_STEP))
    tau_t = []
    for h_t in hs_t:
        _, _, lam_t, ta_t = m2_closed(h_t, DGRID, gam)
        tau_t.append(ta_t)
    sl_t, _, r2_t = ols_loglog(hs_t, tau_t)
    check("A9.TOWER [EXPECTED FAIL -- THE PROOF BLOCKER] tau_zero on "
          "the D = 1/64 tower (h = 588..816, %d frames): fit slope "
          "%+.3f vs the derived random-phase -1 (bar [%.2f, %.2f], "
          "R^2 %.2f) -- the tower decays h^{-2.5}, the alias phases "
          "are NOT random" % (len(hs_t), sl_t, *A9_SLOPE, r2_t),
          A9_SLOPE[0] <= sl_t <= A9_SLOPE[1])
    for w in rows:
        w["shape"] = shape_of(w["h"], w["D"])
        w["tau_eff"] = (w["tau"] if not w["deep"] else w["tau_z"])
    sub73 = [w for w in rows if w["alpha"] >= A10_ALPHA_MIN]
    kap = [w["tau_eff"] / w["shape"] for w in sub73]
    sl_k, _, _ = ols_loglog([w["h"] for w in sub73], kap)
    lt = np.log([w["tau_eff"] for w in sub73])
    lp_ = np.log([np.median(kap) * w["shape"] for w in sub73])
    r2_s = 1.0 - float(np.sum((lt - lp_) ** 2)) \
        / float(np.sum((lt - lt.mean()) ** 2))
    check("A10.SHAPE [EXPECTED FAIL] the derived tau law on the "
          "alpha >= %.1f subset: kappa drift %+.3f (bar |.| <= "
          "%.2f), R^2 %.3f >= %.2f"
          % (A10_ALPHA_MIN, sl_k, A10_KSLOPE, r2_s, A10_R2),
          abs(sl_k) <= A10_KSLOPE and r2_s >= A10_R2)
    tp_pts = [w for w in rows if not w["deep"]]
    sl_tp, _, _ = ols_loglog([w["h"] for w in tp_pts],
                             [w["tau_pnt"] for w in tp_pts])
    sl_rho_meas, _, _ = ols_loglog([w["h"] for w in tp_pts],
                                   [w["rho"] for w in tp_pts])
    sl_shape, _, _ = ols_loglog([w["h"] for w in tp_pts],
                                [w["shape"] for w in tp_pts])
    exp_dev = abs((sl_shape - sl_tp) - sl_rho_meas)
    check("S2.EXP [EXPECTED FAIL] the random-phase decomposition: "
          "predicted rho ~ h^%+.2f vs measured h^%+.2f (|dev| = "
          "%.2f <= 0.15) -- h^{-1} random-phase vs the h^{-2.5} "
          "tower, the blocker restated"
          % (sl_shape - sl_tp, sl_rho_meas, exp_dev),
          exp_dev <= 0.15)

    # the certified envelope + the phase scan (both must PASS)
    for w in rows:
        if w["deep"]:
            w["rho_cert"] = CITED_DEEP[w["M"]]["rho_cf"]
        else:
            bud = 100.0 * EPS * (w["lam"] ** 2 + w["lam_z"] ** 2)
            w["rho_cert"] = (w["cert_cf"] - bud) \
                / (w["lam"] * w["tau_pnt"])
        w["e1_cert"] = w["rho_cert"] * w["h"] ** 1.5
    below = all(w["rho_cert"] <= w["rho"] * (1 + 1e-9) for w in rows)
    c_cert = min(w["e1_cert"] for w in rows)
    sl_e1c, _, _ = ols_loglog([w["h"] for w in rows],
                              [w["e1_cert"] for w in rows])
    check("W3.ENV THE EXPLICIT CERTIFIED ENVELOPE: rho >= "
          "rho_certfam >= c_cert h^{-3/2} with c_cert = %.3f "
          "(frozen %.3f, |dev| <= 0.01) holds on 73/73 points "
          "(rho_cert <= rho everywhere: %s), non-decaying (slope "
          "%+.3f >= %.2f) -- the contract constant c = %.2f made "
          "explicit on the certified route"
          % (c_cert, C_CERT_REF, "yes" if below else "NO", sl_e1c,
             ENV_SLOPE_MIN, C_CONTRACT),
          below and abs(c_cert - C_CERT_REF) <= 0.01
          and sl_e1c >= ENV_SLOPE_MIN)
    t0 = time.time()
    aa_ = np.linspace(PHASE_RANGE[0], PHASE_RANGE[1], PHASE_N)
    Fv = np.empty(PHASE_N)
    for i, a_s in enumerate(aa_):
        Xs, _, _, _, _ = fam_closed(PHASE_H, a_s / PHASE_H, gam)
        Fv[i] = float(np.sum(Xs ** 2))
    y = np.log(Fv / np.sinh(aa_ / 2.0) ** 2)
    cf = np.polyfit(np.log(aa_), y, 1)
    resid = y - np.polyval(cf, np.log(aa_))
    floor_ratio = math.exp(float(np.min(resid))
                           - float(np.median(resid)))
    check("W4.PHASE no oscillation conspiracy: the family-sum dip "
          "floor %.3f >= %.2f over %d alphas in [%.1f, %.2f] (%.0f "
          "s; the SOS over %d zeros never conspires to near-zero)"
          % (floor_ratio, PHASE_FLOOR, PHASE_N, *PHASE_RANGE,
             time.time() - t0, len(gam)),
          floor_ratio >= PHASE_FLOOR)

    # ============================================================== V
    print("\n" + "=" * 78)
    got_fails = sorted(set(FAILS))
    exp_fails = sorted(set(EXPECTED_FAILS_P2))
    pattern_ok = got_fails == exp_fails
    print("V -- verdict pair: %s + %s"
          % ("BUDGET-LINEAR-CLOSES-ALL" if not any(
              f.startswith(("P1", "R1")) for f in FAILS) else "?!",
             "ENVELOPE-ASYMPTOTIC-PARTIAL" if pattern_ok else "?!"))
    print("=" * 78)
    print("  THE PROOF BLOCKER (typed): the alias phase correlations "
          "-- h^{-1} random-phase vs the\n  h^{-2.5} tower -- block "
          "the analytic uniformity; the envelope stands "
          "CERTIFIED-EXPLICIT\n  (c_cert = %.3f on 73/73), not "
          "proven.  NO RH claim." % c_cert)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = pattern_ok
    print("[%s] PATTERN GATE: expected exactly the FIVE "
          "preregistered-honest asymptotic FAILs %s (got %s)"
          % ("PASS" if ok else "FAIL", ",".join(exp_fails),
             ",".join(got_fails) if got_fails else "none"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
