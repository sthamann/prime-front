#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signpos_probe.py -- WHERE THE GROUND-EIGENVECTOR SIGN CHANGES SIT:
NODE DUALITY, A SOURCE-ONLY POSITION PREDICTOR, TOTAL-POSITIVITY CENSUS,
INTERLACING RIGIDITY, AND THE JOINT (x,K) LIMIT.

EXPLORATION PROBE, experiments/ only.  NO RH CLAIM.  NO POSITIVITY CLAIM.
Nothing here is load-bearing, nothing promoted, no marker moves, no gate
closed or narrowed.

=======================================================================
OBJECT (round-85 record; independent re-assembly in this file)
=======================================================================
a = (log x)/2, orthonormal even trig basis e_0 = 1/sqrt(2a),
e_k = cos(om_k u)/sqrt(a), om_k = k pi/a on [-a,a]; Galerkin matrix
M = POLE + ARCH - PRIME of the semilocal Weil form; c = ground
eigenvector (mp), g_k = (-1)^k c_k/n_k; E = sum_k c_k b_k the minimizer.
Round-85 facts consumed (all re-warded here where used): Z1 (M is the
Gram of the zero evaluations), W4 (ARCH is the smooth zero measure
int b_j b_k theta'/pi), T4 parity lemma (mode interval (om_k, om_{k+1})
holds an EVEN number of E-zeros iff sign(g_k) != sign(g_{k+1})), T5
counting law (#sign changes is forced by D_max = x - 3/8).  OPEN: the
POSITIONS of the sign changes.

NODE DUALITY (L1 derivation; the G04 ward measures its density half):
psi_jk = e_j * e_k~ has Fourier transform b_j b_k, so by Parseval
  PRIME[j,k] = 2 sum_{p^m<=x} w_n psi_jk(u_n)
             = int b_j(t) b_k(t) dmu_P(t),
  dmu_P(t)/dt = (1/pi) sum_{p^m<=x} (log p/p^{m/2}) cos(t m log p),
  u_n = m log p, w_n = log p/p^{m/2}.
The single matrix M therefore carries TWO node systems -- the zero
nodes {gamma} (frequency side, unknown) and the prime-power nodes
{u_n} (time side, fully computable) -- glued by the explicit formula
  sum_rho delta_gamma = (pole pair) + theta'(|t|)/pi dt - dmu_P(t)
tested against the band-limited family {b_j b_k}.

LATTICE-EVALUATION LEMMA (exact; ward G06): b_j(om_k) = 0 for j != k
and b_k(om_k) = a/n_k (2a/n_0 at k = 0), hence
  c_k = n_k E(om_k)/a  (k >= 1),   c_0 = n_0 E(0)/(2a):
the eigenvector sign pattern IS the sign sequence of the minimizer at
the Nyquist lattice, and with band real-rootedness
  sigma_k := sign((-1)^k c_k) = sigma_0 (-1)^{k + N_E(om_k)},
N_E = number of E-zeros below om_k.  The positions question is exactly
the question of the PARITY OF THE COUNTING FUNCTION AT THE LATTICE.

SOURCE-ONLY POSITION PREDICTOR (L1, priority computation; NO zero is
consulted anywhere inside it):
  sigma^hat_k = (-1)^{k + Chat(k)},
  Chat(k) = round(N_src(om_k)) for k >= 1, Chat(0) = 0
  (the Riemann-von Mangoldt anchor N = theta/pi + 1 + S holds for
  T > 0 with S(0+) = -1; the band-limited S_x is ODD, S_x(0) = 0, so
  the k = 0 lattice point is anchored by N(0) = 0 directly),
  N_src(T) = theta(T)/pi + 1 + S_x(T),
  theta(T) = Im log Gamma(1/4 + iT/2) - (T/2) log pi   (ARCH data),
  S_x(T) = -(1/pi) sum_{p^m<=x} (log p/p^{m/2})
            * sin(T m log p)/(m log p) * taper(m log p),
  taper: fejer = 1 - u/(2a)  (PRIMARY, declared before any run),
         sharp = 1           (secondary).
Diagnostic channels (cache = ward/target namespace only):
  F1 (counting): sigma^hat vs the cache-parity pattern
     sigma^tgt_k = (-1)^{k + N_true(om_k)};
  F2 (tracking): sigma (eigenvector) vs sigma^tgt.
  eps_k = N_src(om_k) - N_true(om_k) (k >= 1) is the real counting
  error; parity-correct iff round lands even; margin_k = 1/2 - |eps_k|.

FROZEN BARS, LADDERS, SEEDS (before any run)
  KFAC = 1.25 (record); ladder x = 3, 5, 8 gated + x = 13 stretch cell
  (printed, NOT gated; declared).  dps = 45/60/80/115, all >= floor
  4 pi x/ln 10 + 5.  PRIMARY taper = fejer.  K-sweep x = 5,
  K = 6, 8, 11, 16, 22, dps 60.  Scramble control x = 5: atom positions
  u_n -> sorted Uniform(0.15, 2a - 0.05), same weights, SEED 20260814.
  Minor census x = 8 float64, contiguous orders 1..5, tol 1e-10 after
  max-entry normalization.  Jitter: A = uniform +-0.4 d_min (must keep
  the pattern; code ward), B = reflect the closest ordinate across its
  lattice point (must flip it).  W3 record bar: |lam8/3.77e-30 - 1| <
  0.05.  W-DUAL bar 5e-3 rel.  Sign-reliability floor: min|c_k| >
  10^{-(dps-15)}.  Runtime bar 2400 s.

DECLARED SUBSAMPLING AND LIMITS
  Secular-root/occupancy scans (float64 from the mp eigenvector) only
  at x <= 8 (|E(gamma)| ~ sqrt(lam_min) above the 1e-17 cancellation
  floor there; at x = 13 the pattern is read in mp from the eigenvector
  alone -- no root scan).  x = 13 is a stretch cell: all its rows are
  printed, no gate consumes it.  The Epstein/Dirichlet control is NOT
  built: an honest second world needs its own archimedean block
  (conductor, gamma factors) and pole bookkeeping; a wrong ARCH would
  make the control ill-posed -- declared skipped, the scramble control
  carries the burden.  float64 minor census cannot see the e^{-4 pi x}
  bottom cluster; it reads the O(1) block structure only (declared).

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
from scipy.special import loggamma as sp_loggamma

# ------------------------------------------------------------------ bars
KFAC = 1.25
LADDER_MP = (3, 5, 8, 13)
GATED_MP = (3, 5, 8)
DPS_MP = {3: 45, 5: 60, 8: 80, 13: 115}
DPS_FLOOR_MARGIN = 5.0
PRIMARY_TAPER = "fejer"
TAPERS = ("fejer", "sharp")
KSWEEP_X = 5
KSWEEP_K = (6, 8, 11, 16, 22)
SCRAMBLE_X = 5
SEED = 20260814
CENSUS_X = 8
CENSUS_ORDERS = (1, 2, 3, 4, 5)
MINOR_TOL = 1e-10
GAUSS_ORDER = 30
GAUSS_ORDER_MP = 24
PANEL_FAC = 3.0
W3_REL_BAR = 0.05
WDUAL_REL_BAR = 5e-3
SIGN_FLOOR_SHIFT = 15
JITTER_FRAC = 0.4
RUNTIME_BAR = 2400.0

EULER = 0.57721566490153286061
LOG_PI = math.log(math.pi)
GAMMA1_LIT = 14.134725141734693790          # literature constant, ward only
RECORD_TAU8 = 3.77e-30                      # RECORD constant (round 83)

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
    """(u = m log p, w = log p/p^{m/2}) for ALL p^m <= cap.  Own sieve,
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
    return np.exp(-0.5 * v) / (-np.expm1(-2.0 * v))


def basis_data(x: float, K: int) -> dict:
    a = 0.5 * math.log(x)
    om = np.arange(K) * math.pi / a
    nrm = np.full(K, math.sqrt(a))
    nrm[0] = math.sqrt(2.0 * a)
    par = (-1.0) ** np.arange(K)
    return {"x": x, "a": a, "K": K, "om": om, "nrm": nrm, "par": par,
            "L": 2.0 * a}


def bmat(bd: dict, ts: np.ndarray) -> np.ndarray:
    a, om, nrm = bd["a"], bd["om"], bd["nrm"]
    t = np.asarray(ts, float)[:, None]
    d1 = t - om[None, :]
    d2 = t + om[None, :]
    tiny = 1e-13
    s1 = np.where(np.abs(d1) < tiny, a, np.sin(a * d1) / np.where(
        np.abs(d1) < tiny, 1.0, d1))
    s2 = np.where(np.abs(d2) < tiny, a, np.sin(a * d2) / np.where(
        np.abs(d2) < tiny, 1.0, d2))
    return (s1 + s2) / nrm[None, :]


def sep_offdiag(bd: dict, vec: np.ndarray) -> np.ndarray:
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
    p = bd["par"] * math.sinh(0.5 * a) / (0.25 + om ** 2) / nrm
    m_pole = 2.0 * np.outer(p, p)

    npan = max(48, int(math.ceil(PANEL_FAC * 2.0 * (K + 1))))
    v, w = panel_nodes(1e-300, L, npan)
    A = arch_A(v)
    E2 = np.exp(-2.0 * v) / (-np.expm1(-2.0 * v))

    J = np.sin(np.outer(om, v)) @ (w * A)
    m_arch = -2.0 * sep_offdiag(bd, J)

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


def build_form_mp(x: int, K: int, dps: int,
                  atoms_f: list[tuple[float, float]] | None = None) -> dict:
    """The three blocks at working precision dps.  atoms_f overrides the
    prime-power atoms (scramble control); default = own sieve."""
    t0 = time.time()
    with mp.workdps(dps + 10):
        aa = mp.log(x) / 2
        L = 2 * aa
        oms = [mp.mpf(k) * mp.pi / aa for k in range(K)]
        nrm = [mp.sqrt(2 * aa)] + [mp.sqrt(aa)] * (K - 1)
        par = [mp.mpf((-1) ** k) for k in range(K)]

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
        th = [mp.pi * v / aa for v in vs]
        cth = [mp.cos(t) for t in th]
        sth = [mp.sin(t) for t in th]

        J = [mp.mpf(0)] * K
        DI = [mp.mpf(0)] * K
        ck = [mp.mpf(1)] * len(vs)
        sk = [mp.mpf(0)] * len(vs)
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

        if atoms_f is None:
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
        else:
            atoms = [(mp.mpf(u), mp.mpf(w)) for (u, w) in atoms_f]

        P = [mp.mpf(0)] * K
        DP = [mp.mpf(0)] * K
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
        M = mp.zeros(K, K)
        for j in range(K):
            for k in range(K):
                M[j, k] = (2 * pv[j] * pv[k] + m_arch[j, k]
                           - m_prime[j, k])
        for j in range(K):
            for k in range(j):
                s = (M[j, k] + M[k, j]) / 2
                M[j, k] = s
                M[k, j] = s
    return {"x": x, "K": K, "dps": dps, "M": M, "a": float(aa),
            "n_atoms": len(atoms), "build_s": time.time() - t0}


def eig_mp_full(M: mp.matrix, dps: int) -> dict:
    """Full mp spectrum, ascending; ground vector oriented c_0 > 0."""
    with mp.workdps(dps + 10):
        E, Q = mp.eigsy(M)
        n = M.rows
        order = sorted(range(n), key=lambda i: E[i])
        evals = [E[i] for i in order]
        vecs = []
        for pos in order:
            col = [Q[i, pos] for i in range(n)]
            vecs.append(col)
        c = vecs[0]
        if c[0] == 0:
            big = max(range(n), key=lambda i: abs(c[i]))
            flip = c[big] < 0
        else:
            flip = c[0] < 0
        if flip:
            vecs[0] = [-v for v in c]
        lam = float(evals[0])
        gap = float(evals[1] - evals[0])
        minc = min(abs(v) for v in vecs[0])
        return {"evals": evals, "vecs": vecs, "lam": lam, "gap": gap,
                "lam_str": mp.nstr(evals[0], 6), "minc": float(minc),
                "c": vecs[0]}


# ============================================== sign-pattern machinery
def sigma_from_c(c) -> np.ndarray:
    """sigma_k = sign((-1)^k c_k) as +-1 ints (c mp list or f64 array)."""
    out = []
    for k, v in enumerate(c):
        pos = (v > 0)
        out.append(1 if pos == (k % 2 == 0) else -1)
    return np.asarray(out, dtype=int)


def sc_set(sig: np.ndarray) -> list[int]:
    return [k for k in range(len(sig) - 1) if sig[k] * sig[k + 1] < 0]


def secular_roots(bd: dict, g: np.ndarray, pad: float = 12.0
                  ) -> tuple[np.ndarray, np.ndarray]:
    """Roots of f(u) = sum g_k/(u - om_k^2), interval by interval;
    returns (roots in u, occupancy per mode interval)."""
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
                continue
            roots.append(r)
            cnt += 1
        if i < K - 1:
            occ.append(cnt)
    return np.asarray(roots), np.asarray(occ, dtype=int)


# ============================================ the source-only predictor
def theta_arch(T: np.ndarray) -> np.ndarray:
    """Riemann-Siegel theta via log Gamma (archimedean source data)."""
    T = np.asarray(T, float)
    z = 0.25 + 0.5j * T
    return np.imag(sp_loggamma(z)) - 0.5 * T * LOG_PI


def s_band(T: np.ndarray, us: np.ndarray, ws: np.ndarray, a: float,
           taper: str) -> np.ndarray:
    """Band-limited fluctuation S_x(T) from the prime nodes alone."""
    T = np.asarray(T, float)[:, None]
    if len(us) == 0:
        return np.zeros(T.shape[0])
    if taper == "fejer":
        tp = 1.0 - us / (2.0 * a)
    elif taper == "sharp":
        tp = np.ones_like(us)
    else:
        raise ValueError(taper)
    coef = ws / us * tp
    return -(1.0 / math.pi) * (coef[None, :] * np.sin(T * us[None, :])
                               ).sum(1)


def predict_sigma(x: float, K: int, us: np.ndarray, ws: np.ndarray,
                  taper: str | None) -> tuple[np.ndarray, np.ndarray,
                                              np.ndarray]:
    """sigma^hat_k = (-1)^{k + Chat(k)}; taper=None -> density-only P0.
    Anchor: Chat(0) = 0 (N(0) = 0); Chat(k) = round(N_src(om_k)) for
    k >= 1 (RvM formula, valid for T > 0)."""
    a = 0.5 * math.log(x)
    om = np.arange(K) * math.pi / a
    ns = theta_arch(om) / math.pi + 1.0
    if taper is not None:
        ns = ns + s_band(om, us, ws, a, taper)
    chat = np.rint(ns).astype(int)
    chat[0] = 0
    ns[0] = 0.0
    sig = np.asarray([1 if (k + chat[k]) % 2 == 0 else -1
                      for k in range(K)], dtype=int)
    return sig, chat, ns


# ============================================== target-namespace tools
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def target_counts(gam: np.ndarray, om: np.ndarray) -> np.ndarray:
    """N_true(om_k) = #{gamma < om_k} from the READ-ONLY cache."""
    return np.searchsorted(gam, om).astype(int)


def target_sigma(gam: np.ndarray, om: np.ndarray) -> np.ndarray:
    nt = target_counts(gam, om)
    return np.asarray([1 if (k + nt[k]) % 2 == 0 else -1
                       for k in range(len(om))], dtype=int)


def target_theta_prime(t: np.ndarray) -> np.ndarray:
    z = 0.25 + 0.5j * np.abs(np.asarray(t, float))
    return 0.5 * np.real(sp_digamma(z)) - 0.5 * LOG_PI


def target_tail_model(bd: dict, gtop: float) -> np.ndarray:
    nrm = bd["nrm"]
    mag = (2.0 / math.pi) * (math.log(gtop / (2.0 * math.pi)) + 1.0) / gtop
    return (np.outer(bd["par"], bd["par"]) * mag / np.outer(nrm, nrm))


# ================================================== L2 census machinery
def minor_census(X: np.ndarray, orders=CENSUS_ORDERS) -> dict:
    """Contiguous-minor sign census after max-entry normalization."""
    s = float(np.max(np.abs(X)))
    Y = X / s
    n = Y.shape[0]
    out = {}
    for m in orders:
        pos = neg = zer = 0
        neg_locs = []
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                d = float(np.linalg.det(Y[i:i + m, j:j + m]))
                if d > MINOR_TOL:
                    pos += 1
                elif d < -MINOR_TOL:
                    neg += 1
                    if len(neg_locs) < 12:
                        neg_locs.append((i, j))
                else:
                    zer += 1
        out[m] = (pos, neg, zer, neg_locs)
    return out


def variations(vec: np.ndarray) -> int:
    v = np.asarray(vec, float)
    s = np.sign(v[np.abs(v) > 1e-13 * np.max(np.abs(v))])
    return int(np.sum(s[:-1] * s[1:] < 0))


def offtri_ratio(A: np.ndarray) -> float:
    n = A.shape[0]
    mask = np.abs(np.subtract.outer(np.arange(n), np.arange(n))) > 1
    return float(np.linalg.norm(A[mask]) / np.linalg.norm(A))


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
    global LADDER_MP, KSWEEP_K, CENSUS_ORDERS, CENSUS_X
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.smoke:
        LADDER_MP = (3, 5)
        KSWEEP_K = (6, 11)
        CENSUS_ORDERS = (1, 2, 3)
        CENSUS_X = 5

    print("=" * 78)
    print("signpos_probe  POSITIONS OF THE GROUND-EIGENVECTOR SIGN CHANGES")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if args.smoke else ""))
    print("=" * 78)

    # ------------------------------------------------ I. instrument wards
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("G01 AST firewall (no zero oracle, no probe imports; cache only"
          " in ward_/target_/main)", fw_ok, fw_det)
    gam = ward_cache()
    check("G02 ordinate cache health (READ-ONLY, target namespace)",
          len(gam) >= 5000 and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e top %.3f"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT), float(gam[-1])))

    cells: dict[int, dict] = {}
    floors_ok = True
    for xv in LADDER_MP:
        Kv = int(math.ceil(KFAC * xv * math.log(xv)))
        dps = DPS_MP[xv]
        floor = 4.0 * math.pi * xv / math.log(10.0) + DPS_FLOOR_MARGIN
        floors_ok &= dps >= floor
        cc = build_form_mp(xv, Kv, dps)
        ec = eig_mp_full(cc["M"], dps)
        cc.update(ec)
        cells[xv] = cc
        print("    mp cell x=%2d K=%2d dps=%3d (floor %5.1f) lam_min=%s"
              " gap=%.3e min|c_k|=%.2e  %.1fs"
              % (xv, Kv, dps, floor, cc["lam_str"], cc["gap"], cc["minc"],
                 cc["build_s"]), flush=True)
    if 8 in cells:
        rel8 = abs(cells[8]["lam"] - RECORD_TAU8) / RECORD_TAU8
        check("G03 dps floors honored AND lam_min(x=8,K=21) matches the"
              " RECORD 3.77e-30", floors_ok and rel8 < W3_REL_BAR,
              "mine %s vs record %.3e -> rel dev %.3e (bar %.0e)"
              % (cells[8]["lam_str"], RECORD_TAU8, rel8, W3_REL_BAR))
    else:
        check("G03 dps floors honored (record rung not built in smoke)",
              floors_ok, "smoke ladder %s" % (LADDER_MP,))

    # G04 -- density half of the node duality (ARCH == smooth zero measure)
    cell5f = build_form_f64(5, int(math.ceil(KFAC * 5 * math.log(5))))
    npan = 4000
    tt, tw = panel_nodes(1e-9, 1500.0, npan)
    B = bmat(cell5f, tt)
    nsm = target_theta_prime(tt) / math.pi
    dens = 2.0 * (B * (tw * nsm)[:, None]).T @ B
    dens = dens + target_tail_model(cell5f, 1500.0)
    dev_d = float(np.max(np.abs(cell5f["arch"] - dens)))
    scl = float(np.max(np.abs(cell5f["arch"])))
    check("G04 node-duality density half: ARCH == int b_j b_k theta'/pi"
          " (so -PRIME == the prime-node comb -dmu_P)",
          dev_d / scl < WDUAL_REL_BAR,
          "worst |dev| %.3e vs ||ARCH|| %.3f -> rel %.2e (bar %.0e);"
          " the prime half is exact by Parseval (assembly identity)"
          % (dev_d, scl, dev_d / scl, WDUAL_REL_BAR))

    # ------------------------------------ II. truth-pattern extraction
    section("II. THE TRUE SIGN PATTERNS AND THEIR THREE EXACT IDENTITIES\n"
            "     sigma_k = sign((-1)^k c_k);  lattice-evaluation lemma"
            " c_k = n_k E(om_k)/a;\n     parity lemma occ_k even <=>"
            " sign change;  band form sigma_k = (-1)^{k+N_E(om_k)}")
    par_ok = True
    lat_ok = True
    rel_ok = True
    f2_gated_ok = True
    truth: dict[int, dict] = {}
    for xv in LADDER_MP:
        cc = cells[xv]
        Kv = cc["K"]
        bd = basis_data(xv, Kv)
        cf = np.asarray([float(v) for v in cc["c"]])
        sig = sigma_from_c(cc["c"])
        sc = sc_set(sig)
        st = target_sigma(gam, bd["om"])
        f2 = [k for k in range(Kv) if sig[k] != st[k]]
        row = {"sig": sig, "sc": sc, "st": st, "f2": f2, "bd": bd,
               "cf": cf}
        # lattice-evaluation lemma (float64 evaluation of the mp vector)
        Ev = bmat(bd, bd["om"]) @ cf
        pred_c = Ev * bd["nrm"] / bd["a"]
        pred_c[0] = Ev[0] * bd["nrm"][0] / (2.0 * bd["a"])
        big = np.abs(cf) > 1e-8
        dev_l = float(np.max(np.abs(cf[big] - pred_c[big])))
        lat_ok &= dev_l < 1e-8
        # sign reliability
        floor_c = 10.0 ** (-(cc["dps"] - SIGN_FLOOR_SHIFT))
        rel_here = cc["minc"] > floor_c
        if xv in GATED_MP:
            rel_ok &= rel_here
            f2_gated_ok &= not f2
        # parity lemma re-verification (x <= 8 only, declared)
        if xv <= 8:
            g = bd["par"] * cf / bd["nrm"]
            roots_u, occ = secular_roots(bd, g)
            viol = [k for k in range(len(occ))
                    if (occ[k] % 2 == 0) != (sig[k] != sig[k + 1])]
            par_ok &= not viol
            row["occ"] = occ
            row["roots_t"] = np.sqrt(np.maximum(roots_u, 0.0))
            cache_cnt = np.diff(target_counts(gam, bd["om"]))
            row["cache_cnt"] = cache_cnt
            occ_dev = [k for k in range(len(occ))
                       if occ[k] != int(cache_cnt[k])]
            row["occ_dev"] = occ_dev
        truth[xv] = row
        pat = "".join("+" if v > 0 else "-" for v in sig)
        print("  x=%2d K=%2d  #sc=%d  SC=%s" % (xv, Kv, len(sc), sc))
        print("        pattern %s" % pat)
        print("        F2 (pattern vs cache-parity) = %s ; min|c_k|=%.2e"
              " ; lattice-lemma dev %.1e"
              % (f2 if f2 else "empty", cc["minc"], dev_l))
        if "occ" in row:
            print("        occupancy %s ; occ-vs-cache count deviations %s"
                  % ("".join(str(min(v, 9)) for v in row["occ"]),
                     row["occ_dev"] if row["occ_dev"] else "none"))
    check("G05 parity lemma re-verified: occ_k even <=> sign change,"
          " zero violations on x <= 8", par_ok,
          "IVT on the secular function, no analytic input")
    check("G06 lattice-evaluation lemma c_k = n_k E(om_k)/a exact"
          " (components |c_k| > 1e-8, f64 check)", lat_ok,
          "the sign pattern IS the minimizer's sign sequence at the"
          " Nyquist lattice")
    check("G07 sign reliability: min|c_k| clears the mp floor"
          " 10^-(dps-%d) on every gated rung" % SIGN_FLOOR_SHIFT, rel_ok,
          "min|c_k| = %s" % {xv: "%.1e" % cells[xv]["minc"]
                             for xv in GATED_MP if xv in cells})
    check("G08 F2 channel EMPTY on gated rungs: the eigenvector pattern"
          " equals the cache-parity pattern (-1)^{k+N(om_k)}",
          f2_gated_ok,
          "F2 sets: %s%s"
          % ({xv: truth[xv]["f2"] or "empty" for xv in GATED_MP
              if xv in truth},
             ("; x=13 (stretch, ungated): %s"
              % (truth[13]["f2"] or "empty")) if 13 in truth else ""))

    # -------------------------------------- III. L1 source-only predictor
    section("III. L1 -- THE SOURCE-ONLY POSITION PREDICTOR\n"
            "     sigma^hat_k = (-1)^{k + round(theta(om_k)/pi + 1 +"
            " S_x(om_k))}, k >= 1; Chat(0) = 0.\n     P0 = density only"
            " (no primes), P1 = with the prime-node comb (PRIMARY taper"
            " fejer).\n     eps_k = N_src - N_true; margin_k = 1/2 -"
            " |eps_k|.")
    print("  %4s %3s %5s %6s %9s %9s %7s %10s %10s %8s"
          % ("x", "K", "|MP0|", "|MP1f|", "|MP1s|", "arithld", "maxE",
             "minMarg_f", "maxTrunc_f", "xorward"))
    l1_rows = []
    xor_ok = True
    for xv in LADDER_MP:
        cc = cells[xv]
        Kv = cc["K"]
        bd = truth[xv]["bd"]
        us, ws = prime_power_atoms(xv)
        sig = truth[xv]["sig"]
        st = truth[xv]["st"]
        nt = target_counts(gam, bd["om"])
        s0, c0h, n0 = predict_sigma(xv, Kv, us, ws, None)
        preds = {}
        for tp in TAPERS:
            preds[tp] = predict_sigma(xv, Kv, us, ws, tp)
        s1, c1h, n1 = preds[PRIMARY_TAPER]
        mp0 = [k for k in range(Kv) if s0[k] != sig[k]]
        mp1 = {tp: [k for k in range(Kv) if preds[tp][0][k] != sig[k]]
               for tp in TAPERS}
        f1 = [k for k in range(Kv) if s1[k] != st[k]]
        f2 = truth[xv]["f2"]
        # xor ward: MP1 == F1 symmetric-difference F2 (code consistency)
        xr = sorted(set(f1) ^ set(f2))
        xor_here = xr == sorted(mp1[PRIMARY_TAPER])
        xor_ok &= xor_here
        eps = n1 - nt
        eps[0] = 0.0                      # anchored point
        eps0v = n0 - nt
        eps0v[0] = 0.0
        e_int = c1h - nt
        marg = 0.5 - np.abs(eps)
        # truncation need: |S_x - S_true| at the lattice (target-side)
        s_true = nt - theta_arch(bd["om"]) / math.pi - 1.0
        s_x = s_band(bd["om"], us, ws, bd["a"], PRIMARY_TAPER)
        trunc = np.abs(s_x - s_true)
        trunc[0] = 0.0                    # S(0+) = -1 vs odd S_x: anchored
        load = [k for k in mp0 if k not in mp1[PRIMARY_TAPER]]
        l1_rows.append((xv, Kv, mp0, mp1, load, e_int, marg, trunc,
                        eps, nt))
        print("  %4d %3d %5d %6d %9d %9d %7d %10.4f %10.4f %8s"
              % (xv, Kv, len(mp0), len(mp1["fejer"]), len(mp1["sharp"]),
                 len(load), int(np.max(np.abs(e_int))),
                 float(np.min(marg)), float(np.max(trunc)),
                 "ok" if xor_here else "BAD"))
        frag = [k for k in range(Kv)
                if abs(eps[k]) > 0.25 or k in mp0 or k in mp1["fejer"]]
        for k in frag:
            print("        k=%2d om=%8.3f N_true=%2d eps0=%+7.3f"
                  " eps_f=%+7.3f  P0 %s  P1f %s"
                  % (k, bd["om"][k], nt[k], eps0v[k], eps[k],
                     "WRONG" if k in mp0 else "ok",
                     "WRONG" if k in mp1["fejer"] else "ok"))
    gated_rows = [r for r in l1_rows if r[0] in GATED_MP]
    check("G09 the prime-node correction never hurts:"
          " |MP1 primary| <= |MP0| on every gated rung",
          all(len(r[3][PRIMARY_TAPER]) <= len(r[2]) for r in gated_rows),
          "P0 %s vs P1 %s"
          % ([len(r[2]) for r in gated_rows],
             [len(r[3][PRIMARY_TAPER]) for r in gated_rows]))
    check("G10 channel-decomposition ward MP1 == F1 xor F2 on all rungs"
          " (code consistency)", xor_ok, "exact set identity")
    alias = []
    for r in gated_rows:
        xv, Kv = r[0], r[1]
        sig = truth[xv]["sig"]
        s1 = None
        us, ws = prime_power_atoms(xv)
        s1 = predict_sigma(xv, Kv, us, ws, PRIMARY_TAPER)[0]
        for k in range(Kv):
            if s1[k] == sig[k] and r[5][k] != 0:
                alias.append((xv, k, int(r[5][k])))
    check("G11 no even-error aliasing: every parity-correct lattice point"
          " has EXACT count (e_k == 0), gated rungs, primary taper",
          not alias, "aliased points: %s" % (alias or "none"))

    # scramble control
    a5 = 0.5 * math.log(SCRAMBLE_X)
    us5, ws5 = prime_power_atoms(SCRAMBLE_X)
    rng = np.random.default_rng(SEED)
    us_scr = np.sort(rng.uniform(0.15, 2.0 * a5 - 0.05, len(us5)))
    K5 = int(math.ceil(KFAC * SCRAMBLE_X * math.log(SCRAMBLE_X)))
    cc_s = build_form_mp(SCRAMBLE_X, K5, DPS_MP[SCRAMBLE_X],
                         atoms_f=list(zip(us_scr.tolist(), ws5.tolist())))
    ec_s = eig_mp_full(cc_s["M"], DPS_MP[SCRAMBLE_X])
    sig_s = sigma_from_c(ec_s["c"])
    s1_s = predict_sigma(SCRAMBLE_X, K5, us_scr, ws5, PRIMARY_TAPER)[0]
    mp_s = [k for k in range(K5) if s1_s[k] != sig_s[k]]
    print("\n  SCRAMBLE control (x=%d, seed %d): atom positions ->"
          " Uniform(0.15, 2a-0.05), weights kept" % (SCRAMBLE_X, SEED))
    print("    lam_min=%s (sign %s) gap=%.3e min|c|=%.1e"
          % (ec_s["lam_str"], "NEG" if ec_s["lam"] < 0 else "pos",
             ec_s["gap"], ec_s["minc"]))
    print("    scrambled truth pattern %s"
          % "".join("+" if v > 0 else "-" for v in sig_s))
    print("    predictor-on-scramble  %s  -> mismatches %s (|MP|=%d of %d)"
          % ("".join("+" if v > 0 else "-" for v in s1_s),
             mp_s if mp_s else "none", len(mp_s), K5))
    floor_s = 10.0 ** (-(DPS_MP[SCRAMBLE_X] - SIGN_FLOOR_SHIFT))
    check("G12 scramble control resolved (gap and min|c_k| above the mp"
          " floor); its verdict is a measurement, recorded either way",
          ec_s["gap"] > floor_s and ec_s["minc"] > floor_s,
          "lam=%s |MP1 on scramble|=%d/%d"
          % (ec_s["lam_str"], len(mp_s), K5))

    # smooth-world print (density model, no primes; f64, declared)
    ev_sm, Q_sm = sla.eigh(cell5f["pole"] + cell5f["arch"])
    c_sm = Q_sm[:, 0] if Q_sm[0, 0] > 0 else -Q_sm[:, 0]
    sig_sm = sigma_from_c(c_sm)
    s0_5 = predict_sigma(5, cell5f["K"], us5, ws5, None)[0]
    print("  SMOOTH world (POLE+ARCH only, f64): lam_min=%.3f pattern %s"
          % (float(ev_sm[0]),
             "".join("+" if v > 0 else "-" for v in sig_sm)))
    print("    vs density-only predictor P0 %s -> mismatches %d/%d"
          " (print only, no gate)"
          % ("".join("+" if v > 0 else "-" for v in s0_5),
             sum(1 for k in range(cell5f["K"]) if sig_sm[k] != s0_5[k]),
             cell5f["K"]))

    # ------------------------------------- IV. L2 total positivity
    section("IV. L2 -- OSCILLATION / TOTAL POSITIVITY (Gantmacher-Krein)\n"
            "     D = diag((-1)^k).  TN symmetric => PSD, so any block"
            " with a negative\n     eigenvalue is structurally NOT TN in"
            " the checkerboard gauge; the census\n     then measures how"
            " far, and WHERE the sign structure breaks.")
    cxf = build_form_f64(CENSUS_X,
                         int(math.ceil(KFAC * CENSUS_X
                                       * math.log(CENSUS_X))))
    Kc = cxf["K"]
    D = np.diag(cxf["par"])
    la_arch = float(sla.eigh(cxf["arch"], eigvals_only=True,
                             subset_by_index=[0, 0])[0])
    la_pa = float(sla.eigh(cxf["pole"] + cxf["arch"], eigvals_only=True,
                           subset_by_index=[0, 0])[0])
    check("G13 structural kill: lam_min(ARCH) = %.3f < 0 and"
          " lam_min(POLE+ARCH) = %.3f < 0 => the density blocks are NOT"
          " totally nonnegative in ANY gauge" % (la_arch, la_pa),
          la_arch < 0.0 and la_pa < 0.0,
          "TN symmetric implies PSD (principal minors); GK oscillation"
          " theory cannot host the density part")
    mats = {"D(POLE+ARCH)D": D @ (cxf["pole"] + cxf["arch"]) @ D,
            "D M D": D @ cxf["full"] @ D,
            "D PRIME D": D @ cxf["prime"] @ D}
    any_neg_m = False
    for nm, X in mats.items():
        cen = minor_census(X)
        line = " ".join("m=%d:%d+/%d-/%d0" % (m, cen[m][0], cen[m][1],
                                              cen[m][2])
                        for m in CENSUS_ORDERS)
        print("  %-14s census %s" % (nm, line))
        if nm == "D M D":
            any_neg_m = any(cen[m][1] > 0 for m in CENSUS_ORDERS)
            print("      first negative-minor windows (order 2): %s"
                  % (cen[2][3] if 2 in cen else []))
    sc8 = truth[CENSUS_X]["sc"] if CENSUS_X in truth else []
    Xm = mats["D M D"]
    adj = []
    for k in range(Kc - 1):
        d = (Xm[k, k] * Xm[k + 1, k + 1] - Xm[k, k + 1] ** 2)
        adj.append(1 if d > 0 else -1)
    neg_adj = [k for k in range(Kc - 1) if adj[k] < 0]
    print("  adjacent 2x2 principal minors of D M D: negatives at %s"
          % neg_adj)
    print("  sign-change positions SC(x=%d) = %s ; overlap = %s"
          % (CENSUS_X, sc8, sorted(set(neg_adj) & set(sc8))))
    check("G14 D M D is measurably NOT totally nonnegative (>= 1 negative"
          " contiguous minor at f64 scale)", any_neg_m,
          "an oscillation M would force K-1 = %d ground sign changes;"
          " the truth has %d" % (Kc - 1, len(sc8)))
    lad_x = CENSUS_X if CENSUS_X in cells else GATED_MP[-1]
    ccl = cells[lad_x]
    vlist = [variations(np.asarray([float(v) for v in col])
                        * basis_data(lad_x, ccl["K"])["par"])
             for col in ccl["vecs"]]
    osc_pred = [ccl["K"] - 1 - i for i in range(ccl["K"])]
    ndev = sum(1 for i in range(ccl["K"]) if vlist[i] != osc_pred[i])
    print("  eigenvector variation ladder (x=%d, ascending eigenvalue):"
          % lad_x)
    print("    measured %s" % vlist)
    print("    oscillation prediction %s -> deviations %d/%d"
          % (osc_pred, ndev, ccl["K"]))
    check("G15 ladder: bottom-eigenvector variation count == #sign"
          " changes, and the GK oscillation ladder measurably fails",
          vlist[0] == len(truth[lad_x]["sc"]) and ndev > 0,
          "v_0 = %d vs #SC = %d; deviations %d"
          % (vlist[0], len(truth[lad_x]["sc"]), ndev))
    inv_pa = np.linalg.inv(cxf["pole"] + cxf["arch"])
    inv_ar = np.linalg.inv(cxf["arch"])
    with mp.workdps(DPS_MP[5] + 10):
        Minv = cells[5]["M"] ** -1
        Minv_f = np.array([[float(Minv[i, j]) for j in range(cells[5]["K"])]
                           for i in range(cells[5]["K"])])
    r_pa = offtri_ratio(inv_pa)
    r_ar = offtri_ratio(inv_ar)
    r_m = offtri_ratio(Minv_f)
    print("  Green/one-pair test (inverse tridiagonality, off-tri mass):"
          " inv(P+A) %.3f  inv(ARCH) %.3f  inv(M, x=5 mp) %.3f"
          % (r_pa, r_ar, r_m))
    check("G16 M is NOT a Green/one-pair matrix: its inverse is"
          " rank-one-dominated (cc^T/lam_min), off-tri mass > 0.1",
          r_m > 0.1, "off-tri ratios: M %.3f, P+A %.3f, ARCH %.3f"
          % (r_m, r_pa, r_ar))

    # ------------------------------------------- V. L3 rigidity
    section("V. L3 -- RIGIDITY OF THE MAP {ordinates} -> {sign pattern}\n"
            "     The map flips a parity only when a node crosses a"
            " lattice point om_k;\n     its modulus of continuity is the"
            " node-to-lattice distance.")
    rig_ok = True
    d_rows = []
    for xv in [v for v in LADDER_MP if v <= 8]:
        bd = truth[xv]["bd"]
        omv = bd["om"]
        cell_w = math.pi / bd["a"]
        edge = float(omv[-1])
        gg = gam[gam < edge]
        dg = np.min(np.abs(gg[:, None] - omv[None, 1:]), axis=1)
        d_tgt = float(np.min(dg))
        i_min = int(np.argmin(dg))
        zt = truth[xv]["roots_t"]
        zt = zt[zt < edge]
        d_e = (float(np.min(np.abs(zt[:, None] - omv[None, 1:])))
               if len(zt) else float("nan"))
        # margins in the three coordinates
        minc = cells[xv]["minc"]
        d_rows.append((xv, d_tgt, d_e, cell_w, minc))
        print("  x=%2d cell=%6.3f  d(ordinate,lattice)=%8.5f"
              " (=%.3f cell)  d(E-zero,lattice)=%8.5f  min|c_k|=%.2e"
              % (xv, cell_w, d_tgt, d_tgt / cell_w, d_e, minc))
        # jitter A: uniform +-JITTER_FRAC*d_tgt (must preserve; code ward)
        rj = np.random.default_rng(SEED + xv)
        gj = gg + rj.uniform(-1.0, 1.0, len(gg)) * JITTER_FRAC * d_tgt
        stA = target_sigma(np.sort(gj), omv)
        okA = bool(np.all(stA == truth[xv]["st"]))
        # jitter B: reflect the closest ordinate across its lattice point
        gb = gg.copy()
        kb = int(np.argmin(np.abs(gg[i_min] - omv[1:]))) + 1
        gb[i_min] = 2.0 * omv[kb] - gg[i_min]
        stB = target_sigma(np.sort(gb), omv)
        okB = not bool(np.all(stB == truth[xv]["st"]))
        rig_ok &= okA and okB
        print("        jitter A (+-%.2f d_min): pattern %s ; jitter B"
              " (reflect gamma_%d across om_%d): pattern %s"
              % (JITTER_FRAC, "UNCHANGED" if okA else "CHANGED",
                 i_min + 1, kb, "FLIPPED" if okB else "unchanged"))
    check("G17 rigidity: the pattern is invariant under sub-margin"
          " jitter and flips exactly when a node crosses the lattice",
          rig_ok and all(r[1] > 0 for r in d_rows),
          "moduli d(ordinate,lattice)/cell = %s"
          % ["%.3f" % (r[1] / r[3]) for r in d_rows])

    # ------------------------------------------- VI. L4 K-sweep
    section("VI. L4 -- SIGN-CHANGE POSITIONS ACROSS K AT FIXED x = %d\n"
            "     The lattice om_k = k pi/a is K-independent; growing K"
            " only extends it.\n     A well-posed reduction needs the"
            " positions on a fixed range to be K-stable." % KSWEEP_X)
    ks_rows = []
    for Kv in KSWEEP_K:
        if Kv == cells[KSWEEP_X]["K"]:
            ec = cells[KSWEEP_X]
        else:
            ccc = build_form_mp(KSWEEP_X, Kv, DPS_MP[KSWEEP_X])
            ec = eig_mp_full(ccc["M"], DPS_MP[KSWEEP_X])
        sigv = sigma_from_c(ec["c"])
        scv = sc_set(sigv)
        us, ws = prime_power_atoms(KSWEEP_X)
        s1v = predict_sigma(KSWEEP_X, Kv, us, ws, PRIMARY_TAPER)[0]
        mpv = [k for k in range(Kv) if s1v[k] != sigv[k]]
        ks_rows.append((Kv, ec["lam"], sigv, scv, mpv))
        print("  K=%2d lam=%12.4e  SC=%-24s |MP1f|=%d  pattern %s"
              % (Kv, ec["lam"], scv, len(mpv),
                 "".join("+" if v > 0 else "-" for v in sigv)))
    kmin = KSWEEP_K[0]
    base_sc = set(k for k in ks_rows[0][3])
    stable = True
    for r in ks_rows[1:]:
        got = set(k for k in r[3] if k <= kmin - 2)
        stable &= got == set(k for k in base_sc if k <= kmin - 2)
    prefix_agree = all(
        bool(np.all(r[2][:kmin] == ks_rows[0][2][:kmin]))
        for r in ks_rows[1:])
    check("G18 K-stability measured and recorded: sign-change positions"
          " on the common range k <= %d across K = %s" % (kmin - 2,
                                                          list(KSWEEP_K)),
          stable and prefix_agree,
          "common-range SC sets %s; verdict %s"
          % ([sorted(k for k in r[3] if k <= kmin - 2) for r in ks_rows],
             "K-STABLE" if (stable and prefix_agree) else "K-DRIFT"))

    # ------------------------------------------------------- verdict
    section("VII. VERDICT")
    wall = time.time() - T0_WALL
    check("G19 runtime", wall <= RUNTIME_BAR, "%.1f s (bar %.0f)"
          % (wall, RUNTIME_BAR))
    exact_gated = all(len(r[3][PRIMARY_TAPER]) == 0 for r in gated_rows)
    exact_13 = (len([r for r in l1_rows if r[0] == 13]) == 1
                and len([r for r in l1_rows
                         if r[0] == 13][0][3][PRIMARY_TAPER]) == 0)
    load_tot = sum(len(r[4]) for r in l1_rows)
    min_marg = min(float(np.min(r[6])) for r in l1_rows)
    v1 = ("SIGNPOS-PREDICTOR-EXACT" if exact_gated
          else "SIGNPOS-PREDICTOR-INEXACT")
    npass = sum(1 for _n, o, _d in CHECKS if o)
    ok_all = npass == len(CHECKS)
    print("""
DELIVERABLE (the mathematics is in the run report):
  D1  Node duality: M = Gram of zero nodes = POLE + smooth density
      - prime-node comb; the sign pattern sigma_k = sign((-1)^k c_k)
      equals the minimizer's sign sequence at the Nyquist lattice
      (lattice-evaluation lemma, G06), i.e. the PARITY of the counting
      function at the source lattice.
  D2  Source-only predictor sigma^hat (theta + band-limited prime sum):
      exactness measured above; the CATCH is exact and two-sided --
      correctness at k <=> |eps_k| < 1/2, and BOTH sides are the open
      quantities: the margin 1/2 - |eps_k| is the ordinate-to-lattice
      distance in counting units (L3), and keeping the band-limited
      truncation |S_x - S| below it for ALL x is pointwise control of
      S(T) at the mean-spacing scale -- Littlewood-class information,
      not obtainable from density (Obstruction A) nor from mean-square
      bounds; measured min margin above.
  D3  Total positivity: the density blocks have negative eigenvalues,
      so no gauge makes them TN (G13); M itself is measurably non-TN
      and non-Green (G14/G16); GK oscillation theory addresses the
      MAXIMAL pattern only -- the shortfall (K-1) - #SC = N_Xi(edge) is
      the arithmetic content and GK cannot localize it.
  D4  Rigidity: the map {nodes} -> {pattern} is locally constant with
      modulus = node-to-lattice distance (G17): TPL(i)-positions ==
      'the prime block never carries a node across the lattice'.
  D5  K-stability of the positions measured (G18).

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.""")
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (npass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s(gated x=3/5/8%s; arithmetic load %d; min margin"
          " %.4f; catch = half-integer-margin control of the band-"
          "limited S == TPL(i) itself) + %s + SIGNPOS-%s + SIGNPOS-%s"
          % (v1,
             ", x=13 %s" % ("exact" if exact_13 else "INEXACT")
             if any(r[0] == 13 for r in l1_rows) else "",
             load_tot, min_marg,
             "SIGNPOS-TP-DEAD(density indefinite; M non-TN, non-Green;"
             " GK localizes nothing)",
             "RIGID" if rig_ok else "FRAGILE",
             "K-STABLE" if (stable and prefix_agree) else "K-DRIFT"))
    if args.smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("=" * 78)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
