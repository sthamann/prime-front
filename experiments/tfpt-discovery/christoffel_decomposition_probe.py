#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_decomposition_probe -- PRIME.PORT.LSTAR.
CHRISTOFFEL_DECOMPOSITION.01 (round 285): the candidate-wise
DECOMPOSITION of the missing lemma L*.  r283 reduced the full
free-window question to ONE scalar (L*: lambda_max(E_{N_w}) < 1,
E = the nu-dressed mu-CD kernel; margin 1.68e-4); r284 measured
the Christoffel sandwich max_k v_k K_n(y_k) <= lambda_max(E_n)
<= trace(E_n) and found MAIN's crossing to be a NEAR-SINGLE-ATOM
event (n_DIAG = 187 vs crossing 185, coherent assist 3.1 percent,
aggregate coherence destructive slack 50x) while ALL controls die
COLLECTIVELY far below their single-atom degree.  THIS ROUND
adjudicates the decomposition perspective: L* splits into
(D) the PER-ATOM DIAGONAL CONDITION  v_k K_{N_w}(y_k) < 1 - delta
    for ALL nu atoms k (a LOCAL two-measure statement: nu mass at
    the atom against the inverse mu-Christoffel function --
    classical approximation terrain), and
(C) the COHERENCE CONDITION  assist_{N_w} =
    lambda_max/maxdiag - 1 < delta' (on MAIN 3.1 percent; the
    off-diagonal is destructive -- presumably the r272/r273
    generic cancellation);
together (exact bookkeeping) => lambda_max < 1.  On the controls
(C) fails (collective death) -- the arithmetic would then sit in
the spectral coherence of the WEIGHTS while (D) carries the
metric-local half.  NOT a proof round: no L* claim, no bound
mechanism, no asymptotic law -- exact accounting + budget tables
+ classical comparison + honest typing.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r284 discipline): w = window (kz),
S = #union entries of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = builder depth = (S+1)//2, n = degree, minC =
first n with h_n < 0, crossing = minC + 1 (r283 monotone-loading
theorem, consumed as the crossing dictionary; re-gated spectrally
on w9 + mains + all four controls + one replicate per ensemble);
f = fold index (theta_f = 2 pi f / L, x = cos theta_f).  Ground
truth (minC, flips, census offsets, r283/r284 records) enters
GATES and record tables only; the sealed constructors consume
split-source arrays (fold indices, weights, kernel matrices,
vectors, L) ONLY (AST scope audit); no zero/prime oracles
anywhere (AST firewall; atom classes via the r254 world-blind
integer root extraction ODG.base_exp).  MACHINERY IMPORTED
VERBATIM: r284 LS.{split_by_fold, atom_labels, christoffel_rows,
top_eigvecs, dist_rule, world_pack, spectral_block,
shield_profile}, r283 FS.{mu_chain_f64, b_matrix_f64,
mu_chain_mp, b_matrix_mp, crossing_from_B}, r278 MS.ctx_build,
r280 BL.{union_of_ctx, sign_chain_f64}, v881 PIK.{folded_measure,
build_rung, lambda_eps}, r243 PB.smooth_comb, paircorr PC.{Grid,
gen_model}, r254 ODG.base_exp, r244 BH.spearman, r274 WD.{stj_gen,
pv_seq}, r230 JF.{TOY_NODES, TOY_WTS}, v563 core READ-ONLY.

LEG A -- THE EXACT DECOMPOSITION BOOKKEEPING:
(a1) SEALED FORMS (both candidates, frozen): (i) MULTIPLICATIVE
  (definition-exact, trivially honest): with maxdiag_n =
  max_k v_k K_n(y_k) and assist_n = lambda_max(E_n)/maxdiag_n - 1
  we have lambda_max = maxdiag x (1 + assist) EXACTLY, hence the
  BUDGET THEOREM: maxdiag <= 1 - delta AND assist <= delta' with
  (1 - delta)(1 + delta') < 1  =>  lambda_max < 1; equivalence
  lambda_max < 1 <=> assist < 1/maxdiag - 1 (algebraic identity,
  gated at every degree).  (ii) ADDITIVE with exact remainder:
  lambda_max = maxdiag + coh with coh := lambda_max - maxdiag,
  and the Weyl bracket 0 <= coh <= lambda_max(Off(E_n)) (gated;
  its slack vs the exact remainder is the price of the additive
  bookkeeping, reported).  The Rayleigh decomposition rho =
  sum_k u_k^2 d_k + u^T Off u (diagonal part + off-diagonal
  interference of the top eigenvector) is gated exactly -- NO
  give-away sandwich anywhere.
(a2) BUDGETS OVER THE LADDER: maxdiag_{N_w} and assist_{N_w} on
  all 42 frame-A rungs (h <= 900, r281 census channel) + the
  extra mains w13/kz15: is maxdiag_{N_w} uniformly < 1 - delta
  with stable delta (min/med/max, halves medians, spearman vs N);
  is the assist uniformly small; per-rung budget-margin
  (1/maxdiag - 1) - assist > 0 <=> rho_{N_w} < 1 (gated 42/42);
  FINGERPRINT ward: |spearman| of maxdiag/assist vs the withheld
  offset minC - N_w reported, alias bar 0.9.
(a3) THE SAME BOOKKEEPING ON THE CONTROLS (EPST/SCR/SMOOTH/HL2,
  r281 channel verbatim): at their crossing degrees, where
  exactly does the budget rip -- maxdiag still < 1 but assist
  exploded?  The budget split quantified: offdiag share of the
  crossing 1 - maxdiag_cross/rho_cross.

LEG B -- THE PER-ATOM DIAGONAL (the potentially provable half):
(b1) the v_k K_n(y_k) profile over all nu atoms up to N_w + 5 on
  w9 + the sealed ladder sample (anchor rungs 12/26/40/52):
  WHICH atoms are binding (top-5 diag table with fold, u, x,
  class, primary p, v, d_{N_w}); LADDER CENSUS over all 42
  rungs: binding atom = argmax diag at N_w -- fraction ARCH,
  fraction with u < log 2 (below the first prime), fraction at
  nu-fold-rank <= 1 (the shallow edge).
(b2) THE CLASSICAL COMPARISON (typed COMPARISON_ONLY -- the
  equilibrium prediction is a comparison yardstick, NEVER a
  substitute source; r232a measured the discrete QP equilibrium
  to node accuracy only, cited): the mu-Christoffel function has
  the classical bulk asymptotic lambda_{mu,n}(y) ~ mu'(y) /
  (n omega(y)) (Mate-Nevai-Totik form; omega = arcsine
  equilibrium density of the hull 1/(pi sqrt((y-a)(b-y)))), i.e.
  K_n^cl(y) = n omega(y)/mu'_loc(y) with the sealed local
  density mu'_loc = (mu mass within R_LOC = 8 folds)/(x-width);
  soft-edge law ~ n^2.  Measured: the growth exponent p_k =
  halves log-slope of K_n(y_k) over [N_w/4, N_w] (typed
  BULK_LIKE / EDGE_LIKE by proximity to 1 vs 2) for the binding
  and a sealed bulk reference atom; the classical isolation
  degree n*_k = mu'_loc/(v_k omega(y_k)) (first n with
  v_k K^cl >= 1) for ALL nu atoms: coverage = min_k n*_k vs N_w,
  and n*_bind vs the measured n_DIAG (octave band 1.0); the same
  coverage census over the 42 rungs.
(b3) THE HONEST DETECTOR: is the per-atom condition WORLD_BLIND
  (expected YES -- the controls die at (C)): controls' maxdiag
  at n = 184 (their own N_w) measured to depth 189, their
  n_DIAG within the window; typed by measurement + the sealed
  r281 distance rule -- if blind, (D) is the metric-local,
  world-blind half and (C) carries the ENTIRE arithmetic.

LEG C -- THE COHERENCE HALF (where the arithmetic sits):
(c1) assist profiles over n and worlds: MAIN at the sealed
  degrees (20, 40, 120, 184, 185); every world at the sealed
  crossing fractions (0.25, 0.5, 0.75, 1.0) x its own crossing
  -- when do the controls become constructive-collective?
(c2) the GENERIC yardstick (r272-c3 / r273 from the other side):
  the assist is a weighted off-diagonal sum of the E kernel;
  with the NON-ADAPTIVE source vector u_v = sqrt(v)/||.|| the
  interference X_v = u_v^T Off u_v has the exact random-sign
  scale G_v = sqrt(sum_{i!=j} (u_i u_j E_ij)^2): z_v = X_v/G_v
  is the random-sign z-score (analytic, no MC), plus the
  cancellation depth C_off = X/sum|terms| (the r272 coordinate)
  and the same for the adaptive extremal vector.  Sealed typing
  at the crossing degree: MAIN_GENERIC_CTRL_OUTLIER iff
  |z_v(MAIN)| <= 3.0 AND every control |z_v| > 3.0; else
  MIXED(values).
(c3) REPLICATE ENSEMBLES around MAIN (conservation-gated):
  ENS_SIGN (16 pinned seeds): random re-assignment of the nu
  label over the union folds at FIXED positions, FIXED
  magnitude-per-fold, FIXED S_- (conservation gates bitwise);
  ENS_SCR (12 pinned seeds): the core position scramble
  (uniform u at the SAME masses -- weights bitwise identical,
  positions re-drawn).  Per replicate: crossing = minC + 1
  (r283 theorem; spectrally spot-gated on replicate 0 of each
  ensemble), assist_20, assist at own crossing, maxdiag/assist
  at own N_w.  MAIN POSITION: percentile of MAIN's assist_20
  (early, pre-crossing) and assist_cross (at the wall) in each
  ensemble; sealed typing per statistic: GENERIC iff pct in
  [0.2, 0.8], LOW_OUTLIER below, HIGH_OUTLIER above.

LEG D -- WARDS / MUST-FAILS (each loud): w9 E-construction gated
against the r283/r284 records (S = 367/263/104, N_w = 184, minC
184, crossing 185, rho records 20/120/185, top-5 eigs, margin
1.68e-4, diag max 0.9700, n_CS = 10, n_DIAG = 187, gain_Nw
1.0307, slack_Nw 50.2); mp ward (dps 60, chain + B recomputed)
on rho_184/rho_185 AND maxdiag_184 (rel bar 1e-6); controls minC
== flips 25/21/27/25 and spectral crossing == flip+1; 42-rung
census regression (anchors, offset distribution == r281,
half-filling 42/42); exact toys: (t1) HAND 2x2 (E = (1/16)
[[4,2],[2,2]]: lambda = (3+sqrt5)/16, assist = (sqrt5-1)/4,
offpart = sqrt5/20, diagpart = (15+sqrt5)/80, off-norm 1/8,
budget equivalence -- every value hand-computed); (t2) JF9
rational Christoffel cross-route (r284 route) + decomposition /
sandwich / Weyl / budget-equivalence gates at every n <= S_+,
crossing 4; (t3) toy conservation battery (legit sign ensemble
op passes the gates, hand counts).  MUST-FAILS: (m1) ASSIST
WITHOUT DIAGONAL SUBTRACTION: the mutant claiming the whole
Rayleigh quotient as off-diagonal interference must break the
exact decomposition identity by >= 0.1 rel; (m2) CHRISTOFFEL
WITHOUT WEIGHT: dropping v_k must break the exact trace identity
by >= 0.1 rel; (m3) ENSEMBLE WITHOUT CONSERVATION GATES: a
mutant surgery scaling one magnitude by 1.15 must be CAUGHT by
the conservation gate (multiset break >= 1e-3 rel); (m4) a
mutant orienting a degree by the withheld crossing is FLAGGED by
the AST scope audit.  PAIRCORR DETECTOR (sealed r281 distance
rule) on K_D1 = maxdiag_184, K_D2 = assist at own crossing,
K_C1 = z_v at own crossing, K_B1 = log10(n*_bind/N_w) (the
b2 classical statistic -- the demanded detector on the classical
arguments).  STOP LIST (anti-gates, binding): NO L* claim, NO
bound mechanism, NO asymptotic law, NO derived 5/7, NO triangle
bound as certificate, NO posthoc window, NO equilibrium
substitution (comparison only), NO RH claim; r243..r284 stand.

SEALED CONSTANTS: MAINS (9, 13, 15); MINC_OFF {9: 0, 13: 2,
15: 1}; ANCHORS {9:0, 12:2, 13:2, 26:3, 40:1, 15:1, 52:0};
R281_DIST {0:18, 1:10, 2:6, 3:6, 4:1, 5:1}; CTRL_FLIPS
{EPST:25, SCR:21, SMOOTH:27}; HL2 seed 101 flip 25; H_CAP 900;
EXT 8 / EXT2 32; DEPTH_PAD 6; CTRL_PAD 5 (controls measured to
N_w + 5 = 189); WARD_DPS 60; RHO_WARD_TOL 1e-6; ID_TOL 1e-12;
DEC_TOL 1e-10; SAND_TOL 1e-9; WEYL_TOL 1e-9; EQ_SKIP 1e-13
(|rho-1| band excluded from the equivalence sign gate);
PROF_DEGS (20, 40, 120, 184, 185); CROSS_FRACS (0.25, 0.5,
0.75, 1.0); R283_RHO {20: 0.47808, 120: 0.99898, 185: 1.00004}
tol 1e-5; R283_TOP5 (0.99983, 0.99874, 0.99597, 0.98461,
0.96408) tol 1e-4; MARGIN_REC 1.68e-4 rel tol 0.01; DIAGMAX_REC
0.9700 tol 5e-3; NCS_REC 10; NDIAG_REC 187; CROSS_REC 185;
GAIN_REC 1.0307 abs tol 5e-3; SLACK_REC 50.2 abs tol 1.0;
R_LOC 8; EDGE_U = log 2; GROWTH_FRACS (0.25, 0.5, 1.0); OCT_BAND
1.0; TOPD 5; SAMPLE_KZ (12, 26, 40, 52); BULK_REF = nu atom with
u closest to the v-weighted mean u; DET_DEG 20; A_MAIN_BAR 0.10;
A_CTRL_BAR 0.5; Z_GEN 3.0; ENS_SIGN_REPS 16; ENS_SCR_REPS 12;
SEED_BASE 285000; PCT_BAND (0.2, 0.8); M1_BAR 0.1; M2_BAR 0.1;
M3_BAR 1e-3; MUT_MASS 1.15; FP_BAR 0.9; ADMIT 1e-9; runtime
<= 1800 s; smoke = toys + firewall + scopes + mutants + w9 f64
block (decomposition, budget, per-atom, classical, MAIN assist
profile); ladder, mains, controls, ensembles, mp ward, detector
and adjudication skipped.  PRE-SPEC SCOPING (disclosed): the
r283/r284/r281 record numbers (S counts, minC offsets, flips,
rho/diag/gain/slack records) are consumed as sealed gate anchors;
the A_MAIN_BAR/A_CTRL_BAR bars quote the published r284 records
(assist 3.1 percent on MAIN; controls' maxdiag far below 1 at
crossing) -- record reading, not tuning; no machinery pass
preceded this spec except record reading; no bar, band or typing
rule was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  DECOMPOSITION_EXACT(sealed forms i/ii, delta/delta' budgets
    over the ladder, control budget split) [awarded iff every
    accounting identity gates exactly AND rho_{N_w} < 1 on
    42/42 rungs; else DECOMPOSITION_BROKEN(locus)]
  + PERATOM_CLASSICAL(binding census, classical coverage +
    octave devs, blindness status) [always]
  + [exactly one of] COHERENCE_CARRIES_ARITHMETIC(assist
    profiles, generic-vs-outlier finding, ensemble position)
    iff (D) is world-blind (all four controls' maxdiag_184 < 1)
    AND assist_cross(MAIN) <= 0.10 AND min ctrl assist_cross
    >= 0.5 / COHERENCE_UNSTRUCTURED(measured values)
  + ENSEMBLE_POSITION(early pct + wall pct per ensemble, typed)
  + DETECTOR_LEDGER [always].
Honesty before beauty: the decomposition is EXACT BOOKKEEPING of
the open scalar L*, not a proof; the budget tables are MEASURED
on 42 rungs; the classical comparison is a yardstick (its octave
deviations are findings, not certificates); no verdict claims
L*, a bound mechanism, a derived 5/7 or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 33/33 at the sealed rules
(0.3 s), calibration pass 1 = first full evaluation = 33/33,
wall 7.1 s -- NO physics bar, band, rule or verdict rule was
moved at any point; the only post-freeze edit is this record-
table insertion, which IS the protocol; run1/run2 identical up
to WALL):
CAL_VERDICT = DECOMPOSITION_EXACT(mult + additive forms exact;
ladder maxdiag max 0.9941 / assist max 0.0702; ctrl offdiag
share 0.63..0.75) + PERATOM_CLASSICAL(binding ARCH 42/42,
u < log 2 42/42; n*_bind 58 vs n_DIAG 187 oct dev 1.68;
coverage 0/42 -> CLASSICAL_GAP; (D) SEPARATES) +
COHERENCE_UNSTRUCTURED(by the sealed blind_D clause -- the
assist itself separates cleanly, see the honest reading below)
+ ENSEMBLE_POSITION(sign_early 1.00 HIGH_OUTLIER, sign_wall
0.00 LOW_OUTLIER, scr_early 0.75 GENERIC, scr_wall 0.00
LOW_OUTLIER) + DETECTOR_LEDGER(K_D1 WORLD_BLIND / K_D2
MAIN_SEPARATING / K_C1 MAIN_SEPARATING / K_B1 WORLD_BLIND).
Key numbers.  W9 BOOKKEEPING (depth 190): multiplicative
identity dev 1.8e-16, Rayleigh decomposition dev 2.0e-15,
budget equivalence sign-exact at every degree, Weyl bracket
holds; at N_w: maxdiag 0.97001 (delta 0.02999), assist 0.03074,
budget margin (1/maxdiag - 1) - assist = +1.727e-4 > 0 <=>
margin 1 - rho = 1.675e-4; additive remainder coh 0.02982 vs
Weyl off-norm 0.31667 (slack 0.287: the additive bookkeeping is
coarse, the multiplicative form is the honest one).  MP WARD
(dps 60): rho_184 = 0.99983248 < 1 < 1.00003660 = rho_185,
maxdiag_184 dev 1.6e-13 (bar 1e-6).  LADDER BUDGETS (42 rungs,
at N_w): maxdiag min/med/max 0.9343/0.9792/0.9941 (max kz38,
delta_min 0.0059), halves med 0.970 -> 0.986, sp(N, maxdiag)
+0.65 -- THE TREND FINDING: the per-atom budget TIGHTENS toward
1 with N; assist min/med/max 0.0059/0.0212/0.0702 (max kz12),
halves 0.031 -> 0.014, sp(N, assist) -0.65 -- the coherent
assist SHRINKS with N: the budget split shifts toward the
diagonal with depth (delta is NOT uniform-stable; no L* budget
with fixed delta/delta' is supported by the measured trend --
a quantified, falsifiable statement, no asymptotic law
claimed); budget margin > 0 and rho_Nw < 1 on 42/42;
fingerprint sp vs withheld offset -0.28 / +0.29 (below the 0.9
alias bar); extra mains w13 (maxdiag 0.9548, assist 0.0472,
cross 171) / kz15 (0.9710, 0.0299, cross 205).  CONTROLS
(depth 189): minC == flips, crossings 26/22/28/26 == flip+1;
budget split at the crossing (maxdiag_c, assist_c, offshare):
EPST (0.376, 1.69, 0.63), SCR (0.256, 2.94, 0.75), SMOOTH
(0.262, 2.99, 0.75), HL2 (0.260, 2.96, 0.75) -- at the death
degree maxdiag sits at 0.26..0.38: the budget rips at (C).
THE b3 SURPRISE (the contract's 'presumably YES' is measured
NO): (D) is NOT world-blind at window scale -- the controls'
maxdiag crosses 1 at n_DIAG = 91/50/90/87 (EPST/SCR/SMOOTH/
HL2), far above their crossings 26/22/28/26 but far below 184
(maxdiag_184 = 1170/8.5e6/1.93/1269); MAIN alone holds the
per-atom bound through its whole free window (n_DIAG = 187 >
185 > 184) -- (D) itself carries world separation at window
scale, so the clean split '(D) metric-local blind + (C) all
the arithmetic' is REFUTED as stated; the arithmetic sits in
BOTH halves at window scale, while at the DEATH DEGREE the
split is clean (controls die collectively via (C) with
maxdiag 0.26..0.38).  PER-ATOM (w9): top-5 diag atoms at N_w =
folds 2/4/6/8/10 (d = 0.9700/0.9649/0.9604/0.9535/0.9411, ALL
ARCH, u = 0.030..0.151, v = 2.8e-6..4.4e-6) -- the shallow-u
edge family BELOW the first prime, near-degenerate leaders;
binding fold 2 == r284 argmax; LADDER CENSUS: binding ARCH
42/42, u < log 2 42/42, nu-fold-rank <= 1 41/42, sample rungs
12/26/40/52 all bind at fold 2.  CLASSICAL (typed
COMPARISON_ONLY): p_bind = 0.38 (SUB-classical -- the measured
kernel growth at the binding edge atom is SLOWER than the bulk
law 1, not faster; BULK_LIKE by the sealed proximity rule),
p_bulk(f = 215, u = 3.24) = 1.27; K_meas/K_cl at N_w = 0.31;
n*_bind = 58 vs n_DIAG 187 (1.68 octaves OUTSIDE the band);
coverage min_k n* = 58.3 at fold 2 << N_w, 0/42 rungs covered
(n*_bind med 175 vs N med 388) -- the arcsine bulk law does
NOT carry (D) anywhere: (D) survives BECAUSE the discrete
kernel grows sub-classically at the binding atoms (measured
0.38 vs classical 1) -- the provability route for (D) must be
a DISCRETE bound, not continuum asymptotics; quantified gap
statement, no certificate.  COHERENCE: MAIN assist profile
4.25/1.74/0.39/0.031/0.019 at n = 20/40/120/184/185 (falls two
decades into the wall); controls at crossing fractions 0.25/
0.5/0.75/1.0: EPST 4.79/2.54/1.95/1.69, SCR 8.58/4.30/3.99/
2.94, SMOOTH 3.81/3.66/3.46/2.99, HL2 6.90/4.84/5.19/2.96 --
high-assist throughout, still ~2..3 at the flip (collective
death) vs MAIN 0.019 (single-atom wall); z-scores at the
crossing: MAIN z_v = -3.15 (DESTRUCTIVE, marginally outside
the |z| <= 3 generic band; C_off = -0.105, adaptive z_x =
+3.36) vs controls z_v = +12.4/+6.6/+5.0/+6.3 (ALL
CONSTRUCTIVE): the SIGN separates cleanly, the sealed
band rule types MIXED because MAIN sits at -3.15 (honest;
the r272/r273 generic-cancellation reading survives in sign,
not in the sealed band).  ENSEMBLES (conservation exact,
crossing == minC+1 spot-gated): ENS_SIGN 16 reps, crossings
5..21 (med 13), assist_20 med 1.25 -> MAIN 4.25 pct 1.00
HIGH_OUTLIER, assist_cross med 1.89 -> MAIN 0.0195 pct 0.00
LOW_OUTLIER; ENS_SCR 12 reps (S 367..367), crossings 5..28,
assist_20 med 3.80 -> pct 0.75 GENERIC, assist_cross med 3.99
-> pct 0.00 LOW_OUTLIER -- MAIN's wall coherence is the
extreme LOW outlier of both ensembles (every replicate dies
collectively; MAIN's near-single-atom wall is MAIN-specific),
while its early coherence is scramble-generic and even HIGH
against the sign ensemble.  DETECTOR: K_D1_maxdiag184
WORLD_BLIND (the dead spread 1.9..8.5e6 swallows everything),
K_D2_assist_cross MAIN_SEPARATING (0.0195 vs 1.69..2.99),
K_C1_zv_cross MAIN_SEPARATING (-3.15 vs +4.95..+12.44),
K_B1_nstar_ratio WORLD_BLIND (SCR binding atom edge-degenerate,
guard value disclosed).  MUST-FAILS: m1 dev 0.968 LOUD; m2 dev
1.0e+05 LOUD; m3 break 1.5e-1 CAUGHT; m4 flagged
(cross_true@545); constructors + fragment audit CLEAN.
Runtime 7.1 s full / 0.3 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE.

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

import lstar_two_measure_probe as LS              # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS   # noqa: E402 r283
import budget_localization_probe as BL            # noqa: E402 r280
import metric_stability_probe as MS               # noqa: E402 r278
import port_integrable_kernel_probe as PIK        # noqa: E402 v881
import principal_bessel_probe as PB               # noqa: E402 r243
import paircorr_margin_probe as PC                # noqa: E402
import bordered_hankel_probe as BH                # noqa: E402 r244
import wronskian_dictionary_probe as WD           # noqa: E402 r274
import jfraction_probe as JF                      # noqa: E402 r230
import v563_paper2_readouts as core               # noqa: E402 READ-ONLY

MAINS = (9, 13, 15)
MINC_OFF = {9: 0, 13: 2, 15: 1}
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
R281_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
H_CAP = 900
EXT = 8
EXT2 = 32
DEPTH_PAD = 6
CTRL_PAD = 5
WARD_DPS = 60
RHO_WARD_TOL = 1e-6
ID_TOL = 1e-12
DEC_TOL = 1e-10
SAND_TOL = 1e-9
WEYL_TOL = 1e-9
EQ_SKIP = 1e-13
PROF_DEGS = (20, 40, 120, 184, 185)
CROSS_FRACS = (0.25, 0.5, 0.75, 1.0)
R283_RHO = {20: 0.47808, 120: 0.99898, 185: 1.00004}
RHO_TOL = 1e-5
R283_TOP5 = (0.99983, 0.99874, 0.99597, 0.98461, 0.96408)
TOP5_TOL = 1e-4
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
DIAGMAX_REC = 0.9700
DIAGMAX_TOL = 5e-3
NCS_REC = 10
NDIAG_REC = 187
CROSS_REC = 185
GAIN_REC = 1.0307
GAIN_TOL = 5e-3
SLACK_REC = 50.2
SLACK_TOL = 1.0
R_LOC = 8
EDGE_U = math.log(2.0)
GROWTH_FRACS = (0.25, 0.5, 1.0)
OCT_BAND = 1.0
TOPD = 5
SAMPLE_KZ = (12, 26, 40, 52)
DET_DEG = 20
A_MAIN_BAR = 0.10
A_CTRL_BAR = 0.5
Z_GEN = 3.0
ENS_SIGN_REPS = 16
ENS_SCR_REPS = 12
SEED_BASE = 285000
PCT_BAND = (0.2, 0.8)
M1_BAR = 0.1
M2_BAR = 0.1
M3_BAR = 1e-3
MUT_MASS = 1.15
FP_BAR = 0.9
ADMIT = 1e-9

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
    return (not bad), ("NO zero/prime oracles; atom classes via the "
                       "r254 integer root extraction; the sealed "
                       "constructors consume split-source arrays and "
                       "kernel matrices ONLY; record counts, offsets "
                       "and flips enter gates and record tables only"
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


CONSTRUCTORS = ("decomp_parts", "assist_terms", "weyl_off_norm",
                "eq_density", "local_density", "classical_nstar",
                "growth_slope", "sign_assignment", "cons_check")
SCOPE_FORBIDDEN = {"ANCHORS", "MINC_OFF", "CTRL_FLIPS", "HL2_FLIP",
                   "R281_DIST", "minC_true", "cross_true",
                   "offs_true"}


def scope_audit(funcname):
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
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def decomp_parts(E, u):
    """exact Rayleigh decomposition of rho = u^T E u into the
    diagonal part sum u_k^2 d_k and the off-diagonal interference
    X = u^T Off u, plus the random-sign scale G = sqrt(sum of the
    squared off-diagonal terms (u_i u_j E_ij)^2) and the absolute
    term sum A (cancellation-depth denominator)."""
    d = np.diag(E).copy()
    diagpart = float(np.sum(u * u * d))
    Off = E - np.diag(d)
    X = float(u @ (Off @ u))
    T = np.outer(u, u) * Off
    G = float(math.sqrt(np.sum(T * T)))
    A = float(np.sum(np.abs(T)))
    return diagpart, X, G, A


def assist_terms(rho, maxd):
    """the sealed multiplicative bookkeeping: assist = rho/maxd
    - 1 (definition-exact), the budget headroom 1/maxd - 1, and
    the budget margin (1/maxd - 1) - assist (> 0 <=> rho < 1)."""
    assist = rho / maxd - 1.0
    head = 1.0 / maxd - 1.0
    return assist, head, head - assist


def weyl_off_norm(E):
    """lambda_max of the off-diagonal part (the Weyl bracket of
    the additive bookkeeping)."""
    Off = E - np.diag(np.diag(E).copy())
    return float(np.linalg.eigvalsh(Off)[-1])


def eq_density(y, a, b):
    """arcsine equilibrium density of the hull [a, b]; inf on the
    closed boundary (edge-degenerate, handled by the caller)."""
    q = (y - a) * (b - y)
    if q <= 0.0:
        return float("inf")
    return 1.0 / (math.pi * math.sqrt(q))


def local_density(fp, wp, f0, L, R):
    """sealed local mu density at fold f0: mu mass within R fold
    steps / the x-width of the (clamped) fold window under
    x = cos(2 pi f / L)."""
    fps = np.sort(np.asarray(fp, np.int64))
    o = np.argsort(fp)
    wps = np.asarray(wp, float)[o]
    cw = np.concatenate([[0.0], np.cumsum(wps)])
    lo = int(np.searchsorted(fps, f0 - R, side="left"))
    hi = int(np.searchsorted(fps, f0 + R, side="right"))
    mass = float(cw[hi] - cw[lo])
    f_lo = max(f0 - R, 0)
    f_hi = min(f0 + R, L // 2)
    x_hi = math.cos(2.0 * math.pi * f_lo / L)
    x_lo = math.cos(2.0 * math.pi * f_hi / L)
    width = x_hi - x_lo
    return mass, width, (mass / width if width > 0 else float("inf"))


def classical_nstar(dens, v, omega):
    """the classical isolation degree: first n with
    v K^cl_n = v n omega / dens >= 1, i.e. n* = dens/(v omega);
    0 for edge-degenerate atoms (omega = inf)."""
    if not math.isfinite(omega) or omega <= 0.0:
        return 0.0
    return dens / (v * omega)


def growth_slope(kvals, nvals):
    """halves log-slope: difference of mean ln K between the
    second and first half of the degree window, divided by the
    same for ln n."""
    m = len(kvals) // 2
    k1 = np.log(np.asarray(kvals[:m], float))
    k2 = np.log(np.asarray(kvals[m:], float))
    n1 = np.log(np.asarray(nvals[:m], float))
    n2 = np.log(np.asarray(nvals[m:], float))
    return float((np.mean(k2) - np.mean(k1))
                 / (np.mean(n2) - np.mean(n1)))


def sign_assignment(n_folds, n_neg, seed):
    """sealed sign-ensemble assignment: a pinned-seed choice of
    exactly n_neg of the n_folds union slots to carry the nu
    label (positions and magnitudes untouched by construction)."""
    rng = np.random.default_rng(seed)
    mask = np.zeros(n_folds, bool)
    mask[rng.permutation(n_folds)[:n_neg]] = True
    return mask


def cons_check(folds_a, mags_a, folds_b, mags_b, n_neg, mask):
    """conservation gate for the sign ensemble: identical fold
    sets, identical magnitude-per-fold, exact nu count; returns
    (ok, max rel magnitude dev)."""
    fa = np.asarray(folds_a, np.int64)
    fb = np.asarray(folds_b, np.int64)
    ma = np.asarray(mags_a, float)
    mb = np.asarray(mags_b, float)
    if len(fa) != len(fb) or not np.array_equal(fa, fb):
        return False, float("inf")
    dev = float(np.max(np.abs(ma - mb)
                       / np.maximum(np.abs(ma), 1e-300)))
    ok = dev == 0.0 and int(np.sum(mask)) == n_neg
    return ok, dev


# ============== must-fail mutants
def mutant_nodiag_assist(E, u):
    """m1 MUST-FAIL: 'off-diagonal interference' WITHOUT the
    diagonal subtraction -- claims the whole Rayleigh quotient;
    must break the exact decomposition identity loudly."""
    return float(u @ (E @ u))


def mutant_unweighted_cs(cum, vn):
    """m2 MUST-FAIL: the Christoffel sum WITHOUT the nu weights
    (must break the exact trace identity, r284 form)."""
    return np.sum(cum / np.asarray(vn, float)[:, None], axis=0)


def mutant_mass_scale(mags):
    """m3 MUST-FAIL: an ensemble surgery that scales the largest
    magnitude by 1.15 -- the conservation gate must CATCH it."""
    out = np.asarray(mags, float).copy()
    out[int(np.argmax(out))] *= MUT_MASS
    return out


def mutant_cross_oracle(cross_true):
    """m4 MUST-FAIL: a degree oriented by the withheld crossing
    -- the scope audit must FLAG this."""
    return cross_true - 1


# ============== gate-side helpers
def rho_at(B, n):
    """lambda_max(E_n) at a single degree (gate-side)."""
    Bn = B[:, :n]
    return float(np.linalg.eigvalsh(Bn @ Bn.T)[-1])


def budget_block(W, depth):
    """gate-side budget bundle at one depth: chain, B, cumulative
    Christoffel rows, maxdiag/trace profiles."""
    al, sb, h0 = FS.mu_chain_f64(np.asarray(W["xp"]),
                                 np.asarray(W["wp"]), depth)
    B = FS.b_matrix_f64(al, sb, h0, np.asarray(W["xn"]),
                        np.asarray(W["vn"]), depth)
    cum = LS.christoffel_rows(B)
    return dict(B=B, cum=cum,
                maxd=np.max(cum, axis=0),
                trace=np.sum(cum, axis=0), depth=depth)


def nstar_all(W, R):
    """gate-side classical isolation degrees for all nu atoms of
    one world (edge-degenerate atoms reported as 0)."""
    xu = np.concatenate([np.asarray(W["xp"]), np.asarray(W["xn"])])
    a, b = float(np.min(xu)), float(np.max(xu))
    out = np.zeros(W["Sm"])
    dens_l = np.zeros(W["Sm"])
    omg_l = np.zeros(W["Sm"])
    for k in range(W["Sm"]):
        omg = eq_density(float(W["xn"][k]), a, b)
        _m, _w, dens = local_density(W["fp"], W["wp"],
                                     int(W["fn"][k]), W["L"], R)
        out[k] = classical_nstar(dens, float(W["vn"][k]), omg)
        dens_l[k] = dens
        omg_l[k] = omg if math.isfinite(omg) else -1.0
    return out, dens_l, omg_l


def ens_sign_world(x_all, mags, mask, need_deg, det_deg):
    """gate-side sign-ensemble replicate: signed union -> minC
    (sign chain) -> mu chain/B -> (assist_20, assist at own
    crossing, maxdiag/assist at 184, crossing)."""
    wu = mags * np.where(mask, -1.0, 1.0)
    N_half = (len(x_all) + 1) // 2
    sg, _lg, _r = BL.sign_chain_f64(x_all, wu, N_half + EXT)
    mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    if mc is None:
        sg, _lg, _r = BL.sign_chain_f64(x_all, wu, N_half + EXT2)
        mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    cross = (mc + 1) if mc is not None else None
    xp, wp = x_all[~mask], mags[~mask]
    yn, vn = x_all[mask], mags[mask]
    depth = min(max(need_deg, (cross or 1) + 1, det_deg + 1),
                len(xp) - 1)
    al, sb, h0 = FS.mu_chain_f64(xp, wp, depth)
    B = FS.b_matrix_f64(al, sb, h0, yn, vn, depth)
    cum = LS.christoffel_rows(B)
    res = dict(minC=mc, cross=cross, depth=depth, B=B, cum=cum,
               Nw=N_half)
    for tag, n in (("20", det_deg), ("cross", cross),
                   ("Nw", min(need_deg, depth))):
        if n is None or n > depth:
            res["assist_" + tag] = None
            continue
        r = rho_at(B, n)
        md = float(np.max(cum[:, n - 1]))
        res["assist_" + tag] = r / md - 1.0
        res["maxd_" + tag] = md
        res["rho_" + tag] = r
    return res


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("christoffel_decomposition_probe -- PRIME.PORT.LSTAR."
          "CHRISTOFFEL_DECOMPOSITION.01 (round 285)")
    print("SPEC_SHA %s   (r284 LS %s / r283 FS %s)"
          % (SPEC_SHA[:16], LS.SPEC_SHA[:16], FS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 f64 block; ladder, mains, controls, "
                        "ensembles, mp ward, detector, adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the two bookkeeping forms "
          "(multiplicative assist, additive remainder + Weyl "
          "bracket), the budget theorem and its equivalence gate, "
          "the ladder/control budget tables, the per-atom census "
          "rules, the classical yardstick (arcsine hull density + "
          "sealed local density, typed COMPARISON_ONLY), the "
          "coherence z-score and its typing, both ensembles with "
          "conservation gates and pinned seeds, every bar/band/"
          "tolerance, the mutants and the verdict form; the STOP "
          "list forbids any L* claim and any equilibrium "
          "substitution")

    # ---------------- S1 toys
    section("S1  TOYS -- HAND 2x2, JF9 DECOMPOSITION, CONSERVATION")
    # t1: hand 2x2  E = (1/16) [[4, 2], [2, 2]]
    E_t = np.array([[4.0, 2.0], [2.0, 2.0]]) / 16.0
    ev_t, V_t = np.linalg.eigh(E_t)
    lam_t = float(ev_t[-1])
    u_t = V_t[:, -1]
    maxd_t = 0.25
    s5 = math.sqrt(5.0)
    lam_h = (3.0 + s5) / 16.0
    assist_h = (s5 - 1.0) / 4.0
    off_h = s5 / 20.0
    diag_h = (15.0 + s5) / 80.0
    dg_t, X_t, _G_t, _A_t = decomp_parts(E_t, u_t)
    a_t, hd_t, mg_t = assist_terms(lam_t, maxd_t)
    wn_t = weyl_off_norm(E_t)
    coh_t = lam_t - maxd_t
    ok_t1 = (abs(lam_t - lam_h) <= 1e-14
             and abs(a_t - assist_h) <= 1e-14
             and abs(X_t - off_h) <= 1e-14
             and abs(dg_t - diag_h) <= 1e-14
             and abs(dg_t + X_t - lam_t) <= 1e-15
             and abs(wn_t - 0.125) <= 1e-14
             and 0.0 <= coh_t <= wn_t + 1e-15
             and (mg_t > 0.0) == (lam_t < 1.0)
             and abs(maxd_t * (1.0 + a_t) - lam_t) <= 1e-16)
    check("G10-toy-hand2x2", ok_t1,
          "HAND 2x2 (E = (1/16)[[4,2],[2,2]]): lambda = (3+sqrt5)"
          "/16 = %.10f, assist = (sqrt5-1)/4 = %.10f, offpart = "
          "sqrt5/20 = %.10f, diagpart = (15+sqrt5)/80 = %.10f, "
          "off-norm = 1/8; multiplicative identity, Rayleigh "
          "decomposition, Weyl bracket 0 <= coh = %.6f <= %.6f "
          "and the budget equivalence all EXACT vs hand values"
          % (lam_t, a_t, X_t, dg_t, coh_t, wn_t))
    # t2: JF9 rational cross-route + decomposition at every n
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    nodes9 = [t[0] for t in jf_pairs]
    wts9 = [t[1] for t in jf_pairs]
    xs_r = [x for x, w in zip(nodes9, wts9) if w > 0]
    ws_r = [w for w in wts9 if w > 0]
    ys_r = [x for x, w in zip(nodes9, wts9) if w < 0]
    vs_r = [-w for w in wts9 if w < 0]
    Sp_t = len(xs_r)
    alm, bem, hsm = WD.stj_gen(xs_r, ws_r, Sp_t - 1)
    vals = [WD.pv_seq(alm, bem, y, Sp_t - 1) for y in ys_r]
    al_f, sb_f, h0_f = FS.mu_chain_f64(
        np.array([float(x) for x in xs_r]),
        np.array([float(w) for w in ws_r]), Sp_t)
    B_t = FS.b_matrix_f64(al_f, sb_f, h0_f,
                          np.array([float(y) for y in ys_r]),
                          np.array([float(v) for v in vs_r]), Sp_t)
    cum_t = LS.christoffel_rows(B_t)
    dev_chr = 0.0
    for n in range(1, Sp_t + 1):
        for k in range(len(ys_r)):
            exact = vs_r[k] * sum(vals[k][i] * vals[k][i] / hsm[i]
                                  for i in range(n))
            dev_chr = max(dev_chr,
                          abs(cum_t[k, n - 1] - float(exact))
                          / max(abs(float(exact)), 1e-300))
    cr_t, rho_t = FS.crossing_from_B(B_t, Sp_t)
    dev_dec = 0.0
    ok_sand = True
    ok_weyl = True
    ok_eq = True
    for n in range(1, Sp_t + 1):
        Bn = B_t[:, :n]
        En = Bn @ Bn.T
        evn, Vn = np.linalg.eigh(En)
        un = Vn[:, -1]
        dgn, Xn, _g, _a = decomp_parts(En, un)
        dev_dec = max(dev_dec, abs(dgn + Xn - float(evn[-1]))
                      / max(abs(float(evn[-1])), 1e-300))
        mdn = float(np.max(cum_t[:, n - 1]))
        trn = float(np.sum(cum_t[:, n - 1]))
        ok_sand = ok_sand and (mdn <= rho_t[n] + SAND_TOL
                               and rho_t[n] <= trn + SAND_TOL)
        ok_weyl = ok_weyl and (rho_t[n] - mdn
                               <= weyl_off_norm(En) + WEYL_TOL)
        an, _h, mn = assist_terms(rho_t[n], mdn)
        if abs(rho_t[n] - 1.0) > EQ_SKIP:
            ok_eq = ok_eq and ((mn > 0.0) == (rho_t[n] < 1.0)) \
                and abs(mdn * (1.0 + an) - rho_t[n]) \
                <= ID_TOL * max(rho_t[n], 1.0)
    check("G11-toy-jf9-decomposition", dev_chr <= DEC_TOL
          and dev_dec <= DEC_TOL and ok_sand and ok_weyl
          and ok_eq and cr_t == 4,
          "JF9: rational Christoffel cross-route max rel dev "
          "%.1e (bar %.0e); Rayleigh decomposition dev %.1e; "
          "sandwich + Weyl bracket + budget equivalence at every "
          "n <= S_+ = %d; crossing %s == 4 (r283 record)"
          % (dev_chr, DEC_TOL, dev_dec, Sp_t, str(cr_t)))
    # t3: toy conservation battery
    tf = np.array([1, 2, 3, 4, 5], np.int64)
    tm = np.array([1.0, 0.5, 0.25, 0.125, 0.0625])
    msk_t = sign_assignment(5, 2, SEED_BASE)
    okc_t, dev_c = cons_check(tf, tm, tf, tm, 2, msk_t)
    check("G12-toy-conservation", okc_t and dev_c == 0.0
          and int(np.sum(msk_t)) == 2,
          "TOY CONSERVATION: the legit sign-ensemble op preserves "
          "fold set + magnitude-per-fold bitwise (dev %.1f) and "
          "carries exactly 2 of 5 nu labels (hand count) -- the "
          "gate passes the legit op" % dev_c)

    # ---------------- S2 w9 machinery + regression
    section("S2  W9 -- E-CONSTRUCTION GATED AGAINST r283/r284")
    rr9 = core.build_window(9)
    D9 = float(rr9["D"])
    ctx9 = MS.ctx_build(9)
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == 367 and W9["Sp"] == 263
              and W9["Sm"] == 104
              and W9["N"] == (W9["S"] + 1) // 2
              and W9["minC"] == W9["N"] + MINC_OFF[9])
    check("G20-w9-source-split", ok_src,
          "w9 FULL SOURCE: S = %d (mu %d / nu %d), N_w = %d == "
          "(S+1)//2, minC = %s == N_w + %d (record)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"],
             str(W9["minC"]), MINC_OFF[9]))
    depth9 = min(W9["N"] + DEPTH_PAD, W9["Sp"] - 1)
    SP9 = LS.spectral_block(W9, depth9)
    rho9 = SP9["rho"]
    check("G21-w9-crossing", SP9["cross"] == W9["minC"] + 1
          and SP9["cross"] == CROSS_REC,
          "lambda_max(E_n) crosses 1 at n = %s == minC + 1 == %d "
          "(r283/r284 route reproduced)"
          % (str(SP9["cross"]), CROSS_REC))
    Nw = W9["N"]
    E184 = SP9["B"][:, :Nw] @ SP9["B"][:, :Nw].T
    ev184 = np.linalg.eigvalsh(E184)
    top5 = ev184[-5:][::-1]
    margin9 = 1.0 - rho9[Nw]
    dmax184 = float(SP9["maxd"][Nw - 1])
    gain9 = float(rho9[Nw] / SP9["maxd"][Nw - 1])
    slack9 = float(SP9["trace"][Nw - 1] / rho9[Nw])
    ok_rec = all(abs(rho9[n] - R283_RHO[n]) <= RHO_TOL
                 for n in R283_RHO)
    ok_top = all(abs(float(top5[i]) - R283_TOP5[i]) <= TOP5_TOL
                 for i in range(5))
    ok_r284 = (SP9["n_cs"] == NCS_REC and SP9["n_diag"] == NDIAG_REC
               and abs(gain9 - GAIN_REC) <= GAIN_TOL
               and abs(slack9 - SLACK_REC) <= SLACK_TOL)
    check("G22-w9-profile-regression",
          ok_rec and ok_top and ok_r284
          and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
          and abs(dmax184 - DIAGMAX_REC) <= DIAGMAX_TOL
          and rho9[Nw] < 1.0,
          "r283/r284 RECORDS REPRODUCED: rho_20/120/185 dev <= "
          "%.0e; top-5 eigs ok; margin %.4e (rec %.2e); diagmax "
          "%.5f (rec %.4f); n_CS = %s (rec %d), n_DIAG = %s (rec "
          "%d), gain_Nw = %.4f (rec %.4f), slack_Nw = %.1f (rec "
          "%.1f)" % (RHO_TOL, margin9, MARGIN_REC, dmax184,
                     DIAGMAX_REC, str(SP9["n_cs"]), NCS_REC,
                     str(SP9["n_diag"]), NDIAG_REC, gain9,
                     GAIN_REC, slack9, SLACK_REC))
    if smoke:
        check("G23-w9-mp-ward", True, "SMOKE: skipped")
    else:
        alm9, sbm9, h0m9 = FS.mu_chain_mp(
            np.asarray(W9["xp"]), np.asarray(W9["wp"]), depth9,
            WARD_DPS)
        B9m = FS.b_matrix_mp(alm9, sbm9, h0m9,
                             np.asarray(W9["xn"]),
                             np.asarray(W9["vn"]), depth9,
                             WARD_DPS)
        cum_m = LS.christoffel_rows(B9m)
        md_mp = float(np.max(cum_m[:, Nw - 1]))
        devs = {}
        rho_mp = {}
        for n in (Nw, Nw + 1):
            Bn = B9m[:, :n]
            rmp = float(np.linalg.eigvalsh(Bn @ Bn.T)[-1])
            rho_mp[n] = rmp
            devs[n] = abs(rmp - rho9[n]) / max(abs(rmp), 1e-300)
        dev_md = abs(md_mp - dmax184) / max(abs(md_mp), 1e-300)
        ok_ward = (max(devs.values()) <= RHO_WARD_TOL
                   and dev_md <= RHO_WARD_TOL
                   and rho_mp[Nw] < 1.0 and rho_mp[Nw + 1] > 1.0)
        check("G23-w9-mp-ward", ok_ward,
              "MP WARD (dps %d): rho_184 = %.8f < 1 < %.8f = "
              "rho_185 (rel devs %.1e / %.1e), maxdiag_184 dev "
              "%.1e (bar %.0e) -- budget arbitration-safe"
              % (WARD_DPS, rho_mp[Nw], rho_mp[Nw + 1], devs[Nw],
                 devs[Nw + 1], dev_md, RHO_WARD_TOL))

    # ---------------- S3 leg A -- decomposition + budgets
    section("S3  LEG A -- EXACT BOOKKEEPING + BUDGETS")
    dev_mult = 0.0
    dev_dec9 = 0.0
    ok_weyl9 = True
    ok_eq9 = True
    weyl_tab = {}
    for n in range(1, depth9 + 1):
        mdn = float(SP9["maxd"][n - 1])
        an, _h, mn = assist_terms(rho9[n], mdn)
        dev_mult = max(dev_mult, abs(mdn * (1.0 + an) - rho9[n])
                       / max(rho9[n], 1e-300))
        if abs(rho9[n] - 1.0) > EQ_SKIP:
            ok_eq9 = ok_eq9 and ((mn > 0.0) == (rho9[n] < 1.0))
    for n in PROF_DEGS:
        Bn = SP9["B"][:, :n]
        En = Bn @ Bn.T
        evn, Vn = np.linalg.eigh(En)
        un = Vn[:, -1]
        dgn, Xn, Gn, An = decomp_parts(En, un)
        dev_dec9 = max(dev_dec9, abs(dgn + Xn - float(evn[-1]))
                       / max(abs(float(evn[-1])), 1e-300))
        wn = weyl_off_norm(En)
        coh = float(evn[-1]) - float(SP9["maxd"][n - 1])
        ok_weyl9 = ok_weyl9 and (-WEYL_TOL <= coh <= wn + WEYL_TOL)
        weyl_tab[n] = (coh, wn)
    check("G30-decomposition-identities",
          dev_mult <= ID_TOL and dev_dec9 <= DEC_TOL
          and ok_weyl9 and ok_eq9,
          "w9 EXACT BOOKKEEPING at every n <= %d: multiplicative "
          "identity lambda == maxdiag x (1 + assist) dev %.1e "
          "(bar %.0e); budget equivalence (margin > 0 <=> rho < "
          "1) sign-exact outside the %.0e band; Rayleigh "
          "decomposition rho == diagpart + offpart dev %.1e at "
          "the sealed degrees; Weyl bracket 0 <= coh <= "
          "lambda_max(Off) holds -- NO give-away sandwich"
          % (depth9, dev_mult, ID_TOL, EQ_SKIP, dev_dec9))
    a9, h9, m9 = assist_terms(float(rho9[Nw]), dmax184)
    coh9, wn9 = weyl_tab[Nw]
    check("G31-w9-budget", m9 > 0.0 and a9 <= A_MAIN_BAR,
          "w9 BUDGET at N_w: maxdiag = %.5f (delta = %.5f), "
          "assist = %.5f (<= %.2f), budget margin (1/maxdiag - 1)"
          " - assist = %+.3e > 0 <=> margin 1 - rho = %.3e; "
          "ADDITIVE remainder coh = %.5f vs Weyl off-norm %.5f "
          "(slack %.3f -- the additive bookkeeping is coarse, "
          "the multiplicative form is the honest one)"
          % (dmax184, 1.0 - dmax184, a9, A_MAIN_BAR, m9, margin9,
             coh9, wn9, wn9 - coh9))
    if smoke:
        for g in ("G32-ladder-census", "G33-ladder-budgets",
                  "G34-mains-budgets", "G35-ctrl-budgets"):
            check(g, True, "SMOKE: skipped")
        WC = {}
        SPC = {}
        lad = {}
        ctrl_budget = {}
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        lad = {}
        ok_hf = True
        for kz in kzs:
            if kz == 9:
                Wp, ctxk, Dk = W9, ctx9, D9
            else:
                ctxk = MS.ctx_build(kz)
                Dk = float(core.build_window(kz)["D"])
                Wp = LS.world_pack("w%d" % kz, ctxk, Dk)
            ok_hf = ok_hf and (Wp["N"] == (Wp["S"] + 1) // 2)
            dep = min(Wp["N"], Wp["Sp"] - 1)
            bb = budget_block(Wp, dep)
            md = float(bb["maxd"][dep - 1])
            rh = rho_at(bb["B"], dep)
            ak, _hk, mk = assist_terms(rh, md)
            kb = int(np.argmax(bb["cum"][:, dep - 1]))
            lab = LS.atom_labels([int(Wp["fn"][kb])], Dk,
                                 Wp["uu"], Wp["mm"])[0]
            u_b = float(Wp["fn"][kb]) * Dk
            frank = int(np.searchsorted(
                np.sort(np.asarray(Wp["fn"])), Wp["fn"][kb]))
            ns_all, _dl, _ol = nstar_all(Wp, R_LOC)
            ns_in = ns_all[ns_all > 0.0]
            lad[kz] = dict(N=Wp["N"], S=Wp["S"],
                           off=Wp["minC"] - Wp["N"], maxd=md,
                           rho=rh, assist=ak, marg=mk,
                           bind_fold=int(Wp["fn"][kb]),
                           bind_cls=lab[0], bind_u=u_b,
                           bind_rank=frank,
                           ns_bind=float(ns_all[kb]),
                           ns_min=float(np.min(ns_in))
                           if len(ns_in) else 0.0,
                           n_edge_deg=int(np.sum(ns_all == 0.0)))
        offs_true = [lad[kz]["off"] for kz in sorted(lad)]
        dist = {}
        for o in offs_true:
            dist[o] = dist.get(o, 0) + 1
        ok_anch = all(lad[kz]["off"] == ANCHORS[kz]
                      for kz in ANCHORS if kz in lad)
        check("G32-ladder-census", len(lad) == 42 and ok_hf
              and ok_anch and dist == R281_DIST,
              "42-rung census (r281 channel): offset distribution "
              "%s == r281 record, anchors exact, half-filling "
              "42/42" % str({("+%d" % k): dist[k]
                             for k in sorted(dist)}))
        mds = [lad[kz]["maxd"] for kz in sorted(lad)]
        aks = [lad[kz]["assist"] for kz in sorted(lad)]
        Ns = [lad[kz]["N"] for kz in sorted(lad)]
        ok_bud = all(lad[kz]["rho"] < 1.0 and lad[kz]["marg"] > 0.0
                     and lad[kz]["maxd"] < 1.0 for kz in lad)
        sp_md = BH.spearman(Ns, mds)
        sp_ak = BH.spearman(Ns, aks)
        fp_md = BH.spearman(mds, offs_true)
        fp_ak = BH.spearman(aks, offs_true)
        o_N = np.argsort(Ns)
        h1 = [mds[i] for i in o_N[:21]]
        h2 = [mds[i] for i in o_N[21:]]
        a1_ = [aks[i] for i in o_N[:21]]
        a2_ = [aks[i] for i in o_N[21:]]
        kz_mdmax = max(lad, key=lambda z: lad[z]["maxd"])
        kz_akmax = max(lad, key=lambda z: lad[z]["assist"])
        fp_typ = ("TARGET_ALIAS" if max(abs(fp_md), abs(fp_ak))
                  >= FP_BAR else "below alias bar")
        check("G33-ladder-budgets", ok_bud,
              "LADDER BUDGETS at N_w (42 rungs): maxdiag min/med/"
              "max %.4f/%.4f/%.4f (max at kz%d -> delta_min = "
              "%.4f), halves med %.3f -> %.3f, sp(N, maxdiag) "
              "%+.2f; assist min/med/max %.4f/%.4f/%.4f (max at "
              "kz%d), halves %.3f -> %.3f, sp(N, assist) %+.2f; "
              "budget margin > 0 AND rho_Nw < 1 on 42/42; "
              "FINGERPRINT vs withheld offset (reported): "
              "sp(maxdiag) %+.2f / sp(assist) %+.2f -> %s "
              "(alias bar %.1f)"
              % (min(mds), float(np.median(mds)), max(mds),
                 kz_mdmax, 1.0 - max(mds),
                 float(np.median(h1)), float(np.median(h2)),
                 sp_md, min(aks), float(np.median(aks)),
                 max(aks), kz_akmax, float(np.median(a1_)),
                 float(np.median(a2_)), sp_ak, fp_md, fp_ak,
                 fp_typ, FP_BAR))
        # extra mains
        ok_m = True
        txt_m = []
        for kz in (13, 15):
            ctxk = MS.ctx_build(kz)
            Dk = float(core.build_window(kz)["D"])
            Wp = LS.world_pack("w%d" % kz, ctxk, Dk)
            dep = min(Wp["N"] + DEPTH_PAD, Wp["Sp"] - 1)
            spb = LS.spectral_block(Wp, dep)
            mdk = float(spb["maxd"][Wp["N"] - 1])
            ak, _h, _m = assist_terms(float(spb["rho"][Wp["N"]]),
                                      mdk)
            ok_m = ok_m and Wp["minC"] == Wp["N"] + MINC_OFF[kz] \
                and spb["cross"] == Wp["minC"] + 1 \
                and spb["rho"][Wp["N"]] < 1.0
            txt_m.append("w%d: N=%d maxdiag=%.4f assist=%.4f "
                         "cross=%s" % (kz, Wp["N"], mdk, ak,
                                       str(spb["cross"])))
        check("G34-mains-budgets", ok_m,
              "EXTRA MAINS (crossing == minC+1, rho_Nw < 1): %s"
              % "; ".join(txt_m))
        # controls
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        WC = {}
        SPC = {}
        ctrl_budget = {}
        ok_c = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            Wp = LS.world_pack(cn, cctx, D9)
            WC[cn] = Wp
            flip = CTRL_FLIPS.get(cn, HL2_FLIP)
            dep = min(Wp["N"] + CTRL_PAD, Wp["Sp"] - 1)
            spb = LS.spectral_block(Wp, dep)
            SPC[cn] = spb
            nc = spb["cross"]
            mdc = float(spb["maxd"][nc - 1])
            ac, _h, _m = assist_terms(float(spb["rho"][nc]), mdc)
            offshare = 1.0 - mdc / float(spb["rho"][nc])
            ctrl_budget[cn] = dict(cross=nc, maxd_c=mdc,
                                   assist_c=ac, offshare=offshare,
                                   maxd_184=float(
                                       spb["maxd"][Wp["N"] - 1]),
                                   n_diag=spb["n_diag"])
            ok_c = ok_c and Wp["minC"] == flip and nc == flip + 1
        check("G35-ctrl-budgets", ok_c,
              "CONTROLS (r281 channel; minC == flips, crossing == "
              "flip+1): budget split at the crossing (maxdiag_c, "
              "assist_c, offdiag share) = %s -- maxdiag stays FAR "
              "below 1: the budget rips at (C), not at (D)"
              % str({cn: (round(v["maxd_c"], 3),
                          round(v["assist_c"], 2),
                          round(v["offshare"], 2))
                     for cn, v in ctrl_budget.items()}))

    # ---------------- S4 leg B -- per-atom + classical
    section("S4  LEG B -- PER-ATOM DIAGONAL + CLASSICAL COMPARISON")
    lab_nu = LS.atom_labels(W9["fn"], D9, W9["uu"], W9["mm"])
    dev_adm = max([d for _c, _p, d in lab_nu if _c != 0] or [0.0])
    d184 = SP9["cum"][:, Nw - 1]
    o_d = np.argsort(d184)[::-1]
    u_nu = np.asarray(W9["fn"], float) * D9
    info("w9 top-%d diag atoms at N_w (fold, u, x, class, p, v, "
         "d_Nw):" % TOPD)
    for t in range(TOPD):
        k = int(o_d[t])
        cls = ("ARCH", "K1", "KHI")[lab_nu[k][0]]
        info("  f=%4d u=%6.3f x=%+.5f %-4s p=%-4d v=%.2e "
             "d=%.4f" % (W9["fn"][k], u_nu[k], W9["xn"][k], cls,
                         lab_nu[k][1], W9["vn"][k], d184[k]))
    kbind = int(o_d[0])
    check("G40-binding-atoms-w9", dev_adm <= ADMIT
          and int(W9["fn"][kbind]) == 2,
          "w9 BINDING ATOM (argmax diag at N_w) = fold %d (u = "
          "%.3f, %s, v = %.2e, d = %.4f) == the r284 argmax and "
          "extremal carrier; label admission dev %.1e <= %.0e"
          % (W9["fn"][kbind], u_nu[kbind],
             ("ARCH", "K1", "KHI")[lab_nu[kbind][0]],
             W9["vn"][kbind], d184[kbind], dev_adm, ADMIT))
    if smoke:
        check("G41-ladder-binding-census", True, "SMOKE: skipped")
    else:
        n_arch = sum(1 for kz in lad if lad[kz]["bind_cls"] == 0)
        n_edgeu = sum(1 for kz in lad
                      if lad[kz]["bind_u"] < EDGE_U)
        n_rank = sum(1 for kz in lad
                     if lad[kz]["bind_rank"] <= 1)
        samp = {kz: lad[kz]["bind_fold"] for kz in SAMPLE_KZ
                if kz in lad}
        check("G41-ladder-binding-census", True,
              "LADDER BINDING CENSUS (42 rungs, argmax diag at "
              "N_w): ARCH %d/42, u < log 2 %d/42, nu-fold-rank "
              "<= 1 %d/42; sample rungs %s binding folds %s -- "
              "the shallow-u hull edge below the first prime is "
              "the binding family across the ladder"
              % (n_arch, n_edgeu, n_rank, str(SAMPLE_KZ),
                 str(samp)))
    # classical comparison on w9
    ns9, dens9, omg9 = nstar_all(W9, R_LOC)
    ubar_v = float(np.sum(np.asarray(W9["vn"]) * u_nu)
                   / np.sum(W9["vn"]))
    kbulk = int(np.argmin(np.abs(u_nu - ubar_v)))
    n_lo = max(int(math.ceil(GROWTH_FRACS[0] * Nw)), 2)
    n_hi = Nw
    degs = list(range(n_lo, n_hi + 1))
    p_bind = growth_slope(
        [SP9["cum"][kbind, n - 1] / W9["vn"][kbind] for n in degs],
        degs)
    p_bulk = growth_slope(
        [SP9["cum"][kbulk, n - 1] / W9["vn"][kbulk] for n in degs],
        degs)
    t_bind = "EDGE_LIKE" if abs(p_bind - 2.0) < abs(p_bind - 1.0) \
        else "BULK_LIKE"
    t_bulk = "EDGE_LIKE" if abs(p_bulk - 2.0) < abs(p_bulk - 1.0) \
        else "BULK_LIKE"
    kcl_bind = Nw * omg9[kbind] / dens9[kbind] \
        if omg9[kbind] > 0 else float("nan")
    ratio_bind = (SP9["cum"][kbind, Nw - 1] / W9["vn"][kbind]) \
        / kcl_bind
    ns_in9 = ns9[ns9 > 0.0]
    ns_min9 = float(np.min(ns_in9))
    k_min9 = int(np.argmin(np.where(ns9 > 0.0, ns9, np.inf)))
    oct_dev = abs(math.log2(ns9[kbind] / NDIAG_REC)) \
        if ns9[kbind] > 0 else float("inf")
    cover9 = ns_min9 >= Nw
    check("G42-classical-comparison", True,
          "CLASSICAL YARDSTICK (typed COMPARISON_ONLY, arcsine "
          "hull density + local mu density at R = %d): growth "
          "exponents p_bind = %.2f (%s; bulk law 1, soft edge 2) "
          "/ p_bulk(f=%d, u=%.2f) = %.2f (%s); level "
          "K_meas/K_cl at N_w = %.2f (binding atom); classical "
          "isolation n*_bind = %.0f vs measured n_DIAG = %d "
          "(octave dev %.2f, band %.1f -> %s); COVERAGE min_k "
          "n* = %.1f at fold %d vs N_w = %d -> %s (edge-"
          "degenerate atoms excluded: %d)"
          % (R_LOC, p_bind, t_bind, W9["fn"][kbulk], u_nu[kbulk],
             p_bulk, t_bulk, ratio_bind, ns9[kbind], NDIAG_REC,
             oct_dev, OCT_BAND,
             "INSIDE" if oct_dev <= OCT_BAND else "OUTSIDE",
             ns_min9, W9["fn"][k_min9], Nw,
             "CLASSICAL_COVERS" if cover9 else
             "CLASSICAL_GAP (the bulk law would break (D) early "
             "-- the discrete kernel grows sub-classically at "
             "the deep atoms)",
             int(np.sum(ns9 == 0.0))))
    if smoke:
        for g in ("G43-ladder-classical-coverage",
                  "G44-peratom-blindness"):
            check(g, True, "SMOKE: skipped")
        blind_D = None
    else:
        n_cov = sum(1 for kz in lad
                    if lad[kz]["ns_min"] >= lad[kz]["N"])
        nsb = [lad[kz]["ns_bind"] for kz in sorted(lad)]
        check("G43-ladder-classical-coverage", True,
              "LADDER CLASSICAL COVERAGE: min_k n* >= N_w on "
              "%d/42 rungs; n*_bind med %.0f vs N med %.0f -- "
              "the classical bulk law does NOT carry (D) through "
              "the window (a quantified gap statement, not a "
              "certificate)" % (n_cov, float(np.median(nsb)),
                                float(np.median(Ns))))
        md184_c = {cn: ctrl_budget[cn]["maxd_184"] for cn in WC}
        nd_c = {cn: ctrl_budget[cn]["n_diag"] for cn in WC}
        blind_D = all(v < 1.0 for v in md184_c.values())
        check("G44-peratom-blindness", True,
              "(D) BLINDNESS: controls' maxdiag at n = 184 = %s "
              "(ALL < 1: %s), n_DIAG within depth 189 = %s -- "
              "%s" % (str({c: round(v, 3)
                           for c, v in md184_c.items()}),
                      str(blind_D), str(nd_c),
                      "(D) holds on every dead world: WORLD_BLIND"
                      " -- the entire separation sits in (C)"
                      if blind_D else
                      "(D) SEPARATES (a control violates the "
                      "per-atom bound)"))

    # ---------------- S5 leg C -- coherence
    section("S5  LEG C -- ASSIST PROFILES + GENERIC YARDSTICK")
    prof9 = {}
    for n in PROF_DEGS:
        mdn = float(SP9["maxd"][n - 1])
        prof9[n] = float(rho9[n]) / mdn - 1.0
    info("w9 assist profile: " + ", ".join(
        "n=%d: %.4f" % (n, prof9[n]) for n in PROF_DEGS))
    check("G50-assist-profiles", prof9[Nw] <= A_MAIN_BAR,
          "MAIN assist FALLS monotonically into the wall: %s "
          "(assist at N_w = %.4f <= %.2f)%s"
          % (str({n: round(prof9[n], 3) for n in PROF_DEGS}),
             prof9[Nw], A_MAIN_BAR,
             "" if smoke else "; controls at crossing fractions "
             + str({cn: [round(float(SPC[cn]["rho"][
                 max(1, int(round(f * ctrl_budget[cn]["cross"])))]
                 / SPC[cn]["maxd"][max(1, int(round(
                     f * ctrl_budget[cn]["cross"]))) - 1]) - 1.0,
                 2) for f in CROSS_FRACS]
                 for cn in SPC}) + " -- monotone RISE into the "
             "flip: collective death vs single-atom wall"))
    # generic yardstick at the crossing
    uv9 = np.sqrt(np.asarray(W9["vn"]))
    uv9 = uv9 / float(np.linalg.norm(uv9))
    E185 = SP9["B"][:, :CROSS_REC] @ SP9["B"][:, :CROSS_REC].T
    _dg, Xv9, Gv9, Av9 = decomp_parts(E185, uv9)
    zv9 = Xv9 / max(Gv9, 1e-300)
    coff9 = Xv9 / max(Av9, 1e-300)
    _e, Vx = LS.top_eigvecs(SP9["B"], CROSS_REC, 1)
    _dgx, Xx9, Gx9, _Ax = decomp_parts(E185, Vx[:, 0])
    zx9 = Xx9 / max(Gx9, 1e-300)
    if smoke:
        check("G51-coherence-stats", True,
              "SMOKE (w9 only): z_v = %+.2f, C_off = %+.4f, z_x "
              "= %+.2f at the crossing" % (zv9, coff9, zx9))
        z_ctrl = {}
        c2_typ = None
    else:
        z_ctrl = {}
        for cn in WC:
            nc = ctrl_budget[cn]["cross"]
            Ec = SPC[cn]["B"][:, :nc] @ SPC[cn]["B"][:, :nc].T
            uvc = np.sqrt(np.asarray(WC[cn]["vn"]))
            uvc = uvc / float(np.linalg.norm(uvc))
            _d, Xc, Gc, Ac = decomp_parts(Ec, uvc)
            _ec, Vc = LS.top_eigvecs(SPC[cn]["B"], nc, 1)
            _dx, Xcx, Gcx, _ax = decomp_parts(Ec, Vc[:, 0])
            z_ctrl[cn] = (Xc / max(Gc, 1e-300),
                          Xc / max(Ac, 1e-300),
                          Xcx / max(Gcx, 1e-300))
        c2_typ = ("MAIN_GENERIC_CTRL_OUTLIER"
                  if abs(zv9) <= Z_GEN
                  and all(abs(v[0]) > Z_GEN
                          for v in z_ctrl.values())
                  else "MIXED")
        check("G51-coherence-stats", True,
              "GENERIC YARDSTICK at the crossing (random-sign "
              "z-score of the source-frame interference): MAIN "
              "z_v = %+.2f (C_off = %+.4f, adaptive z_x = "
              "%+.2f); controls (z_v, C_off, z_x) = %s => sealed "
              "typing %s (bar |z| <= %.1f)"
              % (zv9, coff9, zx9,
                 str({cn: tuple(round(x, 2) for x in v)
                      for cn, v in z_ctrl.items()}),
                 c2_typ, Z_GEN))
    # ensembles
    if smoke:
        for g in ("G52-ensemble-sign", "G53-ensemble-scramble",
                  "G54-ensemble-adjudication"):
            check(g, True, "SMOKE: skipped")
        ens_typ = {}
    else:
        x_all = np.concatenate([np.asarray(W9["xp"]),
                                np.asarray(W9["xn"])])
        f_all = np.concatenate([np.asarray(W9["fp"], np.int64),
                                np.asarray(W9["fn"], np.int64)])
        m_all = np.concatenate([np.asarray(W9["wp"]),
                                np.asarray(W9["vn"])])
        o_f = np.argsort(f_all)
        f_all, x_all, m_all = f_all[o_f], x_all[o_f], m_all[o_f]
        sign_rows = []
        ok_cons = True
        ok_spot = True
        for i in range(ENS_SIGN_REPS):
            msk = sign_assignment(len(f_all), W9["Sm"],
                                  SEED_BASE + i)
            okc, _d = cons_check(f_all, m_all, f_all, m_all,
                                 W9["Sm"], msk)
            ok_cons = ok_cons and okc
            r = ens_sign_world(x_all, m_all, msk, Nw, DET_DEG)
            sign_rows.append(r)
            if i == 0 and r["cross"] is not None:
                xp0, wp0 = x_all[~msk], m_all[~msk]
                yn0, vn0 = x_all[msk], m_all[msk]
                dep0 = min(r["cross"] + 2, len(xp0) - 1)
                al0, sb0, h00 = FS.mu_chain_f64(xp0, wp0, dep0)
                B0 = FS.b_matrix_f64(al0, sb0, h00, yn0, vn0,
                                     dep0)
                cr0, _rp0 = FS.crossing_from_B(B0, dep0)
                ok_spot = ok_spot and cr0 == r["minC"] + 1
        crs = [r["cross"] for r in sign_rows
               if r["cross"] is not None]
        a20s = [r["assist_20"] for r in sign_rows
                if r["assist_20"] is not None]
        acs = [r["assist_cross"] for r in sign_rows
               if r["assist_cross"] is not None]
        a20_main = prof9[DET_DEG]
        ac_main = float(rho9[CROSS_REC]
                        / SP9["maxd"][CROSS_REC - 1]) - 1.0
        pct20_s = float(np.mean([v < a20_main for v in a20s]))
        pctc_s = float(np.mean([v < ac_main for v in acs]))
        check("G52-ensemble-sign", ok_cons and ok_spot,
              "ENS_SIGN (%d pinned reps, conservation gates "
              "exact, crossing == minC+1 spot-gated on rep 0): "
              "crossings %s..%s (med %s); assist_20 med %.2f "
              "(MAIN %.2f, pct %.2f); assist_cross med %.2f "
              "(MAIN %.4f, pct %.2f)"
              % (ENS_SIGN_REPS, min(crs), max(crs),
                 int(np.median(crs)), float(np.median(a20s)),
                 a20_main, pct20_s, float(np.median(acs)),
                 ac_main, pctc_s))
        scr_rows = []
        ok_cons2 = True
        ok_spot2 = True
        Ss = []
        for i in range(ENS_SCR_REPS):
            sctx = MS.ctx_build(9, scramble_seed=SEED_BASE
                                + 100 + i)
            okc = np.array_equal(np.asarray(sctx["mm"]),
                                 np.asarray(ctx9["mm"])) \
                and len(sctx["uu"]) == len(ctx9["uu"])
            ok_cons2 = ok_cons2 and okc
            Wr = LS.world_pack("scr%d" % i, sctx, D9)
            Ss.append(Wr["S"])
            crr = (Wr["minC"] + 1) if Wr["minC"] is not None \
                else None
            dep = min(max(Wr["N"], (crr or 1) + 1, DET_DEG + 1),
                      Wr["Sp"] - 1)
            bb = budget_block(Wr, dep)
            row = dict(cross=crr)
            for tag, n in (("20", DET_DEG), ("cross", crr),
                           ("Nw", min(Wr["N"], dep))):
                if n is None or n > dep:
                    row["assist_" + tag] = None
                    continue
                rr_ = rho_at(bb["B"], n)
                mdn = float(bb["cum"][:, n - 1].max())
                row["assist_" + tag] = rr_ / mdn - 1.0
            scr_rows.append(row)
            if i == 0 and crr is not None:
                cr0, _rp = FS.crossing_from_B(
                    bb["B"], min(crr + 2, dep))
                ok_spot2 = ok_spot2 and cr0 == crr
        crs2 = [r["cross"] for r in scr_rows
                if r["cross"] is not None]
        a20s2 = [r["assist_20"] for r in scr_rows
                 if r["assist_20"] is not None]
        acs2 = [r["assist_cross"] for r in scr_rows
                if r["assist_cross"] is not None]
        pct20_c = float(np.mean([v < a20_main for v in a20s2]))
        pctc_c = float(np.mean([v < ac_main for v in acs2]))
        check("G53-ensemble-scramble", ok_cons2 and ok_spot2,
              "ENS_SCR (%d pinned position scrambles, weights "
              "bitwise == MAIN, crossing == minC+1 spot-gated): "
              "S spread %d..%d; crossings %s..%s; assist_20 med "
              "%.2f (pct %.2f); assist_cross med %.2f (MAIN "
              "%.4f, pct %.2f)"
              % (ENS_SCR_REPS, min(Ss), max(Ss), min(crs2),
                 max(crs2), float(np.median(a20s2)), pct20_c,
                 float(np.median(acs2)), ac_main, pctc_c))

        def pct_typ(p):
            if PCT_BAND[0] <= p <= PCT_BAND[1]:
                return "GENERIC"
            return "LOW_OUTLIER" if p < PCT_BAND[0] \
                else "HIGH_OUTLIER"
        ens_typ = dict(
            sign_early=(pct20_s, pct_typ(pct20_s)),
            sign_wall=(pctc_s, pct_typ(pctc_s)),
            scr_early=(pct20_c, pct_typ(pct20_c)),
            scr_wall=(pctc_c, pct_typ(pctc_c)))
        check("G54-ensemble-adjudication", True,
              "MAIN POSITION (sealed band [%.1f, %.1f]): %s -- "
              "MAIN's EARLY coherence is ensemble-typical, its "
              "WALL coherence is measured against the ensembles "
              "honestly above"
              % (PCT_BAND[0], PCT_BAND[1],
                 str({k: (round(v[0], 2), v[1])
                      for k, v in ens_typ.items()})))

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    evN, VN = np.linalg.eigh(E184)
    uN = VN[:, -1]
    dgN, XN, _gN, _aN = decomp_parts(E184, uN)
    mut1 = mutant_nodiag_assist(E184, uN)
    dev_m1 = abs(dgN + mut1 - float(evN[-1])) \
        / max(abs(float(evN[-1])), 1e-300)
    check("G70-mutant-nodiag", dev_m1 >= M1_BAR,
          "m1 ASSIST WITHOUT DIAGONAL SUBTRACTION: claiming the "
          "whole Rayleigh quotient as interference breaks the "
          "exact decomposition by %.3f rel (>= %.1f) -- LOUD: "
          "the diagonal subtraction is load-bearing"
          % (dev_m1, M1_BAR))
    cs_mut = mutant_unweighted_cs(SP9["cum"], W9["vn"])
    dev_m2 = abs(float(cs_mut[120 - 1])
                 - float(SP9["trace"][120 - 1])) \
        / float(SP9["trace"][120 - 1])
    check("G71-mutant-unweighted", dev_m2 >= M2_BAR,
          "m2 CHRISTOFFEL WITHOUT WEIGHT: dropping v_k breaks "
          "the exact trace identity by %.1e rel at n = 120 "
          "(>= %.1f) -- LOUD" % (dev_m2, M2_BAR))
    tm_mut = mutant_mass_scale(np.array([1.0, 0.5, 0.25, 0.125,
                                         0.0625]))
    okc_m, dev_m3 = cons_check(
        np.array([1, 2, 3, 4, 5], np.int64),
        np.array([1.0, 0.5, 0.25, 0.125, 0.0625]),
        np.array([1, 2, 3, 4, 5], np.int64), tm_mut, 2,
        sign_assignment(5, 2, SEED_BASE))
    check("G72-mutant-conservation", (not okc_m)
          and dev_m3 >= M3_BAR,
          "m3 ENSEMBLE WITHOUT CONSERVATION: the mass-scaling "
          "surgery (x %.2f) is CAUGHT by the conservation gate "
          "(magnitude break %.1e >= %.0e)"
          % (MUT_MASS, dev_m3, M3_BAR))
    hits_m4 = scope_audit("mutant_cross_oracle")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m4) and not hits
          and not ag_hits,
          "m4 CROSS-ORACLE MUTANT FLAGGED (%s); the %d sealed "
          "constructors consume arrays/matrices ONLY (%s); "
          "fragment audit (no fit primitives): %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S7 detector
    section("S7  DETECTOR LEDGER (r281 DISTANCE RULE)")
    if smoke:
        check("G80-detector-ledger", True, "SMOKE: skipped")
        det_typ = {}
    else:
        stats = {"K_D1_maxdiag184": {"MAIN": dmax184},
                 "K_D2_assist_cross": {"MAIN": ac_main},
                 "K_C1_zv_cross": {"MAIN": zv9},
                 "K_B1_nstar_ratio": {"MAIN": math.log10(
                     max(ns9[kbind], 1e-300) / Nw)}}
        for cn in WC:
            spb = SPC[cn]
            nc = ctrl_budget[cn]["cross"]
            stats["K_D1_maxdiag184"][cn] = \
                ctrl_budget[cn]["maxd_184"]
            stats["K_D2_assist_cross"][cn] = \
                ctrl_budget[cn]["assist_c"]
            stats["K_C1_zv_cross"][cn] = z_ctrl[cn][0]
            nsc, _d, _o = nstar_all(WC[cn], R_LOC)
            kb_c = int(np.argmax(spb["cum"][:, WC[cn]["N"] - 1]))
            stats["K_B1_nstar_ratio"][cn] = math.log10(
                max(nsc[kb_c], 1e-300) / WC[cn]["N"])
        det_typ = {nm: LS.dist_rule(tab, list(WC))
                   for nm, tab in stats.items()}
        check("G80-detector-ledger", True,
              "PAIRCORR-STYLE DETECTOR (sealed r281 distance "
              "rule, incl. the b2 classical statistic): %s "
              "(values %s)"
              % (str(det_typ),
                 str({nm: {k: round(v, 4) for k, v in tab.items()}
                      for nm, tab in stats.items()})))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no triangle bound as "
          "certificate, no posthoc window, no equilibrium "
          "substitution (the classical yardstick is a comparison "
          "only), no RH claim; what the round adds: the exact "
          "decomposition bookkeeping, the delta/delta' budget "
          "tables over the ladder + controls, the binding-atom "
          "census with the classical gap statement, and the "
          "coherence adjudication with ensemble position; "
          "r243..r284 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        dec_ok = all(ok for nm, ok, _d in CHECKS
                     if nm in ("G30-decomposition-identities",
                               "G31-w9-budget",
                               "G33-ladder-budgets"))
        parts = []
        parts.append(
            ("DECOMPOSITION_EXACT(mult + additive forms exact; "
             "ladder maxdiag max %.4f / assist max %.4f; ctrl "
             "offdiag share %s)"
             % (max(mds), max(aks),
                str({cn: round(v["offshare"], 2)
                     for cn, v in ctrl_budget.items()})))
            if dec_ok else "DECOMPOSITION_BROKEN(see gate table)")
        parts.append(
            "PERATOM_CLASSICAL(binding ARCH %d/42, u<log2 %d/42; "
            "n*_bind %.0f vs n_DIAG %d oct dev %.2f; coverage "
            "%d/42 -> CLASSICAL_GAP; (D) %s)"
            % (n_arch, n_edgeu, ns9[kbind], NDIAG_REC, oct_dev,
               n_cov, "WORLD_BLIND" if blind_D else "SEPARATES"))
        coh_ok = (blind_D and ac_main <= A_MAIN_BAR
                  and all(v["assist_c"] >= A_CTRL_BAR
                          for v in ctrl_budget.values()))
        parts.append(
            ("COHERENCE_CARRIES_ARITHMETIC(assist_cross MAIN "
             "%.4f <= %.2f vs controls %s >= %.1f; %s)"
             % (ac_main, A_MAIN_BAR,
                str({cn: round(v["assist_c"], 2)
                     for cn, v in ctrl_budget.items()}),
                A_CTRL_BAR, c2_typ))
            if coh_ok else
            "COHERENCE_UNSTRUCTURED(assist_cross MAIN %.4f, "
            "controls %s, blind_D %s)"
            % (ac_main, str({cn: round(v["assist_c"], 2)
                             for cn, v in ctrl_budget.items()}),
               str(blind_D)))
        parts.append("ENSEMBLE_POSITION(%s)"
                     % str({k: (round(v[0], 2), v[1])
                            for k, v in ens_typ.items()}))
        parts.append("DETECTOR_LEDGER(%s)" % str(det_typ))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED decomposition of the open scalar L*; "
          "exact bookkeeping, honest budgets; NO L* claim, NO RH "
          "claim" % (verd, " (SMOKE)" if smoke else ""))
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
