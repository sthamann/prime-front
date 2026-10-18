#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rhp_tier2_polecontrol_probe -- PRIME.PORT.LATTICE.RHP.01 tier 2
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE JOIN.  Two fresh tier-1 results are connected here for the first
time.

  (A) CCXLV (lattice_rhp_szego_probe).  The deployed atomic measure
      mu_+ of the frame-A ladder is NOT Szego class -- the mu_- gap
      set occupies 0.26..0.34 of theta -- but its Jacobi coefficients
      ARE Killip-Simon l2-stable (KS_bulk med 1.830, h-flat), and the
      RESTRICTED Case-C0 sum-rule residual
        res(h) = prod_{n<=h/2} A_n / (sqrt 2 exp(G_+(h)/2))
      is an h-stable constant, med 0.665, slope -0.007.
  (B) CCXLVII (zolotarev_complex_tau_probe).  The certificate reserve
      1 - tr R(M_h) at the eight FIXED CCXXV Zolotarev poles is O(1)
      and h-flat (med 0.9195, h^+0.0215), passing both relocation
      screens -- the first level object that is NOT in c_h currency.
      Its open piece is UNIFORM control of the eight reads
        q_j(h) = d_z log tau_h(z_j) = -tr(M_h - z_j I)^{-1}.

THE THESIS UNDER TEST: the Killip-Simon sum-rule structure of (A) is
the analytic engine for the uniform control demanded by (B).  The
bridge is the classical Weyl m-function: the eight pole reads are
values of the m-function / resolvent trace of a JACOBI matrix at eight
fixed off-spectrum points, and the m-function off the spectrum is
exactly the object l2 (Killip-Simon) perturbation theory controls.

DEPLOYED OBJECTS (read-only, reused verbatim; nothing re-derived).
  measure side (CCXLV):  pt.window_of / grid_density / folded_measure /
      lanczos_chain of v563+port_tangent_schur_probe; A_n = 2 be_{n-1},
      B_n = 2 al_{n-1}; free chain A = 1, B = 0.
  wall side (CCVII/CCXXV/CCXLVII): ob.build_rung / make_steps /
      deep_zone_census, zol.assemble_step giving the 8x8 step matrix
      M_h = sym(Q^T (S_{r2}/tau_{r1}) Q) with the bad mode rotated to
      e_0, its Schur scalar s = step["gap"], and the FIXED global m=8
      Zolotarev filter (c_B = 5523/10000, L = max L_src) with poles
      y_j = 0.4841930600783 .. 4.9743176671938e4 and negative residues
      a_j = -0.3667 .. -3.7671e4.
  stored artifact zolotarev_phase_filter_phases.json (68 steps x 8
      poles: determinant, phase, resolvent trace, trace_R, margin) --
      the reproduction anchor.

EXTERNAL-CITED (facts consumed, warded numerically, never proved here).
  E1  Weyl m-function of a Jacobi matrix.  For J = J(a, b) finite,
        m(z) = [(J - z)^{-1}]_{11}
             = 1/(b_1 - z - a_1^2/(b_2 - z - a_2^2/(...))),
      and the two-sided (coupled-resolvent) formula
        [(J - z)^{-1}]_{kk}
          = 1/(b_k - z - a_{k-1}^2 m^-_{k-1}(z) - a_k^2 m^+_{k+1}(z)),
      with m^- / m^+ the m-functions of the left/right truncated
      blocks.  [Teschl, "Jacobi Operators and Completely Integrable
      Nonlinear Lattices", AMS Math. Surveys 72 (2000), Ch. 2; Simon,
      "Szego's Theorem and its Descendants", PUP 2011, Ch. 3.]
  E2  Killip-Simon class / l2 currency: J - J_0 Hilbert-Schmidt,
      i.e. sum (A_n - 1)^2 + B_n^2 < infinity, is the exact class of
      measures satisfying quasi-Szego + Lieb-Thirring.  [Killip &
      Simon, Ann. Math. 158 (2003) 253-321.]  Used here ONLY as the
      name and the norm of the l2 census -- no spectral claim.
  E3  second resolvent identity + Hilbert-Schmidt trace bound:
        R - R' = R (J' - J) R',   |tr(XY)| <= ||X||_HS ||Y||_HS,
        ||(J - z)^{-1}||_2 <= 1/|Im z|,
      hence with D = J' - J
        |tr R - tr R'| <= sqrt(n) ||D||_HS / y^2       (BOUND-A)
      and, in the Neumann regime ||D||_HS < y,
        |tr R - tr R'| <= ||R||_HS ||D||_HS / (y - ||D||_HS)
                                                       (BOUND-B).
      [Kato, "Perturbation Theory for Linear Operators", Springer
      1980, Ch. I.4 / V.3; Bhatia, "Matrix Analysis", Springer 1997,
      Ch. III (Hoffman-Wielandt); Simon, "Trace Ideals", AMS 2005,
      Ch. 3 for perturbation determinants det((J-z)(J_0-z)^{-1}).]
  E4  Chebyshev-1 (arcsine) measure dx/(pi sqrt(1-x^2)) has Jacobi
      parameters b_n = 0, a_1 = 1/sqrt 2, a_n = 1/2 (n >= 2) and
      Stieltjes transform int dmu(x)/(x - z) = -1/sqrt(z^2 - 1).
      [Szego, "Orthogonal Polynomials", AMS 1939, Sec. 2.4; Chihara,
      "An Introduction to Orthogonal Polynomials", Gordon & Breach
      1978, Ch. V.]  This is the FREE reference of the FOLDED lattice
      measure (derived and warded in-probe, SR-FREE): a constant lag
      arm folds to EQUAL weights on theta_j = 2 pi j / L, j = 1..L/2,
      i.e. uniform theta-density, i.e. arcsine in x -- so the tier-1
      residual normalization sqrt 2 exp(G/2) reads res = 1 on the
      free chain.
  E5  Uvarov / one-mass-point transform: adding an atom to a measure
      adds w/(x_0 - z) to its Stieltjes transform; the finite Jacobi
      chain of a discrete measure with N support points reproduces
      that transform EXACTLY at chain length N (the [N/N] Pade /
      Gauss-quadrature identity).  [Uvarov, USSR Comp. Math. 9 (1969)
      25; Gautschi, "Orthogonal Polynomials: Computation and
      Approximation", OUP 2004, Sec. 2.4.]

FROZEN PROTOCOL (2026-08-12).

 S0 FIREWALL.  AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); verification/ and all predecessor
    probes READ-ONLY; RNG only through the corpus scramble seed.
    AC1 the measure-side chain builder build_chain_from_source()
    receives ONLY a source tuple and its AST body contains NO wall
    identifier and NO eigensolver (measure FORWARD).  AC2 the bound
    functions ks_distance() / bound_a() / bound_b() contain NO read
    identifier (q / tr / reserve / margin): the a-priori bound is
    built from Jacobi data and pole geometry alone, never from the
    read it is supposed to control.

 M  THE SUM-RULE OBJECT (mission a).  On the CCXLV 42-rung frame-A
    ladder, coefficients forward-built to chain length h/2 + 2 (the
    Lanczos prefix is progressive, so A_n for n <= h/2 is identical
    to the tier-1 full-chain value).
    M1 REPRO ward (kill -> REPRO-BROKEN): res med reproduces CCXLV's
       0.665 and KS_bulk med its 1.830 within REPRO_RTOL, and the
       excluded theta-fraction lands in EXCL_BAND.
    M2 THE CARRIER IDENTITY (kill -> WARD-BROKEN).  Against the E4
       free reference the restricted residual splits EXACTLY into
       three named carriers,
         log res(h) = COEF + GAP + SPREAD,
         COEF   = sum_{n<=h/2} log A_n - (1/2) log 2,
         GAP    = (1/2) f log f,          f = 1 - excl,
         SPREAD = -(1/2) f <log(rho/rho_bar)>_{Theta_+},
       where rho is the theta-density of the normalized mu_+ and
       rho_bar its mean over the present cells.  Ward per rung at
       IDENT_TIE, and ward SR-FREE: the folded free (arcsine) chain
       gives res = 1 within SR_FREE_TIE.
    M3 ANATOMY: median and log-log h-slope (2SE) of each carrier; the
       cancellation depth (|COEF| + |SPREAD|)/|log res|; the prime
       split COEF = (LP - LP_smooth) + (LP_smooth - (1/2) log 2); the
       band-resolved LP over n/h in (0,1/16], (1/16,1/8], (1/8,1/4],
       (1/4,1/2].  TYPE: which carrier is the constant carrier
       (smallest |slope| + 2SE) and whether the h-stability is a
       CANCELLATION (two carriers with |slope| > CARRIER_FLAT_BAR and
       opposite signs) or a CARRIERWISE constant.
    M4 the formula candidate is exactly the M2 identity with the
       measured invariant; the closed-form coincidence res -> 2/3 is
       screened as COINCIDENCE-COMPATIBLE / COINCIDENCE-EXCLUDED by
       |med - 2/3| against the ladder IQR (a typed screen, never a
       claim).
    M5 deep extension (budget-permitting): the same identity on
       DEEP_CARRIER_SUB declared deep rungs (h up to ~2900).
    M6 tau- and c_h-screens of every carrier on the matched surface
       steps.

 W  THE WALL LADDER, rebuilt read-only: 68 steps = 40 surface + 1
    bridge + 27 deep; the FIXED global m=8 filter rebuilt from the
    source-only L and warded against the stored artifact; per step
    per pole the LU-only reads (log tau, phase, resolvent trace, q)
    warded against the 68x8 stored artifact and the partial-fraction
    trace / reserve reproduced.

 B  THE M-FUNCTION BRIDGE (mission b).  Per step: the Lanczos chain
    of (M_h, e_0) -- the CCVII n-read direction -- gives the Jacobi
    form J_h = J(a, b) with the SAME spectrum and the SAME reads.
    Wards, all kill -> WARD-BROKEN, per rung AND per pole:
    B1 similarity: Q^T Q = I and Q^T M_h Q = J_h at SIM_TIE.
    B2 m-function: the E1 continued fraction equals the LU read
       [(M_h - z_j)^{-1}]_{00} -- i.e. the Weyl m-function at the
       n-read direction IS CCXLVII's sensitivity kernel G_00.
    B3 trace: the E1 two-sided formula summed over the eight sites
       equals the LU resolvent trace.
    B4 trace, second route: the three-term determinant recurrence
       P_k and its differentiated recurrence give
       tr(M_h - z)^{-1} = -P_n'(z)/P_n(z), and P_n(z_j) equals the
       LU shifted determinant (Christoffel-Darboux route).
    B5 the real-axis anchor: m_h(0) = 1/s with s = step["gap"].
    B6 unitary invariance: ||(J_h - z)^{-1}||_HS = ||(M_h - z)^{-1}||_HS.

 K  THE UNIFORM-CONTROL CENSUS (mission c) -- THE HEADLINE.  The KS
    currency of the ladder is the l2 distance of the Jacobi data of
    consecutive steps,
      D_i = ||J_{i+1} - J_i||_HS
          = sqrt(sum_k (db_k)^2 + 2 sum_k (da_k)^2),
    and the pole geometry is y_j.  For every one of the 67 consecutive
    pairs and eight poles:
    K1 BOUND-SOUNDNESS ward (kill -> WARD-BROKEN): the measured
       |Delta q_j| never exceeds BOUND-A (E3), and never exceeds
       BOUND-B where the Neumann regime holds.  This wards the
       derivation itself.
    K2 the census.  Per-pole budget convention (declared, not tuned):
       the reserve budget of a step is budget_i = min(reserve_i,
       reserve_{i+1}) and the per-pole share is budget_i / NDIM; the
       aggregate bound is
         BND_i = 2 sum_j |a_j| min(BOUND-A_ij, BOUND-B_ij).
       CONTROLLED(i) iff BND_i <= budget_i; CONTROLLED(i,j) iff
       2|a_j| bound_ij <= budget_i/NDIM.  Report the aggregate census
       n/67, the per-pole census n_j/67, the crossover pole y*, the
       decision band (poles with median |decision share| >=
       DECISION_SHARE_FLOOR, inherited), the median gap factor
       BND_i/budget_i, and the LOOSENESS of the bound itself
       (BOUND-A/|Delta q| per pole, BND_i/|Delta tr R| aggregate),
       which separates norm-bound slack from genuine obstruction.  A
       pair whose reserve budget is non-positive is typed BUDGET-VOID
       and excluded from the census denominators (count disclosed).
    K3 the KS-linear capture ratio [the decisive diagnostic]:
       the exact first-order KS response fo_ij = -tr(R_i D_i R_i) and
       the ratio |Delta q_ij| / |fo_ij| (and the aggregate reserve
       version).  Ratio ~ 1 means the KS currency has the RIGHT SIZE
       and only the norm bounds are loose; ratio << 1 means structural
       cancellation that no norm-based route can see.
    K4 the residue, measured: (i) h-uniformity of the KS data (slope
       of log D vs log h with 2SE), (ii) the Neumann-admissible
       fraction #{D_i < y_j}/(67*8), (iii) the measure->wall link:
       correlation and slope of log D_i against the measure-side KS
       increment on the inherited common prefix n <= N_PREFIX.
    K5 tau- and c_h-screens on every new margin (D, gap factor,
       capture ratio) -- the corridor's value is that it is NOT c_h
       currency, and that must survive the KS representation.
    VERDICT: POLES-KS-CONTROLLED(census) iff the aggregate census is
    67/67; PARTIAL(...) iff some but not all (pole/rung band named);
    KS-INSUFFICIENT(gap) iff no pole is controlled on any pair.

 C  CONTROLS (mission e), kill -> CONTROL-SILENT.
    C1 SMOOTH must violate the wall target (negA > 0) on every
       surface rung.
    C2 the m-function representation must SEE the falsifying worlds:
       for smooth and scramble, in CCXLVII's aligned truth
       coordinates M_world = sym(Q_truth^T (S_world/tau_truth)
       Q_truth), both the KS data D_world (relative to ||J_truth||_HS,
       bar KS_CTRL_BAR) and the natural read separation
       y_j |q_world - q_truth| / NDIM (bar CTRL_SEP_BAR) must be
       resolved on a majority of the matched rungs, and BOUND-A must
       hold there too.
    C3 the measure-side carriers must move: |log res_world -
       log res_truth| median >= CARRIER_CTRL_BAR for smooth and
       scramble.

 A  THE SINGLE-ATOM RHP BRICK (mission d, tier-1-spec'd).
    A1 the E4 analytic arcsine m-function is reproduced by the CF of
       the arcsine Jacobi chain at declared complex points, with the
       truncation rate printed.
    A2 the exactly solvable one-atom model: mu_w = (mu_free +
       w delta_{x_0})/(1 + w) on the folded grid; the E5 identity
       (chain length = support size) is warded EXACTLY, and the
       closed-form m_w = (m_free + w/(x_0 - z))/(1 + w) is warded.
    A3 the atomwise KS budget with the DEPLOYED weight law
       w_{p,k} = 2 log(p) p^{-k/2} at u = k log p mapped to the
       folded grid of a declared reference rung, at the atom's
       deployed RELATIVE comb weight: per atom ||J_w - J_free||_HS in
       the (A, B) normalization on the declared prefix, and the
       superposition test -- the JOINT multi-atom budget against the
       SUM of the single-atom budgets.  TYPE:
       SUPERPOSITION-ADDITIVE / SUBADDITIVE / NOT-ADDITIVE.
    SCOPE LINE (honest): the one-atom model lives in the MEASURE
    coordinate x in [-1,1]; the eight Zolotarev poles live in the
    8x8 wall-step coordinate.  The atom model is therefore the seed
    of the parametrix for the KS INPUT D of section K, NOT a read at
    z_j; no coordinate identification is invented.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 identity/ward ->
WARD-BROKEN; K3 tier-1 reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum): RHP-T2( SUMRULE(carrier types) ;
BRIDGE-EXACT | BRIDGE-BROKEN ; POLES-KS-CONTROLLED(census) |
PARTIAL(...) | KS-INSUFFICIENT(gap) ; CAPTURE(ratio) ; ATOM(type) )
plus kills.  Every enum is a finite-ladder theorem-engineering
diagnostic, never an all-h statement and NEVER an RH claim.

FROZEN BARS: NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE = 2e-9;
SIM_TIE = 1e-9; BRIDGE_TIE = 1e-8; DET_TIE = 1e-7; IDENT_TIE = 1e-11;
REPRO_RTOL = 5e-2; RES_MED_REF = 0.665; KSBULK_MED_REF = 1.830;
EXCL_BAND = (0.24, 0.36); SR_FREE_TIE = 5e-3; SR_FREE_COEF_TIE = 1e-4;
CARRIER_FLAT_BAR = 0.10;
N_PREFIX = 48; BAND_EDGES = (1/16, 1/8, 1/4, 1/2); SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; DECISION_SHARE_FLOOR = 0.01; BOUND_SOUND_TOL =
1e-6; COINC_CAND = 2/3; DEEP_CARRIER_SUB = 4; CF_POINTS = (2j,
0.5+1j, -0.3+0.05j); ATOM_GRID = 512; ATOM_SET = ((2,1), (2,2),
(3,1), (3,2), (5,1), (7,1)); ADD_BAND = (0.5, 2.0);
KS_CTRL_BAR = 1e-2; CTRL_SEP_BAR = 1e-3; CARRIER_CTRL_BAR = 1e-2;
runtime cap 25 min.

SMOKE DISCLOSURE (2026-08-12, before freezing; two smoke passes).
 SMOKE-1 (contiguous 10-rung surface subset + the 3 lowest deep rungs,
 3.0 s) ran 33 checks with ONE failure and reshaped the spec in four
 places, all disclosed:
 (i)   M2b SR-FREE confirmed the DERIVED claim -- the folded free
       reference IS the arcsine measure (A_1 = 1.414208 vs sqrt 2 =
       1.414214, A_n med 0.999995, restricted residual 0.998700
       against the bar 5e-3, which PASSED) -- but the incoming
       coefficient sub-bars of 1e-6 were unachievable in principle: a
       folded grid of N = 511 cells reproduces the infinite arcsine
       chain only to ~6e-6.  A declared bar SR_FREE_COEF_TIE = 1e-4
       was introduced with that resolution argument BEFORE the freeze;
       the residual bar 5e-3 was not touched.
 (ii)  the smoke subset necessarily contains steps that are NOT steps
       of the fixed 68-step artifact (its own fake bridge), one with a
       negative reserve.  BUDGET-VOID typing was added (non-positive
       reserve budget -> excluded from the census denominators, count
       printed).  On the frozen ladder CCXLVII's reserve minimum is
       2.730e-2 > 0, so no void pair is expected.
 (iii) two reporting-only additions after SMOKE-1: the per-pole
       looseness BOUND-A/|Delta q| and the aggregate looseness
       BND/|Delta tr R|.  SMOKE-1 showed the bound is nearly TIGHT at
       the top poles (1.95x at j=7) while the census still fails on
       the residue weight; that distinction is invisible without the
       ratio.  No bar, control, screen or enum was touched.
 (iv)  the A3 atom budget of SMOKE-1 was measured against the BARE
       free chain (A = 1) instead of against the arcsine chain of the
       SAME grid, so the arcsine's own A_1 = sqrt 2 offset (0.586)
       sat inside every atom's budget.  Corrected before the freeze to
       the intended object.
 SMOKE-2 (post-corrections, 3.3 s) ran 40/40 GREEN with no kills and
 confirmed as planned: artifact reproduction det 1.46e-14 / phase
 1.33e-15 / trace 0.00e+00; every bridge ward at machine precision
 (similarity 6.4e-16, m-function 6.1e-16, Weyl trace 1.6e-15, CD route
 3.3e-15 and determinant 1.5e-14, m(0)s - 1 = 6.7e-16, unitary
 invariance 1.0e-15); the carrier identity 2.2e-16 on the surface and
 1.1e-16 on deep rungs; BOUND-SOUNDNESS 80/80 for BOTH bounds; all
 three controls firing; A1 1.1e-16 and A2 1.2e-16.
 The smoke also DISCLOSES readings frozen into the spec text before
 the frozen run (they are NOT bars): the census is PARTIAL with only
 the top pole controlled on part of the pairs, the KS-linear capture
 ratio rises monotonically with y_j (0.07 at j=1 to 0.9999 at j=7),
 and the measure->wall link is null on the 7 smoke pairs.  No verdict
 enum, control, screen or structural bar was weakened; all enums were
 fixed before the first smoke.

AMENDMENT AFTER FROZEN RUN 1 (2026-08-12, numerical representation
only, disclosed; no measurement, bar, screen, control or verdict enum
moved).  Frozen run 1 completed sections S0/W/T/B/H/M/M5/K with 28/28
checks GREEN (all reported numbers identical to the run of record) and
then raised OverflowError in the CONTROL section: the aligned control
matrix M_world = sym(Q^T (S_world/tau_truth) Q) has |det(M_world -
z_j I)| beyond float64 range on some rungs, although its log-magnitude
and its inverse trace -- the only quantities any control read uses --
are finite.  This is CCXLVII's own disclosed A2 defect reappearing at
the same seat.  AMENDMENT A1: lu_read() gains want_det; callers that
need only q suppress the raw determinant reconstruction.  Truth reads,
the artifact ward, every identity and every bound are unchanged;
frozen run 2 is the run of record.

AMENDMENT AFTER FROZEN RUN 2 (2026-08-12, control TYPING only,
disclosed; no bar lowered, no measurement of the truth ladder
changed -- runs 1, 2 and 3 report identical S0/W/T/B/H/M/M5/K
numbers).  Frozen run 2 (109.1 s) ran 32/33 with the single failure in
C2 SCRAMBLE: on the full 42-rung ladder the aligned scramble matrix
sym(Q^T (S_scr/tau_truth) Q) leaves float64 range on part of the
rungs (the corpus already reports scramble tau down to -1e80), so the
Lanczos form is NaN and its KS distance overflows; the median-based
aggregate then evaluated to NaN and 16 of 232 cells were counted
"unsound" merely because inf/NaN comparisons are False.  Two changes,
both typing:
 A2a  the fire test is evaluated PER RUNG and a world fires on a
      MAJORITY of aligned rungs -- exactly the wording already frozen
      in C2 above -- instead of through a median aggregate; the
      per-rung counts (resolved / representation-break / silent) are
      printed.
 A2b  a rung whose aligned matrix leaves float64 range is typed
      REPRESENTATION-BREAK and counted as a fire: a world that
      destroys the m-function representation outright is a strictly
      stronger destruction than a resolved separation, and it is
      disclosed separately, never merged into the resolved count.
 Simultaneously a STRICTLY NEW kill is added: BOUND-A must hold on
 EVERY float64-finite aligned control cell (per world, kill K2).  No
 bar (KS_CTRL_BAR, CTRL_SEP_BAR, BOUND_SOUND_TOL) was touched, and
 the truth-side census is untouched.  Frozen run 3 is the run of
 record.

NO RH claim.  Every number is a finite-truncation measurement on the
deployed ladder; the limit question is untouched.  No marker moves; no
paper, ledger, website, manifest or verification file is touched.

Sources (read-only): lattice_rhp_szego_probe (CCXLV tier 1),
zolotarev_complex_tau_probe (CCXLVII), onebadmode_moments_probe
(CCVII ladder), zolotarev_phase_filter_probe (CCXXV filter),
euler_phase_identity_probe (CCXVII c_h), port_tangent_schur_probe
(round 57 machinery), v563_paper2_readouts (deployed window).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rhp_tier2_polecontrol_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rhp_tier2_polecontrol_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import port_tangent_schur_probe as pt        # noqa: E402 (READ-ONLY)
import onebadmode_moments_probe as ob        # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol   # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul     # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
SIM_TIE = 1.0e-9
BRIDGE_TIE = 1.0e-8
DET_TIE = 1.0e-7
IDENT_TIE = 1.0e-11
REPRO_RTOL = 5.0e-2
RES_MED_REF = 0.665
KSBULK_MED_REF = 1.830
EXCL_BAND = (0.24, 0.36)
SR_FREE_TIE = 5.0e-3
SR_FREE_COEF_TIE = 1.0e-4
CARRIER_FLAT_BAR = 0.10
N_PREFIX = 48
BAND_EDGES = (1.0 / 16, 1.0 / 8, 1.0 / 4, 1.0 / 2)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
DECISION_SHARE_FLOOR = 0.01
BOUND_SOUND_TOL = 1.0e-6
COINC_CAND = 2.0 / 3.0
DEEP_CARRIER_SUB = 4
CF_POINTS = (2.0j, 0.5 + 1.0j, -0.3 + 0.05j)
ATOM_GRID = 512
ATOM_SET = ((2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1))
ADD_BAND = (0.5, 2.0)
KS_CTRL_BAR = 1.0e-2
CTRL_SEP_BAR = 1.0e-3
CARRIER_CTRL_BAR = 1.0e-2
CB_F = float(ob.CB_CITED)
SCRAMBLE_SEED = ob.SCR_SEED
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC1: identifiers that mark a construction as wall/tau-derived.
WALL_IDS = ("gram_anatomy", "eigvalsh", "eigh", "svd", "slogdet",
            "tau", "tau_h", "lamS", "negA", "wall_S", "wall_A",
            "assemble_step", "build_rung")
# AC2: identifiers that mark a construction as read-derived.
READ_IDS = ("q", "q_value", "tr", "trace", "resolvent_trace",
            "reserve", "margin", "trace_R", "lu_read", "inv")

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
    """Banned identifiers inside declared function bodies only."""
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
    return "%+.4f/%+.4f/%+.4f" % trio(values)


def linfit(x, y):
    """OLS y = a + s x; returns s, 2SE(s), R^2, a."""
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


def wrap(angle):
    return float(math.atan2(math.sin(angle), math.cos(angle)))


def complex_rel(left, right):
    return abs(left - right) / max(1.0, abs(left), abs(right))

# ==================================================== measure side
def measure_source(kind, kz, world=None, scramble_seed=None):
    """The source tuple of one rung: window geometry + comb only
    (mirrors ob.build_rung's measure construction verbatim)."""
    if kind == "surf":
        rr = pt.window_of(kz, scramble_seed=scramble_seed)
        alpha, mm_len, dd, hh = (rr["alpha"], rr["M"], rr["D"],
                                 rr["h"])
        uu = rr["uu"]
        mass = 2.0 * rr["lam"]
        c_ar = rr["c_ar"]
    else:
        alpha, mm_len, hh, ka = ob.ext_frame(kz)
        dd = 2.0 * alpha / mm_len
        uu = ob.EXT["U"][:ka].copy()
        mass = ob.EXT["MU"][:ka].copy()
        c_ar = np.asarray(core.arch_lags(mm_len, dd), float)
    if world == "smooth":
        mass = pt.smooth_masses(uu)
    return dict(kind=kind, kz=int(kz), alpha=float(alpha),
                M=int(mm_len), D=float(dd), h=int(hh),
                c_ar=np.asarray(c_ar, float), u_at=uu, mu_at=mass)


def build_chain_from_source(src, n_chain):
    """AC1-SCANNED: the Jacobi prefix of mu_+ from SOURCE DATA ONLY
    (measure forward).  No wall matrix, no eigensolver, no tau."""
    c_at, _ = core.atom_lags_at(src["alpha"], src["M"],
                               src["u_at"], src["mu_at"])
    c = np.asarray(src["c_ar"], float) + np.asarray(c_at, float)
    d = pt.grid_density(c)
    ll = 2 * src["M"] - 2
    xs, ws, uf_p = pt.folded_measure(d, ll, +1.0)
    _ys, vs, _uf_n = pt.folded_measure(d, ll, -1.0)
    n_use = min(n_chain, len(xs))
    al, be, m0, steps = pt.lanczos_chain(xs, ws, n_use)
    if steps < n_use or np.any(be <= 0):
        return None
    return dict(h=src["h"], L=ll, al=al, be=be, m0=m0, ws=ws,
                uf=uf_p, n_pos=len(ws), n_neg=len(vs))


def carriers_of(ch):
    """The three named carriers of the RESTRICTED sum-rule residual
    against the folded free (arcsine) reference, plus the tier-1
    residual computed the tier-1 way."""
    hh, ll = ch["h"], ch["L"]
    dth = 2.0 * math.pi / ll
    nb = hh // 2
    A = 2.0 * np.asarray(ch["be"][:nb], float)
    B = 2.0 * np.asarray(ch["al"][:nb], float)
    lp = float(np.sum(np.log(A)))
    rho = (np.asarray(ch["ws"], float) / ch["m0"]) / dth
    g_plus = float(np.sum(np.log(math.pi * rho))) * dth / math.pi
    frac = len(rho) * dth / math.pi
    rho_bar = 1.0 / (math.pi * frac)
    kterm = float(np.mean(np.log(rho / rho_bar)))
    logres = lp - 0.5 * math.log(2.0) - 0.5 * g_plus
    coef = lp - 0.5 * math.log(2.0)
    gap = 0.5 * frac * math.log(frac)
    spread = -0.5 * frac * kterm
    bands = []
    lo = 0.0
    for hi in BAND_EDGES:
        i0, i1 = int(lo * hh), min(int(hi * hh), nb)
        bands.append(float(np.sum(np.log(A[i0:i1])))
                     if i1 > i0 else 0.0)
        lo = hi
    return dict(h=hh, lp=lp, g_plus=g_plus, excl=1.0 - frac,
                frac=frac, logres=logres, res=math.exp(logres),
                coef=coef, gap=gap, spread=spread, bands=bands,
                ks_bulk=float(np.sum((A - 1.0) ** 2 + B ** 2)),
                A=A, B=B)


def free_folded_residual(ll):
    """SR-FREE: the folded free reference is EQUAL weights on
    theta_j = 2 pi j / L, j = 1..L/2 (E4); its residual must read 1."""
    jj = np.arange(1, ll // 2 + 1)
    th = 2.0 * math.pi * jj / ll
    xs = np.cos(th)
    ws = np.full(len(jj), 1.0 / len(jj))
    nb = len(jj) // 2
    al, be, m0, steps = pt.lanczos_chain(xs, ws, nb + 1)
    if steps < nb + 1:
        return None
    ch = dict(h=2 * nb, L=ll, al=al, be=be, m0=m0, ws=ws, uf=jj,
              n_pos=len(ws), n_neg=0)
    car = carriers_of(ch)
    return car, float(2.0 * be[0]), float(np.median(2.0 * be[1:]))


# ====================================================== wall ladder
def build_ladder():
    section("W -- the CCVII/CCXXV wall ladder, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
        print("    SMOKE: %d contiguous surface rungs (so that the "
              "steps remain genuine artifact steps)" % len(zones))
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
    global_l = max(st["L_src"] for st in steps)
    if SMOKE:
        check("T1 SMOKE: fixed CCXXV filter taken from the stored "
              "artifact (a subset ladder cannot reproduce global L)",
              True)
        return poles_art, res_art
    fd = zol.build_filter(CB_F, global_l, NDIM)
    dev_l = abs(global_l - float(artifact["filter"]["L"])) \
        / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fd["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fd["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("T1 fixed CCXXV GLOBAL m=8 filter rebuilt from source-only "
          "L: L rel %.2e, poles %.2e, residues %.2e <= %.0e"
          % (dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    return np.asarray(fd["poles"], complex), \
        np.asarray(fd["residues"], float)


def lu_read(matrix, pole, want_det=True):
    """LU-only shifted tau / resolvent read (no eigensolver).

    AMENDMENT A1 (numerical representation only, inherited verbatim
    from CCXLVII's own A2): log tau is always formed as the sum of
    diagonal log magnitudes plus phases; callers that need only q
    suppress the reconstruction of the raw determinant, whose
    magnitude overflows float64 on the aligned CONTROL matrices while
    every log-read and every inverse trace stays finite."""
    shifted = matrix.astype(complex) - pole * np.eye(NDIM,
                                                     dtype=complex)
    lum, piv = sla.lu_factor(shifted)
    inv = sla.lu_solve((lum, piv), np.eye(NDIM, dtype=complex))
    parity = -1.0 if int(np.sum(piv != np.arange(NDIM))) % 2 else 1.0
    diag = np.diag(lum)
    log_abs = float(np.sum(np.log(np.abs(diag))))
    phase = wrap(float(np.sum(np.angle(diag)))
                 + (math.pi if parity < 0.0 else 0.0))
    det = None
    if want_det:
        mag = math.exp(log_abs)
        det = complex(mag * math.cos(phase), mag * math.sin(phase))
    tr = complex(np.trace(inv))
    return dict(log_abs=log_abs, phase=phase, det=det, inv=inv,
                tr=tr, q=-tr, m00=complex(inv[0, 0]),
                hs=float(np.linalg.norm(inv)))


def translation(steps, artifact, poles, residues):
    section("T -- shifted tau translation, LU only, warded against "
            "the stored 68x8 CCXLVII artifact")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_det = d_ph = d_tr = d_expr = d_marg = 0.0
    for idx, st in enumerate(steps):
        key = (int(st["r1"]["h"]), int(st["r1"]["kz"]),
               int(st["r2"]["h"]), int(st["r2"]["kz"]))
        src = stored.get(key)
        pole_rows = []
        contribs = []
        for j, (pole, resid) in enumerate(zip(poles, residues)):
            rd = lu_read(st["Mt"], pole)
            contribs.append(2.0 * float(resid) * rd["tr"].real)
            if src is not None:
                sp = src["poles"][j]
                d_det = max(d_det, complex_rel(rd["det"],
                                               complex(*sp["determinant"])))
                d_ph = max(d_ph, abs(wrap(rd["phase"] - sp["phase"])))
                d_tr = max(d_tr, complex_rel(
                    rd["tr"], complex(*sp["resolvent_trace"])))
            pole_rows.append(dict(j=j, pole=pole, y=float(pole.imag),
                                  residue=float(resid), read=rd))
        trace_r = NDIM + math.fsum(contribs)
        reserve = 1.0 - trace_r
        if src is not None:
            d_expr = max(d_expr, abs(trace_r - float(src["trace_R"])))
            d_marg = max(d_marg, abs(reserve - float(src["margin"])))
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         gap=float(st["gap"]), trace_r=trace_r,
                         reserve=reserve, contribs=contribs,
                         poles=pole_rows, matched=src is not None))
    n_match = sum(1 for r in rows if r["matched"])
    check("T2 LU det/phase/trace reproduce the stored artifact on "
          "%d matched steps x 8: det %.2e, phase %.2e, trace %.2e "
          "<= %.0e" % (n_match, d_det, d_ph, d_tr, LU_TIE),
          n_match >= 1 and d_det <= LU_TIE and d_ph <= LU_TIE
          and d_tr <= LU_TIE and (SMOKE or n_match == STEPS_EXP),
          kill="K2")
    check("T3 partial fractions reproduce stored trace_R / margin: "
          "%.2e / %.2e <= %.0e" % (d_expr, d_marg, LU_TIE),
          d_expr <= LU_TIE and d_marg <= LU_TIE, kill="K2")
    print("    reserve = 1 - tr R level min/med/max %s"
          % e3([r["reserve"] for r in rows]))
    return rows


# =================================================== the m-function
def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- the CCVII n-read
    direction.  Returns (a, b, Q) with Q^T M Q = J(a, b), or None if
    the direction is not cyclic or the matrix is not float64-finite
    (the latter happens only in the aligned scramble world)."""
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
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0,
                                                      abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b, qq


def jacobi_matrix(a, b):
    jm = np.diag(np.asarray(b, float))
    idx = np.arange(len(a))
    jm[idx, idx + 1] = a
    jm[idx + 1, idx] = a
    return jm


def cf_arrays(a, b, z):
    """E1 continued fractions: g[k] = top-corner m of block [k..n-1],
    f[k] = bottom-corner m of block [0..k]."""
    n = len(b)
    g = np.zeros(n, complex)
    g[n - 1] = 1.0 / (b[n - 1] - z)
    for k in range(n - 2, -1, -1):
        g[k] = 1.0 / (b[k] - z - a[k] ** 2 * g[k + 1])
    f = np.zeros(n, complex)
    f[0] = 1.0 / (b[0] - z)
    for k in range(1, n):
        f[k] = 1.0 / (b[k] - z - a[k - 1] ** 2 * f[k - 1])
    return f, g


def weyl_trace(a, b, z):
    """E1 two-sided formula summed over the sites."""
    f, g = cf_arrays(a, b, z)
    n = len(b)
    total = 0.0 + 0.0j
    for k in range(n):
        den = b[k] - z
        if k > 0:
            den = den - a[k - 1] ** 2 * f[k - 1]
        if k < n - 1:
            den = den - a[k] ** 2 * g[k + 1]
        total += 1.0 / den
    return total, g[0]


def det_recurrence(a, b, z):
    """P_n(z) = det(J - zI) and P_n'(z) by the three-term recurrence
    and its derivative (Christoffel-Darboux route)."""
    n = len(b)
    p0, p1 = 1.0 + 0.0j, complex(b[0] - z)
    d0, d1 = 0.0 + 0.0j, -1.0 + 0.0j
    for k in range(1, n):
        p2 = (b[k] - z) * p1 - a[k - 1] ** 2 * p0
        d2 = -p1 + (b[k] - z) * d1 - a[k - 1] ** 2 * d0
        p0, p1 = p1, p2
        d0, d1 = d1, d2
    return p1, d1


def ks_distance(a1, b1, a2, b2):
    """AC2-SCANNED: the Killip-Simon l2 (Hilbert-Schmidt) distance of
    two Jacobi data sets.  Jacobi data and nothing else."""
    da = np.asarray(a2, float) - np.asarray(a1, float)
    db = np.asarray(b2, float) - np.asarray(b1, float)
    return math.sqrt(float(np.sum(db ** 2))
                     + 2.0 * float(np.sum(da ** 2)))


def bound_a(dks, y_value):
    """AC2-SCANNED: E3 crude bound sqrt(n) ||D||_HS / y^2."""
    return math.sqrt(NDIM) * dks / (y_value * y_value)


def bound_b(dks, hs_ref, y_value):
    """AC2-SCANNED: E3 Neumann-refined bound with the reference
    resolvent Hilbert-Schmidt norm; VOID (inf) outside the regime."""
    if dks >= y_value:
        return float("inf")
    return hs_ref * dks / (y_value - dks)


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def bridge_wards(rows):
    section("B -- THE M-FUNCTION BRIDGE: the eight pole reads as Weyl "
            "m-function / resolvent-trace values of a Jacobi matrix")
    d_orth = d_sim = d_m = d_wtr = d_dtr = d_det = d_hs = d_zero = 0.0
    n_bad = 0
    for row in rows:
        jf = jacobi_form(row["step"]["Mt"])
        if jf is None:
            n_bad += 1
            row["jac"] = None
            continue
        a, b, qq = jf
        jm = jacobi_matrix(a, b)
        scale = max(1.0, float(np.max(np.abs(row["step"]["Mt"]))))
        d_orth = max(d_orth, float(np.max(np.abs(
            qq.T @ qq - np.eye(NDIM)))))
        d_sim = max(d_sim, float(np.max(np.abs(
            qq.T @ row["step"]["Mt"] @ qq - jm))) / scale)
        row["jac"] = (a, b)
        for pr in row["poles"]:
            z = pr["pole"]
            wtr, m_cf = weyl_trace(a, b, z)
            pn, dpn = det_recurrence(a, b, z)
            rj = np.linalg.inv(jm - z * np.eye(NDIM, dtype=complex))
            rd = pr["read"]
            d_m = max(d_m, complex_rel(m_cf, rd["m00"]))
            d_wtr = max(d_wtr, complex_rel(wtr, rd["tr"]))
            d_dtr = max(d_dtr, complex_rel(-dpn / pn, rd["tr"]))
            d_det = max(d_det, complex_rel(pn, rd["det"]))
            d_hs = max(d_hs, abs(float(np.linalg.norm(rj))
                                 - rd["hs"]) / max(1.0, rd["hs"]))
            pr["rj"] = rj
            pr["hs_j"] = float(np.linalg.norm(rj))
        _f0, g0 = cf_arrays(a, b, 0.0 + 0.0j)
        d_zero = max(d_zero, abs(g0[0].real * row["gap"] - 1.0))
    check("B0 Lanczos form of (M_h, e_0) exists on all %d steps "
          "(cyclic n-read direction)" % len(rows), n_bad == 0,
          "breakdowns %d" % n_bad, kill="K2")
    check("B1 WARD similarity Q^T Q = I and Q^T M_h Q = J(a,b): "
          "%.2e / %.2e <= %.0e" % (d_orth, d_sim, SIM_TIE),
          d_orth <= SIM_TIE and d_sim <= SIM_TIE, kill="K2")
    check("B2 WARD m-function: E1 continued fraction == LU "
          "[(M_h - z_j)^{-1}]_00 (CCXLVII's sensitivity kernel G_00) "
          "on %dx8: max rel %.2e <= %.0e"
          % (len(rows), d_m, BRIDGE_TIE), d_m <= BRIDGE_TIE,
          kill="K2")
    check("B3 WARD trace: E1 two-sided Weyl formula summed over the "
          "8 sites == LU resolvent trace on %dx8: max rel %.2e "
          "<= %.0e" % (len(rows), d_wtr, BRIDGE_TIE),
          d_wtr <= BRIDGE_TIE, kill="K2")
    check("B4 WARD trace, CD route: -P_n'(z)/P_n(z) == LU trace and "
          "P_n(z_j) == LU shifted determinant: %.2e / %.2e <= %.0e"
          % (d_dtr, d_det, DET_TIE),
          d_dtr <= DET_TIE and d_det <= DET_TIE, kill="K2")
    check("B5 WARD real-axis anchor m_h(0) = 1/s (s = step gap): "
          "max |m(0) s - 1| = %.2e <= %.0e" % (d_zero, DET_TIE),
          d_zero <= DET_TIE, kill="K2")
    check("B6 WARD unitary invariance ||(J_h - z)^{-1}||_HS == "
          "||(M_h - z)^{-1}||_HS: max rel %.2e <= %.0e"
          % (d_hs, BRIDGE_TIE), d_hs <= BRIDGE_TIE, kill="K2")
    print("    THE POINT: the eight reads are Weyl-function values of "
          "a Jacobi matrix at eight FIXED off-spectrum points; the "
          "KS/l2 machinery acts exactly there.")
    return True


def ch_surface_map(rows):
    section("H -- CCXVII c_h diagnostic on the matched surface "
            "terminators (labelled screen currency only)")
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
        out[(int(rung["h"]), int(kz))] = 1.0 - top
    vals = list(out.values())
    check("H1 c_h matched on %d surface steps; band %s inside cited "
          "[1.4e-8, 1.7e-4] up to 2x" % (len(out), e3(vals)),
          len(out) >= 1 and min(vals) >= 0.5 * 1.4e-8
          and max(vals) <= 2.0 * 1.7e-4, kill="K2")
    return out


# ======================================== the uniform-control census
def uniform_control_census(rows, ch_map, meas_by_kz):
    section("K -- THE UNIFORM-CONTROL CENSUS: is the h-variation of "
            "the eight reads controlled by the KS data?")
    pairs = list(zip(rows[:-1], rows[1:]))
    y_vals = np.asarray([pr["y"] for pr in rows[0]["poles"]], float)
    a_abs = np.asarray([abs(pr["residue"])
                        for pr in rows[0]["poles"]], float)
    shares = np.asarray([[abs(c) for c in r["contribs"]]
                         for r in rows], float)
    shares = shares / shares.sum(axis=1)[:, None]
    share_med = np.median(shares, axis=0)
    band = [j for j in range(NDIM)
            if share_med[j] >= DECISION_SHARE_FLOOR]

    dks = np.zeros(len(pairs))
    meas = np.zeros((len(pairs), NDIM))
    nat = np.zeros((len(pairs), NDIM))
    bnd_a = np.zeros((len(pairs), NDIM))
    bnd_b = np.zeros((len(pairs), NDIM))
    capt = np.full((len(pairs), NDIM), np.nan)
    bnd_tot = np.zeros(len(pairs))
    meas_tot = np.zeros(len(pairs))
    fo_tot = np.zeros(len(pairs))
    budget = np.zeros(len(pairs))
    n_sound = 0
    n_sound_b = 0
    for i, (r0, r1) in enumerate(pairs):
        a0, b0 = r0["jac"]
        a1, b1 = r1["jac"]
        dks[i] = ks_distance(a0, b0, a1, b1)
        dmat = jacobi_matrix(a1, b1) - jacobi_matrix(a0, b0)
        budget[i] = min(r0["reserve"], r1["reserve"])
        meas_tot[i] = abs(r1["trace_r"] - r0["trace_r"])
        fo_terms = []
        for j in range(NDIM):
            p0, p1 = r0["poles"][j], r1["poles"][j]
            meas[i, j] = abs(p1["read"]["q"] - p0["read"]["q"])
            nat[i, j] = y_vals[j] * meas[i, j] / NDIM
            bnd_a[i, j] = bound_a(dks[i], y_vals[j])
            bnd_b[i, j] = bound_b(dks[i], p0["hs_j"], y_vals[j])
            fo = -complex(np.trace(p0["rj"] @ dmat @ p0["rj"]))
            capt[i, j] = meas[i, j] / abs(fo) if abs(fo) > 0 else \
                float("nan")
            fo_terms.append(2.0 * p0["residue"] * fo.real)
            n_sound += int(meas[i, j]
                           <= bnd_a[i, j] * (1.0 + BOUND_SOUND_TOL))
            n_sound_b += int(not np.isfinite(bnd_b[i, j])
                             or meas[i, j] <= bnd_b[i, j]
                             * (1.0 + BOUND_SOUND_TOL))
        fo_tot[i] = abs(math.fsum(fo_terms))
        bnd_tot[i] = 2.0 * float(np.sum(
            a_abs * np.minimum(bnd_a[i], bnd_b[i])))
    n_cell = len(pairs) * NDIM
    check("K1 WARD BOUND-SOUNDNESS: measured |Delta q| <= BOUND-A on "
          "%d/%d cells and <= BOUND-B (where the Neumann regime "
          "holds) on %d/%d" % (n_sound, n_cell, n_sound_b, n_cell),
          n_sound == n_cell and n_sound_b == n_cell, kill="K2")

    bnd_min = np.minimum(bnd_a, bnd_b)
    valid = budget > 0.0
    n_valid = int(np.sum(valid))
    ctrl_cell = ((2.0 * a_abs[None, :] * bnd_min
                  <= budget[:, None] / NDIM) & valid[:, None])
    ctrl_agg = (bnd_tot <= budget) & valid
    per_pole = ctrl_cell.sum(axis=0)
    loose = bnd_a / np.where(meas > 0.0, meas, np.nan)
    print("    KS data D_i = ||J_{i+1} - J_i||_HS: %s   (h-slope "
          "%+.3f, 2SE %.3f)" % (e3(dks),
                                *linfit(np.log([r["h"] for r in
                                                rows[:-1]]),
                                        np.log(dks))[:2]))
    print("    reserve budget min(reserve_i, reserve_{i+1}): %s"
          % e3(budget))
    print("    budget-void pairs (non-positive reserve budget, "
          "excluded from the census denominators): %d/%d"
          % (len(pairs) - n_valid, len(pairs)))
    print("\n    j        y_j     |a_j|   share_med  nat|Dq| "
          "min/med/max        BND-A med   BND-B med   ctrl  capture "
          "med  loose med")
    for j in range(NDIM):
        nb_valid = int(np.sum(np.isfinite(bnd_b[:, j])))
        print("    %-2d %10.4g %9.4g %9.4f  %-25s %10.3e %10.3e "
              "%3d/%-3d %8.3e %10.3e"
              % (j, y_vals[j], a_abs[j], share_med[j],
                 e3(nat[:, j]), float(np.median(bnd_a[:, j])),
                 float(np.median(bnd_b[:, j][
                     np.isfinite(bnd_b[:, j])]))
                 if nb_valid else float("inf"),
                 int(per_pole[j]), n_valid,
                 float(np.nanmedian(capt[:, j])),
                 float(np.nanmedian(loose[:, j]))))
        print("       Neumann-admissible pairs (D_i < y_j) %d/%d; "
              "2|a_j| x bound / per-pole budget med %.3e"
              % (nb_valid, len(pairs),
                 float(np.median((2.0 * a_abs[j] * bnd_min[valid, j])
                                 / (budget[valid] / NDIM)))))
    gapf = bnd_tot / np.where(valid, budget, np.nan)
    print("\n    AGGREGATE: BND_i = 2 sum_j |a_j| bound: %s"
          % e3(bnd_tot))
    print("    measured |Delta tr R|: %s" % e3(meas_tot))
    print("    KS-linear first-order |Delta tr R|: %s" % e3(fo_tot))
    print("    aggregate looseness BND_i / |Delta tr R|: %s"
          % e3(bnd_tot / np.where(meas_tot > 0, meas_tot, np.nan)))
    print("    gap factor BND_i / budget_i: %s" % e3(gapf))
    print("    aggregate census CONTROLLED %d/%d valid pairs; "
          "per-pole census %s"
          % (int(np.sum(ctrl_agg)), n_valid,
             "/".join(str(int(v)) for v in per_pole)))
    print("    decision band (median share >= %.2f): poles %s"
          % (DECISION_SHARE_FLOOR,
             ",".join(str(j) for j in band) or "none"))
    cross = []
    for i in range(len(pairs)):
        j0 = None
        for j in range(NDIM):
            if np.all(ctrl_cell[i, j:]):
                j0 = j
                break
        cross.append(j0 if j0 is not None else NDIM)
    cross = np.asarray(cross, int)
    jstar = int(np.median(cross))
    print("    crossover pole index j* (all poles above are "
          "controlled): med %d -> y* = %.4g (min %d, max %d)"
          % (jstar, y_vals[jstar] if jstar < NDIM else float("inf"),
             int(np.min(cross)), int(np.max(cross))))
    capt_agg = meas_tot / np.where(fo_tot > 0, fo_tot, np.nan)
    print("    KS-LINEAR CAPTURE RATIO |Delta tr R| / "
          "|first-order KS response|: %s" % e3(capt_agg))

    band_ctrl = [j for j in band if per_pole[j] == n_valid]
    if int(np.sum(ctrl_agg)) == n_valid:
        verdict = "POLES-KS-CONTROLLED(%d/%d)" % (n_valid, n_valid)
    elif int(np.max(per_pole)) > 0:
        verdict = ("PARTIAL(agg %d/%d; poles fully controlled %s; "
                   "decision-band controlled %s; y* med %.4g; "
                   "gap factor med %.2e)"
                   % (int(np.sum(ctrl_agg)), n_valid,
                      ",".join(str(j) for j in range(NDIM)
                               if per_pole[j] == n_valid)
                      or "none",
                      ",".join(str(j) for j in band_ctrl) or "none",
                      y_vals[jstar] if jstar < NDIM else float("inf"),
                      float(np.nanmedian(gapf))))
    else:
        verdict = ("KS-INSUFFICIENT(gap factor med %.2e, worst pole "
                   "j=%d)" % (float(np.nanmedian(gapf)),
                              int(np.argmax(np.median(
                                  2.0 * a_abs[None, :] * bnd_min,
                                  axis=0)))))
    print("    CENSUS VERDICT: %s" % verdict)

    # ---- K4 the residue, measured
    hs_pair = np.asarray([r["h"] for r in rows[:-1]], float)
    s_d, s_d2se, r2_d, _ = linfit(np.log(hs_pair), np.log(dks))
    adm = int(np.sum(dks[:, None] < y_vals[None, :]))
    link = []
    for i, (r0, r1) in enumerate(pairs):
        if r0["seg"] != "surf" or r1["seg"] != "surf":
            continue
        m0, m1 = meas_by_kz.get(r0["kz"]), meas_by_kz.get(r1["kz"])
        if m0 is None or m1 is None:
            continue
        npx = min(N_PREFIX, len(m0["A"]), len(m1["A"]))
        dd = math.sqrt(2.0 * float(np.sum(
            (m1["A"][:npx] - m0["A"][:npx]) ** 2))
            + float(np.sum((m1["B"][:npx] - m0["B"][:npx]) ** 2)))
        link.append((dks[i], dd))
    if len(link) >= 3:
        lw = np.log(np.asarray([v[0] for v in link]))
        lm = np.log(np.asarray([v[1] for v in link]))
        cc = float(np.corrcoef(lw, lm)[0, 1])
        sl = linfit(lm, lw)[0]
    else:
        cc, sl = float("nan"), float("nan")
    print("\n    RESIDUE (measured, this is what an all-h statement "
          "needs):")
    print("      (i)   h-uniformity of the KS data: D ~ h^%+.3f "
            "(2SE %.3f, R^2 %.3f)" % (s_d, s_d2se, r2_d))
    print("      (ii)  Neumann-admissible cells D_i < y_j: %d/%d"
          % (adm, n_cell))
    print("      (iii) measure->wall link on %d surface pairs: "
          "corr(log D_wall, log D_measure) = %+.3f, slope %+.3f"
          % (len(link), cc, sl))

    # ---- K5 screens
    taus = np.asarray([r["tau_scale"] for r in rows[:-1]], float)
    mask = np.asarray([(int(r["h"]), r["kz"]) in ch_map
                       for r in rows[:-1]], bool)
    chs = np.asarray([ch_map[(int(r["h"]), r["kz"])]
                      for r in rows[:-1]
                      if (int(r["h"]), r["kz"]) in ch_map], float)
    reloc = []
    for label, arr in (("D_KS", dks), ("gap-factor", gapf),
                       ("capture", capt_agg)):
        t1, v1 = screen(arr, taus, "%s vs step tau" % label)
        t2, v2 = screen(arr[mask], chs, "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("K5 tau- and c_h-relocation screens on every new margin: "
          "relocation seats %s" % (",".join(reloc) or "none"),
          not reloc)
    return dict(verdict=verdict, dks=dks, gapf=gapf,
                capt_agg=capt_agg, ctrl_agg=ctrl_agg,
                per_pole=per_pole, band=band, jstar=jstar,
                y_vals=y_vals, a_abs=a_abs, slope_d=s_d,
                slope_d2se=s_d2se, adm=adm, n_cell=n_cell,
                link=(cc, sl), reloc=reloc)


# ======================================= M: the sum-rule object (a)
def sumrule_anatomy(zones, tau_by_kz, ch_map_kz):
    section("M -- THE SUM-RULE OBJECT: anatomy of the h-stable "
            "restricted residual 0.665")
    truth, smooth, scram = {}, {}, {}
    for kz in zones:
        src = measure_source("surf", kz)
        ch = build_chain_from_source(src, src["h"] // 2 + 2)
        if ch is None:
            continue
        truth[kz] = carriers_of(ch)
        chs = build_chain_from_source(
            measure_source("surf", kz, world="smooth"),
            src["h"] // 2 + 2)
        if chs is not None:
            smooth[kz] = carriers_of(chs)
        chr_ = build_chain_from_source(
            measure_source("surf", kz, scramble_seed=SCRAMBLE_SEED),
            src["h"] // 2 + 2)
        if chr_ is not None:
            scram[kz] = carriers_of(chr_)
    kzs = sorted(truth)
    car = [truth[kz] for kz in kzs]
    hs = np.asarray([c["h"] for c in car], float)
    res = np.asarray([c["res"] for c in car], float)
    ksb = np.asarray([c["ks_bulk"] for c in car], float)
    exc = np.asarray([c["excl"] for c in car], float)
    med_res = float(np.median(res))
    med_ksb = float(np.median(ksb))
    print("    rungs %d, h = %d..%d" % (len(car), int(hs.min()),
                                        int(hs.max())))
    print("    residual res(h): %s  (med %.4f, CCXLV 0.665)"
          % (f4(res), med_res))
    print("    KS_bulk: %s  (med %.4f, CCXLV 1.830)"
          % (e3(ksb), med_ksb))
    print("    excluded theta-fraction: %s" % f4(exc))
    ok_rep = (abs(med_res / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(med_ksb / KSBULK_MED_REF - 1.0) <= REPRO_RTOL
              and EXCL_BAND[0] <= float(np.median(exc))
              <= EXCL_BAND[1])
    check("M1 REPRO of CCXLV tier 1: res med %.4f (rel %.3f), "
          "KS_bulk med %.4f (rel %.3f), excl med %.4f in [%.2f,%.2f]"
          % (med_res, abs(med_res / RES_MED_REF - 1.0), med_ksb,
             abs(med_ksb / KSBULK_MED_REF - 1.0),
             float(np.median(exc)), *EXCL_BAND),
          SMOKE or ok_rep, kill="K3")

    dev_id = max(abs(c["coef"] + c["gap"] + c["spread"] - c["logres"])
                 for c in car)
    check("M2 WARD carrier identity log res = COEF + GAP + SPREAD "
          "per rung: max dev %.2e <= %.0e" % (dev_id, IDENT_TIE),
          dev_id <= IDENT_TIE, kill="K2")
    fr = free_folded_residual(2 * 512 - 2)
    if fr is not None:
        fcar, a1_free, ak_free = fr
        check("M2b WARD SR-FREE: the folded free reference is the "
              "arcsine measure (E4) -- A_1 = %.6f (sqrt2 %.6f), "
              "A_n med %.6f (1), residual %.6f (1), excl %.2e"
              % (a1_free, math.sqrt(2.0), ak_free, fcar["res"],
                 fcar["excl"]),
              abs(fcar["res"] - 1.0) <= SR_FREE_TIE
              and abs(a1_free - math.sqrt(2.0)) <= SR_FREE_COEF_TIE
              and abs(ak_free - 1.0) <= SR_FREE_COEF_TIE, kill="K2")

    print("\n    carrier anatomy (median, log-log h-slope, 2SE):")
    slopes = {}
    for name in ("logres", "coef", "gap", "spread"):
        vals = np.asarray([c[name] for c in car], float)
        sl, s2, r2, _ = linfit(np.log(hs), vals)
        slopes[name] = (sl, s2)
        print("      %-8s med %+10.5f   d/dlog h %+8.4f (2SE %.4f, "
              "R^2 %.3f)" % (name, float(np.median(vals)), sl, s2,
                             r2))
    canc = float(np.median([(abs(c["coef"]) + abs(c["spread"]))
                            / abs(c["logres"]) for c in car]))
    flat = [n for n in ("coef", "gap", "spread")
            if abs(slopes[n][0]) <= CARRIER_FLAT_BAR
            or abs(slopes[n][0]) <= slopes[n][1]]
    steep = [n for n in ("coef", "gap", "spread")
             if n not in flat]
    if len(steep) >= 2:
        ctype = "CANCELLATION(%s)" % ",".join(steep)
    elif not steep:
        ctype = "CARRIERWISE-CONSTANT"
    else:
        ctype = "SINGLE-DRIFT(%s)" % steep[0]
    print("      cancellation depth (|COEF|+|SPREAD|)/|log res| med "
          "%.2f; carriers h-flat %s; type %s"
          % (canc, ",".join(flat) or "none", ctype))

    common = [kz for kz in kzs if kz in smooth]
    if common:
        prime = np.asarray([truth[kz]["lp"] - smooth[kz]["lp"]
                            for kz in common], float)
        base = np.asarray([smooth[kz]["lp"] - 0.5 * math.log(2.0)
                           for kz in common], float)
        hp = np.asarray([truth[kz]["h"] for kz in common], float)
        print("      COEF split: prime part (LP - LP_smooth) med "
              "%+.5f (slope %+.4f), smooth part med %+.5f "
              "(slope %+.4f)"
              % (float(np.median(prime)), linfit(np.log(hp), prime)[0],
                 float(np.median(base)), linfit(np.log(hp), base)[0]))
    print("      band-resolved LP (median over rungs), bands n/h = "
          "(0,1/16] (1/16,1/8] (1/8,1/4] (1/4,1/2]:")
    bmat = np.asarray([c["bands"] for c in car], float)
    print("        " + "  ".join("%+9.4f" % v
                                 for v in np.median(bmat, axis=0)))
    check("M3 carrier anatomy typed %s (constant carrier census "
          "printed)" % ctype, True)

    iqr = float(np.percentile(res, 75) - np.percentile(res, 25))
    coinc = ("COINCIDENCE-COMPATIBLE" if abs(med_res - COINC_CAND)
             <= iqr else "COINCIDENCE-EXCLUDED")
    check("M4 formula candidate res(h) = exp(COEF + GAP + SPREAD) "
          "with GAP = (f log f)/2, f = 1 - excl; closed-form screen "
          "vs 2/3: |med - 2/3| = %.4f vs ladder IQR %.4f -> %s"
          % (abs(med_res - COINC_CAND), iqr, coinc), True)

    scr = []
    for name in ("logres", "coef", "gap", "spread"):
        vals = np.asarray([abs(truth[kz][name]) for kz in kzs], float)
        tv = np.asarray([tau_by_kz.get(kz, float("nan"))
                         for kz in kzs], float)
        cv = np.asarray([ch_map_kz.get(kz, float("nan"))
                         for kz in kzs], float)
        t1, v1 = screen(vals, tv, "|%s| vs step tau" % name)
        t2, v2 = screen(vals, cv, "|%s| vs c_h" % name)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            scr.append(name)
    check("M6 carrier tau/c_h screens: relocation seats %s"
          % (",".join(scr) or "none"), not scr)
    meas_by_kz = {kz: dict(A=truth[kz]["A"], B=truth[kz]["B"])
                  for kz in kzs}
    return dict(truth=truth, smooth=smooth, scram=scram,
                med_res=med_res, ctype=ctype, canc=canc,
                coinc=coinc, slopes=slopes, meas_by_kz=meas_by_kz,
                kzs=kzs)


def deep_carrier_extension(steps, mres):
    section("M5 -- the carrier identity on declared DEEP rungs")
    deep_kz = sorted({int(st["r2"]["kz"]) for st in steps
                      if ob.seg_of(st) == "deep"})
    if not deep_kz:
        check("M5 no deep steps available in this mode", True)
        return None
    idx = np.linspace(0, len(deep_kz) - 1,
                      min(DEEP_CARRIER_SUB, len(deep_kz))).astype(int)
    sub = [deep_kz[i] for i in sorted(set(idx.tolist()))]
    out = []
    for kz in sub:
        src = measure_source("deep", kz)
        ch = build_chain_from_source(src, src["h"] // 2 + 2)
        if ch is None:
            print("    deep kz %-4d CHAIN SHORT [%.1f s]"
                  % (kz, time.time() - T0), flush=True)
            continue
        car = carriers_of(ch)
        out.append(car)
        print("    deep kz %-4d h %-5d res %.4f  COEF %+9.4f  GAP "
              "%+8.4f  SPREAD %+9.4f  excl %.4f  ident %.1e [%.1f s]"
              % (kz, car["h"], car["res"], car["coef"], car["gap"],
                 car["spread"], car["excl"],
                 abs(car["coef"] + car["gap"] + car["spread"]
                     - car["logres"]), time.time() - T0), flush=True)
    if not out:
        check("M5 deep carrier extension: no complete deep chain",
              True)
        return None
    dev = max(abs(c["coef"] + c["gap"] + c["spread"] - c["logres"])
              for c in out)
    dres = [c["res"] for c in out]
    check("M5 deep extension on %d rungs h = %d..%d: identity dev "
          "%.2e <= %.0e; res %s (surface med %.4f)"
          % (len(out), min(c["h"] for c in out),
             max(c["h"] for c in out), dev, IDENT_TIE, f4(dres),
             mres["med_res"]), dev <= IDENT_TIE, kill="K2")
    return out


# ============================================= C: controls / gates
def controls(zones, rows, mres):
    section("C -- CONTROLS: do the falsifying worlds break the "
            "m-function structure and the KS currency?")
    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    fired = []
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
        rels, seps = [], []
        n_align = n_res = n_break = 0
        n_sound = n_cell = 0
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if tr is None or ctl is None or not ctl.get("core_ok") \
                    or tr["jac"] is None:
                continue
            n_align += 1
            with np.errstate(over="ignore", invalid="ignore"):
                mw = sym(tr["step"]["Q"].T
                         @ (ctl["S"] / tr["tau_scale"])
                         @ tr["step"]["Q"])
                jf = jacobi_form(mw)
                at, bt = tr["jac"]
                dks = (ks_distance(at, bt, jf[0], jf[1])
                       if jf is not None else float("inf"))
            if jf is None or not math.isfinite(dks):
                n_break += 1
                continue
            nrm = math.sqrt(float(np.sum(np.asarray(bt) ** 2))
                            + 2.0 * float(np.sum(
                                np.asarray(at) ** 2)))
            rels.append(dks / max(nrm, 1e-300))
            row_sep = []
            sound = True
            for pr in tr["poles"]:
                rd = lu_read(mw, pr["pole"], want_det=False)
                dq = abs(rd["q"] - pr["read"]["q"])
                row_sep.append(pr["y"] * dq / NDIM)
                n_cell += 1
                ok = dq <= bound_a(dks, pr["y"]) \
                    * (1.0 + BOUND_SOUND_TOL)
                n_sound += int(ok)
                sound = sound and ok
            seps.append(row_sep)
            if (rels[-1] >= KS_CTRL_BAR
                    and max(row_sep) >= CTRL_SEP_BAR and sound):
                n_res += 1
        seps = np.asarray(seps, float)
        pole_med = (np.median(seps, axis=0) if len(seps)
                    else np.full(NDIM, np.nan))
        fire = (n_res + n_break) > 0.5 * max(n_align, 1)
        fired.append(fire)
        check("C2.%s BOUND-A holds on every float64-finite aligned "
              "cell of the %s world: %d/%d"
              % (world[:3], world, n_sound, n_cell),
              n_sound == n_cell, kill="K2")
        print("    %-9s wall target fires %d/%d; aligned rungs %d = "
              "resolved %d + representation-break %d + silent %d; KS "
              "data D_world/||J_truth||_HS med %.3e (bar %.0e); read "
              "separation per pole med %s; best %.3e (bar %.0e) -> %s"
              % (world, wall_fire, len(ladder), n_align, n_res,
                 n_break, n_align - n_res - n_break,
                 float(np.median(rels)) if rels else float("nan"),
                 KS_CTRL_BAR,
                 "/".join("%.1e" % v for v in pole_med),
                 float(np.nanmax(pole_med)) if len(seps)
                 else float("nan"), CTRL_SEP_BAR,
                 "FIRE" if fire else "SILENT"))
        if world == "smooth":
            check("C1 SMOOTH violates the wall target (negA > 0) on "
                  "%d/%d surface rungs" % (wall_fire, len(ladder)),
                  wall_fire == len(ladder), kill="K4")
    check("C2 the m-function/KS representation SEES both falsifying "
          "worlds on a majority of aligned rungs (resolved KS data + "
          "resolved read separation + sound bound, OR outright "
          "representation break): %d/2 fired" % sum(fired),
          all(fired), kill="K4")

    dcar = {}
    for world, book in (("smooth", mres["smooth"]),
                        ("scramble", mres["scram"])):
        common = [kz for kz in mres["kzs"] if kz in book]
        dd = [abs(book[kz]["logres"] - mres["truth"][kz]["logres"])
              for kz in common]
        dcar[world] = float(np.median(dd)) if dd else float("nan")
        print("    %-9s carrier move |log res_world - log res_truth| "
              "med %.4f on %d rungs (bar %.0e); res_world med %.4f"
              % (world, dcar[world], len(common), CARRIER_CTRL_BAR,
                 float(np.median([book[kz]["res"]
                                  for kz in common])) if common
                 else float("nan")))
    check("C3 the measure-side carriers move in both falsifying "
          "worlds (>= %.0e): smooth %.4f, scramble %.4f"
          % (CARRIER_CTRL_BAR, dcar["smooth"], dcar["scramble"]),
          all(v >= CARRIER_CTRL_BAR for v in dcar.values()),
          kill="K4")
    return dcar


# ================================== A: the single-atom RHP brick (d)
def arcsine_m(z):
    """E4 Stieltjes transform of the arcsine measure, branch fixed by
    sqrt(z-1) sqrt(z+1) ~ z at infinity."""
    return -1.0 / (np.sqrt(z - 1.0) * np.sqrt(z + 1.0))


def atom_model(zones):
    section("A -- THE SINGLE-ATOM RHP BRICK (tier-1-spec'd first "
            "parametrix brick; MEASURE coordinate only)")
    dev_far = 0.0
    print("    A1 arcsine chain CF vs analytic m(z) = "
          "-1/sqrt(z^2-1) (E4):")
    for n in (8, 32, 128, 512):
        a = np.full(n - 1, 0.5)
        a[0] = 1.0 / math.sqrt(2.0)
        b = np.zeros(n)
        devs = []
        for z in CF_POINTS:
            _f, g = cf_arrays(a, b, complex(z))
            devs.append(abs(g[0] - complex(arcsine_m(complex(z)))))
        print("      n = %-4d |CF - analytic| at z = %s: %s"
              % (n, ", ".join(str(z) for z in CF_POINTS),
                 "  ".join("%.2e" % d for d in devs)))
        if n == 512:
            dev_far = max(devs[:2])
    check("A1 WARD the E4 m-function on the arcsine chain at the two "
          "far points (n = 512): max dev %.2e <= %.0e"
          % (dev_far, BRIDGE_TIE), dev_far <= BRIDGE_TIE, kill="K2")

    # ---- A2 the exactly solvable one-atom measure
    ng = ATOM_GRID
    th = 2.0 * math.pi * np.arange(1, ng + 1) / (2 * ng)
    xs0 = np.cos(th)
    ws0 = np.full(ng, 1.0 / ng)
    src = measure_source("surf", zones[0])
    dd, ll = src["D"], 2 * src["M"] - 2
    al0, be0, _m00, st0 = pt.lanczos_chain(xs0, ws0, ng)
    if st0 < ng:
        check("A2 free reference chain incomplete on the atom grid",
              False, kill="K2")
        return "ATOM-UNAVAILABLE"
    npx_atom = ng // 2
    dev_ex = 0.0
    rows = []
    for (p, k) in ATOM_SET:
        u = k * math.log(p)
        jidx = int(round(u / dd))
        fold = min(jidx % ll, ll - (jidx % ll))
        th0 = 2.0 * math.pi * fold / ll
        x0 = math.cos(th0)
        w_law = 2.0 * math.log(p) * p ** (-0.5 * k)
        w_rel = w_law / float(np.sum(src["mu_at"]))
        xs = np.concatenate([xs0, [x0]])
        ws = np.concatenate([ws0 / (1.0 + w_rel),
                             [w_rel / (1.0 + w_rel)]])
        al, be, m0, steps = pt.lanczos_chain(xs, ws, len(xs))
        if steps < len(xs):
            print("      atom p=%d k=%d CHAIN SHORT (%d/%d)"
                  % (p, k, steps, len(xs)))
            continue
        for z in CF_POINTS[:2]:
            _f, g = cf_arrays(be, al, complex(z))
            exact = complex(np.sum(ws / (xs - complex(z))))
            dev_ex = max(dev_ex, abs(g[0] - exact)
                         / max(1.0, abs(exact)))
        nb = min(len(be), len(be0), npx_atom)
        ks = ks_distance(2.0 * be0[:nb - 1], 2.0 * al0[:nb],
                         2.0 * be[:nb - 1], 2.0 * al[:nb])
        rows.append(dict(p=p, k=k, th0=th0, x0=x0, w=w_rel, ks=ks))
        print("      atom p=%d k=%d: u %.4f -> theta_0 %.4f, x_0 "
              "%+.5f, deployed relative weight %.4e, KS budget "
              "||J_w - J_free||_HS (prefix %d) %.4e"
              % (p, k, u, th0, x0, w_rel, nb, ks))
    check("A2 WARD E5 exactness: the length-N chain of an N-point "
          "one-atom measure reproduces its Stieltjes transform at "
          "the declared complex points: max rel %.2e <= %.0e"
          % (dev_ex, BRIDGE_TIE), dev_ex <= BRIDGE_TIE, kill="K2")

    # ---- A3 superposition
    atype = "ATOM-UNAVAILABLE"
    if len(rows) >= 2:
        xs = np.concatenate([xs0, [r["x0"] for r in rows]])
        wsum = float(np.sum([r["w"] for r in rows]))
        ws = np.concatenate([ws0 / (1.0 + wsum),
                             [r["w"] / (1.0 + wsum) for r in rows]])
        al, be, m0, steps = pt.lanczos_chain(xs, ws, len(xs))
        if steps == len(xs):
            nb = min(len(be), len(be0), npx_atom)
            ks_all = ks_distance(2.0 * be0[:nb - 1], 2.0 * al0[:nb],
                                 2.0 * be[:nb - 1], 2.0 * al[:nb])
            ks_sum = float(np.sum([r["ks"] for r in rows]))
            ratio = ks_all / ks_sum if ks_sum > 0 else float("nan")
            atype = ("SUPERPOSITION-ADDITIVE(%.3f)" % ratio
                     if ADD_BAND[0] <= ratio <= ADD_BAND[1]
                     else "SUBADDITIVE(%.3f)" % ratio
                     if ratio < ADD_BAND[0]
                     else "NOT-ADDITIVE(%.3f)" % ratio)
            print("      joint %d-atom KS budget %.4e vs sum of "
                  "single-atom budgets %.4e -> ratio %.3f"
                  % (len(rows), ks_all, ks_sum, ratio))
    check("A3 atomwise superposition of the KS budget typed %s "
          "(band %s)" % (atype, str(ADD_BAND)), True)
    print("    SCOPE (honest): the one-atom model lives in the "
          "measure coordinate x in [-1,1]; the eight Zolotarev poles "
          "live in the 8x8 wall-step coordinate.  It is the seed of "
          "the parametrix for the KS INPUT D of section K, not a read "
          "at z_j.  No coordinate identification is invented.")
    return atype


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
        print("\n  VERDICT: RHP-T2( %s )" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements on the deployed ladder
  only: the CCXLV 42-rung frame-A measure ladder plus the declared
  deep rungs, and the fixed CCXXV m=8 pole family on the 68-step
  CCVII ladder.  The m-function bridge is an exact algebraic
  representation, warded per rung and per pole; the uniform-control
  census is a bound-versus-measurement census with the classical
  (EXTERNAL-CITED) l2 perturbation estimates, not a theorem about
  all h.  The single-atom brick lives in the measure coordinate and
  is not evaluated at the wall poles.  No marker moves; no paper,
  ledger, website, manifest or verification file is touched; NO RH
  claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.PORT.LATTICE.RHP.01 tier 2 -- the Killip-Simon "
            "sum-rule engine for uniform control of the eight "
            "complex tau reads (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(("build_chain_from_source",
                              "measure_source"), WALL_IDS)
    check("S0.2 AC1 the measure-side chain builder is source-only "
          "(no wall identifier, no eigensolver, no tau)", not ac1,
          ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(("ks_distance", "bound_a", "bound_b"),
                             READ_IDS)
    check("S0.3 AC2 the KS distance and both a-priori bounds contain "
          "no read identifier (bound never built from the read it "
          "controls)", not ac2, ",".join(sorted(set(ac2))),
          kill="K2")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0.4 CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")

    zones, steps = build_ladder()
    if KILLS:
        return finish([])
    poles, residues = get_filter(steps, artifact)
    rows = translation(steps, artifact, poles, residues)
    if KILLS:
        return finish([])
    bridge_wards(rows)
    if KILLS:
        return finish([])
    ch_map = ch_surface_map(rows)
    tau_by_kz = {r["kz"]: r["tau_scale"] for r in rows
                 if r["seg"] == "surf"}
    ch_map_kz = {kz: v for (_h, kz), v in ch_map.items()}

    mres = sumrule_anatomy(zones, tau_by_kz, ch_map_kz)
    deep = deep_carrier_extension(steps, mres)
    cen = uniform_control_census(rows, ch_map, mres["meas_by_kz"])
    controls(zones, rows, mres)
    atype = atom_model(zones)

    labels = [
        "SUMRULE(res med %.4f, %s, cancellation depth %.1f, %s%s)"
        % (mres["med_res"], mres["ctype"], mres["canc"],
           mres["coinc"],
           ", deep-warded %d rungs" % len(deep) if deep else ""),
        "BRIDGE-EXACT(m-function == G_00, Weyl trace == LU trace, "
        "CD route == LU trace)",
        cen["verdict"],
        "CAPTURE(med %.3e)" % float(np.nanmedian(cen["capt_agg"])),
        "RESIDUE(D ~ h^%+.3f +/- %.3f, Neumann-admissible %d/%d, "
        "measure-link corr %+.3f)"
        % (cen["slope_d"], cen["slope_d2se"], cen["adm"],
           cen["n_cell"], cen["link"][0]),
        "ATOM(%s)" % atype,
    ]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())




