#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""radau_sos_certificate_probe -- PRIME.ONEBADMODE.RADAU.SOS.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE RATIONAL DUAL CERTIFICATE THAT TURNS THE RADAU CLASS THEOREM INTO
A SHORT, AUDITABLE ALGEBRAIC PROOF OBJECT.  The certified sigma chain
(CCLXXVII exact machine, CCLXXIX K=5 closure over all 151 built
wall-legal cells, CCLXXXI/CCLXXXV joint class) bounds the wall pivot
integral q = int x^{-1} dmu (mu the spectral measure of the co-block
B at the coupling b, moments nu_k = b^T B^k b) by a Gauss-Radau
OPTIMIZATION RUN.  THIS PROBE dualizes the bound by a POLYNOMIAL
MAJORANT: find p_K(x) with p_K(x) >= 1/x on the certified spectral
interval [beta, L]; then

    q <= int p_K dmu = sum_j c_j nu_j        (LINEAR in the
                                              source-only moments),

and the pointwise inequality is certified EXACTLY by the interval SOS
identity

    x p_K(x) - 1 = s_0(x) + (x - beta)(L - x) s_1(x)

with RATIONAL sums of squares s_0, s_1 (rational PSD Gram matrices).
The class statement then reads sum_j c_j nu_j <= (1 - eta) n with a
rational reserve eta (mission target 0.273).  ADVANTAGES: fully
exact-rational certifiable; only source-only moments; avoids the
width-sensitive per-eigenvalue bounds for lambda_2..lambda_7; produces
a SHORT PROOF OBJECT instead of an optimization run.  The numeric
quadrature finds the candidate; the SOS certificate makes it a
theorem.

 (a) THE CANDIDATES.  Per degree K in {4..8} the numeric candidate
     p_K is the optimal L-infinity majorant of 1/x on [beta, L]: the
     Chebyshev best approximation p* (Remez exchange; the classical
     equioscillation object) SHIFTED UP by its error E -- the shifted
     minimax is EXACTLY the optimal uniform one-sided majorant
     (max(p - f) >= 2E_K for every majorant p; p* + E attains it).
     Per cell a second, WEIGHTED candidate family is built: the
     Radau-dual Hermite interpolant of 1/x (simple contact at beta,
     double contacts at the K_R - 1 free Radau nodes of the cell's
     own moment data, K_R in {4, 5}), constructed EXACTLY in
     rational arithmetic in Newton form from the closed-form divided
     differences of 1/x (f[z_0..z_k] = (-1)^k / prod z_j, confluence
     included) at the float Radau nodes rounded to rationals -- its
     error kernel majorizes 1/x for ANY positive contact nodes and
     its moment functional reproduces the Gauss-Radau rule value.
     ADAPTIVELY (A8) a further simple contact at the certified
     ceiling L is added (even total parity, degree 2 K_R - 1, exact
     moments to nu_9) whenever the top Radau node sits below
     DUAL_TOP * L: the L-contact form carries the extra pointwise
     factor (L-x)/L <= 1 against the pure form, so its moment
     functional is <= the Gauss-Radau value -- the SOS route then
     DOMINATES the Radau route by construction (up to the disclosed
     lift) and stays bounded on [beta, L] instead of exploding above
     the top Ritz node; when the top node is within DUAL_TOP of L
     the pure form is already bounded and the L-contact would nearly
     duplicate the top contact (a factorization-hostile near-triple
     zero), so it is omitted.
     BOTH TIERS are built: (i) per-cell certificates on the cell's own
     certified [c_cell, L_cell] (sharpest) and (ii) ONE GLOBAL
     certificate per degree on the covering interval
     [min_cell floor, max_cell L] (the auditable single object;
     honestly weaker -- measured, not assumed).
 (b) THE SOS CERTIFICATE.  Every candidate is certified in
     t-normalized coordinates x = m + w t, t in [-1, 1] (exact
     rational affine map; (x-beta)(L-x) = w^2 (1-t^2)): the target
     T(t) = x(t) p(t) - 1 is decomposed as T = s_0 + (1-t^2) s_1 by a
     hand-rolled deterministic numeric stage -- the CLASSICAL
     Fejer-Riesz route: under t = cos(theta), T becomes a
     nonnegative trigonometric polynomial, its spectral factorization
     |Q(e^{i theta})|^2 (roots of the Laurent polynomial; degree
     <= 9) yields T = A(t)^2 + (1-t^2) B(t)^2 with A = Re Q in the
     Chebyshev T-basis and B = Im Q / sin(theta) in the U-basis
     (eigenvalue-based Gram completion in the elementary sense);
     because every reciprocal-pair root selection gives such a
     factorization and all their rank-one Grams lie in the SAME
     affine Gram set, the AVERAGE over the base selection and the
     one-group flips is a strictly interior (PD) Gram point.  The
     averaged Grams are RATIONALLY ROUNDED at RND_BITS dyadic bits
     with EXACT CORRECTION: G_1 is fixed at its rounded value, the
     exact remainder T - (1-t^2) s_1 is imposed on G_0's
     anti-diagonals, so the identity holds EXACTLY BY CONSTRUCTION;
     positive definiteness of both rational Grams is then decided by
     EXACT-RATIONAL LDL (round-62 machine).  FOR THE NEWTON DUALS
     the numeric stage is BYPASSED ENTIRELY: the complete root
     structure of T is exact (simple zero at beta, double zeros at
     the contact nodes, optionally at L), so the certificate is
     written down in closed form via the Markov-Lukacs split
     (t+1) = ((t+1)^2 + (1-t^2))/2 -- rank-one rational Grams, PSD
     BY STRUCTURE (the stored rank certificate is reconstructed and
     compared entrywise at verification), zero lift, zero numeric
     error.  The
     certificate is congruence-transported to the x-side mission form
     (G_x = C^T G C with C the exact basis-change of u(x) = (x-m)/w;
     congruence preserves PD exactly) and the x-side identity
     x p(x) - 1 = s_0(x) + (x-beta)(L-x) s_1(x) is verified TWICE:
     exact Fraction polynomial arithmetic AND sympy expand (zero
     residual required).  REFUSAL DISCIPLINE: candidates are lifted to
     strict positivity (the lift is part of the stored rational
     candidate and its cost is measured); if rounding breaks exact
     PSD, the ladder escalates (larger lift) and finally REFUSES --
     a refused certificate is never consumed.
 (c) THE CLASS CENSUS.  Per cell (the 151 CCLXXIX wall-legal cells +
     the declared deep-extension slice), the certified linear bound
     q <= sum_j c_j nu_j is evaluated in exact rational arithmetic
     (consumption gate: the certificate interval must COVER the
     cell's certified [c_cell, L_cell], exact comparisons), and the
     reserve check sum_j c_j nu_j <= (1 - eta) n is run: the eta
     table (min/med/max), the census at eta = 0.273, and the largest
     rational eta that passes 151/151 (conservatively truncated).
     THE DELIVERABLE: the frozen proof object -- p_K coefficients as
     exact rationals, the two rational SOS Gram matrices, the
     identity verification hash -- plus the one-line theorem:
     'for every measure with moments nu and support in [beta, L]:
     nu-linear-form <= (1-eta) n implies sigma <= 1-eta implies
     M > 0 (positive definite)' -- every step exact.
 (d) THE COMPARISON.  Per cell: the SOS bounds against the exact
     Gauss-Radau bounds at K = 4 and K = 5 (CCLXXVII/CCLXXIX route,
     recomputed here at the same certified floors) at matched moment
     budget (degree 6 <-> K = 4, degree 8 <-> K = 5); which is
     sharper where; and the honest verdict on whether the single
     global certificate suffices or the per-cell tier is needed.
 (e) GATES.  SOS identity verified exactly (sympy, zero residual, on
     every consumed certificate); PSD of the rational Grams exact;
     controls-must-fire (a synthetic cell with truth sigma > 1 must
     FAIL the linear-bound census -- the CCLXXIX x10-coupling and
     near-1 synthetics; an interval violating the majorant domain
     must be REFUSED at construction AND at consumption; a
     non-majorant candidate must be REFUSED by the SOS stage); tau /
     CCXVII c_h relocation screens on the eta margins;
     anti-circularity (the consumed certificate path sees moments,
     floors, interval endpoints and rational algebra ONLY --
     AST-scanned; the candidate SEARCH is free by design and its
     output is never trusted, only verified).

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E2 Schur / Sylvester: M = [[n, b^T], [b, B]] symmetric is PD iff
    B is PD and s = n - b^T B^{-1} b > 0; a symmetric matrix is PD
    iff the LDL pivots are all positive.  [Horn & Johnson, Matrix
    Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE (comparison route + node
    heuristic only): the K-node Gauss-Radau rule with the node
    prescribed at the spectral floor is an upper bound for
    u^T A^{-1} u.  [Golub & Meurant, PUP 2010, Ch. 6-7.]
 E7 Gershgorin discs and the PSD trace bound: for symmetric B,
    lambda_max(B) <= max_i sum_j |B_ij|; for B PSD additionally
    lambda_max(B) <= tr B.  Both are exact-rational on rational
    entries.  [Horn & Johnson op. cit. Sec. 6.1, 4.2.]
 E8 Markov-Lukacs / interval Positivstellensatz (COMPLETENESS side
    only: certificates of the used form EXIST for polynomials
    positive on [beta, L]).  The SOUNDNESS direction consumed here is
    ELEMENTARY and self-contained: an exact identity
    T = s_0 + (x-beta)(L-x) s_1 with PSD Grams implies T >= 0 on
    [beta, L] by inspection.  [Powers & Reznick, J. Pure Appl.
    Algebra 164 (2001) 221-229.]
 E9 rational SOS rounding (round Gram, project onto the exact affine
    coefficient constraints, decide PSD exactly).  [Peyrl & Parrilo,
    Theor. Comput. Sci. 409 (2008) 269-281.]

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; no RNG seat.
    AC scan on the CONSUMED certificate path (bound_from_cert /
    verify_cert_exact / exact_interval_data / the Fraction polynomial
    kernel): no eigensolver, no linear solver, no truth read, no
    ladder identifier -- moments, floors, interval endpoints and
    rational algebra only.  The candidate-search functions are
    scanned against the truth-read list (sigma / q_wall / gap /
    trace_R / reserve / margin / artifact / lu_read / assemble_step /
    build_rung); their small-matrix eigen/linear solves are DECLARED
    (search is free; soundness never consumes it).
 U  the CCLXXIX universe rebuilt via the K5 probe's builders imported
    READ-ONLY: 42 surface rungs -> 68 ladder steps (artifact-key
    warded), 17 F0 cells, F1/F2/F4/F5 sweep families -> 151 built
    wall-legal cells; inherited identity wards (B/I), pivot ward,
    CCLXV/CCLXIX/CCLXXVII repro anchors (SR); plus the F5X
    deep-extension slice (N5X adjacent depth-extension cells from the
    SAME frozen F5 census law, frozen mode only, reported separately,
    NEVER gating the 151 census).
 E  per cell: exact moments nu_0..nu_8, exact certified LDL floor
    c_cell (round-62 machine, BIS_ITERS = 40), exact CERTIFIED
    CEILING L_cell (the same machine mirrored at the top edge, A2,
    CEIL_ITERS = 48, Gershgorin/trace bracket); wards: 0 floor
    refusals, floor quality <= 1e-6 rel, ceiling quality <= 1e-6
    rel, L_cell >= float lambda_max(B) truth on every cell
    (reference); exact Gauss-Radau K = 4 / K = 5 at c_cell
    (comparison route) with the CCLXXVII anchor (certified K = 4
    ladder max 0.648113) and the CCLXXIX kz-45 anchor (K = 5 bound
    0.726909) reproduced.
 C  the global tier: one certificate per degree K in {4..8} on
    [min floor, max L]; every certificate exact-verified (identity +
    PSD + sympy).
 P  the per-cell tier: Chebyshev candidates at K in {4..8} plus
    L-contact Radau-dual candidates at K_R in {4, 5} (degree
    2 K_R - 1, exact moments to nu_9) on the cell's own interval;
    every consumed certificate exact-verified; the best bound = min
    over VERIFIED certificates (each independently sound; a minimum
    of sound bounds is sound); wards: bound >= truth q/n on every
    cell (0 violations), DOMINATION (the L-contact dual bound <=
    the exact Radau value up to the disclosed lift/rounding excess),
    exact-vs-float cross route on the bound value.
 T  the eta census on the 151 cells: table, census at ETA_TARGET =
    273/1000, the largest passing rational eta (truncated to the
    1e-6 grid, downward = conservative), and the deep-extension
    report (separate).
 M  the comparison: SOS deg 6 vs Radau K = 4, SOS deg 8 vs Radau
    K = 5, global vs per-cell; the honest tier verdict.
 X  controls-must-fire: construction refusal on beta <= 0;
    consumption refusal on a certificate interval NOT covering the
    cell's certified interval; SOS refusal on the UNSHIFTED best
    approximation (a true non-majorant CANNOT be certified -- the
    refusal must fire); the CCLXXIX x10-coupling synthetic and the
    near-1 synthetic (truth sigma = 1.2) must NOT certify below 1
    (exact Fraction comparisons); exact sanity on a synthetic
    diagonal measure with known rational q (bound >= q as Fractions).
 S  screens: tau and CCXVII c_h relocation screens (CCXLVII bars
    verbatim: PASS <= 0.30, RELOC >= 0.70) on the eta margins
    1 - bound and (1 - ETA_TARGET) - bound; h-slopes with 2SE.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 SOS-CLASS-COMPOSED(151/151 cells certified sum c_j nu_j <=
   (1 - 273/1000) n by the per-cell tier; the largest passing
   rational eta stated; the global-tier status stated honestly)
 SOS-CLASS-SCHUR(151/151 cells certified < 1 but the 0.273 reserve
   fails on listed cells)
 SOS-CLASS-PARTIAL(cells with no certificate or certified bound >= 1
   listed precisely).
Every enum is a finite statement about the deployed ladder artifact
and the built CCLXIX/CCLXXIX wall-legal cells; NEVER an all-h
statement, NEVER an RH claim.

FROZEN BARS.  DEGREES = (4,5,6,7,8); KR_SET = (4,5); CAND_BITS = 48;
RND_BITS = 96; TPOS = 2^-40 (strict-positivity target for T, scaled
by max(1, |tau|_inf); deliberately tiny -- the lift cost enters the
bound, so the base target sits just above the exact-stage needs and
the ESCALATION ladder pays more only where the exact LDL demands
it); AFF_REL = 2^-23 (the per-cell lift target is CAPPED in the
bound currency, lift <= AFF_REL n/nu_0, both source-only -- the
escalation ladder may still pay more where the exact LDL demands it,
and the domination ward P4 measures the result); ESC_MAX = 4;
ESC_FAC = 8; DUAL_TOP = 9/10 (the adaptive L-contact switch, A8);
FEJ_THETA = 17
(least-squares scale samples of the spectral factor); the numeric
Gram point is the AVERAGE over the reciprocal root-flip subsets
(smallest subsets first, FEJ_SEL_CAP = 64 -- the average of >= dim+1
independent rank-one factorizations is an interior Gram point;
deterministic; the exact correction and the exact LDL are the final
arbiters);
REMEZ_GRID = 6000; REMEZ_IT = 40; MIN_GRID = 20001; XR_TIE = 1e-6;
CANDB_TIE = 1e-3 (the DOMINATION ward: the L-contact dual bound may
exceed the exact Radau value only by the lift/rounding excess; cells
with a near-degenerate Lanczos tail, min be^2 < CANDB_DEGEN = 1e-6,
are excluded from that ward and PRINTED -- float Radau nodes wander
there while the consumed bound stays SOS-verified and sound);
RB_TIE = 1e-9; ETA_TARGET = 273/1000; ETA_DEN =
10^6; SCHUR_BAR = 1 (exact); RADAU4_CERT_REF = 0.648113 (rtol 2e-3);
KZ45_K5_REF = 0.726909 (rtol 2e-3); FLOOR_Q_RTOL = 1e-6; CELL_EXP =
151 = 68 ladder + 83 sweep (CCLXXIX); N5X = 4 (deep extension, frozen
only, same census law, slice adjacent to CCLXXIX's F5 pick);
BIS_ITERS = 40 (round 62, via the K5 probe); CEIL_ITERS = 48 (the
certified top edge, A2); SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; runtime cap 25 min.  Smoke: the K5 probe's smoke
subsets verbatim (10 contiguous surface rungs + 3 lowest deep, F0 cap
2, F1 cap 3, F2 (6,) x 1, F4 1, F5 SKIPPED), F5X SKIPPED (typed);
count / repro / census gates decide only on the frozen build and
print their subset values (CCLXV T5 pattern).

HONEST AMENDMENTS (declared before the frozen run).
 A1 the 151-cell universe is rebuilt with the CCLXXIX probe's
    builders imported READ-ONLY (which themselves wrap the CCLXIX
    battery builders); its identity wards, pivot ward and repro
    anchors are routed into this run's check registry.  Reuse, not
    re-derivation; disclosed.
 A2 L is NOT the measured lambda_max: the certificate consumes the
    EXACT-RATIONAL CERTIFIED CEILING L_cell -- the round-62 LDL
    machine mirrored at the TOP edge (u I - B positive definite by
    exact LDL implies lambda_max(B) < u, E2), bisected CEIL_ITERS
    times inside the exact Gershgorin/trace bracket (E7; the trace
    bound's PD premise is discharged by the exact floor
    certificate).  The bisection brackets may use the measured
    lambda_max as a HINT (exactly the inherited hi_hint pattern of
    the floor certificate); soundness is the exact LDL at the
    returned u alone.  The measured lambda_max is also the ward
    reference (L_cell must sit above it on every cell, quality
    <= 1e-6 rel).
 A3 the candidate search is float and FREE (Remez exchange, Hermite
    interpolation at float Radau nodes, small-matrix eigensolves,
    alternating projections).  SOUNDNESS never consumes the search:
    only the exact identity, the exact PSD decisions and the exact
    domain comparisons are consumed.  The AC scan covers exactly the
    consumption path; the search functions carry the truth-read ban
    list only.  'The numeric quadrature finds the candidate; the SOS
    certificate makes it a theorem.'
 A4 the REMEZ/CHEBYSHEV candidates are lifted to strict positivity
    of T (numeric guard TPOS, afford-capped by AFF_REL; the lift is
    a rational part of the stored candidate; its cost enters the
    bound and is therefore measured, not hidden).  On exact-PSD
    refusal the ladder escalates the lift (ESC_FAC, at most ESC_MAX
    times) and then REFUSES honestly.  The NEWTON DUALS carry NO
    lift at all: their complete root structure is exact, so their
    closed-form certificates are zero-error (see (b)).
 A5 the census universe is CCLXXIX's 151 built wall-legal cells; the
    deep tier here is the N5X-cell ADJACENT depth-extension slice of
    the same frozen F5 census law -- NOT the concurrent CCLXXXVII
    deep-membership blocks (mission key cited only; no number of
    that probe is consumed).  Extension cells never gate the 151
    census and are reported separately.
 A6 the certificate object is the ASSEMBLED float64 wall matrix
    (dyadic-rational entries, CCVII v897 class) -- CCLXXVII A5
    verbatim: the float64-vs-ideal enclosure stays with the pg_chain
    interval program and is NOT retried here.
 A7 the sympy verification runs on EVERY consumed certificate (x-side
    mission form); the Fraction verification is the independent
    second route.  If the frozen-run budget were threatened the
    sympy tier would be restricted BY DISCLOSED AMENDMENT, never
    silently -- the smoke measures the cost first.
 A8 the dual candidate's L-contact is ADAPTIVE (DUAL_TOP switch, see
    (a)): both forms are majorants by the same closed-form error
    kernel, the choice only trades sharpness against factorization
    conditioning; the domination ward P4 measures the outcome on
    every consumed dual either way.

SMOKE DISCLOSURE (2026-08-12; EIGHT smoke invocations of the ONE
declared smoke configuration -- 10 contiguous surface rungs + 3
lowest deep rungs + F0 cap 2 + F1 cap 3 + F2 (6,)x1 + F4 1 + F5/F5X
skipped = 17 cells -- were run during construction, and every defect
they exposed is listed here with the repair; NO census rule, bar or
verdict enum was weakened at any point, and every repair made the
certificates SHARPER or the controls STRICTER).
 SMOKE-1 (SPEC 3ae03835) killed at C1: the first numeric SOS stage
   (alternating projections onto the affine set and the PSD cone)
   stalled at a residual plateau on the wide covering interval.
   REPAIR: the numeric stage was replaced by the deterministic
   Fejer-Riesz route of (b).
 SMOKE-2/3 (59cbd745, deff128a) failed the dual ward P4 by up to
   rel 2.7: the dual interpolant was solved in a float Chebyshev
   basis (ill-conditioned on wide intervals), then rebuilt EXACTLY
   in Newton form -- and still exploded above the top Ritz node
   because L was the loose Gershgorin/trace bound (up to 100x above
   lambda_max).  REPAIR: the exact-rational CERTIFIED CEILING of A2
   replaced the loose L (E3 quality moved from ~1e2 rel to 1.3e-15
   rel).
 SMOKE-4 (87796b02) failed E3 by float-ulp noise: the certified
   ceiling sits within one double-ulp of lambda_max, so the ward
   comparison gained the 1e-9 rel tolerance (the CERT itself is
   exact and unchanged).
 SMOKE-5/6 (a7c5d9be, 7d76dc54) still failed P4 by 1.8e-3..8e-2:
   the residual excess was the LIFT cost of the numerically
   certified dual (near-triple zero at t = +1 when the top Radau
   node coincides with L; escalations paid lift into the bound).
   REPAIR: the adaptive L-contact (A8) plus the decisive step --
   the CLOSED-FORM zero-lift dual certificates of (b), which need
   no numeric stage at all.  After this repair the dual bounds tie
   the exact Radau values to all printed digits.
 SMOKE-7 (d59eea15) failed only X2, the domain-refusal CONTROL,
   because the control CLAIMED a floor ABOVE the global
   certificate's beta -- a legitimately covered case.  REPAIR: the
   control now violates coverage in both directions (floor below
   cert beta, ceiling above cert L); the consumption gate itself
   was correct and unchanged.
 SMOKE-8 (a1f22d35, 23.2 s, 17 cells) was FULLY GREEN: 50/50
   checks, no kills; 5/5 global certificates verified (identity
   exact, sympy residual 0, exact PSD; covering ratio 1.01e6), 119
   per-cell certificates verified with 0 refusals, P4 all dominate
   (the radau-dual-8 bounds EQUAL the exact Radau K = 5 values to
   all printed digits), census 17/17 at eta = 0.273 with subset
   eta* = 87357/200000 = 0.4368, global tier honest-weak (1/17
   below 1 -- the per-cell tier is needed), all six controls fired,
   screens PASS (|slope| <= 0.034), sympy tier cost negligible
   (A7 restriction NOT needed).  The verdict line printed
   SOS-CLASS-COMPOSED on the subset; no subset number is consumed
   by the frozen run.
 THE ONLY changes after SMOKE-8 are one stale narrative line in the
 verdict text (the L pedigree now names the certified ceiling
 instead of the pre-repair Gershgorin/trace bound) and this
 disclosure text.  The SPEC SHA moves with this text, as disclosed.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edits outside this file are
the proof-object JSON artifact radau_sos_certificate_proof.json
(frozen run only, experiments/tfpt-discovery/) and the German CCXCIII
line prepended to experiments/next.txt AFTER the frozen summary.

Sources (read-only): bfloor_k5_closure_probe (CCLXXIX universe +
exact machine, imported READ-ONLY, cited), onebadmode_moments_probe
(CCVII ladder + wall blocks), zolotarev_phase_filter_probe (CCXXV
step assembly), sigma_stress_battery_probe (CCLXIX builders),
bfloor_perstep_certification_probe (CCLXXVII exact machine, via
CCLXXIX), sigma_coupling_pivot_probe (CCLXV Radau machinery, cited),
radau_class_assembly_probe / radau_class_close_probe (CCLXXXI /
CCLXXXV class frame, cited), euler_phase_identity_probe (CCXVII c_h),
v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/radau_sos_certificate_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/radau_sos_certificate_probe.py
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
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import bfloor_k5_closure_probe as k5          # noqa: E402 (READ-ONLY)
import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import sigma_stress_battery_probe as bat      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
DEGREES = (4, 5, 6, 7, 8)
KR_SET = (4, 5)
CAND_BITS = 48
RND_BITS = 96
FEJ_THETA = 17
FEJ_SEL_CAP = 64
TPOS = 2.0 ** -40
AFF_REL = 2.0 ** -23
DUAL_TOP = Fraction(9, 10)
ESC_MAX = 4
ESC_FAC = 8
REMEZ_GRID = 6000
REMEZ_IT = 40
MIN_GRID = 20001
XR_TIE = 1.0e-6
CANDB_TIE = 1.0e-3
CANDB_DEGEN = 1.0e-6
RB_TIE = 1.0e-9
ETA_TARGET = Fraction(273, 1000)
ETA_DEN = 10 ** 6
SCHUR_BAR = Fraction(1)
RADAU4_CERT_REF = 0.648113
KZ45_K5_REF = 0.726909
REF_RTOL = 2.0e-3
FLOOR_Q_RTOL = 1.0e-6
CEIL_ITERS = 48
CELL_EXP = 151
N5X = 4
PROOF_JSON = os.path.join(_HERE, "radau_sos_certificate_proof.json")

SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()

# route the K5 probe's check registry into this run (CCLXXXV pattern)
k5.CHECKS = []
k5.KILLS = []
k5.SMOKE = SMOKE
k5.T0 = T0
CHECKS = k5.CHECKS
KILLS = k5.KILLS
check = k5.check
section = k5.section

BANNED_IDS = k5.BANNED_IDS
# the CONSUMED certificate path: moments, floors, interval endpoints
# and rational algebra only -- no eigensolver, no linear solver, no
# truth read, no ladder identifier.
CONSUME_FUNCS = ("bound_from_cert", "verify_cert_exact",
                 "exact_interval_data", "gram_to_poly", "p_add",
                 "p_sub", "p_mul", "compose_poly")
CONSUME_BANNED = ("sigma", "sigma_quotient", "q_wall", "lamB1",
                  "lam_b", "eigs", "eigvals", "eigvalsh", "eigh",
                  "eig", "inv", "pinv", "lstsq", "solve", "roots",
                  "gap", "trace_R", "reserve", "margin", "artifact",
                  "lu_read", "assemble_step", "build_rung", "theta",
                  "step", "steps", "kz")
# the candidate SEARCH is free (A3) but may not read the truth
CAND_FUNCS = ("remez_candidate", "cheb_fallback",
              "newton_dual_candidate", "numeric_min_t",
              "_lift_loop", "lift_candidate", "lift_rational",
              "fejer_factor", "sos_certify")
CAND_BANNED = ("sigma", "sigma_quotient", "q_wall", "gap", "trace_R",
               "reserve", "margin", "artifact", "lu_read",
               "assemble_step", "build_rung")

FR0 = Fraction(0)
FR1 = Fraction(1)


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


# ============================ exact Fraction polynomial kernel
def p_add(pa, pb):
    """Coefficient lists (ascending), exact Fractions."""
    out = [FR0] * max(len(pa), len(pb))
    for i, v in enumerate(pa):
        out[i] += v
    for i, v in enumerate(pb):
        out[i] += v
    return out


def p_sub(pa, pb):
    return p_add(pa, [-v for v in pb])


def p_mul(pa, pb):
    out = [FR0] * (len(pa) + len(pb) - 1)
    for i, va in enumerate(pa):
        if va == 0:
            continue
        for j, vb in enumerate(pb):
            out[i + j] += va * vb
    return out


def compose_poly(pa, inner):
    """p(inner(x)) for coefficient lists of exact Fractions."""
    out = [pa[-1]]
    for k in range(len(pa) - 2, -1, -1):
        out = p_mul(out, inner)
        out = p_add(out, [pa[k]])
    return out


def gram_to_poly(gm):
    """Anti-diagonal sums of a Fraction Gram matrix -> s(t) coeffs."""
    dim = len(gm)
    out = [FR0] * (2 * dim - 1)
    for i in range(dim):
        for j in range(dim):
            out[i + j] += gm[i][j]
    return out


def fr_round(value, bits):
    return Fraction(int(round(float(value) * (1 << bits))), 1 << bits)


def mat_round(mm, bits):
    mm = 0.5 * (mm + mm.T)
    dim = mm.shape[0]
    return [[fr_round(mm[i, j], bits) for j in range(dim)]
            for i in range(dim)]


def exact_interval_data(matrix):
    """Pivot n, exact moments nu_0..nu_9 and the exact source-only
    upper edge candidates (Gershgorin row bound, trace) of the
    co-block -- entries only, exact Fractions (E7)."""
    piv, momv, blk = k5.exact_wall_data(matrix, 9)
    dim = len(blk)
    gersh = max(sum(abs(blk[i][j]) for j in range(dim))
                for i in range(dim))
    trace = sum(blk[i][i] for i in range(dim))
    return piv, momv, blk, gersh, trace


def cert_ceiling_exact(blk, lo, hi, iters=CEIL_ITERS):
    """Smallest certified u in [lo, hi] with u I - B positive
    definite (exact-rational LDL, the round-62 machine mirrored at
    the TOP edge): u I - B PD implies lambda_max(B) < u (E2).
    lo/hi are brackets only; soundness is the exact LDL at the
    returned u.  None if even hi is refused."""
    dim = len(blk)

    def shifted_pd(uu):
        mm = [[(uu if i == j else FR0) - blk[i][j]
               for j in range(dim)] for i in range(dim)]
        okp, _ip = k5.pd_exact(mm)
        return okp

    lo = Fraction(lo)
    hi = Fraction(hi)
    if hi < lo:
        hi = lo
    if not shifted_pd(hi):
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        if shifted_pd(mid):
            hi = mid
        else:
            lo = mid
    assert shifted_pd(hi)
    return hi


# ============================ numeric candidate machinery (A3: free)
def _cheb_mono_table(deg):
    """Monomial coefficients of T_0..T_deg (exact ints, ascending)."""
    tab = [[1], [0, 1]]
    for _k in range(2, deg + 1):
        nxt = [0] + [2 * c for c in tab[-1]]
        for i, c in enumerate(tab[-2]):
            nxt[i] -= c
        tab.append(nxt)
    return tab[:deg + 1]


def _cheb_vals(tpts, deg):
    """Chebyshev Vandermonde T_j(t_i)."""
    tpts = np.asarray(tpts, float)
    vv = np.zeros((len(tpts), deg + 1))
    vv[:, 0] = 1.0
    if deg >= 1:
        vv[:, 1] = tpts
    for j in range(2, deg + 1):
        vv[:, j] = 2.0 * tpts * vv[:, j - 1] - vv[:, j - 2]
    return vv


def cheb_fallback(beta_f, l_f, deg):
    """Chebyshev interpolation of 1/x at deg+1 Chebyshev points --
    the Remez fallback candidate (validity comes from the SOS stage
    anyway; this only costs sharpness)."""
    mid = 0.5 * (beta_f + l_f)
    hw = 0.5 * (l_f - beta_f)
    tpts = -np.cos(np.pi * (np.arange(deg + 1) + 0.5) / (deg + 1))
    vv = _cheb_vals(tpts, deg)
    rhs = 1.0 / (mid + hw * tpts)
    gam = np.linalg.solve(vv, rhs)
    return gam, float("nan")


def remez_candidate(beta_f, l_f, deg):
    """Remez exchange for the best degree-deg approximation of 1/x on
    [beta_f, l_f], in t-Chebyshev basis.  Returns (gamma, E)."""
    if not (beta_f > 0.0 and l_f > beta_f):
        return None
    mid = 0.5 * (beta_f + l_f)
    hw = 0.5 * (l_f - beta_f)

    def gfun(tt):
        return 1.0 / (mid + hw * np.asarray(tt, float))

    xg = np.exp(np.linspace(math.log(beta_f), math.log(l_f),
                            REMEZ_GRID))
    tg = np.clip((xg - mid) / hw, -1.0, 1.0)
    tg = np.unique(np.concatenate([tg, [-1.0, 1.0]]))
    refs = -np.cos(np.pi * np.arange(deg + 2) / (deg + 1))
    gam = None
    err_e = 0.0
    for _it in range(REMEZ_IT):
        vv = _cheb_vals(refs, deg)
        amat = np.zeros((deg + 2, deg + 2))
        amat[:, :deg + 1] = vv
        amat[:, deg + 1] = (-1.0) ** np.arange(deg + 2)
        try:
            sol = np.linalg.solve(amat, gfun(refs))
        except np.linalg.LinAlgError:
            return cheb_fallback(beta_f, l_f, deg)
        gam = sol[:deg + 1]
        err_e = abs(float(sol[deg + 1]))
        err = _cheb_vals(tg, deg) @ gam - gfun(tg)
        # sign-run partition -> one extremum per run
        sgn = np.sign(err)
        sgn[sgn == 0] = 1.0
        cuts = np.nonzero(np.diff(sgn))[0]
        segs = np.split(np.arange(len(tg)), cuts + 1)
        cand = [seg[np.argmax(np.abs(err[seg]))] for seg in segs
                if len(seg)]
        if len(cand) < deg + 2:
            break
        while len(cand) > deg + 2:
            mags = [abs(err[i]) for i in cand]
            drop = int(np.argmin(mags))
            cand.pop(drop)
        new_refs = tg[np.asarray(cand, int)]
        emax = float(np.max(np.abs(err)))
        if emax <= err_e * (1.0 + 1.0e-9):
            refs = new_refs
            break
        refs = new_refs
    if gam is None:
        return cheb_fallback(beta_f, l_f, deg)
    return gam, err_e


def numeric_min_t(a_float, mid, hw):
    """Numeric min (and argmin) of T(t) = (mid + hw t) p(t) - 1 on
    [-1, 1] (guard only; exactness comes from the SOS stage)."""
    pt = np.asarray(a_float, float)
    tt = np.polymul(pt[::-1], np.asarray([hw, mid]))
    tt[-1] -= 1.0
    grid = np.linspace(-1.0, 1.0, MIN_GRID)
    vals = np.polyval(tt, grid)
    imin = int(np.argmin(vals))
    best = float(vals[imin])
    arg = float(grid[imin])
    dtt = np.polyder(tt)
    if len(dtt):
        try:
            rts = np.roots(dtt)
        except np.linalg.LinAlgError:
            rts = np.asarray([])
        for rr in rts:
            if abs(rr.imag) < 1.0e-9 and -1.0 <= rr.real <= 1.0:
                vv = float(np.polyval(tt, rr.real))
                if vv < best:
                    best = vv
                    arg = float(rr.real)
    return best, arg


def newton_dual_candidate(beta_fr, nodes_fr, l_contact=None):
    """Radau-dual majorant, EXACT-RATIONAL Newton form: the Hermite
    interpolant of 1/x with a simple contact at beta, double
    contacts at the interior Radau nodes and (adaptively) a simple
    contact at L (EVEN total contact parity in the L-contact form).
    The divided differences of 1/x are closed-form (confluence
    included): f[z_0..z_k] = (-1)^k / (z_0 z_1 ... z_k).
    PURE form (l_contact None, odd parity): error
    f - p = f[z.., x] (x-beta) prod (x-t_i)^2 <= 0 for x >= beta --
    p majorizes 1/x on [beta, inf) and its moment functional IS the
    Gauss-Radau value (the rule is exact at this degree).
    L-CONTACT form: error f - p = f[z.., x] (x-beta)(x-L)
    prod (x-t_i)^2 <= 0 on [beta, L]; against the PURE form with the
    same interior nodes it carries the extra pointwise factor
    (L-x)/L <= 1, so its moment functional is <= the Gauss-Radau
    value.  Returns exact x-monomial Fraction coefficients."""
    zz = [beta_fr]
    for nd in nodes_fr:
        if nd <= 0:
            return None
        zz += [nd, nd]
    if l_contact is not None:
        zz.append(l_contact)
    p_x = [FR0]
    basis = [FR1]
    prod_z = FR1
    for k, zk in enumerate(zz):
        prod_z *= zk
        ck = (FR1 if k % 2 == 0 else -FR1) / prod_z
        p_x = p_add(p_x, [ck * b for b in basis])
        basis = p_mul(basis, [-zk, FR1])
    return p_x


def _lift_loop(a_fr, beta_fr, l_fr, ref_scale, cap=None):
    """Lift a rational t-monomial candidate until the numeric min of
    T is >= the TPOS target (A4), optionally capped in the BOUND
    currency (cap = AFF_REL * n/nu_0 * beta, source-only).  Returns
    (a_fr, minT, lift_fr) or None."""
    mid_f = float((beta_fr + l_fr) / 2)
    hw_f = float((l_fr - beta_fr) / 2)
    minv, arg = numeric_min_t([float(v) for v in a_fr], mid_f, hw_f)
    target = TPOS * max(1.0, ref_scale * float(l_fr))
    if cap is not None:
        target = min(target, max(cap, 2.0 ** -48))
    lift = FR0
    tries = 0
    while minv < target and tries < 8:
        x_at = max(mid_f + hw_f * arg, float(beta_fr))
        need = (target - minv) * 1.05 / x_at
        dlt = fr_round(need, CAND_BITS)
        if dlt <= 0:
            dlt = Fraction(1, 1 << CAND_BITS)
        a_fr[0] += dlt
        lift += dlt
        minv, arg = numeric_min_t([float(v) for v in a_fr], mid_f,
                                  hw_f)
        tries += 1
    if minv <= 0.0:
        return None
    return a_fr, minv, lift


def lift_candidate(gam, beta_fr, l_fr, shift, cap=None):
    """t-Chebyshev floats -> rational t-monomial candidate, lifted so
    the numeric min of T is >= the TPOS target (A4).  Returns
    (a_fr, minT, lift_fr) or None."""
    deg = len(gam) - 1
    tab = _cheb_mono_table(deg)
    a_float = np.zeros(deg + 1)
    for j, gj in enumerate(gam):
        for i, cc in enumerate(tab[j]):
            a_float[i] += gj * cc
    if shift:
        a_float[0] += shift
    a_fr = [fr_round(v, CAND_BITS) for v in a_float]
    return _lift_loop(a_fr, beta_fr, l_fr,
                      float(np.max(np.abs(a_float))), cap)


def lift_rational(a_fr, beta_fr, l_fr, cap=None):
    """Lift an EXACT rational t-monomial candidate (Newton dual)."""
    ref = max(abs(float(v)) for v in a_fr)
    return _lift_loop(list(a_fr), beta_fr, l_fr, ref, cap)


# ================================ the SOS stage (numeric + exact)
def _u_mono_table(deg):
    """Monomial coefficients of U_0..U_deg (exact ints, ascending)."""
    tab = [[1], [0, 2]]
    for _k in range(2, deg + 1):
        nxt = [0] + [2 * c for c in tab[-1]]
        for i, c in enumerate(tab[-2]):
            nxt[i] -= c
        tab.append(nxt)
    return tab[:deg + 1]


def fejer_factor(tau_f):
    """Fejer-Riesz stage: T(cos theta) >= 0 -> spectral factors
    |Q|^2 = A(t)^2 + (1-t^2) B(t)^2, one per reciprocal root
    selection (base + one-group flips).  Returns a list of
    (a_mono, b_mono) float coefficient vectors."""
    cheb = np.polynomial.chebyshev.poly2cheb(np.asarray(tau_f, float))
    dd = len(cheb) - 1
    if dd < 1:
        return []
    lp = np.zeros(2 * dd + 1)
    lp[dd] = cheb[0]
    for k in range(1, dd + 1):
        lp[dd + k] += cheb[k] / 2.0
        lp[dd - k] += cheb[k] / 2.0
    try:
        rts = np.roots(lp[::-1])
    except np.linalg.LinAlgError:
        return []
    if len(rts) != 2 * dd:
        return []
    inside = sorted(rts, key=abs)[:dd]
    # conjugate groups (flip a complex pair together to stay real)
    used = [False] * dd
    groups = []
    for i, rr in enumerate(inside):
        if used[i]:
            continue
        used[i] = True
        if abs(rr.imag) <= 1.0e-12 * max(1.0, abs(rr)):
            groups.append([i])
            continue
        best_j, best_d = None, float("inf")
        for j in range(i + 1, dd):
            if used[j]:
                continue
            dj = abs(inside[j] - np.conj(rr))
            if dj < best_d:
                best_d, best_j = dj, j
        if best_j is not None and best_d <= 1.0e-6 * max(1.0,
                                                         abs(rr)):
            used[best_j] = True
            groups.append([i, best_j])
        else:
            groups.append([i])
    # all flip subsets, smallest first, capped (rank of the average
    # Gram needs >= dd+1 independent selections)
    import itertools
    sels = []
    for size in range(len(groups) + 1):
        for combo in itertools.combinations(range(len(groups)),
                                            size):
            sel = list(inside)
            ok = True
            for gi in combo:
                for idx in groups[gi]:
                    if sel[idx] == 0:
                        ok = False
                        break
                    sel[idx] = 1.0 / np.conj(sel[idx])
                if not ok:
                    break
            if ok:
                sels.append(sel)
            if len(sels) >= FEJ_SEL_CAP:
                break
        if len(sels) >= FEJ_SEL_CAP:
            break
    ths = np.linspace(0.15, math.pi - 0.15, FEJ_THETA)
    tv = np.polynomial.chebyshev.chebval(np.cos(ths), cheb)
    utab = _u_mono_table(max(dd - 1, 0))
    packs = []
    for sel in sels:
        qd = np.poly(sel)                       # descending, monic
        if float(np.max(np.abs(qd.imag))) > 1.0e-7 * max(
                1.0, float(np.max(np.abs(qd)))):
            continue
        qd = qd.real
        qv2 = np.abs(np.polyval(qd, np.exp(1j * ths))) ** 2
        den = float(np.sum(qv2 * qv2))
        if den <= 0.0:
            continue
        kap2 = float(np.sum(tv * qv2)) / den    # least-squares scale
        if kap2 <= 0.0:
            continue
        qq = math.sqrt(kap2) * qd[::-1]         # ascending z-poly
        a_mono = np.polynomial.chebyshev.cheb2poly(qq)
        b_mono = np.zeros(max(dd, 1))
        for k in range(1, dd + 1):
            for i, cc in enumerate(utab[k - 1]):
                b_mono[i] += qq[k] * cc
        packs.append((a_mono, b_mono))
    return packs


def sos_certify(a_fr, beta_fr, l_fr, minv):
    """The rational-SOS pipeline in t-coordinates: Fejer-Riesz
    average Gram -> rational rounding -> exact anti-diagonal
    correction on G0 -> exact LDL.  Returns (G0_t, G1_t) as Fraction
    matrices or None (REFUSED)."""
    mid_fr = (beta_fr + l_fr) / 2
    hw_fr = (l_fr - beta_fr) / 2
    tau = p_mul([mid_fr, hw_fr], a_fr)
    tau[0] -= FR1
    dd = len(tau) - 1
    tau_f = np.asarray([float(v) for v in tau])
    packs = fejer_factor(tau_f)
    if not packs:
        return None
    n0 = dd + 1
    n1 = dd
    g0f = np.zeros((n0, n0))
    g1f = np.zeros((n1, n1))
    for a_mono, b_mono in packs:
        av = np.zeros(n0)
        av[:len(a_mono)] = a_mono[:n0]
        bv = np.zeros(n1)
        bv[:len(b_mono)] = b_mono[:n1]
        g0f += np.outer(av, av)
        g1f += np.outer(bv, bv)
    g0f /= len(packs)
    g1f /= len(packs)
    if (float(np.linalg.eigvalsh(g0f)[0]) <= 0.0
            or float(np.linalg.eigvalsh(g1f)[0]) <= 0.0):
        return None
    w2 = [FR1, FR0, -FR1]
    g1r = mat_round(g1f, RND_BITS)
    s1 = gram_to_poly(g1r)
    rem = p_sub(tau + [FR0] * (2 * dd + 1 - len(tau)),
                p_mul(w2, s1))
    g0r = mat_round(g0f, RND_BITS)
    for kk in range(2 * dd + 1):
        cur = FR0
        ents = []
        for i in range(n0):
            j = kk - i
            if 0 <= j < n0:
                cur += g0r[i][j]
                ents.append((i, j))
        dk = (rem[kk] if kk < len(rem) else FR0) - cur
        if dk != 0 and ents:
            share = dk / len(ents)
            for i, j in ents:
                g0r[i][j] += share
    ok0, _p0 = k5.pd_exact(g0r)
    ok1, _p1 = k5.pd_exact(g1r)
    if ok0 and ok1:
        return g0r, g1r
    return None


def _basis_change(h_deg, mid_fr, hw_fr):
    """Rows i = monomial-x coefficients of u(x)^i, u = (x-mid)/hw."""
    upoly = [-mid_fr / hw_fr, FR1 / hw_fr]
    rows = [[FR1] + [FR0] * h_deg]
    cur = [FR1]
    for _i in range(h_deg):
        cur = p_mul(cur, upoly)
        rows.append(list(cur) + [FR0] * (h_deg + 1 - len(cur)))
    return rows


def _congruence(gt, cc):
    dim = len(gt)
    out = [[FR0] * (len(cc[0])) for _ in range(len(cc[0]))]
    for i in range(dim):
        for j in range(dim):
            gij = gt[i][j]
            if gij == 0:
                continue
            ri, rj = cc[i], cc[j]
            for a, va in enumerate(ri):
                if va == 0:
                    continue
                for b, vb in enumerate(rj):
                    if vb == 0:
                        continue
                    out[a][b] += gij * va * vb
    return out


def exact_dual_certificate(deg_label, a_t, beta_fr, l_fr, taus_fr,
                           with_l):
    """The CLOSED-FORM certificate for the Newton dual: the complete
    root structure of T = x p - 1 is known exactly (simple zero at
    beta = t=-1, double zeros at the contact nodes, and at L = t=+1
    in the L-contact form), so the SOS decomposition is written down
    exactly -- PURE form via the Markov-Lukacs split
    (t+1) = ((t+1)^2 + (1-t^2))/2:
        T = (C/2) ((t+1) prod(t-tau_i))^2
            + (1-t^2) (C/2) (prod(t-tau_i))^2,
    L-CONTACT form: T = (1-t^2) C (prod(t-tau_i))^2 (s_0 = 0).
    Rank-one Grams, PSD BY STRUCTURE, zero numeric stage, zero
    lift.  Exact polynomial verification decides; None on any
    mismatch."""
    mid_fr = (beta_fr + l_fr) / 2
    hw_fr = (l_fr - beta_fr) / 2
    tau = p_mul([mid_fr, hw_fr], a_t)
    tau[0] -= FR1
    pin = [FR1]
    for tt in taus_fr:
        pin = p_mul(pin, [-tt, FR1])
    if with_l:
        base = p_mul([FR1, FR0, -FR1], p_mul(pin, pin))
    else:
        s_out = p_mul([FR1, FR1], pin)
        base = p_add(p_mul(s_out, s_out),
                     p_mul([FR1, FR0, -FR1], p_mul(pin, pin)))
        base = [v / 2 for v in base]
    idx = max(range(len(base)), key=lambda i: abs(float(base[i])))
    if base[idx] == 0:
        return None
    cc = tau[idx] / base[idx] if idx < len(tau) else None
    if cc is None or cc <= 0:
        return None
    scaled = [cc * v for v in base]
    diff = p_sub(tau, scaled)
    if any(v != 0 for v in diff):
        return None
    n0 = len(tau) // 2 + 1
    n1 = n0 - 1
    if with_l:
        g0t = [[FR0] * n0 for _ in range(n0)]
        v1 = list(pin) + [FR0] * (n1 - len(pin))
        g1t = [[cc * v1[i] * v1[j] for j in range(n1)]
               for i in range(n1)]
        rk0 = []
        rk1 = [(cc, v1)]
    else:
        v0 = list(s_out) + [FR0] * (n0 - len(s_out))
        v1 = list(pin) + [FR0] * (n1 - len(pin))
        half = cc / 2
        g0t = [[half * v0[i] * v0[j] for j in range(n0)]
               for i in range(n0)]
        g1t = [[half * v1[i] * v1[j] for j in range(n1)]
               for i in range(n1)]
        rk0 = [(half, v0)]
        rk1 = [(half, v1)]
    c_x = compose_poly(a_t, [-mid_fr / hw_fr, FR1 / hw_fr])
    cmat0 = _basis_change(n0 - 1, mid_fr, hw_fr)
    cmat1 = _basis_change(n1 - 1, mid_fr, hw_fr)
    g0x = _congruence(g0t, cmat0)
    g1x = _congruence(g1t, cmat1)
    w2inv = FR1 / (hw_fr * hw_fr)
    g1x = [[v * w2inv for v in row] for row in g1x]

    def push(rk, cmat, scale):
        out = []
        for cf, vec in rk:
            nv = [FR0] * len(cmat[0])
            for i, vi in enumerate(vec):
                if vi == 0:
                    continue
                for j, cj in enumerate(cmat[i]):
                    nv[j] += vi * cj
            out.append((cf * scale, nv))
        return out

    cert = dict(kind="radau-dual", deg=deg_label, beta=beta_fr,
                L=l_fr, a_t=list(a_t), c_x=c_x, G0=g0x, G1=g1x,
                G0_rank=push(rk0, cmat0, FR1),
                G1_rank=push(rk1, cmat1, w2inv),
                lift=FR0, minT=0.0)
    okv, hh = verify_cert_exact(cert)
    if not okv:
        return None
    cert["hash"] = hh
    cert["verified"] = True
    return cert


def make_certificate(kind, deg_label, a_fr, beta_fr, l_fr, minv,
                     lift):
    """Full certificate: t-side SOS -> x-side congruence -> exact +
    sympy verification -> hash.  Returns cert dict or None."""
    cur_a = list(a_fr)
    cur_min = minv
    cur_lift = lift
    for _esc in range(ESC_MAX + 1):
        got = sos_certify(cur_a, beta_fr, l_fr, cur_min)
        if got is not None:
            g0t, g1t = got
            break
        bump = fr_round(max(cur_min * ESC_FAC, TPOS)
                        / float(beta_fr), CAND_BITS)
        if bump <= 0:
            bump = Fraction(1, 1 << (CAND_BITS - 8))
        cur_a[0] += bump
        cur_lift += bump
        cur_min, _arg = numeric_min_t([float(v) for v in cur_a],
                                      float((beta_fr + l_fr) / 2),
                                      float((l_fr - beta_fr) / 2))
    else:
        return None
    mid_fr = (beta_fr + l_fr) / 2
    hw_fr = (l_fr - beta_fr) / 2
    c_x = compose_poly(cur_a, [-mid_fr / hw_fr, FR1 / hw_fr])
    h0 = len(g0t) - 1
    h1 = len(g1t) - 1
    g0x = _congruence(g0t, _basis_change(h0, mid_fr, hw_fr))
    g1x = _congruence(g1t, _basis_change(h1, mid_fr, hw_fr))
    w2inv = FR1 / (hw_fr * hw_fr)
    g1x = [[v * w2inv for v in row] for row in g1x]
    cert = dict(kind=kind, deg=deg_label, beta=beta_fr, L=l_fr,
                a_t=cur_a, c_x=c_x, G0=g0x, G1=g1x, lift=cur_lift,
                minT=cur_min)
    okv, hh = verify_cert_exact(cert)
    if not okv:
        return None
    cert["hash"] = hh
    cert["verified"] = True
    return cert


def verify_cert_exact(cert):
    """EXACT verification of the x-side mission identity
    x p(x) - 1 = s0(x) + (x-beta)(L-x) s1(x): Fraction polynomial
    route AND sympy expand (zero residual), exact LDL PSD on both
    Grams.  Returns (ok, hash)."""
    beta_fr = cert["beta"]
    l_fr = cert["L"]
    if not (beta_fr > 0 and l_fr > beta_fr):
        return False, ""
    c_x = cert["c_x"]
    g0x = cert["G0"]
    g1x = cert["G1"]

    def psd_ok(gx, rank_key):
        """PSD decision: exact rank certificate (sum of positive
        multiples of outer squares, reconstructed and compared
        entrywise -- PSD manifest) or exact strict LDL."""
        rank = cert.get(rank_key)
        if rank is not None:
            dim = len(gx)
            acc = [[FR0] * dim for _ in range(dim)]
            for cf, vec in rank:
                if cf <= 0:
                    return False
                for i in range(dim):
                    vi = vec[i]
                    if vi == 0:
                        continue
                    for j in range(dim):
                        acc[i][j] += cf * vi * vec[j]
            return all(acc[i][j] == gx[i][j]
                       for i in range(dim) for j in range(dim))
        okp, _ip = k5.pd_exact(gx)
        return okp

    if not (psd_ok(g0x, "G0_rank") and psd_ok(g1x, "G1_rank")):
        return False, ""
    lhs = p_mul([FR0, FR1], c_x)
    lhs[0] -= FR1
    wx = [-beta_fr * l_fr, beta_fr + l_fr, -FR1]
    rhs = p_add(gram_to_poly(g0x), p_mul(wx, gram_to_poly(g1x)))
    diff = p_sub(lhs, rhs)
    if any(v != 0 for v in diff):
        return False, ""
    xs = sp.Symbol("x")
    pexp = sum(sp.Rational(v.numerator, v.denominator) * xs ** i
               for i, v in enumerate(c_x))
    s0exp = sum(sp.Rational(v.numerator, v.denominator) * xs ** i
                for i, v in enumerate(gram_to_poly(g0x)))
    s1exp = sum(sp.Rational(v.numerator, v.denominator) * xs ** i
                for i, v in enumerate(gram_to_poly(g1x)))
    bq = sp.Rational(beta_fr.numerator, beta_fr.denominator)
    lq = sp.Rational(l_fr.numerator, l_fr.denominator)
    resid = sp.expand(xs * pexp - 1 - s0exp
                      - (xs - bq) * (lq - xs) * s1exp)
    if resid != 0:
        return False, ""
    blob = "|".join(
        [str(beta_fr), str(l_fr)]
        + [str(v) for v in c_x]
        + [str(v) for row in g0x for v in row]
        + [str(v) for row in g1x for v in row])
    return True, hashlib.sha256(blob.encode()).hexdigest()[:16]


def bound_from_cert(cert, momv, piv, c_cell, l_cell):
    """THE CONSUMED LINEAR BOUND: sum_j c_j nu_j / n, exact Fractions.
    Domain gate: the certificate interval must COVER the cell's
    certified [c_cell, l_cell]; REFUSED (None) otherwise."""
    if cert is None or not cert.get("verified"):
        return None
    if not (cert["beta"] <= c_cell and cert["L"] >= l_cell):
        return None
    coeffs = cert["c_x"]
    if len(momv) < len(coeffs) or piv <= 0:
        return None
    acc = FR0
    for cf, mv in zip(coeffs, momv):
        acc += cf * mv
    return acc / piv


# ============================================ universe + exact data
def build_f5x(combined):
    """The declared deep-extension slice: the SAME frozen F5 census
    law as the K5 probe, the ADJACENT slice after CCLXXIX's N5 pick
    (amendment A5).  Frozen mode only."""
    section("F5X -- the deep-extension slice (adjacent to the "
            "CCLXXIX F5 pick, same census law)")
    if SMOKE:
        print("    F5X SMOKE-SKIPPED (typed)")
        return []
    lam2 = core.von_mangoldt_table(k5.TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    g2 = np.diff(u2)
    reg_deep = {kz for kz, _hz in ob.deep_zone_census()}
    f5_new = []
    for kz in range(2, min(k5.KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        hz = mz // 2
        x_val = math.exp(2.0 * alpha)
        if x_val > k5.TAB2 or kz in reg_deep:
            continue
        newly = ((2900 < hz) or (x_val > ob.TAB_EXT and 128 <= hz))
        if not newly:
            continue
        if hz <= k5.H5_CAP:
            f5_new.append((hz, kz, alpha, mz, x_val))
    f5_new.sort(reverse=True)
    picks = f5_new[k5.N5:k5.N5 + N5X]
    rungs = []
    for hz, kz, alpha, mz, x_val in picks:
        ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        rr = bat.build_rung_param(kz, alpha, mz, u2[:ka].copy(),
                                  mu2[:ka].copy())
        rr["mode"] = "deep-ext"
        ok = rr.get("core_ok") and "fail" not in rr
        if ok:
            rungs.append(rr)
        print("    F5X deep-ext kz %-4d h %-5d X %.3g %s [%.1f s]"
              % (kz, hz, x_val, "OK" if ok else rr.get("fail",
                                                       "FAIL"),
                 time.time() - T0), flush=True)
    cells, n_ref = bat.sweep_steps(rungs, "F5X", None, combined)
    print("    F5X census: slice [%d:%d] of the h-sorted law, %d "
          "built, %d admitted, %d step-refused"
          % (k5.N5, k5.N5 + N5X, len(rungs), len(cells), n_ref))
    check("U2 F5X deep-extension slice admitted %d cells (typed "
          "extension; NEVER gates the 151 census)" % len(cells),
          True)
    return cells


def exact_cell_data(rows):
    section("E -- exact per-cell data: moments nu_0..nu_9, certified "
            "floor, certified ceiling L, exact Radau K=4/5")
    n_ref = 0
    d_gapc = 0.0
    n_exceed = 0
    n_lbad = 0
    d_ceil = 0.0
    d_rad = 0.0
    for row in rows:
        mat = row["step"]["Mt"]
        piv, momv, blk, gersh, trace = exact_interval_data(mat)
        row["piv_fr"] = piv
        row["momv"] = momv
        hi_hint = Fraction(float(row["lam_b"])) * (
            FR1 + Fraction(1, 10 ** 6))
        c_cert = k5.cert_floor_exact(blk, FR0, hi_hint)
        if c_cert is None:
            n_ref += 1
            row["c_cert"] = None
            continue
        row["c_cert"] = c_cert
        c_f = float(c_cert)
        if c_f > row["lam_b"] * (1.0 + 1e-9):
            n_exceed += 1
        d_gapc = max(d_gapc, (row["lam_b"] - c_f)
                     / max(1.0, row["lam_b"]))
        blk_f = np.asarray(row["step"]["Bblk"], float)
        lmax_truth = float(np.linalg.eigvalsh(blk_f)[-1])
        row["lmax_truth"] = lmax_truth
        lo_hint = Fraction(float(lmax_truth)) * (
            FR1 - Fraction(1, 10 ** 6))
        l_cell = cert_ceiling_exact(blk, lo_hint,
                                    min(gersh, trace) + FR1)
        if l_cell is None:
            l_cell = min(gersh, trace) if c_cert > 0 else gersh
        row["l_fr"] = l_cell
        if float(l_cell) < lmax_truth * (1.0 - 1.0e-9):
            n_lbad += 1
        d_ceil = max(d_ceil, (float(l_cell) - lmax_truth)
                     / max(1.0, lmax_truth))
        vals = {}
        for kd in (4, 5):
            cheb = k5.chebyshev_monic(momv, kd)
            if cheb is None:
                continue
            vfr = k5.radau_exact(cheb[0], cheb[1], c_cert, momv[0])
            if vfr is None:
                continue
            vals[kd] = vfr / piv
            vf, _jac = k5.sigma_bound_source(mat, c_f, kd)
            if math.isfinite(vf):
                d_rad = max(d_rad, abs(float(vals[kd]) - vf)
                            / max(1.0, abs(vf)))
        row["rad4"] = vals.get(4)
        row["rad5"] = vals.get(5)
    check("E1 exact-rational LDL floor certified on %d/%d cells "
          "(%d REFUSED)" % (len(rows) - n_ref, len(rows), n_ref),
          n_ref == 0, kill="K2")
    check("E2 floor quality: never exceeds the float truth (%d "
          "exceed), within rel %.2e <= %.0e"
          % (n_exceed, d_gapc, FLOOR_Q_RTOL),
          n_exceed == 0 and d_gapc <= FLOOR_Q_RTOL, kill="K2")
    check("E3 exact certified ceiling: L_cell >= float "
          "lambda_max(B) on all %d cells (%d violations), quality "
          "max rel %.2e" % (len(rows), n_lbad, d_ceil),
          n_lbad == 0 and d_ceil <= FLOOR_Q_RTOL, kill="K2")
    check("E4 exact Radau tier == float route at K = 4, 5: max rel "
          "%.2e <= %.0e" % (d_rad, XR_TIE), d_rad <= XR_TIE,
          kill="K2")
    lad = [r for r in rows if r["seg"] in ("surf", "bridge", "deep")
           and r.get("rad4") is not None]
    k4max = max((float(r["rad4"]) for r in lad), default=float("nan"))
    check("G1 REPRO CCLXXVII certified K = 4 ladder bound max %.6f "
          "vs %.6f (rtol %.0e)" % (k4max, RADAU4_CERT_REF, REF_RTOL),
          SMOKE or abs(k4max / RADAU4_CERT_REF - 1.0) <= REF_RTOL,
          kill="K3")
    kz45 = [r for r in rows if r["seg"] == "F0" and r["kz"] == 45]
    kz45 = sorted(kz45, key=lambda r: -r["sigma"])[:1]
    if kz45 and kz45[0].get("rad5") is not None:
        b45 = float(kz45[0]["rad5"])
        check("G2 REPRO CCLXXIX kz-45 exact K = 5 bound %.6f vs "
              "%.6f (rtol %.0e)" % (b45, KZ45_K5_REF, REF_RTOL),
              SMOKE or abs(b45 / KZ45_K5_REF - 1.0) <= REF_RTOL,
              kill="K3")
    else:
        check("G2 REPRO CCLXXIX kz-45 exact K = 5 bound "
              "(cell absent on this subset)", SMOKE, kill="K3")
    floors = [float(r["c_cert"]) for r in rows
              if r.get("c_cert") is not None]
    print("    certified floors: %s   exact L: %s"
          % (k5.f4(floors), k5.e3([float(r["l_fr"]) for r in rows
                                   if r.get("l_fr") is not None])))


# ==================================== the two certificate tiers
def global_tier(rows):
    section("C -- THE GLOBAL TIER: one certificate per degree on "
            "the covering interval")
    ok_rows = [r for r in rows if r.get("c_cert") is not None]
    beta_g = min(r["c_cert"] for r in ok_rows)
    l_g = max(r["l_fr"] for r in ok_rows)
    print("    covering interval [%.6f, %.6f] (ratio %.3g)"
          % (float(beta_g), float(l_g), float(l_g / beta_g)))
    certs = {}
    n_ver = 0
    for deg in DEGREES:
        got = remez_candidate(float(beta_g), float(l_g), deg)
        if got is None:
            continue
        gam, err_e = got
        lifted = lift_candidate(gam, beta_g, l_g,
                                err_e if math.isfinite(err_e)
                                else 0.0)
        if lifted is None:
            continue
        a_fr, minv, lift = lifted
        cert = make_certificate("cheb-global", deg, a_fr, beta_g,
                                l_g, minv, lift)
        if cert is not None:
            certs[deg] = cert
            n_ver += 1
            print("    K = %d: E = %.3e, lift = %.3e, minT = %.3e, "
                  "hash %s [%.1f s]"
                  % (deg, err_e, float(cert["lift"]), cert["minT"],
                     cert["hash"], time.time() - T0), flush=True)
    check("C1 global certificates verified (identity exact + sympy "
          "zero residual + exact PSD) on %d/%d degrees"
          % (n_ver, len(DEGREES)), n_ver == len(DEGREES), kill="K2")
    for row in ok_rows:
        best = None
        for deg in DEGREES:
            bb = bound_from_cert(certs.get(deg), row["momv"],
                                 row["piv_fr"], row["c_cert"],
                                 row["l_fr"])
            if bb is not None and (best is None or bb < best):
                best = bb
        row["glob_fr"] = best
    gb = [float(r["glob_fr"]) for r in ok_rows
          if r.get("glob_fr") is not None]
    n_lt1 = sum(1 for r in ok_rows
                if r.get("glob_fr") is not None
                and r["glob_fr"] < SCHUR_BAR)
    n_eta = sum(1 for r in ok_rows
                if r.get("glob_fr") is not None
                and r["glob_fr"] <= FR1 - ETA_TARGET)
    check("C2 global-tier census: bound < 1 on %d/%d cells, <= "
          "1-%.3f on %d/%d; bound %s"
          % (n_lt1, len(ok_rows), float(ETA_TARGET), n_eta,
             len(ok_rows), k5.f4(gb)), True)
    return certs


def percell_tier(rows):
    section("P -- THE PER-CELL TIER: Chebyshev K = 4..8 + Radau-dual "
            "K_R = 4, 5 on each cell's own certified interval")
    n_unc = 0
    n_certs = 0
    n_fail = 0
    rb_bad = 0
    d_xf = 0.0
    tie_bad = []
    n_tie_excl = 0
    for irow, row in enumerate(rows):
        if row.get("c_cert") is None:
            n_unc += 1
            row["best_fr"] = None
            continue
        beta_fr = row["c_cert"]
        l_fr = row["l_fr"]
        mat = row["step"]["Mt"]
        # the affordable lift in the BOUND currency (source-only):
        # lift <= AFF_REL * n / nu_0  =>  penalty <= AFF_REL
        cap = (AFF_REL * float(row["piv_fr"] / row["momv"][0])
               * float(beta_fr))
        cands = []
        for deg in DEGREES:
            got = remez_candidate(float(beta_fr), float(l_fr), deg)
            if got is None:
                continue
            gam, err_e = got
            lifted = lift_candidate(gam, beta_fr, l_fr,
                                    err_e if math.isfinite(err_e)
                                    else 0.0, cap)
            if lifted is not None:
                cands.append(("cheb", deg, lifted))
        for kr in KR_SET:
            vf, jac = k5.sigma_bound_source(mat, float(beta_fr), kr)
            if jac is None or not math.isfinite(vf):
                continue
            nodes = np.linalg.eigvalsh(jac)[1:]
            nodes_fr = [fr_round(float(x), CAND_BITS) for x in nodes]
            # adaptive L-contact (A8): when the top Radau node sits
            # within DUAL_TOP of the ceiling, the contact would
            # nearly duplicate it (near-triple zero, factorization-
            # hostile) and the PURE dual is already bounded there
            top_near = nodes_fr[-1] >= DUAL_TOP * l_fr
            p_x = newton_dual_candidate(
                beta_fr, nodes_fr,
                l_contact=None if top_near else l_fr)
            if p_x is None:
                continue
            a_t = compose_poly(p_x, [(beta_fr + l_fr) / 2,
                                     (l_fr - beta_fr) / 2])
            be2 = None
            cheb = k5.chebyshev_monic(row["momv"], kr)
            if cheb is not None:
                be2 = min(float(v) for v in cheb[1])
            cands.append(("radau-dual",
                          2 * kr - (2 if top_near else 1),
                          (a_t, nodes_fr, not top_near, kr, be2)))
        best = None
        best_kind = None
        row["sosdeg"] = {}
        mid_fr = (beta_fr + l_fr) / 2
        hw_fr = (l_fr - beta_fr) / 2
        for kind, deg, pack in cands:
            if kind == "cheb":
                a_fr, minv, lift = pack[0], pack[1], pack[2]
                cert = make_certificate(kind, deg, a_fr, beta_fr,
                                        l_fr, minv, lift)
            else:
                a_t, nodes_fr, with_l = pack[0], pack[1], pack[2]
                taus_fr = [(nd - mid_fr) / hw_fr for nd in nodes_fr]
                cert = exact_dual_certificate(deg, a_t, beta_fr,
                                              l_fr, taus_fr, with_l)
            if cert is None:
                n_fail += 1
                continue
            n_certs += 1
            bb = bound_from_cert(cert, row["momv"], row["piv_fr"],
                                 beta_fr, l_fr)
            if bb is None:
                n_fail += 1
                continue
            if kind == "cheb":
                row["sosdeg"][deg] = bb
            else:
                kr, be2 = pack[3], pack[4]
                rad = row.get("rad%d" % kr)
                if rad is not None and rad > 0:
                    # domination ward: the L-contact dual must not
                    # exceed the exact Radau value (lift + node
                    # rounding are the only allowed excess)
                    rel = float(bb / rad) - 1.0
                    if be2 is not None and be2 < CANDB_DEGEN:
                        n_tie_excl += 1
                        print("      P4-EXCLUDED (near-degenerate "
                              "be^2 %.1e): %s kz %d h %.0f rel %+.1e"
                              % (be2, row["seg"], row["kz"],
                                 row["h"], rel))
                    elif rel > CANDB_TIE:
                        tie_bad.append("%s kz %d K%d %+.1e"
                                       % (row["seg"], row["kz"], kr,
                                          rel))
            if best is None or bb < best:
                best = bb
                best_kind = "%s-%d" % (kind, deg)
                row["best_cert"] = cert
        row["best_fr"] = best
        row["best_kind"] = best_kind
        if best is None:
            n_unc += 1
        else:
            # RB-analog ward: certified bound >= truth q/n
            truth = row["q_wall"] / row["n_piv"]
            if float(best) < truth - RB_TIE * max(1.0, truth):
                rb_bad += 1
            # cross route: exact bound vs float spectral evaluation
            blk_f = np.asarray(row["step"]["Bblk"], float)
            bv = np.asarray(row["step"]["bvec"], float)
            ww, vv = np.linalg.eigh(blk_f)
            wts = (vv.T @ bv) ** 2
            mid_f = float((beta_fr + l_fr) / 2)
            hw_f = float((l_fr - beta_fr) / 2)
            a_f = [float(v) for v in row["best_cert"]["a_t"]]
            pvals = np.polyval(np.asarray(a_f[::-1]),
                               (ww - mid_f) / hw_f)
            fl = float(np.sum(wts * pvals) / row["n_piv"])
            d_xf = max(d_xf, abs(float(best) - fl)
                       / max(1.0, abs(fl)))
        if (irow + 1) % 25 == 0:
            print("    ... %d/%d cells certified [%.1f s]"
                  % (irow + 1, len(rows), time.time() - T0),
                  flush=True)
    check("P1 per-cell tier: every cell carries >= 1 verified "
          "certificate (%d uncertified, %d certificates, %d "
          "refusals typed)" % (n_unc, n_certs, n_fail),
          n_unc == 0, kill="K2")
    check("P2 every consumed certificate exact-verified (identity "
          "Fraction + sympy zero residual + exact LDL PD): %d/%d"
          % (n_certs, n_certs), n_certs > 0, kill="K2")
    check("P3 RB-analog ward: certified bound >= truth q/n on every "
          "cell: %d violations (0 required)" % rb_bad,
          rb_bad == 0, kill="K2")
    check("P4 DOMINATION ward: the L-contact dual bound <= exact "
          "Radau value (excess rel <= %.0e; %d near-degenerate "
          "cells excluded, printed): %s"
          % (CANDB_TIE, n_tie_excl,
             "; ".join(tie_bad[:4]) or "all dominate"),
          not tie_bad, kill="K2")
    check("P5 exact bound == float spectral cross route: max rel "
          "%.2e <= %.0e" % (d_xf, XR_TIE), d_xf <= XR_TIE,
          kill="K2")


def print_census(rows):
    print("\n    THE SOS CLASS CENSUS (all built cells):")
    print("    idx seg    kz    h      floor      L_src      "
          "best_kind     bound_sos   rad_K5      reserve")
    for row in rows:
        if row.get("best_fr") is None:
            continue
        bf = float(row["best_fr"])
        r5 = (float(row["rad5"]) if row.get("rad5") is not None
              else float("nan"))
        print("    %3d %-6s %-4d %6.0f %10.4f %10.3e %-13s "
              "%11.6f %11.6f %10.6f"
              % (row["index"], row["seg"], row["kz"], row["h"],
                 float(row["c_cert"]), float(row["l_fr"]),
                 row["best_kind"], bf, r5, 1.0 - bf))


def eta_census(rows):
    section("T -- THE ETA TABLE + CENSUS (the 151-cell universe; "
            "extension separate)")
    uni = [r for r in rows if r["seg"] != "F5X"
           and r.get("best_fr") is not None]
    ext = [r for r in rows if r["seg"] == "F5X"
           and r.get("best_fr") is not None]
    res = [1.0 - float(r["best_fr"]) for r in uni]
    check("T1 eta table (per-cell tier, %d cells): reserve "
          "min/med/max = %s" % (len(uni), k5.f4(res)), True)
    n_eta = sum(1 for r in uni if r["best_fr"] <= FR1 - ETA_TARGET)
    n_lt1 = sum(1 for r in uni if r["best_fr"] < SCHUR_BAR)
    check("T2 census at eta = %.3f: %d/%d cells certify "
          "sum c_j nu_j <= (1-eta) n  (Schur bar < 1: %d/%d)"
          % (float(ETA_TARGET), n_eta, len(uni), n_lt1, len(uni)),
          True)
    worst = max(r["best_fr"] for r in uni)
    eta_max = FR1 - worst
    eta_trunc = Fraction(math.floor(eta_max * ETA_DEN), ETA_DEN)
    n_re = sum(1 for r in uni if r["best_fr"] <= FR1 - eta_trunc)
    check("T3 largest passing rational eta: exact 1 - %.6f, "
          "truncated (downward, 1e-6 grid) eta* = %s = %.6f; exact "
          "re-verification %d/%d"
          % (float(worst), eta_trunc, float(eta_trunc), n_re,
             len(uni)), n_re == len(uni))
    if ext:
        rese = [1.0 - float(r["best_fr"]) for r in ext]
        n_ee = sum(1 for r in ext
                   if r["best_fr"] <= FR1 - ETA_TARGET)
        check("T4 deep-extension report (separate, %d cells): "
              "reserve %s, %d/%d at eta = %.3f"
              % (len(ext), k5.f4(rese), n_ee, len(ext),
                 float(ETA_TARGET)), True)
    return uni, eta_trunc, worst


def comparison(rows):
    section("M -- THE COMPARISON: SOS route vs the Radau route at "
            "matched moment budget")
    uni = [r for r in rows if r.get("best_fr") is not None
           and r.get("rad4") is not None
           and r.get("rad5") is not None]
    pairs = ((6, "rad4", "K=4"), (8, "rad5", "K=5"))
    for deg, key, lab in pairs:
        gains = []
        n_sos = 0
        for r in uni:
            sos = r["sosdeg"].get(deg)
            if sos is None:
                continue
            rad = r[key]
            gains.append(float(rad - sos))
            if sos < rad:
                n_sos += 1
        check("M1 SOS deg %d vs exact Radau %s: SOS sharper on "
              "%d/%d cells; (Radau - SOS) %s"
              % (deg, lab, n_sos, len(gains), k5.e3(gains)), True)
    gl = [r for r in uni if r.get("glob_fr") is not None]
    n_gl_lt1 = sum(1 for r in gl if r["glob_fr"] < SCHUR_BAR)
    n_gl_eta = sum(1 for r in gl
                   if r["glob_fr"] <= FR1 - ETA_TARGET)
    n_pc_eta = sum(1 for r in uni
                   if r["best_fr"] <= FR1 - ETA_TARGET)
    verdict_g = ("the single global certificate SUFFICES"
                 if n_gl_eta == len(gl) else
                 "the single global certificate suffices for the "
                 "SCHUR bar only" if n_gl_lt1 == len(gl) else
                 "the PER-CELL tier is needed")
    check("M2 tier verdict: global <1 on %d/%d, global at eta on "
          "%d/%d, per-cell at eta on %d/%d -- %s"
          % (n_gl_lt1, len(gl), n_gl_eta, len(gl), n_pc_eta,
             len(uni), verdict_g), True)
    return verdict_g


# ================================================ X: the controls
def controls(rows, certs_glob):
    section("X -- controls-must-fire (the certification is not "
            "vacuous)")
    row = rows[0]
    # X1 construction refusal on an invalid interval (beta <= 0)
    got = remez_candidate(-0.5, 2.0, 5)
    check("X1 construction on beta <= 0 REFUSED (majorant domain "
          "must be positive)", got is None, kill="K4")
    # X2 consumption refusal: certificate interval does not cover
    # the cell's certified interval (both directions)
    deg0 = DEGREES[-1]
    cert = certs_glob.get(deg0)
    fake_floor = cert["beta"] / 2
    bb = bound_from_cert(cert, row["momv"], row["piv_fr"],
                         fake_floor, row["l_fr"])
    fake_ceil = cert["L"] * 2
    bb2 = bound_from_cert(cert, row["momv"], row["piv_fr"],
                          row["c_cert"], fake_ceil)
    check("X2 consumption REFUSED when the certificate interval "
          "does not cover the cell's certified interval (floor "
          "%.2e < cert beta %.2e: %s; ceiling %.3e > cert L %.3e: "
          "%s)" % (float(fake_floor), float(cert["beta"]),
                   "REFUSED" if bb is None else "ACCEPTED(!)",
                   float(fake_ceil), float(cert["L"]),
                   "REFUSED" if bb2 is None else "ACCEPTED(!)"),
          bb is None and bb2 is None, kill="K4")
    # X3 the UNSHIFTED best approximation is a NON-majorant and the
    # SOS stage must refuse it
    beta_g = cert["beta"]
    l_g = cert["L"]
    got = remez_candidate(float(beta_g), float(l_g), 5)
    gam, err_e = got
    tab = _cheb_mono_table(5)
    a_float = np.zeros(6)
    for j, gj in enumerate(gam):
        for i, cc in enumerate(tab[j]):
            a_float[i] += gj * cc
    a_bad = [fr_round(v, CAND_BITS) for v in a_float]
    ref = sos_certify(a_bad, beta_g, l_g, err_e)
    check("X3 SOS stage REFUSES the unshifted best approximation "
          "(a true non-majorant, E = %.3e)" % err_e, ref is None,
          kill="K4")
    # X4 the x10-coupling synthetic must FAIL the census (> 1)
    mt2 = np.array(row["step"]["Mt"], float)
    mt2[0, 1:] *= k5.CTRL_COUPLE
    mt2[1:, 0] *= k5.CTRL_COUPLE
    b2 = synth_bound(mt2, row)
    check("X4 census-can-fire: x%.0f coupling synthetic gives "
          "certified bound %.4f > 1 (exact Fraction comparison)"
          % (k5.CTRL_COUPLE,
             float(b2) if b2 is not None else float("nan")),
          b2 is not None and b2 > SCHUR_BAR, kill="K4")
    # X5 the near-1 synthetic (truth sigma = 1.2) must NOT certify
    sig0 = row["sigma"]
    scl = math.sqrt(k5.CTRL_SIG_NEAR / sig0)
    mtn = np.array(row["step"]["Mt"], float)
    mtn = 0.5 * (mtn + mtn.T)
    mtn[0, 1:] *= scl
    mtn[1:, 0] *= scl
    sign = (scl ** 2) * row["q_wall"] / row["n_piv"]
    bn = synth_bound(mtn, row)
    check("X5 SIGMA>1 control: truth sigma %.4f > 1 gives certified "
          "bound %.4f > 1 -> NOT certified"
          % (sign, float(bn) if bn is not None else float("nan")),
          sign > 1.0 and bn is not None and bn > SCHUR_BAR,
          kill="K4")
    # X6 exact sanity: synthetic diagonal measure with known q
    dvals = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
             FR1, Fraction(3, 2), Fraction(2), Fraction(3)]
    momv = [sum(dv ** k for dv in dvals) for k in range(9)]
    q_true = sum(FR1 / dv for dv in dvals)
    beta_s, l_s = Fraction(1, 4), Fraction(4)
    got = remez_candidate(float(beta_s), float(l_s), 6)
    gam, err_e = got
    lifted = lift_candidate(gam, beta_s, l_s, err_e)
    a_fr, minv, lift = lifted
    cert_s = make_certificate("cheb", 6, a_fr, beta_s, l_s, minv,
                              lift)
    bs = bound_from_cert(cert_s, momv, FR1, Fraction(1, 3),
                         Fraction(3))
    check("X6 exact sanity on the synthetic diagonal measure: "
          "certified linear bound %.6f >= q = %.6f (EXACT Fraction "
          "comparison)"
          % (float(bs) if bs is not None else float("nan"),
             float(q_true)),
          cert_s is not None and bs is not None and bs >= q_true,
          kill="K4")


def synth_bound(mt_synth, row_ref):
    """Full per-cell pipeline on a synthetic matrix (controls)."""
    piv, momv, blk, gersh, trace = exact_interval_data(mt_synth)
    hi_hint = Fraction(float(row_ref["lam_b"])) * (
        FR1 + Fraction(1, 10 ** 6))
    c_cert = k5.cert_floor_exact(blk, FR0, hi_hint)
    if c_cert is None:
        return None
    l_cell = min(gersh, trace)
    got = remez_candidate(float(c_cert), float(l_cell), 8)
    if got is None:
        return None
    gam, err_e = got
    lifted = lift_candidate(gam, c_cert, l_cell,
                            err_e if math.isfinite(err_e) else 0.0)
    if lifted is None:
        return None
    a_fr, minv, lift = lifted
    cert = make_certificate("cheb-ctrl", 8, a_fr, c_cert, l_cell,
                            minv, lift)
    return bound_from_cert(cert, momv, piv, c_cert, l_cell)


# ================================================ S: the screens
def screens(rows):
    section("S -- relocation screens (CCXLVII bars verbatim): are "
            "the eta margins tau or c_h in disguise?")
    ok_rows = [r for r in rows if r.get("best_fr") is not None]
    taus = np.asarray([r["tau_scale"] for r in ok_rows], float)
    ch_map = k5.ch_surface_map(ok_rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in ok_rows], float)
    bnd = np.asarray([float(r["best_fr"]) for r in ok_rows], float)
    series = (("1 - bound (the Schur margin)", 1.0 - bnd),
              ("(1-eta_target) - bound (the reserve margin)",
               float(FR1 - ETA_TARGET) - bnd))
    reloc = []
    for label, arr in series:
        pos = arr > 0
        t1, v1 = k5.screen(arr[pos], taus[pos], "%s vs tau" % label)
        mask = pos & np.isfinite(chs)
        t2, v2 = k5.screen(arr[mask], chs[mask],
                           "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau / c_h relocation screens on the eta margins: "
          "relocation seats %s" % (",".join(reloc) or "none"),
          not reloc)
    hs = np.asarray([r["h"] for r in ok_rows], float)
    pos = (1.0 - bnd) > 0
    if int(np.sum(pos)) >= 3:
        slope, two_se, r2, _a = k5.linfit(np.log(hs[pos]),
                                          np.log(1.0 - bnd[pos]))
        print("    h-law of the reserve: log-log slope %+.4f +/- "
              "%.4f (2SE), R^2 %.3f" % (slope, two_se, r2))


# ============================================ the proof object
def write_proof(certs_glob, uni, eta_trunc, worst):
    worst_row = max(uni, key=lambda r: r["best_fr"])
    ex = worst_row.get("best_cert")

    def cert_json(cc):
        return dict(kind=cc["kind"], deg=cc["deg"],
                    beta=str(cc["beta"]), L=str(cc["L"]),
                    p_coeffs_x=[str(v) for v in cc["c_x"]],
                    G0=[[str(v) for v in row] for row in cc["G0"]],
                    G1=[[str(v) for v in row] for row in cc["G1"]],
                    lift=str(cc["lift"]), hash=cc["hash"])

    blob = dict(
        schema="tfpt.radau_sos_certificate.v1",
        spec_sha=SPEC_SHA,
        statement=("for every measure with moments nu and support "
                   "in [beta, L]: sum_j c_j nu_j <= (1-eta) n "
                   "implies sigma <= 1-eta implies M positive "
                   "definite (Schur); every step exact-rational"),
        eta_target=str(ETA_TARGET),
        eta_star=str(eta_trunc),
        worst_bound=str(worst),
        census_cells=len(uni),
        global_certificates={str(k): cert_json(v)
                             for k, v in certs_glob.items()},
        worst_cell_exhibit=dict(
            seg=worst_row["seg"], kz=int(worst_row["kz"]),
            h=float(worst_row["h"]),
            certificate=cert_json(ex) if ex else None),
    )
    with open(PROOF_JSON, "w", encoding="utf-8") as fh:
        json.dump(blob, fh, indent=1)
    fsha = hashlib.sha256(
        open(PROOF_JSON, "rb").read()).hexdigest()[:16]
    print("    proof object written: %s (sha %s)"
          % (os.path.basename(PROOF_JSON), fsha))
    return fsha


# =============================================================== main
def finish(rows, eta_trunc, worst, verdict_g):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    uni = [r for r in rows if r["seg"] != "F5X"]
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not rows:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        miss = [r for r in uni if r.get("best_fr") is None
                or r["best_fr"] >= SCHUR_BAR]
        n_eta = sum(1 for r in uni if r.get("best_fr") is not None
                    and r["best_fr"] <= FR1 - ETA_TARGET)
        if not miss and n_eta == len(uni):
            v = ("SOS-CLASS-COMPOSED(%d/%d cells certified "
                 "sum c_j nu_j <= (1 - %.3f) n by the per-cell "
                 "tier; worst bound %.6f; largest passing rational "
                 "eta* = %s; global tier: %s)"
                 % (n_eta, len(uni), float(ETA_TARGET),
                    float(worst) if worst is not None
                    else float("nan"),
                    eta_trunc, verdict_g))
        elif not miss:
            v = ("SOS-CLASS-SCHUR(%d/%d cells < 1, but the 0.273 "
                 "reserve fails on %d cells)"
                 % (len(uni), len(uni), len(uni) - n_eta))
        else:
            v = ("SOS-CLASS-PARTIAL(%d cells uncertified or >= 1: "
                 "%s)" % (len(miss),
                          "; ".join("%s kz %d" % (r["seg"], r["kz"])
                                    for r in miss[:4])))
        print("\n  VERDICT: %s" % v)
        print("""
  THE ONE-LINE THEOREM (per verified certificate (beta, L, p, G0,
  G1), every step exact-rational): for every measure with moments
  nu and support in [beta, L]: sum_j c_j nu_j <= (1 - eta) n
  implies sigma = q/n <= 1 - eta implies M positive definite --
  because x p(x) - 1 = s_0(x) + (x - beta)(L - x) s_1(x) with PSD
  rational Grams gives p(x) >= 1/x on [beta, L] by inspection, so
  q = int x^{-1} dmu <= int p dmu = sum_j c_j nu_j, and Schur (E2)
  closes with s = n - q >= eta n > 0.
  PEDIGREES, honestly typed: the floors and moments are exact
  dyadic rationals of the ASSEMBLED float64 wall matrices (A6: the
  float64-vs-ideal enclosure stays with the pg_chain program); L is
  the exact-rational CERTIFIED CEILING (round-62 LDL mirrored at
  the top edge, A2); the candidate search is float and free, the
  consumed object is only the verified certificate (A3).  THE HONEST OPEN RESIDUE: cells not
  yet built (the h > 1450 flank and the CCLXXXVII deep-membership
  lane, cited by key only); the all-h / class-level membership
  question.  SCOPE: the built wall-legal cells; NEVER an all-h
  statement; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.RADAU.SOS.01 -- the rational dual "
            "certificate (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))
    print("    bars: eta target %.3f, degrees %s, Radau-dual K_R "
          "%s, RND_BITS %d" % (float(ETA_TARGET), DEGREES, KR_SET,
                               RND_BITS))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(CONSUME_FUNCS, CONSUME_BANNED)
    check("S0.2 AC consumed-certificate path: moments, floors, "
          "interval endpoints and rational algebra only",
          not ac1, ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(CAND_FUNCS, CAND_BANNED)
    check("S0.3 AC candidate-search functions carry no truth read "
          "(search is free by design, A3)", not ac2,
          ",".join(sorted(set(ac2))), kill="K2")

    _zones, steps, census, combined = k5.build_ladder()
    if KILLS:
        return finish([], None, None, "")
    k5.artifact_key_ward(steps)
    f0_cells = k5.build_f0(combined)
    if KILLS:
        return finish([], None, None, "")
    families = k5.build_families(census, combined)
    if KILLS:
        return finish([], None, None, "")
    n_sweep = len(f0_cells) + sum(len(v) for v in families.values())
    n_cells = len(steps) + n_sweep
    check("U1 wall-legal universe: %d ladder + %d sweep = %d cells "
          "(CCLXXIX frozen expectation %d)"
          % (len(steps), n_sweep, n_cells, CELL_EXP),
          SMOKE or n_cells == CELL_EXP, kill="K3")
    f5x_cells = build_f5x(combined)
    rows = k5.make_rows(steps, f0_cells, families)
    for dd in f5x_cells:
        st = dd["step"]
        rows.append(dict(step=st, seg="F5X",
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         mode=dd.get("mode", "deep-ext")))
    for i, r in enumerate(rows):
        r["index"] = i
    rows = k5.jacobi_identity_wards(rows)
    if KILLS:
        return finish(rows, None, None, "")
    k5.pivot_ward(rows)
    k5.repro_anchors([r for r in rows if r["seg"] != "F5X"])
    if KILLS:
        return finish(rows, None, None, "")

    exact_cell_data(rows)
    if KILLS:
        return finish(rows, None, None, "")
    certs_glob = global_tier(rows)
    if KILLS:
        return finish(rows, None, None, "")
    percell_tier(rows)
    if KILLS:
        return finish(rows, None, None, "")
    print_census(rows)
    uni, eta_trunc, worst = eta_census(rows)
    verdict_g = comparison(rows)
    controls(rows, certs_glob)
    screens(rows)
    if not SMOKE and not KILLS and uni:
        write_proof(certs_glob, uni, eta_trunc, worst)
    return finish(rows, eta_trunc, worst, verdict_g)


if __name__ == "__main__":
    sys.exit(main())
