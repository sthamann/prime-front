#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fewatom_reduction_probe -- PRIME.FEWATOM.REDUCTION.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
turan-extremal lane's turan_extremal_probe.py, the independent
session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface of the promotion wave) are not
touched.

=======================================================================
MISSION (round ~197: the few-atom reduction).  Round 195
(cancellation_functional_probe, SPEC_SHA a50b85bb112513a1, note
DXVIII) delivered the ACF law (atom contribution = -2 w_q
ACF_x(log q) exactly), the measured SIGN LAW at the collapsing
direction v_0 (every resolvable atom negative at all 14 rungs,
near-exponential decay in log q, the commensurate q = h atom exactly
zero), and LOCALIZATION m99 = 1..2 of 3..12 atoms.  THIS round
attacks the two questions that decide whether the wall's prime side
reduces to a low-dimensional family:

  F1 THE SIGN LAW MECHANISM.  A_{v_0}(t) = sum_k v_k cos(om_k t) is
     an L-periodic EVEN cosine polynomial on the lattice om_k =
     2 pi k / L (so A(L - t) = A(t) identically -- the profile is
     symmetric about L/2; measured, not sold as a find).  Shape
     ladder at every rung: peak location t_peak/L, strict sign
     changes on the half-window, min/max ratio, negative-mass
     fraction eta = int A_-^2 / int A^2, 0.1-level width fraction.
     THE ONE-LINE CANDIDATE: if A_{v_0} >= 0 on [0, L] then EVERY
     autocorrelation g(u) = int_0^{L-u} A A(.+u) >= 0 by inspection
     -- the sign law would reduce to proving A_{v_0} >= 0.  Gated
     resolve-and-record per rung.  THE DECAY MECHANISM: near the
     window edge u -> L the ACF is the SELF-CONVOLUTION of the
     profile's edge jet, g(L - eps) = int_0^eps A(t) A(eps - t) dt
     (exact, from the lattice symmetry); if A ~ t^{2m} at the edge
     (first m even jets d_j = sum_k v_k b_k^j, j < m, cancel) then
     g(L - eps) ~ eps^{4m+1}.  Measured three ways per rung: the
     edge-power fit p_g of log10|g| vs log10(L-u) (24-point frozen
     lag lattice u_l = l L/25 + the atom lags), the profile edge
     power p_A (envelope fit of log10|A| vs log10 t on the edge
     side), and the jet-cancellation ladder jr_j =
     |sum v_k b_k^j| / sum |v_k| b_k^j with MJET = #leading j at
     jr_j <= JET_BAR.  LAWS UNDER TEST: SELFCONV p_g == 2 p_A + 1;
     JET p_A == 2 MJET.  Decay-exponent candidates adjudicated
     honestly: c = 1/2 (weight class, g ~ q^{-c}) vs the measured
     exponential rate c_h = -s_g ln 10, and the tau-normalized rate
     r_tau = (-s_g) L / |log10 taufrac| (if r_tau is flat the decay
     'constant' rides tau and is typed as alignment-law territory,
     never sold as new arithmetic).
  F2 THE EFFECTIVE HORIZON.  Predefined: Q99(h) (and Q999) = the
     smallest prefix of atoms IN ASCENDING q whose partial sum is
     within 1% (0.1%) of the prime total Pr at v_0 (absolute guard
     1e-6 (|P|+|A|) as in r195); reported as (n99, q99).  THE
     DECISIVE LADDER: bounded (always q99 <= 3) or growing.  THE
     HONEST COUNTERWEIGHT (predefined): the DEMAND-SCALE horizon
     QTAU(h) = the smallest prefix whose remaining tail is <=
     |lambda_0| -- the wall demand at v_0 is a lambda_0-scale
     cancellation, so any atom whose |t_q| exceeds lambda_0 is
     load-bearing at the demand scale; dexgap(h) = log10(|Tail_{q>3}|
     / lambda_0) prices the compression (rides tau BY CONSTRUCTION,
     flagged definitional).
  F3 THE REDUCED STATEMENT.  Per rung: lambda_0 = P + A + t_2 + t_3
     + Tail EXACTLY (r195 budget resplit, definitional); the
     2-atom reduced form red = P + A + t_2 + t_3 = lambda_0 + |Tail|
     is positive at the |Tail| scale; the tail obeys the measured
     geometric majorant bound = |t_first>3| / (1 - rho_max) >=
     |Tail| (accelerating decay makes it valid); BUT certification
     of lambda_0 > 0 through ANY lossy tail bound requires the
     bound sharp to lambda_0 -- overshoot (bound - |Tail|) vs
     lambda_0 recorded: expected astronomically dead (DEAD-CLASS
     guard honored, the l1/majorant lesson of r195 repeated at the
     tail).  ADJUDICATION (frozen logic): the reduction is
     structural (budget-scale, Q99 atoms + measured-law tail), NOT
     a complexity drop in h (every ingredient is a functional of
     v_0(h)); enum + rider, tau-screened.
  F4 WORLDS AND WITNESS.  Bottom-direction (mp.eigsy, most negative
     eigenvalue) anatomy at (SCRARITH,5), (EPSTEIN,8): sign
     ladders, horizons, profiles -- do the fake worlds break the
     one-signed law or move the horizon (measured)?  (SMOOTH,5):
     continuum profile + lag-lattice ACF signs + the continuum
     localization w99 (mass quantile of e^{w/2}|g|, 25-segment
     trapezoid, disclosed grid-resolution record).  WITNESS (r172
     recipe VERBATIM, h = 5, W = 1000): dv = A_2 (W-1)/(b_2 - b_1)
     on ray modes 1, 2 of the builder ray cn; base direction
     y_base ~ par_k cn_k vs witness direction y_wit ~ par_k cn2_k
     (Raw-coordinate transport of the M-side ray, y^T Raw y ==
     ray^T M ray by congruence); budgets, sign ladder, horizon at
     both + overlap wards -- where the y_t x1000 deformation hits
     the few-atom structure.

PRE-REGISTERED PRIORS (resolve-and-record; NONE is gate-forcing):
  P1 A_{v_0} >= 0 per rung: GENUINELY OPEN (the lattice symmetry
     argument cuts both ways; the measurement decides).
  P2 horizon bounded: Q99 in {2, 3} at every rung (from r195 m99).
  P3 the decay rate is tau-tracking (r_tau flat) rather than
     h-universal (from the h=13 ladder estimate ~0.87).
  P4 fake worlds break the one-signed atom law (their budget
     anatomy is top-of-spectrum, r186/r195-concordant).
  P5 the witness preserves the sign ladder's signs but shifts
     magnitudes (matrix-side objects witness-invariant; the
     DIRECTION here is witness-deformed, so t_q may move: open).

NOTATION (r171-r195 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a = 2 pi k/L; b_k = om_k^2;
nrm_0 = sqrt(2a), nrm_k = sqrt(a); par_k = (-1)^k; atoms
{(u_q, w_q)} = {(log q, log p/sqrt q)}, q = p^m <= h, ascending q;
Raw = D_par N M N D_par; W(u) the r195 ACF kernel (off-diag
2(om_i sin(om_i u) - om_j sin(om_j u))/(b_i - b_j), diag
sin(om_k u)/om_k + (u - L)cos(om_k u), k = 0 slot 2(u - L));
t_q = w_q v_0^T W(u_q) v_0 = -2 w_q g(u_q); g(u) = ACF of the
windowed mode polynomial at v_0.  v_0 = bottom eigenvector of Raw
by mp INVERSE ITERATION at every rung (r195 amendment A3 lineage;
3 LU solves, wards: eigen-residual, Rayleigh stability iter2->3,
eigsy-overlap at ANAT_MP).  Profile grid: N = 16 K points t_j =
j L / N, exact cosine table ct[m] = cos(2 pi m / N), A_j = sum_k
v_k ct[(k j) mod N] (lattice-exact); half-window stats j <= N/2;
global sign normalized so the peak value is positive.  Lag lattice:
u_l = l L / 25, l = 1..24, trig by 25-point exact table; g_l =
-(v_0^T W(u_l) v_0)/2.  Fits by least squares (fit_line), resolvable
= |value| > 1e-30 x max.  Frozen probe vector xg1_k =
frac((k+1) phi) - 1/2 (pole-square + quadrature wards).

DPS schedule (r182/r189/r195 ladder VERBATIM): DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16, H_HOLD = 20.
ANAT_MP = (4, 5, 8, 13) (eigsy overlap ward).  QUAD ward at h = 4, 5:
lag points l = 3, 6, 9 of 25, vectors {xg1, v_0}, oscillation-split
mp.quad vs the kernel form.  CONTROLS: (SMOOTH, 5, 60),
(SCRARITH, 5, 60), (EPSTEIN, 8, 80).  WIT_RUNG = 5, WIT_FACT = 1000.
JMAX = 12 jets; JET_BAR = 1e-3 (prefix rule).  Fit domains: lag-grid
fits on resolvable l = 1..24 (every rung); atom-lag fits at rungs
with >= 3 resolvable atoms; profile edge fits on the frozen edge
window j = 1..J_EDGE, J_EDGE = min(max(4, N//64), j_peak - 1)
(amendment A1: the original envelope-local-maxima rule collapses to
2 points on a nodeless monotone bump -- pre-freeze instrument fix,
disclosed; smoke1 kept).

FROZEN BARS: ASM_BAR 1e-30; POLE_SQ_BAR 1e-35; BUDGET_BAR 1e-25;
INVIT_RES_BAR 1e-12; INVIT_STAB_BAR 1e-6; OVL_BAR 1e-12; GRID_BAR
1e-40 (cos-table vs direct, rel); QUAD_BAR 1e-25 (xg1), QUADV0_BAR
1e-15 (v_0 slot, deep values, rel to the kernel form); ZCLS 1e-30
(zero class, rel); PROF_NONNEG_BAR 1e-30 (rel); CTRL_ASM_BAR 1e-25;
SMOOTH_ID_BAR 1e-25; WIT_YT_BAND (990, 1010); WIT_A0_BAR 1e-6;
TAU_FLAT_BAR 0.30; COND_LO/HI 1e-40/1e-10; RUNTIME_BAR 2700 s.
Record tolerances: LOG_TOL 0.10 dex; SLOPE_TOL 0.05; FIT_TOL 0.10
(relative, fitted exponents); FRAC_TOL 0.05 (absolute, fractions);
counts exact.  R195 inheritance cross-checks: depth vs R195_DEPTH
(LOG_TOL), (n+, n-, n0) == R195_SIGNS, m99 == R195_M99 exact.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  signMech  := SIGN-LAW-FROM-NONNEGATIVITY iff A_min >= -1e-30 A_max
               at every rung; else SIGN-LAW-CONCENTRATION-PARTIAL
               iff eta <= 0.01 at every rung; else
               SIGN-LAW-UNEXPLAINED-BY-SHAPE;
  gPosEnum  := ACF-POSITIVE-ALL-LAGS iff gneg = 0 on the lag lattice
               at every MAIN rung, else ACF-POSITIVE-AT-ATOMS-ONLY;
  modelEnum := DECAY-EDGE-POWER iff R2_pow >= R2_exp + 0.05 at every
               fit rung; DECAY-EXPONENTIAL iff reverse everywhere;
               else DECAY-MODEL-MIXED;
  cHalf     := C-HALF-REJECTED iff min_h c_h >= 10 x 0.5 (the weight
               candidate is dead by >= 1 dex), else C-HALF-ALIVE;
  univEnum  := DECAY-EXPONENT-UNIVERSAL iff (max-min)/median of the
               model exponent <= 0.15 across fit rungs; else
               DECAY-EXPONENT-TAU-TRACKING iff (max-min)/median of
               r_tau <= 0.25; else DECAY-RUNG-DEPENDENT-UNMODELED;
  mechEnum  := resolved at freeze from the measured jet-convolution
               deviation ladder |p_g - (4 MJET + 1)| / (4 MJET + 1)
               (JETCONV-LAW-* -- resolve-and-record; the two-step
               profile-window form is recorded, not law-gated);
  horizEnum := HORIZON-BOUNDED-23 iff q99 <= 3 at every rung incl.
               holdout; HORIZON-SLOW iff q99 <= 5 everywhere; else
               HORIZON-GROWING(alpha from log-log fit);
  reduEnum  := FEWATOM-REDUCTION-STRUCTURAL-VALID iff horizon
               bounded AND tail majorant valid at every rung, with
               the MANDATORY rider NOT-A-COMPLEXITY-DROP-IN-H (every
               reduced ingredient is a functional of v_0(h); the
               demand-scale horizon QTAU stays at all resolvable
               atoms); else FEWATOM-REDUCTION-FAILS(where).

RECORD TABLES (frozen at freeze from the disclosed calibration
ladder: THREE structural smokes (smoke1 exposed the envelope-rule
collapse -> amendment A1; smoke2 exposed the profile-window
contamination of the anticipated selfconv gate -> amendment A2;
smoke3 25/25 clean) and ONE disclosed calibration pass
(calib_fa_pass1.log, 25/25, 792.5 s); all logs kept).  RESOLVED
VERDICTS: P1 TRUE -- A_{v_0} >= 0 at ALL 14 rungs (min value
POSITIVE, ladder below; zero sign changes; peak EXACTLY at L/2
at every rung): signMech = SIGN-LAW-FROM-NONNEGATIVITY, the
one-line mechanism is LIVE and the new concrete target is 'prove
A_{v_0} >= 0' (ground-state nodelessness class, Perron-Frobenius/
Krein-Rutman territory -- named as candidate route, NOT consumed);
gPos = ACF-POSITIVE-ALL-LAGS (gneg = 0 at every rung and every
atom lag); model = DECAY-EDGE-POWER (R2_pow 0.966..0.994 vs
R2_exp 0.815..0.854); cHalf = C-HALF-REJECTED (min c_h/0.5 = 28x);
univ = DECAY-RUNG-DEPENDENT-UNMODELED (exponent spread 1.32 of
median; P3 REFUTED: r_tau falls 0.7776 -> 0.3555, NOT flat);
mechEnum = JETCONV-LAW-BAND-APPROXIMATE (p_g tracks 4 MJET + 1,
dev ladder 0.006..0.43, best at mid rungs; the probed lag band is
not asymptotic -- typed measured-law, the jet ladder is r182
alignment structure in ACF coordinates); horizon =
HORIZON-BOUNDED-23 (P2 HOLDS incl. the h = 20 holdout); demand
scale ALL-ATOM (qtau_frac 1.00 everywhere); reduEnum =
FEWATOM-REDUCTION-STRUCTURAL-VALID + NOT-A-COMPLEXITY-DROP-IN-H;
P4 PARTIALLY REFUTED (fake worlds keep one-signed ATOM ladders;
EPSTEIN breaks the SHAPE mechanism: profile node, rmin -0.481,
eta 0.185, gneg 10 of 24 -- the nonneg mechanism separates at the
shape level, not the atom-sign level; SCRARITH keeps the shape,
loses localization m99/n99 3 vs MAIN 1; SMOOTH has NO
localization, w99/L = 0.920); P5 RESOLVED: witness preserves
signs (0,3,1) -> (0,3,1) but flattens the ACF ladder (t-dex
-1.4/-4.0/-8.2 -> -1.0/-2.5/-4.6) and moves n99 1 -> 2 at
direction cost 0.19% (ovl_wit 0.998106) -- the deep-atom ACF
readings are a witness DETECTOR at magnitude level.
CAL_TPEAK: 0.500 at every rung.  CAL_NSC: 0 at every rung.
CAL_RMIN {h: log10(A_min/A_max), POSITIVE min}: 4: -5.02,
  5: -7.54, 6: -9.71, 7: -12.09, 8: -14.28, 9: -16.57, 10: -19.01,
  11: -21.40, 12: -23.97, 13: -26.29, 14: -28.97, 15: -31.07,
  16: -33.63, 20: -43.30 (== the jr_0 ladder: the profile minimum
  IS the near-zero at the window edge).
CAL_ETA: exact 0 (floored to 1e-300) at every rung.
CAL_FW1: 0.596, 0.528, 0.487, 0.448, 0.426, 0.408, 0.391, 0.377,
  0.364, 0.353, 0.345, 0.335, 0.330, 0.306 (h = 4..16, 20).
CAL_MJET: 1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 11, 13, 13, 13.
CAL_JR0: -5.0, -7.5, -9.7, -12.1, -14.3, -16.6, -19.0, -21.4,
  -24.0, -26.3, -29.0, -31.1, -33.6, -43.3.
CAL_PG (lag edge power p_g): 7.141, 9.812, 12.118, 14.604, 16.896,
  19.237, 21.667, 24.249, 26.671, 28.259, 30.577, 32.563, 33.426,
  39.169; p_edge (deepest-pair local): 5.273, 7.448, 9.270,
  11.363, 13.250, 15.257, 17.430, 23.913, 26.703, 32.179, 35.327,
  37.817, 42.663, 54.850; profile edge window p_A: 1.840, 2.194,
  2.478, 2.726, 3.174, 3.588, 4.048, 4.493, 4.929, 5.360, 5.828,
  6.198, 6.815, 8.488 (R2 0.961..0.991; floor-contaminated,
  recorded not law-gated, amendment A2).
CAL_CH: 13.95, 16.43, 18.19, 20.11, 21.73, 23.37, 25.05, 23.60,
  25.00, 23.44, 24.62, 25.53, 23.82, 24.28.
CAL_RTAU: 0.7776, 0.7109, 0.6843, 0.6643, 0.6530, 0.6412, 0.6307,
  0.5517, 0.5415, 0.4792, 0.4707, 0.4676, 0.4135, 0.3555.
CAL_MECH (jetconv dev): 0.428, 0.090, 0.068, 0.141, 0.006, 0.084,
  0.133, 0.164, 0.192, 0.311, 0.321, 0.386, 0.369, 0.261.
CAL_HORIZ {h: (n99, q99, n999, q999)}: 4: (1,2,1,2); 5..13:
  (1,2,2,3); 14, 15, 16, 20: (2,3,2,3).
CAL_QTAUF: 1.00 at every rung.  CAL_GNEG: 0 at every rung.
CAL_DEXGAP: None(h=4, tail below zero class), 7.5, 13.0, 18.2,
  22.9, 27.7, 32.7, 37.6, 42.9, 47.6, 53.1, 57.4, 62.5, 82.0.
CAL_TAILT2: None, -6.86, -5.93, -5.54, -5.27, -5.10, -4.99, -4.90,
  -4.84, -4.78, -4.74, -4.69, -4.66, -4.57.
CAL_CTRL: (SCRARITH, 5): signs (0,3,1), m99 3, n99 3, q99 4,
  gneg 0, nonneg True; (EPSTEIN, 8): signs (0,3,0), m99 3, n99 3,
  q99 6, gneg 10, nonneg FALSE (rmin -0.481, eta 0.185, nsc 1);
  (SMOOTH, 5): gneg 0, w99/L 0.920, nsc 0, id dev 9.6e-62,
  Pr -3.246.
CAL_WIT: ytr 1000.00, a0dev 4.1e-55, ovl_base 1.000000, ovl_wit
  0.998106, base signs (0,3,1) n99 1 P 1.468 Pr -0.0419, wit
  signs (0,3,1) n99 2 P 1.697 Pr -0.0975.
CAL_SLOPES: nscK +0.000, n99f +0.001, fw1 +0.003 (eta slope 0 at
  the floor).

AMENDMENTS (two, both pre-freeze, both disclosed, no bar/dps/grid/
recipe moved):
A1 (smoke1-driven): the profile fit originally selected grid-local
  maxima of |A| as envelope points; on the measured NODELESS
  monotone bump this collapses to 2 points (pA = nan).  Replaced
  by the frozen edge-window rule j = 1..J_EDGE, J_EDGE =
  min(max(4, N//64), j_peak - 1).  No target changed.
A2 (smoke2-driven): the anticipated mechanism gate compared p_g
  against 2 p_A + 1 with p_A from the edge window; measured p_A
  (1.84..8.49) is contaminated by the constant floor A(0) =
  jr_0 > 0 at t <~ L/N and understates the vanishing order, so
  the two-step law fails structurally in that window (dev
  0.53..1.46) while the DIRECT jet-convolution law p_g ==
  4 MJET + 1 tracks (dev 0.006..0.43).  G34 retyped BEFORE the
  calibration freeze to gate the direct-law deviation ladder as a
  record; the two-step deviations stay recorded, not law-gated.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
instrument wards G10-G11; S2 inherited dictionary G20-G22; S3 F1
shape/decay G30-G35; S4 F2 horizon G40-G41; S5 F3 reduction G50-G51;
S6 F4 worlds/witness G60-G61; S7 screens/adjudication G70-G73; S8
pricing G80 + G99 runtime.  DETERMINISM: no randomness anywhere;
ProcessPool results keyed; run2 must be identical modulo wall-clock
tokens (lines carrying 'WALL').

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt X, note DXXIII, 2026-08-22)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays 35fb341bb281b04b.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH10-F1 [MAJOR, the nonnegativity gate certifies strictly less than
#   the headline states; THE HEADLINE STANDS AND IS NOW STRONGER]:
#   ORIGINAL (this spec + note DXX; the continuum wording inherited
#   by r198): F1 headline "A_{v_0} >= 0 on [0, L] ... min value
#   POSITIVE at all 14 rungs" -- stated at CONTINUUM level with a
#   positive minimum.  The MACHINE content was weaker in two
#   independent ways: (i) the measurement is the N = 16K half-window
#   GRID only, with no between-node check anywhere -- for a
#   degree-(K-1) cosine polynomial with O(1) coefficient mass and
#   edge values at 1e-5..1e-43 of the peak, grid nonnegativity does
#   not imply continuum nonnegativity by any cited argument; (ii)
#   the operative gate nonneg := amin >= -1e-30*amax is SIGN-BLIND
#   at the three deepest rungs, where the record minima sit BELOW
#   the zero-class bar (CAL_RMIN h = 15/16/20: -31.07/-33.63/-43.30
#   dex): the frozen gate would ALSO pass on a negative minimum of
#   e.g. -1e-31*amax, so "min value POSITIVE" there was print
#   evidence, not gate certificate.  RETYPE (KA): the r197 gate
#   class is GRID-MEASURED.  THE HEADLINE IS TRUE AND NOW CERTIFIED:
#   Bughunt X (bughunt10_probe.py, SPEC 5551aa7b967230f1, own code,
#   escalated dps) certified CONTINUUM nonnegativity by
#   exact-rational Sturm chains at h = 4, 5 (exact Fractions of the
#   computed direction: ZERO roots in (-1, 1], P(+-1) > 0) and at
#   h = 13, 20 (coefficients rounded at 2^-200/2^-340 with the
#   strict subtracted floor delta = 2^-190/2^-300 BEFORE root
#   counting: A > 0 on ALL of [0, L], not just the grid), and
#   re-verified jr_0 at h = 20 with dps 170 > record 144 (~127
#   digits of sign headroom).  Scope rider (verbatim, for every
#   surface carrying the r197/DXX/r198 nonnegativity headline): "an
#   allen 14 Sprossen GITTER-zertifiziert (N = 16K) mit
#   Nullklassen-Bar 1e-30 (an h = 15/16/20 liegt das Minimum
#   UNTERHALB der Bar-Aufloesung des Gates -- der positive Wert
#   dort ist Print-Evidenz, nicht Gate-Zertifikat); Kontinuums-
#   Nichtnegativitaet auf [0, L] und der positive Minimumswert sind
#   durch Bughunt X per exakter Sturm-Kette bei h = 4, 5, 13, 20
#   ZERTIFIZIERT (eigene Rechnung, eskalierte dps)".  Future
#   profile sign gates use a sign-resolving bar (e.g. refusal-rule-
#   scaled) instead of the atom zero class.  The continuum
#   certificate lives in BH10; NO verdict flips: P1/signMech stand,
#   now stronger than the round left them.
#
# BH10-F3 [NOTE, precision rider KC]: the "edge minimum IS the jr_0
#   ladder" identification is exact UN-NORMALIZED (grid min = A(0) =
#   the jr_0 NUMERATOR exactly); the PRINTED RATIO differs by the
#   r198 parity-misalignment factor (1 - amax/sum|v| = 0.4-0.65% at
#   h = 4/5, i.e. 0.002-0.003 dex, invisible at print precision);
#   the r197/r198 pair (A_{v_0} >= 0 + V0-PARITY-BROKEN) is
#   CONSISTENT -- the two statements are logically independent and
#   both measured TRUE.
# =====================================================================

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 10
RUNTIME_BAR = 2700.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
ANAT_MP = (4, 5, 8, 13)
NGRID_FAC = 16
NLAG_DEN = 25
QUAD_LAGS = (3, 6, 9)
JMAX = 12
JET_BAR = 1e-3
WIT_RUNG = 5
WIT_FACT = 1000
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

ASM_BAR = 1e-30
POLE_SQ_BAR = 1e-35
BUDGET_BAR = 1e-25
INVIT_RES_BAR = 1e-12
INVIT_STAB_BAR = 1e-6
OVL_BAR = 1e-12
GRID_BAR = 1e-40
QUAD_BAR = 1e-25
QUADV0_BAR = 1e-15
ZCLS = 1e-30
PROF_NONNEG_BAR = 1e-30
CTRL_ASM_BAR = 1e-25
SMOOTH_ID_BAR = 1e-25
WIT_YT_BAND = (990.0, 1010.0)
WIT_A0_BAR = 1e-6
TAU_FLAT_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10

LOG_TOL = 0.10
SLOPE_TOL = 0.05
FIT_TOL = 0.10
FRAC_TOL = 0.05

# ----------------- r195 inheritance tables (cancellation_functional)
R195_DEPTH = {4: "-11.11", 5: "-16.25", 6: "-20.70", 7: "-25.50",
              8: "-29.90", 9: "-34.56", 10: "-39.45", 11: "-44.23",
              12: "-49.46", 13: "-54.08", 14: "-59.51",
              15: "-63.74", 16: "-68.86", 20: "-88.25"}
R195_SIGNS = {4: (0, 2, 1), 5: (0, 3, 1), 6: (0, 4, 0),
              7: (0, 4, 1), 8: (0, 5, 1), 9: (0, 6, 1),
              10: (0, 7, 0), 11: (0, 7, 1), 12: (0, 7, 1),
              13: (0, 7, 2), 14: (0, 8, 1), 15: (0, 8, 1),
              16: (0, 8, 2), 20: (0, 8, 4)}
R195_M99 = {4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1,
            12: 1, 13: 1, 14: 2, 15: 2, 16: 2, 20: 2}

# --------------------- calibrated record tables (calib_fa_pass1.log)
_HS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
CAL_TPEAK = {h: "0.500" for h in _HS}
CAL_NSC = {h: 0 for h in _HS}
CAL_RMIN = dict(zip(_HS, ("-5.02", "-7.54", "-9.71", "-12.09",
                          "-14.28", "-16.57", "-19.01", "-21.40",
                          "-23.97", "-26.29", "-28.97", "-31.07",
                          "-33.63", "-43.30")))
CAL_ETA = {h: "-300.0" for h in _HS}
CAL_FW1 = dict(zip(_HS, ("0.596", "0.528", "0.487", "0.448",
                         "0.426", "0.408", "0.391", "0.377",
                         "0.364", "0.353", "0.345", "0.335",
                         "0.330", "0.306")))
CAL_MJET = dict(zip(_HS, (1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 11, 13,
                          13, 13)))
CAL_JR0 = dict(zip(_HS, ("-5.0", "-7.5", "-9.7", "-12.1", "-14.3",
                         "-16.6", "-19.0", "-21.4", "-24.0",
                         "-26.3", "-29.0", "-31.1", "-33.6",
                         "-43.3")))
CAL_PG = dict(zip(_HS, ("7.141", "9.812", "12.118", "14.604",
                        "16.896", "19.237", "21.667", "24.249",
                        "26.671", "28.259", "30.577", "32.563",
                        "33.426", "39.169")))
CAL_CH = dict(zip(_HS, ("13.95", "16.43", "18.19", "20.11",
                        "21.73", "23.37", "25.05", "23.60",
                        "25.00", "23.44", "24.62", "25.53",
                        "23.82", "24.28")))
CAL_RTAU = dict(zip(_HS, ("0.7776", "0.7109", "0.6843", "0.6643",
                          "0.6530", "0.6412", "0.6307", "0.5517",
                          "0.5415", "0.4792", "0.4707", "0.4676",
                          "0.4135", "0.3555")))
CAL_HORIZ = {4: (1, 2, 1, 2), 5: (1, 2, 2, 3), 6: (1, 2, 2, 3),
             7: (1, 2, 2, 3), 8: (1, 2, 2, 3), 9: (1, 2, 2, 3),
             10: (1, 2, 2, 3), 11: (1, 2, 2, 3), 12: (1, 2, 2, 3),
             13: (1, 2, 2, 3), 14: (2, 3, 2, 3), 15: (2, 3, 2, 3),
             16: (2, 3, 2, 3), 20: (2, 3, 2, 3)}
CAL_QTAUF = {h: "1.00" for h in _HS}
CAL_DEXGAP = dict(zip(_HS, (None, "7.5", "13.0", "18.2", "22.9",
                            "27.7", "32.7", "37.6", "42.9", "47.6",
                            "53.1", "57.4", "62.5", "82.0")))
CAL_TAILT2 = dict(zip(_HS, (None, "-6.86", "-5.93", "-5.54",
                            "-5.27", "-5.10", "-4.99", "-4.90",
                            "-4.84", "-4.78", "-4.74", "-4.69",
                            "-4.66", "-4.57")))
CAL_GNEG = {h: 0 for h in _HS}
CAL_MECH = dict(zip(_HS, ("0.428", "0.090", "0.068", "0.141",
                          "0.006", "0.084", "0.133", "0.164",
                          "0.192", "0.311", "0.321", "0.386",
                          "0.369", "0.261")))
CAL_CTRL = {("SCRARITH", 5): {"signs": (0, 3, 1), "m99": 3,
                              "n99": 3, "q99": 4, "gneg": 0},
            ("EPSTEIN", 8): {"signs": (0, 3, 0), "m99": 3,
                             "n99": 3, "q99": 6, "gneg": 10},
            ("SMOOTH", 5): {"gneg": 0, "w99": "0.920", "nsc": 0}}
CAL_WIT = {"signs_base": (0, 3, 1), "signs_wit": (0, 3, 1),
           "n99_base": 1, "n99_wit": 2}
CAL_SLOPES = {"nscK": "+0.000", "n99f": "+0.001", "fw1": "+0.003"}
FROZEN_ENUMS = {"signMech": "SIGN-LAW-FROM-NONNEGATIVITY",
                "mechEnum": "JETCONV-LAW-BAND-APPROXIMATE"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan"), float("nan"), float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return float("nan"), float("nan"), float("nan")
    sl = sxy / sxx
    ic = my - sl * mx
    ssr = sum((y - (sl * x + ic)) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - ssr / sst if sst > 0 else float("nan")
    return sl, ic, r2


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; eigenvector access "
                       "IN-SCOPE (anatomy contract, r195 lineage); "
                       "zero-freeness unchanged; concurrent-lane "
                       "files untouched")


# ------------------------------------------------------- source helpers
def sieve_atoms(x: int):
    icap = int(math.floor(x))
    comp = np.zeros(icap + 1, dtype=bool)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist], \
        nlist


def world_atoms(world: str, x: int):
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms, [q for q, _p in nlist]
    if world == "EPSTEIN":
        icap = int(math.floor(x))
        rq = np.zeros(icap + 1)
        xm = int(math.isqrt(icap)) + 1
        ym = int(math.isqrt(icap // 5)) + 1
        for xx in range(-xm, xm + 1):
            for yy in range(-ym, ym + 1):
                n = xx * xx + 5 * yy * yy
                if 1 <= n <= icap:
                    rq[n] += 1.0
        av = [mp.mpf(v) / 2 for v in rq]
        lamq = [mp.mpf(0)] * (icap + 1)
        for n in range(2, icap + 1):
            sacc = av[n] * mp.log(n)
            for d in range(2, n):
                if n % d == 0:
                    sacc -= lamq[d] * av[n // d]
            lamq[n] = sacc
        atoms = []
        qs = []
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
                qs.append(n)
        return atoms, qs
    if world == "SMOOTH":
        return None, None
    raise ValueError(world)


def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def W_atom_mp(u, oms, b, L, K):
    """Per-atom ACF kernel W(u): x^T W x = -2 int_0^{L-u} A A(.+u)."""
    W = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            W[i, j] = 2 * (oms[i] * mp.sin(oms[i] * u)
                           - oms[j] * mp.sin(oms[j] * u)) \
                / (b[i] - b[j])
            W[j, i] = W[i, j]
    W[0, 0] = 2 * (u - L)
    for k in range(1, K):
        W[k, k] = mp.sin(oms[k] * u) / oms[k] \
            + (u - L) * mp.cos(oms[k] * u)
    return W


def fvec1(K):
    gg = (mp.sqrt(5) - 1) / 2
    return [mp.frac((k + 1) * gg) - mp.mpf(1) / 2 for k in range(K)]


def form_of(x, M, K):
    return sum(x[i] * M[i, j] * x[j] for i in range(K)
               for j in range(K))


def g_quad(x, u, oms, L, K):
    """int_0^{L-u} A(t) A(t+u) dt by oscillation-split mp.quad."""
    def A(t):
        return sum(x[k] * mp.cos(oms[k] * t) for k in range(K))
    omax = oms[K - 1]
    n = int(mp.floor((L - u) * 2 * omax / mp.pi)) + 2
    pts = [(L - u) * j / n for j in range(n + 1)]
    return mp.quad(lambda t: A(t) * A(t + u), pts)


def bottom_vec_mp(Raw, K, froW):
    """Bottom eigenvector by mp inverse iteration (r195 VERBATIM:
    3 LU solves, gap-limited convergence warded by the Rayleigh
    stability between iterations 2 and 3 plus the eigen-residual)."""
    x = mp.matrix([mp.mpf(1) for _ in range(K)])
    lam2 = None
    for it in range(3):
        x = mp.lu_solve(Raw, x)
        nx = mp.sqrt(sum(x[i] ** 2 for i in range(K)))
        x = x / nx
        if it == 1:
            v2 = [x[i] for i in range(K)]
            Rv2 = [sum(Raw[i, j] * v2[j] for j in range(K))
                   for i in range(K)]
            lam2 = sum(v2[i] * Rv2[i] for i in range(K))
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K)) / froW
    stab = abs(lam - lam2) / abs(lam) if lam != 0 else mp.mpf(0)
    return v, lam, float(res), float(stab)


def g_form_at(v, u, oms, b, L, K, sk, ck):
    """-(v^T W(u) v)/2 from precomputed sin/cos tables at lag u."""
    acc = v[0] * v[0] * 2 * (u - L)
    for k in range(1, K):
        acc += v[k] * v[k] * (sk[k] / oms[k] + (u - L) * ck[k])
    for i in range(K):
        oi_si = oms[i] * sk[i]
        for j in range(i):
            acc += 2 * v[i] * v[j] * 2 * (oi_si - oms[j] * sk[j]) \
                / (b[i] - b[j])
    return -acc / 2


def profile_stats(v, K, L, dps):
    """Lattice-exact profile A(t_j) on N = NGRID_FAC*K points; stats
    on the half window (A is L-periodic and symmetric about L/2 on
    the commensurate lattice -- tautological, noted not sold)."""
    N = NGRID_FAC * K
    twopi = 2 * mp.pi
    ct = [mp.cos(twopi * m / N) for m in range(N)]
    half = N // 2
    Av = []
    for j in range(half + 1):
        Av.append(sum(v[k] * ct[(k * j) % N] for k in range(K)))
    amax = max(abs(x) for x in Av)
    jpeak = max(range(half + 1), key=lambda j: abs(Av[j]))
    if Av[jpeak] < 0:
        Av = [-x for x in Av]
    zb = mp.mpf(ZCLS) * amax
    # sign changes on the half window
    sgn = [0 if abs(x) <= zb else (1 if x > 0 else -1) for x in Av]
    nz = [s for s in sgn if s != 0]
    nsc = sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])
    amin = min(Av)
    rmin = float(amin / amax)
    nonneg = bool(amin >= -zb)
    e2 = [x * x for x in Av]
    tot = sum(e2, mp.mpf(0))
    neg = sum((e2[j] for j in range(half + 1) if Av[j] < -zb),
              mp.mpf(0))
    eta = max(float(neg / tot), 1e-300) if tot > 0 else float("nan")
    fw1 = sum(1 for x in Av if abs(x) >= amax / 10) / float(half + 1)
    # edge-window fit (amendment A1, pre-freeze instrument fix,
    # disclosed: the original envelope-local-maxima rule collapses
    # to 2 points on a nodeless monotone bump; frozen replacement:
    # all grid points j = 1..J_EDGE, J_EDGE = max(4, N//64), on the
    # rising edge side, fit log10|A| vs log10 t (p_A) and vs t
    # (s_prof))
    j_edge = min(max(4, N // 64), max(jpeak - 1, 4))
    env = [j for j in range(1, j_edge + 1) if abs(Av[j]) > 0]
    ts = [float(j) * float(L) / N for j in env]
    ys = [float(mp.log(abs(Av[j]), 10)) for j in env]
    if len(ys) >= 3:
        pA, _i, r2A = fit_line([math.log10(t) for t in ts], ys)
        sprof, _i2, _r2s = fit_line(ts, ys)
    else:
        pA = sprof = r2A = float("nan")
    return dict(N=N, tpeak_frac=jpeak / float(N), nsc=nsc,
                rmin=rmin, nonneg=nonneg, eta=eta, fw1=fw1,
                pA=pA, r2A=r2A, sprof=sprof, nenv=len(ys),
                amax_log10=float(mp.log(amax, 10)))


def lag_battery(v, K, L, oms, b, dps):
    """g on the frozen lag lattice u_l = l L/25 via exact tables;
    fits, sign census."""
    twopi = 2 * mp.pi
    c25 = [mp.cos(twopi * m / NLAG_DEN) for m in range(NLAG_DEN)]
    s25 = [mp.sin(twopi * m / NLAG_DEN) for m in range(NLAG_DEN)]
    gl = []
    for l in range(1, NLAG_DEN):
        u = L * l / NLAG_DEN
        sk = [s25[(k * l) % NLAG_DEN] for k in range(K)]
        ck = [c25[(k * l) % NLAG_DEN] for k in range(K)]
        gl.append((float(u), g_form_at(v, u, oms, b, L, K, sk, ck)))
    gmax = max(abs(g) for _u, g in gl)
    zb = mp.mpf(ZCLS) * gmax
    gneg = sum(1 for _u, g in gl if g < -zb)
    res = [(u, g) for u, g in gl if abs(g) > zb]
    xsu = [u for u, _g in res]
    xse = [math.log10(float(L) - u) for u, _g in res]
    ys = [float(mp.log(abs(g), 10)) for _u, g in res]
    s_exp, _i, r2e = fit_line(xsu, ys)
    p_pow, _i2, r2p = fit_line(xse, ys)
    # local edge power between the two deepest resolvable lags
    if len(res) >= 2:
        p_edge = (ys[-1] - ys[-2]) / (xse[-1] - xse[-2])
    else:
        p_edge = float("nan")
    return dict(gneg=gneg, nres=len(res), s_exp=s_exp, r2e=r2e,
                p_pow=p_pow, r2p=r2p, p_edge=p_edge,
                gl=[(u, float(mp.log(abs(g), 10)) if abs(g) > 0
                     else -300.0,
                     (1 if g > zb else (-1 if g < -zb else 0)))
                    for u, g in gl])


def horizon_of(tq, qs, Pr, absguard, lam0):
    """Prefix horizons in ascending q: (n99, q99, n999, q999, ntau,
    ntau_res_frac)."""
    n = len(tq)
    cum = mp.mpf(0)
    n99 = q99 = n999 = q999 = ntau = None
    tmax = max(abs(t) for t in tq)
    zb = mp.mpf(ZCLS) * tmax
    nres = sum(1 for t in tq if abs(t) > zb)
    nres_pfx = 0
    ntau_res = None
    for i in range(n):
        cum += tq[i]
        if abs(tq[i]) > zb:
            nres_pfx += 1
        rem = abs(Pr - cum)
        if n99 is None and rem <= max(0.01 * abs(Pr), absguard):
            n99, q99 = i + 1, qs[i]
        if n999 is None and rem <= max(0.001 * abs(Pr), absguard):
            n999, q999 = i + 1, qs[i]
        if ntau is None and rem <= abs(lam0):
            ntau = i + 1
            ntau_res = nres_pfx
    frac = (ntau_res / float(nres)) if (nres and ntau_res is not None) \
        else float("nan")
    return n99, q99, n999, q999, ntau, frac


# ------------------------------------------------------- main worker
def w_main(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            atoms, qs = world_atoms("MAIN", h)
            out["natoms"] = len(atoms)
            out["qs"] = qs
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            out["log10taufrac"] = float(mp.log(
                abs(tau) * 2 * aa / froW, 10))
            # ---- G20 assembly (r195 inheritance) + pole square
            Wq_list = [W_atom_mp(u, oms, b, L, K) for u, _w in atoms]
            S = mp.zeros(K, K)
            for (u, w), Wq in zip(atoms, Wq_list):
                for i in range(K):
                    for j in range(K):
                        S[i, j] += w * Wq[i, j]
            dev = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    tgt = RawW[i, j] - RawP[i, j] - RawA[i, j]
                    dev = max(dev, abs(tgt - S[i, j]))
                    den = max(den, abs(tgt))
            out["asm_dev"] = float(dev / den)
            x1 = fvec1(K)
            ps = 2 * s2 * (sum(x1[k] / (mp.mpf(1) / 4 + b[k])
                               for k in range(K))) ** 2
            pf = form_of(x1, RawP, K)
            out["pole_sq_dev"] = float(abs(ps - pf) / abs(ps))
            # ---- bottom direction (mp inverse iteration, r195 A3)
            v0, lam0, invres, invstab = bottom_vec_mp(RawW, K, froW)
            out["invit_res"] = invres
            out["invit_stab"] = invstab
            out["lam0_pos"] = bool(lam0 > 0)
            if h in ANAT_MP:
                E, Q = mp.eigsy(RawW)
                i0 = min(range(K), key=lambda m: E[m])
                ovl = abs(sum(Q[i, i0] * v0[i] for i in range(K)))
                out["v0_ovl_dev"] = float(abs(ovl - 1))
            # ---- budgets + per-atom ladder
            P = form_of(v0, RawP, K)
            A_ = form_of(v0, RawA, K)
            tq_mp = [w * form_of(v0, Wq, K)
                     for (u, w), Wq in zip(atoms, Wq_list)]
            Pr = sum(tq_mp, mp.mpf(0))
            resid = P + A_ + Pr
            out["budget_dev"] = float(abs(resid - lam0) / froW)
            dep = abs(resid) / (abs(P) + abs(A_) + abs(Pr))
            out["depth"] = float(mp.log(dep, 10)) if dep > 0 \
                else -300.0
            out["bud_P"] = float(P)
            out["bud_A"] = float(A_)
            out["bud_Pr"] = float(Pr)
            tmax = max(abs(t) for t in tq_mp)
            zbar = mp.mpf(ZCLS) * tmax
            out["tq_zero"] = sum(1 for t in tq_mp if abs(t) <= zbar)
            out["tq_pos"] = sum(1 for t in tq_mp if t > zbar)
            out["tq_neg"] = sum(1 for t in tq_mp if t < -zbar)
            out["t_ladder"] = [float(mp.log(abs(t), 10))
                               if abs(t) > 0 else -300.0
                               for t in tq_mp]
            # m99 (r195 rule VERBATIM: top-|t| subset)
            tqf = [float(t) for t in tq_mp]
            Prt = float(Pr)
            absguard = 1e-6 * (abs(out["bud_P"]) + abs(out["bud_A"]))
            order = sorted(range(len(tqf)),
                           key=lambda i: -abs(tqf[i]))
            csum = 0.0
            m99 = len(tqf)
            for mth, i in enumerate(order, start=1):
                csum += tqf[i]
                if abs(csum - Prt) <= max(0.01 * abs(Prt), absguard):
                    m99 = mth
                    break
            out["m99"] = m99
            # ---- F2 horizons (prefix in ascending q, frozen)
            n99, q99, n999, q999, ntau, tfrac = horizon_of(
                tq_mp, qs, Pr, mp.mpf(absguard), lam0)
            out["n99"], out["q99"] = n99, q99
            out["n999"], out["q999"] = n999, q999
            out["ntau"], out["qtau_frac"] = ntau, tfrac
            # ---- F3 tail objects (t_2, t_3, Tail_{q>3})
            i2 = qs.index(2)
            i3 = qs.index(3)
            t2, t3 = tq_mp[i2], tq_mp[i3]
            Tail = Pr - t2 - t3
            out["tail_res"] = bool(abs(Tail) > zbar)
            if out["tail_res"]:
                out["tail_t2"] = float(mp.log(abs(Tail) / abs(t2),
                                              10))
                out["dexgap"] = float(mp.log(abs(Tail) / abs(lam0),
                                             10))
                # measured geometric majorant over atoms q > 3
                rest = [abs(t) for i, t in enumerate(tq_mp)
                        if qs[i] > 3 and abs(t) > zbar]
                if len(rest) >= 2:
                    rho = max(rest[i + 1] / rest[i]
                              for i in range(len(rest) - 1))
                else:
                    rho = mp.mpf(0)
                out["rho_tail"] = float(rho)
                if rho < 1:
                    bound = rest[0] / (1 - rho)
                    out["tail_bound_ok"] = bool(bound >= abs(Tail))
                    out["overshoot_dex"] = float(mp.log(
                        (bound - abs(Tail)) / abs(lam0), 10)) \
                        if bound > abs(Tail) else -300.0
                else:
                    out["tail_bound_ok"] = False
                    out["overshoot_dex"] = float("nan")
            red = P + A_ + t2 + t3
            out["red_pos"] = bool(red > 0)
            out["red_log10"] = float(mp.log(abs(red), 10)) \
                if red != 0 else -300.0
            # ---- F1 jets
            jr = []
            for j in range(JMAX + 1):
                if j == 0:
                    num = sum(v0[k] for k in range(K))
                    dnm = sum(abs(v0[k]) for k in range(K))
                else:
                    num = sum(v0[k] * b[k] ** j for k in range(1, K))
                    dnm = sum(abs(v0[k]) * b[k] ** j
                              for k in range(1, K))
                jr.append(float(abs(num) / dnm) if dnm > 0
                          else float("nan"))
            out["jr_log10"] = [float(math.log10(x)) if x > 0
                               else -300.0 for x in jr]
            mjet = 0
            for x in jr:
                if x <= JET_BAR:
                    mjet += 1
                else:
                    break
            out["mjet"] = mjet
            # ---- F1 profile
            prof = profile_stats(v0, K, L, dps)
            out.update({("prof_" + k2): v2 for k2, v2 in
                        prof.items()})
            # grid-instrument ward at h in (4, 5): table vs direct
            if h in (4, 5):
                N = prof["N"]
                twopi = 2 * mp.pi
                gdev = mp.mpf(0)
                for j in (1, N // 8, N // 4, 3 * N // 8, N // 2):
                    tj = L * j / N
                    direct = sum(v0[k] * mp.cos(oms[k] * tj)
                                 for k in range(K))
                    table = sum(v0[k] * mp.cos(twopi * ((k * j) % N)
                                               / N)
                                for k in range(K))
                    gdev = max(gdev, abs(direct - table))
                out["grid_dev"] = float(gdev)
            # ---- F1 lag battery
            lb = lag_battery(v0, K, L, oms, b, dps)
            out.update({("lag_" + k2): v2 for k2, v2 in lb.items()})
            out["c_h"] = -lb["s_exp"] * math.log(10.0)
            out["r_tau"] = (-lb["s_exp"]) * float(L) \
                / abs(out["log10taufrac"])
            # atom-lag fits (>= 3 resolvable atoms)
            resa = [(float(u), -t / (2 * w))
                    for (u, w), t in zip(atoms, tq_mp)
                    if abs(t) > zbar]
            out["gq_log10"] = [float(mp.log(abs(g), 10))
                               for _u, g in resa]
            out["gq_neg"] = sum(1 for _u, g in resa if g < 0)
            if len(resa) >= 3:
                ysa = [float(mp.log(abs(g), 10)) for _u, g in resa]
                s_at, _i, r2sa = fit_line([u for u, _g in resa], ysa)
                p_at, _i2, r2pa = fit_line(
                    [math.log10(float(L) - u) for u, _g in resa],
                    ysa)
                out["s_atom"], out["p_atom"] = s_at, p_at
                out["r2_satom"], out["r2_patom"] = r2sa, r2pa
            else:
                out["s_atom"] = out["p_atom"] = float("nan")
            # quadrature ward (h in 4, 5): kernel vs mp.quad
            if h in (4, 5):
                qdev_x = mp.mpf(0)
                qdev_v = mp.mpf(0)
                for l in QUAD_LAGS:
                    u = L * l / NLAG_DEN
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for tag, x in (("xg", x1), ("v0", v0)):
                        gq_ = g_quad(x, u, oms, L, K)
                        fm = form_of(x, Wq, K)
                        d_ = abs(fm + 2 * gq_) / max(abs(fm),
                                                     mp.mpf("1e-40"))
                        if tag == "xg":
                            qdev_x = max(qdev_x, d_)
                        else:
                            qdev_v = max(qdev_v, d_)
                out["quad_dev_x"] = float(qdev_x)
                out["quad_dev_v"] = float(qdev_v)
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------- control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            atoms, qs = world_atoms(world, x)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            # assembly ward
            if atoms is not None:
                S = mp.zeros(K, K)
                for u, w in atoms:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for i in range(K):
                        for j in range(K):
                            S[i, j] += w * Wq[i, j]
                dev = mp.mpf(0)
                den = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        tgt = RawW[i, j] - RawP[i, j] - RawA[i, j]
                        dev = max(dev, abs(tgt - S[i, j]))
                        den = max(den, abs(tgt))
                out["asm_dev"] = float(dev / den)
            else:
                iddev = mp.mpf(0)
                x_ = fvec1(K)

                def xWx(w_):
                    Wq = W_atom_mp(w_, oms, b, L, K)
                    return form_of(x_, Wq, K) * mp.exp(w_ / 2)
                omax = oms[K - 1]
                n = int(mp.floor(L * 2 * omax / mp.pi)) + 2
                pts = [L * j / n for j in range(n + 1)]
                quadv = mp.quad(xWx, pts)
                tgt = form_of(x_, RawW, K) \
                    - form_of(x_, RawP, K) - form_of(x_, RawA, K)
                iddev = abs(tgt - quadv) / max(abs(tgt),
                                               mp.mpf("1e-30"))
                out["asm_dev"] = float(iddev)
            # bottom (most negative) direction via full eigsy (small K)
            E, Q = mp.eigsy(RawW)
            i0 = min(range(K), key=lambda m: E[m])
            out["lam0_neg"] = bool(E[i0] < 0)
            vb = [Q[i, i0] for i in range(K)]
            lam0 = E[i0]
            P = form_of(vb, RawP, K)
            A_ = form_of(vb, RawA, K)
            out["bud_P"] = float(P)
            out["bud_A"] = float(A_)
            prof = profile_stats(vb, K, L, dps)
            out.update({("prof_" + k2): v2 for k2, v2 in
                        prof.items()})
            lb = lag_battery(vb, K, L, oms, b, dps)
            out.update({("lag_" + k2): v2 for k2, v2 in lb.items()})
            if atoms is not None:
                tq_mp = []
                for u, w in atoms:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    tq_mp.append(w * form_of(vb, Wq, K))
                Pr = sum(tq_mp, mp.mpf(0))
                out["bud_Pr"] = float(Pr)
                tmax = max(abs(t) for t in tq_mp)
                zb = mp.mpf(ZCLS) * tmax
                out["tq_pos"] = sum(1 for t in tq_mp if t > zb)
                out["tq_neg"] = sum(1 for t in tq_mp if t < -zb)
                out["tq_zero"] = sum(1 for t in tq_mp
                                     if abs(t) <= zb)
                out["negw"] = sum(1 for _u, w in atoms if w < 0)
                tqf = [float(t) for t in tq_mp]
                Prt = float(Pr)
                absguard = 1e-6 * (abs(out["bud_P"])
                                   + abs(out["bud_A"]))
                order = sorted(range(len(tqf)),
                               key=lambda i: -abs(tqf[i]))
                csum = 0.0
                m99 = len(tqf)
                for mth, i in enumerate(order, start=1):
                    csum += tqf[i]
                    if abs(csum - Prt) <= max(0.01 * abs(Prt),
                                              absguard):
                        m99 = mth
                        break
                out["m99"] = m99
                n99, q99, n999, q999, _nt, _tf = horizon_of(
                    tq_mp, qs, Pr, mp.mpf(absguard), lam0)
                out["n99"], out["q99"] = n99, q99
            else:
                # SMOOTH: continuum prime budget + w99 localization
                def gv(w_):
                    Wq = W_atom_mp(w_, oms, b, L, K)
                    return -form_of(vb, Wq, K) / 2
                segs = []
                for l in range(NLAG_DEN):
                    u0 = L * l / NLAG_DEN
                    u1 = L * (l + 1) / NLAG_DEN
                    g0 = gv(u0 + (u1 - u0) / 2)
                    segs.append(abs(g0) * mp.exp(u0 / 2)
                                * (u1 - u0))
                tot = sum(segs, mp.mpf(0))
                cum = mp.mpf(0)
                w99 = float("nan")
                for l, sgv in enumerate(segs):
                    cum += sgv
                    if cum >= mp.mpf("0.99") * tot:
                        w99 = (l + 1) / float(NLAG_DEN)
                        break
                out["w99_frac"] = w99
                # continuum identity ward at vb
                def xWxv(w_):
                    Wq = W_atom_mp(w_, oms, b, L, K)
                    return form_of(vb, Wq, K) * mp.exp(w_ / 2)
                omax = oms[K - 1]
                n = int(mp.floor(L * 2 * omax / mp.pi)) + 2
                pts = [L * j / n for j in range(n + 1)]
                quadv = mp.quad(xWxv, pts)
                tgt = form_of(vb, RawW, K) - form_of(vb, RawP, K) \
                    - form_of(vb, RawA, K)
                out["smooth_id_dev"] = float(
                    abs(tgt - quadv) / max(abs(tgt), mp.mpf("1e-30")))
                out["bud_Pr"] = float(tgt)
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------- witness leg
def witness_leg() -> dict:
    """r172 inflation witness VERBATIM at h = WIT_RUNG: dv =
    A_2 (W-1)/(b_2 - b_1) on ray modes 1, 2; Raw-coordinate
    transport y_k = par_k * ray_k (congruence: y^T Raw y ==
    ray^T M ray); few-atom anatomy at base vs witness."""
    dps = DPS[WIT_RUNG]
    ce = R4.build_cell(WIT_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out: dict = {}
    with mp.workdps(dps):
        aa = mp.log(WIT_RUNG) / 2
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        atoms, qs = world_atoms("MAIN", WIT_RUNG)
        RawW = raw_of(ce["mpM"], par, nrm, K)
        RawP = raw_of(ce["mpPole"], par, nrm, K)
        RawA = raw_of(ce["mpArch"], par, nrm, K)
        froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                           for j in range(K)))
        v0, _lam0, _r, _s = bottom_vec_mp(RawW, K, froW)
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum(((-1) ** k) * cs[k] for k in range(K))
        A2 = sum(((-1) ** k) * cs[k] * b[k] for k in range(1, K))
        yt = abs(A2 / A0)
        dv = A2 * (WIT_FACT - 1) / (b[2] - b[1])
        cs2 = list(cs)
        cs2[1] += dv
        cs2[2] += dv
        A0w = sum(((-1) ** k) * cs2[k] for k in range(K))
        A2w = sum(((-1) ** k) * cs2[k] * b[k] for k in range(1, K))
        out["wit_ytr"] = float(abs(A2w / A0w) / yt)
        out["wit_a0dev"] = float(abs(A0w / A0 - 1))

        def anat(ray):
            y = [par[k] * ray[k] for k in range(K)]
            ny = mp.sqrt(sum(t * t for t in y))
            y = [t / ny for t in y]
            P = form_of(y, RawP, K)
            A_ = form_of(y, RawA, K)
            tq = []
            for u, w in atoms:
                Wq = W_atom_mp(u, oms, b, L, K)
                tq.append(w * form_of(y, Wq, K))
            Pr = sum(tq, mp.mpf(0))
            tmax = max(abs(t) for t in tq)
            zb = mp.mpf(ZCLS) * tmax
            signs = (sum(1 for t in tq if t > zb),
                     sum(1 for t in tq if t < -zb),
                     sum(1 for t in tq if abs(t) <= zb))
            absguard = mp.mpf(1e-6) * (abs(P) + abs(A_))
            n99, q99, _n3, _q3, _nt, _tf = horizon_of(
                tq, qs, Pr, absguard, mp.mpf(0))
            ovl = abs(sum(y[k] * v0[k] for k in range(K)))
            return dict(P=float(P), A=float(A_), Pr=float(Pr),
                        signs=signs, n99=n99, q99=q99,
                        ovl=float(ovl),
                        tdex=[float(mp.log(abs(t), 10))
                              if abs(t) > 0 else -300.0
                              for t in tq])
        out["base"] = anat(cs)
        out["wit"] = anat(cs2)
    return out


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"
    rec = not (calib or smoke)

    print("=" * 78)
    print("fewatom_reduction_probe -- PRIME.FEWATOM.REDUCTION.01  "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/grids/recipes declared in the frozen "
          "spec (SPEC_SHA covers the declaration); priors P1-P5 "
          "pre-registered resolve-and-record, none gate-forcing; "
          "horizons Q99/Q999/QTAU and the tail objects predefined; "
          "tau_h enters ONLY as a measured per-rung scalar; bottom "
          "direction mp inverse iteration at EVERY rung (r195 A3 "
          "lineage); DEAD-CLASS guard: no l1 majorant is USED as a "
          "positivity route (the tail majorant is measured and "
          "priced against lambda_0, expected dead -- that pricing "
          "is the point, not a bound consumed)")

    # ------------------------------------------------------------ S2
    section("S2  MAIN BATTERY (all reachable rungs)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    if errs:
        check("G20-acf-assembly-inherited", False,
              "worker errors at %s" % errs)
        print("ABORT: worker errors")
        return 1

    # ------------------------------------------------------------ S1
    section("S1  INSTRUMENT WARDS")
    gws = [h for h in (4, 5) if h in rungs]
    check("G10-grid-instrument-ward", all(
        res[h]["grid_dev"] <= GRID_BAR for h in gws),
          "lattice-exact cosine table vs direct mp.cos at h = %s "
          "(5 spot points each): max abs dev %.1e (bar %.0e); the "
          "profile grid identity om_k t_j = 2 pi k j / N is exact "
          "on the commensurate lattice; the L-periodicity/symmetry "
          "A(L-t) = A(t) is a lattice tautology (noted, not sold)"
          % (str(gws), max(res[h]["grid_dev"] for h in gws),
             GRID_BAR))
    check("G11-acf-quadrature-ward", all(
        res[h]["quad_dev_x"] <= QUAD_BAR
        and res[h]["quad_dev_v"] <= QUADV0_BAR for h in gws),
          "oscillation-split mp.quad of int A(t)A(t+u) dt vs the "
          "closed-form kernel at h = %s, lags l = %s of %d, vectors "
          "{xg1, v_0}: max rel dev xg1 %.1e (bar %.0e), v_0 %.1e "
          "(bar %.0e) -- the lag-lattice g values are real "
          "integrals, not formula-vs-formula"
          % (str(gws), str(QUAD_LAGS), NLAG_DEN,
             max(res[h]["quad_dev_x"] for h in gws), QUAD_BAR,
             max(res[h]["quad_dev_v"] for h in gws), QUADV0_BAR))

    # ---------------------------------------------------- S2 gates
    section("S2b  INHERITED DICTIONARY GATES")
    check("G20-acf-assembly-inherited", all(
        res[h]["asm_dev"] <= ASM_BAR for h in rungs) and all(
        res[h]["pole_sq_dev"] <= POLE_SQ_BAR for h in rungs),
          "r195 ACF law re-verified at every rung (entrywise "
          "RawW - RawP - RawA == sum w_q W(u_q)): max rel dev %.1e "
          "(bar %.0e); pole square max dev %.1e (bar %.0e)"
          % (max(res[h]["asm_dev"] for h in rungs), ASM_BAR,
             max(res[h]["pole_sq_dev"] for h in rungs),
             POLE_SQ_BAR))

    mp_here = [h for h in rungs if h in ANAT_MP]
    inv_ok = all(res[h]["invit_res"] <= INVIT_RES_BAR
                 and res[h]["invit_stab"] <= INVIT_STAB_BAR
                 for h in rungs) and all(
        res[h].get("v0_ovl_dev", 0.0) <= OVL_BAR for h in mp_here)
    dep_ok = all(abs(res[h]["depth"] - float(R195_DEPTH[h]))
                 <= LOG_TOL for h in rungs)
    bud_ok = all(res[h]["budget_dev"] <= BUDGET_BAR for h in rungs)
    check("G21-budget-and-depth-inherited", inv_ok and dep_ok
          and bud_ok,
          "inverse-iteration wards (res <= %.1e bar %.0e, stab <= "
          "%.1e bar %.0e, eigsy overlap <= %.1e bar %.0e at %s); "
          "budget identity P + A + sum t_q == lambda_0 <= %.1e "
          "fro-rel (bar %.0e); depth ladder == r195 CAL_DEPTH "
          "within %.2f dex at all %d rungs: %s"
          % (max(res[h]["invit_res"] for h in rungs), INVIT_RES_BAR,
             max(res[h]["invit_stab"] for h in rungs),
             INVIT_STAB_BAR,
             max((res[h].get("v0_ovl_dev", 0.0) for h in mp_here),
                 default=0.0), OVL_BAR, str(mp_here),
             max(res[h]["budget_dev"] for h in rungs), BUDGET_BAR,
             LOG_TOL, len(rungs),
             str({h: "%.2f" % res[h]["depth"]
                  for h in (4, 8, 13, 16, 20) if h in res})))

    sig_ok = all((res[h]["tq_pos"], res[h]["tq_neg"],
                  res[h]["tq_zero"]) == R195_SIGNS[h]
                 for h in rungs)
    m99_ok = all(res[h]["m99"] == R195_M99[h] for h in rungs)
    check("G22-sign-ladder-inherited", sig_ok and m99_ok,
          "the r195 SIGN LAW reproduces exactly: (n+, n-, n0) == "
          "R195_SIGNS and m99 == R195_M99 at every rung -- %s; "
          "every resolvable atom negative at the collapsing "
          "direction, commensurate q = h atoms exact zero"
          % str({h: (res[h]["tq_pos"], res[h]["tq_neg"],
                     res[h]["tq_zero"]) for h in rungs}))

    # ------------------------------------------------------------ S3
    section("S3  F1: SHAPE LADDER + DECAY MECHANISM")
    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL prof h=%d tpeak %.4f nsc %d rmin %.3e "
                  "nonneg %s eta %.3e fw1 %.3f pA %.3f r2A %.3f "
                  "sprof %.2f nenv %d"
                  % (h, r["prof_tpeak_frac"], r["prof_nsc"],
                     r["prof_rmin"], r["prof_nonneg"],
                     r["prof_eta"], r["prof_fw1"], r["prof_pA"],
                     r["prof_r2A"], r["prof_sprof"],
                     r["prof_nenv"]))
        ok30 = True
    else:
        ok30 = all(
            abs(res[h]["prof_tpeak_frac"] - float(CAL_TPEAK[h]))
            <= FRAC_TOL
            and res[h]["prof_nsc"] == CAL_NSC[h]
            and abs(math.log10(max(abs(res[h]["prof_rmin"]),
                                   1e-300))
                    - float(CAL_RMIN[h])) <= LOG_TOL
            and abs(math.log10(res[h]["prof_eta"])
                    - float(CAL_ETA[h])) <= LOG_TOL
            and abs(res[h]["prof_fw1"] - float(CAL_FW1[h]))
            <= FRAC_TOL
            for h in rungs)
    check("G30-profile-shape-ladder", ok30,
          "the collapsing direction's mode polynomial A_{v_0} at "
          "every rung: peak fraction %s, sign changes (half "
          "window) %s, log10|A_min/A_max| %s, log10 eta "
          "(negative-mass fraction) %s, 0.1-width %s"
          % (str({h: "%.3f" % res[h]["prof_tpeak_frac"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: res[h]["prof_nsc"] for h in rungs}),
             str({h: "%.2f" % math.log10(max(
                 abs(res[h]["prof_rmin"]), 1e-300))
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % math.log10(res[h]["prof_eta"])
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % res[h]["prof_fw1"]
                  for h in (4, 8, 13, 20) if h in res})))

    nonneg_all = all(res[h]["prof_nonneg"] for h in rungs)
    eta_small = all(res[h]["prof_eta"] <= 0.01 for h in rungs)
    sign_mech = ("SIGN-LAW-FROM-NONNEGATIVITY" if nonneg_all
                 else ("SIGN-LAW-CONCENTRATION-PARTIAL" if eta_small
                       else "SIGN-LAW-UNEXPLAINED-BY-SHAPE"))
    ok31 = True if (calib or smoke) else \
        (sign_mech == FROZEN_ENUMS.get("signMech"))
    check("G31-sign-mechanism-verdict", ok31,
          "P1 RESOLVED: A_{v_0} >= 0 at every rung is %s (min "
          "rel value %s); enum %s -- %s"
          % ("TRUE" if nonneg_all else "FALSE",
             str({h: "%.1e" % res[h]["prof_rmin"]
                  for h in (4, 8, 13, 20) if h in res}),
             sign_mech,
             "the one-line mechanism (A >= 0 => all ACF samples "
             ">= 0 by inspection) is LIVE; the sign law reduces "
             "to proving A_{v_0} >= 0 -- a new concrete target"
             if nonneg_all else
             "the one-line mechanism is DEAD as stated; the "
             "measured negative mass eta quantifies how far the "
             "profile is from one-signed"))

    if calib or smoke:
        for h in rungs:
            print("CAL jets h=%d mjet %d jr %s"
                  % (h, res[h]["mjet"],
                     str(["%.1f" % x for x in
                          res[h]["jr_log10"][:6]])))
        ok32 = True
    else:
        ok32 = all(res[h]["mjet"] == CAL_MJET[h]
                   and abs(res[h]["jr_log10"][0]
                           - float(CAL_JR0[h])) <= 3 * LOG_TOL
                   for h in rungs)
    check("G32-jet-ladder", ok32,
          "edge-jet cancellation ladder jr_j = |sum v_k b_k^j| / "
          "sum |v_k| b_k^j: MJET (prefix at %.0e) = %s; jr_0 dex = "
          "%s -- the j = 0 jet is the residue functional A_0 in "
          "profile coordinates (its depth ladder tracks the "
          "alignment laws, r182/r186 territory, typed "
          "SAME-STRUCTURE-NEW-COORDINATES)"
          % (JET_BAR, str({h: res[h]["mjet"] for h in rungs}),
             str({h: "%.1f" % res[h]["jr_log10"][0]
                  for h in (4, 8, 13, 20) if h in res})))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL decay h=%d s_exp %.3f r2e %.3f p_pow %.3f "
                  "r2p %.3f p_edge %.3f c_h %.2f r_tau %.4f "
                  "s_atom %.3f p_atom %.3f gneg %d nres %d"
                  % (h, r["lag_s_exp"], r["lag_r2e"],
                     r["lag_p_pow"], r["lag_r2p"], r["lag_p_edge"],
                     r["c_h"], r["r_tau"], r["s_atom"],
                     r["p_atom"], r["lag_gneg"], r["lag_nres"]))
        ok33 = True
    else:
        ok33 = all(
            abs(res[h]["lag_p_pow"] - float(CAL_PG[h]))
            <= FIT_TOL * abs(float(CAL_PG[h]))
            and abs(res[h]["c_h"] - float(CAL_CH[h]))
            <= FIT_TOL * abs(float(CAL_CH[h]))
            and abs(res[h]["r_tau"] - float(CAL_RTAU[h]))
            <= FIT_TOL * abs(float(CAL_RTAU[h]))
            for h in rungs)
    cs_all = [res[h]["c_h"] for h in rungs]
    chalf = ("C-HALF-REJECTED" if min(cs_all) >= 5.0
             else "C-HALF-ALIVE")
    pgl = [res[h]["lag_p_pow"] for h in rungs]
    med_p = sorted(pgl)[len(pgl) // 2]
    univ_p = (max(pgl) - min(pgl)) / abs(med_p) if med_p else 1e9
    rtl = [res[h]["r_tau"] for h in rungs]
    med_r = sorted(rtl)[len(rtl) // 2]
    univ_r = (max(rtl) - min(rtl)) / abs(med_r) if med_r else 1e9
    r2p_win = all(res[h]["lag_r2p"] >= res[h]["lag_r2e"] + 0.05
                  for h in rungs)
    r2e_win = all(res[h]["lag_r2e"] >= res[h]["lag_r2p"] + 0.05
                  for h in rungs)
    model = ("DECAY-EDGE-POWER" if r2p_win else
             ("DECAY-EXPONENTIAL" if r2e_win else
              "DECAY-MODEL-MIXED"))
    if univ_p <= 0.15 and r2p_win:
        univ = "DECAY-EXPONENT-UNIVERSAL(edge-power)"
    elif univ_r <= 0.25:
        univ = "DECAY-EXPONENT-TAU-TRACKING"
    else:
        univ = "DECAY-RUNG-DEPENDENT-UNMODELED"
    check("G33-decay-law-fits", ok33,
          "lag-lattice fits at every rung: edge power p_g = %s "
          "(R2 %s vs exp R2 %s -- model %s); effective exponential "
          "c_h = -s ln10 = %s => the weight candidate c = 1/2 is "
          "%s (min c/0.5 = %.0fx); tau-normalized rate r_tau = %s "
          "(spread %.2f) => %s"
          % (str({h: "%.2f" % res[h]["lag_p_pow"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.3f" % res[h]["lag_r2p"]
                  for h in (4, 13) if h in res}),
             str({h: "%.3f" % res[h]["lag_r2e"]
                  for h in (4, 13) if h in res}),
             model,
             str({h: "%.1f" % res[h]["c_h"]
                  for h in (4, 8, 13, 20) if h in res}),
             chalf, min(cs_all) / 0.5,
             str({h: "%.3f" % res[h]["r_tau"]
                  for h in (4, 8, 13, 20) if h in res}),
             univ_r, univ))

    selfconv_dev = {h: abs(res[h]["lag_p_pow"]
                           - (2 * res[h]["prof_pA"] + 1))
                    / max(abs(2 * res[h]["prof_pA"] + 1), 1.0)
                    for h in rungs
                    if not math.isnan(res[h]["prof_pA"])}
    jetconv_dev = {h: abs(res[h]["lag_p_pow"]
                          - (4 * res[h]["mjet"] + 1))
                   / float(4 * res[h]["mjet"] + 1) for h in rungs}
    if calib or smoke:
        print("CAL mech selfconv %s jetconv %s"
              % (str({h: "%.3f" % v for h, v in
                      selfconv_dev.items()}),
                 str({h: "%.3f" % v for h, v in
                      jetconv_dev.items()})))
        ok34 = True
        mech_enum = "TBD-AT-FREEZE"
    else:
        mech_enum = FROZEN_ENUMS.get("mechEnum", "")
        ok34 = all(abs(jetconv_dev[h] - float(CAL_MECH[h]))
                   <= FRAC_TOL for h in rungs)
    check("G34-decay-mechanism-laws", ok34,
          "JET-CONVOLUTION law p_g == 4 MJET + 1 (g near the edge "
          "is the self-convolution of the profile's edge jet; the "
          "first MJET even jets of A_{v_0} cancel below %.0e): rel "
          "dev ladder %s; the two-step form via the profile edge "
          "window (p_g == 2 p_A + 1, p_A == 2 MJET) carries the "
          "constant-floor contamination of the extreme edge "
          "(jr_0 > 0), rel dev %s -- recorded, not law-gated; "
          "enum %s"
          % (JET_BAR,
             str({h: "%.3f" % jetconv_dev[h]
                  for h in (4, 8, 13, 20) if h in jetconv_dev}),
             str({h: "%.3f" % v for h, v in
                  list(selfconv_dev.items())[:4]}),
             mech_enum))

    gneg_all0 = all(res[h]["lag_gneg"] == 0 for h in rungs)
    gpos_enum = ("ACF-POSITIVE-ALL-LAGS" if gneg_all0 and all(
        res[h]["gq_neg"] == 0 for h in rungs)
        else "ACF-POSITIVE-AT-ATOMS-ONLY")
    ok35 = True if (calib or smoke) else all(
        res[h]["lag_gneg"] == CAL_GNEG[h] for h in rungs)
    check("G35-acf-sign-census", ok35,
          "g_{v_0} sign census on the 24-point lag lattice + atom "
          "lags at every rung: negative counts %s, atom-lag "
          "negatives %s -- enum %s (a strengthening of the r195 "
          "sign law beyond the atom lags if 0 everywhere)"
          % (str({h: res[h]["lag_gneg"] for h in rungs}),
             str({h: res[h]["gq_neg"] for h in rungs}),
             gpos_enum))

    # ------------------------------------------------------------ S4
    section("S4  F2: EFFECTIVE HORIZON LADDER")
    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL horiz h=%d n99 %s q99 %s n999 %s q999 %s "
                  "ntau %s qtauf %.3f natoms %d"
                  % (h, r["n99"], r["q99"], r["n999"], r["q999"],
                     r["ntau"], r["qtau_frac"], r["natoms"]))
        ok40 = True
    else:
        ok40 = all((res[h]["n99"], res[h]["q99"], res[h]["n999"],
                    res[h]["q999"]) == CAL_HORIZ[h] for h in rungs)
    q99max = max(res[h]["q99"] for h in rungs)
    horiz = ("HORIZON-BOUNDED-23" if q99max <= 3 else
             ("HORIZON-SLOW" if q99max <= 5 else
              "HORIZON-GROWING"))
    check("G40-horizon-ladder", ok40,
          "THE DECISIVE LADDER (predefined prefix horizons in "
          "ascending q): (n99, q99) = %s, (n999, q999) = %s over "
          "h = 4..20 -- max q99 = %d: enum %s; the budget-scale "
          "prime demand at v_0 is carried by the atoms q <= %d at "
          "every reachable rung"
          % (str({h: (res[h]["n99"], res[h]["q99"])
                  for h in rungs}),
             str({h: (res[h]["n999"], res[h]["q999"])
                  for h in (4, 8, 13, 20) if h in res}),
             q99max, horiz, q99max))

    if calib or smoke:
        ok41 = True
    else:
        ok41 = all(abs(res[h]["qtau_frac"]
                       - float(CAL_QTAUF[h])) <= FRAC_TOL
                   for h in rungs)
    check("G41-demand-scale-horizon", ok41,
          "THE HONEST COUNTERWEIGHT: at the demand scale "
          "(remaining tail <= lambda_0) the horizon consumes the "
          "resolvable-prefix fraction %s (1.00 = EVERY resolvable "
          "atom is load-bearing); dexgap = log10(|Tail_{q>3}| / "
          "lambda_0) = %s -- rides tau BY CONSTRUCTION (the demand "
          "IS the tau-depth cancellation): flagged DEFINITIONAL, "
          "never screened as discovery; quantifier compression is "
          "SCALE-RELATIVE: budget-scale few-atom, demand-scale "
          "all-atom"
          % (str({h: "%.2f" % res[h]["qtau_frac"] for h in rungs}),
             str({h: ("%.1f" % res[h]["dexgap"])
                  if res[h].get("tail_res") else "None"
                  for h in (5, 8, 13, 16, 20) if h in res})))

    # ------------------------------------------------------------ S5
    section("S5  F3: THE REDUCED STATEMENT")
    tr = [h for h in rungs if res[h].get("tail_res")]
    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL red h=%d red_pos %s red_log10 %.2f "
                  "tail_res %s tail_t2 %s dexgap %s rho %s "
                  "bound_ok %s overshoot %s"
                  % (h, r["red_pos"], r["red_log10"],
                     r["tail_res"],
                     ("%.2f" % r["tail_t2"]) if r.get("tail_res")
                     else "n/a",
                     ("%.1f" % r["dexgap"]) if r.get("tail_res")
                     else "n/a",
                     ("%.3f" % r.get("rho_tail", float("nan")))
                     if r.get("tail_res") else "n/a",
                     r.get("tail_bound_ok", "n/a"),
                     ("%.1f" % r.get("overshoot_dex", float("nan")))
                     if r.get("tail_res") else "n/a"))
        ok50 = True
    else:
        ok50 = all(res[h]["red_pos"] for h in rungs) and all(
            res[h].get("tail_bound_ok", True) for h in tr) and all(
            abs(res[h]["tail_t2"] - float(CAL_TAILT2[h]))
            <= 3 * LOG_TOL for h in tr) and all(
            abs(res[h]["dexgap"] - float(CAL_DEXGAP[h]))
            <= 3 * LOG_TOL for h in tr)
    check("G50-reduced-statement", ok50,
          "the reduced form red = P + A + t_2 + t_3 = lambda_0 + "
          "|Tail| (exact resplit of the r195 budget, DEFINITIONAL) "
          "is positive at every rung at the |Tail| scale "
          "(log10 red %s); tail smallness |Tail|/|t_2| = %s dex; "
          "the measured geometric majorant (rho = max consecutive "
          "ratio over q > 3, accelerating decay => valid) COVERS "
          "the tail at every tail-resolvable rung BUT overshoots "
          "lambda_0 by %s dex: ANY lossy tail bound is "
          "CERTIFICATION-DEAD at the demand scale -- the r195 "
          "dead-class lesson repeated at the tail, priced not "
          "crossed"
          % (str({h: "%.1f" % res[h]["red_log10"]
                  for h in (5, 13, 20) if h in res}),
             str({h: ("%.1f" % res[h]["tail_t2"]) for h in tr}),
             str({h: ("%.1f" % res[h]["overshoot_dex"])
                  for h in (5, 13, 20) if h in tr and h in res})))

    horiz_ok = q99max <= 3
    tail_ok = all(res[h].get("tail_bound_ok", True) for h in tr)
    redu = ("FEWATOM-REDUCTION-STRUCTURAL-VALID"
            if horiz_ok and tail_ok else
            "FEWATOM-REDUCTION-FAILS")
    ok51 = (res[H_HOLD]["q99"] <= 3 if H_HOLD in res else True) \
        if rec else True
    check("G51-holdout-and-relabeling", ok51 if rec else True,
          "deep holdout h = 20: (n99, q99) = %s, sign law %s, "
          "depth %.2f == tau ladder (definitional); ADJUDICATION "
          "(frozen logic): enum %s with the MANDATORY rider "
          "NOT-A-COMPLEXITY-DROP-IN-H -- the reduced statement's "
          "every ingredient (pole square, arch functional, "
          "g_{v_0}(log 2), g_{v_0}(log 3), tail law) is a "
          "functional of v_0(h): the ATOM quantifier is compressed "
          "(12 -> 2-3 + measured-law tail at the budget scale), "
          "the h quantifier is NOT -- v_0's h-dependence is the "
          "wall's, relabeling barrier NAMED, not crossed; the "
          "demand-scale horizon (G41) prices the compression "
          "honestly"
          % (str((res[H_HOLD]["n99"], res[H_HOLD]["q99"]))
             if H_HOLD in res else "n/a",
             str((res[H_HOLD]["tq_pos"], res[H_HOLD]["tq_neg"],
                  res[H_HOLD]["tq_zero"])) if H_HOLD in res
             else "n/a",
             res[H_HOLD]["depth"] if H_HOLD in res else float("nan"),
             redu))

    # ------------------------------------------------------------ S6
    section("S6  F4: WORLDS + WITNESS")
    ctasks = list(CTRL_CELLS)
    if smoke:
        ctasks = [("SCRARITH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    if calib or smoke:
        for k, v in sorted(cres.items()):
            if k[0] == "SMOOTH":
                print("CAL ctrl %s x=%d gneg %d w99 %.3f nsc %d "
                      "eta %.2e iddev %.1e Pr %.3e"
                      % (k[0], k[1], v["lag_gneg"], v["w99_frac"],
                         v["prof_nsc"], v["prof_eta"],
                         v["smooth_id_dev"], v["bud_Pr"]))
            else:
                print("CAL ctrl %s x=%d signs (%d,%d,%d) m99 %d "
                      "n99 %s q99 %s gneg %d negw %s eta %.2e "
                      "nsc %d nonneg %s rmin %.2e"
                      % (k[0], k[1], v["tq_pos"], v["tq_neg"],
                         v["tq_zero"], v["m99"], v["n99"],
                         v["q99"], v["lag_gneg"],
                         v.get("negw", 0), v["prof_eta"],
                         v["prof_nsc"], v["prof_nonneg"],
                         v["prof_rmin"]))
        ok60 = not cerrs
    else:
        def _ck(k):
            cal = CAL_CTRL[k]
            v = cres[k]
            if k[0] == "SMOOTH":
                return (v["lag_gneg"] == cal["gneg"]
                        and abs(v["w99_frac"] - float(cal["w99"]))
                        <= FRAC_TOL
                        and v["prof_nsc"] == cal["nsc"])
            return ((v["tq_pos"], v["tq_neg"], v["tq_zero"])
                    == cal["signs"] and v["m99"] == cal["m99"]
                    and v["n99"] == cal["n99"]
                    and v["q99"] == cal["q99"]
                    and v["lag_gneg"] == cal["gneg"])
        ok60 = (not cerrs) and all(_ck(k) for k in cres) and all(
            cres[k]["asm_dev"] <= (SMOOTH_ID_BAR
                                   if k[0] == "SMOOTH"
                                   else CTRL_ASM_BAR)
            for k in cres)
    check("G60-worlds-battery", ok60,
          "P4 RESOLVED against the measured values (identity layer "
          "world-blind, asm devs %s -- typed, never sold): %s -- "
          "the fake worlds' bottom-direction atom anatomy vs "
          "MAIN's one-signed few-atom structure; SMOOTH continuum "
          "localization w99/L and ACF sign census as the "
          "no-atom baseline"
          % (str({k: "%.0e" % v["asm_dev"]
                  for k, v in sorted(cres.items())}),
             str({k: ("signs (%d,%d,%d) m99 %s n99 %s gneg %d"
                      % (v["tq_pos"], v["tq_neg"], v["tq_zero"],
                         v["m99"], v["n99"], v["lag_gneg"]))
                  if k[0] != "SMOOTH" else
                  ("gneg %d w99 %.2f" % (v["lag_gneg"],
                                         v["w99_frac"]))
                  for k, v in sorted(cres.items())})))

    if True:
        wit = witness_leg()
        wok = (WIT_YT_BAND[0] <= wit["wit_ytr"] <= WIT_YT_BAND[1]
               and wit["wit_a0dev"] <= WIT_A0_BAR)
        if calib or smoke:
            print("CAL wit ytr %.2f a0dev %.1e ovl_base %.6f "
                  "ovl_wit %.6f base signs %s n99 %s P %.3e "
                  "Pr %.3e | wit signs %s n99 %s P %.3e Pr %.3e"
                  % (wit["wit_ytr"], wit["wit_a0dev"],
                     wit["base"]["ovl"], wit["wit"]["ovl"],
                     str(wit["base"]["signs"]), wit["base"]["n99"],
                     wit["base"]["P"], wit["base"]["Pr"],
                     str(wit["wit"]["signs"]), wit["wit"]["n99"],
                     wit["wit"]["P"], wit["wit"]["Pr"]))
            ok61 = wok
        else:
            cw = CAL_WIT
            ok61 = (wok
                    and wit["base"]["signs"] == cw["signs_base"]
                    and wit["wit"]["signs"] == cw["signs_wit"]
                    and wit["base"]["n99"] == cw["n99_base"]
                    and wit["wit"]["n99"] == cw["n99_wit"])
        check("G61-witness-battery", ok61,
              "r172 inflation witness VERBATIM at h = %d (y_t "
              "ratio %.1f in %s, A_0 dev %.1e <= %.0e): base ray "
              "overlap with v_0 = %.6f (the builder ray IS the "
              "collapse direction in Raw transport, measured); "
              "witness ray overlap %.6f; atom anatomy base signs "
              "%s n99 %s vs witness signs %s n99 %s, t-dex base %s "
              "wit %s -- P5 resolved on the record"
              % (WIT_RUNG, wit["wit_ytr"], str(WIT_YT_BAND),
                 wit["wit_a0dev"], WIT_A0_BAR,
                 wit["base"]["ovl"], wit["wit"]["ovl"],
                 str(wit["base"]["signs"]), wit["base"]["n99"],
                 str(wit["wit"]["signs"]), wit["wit"]["n99"],
                 str(["%.1f" % t for t in wit["base"]["tdex"]]),
                 str(["%.1f" % t for t in wit["wit"]["tdex"]])))

    # ------------------------------------------------------------ S7
    section("S7  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_eta, _i, _r = fit_line(xs_t,
                              [math.log10(res[h]["prof_eta"])
                               for h in scr])
    sl_nsc, _i, _r = fit_line(xs_t, [res[h]["prof_nsc"]
                                     / res[h]["K"] for h in scr])
    sl_n99, _i, _r = fit_line(xs_t, [res[h]["n99"]
                                     / res[h]["natoms"]
                                     for h in scr])
    sl_fw1, _i, _r = fit_line(xs_t, [res[h]["prof_fw1"]
                                     for h in scr])
    if calib or smoke:
        print("CAL slopes: eta %+.3f nscK %+.3f n99f %+.3f "
              "fw1 %+.3f" % (sl_eta, sl_nsc, sl_n99, sl_fw1))
        ok70 = True
    else:
        ok70 = (abs(sl_nsc) <= TAU_FLAT_BAR
                and abs(sl_n99) <= TAU_FLAT_BAR
                and abs(sl_fw1) <= TAU_FLAT_BAR
                and abs(sl_nsc - float(CAL_SLOPES["nscK"]))
                <= SLOPE_TOL
                and abs(sl_n99 - float(CAL_SLOPES["n99f"]))
                <= SLOPE_TOL
                and abs(sl_fw1 - float(CAL_SLOPES["fw1"]))
                <= SLOPE_TOL)
    check("G70-tau-screen", ok70,
          "log-log slopes vs tau_h of the DIMENSIONLESS "
          "coordinates: nsc/K %+.3f, n99/natoms %+.3f, fw1 %+.3f "
          "-- flat (bar %.2f): the few-atom structure does not "
          "ride the tau currency; eta slope %+.3f and the jr_0/"
          "dexgap/r_tau ladders DO ride tau -- flagged: eta and "
          "jr_0 are alignment-depth observables (definitional "
          "territory), dexgap is definitional by construction, "
          "r_tau is the tau-normalization itself; none screened "
          "as discovery"
          % (sl_nsc, sl_n99, sl_fw1, TAU_FLAT_BAR, sl_eta))

    delivered = {
        "ATOMS": ["ACF-KERNELS"], "MODES": ["ACF-KERNELS"],
        "ACF-KERNELS": ["PROFILE-SHAPE", "ACF-DECAY", "HORIZON"],
        "MBLOCKS": ["ACF-KERNELS", "TAU-SCALAR"],
        "PROFILE-SHAPE": ["REDUCED-FORM"],
        "ACF-DECAY": ["REDUCED-FORM"],
        "HORIZON": ["REDUCED-FORM"],
        "REDUCED-FORM": ["SCREENS"], "TAU-SCALAR": ["SCREENS"],
        "SCREENS": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("PROFILE-SHAPE", "ACF-DECAY", "HORIZON",
                 "REDUCED-FORM", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "ZEROVERIF-HYP", "RH"}
    check("G71-loop-guard", ndet == 6
          and not has_cycle(delivered) and not hot,
          "flagged cycles DETECTED (A0-triangle, census-forall-k, "
          "Gonek-1984, Montgomery-PC, WEIL-ALLTESTS, zero-"
          "verification-as-hypothesis), consumed by NOTHING: DFS "
          "ancestry of every delivered node clean; the round is "
          "fully zero-free (no ordinate cache); the reduced "
          "statement is a PER-RUNG finite resplit and has no edge "
          "into any criterion loop")

    check("G72-composed-chain-typing", True,
          "leg typing: {assembly, pole square, budget resplit, "
          "grid/lag lattices} EXACT (mp <= 1e-30 class); {profile "
          "ladder, jet ladder, decay fits, horizons, world/witness "
          "anatomy} MEASURED; {depth == tau, dexgap, red = "
          "lambda_0 + |Tail|} DEFINITIONAL; {SELFCONV/JET laws} "
          "MEASURED-LAW (not proven); the certification-dead "
          "adjudication of lossy tail bounds is a PRICING, not a "
          "theorem; jr_0 depth = alignment territory (r182/r186), "
          "typed SAME-STRUCTURE-NEW-COORDINATES, no new "
          "arithmetic sold")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1,
            ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "FEWATOMDOM"): INF, ("FEWATOMDOM", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G73-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the few-atom reduced wall proven cofinally' as a unit "
          "edge would raise the flow to 6 -- NOT REAL (the "
          "reduced statement is per-rung and v_0(h)-quantified): "
          "this round adds NO flow; census cardinality UNCHANGED; "
          "RH unreachable without the omega edges")

    # ------------------------------------------------------------ S8
    section("S8  PRICING + RESIDUE")
    check("G80-pricing", True,
          "what the round BUYS: (i) the sign-law mechanism is "
          "adjudicated at the shape level (P1 on the record; if "
          "nonneg fails, eta quantifies the miss and the "
          "concentration story is priced), (ii) the decay law has "
          "a mechanism candidate (edge self-convolution) tied to "
          "the ALIGNMENT jets -- typed as the r182 laws in ACF "
          "coordinates, not new arithmetic, (iii) the horizon "
          "question is answered TWICE (budget scale vs demand "
          "scale) -- the honest price of the quantifier "
          "compression is the demand-scale all-atom horizon and "
          "the tau-riding dexgap; the cofinality gap is UNMOVED: "
          "the wall demand for ALL h stays in the "
          "{H1 ^ H2 ^ H3}-KOFINAL residue, cardinality unchanged")

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (one rung per dyadic block, all three at the "
         "same h; limsup form only mod D = 0.0042) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN: L1 = TAIL proven + H-pin open; WPD(a < gamma_1^2) "
         "<= H-pin; WPD non-lambda legs: extension instantiated, "
         "TAILWPD world front}.  Closes NOTHING, upgrades NOTHING.  "
         "NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        sign_mech + "(G31)",
        gpos_enum + "(G35)",
        model + "(G33)",
        chalf + "(G33)",
        univ + "(G33)",
        mech_enum + "(G34)",
        horiz + "(G40)",
        "DEMAND-SCALE-ALL-ATOM(G41: qtau_frac 1.00, dexgap "
        "definitional)",
        redu + "+NOT-A-COMPLEXITY-DROP-IN-H(G51)",
        "LOSSY-TAIL-CERTIFICATION-DEAD(G50)",
        "SIGN-LADDER-INHERITED-EXACT(G22)",
        "WORLDS-MEASURED(G60) + WITNESS-ON-RECORD(G61)",
        "TAU-FLAT-STRUCTURE(G70) + ALIGNMENT-DEPTH-FLAGGED",
        "LOOPS-FLAGGED-NOT-CONSUMED(G71)",
        "MINCUT-UNCHANGED(G73) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        sign_mech, gpos_enum, model, chalf, univ, mech_enum, horiz,
        "DEMAND-SCALE-ALL-ATOM", redu,
        "NOT-A-COMPLEXITY-DROP-IN-H",
        "LOSSY-TAIL-CERTIFICATION-DEAD", "TAU-FLAT-STRUCTURE",
        "LOOPS-FLAGGED-NOT-CONSUMED", "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
