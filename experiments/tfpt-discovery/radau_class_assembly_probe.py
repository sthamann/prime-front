#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""radau_class_assembly_probe -- PRIME.ONEBADMODE.RADAU.CLASS.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE NON-CIRCULAR CLASS-LEVEL ASSEMBLY OF THE SIGMA CHAIN.  The lead
auditor's demand is exact: CCLXI's separate-envelope KS class LEAKS
(machine-shown, uncapped sup tr R = 2.2551 reproduced by CCLXV), and
CCLXV's repair -- the cap sigma <= t -- is CIRCULAR, because
sigma = q/n = 1 - s/n IS the Schur quotient, i.e. the conclusion
(M > 0 <=> sigma < 1) written as a hypothesis.  The missing object is
therefore a JOINT relation between the carriers (the pivot n, the
b-weighted moments nu, the co-block floor c) that is a function of the
SOURCE data only.  THE CANDIDATE, named by the mission: the
Gauss-Radau functional itself.  It is nonlinear, it is a SOURCE-ONLY
function of the moment vector and the certified floor
(RADAU_K(nu_0..nu_{2K-2}; c), CCLXXVII's exact-rational bound
functional), it is exactly the correlation between n and nu that
separate envelopes forget, and per step it already delivers
sigma <= 0.648113 => M positive definite on 68/68 (CCLXXVII) and
< 1 on every built wall-legal cell at K = 5 (CCLXXIX lane).  THIS
PROBE lifts it from per-step to CLASS level and shapes the joint sum
rule.

 (a) THE NO-GO LEMMA (cheap, permanent).  The lead's high-pole
     blindness lemma, warded SYMBOLICALLY (sympy, exact): for the
     unit atom moved from +eps to -eps -- i.e. exactly the flip
     between a positive-definite and an indefinite one-bad-mode
     world -- the Cauchy transform difference at the high point
     z = i y is
         Delta m(i y) = 2 eps / (eps^2 + y^2) <= 2 eps / y^2,
     while the SAME flip moves the low-pole functional
     q = int x^{-1} d nu by 2 / eps.  The sensitivity ratio is
     exactly y^2 / eps^2.  High-pole data is therefore blind to the
     decision at rate O(eps / y^2) and low-pole / moment data is
     unboundedly sensitive to it.  CCLXXV (pick_dual_probe) is the
     empirical instance of the lemma: the corrected interlacing
     Stieltjes/Pick class over the frozen disk ladder
     Y = (2100, ..., 49743.176671938345) is PICK-DEAD in BOTH
     tiers, with an exact one-bad-atom witness Phi = 2.116960965
     and a rational Sturm enclosure of 3.16e-7.  The lemma freezes
     the typing 'why moments, not high poles' permanently.
 (b) THE RADAU-CONSTRAINED CLASS and THE EXTREMAL TEST.  The CCLXI
     class C_KS is rebuilt VERBATIM (entry box, a_i > 0, co-block
     floor lambda_min(J_B) >= c_B, KS radius spec(J) in [-L, L],
     KS_wall / COEF / SPREAD wall functionals, all frozen from the
     truth ladder with the CCLXI widening rule MARGIN_FRAC = 0.10)
     and the CIRCULAR sigma-cap is REPLACED by two source-only
     objects:
       MOM  the moment box: nu_k in [nu_lo_k, nu_hi_k] for
            k = 0..2K-2, measured flat over the truth ladder and
            widened in LOG space (amendment A2) -- the SEPARATE
            envelope of each carrier;
       RAD  the JOINT constraint RADAU_K(nu_0..nu_{2K-2}; c) <=
            t_R * n, evaluated at the member's OWN certified
            co-block floor c = lambda_min(J_B) (amendment A7), with
            t_R = SIGMA_ENV = 0.7809 (the CCLXIX registered
            envelope, consumed at its cited 4-digit truncation) --
            the nonlinear relation BETWEEN the carriers.
     The extremal test is a ladder of tiers, each a numeric global
     (multi-start SLSQP + differential evolution, seed declared;
     an optimizer maximum is a LOWER bound of the true sup, so
     every 'closes' is typed NUMERIC):
       E0  C_KS alone                     (CCLXI/CCLXV repro anchor)
       E1  C_KS + n > 0                   (the entry sheet)
       E2  E1 + MOM                       (SEPARATE ENVELOPES)
       E3  E2 + RAD at K = 4              (THE JOINT TIER)
       E4  E2 + RAD at K = 5              (the CCLXXIX depth)
       E5  E1 + the CIRCULAR sigma-cap    (reference only, flagged)
     THE QUESTION: does the JOINT constraint close the leak that the
     separate envelopes could not (sup < 1)?  The sup, the maximizer
     anatomy and the margin are reported per tier.  NOTE the honest
     ceiling: the truth ladder is inside every tier, so every sup is
     >= the truth's own max tr R = 0.9727 (CCLXVII); the achievable
     margin is at most 1 - 0.9727 = 0.0273.
 (c) THE MEMBERSHIP CENSUS.  The 68 deployed ladder steps and the
     CCLXIX F0 off-ladder cells (CCLXXVII builder verbatim) are
     censused against every tier: per cell the certified
     exact-rational co-block floor c_cert (round-62 LDL machine,
     CCLXXVII verbatim), the certified RADAU_K/n value at K = 4 and
     K = 5, and the per-constraint slack.  The CCLXXIII edge family
     (111 wall-legal steps beyond the registration cut, sigma max
     0.670393) is CITED, NOT REBUILT -- its cost is outside this
     probe's frozen budget and its numbers are consumed only as a
     compatibility check against t_R.  FALSIFYING WORLDS (built
     here: inflated coupling, shrunk pivot, flipped pivot) are
     censused for WHICH constraint excludes each; if any indefinite
     world is INSIDE the joint tier AND has tr R >= 1, the class
     FAILS and that is reported in the verdict line.
 (d) THE JOINT SUM RULE SHAPE.  The composition
     separator o interlacing o Schur o Radau is derived here, with
     every rung typed:
       R1 Cauchy interlacing: lambda_i(J) >= lambda_{i-1}(J_B) for
          i = 2..8, so AT MOST ONE eigenvalue of J lies below
          lambda_min(J_B) -- the one bad mode.  [THEOREM]
       R2 the separator: R >= 0 on all of R (CCXXV certified), so
          no contribution is dropped; on [x, L] the frozen filter
          admits the NON-INCREASING envelope Rdec(x) = sup_{[x,L]} R
          computed on a declared log grid.  [FROZEN FUNCTION +
          declared numeric envelope]
       R3 the bad mode from below.  For 0 <= lam < c one has
          (B - lam)^{-1} <= (c / (c - lam)) B^{-1} (eigenvalue-wise,
          x >= c), so the secular function
          phi(lam) = n - lam - b^T (B - lam)^{-1} b obeys
          phi(lam) >= n - lam - c q / (c - lam); phi is strictly
          decreasing below lambda_min(B) and phi(lambda_1) = 0,
          hence with rho := RADAU_K(nu; c) / n >= q / n = sigma
              lambda_1(J) >= Lambda(n, c, rho)
                          := ((n + c) - sqrt((n - c)^2 + 4 n c rho))/2
          -- a CLOSED-FORM, SOURCE-ONLY, strictly positive lower
          bound on the bad eigenvalue whenever rho < 1.  The
          quadratic algebra is warded symbolically (sympy, exact).
          A sharper source-only variant (SHIFT-RADAU) bisects the
          largest lam with n - lam - RADAU_K(nu(lam); c - lam) >= 0,
          where nu(lam) are the shifted moments (the Jacobi
          coefficients shift by -lam, E4).  [DERIVED HERE + E3]
       R4 compose:
              1 - tr R(J) >= 1 - Rdec(Lambda(n, c, rho))
                               - sum_j Rdec(lambda_j(J_B)) =: F,
          and the crude class-uniform form replaces the co-block sum
          by 7 * Rdec(c_B).  F is an explicit function of the SOURCE
          carriers (n, nu, c) and the co-block geometry alone.
     F is evaluated per cell against the truth reserve (the chain
     must never exceed it -- warded per cell), its sign census is
     reported, and the LOSSY RUNG (the measured seat) is isolated by
     replacing each bound in turn by its truth value.  If F is
     provably >= delta > 0 under the class constraints, that is the
     joint sum rule and it is stated loudly; if not, the seat is
     stated just as loudly, with the loss factor per rung.
 (e) GATES.  tau / CCXVII c_h relocation screens on the class margin
     and on F; controls-must-fire (search power, falsifying worlds,
     the Radau bound property RB1 per cell, the exact-vs-float
     route ward); anti-circularity STRICT, by MOMENT LOCALITY
     (amendment A8): the joint constraint path is AST-scanned
     against a ban list containing sigma, the Schur gap, the wall
     margin/reserve/trace and every eigensolver, and the DECISIVE
     numeric ward is that RADAU_K and the moment box read only the
     Jacobi coordinates (a_1; b_2..b_K; a_2..a_K), so perturbing the
     DEEP TAIL leaves them EXACTLY unchanged while the circular
     sigma -- which reads the whole co-block resolvent
     b^T B^{-1} b -- moves (control MUST fire).  The inherited CCLXI
     spectral functionals are typed separately and warded invariant
     under the flip J -> -J, and the co-block floor is warded
     independent of the two coordinates b_1, a_1 that carry the
     pivot and the coupling.

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E2 Schur / Sylvester: M = [[n, b^T], [b, B]] symmetric is PD iff
    B is PD and s = n - b^T B^{-1} b > 0.  [Horn & Johnson, Matrix
    Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE: for symmetric A with spec(A)
    in [c, inf), the K-node Gauss-Radau rule with the node prescribed
    at c is an UPPER bound for u^T A^{-1} u (f(x) = 1/x completely
    monotone).  [Golub & Meurant, Matrices, Moments and Quadrature,
    PUP 2010, Ch. 6-7.]  WARDED PER CELL (RB1).
 E4 the Chebyshev algorithm: the monic three-term recurrence of the
    orthogonal polynomials of a positive measure is a rational
    function of its power moments; exact in exact arithmetic.
    [Gautschi, OUP 2004, Sec. 2.1; Golub & Meurant op. cit. Ch. 4.]
 E7 Cauchy interlacing: for a symmetric A and the principal
    submatrix A' obtained by deleting one row/column,
    lambda_i(A) <= lambda_i(A') <= lambda_{i+1}(A).  [Horn &
    Johnson op. cit. Sec. 4.3.]
 E8 the CCXXV separator certificates, re-consumed: R >= 0 on R,
    R >= 1 on x <= 0, and 0 <= R <= delta on [c_B, L] for the frozen
    m = 8 Zolotarev filter.

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seat is the declared optimizer seed.
 AC the joint-constraint path (moment_vector / radau_from_entries /
    radau_con / moment_box_con / pivot_con / theta_matrices /
    lanczos_pair / radau_upper) is AST-scanned against
    CLASS_BANNED; the inherited CCLXI functionals are typed in a
    printed table and warded definiteness-blind numerically; the
    circular sigma-cap is run through the same wards as a control
    that MUST fail.
 L  the no-go lemma, exact in sympy.
 W  the CCVII/CCXXV ladder rebuilt read-only (42 surface rungs ->
    68 = 40 + 1 + 27 steps), step keys warded against the stored
    CCXLVII artifact; the CCLXIX/CCLXXVII F0 family rebuilt verbatim.
 T  filter + per-step reads (LU vs eigen vs stored artifact).
 B/I Jacobi translation and the CCLXV identity wards per cell.
 SR repro anchors: reserve med 0.9195 / min 2.7302e-2 (CCXLVII),
    ladder sigma max 0.604556, F0 sigma max 0.709925 (CCLXIX),
    certified K = 4 ladder bound max 0.648113 (CCLXXVII).
 G  the class frozen and SHA-printed BEFORE any optimization.
 N  the membership census.
 E  the extremal tier ladder (the RESERVE question sup tr R) and the
    definiteness tier D (the strictly weaker question inf lambda_1).
 A  the joint sum rule.
 X  controls-must-fire.
 S  tau / CCXVII c_h relocation screens.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 RADAU-CLASS-CLOSES(sup, margin; the separate-envelope tier leaks at
   X) -- the joint source-only constraint closes what the separate
   envelopes could not; NUMERIC-GLOBAL typing mandatory.
 RADAU-CLASS-CLOSES-ENVELOPE-ALSO(sup) -- the joint tier closes but
   so does the separate-envelope tier: the joint relation is not the
   decisive object on this class.
 RADAU-CLASS-LEAKS(witness anatomy) -- the joint tier admits
   tr R >= 1; the leak is NOT closed by the Radau functional.
Every verdict carries the DEFINITENESS qualifier
+DEFINITE(inf lambda_1) / +INDEFINITE-ADMITTED(inf lambda_1), the
strictly weaker question of amendment A6: whether the class forces
M > 0 at all.  A leak in the reserve question with +DEFINITE is NOT
a contradiction with the CCLXXVII per-step chain.
Sub-verdict for (d): SUMRULE-EXPLICIT(delta) / SUMRULE-PERCELL(k/n,
seat) / SUMRULE-SEAT(rung, loss factor).
Every enum is a finite statement about the deployed ladder artifact,
the tested F0 cells and the frozen class; NEVER an all-h statement,
NEVER an RH claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE =
2e-9; PF_TIE = 2e-8; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7;
IDENT_TIE = 1e-12; REPRO_RTOL = 5e-2; RES_MED_REF = 0.9195;
RES_MIN_REF = 2.730e-2; SIGMA_MAX_REF = 0.604556; F0_SIGMA_REF =
0.709925; BOUND4_REF = 0.648113; SUP_NOCAP_REF = 2.2551;
SUP_NOCAP_BAR = 1.0; TRUTH_TRR_REF = 0.9727; MARGIN_FRAC = 0.10;
MOM_MARGIN = 0.10; FEAS_TOL = 1e-9; KDEG = 4; KDEG5 = 5; T_R =
7809/10000 (= SIGMA_ENV, CCLXIX registration at its cited 4-digit
truncation); F0_CAP = 12; BIS_ITERS = 40; RADAU_SIGN_TIE = 1e-12;
NODE_TIE = 1e-9; XR_TIE = 1e-6; ENV_LO = 1e-7; ENV_GRID = 40000;
ENV_TEST = 400; MAP_MS = 20; MAP_DE = 140; CONF_MS = 40; CONF_DE =
280; DE_POP = 20; SLSQP_MAXIT = 150; OPT_SEED = 20260812; PEN_W =
1e4; QBITS = 12; CTRL_COUPLE = 10.0; CTRL_PIVOT = 0.05;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; runtime cap 25 min.

HONEST AMENDMENTS (declared before the frozen run).
 A1 the mission names 'sigma <= 0.648 => M > 0 on 68/68 (CCLXXVII)'
    as the per-step delivery.  0.648113 is the certified K = 4
    LADDER bound max; the F0 sigma-max cell (kz 45, h 1359) is
    K = 4 INFEASIBLE and needs K = 5 (0.7269, CCLXXVII's disclosed
    diagnostic, CCLXXIX lane).  Both depths are therefore run as
    separate tiers here and the census reports both.
 A2 the moment box is frozen in LOG space (nu_k > 0 on the whole
    class because the co-block floor forces B > 0, and the truth
    values span many decades, so a linear box widened by
    MARGIN_FRAC of its width would clip its lower edge to 0 and be
    vacuous).  This makes the separate-envelope tier TIGHTER, i.e.
    it makes the (b) question HARDER, not easier.  Disclosed.
 A3 the Radau functional is mathematically a function of
    (nu_0..nu_{2K-2}, c) alone (E4).  In the class-constraint
    evaluation it is computed by the numerically stable Lanczos
    route on the ENTRIES rather than by the float Chebyshev
    recursion on the power moments, because the power-moment Hankel
    form is catastrophically ill-conditioned in float64 at the
    deployed dynamic range (nu_6 ~ 1e18).  The two routes are
    warded equal per truth cell against CCLXXVII's EXACT-RATIONAL
    moment tier, so the constraint is the same source-only
    functional; the moment vector itself is computed and boxed in
    float directly from the entries, where no ill-conditioning
    arises.
 A4 the class co-block floor c_B is WIDENED by the CCLXI rule when
    the truth minimum falls below the cited c_B = 0.5523 (it does:
    ladder min lambda_min(J_B) = 0.3496 -> c_class = 0.3146).  The
    separator's certified bulk bound R <= delta holds only on
    [0.5523, L], so the sum rule (d) must use the declared envelope
    Rdec on [c_class, L], which is LARGER than delta.  This is
    disclosed as the first structural cost of the widening and is
    quantified in section A.
 A5 the CCLXXIII edge family (111 wall-legal steps) is CITED, not
    rebuilt: rebuilding it needs the h > 1450 deep scan, which does
    not fit the 25 min frozen budget together with the extremal
    ladder.  Its consumption here is limited to the compatibility
    statement 'edge sigma max 0.670393 <= t_R = 0.7809', typed
    CITED.
 A6 tr R >= 1 does NOT contradict M > 0: the reserve condition
    1 - tr R > 0 is strictly stronger than positive definiteness.
    The joint tier can therefore leak even though every member of
    it is certified positive definite.  This is stated so that a
    LEAK verdict is not misread as a contradiction with CCLXXVII.
 A7 the mission sketch writes the joint constraint with 'the
    certified floor'.  Two readings exist: the CLASS-UNIFORM floor
    c_class and the member's OWN certified co-block floor
    lambda_min(J_B).  At the class-uniform floor the constraint
    EXCLUDES most of the truth ladder -- CCLXV already reported the
    ladder max bound 2.1609 at the widened global floor 0.3146 --
    so the class would not contain truth and the extremal test
    would be vacuous.  The joint relation is therefore evaluated at
    the member's OWN co-block floor, which is exactly CCLXXVII's
    per-step object lifted to the class; the class-uniform variant
    is reported alongside it in the census as the disclosed cost.
    Smoke-1 is the disclosure event for this amendment (it ran the
    class-uniform reading and 10 of 11 ladder cells fell out).
 A8 the anti-circularity ward is MOMENT LOCALITY, not sign-flip
    invariance: sigma = q/n is INVARIANT under M -> -M (both n and
    s change sign), so flip invariance is necessary but NOT
    sufficient.  Smoke-1 is the disclosure event: the flip control
    on sigma was silent (0.0e+00) and is replaced by the decisive
    ward -- RADAU_K and the moment box depend only on
    (nu_0..nu_{2K-2}), i.e. only on the Jacobi coordinates
    (a_1; b_2..b_K; a_2..a_K), so a perturbation of the DEEP TAIL
    leaves them exactly unchanged while sigma moves.
 A9 the closed-form Lambda and the SHIFT-RADAU floor are two
    INDEPENDENTLY valid lower bounds for lambda_1 and neither
    dominates the other (Lambda may consume a deeper moment depth
    through rho, SHIFT-RADAU tracks the secular function directly).
    Smoke-1 is the disclosure event: an ordering ward between them
    failed on 6 of 12 cells because it is not a theorem.  The chain
    therefore uses lambda_bad_lo = max of the two and wards
    VALIDITY (both <= lambda_1 truth), never an ordering.
 A10 the class-uniform form in (d) needs a pivot floor.  It is NOT
    taken from the measured truth minimum (that would be an extra
    premise smuggled into a 'class-uniform' statement); it is
    DERIVED from the class itself as n >= RADAU_K/t_R >= q/t_R >=
    nu_0/(L t_R) >= nu_0_lo/(L t_R), using E3, the KS radius
    constraint lambda_max <= L and the MOM lower edge.  The measured
    floor is printed alongside as a diagnostic only.
 A11 the extremal search seeds TWO declared adversarial corner
    families in OPPOSITE directions, so that the search is not
    biased toward the closure answer: pivot at its box floor with
    the coupling a_1 at its CEILING (the sigma-blow-up corner, which
    RAD is designed to cut) and pivot at its box floor with a_1 at
    its FLOOR (the SCALE corner, where n and a_1 shrink together, so
    sigma and the scale-invariant ratio RADAU_K/n stay put while
    lambda_1(J) -> 0 and R(lambda_1) -> 1).  Smoke-2 is the
    disclosure event: its bridge cell had tr R = 4.85 at
    RADAU_4/n = 0.586, i.e. INSIDE the joint relation, which
    identified the scale corner as the live leak mechanism.
 A12 the F0 census is split.  The KS ENTRY BOX is frozen from the
    DEPLOYED LADDER and therefore makes no claim about off-ladder
    cells; requiring F0 to lie inside it is a category error
    (smoke-2 disclosure: the F0 cell failed the entry box by
    -5.8e-01 while satisfying every joint constraint).  N2 therefore
    wards the box-free statement -- every F0 cell satisfies n > 0,
    MOM and RAD at the depth A1 declares for this family (K = 5) --
    and reports both the K = 4 count and the entry-box membership
    separately as disclosed facts.  Frozen run 1 is the disclosure
    event: N2 demanded BOTH depths at once, which contradicts A1,
    and the sigma-max cell kz 45 failed it at K = 4 exactly as A1
    had predicted.
 A13 the frozen run is repeated once after that correction, and the
    repeat also adds the DEFINITENESS tier D (inf lambda_1(J) over
    the joint class, with the separate-envelope tier as the control
    that must fire).  Rationale: run 1 answered the RESERVE question
    (sup tr R) and found the K = 5 tier leaking at 1.0411 with a
    STRICTLY POSITIVE lambda_1 at the witness, so the strictly
    weaker definiteness question of A6 -- the one CCLXXVII actually
    settles per step -- was left unmeasured at class level.  Both
    SPEC_SHAs are printed in the note.
"""
import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
from scipy import optimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)
import bfloor_perstep_certification_probe as bf  # noqa: E402 (RO)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
PF_TIE = 2.0e-8
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
IDENT_TIE = 1.0e-12
REPRO_RTOL = 5.0e-2
RES_MED_REF = 0.9195
RES_MIN_REF = 2.730e-2
SIGMA_MAX_REF = 0.604556
F0_SIGMA_REF = 0.709925
BOUND4_REF = 0.648113
SUP_NOCAP_REF = 2.2551
SUP_NOCAP_BAR = 1.0
TRUTH_TRR_REF = 0.9727
MARGIN_FRAC = 0.10
MOM_MARGIN = 0.10
FEAS_TOL = 1.0e-9
KDEG = 4
KDEG5 = 5
T_R = Fraction(7809, 10000)
T_R_F = float(T_R)
F0_CAP = 12
BIS_ITERS = 40
RADAU_SIGN_TIE = 1.0e-12
NODE_TIE = 1.0e-9
XR_TIE = 1.0e-6
ENV_LO = 1.0e-7
ENV_GRID = 40000
ENV_TEST = 400
MAP_MS = 20
MAP_DE = 140
CONF_MS = 40
CONF_DE = 280
DE_POP = 20
SLSQP_MAXIT = 150
OPT_SEED = 20260812
PEN_W = 1.0e4
QBITS = 12
CTRL_COUPLE = 10.0
CTRL_PIVOT = 0.05
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CB_F = float(ob.CB_CITED)
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

# CCLXXV citations (declared constants; NOT recomputed here).
PICK_Y = (2100.0, 4200.0, 8400.0, 16800.0, 33600.0,
          49743.176671938345)
PICK_PHI = 2.116960965
PICK_STURM = 3.16e-7
# CCLXXIII citation (declared; the edge family is NOT rebuilt, A5).
EDGE_STEPS_CITED = 111
EDGE_SIGMA_CITED = 0.670393

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: the JOINT-constraint path may see the wall ENTRIES (theta) and
# frozen constants only -- never the Schur quotient, the gap, the
# wall margin/trace, a read, a ladder identifier or ANY eigensolver.
CLASS_BANNED = ("sigma", "sigma_quotient", "sigma_cap_con", "schur",
                "gap", "s_gap", "trace_r", "trace_R", "tr_r_of_theta",
                "margin", "reserve", "lu_read", "assemble_step",
                "build_rung", "artifact", "h", "tau", "lamB1",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "row", "rows", "step", "steps", "scalar_r",
                "q_wall", "lam_1")
CLASS_FUNCS = ("moment_vector", "radau_from_entries", "radau_con",
               "moment_box_con", "pivot_con", "theta_matrices",
               "lanczos_pair", "radau_upper", "lambda_closed")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

COORD = tuple(["b%d" % (i + 1) for i in range(NDIM)]
              + ["a%d" % (i + 1) for i in range(NDIM - 1)])


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


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(values):
    v = np.asarray(values, float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return (float("nan"),) * 3
    return (float(np.min(v)), float(np.median(v)), float(np.max(v)))


def e3(values):
    return "%.3e/%.3e/%.3e" % trio(values)


def f4(values):
    return "%.4f/%.4f/%.4f" % trio(values)


def linfit(x, y):
    """OLS y = a + s x (CCLIII verbatim); returns s, 2SE, R^2, a."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan"), float(ym)
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * xm
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, 2.0 * se, r2, a


def screen(values, scales, label):
    """CCXLVII relocation screen, bars inherited verbatim."""
    v = np.asarray(values, float)
    s = np.asarray(scales, float)
    pos = (v > 0.0) & (s > 0.0) & np.isfinite(v) & np.isfinite(s)
    if int(np.sum(pos)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(pos))),
                "VAC")
    slope, _2se, r2, _a = linfit(np.log(s[pos]), np.log(v[pos]))
    verd = ("PASS" if abs(slope) <= SLOPE_PASS
            else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope=%+.3f,R2=%.3f,%d excl)"
            % (label, verd, slope, r2, int(np.sum(~pos))), verd)


# ================================== L: (a) THE NO-GO LEMMA (sympy)
def no_go_lemma():
    section("L -- (a) THE NO-GO LEMMA: high-pole blindness, warded "
            "SYMBOLICALLY; PICK-DEAD is its empirical instance")
    import sympy as sp
    eps, yy = sp.symbols("epsilon y", positive=True)
    # m_nu(z) = int d nu(x) / (x - z); the decision flip moves the
    # single bad unit atom from +eps to -eps.
    m_pos = 1 / (eps - sp.I * yy)
    m_neg = 1 / (-eps - sp.I * yy)
    d_m = sp.simplify(m_pos - m_neg)
    closed = 2 * eps / (eps ** 2 + yy ** 2)
    w1 = sp.simplify(d_m - closed) == 0
    check("L1 EXACT Delta m(i y) = 1/(eps - i y) - 1/(-eps - i y) = "
          "2 eps / (eps^2 + y^2)  [sympy simplify == 0]", w1,
          kill="K2")
    slack = sp.simplify(2 * eps / yy ** 2 - closed)
    slack_t = sp.simplify(slack
                          - 2 * eps ** 3 / (yy ** 2
                                            * (eps ** 2 + yy ** 2)))
    w2 = (slack_t == 0)
    check("L2 EXACT the lemma 2 eps/(eps^2 + y^2) <= 2 eps/y^2 with "
          "explicit nonnegative slack 2 eps^3 / (y^2 (eps^2 + y^2))",
          w2, kill="K2")
    w2b = bool((2 * eps ** 3
                / (yy ** 2 * (eps ** 2 + yy ** 2))).is_positive)
    check("L3 the slack is POSITIVE for eps > 0, y > 0 (sympy "
          "assumption query) -- the high-pole read is strictly "
          "blind, never exactly informative", w2b, kill="K2")
    # the contrast: the low-pole / moment functional q = int x^-1 dnu
    d_q = sp.simplify(1 / eps - 1 / (-eps))
    w3 = sp.simplify(d_q - 2 / eps) == 0
    check("L4 EXACT the SAME flip moves the low-pole functional "
          "q = int x^{-1} d nu by 2 / eps (unbounded as eps -> 0)",
          w3, kill="K2")
    ratio = sp.simplify(d_q / closed)
    w4 = sp.simplify(ratio - (eps ** 2 + yy ** 2) / eps ** 2) == 0
    check("L5 EXACT sensitivity ratio (low-pole)/(high-pole) = "
          "(eps^2 + y^2)/eps^2 >= y^2/eps^2 -- the permanent typing "
          "'moments, not high poles'", w4, kill="K2")
    print("    QUANTITATIVE INSTANCE on the CCLXXV frozen disk "
          "ladder (declared constants, NOT recomputed here); the "
          "blindness budget 2 eps / y^2 at eps = c_B = %.4f:" % CB_F)
    for yv in PICK_Y:
        print("      Y = %-20.10g  2 eps / Y^2 = %.3e"
              % (yv, 2.0 * CB_F / (yv * yv)))
    print("    EMPIRICAL INSTANCE (CCLXXV, cited): the corrected "
          "interlacing Stieltjes/Pick class over exactly this disk "
          "ladder is PICK-DEAD in BOTH tiers -- an exact "
          "one-bad-atom witness reaches Phi = %.9f >= 1 and the "
          "rational Sturm dual encloses the number to %.2e.  The "
          "lemma explains it: no disk radius above the blindness "
          "budget can separate the decision, and every deployed "
          "radius is far above it."
          % (PICK_PHI, PICK_STURM))
    print("    CONSEQUENCE, frozen: the class-level object must be "
          "built from LOW-POLE / MOMENT information (the b-weighted "
          "moments nu_k and the certified co-block floor), which is "
          "exactly what the Gauss-Radau functional consumes.")


# ============================== the class functions (AC-scanned)
def theta_matrices(theta):
    """theta = (b_1..b_8, a_1..a_7) -> (J, J_B).  theta only."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def moment_vector(theta, kdeg):
    """nu_k = b^T B^k b, k = 0..2*kdeg-2, from the ENTRIES only.
    In Jacobi coordinates the coupling vector is (a_1, 0, ..., 0)
    and B = J_B.  No eigensolver, no inverse, no pivot read."""
    jm, blk = theta_matrices(theta)
    vec = np.asarray(jm, float)[1:, 0]
    out = []
    cur = vec.copy()
    for _k in range(2 * kdeg - 1):
        out.append(float(vec @ cur))
        cur = blk @ cur
    return np.asarray(out, float)


def lanczos_pair(matrix, kdeg):
    """Lanczos data of (B, b/||b||) from the wall ENTRIES (CCLXV
    verbatim); forward recursion only."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    dim = blk.shape[0]
    nrm = float(np.linalg.norm(vec))
    if not math.isfinite(nrm) or nrm <= 0.0:
        return None
    frame = np.zeros((dim, kdeg))
    frame[:, 0] = vec / nrm
    alp = []
    bet = []
    for j in range(kdeg):
        zvec = blk @ frame[:, j]
        aj = float(frame[:, j] @ zvec)
        alp.append(aj)
        zvec = zvec - aj * frame[:, j]
        if j > 0:
            zvec = zvec - bet[j - 1] * frame[:, j - 1]
        for _ in range(2):
            zvec = zvec - frame[:, :j + 1] @ (frame[:, :j + 1].T
                                              @ zvec)
        if j == kdeg - 1:
            break
        nz = float(np.linalg.norm(zvec))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(aj)):
            return None
        bet.append(nz)
        frame[:, j + 1] = zvec / nz
    return np.asarray(alp, float), np.asarray(bet, float), nrm * nrm


def radau_upper(alp, bet, floor_c, mass):
    """E3 Gauss-Radau upper bound for b^T B^{-1} b at depth
    K = len(alp) with the node prescribed at floor_c (CCLXV
    verbatim); the node ward is done by the CALLER."""
    kdeg = len(alp)
    jac = np.diag(np.asarray(alp, float)).copy()
    for i in range(kdeg - 1):
        jac[i, i + 1] = jac[i + 1, i] = float(bet[i])
    if kdeg > 1:
        shifted = jac[:kdeg - 1, :kdeg - 1] - floor_c * np.eye(
            kdeg - 1)
        rhs = np.zeros(kdeg - 1)
        rhs[-1] = float(bet[kdeg - 2]) ** 2
        try:
            sol = np.linalg.solve(shifted, rhs)
        except np.linalg.LinAlgError:
            return float("nan"), None
        jac[kdeg - 1, kdeg - 1] = floor_c + float(sol[-1])
    else:
        jac[0, 0] = floor_c
    unit = np.zeros(kdeg)
    unit[0] = 1.0
    try:
        val = float(np.linalg.solve(jac, unit)[0]) * mass
    except np.linalg.LinAlgError:
        return float("nan"), None
    return val, jac


def radau_from_entries(theta, kdeg, floor_c):
    """RADAU_K(nu_0..nu_{2K-2}; floor_c): CCLXXVII's bound functional
    of the moment data and the certified floor, evaluated by the
    numerically stable Lanczos route on the ENTRIES (amendment A3).
    Returns nan on a degenerate recursion."""
    jmat, _blk = theta_matrices(theta)
    lan = lanczos_pair(jmat, kdeg)
    if lan is None:
        return float("nan")
    alp, bet, mass = lan
    val, _jac = radau_upper(alp, bet, floor_c, mass)
    return val


def lambda_closed(pivot, floor_c, rho):
    """R3, closed form: Lambda(n, c, rho) =
    ((n + c) - sqrt((n - c)^2 + 4 n c rho)) / 2, the SOURCE-ONLY
    lower bound for the single eigenvalue below the co-block floor.
    Positive iff rho < 1 (with n, c > 0)."""
    if not (pivot > 0.0 and floor_c > 0.0) or not math.isfinite(rho):
        return float("nan")
    disc = (pivot - floor_c) ** 2 + 4.0 * pivot * floor_c * rho
    if disc < 0.0:
        return float("nan")
    return 0.5 * ((pivot + floor_c) - math.sqrt(disc))


def pivot_con(theta):
    """The SOURCE-ONLY entry fact n = M[0,0] > 0, normalized."""
    return float(theta[0])


def moment_box_con(theta, kdeg, mlo, mhi):
    """MOM: the SEPARATE per-carrier envelope of each moment, in log
    space (amendment A2).  Entries and frozen constants only."""
    momv = moment_vector(theta, kdeg)
    out = []
    for k in range(len(momv)):
        val = float(momv[k])
        if not (val > 0.0) or not math.isfinite(val):
            out.append(-1.0)
            out.append(-1.0)
            continue
        wid = max(math.log(mhi[k]) - math.log(mlo[k]), 1e-12)
        out.append((math.log(val) - math.log(mlo[k])) / wid)
        out.append((math.log(mhi[k]) - math.log(val)) / wid)
    return np.asarray(out, float)


def radau_con(theta, kdeg, floor_c, t_cap):
    """RAD: the JOINT relation RADAU_K(nu; c) <= t_cap * n, as a
    normalized slack.  Entries, the supplied floor and frozen
    constants only -- never the Schur quotient, never an
    eigensolver, never a read."""
    pivot = float(theta[0])
    if not (pivot > 0.0) or not math.isfinite(floor_c) \
            or floor_c <= 0.0:
        return -1.0
    val = radau_from_entries(theta, kdeg, floor_c)
    if not math.isfinite(val) or val < 0.0:
        return -1.0
    return (t_cap * pivot - val) / max(abs(t_cap * pivot), 1e-12)


def coblock_floor(theta):
    """P2, the CO-BLOCK PREMISE: lambda_min(J_B).  A spectral fact
    about B alone; certified per cell by the round-62 exact LDL and
    warded independent of the pivot and coupling coordinates (AC6).
    This function is deliberately OUTSIDE the AST-scanned joint
    path -- it is the one premise the path is allowed to consume."""
    _jm, jb = theta_matrices(theta)
    try:
        return float(np.linalg.eigvalsh(jb)[0])
    except np.linalg.LinAlgError:
        return float("nan")


def radau_self_con(theta, kdeg, t_cap):
    """RAD at the member's OWN certified co-block floor (amendment
    A7): exactly CCLXXVII's per-step object lifted to the class."""
    return radau_con(theta, kdeg, coblock_floor(theta), t_cap)


# ============ the inherited CCLXI functionals (typed, not re-scanned)
def ks_wall_functionals(theta, cls):
    """CCLXI verbatim: wall-side sum-rule functionals on [0, L]."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    ll = cls["L"]
    aa = 4.0 * ad / ll
    bb = (4.0 * bd - 2.0 * ll) / ll
    ks = float(np.sum((aa - 1.0) ** 2) + np.sum(bb ** 2))
    if np.any(aa <= 0.0):
        coef = -float("inf")
    else:
        coef = float(np.sum(np.log(aa))) - 0.5 * math.log(2.0)
    jm, _jb = theta_matrices(theta)
    try:
        evals, evecs = np.linalg.eigh(jm)
    except np.linalg.LinAlgError:
        return ks, coef, float("inf")
    ww = np.maximum(evecs[0, :] ** 2, 1e-300)
    spread = -0.5 * float(np.mean(np.log(NDIM * ww)))
    return ks, coef, spread


def class_slack_vector(theta, cls):
    """CCLXI verbatim: normalized slack vector of C_KS at theta
    (>= 0 iff inside)."""
    theta = np.asarray(theta, float)
    lo, hi, wd = cls["lo"], cls["hi"], cls["wd"]
    out = []
    names = []
    for i in range(len(theta)):
        out.append((theta[i] - lo[i]) / wd[i])
        names.append("box_lo[%s]" % cls["coord"][i])
        out.append((hi[i] - theta[i]) / wd[i])
        names.append("box_hi[%s]" % cls["coord"][i])
    ad = theta[NDIM:]
    for k in range(NDIM - 1):
        out.append(ad[k] / wd[NDIM + k])
        names.append("a_pos[a%d]" % (k + 1))
    jm, jb = theta_matrices(theta)
    if np.all(np.isfinite(jm)):
        evj = np.linalg.eigvalsh(jm)
        evb = np.linalg.eigvalsh(jb)
        out.append((float(evb[0]) - cls["cb"]) / cls["cb"])
        names.append("B_floor")
        out.append((cls["L"] - float(evj[-1])) / cls["L"])
        names.append("radius_hi")
        out.append((float(evj[0]) + cls["L"]) / cls["L"])
        names.append("radius_lo")
    else:
        out.extend([-1.0, -1.0, -1.0])
        names.extend(["B_floor", "radius_hi", "radius_lo"])
    ks, coef, spread = ks_wall_functionals(theta, cls)
    out.append((cls["ks_cap"] - ks) / max(cls["ks_cap"], 1.0))
    names.append("KS_wall")
    out.append((coef - cls["coef_lo"]) / cls["coef_w"])
    names.append("COEF_lo")
    out.append((cls["coef_hi"] - coef) / cls["coef_w"])
    names.append("COEF_hi")
    out.append((spread - cls["spr_lo"]) / cls["spr_w"])
    names.append("SPREAD_lo")
    out.append((cls["spr_hi"] - spread) / cls["spr_w"])
    names.append("SPREAD_hi")
    return np.asarray(out, float), names


def sigma_quotient(theta):
    """THE CIRCULAR OBJECT (reference and control only): the Schur
    quotient sigma = a_1^2 [J_B^-1]_11 / b_1 = 1 - s/n."""
    _jm, jb = theta_matrices(theta)
    b1 = float(theta[0])
    a1 = float(theta[NDIM])
    if b1 == 0.0:
        return float("inf")
    try:
        e1 = np.zeros(NDIM - 1)
        e1[0] = 1.0
        mb = float(np.linalg.solve(jb, e1)[0])
    except np.linalg.LinAlgError:
        return float("inf")
    return a1 * a1 * mb / b1


def tr_r_of_theta(theta, fdata):
    """tr R(J(theta)) by the eigenvalue route (the frozen filter is
    a constant)."""
    jm, _jb = theta_matrices(theta)
    if not np.all(np.isfinite(jm)):
        return float("nan")
    evals = np.linalg.eigvalsh(jm)
    return math.fsum(zol.scalar_r(fdata, float(v)) for v in evals)


# ====================================================== wall ladder
def build_ladder():
    section("W -- the CCVII/CCXXV wall ladder, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
        print("    SMOKE: %d contiguous surface rungs" % len(zones))
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W2 all surface chains complete",
          all(r is not None for r in surface), kill="K1")
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    if SMOKE:
        census = census[:3]
    deep = []
    for kz, hz in census:
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep
               if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    combined = sorted([r for r in surface
                       if r is not None and r["core_ok"]] + deep_ok,
                      key=lambda r: (r["h"], r["kz"]))
    steps = ob.make_steps(combined)
    for st in steps:
        zol.assemble_step(st)
    steps = [st for st in steps if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in steps]
    ok = (SMOKE or (len(steps) == STEPS_EXP
                    and segs.count("surf") == 40
                    and segs.count("bridge") == 1
                    and segs.count("deep") == 27))
    check("W3 combined steps %d = surface %d + bridge %d + deep %d"
          % (len(steps), segs.count("surf"), segs.count("bridge"),
             segs.count("deep")), ok, kill="K1")
    return steps, combined


def artifact_key_ward(steps):
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("W4a CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"]))
              for r in artifact["rungs"]}
    ours = {(int(st["r1"]["h"]), int(st["r1"]["kz"]),
             int(st["r2"]["h"]), int(st["r2"]["kz"]))
            for st in steps}
    n_match = len(stored & ours)
    check("W4b ladder identity: %d/%d step keys match the stored "
          "CCXLVII artifact" % (n_match, len(ours)),
          SMOKE or (n_match == STEPS_EXP and len(ours) == STEPS_EXP),
          kill="K2")
    return artifact


def build_f0(anchors):
    """The CCLXIX/CCLXXVII F0 family verbatim: off-ladder frame-A
    zones (descending h, cap F0_CAP), chain steps + one bridge step
    per rung from the nearest registered truth predecessor."""
    section("F0 -- the CCLXIX off-ladder zone, rebuilt verbatim")
    f0_cap = 2 if SMOKE else F0_CAP
    reg = set(ob.ladder_zones())
    f0_zones = [kz for kz in core.frame_a_zones() if kz not in reg]
    f0_pick = sorted(f0_zones,
                     key=lambda kz: -ob.window_of(kz)["h"])[:f0_cap]
    f0_rungs = []
    for kz in f0_pick:
        rr = ob.build_rung("surf", kz, with_split=False)
        if rr is not None:
            f0_rungs.append(rr)
    fam = sorted([r for r in f0_rungs if r.get("core_ok")],
                 key=lambda r: (r["h"], r["kz"]))
    pairs = list(zip(fam, fam[1:]))
    anc = sorted(anchors, key=lambda r: r["h"])
    for r2 in fam:
        below = [a for a in anc if a["h"] <= r2["h"]]
        r1 = below[-1] if below else anc[0]
        pairs.append((r1, r2))
    out = []
    n_ref = 0
    for r1, r2 in pairs:
        sts = ob.make_steps([r1, r2])
        if not sts:
            n_ref += 1
            continue
        st = sts[0]
        zol.assemble_step(st)
        if st["status"] != "OK":
            n_ref += 1
            continue
        kind = ("chain" if r1.get("kind") == r2.get("kind")
                and r1 in fam else "bridge")
        out.append((st, kind))
    print("    F0 census: %d zones off-ladder, %d picked, %d built, "
          "%d steps admitted (%d chain, %d bridge), %d step-refused"
          % (len(f0_zones), len(f0_pick), len(f0_rungs), len(out),
             sum(1 for _s, k in out if k == "chain"),
             sum(1 for _s, k in out if k == "bridge"), n_ref))
    check("F0.1 the CCLXIX F0 family admitted %d wall-legal cells"
          % len(out), len(out) >= (1 if SMOKE else 8), kill="K1")
    return out


def get_filter(steps, artifact):
    poles_art = np.asarray([complex(*p)
                            for p in artifact["filter"]["poles"]],
                           complex)
    res_art = np.asarray(artifact["filter"]["residues"], float)
    l_art = float(artifact["filter"]["L"])
    global_l = (l_art if SMOKE
                else max(st["L_src"] for st in steps))
    fdata = zol.build_filter(CB_F, global_l, NDIM)
    dev_l = abs(global_l - l_art) / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fdata["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fdata["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("T1 fixed CCXXV GLOBAL m=8 filter rebuilt: L rel %.2e, "
          "poles %.2e, residues %.2e <= %.0e"
          % (dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    print("    separator facts (CCXXV interval certificates, "
          "re-consumed): global R lower %.3e >= 0 (outward), bulk "
          "delta %.6e on [c_B, L] = [%.6f, %.6g]"
          % (fdata["global_R_lower"], fdata["delta"], CB_F,
             fdata["L"]))
    return fdata


def make_rows(steps, f0_cells, artifact, fdata):
    section("T -- per-cell reads: LU partial fractions vs artifact "
            "vs eigen route")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_tr = d_marg = d_eig = 0.0
    n_match = 0
    cells = [(st, ob.seg_of(st)) for st in steps] \
        + [(st, "F0") for st, _k in f0_cells]
    for idx, (st, seg) in enumerate(cells):
        key = (int(st["r1"]["h"]), int(st["r1"]["kz"]),
               int(st["r2"]["h"]), int(st["r2"]["kz"]))
        src = stored.get(key)
        trace_lu = zol.trace_filter_lu(st["Mt"], fdata)
        trace_eig = math.fsum(zol.scalar_r(fdata, float(v))
                              for v in st["eigs"])
        d_eig = max(d_eig, abs(trace_lu - trace_eig))
        if src is not None:
            n_match += 1
            d_tr = max(d_tr, abs(trace_lu - float(src["trace_R"])))
            d_marg = max(d_marg, abs((1.0 - trace_lu)
                                     - float(src["margin"])))
        rows.append(dict(index=idx, step=st, seg=seg,
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         l_src=float(st["L_src"]),
                         trace_r=trace_lu,
                         reserve=1.0 - trace_lu))
    check("T2 LU trace_R / margin reproduce the stored artifact on "
          "%d matched cells: %.2e / %.2e <= %.0e"
          % (n_match, d_tr, d_marg, LU_TIE),
          n_match >= 1 and d_tr <= LU_TIE and d_marg <= LU_TIE
          and (SMOKE or n_match == STEPS_EXP), kill="K2")
    check("T3 eigen-route trace == LU partial-fraction trace on all "
          "%d cells: max dev %.2e <= %.0e"
          % (len(rows), d_eig, PF_TIE), d_eig <= PF_TIE, kill="K2")
    lad = [r for r in rows if r["seg"] != "F0"]
    reserves = np.asarray([r["reserve"] for r in lad], float)
    med, mn = float(np.median(reserves)), float(np.min(reserves))
    ok_rep = (abs(med / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(mn / RES_MIN_REF - 1.0) <= REPRO_RTOL)
    check("T5 REPRO CCXLVII ladder reserve med %.4f (ref %.4f), min "
          "%.4e (ref %.3e), rtol %.0e"
          % (med, RES_MED_REF, mn, RES_MIN_REF, REPRO_RTOL),
          SMOKE or ok_rep, kill="K3")
    print("    ladder reserve = 1 - tr R: %s; ladder max tr R = "
          "%.6f (CCLXVII truth-best ref %.4f)"
          % (e3(reserves), float(np.max([r["trace_r"] for r in lad])),
             TRUTH_TRR_REF))
    return rows


# ============================= B/I: translation + identity wards
def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- CCLIII/CCLXI/CCLXV
    machinery reproduced verbatim.  Returns (a, b, Q) or None."""
    if not np.all(np.isfinite(matrix)):
        return None
    n = NDIM
    qq = np.zeros((n, n))
    qq[0, 0] = 1.0
    a = np.zeros(n - 1)
    b = np.zeros(n)
    for k in range(n):
        z = matrix @ qq[:, k]
        b[k] = float(qq[:, k] @ z)
        z = z - b[k] * qq[:, k]
        if k > 0:
            z = z - a[k - 1] * qq[:, k - 1]
        for _ in range(2):
            z = z - qq[:, :k + 1] @ (qq[:, :k + 1].T @ z)
        if k == n - 1:
            break
        nz = float(np.linalg.norm(z))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b, qq


def jacobi_identity_wards(rows):
    section("B/I -- Jacobi translation + the CCLXV identity wards "
            "on every cell")
    d_b1 = d_a1 = d_bfl = d_m0 = d_q = d_sig = d_gap = d_nu = 0.0
    n_bad = 0
    for row in rows:
        st = row["step"]
        jf = jacobi_form(st["Mt"])
        if jf is None:
            n_bad += 1
            row["theta"] = None
            continue
        a, b, _qq = jf
        theta = np.concatenate([b, a])
        row["theta"] = theta
        _jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(b[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(a[0] - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        row["lam_b_j"] = lamb
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(_jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["schur"] - 1.0))
        piv = float(st["n0"])
        vec = np.asarray(st["bvec"], float)
        blk = np.asarray(st["Bblk"], float)
        q_wall = float(vec @ np.linalg.solve(blk, vec))
        sig = sigma_quotient(theta)
        row["sigma"] = sig
        row["q_wall"] = q_wall
        d_q = max(d_q, abs(sig * piv - q_wall) / max(1.0, abs(q_wall)))
        d_sig = max(d_sig, abs(sig - q_wall / piv)
                    / max(1.0, abs(sig)))
        d_gap = max(d_gap, abs(sig - (1.0 - row["schur"] / piv))
                    / max(1.0, abs(sig)))
        momv = moment_vector(theta, KDEG5)
        row["nu"] = momv
        d_nu = max(d_nu, abs(momv[0] - float(vec @ vec))
                   / max(1.0, abs(momv[0])))
        row["lam_j"] = np.linalg.eigvalsh(_jm)
        row["lam_jb"] = np.linalg.eigvalsh(jb)
    check("B1 Lanczos form of (M, e_0) exists on all %d cells"
          % len(rows), n_bad == 0, "breakdowns %d" % n_bad, kill="K2")
    check("B2 TRANSLATE b_1 == M[0,0], a_1 == ||M[1:,0]||: %.2e / "
          "%.2e <= %.0e" % (d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill="K2")
    check("B3 TRANSLATE lambda_min(J_B) == lamB1 (E2 compression): "
          "max rel %.2e <= %.0e" % (d_bfl, TRANSLATE_TIE),
          d_bfl <= TRANSLATE_TIE, kill="K2")
    check("B4 WARD m(0) * gap == 1: max %.2e <= %.0e"
          % (d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill="K2")
    check("I1/I2 IDENTITY sigma * n == q == b^T B^-1 b: max rel "
          "%.2e / %.2e <= %.0e" % (d_q, d_sig, IDENT_TIE),
          d_q <= IDENT_TIE and d_sig <= IDENT_TIE, kill="K2")
    check("I3 IDENTITY sigma == 1 - s/n (the CIRCULARITY, restated): "
          "max rel %.2e <= %.0e" % (d_gap, IDENT_TIE),
          d_gap <= IDENT_TIE, kill="K2")
    check("I4 MOMENT WARD nu_0 == b^T b in Jacobi coordinates "
          "(a_1^2): max rel %.2e <= %.0e" % (d_nu, TRANSLATE_TIE),
          d_nu <= TRANSLATE_TIE, kill="K2")
    return [r for r in rows if r["theta"] is not None]


def repro_anchors(rows):
    section("SR -- repro anchors against CCLXV / CCLXIX / CCLXXVII")
    lad = [r for r in rows if r["seg"] != "F0"]
    f0 = [r for r in rows if r["seg"] == "F0"]
    s_lad = max(r["sigma"] for r in lad)
    ok1 = abs(s_lad / SIGMA_MAX_REF - 1.0) <= 2.0e-3
    check("SR1 ladder sigma max %.6f (CCLXV/CCLXIX ref %.6f)"
          % (s_lad, SIGMA_MAX_REF), SMOKE or ok1, kill="K3")
    if f0:
        s_f0 = max(r["sigma"] for r in f0)
        ok2 = abs(s_f0 / F0_SIGMA_REF - 1.0) <= 2.0e-3
        check("SR2 F0 sigma max %.6f (CCLXIX ref %.6f)"
              % (s_f0, F0_SIGMA_REF), SMOKE or ok2, kill="K3")
    pivs = [r["n_piv"] for r in rows]
    n_pos = sum(1 for p in pivs if p > 0.0)
    n_exact = sum(1 for r in rows
                  if Fraction(float(r["step"]["Mt"][0, 0])) > 0)
    check("SR3 PIVOT SIGN n = M[0,0] > 0 on all %d cells (float AND "
          "exact rational): %d / %d, min %.6f"
          % (len(rows), n_pos, n_exact, min(pivs)),
          n_pos == len(rows) and n_exact == len(rows), kill="K2")


# ============= C: the certified per-cell floors and Radau values
def certify_cells(rows):
    section("C -- per-cell certified co-block floor (CCLXXVII "
            "round-62 exact LDL, verbatim) and the certified "
            "RADAU_K / n values at K = 4 and K = 5")
    n_ref = 0
    d_xr = 0.0
    n_sign = 0
    n_node = 0
    for row in rows:
        mat = row["step"]["Mt"]
        piv_fr, momv_fr, blk_fr = bf.exact_wall_data(mat,
                                                     2 * KDEG5 - 2)
        lam_hi = Fraction(float(max(row["lam_b_j"], 0.0)))
        cfr = bf.cert_floor_exact(blk_fr, Fraction(0), lam_hi,
                                  iters=BIS_ITERS)
        if cfr is None:
            n_ref += 1
            row["c_cert"] = float("nan")
            row["bound4"] = float("nan")
            row["bound5"] = float("nan")
            continue
        row["c_cert"] = float(cfr)
        for kdeg, tag in ((KDEG, "4"), (KDEG5, "5")):
            cheb = bf.chebyshev_monic(momv_fr[:2 * kdeg - 1], kdeg)
            if cheb is None:
                row["bound%s" % tag] = float("nan")
                continue
            alx, bex = cheb
            qex = bf.radau_exact(alx, bex, cfr, momv_fr[0])
            if qex is None:
                row["bound%s" % tag] = float("nan")
                continue
            row["bound%s" % tag] = float(qex / piv_fr)
            if qex < Fraction(float(row["q_wall"])) \
                    - Fraction(float(RADAU_SIGN_TIE)):
                n_sign += 1
            val_f = radau_from_entries(row["theta"], kdeg,
                                       float(cfr))
            d_xr = max(d_xr, abs(val_f - float(qex))
                       / max(1.0, abs(float(qex))))
            lan = lanczos_pair(row["step"]["Mt"], kdeg)
            if lan is not None:
                _v, jac = radau_upper(lan[0], lan[1], float(cfr),
                                      lan[2])
                if jac is not None:
                    nodes = np.linalg.eigvalsh(jac)
                    if abs(float(nodes[0]) - float(cfr)) > NODE_TIE \
                            * max(1.0, abs(float(cfr))):
                        n_node += 1
    check("C1 exact-rational co-block floor certified on all %d "
          "cells (round-62 LDL, %d bisections): %d refusals"
          % (len(rows), BIS_ITERS, n_ref), n_ref == 0, kill="K2")
    cs = [r["c_cert"] for r in rows if math.isfinite(r["c_cert"])]
    lams = [r["lam_b_j"] for r in rows]
    qual = max(abs(c / lm - 1.0) for c, lm in zip(cs, lams))
    check("C2 floor QUALITY: c_cert <= lambda_min(J_B) on every "
          "cell and within %.2e relative of it" % qual,
          all(c <= lm * (1.0 + 1e-12) for c, lm in zip(cs, lams))
          and qual <= 1e-6, kill="K2")
    check("C3 RB1 the exact Radau value is an UPPER bound of the "
          "truth q = b^T B^-1 b on every cell and depth: %d "
          "violations" % n_sign, n_sign == 0, kill="K2")
    check("C4 NODE ward: the prescribed node stays the smallest node "
          "of the modified rule: %d violations" % n_node,
          n_node == 0, kill="K2")
    check("C5 AMENDMENT A3 exact moment tier == float Lanczos route "
          "for RADAU_K on every cell/depth: max rel %.2e <= %.0e"
          % (d_xr, XR_TIE), d_xr <= XR_TIE, kill="K2")
    lad = [r for r in rows if r["seg"] != "F0"]
    b4 = [r["bound4"] for r in lad if math.isfinite(r["bound4"])]
    ok = abs(max(b4) / BOUND4_REF - 1.0) <= 1e-3 if b4 else False
    check("C6 REPRO CCLXXVII certified K = 4 ladder bound max %.6f "
          "(ref %.6f)" % (max(b4) if b4 else float("nan"),
                          BOUND4_REF), SMOKE or ok, kill="K3")
    print("    c_cert  min/med/max: %s" % e3(cs))
    print("    RADAU_4/n min/med/max: %s"
          % f4([r["bound4"] for r in rows]))
    print("    RADAU_5/n min/med/max: %s"
          % f4([r["bound5"] for r in rows]))
    for tag in ("4", "5"):
        vals = [r["bound%s" % tag] for r in rows
                if math.isfinite(r["bound%s" % tag])]
        n_ok = sum(1 for v in vals if v <= T_R_F)
        print("    cells with RADAU_%s/n <= t_R = %.4f: %d/%d"
              % (tag, T_R_F, n_ok, len(rows)))


# ================================== G: freeze the Radau class
def freeze_class(rows, fdata):
    section("G -- FREEZE the RADAU class (CCLXI construction "
            "verbatim + the source-only MOM box and RAD relation; "
            "all constants printed BEFORE any optimization)")
    lad = [r for r in rows if r["seg"] != "F0"]
    thetas = np.asarray([r["theta"] for r in lad], float)
    t_lo = thetas.min(axis=0)
    t_hi = thetas.max(axis=0)
    width = np.maximum(t_hi - t_lo, 1e-12 * np.maximum(1.0,
                                                       np.abs(t_hi)))
    lo = t_lo - MARGIN_FRAC * width
    hi = t_hi + MARGIN_FRAC * width
    lo[NDIM:] = np.maximum(lo[NDIM:], 0.0)
    cb_use = CB_F
    lamb_min = min(float(np.linalg.eigvalsh(
        theta_matrices(r["theta"])[1])[0]) for r in lad)
    widened = False
    if lamb_min < CB_F:
        cb_use = lamb_min * (1.0 - MARGIN_FRAC)
        widened = True
        print("    WIDENED (disclosed, amendment A4): measured truth "
              "lambda_min(J_B) = %.6f < cited c_B = %.6f; floor "
              "honestly widened to %.6f" % (lamb_min, CB_F, cb_use))
    cls = dict(lo=lo, hi=hi, wd=hi - lo, cb=cb_use, L=fdata["L"],
               coord=COORD)
    funcs = np.asarray([ks_wall_functionals(r["theta"], cls)
                        for r in lad], float)
    ks_max = float(np.max(funcs[:, 0]))
    coef_lo_t, coef_hi_t = float(np.min(funcs[:, 1])), \
        float(np.max(funcs[:, 1]))
    spr_lo_t, spr_hi_t = float(np.min(funcs[:, 2])), \
        float(np.max(funcs[:, 2]))
    coef_w = max(coef_hi_t - coef_lo_t, 1e-12)
    spr_w = max(spr_hi_t - spr_lo_t, 1e-12)
    cls.update(ks_cap=ks_max * (1.0 + MARGIN_FRAC),
               coef_lo=coef_lo_t - MARGIN_FRAC * coef_w,
               coef_hi=coef_hi_t + MARGIN_FRAC * coef_w,
               coef_w=coef_w,
               spr_lo=spr_lo_t - MARGIN_FRAC * spr_w,
               spr_hi=spr_hi_t + MARGIN_FRAC * spr_w,
               spr_w=spr_w)
    print("    coord        truth_min      truth_max       box_lo"
          "         box_hi")
    for i, cn in enumerate(COORD):
        print("    %-5s %14.6g %14.6g %14.6g %14.6g"
              % (cn, t_lo[i], t_hi[i], lo[i], hi[i]))
    print("    B-floor c_B = %.6f (%s); L = %.8g; KS_wall cap "
          "%.6f; COEF box [%.6f, %.6f]; SPREAD box [%.6f, %.6f]"
          % (cls["cb"], "WIDENED" if widened else "CITED CLIII",
             cls["L"], cls["ks_cap"], cls["coef_lo"], cls["coef_hi"],
             cls["spr_lo"], cls["spr_hi"]))
    # ---- the MOM box: per-carrier envelopes, log space (A2)
    n_mom = 2 * KDEG5 - 1
    mom = np.asarray([r["nu"][:n_mom] for r in lad], float)
    mlo_t = mom.min(axis=0)
    mhi_t = mom.max(axis=0)
    mlo = np.zeros(n_mom)
    mhi = np.zeros(n_mom)
    print("    MOM box (measured FLAT over the %d ladder cells, "
          "widened by %.2f of the LOG width -- amendment A2):"
          % (len(lad), MOM_MARGIN))
    check("G0 every truth moment nu_0..nu_%d is strictly positive "
          "(the co-block floor forces B > 0, so the LOG box of "
          "amendment A2 is well posed)" % (n_mom - 1),
          bool(np.all(mom > 0.0)), kill="K2")
    for k in range(n_mom):
        lo_k = max(float(mlo_t[k]), 1e-300)
        hi_k = max(float(mhi_t[k]), lo_k)
        wid = math.log(hi_k) - math.log(lo_k)
        mlo[k] = math.exp(math.log(lo_k) - MOM_MARGIN * wid)
        mhi[k] = math.exp(math.log(hi_k) + MOM_MARGIN * wid)
        print("      nu_%d  truth [%.6e, %.6e]  box [%.6e, %.6e]  "
              "log-decades %.2f"
              % (k, mlo_t[k], mhi_t[k], mlo[k], mhi[k],
                 wid / math.log(10.0)))
    cls["mlo"] = mlo
    cls["mhi"] = mhi
    cls["t_r"] = T_R_F
    # the pivot floor is DERIVED from the class, not assumed:
    # RADAU_K >= q >= nu_0 / lambda_max(B) >= nu_0_lo / L (E3 plus
    # the KS radius constraint), and RAD gives n >= RADAU_K / t_R.
    cls["piv_lo"] = mlo[0] / (cls["L"] * cls["t_r"])
    cls["piv_lo_meas"] = float(np.min([r["n_piv"]
                                       for r in lad])) \
        * (1.0 - MARGIN_FRAC)
    jbs = np.asarray([np.sort(r["lam_jb"]) for r in lad], float)
    cls["jb_floor"] = jbs.min(axis=0)
    print("    RAD relation: RADAU_K(nu_0..nu_{2K-2}; c_B) <= t_R * "
          "n with t_R = %.4f (= SIGMA_ENV, CCLXIX registration at "
          "its cited 4-digit truncation); K in {%d, %d}"
          % (T_R_F, KDEG, KDEG5))
    print("    auxiliary geometry (used ONLY in section A, both "
          "definiteness-blind): pivot floor n >= %.6e, DERIVED from "
          "the class as nu_0_lo / (L * t_R) = %.6e / (%.1f * %.4f) "
          "[measured truth floor, a diagnostic only: %.6e]; co-block "
          "spectral floors f_j = %s"
          % (cls["piv_lo"], mlo[0], cls["L"], cls["t_r"],
             cls["piv_lo_meas"],
             " ".join("%.4g" % v for v in cls["jb_floor"])))
    frozen = np.concatenate([lo, hi, mlo, mhi,
                             [cls["cb"], cls["L"], cls["ks_cap"],
                              cls["coef_lo"], cls["coef_hi"],
                              cls["spr_lo"], cls["spr_hi"],
                              cls["t_r"], cls["piv_lo"]],
                             cls["jb_floor"]])
    box_sha = hashlib.sha256(frozen.tobytes()).hexdigest()
    check("G1 class frozen BEFORE optimization (box SHA-256 %s%s)"
          % (box_sha[:16], "; B-floor WIDENED, disclosed"
             if widened else ""), True)
    cls["box_sha"] = box_sha
    cls["widened"] = widened
    return cls


# ================================ AC: the anti-circularity typing
def ac_typing(rows, cls):
    section("AC -- ANTI-CIRCULARITY, strict: what each constraint "
            "is allowed to see, and the wards that enforce it")
    print("""    constraint        consumes                    typing
    ----------------  --------------------------  --------------
    entry box         theta (entries)             SOURCE-ONLY
    a_i > 0           theta (entries)             SOURCE-ONLY
    KS_wall / COEF    theta (entries)             SOURCE-ONLY
    MOM box           nu_0..nu_{2K-2}(theta)      SOURCE-ONLY,
                                                  MOMENT-LOCAL
    RAD relation      nu_0..nu_{2K-2}, c, n       SOURCE-ONLY,
                                                  MOMENT-LOCAL
    n > 0             theta[0] = M[0,0]           SOURCE-ONLY
    c = lambda_min(J_B) spec(J_B)                 CO-BLOCK PREMISE
                                                  (P2, certified)
    radius / SPREAD   spec(J)                     WALL-SPECTRAL,
                                                  FLIP-INVARIANT
    sigma <= t        b^T B^{-1} b (the FULL      CIRCULAR (= the
                      co-block resolvent)         conclusion)""")
    rng = np.random.default_rng(OPT_SEED)
    sample = [np.asarray(r["theta"], float) for r in rows[:12]]
    while len(sample) < 24:
        sample.append(rng.uniform(cls["lo"], cls["hi"]))
    # AC1/AC2: the definiteness flip J -> -J (re-gauged to a_i > 0).
    d_spread = 0.0
    d_radius = 0.0
    d_sig_flip = 0.0
    for th in sample:
        flip = np.concatenate([-th[:NDIM], th[NDIM:]])
        _k1, _c1, sp1 = ks_wall_functionals(th, cls)
        _k2, _c2, sp2 = ks_wall_functionals(flip, cls)
        d_spread = max(d_spread, abs(sp1 - sp2)
                       / max(1.0, abs(sp1)))
        j1, _b1 = theta_matrices(th)
        j2, _b2 = theta_matrices(flip)
        e1 = np.linalg.eigvalsh(j1)
        e2 = np.linalg.eigvalsh(j2)
        pair1 = sorted([cls["L"] - float(e1[-1]),
                        float(e1[0]) + cls["L"]])
        pair2 = sorted([cls["L"] - float(e2[-1]),
                        float(e2[0]) + cls["L"]])
        d_radius = max(d_radius, max(abs(a - b) / max(1.0, abs(a))
                                     for a, b in zip(pair1, pair2)))
        s1, s2 = sigma_quotient(th), sigma_quotient(flip)
        if math.isfinite(s1) and math.isfinite(s2):
            d_sig_flip = max(d_sig_flip,
                             abs(s1 - s2) / max(1.0, abs(s1)))
    check("AC1 SPREAD is INVARIANT under the definiteness flip "
          "J -> -J on %d sample points: max rel %.2e <= %.0e -- it "
          "carries no orientation" % (len(sample), d_spread, 1e-9),
          d_spread <= 1e-9, kill="K2")
    check("AC2 the radius constraint PAIR is invariant under the "
          "same flip: max rel %.2e <= %.0e" % (d_radius, 1e-9),
          d_radius <= 1e-9, kill="K2")
    print("    DISCLOSED (amendment A8, smoke-1 finding): sigma is "
          "ALSO flip-invariant (max rel change %.2e), because both "
          "n and s = n - q change sign under M -> -M.  Flip "
          "invariance is therefore NECESSARY but NOT SUFFICIENT and "
          "is NOT used as the discriminating ward.  The decisive "
          "ward is MOMENT LOCALITY, below." % d_sig_flip)
    # AC3/AC4: MOMENT LOCALITY -- the decisive ward.  RADAU_K and
    # the moment box read only (a_1; b_2..b_K; a_2..a_K); the deep
    # tail coordinates are invisible to them and visible to sigma.
    tail = ([i for i in range(KDEG5, NDIM)]
            + [NDIM + i for i in range(KDEG5, NDIM - 1)])
    d_mom = 0.0
    d_rad = 0.0
    d_sig_tail = 0.0
    n_tail = 0
    for th in sample[:12]:
        th2 = np.asarray(th, float).copy()
        for i in tail:
            th2[i] = th[i] * 1.37 + 0.11
        m1 = moment_vector(th, KDEG5)
        m2 = moment_vector(th2, KDEG5)
        d_mom = max(d_mom, float(np.max(np.abs(m1 - m2)
                                        / np.maximum(1.0,
                                                     np.abs(m1)))))
        for kdeg in (KDEG, KDEG5):
            v1 = radau_from_entries(th, kdeg, cls["cb"])
            v2 = radau_from_entries(th2, kdeg, cls["cb"])
            if math.isfinite(v1) and math.isfinite(v2):
                d_rad = max(d_rad, abs(v1 - v2) / max(1.0, abs(v1)))
        s1, s2 = sigma_quotient(th), sigma_quotient(th2)
        if math.isfinite(s1) and math.isfinite(s2):
            n_tail += 1
            d_sig_tail = max(d_sig_tail,
                             abs(s1 - s2) / max(1.0, abs(s1)))
    check("AC3 MOMENT LOCALITY: perturbing the %d DEEP TAIL Jacobi "
          "coordinates %s leaves nu_0..nu_%d and RADAU_K (K = %d, "
          "%d) EXACTLY unchanged: max rel %.2e / %.2e <= %.0e"
          % (len(tail), ",".join(COORD[i] for i in tail),
             2 * KDEG5 - 2, KDEG, KDEG5, d_mom, d_rad, 1e-12),
          d_mom <= 1e-12 and d_rad <= 1e-12, kill="K2")
    check("AC4 CONTROL-MUST-FIRE the CIRCULAR sigma DOES see the "
          "same deep tail (max rel change %.3e on %d cells), "
          "because it reads the FULL co-block resolvent -- the ward "
          "has discriminating power" % (d_sig_tail, n_tail),
          d_sig_tail > 1e-6, kill="K4")
    # AC5/AC6: the co-block floor cannot see the pivot or coupling.
    d_floor = 0.0
    d_sig2 = 0.0
    for th in sample[:12]:
        th = np.asarray(th, float).copy()
        f1 = coblock_floor(th)
        s1 = sigma_quotient(th)
        th2 = th.copy()
        th2[0] = th[0] * 0.37 + 1.0
        th2[NDIM] = th[NDIM] * 2.9
        f2 = coblock_floor(th2)
        s2 = sigma_quotient(th2)
        d_floor = max(d_floor, abs(f1 - f2) / max(1.0, abs(f1)))
        if math.isfinite(s1) and math.isfinite(s2):
            d_sig2 = max(d_sig2, abs(s1 - s2) / max(1.0, abs(s1)))
    check("AC5 the CO-BLOCK PREMISE c = lambda_min(J_B) is "
          "INDEPENDENT of the two coordinates b_1, a_1 that carry "
          "the pivot and the coupling: max rel %.2e <= %.0e"
          % (d_floor, 1e-12), d_floor <= 1e-12, kill="K2")
    check("AC6 CONTROL-MUST-FIRE the CIRCULAR sigma DEPENDS on them "
          "(max rel change %.3e), confirming the separation is real"
          % d_sig2, d_sig2 > 1e-6, kill="K4")


# ============================== N: the membership census
def membership(rows, cls):
    section("N -- (c) THE MEMBERSHIP CENSUS: truth, F0 and the "
            "cited edge family against every constraint")
    slack_rows = []
    for r in rows:
        sl, names = class_slack_vector(r["theta"], cls)
        mom = moment_box_con(r["theta"], KDEG5, cls["mlo"],
                             cls["mhi"])
        r["slack_ks"] = float(np.min(sl))
        r["slack_mom"] = float(np.min(mom))
        r["slack_rad4"] = radau_self_con(r["theta"], KDEG,
                                         cls["t_r"])
        r["slack_rad5"] = radau_self_con(r["theta"], KDEG5,
                                         cls["t_r"])
        r["slack_radu"] = radau_con(r["theta"], KDEG, cls["cb"],
                                    cls["t_r"])
        r["slack_piv"] = pivot_con(r["theta"])
        slack_rows.append(sl)
    slack_rows = np.asarray(slack_rows, float)
    _sl, names = class_slack_vector(rows[0]["theta"], cls)
    per_min = slack_rows.min(axis=0)
    order = np.argsort(per_min)
    print("    tightest C_KS constraints across all cells:")
    for j in order[:6]:
        print("      %-16s %.6e" % (names[j], per_min[j]))
    lad = [r for r in rows if r["seg"] != "F0"]
    f0 = [r for r in rows if r["seg"] == "F0"]
    for tag, grp in (("ladder", lad), ("F0", f0)):
        if not grp:
            continue
        n_ks = sum(1 for r in grp if r["slack_ks"] >= -FEAS_TOL)
        n_pv = sum(1 for r in grp if r["slack_piv"] > 0.0)
        n_mo = sum(1 for r in grp if r["slack_mom"] >= -FEAS_TOL)
        n_r4 = sum(1 for r in grp if r["slack_rad4"] >= -FEAS_TOL)
        n_r5 = sum(1 for r in grp if r["slack_rad5"] >= -FEAS_TOL)
        n_ru = sum(1 for r in grp if r["slack_radu"] >= -FEAS_TOL)
        n_all = sum(1 for r in grp
                    if min(r["slack_ks"], r["slack_mom"],
                           r["slack_rad5"]) >= -FEAS_TOL
                    and r["slack_piv"] > 0.0)
        print("    %-7s cells %3d | C_KS %3d | n>0 %3d | MOM %3d | "
              "RAD4 %3d | RAD5 %3d | JOINT(K5) %3d | "
              "[class-uniform floor: RAD4 %3d]"
              % (tag, len(grp), n_ks, n_pv, n_mo, n_r4, n_r5,
                 n_all, n_ru))
    n_lad_in = sum(1 for r in lad
                   if min(r["slack_ks"], r["slack_mom"],
                          r["slack_rad4"]) >= -FEAS_TOL
                   and r["slack_piv"] > 0.0)
    check("N1 all %d ladder cells are INSIDE the joint Radau class "
          "at K = %d (%d in)" % (len(lad), KDEG, n_lad_in),
          n_lad_in == len(lad), kill="K2")
    if f0:
        n_f0_j = sum(1 for r in f0
                     if min(r["slack_mom"],
                            r["slack_rad5"]) >= -FEAS_TOL
                     and r["slack_piv"] > 0.0)
        n_f0_4 = sum(1 for r in f0
                     if min(r["slack_mom"],
                            r["slack_rad4"]) >= -FEAS_TOL
                     and r["slack_piv"] > 0.0)
        miss = [r for r in f0
                if min(r["slack_mom"],
                       r["slack_rad5"]) < -FEAS_TOL
                or r["slack_piv"] <= 0.0]
        det = "; ".join("kz %d h %.0f mom %.2e rad5 %.2e"
                        % (r["kz"], r["h"], r["slack_mom"],
                           r["slack_rad5"])
                        for r in miss[:4])
        check("N2 every OFF-LADDER F0 cell satisfies the SOURCE-ONLY "
              "JOINT relation at the depth amendment A1 declares for "
              "this family, K = %d (n > 0, MOM, RAD): %d/%d"
              % (KDEG5, n_f0_j, len(f0)),
              n_f0_j == len(f0), det, kill="K2")
        print("    A1 CONFIRMED BY MEASUREMENT: at the shallower "
              "depth K = %d only %d/%d F0 cells satisfy the same "
              "relation -- the sigma-max cell needs K = %d, exactly "
              "CCLXXVII's disclosed diagnostic; the two depths are "
              "therefore run as separate tiers throughout."
              % (KDEG, n_f0_4, len(f0), KDEG5))
        n_f0_ks = sum(1 for r in f0 if r["slack_ks"] >= -FEAS_TOL)
        print("    DISCLOSED, NOT A FAILURE: %d/%d F0 cells lie "
              "inside the KS ENTRY BOX C_KS, which was frozen from "
              "the DEPLOYED LADDER alone and therefore makes no "
              "claim about off-ladder cells; the tightest violated "
              "entry bound over the F0 cells is %.4e.  The joint "
              "relation above is box-free and holds regardless."
              % (n_f0_ks, len(f0),
                 min(r["slack_ks"] for r in f0)))
    n_ru_all = sum(1 for r in rows if r["slack_radu"] >= -FEAS_TOL)
    print("    THE DISCLOSED COST OF AMENDMENT A7: at the "
          "CLASS-UNIFORM floor c_class = %.6f the very same "
          "relation admits only %d/%d cells (CCLXV's 2.1609 ladder "
          "max at the widened global floor, restated); at the "
          "member's OWN certified co-block floor it admits %d/%d."
          % (cls["cb"], n_ru_all, len(rows),
             sum(1 for r in rows if r["slack_rad4"] >= -FEAS_TOL),
             len(rows)))
    print("    CITED, NOT REBUILT (amendment A5): the CCLXXIII edge "
          "family, %d wall-legal steps beyond the registration cut, "
          "edge sigma max %.6f -- compatible with t_R = %.4f "
          "(margin %+.4f).  Their MOM / RAD membership is NOT "
          "established here; the edge remains the open flank."
          % (EDGE_STEPS_CITED, EDGE_SIGMA_CITED, T_R_F,
             T_R_F - EDGE_SIGMA_CITED))


# ============================== O: the optimization machinery
def make_objective(cls, fdata, extras):
    def neg_f(theta):
        v = tr_r_of_theta(theta, fdata)
        return -v if math.isfinite(v) else 1e12

    def slacks(theta):
        sl, _names = class_slack_vector(theta, cls)
        add = []
        for fun in extras:
            val = fun(theta)
            if np.isscalar(val):
                add.append(float(val))
            else:
                add.extend([float(v) for v in np.asarray(val, float)])
        if add:
            sl = np.concatenate([sl, np.asarray(add, float)])
        return sl

    def penalized(theta):
        v = tr_r_of_theta(theta, fdata)
        if not math.isfinite(v):
            return 1e12
        sl = slacks(theta)
        viol = float(np.sum(np.clip(-sl, 0.0, None)))
        return -v + PEN_W * viol * viol
    return neg_f, slacks, penalized


def opt_seeds(rows, lo, hi, n_ms):
    """The declared multi-start seed set: truth cells, plus TWO
    adversarial corner families seeded in OPPOSITE directions so the
    search is not biased toward the closure answer -- the pivot at
    its box floor with the coupling a_1 at its CEILING (the
    sigma-blow-up corner, which RAD is designed to cut) and at its
    FLOOR (the SCALE corner, where n and a_1 shrink together, so
    sigma and the scale-invariant ratio RADAU_K/n stay put while
    lambda_1(J) -> 0 and R(lambda_1) -> 1), then uniform fill."""
    rng = np.random.default_rng(OPT_SEED)
    thetas = [r["theta"] for r in rows]
    seeds = []
    idx = np.linspace(0, len(thetas) - 1,
                      max(2, n_ms // 3)).astype(int)
    for i in sorted(set(idx.tolist())):
        seeds.append(np.clip(thetas[i], lo, hi))
    for i in sorted(set(idx.tolist())):
        for frac in (1.0, 0.0):
            cn = np.clip(thetas[i], lo, hi).copy()
            cn[0] = lo[0] + 1e-9 * (hi[0] - lo[0])
            cn[NDIM] = lo[NDIM] + frac * (hi[NDIM] - lo[NDIM]) \
                + (1e-9 if frac == 0.0 else -1e-9) \
                * (hi[NDIM] - lo[NDIM])
            seeds.append(cn)
    while len(seeds) < n_ms:
        seeds.append(rng.uniform(lo, hi))
    return seeds


def maximize(rows, cls, fdata, label, extras, box, n_ms, de_it):
    lo = cls["lo"] if box is None else box[0]
    hi = cls["hi"] if box is None else box[1]
    bounds = list(zip(lo, hi))
    neg_f, slacks, penalized = make_objective(cls, fdata, extras)
    seeds = opt_seeds(rows, lo, hi, n_ms)
    cons = [dict(type="ineq", fun=slacks)]
    best_v, best_t = -float("inf"), None
    n_conv = 0
    for sd in seeds[:n_ms]:
        try:
            res = optimize.minimize(neg_f, sd, method="SLSQP",
                                    bounds=bounds, constraints=cons,
                                    options=dict(maxiter=SLSQP_MAXIT,
                                                 ftol=1e-12))
        except (ValueError, OverflowError):
            continue
        th = np.clip(res.x, lo, hi)
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            n_conv += 1
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    de = optimize.differential_evolution(
        penalized, bounds=bounds, seed=OPT_SEED, maxiter=de_it,
        popsize=DE_POP, polish=False, tol=1e-10, init="sobol")
    th_de = np.clip(de.x, lo, hi)
    try:
        res = optimize.minimize(neg_f, th_de, method="SLSQP",
                                bounds=bounds, constraints=cons,
                                options=dict(maxiter=SLSQP_MAXIT,
                                             ftol=1e-12))
        th_pol = np.clip(res.x, lo, hi)
    except (ValueError, OverflowError):
        th_pol = th_de
    for th in (th_de, th_pol):
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    truth_best = -float("inf")
    truth_th = None
    truth_seg = "-"
    lad_best = -float("inf")
    for r in rows:
        if float(np.min(slacks(r["theta"]))) >= -FEAS_TOL:
            if r["seg"] != "F0":
                lad_best = max(lad_best, r["trace_r"])
            if r["trace_r"] > truth_best:
                truth_best = r["trace_r"]
                truth_th = r["theta"]
                truth_seg = r["seg"]
    sup = max(best_v, truth_best)
    src = "optimizer" if best_v >= truth_best else "truth-in-class"
    print("    %-46s sup tr R = %.6f (%s; optimizer %.6f on %d/%d "
          "feasible starts, truth floor %.6f from seg %s, ladder-"
          "only floor %.6f) [%.1f s]"
          % (label, sup, src, best_v, n_conv, n_ms,
             truth_best if math.isfinite(truth_best) else float("nan"),
             truth_seg,
             lad_best if math.isfinite(lad_best) else float("nan"),
             time.time() - T0), flush=True)
    theta_best = best_t if best_v >= truth_best else truth_th
    return dict(label=label, sup=sup, opt=best_v, truth=truth_best,
                theta=theta_best, theta_opt=best_t, src=src,
                slacks=slacks)


def lam_min_of_theta(theta):
    jm, _jb = theta_matrices(theta)
    try:
        return float(np.linalg.eigvalsh(jm)[0])
    except np.linalg.LinAlgError:
        return float("nan")


def min_lambda(rows, cls, fdata, label, extras, box, n_ms, de_it):
    """THE DEFINITENESS QUESTION at class level: inf lambda_1(J) over
    the class.  This is CCLXXVII's per-step conclusion 'M > 0' lifted
    to the class, and it is STRICTLY WEAKER than the reserve question
    sup tr R < 1 that the tier ladder asks (amendment A6).  The value
    is a NUMERIC global, i.e. an UPPER bound of the true infimum, so
    inf <= 0 is a CERTAIN refutation and inf > 0 is numeric."""
    lo = cls["lo"] if box is None else box[0]
    hi = cls["hi"] if box is None else box[1]
    bounds = list(zip(lo, hi))
    _neg, slacks, _pen = make_objective(cls, fdata, extras)

    def obj(theta):
        v = lam_min_of_theta(theta)
        return v if math.isfinite(v) else 1e12

    def pen(theta):
        v = lam_min_of_theta(theta)
        if not math.isfinite(v):
            return 1e12
        sl = slacks(theta)
        viol = float(np.sum(np.clip(-sl, 0.0, None)))
        return v + PEN_W * viol * viol

    seeds = opt_seeds(rows, lo, hi, n_ms)
    cons = [dict(type="ineq", fun=slacks)]
    best_v, best_t = float("inf"), None
    n_conv = 0
    for sd in seeds[:n_ms]:
        try:
            res = optimize.minimize(obj, sd, method="SLSQP",
                                    bounds=bounds, constraints=cons,
                                    options=dict(maxiter=SLSQP_MAXIT,
                                                 ftol=1e-14))
        except (ValueError, OverflowError):
            continue
        th = np.clip(res.x, lo, hi)
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            n_conv += 1
            v = lam_min_of_theta(th)
            if math.isfinite(v) and v < best_v:
                best_v, best_t = v, th
    de = optimize.differential_evolution(
        pen, bounds=bounds, seed=OPT_SEED, maxiter=de_it,
        popsize=DE_POP, polish=False, tol=1e-10, init="sobol")
    th_de = np.clip(de.x, lo, hi)
    try:
        res = optimize.minimize(obj, th_de, method="SLSQP",
                                bounds=bounds, constraints=cons,
                                options=dict(maxiter=SLSQP_MAXIT,
                                             ftol=1e-14))
        th_pol = np.clip(res.x, lo, hi)
    except (ValueError, OverflowError):
        th_pol = th_de
    for th in (th_de, th_pol):
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            v = lam_min_of_theta(th)
            if math.isfinite(v) and v < best_v:
                best_v, best_t = v, th
    truth_ceil = float("inf")
    truth_th = None
    for r in rows:
        if float(np.min(slacks(r["theta"]))) >= -FEAS_TOL:
            v = float(np.min(r["lam_j"]))
            if v < truth_ceil:
                truth_ceil, truth_th = v, r["theta"]
    inf = min(best_v, truth_ceil)
    src = "optimizer" if best_v <= truth_ceil else "truth-in-class"
    print("    %-46s inf lambda_1(J) = %.6e (%s; optimizer %.6e on "
          "%d/%d feasible starts, truth-in-class ceiling %.6e) "
          "[%.1f s]"
          % (label, inf, src, best_v, n_conv, n_ms, truth_ceil,
             time.time() - T0), flush=True)
    return dict(label=label, inf=inf,
                theta=best_t if best_v <= truth_ceil else truth_th,
                truth=truth_ceil, src=src, sup=inf, slacks=slacks)


def anatomy(res, cls, fdata, kdeg):
    th = res["theta"]
    if th is None:
        print("      (no feasible incumbent)")
        return
    sl, names = class_slack_vector(th, cls)
    order = np.argsort(sl)
    jm, _jb = theta_matrices(th)
    ev = np.linalg.eigvalsh(jm)
    flo = coblock_floor(th)
    rad = radau_from_entries(th, kdeg, flo)
    print("      anatomy [%s]: n = %.6g, a_1 = %.6g, sigma = %.6f, "
          "c = lambda_min(J_B) = %.6g, RADAU_%d/n = %.6f, "
          "lambda_min(J) = %.6g, tr R = %.6f"
          % (res["src"], float(th[0]), float(th[NDIM]),
             sigma_quotient(th), flo, kdeg,
             rad / float(th[0]) if float(th[0]) > 0 else float("nan"),
             float(ev[0]), tr_r_of_theta(th, fdata)))
    print("      active constraints: %s"
          % ", ".join("%s %.2e" % (names[j], sl[j])
                      for j in order[:4]))


# =================== E: (b) THE EXTREMAL TEST on the tier ladder
def extremal(rows, cls, fdata):
    section("E -- (b) THE EXTREMAL TEST: sup tr R over the tier "
            "ladder.  THE QUESTION: does the JOINT source-only "
            "relation close what the SEPARATE envelopes cannot?")
    n_ms = 6 if SMOKE else MAP_MS
    de_it = 20 if SMOKE else MAP_DE
    lo_p = np.asarray(cls["lo"], float).copy()
    hi_p = np.asarray(cls["hi"], float).copy()
    lo_p[0] = 0.0
    pbox = (lo_p, hi_p)

    def mom_extra(theta):
        return moment_box_con(theta, KDEG5, cls["mlo"], cls["mhi"])

    def rad4_extra(theta):
        return radau_self_con(theta, KDEG, cls["t_r"])

    def rad5_extra(theta):
        return radau_self_con(theta, KDEG5, cls["t_r"])

    def sig_extra(theta):
        s = sigma_quotient(theta)
        if not math.isfinite(s):
            return -1.0
        return (cls["t_r"] - s) / max(abs(cls["t_r"]), 1e-6)

    out = {}
    out["E0"] = maximize(rows, cls, fdata,
                         "E0  C_KS alone (CCLXI/CCLXV anchor)",
                         [], None, n_ms, de_it)
    anatomy(out["E0"], cls, fdata, KDEG)
    check("E0 REPRO the uncapped CCLXI leak is reproduced: sup tr R "
          "= %.4f >= %.1f (CCLXV anchor %.4f, ratio %.3f)"
          % (out["E0"]["sup"], SUP_NOCAP_BAR, SUP_NOCAP_REF,
             out["E0"]["sup"] / SUP_NOCAP_REF),
          SMOKE or out["E0"]["sup"] >= SUP_NOCAP_BAR, kill="K3")
    out["E1"] = maximize(rows, cls, fdata,
                         "E1  + n > 0 (the entry sheet)",
                         [], pbox, n_ms, de_it)
    anatomy(out["E1"], cls, fdata, KDEG)
    out["E2"] = maximize(rows, cls, fdata,
                         "E2  + MOM box (SEPARATE ENVELOPES)",
                         [mom_extra], pbox, n_ms, de_it)
    anatomy(out["E2"], cls, fdata, KDEG)
    out["E3"] = maximize(rows, cls, fdata,
                         "E3  + RAD at K = 4 (THE JOINT TIER)",
                         [mom_extra, rad4_extra], pbox,
                         6 if SMOKE else CONF_MS,
                         20 if SMOKE else CONF_DE)
    anatomy(out["E3"], cls, fdata, KDEG)
    out["E4"] = maximize(rows, cls, fdata,
                         "E4  + RAD at K = 5 (the CCLXXIX depth)",
                         [mom_extra, rad5_extra], pbox,
                         6 if SMOKE else CONF_MS,
                         20 if SMOKE else CONF_DE)
    anatomy(out["E4"], cls, fdata, KDEG5)
    out["E5"] = maximize(rows, cls, fdata,
                         "E5  + the CIRCULAR sigma-cap (REFERENCE)",
                         [sig_extra], pbox, n_ms, de_it)
    anatomy(out["E5"], cls, fdata, KDEG)
    print("\n    TIER LADDER (sup tr R; < 1 = CLOSES, >= 1 = LEAKS; "
          "every value is a NUMERIC global, i.e. a LOWER bound of "
          "the true sup, so a LEAK is certain and a CLOSURE is "
          "numeric):")
    for key in ("E0", "E1", "E2", "E3", "E4", "E5"):
        res = out[key]
        print("      %-46s %.6f   %s"
              % (res["label"], res["sup"],
                 "CLOSES" if res["sup"] < 1.0 else "LEAKS"))
    check("E1 SEARCH POWER: the optimizer itself (truth floor "
          "excluded) reaches tr R = %.4f >= 1 on the tier that has "
          "no joint constraint, so any closure below is not a "
          "search failure" % max(out["E0"]["opt"], out["E1"]["opt"]),
          max(out["E0"]["opt"], out["E1"]["opt"]) >= 1.0, kill="K4")
    # the tier NESTING is a theorem, not an accident: the Gauss-Radau
    # upper bounds decrease in K, so RAD at K = 4 IMPLIES RAD at
    # K = 5 and the K = 5 tier is the LARGER class.
    check("E2 TIER NESTING ward: the K = 4 joint tier is contained in "
          "the K = 5 one (Radau bounds decrease in K), so its sup "
          "must not exceed it: %.6f <= %.6f"
          % (out["E3"]["sup"], out["E4"]["sup"]),
          out["E3"]["sup"] <= out["E4"]["sup"] + 1e-6, kill="K2")
    joint_closes = out["E3"]["sup"] < 1.0 and out["E4"]["sup"] < 1.0
    env_leaks = out["E2"]["sup"] >= 1.0
    print("    THE HEADLINE: the SEPARATE-ENVELOPE tier %s (%.6f); "
          "the JOINT tier at K = 4 %s (%.6f, margin %+.6f) and at "
          "K = 5 %s (%.6f, margin %+.6f).\n    %s"
          % ("LEAKS" if env_leaks else "closes", out["E2"]["sup"],
             "CLOSES" if out["E3"]["sup"] < 1.0 else "LEAKS",
             out["E3"]["sup"], 1.0 - out["E3"]["sup"],
             "CLOSES" if out["E4"]["sup"] < 1.0 else "LEAKS",
             out["E4"]["sup"], 1.0 - out["E4"]["sup"],
             "The joint relation is the decisive object: it removes "
             "%.1f%% of the separate-envelope excess."
             % (100.0 * (out["E2"]["sup"] - max(out["E3"]["sup"],
                                                out["E4"]["sup"]))
                / max(out["E2"]["sup"] - 1.0, 1e-12))
             if env_leaks and joint_closes else
             "The joint relation removes %.1f%% of the "
             "separate-envelope excess over 1 but does NOT close it "
             "at every declared depth."
             % (100.0 * (out["E2"]["sup"] - max(out["E3"]["sup"],
                                                out["E4"]["sup"]))
                / max(out["E2"]["sup"] - 1.0, 1e-12))
             if env_leaks else
             "The separate envelopes already close, so the joint "
             "relation is not the decisive object on this class."))
    # THE DEFINITENESS QUESTION, strictly weaker than the reserve
    # question the tiers ask (A6): does the joint class force M > 0?
    out["D3"] = min_lambda(rows, cls, fdata,
                           "D3  inf lambda_1(J) on the K = 4 tier",
                           [mom_extra, rad4_extra], pbox,
                           6 if SMOKE else CONF_MS,
                           20 if SMOKE else CONF_DE)
    out["D4"] = min_lambda(rows, cls, fdata,
                           "D4  inf lambda_1(J) on the K = 5 tier",
                           [mom_extra, rad5_extra], pbox,
                           6 if SMOKE else CONF_MS,
                           20 if SMOKE else CONF_DE)
    out["D2"] = min_lambda(rows, cls, fdata,
                           "D2  inf lambda_1(J) WITHOUT the joint "
                           "relation (control)",
                           [mom_extra], pbox,
                           6 if SMOKE else CONF_MS,
                           20 if SMOKE else CONF_DE)
    def_ok = out["D3"]["inf"] > 0.0 and out["D4"]["inf"] > 0.0
    check("E3 CONTROL-MUST-FIRE the separate-envelope tier does NOT "
          "force definiteness: inf lambda_1(J) = %.6e <= 0"
          % out["D2"]["inf"], out["D2"]["inf"] <= 0.0, kill="K4")
    check("E4 THE DEFINITENESS VERDICT: the JOINT class forces "
          "M > 0 at BOTH declared depths (inf lambda_1 = %.6e at "
          "K = 4, %.6e at K = 5) -- CCLXXVII's per-step conclusion "
          "lifted to the class"
          % (out["D3"]["inf"], out["D4"]["inf"]), def_ok)
    print("    READ THIS WITH AMENDMENT A6: definiteness (inf "
          "lambda_1 > 0) is STRICTLY WEAKER than the reserve "
          "(sup tr R < 1).  The joint class %s definiteness and %s "
          "the reserve at K = 5, so a LEAK above is NOT a "
          "contradiction with the per-step chain."
          % ("SETTLES" if def_ok else "does NOT settle",
             "settles" if out["E4"]["sup"] < 1.0 else "does NOT"))
    out["joint_closes"] = joint_closes
    out["env_leaks"] = env_leaks
    out["def_ok"] = def_ok
    return out


# ================= A: (d) THE JOINT SUM RULE SHAPE
def r_envelope_builder(fdata, cls):
    """Rdec(x) = sup_{[x, L]} R for the FROZEN filter, on a declared
    log grid (a numeric envelope of a frozen function, no fitting;
    the lookup is conservative -- it always includes one grid point
    below x)."""
    grid = np.geomspace(ENV_LO, cls["L"], ENV_GRID)
    vals = np.asarray([zol.scalar_r(fdata, float(x)) for x in grid],
                      float)
    suffix = np.maximum.accumulate(vals[::-1])[::-1]

    def rdec(x):
        if not math.isfinite(x):
            return 1.0
        if x <= ENV_LO:
            return 1.0
        if x >= cls["L"]:
            return float(vals[-1])
        j = int(np.searchsorted(grid, x)) - 1
        j = max(j, 0)
        return float(suffix[j])
    return rdec, grid, vals


def sum_rule(rows, cls, fdata, tiers):
    section("A -- (d) THE JOINT SUM RULE: the composition "
            "separator o interlacing o Schur o Radau, every rung "
            "typed and warded")
    import sympy as sp
    nn, cc, rr, lam = sp.symbols("n c rho lam", positive=True)
    # R3 ward: the quadratic (n - lam)(c - lam) >= rho c n has the
    # closed-form smaller root Lambda.
    quad = sp.expand((nn - lam) * (cc - lam) - rr * cc * nn)
    lam_sol = sp.solve(sp.Eq(quad, 0), lam)
    closed = ((nn + cc) - sp.sqrt((nn - cc) ** 2
                                  + 4 * nn * cc * rr)) / 2
    w1 = any(sp.simplify(s - closed) == 0 for s in lam_sol)
    check("A1 EXACT (sympy) the smaller root of "
          "(n - lam)(c - lam) = rho c n is Lambda(n, c, rho) = "
          "((n + c) - sqrt((n - c)^2 + 4 n c rho)) / 2", w1,
          kill="K2")
    w2 = all(closed.subs({rr: 0, nn: sp.Rational(a),
                          cc: sp.Rational(b)})
             == min(sp.Rational(a), sp.Rational(b))
             for a, b in ((1, 2), (3, 1), (5, 5), (7, 4)))
    check("A2 EXACT sanity: rho -> 0 gives Lambda -> min(n, c) (the "
          "decoupled wall), on 4 exact rational substitutions",
          bool(w2), kill="K2")
    xx = sp.symbols("x", positive=True)
    # R3 ward: (B - lam)^{-1} <= (c/(c-lam)) B^{-1} eigenvalue-wise.
    ineq = sp.simplify(cc / ((cc - lam) * xx) - 1 / (xx - lam))
    ineq_t = sp.simplify(ineq - lam * (xx - cc)
                         / (xx * (cc - lam) * (xx - lam)))
    check("A3 EXACT the resolvent comparison c/((c - lam) x) - "
          "1/(x - lam) = lam (x - c) / (x (c - lam)(x - lam)) >= 0 "
          "for x >= c > lam >= 0 -- the rung that turns q into the "
          "shifted bound", ineq_t == 0, kill="K2")
    rdec, grid, vals = r_envelope_builder(fdata, cls)
    rng = np.random.default_rng(OPT_SEED)
    tests = np.exp(rng.uniform(math.log(ENV_LO * 10.0),
                               math.log(cls["L"]), ENV_TEST))
    d_env = float("inf")
    for x in tests:
        d_env = min(d_env, rdec(float(x))
                    - zol.scalar_r(fdata, float(x)))
    check("A4 the declared envelope Rdec dominates R at %d random "
          "test points (worst defect %.2e >= 0)" % (ENV_TEST, d_env),
          d_env >= -1e-12, kill="K2")
    non_inc = bool(np.all(np.diff(
        np.maximum.accumulate(vals[::-1])[::-1]) <= 1e-15))
    check("A5 Rdec is NON-INCREASING by construction (suffix "
          "maximum of the frozen filter on a %d-point log grid)"
          % ENV_GRID, non_inc, kill="K2")
    delta_z = float(fdata["delta"])
    rdec_class = rdec(cls["cb"])
    print("    separator numbers: certified bulk delta on [c_B, L] "
          "= %.6e (c_B = %.4f); Rdec at the WIDENED class floor "
          "c_class = %.4f is %.6f -- amendment A4's structural cost "
          "is the factor %.1f" % (delta_z, CB_F, cls["cb"],
                                  rdec_class, rdec_class / delta_z))
    n_int = 0
    n_valid = 0
    n_ord = 0
    n_fin = 0
    for r in rows:
        c_cert = r["c_cert"]
        piv = float(r["theta"][0])
        cand = [r["bound%s" % t] for t in ("4", "5")
                if math.isfinite(r["bound%s" % t])]
        rho = min(cand) if cand else float("nan")
        r["rho_best"] = rho
        lam_j = r["lam_j"]
        r["lam_1"] = float(lam_j[0])
        r["n_below"] = int(np.sum(lam_j < c_cert - 1e-12))
        if r["n_below"] <= 1:
            n_int += 1
        r["good_sum"] = math.fsum(zol.scalar_r(fdata, float(v))
                                  for v in lam_j[1:])
        r["r_bad"] = zol.scalar_r(fdata, float(lam_j[0]))
        r["lam_closed"] = lambda_closed(piv, c_cert, rho)
        r["lam_shift"] = shift_radau_floor(r["theta"], KDEG, c_cert)
        cand_l = [v for v in (r["lam_closed"], r["lam_shift"])
                  if math.isfinite(v)]
        r["lam_bad"] = max(cand_l) if cand_l else float("nan")
        r["good_crude"] = (NDIM - 1) * rdec(c_cert)
        r["good_sharp"] = math.fsum(rdec(float(v))
                                    for v in r["lam_jb"])
        r["F_crude"] = (1.0 - rdec(r["lam_closed"])
                        - r["good_crude"])
        r["F_best"] = (1.0 - rdec(r["lam_bad"]) - r["good_sharp"])
        if r["F_best"] <= r["reserve"] + 1e-9:
            n_valid += 1
        if math.isfinite(r["lam_closed"]) \
                and math.isfinite(r["lam_shift"]):
            n_fin += 1
            if (r["lam_closed"] <= r["lam_1"] + 1e-9
                    and r["lam_shift"] <= r["lam_1"] + 1e-9):
                n_ord += 1
    check("A6 R1 INTERLACING ward: at most ONE eigenvalue of J lies "
          "below the certified co-block floor on %d/%d cells"
          % (n_int, len(rows)), n_int == len(rows), kill="K2")
    check("A7 R3 VALIDITY ward (amendment A9): BOTH source-only "
          "lower bounds -- the closed-form Lambda and the "
          "SHIFT-RADAU floor -- are <= the truth lambda_1(J) on "
          "%d/%d cells (both finite on %d/%d); no ordering between "
          "them is claimed" % (n_ord, n_fin, n_fin, len(rows)),
          n_ord == n_fin and n_fin == len(rows), kill="K2")
    n_sh = sum(1 for r in rows
               if math.isfinite(r["lam_shift"])
               and math.isfinite(r["lam_closed"])
               and r["lam_shift"] > r["lam_closed"])
    print("    which bound is sharper: SHIFT-RADAU on %d cells, the "
          "closed form on %d -- the chain consumes the max"
          % (n_sh, n_fin - n_sh))
    check("A8 CHAIN VALIDITY ward: F never exceeds the truth "
          "reserve 1 - tr R on %d/%d cells" % (n_valid, len(rows)),
          n_valid == len(rows), kill="K2")
    n_pos_c = sum(1 for r in rows if r["F_crude"] > 0.0)
    n_pos_b = sum(1 for r in rows if r["F_best"] > 0.0)
    print("    per-cell F census (%d cells): F_crude > 0 on %d, "
          "F_best > 0 on %d" % (len(rows), n_pos_c, n_pos_b))
    print("    lambda_1 truth  min/med/max  %s" % e3(
        [r["lam_1"] for r in rows]))
    print("    Lambda closed   min/med/max  %s" % e3(
        [r["lam_closed"] for r in rows]))
    print("    lambda shift-K  min/med/max  %s" % e3(
        [r["lam_shift"] for r in rows]))
    print("    lambda_bad_lo   min/med/max  %s" % e3(
        [r["lam_bad"] for r in rows]))
    print("    F_best          min/med/max  %s" % e3(
        [r["F_best"] for r in rows]))
    print("    truth reserve   min/med/max  %s" % e3(
        [r["reserve"] for r in rows]))
    # ---- the measured seat: replace each bound by its truth value
    loss_bad = [rdec(r["lam_bad"]) - r["r_bad"] for r in rows]
    loss_good = [r["good_sharp"] - r["good_sum"] for r in rows]
    loss_good_c = [r["good_crude"] - r["good_sum"] for r in rows]
    print("    RUNG LOSSES (bound minus truth, min/med/max):")
    print("      R3 bad mode   Rdec(lambda_bad_lo) - R(lambda_1)   %s"
          % e3(loss_bad))
    print("      R2 good block sum_j Rdec(lam_j(J_B)) - Sum_good   %s"
          % e3(loss_good))
    print("      R2 crude      7 Rdec(c_cert) - Sum_good          %s"
          % e3(loss_good_c))
    med_bad = float(np.median(loss_bad))
    med_good = float(np.median(loss_good))
    seat = ("R2 good block" if med_good >= med_bad
            else "R3 bad mode")
    print("    THE MEASURED SEAT: %s (median loss %.4f vs %.4f)"
          % (seat, max(med_good, med_bad), min(med_good, med_bad)))
    # ---- the class-uniform form
    piv_lo = cls["piv_lo"]
    lam_cls = lambda_closed(piv_lo, cls["cb"], cls["t_r"])
    good_cls = math.fsum(rdec(float(v)) for v in cls["jb_floor"])
    f_class = 1.0 - rdec(lam_cls) - good_cls
    u_class = rdec(lam_cls) + good_cls
    lam_msr = lambda_closed(cls["piv_lo_meas"], cls["cb"],
                            cls["t_r"])
    print("""
    THE CLASS-UNIFORM FORM (every ingredient a frozen class
    constant, no cell data):
      Lambda(n_lo = %.6e, c_class = %.6f, t_R = %.4f) = %.6e
      Rdec(Lambda)                                       = %.6f
      sum_j Rdec(f_j) over the co-block floors           = %.6f
      =>  sup_class tr R <= %.6f   and   F_class = %.6f
      (n_lo is the CLASS-IMPLIED pivot floor nu_0_lo/(L t_R); with
       the MEASURED truth pivot floor %.6e -- an EXTRA premise, not
       a class constraint -- one would get Lambda = %.6e and
       Rdec(Lambda) = %.6f, i.e. the same verdict)"""
          % (piv_lo, cls["cb"], cls["t_r"], lam_cls, rdec(lam_cls),
             good_cls, u_class, f_class, cls["piv_lo_meas"], lam_msr,
             rdec(lam_msr)))
    if tiers is not None:
        print("      (the NUMERIC sup of the joint tier E3 was "
              "%.6f, so the analytic bound is %s the numeric one "
              "by %.4f)"
              % (tiers["E3"]["sup"],
                 "above" if u_class >= tiers["E3"]["sup"]
                 else "BELOW", abs(u_class - tiers["E3"]["sup"])))
    if f_class > 0.0:
        sub = ("SUMRULE-EXPLICIT(delta = %.6f, class-uniform)"
               % f_class)
    elif n_pos_b > 0:
        sub = ("SUMRULE-PERCELL(%d/%d cells with F_best > 0; seat "
               "%s)" % (n_pos_b, len(rows), seat))
    else:
        ratio = (float(np.median([r["good_sharp"] for r in rows]))
                 / max(float(np.median([r["good_sum"] for r in rows])),
                       1e-300))
        sub = ("SUMRULE-SEAT(%s, median loss factor %.1f)"
               % (seat, ratio))
    print("\n    SUM-RULE SUB-VERDICT: %s" % sub)
    print("""    WHAT IS A THEOREM AND WHAT IS FROZEN, rung by rung:
      R1 Cauchy interlacing              THEOREM (E7)
      R2 R >= 0 on R, R <= delta on      CCXXV CERTIFIED (E8),
         [c_B, L]                        re-consumed
         Rdec on [x, L]                  DECLARED NUMERIC ENVELOPE
                                         of a FROZEN function
                                         (%d-point log grid, warded
                                         at %d random points)
      R3 resolvent comparison + secular  THEOREM, derived and
         monotonicity                    warded symbolically here
         q <= RADAU_K(nu; c)             E3, hypothesis DISCHARGED
                                         by the certified floor,
                                         remainder sign warded per
                                         cell (C3)
      R4 composition                     arithmetic
    THE ALL-h RESIDUE, stated plainly: everything above is a finite
    statement about the deployed cells and the frozen class.  What
    an all-h form would still need is (i) truth's membership in the
    MOM box and the floor class for every h -- the measured laws are
    flat here and CCLXXIII established that the deployed surface
    family beyond the registration cut is FINITE (58 zones, then
    nothing), and (ii) a class-level co-block geometry premise: the
    class-uniform form above is only as good as the floors f_j, and
    those are measured, not derived.  NO all-h claim is made."""
          % (ENV_GRID, ENV_TEST))
    return sub, seat, f_class


def shift_radau_floor(theta, kdeg, floor_c):
    """SHIFT-RADAU: the largest lam in [0, c) with
    n - lam - RADAU_K(nu(lam); c - lam) >= 0.  Source-only: the
    shifted measure's Jacobi coefficients are alpha - lam (E4), so
    the same functional applies with the shifted floor."""
    if not math.isfinite(floor_c) or floor_c <= 0.0:
        return float("nan")
    jmat, _blk = theta_matrices(theta)
    lan = lanczos_pair(jmat, kdeg)
    if lan is None:
        return float("nan")
    alp, bet, mass = lan
    piv = float(theta[0])

    def phi(lam):
        val, _j = radau_upper(alp - lam, bet, floor_c - lam, mass)
        if not math.isfinite(val) or val < 0.0:
            return -1.0
        return piv - lam - val

    if phi(0.0) < 0.0:
        return float("nan")
    lo, hi = 0.0, floor_c * (1.0 - 1e-12)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if phi(mid) >= 0.0:
            lo = mid
        else:
            hi = mid
    return lo


# ================================================ X: the controls
def controls(rows, cls, fdata, tiers):
    section("X -- controls-must-fire: falsifying worlds and the "
            "exclusion census")
    worlds = []
    base = [r for r in rows if r["seg"] != "F0"][:3] \
        + [r for r in rows if r["seg"] == "F0"][:1]
    for r in base:
        th = np.asarray(r["theta"], float)
        w1 = th.copy()
        w1[NDIM] = th[NDIM] * CTRL_COUPLE
        worlds.append(("coupling x%.0f" % CTRL_COUPLE,
                       r["kz"], w1))
        w2 = th.copy()
        w2[0] = th[0] * CTRL_PIVOT
        worlds.append(("pivot x%.2f" % CTRL_PIVOT, r["kz"], w2))
        w3 = th.copy()
        w3[0] = -abs(th[0])
        worlds.append(("pivot sign flipped", r["kz"], w3))
    n_fire = 0
    n_indef = 0
    n_inside_bad = 0
    print("    world                      kz    sigma     tr R    "
          "excluded by")
    for tag, kz, th in worlds:
        sig = sigma_quotient(th)
        trr = tr_r_of_theta(th, fdata)
        jw, _bw = theta_matrices(th)
        lam_w = float(np.linalg.eigvalsh(jw)[0])
        sl, names = class_slack_vector(th, cls)
        reasons = [names[j] for j in np.argsort(sl)[:2]
                   if sl[j] < -FEAS_TOL]
        if pivot_con(th) <= 0.0:
            reasons.append("n>0")
        mom = moment_box_con(th, KDEG5, cls["mlo"], cls["mhi"])
        if float(np.min(mom)) < -FEAS_TOL:
            reasons.append("MOM")
        rad = radau_self_con(th, KDEG, cls["t_r"])
        if rad < -FEAS_TOL:
            reasons.append("RAD")
        inside = not reasons
        indefinite = lam_w <= 0.0
        if indefinite:
            n_indef += 1
            if reasons:
                n_fire += 1
        if inside and trr >= 1.0:
            n_inside_bad += 1
        print("    %-26s %-5d %8.4f %8.4f  %s"
              % (tag, kz, sig if math.isfinite(sig) else float("nan"),
                 trr, ",".join(reasons) if reasons
                 else "*** NONE: INSIDE ***"))
    check("X1 every INDEFINITE falsifying world (lambda_min(J) <= 0) "
          "is excluded by at least one constraint: %d/%d fired"
          % (n_fire, n_indef), n_indef >= 1 and n_fire == n_indef,
          kill="K4")
    check("X2 NO falsifying world is inside the joint class WITH "
          "tr R >= 1 (%d such worlds)" % n_inside_bad,
          n_inside_bad == 0, kill="K4")
    # the RAD constraint must be the one doing the work on the
    # pivot-shrink world: check it fires where MOM does not.
    n_rad_only = 0
    for _tag, _kz, th in worlds:
        mom = float(np.min(moment_box_con(th, KDEG5, cls["mlo"],
                                          cls["mhi"])))
        rad = radau_self_con(th, KDEG, cls["t_r"])
        if mom >= -FEAS_TOL and rad < -FEAS_TOL:
            n_rad_only += 1
    check("X3 the JOINT relation excludes worlds the SEPARATE "
          "moment envelopes admit: %d such worlds" % n_rad_only,
          n_rad_only >= 1, kill="K4")
    if tiers is not None:
        check("X4 the CIRCULAR reference tier E5 is not stronger "
              "than the source-only joint tier E3 (sigma-cap sup "
              "%.4f vs Radau sup %.4f) -- the source-only object "
              "loses nothing here"
              % (tiers["E5"]["sup"], tiers["E3"]["sup"]),
              tiers["E3"]["sup"] <= tiers["E5"]["sup"] + 1e-6
              or tiers["E3"]["sup"] < 1.0)


# =========================================== S: the screens
def ch_surface_map(rows):
    """CCXVII c_h on matched surface terminators (CCLIII verbatim,
    labelled screen currency only)."""
    out = {}
    for kz in sorted({r["kz"] for r in rows
                      if r["seg"] in ("surf", "F0")}):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        import scipy.linalg as sla
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        out[int(kz)] = 1.0 - top
    return out


def screens(rows, cls):
    section("S -- relocation screens (CCXLVII bars verbatim): are "
            "the class margin and F tau or c_h in disguise?")
    taus = np.asarray([r["tau_scale"] for r in rows], float)
    ch_map = ch_surface_map(rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in rows], float)
    rad_marg = np.asarray([cls["t_r"] - r["bound4"] for r in rows],
                          float)
    series = (("RAD class margin t_R - RADAU_4/n", rad_marg),
              ("the truth reserve 1 - tr R",
               np.asarray([r["reserve"] for r in rows], float)),
              ("F_best (the sum-rule currency)",
               np.asarray([r["F_best"] for r in rows], float)),
              ("lambda_bad_lo (source-only)",
               np.asarray([r["lam_bad"] for r in rows], float)))
    reloc = []
    for label, arr in series:
        t1, v1 = screen(arr, taus, "%s vs tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask],
                        "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau / c_h relocation screens: relocation seats %s"
          % (",".join(reloc) or "none"), not reloc)
    hs = np.asarray([r["h"] for r in rows], float)
    for label, arr in series[:3]:
        pos = arr > 0
        if int(np.sum(pos)) >= 3:
            slope, two_se, r2, _a = linfit(np.log(hs[pos]),
                                           np.log(arr[pos]))
            print("    h-law of %s: log-log slope %+.4f +/- %.4f "
                  "(2SE), R^2 %.3f" % (label, slope, two_se, r2))


# =============================================================== main
def finish(rows, cls, tiers, sub, seat):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif tiers is None:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        sup3, sup4 = tiers["E3"]["sup"], tiers["E4"]["sup"]
        sup_j = max(sup3, sup4)
        if not tiers["joint_closes"]:
            worst = tiers["E3"] if sup3 >= sup4 else tiers["E4"]
            th = worst["theta"]
            v = ("RADAU-CLASS-LEAKS(joint sup tr R = %.6f >= 1 at "
                 "K = %d; n = %.4g, sigma = %.4f, source = %s)"
                 % (sup_j, KDEG if sup3 >= sup4 else KDEG5,
                    float(th[0]) if th is not None else float("nan"),
                    sigma_quotient(th) if th is not None
                    else float("nan"), worst["src"]))
        elif tiers["env_leaks"]:
            v = ("RADAU-CLASS-CLOSES(joint sup tr R = %.6f at K = 4 "
                 "/ %.6f at K = 5, margin %+.6f; the "
                 "SEPARATE-ENVELOPE tier LEAKS at %.6f) "
                 "[NUMERIC-GLOBAL]"
                 % (sup3, sup4, 1.0 - sup_j, tiers["E2"]["sup"]))
        else:
            v = ("RADAU-CLASS-CLOSES-ENVELOPE-ALSO(joint sup %.6f, "
                 "separate-envelope sup %.6f) [NUMERIC-GLOBAL]"
                 % (sup_j, tiers["E2"]["sup"]))
        if "D3" in tiers:
            d_inf = min(tiers["D3"]["inf"], tiers["D4"]["inf"])
            v += ("\n           +%s(inf lambda_1(J) = %.6e over the "
                  "joint class; separate-envelope control %.6e)"
                  % ("DEFINITE" if tiers.get("def_ok")
                     else "INDEFINITE-ADMITTED", d_inf,
                     tiers["D2"]["inf"]))
        print("\n  VERDICT: %s" % v)
        print("  SUM-RULE SUB-VERDICT: %s" % (sub or "not reached"))
        print("""
  THE CLASS-LEVEL ASSEMBLY, stated with every step typed.  The
  class is
      C_RADAU = C_KS(CCLXI, verbatim)
                AND  n = M[0,0] > 0                    [ENTRY]
                AND  lambda_min(J_B) >= c_B = %.6f     [CO-BLOCK
                                                        PREMISE,
                                                        certified
                                                        per cell by
                                                        the round-62
                                                        exact LDL]
                AND  nu_k in [nu_lo_k, nu_hi_k]        [MOM, measured
                                                        flat, log-
                                                        widened, A2]
                AND  RADAU_K(nu_0..nu_{2K-2}; c_B)
                       <= t_R * n,  t_R = %.4f         [RAD, the
                                                        JOINT source-
                                                        only relation]
  and the box SHA-256 %s was printed before any
  optimization ran.  NOTHING in C_RADAU consumes s, sigma,
  lambda_min(M) or any definiteness-carrying wall eigendatum.  The
  ward that carries this is MOMENT LOCALITY (A8): RADAU_K and the
  MOM box read only the Jacobi coordinates that build
  nu_0..nu_{2K-2}, so a DEEP TAIL perturbation leaves them exactly
  unchanged (AC3) while the circular sigma, which reads the whole
  co-block resolvent, moves (AC4, the control that must fire).  The
  two inherited CCLXI spectral functionals are separately warded
  invariant under the flip J -> -J (AC1/AC2), and the co-block
  floor is warded independent of the pivot and coupling coordinates
  (AC5) where sigma again moves (AC6).
  WHAT THE TIER LADDER SHOWS (the RESERVE question): E0 %.4f ->
  E1 %.4f -> E2 %.4f -> E3 %.4f (K=4) / E4 %.4f (K=5).  %s
  AND THE STRICTLY WEAKER DEFINITENESS QUESTION (A6): inf
  lambda_1(J) = %.4e over the joint class versus %.4e without it --
  %s
  PEDIGREE: every sup is a NUMERIC global (multi-start SLSQP +
  differential evolution, seed %d); an optimizer maximum is a LOWER
  bound of the true supremum, so a LEAK is certain and a CLOSURE is
  numeric, never certified (and symmetrically for the definiteness
  infimum: inf <= 0 would be certain, inf > 0 is numeric).  The
  truth ladder lies inside every tier, so no tier can close below
  its own truth maximum %.4f.
  SCOPE: the deployed 68-step ladder, the tested F0 cells and the
  frozen class; the CCLXXIII edge family is CITED, not rebuilt
  (A5).  NO all-h claim, NO RH claim."""
              % (cls["cb"], cls["t_r"], cls["box_sha"][:32],
                 tiers["E0"]["sup"], tiers["E1"]["sup"],
                 tiers["E2"]["sup"], tiers["E3"]["sup"],
                 tiers["E4"]["sup"],
                 ("The joint relation is the decisive object: the "
                  "separate envelopes leak, the joint relation "
                  "closes." if tiers["env_leaks"]
                  and tiers["joint_closes"] else
                  "The joint relation removes almost all of the "
                  "excess but does NOT close the reserve at every "
                  "declared depth."
                  if not tiers["joint_closes"] else
                  "The separate envelopes already close, so the "
                  "joint relation is not the decisive object here."),
                 min(tiers["D3"]["inf"], tiers["D4"]["inf"]),
                 tiers["D2"]["inf"],
                 ("the joint relation DOES settle definiteness at "
                  "class level, which is exactly CCLXXVII's per-step "
                  "conclusion lifted, and it is the separate "
                  "envelopes that cannot."
                  if tiers.get("def_ok") else
                  "the joint relation does NOT settle definiteness "
                  "either."),
                 OPT_SEED,
                 max(r["trace_r"] for r in rows)))
    print("""
  HONEST FRAME.  Finite numeric and exact-rational statements about
  the deployed ladder artifact, the tested F0 cells and one frozen
  class.  E3 (Gauss-Radau), E7 (interlacing) and the CCXXV
  separator certificates are external-cited and warded, never
  proved here.  No marker moves; no paper, ledger, website,
  manifest or verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.RADAU.CLASS.01 -- the non-circular "
            "class-level assembly (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))
    print("    t_R = %.4f (SIGMA_ENV, CCLXIX); K = %d and %d; "
          "MARGIN_FRAC = %.2f; MOM_MARGIN = %.2f"
          % (T_R_F, KDEG, KDEG5, MARGIN_FRAC, MOM_MARGIN))

    print("\nS0 -- firewall / anti-circularity AST scans")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(CLASS_FUNCS, CLASS_BANNED)
    check("S0.2 AC the JOINT-constraint path carries no sigma, no "
          "Schur gap, no wall margin/trace, no read, no ladder "
          "identifier and NO eigensolver", not ac,
          ",".join(sorted(set(ac))), kill="K2")

    no_go_lemma()
    if KILLS:
        return finish([], None, None, None, None)

    steps, combined = build_ladder()
    if KILLS:
        return finish([], None, None, None, None)
    artifact = artifact_key_ward(steps)
    f0_cells = build_f0(combined)
    if KILLS:
        return finish([], None, None, None, None)
    fdata = get_filter(steps, artifact)
    rows = make_rows(steps, f0_cells, artifact, fdata)
    rows = jacobi_identity_wards(rows)
    if KILLS:
        return finish(rows, None, None, None, None)
    repro_anchors(rows)
    certify_cells(rows)
    if KILLS:
        return finish(rows, None, None, None, None)
    cls = freeze_class(rows, fdata)
    ac_typing(rows, cls)
    membership(rows, cls)
    tiers = extremal(rows, cls, fdata)
    sub, seat, _fc = sum_rule(rows, cls, fdata, tiers)
    controls(rows, cls, fdata, tiers)
    screens(rows, cls)
    return finish(rows, cls, tiers, sub, seat)


if __name__ == "__main__":
    sys.exit(main())
