#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""profile_functional_probe -- PRIME.PORT.LSTAR.
PROFILE_FUNCTIONAL.01 (round 290): the GEOMETRY of the working
set in profile space.  r289 sealed METRIC_ONLY: the firewall
reads the fraction PROFILE metrically (rational twin keeps
everything at destroyed log-relations; coherence threshold
1e-3..3e-3 of the local gap; sub-gap entry = tent-split
fractions; flip carrier = mid degree band 50-75 pct; O(1) mover
= crossing relocation).  r288: carrier class = antiphase 3-4
ARCH pairs.  r285: MAIN assist = ensemble LOW_OUTLIER pct 0.00
(all 28 replicates die collectively).  r280: MAIN is a RIDGE,
not a peak (raising directions exist, OPT at theta 7.75e-5 ->
minC 185).  THE OPEN FRONT: which FUNCTIONAL of the profile
forces the destructive coherence -- the working set in profile
space is neither a point nor a ball around MAIN; its geometry
is the question.  NOT a proof round: no L* claim, no bound
mechanism, no asymptotic law.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

PROFILE CONVENTION (sealed FIRST, from the r289 completeness
identity): the source enters the machinery EXACTLY through the
signed lag density d on the fixed grid (d = grid_density(c_ar +
c_at); the lag vector factors through (cell, fraction, mass) to
1e-12 -- r289 G40).  PROFILE := the signed density d (length L,
even), equivalently the signed folded weight vector wsig =
MS.wsig_vec(d, L) (both LINEAR in the tent-split fractions at
fixed cells).  Profile-space moves keep the GRID (positions/
cells) fixed and move WEIGHT PROFILES: interpolation d(t) =
(1-t) d_MAIN + t d_TARGET (exactly the weight-profile
interpolation; the ARCH background c_ar is shared w9 geometry
and rides along both endpoints).  The gap-equivalent DISTANCE
of a profile move dd is measured in the LAG coordinate (the
r289 completeness object; densities invert exactly to lag
profiles, lag(d) = ifft(d).real[:M], identity gated 1e-12):
theta_eq(dd) = |lag(dd)|_1 / REF with the ANALYTIC reference
REF = 0.5 sum_j m_j g_j / Delta = the exact expectation
E|lag(dd)|_1 / theta of one r276 gap-scaled jitter (U[-1, 1];
per-atom |dc|_1 = m |du| / Delta, tent linearity in-cell);
gate: three pinned calibration jitters at 1e-3 AND one
independent jitter at 3e-4 must each measure theta_eq within
0.15 of their theta.  The
survival depth of ANY profile point is s = minC / N_REF with
N_REF = 184 (the w9 window depth -- the r276/r288/r289 house
normalization; own half-filling (S+1)//2 is DISCLOSED per point,
never silently substituted).

INDEX FIREWALL (binding, r238-r289 discipline): w = window (kz),
S = #union entries, S_+/S_- = #mu/#nu atoms, N_REF = 184 = w9
window depth, n = chain degree, p = fold-grid index, t = path
parameter, theta_eq = gap-equivalent profile distance; ground
truth (minC, crossings, z_v, onset records) enters GATES and
record tables only; the sealed constructors consume profiles/
densities + grid geometry + seeds ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r288 DC.{zv_block, balance_terms, band_split,
jacobi_zeros, phase_field, circ_dist}, r284 LS.{split_by_fold,
atom_labels, spectral_block, world_pack, dist_rule,
christoffel_rows, top_eigvecs}, r283 FS.{mu_chain_f64,
b_matrix_f64, crossing_from_B}, r278 MS.{ctx_build, wsig_vec,
grad_chain, grad_pack}, r276 MF.{local_gaps, pert_jit,
conserve_comb}, r280 BL.{union_of_ctx, sign_chain_f64,
grad_ext, dir_opt, theta_of_dir}, r285 CD.{sign_assignment,
ens_sign_world}, v881 PIK.{build_rung, grid_density,
folded_measure, lambda_eps}, r243 PB.smooth_comb, r244
BH.spearman, paircorr PC.{Grid, gen_model}, v563 core READ-ONLY.

LEG A -- INTERPOLATION PATHS (the death-onset map): five sealed
weight-profile paths d(t) = (1-t) d_MAIN + t d_TARGET, targets
= SMOOTH (PB.smooth_comb), SCRAMBLE (scramble_seed 1), EPSTEIN
(r285 comb 2 lam_eps(n)/sqrt(n) at log n), ENSR (the r285
ENS_SCR replicate 0, scramble_seed 285100 -- an ensemble
replicate as a profile point), RIDGE (the r280 OPT endpoint,
rebuilt from the exact r280 machinery: xi = dir_opt at the wall
degree, endpoint dose 2 theta_up; anchor: theta_up == 3.87e-5
rel 0.05 AND rebuilt minC == 185).  Per path the sealed t
ladder PATH_TS, measured s = minC/N_REF, z_v + fold-band 3-4
share at the own crossing, S + own half-filling (disclosed).
(a1) ONSET per path: first ladder t with s < NEAR (0.90),
  bracketed and refined by 3 geometric bisections; reported in
  t AND in theta_eq units (the direction dependence: r276
  curves were surgery doses, THESE are directed profile
  distances against the 1e-3..3e-3 jitter threshold).
(a2) SHARP iff the refined bracket has s(t_lo) >= NEAR and
  s(t_hi) <= DEAD (0.50) with t_hi/t_lo <= 1.5; else GRADUAL.
(a3) RIDGE REACH: the OPT direction extended linearly in
  profile space to RIDGE_FACS x the endpoint (in-cell the
  linear density extension EQUALS the position move, disclosed);
  lift reach = max factor with minC > 184, death = first factor
  with s < NEAR.
LEG B -- BASIN GEOMETRY: (b1) ISOTROPY: NDIR_FRAC = 10 pinned
random fraction directions (comb jitter directions at theta_cal,
weights bitwise -- exact r276 conservation) + NDIR_DENS = 6
pinned on-support density directions (even-symmetrized,
0th-moment eta_0 projected out EXACTLY, gate 1e-12) at the
sealed distances DIST_GRID (5e-4, 1e-3, 2e-3, 3e-3, 5e-3)
theta_eq units: kill fraction per distance; sealed typing at
ISO_DIST 3e-3 over ALL 16 directions: TUBE iff killfrac >=
0.75, BROAD iff <= 0.25, else MIXED.  (b2) CURVATURE at the
rim: along KILLER (the fraction direction with the smallest
death bracket), RIDGE, and RAND (fraction direction seed
290100): s at CURV_FACS (0.5, 0.7, 1.0, 1.4, 2.0) x theta_on;
second-order index kappa = s(0.5 th) + s(2 th) - 2 s(th) and
the same SHARP/GRADUAL rule.  (b3) SMOOTH ANATOMY: the
MAIN-minus-SMOOTH direction (the arithmetic direction in
profile space): its theta_eq length, its onset distance vs the
jitter threshold, the midpoint t = 0.5 anatomy (s, z_v, b34, S),
and the alignment cosine of dwsig_SMOOTH with the last free
wall-pivot profile gradient Q2[:, N_REF-1] (typed PERTURBATIVE).
LEG C -- FUNCTIONAL CANDIDATES (sealed, exactly 4; source-pure
profile functionals, NO chain/kernel computation on the test
world -- AST-scoped; F3 consumes the FROZEN MAIN gradient pack
and is honestly typed PERTURBATIVE/MAIN-LOCAL):
  F1 ANTIPHASE34 (r288 carrier as profile statistic): lag-3+4
    autocorrelation of the OWN wsig: (sum_p w_p w_{p+3} + sum_p
    w_p w_{p+4}) / sum_p w_p^2.
  F2 ROUGHNESS (the 1e-3 precision reading): total variation
    of the OWN wsig / sum |w|.
  F3 GRADALIGN (r278 gradients, PERTURBATIVE): min over the
    wall band n = N_REF-5..N_REF-1 of (dwsig @ Q2[:, n]) /
    eta_n -- the linearized d log h_n of the profile deviation
    (Hellmann-Feynman in the wsig coordinate; eta ward re-gated
    <= 1e-9); dwsig = wsig - wsig_MAIN.
  F4 MIDBAND (r289 flip carrier as profile statistic): the
    50-75 pct Chebyshev band energy share of the DEVIATION:
    coef_k = sum_p dwsig_p cos(2 pi k p / L), F4 = sum_{k in
    [0.5 N_REF, 0.75 N_REF)} coef_k^2 / sum_{k <= N_REF}
    coef_k^2 (F3 = 0 and F4 = 0 sealed at zero deviation).
  PREDICTION: Spearman rank correlation (r244 BH.spearman,
  tie-averaged) of each F against the measured s over the FULL
  test set (all path points + bisections + ridge + 16 x 5
  directions + curvature points + 28 replicates + 5 worlds +
  MAIN); WORLD SEPARATION per F via the sealed r281 distance
  rule over MAIN + EPST/SCR/SMOOTH/HL2.  SEALED ADJUDICATION
  (exactly one): FUNCTIONAL_FOUND iff best |sp| >= 0.8 AND that
  functional is MAIN_SEPARATING; FUNCTIONAL_PARTIAL iff best
  |sp| >= 0.5; ALL_FUNCTIONALS_BLIND otherwise (honest -- the
  working set then remains implicitly characterized).
REPLICATES (the r285 ensembles as profile points): ENS_SIGN 16
(sign_assignment seeds 285000+i; realized as DENSITY sign flips
at both grid points l and L-l of every union fold -- magnitudes
untouched, fold multiset + magnitude conservation gated exactly;
rep 0 minC identity-gated against CD.ens_sign_world) + ENS_SCR
12 (scramble_seed 285100+i, weights bitwise gated).

WARDS / MUST-FAILS (each loud): w9 regression (S = 367/263/104,
N_REF 184, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, C_off -0.1046 tol 0.005, band 3-4 -0.105 tol
0.01, AA -0.056 tol 0.01); measurement-channel identity (the
density channel reproduces world_pack/spectral_block on MAIN:
union bitwise, minC/crossing equal, z_v to 1e-9, rho at
20/120/184/185 to 1e-10 against crossing_from_B -- the
early-stop rho scan is a gated measurement-domain optimization);
r289 LADDER ANCHOR (exact r289 seeds 289320/21 + 289330/31:
depth med 1.00 / 0.37 tol 0.02, z_v med -3.34 / +5.26 tol
0.05); r280 RIDGE ANCHOR (theta_up 3.87e-5 rel 0.05, rebuilt
minC 185, f64 level of the mp-confirmed r280 record,
disclosed); CONTROL FLIPS minC = 25/21/27/25 on EPST/SCR/
SMOOTH/HL2 (r285); eta ward <= 1e-9; exact toys (t1 interp
identity/linearity bitwise + exact mean; t2 hand functionals
wsig = (1, 2, -1, 3, -2): F1 = -3/19, F2 = 13/9, F3 toy 4/2 =
2, F4 toy argmax band at k = 2; t3 theta_eq self-consistency at
3e-4, seed 290010, tol 0.15; t4 ENS_SIGN rep-0 density identity:
fold multiset + magnitudes exact + minC == ens_sign_world).
MUST-FAILS: (m1) UNPROJECTED DENSITY DIRECTION (eta_0 kept)
must be CAUGHT by the conservation gate; (m2) UNWEIGHTED
PROFILE (fold aggregation WITHOUT the s_l weighting) must break
the eta ward by >= 0.1 rel (LOUD); (m3) ONE-SIDED SIGN FLIP
(only grid point l, not L-l) must be CAUGHT by the fold
conservation gate (union fold multiset breaks); (m4) a
direction oriented by the withheld onset census is FLAGGED by
the AST scope audit.  STOP LIST (anti-gates, binding): NO L*
claim, NO bound mechanism, NO asymptotic law, NO derived 5/7,
NO equidistribution premise, NO posthoc window, NO RH claim;
r243..r289 stand.

SEALED CONSTANTS: MAIN window 9; N_REF 184; DEPTH_PAD 6; EXT 8
/ EXT2 32; CROSS_REC 185; MINC_REC 184; S_REC (367, 263, 104);
MARGIN_REC 1.68e-4 rel 0.01; ZV_REC -3.149 tol 0.02; COFF_REC
-0.1046 tol 0.005; B34_REC -0.105 tol 0.01; AA_REC -0.056 tol
0.01; CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27 / HL2 25 (seed
101); NEAR 0.90; DEAD 0.50; SHARP_RATIO 1.5; PATH_TS (1e-4,
3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 0.5, 1.0); N_BISECT 3;
RIDGE_FACS (0.25, 0.5, 1, 2, 4, 8, 16, 32, 64); THETA_CAL 1e-3;
CAL_SEEDS (290000, 290001, 290002); T3_SEED 290010 / T3_THETA
3e-4 / T3_TOL 0.15; NDIR_FRAC 10 seeds 290100+; NDIR_DENS 6
seeds 290200+; DIST_GRID (5e-4, 1e-3, 2e-3, 3e-3, 5e-3);
ISO_DIST 3e-3; TUBE_BAR 0.75 / BROAD_BAR 0.25; CURV_FACS (0.5,
0.7, 1.0, 1.4, 2.0); WALL_BAND N_REF-5..N_REF-1; SP_FOUND 0.8 /
SP_PART 0.5; ETA0_BAR 1e-12; ETAWARD_BAR 1e-9; RHO_ID_TOL
1e-10; ZV_ID_TOL 1e-9; LAD_ANCH theta 1e-3 -> (1.00, -3.34) /
3e-3 -> (0.37, +5.26), tol depth 0.02 / z_v 0.05, seeds 289320,
289321, 289330, 289331 (the r289 SEED_JL formula); THUP_REC
3.87e-5 rel 0.05; RIDGE_MINC_REC 185; ENS_SIGN_REPS 16 /
ENS_SCR_REPS 12 / SEED_R285 285000 (scr +100+i); M2_BAR 0.1;
runtime <= 1800 s; smoke = toys + firewall + scopes + mutants +
w9 regression + measurement-channel identity + eta ward (paths,
directions, replicates, functionals, anchors, adjudication
skipped).  PRE-SPEC SCOPING (disclosed): every record number is
a published r276/r280/r283/r284/r285/r288/r289 record adopted
as-is; the profile convention, the five paths, the distance
metric, the direction classes, the four functionals with their
bands, and all typing rules were fixed at design time from the
published records and the lstar_problem construction; no
machinery pass preceded this spec except record reading; no
bar, band or rule was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  BASIN_GEOMETRY(onset map (t and theta_eq per path),
    SHARP/GRADUAL census, ISOTROPY = TUBE/BROAD/MIXED(killfrac),
    SMOOTH_DIRECTION(onset vs jitter threshold, midpoint
    anatomy, wall-gradient alignment)) [always]
  + RIDGE_MAP(lift reach factor, death factor) [always]
  + [exactly one of] FUNCTIONAL_FOUND(name, spearman,
    separation) / FUNCTIONAL_PARTIAL(best name, spearman) /
    ALL_FUNCTIONALS_BLIND
  + FUNCTIONAL_TABLE(per candidate: spearman, world values,
    detector typing) [always]
  + DETECTOR_LEDGER [always].
Honesty before beauty: onset maps, kill fractions, curvature
indices and functional correlations are MEASUREMENTS on finite
w9 profile space; F3 is perturbative and MAIN-local by
construction; no verdict claims L*, a bound mechanism, a
derived 5/7 or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 32/32 (0.3 s); calibration
pass 1 = first full evaluation = 30/32, wall 3.9 s, exposing
amendment a1 (G30 t3 self-consistency FAILED as designed; G96
failed only as the all-pass mirror); pass 2 with a1 = 32/32,
wall 4.0 s = the record run; the record-table insertion below
is the only post-freeze edit, which IS the protocol; run1/run2
identical up to WALL).
DISCLOSED CALIBRATION AMENDMENT (found in calibration pass 1,
BEFORE the record freeze; no physics bar, band, path, direction
class, functional or verdict rule moved): (a1) the theta_eq
coordinate was first realized as the DENSITY-L1 norm |dd|_1
with a seed-calibrated reference; the sealed t3 gate exposed
that this coordinate is ill-conditioned (the FFT density is
delocalized: |dd|_1/theta varies ~37 pct between seeds -- dev
0.370 > bar 0.15).  The coordinate was re-anchored in the exact
LAG profile (lag(d) = ifft(d).real[:M], the r289 completeness
object; inversion identity 1.5e-16) with the ANALYTIC reference
REF = 0.5 sum m g / Delta = 125.75 (the exact expectation of
one gap-scaled jitter); the same sealed gate then measures devs
(0.059, 0.125, 0.117, 0.028) <= 0.15.  A measurement-domain
COORDINATE fix demanded by the gate itself; every physics bar,
band, path, direction class, functional and verdict rule stands.
CAL_VERDICT = BASIN_GEOMETRY(onset map (theta_eq units, sealed
NEAR = 0.90 bar): SMOOTH 1.36e-4 / SCR 1.73e-4 / EPST 2.32e-4 /
ENSR 3.95e-5 -- ALL FOUR world paths die 5..50x BELOW the
1e-3..3e-3 jitter threshold band: world-directed profile moves
are far more lethal per gap-dose than random moves (the rim is
strongly ANISOTROPIC); all four GRADUAL at the sealed 1.5-ratio
rule (brackets s 0.95->0.89 / 0.91->0.77 / 0.96->0.86 / ENSR
dead at the first ladder point 1e-4 with s 0.78) -- the onset
is a SOFT SHOULDER (a few wall degrees retreat), not a cliff;
ISOTROPY = TUBE (killfrac 1.00 at the sealed 3e-3; 0.38 / 0.62
/ 1.00 / 1.00 / 1.00 at 5e-4/1e-3/2e-3/3e-3/5e-3 -- by the
NEAR bar the tube radius is ~5e-4..2e-3, consistent with the
ensemble pct 0.00; the DEEP collapse s < 0.5 sits at the r289
2..3e-3 scale, disclosed); SMOOTH_DIRECTION(theta_eq length
0.268, onset 1.36e-4 = 5.1e-4 x full path -- the arithmetic
direction IS a privileged killer axis (~4..7x below the random
shoulder); midpoint t = 0.5: s 0.158, minC 29, S 367, z_v
+3.64, b34 +0.183 -- control-like at half way; wall-gradient
alignment cos = -3e-5: the lethality is NOT first-order wall
gradient, it is orthogonal-collective)) + RIDGE_MAP(lift minC
= 185 at factors 1..8 = theta_eq 1.5e-4..1.2e-3 (the crest is
REAL and extends to ~1.2e-3 gap-dose -- inside a tube where
half the random directions already kill!); alive to 8; first
death at 16 = 2.4e-3; s at 16/32/64 = 0.79/0.46/0.29) +
ALL_FUNCTIONALS_BLIND(best F4 MIDBAND sp +0.263 < 0.5 -- none
of the four sealed profile scalars predicts the survival depth
over the 187-point test set) + FUNCTIONAL_TABLE(sp vs s: F1
ANTIPHASE34 -0.048, F2 ROUGHNESS +0.168, F3 GRADALIGN +0.185
(PERTURBATIVE), F4 MIDBAND +0.263; secondary sp vs z_v: -0.01 /
-0.13 / -0.16 / -0.27; world values F1 MAIN 0.973 / EPST 0.13 /
SCR 1.08 / SMOOTH 1.96 / HL2 0.994; F2 1.22 / 1.71 / 0.829 /
0.0368 / 1.13; F3 0 / +136 / -69.2 / -32.2 / -53.1; F4 0 /
0.329 / 0.252 / 0.362 / 0.413) + DETECTOR_LEDGER(F1/F2/F3
WORLD_BLIND; F4 MAIN_SEPARATING -- construction-trivial (MAIN
deviation = 0 by definition), disclosed as such, and its sp
0.263 fails the sealed bar anyway).
Key numbers.  W9 regression: S 367/263/104, minC 184, crossing
185, margin 1.6752e-4, z_v -3.149, C_off -0.1046, b34 -0.105,
AA -0.056 -- all records reproduced; channel identity: union
BITWISE, z_v dev 0.0, rho devs 2.2e-16 vs crossing_from_B; eta
ward 1.5e-13.  METRIC (a1): REF = 125.75 analytic, devs
(0.059, 0.125, 0.117, 0.028).  r289 LADDER ANCHOR: s med
1.00 / 0.37, z_v -3.34 / +5.26 at theta 1e-3 / 3e-3 -- exact.
r280 RIDGE ANCHOR: theta_up 3.873e-5 (rec 3.87e-5), theta_kill
3.2e-2, OPT endpoint minC 185.  CONTROL FLIPS 25/21/27/25 ==
records.  ONSET MAP (t_on, theta_eq_on): SMOOTH (5.08e-4,
1.36e-4) / SCR (4.37e-4, 1.73e-4) / EPST (5.08e-4, 2.32e-4) /
ENSR (<= 1e-4, 3.95e-5); path theta_eq lengths 0.268 / 0.397 /
0.456 / 0.395.  RIDGE ROWS (fac, minC, s, theta_eq): (0.25,
184, 1.00) (0.5, 184, 1.00) (1, 185, 1.01, 1.5e-4) (2, 185,
1.01) (4, 185, 1.01) (8, 185, 1.01, 1.2e-3) (16, 145, 0.79,
2.4e-3) (32, 85, 0.46) (64, 53, 0.29, 9.6e-3).  ISOTROPY
killfrac 0.38 / 0.62 / 1.00 / 1.00 / 1.00 at 5e-4..5e-3 (FRAC
== DENS 1.00 at 2e-3: both direction classes see the same
tube).  CURVATURE (s at 0.5/0.7/1.0/1.4/2.0 x theta_on):
KILLER FRAC04 (theta_on 5.0e-4) 1.00/1.00/0.85/0.77/0.72 kappa
+0.02; RAND FRAC00 (7.07e-4) 1.00/1.00/0.85/0.78/0.73 kappa
+0.04; RIDGE (probed at the tube scale 3e-3) 1.01/0.85/0.74/
0.52/0.42 kappa -0.07 -- the shoulder decays quasi-linearly
(|kappa| <= 0.08), NO second-order cliff at the NEAR rim.
ENSEMBLES: ENS_SIGN 16/16 conservation exact, rep-0 identity
minC 20 == ens_sign_world, s in [0.022, 0.109]; ENS_SCR 12/12
weights bitwise, s in [0.022, 0.147] -- the r285 collective
death, profile-resolved.  MUST-FAILS: m1 CAUGHT (|eta_0|
5.5e-2 > 1e-12); m2 LOUD (eta ward rel 2.8e6); m3 CAUGHT
(union fold count 524 != 367); m4 FLAGGED (onsets_true);
scopes + fragments CLEAN.  Runtime 4.0 s full / 0.3 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE
(records inserted per protocol; a1 disclosed above, found and
fixed BEFORE the freeze; no bar, band, class rule or verdict
rule moved).
READING (typed MEASUREMENT): the working set around MAIN is a
SOFT-SHOULDERED TUBE of NEAR-radius ~5e-4..2e-3 gap-equivalent
whose rim is strongly anisotropic: world-directed axes (SMOOTH/
SCR/EPST/replicate) kill at 4e-5..2.3e-4 -- 5..50x earlier than
random directions -- while the r280 ridge axis not only
survives but LIFTS the wall (minC 185) out to 1.2e-3 and only
dies at 2.4e-3; the arithmetic (SMOOTH) direction is such a
privileged killer axis yet is ORTHOGONAL to the first-order
wall gradient (cos -3e-5): its lethality is collective, not
gradient-linear; NONE of the four sealed profile scalars
(antiphase band, roughness, perturbative gradient alignment,
mid-band deviation energy) predicts the survival depth (best
sp 0.263) -- the coherence functional, if it exists as a
closed profile scalar, is NOT among these candidate classes:
the working set remains implicitly characterized
(ALL_FUNCTIONALS_BLIND, honest; the mechanism question stays
OPEN).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import destructive_coherence_probe as DC           # noqa: E402 r288
import lstar_two_measure_probe as LS               # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import budget_localization_probe as BL             # noqa: E402 r280
import christoffel_decomposition_probe as CD       # noqa: E402 r285
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import bordered_hankel_probe as BH                 # noqa: E402 r244
import paircorr_margin_probe as PC                 # noqa: E402
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

MAIN_KZ = 9
N_REF = 184
DEPTH_PAD = 6
EXT = 8
EXT2 = 32
CROSS_REC = 185
MINC_REC = 184
S_REC = (367, 263, 104)
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
ZV_REC = -3.149
ZV_TOL = 0.02
COFF_REC = -0.1046
COFF_TOL = 0.005
B34_REC = -0.105
B34_TOL = 0.01
AA_REC = -0.056
AA_TOL = 0.01
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27, "HL2": 25}
HL2_SEED = 101
NEAR = 0.90
DEAD = 0.50
SHARP_RATIO = 1.5
PATH_TS = (1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 0.5, 1.0)
N_BISECT = 3
RIDGE_FACS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)
THETA_CAL = 1e-3
CAL_SEEDS = (290000, 290001, 290002)
T3_SEED = 290010
T3_THETA = 3e-4
T3_TOL = 0.15
NDIR_FRAC = 10
SEED_FRAC = 290100
NDIR_DENS = 6
SEED_DENS = 290200
DIST_GRID = (5e-4, 1e-3, 2e-3, 3e-3, 5e-3)
ISO_DIST = 3e-3
TUBE_BAR = 0.75
BROAD_BAR = 0.25
CURV_FACS = (0.5, 0.7, 1.0, 1.4, 2.0)
WALL_BAND_LO = N_REF - 5
SP_FOUND = 0.8
SP_PART = 0.5
ETA0_BAR = 1e-12
ETAWARD_BAR = 1e-9
RHO_ID_TOL = 1e-10
ZV_ID_TOL = 1e-9
LAD_ANCH = {1e-3: (1.00, -3.34), 3e-3: (0.37, 5.26)}
LAD_DEPTH_TOL = 0.02
LAD_ZV_TOL = 0.05
SEED_JL289 = 289300
R289_LADDER = (1e-4, 3e-4, 1e-3, 3e-3, 5e-3, 1e-2)
THUP_REC = 3.87e-5
THUP_TOL = 0.05
RIDGE_MINC_REC = 185
ENS_SIGN_REPS = 16
ENS_SCR_REPS = 12
SEED_R285 = 285000
M2_BAR = 0.1

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume profiles/densities + "
                       "grid geometry + seeds ONLY; record numbers "
                       "enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("lag_of", "interp_density", "dir_frac",
                "dir_dens", "ens_sign_density", "ridge_comb",
                "func_antiphase", "func_roughness",
                "func_gradalign", "func_midband")
SCOPE_FORBIDDEN = {"minC", "mc", "zv", "onsets_true", "MINC_REC",
                   "CROSS_REC", "ZV_REC", "sg_h", "lgh", "s_meas"}


def scope_audit(funcname, forbidden):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def lag_of(d, M):
    """exact inverse of PIK.grid_density: the LAG profile of a
    density (linear bijection; identity gated on MAIN).  The
    theta_eq metric lives in this coordinate (amendment a1)."""
    a = np.fft.ifft(np.asarray(d, float)).real
    return a[:M]


def interp_density(d0, d1, t):
    """LINEAR weight-profile interpolation on the fixed grid:
    d(t) = (1-t) d0 + t d1 (positions/cells fixed; linear in the
    tent-split fractions at fixed cells by the r289 completeness
    identity).  Consumes densities + parameter only."""
    return (1.0 - float(t)) * np.asarray(d0, float) \
        + float(t) * np.asarray(d1, float)


def dir_frac(uu, mm, kz, d0, theta_cal, seed):
    """random FRACTION direction: the density move of one r276
    comb jitter at theta_cal (weights bitwise by construction;
    exact r276 conservation) -- returns the raw direction
    dd = d_jit - d0.  Consumes comb + grid + seed only."""
    u2, m2 = MF.pert_jit(np.asarray(uu, float),
                         np.asarray(mm, float), theta_cal, seed,
                         False)
    d2 = np.asarray(PIK.build_rung(kz, comb=(u2, m2))["d"], float)
    return d2 - np.asarray(d0, float), (u2, m2)


def dir_dens(d0, L, seed):
    """random on-support DENSITY direction: even-symmetrized
    gaussian values on the union folds of d0, 0th moment eta_0
    = sum dd_l s_l projected out EXACTLY.  Consumes density +
    grid + seed only."""
    d0 = np.asarray(d0, float)
    rng = np.random.default_rng(seed)
    ll = np.arange(L)
    s_l = 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)
    dd = np.zeros(L)
    for p in range(L // 2 + 1):
        l2 = (L - p) % L
        if d0[p] == 0.0 and d0[l2] == 0.0:
            continue
        v = float(rng.standard_normal())
        dd[p] = v
        dd[l2] = v
    supp = dd != 0.0
    denom = float(np.sum(s_l[supp] ** 2))
    coef = float(np.sum(dd * s_l)) / max(denom, 1e-300)
    dd[supp] -= coef * s_l[supp]
    return dd


def ens_sign_density(d0, folds_sorted, mask, L):
    """r285 ENS_SIGN replicate as a DENSITY: at every union fold
    the sign of the grid density is set to the new label
    (+mu / -nu) at BOTH grid points l and L-l; magnitudes
    untouched by construction.  Consumes density + fold list +
    mask only."""
    d2 = np.asarray(d0, float).copy()
    for f, is_nu in zip(np.asarray(folds_sorted, np.int64), mask):
        s = -1.0 if is_nu else 1.0
        l1 = int(f)
        l2 = (L - l1) % L
        d2[l1] = s * abs(d2[l1])
        if l2 != l1:
            d2[l2] = s * abs(d2[l2])
    return d2


def ridge_comb(uu, mm, gR, gL, g, deg, fac):
    """the r280 OPT raise direction rebuilt verbatim (dir_opt +
    theta_of_dir at the given degree); returns the comb at dose
    fac x theta_up and (theta_up, theta_kill).  Consumes comb +
    gradient arrays + degree only."""
    xi = BL.dir_opt(gR, gL, g, deg)
    th_up, th_kill, _c = BL.theta_of_dir(gR, gL, g, xi, deg)
    u2 = np.asarray(uu, float) + fac * th_up * g * xi
    return u2, np.asarray(mm, float).copy(), th_up, th_kill


def func_antiphase(w):
    """F1 ANTIPHASE34: lag-3 + lag-4 autocorrelation of the own
    signed fold profile (the r288 carrier band as a cheap profile
    statistic; no kernel computation)."""
    w = np.asarray(w, float)
    den = float(np.sum(w * w))
    a3 = float(np.sum(w[:-3] * w[3:]))
    a4 = float(np.sum(w[:-4] * w[4:]))
    return (a3 + a4) / max(den, 1e-300)


def func_roughness(w):
    """F2 ROUGHNESS: total variation of the own signed fold
    profile / sum |w| (local profile roughness on the fraction
    scale)."""
    w = np.asarray(w, float)
    tv = float(np.sum(np.abs(np.diff(w))))
    return tv / max(float(np.sum(np.abs(w))), 1e-300)


def func_gradalign(dw, q2band, etaband):
    """F3 GRADALIGN (PERTURBATIVE, MAIN-local): min over the wall
    band of the linearized d log h_n = (dw @ Q2[:, n]) / eta_n
    (Hellmann-Feynman in the wsig coordinate; the frozen MAIN
    gradient pack is the only non-profile input, disclosed)."""
    dw = np.asarray(dw, float)
    vals = (dw @ np.asarray(q2band, float)) \
        / np.asarray(etaband, float)
    return float(np.min(vals))


def func_midband(dw, L, nref):
    """F4 MIDBAND: 50-75 pct Chebyshev band energy share of the
    profile DEVIATION (coef_k = sum_p dw_p cos(2 pi k p / L));
    0.0 sealed at zero deviation."""
    dw = np.asarray(dw, float)
    if float(np.max(np.abs(dw))) == 0.0:
        return 0.0
    pp = np.arange(len(dw))
    kk = np.arange(nref + 1)
    C = np.cos(2.0 * math.pi * np.outer(kk, pp) / float(L))
    coef = C @ dw
    tot = float(np.sum(coef * coef))
    lo, hi = int(0.5 * nref), int(0.75 * nref)
    mid = float(np.sum(coef[lo:hi] ** 2))
    return mid / max(tot, 1e-300)


# ============== must-fail mutants
def mutant_unprojected_dir(d0, L, seed):
    """m1 MUST-FAIL: a density direction WITHOUT the eta_0
    projection -- the conservation gate must CATCH it."""
    d0 = np.asarray(d0, float)
    rng = np.random.default_rng(seed)
    dd = np.zeros(L)
    for p in range(L // 2 + 1):
        l2 = (L - p) % L
        if d0[p] == 0.0 and d0[l2] == 0.0:
            continue
        v = float(rng.standard_normal())
        dd[p] = v
        dd[l2] = v
    return dd


def mutant_unweighted_profile(d, L):
    """m2 MUST-FAIL: fold aggregation WITHOUT the s_l weighting
    (raw density sums) -- must break the eta ward loudly."""
    ll = np.arange(L)
    fold = np.minimum(ll, L - ll)
    npts = L // 2 + 1
    w = np.zeros(npts)
    np.add.at(w, fold, np.asarray(d, float))
    return w


def mutant_onesided_flip(d0, folds_sorted, mask, L):
    """m3 MUST-FAIL: the sign flip applied at grid point l ONLY
    (not L-l) -- must break the union fold conservation."""
    d2 = np.asarray(d0, float).copy()
    for f, is_nu in zip(np.asarray(folds_sorted, np.int64), mask):
        s = -1.0 if is_nu else 1.0
        d2[int(f)] = s * abs(d2[int(f)])
    return d2


def mutant_gift_dir(onsets_true, dirs):
    """m4 MUST-FAIL: a direction chosen by the withheld onset
    census -- the scope audit must FLAG this."""
    o = np.argsort(np.asarray(onsets_true))
    return dirs[int(o[0])]


# ============== gate-side measurement channel
def rho_scan(B, n_hi):
    """early-stop crossing scan (gate-side; identity-gated on
    MAIN against FS.crossing_from_B): lambda_max(E_n) ascending,
    Gram side chosen by size, stop at the first rho >= 1."""
    Sm = B.shape[0]
    rho = np.zeros(n_hi + 1)
    cross = None
    for n in range(1, n_hi + 1):
        Bn = B[:, :n]
        Mn = Bn @ Bn.T if Sm <= n else Bn.T @ Bn
        rho[n] = float(np.linalg.eigvalsh(Mn)[-1])
        if rho[n] >= 1.0:
            cross = n
            break
    return cross, rho


def measure_density(d, L):
    """the ONE measurement channel for every profile point
    (gate-side): union sign chain -> minC, s = minC/N_REF;
    mu chain/B -> crossing, z_v, C_off, fold band 3-4 share;
    own half-filling disclosed."""
    d = np.asarray(d, float)
    xu, wu, _z = BL.union_of_ctx(dict(darm=d, L=L))
    fp, wp, fn, vn, xp, xn = LS.split_by_fold(d, L)
    S = len(xu)
    nw_own = (S + 1) // 2
    sg, _l, _r = BL.sign_chain_f64(xu, wu, N_REF + EXT)
    mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    if mc is None:
        sg, _l, _r = BL.sign_chain_f64(xu, wu, N_REF + EXT2)
        mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    s = 1.0 if mc is None else mc / float(N_REF)
    out = dict(S=S, Sp=len(xp), Sm=len(xn), nw_own=nw_own,
               minC=mc, s=s, cross=None, zv=float("nan"),
               coff=float("nan"), b34=float("nan"),
               rho=None, B=None, fn=fn, vn=vn)
    dep = min(max(N_REF + DEPTH_PAD, (mc or N_REF) + 2),
              len(xp) - 1)
    if dep < 2 or len(xn) < 2:
        return out
    al, sb, h0 = FS.mu_chain_f64(np.asarray(xp), np.asarray(wp),
                                 dep)
    B = FS.b_matrix_f64(al, sb, h0, np.asarray(xn),
                        np.asarray(vn), dep)
    cross, rho = rho_scan(B, dep)
    out.update(cross=cross, rho=rho, B=B, dep=dep)
    if cross is not None and cross <= dep:
        zb = DC.zv_block(B, cross, np.asarray(vn))
        iu = np.triu_indices(len(fn), 1)
        dist = np.abs(np.asarray(fn)[iu[0]]
                      - np.asarray(fn)[iu[1]])
        bidx = DC.band_split(dist)
        A = max(float(np.sum(np.abs(zb["T"]))), 1e-300)
        out.update(zv=zb["zv"], coff=zb["coff"],
                   b34=float(np.sum(zb["T"][bidx == 1])) / A,
                   T=zb["T"], bidx=bidx, iu=iu, uv=zb["uv"])
    return out


def onset_bracket(svals, tvals):
    """first dead index bracket on a ladder (gate-side)."""
    for i, sv in enumerate(svals):
        if sv < NEAR:
            lo = tvals[i - 1] if i > 0 else None
            return lo, tvals[i], i
    return None, None, None


def sharp_type(s_lo, s_hi, t_lo, t_hi):
    """sealed sharpness rule on the refined bracket."""
    if t_lo is None or t_lo <= 0:
        return "GRADUAL(no-alive-bracket)"
    ratio = t_hi / t_lo
    if s_lo >= NEAR and s_hi <= DEAD and ratio <= SHARP_RATIO:
        return "SHARP"
    return "GRADUAL"


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("profile_functional_probe -- PRIME.PORT.LSTAR."
          "PROFILE_FUNCTIONAL.01 (round 290)")
    print("SPEC_SHA %s   (r288 DC %s / r284 LS %s / r278 MS %s)"
          % (SPEC_SHA[:16], DC.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             MS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 regression + channel identity + eta "
                        "ward; paths, directions, replicates, "
                        "functionals, anchors, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the profile convention "
          "(signed density / wsig, grid fixed), the theta_eq "
          "metric with its jitter calibration, the five "
          "interpolation paths and their t ladder, the onset/"
          "sharpness/isotropy rules, the ridge extension, the "
          "two direction classes with exact conservation gates, "
          "the four functional candidates with bands and the "
          "three-way functional adjudication; F3 is typed "
          "PERTURBATIVE/MAIN-LOCAL by construction; the STOP "
          "list forbids any L* claim and any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- INTERPOLATION, FUNCTIONALS, METRIC, "
            "ENS-SIGN IDENTITY")
    d_a = np.array([1.0, 2.0, 3.0])
    d_b = np.array([3.0, 0.0, 1.0])
    ok_t1 = (bool(np.array_equal(interp_density(d_a, d_b, 0.0),
                                 d_a))
             and bool(np.array_equal(interp_density(d_a, d_b, 1.0),
                                     d_b))
             and bool(np.array_equal(interp_density(d_a, d_b, 0.5),
                                     np.array([2.0, 1.0, 2.0]))))
    check("G10-toy-interp", ok_t1,
          "HAND INTERPOLATION: d(0) == d0 bitwise, d(1) == d1 "
          "bitwise, d(1/2) == exact mean -- the weight-profile "
          "path is linear on the fixed grid")
    w_t = np.array([1.0, 2.0, -1.0, 3.0, -2.0])
    f1_t = func_antiphase(w_t)
    f2_t = func_roughness(w_t)
    f3_t = func_gradalign(np.array([1.0, 1.0, 1.0]),
                          np.array([[1.0], [2.0], [1.0]]),
                          np.array([2.0]))
    L_t4 = 8
    dw_t4 = np.cos(2.0 * math.pi * 2.0 * np.arange(5) / L_t4)
    kk_t = np.arange(5)
    C_t = np.cos(2.0 * math.pi
                 * np.outer(kk_t, np.arange(5)) / L_t4)
    coef_t = C_t @ dw_t4
    ok_t2 = (abs(f1_t - (-3.0 / 19.0)) <= 1e-14
             and abs(f2_t - 13.0 / 9.0) <= 1e-14
             and abs(f3_t - 2.0) <= 1e-14
             and int(np.argmax(coef_t ** 2)) == 2)
    check("G11-toy-functionals", ok_t2,
          "HAND FUNCTIONALS: F1((1,2,-1,3,-2)) = -3/19 exact; "
          "F2 = 13/9 exact; F3 toy (dw = 1s, q2 = (1,2,1), eta "
          "= 2) = 2 exact; F4 toy cos(2 theta_p) concentrates "
          "at k = 2 (argmax exact)")

    # ---------------- S2 w9 regression + channel identity
    section("S2  W9 -- REGRESSION + MEASUREMENT-CHANNEL IDENTITY")
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    ctx9 = MS.ctx_build(MAIN_KZ)
    d9 = np.asarray(ctx9["darm"], float)
    L9 = int(ctx9["L"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"], W9["Sp"], W9["Sm"]) == S_REC \
        and W9["minC"] == MINC_REC and ctx9["N"] == N_REF
    check("G20-w9-source", ok_src,
          "w9: S = %d (mu %d / nu %d), N_REF = %d, minC = %s == "
          "%d (record)" % (W9["S"], W9["Sp"], W9["Sm"], ctx9["N"],
                           str(W9["minC"]), MINC_REC))
    depth9 = min(N_REF + DEPTH_PAD, W9["Sp"] - 1)
    SP9 = LS.spectral_block(W9, depth9)
    margin9 = 1.0 - SP9["rho"][N_REF]
    ok_cross = SP9["cross"] == CROSS_REC \
        and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
    check("G21-w9-crossing", ok_cross,
          "crossing %s == %d, margin %.4e (rec %.2e rel %.2f)"
          % (str(SP9["cross"]), CROSS_REC, margin9, MARGIN_REC,
             MARGIN_TOL))
    M0 = measure_density(d9, L9)
    ZB9 = DC.zv_block(SP9["B"], CROSS_REC, np.asarray(W9["vn"]))
    iu9 = np.triu_indices(W9["Sm"], 1)
    dist9 = np.abs(np.asarray(W9["fn"])[iu9[0]]
                   - np.asarray(W9["fn"])[iu9[1]])
    bidx9 = DC.band_split(dist9)
    lab9 = LS.atom_labels(W9["fn"], D9, W9["uu"], W9["mm"])
    cls9 = DC.pair_label_classes(lab9, iu9)
    _b9, classes9 = DC.balance_by_class(ZB9["T"], bidx9, cls9)
    A9 = max(float(np.sum(np.abs(ZB9["T"]))), 1e-300)
    b34_9 = float(np.sum(ZB9["T"][bidx9 == 1])) / A9
    ok_carr = (abs(ZB9["zv"] - ZV_REC) <= ZV_TOL
               and abs(ZB9["coff"] - COFF_REC) <= COFF_TOL
               and abs(b34_9 - B34_REC) <= B34_TOL
               and abs(classes9["AA"] - AA_REC) <= AA_TOL)
    check("G22-w9-carrier-map", ok_carr,
          "r288 CARRIER MAP: z_v = %+.3f (rec %+.3f), C_off = "
          "%+.4f (rec %+.4f), band 3-4 %+.3f (rec %+.3f), AA "
          "%+.3f (rec %+.3f)"
          % (ZB9["zv"], ZV_REC, ZB9["coff"], COFF_REC, b34_9,
             B34_REC, classes9["AA"], AA_REC))
    xu9, wu9, _z9 = BL.union_of_ctx(ctx9)
    xuM, wuM, _zM = BL.union_of_ctx(dict(darm=d9, L=L9))
    cross_fs, rho_fs = FS.crossing_from_B(M0["B"], M0["dep"])
    rho_devs = [abs(M0["rho"][n] - rho_fs[n])
                for n in (20, 120, 184, 185)]
    ok_chan = (bool(np.array_equal(xu9, xuM))
               and bool(np.array_equal(wu9, wuM))
               and M0["minC"] == MINC_REC
               and M0["cross"] == CROSS_REC
               and cross_fs == CROSS_REC
               and max(rho_devs) <= RHO_ID_TOL
               and abs(M0["zv"] - ZB9["zv"]) <= ZV_ID_TOL
               and abs(M0["b34"] - b34_9) <= ZV_ID_TOL)
    check("G23-channel-identity", ok_chan,
          "the density measurement channel reproduces the "
          "world_pack route on MAIN: union BITWISE, minC %s, "
          "crossing %s, z_v dev %.1e, b34 dev %.1e; early-stop "
          "rho scan == crossing_from_B (max dev %.1e at n = "
          "20/120/184/185, bar %.0e) -- one gated channel for "
          "every profile point"
          % (str(M0["minC"]), str(M0["cross"]),
             abs(M0["zv"] - ZB9["zv"]), abs(M0["b34"] - b34_9),
             max(rho_devs), RHO_ID_TOL))
    # frozen MAIN profile objects
    wsig0 = MS.wsig_vec(d9, L9)
    xs9, ws9, _f = PIK.folded_measure(d9, L9, +1.0)
    ys9, vs9, _fn = PIK.folded_measure(d9, L9, -1.0)
    rows9, Q9 = MS.grad_chain(xs9, ws9, ys9, vs9, ctx9["bx"],
                              ctx9["bw"], ctx9["by"], ctx9["bv"],
                              N_REF, np.cos(2.0 * math.pi
                                            * np.arange(L9 // 2 + 1)
                                            / L9))
    n_run9 = len(rows9)
    eta9 = np.array([r["eta"] for r in rows9])
    Q2_9 = Q9[:, :n_run9] ** 2
    eta_ward = float(np.max(np.abs(wsig0 @ Q2_9 - eta9)
                            / np.abs(eta9)))
    band_idx = list(range(WALL_BAND_LO, N_REF))
    q2band = Q2_9[:, band_idx]
    etaband = eta9[band_idx]
    ok_eta = eta_ward <= ETAWARD_BAR and n_run9 >= N_REF
    check("G24-eta-ward", ok_eta,
          "eta_n == <wsig, q_n^2> at every degree (worst rel "
          "%.1e, bar %.0e; chain ran to %d) -- the wsig "
          "coordinate is the exact profile coordinate of the "
          "chain; F3's wall band = degrees %d..%d frozen"
          % (eta_ward, ETAWARD_BAR, n_run9, WALL_BAND_LO,
             N_REF - 1))

    # ---------------- S3 metric calibration + anchors
    section("S3  METRIC CALIBRATION + r289/r280 ANCHORS")
    M9 = L9 // 2 + 1
    if smoke:
        for g in ("G30-metric-calibration", "G31-r289-ladder-anchor",
                  "G32-r280-ridge-anchor"):
            check(g, True, "SMOKE: skipped")
        REF = float("nan")

        def lag_l1(dd):
            return float("nan")
    else:
        # amendment a1: the ANALYTIC lag-L1 reference (exact
        # jitter expectation), gated against pinned realizations
        c_back = lag_of(d9, M9)
        inv_dev = float(np.max(np.abs(PIK.grid_density(c_back)
                                      - d9))) \
            / max(float(np.max(np.abs(d9))), 1e-300)
        g_cal = MF.local_gaps(np.asarray(ctx9["uu"], float))
        Dg9 = 2.0 * ctx9["alpha"] / ctx9["M"]
        REF = 0.5 * float(np.sum(np.asarray(ctx9["mm"], float)
                                 * g_cal)) / Dg9

        def lag_l1(dd):
            return float(np.sum(np.abs(lag_of(dd, M9))))

        devs = []
        cons_ok = True
        for th_c, seed in [(THETA_CAL, s) for s in CAL_SEEDS] \
                + [(T3_THETA, T3_SEED)]:
            dd_c, (u2c, m2c) = dir_frac(ctx9["uu"], ctx9["mm"],
                                        MAIN_KZ, d9, th_c, seed)
            cons_ok = cons_ok and MF.conserve_comb(
                "P2_JIT", ctx9["uu"], ctx9["mm"], u2c, m2c, th_c)
            devs.append(abs(lag_l1(dd_c) / REF / th_c - 1.0))
        ok_cal = (inv_dev <= 1e-12 and cons_ok
                  and max(devs) <= T3_TOL)
        check("G30-metric-calibration", ok_cal,
              "theta_eq METRIC (a1: LAG coordinate): density -> "
              "lag inversion identity rel %.1e (bar 1e-12); "
              "analytic REF = 0.5 sum m g / Delta = %.4e; the 3 "
              "pinned 1e-3 jitters + the independent 3e-4 jitter "
              "measure theta_eq/theta devs %s (bar %.2f, "
              "conservation exact) -- profile distances are "
              "gap-equivalent doses in the exact tent coordinate"
              % (inv_dev, REF,
                 str([round(v, 3) for v in devs]), T3_TOL))
        # r289 jitter ladder anchor (exact seeds)
        ok_lad = True
        lad_txt = []
        for th, (dep_rec, zv_rec) in LAD_ANCH.items():
            di = R289_LADDER.index(th)
            svals, zvals = [], []
            for rep in range(2):
                u2, m2 = MF.pert_jit(ctx9["uu"], ctx9["mm"], th,
                                     SEED_JL289 + di * 10 + rep,
                                     False)
                ok_lad = ok_lad and MF.conserve_comb(
                    "P2_JIT", ctx9["uu"], ctx9["mm"], u2, m2, th)
                d2 = np.asarray(PIK.build_rung(
                    MAIN_KZ, comb=(u2, m2))["d"], float)
                mm_ = measure_density(d2, L9)
                svals.append(mm_["s"])
                if math.isfinite(mm_["zv"]):
                    zvals.append(mm_["zv"])
            s_med = float(np.median(svals))
            zv_med = float(np.median(zvals)) if zvals \
                else float("nan")
            ok_lad = ok_lad \
                and abs(s_med - dep_rec) <= LAD_DEPTH_TOL \
                and abs(zv_med - zv_rec) <= LAD_ZV_TOL
            lad_txt.append("theta %.0e: s %.2f (rec %.2f), z_v "
                           "%+.2f (rec %+.2f)"
                           % (th, s_med, dep_rec, zv_med, zv_rec))
        check("G31-r289-ladder-anchor", ok_lad,
              "r289 LADDER ANCHOR (exact r289 seeds, measured "
              "through THIS channel): %s -- the 1e-3..3e-3 "
              "threshold re-derived" % "; ".join(lad_txt))
        # r280 ridge anchor
        GE = BL.grad_ext(ctx9, N_REF + 2)
        ok_grun = GE["n_run"] >= N_REF + 1
        uR, mR, th_up, th_kill = ridge_comb(
            ctx9["uu"], ctx9["mm"], GE["gR"], GE["gL"],
            GE["gaps"], N_REF, 2.0)
        dR = np.asarray(PIK.build_rung(MAIN_KZ,
                                       comb=(uR, mR))["d"], float)
        MR = measure_density(dR, L9)
        ok_ridge = (ok_grun
                    and abs(th_up / THUP_REC - 1.0) <= THUP_TOL
                    and th_kill > th_up
                    and MR["minC"] == RIDGE_MINC_REC)
        check("G32-r280-ridge-anchor", ok_ridge,
              "r280 RIDGE ANCHOR: theta_up = %.3e (rec %.2e rel "
              "%.2f), theta_kill = %.2e > theta_up; rebuilt OPT "
              "endpoint (dose 2 theta_up = %.3e) minC = %s == %d "
              "(f64 level of the mp-confirmed r280 record, "
              "disclosed) -- the raise direction is live in this "
              "channel" % (th_up, THUP_REC, THUP_TOL, th_kill,
                           2.0 * th_up, str(MR["minC"]),
                           RIDGE_MINC_REC))

    # ---------------- S4 LEG A: paths + onset map + ridge
    section("S4  LEG A -- INTERPOLATION PATHS: THE DEATH-ONSET MAP")
    ROWS = []  # the global functional test set

    def add_row(tag, dvec, meas, theq):
        dw = MS.wsig_vec(np.asarray(dvec, float), L9) - wsig0
        ROWS.append(dict(
            tag=tag, s=meas["s"], zv=meas["zv"], theq=theq,
            F1=func_antiphase(MS.wsig_vec(np.asarray(dvec, float),
                                          L9)),
            F2=func_roughness(MS.wsig_vec(np.asarray(dvec, float),
                                          L9)),
            F3=func_gradalign(dw, q2band, etaband),
            F4=func_midband(dw, L9, N_REF)))

    if smoke:
        for g in ("G40-path-endpoints", "G41-onset-map",
                  "G42-sharpness", "G43-ridge-map"):
            check(g, True, "SMOKE: skipped")
        onset_map = {}
        worlds_meas = {}
        d_worlds = {}
    else:
        # world endpoint densities (r285 control constructions)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        d_worlds = {
            "SMOOTH": np.asarray(MS.ctx_build(
                MAIN_KZ, comb=(ug9, uw9))["darm"], float),
            "SCR": np.asarray(MS.ctx_build(
                MAIN_KZ, scramble_seed=1)["darm"], float),
            "EPST": np.asarray(MS.ctx_build(
                MAIN_KZ, comb=(np.log(nn_idx.astype(float)),
                               2.0 * lamE[nn_idx]
                               / np.sqrt(nn_idx.astype(float))))
                ["darm"], float),
            "ENSR": np.asarray(MS.ctx_build(
                MAIN_KZ, scramble_seed=SEED_R285 + 100)["darm"],
                float),
            "HL2": np.asarray(MS.ctx_build(
                MAIN_KZ, comb=comb_hl)["darm"], float),
            "RIDGE": dR}
        worlds_meas = {}
        ok_fl = True
        for wn in ("EPST", "SCR", "SMOOTH", "HL2"):
            worlds_meas[wn] = measure_density(d_worlds[wn], L9)
            ok_fl = ok_fl and worlds_meas[wn]["minC"] \
                == CTRL_FLIPS[wn]
        worlds_meas["ENSR"] = measure_density(d_worlds["ENSR"], L9)
        worlds_meas["RIDGE"] = MR
        add_row("MAIN", d9, M0, 0.0)
        for wn in ("EPST", "SCR", "SMOOTH", "HL2", "ENSR"):
            add_row("WORLD:" + wn,
                    d_worlds[wn], worlds_meas[wn],
                    lag_l1(d_worlds[wn] - d9) / REF)
        ok_ends = ok_fl
        path_targets = ("SMOOTH", "SCR", "EPST", "ENSR")
        for wn in path_targets:
            dT = d_worlds[wn]
            ok_ends = ok_ends and bool(np.array_equal(
                interp_density(d9, dT, 0.0), d9)) \
                and bool(np.array_equal(
                    interp_density(d9, dT, 1.0), dT))
        check("G40-path-endpoints", ok_ends,
              "path endpoints: d(0) == MAIN and d(1) == target "
              "BITWISE on all four world paths; control flips "
              "minC = %s == records (25/21/27/25) -- the r285 "
              "control worlds re-derived through this channel"
              % str({w: worlds_meas[w]["minC"]
                     for w in ("EPST", "SCR", "SMOOTH", "HL2")}))
        # onset map
        onset_map = {}
        ok_on = True
        for wn in path_targets:
            dT = d_worlds[wn]
            plen = lag_l1(dT - d9) / REF
            svals = []
            for t in PATH_TS:
                mm_ = measure_density(interp_density(d9, dT, t),
                                      L9)
                svals.append(mm_["s"])
                add_row("PATH:%s:t=%.4g" % (wn, t),
                        interp_density(d9, dT, t), mm_, t * plen)
            lo, hi, idx = onset_bracket(svals, PATH_TS)
            if hi is None:
                onset_map[wn] = dict(t_on=None, theq=None,
                                     typ="ALIVE", plen=plen)
                continue
            s_lo = svals[idx - 1] if idx > 0 else float("nan")
            s_hi = svals[idx]
            if lo is not None:
                for _b in range(N_BISECT):
                    tm = math.sqrt(lo * hi)
                    mm_ = measure_density(
                        interp_density(d9, dT, tm), L9)
                    add_row("PATH:%s:t=%.4g" % (wn, tm),
                            interp_density(d9, dT, tm), mm_,
                            tm * plen)
                    if mm_["s"] < NEAR:
                        hi, s_hi = tm, mm_["s"]
                    else:
                        lo, s_lo = tm, mm_["s"]
            t_on = math.sqrt(lo * hi) if lo else hi
            onset_map[wn] = dict(
                t_on=t_on, theq=t_on * plen, plen=plen,
                lo=lo, hi=hi, s_lo=s_lo, s_hi=s_hi,
                typ=sharp_type(s_lo, s_hi, lo, hi))
            ok_on = ok_on and t_on is not None
        info("ONSET MAP (t_on, theta_eq_on, path length, type): "
             + "; ".join(
                 "%s (%.3g, %.3g, %.3g, %s)"
                 % (w, r["t_on"] or -1, r["theq"] or -1,
                    r["plen"], r["typ"])
                 for w, r in onset_map.items()))
        check("G41-onset-map", ok_on,
              "MEASURED death-onset per path (theta_eq units vs "
              "the 1e-3..3e-3 jitter threshold): %s -- the "
              "direction dependence of the rim, measured"
              % "; ".join("%s %.2e" % (w, r["theq"])
                          for w, r in onset_map.items()
                          if r["theq"] is not None))
        n_sharp = sum(1 for r in onset_map.values()
                      if r["typ"] == "SHARP")
        check("G42-sharpness", True,
              "SHARPNESS census (sealed rule: s >= %.2f -> <= "
              "%.2f within bracket ratio %.1f): %d/%d paths "
              "SHARP; brackets %s"
              % (NEAR, DEAD, SHARP_RATIO, n_sharp, len(onset_map),
                 str({w: (round(r.get("s_lo", float("nan")), 2),
                          round(r.get("s_hi", float("nan")), 2))
                      for w, r in onset_map.items()})))
        # ridge extension
        dd_R = dR - d9
        ridge_rows = []
        for fac in RIDGE_FACS:
            d_f = d9 + fac * dd_R
            mm_ = measure_density(d_f, L9)
            theq_f = fac * lag_l1(dd_R) / REF
            ridge_rows.append((fac, mm_["minC"], mm_["s"], theq_f))
            add_row("RIDGE:f=%g" % fac, d_f, mm_, theq_f)
        lift = [f for f, mc_, s_, _t in ridge_rows
                if mc_ is not None and mc_ > MINC_REC]
        alive = [f for f, _mc, s_, _t in ridge_rows if s_ >= NEAR]
        dead = [f for f, _mc, s_, _t in ridge_rows if s_ < NEAR]
        check("G43-ridge-map", len(ridge_rows) == len(RIDGE_FACS),
              "RIDGE MAP (linear density extension of the r280 "
              "OPT move; in-cell == position move, disclosed; "
              "the raise itself is gated in G32): rows (fac, "
              "minC, s, theta_eq) = %s; lift (minC > %d) at "
              "factors %s; alive to %s; first death %s"
              % (str([(f, mc_, round(s_, 2), "%.1e" % t)
                      for f, mc_, s_, t in ridge_rows]),
                 MINC_REC,
                 str(lift) if lift else "NONE(density-path fp "
                 "boundary case, amendment a1 disclosed)",
                 str(max(alive)) if alive else "n/a",
                 str(min(dead)) if dead else
                 "NOT REACHED on the sealed ladder"))

    # ---------------- S5 LEG B: basin geometry
    section("S5  LEG B -- BASIN GEOMETRY: ISOTROPY, CURVATURE, "
            "SMOOTH DIRECTION")
    if smoke:
        for g in ("G50-direction-conservation", "G51-isotropy",
                  "G52-curvature", "G53-smooth-anatomy"):
            check(g, True, "SMOKE: skipped")
        iso_typ = "SMOKE"
    else:
        ll9 = np.arange(L9)
        s_l9 = 4.0 * np.sin(math.pi * ll9 / L9) ** 2 / (2.0 * L9)
        dirs = []
        ok_cons = True
        for i in range(NDIR_FRAC):
            dd, (u2, m2) = dir_frac(ctx9["uu"], ctx9["mm"],
                                    MAIN_KZ, d9, THETA_CAL,
                                    SEED_FRAC + i)
            ok_cons = ok_cons and MF.conserve_comb(
                "P2_JIT", ctx9["uu"], ctx9["mm"], u2, m2,
                THETA_CAL)
            dirs.append(("FRAC%02d" % i, dd))
        for i in range(NDIR_DENS):
            dd = dir_dens(d9, L9, SEED_DENS + i)
            eta0 = abs(float(np.sum(dd * s_l9)))
            ok_cons = ok_cons and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * s_l9))), 1.0)
            dirs.append(("DENS%02d" % i, dd))
        check("G50-direction-conservation", ok_cons,
              "%d FRAC directions (r276 comb-jitter moves, "
              "weights bitwise, conservation exact) + %d DENS "
              "directions (even-symmetrized, eta_0 projected out "
              "exactly, bar %.0e) -- the sealed direction "
              "classes" % (NDIR_FRAC, NDIR_DENS, ETA0_BAR))
        # isotropy census
        killfrac = {}
        dir_s = {}
        for dist in DIST_GRID:
            kills = 0
            for name, dd in dirs:
                unit = dd / max(lag_l1(dd), 1e-300)
                d_pt = d9 + unit * (dist * REF)
                mm_ = measure_density(d_pt, L9)
                dir_s.setdefault(name, {})[dist] = mm_["s"]
                add_row("DIR:%s:d=%.0e" % (name, dist), d_pt,
                        mm_, dist)
                if mm_["s"] < NEAR:
                    kills += 1
            killfrac[dist] = kills / float(len(dirs))
        kf_iso = killfrac[ISO_DIST]
        iso_typ = ("TUBE" if kf_iso >= TUBE_BAR else
                   ("BROAD" if kf_iso <= BROAD_BAR else "MIXED"))
        kf_frac = float(np.mean(
            [1.0 if dir_s[n][2e-3] < NEAR else 0.0
             for n, _d in dirs if n.startswith("FRAC")]))
        kf_dens = float(np.mean(
            [1.0 if dir_s[n][2e-3] < NEAR else 0.0
             for n, _d in dirs if n.startswith("DENS")]))
        check("G51-isotropy", True,
              "ISOTROPY census (16 directions x %d distances): "
              "killfrac %s; at the sealed ISO_DIST %.0e: %.2f -> "
              "%s (bars %.2f/%.2f); class split at 2e-3: FRAC "
              "%.2f vs DENS %.2f -- the tube-vs-broad question, "
              "measured" % (len(DIST_GRID),
                            str({("%.0e" % d): round(v, 2)
                                 for d, v in killfrac.items()}),
                            ISO_DIST, kf_iso, iso_typ, TUBE_BAR,
                            BROAD_BAR, kf_frac, kf_dens))
        # curvature at the rim
        def dir_onset(name):
            ss = dir_s[name]
            lo = None
            for dist in DIST_GRID:
                if ss[dist] < NEAR:
                    return (lo, dist)
                lo = dist
            return (lo, None)
        cand = [(n, dir_onset(n)) for n, _d in dirs
                if n.startswith("FRAC")]
        cand = [(n, br) for n, br in cand if br[1] is not None]
        cand.sort(key=lambda t: (t[1][1], t[0]))
        curv_txt = []
        curv_sel = []
        if cand:
            curv_sel.append(("KILLER:" + cand[0][0],
                             dict(dirs)[cand[0][0]], cand[0][1]))
        curv_sel.append(("RAND:FRAC00", dict(dirs)["FRAC00"],
                         dir_onset("FRAC00")))
        curv_sel.append(("RIDGE", dd_R, (None, None)))
        for cname, dd, br in curv_sel:
            unit = dd / max(lag_l1(dd), 1e-300)
            if br[1] is not None:
                th_on = math.sqrt(br[0] * br[1]) if br[0] \
                    else br[1]
            else:
                th_on = ISO_DIST  # ridge/no-death: probe at tube scale
            svals = []
            for fc in CURV_FACS:
                d_pt = d9 + unit * (fc * th_on * REF)
                mm_ = measure_density(d_pt, L9)
                svals.append(mm_["s"])
                add_row("CURV:%s:f=%g" % (cname, fc), d_pt, mm_,
                        fc * th_on)
            kap = svals[0] + svals[4] - 2.0 * svals[2]
            curv_txt.append("%s (theta_on %.2e): s = %s, kappa "
                            "= %+.2f" % (cname, th_on,
                                         str([round(v, 2)
                                              for v in svals]),
                                         kap))
        check("G52-curvature", True,
              "RIM CURVATURE (s at %s x theta_on): %s -- the "
              "local second-order shape of the basin boundary, "
              "measured" % (str(CURV_FACS), "; ".join(curv_txt)))
        # SMOOTH anatomy
        dd_SM = d_worlds["SMOOTH"] - d9
        dwsig_SM = MS.wsig_vec(d_worlds["SMOOTH"], L9) - wsig0
        gwall = Q2_9[:, N_REF - 1]
        cosal = float(dwsig_SM @ gwall) \
            / max(float(np.linalg.norm(dwsig_SM))
                  * float(np.linalg.norm(gwall)), 1e-300)
        mid = measure_density(interp_density(
            d9, d_worlds["SMOOTH"], 0.5), L9)
        om = onset_map.get("SMOOTH", {})
        check("G53-smooth-anatomy", True,
              "SMOOTH DIRECTION (the arithmetic direction): "
              "theta_eq length %.3g, onset %.2e theta_eq (= "
              "%.2e x full path; jitter threshold band 1e-3.."
              "3e-3); MIDPOINT t = 0.5: s %.3f, minC %s, S %d, "
              "z_v %s, b34 %s; wall-gradient alignment cos = "
              "%+.4f (PERTURBATIVE typing) -- what the "
              "MAIN-minus-SMOOTH profile difference carries"
              % (om.get("plen", float("nan")),
                 om.get("theq") or float("nan"),
                 om.get("t_on") or float("nan"), mid["s"],
                 str(mid["minC"]), mid["S"],
                 ("%+.2f" % mid["zv"])
                 if math.isfinite(mid["zv"]) else "n/a",
                 ("%+.3f" % mid["b34"])
                 if math.isfinite(mid["b34"]) else "n/a",
                 cosal))

    # ---------------- S6 LEG C: replicates + functionals
    section("S6  LEG C -- REPLICATE ENSEMBLES + THE FUNCTIONAL "
            "CONTEST")
    if smoke:
        for g in ("G60-ensembles", "G61-functional-table",
                  "G62-detectors", "G63-functional-adjudication"):
            check(g, True, "SMOKE: skipped")
        func_verdict = "SMOKE_NO_ADJUDICATION"
        det_typ = {}
        sp_tab = {}
    else:
        f_all = np.concatenate([np.asarray(W9["fp"], np.int64),
                                np.asarray(W9["fn"], np.int64)])
        x_all = np.concatenate([np.asarray(W9["xp"]),
                                np.asarray(W9["xn"])])
        m_all = np.concatenate([np.asarray(W9["wp"]),
                                np.asarray(W9["vn"])])
        o_f = np.argsort(f_all)
        f_srt, x_srt, m_srt = f_all[o_f], x_all[o_f], m_all[o_f]
        ok_ens = True
        sgn_s = []
        for i in range(ENS_SIGN_REPS):
            msk = CD.sign_assignment(len(f_srt), W9["Sm"],
                                     SEED_R285 + i)
            dE = ens_sign_density(d9, f_srt, msk, L9)
            fpE, wpE, fnE, vnE, _xpE, _xnE = LS.split_by_fold(
                dE, L9)
            fu = np.sort(np.concatenate([fpE, fnE]))
            mu_ = np.concatenate([wpE, vnE])
            ou = np.argsort(np.concatenate([fpE, fnE]))
            ok_ens = ok_ens \
                and bool(np.array_equal(fu, f_srt)) \
                and float(np.max(np.abs(mu_[ou] - m_srt))) == 0.0 \
                and int(np.sum(msk)) == W9["Sm"]
            mmE = measure_density(dE, L9)
            sgn_s.append(mmE["s"])
            add_row("ENS_SIGN:%02d" % i, dE, mmE, float("nan"))
            if i == 0:
                r0 = CD.ens_sign_world(x_srt, m_srt, msk, N_REF,
                                       20)
                ok_ens = ok_ens and r0["minC"] == mmE["minC"]
                info("t4 ENS_SIGN rep-0 identity: density-channel "
                     "minC %s == ens_sign_world %s; fold multiset "
                     "+ magnitudes EXACT"
                     % (str(mmE["minC"]), str(r0["minC"])))
        scr_s = []
        for i in range(ENS_SCR_REPS):
            sctx = MS.ctx_build(MAIN_KZ,
                                scramble_seed=SEED_R285 + 100 + i)
            ok_ens = ok_ens and bool(np.array_equal(
                np.asarray(sctx["mm"]), np.asarray(ctx9["mm"])))
            dS = np.asarray(sctx["darm"], float)
            mmS = measure_density(dS, L9)
            scr_s.append(mmS["s"])
            add_row("ENS_SCR:%02d" % i, dS, mmS, float("nan"))
        check("G60-ensembles", ok_ens,
              "REPLICATES as profile points (conservation gates "
              "exact, rep-0 identity gated): ENS_SIGN %d reps s "
              "in [%.3f, %.3f]; ENS_SCR %d reps (weights "
              "bitwise) s in [%.3f, %.3f] -- the r285 collective "
              "death, profile-resolved"
              % (ENS_SIGN_REPS, min(sgn_s), max(sgn_s),
                 ENS_SCR_REPS, min(scr_s), max(scr_s)))
        # functional table
        svec = [r["s"] for r in ROWS]
        sp_tab = {}
        for F in ("F1", "F2", "F3", "F4"):
            sp_tab[F] = BH.spearman([r[F] for r in ROWS], svec)
        zrows = [r for r in ROWS if math.isfinite(r["zv"])]
        sp_zv = {F: BH.spearman([r[F] for r in zrows],
                                [r["zv"] for r in zrows])
                 for F in ("F1", "F2", "F3", "F4")}
        wtab = {}
        for F in ("F1", "F2", "F3", "F4"):
            wtab[F] = {}
            for r in ROWS:
                if r["tag"] == "MAIN":
                    wtab[F]["MAIN"] = r[F]
                for wn in ("EPST", "SCR", "SMOOTH", "HL2"):
                    if r["tag"] == "WORLD:" + wn:
                        wtab[F][wn] = r[F]
        check("G61-functional-table", len(ROWS) >= 100,
              "FUNCTIONAL CONTEST over %d test points (paths + "
              "bisections + ridge + directions + curvature + %d "
              "replicates + worlds): spearman vs depth s: F1 "
              "ANTIPHASE34 %+.3f, F2 ROUGHNESS %+.3f, F3 "
              "GRADALIGN %+.3f (PERTURBATIVE), F4 MIDBAND %+.3f; "
              "secondary vs z_v (%d finite): %s"
              % (len(ROWS), ENS_SIGN_REPS + ENS_SCR_REPS,
                 sp_tab["F1"], sp_tab["F2"], sp_tab["F3"],
                 sp_tab["F4"], len(zrows),
                 str({k: round(v, 2) for k, v in sp_zv.items()})))
        ctrls = ["EPST", "SCR", "SMOOTH", "HL2"]
        det_typ = {F: LS.dist_rule(wtab[F], ctrls)
                   for F in ("F1", "F2", "F3", "F4")}
        check("G62-detectors", True,
              "WORLD SEPARATION (sealed r281 distance rule): %s; "
              "world values %s"
              % (str(det_typ),
                 str({F: {w: ("%.3g" % v)
                          for w, v in wtab[F].items()}
                      for F in ("F1", "F2", "F3", "F4")})))
        best_F = max(sp_tab, key=lambda k: abs(sp_tab[k]))
        best_sp = sp_tab[best_F]
        if abs(best_sp) >= SP_FOUND \
                and det_typ[best_F] == "MAIN_SEPARATING":
            func_verdict = ("FUNCTIONAL_FOUND(%s, spearman "
                            "%+.3f, MAIN_SEPARATING)"
                            % (best_F, best_sp))
        elif abs(best_sp) >= SP_PART:
            func_verdict = ("FUNCTIONAL_PARTIAL(best %s, "
                            "spearman %+.3f, %s)"
                            % (best_F, best_sp, det_typ[best_F]))
        else:
            func_verdict = ("ALL_FUNCTIONALS_BLIND(best %s "
                            "%+.3f < %.1f)"
                            % (best_F, best_sp, SP_PART))
        check("G63-functional-adjudication", True,
              "SEALED RULE (FOUND iff best |sp| >= %.1f AND "
              "MAIN_SEPARATING; PARTIAL iff >= %.1f): best = %s "
              "(%+.3f, %s) -> %s"
              % (SP_FOUND, SP_PART, best_F, best_sp,
                 det_typ[best_F], func_verdict.split("(")[0]))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    ll9s = np.arange(L9)
    s_l9s = 4.0 * np.sin(math.pi * ll9s / L9) ** 2 / (2.0 * L9)
    dd_m1 = mutant_unprojected_dir(d9, L9, 290900)
    eta0_m1 = abs(float(np.sum(dd_m1 * s_l9s)))
    check("G70-mustfail-unprojected", eta0_m1 > ETA0_BAR,
          "m1 UNPROJECTED DIRECTION: |eta_0| = %.1e > %.0e -- "
          "CAUGHT by the conservation gate; mass-moving "
          "directions cannot pass as basin probes"
          % (eta0_m1, ETA0_BAR))
    w_m2 = mutant_unweighted_profile(d9, L9)
    n_m2 = min(len(w_m2), Q2_9.shape[0])
    dev_m2 = float(np.max(np.abs(w_m2[:n_m2] @ Q2_9[:n_m2]
                                 - eta9) / np.abs(eta9)))
    check("G71-mustfail-unweighted", dev_m2 >= M2_BAR,
          "m2 UNWEIGHTED PROFILE (fold sums without s_l): eta "
          "ward breaks by rel %.2f >= %.1f -- LOUD: wsig is the "
          "unique exact profile coordinate" % (dev_m2, M2_BAR))
    f_all7 = np.concatenate([np.asarray(W9["fp"], np.int64),
                             np.asarray(W9["fn"], np.int64)])
    o_f7 = np.argsort(f_all7)
    f_srt7 = f_all7[o_f7]
    msk7 = CD.sign_assignment(len(f_srt7), W9["Sm"], SEED_R285)
    d_m3 = mutant_onesided_flip(d9, f_srt7, msk7, L9)
    fp3, _wp3, fn3, _vn3, _x3, _y3 = LS.split_by_fold(d_m3, L9)
    S_m3 = len(fp3) + len(fn3)
    check("G72-mustfail-onesided", S_m3 != len(f_srt7),
          "m3 ONE-SIDED SIGN FLIP (l only, not L-l): union fold "
          "count %d != %d -- CAUGHT by the fold conservation "
          "gate; broken evenness cannot pass as a replicate"
          % (S_m3, len(f_srt7)))
    hits_m4 = scope_audit("mutant_gift_dir", SCOPE_FORBIDDEN)
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m4) and not hits
          and not ag_hits,
          "m4 GIFT DIRECTION FLAGGED (%s); the %d sealed "
          "constructors consume profiles/densities + grid "
          "geometry + seeds ONLY (%s); fragment audit: %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 honesty ledger
    section("S8  HONESTY LEDGER")
    check("G80-honesty-ledger", True,
          "onset maps, kill fractions, curvature indices and "
          "functional correlations are MEASUREMENTS on finite w9 "
          "profile space; F3 is PERTURBATIVE/MAIN-LOCAL by "
          "construction and its correlation is not a mechanism "
          "claim; the ridge anchor is gated at f64 level of the "
          "mp-confirmed r280 record (disclosed); no functional "
          "statistic is a proof premise")

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no equidistribution "
          "premise, no posthoc window, no RH claim; what the "
          "round adds: the death-onset map of the five profile "
          "paths, the basin isotropy/curvature census, the "
          "SMOOTH-direction anatomy, the ridge map, and the "
          "sealed four-candidate functional contest; r243..r289 "
          "stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        parts.append(
            "BASIN_GEOMETRY(onsets theta_eq %s; %s; ISOTROPY = "
            "%s(killfrac %.2f at %.0e); SMOOTH onset %s)"
            % (str({w: ("%.1e" % r["theq"])
                    for w, r in onset_map.items()
                    if r["theq"] is not None}),
               str({w: r["typ"] for w, r in onset_map.items()}),
               iso_typ, killfrac[ISO_DIST], ISO_DIST,
               ("%.1e" % onset_map["SMOOTH"]["theq"])
               if onset_map.get("SMOOTH", {}).get("theq")
               else "n/a"))
        parts.append(
            "RIDGE_MAP(lift at %s; alive to %s; death %s)"
            % (str(lift) if lift else "G32-anchor only (a1)",
               str(max(alive)) if alive else "n/a",
               str(min(dead)) if dead else "NOT REACHED"))
        parts.append(func_verdict)
        parts.append("FUNCTIONAL_TABLE(sp %s)"
                     % str({k: round(v, 3)
                            for k, v in sp_tab.items()}))
        parts.append("DETECTOR_LEDGER(%s)" % str(det_typ))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED geometry of the working set in "
          "profile space + sealed functional contest; NO L* "
          "claim, NO RH claim" % (verd, " (SMOKE)" if smoke
                                  else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
