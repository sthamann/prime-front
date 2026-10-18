#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""certified_ladder_probe -- PRIME.PORT.CERTIFIED.LADDER.01
(EXPLORATION ONLY, experiments/; round 40, work package (a) of the
closing-cylinder plan: roll the head certificate out to EVERY
reachable ladder rung, 2026-08-09).

EXTENDS PRIME.PORT.CERTIFIED.HEAD.01 (certified_head_probe.py; head
rungs kz 9/12/13 PROVEN by exact integer Bareiss LDL).  Same
simplification (promoted, v866/v876): ||C_h|| <= 1  <=>  K >= 0
where K = odd_toeplitz(c, M) is DIRECTLY the h x h odd-Toeplitz
matrix of the window lags c = c_arch + c_atoms; a certified PSD
proof of K is a certified wall proof.  Same error model: eps_c =
SAFETY x the dps-60-vs-high-dps lag disagreement (SAFETY = 10,
floored at 1e-55), entrywise |K_hi - K_true| <= 2 eps_c, spectral
||.||_2 <= 2 h eps_c -- stated and conservative, NOT interval
arithmetic.

THE LADDER: core.frame_a_zones() restricted to h <= 900 -- the 42
reachable rungs (h from 142 to 878).  TWO CERTIFICATE TIERS, typed
separately and honestly:

 TIER 1 (h <= 300), "exact-rational (integer Bareiss LDL)": the
     head machinery verbatim.  Lags at dps 60/100, grid
     N = floor(K Q) with Q = 10^20, shift s = 2 h eps_c + h/Q,
     EXACT integer fraction-free Bareiss LDL of N - ceil(s Q) I
     (every division remainder-checked; pivot k = the (k+1)-st
     leading principal minor; all pivots > 0 ==> PD, Sylvester).
     A certified floor is attempted IN the same run by shifting an
     extra m = 0.5 x lambda_min(f64); a refusal at m > 0 retries
     m = 0; a refusal at m = 0 is a genuine refusal (K1).
 TIER 2 (h > 300), "validated-precision (mpmath Cholesky dps
     120/200)" -- NOT exact-rational, and never labelled as such:
     lags at dps 60/120, K assembled at dps 130 (entries then
     exact binary rationals), shifted by delta + m with
     delta = 2 h eps_c + h * 10^-118 * max|c|   (the spectral
     error bound PLUS a rigorous rounding allowance for the
     single-subtraction K assembly at dps 130), m as in tier 1.
     Cholesky runs at working dps 120; on success it is RE-RUN at
     dps 200 (precision doubling) and every pivot d_j must exceed
     10^6 x the accumulated per-pivot rounding-bound estimate
     b_j = 8 (j+2) u (|K_jj - shift| + sum_k L_jk^2), u = 2^(2-prec),
     at BOTH precisions.  Certified only if both passes are
     positive-definite AND both ratio bars hold; a nonpositive
     pivot at dps 200 is a genuine refusal (K1); positive pivots
     that miss the ratio bar are typed CERT-OUT-OF-REACH
     (precision), never certified and never a kill.

SCALING CAUTION (frozen into the protocol): tau_h shrinks like
e^{-2.4 alpha} down the ladder, but the certified floor is
lambda_min(K) itself, NOT tau -- so MEASURE FIRST:

 T0  FLOAT SURVEY: float64 lambda_min(K) for ALL 42 rungs is
     computed and PRINTED up front (fast), before any certificate.
 REACH GATE (frozen): a certificate is attempted only where the
     float lambda_min >= 100 x that rung's conservative shift
     bound (tier 1: s = 2 h eps_c + h/Q; tier 2: delta).  Rungs
     below the gate are typed CERT-OUT-OF-REACH with the gap
     printed -- these need higher-precision lag evaluation, which
     is the named follow-up work package.

FROZEN PROTOCOL (2026-08-09; the 42 rungs; control kz 9):

 T0  FLOAT SURVEY as above; expected 42 rungs (frozen count).
 T1  CROSS-IMPLEMENTATION WARD: on every ATTEMPTED rung (and the
     control) the high-dps mpmath lag vector must agree with the
     deployed float64 core lags at relative sup distance <= 1e-9.
     A miss means the reimplementation is buggy -- fix, never
     proceed.
 T2  TIER-1 CERTIFICATES: every attempted tier-1 rung must be
     certified (all pivots > 0)  ==>  sigma_h > 0 PROVEN modulo
     the stated error model.  Report per rung: h, eps_c, shift,
     mode, certified floor, runtime.
 T3  TIER-2 CERTIFICATES: every attempted tier-2 rung must pass
     BOTH Cholesky precisions AND the 10^6 pivot-vs-bound bar;
     typed "validated-precision", never "exact-rational".
 C   CONTROL (must fire): the Epstein x^2+5y^2 comb at kz 9,
     through the IDENTICAL tier-1 lag assembly and certificate,
     must hit a nonpositive pivot -- the machinery must REFUSE
     the wall for the wrong comb.  The control runs IMMEDIATELY
     after the survey so that budget exhaustion can never
     silently drop it.

RUNTIME BUDGET (frozen): 2700 s total, hard deadline 2640 s.
Order: survey -> control -> tier-1 ascending h -> tier-2 ascending
h.  Tier-1 gets a 1200 s slice with a measured-cost predictor
(seed: 54 s at h = 184, exponent 4.8, updated from each measured
rung); a tier-1 rung predicted past the slice is NOT silently
skipped -- it falls back to tier 2 and is typed
"validated-precision (budget fallback from tier-1)".  When the
global deadline is predicted or reached, the remaining rungs are
typed SKIPPED-BUDGET and PRINTED -- partial coverage is an honest
result.  Elapsed time is tracked and printed per rung.

KILLS: K1 the ward fails on an attempted rung, or an attempted
prime rung is genuinely refused (tier 1: nonpositive exact pivot
at m = 0; tier 2: nonpositive pivot at dps 200 at m = 0) ->
CERT-BROKEN; K2 the control is certified (does not fire) ->
CONTROL-DEAD.

VERDICT (frozen enum): CERTIFIED-LADDER (all 42 rungs certified)
/ CERTIFIED-LADDER-PARTIAL (>= 1 rung certified, none broken;
the rest typed CERT-OUT-OF-REACH or SKIPPED-BUDGET) /
CERT-BROKEN / CONTROL-DEAD.

MECHANICAL CACHES (performance only, no protocol content): the
Gauss-Legendre nodes per dps, the atom position/mass PREFIX per
dps (the rung atom lists are prefixes of the one deployed v563
table), and the trial-division smallest-prime-factor memo.

SPEC AMENDMENTS (fail-first history preserved, house precedent):
  v1 (frozen 2026-08-09, pre-run): everything above, with the
     reach gate applied to EVERY certificate call.  First run: the
     survey passed (42/42 rungs, all float floors positive, the
     smallest 1.03e-5 at kz 43 -- every rung >= 1e12 x its grid
     shift scale, nothing out of reach), but the CONTROL was typed
     OUT-OF-REACH instead of REFUSED: the Epstein comb has float
     lambda_min = -10, so the v1 reach gate blocked the Bareiss
     run that the control exists to refuse.  C1 FAILED -- an
     ordering bug in the gate, not a certificate failure.
  v2 (this file): the reach gate applies to PRIME rungs only; the
     control always runs its certificate (the head probe's
     unconditional behaviour, restored).  Purely mechanical; no
     bar, error model or arithmetic changed.

NO RH claim: these are finite-h positivity certificates for the
reachable rungs of the deployed v563 window ladder; the tail
(h -> infinity) is untouched and stays with the registered port
contracts.

FIREWALL: no zeros, no prime oracles (AST scan for zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime);
the atom tables come from the deployed v563 window, READ-ONLY;
the only factorisation used is trial-division smallest-prime-
factor recovery on the v563 atom list (needed for exact masses
log p in mpmath).  Deterministic, no RNG.  Stdout only -- writes
nothing.  No marker moves.

Sources (read-only): certified_head_probe (round 40 WP2, the
machinery being rolled out); v563_paper2_readouts (window/lag
assembly); v866/v876 (wall <=> odd-Toeplitz PSD, promoted);
port_scalar_schur_probe (Epstein control recursion, round 39).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/certified_ladder_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_LADDER_MAX = 900             # reachable-rung cap (the 42 rungs)
N_RUNGS_EXP = 42               # frozen expected rung count
TIER1_H_MAX = 300              # tier boundary (exact vs validated)
DPS_LO = 60                    # low lag precision (error model)
DPS_T1 = 100                   # tier-1 high lag precision (as head)
DPS_T2 = 120                   # tier-2 lag/Cholesky precision
DPS_T2V = 200                  # tier-2 verification precision
SAFETY = 10                    # error-model safety factor on eps_c
EPS_FLOOR = "1e-55"            # eps_c floor (dps-60 round-off scale)
Q_POW = 20                     # grid denominator Q = 10^Q_POW (head v2)
WARD_REL = 1.0e-9              # T1 bar (expected ~1e-12)
GL_N = 48                      # the deployed panel order (v563)
REACH_FACTOR = 100.0           # float lam_min >= this x shift bound
PIVOT_FACTOR = 1.0e6           # tier-2 pivot > this x rounding bound
FLOOR_FRAC = 0.5               # certified-floor attempt m = this x lam_f
ROUND_ALLOW = "1e-118"         # tier-2 K-assembly rounding allowance/h
BUDGET_S = 2700.0              # total budget (45 min)
DEADLINE_S = 2640.0            # hard deadline (leave room to report)
T1_SLICE_S = 1200.0            # tier-1 phase slice of the budget
T1_EXP = 4.8                   # Bareiss cost exponent (calibrated)
C1_SEED = 54.0 / 184.0 ** T1_EXP   # measured: 54 s at h = 184
C2_SEED = 2.5e-7               # tier-2 s per h^3 (both passes, seeded)
CL_SEED = 6.0e-3               # lag-assembly s per lag (seeded)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def elapsed():
    return time.time() - T0


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


# ------------------------------------------------ mpmath lag assembly
_GL_CACHE = {}
_ATOM_CACHE = {}
_SPF_CACHE = {}


def gl_nodes(n):
    """Gauss-Legendre nodes/weights by Newton on P_n at current dps
    (cached per dps)."""
    key = (n, mp.dps)
    if key in _GL_CACHE:
        return _GL_CACHE[key]
    xs, ws = [], []
    tol = mp.mpf(10) ** (-(mp.dps - 6))
    for i in range(n):
        x = mp.cos(mp.pi * (i + mp.mpf(3) / 4) / (n + mp.mpf(1) / 2))
        dp = mp.mpf(1)
        for _ in range(80):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < tol:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    _GL_CACHE[key] = (xs, ws)
    return xs, ws


def arch_A_far_mp(s, D, glx, glw):
    """v563 _arch_A_far, verbatim in mpmath (s >= D)."""
    out = mp.mpf(0)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        acc = mp.mpf(0)
        for x, wt in zip(glx, glw):
            w = mid + half * x
            acc += wt * ((1 - abs(s - w) / D) * mp.exp(-w / 2)
                         / (-mp.expm1(-2 * w)))
        out -= half * acc
    return out


def arch_A_near_mp(s, D, glx, glw):
    """v563 _arch_A_near, verbatim in mpmath (0 <= s < D)."""
    s = abs(s)
    tri_s = max(mp.mpf(0), 1 - s / D)
    W = s + D
    pts = sorted({mp.mpf(0), s, D - s, W})
    pts = [p for p in pts if 0 <= p <= W]
    tot = mp.mpf(0)
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        for x, wt in zip(glx, glw):
            w = mid + half * x
            S = (max(mp.mpf(0), 1 - abs(s - w) / D)
                 + max(mp.mpf(0), 1 - (s + w) / D)) / 2
            tot += half * wt * ((tri_s * mp.exp(-2 * w)
                                 - S * mp.exp(-w / 2))
                                / (-mp.expm1(-2 * w)))
    return (-(mp.euler + mp.log(mp.pi)) * tri_s + 2 * tot
            - tri_s * mp.log(-mp.expm1(-2 * W)))


def atom_lags_mp(alpha, M, uu, mm):
    """v563 atom_lags_at (T115 tent assembly), verbatim in mpmath."""
    D = 2 * alpha / M
    c = [mp.mpf(0)] * M
    for u_j, mu_j in zip(uu, mm):
        i0 = int(mp.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(i * D - u_j) / D
            if v > 0:
                c[i] -= mu_j * v / 2
        if u_j < D:
            for i in range(0, min(M, int(mp.floor((D - u_j) / D)) + 2)):
                v = 1 - (i * D + u_j) / D
                if v > 0:
                    c[i] -= mu_j * v / 2
    return c, D


def spf(n):
    """Smallest prime factor by trial division (n is a prime power
    from the READ-ONLY v563 atom list, so spf(n) = its base p);
    memoised."""
    if n in _SPF_CACHE:
        return _SPF_CACHE[n]
    d = 2
    while d * d <= n:
        if n % d == 0:
            _SPF_CACHE[n] = d
            return d
        d += 1
    _SPF_CACHE[n] = n
    return n


def atom_arrays(dps, ka):
    """The first ka atom positions log n and masses 2 log p / sqrt(n)
    in mpmath at the given dps.  The rung atom lists are PREFIXES of
    the one deployed v563 table, so the cache extends lazily."""
    ent = _ATOM_CACHE.setdefault(dps, {"uu": [], "mm": []})
    uu, mm = ent["uu"], ent["mm"]
    if len(uu) < ka:
        with mp.workdps(dps):
            for idx in range(len(uu), ka):
                n = int(core._NN[idx])
                p = spf(n)
                uu.append(mp.log(n))
                mm.append(2 * mp.log(p) / mp.sqrt(n))
    return uu[:ka], mm[:ka]


def lambda_eps_mp(N):
    """The Epstein x^2+5y^2 von-Mangoldt recursion (round-39 control),
    run in mpmath at the current dps."""
    r = [0] * (N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1
    a = [mp.mpf(t) / 2 for t in r]
    lam = [mp.mpf(0)] * (N + 1)
    for n in range(2, N + 1):
        acc = a[n] * mp.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def lags_mp(spec, dps):
    """The full lag vector c = c_arch + c_atoms of one rung, in
    mpmath at the given dps.  spec: kind, M, n_zone, ka (prime) or
    the (READ-ONLY float-selected) support nn (epstein)."""
    with mp.workdps(dps):
        glx, glw = gl_nodes(GL_N)
        alpha = mp.log(spec["n_zone"])
        M = spec["M"]
        if spec["kind"] == "prime":
            uu, mm = atom_arrays(dps, spec["ka"])
        else:
            lamE = lambda_eps_mp(spec["N_E"])
            uu = [mp.log(n) for n in spec["nn"]]
            mm = [2 * lamE[n] / mp.sqrt(n) for n in spec["nn"]]
        c_at, D = atom_lags_mp(alpha, M, uu, mm)
        c = []
        for i in range(M):
            s = i * D
            if s >= D:
                c.append(arch_A_far_mp(s, D, glx, glw) + c_at[i])
            else:
                c.append(arch_A_near_mp(s, D, glx, glw) + c_at[i])
        return c


# ------------------------------------------------ tier-1 certificate
def bareiss_pd(A):
    """Exact integer fraction-free LDL (Bareiss).  Pivot k equals the
    (k+1)-st leading principal minor; all pivots > 0 <=> PD
    (Sylvester).  Every exact division is remainder-checked.
    Returns (certified, pivots_done, first_bad_pivot)."""
    n = len(A)
    A = [row[:] for row in A]
    prev = 1
    for k in range(n):
        piv = A[k][k]
        if piv <= 0:
            return False, k, piv
        for i in range(k + 1, n):
            Ai, Ak, aik = A[i], A[k], A[i][k]
            for j in range(i, n):
                q, r = divmod(piv * Ai[j] - aik * Ak[j], prev)
                if r:
                    raise ArithmeticError("Bareiss divisibility broken")
                Ai[j] = q
        for i in range(k + 1, n):
            Ai = A[i]
            for j in range(k + 1, i):
                Ai[j] = A[j][i]
        prev = piv
    return True, n, None


def grid_matrix(c_hi, M, Q, dps):
    """K = odd_toeplitz(c, M) on the integer grid N = floor(K Q)."""
    h = M // 2
    with mp.workdps(dps + 10):
        Qm = mp.mpf(Q)
        N = [[0] * h for _ in range(h)]
        for i in range(h):
            for j in range(i, h):
                kij = c_hi[abs(i - j)] - c_hi[(M - 1) - i - j]
                N[i][j] = N[j][i] = int(mp.floor(kij * Qm))
    return N


def ward_eps(spec, c_f, dps_hi):
    """Lags at dps 60 and dps_hi, the conservative eps_c and the T1
    cross-implementation ward vs the deployed float64 lags."""
    t0 = time.time()
    c_lo = lags_mp(spec, DPS_LO)
    c_hi = lags_mp(spec, dps_hi)
    t_lag = time.time() - t0
    with mp.workdps(dps_hi + 10):
        eps_c = max(SAFETY * max(abs(a - b) for a, b in zip(c_lo, c_hi)),
                    mp.mpf(EPS_FLOOR))
        ward = (max(abs(a - mp.mpf(b)) for a, b in zip(c_hi, c_f))
                / max(abs(mp.mpf(b)) for b in c_f))
    return c_hi, eps_c, float(ward), t_lag


def certify_tier1(spec, c_f, lam_f):
    """One tier-1 rung: dps-60/100 lags, ward, conservative shift,
    reach gate, exact integer Bareiss with the in-run floor attempt
    m = FLOOR_FRAC x lam_f (retry m = 0 on refusal)."""
    M, h = spec["M"], spec["M"] // 2
    Q = 10 ** Q_POW
    c_hi, eps_c, ward, t_lag = ward_eps(spec, c_f, DPS_T1)
    with mp.workdps(DPS_T1 + 10):
        shift_int = h + int(mp.ceil(2 * h * eps_c * Q))
        s_total = float(mp.mpf(shift_int) / Q)
    out = dict(h=h, mode="exact-rational (integer Bareiss LDL)",
               eps_c=eps_c, ward=ward, shift=s_total, lam_f=lam_f,
               t_lag=t_lag, t_cert=0.0, floor=None, npiv=0, bad=None)
    # SPEC v2: the reach gate applies to prime rungs only; the
    # control always runs its certificate.
    if spec["kind"] == "prime" and lam_f < REACH_FACTOR * s_total:
        out["status"] = "out-of-reach"
        return out
    N = grid_matrix(c_hi, M, Q, DPS_T1)
    t0 = time.time()
    m_int = int(FLOOR_FRAC * max(lam_f, 0.0) * Q)
    ok, npiv, bad = bareiss_pd(
        [[N[i][j] - (shift_int + m_int if i == j else 0)
          for j in range(h)] for i in range(h)])
    if ok:
        out.update(status="certified", floor=m_int / Q, npiv=npiv)
    elif m_int > 0:
        ok0, npiv0, bad0 = bareiss_pd(
            [[N[i][j] - (shift_int if i == j else 0)
              for j in range(h)] for i in range(h)])
        if ok0:
            out.update(status="certified", floor=0.0, npiv=npiv0)
        else:
            out.update(status="refused", npiv=npiv0, bad=bad0)
    else:
        out.update(status="refused", npiv=npiv, bad=bad)
    out["t_cert"] = time.time() - t0
    return out


# ------------------------------------------------ tier-2 certificate
def build_K_rows(c_hi, M):
    """Lower-triangular K = odd_toeplitz(c, M) as exact mpf entries,
    assembled at dps DPS_T2 + 10 (one subtraction per entry; the
    rounding is covered by the ROUND_ALLOW term of delta)."""
    h = M // 2
    with mp.workdps(DPS_T2 + 10):
        return [[c_hi[abs(i - j)] - c_hi[(M - 1) - i - j]
                 for j in range(i + 1)] for i in range(h)]


def chol_pass(Krows, shift, dps):
    """One Cholesky pass at working dps with the per-pivot rounding
    bound b_j = 8 (j+2) u (|K_jj - shift| + sum L_jk^2); returns
    (pd_ok, min pivot/bound ratio, pivots_done, first_bad_pivot)."""
    h = len(Krows)
    with mp.workdps(dps):
        u = mp.mpf(2) ** (2 - mp.prec)
        sh = mp.mpf(shift)
        Ld, Lo = [], []
        min_ratio = mp.inf
        fdot = mp.fdot
        for i in range(h):
            Ki = Krows[i]
            Li = []
            for j in range(i):
                s = fdot(Li, Lo[j])
                Li.append((Ki[j] - s) / Ld[j])
            s2 = fdot(Li, Li)
            d = Ki[i] - sh - s2
            if d <= 0:
                return False, float(min_ratio), i, d
            bnd = 8 * (i + 2) * u * (abs(Ki[i] - sh) + s2)
            ratio = d / bnd
            if ratio < min_ratio:
                min_ratio = ratio
            Ld.append(mp.sqrt(d))
            Lo.append(Li)
        return True, float(min_ratio), h, None


def certify_tier2(spec, c_f, lam_f, fallback=False):
    """One tier-2 rung: dps-60/120 lags, ward, delta = spectral bound
    + rounding allowance, reach gate, dps-120 Cholesky + dps-200
    re-verification with the 10^6 pivot-vs-bound bar; floor attempt
    m = FLOOR_FRAC x lam_f (retry m = 0)."""
    M, h = spec["M"], spec["M"] // 2
    c_hi, eps_c, ward, t_lag = ward_eps(spec, c_f, DPS_T2)
    with mp.workdps(DPS_T2 + 10):
        delta = (2 * h * eps_c
                 + h * mp.mpf(ROUND_ALLOW) * max(abs(x) for x in c_hi))
    mode = ("validated-precision (budget fallback from tier-1)"
            if fallback else
            "validated-precision (mpmath Cholesky dps 120/200)")
    out = dict(h=h, mode=mode, eps_c=eps_c, ward=ward,
               shift=float(delta), lam_f=lam_f, t_lag=t_lag,
               t_cert=0.0, floor=None, npiv=0, bad=None, ratio=None)
    if lam_f < REACH_FACTOR * float(delta):
        out["status"] = "out-of-reach"
        return out
    Krows = build_K_rows(c_hi, M)
    t0 = time.time()
    for m in ((FLOOR_FRAC * max(lam_f, 0.0)), 0.0):
        with mp.workdps(DPS_T2 + 10):
            sh = delta + mp.mpf(m)
        ok1, r1, n1, _b1 = chol_pass(Krows, sh, DPS_T2)
        ok2, r2, n2, _b2 = chol_pass(Krows, sh, DPS_T2V)
        if ok1 and ok2 and r1 >= PIVOT_FACTOR and r2 >= PIVOT_FACTOR:
            out.update(status="certified", floor=m, npiv=n2,
                       ratio=min(r1, r2))
            break
        if not ok2 and m == 0.0:
            out.update(status="refused", npiv=n2, bad=_b2, ratio=r2)
            break
        if ok2 and m == 0.0:
            # positive pivots but the validation bar missed
            out.update(status="out-of-reach", npiv=n2,
                       ratio=min(r1, r2))
            break
    out["t_cert"] = time.time() - t0
    return out


# ------------------------------------------------ survey and driver
def rung_survey(kz):
    """One rung's deployed float64 assembly: geometry, lags, K and
    lambda_min(K) -- the frame_a_zones/build_window formulas,
    verbatim."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    h = M // 2
    ka = core.atoms_in(alpha)
    c_at, D = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    c_f = core.arch_lags(M, D) + c_at
    lam_f = float(np.linalg.eigvalsh(core.odd_toeplitz(c_f, M))[0])
    return dict(kz=kz, h=h, M=M, alpha=alpha, ka=ka,
                n_zone=int(core._NN[kz]), c_f=list(c_f), lam_f=lam_f)


def run_control():
    """The Epstein x^2+5y^2 comb at kz 9 through the identical tier-1
    machinery -- must be REFUSED (head-probe control, verbatim)."""
    r9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1
    lamE = np.zeros(N_E + 1)
    with mp.workdps(30):
        for n, v in enumerate(lambda_eps_mp(N_E)):
            lamE[n] = float(v)
    nn = [int(n) for n in np.nonzero(np.abs(lamE) > 1e-12)[0]]
    spec_e = dict(kind="epstein", M=r9["M"], n_zone=r9["n_zone"],
                  N_E=N_E, nn=nn)
    uuE = np.log(np.asarray(nn, float))
    mmE = 2.0 * lamE[nn] / np.sqrt(np.asarray(nn, float))
    c_atE, _ = core.atom_lags_at(r9["alpha"], r9["M"], uuE, mmE)
    c_fE = list(core.arch_lags(r9["M"], r9["D"]) + c_atE)
    lam_fE = float(np.linalg.eigvalsh(
        core.odd_toeplitz(np.asarray(c_fE), r9["M"]))[0])
    return certify_tier1(spec_e, c_fE, lam_fE)


def main():
    section("PRIME.PORT.CERTIFIED.LADDER.01 -- rigorous positivity "
            "certificates for ALL reachable rungs (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Tiers: h <= %d exact-"
          "rational (Bareiss, Q = 10^%d); h > %d validated-precision "
          "(Cholesky dps %d/%d)" % (TIER1_H_MAX, Q_POW, TIER1_H_MAX,
                                    DPS_T2, DPS_T2V))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("T0 -- float survey: lambda_min(K) on every reachable "
            "rung (h <= %d)" % H_LADDER_MAX)
    zones = [kz for kz in core.frame_a_zones()]
    rungs = []
    for kz in zones:
        r = rung_survey(kz)
        if r["h"] <= H_LADDER_MAX:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("T0.1 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(rungs) == N_RUNGS_EXP, "found %d" % len(rungs))
    grid_floor = 1.0 / 10 ** (Q_POW)
    print("\n    kz   h     M   n_zone  alpha    lam_min(f64)   "
          "lam/(h/Q)")
    for r in rungs:
        print("    %-4d %-5d %-5d %-7d %-8.3f %13.4e  %9.1e"
              % (r["kz"], r["h"], r["M"], r["n_zone"], r["alpha"],
                 r["lam_f"], r["lam_f"] / (r["h"] * grid_floor)),
              flush=True)
    n_pos = sum(1 for r in rungs if r["lam_f"] > 0)
    check("T0.2 float floors positive on all rungs (informative)",
          n_pos == len(rungs), "%d/%d positive" % (n_pos, len(rungs)))
    print("    [survey done at %.1f s]" % elapsed())

    section("C -- control (kz 9, Epstein x^2+5y^2 comb; runs before "
            "the ladder so the budget can never drop it)")
    res_e = run_control()
    print("    Epstein : h %d | ward rel %.2e | pivots done %d | "
          "first bad pivot index %s | lam_min(f64) %.3e | "
          "certificate %s | %.1f s"
          % (res_e["h"], res_e["ward"], res_e["npiv"],
             res_e["npiv"] if res_e["status"] == "refused" else "-",
             res_e["lam_f"],
             "REFUSED (fires)" if res_e["status"] == "refused"
             else res_e["status"].upper(),
             res_e["t_lag"] + res_e["t_cert"]), flush=True)
    check("C0 control ward: the mpmath Epstein lags match the "
          "float64 assembly at rel <= %.0e" % WARD_REL,
          res_e["ward"] <= WARD_REL, kill="K1")
    check("C1 CONTROL FIRES: the certificate machinery hits a "
          "nonpositive pivot on the Epstein comb -- the wall is "
          "REFUSED for the wrong comb", res_e["status"] == "refused",
          kill="K2")

    section("T1/T2/T3 -- the ladder (tier-1 ascending h, then "
            "tier-2 ascending h; budget %.0f s, deadline %.0f s, "
            "tier-1 slice %.0f s)" % (BUDGET_S, DEADLINE_S,
                                      T1_SLICE_S))
    tier1 = [r for r in rungs if r["h"] <= TIER1_H_MAX]
    tier2 = [r for r in rungs if r["h"] > TIER1_H_MAX]
    results = {}
    c1, c2, cl = C1_SEED, C2_SEED, CL_SEED

    def report(r, res):
        results[r["kz"]] = res
        st = res["status"]
        extra = ""
        if st == "certified":
            extra = "floor >= %.3e" % res["floor"]
            if res.get("ratio") is not None:
                extra += " | pivot/bound %.1e" % res["ratio"]
        elif st == "out-of-reach":
            extra = ("gap: lam_f %.3e < %.0f x shift %.3e"
                     % (res["lam_f"], REACH_FACTOR, res["shift"]))
        elif st == "refused":
            extra = "first bad pivot index %s" % res["npiv"]
        print("    kz %-4d h %-4d %-52s %-12s ward %.1e | eps_c %s | "
              "shift %.2e | %s | lag %.1fs cert %.1fs | t %.0fs"
              % (r["kz"], r["h"], res["mode"], st.upper(),
                 res["ward"], mp.nstr(res["eps_c"], 3), res["shift"],
                 extra, res["t_lag"], res["t_cert"], elapsed()),
              flush=True)

    # ---- tier-1 phase (exact-rational), slice-budgeted
    fallback = []
    for r in tier1:
        pred = c1 * r["h"] ** T1_EXP + cl * r["M"]
        if elapsed() + pred > min(T1_SLICE_S, DEADLINE_S):
            fallback.append(r)
            continue
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    ka=r["ka"])
        res = certify_tier1(spec, r["c_f"], r["lam_f"])
        report(r, res)
        if res["t_cert"] > 0:
            c1 = max(c1, res["t_cert"] / r["h"] ** T1_EXP)
        cl = max(cl, res["t_lag"] / r["M"])
    if fallback:
        print("    [tier-1 slice: %d rung(s) fall back to tier-2 "
              "mode: %s]" % (len(fallback),
                             [r["kz"] for r in fallback]), flush=True)

    # ---- tier-2 phase (validated-precision), deadline-budgeted
    queue = sorted(tier2 + fallback, key=lambda r: (r["h"], r["kz"]))
    fb_set = {r["kz"] for r in fallback}
    skipped = []
    for r in queue:
        pred = c2 * r["h"] ** 3 + cl * r["M"]
        if elapsed() + pred > DEADLINE_S:
            skipped.append(r)
            results[r["kz"]] = dict(h=r["h"], status="skipped-budget",
                                    mode="-", ward=0.0, shift=0.0,
                                    lam_f=r["lam_f"], floor=None,
                                    eps_c=mp.mpf(0), t_lag=0.0,
                                    t_cert=0.0)
            continue
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    ka=r["ka"])
        res = certify_tier2(spec, r["c_f"], r["lam_f"],
                            fallback=(r["kz"] in fb_set))
        report(r, res)
        if res["t_cert"] > 0:
            c2 = max(c2, res["t_cert"] / r["h"] ** 3)
        cl = max(cl, res["t_lag"] / r["M"])
    if skipped:
        print("    [SKIPPED-BUDGET: %s]"
              % [(r["kz"], r["h"]) for r in skipped], flush=True)

    # ---- gates over the attempted rungs
    attempted = [(r, results[r["kz"]]) for r in rungs
                 if results[r["kz"]]["status"] in
                 ("certified", "refused", "out-of-reach")]
    att_t1 = [(r, x) for r, x in attempted
              if x["mode"].startswith("exact-rational")]
    att_t2 = [(r, x) for r, x in attempted
              if x["mode"].startswith("validated-precision")]
    ok_ward = all(x["ward"] <= WARD_REL for _r, x in attempted)
    check("T1.1 CROSS-IMPLEMENTATION WARD: mpmath lags == deployed "
          "float64 core lags at rel <= %.0e on every attempted rung"
          % WARD_REL, ok_ward, kill="K1")
    ok_t1 = all(x["status"] != "refused" for _r, x in att_t1)
    check("T2.1 TIER-1: no attempted exact-rational rung refused "
          "(%d attempted)" % len(att_t1), ok_t1, kill="K1")
    ok_t2 = all(x["status"] != "refused" for _r, x in att_t2)
    check("T3.1 TIER-2: no attempted validated-precision rung "
          "refused (%d attempted; certified ones passed both dps "
          "%d/%d and the 10^6 pivot-vs-bound bar)"
          % (len(att_t2), DPS_T2, DPS_T2V), ok_t2, kill="K1")

    section("CENSUS -- per-rung certificate table")
    n_cert = n_oor = n_skip = n_ref = 0
    print("    kz   h     status          floor         mode")
    for r in rungs:
        x = results[r["kz"]]
        st = x["status"]
        n_cert += st == "certified"
        n_oor += st == "out-of-reach"
        n_skip += st == "skipped-budget"
        n_ref += st == "refused"
        fl = ("%.3e" % x["floor"]) if x.get("floor") is not None \
            else "-"
        print("    %-4d %-5d %-15s %-13s %s"
              % (r["kz"], r["h"], st.upper(), fl, x["mode"]),
              flush=True)
    print("\n    PROVEN %d/%d | out-of-reach %d | skipped-budget %d "
          "| refused %d" % (n_cert, len(rungs), n_oor, n_skip, n_ref))
    if n_oor:
        print("    out-of-reach census (need higher-precision lag "
              "evaluation -- the named follow-up):")
        for r in rungs:
            x = results[r["kz"]]
            if x["status"] == "out-of-reach":
                print("      kz %-4d h %-5d lam_f %.3e vs %.0f x "
                      "shift %.3e" % (r["kz"], r["h"], x["lam_f"],
                                      REACH_FACTOR, x["shift"]))

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "CERT-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    elif n_cert == len(rungs):
        VERDICT = "CERTIFIED-LADDER"
    else:
        VERDICT = "CERTIFIED-LADDER-PARTIAL"
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  DELIVERABLE: sigma_h > 0 certified on %d of the %d reachable
  rungs of the deployed v563 window ladder (tier 1 exact-rational
  integer Bareiss LDL; tier 2 validated-precision mpmath Cholesky
  at dps %d re-verified at dps %d -- typed separately, never
  conflated), modulo the stated conservative error model.  The
  remaining rungs are typed honestly (out-of-reach / skipped-
  budget) above.  The tail stays with the port contracts.
  NO RH claim.""" % (n_cert, len(rungs), DPS_T2, DPS_T2V))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (elapsed(), n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
