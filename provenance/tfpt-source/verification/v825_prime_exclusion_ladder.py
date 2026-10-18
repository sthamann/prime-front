#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v825 -- PRIME.EXCLUSION.LADDER.01: the certified exclusion ladder of the GL1 prime-comb tower -- verified PSD rungs inverted into rigorous quadruple-exclusion regions -- extended to X = 24.81 with hardened floating-point certificates, and the saturation of the deployed rank-4 instrument typed, ONE module from two probes (26/26 + 21/21 checks; discovery probes exclusion_ladder_deep_probe.py LADDER-EXTENDED and exclusion_ladder_saturation_probe.py SATURATION-TYPED, 2026-08-06, re-run identically 2026-08-07).  THE INSTRUMENT (inherited from the detector-inversion chain, frozen): the verified PSD rungs T_X = toeplitz(c[:M]) of the GL1 tower (D = 1/64, X = M D; continuum lags v755 + atom tent reads in the deployed T115 convention of v563) are inverted into exclusion regions via the tent-read Guinand identity -- a quadruple hypothesis {1/2 +- delta +- i gamma} is EXCLUDED where the subspace lambda_min(T_X - Q) < -EXC_BUD on the frozen rank-4 battery (T - Q interpolation-zone criterion), and detector-native margin-break where lambda_min(T_X + Q) < -EXC_BUD, with the identity budget EXC_BUD = 1e-8 + 100 eps (||T|| + M max|q|).  THE CERTIFICATES (hardening, per rung): (i) a rigorous lambda_min > 0 lower bound via Cholesky PD verification with the Higham backward-error bound (Acc&Stab Thm 10.3: float Cholesky success on T - beta I => lambda_min(T) >= beta - gamma_{M+1} rowsum(|L||L|^T) - u max|diag|), (ii) a Rayleigh-residual enclosure of the bottom eigenvalue with rigorous dot-product inflations, (iii) every published boundary point re-proved by a rigorous witness-Rayleigh certificate (dense matvec, inflated bounds).  THE LADDER (deep rungs frozen reference, re-run 2026-08-07): X = 4 / 10 / 18.375 / 20.719 / 22.094 / 23.484 / 24.813 with certified lambda_min 5.29e-5 .. 1.078e-6 (certified lower bounds 4.76e-5 .. 9.70e-7) and the threshold census Xi_eff = X median delta_mb falling 0.639 -> 0.457 -> 0.274 -> 0.218 -> 0.219 -> 0.222 -> 0.212: the ladder converts computation depth into effective zero-free width at the calibrated rate X*(delta) ~= Xi_eff/delta.  THE SATURATION DECISION (frozen gates, recomputed here from the frozen series): gate S1 (slope of the last three rungs <= -0.3) does NOT fire (slope ~ -0.06); gate S2 (plateau |Xi/0.2187 - 1| <= 0.05 on >= 2 new rungs) FIRES => SATURATION-TYPED at Xi ~ 0.218 +- 3%, mechanism SUPPORT-ACTIVE-BUT-X-STALLED (the battery still converts u-support into width inside a rung -- support slope -0.68 on the 0.875 -> 1 leg -- but added depth stopped helping; the rank-12 detune enrichment gain GROWS with depth 19.3% -> 23.2% -> 25.0%, below the 30% battery-limited bar, typed).  MULTI-ZERO HARDENING: double injection breaks the margin on every boundary pair (no interference rescue) and the two-quadruple hypothesis is excluded (superadditive); battery-dependence typed (exclusion is battery-relative).  HONEST REACH (typed, unchanged): the gamma window is Nyquist-limited to pi/D = 201; every visible gamma lies INSIDE the [A1]-verified strip (Platt-Trudgian 3e12) -- the region is an independent TFPT-data-only re-derivation, NOT new territory, and the ladder is a depth-to-width bridge, not a record claim.  Controls fire (synthetic quadruple at 2 delta_mb breaks the full spectrum; no-false-exclusion confirmed by full eigensolves; the seed-7 scramble destroys the rung PSD at lambda_min ~ -5e4; the Epstein x^2+5y^2 swap destroys PSD at M = 640).  Feeds PRIME.DETECTOR.WINDOW.01 [O] and PRIME.FLOOR.RATIO.01 (the detector-inversion direction where floor bounds convert to zero-exclusion).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes exclusion_ladder_deep_probe.py (2026-08-06,
26/26 checks, ~51 s, LADDER-EXTENDED: new certified rungs X = 20.71875 /
22.09375, extended exclusion maps, Xi_eff 0.31 -> 0.218 on the extended
grid) and exclusion_ladder_saturation_probe.py (2026-08-06, 21/21
checks, ~13 min, SATURATION-TYPED: deciding rungs X = 23.484375 /
24.8125, Xi_eff plateau 0.218 +- 3%, mechanism support-active-but-
X-stalled); both re-run identically at promotion (2026-08-07, logs in
experiments/tfpt-discovery/*.log).  DOWNSCOPING (predeclared): the
suite module re-runs the COMPLETE instrument -- sieve, parity, anchors,
certificates, census maps, extended boundaries, witness certificates,
multi-zero hardening, all controls -- on the fast sub-ladder M = 256 /
640 / 1176 (X <= 18.375, sieve to 9.6e7, machinery verbatim); the deep
rungs X = 20.72 / 22.09 / 23.48 / 24.81 (sieve to 6e10, ~25 min at
promotion) enter as FROZEN REFERENCE constants from the probe runs,
with the continuation and saturation gates RECOMPUTED here from the
frozen series and the live sub-ladder tied to the frozen table by the
instrument-continuity ward (the shallow entries of the frozen Xi series
must reproduce live at rel 2e-2).  The deployed 1e8-table parity ward
is downscoped to the EXACT parity ward at M = 640 against the deployed
core.atom_lags_at path (atom count EXACT + max|dc| <= 5e-9) plus the
v780 lambda_min anchor 3.882e-6 at M = 1176 (rel 2e-2).  Original probe
docstrings and frozen protocols live in the two probe files verbatim.

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls in this
module (AST-checked); the cached RvM-checked ordinate list (v684
provenance, n = 2500) is read for the calibration wards only; RNG only
in the declared C2 scramble (seed 7).  NO RH claim -- the output is a
conditional exclusion-ladder statement with typed caveats
(single-quadruple dominance, float+certificate discipline, inside the
[A1] strip).
"""
import ast
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)

# shared zero-comb caches (repo tree; local fallback for mirror use)
_DISC = os.path.join(os.path.dirname(_here), "experiments",
                     "tfpt-discovery")
_REPO_CACHE = os.path.join(_DISC, "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(_here, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE
_REPO_EXT = os.path.join(_DISC, "c1_zero_ext_n2500.json")
_LOCAL_EXT = os.path.join(_here, "c1_zero_ext_n2500.json")
CACHE_EXT = _REPO_EXT if os.path.exists(_REPO_EXT) else _LOCAL_EXT

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = 1.0 / 64.0
SUB_RUNGS = ((256, 5.29e-5), (640, 1.18e-5), (1176, 3.9e-6))
V780_DEEP = 3.882e-6
ANCH_REL = 2.0e-2
SEG_ASC = 1 << 26
PARITY_C_ABS = 5.0e-9
FFT_WARD_BAR = 1.0e-9
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)       # frozen (parent)
DELTAS_GRID = np.linspace(1.0 / 60.0, 0.5, 30)   # frozen (parent)
EXT_DELTAS = np.geomspace(1.0 / 240.0, 0.5, 44)  # extended instrument
N_BISECT = 3
W0_BAR, WQ_BAR, W2_SLACK = 1.0e-12, 1.0e-8, 3.0
MONO_TOL = 0.02
IDENT_BUD = 1.0e-8
XI_4_CITED, XI_18_CITED = 0.67, 0.31   # detector-inversion frozen-grid
XI_CMP_REL = 0.15
XI_CONT_TOL = 1.05                     # continuation gate (deep probe S5)
GATE_SLOPE = -0.3                      # saturation gate S1 (frozen)
GATE_BAND = 0.05                       # saturation gate S2 (frozen)
ENRICH_BATT_BAR = 0.30                 # battery-limited bar (frozen)
A2A, A2B, A2C = 0.1038, 0.2573, 9.3675  # [A2] Hasanalizade-Shen-Wong
W2_PACKETS = (30.0, 50.0, 80.0)
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01
BATT_GIDX = (3, 10, 17, 24, 30, 35)
MZ_GIDX = (6, 14, 22, 30)
UNDER_SCAN_CAP = 6
SEED_SCRAMBLE = 7
R_CLASSICAL = 5.558691                 # Mossinghoff-Trudgian-Yang 2024
T_RH_CITED = 3.0e12                    # [A1] Platt-Trudgian 2021
EPSTEIN_CAP = 34000

# FROZEN DEEP REFERENCE (probe runs 2026-08-06/07; sieve to 6e10):
# X -> (lambda_min, certified lower bound, Xi_eff on the extended grid)
DEEP_REF = {
    20.71875: (2.4453e-6, 2.2005e-6, 0.2179),
    22.09375: (2.0092e-6, 1.8080e-6, 0.2187),
    23.484375: (1.5883e-6, 1.4292e-6, 0.2225),
    24.8125: (1.0779e-6, 9.6975e-7, 0.2121),
}
# the full frozen Xi_eff series (extended instrument, median over the
# 36-gamma grid); the first three entries MUST reproduce live below
XI_SERIES_REF = {4.0: 0.6388, 10.0: 0.4568, 18.375: 0.2736,
                 20.71875: 0.2179, 22.09375: 0.2187,
                 23.484375: 0.2225, 24.8125: 0.2121}
XI_LIVE_REL = 2.0e-2                   # instrument-continuity ward
CERT_LIVE = {256: 4.7605e-5, 640: 1.0638e-5, 1176: 3.4941e-6}
# saturation-probe mechanism constants (frozen; support slope on the
# 0.875 -> 1.0 leg at the deepest rung; rank-12 gains at X = 22.1 /
# 23.5 / 24.8) -- filled from the 2026-08-07 re-run log
SUPPORT_SLOPE_REF = -0.68
SUPPORT_SLOPE_BAR = -0.3
R12_GAINS_REF = (0.193, 0.232, 0.250)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in ("zetazero", "nzeros", "find_zeros"):
                return False
    return True


# ------------------------------------------- parent conventions (verbatim)
def quad_lags(M, gamma, delta):
    """Full off-line quadruple {1/2 +- delta +- i gamma}: tent reads
    of 4 cosh(delta u) cos(gamma u) (v765 RT3 kernel, AMP_Z = 2)."""
    z1, z2 = complex(delta, gamma), complex(-delta, gamma)
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = 2.0 * (np.exp(z1 * t) / z1 ** 2 + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def pair_lags(M, gamma):
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = -2.0 * np.cos(gamma * t) / gamma ** 2
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def a_weight(g):
    x = g * DGRID / 2.0
    return DGRID * (np.sin(x) / x) ** 2


def n_upper(t):
    return (t / (2.0 * math.pi) * math.log(t / (2.0 * math.pi * math.e))
            + A2A * math.log(t) + A2B * math.log(math.log(t)) + A2C)


def tail_budget(x, gamma_top, n_cached):
    jj = np.arange(len(x)) * DGRID
    band = np.linspace(0.0, 2.0 * math.pi / DGRID, 4096)
    Xb = np.abs(np.exp(1j * np.outer(band, jj)) @ x)
    x2max = float(np.max(Xb) ** 2)
    tt = np.geomspace(gamma_top, 1.0e9, 4000)
    integ = np.trapezoid(
        16.0 / (DGRID * tt ** 3)
        * np.array([n_upper(t) - n_cached for t in tt]), tt)
    return x2max * (integ + 16.0 / (DGRID * 1.0e9)
                    * n_upper(1.0e9) / 2.0)


# ------------------------------------------- segmented sieve + tent reads
def base_primes(n):
    sv = np.ones(n + 1, dtype=bool)
    sv[:2] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sv[i]:
            sv[i * i::i] = False
    return np.flatnonzero(sv)


def tent_accumulate(c, M, u, mu, chunk=4000000):
    """Deployed T115 tent convention (v563 atom_lags_at), vectorized:
    offsets -2..2 with idx < M plus the u < D reflection branch."""
    for s in range(0, u.size, chunk):
        uu, mm = u[s:s + chunk], mu[s:s + chunk]
        i0 = np.floor(uu / DGRID).astype(np.int64)
        for off in (-2, -1, 0, 1, 2):
            idx = i0 + off
            ok = (idx >= 0) & (idx < M)
            if not ok.any():
                continue
            v = 1.0 - np.abs(idx[ok] * DGRID - uu[ok]) / DGRID
            pos = v > 0.0
            if pos.any():
                c -= np.bincount(idx[ok][pos],
                                 weights=mm[ok][pos] * 0.5 * v[pos],
                                 minlength=M)
        refl = uu < DGRID
        if refl.any():
            v = 1.0 - uu[refl] / DGRID
            pos = v > 0.0
            if pos.any():
                c[0] -= float(np.sum(mm[refl][pos] * 0.5 * v[pos]))


def nmax_of_M(M):
    return int(math.floor(math.exp(M * DGRID + 1.0e-14)))


def seg_assemble(Ms, collect_mass_M=None, seg=SEG_ASC, reverse=False):
    """Segmented Eratosthenes over all prime powers <= e^{M D}; tent
    reads accumulated per rung (probe machinery verbatim)."""
    Ms = sorted(Ms)
    ncap = {M: nmax_of_M(M) for M in Ms}
    nmax = max(ncap.values())
    cs = {M: np.zeros(M) for M in Ms}
    cnt = {M: 0 for M in Ms}
    mass_cap = ncap[collect_mass_M] if collect_mass_M else None
    masses = [] if mass_cap else None
    bp = base_primes(int(math.isqrt(nmax)))
    los = list(range(0, nmax + 1, seg))
    if reverse:
        los = los[::-1]
    for lo in los:
        hi = min(lo + seg, nmax + 1)
        sv = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            sv[:2] = False
        for p in bp:
            p = int(p)
            st = max(p * p, ((lo + p - 1) // p) * p)
            if st < hi:
                sv[st - lo::p] = False
        nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
        if nn.size == 0:
            continue
        lg = np.log(nn)
        mu = 2.0 * lg / np.sqrt(nn)
        for M in Ms:
            if ncap[M] >= hi - 1:
                tent_accumulate(cs[M], M, lg, mu)
                cnt[M] += int(nn.size)
            else:
                sel = nn <= ncap[M]
                if sel.any():
                    tent_accumulate(cs[M], M, lg[sel], mu[sel])
                    cnt[M] += int(sel.sum())
        if masses is not None:
            masses.append(mu[nn <= mass_cap].copy())
    for p in bp:                       # prime powers p^k, k >= 2
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= nmax:
            u1 = np.array([math.log(q)])
            m1 = np.array([2.0 * lp / math.sqrt(q)])
            for M in Ms:
                if q <= ncap[M]:
                    tent_accumulate(cs[M], M, u1, m1)
                    cnt[M] += 1
            if masses is not None and q <= mass_cap:
                masses.append(m1.copy())
            q *= p
    return cs, cnt, (np.concatenate(masses) if masses is not None
                     else None), ncap


# ------------------------------------------- battery + subspace minimum
def battery_B(M, gamma, delta, support=1.0, detunes=(0.0,)):
    jj = np.arange(M) * DGRID
    msk = (jj <= support * M * DGRID).astype(float)
    cols = []
    for dg in detunes:
        g = gamma + dg
        for sgn in (delta, -delta):
            e = np.exp(sgn * jj) * msk
            cols.append(e * np.cos(g * jj))
            cols.append(e * np.sin(g * jj))
    return np.stack(cols, axis=1)


def sub_lam(cA, Qb):
    """lambda_min of sym-Toeplitz(cA) restricted to span(Qb) (>= full
    minimum: SAFE under-exclusion) + the witness vector."""
    Y = sla.matmul_toeplitz((cA, cA), Qb, check_finite=False)
    S = Qb.T @ Y
    S = 0.5 * (S + S.T)
    w, V = np.linalg.eigh(S)
    return float(w[0]), Qb @ V[:, 0]


def bud_of(M, nrmT, ql_max):
    return IDENT_BUD + 100.0 * np.finfo(float).eps * (nrmT + M * ql_max)


def boundary_scan(cT, M, nrmT, g, grid, sign, bisect=0,
                  support=1.0, detunes=(0.0,)):
    """First delta on the grid with subspace lambda_min < -bud for
    T + sign*Q; geometric bisection refinement (probe verbatim)."""
    prev = None
    for dl in grid:
        dl = float(dl)
        ql = quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(battery_B(M, g, dl, support, detunes))
        bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = sub_lam(cT + sign * ql, Qb)
        if lam < -bud:
            hit, w_hit, b_hit, lo = dl, wit, bud, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(battery_B(M, g, mid,
                                                support, detunes))
                bm = bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = sub_lam(cT + sign * qlm, Qbm)
                if lm < -bm:
                    hit, w_hit, b_hit = mid, wm, bm
                else:
                    lo = mid
            return hit, w_hit, b_hit
        prev = dl
    return float("nan"), None, float("nan")


def census_maps(cT, M, nrmT):
    exc = np.zeros((len(GAMMAS_GRID), len(DELTAS_GRID)), bool)
    mbk = np.zeros_like(exc)
    for ig, g in enumerate(GAMMAS_GRID):
        for idl, dl in enumerate(DELTAS_GRID):
            ql = quad_lags(M, float(g), float(dl))[:M]
            Qb, _ = np.linalg.qr(battery_B(M, float(g), float(dl)))
            bud = bud_of(M, nrmT, float(np.max(np.abs(ql))))
            lm, _ = sub_lam(cT - ql, Qb)
            lp, _ = sub_lam(cT + ql, Qb)
            exc[ig, idl] = lm < -bud
            mbk[ig, idl] = lp < -bud
    return exc, mbk


def full_min(cA, M):
    return float(sla.eigvalsh(sla.toeplitz(cA),
                              subset_by_index=[0, 0])[0])


# ----------------------------------------------------------- certificates
def gamma_fl(n):
    t = n * U_RND
    return t / (1.0 - t)


def chol_cert_lower(T, lam_hat):
    """Rigorous lower bound for lambda_min of the float matrix T:
    float Cholesky success on T - beta I => (Higham Thm 10.3)
    lambda_min(T) >= beta - gamma_{M+1} rowsum(|L||L|^T) - u diag."""
    M = T.shape[0]
    for frac in (0.9, 0.5, 0.25, 0.1):
        beta = frac * lam_hat
        A = T.copy()
        A[np.diag_indices(M)] -= beta
        try:
            L = np.linalg.cholesky(A)
        except np.linalg.LinAlgError:
            continue
        aL = np.abs(L)
        w = float(np.max(aL @ aL.sum(axis=0))) * CERT_INFL
        slack = gamma_fl(M + 1) * w
        e_diag = U_RND * float(np.max(np.abs(np.diag(A)))) \
            + U_RND * abs(beta)
        return beta - slack - e_diag, beta, slack + e_diag
    return None, None, None


def rayleigh_enclosure(T):
    """Rayleigh-residual localization of the bottom eigenpair with
    rigorous dot-product inflations: some eigenvalue in [lo, hi]."""
    M = T.shape[0]
    _w, v = sla.eigh(T, subset_by_index=[0, 0])
    v = v[:, 0] / np.linalg.norm(v[:, 0])
    y = T @ v
    aTv = np.abs(T) @ np.abs(v)
    rho = float(v @ y)
    e_rho = gamma_fl(M) * (float(np.abs(v) @ aTv)
                           + abs(rho)) * CERT_INFL
    r = float(np.linalg.norm(y - rho * v))
    e_y = gamma_fl(M) * float(np.linalg.norm(aTv)) * CERT_INFL \
        + e_rho
    return rho - e_rho - (r + e_y), rho + e_rho + (r + e_y)


def certified_break(cA, M, x, bud):
    """Rigorous Rayleigh UPPER bound on lambda_min of sym-Toeplitz(cA)
    from witness x: returns (certified lambda_min < -bud, value)."""
    A = sla.toeplitz(cA)
    y = A @ x
    q = float(x @ y)
    ax = np.abs(x)
    E = gamma_fl(M) * (float(ax @ (np.abs(A) @ ax))
                       + float(ax @ np.abs(y))) * CERT_INFL
    n2 = float(x @ x)
    num_up = q + E
    if num_up >= 0.0:
        return False, 0.0
    ray_up = num_up / (n2 * (1.0 + gamma_fl(M)))
    return ray_up < -bud, ray_up


# ------------------------------------- Epstein control comb (C3, frozen)
def lattice_r1(N):
    """r_{Q1}(n), Q1 = x^2 + 5y^2, exact count over Z^2 (verbatim from
    the epstein_firewall probe machinery)."""
    r = np.zeros(N + 1, dtype=np.int64)
    for x in range(0, int(math.isqrt(N)) + 1):
        x2 = x * x
        wx = 2 if x > 0 else 1
        ymax = int(math.isqrt((N - x2) // 5)) if x2 <= N else -1
        for y in range(0, ymax + 1):
            n = x2 + 5 * y * y
            if n == 0 or n > N:
                continue
            r[n] += wx * (2 if y > 0 else 1)
    return r


def dirichlet_vonmangoldt(a, N):
    """Coefficients Lambda_F(n) of -F'/F for F = sum a_n n^{-s}."""
    lam = np.zeros(N + 1)
    S = np.zeros(N + 1)
    logs = np.zeros(N + 1)
    logs[1:] = np.log(np.arange(1, N + 1, dtype=float))
    af = a.astype(float)
    for n in range(2, N + 1):
        lam[n] = af[n] * logs[n] - S[n]
        k = N // n
        if k >= 2:
            S[2 * n::n] += lam[n] * af[2:k + 1]
    return lam


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v825 -- PRIME.EXCLUSION.LADDER.01: the certified exclusion "
          "ladder + saturation")
    print("(two probes: LADDER-EXTENDED + SATURATION-TYPED; live "
          "sub-ladder X <= 18.375,")
    print(" deep rungs frozen reference -- downscoping predeclared in "
          "PROVENANCE; NO RH claim)")
    print("=" * 78)

    # ==================================================== P1: live wards
    print("\nP1 -- firewall + caches + instrument wards (live)")
    check("P1.AST no zeta-zero generator call in this module (cached "
          "RvM list read for wards only; RNG only in the declared C2 "
          "scramble)", ast_zero_firewall(__file__))
    d1 = json.load(open(CACHE))
    d2 = json.load(open(CACHE_EXT))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    check("P1.CACHE %d cached ordinates, gamma_1 = %.4f"
          % (len(gam_c), gam_c[0]),
          len(gam_c) == 2500 and abs(gam_c[0] - 14.134725) < 1e-5)
    Mw = 640
    cw = srp.continuum_lags(Mw)[:Mw]
    xw = np.cos(0.37 * np.arange(Mw)) / math.sqrt(Mw)
    y_f = sla.matmul_toeplitz((cw, cw), xw, check_finite=False)
    y_d = sla.toeplitz(cw) @ xw
    dev_f = float(np.max(np.abs(y_f - y_d))
                  / max(float(np.max(np.abs(y_d))), 1e-300))
    check("P1.FFT Toeplitz matvec (map scan path) == dense: rel dev "
          "%.2e <= %.0e" % (dev_f, FFT_WARD_BAR), dev_f <= FFT_WARD_BAR)

    # ============================================== P2: sub-ladder tower
    print("\nP2 -- the fast sub-ladder (sieve to e^18.375 = 9.6e7)")
    sub_ms = [M for M, _ in SUB_RUNGS]
    t0 = time.time()
    cs, cnt, masses_scr, ncap = seg_assemble(sub_ms,
                                             collect_mass_M=1176)
    print("    segmented sieve+reads: %d atoms to n = %d in %.1f s"
          % (cnt[1176], ncap[1176], time.time() - t0))
    # EXACT parity ward at M = 640 vs the deployed T115 path
    alpha6 = 0.5 * 640 * DGRID
    ka6 = core.atoms_in(alpha6)
    c_dep6, _ = core.atom_lags_at(alpha6, 640, core.U_ALL[:ka6],
                                  core.MU_ALL[:ka6])
    dev_c = float(np.max(np.abs(cs[640] - c_dep6)))
    check("P2.PARITY segmented assembly == deployed T115 path at "
          "M = 640: atom count %d == %d (EXACT), max |dc| = %.2e <= "
          "%.0e (deep 1e8-table ward downscoped, predeclared)"
          % (cnt[640], ka6, dev_c, PARITY_C_ABS),
          cnt[640] == ka6 and dev_c <= PARITY_C_ABS)

    towers, T_of, m_of, nrm_of = {}, {}, {}, {}
    for M, anch in SUB_RUNGS:
        towers[M] = srp.continuum_lags(M) + cs[M]
        T = sla.toeplitz(towers[M][:M])
        T_of[M], m_of[M] = T, float(
            sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm_of[M] = float(sla.norm(T, 2))
        rel = abs(m_of[M] - anch) / anch
        check("P2.%d rung M = %d (X = %.3f): lambda_min = %.4e vs "
              "anchor %.2e (rel dev %.3f <= %.2f)"
              % (M, M, M * DGRID, m_of[M], anch, rel, ANCH_REL),
              rel <= ANCH_REL)
    rel780 = abs(m_of[1176] - V780_DEEP) / V780_DEEP
    check("P2.DEEP v780 drainage anchor 3.882e-6 reproduced at M = "
          "1176 (rel dev %.4f <= %.2f)" % (rel780, ANCH_REL),
          rel780 <= ANCH_REL)

    # ============================================== P3: certificates
    print("\nP3 -- rigorous certificates (Cholesky/Higham + Rayleigh "
          "enclosure)")
    cert_ok = True
    for M in sub_ms:
        lb, beta, slack = chol_cert_lower(T_of[M], m_of[M])
        lo, hi = rayleigh_enclosure(T_of[M])
        ok_m = (lb is not None and lb > 0.0 and lo <= m_of[M] <= hi
                and abs(lb - CERT_LIVE[M]) / CERT_LIVE[M] <= ANCH_REL)
        cert_ok = cert_ok and ok_m
        print("      M = %4d: lambda_min >= %.4e CERTIFIED (frozen "
              "%.4e; slack %.1e); enclosure [%.4e, %.4e]"
              % (M, lb if lb is not None else float("nan"),
                 CERT_LIVE[M],
                 slack if slack is not None else float("nan"), lo, hi))
    check("P3.CERT every live rung carries a rigorous lambda_min > 0 "
          "certificate matching the frozen values (rel <= %.2f) and "
          "the enclosure brackets the float margin" % ANCH_REL,
          cert_ok)

    # ============================================== P4: calibration wards
    print("\nP4 -- calibration wards")
    gtest = 47.3
    lp = pair_lags(256, gtest)
    rank2 = 2.0 * a_weight(gtest) * np.cos(
        gtest * DGRID * np.arange(256))
    dev0 = float(np.max(np.abs(lp - rank2)))
    check("P4.W0 on-line pair layer == 2 a(g) cos(g k D) exactly: max "
          "dev %.2e <= %.0e" % (dev0, W0_BAR), dev0 <= W0_BAR)
    dev_q = 0.0
    for (gq, dq, kq) in ((31.7, 0.21, 40), (88.2, 0.44, 130),
                         (9.4, 0.08, 3)):
        ql = quad_lags(200, gq, dq)
        uu = np.linspace((kq - 1) * DGRID, (kq + 1) * DGRID, 20001)
        tent = (1.0 - np.abs(uu / DGRID - kq)) / DGRID
        integ = DGRID * float(np.trapezoid(
            tent * 4.0 * np.cosh(dq * uu) * np.cos(gq * uu), uu))
        dev_q = max(dev_q, abs(ql[kq] - integ) / abs(integ))
    check("P4.WQ quadruple lag reads == D x tent quadrature (max rel "
          "dev %.1e <= %.0e)" % (dev_q, WQ_BAR), dev_q <= WQ_BAR)
    aw = a_weight(gam_c)
    jj = np.arange(1176) * DGRID
    worst = 0.0
    for g0 in W2_PACKETS:
        x = np.exp(-0.5 * ((jj - jj[588]) / (1176 * DGRID / 8.0))
                   ** 2) * np.cos(g0 * jj)
        xTx = float(x @ (T_of[1176] @ x))
        Xg = np.abs(np.exp(1j * np.outer(gam_c, jj)) @ x) ** 2
        zside = float(np.sum(2.0 * aw * Xg))
        tb = tail_budget(x, gam_c[-1], len(gam_c))
        worst = max(worst, abs(xTx - zside) / max(tb, 1e-300))
    check("P4.W2 smooth-packet Guinand identity at M = 1176: |x^T T x "
          "- zero side| <= %.1f x tail budget (worst ratio %.3f)"
          % (W2_SLACK, worst), worst <= W2_SLACK)

    # ============================================== P5: exclusion maps
    print("\nP5 -- exclusion maps + extended boundaries (live "
          "sub-ladder)")
    maps, maps_mb = {}, {}
    for M in sub_ms:
        exc, mbk = census_maps(towers[M][:M], M, nrm_of[M])
        maps[M], maps_mb[M] = exc, mbk
        print("    M = %4d (X = %7.3f): T-Q exclusion %4d/%d | "
              "margin-break %4d/%d"
              % (M, M * DGRID, int(exc.sum()), exc.size,
                 int(mbk.sum()), mbk.size))
    check("P5.MAPS both regions NONEMPTY on every live rung",
          all(maps[M].sum() > 0 and maps_mb[M].sum() > 0
              for M in sub_ms))
    mono_ok = True
    for mp_, lab in ((maps, "T-Q"), (maps_mb, "margin-break")):
        for M1, M2 in zip(sub_ms[:-1], sub_ms[1:]):
            lost = int((mp_[M1] & ~mp_[M2]).sum())
            frac = lost / max(int(mp_[M1].sum()), 1)
            mono_ok = mono_ok and frac <= MONO_TOL
    check("P5.MONO deeper rungs keep shallower exclusions on BOTH "
          "boundaries (loss <= %.0f%%)" % (100 * MONO_TOL), mono_ok)

    bounds_mb = {M: np.full(len(GAMMAS_GRID), np.nan) for M in sub_ms}
    wits_mb = {M: [None] * len(GAMMAS_GRID) for M in sub_ms}
    for M in sub_ms:
        cT = towers[M][:M]
        for ig, g in enumerate(GAMMAS_GRID):
            d_mb, w_mb, _ = boundary_scan(cT, M, nrm_of[M], float(g),
                                          EXT_DELTAS, +1.0,
                                          bisect=N_BISECT)
            bounds_mb[M][ig] = d_mb
            wits_mb[M][ig] = w_mb
    xi_live = {}
    for M in sub_ms:
        X = M * DGRID
        fin = bounds_mb[M][np.isfinite(bounds_mb[M])]
        xi_live[X] = float(np.median(fin)) * X
        print("    X = %8.4f: median delta_mb = %.5f -> Xi_eff = "
              "%.4f (%d/36 reach)"
              % (X, float(np.median(fin)), xi_live[X], len(fin)))
    cont_ok = all(abs(xi_live[X] - XI_SERIES_REF[X]) / XI_SERIES_REF[X]
                  <= XI_LIVE_REL for X in xi_live)
    check("P5.XI instrument continuity: the live Xi_eff series (%s) "
          "reproduces the frozen shallow entries of the deep table "
          "(rel <= %.2f) -- the frozen reference and the live "
          "instrument are the same machine"
          % (", ".join("%.4f" % xi_live[X] for X in sorted(xi_live)),
             XI_LIVE_REL), cont_ok)
    # frozen-grid comparability (parent detector-inversion medians)
    xi_frozen = {}
    for M in (256, 1176):
        db = []
        for ig in range(len(GAMMAS_GRID)):
            idx = np.nonzero(maps_mb[M][ig])[0]
            if len(idx):
                db.append(DELTAS_GRID[idx[0]])
        xi_frozen[M] = float(np.median(db)) * M * DGRID
    c4 = abs(xi_frozen[256] - XI_4_CITED) / XI_4_CITED
    c18 = abs(xi_frozen[1176] - XI_18_CITED) / XI_18_CITED
    check("P5.CMP frozen-grid comparability: Xi(X=4) = %.3f vs parent "
          "0.67 (rel %.2f), Xi(X=18.375) = %.3f vs parent 0.31 (rel "
          "%.2f) <= %.2f"
          % (xi_frozen[256], c4, xi_frozen[1176], c18, XI_CMP_REL),
          c4 <= XI_CMP_REL and c18 <= XI_CMP_REL)

    # ==================================== P6: witness + multi-zero cert
    print("\nP6 -- hardening (witness certificates + multi-zero, "
          "live)")
    n_cert, n_cert_ok = 0, 0
    for M in sub_ms:
        cT = towers[M][:M]
        for ig in BATT_GIDX:
            g = float(GAMMAS_GRID[ig])
            b = bounds_mb[M][ig]
            if not np.isfinite(b) or wits_mb[M][ig] is None:
                continue
            ql = quad_lags(M, g, float(b))[:M]
            bud = bud_of(M, nrm_of[M], float(np.max(np.abs(ql))))
            ok1, _ = certified_break(cT + ql, M, wits_mb[M][ig], bud)
            n_cert += 1
            n_cert_ok += int(ok1)
    check("P6.WIT rigorous witness-Rayleigh certificates re-prove "
          "%d/%d sampled boundary points" % (n_cert_ok, n_cert),
          n_cert >= 10 and n_cert_ok == n_cert)
    deep_m = 1176
    cTd = towers[deep_m][:deep_m]
    pts = [(float(GAMMAS_GRID[ig]), float(bounds_mb[deep_m][ig]))
           for ig in MZ_GIDX if np.isfinite(bounds_mb[deep_m][ig])]
    n_pair, ok_break, ok_excl = 0, 0, 0
    for a_i in range(len(pts)):
        for b_i in range(a_i + 1, len(pts)):
            g1_, dl1 = pts[a_i]
            g2_, dl2 = pts[b_i]
            q1 = quad_lags(deep_m, g1_, dl1)[:deep_m]
            q2 = quad_lags(deep_m, g2_, dl2)[:deep_m]
            budp = IDENT_BUD + 100.0 * np.finfo(float).eps * (
                nrm_of[deep_m] + deep_m
                * (float(np.max(np.abs(q1)))
                   + float(np.max(np.abs(q2)))))
            B1 = battery_B(deep_m, g1_, dl1)
            B2 = battery_B(deep_m, g2_, dl2)
            Qb, _ = np.linalg.qr(np.concatenate([B1, B2], axis=1))
            lam_b, _ = sub_lam(cTd + q1 + q2, Qb)
            lam_e, _ = sub_lam(cTd - q1 - q2, Qb)
            n_pair += 1
            ok_break += int(lam_b < -budp)
            ok_excl += int(lam_e < -budp)
    check("P6.MZ multi-zero interference at M = 1176: double "
          "injection breaks the margin on %d/%d boundary pairs (no "
          "interference rescue) and the two-quadruple hypothesis is "
          "excluded on %d/%d" % (ok_break, n_pair, ok_excl, n_pair),
          n_pair >= 3 and ok_break == n_pair and ok_excl == n_pair)

    # ============================================== P7: controls (live)
    print("\nP7 -- controls (live sub-ladder)")
    inside_ok, n_in = True, 0
    for ig in MZ_GIDX:
        b = bounds_mb[deep_m][ig]
        if not np.isfinite(b) or 2.0 * b > 0.5:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, 2.0 * float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam = full_min(cTd + ql, deep_m)
        n_in += 1
        inside_ok = inside_ok and (lam < -bud)
    check("P7.C1a [must-fire] synthetic quadruple at 2 delta_mb "
          "inside the region breaks the verified margin (full "
          "eigensolve): %d/%d interior points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 3)
    valid_ok, n_val, under = True, 0, []
    for ig in BATT_GIDX:
        b = bounds_mb[deep_m][ig]
        if not np.isfinite(b):
            continue
        g = float(GAMMAS_GRID[ig])
        ql = quad_lags(deep_m, g, float(b))[:deep_m]
        bud = bud_of(deep_m, nrm_of[deep_m],
                     float(np.max(np.abs(ql))))
        lam = full_min(cTd + ql, deep_m)
        n_val += 1
        valid_ok = valid_ok and (lam < -bud)
        d_full, steps = float(b), 0
        for dl in DELTAS_GRID[DELTAS_GRID < b][::-1]:
            if steps >= UNDER_SCAN_CAP:
                break
            steps += 1
            ql2 = quad_lags(deep_m, g, float(dl))[:deep_m]
            bud2 = bud_of(deep_m, nrm_of[deep_m],
                          float(np.max(np.abs(ql2))))
            if full_min(cTd + ql2, deep_m) < -bud2:
                d_full = float(dl)
            else:
                break
        under.append(b / d_full)
    check("P7.C1b [no-false-exclusion] every claimed boundary point "
          "confirmed by the FULL eigensolve: %d/%d (under-detection "
          "median %.2f, descent capped at %d steps, lower bound "
          "typed)"
          % (n_val if valid_ok else -1, n_val,
             float(np.median(under)) if under else float("nan"),
             UNDER_SCAN_CAP), valid_ok and n_val >= 3)
    rng = np.random.default_rng(SEED_SCRAMBLE)
    alpha_t = 0.5 * 1176 * DGRID
    u_scr = rng.uniform(0.0, 2.0 * alpha_t, size=masses_scr.size)
    c_scr = np.zeros(1176)
    tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    lam_scr = full_min(srp.continuum_lags(1176) + c_scr, 1176)
    check("P7.C2 [must-fire] scramble at M = 1176 (positions uniform, "
          "SAME %d masses, seed %d): lambda_min = %.3e < 0 -- the "
          "rung PSD measures the true comb"
          % (masses_scr.size, SEED_SCRAMBLE, lam_scr), lam_scr < 0.0)
    r1 = lattice_r1(EPSTEIN_CAP)
    lamE = dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                 EPSTEIN_CAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    cE, _ = core.atom_lags_at(0.5 * 640 * DGRID, 640, posE, masE)
    lam_ep = full_min(srp.continuum_lags(640) + cE, 640)
    check("P7.C3 [must-fire] Epstein swap (Lambda_E of x^2 + 5 y^2, "
          "table reach %d => control at M = 640, typed): lambda_min "
          "= %.3e < 0" % (EPSTEIN_CAP, lam_ep), lam_ep < 0.0)

    # ================================ R: the frozen deep reference layer
    print("\nR -- THE DEEP LADDER (frozen reference, probe runs "
          "2026-08-06/07; gates recomputed)")
    print("  %10s %10s %12s %12s %8s" % ("X", "comb cap", "lam_min",
                                         "cert lower", "Xi_eff"))
    for X in sorted(XI_SERIES_REF):
        if X in DEEP_REF:
            lam, lb, xi = DEEP_REF[X]
            print("  %10.5f %10.2e %12.4e %12.4e %8.4f"
                  % (X, math.exp(X), lam, lb, xi))
        else:
            print("  %10.5f %10.2e %12s %12s %8.4f  (live above)"
                  % (X, math.exp(X), "--", "--", XI_SERIES_REF[X]))
    check("R1.CERT the frozen deep certificates are strictly ordered "
          "and positive: cert lower < lambda_min, both decreasing in "
          "X, all > 0",
          all(0.0 < lb < lam for lam, lb, _ in DEEP_REF.values())
          and all(DEEP_REF[x1][0] > DEEP_REF[x2][0]
                  for x1, x2 in zip(sorted(DEEP_REF)[:-1],
                                    sorted(DEEP_REF)[1:])))
    xi18 = XI_SERIES_REF[18.375]
    cont = all(DEEP_REF[X][2] <= XI_CONT_TOL * xi18
               for X in (20.71875, 22.09375))
    check("R2.CONT the continuation gate (deep probe S5.2, "
          "recomputed): Xi_eff(20.72) = %.4f, Xi_eff(22.09) = %.4f "
          "<= %.2f x Xi_eff(18.375) = %.4f -- LADDER-EXTENDED"
          % (DEEP_REF[20.71875][2], DEEP_REF[22.09375][2],
             XI_CONT_TOL, XI_CONT_TOL * xi18), cont)
    last3 = sorted(DEEP_REF)[-3:]
    lx = np.log(last3)
    ly = np.log([DEEP_REF[X][2] for X in last3])
    slope3 = float(np.polyfit(lx, ly, 1)[0])
    gate_s1 = slope3 <= GATE_SLOPE
    band_devs = [abs(DEEP_REF[X][2] / XI_SERIES_REF[22.09375] - 1.0)
                 for X in (23.484375, 24.8125)]
    gate_s2 = all(d <= GATE_BAND for d in band_devs)
    check("R3.SAT the saturation gates (saturation probe S3, "
          "recomputed from the frozen series): gate S1 slope(last 3) "
          "= %+.3f > %.2f (no continued sharpening), gate S2 plateau "
          "|Xi/0.2187 - 1| = %.3f / %.3f <= %.2f on both deciding "
          "rungs => SATURATION-TYPED at Xi ~ 0.218 +- 3%%"
          % (slope3, GATE_SLOPE, band_devs[0], band_devs[1],
             GATE_BAND), (not gate_s1) and gate_s2)
    check("R4.MECH the mechanism constants (frozen): support slope "
          "%.2f <= %.2f (SUPPORT-ACTIVE) while the rank-12 enrichment "
          "gain grows %.1f%% -> %.1f%% -> %.1f%% with depth yet stays "
          "below the %.0f%% battery-limited bar -- typed "
          "SUPPORT-ACTIVE-BUT-X-STALLED (mixed/unresolved)"
          % (SUPPORT_SLOPE_REF, SUPPORT_SLOPE_BAR,
             *(100 * g for g in R12_GAINS_REF),
             100 * ENRICH_BATT_BAR),
          SUPPORT_SLOPE_REF <= SUPPORT_SLOPE_BAR
          and all(g1 < g2 for g1, g2 in zip(R12_GAINS_REF[:-1],
                                            R12_GAINS_REF[1:]))
          and max(R12_GAINS_REF) < ENRICH_BATT_BAR)
    xi_deep = DEEP_REF[24.8125][2]
    print("    depth-to-width benchmark (deepest frozen calibration, "
          "Xi_eff = %.4f):" % xi_deep)
    for dl in (0.5, 0.25, 0.1, 0.05, 0.01):
        xs_ = xi_deep / dl
        print("      delta >= %5.2f excluded at depth X* = %7.1f "
              "(comb cap e^{X*} = %.2e)" % (dl, xs_, math.exp(xs_)))
    for gb in (50.0, 100.0, 180.0):
        dcl = 0.5 - 1.0 / (R_CLASSICAL * math.log(gb))
        print("    gamma = %5.1f: classical (MTY 2024) delta > %.3f "
              "-- the comb region is WIDER in-band but lies INSIDE "
              "the [A1] strip (|gamma| <= %.0e verified on-line): "
              "consistency re-derivation, NOT new territory"
              % (gb, dcl, T_RH_CITED))
    print("    REACH (honest, unchanged): gamma-window Nyquist-"
          "limited to pi/D = %.1f; new territory needs gamma > 3e12 "
          "=> M > 1e12 lags -- out of reach by ~10 orders; the "
          "ladder is a DEPTH-to-WIDTH bridge, not a record claim."
          % (math.pi / DGRID))

    # ============================================================== V
    print("\n" + "=" * 78)
    verdicts_ok = cont and (not gate_s1) and gate_s2
    print("V -- verdict pair (recomputed): %s + %s"
          % ("LADDER-EXTENDED" if cont else "?!",
             "SATURATION-TYPED" if ((not gate_s1) and gate_s2)
             else "?!"))
    print("=" * 78)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = not FAILS and verdicts_ok
    print("[%s] PATTERN GATE: expected all checks green with the "
          "verdict pair LADDER-EXTENDED + SATURATION-TYPED"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
