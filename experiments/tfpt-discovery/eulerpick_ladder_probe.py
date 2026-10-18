#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""eulerpick_ladder_probe -- PRIME.EULERPICK.CERTIFIED.LADDER.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, zero table, paper, ledger, website or
verification file, and makes NO RH claim in either direction.

MISSION
=======
Turn the Euler--Pick falsification ladder pinned by
PRIME.SCREW.VERBLUNSKY.INVARIANT.01 (V0c) into a CERTIFIED instrument:
outward-rounded interval enclosures end to end, machine-checked
positivity certificates per rung, an honest wall quantification, and
the measured detection law that prices what the instrument can see.

THE OBJECT.  P(sigma) = xi'/xi(1/2+sigma), sigma_j = 1+1/j, and
  Pick_N[j,k] = (P(sigma_j)+P(sigma_k))/(sigma_j+sigma_k).
The audited criterion (V0c, not re-litigated here):
RH iff Pick_N >= 0 for every N.  Forward (RH => all Pick_N PSD) is
exact -- two rank-one Grams per zero ordinate.  Hence a CERTIFIED
negative eigenvalue at any N would DISPROVE RH using the forward
direction alone; a certified positive floor at N is an unconditional
finite consequence check of RH from prime data alone (source-only:
no zero computations anywhere in this file).

E1 -- CERTIFIED ENCLOSURES, NOT FLOATS
======================================
P(sigma) is computed source-only from the absolutely convergent
identity, for s = 1/2+sigma = (3j+2)/(2j) > 3/2:
  P = 1/s + 1/(s-1) - (1/2)log(pi) + (1/2)psi(s/2)
      - sum_{n<=X} Lambda(n) n^{-s}  -  T(s,X),
  T(s,X) = sum_{n>X} Lambda(n) n^{-s}.
(a) FINITE PART: own sieve to X, every term Lambda(n)n^{-s} evaluated
    in mpmath.iv outward-rounded interval arithmetic (iv.dps = 22 for
    the prime pass; per-term widths ~1e-20 are negligible against the
    tail widths that dominate every verdict-relevant number).
(b) TAIL, RIGOROUS.  With psi(x) = x + E(x), Stieltjes/Abel partial
    summation for s > 1 gives (boundary term at infinity vanishes by
    psi(x) < 1.03883 x and s > 1):
      T(s,X) = X^{1-s}/(s-1) - E(X) X^{-s} + s int_X^inf E(x) x^{-s-1} dx.
    E(X) is EXACT from the own sieve.  The integral is enclosed by
      |int_X^A E x^{-s-1} dx| <= 0.94 X^{1/2-s}/(s-1/2),  A = 1e19,
    from the published bound |psi(x)-x| < 0.94 sqrt(x) for
    11 < x <= 1e19 (J. Buethe, "An analytic method for bounding
    psi(x)", Math. Comp. 87 (2018), 1991-2009; backed by verified
    zeros; same citation and range as corpus v594_unconditional_cert
    lines 10-13), and beyond A by the two-sided crude pair
    0 <= psi(x) < 1.03883 x (upper: Rosser--Schoenfeld, "Approximate
    formulas for some functions of prime numbers", Illinois J. Math. 6
    (1962) 64-94, Theorem 12, valid for ALL x > 0, maximum of
    psi(x)/x at x = 113; the corpus pin B_PSI in v563 line 136), i.e.
    E(x) in [-x, 0.03883 x] there, contributing
    [-A^{1-s}/(s-1), 0.03883 A^{1-s}/(s-1)].  Applicability is gated
    per cap (11 < X <= 1e19) and the citations are additionally
    WARDED against the own exact sieve data (|E(X)| <= 0.94 sqrt(X)
    and psi(X) < 1.03883 X at every cap -- necessary conditions).
(c) ELEMENTARY TERMS: 1/s, 1/(s-1), log(pi) in iv; psi(s/2) by an own
    certified digamma: recurrence shift by 32, then the asymptotic
    series psi(y) = log y - 1/(2y) - sum_{k=1}^{32} B_{2k}/(2k y^{2k})
    + R with |R| <= |B_66|/(66 y^66), B_2k EXACT rationals (Fraction
    recurrence).  The remainder bound is the classical enveloping
    property of the digamma asymptotic series for real y > 0: in the
    Binet-type representation psi(y) = log y - 1/(2y)
    - 2 int_0^inf t dt/((t^2+y^2)(e^{2pi t}-1)) (DLMF 5.9.13), expand
    1/(t^2+y^2) geometrically with the exact alternating remainder
    (-1)^K t^{2K}/(y^{2K}(t^2+y^2)); each moment produces one series
    term, the remainder integral is bounded by the first omitted
    term and carries its sign.  Gated against mp.digamma (containment
    + width bar).
(d) CERTIFIED lambda_min FOR THE SYMMETRIC INTERVAL MATRIX (method
    STATED): entry enclosures E_jk = (P_j+P_k)/(sigma_j+sigma_k) give
    a midpoint matrix Mc and an outward radius matrix R.  For every
    symmetric M with |M-Mc| <= R entrywise (which contains the TRUE
    Pick_N), Weyl + Perron give
      lambda_min(M) >= tau - rho_up,  provided  Mc - tau I > 0,
    where rho_up >= ||R||_2 is the certified maximal row sum of R and
    Mc - tau I > 0 is certified by INTERVAL CHOLESKY (all pivots with
    certified positive lower endpoint; Rump-style verification, cf.
    S. M. Rump, "Verification methods: Rigorous results using
    floating-point arithmetic", Acta Numerica 19 (2010), Sec. 10).
    tau runs down a frozen factor ladder from the float eigenvalue.
    Upper end: lambda_min(M) <= RayleighUp(Mc,v0) + rho_up with v0
    the float bottom eigenvector (Rayleigh quotient >= lambda_min
    always; evaluated in iv, upper endpoint taken).  Deliverable per
    N: certified [lambda_min_lo, lambda_min_hi]; lo > 0 is a
    machine-checked positivity certificate for the true Pick_N;
    hi < 0 anywhere would be a certified RH disproof (falsification
    channel, self-tested on a planted negative family).

E2 -- THE WALL, MEASURED AND PRICED
===================================
Caps X = 1e5, 4e5, 1e6, 4e6 (corpus cap), 1.6e7 in ONE ascending
sieve pass with snapshots.  Frozen expectations from the derivation:
certified floor width per node scales as X^{-(1+1/j)} (slope gated);
cap 4e6 certifies N <= 2, cap 1.6e7 certifies N <= 3 with
lo(N=3) > 1e-10.  The required-cap law X_req(N) (radius model of the
Buethe term, float bisection) is printed and gated in coarse windows:
X_req(4) ~ 5e11 (SIEVE WALL: beyond any Python-minutes sieve, same
compute class as classical verification), X_req(5) ~ 3e16,
X_req(6) > 1e19 = KNOWLEDGE WALL: beyond the cited sqrt(x)-bound
range, i.e. beyond the current verified-zeros regime, independent of
compute.  dps is NOT the binding constraint anywhere: the float
ladder runs to N = 24 at dps 240 while certification dies at N = 3.
Cost law: minimal working precision for rung N measured by a frozen
dps ladder against the dps-300 reference (expected ~6.3 digits/rung).

E3 -- DECAY LAW AND DETECTION LAW (the instrument's real content)
=================================================================
Float ladder (EM Dirichlet route, corpus parity gated to the twelve
CCCXCIII floors) extended to N = 24.  Decay-law fits (frozen models):
ln lambda_min = a + b N (M1) vs a + b N + c N ln N (M2); expected
c ~ -3.3, M2 rms ~ 0.15 nats << M1 rms ~ 5.9.  CONTROL DECOMPOSITION
on the same nodes (all Herglotz, all must be PSD):
  CAUCHY   values 1 (pure node geometry; Cauchy-matrix conditioning;
           cf. Beckermann--Townsend, SIMAX 38 (2017), 1227-1248:
           displacement rank 2 forces at least exponential decay;
           the observed super-exponential N log N excess is the node
           clustering sigma_j -> 1),
  SMOOTH   RvM density log(t/2pi)/(2pi) from t0 = 2pi
           (closed form Ti_2, quad-gated),
  GAP      same density from t0 = 14 (RvM counting keeps N(t) < 1
           below ~14; model constant, no zero data),
  DISC     RvM QUANTILE ATOMS: gamma_hat_k solves
           (t/2pi)log(t/2pi) - t/2pi + 7/8 = k - 1/2, k <= 400,
           plus the exact density tail integral -- a source-only
           discrete model with NO arithmetic input (gamma_hat_1
           ~ 14.52 vs the true 14.13... which is NOWHERE used).
Frozen generic-decay decision: the ladder decay carries no
arithmetic information iff |slope(EULER) - slope(DISC)| <= 0.5
nats/step (N = 8..16) and max_{N=4..24} |log10(lambda_E/lambda_D)|
<= 1.0.  Pre-run values: slopes -15.17 vs -15.16, ratio bar 0.08.
DETECTION LAW: plant one off-line quadruple (zeros 1/2 +- delta
+- i gamma0, model heights, no zeta input) on the Euler base:
  P_delta = P + Q(.,delta,gamma0) - Q(.,0,gamma0),
  Q(s,d,g) = 2(s-d)/((s-d)^2+g^2) + 2(s+d)/((s+d)^2+g^2).
For delta > 0 the interpolant has poles in Re z > 0, so some Pick_N
must go negative: N*(delta,gamma) = first negative rung, measured on
the frozen grid delta in {0.4 ... 1e-6} at gamma0 = 14, gamma sweep
{14,20,30,50} at delta = 0.1, low-gamma frontier {2,3,5,8,10} x
{0.4,0.1}.  Frozen expected tables from the pre-run are gated
exactly.  PREDICTOR (gated |diff| <= 1): first-order Rayleigh
crossing lambda_N + v0^T DeltaM v0 / v0^T v0 < 0 on the base bottom
eigenvector -- the naive norm crossing ||DeltaM||_F is REFUTED as a
predictor (pre-run: predicts 2-5 where the truth is 6-17; recorded,
not gated).  Expected law: N* ~ 6.1 + 1.9 log10(1/delta) at
gamma = 14, and gamma-BLINDNESS: N*(0.1; 14/20/30) = 8/12/22,
gamma = 50 undetected through N = 36.

E4 -- INSTRUMENT CASE (printed, no gate)
========================================
What the certified slice buys against the classical state of the art
(RH verified for 0 < gamma <= 3e12: Platt--Trudgian, Bull. LMS 53
(2021), 792-797), what it costs, and the promotion recommendation.
No RH claim in either direction.

FROZEN NUMERICS.  Caps (1e5,4e5,1e6,4e6,1.6e7); N_CERT = 6 certified
nodes; iv.dps = 22 (prime pass) / 60 (elementary, tail, matrix
certificates); float ladder N = 24 at dps 240 vs 300; E3 at dps 340,
detection to N <= 28 (delta sweep), 36 (gamma sweep), 12 (low-gamma);
EM cutoffs 400/60 (dps <= 300) and 700/80 (dps 340); Bernoulli exact
to B_66; digamma shift/terms 32/32; quantile atoms 400; runtime bar
900 s.  Corpus anchors: pi(4e6) = 283146, psi(4e6) = 3999490.856797,
twelve CCCXCIII lambda floors, pi(1.6e7) = 1031130 (pre-run pinned).

VERDICT ENUMS (frozen):
 EULERPICK-CERTIFIED(N_max)      certified positive floors to N_max
 EULERPICK-GENERIC-DECAY         decay explained by node geometry +
                                 RvM density/gap/discreteness bars
 EULERPICK-ARITHMETIC-SIGNAL     generic bars violated
 EULERPICK-DETECTION-LAW(...)    detection gates green, law stated
 EULERPICK-LIMITED(reason)       a certified/measured wall gate fails
 INSTRUMENT-EDGE                 an instrument ward fails; exit 1.

KILL CRITERIA: source-only AST (no zeta/zetazero/siegel calls, no
data loads, no repository imports); the true first ordinate 14.13...
appears nowhere; every certified number is an outward-rounded
interval; finite N is NEVER sold as "all N"; a certified negative
would be reported as EULERPICK-NEGATIVE-CANDIDATE, not as a proof,
pending independent verification.  NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time
from fractions import Fraction

import numpy as np
from mpmath import iv, mp

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

CAPS = (100_000, 400_000, 1_000_000, 4_000_000, 16_000_000)
CAP_CORPUS = 4_000_000
CAP_BEST = 16_000_000
N_CERT = 6
IV_DPS_SUM = 22
IV_DPS_CERT = 60
C_BUETHE = "0.94"
B_PSI = "1.03883"
T_BUETHE = 10 ** 19
X_BUETHE_MIN = 11
DG_SHIFT = 32
DG_TERMS = 32
N_FLOAT = 24
DPS_FLOAT = 240
DPS_FLOAT_HI = 300
DPS_E3 = 340
EM_CUT = 400
EM_TERMS = 60
EM_CUT_HI = 700
EM_TERMS_HI = 80
N_DETECT_DELTA = 28
N_DETECT_GAMMA = 36
N_DETECT_LOW = 12
QUANTILE_ATOMS = 400
RUNTIME_BAR = 900.0
NEG_BAR = "1e-250"
TAU_FACTORS = ("0.99999999", "0.9999", "0.99", "0.9", "0.5", "0.25")
DPS_LADDER = (40, 60, 80, 100, 120, 140, 160, 180, 200, 220)
DPS_PROBE_N = (8, 12, 16, 20, 24)

CORPUS_FLOORS = (
    "4.59171357e-2", "9.0288888e-6", "6.93102462e-10", "1.10594158e-14",
    "7.91863638e-20", "2.31933623e-25", "4.18868231e-31", "4.39819276e-37",
    "3.55534552e-43", "2.02742256e-49", "8.77343259e-56", "2.43916614e-62")
CORPUS_PI_4E6 = 283146
CORPUS_PSI_4E6 = "3999490.856797"
PIN_PI_16E6 = 1031130

DELTA_GRID = ("0.4", "0.3", "0.2", "0.1", "0.05", "0.02", "0.01",
              "0.005", "0.002", "0.001", "1e-4", "1e-5", "1e-6")
NSTAR_EXPECT = (6, 7, 7, 8, 9, 10, 10, 11, 12, 12, 14, 16, 17)
GAMMA_SWEEP = ("14", "20", "30", "50")
GAMMA_NSTAR_EXPECT = (8, 12, 22, None)
LOWG_GRID = ("2", "3", "5", "8", "10")
LOWG_EXPECT = {("2", "0.4"): 2, ("2", "0.1"): 2, ("3", "0.4"): 2,
               ("3", "0.1"): 2, ("5", "0.4"): 2, ("5", "0.1"): 3,
               ("8", "0.4"): 3, ("8", "0.1"): 4, ("10", "0.4"): 4,
               ("10", "0.1"): 5}
GAMMA0 = "14"

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
    allowed_roots = {"__future__", "ast", "hashlib", "math", "os", "time",
                     "fractions", "mpmath", "numpy"}
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
    live_context = mp.__class__.__name__ == "MPContext"
    old = mp.dps
    mp.dps = 77
    live_context = live_context and mp.dps == 77
    mp.dps = old
    return (not bad) and live_context, ("violations=%s live_mp_context=%s"
                                        % (bad or "none", live_context))


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
    """Certified digamma enclosure for real interval x > 0 (spec E1c)."""
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
def tail_iv(s, X: int, EX):
    """Certified enclosure of sum_{n>X} Lambda(n) n^{-s} (spec E1b)."""
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


# ---------------------------------------------------------------- ladders
def lam_ladder(vals, sigmas, nmax: int) -> list:
    out = []
    for n in range(1, nmax + 1):
        M = mp.matrix(n, n)
        for j in range(n):
            for k in range(n):
                M[j, k] = (vals[j] + vals[k]) / (sigmas[j] + sigmas[k])
        out.append(mp.eigsy(M, eigvals_only=True)[0])
    return out


def lam_min_vec(vals, sigmas, n: int):
    M = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            M[j, k] = (vals[j] + vals[k]) / (sigmas[j] + sigmas[k])
    E, Q = mp.eigsy(M)
    lam = min(E)
    idx = list(E).index(lam)
    return lam, [Q[r, idx] for r in range(n)]


# ---------------------------------------------------------------- certificate
def certified_lambda(mid, rad, N: int):
    """Certified [lo, hi] for lambda_min over all symmetric M with
    |M - Mc| <= R entrywise.  Method: spec E1d.  Returns
    (lo_or_None, hi, rho_up, lam_float)."""
    rho = mp.mpf(0)
    for j in range(N):
        acc = iv.mpf(0)
        for k in range(N):
            acc += iv.mpf(rad[j][k])
        rho = max(rho, iv_hi(acc))
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


# ---------------------------------------------------------------- E3 models
def Qpair(s, d, g):
    return (2 * (s - d) / ((s - d) ** 2 + g ** 2)
            + 2 * (s + d) / ((s + d) ** 2 + g ** 2))


def rvm_count(t):
    return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi)) - t / (2 * mp.pi) \
        + mp.mpf(7) / 8


def density_tail_P(s, a):
    """int_a^inf 2s/(s^2+t^2) log(t/2pi)/(2pi) dt, closed form via Ti_2."""
    b1 = (mp.pi - 2 * mp.atan(a / s)) * mp.log(a / (2 * mp.pi)) / (2 * mp.pi)
    return b1 + mp.im(mp.polylog(2, mp.mpc(0, 1) * (s / a))) / mp.pi


def main() -> int:
    print("=" * 78)
    print("eulerpick_ladder_probe  PRIME.EULERPICK.CERTIFIED.LADDER.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ============================================================ E0
    section("E0. FIREWALL + INSTRUMENT SELF-TESTS")
    ok, detail = firewall_audit()
    check("G01 source-only firewall + live mp context", ok, detail)

    iv.dps = IV_DPS_CERT
    mp.dps = IV_DPS_CERT
    # planted-PSD family: diag(2,2) +- 0.1
    mid2 = [[mp.mpf(2), mp.mpf(0)], [mp.mpf(0), mp.mpf(2)]]
    rad2 = [[mp.mpf("0.1")] * 2 for _ in range(2)]
    lo, hi, rho, lam_t = certified_lambda(mid2, rad2, 2)
    check("G02 certificate self-test: PSD family floor",
          lo is not None and lo > mp.mpf("1.79") and hi >= 2,
          "diag(2)+-0.1: lo=%s hi=%s" % (fmt(lo, 6), fmt(hi, 6)))

    ones = [[mp.mpf(1), mp.mpf(1)], [mp.mpf(1), mp.mpf(1)]]
    zr = [[mp.mpf(0)] * 2 for _ in range(2)]
    lo_s, hi_s, _, lam_s = certified_lambda(ones, zr, 2)
    negm = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(-1)]]
    lo_n, hi_n, _, _ = certified_lambda(negm, zr, 2)
    check("G03 certificate self-test: singular fails, negative certified",
          lo_s is None and hi_n < 0,
          "all-ones tau-cert=%s (must be None); diag(1,-1) hi=%s < 0"
          % (lo_s, fmt(hi_n, 4)))

    mp.dps = 120
    worst_w = mp.mpf(0)
    contain = True
    for xs in ["0.75", "1.25"] + ["%d/%d" % (3 * j + 2, 4 * j)
                                  for j in range(1, N_CERT + 1)]:
        if "/" in xs:
            nu, de = xs.split("/")
            x_iv = iv.mpf(int(nu)) / iv.mpf(int(de))
            ref = mp.digamma(mp.mpf(int(nu)) / int(de))
        else:
            x_iv = iv.mpf(xs)
            ref = mp.digamma(mp.mpf(xs))
        enc = iv_digamma(x_iv)
        contain = contain and (iv_lo(enc) <= ref <= iv_hi(enc))
        worst_w = max(worst_w, iv_hi(enc) - iv_lo(enc))
    check("G04 certified digamma: containment + width",
          contain and worst_w < mp.mpf("1e-50"),
          "contains mp.digamma on 8 nodes, max width=%s" % fmt(worst_w, 3))

    # ============================================================ E1
    section("E1. CERTIFIED ENCLOSURES (sieve %d, caps %s)"
            % (CAPS[-1], list(CAPS)))
    t_sieve = time.time()
    limit = CAPS[-1]
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            bits[p * p:limit + 1:p] = b"\x00" * ((limit - p * p) // p + 1)
    primes = np.flatnonzero(
        np.frombuffer(bytes(bits), dtype=np.uint8)).astype(np.int64)
    pi_4e6 = int(np.searchsorted(primes, CAP_CORPUS, "right"))
    check("G05a sieve anchors: prime counts",
          pi_4e6 == CORPUS_PI_4E6 and len(primes) == PIN_PI_16E6,
          "pi(4e6)=%d (corpus %d), pi(1.6e7)=%d (pinned %d), sieve %.1fs"
          % (pi_4e6, CORPUS_PI_4E6, len(primes), PIN_PI_16E6,
             time.time() - t_sieve))

    iv.dps = IV_DPS_SUM
    S_IV = [iv.mpf(3 * j + 2) / iv.mpf(2 * j) for j in range(1, N_CERT + 1)]
    t_pass = time.time()
    sums = [iv.mpf(0) for _ in range(N_CERT)]
    theta = iv.mpf(0)
    snap: dict[int, tuple] = {}
    ci = 0
    for p in primes:
        p = int(p)
        while p > CAPS[ci]:
            snap[CAPS[ci]] = (theta, list(sums))
            ci += 1
        L = iv.log(iv.mpf(p))
        theta += L
        for i in range(N_CERT):
            sums[i] += L * iv.exp(-S_IV[i] * L)
    snap[CAPS[-1]] = (theta, list(sums))
    t_pass = time.time() - t_pass
    print("  interval prime pass (iv.dps=%d): %.1f s, %d primes"
          % (IV_DPS_SUM, t_pass, len(primes)))

    def powers(cap: int):
        th = iv.mpf(0)
        ss = [iv.mpf(0) for _ in range(N_CERT)]
        for p in primes:
            p = int(p)
            if p * p > cap:
                break
            L = iv.log(iv.mpf(p))
            q = p * p
            while q <= cap:
                th += L
                Lq = iv.log(iv.mpf(q))
                for i in range(N_CERT):
                    ss[i] += L * iv.exp(-S_IV[i] * Lq)
                q *= p
        return th, ss

    iv.dps = IV_DPS_CERT
    mp.dps = 120
    psi_iv: dict[int, object] = {}
    finite: dict[int, list] = {}
    ward_ok = True
    ward_lines = []
    for cap in CAPS:
        th, ss = snap[cap]
        thp, ssp = powers(cap)
        psi = th + thp
        psi_iv[cap] = psi
        finite[cap] = [ss[i] + ssp[i] for i in range(N_CERT)]
        E_abs = max(abs(iv_lo(psi) - cap), abs(iv_hi(psi) - cap))
        bu = mp.mpf(C_BUETHE) * mp.sqrt(cap)
        rs = mp.mpf(B_PSI) * cap
        this = (X_BUETHE_MIN < cap <= T_BUETHE and E_abs <= bu
                and iv_hi(psi) < rs)
        ward_ok = ward_ok and this
        ward_lines.append("X=%.0e |E|=%.4g<=%.4g" % (cap, float(E_abs),
                                                     float(bu)))
    check("G06 psi-bound applicability + own-data consistency wards",
          ward_ok, "; ".join(ward_lines))
    psi4 = psi_iv[CAP_CORPUS]
    mid4 = iv_lo(psi4) + (iv_hi(psi4) - iv_lo(psi4)) / 2
    check("G05b sieve anchor: psi(4e6) corpus value",
          abs(mid4 - mp.mpf(CORPUS_PSI_4E6)) < mp.mpf("1e-5"),
          "psi(4e6)=%s (corpus %s), width=%s"
          % (fmt(mid4, 13), CORPUS_PSI_4E6, fmt(iv_hi(psi4) - iv_lo(psi4), 3)))

    # certified P enclosures
    LOG_PI = iv.log(iv.pi)
    P_ENC: dict[tuple, object] = {}
    for cap in CAPS:
        EX = psi_iv[cap] - cap
        for j in range(1, N_CERT + 1):
            s = iv.mpf(3 * j + 2) / iv.mpf(2 * j)
            elem = 1 / s + 1 / (s - 1) - LOG_PI / 2 + iv_digamma(s / 2) / 2
            P_ENC[(cap, j)] = (elem - finite[cap][j - 1]
                               - tail_iv(s, cap, EX))

    # EM reference + stability
    mp.dps = 120
    sig120 = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, N_CERT + 1)]
    P_ref = [em_P(s, EM_CUT, EM_TERMS) for s in sig120]
    P_ref2 = [em_P(s, 512, 70) for s in sig120]
    em_dev = max(abs(a - b) for a, b in zip(P_ref, P_ref2))
    check("G07 EM reference stability (400/60 vs 512/70)",
          em_dev < mp.mpf("1e-80"), "max dev=%s" % fmt(em_dev, 3))

    contain = True
    for cap in CAPS:
        for j in range(1, N_CERT + 1):
            e = P_ENC[(cap, j)]
            contain = contain and (iv_lo(e) <= P_ref[j - 1] <= iv_hi(e))
    check("G08 EM values contained in every certified enclosure",
          contain, "%d enclosures (6 nodes x 5 caps)" % (5 * N_CERT))

    consistent = True
    for j in range(1, N_CERT + 1):
        los = [iv_lo(P_ENC[(cap, j)]) for cap in CAPS]
        his = [iv_hi(P_ENC[(cap, j)]) for cap in CAPS]
        consistent = consistent and max(los) <= min(his)
    check("G09 cross-cap enclosure consistency (pairwise intersect)",
          consistent, "all %d nodes" % N_CERT)

    print("  P(sigma_j) certified widths per cap:")
    for j in (1, 2, 3, 4):
        ws = ["%.3g" % float(iv_hi(P_ENC[(cap, j)]) - iv_lo(P_ENC[(cap, j)]))
              for cap in CAPS]
        print("    j=%d: %s" % (j, "  ".join(ws)))

    # certified floors
    mp.dps = IV_DPS_CERT
    floors: dict[tuple, tuple] = {}
    for cap in (CAP_CORPUS, CAP_BEST):
        print("  certified lambda_min intervals, cap=%d:" % cap)
        for N in range(1, N_CERT + 1):
            mid, rad = entry_mid_rad([P_ENC[(cap, j)]
                                      for j in range(1, N + 1)], N)
            lo, hi, rho, lam_t = certified_lambda(mid, rad, N)
            floors[(cap, N)] = (lo, hi, rho, lam_t)
            print("    N=%d  lo=%-14s hi=%-13s rho_up=%-10s  %s"
                  % (N, fmt(lo, 8) if lo is not None else "none",
                     fmt(hi, 8), fmt(rho, 4),
                     "CERTIFIED POSITIVE" if (lo is not None and lo > 0)
                     else "UNDECIDED AT THIS CAP"))
    ok46 = all(floors[(CAP_CORPUS, N)][0] is not None
               and floors[(CAP_CORPUS, N)][0] > 0 for N in (1, 2))
    check("G10 cap 4e6 certifies N<=2",
          ok46, "lo(2)=%s" % fmt(floors[(CAP_CORPUS, 2)][0], 8))
    lo3 = floors[(CAP_BEST, 3)][0]
    ok16 = (all(floors[(CAP_BEST, N)][0] is not None
                and floors[(CAP_BEST, N)][0] > 0 for N in (1, 2, 3))
            and lo3 > mp.mpf("1e-10"))
    check("G11 cap 1.6e7 certifies N<=3 with lo(3) > 1e-10",
          ok16, "lo(3)=%s" % fmt(lo3, 8))
    n_cert_max = 0
    for N in range(1, N_CERT + 1):
        if any(floors[(cap, N)][0] is not None and floors[(cap, N)][0] > 0
               for cap in (CAP_CORPUS, CAP_BEST)):
            n_cert_max = N

    mp.dps = 120
    in_int = True
    for cap in (CAP_CORPUS, CAP_BEST):
        lam_ref6 = lam_ladder(P_ref, sig120, N_CERT)
        for N in range(1, N_CERT + 1):
            lo, hi, _, _ = floors[(cap, N)]
            ok_lo = True if lo is None else lo <= lam_ref6[N - 1]
            in_int = in_int and ok_lo and lam_ref6[N - 1] <= hi
    check("G12 float reference floors inside certified intervals",
          in_int, "N=1..6 at both caps")

    neg_hit = [(cap, N) for cap in (CAP_CORPUS, CAP_BEST)
               for N in range(1, N_CERT + 1) if floors[(cap, N)][1] < 0]
    check("G13 falsification channel: no certified negative rung",
          not neg_hit, "certified hi<0 rungs: %s (a hit would be an"
          " RH-disproof candidate)" % (neg_hit or "none"))

    # ============================================================ E2
    section("E2. THE WALL: CAP LAW, REQUIRED CAPS, COST LAW")
    slope_ok = True
    for j in (2, 3):
        xs = [math.log(cap) for cap in CAPS]
        ys = [math.log(float(iv_hi(P_ENC[(cap, j)])
                             - iv_lo(P_ENC[(cap, j)]))) for cap in CAPS]
        n = len(xs)
        sl = ((n * sum(x * y for x, y in zip(xs, ys)) - sum(xs) * sum(ys))
              / (n * sum(x * x for x in xs) - sum(xs) ** 2))
        target = -(1 + 1 / j)
        slope_ok = slope_ok and abs(sl - target) < 0.08
        print("  width-vs-cap slope j=%d: %.4f (theory %.4f)"
              % (j, sl, target))
    check("G14 enclosure width law: slope = -(1+1/j) within 0.08",
          slope_ok, "tail-dominated Buethe scaling X^{1/2-s}")

    lam_f = [float(mp.mpf(v)) for v in CORPUS_FLOORS]
    sig_f = [1 + 1 / j for j in range(1, N_CERT + 1)]

    def rho_model(N, logX):
        w = [0.94 * (1.5 + 1 / j) / (1 + 1 / j)
             * math.exp((0.5 - (1.5 + 1 / j)) * logX)
             for j in range(1, N + 1)]
        return max(sum((w[j] + w[k]) / (sig_f[j] + sig_f[k])
                       for k in range(N)) for j in range(N))

    x_req = {}
    for N in (4, 5, 6):
        lo_l, hi_l = 6.0 * math.log(10), 30.0 * math.log(10)
        for _ in range(200):
            mid_l = (lo_l + hi_l) / 2
            if rho_model(N, mid_l) > lam_f[N - 1]:
                lo_l = mid_l
            else:
                hi_l = mid_l
        x_req[N] = mid_l / math.log(10)
        print("  X_req(N=%d) ~ 10^%.2f%s" % (N, x_req[N],
              "  > 1e19: KNOWLEDGE WALL (beyond cited sqrt-x range)"
              if x_req[N] > 19 else "  (sieve wall)"))
    check("G15 wall quantification: X_req windows",
          10 < x_req[4] < 14 and 14 < x_req[5] < 19 and x_req[6] > 19,
          "X_req(4)=10^%.2f X_req(5)=10^%.2f X_req(6)=10^%.2f"
          % (x_req[4], x_req[5], x_req[6]))

    mp.dps = DPS_FLOAT
    sigN = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, N_FLOAT + 1)]
    P240 = [em_P(s, EM_CUT, EM_TERMS) for s in sigN]
    lam240 = lam_ladder(P240, sigN, N_FLOAT)
    parity = max(abs(lam240[i] / mp.mpf(CORPUS_FLOORS[i]) - 1)
                 for i in range(12))
    check("G16 corpus parity: CCCXCIII floors N=1..12, rel < 1e-7",
          parity < mp.mpf("1e-7"), "max rel dev=%s" % fmt(parity, 3))

    mp.dps = DPS_FLOAT_HI
    sigH = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, N_FLOAT + 1)]
    PH = [em_P(s, EM_CUT, EM_TERMS) for s in sigH]
    lamH = lam_ladder(PH, sigH, N_FLOAT)
    agree = max(abs(lam240[i] / lamH[i] - 1) for i in range(N_FLOAT))
    all_pos = all(l > 0 for l in lamH)
    check("G17 float ladder N<=24: dps 240 vs 300 agree, all positive",
          agree < mp.mpf("1e-8") and all_pos,
          "max rel dev=%s lam(24)=%s" % (fmt(agree, 3), fmt(lamH[-1], 6)))
    print("  extended float ladder (dps %d):" % DPS_FLOAT_HI)
    for n in range(13, N_FLOAT + 1):
        print("    N=%2d lambda_min=%s" % (n, fmt(lamH[n - 1], 9)))

    dps_min = {}
    for n in DPS_PROBE_N:
        for dps in DPS_LADDER:
            try:
                mp.dps = dps
                sg = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, n + 1)]
                Pv = [em_P(s, EM_CUT, EM_TERMS) for s in sg]
                lam_try = lam_ladder(Pv, sg, n)[-1]
            except Exception:
                mp.dps = DPS_FLOAT_HI
                continue
            mp.dps = DPS_FLOAT_HI
            if lam_try > 0 and abs(lam_try / lamH[n - 1] - 1) \
                    < mp.mpf("1e-6"):
                dps_min[n] = dps
                break
        else:
            dps_min[n] = None
    mp.dps = DPS_FLOAT_HI
    xs = list(DPS_PROBE_N)
    ys = [dps_min[n] for n in xs]
    n_ = len(xs)
    slope_dps = ((n_ * sum(x * y for x, y in zip(xs, ys))
                  - sum(xs) * sum(ys))
                 / (n_ * sum(x * x for x in xs) - sum(xs) ** 2))
    check("G18 cost law: dps_min(N) linear, slope in [5, 8]",
          all(v is not None for v in ys) and 5 <= slope_dps <= 8,
          "dps_min=%s slope=%.2f digits/rung"
          % ({n: dps_min[n] for n in xs}, slope_dps))
    print("  timing: interval prime pass %.1f s for %d primes x %d nodes"
          % (t_pass, len(primes), N_CERT))

    # ============================================================ E3
    section("E3. DECAY LAW (controls) + DETECTION LAW (planted off-line)")
    mp.dps = DPS_E3
    sigD = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, N_DETECT_GAMMA + 1)]
    t_e3 = time.time()
    PE = [em_P(s, EM_CUT_HI, EM_TERMS_HI) for s in sigD]
    lam_e = []
    vec_e = []
    for n in range(1, N_DETECT_GAMMA + 1):
        l, v = lam_min_vec(PE, sigD, n)
        lam_e.append(l)
        vec_e.append(v)
    print("  base ladder to N=%d: %.1f s, lam(36)=%s"
          % (N_DETECT_GAMMA, time.time() - t_e3, fmt(lam_e[-1], 4)))

    # exact Cauchy determinant anchor at N=10
    n10 = 10
    fr = [Fraction(j + 1, j) for j in range(1, n10 + 1)]
    num = Fraction(1)
    for j in range(n10):
        for k in range(j):
            num *= (fr[j] - fr[k]) ** 2
    den = Fraction(1)
    for j in range(n10):
        for k in range(n10):
            den *= (fr[j] + fr[k])
    det_frac = num / den * Fraction(2) ** n10
    Mc10 = mp.matrix(n10, n10)
    for j in range(n10):
        for k in range(n10):
            Mc10[j, k] = 2 / (sigD[j] + sigD[k])
    Ec = mp.eigsy(Mc10, eigvals_only=True)
    prod = mp.mpf(1)
    for e in Ec:
        prod *= e
    det_ref = mp.mpf(det_frac.numerator) / mp.mpf(det_frac.denominator)
    det_dev = abs(prod / det_ref - 1)
    check("G19 eigensolver anchor: exact rational Cauchy det, N=10",
          det_dev < mp.mpf("1e-100"), "rel dev=%s" % fmt(det_dev, 3))

    # control closed forms gated against quadrature
    mp.dps = 40
    s3 = mp.mpf(1) + mp.mpf(1) / 3
    q_s = mp.quad(lambda t: 2 * s3 / (s3 ** 2 + t ** 2)
                  * mp.log(t / (2 * mp.pi)) / (2 * mp.pi),
                  [2 * mp.pi, mp.inf])
    q_g = mp.quad(lambda t: 2 * s3 / (s3 ** 2 + t ** 2)
                  * mp.log(t / (2 * mp.pi)) / (2 * mp.pi), [14, mp.inf])
    dev_s = abs(q_s / density_tail_P(s3, 2 * mp.pi) - 1)
    dev_g = abs(q_g / density_tail_P(s3, mp.mpf(14)) - 1)
    check("G20 control closed forms (Ti_2) vs quadrature",
          dev_s < mp.mpf("1e-30") and dev_g < mp.mpf("1e-30"),
          "smooth dev=%s gap dev=%s" % (fmt(dev_s, 3), fmt(dev_g, 3)))

    mp.dps = DPS_E3
    P_sm = [density_tail_P(s, 2 * mp.pi) for s in sigD]
    P_gp = [density_tail_P(s, mp.mpf(14)) for s in sigD]
    atoms = []
    guess = mp.mpf(14)
    for k in range(1, QUANTILE_ATOMS + 1):
        g = mp.findroot(lambda x: rvm_count(x) - (k - mp.mpf(1) / 2), guess)
        atoms.append(g)
        guess = g + 3
    TM = mp.findroot(lambda x: rvm_count(x) - QUANTILE_ATOMS, atoms[-1])
    P_dc = [mp.fsum(2 * s / (s * s + g * g) for g in atoms)
            + density_tail_P(s, TM) for s in sigD]
    print("  RvM quantile atoms: gamma_hat_1=%s (true 14.13... NOT used),"
          " T_M=%s" % (fmt(atoms[0], 8), fmt(TM, 8)))
    check("G21 quantile-atom model source check: gamma_hat_1 in (14.4,14.7)",
          mp.mpf("14.4") < atoms[0] < mp.mpf("14.7"),
          "gamma_hat_1=%s from RvM counting only" % fmt(atoms[0], 8))

    lam_c = lam_ladder([mp.mpf(1)] * N_FLOAT, sigD, N_FLOAT)
    lam_s = lam_ladder(P_sm, sigD, N_FLOAT)
    lam_g = lam_ladder(P_gp, sigD, N_FLOAT)
    lam_d = lam_ladder(P_dc, sigD, N_FLOAT)
    check("G22 Herglotz controls all PSD through N=24",
          all(l > 0 for ls in (lam_c, lam_s, lam_g, lam_d) for l in ls),
          "cauchy/smooth/gap/disc floors positive")

    def slope(ls):
        return float((mp.log(ls[15]) - mp.log(ls[7])) / 8)

    sl_c, sl_s, sl_g = slope(lam_c), slope(lam_s), slope(lam_g)
    sl_d, sl_e = slope(lam_d), slope(lam_e[:N_FLOAT])
    print("  decay slopes N=8->16 (nats/step): cauchy %.3f smooth %.3f"
          " gap %.3f disc %.3f EULER %.3f" % (sl_c, sl_s, sl_g, sl_d, sl_e))
    order_ok = sl_c > sl_s > sl_g > sl_d - 0.5
    generic_ok = abs(sl_e - sl_d) <= 0.5
    check("G23 slope decomposition order + generic bar |E-D| <= 0.5",
          order_ok and generic_ok,
          "|slope_E - slope_D|=%.3f" % abs(sl_e - sl_d))
    ratio_bar = max(abs(mp.log10(lam_e[n - 1] / lam_d[n - 1]))
                    for n in range(4, N_FLOAT + 1))
    check("G24 generic ratio bar: max |log10(lam_E/lam_D)| <= 1.0, N=4..24",
          ratio_bar <= 1, "max=%s" % fmt(ratio_bar, 3))

    Ns = list(range(2, N_FLOAT + 1))
    yv = [float(mp.log(lam_e[n - 1])) for n in Ns]

    def lstsq(cols):
        A = np.array(cols).T
        y = np.array(yv)
        coef, res = np.linalg.lstsq(A, y, rcond=None)[:2]
        rms = float(np.sqrt(res[0] / len(y))) if len(res) else 0.0
        return coef, rms

    c1, rms1 = lstsq([[float(n) for n in Ns], [1.0] * len(Ns)])
    c2, rms2 = lstsq([[n * math.log(n) for n in Ns],
                      [float(n) for n in Ns], [1.0] * len(Ns)])
    print("  fit M1 ln lam = a + bN:        b=%.3f  rms=%.3f nats"
          % (c1[0], rms1))
    print("  fit M2 ln lam = a+bN+cN ln N:  c=%.3f b=%.3f  rms=%.3f nats"
          % (c2[0], c2[1], rms2))
    check("G25 decay law: N ln N model, rms < 1 nat and < rms(M1)/5",
          rms2 < 1.0 and rms2 < rms1 / 5,
          "rms(M2)=%.3f rms(M1)=%.3f c=%.3f" % (rms2, rms1, c2[0]))

    # ---------------- detection sweeps
    g14 = mp.mpf(GAMMA0)
    neg_bar = -mp.mpf(NEG_BAR)

    def detect(dm, gm, nmax):
        Pd = [PE[j] + Qpair(sigD[j], dm, gm) - Qpair(sigD[j], 0, gm)
              for j in range(nmax)]
        nstar = None
        lneg = None
        for n in range(1, nmax + 1):
            M = mp.matrix(n, n)
            for j in range(n):
                for k in range(n):
                    M[j, k] = (Pd[j] + Pd[k]) / (sigD[j] + sigD[k])
            l = mp.eigsy(M, eigvals_only=True)[0]
            if l < neg_bar:
                nstar, lneg = n, l
                break
        return nstar, lneg

    def rayleigh_pred(dm, gm, nmax):
        for n in range(1, nmax + 1):
            v = vec_e[n - 1]
            acc = mp.mpf(0)
            den = mp.mpf(0)
            for j in range(n):
                den += v[j] ** 2
                for k in range(n):
                    djk = ((Qpair(sigD[j], dm, gm) - Qpair(sigD[j], 0, gm))
                           + (Qpair(sigD[k], dm, gm)
                              - Qpair(sigD[k], 0, gm))) \
                        / (sigD[j] + sigD[k])
                    acc += v[j] * v[k] * djk
            if lam_e[n - 1] + acc / den < 0:
                return n
        return None

    t_det = time.time()
    meas = []
    preds = []
    print("  detection sweep gamma0=%s:" % GAMMA0)
    for i, ds in enumerate(DELTA_GRID):
        dm = mp.mpf(ds)
        ns, lneg = detect(dm, g14, N_DETECT_DELTA)
        npred = rayleigh_pred(dm, g14, N_DETECT_DELTA)
        meas.append(ns)
        preds.append(npred)
        print("    delta=%-6s N*=%-4s pred=%-4s expect=%-3d lam_neg=%s"
              % (ds, ns, npred, NSTAR_EXPECT[i],
                 fmt(lneg, 3) if lneg is not None else "-"))
    sweep_ok = (all(m is not None for m in meas)
                and tuple(meas) == NSTAR_EXPECT
                and all(meas[i] >= meas[i - 1] for i in range(1, len(meas)))
                and all(abs(meas[i] - preds[i]) <= 1
                        for i in range(len(meas))))
    check("G26 delta sweep: frozen N* table, monotone, Rayleigh pred +-1",
          sweep_ok, "N*=%s" % (meas,))

    u = [math.log10(1 / float(mp.mpf(d))) for d in DELTA_GRID]
    A = np.array([u, [1.0] * len(u)]).T
    coefd, resd = np.linalg.lstsq(A, np.array([float(m) for m in meas]),
                                  rcond=None)[:2]
    rms_d = float(np.sqrt(resd[0] / len(u))) if len(resd) else 0.0
    print("  DETECTION LAW: N*(delta) = %.3f + %.3f log10(1/delta),"
          " rms=%.3f rungs" % (coefd[1], coefd[0], rms_d))
    check("G27 detection law fit: slope in [1,3], rms < 1 rung",
          1 <= coefd[0] <= 3 and rms_d < 1,
          "b=%.3f rms=%.3f" % (coefd[0], rms_d))

    gam_meas = []
    for i, gs in enumerate(GAMMA_SWEEP):
        ns, _ = detect(mp.mpf("0.1"), mp.mpf(gs), N_DETECT_GAMMA)
        gam_meas.append(ns)
        print("    gamma=%-3s delta=0.1: N*=%s (expect %s)"
              % (gs, ns, GAMMA_NSTAR_EXPECT[i]))
    check("G28 gamma blindness: frozen table incl. gamma=50 undetected<=36",
          tuple(gam_meas) == GAMMA_NSTAR_EXPECT,
          "N*(0.1;14/20/30/50)=%s" % (gam_meas,))

    low_ok = True
    for gs in LOWG_GRID:
        for ds in ("0.4", "0.1"):
            ns, _ = detect(mp.mpf(ds), mp.mpf(gs), N_DETECT_LOW)
            low_ok = low_ok and ns == LOWG_EXPECT[(gs, ds)]
            print("    low-gamma gamma=%-3s delta=%-4s N*=%s (expect %d)"
                  % (gs, ds, ns, LOWG_EXPECT[(gs, ds)]))
    check("G29 low-gamma frontier: frozen table (certified-slice reach)",
          low_ok, "N<=3 slice sees only gamma <~ 5-8 at delta <= 0.4")
    print("  detection total: %.1f s" % (time.time() - t_det))

    # ============================================================ E4
    section("E4. INSTRUMENT CASE + COMPOSITE VERDICT")
    elapsed = time.time() - T0
    print("""  WHAT THE LADDER ADDS: a source-only, certificate-typed finite
  RH-consequence check from prime data alone -- no zero computations
  at runtime; each certified rung is unconditional (Buethe/RS inputs
  cited); a certified negative rung would falsify RH via the exact
  forward direction alone.
  WHAT IT COSTS (measured): certification dies at the TAIL, not at
  precision -- N<=2 at the corpus cap 4e6, N<=3 at 1.6e7;
  X_req(4)~10^%.1f (sieve wall), X_req(6)~10^%.1f > 1e19 (knowledge
  wall: beyond the cited verified-zeros sqrt(x) range).  The float
  ladder alone reaches N=24 at dps 240 (lambda~1e-148): dps ~ %.1f
  digits/rung is NEVER the binding constraint.
  REACH VS STATE OF THE ART: the certified N<=3 slice detects a
  planted off-line pair only for gamma <~ 5-8 (delta<=0.4) -- a region
  classical verification (RH true to 3e12, Platt--Trudgian 2021)
  closed decades ago; emulating height T needs N ~ O(T) rungs (gamma
  blindness law), i.e. the instrument does NOT shortcut verification.
  DECAY VERDICT: lambda_min(N) ~ exp(-3.3 N ln N) is fully explained
  by node geometry + RvM density + gap + discreteness (quantile-atom
  control matches within a factor <~1.2): NO arithmetic information
  in the decay; the ladder's value is the CERTIFICATE, not the rate."""
          % (x_req[4], x_req[6], slope_dps))

    check("G30 runtime < %.0f s" % RUNTIME_BAR, elapsed < RUNTIME_BAR,
          "%.1f s" % elapsed)

    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    n_tot = len(CHECKS)
    instrument_edge = any(not ok for name, ok, _ in CHECKS
                          if name.startswith(("G01", "G02", "G03", "G04",
                                              "G05", "G07", "G19", "G20")))
    cert_ok = all(ok for name, ok, _ in CHECKS
                  if name.startswith(("G06", "G08", "G09", "G10", "G11",
                                      "G12", "G13")))
    generic_ok2 = all(ok for name, ok, _ in CHECKS
                      if name.startswith(("G23", "G24")))
    detect_ok = all(ok for name, ok, _ in CHECKS
                    if name.startswith(("G26", "G27", "G28", "G29")))
    parts = []
    if cert_ok:
        parts.append("EULERPICK-CERTIFIED(N_max=%d @ cap %.1e; N<=2 @ 4e6)"
                     % (n_cert_max, CAP_BEST))
    else:
        parts.append("EULERPICK-LIMITED(certification gates failed)")
    parts.append("EULERPICK-GENERIC-DECAY" if generic_ok2
                 else "EULERPICK-ARITHMETIC-SIGNAL")
    if detect_ok:
        parts.append("EULERPICK-DETECTION-LAW(N*=%.1f+%.2f log10(1/delta)"
                     " @ gamma=14; gamma-blind >~50 by N<=36)"
                     % (coefd[1], coefd[0]))
    else:
        parts.append("EULERPICK-LIMITED(detection gates failed)")
    verdict = " + ".join(parts) if not instrument_edge else "INSTRUMENT-EDGE"

    print("\n" + "=" * 78)
    print("CHECKS: %d/%d PASS" % (n_pass, n_tot))
    print("COMPOSITE VERDICT: %s" % verdict)
    print("NO RH CLAIM IN EITHER DIRECTION.  EXPLORATION ONLY.")
    print("SPEC_SHA %s   runtime %.1f s" % (SPEC_SHA[:16], elapsed))
    print("=" * 78)
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
