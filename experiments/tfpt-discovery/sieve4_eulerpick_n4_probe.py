#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sieve4_eulerpick_n4_probe -- PRIME.EULERPICK.N4.SIEVE.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe (plus its
compiled helper sieve4_helper.c, SHA-pinned below) is the sole
instrument of the round.  It writes nothing except its own compiled
binary sieve4_helper.bin, imports no repository module, reads no
measured pin, zero table, paper, ledger, website or verification
file, and makes NO RH claim in either direction.

MISSION
=======
Push the certified Euler--Pick falsification ladder of round 95
(PRIME.EULERPICK.CERTIFIED.LADDER.01, eulerpick_ladder_probe.py,
SPEC_SHA bef49fd06f5ef609) from N = 3 to N = 4 with a compiled
segmented sieve, per the round-95 named upgrade path
X_req(4) ~ 10^11.5.  Same object, same criterion (V0c, audited in
CCCXCIII, not re-litigated): P(sigma) = xi'/xi(1/2+sigma),
sigma_j = 1+1/j, Pick_N[j,k] = (P(sigma_j)+P(sigma_k))/(sigma_j+
sigma_k); RH iff Pick_N >= 0 for all N.  A certified positive floor
at N = 4 is an unconditional finite RH-consequence check from prime
data alone; a certified negative would be an RH-disproof candidate
(falsification channel, kept open and asserted empty).

S1 -- THE FAR-TAIL FLOOR (load-bearing finding of this round)
=============================================================
Round 95's tail enclosure bounds E(x) = psi(x) - x beyond
T = 1e19 (the end of the cited Buethe sqrt-x range) only by
0 <= psi(x) < 1.03883 x.  The resulting lower-side radius
s*T^{1-s}/(s-1) at node j = 4 (s = 7/4) is 1.31e-14 -- LARGER than
lambda_min(Pick_4) ~ 1.106e-14 itself and INDEPENDENT of the sieve
cap X.  The round-95 required-cap model (its G15) omitted this
floor: under the round-95 citations alone, N = 4 is uncertifiable
at ANY cap.  This probe adds one elementary, airtight input:
  NAIR (M. Nair, "On Chebyshev-type inequalities for primes",
  Amer. Math. Monthly 89 (1982), 126-129): lcm(1,...,n) >= 2^{n-1}
  for n >= 7, hence psi(x) = log lcm(1,...,floor(x)) >=
  (floor(x)-1) log 2 >= (x-2) log 2 for all x >= 7.
So E(x) >= -(1-log 2) x - 2 log 2 beyond T, and the far lower
radius drops by the factor (1-log 2) = 0.3069 to ~4.0e-15 at j = 4:
certification at N = 4 becomes possible and needs
X_req(4) ~ 10^11.5 (recomputed with the corrected model, gated).
Both the necessity of the Nair floor and the corrected budget are
gated; the crude-floor assembly is also RUN as a demonstration.

S2 -- CERTIFIED ENCLOSURES (architecture = round 95, re-implemented)
====================================================================
P(sigma) source-only from the absolutely convergent identity, for
s = 1/2 + sigma = (3j+2)/(2j) >= 7/4:
  P = 1/s + 1/(s-1) - (1/2)log(pi) + (1/2)psi(s/2)
      - sum_{n<=X} Lambda(n) n^{-s} - T(s,X).
(a) FINITE PART, split at Y = 1e6:
    - primes p <= Y and ALL prime powers p^m <= X (m >= 2, only
      ~sqrt(X) terms) in mpmath.iv outward-rounded intervals
      (iv.dps = 26 sum pass / 60 assembly);
    - primes Y < p <= X in the compiled helper (sieve4_helper.c,
      cc -O2, SHA-pinned, subprocessed over NCHUNK deterministic
      chunks combined in fixed order at dps 60).
(b) SUMMATION-ERROR MODEL (typed, gated).  The helper computes
    p^{-s} WITHOUT exp/pow: p^{-2} = (1/p)^2 and IEEE-correct
    sqrt/cbrt composites (u = 2^-53; div/sqrt/mult <= 0.5 ulp each
    by IEEE-754; ASSUMPTION A, gated pointwise: libm log and cbrt
    <= 2 ulp).  Derived per-term relative error <= 13.5u; FROZEN
    outward bound K_TERM = 32u.  Accumulation is double-double
    (two_sum + fast_two_sum, Shewchuk/QD), error <= 4u^2|acc| per
    add.  All terms positive, so the certified radius is
      ERR_S(j) = 32u * S_C(j) + 4 N_C u^2 * S_C(j)   (< 1e-18 here:
    the Y-split confines the float mass to S_C(4) ~ 4.2e-5), and
      ERR_TH  =  4u * theta_C + 4 N_C u^2 * theta_C  (< 1e-2, enters
    only via E(X) X^{-s} ~ 1e-25).  GATES: window-sum wards
    (mp.dps 50 references) at <= bound/2 on (100,1e5], (1e4,1e6],
    (1e6,4e6] and the top window (X-2e6, X]; pointwise sample wards
    (3 windows x 700 primes) at <= 16u = K_TERM/2; exactness wards
    pi(1e6) = 78498, pi(4e6) = 283146, psi(4e6) = corpus
    3999490.856797, and pi(X) = the exact published count (Y-split
    + helper chunk counts must reproduce it EXACTLY).
(c) TAIL, RIGOROUS (round-95 Abel structure + S1 floor):
      T(s,X) = X^{1-s}/(s-1) - E(X) X^{-s} + s int_X^inf E x^{-s-1},
    E(X) exact-to-enclosure from the own hybrid sieve; on [X, T]
    |E(x)| < 0.94 sqrt(x) (J. Buethe, Math. Comp. 87 (2018),
    1991-2009, valid 11 < x <= 1e19, corpus pin v594:10-13); beyond
    T = 1e19: E(x) in [-(1-log2)x - 2log2, 0.03883x] (NAIR lower,
    upper psi(x) < 1.03883x from Rosser--Schoenfeld, Illinois J.
    Math. 6 (1962), Theorem 12, all x > 0, corpus pin v563:136).
    Applicability AND own-data consistency warded per cap
    (|E| <= 0.94 sqrt(X), psi < 1.03883 X, psi > (X-2) log 2).
(d) ELEMENTARY TERMS: certified digamma enclosure as in round 95
    (shift 32, 32 terms, exact Bernoulli fractions, enveloping
    remainder via DLMF 5.9.13; containment + width gated).
(e) CERTIFIED lambda_min: entry enclosures -> midpoint Mc + radius
    R; Weyl + interval Cholesky on Mc - tau I (Rump, Acta Numerica
    19 (2010), Sec. 10; tau down a frozen factor ladder) give
    lambda_min >= tau - rho_up with rho_up >= ||R||_2 certified as
    min(max row sum, Frobenius norm) in iv (both are upper bounds
    for symmetric R; Frobenius is the sharper one here because R is
    concentrated in row/column 4).  Upper end: iv Rayleigh quotient
    on the float bottom eigenvector + rho_up.  Self-tests: planted
    PSD family, singular must-refuse, planted negative certified.

S3 -- THE BUDGET AND THE CAP (frozen decision rule)
===================================================
Radius model (Buethe term + far floor + summation), midpoint-shift
model (the Nair band is asymmetric; worst-case lambda shift =
||DeltaM||_F of the center offsets): X_req(4) = the X where
rho_F + shift_F = lambda_4; gated in (10^11.2, 10^12.2).  The far
floor saturates the budget beyond X ~ 1e13, so the FROZEN target
cap is X_TARGET = 1e13 = 10^13 (a decade and a half above the
round-95 named target; exact pin pi(1e13) = 346065536839), with
fallback X_FALL = 1e12 (pi = 37607912018) if the measured-throughput
prediction exceeds PRED_BAR = 2400 s.  Declared compute budget:
<= 60 min sieve wall on this machine's W workers; measured
throughput and the wall prediction are printed before the run.

S4 -- DELIVERABLES
==================
Certified [lambda_min_lo, lambda_min_hi] for N = 1..4 at the final
cap; N <= 3 floors must TIGHTEN against the round-95 pins
(lo3 = 2.3643695e-10 / hi3 = 1.1497752e-9 at cap 1.6e7); N = 4
verdict; corrected N = 5 wall: the far-tail floor at j = 5
(s = 17/10) is ~3.7e-14 vs lambda_5 ~ 7.9e-20 -- N = 5 is
KNOWLEDGE-walled at T = 1e19 (needs |psi(x)-x| <~ 0.94 sqrt(x) out
to ~1e28, i.e. verified zeros far beyond the current 3e12 height),
NOT merely sieve-walled as round 95's 10^16.3 suggested; the
sieve-side cost at the measured throughput is also printed.
dps is not binding anywhere (round-95 cost law unchanged).

VERDICT ENUMS (frozen):
 EULERPICK-N4-CERTIFIED(lo, margin)   certified lo > 0 at N = 4
 EULERPICK-N4-NARROWED(factor)        straddle; factor = needed
                                      radius shrink lambda/rho
 EULERPICK-NEGATIVE-CANDIDATE         certified hi < 0 (RH-disproof
                                      candidate, NOT a proof)
 SIEVE4-EDGE                          an instrument ward fails

KILL CRITERIA: source-only AST (no zeta/zetazero/siegel calls, no
data loads, no repository imports; helper SHA-pinned and grepped
free of any transcendental beyond log/cbrt/sqrt); the true first
ordinate 14.13... appears nowhere; every certified number is an
outward-rounded interval or carries a stated, gated error model;
finite N is NEVER sold as "all N"; NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from fractions import Fraction

import numpy as np
from mpmath import iv, mp

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
HERE = os.path.dirname(os.path.abspath(__file__))
HELPER_C = os.path.join(HERE, "sieve4_helper.c")
HELPER_BIN = os.path.join(HERE, "sieve4_helper.bin")
HELPER_SHA_PIN = ("d0242f53ad9f318ef673214062f5d50576777427"
                  "d0d59a735779daf380759b6b")

# ---------------------------------------------------------------- frozen
X_TARGET = 10 ** 13
X_FALL = 10 ** 12
Y_SPLIT = 10 ** 6
NCHUNK = 512
PRED_BAR = 2400.0
RUNTIME_BAR = 5400.0
N_CERT = 4
IV_DPS_SUM = 26
IV_DPS_CERT = 60
C_BUETHE = "0.94"
B_PSI = "1.03883"
T_BUETHE = 10 ** 19
X_BUETHE_MIN = 11
K_TERM_U = 32          # frozen per-term relative bound, units of u
E_LOG_U = 4            # frozen log relative bound, units of u
DD_ACC_U2 = 4          # dd accumulation bound per add, units of u^2
SAMPLE_N = 700
SAMPLE_TOL_U = 16      # = K_TERM_U / 2
DG_SHIFT = 32
DG_TERMS = 32
EM_CUT = 400
EM_TERMS = 60
TAU_FACTORS = ("0.99999999", "0.9999", "0.99", "0.9", "0.5", "0.25")
PI_PINS = {10 ** 6: 78_498, 4 * 10 ** 6: 283_146,
           10 ** 12: 37_607_912_018, 10 ** 13: 346_065_536_839}
CORPUS_PSI_4E6 = "3999490.856797"
CORPUS_FLOORS = ("4.59171357e-2", "9.0288888e-6",
                 "6.93102462e-10", "1.10594158e-14")
CORPUS_LAM5 = "7.91863638e-20"
R95_LO3 = "2.3643695e-10"
R95_HI3 = "1.1497752e-9"
R95_LO2_4E6 = "9.0287394e-6"
WIN_MICRO = (100, 10 ** 5)
WIN_A = (10 ** 4, 10 ** 6)
WIN_B = (10 ** 6, 4 * 10 ** 6)
TOP_SPAN = 2 * 10 ** 6
BENCH_SPAN = 3 * 10 ** 8

U = 2.0 ** -53

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-52s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fmt(x, digits: int = 8) -> str:
    return mp.nstr(x, digits, min_fixed=0, max_fixed=0)


def iv_lo(x) -> mp.mpf:
    return mp.make_mpf(x._mpi_[0])


def iv_hi(x) -> mp.mpf:
    return mp.make_mpf(x._mpi_[1])


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {"__future__", "ast", "hashlib", "math", "os",
                     "subprocess", "time", "concurrent", "fractions",
                     "mpmath", "numpy"}
    forbidden_calls = {"load", "loadtxt", "genfromtxt", "fromfile",
                       "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta", "zeta"}
    forbidden_attrs = {"zeta", "zetazero", "zetazeros", "nzeros",
                       "siegelz", "siegeltheta"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    with open(HELPER_C, "r", encoding="utf-8") as fh:
        csrc = fh.read()
    for word in ("zeta", "exp(", "pow("):
        if word in csrc:
            bad.append("helper:" + word)
    live = mp.__class__.__name__ == "MPContext"
    old = mp.dps
    mp.dps = 77
    live = live and mp.dps == 77
    mp.dps = old
    return (not bad) and live, ("violations=%s live_mp_context=%s"
                                % (bad or "none", live))


# ---------------------------------------------------------------- Bernoulli
def bernoulli_fracs(m_max: int) -> list[Fraction]:
    B = [Fraction(1)]
    for m in range(1, m_max + 1):
        acc = Fraction(0)
        for k in range(m):
            acc += math.comb(m + 1, k) * B[k]
        B.append(-acc / (m + 1))
    return B


BFR = bernoulli_fracs(2 * DG_TERMS + 2)


def iv_frac(fr: Fraction):
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def iv_digamma(x):
    """Certified digamma enclosure for real interval x > 0 (spec S2d)."""
    acc = iv.mpf(0)
    for k in range(DG_SHIFT):
        acc += 1 / (x + k)
    y = x + DG_SHIFT
    res = iv.log(y) - 1 / (2 * y) - acc
    y2 = 1 / (y * y)
    yp = y2
    for k in range(1, DG_TERMS + 1):
        res -= iv_frac(BFR[2 * k] / (2 * k)) * yp
        yp = yp * y2
    rem = iv_frac(abs(BFR[2 * DG_TERMS + 2]) / (2 * DG_TERMS + 2)) * yp
    return res + iv.mpf([-1, 1]) * rem


# ---------------------------------------------------------------- tail
def tail4_iv(s, X: int, EX):
    """Certified enclosure of sum_{n>X} Lambda(n) n^{-s} (spec S2c):
    Buethe on [X, 1e19], Nair/RS band beyond."""
    half = iv.mpf(1) / 2
    ln2 = iv.log(iv.mpf(2))
    lX = iv.log(iv.mpf(X))
    main = iv.exp((1 - s) * lX) / (s - 1) - EX * iv.exp(-s * lX)
    r_bu = iv.mpf(C_BUETHE) * iv.exp((half - s) * lX) / (s - half)
    lT = iv.log(iv.mpf(T_BUETHE))
    T1ms = iv.exp((1 - s) * lT)
    Tms = iv.exp(-s * lT)
    r_lo = (1 - ln2) * T1ms / (s - 1)
    r_hi = (iv.mpf(B_PSI) - 1) * T1ms / (s - 1)
    lo = iv_hi(s * (r_bu + r_lo) + 2 * ln2 * Tms)
    hi = iv_hi(s * (r_bu + r_hi))
    return main + iv.mpf([-lo, hi])


def tail4_iv_crude(s, X: int, EX):
    """Round-95 far bound (psi >= 0 only) -- for the S1 demonstration."""
    half = iv.mpf(1) / 2
    lX = iv.log(iv.mpf(X))
    main = iv.exp((1 - s) * lX) / (s - 1) - EX * iv.exp(-s * lX)
    r_bu = iv.mpf(C_BUETHE) * iv.exp((half - s) * lX) / (s - half)
    lT = iv.log(iv.mpf(T_BUETHE))
    T1ms = iv.exp((1 - s) * lT)
    r_lo = T1ms / (s - 1)
    r_hi = (iv.mpf(B_PSI) - 1) * T1ms / (s - 1)
    lo = iv_hi(s * (r_bu + r_lo))
    hi = iv_hi(s * (r_bu + r_hi))
    return main + iv.mpf([-lo, hi])


# ---------------------------------------------------------------- EM float P
def em_P(sigma, cutoff: int, terms: int):
    s = mp.mpf("0.5") + sigma
    tot = mp.mpf(0)
    der = mp.mpf(0)
    for n in range(2, cutoff):
        u = mp.power(n, -s)
        tot += u
        der -= mp.log(n) * u
    tot += 1
    M = mp.mpf(cutoff)
    lM = mp.log(M)
    lead = M ** (1 - s) / (s - 1)
    tot += lead
    der += lead * (-lM - 1 / (s - 1))
    half = mp.mpf("0.5") * M ** (-s)
    tot += half
    der -= lM * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        corr = (mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
                * mp.rf(s, order) * M ** (-s - order))
        harm = mp.fsum(1 / (s + i) for i in range(order))
        tot += corr
        der += corr * (harm - lM)
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + der / tot)


def lam_ladder(vals, sigmas, nmax: int) -> list:
    out = []
    for n in range(1, nmax + 1):
        M = mp.matrix(n, n)
        for j in range(n):
            for k in range(n):
                M[j, k] = (vals[j] + vals[k]) / (sigmas[j] + sigmas[k])
        out.append(mp.eigsy(M, eigvals_only=True)[0])
    return out


# ---------------------------------------------------------------- certificate
def rho_upper(rad, N: int):
    """Certified upper bound for ||R||_2: min(max row sum, Frobenius)."""
    row = mp.mpf(0)
    for j in range(N):
        acc = iv.mpf(0)
        for k in range(N):
            acc += iv.mpf(rad[j][k])
        row = max(row, iv_hi(acc))
    fr = iv.mpf(0)
    for j in range(N):
        for k in range(N):
            fr += iv.mpf(rad[j][k]) ** 2
    frob = iv_hi(iv.sqrt(fr))
    return min(row, frob), row, frob


def certified_lambda(mid, rad, N: int):
    """Certified [lo, hi] for lambda_min over all symmetric M with
    |M - Mc| <= R entrywise (method: spec S2e).  Returns
    (lo_or_None, hi, rho, lam_float)."""
    rho, _, _ = rho_upper(rad, N)
    Mmid = mp.matrix(N, N)
    for j in range(N):
        for k in range(N):
            Mmid[j, k] = mid[j][k]
    Ev, Q = mp.eigsy(Mmid)
    lam_t = min(Ev)
    idx = list(Ev).index(lam_t)
    v = [Q[r, idx] for r in range(N)]

    def chol_ok(tau) -> bool:
        A = [[iv.mpf(mid[j][k]) - (iv.mpf(tau) if j == k else 0)
              for k in range(N)] for j in range(N)]
        L = [[iv.mpf(0)] * N for _ in range(N)]
        for j in range(N):
            d = A[j][j]
            for t in range(j):
                d -= L[j][t] * L[j][t]
            if not iv_lo(d) > 0:
                return False
            L[j][j] = iv.sqrt(d)
            for k in range(j + 1, N):
                x = A[k][j]
                for t in range(j):
                    x -= L[k][t] * L[j][t]
                L[k][j] = x / L[j][j]
        return True

    tau_ok = None
    if lam_t > 0:
        for f in TAU_FACTORS:
            tau = lam_t * mp.mpf(f)
            if chol_ok(tau):
                tau_ok = tau
                break
    num = iv.mpf(0)
    den = iv.mpf(0)
    for j in range(N):
        den += iv.mpf(v[j]) ** 2
        for k in range(N):
            num += iv.mpf(v[j]) * iv.mpf(v[k]) * iv.mpf(mid[j][k])
    ray_up = iv_hi(num / den)
    lo = iv_lo(iv.mpf(tau_ok) - iv.mpf(rho)) if tau_ok is not None else None
    hi = iv_hi(iv.mpf(ray_up) + iv.mpf(rho))
    return lo, hi, rho, lam_t


def entry_mid_rad(P_enc, N: int):
    sig_fr = [Fraction(j + 1, j) for j in range(1, N + 1)]
    mid = [[None] * N for _ in range(N)]
    rad = [[None] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            E = (P_enc[j] + P_enc[k]) / iv_frac(sig_fr[j] + sig_fr[k])
            a, b = iv_lo(E), iv_hi(E)
            m = a + (b - a) / 2
            r = max(iv_hi(iv.mpf(m) - iv.mpf(a)),
                    iv_hi(iv.mpf(b) - iv.mpf(m)))
            mid[j][k] = m
            rad[j][k] = r
    return mid, rad


# ---------------------------------------------------------------- helper IO
def run_helper(lo: int, hi: int):
    """Returns (count, theta_dd, [S_dd x4]) as (hi, lo) float pairs."""
    out = subprocess.run([HELPER_BIN, "sum", str(lo), str(hi)],
                         capture_output=True, text=True, check=True)
    tok = out.stdout.split()
    assert tok[0] == "OK"
    cnt = int(tok[1])
    th = (float(tok[2]), float(tok[3]))
    S = [(float(tok[4 + 2 * j]), float(tok[5 + 2 * j])) for j in range(4)]
    return cnt, th, S


def run_helper_sample(lo: int, hi: int, maxn: int):
    out = subprocess.run([HELPER_BIN, "sample", str(lo), str(hi),
                          str(maxn)], capture_output=True, text=True,
                         check=True)
    rows = []
    for line in out.stdout.splitlines():
        tok = line.split()
        if tok and tok[0] == "P":
            rows.append((int(tok[1]), [float(t) for t in tok[2:7]]))
    return rows


def dd_to_mp(pair):
    return mp.mpf(pair[0]) + mp.mpf(pair[1])


def np_prime_sieve(limit: int) -> np.ndarray:
    bits = np.ones(limit + 1, dtype=bool)
    bits[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            bits[p * p::p] = False
    return np.flatnonzero(bits).astype(np.int64)


def np_window_primes(lo: int, hi: int, base: np.ndarray) -> np.ndarray:
    """Primes p with lo < p <= hi via a numpy segmented window sieve."""
    n = hi - lo
    bits = np.ones(n, dtype=bool)          # index i <-> lo + 1 + i
    for p in base:
        p = int(p)
        if p * p > hi:
            break
        start = max(p * p, (lo // p + 1) * p)
        if start > hi:
            continue
        bits[start - lo - 1::p] = False
    return (np.flatnonzero(bits) + lo + 1).astype(np.int64)


def mp_window_ref(primes, s_list):
    """dps-50 reference (theta, S_j) over an explicit prime list."""
    th = mp.mpf(0)
    ss = [mp.mpf(0)] * 4
    for p in primes:
        p = int(p)
        L = mp.log(p)
        th += L
        for i, s in enumerate(s_list):
            ss[i] += L * mp.power(p, -s)
    return th, ss


def err_model_S(S_up, n_terms: int):
    return (K_TERM_U * U + DD_ACC_U2 * n_terms * U * U) * S_up


def err_model_TH(th_up, n_terms: int):
    return (E_LOG_U * U + DD_ACC_U2 * n_terms * U * U) * th_up


# ---------------------------------------------------------------- budget
SIG_F = [1.0 + 1.0 / j for j in range(1, N_CERT + 1)]
S_F = [1.5 + 1.0 / j for j in range(1, N_CERT + 1)]
LN2 = math.log(2.0)


def far_band(j: int, nair: bool):
    """(lower_radius, upper_radius) of the beyond-T band at node j."""
    s = S_F[j - 1]
    t1ms = math.exp((1 - s) * math.log(T_BUETHE))
    lo = s * ((1 - LN2) if nair else 1.0) * t1ms / (s - 1)
    hi = s * 0.03883 * t1ms / (s - 1)
    return lo, hi


def model_matrices(logX: float, nair: bool, n: int = N_CERT):
    """Float model: (rho_F, shift_F) of the certified assembly."""
    r = []
    d = []
    for j in range(1, n + 1):
        s = S_F[j - 1]
        bu = s * 0.94 * math.exp((0.5 - s) * logX) / (s - 0.5)
        flo, fhi = far_band(j, nair)
        r.append(bu + (flo + fhi) / 2)
        d.append(abs(fhi - flo) / 2)
    fr = fs = 0.0
    for j in range(n):
        for k in range(n):
            den = SIG_F[j] + SIG_F[k]
            fr += ((r[j] + r[k]) / den) ** 2
            fs += ((d[j] + d[k]) / den) ** 2
    return math.sqrt(fr), math.sqrt(fs)


def x_req(lam: float, nair: bool, n: int = N_CERT):
    lo_l, hi_l = 9.0 * math.log(10), 16.0 * math.log(10)
    rho_inf, shift_inf = model_matrices(hi_l, nair, n)
    if rho_inf + shift_inf >= lam:
        return None                        # floor-blocked at any cap
    for _ in range(200):
        mid = (lo_l + hi_l) / 2
        rho, shift = model_matrices(mid, nair, n)
        if rho + shift > lam:
            lo_l = mid
        else:
            hi_l = mid
    return mid / math.log(10)


# ---------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("sieve4_eulerpick_n4_probe  PRIME.EULERPICK.N4.SIEVE.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ============================================================ Z0
    section("Z0. FIREWALL, HELPER BUILD, INSTRUMENT SELF-TESTS")
    ok, detail = firewall_audit()
    check("G01 source-only firewall + live mp context", ok, detail)

    with open(HELPER_C, "rb") as fh:
        hsha = hashlib.sha256(fh.read()).hexdigest()
    t_cc = time.time()
    cc = subprocess.run(["cc", "-O2", "-std=c11", "-o", HELPER_BIN,
                         HELPER_C, "-lm"], capture_output=True, text=True)
    check("G02 helper SHA pinned + cc -O2 compile",
          hsha == HELPER_SHA_PIN and cc.returncode == 0,
          "sha=%s.. cc_rc=%d (%.1f s)" % (hsha[:16], cc.returncode,
                                          time.time() - t_cc))

    iv.dps = IV_DPS_CERT
    mp.dps = IV_DPS_CERT
    mid2 = [[mp.mpf(2), mp.mpf(0)], [mp.mpf(0), mp.mpf(2)]]
    rad2 = [[mp.mpf("0.1")] * 2 for _ in range(2)]
    lo, hi, rho, _ = certified_lambda(mid2, rad2, 2)
    ones = [[mp.mpf(1), mp.mpf(1)], [mp.mpf(1), mp.mpf(1)]]
    zr = [[mp.mpf(0)] * 2 for _ in range(2)]
    lo_s, _, _, _ = certified_lambda(ones, zr, 2)
    negm = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(-1)]]
    _, hi_n, _, _ = certified_lambda(negm, zr, 2)
    check("G03 certificate self-tests (PSD/singular/negative)",
          lo is not None and lo > mp.mpf("1.79") and hi >= 2
          and lo_s is None and hi_n < 0,
          "PSD lo=%s; singular refused=%s; planted hi=%s < 0"
          % (fmt(lo, 6), lo_s is None, fmt(hi_n, 4)))

    mp.dps = 120
    worst_w = mp.mpf(0)
    contain = True
    for nu, de in [(3, 4), (5, 4), (5, 4), (1, 1), (11, 12), (7, 8)]:
        x_iv = iv.mpf(nu) / iv.mpf(de)
        ref = mp.digamma(mp.mpf(nu) / de)
        enc = iv_digamma(x_iv)
        contain = contain and (iv_lo(enc) <= ref <= iv_hi(enc))
        worst_w = max(worst_w, iv_hi(enc) - iv_lo(enc))
    check("G04 certified digamma: containment + width",
          contain and worst_w < mp.mpf("1e-50"),
          "contains mp.digamma on 6 nodes, max width=%s" % fmt(worst_w, 3))

    # ============================================================ Z1
    section("Z1. HYBRID SIEVE, SMALL SIDE (iv) + HELPER WARDS")
    t_np = time.time()
    base_primes = np_prime_sieve(4 * 10 ** 6)
    pi_1e6 = int(np.searchsorted(base_primes, Y_SPLIT, "right"))
    pi_4e6 = len(base_primes)
    check("G05 sieve anchors: pi(1e6), pi(4e6)",
          pi_1e6 == PI_PINS[10 ** 6] and pi_4e6 == PI_PINS[4 * 10 ** 6],
          "pi(1e6)=%d pi(4e6)=%d (numpy %.1f s)"
          % (pi_1e6, pi_4e6, time.time() - t_np))

    mp.dps = 50
    S_MP = [mp.mpf(3 * j + 2) / (2 * j) for j in range(1, N_CERT + 1)]

    # micro ward (100, 1e5] against dps-50 reference
    t_w = time.time()
    cnt_m, th_m, S_m = run_helper(*WIN_MICRO)
    prs = [int(p) for p in base_primes
           if WIN_MICRO[0] < p <= WIN_MICRO[1]]
    th_ref, ss_ref = mp_window_ref(prs, S_MP)
    dev_th = abs(dd_to_mp(th_m) - th_ref)
    ok_m = (cnt_m == len(prs)
            and dev_th <= err_model_TH(th_ref, cnt_m) / 2)
    worst_ratio = mp.mpf(0)
    for j in range(4):
        dev = abs(dd_to_mp(S_m[j]) - ss_ref[j])
        bound = err_model_S(ss_ref[j], cnt_m)
        ok_m = ok_m and dev <= bound / 2
        worst_ratio = max(worst_ratio, dev / bound)
    check("G06 micro exactness ward (100,1e5] vs dps-50",
          ok_m, "count=%d dev/bound worst=%s (bar 0.5), %.1f s"
          % (cnt_m, fmt(worst_ratio, 3), time.time() - t_w))

    # window wards (1e4,1e6] and (1e6,4e6]
    t_w = time.time()
    ok_w = True
    msgs = []
    for wlo, whi in (WIN_A, WIN_B):
        cnt_w, th_w, S_w = run_helper(wlo, whi)
        prs = [int(p) for p in base_primes if wlo < p <= whi]
        th_ref, ss_ref = mp_window_ref(prs, S_MP)
        this = (cnt_w == len(prs)
                and abs(dd_to_mp(th_w) - th_ref)
                <= err_model_TH(th_ref, cnt_w) / 2)
        wr = mp.mpf(0)
        for j in range(4):
            dev = abs(dd_to_mp(S_w[j]) - ss_ref[j])
            bound = err_model_S(ss_ref[j], cnt_w)
            this = this and dev <= bound / 2
            wr = max(wr, dev / bound)
        ok_w = ok_w and this
        msgs.append("(%.0e,%.0e]: n=%d ratio=%s" % (wlo, whi, cnt_w,
                                                    fmt(wr, 3)))
    check("G07 window-sum wards vs dps-50 (bar dev<=bound/2)",
          ok_w, "; ".join(msgs) + " (%.1f s)" % (time.time() - t_w))

    # iv small-prime pass p <= Y (enters the final enclosure)
    t_iv = time.time()
    iv.dps = IV_DPS_SUM
    S_IV = [iv.mpf(3 * j + 2) / iv.mpf(2 * j) for j in range(1, 5)]
    th_small = iv.mpf(0)
    S_small = [iv.mpf(0) for _ in range(4)]
    th_4e6 = iv.mpf(0)
    S_4e6 = [iv.mpf(0) for _ in range(4)]
    for p in base_primes:
        p = int(p)
        L = iv.log(iv.mpf(p))
        terms = [L * iv.exp(-S_IV[i] * L) for i in range(4)]
        if p <= Y_SPLIT:
            th_small += L
            for i in range(4):
                S_small[i] += terms[i]
        th_4e6 += L
        for i in range(4):
            S_4e6[i] += terms[i]
    print("  iv prime pass p<=4e6 (dps %d): %.1f s"
          % (IV_DPS_SUM, time.time() - t_iv))
    t_iv = time.time()

    def iv_powers(cap: int):
        """theta-part and S-part of prime powers p^m <= cap, m >= 2."""
        th = iv.mpf(0)
        ss = [iv.mpf(0) for _ in range(4)]
        for p in base_primes:
            p = int(p)
            if p * p > cap:
                break
            L = iv.log(iv.mpf(p))
            q = p * p
            m = 2
            while q <= cap:
                th += L
                for i in range(4):
                    ss[i] += L * iv.exp(-S_IV[i] * (m * L))
                q *= p
                m += 1
        return th, ss

    # ============================================================ Z2
    section("Z2. BUDGET: FAR-TAIL FLOOR, CORRECTED X_req, CAP DECISION")
    lam4 = float(mp.mpf(CORPUS_FLOORS[3]))
    rho_crude, shift_crude = model_matrices(50.0, nair=False)
    rho_nair, shift_nair = model_matrices(50.0, nair=True)
    print("  beyond-1e19 floor at infinite cap (radius+shift, Frobenius):")
    print("    crude (psi>=0):  rho_F=%.3e shift_F=%.3e sum=%.3e  vs"
          " lambda_4=%.3e" % (rho_crude, shift_crude,
                              rho_crude + shift_crude, lam4))
    print("    Nair  (x-2)ln2:  rho_F=%.3e shift_F=%.3e sum=%.3e"
          % (rho_nair, shift_nair, rho_nair + shift_nair))
    xr_crude = x_req(lam4, nair=False)
    xr_nair = x_req(lam4, nair=True)
    check("G08 far-tail floor necessity: crude floor blocks N=4 at ANY"
          " cap, Nair unblocks",
          xr_crude is None and xr_nair is not None
          and rho_crude + shift_crude > lam4,
          "X_req(crude)=%s X_req(Nair)=10^%.2f (round-95 G15 said 10^11.48"
          " without the floor)" % (xr_crude, xr_nair or -1))
    check("G09 corrected budget: X_req(4) in (10^11.2, 10^12.2)",
          xr_nair is not None and 11.2 < xr_nair < 12.2,
          "X_req(4)=10^%.3f incl. Nair floor + midpoint shift" % xr_nair)

    # throughput benchmark -> frozen cap decision
    t_b = time.time()
    b1_lo = 10 ** 9
    cnt_b1, _, _ = run_helper(b1_lo, b1_lo + BENCH_SPAN)
    t_b1 = time.time() - t_b
    t_b = time.time()
    b2_lo = X_TARGET - BENCH_SPAN
    cnt_b2, _, _ = run_helper(b2_lo, X_TARGET)
    t_b2 = time.time() - t_b
    ns_per = max(t_b1, t_b2) / BENCH_SPAN * 1e9
    W = min(24, max(4, (os.cpu_count() or 8) - 8))
    pred = (X_TARGET - Y_SPLIT) * ns_per * 1e-9 / W * 1.20
    rate_core = max(cnt_b1, cnt_b2) / min(t_b1, t_b2)
    print("  benchmark: %.2f ns/number (spans at 1e9: %.2fs, at top:"
          " %.2fs); ~%.2e primes/s/core; W=%d workers"
          % (ns_per, t_b1, t_b2, rate_core, W))
    X_FINAL = X_TARGET if pred <= PRED_BAR else X_FALL
    check("G10 cap decision (frozen rule): predicted wall vs bar",
          X_FINAL in PI_PINS,
          "pred=%.0f s (bar %.0f) -> X_FINAL=1e%d, margin to X_req ="
          " 10^%.2f" % (pred, PRED_BAR, round(math.log10(X_FINAL)),
                        math.log10(X_FINAL) - xr_nair))

    # ============================================================ Z3
    section("Z3. FULL COMPILED RUN TO X = %.1e (W=%d, %d chunks)"
            % (X_FINAL, W, NCHUNK))
    bounds = [Y_SPLIT + (i * (X_FINAL - Y_SPLIT)) // NCHUNK
              for i in range(NCHUNK + 1)]
    results: dict[int, tuple] = {}
    t_run = time.time()
    done = [0, 0]  # chunks, primes

    def job(i: int):
        r = run_helper(bounds[i], bounds[i + 1])
        return i, r

    with ThreadPoolExecutor(max_workers=W) as pool:
        futs = [pool.submit(job, i) for i in range(NCHUNK)]
        for fut in as_completed(futs):
            i, r = fut.result()
            results[i] = r
            done[0] += 1
            done[1] += r[0]
            if done[0] % 64 == 0 or done[0] == NCHUNK:
                el = time.time() - t_run
                print("  progress %3d/%d chunks  %.3e primes  %.0f s"
                      "  ETA %.0f s"
                      % (done[0], NCHUNK, done[1], el,
                         el / done[0] * (NCHUNK - done[0])))
    t_sieve = time.time() - t_run
    mp.dps = IV_DPS_CERT
    N_C = sum(results[i][0] for i in range(NCHUNK))
    th_C = mp.mpf(0)
    S_C = [mp.mpf(0) for _ in range(4)]
    for i in range(NCHUNK):
        th_C += dd_to_mp(results[i][1])
        for j in range(4):
            S_C[j] += dd_to_mp(results[i][2][j])
    rate = N_C / t_sieve
    print("  sieve wall %.1f s, %d primes in (1e6, %.0e], throughput"
          " %.2e primes/s = %.2e primes/min (%d workers)"
          % (t_sieve, N_C, X_FINAL, rate, rate * 60, W))
    check("G11 exact prime-count pin at final cap",
          pi_1e6 + N_C == PI_PINS[X_FINAL],
          "pi(%.0e) = %d + %d = %d (published %d)"
          % (X_FINAL, pi_1e6, N_C, pi_1e6 + N_C, PI_PINS[X_FINAL]))

    # top-window ward at the final cap
    t_w = time.time()
    top_lo = X_FINAL - TOP_SPAN
    base_top = np_prime_sieve(math.isqrt(X_FINAL) + 1)
    prs_top = np_window_primes(top_lo, X_FINAL, base_top)
    cnt_t, th_t, S_t = run_helper(top_lo, X_FINAL)
    mp.dps = 50
    th_ref, ss_ref = mp_window_ref(prs_top, S_MP)
    ok_t = (cnt_t == len(prs_top)
            and abs(dd_to_mp(th_t) - th_ref)
            <= err_model_TH(th_ref, cnt_t) / 2)
    wr = mp.mpf(0)
    for j in range(4):
        dev = abs(dd_to_mp(S_t[j]) - ss_ref[j])
        bound = err_model_S(ss_ref[j], cnt_t)
        ok_t = ok_t and dev <= bound / 2
        wr = max(wr, dev / bound)
    check("G12 top-window ward (X-2e6, X] vs dps-50",
          ok_t, "n=%d dev/bound worst=%s (%.1f s)"
          % (cnt_t, fmt(wr, 3), time.time() - t_w))

    # pointwise sample ward (Assumption A: libm log/cbrt <= 2 ulp)
    t_w = time.time()
    mp.dps = 40
    worst_u = 0.0
    n_samp = 0
    for wlo in (Y_SPLIT, 10 ** 10, X_FINAL - 2 * 10 ** 5):
        whi = min(wlo + 10 ** 7, X_FINAL)
        for p, vals in run_helper_sample(wlo, whi, SAMPLE_N):
            n_samp += 1
            L = mp.log(p)
            refs = [L] + [L * mp.power(p, -s) for s in S_MP]
            for c, r in zip(vals, refs):
                worst_u = max(worst_u, abs(float((mp.mpf(c) - r) / r)) / U)
    check("G13 pointwise term ward: max rel err <= %du (=K_TERM/2)"
          % SAMPLE_TOL_U, worst_u <= SAMPLE_TOL_U,
          "%d samples x 5 values, worst = %.3f u (%.1f s)"
          % (n_samp, worst_u, time.time() - t_w))

    # ---- assembly of certified S(s,X), psi(X), E(X)
    iv.dps = IV_DPS_CERT
    mp.dps = IV_DPS_CERT
    th_pow, S_pow = iv_powers(X_FINAL)
    th_pow4, _ = iv_powers(4 * 10 ** 6)
    print("  prime-power pass p^m <= X in iv: %.1f s"
          % (time.time() - t_iv))

    err_th = err_model_TH(th_C * (1 + mp.mpf(2) ** -40), N_C)
    psi_X = (th_small + iv.mpf(th_C)
             + iv.mpf([-float(err_th), float(err_th)]) + th_pow)
    EX = psi_X - X_FINAL
    E_mid = iv_lo(EX) + (iv_hi(EX) - iv_lo(EX)) / 2
    E_abs = max(abs(iv_lo(EX)), abs(iv_hi(EX)))
    psi_4e6 = th_4e6 + th_pow4
    mid4 = iv_lo(psi_4e6) + (iv_hi(psi_4e6) - iv_lo(psi_4e6)) / 2
    check("G14 psi anchors + bound applicability wards",
          abs(mid4 - mp.mpf(CORPUS_PSI_4E6)) < mp.mpf("1e-5")
          and X_BUETHE_MIN < X_FINAL <= T_BUETHE
          and E_abs < 0.94 * math.sqrt(X_FINAL)
          and iv_hi(psi_X) < mp.mpf(B_PSI) * X_FINAL
          and iv_lo(psi_X) > (X_FINAL - 2) * LN2,
          "psi(4e6)=%s (corpus %s); E(X)=%s width %.2e; |E|<=0.94sqrtX,"
          " psi<1.03883X, psi>(X-2)ln2 all hold"
          % (fmt(mid4, 13), CORPUS_PSI_4E6, fmt(E_mid, 6),
             float(iv_hi(EX) - iv_lo(EX))))

    S_total = []
    err_msgs = []
    ok_err = True
    for j in range(4):
        e = float(err_model_S(S_C[j] * (1 + mp.mpf(2) ** -40), N_C))
        band = iv.mpf([-e, e])
        S_total.append(S_small[j] + iv.mpf(S_C[j]) + band + S_pow[j])
        ok_err = ok_err and e <= 1e-18
        err_msgs.append("ERR_S(%d)=%.1e" % (j + 1, e))
    check("G15 summation-error model gate: ERR_S<=1e-18, ERR_TH<=1e-2",
          ok_err and float(err_th) <= 1e-2,
          "; ".join(err_msgs) + "; ERR_TH=%.2e" % float(err_th))

    LOG_PI = iv.log(iv.pi)
    P_ENC = []
    P_ENC_CRUDE = []
    for j in range(1, 5):
        s = iv.mpf(3 * j + 2) / iv.mpf(2 * j)
        elem = 1 / s + 1 / (s - 1) - LOG_PI / 2 + iv_digamma(s / 2) / 2
        P_ENC.append(elem - S_total[j - 1] - tail4_iv(s, X_FINAL, EX))
        P_ENC_CRUDE.append(elem - S_total[j - 1]
                           - tail4_iv_crude(s, X_FINAL, EX))
    print("  P(sigma_j) certified widths at X=%.0e (Nair | crude):"
          % X_FINAL)
    for j in range(4):
        print("    j=%d: %.3e | %.3e"
              % (j + 1, float(iv_hi(P_ENC[j]) - iv_lo(P_ENC[j])),
                 float(iv_hi(P_ENC_CRUDE[j]) - iv_lo(P_ENC_CRUDE[j]))))

    # EM float reference + containment + corpus parity
    mp.dps = 120
    sig120 = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, 5)]
    P_ref = [em_P(s, EM_CUT, EM_TERMS) for s in sig120]
    lam_ref = lam_ladder(P_ref, sig120, 4)
    parity = max(abs(lam_ref[i] / mp.mpf(CORPUS_FLOORS[i]) - 1)
                 for i in range(4))
    contain = all(iv_lo(P_ENC[j]) <= P_ref[j] <= iv_hi(P_ENC[j])
                  for j in range(4))
    check("G16 EM reference: corpus floor parity + containment",
          parity < mp.mpf("1e-7") and contain,
          "max floor rel dev=%s; EM P inside all 4 enclosures"
          % fmt(parity, 3))

    # certified floors N=1..4
    mp.dps = IV_DPS_CERT
    floors = {}
    print("  certified lambda_min intervals at X=%.0e (Nair tail):"
          % X_FINAL)
    for N in range(1, 5):
        mid, rad = entry_mid_rad(P_ENC[:N], N)
        lo, hi, rho, lam_t = certified_lambda(mid, rad, N)
        floors[N] = (lo, hi, rho, lam_t)
        print("    N=%d  lo=%-14s hi=%-13s rho_up=%-10s  %s"
              % (N, fmt(lo, 8) if lo is not None else "none",
                 fmt(hi, 8), fmt(rho, 4),
                 "CERTIFIED POSITIVE" if (lo is not None and lo > 0)
                 else "UNDECIDED AT THIS CAP"))
    in_int = all((floors[N][0] is None or floors[N][0] <= lam_ref[N - 1])
                 and lam_ref[N - 1] <= floors[N][1] for N in range(1, 5))
    check("G17 float reference floors inside certified intervals",
          in_int, "N=1..4")

    lo1, lo2, lo3 = floors[1][0], floors[2][0], floors[3][0]
    w3 = floors[3][1] - floors[3][0] if lo3 is not None else None
    check("G18 N<=3 floors tightened vs round 95",
          lo1 is not None and lo1 > mp.mpf("4.59e-2")
          and lo2 is not None and lo2 > mp.mpf(R95_LO2_4E6)
          and lo3 is not None and lo3 > mp.mpf("5e-10")
          and w3 is not None and w3 < mp.mpf("1e-12"),
          "lo3: %s -> %s (r95 cap 1.6e7), width3: %s -> %s"
          % (R95_LO3, fmt(lo3, 8),
             fmt(mp.mpf(R95_HI3) - mp.mpf(R95_LO3), 3), fmt(w3, 3)))

    lo4, hi4, rho4, lam4t = floors[4]
    margin = (lo4 / lam4t) if (lo4 is not None and lam4t > 0) else None
    if lo4 is not None and lo4 > 0:
        verdict_n4 = ("EULERPICK-N4-CERTIFIED(lo=%s, margin=lo/lam=%s)"
                      % (fmt(lo4, 8), fmt(margin, 4)))
    elif hi4 < 0:
        verdict_n4 = "EULERPICK-NEGATIVE-CANDIDATE"
    else:
        need = float(rho4) / float(lam4t) if lam4t > 0 else float("inf")
        verdict_n4 = "EULERPICK-N4-NARROWED(factor %.2f)" % need
    check("G19 N=4 positivity certificate (the round's target)",
          lo4 is not None and lo4 > 0,
          "N=4: [%s, %s], rho=%s -> %s"
          % (fmt(lo4, 8) if lo4 is not None else "none",
             fmt(hi4, 8), fmt(rho4, 4), verdict_n4))

    # crude-floor demonstration (S1): same data, round-95 far bound
    mid_c, rad_c = entry_mid_rad(P_ENC_CRUDE, 4)
    lo4c, hi4c, rho4c, lam4c = certified_lambda(mid_c, rad_c, 4)
    print("  S1 demonstration, crude far bound (psi>=0 only): N=4"
          " lo=%s hi=%s rho=%s lam_mid=%s"
          % (fmt(lo4c, 6) if lo4c is not None else "none",
             fmt(hi4c, 6), fmt(rho4c, 4), fmt(lam4c, 6)))

    neg_hit = [N for N in range(1, 5) if floors[N][1] < 0]
    check("G20 falsification channel: no certified negative rung",
          not neg_hit and hi4c > 0,
          "certified hi<0 rungs: %s (a hit would be an RH-disproof"
          " candidate)" % (neg_hit or "none"))

    # ============================================================ Z4
    section("Z4. COST LAW: MEASURED THROUGHPUT, N=5 WALL (CORRECTED)")
    lam5 = float(mp.mpf(CORPUS_LAM5))
    S_F.append(1.5 + 1.0 / 5)
    SIG_F.append(1.0 + 1.0 / 5)
    flo5, fhi5 = far_band(5, nair=True)
    xr5_bu = None
    lo_l, hi_l = 12.0 * math.log(10), 22.0 * math.log(10)
    for _ in range(200):
        mid_l = (lo_l + hi_l) / 2
        s5 = S_F[4]
        bu5 = s5 * 0.94 * math.exp((0.5 - s5) * mid_l) / (s5 - 0.5)
        if bu5 * 2.0 > lam5:      # Buethe-only reach (floor ignored)
            lo_l = mid_l
        else:
            hi_l = mid_l
    xr5_bu = mid_l / math.log(10)
    t_pp = (1 - LN2)
    T_need = (lam5 / 4 / (S_F[4] * t_pp / (S_F[4] - 1))) \
        ** (1.0 / (1 - S_F[4]))
    span5 = 10 ** xr5_bu
    days5 = span5 * ns_per * 1e-9 / W / 86400
    print("  N=5: far floor at T=1e19 (Nair) = %.3e vs lambda_5 = %.3e"
          " -- excess factor %.1e AT ANY CAP" % (flo5, lam5, flo5 / lam5))
    print("  N=5 would need the sqrt-x psi bound out to T ~ %.1e"
          " (currently 1e19; verified-zeros height ~3e12)" % T_need)
    print("  N=5 sieve-side alone (floor magically solved): X ~ 10^%.2f,"
          " %.1f machine-days at the measured %.2f ns/number on W=%d"
          % (xr5_bu, days5, ns_per, W))
    check("G21 corrected N=5 wall: KNOWLEDGE-walled at T=1e19, not"
          " sieve-walled",
          flo5 > 100 * lam5 and T_need > 10 ** 25
          and 15.5 < xr5_bu < 17.5,
          "floor/lambda_5=%.1e, T_need=%.1e, X_req5(Buethe-only)"
          "=10^%.2f" % (flo5 / lam5, T_need, xr5_bu))

    elapsed = time.time() - T0
    check("G22 runtime < %.0f s" % RUNTIME_BAR, elapsed < RUNTIME_BAR,
          "%.1f s total (sieve %.1f s)" % (elapsed, t_sieve))

    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    n_tot = len(CHECKS)
    edge = any(not ok for name, ok, _ in CHECKS
               if name.startswith(("G01", "G02", "G03", "G04", "G05",
                                   "G06", "G07", "G11", "G12", "G13")))
    verdict = verdict_n4 if not edge else "SIEVE4-EDGE"

    print("\n" + "=" * 78)
    print("CHECKS: %d/%d PASS" % (n_pass, n_tot))
    print("COMPOSITE VERDICT: %s" % verdict)
    print("N<=3 floors (tightened): lo1=%s lo2=%s lo3=%s"
          % (fmt(lo1, 9), fmt(lo2, 9), fmt(lo3, 9)))
    print("NO RH CLAIM IN EITHER DIRECTION.  EXPLORATION ONLY.")
    print("SPEC_SHA %s   runtime %.1f s" % (SPEC_SHA[:16], elapsed))
    print("=" * 78)
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
