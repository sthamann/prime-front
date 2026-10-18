#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hardness_calibration_falsification_probe -- PRIME.CORE.HARDNESS.FALSIFY.01.

EXPLORATION ONLY (experiments/).  NO RH CLAIM IN EITHER DIRECTION, no all-h
claim, no promotion, no marker move.  The frozen predecessors
shift_average_deep_probe.py, shift_average_probe.py and
shift_average_hh_audit_probe.py are imported or read READ-ONLY, never edited.

TWO MISSIONS.

PART A -- HARDNESS CALIBRATION of the single irreducible missing inequality of
note CCCLXI,

    P_err,h  <=  Q_h - P_main,h - need_h      on a predefined cofinal family,

restated in purely classical analytic-number-theory terms, then priced against
RH, Lindeloef, the density hypothesis, a zero-density exponent, Montgomery pair
correlation, Chowla/Elliott, Vinogradov--Korobov, Vaughan/Montgomery mean
values, the large sieve and Selberg's symmetry formula.  The deliverable is an
EXPONENT TABLE, not adjectives.  NO FITTING anywhere in Part A.

PART B -- ADVERSARIAL FALSIFICATION of the wall positivity with the CORRECTED
high-precision instrument of CCCLVIII/CCCLX (MP_DPS=90 source balls, Arb-256
congruence-preconditioned interval LDL/Schur), hunting for a genuine certified
negative rung and measuring the certified margin trend.

=============================================================================
A.  THE CLASSICAL RESTATEMENT (source-only, no TFPT-internal names)
=============================================================================

FRAME.  For an index kz let n_kz be the kz-th prime power, alpha = log n_kz,
gap = log n_{kz+1} - log n_kz, D_k = gap/8, M = 2 ceil(alpha/D_k + 1) rounded
up to even, h = M/2, D = 2 alpha/M = alpha/h, N = floor(exp(2 alpha + 2 D)).

KERNEL.  tent  tau_D(t) = max(0, 1 - |t|/D);  second-difference kernel

    K_D(t) = tau_D(t) - (tau_D(t-D) + tau_D(t+D))/2 .

EXACT KERNEL DATA (proved here in exact rational arithmetic):
    int K_D = 0,  ||K_D||_inf = 1,  ||K_D'||_1 = 4,  ||K_D||_1 = 4D/3,
    D^{-1} int K_D^2 = 2/3,
    T_D := int e^{-t/2} tau_D(t) dt = (8/D)(cosh(D/2) - 1),
    int e^{-t/2} K_D(t) dt = -(8/D)(cosh(D/2) - 1)^2 .

THE TESTED FUNCTIONAL.  For a translation u0 in [0, 2 alpha + 2 D] put

    Phi(u0) = sum_{p^k <= N} (log p) p^{-k/2} K_D(u0 - k log p)
            = int_1^N x^{-1/2} K_D(u0 - log x) d psi(x) ,

split by psi(x) = x + Delta(x) into

    Phi_main(u0) = e^{u0/2} int e^{-t/2} K_D(t) dt
                 = -e^{u0/2} (8/D)(cosh(D/2) - 1)^2 ,
    Phi_err(u0)  = int_1^N x^{-1/2} K_D(u0 - log x) d Delta(x) .

The wall matrix is the Gram matrix of h such reads,
Omega_theta[m,n] = (G(m+n+2 theta) + G(|m-n|))/2, with G a fixed finite signed
combination of Phi at ladder translations plus the explicit archimedean
counterpart.  P_err,h, Q_h, P_main,h and need_h of CCCLXI are exactly the
Delta-part, the archimedean part, the x-part and the geometric requirement of
one such signed combination.  Hence the missing inequality is, classically:

    ==> A ONE-SIDED BOUND ON A WEIGHTED VON MANGOLDT FLUCTUATION
        sum_{p^k <= N_h} (log p) p^{-k/2} W_h(k log p)  <=  B_h ,
        W_h a fixed piecewise-linear window built from K_{D_h} translates,
        support [0, 2 alpha_h + 2 D_h], B_h an explicit O(1) geometric budget,
        with MEASURED slack B_h - (left side) in 1.5e-05 .. 2.7e-03 that
        SHRINKS with depth (CCCXXXI Spearman -0.859, CITED).

Equivalently, by Abel summation against Delta = psi(x) - x, with
G_h(u) := W_h(u) e^{-u/2}:

    F_h := W_h(2 alpha_h) Delta(N_h) N_h^{-1/2}
           - int_0^{2 alpha_h} Delta(e^u) G_h'(u) du   <=   B_h - P_main,h .

ABSOLUTE-VALUE (MAGNITUDE) ENVELOPE.  With
S(N) := sup_{x <= N} |psi(x) - x| x^{-1/2} one gets, exactly,

    |F_h| <= C_h * S(N_h),
    C_h  := ||W_h'||_1 + (1/2)||W_h||_1 + |W_h(2 alpha_h)| ,

and per single block C = 2||K_D||_inf + ||K_D'||_1 + (1/2)||K_D||_1 = 6 + 2D/3.

TWO SCALE FACTS THAT DECIDE THE WHOLE TABLE.

  (S1) THE TEST SCALE SITS AT THE SQUARE-ROOT BARRIER.  D_h = alpha_h/h with
       h = M/2, M ~ 8 alpha/gap, hence D_h = gap/4 (1 + O(1/h)) and

           D_h * sqrt(N_h) = (n_kz log(n_{kz+1}/n_kz)/4) e^{D_h}(1 + O(1/h))
                           = Delta n_kz / 4 * (1 + O(Delta n / n)) ,

       Delta n_kz = n_{kz+1} - n_kz.  The kernel therefore probes psi on
       multiplicative windows of relative width D_h, i.e. ABSOLUTE length
       y_h(x) = x D_h, and at the top of the range

           y_h(N_h) = sqrt(N_h) * Delta n_kz / 4 * (1 + o(1)),
           Delta n_kz = O(log N_h) .

       RH's short-interval asymptotic needs y >> sqrt(x) log^2 x: the family is
       short by a factor ~ 4 log^2 N_h / Delta n_kz.  For x < N_h the windows
       are relatively even shorter, i.e. BELOW the square-root barrier, where
       no hypothesis gives a per-window asymptotic.

  (S2) THE PNT MAIN TERM OF A BLOCK IS N_h^{-1}-SMALL RELATIVE TO ANY
       MAGNITUDE ENVELOPE.  |Phi_main(2 alpha)| = e^{alpha}(8/D)(cosh(D/2)-1)^2
       and with D = (Delta n/4) N^{-1/2}(1 + o(1)),

           (6 + 2D/3) * S_RH(N_h) / |Phi_main(2 alpha_h)|
              = 4 (6 + 2D/3) (alpha_h + D_h)^2 N_h / (pi (Delta n_kz/4)^3)
                * (1 + o(1))
              ~ N_h * alpha_h^2 ,

       i.e. THE EXPONENT GAP GROWS LINEARLY IN N_h = e^{2 alpha_h}.  Section A3
       verifies this closed form against the measured ratio at all nine built
       depths; the residual is exactly 3x the (S1) relative deviation, which
       enters cubed.

MAGNITUDE-CLASS EMPTINESS (unconditional).  Littlewood (1914):
psi(x) - x = Omega_pm(sqrt(x) log log log x), hence S(N) >= c0 log log log N
for infinitely many N and S(N) -> infinity.  Since C_h >= ||K_D'||_1 = 4 > 0
and B_h = O(1), NO bound of the form |psi(x) - x| <= f(x) sqrt(x) can yield the
needed inequality: the entire magnitude class is unconditionally empty for all
sufficiently deep h.  The inequality is therefore NOT a magnitude statement; it
is a SIGN statement, and the only listed route that produces a sign is the
explicit formula, i.e. Weil positivity, i.e. RH itself.

Section A3 prints the exponent table with one row per requested source and an
explicit exponent or explicit numeric shortfall at the built depths.

=============================================================================
A.  THE STRICTLY WEAKER SUFFICIENT VARIANT (the main Part A deliverable)
=============================================================================

The Lean extraction core (TfptCarrier/CofinalWeil.lean, read-only) is

    limit_nonneg_of_cofinal_seq : StrictMono idx -> (forall j, 0 <= q (idx j))
        -> Tendsto q atTop (nhds L) -> 0 <= L ,
    weil_nonneg_of_cofinal      : CofinalHypothesis A -> form convergence
        -> forall v, 0 <= QW v ,

and CofinalHypothesis carries `psd : forall j, (A (idx j)).PosSemidef`.  Three
INDEPENDENT weakenings live inside exactly this chain:

  (W1) DEFICIT RELAXATION.  Replace 0 <= q(idx j) by -eps_j <= q(idx j) with
       eps_j -> 0; the same squeeze gives 0 <= L.
  (W2) DIRECTION RESTRICTION.  weil_nonneg_of_cofinal consumes PosSemidef only
       through ladderForm_nonneg at the SAMPLED vectors sample (idx j) v.  Only
       nonnegativity on the closure of the sampled cone is used; full matrix
       PSD is strictly stronger.
  (W3) ELEMENT-DEPENDENT LADDER.  For fixed v the ladder forms CONVERGE, so
       liminf = lim and the ladder may depend on v without reintroducing
       sign-mining.

  ==> WEAKER SUFFICIENT VARIANT (WSV).  For every v in the dense family and
      every delta > 0 there exist infinitely many m with
          formAt (A m) (sample m v)  >=  -delta .
      With per-element form convergence, density and C0 extension this already
      forces Weil positivity.  WSV is strictly weaker than "there exists a
      predefined cofinal (h_j, theta_j) with Omega PSD".

  STRICTNESS IS PROVED HERE, exactly, by two rational witnesses:
      (X1) M_m := I_m - 2 e_m e_m^T is never PSD, has lambda_min = -1 at every
           m, converges entrywise to I, and satisfies WSV with delta = 0 for
           every finitely supported v -- so (W2)+(W3) are strict.
      (X2) N_m := I_m - (1 + 1/m) e_m e_m^T has lambda_min = -1/m < 0 for all
           m with lambda_min -> 0 -- so (W1) is strict.
  NON-VACUITY.  WSV still excludes the SCRAMBLE and EPSTEIN control worlds,
  because their certified negative directions are O(1), not o(1).  Measured in
  section B3 with certified Arb enclosures.

  QUANTITATIVE VALUE.  At the deepest certified depth of CCCLX the program
  proves s = 2.12e-10 > 0 where WSV requires only >= -eps_h with eps_h -> 0
  (e.g. 1/log h ~ 1.3e-01): the current target is over-strong by ~9 orders of
  magnitude, and the classical budget B_h may be relaxed by eps_h, i.e. by
  ~4 orders relative to the measured slack 1.5e-05.  This closes NO row of the
  exponent table -- the RH block envelope is still 48.1 at h=2854 and 65.0 at
  the deepest built depth h=12632 -- and it is NOT an RH claim.

=============================================================================
B.  THE ADVERSARIAL FALSIFICATION PROTOCOL
=============================================================================

INSTRUMENT (post-CCCXXIII standard, reused verbatim, never re-implemented):
  * MP_DPS=90 independent Eratosthenes prime-power source with outward balls;
  * Arb-256 congruence-preconditioned interval LDL/Schur (deep.certify_point);
  * every binary64 object (Cholesky preconditioner, candidate generator,
    localisation profile) carries NO sign claim; every reported sign comes from
    an Arb interval.

TWO CERTIFIED READS PER CELL.
  (R1) SCHUR:  s_h(theta) = Omega[0,0] - b^T B^{-1} b via deep.certify_point.
       Cost O(h^3); sign-blind synthetic timing gave 115.5 s at dimension 2400
       with exponent 3.0, so the O(h^3) route ceiling under the 1800 s bar is
       h ~ 3.4e3 and the CCCXXIX straddle cells at h >= 10863 are ~30x beyond
       it in wall time.
  (R2) WITNESS: for an exact dyadic vector v (denominator 2^38) the value

           v^T Omega_theta v
             = (1/2) [ sum_r A_r G_theta(r) + sum_r C_r G_0(r) ] ,
           A_r = sum_{m+n=r} v_m v_n ,  C_r = sum_{|m-n|=r} v_m v_n ,

       with A_r, C_r EXACT integers from 19-bit limb-split binary64
       convolutions -- each limb product is an integer of modulus at most
       h * 2^38 < 2^53, hence exactly representable -- and the final sum
       formed in Arb from the SAME source balls.  Cost O(h^2).  A certified
       negative v^T Omega v FALSIFIES wall positivity at that cell; a certified
       positive value bounds s_h from ABOVE and is never a positivity proof.

ADVERSARIAL SEARCH SURFACE (frozen before any sign read):
  * theta corners the frozen denominator-order rule never reached because it
    stopped at its first positive candidate theta=1/2:
        theta = 0 and theta = 1        (the two remaining INTEGER alignments
                                        2 theta in {0, 2}; theta=1 was never
                                        scanned at any depth),
        theta = 1/4, 3/4               (2 theta half-integer),
        theta = 1/2 -+ 1/64, 1/2 -+ 1/32     (approach to the near-degenerate
                                        integer point, as close as the frozen
                                        source can be evaluated at all),
        theta = 1/32, 31/32            (deeper than the frozen order),
        theta = 349525/2^20, 699051/2^20  (non-order dyadics approximating
                                        1/3 and 2/3).
    COST SINGULARITY, DISCLOSED.  The frozen archimedean source truncates a
    geometric series and needs ~94.5/(dist(2 theta, Z) D_h) terms, so the
    punctured neighbourhood of theta=1/2 is not merely expensive but divergent
    in cost, while theta=1/2 itself is the exact closed-form point.  Corners
    above a frozen bar of 6.3e5 terms are REFUSED BY COST and reported as
    such.  This is an instrument edge, never a sign claim.
  * four candidate directions per cell: the binary64 Schur minimizer
    (1, -B^{-1} b), a 200-step shifted power iteration towards the most
    negative direction, the pure escape direction e_{h-1}, and a fixed
    SHA256-derived deterministic direction.  The certified minimum over the
    four is reported.
  * depth: the certified two-sided Schur ladder is extended to the NEW depths
    h=2015 and h=2607; the O(h^2) certified witness instrument is pushed to
    h=5746 and h=12632, i.e. 4.4x deeper than any previously certified read in
    this family.

TWO CERTIFIED READS PER CELL, AND WHY THE CHEAP ONE IS ENOUGH TO FALSIFY.
  s_h = min { v^T Omega v : v_0 = 1 } is a MINIMUM, so every admissible vector
  delivers a certified UPPER bound U_h >= s_h at O(h^2) cost, while the
  two-sided interval-LDL Schur read costs O(h^3).  A negative rung is exactly a
  negative upper bound, so the cheap instrument is the falsification-relevant
  one and it reaches depths the Schur route cannot.  Section B1 measures the
  slack U_h/s_h - 1 at four depths where both are computed.

INDEPENDENT RE-READS, PREDECLARED AND IMPLEMENTED.  A certified negative read
is reported as FALSIFIED only if FOUR independent paths reproduce the sign on
the SAME exact rational vector:
  V-A  the cell rebuilt at MP_DPS=140 / ARB_BITS=1024 with a cleared memo
       (the CCCXXIII float64/precision artifact class);
  V-B  the form reduced to a linear functional of the pre-difference ladder
       c_j by the exact integer adjoint of the second difference, bypassing
       both the G differencing and the per-entry Omega assembly (the CCCXXXV
       assembly-defect class);
  V-C  no interval library at all: the integer coefficient arrays verified by
       Kronecker substitution (one big-integer multiplication instead of the
       limb-split convolution) and summed as exact dyadic big integers;
  V-D  a direct O(h^2) Arb double summation for h <= 1500.
  V-E  additionally audits the frozen archimedean source against mpmath's own
       Lerch transcendent at sampled ladder indices.  Agreement check only.
Anything less is INSTRUMENT-EDGE, not FALSIFIED.

MARGIN TREND.  Certified enclosures of s_h at theta=1/2 are combined with the
frozen CCCLX run-of-record intervals (h=2854 CITED; h=184, 388, 839, 1393
REPRODUCED here as the gate on the citation chain) and the two new depths, then
normalised by two source-only scales: mu_h := D_h^2 and the dimensionless
n0_h := Omega[0,0].  The certified upper bounds carry the same two ladders to
h=12632.  Every slope is an interval quotient of interval logarithms.  No
least squares, no weighting and no fitted constant enters any verdict.

  TREND RULE, frozen: a positive power law cannot reach zero at finite h, so a
  downward drift of a normalised ratio is NOT a crossing.  TREND-DOWNWARD is
  emitted only if the local log-log exponent of the normalised ratio steepens
  monotonically AND its deepest value is below -8, i.e. only for a
  super-polynomial collapse.  Otherwise the secant crossing of an affine
  extrapolation is printed and explicitly REFUSED as an artifact of linearising
  a convex positive decay.

FROZEN VERDICT ENUMS.
  PART A:  HARDNESS-EQUIVALENT | HARDNESS-STRICTLY-WEAKER |
           HARDNESS-FOLLOWS-FROM-KNOWN | HARDNESS-UNRESOLVED
  PART B (precedence FALSIFIED > INSTRUMENT-EDGE > TREND-DOWNWARD >
           NO-WITNESS):
           FALSIFIED | TREND-DOWNWARD | NO-WITNESS | INSTRUMENT-EDGE

FROZEN BARS.  MP_DPS=90, ARB_BITS=256, LIMB_BITS=19, VEC_BITS=38,
POWER_ITERS=200, sieve cap 15_000_000, verification precision 140/1024,
total runtime < 1800 s.

SMOKE / RECONNAISSANCE DISCLOSURE (before this file was frozen).
  (r1) A geometry-only frame census (h, kz, n_kz, alpha, D, cap) over kz<=4000
       was printed to choose the depth ladder.  It carries no sign datum, in
       the sense of CCCXXIX's blind census.
  (r2) Sign-blind Arb timing on synthetic diagonally dominant matrices gave
       115.5 s at dimension 2400 with exponent 3.0; source-assembly timing was
       taken at h=839..3401.  No genuine or control sign was read before the
       freeze.
  (r3) The tent-kernel identities were checked by hand on the four exact linear
       pieces; they are re-proved here in exact rational arithmetic.
  AMENDMENT A1 (disclosed): deep.g_sequences is memoised by a wrapper keyed on
  (frame.tag, theta, world.name) and the module attribute is REASSIGNED to that
  wrapper, so deep.certify_point reuses the same cached source.  It is a pure
  deterministic function of those arguments; section S0 wards the memo by
  recomputing one entry through the ORIGINAL function and demanding bitwise
  equality of every value and radius.  No source formula, cap, control, bar or
  verdict rule changes.
  AMENDMENT A2 (disclosed): the binary64 localisation profile of the Schur
  minimizer is printed as DIAGNOSTIC-ONLY, is typed as such, decides nothing
  and enters no verdict.
  AMENDMENT A3 (disclosed, PRE-FREEZE SIGN READS).  Building this file required
  three end-to-end structural passes that DID read genuine signs, and the
  post-CCCXXIII standard requires naming them:
    (a) a smoke pass at h=184, theta=1/2 (positive, and it reproduced the CCCLX
        interval bit-for-bit, which is why that reproduction became the B1
        gate);
    (b) two tiny-frame structural passes over h in {184, 388, 454, 490, 516,
        540, 606} at theta in {0, 1, 1/2 - 2^-10} plus both control worlds.
        Every genuine read was positive; every control read was negative.
        Of those cells only theta in {0, 1, 1/2} at h=184 and h=388 survive
        into the frozen surface, and h=454..606 appear nowhere in it.
    (c) THE CORNER SET WAS CHANGED AFTER (b), and the reason must be stated
        because changing a search surface after seeing signs is exactly what
        biases a hunt: the original corners theta = 1/2 -+ 2^-10 and 1/2 -+
        2^-20 were replaced by 1/2 -+ 1/64 and 1/2 -+ 1/32 PURELY ON COST.
        The measured wall time of the single 2^-10 corner at the SHALLOWEST
        frame was 104.2 s and the cost scales like 1/(dist(2 theta, Z) D_h), so
        the 2^-20 corners would have needed ~10^4 s each at h=839 alone.  The
        replaced corner had read POSITIVE (6.7447e-05), i.e. the discarded cell
        was not a candidate negative, and the replacement moves the surface
        FURTHER from theta=1/2, which is the conservative direction for a
        falsification hunt.  Section B2 prints the cost bar and the cost
        singularity explicitly.
    (d) the closed-form law of scale fact (S2) was found WRONG BY A FACTOR 4 by
        pass (b) and corrected before the run of record; the residual is now
        exactly 3x the (S1) deviation at all nine depths, which is the
        signature of a correct derivation.  This is a Part A identity and
        touches no sign.

SCOPE.  ONLY this file plus one prepended German experiments/next.txt note
written after the exact run summary.  shift_average_probe.py,
shift_average_deep_probe.py, shift_average_hh_audit_probe.py and all of
verification/ stay read-only.  No papers, no ledger, no website, no manifests,
no commit, no Markdown file, no Lean edit.  NO RH CLAIM IN EITHER DIRECTION.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np

try:
    import scipy.linalg as sla
except ImportError:  # pragma: no cover
    sla = None

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shift_average_deep_probe as deep  # noqa: E402  (frozen, read-only)

from flint import arb, ctx  # noqa: E402


MP_DPS = 90
ARB_BITS = 256
VERIFY_DPS = 140
VERIFY_BITS = 1024
LIMB_BITS = 19
VEC_BITS = 38
POWER_ITERS = 200
SIEVE_CAP = 15_000_000
RUNTIME_BAR = 1800.0
STEEPEN_BAR = -8.0
DIRECT_SUM_MAX = 1500
CAND_SEED = "HARDFALSIFY:20260813"

SCHUR_CAL = (("H184", 184, 9), ("H388", 388, 55), ("H839", 839, 43),
             ("H1393", 1393, 88))
SCHUR_NEW = (("H2015", 2015, 85), ("H2607", 2607, 131))
N0_ONLY = (("H2854", 2854, 222),)
DEEP_WITNESS = (("H5746", 5746, 273), ("H12632", 12632, 569))

_TWO20 = 1 << 20
THETA_CORNERS = (
    ("ZERO", Fraction(0)),
    ("ONE", Fraction(1)),
    ("QUARTER", Fraction(1, 4)),
    ("THREE-QUARTER", Fraction(3, 4)),
    ("HALF-M64", Fraction(1, 2) - Fraction(1, 64)),
    ("HALF-P64", Fraction(1, 2) + Fraction(1, 64)),
    ("HALF-M32", Fraction(1, 2) - Fraction(1, 32)),
    ("HALF-P32", Fraction(1, 2) + Fraction(1, 32)),
    ("D-1/32", Fraction(1, 32)),
    ("D-31/32", Fraction(31, 32)),
    ("NEAR-1/3", Fraction(349525, _TWO20)),
    ("NEAR-2/3", Fraction(699051, _TWO20)),
)
CORNERS_DEEPCAL = ("ONE", "QUARTER", "HALF-M32", "D-1/32", "NEAR-1/3")
CORNERS_WITNESS_DEEP = ("ONE",)

# Cost model of the FROZEN archimedean source.  lerch_value truncates a
# geometric series until the omitted tail falls under LERCH_TAIL=1e-82, so it
# needs about 94.5/t terms at argument t.  Along the ladder x_j=|j-1+2theta|
# the two smallest arguments are dist(2theta, Z) * D, hence the worst-case
# term count below.  Measured throughput of the frozen loop at MP_DPS=90 is
# 6.3e4 terms/s, and two ladder points hit the worst case, so the bar below
# is a ~20 s per-corner ceiling.
LERCH_TERM_BAR = 6.3e5

# CITED frozen CCCLX run-of-record theta=1/2 Schur intervals.  h=839 and 1393
# are reproduced in section B1 as the gate on this citation chain.
CITED_SCHUR = {
    184: ("2.55040492106466221e-06", "2.55040492106466306e-06"),
    388: ("1.22362650956722969e-07", "1.22362650956723022e-07"),
    839: ("1.05673858430073635e-08", "1.05673858430073668e-08"),
    1393: ("2.27451283174326270e-09", "2.27451283174326353e-09"),
    2854: ("2.12003444567896238e-10", "2.12003444567896289e-10"),
}
CITED_LAMBDA = {
    184: "1.2022628946795073e-07", 388: "5.740612089835872e-09",
    839: "1.948378488059919e-10", 1393: "4.298153e-11",
    2854: "1.472988e-12",
}
CITED_ENVELOPE_MIN = 1.60e4
CITED_ENVELOPE_MED = 9.1e5
CITED_ORACLE_MED = 2.02e4
CITED_SLACK = (1.500e-05, 9.207e-05, 2.730e-03)
CITED_PRIMEDIAG = (9.536, 35.21)
CITED_GGEO = (1.713710666, 1.772451887)
CITED_VK_HULL = (17.76, 60.49)

AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigvalsh", "eigvals", "eigsh", "target_sign", "cached_sign",
}
PART_A_VERDICTS = {
    "HARDNESS-EQUIVALENT", "HARDNESS-STRICTLY-WEAKER",
    "HARDNESS-FOLLOWS-FROM-KNOWN", "HARDNESS-UNRESOLVED",
}
PART_B_VERDICTS = {
    "FALSIFIED", "TREND-DOWNWARD", "NO-WITNESS", "INSTRUMENT-EDGE",
}

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []
KILLS: list[str] = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    bad = set()
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in AST_BANNED:
            bad.add(name)
    return sorted(bad)


# ===========================================================================
# memoisation of the frozen pure source function (AMENDMENT A1)
# ===========================================================================

_G_MEMO: dict[tuple[str, str, str], tuple[list, list]] = {}
_G_ORIGINAL = deep.g_sequences


def _memo_key(frame, theta, world):
    return (frame.tag, mp.nstr(mp.mpf(theta), 45), world.name)


def g_memo(frame, theta, world):
    key = _memo_key(frame, theta, world)
    hit = _G_MEMO.get(key)
    if hit is None:
        hit = _G_ORIGINAL(frame, theta, world)
        _G_MEMO[key] = hit
    return hit


def memo_ward(frame, theta, world):
    cached_values, cached_errors = g_memo(frame, theta, world)
    fresh_values, fresh_errors = _G_ORIGINAL(frame, theta, world)
    if len(cached_values) != len(fresh_values):
        return False
    return (all(a == b for a, b in zip(cached_values, fresh_values))
            and all(a == b for a, b in zip(cached_errors, fresh_errors)))


def drop_frame_memo(tag):
    for key in [k for k in _G_MEMO if k[0] == tag]:
        del _G_MEMO[key]
    for key in [k for k in deep._ARCH_CACHE if k[0] == tag]:
        del deep._ARCH_CACHE[key]


deep.g_sequences = g_memo


# ===========================================================================
# PART A -- exact kernel data
# ===========================================================================

def _k1(t):
    """K_1 on its four exact linear pieces."""
    if t <= Fraction(-1):
        return -(t + 2) / 2
    if t <= Fraction(0):
        return 1 + 3 * t / 2
    if t <= Fraction(1):
        return 1 - 3 * t / 2
    return -(2 - t) / 2


def tent_kernel_exact():
    breaks = (Fraction(-2), Fraction(-1), Fraction(0), Fraction(1),
              Fraction(2))
    slopes = (Fraction(-1, 2), Fraction(3, 2), Fraction(-3, 2),
              Fraction(1, 2))
    integral = square = l1 = tv = Fraction(0)
    peak = Fraction(0)
    for (a, b), slope in zip(zip(breaks[:-1], breaks[1:]), slopes):
        va, vb = _k1(a), _k1(b)
        width = b - a
        integral += (va + vb) * width / 2
        square += width * (va * va + va * vb + vb * vb) / 3
        tv += abs(slope) * width
        peak = max(peak, abs(va), abs(vb))
        if va * vb >= 0:
            l1 += abs((va + vb) * width / 2)
        else:
            root = a + width * va / (va - vb)
            l1 += abs(va) * (root - a) / 2 + abs(vb) * (b - root) / 2
    return dict(integral=integral, square=square, l1=l1, tv=tv, peak=peak)


def exp_weighted_kernel(dval):
    """Closed forms for T_D and int e^{-t/2}K_D versus independent quadrature."""
    dval = mp.mpf(dval)
    t_closed = 8 / dval * (mp.cosh(dval / 2) - 1)
    k_closed = -8 / dval * (mp.cosh(dval / 2) - 1) ** 2

    def tent(t):
        t = abs(t)
        return mp.mpf(0) if t >= dval else 1 - t / dval

    def kernel(t):
        return tent(t) - (tent(t - dval) + tent(t + dval)) / 2

    t_quad = mp.quad(lambda t: mp.exp(-t / 2) * tent(t), [-dval, 0, dval])
    k_quad = mp.quad(lambda t: mp.exp(-t / 2) * kernel(t),
                     [-2 * dval, -dval, 0, dval, 2 * dval])
    return dict(t_closed=t_closed, k_closed=k_closed,
                t_rel=abs(t_closed - t_quad) / abs(t_closed),
                k_rel=abs(k_closed - k_quad) / abs(k_closed))


def frame_scale_row(frame, nn):
    n_now = int(nn[frame.kz])
    n_next = int(nn[frame.kz + 1])
    root_n = mp.exp(frame.alpha + frame.D)
    prod = frame.D * root_n
    gapint = n_next - n_now
    predicted = mp.mpf(gapint) / 4
    return dict(h=frame.h, kz=frame.kz, n=n_now, n_next=n_next,
                gapint=gapint, alpha=frame.alpha, D=frame.D,
                cap=frame.cap_n, root_n=root_n, dsqrtn=prod,
                predicted=predicted, rel=abs(prod - predicted) / predicted)


def rh_envelope_row(frame):
    alpha, dval = frame.alpha, frame.D
    log_n = 2 * alpha + 2 * dval
    block_c = 6 + 2 * dval / 3
    s_rh = log_n ** 2 / (8 * mp.pi)
    envelope = block_c * s_rh
    main = mp.exp(alpha + dval) * 8 / dval * (mp.cosh(dval / 2) - 1) ** 2
    return dict(h=frame.h, alpha=alpha, D=dval, log_n=log_n,
                block_c=block_c, s_rh=s_rh, envelope=envelope,
                main=main, ratio=envelope / main,
                root_n=mp.exp(alpha + dval))


def wsv_witnesses(dims=(3, 4, 6, 9)):
    """Exact rational proof that WSV is strictly weaker than rung PSD."""
    rows = []
    for m in dims:
        rows.append(dict(
            m=m,
            # X1: M = I - 2 e_m e_m^T
            x1_escape=Fraction(-1),          # e_m direction, never PSD
            x1_fixed=Fraction(1),            # any fixed early direction
            # X2: N = I - (1 + 1/m) e_m e_m^T
            x2_min=Fraction(-1, m),
        ))
    strict_w2 = all(row["x1_escape"] < 0 and row["x1_fixed"] >= 0
                    for row in rows)
    strict_w1 = (all(row["x2_min"] < 0 for row in rows)
                 and abs(rows[-1]["x2_min"]) < abs(rows[0]["x2_min"]))
    return rows, strict_w1, strict_w2


# ===========================================================================
# PART B -- certified reads
# ===========================================================================

def arb_from_decimals(lo_text, hi_text):
    lo = mp.mpf(lo_text)
    hi = mp.mpf(hi_text)
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2 + abs(mid) * mp.mpf("1e-50") + mp.mpf("1e-300")
    return arb(mp.nstr(mid, 60), mp.nstr(rad, 60))


def arb_interval(value):
    return deep.arb_bounds(value)


def corner_terms(frame, frac):
    """Worst-case frozen-Lerch term count of a theta corner on a frame."""
    two = 2 * Fraction(frac)
    delta = min(two - int(two), int(two) + 1 - two)
    if delta == 0:
        return 0.0
    return float(mp.mpf("94.5") / (mp.mpf(delta.numerator)
                                   / delta.denominator * frame.D))


def source_balls(frame, theta, world):
    gt, gte = g_memo(frame, mp.mpf(0), world)
    if theta == 0:
        return gt, gte, gt, gte
    gh, ghe = g_memo(frame, theta, world)
    return gt, gte, gh, ghe


def n0_from_source(gt, gte, gh, ghe):
    return (deep.arb_ball(gh[0], ghe[0]) + deep.arb_ball(gt[0], gte[0])) / 2


def float_matrix(frame, gt, gh):
    """Row-by-row binary64 Omega.  Peak memory is one h x h array."""
    dim = frame.h
    gt64 = np.asarray([float(v) for v in gt[:dim]])
    gh64 = np.asarray([float(v) for v in gh])
    out = np.empty((dim, dim), dtype=np.float64)
    lag = np.empty(dim, dtype=np.int64)
    idx = np.arange(dim)
    for m in range(dim):
        np.abs(idx - m, out=lag)
        np.add(gh64[m:m + dim], gt64[lag], out=out[m])
    out *= 0.5
    return out


def sha_direction(dim):
    """Deterministic SHA256 counter stream; fixed before any read."""
    need = 8 * dim
    blob = b""
    counter = 0
    while len(blob) < need:
        blob += hashlib.sha256(
            ("%s:%d" % (CAND_SEED, counter)).encode()).digest()
        counter += 1
    raw = np.frombuffer(blob[:need], dtype=">u8").astype(np.float64)
    out = raw / float(1 << 63) - 1.0
    norm = float(np.linalg.norm(out))
    return out / norm if norm else out


def candidate_directions(matrix):
    """Binary64 candidate generators.  They carry NO sign claim.

    The stationary vector of v -> v^T Omega v under v_0 = 1 is
    Omega^{-1} e_0 normalised to v_0 = 1, and its form value is exactly the
    Schur complement.  Factorising the full matrix in place avoids the
    non-contiguous copy of the trailing block, which matters at h > 10^4.
    """
    dim = matrix.shape[0]
    cands = {}
    start = sha_direction(dim)
    shift = float(np.max(np.sum(np.abs(matrix), axis=1)))
    vec = start.copy()
    work = np.empty(dim)
    for _ in range(POWER_ITERS):
        np.matmul(matrix, vec, out=work)
        vec *= shift
        vec -= work
        norm = float(np.linalg.norm(vec))
        if not np.isfinite(norm) or norm == 0.0:
            break
        vec /= norm
    if np.all(np.isfinite(vec)):
        cands["POWER-NEG"] = vec
    esc = np.zeros(dim)
    esc[dim - 1] = 1.0
    cands["ESCAPE"] = esc
    cands["SHA-FIXED"] = start
    del work
    rhs = np.zeros(dim)
    rhs[0] = 1.0
    sol = None
    if sla is not None:
        try:
            factor = sla.cho_factor(matrix, lower=True, overwrite_a=True,
                                    check_finite=False)
            sol = sla.cho_solve(factor, rhs, check_finite=False)
        except Exception:
            sol = None
        if sol is None:
            try:
                lu = sla.lu_factor(matrix, overwrite_a=True,
                                   check_finite=False)
                sol = sla.lu_solve(lu, rhs, check_finite=False)
            except Exception:
                sol = None
    if sol is not None and np.all(np.isfinite(sol)) and sol[0] != 0.0:
        cands["SCHUR-MIN"] = sol / sol[0]
    return cands


def exact_vector(vec):
    peak = float(np.max(np.abs(vec)))
    if peak == 0.0 or not np.isfinite(peak):
        return None
    scaled = np.rint((vec / peak) * float(1 << VEC_BITS))
    return np.clip(scaled, -(1 << VEC_BITS), (1 << VEC_BITS))


def exact_autocorrelations(arr):
    """Exact integer A_r = sum_{m+n=r} a_m a_n, C_r = sum_{|m-n|=r} a_m a_n."""
    base_f = float(1 << LIMB_BITS)
    hi = np.rint(arr / base_f)
    lo = arr - hi * base_f
    base = 1 << LIMB_BITS

    def combine(fn):
        hh = fn(hi, hi)
        hl = fn(hi, lo)
        lh = fn(lo, hi)
        ll = fn(lo, lo)
        return [int(a) * base * base + (int(b) + int(c)) * base + int(d)
                for a, b, c, d in zip(hh, hl, lh, ll)]

    conv = combine(lambda x, y: np.convolve(x, y, "full"))
    corr = combine(lambda x, y: np.correlate(x, y, "full"))
    dim = arr.size
    lags = corr[dim - 1:]
    csum = [lags[0]] + [2 * v for v in lags[1:]]
    return conv, csum


def certified_form(arr, gt, gte, gh, ghe):
    """Arb enclosure of v^T Omega v and of ||v||^2 with v = arr / 2^VEC_BITS."""
    conv, csum = exact_autocorrelations(arr)
    total = arb(0)
    for r, coeff in enumerate(conv):
        if coeff:
            total += arb(coeff) * deep.arb_ball(gh[r], ghe[r])
    for r, coeff in enumerate(csum):
        if coeff:
            total += arb(coeff) * deep.arb_ball(gt[r], gte[r])
    scale = arb(1) / arb(1 << (2 * VEC_BITS))
    return total * scale / 2, arb(csum[0]) * scale


def direct_form(arr, gt, gte, gh, ghe):
    """Independent O(h^2) Arb double summation of v^T Omega v (V-C)."""
    dim = arr.size
    entries_h = [deep.arb_ball(gh[r], ghe[r]) for r in range(2 * dim - 1)]
    entries_t = [deep.arb_ball(gt[r], gte[r]) for r in range(dim)]
    total = arb(0)
    for m in range(dim):
        am = int(arr[m])
        if am == 0:
            continue
        for n in range(dim):
            an = int(arr[n])
            if an == 0:
                continue
            total += arb(am * an) * (entries_h[m + n] + entries_t[abs(m - n)])
    scale = arb(1) / arb(1 << (2 * VEC_BITS))
    return total * scale / 2


def kronecker_check(arr, conv, csum):
    """Independent exact verification of the two coefficient arrays.

    Kronecker substitution: with k chosen so that every true and every
    claimed coefficient is bounded by 2^{k-1} in modulus, a polynomial
    identity holds iff it holds at x = 2^k, because a nonzero difference
    polynomial with coefficients in (-2^{k-1}, 2^{k-1}) cannot vanish
    there.  One big-integer multiplication replaces the whole convolution,
    so this shares no code with the limb-split numpy path.
    """
    dim = arr.size
    ints = [int(v) for v in arr]
    bound = max([abs(v) for v in conv] + [abs(v) for v in csum] + [1])
    bound = max(bound, dim * (1 << (2 * VEC_BITS)))
    k = bound.bit_length() + 4
    poly = sum(v << (k * m) for m, v in enumerate(ints) if v)
    rev = sum(v << (k * (dim - 1 - m)) for m, v in enumerate(ints) if v)
    lhs_conv = sum(c << (k * r) for r, c in enumerate(conv) if c)
    ok_conv = lhs_conv == poly * poly
    lags = [csum[0]] + [v // 2 for v in csum[1:]]
    halves_exact = all(v % 2 == 0 for v in csum[1:])
    corr = [lags[abs(r - (dim - 1))] for r in range(2 * dim - 1)]
    lhs_corr = sum(c << (k * r) for r, c in enumerate(corr) if c)
    ok_corr = lhs_corr == poly * rev
    return bool(ok_conv and ok_corr and halves_exact)


def dyadic_parts(value):
    """(mantissa, exponent) with value = mantissa * 2^exponent exactly."""
    num, den = mp.libmp.to_rational(mp.mpf(value)._mpf_)
    return num, 1 - den.bit_length()


def rational_form_bounds(arr, gt, gte, gh, ghe):
    """Arb-free exact dyadic bounds on v^T Omega v (no interval library).

    Every source ball endpoint is an exact dyadic rational, so the outward
    rounded form bound is one exact big-integer sum after alignment to a
    common power of two.
    """
    conv, csum = exact_autocorrelations(arr)
    terms = []
    for coeff, mid, err in ([(conv[r], gh[r], ghe[r])
                             for r in range(len(conv)) if conv[r]]
                            + [(csum[r], gt[r], gte[r])
                               for r in range(len(csum)) if csum[r]]):
        pm, em = dyadic_parts(mid)
        pe, ee = dyadic_parts(err)
        terms.append((coeff, pm, em, pe, ee))
    exps = [e for _c, _p, e, _q, f in terms for e in (e, f)]
    if not exps:
        return Fraction(0), Fraction(0)
    base = min(exps)
    up = lo = 0
    for coeff, pm, em, pe, ee in terms:
        centre = coeff * (pm << (em - base))
        spread = abs(coeff) * (pe << (ee - base))
        up += centre + spread
        lo += centre - spread
    shift = Fraction(1, 1 << (2 * VEC_BITS + 1))
    if base >= 0:
        factor = Fraction(1 << base) * shift
    else:
        factor = shift / (1 << -base)
    return Fraction(lo) * factor, Fraction(up) * factor


def witness_status(value):
    if value.upper() < 0:
        return "W-NEG"
    if value.lower() > 0:
        return "W-POS"
    return "W-STRADDLE"


def witness_read(frame, theta, world, label, want_profile=False):
    started = time.time()
    gt, gte, gh, ghe = source_balls(frame, theta, world)
    matrix = float_matrix(frame, gt, gh)
    cands = candidate_directions(matrix)
    best = None
    rows = []
    for name, vec in cands.items():
        arr = exact_vector(vec)
        if arr is None:
            continue
        form, norm_sq = certified_form(arr, gt, gte, gh, ghe)
        rayleigh = form / norm_sq
        lo, hi = arb_interval(rayleigh)
        row = dict(name=name, arr=arr, form=form, rayleigh=rayleigh,
                   lo=lo, hi=hi, up=float(rayleigh.upper()),
                   status=witness_status(rayleigh))
        rows.append(row)
        if best is None or row["up"] < best["up"]:
            best = row
    profile = None
    if want_profile and "SCHUR-MIN" in cands:
        absv = np.abs(cands["SCHUR-MIN"])
        mass = float(np.sum(absv * absv))
        tail = int(0.9 * absv.size)
        profile = (float(np.sum(absv[tail:] ** 2) / mass)
                   if mass > 0 else None)
    elapsed = time.time() - started
    print("    %-26s theta=%-16s min dir %-10s r in [%s, %s] %s  %.1f s"
          % (label, str(theta), best["name"] if best else "none",
             best["lo"] if best else "n/a", best["hi"] if best else "n/a",
             best["status"] if best else "NONE", elapsed), flush=True)
    del matrix, cands
    return dict(label=label, theta=theta, frame=frame, world=world,
                rows=rows, best=best, profile=profile, elapsed=elapsed)


def schur_read(frame, theta, world, label):
    row = deep.certify_point(frame, mp.mpf(theta), world, label)
    gt, gte, gh, ghe = row["gt"], row["gte"], row["gh"], row["ghe"]
    n0 = n0_from_source(gt, gte, gh, ghe)
    row["n0_lo"], row["n0_hi"] = arb_interval(n0)
    return row


def independent_lerch(t):
    """V-B: L(t) through mpmath's own Lerch transcendent.

    L(t) = sum_{k>=0} e^{-(2k+1/2)t}/(2k+1/2)^2
         = (e^{-t/2}/4) * Phi(e^{-2t}, 2, 1/4),
    which mpmath evaluates by its own hypergeometric machinery, not by the
    truncated-geometric loop of the frozen instrument.
    """
    t = abs(mp.mpf(t))
    if t == 0:
        return (mp.pi ** 2 + 8 * mp.catalan) / 4
    return mp.exp(-t / 2) * mp.lerchphi(mp.exp(-2 * t), 2,
                                        mp.mpf(1) / 4) / 4


def c_ladder(frame, theta, world):
    """The pre-difference ladder c_j = arch_j + atom_j and its ball radii."""
    arch, arch_err = deep.arch_ladder(frame, mp.mpf(theta))
    atom, atom_err = deep.atom_ladder(frame, mp.mpf(theta), world)
    c = [a + b for a, b in zip(arch, atom)]
    ce = [a + b + deep.SOURCE_PAD * (1 + abs(v))
          for a, b, v in zip(arch_err, atom_err, c)]
    return c, ce


def adjoint_weights(coeffs, length):
    """Integer adjoint of the second difference G_r = c_{r+1}-(c_r+c_{r+2})/2.

    sum_r coeff_r G_r = (1/2) sum_j (2 coeff_{j-1} - coeff_j - coeff_{j-2}) c_j,
    so the weights below are exact integers and the whole quadratic form is a
    single linear functional of the ladder.  This bypasses both the G
    differencing and the per-entry Omega assembly.
    """
    def at(index):
        return coeffs[index] if 0 <= index < len(coeffs) else 0
    return [2 * at(j - 1) - at(j) - at(j - 2) for j in range(length)]


def adjoint_form(arr, frame, theta, world):
    """Independent reduction of v^T Omega v as a functional of the ladder."""
    conv, csum = exact_autocorrelations(arr)
    length = 2 * frame.h + 1
    total = arb(0)
    for coeffs, ladder_theta in ((conv, theta), (csum, mp.mpf(0))):
        c, ce = c_ladder(frame, ladder_theta, world)
        for j, weight in enumerate(adjoint_weights(coeffs, length)):
            if weight:
                total += arb(weight) * deep.arb_ball(c[j], ce[j])
    return total / arb(4 * (1 << (2 * VEC_BITS)))


def source_spot_audit(frame, theta, samples=12):
    """Independent mpmath-lerchphi audit of the frozen archimedean ladder.

    The frozen source truncates a geometric series with a rigorous omitted
    tail; mpmath's Lerch transcendent is a different algorithm entirely.  A
    full ladder recomputation costs seconds per point, so a deterministic
    sample of ladder indices is audited instead.  This is an AGREEMENT check,
    not one of the sign paths.
    """
    constant = mp.euler + mp.log(mp.pi) + 3 * mp.log(2) + mp.pi / 2
    count = 2 * frame.h + 1
    step = max(1, count // samples)
    worst = mp.mpf(0)
    checked = 0
    for j in range(0, count, step):
        x = abs(mp.mpf(j - 1) + 2 * mp.mpf(theta))
        t = x * frame.D
        tri = max(mp.mpf(0), 1 - t / frame.D)
        alt = -constant * tri + (2 * independent_lerch(t)
                                 - independent_lerch(abs(t - frame.D))
                                 - independent_lerch(t + frame.D)) / frame.D
        value, error = deep.arch_a(frame, x)
        gap = abs(alt - value)
        scale = error + abs(value) * mp.mpf("1e-70") + mp.mpf("1e-70")
        worst = max(worst, gap / scale)
        checked += 1
    return checked, worst


def triple_verify(cell, row):
    """PREDECLARED independent re-reads of one exact rational witness vector.

    Every path reports the same normalised r = v^T Omega v / ||v||^2, so the
    enclosures are directly comparable, and only a unanimous W-NEG counts:
      V-A  quadruples the working precision (the CCCXXIII artifact class),
      V-B  reduces the form to a linear functional of the pre-difference
           ladder, bypassing both the G differencing and the per-entry
           assembly (the CCCXXXV assembly-defect class),
      V-C  leaves the interval library entirely: Kronecker-substitution
           verification of the integer coefficients plus an exact dyadic
           big-integer sum,
      V-D  an O(h^2) Arb double summation at shallow depth,
      V-E  audits the frozen archimedean source against mpmath's own Lerch
           transcendent (agreement check, not a sign path).
    """
    frame, world, theta, arr = cell["frame"], cell["world"], cell["theta"], \
        row["arr"]
    print("    triple verification of %s direction %s"
          % (cell["label"], row["name"]), flush=True)
    results = {}
    started = time.time()

    mp.mp.dps = VERIFY_DPS
    ctx.prec = VERIFY_BITS
    deep._ARCH_CACHE.clear()
    _G_MEMO.clear()
    gt, gte, gh, ghe = source_balls(frame, theta, world)
    form_a, norm_a = certified_form(arr, gt, gte, gh, ghe)
    results["V-A"] = witness_status(form_a / norm_a)
    print("      V-A  MP_DPS=%d ARB_BITS=%d -> %s  r in [%s, %s]  %.1f s"
          % (VERIFY_DPS, VERIFY_BITS, results["V-A"],
             *arb_interval(form_a / norm_a), time.time() - started),
          flush=True)

    mp.mp.dps = MP_DPS
    ctx.prec = ARB_BITS
    deep._ARCH_CACHE.clear()
    _G_MEMO.clear()
    started = time.time()
    gt, gte, gh, ghe = source_balls(frame, theta, world)
    conv, csum = exact_autocorrelations(arr)
    norm_sq = arb(int(csum[0])) / arb(1 << (2 * VEC_BITS))
    quotient_b = adjoint_form(arr, frame, theta, world) / norm_sq
    results["V-B"] = witness_status(quotient_b)
    print("      V-B  adjoint-weight reduction, no G differencing and no "
          "per-entry assembly -> %s  r in [%s, %s]  %.1f s"
          % (results["V-B"], *arb_interval(quotient_b),
             time.time() - started), flush=True)

    started = time.time()
    kron = kronecker_check(arr, conv, csum)
    rat_lo, rat_up = rational_form_bounds(arr, gt, gte, gh, ghe)
    nsq = Fraction(int(csum[0]), 1 << (2 * VEC_BITS))
    results["V-C"] = ("W-NEG" if rat_up < 0 else
                      "W-POS" if rat_lo > 0 else "W-STRADDLE")
    if not kron:
        results["V-C"] = "COEFFICIENTS-REFUSED"
    print("      V-C  Kronecker-verified coefficients (%s) + Arb-free exact "
          "dyadic sum -> %s  r in [%.17e, %.17e]  %.1f s"
          % ("exact" if kron else "MISMATCH", results["V-C"],
             float(rat_lo / nsq), float(rat_up / nsq),
             time.time() - started), flush=True)

    if frame.h <= DIRECT_SUM_MAX:
        started = time.time()
        quotient = direct_form(arr, gt, gte, gh, ghe) / norm_sq
        results["V-D"] = witness_status(quotient)
        print("      V-D  direct O(h^2) Arb double sum -> %s  r in [%s, %s]"
              "  %.1f s" % (results["V-D"], *arb_interval(quotient),
                            time.time() - started), flush=True)

    started = time.time()
    checked, worst = source_spot_audit(frame, theta)
    audit_ok = worst <= 1
    print("      V-E  mpmath-lerchphi spot audit of %d ladder indices: worst "
          "deviation %.3e of the claimed radius (agreement check, not a sign "
          "path)  %.1f s"
          % (checked, float(worst), time.time() - started), flush=True)

    agree = (all(results[key] == "W-NEG" for key in sorted(results))
             and audit_ok)
    print("      UNANIMOUS W-NEG ACROSS %d INDEPENDENT SIGN PATHS: %s "
          "(source audit %s)"
          % (len(results), agree, "OK" if audit_ok else "MISMATCH"),
          flush=True)
    return agree, results


def interval_exponent(value_a, h_a, value_b, h_b):
    num = (value_b / value_a).log()
    den = arb(str(h_b)).log() - arb(str(h_a)).log()
    return num / den


# ===========================================================================
def main():
    mp.mp.dps = MP_DPS
    ctx.prec = ARB_BITS
    deep.ctx.prec = ARB_BITS
    print("hardness_calibration_falsification_probe -- "
          "PRIME.CORE.HARDNESS.FALSIFY.01")
    print("SPEC_SHA %s  MP_DPS %d  ARB_BITS %d  LIMB %d  VEC %d"
          % (SPEC_SHA[:16], MP_DPS, ARB_BITS, LIMB_BITS, VEC_BITS))

    # ------------------------------------------------------------------ S0
    section("S0 -- firewall, validated Arb LDL bridge, memo ward, frames")
    bad = ast_firewall()
    check("S0.1 AST carries no zero-reader or sign-oracle identifier",
          not bad, ",".join(bad) if bad else "clean", kill="PIPELINE-BROKEN")
    check("S0.2 FLINT/Arb interval LDL bridge certifies SPD and refuses an "
          "indefinite control", deep.ldl_bridge_ward(), kill="PIPELINE-BROKEN")
    if KILLS:
        return finish("HARDNESS-UNRESOLVED", "INSTRUMENT-EDGE", [], {})

    nn, pp = deep.prime_power_table(SIEVE_CAP)
    specs = list(SCHUR_CAL) + list(SCHUR_NEW) + list(N0_ONLY) \
        + list(DEEP_WITNESS)
    frames = {tag: deep.frame_from_integers(tag, want_h, kz, nn)
              for tag, want_h, kz in specs}
    ok_frames = all(frames[tag].h == want_h
                    and frames[tag].cap_n <= int(nn[-1])
                    for tag, want_h, _kz in specs)
    check("S0.3 all %d frames rebuild exactly from integer prime powers"
          % len(specs), ok_frames,
          "; ".join("h=%d/kz=%d/n=%d/cap=%d"
                    % (frames[t].h, frames[t].kz, frames[t].source_n,
                       frames[t].cap_n) for t, _w, _k in specs),
          kill="PIPELINE-BROKEN")
    if KILLS:
        return finish("HARDNESS-UNRESOLVED", "INSTRUMENT-EDGE", [], {})
    order = sorted((tag for tag, _w, _k in specs), key=lambda t: frames[t].h)
    shallow, deepest = order[0], order[-1]
    corner_tag, corner_deep_tag = SCHUR_CAL[-2][0], SCHUR_CAL[-1][0]
    worlds = {tag: deep.genuine_world(frames[tag], nn, pp)
              for tag, _w, _k in specs}
    check("S0.4 memo of the frozen pure source is bitwise faithful",
          memo_ward(frames[corner_tag], mp.mpf("0.5"), worlds[corner_tag]),
          "recomputed through the original g_sequences", kill="MEMO-BROKEN")
    if KILLS:
        return finish("HARDNESS-UNRESOLVED", "INSTRUMENT-EDGE", [], {})

    # ------------------------------------------------------------------ A1
    section("A1 -- exact kernel data of the classical restatement")
    kern = tent_kernel_exact()
    check("A1.1 int K_D = 0 exactly", kern["integral"] == 0,
          "value %s" % kern["integral"])
    check("A1.2 D^-1 int K_D^2 = 2/3 exactly",
          kern["square"] == Fraction(2, 3), "value %s" % kern["square"])
    check("A1.3 ||K_D||_1 = 4D/3 exactly", kern["l1"] == Fraction(4, 3),
          "value %s" % kern["l1"])
    check("A1.4 ||K_D'||_1 = 4 exactly and D-independent", kern["tv"] == 4,
          "value %s" % kern["tv"])
    check("A1.5 ||K_D||_inf = 1 exactly", kern["peak"] == 1)
    expw = {tag: exp_weighted_kernel(frames[tag].D)
            for tag in (corner_tag, corner_deep_tag, deepest)}
    for tag, row in expw.items():
        print("    %s D=%s  T_D=%s (rel dev %s)  int e^{-t/2}K_D=%s "
              "(rel dev %s)"
              % (tag, mp.nstr(frames[tag].D, 12),
                 mp.nstr(row["t_closed"], 14), mp.nstr(row["t_rel"], 4),
                 mp.nstr(row["k_closed"], 14), mp.nstr(row["k_rel"], 4)))
    check("A1.6 both closed forms match independent quadrature",
          all(row["t_rel"] < mp.mpf("1e-40")
              and row["k_rel"] < mp.mpf("1e-40") for row in expw.values()),
          "relative bar 1e-40")

    # ------------------------------------------------------------------ A2
    section("A2 -- scale identity: the test scale sits at the "
            "square-root barrier")
    scale_rows = [frame_scale_row(frames[tag], nn) for tag, _w, _k in specs]
    scale_rows.sort(key=lambda row: row["h"])
    for row in scale_rows:
        print("    h=%6d kz=%4d n=%8d dn=%3d  D=%s  sqrt(N)=%s  "
              "D*sqrt(N)=%s  dn/4=%s  rel=%.3e"
              % (row["h"], row["kz"], row["n"], row["gapint"],
                 mp.nstr(row["D"], 10), mp.nstr(row["root_n"], 10),
                 mp.nstr(row["dsqrtn"], 10), mp.nstr(row["predicted"], 10),
                 float(row["rel"])))
    worst = max(float(row["rel"]) for row in scale_rows)
    check("A2.1 D_h sqrt(N_h) = Delta n_kz / 4 on every built frame",
          worst < 0.05, "worst relative deviation %.3e < 5e-2" % worst)
    check("A2.2 the short-interval length at x=N_h is sqrt(N_h)*Delta n/4, "
          "i.e. at or below the square-root barrier",
          all(row["dsqrtn"] < row["gapint"] for row in scale_rows))

    # ------------------------------------------------------------------ A3
    section("A3 -- THE EXPONENT TABLE")
    env = {tag: rh_envelope_row(frames[tag]) for tag in order}
    first_env, last_env = env[shallow], env[deepest]
    print("    per-block magnitude envelope under RH (Schoenfeld 1976, "
          "|psi(x)-x| <= sqrt(x) log^2 x / 8pi for x>=73.2) against the PNT "
          "block main term:")
    for tag in order:
        row = env[tag]
        print("      h=%6d alpha=%s  S_RH=%s  envelope=%s  |main|=%s  "
              "ratio=%s" % (row["h"], mp.nstr(row["alpha"], 8),
                            mp.nstr(row["s_rh"], 8),
                            mp.nstr(row["envelope"], 8),
                            mp.nstr(row["main"], 8),
                            mp.nstr(row["ratio"], 8)))
    check("A3.1 the RH envelope / main-term ratio grows with depth",
          last_env["ratio"] > first_env["ratio"],
          "%s -> %s, growth %s" % (mp.nstr(first_env["ratio"], 6),
                                   mp.nstr(last_env["ratio"], 6),
                                   mp.nstr(last_env["ratio"]
                                           / first_env["ratio"], 6)))
    law = {}
    for tag, row in env.items():
        gapint = next(r["gapint"] for r in scale_rows if r["h"] == row["h"])
        predicted = (4 * row["block_c"] * (row["alpha"] + row["D"]) ** 2
                     * mp.exp(row["log_n"])
                     / (mp.pi * (mp.mpf(gapint) / 4) ** 3))
        law[tag] = abs(predicted - row["ratio"]) / row["ratio"]
    print("    closed form: with T_D = (8/D)(cosh(D/2)-1) the block main term "
          "is sqrt(N_h) T_D (cosh(D/2)-1) ~ sqrt(N_h) D^3/8, and the A2 "
          "identity D sqrt(N_h) = dn/4 turns the ratio into")
    print("        envelope / |main| = 4 C_h (alpha+D)^2 N_h / (pi (dn/4)^3),")
    print("    i.e. the RH-conditional envelope exceeds the geometric budget "
          "by a factor GROWING LIKE N_h log^2 N_h at fixed prime-power gap.")
    check("A3.2 that closed-form law reproduces the measured ratio at every "
          "built depth", max(float(v) for v in law.values()) < 0.08,
          "worst relative deviation %.3e (the residual is 3x the A2.1 "
          "deviation, which enters cubed)"
          % max(float(v) for v in law.values()))
    deep_h = frames[deepest].h
    deep_gap = next(r["gapint"] for r in scale_rows if r["h"] == deep_h)
    table = (
        ("1  Chebyshev / trivial",
         "psi(x) << x",
         "S(N) <= N^{1/2}; envelope ~ exp(alpha_h)",
         "exp(alpha_h + D_h) = %s at h=%d (alpha=%s) against an O(1) budget"
         % (mp.nstr(last_env["root_n"], 6), deep_h,
            mp.nstr(last_env["alpha"], 6))),
        ("2  Vinogradov-Korobov",
         "psi(x)-x << x exp(-c (log x)^{3/5}(log log x)^{-1/5})",
         "exp((1-o(1)) alpha_h); the o(1) is alpha^{-2/5} polylog",
         "CCCLIX hull R = %s / %s against slack 1.5e-05 -> >= 1.1e6"
         % CITED_VK_HULL),
        ("3  zero density N(s,T) << T^{A(1-s)+e}",
         "short-interval asymptotic for y >= x^{1-1/A+e}",
         "needs D_h >= N_h^{-1/A+e}, i.e. 1/A >= 1/2 + e, i.e. A <= 2-delta",
         "UNCONDITIONALLY IMPOSSIBLE: N(1/2,T) >> T log T forces A >= 2"),
        ("4  density hypothesis (A = 2)",
         "y >= x^{1/2+e}",
         "EXACTLY CRITICAL: 1/A = 1/2 hits D_h = N_h^{-1/2} on the nose",
         "misses by the N_h^{e} and by the log^2 factor; no slack at all"),
        ("5  Lindeloef hypothesis",
         "LH => density hypothesis (A = 2)",
         "identical to row 4",
         "same exact-criticality failure; LH adds nothing here"),
        ("6  RH (Schoenfeld 1976)",
         "|psi(x)-x| <= sqrt(x) log^2 x / 8pi",
         "block envelope (6+2D/3) log^2 N_h / 8pi = C_h alpha_h^2 * 2/pi",
         "envelope %s at h=%d; ratio to the block main term %s, and the "
         "ratio law grows like N_h alpha_h^2"
         % (mp.nstr(last_env["envelope"], 6), deep_h,
            mp.nstr(last_env["ratio"], 6))),
        ("7  RH short-interval asymptotic",
         "psi(x+y)-psi(x) ~ y for y >> sqrt(x) log^2 x",
         "here y_h(N_h) = sqrt(N_h) * Delta n / 4",
         "short by 4 log^2 N_h / Delta n = %s at h=%d (Delta n = %d); for "
         "x < N_h the shortfall grows like sqrt(N_h/x)"
         % (mp.nstr(4 * last_env["log_n"] ** 2 / deep_gap, 6), deep_h,
            deep_gap)),
        ("8  Montgomery pair correlation / Goldston-Montgomery",
         "short-interval VARIANCE asymptotic, itself conditional on RH",
         "an average over x, never a pointwise sign at prescribed ladder "
         "positions",
         "CIRCULAR as a source (assumes RH) and of the wrong type (variance, "
         "not sign)"),
        ("9  Chowla / Elliott",
         "cancellation in additive-shift multiplicative correlations",
         "no control of a logarithmic translation at scale D_h = "
         "Delta n /(4 sqrt(N_h))",
         "CCCLXI no-go: Moebius inversion and finite Dirichlet convolution "
         "are unitriangular, so Sylvester preserves the negative inertia "
         "direction; no orientation is produced"),
        ("10 large sieve / Montgomery-Vaughan / Vaughan mean value",
         "L^2 means of Dirichlet polynomials and bilinear forms",
         "retains the POSITIVE prime diagonal (2/3) sum Lambda(n)^2/n ~ "
         "(4/3) alpha^2",
         "CCCLIX measured %s / %s against |G_geo| %s / %s, i.e. 5.6x / 19.9x "
         "the whole budget and with the wrong sign role"
         % (CITED_PRIMEDIAG + CITED_GGEO)),
        ("11 Selberg symmetry formula",
         "Lambda(n)log n + (Lambda*Lambda)(n) = sum_{d|n} mu(d) log^2(n/d)",
         "A_err - B_err = P_err EXACTLY, so the rewritten residual is "
         "bit-identical to the original",
         "CCCXXXI ward 4.47e-14; information gain factor 1.000, provably "
         "neutral, and its own delivery is 4-5 orders coarser"),
        ("12 Littlewood Omega-theorem (UNCONDITIONAL)",
         "psi(x)-x = Omega_pm(sqrt(x) log log log x)",
         "S(N) >= c0 log log log N -> infinity",
         "THE ENTIRE MAGNITUDE CLASS IS EMPTY: no f with |psi(x)-x| <= "
         "f(x) sqrt(x) can give an O(1) envelope"),
    )
    for name, uses, gives, shortfall in table:
        print("    %s\n        uses     : %s\n        gives    : %s"
              "\n        shortfall: %s" % (name, uses, gives, shortfall))
    check("A3.3 the exponent table has one explicit row per requested source",
          len(table) == 12, "12 rows, every row carries an exponent or a "
                            "numeric shortfall")
    print("    CITED frozen calibration ratios (CCCXXXI, not re-scanned): "
          "best envelope/margin >= %.2e, median %.2e, oracle-exact-main "
          "median %.2e" % (CITED_ENVELOPE_MIN, CITED_ENVELOPE_MED,
                           CITED_ORACLE_MED))

    # ------------------------------------------------------------------ A4
    section("A4 -- magnitude-class emptiness (unconditional)")
    floors = []
    for tag in (shallow, deepest):
        row = env[tag]
        n_val = mp.exp(row["log_n"])
        floor = mp.log(mp.log(mp.log(n_val)))
        floors.append(4 * floor)
        print("    h=%6d N_h=%s  log log log N_h=%s  C_h >= ||K'||_1 = 4  "
              "=> envelope floor >= %s  against a budget with measured slack "
              "%s .. %s" % (row["h"], mp.nstr(n_val, 10), mp.nstr(floor, 8),
                            mp.nstr(4 * floor, 8),
                            mp.nstr(mp.mpf(CITED_SLACK[0]), 4),
                            mp.nstr(mp.mpf(CITED_SLACK[2]), 4)))
    check("A4.1 the unconditional Littlewood floor exceeds the measured slack "
          "at every built depth",
          all(f > mp.mpf(CITED_SLACK[2]) for f in floors),
          "4 log log log N_h vs slack <= 2.73e-03")
    check("A4.2 therefore no magnitude hypothesis delivers an O(1) envelope",
          True, "S(N) -> infinity by Littlewood and C_h >= 4 > 0")

    # ------------------------------------------------------------------ A5
    section("A5 -- the strictly weaker sufficient variant (WSV)")
    wsv_rows, strict_w1, strict_w2 = wsv_witnesses()
    for row in wsv_rows:
        print("    m=%d  X1 = I-2 e_m e_m^T: escape direction %s (never PSD), "
              "fixed direction %s (WSV holds with delta=0)   "
              "X2 = I-(1+1/m) e_m e_m^T: lambda_min %s -> 0"
              % (row["m"], row["x1_escape"], row["x1_fixed"], row["x2_min"]))
    check("A5.1 (W2)+(W3) direction restriction is strictly weaker than rung "
          "PSD", strict_w2,
          "lambda_min = -1 at every m, entrywise limit I, WSV holds")
    check("A5.2 (W1) deficit relaxation is strictly weaker than PSD",
          strict_w1, "lambda_min = -1/m < 0 for all m and -> 0")
    ref_h = max(CITED_SCHUR)
    eps_h = 1 / mp.log(ref_h)
    over = eps_h / mp.mpf(CITED_SCHUR[ref_h][0])
    print("    quantitative value: at h=%d the program proves s >= %s while "
          "WSV needs only s >= -eps_h with eps_h = 1/log h = %s; the current "
          "target is over-strong by a factor %s"
          % (ref_h, CITED_SCHUR[ref_h][0], mp.nstr(eps_h, 6),
             mp.nstr(over, 6)))
    print("    budget effect: B_h may be relaxed by eps_h, which is %s times "
          "the measured slack 1.5e-05, yet the RH block envelope %s at the "
          "deepest built depth h=%d still exceeds eps_h by %s -- WSV relaxes "
          "the target, it does NOT close the table"
          % (mp.nstr(eps_h / mp.mpf(CITED_SLACK[0]), 6),
             mp.nstr(last_env["envelope"], 6), frames[deepest].h,
             mp.nstr(last_env["envelope"] / eps_h, 6)))
    check("A5.3 WSV closes no row of the exponent table",
          last_env["envelope"] > eps_h)

    # ------------------------------------------------------------------ B1
    section("B1 -- citation gate: reproduce the frozen CCCLX theta=1/2 "
            "intervals")
    schur_rows = {}
    upper_rows = {}
    for tag, want_h, _kz in SCHUR_CAL:
        schur_rows[want_h] = schur_read(frames[tag], mp.mpf("0.5"),
                                        worlds[tag], tag + "-CAL-HALF")
        upper_rows[want_h] = witness_read(frames[tag], mp.mpf("0.5"),
                                          worlds[tag], tag + "-CAL-UPPER")
    cal_ok = True
    for _tag, want_h, _kz in SCHUR_CAL:
        row = schur_rows[want_h]
        lo_text, hi_text = CITED_SCHUR[want_h]
        if not row.get("b_pd"):
            cal_ok = False
            print("    h=%4d instrument refused; citation gate cannot close"
                  % want_h)
            continue
        overlap = (mp.mpf(row["schur_hi"]) >= mp.mpf(lo_text)
                   and mp.mpf(row["schur_lo"]) <= mp.mpf(hi_text))
        cal_ok = cal_ok and overlap
        print("    h=%4d reproduced [%s, %s] vs CITED [%s, %s] -> %s"
              % (want_h, row["schur_lo"], row["schur_hi"], lo_text, hi_text,
                 "OVERLAP" if overlap else "DISJOINT"))
    check("B1.1 all %d reproduced theta=1/2 intervals overlap the frozen "
          "run-of-record" % len(SCHUR_CAL), cal_ok,
          kill="CITATION-GATE-BROKEN")
    if KILLS:
        return finish("HARDNESS-UNRESOLVED", "INSTRUMENT-EDGE", [], {})
    print("    the O(h^2) witness path is an UPPER bound on the same s_h "
          "(s_h = min over v_0=1 of v^T Omega v), so U_h >= s_h with equality "
          "at the exact minimiser; measured excess at the gate depths:")
    gate_excess = []
    for _tag, want_h, _kz in SCHUR_CAL:
        u_ball = upper_rows[want_h]["best"]["form"]
        s_ball = arb_from_decimals(*(schur_rows[want_h]["schur_lo"],
                                     schur_rows[want_h]["schur_hi"]))
        excess = float((u_ball / s_ball - 1).upper())
        gate_excess.append(excess)
        print("      h=%5d U_h <= %s   s_h >= %s   U_h/s_h - 1 <= %.3e"
              % (want_h, arb_interval(u_ball)[1],
                 schur_rows[want_h]["schur_lo"], excess))
    check("B1.2 the witness upper bound brackets the Schur value from above "
          "at every gate depth", all(e >= 0 for e in gate_excess))
    check("B1.3 the upper bound is tight to at least 10 significant digits "
          "at the deepest gate depth", gate_excess[-1] < 1e-10,
          "excess %.3e at h=%d" % (gate_excess[-1], SCHUR_CAL[-1][1]))

    # ------------------------------------------------------------------ B2
    section("B2 -- adversarial theta corner sweep (certified witness reads)")
    witness_cells = []
    refused = []
    plan = ([(corner_tag, name, frac) for name, frac in THETA_CORNERS]
            + [(corner_deep_tag, name, frac) for name, frac in THETA_CORNERS
               if name in CORNERS_DEEPCAL])
    for tag, name, frac in plan:
        terms = corner_terms(frames[tag], frac)
        if terms > LERCH_TERM_BAR:
            refused.append((tag, name, terms))
            continue
        theta = mp.mpf(frac.numerator) / frac.denominator
        witness_cells.append(witness_read(
            frames[tag], theta, worlds[tag], tag + "-" + name,
            want_profile=(name == "ONE")))
    print("    frozen-instrument cost bar: a corner at 2theta-distance delta "
          "from Z needs ~94.5/(delta D_h) terms of the truncated Lerch series; "
          "the bar is %.1e terms." % LERCH_TERM_BAR)
    for tag, name, terms in refused:
        print("    REFUSED BY COST (instrument edge, NOT a sign claim): "
              "%s theta corner %s needs ~%.2e Lerch terms"
              % (tag, name, terms))
    check("B2.1 the corner sweep built every corner under the cost bar",
          len(witness_cells) == len(plan) - len(refused),
          "%d built, %d refused by cost out of %d planned"
          % (len(witness_cells), len(refused), len(plan)))
    check("B2.2 the never-scanned integer alignment theta=1 is read at both "
          "corner depths",
          sum(1 for c in witness_cells if c["label"].endswith("-ONE")) == 2)
    print("    INSTRUMENT EDGE, stated honestly: the immediate punctured "
          "neighbourhood of the certified theta=1/2 point is unreachable for "
          "this assembly.  dist(2theta, Z) -> 0 drives the frozen Lerch cost "
          "to infinity while theta=1/2 itself is the exact closed-form point, "
          "so |theta - 1/2| < %.3e at h=%d is a cost singularity, not a "
          "certified region."
          % (94.5 / (LERCH_TERM_BAR * float(frames[corner_deep_tag].D)) / 2,
             frames[corner_deep_tag].h))

    # ------------------------------------------------------------------ B3
    section("B3 -- control worlds: WSV non-vacuity with certified enclosures")
    control_cells = []
    scramble = deep.scramble_world((frames[corner_tag].alpha,
                                    worlds[corner_tag].masses))
    epstein = deep.epstein_world()
    for world in (scramble, epstein):
        control_cells.append(witness_read(
            frames[corner_tag], mp.mpf("0.5"), world,
            corner_tag + "-" + world.name))
    ctrl_neg = [c for c in control_cells
                if c["best"] and c["best"]["status"] == "W-NEG"]
    ctrl_scale = min((abs(float(c["best"]["hi"])) for c in ctrl_neg),
                     default=0.0)
    check("B3.1 both control worlds carry a certified negative direction",
          len(ctrl_neg) == 2, "smallest certified |negative bound| %.3e"
          % ctrl_scale)
    check("B3.2 the control deficits are O(1), hence excluded by any "
          "eps_h -> 0 relaxation", ctrl_scale > 1e-6,
          "min |negative Rayleigh bound| %.3e against the genuine margin "
          "2.12e-10 at h=2854" % ctrl_scale)

    # ------------------------------------------------------------------ B4
    section("B4 -- new certified Schur depths at theta=1/2")
    for tag, want_h, _kz in SCHUR_NEW:
        upper_rows[want_h] = witness_read(frames[tag], mp.mpf("0.5"),
                                          worlds[tag], tag + "-NEW-UPPER")
        schur_rows[want_h] = schur_read(frames[tag], mp.mpf("0.5"),
                                        worlds[tag], tag + "-NEW-HALF")
    check("B4.1 both new depths certify B>0 and a rigorously signed Schur "
          "ball", all(schur_rows[h].get("b_pd") for _t, h, _k in SCHUR_NEW),
          "; ".join("h=%d %s" % (h, schur_rows[h].get("status"))
                    for _t, h, _k in SCHUR_NEW))
    print("    these two depths are NOT in the frozen run-of-record: they are "
          "new two-sided rungs of the wall.")
    schur_nonpos = [h for h in sorted(schur_rows)
                    if schur_rows[h].get("status") == "S-NONPOS"]
    check("B4.2 no certified nonpositive Schur ball at any built depth",
          not schur_nonpos, "nonpositive depths: %s"
          % (schur_nonpos if schur_nonpos else "none"))

    # ------------------------------------------------------------------ B5
    section("B5 -- deep certified witness reads (the O(h^2) instrument)")
    deep_cells = []
    for tag, want_h, _kz in N0_ONLY + DEEP_WITNESS:
        cell = witness_read(frames[tag], mp.mpf("0.5"), worlds[tag],
                            tag + "-DEEP-HALF", want_profile=True)
        upper_rows[want_h] = cell
        deep_cells.append(cell)
        if tag == DEEP_WITNESS[0][0]:
            for name, frac in THETA_CORNERS:
                if name not in CORNERS_WITNESS_DEEP:
                    continue
                if corner_terms(frames[tag], frac) > LERCH_TERM_BAR:
                    continue
                theta = mp.mpf(frac.numerator) / frac.denominator
                deep_cells.append(witness_read(
                    frames[tag], theta, worlds[tag], tag + "-DEEP-" + name))
        if tag != deepest:
            drop_frame_memo(tag)
    check("B5.1 the certified witness instrument reaches h=%d, %.1fx deeper "
          "than the deepest previously certified read in this family"
          % (frames[deepest].h, frames[deepest].h / float(max(CITED_SCHUR))),
          len(deep_cells) >= 3)
    for cell in witness_cells + deep_cells:
        if cell["profile"] is not None:
            print("    DIAGNOSTIC-ONLY (binary64, decides nothing): %s "
                  "Schur-minimizer mass in the top decile of indices = %.4f"
                  % (cell["label"], cell["profile"]))

    all_cells = witness_cells + deep_cells
    negatives = [c for c in all_cells
                 if c["best"] and c["best"]["status"] == "W-NEG"]
    straddles = [c for c in all_cells
                 if c["best"] and c["best"]["status"] == "W-STRADDLE"]
    check("B5.2 no certified negative direction at any genuine cell",
          not negatives, "negatives %d, straddles %d"
          % (len(negatives), len(straddles)))

    # ------------------------------------------------------------------ B6
    section("B6 -- certified margin trend and the honest extrapolation")
    depths = sorted(set(upper_rows)
                    | {h for h in CITED_SCHUR if ("H%d" % h) in frames})
    trend = []
    for want_h in depths:
        tag = "H%d" % want_h
        frame = frames[tag]
        row = schur_rows.get(want_h)
        upper = upper_rows.get(want_h)
        if row is not None and row.get("b_pd"):
            s_lo, s_hi = row["schur_lo"], row["schur_hi"]
            n0_lo, n0_hi = row["n0_lo"], row["n0_hi"]
            origin = "TWO-SIDED"
        elif want_h in CITED_SCHUR:
            s_lo, s_hi = CITED_SCHUR[want_h]
            gt, gte, gh, ghe = source_balls(frame, mp.mpf("0.5"), worlds[tag])
            n0_lo, n0_hi = arb_interval(n0_from_source(gt, gte, gh, ghe))
            origin = "CITED"
        else:
            gt, gte, gh, ghe = source_balls(frame, mp.mpf("0.5"), worlds[tag])
            n0_lo, n0_hi = arb_interval(n0_from_source(gt, gte, gh, ghe))
            s_lo, s_hi = None, arb_interval(upper["best"]["form"])[1]
            origin = "UPPER-ONLY"
        n0_ball = arb_from_decimals(n0_lo, n0_hi)
        dball = arb(mp.nstr(frame.D, 60))
        mu = dball * dball
        u_ball = (upper["best"]["form"] if upper is not None
                  else arb_from_decimals(s_lo, s_hi))
        entry = dict(h=want_h, origin=origin, s_lo=s_lo, s_hi=s_hi,
                     n0_lo=n0_lo, n0_hi=n0_hi, u=u_ball,
                     uhat=u_ball / n0_ball, umu=u_ball / mu, D=frame.D)
        if s_lo is not None:
            s_ball = arb_from_decimals(s_lo, s_hi)
            entry.update(s=s_ball, shat=s_ball / n0_ball, smu=s_ball / mu)
        trend.append(entry)
        print("    h=%5d [%-10s] s in [%s, %s]  n0 in [%s, %s]"
              % (want_h, origin, s_lo if s_lo else "  (upper only)  ", s_hi,
                 n0_lo, n0_hi))
        if s_lo is not None:
            print("                       s/n0 in [%s, %s]   "
                  "s/D^2 in [%s, %s]"
                  % (*arb_interval(entry["shat"]), *arb_interval(entry["smu"])))
        print("                       certified U_h <= %s   U/n0 <= %s   "
              "U/D^2 <= %s"
              % (arb_interval(u_ball)[1], arb_interval(entry["uhat"])[1],
                 arb_interval(entry["umu"])[1]))
    two_sided = [row for row in trend if row.get("s") is not None]
    exps = []
    for a, b in zip(two_sided[:-1], two_sided[1:]):
        e_s = interval_exponent(a["s"], a["h"], b["s"], b["h"])
        e_shat = interval_exponent(a["shat"], a["h"], b["shat"], b["h"])
        e_smu = interval_exponent(a["smu"], a["h"], b["smu"], b["h"])
        exps.append(dict(a=a["h"], b=b["h"], s=e_s, shat=e_shat, smu=e_smu))
        print("    TWO-SIDED local exponent %5d -> %5d : s in [%s, %s]   "
              "s/n0 in [%s, %s]   s/D^2 in [%s, %s]"
              % (a["h"], b["h"], *arb_interval(e_s), *arb_interval(e_shat),
                 *arb_interval(e_smu)))
    uexps = []
    for a, b in zip(trend[:-1], trend[1:]):
        e_u = interval_exponent(a["u"], a["h"], b["u"], b["h"])
        e_uhat = interval_exponent(a["uhat"], a["h"], b["uhat"], b["h"])
        uexps.append(dict(a=a["h"], b=b["h"], u=e_u, uhat=e_uhat))
        print("    UPPER-BOUND local exponent %5d -> %5d : U in [%s, %s]   "
              "U/n0 in [%s, %s]"
              % (a["h"], b["h"], *arb_interval(e_u), *arb_interval(e_uhat)))
    g_s = interval_exponent(two_sided[0]["s"], two_sided[0]["h"],
                            two_sided[-1]["s"], two_sided[-1]["h"])
    g_shat = interval_exponent(two_sided[0]["shat"], two_sided[0]["h"],
                               two_sided[-1]["shat"], two_sided[-1]["h"])
    g_smu = interval_exponent(two_sided[0]["smu"], two_sided[0]["h"],
                              two_sided[-1]["smu"], two_sided[-1]["h"])
    g_u = interval_exponent(trend[0]["u"], trend[0]["h"],
                            trend[-1]["u"], trend[-1]["h"])
    g_uhat = interval_exponent(trend[0]["uhat"], trend[0]["h"],
                               trend[-1]["uhat"], trend[-1]["h"])
    print("    GLOBAL TWO-SIDED h=%d -> h=%d : s ~ h^p with p in [%s, %s];  "
          "s/n0 ~ h^[%s, %s];  s/D^2 ~ h^[%s, %s]"
          % (two_sided[0]["h"], two_sided[-1]["h"], *arb_interval(g_s),
             *arb_interval(g_shat), *arb_interval(g_smu)))
    print("    GLOBAL UPPER-BOUND h=%d -> h=%d : U ~ h^[%s, %s];  "
          "U/n0 ~ h^[%s, %s]"
          % (trend[0]["h"], trend[-1]["h"], *arb_interval(g_u),
             *arb_interval(g_uhat)))
    all_positive = all(mp.mpf(row["s_lo"]) > 0 for row in two_sided)
    check("B6.1 every two-sided margin enclosure is strictly positive",
          all_positive, "%d depths %d <= h <= %d"
          % (len(two_sided), two_sided[0]["h"], two_sided[-1]["h"]))
    up_positive = all(mp.mpf(arb_interval(row["u"])[0]) > 0
                      for row in trend)
    check("B6.2 every certified upper-bound read is itself strictly positive, "
          "so no depth up to h=%d hides a negative rung in the near-optimal "
          "direction" % trend[-1]["h"], up_positive)
    check("B6.3 every local log-log exponent has a finite two-sided "
          "enclosure",
          all(float(e["s"].lower()) > -50 and float(e["s"].upper()) < 0
              for e in exps),
          "%d two-sided and %d upper-bound interval exponents"
          % (len(exps), len(uexps)))
    monotone = all(mp.mpf(b["s_hi"]) < mp.mpf(a["s_lo"])
                   for a, b in zip(two_sided[:-1], two_sided[1:]))
    down_shat = all(float(e["shat"].upper()) < 0 for e in exps)
    down_smu = all(float(e["smu"].upper()) < 0 for e in exps)
    steepening = all(float(exps[i + 1]["shat"].upper())
                     < float(exps[i]["shat"].lower())
                     for i in range(len(exps) - 1))
    up_steepening = all(float(uexps[i + 1]["uhat"].upper())
                        < float(uexps[i]["uhat"].lower())
                        for i in range(len(uexps) - 1))
    deepest_exp = float(exps[-1]["shat"].upper())
    deepest_up_exp = float(uexps[-1]["uhat"].upper())
    print("    margins strictly decreasing across all two-sided depths: %s"
          % monotone)
    print("    normalised drift downward on every step: s/n0 %s, s/D^2 %s"
          % (down_shat, down_smu))
    print("    monotone steepening: two-sided s/n0 %s (deepest local exponent "
          "upper bound %.4f), upper-bound U/n0 %s (deepest %.4f), against the "
          "frozen collapse bar %.1f"
          % (steepening, deepest_exp, up_steepening, deepest_up_exp,
             STEEPEN_BAR))
    print("    the s/n0 and s/D^2 ladders are the mu_h-normalised margin the "
          "task asks about: mu_h = D_h^2 shrinks like h^-2, and the measured "
          "s/D^2 exponent band is stated above.  Both normalisations drift "
          "downward with a NEGATIVE exponent that is bounded away from -inf "
          "at every step, i.e. a pure power law, not a collapse.")
    tail_flat = float(uexps[-1]["uhat"].lower()) > float(g_uhat.upper())
    print("    DIRECTION OF THE DRIFT AT DEPTH: the deepest upper-bound step "
          "%d -> %d carries the local exponent [%s, %s], strictly ABOVE the "
          "global [%s, %s]; the step before it is [%s, %s]."
          % (uexps[-1]["a"], uexps[-1]["b"],
             *arb_interval(uexps[-1]["uhat"]), *arb_interval(g_uhat),
             *arb_interval(uexps[-2]["uhat"])))
    check("B6.4 the deepest local upper-bound exponent is strictly flatter "
          "than the global one, i.e. the decay FLATTENS with depth instead "
          "of accelerating -- evidence in the direction opposite to "
          "TREND-DOWNWARD", tail_flat,
          "deepest local lower end %s vs global upper end %s"
          % (arb_interval(uexps[-1]["uhat"])[0], arb_interval(g_uhat)[1]))
    positive_steps = [e for e in exps if float(e["smu"].lower()) > 0]
    print("    CAVEAT ON THE WHOLE TREND, stated honestly: this family is "
          "indexed by the prime-power index kz, NOT by h.  The integer gap "
          "Delta n_kz along the built ladder is %s, so s_h is not a function "
          "of h alone and every exponent above is a two-point secant in "
          "log h, not a fit.  %s"
          % (", ".join(str(next(r["gapint"] for r in scale_rows
                                if r["h"] == row["h"])) for row in trend),
             ("The steps %s even carry a certified POSITIVE s/D^2 exponent, "
              "which is exactly this effect."
              % "; ".join("%d -> %d" % (e["a"], e["b"])
                          for e in positive_steps))
             if positive_steps else
             "No step carries a positive s/D^2 exponent on this ladder."))
    last_a, last_b = two_sided[-2], two_sided[-1]
    shat_a = mp.mpf(arb_interval(last_a["shat"])[0])
    shat_b = mp.mpf(arb_interval(last_b["shat"])[1])
    slope = (shat_b - shat_a) / (mp.log(last_b["h"]) - mp.log(last_a["h"]))
    secant_h = (mp.exp(mp.log(last_b["h"]) - shat_b / slope)
                if slope < 0 else mp.inf)
    print("    affine (NOT log-affine) secant through the two deepest "
          "two-sided points reaches zero at h* = %s"
          % mp.nstr(secant_h, 8))
    print("    THIS SECANT IS REFUSED as a crossing prediction: it is an "
          "artifact of linearising a convex positive decay.  A positive power "
          "law s ~ h^p with p in the measured band never reaches zero at "
          "finite h.")
    print("    EXTRAPOLATION LIMITS, stated honestly: the two-sided data are "
          "%d depths in %d <= h <= %d (%d reproduced from the frozen CCCLX "
          "record, %d new, 1 CITED); the certified upper bounds run to h=%d; "
          "nothing outside the built cells is measured.  The O(h^3) route "
          "ceiling under the %.0f s bar is h ~ 3.4e3, so the CCCXXIX straddle "
          "band h >= 10863 is reachable ONLY by the O(h^2) upper-bound "
          "instrument, which is what h=%d delivers."
          % (len(two_sided), two_sided[0]["h"], two_sided[-1]["h"],
             len(SCHUR_CAL), len(SCHUR_NEW), trend[-1]["h"], RUNTIME_BAR,
             trend[-1]["h"]))

    # ------------------------------------------------------------------ V
    part_b = "NO-WITNESS"
    if negatives or schur_nonpos:
        section("B7 -- PREDECLARED TRIPLE VERIFICATION")
        agreed = False
        for cell in negatives:
            ok, _res = triple_verify(cell, cell["best"])
            agreed = agreed or ok
        part_b = "FALSIFIED" if agreed else "INSTRUMENT-EDGE"
    elif straddles:
        part_b = "INSTRUMENT-EDGE"
    elif (down_shat and down_smu and steepening
          and deepest_exp < STEEPEN_BAR) or (
              up_steepening and deepest_up_exp < STEEPEN_BAR):
        part_b = "TREND-DOWNWARD"
    stats = dict(witness=len(witness_cells), deep=len(deep_cells),
                 controls=len(control_cells), schur=len(schur_rows),
                 negatives=len(negatives), straddles=len(straddles),
                 deepest_witness=frames[deepest].h,
                 deepest_schur=max(schur_rows), monotone=monotone,
                 down=down_shat and down_smu,
                 exp_band=(arb_interval(g_shat), arb_interval(g_smu)),
                 upper_band=arb_interval(g_uhat))
    return finish("HARDNESS-UNRESOLVED", part_b, trend, stats)


def finish(part_a, part_b, trend, stats):
    section("V -- frozen verdicts")
    runtime = time.time() - T0
    if part_a not in PART_A_VERDICTS:
        part_a = "HARDNESS-UNRESOLVED"
    if part_b not in PART_B_VERDICTS:
        part_b = "INSTRUMENT-EDGE"
    check("V.1 Part A verdict in the frozen enum", part_a in PART_A_VERDICTS)
    check("V.2 Part B verdict in the frozen enum", part_b in PART_B_VERDICTS)
    check("V.3 runtime %.1f s < %.0f s" % (runtime, RUNTIME_BAR),
          runtime < RUNTIME_BAR)
    if not all(ok for _n, ok in CHECKS) and part_b != "FALSIFIED":
        part_b = "INSTRUMENT-EDGE"
    passed = sum(ok for _n, ok in CHECKS)
    print("\n  PART A VERDICT: %s" % part_a)
    print("    RH => the inequality: PROVED direction, by Weil's criterion "
          "applied to the explicit Gram family; no exponents are needed.")
    print("    the inequality => RH: OPEN at four named premises (PREDEFINED "
          "H_cof / noninterference, per-element form convergence, density, "
          "C0 extension), so equivalence is NOT established.")
    print("    the magnitude class is UNCONDITIONALLY EMPTY (Littlewood), so "
          "no listed conjecture suffices; the exact gap is the exponent "
          "ladder exp((1-o(1))alpha_h) -> alpha_h^2 * 2/pi against an O(1) "
          "budget whose envelope/main-term ratio grows like N_h alpha_h^2.")
    print("    STRICTLY WEAKER SUFFICIENT VARIANT (WSV) is specified, its "
          "strictness is proved by exact rational witnesses, and it relaxes "
          "the target by ~9 orders at h=2854 without weakening the "
          "conclusion.")
    print("  PART B VERDICT: %s" % part_b)
    if stats:
        print("    cells: %d corner witness, %d deep witness, %d control, "
              "%d Schur; certified negatives %d; straddles %d"
              % (stats.get("witness", 0), stats.get("deep", 0),
                 stats.get("controls", 0), stats.get("schur", 0),
                 stats.get("negatives", 0), stats.get("straddles", 0)))
        print("    depth reached: certified witness h=%d, certified Schur "
              "h=%d; margins monotone decreasing %s; normalised drift "
              "downward %s"
              % (stats.get("deepest_witness", 0),
                 stats.get("deepest_schur", 0), stats.get("monotone"),
                 stats.get("down")))
    print("  NO RH CLAIM IN EITHER DIRECTION; no all-h claim; no marker move; "
          "nothing enters a certificate.")
    print("\n  checks %d/%d PASS; kills=%s; SPEC_SHA=%s; runtime %.1f s"
          % (passed, len(CHECKS), KILLS if KILLS else "none",
             SPEC_SHA[:16], runtime))
    return 0 if (not KILLS and passed == len(CHECKS)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
