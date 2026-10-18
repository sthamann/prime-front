#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""certified_ladder_tail_probe -- PRIME.PORT.CERTIFIED.LADDER.02
(EXPLORATION ONLY, experiments/; round 40, completion of the
certificate rollout, 2026-08-09).

COMPLETES PRIME.PORT.CERTIFIED.LADDER.01 (certified_ladder_probe.py,
verdict CERTIFIED-LADDER-PARTIAL): the parent probe PROVED
sigma_h > 0 on 40 of the 42 reachable rungs of the deployed v563
window ladder; the two deepest rungs h = 859 and h = 878 were typed
SKIPPED-BUDGET at the frozen 45-minute deadline.  THIS probe applies
the IDENTICAL tier-2 validated-precision machinery (copied verbatim
from the parent) to EXACTLY those two rungs, with NO wall-clock
deadline -- elapsed time is printed per stage; a total runtime of
30-90 minutes is expected and acceptable.

TIER-2 MACHINERY (verbatim from the parent; "validated-precision
(mpmath Cholesky dps 120/200)" -- NOT exact-rational, and never
labelled as such): the wall <=> odd-Toeplitz PSD simplification
(promoted, v866/v876): ||C_h|| <= 1  <=>  K >= 0 where
K = odd_toeplitz(c, M) is DIRECTLY the h x h odd-Toeplitz matrix of
the window lags c = c_arch + c_atoms.  Lags at dps 60/120;
conservative error model eps_c = SAFETY x the dps-60-vs-120 lag
disagreement (SAFETY = 10, floored at 1e-55), entrywise
|K_hi - K_true| <= 2 eps_c, spectral ||.||_2 <= 2 h eps_c -- stated
and conservative, NOT interval arithmetic.  K assembled at dps 130
(entries then exact binary rationals), shifted by delta + m with
delta = 2 h eps_c + h * 10^-118 * max|c|   (the spectral error
bound PLUS a rigorous rounding allowance for the single-subtraction
K assembly at dps 130), m = 0.5 x lambda_min(f64) with an m = 0
retry on refusal.  Cholesky runs at working dps 120; on success it
is RE-RUN at dps 200 (precision doubling) and every pivot d_j must
exceed 10^6 x the accumulated per-pivot rounding-bound estimate
b_j = 8 (j+2) u (|K_jj - shift| + sum_k L_jk^2), u = 2^(2-prec),
at BOTH precisions.  Certified only if both passes are
positive-definite AND both ratio bars hold; a nonpositive pivot at
dps 200 is a genuine refusal (K1); positive pivots that miss the
ratio bar are typed out-of-reach (precision), never certified and
never a kill.  The parent's reach gate (float lambda_min >= 100 x
delta, prime rungs only) is kept verbatim.

FROZEN PROTOCOL (2026-08-09; the 2 tail rungs; control kz 9):

 T0  TAIL SURVEY: the deployed float64 assembly (frame_a_zones /
     build_window formulas, verbatim) must yield EXACTLY the two
     frozen tail rungs h = 859 and h = 878 among the reachable
     rungs, and their float64 lambda_min(K) is printed up front.
 C   CONTROL (must fire; runs IMMEDIATELY after the survey): the
     Epstein x^2+5y^2 comb at kz 9, through the IDENTICAL tier-1
     lag assembly and exact integer Bareiss certificate of the
     parent probe (verbatim, unconditional -- SPEC v2 of the
     parent), must hit a nonpositive pivot: the machinery must
     REFUSE the wall for the wrong comb.
 T1  CROSS-IMPLEMENTATION WARD: on both attempted rungs (and the
     control) the high-dps mpmath lag vector must agree with the
     deployed float64 core lags at relative sup distance <= 1e-9.
     A miss means the reimplementation is buggy -- fix, never
     proceed.
 T2  TAIL CERTIFICATES: both rungs must pass BOTH Cholesky
     precisions AND the 10^6 pivot-vs-bound bar; typed
     "validated-precision", never "exact-rational".  Report per
     rung: h, eps_c, shift, mode, certified floor, per-stage
     runtimes.

NO RUNTIME BUDGET (frozen): unlike the parent, there is NO deadline
and NO skip path -- both rungs are always attempted to completion.
Elapsed time is tracked and printed per stage (lag assembly, K
assembly, each Cholesky pass, per rung, total).

KILLS: K1 the ward fails on an attempted rung, or an attempted
prime rung is genuinely refused (nonpositive pivot at dps 200 at
m = 0) -> CERT-REFUSED (an honest kill, reported loudly); K2 the
control is certified (does not fire) -> CONTROL-DEAD.

VERDICT (frozen enum): CERTIFIED-LADDER-COMPLETE (both tail rungs
certified -- together with the parent's 40 this closes all 42
reachable rungs) / CERT-OUT-OF-REACH (>= 1 rung typed out-of-reach:
reach gate missed or positive pivots below the ratio bar; no kill)
/ CERT-REFUSED / CONTROL-DEAD.

MECHANICAL CACHES (performance only, no protocol content): the
Gauss-Legendre nodes per dps, the atom position/mass PREFIX per
dps, and the trial-division smallest-prime-factor memo -- all
verbatim from the parent.  The per-stage progress prints inside the
tier-2 certificate are reporting only; no bar, error model or
arithmetic differs from the parent.

SPEC AMENDMENTS (fail-first history preserved, house precedent):
  v1 (frozen 2026-08-09, pre-run): everything above.

NO RH claim: these are finite-h positivity certificates for the
two deepest reachable rungs of the deployed v563 window ladder;
the tail (h -> infinity) is untouched and stays with the
registered port contracts.

FIREWALL: no zeros, no prime oracles (AST scan for zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime);
the atom tables come from the deployed v563 window, READ-ONLY;
the only factorisation used is trial-division smallest-prime-
factor recovery on the v563 atom list (needed for exact masses
log p in mpmath).  Deterministic, no RNG.  Stdout only -- writes
nothing.  No marker moves.

Sources (read-only): certified_ladder_probe (the parent, round 40
WP(a); machinery copied verbatim); certified_head_probe (round 40
WP2); v563_paper2_readouts (window/lag assembly); v866/v876
(wall <=> odd-Toeplitz PSD, promoted); port_scalar_schur_probe
(Epstein control recursion, round 39).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/certified_ladder_tail_probe.py
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

H_LADDER_MAX = 900             # reachable-rung cap (as the parent)
H_TAIL = (859, 878)            # frozen: the two SKIPPED-BUDGET rungs
DPS_LO = 60                    # low lag precision (error model)
DPS_T1 = 100                   # tier-1 high lag precision (control)
DPS_T2 = 120                   # tier-2 lag/Cholesky precision
DPS_T2V = 200                  # tier-2 verification precision
SAFETY = 10                    # error-model safety factor on eps_c
EPS_FLOOR = "1e-55"            # eps_c floor (dps-60 round-off scale)
Q_POW = 20                     # grid denominator Q = 10^Q_POW (control)
WARD_REL = 1.0e-9              # T1 bar (expected ~1e-12)
GL_N = 48                      # the deployed panel order (v563)
REACH_FACTOR = 100.0           # float lam_min >= this x shift bound
PIVOT_FACTOR = 1.0e6           # tier-2 pivot > this x rounding bound
FLOOR_FRAC = 0.5               # certified-floor attempt m = this x lam_f
ROUND_ALLOW = "1e-118"         # tier-2 K-assembly rounding allowance/h
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
# (kept verbatim from the parent ONLY for the Epstein control at kz 9)
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
    # Parent SPEC v2: the reach gate applies to prime rungs only; the
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


def certify_tier2(spec, c_f, lam_f):
    """One tier-2 rung: dps-60/120 lags, ward, delta = spectral bound
    + rounding allowance, reach gate, dps-120 Cholesky + dps-200
    re-verification with the 10^6 pivot-vs-bound bar; floor attempt
    m = FLOOR_FRAC x lam_f (retry m = 0).  Arithmetic verbatim from
    the parent; the [stage] prints are reporting only."""
    M, h = spec["M"], spec["M"] // 2
    c_hi, eps_c, ward, t_lag = ward_eps(spec, c_f, DPS_T2)
    print("      [stage] h %d lag assembly dps %d/%d done: %.1f s "
          "(total %.1f s)" % (h, DPS_LO, DPS_T2, t_lag, elapsed()),
          flush=True)
    with mp.workdps(DPS_T2 + 10):
        delta = (2 * h * eps_c
                 + h * mp.mpf(ROUND_ALLOW) * max(abs(x) for x in c_hi))
    mode = "validated-precision (mpmath Cholesky dps 120/200)"
    out = dict(h=h, mode=mode, eps_c=eps_c, ward=ward,
               shift=float(delta), lam_f=lam_f, t_lag=t_lag,
               t_cert=0.0, floor=None, npiv=0, bad=None, ratio=None)
    if lam_f < REACH_FACTOR * float(delta):
        out["status"] = "out-of-reach"
        return out
    tK = time.time()
    Krows = build_K_rows(c_hi, M)
    print("      [stage] h %d K assembly (dps %d) done: %.1f s "
          "(total %.1f s)" % (h, DPS_T2 + 10, time.time() - tK,
                              elapsed()), flush=True)
    t0 = time.time()
    for m in ((FLOOR_FRAC * max(lam_f, 0.0)), 0.0):
        with mp.workdps(DPS_T2 + 10):
            sh = delta + mp.mpf(m)
        tc = time.time()
        ok1, r1, n1, _b1 = chol_pass(Krows, sh, DPS_T2)
        print("      [stage] h %d Cholesky dps %d (m %.3e): pd %s | "
              "min pivot/bound %.2e | %.1f s (total %.1f s)"
              % (h, DPS_T2, m, ok1, r1, time.time() - tc, elapsed()),
              flush=True)
        tc = time.time()
        ok2, r2, n2, _b2 = chol_pass(Krows, sh, DPS_T2V)
        print("      [stage] h %d Cholesky dps %d (m %.3e): pd %s | "
              "min pivot/bound %.2e | %.1f s (total %.1f s)"
              % (h, DPS_T2V, m, ok2, r2, time.time() - tc, elapsed()),
              flush=True)
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


def rung_h(kz):
    """The rung geometry only (cheap; used to select the tail rungs
    before the full float survey)."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M // 2


def run_control():
    """The Epstein x^2+5y^2 comb at kz 9 through the identical tier-1
    machinery -- must be REFUSED (parent control, verbatim)."""
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
    section("PRIME.PORT.CERTIFIED.LADDER.02 -- tail rungs h = %d and "
            "h = %d, no deadline (EXPLORATION ONLY)" % H_TAIL)
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Mode: validated-"
          "precision (mpmath Cholesky dps %d/%d), verbatim from "
          "PRIME.PORT.CERTIFIED.LADDER.01" % (DPS_T2, DPS_T2V))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("T0 -- tail survey: the two frozen rungs h in %s"
            % (H_TAIL,))
    tail_kz = [kz for kz in core.frame_a_zones()
               if rung_h(kz) in H_TAIL]
    rungs = [rung_survey(kz) for kz in tail_kz]
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("T0.1 frozen tail set: exactly the rungs h = %d and h = %d"
          % H_TAIL, sorted(r["h"] for r in rungs) == sorted(H_TAIL),
          "found %s" % [(r["kz"], r["h"]) for r in rungs])
    print("\n    kz   h     M     n_zone   alpha    lam_min(f64)")
    for r in rungs:
        print("    %-4d %-5d %-5d %-8d %-8.3f %13.4e"
              % (r["kz"], r["h"], r["M"], r["n_zone"], r["alpha"],
                 r["lam_f"]), flush=True)
    n_pos = sum(1 for r in rungs if r["lam_f"] > 0)
    check("T0.2 float floors positive on both rungs (informative)",
          n_pos == len(rungs), "%d/%d positive" % (n_pos, len(rungs)))
    print("    [survey done at %.1f s]" % elapsed())

    section("C -- control (kz 9, Epstein x^2+5y^2 comb; runs before "
            "the tail rungs)")
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
    print("    [control done at %.1f s]" % elapsed())

    section("T1/T2 -- the tail certificates (ascending h; NO "
            "deadline, NO skip path)")
    results = {}

    def report(r, res):
        results[r["kz"]] = res
        st = res["status"]
        extra = ""
        if st == "certified":
            extra = "floor >= %.3e" % res["floor"]
            if res.get("ratio") is not None:
                extra += " | pivot/bound %.1e" % res["ratio"]
        elif st == "out-of-reach":
            if res.get("ratio") is not None:
                extra = ("ratio bar missed: min pivot/bound %.1e < "
                         "%.0e" % (res["ratio"], PIVOT_FACTOR))
            else:
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

    for r in rungs:
        print("\n    [rung kz %d, h %d: attempting -- started at "
              "%.1f s]" % (r["kz"], r["h"], elapsed()), flush=True)
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    ka=r["ka"])
        res = certify_tier2(spec, r["c_f"], r["lam_f"])
        report(r, res)

    # ---- gates over the attempted rungs
    attempted = [(r, results[r["kz"]]) for r in rungs]
    ok_ward = all(x["ward"] <= WARD_REL for _r, x in attempted)
    check("T1.1 CROSS-IMPLEMENTATION WARD: mpmath lags == deployed "
          "float64 core lags at rel <= %.0e on both attempted rungs"
          % WARD_REL, ok_ward, kill="K1")
    ok_ref = all(x["status"] != "refused" for _r, x in attempted)
    check("T2.1 TAIL: no attempted rung genuinely refused "
          "(certified ones passed both dps %d/%d and the 10^6 "
          "pivot-vs-bound bar)" % (DPS_T2, DPS_T2V), ok_ref,
          kill="K1")

    section("CENSUS -- per-rung certificate table")
    n_cert = n_oor = n_ref = 0
    print("    kz   h     status          floor         mode")
    for r in rungs:
        x = results[r["kz"]]
        st = x["status"]
        n_cert += st == "certified"
        n_oor += st == "out-of-reach"
        n_ref += st == "refused"
        fl = ("%.3e" % x["floor"]) if x.get("floor") is not None \
            else "-"
        print("    %-4d %-5d %-15s %-13s %s"
              % (r["kz"], r["h"], st.upper(), fl, x["mode"]),
              flush=True)
    print("\n    PROVEN %d/%d | out-of-reach %d | refused %d"
          % (n_cert, len(rungs), n_oor, n_ref))

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "CERT-REFUSED",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    elif n_cert == len(rungs) and len(rungs) == len(H_TAIL):
        VERDICT = "CERTIFIED-LADDER-COMPLETE"
    else:
        VERDICT = "CERT-OUT-OF-REACH"
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  DELIVERABLE: the two deepest reachable rungs (h = %d and h = %d)
  of the deployed v563 window ladder, left SKIPPED-BUDGET by
  PRIME.PORT.CERTIFIED.LADDER.01, attempted to completion with the
  parent's tier-2 validated-precision machinery (mpmath Cholesky at
  dps %d re-verified at dps %d, 10^6 pivot-vs-bound bar), modulo
  the stated conservative error model.  %d/%d certified here; with
  the parent's 40/42 this %s the reachable ladder.  The tail
  (h -> infinity) stays with the port contracts.  NO RH claim."""
          % (H_TAIL[0], H_TAIL[1], DPS_T2, DPS_T2V, n_cert,
             len(rungs),
             "CLOSES" if VERDICT == "CERTIFIED-LADDER-COMPLETE"
             else "does NOT yet close"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (elapsed(), n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
