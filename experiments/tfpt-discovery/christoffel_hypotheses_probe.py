#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_hypotheses_probe -- PRIME.CASE.HYPOTHESES.01
(EXPLORATION ONLY, experiments/; round 42: the strategy memo's FAST
FALSIFIER battery against the hypotheses of the target theorem
"triangular bulk-port Christoffel domination => T_h <= 1",
2026-08-09).

CONTEXT (machinery verbatim from freetail_case_bridge_probe):
the deployed tilde-measures carry atoms nu~_m at nodes y_m;
T_m = nu~_m K_h(y_m, y_m); lambda_h(y) = 1/K_h(y, y).  The free-tail
measure mu_h^ft (append a_k = 0, b_k = 1/2 for k > h) has the EXACT
ac density w_h(x) = 2 m0 f(2x), f = Im m / pi by coefficient
stripping down to the free m-function -- and J_h^ft reproduces the
deployed CD kernel K_h EXACTLY at the deployed nodes (freetail B1).
Every hypothesis below is a property of (w_h, K_h, nu~) that the
target theorem needs; each gets a measured verdict.  A falsification
is a finding.  Heavy rungs kz {9, 12, 13, 26, 40}; controls kz 9.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first run:
A_h = 20, C = 2, port aliases m = 1..8, edge-fit window
s = 1 - x in [max(1e-4, A_h/h^2), 1e-2], 25 log-spaced fit points,
shallow/deep = the 2 lowest-/highest-h heavy rungs, pair medians):

 H1  BULK OSCILLATION: on the bulk zone B_h (see CONCRETIZATIONS:
     min(1 -+ x) >= A_h/h^2, A_h = 20) compute per bulk node the
     oscillation osc = max - min of log w_h over I_h(x) =
     [x -+ C (sqrt(1-x^2)/h + 1/h^2)], C = 2, 33 uniform samples;
     report the max over bulk nodes per rung.  SUPPORTED iff the
     max oscillation is non-increasing in h (deep-pair median <=
     shallow-pair median); FALSIFIED if it grows.

 H2  LOCAL DOUBLING: per bulk node the ratio
     mu_h^ft(I(y, 2r)) / mu_h^ft(I(y, r)) at r = rho_h(y) =
     sqrt(1-y^2)/h + 1/h^2 (ac part; Gauss-Legendre 96 per
     interval; intervals stay inside the band by construction);
     report the sup per rung.  SUPPORTED iff bounded (deep-pair
     median <= 1.2 x shallow-pair median), FALSIFIED if growing.

 H3  BULK MARGIN SEPARATION: per bulk node S_h^B(y) =
     pi sqrt(1-y^2) w_h(y) K_h(y,y) / h and R_h^B_m =
     nu~_m / M_h(y_m), M_h = pi sqrt(1-y^2) w_h / h; the product
     margin 1 - S R = 1 - T_m (exact; w_h cancels).  Report the
     min bulk margin per rung, its location a* = 2 h^2 (1 - y*),
     and bulk medians of S and R.  SUPPORTED iff the min bulk
     margin >= 0.05 on EVERY rung (bulk safe, difficulty confined
     to the port); FALSIFIED if it shrinks toward 0 or flips sign.

 H4  PORT EDGE MODEL: fit w_h(x) ~ c_h (1-x)^alpha at x -> 1 on
     the CUMULATIVE edge mass W_h(s) = Int_{1-s}^{1} w_h dx ~
     c_h s^(alpha+1)/(alpha+1) (integration kills the polynomial-
     scale oscillation), window s in [max(1e-4, A_h/h^2), 1e-2];
     sub-window fits [lo, 1e-3] / [1e-3, 1e-2] gauge drift; Jost
     endpoint J_h(1) = u_0(E = 2) by downward recursion with the
     free tail; near-edge point spectrum eps_h^+ = min(E_j - 2).
     Typed: BESSEL-GENERIC iff |alpha - 0.5| <= 0.15 on every rung
     and max c_h / min c_h <= 10 (c_h at the common median alpha);
     RESONANT-MODEL-NEEDED iff median alpha < 0 (edge-divergent
     density) OR any rung has an outside eigenvalue with
     h^2 eps_h^+ / 2 <= 200 (near-edge bound state) OR |J_h(1)|
     decays (deep-pair median <= 0.5 x shallow-pair median);
     FALSIFIED if neither pattern is stable.

 H5  BESSEL MASS PROFILE: port aliases m = 1..8 = the 8 neg nodes
     closest to x = 1; record a_{h,m} = 2 h^2 (1 - y_{h,m}) and
     the scaled masses nuhat_m = h^(2 alpha* + 2) nu~_{h,m} / c_h
     with the COMMON H4 alpha* (median over heavy rungs) and the
     per-rung c_h refit at alpha* (cross-rung c comparison is only
     defined at fixed exponent).  SUPPORTED iff both profiles
     converge along fixed aliases: last-third drift (deepest vs
     second-deepest rung) <= 20 % for every alias; else FALSIFIED.

 H6  MASK CONSTANT: delta_h = h Dtheta / pi = 2h/L; the deployed-
     mask flat-weight Christoffel ratio per rung (flat masses on
     the pos node mask, bulk = tau-deciles 3..8 median -- verbatim
     the freetail flat-mask benchmark); residual against pi^2/8 =
     1.2337 as delta_h -> 1/2.  SUPPORTED iff |resid| <= 0.05 on
     the deepest rung OR the deep-pair median |resid| <= 0.5 x the
     shallow-pair median; else the scalar Fejer model is FALSIFIED
     (the mask factor depends on more than delta_h -- an honest
     kill of the pi^2/8 numerology).

 H7  FIRST-CORRECTION SIGN: exact Jacobi(alpha, beta) reference on
     [-1, 1] with the per-rung H4 alpha (+1 end) and beta (-1 end
     fit, same estimator); orthonormal chain from the closed-form
     Jacobi recurrence; Lambda_h^E = 1/K_h^Jac(y, y), edge-matched
     normalization mass = c_h 2^(alpha+1) B(alpha+1, beta+1) (the
     gamma SIGN is normalization-free).  At the port aliases:
     S_h^E = Lambda_h^E / lambda_h, R_h^E = nu~ / Lambda_h^E,
     gamma_m = (lambda_h - nu~_m) / Lambda_h^E.  Sign census +
     h-trend.  SUPPORTED iff gamma_m > 0 on every rung and alias;
     FALSIFIED iff any CONVERGED gamma_m <= 0 (deep pair).

 C   CONTROLS (kz 9, scramble seed 1): must-fire on the signs the
     theorem lives on: (ch1) the H3 bulk margin flips sign
     (min < 0, i.e. T > 1 in the bulk) OR (ch2) a port-alias
     first correction flips (some T_alias >= 1 <=> gamma <= 0).
     Which channel fires is stated.

FROZEN CONCRETIZATIONS (pre-registered with the protocol, before
the first run):
  (i)   the contract writes B_h = {1 - x >= A_h/h^2}; concretized
        TWO-SIDEDLY (min(1 -+ x) >= A_h/h^2) because w_h vanishes/
        diverges at BOTH spectral edges and log w_h over I_h(x) is
        undefined across an edge (several rungs carry a node at
        x = -1 exactly); the one-sided min margin is printed
        alongside in H3 for the record.
  (ii)  the edge exponent is fit on the CUMULATIVE mass W_h(s)
        (pointwise log w_h oscillates on the polynomial scale
        through the whole window); c_h from the intercept.
  (iii) cross-rung c_h statements (H4 boundedness, H5 scaling) use
        the COMMON median alpha*; per-rung alphas type H4.
  (iv)  the H7 Jacobi reference is normalized to match the fitted
        +1-edge constant (mass c_h 2^(alpha+1) B(alpha+1, beta+1));
        the gamma sign -- the H7 bar -- does not depend on this.
  (v)   trend statistic everywhere: heavy rungs sorted by h,
        shallow = median of the 2 lowest, deep = median of the
        2 highest.

KILLS: pipeline breaks (chain short, fits non-finite, Jacobi
recurrence self-test fails, quadrature leaves the band) ->
PIPELINE-BROKEN; controls silent -> CONTROL-DEAD.  H1..H7 verdicts
are MEASUREMENTS (SUPPORTED / FALSIFIED / RESONANT-MODEL-NEEDED /
BESSEL-GENERIC), never kills: a falsification is a finding.

VERDICT (frozen enum): HYPOTHESES-MEASURED (+ the seven-item typed
table) / PIPELINE-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  Pre-sizing (frozen with the
  protocol, before the battery ran) disclosed that rung kz 9
  carries one anomalous port alias with nu~ = 6.97e-8 (a near-
  vanishing atom, ~50x below its neighbours), so the H5 drifts
  carry a 1e-300 denominator floor; kz 9 is not in the last-third
  drift window (kz 26 vs kz 40) and no bar depends on the guard.

NO RH claim: these are measured properties of the deployed family
and its free-tail completion; no hypothesis verdict proves or
refutes the target theorem -- it maps which of its assumptions
survive contact with the data.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; freetail_case_bridge_
probe (chain + free-tail density + flat-mask benchmark, verbatim),
declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_hypotheses_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

HEAVY = (9, 12, 13, 26, 40)
A_H = 20.0                     # bulk cut: min(1 -+ x) >= A_H / h^2
C_OSC = 2.0                    # H1 interval half-width factor
N_OSC = 33                     # H1 samples per interval
N_GL = 96                      # H2 Gauss-Legendre points/interval
N_EDGE = 20001                 # edge cumulative theta-grid points
S_HI = 1.0e-2                  # edge-fit window top
S_LO_FLOOR = 1.0e-4            # edge-fit window floor
S_MID = 1.0e-3                 # sub-window split
N_FIT = 25                     # log-spaced fit points
N_ALIAS = 8                    # port aliases m = 1..8
H2_BAR = 1.2                   # H2 doubling trend bar
H3_BAR = 0.05                  # H3 min bulk margin bar
H4_ALPHA_TOL = 0.15            # |alpha - 1/2| for BESSEL-GENERIC
H4_C_SPREAD = 10.0             # max c / min c for BESSEL-GENERIC
H4_NEAR_EDGE_A = 200.0         # h^2 eps/2 bar for near-edge eig
H4_JOST_DECAY = 0.5            # |J| deep/shallow decay bar
H5_DRIFT = 0.20                # last-third profile drift bar
H6_RESID = 0.05                # |flat-mask - pi^2/8| abs bar
H6_DECAY = 0.5                 # residual deep/shallow decay bar
PI2_8 = math.pi ** 2 / 8.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------------ pipeline
# (grid density, folded arm measures, Lanczos chain, CD kernel, free-tail
#  m-function, flat-mask benchmark: verbatim from freetail_case_bridge_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def build_rung(kz, scramble_seed=None):
    """Window -> pos/neg folded measures -> chain -> CD diagonal + T."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = vs * Kdiag
    tau_m = (2.0 * math.pi * uf_n / L) / D
    dec = np.minimum((10 * tau_m / np.max(tau_m)).astype(int), 9)
    return dict(kz=kz, h=h, L=L, D=D, xs=xs, ws=ws, ys=ys, vs=vs,
                dec=dec, al=al, be=be, m0=m0, Kdiag=Kdiag, T=T,
                A2=2.0 * be[:h], B2=2.0 * al[:h])


def m_strip(A2, B2v, E):
    """Exact m-function of J_h^ft on the essential spectrum: free
    boundary value + coefficient stripping (Herglotz-preserving)."""
    m = 0.5 * (-E + 1j * np.sqrt(4.0 - E * E))
    for k in range(len(A2) - 1, -1, -1):
        m = 1.0 / (B2v[k] - E - (A2[k] ** 2) * m)
    return m


def shoot_u0(A2, B2v, E):
    """Renormalized downward shooting: u_0(E) for real |E| > 2."""
    h = len(A2)
    beta = 0.5 * (E + np.sign(E) * np.sqrt(E * E - 4.0))
    up = np.ones_like(E)
    upp = 1.0 / beta
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((E - Bn) * up - An * upp) / Anm1
        upp, up = up, u
        sc = np.maximum(np.maximum(np.abs(up), np.abs(upp)), 1e-300)
        up = up / sc
        upp = upp / sc
    return up


def point_spectrum(A2, B2v):
    """Eigenvalues of J_h^ft outside [-2, 2] (shooting + bisection)."""
    h = len(A2)
    emax = 2.0
    for n in range(1, h + 2):
        b = B2v[n - 1] if n <= h else 0.0
        left = A2[n - 2] if 2 <= n <= h + 1 else (1.0 if n > h + 1
                                                  else 0.0)
        right = A2[n - 1] if n <= h else 1.0
        emax = max(emax, abs(b) + left + right)
    emax += 0.5
    tmax = 0.5 * (emax + math.sqrt(emax * emax - 4.0))
    ts = 1.0 + np.geomspace(1e-9, tmax - 1.0, 4000)
    eigs = []
    for sgn in (+1.0, -1.0):
        E = sgn * (ts + 1.0 / ts)
        v = shoot_u0(A2, B2v, E)
        idx = np.nonzero(v[:-1] * v[1:] < 0.0)[0]
        for i in idx:
            lo, hi = ts[i], ts[i + 1]
            flo = float(shoot_u0(A2, B2v,
                                 np.array([sgn * (lo + 1.0 / lo)]))[0])
            for _ in range(64):
                mid = 0.5 * (lo + hi)
                fm = float(shoot_u0(
                    A2, B2v, np.array([sgn * (mid + 1.0 / mid)]))[0])
                if flo * fm <= 0.0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            t = 0.5 * (lo + hi)
            eigs.append(sgn * (t + 1.0 / t))
    return eigs


def voronoi_density(x_sorted, w_sorted):
    edges = np.empty(len(x_sorted) + 1)
    edges[1:-1] = 0.5 * (x_sorted[1:] + x_sorted[:-1])
    edges[0] = x_sorted[0] - 0.5 * (x_sorted[1] - x_sorted[0])
    edges[-1] = x_sorted[-1] + 0.5 * (x_sorted[-1] - x_sorted[-2])
    return w_sorted / np.diff(edges)


def nearest_idx(x_sorted, y):
    i = np.searchsorted(x_sorted, y)
    i0 = np.clip(i - 1, 0, len(x_sorted) - 1)
    i1 = np.clip(i, 0, len(x_sorted) - 1)
    return np.where(np.abs(x_sorted[i1] - y)
                    < np.abs(x_sorted[i0] - y), i1, i0)


def mnt_ratio(Kdiag, ys, h, wdens):
    return (Kdiag * math.pi
            * np.sqrt(np.maximum(1.0 - ys ** 2, 1e-12)) * wdens / h)


def flat_structure(xs, h, ys, mask):
    """Structure factor of the FLATTENED measure on the same node
    set (flat masses; self-consistent Voronoi density)."""
    o = np.argsort(xs)
    xs_s = xs[o]
    ws_s = np.full(len(xs_s), 1.0 / len(xs_s))
    al, be, m0, steps = lanczos_chain(xs_s, ws_s, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kd = np.sum(Pn ** 2, axis=1)
    wv = voronoi_density(xs_s, ws_s)[nearest_idx(xs_s, ys)]
    return float(np.median(mnt_ratio(Kd, ys, h, wv)[mask]))


# ------------------------------------------------------- battery helpers
def w_ft(r, x):
    """The exact free-tail ac density w_h at x (any shape)."""
    E = np.clip(2.0 * np.asarray(x, float), -2.0 + 1e-15, 2.0 - 1e-15)
    return 2.0 * r["m0"] * m_strip(r["A2"], r["B2"], E).imag / math.pi


def bulk_mask(r):
    """FROZEN two-sided bulk zone (CONCRETIZATION i)."""
    ys, h = r["ys"], r["h"]
    return np.minimum(1.0 - ys, 1.0 + ys) >= A_H / h ** 2


def edge_cumulative(r, sign):
    """Cumulative edge mass W(theta) = Int_0^theta w(sign cos t)
    sin t dt on a uniform theta grid up to s = S_HI."""
    th_max = math.acos(1.0 - S_HI)
    thg = np.linspace(0.0, th_max, N_EDGE)
    w = w_ft(r, sign * np.cos(thg[1:]))
    integ = w * np.sin(thg[1:])
    Wc = np.concatenate(
        [[0.0], np.cumsum(0.5 * (integ[1:] + integ[:-1])
                          * np.diff(thg[1:]))])
    return thg[1:], Wc


def fit_powerlaw(thg, Wc, lo, hi):
    """log W = (alpha+1) log s + log(c/(alpha+1)) on [lo, hi]."""
    s = np.geomspace(lo, hi, N_FIT)
    Ws = np.interp(np.arccos(1.0 - s), thg, Wc)
    if np.any(Ws <= 0.0):
        return None
    A = np.vstack([np.log(s), np.ones_like(s)]).T
    sol, *_ = np.linalg.lstsq(A, np.log(Ws), rcond=None)
    alpha = float(sol[0]) - 1.0
    c = math.exp(float(sol[1])) * float(sol[0])
    resid = float(np.max(np.abs(np.log(Ws) - A @ sol)))
    return dict(alpha=alpha, c=c, resid=resid, s=s, Ws=Ws)


def c_at_alpha(s, Ws, alpha):
    """Refit only the constant at a FIXED exponent (median)."""
    return float(np.median(Ws * (alpha + 1.0) / s ** (alpha + 1.0)))


def jost_endpoint(A2, B2v):
    """u_0(E = 2): downward recursion, free-tail solution u = 1."""
    h = len(A2)
    up, upp = 1.0, 1.0
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((2.0 - Bn) * up - An * upp) / Anm1
        upp, up = up, u
    return float(up)


def jacobi_chain(a, b, n):
    """Closed-form orthonormal recurrence for the Jacobi weight
    (1-x)^a (1+x)^b on [-1, 1]: al_k, be_k, unit-constant mass
    2^(a+b+1) B(a+1, b+1)."""
    al = np.empty(n)
    be = np.empty(n)
    al[0] = (b - a) / (a + b + 2.0)
    for k in range(1, n):
        d = 2.0 * k + a + b
        al[k] = (b * b - a * a) / (d * (d + 2.0))
    b1 = 4.0 * (a + 1.0) * (b + 1.0) / ((a + b + 2.0) ** 2
                                        * (a + b + 3.0))
    be[0] = math.sqrt(b1)
    for k in range(2, n + 1):
        d = 2.0 * k + a + b
        bk = (4.0 * k * (k + a) * (k + b) * (k + a + b)
              / (d * d * (d * d - 1.0)))
        be[k - 1] = math.sqrt(bk)
    mass = math.exp((a + b + 1.0) * math.log(2.0)
                    + math.lgamma(a + 1.0) + math.lgamma(b + 1.0)
                    - math.lgamma(a + b + 2.0))
    return al, be, mass


def pair_stat(vals_by_h):
    """CONCRETIZATION (v): shallow/deep pair medians."""
    v = list(vals_by_h)
    return (float(np.median(v[:2])), float(np.median(v[-2:])))


def port_aliases(r):
    """The N_ALIAS neg nodes closest to x = 1 (sorted inward)."""
    o = np.argsort(-r["ys"])[:N_ALIAS]
    return o


def main():
    section("PRIME.CASE.HYPOTHESES.01 -- fast falsifier battery for "
            "the bulk-port Christoffel theorem (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    alc, bec, msc = jacobi_chain(-0.5, -0.5, 6)
    cheb_ok = (max(abs(float(x)) for x in alc) <= 1e-14
               and abs(float(bec[0]) - math.sqrt(0.5)) <= 1e-14
               and max(abs(float(x) - 0.5) for x in bec[1:]) <= 1e-14
               and abs(msc - math.pi) <= 1e-12)
    check("S0.2 Jacobi recurrence self-test (Chebyshev a=b=-1/2: "
          "al=0, be=[sqrt(1/2),1/2,...], mass=pi)", cheb_ok,
          kill="PIPELINE")

    section("B0 -- heavy rungs (chains + CD kernel + T + bulk zone)")
    R = {}
    ok = True
    for kz in HEAVY:
        r = build_rung(kz)
        ok &= r is not None
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz)
            continue
        R[kz] = r
        r["bulk"] = bulk_mask(r)
        r["alias"] = port_aliases(r)
        print("    kz %-3d h %4d: pos %5d, neg %5d, bulk %5d "
              "(two-sided, A_h=%.0f), max T %.4f, delta_h %.4f"
              % (kz, r["h"], len(r["xs"]), len(r["ys"]),
                 int(r["bulk"].sum()), A_H, float(np.max(r["T"])),
                 2.0 * r["h"] / r["L"]))
    check("B0.1 all heavy chains complete", ok, kill="PIPELINE")
    if not ok:
        return finish({}, None)
    order = sorted(HEAVY, key=lambda kz: R[kz]["h"])

    # ---------------------------------------------------------- H1
    section("H1 -- BULK OSCILLATION of log w_h on I_h(x) "
            "(C = %.0f, %d samples)" % (C_OSC, N_OSC))
    ok_h1 = True
    h1 = {}
    for kz in order:
        r = R[kz]
        h = r["h"]
        yb = r["ys"][r["bulk"]]
        dx = C_OSC * (np.sqrt(1.0 - yb ** 2) / h + 1.0 / h ** 2)
        tt = np.linspace(-1.0, 1.0, N_OSC)
        pts = yb[:, None] + dx[:, None] * tt[None, :]
        pts = np.clip(pts, -1.0 + 1e-15, 1.0 - 1e-15)
        lw = np.log(np.maximum(w_ft(r, pts.ravel()), 1e-300))
        lw = lw.reshape(pts.shape)
        osc = lw.max(axis=1) - lw.min(axis=1)
        ok_h1 &= bool(np.all(np.isfinite(osc)))
        i = int(np.argmax(osc))
        h1[kz] = float(osc[i])
        print("    kz %-3d h %4d: max osc(log w_h) = %.4f at "
              "1-y = %.3e (a = %.1f); median %.4f"
              % (kz, h, h1[kz], 1.0 - yb[i],
                 2.0 * h * h * (1.0 - yb[i]), float(np.median(osc))))
    check("H1.0 all oscillations finite", ok_h1, kill="PIPELINE")
    sh1, dp1 = pair_stat([h1[kz] for kz in order])
    h1_ok = dp1 <= sh1
    h1_type = "SUPPORTED" if h1_ok else "FALSIFIED"
    print("    trend: shallow-pair median %.4f -> deep-pair median "
          "%.4f (%s)" % (sh1, dp1, "non-increasing" if h1_ok
                         else "GROWS"))
    check("H1.1 typed: %s (bulk log-density oscillation)" % h1_type,
          True)

    # ---------------------------------------------------------- H2
    section("H2 -- LOCAL DOUBLING mu^ft(I(y,2r))/mu^ft(I(y,r)) at "
            "r = rho_h(y)")
    gx, gw = np.polynomial.legendre.leggauss(N_GL)
    ok_h2 = True
    h2 = {}
    for kz in order:
        r = R[kz]
        h = r["h"]
        yb = r["ys"][r["bulk"]]
        rho = np.sqrt(1.0 - yb ** 2) / h + 1.0 / h ** 2
        ratios = np.empty(len(yb))
        inside = True
        for j, (y, rr_) in enumerate(zip(yb, rho)):
            masses = []
            for rad in (rr_, 2.0 * rr_):
                a, b = y - rad, y + rad
                inside &= (a > -1.0) and (b < 1.0)
                xq = 0.5 * (b - a) * gx + 0.5 * (a + b)
                masses.append(0.5 * (b - a)
                              * float(np.sum(gw * w_ft(r, xq))))
            ratios[j] = masses[1] / max(masses[0], 1e-300)
        ok_h2 &= inside and bool(np.all(np.isfinite(ratios)))
        i = int(np.argmax(ratios))
        h2[kz] = float(ratios[i])
        print("    kz %-3d h %4d: sup doubling = %.4f at 1-y = %.3e"
              " (a = %.1f); median %.4f"
              % (kz, h, h2[kz], 1.0 - yb[i],
                 2.0 * h * h * (1.0 - yb[i]),
                 float(np.median(ratios))))
    check("H2.0 doubling intervals inside the band, ratios finite",
          ok_h2, kill="PIPELINE")
    sh2, dp2 = pair_stat([h2[kz] for kz in order])
    h2_ok = dp2 <= H2_BAR * sh2
    h2_type = "SUPPORTED" if h2_ok else "FALSIFIED"
    print("    trend: shallow-pair median %.4f -> deep-pair median "
          "%.4f (bar %.1fx: %s)" % (sh2, dp2, H2_BAR,
                                    "bounded" if h2_ok else "GROWS"))
    check("H2.1 typed: %s (local doubling of mu_h^ft)" % h2_type,
          True)

    # ---------------------------------------------------------- H3
    section("H3 -- BULK MARGIN SEPARATION 1 - S R = 1 - T_m "
            "(bar: min >= %.2f on every rung)" % H3_BAR)
    h3 = {}
    h3_flip = False
    for kz in order:
        r = R[kz]
        h = r["h"]
        bulk = r["bulk"]
        yb, Tb = r["ys"][bulk], r["T"][bulk]
        wb = w_ft(r, yb)
        Mh = math.pi * np.sqrt(1.0 - yb ** 2) * wb / h
        S = Mh * r["Kdiag"][bulk]
        Rm = r["vs"][bulk] / np.maximum(Mh, 1e-300)
        marg = 1.0 - Tb
        i = int(np.argmin(marg))
        h3[kz] = float(marg[i])
        h3_flip |= h3[kz] < 0.0
        one_sided = float(np.min(
            1.0 - r["T"][(1.0 - r["ys"]) >= A_H / h ** 2]))
        print("    kz %-3d h %4d: min bulk margin %.4f at 1-y = "
              "%.3e (a = %.1f) | med S %.3f, med R %.3f | "
              "one-sided min %.4f"
              % (kz, h, h3[kz], 1.0 - yb[i],
                 2.0 * h * h * (1.0 - yb[i]), float(np.median(S)),
                 float(np.median(Rm)), one_sided))
    sh3, dp3 = pair_stat([h3[kz] for kz in order])
    h3_ok = all(v >= H3_BAR for v in h3.values()) and not h3_flip
    h3_type = "SUPPORTED" if h3_ok else "FALSIFIED"
    print("    trend: shallow-pair median %.4f -> deep-pair median "
          "%.4f%s" % (sh3, dp3,
                      "; SIGN FLIP" if h3_flip else ""))
    check("H3.1 typed: %s (bulk margin %s)"
          % (h3_type, "separated" if h3_ok else
             "NOT separated at A_h = %.0f" % A_H), True)

    # ---------------------------------------------------------- H4
    section("H4 -- PORT EDGE MODEL: w_h(x) ~ c_h (1-x)^alpha, Jost "
            "endpoint, near-edge point spectrum")
    ok_h4 = True
    for kz in order:
        r = R[kz]
        h = r["h"]
        lo = max(S_LO_FLOOR, A_H / h ** 2)
        thg, Wc = edge_cumulative(r, +1.0)
        fit = fit_powerlaw(thg, Wc, lo, S_HI)
        fin = (fit_powerlaw(thg, Wc, lo, S_MID)
               if lo < S_MID / 3.0 else None)
        fout = fit_powerlaw(thg, Wc, S_MID, S_HI)
        thgm, Wcm = edge_cumulative(r, -1.0)
        fitb = fit_powerlaw(thgm, Wcm, lo, S_HI)
        ok_h4 &= (fit is not None and fitb is not None
                  and -1.0 < fit["alpha"] < 2.0
                  and -1.0 < fitb["alpha"] < 2.0)
        if not ok_h4:
            break
        eigs = point_spectrum(r["A2"], r["B2"])
        above = sorted(e - 2.0 for e in eigs if e > 2.0)
        eps = above[0] if above else float("inf")
        r["fit"] = fit
        r["beta_fit"] = fitb
        r["eps_plus"] = eps
        r["jost"] = jost_endpoint(r["A2"], r["B2"])
        print("    kz %-3d h %4d: alpha %+.3f (c %.4f, fit resid "
              "%.2f; window s in [%.1e, %.0e])"
              % (kz, h, fit["alpha"], fit["c"], fit["resid"], lo,
                 S_HI))
        print("             sub-windows: inner %s / outer %s"
              " | beta(-1 end) %+.3f | J_h(1) %+.3f | nearest eig"
              " above +2: %s (h^2 eps/2 = %s)"
              % ("%+.3f" % fin["alpha"] if fin else "n/a",
                 "%+.3f" % fout["alpha"] if fout else "n/a",
                 fitb["alpha"], r["jost"],
                 "%.2e" % eps if above else "none",
                 "%.1f" % (h * h * eps / 2.0) if above else "-"))
    check("H4.0 edge fits finite, exponents in (-1, 2)", ok_h4,
          kill="PIPELINE")
    if not ok_h4:
        return finish({}, None)
    alphas = [R[kz]["fit"]["alpha"] for kz in order]
    alpha_star = float(np.median(alphas))
    for kz in order:
        f = R[kz]["fit"]
        R[kz]["c_star"] = c_at_alpha(f["s"], f["Ws"], alpha_star)
    cs = [R[kz]["c_star"] for kz in order]
    js = [abs(R[kz]["jost"]) for kz in order]
    shj, dpj = pair_stat(js)
    generic = (all(abs(a - 0.5) <= H4_ALPHA_TOL for a in alphas)
               and max(cs) <= H4_C_SPREAD * min(cs))
    near_edge = any(
        R[kz]["h"] ** 2 * R[kz]["eps_plus"] / 2.0 <= H4_NEAR_EDGE_A
        for kz in order)
    jost_decay = dpj <= H4_JOST_DECAY * shj
    if generic:
        h4_type = "BESSEL-GENERIC"
    elif alpha_star < 0.0 or near_edge or jost_decay:
        h4_type = "RESONANT-MODEL-NEEDED"
    else:
        h4_type = "FALSIFIED"
    print("    common alpha* = %+.3f (median); c_h at alpha*: %s "
          "(spread x%.1f)"
          % (alpha_star, " ".join("%.4f" % c for c in cs),
             max(cs) / min(cs)))
    print("    |J_h(1)| shallow-pair %.2f -> deep-pair %.2f | "
          "near-edge bound state (h^2 eps/2 <= %.0f): %s"
          % (shj, dpj, H4_NEAR_EDGE_A, "YES" if near_edge else "no"))
    check("H4.1 typed: %s (edge exponent %+.3f vs Bessel-generic "
          "+0.5)" % (h4_type, alpha_star), True)

    # ---------------------------------------------------------- H5
    section("H5 -- BESSEL MASS PROFILE at the port aliases m = 1..%d"
            % N_ALIAS)
    prof_a, prof_n = [], []
    for kz in order:
        r = R[kz]
        h = r["h"]
        ia = r["alias"]
        a_m = 2.0 * h * h * (1.0 - r["ys"][ia])
        nh = (h ** (2.0 * alpha_star + 2.0) * r["vs"][ia]
              / r["c_star"])
        prof_a.append(a_m)
        prof_n.append(nh)
        print("    kz %-3d h %4d: a_m    %s" % (kz, h, " ".join(
            "%8.2f" % v for v in a_m)))
        print("                 nuhat  %s" % " ".join(
            "%8.4f" % v for v in nh))
    da = np.abs(prof_a[-1] / np.maximum(prof_a[-2], 1e-300) - 1.0)
    dn = np.abs(prof_n[-1] / np.maximum(prof_n[-2], 1e-300) - 1.0)
    h5_ok = bool(np.max(da) <= H5_DRIFT and np.max(dn) <= H5_DRIFT)
    h5_type = "SUPPORTED" if h5_ok else "FALSIFIED"
    print("    last-third drift (kz %d -> kz %d): a_m max %.1f%%, "
          "nuhat max %.1f%% (bar %.0f%%)"
          % (order[-2], order[-1], 100 * float(np.max(da)),
             100 * float(np.max(dn)), 100 * H5_DRIFT))
    check("H5.1 typed: %s (Bessel-profile convergence along fixed "
          "aliases)" % h5_type, True)

    # ---------------------------------------------------------- H6
    section("H6 -- MASK CONSTANT: flat-mask Christoffel ratio vs "
            "pi^2/8 = %.4f, conditioned on delta_h" % PI2_8)
    h6 = {}
    ok_h6 = True
    for kz in order:
        r = R[kz]
        mask = (r["dec"] >= 3) & (r["dec"] <= 8)
        s_fl = flat_structure(r["xs"], r["h"], r["ys"], mask)
        ok_h6 &= s_fl is not None
        if s_fl is None:
            break
        h6[kz] = s_fl
        print("    kz %-3d h %4d: delta_h = %.4f  flat-mask ratio "
              "%.4f  residual vs pi^2/8: %+.4f"
              % (kz, r["h"], 2.0 * r["h"] / r["L"], s_fl,
                 s_fl - PI2_8))
    check("H6.0 flat-mask chains complete", ok_h6, kill="PIPELINE")
    res = [abs(h6[kz] - PI2_8) for kz in order]
    sh6, dp6 = pair_stat(res)
    h6_ok = (res[-1] <= H6_RESID) or (dp6 <= H6_DECAY * sh6)
    h6_type = "SUPPORTED" if h6_ok else "FALSIFIED"
    print("    |residual| shallow-pair %.4f -> deep-pair %.4f; "
          "deepest %.4f (bars: abs %.2f / decay x%.1f)"
          % (sh6, dp6, res[-1], H6_RESID, H6_DECAY))
    check("H6.1 typed: %s (scalar Fejer pi^2/8 mask model)"
          % h6_type, True)

    # ---------------------------------------------------------- H7
    section("H7 -- FIRST-CORRECTION SIGN vs the Jacobi(alpha, beta) "
            "reference at the port")
    ok_h7 = True
    gam_min = {}
    census_neg = {}
    for kz in order:
        r = R[kz]
        h = r["h"]
        a, b = r["fit"]["alpha"], r["beta_fit"]["alpha"]
        ok_h7 &= (a > -0.95) and (b > -0.95)
        if not ok_h7:
            break
        alJ, beJ, mass1 = jacobi_chain(a, b, h + 1)
        m0E = (r["fit"]["c"] * 2.0 ** (a + 1.0)
               * math.exp(math.lgamma(a + 1.0)
                          + math.lgamma(b + 1.0)
                          - math.lgamma(a + b + 2.0)))
        ia = r["alias"]
        PJ = eval_chain(alJ, beJ, m0E, r["ys"][ia], h)
        LamE = 1.0 / np.sum(PJ ** 2, axis=1)
        ok_h7 &= bool(np.all(LamE > 0.0))
        lam = 1.0 / r["Kdiag"][ia]
        SE = LamE / lam
        RE = r["vs"][ia] / LamE
        gam = (lam - r["vs"][ia]) / LamE
        gam_min[kz] = float(np.min(gam))
        census_neg[kz] = int(np.sum(gam <= 0.0))
        print("    kz %-3d h %4d (alpha %+.3f, beta %+.3f): "
              "gamma_m %s" % (kz, h, a, b,
                              " ".join("%+.2e" % g for g in gam)))
        print("             med S^E %.3f, med R^E %.3e, min gamma "
              "%+.3e, negatives %d/%d"
              % (float(np.median(SE)), float(np.median(RE)),
                 gam_min[kz], census_neg[kz], N_ALIAS))
    check("H7.0 Jacobi model admissible (alpha, beta > -0.95; "
          "Lambda > 0)", ok_h7, kill="PIPELINE")
    if not ok_h7:
        return finish({}, None)
    shg, dpg = pair_stat([gam_min[kz] for kz in order])
    conv_neg = any(census_neg[kz] > 0 for kz in order[-2:])
    all_pos = all(census_neg[kz] == 0 for kz in order)
    h7_type = ("SUPPORTED" if all_pos
               else ("FALSIFIED" if conv_neg else "SUPPORTED"))
    print("    sign census: negatives per rung %s | min-gamma "
          "trend: shallow-pair %+.3e -> deep-pair %+.3e"
          % (" ".join("%d:%d" % (kz, census_neg[kz])
                      for kz in order), shg, dpg))
    if not all_pos and not conv_neg:
        print("    (shallow-only negatives: reported, not a "
              "converged falsifier)")
    check("H7.1 typed: %s (gamma_m = (lambda_h - nu~)/Lambda^E > 0 "
          "at the port)" % h7_type, True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9, scramble seed 1): the signs the "
            "theorem lives on")
    rs = build_rung(9, scramble_seed=1)
    if rs is None:
        check("C0 scramble chain completes", False, kill="PIPELINE")
        return finish({}, None)
    bs = bulk_mask(rs)
    marg_s = float(np.min(1.0 - rs["T"][bs]))
    Ta_s = rs["T"][port_aliases(rs)]
    f1 = marg_s < 0.0
    f2 = bool(np.any(Ta_s >= 1.0))
    print("    scramble min bulk margin %.3e (real %.4f) -> %s"
          % (marg_s, h3[9], "FIRES (H3 sign flip)" if f1
             else "silent"))
    print("    scramble port-alias T: %s -> %s (gamma <= 0 <=> "
          "T >= 1; %d/%d aliases flipped)"
          % (" ".join("%.2e" % t for t in Ta_s),
             "FIRES (H7 sign flip)" if f2 else "silent",
             int(np.sum(Ta_s >= 1.0)), N_ALIAS))
    ctrl = ("H3+H7" if (f1 and f2)
            else ("H3" if f1 else ("H7" if f2 else None)))
    check("C1 CONTROLS FIRE on the H3/H7 signs", f1 or f2,
          kill="CONTROL")

    types = {"H1": h1_type, "H2": h2_type, "H3": h3_type,
             "H4": h4_type, "H5": h5_type, "H6": h6_type,
             "H7": h7_type}
    return finish(types, ctrl)


def finish(types, ctrl):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "HYPOTHESES-MEASURED"
    if types:
        print("\n  typed table:")
        labels = {"H1": "BULK OSCILLATION   ",
                  "H2": "LOCAL DOUBLING     ",
                  "H3": "BULK MARGIN SEP.   ",
                  "H4": "PORT EDGE MODEL    ",
                  "H5": "BESSEL MASS PROFILE",
                  "H6": "MASK CONSTANT      ",
                  "H7": "FIRST-CORR. SIGN   "}
        for k in ("H1", "H2", "H3", "H4", "H5", "H6", "H7"):
            print("    %s %s : %s" % (k, labels[k], types[k]))
    sub = ([("%s=%s" % (k, v)) for k, v in sorted(types.items())]
           if types else [])
    if ctrl:
        sub.append("CONTROL=%s" % ctrl)
    print("\n  VERDICT: %s (%s)" % (VERDICT, " + ".join(sub)))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
