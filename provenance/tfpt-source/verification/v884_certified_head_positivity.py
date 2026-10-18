#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v884 -- PRIME.PORT.CERTIFIED.HEAD.01: THE FIRST RIGOROUS POSITIVITY STATEMENT OF THE PROGRAM -- sigma_h > 0 PROVEN on the head rungs kz 9 (h = 184), 12 (151), 13 (168) by EXACT INTEGER Bareiss/LDL Sylvester certificates, modulo a declared conservative transcendental-evaluation error model, with the Epstein control REFUSED by the identical machinery, ONE module from one probe (5/5 checks, zero fails, verdict CERTIFIED-HEAD; discovery probe certified_head_probe.py, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~6 min).  THE CERTIFICATE CHAIN: (1) the window lag vector is REBUILT INDEPENDENTLY in mpmath (dps 60 and dps 100; the dps disagreement defines the conservative per-entry evaluation error eps_c = 10 x disagreement with floor 1e-55; cross-ward against the deployed float64 core at <= 1.1e-14 -- the v1 ward CAUGHT a sign bug in the rebuilt Arch near-branch, rel 2.5 -> 1.1e-14, amendment on record: the ward did exactly its job); (2) K = G_plus - G_minus is assembled at high precision and shifted by the TOTAL error budget (matrix-level shift ~2e-18, i.e. ~14 orders below the certified margins) so that K_true >= K_shifted entrywise-provably; (3) K_shifted is scaled to the EXACT INTEGER grid Q = 10^20 (SPEC v2: Q lowered from 10^40 purely for the runtime budget, amendment on record) and an exact-arithmetic Bareiss/LDL elimination runs in unlimited-precision integers: ALL pivots > 0, hence K_shifted is positive definite by Sylvester, hence K_true > 0, hence sigma_h > 0 -- via the exact v866 equivalence K = G_plus - G_minus >= 0 <=> the wall, NO Lanczos and NO floating point in the decisive step; certified floors lambda_min >= 3.633e-4 / 3.327e-4 / 3.842e-4 (two confirmation runs).  THE CONTROL: the Epstein comb x^2 + 5y^2 through the IDENTICAL machinery is REFUSED at pivot index 10 (float lambda_min ~ -10.06) -- the kill test fires.  STATUS TYPING (honest, carried verbatim from the frozen spec): PROVEN MODULO the declared conservative lag-evaluation error model (validated-numerics standard); the formal end-to-end certification of the transcendental evaluations (ball arithmetic of the Arch evaluation) and the rollout to all 42 head rungs are the NAMED follow-up steps of PRIME.PORT.TAIL.01 -- this module is the head part of that contract's finite half.  NO RH claim; no marker moves; the certificates prove three finite rungs, not one-sidedness on the ladder.  mpmath + exact integers; no zeros, no prime-table oracles (AST firewall inside the probe); no RNG.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe certified_head_probe.py (5/5,
CERTIFIED-HEAD, SPEC v2 with the two amendments on record: the v1
cross-ward caught the rebuilt-Arch sign bug; the integer grid Q was
lowered 10^40 -> 10^20 mechanically for the runtime budget),
2026-08-09, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen source embedded BYTE-EXACT, executed verbatim in
an isolated namespace; printed spec SHA reproduces; byte-equality
ward vs experiments/tfpt-discovery/ inside the pattern gate.

CORPUS SURFACES: v866 (the K >= 0 equivalence), v563 (deployed
machinery, READ-ONLY cross-ward only); the ladder rollout
certificate probe (round 41) extends this head.  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source certified_head_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""certified_head_probe -- PRIME.PORT.CERTIFIED.HEAD.01
(EXPLORATION ONLY, experiments/; round 40, work package 2 of the
closing-cylinder plan: rigorous positivity certificates for the
finite head of the window ladder, 2026-08-09).

THE SIMPLIFICATION USED (promoted, v866/v876): the wall needs NO
Lanczos/Carleson pipeline.  Exactly: ||C_h|| <= 1  <=>  K >= 0
where K = odd_toeplitz(c, M) is DIRECTLY the h x h odd-Toeplitz
matrix (h = M/2, K[i,j] = c[|i-j|] - c[(M-1)-i-j]) of the window
lags c = c_arch + c_atoms.  A certified PSD proof of K is a
certified wall proof -- no orthogonal polynomials, no folding, no
density.

WHAT IS CERTIFIED (stated, conservative error model): the lag
assembly of the deployed v563 window -- the GL-48 panel quadrature
of the archimedean Weil layer (a FINITE, exactly specified real
algorithm) plus the exact tent atoms at positions log n with
masses 2 Lambda(n)/sqrt(n) -- is recomputed in mpmath at dps 60
AND dps 100 with exact high-precision Gauss-Legendre nodes.  The
error model is:
  eps_c   = SAFETY x max_i |c_dps60[i] - c_dps100[i]|  (SAFETY =
            10; floored at 1e-55), taken as a conservative
            per-entry radius |c_dps100 - c_true| <= eps_c;
  entrywise |K_dps100 - K_true| <= 2 eps_c, hence (Gershgorin/
            Frobenius) ||K_true - K_dps100||_2 <= 2 h eps_c;
  grid    : each K entry is floored onto the integer grid
            N[i,j] = floor(K[i,j] * Q), Q = 10^20 (SPEC v2, below;
            the Fraction-with-common-denominator route; per-entry
            error eta = 1/Q, spectral h eta) -- this IS the
            limit_denominator mitigation of the spec, realised as
            one common denominator so that exact rational LDL
            becomes exact INTEGER fraction-free LDL (Bareiss);
  shift   : s = 2 h eps_c + h eta; the integer matrix
            M_int = N - ceil(s Q) I is processed by EXACT integer
            Bareiss LDL (every intermediate division checked for
            zero remainder; pivot k = the (k+1)-st leading
            principal minor).  All pivots > 0  ==>  M_int PD
            (Sylvester)  ==>  K_true >= K_low - s I >= M_int/Q > 0.
  bound   : the same machinery on N - (ceil(s Q) + m Q) I gives a
            CERTIFIED lower bound lambda_min(K_true) >= m; two
            confirmation steps at m = 0.5 and 0.9 of the float64
            estimate are run when the base certificate is cheap.
Certificate type printed per rung: "exact-rational (integer
Bareiss LDL)" -- no floating step enters the positivity decision;
the only non-interval element is the dps60-vs-dps100 error model,
which is stated and conservative (factor 10 safety), NOT interval
arithmetic.

FROZEN PROTOCOL (2026-08-09; head rungs kz {9, 12, 13}; control
kz 9):

 T1  CROSS-IMPLEMENTATION WARD: the mpmath dps-100 lag vector
     must agree with the deployed float64 core lags (v563
     atom_lags_at + arch_lags, READ-ONLY) at relative sup
     distance <= 1e-9 (expected ~1e-12) on every head rung AND on
     the control comb.  A miss means the reimplementation is
     buggy -- fix, never proceed.

 T2  CERTIFIED HEAD: on every head rung the exact integer Bareiss
     LDL of the shifted grid matrix has ALL pivots > 0
     ==>  sigma_h > 0 PROVEN modulo the stated error model.
     Report per rung: h, eps_c, shift s, arithmetic mode, pivot
     count, certified lambda_min bound, runtime.

 C   CONTROL (must fire): the Epstein comb at kz 9 (the x^2+5y^2
     Dirichlet-series von-Mangoldt recursion, run in mpmath
     through the IDENTICAL lag assembly and certificate) must hit
     a nonpositive pivot -- the certificate machinery must REFUSE
     the wall for the wrong comb.

KILLS: K1 the ward fails or a head rung is refused ->
CERT-BROKEN; K2 the control is certified (does not fire) ->
CONTROL-DEAD.

VERDICT (frozen enum): CERTIFIED-HEAD / CERT-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first history preserved, house precedent):
  v1 (frozen 2026-08-09): grid Q = 10^40.  First run: the T1 ward
     FIRED at rel 2.5 -- a sign error in the reimplemented
     near-branch archimedean term (+tri_s log(-expm1(-2W)) instead
     of -tri_s log1p(-exp(-2W))); fixed, ward then 1.1e-14.
     Second run: certificates all PASSED but the kz-9 base Bareiss
     took 164 s, projecting the full protocol past the 10-minute
     budget (integer growth ~ 40 digits per elimination step).
  v2 (this file): Q = 10^20 -- a purely mechanical performance
     amendment; the arithmetic stays EXACT integer Bareiss, the
     error model is unchanged in kind, and the total conservative
     shift rises only to ~2e-18, still >= 14 orders below the
     measured wall margins (~4e-4).  Nothing else changed.

NO RH claim: these are finite-h positivity certificates for three
window rungs of the deployed ladder; the tail (h -> infinity) is
untouched and stays with the registered port contracts.

FIREWALL: no zeros, no prime oracles (AST scan for zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime);
the atom tables come from the deployed v563 window, READ-ONLY;
the only factorisation used is trial-division smallest-prime-
factor recovery on the v563 atom list (needed for exact masses
log p in mpmath).  Deterministic, no RNG.  Stdout only -- writes
nothing.  No marker moves.

Sources (read-only): v563_paper2_readouts (window/lag assembly);
v866/v876 (wall <=> odd-Toeplitz PSD, promoted);
port_scalar_schur_probe (Epstein control recursion, round 39);
port_tau_determinant_probe (house template, round 40 WP1).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/certified_head_probe.py
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

HEAD = (9, 12, 13)
DPS_LO, DPS_HI = 60, 100
SAFETY = 10                    # error-model safety factor on eps_c
EPS_FLOOR = "1e-55"            # eps_c floor (dps-60 round-off scale)
Q_POW = 20                     # grid denominator Q = 10^Q_POW (SPEC v2)
WARD_REL = 1.0e-9              # T1 bar (expected ~1e-12)
GL_N = 48                      # the deployed panel order (v563)
BISECT_BUDGET = 120.0          # s; skip the bound steps above this
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


# ------------------------------------------------ mpmath lag assembly
def gl_nodes(n):
    """Gauss-Legendre nodes/weights by Newton on P_n at current dps."""
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
    from the READ-ONLY v563 atom list, so spf(n) = its base p)."""
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


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
    mpmath at the given dps.  spec: kind, M, n_zone, and for
    kind=='epstein' the (READ-ONLY float-selected) support nn."""
    with mp.workdps(dps):
        glx, glw = gl_nodes(GL_N)
        alpha = mp.log(spec["n_zone"])
        M = spec["M"]
        if spec["kind"] == "prime":
            uu = [mp.log(n) for n in spec["atoms_n"]]
            mm = [2 * mp.log(spf(n)) / mp.sqrt(n)
                  for n in spec["atoms_n"]]
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


# ------------------------------------------------ exact certificate
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


def grid_matrix(c_hi, M, Q):
    """K = odd_toeplitz(c, M) on the integer grid N = floor(K Q)."""
    h = M // 2
    with mp.workdps(DPS_HI + 10):
        Qm = mp.mpf(Q)
        N = [[0] * h for _ in range(h)]
        for i in range(h):
            for j in range(i, h):
                kij = c_hi[abs(i - j)] - c_hi[(M - 1) - i - j]
                N[i][j] = N[j][i] = int(mp.floor(kij * Qm))
    return N


def certify(spec, c_f):
    """One rung: dps-60/100 lags, ward vs the float64 core lags,
    conservative shift, exact integer Bareiss certificate, and (when
    cheap) two certified lambda_min confirmation steps."""
    M, h = spec["M"], spec["M"] // 2
    Q = 10 ** Q_POW
    t_lag = time.time()
    c_lo = lags_mp(spec, DPS_LO)
    c_hi = lags_mp(spec, DPS_HI)
    t_lag = time.time() - t_lag
    with mp.workdps(DPS_HI + 10):
        eps_c = max(SAFETY * max(abs(a - b) for a, b in zip(c_lo, c_hi)),
                    mp.mpf(EPS_FLOOR))
        ward = (max(abs(a - mp.mpf(b)) for a, b in zip(c_hi, c_f))
                / max(abs(mp.mpf(b)) for b in c_f))
        shift_int = h + int(mp.ceil(2 * h * eps_c * Q))
        s_total = mp.mpf(shift_int) / Q
    N = grid_matrix(c_hi, M, Q)
    Kf = core.odd_toeplitz(np.asarray(c_f, float), M)
    lam_f = float(np.linalg.eigvalsh(Kf)[0])
    t_cert = time.time()
    base = [[N[i][j] - (shift_int if i == j else 0) for j in range(h)]
            for i in range(h)]
    ok, npiv, bad = bareiss_pd(base)
    t_cert = time.time() - t_cert
    lam_lb, n_conf = (mp.mpf(0) if ok else None), 0
    if ok and t_cert <= BISECT_BUDGET and lam_f > 0:
        for frac in (0.5, 0.9):
            m = frac * lam_f
            mQ = int(m * Q)
            okm, _, _ = bareiss_pd(
                [[N[i][j] - (shift_int + mQ if i == j else 0)
                  for j in range(h)] for i in range(h)])
            n_conf += 1
            if okm:
                lam_lb = mp.mpf(mQ) / Q
            else:
                break
    return dict(h=h, ok=ok, npiv=npiv, bad=bad, eps_c=eps_c,
                ward=float(ward), shift=s_total, lam_f=lam_f,
                lam_lb=lam_lb, n_conf=n_conf, t_lag=t_lag,
                t_cert=t_cert)


def main():
    section("PRIME.PORT.CERTIFIED.HEAD.01 -- rigorous positivity "
            "certificates for the ladder head (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Certificate mode: "
          "exact-rational (integer Bareiss LDL, Q = 10^%d)" % Q_POW)
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("T1/T2 -- the head rungs kz %s" % (HEAD,))
    rows = []
    ok_ward = ok_cert = True
    for kz in HEAD:
        r = core.build_window(kz)
        ka = r["n_atom"]
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    atoms_n=[int(n) for n in core._NN[:ka]])
        c_at_f, _ = core.atom_lags_at(r["alpha"], r["M"],
                                      np.asarray(r["uu"], float),
                                      2.0 * np.asarray(r["lam"], float))
        c_f = list(core.arch_lags(r["M"], r["D"]) + c_at_f)
        res = certify(spec, c_f)
        ok_ward &= res["ward"] <= WARD_REL
        ok_cert &= res["ok"]
        rows.append((kz, res))
        print("    kz %-3d h %4d | ward rel %.2e | eps_c %s | "
              "shift %s | pivots %d/%d %s | lam_min(f64) %.3e | "
              "certified lam_min >= %s (%d conf) | lag %.1fs "
              "cert %.1fs"
              % (kz, res["h"], res["ward"], mp.nstr(res["eps_c"], 3),
                 mp.nstr(res["shift"], 3), res["npiv"], res["h"],
                 "OK" if res["ok"] else "REFUSED", res["lam_f"],
                 mp.nstr(res["lam_lb"], 4), res["n_conf"],
                 res["t_lag"], res["t_cert"]), flush=True)
    check("T1.1 CROSS-IMPLEMENTATION WARD: mpmath dps-100 lags == "
          "deployed float64 core lags at rel <= %.0e on every head "
          "rung" % WARD_REL, ok_ward, kill="K1")
    check("T2.1 CERTIFIED HEAD: exact integer Bareiss LDL passes "
          "with ALL pivots > 0 on every head rung -- sigma_h > 0 "
          "PROVEN modulo the stated conservative error model "
          "(eps_c from dps-60/100 disagreement x%d, grid eta = "
          "10^-%d, spectral shift 2 h eps_c + h eta)"
          % (SAFETY, Q_POW), ok_cert, kill="K1")

    section("C -- control (kz 9, Epstein x^2+5y^2 comb)")
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
    res_e = certify(spec_e, c_fE)
    print("    Epstein : h %d | ward rel %.2e | pivots done %d | "
          "first bad pivot index %s | lam_min(f64) %.3e | "
          "certificate %s"
          % (res_e["h"], res_e["ward"], res_e["npiv"],
             res_e["npiv"] if not res_e["ok"] else "-",
             res_e["lam_f"],
             "REFUSED (fires)" if not res_e["ok"] else "PASSED"),
          flush=True)
    ok_ward_e = res_e["ward"] <= WARD_REL
    check("C0 control ward: the mpmath Epstein lags match the "
          "float64 assembly at rel <= %.0e" % WARD_REL, ok_ward_e,
          kill="K1")
    check("C1 CONTROL FIRES: the certificate machinery hits a "
          "nonpositive pivot on the Epstein comb -- the wall is "
          "REFUSED for the wrong comb", not res_e["ok"], kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "CERT-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "CERTIFIED-HEAD"
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  DELIVERABLE: sigma_h > 0 PROVEN (modulo the stated, conservative
  error model printed above) on the head rungs kz 9, 12, 13 of the
  deployed v563 window ladder, by exact integer Bareiss LDL of the
  conservatively shifted odd-Toeplitz lag matrix -- the v866/v876
  equivalence makes this a certified wall proof for the finite
  head.  The tail stays with the port contracts.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('certified_head_probe', _SRC_0, 5, (), 'CERTIFIED-HEAD', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v884 -- PRIME.PORT.CERTIFIED.HEAD.01 (+ LADDER rollout): rigorous positivity certificates for the head of the window ladder -- sigma_h > 0 PROVEN by exact integer Bareiss/LDL modulo a declared conservative lag error model')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v884: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the first rigorous positivity statements of the program; Epstein refused by the identical machinery')
    print("[%s] v884 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
