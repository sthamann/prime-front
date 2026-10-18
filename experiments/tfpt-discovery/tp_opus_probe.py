#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tp_opus_probe.py -- THINNING-PERSISTENCE LEMMA (TPL): DETECTOR, BLIND
SET, AND THE TWO OBSTRUCTIONS.

EXPLORATION PROBE, experiments/ only.  NO RH CLAIM.  NO POSITIVITY CLAIM.
Nothing here is load-bearing, nothing promoted, no marker moves, no gate
closed or narrowed.

=======================================================================
THE OBJECT (independent re-implementation; nothing imported from the
existing probes)
=======================================================================
a = (log x)/2.  Orthonormal even basis of L^2[-a,a]:
      e_0 = 1/sqrt(2a),  e_k = cos(om_k u)/sqrt(a),  om_k = k pi/a.
Galerkin matrix of the semilocal Weil form,
      M[j,k] = POLE - ... = POLE[j,k] + ARCH[j,k] - PRIME[j,k],
with psi_jk = e_j * e_k~  (psi_jk(0) = delta_jk) and L = 2a:
  POLE[j,k]  = 2 b_j(i/2) b_k(i/2)                       (rank one, exact)
  ARCH[j,k]  = -delta_jk (gamma_E + log pi + log(1-e^{-2L}))
               + 2 int_0^L [delta_jk e^{-2v} - psi_jk(v) e^{-v/2}]
                           / (1 - e^{-2v}) dv
  PRIME[j,k] = 2 sum_{p^m <= x} (log p / p^{m/2}) psi_jk(m log p)
b_k = Fourier transform of e_k:
  b_k(t) = [sin(a(t-om_k))/(t-om_k) + sin(a(t+om_k))/(t+om_k)] / n_k,
  n_0 = sqrt(2a), n_k = sqrt(a);  b_k(t) = (-1)^k sin(at) 2t/((t^2-om_k^2) n_k).

lam(x) := lam_min(M) is the wall scalar; the minimizer E_x = sum_k c_k b_k
is entire of exponential type a, even, real, and (Caratheodory-Fejer /
Connes-van Suijlekom, hypothesis H1 = simple bottom with even eigenvector)
REAL-ROOTED.

=======================================================================
THE IDENTITY THE PROBE IS BUILT ON (Theorem 1 of the accompanying
analysis; unconditional)
=======================================================================
For phi in L^2[-a,a] real even, E = phihat, psi = phi * phi~, the
Guinand-Weil explicit formula gives psihat = E^2 and

      Q_x(phi) = W[psi] = sum_rho E(gamma_rho)^2 ,
      gamma_rho = -i(rho - 1/2)   over ALL nontrivial zeros,

an off-line quadruple {+-gam0, +-conj(gam0)}, gam0 = alpha + i beta,
contributing 4 Re[E(gam0)^2] (indefinite sign), and a real ordinate pair
contributing 2 E(gamma)^2 >= 0.  Hence in matrix form

      M[j,k] = sum_rho b_j(gamma_rho) b_k(gamma_rho)
             = 2 sum_{gamma>0 real} b_j b_k + sum_quad 4 Re[b_j b_k].

Consequences used here: lam(x) >= 0 for every x iff RH; lam(x) is
nonincreasing in x (PW_a is increasing); and lam(x) is the least positive
eigenvalue of the sine-kernel Gram matrix [sin(a(g-g'))/(pi(g-g'))] of
the zeta ordinates.

=======================================================================
WHAT THIS PROBE MEASURES (all numbers printed exactly)
=======================================================================
W1  quadruple algebra ward (the 4 Re bookkeeping).
W1b instrument identity: my assembly reproduces the RECORD lam_min at
    x = 8, K = 21 (an independent second implementation).
W2  Gram-identity ward: my source-only assembly at x = 5 against
    2 sum_{gamma>0} b_j b_k from the read-only ordinate cache plus the
    analytic tail model  (-1)^{j+k} (2/pi)(log(G/2pi)+1)/G.
W3  cross-instrument ward: my mp lam_min at x = 8, K = 21 against the
    RECORD constant 3.77e-30 (round-83 arbiter / lane 1).
W4  density ward: ARCH[j,k] == int b_j b_k n_smooth,
    n_smooth(t) = theta'(|t|)/pi  (Riemann-Siegel theta), i.e. ARCH IS
    the smooth (archimedean) part of the zero measure and -PRIME IS the
    fluctuation dS.  This is the identification Obstruction A rests on.
S1  OBSTRUCTION A (density blindness): lam_min(ARCH), lam_min(POLE+ARCH),
    ||PRIME||, lam_min(full) over the ladder.  Prediction: the
    density-level model has a NEGATIVE O(1) ground state while the true
    one is positive and e^{-c x}.
S2  OBSTRUCTION B (no perturbative comparison): Davis-Kahan ledger
    ||PRIME|| vs the bottom gap.
S3  BLIND SET: Phi_Lam(alpha,beta) = sum_gamma arctan(beta/(alpha-gamma))
    from the cache; B(beta) = {alpha : |Phi| >= pi/4} is exactly the set
    of off-line real parts the census instrument cannot see.
S4  PLANTED WORLDS: M -> M + 4 Re[b(gam0) b(gam0)^T] (an off-line
    quadruple planted into the zero measure at fixed source data), with
    a REAL-pair control 2 b(alpha) b(alpha)^T.  Measures sign of
    lam_min, realness, the census in (0,30), the distance from alpha to
    the nearest zero, and the detector resolution beta*.
S5  K-SWEEP and DEPTH LADDER: position depth (|z_i - gamma_i| <= tol)
    and count depth (z_i in the i-th ordinate slot) vs x and vs K.
S6  SECULAR REPRESENTATION: E = sin(a t) . 2t . f(t^2)/prod(t^2-om_k^2)
    with f(u) = sum_k g_k/(u - om_k^2), g_k = (-1)^k c_k/n_k.  A mode
    interval has an EVEN zero count iff sign(g_k) != sign(g_{k+1}), so
    the thinning below the Nyquist count is paid for, one for one, in
    SIGN CHANGES of ((-1)^k c_k).
S7  DENSITY-DEFICIT LAW: D(T) = a T/pi - N_Xi(T) is the number of mode
    intervals that must be skipped; it peaks at T = 2 pi x with
    D_max = x - 3/8 + O(S).  The tracking band ends at that peak, the
    skip count equals D_max, and d(-log lam_min)/dD_max is constant.

DECLARED SUBSAMPLING AND LIMITS: mp cells only at x in (3,5,8) (dps
45/60/80, floor 4 pi x/ln 10 + margin); deeper lam_min values are quoted
from the RECORD, not re-measured.  The zero profile is scanned in
float64 from an mp eigenvector, which is sound while |E(gamma)| ~
sqrt(lam) stays above the 1e-17 cancellation floor, i.e. for x <= 8;
census/secular sections therefore stop at x = 8.  Beyond the last
secular pole f is a 16-digit cancellation in float64, so tail roots are
not counted.  The cache tail is modelled analytically (model printed).
The blind set is measured on alpha in (0,100) from the cache.

NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
import scipy.linalg as sla
from scipy.special import digamma as sp_digamma

# ------------------------------------------------------------------ bars
KFAC = 1.25
LADDER_F64 = (3, 5, 8, 13, 21, 34, 55)
LADDER_MP = (3, 5, 8)
DPS_MP = {3: 45, 5: 60, 8: 80}
DPS_FLOOR_MARGIN = 5.0
KSWEEP_X = 5
KSWEEP_K = (6, 8, 11, 16, 22)
PLANT_X = 5
PLANT_BETAS = (1e-9, 1e-8, 1e-7, 1e-5, 1e-3, 1e-1, 0.25)
GAUSS_ORDER = 30
GAUSS_ORDER_MP = 24
PANEL_FAC = 3.0
SCAN_STEP = 0.01
BISECT = 60
CENSUS_T = 30.0
Z1_TAIL_BAR = 3e-4
Z1_MODEL_SHARE = 0.70
W3_REL_BAR = 0.05
W4_REL_BAR = 5e-3
BLIND_BETAS = (0.5, 0.25, 0.1, 0.05, 0.02)
BLIND_ALPHA_HI = 100.0
BLIND_GRID = 0.002
RUNTIME_BAR = 1500.0

EULER = 0.57721566490153286061
LOG_PI = math.log(math.pi)
GAMMA1_LIT = 14.134725141734693790          # literature constant, ward only
RECORD_TAU8 = 3.77e-30                      # RECORD constant (round 83)
RECORD_TAU13 = 2.5e-54                      # RECORD constant
RECORD_TAU21 = 1.25e-93                     # RECORD constant

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ======================================================== source tables
def prime_power_atoms(cap: float) -> tuple[np.ndarray, np.ndarray]:
    """(u = m log p, w = log p / p^{m/2}) for all p^m <= cap.  Own sieve,
    no primality oracle, no selection."""
    icap = int(math.floor(cap + 1e-12))
    if icap < 2:
        return np.zeros(0), np.zeros(0)
    comp = np.zeros(icap + 1, dtype=bool)
    us, ws = [], []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        lp = math.log(p)
        q = p
        while q <= icap:
            us.append(math.log(q))
            ws.append(lp / math.sqrt(q))
            q *= p
    o = np.argsort(np.asarray(us))
    return np.asarray(us)[o], np.asarray(ws)[o]


# ================================================ float64 Weil assembly
_GX, _GW = np.polynomial.legendre.leggauss(GAUSS_ORDER)


def panel_nodes(lo: float, hi: float, npan: int) -> tuple[np.ndarray,
                                                          np.ndarray]:
    e = np.linspace(lo, hi, npan + 1)
    mid = 0.5 * (e[:-1] + e[1:])
    half = 0.5 * (e[1:] - e[:-1])
    xs = (mid[:, None] + half[:, None] * _GX[None, :]).ravel()
    ws = (half[:, None] * _GW[None, :]).ravel()
    return xs, ws


def arch_A(v: np.ndarray) -> np.ndarray:
    """A(v) = e^{-v/2}/(1-e^{-2v}); ~1/(2v) at 0 (integrable against
    psi_jk, which vanishes linearly there)."""
    return np.exp(-0.5 * v) / (-np.expm1(-2.0 * v))


def basis_data(x: float, K: int) -> dict:
    a = 0.5 * math.log(x)
    om = np.arange(K) * math.pi / a
    nrm = np.full(K, math.sqrt(a))
    nrm[0] = math.sqrt(2.0 * a)
    par = (-1.0) ** np.arange(K)
    return {"x": x, "a": a, "K": K, "om": om, "nrm": nrm, "par": par,
            "L": 2.0 * a}


def bvec(bd: dict, t) -> np.ndarray:
    """b_k(t) for scalar (possibly complex) t."""
    a, om, nrm = bd["a"], bd["om"], bd["nrm"]
    d1 = t - om
    d2 = t + om
    tiny = 1e-13
    q1 = np.where(np.abs(d1) < tiny, 1.0, d1)
    q2 = np.where(np.abs(d2) < tiny, 1.0, d2)
    s1 = np.where(np.abs(d1) < tiny, a, np.sin(a * d1) / q1)
    s2 = np.where(np.abs(d2) < tiny, a, np.sin(a * d2) / q2)
    return (s1 + s2) / nrm


def bmat(bd: dict, ts: np.ndarray) -> np.ndarray:
    """(len(ts), K) matrix of b_k(t)."""
    a, om, nrm = bd["a"], bd["om"], bd["nrm"]
    t = np.asarray(ts)[:, None]
    d1 = t - om[None, :]
    d2 = t + om[None, :]
    tiny = 1e-13
    s1 = np.where(np.abs(d1) < tiny, a, np.sin(a * d1) / np.where(
        np.abs(d1) < tiny, 1.0, d1))
    s2 = np.where(np.abs(d2) < tiny, a, np.sin(a * d2) / np.where(
        np.abs(d2) < tiny, 1.0, d2))
    return (s1 + s2) / nrm[None, :]


def sep_offdiag(bd: dict, vec: np.ndarray) -> np.ndarray:
    """Off-diagonal matrix of  int psi_jk d(channel)  for a channel whose
    1-D sine transform is vec_k:  raw = (-1)^{j+k}(om_k V_k - om_j V_j)
    /(om_j^2 - om_k^2), normalized by n_j n_k.  Diagonal set to 0."""
    om, nrm, par = bd["om"], bd["nrm"], bd["par"]
    om2 = om ** 2
    den = om2[:, None] - om2[None, :]
    np.fill_diagonal(den, 1.0)
    term = om * vec
    raw = np.outer(par, par) * (term[None, :] - term[:, None]) / den
    np.fill_diagonal(raw, 0.0)
    return raw / np.outer(nrm, nrm)


def build_form_f64(x: float, K: int) -> dict:
    """POLE, ARCH, PRIME blocks in the orthonormal even basis (float64)."""
    bd = basis_data(x, K)
    a, om, nrm, L = bd["a"], bd["om"], bd["nrm"], bd["L"]

    # ---- POLE: exact rank one, p_j = b_j(i/2) = (-1)^j sinh(a/2)
    #      /((1/4 + om_j^2) n_j)   (k = 0 needs no special case)
    p = bd["par"] * math.sinh(0.5 * a) / (0.25 + om ** 2) / nrm
    m_pole = 2.0 * np.outer(p, p)

    # ---- quadrature grid on [0, L]
    npan = max(48, int(math.ceil(PANEL_FAC * 2.0 * (K + 1))))
    v, w = panel_nodes(1e-300, L, npan)
    A = arch_A(v)
    E2 = np.exp(-2.0 * v) / (-np.expm1(-2.0 * v))

    # ---- ARCH off-diagonal via J_k = int_0^L sin(om_k v) A(v) dv
    J = np.sin(np.outer(om, v)) @ (w * A)
    m_arch = -2.0 * sep_offdiag(bd, J)

    # ---- ARCH diagonal (regularized integrand, chunked over k)
    diag_int = np.empty(K)
    CH = 64
    for i0 in range(0, K, CH):
        ks = np.arange(i0, min(i0 + CH, K))
        ph = np.outer(om[ks], v)
        psi = ((a - 0.5 * v)[None, :] * np.cos(ph)
               - np.sin(ph) / np.where(om[ks][:, None] == 0.0, 1.0,
                                       2.0 * om[ks][:, None])) / a
        if ks[0] == 0:
            psi[0] = (2.0 * a - v) / (2.0 * a)
        diag_int[ks] = (E2[None, :] - psi * A[None, :]) @ w
    np.fill_diagonal(m_arch, -(EULER + LOG_PI)
                     - math.log1p(-math.exp(-2.0 * L)) + 2.0 * diag_int)

    # ---- PRIME
    us, wts = prime_power_atoms(x)
    if len(us):
        P = np.sin(np.outer(om, us)) @ wts
        m_prime = 2.0 * sep_offdiag(bd, P)
        ph = np.outer(om, us)
        dg = ((a - 0.5 * us)[None, :] * np.cos(ph)
              - np.sin(ph) / np.where(om[:, None] == 0.0, 1.0,
                                      2.0 * om[:, None])) / a
        dg[0] = (2.0 * a - us) / (2.0 * a)
        np.fill_diagonal(m_prime, 2.0 * (dg @ wts))
    else:
        m_prime = np.zeros((K, K))

    m_pole = 0.5 * (m_pole + m_pole.T)
    m_arch = 0.5 * (m_arch + m_arch.T)
    m_prime = 0.5 * (m_prime + m_prime.T)
    out = dict(bd)
    out.update({"pole": m_pole, "arch": m_arch, "prime": m_prime,
                "full": m_pole + m_arch - m_prime, "n_atoms": len(us)})
    return out


# ===================================================== mp Weil assembly
_GLC: dict[tuple[int, int], tuple] = {}


def gauss_mp(order: int):
    key = (order, mp.mp.dps)
    if key not in _GLC:
        nd, wt = mp.gauss_quadrature(order, "legendre")
        _GLC[key] = ([nd[i] for i in range(order)],
                     [wt[i] for i in range(order)])
    return _GLC[key]


def build_form_mp(x: int, K: int, dps: int) -> dict:
    """Same three blocks at working precision dps.  The bottom cluster of
    the full form lives at the Connes scale, so only this build resolves
    lam_min; float64 resolves the ARCH/PRIME blocks (O(1)) but not the
    ground state."""
    t0 = time.time()
    with mp.workdps(dps + 10):
        aa = mp.log(x) / 2
        L = 2 * aa
        oms = [mp.mpf(k) * mp.pi / aa for k in range(K)]
        nrm = [mp.sqrt(2 * aa)] + [mp.sqrt(aa)] * (K - 1)
        par = [mp.mpf((-1) ** k) for k in range(K)]

        # quadrature nodes on [0, L]
        npan = max(48, int(math.ceil(PANEL_FAC * 2.0 * (K + 1))))
        nd, wt = gauss_mp(GAUSS_ORDER_MP)
        vs, ws = [], []
        step = L / npan
        for ip in range(npan):
            mid = (2 * ip + 1) * step / 2
            half = step / 2
            for nn, ww in zip(nd, wt):
                vs.append(mid + half * nn)
                ws.append(half * ww)
        Av = [mp.exp(-v / 2) / (-mp.expm1(-2 * v)) for v in vs]
        E2v = [mp.exp(-2 * v) / (-mp.expm1(-2 * v)) for v in vs]
        th = [mp.pi * v / aa for v in vs]                 # om_1 * v
        cth = [mp.cos(t) for t in th]
        sth = [mp.sin(t) for t in th]

        # J_k and the ARCH diagonal integrals, cos/sin(k th) by recursion
        J = [mp.mpf(0)] * K
        DI = [mp.mpf(0)] * K
        ck = [mp.mpf(1)] * len(vs)      # cos(0 * th)
        sk = [mp.mpf(0)] * len(vs)      # sin(0 * th)
        for k in range(K):
            if k > 0:
                nc = [ck[i] * cth[i] - sk[i] * sth[i] for i in range(len(vs))]
                ns = [sk[i] * cth[i] + ck[i] * sth[i] for i in range(len(vs))]
                ck, sk = nc, ns
            jj = mp.mpf(0)
            di = mp.mpf(0)
            ok = oms[k]
            for i in range(len(vs)):
                jj += ws[i] * Av[i] * sk[i]
                if k == 0:
                    psi = (L - vs[i]) / L
                else:
                    psi = ((aa - vs[i] / 2) * ck[i] - sk[i] / (2 * ok)) / aa
                di += ws[i] * (E2v[i] - psi * Av[i])
            J[k] = jj
            DI[k] = di

        # prime atoms at working precision (own sieve, no oracle)
        P = [mp.mpf(0)] * K
        DP = [mp.mpf(0)] * K
        atoms = []
        icap = int(math.floor(x))
        comp = [False] * (icap + 1)
        for pp in range(2, icap + 1):
            if comp[pp]:
                continue
            for q0 in range(pp * pp, icap + 1, pp):
                comp[q0] = True
            q = pp
            while q <= icap:
                atoms.append((mp.log(q), mp.log(pp) / mp.sqrt(q)))
                q *= pp
        for k in range(K):
            ok = oms[k]
            s1 = mp.mpf(0)
            s2 = mp.mpf(0)
            for (u, wgt) in atoms:
                s1 += wgt * mp.sin(ok * u)
                if k == 0:
                    s2 += wgt * (L - u) / L
                else:
                    s2 += wgt * ((aa - u / 2) * mp.cos(ok * u)
                                 - mp.sin(ok * u) / (2 * ok)) / aa
            P[k] = s1
            DP[k] = s2

        def sep(vec):
            out = mp.zeros(K, K)
            for j in range(K):
                for k in range(K):
                    if j == k:
                        continue
                    num = oms[k] * vec[k] - oms[j] * vec[j]
                    den = oms[j] ** 2 - oms[k] ** 2
                    out[j, k] = (par[j] * par[k] * num / den
                                 / (nrm[j] * nrm[k]))
            return out

        m_arch = sep(J)
        for j in range(K):
            for k in range(K):
                m_arch[j, k] = -2 * m_arch[j, k]
        cdiag = (-(mp.euler + mp.log(mp.pi))
                 - mp.log1p(-mp.exp(-2 * L)))
        for k in range(K):
            m_arch[k, k] = cdiag + 2 * DI[k]
        m_prime = sep(P)
        for j in range(K):
            for k in range(K):
                m_prime[j, k] = 2 * m_prime[j, k]
        for k in range(K):
            m_prime[k, k] = 2 * DP[k]
        pv = [par[k] * mp.sinh(aa / 2) / (mp.mpf(1) / 4 + oms[k] ** 2)
              / nrm[k] for k in range(K)]
        m_pole = mp.zeros(K, K)
        for j in range(K):
            for k in range(K):
                m_pole[j, k] = 2 * pv[j] * pv[k]
        M = mp.zeros(K, K)
        for j in range(K):
            for k in range(K):
                M[j, k] = m_pole[j, k] + m_arch[j, k] - m_prime[j, k]
        for j in range(K):
            for k in range(j):
                s = (M[j, k] + M[k, j]) / 2
                M[j, k] = s
                M[k, j] = s
    return {"x": x, "K": K, "dps": dps, "M": M, "a": float(aa),
            "n_atoms": len(atoms), "build_s": time.time() - t0}


def basis_mp(x: int, K: int):
    """(a, om, nrm) at working precision, for exact planted updates."""
    aa = mp.log(x) / 2
    oms = [mp.mpf(k) * mp.pi / aa for k in range(K)]
    nrm = [mp.sqrt(2 * aa)] + [mp.sqrt(aa)] * (K - 1)
    return aa, oms, nrm


def bvec_mp(x: int, K: int, tau):
    """b_k(tau) at working precision, tau real or complex."""
    aa, oms, nrm = basis_mp(x, K)
    out = []
    for k in range(K):
        d1 = tau - oms[k]
        d2 = tau + oms[k]
        s1 = aa if abs(d1) < mp.mpf(10) ** (-mp.mp.dps + 5) \
            else mp.sin(aa * d1) / d1
        s2 = aa if abs(d2) < mp.mpf(10) ** (-mp.mp.dps + 5) \
            else mp.sin(aa * d2) / d2
        out.append((s1 + s2) / nrm[k])
    return out


def eig_mp(M: mp.matrix, dps: int) -> tuple[float, float, np.ndarray, str]:
    with mp.workdps(dps + 10):
        E, Q = mp.eigsy(M)
        n = M.rows
        order = sorted(range(n), key=lambda i: E[i])
        i0, i1 = order[0], order[1]
        c = [Q[i, i0] for i in range(n)]
        big = max(range(n), key=lambda i: abs(c[i]))
        if c[big] < 0:
            c = [-v for v in c]
        lam = E[i0]
        gap = E[i1] - E[i0]
        return (float(lam), float(gap),
                np.array([float(v) for v in c]), mp.nstr(lam, 6))


# ============================================== zeros of the minimizer
def profile(bd: dict, cn: np.ndarray, ts: np.ndarray) -> np.ndarray:
    out = np.empty(len(ts))
    CH = 4000
    for i in range(0, len(ts), CH):
        out[i: i + CH] = bmat(bd, ts[i: i + CH]) @ cn
    return out


def secular(bd: dict, cn: np.ndarray) -> np.ndarray:
    """E(t) = sin(a t) . 2t . sum_k g_k/(t^2 - om_k^2),
       g_k = (-1)^k c_k / n_k  (from b_k(t) = (-1)^k sin(a t) 2t
       /((t^2-om_k^2) n_k)).  The K-1 FREE zeros of E are the roots of
       the secular function f(u) = sum_k g_k/(u - om_k^2); everything
       else is the fixed lattice {om_j : j >= K}.  Between consecutive
       poles f runs from sign(g_k) inf to -sign(g_{k+1}) inf, so a mode
       interval can be EMPTY only if sign(g_k) != sign(g_{k+1}).
       Thinning below the Nyquist count therefore REQUIRES sign changes
       in ((-1)^k c_k) -- one per skipped mode interval."""
    return bd["par"] * cn / bd["nrm"]


def secular_roots(bd: dict, g: np.ndarray, pad: float = 12.0
                  ) -> tuple[np.ndarray, np.ndarray]:
    """Count/locate the roots of f(u) = sum g_k/(u - p_k), p_k = om_k^2,
    interval by interval.  Returns (roots in u, occupancy per mode
    interval)."""
    p = bd["om"] ** 2
    K = len(p)
    tail = p[-1] - p[-2] + 1.0
    edges = list(p) + [p[-1] + pad * tail * 4 ** m for m in range(4)]
    roots, occ = [], []
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        w = hi - lo
        s = 0.5 * (1.0 - np.cos(np.pi * np.linspace(0.0, 1.0, 1500)))
        u = lo + w * s[1:-1]
        f = (g[None, :] / (u[:, None] - p[None, :])).sum(1)
        idx = np.nonzero(f[:-1] * f[1:] < 0.0)[0]
        cnt = 0
        for j in idx:
            a0, b0 = u[j], u[j + 1]
            fa = f[j]
            for _ in range(80):
                m = 0.5 * (a0 + b0)
                fm = float((g / (m - p)).sum())
                if fm * fa > 0.0:
                    a0, fa = m, fm
                else:
                    b0 = m
            r = 0.5 * (a0 + b0)
            if roots and abs(r - roots[-1]) <= 1e-8 * max(abs(r), 1.0):
                continue                      # sub-interval boundary dup
            roots.append(r)
            cnt += 1
        if i < K - 1:
            occ.append(cnt)
    return np.asarray(roots), np.asarray(occ, dtype=int)


def track_depth(zs: np.ndarray, gam: np.ndarray, tol: float = 1e-4) -> int:
    """POSITION depth: the largest m with |z_i - gamma_i| <= tol for all
    i <= m.  (Hurwitz/determination needs this one.)"""
    m = 0
    for i in range(min(len(zs), len(gam))):
        if abs(float(zs[i]) - float(gam[i])) > tol:
            break
        m += 1
    return m


def count_depth(zs: np.ndarray, gam: np.ndarray) -> int:
    """COUNT depth: the largest m such that the i-th zero sits in the
    i-th ordinate slot (gamma_{i-1}, gamma_{i+1}), gamma_0 = 0, for all
    i <= m -- i.e. the counting functions #Z(E) cap (0,T) and N_Xi(T)
    agree up to the slot boundaries.  This is what TPL(i) asserts."""
    m = 0
    for i in range(min(len(zs), len(gam) - 1)):
        lo = 0.0 if i == 0 else float(gam[i - 1])
        if not (lo < float(zs[i]) < float(gam[i + 1])):
            break
        m += 1
    return m


def scan_zeros(bd: dict, cn: np.ndarray, t_hi: float,
               step: float = SCAN_STEP) -> np.ndarray:
    ts = np.arange(1e-9, t_hi, step)
    vs = profile(bd, cn, ts)
    idx = np.nonzero(vs[:-1] * vs[1:] < 0.0)[0]
    lo, hi = ts[idx].copy(), ts[idx + 1].copy()
    flo = vs[idx].copy()
    for _ in range(BISECT):
        mid = 0.5 * (lo + hi)
        fm = profile(bd, cn, mid)
        same = fm * flo > 0.0
        lo = np.where(same, mid, lo)
        flo = np.where(same, fm, flo)
        hi = np.where(same, hi, mid)
    return 0.5 * (lo + hi)


# ============================================== target-namespace wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def target_gram(bd: dict, gam: np.ndarray) -> np.ndarray:
    """2 sum_{gamma>0} b_j(gamma) b_k(gamma) over the cache."""
    B = bmat(bd, gam)
    return 2.0 * (B.T @ B)


def target_tail_model(bd: dict, gtop: float) -> np.ndarray:
    """Analytic tail of the Gram sum beyond the cache:
    b_j b_k -> (-1)^{j+k} sin^2(a t) 4 t^2/((t^2-om_j^2)(t^2-om_k^2)
    n_j n_k) ~ (-1)^{j+k} 4 sin^2(a t)/(t^2 n_j n_k), <sin^2> = 1/2, and
    the two-sided sum 2 sum_{gamma>gtop} -> 2 int (1/2pi) log(t/2pi)
    ... = (2/pi)(log(gtop/2pi)+1)/gtop / (n_j n_k)."""
    nrm = bd["nrm"]
    mag = (2.0 / math.pi) * (math.log(gtop / (2.0 * math.pi)) + 1.0) / gtop
    return (np.outer(bd["par"], bd["par"]) * mag
            / np.outer(nrm, nrm))


def target_theta_prime(t: np.ndarray) -> np.ndarray:
    """theta'(t) = (1/2) Re psi(1/4 + i t/2) - (1/2) log pi; the smooth
    zero density is n_smooth(t) = theta'(|t|)/pi (signed near 0)."""
    z = 0.25 + 0.5j * np.abs(np.asarray(t, float))
    return 0.5 * np.real(sp_digamma(z)) - 0.5 * LOG_PI


def target_phi_lambda(alpha: np.ndarray, beta: float, gam: np.ndarray
                      ) -> np.ndarray:
    """Phi_Lam(alpha,beta) = sum_{gamma real ordinate} arctan(beta/
    (alpha-gamma)), the +- pair sum, with the analytic tail beyond the
    cache.  Re[E(alpha+i beta)^2] < 0 for a real-rooted E iff the SAME
    functional of E's zero set lies in (pi/4, 3pi/4) mod pi."""
    al = np.asarray(alpha, float)[:, None]
    g = gam[None, :]
    val = (np.arctan(beta / (al - g)) + np.arctan(beta / (al + g))).sum(1)
    gtop = float(gam[-1])
    # tail: sum_{gamma>gtop} -2 alpha beta/(gamma^2-alpha^2)
    #       ~ -2 alpha beta int_gtop^inf n(t)/t^2 dt
    tail = -2.0 * al[:, 0] * beta * (
        (math.log(gtop / (2.0 * math.pi)) + 1.0) / (2.0 * math.pi * gtop))
    return val + tail


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import) else [node.module or ""])
            for m in mods:
                if m.startswith("verification") or "probe" in m:
                    bad.append("import " + m)
        if isinstance(node, ast.Attribute) and node.attr.lower() in {
                "zetazero", "zetazeros", "nzeros", "siegelz", "siegeltheta"}:
            bad.append("attr " + node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            nm = (fn.id if isinstance(fn, ast.Name)
                  else fn.attr if isinstance(fn, ast.Attribute) else "")
            if nm.lower() in {"zetazero", "zetazeros", "nzeros"}:
                bad.append("call " + nm)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        ok = node.name.startswith(("ward_", "target_")) or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" and not ok:
                bad.append("cache in " + node.name)
    return not bad, "violations: %s" % (bad or "none")


# ---------------------------------------------------------------- main
def main() -> int:
    global LADDER_F64, LADDER_MP, PLANT_BETAS
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.smoke:
        LADDER_F64 = (3, 5, 8)
        LADDER_MP = (3, 5)
        PLANT_BETAS = (1e-8, 1e-5, 0.25)

    print("=" * 78)
    print("tp_opus_probe  THINNING-PERSISTENCE LEMMA: detector, blind set,"
          " obstructions")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if args.smoke else ""))
    print("=" * 78)

    # ------------------------------------------------ I. instrument wards
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("A1 AST firewall (no zero oracle, no probe imports; cache only"
          " in ward_/target_/main)", fw_ok, fw_det)
    gam = ward_cache()
    check("A2 ordinate cache health (READ-ONLY, target namespace)",
          len(gam) >= 5000 and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e top %.3f"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT), float(gam[-1])))

    # W1 -- quadruple algebra
    bd_t = basis_data(5, 8)
    g0 = complex(23.7, 0.31)
    b_p = bvec(bd_t, g0)
    b_m = bvec(bd_t, -g0)
    b_c = bvec(bd_t, np.conj(g0))
    b_mc = bvec(bd_t, -np.conj(g0))
    quad = (np.outer(b_p, b_p) + np.outer(b_m, b_m)
            + np.outer(b_c, b_c) + np.outer(b_mc, b_mc))
    dev_q = float(np.max(np.abs(quad - 4.0 * np.real(np.outer(b_p, b_p)))))
    check("W1 quadruple algebra: the four ordinates of an off-line zero"
          " contribute 4 Re[b_j b_k]", dev_q < 1e-9,
          "max dev %.2e (b_k even, real-coefficient)" % dev_q)

    # W2 -- Gram identity ward at x = 5
    cell5 = build_form_f64(5, int(math.ceil(KFAC * 5 * math.log(5))))
    G5 = target_gram(cell5, gam)
    T5 = target_tail_model(cell5, float(gam[-1]))
    raw = float(np.max(np.abs(cell5["full"] - G5)))
    corr = float(np.max(np.abs(cell5["full"] - G5 - T5)))
    check("W2 Gram identity M[j,k] == sum_rho b_j b_k (source-only"
          " assembly vs cache)", corr < Z1_TAIL_BAR
          and corr < (1.0 - Z1_MODEL_SHARE) * raw,
          "worst |dev| %.3e raw -> %.3e after the analytic tail model"
          " (model explains %.0f%%; bar %.0e)"
          % (raw, corr, 100.0 * (1.0 - corr / raw), Z1_TAIL_BAR))

    # W4 -- ARCH is the smooth (archimedean) density block
    npan = 4000
    tt, tw = panel_nodes(1e-9, 1500.0, npan)
    B = bmat(cell5, tt)
    ns = target_theta_prime(tt) / math.pi
    dens = 2.0 * (B * (tw * ns)[:, None]).T @ B      # both signs of tau
    gtop_d = 1500.0
    dens = dens + target_tail_model(cell5, gtop_d)
    dev_d = float(np.max(np.abs(cell5["arch"] - dens)))
    scl = float(np.max(np.abs(cell5["arch"])))
    check("W4 ARCH == int b_j b_k n_smooth, n_smooth = theta'(|t|)/pi"
          " (so -PRIME == the fluctuation dS)", dev_d / scl < W4_REL_BAR,
          "worst |dev| %.3e vs ||ARCH|| %.3f -> rel %.2e (bar %.0e)"
          % (dev_d, scl, dev_d / scl, W4_REL_BAR))

    # W3 -- cross-instrument: mp lam_min at x = 8 vs the RECORD constant
    mpcells: dict[int, dict] = {}
    for xv in LADDER_MP:
        Kv = int(math.ceil(KFAC * xv * math.log(xv)))
        dps = DPS_MP[xv]
        floor = 4.0 * math.pi * xv / math.log(10.0) + DPS_FLOOR_MARGIN
        cc = build_form_mp(xv, Kv, dps)
        lam, gapv, cn, lstr = eig_mp(cc["M"], dps)
        cc.update({"lam": lam, "gap": gapv, "cn": cn, "lam_str": lstr,
                   "floor": floor})
        mpcells[xv] = cc
        print("    mp cell x=%2d K=%2d dps=%3d (floor %5.1f) lam_min=%s"
              " gap=%.3e  %.1fs"
              % (xv, Kv, dps, floor, lstr, gapv, cc["build_s"]))
    if 8 in mpcells:
        rel8 = abs(mpcells[8]["lam"] - RECORD_TAU8) / RECORD_TAU8
        check("W3 cross-instrument: my lam_min(x=8,K=21) vs RECORD"
              " 3.77e-30", rel8 < W3_REL_BAR,
              "mine %s vs record %.3e -> rel dev %.3e (bar %.0e)"
              % (mpcells[8]["lam_str"], RECORD_TAU8, rel8, W3_REL_BAR))

    # ------------------------------------- II. OBSTRUCTION A (density)
    section("II. OBSTRUCTION A -- THE DENSITY-LEVEL MODEL HAS THE WRONG"
            " SIGN\n     (ARCH = smooth zero density; -PRIME = the"
            " fluctuation dS.  Any argument\n     that sees only the"
            " density -- MNT/Totik regularity, Christoffel\n"
            "     asymptotics, Landau-Widom background/plunge -- reads"
            " lam_min(ARCH).)")
    print("  %4s %5s %14s %14s %13s %13s %14s"
          % ("x", "K", "lam(ARCH)", "lam(POLE+ARCH)", "||PRIME||",
             "||M_full||", "lam_min(full)"))
    rows = []
    for xv in LADDER_F64:
        Kv = int(math.ceil(KFAC * xv * math.log(xv)))
        cc = build_form_f64(xv, Kv)
        la = float(sla.eigh(cc["arch"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
        lpa = float(sla.eigh(cc["pole"] + cc["arch"], eigvals_only=True,
                             subset_by_index=[0, 0])[0])
        npr = float(np.linalg.norm(cc["prime"], 2))
        nfu = float(np.linalg.norm(cc["full"], 2))
        if xv in mpcells:
            lf = "%.4e" % mpcells[xv]["lam"]
        elif xv == 13:
            lf = "%.2e [REC]" % RECORD_TAU13
        elif xv == 21:
            lf = "%.2e [REC]" % RECORD_TAU21
        else:
            lf = "  (mp needed)"
        rows.append((xv, Kv, la, lpa, npr, nfu, lf))
        print("  %4d %5d %14.6f %14.6f %13.4f %13.4f %14s"
              % (xv, Kv, la, lpa, npr, nfu, lf))
    lam_arch_all_neg = all(r[2] < -0.05 for r in rows)
    lim_arch = 2.0 * target_theta_prime(np.array([0.0]))[0]
    check("S1.1 the density-level ground state is NEGATIVE and O(1) on"
          " every rung (lam(ARCH) = %.3f -> %.3f) while the true one is"
          " positive and e^{-c x}" % (rows[0][2], rows[-1][2]),
          lam_arch_all_neg and rows[-1][2] < rows[0][2]
          and rows[-1][2] > lim_arch,
          "monotone down towards the a -> inf value 2 theta'(0) ="
          " 2 pi n_smooth(0) = %.4f" % lim_arch)
    check("S1.2 lam_min(POLE+ARCH) is negative too (%s): the pole block"
          " does not rescue the density model"
          % " ".join("%.3f" % r[3] for r in rows),
          all(r[3] < 0.0 for r in rows),
          "so the +|lam(POLE+ARCH)| shift to the true ground state is"
          " supplied by the prime block ALONE, to e^{-c x} accuracy")
    fit = np.polyfit(np.log([r[0] for r in rows]),
                     np.log([r[4] for r in rows]), 1)[0]
    check("S1.3 ||PRIME|| grows like x^%.3f -- the fluctuation block is"
          " LARGE, not a correction" % fit,
          rows[-1][4] > 3.0 * rows[0][4],
          "%.3f -> %.3f over x = %d..%d (Chebyshev floor: the triangle"
          " test function already gives PRIME ~ 8 sqrt(x)/log x)"
          % (rows[0][4], rows[-1][4], rows[0][0], rows[-1][0]))
    lams = [(xv, mpcells[xv]["lam"]) for xv in LADDER_MP]
    mono_x = all(lams[i][1] > lams[i + 1][1] for i in range(len(lams) - 1))
    check("S1.4 lam(x) is nonincreasing in x (Theorem 1(b): PW_a grows"
          " with x)", mono_x,
          " > ".join("%.3e" % v for _k, v in lams))

    # ------------------------------ III. OBSTRUCTION B (Davis-Kahan)
    section("III. OBSTRUCTION B -- NO PERTURBATIVE GROUND-STATE"
            " COMPARISON IS POSSIBLE\n     (Davis-Kahan / analytic"
            " perturbation needs ||Delta|| < gap/2.)")
    print("  %4s %13s %13s %13s %16s"
          % ("x", "||PRIME||", "lam_min", "bottom gap", "||PRIME||/gap"))
    dk = []
    for xv in LADDER_MP:
        cc = mpcells[xv]
        Kv = cc["K"]
        cf = build_form_f64(xv, Kv)
        npr = float(np.linalg.norm(cf["prime"], 2))
        ratio = npr / max(cc["gap"], 1e-300)
        dk.append((xv, npr, cc["lam"], cc["gap"], ratio))
        print("  %4d %13.4f %13.4e %13.4e %16.4e"
              % (xv, npr, cc["lam"], cc["gap"], ratio))
    if 13 not in LADDER_MP:
        print("  (record rungs, not re-measured: x=13 lam=%.2e, x=21"
              " lam=%.2e -- the gap scale follows lam)"
              % (RECORD_TAU13, RECORD_TAU21))
    slope = np.polyfit([r[0] for r in dk],
                       [math.log10(r[4]) for r in dk], 1)[0]
    check("S2.1 Davis-Kahan is void: ||PRIME||/gap = %.2e at the deepest"
          " measured rung, growing 10^(%.2f x)" % (dk[-1][4], slope),
          dk[-1][4] > 1e6 and slope > 0.5
          and all(dk[i][4] < dk[i + 1][4] for i in range(len(dk) - 1)),
          "the hypothesis ||Delta|| < gap/2 fails by e^{c x}: the"
          " comparison must be an EXACT cancellation, not a perturbation")

    # --------------------------------------------- IV. THE BLIND SET
    section("IV. THE BLIND SET B(beta) = {alpha : |Phi_Lam(alpha,beta)|"
            " >= pi/4}\n     Phi_Lam(alpha,beta) = sum_gamma arctan(beta"
            "/(alpha-gamma)).  For a real-rooted E,\n     Re[E(alpha+i"
            " beta)^2] < 0 iff the same functional of Z(E) is in"
            " (pi/4,3pi/4)\n     mod pi.  An off-line zero whose real"
            " part lies OUTSIDE B(beta) cannot be\n     exploited by a"
            " minimizer whose zeros sit on the real ordinates: the"
            " census\n     must then differ.  B(beta) is where the"
            " census instrument is blind.")
    alphas = np.arange(2.0, BLIND_ALPHA_HI, BLIND_GRID)
    print("  %8s %12s %12s %12s %12s %12s"
          % ("beta", "|B|/|I|", "half-width", "pred = beta", "hw/beta",
             "mean spacing"))
    blind_rows = []
    for bet in BLIND_BETAS:
        phi = target_phi_lambda(alphas, bet, gam)
        phim = np.abs((phi + math.pi / 2.0) % math.pi - math.pi / 2.0)
        blind = phim >= math.pi / 4.0
        frac = float(blind.mean())
        ncnt = int((gam < BLIND_ALPHA_HI).sum() - (gam < 2.0).sum())
        hw = frac * (BLIND_ALPHA_HI - 2.0) / max(2 * ncnt, 1)
        spac = (BLIND_ALPHA_HI - 2.0) / max(ncnt, 1)
        blind_rows.append((bet, frac, hw, hw / bet))
        print("  %8.3f %12.4f %12.4f %12.4f %12.4f %12.4f"
              % (bet, frac, hw, bet, hw / bet, spac))
    mono = all(blind_rows[i][1] > blind_rows[i + 1][1]
               for i in range(len(blind_rows) - 1))
    small = [r for r in blind_rows if r[0] <= 0.1]
    check("S3.1 B(beta) = union_gamma [gamma-beta, gamma+beta] to"
          " measured accuracy (hw/beta = %s)"
          % " ".join("%.3f" % r[3] for r in blind_rows),
          mono and all(abs(r[3] - 1.0) < 0.05 for r in small),
          "arctan(beta/delta) >= pi/4 <=> delta <= beta; blind fraction"
          " = 2 beta n(alpha) = beta log(alpha/2pi)/pi, so the census"
          " instrument resolves an off-line pair iff beta < half the"
          " local mean spacing")

    # ------------------------------------------ V. PLANTED WORLDS
    section("V. PLANTED WORLDS -- THE DETECTOR IN ACTION\n"
            "     M -> M + 4 Re[b(gam0) b(gam0)^T]: one off-line"
            " quadruple planted into\n     the zero measure at UNCHANGED"
            " source data.  Theorem: the minimizer must\n     acquire"
            " phase pi/4 at gam0, i.e. plant a zero within ~beta of"
            " alpha.")
    xp = PLANT_X
    cc = mpcells[xp]
    Kp = cc["K"]
    bdp = basis_data(xp, Kp)
    band = float(bdp["om"][-1])
    z0 = scan_zeros(bdp, cc["cn"], band)
    n30_xi = int((gam < CENSUS_T).sum())
    print("  reference x=%d K=%d: lam_min=%s  zeros in (0,%.0f): %d"
          "  (Xi census %d)  first zeros %s"
          % (xp, Kp, cc["lam_str"], CENSUS_T,
             int((z0 < CENSUS_T).sum()), n30_xi,
             " ".join("%.4f" % v for v in z0[:4])))
    d1 = abs(float(z0[0]) - float(gam[0])) if len(z0) else float("nan")
    check("S4.0 the unplanted minimizer reproduces the Xi census in"
          " (0,%.0f) and its first zero is gamma_1" % CENSUS_T,
          int((z0 < CENSUS_T).sum()) == n30_xi and d1 < 1e-3,
          "count %d == %d, |z_1 - gamma_1| = %.2e"
          % (int((z0 < CENSUS_T).sum()), n30_xi, d1))

    alpha_gen = 0.5 * (float(gam[0]) + float(gam[1]))     # gap midpoint
    alpha_bl = float(gam[1])                              # on an ordinate

    def plant(al: float, bet: float, real_pair: bool = False):
        with mp.workdps(cc["dps"] + 10):
            if real_pair:
                bq = bvec_mp(xp, Kp, mp.mpf(al))
                upd = [[2 * bq[j] * bq[k] for k in range(Kp)]
                       for j in range(Kp)]
            else:
                bq = bvec_mp(xp, Kp, mp.mpc(al, bet))
                upd = [[4 * (bq[j] * bq[k]).real for k in range(Kp)]
                       for j in range(Kp)]
            Mp = mp.matrix(Kp, Kp)
            for j in range(Kp):
                for k in range(Kp):
                    Mp[j, k] = cc["M"][j, k] + upd[j][k]
        lamp, _g, cnp, _s = eig_mp(Mp, cc["dps"])
        zp = scan_zeros(bdp, cnp, band)
        dmin = float(np.min(np.abs(zp - al))) if len(zp) else float("nan")
        return (lamp, int((zp < CENSUS_T).sum()), dmin, len(zp),
                track_depth(zp, gam))

    print("\n  %-11s %8s %13s %6s %8s %10s %9s %8s"
          % ("site", "beta", "lam_min", "sign", "#(0,30)", "d(alpha,Z)",
             "realness", "track"))
    lamr, c30r, dmr, nzr, tdr = plant(alpha_gen, 0.0, real_pair=True)
    print("  %-11s %8s %13.5e %6s %8d %10.2e %9s %8d"
          % ("REAL ctrl", "--", lamr, "pos" if lamr > 0 else "NEG", c30r,
             dmr, "%d/%d" % (nzr, Kp - 1), tdr))
    plant_rows = []
    for (tag, al) in (("generic", alpha_gen), ("blind", alpha_bl)):
        for bet in PLANT_BETAS:
            lamp, c30, dmin, nz, td = plant(al, bet)
            plant_rows.append((tag, bet, lamp, c30, dmin, nz, td))
            print("  %-11s %8.1e %13.5e %6s %8d %10.2e %9s %8d"
                  % (tag, bet, lamp, "NEG" if lamp < 0 else "pos", c30,
                     dmin, "%d/%d" % (nz, Kp - 1), td))
    gen = [r for r in plant_rows if r[0] == "generic"]
    bl = [r for r in plant_rows if r[0] == "blind"]
    check("S4.0b REAL control: planting a REAL pair at alpha keeps"
          " lam_min > 0 (sum of squares) and adds exactly one zero, AT"
          " alpha", lamr > 0 and c30r == n30_xi + 1 and dmr < 1e-6,
          "lam %.3e, #(0,30) %d = %d+1, d(alpha,Z) %.1e -- so a census"
          " EXCESS by itself only says 'a zero of the target sits at"
          " alpha'; off-line-ness is the SIGN" % (lamr, c30r, n30_xi, dmr))
    gp = [r for r in gen if r[2] > 0]          # perturbative regime
    gn = [r for r in gen if r[2] < 0]          # sign-flipped regime
    bp = [r for r in bl if r[2] > 0]
    bn = [r for r in bl if r[2] < 0]
    seen = [r for r in gp if r[3] > n30_xi]
    top = max(gp, key=lambda r: r[1]) if gp else None
    check("S4.1 GENERIC site, perturbative regime (lam_min > 0): census"
          " EXCESS +1, extra zero within ~beta of alpha, monotone in"
          " beta",
          top is not None and top[3] == n30_xi + 1
          and top[4] <= max(2.5 * top[1], 1e-6)
          and all(r[3] > n30_xi for r in gp if r[1] >= min(
              (s[1] for s in seen), default=float("inf"))),
          "counts %s vs Xi %d; d(alpha,Z) %s"
          % ([r[3] for r in gp], n30_xi,
             " ".join("%.1e" % r[4] for r in gp)))
    check("S4.2 BLIND site (alpha ON an ordinate), perturbative regime:"
          " census UNCHANGED -- the detector is blind exactly on B(beta)",
          bool(bp) and all(r[3] == n30_xi for r in bp),
          "counts %s vs Xi %d (the zero already there does the work)"
          % ([r[3] for r in bp], n30_xi))
    check("S4.3 SIGN-FLIPPED regime (lam_min < 0): the census breaks at"
          " BOTH sites -- blindness does not survive optimisation",
          bool(gn) and bool(bn)
          and all(r[3] != n30_xi for r in gn + bn),
          "generic %s, blind %s vs Xi %d; track depth collapses to %s"
          % ([r[3] for r in gn], [r[3] for r in bn], n30_xi,
             [r[6] for r in gn + bn]))
    b_star = max([r[1] for r in gp] + [0.0])
    check("S4.4 DETECTOR RESOLUTION: the sign flips between beta = %.0e"
          " and %.0e, bracketing sqrt(lam_min) = %.2e"
          % (b_star, min([r[1] for r in gn] + [1.0]),
             math.sqrt(max(cc["lam"], 0.0))),
          bool(gn) and b_star < min(r[1] for r in gn),
          "so rung x detects an off-line pair down to beta* ~"
          " sqrt(lam_min(x)) ~ e^{-c x/2}: deeper rungs see smaller"
          " displacements")

    # ------------------------------------------------- VI. K-SWEEP
    section("VI. K-SWEEP AT FIXED x -- IS THE THINNING INTRINSIC OR A"
            " CUTOFF ARTIFACT?\n     E = sin(a t) P(t)/prod(t^2-om_k^2):"
            " K-1 FREE zeros plus the fixed lattice\n     {om_j, j >= K}"
            " beyond the cutoff.  The free zeros can only cover the"
            " ordinates\n     while the budget lasts: T_bud is defined by"
            " N_Xi(T_bud) = K-1, and the count\n     crossover of the"
            " Nyquist line a T/pi with N_Xi(T) sits at T = 2 pi e x.")
    print("  %5s %10s %12s %8s %8s %8s %8s %9s %9s"
          % ("K", "band edge", "lam_min", "#(0,T0)", "Xi(0,T0)",
             "pos-dep", "cnt-dep", "Xi(0,edge)", "T_pos"))
    ks_rows = []
    for Kv in KSWEEP_K:
        ccc = build_form_mp(KSWEEP_X, Kv, DPS_MP[KSWEEP_X])
        lam, _g, cn, _s = eig_mp(ccc["M"], DPS_MP[KSWEEP_X])
        bdk = basis_data(KSWEEP_X, Kv)
        edge = float(bdk["om"][-1])
        zz = scan_zeros(bdk, cn, edge)
        t0 = min(CENSUS_T, edge)
        c0 = int((zz < t0).sum())
        x0 = int((gam < t0).sum())
        xe = int((gam < edge).sum())
        td = track_depth(zz, gam)
        cd = count_depth(zz, gam)
        tp = float(gam[td - 1]) if td else 0.0
        ks_rows.append((Kv, edge, lam, c0, x0, td, cd, xe, tp))
        print("  %5d %10.3f %12.4e %8d %8d %8d %8d %9d %9.2f"
              % (Kv, edge, lam, c0, x0, td, cd, xe, tp))
    check("S5.1 the census in (0, min(30, edge)) is K-STABLE: %s vs Xi %s"
          % ([r[3] for r in ks_rows], [r[4] for r in ks_rows]),
          all(r[3] == r[4] for r in ks_rows),
          "thinning at a fixed band is NOT a cutoff artifact")
    sat = [r[5] for r in ks_rows if r[1] > 2.0 * float(gam[max(
        r[5] - 1, 0)])] or [r[5] for r in ks_rows[-2:]]
    check("S5.2 the POSITION depth SATURATES in K at fixed x (pos-dep %s"
          " while the free-zero budget K-1 = %s and Xi(0,edge) = %s):"
          " there is an INTRINSIC tracking band at each x"
          % ([r[5] for r in ks_rows], [r[0] - 1 for r in ks_rows],
             [r[7] for r in ks_rows]),
          len(set(sat)) == 1 and ks_rows[-1][5] < ks_rows[-1][7],
          "so the K -> inf limit at fixed x has a finite depth D(x);"
          " TPL(i) is exactly the statement D(x) -> inf")
    check("S5.2b the COUNT depth exceeds the POSITION depth (cnt %s vs"
          " pos %s): the counting functions agree past the point where"
          " the zeros stop sitting ON the ordinates"
          % ([r[6] for r in ks_rows], [r[5] for r in ks_rows]),
          all(r[6] >= r[5] for r in ks_rows),
          "TPL(i) as stated is the WEAKER (count) form; Hurwitz"
          " determination needs the position form")
    # ---- depth ladder in x + zero anatomy
    print("\n  %4s %5s %10s %8s %8s %9s %10s %12s"
          % ("x", "K", "band edge", "pos-dep", "cnt-dep", "T_pos",
             "2 pi x", "|z_i-gam_i| profile"))
    dep_rows = []
    for xv in LADDER_MP:
        ca = mpcells[xv]
        bda = basis_data(xv, ca["K"])
        ea = float(bda["om"][-1])
        za = scan_zeros(bda, ca["cn"], ea)
        td = track_depth(za, gam)
        cd = count_depth(za, gam)
        prof = " ".join("%.0e" % abs(float(za[i]) - float(gam[i]))
                        for i in range(min(5, len(za))))
        dep_rows.append((xv, ca["K"], ea, td, cd, ca))
        print("  %4d %5d %10.2f %8d %8d %9.2f %10.2f   %s"
              % (xv, ca["K"], ea, td, cd,
                 float(gam[td - 1]) if td else 0.0,
                 2.0 * math.pi * xv, prof))
    check("S5.3 both depths GROW with x (pos %s, cnt %s): the empirical"
          " content of TPL(i)"
          % ([r[3] for r in dep_rows], [r[4] for r in dep_rows]),
          all(dep_rows[i][3] <= dep_rows[i + 1][3]
              for i in range(len(dep_rows) - 1))
          and dep_rows[-1][3] > dep_rows[0][3],
          "no proof follows: the growth rate is exactly the open"
          " quantitative statement")
    check("S5.4 lam_min decreases with K at fixed x (%s): the invariant"
          " object is the K -> inf bottom of the sine-kernel frame"
          " operator on PW_a"
          % " ".join("%.1e" % r[2] for r in ks_rows),
          all(ks_rows[i][2] > ks_rows[i + 1][2]
              for i in range(len(ks_rows) - 1)),
          "so the ladder is a JOINT (x, K) limit and TPL must declare"
          " it; the frozen KFAC = 1.25 ties them")

    # ---------------------------------------- VII. SECULAR STRUCTURE
    section("VII. THE SECULAR REPRESENTATION -- WHAT THINNING COSTS IN"
            " THE EIGENVECTOR\n     E(t) = sin(a t) . 2t . sum_k g_k/"
            "(t^2 - om_k^2),  g_k = (-1)^k c_k/n_k.\n     The K-1 free"
            " zeros are the roots of f(u) = sum_k g_k/(u - om_k^2).  On"
            " (om_k^2,\n     om_{k+1}^2) f runs from sign(g_k) inf to"
            " -sign(g_{k+1}) inf, so that mode\n     interval is FORCED"
            " to contain a zero when sign(g_k) = sign(g_{k+1}).  Every"
            "\n     skipped interval -- every unit of thinning below the"
            " Nyquist count a T/pi --\n     therefore costs one SIGN"
            " CHANGE of ((-1)^k c_k).")
    print("  %4s %5s %8s %8s %9s %7s %8s   %s"
          % ("x", "K", "sum occ", "Xi(edge)", "Nyq = K-1", "empty",
             "sign chg", "sign pattern of (-1)^k c_k"))
    sec_rows = []
    for xv in LADDER_MP:
        ca = mpcells[xv]
        bdv = basis_data(xv, ca["K"])
        g = secular(bdv, ca["cn"])
        _ru, occ = secular_roots(bdv, g)
        edge_v = float(bdv["om"][-1])
        nyq = ca["K"] - 1
        xie = int((gam < edge_v).sum())
        empty = int((occ == 0).sum())
        sg = np.sign(g)
        chg = int((sg[:-1] * sg[1:] < 0).sum())
        pat = "".join("+" if v > 0 else "-" for v in sg)
        bad = [k for k in range(len(occ)) if occ[k] == 0
               and sg[k] * sg[k + 1] > 0]
        # exact parity form: occ_k even  <=>  sign(g_k) != sign(g_{k+1})
        par = [k for k in range(len(occ))
               if (occ[k] % 2 == 0) != (sg[k] * sg[k + 1] < 0)]
        nev = int(sum(1 for v in occ if v % 2 == 0))
        sec_rows.append((xv, ca["K"], int(occ.sum()), nyq, xie, empty,
                         chg, pat, bad, occ, par, nev))
        print("  %4d %5d %8d %8d %9d %7d %8d   %s"
              % (xv, ca["K"], int(occ.sum()), xie, nyq, empty, chg,
                 pat if len(pat) <= 40 else pat[:37] + "..."))
        print("       occupancy of the mode intervals: %s"
              % "".join(str(min(v, 9)) for v in occ))
    check("S6.1 the secular occupancy reproduces the thinned census"
          " below the cutoff EXACTLY: sum occ %s vs N_Xi(edge) %s (out"
          " of K-1 = %s Nyquist slots)"
          % ([r[2] for r in sec_rows], [r[4] for r in sec_rows],
             [r[3] for r in sec_rows]),
          all(r[2] == r[4] for r in sec_rows),
          "so E = sin(a t) . 2t . f(t^2)/prod(t^2-om_k^2) and the whole"
          " census question is a question about ONE secular function"
          " (beyond the last pole f is a 16-digit cancellation in"
          " float64 -- its tail roots are declared unresolved here)")
    check("S6.2 EVERY empty mode interval carries a sign change of"
          " ((-1)^k c_k) -- violations %s" % [r[8] for r in sec_rows],
          all(not r[8] for r in sec_rows),
          "#sign changes %s >= #empty %s >= Nyquist deficit (K-1) -"
          " N_Xi(edge) = %s: thinning by n units costs at least n sign"
          " changes of the ground eigenvector"
          % ([r[6] for r in sec_rows], [r[5] for r in sec_rows],
             [r[3] - r[4] for r in sec_rows]))
    check("S6.2b EXACT PARITY IDENTITY: occ_k is even <=> sign(g_k) !="
          " sign(g_{k+1}) -- violating modes %s, so #sign changes %s =="
          " #{k : occ_k even} %s"
          % ([r[10] for r in sec_rows], [r[6] for r in sec_rows],
             [r[11] for r in sec_rows]),
          all(not r[10] and r[6] == r[11] for r in sec_rows),
          "the sign pattern of ((-1)^k c_k) DETERMINES the parity of the"
          " zero count in every mode interval: no analytic input, just"
          " the intermediate value theorem on f")
    check("S6.3 the chain #chg >= #empty >= deficit holds on every rung"
          " and all three grow with x (%s / %s / %s)"
          % ([r[6] for r in sec_rows], [r[5] for r in sec_rows],
             [r[3] - r[4] for r in sec_rows]),
          all(r[6] >= r[5] >= r[3] - r[4] for r in sec_rows)
          and sec_rows[-1][6] > sec_rows[0][6],
          "TPL(i) is thus EQUIVALENT to a statement about the SIGN"
          " PATTERN of the ground eigenvector of M: a finite,"
          " combinatorial reformulation of the open lemma")

    # --------------------------------- VIII. THE DENSITY-DEFICIT LAW
    section("VIII. THE DENSITY-DEFICIT LAW -- WHAT SETS THE SCALE OF"
            " lam_min\n     D(T) = a T/pi - N_Xi(T) = #(Nyquist slots) -"
            " #(ordinates) in (0,T)\n     is the number of mode intervals"
            " the minimiser is FORCED to skip.\n     Closed form: D is"
            " maximised at T = 2 pi x with D_max = x - 3/8 + O(S), and"
            "\n     D > 0 exactly for T < 2 pi e x.  So the ordinates"
            " are sub-Nyquist below\n     2 pi x and super-Nyquist above"
            " -- which is where tracking must stop.")
    print("  %4s %10s %10s %10s %9s %8s %8s %10s"
          % ("x", "argmax D", "2 pi x", "D_max", "x - 7/8", "#empty",
             "#chg", "-log lam/D"))
    dd_rows = []
    for xv in LADDER_MP:
        av = 0.5 * math.log(xv)
        gf = np.asarray([float(v) for v in gam], dtype=float)
        # D jumps down by 1 at each ordinate: evaluate just below each
        cand = av * gf / math.pi - np.arange(len(gf), dtype=float)
        jj = int(np.argmax(cand))
        dmax, targ = float(cand[jj]), float(gf[jj])
        sr = [r for r in sec_rows if r[0] == xv][0]
        lam = float(mpcells[xv]["lam"])
        rate = -math.log(lam) / dmax
        dd_rows.append((xv, targ, dmax, sr[5], sr[6], rate))
        print("  %4d %10.2f %10.2f %10.3f %9.3f %8d %8d %10.2f"
              % (xv, targ, 2.0 * math.pi * xv, dmax, xv - 0.875,
                 sr[5], sr[6], rate))
    for xv, lam in ((13, RECORD_TAU13), (21, RECORD_TAU21)):
        av = 0.5 * math.log(xv)
        gf = np.asarray([float(v) for v in gam], dtype=float)
        cand = av * gf / math.pi - np.arange(len(gf), dtype=float)
        jj = int(np.argmax(cand))
        dmax, targ = float(cand[jj]), float(gf[jj])
        dd_rows.append((xv, targ, dmax, -1, -1,
                        -math.log(lam) / dmax))
        print("  %4d %10.2f %10.2f %10.3f %9.3f %8s %8s %10.2f  [REC]"
              % (xv, targ, 2.0 * math.pi * xv, dmax, xv - 0.875,
                 "--", "--", -math.log(lam) / dmax))
    dev_arg = max(abs(r[1] / (2.0 * math.pi * r[0]) - 1.0)
                  for r in dd_rows)
    dev_max = max(abs(r[2] / r[0] - 1.0) for r in dd_rows)
    check("S7.1 the Nyquist surplus D(T) peaks at T = 2 pi x with"
          " D_max -> x (argmax/2 pi x within %.2f of 1, D_max/x within"
          " %.2f of 1, deviations %s)"
          % (dev_arg, dev_max,
             " ".join("%+.2f" % (r[2] - r[0]) for r in dd_rows)),
          dev_arg <= 0.20 and dev_max <= 0.15,
          "closed form: max_T [a T/pi - N_Xi(T)] = x - 3/8 + O(S), the"
          " -3/8 being 7/8 from the Riemann-von Mangoldt constant less"
          " the 1/2 half-jump; attained where the ordinate density"
          " log(T/2pi)/2pi crosses the Nyquist density a/pi.  The peak"
          " is FLAT (D'' = -1/4 pi^2 x), which is why the discrete"
          " argmax jitters by ~10% while D_max itself does not")
    tp_dev = [abs(float(gam[r[3] - 1]) / (2.0 * math.pi * r[0]) - 1.0)
              for r in dep_rows if r[3] > 0]
    check("S7.2 the POSITION-tracking band ends AT the surplus peak:"
          " T_pos/(2 pi x) = %s"
          % " ".join("%.2f" % (float(gam[r[3] - 1])
                               / (2.0 * math.pi * r[0]))
                     for r in dep_rows if r[3] > 0),
          bool(tp_dev) and max(tp_dev) <= 0.20,
          "the minimiser tracks ordinates exactly while it has spare"
          " zeros (D > 0 and rising) and stops where the ordinates go"
          " super-Nyquist -- the saturation of S5.2 is DENSITY-FORCED,"
          " not a numerical artefact")
    check("S7.3 #empty mode intervals == the surplus D_max to within 1"
          " (%s vs %s)"
          % ([r[3] for r in dd_rows if r[3] >= 0],
             ["%.1f" % r[2] for r in dd_rows if r[3] >= 0]),
          all(abs(r[3] - r[2]) <= 1.0 for r in dd_rows if r[3] >= 0),
          "the skips of S6 are not free choices: their NUMBER is fixed"
          " by counting alone; only their POSITIONS are the open lemma")
    # the RATIO -log lam / D is not constant (it carries the offset);
    # the MARGINAL cost d(-log lam)/dD is.
    lls = [-math.log(float(mpcells[r[0]]["lam"])) if r[0] in mpcells
           else -math.log(RECORD_TAU13 if r[0] == 13 else RECORD_TAU21)
           for r in dd_rows]
    marg = [(lls[i + 1] - lls[i]) / (dd_rows[i + 1][2] - dd_rows[i][2])
            for i in range(len(dd_rows) - 1)]
    mspread = (max(marg) - min(marg)) / (sum(marg) / len(marg))
    print("  ratio -log lam/D_max %s -- NOT constant (offset);"
          % " ".join("%.1f" % r[5] for r in dd_rows))
    print("  MARGINAL d(-log lam)/dD_max %s -- constant to %.0f%%"
          % (" ".join("%.2f" % v for v in marg), 100.0 * mspread))
    check("S7.4 the MARGINAL cost d(-log lam_min)/dD_max is constant"
          " along the ladder x = 3..21 (%s, spread %.0f%%) while the"
          " ratio itself is not (%s)"
          % (" ".join("%.2f" % v for v in marg), 100.0 * mspread,
             " ".join("%.1f" % r[5] for r in dd_rows)),
          mspread <= 0.25,
          "so -log lam_min = c D_max(x) + const with c ~ %.0f over 23"
          " decades: EACH ADDITIONAL FORCED SKIP -- each extra sign"
          " change of the ground eigenvector -- COSTS ONE FIXED FACTOR"
          " e^-c IN THE FRAME BOUND.  The e^{-c x} law of the ladder is"
          " thus a COUNTING law, and the exponent is the Nyquist"
          " surplus, not the bandwidth" % (sum(marg) / len(marg)))

    # ------------------------------------------------------- verdict
    section("IX. VERDICT")
    wall = time.time() - T0_WALL
    check("A9 runtime", wall <= RUNTIME_BAR, "%.1f s (bar %.0f)"
          % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, o, _d in CHECKS if o)
    ok_all = npass == len(CHECKS)
    print("""
DELIVERABLE (proofs in the run report, measurements above):
  T1  Gram identity  Q_x(phi) = sum_rho E(gamma_rho)^2  (unconditional,
      off-line quadruples entering as 4 Re[E^2]): lam(x) >= 0 for all x
      <=> RH; lam nonincreasing in x; lam(x) = the bottom of the frame
      operator of the reproducing kernels at the ordinates, equivalently
      the least positive eigenvalue of the sine-kernel Gram matrix
      [sin(a(g-g'))/(pi(g-g'))] at bandwidth a = (log x)/2.
  T2  Phase criterion (exact): for a real-rooted E, Re[E(alpha+i
      beta)^2] < 0 iff Phi_E(alpha,beta) = sum_{r in Z(E)} arctan(beta/
      (alpha-r)) lies in (pi/4, 3pi/4) mod pi.  Every factor 1 + i beta/
      (alpha-r) has real part 1, so the branch is unambiguous.
  T3  Census dichotomy: under H1 + TPL(i)+(ii), an off-line zero with
      alpha outside the blind set B(beta) = union [gamma-beta,
      gamma+beta] (S3, measured) contradicts the band census.  The
      extremal census is a DETECTOR with resolution beta* ~
      sqrt(lam_min(x)) (S4.4), and blindness does not survive the
      sign-flipped regime (S4.3).
  T4  Sign-pattern reduction (exact parity): occ_k is even iff sign(g_k)
      != sign(g_{k+1}), g_k = (-1)^k c_k/n_k, so #sign changes of
      ((-1)^k c_k) == #{mode intervals with an even zero count} (S6.2b).
      TPL(i) is a statement about the SIGN PATTERN of the ground
      eigenvector of M -- a finite combinatorial restatement.
  T5  Density-deficit law (S7): D(T) = aT/pi - N_Xi(T) peaks at
      T = 2 pi x with D_max = x - 3/8 + O(S).  The position-tracking
      band ends AT that peak (so the saturation of S5.2 is density-
      forced), #skips == D_max, and d(-log lam_min)/dD_max = 11.0 +- 11%
      over 23 decades: the e^{-c x} law of the ladder is a COUNTING law
      -- one fixed factor e^-c per forced sign change.
  O-A density blindness (S1): the density-level block ARCH is exactly
      the smooth zero measure (W4) and its ground state is negative and
      O(1), converging to 2 theta'(0) = -5.372.
  O-B no perturbative comparison (S2): ||PRIME||/gap ~ e^{c x}.

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.""")
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (npass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % ("TPL-REDUCED(sign-pattern) +"
                           " TPL-DICHOTOMY-MEASURED +"
                           " TPL-OBSTRUCTED(density-blind,"
                           " non-perturbative)"
                           if ok_all else "TPL-INSTRUMENT-EDGE"))
    if args.smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("=" * 78)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
