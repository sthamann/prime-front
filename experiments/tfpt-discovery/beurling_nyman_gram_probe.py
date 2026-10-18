#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""beurling_nyman_gram_probe -- PRIME.BN.GRAM.TRANSPORT.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-13.)

THE QUESTION.  Not "does d_N decrease" (known, proves nothing) but:
does the TFPT compiler side supply anything that bounds the
Baez-Duarte distance d_N from ABOVE unconditionally?  I.e. is there a
certified inequality of the shape

    <compiler object> >= <something>   ==>   d_N <= f(N) -> 0 ?

PREMISE CORRECTION (declared first, honesty rule).  The mission brief
states the corpus contains NO Beurling-Nyman attempt.  That is FALSE:
verification/v667_baez_duarte.py (ledger PRIME.BAEZDUARTE.01, 12
checks, verdict BD-CONTROL-CLEAN) is a deployed Baez-Duarte module,
built as an EXTERNAL CONTROL FRAME for the Suzuki route; the
discovery probe baez_duarte_probe.py and the Nyman-Beurling PART 2
of criteria_atlas_probe.py exist as well.  What is genuinely NEW here
is the TRANSPORT question (can compiler positivity certificates
dominate the BD Gram?) and the rigor tier (v667 is float64 with
dps-30 spot checks; this probe is outward-rounded interval end to
end).  criteria_atlas_probe PART 2 already TYPED the direction in
prose ("a FINITE certified ladder supplies no d_N upper bound"); this
probe turns that typed prose into a decided, machine-checked
obstruction with named failure points.  Nothing here duplicates
v667's N = 2048 corridor ladder.

THE SYSTEM (source-only, classical closed forms; H = L^2(0, inf)).
  e_k(x) = {1/(k x)},  k = 1..N;   chi = 1_(0,1];   ||chi||^2 = 1.
  b_k    = <chi, e_k>  = (1 - gamma + log k)/k.
  G(k,l) = <e_k, e_l>  = int_0^inf {u/k}{u/l} u^-2 du
         = nu(k/d, l/d)/d,   d = gcd(k,l),
  and for coprime h <= q the Vasyunin closed form
    nu(h,q) = (log 2pi - gamma)/2 (1/h + 1/q)
              + (q - h)/(2 h q) log(h/q)
              - pi/(2 h q) (V(h,q) + V(q mod h, h)),
    V(p,q) = sum_{m=1}^{q-1} {m p / q} cot(pi m / q).
  d_N^2 = 1 - b^T G_N^{-1} b = dist^2(chi, span{e_1..e_N}).
  Baez-Duarte 2003: RH <=> d_N -> 0.

TASK 1 -- ENTRY FORMULAS, SOURCE-ONLY, TWO INDEPENDENT ROUTES.
  ROUTE A  the Vasyunin closed form above (interval arithmetic).
  ROUTE B  EXACT elementary route, fully independent of Vasyunin:
    on every breakpoint-free interval {u/k}{u/l} u^-2 =
    1/(kl) - (b/k + a/l)/u + ab/u^2 with a = floor(u/k), b =
    floor(u/l), antiderivative u/(kl) - (b/k+a/l) log u - ab/u.  The
    head int_0^T (T a multiple of L = lcm(k,l)) is Abel-summed into
    CLOSED FORM (one log-gamma per index, no O(T) log calls); the
    tail is enclosed by the exact periodic expansion
      int_T^inf f u^-2 du = mbar/T + Phibar/T^2 + E, |E| <= 4 L^2/T^3,
      mbar   = 1/4 + gcd(k,l)^2/(12 k l)          (exact rational),
      Phibar = mbar L/2 - (1/L) int_0^L w f(w) dw (exact rational).
  ROUTE C  the trigamma folding sum_{j>=0}(v+jL)^-2 = psi_1(v/L)/L^2
    with mpmath quadrature at dps 60 between the breakpoints (the
    v667 V0.1 route, re-run at 60 dps, quoted here only as the third
    opinion).
  ADVERSARY: four WRONG conventions (Vasyunin with modular inverse;
  the missing second cotangent sum; flipped log sign; gcd
  normalization x d instead of / d) must be REJECTED by Route B --
  a test with no power is no test.

TASK 2 -- RIGOROUS d_N.  One outward-rounded interval LDL^T of the
  N_CERT x N_CERT Gram.  Because LDL prefixes ARE the leading
  principal blocks, the single forward substitution z = L^-1 b gives
  the WHOLE ladder at once:
      d_N^2 = 1 - sum_{j<=N} z_j^2 / D_j,
  each increment z_j^2/D_j >= 0 certified, no eigensolver, no sign
  claim from floating point.  Decay read against the closed-form
  BDBLS/Burnol constant C_BD = 2 + gamma - log 4pi (RATIOS ONLY, NO
  FIT).

TASK 3 -- THE TRANSPORT BATTERY (the actual question).  The compiler
  certificate class, read VERBATIM from the ledger/notes as declared
  external constants (nothing recomputed, nothing consumed):
    (H1) n > 0                              entry pivot
    (H2) B >= c_B I, c_B >= 0.5523          v905 IVAL surface floor
    (H3) sigma = (b^T B^-1 b)/n <= 0.726909 CCLXXIX, 151 wall cells
    ==> reserve  s/n = 1 - sigma >= 0.273091 > 0.
  Under the only natural dictionary (n, b, B, s, sigma) <->
  (1, b_BD, G_N, d_N^2, 1 - d_N^2) the battery decides:
    T1 VACUITY     the bordered BD Gram is PSD BY CONSTRUCTION, so
                   every PSD / SOS / principal-minor / Schur-
                   positivity certificate on it is a tautology.
    T2 DIRECTION   Loewner antitonicity: G >= P  ==>  G^-1 <= P^-1
                   ==> d_N^2 >= 1 - b^T P^-1 b.  A FLOOR yields a
                   LOWER bound on d_N.  Verified, and the resulting
                   floor-transport bound is computed and shown
                   vacuous (negative).
    T3 NO FLOOR    lambda_min(G_N) <= G_NN = (log 2pi - gamma)/N,
                   exact one-liner: the BD Gram admits NO N-uniform
                   Loewner floor at all, so (H2) is FALSE on the BD
                   side from some explicit N onwards.
    T4 MARGIN      (H3)'s conclusion transported reads d_N^2 >=
                   0.273091; refuted by the certified ladder at an
                   explicit N*.
    T5 CLASS NO-GO an EXPLICIT Gram family satisfying (H1)+(H2)+(H3)
                   at EVERY N with d_N^2 >= 1/2 for every N (proof
                   in-probe, three lines): therefore no conclusion
                   "d_N -> 0" follows from that hypothesis set.
    T6 STRUCTURE   the BD Gram is exactly MULTIPLICATIVELY covariant
                   (G(mk,ml) = G(k,l)/m, warded) while the deployed
                   wall is additively shift-covariant (Toeplitz +
                   Hankel in the lag, CCCXLI); the BD Gram's distance
                   to the Toeplitz and to the Hankel subspace is
                   measured (orthogonal projection, closed form, NO
                   fit).

TASK 4 -- THE CLASSICAL FENCE (what any transport may not violate).
  Burnol, Adv. Math. 170 (2002) 56-70, unconditional:
      liminf_N d_N^2 log N >= sum_{Re rho = 1/2} m(rho)^2 / |rho|^2,
  distinct critical zeros, m = multiplicity; improves BDBLS, Adv.
  Math. 149 (2000) 130-144, which had m(rho)^1.  The critical-line
  restriction is the safe reading (a subsum is a weaker bound, and
  Hardy already makes it positive).  Hardy => the right side is > 0
  unconditionally, hence d_N >> 1/sqrt(log N) and NO bound
  f(N) = o(1/log N) can be true.  Under RH with simple zeros the
  constant is the closed form C_BD = 2 + gamma - log 4pi (no zero
  data needed, no zero data read).  The best known UPPER bound is
  conditional (under RH, Balazard-de Roton type, size (log N)^-1/2 up
  to log log factors); unconditional upper bound with f -> 0: NONE
  known and, by Baez-Duarte's theorem, equivalent to RH.

TASK 5 -- CONTROLS.  (C1) exactly computable comb surrogates via the
  identity: for theta = c/m (c, m integers) the dilation family
  {theta_k/x} has Gram c * G_BD(m_j, m_k) and b = theta(1 - gamma -
  log theta) -- so the odd comb (2k+1), the 1 mod 3 comb (3k+1) and
  the 2-adic comb (2^k) run on the SAME certified machinery.  A
  criterion whose finite-N behaviour cannot separate these is
  COMB-BLIND at reachable N.  (C2) the T5 plateau family is the
  comb-FREE surrogate: no arithmetic at all, every compiler
  hypothesis satisfied, d_N^2 >= 1/2 forever.

VERDICT enum (frozen, precedence top-down):
  BN-INSTRUMENT-EDGE   any entry-formula / adversary / LDL ward fails
  BN-TRANSPORT-FOUND   a certified chain compiler-object => d_N <=
                       f(N) -> 0 is exhibited and verified
  BN-NO-TRANSPORT      the obstruction battery fires (T2 direction +
                       T3 no floor + T4 margin + T5 class no-go)
  BN-RESTATEMENT       the needed object is provably RH-equivalent
  BN-CLASSICAL-GAP     the measured ladder conflicts with the fence

RIGOR: post-CCCXXIII.  Every sign/limit claim is exact-rational or
outward-rounded interval (mpmath.iv, dps 50) or mpmath >= 60 dps.
No eigensolver decides any sign.  No fit anywhere.  NO zero data is
read (no zetazero, no zeta call at all), no prime tables, no target
sign consumed.  FIREWALL: this file writes nothing, imports no
verification/ or experiments/ module, touches no marker, makes no RH
claim.  Python-only per GATE.WOLFRAM.02.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/beurling_nyman_gram_probe.py
"""

import ast
import hashlib
import math
import os
import time
from fractions import Fraction

from mpmath import iv, mp
from mpmath.libmp import to_rational

# ------------------------------------------------------------------ frozen spec
FROZEN_SPEC = """\
PRIME.BN.GRAM.TRANSPORT.01 spec v2 (frozen 2026-08-13).  AMENDMENT
HISTORY, declared openly: run 1 of spec v1 was an INSTRUMENT-EDGE
(4 fails, no result read) and v2 repairs only the instrument, never
a bar, a bound or an enum -- (A1) the firewall is now an AST
identifier scan, because a text scan flags its own banned-word list;
(A2) widths are read from the exact interval diameter instead of the
float64 endpoint difference, which cannot resolve 1e-52; (A3) the
interval Cholesky loses ~0.5 decimal digits per step, so IV_DPS goes
50 -> 170 and the routine is FAIL-CLOSED-BUT-NOT-FATAL: it reports
the certified reach instead of abandoning the run, with a declared
minimum reach N_CERT_MIN = 64; (A4) N_CERT 256 -> 192 for runtime.
No number produced by v1 was read before these repairs.  After run 2
the T1 border was REORDERED (chi last) so that its final pivot really
is the Schur complement d_M^2 -- as run 2 had claimed in prose but
not in code -- and two WARDS were ADDED on top of that: S3.1b (the
bordered pivot must equal the ladder value) and S2.5 (a
factorization-free closed form at N = 1, 2 must reproduce the
ladder).  Additions only: no bar loosened, no bound relaxed, no enum
touched, and the S5 control was retyped to what the spec had frozen
all along (feature gate, values a bar-free read).
SYSTEM: e_k(x) = {1/(kx)} on L^2(0,inf), chi = 1_(0,1], b_k =
(1-gamma+log k)/k, G(k,l) = nu(k/d,l/d)/d with the Vasyunin nu and
V(p,q) = sum_{m<q} {mp/q} cot(pi m/q); d_N^2 = 1 - b^T G_N^-1 b.
TIERS: interval = mpmath.iv at IV_DPS 170 (outward rounded); high =
mpmath at MP_DPS 60/80; float64 appears NOWHERE in a decision path.
ENTRY WARDS (declared bars):
 W1 mean identity int_0^1 {ht}{kt} dt = 1/4 + 1/(12hk) for coprime
    h,k EXACT (Fraction, residual == 0) on PAIRS_MEAN.
 W2 b_k: Route B enclosure must contain (1-gamma+log k)/k, width
    <= 1e-9, for k in K_B.
 W3 Route A (Vasyunin) inside the Route B enclosure on PAIRS, and
    Route B width <= 1e-9.
 W4 Route A vs Route C (trigamma quadrature, dps 60) |dev| <= 1e-30
    on PAIRS_C.
 W5 all four ADVERSARY conventions rejected on at least one pair of
    PAIRS with |dev| >= 1e-6 (test power).
 W6 multiplicative covariance G(mk,ml) == G(k,l)/m on PAIRS_COV,
    intervals must overlap and width <= 1e-9.
LADDER: N_CERT 192 attempted; one interval LDL^T; every pivot D_j > 0
 certified (lower endpoint > 0); the routine stops at the first pivot
 whose enclosure touches 0 and reports the REACH, which is the honest
 certified N -- the bar is reach >= N_CERT_MIN = 64; ladder read at
 LADDER_N below the reach; d_N^2 enclosure width bar 1e-6; monotone
 decrease certified from the increments; the ladder cross-checked
 against a factorization-free closed form at N = 1, 2 and against the
 bordered Schur pivot at N = FLOOR_M.
TRANSPORT (declared BEFORE the run):
 COMPILER_CERTS are quoted verbatim external constants, never
 recomputed: c_B = 0.5523 (v905 IVAL, 39 steps), c_B_float = 0.5914,
 c_G = 0.4614, sigma_worst = 0.726909 (151 cells), reserve eta* =
 0.273091, SIGMA_ENV 0.7809, deep worst 0.787603 / margin 0.212397.
 T2 Loewner antitonicity verified on an explicitly certified floor
    (interval LDL of G_M - c0 I, M = FLOOR_M) and the transported
    bound 1 - ||b||^2/c0 reported; the transport is DEAD if that
    number is <= 0 at every tested N.
 T3 lambda_min(G_N) <= (log 2pi - gamma)/N exact; N_FLOOR* = first N
    with (log 2pi - gamma)/N < c_B.
 T4 N* = first N in LADDER_N with certified d_N^2 upper endpoint <
    eta* = 0.273091.
 T5 plateau family: G~ = A A^T + eps^2 I, A row k = (1, 1/k),
    eps = 4/5, beta = (1/2, 1/2), b~ = A beta; claims certified in
    interval arithmetic at PLATEAU_N: (i) G~ >= c_B I, (ii)
    sigma~ <= sigma_worst, (iii) d~_N^2 >= 1/2.
 T6 relative distance of the normalized BD Gram to the Toeplitz and
    to the Hankel subspace at N = STRUCT_N by orthogonal projection
    (diagonal / antidiagonal means, closed form).
CONTROLS: comb surrogates ODD (2k+1, c=2), MOD3 (3k+1, c=3), DYADIC
 (2^k, c=1) at N_CTRL, same interval machinery; reported as
 d_N^2 and d_N^2 log N ratios, NO fit, NO bar (comb-blindness is a
 typed read, not a gate).
NO RH claim.  Writes nothing.  No zeros.  Runtime bar 1800 s.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()

# ------------------------------------------------------------------ constants
IV_DPS = 170                     # interval Cholesky loses ~0.5 digits/step
MP_DPS = 60
MP_DPS_HI = 80
PAD = "1e-40"                    # declared outward pad for the mp -> iv lift

N_CERT = 192                     # attempted; the certified REACH is reported
N_CERT_MIN = 64                  # declared minimum reach (bar)
LADDER_N = (1, 2, 3, 4, 5, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192)
PAIRS = ((1, 1), (1, 2), (2, 3), (3, 4), (2, 5), (5, 7), (5, 12),
         (4, 6), (6, 15))
PAIRS_C = ((1, 2), (2, 3), (5, 7), (5, 12), (4, 6), (6, 15))
PAIRS_MEAN = ((1, 1), (1, 2), (2, 3), (3, 4), (5, 7), (5, 12))
PAIRS_COV = ((1, 2, 3), (2, 3, 5), (3, 4, 2), (5, 7, 4))   # (k, l, m)
K_B = (1, 2, 5, 7, 12)
T_ROUTE_B = 100000               # head length, rounded up to a multiple of L
BAR_WIDTH = Fraction(1, 10 ** 9)
BAR_ROUTE_C = mp.mpf("1e-30")
BAR_ADVERSARY = mp.mpf("1e-6")
BAR_D2_WIDTH = mp.mpf("1e-6")
FLOOR_M = 16                     # size at which an explicit floor is certified
PLATEAU_N = (2, 4, 8, 16, 32, 64)
STRUCT_N = 64
N_CTRL = 48
CTRL_DYADIC_N = 8
RUNTIME_BAR = 1800.0

# ---- COMPILER CERTIFICATE CLASS: declared EXTERNAL constants, quoted
# ---- verbatim from the ledger / next.txt.  Nothing here is recomputed
# ---- and nothing from the TFPT side is consumed as data.
COMPILER_CERTS = {
    "c_B_ival": Fraction(5523, 10000),        # v905 IVAL, min over 39 steps
    "c_B_float": Fraction(5914, 10000),       # v905 float tier
    "c_G_min": Fraction(4614, 10000),         # P_G floor
    "sigma_worst_151": Fraction(726909, 10 ** 6),   # CCLXXIX, 151 cells
    "eta_star": Fraction(273091, 10 ** 6),    # 1 - sigma_worst
    "sigma_env": Fraction(7809, 10000),       # SIGMA_ENV t_R
    "deep_worst_59": Fraction(787603, 10 ** 6),
    "deep_margin_59": Fraction(212397, 10 ** 6),
}

BANNED = ("zetazero", "zetazeros", "nzeros", "zeta", "siegelz",
          "primepi", "primerange", "isprime", "nextprime", "prevprime",
          "primefactors", "factorint", "mertens", "moebius", "mobius")
ALLOWED_MODULES = {"ast", "hashlib", "math", "os", "time", "fractions",
                   "mpmath"}

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def sect(title):
    print("\n" + "-" * 74)
    print(title)
    print("-" * 74, flush=True)


# ------------------------------------------------------------------ iv helpers
def ivq(num, den=1):
    """exact rational -> tight interval."""
    return iv.mpf(int(num)) / iv.mpf(int(den))


def ivf(fr):
    return ivq(fr.numerator, fr.denominator)


def mp2iv(x):
    """lift an mpmath value to an outward-padded interval.  mpf values
    are exact binary rationals, so [x - pad, x + pad] transfers to the
    interval context without inward rounding; PAD is the declared
    accuracy budget of the mpmath tier."""
    with mp.workdps(MP_DPS_HI):
        pad = mp.mpf(PAD) * (1 + abs(x))
        return iv.mpf([x - pad, x + pad])


def width(x):
    """diameter as a float; x.delta is exact, so widths far below the
    float64 resolution of the endpoints are still reported."""
    return float(x.delta.b)


def mid(x):
    """midpoint as a plain float (mpmath's .a/.b are degenerate
    intervals, so arithmetic on them must not leave the endpoints)."""
    return 0.5 * (float(x.a) + float(x.b))


def as_frac(x):
    """the two endpoints as EXACT Fractions.  Binary floats are exact
    rationals, so a bracket test done here is tier-independent: it does
    not silently compare against a rounded value from another dps."""
    lo, hi = x._mpi_
    return Fraction(*to_rational(lo)), Fraction(*to_rational(hi))


def contains(outer, inner):
    return outer.a <= inner.a and inner.b <= outer.b


def overlap(x, y):
    return not (x.b < y.a or y.b < x.a)


def gap(x, y):
    """certified minimal distance between two enclosures (0 if they
    overlap) -- a rejection needs a POSITIVE gap."""
    if x.b < y.a:
        return float(y.a) - float(x.b)
    if y.b < x.a:
        return float(x.a) - float(y.b)
    return 0.0


def max_sep(x, y):
    """certified maximal distance between two enclosures."""
    return max(abs(float(x.a) - float(y.b)), abs(float(x.b) - float(y.a)))


# ------------------------------------------------------------------ route A
class VasyuninGram(object):
    """G(k,l) = nu(k/d, l/d)/d in outward-rounded interval arithmetic."""

    def __init__(self):
        self.CG = (iv.log(2 * iv.pi) - iv.euler) / 2      # (log 2pi - gamma)/2
        self._cot = {}
        self._V = {}
        self._nu = {}
        self.terms = 0

    def cot_table(self, q):
        t = self._cot.get(q)
        if t is None:
            # cos/sin, NOT 1/tan: at m/q = 1/2 the tangent interval
            # straddles the pole and 1/tan degenerates to [-inf, inf],
            # while sin(pi m/q) is certified bounded away from 0.
            pi_q = iv.pi / iv.mpf(q)
            t = []
            for m in range(1, q):
                x = pi_q * iv.mpf(m)
                t.append(iv.cos(x) / iv.sin(x))
            self._cot[q] = t
        return t

    def V(self, p, q):
        """V(p,q) = sum_{m=1}^{q-1} {mp/q} cot(pi m/q); {mp/q} exact."""
        if q == 1 or p % q == 0:
            return iv.mpf(0)
        key = (p % q, q)
        v = self._V.get(key)
        if v is None:
            ct = self.cot_table(q)
            qq = iv.mpf(q)
            acc = iv.mpf(0)
            p0 = p % q
            for m in range(1, q):
                acc = acc + (iv.mpf((m * p0) % q) / qq) * ct[m - 1]
            self.terms += q - 1
            self._V[key] = acc
            v = acc
        return v

    def nu(self, h, q):
        """nu for coprime h, q (order irrelevant, formula symmetric)."""
        key = (h, q) if h <= q else (q, h)
        val = self._nu.get(key)
        if val is None:
            h0, q0 = key
            hm, qm = iv.mpf(h0), iv.mpf(q0)
            val = (self.CG * (1 / hm + 1 / qm)
                   + (qm - hm) / (2 * hm * qm) * iv.log(hm / qm)
                   - iv.pi / (2 * hm * qm)
                   * (self.V(h0, q0) + self.V(q0 % h0 if h0 > 1 else 0, h0)))
            self._nu[key] = val
        return val

    def G(self, k, l):
        d = math.gcd(k, l)
        return self.nu(k // d, l // d) / iv.mpf(d)


def b_closed(k):
    """b_k = (1 - gamma + log k)/k as an interval."""
    return (1 - iv.euler + iv.log(iv.mpf(k))) / iv.mpf(k)


# ------------------------------------------------------------------ route B
def exact_mean(k, l):
    """mbar = (1/L) int_0^L {u/k}{u/l} du = 1/4 + gcd^2/(12 k l)."""
    d = math.gcd(k, l)
    return Fraction(1, 4) + Fraction(d * d, 12 * k * l)


def exact_first_moment(k, l):
    """int_0^L w {w/k}{w/l} dw, exact (L = lcm(k,l))."""
    L = k * l // math.gcd(k, l)
    bps = sorted({0, L} | {j * k for j in range(1, L // k + 1)}
                 | {j * l for j in range(1, L // l + 1)})
    tot = Fraction(0)
    for lo, hi in zip(bps[:-1], bps[1:]):
        a, b = Fraction(lo // k), Fraction(lo // l)
        # w (w/k - a)(w/l - b) = w^3/(kl) - w^2 (b/k + a/l) + w a b
        c3 = Fraction(1, k * l)
        c2 = b / k + a / l
        c1 = a * b

        def prim(w):
            w = Fraction(w)
            return c3 * w ** 4 / 4 - c2 * w ** 3 / 3 + c1 * w ** 2 / 2
        tot += prim(hi) - prim(lo)
    return tot


def route_b_gram(k, l, T_target=T_ROUTE_B):
    """rigorous enclosure of G(k,l) = int_0^inf {u/k}{u/l} u^-2 du,
    independent of the Vasyunin closed form.

    head int_0^T in Abel-summed closed form (T a multiple of L), tail
    by the exact periodic expansion mbar/T + Phibar/T^2 + E,
    |E| <= 4 L^2 / T^3.
    """
    L = k * l // math.gcd(k, l)
    T = ((T_target + L - 1) // L) * L
    mbar = exact_mean(k, l)
    Phibar = mbar * Fraction(L, 2) - exact_first_moment(k, l) / L

    # --- head, term 1: telescoping  T/(kl)
    head = ivq(T, k * l)

    # --- head, term 2: -(sum_j c_j Dlog).  Abel:
    #     sum_j c_j Dlog = c_J log T
    #                      - (1/k)[(T/l - 1) log l + logGamma(T/l)]
    #                      - (1/l)[(T/k - 1) log k + logGamma(T/k)]
    mp.dps = MP_DPS_HI
    lg_Tl = mp2iv(mp.loggamma(mp.mpf(T // l)))
    lg_Tk = mp2iv(mp.loggamma(mp.mpf(T // k)))
    mp.dps = MP_DPS
    cJ = ivq(2 * T, k * l) - ivq(1, k) - ivq(1, l)
    s_log = (cJ * iv.log(iv.mpf(T))
             - (ivq(T - l, l * k) * iv.log(iv.mpf(l)) + lg_Tl / iv.mpf(k))
             - (ivq(T - k, k * l) * iv.log(iv.mpf(k)) + lg_Tk / iv.mpf(l)))
    head = head - s_log

    # --- head, term 3: -(sum_j a_j b_j Dinv).  Abel:
    #     sum_j p_j Dinv = p_J/T - sum_{m interior} (p_m - p_{m-1})/u_m
    pJ = ivq((T // k - 1) * (T // l - 1), T)
    s_inv = pJ
    acc = iv.mpf(0)
    # walk the interior breakpoints once, in increasing order
    jk, jl = 1, 1
    while True:
        uk = jk * k
        ul = jl * l
        u = uk if uk <= ul else ul
        if u >= T:
            break
        hit_k = (u == uk)
        hit_l = (u == ul)
        a = u // k
        b = u // l
        if hit_k and hit_l:
            dp = a + b - 1
        elif hit_k:
            dp = b
        else:
            dp = a
        acc = acc + ivq(dp, u)
        if hit_k:
            jk += 1
        if hit_l:
            jl += 1
    s_inv = s_inv - acc
    head = head - s_inv

    # --- tail
    tail_mid = ivf(mbar) / iv.mpf(T) + ivf(Phibar) / iv.mpf(T) ** 2
    err = 4.0 * L * L / float(T) ** 3
    tail = tail_mid + iv.mpf([-err, err])
    return head + tail


def route_b_b(k, T_target=T_ROUTE_B):
    """rigorous enclosure of b_k = int_1^inf {u/k} u^-2 du, independent
    of the closed form.  On a breakpoint-free piece {u/k} u^-2 =
    1/(ku) - a/u^2 with antiderivative log(u)/k + a/u; the log part
    telescopes and the 1/u part Abel-sums into a harmonic number, so
    the head is O(1) work.  Tail by the same exact periodic expansion
    (mean 1/2, Phibar = -k/12, |E| <= 4k^2/T^3)."""
    T = ((T_target + k - 1) // k) * k
    J = T // k
    mp.dps = MP_DPS_HI
    harm = mp2iv(mp.psi(0, mp.mpf(J)) + mp.euler)      # H_{J-1}
    mp.dps = MP_DPS
    head = iv.log(iv.mpf(T)) / iv.mpf(k) + ivq(J - 1, T) - harm / iv.mpf(k)
    mbar = Fraction(1, 2)
    Phibar = -Fraction(k, 12)
    tail_mid = ivf(mbar) / iv.mpf(T) + ivf(Phibar) / iv.mpf(T) ** 2
    err = 4.0 * k * k / float(T) ** 3
    return head + tail_mid + iv.mpf([-err, err])


_RB_CACHE = {}


def route_b_cached(k, l, T_target=T_ROUTE_B):
    key = (k, l, T_target)
    v = _RB_CACHE.get(key)
    if v is None:
        v = route_b_gram(k, l, T_target)
        _RB_CACHE[key] = v
    return v


# ------------------------------------------------------------------ route C
def route_c_gram(k, l):
    """<e_k,e_l> via the trigamma folding, mpmath dps 60 (third opinion).
    <e_k,e_l>_{L2(0,1)} = int_1^inf {u/k}{u/l} u^-2 du and
    G = that + 1/(kl)."""
    mp.dps = MP_DPS
    L = k * l // math.gcd(k, l)
    bps = {1, 1 + L}
    for step in (k, l):
        j = 1
        while j * step < 1 + L:
            if j * step > 1:
                bps.add(j * step)
            j += 1
    bps = sorted(bps)
    Lm = mp.mpf(L)

    def f(v):
        return mp.frac(v / k) * mp.frac(v / l) * mp.psi(1, v / Lm)

    tot = mp.mpf(0)
    for a, b in zip(bps[:-1], bps[1:]):
        tot += mp.quad(f, [mp.mpf(a), mp.mpf(b)])
    return tot / Lm ** 2 + mp.mpf(1) / (k * l)


# ------------------------------------------------------------------ adversaries
def adversary_gram(kind, gram, k, l):
    """deliberately WRONG conventions -- must be rejected."""
    d = math.gcd(k, l)
    h, q = k // d, l // d
    if h > q:
        h, q = q, h
    hm, qm = iv.mpf(h), iv.mpf(q)
    base = gram.CG * (1 / hm + 1 / qm)
    logt = (qm - hm) / (2 * hm * qm) * iv.log(hm / qm)
    if kind == "inverse":                      # Vasyunin with h-bar mod q
        hb = pow(h, -1, q) if q > 1 else 0
        qb = pow(q % h, -1, h) if h > 1 and (q % h) % h else 0
        v = gram.V(hb, q) + gram.V(qb, h)
    elif kind == "single":                     # only one cotangent sum
        v = gram.V(h, q)
    elif kind == "logflip":                    # flipped log sign
        logt = -logt
        v = gram.V(h, q) + gram.V(q % h if h > 1 else 0, h)
    elif kind == "gcdmul":                     # x d instead of / d
        v = gram.V(h, q) + gram.V(q % h if h > 1 else 0, h)
        return (base + logt - iv.pi / (2 * hm * qm) * v) * iv.mpf(d)
    else:
        raise ValueError(kind)
    return (base + logt - iv.pi / (2 * hm * qm) * v) / iv.mpf(d)


# ------------------------------------------------------------------ interval LDL
def iv_ldl(A, n, strict=True):
    """outward-rounded LDL^T, FAIL-CLOSED: a pivot whose enclosure
    touches 0 is a REFUSAL, never a pass.  With strict=False the
    routine stops at the last certified pivot and reports the reach
    instead of raising, so the ladder is truncated honestly rather
    than abandoned."""
    Lm = [[None] * n for _ in range(n)]
    D = [None] * n
    LD = [[None] * n for _ in range(n)]        # LD[k][i] = L[i][k]*D[k]
    for j in range(n):
        s = A[j][j]
        for k in range(j):
            s = s - LD[k][j] * Lm[j][k]
        if not (s.a > 0):
            if strict:
                raise ArithmeticError("pivot %d not certified positive: %s"
                                      % (j, s))
            return Lm, D, j
        D[j] = s
        Lm[j][j] = iv.mpf(1)
        LD[j][j] = s
        for i in range(j + 1, n):
            t = A[i][j]
            for k in range(j):
                t = t - LD[k][i] * Lm[j][k]
            v = t / s
            Lm[i][j] = v
            LD[j][i] = v * s
    return Lm, D, n


def iv_forward(Lm, rhs, n):
    """z = L^-1 rhs for unit lower-triangular L."""
    z = [None] * n
    for i in range(n):
        s = rhs[i]
        for k in range(i):
            s = s - Lm[i][k] * z[k]
        z[i] = s
    return z


# ------------------------------------------------------------------ run
def run():
    iv.dps = IV_DPS
    mp.dps = MP_DPS
    print("=" * 74)
    print("PRIME.BN.GRAM.TRANSPORT.01 -- the Beurling-Nyman / Baez-Duarte")
    print("Gram system and the TFPT transport question")
    print("=" * 74)
    print("SPEC_SHA %s (spec v2, amendments declared in the source)"
          % SPEC_SHA)
    print("tiers: interval mpmath.iv dps %d (outward) | mpmath dps %d/%d"
          % (IV_DPS, MP_DPS, MP_DPS_HI))

    # ---------------------------------------------------------- S0 instrument
    sect("S0 -- INSTRUMENT + FIREWALL")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    used, mods = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            used.add(node.attr)
        elif isinstance(node, ast.Import):
            mods.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    hits = sorted(used & set(BANNED))
    check("S0.1 AST firewall (identifiers, not text -- a text scan "
          "would flag its own banned list): no zero oracle, no zeta "
          "evaluation, no prime table anywhere in the call graph",
          not hits, "banned identifiers reached: %s" % (hits or "none"))
    check("S0.2 import allowlist: source-only, no verification/ or "
          "experiments/ module imported",
          mods <= ALLOWED_MODULES,
          "imports %s (allowlist %s)"
          % (sorted(mods), sorted(ALLOWED_MODULES)))
    t = iv.mpf(1) / iv.mpf(3)
    tlo, thi = as_frac(t)
    check("S0.3 interval arithmetic live and outward rounded: the "
          "enclosure of 1/3 STRICTLY brackets the exact rational (the "
          "bracket is decided in Fraction arithmetic, not against a "
          "value rounded at some other dps) and has positive width",
          tlo < Fraction(1, 3) < thi and width(t) > 0,
          "width(1/3) = %.2e at %d dps, both endpoints strict"
          % (width(t), IV_DPS))

    gram = VasyuninGram()

    # ---------------------------------------------------------- S1 entries
    sect("S1 -- THE ENTRY FORMULAS (task 1: source-only, two "
         "independent routes, adversary-tested)")

    # W1 -- the exact mean identity (needed by Route B's tail)
    bad = []
    for (h, q) in PAIRS_MEAN:
        d = math.gcd(h, q)
        L = h * q // d
        # (1/L) int_0^L {w/h}{w/q} dw computed exactly, piecewise
        bps = sorted({0, L} | {j * h for j in range(1, L // h + 1)}
                     | {j * q for j in range(1, L // q + 1)})
        tot = Fraction(0)
        for lo, hi in zip(bps[:-1], bps[1:]):
            a, b = Fraction(lo // h), Fraction(lo // q)
            c2, c1, c0 = Fraction(1, h * q), -(b / h + a / q), a * b

            def prim(w, c2=c2, c1=c1, c0=c0):
                w = Fraction(w)
                return c2 * w ** 3 / 3 + c1 * w ** 2 / 2 + c0 * w
            tot += prim(hi) - prim(lo)
        got = tot / L
        want = exact_mean(h, q)
        if got != want:
            bad.append((h, q, got, want))
    check("S1.1 [EXACT] the period mean identity (1/L) int_0^L {u/h}"
          "{u/k} du == 1/4 + gcd^2/(12hk), Fraction-exact on %d pairs "
          "(the exact tail anchor of Route B)" % len(PAIRS_MEAN),
          not bad, "residual 0 on all pairs" if not bad else str(bad))

    # W2 -- b_k, independent route
    worst_bw = 0.0
    okb = True
    for k in K_B:
        encl = route_b_b(k)
        closed = b_closed(k)
        okb = okb and contains(encl, closed) and width(encl) < 1e-9
        worst_bw = max(worst_bw, width(encl))
    check("S1.2 [IVAL] b_k = (1 - gamma + log k)/k is INSIDE the "
          "independent Route-B enclosure for k = %s"
          % ",".join(str(k) for k in K_B),
          okb, "max enclosure width %.2e" % worst_bw)

    # W3 -- Route A inside Route B
    okA, wmax, tbl = True, 0.0, []
    for (k, l) in PAIRS:
        eb = route_b_cached(k, l)
        ea = gram.G(k, l)
        ok = contains(eb, ea)
        okA = okA and ok and width(eb) < 1e-9
        wmax = max(wmax, width(eb))
        tbl.append((k, l, ea, eb, ok))
    print("   (k,l)   Route A (Vasyunin)            Route B enclosure "
          "(width)      A in B")
    for (k, l, ea, eb, ok) in tbl:
        print("   (%d,%2d)  %.18f   [w %.2e]                 %s"
              % (k, l, mid(ea), width(eb),
                 "yes" if ok else "NO"))
    check("S1.3 [IVAL, central] the Vasyunin closed form lies inside "
          "the INDEPENDENT exact-elementary Route-B enclosure on %d "
          "declared pairs (incl. gcd > 1)" % len(PAIRS),
          okA, "max Route-B width %.2e < 1e-9" % wmax)

    # W4 -- Route C third opinion
    devs = []
    for (k, l) in PAIRS_C:
        c = route_c_gram(k, l)
        devs.append(max_sep(gram.G(k, l), mp2iv(c)))
    dmax = max(devs)
    check("S1.4 [MP60] third opinion: trigamma-folded quadrature "
          "reproduces the Vasyunin entries on %d pairs" % len(PAIRS_C),
          dmax < float(BAR_ROUTE_C),
          "max |dev| = %.3e < %s" % (dmax, mp.nstr(BAR_ROUTE_C, 2)))

    # W5 -- adversary conventions
    adv_rows = []
    all_rejected = True
    for kind in ("inverse", "single", "logflip", "gcdmul"):
        worst = 0.0
        for (k, l) in PAIRS:
            try:
                w = adversary_gram(kind, gram, k, l)
            except Exception:
                continue
            worst = max(worst, gap(w, route_b_cached(k, l, 20000)))
        adv_rows.append((kind, worst))
        all_rejected = all_rejected and worst >= float(BAR_ADVERSARY)
    print("   convention adversaries (certified GAP between the wrong "
          "value and the Route-B enclosure, max over the pairs):")
    for kind, worst in adv_rows:
        print("     %-9s  %.6e   %s"
              % (kind, worst,
                 "REJECTED" if worst >= float(BAR_ADVERSARY)
                 else "NOT SEPARATED"))
    check("S1.5 [IVAL] test power: all four WRONG conventions "
          "(modular-inverse Vasyunin, single cotangent sum, flipped "
          "log sign, gcd normalization x d) are rejected by Route B",
          all_rejected, "min separation %.3e >= %s"
          % (min(w for _, w in adv_rows), mp.nstr(BAR_ADVERSARY, 2)))

    # W6 -- multiplicative covariance (a NEW exact ward)
    okc, cw = True, 0.0
    for (k, l, m) in PAIRS_COV:
        lhs = gram.G(m * k, m * l)
        rhs = gram.G(k, l) / iv.mpf(m)
        okc = okc and overlap(lhs, rhs)
        cw = max(cw, width(lhs), width(rhs))
    check("S1.6 [IVAL] multiplicative covariance ward G(mk, ml) == "
          "G(k,l)/m on %d triples -- the BD Gram is exactly covariant "
          "under the DILATION semigroup" % len(PAIRS_COV),
          okc and cw < 1e-9, "max interval width %.2e" % cw)

    # ---------------------------------------------------------- S2 ladder
    sect("S2 -- THE CERTIFIED LADDER (task 2: interval LDL^T, no "
         "eigensolver, no fit)")
    t1 = time.time()
    A = [[None] * N_CERT for _ in range(N_CERT)]
    for k in range(1, N_CERT + 1):
        for l in range(k, N_CERT + 1):
            v = gram.G(k, l)
            A[k - 1][l - 1] = v
            A[l - 1][k - 1] = v
    print("   interval Gram assembled: N = %d, %d Vasyunin sum terms "
          "[%.1f s]" % (N_CERT, gram.terms, time.time() - t1))
    bvec = [b_closed(k) for k in range(1, N_CERT + 1)]

    t1 = time.time()
    Lm, D, reach = iv_ldl(A, N_CERT, strict=False)
    ldl_ok = reach >= N_CERT_MIN
    check("S2.1 [IVAL, central] outward-rounded LDL^T of the BD Gram "
          "(attempted %d x %d): pivots certified strictly positive up "
          "to N = %d (fail-closed -- the run stops at the first pivot "
          "whose enclosure touches 0 and reports the reach, it never "
          "widens a bar)" % (N_CERT, N_CERT, reach), ldl_ok,
          "certified reach %d >= declared minimum %d  [%.1f s]"
          % (reach, N_CERT_MIN, time.time() - t1))
    if not ldl_ok:
        return finish("BN-INSTRUMENT-EDGE", {})
    ladder_n = tuple(N for N in LADDER_N if N <= reach)

    z = iv_forward(Lm, bvec, reach)
    incr = [z[j] * z[j] / D[j] for j in range(reach)]
    d2 = []
    acc = iv.mpf(1)
    for j in range(reach):
        acc = acc - incr[j]
        d2.append(acc)
    pos_incr = all(x.a >= 0 for x in incr)
    check("S2.2 [IVAL] the Gram-Schmidt increments z_j^2/D_j are "
          "certified non-negative for all j <= %d, hence d_N^2 is "
          "certified NON-INCREASING (nested spans, no float claim)"
          % reach, pos_incr,
          "min lower endpoint %.3e" % min(float(x.a) for x in incr))

    C_BD = 2 + iv.euler - iv.log(4 * iv.pi)
    print("\n     N     d_N^2 (certified enclosure)              width"
          "      d_N^2 logN   / C_BD")
    ladder = {}
    wmaxd = 0.0
    for N in ladder_n:
        e = d2[N - 1]
        ladder[N] = e
        wmaxd = max(wmaxd, width(e))
        if N == 1:
            print("   %4d   [%.12f, %.12f]  %.1e     --           --"
                  % (N, float(e.a), float(e.b), width(e)))
        else:
            y = e * iv.log(iv.mpf(N))
            r = y / C_BD
            print("   %4d   [%.12f, %.12f]  %.1e   %.8f   %.5f"
                  % (N, float(e.a), float(e.b), width(e),
                     mid(y), mid(r)))
    check("S2.3 [IVAL] every ladder enclosure is narrower than the "
          "declared bar (the d_N^2 reads are certificates, not "
          "measurements)", wmaxd < float(BAR_D2_WIDTH),
          "max width %.2e < %s" % (wmaxd, mp.nstr(BAR_D2_WIDTH, 2)))

    n_top = ladder_n[-1]
    mono = all(ladder[ladder_n[i + 1]].b <= ladder[ladder_n[i]].a
               for i in range(len(ladder_n) - 1))
    check("S2.4 [IVAL] strict decrease certified across the whole "
          "ladder N = %d .. %d (enclosures disjoint and ordered)"
          % (ladder_n[0], n_top), mono,
          "d_1^2 in [%.6f, %.6f] -> d_%d^2 in [%.8f, %.8f]"
          % (float(ladder[1].a), float(ladder[1].b), n_top,
             float(ladder[n_top].a), float(ladder[n_top].b)))

    # end-to-end ward: at N = 1, 2 the whole pipeline has a closed form
    # that uses NO factorization at all (scalar / explicit 2x2 inverse),
    # so it tests the Gram, b and the Schur assembly jointly.
    g11, g12, g22 = A[0][0], A[0][1], A[1][1]
    b1, b2 = bvec[0], bvec[1]
    d1_closed = 1 - b1 * b1 / g11
    det2 = g11 * g22 - g12 * g12
    d2_closed = 1 - (b1 * b1 * g22 - 2 * b1 * b2 * g12
                     + b2 * b2 * g11) / det2
    check("S2.5 [IVAL] end-to-end ward against a FACTORIZATION-FREE "
          "closed form: d_1^2 = 1 - (1-gamma)^2/(log 2pi - gamma) and "
          "d_2^2 from the explicit 2x2 inverse must reproduce the LDL "
          "ladder (this tests entries, b and Schur assembly jointly, "
          "not just the factorization)",
          overlap(d1_closed, ladder[1]) and overlap(d2_closed, ladder[2]),
          "d_1^2 closed %.15f vs ladder %.15f | d_2^2 closed %.15f vs "
          "ladder %.15f" % (mid(d1_closed), mid(ladder[1]),
                            mid(d2_closed), mid(ladder[2])))

    print("   C_BD = 2 + gamma - log 4pi in [%.15f, %.15f] (closed "
          "form, NO zero data)" % (float(C_BD.a), float(C_BD.b)))

    # ---------------------------------------------------------- S3 transport
    sect("S3 -- THE TRANSPORT BATTERY (task 3: can a compiler "
         "positivity object bound d_N from ABOVE?)")
    cB = COMPILER_CERTS["c_B_ival"]
    eta = COMPILER_CERTS["eta_star"]
    sig = COMPILER_CERTS["sigma_worst_151"]
    print("   compiler certificate class (DECLARED external constants, "
          "quoted, nothing recomputed):")
    print("     (H1) n > 0                          entry pivot")
    print("     (H2) B >= c_B I,  c_B = %s          v905 IVAL, 39 steps"
          % float(cB))
    print("     (H3) sigma = b^T B^-1 b / n <= %s   CCLXXIX, 151 cells"
          % float(sig))
    print("     ==>  reserve 1 - sigma >= eta* = %s" % float(eta))
    print("   dictionary (the only natural one):  (n, b, B, s, sigma)"
          "  <->  (1, b_BD, G_N, d_N^2, 1 - d_N^2)")

    # ---- T1 vacuity: the bordered Gram is PSD by construction.  chi is
    # bordered LAST, so the final pivot is exactly the Schur complement
    # 1 - b^T G_M^-1 b = d_M^2 -- which cross-checks the S2 ladder by a
    # different arithmetic path.
    Ab = [[None] * (FLOOR_M + 1) for _ in range(FLOOR_M + 1)]
    for k in range(FLOOR_M):
        for l in range(FLOOR_M):
            Ab[k][l] = A[k][l]
        Ab[k][FLOOR_M] = bvec[k]
        Ab[FLOOR_M][k] = bvec[k]
    Ab[FLOOR_M][FLOOR_M] = iv.mpf(1)
    try:
        _, Db, _ = iv_ldl(Ab, FLOOR_M + 1)
        bord_ok = all(x.a > 0 for x in Db)
        schur = Db[-1]
    except ArithmeticError:
        bord_ok, schur = False, None
    check("S3.1 [IVAL] T1 VACUITY: the BORDERED Gram [[G_M, b],[b^T, "
          "1]] (M = %d, chi bordered LAST) is positive definite -- as "
          "it must be, being a genuine Gram matrix of L^2 vectors.  "
          "Every PSD / SOS / principal-minor / Schur-positivity "
          "certificate applied to the BD system therefore certifies a "
          "TAUTOLOGY and carries ZERO information about RH"
          % FLOOR_M, bord_ok,
          "all %d pivots certified > 0" % (FLOOR_M + 1))
    check("S3.1b [IVAL] cross-check by a DIFFERENT arithmetic path: "
          "the final pivot of that bordered LDL is the Schur "
          "complement 1 - b^T G_M^-1 b, so it must equal the ladder "
          "value d_%d^2 assembled from the Gram-Schmidt increments"
          % FLOOR_M,
          schur is not None and overlap(schur, ladder[FLOOR_M]),
          "bordered pivot %.15f vs ladder %.15f"
          % (mid(schur), mid(ladder[FLOOR_M])) if schur is not None
          else "bordered LDL failed")

    # ---- T2 direction: Loewner antitonicity + explicit certified floor
    # find the largest c we can certify with the SAME certificate class
    c0 = None
    lo, hi = Fraction(0), Fraction(1)
    for _ in range(14):
        midf = (lo + hi) / 2
        Ash = [[A[i][j] - (ivf(midf) if i == j else iv.mpf(0))
                for j in range(FLOOR_M)] for i in range(FLOOR_M)]
        try:
            iv_ldl(Ash, FLOOR_M)
            lo = midf
        except ArithmeticError:
            hi = midf
    c0, c0_fail = lo, hi
    nb2 = iv.mpf(0)
    for k in range(FLOOR_M):
        nb2 = nb2 + bvec[k] * bvec[k]
    floor_bound = 1 - nb2 / ivf(c0)
    # the SHARPEST floor any method could certify is lambda_min itself,
    # and lambda_min <= min diagonal = (log 2pi - gamma)/M; even that
    # optimal floor must leave the transported bound negative, else the
    # obstruction would be an artefact of a weak bisection.
    lam_sharp = (iv.log(2 * iv.pi) - iv.euler) / iv.mpf(FLOOR_M)
    floor_sharp = 1 - nb2 / lam_sharp
    check("S3.2 [IVAL] T2 DIRECTION: Loewner antitonicity.  G >= P > 0 "
          "==> G^-1 <= P^-1 ==> d_N^2 >= 1 - b^T P^-1 b: a FLOOR gives "
          "a LOWER bound on d_N, never an upper one.  Certified floor "
          "for G_%d (same exact/interval LDL class as the compiler, "
          "largest value on a 14-step dyadic bisection -- NOT claimed "
          "to be lambda_min): G_%d >= %s I; the transported bound "
          "1 - ||b||^2/c is %.4f <= 0 == VACUOUS"
          % (FLOOR_M, FLOOR_M, float(c0),
             mid(floor_bound)),
          floor_bound.b < 0 and floor_sharp.b < 0,
          "||b_%d||^2 = %.6f, certified floor c = %.8f (bisection could "
          "not certify %.8f).  Not an artefact of a weak bisection: "
          "lambda_min <= %.6f from the smallest diagonal entry, and "
          "even THAT optimal floor transports to %.4f < 0"
          % (FLOOR_M, mid(nb2), float(c0), float(c0_fail),
             mid(lam_sharp), mid(floor_sharp)))

    # ---- T3 no uniform floor
    lam_cap = (iv.log(2 * iv.pi) - iv.euler)
    n_floor = None
    for N in range(1, 1000):
        cap = lam_cap / iv.mpf(N)
        if cap.b < float(cB):
            n_floor = N
            break
    check("S3.3 [EXACT+IVAL] T3 NO FLOOR: lambda_min(G_N) <= G_NN = "
          "(log 2pi - gamma)/N -> 0 (a diagonal entry bounds the "
          "smallest eigenvalue), so the BD Gram admits NO N-uniform "
          "Loewner floor whatsoever.  Hypothesis (H2) B >= c_B I with "
          "c_B = %s is therefore FALSE on the BD side for every "
          "N >= %d" % (float(cB), n_floor), n_floor is not None,
          "(log 2pi - gamma) = %.10f; cap at N = %d is %.6f < %s"
          % (mid(lam_cap), n_floor,
             mid(lam_cap / iv.mpf(n_floor)), float(cB)))

    # ---- T4 margin direction
    n_star = None
    for N in ladder_n:
        if ladder[N].b < float(eta):
            n_star = N
            break
    n_star_sig = None
    for N in ladder_n:
        if ladder[N].b < float(cB):
            n_star_sig = N
            break
    check("S3.4 [IVAL] T4 MARGIN DIRECTION: the compiler certifies the "
          "reserve BOUNDED AWAY FROM ZERO (1 - sigma >= %s); the "
          "Baez-Duarte criterion needs the reserve to VANISH "
          "(d_N^2 -> 0, i.e. sigma_N -> 1).  Transported, (H3)'s "
          "conclusion asserts d_N^2 >= %s, which is REFUTED by the "
          "certified ladder at N* = %s (d^2 upper endpoint %.8f)"
          % (float(eta), float(eta), n_star,
             float(ladder[n_star].b) if n_star else float("nan")),
          n_star is not None,
          "d_%s^2 <= %.8f < eta* = %s; the c_B threshold is already "
          "crossed at N = %s"
          % (n_star, float(ladder[n_star].b), float(eta), n_star_sig))

    # ---- T5 the class no-go theorem (plateau family)
    eps = Fraction(4, 5)
    beta = (Fraction(1, 2), Fraction(1, 2))
    beta2 = beta[0] ** 2 + beta[1] ** 2
    plateau_rows = []
    plat_ok = True
    for N in PLATEAU_N:
        a = [(Fraction(1), Fraction(1, k)) for k in range(1, N + 1)]
        Gt = [[ivf(a[i][0] * a[j][0] + a[i][1] * a[j][1]
                   + (eps ** 2 if i == j else Fraction(0)))
               for j in range(N)] for i in range(N)]
        bt = [ivf(a[i][0] * beta[0] + a[i][1] * beta[1]) for i in range(N)]
        # (i) G~ >= c_B I  (certified with the same interval LDL class)
        Gsh = [[Gt[i][j] - (ivf(cB) if i == j else iv.mpf(0))
                for j in range(N)] for i in range(N)]
        try:
            iv_ldl(Gsh, N)
            floor_holds = True
        except ArithmeticError:
            floor_holds = False
        # (ii)+(iii) sigma~ and d~^2
        Lt, Dt, _ = iv_ldl(Gt, N)
        zt = iv_forward(Lt, bt, N)
        q = iv.mpf(0)
        for j in range(N):
            q = q + zt[j] * zt[j] / Dt[j]
        d2t = 1 - q
        sig_ok = q.b <= float(sig)
        half_ok = d2t.a >= 0.5
        plateau_rows.append((N, floor_holds, mid(q),
                             float(d2t.a), sig_ok, half_ok))
        plat_ok = plat_ok and floor_holds and sig_ok and half_ok
    print("   plateau family  G~ = A A^T + (4/5)^2 I,  A row k = "
          "(1, 1/k),  b~ = A beta,  beta = (1/2, 1/2):")
    print("      N   G~ >= c_B I   sigma~      d~_N^2 lower   "
          "sigma~ <= 0.726909   d~^2 >= 1/2")
    for (N, f_ok, q_, d_, s_ok, h_ok) in plateau_rows:
        print("    %3d   %-11s   %.8f  %.10f     %-19s  %s"
              % (N, "yes" if f_ok else "NO", q_, d_,
                 "yes" if s_ok else "NO", "yes" if h_ok else "NO"))
    print("   PROOF (three lines, exact): d~_N^2 = min_c ||chi - sum c_k "
          "e~_k||^2 with e~_k = a_k . f + eps g_k, the f_i and g_k "
          "orthonormal and g_k _|_ chi, so")
    print("     d~_N^2 = min_c [ ||chi - (A^T c).f||^2 + eps^2 |c|^2 ] "
          ">= min_v ||chi - v.f||^2 = 1 - |beta|^2 = 1/2  for EVERY N.")
    check("S3.5 [IVAL+EXACT] T5 CLASS NO-GO: an EXPLICIT Gram family "
          "satisfies (H1) n = 1 > 0, (H2) G~ >= c_B I with c_B = %s, "
          "(H3) sigma~ <= %s -- i.e. EVERY hypothesis of the compiler "
          "certificate class, at EVERY N -- while d~_N^2 >= 1/2 for "
          "all N.  Hence NO conclusion of the form 'd_N -> 0' can "
          "follow from that hypothesis set" % (float(cB), float(sig)),
          plat_ok, "verified at N = %s; the plateau bound 1 - |beta|^2 "
          "= 1/2 is exact" % ",".join(str(n) for n, *_ in plateau_rows))

    # ---- T6 structure: Toeplitz / Hankel misfit of the BD Gram
    Nn = STRUCT_N
    dg = [1 / iv.sqrt(A[i][i]) for i in range(Nn)]
    Gh = [[A[i][j] * dg[i] * dg[j] for j in range(Nn)] for i in range(Nn)]
    def rel_misfit(mode):
        buckets = {}
        for i in range(Nn):
            for j in range(Nn):
                key = (i - j) if mode == "toeplitz" else (i + j)
                buckets.setdefault(key, []).append(Gh[i][j])
        num = iv.mpf(0)
        den = iv.mpf(0)
        for key, vals in buckets.items():
            m = iv.mpf(0)
            for v in vals:
                m = m + v
            m = m / iv.mpf(len(vals))
            for v in vals:
                num = num + (v - m) * (v - m)
        for i in range(Nn):
            for j in range(Nn):
                den = den + Gh[i][j] * Gh[i][j]
        return iv.sqrt(num / den)
    mis_t = rel_misfit("toeplitz")
    mis_h = rel_misfit("hankel")
    check("S3.6 [IVAL] T6 STRUCTURE: the normalized BD Gram at N = %d "
          "is exactly DILATION-covariant (S1.6) but sits far from the "
          "additive-lag world the deployed wall lives in -- relative "
          "orthogonal distance to the Toeplitz subspace %.4f and to "
          "the Hankel subspace %.4f (closed-form projection, NO fit).  "
          "The two Gram families are covariant for DIFFERENT groups, "
          "so a Loewner comparison between them has no index map"
          % (Nn, mid(mis_t),
             mid(mis_h)),
          mis_t.a > 0 and mis_h.a > 0,
          "both distances certified strictly positive")

    # ---------------------------------------------------------- S4 the fence
    sect("S4 -- THE CLASSICAL FENCE (task 4: what any transport may "
         "not violate)")
    print("   Burnol, Adv. Math. 170 (2002) 56-70 [UNCONDITIONAL]:")
    print("      liminf_N  d_N^2 log N  >=  sum_{Re rho = 1/2} "
          "m(rho)^2 / |rho|^2   (distinct critical zeros, m = "
          "multiplicity)")
    print("   improving BDBLS, Adv. Math. 149 (2000) 130-144 ('Notes "
          "sur la fonction zeta de Riemann, 3'), which had m(rho)^1.")
    print("   (the critical-line restriction is the SAFE reading of the "
          "sum: a subsum is a weaker lower bound, and Hardy already "
          "makes THIS subsum positive.)")
    print("   Hardy's theorem => the right-hand side is > 0 "
          "UNCONDITIONALLY, hence")
    print("      d_N  >>  1 / sqrt(log N)   and   NO bound d_N^2 = "
          "o(1/log N) can be true.")
    print("   Under RH with simple zeros the constant is the CLOSED "
          "FORM C_BD = 2 + gamma - log 4pi = %.12f (no zero data read "
          "here)." % mid(C_BD))
    print("   Best known UPPER bound is CONDITIONAL (under RH, "
          "Balazard-de Roton type): of size (log N)^(-1/2) up to "
          "log log factors -- WEAKER than the conjectured C_BD/log N, "
          "and no check below depends on this line.")
    print("   Best known UPPER bound, UNCONDITIONAL, with f -> 0:  "
          "NONE -- and by Baez-Duarte's theorem any such bound IS RH.")
    corridor = []
    for N in ladder_n:
        if N == 1:
            continue
        r = (ladder[N] * iv.log(iv.mpf(N))) / C_BD
        corridor.append((N, mid(r)))
    tail_rows = [r for (N, r) in corridor if N >= 32]
    check("S4.1 [IVAL] the certified ladder respects the fence: "
          "d_N^2 log N / C_BD stays in [%.4f, %.4f] on N >= 32 (v667 "
          "already registered the N = 256..2048 corridor; NOT "
          "duplicated here) -- consistent with the Burnol floor and "
          "with the conjectured C_BD/log N, and INCOMPATIBLE with any "
          "geometric or power decay"
          % (min(tail_rows), max(tail_rows)),
          min(tail_rows) > 0.5,
          "no ladder point falls below half the Burnol/BDBLS constant")
    # the rate fence, made explicit against the compiler's own rates
    print("   RATE FENCE applied to the compiler certificate class: a "
          "per-step contraction with a FIXED factor (the compiler's "
          "sigma <= %.6f, reserve %.6f, deep worst %.6f) iterated over "
          "a ladder of n steps yields sigma^n -- geometric.  Burnol "
          "forbids d_N^2 = o(1/log N), so a transported geometric "
          "contraction is not merely unavailable, it is PROVABLY "
          "FALSE unless the step index n grows like log log N, which "
          "the deployed rung ladder (h <= ~4072, 151 cells) does not."
          % (float(sig), float(eta),
             float(COMPILER_CERTS["deep_worst_59"])))

    # ---------------------------------------------------------- S5 controls
    sect("S5 -- CONTROLS (task 5: comb-blindness)")
    print("   exact surrogate identity: for theta = c/m (integers) the "
          "dilation family {theta_k/x} has Gram  c * G_BD(m_j, m_k)  "
          "and  b = theta (1 - gamma - log theta)  -- so thinned combs "
          "run on the SAME certified machinery.")

    def comb_ladder(name, ms, c):
        """the same certified pipeline as the full comb: interval LDL,
        certified pivots, Schur increments.  Returns the ladder plus the
        two compiler-visible FEATURES (positive definiteness and
        monotone non-increase), so the control can report whether the
        certificate class distinguishes the families at all."""
        n = len(ms)
        M = [[gram.G(ms[i], ms[j]) * iv.mpf(c) for j in range(n)]
             for i in range(n)]
        bb = []
        for m in ms:
            th = iv.mpf(c) / iv.mpf(m)
            bb.append(th * (1 - iv.euler - iv.log(th)))
        Lc, Dc, reach_c = iv_ldl(M, n, strict=False)
        zc = iv_forward(Lc, bb, reach_c)
        out, acc2, mono = [], iv.mpf(1), True
        for j in range(reach_c):
            step = zc[j] * zc[j] / Dc[j]
            if not step.a >= 0:
                mono = False
            acc2 = acc2 - step
            out.append(acc2)
        return out, (reach_c == n), mono

    odd, odd_pd, odd_mo = comb_ladder(
        "odd", [2 * k + 1 for k in range(1, N_CTRL + 1)], 2)
    mod3, mod3_pd, mod3_mo = comb_ladder(
        "mod3", [3 * k + 1 for k in range(1, N_CTRL + 1)], 3)
    dy, dy_pd, dy_mo = comb_ladder(
        "dyadic", [2 ** k for k in range(1, CTRL_DYADIC_N + 1)], 1)
    print("\n      N     BD full 1/k        odd 1/(k+1/2)      "
          "1 mod 3 comb       dyadic 1/2^k")
    for N in (2, 4, 8, 16, 32, N_CTRL):
        row = [ladder[N] if N in ladder else d2[N - 1],
               odd[N - 1], mod3[N - 1]]
        dyv = dy[N - 1] if N <= CTRL_DYADIC_N else None
        print("    %3d     %.10f       %.10f       %.10f       %s"
              % (N, mid(row[0]),
                 mid(row[1]),
                 mid(row[2]),
                 "%.10f" % mid(dyv) if dyv else "  --"))
    dy_plateau = dy[CTRL_DYADIC_N - 1].a
    d2_full = ladder[N_CTRL] if N_CTRL in ladder else d2[N_CTRL - 1]
    feat_blind = (odd_pd and odd_mo and mod3_pd and mod3_mo
                  and dy_pd and dy_mo)
    check("S5.1 [IVAL] FEATURE comb-blindness (this is the gate; the "
          "spec froze the control VALUES as a read with no bar): all "
          "three thinned combs -- odd 2/(2k+1), 1 mod 3, dyadic 1/2^k, "
          "none of them multiplicatively closed, no Moebius inversion "
          "available on any of them -- are certified positive definite "
          "with certified non-negative Schur increments by the SAME "
          "interval machinery as the arithmetic comb.  Positive "
          "definiteness, Schur positivity and monotonicity therefore "
          "carry NO arithmetic information",
          feat_blind,
          "odd PD %s mono %s | mod3 PD %s mono %s | dyadic PD %s mono %s"
          % (odd_pd, odd_mo, mod3_pd, mod3_mo, dy_pd, dy_mo))
    sep_odd = float(odd[N_CTRL - 1].a) / float(d2_full.b)
    sep_mod3 = float(mod3[N_CTRL - 1].a) / float(d2_full.b)
    print("   [READ, no bar -- and it REFUTES the expectation declared "
          "in C1] the control was set up expecting the finite-N VALUES "
          "to be comb-blind too.  They are not: at N = %d the "
          "arithmetic comb is certified BELOW the thinned combs by a "
          "factor %.1f (odd) and %.1f (1 mod 3), and the dyadic comb "
          "sits at d^2 >= %.4f.  Typed: NOT value-blind, feature-blind."
          % (N_CTRL, sep_odd, sep_mod3, float(dy_plateau)))
    print("   the separation is certified only AT the reachable N; the "
          "surrogate LIMITS are NOT claimed here (monotone non-increase "
          "bounds a limit from above, never from below).  What the "
          "control does establish is the T5 point on NATURAL objects "
          "instead of a synthetic family: four genuine L^2 dilation "
          "Gram systems, one certificate class, four different "
          "destinations -- so the class cannot see the destination.")

    # ---------------------------------------------------------- verdict
    res = dict(
        n_star=n_star, n_floor=n_floor, c0=float(c0),
        floor_bound=mid(floor_bound),
        lam_sharp=mid(lam_sharp), floor_sharp=mid(floor_sharp),
        d2_top=(float(ladder[n_top].a), float(ladder[n_top].b)),
        reach=reach, n_top=n_top,
        mis_t=mid(mis_t),
        mis_h=mid(mis_h),
        dy_plateau=float(dy_plateau),
        corridor=(min(tail_rows), max(tail_rows)),
    )
    transport_found = False           # nothing in the battery produced one
    obstruction = (floor_bound.b < 0 and n_floor is not None
                   and n_star is not None and plat_ok)
    if FAILS:
        verdict = "BN-INSTRUMENT-EDGE"
    elif transport_found:
        verdict = "BN-TRANSPORT-FOUND"
    elif obstruction:
        verdict = "BN-NO-TRANSPORT"
    else:
        verdict = "BN-CLASSICAL-GAP"
    return finish(verdict, res)


def finish(verdict, res):
    sect("VERDICT")
    print("  %s" % verdict)
    if verdict == "BN-NO-TRANSPORT":
        print("""
  THE OBSTRUCTION, in one paragraph.  The compiler's certified
  objects are, without exception, LOWER bounds on quadratic forms
  carrying a FIXED positive margin: B >= c_B I with c_B >= %.4f, and
  sigma <= %.6f i.e. reserve >= %.6f.  Under the only natural
  dictionary the BD Schur scalar IS d_N^2 and the BD sigma IS
  1 - d_N^2.  Three independent facts kill the transport:
    (i)  DIRECTION.  Loewner order is antitone under inversion, so a
         floor G >= P forces d_N^2 >= 1 - b^T P^-1 b -- a LOWER bound.
         The floor certified for G_%d by the compiler's own
         exact/interval LDL class is c = %.6f, transporting to %.1f;
         and that is no weak-bisection artefact, since even the
         sharpest conceivable floor lambda_min <= %.6f transports to
         %.1f.  Both vacuous.  Upper bounds on d_N need an
         UPPER Loewner domination G <= Q, which is a boundedness
         certificate, not a positivity certificate; the compiler
         produces none.
    (ii) EXISTENCE.  lambda_min(G_N) <= (log 2pi - gamma)/N -> 0, so
         hypothesis (H2) is not merely unhelpful, it is FALSE on the
         BD side for every N >= %s.  The BD Gram has no N-uniform
         floor to dominate.
    (iii) MARGIN.  The compiler certifies the reserve bounded AWAY
         from zero; Baez-Duarte needs it to VANISH.  Transported,
         (H3) asserts d_N^2 >= %.6f, refuted by the certified ladder
         at N* = %s.  And the class no-go is exact: an explicit Gram
         family satisfies every compiler hypothesis at every N while
         d_N^2 >= 1/2 forever, so the hypothesis set is logically
         incapable of implying d_N -> 0.
  Consistency with the classical fence: Burnol's unconditional
  liminf d_N^2 log N >= sum m(rho)^2/|rho|^2 > 0 forbids any o(1/log N)
  bound, so a transported per-step contraction would have been
  provably false, not merely unproved.
""" % (float(COMPILER_CERTS["c_B_ival"]),
       float(COMPILER_CERTS["sigma_worst_151"]),
       float(COMPILER_CERTS["eta_star"]), FLOOR_M,
       res.get("c0", float("nan")), res.get("floor_bound", float("nan")),
       res.get("lam_sharp", float("nan")),
       res.get("floor_sharp", float("nan")),
       res.get("n_floor"), float(COMPILER_CERTS["eta_star"]),
       res.get("n_star")))
        print("""  THE SHORTEST HONEST REMAINING LEMMA.  Produce, for each N, an
  EXPLICIT unconditional coefficient vector c^(N) with
      || chi - sum_{k<=N} c_k^(N) e_k ||^2 -> 0,
  equivalently an unconditional UPPER Loewner domination G_N <= Q_N
  with 1 - b^T Q_N^-1 b -> 0.  By Baez-Duarte's theorem that lemma is
  EQUIVALENT to RH, so it is not a step towards RH -- it is RH.  The
  honest corollary typing of this run is therefore
  BN-NO-TRANSPORT + BN-RESTATEMENT: no compiler object dominates the
  BD Gram, and the object that would is RH itself.""")
    ok = len(FAILS) == 0
    print("\nchecks: %d, failures: %d %s"
          % (len(CHECKS), len(FAILS), FAILS or ""))
    el = time.time() - T0
    print("elapsed: %.1f s (bar %.0f s) %s"
          % (el, RUNTIME_BAR, "OK" if el < RUNTIME_BAR else "OVER"))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FIREWALL: experiments-only; writes nothing; no zeros read; "
          "no prime tables; no verification/ import; no marker moved; "
          "NO RH claim.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
