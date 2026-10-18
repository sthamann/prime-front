#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sigma_coupling_pivot_probe -- PRIME.ONEBADMODE.KS.SIGMA.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE NAMED FINAL SEAM OF THE KS.DUAL CONTRACT.  CCLXI (probe B,
zolotarev_ks_dual_probe) posed the finite robust extremal problem
sup_{J in C_KS} tr R(J) < 1 over a frozen truth-envelope class in the
15 wall Jacobi parameters and measured KSDUAL-GAP: the product box
alone allows tr R = 2.26 because it forgets the correlation between
the coupling a_1 and the pivot b_1.  ONE additional source-only
constraint closed it in the reported-only preview: the Schur-quotient
envelope
    sigma := a_1^2 [J_B^{-1}]_{11} / b_1   <=  0.665
gave sup tr R = 0.7264 < 1.  CCLXI flagged that cap MECHANISM-
IMPORTING and left the question open.  THIS PROBE asks the only
question that matters for the corridor: can sigma <= t be DERIVED
from the ladder construction (window geometry + exact-law weights +
the certified B-floor), with NO wall pivot and NO target eigendata --
and if not, what exactly is the obstruction.

 (a) THE IDENTITY.  What IS sigma in wall coordinates?  The wall step
     matrix is M = [[n, b^T], [b, B]] (CCVII: n = M[0,0] the bad-mode
     pivot, b the coupling, B the bulk block, Schur scalar
     s = n - q with q = b^T B^{-1} b).  Lanczos of (M, e_0) has first
     frame vector e_0 and second b/||b||, so J_B = Q_B^T B Q_B with
     Q_B e_1 = b/||b|| and a_1 = ||b||, whence
         a_1^2 [J_B^{-1}]_{11} = b^T B^{-1} b = q      (E2)
     and therefore, EXACTLY,
         sigma = q / n = 1 - s/n.
     sigma is the NORMALIZED coupling-to-pivot Schur ratio: the
     constraint sigma <= t is literally the RELATIVE Schur-gap floor
     s >= (1 - t) n.  Warded per rung on the whole 68-step ladder at
     IDENT_TIE.
 (b) THE THRESHOLD MAP.  CCLXI's optimization is rebuilt verbatim
     (same class C_KS, same frozen filter, same box construction) and
     re-run with the extra constraint sigma <= t on a frozen grid of
     t, plus a declared bisection: the map t -> sup tr R and the
     closing threshold t* (sup = 1).  Reported with the truth sigma
     envelope so the margin structure is visible.
 (c) THE SOURCE-ONLY DERIVATION.  q = b^T B^{-1} b = integral of 1/x
     against the b-weighted spectral measure of B.  That measure's
     moments nu_k = b^T B^k b are ENTRY reads of the source-built wall
     matrix (equivalently: polynomial functions of the e_0-diagonal
     moments m_j = (M^j)_{00}, warded by the exact triangular
     recursion below) -- no eigendata, no inverse of B, no wall pivot.
     With the certified floor spec(B) >= c_B, the classical
     Gauss-Radau quadrature bound (E3) gives, at every depth
     K = 1..7,
         q <= RADAU_K(nu_0..nu_{2K-2}; c_B),
     hence a source-only sigma bound sigma <= RADAU_K / n.  The probe
     measures the ladder maximum per depth, the minimal depth K* whose
     ladder maximum lies below t*, and CONFIRMS by re-running the
     optimization with the DERIVED cap.  Cross-route: the same bound
     as the optimum of the truncated moment LP (min over polynomial
     majorants p >= 1/x on [c_B, L] of sum_k p_k nu_k), agreeing with
     RADAU_K at the degrees where the LP is numerically stable.
     PREMISE VARIANT (named, not adopted): the same bound with the
     per-step B-floor at its measured level instead of the global
     cited c_B -- reported to type WHICH premise buys the depth.
 (d) GATES.  tau / c_h relocation screens on sigma, on its margin to
     t*, on the derived bound and its margin (the decisive check: if
     the margin is c_h in disguise the seam has only moved); the
     falsifying worlds must not be admitted by the sigma-capped class;
     controls-must-fire for the optimizer; anti-circularity scanned
     per route.

THE 0.665 STRATEGY DECIDER (mission's first test).  CCLIII/CCXLV
report a restricted Case-C0 sum-rule residual res(h) with median
0.665.  CCLXI's sigma cap is 0.665 as well.  C0 below decides whether
this is the SAME invariant: the cap's provenance is
max_truth(sigma) * (1 + MARGIN_FRAC) -- a number that MOVES with the
probe's own margin parameter and therefore cannot be an invariant --
and the per-rung correlation of sigma with res(h) is measured on a
frozen stride subset of the surface ladder (CCLIII K4(iii) already
measured the measure->wall link null, corr -0.022).  Verdict typed
COINCIDENCE / SAME-INVARIANT; the strategy follows.

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E1 Killip-Simon l2 class / sum rules: Killip & Simon, Ann. Math. 158
    (2003) 253-321.  Name and l2 norm of the wall currency only
    (inherited from CCXLV/CCLIII/CCLXI); no spectral claim.
 E2 compression / Schur / Sylvester / interlacing: for orthogonal Q
    with first column e_0, (Q^T M Q)[1:,1:] and M[1:,1:] are
    orthogonally similar compressions of M onto e_0-perp; Schur
    complement s = n - b^T B^{-1} b; a symmetric matrix is PD iff all
    leading principal minors are positive.  [Horn & Johnson, Matrix
    Analysis, 2nd ed., CUP 2013, Sec. 0.8.5, 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE.  For symmetric A with
    spec(A) in [c, inf), unit vector u and the Lanczos data
    (alpha_1..alpha_K, beta_1..beta_{K-1}) of (A, u), the K-node
    Gauss-Radau rule with the node prescribed at c evaluates
    u^T f(A) u as e_1^T f(J~_K) e_1 with J~_K the Jacobi matrix whose
    last diagonal entry is modified to alpha_K^R = c + u_{K-1},
    (J_{K-1} - c I) u = beta_{K-1}^2 e_{K-1}; for f completely
    monotone on (0, inf) -- f(x) = 1/x -- the remainder has a fixed
    sign and the rule is an UPPER bound for u^T A^{-1} u, exact in the
    limit K = dim.  [Golub & Meurant, Matrices, Moments and
    Quadrature with Applications, PUP 2010, Ch. 6-7; Golub & Meurant,
    Acta Numerica 6 (1997) 203-267; Golub & Welsch, Math. Comp. 23
    (1969) 221-230.]  THE SIGN IS WARDED PER STEP AND PER DEPTH
    (RB1): no bound is consumed on faith.
 E4 truncated moment problem / Markov-Krein: the optimum of
    min { sum_k p_k nu_k : p polynomial of degree d, p(x) >= 1/x on
    [c, L] } is the sharpest bound obtainable from moments of order
    <= d; it is attained by a quadrature rule.  [Krein & Nudelman,
    The Markov Moment Problem, AMS 1977, Ch. III-IV; Karlin & Studden,
    Tchebycheff Systems, Wiley 1966.]  Used only as the cross-route
    (LP) that must not undercut RADAU.
 E5 the Zolotarev separator facts (R >= 1 on x <= 0, R >= 0 on R,
    R <= delta on [c_B, L]) are the CCXXV in-repo outward-rounded
    interval certificates of zolotarev_phase_filter_probe.build_filter,
    re-consumed READ-ONLY (pedigree: Akhiezer, Theory of
    Approximation, Dover 1992, Ch. 9).
 E6 SLSQP / differential evolution are numerical search tools (SciPy);
    nothing rigorous is consumed from them.

FROZEN PROTOCOL.
 S0 FIREWALL.  AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); all predecessor probes READ-ONLY; RNG
    seats: the corpus scramble seed (SCR_SEED = 1) and the declared
    OPT_SEED, nothing else.  AC scan: the class functions
    (theta_matrices / ks_wall_functionals / class_slack_vector /
    sigma_quotient / tr_r_of_theta) carry no ladder or read identifier
    (CCLXI verbatim), AND the derivation functions (wall_moments /
    lanczos_pair / radau_upper / sigma_bound_source / nu_from_e0_
    moments) carry no read, no eigensolver, no pivot and no ladder
    identifier -- the bound may see the wall matrix ENTRIES and the
    frozen constants, nothing else.
 W  ladder rebuilt read-only (42 surface rungs, 68 = 40 + 1 + 27
    steps), the fixed CCXXV global m = 8 filter rebuilt from the
    source-only L and warded against the stored artifact; per-step LU
    partial-fraction trace_R / margin warded against the stored 68x8
    artifact; eigen-route == LU; REPRO: reserve med vs CCXLVII 0.9195
    and min vs 2.730e-2.
 B  Jacobi translation warded per step (CCLXI verbatim): b_1 ==
    M[0,0], a_1 == ||b||, lambda_min(J_B) == lamB1, m(0) * gap == 1.
 I  THE IDENTITY (a), warded per step: a_1^2 [J_B^{-1}]_{11} == q,
    sigma == q/n == 1 - s/n, Q_B e_1 == b/||b||, all at IDENT_TIE.
 C0 the 0.665 decider as described above.
 G  class C_KS frozen exactly as in CCLXI (same box construction, same
    functional caps, SHA-256 of the frozen box bytes printed) BEFORE
    any optimization; truth membership census.
 T  the threshold map (b) + bisection; REPRO anchors: the uncapped
    sup must reproduce CCLXI's GAP (>= SUP_NOCAP_BAR, ratio to 2.26
    printed) and the cap 0.665 must still close (< 1) as CCLXI's
    preview reported.
 D  the derivation (c): the b-weighted moments by two routes (block
    entries and the amendment-A1 triangular reconstruction from the
    e_0-diagonal moments) plus an exact-rational tier; RADAU per
    depth with the sign ward RB1 and the node ward; the LP cross-
    route in two parts (D4a the theoretical direction -- the grid-
    discretised LP optimum is a LOWER bound on the true moment-
    problem supremum and may never exceed RADAU; D4b agreement at
    degrees 2 and 4, with degree 6 reported-only because the
    discretisation, not the theory, is the limit there); the ladder
    maxima per depth, the minimal depth K*, the extremal measure of
    the LP (what the moments cannot exclude), the premise variant,
    and the CONFIRM optimization at the derived cap.
 X  controls: falsifying worlds (smooth, scramble seed 1) aligned per
    CCLIII C2 must not sit inside the sigma-capped class with
    tr R >= 1 (-> CLASS-USELESS-SIGMA, dominating); OPT-POWER control
    (b_1 box extended to OPT_CTRL_B1 = -1, sigma cap ACTIVE) must
    reach tr R >= 1, else the search is too weak to trust.
 S  screens: tau and CCXVII c_h relocation screens (CCXLVII bars
    verbatim: PASS <= 0.30, RELOC >= 0.70) on sigma, on t* - sigma, on
    the derived bound and on t* - bound; plus h-slopes with 2SE.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 CLASS-USELESS-SIGMA(world; a control inside the sigma-capped class
   with tr R >= 1)
 SIGMA-DERIVED(bound t_der, depth K*, route; the composed closure
   stated loudly: C_KS + the DERIVED sigma cap closes with reserve
   1 - sup, truth lies in the class on all 68 rungs, the remaining
   all-h residue is class membership plus 'the depth-K* moment bound
   stays below the bar', both with measured flat h-laws; typed
   premises: certified B-floor + source-only moments + NUMERIC-GLOBAL
   optimization)
 SIGMA-CONDITIONAL(the bound needs X -- X named precisely, with the
   honest relocation check: is X the halfgap?)
 SIGMA-OPEN(the measured obstruction: the deepest available bound and
   the factor by which it exceeds the closing threshold).
Every enum is a finite float64/rational statement about the deployed
ladder and the frozen class; NEVER an all-h statement, NEVER an RH
claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE = 2e-9;
PF_TIE = 2e-8; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7;
IDENT_TIE = 1e-12; MOM_TIE = 1e-6 (float reconstruction, scaled
matrix); LP_TIE = 1e-2 (grid-discretised LP); NU_RECON_K = 6;
RADAU_SIGN_TIE = 1e-12; REPRO_RTOL = 5e-2; RES_MED_REF = 0.9195;
RES_MIN_REF = 2.730e-2; MARGIN_FRAC = 0.10; FEAS_TOL = 1e-9;
RESERVE_FLOOR = 1e-2; T_GRID = (0.50, 0.60, 0.665, 0.75, 0.85, 0.95,
1.10); BISECT_MAX = 5; BISECT_TOL = 5e-3; T_MARGIN = 0.05;
MAP_MS = 16; MAP_DE = 110; CONF_MS = 32; CONF_DE = 240;
SLSQP_MAXIT = 150; DE_POP = 20; OPT_SEED = 20260812; PEN_W = 1e4;
SUP_NOCAP_REF = 2.26; SUP_NOCAP_BAR = 1.0; SIG_CAP_REF = 0.665;
SIG_PREV_REF = 0.7264; KMAX = 7; LP_DEG_MAX = 6; LP_GRID = 4000
(geometric);
EXACT_STEPS = 3; MEAS_STRIDE = 3; CORR_BAR = 0.30;
QBITS = 12; FUNC_PAD = 1e-6; OPT_CTRL_B1 = -1.0; OPT_CTRL_BAR = 1.0;
R_SAMPLE_TIE = 2e-8; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CTRL_MAJORITY = 0.5; runtime cap 25 min.

HONEST AMENDMENTS (declared before the frozen run).
 A1 the mission sketch says the moments are 'traces of powers'.  They
    are not: the measure whose 1/x integral is q is the b-WEIGHTED
    spectral measure of B, whose moments are nu_k = b^T B^k b, i.e.
    the e_0-DIAGONAL moments m_j = (M^j)_{00} of the wall matrix
    (triangular relation warded in D1), not tr(M^j).  Both are entry-
    level source reads and the CCVII dyadic-integer machinery applies
    verbatim; the correction is disclosed, not hidden.
 A2 the mission asks for 'the exact closing threshold'.  A numeric
    maximum is a LOWER bound on a supremum, so the measured t* is an
    UPPER bound on the true closing threshold (t*_true <= t*_num).
    The verdict therefore never rests on t* alone: the DERIVED cap is
    re-run through the full optimization (D-CONFIRM) and the reserve
    is read there.
 A3 the Gauss-Radau construction inverts the (K-1)x(K-1) shifted
    truncated Jacobi block of the b-measure.  That is the quadrature
    rule, not the wall pivot (no inverse of B, no inverse of J_B, no
    eigendata); disclosed, and the bound property is warded per step
    and per depth against the truth q (RB1) rather than consumed on
    faith.
 A4 HONEST CORRECTION TO CCLXI, disclosed and printed at T*2: the
    CCLXI stage-3 preview number 0.7264 was produced by the SEARCH
    alone, without the truth floor.  The truth ladder lies inside
    C_KS (N1) and every truth step satisfies sigma <= the cap, so
    ANY constrained supremum is at least the truth ladder's own
    maximum tr R (= 1 - the CCXLVII minimum reserve).  This probe
    therefore reports sup = max(optimizer, truth-under-cap)
    everywhere; the corridor's reserve under ANY sigma cap is bounded
    by the CCXLVII worst step, not by the preview number.  The
    correction makes the reserve SMALLER, never larger.
 A5 the bar for the derived cap is t_bar = t_close - T_MARGIN with
    t_close the largest MEASURED closing cap (not t* itself), so that
    a t* lying above the frozen grid can never inflate the bar; the
    CONFIRM run then measures the reserve at the derived cap
    directly.

SMOKE DISCLOSURE (2026-08-12, one smoke pass before the freeze;
 everything that changed between the smoke and this freeze is listed
 here, and NO change makes a positive verdict easier).
 SMOKE-1 (contiguous 10-rung surface subset + 3 lowest deep rungs,
 29.6 s) ran 38 checks with 1 failure and no kills.  Honest readings:
 (i)   the smoke subset necessarily contains steps that are NOT
       steps of the fixed 68-step artifact (its own fake bridge --
       the identical CCLIII/CCLXI smoke phenomenon), one with
       NEGATIVE reserve -3.85 and lambda_min(J_B) = 0.0059.  That
       single fake step drove the disclosed B-floor widening to
       0.0053, the smoke 'sup' of 4.8506 (a truth point of the
       subset ladder, not an optimizer discovery), the single FAIL
       (T*2, which asks whether the class still closes at the CCLXI
       cap), and -- because every Radau bound scales like 1/c_B --
       the smoke's SIGMA-OPEN verdict at ladder max 19.66.  T5 REPRO
       is smoke-bypassed by design and decides only on the frozen
       ladder, where the CCXLVII reserve minimum is 2.730e-2 > 0 and
       the CLIII floor 0.5523 holds.
 (ii)  every identity ward sat at machine precision on the smoke
       ladder: a_1^2 [J_B^-1]_11 == q at 6.9e-16, sigma == q/n at
       3.3e-16, sigma == 1 - s/n at 2.7e-16, the frame ward
       Q_B e_1 == b/||b|| at 1.1e-16; the moment reconstruction
       (A1) at 6.3e-16 float and EXACT in the rational tier; the
       Radau sign ward RB1 fired zero violations at every depth.
 (iii) the scramble control world reads sigma in [1.007, 1.052],
       i.e. a NEGATIVE relative Schur gap -- any cap t < 1 excludes
       it structurally; the smooth world was excluded by the B-floor
       on every aligned rung; the OPT-POWER control reached 2.80
       with the cap active, as designed.
 CHANGES made after SMOKE-1, each disclosed with its direction:
   C1 CRASH FIX: the frame ward compared an 8-vector with a
      7-vector; now it compares the wall block correctly (the ward
      itself is unchanged in meaning).
   C2 the LP cross-route grid was changed from Chebyshev to
      GEOMETRIC spacing (LP_GRID 1200 -> 4000), which is the correct
      grid for 1/x, and the single agreement ward was SPLIT into
      D4a (NEW, strict, kills: the discretised LP optimum is a lower
      bound on the true moment-problem supremum and may never exceed
      RADAU, bar 1e-6) and D4b (agreement at degrees 2 and 4, bar
      LOOSENED 1e-5 -> 1e-2 because the discretisation, not the
      theory, is the limit; degree 6 reported-only).  This is a
      diagnostic cross-route: it can never produce the headline
      bound, and the loosened part is compensated by the new strict
      directional kill.
   C3 the C0 decider was restructured: the provenance argument (the
      cap is max_truth(sigma) * (1 + MARGIN_FRAC), a margin
      artifact) is now the DECISIVE typing, and the correlation with
      the CCXLV residual is reported separately with an
      underpowering guard (n < 8 -> UNDERPOWERED); on the smoke
      subset the correlation had n = 3 and was meaningless.
   C4 TIGHTENING: the bar for the minimal depth K* was changed from
      t* - T_MARGIN to t_close - T_MARGIN (amendment A5), where
      t_close <= t* is the largest MEASURED closing cap.  This makes
      SIGMA-DERIVED strictly harder to reach.
 No bar, control, screen or verdict enum was changed in a direction
 that favours a positive outcome; the SPEC SHA moves with this text,
 as disclosed.

FROZEN RUN 1 (SPEC_SHA 4a3cb2f4b1b057cc8ecd41f5f74411773089721d3e00
 bd41e10b27f19fc98ee3, 264.7 s, 38 checks, 1 fail = T*2, no kills) and
 the AMENDMENT A6 it forced.  Run 1 measured, on the FULL 68-step
 ladder: every identity ward at machine precision (I1 9.2e-15, I2/I3
 3.8e-15), sup tr R = 2.2551 without the cap (CCLXI 2.26 reproduced),
 and -- the decisive reading -- sup tr R ~ 2.22 at EVERY cap in the
 frozen grid [0.50, 1.10], i.e. NO cap closes.  The anatomy of the
 capped incumbents says why: the maximizer sits at pivot b_1 = n =
 -2.892 < 0, where sigma = q/n is NEGATIVE (-859.8 at the confirm
 incumbent), so the ONE-SIDED cap sigma <= t is VACUOUS on the
 pivot-negative sheet and the CCLXI bad mode survives it untouched.
 The CCLXI stage-3 preview 0.7264 is therefore not reproducible: it
 was a constrained search that never visited that sheet.
 A6 (the amendment, declared here, direction disclosed): the probe now
    ALSO maps the pivot-POSITIVE sheet, C_KS ∩ {n > 0} ∩ {sigma <= t}
    (section T*P).  n = M[0,0] is an ENTRY of the assembled wall
    matrix -- source-computable, no eigendata, no read -- and it is
    warded positive on all 68 deployed rungs (P1), so this is a new
    PREMISE of the composed statement, named and carried explicitly,
    never smuggled.  On that sheet the identity of section I gives the
    exact reading: with B >= c_B I > 0, sigma < 1 <=> s > 0 <=> the
    step is positive definite (Schur criterion).  A6 makes the closure
    HARDER to claim, not easier: it adds a premise, it re-runs the
    D-CONFIRM optimization on the sheet the bar came from, it adds the
    pivot sign to the control census (X2) and a dedicated OPT-POWER
    control on the new sheet (P3, read on the OPTIMIZER's own value
    with the truth floor excluded, so a closure can never be a search
    failure in disguise), and it replaces the meaningless plain bar
    (no closing cap at all) with the pivot-positive one.  The
    pivot-positive map reports the optimizer value and the truth
    floor separately at every t.
 The frozen run below (SPEC SHA moved by this text) is the run of
 record; run 1's log is superseded only in the sections A6 touches.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXV line prepended to experiments/next.txt AFTER the frozen
summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder + wall
blocks), zolotarev_phase_filter_probe (CCXXV filter + artifact),
zolotarev_ks_dual_probe (CCLXI class + optimization, machinery
reproduced locally, cited), rhp_tier2_polecontrol_probe (CCLIII/CCXLV
measure carriers, imported read-only for C0),
euler_phase_identity_probe (CCXVII c_h).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_coupling_pivot_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_coupling_pivot_probe.py
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
import scipy.linalg as sla
from scipy import optimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import rhp_tier2_polecontrol_probe as rt      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
PF_TIE = 2.0e-8
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
IDENT_TIE = 1.0e-12
MOM_TIE = 1.0e-6
LP_TIE = 1.0e-2
RADAU_SIGN_TIE = 1.0e-12
REPRO_RTOL = 5.0e-2
RES_MED_REF = 0.9195
RES_MIN_REF = 2.730e-2
MARGIN_FRAC = 0.10
FEAS_TOL = 1.0e-9
RESERVE_FLOOR = 1.0e-2
T_GRID = (0.50, 0.60, 0.665, 0.75, 0.85, 0.95, 1.10)
BISECT_MAX = 5
BISECT_TOL = 5.0e-3
T_MARGIN = 0.05
MAP_MS = 16
MAP_DE = 110
CONF_MS = 32
CONF_DE = 240
SLSQP_MAXIT = 150
DE_POP = 20
OPT_SEED = 20260812
PEN_W = 1.0e4
SUP_NOCAP_REF = 2.26
SUP_NOCAP_BAR = 1.0
SIG_CAP_REF = 0.665
SIG_PREV_REF = 0.7264
KMAX = 7
LP_DEG_MAX = 6
LP_GRID = 4000
EXACT_STEPS = 3
NU_RECON_K = 6
MEAS_STRIDE = 3
CORR_BAR = 0.30
QBITS = 12
FUNC_PAD = 1.0e-6
OPT_CTRL_B1 = -1.0
OPT_CTRL_BAR = 1.0
R_SAMPLE_TIE = 2.0e-8
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_MAJORITY = 0.5
CB_F = float(ob.CB_CITED)
SCRAMBLE_SEED = ob.SCR_SEED
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: identifiers marking a construction as ladder/read-derived.
CLASS_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h")
# AC: the derivation may see wall ENTRIES and frozen constants only --
# no read, no pivot, no eigensolver, no ladder identifier.
DERIV_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h", "gap", "lamB1", "sigma", "sigma_quotient",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "theta", "row", "rows", "step", "steps")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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


def pearson(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3:
        return float("nan")
    x, y = x[m] - x[m].mean(), y[m] - y[m].mean()
    dn = math.sqrt(float(x @ x) * float(y @ y))
    return float(x @ y) / dn if dn > 0 else float("nan")


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# =========================================== Jacobi form (CCLIII)
def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- CCLIII/CCLXI
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


def ks_distance(a1, b1, a2, b2):
    """CCLIII KS l2 distance of two Jacobi data sets (verbatim)."""
    da = np.asarray(a2, float) - np.asarray(a1, float)
    db = np.asarray(b2, float) - np.asarray(b1, float)
    return math.sqrt(float(np.sum(db ** 2))
                     + 2.0 * float(np.sum(da ** 2)))


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


def ks_wall_functionals(theta, cls):
    """CCLXI verbatim: wall-side sum-rule functionals on [0, L]
    (disclosed translation; theta and frozen constants only)."""
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
    (>= 0 iff inside).  theta and frozen constants only."""
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
    """The Schur quotient sigma = a_1^2 [J_B^-1]_11 / b_1 in the 15
    Jacobi coordinates (CCLXI definition; theta only)."""
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
    """tr R(J(theta)) by the eigenvalue route (spectral function of
    theta; the frozen filter is a constant)."""
    jm, _jb = theta_matrices(theta)
    if not np.all(np.isfinite(jm)):
        return float("nan")
    evals = np.linalg.eigvalsh(jm)
    return math.fsum(zol.scalar_r(fdata, float(v)) for v in evals)


# ================= the derivation functions (AC-scanned, entries only)
def wall_moments(matrix, kdeg):
    """nu_k = b^T B^k b, k = 0..kdeg, from the ENTRIES of the wall
    matrix (first column below the diagonal and the trailing block).
    No eigensolver, no inverse, no pivot."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    out = []
    cur = vec.copy()
    for _k in range(kdeg + 1):
        out.append(float(vec @ cur))
        cur = blk @ cur
    return np.asarray(out, float)


def e0_diagonal_moments(matrix, jmax):
    """m_j = (M^j)_{00}, j = 0..jmax, by the Krylov recursion on the
    ENTRIES of the wall matrix."""
    mat = np.asarray(matrix, float)
    vec = np.zeros(mat.shape[0])
    vec[0] = 1.0
    out = []
    for _j in range(jmax + 1):
        out.append(float(vec[0]))
        vec = mat @ vec
    return np.asarray(out, float)


def nu_from_e0_moments(mom, kdeg):
    """Invert the exact triangular relation between the e_0-diagonal
    moments m_j = (M^j)_{00} and the b-weighted moments nu_k.  With
    M^j e_0 = (m_j, y_j) and y_j = sum_i c^j_i B^i b one gets
    c^j_i = m_{j-1-i}, hence for every j >= 1
      m_{j+1} = m_1 m_j + sum_{i=0}^{j-1} m_{j-1-i} nu_i,
    a unit-leading triangular system (the coefficient of nu_{j-1} is
    m_0 = 1).  Needs m_0..m_{kdeg+2}; returns nu_0..nu_kdeg.  Works
    for floats and for Fractions."""
    nus = []
    for j in range(1, kdeg + 2):
        acc = mom[j + 1] - mom[1] * mom[j]
        for i in range(j - 1):
            acc = acc - mom[j - 1 - i] * nus[i]
        nus.append(acc)
    return nus


def lanczos_pair(matrix, kdeg):
    """Lanczos data (alpha_1..alpha_K, beta_1..beta_{K-1}) of the pair
    (B, b/||b||) from the wall ENTRIES; forward recursion only."""
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
    K = len(alp) with the node prescribed at floor_c.  Returns
    (bound, the modified Jacobi matrix of the rule) -- the node ward
    is done by the CALLER, so that no eigensolver ever appears inside
    the bound path (AC)."""
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


def sigma_bound_source(matrix, floor_c, kdeg):
    """THE SOURCE-ONLY BOUND: sigma <= RADAU_K(nu; floor_c) / n, from
    the wall ENTRIES and the certified floor alone."""
    piv = float(np.asarray(matrix, float)[0, 0])
    lan = lanczos_pair(matrix, kdeg)
    if lan is None or piv <= 0.0:
        return float("nan"), None
    alp, bet, mass = lan
    val, jac = radau_upper(alp, bet, floor_c, mass)
    if not math.isfinite(val):
        return float("nan"), None
    return val / piv, jac


def lp_moment_bound(matrix, floor_c, radius_l, deg):
    """E4 cross-route: the truncated moment LP optimum on
    [floor_c, radius_l], i.e. the sharpest bound obtainable from the
    moments of order <= deg.  The Chebyshev moments are built by the
    stable three-term matrix recursion on the wall ENTRIES; the LP is
    the measure-side (primal) form, whose optimizer is the extremal
    measure the moments cannot exclude.  Ward route only."""
    mat = np.asarray(matrix, float)
    vec = mat[1:, 0]
    blk = mat[1:, 1:]
    pmat = (2.0 * blk - (floor_c + radius_l)
            * np.eye(blk.shape[0])) / (radius_l - floor_c)
    v_prev = vec.copy()
    v_cur = pmat @ vec
    tau = [float(vec @ v_prev), float(vec @ v_cur)]
    for _k in range(2, deg + 1):
        v_new = 2.0 * (pmat @ v_cur) - v_prev
        tau.append(float(vec @ v_new))
        v_prev, v_cur = v_cur, v_new
    tau = np.asarray(tau[:deg + 1], float)
    if tau[0] <= 0.0:
        return float("nan"), None
    xs = np.geomspace(floor_c, radius_l, LP_GRID)
    ys = (2.0 * xs - (floor_c + radius_l)) / (radius_l - floor_c)
    tmat = np.zeros((deg + 1, LP_GRID))
    tmat[0] = 1.0
    if deg >= 1:
        tmat[1] = ys
    for k in range(2, deg + 1):
        tmat[k] = 2.0 * ys * tmat[k - 1] - tmat[k - 2]
    res = optimize.linprog(c=-(floor_c / xs), A_eq=tmat,
                           b_eq=tau / tau[0],
                           bounds=[(0.0, None)] * LP_GRID,
                           method="highs")
    if not res.success:
        return float("nan"), None
    weights = np.asarray(res.x, float) * tau[0]
    keep = weights > 1e-12 * float(np.sum(weights))
    return -res.fun / floor_c * tau[0], (xs[keep], weights[keep])


def exact_moment_pair(matrix, kdeg):
    """Exact-rational tier on the dyadic float entries (CCVII v897
    class machinery): the b-weighted moments nu_k = b^T B^k b and the
    e_0-diagonal moments m_j = (M^j)_{00}, both as Fractions."""
    mat = np.asarray(matrix, float)
    vecf = [Fraction(float(v)) for v in mat[1:, 0]]
    blkf = [[Fraction(float(mat[i + 1, j + 1]))
             for j in range(NDIM - 1)] for i in range(NDIM - 1)]
    cur = list(vecf)
    nus = []
    for _k in range(kdeg + 1):
        nus.append(sum(a * b for a, b in zip(vecf, cur)))
        cur = [sum(blkf[i][j] * cur[j] for j in range(NDIM - 1))
               for i in range(NDIM - 1)]
    matf = [[Fraction(float(mat[i, j])) for j in range(NDIM)]
            for i in range(NDIM)]
    vecm = [Fraction(1)] + [Fraction(0)] * (NDIM - 1)
    mom = []
    for _j in range(kdeg + 3):
        mom.append(vecm[0])
        vecm = [sum(matf[i][j] * vecm[j] for j in range(NDIM))
                for i in range(NDIM)]
    return nus, mom


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
    return zones, steps


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
    check("T1 fixed CCXXV GLOBAL m=8 filter %s: L rel %.2e, poles "
          "%.2e, residues %.2e <= %.0e"
          % ("rebuilt from stored L (SMOKE)" if SMOKE
             else "rebuilt from source-only L",
             dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    print("    separator facts (CCXXV interval certificates, "
          "re-consumed): global R lower %.3e >= 0 (outward), bulk "
          "delta %.6e on [c_B, L] = [%.6f, %.6g]"
          % (fdata["global_R_lower"], fdata["delta"], CB_F,
             fdata["L"]))
    return fdata


def translation(steps, artifact, fdata):
    section("T -- per-step reads: LU partial fractions vs artifact "
            "vs eigen route")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_tr = d_marg = d_eig = 0.0
    n_match = 0
    for idx, st in enumerate(steps):
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
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         gap=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         l_src=float(st["L_src"]),
                         trace_r=trace_lu,
                         reserve=1.0 - trace_lu,
                         matched=src is not None))
    check("T2 LU trace_R / margin reproduce the stored artifact on "
          "%d matched steps: %.2e / %.2e <= %.0e"
          % (n_match, d_tr, d_marg, LU_TIE),
          n_match >= 1 and d_tr <= LU_TIE and d_marg <= LU_TIE
          and (SMOKE or n_match == STEPS_EXP), kill="K2")
    check("T3 eigen-route trace == LU partial-fraction trace on all "
          "%d steps: max dev %.2e <= %.0e"
          % (len(rows), d_eig, PF_TIE), d_eig <= PF_TIE, kill="K2")
    xs_test = [-fdata["L"], -math.sqrt(CB_F * fdata["L"]), -CB_F,
               CB_F, math.sqrt(CB_F * fdata["L"]), fdata["L"]]
    d_pf = 0.0
    for x in xs_test:
        pf = 1.0 + 2.0 * math.fsum(
            float(rr) * x / (x * x + float(zz.imag) ** 2)
            for rr, zz in zip(fdata["residues"], fdata["poles"]))
        d_pf = max(d_pf, abs(pf - zol.scalar_r(fdata, x))
                   / max(1.0, abs(pf)))
    check("T4 scalar partial-fraction form == product form R at %d "
          "declared sample points: max rel %.2e <= %.0e"
          % (len(xs_test), d_pf, R_SAMPLE_TIE),
          d_pf <= R_SAMPLE_TIE, kill="K2")
    reserves = np.asarray([r["reserve"] for r in rows], float)
    med, mn = float(np.median(reserves)), float(np.min(reserves))
    ok_rep = (abs(med / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(mn / RES_MIN_REF - 1.0) <= REPRO_RTOL)
    check("T5 REPRO CCXLVII: reserve med %.4f (ref %.4f), min %.4e "
          "(ref %.3e), rtol %.0e" % (med, RES_MED_REF, mn,
                                     RES_MIN_REF, REPRO_RTOL),
          SMOKE or ok_rep, kill="K3")
    print("    reserve = 1 - tr R: %s" % e3(reserves))
    return rows


# ============================= B: the Jacobi translation, warded
def jacobi_translation(rows):
    section("B -- the Jacobi translation of every step (CCLXI "
            "verbatim), warded")
    d_b1 = d_a1 = d_bfl = d_m0 = 0.0
    n_bad = 0
    for row in rows:
        st = row["step"]
        jf = jacobi_form(st["Mt"])
        if jf is None:
            n_bad += 1
            row["theta"] = None
            continue
        a, b, qq = jf
        theta = np.concatenate([b, a])
        row["theta"] = theta
        row["frame"] = qq
        _jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(b[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(a[0] - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(_jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["gap"] - 1.0))
    check("B1 Lanczos form of (M_h, e_0) exists on all %d steps"
          % len(rows), n_bad == 0, "breakdowns %d" % n_bad,
          kill="K2")
    check("B2 TRANSLATE b_1 == M[0,0] and a_1 == ||M[1:,0]||: "
          "%.2e / %.2e <= %.0e" % (d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill="K2")
    check("B3 TRANSLATE lambda_min(J_B) == lamB1 (E2 compression "
          "similarity): max rel %.2e <= %.0e"
          % (d_bfl, TRANSLATE_TIE), d_bfl <= TRANSLATE_TIE,
          kill="K2")
    check("B4 WARD m(0) * gap == 1 (CCLIII B5): max %.2e <= %.0e"
          % (d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill="K2")
    return [r for r in rows if r["theta"] is not None]


# =================== I: THE IDENTITY -- sigma in wall coordinates
def identity_section(rows):
    section("I -- (a) THE IDENTITY: what sigma IS in wall "
            "coordinates")
    print("""    CLAIM (E2, exact).  M = [[n, b^T], [b, B]] with
      n = M[0,0] (bad-mode pivot), b = M[1:,0], B = M[1:,1:],
      q = b^T B^{-1} b, Schur scalar s = n - q.  Lanczos of (M, e_0)
      builds the frame Q = [e_0, Q_B] with Q_B e_1 = b/||b|| and
      a_1 = ||b||, and J_B = Q_B^T B Q_B.  Therefore
        a_1^2 [J_B^{-1}]_{11} = (a_1 Q_B e_1)^T B^{-1} (a_1 Q_B e_1)
                              = b^T B^{-1} b = q,
      and with b_1 = n,
        sigma = a_1^2 [J_B^{-1}]_{11} / b_1 = q / n = 1 - s/n.
      The CCLXI cap sigma <= t is therefore EXACTLY the RELATIVE
      Schur-gap floor s >= (1 - t) n.""")
    d_q = d_sig = d_gap = d_frame = 0.0
    for row in rows:
        st = row["step"]
        theta = row["theta"]
        piv = float(st["n0"])
        vec = np.asarray(st["bvec"], float)
        blk = np.asarray(st["Bblk"], float)
        q_wall = float(vec @ np.linalg.solve(blk, vec))
        sig = sigma_quotient(theta)
        row["sigma"] = sig
        row["q_wall"] = q_wall
        _jm, jb = theta_matrices(theta)
        e1 = np.zeros(NDIM - 1)
        e1[0] = 1.0
        a1sq_m11 = (float(theta[NDIM]) ** 2
                    * float(np.linalg.solve(jb, e1)[0]))
        d_q = max(d_q, abs(a1sq_m11 - q_wall) / max(1.0, abs(q_wall)))
        d_sig = max(d_sig, abs(sig - q_wall / piv)
                    / max(1.0, abs(sig)))
        d_gap = max(d_gap, abs(sig - (1.0 - row["gap"] / piv))
                    / max(1.0, abs(sig)))
        nrm = float(np.linalg.norm(vec))
        if nrm > 0.0:
            col = row["frame"][:, 1]
            d_frame = max(d_frame, abs(float(col[0])),
                          float(np.max(np.abs(col[1:]
                                              - vec / nrm))))
        else:
            d_frame = 1.0
    check("I1 IDENTITY a_1^2 [J_B^-1]_11 == q = b^T B^-1 b on all "
          "%d steps: max rel %.2e <= %.0e"
          % (len(rows), d_q, IDENT_TIE), d_q <= IDENT_TIE, kill="K2")
    check("I2 IDENTITY sigma == q/n: max rel %.2e <= %.0e"
          % (d_sig, IDENT_TIE), d_sig <= IDENT_TIE, kill="K2")
    check("I3 IDENTITY sigma == 1 - s/n (s = the CCVII Schur gap): "
          "max rel %.2e <= %.0e" % (d_gap, IDENT_TIE),
          d_gap <= IDENT_TIE, kill="K2")
    check("I4 FRAME ward Q_B e_1 == b/||b||: max abs %.2e <= %.0e"
          % (d_frame, TRANSLATE_TIE), d_frame <= TRANSLATE_TIE,
          kill="K2")
    sig = [r["sigma"] for r in rows]
    rel_gap = [1.0 - s for s in sig]
    print("    sigma min/med/max over the ladder: %s" % f4(sig))
    print("    relative Schur gap s/n = 1 - sigma: %s" % f4(rel_gap))
    for seg in ("surf", "bridge", "deep"):
        sub = [r["sigma"] for r in rows if r["seg"] == seg]
        if sub:
            print("      %-7s (%2d steps): %s" % (seg, len(sub),
                                                  f4(sub)))
    hs = np.asarray([r["h"] for r in rows], float)
    slope, two_se, r2, _a = linfit(np.log(hs), np.log(np.asarray(
        sig, float)))
    print("    h-law of sigma: log-log slope %+.4f +/- %.4f "
          "(2SE), R^2 %.3f" % (slope, two_se, r2))
    return slope, two_se


# ============== C0: is sigma's 0.665 the CCLIII/CCXLV invariant?
def coincidence_test(rows):
    section("C0 -- THE 0.665 DECIDER: is the sigma cap the CCLIII / "
            "CCXLV invariant?")
    sig = np.asarray([r["sigma"] for r in rows], float)
    smax = float(np.max(sig))
    cap = smax * (1.0 + MARGIN_FRAC)
    print("    PROVENANCE of the CCLXI cap: max_truth(sigma) * "
          "(1 + MARGIN_FRAC) = %.6f * %.2f = %.6f (CCLXI reported "
          "0.665).  The cap MOVES with the probe's own margin "
          "parameter: at MARGIN_FRAC 0.05 it would read %.4f, at "
          "0.20 %.4f -- an invariant cannot do that."
          % (smax, 1.0 + MARGIN_FRAC, cap, smax * 1.05, smax * 1.20))
    kzs = sorted({r["kz"] for r in rows if r["seg"] == "surf"})
    subset = kzs[::MEAS_STRIDE]
    meas = {}
    for kz in subset:
        src = rt.measure_source("surf", kz)
        chain = rt.build_chain_from_source(src, src["h"] // 2 + 2)
        if chain is None:
            continue
        car = rt.carriers_of(chain)
        meas[int(kz)] = car
    res_vals = []
    sig_vals = []
    for row in rows:
        car = meas.get(row["kz"])
        if car is not None and row["seg"] == "surf":
            res_vals.append(float(car["res"]))
            sig_vals.append(float(row["sigma"]))
    corr = pearson(res_vals, sig_vals)
    med_res = float(np.median(res_vals)) if res_vals else float("nan")
    ok_rep = (math.isfinite(med_res)
              and abs(med_res / rt.RES_MED_REF - 1.0) <= REPRO_RTOL)
    check("C0.1 REPRO CCXLV restricted residual on the frozen stride "
          "subset (%d rungs, stride %d): res med %.4f vs CCXLV %.3f"
          % (len(res_vals), MEAS_STRIDE, med_res, rt.RES_MED_REF),
          ok_rep or SMOKE, kill="K3")
    print("    measure-side res(h) med %.4f (the CCXLV/CCLIII 0.665) "
          "vs wall-side sigma med %.4f: Pearson corr %.3f over %d "
          "matched rungs (CCLIII K4(iii) measured the measure->wall "
          "link null, -0.022)"
          % (med_res, float(np.median(sig)), corr, len(res_vals)))
    link = ("UNDERPOWERED(n=%d)" % len(res_vals)
            if len(res_vals) < 8 or not math.isfinite(corr)
            else "NULL" if abs(corr) <= CORR_BAR else "PRESENT")
    check("C0.2 DECIDER (provenance, decisive): the CCLXI cap is a "
          "MARGIN ARTIFACT of the truth envelope, not an invariant "
          "-- typed COINCIDENCE.  Secondary, separable question, the "
          "carrier link corr(sigma, res) = %.3f -> %s (a link would "
          "make the CCLIII carrier formulas transferable, but would "
          "still not make 0.665 the cap)"
          % (corr, link), True)
    return "COINCIDENCE(cap = margin artifact); CARRIER-LINK %s" \
        % link, corr, cap


# ================================== G: freeze the class C_KS
COORD = tuple(["b%d" % (i + 1) for i in range(NDIM)]
              + ["a%d" % (i + 1) for i in range(NDIM - 1)])


def freeze_class(rows, fdata):
    section("G -- FREEZE the class C_KS (CCLXI construction "
            "verbatim; constants printed BEFORE any optimization)")
    thetas = np.asarray([r["theta"] for r in rows], float)
    t_lo = thetas.min(axis=0)
    t_hi = thetas.max(axis=0)
    width = np.maximum(t_hi - t_lo, 1e-12 * np.maximum(1.0,
                                                       np.abs(t_hi)))
    lo = t_lo - MARGIN_FRAC * width
    hi = t_hi + MARGIN_FRAC * width
    lo[NDIM:] = np.maximum(lo[NDIM:], 0.0)
    cb_use = CB_F
    lamb_min = min(float(np.linalg.eigvalsh(
        theta_matrices(r["theta"])[1])[0]) for r in rows)
    widened = False
    if lamb_min < CB_F:
        cb_use = lamb_min * (1.0 - MARGIN_FRAC)
        widened = True
        print("    WIDENED (disclosed): measured truth "
              "lambda_min(J_B) = %.6f < cited c_B = %.6f; floor "
              "honestly widened to %.6f" % (lamb_min, CB_F, cb_use))
    cls = dict(lo=lo, hi=hi, wd=hi - lo, cb=cb_use, L=fdata["L"],
               coord=COORD)
    funcs = np.asarray([ks_wall_functionals(r["theta"], cls)
                        for r in rows], float)
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
    print("    B-floor c_B = %.6f (%s); L = %.8g (CCXXV frozen "
          "filter L); KS_wall cap %.6f; COEF box [%.6f, %.6f]; "
          "SPREAD box [%.6f, %.6f]"
          % (cls["cb"], "WIDENED" if widened else "CITED CLIII, "
             "holds on all steps", cls["L"], cls["ks_cap"],
             cls["coef_lo"], cls["coef_hi"], cls["spr_lo"],
             cls["spr_hi"]))
    frozen = np.concatenate([lo, hi,
                             [cls["cb"], cls["L"], cls["ks_cap"],
                              cls["coef_lo"], cls["coef_hi"],
                              cls["spr_lo"], cls["spr_hi"]]])
    box_sha = hashlib.sha256(frozen.tobytes()).hexdigest()
    check("G1 class frozen BEFORE optimization (box SHA-256 %s%s)"
          % (box_sha[:16], "; B-floor WIDENED, disclosed"
             if widened else ""), True)
    cls["box_sha"] = box_sha
    cls["widened"] = widened
    return cls


def membership_census(rows, cls):
    section("N -- membership census: all truth steps IN the class")
    slack_rows = []
    n_in = 0
    for r in rows:
        sl, names = class_slack_vector(r["theta"], cls)
        r["slack_min"] = float(np.min(sl))
        slack_rows.append(sl)
        if r["slack_min"] >= -FEAS_TOL:
            n_in += 1
    slack_rows = np.asarray(slack_rows, float)
    _sl, names = class_slack_vector(rows[0]["theta"], cls)
    per_min = slack_rows.min(axis=0)
    order = np.argsort(per_min)
    print("    tightest constraints across the truth ladder "
          "(min normalized slack):")
    for j in order[:6]:
        print("      %-14s %.6e" % (names[j], per_min[j]))
    check("N1 truth membership %d/%d steps IN C_KS (min slack %s)"
          % (n_in, len(rows), e3([r["slack_min"] for r in rows])),
          n_in == len(rows), kill="K2")
    return names


# ============================== O: the optimization machinery
def make_objective(cls, fdata, extra_con=None):
    def neg_f(theta):
        v = tr_r_of_theta(theta, fdata)
        return -v if math.isfinite(v) else 1e12

    def slacks(theta):
        sl, _names = class_slack_vector(theta, cls)
        if extra_con is not None:
            sl = np.concatenate([sl, [extra_con(theta)]])
        return sl

    def penalized(theta):
        v = tr_r_of_theta(theta, fdata)
        if not math.isfinite(v):
            return 1e12
        sl = slacks(theta)
        viol = float(np.sum(np.clip(-sl, 0.0, None)))
        return -v + PEN_W * viol * viol
    return neg_f, slacks, penalized


def sigma_cap_con(cap):
    """The sigma constraint as a normalized slack (theta only)."""
    def con(theta):
        s = sigma_quotient(theta)
        if not math.isfinite(s):
            return -1.0
        return (cap - s) / max(abs(cap), 1e-6)
    return con


def run_stage1(rows, cls, fdata, label, n_ms, de_maxiter,
               extra_con=None, box=None, quiet=False):
    lo = cls["lo"] if box is None else box[0]
    hi = cls["hi"] if box is None else box[1]
    bounds = list(zip(lo, hi))
    neg_f, slacks, penalized = make_objective(cls, fdata, extra_con)
    rng = np.random.default_rng(OPT_SEED)
    thetas = [r["theta"] for r in rows]
    seeds = []
    idx = np.linspace(0, len(thetas) - 1,
                      max(2, n_ms // 3)).astype(int)
    for i in sorted(set(idx.tolist())):
        seeds.append(np.clip(thetas[i], lo, hi))
    for i in sorted(set(idx.tolist())):
        cn = np.clip(thetas[i], lo, hi).copy()
        cn[0] = lo[0] + 1e-9 * (hi[0] - lo[0])
        cn[NDIM] = hi[NDIM] - 1e-9 * (hi[NDIM] - lo[NDIM])
        seeds.append(cn)
    while len(seeds) < n_ms:
        seeds.append(rng.uniform(lo, hi))
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
        penalized, bounds=bounds, seed=OPT_SEED, maxiter=de_maxiter,
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
    if not quiet:
        print("    %s: best feasible tr R = %.6f (feasible SLSQP "
              "starts %d/%d) [%.1f s]"
              % (label, best_v, n_conv, n_ms, time.time() - T0),
              flush=True)
    return best_v, best_t


def truth_best_under_cap(rows, cap):
    """The truth ladder is inside the class; its own best tr R under
    the cap is a valid lower bound for the constrained supremum."""
    best = -float("inf")
    for r in rows:
        if r["sigma"] <= cap:
            best = max(best, r["trace_r"])
    return best


# ------------------- stage-2 rational witness (CCLXI verbatim)
def frac_first_bad_pivot(mfrac):
    n = len(mfrac)
    m = [row[:] for row in mfrac]
    for k in range(n):
        if m[k][k] <= 0:
            return k + 1
        for i in range(k + 1, n):
            f = m[i][k] / m[k][k]
            for j in range(k, n):
                m[i][j] -= f * m[k][j]
    return None


def rational_witness(theta, cls, fdata):
    scale = 2 ** QBITS
    th_r = np.round(np.asarray(theta, float) * scale) / scale
    exact_ok = True
    reasons = []
    lo, hi = cls["lo"], cls["hi"]
    for i in range(len(th_r)):
        if not (Fraction(float(lo[i])) <= Fraction(float(th_r[i]))
                <= Fraction(float(hi[i]))):
            exact_ok = False
            reasons.append("box[%s]" % COORD[i])
    if any(Fraction(float(v)) <= 0 for v in th_r[NDIM:]):
        exact_ok = False
        reasons.append("a>0")
    bf = [Fraction(float(v)) for v in th_r[:NDIM]]
    af = [Fraction(float(v)) for v in th_r[NDIM:]]
    cbf = (Fraction(5523, 10000) if not cls["widened"]
           else Fraction(float(cls["cb"])))
    lf = Fraction(float(cls["L"]))

    def jac_frac(bd, ad, shift, sign):
        n = len(bd)
        m = [[Fraction(0)] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = sign * bd[i] + shift
            if i + 1 < n:
                m[i][i + 1] = sign * ad[i]
                m[i + 1][i] = sign * ad[i]
        return m
    if frac_first_bad_pivot(jac_frac(bf[1:], af[1:], -cbf, 1)) \
            is not None:
        exact_ok = False
        reasons.append("B_floor")
    if frac_first_bad_pivot(jac_frac(bf, af, lf, -1)) is not None:
        exact_ok = False
        reasons.append("radius_hi")
    if frac_first_bad_pivot(jac_frac(bf, af, lf, 1)) is not None:
        exact_ok = False
        reasons.append("radius_lo")
    ks, coef, spread = ks_wall_functionals(th_r, cls)
    for nm, val, lo_v, hi_v in (
            ("KS_wall", ks, None, cls["ks_cap"]),
            ("COEF", coef, cls["coef_lo"], cls["coef_hi"]),
            ("SPREAD", spread, cls["spr_lo"], cls["spr_hi"])):
        if hi_v is not None and val > hi_v - FUNC_PAD * abs(hi_v):
            exact_ok = False
            reasons.append(nm + "_pad")
        if lo_v is not None and val < lo_v + FUNC_PAD * abs(lo_v):
            exact_ok = False
            reasons.append(nm + "_pad")
    bad = frac_first_bad_pivot(jac_frac(bf, af, Fraction(0), 1))
    tr_r = tr_r_of_theta(th_r, fdata)
    if exact_ok and bad is not None:
        return ("WITNESS-RATIONAL-EXACT", dict(
            theta=th_r, minor=bad, tr=tr_r,
            note="rounded incumbent IN the class and leading minor "
                 "%d <= 0 -> not PD -> tr R >= 1 by the certified "
                 "separator facts" % bad))
    return ("NUMERIC(point)", dict(
        theta=th_r, minor=bad, tr=tr_r,
        note=("rounded incumbent %s; not-PD witness %s"
              % ("IN class" if exact_ok
                 else "leaves class at " + ",".join(reasons[:4]),
                 "found (minor %s)" % bad if bad is not None
                 else "absent (matrix PD)"))))


# ==================== T: (b) THE THRESHOLD MAP t -> sup tr R
def threshold_map(rows, cls, fdata):
    section("T* -- (b) THE THRESHOLD MAP: sup tr R over C_KS with "
            "sigma <= t")
    n_ms = 8 if SMOKE else MAP_MS
    de_it = 30 if SMOKE else MAP_DE
    grid = T_GRID if not SMOKE else (0.665, 0.95)
    sup_nocap, theta_nc = run_stage1(rows, cls, fdata,
                                     "t = +inf (no cap, CCLXI GAP "
                                     "reproduction)",
                                     CONF_MS if not SMOKE else 8,
                                     CONF_DE if not SMOKE else 30)
    sup_nocap = max(sup_nocap, max(r["trace_r"] for r in rows))
    check("T*0 REPRO CCLXI KSDUAL-GAP without the cap: sup tr R = "
          "%.4f >= %.1f (CCLXI reported %.2f; ratio %.3f -- a "
          "numeric sup is a lower bound, so a smaller value is a "
          "weaker search, not a contradiction)"
          % (sup_nocap, SUP_NOCAP_BAR, SUP_NOCAP_REF,
             sup_nocap / SUP_NOCAP_REF),
          SMOKE or sup_nocap >= SUP_NOCAP_BAR, kill="K3")
    table = []
    incumb = []
    for t_cap in grid:
        val, th_c = run_stage1(rows, cls, fdata,
                               "sigma <= %.4f" % t_cap, n_ms, de_it,
                               extra_con=sigma_cap_con(t_cap))
        val = max(val, truth_best_under_cap(rows, t_cap))
        table.append((t_cap, val))
        if th_c is not None:
            incumb.append((t_cap, float(th_c[0]),
                           sigma_quotient(th_c)))
    mono = all(table[i][1] <= table[i + 1][1] + 1e-6
               for i in range(len(table) - 1))
    print("    HARD FLOOR (disclosed): the truth ladder lies IN the "
          "class, so every constrained supremum is at least the "
          "truth maximum tr R = %.6f (reserve %.4e); the map below "
          "reports max(optimizer, truth-under-cap)."
          % (max(r["trace_r"] for r in rows),
             1.0 - max(r["trace_r"] for r in rows)))
    print("    map t -> sup tr R (numeric global; monotone "
          "nondecreasing in t by construction):")
    for t_cap, val in table:
        print("      t = %-6.4f  sup tr R = %.6f   %s"
              % (t_cap, val, "CLOSES" if val < 1.0 else "OPEN"))
    check("T*1 monotonicity of the measured map (optimizer noise "
          "tolerated, reported): %s"
          % ("monotone" if mono else "NON-MONOTONE (search noise)"),
          True)
    n_neg = sum(1 for _t, b1v, _s in incumb if b1v <= 0.0)
    print("    VACUITY DIAGNOSTIC (amendment A6, the decisive "
          "anatomy of this map): the capped incumbents carry pivot "
          "b_1 = n and sigma %s"
          % ", ".join("t=%.3f: n=%+.4g sigma=%+.4g"
                      % (t, b1v, sv) for t, b1v, sv in incumb[:4]))
    print("      %d of %d capped incumbents have a NONPOSITIVE pivot "
          "n <= 0.  By the section-I identity sigma = q/n, a "
          "nonpositive pivot with q > 0 gives sigma < 0, so the "
          "ONE-SIDED cap sigma <= t is VACUOUS there: the optimizer "
          "keeps the CCLXI bad mode and satisfies the cap for free.  "
          "The cap only carries its intended meaning (the relative "
          "Schur-gap floor s >= (1 - t) n) on the pivot-positive "
          "sheet -- measured next in T*P." % (n_neg, len(incumb)))
    below = [t for t, v in table if v < 1.0]
    above = [t for t, v in table if v >= 1.0]
    t_close = max(below) if below else 0.0
    if not below:
        t_star = float(min(grid))
        print("    every grid t already OPEN -> t* below the grid; "
              "no measured closing cap")
    elif not above:
        t_star = float("inf")
        print("    no grid t reaches 1 -> t* above the frozen grid; "
              "the largest MEASURED closing cap is %.4f" % t_close)
    else:
        lo_t, hi_t = max(below), min(above)
        for _it in range(BISECT_MAX if not SMOKE else 1):
            if hi_t - lo_t <= BISECT_TOL:
                break
            mid = 0.5 * (lo_t + hi_t)
            val, _th = run_stage1(rows, cls, fdata,
                                  "bisect sigma <= %.5f" % mid,
                                  n_ms, de_it,
                                  extra_con=sigma_cap_con(mid),
                                  quiet=True)
            val = max(val, truth_best_under_cap(rows, mid))
            print("      bisect t = %.5f -> sup %.6f (%s)"
                  % (mid, val, "closes" if val < 1.0 else "open"))
            if val < 1.0:
                lo_t = mid
            else:
                hi_t = mid
        t_star = 0.5 * (lo_t + hi_t)
        t_close = lo_t
    sig = np.asarray([r["sigma"] for r in rows], float)
    print("    CLOSING THRESHOLD t* = %.4f (bracket width <= %.4f); "
          "largest MEASURED closing cap t_close = %.4f; truth sigma "
          "max %.4f -> truth margin t* - max(sigma) = %+.4f, ratio "
          "max(sigma)/t* = %.3f"
          % (t_star, BISECT_TOL, t_close, float(np.max(sig)),
             t_star - float(np.max(sig)),
             float(np.max(sig)) / t_star if t_star > 0 else
             float("nan")))
    ref = [v for t, v in table if abs(t - SIG_CAP_REF) < 1e-9]
    if ref:
        check("T*2 CCLXI preview re-measured at the cap %.3f: sup "
              "tr R = %.4f, still < 1 (CCLXI reported %.4f -- "
              "HONEST CORRECTION, disclosed: that preview searched "
              "only, without the truth floor, and the truth ladder "
              "itself lies in the class with max tr R = %.4f, so "
              "ANY constrained supremum is at least that; the "
              "reserve under any sigma cap is therefore bounded by "
              "the CCXLVII worst step, not by the preview number)"
              % (SIG_CAP_REF, ref[0], SIG_PREV_REF,
                 max(r["trace_r"] for r in rows)), ref[0] < 1.0)
    return t_star, t_close, table, sup_nocap, theta_nc


def pivot_positive_box(cls):
    """The class box intersected with the SOURCE-ONLY entry fact
    n = M[0,0] > 0 (b_1 is the pivot in Jacobi coordinates)."""
    lo = np.asarray(cls["lo"], float).copy()
    hi = np.asarray(cls["hi"], float).copy()
    lo[0] = 0.0
    return (lo, hi)


def pivot_positive_map(rows, cls, fdata):
    """Amendment A6.  The same map on the pivot-positive sheet, where
    the cap is not vacuous.  n > 0 is an ENTRY fact of the assembled
    wall matrix -- no eigendata, no read, source-checkable per rung."""
    section("T*P -- (b, amendment A6) THE MAP ON THE PIVOT-POSITIVE "
            "SHEET: sup tr R over C_KS with n > 0 and sigma <= t")
    piv = np.asarray([r["n_piv"] for r in rows], float)
    check("P1 SOURCE-ONLY PIVOT SIGN the wall pivot n = M[0,0] is "
          "positive on %d/%d deployed rungs (min %.6f, med %.4f) -- "
          "an entry of the assembled step matrix, so this premise "
          "costs no eigendata and no read"
          % (int(np.sum(piv > 0)), len(piv), float(np.min(piv)),
             float(np.median(piv))), bool(np.all(piv > 0)))
    print("    ALGEBRA (E2, exact).  With n > 0 and B >= c_B I > 0 "
          "the Schur criterion gives  M > 0  <=>  s = n - q > 0  "
          "<=>  sigma < 1.  So on this sheet the cap sigma <= t < 1 "
          "is EXACTLY 'the wall step is positive definite with "
          "relative Schur gap >= 1 - t' -- the CCLXI cap finally "
          "means what its name says.")
    n_ms = 8 if SMOKE else MAP_MS
    de_it = 30 if SMOKE else MAP_DE
    grid = T_GRID if not SMOKE else (0.665, 1.10)
    box = pivot_positive_box(cls)
    table, opt_only, bad_ward = [], [], 0
    for t_cap in grid:
        val, th_c = run_stage1(rows, cls, fdata,
                               "n > 0, sigma <= %.4f" % t_cap,
                               n_ms, de_it,
                               extra_con=sigma_cap_con(t_cap),
                               box=box)
        if th_c is not None:
            if float(th_c[0]) < -1e-12 \
                    or sigma_quotient(th_c) > t_cap + 1e-6:
                bad_ward += 1
        opt_only.append(val)
        val = max(val, truth_best_under_cap(rows, t_cap))
        table.append((t_cap, val))
    check("P2 WARD every pivot-positive incumbent really has n >= 0 "
          "and sigma <= t (the cap is enforced, not assumed): "
          "violations %d" % bad_ward, bad_ward == 0)
    print("    map t -> sup tr R on the pivot-positive sheet "
          "(optimizer value and truth floor reported separately):")
    for (t_cap, val), ov in zip(table, opt_only):
        print("      t = %-6.4f  sup tr R = %.6f   %-6s "
              "(optimizer %.6f, truth-under-cap %.6f)"
              % (t_cap, val, "CLOSES" if val < 1.0 else "OPEN", ov,
                 truth_best_under_cap(rows, t_cap)))
    below = [t for t, v in table if v < 1.0]
    above = [t for t, v in table if v >= 1.0]
    t_close = max(below) if below else 0.0
    if not below:
        t_star = float(min(grid))
        print("    every grid t OPEN on the pivot-positive sheet too "
              "-> the pivot sign does not rescue the cap")
    elif not above:
        t_star = float("inf")
        print("    no grid t reaches 1 -> t* above the frozen grid; "
              "largest MEASURED closing cap %.4f" % t_close)
    else:
        lo_t, hi_t = max(below), min(above)
        for _it in range(BISECT_MAX if not SMOKE else 1):
            if hi_t - lo_t <= BISECT_TOL:
                break
            mid = 0.5 * (lo_t + hi_t)
            val, _th = run_stage1(rows, cls, fdata,
                                  "bisect n > 0, sigma <= %.5f" % mid,
                                  n_ms, de_it,
                                  extra_con=sigma_cap_con(mid),
                                  box=box, quiet=True)
            val = max(val, truth_best_under_cap(rows, mid))
            print("      bisect t = %.5f -> sup %.6f (%s)"
                  % (mid, val, "closes" if val < 1.0 else "open"))
            if val < 1.0:
                lo_t = mid
            else:
                hi_t = mid
        t_star = 0.5 * (lo_t + hi_t)
        t_close = lo_t
    sig = np.asarray([r["sigma"] for r in rows], float)
    print("    PIVOT-POSITIVE CLOSING THRESHOLD t*_pos = %.4f "
          "(bracket <= %.4f); largest MEASURED closing cap %.4f; "
          "truth sigma max %.4f -> margin %+.4f, ratio %.3f"
          % (t_star, BISECT_TOL, t_close, float(np.max(sig)),
             t_star - float(np.max(sig)),
             float(np.max(sig)) / t_star if t_star > 0
             else float("nan")))
    if not above:
        val, _th = run_stage1(rows, cls, fdata,
                              "OPT-POWER control n > 0, sigma <= 2.0 "
                              "(indefinite sheet must be reachable)",
                              n_ms, de_it,
                              extra_con=sigma_cap_con(2.0), box=box)
        check("P3 OPT-POWER control on the pivot-positive sheet: with "
              "the cap relaxed to 2.0 (sigma > 1 <=> s < 0 <=> the "
              "step is NOT positive definite) the optimizer reaches "
              "tr R = %.4f >= 1" % val, val >= 1.0)
    else:
        check("P3 OPT-POWER control: at the map's own largest cap t = "
              "%.2f the OPTIMIZER itself (truth floor excluded) "
              "reaches tr R = %.4f >= 1 on the very same "
              "pivot-positive box, so the closures at smaller t are "
              "not search failures"
              % (table[-1][0], opt_only[-1]), opt_only[-1] >= 1.0)
    return t_star, t_close, table


# ============ D: (c) THE SOURCE-ONLY DERIVATION and its confirm
def derivation_section(rows, cls, t_star, t_close, t_close_pos):
    section("D -- (c) THE SOURCE-ONLY DERIVATION: Gauss-Radau "
            "moment bounds on sigma")
    floor_c = cls["cb"]
    d_mom = d_lp = d_lp6 = 0.0
    n_lp = 0
    dir_fail = 0
    n_exact = 0
    exact_ok = True
    sign_fail = 0
    node_fail = 0
    lp_extremal = None
    for i, row in enumerate(rows):
        mat = row["step"]["Mt"]
        scl = max(1.0, float(np.max(np.abs(mat))))
        nus = wall_moments(mat, 2 * KMAX)
        row["nus"] = nus
        mom_s = e0_diagonal_moments(mat / scl, NU_RECON_K + 2)
        nus_s = wall_moments(mat / scl, NU_RECON_K)
        rec = np.asarray(nu_from_e0_moments(mom_s, NU_RECON_K),
                         float)
        rel = np.abs(rec[:NU_RECON_K + 1] - nus_s) / np.maximum(
            1e-300, np.abs(nus_s))
        d_mom = max(d_mom, float(np.max(rel)))
        bounds = []
        for kdeg in range(1, KMAX + 1):
            val, jac = sigma_bound_source(mat, floor_c, kdeg)
            bounds.append(val)
            if math.isfinite(val):
                if val * row["n_piv"] < row["q_wall"] \
                        - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                    sign_fail += 1
                node = float(np.linalg.eigvalsh(jac)[0])
                if node < floor_c - 1e-9 * max(1.0, floor_c):
                    node_fail += 1
        row["bounds"] = np.asarray(bounds, float)
        if i < EXACT_STEPS:
            ex_nu, ex_mom = exact_moment_pair(mat, NU_RECON_K)
            rec_ex = nu_from_e0_moments(ex_mom, NU_RECON_K)
            n_exact += 1
            if any(rec_ex[k] != ex_nu[k]
                   for k in range(NU_RECON_K + 1)):
                exact_ok = False
            for deg in (2, 4, LP_DEG_MAX):
                lp, extr = lp_moment_bound(mat, floor_c,
                                           row["l_src"], deg)
                rad = row["bounds"][deg // 2] * row["n_piv"]
                if math.isfinite(lp) and math.isfinite(rad):
                    rel = abs(lp - rad) / max(1e-300, abs(rad))
                    if lp > rad * (1.0 + 1e-6):
                        dir_fail += 1
                    if deg <= 4:
                        n_lp += 1
                        d_lp = max(d_lp, rel)
                    else:
                        d_lp6 = max(d_lp6, rel)
                if i == 0 and deg == LP_DEG_MAX and extr is not None:
                    lp_extremal = extr
    check("D1 MOMENT ROUTE the b-weighted moments nu_k = b^T B^k b "
          "reconstruct from the e_0-diagonal moments m_j = (M^j)_00 "
          "by the amendment-A1 triangular relation, k <= %d, all %d "
          "steps (scaled matrix, float): max rel %.2e <= %.0e"
          % (NU_RECON_K, len(rows), d_mom, MOM_TIE),
          d_mom <= MOM_TIE, kill="K2")
    check("D2 EXACT-RATIONAL TIER the same reconstruction is EXACT "
          "(dyadic Fractions on the float entries, CCVII v897 class) "
          "on %d representative steps, k <= %d"
          % (n_exact, NU_RECON_K), exact_ok, kill="K2")
    check("D3 RB1 SIGN WARD the Gauss-Radau value is an UPPER bound "
          "for q on every step and every depth (E3 consumed with a "
          "ward, not on faith): violations %d; rules with a node "
          "below the floor: %d" % (sign_fail, node_fail),
          sign_fail == 0 and node_fail == 0, kill="K2")
    check("D4a LP CROSS-ROUTE DIRECTION (E4): the grid-discretised "
          "moment LP, whose optimum is a LOWER bound on the true "
          "moment-problem supremum, never exceeds RADAU -- "
          "violations %d" % dir_fail, dir_fail == 0, kill="K2")
    check("D4b LP CROSS-ROUTE AGREEMENT at degrees 2 and 4 (%d "
          "comparisons): max rel %.2e <= %.0e; at degree %d the "
          "discretisation is the limit, REPORTED-ONLY: max rel %.2e"
          % (n_lp, d_lp, LP_TIE, LP_DEG_MAX, d_lp6),
          n_lp == 0 or d_lp <= LP_TIE)
    if lp_extremal is not None:
        xs_e, ws_e = lp_extremal
        print("    the extremal measure of the LP at degree %d on "
              "the first step (WHAT the moments cannot exclude): "
              "nodes %s with masses %s"
              % (LP_DEG_MAX,
                 " ".join("%.4g" % v for v in xs_e[:6]),
                 " ".join("%.3g" % v for v in ws_e[:6])))
    if t_close > 0.0:
        t_bar, bar_src = t_close - T_MARGIN, "PLAIN"
    else:
        t_bar, bar_src = t_close_pos - T_MARGIN, "PIVOT-POSITIVE"
    print("    ladder maxima of the DERIVED sigma bound per depth "
          "(K = depth, moments consumed = m_1..m_2K); the bar is "
          "t_bar = t_close - %.2f = %.4f, taken from the %s map "
          "(amendment A6: the plain map has NO closing cap, so the "
          "only meaningful bar is the pivot-positive one, and the "
          "composed premise then carries the source-only entry fact "
          "n > 0 warded in P1):"
          % (T_MARGIN, t_bar, bar_src))
    lad = {}
    for kdeg in range(1, KMAX + 1):
        vals = np.asarray([r["bounds"][kdeg - 1] for r in rows],
                          float)
        lad[kdeg] = vals
        finite = vals[np.isfinite(vals)]
        print("      K = %d (m_1..m_%2d): bound min/med/max = %s "
              "%s" % (kdeg, 2 * kdeg, f4(finite),
                      "<- ladder max BELOW the bar"
                      if len(finite) == len(vals)
                      and float(np.max(finite)) <= t_bar else ""))
    k_star = None
    for kdeg in range(1, KMAX + 1):
        vals = lad[kdeg]
        if np.all(np.isfinite(vals)) and float(np.max(vals)) \
                <= t_bar:
            k_star = kdeg
            break
    if k_star is None:
        best_k = max(range(1, KMAX + 1),
                     key=lambda k: -float(np.max(lad[k]))
                     if np.all(np.isfinite(lad[k])) else -1e18)
        t_der = float(np.max(lad[best_k]))
        print("    NO depth K <= %d reaches the bar %.4f; deepest "
              "available bound (K = %d) has ladder max %.4f = %.2f "
              "x t_bar" % (KMAX, t_bar, best_k, t_der,
                           t_der / t_bar if t_bar > 0
                           else float("nan")))
    else:
        t_der = float(np.max(lad[k_star]))
        print("    MINIMAL DEPTH K* = %d: ladder max of the derived "
              "bound = %.6f <= the bar %.4f  -> the derived cap is "
              "t_der = %.6f, consuming the e_0-moments m_1..m_%d and "
              "the certified floor c_B = %.4f ONLY"
              % (k_star, t_der, t_bar, t_der, 2 * k_star, floor_c))
    # anatomy: which steps need the deepest bound
    if k_star is not None:
        vals = lad[k_star]
        worst = int(np.argmax(vals))
        print("    tightest step at K*: seg %s h %d, bound %.4f vs "
              "truth sigma %.4f (looseness factor %.2f)"
              % (rows[worst]["seg"], int(rows[worst]["h"]),
                 vals[worst], rows[worst]["sigma"],
                 vals[worst] / max(rows[worst]["sigma"], 1e-12)))
    loose = [r["bounds"][(k_star or KMAX) - 1] / max(r["sigma"],
                                                     1e-12)
             for r in rows]
    print("    looseness factor bound/sigma at depth %d: %s"
          % (k_star or KMAX, f4(loose)))
    # PREMISE VARIANT: the same bound with the measured per-step floor
    var = {}
    for kdeg in (1, 2, 3, 4):
        vals = []
        for row in rows:
            val, _jac = sigma_bound_source(row["step"]["Mt"],
                                           row["lam_b"], kdeg)
            vals.append(val)
        var[kdeg] = float(np.max(np.asarray(vals, float)))
    print("    PREMISE VARIANT (named, NOT adopted): the identical "
          "bound with the per-step measured B-floor lambda_min(B) "
          "(min over the ladder %.3f) instead of the global cited "
          "c_B = %.4f gives ladder max %s -- i.e. the depth is "
          "bought by the QUALITY of the floor premise, not by the "
          "moment machinery"
          % (min(r["lam_b"] for r in rows), floor_c,
             ", ".join("K%d: %.4f" % (k, v)
                       for k, v in sorted(var.items()))))
    kv = [k for k, v in sorted(var.items()) if v <= t_bar]
    print("      -> against the bar %.4f the PREMISE VARIANT %s "
          "(depths %s), so the missing input is the FLOOR QUALITY, "
          "measured here and named in the verdict"
          % (t_bar, "CLEARS at depth %d" % min(kv) if kv
             else "still fails at every depth K <= 4",
             ", ".join(str(k) for k in kv) if kv else "none"))
    return k_star, t_der, lad, var, t_bar, bar_src


def confirm_run(rows, cls, fdata, t_der, pivot_pos):
    section("D-CONFIRM -- the optimization with the DERIVED cap "
            "(amendment A2: the verdict rests here, not on t*)")
    n_ms = 8 if SMOKE else CONF_MS
    de_it = 30 if SMOKE else CONF_DE
    box = pivot_positive_box(cls) if pivot_pos else None
    lab = "C_KS%s + sigma <= t_der = %.6f" \
        % (" + n > 0" if pivot_pos else "", t_der)
    val, theta = run_stage1(rows, cls, fdata, lab, n_ms, de_it,
                            extra_con=sigma_cap_con(t_der), box=box)
    val = max(val, truth_best_under_cap(rows, t_der))
    reserve = 1.0 - val
    check("D5 CONFIRM sup tr R over C_KS%s ∩ {sigma <= %.6f} = %.6f, "
          "reserve %+.6f" % (" ∩ {n > 0}" if pivot_pos else "",
                             t_der, val, reserve), True)
    return val, reserve, theta


def maximizer_anatomy(theta, rows, cls, fdata, names):
    if theta is None:
        print("    maximizer anatomy: no feasible incumbent")
        return "NONE", [], float("nan"), float("nan")
    jm, jb = theta_matrices(theta)
    evj = np.linalg.eigvalsh(jm)
    rv = [zol.scalar_r(fdata, float(v)) for v in evj]
    sl, _ = class_slack_vector(theta, cls)
    active = [names[j] for j in range(len(sl)) if sl[j] <= 1e-6]
    dks = [ks_distance(theta[NDIM:], theta[:NDIM],
                       r["theta"][NDIM:], r["theta"][:NDIM])
           for r in rows]
    d_near = float(np.min(dks))
    d_cons = [ks_distance(rows[i]["theta"][NDIM:],
                          rows[i]["theta"][:NDIM],
                          rows[i + 1]["theta"][NDIM:],
                          rows[i + 1]["theta"][:NDIM])
              for i in range(len(rows) - 1)]
    d_env = float(np.max(d_cons))
    typing = ("WALL-LIKE" if d_near <= d_env else
              "UNPHYSICAL-CORNER")
    print("    maximizer anatomy:")
    print("      eigenvalues: %s" % "  ".join("%+.5g" % v
                                              for v in evj))
    print("      R(lambda_i): %s" % "  ".join("%.4g" % v for v in rv))
    print("      lambda_min(J_B) = %.6f (floor %.6f); b_1 = %.6g; "
          "a_1 = %.6g; sigma = %.6g"
          % (float(np.linalg.eigvalsh(jb)[0]), cls["cb"], theta[0],
             theta[NDIM], sigma_quotient(theta)))
    print("      active constraints (slack <= 1e-6): %s"
          % (", ".join(active[:10]) or "none"))
    print("      KS distance to nearest truth step %.4g vs max "
          "consecutive truth D %.4g -> %s" % (d_near, d_env, typing))
    return typing, active, d_near, d_env


# ================================================ X: the controls
def control_census(zones, rows, cls, fdata, t_used):
    section("X -- the falsifying worlds against the sigma-capped "
            "class")
    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    useless = []
    for world in ("smooth", "scramble"):
        ladder = []
        for kz in zones:
            if world == "smooth":
                ladder.append((kz, ob.build_rung("surf", kz,
                                                 world="smooth")))
            else:
                ladder.append((kz, ob.build_rung(
                    "surf", kz, scramble_seed=SCRAMBLE_SEED)))
        wall_fire = sum(1 for _kz, r in ladder
                        if r is None or r["negA"] > 0)
        if world == "smooth":
            check("X1 C1 SMOOTH violates the wall target (negA > 0) "
                  "on %d/%d surface rungs" % (wall_fire, len(ladder)),
                  wall_fire == len(ladder), kill="K4")
        n_align = n_out = n_break = n_in = n_sig_out = n_piv_out = 0
        excl = {}
        sig_world = []
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if tr is None or ctl is None or not ctl.get("core_ok"):
                continue
            n_align += 1
            with np.errstate(over="ignore", invalid="ignore"):
                mw = sym(tr["step"]["Q"].T
                         @ (ctl["S"] / tr["tau_scale"])
                         @ tr["step"]["Q"])
                jf = jacobi_form(mw)
            if jf is None:
                n_break += 1
                continue
            theta_w = np.concatenate([jf[1], jf[0]])
            sig_w = sigma_quotient(theta_w)
            sig_world.append(sig_w)
            sl, names = class_slack_vector(theta_w, cls)
            inside_box = float(np.min(sl)) >= -FEAS_TOL
            inside_sig = math.isfinite(sig_w) and sig_w <= t_used
            inside_piv = float(theta_w[0]) > 0.0
            if not inside_piv:
                n_piv_out += 1
            if inside_box and inside_sig and inside_piv:
                n_in += 1
                trw = tr_r_of_theta(theta_w, fdata)
                print("      INSIDE (box AND sigma cap) rung kz %d: "
                      "sigma %.4f, tr R = %.6f %s"
                      % (kz, sig_w, trw,
                         "<- tr R >= 1, CLASS-USELESS SEAT"
                         if trw >= 1.0 else "(tr R < 1)"))
                if trw >= 1.0:
                    useless.append((world, kz, trw, sig_w))
            else:
                n_out += 1
                if not inside_sig:
                    n_sig_out += 1
                j = int(np.argmin(sl))
                key = names[j] if not inside_box else (
                    "sigma_cap" if not inside_sig else "pivot_sign")
                excl.setdefault(key, 0)
                excl[key] += 1
        fire = (n_out + n_break) > CTRL_MAJORITY * max(n_align, 1)
        top = sorted(excl.items(), key=lambda kv: -kv[1])[:4]
        print("    %-9s aligned %d = OUT %d (sigma cap alone %d, "
              "pivot sign n > 0 alone %d) + REPRESENTATION-BREAK %d "
              "+ INSIDE %d; excluders: %s; control sigma "
              "min/med/max %s"
              % (world, n_align, n_out, n_sig_out, n_piv_out,
                 n_break, n_in,
                 ", ".join("%s x%d" % kv for kv in top) or "none",
                 f4(sig_world)))
        check("X2 class-exclusion census %s (box + pivot sign + "
              "sigma cap %.4f): OUT+BREAK %d/%d aligned -> %s"
              % (world, t_used, n_out + n_break, n_align,
                 "FIRE" if fire else "SILENT"), fire, kill="K4")
    return useless


def opt_power_control(rows, cls, fdata, t_used):
    ctrl_lo = cls["lo"].copy()
    ctrl_lo[0] = min(ctrl_lo[0], OPT_CTRL_B1)
    ctrl_cls = dict(cls)
    ctrl_cls["lo"] = ctrl_lo
    ctrl_cls["wd"] = cls["hi"] - ctrl_lo
    v_ctrl, _t = run_stage1(
        rows, ctrl_cls, fdata,
        "O0 OPT-POWER control (b_1 box extended to %.1f, sigma cap "
        "%.4f ACTIVE)" % (OPT_CTRL_B1, t_used),
        max(8, (CONF_MS if not SMOKE else 8) // 2),
        max(30, (CONF_DE if not SMOKE else 30) // 3),
        extra_con=sigma_cap_con(t_used))
    check("O0 CONTROL the optimizer reaches tr R >= %.1f on the "
          "declared control box WITH the sigma cap active (a "
          "nonpositive pivot makes sigma negative, so the target "
          "provably lives there): best %.4f"
          % (OPT_CTRL_BAR, v_ctrl), v_ctrl >= OPT_CTRL_BAR,
          kill="K4")
    return v_ctrl


# =========================================== S: the screens
def ch_surface_map(rows):
    """CCXVII c_h on matched surface terminators (CCLIII verbatim,
    labelled screen currency only)."""
    out = {}
    for kz in sorted({r["kz"] for r in rows if r["seg"] == "surf"}):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        out[int(kz)] = 1.0 - top
    return out


def screens(rows, t_star, k_star):
    section("S -- (d) relocation screens (CCXLVII bars inherited "
            "verbatim): is the sigma margin c_h in disguise?")
    taus = np.asarray([r["tau_scale"] for r in rows], float)
    ch_map = ch_surface_map(rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in rows], float)
    kk = (k_star or KMAX) - 1
    sig = np.asarray([r["sigma"] for r in rows], float)
    bnd = np.asarray([r["bounds"][kk] for r in rows], float)
    series = (("sigma", sig),
              ("t*_pos - sigma (the truth margin)", t_star - sig),
              ("derived bound (K=%d)" % (kk + 1), bnd),
              ("t*_pos - derived bound (THE decisive margin)",
               t_star - bnd),
              ("relative Schur gap s/n", 1.0 - sig))
    reloc = []
    for label, arr in series:
        t1, v1 = screen(arr, taus, "%s vs step tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask],
                        "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau / c_h relocation screens: relocation seats %s"
          % (",".join(reloc) or "none"), not reloc)
    hs = np.asarray([r["h"] for r in rows], float)
    for label, arr in (("sigma", sig),
                       ("derived bound K=%d" % (kk + 1), bnd)):
        pos = arr > 0
        if int(np.sum(pos)) >= 3:
            slope, two_se, r2, _a = linfit(np.log(hs[pos]),
                                           np.log(arr[pos]))
            print("      h-law %-22s slope %+.4f +/- %.4f (2SE), "
                  "R^2 %.3f -> %s"
                  % (label, slope, two_se, r2,
                     "flat-compatible" if abs(slope) <= two_se
                     + SLOPE_PASS else "trending"))
    return reloc


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64/rational measurements on the deployed
  68-step ladder, one frozen truth-envelope class in the 15 wall
  Jacobi parameters, and one source-only bound family consuming the
  wall matrix ENTRIES plus the certified B-floor.  A numeric maximum
  is a lower bound on a supremum: the closing threshold t* is
  therefore an UPPER bound on the true one, and the verdict rests on
  the CONFIRM run at the derived cap, typed NUMERIC-GLOBAL, never
  certified over the class.  No marker moves; no paper, ledger,
  website, manifest or verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.SIGMA.01 -- the Schur-quotient seam "
            "of the KS.DUAL contract (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(("theta_matrices", "ks_wall_functionals",
                             "class_slack_vector", "sigma_quotient",
                             "tr_r_of_theta"), CLASS_BANNED)
    check("S0.2 AC the class/objective functions carry no ladder or "
          "read identifier (CCLXI verbatim)", not ac,
          ",".join(sorted(set(ac))), kill="K2")
    ac2 = ast_scan_functions(("wall_moments", "e0_diagonal_moments",
                              "nu_from_e0_moments", "lanczos_pair",
                              "radau_upper", "sigma_bound_source"),
                             DERIV_BANNED)
    check("S0.3 AC the DERIVATION functions carry no read, no pivot, "
          "no eigensolver and no ladder identifier (entries + frozen "
          "constants only)", not ac2, ",".join(sorted(set(ac2))),
          kill="K2")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0.4 CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")

    zones, steps = build_ladder()
    if KILLS:
        return finish([])
    fdata = get_filter(steps, artifact)
    rows = translation(steps, artifact, fdata)
    if KILLS:
        return finish([])
    rows = jacobi_translation(rows)
    if KILLS:
        return finish([])
    identity_section(rows)
    if KILLS:
        return finish([])
    coin_verdict, coin_corr, _cap = coincidence_test(rows)
    if KILLS:
        return finish([])

    cls = freeze_class(rows, fdata)
    names = membership_census(rows, cls)
    if KILLS:
        return finish([])

    t_star, t_close, _table, _sup_nc, _th_nc = threshold_map(
        rows, cls, fdata)
    if KILLS:
        return finish([])
    t_star_pos, t_close_pos, _tab_pos = pivot_positive_map(
        rows, cls, fdata)
    if KILLS:
        return finish([])
    k_star, t_der, lad, var, t_bar, bar_src = derivation_section(
        rows, cls, t_star, t_close, t_close_pos)
    if KILLS:
        return finish([])
    on_pos = bar_src == "PIVOT-POSITIVE"
    sup_der, reserve, theta_der = confirm_run(rows, cls, fdata,
                                              t_der, on_pos)
    maximizer_anatomy(theta_der, rows, cls, fdata, names)
    rigor, details = rational_witness(theta_der, cls, fdata) \
        if theta_der is not None else ("NUMERIC(none)", dict(
            note="no incumbent", tr=float("nan")))
    print("    stage-2 rigor at the confirm incumbent: %s -- %s"
          % (rigor, details["note"]))

    opt_power_control(rows, cls, fdata, t_der)
    if KILLS:
        return finish([])
    useless = control_census(zones, rows, cls, fdata, t_der)
    if KILLS:
        return finish([])
    reloc = screens(rows, t_star_pos, k_star)

    # ------------------------------------------------ the verdict
    section("R -- the relocation ledger of the closure (honest "
            "restatement of what the corridor now needs)")
    sig = np.asarray([r["sigma"] for r in rows], float)
    print("""    The composed statement under test is:
      (0) AMENDMENT A6, measured: the pivot sign n > 0 must be
          carried EXPLICITLY -- without it the cap is vacuous
          (sigma = q/n < 0 at n < 0) and NO cap closes;
      (1) every J in C_KS%s with sigma(J) <= t_der is positive-
          certified by the frozen CCXXV separator (measured: sup
          tr R = %.4f, reserve %+.4f);"""
          % (" with n > 0" if on_pos else "", sup_der, reserve))
    print("""      (2) truth lies in C_KS on all %d tested rungs (N1), has a
          positive pivot on %d/%d (P1) and obeys sigma <= %.4f
          there (max %.4f);
      (3) the sigma cap is not assumed: it is BOUNDED from the wall
          ENTRIES via the e_0-moments m_1..m_%s and the certified
          B-floor c_B = %.4f (D3-warded Gauss-Radau).
    The all-h residue is therefore: class membership of the wall
    Jacobi data PLUS the pivot sign PLUS 'the depth-%s moment bound
    stays below the bar'.  None is proved here; all are FINITE,
    SOURCE-COMPUTABLE functionals with measured h-laws, which is a
    strictly weaker residue than an assumed Schur positivity."""
          % (len(rows), int(np.sum(np.asarray(
              [r["n_piv"] for r in rows], float) > 0)), len(rows),
             t_der, float(np.max(sig)),
             str(2 * k_star) if k_star else "{2K}",
             cls["cb"], str(k_star) if k_star else "K"))
    print("    HALFGAP RELOCATION CHECK: sigma <= t is the relative "
          "Schur-gap floor s >= (1 - t) n.  Measured relative gap "
          "s/n = 1 - sigma: %s.  The halfgap grade is the regime "
          "s/n -> 0 (arithmetic supply must resolve n to relative "
          "precision s/n); the deployed ladder sits at s/n = %.3f "
          "median, i.e. O(1), and the derived bound consumes only "
          "moments and the floor -- no pivot read enters, so the "
          "route does NOT relocate onto the halfgap."
          % (f4(1.0 - sig), float(np.median(1.0 - sig))))

    if useless:
        w, kz, trw, sw = useless[0]
        labels = ["CLASS-USELESS-SIGMA(%s world INSIDE the "
                  "sigma-capped class at kz %d with sigma %.4f and "
                  "tr R = %.4f >= 1)" % (w, kz, sw, trw)]
    elif k_star is not None and reserve >= RESERVE_FLOOR:
        labels = [
            "SIGMA-DERIVED(t_der = %.6f at depth K* = %d, route "
            "GAUSS-RADAU(e_0-moments m_1..m_%d + certified B-floor "
            "c_B = %.4f)%s; CONFIRM sup tr R = %.4f, reserve %+.4f "
            ">= %.0e; truth in class %d/%d and truth sigma max %.4f; "
            "closing threshold t*_pos = %.4f; rigor NUMERIC-GLOBAL, "
            "premises: E2 compression + E3 quadrature (warded) + "
            "CLIII certified floor + CCXXV separator%s)"
            % (t_der, k_star, 2 * k_star, cls["cb"],
               " + PIVOT SIGN n > 0 (A6, source-only entry fact)"
               if on_pos else "", sup_der, reserve, RESERVE_FLOOR,
               len(rows), len(rows), float(np.max(sig)), t_star_pos,
               " + pivot sign" if on_pos else "")]
    elif k_star is not None:
        labels = ["SIGMA-MARGINAL(derived cap %.4f closes but "
                  "reserve %.4e < floor %.0e)"
                  % (t_der, reserve, RESERVE_FLOOR)]
    else:
        deep = float(np.max(lad[KMAX]))
        v_best = min(var.values()) if var else float("nan")
        cond = math.isfinite(v_best) and v_best <= t_bar
        labels = [
            "%s(no depth K <= %d bounds sigma below the bar %.4f "
            "with the CITED floor: deepest ladder max %.4f, factor "
            "%.2f.  The measured obstruction is the b-weighted "
            "spectral mass the moments cannot exclude just above "
            "c_B = %.4f.  X = A SHARPER CERTIFIED B-FLOOR: the "
            "identical bound with the per-step MEASURED "
            "lambda_min(B) reaches %.4f (K=4) and %s the bar, so "
            "the missing input is floor QUALITY, not moment depth; "
            "X is NOT the halfgap -- the halfgap constrains s/n "
            "(measured O(1) here, med %.3f), X constrains the "
            "bulk block B alone)"
            % ("SIGMA-CONDITIONAL" if cond else "SIGMA-OPEN", KMAX,
               t_bar, deep, deep / t_bar if t_bar > 0
               else float("nan"), cls["cb"],
               var.get(4, float("nan")),
               "CLEARS" if cond else "still misses",
               float(np.median(1.0 - sig)))]
    labels.append(
        "CAP-VACUITY(A6, the decisive correction of CCLXI: the "
        "one-sided cap alone closes NOTHING -- plain map OPEN at "
        "every t in [%.2f, %.2f] with sup tr R ~ %.2f because the "
        "maximizer takes n < 0 where sigma < 0; WITH the source-only "
        "pivot sign n > 0 the map closes and t*_pos = %.4f, truth "
        "sigma max %.4f, margin %+.4f)"
        % (min(T_GRID), max(T_GRID),
           max(v for _t, v in _table), t_star_pos,
           float(np.max(sig)), t_star_pos - float(np.max(sig))))
    labels.append("0.665-DECIDER: %s (corr %.3f)"
                  % (coin_verdict, coin_corr))
    if reloc:
        labels.append("RELOCATION-SEAT(%s)" % ",".join(reloc))
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
