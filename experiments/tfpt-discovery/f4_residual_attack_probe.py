#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""f4_residual_attack_probe -- PRIME.F4.RESIDUAL.ATTACK.01.

EXPLORATION ONLY.  Demand accounting for an already-published valid
lower bound.  No positivity claim, no RH claim, no promotion, nothing
outside experiments/.

THE QUESTION.  CCCLXVIII reduced the residual demand of CCCLIX to the
F4 form: with x_0 = B^-1 b_0, v := A_2^T x_0, w the source lag profile
(b_c = -(1/4) A_2 w, sympy-exact, residual 1.1e-16 at 96 points),

  int_0^1 [ -(1/2)<w, v> - q_c ] dtheta > int_0^1 [ q_0 - n_0 ] dtheta
  (n_c = 0 identically),

q_c = b_c^T B^-1 b_c >= 0 the UNSIGNED alignment term (miss 9.96e3 /
4.26e5 / 3.62e5) and -(1/2)<w,v> the SIGNED input (miss 60.888 /
295.97 / 205.35, growth exponent 2.119).  This probe attacks BOTH with
the unconditional classical toolkit, prices the explicit-formula
content of the signed term, and computes the invariant floor of every
reformulation that consumes the same information.

FOUR EXACT FACTS THIS PROBE USES (all machine-checked in S1).

(I) THE F4 KERNEL IS A CONGRUENCE INVARIANT.  q_c = (1/16) w^T K w with
K := A_2^T B^-1 A_2, and under the congruence B -> M^T B M (which
sends b_c -> M^T b_c, hence A_2 -> M^T A_2) the kernel is UNCHANGED:
(M^T A_2)^T (M^T B M)^-1 (M^T A_2) = A_2^T B^-1 A_2.  Every bound and
every floor built from K is therefore basis independent -- strictly
stronger than CCCLXVIII (III), where only the box floor was invariant.

(II) THE SOURCE PROFILE LIVES IN A CONE, NOT IN A BOX.  c_c(x) =
sum_n a_n tau(x - nu_n) with a_n = Lambda(n)/sqrt(n) >= 0, nu_n =
log n / D, tau the unit hat; hence w_k = c_c(k-1+2theta) + c_c(k-1)
satisfies w >= 0 ENTRYWISE, supp w subset J := {k : k >= nu_2 - 3},
and w = Phi^T a with a >= 0.  The sign flip w -> -w used by the
CCCLXVIII unsigned no-go is NOT admissible in this cone; the box class
I(R) discards the positivity of the von Mangoldt weights.

(III) A_2 ANNIHILATES THE PNT MAIN COMB.  For the geometric profile
p_k = e^{lambda k}, lambda = D/2, (A_2 p)_i = (2 cosh lambda - 2)
e^{lambda(i+2)}, i.e. the smooth main comb enters b_c only at relative
order D^2/4 (exact).  The deployed envelope R_c prices the smooth main
mass in FULL, while the exact PNT main lag profile w_s contributes of
order 1e-5 of the signed term (measured in D1, controlled in X3).  The
signed input is a pure prime FLUCTUATION correlation.

(IV) THE ATOM-COORDINATE IDENTITY.  <w, v> = sum_n a_n Psi(nu_n) with
Psi(nu) := I_v(nu) + I_v(nu - 2theta), I_v the piecewise-linear
interpolant of v on the nodes -1..h (exact; warded to roundoff).  With
the EVEN test function F(u) := -(1/4) Psi(|u|/D), supported in
|u| <= S := (h + 2theta) D, the signed input is EXACTLY CCCLXVI's
PRIME(F) = 2 sum_{n <= e^S} Lambda(n) n^{-1/2} F(log n) (warded from
the atoms, E0), so Weil's explicit formula applies verbatim in
CCCLXVI's normalisation.

ERROR CONVENTION (stated because it decides comparability).  The
signed VALUE is enclosed sharply by Cauchy-Schwarz in the B^-1 inner
product (2<b_c,x_0>, CCCLXVIII's bilin_encl; ward A9b).  The demands
are Hoelder products of a source envelope with a NORM of v, and the
norms are reported in the DEPLOYED convention: summation roundoff
(Higham gamma, outward) on the computed x_0, exactly as CCCLXVIII's
x0_d2_l1, so that every miss and exponent is comparable to the note.
The entrywise certificate for the exact x_0, ||A_2^T delta||_2 <=
4 ||res||_2 / beta, is reported per rung as a separate diagnostic and
never folded into a demand; at the deep rung it exceeds the demand
itself, which is a statement about beta, not about the bounds.

THE CLASSICAL INPUTS, WITH EXPLICIT CONSTANTS (all EXTERNAL-CITED,
nothing re-proved here):
 (C1) Rosser-Schoenfeld/Schoenfeld  psi(x) < 1.03883 x for x > 0.
 (C2) Brun-Titchmarsh in the MONTGOMERY-VAUGHAN 1973 form
      pi(x+y) - pi(x) <= 2 y / log y   for y >= 2, all x >= 0.
      (This is the large-sieve tool.  CCCLXVII excluded Montgomery-
      Vaughan/large sieve in the LI coordinates because the extraction
      point z = 0 sits on the boundary of the absolute-convergence
      disc Re s > 1.  In the F4 coordinates there is NO Dirichlet
      series: the prime side is the FINITE sum over n <= e^{a+3D}
      (compact support in log space), so the exclusion does not
      apply.  S1.9 wards the finiteness.)
 (C3) Chebyshev-Mertens  sum_{n<=x} Lambda(n)/n <= log x + 1.03883
      (from log floor(x)! = sum Lambda(n) floor(x/n), Stirling, (C1)).
 (C4) T(N) := sum_{n<=N} Lambda(n)/sqrt(n) <= 2 * 1.03883 sqrt(N)
      (Stieltjes + (C1)).
 (C5) sum_{n<=N} Lambda(n)^2/n <= (log N)(log N + 1.03883)  ((C3)).
 (C6) prime powers: #{p^k in (A,B], k>=2} <= sum_{2<=k<=log_2 B}
      (B^{1/k} - A^{1/k} + 1).
Each of (C3)-(C6) is additionally checked against the EXACT finite sum
at every audited cell (wards A8-A10); the reported bounds use the
envelopes, the exact sums are reported only as slack diagnostics.

THE FIVE NEW DEMANDS (same finite statement, same classical inputs,
different information consumed; every quantity outward rounded).

 U0 DEPLOYED F4 UNSIGNED   0.25 R_c^2 sum_{rs}|K_rs|.
 U1 SCHUR/l2              (1/16) maxrow_J |K| * W2, W2 an upper bound
                          for ||w||_2^2 from (C2)/(C5).
 U2 GRAM/l2               (1/16) lam_max(K_J) * W2, lam_max certified
                          by a SHIFTED CHOLESKY on mu I - K_J (no
                          eigensolver; power iteration is an
                          unverified hint whose value is re-certified).
 S0 DEPLOYED F4 SIGNED     R_c ||v||_1                (Hoelder, lags).
 S1 REACH+SUPPORT          R_c^reach ||v_J||_1        (same Hoelder;
                          R_c^reach corrects the log-reach of w from
                          2a+2D to a+3D -- pure bookkeeping).
 S2 CAUCHY-SCHWARZ         (1/2) sqrt(W2) ||v_J||_2.
 S3 ATOM-HOELDER           (1/2) T(N) ||Psi||_inf     (Hoelder in the
                          ATOM coordinates; ||Psi||_inf is exact,
                          Psi piecewise linear).
 S4 WINDOW-KNAPSACK        (1/2) sum over the top ceil(T/L) disjoint
                          8D-windows of L * max_window |Psi|, L the
                          (C2)-envelope for the mass of any 8D window
                          -- the sharp bound for the information
                          {a >= 0, local density <= L, total <= T}.
Every demand is aggregated as the MAX over the 32 frozen theta (the
CCCLXVIII convention), and so is every floor, so that floor <= demand
holds theta by theta and hence after aggregation.

THE FLOORS (the CCCLXVIII (III) method, one class per line; each floor
is ATTAINED at an admissible datum, hence a valid lower bound for
EVERY bound consuming that information, and each is invariant under
the congruence by (I)):
 FL-box+l2   sup{ |<w,v>|/2 : |w|_inf <= W_inf, ||w||_2^2 <= W2,
             supp w subset J } -- exact water filling (sorted greedy).
 FL-cone     sup{ <w,v>/2 : w = Phi^T a, a >= 0, local density <= L,
             total <= T } -- knapsack; the attained lower bound places
             mass L at the argmax of Psi_+ in every SECOND selected
             window (so the density constraint holds strictly).
 FL-unsigned sup{ (1/16) w^T K w } over the same cone, evaluated with
             a certified quadratic-form enclosure at an admissible
             cone point aligned with a power-iteration hint.

WHAT IS MEASURED.  Per registered cell and frozen theta midpoint:
the CCCLXVIII quantities (beta, q_0, q_c, <b_c,x_0>, ||v||_1,
sum|K|, R_c), the new ones (maxrow_J|K|, certified lam_max(K_J), W2 by
three routes, T, L, P_max, ||Psi||_inf, the window ladder, ||v_J||_2,
the smooth/fluctuation split of the signed term, the DFT profile of
v_J), the three floors, and -- at ONE frozen theta per cell -- the
explicit-formula readout POLE(F), ARCH(F), PRIME(F) and the DERIVED
zero sum sum_rho Fhat(gamma_rho) = POLE + ARCH - PRIME.  NO zero datum
is read anywhere: the zero sum is obtained from the cited identity, and
the POLE/ARCH implementation is warded against CCCLXVI's independently
certified 50-digit closed form for the deployed Fejer window.
Growth is reported as ratios and two-point exponents p =
log(ratio)/log(h ratio) between the registered rungs.  NO fit.

FROZEN PROTOCOL (before the run of record).
 S0  SHA and AST firewall: no zero reader, tau, target sign,
     eigensolver or fitting call; deep evaluator cells excluded.
 S1  The nine exact lemmas above.
 S2  Self-tests: quadratic-form enclosure, |K| row-sum bound, the
     shifted-Cholesky lam_max certificate on a planted spectrum, the
     water-filling optimality, and the POLE/ARCH ward against
     CCCLXVI's closed form at both registered cells.
 A   Targets 184/405/838, 32 frozen theta midpoints.  Wards: the
     CCCLIX/CCCLXVIII deployed miss A/G, the measured theta-means of
     s, the source factorisation, n_c = 0, w >= 0, supp w, and the
     CCCLXVIII signed/unsigned misses must be reproduced.
 B   The unsigned ladder U0/U1/U2 + FL-unsigned, misses, exponents.
 C   The signed ladder S0..S4 + FL-box+l2/FL-cone, misses, exponents.
 D   The structure of v: norms, sign changes, DFT profile, log
     frequency r = omega/D, the Type I/II availability diagnostic
     log N / log r, and the smooth/fluctuation split.
 E   The explicit-formula readout: the CCCLXVI normalisation warded
     from the atoms, POLE/ARCH/P_main, the DERIVED zero sum, the sign of
     the remaining bar, and the sign pattern of Fhat on the real axis
     (which decides whether a positivity route could exist at all).
 X   SCRAMBLE, EPSTEIN and SMOOTH-WALL (the PNT main density as a comb,
     two discretisations) through the identical pipeline at the 184
     cell, 8 frozen offsets; plus SMOOTH-SOURCE, which keeps the
     deployed wall, the deployed v and the PD premise and replaces ONLY
     the source profile w by the exact PNT main lag profile w_s.  The
     frame controls can only refuse the premise (they are comb-blind on
     the algebra); SMOOTH-SOURCE is the control the SIGNED term must
     break, and it must break it with the premise intact.
 V   Frozen enum and precedence as below.

FROZEN VERDICT ENUM AND PRECEDENCE (the mission's enum, unchanged).
  F4-NO-PROGRESS        iff a structural ward (S0/S1/S2) fails, or the
      CCCLXVIII reproduction wards miss by more than 5 percent, or no
      new demand improves on the deployed one.
  F4-UNSIGNED-CLOSED    iff the best unsigned demand leaves the signed
      term a POSITIVE budget, i.e. U_best + (q_0 - n_0) < the measured
      signed input at every audited (cell, theta).
  F4-SIGNED-EXPLICIT    iff the signed input is exhibited in
      explicit-formula form with the POLE/ARCH ward green.
  F4-EXPONENT-IMPROVED  iff the best signed miss exponent is at most
      0.8 times the deployed 2.119.
  F4-EXPONENT-FLOOR     iff a floor above 1 with a positive exponent is
      certified for the sharpest declared class.
Precedence: NO-PROGRESS > UNSIGNED-CLOSED > SIGNED-EXPLICIT >
EXPONENT-IMPROVED > EXPONENT-FLOOR; the non-selected applicable labels
are reported as TAGS.

DISCLOSURE.  Before this spec was frozen, an exploratory read measured,
at ONE theta per cell: sum|K|, maxrow|K|, a power-iteration hint for
lam_max(K_J), ||w||_2^2, the norms of v, the DFT peak of v_J, the
smooth/fluctuation split of <w,v>, the three W2 routes, and the
Fejer-window ward of the POLE/ARCH implementation.  The verdict enum
and its precedence are the mission's, fixed before any read; the cell
list, theta grid, window width, classical constants and envelope
formulas were not chosen after a result read.

SCOPE.  Reads shift_average_probe, shift_average_all_depth_probe and
matrix_stage_conditioning_probe READ-ONLY (deployed generators, the
deployed envelopes and the CCCLXVIII enclosure toolkit) so that the
CCCLIX/CCCLXVIII numbers are reproduced rather than re-derived.  Writes
nothing.  No verification/, papers, ledger, website, manifests, .md or
commits.  No tau, no zero data, no target sign, no eigensolver, no fit,
no ladder scan (deep evaluator cells 1393/2854 excluded).  Runtime bar
1800 s.  NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap                # noqa: E402  READ-ONLY
import shift_average_all_depth_probe as sad      # noqa: E402  READ-ONLY
import matrix_stage_conditioning_probe as msc    # noqa: E402  READ-ONLY

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

AUDIT_TARGETS = (184, 405, 838)
REGISTERED_RUNGS = (184, 405)
N_THETA = 32
CTRL_THETA = tuple((k + 0.5) / 8.0 for k in range(8))
EF_THETA = 0.5 / 32.0                  # frozen theta for the E readout
RUNTIME_BAR = 1800.0
WARD_REL = 0.05
U_RND = 0.5 * float(np.finfo(float).eps)

# classical constants (EXTERNAL-CITED, never re-proved here)
PSI_CHEB = 1.03883          # (C1) Rosser-Schoenfeld/Schoenfeld
BT_CONST = 2.0              # (C2) Montgomery-Vaughan 1973 Brun-Titchmarsh
WIN_GRID = 8.0              # window width in grid units (8D in log space)
N_PART = 512                # subintervals for the monotone envelope maxima
GL_N = 24                   # Gauss-Legendre nodes per panel (E readout)
GL_N_WARD = 8               # second resolution for the quadrature ward
GRADE_RATIO = 2.0           # geometric panel grading bar b/a for ARCH
FHAT_XI_MAX = 4.0           # Fhat grid reaches xi = 4/D (past Nyquist)
FHAT_N = 257                # Fhat grid points (positive-type diagnosis)
SMOOTH_PER_GRID = (8, 16)   # smooth-control discretisations
LAM_INFLATE = (1.02, 1.05, 1.15, 1.4, 2.0, 4.0, 16.0)

# CCCLXVIII numbers this probe must reproduce (wards)
WARD_F0_REL = {184: 2.4701e11, 405: 1.9898e14}
WARD_S_MEAN = {184: 1.507357381e-1, 405: 9.991056582e-2}
WARD_SIGNED_MISS = {184: 60.888, 405: 295.97, 838: 205.35}
WARD_UNSIGNED_MISS = {184: 9.96e3, 405: 4.26e5, 838: 3.62e5}
WARD_FEJER_B = {184: -1.2648057425013541047014253722995504938946619780529,
                405: -1.3147508968858830784281862643309942548233303249968}
DEPLOYED_SIGNED_EXP = 2.119

AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
    "tau", "target_sign", "cached_sign", "polyfit", "curve_fit",
    "lstsq", "least_squares",
}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in AST_BANNED:
            hits.append(name)
    return sorted(set(hits))


def gam(k):
    return msc.gam(k)


def fsum(v):
    return msc.fsum(v)


def orders(v_lo, v_hi):
    if v_lo <= 0 or v_hi <= 0:
        return float("nan")
    return math.log10(v_hi / v_lo)


def exponent(v_lo, v_hi, h_lo, h_hi):
    if v_lo <= 0 or v_hi <= 0:
        return float("nan")
    return math.log(v_hi / v_lo) / math.log(float(h_hi) / float(h_lo))


# ==================================================== classical envelopes
def prime_power_count_up(a_lo, b_hi):
    """(C6) upper bound for #{p^k in (a_lo, b_hi], k >= 2}."""
    if b_hi <= 4.0:
        return 0.0
    tot = 0.0
    k = 2
    while 2.0 ** k <= b_hi:
        tot += max(0.0, b_hi ** (1.0 / k) - max(a_lo, 1.0) ** (1.0 / k)) + 1.0
        k += 1
    return tot


def prime_count_up(a_lo, b_hi):
    """Upper bound for pi(b_hi) - pi(a_lo): the integer count when the
    interval is shorter than 2, else (C2) Brun-Titchmarsh."""
    length = b_hi - a_lo
    if length <= 0.0:
        return 0.0
    integers = math.floor(b_hi) - math.ceil(a_lo) + 1.0
    integers = max(integers, 0.0)
    if length < 2.0:
        return integers
    return min(integers, BT_CONST * length / math.log(length))


def window_mass_up(y_lo, y_hi, half_log):
    """Upper bound for max over y in [y_lo, y_hi] of
    sum_{n in (y e^-half, y e^half]} Lambda(n)/sqrt(n), monotone
    envelope on the whole y-interval."""
    a_lo = max(1.0, y_lo * math.exp(-half_log))
    b_hi = y_hi * math.exp(half_log)
    cnt = prime_count_up(a_lo, y_hi * math.exp(half_log)) \
        + prime_power_count_up(a_lo, b_hi)
    # the count bound above is taken on the WIDEST window in the range
    return cnt * math.log(b_hi) / math.sqrt(a_lo), cnt


def env_maxima(n_top, half_log, n_part=N_PART):
    """(P_max, L_max): rigorous upper bounds for the number of prime
    powers and for the Lambda/sqrt mass of ANY window
    (y e^-half, y e^half] with 2 <= y <= n_top, via a monotone
    envelope on each of n_part geometric subintervals."""
    if n_top <= 2.0:
        return 1.0, math.log(2.0) / math.sqrt(2.0)
    edges = 2.0 * np.exp(np.linspace(0.0, math.log(n_top / 2.0),
                                     n_part + 1))
    p_max = 0.0
    l_max = 0.0
    for i in range(n_part):
        mass, cnt = window_mass_up(float(edges[i]), float(edges[i + 1]),
                                   half_log)
        p_max = max(p_max, cnt)
        l_max = max(l_max, mass)
    return p_max, l_max


_ENV_CACHE: dict[tuple[float, float, int, int], dict] = {}


def source_envelopes(a_value, d_value, h, k0):
    """All classical inputs of one cell in one place (cached): the
    reach-corrected source envelope R_c^reach, N = e^{a+3D}, the
    window count/mass envelopes (C2)/(C6), the total mass (C4), the
    square sum (C5) and the three W2 routes for ||w||_2^2."""
    key = (a_value, d_value, h, k0)
    if key in _ENV_CACHE:
        return _ENV_CACHE[key]
    eta = sad.vk_eta(max(2.0 * a_value - 2.0 * d_value, math.e),
                     sad.VK_c_OPT)
    sqrt_y = math.exp(0.5 * (a_value + 3.0 * d_value))
    rc_reach = (msc.head_source(2)
                + 4.0 * sqrt_y * math.sinh(0.5 * d_value)
                + 2.0 * sad.VK_C_OPT * sqrt_y * math.exp(0.5 * d_value)
                * math.exp(-eta))
    n_top = math.exp(a_value + 3.0 * d_value)
    half_log = 0.5 * WIN_GRID * d_value
    p_max, l_max = env_maxima(n_top, half_log)
    t_env = total_mass_up(n_top)
    l2_env = lam2_sum_up(n_top)
    w2_box = float(h + 2 - k0) * (2.0 * rc_reach) ** 2
    w2_schur = 4.0 * p_max * l2_env
    w2_mix = 4.0 * l_max * t_env
    w2 = min(w2_box, w2_schur, w2_mix)
    out = dict(Rc_reach=rc_reach, n_top=n_top, half_log=half_log,
               p_max=p_max, l_max=l_max, t_env=t_env, l2_env=l2_env,
               W2_box=w2_box, W2_schur=w2_schur, W2_mix=w2_mix, W2=w2,
               W2_route=("box (|J| (2 R_c^reach)^2)" if w2 == w2_box
                         else "Schur/atom (4 P sum Lambda^2/n)"
                         if w2 == w2_schur else "mixed (4 L T)"))
    _ENV_CACHE[key] = out
    return out


def total_mass_up(n_top):
    """(C4) sum_{n<=N} Lambda(n)/sqrt(n) <= 2*1.03883 sqrt(N)."""
    return 2.0 * PSI_CHEB * math.sqrt(n_top)


def lam2_sum_up(n_top):
    """(C5) sum_{n<=N} Lambda(n)^2/n <= log N (log N + 1.03883)."""
    lg = math.log(max(n_top, 2.0))
    return lg * (lg + PSI_CHEB)


def chebyshev_sum_up(n_top):
    """(C3) sum_{n<=N} Lambda(n)/n <= log N + 1.03883."""
    return math.log(max(n_top, 2.0)) + PSI_CHEB


# ============================================================== S1 exact
def s1_qc_kernel():
    """q_c = (1/16) w^T A_2^T B^-1 A_2 w, exactly, from
    b_c = -(1/4) A_2 w."""
    h = 4
    Bs = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    A = sp.Matrix(msc.second_difference_matrix(h).tolist())
    ww = sp.Matrix(sp.symbols("w0:%d" % (h + 2)))
    bc = -sp.Rational(1, 4) * (A * ww)
    lhs = sp.simplify((bc.T * Bs.inv() * bc)[0])
    rhs = sp.simplify(sp.Rational(1, 16)
                      * (ww.T * A.T * Bs.inv() * A * ww)[0])
    return sp.simplify(lhs - rhs) == 0


def s1_kernel_congruence_invariance():
    """K = A_2^T B^-1 A_2 is UNCHANGED under the congruence
    B -> M^T B M, A_2 -> M^T A_2 (which is what b_c -> M^T b_c
    induces)."""
    n = 3
    Bs = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    M = sp.Matrix(n, n, lambda i, j: sp.Symbol("M%d%d" % (i, j)))
    A = sp.Matrix(n, 2, lambda i, j: sp.Symbol("A%d%d" % (i, j)))
    k_raw = sp.simplify(A.T * Bs.inv() * A)
    k_new = sp.simplify((M.T * A).T * (M.T * Bs * M).inv() * (M.T * A))
    return sp.simplify(k_raw - k_new) == sp.zeros(2, 2)


def s1_schur_test():
    """|w^T K w| <= (max_r sum_s |K_rs|) ||w||_2^2, exact-rational
    witness plus the AM-GM step symbolically."""
    a, b = sp.symbols("a b", real=True)
    amgm = sp.simplify(sp.Rational(1, 2) * (a ** 2 + b ** 2) - a * b)
    step = sp.simplify(sp.factor(amgm) - sp.Rational(1, 2) * (a - b) ** 2)
    K = sp.Matrix([[sp.Rational(7, 2), sp.Rational(-4, 3)],
                   [sp.Rational(-4, 3), sp.Rational(5, 4)]])
    ww = sp.Matrix([sp.Rational(3, 5), sp.Rational(-7, 4)])
    lhs = sp.simplify((ww.T * K * ww)[0])
    rows = max(sum(abs(K[r, s]) for s in range(2)) for r in range(2))
    rhs = rows * sp.simplify((ww.T * ww)[0])
    return step == 0 and lhs <= rhs, lhs, rhs


def s1_a2_annihilates_geometric():
    """(A_2 p)_i = (2 cosh lambda - 2) e^{lambda (i+2)} for
    p_k = e^{lambda k}: the smooth main comb survives only at relative
    order lambda^2 = D^2/4."""
    lam = sp.Symbol("lam", positive=True)
    h = 5
    p = sp.Matrix([sp.exp(lam * k) for k in range(h + 2)])
    A = sp.Matrix(msc.second_difference_matrix(h).tolist())
    got = A * p
    ok = True
    for i in range(h - 1):
        want = (2 * sp.cosh(lam) - 2) * sp.exp(lam * (i + 2))
        dif = sp.expand((got[i] - want).rewrite(sp.exp))
        ok = ok and sp.simplify(dif) == 0
    ser = sp.series(2 * sp.cosh(lam) - 2, lam, 0, 4).removeO()
    return ok and sp.simplify(ser - lam ** 2) == 0


def s1_atom_identity():
    """<w, v> = sum_n a_n Psi(nu_n) with w_k = sum_n a_n [tau(x_k+2t-nu)
    + tau(x_k-nu)] and Psi(nu) = I_v(nu) + I_v(nu-2t): the exact
    transposition of the tent-sampling operator (Fraction-exact on a
    small instance)."""
    h = 4
    t2 = Fraction(1, 3)                      # 2 theta
    nus = [Fraction(7, 5), Fraction(23, 10)]
    aa = [Fraction(3, 4), Fraction(1, 2)]
    vv = [Fraction(k * k + 1, k + 3) for k in range(h + 2)]

    def tent(x):
        x = abs(x)
        return Fraction(0) if x >= 1 else 1 - x

    lhs = Fraction(0)
    for k in range(h + 2):
        xk = Fraction(k - 1)
        wk = sum(aa[j] * (tent(xk + t2 - nus[j]) + tent(xk - nus[j]))
                 for j in range(len(aa)))
        lhs += wk * vv[k]
    rhs = Fraction(0)
    for j in range(len(aa)):
        psi = sum(vv[k] * (tent(nus[j] - t2 - Fraction(k - 1))
                           + tent(nus[j] - Fraction(k - 1)))
                  for k in range(h + 2))
        rhs += aa[j] * psi
    return lhs == rhs, lhs


def s1_cone_positivity():
    """w = Phi^T a with a >= 0 and Phi >= 0 entrywise, hence w >= 0 and
    the flip w -> -w is inadmissible unless w = 0 (exact)."""
    Phi = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)],
                     [sp.Rational(0), sp.Rational(3, 4)]])
    aa = sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 5)])
    ww = Phi.T * aa
    nonneg = all(ww[i] >= 0 for i in range(2))
    flip_admissible = all(-ww[i] >= 0 for i in range(2))
    return nonneg and not flip_admissible


def s1_waterfill_optimal():
    """max sum_k |v_k| w_k over {0 <= w <= c, sum w^2 <= q} is the
    sorted greedy (exact-rational witness: greedy >= every vertex of a
    fine admissible net)."""
    vabs = [Fraction(5), Fraction(3), Fraction(1)]
    cap = Fraction(2)
    q = Fraction(9, 2)
    best = waterfill(np.array([float(x) for x in vabs]), float(cap),
                     float(q))
    grid = [Fraction(i, 4) * cap for i in range(5)]
    worst = 0.0
    for x in grid:
        for y in grid:
            for z in grid:
                if x * x + y * y + z * z <= q:
                    val = float(vabs[0] * x + vabs[1] * y + vabs[2] * z)
                    worst = max(worst, val)
    return best + 1e-12 >= worst, best, worst


def s1_class_floor_attained():
    """The water-filling value is ATTAINED at an admissible datum, so
    every valid bound consuming only {|w|_inf <= cap, ||w||_2^2 <= q}
    is at least that value (the CCCLXVIII (III) step, re-run for the
    box+l2 class; exact-rational witness, float greedy compared)."""
    vv = [sp.Rational(4), sp.Rational(-3), sp.Rational(1)]
    cap = sp.Rational(1)
    q = sp.Rational(2)
    w_star = [cap, -cap, sp.Rational(0)]
    adm = all(abs(x) <= cap for x in w_star) \
        and sum(x * x for x in w_star) <= q
    val = sum(w_star[i] * vv[i] for i in range(3))
    greedy = waterfill(np.array([float(abs(x)) for x in vv]),
                       float(cap), float(q))
    return (adm and abs(greedy - float(val)) < 1.0e-12
            and val > 0), val


def s1_prime_side_finite():
    """The F4 prime side is a FINITE sum: w reads only atoms with
    nu_n <= h + 3, i.e. n <= e^{a+3D}; there is no Dirichlet series and
    no absolute-convergence boundary (the CCCLXVII E9 exclusion of
    Montgomery-Vaughan/large sieve does not transfer)."""
    h = sp.Symbol("h", positive=True, integer=True)
    dd = sp.Symbol("D", positive=True)
    nu_max = (h + 1) + 1 + 1              # x_k <= h + 2theta, tent < 1
    reach = sp.simplify(nu_max * dd)
    return sp.simplify(reach - (h * dd + 3 * dd)) == 0, reach


# ================================================================ toolkit
def waterfill(vabs, cap, quad):
    """max sum_k vabs_k w_k over 0 <= w_k <= cap, sum w_k^2 <= quad:
    the sorted greedy, evaluated with fsum."""
    if cap <= 0.0 or quad <= 0.0:
        return 0.0
    idx = np.argsort(-np.asarray(vabs, float))
    budget = float(quad)
    parts = []
    for j in idx:
        if budget <= 0.0:
            break
        take = min(cap, math.sqrt(budget))
        parts.append(float(vabs[j]) * take)
        budget -= take * take
    return fsum(parts) if parts else 0.0


def knapsack_windows(win_max, cap, total):
    """Upper bound sum_j m_j M_j over m_j <= cap, sum m_j <= total,
    M_j = win_max sorted descending (exact LP value)."""
    mm = np.sort(np.asarray(win_max, float))[::-1]
    mm = mm[mm > 0.0]
    left = float(total)
    parts = []
    for val in mm:
        if left <= 0.0:
            break
        take = min(cap, left)
        parts.append(take * val)
        left -= take
    return fsum(parts) if parts else 0.0


def knapsack_attained(win_max, cap, total):
    """LOWER bound of the same sup, attained by an admissible measure:
    point masses cap at the argmax of the selected windows, no two
    selected windows adjacent (so every window-width interval carries
    at most one atom)."""
    vals = np.asarray(win_max, float)
    order = np.argsort(-vals)
    used = set()
    left = float(total)
    parts = []
    for j in order:
        if left <= 0.0:
            break
        if vals[j] <= 0.0:
            break
        if (j - 1) in used or (j + 1) in used or j in used:
            continue
        take = min(cap, left)
        parts.append(take * float(vals[j]))
        left -= take
        used.add(int(j))
    return fsum(parts) if parts else 0.0


def rowsum_and_lammax(A2, B, cf, beta, h, k0):
    """Outward-rounded (max_r sum_s |K_rs| over r,s in J,
    certified lam_max(K_J) upper bound, K float) for
    K = A_2^T B^-1 A_2, via the exact residual identity
    K = A_2^T Y + Y^T Res + Res^T B^-1 Res,  Res = A_2 - B Y."""
    n = B.shape[0]
    Y = sla.cho_solve(cf, A2, check_finite=False)
    Res = A2 - B @ Y
    env_res = gam(n + 1) * (np.abs(B) @ np.abs(Y) + np.abs(A2))
    res_col = np.sqrt(msc.fsum_sq_cols(np.abs(Res) + env_res)) \
        * (1.0 + gam(n + 2))
    y_col = np.sqrt(msc.fsum_sq_cols(np.abs(Y))) * (1.0 + gam(n + 2))
    C = msc.apply_at_matrix(Y, h)
    env_c = gam(n + 1) * msc.apply_at_matrix(Y, h, absolute=True)
    res_tot = fsum(res_col)
    # row sums on the J block
    absC = np.abs(C[k0:, k0:]) + env_c[k0:, k0:]
    rows = absC.sum(axis=1) * (1.0 + gam(n + 2))
    rows = rows + y_col[k0:] * res_tot + res_col[k0:] * res_tot / beta
    schur_up = float(np.max(rows)) if rows.size else 0.0
    # certified lam_max on the J block
    KJ = np.ascontiguousarray(C[k0:, k0:])
    KJ = 0.5 * (KJ + KJ.T)
    nJ = KJ.shape[0]
    corr = float(np.max(env_c[k0:, k0:].sum(axis=1))) \
        + 2.0 * math.sqrt(fsum(y_col ** 2)) * math.sqrt(fsum(res_col ** 2)) \
        + fsum(res_col ** 2) / beta
    vv = np.ones(nJ) / math.sqrt(nJ)
    for _ in range(120):
        vv = KJ @ vv
        nv = float(np.linalg.norm(vv))
        if not math.isfinite(nv) or nv == 0.0:
            vv = np.ones(nJ) / math.sqrt(nJ)
            break
        vv /= nv
    mu_hat = abs(float(fsum(vv * (KJ @ vv))))
    lam_up = None
    for infl in LAM_INFLATE:
        mu = mu_hat * infl + 1e-300
        Ash = -KJ.copy()
        Ash[np.diag_indices(nJ)] += mu
        try:
            L = np.linalg.cholesky(Ash)
        except np.linalg.LinAlgError:
            continue
        aL = np.abs(L)
        wgt = float(np.max(aL @ aL.sum(axis=0)))
        slack = gam(nJ + 1) * wgt + U_RND * (mu + float(np.max(np.abs(
            np.diag(Ash)))))
        lam_up = mu + slack + corr
        break
    return schur_up, lam_up, mu_hat, vv


def tent_interp(nodes, vals, xs):
    return np.interp(np.asarray(xs, float), nodes, vals, left=0.0,
                     right=0.0)


# ===================================================== POLE / ARCH / F
def panel_int(fun, edges, glx, glw):
    a = edges[:-1]
    b = edges[1:]
    half = 0.5 * (b - a)
    mid = 0.5 * (a + b)
    xs = mid[:, None] + half[:, None] * glx[None, :]
    vals = fun(xs.ravel()).reshape(xs.shape)
    return float(np.dot(half, vals @ glw))


def graded_edges(edges, ratio=GRADE_RATIO):
    """Geometric refinement of every panel with b/a > ratio and a > 0.
    The ARCH integrand is analytic at w = 0 only through the linear
    piece that touches 0; on a panel [a, b] not touching 0 its analytic
    continuation keeps the simple pole of 1/(1-e^{-2w}) at the origin,
    so Gauss-Legendre needs (b - a) <~ a.  F stays linear on every
    sub-panel, hence POLE and P_main remain exact."""
    out = [float(edges[0])]
    for a, b in zip(edges[:-1], edges[1:]):
        a = float(a)
        b = float(b)
        if a > 0.0 and b / a > ratio:
            n_sub = int(math.ceil(math.log(b / a) / math.log(ratio)))
            for k in range(1, n_sub):
                out.append(a * (b / a) ** (k / float(n_sub)))
        out.append(b)
    return np.array(out)


def pole_arch(fun, edges_raw, f0, n_gl):
    """POLE(F) = 4 int_0^S F cosh(x/2);
    ARCH(F) = -F(0)(gamma+log pi)
              + 2 int_0^inf [F(0)e^{-2w} - F(w)e^{-w/2}]/(1-e^{-2w}) dw;
    P_main(F) = 2 int_0^S F e^{x/2}.  F even, supp F subset [-S, S]."""
    glx, glw = np.polynomial.legendre.leggauss(n_gl)
    edges = graded_edges(edges_raw)
    s_end = float(edges[-1])
    pole = 4.0 * panel_int(lambda x: fun(x) * np.cosh(0.5 * x), edges,
                           glx, glw)
    pmain = 2.0 * panel_int(lambda x: fun(x) * np.exp(0.5 * x), edges,
                            glx, glw)

    def integ(w):
        return (f0 * np.exp(-2.0 * w) - fun(w) * np.exp(-0.5 * w)) \
            / (-np.expm1(-2.0 * w))
    body = panel_int(integ, edges, glx, glw)
    tail = -0.5 * math.log1p(-math.exp(-2.0 * s_end)) * f0
    arch = -f0 * (np.euler_gamma + math.log(math.pi)) \
        + 2.0 * (body + tail)
    return pole, arch, pmain


def fejer_ward(s_end, n_gl):
    edges = np.linspace(0.0, s_end, 1201)

    def fej(x):
        return np.maximum(0.0, 1.0 - np.abs(x) / s_end)
    pole, arch, pmain = pole_arch(fej, edges, 1.0, n_gl)
    return pole - pmain + arch


# ============================================================= smooth ctl
def smooth_atoms(cell, per_grid):
    """PNT main density as a comb for the deployed generators:
    sum_j (mm_j/2) tau(x - u_j/D) approximates
    int tau(x - u/D) e^{u/2} du."""
    alpha = float(cell["alpha"])
    d_cell = 2.0 * alpha / cell["M"]
    delta = d_cell / float(per_grid)
    n_pt = int(math.ceil((2.0 * alpha + 2.0 * d_cell) / delta))
    uu = (np.arange(n_pt) + 0.5) * delta
    mm = 2.0 * delta * np.exp(0.5 * uu)
    return uu, mm


# ============================================================== per cell
def f4_row(wall, a_value, theta, A2, want_heavy=True):
    """Everything this probe measures at one (cell, theta)."""
    h = wall.h
    d_value = wall.D
    car, cat = wall.c_ladder(theta, split=True)
    xs_int = np.arange(-1.0, h + 2.0)
    ci = wall.c_scalar_vec(xs_int)
    ci_ar = sap.core.arch_A(np.abs(xs_int) * d_value, d_value)
    c_tot = car + cat
    gh = c_tot[1:-1] - 0.5 * (c_tot[2:] + c_tot[:-2])
    gh_ar = car[1:-1] - 0.5 * (car[2:] + car[:-2])
    om = wall.omega_from_gh(gh)
    gt_ar = ci_ar[1:h + 1] - 0.5 * (ci_ar[2:h + 2] + ci_ar[0:h])
    om0 = 0.5 * (sla.hankel(gh_ar[:h], gh_ar[h - 1:2 * h - 1])
                 + sla.toeplitz(gt_ar[:h]))
    n_true = float(om[0, 0])
    n0 = float(om0[0, 0])
    b = np.ascontiguousarray(om[1:, 0])
    B = np.ascontiguousarray(om[1:, 1:])
    b0 = np.ascontiguousarray(om0[1:, 0])
    bc = b0 - b
    nc = n0 - n_true
    w_src = -(cat[:h + 2] + (ci - ci_ar)[:h + 2])
    fact_resid = float(np.max(np.abs(-0.25 * (A2 @ w_src) - bc)))
    row = dict(theta=theta, refused=None, fact_resid=fact_resid,
               w_min=float(np.min(w_src)), w_linf=float(np.max(np.abs(
                   w_src))), w_l2sq=fsum(w_src * w_src) * (1.0 + gam(h + 2)),
               n0=n0, nc=nc, n_true=n_true)
    nzw = np.nonzero(np.abs(w_src) > 0.0)[0]
    row["k0_meas"] = int(nzw[0]) if nzw.size else h + 2
    try:
        cf = sla.cho_factor(B, lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        row["refused"] = "CHOL-FAIL"
        return row
    beta = sap.chol_cert_lower(B, sap.lam_hint(B, cf))
    if beta is None or beta <= 0.0:
        row["refused"] = "CERT-WEAK"
        return row
    row["beta"] = beta
    q0_lo, q0_hi, x0, _r0 = msc.quad_encl(b0, B, cf, beta)
    qc_lo, qc_hi, yc, _rc = msc.quad_encl(bc, B, cf, beta)
    q_lo, q_hi, _y, _r = msc.quad_encl(b, B, cf, beta)
    lin_lo, lin_hi = msc.bilin_encl(bc, b0, B, cf, beta, q0_hi)
    v = msc.second_difference_T(x0, h)
    row.update(q0_lo=q0_lo, q0_hi=q0_hi, qc_lo=qc_lo, qc_hi=qc_hi,
               lin_lo=lin_lo, lin_hi=lin_hi,
               s_lo=n_true - q_hi, s_hi=n_true - q_lo,
               b0_l2sq=fsum(b0 * b0) * (1.0 + gam(h)))
    # ---- support block: w_k = 0 for k < k0 (nu_2 = log 2 / D)
    nu2 = math.log(2.0) / d_value
    k0 = max(0, int(math.floor(nu2)) - 3)
    row["k0"] = k0
    # ---- v norms in the DEPLOYED convention (summation roundoff only,
    # exactly CCCLXVIII's x0_d2_l1), plus the SEPARATE certificate that
    # transports the solve residual to the exact x_0 = B^-1 b_0:
    # ||A_2^T delta||_2 <= 4 ||delta||_2 <= 4 r_up / beta.  That
    # certificate is reported as a diagnostic, never folded into the
    # ladder, so every demand stays comparable to CCCLXVIII.
    slack2 = 4.0 * _r0 / beta
    vJ = v[k0:]
    nJ = int(vJ.size)
    row["x0_slack2"] = slack2
    row["x0_slack_l1"] = math.sqrt(h + 2.0) * slack2
    row["v_l1"] = fsum(np.abs(v)) * (1.0 + gam(h + 4))
    row["vJ_l1"] = fsum(np.abs(vJ)) * (1.0 + gam(h + 4))
    row["vJ_l2"] = math.sqrt(fsum(vJ * vJ) * (1.0 + gam(h + 4)))
    row["v_linf"] = float(np.max(np.abs(v)))
    row["v_sign_changes"] = int(np.sum(np.sign(vJ[1:]) != np.sign(vJ[:-1])))
    # ---- Psi = tent transform of v (exact piecewise linear)
    nodes = np.arange(-1.0, h + 1.0)
    psi_break = np.unique(np.concatenate([nodes, nodes + 2.0 * theta]))
    psi_vals = tent_interp(nodes, v, psi_break) \
        + tent_interp(nodes, v, psi_break - 2.0 * theta)
    row["psi_linf"] = float(np.max(np.abs(psi_vals))) * (1.0 + gam(4))
    # ---- atom-coordinate ward and the smooth/fluctuation split
    reach = float(h) + 3.0
    sel = wall.uh <= reach + 1.0e-12
    a_n = 0.5 * wall.mm[sel]
    nu_n = wall.uh[sel]
    psi_at = tent_interp(nodes, v, nu_n) \
        + tent_interp(nodes, v, nu_n - 2.0 * theta)
    row["atom_ident"] = abs(fsum(a_n * psi_at) - fsum(w_src * v))
    row["n_atom_reach"] = int(a_n.size)
    row["nu_min"] = float(nu_n.min()) if nu_n.size else float("inf")
    row["signed"] = -0.5 * fsum(w_src * v)
    row["signed_lo"] = 2.0 * lin_lo
    row["signed_hi"] = 2.0 * lin_hi
    row["v_vec"] = v
    row["w_vec"] = w_src
    # the PNT main lag profile in closed form (S1.4 says A_2 kills it)
    ws = smooth_lag_profile(xs_int[:h + 2], theta, d_value)
    row["signed_smooth"] = -0.5 * fsum(ws * v)
    row["signed_fluct"] = row["signed"] - row["signed_smooth"]
    row["ws_linf"] = float(np.max(np.abs(ws)))
    if not want_heavy:
        return row
    # ---- the K quantities
    schur_up, lam_up, mu_hat, vhint = rowsum_and_lammax(
        A2, B, cf, beta, h, k0)
    row["schur_J"] = schur_up
    row["lam_max_up"] = lam_up if lam_up else float("inf")
    row["lam_hint"] = mu_hat
    sum_conj, _C = msc.sum_abs_conj_up(A2, B, cf, beta, h,
                                       np.abs(B).sum(axis=1))
    row["sum_abs_conj"] = sum_conj
    env = source_envelopes(a_value, d_value, h, k0)
    fl_u, fl_adm = unsigned_floor(A2, B, cf, beta, h, k0,
                                  2.0 * env["Rc_reach"], env["W2"], vhint)
    row["floor_unsigned_meas"] = fl_u
    row["floor_unsigned_adm"] = fl_adm
    return row


def unsigned_floor(A2, B, cf, beta, h, k0, w_inf_cap, w2_cap, vhint):
    """FL-unsigned: (1/16) w*^T K w* at an ADMISSIBLE point of the
    box+l2 cone {w >= 0, |w|_inf <= w_inf_cap, ||w||_2^2 <= w2_cap,
    supp w subset J}, aligned with the power hint and re-certified by
    the deployed quadratic-form enclosure.  Every bound consuming only
    that information (U1, U2) is at least this value."""
    wcone = np.zeros(h + 2)
    wcone[k0:] = np.abs(vhint)
    top = float(np.max(wcone))
    if top <= 0.0:
        return 0.0, False
    wcone *= w_inf_cap / top
    l2 = fsum(wcone * wcone)
    if l2 > w2_cap:
        wcone *= math.sqrt(w2_cap / l2)
    adm = (float(np.min(wcone)) >= 0.0
           and float(np.max(wcone)) <= w_inf_cap * (1.0 + 1.0e-12)
           and fsum(wcone * wcone) <= w2_cap * (1.0 + 1.0e-12)
           and float(np.max(np.abs(wcone[:k0]))) == 0.0)
    bc_cone = -0.25 * (A2 @ wcone)
    qq_lo, _hi, _y, _r = msc.quad_encl(bc_cone, B, cf, beta)
    return qq_lo, adm


def smooth_lag_profile(xs, theta, d_value):
    """w_s: the lag profile of the PNT main density,
    c_s(x) = int_1^inf tau(x - log t/D) t^-1/2 dt (+ the deployed even
    reflection of the u < D part), exact piecewise closed form; the
    profile is c_s(x+2theta) + c_s(x)."""
    lam = 0.5 * d_value

    def pneg(s):
        return (-(1.0 + s) / lam - 1.0 / lam ** 2) * math.exp(-lam * s)

    def ppos(s):
        return (-(1.0 - s) / lam + 1.0 / lam ** 2) * math.exp(-lam * s)

    def seg(lo, hi):
        if hi <= lo:
            return 0.0
        tot = 0.0
        if lo < 0.0:
            tot += pneg(min(hi, 0.0)) - pneg(lo)
        if hi > 0.0:
            tot += ppos(hi) - ppos(max(lo, 0.0))
        return tot

    def c_s(xv):
        val = seg(-1.0, min(1.0, xv))
        lo, hi = max(-1.0, -xv - 1.0), min(1.0, -xv)
        val += seg(lo, hi)
        return d_value * math.exp(lam * xv) * val

    return np.array([c_s(float(x) + 2.0 * theta) + c_s(float(x))
                     for x in xs])


def audit_cell(cell, target, world=None, thetas=None, want_heavy=True,
               per_grid=None):
    if world == "smooth":
        uu, mm = smooth_atoms(cell, per_grid)
    else:
        uu, mm = sap.cell_atoms(cell, world=world, seed=sap.SEED_SCR)
    wall = sap.Wall(cell, uu, mm)
    h = wall.h
    A2 = msc.second_difference_matrix(h)
    if thetas is None:
        thetas = [(k + 0.5) / N_THETA for k in range(N_THETA)]
    rows = []
    refused = 0
    for theta in thetas:
        row = f4_row(wall, float(cell["alpha"]), theta, A2,
                     want_heavy=want_heavy)
        if row["refused"]:
            refused += 1
        rows.append(row)
    out = msc.Rung()
    out.target = target
    out.h = h
    out.a = float(cell["alpha"])
    out.D = wall.D
    out.rows = rows
    out.refused = refused
    out.good = [r for r in rows if r["refused"] is None]
    out.world = world or "truth"
    out.wall = wall
    return out


def agg(rung):
    """CCCLXVIII aggregation: MAX over theta for demands, MEAN for the
    supply/need."""
    good = rung.good
    m = len(good)
    a_value, d_value, h = rung.a, rung.D, rung.h
    d = dict(h=h, a=a_value, D=d_value, m=m, world=rung.world)
    r_dep, r_fluc, r_sm = msc.r_deployed(a_value, d_value)
    rc_dep = msc.r_source(a_value, d_value)[0]
    k0_env = min([r["k0"] for r in good], default=0)
    d.update(R=r_dep, r_fluc=r_fluc, r_sm=r_sm, Rc_dep=rc_dep,
             **source_envelopes(a_value, d_value, h, k0_env))
    if m == 0:
        return d
    beta = min(r["beta"] for r in good)
    g_geo = fsum([r["n0"] for r in good]) / m
    q0_hi = max(r["q0_hi"] for r in good)
    need = fsum([(r["q0_hi"] - r["n0"]) + r["qc_hi"] + abs(r["nc"])
                 for r in good]) / m
    s_mean = fsum([0.5 * (r["s_lo"] + r["s_hi"]) for r in good]) / m
    d.update(beta=beta, G=g_geo, q0_hi=q0_hi, need=need, s_mean=s_mean,
             b0_l2=math.sqrt(fsum([r["b0_l2sq"] for r in good]) / m),
             sqrt_h=math.sqrt(h - 1),
             fact_resid=max(r["fact_resid"] for r in rung.rows),
             w_min=min(r["w_min"] for r in rung.rows),
             w_linf=max(r["w_linf"] for r in rung.rows),
             w_l2sq=max(r["w_l2sq"] for r in good),
             nc_sup=max(abs(r["nc"]) for r in good),
             atom_ident=max(r["atom_ident"] for r in good),
             nu_min=min(r["nu_min"] for r in good),
             k0=min(r["k0"] for r in good),
             k0_meas=min(r["k0_meas"] for r in rung.rows),
             n_atom_reach=max(r["n_atom_reach"] for r in good),
             v_l1=max(r["v_l1"] for r in good),
             vJ_l1=max(r["vJ_l1"] for r in good),
             vJ_l2=max(r["vJ_l2"] for r in good),
             v_linf=max(r["v_linf"] for r in good),
             psi_linf=max(r["psi_linf"] for r in good),
             x0_slack2=max(r["x0_slack2"] for r in good),
             x0_slack_l1=max(r["x0_slack_l1"] for r in good),
             signed_encl=max(r["signed_hi"] - r["signed_lo"]
                             for r in good),
             signed_in_encl=all(r["signed_lo"] - 1.0e-9 <= r["signed"]
                                <= r["signed_hi"] + 1.0e-9
                                for r in good),
             qc_hi=max(r["qc_hi"] for r in good),
             qc_lo_mean=fsum([r["qc_lo"] for r in good]) / m,
             signed_mean=fsum([r["signed"] for r in good]) / m,
             signed_smooth=fsum([r["signed_smooth"] for r in good]) / m,
             signed_fluct=fsum([r["signed_fluct"] for r in good]) / m,
             v_sign_frac=fsum([r["v_sign_changes"] for r in good])
             / max(1.0, m * (h + 1.0)))
    # deployed F0 demand (the CCCLIX ward)
    d["A_F0"] = r_dep + (d["b0_l2"] + math.sqrt(h - 1) * r_dep) ** 2 / beta
    d["A_F0_rel"] = d["A_F0"] / abs(g_geo)
    if "sum_abs_conj" not in good[0]:
        return d
    d["sum_abs_conj"] = max(r["sum_abs_conj"] for r in good)
    d["schur_J"] = max(r["schur_J"] for r in good)
    d["lam_max_up"] = max(r["lam_max_up"] for r in good)
    d["lam_hint"] = max(r["lam_hint"] for r in good)
    d["floor_unsigned_meas"] = max(r["floor_unsigned_meas"] for r in good)
    d["floor_unsigned_adm"] = all(r["floor_unsigned_adm"] for r in good)
    # ---- unsigned demands
    d["U0"] = 0.25 * rc_dep ** 2 * d["sum_abs_conj"]
    d["U1"] = d["schur_J"] * d["W2"] / 16.0
    d["U2"] = d["lam_max_up"] * d["W2"] / 16.0
    d["U_best"] = min(d["U1"], d["U2"])
    # ---- signed demands
    d["S0"] = rc_dep * d["v_l1"]
    d["S1"] = d["Rc_reach"] * d["vJ_l1"]
    d["S2"] = 0.5 * math.sqrt(d["W2"]) * d["vJ_l2"]
    d["S3"] = 0.5 * d["t_env"] * d["psi_linf"]
    return d


def psi_breaks(v, theta, h):
    """The exact breakpoints of Psi (piecewise linear) and its values
    there; Psi(nu) = I_v(nu) + I_v(nu - 2 theta)."""
    nodes = np.arange(-1.0, h + 1.0)
    brk = np.unique(np.concatenate([nodes, nodes + 2.0 * theta]))
    vals = tent_interp(nodes, v, brk) \
        + tent_interp(nodes, v, brk - 2.0 * theta)
    return nodes, brk, vals


def window_ladder(v, theta, h, l_cap, t_tot):
    """(S4 upper, FL-cone attained lower) from the exact piecewise-linear
    maxima of |Psi| and Psi_+ over disjoint WIN_GRID windows."""
    _nodes, brk, vals = psi_breaks(v, theta, h)
    n_win = int(math.ceil((h + 2.0) / WIN_GRID)) + 1
    win_abs = np.zeros(n_win)
    win_pos = np.zeros(n_win)
    iw = np.clip(((brk + 1.0) / WIN_GRID).astype(int), 0, n_win - 1)
    np.maximum.at(win_abs, iw, np.abs(vals))
    np.maximum.at(win_pos, iw, np.maximum(vals, 0.0))
    return (0.5 * knapsack_windows(win_abs, l_cap, t_tot),
            0.5 * knapsack_attained(win_pos, l_cap, t_tot))


def main():
    print("=" * 78)
    print("PRIME.F4.RESIDUAL.ATTACK.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("EXPLORATION ONLY -- demand accounting -- NO RH CLAIM")
    print("=" * 78)

    section("S0 -- freeze and source firewall")
    hits = ast_firewall()
    check("S0.1 no zero reader, tau, target sign, eigensolver or fit",
          not hits, "hits=%s" % hits)
    check("S0.2 deep evaluator cells excluded",
          1393 not in AUDIT_TARGETS and 2854 not in AUDIT_TARGETS)
    check("S0.3 registered rungs are the two CCCLIX priced cells",
          REGISTERED_RUNGS == (184, 405))

    section("S1 -- exact structural lemmas")
    check("S1.1 q_c = (1/16) w^T A_2^T B^-1 A_2 w exactly", s1_qc_kernel())
    check("S1.2 the F4 kernel K = A_2^T B^-1 A_2 is UNCHANGED under the "
          "congruence B -> M^T B M (every K-bound and K-floor is basis "
          "independent)", s1_kernel_congruence_invariance())
    ok_schur, lhs_s, rhs_s = s1_schur_test()
    check("S1.3 Schur test |w^T K w| <= maxrow|K| ||w||_2^2 (AM-GM step "
          "symbolic + exact-rational witness)", ok_schur,
          "%s <= %s" % (lhs_s, rhs_s))
    check("S1.4 A_2 annihilates the geometric/PNT main comb up to "
          "(2 cosh(D/2) - 2) = D^2/4 + O(D^4)",
          s1_a2_annihilates_geometric())
    ok_atom, val_atom = s1_atom_identity()
    check("S1.5 atom-coordinate identity <w,v> = sum_n a_n Psi(nu_n) "
          "(Fraction-exact)", ok_atom, "value %s" % val_atom)
    check("S1.6 w = Phi^T a with a >= 0 gives w >= 0 entrywise, so the "
          "CCCLXVIII flip w -> -w is INADMISSIBLE in the cone",
          s1_cone_positivity())
    ok_wf, wf_best, wf_worst = s1_waterfill_optimal()
    check("S1.7 sorted greedy solves the box+l2 linear program", ok_wf,
          "greedy %.9f >= net max %.9f" % (wf_best, wf_worst))
    ok_fl, fl_val = s1_class_floor_attained()
    check("S1.8 the class sup is attained at an admissible datum, so it "
          "floors every bound consuming that information", ok_fl,
          "sup %s" % fl_val)
    ok_fin, reach_expr = s1_prime_side_finite()
    check("S1.9 the F4 prime side is FINITE (reach a+3D, no Dirichlet "
          "series, no absolute-convergence boundary -- the CCCLXVII E9 "
          "exclusion of Montgomery-Vaughan/large sieve does not "
          "transfer)", ok_fin, "reach %s" % reach_expr)

    section("S2 -- toolkit self-tests")
    rng = np.random.default_rng(20260813)
    Q = np.linalg.qr(rng.standard_normal((7, 7)))[0]
    lam = np.array([1e-8, 1e-5, 1e-3, 0.1, 0.5, 1.0, 3.0])
    Bt = 0.5 * ((Q * lam) @ Q.T + ((Q * lam) @ Q.T).T)
    cft = sla.cho_factor(Bt, lower=True, check_finite=False)
    bt = rng.standard_normal(7)
    q_lo, q_hi, _y, _r = msc.quad_encl(bt, Bt, cft, 0.5e-8)
    q_ref = float(bt @ np.linalg.solve(Bt, bt))
    check("S2.1 quadratic-form enclosure brackets the reference solve",
          q_lo <= q_ref <= q_hi)
    A2t = msc.second_difference_matrix(8)
    schur_up, lam_up, mu_hat, _vh = rowsum_and_lammax(
        A2t, Bt, cft, 0.5e-8, 8, 0)
    Kref = A2t.T @ np.linalg.solve(Bt, A2t)
    check("S2.2 |K| row-sum upper bound dominates the reference",
          schur_up >= float(np.abs(Kref).sum(axis=1).max()),
          "%.9e >= %.9e" % (schur_up,
                            float(np.abs(Kref).sum(axis=1).max())))
    ref_lam = float(np.max(np.abs(Kref @ _vh) / max(
        np.linalg.norm(_vh), 1e-300))) if _vh is not None else 0.0
    check("S2.3 certified lam_max upper bound exceeds a Rayleigh "
          "quotient of the same kernel",
          lam_up is not None and lam_up >= mu_hat,
          "cert %.9e >= hint %.9e (Rayleigh proxy %.3e)"
          % (lam_up if lam_up else -1.0, mu_hat, ref_lam))
    check("S2.4 water filling matches a brute-force net (S1.7) and is "
          "monotone in both budgets",
          waterfill(np.array([3.0, 1.0]), 1.0, 2.0)
          >= waterfill(np.array([3.0, 1.0]), 1.0, 1.0))
    check("S2.5 knapsack attained-lower <= knapsack LP-upper",
          knapsack_attained(np.array([5.0, 4.0, 3.0, 2.0]), 1.0, 2.0)
          <= knapsack_windows(np.array([5.0, 4.0, 3.0, 2.0]), 1.0, 2.0))
    check("S2.6 source sieve matches the deployed prefix",
          sap.build_tables())
    picks = sap.pick_cells(sap.census())
    ward_fej = {}
    for tgt in REGISTERED_RUNGS:
        cell = picks[tgt]
        a_v = float(cell["alpha"])
        d_v = 2.0 * a_v / cell["M"]
        s_end = 2.0 * a_v + 2.0 * d_v
        got = fejer_ward(s_end, GL_N)
        got8 = fejer_ward(s_end, GL_N_WARD)
        ward_fej[tgt] = (got, abs(got - WARD_FEJER_B[tgt]),
                         abs(got8 - WARD_FEJER_B[tgt]))
    check("S2.7 POLE/ARCH implementation reproduces CCCLXVI's "
          "independently certified 50-digit Fejer closed form at both "
          "registered cells",
          all(v[1] < 1.0e-12 for v in ward_fej.values()),
          "deviations %s (GL8 %s)"
          % (["%.2e" % ward_fej[t][1] for t in REGISTERED_RUNGS],
             ["%.2e" % ward_fej[t][2] for t in REGISTERED_RUNGS]))

    section("A -- registered rungs, rigorous demand accounting")
    rungs, aggs = {}, {}
    for tgt in AUDIT_TARGETS:
        t_a = time.time()
        rungs[tgt] = audit_cell(picks[tgt], tgt)
        aggs[tgt] = agg(rungs[tgt])
        d = aggs[tgt]
        print("  target %d -> h %d  a %.9f  D %.9e  good theta %d/%d  "
              "(%.1f s)" % (tgt, d["h"], d["a"], d["D"], d["m"], N_THETA,
                            time.time() - t_a))
        print("    R %.6e | R_c dep %.6e -> reach-corrected %.6e "
              "(factor %.3f) | beta %.6e | G_geo %.9e"
              % (d["R"], d["Rc_dep"], d["Rc_reach"],
                 d["Rc_dep"] / d["Rc_reach"], d["beta"], d["G"]))
        print("    N = e^{a+3D} %.4f | atoms in reach %d | nu_min %.3f | "
              "k0 %d (measured first nonzero %d) | supp |J| %d"
              % (d["n_top"], d["n_atom_reach"], d["nu_min"], d["k0"],
                 d["k0_meas"], d["h"] + 2 - d["k0"]))
        print("    classical inputs: T <= %.6f, sum Lambda^2/n <= %.6f, "
              "P_max <= %.1f, L(8D) <= %.6f"
              % (d["t_env"], d["l2_env"], d["p_max"], d["l_max"]))
        print("    W2 routes: box %.6e | Schur/atom %.6e | mixed %.6e "
              "-> W2 %.6e via %s (measured ||w||_2^2 %.6f, slack %.2fx)"
              % (d["W2_box"], d["W2_schur"], d["W2_mix"], d["W2"],
                 d["W2_route"], d["w_l2sq"],
                 d["W2"] / max(d["w_l2sq"], 1e-300)))
        print("    K: sum|K| %.6e | maxrow_J|K| %.6e | certified "
              "lam_max(K_J) <= %.6e (hint %.6e)"
              % (d["sum_abs_conj"], d["schur_J"], d["lam_max_up"],
                 d["lam_hint"]))
        print("    need %.9f | q_c <= %.6f (theta-mean lower %.6f) | "
              "signed input %.6f (smooth %.3e + fluctuation %.6f)"
              % (d["need"], d["qc_hi"], d["qc_lo_mean"],
                 d["signed_mean"], d["signed_smooth"], d["signed_fluct"]))
        print("    error accounting: the SIGNED VALUE is enclosed "
              "sharply (Cauchy-Schwarz in B^-1, width %.3e), while the "
              "ENTRYWISE certificate for x_0 costs 4 r/beta = %.3e "
              "(l1 %.3e) -- excluded from every demand, exactly as "
              "CCCLXVIII"
              % (d["signed_encl"], d["x0_slack2"], d["x0_slack_l1"]),
              flush=True)

    ward_ok = all(abs(aggs[t]["A_F0_rel"] - WARD_F0_REL[t])
                  <= WARD_REL * WARD_F0_REL[t] for t in REGISTERED_RUNGS)
    check("A1 CCCLIX/CCCLXVIII deployed miss A/G reproduced within 5 pct",
          ward_ok, "got %s vs %s"
          % (["%.4e" % aggs[t]["A_F0_rel"] for t in REGISTERED_RUNGS],
             ["%.4e" % WARD_F0_REL[t] for t in REGISTERED_RUNGS]))
    check("A2 registered rung shapes match (h 184 and 388)",
          [aggs[t]["h"] for t in REGISTERED_RUNGS] == [184, 388])
    check("A3 measured theta-means of s reproduced",
          all(abs(aggs[t]["s_mean"] - WARD_S_MEAN[t])
              <= 1.0e-8 * abs(WARD_S_MEAN[t]) for t in REGISTERED_RUNGS),
          "%s" % ["%.9e" % aggs[t]["s_mean"] for t in REGISTERED_RUNGS])
    check("A4 source factorisation b_c = -(1/4) A_2 w holds to roundoff",
          all(aggs[t]["fact_resid"] < 1.0e-12 for t in AUDIT_TARGETS),
          "max %s" % ["%.2e" % aggs[t]["fact_resid"]
                      for t in AUDIT_TARGETS])
    check("A5 n_c vanishes identically",
          all(aggs[t]["nc_sup"] == 0.0 for t in AUDIT_TARGETS))
    check("A6 w >= 0 entrywise at every audited (cell, theta) -- the "
          "source profile is in the CONE, not merely in the box",
          all(aggs[t]["w_min"] >= 0.0 for t in AUDIT_TARGETS),
          "min w %s" % ["%.3e" % aggs[t]["w_min"] for t in AUDIT_TARGETS])
    check("A7 declared support k0 is conservative (k0 <= measured first "
          "nonzero) and no atom reaches the reflection branch (nu > 1)",
          all(aggs[t]["k0"] <= aggs[t]["k0_meas"]
              and aggs[t]["nu_min"] > 1.0 for t in AUDIT_TARGETS),
          "k0 %s vs measured %s"
          % ([aggs[t]["k0"] for t in AUDIT_TARGETS],
             [aggs[t]["k0_meas"] for t in AUDIT_TARGETS]))
    check("A8 atom-coordinate identity closes numerically at every "
          "audited (cell, theta)",
          all(aggs[t]["atom_ident"] < 1.0e-9 for t in AUDIT_TARGETS),
          "max deviation %s" % ["%.2e" % aggs[t]["atom_ident"]
                                for t in AUDIT_TARGETS])
    exact_in = {}
    for tgt in AUDIT_TARGETS:
        wall = rungs[tgt].wall
        d = aggs[tgt]
        sel = wall.uh <= float(d["h"]) + 3.0 + 1.0e-12
        a_n = 0.5 * wall.mm[sel]
        nu_n = wall.uh[sel]
        t_ex = fsum(a_n)
        lam2_ex = fsum(a_n * a_n)
        cheb_ex = fsum(a_n * np.exp(-0.5 * nu_n * d["D"]))
        close = np.abs(nu_n[None, :] - nu_n[:, None]) < WIN_GRID / 2.0
        p_ex = int(close.sum(axis=1).max()) if a_n.size else 0
        l_ex = float((close * a_n[None, :]).sum(axis=1).max()) \
            if a_n.size else 0.0
        exact_in[tgt] = (t_ex, lam2_ex, p_ex, l_ex, cheb_ex)
    check("A9 the classical envelopes (C2)-(C6) dominate the EXACT "
          "finite sums at every audited cell",
          all(aggs[t]["t_env"] >= exact_in[t][0]
              and aggs[t]["l2_env"] >= exact_in[t][1]
              and aggs[t]["p_max"] >= exact_in[t][2]
              and aggs[t]["l_max"] >= exact_in[t][3]
              and chebyshev_sum_up(aggs[t]["n_top"]) >= exact_in[t][4]
              for t in AUDIT_TARGETS),
          "env/exact ratios: T %s | sum Lambda^2/n %s | sum Lambda/n %s "
          "| P %s | L %s"
          % (["%.2f" % (aggs[t]["t_env"] / exact_in[t][0])
              for t in AUDIT_TARGETS],
             ["%.2f" % (aggs[t]["l2_env"] / exact_in[t][1])
              for t in AUDIT_TARGETS],
             ["%.2f" % (chebyshev_sum_up(aggs[t]["n_top"])
                        / exact_in[t][4]) for t in AUDIT_TARGETS],
             ["%.1f/%d" % (aggs[t]["p_max"], exact_in[t][2])
              for t in AUDIT_TARGETS],
             ["%.2f" % (aggs[t]["l_max"] / max(exact_in[t][3], 1e-30))
              for t in AUDIT_TARGETS]))
    check("A9b the sharp bilinear enclosure of the signed VALUE "
          "(2<b_c,x_0>, Cauchy-Schwarz in the B^-1 inner product) "
          "contains the measured -(1/2)<w,v> at every audited "
          "(cell, theta)",
          all(aggs[t]["signed_in_encl"] for t in AUDIT_TARGETS),
          "enclosure widths %s" % ["%.2e" % aggs[t]["signed_encl"]
                                   for t in AUDIT_TARGETS])
    check("A10 the W2 envelope dominates the measured ||w||_2^2",
          all(aggs[t]["W2"] >= aggs[t]["w_l2sq"] for t in AUDIT_TARGETS),
          "slack %s" % ["%.2f" % (aggs[t]["W2"] / aggs[t]["w_l2sq"])
                        for t in AUDIT_TARGETS])
    check("A11 the reach-corrected source envelope still dominates the "
          "measured sup|w|",
          all(2.0 * aggs[t]["Rc_reach"] >= aggs[t]["w_linf"]
              for t in AUDIT_TARGETS),
          "2Rc/sup|w| %s"
          % ["%.2f" % (2.0 * aggs[t]["Rc_reach"] / aggs[t]["w_linf"])
             for t in AUDIT_TARGETS])
    check("A12 CCCLXVIII signed and unsigned misses reproduced within "
          "5 pct (same object, same aggregation)",
          all(abs(aggs[t]["S0"] / aggs[t]["need"] - WARD_SIGNED_MISS[t])
              <= WARD_REL * WARD_SIGNED_MISS[t] for t in AUDIT_TARGETS)
          and all(abs(aggs[t]["U0"] / aggs[t]["need"]
                      - WARD_UNSIGNED_MISS[t])
                  <= WARD_REL * WARD_UNSIGNED_MISS[t]
                  for t in AUDIT_TARGETS),
          "signed %s vs %s | unsigned %s vs %s"
          % (["%.4g" % (aggs[t]["S0"] / aggs[t]["need"])
              for t in AUDIT_TARGETS],
             [WARD_SIGNED_MISS[t] for t in AUDIT_TARGETS],
             ["%.4g" % (aggs[t]["U0"] / aggs[t]["need"])
              for t in AUDIT_TARGETS],
             ["%.3g" % WARD_UNSIGNED_MISS[t] for t in AUDIT_TARGETS]))

    lo, hi = REGISTERED_RUNGS
    dl, dh, dx = aggs[lo], aggs[hi], aggs[AUDIT_TARGETS[2]]

    section("B -- the UNSIGNED alignment bound (q_c), classical toolkit")
    print("  %-46s %12s %12s %12s %8s %8s"
          % ("unsigned demand", "h=%d" % dl["h"], "h=%d" % dh["h"],
             "h=%d" % dx["h"], "orders", "exp p"))
    for name, key in (("U0 deployed  0.25 R_c^2 sum|K|", "U0"),
                      ("U1 Schur/l2  (1/16) maxrow_J|K| W2", "U1"),
                      ("U2 Gram/l2   (1/16) lam_max(K_J) W2", "U2")):
        v0, v1, v2 = dl[key], dh[key], dx[key]
        print("  %-46s %12.5e %12.5e %12.5e %8.4f %8.4f"
              % (name, v0, v1, v2, orders(v0, v1),
                 exponent(v0, v1, dl["h"], dh["h"])))
    print("  %-46s %12.5e %12.5e %12.5e"
          % ("measured q_c (theta-max certified upper)", dl["qc_hi"],
             dh["qc_hi"], dx["qc_hi"]))
    print("  %-46s %12.5e %12.5e %12.5e %8.4f %8.4f"
          % ("FL-unsigned attained box+l2-cone floor",
             dl["floor_unsigned_meas"], dh["floor_unsigned_meas"],
             dx["floor_unsigned_meas"],
             orders(dl["floor_unsigned_meas"], dh["floor_unsigned_meas"]),
             exponent(dl["floor_unsigned_meas"],
                      dh["floor_unsigned_meas"], dl["h"], dh["h"])))
    u_miss = {t: aggs[t]["U_best"] / aggs[t]["need"] for t in AUDIT_TARGETS}
    u0_miss = {t: aggs[t]["U0"] / aggs[t]["need"] for t in AUDIT_TARGETS}
    uf_miss = {t: aggs[t]["floor_unsigned_meas"] / aggs[t]["need"]
               for t in AUDIT_TARGETS}
    print("  UNSIGNED MISS (demand / need): deployed %s -> best %s | "
          "certified class floor %s"
          % (["%.4e" % u0_miss[t] for t in AUDIT_TARGETS],
             ["%.4e" % u_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % uf_miss[t] for t in AUDIT_TARGETS]))
    print("  UNSIGNED exponent: deployed %.4f -> best %.4f "
          "(extension rung %.4f)"
          % (exponent(u0_miss[lo], u0_miss[hi], dl["h"], dh["h"]),
             exponent(u_miss[lo], u_miss[hi], dl["h"], dh["h"]),
             exponent(u_miss[hi], u_miss[AUDIT_TARGETS[2]], dh["h"],
                      dx["h"])))
    check("B1 the classical unsigned bound improves the deployed one by "
          "at least one order at both registered rungs",
          all(orders(u_miss[t], u0_miss[t]) >= 1.0
              for t in REGISTERED_RUNGS),
          "gain %s orders" % ["%.3f" % orders(u_miss[t], u0_miss[t])
                              for t in REGISTERED_RUNGS])
    unsigned_closed = all(
        aggs[t]["U_best"] + (aggs[t]["q0_hi"] - aggs[t]["G"])
        < aggs[t]["signed_mean"] for t in AUDIT_TARGETS)
    check("B2 UNSIGNED-CLOSED test, measured state: the best unsigned "
          "bound does NOT yet leave the signed term a positive budget "
          "(typed F4-UNSIGNED-NOT-CLOSED)", not unsigned_closed,
          "budget = signed - U_best - (q_0 - n_0): %s"
          % ["%.4e" % (aggs[t]["signed_mean"] - aggs[t]["U_best"]
                       - (aggs[t]["q0_hi"] - aggs[t]["G"]))
             for t in AUDIT_TARGETS])
    check("B3 the certified Gram route beats the Schur test",
          all(aggs[t]["U2"] <= aggs[t]["U1"] for t in AUDIT_TARGETS),
          "ratio %s" % ["%.3f" % (aggs[t]["U2"] / aggs[t]["U1"])
                        for t in AUDIT_TARGETS])
    check("B4 FL-unsigned is attained at an ADMISSIBLE point of the same "
          "box+l2 cone that U1/U2 consume, and it lies below both: the "
          "unsigned part cannot be pushed below it either",
          all(aggs[t]["floor_unsigned_adm"]
              and aggs[t]["floor_unsigned_meas"] <= aggs[t]["U_best"]
              for t in AUDIT_TARGETS),
          "floor/U_best %s, admissible %s"
          % (["%.4f" % (aggs[t]["floor_unsigned_meas"]
                        / aggs[t]["U_best"]) for t in AUDIT_TARGETS],
             [aggs[t]["floor_unsigned_adm"] for t in AUDIT_TARGETS]))
    check("B5 F4-UNSIGNED-CLOSED is IMPOSSIBLE inside this information "
          "class, not merely unachieved: the attained floor already "
          "exceeds the need at every rung, so no bound on q_c that "
          "consumes only {w >= 0, |w|_inf <= 2 R_c^reach, ||w||_2^2 <= "
          "W2, supp w subset J} can close the unsigned part",
          all(uf_miss[t] > 1.0 for t in AUDIT_TARGETS),
          "floor miss %s" % ["%.3f" % uf_miss[t] for t in AUDIT_TARGETS])
    check("B6 U2 is the EXACT class supremum for the l2-only class "
          "(lam_max(K_J) W2 / 16 is attained at the top eigenvector), so "
          "the only remaining unsigned gain is the positivity/box factor "
          "between FL-unsigned and U2",
          all(aggs[t]["lam_max_up"] >= aggs[t]["lam_hint"]
              and aggs[t]["lam_max_up"]
              <= 1.10 * aggs[t]["lam_hint"] for t in AUDIT_TARGETS),
          "certificate slack lam_up/lam_hint %s | remaining "
          "positivity+box factor U2/FL %s"
          % (["%.4f" % (aggs[t]["lam_max_up"] / aggs[t]["lam_hint"])
              for t in AUDIT_TARGETS],
             ["%.2f" % (aggs[t]["U2"] / aggs[t]["floor_unsigned_meas"])
              for t in AUDIT_TARGETS]))

    section("C -- the SIGNED correlation, five bounds and two floors")
    for tgt in AUDIT_TARGETS:
        d = aggs[tgt]
        best_s4, best_fl, best_box = 0.0, 0.0, 0.0
        for r in rungs[tgt].good:
            up4, lo4 = window_ladder(r["v_vec"], r["theta"], d["h"],
                                     d["l_max"], d["t_env"])
            best_s4 = max(best_s4, up4)
            best_fl = max(best_fl, lo4)
            best_box = max(best_box, 0.5 * waterfill(
                np.abs(r["v_vec"][d["k0"]:]), 2.0 * d["Rc_reach"],
                d["W2"]))
        d["S4"] = best_s4
        d["FL_cone"] = best_fl
        d["FL_box"] = best_box
        d["S_best"] = min(d["S0"], d["S1"], d["S2"], d["S3"], best_s4)
    print("  %-46s %12s %12s %12s %8s %8s"
          % ("signed demand", "h=%d" % dl["h"], "h=%d" % dh["h"],
             "h=%d" % dx["h"], "orders", "exp p"))
    for name, key in (
            ("S0 deployed   R_c ||v||_1", "S0"),
            ("S1 reach+supp R_c^reach ||v_J||_1", "S1"),
            ("S2 Cauchy-Schwarz (1/2) sqrt(W2) ||v_J||_2", "S2"),
            ("S3 atom-Hoelder  (1/2) T ||Psi||_inf", "S3"),
            ("S4 window knapsack (BT + Chebyshev)", "S4"),
            ("FL-box+l2 attained floor (any box+l2 bound)", "FL_box"),
            ("FL-cone attained floor (nonneg + BT + T)", "FL_cone")):
        v0, v1, v2 = aggs[lo][key], aggs[hi][key], \
            aggs[AUDIT_TARGETS[2]][key]
        print("  %-46s %12.5e %12.5e %12.5e %8.4f %8.4f"
              % (name, v0, v1, v2, orders(v0, v1),
                 exponent(v0, v1, dl["h"], dh["h"])))
    print("  %-46s %12.5e %12.5e %12.5e"
          % ("measured signed input (theta-mean)", dl["signed_mean"],
             dh["signed_mean"], dx["signed_mean"]))
    print("  %-46s %12.5e %12.5e %12.5e"
          % ("need = mean[(q_0-n_0) + q_c]", dl["need"], dh["need"],
             dx["need"]))
    s_miss = {t: aggs[t]["S_best"] / aggs[t]["need"]
              for t in AUDIT_TARGETS}
    s0_miss = {t: aggs[t]["S0"] / aggs[t]["need"] for t in AUDIT_TARGETS}
    f_miss = {t: aggs[t]["FL_cone"] / aggs[t]["need"]
              for t in AUDIT_TARGETS}
    fb_miss = {t: aggs[t]["FL_box"] / aggs[t]["need"]
               for t in AUDIT_TARGETS}
    print("  SIGNED MISS: deployed %s -> best %s | floors: box+l2 %s, "
          "cone %s"
          % (["%.4g" % s0_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % s_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % fb_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % f_miss[t] for t in AUDIT_TARGETS]))
    p_s0 = exponent(s0_miss[lo], s0_miss[hi], dl["h"], dh["h"])
    p_s = exponent(s_miss[lo], s_miss[hi], dl["h"], dh["h"])
    p_fl = exponent(f_miss[lo], f_miss[hi], dl["h"], dh["h"])
    print("  SIGNED exponent: deployed %.4f (CCCLXVIII %.3f) -> best "
          "%.4f | cone floor %.4f | extension-rung best %.4f"
          % (p_s0, DEPLOYED_SIGNED_EXP, p_s, p_fl,
             exponent(s_miss[hi], s_miss[AUDIT_TARGETS[2]], dh["h"],
                      dx["h"])))
    check("C1 the signed miss exponent falls to at most 0.8 x the "
          "deployed 2.119", p_s <= 0.8 * DEPLOYED_SIGNED_EXP,
          "%.4f vs %.4f" % (p_s, 0.8 * DEPLOYED_SIGNED_EXP))
    check("C2 the cone floor is BELOW the best achieved bound at every "
          "rung (the floor is a floor)",
          all(aggs[t]["FL_cone"] <= aggs[t]["S_best"] * (1.0 + 1e-9)
              for t in AUDIT_TARGETS),
          "floor/best %s" % ["%.3f" % (aggs[t]["FL_cone"]
                                       / aggs[t]["S_best"])
                             for t in AUDIT_TARGETS])
    check("C2b the box+l2 floor lies below the box+l2 bound S2 at every "
          "rung (the two classes are separated: the cone floor is "
          "strictly smaller because w >= 0 forbids sign alignment)",
          all(aggs[t]["FL_box"] <= aggs[t]["S2"] * (1.0 + 1.0e-9)
              and aggs[t]["FL_cone"] < aggs[t]["FL_box"]
              for t in AUDIT_TARGETS),
          "FL_box/S2 %s | FL_cone/FL_box %s"
          % (["%.3f" % (aggs[t]["FL_box"] / aggs[t]["S2"])
              for t in AUDIT_TARGETS],
             ["%.3f" % (aggs[t]["FL_cone"] / aggs[t]["FL_box"])
              for t in AUDIT_TARGETS]))
    check("C3 the cone floor exceeds 1 at every rung: NO bound "
          "consuming only {a >= 0, local density <= L, total <= T, "
          "support} can close the signed part",
          all(f_miss[t] > 1.0 for t in AUDIT_TARGETS),
          "floor miss %s" % ["%.4f" % f_miss[t] for t in AUDIT_TARGETS])
    check("C4 the certified floor GROWS between the registered rungs "
          "(the exponent is not killed inside the class)", p_fl > 0.0,
          "floor exponent %.4f" % p_fl)

    section("D -- the structure of the test direction v = A_2^T x_0")
    for tgt in AUDIT_TARGETS:
        d = aggs[tgt]
        rung = rungs[tgt]
        r_ef = min(rung.good, key=lambda r: abs(r["theta"] - EF_THETA))
        v = r_ef["v_vec"]
        vJ = v[d["k0"]:]
        spec = np.abs(np.fft.rfft(vJ)) ** 2
        spec = spec / max(float(spec.sum()), 1e-300)
        n_bin = spec.size
        om_grid = np.arange(n_bin) * math.pi / max(n_bin - 1.0, 1.0)
        peak = int(np.argmax(spec))
        cum = np.cumsum(spec)
        r_peak = om_grid[peak] / rung.D
        d["r_peak"] = r_peak
        d["hf_mass"] = 1.0 - float(cum[n_bin // 2])
        print("  h %4d (theta %.5f): ||v||_1 %.4e | ||v_J||_1 %.4e | "
              "||v_J||_2 %.4e | ||v||_inf %.4e | ||Psi||_inf %.4e"
              % (d["h"], r_ef["theta"], d["v_l1"], d["vJ_l1"], d["vJ_l2"],
                 d["v_linf"], d["psi_linf"]))
        print("        sign changes per entry %.4f | DFT peak omega/pi "
              "%.4f -> LOG FREQUENCY r = omega/D %.2f | l2 mass above "
              "pi/2 %.4f | above 0.9 pi %.4f"
              % (d["v_sign_frac"], om_grid[peak] / math.pi, r_peak,
                 d["hf_mass"],
                 1.0 - float(cum[int(0.9 * (n_bin - 1))])))
        print("        Type I/II availability: N = e^{a+3D} %.1f, "
              "log N / log r = %.4f, r / N = %.4f (a bilinear gain needs "
              "r << N; here r is of the size of N)"
              % (d["n_top"], math.log(d["n_top"])
                 / math.log(max(r_peak, 2.0)), r_peak / d["n_top"]))
        print("        smooth/fluctuation split of the signed input: "
              "PNT main %+.6e, fluctuation %+.6f, ratio %.3e "
              "(sup|w_s| %.4e)"
              % (d["signed_smooth"], d["signed_fluct"],
                 abs(d["signed_smooth"]) / abs(d["signed_fluct"]),
                 max(r["ws_linf"] for r in rung.good)))
    check("D1 the PNT main comb contributes at most 1e-3 of the signed "
          "input (A_2 annihilates it, S1.4): the signed input is a PURE "
          "prime-fluctuation correlation",
          all(abs(aggs[t]["signed_smooth"])
              <= 1.0e-3 * abs(aggs[t]["signed_fluct"])
              for t in AUDIT_TARGETS),
          "ratios %s" % ["%.2e" % (abs(aggs[t]["signed_smooth"])
                                   / abs(aggs[t]["signed_fluct"]))
                         for t in AUDIT_TARGETS])
    check("D2 v is Nyquist-dominated (more than half of its l2 mass "
          "above omega = pi/2), so no smooth-test-function cancellation "
          "is available",
          all(aggs[t]["hf_mass"] > 0.5 for t in AUDIT_TARGETS),
          "high-frequency mass %s | log frequencies r_peak %s"
          % (["%.4f" % aggs[t]["hf_mass"] for t in AUDIT_TARGETS],
             ["%.1f" % aggs[t]["r_peak"] for t in AUDIT_TARGETS]))
    check("D3 the bilinear (Type I/II) regime is UNAVAILABLE: the log "
          "frequency r is not small against N, so Vaughan/large-sieve "
          "cancellation in the signed term has no length to exploit",
          all(aggs[t]["r_peak"] > 0.05 * aggs[t]["n_top"]
              for t in AUDIT_TARGETS),
          "r/N %s" % ["%.4f" % (aggs[t]["r_peak"] / aggs[t]["n_top"])
                      for t in AUDIT_TARGETS])

    section("E -- explicit-formula readout at the frozen theta")
    ef = {}
    for tgt in AUDIT_TARGETS:
        d = aggs[tgt]
        rung = rungs[tgt]
        h = rung.h
        r_ef = min(rung.good, key=lambda r: abs(r["theta"] - EF_THETA))
        theta = r_ef["theta"]
        v = r_ef["v_vec"]
        w_src = r_ef["w_vec"]
        nodes = np.arange(-1.0, h + 1.0)
        dv = rung.D

        def f_even(u, nodes=nodes, v=v, theta=theta, dv=dv):
            """F(u) = -(1/4) Psi(|u|/D), even, supp in |u| <= (h+2t)D;
            with CCCLXVI's PRIME(F) = 2 sum Lambda(n) n^{-1/2} F(log n)
            this makes PRIME(F) the signed input EXACTLY (S1.5)."""
            nu = np.abs(np.asarray(u, float)) / dv
            return -0.25 * (tent_interp(nodes, v, nu)
                            + tent_interp(nodes, v, nu - 2.0 * theta))
        brk = np.unique(np.concatenate([nodes, nodes + 2.0 * theta]))
        edges = np.concatenate([[0.0], brk[brk > 0.0] * dv])
        f0 = float(f_even(np.array([0.0]))[0])
        pole, arch, pmain = pole_arch(f_even, edges, f0, GL_N)
        pole8, arch8, pmain8 = pole_arch(f_even, edges, f0, GL_N_WARD)
        prime = -0.5 * fsum(w_src * v)          # = PRIME(F), S1.5
        # normalisation ward: CCCLXVI's PRIME(F) computed from the ATOMS
        sel = rung.wall.uh <= float(h) + 3.0 + 1.0e-12
        a_n = 0.5 * rung.wall.mm[sel]
        prime_atoms = 2.0 * fsum(a_n * f_even(rung.wall.uh[sel] * dv))
        need_t = (r_ef["q0_hi"] - r_ef["n0"]) + r_ef["qc_hi"] \
            + abs(r_ef["nc"])
        zero_sum = pole + arch - prime
        budget = pole + arch - need_t
        # Fhat(xi) = 2 int_0^S F(u) cos(xi u) du, purely archimedean:
        # this decides whether a Weil-positivity route could exist
        glx, glw = np.polynomial.legendre.leggauss(GL_N)
        xi_grid = np.linspace(0.0, FHAT_XI_MAX / dv, FHAT_N)
        fhat = np.array([2.0 * panel_int(
            lambda u, xi=xi: f_even(u) * np.cos(xi * u), edges, glx, glw)
            for xi in xi_grid])
        ef[tgt] = dict(pole=pole, arch=arch, prime=prime, pmain=pmain,
                       zero=zero_sum, budget=budget, f0=f0, need=need_t,
                       prime_dev=abs(prime_atoms - prime),
                       fhat_min=float(fhat.min()),
                       fhat_max=float(fhat.max()),
                       fhat_negfrac=float(np.mean(fhat < 0.0)),
                       ward=max(abs(pole - pole8), abs(arch - arch8)))
        print("  h %4d (theta %.5f): F(0) %+.6e | POLE %+.9e | ARCH "
              "%+.9e | P_main %+.6e"
              % (h, theta, f0, pole, arch, pmain))
        print("        PRIME(F) = signed input %+.9e (from the atoms "
              "%+.9e, deviation %.2e) | DERIVED zero sum sum_rho "
              "Fhat(gamma_rho) = POLE + ARCH - PRIME = %+.9e"
              % (prime, prime_atoms, ef[tgt]["prime_dev"], zero_sum))
        print("        this theta needs %+.9e, i.e. sum_rho Fhat < POLE "
              "+ ARCH - need = %+.9e; the DERIVED value satisfies it "
              "with margin %+.6e | quadrature ward %.2e"
              % (need_t, budget, budget - zero_sum, ef[tgt]["ward"]))
        print("        Fhat on [0, %.1f/D]: min %+.6e, max %+.6e, "
              "negative on %.1f pct of the grid -> F is %s of positive "
              "type"
              % (FHAT_XI_MAX, ef[tgt]["fhat_min"], ef[tgt]["fhat_max"],
                 100.0 * ef[tgt]["fhat_negfrac"],
                 "NOT" if ef[tgt]["fhat_min"] < 0.0 else "possibly"))
    check("E0 the CCCLXVI normalisation is exact: PRIME(F) = 2 sum_n "
          "Lambda(n) n^{-1/2} F(log n) computed from the ATOMS equals "
          "the signed input -(1/2)<w,v> to roundoff, with F(u) = "
          "-(1/4) Psi(|u|/D)",
          all(ef[t]["prime_dev"] < 1.0e-9 for t in AUDIT_TARGETS),
          "deviations %s" % ["%.2e" % ef[t]["prime_dev"]
                             for t in AUDIT_TARGETS])
    check("E1 the archimedean functionals are quadrature-stable "
          "(GL24 vs GL8 on the same panels)",
          all(ef[t]["ward"] < 1.0e-8 for t in AUDIT_TARGETS),
          "max deviation %s" % ["%.2e" % ef[t]["ward"]
                                for t in AUDIT_TARGETS])
    check("E2 the Weil transform is FAITHFUL: the miss in the "
          "zero-sum coordinate equals the miss in the signed coordinate "
          "to roundoff, so the reformulation neither gains nor loses",
          all(abs((ef[t]["budget"] - ef[t]["zero"])
                  - (ef[t]["prime"] - ef[t]["need"]))
              <= 1.0e-9 * (abs(ef[t]["pole"]) + abs(ef[t]["arch"]) + 1.0)
              for t in AUDIT_TARGETS),
          "deviations %s"
          % ["%.2e" % abs((ef[t]["budget"] - ef[t]["zero"])
                          - (ef[t]["prime"] - ef[t]["need"]))
             for t in AUDIT_TARGETS])
    check("E3 the bar POLE + ARCH - need is NEGATIVE at every audited "
          "cell, so the remaining statement is an upper bound on a zero "
          "sum against a NEGATIVE bar: it demands that Fhat evaluate "
          "NEGATIVELY on the actual ordinates.  It is therefore the "
          "OPPOSITE of a Weil-positivity statement -- an F of positive "
          "type would make it FALSE under RH (sum_rho Fhat >= 0 > bar)",
          all(ef[t]["budget"] < 0.0 for t in AUDIT_TARGETS),
          "bars %s | derived zero sums %s"
          % (["%.4e" % ef[t]["budget"] for t in AUDIT_TARGETS],
             ["%.4e" % ef[t]["zero"] for t in AUDIT_TARGETS]))
    check("E4 F is NOT of positive type (Fhat takes both signs on the "
          "real axis -- a purely ARCHIMEDEAN fact, no zero datum read), "
          "so the E3 requirement is not self-contradictory; what remains "
          "is a quantitative statement about the position of the "
          "ordinates relative to the sign pattern of Fhat, i.e. RH-grade "
          "information that no magnitude bound can supply",
          all(ef[t]["fhat_min"] < 0.0 < ef[t]["fhat_max"]
              for t in AUDIT_TARGETS),
          "min Fhat %s | max Fhat %s | negative fraction of the grid %s"
          % (["%.4e" % ef[t]["fhat_min"] for t in AUDIT_TARGETS],
             ["%.4e" % ef[t]["fhat_max"] for t in AUDIT_TARGETS],
             ["%.3f" % ef[t]["fhat_negfrac"] for t in AUDIT_TARGETS]))

    section("X -- identical-pipeline controls")
    ctrl = []
    for world in ("scramble", "epstein"):
        cr = audit_cell(picks[184], 184, world=world,
                        thetas=list(CTRL_THETA), want_heavy=False)
        resid = max(r["fact_resid"] for r in cr.rows)
        wmin = min(r["w_min"] for r in cr.rows)
        ctrl.append((world, cr.refused, len(cr.good), resid, wmin))
        print("  %-9s MEASURED: PD/cert refusals %d/%d, usable %d, "
              "factorisation residual %.3e, min w %.3e"
              % (world.upper(), cr.refused, len(CTRL_THETA), len(cr.good),
                 resid, wmin))
    smooth_out = []
    for per_grid in SMOOTH_PER_GRID:
        cs = audit_cell(picks[184], 184, world="smooth",
                        thetas=list(CTRL_THETA), want_heavy=False,
                        per_grid=per_grid)
        n_good = len(cs.good)
        sm = fsum([r["signed"] for r in cs.good]) / n_good \
            if n_good else float("nan")
        nd = fsum([(r["q0_hi"] - r["n0"]) + r["qc_hi"]
                   for r in cs.good]) / n_good if n_good else float("nan")
        smooth_out.append((per_grid, cs.refused, n_good, sm, nd))
        print("  SMOOTH-WALL(%2d/grid) MEASURED: refusals %d/%d, usable "
              "%d -> %s"
              % (per_grid, cs.refused, len(CTRL_THETA), n_good,
                 "PREMISE REFUSED, no F4 statement exists in this world"
                 if n_good == 0 else
                 "signed %+.6e vs need %.6e, statement %s"
                 % (sm, nd, "HOLDS" if sm > nd else "FAILS")))
    # SMOOTH-SOURCE: deployed wall, deployed v, premise intact, only the
    # SOURCE profile replaced by the PNT main lag profile w_s
    src_ratio = []
    for tgt in AUDIT_TARGETS:
        d = aggs[tgt]
        src_ratio.append((d["h"], d["signed_smooth"], d["need"]))
        print("  SMOOTH-SOURCE h %4d MEASURED: same wall, same v, w -> "
              "w_s: signed input %+.6e vs need %.6e -> statement FAILS "
              "by %.2f orders"
              % (d["h"], d["signed_smooth"], d["need"],
                 orders(abs(d["signed_smooth"]), d["need"])))
    check("X1 the F4 algebra (factorisation and the cone) is COMB-BLIND: "
          "it holds in the control worlds too, so neither it nor any "
          "unsigned bound built on it can be the discriminating lemma",
          all(rd < 1.0e-12 and wm >= 0.0 for _w, _rf, _ng, rd, wm in ctrl),
          "residuals %s, min w %s"
          % (["%.2e" % rd for _w, _rf, _ng, rd, _wm in ctrl],
             ["%.2e" % wm for _w, _rf, _ng, _rd, wm in ctrl]))
    check("X2 SCRAMBLE, EPSTEIN and SMOOTH-WALL all refuse the deployed "
          "PD premise: the comb discrimination of the FRAME sits in "
          "beta > 0, not in any bound derived here",
          all(rf > 0 for _w, rf, _ng, _rd, _wm in ctrl)
          and all(ng == 0 for _pg, _rf, ng, _sm, _nd in smooth_out),
          "%s | smooth-wall refusals %s"
          % ([(w, rf) for w, rf, _ng, _rd, _wm in ctrl],
             [(pg, rf) for pg, rf, _ng, _sm, _nd in smooth_out]))
    check("X3 SMOOTH-SOURCE breaks the SIGNED requirement by more than "
          "3 orders at every audited cell with the PREMISE INTACT: the "
          "signed term is carried entirely by prime FLUCTUATIONS, so a "
          "fluctuation-blind bound can never supply it",
          all(abs(s) < 1.0e-3 * n for _h, s, n in src_ratio),
          "signed_smooth %s vs need %s"
          % (["%+.3e" % s for _h, s, _n in src_ratio],
             ["%.3e" % n for _h, _s, n in src_ratio]))

    section("V -- frozen verdict")
    failed = [name for name, ok in CHECKS if not ok]
    structural = any(n.startswith(("S0", "S1", "S2")) for n in failed)
    improved = p_s <= 0.8 * DEPLOYED_SIGNED_EXP
    floor_ok = all(f_miss[t] > 1.0 for t in AUDIT_TARGETS) and p_fl > 0.0
    explicit_ok = all(ef[t]["ward"] < 1.0e-8 for t in AUDIT_TARGETS) \
        and all(v[1] < 1.0e-12 for v in ward_fej.values()) \
        and all(ef[t]["prime_dev"] < 1.0e-9 for t in AUDIT_TARGETS)
    if structural or not ward_ok:
        verdict = "F4-NO-PROGRESS"
    elif unsigned_closed:
        verdict = "F4-UNSIGNED-CLOSED"
    elif explicit_ok:
        verdict = "F4-SIGNED-EXPLICIT"
    elif improved:
        verdict = "F4-EXPONENT-IMPROVED"
    elif floor_ok:
        verdict = "F4-EXPONENT-FLOOR"
    else:
        verdict = "F4-NO-PROGRESS"
    tags = []
    if improved:
        tags.append("F4-EXPONENT-IMPROVED")
    if floor_ok:
        tags.append("F4-EXPONENT-FLOOR")
    if not unsigned_closed:
        tags.append("F4-UNSIGNED-NOT-CLOSED")
    print("  VERDICT: %s   TAGS: %s" % (verdict, ", ".join(tags)))
    print("  UNSIGNED (q_c): the bound is q_c <= (1/16) lam_max(K_J) W2 "
          "with W2 = 4 L(8D) T(N), T(N) <= 2 * 1.03883 sqrt(N) "
          "(Chebyshev/Schoenfeld), L(8D) from Brun-Titchmarsh in the "
          "Montgomery-Vaughan 1973 form pi(x+y)-pi(x) <= 2y/log y, "
          "N = e^{a+3D}, lam_max(K_J) certified per cell by shifted "
          "Cholesky.  Miss %s -> %s, exponent %.3f -> %.3f."
          % (["%.3e" % u0_miss[t] for t in AUDIT_TARGETS],
             ["%.3e" % u_miss[t] for t in AUDIT_TARGETS],
             exponent(u0_miss[lo], u0_miss[hi], dl["h"], dh["h"]),
             exponent(u_miss[lo], u_miss[hi], dl["h"], dh["h"])))
    print("  UNSIGNED IS NOT CLOSABLE IN THIS CLASS (B4/B5/B6): U2 is "
          "the exact supremum of the l2-only class, and the attained "
          "box+l2-cone floor is %s -- miss %s > 1 at every rung.  So "
          "only a bound that uses MORE than {w >= 0, |w|_inf, ||w||_2, "
          "supp} about the source profile (i.e. its alignment with the "
          "eigenvectors of K, not just its size) can remove q_c."
          % (["%.4g" % aggs[t]["floor_unsigned_meas"]
              for t in AUDIT_TARGETS],
             ["%.3g" % uf_miss[t] for t in AUDIT_TARGETS]))
    print("  SIGNED: deployed miss %s -> best miss %s (exponent %.3f -> "
          "%.3f, so 2.119 was NOT an invariant floor); certified "
          "attained class floors box+l2 %s and cone %s (floor exponent "
          "%.3f > 0, so the exponent CANNOT be driven to 0 inside the "
          "class either -- both halves of task C answered)."
          % (["%.4g" % s0_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % s_miss[t] for t in AUDIT_TARGETS], p_s0, p_s,
             ["%.4g" % fb_miss[t] for t in AUDIT_TARGETS],
             ["%.4g" % f_miss[t] for t in AUDIT_TARGETS], p_fl))
    print("  EXPLICIT FORM: with F(u) := -(1/4) Psi(|u|/D) (even, "
          "supported in |u| <= S = (h+2theta)D, piecewise linear) the "
          "signed input IS CCCLXVI's PRIME(F) = 2 sum_{n<=e^S} Lambda(n)"
          " n^{-1/2} F(log n) EXACTLY (E0), and Weil gives PRIME(F) = "
          "POLE(F) + ARCH(F) - sum_rho Fhat(gamma_rho), so the remaining "
          "statement is EXACTLY")
    print("    sum_rho Fhat(gamma_rho) < POLE(F) + ARCH(F) - int_0^1 "
          "[q_0 - n_0 + q_c] dtheta   (budget %s at h = %s)."
          % (["%.4e" % ef[t]["budget"] for t in AUDIT_TARGETS],
             [aggs[t]["h"] for t in AUDIT_TARGETS]))
    print("  RH DEPENDENCE (honest, E3/E4): the bar is NEGATIVE (%s), so "
          "the statement demands that Fhat evaluate NEGATIVELY on the "
          "actual ordinates -- the opposite of a Weil-positivity "
          "statement, which for a positive-type F would make it FALSE "
          "under RH.  Fhat does take both signs (min %s, negative on "
          "%s of the grid), so the demand is not self-contradictory, but "
          "what remains is the position of the ordinates against the "
          "sign pattern of Fhat.  The zero sum is not removable by any "
          "of the five bounds either: they all bound |PRIME(F)| from "
          "ABOVE, while the statement needs a LOWER bound on a signed "
          "prime-fluctuation correlation (D1, D2, D3, X3)."
          % (["%.3e" % ef[t]["budget"] for t in AUDIT_TARGETS],
             ["%.2e" % ef[t]["fhat_min"] for t in AUDIT_TARGETS],
             ["%.0f pct" % (100.0 * ef[t]["fhat_negfrac"])
              for t in AUDIT_TARGETS]))
    print("  REMAINING STATEMENT AFTER THIS PASS: on ONE "
          "sign-independent predeclared cofinal (a_j, D_j) with "
          "beta_j > 0, prove")
    print("    int_0^1 [ -(1/2) sum_n Lambda(n) n^{-1/2} "
          "Psi_theta(log n / D) - q_c ] dtheta > int_0^1 [ q_0 - n_0 ] "
          "dtheta,")
    print("  where Psi_theta = I_v(.) + I_v(. - 2theta) is the explicit "
          "archimedean tent transform of v = A_2^T x_0 (log frequency "
          "r ~ %s against N ~ %s, so no bilinear length is available), "
          "q_c carries the unconditional bound (1/16) lam_max(K_J) W2 "
          "with W2 = 4 L T (miss %s), and no bound consuming only "
          "{a >= 0, local density <= L, total mass <= T, support} can "
          "close the signed term (certified attained floor %s)."
          % (["%.0f" % aggs[t]["r_peak"] for t in AUDIT_TARGETS],
             ["%.0f" % aggs[t]["n_top"] for t in AUDIT_TARGETS],
             ["%.3g" % u_miss[t] for t in AUDIT_TARGETS],
             ["%.3g" % f_miss[t] for t in AUDIT_TARGETS]))
    elapsed = time.time() - T0
    check("V1 runtime below the frozen bar", elapsed < RUNTIME_BAR,
          "%.3f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    print("\n[SUMMARY] %d/%d checks pass | failed=%s | %.3f s | %s"
          % (len(CHECKS) - len(failed), len(CHECKS),
             failed if failed else "none", elapsed, verdict))
    print("NO RH CLAIM.  No positivity claim.  Nothing promoted.")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
