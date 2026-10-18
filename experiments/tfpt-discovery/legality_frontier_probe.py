#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""legality_frontier_probe -- PRIME.ONEBADMODE.LEGALITY.FRONTIER.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

WHERE CAN THE COFINAL LADDER LIVE?  CCLXXXVII found that WALL-LEGALITY
itself fails on part of the deep frontier: of the four frontier census
cells it built (h = 6197, 6247, 6280, 6344 on the TAB2 = 1.6e7
depth-extension table), TWO are NOT wall-legal (h 6197 kz 337 tau =
-5.227e-11 NEGA; h 6247 kz 436 tau = -1.611e-10 NEGA), while their
neighbours h 6280 kz 340 and h 6344 kz 241 are legal.  A legality gap
REMOVES cells from the positivity question (an illegal cell forms no
step and enters no membership statement), but the COFINAL LADDER of
the registered extraction chain must run through LEGAL cells -- the
halfgap registration's deep rungs are exactly such cells.  THIS PROBE
maps the wall-legality frontier: (a) a LEGALITY CENSUS across the deep
frame as far as the frozen budget affords, (b) the COFINAL QUESTION --
does a legal sub-ladder persist per built depth band, (c) the
SIGMA-CHAIN PROFILE on the built legal set, and (d) the NEGA ANATOMY
-- what drives tau < 0 at the frontier.

THE OBJECT.  Per census cell the deployed deep-branch rung builder
(sigma_stress_battery_probe.build_rung_param VERBATIM) assembles the
wall operator A = I - G on the folded negative-arm nodes, where
G = W W^T is the Gram of the first h chain polynomials (orthonormal
w.r.t. the positive-arm measure) under the negative-arm measure,
W = sqrt(v) P.  WALL-LEGALITY is the CCLXXIII/CCLXIX cell_legal
definition VERBATIM: core_ok AND negA = 0 AND lamS > 0 AND tau > 0,
with tau = lambda_min(A), negA = #(eig(A) < 0), lamS = lambda_min of
the 8 x 8 core Schur complement S of A.  STRUCTURAL FACTS stated
before measurement: (i) rank(G) <= min(h, n_neg) and tau =
1 - lambda_max(G): legality is the statement that the
chain-polynomial frame, transported to the negative arm, stays
strictly inside the unit ball; when n_neg > h, A additionally has
>= n_neg - h eigenvalues EXACTLY 1 (warded as W7 with the honest
max(0, .) expectation -- the smoke measured n_neg ~ 0.66 h, so the
unit block is typically EMPTY here); (ii) for A PD with
PD trailing block, lambda_min(S) >= lambda_min(A) = tau (S^{-1} is a
principal submatrix of A^{-1}, fact E8) -- so tau > 0 already implies
lamS > 0 and the legality question is decided by (core_ok, tau, negA).
Both facts are WARDED numerically on every built cell, consumed
nowhere.

 (a) THE LEGALITY CENSUS.  The TAB2 census (587 cells, h 20..65051)
     is enumerated in full; cells are built VERBATIM in a FROZEN
     PRIORITY ORDER behind a cost guard (the h^3 law):
       P1 the two CCLXXXVII NEGA cells (reproduction gate),
       P2 the band neighbours h 6191 / 6280 / 6344 (6280 and 6344
          double as the CCLXXXVII LEGAL reproduction),
       P3 the DEPTH LADDER: the census cells nearest the targets
          (7000, 9000, 8000, 10500, 12500), in the DECLARED knapsack
          order of amendment A2,
       P4 band densification (6155, 6381, 6137, 6426),
       P5 the documented-infeasible tail (15000, 20000, 65051) --
          the guard prints the honest UNBUILT-GUARD line with the
          estimated cost for each.
     Per cell: LEGAL / NEGA / TAU / LAMS / CORE-SHORT / MARGINAL
     (|tau| <= TAU_NOISE, sign not trusted) / UNBUILT-GUARD.  THE
     MAP: legality fraction per frozen depth bin, the tau(h) level
     and sign geometry, the kz/alpha spread of the NEGA set, and the
     drift fit log10|tau| vs log10 h with the extrapolated
     noise-crossing depth (CONJECTURE-GRADE, a fit, never a proof).
 (b) THE COFINAL QUESTION, decided on BUILT cells only (frozen enum
     below): does every built depth bin retain a legal cell, and is
     the deepest built cell legal?  The canonical choice rule, named
     before the run: MAX-TAU-PER-BIN over legal cells (tau is the
     cell's own wall datum -- the same datum class the CCLXXIII
     legality read already consumes; it enters no certificate).
 (c) THE CHAIN PROFILE ON THE LEGAL SET.  Steps on the built legal
     cells (the CCLXIX formations: one bridge per cell from the
     nearest registered anchor STRICTLY below; chain pairs between
     consecutive legal cells within the contiguous band segment
     h in [6100, 6600] -- depth cells get bridges only, the
     CCLXXXVII contiguity lesson).  Per step the FULL certified
     chain: P1 pivot sign (float AND exact), CCLXXVII exact-rational
     floor (round-62 LDL), exact Chebyshev + exact Gauss-Radau at
     K = 4, 5 with RB1 and node wards, interval cross-tier, sigma /
     rho_4 / rho_5, and BOTH bars reported per CCLXXXVII A13: the
     definiteness bar 1 and the registered class bar t_R = 0.7809.
     The known CCLXXXVII t_R breach at the 6280 bridge (rho_5 =
     0.787603) is a REPRODUCTION GATE here, not a new finding.
 (d) THE NEGA ANATOMY.  For every built NEGA cell and one legal
     contrast cell: the bottom of spec(A) (isolated negative mode or
     cluster?), the count of unit eigenvalues (the rank identity),
     negS (does the bad mode survive the core compression -- the
     Haynsworth seat question), and the LOCALIZATION of the bottom
     mode of A (deterministic LU inverse iteration on the assembled
     A -- the bottom mode is separated by |tau| / eva[1]; DIAGNOSTIC
     tier: participation ratio + the folded-node seats + the
     Rayleigh-quotient tie and residual).  Plus the comparison the
     mission asks for: the registered ladder's own tau margins (the
     h = 1219 rung and the ladder minimum) against the frontier
     margins.

EXTERNAL-CITED (facts consumed, warded numerically, never proved).
 E2 Schur / Sylvester: M = [[n, b^T],[b, B]] symmetric is PD iff B PD
    and n - b^T B^{-1} b > 0; a symmetric matrix is PD iff its LDL
    pivots are positive.  [Horn & Johnson, Matrix Analysis, 2nd ed.,
    CUP 2013, Sec. 4.3, 7.2.]
 E3 Gauss-Radau: for symmetric A with spec(A) in [c, inf), the K-node
    Radau rule with node prescribed at c upper-bounds u^T A^{-1} u.
    [Golub & Meurant, PUP 2010, Ch. 6-7.]  Sign WARDED per cell.
 E4 Chebyshev algorithm: monic recurrence coefficients are rational
    in the power moments; exact in exact arithmetic.  [Gautschi,
    Orthogonal Polynomials, OUP 2004, Sec. 2.1.]
 E5 interval Cholesky: outward-rounded completion with positive
    pivots proves PD for every matrix in the interval.  [Rump, Acta
    Numerica 19 (2010).]
 E6 [J^{-1}]_{11} = [T^{-1}]_{11} for a Jacobi matrix and its monic
    form.  [Horn & Johnson op. cit. Sec. 1.3.]
 E8 for A PD partitioned with A_bb PD: lambda_min(S) >=
    lambda_min(A), S the Schur complement of A_bb, because S^{-1} =
    (A^{-1})_cc is a principal submatrix of A^{-1}.  [Horn & Johnson
    op. cit. Sec. 0.7.3, 7.7.]  WARDED on every built PD cell (W8),
    CONSUMED NOWHERE (every legality read uses the full verbatim
    builder).

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seat is the DECLARED scramble control seed.  AC scans (CCLXV /
    CCLXXVII / CCLXXIX ban list verbatim) on the certificate path
    (exact_wall_data / chebyshev_monic / radau_exact / fr_solve /
    pd_exact / cert_floor_exact / chol_iv) and the float bound path
    (wall_moments / lanczos_pair / radau_upper / rho_source).
 W  the registered ladder rebuilt read-only (42 surface rungs -> 68
    steps); NEW READ: the per-rung tau map of the registered deep
    rungs (h 1219..2854) -- the anatomy comparison seat.
 T  TAB2 = 1.6e7 arrays built and warded BITWISE against the
    deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  the deep census (deployed frame formula verbatim), h-sorted;
    gates: 587 cells, h max 65051, and the census CONTAINS the four
    CCLXXXVII frontier keys.
 TIE the anatomy builder (verbatim copy of bat.build_rung_param with
    extra READS of already-computed objects) must tie
    bat.build_rung_param EXACTLY (tau, negA, lamS ==) on the TIE
    cell (nearest h 2012).
 CEN the priority census behind the guard: build item i iff
    elapsed + GUARD_FAC * COST_C * h^3 <= BUILD_CAP_S; else
    UNBUILT-GUARD (censused with the estimate, the list continues --
    cheaper later items may still fit).
 G  gates: G1/G2 the two NEGA cells reproduce (negA >= 1 and tau at
    the CCLXXXVII printed value, rtol NEGA_RTOL); G3 the 6280 / 6344
    cells reproduce LEGAL; G4 the 6280 bridge step reproduces the
    CCLXXXVII breach anatomy (rho_5, truth sigma, certified bound at
    rtol RHO_RTOL); SR the ladder anchors (sigma max 0.604556,
    lambda_min(B) min 0.3496, pivot min 0.082730); W4 the stored
    step-key identity.
 PR the profile: B/I Jacobi + identity wards per step, P1 pivot sign
    float AND exact, the CCLXXVII exact tier (C1..C7 wards), the
    closing census against BOTH bars, the G5 scale-invariance ward.
 AN the anatomy reads per built cell (eva bottom, unit count, negS,
    E8/rank wards) + ARPACK localization (diagnostic, non-kill; RQ
    report bar RQ_TIE).
 X  controls-must-fire: X1 the scramble world (seed SCR_SEED) leaves
    legality or moves the data off the measured envelope; X2 the
    smooth (prime-free) world LEGALITY PROFILE at X2_DEPTHS -- the
    DISCRIMINATION: it must leave legality (or land outside the
    envelope) at EVERY tested depth; X3 a synthetic near-1 cell must
    NOT certify bound < 1; X4 an inflated floor claim must be
    refused by BOTH tiers.
 S  screens: tau relocation screens (CCXLVII bars verbatim: PASS <=
    0.30, RELOC >= 0.70) on the profile levels and margins; the
    CCXVII c_h screen where the surface window is legitimate (deep
    cells are OUT-OF-SURFACE and the screen is then typed VACUOUS,
    CCLXXXVII verbatim).

COFINAL RULE (frozen BEFORE the run).  DBINS = ((6100, 6320),
(6320, 6600), (6600, 7300), (7300, 8300), (8300, 9500), (9500,
11000), (11000, 13000), (13000, 17000), (17000, 70000)).  A built
cell is LEGAL only if cell_legal says OK and |tau| > TAU_NOISE
(MARGINAL cells are censused separately and count as NOT legal).
Over the built-nonempty bins:
 LEGFRONT-COFINAL-MEASURED(h*)   iff every built-nonempty bin has
   >= 1 legal cell AND the deepest built cell is legal.
 LEGFRONT-COFINAL-GAPPED(gaps)   iff the deepest built-nonempty bin
   has a legal cell but >= 1 shallower built bin has none.
 LEGFRONT-TERMINATES-MEASURED(h_last_legal) iff the deepest
   built-nonempty bin has NO legal cell AND (the next-deepest built
   bin also has none, OR the deepest bin has >= 2 built cells).
 LEGFRONT-FRONTIER-AMBIGUOUS     otherwise (a single illegal
   deepest sample decides nothing).
The four cases are exhaustive and disjoint; the horizon is ALWAYS
reported: every statement is about BUILT cells, never all-h.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum): the COFINAL RULE case, plus typed tags
LEGALITY-MAP(bin fractions, NEGA geometry), CHAIN-PROFILE(closing
census at bar 1; t_R census with the cited known breach),
NEGA-ANATOMY(margin scale, seat, localization), MARGINAL(count),
CONTROLS, SCREENS, AMENDMENTS.  Every enum is a finite
float64/exact-rational statement about BUILT cells of the deployed
construction plus explicitly CONJECTURE-GRADE fits; NEVER an all-h
statement, NEVER an RH claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; IDENT_TIE =
1e-12; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7; SIGMA_MAX_REF =
0.604556 (rtol 2e-3); LAMB_MIN_REF = 0.3496, PIV_MIN_REF = 0.082730
(rtol 5e-2); KBASE = 4; KDEEP = 5; KMOM = 8; SCHUR_BAR = 1 (exact);
T_R = 7809/10000; BIS_ITERS = 40; RADAU_SIGN_TIE = 1e-12; XR_TIE =
1e-6; COEF_TIE = 1e-6; CERT_GAP_RTOL = 1e-6; NODE_TIE = 1e-9;
SCALE_SET = (1e-3, 1, 1e3), SCALE_TIE = 1e-9; TAB2 = 1.6e7; KZ2_MAX
= 1200; LOC_ITERS = 30; CENSUS_N_REF = 587; CENSUS_HMAX_REF = 65051;
NEGA_REF =
((6197, 337, -5.227e-11), (6247, 436, -1.611e-10)), NEGA_RTOL =
2e-3; LEG_REF = ((6280, 340), (6344, 241)); RHO_REF = (6280, 340,
rho5 0.787603, sigma 0.751875, bound 0.787603), RHO_RTOL = 1e-4;
TAU_NOISE = 5e-12 (from the disclosed recon cross-route, max
|d tau| = 2.7e-13, headroom ~20x); UNIT_TIE = 1e-9; RQ_TIE = 1e-10;
BAND_KEYS = ((6197, 337), (6247, 436), (6191, 178), (6280, 340),
(6344, 241)); DEPTH_TGT = (7000, 9000, 8000, 10500, 12500);
DENS_KEYS = ((6155, 335), (6381, 397), (6137, 233), (6426, 182));
TAIL_TGT = (15000, 20000, 65051); BAND_SEG = (6100, 6600); DBINS
above; COST_C = 4.2e-10 s (machine calibration, DISCLOSED below);
GUARD_FAC = 1.15; BUILD_CAP_S = 1320; runtime cap 25 min; SCR_SEED =
1; CTRL_INFLATE = 1.01; CTRL_SIG_NEAR = 1.2; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; X2_DEPTHS = (1300, 2400, 3300); CH_N = 4;
CH_HMAX = 2900; DEGEN_BAR = 1e-12; LOC_CONTRAST = (6280, 340).
Smoke: ladder 10 contiguous surface rungs + 3 lowest
deep; PRIO = (TIE cell h ~2012, the census cell nearest 2200);
census gates, G1-G4 and SR / W4 counts SMOKE-SKIPPED (typed, the
CCLXI / CCLXIX / CCLXXVII identical smoke phenomenon -- subset
values printed); X2_DEPTHS = (600,); bins vacuous, verdict typed
SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 PRE-FREEZE RECONNAISSANCE, fully disclosed (two throwaway
    scripts, deleted; no bar, rule, control or enum was chosen in
    response to a FRONTIER measurement -- no cell with h > 5200 was
    read in the recon):
    (i) the CENSUS SHAPE: 587 cells, h 20..65051; band (5500, 8000]
        holds 71 cells at ~8200 s full-build cost -- an exhaustive
        band census does NOT fit the 25-min cap; the priority design
        is the corrected plan.
    (ii) the COST LAW re-measured on this machine: 2.3 s at h 2012,
        10.8 s at h 3113, 52.9 s at h 5167 (COST_C 2.8e-10 ..
        4.5e-10 under load); frozen envelope COST_C = 4.2e-10,
        GUARD_FAC = 1.15.  The ladder rebuild costs ~101 s.
    (iii) the FAST-TIER FINDING: a mathematically identical legality
        read from the h x h Gram W^T W (the nonzero spectrum of G)
        was implemented and gave NO speedup -- the h^3 cost is the
        reorthogonalized Lanczos chain itself (55 of 62 s at
        h 5167), not the eigensolve.  The fast tier is ABANDONED;
        every census read below uses the verbatim builder.  Its one
        deliverable is the cross-route noise calibration max |d tau|
        = 2.7e-13 over three cells, from which TAU_NOISE = 5e-12.
    (iv) tau magnitudes seen at the three calibration cells (3.3e-9,
        4.4e-9, 5.6e-10 at h 2012 / 3113 / 5167) and the ladder
        rungs' tau range (min 8.3e-10 at h 2704) -- DISCLOSED
        because they motivate the MARGINAL type and the anatomy
        comparison; they enter no gate and no enum.
 A2 THE KNAPSACK ORDER of the depth targets (7000, 9000, 8000) is
    deliberately non-monotone: under the frozen cost law the
    ascending order (7000, 8000, 9000) spends the budget before the
    9000 cell (cum. guard 984 + 352 > 1320), while the declared
    order fits all three (cum. 1290 <= 1320).  Pure arithmetic on
    the frozen constants, fixed before the run; the guard still
    decides honestly at run time.
 A3 the cofinal verdict is decided on BUILT cells only, and MARGINAL
    cells (|tau| <= TAU_NOISE) count as NOT legal for the enum while
    being censused separately -- the sign of a 1e-12 eigenvalue of a
    float64 build is not evidence.  Declared before any frontier
    cell was read.
 A4 the profile's t_R comparison will re-encounter the KNOWN
    CCLXXXVII breach at the 6280 bridge (rho_5 = 0.787603 > t_R);
    it is consumed here as reproduction gate G4 and reported per
    CCLXXXVII A13 with BOTH bars explicit.  It is NOT a new finding
    and does NOT decide the legality verdict.
 A5 the certificate object is the ASSEMBLED float64 wall matrix
    (CCLXXVII A3 / CCLXXIX A5 / CCLXXXVII A5 verbatim): the
    float64-vs-ideal enclosure stays with the pg_chain interval
    program and is NOT retried here.  In particular the MARGINAL
    type is exactly the honest acknowledgement of that scope edge at
    the tau = 0 boundary.
 A6 the smooth and arch worlds are expected to leave wall-legality
    outright (CCLXXXVII A6).  X2 therefore reports the legality
    verdict as the primary discrimination and the |tau_1|-normalized
    entry data of the refused step as a DECLARED DIAGNOSTIC only.
 A7 the localization is a DIAGNOSTIC tier: deterministic start
    vector, LU inverse iteration on the assembled A (LOC_ITERS
    iterations), non-kill; its Rayleigh-quotient tie to the verbatim
    tau is REPORTED against RQ_TIE together with the residual, and a
    failure types the read LOCALIZATION-REFUSED, never a kill (the
    legality verdicts consume only the verbatim eigvalsh route).
    The first smoke ran an ARPACK top-of-G tier instead and it
    REFUSED on the TIE cell (no convergence at the clustered top
    spectrum within the iteration cap); the swap to inverse
    iteration was made pre-freeze and touches no verdict path.
 A8 the depth ladder reaches h ~9000 at best under the 25-min cap;
    h = 65051 (the table limit) costs ~1.3e5 s (~36 h) per cell and
    is DOCUMENTED-INFEASIBLE here: the guard prints its honest
    UNBUILT line.  Statements about depths beyond the built horizon
    are typed as such and never implied.

SMOKE DISCLOSURE (2026-08-12), pre-freeze, verbatim.
 SMOKE-1 (SPEC_SHA d7d80fb5, 48/48 PASS, 21.6 s): every check green;
   TWO design defects surfaced by INSPECTION of the output, both
   repaired pre-freeze, no bar / census rule / enum touched:
   (i) the unit-eigenvalue expectation was written for n_neg > h,
   but the folded negative arm carries n_neg ~ 0.66 h nodes (the
   smoke printed "unit 0/-686") -- structural fact (i) and ward W7
   now carry the honest max(0, .) form (W7 passed vacuously and
   stays near-vacuous); (ii) the ARPACK top-of-G localization
   REFUSED silently on the TIE cell (no convergence at the clustered
   top spectrum within the cap, and the refusal was not printed) --
   replaced by deterministic LU inverse iteration on the assembled A
   per amendment A7, refusals now printed.  Localization is
   diagnostic-only; no verdict path touched.
 SMOKE-2 (SPEC_SHA 75926f00, 48/48 PASS, 12.9 s): TIE ward EXACT
   (tau, negA, lamS ==); localization rq_gap 1.9e-17, residual
   8.1e-18, IPR 1.6; census 2/2 LEGAL (tau 3.3e-9 / 1.1e-8); profile
   3 steps, certified bounds < 1 and <= t_R (worst m_1 0.8473);
   controls all fired (scramble tau -7.8e+89 NEGA, smooth tau -812.1
   NEGA at h 606, near-1 bound 1.3896 >= 1 refused, inflated floor
   refused by BOTH tiers 2/2); screens 2 PASS / 4 AMBIG on n = 3
   rows (small-sample, typed) / S2 VACUOUS typed.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCXCIX line prepended to experiments/next.txt AFTER the frozen
summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder + rung
builder), zolotarev_phase_filter_probe (CCXXV step assembly),
sigma_stress_battery_probe (CCLXIX parametric rung builder, imported
READ-ONLY -- the census builder of record), sigma_edge_growth_probe
(CCLXXIII cell_legal, reproduced verbatim),
bfloor_perstep_certification_probe (CCLXXVII exact machine,
reproduced verbatim), bfloor_k5_closure_probe (CCLXXIX K = 5 tier),
deep_membership_limit_probe (CCLXXXVII deep census machinery and the
frontier finding under reproduction), halfgap_registration_probe
(the registered-ladder cofinality language, cited),
euler_phase_identity_probe (CCXVII c_h), v563_paper2_readouts
(deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/legality_frontier_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/legality_frontier_probe.py
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
IDENT_TIE = 1.0e-12
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
SIGMA_MAX_REF = 0.604556
SIGMA_RTOL = 2.0e-3
LAMB_MIN_REF = 0.3496
PIV_MIN_REF = 0.082730
REPRO_RTOL = 5.0e-2
KBASE = 4
KDEEP = 5
KMOM = 8
SCHUR_BAR = Fraction(1)
T_R = Fraction(7809, 10000)
T_R_F = float(T_R)
BIS_ITERS = 40
RADAU_SIGN_TIE = 1.0e-12
XR_TIE = 1.0e-6
COEF_TIE = 1.0e-6
CERT_GAP_RTOL = 1.0e-6
NODE_TIE = 1.0e-9
SCALE_SET = (1.0e-3, 1.0, 1.0e3)
SCALE_TIE = 1.0e-9
TAB2 = 16_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
NEGA_REF = ((6197, 337, -5.227e-11), (6247, 436, -1.611e-10))
NEGA_RTOL = 2.0e-3
LEG_REF = ((6280, 340), (6344, 241))
RHO_REF = dict(h=6280, kz=340, rho5=0.787603, sigma=0.751875,
               bound=0.787603)
RHO_RTOL = 1.0e-4
TAU_NOISE = 5.0e-12
UNIT_TIE = 1.0e-9
RQ_TIE = 1.0e-10
BAND_KEYS = ((6197, 337), (6247, 436), (6191, 178), (6280, 340),
             (6344, 241))
DEPTH_TGT = (7000, 9000, 8000, 10500, 12500)
DENS_KEYS = ((6155, 335), (6381, 397), (6137, 233), (6426, 182))
TAIL_TGT = (15000, 20000, 65051)
BAND_SEG = (6100, 6600)
DBINS = ((6100, 6320), (6320, 6600), (6600, 7300), (7300, 8300),
         (8300, 9500), (9500, 11000), (11000, 13000), (13000, 17000),
         (17000, 70000))
COST_C = 4.2e-10
GUARD_FAC = 1.15
BUILD_CAP_S = 1320.0
SCR_SEED = 1
CTRL_INFLATE = 1.01
CTRL_SIG_NEAR = 1.2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
X2_DEPTHS = (1300, 2400, 3300)
CH_N = 4
CH_HMAX = 2900
DEGEN_BAR = 1.0e-12
LOC_ITERS = 30
LOC_CONTRAST = (6280, 340)
TIE_TGT = 2012
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
DERIV_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h", "gap", "lamB1", "sigma", "sigma_quotient",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "theta", "row", "rows", "step", "steps")
CERT_FUNCS = ("exact_wall_data", "chebyshev_monic", "radau_exact",
              "fr_solve", "pd_exact", "cert_floor_exact", "chol_iv")
FLOAT_FUNCS = ("wall_moments", "lanczos_pair", "radau_upper",
               "rho_source")

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
    machinery reproduced verbatim.  Returns (a, b) or None."""
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
    return a, b


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


def rho_source(matrix, floor_c, kdeg):
    """THE SOURCE-ONLY RATIO rho_K = RADAU_K(nu; floor_c) / n from the
    wall ENTRIES and the floor (CCLXV verbatim, scale-invariant)."""
    piv = float(np.asarray(matrix, float)[0, 0])
    lan = lanczos_pair(matrix, kdeg)
    if lan is None or piv <= 0.0:
        return float("nan"), None
    alp, bet, mass = lan
    val, jac = radau_upper(alp, bet, floor_c, mass)
    if not math.isfinite(val):
        return float("nan"), None
    return val / piv, jac


# ============ the exact-rational tier (round 62 + E4, AC-scanned)
def exact_wall_data(matrix, kdeg):
    """Pivot n, b-weighted moments nu_0..nu_kdeg and the co-block, ALL
    as exact Fractions of the dyadic float64 ENTRIES (CCVII v897
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
    """E4 Chebyshev algorithm, EXACT and depth-generic (CCLXXVII
    verbatim).  None on degeneracy."""
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
    """Exact Gaussian elimination with nonzero pivoting on Fractions;
    returns the solution list or None if singular."""
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
    """EXACT-RATIONAL Gauss-Radau upper-bound value at depth
    K = len(al)+1 with the node prescribed at flo (CCLXXVII
    verbatim, monic form E6)."""
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
    """Exact Sylvester/LDL decision (round 62 verbatim)."""
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
    verbatim: dyadic bisection, NEVER rounded inward)."""
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
    """Directed-rounding float64 interval Cholesky of (blk - shift I)
    (E5, refuse-only; CCLXXVII verbatim)."""
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
    section("W -- the registered CCVII/CCXXV ladder, rebuilt "
            "read-only (anchors + the rung tau map)")
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
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"]))
              for r in artifact["rungs"]}
    ours = {(int(st["r1"]["h"]), int(st["r1"]["kz"]),
             int(st["r2"]["h"]), int(st["r2"]["kz"]))
            for st in steps}
    n_match = len(stored & ours)
    check("W4 ladder identity: %d/%d step keys match the stored "
          "CCXLVII artifact" % (n_match, len(ours)),
          SMOKE or (n_match == STEPS_EXP and len(ours) == STEPS_EXP),
          kill="K2")
    # ---- the rung tau map (anatomy comparison seat)
    dtau = sorted((r["tau"], r["h"], r["kz"]) for r in deep_ok)
    print("    LADDER TAU MAP (registered deep rungs, %d): min-3 "
          "and the h = 1219 rung:" % len(dtau))
    for tv, hv, kv in dtau[:3]:
        print("      tau %.4e  h %-5d kz %d" % (tv, hv, kv))
    r1219 = [t for t in dtau if t[1] == 1219]
    for tv, hv, kv in r1219:
        print("      tau %.4e  h %-5d kz %d  (the mission's "
              "comparison rung)" % (tv, hv, kv))
    lad_tau = dict(min=dtau[0] if dtau else None,
                   r1219=r1219[0] if r1219 else None, all=dtau)
    return steps, combined, lad_tau


# ============================================ TAB2 + the deep census
DEEP = {}


def build_tab2():
    section("T -- the CCLXIX depth-extension table TAB2 = %.3g, "
            "warded BITWISE against the deployed 4e6 prefix" % TAB2)
    lam2 = core.von_mangoldt_table(TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    g2 = np.diff(u2)
    n_pref = len(ob.EXT["NN"])
    check("T1 TAB2 prefix ward: the 1.6e7 arrays agree BITWISE with "
          "the deployed 4e6 EXT arrays (%d atoms of %d)"
          % (n_pref, len(nn2)),
          (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
           and np.array_equal(u2[:n_pref], ob.EXT["U"])
           and np.array_equal(mu2[:n_pref], ob.EXT["MU"])),
          kill="K2")
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = g2
    return u2, mu2, g2


def deep_census():
    section("D -- THE DEEP-FRAME CENSUS on TAB2 (deployed formula "
            "verbatim), h-sorted")
    u2, _mu2, g2 = DEEP["U"], DEEP["MU"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        hz = mz // 2
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=hz, kz=kz, alpha=alpha, M=mz, X=x_val))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    print("    census %d cells, h %d .. %d; frozen cost law "
          "%.3e * h^3 s" % (len(out), int(hs.min()), int(hs.max()),
                            COST_C))
    keys = {(c["h"], c["kz"]) for c in out}
    ok_keys = all(k in keys for k in BAND_KEYS)
    if SMOKE:
        check("D1 census gates SMOKE-TYPED (full census %d cells, "
              "h max %d, frontier keys %s)"
              % (len(out), int(hs.max()),
                 "present" if ok_keys else "MISSING"), True)
    else:
        check("D1 census reproduces CCLXXXVII: %d == %d cells, "
              "h max %d == %d, all four frontier keys present (%s)"
              % (len(out), CENSUS_N_REF, int(hs.max()),
                 CENSUS_HMAX_REF, ok_keys),
              len(out) == CENSUS_N_REF
              and int(hs.max()) == CENSUS_HMAX_REF and ok_keys,
              kill="K3")
    return out


def cell_legal(rung):
    """CCLXXIII/CCLXIX wall-legality of a single cell, VERBATIM."""
    if rung is None:
        return False, "NONE"
    if "fail" in rung:
        return False, rung["fail"]
    if not rung.get("core_ok"):
        return False, "CORE-SHORT"
    if rung["negA"] > 0:
        return False, "NEGA"
    if rung.get("lamS", -1.0) <= 0.0:
        return False, "LAMS"
    if rung["tau"] <= 0.0:
        return False, "TAU"
    return True, "OK"


_CELL_CACHE = {}


def build_cell(cell, world=None, scr_seed=None):
    """The deployed deep-branch rung builder (bat.build_rung_param
    VERBATIM) with the CCLXXXVII world handling; cached by the full
    frame identity."""
    key = (int(cell["kz"]), int(cell["M"]), world, scr_seed)
    if key in _CELL_CACHE:
        return _CELL_CACHE[key]
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "arch":
        mm = np.zeros_like(mm)
    elif world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    rung = bat.build_rung_param(cell["kz"], alpha, mfold, uu, mm)
    rung["X"] = cell["X"]
    rung["alpha_c"] = float(alpha)
    _CELL_CACHE[key] = rung
    return rung


def build_cell_anatomy(cell, localize=False):
    """bat.build_rung_param VERBATIM (same sub-calls, same order,
    Schur part inline) plus EXTRA READS of the already-computed
    objects: the bottom of spec(A), the unit-eigenvalue count (rank
    identity), and -- if localize or negA >= 1 -- the deterministic
    ARPACK localization of the extremal mode of G = W W^T
    (DIAGNOSTIC tier, amendment A7)."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka]
    mm = mu2[:ka]
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _uf_p, _fdp = ob.folded_measure_full(dens, lfold, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(dens, lfold, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1 or np.any(be <= 0):
        return dict(kind="param", kz=cell["kz"], h=half,
                    fail="CHAIN")
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = sym(gram)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    eva = np.linalg.eigvalsh(amat)
    out = dict(kind="param", kz=cell["kz"], h=half, n=n,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               tau=float(eva[0]), negA=int(np.sum(eva < 0.0)))
    out["X"] = cell["X"]
    out["alpha_c"] = float(alpha)
    # ---- anatomy extras (reads only; nothing above changed)
    out["eva_bot"] = [float(v) for v in eva[:5]]
    out["n_unit"] = int(np.sum(np.abs(eva - 1.0) <= UNIT_TIE))
    out["n_neg_nodes"] = int(n)
    out["rank_g"] = int(half)
    if localize or out["negA"] >= 1:
        try:
            lu, piv = sla.lu_factor(amat)
            vloc = np.full(n, 1.0 / math.sqrt(n))
            for _ in range(LOC_ITERS):
                vloc = sla.lu_solve((lu, piv), vloc)
                vloc = vloc / float(np.linalg.norm(vloc))
            rq = float(vloc @ (amat @ vloc))
            res = float(np.linalg.norm(amat @ vloc - rq * vloc))
            p4 = float(np.sum(vloc ** 4))
            top3 = np.argsort(-np.abs(vloc))[:3]
            out["loc"] = dict(
                rq=rq, rq_gap=abs(rq - out["tau"]), res=res,
                ipr=1.0 / p4 if p4 > 0 else float("nan"),
                seats=[(int(uf_n[j]), float(ys[j]),
                        float(abs(vloc[j]))) for j in top3])
            del lu
        except Exception as exc:                   # noqa: BLE001
            out["loc"] = dict(refused=type(exc).__name__)
    del pn, gram
    # ---- the Schur part, bat.build_rung_param VERBATIM
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in ob.CORE_J)
    if not out["core_ok"]:
        out["fail"] = "CORE-SHORT"
        return out
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset], dtype=int)
    bblk = amat[np.ix_(ic, ic)]
    xc = amat[np.ix_(ic, ib)]
    rblk = amat[np.ix_(ib, ib)]
    try:
        zsol = np.linalg.solve(rblk, xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        out["fail"] = "R-SINGULAR"
        return out
    smat = sym(bblk - xc @ zsol)
    evs = np.linalg.eigvalsh(smat)
    out["S"] = smat
    out["lamS"] = float(evs[0])
    out["negS"] = int(np.sum(evs < 0.0))
    return out


# ================================ the priority census (the frontier)
def build_prio(census):
    """The frozen priority list (docstring order)."""
    by_key = {(c["h"], c["kz"]): c for c in census}
    hs = np.asarray([c["h"] for c in census], float)
    tie_cell = census[int(np.argmin(np.abs(hs - TIE_TGT)))]
    if SMOKE:
        c2200 = census[int(np.argmin(np.abs(hs - 2200)))]
        return tie_cell, [("SMOKE-A", tie_cell),
                          ("SMOKE-B", c2200)]
    prio = []
    used = set()

    def add(tag, cell):
        key = (cell["h"], cell["kz"])
        if key in used:
            return
        used.add(key)
        prio.append((tag, cell))

    for (hv, kv), tag in zip(BAND_KEYS,
                             ("P1-NEGA", "P1-NEGA", "P2-BAND",
                              "P2-BAND", "P2-BAND")):
        add(tag, by_key[(hv, kv)])
    for tgt in DEPTH_TGT:
        idx = int(np.argmin(np.abs(hs - tgt)))
        add("P3-DEPTH(%d)" % tgt, census[idx])
    for hv, kv in DENS_KEYS:
        add("P4-DENS", by_key[(hv, kv)])
    for tgt in TAIL_TGT:
        idx = int(np.argmin(np.abs(hs - tgt)))
        add("P5-TAIL(%d)" % tgt, census[idx])
    return tie_cell, prio


def census_build(census):
    section("CEN -- THE LEGALITY CENSUS (verbatim builds in the "
            "frozen priority order, guard %.2f * %.2e * h^3 <= "
            "%.0f s)" % (GUARD_FAC, COST_C, BUILD_CAP_S))
    tie_cell, prio = build_prio(census)
    # ---- TIE ward: anatomy builder == bat builder, exactly
    r_bat = build_cell(tie_cell)
    r_ana = build_cell_anatomy(tie_cell, localize=True)
    check("TIE anatomy builder ties bat.build_rung_param EXACTLY on "
          "h %d kz %d (tau %s negA %s lamS %s)"
          % (tie_cell["h"], tie_cell["kz"],
             "==" if r_ana["tau"] == r_bat["tau"] else "DIFF",
             "==" if r_ana["negA"] == r_bat["negA"] else "DIFF",
             "==" if r_ana.get("lamS") == r_bat.get("lamS")
             else "DIFF"),
          (r_ana["tau"] == r_bat["tau"]
           and r_ana["negA"] == r_bat["negA"]
           and r_ana.get("lamS") == r_bat.get("lamS")), kill="K2")
    loc = r_ana.get("loc", {})
    if "rq_gap" in loc:
        print("    TIE localization: rq %.6e rq_gap %.2e res %.2e "
              "ipr %.1f" % (loc["rq"], loc["rq_gap"], loc["res"],
                            loc["ipr"]))
    elif "refused" in loc:
        print("    TIE localization: LOCALIZATION-REFUSED (%s)"
              % loc["refused"])
    reads = []
    for tag, cell in prio:
        est = GUARD_FAC * COST_C * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-14s h %-6d kz %-4d UNBUILT-GUARD (est "
                  "%.0f s, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            reads.append(dict(tag=tag, cell=cell, verdict="UNBUILT",
                              why="UNBUILT-GUARD", rung=None))
            continue
        tc = time.time()
        want_loc = (cell["h"], cell["kz"]) == LOC_CONTRAST
        rung = build_cell_anatomy(cell, localize=want_loc)
        ok, why = cell_legal(rung)
        marginal = ("tau" in rung
                    and abs(rung["tau"]) <= TAU_NOISE)
        verdict = ("MARGINAL" if marginal
                   else "LEGAL" if ok else why)
        reads.append(dict(tag=tag, cell=cell, verdict=verdict,
                          why=why, rung=rung, marginal=marginal))
        tau_s = ("%.4g" % rung["tau"]) if "tau" in rung else "-"
        print("    %-14s h %-6d kz %-4d alpha %.4f  %-9s tau %-12s "
              "negA %s negS %s unit %s/%s  %.1f s"
              % (tag, cell["h"], cell["kz"], cell["alpha"], verdict,
                 tau_s, rung.get("negA", "-"), rung.get("negS", "-"),
                 rung.get("n_unit", "-"),
                 max(0, rung.get("n_neg_nodes", 0)
                     - rung.get("rank_g", 0)),
                 time.time() - tc), flush=True)
        lc = rung.get("loc", {})
        if "rq_gap" in lc:
            print("      loc: rq %.6e rq_gap %.2e res %.2e ipr %.1f "
                  "seats %s"
                  % (lc["rq"], lc["rq_gap"], lc["res"], lc["ipr"],
                     [(s[0], "%.4f" % s[1], "%.3f" % s[2])
                      for s in lc["seats"]]), flush=True)
        elif "refused" in lc:
            print("      loc: LOCALIZATION-REFUSED (%s)"
                  % lc["refused"])
    n_built = sum(1 for r in reads if r["rung"] is not None)
    check("CEN1 the census built %d cells (%d unbuilt-guard, "
          "honestly censused)"
          % (n_built, len(reads) - n_built),
          n_built >= (2 if SMOKE else 6), kill="K1")
    return reads


def census_gates(reads):
    section("G -- reproduction gates against CCLXXXVII")
    if SMOKE:
        check("G1-G4 CCLXXXVII frontier reproduction SMOKE-SKIPPED "
              "(typed; the frontier cells are not built in smoke)",
              True)
        return
    got = {(r["cell"]["h"], r["cell"]["kz"]): r for r in reads
           if r["rung"] is not None}
    for hv, kv, tref in NEGA_REF:
        r = got.get((hv, kv))
        if r is None:
            check("G1/G2 NEGA cell h %d kz %d NOT BUILT" % (hv, kv),
                  False, kill="K3")
            continue
        tau = r["rung"].get("tau", float("nan"))
        ok = (r["rung"].get("negA", 0) >= 1
              and math.isfinite(tau)
              and abs(tau / tref - 1.0) <= NEGA_RTOL)
        check("G1/G2 NEGA repro h %d kz %d: tau %.4g vs CCLXXXVII "
              "%.4g (rtol %.0e), negA %d >= 1"
              % (hv, kv, tau, tref, NEGA_RTOL,
                 r["rung"].get("negA", 0)), ok, kill="K3")
    for hv, kv in LEG_REF:
        r = got.get((hv, kv))
        ok = r is not None and r["verdict"] == "LEGAL"
        check("G3 LEGAL repro h %d kz %d: %s"
              % (hv, kv, r["verdict"] if r else "NOT BUILT"),
              ok, kill="K3")


# =========================== the profile steps on the built legal set
def profile_steps(reads, anchors):
    """CCLXIX formations on the built legal cells: one bridge per
    cell from the nearest registered anchor STRICTLY below; chain
    pairs between consecutive legal cells inside the contiguous band
    segment BAND_SEG (depth cells: bridges only -- the CCLXXXVII
    contiguity lesson A2)."""
    legal = [r["rung"] for r in reads
             if r["rung"] is not None and r["verdict"] == "LEGAL"]
    legal.sort(key=lambda r: (r["h"], r["kz"]))
    anc = sorted(anchors, key=lambda r: r["h"])
    pairs = []
    band = [r for r in legal
            if BAND_SEG[0] <= r["h"] <= BAND_SEG[1]]
    if SMOKE:
        band = legal
    pairs += [(r1, r2, "chain") for r1, r2 in zip(band, band[1:])]
    for r2 in legal:
        below = [a for a in anc
                 if a["h"] <= r2["h"]
                 and not (int(a["kz"]) == int(r2["kz"])
                          and int(a["h"]) == int(r2["h"]))]
        if not below:
            continue
        pairs.append((below[-1], r2, "bridge"))
    rows = []
    for r1, r2, kind in pairs:
        sts = ob.make_steps([r1, r2])
        if not sts:
            continue
        st = sts[0]
        zol.assemble_step(st)
        if st["status"] != "OK":
            continue
        mt = np.asarray(st["Mt"], float)
        piv = float(mt[0, 0])
        vec = mt[1:, 0]
        if piv <= 0.0 or float(vec @ vec) / piv ** 2 < DEGEN_BAR:
            continue
        rows.append(dict(step=st, mode=kind,
                         h=float(r2["h"]), kz=int(r2["kz"]),
                         alpha=float(r2["alpha"]),
                         X=float(r2.get("X", float("nan"))),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         c_meas=float(st["lamB1"])))
    for i, r in enumerate(rows):
        r["index"] = i
    print("    profile formations: %d steps (%d chain, %d bridge) "
          "on %d built legal cells"
          % (len(rows), sum(1 for r in rows if r["mode"] == "chain"),
             sum(1 for r in rows if r["mode"] == "bridge"),
             len(legal)))
    return rows


def jacobi_identity_wards(rows, label):
    section("B/I -- Jacobi translation + the CCLXV identity wards on "
            "every %s step" % label)
    d_b1 = d_a1 = d_bfl = d_m0 = d_q = d_sig = d_gap = 0.0
    n_bad = 0
    for row in rows:
        st = row["step"]
        jf = jacobi_form(st["Mt"])
        if jf is None:
            n_bad += 1
            row["theta"] = None
            continue
        a, b = jf
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
    check("B1 Lanczos form of (M, e_0) exists on all %d %s steps"
          % (len(rows), label), n_bad == 0,
          "breakdowns %d" % n_bad, kill="K2")
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
    keep = [r for r in rows if r["theta"] is not None]
    pivs = [r["n_piv"] for r in keep]
    n_pos = sum(1 for r in keep if r["n_piv"] > 0.0)
    n_pos_x = sum(1 for r in keep
                  if Fraction(float(r["step"]["Mt"][0, 0])) > 0)
    check("P1 PIVOT SIGN n = M[0,0] > 0 on all %d %s steps (float "
          "AND exact rational): %d / %d positive, min %.6f"
          % (len(keep), label, n_pos, n_pos_x,
             min(pivs) if pivs else float("nan")),
          n_pos == len(keep) and n_pos_x == len(keep), kill="K2")
    return keep


def repro_anchors(lad_rows):
    section("SR -- repro anchors against CCLXV / CCLXIX")
    sig_max = max(r["sigma"] for r in lad_rows)
    lam_min = min(r["c_meas"] for r in lad_rows)
    piv_min = min(r["n_piv"] for r in lad_rows)
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


def entry_data(rows):
    """Entry data + the CCLXXVII exact-rational certification per
    step (CCLXXXVII entry_data reproduced, minus the limit-object
    machinery)."""
    section("E/C -- entry data + exact-rational certification at "
            "K = %d, %d on the legal-set profile" % (KBASE, KDEEP))
    d_coef = d_xr = d_gapc = 0.0
    sign_fail = node_fail = n_ref = n_deg = n_exceed = 0
    iv_conf = iv_ref = 0
    for row in rows:
        mat = row["step"]["Mt"]
        piv = float(mat[0, 0])
        mom = wall_moments(mat, KMOM)
        pivf, momv, blkf = exact_wall_data(mat, 2 * KDEEP - 2)
        hi_hint = Fraction(float(row["c_meas"])) * (
            Fraction(1) + Fraction(1, 10 ** 6))
        c_cert = cert_floor_exact(blkf, Fraction(0), hi_hint)
        if c_cert is None:
            n_ref += 1
            row["c_cert"] = None
            row["bound_fr"] = None
            continue
        row["c_cert"] = c_cert
        c_f = float(c_cert)
        row["c_cert_f"] = c_f
        if c_f > row["c_meas"] * (1.0 + 1e-9):
            n_exceed += 1
        d_gapc = max(d_gapc, (row["c_meas"] - c_f)
                     / max(1.0, row["c_meas"]))
        lan = lanczos_pair(mat, KDEEP)
        cheb5 = chebyshev_monic(momv, KDEEP)
        if lan is not None and cheb5 is not None:
            alp, bet, _mass = lan
            for k in range(KDEEP - 1):
                d_coef = max(d_coef, abs(float(cheb5[0][k]) - alp[k])
                             / max(1.0, abs(alp[k])))
                d_coef = max(d_coef, abs(float(cheb5[1][k])
                                         - bet[k] ** 2)
                             / max(1.0, bet[k] ** 2))
        vals = {}
        for kd in (KBASE, KDEEP):
            cheb = chebyshev_monic(momv, kd)
            if cheb is None:
                n_deg += 1
                continue
            val_fr = radau_exact(cheb[0], cheb[1], c_cert, momv[0])
            if val_fr is None:
                n_deg += 1
                continue
            vals[kd] = val_fr / pivf
        if not vals:
            row["bound_fr"] = None
            continue
        for kd, bfr in sorted(vals.items()):
            if float(bfr) * piv < row["q_wall"] \
                    - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                sign_fail += 1
            val_f, jac = rho_source(mat, c_f, kd)
            if math.isfinite(val_f):
                d_xr = max(d_xr, abs(float(bfr) - val_f)
                           / max(1.0, abs(val_f)))
            if jac is not None:
                node = float(np.linalg.eigvalsh(jac)[0])
                if node < c_f - NODE_TIE * max(1.0, c_f):
                    node_fail += 1
        best = min(vals.values())
        row["bound_fr"] = best
        row["bound_f"] = float(best)
        row["k_used"] = min(kd for kd, v in vals.items() if v == best)
        got = chol_iv(np.asarray(row["step"]["Bblk"], float), c_f)
        if got:
            iv_conf += 1
        else:
            iv_ref += 1
        rho4, _ = rho_source(mat, c_f, KBASE)
        rho5, _ = rho_source(mat, c_f, KDEEP)
        dat = dict(r_floor=c_f / piv, sigma=row["sigma"],
                   rho4=rho4, rho5=rho5)
        for k in (0, 1):
            val = float(mom[k]) / piv ** (k + 2)
            dat["g%d" % k] = (math.log10(abs(val)) if val > 0.0
                              else float("nan"))
        row["dat"] = dat
        row["closes_schur"] = best < SCHUR_BAR
        row["closes_env"] = best <= T_R
    check("C1 exact-rational LDL floor certified on %d/%d steps "
          "(%d REFUSED)" % (len(rows) - n_ref, len(rows), n_ref),
          n_ref == 0, kill="K2")
    check("C2 floor quality: certified floor never exceeds the float "
          "truth (%d exceed), within rel %.2e <= %.0e"
          % (n_exceed, d_gapc, CERT_GAP_RTOL),
          n_exceed == 0 and d_gapc <= CERT_GAP_RTOL, kill="K2")
    check("C3 exact Chebyshev == float Lanczos at K = %d: max rel "
          "%.2e <= %.0e" % (KDEEP, d_coef, COEF_TIE),
          d_coef <= COEF_TIE, kill="K2")
    check("C4 exact Radau == float route at every consumed depth: "
          "max rel %.2e <= %.0e (%d degenerate)"
          % (d_xr, XR_TIE, n_deg), d_xr <= XR_TIE and n_deg == 0,
          kill="K2")
    check("C5 RB1 BOUND PROPERTY WARD: %d violations (0 required)"
          % sign_fail, sign_fail == 0, kill="K2")
    check("C6 node ward at the certified floor: %d nodes below the "
          "floor" % node_fail, node_fail == 0, kill="K2")
    check("C7 interval cross-tier (E5, refuse-only): %d confirmed, "
          "%d REFUSED-WIDTH, 0 denials possible"
          % (iv_conf, iv_ref), True)
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    n_schur = sum(1 for r in ok_rows if r["closes_schur"])
    n_env = sum(1 for r in ok_rows if r["closes_env"])
    m1 = [1.0 - r["bound_f"] for r in ok_rows]
    me = [T_R_F - r["bound_f"] for r in ok_rows]
    check("C8 CLOSING CENSUS on the legal set: certified bound < 1 "
          "on %d/%d steps (worst margin %.4f); bound <= t_R %.4f on "
          "%d/%d (worst margin %.4f)"
          % (n_schur, len(ok_rows), min(m1) if m1 else float("nan"),
             T_R_F, n_env, len(ok_rows),
             min(me) if me else float("nan")), True)
    return ok_rows


def scale_invariance_ward(rows):
    """G5: sigma, rho_4, rho_5 invariant under Mt -> lambda Mt."""
    d_max = 0.0
    n_used = 0
    for row in rows[:4]:
        mat = row["step"]["Mt"]
        base = None
        for lam in SCALE_SET:
            scl = mat * lam
            c_s = float(np.linalg.eigvalsh(np.asarray(scl)[1:, 1:])[0])
            jf = jacobi_form(scl)
            if jf is None:
                continue
            sig = sigma_quotient(np.concatenate(jf[::-1]))
            r4, _ = rho_source(scl, c_s, KBASE)
            r5, _ = rho_source(scl, c_s, KDEEP)
            v = (sig, r4, r5)
            if base is None:
                base = v
            else:
                d_max = max(d_max, max(abs(a - b) / max(1.0, abs(b))
                                       for a, b in zip(v, base)))
        n_used += 1
    check("G5 SCALE-INVARIANCE ward on %d steps x %d scales: max rel "
          "drift %.2e <= %.0e" % (n_used, len(SCALE_SET), d_max,
                                  SCALE_TIE),
          d_max <= SCALE_TIE, kill="K2")


def rho_gate(rows):
    if SMOKE:
        check("G4 CCLXXXVII breach-anatomy repro SMOKE-SKIPPED "
              "(typed)", True)
        return
    hit = [r for r in rows
           if r["mode"] == "bridge" and int(r["h"]) == RHO_REF["h"]
           and r["kz"] == RHO_REF["kz"]
           and r.get("bound_fr") is not None]
    if not hit:
        check("G4 the %d bridge step was not formed" % RHO_REF["h"],
              False, kill="K3")
        return
    r = hit[0]
    ok = (abs(r["dat"]["rho5"] / RHO_REF["rho5"] - 1.0) <= RHO_RTOL
          and abs(r["sigma"] / RHO_REF["sigma"] - 1.0) <= RHO_RTOL
          and abs(r["bound_f"] / RHO_REF["bound"] - 1.0) <= RHO_RTOL)
    check("G4 the KNOWN CCLXXXVII breach anatomy reproduces on the "
          "h %d bridge: rho_5 %.6f / sigma %.6f / bound %.6f vs "
          "(%.6f / %.6f / %.6f), rtol %.0e -- KNOWN, cited, not a "
          "new finding"
          % (RHO_REF["h"], r["dat"]["rho5"], r["sigma"], r["bound_f"],
             RHO_REF["rho5"], RHO_REF["sigma"], RHO_REF["bound"],
             RHO_RTOL), ok, kill="K3")


def print_table(rows):
    print("\n    THE LEGAL-SET PROFILE TABLE (certified):")
    print("    idx mode    kz    h      n_raw       c_raw     c/n    "
          " sigma     rho4      rho5      K  bound_cert  m_1")
    for row in rows:
        d = row["dat"]
        print("    %3d %-7s %-5d %6d %11.4g %10.4g %8.4f %9.6f "
              "%9.6f %9.6f %2d %11.6f %9.6f"
              % (row["index"], row["mode"], row["kz"],
                 int(row["h"]), row["n_piv"], row["c_meas"],
                 d["r_floor"], d["sigma"], d["rho4"], d["rho5"],
                 row.get("k_used", 0), row["bound_f"],
                 1.0 - row["bound_f"]))


# ================================= the map + the cofinal verdict
def anatomy_wards(reads):
    section("AN -- anatomy wards on every built cell")
    n_rank = n_e8 = n_tot = 0
    d_rank = 0
    for r in reads:
        rung = r["rung"]
        if rung is None or "tau" not in rung:
            continue
        n_tot += 1
        if "n_unit" in rung:
            expect = max(0, rung["n_neg_nodes"] - rung["rank_g"])
            got = rung["n_unit"]
            if got >= expect:
                n_rank += 1
            d_rank = max(d_rank, abs(got - expect))
        if (rung["tau"] > 0.0 and rung.get("lamS") is not None
                and rung["lamS"] >= rung["tau"]
                - 1e-12 * max(1.0, abs(rung["tau"]))):
            n_e8 += 1
        elif rung["tau"] <= 0.0:
            n_e8 += 1
    check("W7 RANK IDENTITY: #unit eigenvalues >= max(0, n_neg - "
          "rank(G)) on %d/%d built cells (max slack %d; typically "
          "vacuous, n_neg < h here)"
          % (n_rank, n_tot, d_rank), n_rank == n_tot, kill="K2")
    check("W8 E8 ward lamS >= tau on every built PD cell "
          "(%d/%d conforming; consumed nowhere)"
          % (n_e8, n_tot), n_e8 == n_tot, kill="K2")


def legality_map(reads, lad_tau):
    section("MAP -- THE LEGALITY MAP (fractions per bin, tau "
            "geometry, NEGA anatomy)")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"]]
    # ---- per-bin fractions
    bins = []
    for lo, hi in DBINS:
        cells = [r for r in built if lo < r["cell"]["h"] <= hi]
        if not cells:
            continue
        n_leg = sum(1 for r in cells if r["verdict"] == "LEGAL")
        n_marg = sum(1 for r in cells if r["verdict"] == "MARGINAL")
        best = max((r for r in cells if r["verdict"] == "LEGAL"),
                   key=lambda r: r["rung"]["tau"], default=None)
        bins.append(dict(lo=lo, hi=hi, n=len(cells), n_leg=n_leg,
                         n_marg=n_marg, best=best))
        print("    bin (%6d, %6d]: %d built, %d LEGAL, %d MARGINAL"
              "%s"
              % (lo, hi, len(cells), n_leg, n_marg,
                 ("; MAX-TAU pick h %d kz %d tau %.4g"
                  % (best["cell"]["h"], best["cell"]["kz"],
                     best["rung"]["tau"])) if best else ""))
    # ---- the tau(h) geometry
    leg = [(r["cell"]["h"], r["rung"]["tau"]) for r in built
           if r["rung"]["tau"] > 0.0]
    neg = [(r["cell"]["h"], r["rung"]["tau"]) for r in built
           if r["rung"]["tau"] <= 0.0]
    print("    tau sign census on %d built cells: %d positive, %d "
          "negative" % (len(built), len(leg), len(neg)))
    if len(leg) >= 3:
        s, e, r2, a = linfit([math.log10(h) for h, _t in leg],
                             [math.log10(t) for _h, t in leg])
        print("    LEGAL-tau drift fit log10 tau = %.4f + %.4f "
              "log10 h (2SE %.4f, R2 %.3f) [MEASURED]"
              % (a, s, e, r2))
        if s < 0.0:
            hx = 10.0 ** ((math.log10(TAU_NOISE) - a) / s)
            print("    extrapolated tau -> TAU_NOISE crossing at "
                  "h ~ %.3g [CONJECTURE-GRADE, a fit]" % hx)
    for r in built:
        if r["rung"]["tau"] <= 0.0:
            rung = r["rung"]
            print("    NEGA anatomy h %d kz %d: tau %.4g, negA %d, "
                  "negS %s (bad mode %s the core seat), bottom "
                  "spec(A) %s"
                  % (r["cell"]["h"], r["cell"]["kz"], rung["tau"],
                     rung["negA"], rung.get("negS", "-"),
                     "SURVIVES to" if rung.get("negS", 0) > 0
                     else "does NOT reach",
                     ["%.3g" % v for v in rung.get("eva_bot", [])]))
    if lad_tau.get("min"):
        tv, hv, kv = lad_tau["min"]
        frontier = min((abs(r["rung"]["tau"]) for r in built
                        if r["cell"]["h"] > 6000), default=None)
        print("    COMPARISON: registered-ladder min tau %.4g "
              "(h %d kz %d)%s vs frontier min |tau| %s"
              % (tv, hv, kv,
                 ("; h1219 rung tau %.4g" % lad_tau["r1219"][0])
                 if lad_tau.get("r1219") else "",
                 ("%.4g" % frontier) if frontier else "-"))
    return bins


def cofinal_verdict(reads, bins):
    if SMOKE:
        return "LEGFRONT-SMOKE(no frontier cells built by design)"
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"] and r["cell"]["h"] > DBINS[0][0]]
    if not built or not bins:
        return "LEGFRONT-FRONTIER-AMBIGUOUS(no frontier cell built)"
    deepest = max(built, key=lambda r: r["cell"]["h"])
    deep_bin = bins[-1]
    gaps = [b for b in bins if b["n_leg"] == 0]
    h_star = max((r["cell"]["h"] for r in built
                  if r["verdict"] == "LEGAL"), default=None)
    if all(b["n_leg"] >= 1 for b in bins) \
            and deepest["verdict"] == "LEGAL":
        return ("LEGFRONT-COFINAL-MEASURED(h* = %d; every built bin "
                "legal; rule MAX-TAU-PER-BIN)" % h_star)
    if deep_bin["n_leg"] >= 1 and gaps:
        return ("LEGFRONT-COFINAL-GAPPED(h* = %d; gap bins %s)"
                % (h_star, ["(%d,%d]" % (b["lo"], b["hi"])
                            for b in gaps]))
    if deep_bin["n_leg"] == 0:
        second = bins[-2] if len(bins) >= 2 else None
        if (second is not None and second["n_leg"] == 0) \
                or deep_bin["n"] >= 2:
            return ("LEGFRONT-TERMINATES-MEASURED(last legal h = %s "
                    "on the built horizon)" % h_star)
    return ("LEGFRONT-FRONTIER-AMBIGUOUS(deepest built h %d %s; "
            "single-sample)" % (deepest["cell"]["h"],
                                deepest["verdict"]))


# ==================================================== controls
def controls(census, anchors, rows):
    section("X -- CONTROLS-MUST-FIRE")
    hs = np.asarray([c["h"] for c in census], float)
    tgt = 600 if SMOKE else 1300
    cell = census[int(np.argmin(np.abs(hs - tgt)))]
    anc = sorted(anchors, key=lambda r: r["h"])
    below = [a for a in anc if a["h"] <= cell["h"]]
    r1 = below[-1] if below else anc[0]
    print("    control cell: h %d kz %d alpha %.4f; anchor %s kz %d "
          "h %d" % (cell["h"], cell["kz"], cell["alpha"],
                    r1["kind"], r1["kz"], r1["h"]))

    def world_read(world, seed=None):
        rung = build_cell(cell, world=world, scr_seed=seed)
        ok, why = cell_legal(rung)
        out = dict(world=world, legal=ok, why=why,
                   tau=rung.get("tau", float("nan")))
        if "S" not in rung:
            return out
        sts = ob.make_steps([r1, rung])
        if not sts:
            return out
        st = sts[0]
        mat = sym(st["Q"].T @ (rung["S"] / abs(float(st["tau"])))
                  @ st["Q"])
        piv = float(mat[0, 0])
        try:
            c_w = float(np.linalg.eigvalsh(np.asarray(mat)[1:, 1:])[0])
        except np.linalg.LinAlgError:
            return out
        jf = jacobi_form(mat)
        out["piv"] = piv
        out["sigma"] = (sigma_quotient(np.concatenate(jf))
                        if jf is not None else float("nan"))
        out["rho5"] = (rho_source(mat, c_w, KDEEP)[0]
                       if c_w > 0.0 and piv > 0.0 else float("nan"))
        return out

    scr = world_read("scramble", seed=SCR_SEED)
    smo_all = []
    x2_depths = (600,) if SMOKE else X2_DEPTHS
    for dep in x2_depths:
        cdep = census[int(np.argmin(np.abs(hs - dep)))]
        rung = build_cell(cdep, world="smooth")
        ok, why = cell_legal(rung)
        smo_all.append((cdep["h"], ok, why,
                        rung.get("tau", float("nan"))))
        print("      SMOOTH world h %-6d legal %-5s (%s) tau %s"
              % (cdep["h"], ok, why,
                 ("%.4g" % rung["tau"]) if "tau" in rung else "-"))
    sig_hi = max(r["dat"]["sigma"] for r in rows)
    rho_hi = max((r["dat"]["rho5"] for r in rows
                  if math.isfinite(r["dat"]["rho5"])),
                 default=float("nan"))
    print("      scramble world: legal %s (%s) tau %s sigma %s"
          % (scr["legal"], scr["why"],
             ("%.4g" % scr["tau"]) if math.isfinite(scr["tau"])
             else "-",
             ("%.6f" % scr["sigma"]) if math.isfinite(
                 scr.get("sigma", float("nan"))) else "-"))
    print("      measured legal-set envelope: sigma <= %.6f, rho_5 "
          "<= %.6f" % (sig_hi, rho_hi))

    def outside(w):
        s = w.get("sigma", float("nan"))
        if not math.isfinite(s):
            return True, "sigma non-finite"
        if s > sig_hi or s <= 0.0:
            return True, "sigma %.4f outside" % s
        r5 = w.get("rho5", float("nan"))
        if math.isfinite(r5) and math.isfinite(rho_hi) \
                and r5 > rho_hi:
            return True, "rho_5 %.4f outside" % r5
        return False, "inside the envelope"

    scr_out, scr_why = outside(scr)
    check("X1 the SCRAMBLE world (seed %d) fires: legality %s / %s"
          % (SCR_SEED, "LEFT" if not scr["legal"] else "kept",
             scr_why), (not scr["legal"]) or scr_out, kill="K4")
    n_illegal = sum(1 for _h, ok, _w, _t in smo_all if not ok)
    check("X2 the SMOOTH world LEGALITY PROFILE fires -- THE "
          "DISCRIMINATION: illegal at %d/%d tested depths (all "
          "required)" % (n_illegal, len(smo_all)),
          n_illegal == len(smo_all), kill="K4")
    # X3: a synthetic near-1 cell must NOT certify
    base = rows[0]["step"]["Mt"].copy()
    piv0 = float(base[0, 0])
    vec0 = np.asarray(base)[1:, 0]
    blk0 = np.asarray(base)[1:, 1:]
    q0 = float(vec0 @ np.linalg.solve(blk0, vec0))
    scale = math.sqrt(CTRL_SIG_NEAR * piv0 / q0)
    ctrl = base.copy()
    ctrl[1:, 0] = vec0 * scale
    ctrl[0, 1:] = vec0 * scale
    sig_c = (float(np.asarray(ctrl)[1:, 0]
                   @ np.linalg.solve(blk0, np.asarray(ctrl)[1:, 0]))
             / piv0)
    c_c = float(np.linalg.eigvalsh(blk0)[0])
    _pv, momc, blkc = exact_wall_data(ctrl, 2 * KDEEP - 2)
    cc = cert_floor_exact(blkc, Fraction(0),
                          Fraction(float(c_c)) * (Fraction(1)
                                                  + Fraction(1,
                                                             10 ** 6)))
    bnd_c = float("nan")
    if cc is not None:
        cheb = chebyshev_monic(momc, KDEEP)
        if cheb is not None:
            vv = radau_exact(cheb[0], cheb[1], cc, momc[0])
            if vv is not None:
                bnd_c = float(vv / Fraction(float(ctrl[0, 0])))
    check("X3 the synthetic NEAR-1 control (truth sigma %.4f > 1) "
          "must NOT certify bound < 1: certified K = %d bound %.6f"
          % (sig_c, KDEEP, bnd_c),
          math.isfinite(bnd_c) and bnd_c >= 1.0, kill="K4")
    # X4: an inflated floor claim must be refused by BOTH tiers
    n_ref_x = n_try = 0
    for row in rows[:2]:
        n_try += 1
        bad = Fraction(float(row["c_meas"])) * Fraction(
            int(CTRL_INFLATE * 100), 100)
        okx, _ = pd_exact(exact_wall_data(row["step"]["Mt"],
                                          2)[2], bad)
        oki = chol_iv(np.asarray(row["step"]["Bblk"], float),
                      float(bad))
        if (not okx) and (oki is None):
            n_ref_x += 1
    check("X4 an INFLATED floor claim (x %.2f) is refused by BOTH "
          "tiers on %d/%d steps" % (CTRL_INFLATE, n_ref_x, n_try),
          n_ref_x == n_try, kill="K4")


# ==================================== S: the screens
def screens(rows):
    section("S -- tau and CCXVII c_h relocation screens (CCXLVII "
            "bars verbatim)")
    taus = [r["tau_scale"] for r in rows]
    verds = []
    for key in ("sigma", "rho4", "rho5", "r_floor"):
        vals = [r["dat"][key] for r in rows]
        txt, vd = screen(vals, taus, "tau-screen %s" % key)
        print("    " + txt)
        verds.append(vd)
    for lab, vals in (("t_R - rho5",
                       [T_R_F - r["dat"]["rho5"] for r in rows]),
                      ("1 - bound",
                       [1.0 - r["bound_f"] for r in rows])):
        txt, vd = screen(vals, taus, "tau-screen %s" % lab)
        print("    " + txt)
        verds.append(vd)
    n_reloc = sum(1 for v in verds if v == "RELOC")
    check("S1 tau relocation screens on the fitted levels and "
          "margins: %d PASS, %d AMBIG, %d RELOC, %d vacuous"
          % (verds.count("PASS"), verds.count("AMBIG"), n_reloc,
             verds.count("VAC")), n_reloc == 0)
    pool = [r for r in rows
            if r["X"] <= core.ATOM_MAX and r["h"] <= CH_HMAX]
    if len(pool) >= 3:
        chs = []
        sigs = []
        seen = set()
        for r in sorted(pool, key=lambda r: r["h"]):
            if r["kz"] in seen or len(chs) >= CH_N:
                continue
            seen.add(r["kz"])
            try:
                rr = ob.window_of(r["kz"])
                c_at = np.asarray(core.atom_lags_at(
                    rr["alpha"], rr["M"], rr["uu"],
                    2.0 * rr["lam"])[0], float)
                dens = eul.grid_density(rr["c_ar"] + c_at)
                pos = eul.gram_from_dens(
                    np.where(dens > 0.0, dens, 0.0), rr["M"])
                neg = eul.gram_from_dens(
                    np.where(dens > 0.0, 0.0, -dens), rr["M"])
                last = pos.shape[0] - 1
                top = float(sla.eigh(neg, pos, eigvals_only=True,
                                     subset_by_index=[last,
                                                      last])[0])
                chs.append(1.0 - top)
                sigs.append(r["dat"]["sigma"])
            except Exception as exc:               # noqa: BLE001
                print("    c_h cell kz %d REFUSED (%s)"
                      % (r["kz"], exc))
        if len(chs) >= 3:
            txt, vd = screen(sigs, chs, "c_h-screen sigma")
            print("    " + txt)
            check("S2 CCXVII c_h relocation screen: %s" % vd,
                  vd != "RELOC")
            return
    check("S2 CCXVII c_h relocation screen: VACUOUS (%d in-surface "
          "steps of %d; the deployed surface window is only defined "
          "for X <= %.0e and h <= %d -- the legal frontier set is "
          "OUT-OF-SURFACE, typed per CCLXXXVII)"
          % (len(pool), len(rows), float(core.ATOM_MAX), CH_HMAX),
          True)


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
  HONEST FRAME.  Finite float64 + exact-rational measurements on
  BUILT cells of the deployed deep-frame construction (TAB2 census,
  builder verbatim).  Wall-legality is the CCLXXIII/CCLXIX cell_legal
  read of the ASSEMBLED float64 matrix (the known scope edge, A5);
  MARGINAL cells acknowledge the tau = 0 boundary of that object.
  The cofinal statement is a statement about the BUILT horizon and
  the frozen bins, never about all h; every extrapolation is a fit
  and is typed CONJECTURE-GRADE.  The legality census does not touch
  the class-membership question (CCLXXXVII) except through the cited
  reproduction gates.  No marker moves, no promotion, NO RH claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("legality_frontier_probe -- "
          "PRIME.ONEBADMODE.LEGALITY.FRONTIER.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_c = ast_scan_functions(CERT_FUNCS, DERIV_BANNED)
    check("S0.2 AC certificate path sees ENTRIES and frozen "
          "constants only (%s)" % (",".join(sorted(set(bad_c)))
                                   or "clean"), not bad_c, kill="K1")
    bad_f = ast_scan_functions(FLOAT_FUNCS, DERIV_BANNED)
    check("S0.3 AC float bound path sees ENTRIES and frozen "
          "constants only (%s)" % (",".join(sorted(set(bad_f)))
                                   or "clean"), not bad_f, kill="K1")

    lad_steps, anchors, lad_tau = build_ladder()
    if KILLS:
        return finish([])
    build_tab2()
    census = deep_census()
    if KILLS:
        return finish([])

    lad_rows = [dict(step=st, mode=ob.seg_of(st),
                     h=float(st["r2"]["h"]), kz=int(st["r2"]["kz"]),
                     alpha=float(st["r2"]["alpha"]),
                     X=math.exp(2.0 * float(st["r2"]["alpha"])),
                     tau_scale=float(st["tau"]),
                     schur=float(st["gap"]),
                     n_piv=float(st["n0"]),
                     c_meas=float(st["lamB1"]), index=i)
                for i, st in enumerate(lad_steps)]
    lad_rows = jacobi_identity_wards(lad_rows, "registered ladder")
    repro_anchors(lad_rows)
    if KILLS:
        return finish([])

    reads = census_build(census)
    if KILLS:
        return finish([])
    census_gates(reads)
    anatomy_wards(reads)

    rows = profile_steps(reads, anchors)
    check("PR1 the profile admitted %d steps on the built legal set"
          % len(rows), len(rows) >= (1 if SMOKE else 3), kill="K1")
    if KILLS:
        return finish([])
    rows = jacobi_identity_wards(rows, "legal-set profile")
    rows = entry_data(rows)
    scale_invariance_ward(rows)
    if KILLS:
        return finish([])
    print_table(rows)
    rho_gate(rows)

    bins = legality_map(reads, lad_tau)
    verdict = cofinal_verdict(reads, bins)
    controls(census, anchors, rows)
    screens(rows)

    labels = [verdict]
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"]]
    n_leg = sum(1 for r in built if r["verdict"] == "LEGAL")
    n_nega = sum(1 for r in built if r["rung"]["tau"] <= 0.0)
    n_marg = sum(1 for r in built if r.get("marginal"))
    labels.append("LEGALITY-MAP(%d built, %d legal, %d tau<0, %d "
                  "marginal; horizon h %d)"
                  % (len(built), n_leg, n_nega, n_marg,
                     max((r["cell"]["h"] for r in built), default=0)))
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    n_schur = sum(1 for r in ok_rows if r["closes_schur"])
    n_env = sum(1 for r in ok_rows if r["closes_env"])
    labels.append("CHAIN-PROFILE(bound < 1 on %d/%d; <= t_R on "
                  "%d/%d, the deficit being the CITED known "
                  "CCLXXXVII breach class)"
                  % (n_schur, len(ok_rows), n_env, len(ok_rows)))
    negas = [r for r in built if r["rung"]["tau"] <= 0.0]
    if negas:
        seats = {("negS>0" if r["rung"].get("negS", 0) > 0
                  else "negS=0") for r in negas}
        labels.append("NEGA-ANATOMY(%d cells, |tau| %.3g..%.3g, "
                      "seat %s)"
                      % (len(negas),
                         min(abs(r["rung"]["tau"]) for r in negas),
                         max(abs(r["rung"]["tau"]) for r in negas),
                         "/".join(sorted(seats))))
    return finish(labels)


if __name__ == "__main__":
    main()
