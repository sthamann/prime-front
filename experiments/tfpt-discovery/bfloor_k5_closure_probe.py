#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bfloor_k5_closure_probe -- PRIME.ONEBADMODE.BFLOOR.K5.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE ONE OPEN CELL OF THE CERTIFIED SIGMA CHAIN, CLOSED AT DEPTH
K = 5 -- AND THE CHAIN EXTENDED OVER EVERYTHING WALL-LEGAL THAT HAS
EVER BEEN BUILT.  CCLXXVII (bfloor_perstep_certification_probe)
composed the exact-rational chain (P1 entry theorem n > 0 + P2
per-step LDL B-floor + P3 Gauss-Radau depth K = 4 + P4 exact
arithmetic) and certified sigma <= 0.648113 => M positive definite on
68/68 deployed ladder steps, but the F0 sigma-max cell (kz 45,
h 1359, truth sigma = 0.709925) is INFEASIBLE at K = 4 for every
floor: the bound at the full measured floor lambda_min(B) = 122.85
reads 0.8897.  Its disclosed post-frozen diagnostic located the
precise shortfall as ONE moment depth: at the measured floor the
depth curve reads K = 4/5/6/7 -> 0.8897/0.7269/0.7114/0.709925 --
NOT floor quality.  CCLXIX (sigma_stress_battery_probe) built the
full wall-legal adversarial surface: 68 ladder steps + 83 sweep steps
in families F0 (surface-offladder, the breach zone, 17 cells), F1
(deep off-census kz, max sigma 0.468), F2 (denser grids nu > 4,
0.518), F4 (off-anchor alpha, 0.420), F5 (depth extension TAB2,
0.297), and registered SIGMA_ENV = 0.780917.  THIS PROBE lifts the
K = 5 (and, where a cell needs it, K = 6) Gauss-Radau bound to the
SAME exact-rational certified tier -- two more exact Chebyshev
moments nu_7, nu_8 (four more for K = 6), the same monic Radau
modification, the same Fraction census -- WARDS the bound property at
every consumed depth (never assumes it), and runs the closure census
over every built wall-legal cell.

 (a) THE MOMENT EXTENSION.  Per cell, the b-weighted moments
     nu_k = b^T B^k b are computed as exact dyadic rationals to
     k = 8 (K = 5 needs nu_0..nu_8; the escalation depth K = 6 needs
     nu_0..nu_10, computed only where consumed).  The exact Chebyshev
     algorithm (E4), the monic Radau modification and the rule value
     (E6) are the CCLXXVII functions VERBATIM -- they are
     depth-generic; the extension is the two extra exact moments plus
     the deeper ward set.  THE BOUND PROPERTY IS WARDED, NOT ASSUMED,
     at every consumed depth: RB1 (the exact Radau value is >= the
     truth q = b^T B^{-1} b) per cell per depth with 0 violations
     required, the node ward (the prescribed node stays the smallest
     node of the modified rule) per cell per depth, the exact-vs-
     float cross-route per cell per depth, and an EXACT-arithmetic
     RB1 sanity control at K = 5 on a synthetic diagonal measure with
     known rational q.
 (b) THE CLOSURE CENSUS.  Every built wall-legal cell: the 68
     registered ladder steps, the 17 F0 cells (CCLXXVII family
     verbatim) and the F1 / F2 / F4 / F5 sweep cells (CCLXIX
     builders, imported READ-ONLY, BW builder ward re-run here) --
     the CCLXIX wall-legal universe complete.  Per cell: the
     exact-rational LDL floor c_cert (round-62 machine verbatim,
     BIS_ITERS = 40), the certified exact-rational Radau bound at
     the frozen depth ladder K = 4 then K = 5 (always both) then
     K = 6 (only if the K <= 5 best exceeds SIGMA_ENV), the best
     bound = min over the warded depths (LEGITIMATE without any
     monotonicity-in-K assumption: each depth's value is an
     INDEPENDENTLY warded upper bound for the same q -- amendment
     A4), and the two margins: to 1 (the Schur criterion: sigma < 1
     => s = (1 - sigma) n > 0 => M PD) and to the registered
     SIGMA_ENV = 0.7809.  MISSION TARGET: 100 percent of built
     wall-legal cells certified sigma-bound < 1 with O(1) margin
     (the worst margin is stated in the verdict).
 (c) THE COMPOSED STATEMENT UPDATE.  CCLXXVII's composed chain
     restated with the F0 completion: for EVERY built wall-legal
     cell, P1 + P2 + P3(K in {4,5,6}, hypothesis discharged by P2,
     remainder sign warded) + P4 => sigma <= bound < 1 => M positive
     definite, worst bound printed, every premise typed.  The honest
     open residue typed loudly: (i) cells NOT YET BUILT -- the
     surface-registration edge h > 1450 (the concurrent edge scan,
     mission citation key fdae3b68, is mapping sigma's growth there;
     cited as the OPEN FLANK, no number consumed); (ii) the
     all-h / class-level form of the chain (the rigor lane, mission
     citation key d7a7e574) -- this probe is finite, per-cell, on
     the deployed artifacts.
 (d) GATES.  Reproduce CCLXXVII's K = 4 numbers: the certified
     ladder bound max 0.648113, the required-floor census on the 85
     CCLXXVII cells (FEAS ratio med/max 0.1583/0.7779, INFEAS set =
     exactly the kz 45 h 1359 cell, bridge risk point c_req
     0.034904), 3 spot cells printed; the K-depth curve on the kz 45
     cell at the measured floor (K = 4..7 float route ->
     0.8897/0.7269/0.7114/0.709925) with the exact tier tied to the
     float route at K = 5 and K = 6; controls-must-fire (inflated
     floor refused by BOTH tiers; a synthetic cell with truth
     sigma > 1 must NOT certify sigma < 1 -- built here at two
     strengths, x10 coupling and the sharp near-1 scaling); tau /
     CCXVII c_h relocation screens on the NEW margins (1 - bound and
     SIGMA_ENV - bound); anti-circularity AST-scanned (moments and
     floors from B's entries forward; NO eigendata in the
     certificate path -- eig only as truth reference).

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E2 Schur / Sylvester: M = [[n, b^T], [b, B]] symmetric is PD iff
    B is PD and s = n - b^T B^{-1} b > 0; a symmetric matrix is PD
    iff the LDL pivots are all positive.  [Horn & Johnson, Matrix
    Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE: for symmetric A with spec(A)
    in [c, inf), the K-node Gauss-Radau rule with the node prescribed
    at c is an UPPER bound for u^T A^{-1} u (f(x) = 1/x completely
    monotone); the statement is depth-uniform in K.  [Golub &
    Meurant, Matrices, Moments and Quadrature, PUP 2010, Ch. 6-7.]
    THE SIGN IS WARDED PER CELL PER CONSUMED DEPTH (C5).
 E4 the Chebyshev algorithm: the monic three-term recurrence
    coefficients of the orthogonal polynomials of a positive measure
    are rational functions of its power moments (the sigma-table
    recursion); the map is exact in exact arithmetic and
    depth-generic.  [Gautschi, Orthogonal Polynomials: Computation
    and Approximation, OUP 2004, Sec. 2.1; Golub & Meurant op. cit.
    Ch. 4.]
 E5 interval Cholesky: if the outward-rounded interval Cholesky of a
    symmetric interval matrix completes with all pivot lower bounds
    positive, every symmetric matrix in the interval is PD.  [Rump,
    Acta Numerica 19 (2010) 287-449.]
 E6 the diagonal-similarity fact [J^{-1}]_{11} = [T^{-1}]_{11} for a
    symmetric Jacobi matrix J and its monic (unit-subdiagonal) form
    T = D J D^{-1}.  [Horn & Johnson op. cit. Sec. 1.3.]

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; no RNG seat.
    AC scans: the CERTIFICATE-path functions (exact_wall_data /
    chebyshev_monic / radau_exact / fr_solve / pd_exact /
    cert_floor_exact / chol_iv) and the float bound-path functions
    (wall_moments / lanczos_pair / radau_upper / sigma_bound_source /
    required_floor) carry no read, no eigensolver, no pivot read, no
    ladder identifier -- entries and frozen constants only (CCLXV /
    CCLXXVII ban list verbatim).
 W  ladder rebuilt read-only (42 surface rungs -> 68 = 40 + 1 + 27
    steps); step keys warded against the stored CCXLVII artifact.
 F0 the CCLXIX / CCLXXVII F0 family rebuilt verbatim (off-ladder
    frame-A zones, descending h, cap 12; chain + nearest-anchor
    bridge steps).
 FX the CCLXIX families F1 / F2 / F4 / F5 rebuilt with the stress
    battery's parametric builders imported READ-ONLY (frame_of /
    build_rung_param / sweep_steps); BW builder ward re-run here on
    BW_N = 3 declared census zones; the F5 TAB2 = 1.6e7 table arrays
    warded BITWISE against the deployed 4e6 EXT prefix; the total
    sweep census must reproduce CCLXIX's 83 wall-legal steps.
 B/I Jacobi translation and the CCLXV identity wards per cell
    (sigma == q/n == 1 - s/n at IDENT_TIE); P1 pivot sign n > 0
    warded per cell in float AND exact rational.
 SR repro anchors: ladder sigma max 0.604556, ladder lambda_min(B)
    min 0.3496, ladder pivot min 0.082730, F0 sigma max 0.709925
    (kz 45, h 1359), family sigma maxima F1 0.468 / F2 0.518 /
    F4 0.420 / F5 0.297 (CCLXIX).
 G  the CCLXXVII K = 4 reproduction gates (certified ladder max
    0.648113; the 85-cell required-floor census: FEAS ratio trio,
    INFEAS set == {kz 45}, bridge risk point) and the kz 45 K-depth
    curve (float route K = 4..7 vs 0.8897/0.7269/0.7114/0.709925;
    exact tier == float route at K = 5, 6).
 R  the K = 5 required-floor table against SIGMA_ENV on ALL cells
    (float route; the interval cross-tier E5 confirms at the
    required floor, refuse-only).
 C  the certification: exact LDL floors (quality ward vs the float
    truth), exact Chebyshev coefficients vs float Lanczos at K = 5,
    exact Radau value vs float route at EVERY consumed depth, RB1
    exact-vs-truth at EVERY consumed depth (0 violations), node ward
    at EVERY consumed depth, the depth-escalation census, and the
    CLOSING CENSUS: best bound < 1 (exact Fraction, the Schur bar)
    and <= SIGMA_ENV (exact Fraction, the registered bar).
 X  controls-must-fire: inflated floor claim refused by BOTH tiers;
    exact-machine sanity on a synthetic diagonal matrix with known
    rational spectrum; exact RB1 at K = 5 on a synthetic diagonal
    measure (Fraction comparison); a synthetic near-1 cell (coupling
    scaled so the truth sigma ~ 1.2 > 1) must NOT certify
    sigma < 1; the x10-coupling cell must FAIL the census
    (CCLXXVII X5 pattern at the new depth).
 S  screens: tau and CCXVII c_h relocation screens (CCXLVII bars
    verbatim: PASS <= 0.30, RELOC >= 0.70) on the best bound and on
    the NEW margins 1 - bound and SIGMA_ENV - bound; h-slopes with
    2SE.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 K5-CLOSURE-COMPOSED(every built wall-legal cell certifies
   bound < 1 AND bound <= SIGMA_ENV; worst margins stated)
 K5-CLOSURE-SCHUR(every built wall-legal cell certifies bound < 1;
   the SIGMA_ENV shortfall listed precisely)
 K5-CLOSURE-PARTIAL(the cells with certified bound >= 1 listed
   precisely: cell, floor, depth, bound).
Every enum is a finite statement about the deployed ladder artifact
and the built CCLXIX wall-legal cells; NEVER an all-h statement,
NEVER an RH claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; SWEEP_EXP =
83; F0_EXP = 17; IDENT_TIE = 1e-12; TRANSLATE_TIE = 1e-8; MZERO_TIE
= 1e-7; REPRO_RTOL = 5e-2; SIGMA_MAX_REF = 0.604556; SIGMA_RTOL =
2e-3; F0_SIGMA_REF = 0.709925; F0_RTOL = 2e-3; FAM_REFS = F1 0.468 /
F2 0.518 / F4 0.420 / F5 0.297 (rtol 5e-2); LAMB_MIN_REF = 0.3496;
PIV_MIN_REF = 0.082730; KBASE = 4; KDEEP = 5; KESC = 6; KCURVE = 7;
CURVE_REF = {4: 0.8897, 5: 0.7269, 6: 0.7114, 7: 0.709925} with
CURVE_RTOL = 2e-3; RADAU4_CERT_REF = 0.648113 (rtol 2e-3);
RATIO_MED_REF = 0.1583; RATIO_MAX_REF = 0.7779; BRIDGE_CREQ_REF =
0.034904 (rtol 5e-2); SCHUR_BAR = 1 (exact); SIGMA_ENV = 7809/10000
(CCLXIX registration, consumed at the cited 4-digit truncation --
truncation direction makes the bar HARDER); TSTAR_POS = 8828/10000
(reported only); BIS_ITERS = 40 (round 62); REQ_ITERS = 60; REQ_LO =
1e-12; RADAU_SIGN_TIE = 1e-12; XR_TIE = 1e-6; COEF_TIE = 1e-6;
CERT_GAP_RTOL = 1e-6; NODE_TIE = 1e-9; F0_CAP = 12; F1_BAND =
(64, 2900); F1_CAP = 14; F2_NU = (5, 6, 8); F2_NKZ = 4; F4_NKZ = 6;
TAB2 = 1.6e7; KZ2_MAX = 800; H5_CAP = 4200; N5 = 4; BW_N = 3; BW_TIE
= 1e-12; CTRL_STEPS = 3; CTRL_INFLATE = 1.01; CTRL_COUPLE = 10.0;
CTRL_SIG_NEAR = 1.2; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; runtime
cap 20 min.  Smoke: 10 contiguous surface rungs + 3 lowest deep;
F0_CAP 2, F1_CAP 3, F2_NU (6,) x 1 kz, F4 1 kz, F5 SKIPPED (typed);
count / repro gates decide only on the frozen build (CCLXV T5
pattern) and print their subset values.

HONEST AMENDMENTS (declared before the frozen run).
 A1 CCLXXVII printed its per-cell K = 4 table in the run log but
    archived no artifact file; the K = 4 reproduction gates are
    therefore its FROZEN AGGREGATES (certified ladder max 0.648113,
    the FEAS ratio census med/max, the INFEAS set = exactly the
    kz 45 cell, the bridge risk point) plus 3 spot cells printed --
    disclosed, not hidden.
 A2 the F1 / F2 / F4 / F5 builders are imported READ-ONLY from
    sigma_stress_battery_probe (CCLXIX) rather than re-derived; the
    BW builder ward (parametric builder == ob.build_rung on BW_N
    declared census zones) is RE-RUN here, and the wall-legality
    definition is CCLXIX's verbatim.  Reuse, not re-derivation;
    disclosed.
 A3 the mission cites the concurrent edge scan as fdae3b68 and the
    rigor lane as d7a7e574; the working-tree doc SHAs read b320c1a5
    and 238499bf at this probe's freeze time (concurrent agents,
    mid-flight).  Both are cited as OPEN residue by citation key
    only -- NO number of either probe is consumed anywhere in this
    probe's certificates or gates.
 A4 the best bound = min over the consumed depths K needs NO
    monotonicity-in-K assumption: each depth's exact Radau value is
    an INDEPENDENTLY warded upper bound for the same q (RB1 at that
    depth), so the minimum of finitely many warded upper bounds is
    an upper bound.  Disclosed as the selection rule.
 A5 the certificate object is the ASSEMBLED float64 wall matrix
    (dyadic-rational entries, CCVII v897 class) -- CCLXXVII A3
    verbatim: the float64-vs-ideal enclosure stays with the pg_chain
    interval program (round 63 / CCXLI) and is NOT retried here; it
    is typed as the known scope edge of the composed chain.
 A6 the K = 4 depth is kept and computed on every cell alongside
    K = 5 (the reproduction anchor and the cheap first rung of the
    escalation); the escalation to K = 6 fires only when the
    K <= 5 best exceeds SIGMA_ENV -- the rule is frozen here,
    before any frozen-run number is seen.
 A7 POST-FREEZE AMENDMENT (disclosed, the CCLXXI A3 pattern):
    FROZEN RUN 1 (SPEC_SHA cc44c4e7, 289.9 s, killed K3 at G2)
    failed ONLY at the depth-curve gate's TARGET SELECTION: the F0
    family contains TWO kz 45 cells (the chain step, truth sigma
    0.286536, and the bridge step, truth sigma 0.709925 = the
    CCLXXVII diagnostic cell), and the gate picked the first list
    entry (the chain cell) instead of the sigma-max one.  In run 1
    everything upstream PASSED: SR4 reproduced the F0 max 0.709925
    exactly ON the bridge cell, G4 found the K = 4 INFEAS census =
    exactly that cell at bound 0.8897, the sweep census reproduced
    83/83, and G3 tied the exact tier to the float route at
    3.3e-16 -- the failure is the gate aiming at the wrong of two
    same-kz cells, not a certification or reproduction failure.
    THE ONLY CHANGE for run 2: the target cell is the sigma-max
    kz 45 cell (mathematically the cell CCLXXVII's diagnostic
    names).  No bar, control, screen, census rule or enum touched;
    the change cannot make the CLOSURE census easier (the census
    runs on ALL cells regardless).
 A8 POST-FREEZE AMENDMENT 2 (disclosed): FROZEN RUN 2 (SPEC_SHA
    3508c9ee, 296.6 s, 47/47 checks, no kills, verdict
    K5-CLOSURE-COMPOSED) was fully green, but its NARRATIVE text
    (not a check, not the verdict line) printed the same
    duplicate-kz slip in one place: 'the kz 45 cell closes at K = 5
    (certified bound 0.295874)' named the CHAIN kz 45 cell's bound
    instead of the sigma-max BRIDGE cell's 0.726909 (which the
    verdict line correctly states as the worst bound).  THE ONLY
    CHANGE for run 3 (the run of record): that one print selects
    the max bound over the kz 45 cells.  No check, bar, control,
    screen, census rule or enum touched; every check result of run
    2 is unchanged by construction.

SMOKE DISCLOSURE (2026-08-12, ONE smoke configuration before this
 freeze, deterministic and invoked twice with ZERO code change in
 between -- once for the decision, once to re-print the head for
 this record; everything that changed between the smoke and this
 freeze is listed here, and NO change makes a positive verdict
 easier).
 SMOKE-1 (SPEC_SHA 9f98dc3e, 10 contiguous surface rungs + 3 lowest
 deep rungs -> 11 ladder steps, F0 cap 2 -> 1 cell, F1 cap 3 -> 3
 cells (one CORE-SHORT censused), F2 (6,) x 1 -> 1, F4 1 -> 1, F5
 typed SKIPPED = 17 cells total, 11.7 s, 46 checks, 0 failed, no
 kills) measured: identity wards at machine precision (B2 6.2e-18,
 B3 9.0e-14, I1/I2 2.3e-15 / 2.8e-15, I3 2.8e-15), the BW builder
 ward exact 0.0e0 on 3 zones, the exact Chebyshev monic
 coefficients against float Lanczos at K = 5 at 7.3e-15, the
 exact-rational Radau value against the float route at 2.6e-15
 across ALL consumed depths (and 5.6e-17 on the G3 cell at K = 5
 and 6), RB1 ZERO violations at every consumed depth and the node
 ward clean, the exact LDL floor within 4.3e-13 (rel) of the float
 truth on every cell with zero refusals, the interval cross-tier
 confirming 17/17 required floors with zero REFUSED-WIDTH, the
 smoke closure census 17/17 bound < 1 AND <= SIGMA_ENV (worst Schur
 margin 0.4368 on the fake smoke bridge kz 177 h 1219 -- the known
 CCLIII/CCLXI smoke phenomenon, not a frozen-ladder cell), zero
 K = 6 escalations on the smoke subset, and ALL SIX controls firing
 (inflated claims refused by BOTH tiers 3/3; the synthetic-diagonal
 floor bracket exact with PD refused exactly AT the spectrum edge;
 exact RB1 at K = 5 9.064858 >= 9 as a Fraction comparison; the
 near-1 control truth sigma 1.2000 -> certified K = 5 bound 1.2126
 > 1 NOT certified; the x10-coupling census control FAILED the
 census at bound 12.58); all six relocation screens PASS (|slopes|
 <= 0.151).  The smoke-bypassed gates (W4b key match 5/11 on the
 subset, SR1-SR5, G1 subset 0.586029, G2 run on the substitute F0
 cell kz 116 because kz 45 is absent from the 2-zone smoke pick,
 G4 subset INFEAS empty / bridge c_req 0.001065 on the fake smoke
 bridge, FX2 subset 6) printed their subset values and decide only
 on the frozen build, exactly like CCLXXVII's T5 pattern.
 CHANGES made after SMOKE-1: NONE in code, bars, controls, screens
 or verdict enums -- the only edit is this disclosure text itself.
 The SPEC SHA moves with this text, as disclosed.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXXIX line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder + wall
blocks), zolotarev_phase_filter_probe (CCXXV step assembly),
sigma_coupling_pivot_probe (CCLXV machinery, reproduced locally,
cited), sigma_stress_battery_probe (CCLXIX families, builders
imported READ-ONLY, cited), bfloor_perstep_certification_probe
(CCLXXVII exact machine, reproduced verbatim, cited),
pg_chain_interval_rollout_probe (round 62 exact LDL machine, via
CCLXXVII, cited), euler_phase_identity_probe (CCXVII c_h),
v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_k5_closure_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_k5_closure_probe.py
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

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)
import sigma_stress_battery_probe as bat      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
SWEEP_EXP = 83
F0_EXP = 17
IDENT_TIE = 1.0e-12
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
REPRO_RTOL = 5.0e-2
SIGMA_MAX_REF = 0.604556
SIGMA_RTOL = 2.0e-3
F0_SIGMA_REF = 0.709925
F0_RTOL = 2.0e-3
FAM_REFS = {"F1": 0.468, "F2": 0.518, "F4": 0.420, "F5": 0.297}
LAMB_MIN_REF = 0.3496
PIV_MIN_REF = 0.082730
KBASE = 4
KDEEP = 5
KESC = 6
KCURVE = 7
CURVE_REF = {4: 0.8897, 5: 0.7269, 6: 0.7114, 7: 0.709925}
CURVE_RTOL = 2.0e-3
RADAU4_CERT_REF = 0.648113
RADAU4_CERT_RTOL = 2.0e-3
RATIO_MED_REF = 0.1583
RATIO_MAX_REF = 0.7779
BRIDGE_CREQ_REF = 0.034904
SCHUR_BAR = Fraction(1)
SIGMA_ENV = Fraction(7809, 10000)
TSTAR_POS = Fraction(8828, 10000)
BIS_ITERS = 40
REQ_ITERS = 60
REQ_LO = 1.0e-12
RADAU_SIGN_TIE = 1.0e-12
XR_TIE = 1.0e-6
COEF_TIE = 1.0e-6
CERT_GAP_RTOL = 1.0e-6
NODE_TIE = 1.0e-9
F0_CAP = 12
F1_BAND = (64, 2900)
F1_CAP = 14
F2_NU = (5, 6, 8)
F2_NKZ = 4
F4_NKZ = 6
TAB2 = 16_000_000
KZ2_MAX = 800
H5_CAP = 4200
N5 = 4
BW_N = 3
BW_TIE = 1.0e-12
CTRL_STEPS = 3
CTRL_INFLATE = 1.01
CTRL_COUPLE = 10.0
CTRL_SIG_NEAR = 1.2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: the bound/certificate path may see wall ENTRIES and frozen
# constants only -- no read, no pivot read, no eigensolver, no ladder
# identifier (CCLXV / CCLXXVII DERIV ban list verbatim).
DERIV_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h", "gap", "lamB1", "sigma", "sigma_quotient",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "theta", "row", "rows", "step", "steps")
CERT_FUNCS = ("exact_wall_data", "chebyshev_monic", "radau_exact",
              "fr_solve", "pd_exact", "cert_floor_exact", "chol_iv")
FLOAT_FUNCS = ("wall_moments", "lanczos_pair", "radau_upper",
               "sigma_bound_source", "required_floor")

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


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# =========================================== Jacobi form (CCLIII)
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


def theta_matrices(theta):
    """theta = (b_1..b_8, a_1..a_7) -> (J, J_B) (CCLXI verbatim)."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def sigma_quotient(theta):
    """sigma = a_1^2 [J_B^-1]_11 / b_1 (CCLXI verbatim)."""
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


# ============= float bound path (CCLXV verbatim, AC-scanned)
def wall_moments(matrix, kdeg):
    """nu_k = b^T B^k b, k = 0..kdeg, from the ENTRIES of the wall
    matrix.  No eigensolver, no inverse, no pivot read."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    out = []
    cur = vec.copy()
    for _k in range(kdeg + 1):
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


def sigma_bound_source(matrix, floor_c, kdeg):
    """THE SOURCE-ONLY BOUND (CCLXV verbatim): sigma <=
    RADAU_K(nu; floor_c) / n from the wall ENTRIES and the floor."""
    piv = float(np.asarray(matrix, float)[0, 0])
    lan = lanczos_pair(matrix, kdeg)
    if lan is None or piv <= 0.0:
        return float("nan"), None
    alp, bet, mass = lan
    val, jac = radau_upper(alp, bet, floor_c, mass)
    if not math.isfinite(val):
        return float("nan"), None
    return val / piv, jac


def required_floor(matrix, tgt, kdeg, flo_hi):
    """THE REQUIRED FLOOR (CCLXXVII verbatim, amendment A1 there):
    the smallest c in [REQ_LO, flo_hi] with sigma_bound(c) <= tgt.
    Returns (c_req, status): status FEAS / ANY / INFEAS."""
    val_hi, _ = sigma_bound_source(matrix, flo_hi, kdeg)
    if not math.isfinite(val_hi) or val_hi > tgt:
        return float("nan"), "INFEAS"
    val_lo, _ = sigma_bound_source(matrix, REQ_LO, kdeg)
    if math.isfinite(val_lo) and val_lo <= tgt:
        return REQ_LO, "ANY"
    lo, hi = REQ_LO, flo_hi
    for _ in range(REQ_ITERS):
        mid = 0.5 * (lo + hi)
        val, _ = sigma_bound_source(matrix, mid, kdeg)
        if math.isfinite(val) and val <= tgt:
            hi = mid
        else:
            lo = mid
    return hi, "FEAS"


# ============ the exact-rational tier (round 62 + E4, AC-scanned)
def exact_wall_data(matrix, kdeg):
    """Pivot n, b-weighted moments nu_0..nu_kdeg and the co-block,
    ALL as exact Fractions of the dyadic float64 ENTRIES (CCVII v897
    class).  No eigensolver, no inverse, no read."""
    mm = np.asarray(matrix, float)
    dim = mm.shape[0] - 1
    piv = Fraction(float(mm[0, 0]))
    vec = [Fraction(float(v)) for v in mm[1:, 0]]
    blk = [[Fraction(float(mm[i + 1, j + 1])) for j in range(dim)]
           for i in range(dim)]
    cur = list(vec)
    momv = []
    for _k in range(kdeg + 1):
        momv.append(sum(a * c for a, c in zip(vec, cur)))
        cur = [sum(blk[i][j] * cur[j] for j in range(dim))
               for i in range(dim)]
    return piv, momv, blk


def chebyshev_monic(momv, kdeg):
    """E4 Chebyshev algorithm, EXACT and depth-generic: monic
    recurrence al_1..al_{k-1}, be_1..be_{k-1} (be = squared symmetric
    betas) of the measure with power moments momv[0..2k-2].  None on
    degeneracy (a be <= 0)."""
    need = 2 * kdeg - 1
    if len(momv) < need or momv[0] <= 0:
        return None
    tab = {-1: [Fraction(0)] * need, 0: list(momv[:need])}
    al = [momv[1] / momv[0]]
    be = []
    for k in range(1, kdeg):
        prev = tab[k - 1]
        pprev = tab[k - 2]
        cur = [Fraction(0)] * need
        for pos in range(k, 2 * kdeg - 1 - k):
            cur[pos] = (prev[pos + 1] - al[k - 1] * prev[pos]
                        - (be[k - 2] * pprev[pos] if k >= 2
                           else Fraction(0)))
        tab[k] = cur
        if prev[k - 1] <= 0 or cur[k] <= 0:
            return None
        be.append(cur[k] / prev[k - 1])
        if 2 * kdeg - 1 - k > k + 1:
            al.append(cur[k + 1] / cur[k] - prev[k] / prev[k - 1])
    if len(al) != kdeg - 1 or len(be) != kdeg - 1:
        return None
    return al, be


def fr_solve(amat, rhs):
    """Exact Gaussian elimination with partial (nonzero) pivoting on
    Fractions; returns the solution list or None if singular."""
    dim = len(amat)
    aa = [list(r) + [rhs[i]] for i, r in enumerate(amat)]
    for k in range(dim):
        pr = None
        for i in range(k, dim):
            if aa[i][k] != 0:
                pr = i
                break
        if pr is None:
            return None
        aa[k], aa[pr] = aa[pr], aa[k]
        pv = aa[k][k]
        for i in range(k + 1, dim):
            f = aa[i][k] / pv
            if f == 0:
                continue
            for j in range(k, dim + 1):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    out = [Fraction(0)] * dim
    for k in range(dim - 1, -1, -1):
        acc = aa[k][dim]
        for j in range(k + 1, dim):
            acc = acc - aa[k][j] * out[j]
        out[k] = acc / aa[k][k]
    return out


def radau_exact(al, be, flo, mass):
    """EXACT-RATIONAL Gauss-Radau upper-bound value for the 1/x
    integral at depth K = len(al)+1 with the node prescribed at flo:
    monic form (E6: diagonal entries of the inverse are invariant
    under the diagonal similarity to the symmetric Jacobi form).
    None on a singular solve.  Depth-generic (CCLXXVII verbatim)."""
    kdeg = len(al) + 1
    dim = kdeg - 1
    tm = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(dim):
        tm[i][i] = al[i] - flo
        if i + 1 < dim:
            tm[i][i + 1] = be[i]
            tm[i + 1][i] = Fraction(1)
    rhs = [Fraction(0)] * dim
    rhs[dim - 1] = Fraction(1)
    sol = fr_solve(tm, rhs)
    if sol is None:
        return None
    alr = flo + be[kdeg - 2] * sol[dim - 1]
    tt = [[Fraction(0)] * kdeg for _ in range(kdeg)]
    for i in range(kdeg):
        tt[i][i] = al[i] if i < kdeg - 1 else alr
        if i + 1 < kdeg:
            tt[i][i + 1] = be[i]
            tt[i + 1][i] = Fraction(1)
    rhs2 = [Fraction(0)] * kdeg
    rhs2[0] = Fraction(1)
    sol2 = fr_solve(tt, rhs2)
    if sol2 is None:
        return None
    return mass * sol2[0]


def pd_exact(afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision (round 62 verbatim): is
    A - shift I PD?"""
    dim = len(afr)
    aa = [[afr[i][j] - (shift if i == j else 0) for j in range(dim)]
          for i in range(dim)]
    for k in range(dim):
        p = aa[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, dim):
            f = aa[i][k] / p
            for j in range(k + 1, dim):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    return True, -1


def cert_floor_exact(afr, lo, hi, iters=BIS_ITERS):
    """Largest certified c in [lo, hi] with A - c I PD (round 62
    verbatim: dyadic bisection; the final decision re-run exactly;
    NEVER rounded inward).  None if even lo is refused."""
    lo = Fraction(lo)
    hi = Fraction(hi)
    if hi < lo:
        hi = lo
    ok, _ = pd_exact(afr, lo)
    if not ok:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok, _ = pd_exact(afr, mid)
        if ok:
            lo = mid
        else:
            hi = mid
    ok, _ = pd_exact(afr, lo)
    assert ok
    return lo


def chol_iv(blk, shift):
    """Directed-rounding float64 interval Cholesky/LDL of
    (blk - shift I): returns True iff EVERY symmetric matrix within
    one outward ulp of the exact elimination is PD (E5), None on a
    pivot interval touching <= 0 (REFUSED -- never a denial)."""
    nxt = np.nextafter

    def i_sub(alo, ahi, blo, bhi):
        return nxt(alo - bhi, -np.inf), nxt(ahi - blo, np.inf)

    def i_mul(alo, ahi, blo, bhi):
        cand = (alo * blo, alo * bhi, ahi * blo, ahi * bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    def i_div(alo, ahi, blo, bhi):
        cand = (alo / blo, alo / bhi, ahi / blo, ahi / bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    dim = blk.shape[0]
    alo = np.array(blk, float)
    ahi = np.array(blk, float)
    for i in range(dim):
        alo[i, i], ahi[i, i] = i_sub(alo[i, i], ahi[i, i],
                                     shift, shift)
    for k in range(dim):
        plo, phi = alo[k, k], ahi[k, k]
        if not (plo > 0.0):
            return None
        for i in range(k + 1, dim):
            flo, fhi = i_div(alo[i, k], ahi[i, k], plo, phi)
            for j in range(k + 1, dim):
                qlo, qhi = i_mul(flo, fhi, alo[k, j], ahi[k, j])
                alo[i, j], ahi[i, j] = i_sub(alo[i, j], ahi[i, j],
                                             qlo, qhi)
    return True


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
    return zones, steps, census, combined


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


def build_f0(anchors):
    """The CCLXIX / CCLXXVII F0 family verbatim: off-ladder frame-A
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
        print("    F0 surf kz %-4d h %-5s %s [%.1f s]"
              % (kz, ob.window_of(kz)["h"],
                 "OK" if rr is not None else "SHORT",
                 time.time() - T0), flush=True)
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
    check("F0.1 the CCLXIX F0 family admitted %d wall-legal cells "
          "(frozen expectation %d)" % (len(out), F0_EXP),
          (len(out) >= 1) if SMOKE else (len(out) == F0_EXP),
          kill="K1")
    return out


def build_families(census, combined):
    """The CCLXIX families F1/F2/F4/F5, rebuilt with the stress
    battery's parametric builders imported READ-ONLY (amendment A2);
    BW builder ward re-run here; F5 TAB2 prefix warded bitwise."""
    section("FX -- the CCLXIX families F1/F2/F4/F5 (builders "
            "imported READ-ONLY from the stress battery)")
    # BW builder ward on declared census zones (CCLXIX verbatim)
    bw_kz = [kz for kz, _hz in census[:BW_N]]
    d_bw = 0.0
    for kz in bw_kz:
        ref = ob.build_rung("deep", kz, with_split=False)
        alpha, mz, _hz, uu, mm = bat.frame_of(
            ob.EXT["U"], ob.EXT["G"], ob.EXT["MU"], kz, 4)
        par = bat.build_rung_param(kz, alpha, mz, uu, mm)
        for key in ("tau", "lamS"):
            d_bw = max(d_bw, abs(par[key] - ref[key])
                       / max(1.0, abs(ref[key])))
        d_bw = max(d_bw, abs(par["h"] - ref["h"]))
    check("FX0 BW builder ward: parametric builder == ob.build_rung "
          "on %d census zones: max rel %.2e <= %.0e"
          % (len(bw_kz), d_bw, BW_TIE), d_bw <= BW_TIE, kill="K2")

    families = {}
    censuses = {}
    reg_deep = {kz for kz, _hz in ob.deep_zone_census()}
    reg_surf = set(ob.ladder_zones())

    # F1 deep off-ladder kz on the deployed table (CCLXIX verbatim)
    f1_cap = 3 if SMOKE else F1_CAP
    f1_all = []
    for kz in range(2, ob.KZ_SCAN_MAX):
        alpha, _mz, hz, _ka = ob.ext_frame(kz)
        x_val = math.exp(2.0 * alpha)
        if (F1_BAND[0] <= hz <= F1_BAND[1] and x_val <= ob.TAB_EXT
                and kz not in reg_deep and kz not in reg_surf):
            f1_all.append(kz)
    stride = max(1, len(f1_all) // f1_cap)
    f1_pick = f1_all[::stride][:f1_cap]
    f1_rungs = []
    n_core_short = 0
    for kz in f1_pick:
        r = ob.build_rung("deep", kz, with_split=False)
        ok = r is not None and r.get("core_ok")
        if r is not None and not r.get("core_ok"):
            n_core_short += 1
        if ok:
            f1_rungs.append(r)
        print("    F1 deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, ob.ext_frame(kz)[2],
                 "OK" if ok else "CORE-SHORT/FAIL",
                 time.time() - T0), flush=True)
    families["F1"], ref1 = bat.sweep_steps(f1_rungs, "F1", None,
                                           combined)
    censuses["F1"] = ("%d qualifying kz, stride %d -> %d picked, "
                      "%d built, %d CORE-SHORT, %d step-refused"
                      % (len(f1_all), stride, len(f1_pick),
                         len(f1_rungs), n_core_short, ref1))

    # F2 density nu > 4 (CCLXIX verbatim)
    f2_nu = (6,) if SMOKE else F2_NU
    f2_nkz = 1 if SMOKE else F2_NKZ
    f2_kz = [kz for kz, _hz in census[:f2_nkz]]
    f2_rungs = []
    for nu in f2_nu:
        for kz in f2_kz:
            alpha, mz, hz, uu, mm = bat.frame_of(
                ob.EXT["U"], ob.EXT["G"], ob.EXT["MU"], kz, nu)
            r = bat.build_rung_param(kz, alpha, mz, uu, mm)
            r["nu"] = nu
            ok = r.get("core_ok") and "fail" not in r
            if ok:
                f2_rungs.append(r)
            print("    F2 nu %d kz %-4d h %-5d %s [%.1f s]"
                  % (nu, kz, hz, "OK" if ok
                     else r.get("fail", "FAIL"),
                     time.time() - T0), flush=True)
    families["F2"], ref2 = bat.sweep_steps(f2_rungs, "F2", None,
                                           combined)
    censuses["F2"] = ("%d nu-variants attempted, %d built, %d "
                      "step-refused"
                      % (len(f2_nu) * len(f2_kz), len(f2_rungs),
                         ref2))

    # F4 off-anchor alpha (CCLXIX verbatim)
    f4_nkz = 1 if SMOKE else F4_NKZ
    f4_kz = [kz for kz, _hz in census[:f4_nkz]]
    f4_rungs = []
    for kz in f4_kz:
        alpha_mid = 0.5 * (float(ob.EXT["U"][kz])
                           + float(ob.EXT["U"][kz + 1]))
        alpha, mz, hz, uu, mm = bat.frame_of(
            ob.EXT["U"], ob.EXT["G"], ob.EXT["MU"], kz, 4,
            alpha=alpha_mid)
        r = bat.build_rung_param(kz, alpha, mz, uu, mm)
        r["mode"] = "mid-alpha"
        ok = r.get("core_ok") and "fail" not in r
        if ok:
            f4_rungs.append(r)
        print("    F4 mid-alpha kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if ok else r.get("fail", "FAIL"),
                 time.time() - T0), flush=True)
    families["F4"], ref4 = bat.sweep_steps(f4_rungs, "F4", None,
                                           combined)
    censuses["F4"] = ("%d mid-alpha frames attempted, %d built, %d "
                      "step-refused"
                      % (len(f4_kz), len(f4_rungs), ref4))

    # F5 depth extension (TAB2 table, CCLXIX verbatim)
    if SMOKE:
        censuses["F5"] = "SMOKE-SKIPPED (typed)"
        families["F5"] = []
        print("    F5 SMOKE-SKIPPED (typed)")
    else:
        lam2 = core.von_mangoldt_table(TAB2)
        nn2 = np.nonzero(lam2 > 0.0)[0]
        u2 = np.log(nn2.astype(float))
        mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
        g2 = np.diff(u2)
        n_pref = len(ob.EXT["NN"])
        check("FX5 TAB2 prefix ward: 1.6e7 arrays agree bitwise "
              "with the deployed 4e6 EXT arrays",
              (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
               and np.array_equal(u2[:n_pref], ob.EXT["U"])
               and np.array_equal(mu2[:n_pref], ob.EXT["MU"])),
              kill="K2")
        f5_new = []
        for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
            alpha = float(u2[kz])
            d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
            mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
            if mz % 2:
                mz += 1
            hz = mz // 2
            x_val = math.exp(2.0 * alpha)
            if x_val > TAB2 or kz in reg_deep:
                continue
            newly = ((2900 < hz) or
                     (x_val > ob.TAB_EXT and 128 <= hz))
            if not newly:
                continue
            if hz <= H5_CAP:
                f5_new.append((hz, kz, alpha, mz, x_val))
        f5_new.sort(reverse=True)
        f5_pick = f5_new[:N5]
        f5_rungs = []
        for hz, kz, alpha, mz, x_val in f5_pick:
            ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14,
                                     side="right"))
            r = bat.build_rung_param(kz, alpha, mz, u2[:ka].copy(),
                                     mu2[:ka].copy())
            r["mode"] = "depth-ext"
            ok = r.get("core_ok") and "fail" not in r
            if ok:
                f5_rungs.append(r)
            print("    F5 deep-ext kz %-4d h %-5d X %.3g %s [%.1f s]"
                  % (kz, hz, x_val, "OK" if ok
                     else r.get("fail", "FAIL"),
                     time.time() - T0), flush=True)
        families["F5"], ref5 = bat.sweep_steps(f5_rungs, "F5", None,
                                               combined)
        censuses["F5"] = ("%d newly reachable frames, %d picked, %d "
                          "built, %d step-refused"
                          % (len(f5_new), len(f5_pick),
                             len(f5_rungs), ref5))
    for fam, cen in sorted(censuses.items()):
        print("    census %s: %s" % (fam, cen))
    n_fx = sum(len(v) for v in families.values())
    check("FX1 families admitted %d wall-legal cells (%s)"
          % (n_fx, ", ".join("%s %d" % (k, len(v))
                             for k, v in sorted(families.items()))),
          n_fx >= (2 if SMOKE else 8), kill="K1")
    return families


def make_rows(steps, f0_cells, families):
    rows = []
    for st in steps:
        rows.append(dict(step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         mode="ladder"))
    for st, kind in f0_cells:
        rows.append(dict(step=st, seg="F0",
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         mode=kind))
    for fam in sorted(families):
        for d in families[fam]:
            st = d["step"]
            rows.append(dict(step=st, seg=fam,
                             h=float(st["r2"]["h"]),
                             kz=int(st["r2"]["kz"]),
                             tau_scale=float(st["tau"]),
                             schur=float(st["gap"]),
                             n_piv=float(st["n0"]),
                             lam_b=float(st["lamB1"]),
                             mode=d["mode"]))
    for i, r in enumerate(rows):
        r["index"] = i
    return rows


# ============================= B/I: translation + identity wards
def jacobi_identity_wards(rows):
    section("B/I -- Jacobi translation + the CCLXV identity wards "
            "on every cell")
    d_b1 = d_a1 = d_bfl = d_m0 = d_q = d_sig = d_gap = 0.0
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
    check("I3 IDENTITY sigma == 1 - s/n: max rel %.2e <= %.0e"
          % (d_gap, IDENT_TIE), d_gap <= IDENT_TIE, kill="K2")
    return [r for r in rows if r["theta"] is not None]


def pivot_ward(rows):
    n_pos = 0
    n_pos_exact = 0
    for row in rows:
        if row["n_piv"] > 0.0:
            n_pos += 1
        if Fraction(float(row["step"]["Mt"][0, 0])) > 0:
            n_pos_exact += 1
    pivs = [r["n_piv"] for r in rows]
    check("P1 PIVOT SIGN n = M[0,0] > 0 on all %d cells (float AND "
          "exact rational): %d / %d positive, min %.6f"
          % (len(rows), n_pos, n_pos_exact, min(pivs)),
          n_pos == len(rows) and n_pos_exact == len(rows), kill="K2")


def repro_anchors(rows):
    section("SR -- repro anchors against CCLXV/CCLXIX/CCLXXVII")
    lad = [r for r in rows if r["seg"] in ("surf", "bridge", "deep")]
    f0 = [r for r in rows if r["seg"] == "F0"]
    sig_max = max(r["sigma"] for r in lad)
    lam_min = min(r["lam_b"] for r in lad)
    piv_min = min(r["n_piv"] for r in lad)
    check("SR1 ladder sigma max %.6f reproduces %.6f (rtol %.0e)"
          % (sig_max, SIGMA_MAX_REF, SIGMA_RTOL),
          SMOKE or abs(sig_max / SIGMA_MAX_REF - 1.0) <= SIGMA_RTOL,
          kill="K3")
    check("SR2 ladder lambda_min(B) min %.4f reproduces %.4f "
          "(rtol %.0e)" % (lam_min, LAMB_MIN_REF, REPRO_RTOL),
          SMOKE or abs(lam_min / LAMB_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")
    check("SR3 ladder pivot min %.6f reproduces %.6f (rtol %.0e)"
          % (piv_min, PIV_MIN_REF, REPRO_RTOL),
          SMOKE or abs(piv_min / PIV_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")
    if f0:
        f0_max = max(r["sigma"] for r in f0)
        i_mx = max(f0, key=lambda r: r["sigma"])
        print("    F0 sigma max %.6f at kz %d h %.0f mode %s "
              "(CCLXIX 0.709925 at kz 45 h 1359)"
              % (f0_max, i_mx["kz"], i_mx["h"], i_mx["mode"]))
        check("SR4 F0 sigma max %.6f reproduces %.6f (rtol %.0e)"
              % (f0_max, F0_SIGMA_REF, F0_RTOL),
              SMOKE or abs(f0_max / F0_SIGMA_REF - 1.0) <= F0_RTOL,
              kill="K3")
    fam_bad = []
    for fam, ref in sorted(FAM_REFS.items()):
        sub = [r["sigma"] for r in rows if r["seg"] == fam]
        if not sub:
            if not SMOKE:
                fam_bad.append("%s EMPTY" % fam)
            continue
        mx = max(sub)
        print("    %s sigma max %.4f (CCLXIX %.3f)" % (fam, mx, ref))
        if not SMOKE and abs(mx / ref - 1.0) > REPRO_RTOL:
            fam_bad.append("%s %.4f vs %.3f" % (fam, mx, ref))
    check("SR5 family sigma maxima reproduce CCLXIX (rtol %.0e): %s"
          % (REPRO_RTOL, "; ".join(fam_bad) or "all match"),
          SMOKE or not fam_bad, kill="K3")
    for seg in ("surf", "bridge", "deep", "F0", "F1", "F2", "F4",
                "F5"):
        sub = [r["sigma"] for r in rows if r["seg"] == seg]
        if sub:
            print("      sigma %-6s (%2d): %s" % (seg, len(sub),
                                                  f4(sub)))


# ================== G: the CCLXXVII K = 4 reproduction gates
def k4_repro(rows):
    section("G -- reproduce CCLXXVII's K = 4 tier + the kz 45 "
            "K-depth curve")
    old = [r for r in rows
           if r["seg"] in ("surf", "bridge", "deep", "F0")]
    # G4: the CCLXXVII required-floor census on its 85 cells (K = 4,
    # TARGET = SIGMA_ENV -- the binding bar there, amendment A1)
    tgt = float(SIGMA_ENV)
    n_feas = n_any = 0
    infeas = []
    ratios = []
    for row in old:
        c_req, status = required_floor(row["step"]["Mt"], tgt, KBASE,
                                       row["lam_b"])
        row["c_req4"] = c_req
        if status == "INFEAS":
            infeas.append(row)
        elif status == "ANY":
            n_any += 1
        else:
            n_feas += 1
            ratios.append(c_req / row["lam_b"])
    tr = trio(ratios)
    print("    K=4 required/measured floor ratio (FEAS cells): %s"
          % f4(ratios))
    for r in infeas:
        val, _ = sigma_bound_source(r["step"]["Mt"], r["lam_b"],
                                    KBASE)
        print("      K=4 INFEASIBLE cell: %s kz %d h %.0f -- bound "
              "at the measured floor %.4f"
              % (r["seg"], r["kz"], r["h"], val))
    brg = [r for r in old if r["seg"] == "bridge"]
    bridge_ok = True
    for r in brg:
        print("    bridge risk point: lambda_min(B) = %.6f, "
              "c_req(K=4) = %.6f (CCLXXVII 0.034904)"
              % (r["lam_b"], r["c_req4"]))
        bridge_ok = (math.isfinite(r["c_req4"]) and
                     abs(r["c_req4"] / BRIDGE_CREQ_REF - 1.0)
                     <= REPRO_RTOL)
    ok_g4 = (SMOKE
             or (abs(tr[1] / RATIO_MED_REF - 1.0) <= REPRO_RTOL
                 and abs(tr[2] / RATIO_MAX_REF - 1.0) <= REPRO_RTOL
                 and len(infeas) == 1
                 and infeas[0]["kz"] == 45
                 and bridge_ok))
    check("G4 CCLXXVII required-floor census reproduced: FEAS "
          "ratio med/max %.4f/%.4f vs %.4f/%.4f, INFEAS set = %s "
          "(expect exactly kz 45), bridge c_req ok %s"
          % (tr[1], tr[2], RATIO_MED_REF, RATIO_MAX_REF,
             ",".join("kz %d" % r["kz"] for r in infeas) or "empty",
             bridge_ok), ok_g4, kill="K3")
    # 3 spot cells at K = 4 (amendment A1: the printed anchor)
    for i in [0, len(old) // 2, len(old) - 1]:
        row = old[i]
        val, _ = sigma_bound_source(row["step"]["Mt"], row["lam_b"],
                                    KBASE)
        print("    spot cell %d (%s kz %d h %.0f): measured-floor "
              "K=%d bound %.6f vs truth sigma %.6f"
              % (row["index"], row["seg"], row["kz"], row["h"],
                 KBASE, val, row["sigma"]))
    return infeas


def depth_curve(rows):
    """G2/G3: the kz 45 h 1359 cell -- float depth curve K = 4..7 at
    the measured floor vs CCLXXVII's post-frozen diagnostic, and the
    exact tier tied to the float route at K = 5 and K = 6."""
    f0 = [r for r in rows if r["seg"] == "F0"]
    tgt_cell = sorted((r for r in f0 if r["kz"] == 45),
                      key=lambda r: -r["sigma"])[:1]
    if not tgt_cell:
        tgt_cell = sorted(f0, key=lambda r: -r["sigma"])[:1]
        if not tgt_cell:
            check("G2 kz 45 depth curve: NO F0 cell available",
                  SMOKE, kill="K3")
            return
        print("    (kz 45 absent on this subset; curve printed on "
              "the F0 sigma-max cell, gate smoke-bypassed)")
    row = tgt_cell[0]
    mat = row["step"]["Mt"]
    curve = {}
    bad = []
    for kd in range(KBASE, KCURVE + 1):
        val, _ = sigma_bound_source(mat, row["lam_b"], kd)
        curve[kd] = val
        ref = CURVE_REF[kd]
        if not (math.isfinite(val)
                and abs(val / ref - 1.0) <= CURVE_RTOL):
            bad.append("K=%d %.4f vs %.4f" % (kd, val, ref))
    print("    depth curve at the measured floor (kz %d h %.0f, "
          "truth sigma %.6f):" % (row["kz"], row["h"], row["sigma"]))
    for kd in sorted(curve):
        print("      K = %d: bound %.6f (CCLXXVII diagnostic %.6f)"
              % (kd, curve[kd], CURVE_REF[kd]))
    is45 = (row["kz"] == 45)
    check("G2 the kz 45 K-depth curve reproduces CCLXXVII's "
          "diagnostic (rtol %.0e): %s"
          % (CURVE_RTOL, "; ".join(bad) or "all four depths match"),
          SMOKE or (is45 and not bad), kill="K3")
    # G3: exact tier == float route at K = 5 and K = 6 on this cell
    pivf, momv, _blkf = exact_wall_data(mat, 2 * KESC - 2)
    flo = Fraction(float(row["lam_b"]))
    d_xr = 0.0
    n_deg = 0
    for kd in (KDEEP, KESC):
        cheb = chebyshev_monic(momv, kd)
        if cheb is None:
            n_deg += 1
            continue
        val_fr = radau_exact(cheb[0], cheb[1], flo, momv[0])
        if val_fr is None:
            n_deg += 1
            continue
        bfr = float(val_fr / pivf)
        d_xr = max(d_xr, abs(bfr - curve[kd])
                   / max(1.0, abs(curve[kd])))
        print("      exact tier K = %d at the measured floor: "
              "%.9f (float %.9f)" % (kd, bfr, curve[kd]))
    check("G3 exact-rational tier == float route at K = 5 and "
          "K = 6 on the kz 45 cell: max rel %.2e <= %.0e "
          "(%d degenerate)" % (d_xr, XR_TIE, n_deg),
          d_xr <= XR_TIE and n_deg == 0, kill="K2")


# ==================== R: the K = 5 required-floor table
def required_table_k5(rows):
    section("R -- the K = 5 required-floor table against SIGMA_ENV "
            "= %.4f on ALL cells" % float(SIGMA_ENV))
    tgt = float(SIGMA_ENV)
    n_feas = n_any = n_infeas = 0
    for row in rows:
        c_req, status = required_floor(row["step"]["Mt"], tgt, KDEEP,
                                       row["lam_b"])
        row["c_req"] = c_req
        row["req_status"] = status
        if status == "INFEAS":
            n_infeas += 1
        elif status == "ANY":
            n_any += 1
        else:
            n_feas += 1
    ratios = [row["c_req"] / row["lam_b"] for row in rows
              if row["req_status"] == "FEAS"]
    print("    K=5 required/measured floor ratio (FEAS cells): %s"
          % f4(ratios))
    for r in rows:
        if r["req_status"] == "INFEAS":
            val, _ = sigma_bound_source(r["step"]["Mt"], r["lam_b"],
                                        KDEEP)
            print("      K=5 INFEASIBLE cell: %s kz %d h %.0f -- "
                  "bound at the measured floor %.4f > %.4f"
                  % (r["seg"], r["kz"], r["h"], val, tgt))
    check("R1 K = 5 feasibility census vs SIGMA_ENV: %d FEAS, %d "
          "ANY, %d INFEASIBLE at the measured floor (INFEAS cells "
          "escalate to K = 6 in the certification)"
          % (n_feas, n_any, n_infeas), True)
    return n_infeas


# ==================== C: THE CERTIFICATION at depth
def certification(rows):
    section("C -- THE CERTIFICATION: exact-rational LDL floor + "
            "exact-rational Gauss-Radau at K = 4, 5 (6 on "
            "escalation) per cell")
    d_gapc = 0.0
    n_exceed = 0
    d_coef = 0.0
    d_xr = 0.0
    sign_fail = node_fail = 0
    n_refused = 0
    n_degen = 0
    iv_conf = iv_ref = 0
    n_need5 = 0
    n_need6 = 0
    esc_cells = []
    for row in rows:
        mat = row["step"]["Mt"]
        pivf, momv, blkf = exact_wall_data(mat, 2 * KDEEP - 2)
        hi_hint = Fraction(float(row["lam_b"])) * (
            Fraction(1) + Fraction(1, 10 ** 6))
        c_cert = cert_floor_exact(blkf, Fraction(0), hi_hint)
        if c_cert is None:
            n_refused += 1
            row["c_cert"] = None
            row["bound_fr"] = None
            row["k_used"] = None
            row["closes_schur"] = False
            row["closes_env"] = False
            continue
        row["c_cert"] = c_cert
        c_f = float(c_cert)
        row["c_cert_f"] = c_f
        if c_f > row["lam_b"] * (1.0 + 1e-9):
            n_exceed += 1
        d_gapc = max(d_gapc, (row["lam_b"] - c_f)
                     / max(1.0, row["lam_b"]))
        # exact Chebyshev coefficients vs float Lanczos at K = 5
        lan = lanczos_pair(mat, KDEEP)
        cheb5 = chebyshev_monic(momv, KDEEP)
        if lan is not None and cheb5 is not None:
            alp, bet, _mass = lan
            for k in range(KDEEP - 1):
                sc = max(1.0, abs(alp[k]))
                d_coef = max(d_coef, abs(float(cheb5[0][k]) - alp[k])
                             / sc)
                sc2 = max(1.0, bet[k] ** 2)
                d_coef = max(d_coef, abs(float(cheb5[1][k])
                                         - bet[k] ** 2) / sc2)
        # the depth ladder: K = 4 and K = 5 always, K = 6 on
        # escalation (amendment A6); best = min of warded values (A4)
        vals = {}
        for kd in (KBASE, KDEEP):
            cheb = chebyshev_monic(momv, kd)
            if cheb is None:
                n_degen += 1
                continue
            val_fr = radau_exact(cheb[0], cheb[1], c_cert, momv[0])
            if val_fr is None:
                n_degen += 1
                continue
            vals[kd] = val_fr / pivf
        best = min(vals.values()) if vals else None
        if best is not None and vals.get(KBASE) is not None \
                and vals[KBASE] > SIGMA_ENV:
            n_need5 += 1
        if best is not None and best > SIGMA_ENV:
            n_need6 += 1
            esc_cells.append(row)
            _p6, momv6, _b6 = exact_wall_data(mat, 2 * KESC - 2)
            cheb6 = chebyshev_monic(momv6, KESC)
            val6 = (radau_exact(cheb6[0], cheb6[1], c_cert,
                                momv6[0])
                    if cheb6 is not None else None)
            if val6 is None:
                n_degen += 1
            else:
                vals[KESC] = val6 / pivf
                best = min(best, vals[KESC])
        if best is None:
            row["bound_fr"] = None
            row["k_used"] = None
            row["closes_schur"] = False
            row["closes_env"] = False
            continue
        # wards at EVERY consumed depth: RB1 + node + exact-vs-float
        for kd, bfr in sorted(vals.items()):
            if float(bfr) * row["n_piv"] < row["q_wall"] \
                    - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                sign_fail += 1
            val_f, jac = sigma_bound_source(mat, c_f, kd)
            if math.isfinite(val_f):
                d_xr = max(d_xr, abs(float(bfr) - val_f)
                           / max(1.0, abs(val_f)))
            if jac is not None:
                node = float(np.linalg.eigvalsh(jac)[0])
                if node < c_f - NODE_TIE * max(1.0, c_f):
                    node_fail += 1
        row["bound_fr"] = best
        row["bound_f"] = float(best)
        row["k_used"] = min(kd for kd, bfr in vals.items()
                            if bfr == best)
        row["vals"] = {kd: float(v) for kd, v in vals.items()}
        # interval cross-tier at the K = 5 required floor
        if row.get("req_status") == "FEAS":
            got = chol_iv(np.asarray(row["step"]["Bblk"], float),
                          row["c_req"])
            if got:
                iv_conf += 1
            else:
                iv_ref += 1
        row["closes_schur"] = best < SCHUR_BAR
        row["closes_env"] = best <= SIGMA_ENV
    k4_lad = [r["vals"][KBASE] for r in rows
              if r.get("vals") and KBASE in r["vals"]
              and r["seg"] in ("surf", "bridge", "deep")]
    k4max = max(k4_lad) if k4_lad else float("nan")
    check("G1 REPRO CCLXXVII certified K = 4 ladder bound max "
          "%.6f vs %.6f (rtol %.0e)"
          % (k4max, RADAU4_CERT_REF, RADAU4_CERT_RTOL),
          SMOKE or abs(k4max / RADAU4_CERT_REF - 1.0)
          <= RADAU4_CERT_RTOL, kill="K3")
    check("C1 exact-rational LDL floor certified on %d/%d cells "
          "(%d REFUSED, carried)" % (len(rows) - n_refused,
                                     len(rows), n_refused),
          n_refused == 0, kill="K2")
    check("C2 floor quality: certified floor never exceeds the "
          "float truth (%d exceed) and sits within rel %.2e <= %.0e "
          "of it" % (n_exceed, d_gapc, CERT_GAP_RTOL),
          n_exceed == 0 and d_gapc <= CERT_GAP_RTOL, kill="K2")
    check("C3 exact Chebyshev monic coefficients == float Lanczos "
          "at K = %d (al, be = bet^2): max rel %.2e <= %.0e"
          % (KDEEP, d_coef, COEF_TIE), d_coef <= COEF_TIE, kill="K2")
    check("C4 exact-rational Radau value == float route at EVERY "
          "consumed depth: max rel %.2e <= %.0e (%d degenerate)"
          % (d_xr, XR_TIE, n_degen),
          d_xr <= XR_TIE and n_degen == 0, kill="K2")
    check("C5 RB1 BOUND PROPERTY WARD: the EXACT Radau value is an "
          "upper bound for the truth q at EVERY consumed depth on "
          "every cell: %d violations (0 required)" % sign_fail,
          sign_fail == 0, kill="K2")
    check("C6 node ward at the certified floor, every consumed "
          "depth: %d rules with a node below the floor" % node_fail,
          node_fail == 0, kill="K2")
    check("C7 interval cross-tier (E5, refuse-only) at the K = 5 "
          "required floor: %d confirmed, %d REFUSED-WIDTH, 0 "
          "denials possible" % (iv_conf, iv_ref), True)
    check("C8 depth-escalation census: %d cells need K = 5 (K = 4 "
          "bound > SIGMA_ENV), %d escalated to K = 6 (%s)"
          % (n_need5, n_need6,
             "; ".join("%s kz %d h %.0f" % (r["seg"], r["kz"],
                                            r["h"])
                       for r in esc_cells) or "none"), True)
    n_schur = sum(1 for r in rows if r.get("closes_schur"))
    n_env = sum(1 for r in rows if r.get("closes_env"))
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    m1 = [1.0 - r["bound_f"] for r in ok_rows]
    me = [float(SIGMA_ENV) - r["bound_f"] for r in ok_rows]
    check("C9 CLOSING CENSUS (Schur bar): certified bound < 1 on "
          "%d/%d cells; WORST margin to 1 = %.4f"
          % (n_schur, len(rows), min(m1) if m1 else float("nan")),
          True)
    check("C10 CLOSING CENSUS (registered bar): certified bound <= "
          "SIGMA_ENV %.4f on %d/%d cells; worst margin %.4f"
          % (float(SIGMA_ENV), n_env, len(rows),
             min(me) if me else float("nan")), True)
    return n_schur, n_env


def print_table(rows):
    print("\n    THE CERTIFIED CLOSURE TABLE (all built wall-legal "
          "cells):")
    print("    idx seg    kz    h      lamB_meas  c_cert     K  "
          "bound_cert  marg_1     marg_ENV   verdict")
    for row in rows:
        cc = row.get("c_cert_f", float("nan"))
        bf = row.get("bound_f", float("nan"))
        ku = row.get("k_used")
        print("    %3d %-6s %-4d %6.0f %10.4f %10.4f %2s %11.6f "
              "%10.6f %10.6f  %s"
              % (row["index"], row["seg"], row["kz"], row["h"],
                 row["lam_b"], cc, str(ku) if ku else "-", bf,
                 1.0 - bf if math.isfinite(bf) else float("nan"),
                 float(SIGMA_ENV) - bf if math.isfinite(bf)
                 else float("nan"),
                 "CLOSE" if row.get("closes_env")
                 else "SCHUR-ONLY" if row.get("closes_schur")
                 else "FAIL"))


# ================================================ X: the controls
def controls(rows):
    section("X -- controls-must-fire (the certification is not "
            "vacuous)")
    idxs = [0, len(rows) // 2, len(rows) - 1][:CTRL_STEPS]
    n_fire = 0
    n_iv_ok = 0
    for i in idxs:
        row = rows[i]
        _p, _m, blkf = exact_wall_data(row["step"]["Mt"], 0)
        claim = Fraction(float(row["lam_b"] * CTRL_INFLATE))
        ok, piv_k = pd_exact(blkf, claim)
        if not ok:
            n_fire += 1
        got = chol_iv(np.asarray(row["step"]["Bblk"], float),
                      float(claim))
        if got is not True:
            n_iv_ok += 1
        print("    X1 cell %d: claimed floor %.6f > true "
              "lambda_min %.6f -> exact LDL %s (pivot %d), interval "
              "tier %s" % (row["index"], float(claim), row["lam_b"],
                           "REFUSED" if not ok else "ACCEPTED(!)",
                           piv_k,
                           "not certified" if got is not True
                           else "certified(!)"))
    check("X1 inflated floor claim REFUSED by the exact LDL on "
          "%d/%d declared cells" % (n_fire, len(idxs)),
          n_fire == len(idxs), kill="K4")
    check("X2 inflated floor claim NOT certified by the interval "
          "tier on %d/%d declared cells" % (n_iv_ok, len(idxs)),
          n_iv_ok == len(idxs), kill="K4")
    # exact-machine sanity on a synthetic diagonal with known spectrum
    dvals = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
             Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)]
    dfr = [[dvals[i] if i == j else Fraction(0) for j in range(7)]
           for i in range(7)]
    ok_at, _ = pd_exact(dfr, Fraction(1, 3))
    ok_below, _ = pd_exact(dfr, Fraction(1, 3) - Fraction(1, 2 ** 50))
    cert = cert_floor_exact(dfr, Fraction(0), Fraction(1, 2))
    gap = Fraction(1, 3) - cert
    check("X3 exact-machine sanity (known rational spectrum, min "
          "1/3): PD refused exactly AT 1/3 (%s), accepted just "
          "below (%s), certified floor gap %.3e in (0, 2^-30]"
          % (not ok_at, ok_below, float(gap)),
          (not ok_at) and ok_below and Fraction(0) < gap
          <= Fraction(1, 2 ** 30), kill="K4")
    # exact RB1 sanity AT THE NEW DEPTH K = 5: diagonal measure,
    # q known exactly, Fraction comparison
    momv = [sum(dv ** k for dv in dvals)
            for k in range(2 * KDEEP - 1)]
    q_true = sum(Fraction(1) / dv for dv in dvals)
    cheb = chebyshev_monic(momv, KDEEP)
    val = (radau_exact(cheb[0], cheb[1], Fraction(1, 4), momv[0])
           if cheb else None)
    check("X4 exact RB1 sanity at K = %d: Radau at node 1/4 on the "
          "synthetic diagonal measure gives %.6f >= q = %.6f "
          "(EXACT Fraction comparison)"
          % (KDEEP, float(val) if val is not None else float("nan"),
             float(q_true)),
          val is not None and val >= q_true, kill="K4")
    # THE SIGMA > 1 CONTROL (sharp): coupling scaled so the truth
    # sigma ~ CTRL_SIG_NEAR > 1; the cell must NOT certify sigma < 1
    row = rows[idxs[0]]
    sig0 = row["sigma"]
    scale = math.sqrt(CTRL_SIG_NEAR / sig0)
    mt_near = np.array(row["step"]["Mt"], float)
    mt_near[0, 1:] *= scale
    mt_near[1:, 0] *= scale
    sig_near = (scale ** 2) * row["q_wall"] / row["n_piv"]
    pivn, momn, blkn = exact_wall_data(mt_near, 2 * KDEEP - 2)
    cn = cert_floor_exact(blkn, Fraction(0),
                          Fraction(float(row["lam_b"])))
    chebn = chebyshev_monic(momn, KDEEP)
    vn = (radau_exact(chebn[0], chebn[1], cn, momn[0]) / pivn
          if (chebn and cn is not None) else None)
    check("X5 SIGMA>1 control (sharp): synthetic cell with truth "
          "sigma %.4f > 1 gives certified K = %d bound %.4f > 1 -> "
          "NOT certified (exact Fraction comparison)"
          % (sig_near, KDEEP,
             float(vn) if vn is not None else float("nan")),
          sig_near > 1.0 and vn is not None and vn > SCHUR_BAR,
          kill="K4")
    # the x10 coupling census control (CCLXXVII X5 at the new depth)
    mt2 = np.array(row["step"]["Mt"], float)
    mt2[0, 1:] *= CTRL_COUPLE
    mt2[1:, 0] *= CTRL_COUPLE
    piv2, momv2, blkf2 = exact_wall_data(mt2, 2 * KDEEP - 2)
    c2 = cert_floor_exact(blkf2, Fraction(0),
                          Fraction(float(row["lam_b"])))
    cheb2 = chebyshev_monic(momv2, KDEEP)
    v2 = (radau_exact(cheb2[0], cheb2[1], c2, momv2[0]) / piv2
          if (cheb2 and c2 is not None) else None)
    check("X6 census-can-fire: synthetic coupling x%.0f on cell %d "
          "gives certified K = %d bound %.4f > SIGMA_ENV %.4f AND "
          "> 1 -> census FAILS there"
          % (CTRL_COUPLE, row["index"], KDEEP,
             float(v2) if v2 is not None else float("nan"),
             float(SIGMA_ENV)),
          v2 is not None and v2 > SIGMA_ENV and v2 > SCHUR_BAR,
          kill="K4")


# ============================================ S: the screens
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


def screens(rows):
    section("S -- relocation screens (CCXLVII bars verbatim): are "
            "the NEW margins tau or c_h in disguise?")
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    taus = np.asarray([r["tau_scale"] for r in ok_rows], float)
    ch_map = ch_surface_map(ok_rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in ok_rows], float)
    bnd = np.asarray([r["bound_f"] for r in ok_rows], float)
    series = (("certified best bound", bnd),
              ("1 - bound (the Schur margin)", 1.0 - bnd),
              ("SIGMA_ENV - bound (the registered margin)",
               float(SIGMA_ENV) - bnd))
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
    hs = np.asarray([r["h"] for r in ok_rows], float)
    for label, arr in (("certified best bound", bnd),
                       ("Schur margin", 1.0 - bnd)):
        pos = arr > 0
        if int(np.sum(pos)) >= 3:
            slope, two_se, r2, _a = linfit(np.log(hs[pos]),
                                           np.log(arr[pos]))
            print("    h-law of %s: log-log slope %+.4f +/- %.4f "
                  "(2SE), R^2 %.3f" % (label, slope, two_se, r2))


# =============================================================== main
def finish(rows, n_schur, n_env):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not rows:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        bmax = max((r["bound_f"] for r in ok_rows),
                   default=float("nan"))
        worst1 = min((1.0 - r["bound_f"] for r in ok_rows),
                     default=float("nan"))
        worste = min((float(SIGMA_ENV) - r["bound_f"]
                      for r in ok_rows), default=float("nan"))
        if n_schur == len(rows) and n_env == len(rows):
            v = ("K5-CLOSURE-COMPOSED(%d/%d built wall-legal cells "
                 "certify bound < 1 AND <= SIGMA_ENV %.4f; worst "
                 "bound %.6f, worst Schur margin %.4f, worst "
                 "registered margin %.4f)"
                 % (n_schur, len(rows), float(SIGMA_ENV), bmax,
                    worst1, worste))
        elif n_schur == len(rows):
            miss = [r for r in rows if not r.get("closes_env")]
            v = ("K5-CLOSURE-SCHUR(%d/%d cells certify bound < 1, "
                 "worst Schur margin %.4f; SIGMA_ENV shortfall on "
                 "%d cells: %s)"
                 % (n_schur, len(rows), worst1, len(miss),
                    "; ".join("%s kz %d h %.0f bound %.4f"
                              % (r["seg"], r["kz"], r["h"],
                                 r.get("bound_f", float("nan")))
                              for r in miss[:4])))
        else:
            miss = [r for r in rows if not r.get("closes_schur")]
            v = ("K5-CLOSURE-PARTIAL(certified bound >= 1 on %d/%d "
                 "cells: %s)"
                 % (len(miss), len(rows),
                    "; ".join("%s kz %d h %.0f K %s bound %.4f"
                              % (r["seg"], r["kz"], r["h"],
                                 r.get("k_used"),
                                 r.get("bound_f", float("nan")))
                              for r in miss[:4])))
        print("\n  VERDICT: %s" % v)
        if n_schur == len(rows):
            print("""
  THE COMPOSED CHAIN, UPDATED (CCLXXVII restated with the F0
  completion; premises typed).  For EVERY built wall-legal cell --
  the 68 registered ladder steps, the %d F0 off-ladder cells and
  the CCLXIX F1/F2/F4/F5 sweep cells:
    P1  n = M[0,0] > 0            EXACT-RATIONAL entry theorem
                                  (per cell, this run)
    P2  lambda_min(B) >= c_cell   EXACT-RATIONAL LDL theorem
                                  (round-62 machine, per cell,
                                  this run; c_cell in the table)
    P3  q <= RADAU_K(nu_0..nu_{2K-2}; c_cell), K in {4, 5, 6}
                                  E3 theorem (Golub-Meurant,
                                  EXTERNAL-CITED); its hypothesis
                                  spec(B) in [c_cell, inf) is
                                  DISCHARGED BY P2; the remainder
                                  sign is WARDED per cell per
                                  consumed depth (C5, 0 violations)
    P4  sigma = q/n <= bound      exact rational arithmetic
    =>  sigma <= %.6f (the worst certified bound over ALL cells)
        < 1
    =>  s = (1 - sigma) n > 0
    =>  M is positive definite (E2 Schur, with B > 0 from P2).
  The F0 sigma-max cell (kz 45, h 1359) -- CCLXXVII's ONE open
  cell -- closes at K = 5%s.
  PEDIGREES, honestly typed: SIGMA_ENV = 0.7809 is the CCLXIX
  REGISTERED numeric envelope (consumed at the cited truncation);
  t*_pos = 0.8828 is CCLXV's NUMERIC supremum (reported only); the
  moments and floors are exact dyadic rationals of the ASSEMBLED
  float64 wall matrices (amendment A5: the float64-vs-ideal
  enclosure is the pg_chain interval program's open half).
  THE HONEST OPEN RESIDUE: (i) cells NOT YET BUILT -- the
  surface-registration edge h > 1450, where the concurrent edge
  scan (mission key fdae3b68) is mapping sigma's growth: THE OPEN
  FLANK; (ii) the all-h / class-level form of the chain (the rigor
  lane, mission key d7a7e574).  SCOPE: every wall-legal cell BUILT
  so far; the cofinal claim is NOT included; NO RH claim.""" % (
                sum(1 for r in rows if r["seg"] == "F0"), bmax,
                (" (certified bound %.6f)"
                 % max((r["bound_f"] for r in rows
                        if r["seg"] == "F0" and r["kz"] == 45
                        and r.get("bound_fr") is not None),
                       default=float("nan")))))
        else:
            print("""
  THE PRECISE SHORTFALL: the cells listed in the verdict carry a
  certified bound >= 1 even at the escalation depth K = %d -- for
  each, the certified floor (within 2^-40 of the true lambda_min)
  and the exact moments to nu_%d were consumed; the obstruction is
  the MATRIX, not the certification machinery.""" % (
                KESC, 2 * KESC - 2))
    print("""
  HONEST FRAME.  Finite exact-rational and float64 statements about
  the deployed 68-step ladder artifact and the built CCLXIX
  wall-legal cells (F0/F1/F2/F4/F5); the certified floors and
  bounds are per-cell theorems about the ASSEMBLED float64 wall
  matrices; E3's remainder sign and E5's interval-Cholesky facts
  are external-cited and warded, never proved here.  NEVER an
  all-h statement.  No marker moves; no paper, ledger, website,
  manifest or verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.BFLOOR.K5.01 -- the K = 5 closure of "
            "the certified sigma chain (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))
    print("    bars: Schur < 1 (exact), SIGMA_ENV = %.4f "
          "(registered), depth ladder K = %d -> %d -> %d"
          % (float(SIGMA_ENV), KBASE, KDEEP, KESC))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(CERT_FUNCS, DERIV_BANNED)
    check("S0.2 AC certificate-path functions carry no read, no "
          "eigensolver, no pivot read, no ladder identifier",
          not ac1, ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(FLOAT_FUNCS, DERIV_BANNED)
    check("S0.3 AC float bound-path functions clean (CCLXV ban list "
          "verbatim)", not ac2, ",".join(sorted(set(ac2))),
          kill="K2")

    zones, steps, census, combined = build_ladder()
    if KILLS:
        return finish([], 0, 0)
    artifact_key_ward(steps)
    f0_cells = build_f0(combined)
    if KILLS:
        return finish([], 0, 0)
    families = build_families(census, combined)
    if KILLS:
        return finish([], 0, 0)
    n_sweep = len(f0_cells) + sum(len(v) for v in families.values())
    check("FX2 total wall-legal sweep census %d reproduces "
          "CCLXIX's %d" % (n_sweep, SWEEP_EXP),
          SMOKE or n_sweep == SWEEP_EXP, kill="K3")
    rows = make_rows(steps, f0_cells, families)
    rows = jacobi_identity_wards(rows)
    if KILLS:
        return finish(rows, 0, 0)
    pivot_ward(rows)
    repro_anchors(rows)
    if KILLS:
        return finish(rows, 0, 0)
    k4_repro(rows)
    depth_curve(rows)
    if KILLS:
        return finish(rows, 0, 0)
    required_table_k5(rows)
    n_schur, n_env = certification(rows)
    print_table(rows)
    controls(rows)
    screens(rows)
    return finish(rows, n_schur, n_env)


if __name__ == "__main__":
    sys.exit(main())
