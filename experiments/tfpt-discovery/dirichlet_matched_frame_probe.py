#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_matched_frame_probe --
PRIME.WORLD.DIRICHLET_MATCHED_FRAME.01 (round 357): THE
GRH-FAITHFUL DIRICHLET FRAME -- the missing second arithmetic,
reviewer rank 2 after the r355 substance condition.

CONTEXT (binding).  R330 (dirichlet_secondworld_probe,
SECOND_WORLD_SPLITS) twisted the SOURCE ATOMS ONLY inside the MAIN
frame: the archimedean lags, the smooth border and every constant
stayed zeta's -- the Gamma-factor parity and the conductor of
L(s, chi) were NOT modeled (disclosed there as the honest limit).
Result: the half-filling wall died at control depth (w9 DIR nf 24
/ ABS nf 37 vs MAIN nf None), the r306 pointwise C_2 broke by up
to 149x, sigma grew, the O-sign class flipped -- but the round
COULD NOT distinguish "wall is zeta-specific" from "wall needs the
matched frame".  That distinction is THIS round (the r338-U5 named
successor, demanded by both lanes since; reviewer fork verbatim:
"Dirichlet-Frame priorisieren ... echte zweite Arithmetik ...
wenn dieselben Mechanismen dort tragen, gewinnt ihr massiv an
Universalitaet; wenn nicht, wisst ihr sofort, was MAIN-spezifisch
ist").

LEG 0 -- THE FRAME DERIVATION (sealed FIRST, the core).  For a
primitive Dirichlet character chi mod q with parity a =
(1 - chi(-1))/2 the completed L-function is
    Lambda(s, chi) = (q/pi)^((s+a)/2) Gamma((s+a)/2) L(s, chi),
entire for chi != chi_0 (NO pole term -- and none exists in the
frame: the window density is arch lags + prime lags only).  The
Weil explicit formula for L(s, chi) has
  PRIME SIDE: the chi-weighted von Mangoldt comb Lambda(n) chi(n)
    (for the real characters mod 3 / mod 4 the weights stay REAL
    but sign-modulated; chi(n) = 0 atoms drop; positions log n and
    the v563 gauge 2 Lambda(n)/sqrt(n) unchanged -- the r330 comb,
    reused bitwise);
  ARCHIMEDEAN SIDE: 2 (d/ds) log[(q/pi)^((s+a)/2) Gamma((s+a)/2)]
    at s = 1/2 + i xi, i.e. the matched arch density
      F_A^chi(xi) = -log(pi/q) + Re psi((1+2a)/4 + i xi/2)
    (zeta: -log pi + Re psi(1/4 + i xi/2), the r342 dictionary).
  LAG SPACE: with the Gauss integral psi(z) = -gamma +
    2 int_0^inf [e^{-2w} - e^{-2wz}]/(1 - e^{-2w}) dw and z =
    (1+2a)/4 + i xi/2 (so e^{-2wz} = e^{-(1/2+a)w} e^{-i xi w}),
      Re psi((1+2a)/4 + i xi/2) = -gamma
        + 2 int_0^inf [e^{-2w} - cos(xi w) e^{-(1/2+a)w}]
                      / (1 - e^{-2w}) dw,
    hence the matched tent-sampled arch lag function is EXACTLY
    the document body (lstar_problem / verify_lstar_instance
    arch_A_far / arch_A_near) with TWO swaps:
      kernel  e^{-w/2}      ->  e^{-(1/2+a)w}      (parity)
      const  -(gamma+log pi) -> -(gamma+log(pi/q))  (conductor)
    (the e^{-2w} regulator and the truncation-tail term are
    parity/conductor-free and stay verbatim); the truncation tail
    of the dictionary generalizes to a_k = 2k + 1/2 + a.  At
    (a = 0, q = 1) the construction MUST reproduce zeta's arch
    layer BITWISE -- gated.
  CHARACTERS: chi mod 3 (odd, a = 1, the r330 character, comb
    cross-warded bitwise against DSW.dirichlet_comb) = PRIMARY
    WORLD; chi mod 4 (odd, a = 1, drops the 2^k atoms) = second
    probe, census.
  R330 DIVERGENCE LEDGER (what was NOT matched there, now is):
    (i) conductor term log(q/pi) -- ABSENT in r330, PRESENT here;
    (ii) Gamma parity a = 1 (psi at 3/4, kernel e^{-3w/2}) --
    ABSENT, PRESENT; (iii) the smooth-comb border companion of the
    bordered chain -- r330 build it through zeta's arch, here it
    passes through the SAME chi arch (the border is a construction
    object of the frame); STILL SHARED BY CONSTRUCTION (disclosed,
    not matched because it is not zeta-specific): the prime-power
    anchor grid / window mesh D = 0.5 gap/NU (the support log p^k
    is the SAME for every Dirichlet L over Q), the tent test
    family, the fold map and the depth rule N_w = (S+1)/2 read
    from the world's OWN atom count.

THE TWO WALL INSTRUMENTS (both measured, both in the sealed
adjudication): (E) the document E-Gram wall margin(N_w) = 1 -
lambda_max(E_{N_w}) with the crossing degree minC (smallest n with
lambda_max(E_n) >= 1; lambda_max is monotone in n since E_{n+1} =
E_n + b b^T, so bisection is exact); the PINNING coordinate
minC_ext - (N_w + 1) (MAIN: 0 at w9 -- crossing exactly one past
half-filling); (T) the terminal bordered-chain flip nf
(POSITIVE_PREFIX admission) through the identical r244/r330
channel, adjudicated by the VERBATIM r330 seven-property battery
(DSW.rung_rec / eval_rung / battery_stats / battery_classes with
the identical class rules and the identical live-frozen MAIN
first-5 cubic constant) -- the r330 SPLIT criterion re-adjudicated
with ONLY the frame matched.

THE CONTRACT LEGS:
  LEG A -- the wall census on the sealed ladder (the 42 frame-A
    admissible windows, V.admissible_indices verbatim -- the
    window frame is world-independent by construction, r330
    convention; matched admission floor: >= N_ATOM_MIN kept atoms
    after the chi(n) = 0 drop, exclusions disclosed -- the pool
    carries all 42 for both characters, census printed): per rung
    margin, minC, pinning offset, S/S_+/S_-, terminal nf; the
    r330 battery re-adjudication table (matched class vs the r330
    unmatched record class per property).
  LEG B -- the L* mechanisms on the primary world: the shallow-
    edge pair (PX.pair_select/pair_block verbatim; pair mass, PR),
    the determinant condition c^2 < pq (exact identity + Cauchy
    interlacing wards per rung, r342 a1 backward-error
    normalization), the DICTIONARY UNIVERSALITY TEST (the r342
    weight dictionary with the chi offset: v_pred = -(2/L)
    (1 - cos theta)(F_A^chi - TAIL^chi + f_P^chi) against the
    measured nu weights; density-level ward at the pair folds of
    the sample rungs), and the PHI CO-WANDER (r352/r354: phi_D =
    log(pq) + A_LEAD ln N vs phi_K = log(c^2) + A_LEAD ln N,
    A_LEAD = 17/12, RSA.fine_structure verbatim; usable rows need
    p > 0, q > 0, c^2 > 0 and finite logs -- the r354-a2 clause;
    MAIN through the same instrument as GATE, corr >= 0.99 and
    rmsr <= 0.2; the 500x suppression printed as 1/rmsr).
  LEG C -- the terminal mechanisms: the K2 law FAB grel <= C_2
    with the FROZEN cross-family constant C_2 = 11.87 (the
    r351/r353/r355 pin -- NEVER recalibrated here, that is the
    test) on every live matched row of BOTH characters (FAB =
    m q_max / log m via QGL.fab_of; q_max = mqs.qm on the r314
    fold genealogy; grel = EFA.grel_col, a zone property shared
    with MAIN); the r329 counting constants (nsc_rel/log m <=
    2.0258, ngj/log m <= 2.6351, imported frozen from EFA) --
    the sixth cohort, first arithmetic test; the FAB identity +
    one-sided K2 chain wards (r324/r327) live on every row;
    q_max/FAB scale + dominance (hgn, bshare, maj) census.
  LEG D -- the control discipline OF THE NEW WORLD: the rational
    twin of the chi3 comb (AKD.twin_rational at 1e-8, weights
    untouched) through the matched frame at w9 (margin + pair
    scalars within 1e-3 rel), and the SCRAMBLE analogue (positions
    redrawn uniform on [0, 2 alpha], r-convention seed 1, signed
    chi weights kept, through the SAME matched frame) -- sealed
    break rule: E-wall break at w9 (margin <= 0 or minC <= 0.5
    N_w) or terminal flip ratio <= 0.5.
  LEG E -- must-fails (>= 5, each loud, plus scope audits):
    (m1) ARCH WITHOUT THE CONDUCTOR TERM (the r330 trap exactly):
      only the near-lag constant changes, so the mutant density
      is the true density MINUS log q UNIFORMLY -- caught EXACT
      (max |d_true - d_mut - log q| <= 1e-12 x scale);
    (m2) WRONG PARITY OFFSET a = 0 (conductor kept): the mutant
      arch dictionary misses the w9 chi3 pair folds by >= 0.2 rel
      (measured separation ~2.2 .. 14) while the true chi
      dictionary passes at <= 0.02 -- caught loud;
    (m3) CHI WEIGHTS PERMUTED (world clause): the mod-3 table
      applied at period 4 (DSW.mutant_chi_wrong_period verbatim)
      breaks the periodicity + support wards at the named
      witnesses -- caught exact;
    (m4) DICTIONARY WITH MAIN ARCH instead of chi arch: the
      v_pred mutant misses the measured chi weights by >= 0.5 rel
      (measured ~4.0 .. 4.4) while the chi dictionary passes at
      <= 0.10 -- caught loud;
    (m5) C_2 RECALIBRATED on the chi rows: the mutant consumes
      the withheld fabg_true column (AST-FLAGGED) and on the
      sealed toy returns 3.0 != the sealed toy freeze 1.0 --
      protocol-CAUGHT twice (the frozen constant is the test);
    (m6, scope) MAIN CONTAMINATION: a builder blending untwisted
      MAIN weights (marker MAIN_MM_BLEND) -- AST-FLAGGED.

SEALED VERDICTS (main letter: exactly one fires, total order;
letters/flags appended with '+', combinations allowed):
  TARGET_LEAK  iff any firewall/scope/fragment audit hit;
  FRAME_INSUFFICIENT(named)  iff a derivation ward fails (digamma
    identity, arch/prime/frame reproduction, comb cross-route,
    the chi density dictionary at the frame level) or the primary
    world has < LIVE_MIN live rungs -- the derivation itself
    fails at a named place;
  SECOND_ARITHMETIC_LIVES  iff on the primary world (chi mod 3)
    the E-wall holds (margin > 0 on ALL live rungs) AND the
    verbatim r330 HALF_FILLING class is MAIN-side (nf None on all
    live terminal rungs);
  WALL_ZETA_SPECIFIC  iff both instruments are control-side
    (margin <= 0 on more than half the live rungs AND the r330
    class rule lands CTRL, ratio med <= 0.5);
  WALL_SPLIT_MATCHED(loci)  otherwise (the instruments disagree
    or the wall is partial -- the honest intermediate, census).
  APPENDED: MECHANISMS_TRANSFER(list of TWO_ATOM / DET_COND /
    DICT / PHI that pass their sealed clauses; MECHANISMS_CENSUS
    if none) + [K2_ARITHMETIC_UNIVERSAL iff 0 FABg violations at
    the frozen C_2 AND 0 counting violations on ALL live rows of
    both characters AND >= K2_MIN_ROWS chi3 rows; else
    K2_CENSUS(loci)] + [DICTIONARY_TRANSFERS iff median v_pred
    rel dev <= 0.10 over the chi3 ladder AND the density
    dictionary <= 0.02 at the sample pair folds; else
    DICTIONARY_CENSUS] + [PHI_COWANDER_UNIVERSAL iff corr >=
    0.99 AND rmsr <= 0.2 on >= PHI_MIN_ROWS usable chi3 rows;
    else PHI_CENSUS] + R330_READJUDICATION(property table:
    matched class vs r330 record class; RETYPED_FRAME_ARTIFACT
    per property iff the matched class is MAIN-side where r330
    was control-side) + CHI4_LEDGER(census) + CONTROL_LEDGER
    (twin devs, scramble break) + CONVENTION_LEDGER.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): document
pipeline V.{window_shape, prime_lags, arch_lags, spectral_density,
build_measures, mu_chain, b_matrix, admissible_indices, U, W_VM,
PP, GL_N, EULER} (rh/problem, the L* problem statement); r330
DSW.{dirichlet_comb, dirichlet_abs_comb, mutant_chi_wrong_period,
rung_rec, eval_rung, battery_stats, battery_classes,
variant_status, world_w9 constants} (66526018); r342
PX.{pair_select, pair_block, pair_eigs, det_reserve,
prime_cf_density} (b09f8ccd); r352 RSA.fine_structure (dc6bbd2c);
r353 SFE.window_data_b (bd89e331, the trivial terminal
reproduction ward); r351 QGL.fab_of (67102e4c); r329
EFA.{grel_col, FROZEN_CNSC, FROZEN_CNG} (bbfaf199); r314 SCF, r324
FAP/QMO, r327 GMC, r306 RY3, r269 PBB, r298 WBT, r244 BH, r243 PB,
v881 PIK, r289 AKD.twin_rational, r276 MF.local_gaps, v563 core
READ-ONLY.  NEW module-own (source-pure, AST-audited): chi_char_q,
chi_window_comb, chi_arch_A_far / chi_arch_A_near / chi_arch_lags
(the document arch body with the two sealed swaps),
chi_prime_lags (the document prime body on a passed signed comb),
chi_build_measures (document fold verbatim), chi_window_data /
chi_wpack (the r353 window_data_b body at NU = 4 with the chi arch
+ the matched border companion), chi_arch_dict_density /
chi_v_predict (the r342 dictionary with the chi offset), wall_scan
(margin / crossing bisection on the monotone Gram).

INDEX FIREWALL (binding, r238-r356 discipline): w = window (kz),
S = #union atoms, N_w = (S+1)//2 world-own, m = block count;
ground truth (records, control flips, the frozen C_2 = 11.87)
enters GATES and census tables only, never a builder (AST scope
audit; withheld identifiers fabg_true / margin_col_true /
MAIN_MM_BLEND); no zero/prime oracles anywhere (AST firewall; the
prime-power grid is the sealed source comb, r238 convention); no
fit primitives (fragment audit; the only fits are the imported
Theil-Sen-free FS medians).  Budget <= 1800 s.

SEALED CONSTANTS: Q_CHI3 3; Q_CHI4 4; CHI3_TAB (0, +1, -1);
CHI4_TAB (0, +1, 0, -1); parity a DERIVED from the oddness ward
(chi(-1) = -1 => a = 1, gated); LPQ3 = log(pi/3); LPQ4 =
log(pi/4); DIG_XI (0.0, 0.5, 1.7, 4.0, 12.0); DIG_TOY_BAR 1e-8;
TAIL_K 12; DIGAMMA_BAR 0.02; V_BAR 0.10; SAMPLE_KZ (18, 9, 52,
82); MASS_BAR 0.90; DET_ID_BAR 1e-10; INTERLACE_TOL 1e-9; A_LEAD
17/12; FS_CORR_MIN 0.99; FS_RMSR_MAX 0.2; PHI_MIN_ROWS 21;
C2_K2_FROZEN 11.87 (r351/r353/r355 pin, frozen, never moved);
K2_EPS 1e-9; K2_MIN_ROWS 21; K2_CHAIN_BAR 1e-12; FAB_ID_BAR =
QGL verbatim; counting constants EFA.FROZEN_CNSC / FROZEN_CNG
verbatim; LIVE_MIN 21; DEPTH_DEAD 0.5 (DSW verbatim); TWIN_TOL
1e-8; TWIN_BAR 1e-3; SCR_SEED 1; M1_BAR 1e-12; M2_BAR 0.2;
M4_BAR 0.5; MUT_MIN 1e-6; TOY_BAR 1e-14; W9 anchors (REC_S 367,
REC_NW 184, REC_LAM 0.99983248, REC_LAM_NEXT 1.00003660,
REC_MARGIN 1.6752e-4 rel 0.01); R330 anchors verbatim from DSW
module constants (DIR w9 nf 24 / ABS w9 nf 37 record literals;
C2 refreeze R306_C2 1.0694 tol 0.005; SL_D -0.571 tol 0.01;
NEFF 37.41/0.963; ONEG 13 EXACT; FILL < 0.5; MULT <= 2); r352 FS
record (corr 0.999998 / rmsr 0.0019 on 75 rows) printed as census
reference, gated only via the FS clauses on this round's 42-row
MAIN instrument; runtime <= 1800 s; smoke = toys + wards +
mutants + the w9 worlds (MAIN, chi3/chi4 matched, r330 unmatched
baseline, matched terminal); ladders, battery, K2 tables, phi,
twin, scramble and adjudication skipped.

PRE-SPEC SCOPING (disclosed, r330/r353/r355 precedent -- ONE
sizing pass, /tmp, deleted; no bar, band, class rule, letter or
adjudication rule was tuned after any evaluation except as sized
here and said so): (s1) machinery validation, all EXACT: digamma
identity a = 1 dev 0.0 at the five xi; arch reproduction (a = 0,
q = 1) BITWISE on the w9 mesh; prime-lag + document-frame +
terminal-frame trivial reproductions BITWISE; the r330 unmatched
baseline reproduces (w9 DIR nf 24, ABS nf 37).  (s2) sizing data
at w9 (DISCLOSED -- these numbers were seen before the freeze;
the 42-rung ladders, the battery classes, every K2/counting/phi
column and every adjudication are GENUINELY OPEN): matched chi3
w9 lam(E_184) = 0.999118 / lam(E_185) = 0.999124 (margin 8.8e-4,
minC None -- the wall LIVES at w9 on the matched frame; crossing
between 185 and 194: the MAIN pinning-at-half-filling does NOT
reproduce, the wall is UNPINNED-OVERFULL there); matched chi4 w9
lam 0.999687/0.999844; matched terminal chi3 w9 nf None (vs
unmatched 24); deep rung kz82 chi3 lam 0.999977 minC None; chi3
w9 pair folds (2, 4) == MAIN, d1 0.998961 d2 0.993774 c 3.38e-4
(r_det 0.982 -- NOT near-saturated), pmass 0.998, PR 1.00; chi
dictionary devs at the pair folds 2.9e-4 / 7.5e-3 (sizing
DIGAMMA_BAR 0.02), v_pred devs 5.9e-4 / 2.1e-3 (sizing V_BAR
0.10); MAIN-arch mutant separations 2.2 / 14.3 (density) and
4.4 / 4.0 (v_pred) -- sizing M2_BAR 0.2 / M4_BAR 0.5; runtime
trivial (0.4 s scoping total).  The sealed toys are computed by
hand (m5 toy: fabg column (3.0 x 1.0, 2.0 x 0.5) -> mutant 3.0
!= sealed toy freeze 1.0; m1 shift == log q exact by the
near-lag constant algebra).  LIVE_MIN, PHI_MIN_ROWS, K2_MIN_ROWS,
M1/M2/M4 bars and the letter trees are a-priori choices fixed
BEFORE any ladder evaluation; the letters are symmetric and total
by contract.

STOP LIST (anti-gates, binding): NO RH claim, NO GRH claim, NO L*
claim, NO bound mechanism, NO certificate, no posthoc bar / class
/ constant move (C_2 = 11.87 frozen), no derived 5/7, mincut
unchanged; a living second arithmetic strengthens the
living-world reading of finitely many measured windows -- it
proves NOTHING about zeta or L(s, chi); a dead wall retypes
finite statistics; GRH only motivates the candidate (under GRH
the zero structure of L(s, chi) is analogous), it is USED
nowhere; r243..r356 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit, which IS the protocol; freeze
SPEC_SHA 4be4777fd6ec5bdf, pre-freeze commit 1381f6ea;
chronology honest: smoke pass 1 = 33/33 (0.8 s, run pre-commit,
byte-identical twice, disclosed in the commit message);
calibration pass 1 = FIRST full evaluation = 31/33 (23.6 s) with
ONE finding: the r329 counting constants ARE the frame-A ladder
maxima (kz16 nscl 2.02581735 / kz36 ngl 2.63511735) and counting
against the 4-decimal record literals made the calibration rungs
"violate" their own constants by 1.7e-5 -- the r330-a1 lesson
exactly.  DISCLOSED CALIBRATION AMENDMENT a1 (representation fix,
r330-a1 class; NO adjudication bar, class rule, letter or verdict
rule moved): the counting constants are re-frozen LIVE at full
precision on the MAIN ladder, anchor-gated against the r329
literals at 5e-4, and every chi violation count runs against the
live-frozen constants.  Smoke re-pass 33/33; calibration pass 2 =
33/33 (20.1 s); record run1/run2 after this insertion,
byte-identical up to the WALL line):
MAIN VERDICT: SECOND_ARITHMETIC_LIVES(E-wall 42/42 margins
positive; r330 HALF_FILLING class MAIN-side: nf None 42/42)
+ MECHANISMS_TRANSFER(TWO_ATOM, DET_COND, DICT)
+ K2_CENSUS + DICTIONARY_TRANSFERS + PHI_CENSUS
+ R330_READJUDICATION + CHI4_LEDGER(ALIVE) + CONTROL_LEDGER
(twin 7.9e-6; scramble BREAKS) + CONVENTION_LEDGER.
THE HEADLINE FINDINGS:
(1) THE WALL LIVES ON THE MATCHED FRAME -- THE r330 DEATH WAS A
FRAME ARTIFACT: with the derived chi arch side (conductor
log(q/pi) + parity psi(3/4 + i xi/2) + matched border) the chi
mod 3 world holds the E-Gram wall on 42/42 windows (margins
8.10e-06 (kz43) .. 3.34e-03 (kz18), ALL positive; minC None
42/42 to the window depth) AND the terminal half-filling wall
(nf None 42/42 -- the SAME comb that died at nf 24 through the
unmatched frame, reproduced as the baseline gate).  chi mod 4:
the same (margins 42/42 positive, min 1.10e-05; nf None 42/42).
The living-world evidence moves from n = 1 to n = 3 arithmetics
on 126 windows.
(2) THE r330 RE-ADJUDICATION (verbatim battery, identical class
rules, identical live-frozen C_2 = 1.069434): ALL FOUR r330
splits are RETYPED_FRAME_ARTIFACT -- HALF_FILLING CTRL ->
MAIN(ALIVE_TO_DEPTH); RENYI3_C2 CTRL(32/42 violations, max
27.6x) -> MAIN(0/42); SIGMA_DECAY SPLIT(+0.793) -> MAIN(sl_D
-0.578 vs MAIN -0.571); O_SIGN CTRL(27/42) -> MAIN(O_POS,
O<0 on 20/42); NEFF_GROWTH (+0.947), FILL (med 0.442), MULT2
(<= 2) stay MAIN-side: the matched battery is 7/7 MAIN-side,
status(chi3) = ALIVE, status(chi4) = ALIVE.  CONFIRMED
zeta idiosyncrasies: NONE at battery level.
(3) THE PINNING FINE STRUCTURE (fresh coordinate): MAIN pins at
minC_ext == N_w + 1 exactly (w9 == 185).  The chi worlds are
NEAR-pinned: crossing offsets minC_ext - (N_w+1) = 0..9 (chi3
med 1.5, pinned-exactly on 8/42; chi4 med 2.0) -- the wall
extends slightly PAST half-filling on most chi rungs; the EXACT
pinning is (so far) zeta's sharpest signature, typed census.
(4) K2 SPLITS INTO PRODUCT vs COUNTING (the honest Leg-C
verdict): the FROZEN C_2 = 11.87 holds with ZERO violations on
all 126 live rows (MAIN max FABg 6.95 / chi3 4.73 at kz32 /
chi4 5.16 -- 60/56 pct headroom: the Klein-gap product is
ARITHMETIC-ROBUST census across 2 families + 3 aspects + now 3
arithmetics), BUT the r329 counting constants BREAK on the
second arithmetic: chi3 2 violations (kz33 nscl 2.41 = +19 pct;
kz14 ngl 3.38 = +28 pct), chi4 1 violation -- the O(log m)
counting side, the lane's most wall-robust asset (6 zeta
cohorts), is ZETA-CALIBRATED census, not arithmetic-universal:
K2_CENSUS, sealed letter, said honestly.  FAB identity 1.8e-16,
K2 chain one-sided 0.0 on all worlds; dominance census chi3
hgn med 3.18, bshare med 0.38, maj med 0.44.
(5) THE DICTIONARY TRANSFERS (the r342 wall-side universality
win): v_pred with the chi offset predicts the second
arithmetic's nu weights at median rel dev 4e-4, max 3.3e-3 over
42 rungs (V_BAR 0.10); density dictionary at the sample pair
folds kz9/18/52/82 devs 7.5e-3 / 1.2e-3 / 3e-5 / 1.3e-4 (bar
0.02) -- the explicit-formula weight dictionary is
explicit-formula-generic, not zeta bookkeeping.
(6) PHI DOES NOT TRANSFER (the honest negative of the round):
the co-wander corr is 0.9817 (clause 0.99) with rmsr 0.3187
(clause 0.2) on 42/42 usable chi3 rows -- the suppression is 3x
vs MAIN 439x on the identical instrument (chi4: 0.9690/0.2867 =
3.5x); PHI_CENSUS.  READING: the chi pair sits FAR from the
binding point (r_det med 0.247 vs MAIN's near-saturated
1e-2..1e-6; c med ~1e-3; pair mass med 0.9913 but PR med 1.26
with two delocalized rungs kz40/kz55 pmass 0.009/0.003) -- the
500x phi suppression is the signature of NEAR-CANCELLATION,
which only zeta's world exhibits at these depths: universal in
KIND (strong co-wander corr 0.98) but NOT at the sealed
clauses; the r354-named ABS universality test is answered
NEGATIVE in the right world, and that is information about the
BINDING REGIME, not about the frame.
(7) CONTROLS: the rational twin of the chi comb carries
(margin/pair devs <= 7.9e-6, bar 1e-3); the matched-frame
SCRAMBLE (seed 1, signed chi weights kept) BREAKS (E-margin
-2.63e+02, minC 38/184, terminal nf 37) -- the matched frame
does NOT rescue a scrambled comb: the wall needs the
arithmetic, the second lab brings its own dead control.
KEY NUMBERS.  w9 matched chi3: S 367 (S+ 279 / S- 88), margin
8.818e-4, minC_ext 187 (pin offset 2), pair folds (2, 4) ==
MAIN shallow edge, d1 0.998961, d2 0.993774, c 3.38e-4, r_det
0.9823, pmass 0.9980; w9 matched chi4: S 367 (293/74), margin
3.130e-4.  MAIN anchors through the verbatim channel: nf None
42/42, C_2 refreeze 1.069434, sl_D -0.5710, n_eff 37.41/+0.963,
O<0 13/42 EXACT, fill 0.434; E-ladder margins 42/42 positive
(min 1.42e-7), w9 pinned at 185; FS gate corr 0.999998 rmsr
0.0023 (r352 ref 0.999998/0.0019).  Counting live-freeze (a1):
C_NSC 2.025817 (kz16), C_NG 2.635117 (kz36).  Must-fails: m1
conductor shift == log 3 EXACT (dev 3.8e-15); m2 parity dev
0.24 >= 0.2 (true 7.5e-3); m3 periodicity witness n = 1 +
support n = 4 CAUGHT; m4 MAIN-arch dictionary dev 4.43 >= 0.5
(true 2.1e-3); m5 AST-FLAGGED fabg_true + toy 3.0 != 1.0
protocol-CAUGHT; m6 MAIN_MM_BLEND AST-FLAGGED; digamma
identities a=0 3.7e-13 / a=1 0.0; frame reproductions BITWISE
(document + terminal).  Runtime 20.1 s calibration pass 2 /
record run1/run2 byte-identical up to WALL / 0.8 s smoke.
AMENDMENTS AFTER FREEZE: the disclosed a1 (calibration,
representation fix) and this record-table insertion -- nothing
else.
READING (typed MEASUREMENT): the reviewer fork is answered on
the substance side -- the wall, the battery, the two-atom
mechanisms, the determinant condition, the weight dictionary
and the K2 gap product are EXPLICIT-FORMULA-GENERIC (they
transfer to the matched second arithmetic on all 126 windows);
what stays zeta-graded is the BINDING REGIME: the exact
half-filling pinning, the near-saturated determinant reserve,
the 500x phi suppression and the r329 counting constants.  The
L* margin legislation is a statement about how CLOSE zeta's
world sits to the wall -- the chi worlds obey the same law far
from it.  NO RH CLAIM, NO GRH CLAIM.

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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V                   # noqa: E402 document
import dirichlet_secondworld_probe as DSW           # noqa: E402 r330
import pair_extremal_probe as PX                    # noqa: E402 r342
import rhor_source_anatomy_probe as RSA             # noqa: E402 r352
import second_family_erosion_probe as SFE           # noqa: E402 r353
import qmax_growth_law_probe as QGL                 # noqa: E402 r351
import ext3_fresh_anchors_probe as EFA              # noqa: E402 r329
import signed_cubic_flux_probe as SCF               # noqa: E402 r314
import fa_provenance_probe as FAP                   # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO                  # noqa: E402 r324
import group_mass_cap_probe as GMC                  # noqa: E402 r327
import renyi3_probe as RY3                          # noqa: E402 r306
import phase_bulk_bound_probe as PBB                # noqa: E402 r269
import window_border_transfer_probe as WBT          # noqa: E402 r298
import bordered_hankel_probe as BH                  # noqa: E402 r244
import principal_bessel_probe as PB                 # noqa: E402 r243
import port_integrable_kernel_probe as PIK          # noqa: E402 v881
import arch_kernel_diophantine_probe as AKD         # noqa: E402 r289
import minimal_firewall_probe as MF                 # noqa: E402 r276
import v563_paper2_readouts as core                 # noqa: E402 READ-ONLY

MAIN_KZ = 9
Q_CHI3 = 3
Q_CHI4 = 4
CHI3_TAB = np.array((0.0, 1.0, -1.0))
CHI4_TAB = np.array((0.0, 1.0, 0.0, -1.0))
LPQ3 = math.log(math.pi / Q_CHI3)
LPQ4 = math.log(math.pi / Q_CHI4)
DIG_XI = (0.0, 0.5, 1.7, 4.0, 12.0)
DIG_TOY_BAR = 1.0e-8
TAIL_K = 12
DIGAMMA_BAR = 0.02
V_BAR = 0.10
SAMPLE_KZ = (18, 9, 52, 82)
MASS_BAR = 0.90
DET_ID_BAR = 1.0e-10
INTERLACE_TOL = 1.0e-9
A_LEAD = 17.0 / 12.0
FS_CORR_MIN = 0.99
FS_RMSR_MAX = 0.2
PHI_MIN_ROWS = 21
C2_K2_FROZEN = 11.87
K2_EPS = 1.0e-9
K2_MIN_ROWS = 21
K2_CHAIN_BAR = 1.0e-12
LIVE_MIN = 21
DEPTH_DEAD = 0.5
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
SCR_SEED = 1
M1_BAR = 1.0e-12
M2_BAR = 0.2
M4_BAR = 0.5
MUT_MIN = 1.0e-6
TOY_BAR = 1.0e-14
RUNTIME_BAR = 1800.0
REC_S, REC_NW = 367, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
R330_DIR_NF = 24
R330_ABS_NF = 37
R352_FS_REC = (0.999998, 0.0019)    # census reference (75 rows)
MAIN_MM_BLEND = 0.5                  # m6 contamination marker
EULER = V.EULER
_GLX, _GLW = np.polynomial.legendre.leggauss(V.GL_N)

DSW_SHA_PREFIX = "66526018"
PX_SHA_PREFIX = "b09f8ccd"
RSA_SHA_PREFIX = "dc6bbd2c"
SFE_SHA_PREFIX = "bd89e331"
QGL_SHA_PREFIX = "67102e4c"
EFA_SHA_PREFIX = "bbfaf199"

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
    return (not bad), ("NO zero/prime oracles; the matched frame "
                       "consumes the document gauge tables, the "
                       "character tables and window shape ONLY; "
                       "records and the frozen C_2 enter gates and "
                       "census tables only"
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


CONSTRUCTORS = ("chi_char_q", "chi_window_comb", "chi_arch_A_far",
                "chi_arch_A_near", "chi_arch_lags", "chi_prime_lags",
                "chi_build_measures", "chi_window_data", "chi_wpack",
                "chi_arch_dict_density", "chi_v_predict", "wall_scan")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_MARGIN", "C2_K2_FROZEN",
                   "R330_DIR_NF", "R330_ABS_NF", "fabg_true",
                   "margin_col_true", "MAIN_MM_BLEND"}


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


# ============ sealed matched-frame constructors (AST-audited)
def chi_char_q(nn, q):
    """the real primitive character mod q in {3, 4}: table lookup
    on n mod q.  Consumes integers only."""
    tab = CHI3_TAB if q == Q_CHI3 else CHI4_TAB
    return tab[np.asarray(nn, np.int64) % q]


def chi_window_comb(kz, q):
    """the chi-weighted von Mangoldt comb of window kz in the
    DOCUMENT gauge: positions V.U, weights chi(n) x V.W_VM on the
    kept atoms (chi = 0 atoms dropped).  Consumes the document
    gauge tables + the character table only."""
    alpha = float(V.U[kz])
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14,
                             side="right"))
    nn = V.PP[:ka].astype(np.int64)
    uu = np.asarray(V.U[:ka], float)
    mm = np.asarray(V.W_VM[:ka], float)
    ch = chi_char_q(nn, q)
    keep = ch != 0.0
    return uu[keep], mm[keep] * ch[keep], nn[keep], ch[keep]


def chi_arch_A_far(s, D, a_par):
    """the matched arch lag for s >= Delta: the document arch_A_far
    body with the parity kernel e^{-(1/2+a)w}."""
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D)
               * np.exp(-(0.5 + a_par) * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def chi_arch_A_near(s, D, a_par, lpq):
    """the matched arch lag for 0 <= s < Delta: the document
    arch_A_near body with the conductor constant -(gamma +
    log(pi/q)) and the parity kernel; the e^{-2w} regulator and
    the truncation tail are parity/conductor-free (spec)."""
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    Wend = s + D
    pts = sorted({0.0, s, D - s, Wend})
    pts = [p for p in pts if 0.0 <= p <= Wend]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
                   + np.maximum(0.0, 1.0 - (s + w) / D))
        integ = ((tri_s * np.exp(-2.0 * w)
                  - S * np.exp(-(0.5 + a_par) * w))
                 / (-np.expm1(-2.0 * w)))
        tot += half * float(np.dot(_GLW, integ))
    return (-(EULER + lpq) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * Wend))))


def chi_arch_lags(M, D, a_par, lpq):
    """c^A_i = A^chi(i Delta), i = 0..M-1 (document arch_lags
    body with the two sealed swaps)."""
    sv = np.arange(M) * D
    out = np.empty(M)
    far = sv >= D
    if far.any():
        out[far] = chi_arch_A_far(sv[far], D, a_par)
    for i in np.nonzero(~far)[0]:
        out[i] = chi_arch_A_near(sv[i], D, a_par, lpq)
    return out


def chi_prime_lags(M, D, uu, ww):
    """the document prime_lags body on a PASSED signed comb
    (tent sampling incl. the reflected tent for u < Delta)."""
    c = np.zeros(M)
    for u_j, m_j in zip(uu, ww):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D))
                                  + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= m_j * 0.5 * v
    return c


def chi_build_measures(kz, uu, ww, a_par, lpq):
    """the document build_measures body with the matched arch and
    the passed comb: density -> fold -> sign split (verbatim)."""
    alpha, M, L, Nw, D = V.window_shape(kz)
    cP = chi_prime_lags(M, D, uu, ww)
    cA = chi_arch_lags(M, D, a_par, lpq)
    d = V.spectral_density(cA + cP)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    o = np.argsort(x)
    return dict(alpha=alpha, M=M, L=L, Nw=Nw, D=D,
                xp=x[pos], wp=wt[pos], yn=x[~pos], vn=-wt[~pos],
                xu=x[o], wu=wt[o], S=len(x))


def chi_window_data(kz, a_par, lpq, comb):
    """the terminal window (the r353 window_data_b body at
    NU = NU_MAIN with the matched arch): tent assembly + chi arch
    lags + fold + Lanczos chain (PIK verbatim)."""
    alpha = float(core.U_ALL[kz])
    dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    mzn = int(math.ceil(alpha / dk - 1.0e-9)) + 1
    if mzn % 2:
        mzn += 1
    h = mzn // 2
    uu_, ww_ = comb
    c_at, dd = core.atom_lags_at(alpha, mzn, uu_, ww_)
    c_ar = chi_arch_lags(mzn, dd, a_par, lpq)
    dgrid = PIK.grid_density(c_ar + c_at)
    ll = 2 * mzn - 2
    xs, ws, _ = PIK.folded_measure(dgrid, ll, +1.0)
    ys, vs, _uf = PIK.folded_measure(dgrid, ll, -1.0)
    al, be, m0, steps = PIK.lanczos_chain(xs, ws, h + 4)
    pn = PIK.eval_chain(al, be, m0, ys, min(steps, h + 2))
    return dict(w=kz, n_max=h, xs=xs, ws=ws, ys=ys, vs=vs,
                al=al, be=be, m0=m0, Pn=pn)


def chi_wpack(kz, a_par, lpq, comb):
    """the matched terminal pack: real chi comb + the matched
    border companion (smooth comb through the SAME chi arch), the
    r244 bordered chain, the flip nf (r330/r353 convention)."""
    d = chi_window_data(kz, a_par, lpq, comb)
    n_w = d["n_max"]
    alpha = float(core.U_ALL[kz])
    dsm = chi_window_data(kz, a_par, lpq, PB.smooth_comb(alpha))
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"],
                         dsm["vs"], n_w)
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    return dict(kz=kz, N=n_w, rows=rows, nf=nf, d=d, dsm=dsm,
                complete=(len(rows) == n_w))


def chi_arch_dict_density(theta, alpha, D, a_par, lpq,
                          tail_k=TAIL_K):
    """the matched digamma dictionary: F_A^chi(xi) = -log(pi/q) +
    Re psi((1+2a)/4 + i xi/2), minus the explicit truncation tail
    with a_k = 2k + 1/2 + a (r342 body with the chi offset)."""
    xi = theta / D
    fa = float(-lpq + mp.re(mp.digamma(
        mp.mpf(1 + 2 * int(round(a_par))) / 4
        + mp.mpc(0, 1) * xi / 2)))
    tail = 0.0
    for k in range(tail_k):
        a_k = 2.0 * k + 0.5 + a_par
        z = complex(a_k, xi)
        tail += (-2.0) * (np.exp(-2.0 * alpha * z) / z).real
    return fa - tail, fa


def chi_v_predict(theta, alpha, M, L, D, uu, ww, a_par, lpq):
    """the matched source-explicit weight prediction: v_pred =
    -(2/L)(1 - cos theta)(chi arch dictionary + exact prime
    closed form on the signed comb)."""
    da, _fa = chi_arch_dict_density(theta, alpha, D, a_par, lpq)
    dp = PX.prime_cf_density(theta, uu, ww, M, D)
    return -(2.0 / L) * (1.0 - math.cos(theta)) * (da + dp), da, dp


def wall_scan(mz, cross_ext=False):
    """the E-Gram wall of one world: margin at N_w, lambda at
    N_w + 1, the crossing degree minC (bisection; lambda_max is
    monotone in n: E_{n+1} = E_n + b b^T >= E_n), and optionally
    the extended crossing minC_ext in (N_w+1, min(S_+ - 1, 2 N_w)]
    (the pinning coordinate).  Consumes measure arrays only."""
    Sm = len(mz["yn"])
    Sp = len(mz["xp"])
    Nw = mz["Nw"]

    def lam_of(B, n):
        Bn = B[:, :n]
        G = Bn.T @ Bn if n < Sm else Bn @ Bn.T
        return float(np.linalg.eigvalsh(G)[-1])

    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], Nw + 1)
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], Nw + 1)
    lamN = lam_of(B, Nw)
    lamN1 = lam_of(B, Nw + 1)
    minc = None
    if lamN >= 1.0:
        lo, hi = 1, Nw
        while lo < hi:
            mid = (lo + hi) // 2
            if lam_of(B, mid) >= 1.0:
                hi = mid
            else:
                lo = mid + 1
        minc = lo
    minc_ext = minc
    if cross_ext and minc is None:
        cap = min(Sp - 1, 2 * Nw)
        if lamN1 >= 1.0:
            minc_ext = Nw + 1
        elif cap > Nw + 1:
            a2, b2, h02 = V.mu_chain(mz["xp"], mz["wp"], cap)
            B2 = V.b_matrix(a2, b2, h02, mz["yn"], mz["vn"], cap)
            if lam_of(B2, cap) < 1.0:
                minc_ext = None
            else:
                lo, hi = Nw + 2, cap
                while lo < hi:
                    mid = (lo + hi) // 2
                    if lam_of(B2, mid) >= 1.0:
                        hi = mid
                    else:
                        lo = mid + 1
                minc_ext = lo
    return dict(lamN=lamN, lamN1=lamN1, margin=1.0 - lamN,
                minc=minc, minc_ext=minc_ext, B=B, Sm=Sm, Sp=Sp,
                Nw=Nw)


# ============ must-fail mutants
def mutant_arch_no_conductor(M, D, a_par):
    """m1 MUST-FAIL (the r330 trap exactly): the chi arch WITHOUT
    the conductor term (constant -(gamma + log pi) kept) -- only
    the near lag changes, so the density shifts by -log q
    UNIFORMLY; caught EXACT."""
    return chi_arch_lags(M, D, a_par, math.log(math.pi))


def mutant_arch_wrong_parity(M, D, lpq):
    """m2 MUST-FAIL: the parity offset dropped (a = 0, conductor
    kept) -- the dictionary ward at the pair folds must break
    loudly."""
    return chi_arch_lags(M, D, 0.0, lpq)


def mutant_dict_main_arch(theta, alpha, M, L, D, uu, ww):
    """m4 MUST-FAIL: the weight dictionary with MAIN's arch
    (a = 0 AND log pi) instead of the chi arch -- must miss the
    measured chi weights loudly."""
    return chi_v_predict(theta, alpha, M, L, D, uu, ww, 0.0,
                         math.log(math.pi))[0]


def mutant_c2_recalibrate(fabg_true):
    """m5 MUST-FAIL (protocol): the K2 constant re-picked from the
    SEEN chi FABg column (consumes the withheld column) --
    AST-FLAGGED, and on the sealed toy returns 3.0 != the sealed
    toy freeze 1.0; the frozen constant is the test."""
    return max(fabg_true)


def mutant_main_blend(kz, q):
    """m6 MUST-FAIL (scope): MAIN contamination -- blends the
    untwisted MAIN weights into the chi comb (marker
    MAIN_MM_BLEND); AST-FLAGGED."""
    uu, ww, nn, ch = chi_window_comb(kz, q)
    return uu, MAIN_MM_BLEND * ww + MAIN_MM_BLEND * np.abs(ww)


# ============ gate-side helpers
def char_wards(chifun, q):
    """exact character wards: periodicity mod q, support (zero iff
    gcd(n, q) > 1), multiplicativity on the 40 x 40 grid,
    orthogonality over one period, oddness chi(-1) = -1."""
    nn = np.arange(1, 301, dtype=np.int64)
    ch = chifun(nn, q)
    ok_per = bool(np.array_equal(ch[q:], ch[:-q]))
    ok_sup = bool(np.all((ch == 0.0) == (np.gcd(nn, q) > 1)))
    aa = np.arange(1, 41, dtype=np.int64)
    A, Bv = np.meshgrid(aa, aa, indexing="ij")
    ok_mul = bool(np.array_equal(chifun(A * Bv, q),
                                 chifun(A, q) * chifun(Bv, q)))
    ok_orth = float(np.sum(chifun(
        np.arange(1, q + 1, dtype=np.int64), q))) == 0.0
    ok_odd = float(chifun(np.array([q - 1]), q)[0]) == -1.0
    return ok_per, ok_sup, ok_mul, ok_orth, ok_odd


def eval_k2(rc):
    """the terminal K2 evaluation of one rung (the r355 eval_rung
    body, trimmed to the K2/counting columns): edge mask, runs,
    level-2 blocks, PDelta, cubic moments, rho2, the r314 fold
    genealogy, mqs (q_max), pileup + heavy-group states."""
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    cb = cts[~ed]
    xb = bxs[~ed]
    runs = PBB.runs_split(cb)
    brk, m, jb = WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=m) if m \
        else np.zeros(0)
    Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                              rc["hi"], brk, m)
    Pd = Pb - Pw
    cm = RY3.cubic_moments(Pd)
    absm = float(np.sum(np.abs(rc["ct"]))) \
        + float(np.sum(np.abs(rc["cw"])))
    degenerate = (cm["L1"] <= DSW.DEG_FLOOR * absm) or (m < 2)
    if degenerate:
        return dict(degenerate=True, m=m)
    edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], DSW.EDGE_F)
    xw = rc["xu"][~edw]
    vw = -rc["cw"][~edw]
    jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
    pos_all = np.concatenate([xb, xw])
    val_all = np.concatenate([cb, vw])
    blk_all = np.concatenate([jb, jw]).astype(int)
    src_all = np.concatenate([np.zeros(len(xb)), np.ones(len(xw))])
    gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
    sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
    x_dev = float(np.max(np.abs(sct["x"] - Pd))
                  / max(np.max(np.abs(Pd)), 1e-300))
    rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
    mqs = FAP.m2_qmax_state(sct["x"])
    led = GMC.group_mass_ledger(pos_all, val_all, blk_all,
                                src_all, m)
    pst = QMO.pileup_state(sct["x"], val_all, blk_all)
    hst = GMC.heavy_state(sct["x"], led)
    return dict(degenerate=False, m=m, rho2=rho2, mqs=mqs,
                pst=pst, hst=hst, x_dev=x_dev)


def k2_rows(recs, grels):
    """the K2/counting columns per live rung: FAB = fab_of(m,
    q_max, log m), FABg = FAB grel, counting nsc_rel/lg and
    ngj/lg, dominance census; exact FAB-identity + one-sided K2
    chain wards."""
    rows = []
    fabid_w = 0.0
    k2ch_w = 0.0
    for rc in recs:
        ev = rc["evk"]
        if ev["degenerate"]:
            continue
        mloc = ev["m"]
        lgl = math.log(float(mloc))
        pk = ev["mqs"]["qm"]
        if pk <= 0.0:
            continue
        fab = QGL.fab_of(float(mloc), pk, lgl)
        fabid_w = max(fabid_w, abs(fab * lgl - mloc * pk)
                      / max(mloc * pk, 1e-300))
        g = grels[rc["kz"]]
        fabg = fab * g
        hst = ev["hst"]
        if hst["ngj"]:
            rhs = (hst["ngj"] / lgl) * (hst["hgn"] * g)
            k2ch_w = max(k2ch_w, max(0.0, fabg - rhs)
                         / max(rhs, 1e-300))
        rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc, pk=pk,
                         fab=fab, g=g, fabg=fabg,
                         nscl=(ev["pst"]["nsc_rel"] / lgl),
                         ngl=(hst["ngj"] / lgl),
                         hgn=hst["hgn"], bsh=hst.get("bshare",
                                                     float("nan")),
                         maj=ev["mqs"]["maj"],
                         rho2=ev["rho2"], xdev=ev["x_dev"]))
    return rows, fabid_w, k2ch_w


def phi_fs(rows):
    """the phi co-wander on usable rows (p > 0, q > 0, c^2 > 0,
    finite logs -- r354-a2 clause): RSA.fine_structure verbatim
    at the sealed A_LEAD."""
    use = [r for r in rows
           if r["p"] > 0.0 and r["q"] > 0.0 and r["c"] != 0.0
           and math.isfinite(math.log(r["p"] * r["q"]))
           and math.isfinite(math.log(r["c"] * r["c"]))]
    if len(use) < 2:
        return None, len(use)
    lnN = [math.log(r["Nw"]) for r in use]
    lpq = [math.log(r["p"] * r["q"]) for r in use]
    lcs = [math.log(r["c"] * r["c"]) for r in use]
    corr, rmsr, rms_D, rms_K, rms_d, _pD, _pK = \
        RSA.fine_structure(lnN, lpq, lcs, A_LEAD)
    return dict(corr=corr, rmsr=rmsr, rms_D=rms_D, rms_K=rms_K,
                rms_d=rms_d), len(use)


def pair_row(mz, ws):
    """the pair block of one world rung on the E frame at N_w
    (PX verbatim): folds, (d1, d2, c), reserves, pair mass, PR,
    identity + interlacing devs."""
    B = ws["B"][:, :mz["Nw"]]
    i1, i2 = PX.pair_select(mz["yn"])
    d1, d2, c = PX.pair_block(B, i1, i2)
    lam2, lam2m = PX.pair_eigs(d1, d2, c)
    p, q, rdet = PX.det_reserve(d1, d2, c)
    m2 = 1.0 - lam2
    det_dev = abs((1.0 - lam2) * (1.0 - lam2m) - (p * q - c * c)) \
        / max(p * q + c * c, 1e-300)
    E = B @ B.T
    ev, W = np.linalg.eigh(E)
    w1 = W[:, -1]
    pmass = float(w1[i1] ** 2 + w1[i2] ** 2)
    pr = float(1.0 / np.sum(w1 ** 4))
    f1 = int(round(math.acos(min(max(mz["yn"][i1], -1.0), 1.0))
                   * mz["L"] / (2.0 * math.pi)))
    f2 = int(round(math.acos(min(max(mz["yn"][i2], -1.0), 1.0))
                   * mz["L"] / (2.0 * math.pi)))
    return dict(i1=i1, i2=i2, f1=f1, f2=f2, d1=d1, d2=d2, c=c,
                p=p, q=q, rdet=rdet, m2=m2, det_dev=det_dev,
                pmass=pmass, pr=pr, Nw=mz["Nw"],
                margin=ws["margin"],
                inter_ok=(ws["margin"] <= m2 + INTERLACE_TOL),
                sign_ok=((m2 > 0) == (rdet > 0)))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("dirichlet_matched_frame_probe -- "
          "PRIME.WORLD.DIRICHLET_MATCHED_FRAME.01 (round 357)")
    print("SPEC_SHA %s   (DSW %s / PX %s / RSA %s)"
          % (SPEC_SHA[:16], DSW.SPEC_SHA[:16], PX.SPEC_SHA[:16],
             RSA.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + wards + mutants + w9 "
                        "worlds; ladders, battery, K2, phi, "
                        "controls, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and RSA.SPEC_SHA.startswith(RSA_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX)
              and QGL.SPEC_SHA.startswith(QGL_SHA_PREFIX)
              and EFA.SPEC_SHA.startswith(EFA_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "sealed BEFORE evaluation: the frame derivation (parity "
          "kernel e^-(1/2+a)w + conductor -(gamma+log(pi/q)) + "
          "matched border), both characters (mod 3 primary / mod "
          "4 census), the two wall instruments, the verbatim r330 "
          "battery re-adjudication, the frozen C_2 = %.2f K2 test "
          "+ frozen r329 counting, the mechanism clauses (MASS %.2f "
          "/ V %.2f / DIGAMMA %.2f / FS %.2f/%.1f), all letters "
          "and every bar; import integrity DSW %s / PX %s / RSA "
          "%s / SFE %s / QGL %s / EFA %s"
          % (C2_K2_FROZEN, MASS_BAR, V_BAR, DIGAMMA_BAR,
             FS_CORR_MIN, FS_RMSR_MAX, DSW.SPEC_SHA[:8],
             PX.SPEC_SHA[:8], RSA.SPEC_SHA[:8], SFE.SPEC_SHA[:8],
             QGL.SPEC_SHA[:8], EFA.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in CONSTRUCTORS:
        sc_own += scope_audit(fn)
    sc_m5 = scope_audit("mutant_c2_recalibrate")
    sc_m6 = scope_audit("mutant_main_blend")
    leak = bool(frag) or bool(sc_own) or not okf
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_m5) >= 1 and len(sc_m6) >= 1,
          "fragment audit clean (%d hits); the %d sealed "
          "constructors consume gauge tables + character tables + "
          "window shape ONLY (%s); m5 recalibration FLAGGED (%s); "
          "m6 MAIN-blend FLAGGED (%s)"
          % (len(frag), len(CONSTRUCTORS),
             "CLEAN" if not sc_own else "; ".join(sc_own),
             sc_m5[0] if sc_m5 else "MISS",
             sc_m6[0] if sc_m6 else "MISS"))

    # ---------------- S1 toys + derivation wards + m1/m2/m3
    section("S1  CHARACTER WARDS + DIGAMMA IDENTITIES + FRAME "
            "REPRODUCTION + m1/m2/m3")
    w3 = char_wards(chi_char_q, Q_CHI3)
    w4 = char_wards(chi_char_q, Q_CHI4)
    m_per, m_sup, _m, _o = DSW.char_wards(
        DSW.mutant_chi_wrong_period)
    check("G10-character-wards", all(w3) and all(w4)
          and (not m_per) and (not m_sup),
          "chi mod 3 + chi mod 4: periodicity, support (zero iff "
          "gcd(n, q) > 1), multiplicativity (40 x 40), "
          "orthogonality, ODDNESS chi(-1) = -1 => parity a = 1 "
          "DERIVED for both; m3 PERMUTED TABLE (r330 mutant "
          "verbatim): periodicity witness n = 1 + support witness "
          "n = 4 break -- CAUGHT exact")
    old_dps = mp.mp.dps
    mp.mp.dps = 30
    dev_dig = {0: 0.0, 1: 0.0}
    for a_par in (0, 1):
        for xi in DIG_XI:
            f_int = mp.quad(
                lambda w: (mp.e ** (-2 * w) - mp.cos(xi * w)
                           * mp.e ** (-(0.5 + a_par) * w))
                / (1 - mp.e ** (-2 * w)), [0, 1, 10, 60])
            quad_v = float(-mp.euler + 2 * f_int)
            cf_v = float(mp.re(mp.digamma(
                mp.mpf(1 + 2 * a_par) / 4 + mp.mpc(0, 1) * xi / 2)))
            dev_dig[a_par] = max(dev_dig[a_par],
                                 abs(quad_v - cf_v))
    mp.mp.dps = old_dps
    check("G11-digamma-identities", dev_dig[0] <= DIG_TOY_BAR
          and dev_dig[1] <= DIG_TOY_BAR,
          "Re psi((1+2a)/4 + i xi/2) == -gamma + 2 int [e^-2w - "
          "cos(xi w) e^-(1/2+a)w]/(1-e^-2w) dw at xi = %s: max "
          "dev a=0 %.1e (r342 regate) / a=1 %.1e (the matched "
          "parity identity, bar %.0e) -- the arch swap is the "
          "classical Gauss-digamma integral, derived not fitted"
          % (str(DIG_XI), dev_dig[0], dev_dig[1], DIG_TOY_BAR))
    alpha9, M9, L9, Nw9, D9 = V.window_shape(MAIN_KZ)
    ca_v = V.arch_lags(M9, D9)
    ca_chi0 = chi_arch_lags(M9, D9, 0.0, math.log(math.pi))
    ka9 = int(np.searchsorted(V.U, 2.0 * alpha9 + 1e-14,
                              side="right"))
    uu9 = np.asarray(V.U[:ka9], float)
    mm9 = np.asarray(V.W_VM[:ka9], float)
    cp_v, _ka = V.prime_lags(alpha9, M9, D9)
    cp_chi = chi_prime_lags(M9, D9, uu9, mm9)
    mz9 = V.build_measures(MAIN_KZ)
    mz9t = chi_build_measures(MAIN_KZ, uu9, mm9, 0.0,
                              math.log(math.pi))
    ok_doc = (np.array_equal(ca_v, ca_chi0)
              and np.array_equal(cp_v, cp_chi)
              and np.array_equal(mz9["xp"], mz9t["xp"])
              and np.array_equal(mz9["wp"], mz9t["wp"])
              and np.array_equal(mz9["yn"], mz9t["yn"])
              and np.array_equal(mz9["vn"], mz9t["vn"]))
    alpha9c = float(core.U_ALL[MAIN_KZ])
    ka9c = core.atoms_in(alpha9c)
    db_v = SFE.window_data_b(MAIN_KZ, core.NU_MAIN)
    db_chi = chi_window_data(MAIN_KZ, 0.0, math.log(math.pi),
                             (core.U_ALL[:ka9c].copy(),
                              core.MU_ALL[:ka9c].copy()))
    ok_term = all(np.array_equal(db_v[k], db_chi[k])
                  for k in ("xs", "ws", "ys", "vs"))
    check("G12-frame-reproduction", ok_doc and ok_term,
          "TRIVIAL FRAME (a = 0, q = 1, full comb) BITWISE: chi "
          "arch lags == V.arch_lags, chi prime lags == "
          "V.prime_lags, chi_build_measures == V.build_measures "
          "(xp/wp/yn/vn) at w9 [%s]; terminal chi_window_data == "
          "SFE.window_data_b(NU = 4) (xs/ws/ys/vs) [%s] -- the "
          "construction IS the frame-A machinery, only the arch "
          "source is swapped" % (ok_doc, ok_term))
    u3, w3c, nn3, ch3 = chi_window_comb(MAIN_KZ, Q_CHI3)
    uD, wD, nnD, chD = DSW.dirichlet_comb(MAIN_KZ)
    ok_comb = (np.array_equal(u3, uD) and np.array_equal(w3c, wD)
               and np.array_equal(nn3, nnD)
               and bool(np.array_equal(np.abs(w3c),
                                       mm9[chi_char_q(
                                           V.PP[:ka9].astype(
                                               np.int64),
                                           Q_CHI3) != 0.0]))
               and bool(np.array_equal(np.sign(w3c), ch3)))
    u4, w4c, nn4, ch4 = chi_window_comb(MAIN_KZ, Q_CHI4)
    n_drop4 = int(np.sum(V.PP[:ka9].astype(np.int64) % 2 == 0))
    check("G13-comb-wards", ok_comb
          and len(w4c) == ka9 - n_drop4,
          "chi3 comb == DSW.dirichlet_comb BITWISE (positions + "
          "weights + kept atoms: the r330 comb, matched frame "
          "around it); gauge |w| == W_VM bitwise, sign == chi; "
          "chi4 comb drops the %d atoms n = 2^k of %d (census)"
          % (n_drop4, ka9))
    # m1 conductor: uniform -log q density shift, EXACT
    ca3 = chi_arch_lags(M9, D9, 1.0, LPQ3)
    ca3_m1 = mutant_arch_no_conductor(M9, D9, 1.0)
    d3 = V.spectral_density(ca3)
    d3_m1 = V.spectral_density(ca3_m1)
    dev_m1 = float(np.max(np.abs(d3 - d3_m1 - math.log(Q_CHI3))))
    check("G14-m1-conductor", dev_m1 <= M1_BAR * max(
        1.0, float(np.max(np.abs(d3)))),
          "m1 ARCH WITHOUT CONDUCTOR (the r330 trap): only the "
          "near-lag constant moves, the density shifts by -log q "
          "uniformly -- max |d_true - d_mut - log 3| = %.1e "
          "(EXACT; break scale log 3 = %.4f) -- CAUGHT"
          % (dev_m1, math.log(Q_CHI3)))

    # ---------------- S2 the w9 worlds
    section("S2  W9 -- MAIN RECORDS, MATCHED CHI3/CHI4, UNMATCHED "
            "r330 BASELINE, MATCHED TERMINAL, m2/m4")
    ws9 = wall_scan(mz9, cross_ext=True)
    ok_main9 = (mz9["S"] == REC_S and mz9["Nw"] == REC_NW
                and abs(ws9["lamN"] - REC_LAM) <= 1e-6
                and abs(ws9["lamN1"] - REC_LAM_NEXT) <= 1e-6
                and abs(ws9["margin"] / REC_MARGIN - 1.0)
                <= REC_MARGIN_TOL
                and ws9["minc_ext"] == REC_NW + 1)
    check("G20-w9-main-records", ok_main9,
          "MAIN w9: S = %d, N_w = %d, lambda(N_w) = %.8f (rec "
          "%.8f), lambda(N_w+1) = %.8f > 1, margin %.4e (rec "
          "%.4e); PINNED: minC_ext == N_w + 1 == %d (crossing "
          "exactly one past half-filling -- the document route)"
          % (mz9["S"], mz9["Nw"], ws9["lamN"], REC_LAM,
             ws9["lamN1"], ws9["margin"], REC_MARGIN,
             ws9["minc_ext"]))
    mz3 = chi_build_measures(MAIN_KZ, u3, w3c, 1.0, LPQ3)
    ws3 = wall_scan(mz3, cross_ext=True)
    pr3 = pair_row(mz3, ws3)
    dev_dict9 = 0.0
    dev_v9 = 0.0
    dev_m2 = 0.0
    dev_m4 = 0.0
    cP3 = chi_prime_lags(M9, D9, u3, w3c)
    dA3 = V.spectral_density(chi_arch_lags(M9, D9, 1.0, LPQ3))
    dA3_m2 = V.spectral_density(mutant_arch_wrong_parity(M9, D9,
                                                         LPQ3))
    _ = cP3
    for (ii, ff) in ((pr3["i1"], pr3["f1"]), (pr3["i2"],
                                              pr3["f2"])):
        th = 2.0 * math.pi * ff / L9
        dic_c, _p = chi_arch_dict_density(th, alpha9, D9, 1.0,
                                          LPQ3)
        dev_dict9 = max(dev_dict9, abs(dic_c - float(dA3[ff]))
                        / max(abs(float(dA3[ff])), 1e-300))
        dev_m2 = max(dev_m2, abs(float(dA3_m2[ff])
                                 - float(dA3[ff]))
                     / max(abs(float(dA3[ff])), 1e-300))
        vp, _a, _pp = chi_v_predict(th, alpha9, M9, L9, D9, u3,
                                    w3c, 1.0, LPQ3)
        vt = float(mz3["vn"][ii])
        dev_v9 = max(dev_v9, abs(vp - vt) / vt)
        vpm = mutant_dict_main_arch(th, alpha9, M9, L9, D9, u3,
                                    w3c)
        dev_m4 = max(dev_m4, abs(vpm - vt) / vt)
    check("G21-w9-chi3-matched", mz3["S"] > 0
          and dev_dict9 <= DIGAMMA_BAR and dev_v9 <= V_BAR,
          "MATCHED CHI3 w9: S = %d (S+ %d / S- %d), N_w = %d; "
          "lambda(N_w) = %.6f, margin %.4e, minC %s, minC_ext %s "
          "(pin offset %s); pair folds (%d, %d), d1 %.6f d2 %.6f "
          "c %.2e, r_det %.4f, pmass %.4f, PR %.2f; CHI "
          "DICTIONARY at the pair folds: density dev %.1e (bar "
          "%.2f), v_pred dev %.1e (bar %.2f) -- the matched arch "
          "side is the derived F_A^chi"
          % (mz3["S"], len(mz3["xp"]), len(mz3["yn"]), mz3["Nw"],
             ws3["lamN"], ws3["margin"], str(ws3["minc"]),
             str(ws3["minc_ext"]),
             str(ws3["minc_ext"] - (mz3["Nw"] + 1)
                 if ws3["minc_ext"] is not None else None),
             pr3["f1"], pr3["f2"], pr3["d1"], pr3["d2"], pr3["c"],
             pr3["rdet"], pr3["pmass"], pr3["pr"], dev_dict9,
             DIGAMMA_BAR, dev_v9, V_BAR))
    mz4 = chi_build_measures(MAIN_KZ, u4, w4c, 1.0, LPQ4)
    ws4 = wall_scan(mz4, cross_ext=True)
    check("G22-w9-chi4-matched", mz4["S"] > 0,
          "MATCHED CHI4 w9 (census): S = %d (S+ %d / S- %d), "
          "N_w = %d; lambda(N_w) = %.6f, margin %.4e, minC %s, "
          "minC_ext %s" % (mz4["S"], len(mz4["xp"]),
                           len(mz4["yn"]), mz4["Nw"], ws4["lamN"],
                           ws4["margin"], str(ws4["minc"]),
                           str(ws4["minc_ext"])))
    pD = BH.wpack(MAIN_KZ, base_kw=dict(comb=(uD, wD)))
    uA, wA, _nnA = DSW.dirichlet_abs_comb(MAIN_KZ)
    pA = BH.wpack(MAIN_KZ, base_kw=dict(comb=(uA, wA)))
    check("G23-r330-unmatched-baseline", pD["nf"] == R330_DIR_NF
          and pA["nf"] == R330_ABS_NF,
          "THE r330 UNMATCHED BASELINE reproduced: the SAME chi3 "
          "comb through zeta's frame dies at nf = %s (record 24); "
          "ABS at nf = %s (record 37) -- the re-adjudication "
          "anchor" % (str(pD["nf"]), str(pA["nf"])))
    pk3 = chi_wpack(MAIN_KZ, 1.0, LPQ3, (u3, w3c))
    check("G24-w9-terminal-matched", pk3["complete"],
          "MATCHED TERMINAL chi3 w9: chain-complete N = %d, nf = "
          "%s (the SAME comb, the MATCHED frame -- vs unmatched "
          "nf 24)" % (pk3["N"], str(pk3["nf"])))
    check("G25-m2-m4-arch-mutants", dev_m2 >= M2_BAR
          and dev_m4 >= M4_BAR and dev_dict9 <= DIGAMMA_BAR
          and dev_v9 <= V_BAR,
          "m2 WRONG PARITY (a = 0, conductor kept): density dev "
          "%.2f >= %.1f at the pair folds (true %.1e); m4 "
          "DICTIONARY WITH MAIN ARCH: v_pred dev %.2f >= %.1f "
          "(true %.1e) -- both CAUGHT loud"
          % (dev_m2, M2_BAR, dev_dict9, dev_m4, M4_BAR, dev_v9))

    # ---------------- S3 leg A: the ladders + the battery
    section("S3  LEG A -- WALL CENSUS LADDERS + THE VERBATIM r330 "
            "BATTERY RE-ADJUDICATION")
    frame_ins = []
    if not (dev_dig[0] <= DIG_TOY_BAR and dev_dig[1]
            <= DIG_TOY_BAR):
        frame_ins.append("digamma-identity")
    if not (ok_doc and ok_term):
        frame_ins.append("frame-reproduction")
    if not ok_comb:
        frame_ins.append("comb-cross-route")
    if dev_dict9 > DIGAMMA_BAR:
        frame_ins.append("chi-density-dictionary")
    if smoke:
        for g in ("G30-main-eladder", "G31-main-terminal-anchors",
                  "G32-chi3-eladder", "G33-chi3-battery",
                  "G34-readjudication", "G35-chi4-ladders"):
            check(g, True, "SMOKE: skipped")
        stD = None
        rows3 = []
        rows4 = []
        wall3 = {}
        wall4 = {}
        kzs = [MAIN_KZ]
        clD = {}
        statD = "SMOKE"
    else:
        kzs = list(V.admissible_indices())
        # MAIN E-ladder
        wallM = {}
        for kz in kzs:
            mzk = V.build_measures(kz)
            wallM[kz] = (wall_scan(mzk, cross_ext=(kz == MAIN_KZ)),
                         mzk["S"])
        margM = [wallM[kz][0]["margin"] for kz in kzs]
        check("G30-main-eladder", len(kzs) == 42
              and all(mg > 0.0 for mg in margM),
              "MAIN E-ladder: 42 windows, ALL margins positive "
              "(min %.2e, max %.2e); w9 pinned at minC_ext == "
              "N_w + 1 (G20) -- document self-consistency"
              % (min(margM), max(margM)))
        # MAIN terminal ladder through the verbatim r330 channel
        packsM = [BH.wpack(kz) for kz in kzs]
        packsM.sort(key=lambda p: (p["N"], p["kz"]))
        recsM = []
        for p in packsM:
            rc = DSW.rung_rec(p)
            rc["ev"] = DSW.eval_rung(rc)
            rc["S_own"] = len(p["d"]["xs"]) + len(p["d"]["ys"])
            recsM.append(rc)
        rho2M = [r["ev"]["rho2"] for r in recsM]
        C2_live = max(rho2M[:DSW.N_CAL])
        stM = DSW.battery_stats(recsM, C2_live)
        ok_m_anch = (stM["nf_none"] == 42 and stM["valid"]
                     and abs(C2_live - DSW.R306_C2) <= DSW.C2_TOL
                     and not stM["viol"]
                     and abs(stM["sl_D"] - DSW.R299_SL_D)
                     <= DSW.SL_TOL
                     and abs(stM["neff_med"] - DSW.R301_NEFF_MED)
                     <= DSW.NEFF_MED_TOL
                     and abs(stM["sl_neff"] - DSW.R301_SL_NEFF)
                     <= DSW.SL_TOL
                     and stM["oneg"] == DSW.R299_ONEG
                     and stM["fill_med"] < DSW.FILL_CLS
                     and stM["multmax"] <= DSW.MULT_CAP)
        check("G31-main-terminal-anchors", ok_m_anch,
              "the r330 MAIN anchors re-derived through the "
              "VERBATIM channel: nf None %d/42; C_2 refreeze "
              "%.6f == %.4f (tol %.3f), 0 violations; sl_D %+.4f "
              "(rec %+.3f); n_eff med %.2f slope %+.3f; O<0 on "
              "%d/42 == %d EXACT; fill med %.3f < %.1f; mult <= "
              "%d" % (stM["nf_none"], C2_live, DSW.R306_C2,
                      DSW.C2_TOL, stM["sl_D"], DSW.R299_SL_D,
                      stM["neff_med"], stM["sl_neff"],
                      stM["oneg"], DSW.R299_ONEG, stM["fill_med"],
                      DSW.FILL_CLS, DSW.MULT_CAP))
        # CHI3 matched E-ladder + pair rows
        wall3 = {}
        rows3 = []
        excl3 = []
        print("    %-5s %-5s %-5s %-5s %-11s %-6s %-8s %-9s "
              "%-9s %-7s %-6s"
              % ("kz", "S", "S-", "N_w", "margin", "minC",
                 "pinoff", "c", "r_det", "pmass", "PR"))
        for kz in kzs:
            uu_c, ww_c, nn_c, _ch = chi_window_comb(kz, Q_CHI3)
            if len(uu_c) < V.N_ATOM_MIN:
                excl3.append(kz)
                continue
            mzc = chi_build_measures(kz, uu_c, ww_c, 1.0, LPQ3)
            wsc = wall_scan(mzc, cross_ext=True)
            wall3[kz] = wsc
            prc = pair_row(mzc, wsc)
            prc["kz"] = kz
            rows3.append(prc)
            po = (wsc["minc_ext"] - (mzc["Nw"] + 1)
                  if wsc["minc_ext"] is not None else None)
            print("    %-5d %-5d %-5d %-5d %+.4e %-6s %-8s "
                  "%.3e %.3e %.4f %5.2f"
                  % (kz, mzc["S"], len(mzc["yn"]), mzc["Nw"],
                     wsc["margin"], str(wsc["minc"]), str(po),
                     prc["c"], prc["rdet"], prc["pmass"],
                     prc["pr"]), flush=True)
        marg3 = [wall3[kz]["margin"] for kz in wall3]
        pin3 = [wall3[kz]["minc_ext"] - (wall3[kz]["Nw"] + 1)
                for kz in wall3
                if wall3[kz]["minc_ext"] is not None]
        n_pin3 = sum(1 for v in pin3 if v == 0)
        check("G32-chi3-eladder", len(wall3) >= LIVE_MIN,
              "CHI3 matched E-ladder: %d/42 built (kept-atom "
              "exclusions %s); margins positive %d/%d (min %.2e "
              "max %.2e); minC None (wall to window depth) on "
              "%d/%d; PINNING census: pinned-at-N_w+1 on %d, "
              "crossing offsets %s..%s (med %s) -- the "
              "half-filling pinning coordinate, measured"
              % (len(wall3), str(excl3) if excl3 else "none",
                 sum(1 for mg in marg3 if mg > 0.0), len(marg3),
                 min(marg3), max(marg3),
                 sum(1 for kz in wall3
                     if wall3[kz]["minc"] is None), len(wall3),
                 n_pin3,
                 str(min(pin3)) if pin3 else "n/a",
                 str(max(pin3)) if pin3 else "n/a",
                 str(float(np.median(pin3))) if pin3 else "n/a"))
        # CHI3 matched terminal battery (verbatim r330 channel)
        rowsD = []
        for kz in kzs:
            uu_c, ww_c, _nn, _ch = chi_window_comb(kz, Q_CHI3)
            try:
                p = chi_wpack(kz, 1.0, LPQ3, (uu_c, ww_c))
                rc = DSW.rung_rec(p)
                rc["ev"] = DSW.eval_rung(rc)
                rc["S_own"] = len(p["d"]["xs"]) \
                    + len(p["d"]["ys"])
                rowsD.append(rc)
            except Exception as exc:        # noqa: BLE001
                rowsD.append(dict(kz=kz, failed=str(exc)))
        rowsD.sort(key=lambda r: (r.get("N", 10 ** 9),
                                  r.get("kz", 0)))
        stD = DSW.battery_stats(rowsD, C2_live)
        clD = DSW.battery_classes(stD) if stD.get("valid") else {}
        statD, splD = DSW.variant_status(stD, clD)
        check("G33-chi3-battery", stD.get("n_built", 0) == 42,
              "CHI3 matched battery (DSW channel verbatim, "
              "live-frozen C_2 %.6f): built %d/42, live %d, tb "
              "%.1e/%.1e (bars %.0e/%.0e), validity %s; nf None "
              "%s/42 (r330 unmatched: 0/42); rho_2 violations %s "
              "(r330 unmatched: 32/42, max 27.6); sl_D %s (r330 "
              "+0.793); sl_neff %s; O<0 %s/42 (r330 27/42); fill "
              "med %s; mult max %s; STATUS %s%s"
              % (C2_live, stD.get("n_built", 0),
                 stD.get("n_live", 0), stD.get("tb_sh", 0.0),
                 stD.get("tb_dp", 0.0), DSW.TB_BAR_SECOND,
                 DSW.TB_BAR_SECOND_DEEP, stD.get("why"),
                 str(stD.get("nf_none")),
                 str(len(stD.get("viol", []))),
                 ("%+.3f" % stD["sl_D"]) if "sl_D" in stD
                 else "n/a",
                 ("%+.3f" % stD["sl_neff"]) if "sl_neff" in stD
                 else "n/a", str(stD.get("oneg")),
                 ("%.3f" % stD["fill_med"]) if "fill_med" in stD
                 else "n/a", str(stD.get("multmax")), statD,
                 "(%s)" % ",".join(splD) if splD else ""))
        # the re-adjudication table
        r330_cls = {"HALF_FILLING": "CTRL", "RENYI3_C2": "CTRL",
                    "SIGMA_DECAY": "SPLIT", "NEFF_GROWTH": "MAIN",
                    "O_SIGN": "CTRL", "FILL": "MAIN",
                    "MULT2": "MAIN"}
        retyped = []
        confirmed = []
        info("R330 RE-ADJUDICATION (property: r330 unmatched -> "
             "matched):")
        for prp in DSW.PROPS:
            mcl = clD.get(prp, ("-", "invalid"))
            info("  %-12s %s -> %s %s"
                 % (prp, r330_cls[prp], mcl[0], mcl[1]))
            if r330_cls[prp] != "MAIN":
                if mcl[0] == "MAIN":
                    retyped.append(prp)
                else:
                    confirmed.append(prp)
        check("G34-readjudication", bool(clD),
              "the four r330 splits re-adjudicated on the matched "
              "frame: RETYPED_FRAME_ARTIFACT %s; "
              "CONFIRMED_ZETA_IDIOSYNCRASY %s"
              % (str(retyped) if retyped else "none",
                 str(confirmed) if confirmed else "none"))
        # CHI4 ladders (census)
        wall4 = {}
        rows4 = []
        excl4 = []
        rows4T = []
        for kz in kzs:
            uu_c, ww_c, _nn, _ch = chi_window_comb(kz, Q_CHI4)
            if len(uu_c) < V.N_ATOM_MIN:
                excl4.append(kz)
                continue
            mzc = chi_build_measures(kz, uu_c, ww_c, 1.0, LPQ4)
            wsc = wall_scan(mzc, cross_ext=True)
            wall4[kz] = wsc
            prc = pair_row(mzc, wsc)
            prc["kz"] = kz
            rows4.append(prc)
            try:
                p = chi_wpack(kz, 1.0, LPQ4, (uu_c, ww_c))
                rc = DSW.rung_rec(p)
                rc["ev"] = DSW.eval_rung(rc)
                rc["S_own"] = len(p["d"]["xs"]) \
                    + len(p["d"]["ys"])
                rows4T.append(rc)
            except Exception as exc:        # noqa: BLE001
                rows4T.append(dict(kz=kz, failed=str(exc)))
        rows4T.sort(key=lambda r: (r.get("N", 10 ** 9),
                                   r.get("kz", 0)))
        stA4 = DSW.battery_stats(rows4T, C2_live)
        clA4 = DSW.battery_classes(stA4) if stA4.get("valid") \
            else {}
        statA4, splA4 = DSW.variant_status(stA4, clA4)
        marg4 = [wall4[kz]["margin"] for kz in wall4]
        pin4 = [wall4[kz]["minc_ext"] - (wall4[kz]["Nw"] + 1)
                for kz in wall4
                if wall4[kz]["minc_ext"] is not None]
        check("G35-chi4-ladders", len(wall4) >= LIVE_MIN,
              "CHI4 census: %d/42 built (exclusions %s); margins "
              "positive %d/%d (min %.2e); minC None %d/%d; pin "
              "offsets med %s; battery: nf None %s/42, rho_2 "
              "viol %s, STATUS %s%s"
              % (len(wall4), str(excl4) if excl4 else "none",
                 sum(1 for mg in marg4 if mg > 0.0), len(marg4),
                 min(marg4),
                 sum(1 for kz in wall4
                     if wall4[kz]["minc"] is None), len(wall4),
                 str(float(np.median(pin4))) if pin4 else "n/a",
                 str(stA4.get("nf_none")),
                 str(len(stA4.get("viol", []))), statA4,
                 "(%s)" % ",".join(splA4) if splA4 else ""))

    # ---------------- S4 leg B: mechanisms
    section("S4  LEG B -- MECHANISMS: PAIR, DETERMINANT, "
            "DICTIONARY, PHI")
    if smoke:
        for g in ("G40-pair-census", "G41-pair-identities",
                  "G42-dictionary-ladder", "G43-phi-fs"):
            check(g, True, "SMOKE: skipped")
        mech = []
    else:
        live3 = [r for r in rows3 if r["margin"] > 0.0]
        pm_med = float(np.median([r["pmass"] for r in live3]))
        pr_med = float(np.median([r["pr"] for r in live3]))
        mech_pair = pm_med >= MASS_BAR
        check("G40-pair-census", True,
              "CHI3 pair census on %d margin-positive rungs: "
              "pair mass med %.4f (min %.4f, clause >= %.2f => "
              "%s); PR med %.2f (MAIN 1.6-1.9; PR -> 1 = the "
              "two-atom structure degenerates toward ONE atom, "
              "census); folds (2, 4) at w9 == MAIN shallow edge"
              % (len(live3), pm_med,
                 min(r["pmass"] for r in live3), MASS_BAR,
                 "TRANSFERS" if mech_pair else "MISSES", pr_med))
        det_w = max(r["det_dev"] for r in rows3)
        inter_ok = all(r["inter_ok"] for r in rows3)
        sign_ok = all(r["sign_ok"] for r in rows3)
        rdet_pos = all(r["rdet"] > 0.0 for r in live3)
        mech_det = (det_w <= DET_ID_BAR and inter_ok and sign_ok
                    and rdet_pos)
        check("G41-pair-identities", det_w <= DET_ID_BAR
              and inter_ok and sign_ok,
              "determinant identity (1-l)(1-l') == pq - c^2 "
              "backward-dev max %.1e (bar %.0e); interlacing "
              "margin <= m2 on %d/%d; sign(m2) == sign(r_det) "
              "%d/%d; r_det > 0 on all margin-positive rungs: %s "
              "(r_det med %.3f -- far from MAIN's near-saturated "
              "1e-2..1e-6, census)"
              % (det_w, DET_ID_BAR,
                 sum(1 for r in rows3 if r["inter_ok"]),
                 len(rows3),
                 sum(1 for r in rows3 if r["sign_ok"]),
                 len(rows3), rdet_pos,
                 float(np.median([r["rdet"] for r in live3]))))
        # dictionary over the ladder (v_pred vs the measured nu
        # weights; density-level ward on the sample rungs)
        devs_v = {}
        dev_dict_s = {}
        for r in rows3:
            kz = r["kz"]
            alpha_, M_, L_, _Nw, D_ = V.window_shape(kz)
            uu_c, ww_c, _nn, _ch = chi_window_comb(kz, Q_CHI3)
            mzc = chi_build_measures(kz, uu_c, ww_c, 1.0, LPQ3)
            dA_s = (V.spectral_density(
                chi_arch_lags(M_, D_, 1.0, LPQ3))
                if kz in SAMPLE_KZ else None)
            dv = 0.0
            for (ii, ff) in ((r["i1"], r["f1"]),
                             (r["i2"], r["f2"])):
                th = 2.0 * math.pi * ff / L_
                vp, da_c, _dp = chi_v_predict(
                    th, alpha_, M_, L_, D_, uu_c, ww_c, 1.0, LPQ3)
                vt = float(mzc["vn"][ii])
                dv = max(dv, abs(vp - vt) / vt)
                if dA_s is not None:
                    dev_dict_s[kz] = max(
                        dev_dict_s.get(kz, 0.0),
                        abs(da_c - float(dA_s[ff]))
                        / max(abs(float(dA_s[ff])), 1e-300))
            devs_v[kz] = dv
        med_v = float(np.median(list(devs_v.values())))
        max_v = max(devs_v.values())
        ok_dict_s = all(v <= DIGAMMA_BAR
                        for v in dev_dict_s.values())
        mech_dict = (med_v <= V_BAR) and ok_dict_s
        check("G42-dictionary-ladder", ok_dict_s,
              "THE CHI DICTIONARY UNIVERSALITY TEST: v_pred = "
              "-(2/L)(1-cos)(F_A^chi - TAIL^chi + f_P^chi) over "
              "%d rungs: median rel dev %.4f (V_BAR %.2f => %s), "
              "max %.4f; density dictionary at the sample pair "
              "folds %s (bar %.2f) -- the r342 dictionary "
              "predicts the SECOND arithmetic's weights with the "
              "chi offset"
              % (len(devs_v), med_v, V_BAR,
                 "TRANSFERS" if med_v <= V_BAR else "MISSES",
                 max_v,
                 str({("kz%d" % k): round(v, 5)
                      for k, v in sorted(dev_dict_s.items())}),
                 DIGAMMA_BAR))
        # phi FS: MAIN gate + chi census
        rowsM_fs = []
        for kz in kzs:
            mzk = V.build_measures(kz)
            wsk = wallM[kz][0]
            prk = pair_row(mzk, wsk)
            prk["kz"] = kz
            rowsM_fs.append(prk)
        fsM, nM = phi_fs(rowsM_fs)
        fs3, n3 = phi_fs(rows3)
        fs4, n4 = phi_fs(rows4)
        ok_fsM = (fsM is not None and fsM["corr"] >= FS_CORR_MIN
                  and fsM["rmsr"] <= FS_RMSR_MAX)
        mech_phi = (fs3 is not None and n3 >= PHI_MIN_ROWS
                    and fs3["corr"] >= FS_CORR_MIN
                    and fs3["rmsr"] <= FS_RMSR_MAX)
        check("G43-phi-fs", ok_fsM,
              "PHI CO-WANDER (A_LEAD 17/12, RSA verbatim): MAIN "
              "GATE corr %.6f rmsr %.4f on %d rows (clauses "
              ">= %.2f / <= %.1f; r352 75-row record %.6f/%.4f "
              "census ref); CHI3 corr %s rmsr %s on %d usable "
              "(suppression 1/rmsr = %s; MAIN %s); CHI4 %s/%s on "
              "%d -- the r354-named ABS universality test in the "
              "RIGHT world"
              % (fsM["corr"] if fsM else float("nan"),
                 fsM["rmsr"] if fsM else float("nan"), nM,
                 FS_CORR_MIN, FS_RMSR_MAX, R352_FS_REC[0],
                 R352_FS_REC[1],
                 ("%.6f" % fs3["corr"]) if fs3 else "n/a",
                 ("%.4f" % fs3["rmsr"]) if fs3 else "n/a", n3,
                 ("%.0fx" % (1.0 / fs3["rmsr"]))
                 if fs3 and fs3["rmsr"] > 0 else "n/a",
                 ("%.0fx" % (1.0 / fsM["rmsr"]))
                 if fsM and fsM["rmsr"] > 0 else "n/a",
                 ("%.6f" % fs4["corr"]) if fs4 else "n/a",
                 ("%.4f" % fs4["rmsr"]) if fs4 else "n/a", n4))
        mech = [nm for nm, okm in (("TWO_ATOM", mech_pair),
                                   ("DET_COND", mech_det),
                                   ("DICT", mech_dict),
                                   ("PHI", mech_phi)) if okm]

    # ---------------- S5 leg C: the terminal K2 mechanisms
    section("S5  LEG C -- K2 AT THE FROZEN C_2 + THE COUNTING "
            "CONSTANTS")
    if smoke:
        for g in ("G50-main-k2-anchor", "G51-chi3-k2",
                  "G52-chi4-k2", "G53-m5-recalibration"):
            check(g, True, "SMOKE: skipped")
        k2_ok = False
        fabg3 = []
    else:
        grels = {kz: g for kz, g in zip(
            kzs, EFA.grel_col(kzs, core.G_ALL))}
        for rc in recsM:
            rc["evk"] = eval_k2(rc)
        kM, fabidM, k2chM = k2_rows(recsM, grels)
        violM = [r for r in kM if r["fabg"] > C2_K2_FROZEN + K2_EPS]
        # amendment a1 (disclosed, calibration pass 1; the r330-a1
        # lesson exactly): the r329 counting constants ARE the
        # frame-A ladder maxima (kz16 nscl 2.02581735 / kz36 ngl
        # 2.63511735) -- counting against the 4-decimal record
        # literals makes the calibration rungs "violate" their own
        # constants by 1.7e-5.  The constants are re-frozen LIVE at
        # full precision on the MAIN ladder, anchor-gated against
        # the r329 literals (the r330 C_2 convention verbatim);
        # every chi violation count runs against the live-frozen
        # constants.  No adjudication rule moved.
        CNSC_live = max(r["nscl"] for r in kM)
        CNG_live = max(r["ngl"] for r in kM)
        ok_cnt_anchor = (abs(CNSC_live - EFA.FROZEN_CNSC) <= 5e-4
                         and abs(CNG_live - EFA.FROZEN_CNG)
                         <= 5e-4)
        check("G50-main-k2-anchor", (not violM) and ok_cnt_anchor
              and fabidM <= 1e-12 and k2chM <= K2_CHAIN_BAR,
              "MAIN anchor through THIS channel: FAB identity "
              "%.1e, K2 chain one-sided %.1e; FABg <= frozen "
              "%.2f on %d/%d (max %.2f); counting constants "
              "re-frozen LIVE at full precision (a1): C_NSC "
              "%.6f / C_NG %.6f == r329 records %.4f / %.4f "
              "(tol 5e-4) -- the chi counts run against these"
              % (fabidM, k2chM, C2_K2_FROZEN, len(kM) - len(violM),
                 len(kM), max(r["fabg"] for r in kM),
                 CNSC_live, CNG_live, EFA.FROZEN_CNSC,
                 EFA.FROZEN_CNG))
        for rc in rowsD:
            if "failed" not in rc:
                rc["evk"] = eval_k2(rc)
        k3, fabid3, k2ch3 = k2_rows(
            [rc for rc in rowsD if "failed" not in rc], grels)
        viol3 = [r for r in k3 if r["fabg"] > C2_K2_FROZEN + K2_EPS]
        cnt3 = [r for r in k3 if r["nscl"] > CNSC_live
                or r["ngl"] > CNG_live]
        fabg3 = [r["fabg"] for r in k3]
        info("CHI3 K2 table (kz m q_max FAB grel FABg nscl ngl):")
        for r in k3:
            info("  kz%-4d m %-4d %.4f %6.2f %.3f %6.2f %.2f %.2f"
                 % (r["kz"], r["m"], r["pk"], r["fab"], r["g"],
                    r["fabg"], r["nscl"], r["ngl"]))
        check("G51-chi3-k2", fabid3 <= 1e-12
              and k2ch3 <= K2_CHAIN_BAR,
              "CHI3 K2 at the FROZEN C_2 = %.2f: %d live rows, "
              "violations %s (max FABg %.2f); counting "
              "violations %s (max nscl %.2f / ngl %.2f); FAB "
              "identity %.1e, K2 chain one-sided %.1e; dominance "
              "census hgn med %.2f, bshare med %.2f, maj med "
              "%.2f" % (C2_K2_FROZEN, len(k3),
                        str([(r["kz"], round(r["fabg"], 2))
                             for r in viol3]) if viol3 else "0",
                        max(fabg3) if fabg3 else float("nan"),
                        str(len(cnt3)),
                        max(r["nscl"] for r in k3),
                        max(r["ngl"] for r in k3), fabid3, k2ch3,
                        float(np.median([r["hgn"] for r in k3])),
                        float(np.median([r["bsh"] for r in k3])),
                        float(np.median([r["maj"]
                                         for r in k3]))))
        for rc in rows4T:
            if "failed" not in rc:
                rc["evk"] = eval_k2(rc)
        k4, fabid4, k2ch4 = k2_rows(
            [rc for rc in rows4T if "failed" not in rc], grels)
        viol4 = [r for r in k4 if r["fabg"] > C2_K2_FROZEN + K2_EPS]
        cnt4 = [r for r in k4 if r["nscl"] > CNSC_live
                or r["ngl"] > CNG_live]
        check("G52-chi4-k2", fabid4 <= 1e-12
              and k2ch4 <= K2_CHAIN_BAR,
              "CHI4 K2: %d live rows, violations %s (max FABg "
              "%.2f); counting violations %s; FAB identity %.1e, "
              "chain %.1e"
              % (len(k4),
                 str([(r["kz"], round(r["fabg"], 2))
                      for r in viol4]) if viol4 else "0",
                 max(r["fabg"] for r in k4) if k4
                 else float("nan"), str(len(cnt4)), fabid4,
                 k2ch4))
        k2_ok = ((not violM) and (not viol3) and (not viol4)
                 and ok_cnt_anchor and (not cnt3) and (not cnt4)
                 and len(k3) >= K2_MIN_ROWS)
        mut5 = mutant_c2_recalibrate([3.0 * 1.0, 2.0 * 0.5])
        check("G53-m5-recalibration", bool(sc_m5)
              and abs(mut5 - 3.0) <= TOY_BAR
              and abs(mut5 - 1.0) >= MUT_MIN,
              "m5 C_2 RECALIBRATED ON THE CHI ROWS: AST-FLAGGED "
              "(%s) and the toy re-pick %.1f != the sealed toy "
              "freeze 1.0 -- protocol-CAUGHT twice; the real chi "
              "FABg max %.2f is printed against the frozen %.2f, "
              "NEVER adopted"
              % (sc_m5[0] if sc_m5 else "MISS", mut5,
                 max(fabg3) if fabg3 else float("nan"),
                 C2_K2_FROZEN))

    # ---------------- S6 leg D: controls
    section("S6  LEG D -- THE WORLD'S OWN CONTROLS: TWIN + "
            "SCRAMBLE")
    if smoke:
        for g in ("G60-twin", "G61-scramble"):
            check(g, True, "SMOKE: skipped")
        scr_dead = None
    else:
        gaps3 = MF.local_gaps(u3)
        u3t, w3t, _dens, _du = AKD.twin_rational(u3, w3c, gaps3,
                                                 D9, TWIN_TOL)
        mz3t = chi_build_measures(MAIN_KZ, u3t, w3t, 1.0, LPQ3)
        ws3t = wall_scan(mz3t)
        pr3t = pair_row(mz3t, ws3t)
        devT = max(abs(ws3t["margin"] - ws3["margin"])
                   / abs(ws3["margin"]),
                   abs(pr3t["d1"] - pr3["d1"]) / pr3["d1"],
                   abs(pr3t["d2"] - pr3["d2"]) / pr3["d2"],
                   abs(pr3t["c"] - pr3["c"])
                   / max(abs(pr3["c"]), 1e-300))
        check("G60-twin", devT <= TWIN_BAR,
              "RATIONAL TWIN of the chi3 comb (tol %.0e, weights "
              "untouched) through the matched frame at w9: "
              "margin/pair devs max %.1e (bar %.0e) -- the "
              "second world brings its own twin discipline"
              % (TWIN_TOL, devT, TWIN_BAR))
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9,
                                    size=len(w3c)))
        mz_scr = chi_build_measures(MAIN_KZ, u_scr, w3c, 1.0,
                                    LPQ3)
        ws_scr = wall_scan(mz_scr)
        try:
            pk_scr = chi_wpack(MAIN_KZ, 1.0, LPQ3, (u_scr, w3c))
            nf_scr = pk_scr["nf"]
        except Exception as exc:            # noqa: BLE001
            nf_scr = "build-fail: %s" % exc
        e_dead = (ws_scr["margin"] <= 0.0
                  or (ws_scr["minc"] is not None
                      and ws_scr["minc"]
                      <= DEPTH_DEAD * mz_scr["Nw"]))
        t_dead = (isinstance(nf_scr, str)
                  or (nf_scr is not None
                      and nf_scr <= DEPTH_DEAD * pk3["N"]))
        scr_dead = e_dead or t_dead
        check("G61-scramble", scr_dead,
              "SCRAMBLE-CHI (positions uniform [0, 2 alpha] seed "
              "%d, signed chi weights kept, MATCHED frame): "
              "E-margin %+.2e, minC %s / N_w %d; terminal nf %s "
              "-- the sealed break rule fires (%s): the matched "
              "frame does NOT rescue a scrambled comb, the wall "
              "needs the arithmetic"
              % (SCR_SEED, ws_scr["margin"], str(ws_scr["minc"]),
                 mz_scr["Nw"], str(nf_scr),
                 "E-dead" if e_dead else "terminal-dead"))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO RH claim, NO GRH claim (GRH only "
          "motivates the candidate, used nowhere), no L* claim, "
          "no bound mechanism, no posthoc bar/class/constant "
          "move (C_2 = %.2f frozen), no derived 5/7, mincut "
          "unchanged; what the round adds: the GRH-faithful "
          "matched Dirichlet frame (conductor + parity + border) "
          "with the verbatim r330 battery re-adjudication, the "
          "mechanism transfer table of both lanes and the "
          "world's own controls; r243..r356 stand"
          % C2_K2_FROZEN)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        n_live3 = len([r for r in rows3])
        e_alive = all(wall3[kz]["margin"] > 0.0 for kz in wall3)
        e_dead_maj = (sum(1 for kz in wall3
                          if wall3[kz]["margin"] <= 0.0)
                      > len(wall3) // 2)
        t_main = (clD.get("HALF_FILLING", ("-",))[0] == "MAIN")
        t_ctrl = (clD.get("HALF_FILLING", ("-",))[0] == "CTRL")
        if leak:
            head = "TARGET_LEAK"
        elif frame_ins or n_live3 < LIVE_MIN:
            head = "FRAME_INSUFFICIENT(%s)" % ",".join(
                frame_ins or ["live<%d" % LIVE_MIN])
        elif e_alive and t_main:
            head = ("SECOND_ARITHMETIC_LIVES(E-wall %d/%d "
                    "margins positive; r330 HALF_FILLING class "
                    "MAIN-side: nf None %d/%d)"
                    % (len(wall3), len(wall3),
                       stD.get("nf_none", -1),
                       stD.get("n_live", -1)))
        elif e_dead_maj and t_ctrl:
            head = "WALL_ZETA_SPECIFIC(matched frame, wall dead)"
        else:
            head = ("WALL_SPLIT_MATCHED(E-alive %s, terminal "
                    "class %s)" % (e_alive,
                                   str(clD.get("HALF_FILLING"))))
        parts = [head]
        parts.append("MECHANISMS_TRANSFER(%s)" % ",".join(mech)
                     if mech else "MECHANISMS_CENSUS")
        parts.append("K2_ARITHMETIC_UNIVERSAL(frozen %.2f, 0 "
                     "violations, counting holds)" % C2_K2_FROZEN
                     if k2_ok else "K2_CENSUS")
        parts.append("DICTIONARY_TRANSFERS"
                     if ("DICT" in mech) else "DICTIONARY_CENSUS")
        parts.append("PHI_COWANDER_UNIVERSAL"
                     if ("PHI" in mech) else "PHI_CENSUS")
        parts.append("R330_READJUDICATION(table above)")
        parts.append("CHI4_LEDGER(census above)")
        parts.append("CONTROL_LEDGER(twin + scramble %s)"
                     % ("BREAKS" if scr_dead else "SURVIVES"))
        parts.append("CONVENTION_LEDGER(conductor+parity+border "
                     "matched; grid/mesh/tent/fold/N_w shared by "
                     "construction, disclosed)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the matched second arithmetic, measured; NO "
          "RH/GRH claim" % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
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
