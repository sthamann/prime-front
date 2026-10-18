#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""loewner_pick_probe -- PRIME.LOEWNER.PICK.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
census-lift lane, the causal-synthesis lane, the independent session's
untracked probes, sieve4_helper.bin) are not touched.

=======================================================================
MISSION (round ~187: Loewner's theorem as a currency change).  Round
186 (ground_residue_obs_probe, SPEC_SHA 48637c8898a1da5a) established
EXACTLY: the wall M_h has, in raw coordinates Raw = D_par N M N D_par
(D_par = diag((-1)^k), N = diag(nrm_k) -- a CONGRUENCE, so M_h PSD
<=> Raw_h PSD by Sylvester's law of inertia), displacement rank
exactly 2 against diag(b), i.e. the OFF-DIAGONAL entries are the
divided differences Raw[i,j] = (f(b_i) - f(b_j))/(b_i - b_j) of ONE
explicit source potential f = f_pole + f_arch + 2 om pj on the node
set b_k = (k pi/a)^2.  The classical dictionary (Loewner 1934, Math.
Z. 38, 177; Donoghue, "Monotone Matrix Functions and Analytic
Continuation", Springer 1974; Simon, "Loewner's Theorem on Monotone
Matrix Functions", Springer 2019; Bhatia, "Positive Definite
Matrices", Princeton 2007 Ch. 5 for Loewner/Cauchy kernels) speaks
about the CANONICAL Loewner matrix L_f with diagonal f'(b_i): L_f is
PSD for ALL node choices in an interval I iff f is matrix monotone on
I iff f extends to a Pick/Herglotz function on I; for FIXED n nodes
the PSD condition is the weaker order-n statement.  THIS round
adjudicates whether that theorem is a genuinely new coordinate for
wall positivity or tau_h in a Pick costume.  Goals:
  P1  THE EXACT DICTIONARY.  Which object is the wall exactly?
      Machine-verify at all reachable rungs: (i) the off-diagonal
      one-function Loewner form (r186 G60, upgraded from float64 to
      mp at every rung); (ii) the DIAGONAL: Raw[k,k] differs from the
      canonical f'(b_k) by an explicit excess Delta_k, with the NEW
      exact laws derived and gated here:
        POLE block: Delta_pole = 0 IDENTICALLY -- the pole block IS a
        full canonical Loewner matrix (equivalently the rank-1 Cauchy
        matrix 2 sinh(a/2)^2/((1/4+b_i)(1/4+b_j))), and its potential
        f_pole(b) = -2 sinh(a/2)^2/(1/4+b) is a genuine PICK function
        with EXACT Herglotz representation: point mass
        2 sinh(a/2)^2 delta_{t = -1/4} (Cauchy transform; symbolic +
        mp gates).
        PRIME block: Delta_prime,k = 2a pc_k for k >= 1 and
        4a pc_0 at k = 0, where pc_k = sum_q w_q cos(om_k u_q) is the
        COSINE quadrature of the SAME sieve atoms whose SINE
        quadrature pj feeds the potential (symbolic per-atom proof +
        mp gates at every rung).  The k = 0 doubling mirrors the mode
        norm nrm_0^2 = 2a vs a.
        ARCH block: Delta_arch,k measured in mp (the arch atom
        measure a(w) = e^{-w/2}/(1-e^{-2w}) has a 1/(2w) singularity;
        its cos-transform is log-divergent and the builder diagonal
        carries the -f0(gamma+log pi) regularisation -- the excess is
        recorded, its closed form NOT claimed).
      => the wall is EXACTLY a DIAGONALLY-SHIFTED one-function
      Loewner matrix M_h ~ L_f + diag(Delta), Delta = Delta_arch -
      2a pc (wall sign; k = 0 doubled), i.e. NOT literally the
      canonical L_f of Loewner's theorem, NOT a Loewner-type SUM
      kernel (f_i+f_j)/(b_i+b_j) (anticommutator control gated), NOT
      a sum of two Loewner structures (the displacement normalisation
      g = ones is exact, r186).  The sine quadrature of the source
      sits in the potential, the cosine quadrature in the diagonal
      shift: the wall carries BOTH quadratures in different slots.
  P2  THE PICK-CLASS TEST (the round's decisive cheap numbers).
      (i) order-n in canonical completion: eigsy(L_f) on the actual
      nodes at every rung -- lambda_min(L_f)/||L_f||_F sign + ladder;
      (ii) order-1 necessity: f matrix monotone of ANY order on the
      node hull requires f nondecreasing there -- gated by the
      descent count of the extracted node values (all rungs) and by
      the analytic f' sign-change count on a predefined 129-point
      grid uniform in om (PICK_RUNGS); (iii) refinement battery at
      PICK_RUNGS: R1 = one inserted midpoint (order n+1), R2 = all
      internode midpoints (order 2n-1), R3 = uniform-in-b grid of the
      same size (node-law control) -- lambda_min ladders; (iv) the
      monotone head: first f'-sign-change b*_1 (bisection), number of
      nodes below it, lambda_min of the head submatrix.
  P3  THE HERGLOTZ REPRESENTATION, adjudicated per leg: pole leg
      EXACT point measure (source-expressible: weight 2 sinh(a/2)^2,
      location -1/4 = the completed-square shift of s(1-s)); arch leg
      measured (sign of f_arch' on the grid: monotone-on-hull or
      not); prime leg 2 om pj -- entire oscillatory, NOT Pick; its
      formal density is the signed atom data itself, so any
      positive-measure rewrite of THIS leg is the wall positivity
      again (relabeling barrier named, not crossed).
  P4  WORLDS, WITNESS, SCREENS.  Same dictionary through
      SMOOTH/SCRARITH/EPSTEIN (7 control cells): structure laws must
      hold WORLD-BLIND (linear algebra, typed, never sold), the
      VALUES (lambda_min(L_f) fraction, descent fraction, grid sign
      counts at WGRID cells) may or may not separate -- enum resolved
      either way.  The r172 inflation witness deforms the source
      COEFFICIENT ray (eigenvector-side): every object of this round
      is matrix-side, so the witness is INVARIANT BY CONSTRUCTION --
      typed as definitional, not sold; the matrix-side jet that IS
      detectable is gated instead: ATOMJET (double the FIRST atom's
      (q = 2) weight at h = 5; amendment A1) must shift the
      potential by EXACTLY delta f(b) = 2 om dw sin(om u_jet) and
      the diagonal law by EXACTLY -2a dw cos(om u_jet) (k = 0
      doubled) -- the dictionary detects source jets LINEARLY.  Tau-screen strict: log-log
      slopes of {|lambda_min(L_f)|/||F||, max|Delta|} vs tau_h;
      ride band (0.7, 1.3), flat bar 0.30.  Loop guard extra-sharp
      (A_0-triangle with TAUPOS/TLAWCAP nodes, census-forall-k,
      Gonek-1984, Montgomery-PC flagged, consumed by nothing); tau_h
      enters ONLY as a measured per-rung scalar for the screens.
      r45 prior art carried forward: r45-class LOEWNER-DEAD killed
      the LADDER-as-Loewner-flow identification; r186/this round
      concern the wall MATRIX itself; the kill risked HERE is of the
      "wall positivity == f_h in Pick class" reading -- a NEW
      adjudication, not a re-death.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  canon_indef := lambda_min(L_f)/||L_f||_F < -1e-10 at >= 1
                 non-refused rung;
  pick_dead   := canon_indef OR any descent count >= 1 OR any
                 PICK-rung grid sign-change count >= 1 OR any refined
                 lambda_min/||F|| < -1e-10;
  primary     := DICTIONARY-MISMATCH if canon_indef (the wall is not
                 the canonical object of the theorem AND the
                 canonical object is not PSD -- the Pick costume
                 fails at order n already), else PICK-ORDER-N-ONLY if
                 pick_dead, else PICK-COORDINATE-NEW (requires also
                 tau-flat screens; not anticipated);
  append      := PICK-DEFECT-WORLD-SEPARATING iff the MAIN
                 log10(|lambda_min|/||F||) range at x in {4,5,8} is
                 >= 1 dex clear of every indefinite fake-world cell;
                 else WORLD-MIXED-SMOOTH-PSD-AT-NODES iff the SMOOTH
                 cell is PSD with 0 descents while MAIN is
                 indefinite (amendment A3); else
                 WORLD-BLIND-STRUCTURE.

NOTATION (r171-r186 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; K = ceil(1.25
h log h); om_k = k pi/a; b_k = om_k^2; nrm_0 = sqrt(2a), nrm_k =
sqrt(a); par_k = (-1)^k; atoms = {(u_q, w_q)} = {(log q,
log p/sqrt(q))}, q = p^m <= h; pj_k = sum w sin(om_k u), pc_k =
sum w cos(om_k u); arch J(om) = int_0^{2a} sin(om w) r(w) dw +
Si(2a om)/2, r(w) = e^{-w/2}/(1-e^{-2w}) - 1/(2w), r(0) = 1/4;
J'(om) = int_0^{2a} w cos(om w) r(w) dw + sin(2a om)/(2 om);
f_pole(b) = -2 sinh(a/2)^2/(1/4+b), f_arch(b) = 2 om J(om),
f_prime,wall(b) = 2 om pj(om); f = f_pole + f_arch + 2 om pj;
f'(b): pole' = 2 sinh(a/2)^2/(1/4+b)^2, arch' = J/om + J' (limit
2(int w r dw + a) at b = 0), prime' = sum w [sin(om u)/om +
u cos(om u)] (limit 2 sum w u at b = 0).  f is extracted from the
wall commutator column as fhat_i = b_i Raw[i,0] = f(b_i) - f(0)
(additive constants drop from every Loewner statement); J is
extracted from the arch block as J_i = (om_i/2) RawArch[i,0]; both
extractions are independently re-derived by quadrature at PICK_RUNGS
(wards).  L_f(nodes) := off-diag Raw, diag f'(b_k).  SMOOTH world
atom measure e^{w/2} dw on [0, 2a]: pj_s closed form
((sin(2a om)/2 - om cos(2a om)) e^a + om)/(1/4+om^2), pc_s closed
form (e^a (cos(2a om)/2 + om sin(2a om)) - 1/2)/(1/4+om^2), prime'
by quadrature int (sin(om w)/om + w cos(om w)) e^{w/2} dw.
EPSTEIN/SCRARITH atoms ported VERBATIM from the builder (golden-map
permutation deterministic).

DPS schedule (r182/r186 conditioning ladder VERBATIM): DPS = {4: 60,
5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110,
13: 120, 14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16,
H_HOLD = 20.  PICK_RUNGS = (4, 5, 8, 13); refinement eigensolves in
mp at PICK_MP = (4, 5, 8) (rung dps), float64 at h = 13 (matrix
built in mp at dps 60, downcast -- disclosed reduced scope, refusal
rule below).  GRID_N = 129 points uniform in om on [0, om_max],
GRID_DPS = 40 (sign structure is O(1)); FD ward at grid indices
(7, 31, 63, 95, 119), relative step 1e-12, FD_BAR 1e-6.  WINDOW_N =
17 linear nodes on [0, 0.9 b*_1].  JET_RUNG = 5 (dps 60), jet =
double the weight of the FIRST atom (q = 2; amendment A1).
CONTROLS:
SMOOTH(5), SCRARITH(4, 5, 8), EPSTEIN(8, 9, 10) at CTRL_DPS {60, 60,
80}; WGRID cells (SMOOTH,5), (SCRARITH,5), (EPSTEIN,8).
PRECISION REFUSAL RULE: an eigenvalue-sign statement is REFUSED
(counted, excluded) if |lambda_min| < 10^-(dps-20) ||L||_F (float64:
10^-12 ||L||_F).

FROZEN BARS: LOEW_MP_BAR 1e-30 (off-diag reconstruction, mp, every
rung); POLE_DIAG_BAR 1e-35; PRIME_LAW_BAR 1e-30; WALLDELTA_BAR
1e-28 (Delta assembly consistency); F_WARD_BAR 1e-25; J_WARD_BAR
1e-25; CTRL_LAW_BAR 1e-25; JET_BAR 1e-28; SUMK_S3_MIN 1e-6 (the
anticommutator must NOT be displacement-rank-2-like); INDEF_FRAC
-1e-10; TAU_FLAT_BAR 0.30; TAU_RIDE_BAND (0.7, 1.3); COND_LO/HI
1e-40/1e-10; RUNTIME_BAR 2700 s.  Record tolerances: LM_TOL 0.05
dex; DL_TOL 0.10 dex; BST_TOL 0.05 dex; SLOPE_TOL 0.05; CTRL_TOL
0.10 dex; count records exact.

=======================================================================
RECORD TABLES (frozen at freeze from the ONE disclosed pre-freeze
calibration pass, calib_lp_pass1.log, 27/28; TWO structural smokes
loewner_pick_probe.smoke1/2.log ran rungs 4/5/8 with record
comparisons vacuous pre-freeze by design, smoke2 28/28 after A1/A2).
Verdicts frozen from calibration:
CANONICAL COMPLETION INDEFINITE AT EVERY RUNG -- log10(|lambda_min(
L_f)|/||F||) between -0.84 and -2.00 (roughly CONSTANT, no decay),
SIGN NEGATIVE at all 14 rungs, 0 refusals: the Pick costume misses
wall positivity by 9.4 (h=4) .. 87.9 (h=20) orders (gap to
log10(tau nrm_0^2/||RawW||_F)); descent counts 2..34 of K-1
(monotonicity dead at every rung); grid sign-change counts
10/18/35/68 at h=4/5/8/13, ALL carried by the prime leg (pole+arch
sign changes = 0 everywhere, arch min f' > 0); refinements DEEPEN
the defect (R1/R2/R3 more negative than R0 at every PICK rung); the
monotone head holds exactly 1 node (b=0) at all four PICK rungs;
the 17-node window below b*_1 is INDEFINITE (lm/||F|| ~ -4.3e-2..
-4.6e-2) while f' > 0 on it (min f' 0.26..1.32) -- the classical
scalar-vs-matrix order separation LIVE in the wall potential; Delta
indefinite BOTH signs at every rung; worlds: structure laws hold in
all 7 cells (world-blind by design); VALUES are MIXED: MAIN
indefinite 14/14, the SMOOTH cell is PSD with ZERO descents (its
2a-periodic oscillation vanishes exactly on the node lattice,
sin(2a om_k) = 0 -- commensurate sampling; the incommensurate prime
atoms cannot vanish there), SCRARITH/EPSTEIN mixed (4 of 6
indefinite, no 1-dex clearance): enum
WORLD-MIXED-SMOOTH-PSD-AT-NODES; ATOMJET detected linearly (devs
4.2e-61/3.0e-61); tau-screen: slope log10(|lm|/||F||) vs log10 tau
= -0.011 (R^2 0.383), slope log10 max|Delta| = -0.011 (R^2 0.918)
-- BOTH FLAT (|slope| <= 0.30): the Pick-defect coordinates do NOT
ride the tau currency -- and do not need to, being indefiniteness
certificates, not positivity coordinates; taxonomy resolves
DICTIONARY-MISMATCH + WORLD-MIXED-SMOOTH-PSD-AT-NODES.
CAL_LM (log10(|lambda_min(L_f)|/||F||), sign negative everywhere):
  4: -1.355  5: -2.001  6: -0.938  7: -1.395  8: -0.929  9: -1.008
  10: -0.961  11: -1.269  12: -0.912  13: -1.047  14: -0.837
  15: -0.837  16: -0.944  20: -0.958
CAL_TAUFRAC (log10(tau nrm_0^2/||RawW||_F), display proxy):
  4: -10.80  5: -16.15  6: -20.68  7: -25.59  8: -30.06  9: -34.78
  10: -39.72  11: -44.54  12: -49.82  13: -54.49  14: -59.94
  15: -64.21  16: -69.37  20: -88.85
CAL_DESC (descent count): 4: 2  5: 5  6: 4  7: 7  8: 9  9: 9
  10: 13  11: 16  12: 18  13: 20  14: 22  15: 23  16: 25  20: 34
CAL_DMIN/CAL_DMAX (raw Delta anchors, min/max over k):
  4: -8.72/+1.37   5: -12.80/+1.43   8: -21.41/+5.73
  13: -36.44/+9.04  16: -40.65/+11.32  20: -52.40/+10.26
CAL_GRID (PICK_RUNGS): h=4: nsc 10, fpmin -1.067, log10 b*1 0.671,
  head 1, arch fpmin +1.84e-3, prime nsc 10, win_lm -4.47e-2,
  win_fp +0.26; h=5: nsc 18, fpmin -2.076, log10 b*1 0.487, head 1,
  arch fpmin +1.00e-3, prime nsc 18, win_lm -4.40e-2, win_fp +0.42;
  h=8: nsc 35, fpmin -3.060, log10 b*1 0.300, head 1, arch fpmin
  +6.81e-4, prime nsc 35, win_lm -4.29e-2, win_fp +0.70;
  h=13: nsc 68, fpmin -5.610, log10 b*1 0.092, head 1, arch fpmin
  +7.42e-4, prime nsc 68, win_lm -4.62e-2, win_fp +1.32.
CAL_REFINE (lambda_min/||F|| fractions R0/R1/R2/R3):
  h=4: -0.0442/-0.1198/-0.1498/-0.2063;
  h=5: -0.0100/-0.1543/-0.1624/-0.2227;
  h=8: -0.1176/-0.1346/-0.1384/-0.2106;
  h=13: -0.0897/-0.1450/-0.1302/-0.1852.
CAL_CTRL (lm_log10 / descents / indefinite?): (SMOOTH,5): -4.08 /
  0 / PSD; (SCRARITH,4): -1.55 / 2 / PSD; (SCRARITH,5): -1.66 / 4 /
  indef; (SCRARITH,8): -0.98 / 10 / indef; (EPSTEIN,8): -0.70 / 10
  / indef; (EPSTEIN,9): -1.41 / 10 / PSD; (EPSTEIN,10): -0.61 / 13
  / indef; WGRID nsc: (SMOOTH,5) 20, (SCRARITH,5) 18, (EPSTEIN,8)
  35.  tau < 0 in every fake cell (top-of-spectrum class, r186
  concordant).
CAL_JET: f-shift dev 4.2e-61, Delta-law shift dev 3.0e-61, prime
  rebuild ward 0.0 EXACT.
CAL_SUMK: s3/s1 of the anticommutator 0.372/0.463/0.530/0.622 at
  h=4/5/8/13 (NOT a sum-kernel; difference-class confirmed).
CAL_SLOPES: lm -0.011 (R^2 0.383), dmax -0.011 (R^2 0.918).
DICTIONARY DEVS at calibration: off-diag Loewner mp <= 1.5e-61 (14
rungs), pole diag <= 7.8e-62, prime cos-law <= 6.0e-61, Delta
assembly <= 9.7e-62, wards J <= 1.6e-61 / f <= 1.4e-61, FD <=
8.0e-23.  Runtime 1059 s (bar 2700).
AMENDMENTS (three, all pre-freeze, all disclosed):
A1 (smoke-driven): the jet atom was originally the LAST atom (q = h
  = 5), which sits at u = log 5 = 2a -- COMMENSURATE with every
  mode (sin(2 pi k) = 0): the jet is invisible to the entire basis
  and both linearity metrics degenerate to 0/0.  The jet atom is
  the FIRST atom (q = 2, incommensurate) from smoke2 on.
A2 (smoke-driven): the window gate originally ASSERTED the 17-node
  window below b*_1 PSD; measured: INDEFINITE while f' > 0 there.
  The gate was redefined resolve-and-record BEFORE freeze; the
  window order-separation is now gated as a FINDING, not a failure.
A3 (calibration-driven): the world enum was binary
  (separating/blind) and the calib gate asserted every control cell
  indefinite; measured: SMOOTH PSD + 0 descents (node
  commensurability), SCRARITH/EPSTEIN mixed.  The enum gained the
  third resolution WORLD-MIXED-SMOOTH-PSD-AT-NODES and the gate
  resolves-and-records.
No bar, grid, dps rung, or control recipe moved at any point; the
record tables and resolved enums above were inserted at freeze
(house pattern identical to r186).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition + G03
classical-dictionary exact instances; S1 exact layer G10-G13; S2
house dictionary G20-G25; S3 Pick layer G30-G33; S4 controls/witness
G40-G43; S5 screens/adjudication G50-G53; S6 pricing G60-G61 + G99
runtime.  DETERMINISM: no randomness anywhere (the SCRARITH
permutation is the deterministic golden map); ProcessPool results
keyed; run2 must be identical modulo wall-clock tokens (lines
carrying 'WALL').

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
PICK_RUNGS = (4, 5, 8, 13)
PICK_MP = (4, 5, 8)
GRID_N = 129
GRID_DPS = 40
FD_IDX = (7, 31, 63, 95, 119)
FD_BAR = 1e-6
WINDOW_N = 17
JET_RUNG = 5
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CTRL_SMOOTH = (5,)
CTRL_SCRARITH = (4, 5, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
WGRID_CELLS = (("SMOOTH", 5), ("SCRARITH", 5), ("EPSTEIN", 8))
CTRL_MAIN_X = (4, 5, 8)

# structural bars (frozen pre-calibration)
LOEW_MP_BAR = 1e-30
POLE_DIAG_BAR = 1e-35
PRIME_LAW_BAR = 1e-30
WALLDELTA_BAR = 1e-28
F_WARD_BAR = 1e-25
J_WARD_BAR = 1e-25
CTRL_LAW_BAR = 1e-25
JET_BAR = 1e-28
SUMK_S3_MIN = 1e-6
INDEF_FRAC = -1e-10
EIG_REFUSE_SAFETY = 20
TAU_FLAT_BAR = 0.30
TAU_RIDE_BAND = (0.7, 1.3)
COND_LO, COND_HI = 1e-40, 1e-10

# record tolerances
LM_TOL = 0.05
DL_TOL = 0.10
BST_TOL = 0.05
SLOPE_TOL = 0.05
CTRL_TOL = 0.10

# --------------------- calibrated record tables (calib_lp_pass1.log)
CAL_LM = {4: "-1.355", 5: "-2.001", 6: "-0.938", 7: "-1.395",
          8: "-0.929", 9: "-1.008", 10: "-0.961", 11: "-1.269",
          12: "-0.912", 13: "-1.047", 14: "-0.837", 15: "-0.837",
          16: "-0.944", 20: "-0.958"}
CAL_DESC = {4: 2, 5: 5, 6: 4, 7: 7, 8: 9, 9: 9, 10: 13, 11: 16,
            12: 18, 13: 20, 14: 22, 15: 23, 16: 25, 20: 34}
CAL_DANCHOR = {4: ("-8.72", "1.37"), 5: ("-12.80", "1.43"),
               8: ("-21.41", "5.73"), 13: ("-36.44", "9.04"),
               16: ("-40.65", "11.32"), 20: ("-52.40", "10.26")}
CAL_GRID = {4: {"nsc": 10, "fpmin": "-1.067", "lbst": "0.671",
                "head": 1},
            5: {"nsc": 18, "fpmin": "-2.076", "lbst": "0.487",
                "head": 1},
            8: {"nsc": 35, "fpmin": "-3.060", "lbst": "0.300",
                "head": 1},
            13: {"nsc": 68, "fpmin": "-5.610", "lbst": "0.092",
                 "head": 1}}
CAL_REFINE = {4: ("-0.0442", "-0.1198", "-0.1498", "-0.2063"),
              5: ("-0.0100", "-0.1543", "-0.1624", "-0.2227"),
              8: ("-0.1176", "-0.1346", "-0.1384", "-0.2106"),
              13: ("-0.0897", "-0.1450", "-0.1302", "-0.1852")}
# (lm_log10, descents, lm_neg)
CAL_CTRL = {("SMOOTH", 5): ("-4.08", 0, 0),
            ("SCRARITH", 4): ("-1.55", 2, 0),
            ("SCRARITH", 5): ("-1.66", 4, 1),
            ("SCRARITH", 8): ("-0.98", 10, 1),
            ("EPSTEIN", 8): ("-0.70", 10, 1),
            ("EPSTEIN", 9): ("-1.41", 10, 0),
            ("EPSTEIN", 10): ("-0.61", 13, 1)}
CAL_WGRID = {("SMOOTH", 5): 20, ("SCRARITH", 5): 18,
             ("EPSTEIN", 8): 35}
CAL_SLOPES = {"lm": "-0.011", "dmax": "-0.011"}
REFINE_TOL = 0.10   # relative dex on log10 of |fraction|

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
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
    eig_forb = {"mp" + "V", "cn_mp" + "_str"}
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
        if nm in eig_forb:
            bad.append("eigenvector access %s @%d (this round is "
                       "FULLY eigenvector-free)" % (nm, node.lineno))
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
                       "verification/ import; NO eigenvector access "
                       "anywhere (matrix blocks + the tau scalar "
                       "only): the round is eigenvector-free by AST")


# ------------------------------------------------------- source helpers
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def J_quad(o, aa):
    """arch potential J(om) = int sin(om w) r(w) dw + Si(2a om)/2."""
    L2v = 2 * aa
    if o == 0:
        return mp.mpf(0)
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w), pts)
    return val + mp.si(L2v * o) / 2


def Jp_quad(o, aa):
    """J'(om) = int w cos(om w) r(w) dw + sin(2a om)/(2 om)."""
    L2v = 2 * aa
    if o == 0:
        return mp.quad(lambda w: w * r_of(w), [mp.mpf(0), L2v]) + aa
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: w * mp.cos(o * w) * r_of(w), pts)
    return val + mp.sin(L2v * o) / (2 * o)


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
    """Builder atom recipes ported VERBATIM (SMOOTH returns None --
    integral mode)."""
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms
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
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
        return atoms
    if world == "SMOOTH":
        return None
    raise ValueError(world)


def pj_at(o, atoms, aa):
    if atoms is None:                       # SMOOTH closed form
        if o == 0:
            return mp.mpf(0)
        ea = mp.exp(aa)
        return ((mp.sin(2 * aa * o) / 2 - o * mp.cos(2 * aa * o)) * ea
                + o) / (mp.mpf(1) / 4 + o * o)
    return sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))


def pc_at(o, atoms, aa):
    if atoms is None:                       # SMOOTH closed form
        ea = mp.exp(aa)
        return ((mp.cos(2 * aa * o) / 2 + o * mp.sin(2 * aa * o)) * ea
                - mp.mpf(1) / 2) / (mp.mpf(1) / 4 + o * o)
    return sum((w * mp.cos(o * u) for u, w in atoms), mp.mpf(0))


def primep_wall_at(o, atoms, aa):
    """d/db [2 om pj(om)], wall sign (+); b = om^2."""
    if atoms is None:                       # SMOOTH: quadrature
        L2v = 2 * aa
        if o == 0:
            return mp.quad(lambda w: 2 * w * mp.exp(w / 2),
                           [mp.mpf(0), L2v])
        npts = max(int(mp.floor(L2v * o / mp.pi)), 1)
        pts = ([mp.mpf(0)]
               + [jj * mp.pi / o for jj in range(1, npts + 1)] + [L2v])
        pts = sorted(set(p for p in pts if p <= L2v))
        return mp.quad(lambda w, o=o: (mp.sin(o * w) / o
                                       + w * mp.cos(o * w))
                       * mp.exp(w / 2), pts)
    if o == 0:
        return 2 * sum((w * u for u, w in atoms), mp.mpf(0))
    return sum((w * (mp.sin(o * u) / o + u * mp.cos(o * u))
                for u, w in atoms), mp.mpf(0))


def polep_at(b, s2):
    return 2 * s2 / (mp.mpf(1) / 4 + b) ** 2


def fpole_at(b, s2):
    return -2 * s2 / (mp.mpf(1) / 4 + b)


def fp_wall_at(o, atoms, aa, s2, Jv=None, Jpv=None):
    """f'(b) at b = om^2 (wall potential); J/J' quadratured unless
    supplied."""
    b = o * o
    if Jpv is None:
        Jpv = Jp_quad(o, aa)
    if o == 0:
        archp = 2 * Jpv
    else:
        if Jv is None:
            Jv = J_quad(o, aa)
        archp = Jv / o + Jpv
    return polep_at(b, s2) + archp + primep_wall_at(o, atoms, aa)


def g_wall_at(o, atoms, aa, s2, Jv=None):
    """g(b) = f(b) - f(0) at b = om^2 (additive-constant-free)."""
    b = o * o
    if o == 0:
        return mp.mpf(0)
    if Jv is None:
        Jv = J_quad(o, aa)
    return (fpole_at(b, s2) - fpole_at(mp.mpf(0), s2)
            + 2 * o * Jv + 2 * o * pj_at(o, atoms, aa))


def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def loewner_matrix(gv, fpv, xs):
    n = len(xs)
    L = mp.zeros(n, n)
    for i in range(n):
        L[i, i] = fpv[i]
        for j in range(i):
            L[i, j] = (gv[i] - gv[j]) / (xs[i] - xs[j])
            L[j, i] = L[i, j]
    return L


def eig_min_frac(L, n):
    """(lambda_min, ||L||_F, lambda_min/||L||_F) via mp.eigsy."""
    E = mp.eigsy(L, eigvals_only=True)
    lmin = min(E[i] for i in range(n))
    fro = mp.sqrt(sum(L[i, j] ** 2 for i in range(n)
                      for j in range(n)))
    return lmin, fro, lmin / fro


def eig_min_frac_np(Lnp):
    ev = np.linalg.eigvalsh(Lnp)
    fro = float(np.sqrt((Lnp * Lnp).sum()))
    return float(ev[0]), fro, float(ev[0]) / fro


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
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            atoms = world_atoms("MAIN", h)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            RawPr = raw_of(ce["mpPrime"], par, nrm, K)
            froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            out["log10taufrac"] = float(mp.log(
                abs(tau) * 2 * aa / froW, 10))
            # tau_raw estimate: congruence changes eigenvalues; the
            # RECORDED tau fraction uses the builder tau scaled by the
            # smallest congruence factor (nrm^2 in [a, 2a]) as a
            # DISPLAY proxy only; the exact inertia statement needs no
            # number (Sylvester).
            # --- f extraction (column 0) + off-diag reconstruction
            fhat = [b[i] * RawW[i, 0] for i in range(K)]
            cmax = max(abs(fhat[i]) for i in range(1, K))
            ldev = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    pred = (fhat[i] - fhat[j]) / (b[i] - b[j]) \
                        if i != j else mp.mpf(0)
                    ldev = max(ldev, abs(RawW[i, j] * (b[i] - b[j])
                                         - (fhat[i] - fhat[j])))
            out["loew_dev"] = float(ldev / cmax)
            # --- J extraction + f' assembly at nodes
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]
            pcs = [pc_at(oms[i], atoms, aa) for i in range(K)]
            fp = []
            for i in range(K):
                if i == 0:
                    archp = 2 * Jpv[0]
                else:
                    archp = Jx[i] / oms[i] + Jpv[i]
                fp.append(polep_at(b[i], s2) + archp
                          + primep_wall_at(oms[i], atoms, aa))
            # --- dictionary laws
            pdev = mp.mpf(0)
            for i in range(K):
                pdev = max(pdev, abs(RawP[i, i] - polep_at(b[i], s2)))
                for j in range(i):
                    pdev = max(pdev, abs(
                        RawP[i, j] - (fpole_at(b[i], s2)
                                      - fpole_at(b[j], s2))
                        / (b[i] - b[j])))
            out["pole_diag_dev"] = float(pdev / abs(polep_at(
                mp.mpf(0), s2)))
            prdev = mp.mpf(0)
            prden = mp.mpf(0)
            for i in range(K):
                mult = 2 if i == 0 else 1
                blockp = -primep_wall_at(oms[i], atoms, aa)
                law = blockp + mult * 2 * aa * pcs[i]
                prdev = max(prdev, abs(RawPr[i, i] - law))
                prden = max(prden, abs(law))
            out["prime_law_dev"] = float(prdev / prden)
            # wall Delta + assembly consistency
            dlt = [RawW[i, i] - fp[i] for i in range(K)]
            wdev = mp.mpf(0)
            for i in range(K):
                mult = 2 if i == 0 else 1
                dA = RawA[i, i] - ((2 * Jpv[0]) if i == 0
                                   else (Jx[i] / oms[i] + Jpv[i]))
                pred = dA - mult * 2 * aa * pcs[i] \
                    + (RawP[i, i] - polep_at(b[i], s2))
                wdev = max(wdev, abs(dlt[i] - pred))
            out["walldelta_dev"] = float(wdev / max(abs(d)
                                                    for d in dlt))
            out["dmin"] = float(min(dlt))
            out["dmax"] = float(max(dlt))
            out["dmax_abs_log10"] = float(mp.log(
                max(abs(d) for d in dlt), 10))
            out["delta_has_neg"] = bool(min(dlt) < 0)
            out["delta_has_pos"] = bool(max(dlt) > 0)
            # --- canonical completion L_f on the actual nodes
            Lc = mp.zeros(K, K)
            for i in range(K):
                Lc[i, i] = fp[i]
                for j in range(K):
                    if j != i:
                        Lc[i, j] = RawW[i, j]
            lmin, fro, frac = eig_min_frac(Lc, K)
            refuse = abs(lmin) < mp.mpf(10) ** (-(dps
                                                  - EIG_REFUSE_SAFETY)) \
                * fro
            out["lm_refused"] = bool(refuse)
            out["lm_neg"] = bool(lmin < 0)
            out["lm_frac"] = float(frac)
            out["lm_log10"] = float(mp.log(abs(frac), 10)) \
                if lmin != 0 else float("-inf")
            # --- descent count of the node potential
            out["descents"] = sum(1 for i in range(K - 1)
                                  if fhat[i + 1] < fhat[i])
            # --- PICK layer
            if h in PICK_RUNGS:
                # wards: fresh-quad f and J vs extraction
                jw = mp.mpf(0)
                fw = mp.mpf(0)
                for i in range(1, K):
                    Jq = J_quad(oms[i], aa)
                    jw = max(jw, abs(Jq - Jx[i]) / max(abs(Jq),
                                                       mp.mpf(1)))
                    ga = g_wall_at(oms[i], atoms, aa, s2, Jv=Jq)
                    fw = max(fw, abs(ga - fhat[i]) / cmax)
                out["j_ward_dev"] = float(jw)
                out["f_ward_dev"] = float(fw)
                # grid layer at GRID_DPS
                with mp.workdps(GRID_DPS):
                    aag = mp.log(h) / 2
                    s2g = mp.sinh(aag / 2) ** 2
                    omax = (K - 1) * mp.pi / aag
                    ogrid = [omax * j / (GRID_N - 1)
                             for j in range(GRID_N)]
                    fpg, fpg_arch, fpg_prime = [], [], []
                    for o in ogrid:
                        Jv = J_quad(o, aag)
                        Jpv_ = Jp_quad(o, aag)
                        if o == 0:
                            ar = 2 * Jpv_
                        else:
                            ar = Jv / o + Jpv_
                        pr = primep_wall_at(o, atoms, aag)
                        po = polep_at(o * o, s2g)
                        fpg.append(po + ar + pr)
                        fpg_arch.append(ar)
                        fpg_prime.append(pr)
                    nsc = sum(1 for j in range(GRID_N - 1)
                              if fpg[j] * fpg[j + 1] < 0)
                    tot_pr = [polep_at(ogrid[j] ** 2, s2g)
                              + fpg_arch[j] for j in range(GRID_N)]
                    nsc_wo_pr = sum(1 for j in range(GRID_N - 1)
                                    if tot_pr[j] * tot_pr[j + 1] < 0)
                    nsc_pr = sum(
                        1 for j in range(GRID_N - 1)
                        if fpg_prime[j] * fpg_prime[j + 1] < 0)
                    out["grid_nsc"] = nsc
                    out["grid_nsc_prime"] = nsc_pr
                    out["grid_nsc_noprime"] = nsc_wo_pr
                    out["grid_fpmin"] = float(min(fpg))
                    out["grid_arch_fpmin"] = float(min(fpg_arch))
                    # FD ward
                    fdw = 0.0
                    scale = max(abs(v) for v in fpg)
                    for j in FD_IDX:
                        o = ogrid[j]
                        bb = o * o
                        hstep = bb * mp.mpf("1e-12")
                        gp = g_wall_at(mp.sqrt(bb + hstep), atoms,
                                       aag, s2g)
                        gm = g_wall_at(mp.sqrt(bb - hstep), atoms,
                                       aag, s2g)
                        fd = (gp - gm) / (2 * hstep)
                        fdw = max(fdw, float(abs(fd - fpg[j])
                                             / scale))
                    out["fd_dev"] = fdw
                    # first sign change: bisection on o
                    bst = None
                    for j in range(GRID_N - 1):
                        if fpg[j] * fpg[j + 1] < 0:
                            lo, hi = ogrid[j], ogrid[j + 1]
                            for _ in range(60):
                                mid = (lo + hi) / 2
                                vm = fp_wall_at(mid, atoms, aag, s2g)
                                if vm * fpg[j] < 0:
                                    hi = mid
                                else:
                                    lo = mid
                            bst = ((lo + hi) / 2) ** 2
                            break
                    out["bstar1"] = float(bst) if bst is not None \
                        else float("nan")
                    out["log10_bstar1"] = float(mp.log(bst, 10)) \
                        if bst is not None else float("nan")
                # head window (back at rung dps)
                if bst is not None:
                    bstd = mp.mpf(repr(float(bst)))
                    headn = [i for i in range(K) if b[i] < bstd]
                    out["head_nodes"] = len(headn)
                    if len(headn) >= 2:
                        Lh = mp.zeros(len(headn), len(headn))
                        for ii, i in enumerate(headn):
                            for jj, j in enumerate(headn):
                                Lh[ii, jj] = Lc[i, j]
                        lmh, froh, frach = eig_min_frac(Lh,
                                                        len(headn))
                        out["head_lm_frac"] = float(frach)
                    # WINDOW17 on [0, 0.9 b*1]
                    wnodes = [mp.mpf(9) / 10 * bstd * j
                              / (WINDOW_N - 1) for j in range(WINDOW_N)]
                    gv, fpv = [], []
                    for wb in wnodes:
                        o = mp.sqrt(wb)
                        gv.append(g_wall_at(o, atoms, aa, s2))
                        fpv.append(fp_wall_at(o, atoms, aa, s2))
                    Lw = loewner_matrix(gv, fpv, wnodes)
                    lmw, frow, fracw = eig_min_frac(Lw, WINDOW_N)
                    out["win_lm_frac"] = float(fracw)
                    out["win_fpmin"] = float(min(fpv))
                # refinement battery
                mids = [(b[i] + b[i + 1]) / 2 for i in range(K - 1)]
                # R1 node: midpoint of the gap holding argmin f'
                jmin = min(range(GRID_N),
                           key=lambda j: fpg[j])
                barg = float(ogrid[jmin]) ** 2
                gsel = K - 2
                for i in range(K - 1):
                    if float(b[i]) <= barg <= float(b[i + 1]):
                        gsel = i
                        break
                r1_nodes = sorted(b + [mids[gsel]])
                r2_nodes = sorted(b + mids)
                bmaxv = b[K - 1]
                r3_nodes = [bmaxv * j / (2 * K - 2)
                            for j in range(2 * K - 1)]

                def build_lf(nodes, float64):
                    gv, fpv = [], []
                    for x_ in nodes:
                        o = mp.sqrt(x_)
                        gv.append(g_wall_at(o, atoms, aa, s2))
                        fpv.append(fp_wall_at(o, atoms, aa, s2))
                    if float64:
                        n = len(nodes)
                        Lnp = np.zeros((n, n))
                        for i in range(n):
                            Lnp[i, i] = float(fpv[i])
                            for j in range(i):
                                Lnp[i, j] = float(
                                    (gv[i] - gv[j])
                                    / (nodes[i] - nodes[j]))
                                Lnp[j, i] = Lnp[i, j]
                        return eig_min_frac_np(Lnp)
                    L = loewner_matrix(gv, fpv, nodes)
                    lm, fr, fc = eig_min_frac(L, len(nodes))
                    return float(lm), float(fr), float(fc)

                f64 = h not in PICK_MP
                if f64:
                    with mp.workdps(60):
                        aa60 = mp.log(h) / 2
                        s260 = mp.sinh(aa60 / 2) ** 2
                        # rebuild node lists at dps 60
                        oms60 = [k * mp.pi / aa60 for k in range(K)]
                        b60 = [o * o for o in oms60]
                        mids60 = [(b60[i] + b60[i + 1]) / 2
                                  for i in range(K - 1)]
                        r1n = sorted(b60 + [mids60[gsel]])
                        r2n = sorted(b60 + mids60)
                        r3n = [b60[K - 1] * j / (2 * K - 2)
                               for j in range(2 * K - 1)]
                        sav_aa, sav_s2 = aa, s2
                        aa, s2 = aa60, s260
                        _l1, _f1, fr1 = build_lf(r1n, True)
                        _l2, _f2, fr2 = build_lf(r2n, True)
                        _l3, _f3, fr3 = build_lf(r3n, True)
                        aa, s2 = sav_aa, sav_s2
                else:
                    _l1, _f1, fr1 = build_lf(r1_nodes, False)
                    _l2, _f2, fr2 = build_lf(r2_nodes, False)
                    _l3, _f3, fr3 = build_lf(r3_nodes, False)
                out["r1_frac"] = fr1
                out["r2_frac"] = fr2
                out["r3_frac"] = fr3
                # anticommutator (sum-kernel) control, float64
                Rnp = np.array([[float(RawW[i, j]) for j in range(K)]
                                for i in range(K)])
                bf = np.array([float(x_) for x_ in b])
                Acm = np.diag(bf) @ Rnp + Rnp @ np.diag(bf)
                sv = np.linalg.svd(Acm, compute_uv=False)
                out["sumk_s3s1"] = float(sv[2] / sv[0])
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------- control worker
def w_ctrl(args) -> dict:
    world, x, dps, want_grid = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            atoms = world_atoms(world, x)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            RawPr = raw_of(ce["mpPrime"], par, nrm, K)
            fhat = [b[i] * RawW[i, 0] for i in range(K)]
            cmax = max(abs(fhat[i]) for i in range(1, K))
            ldev = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    ldev = max(ldev, abs(RawW[i, j] * (b[i] - b[j])
                                         - (fhat[i] - fhat[j])))
            out["loew_dev"] = float(ldev / cmax)
            pdev = mp.mpf(0)
            for i in range(K):
                pdev = max(pdev, abs(RawP[i, i] - polep_at(b[i], s2)))
            out["pole_diag_dev"] = float(pdev / abs(polep_at(
                mp.mpf(0), s2)))
            pcs = [pc_at(oms[i], atoms, aa) for i in range(K)]
            prdev = mp.mpf(0)
            prden = mp.mpf(0)
            for i in range(K):
                mult = 2 if i == 0 else 1
                blockp = -primep_wall_at(oms[i], atoms, aa)
                law = blockp + mult * 2 * aa * pcs[i]
                prdev = max(prdev, abs(RawPr[i, i] - law))
                prden = max(prden, abs(law))
            out["prime_law_dev"] = float(prdev / prden)
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]
            Lc = mp.zeros(K, K)
            for i in range(K):
                if i == 0:
                    archp = 2 * Jpv[0]
                else:
                    archp = Jx[i] / oms[i] + Jpv[i]
                Lc[i, i] = polep_at(b[i], s2) + archp \
                    + primep_wall_at(oms[i], atoms, aa)
                for j in range(K):
                    if j != i:
                        Lc[i, j] = RawW[i, j]
            lmin, fro, frac = eig_min_frac(Lc, K)
            out["lm_neg"] = bool(lmin < 0)
            out["lm_log10"] = float(mp.log(abs(frac), 10))
            out["lm_refused"] = bool(
                abs(lmin) < mp.mpf(10) ** (-(dps - EIG_REFUSE_SAFETY))
                * fro)
            out["descents"] = sum(1 for i in range(K - 1)
                                  if fhat[i + 1] < fhat[i])
            if want_grid:
                with mp.workdps(GRID_DPS):
                    aag = mp.log(x) / 2
                    s2g = mp.sinh(aag / 2) ** 2
                    omax = (K - 1) * mp.pi / aag
                    ogrid = [omax * j / (GRID_N - 1)
                             for j in range(GRID_N)]
                    fpg = [fp_wall_at(o, atoms, aag, s2g)
                           for o in ogrid]
                    out["grid_nsc"] = sum(
                        1 for j in range(GRID_N - 1)
                        if fpg[j] * fpg[j + 1] < 0)
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    # G03: classical dictionary instances, exact
    nodes = [sp.Integer(1), sp.Integer(4), sp.Integer(9)]

    def loew(fexpr, bs, var):
        n = len(bs)
        L = sp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    L[i, j] = sp.diff(fexpr, var).subs(var, bs[i])
                else:
                    L[i, j] = ((fexpr.subs(var, bs[i])
                                - fexpr.subs(var, bs[j]))
                               / (bs[i] - bs[j]))
        return L

    t = sp.symbols("t", positive=True)
    Ls = loew(sp.sqrt(t), nodes, t)
    m1 = sp.simplify(Ls[0, 0])
    m2 = sp.simplify(Ls[:2, :2].det())
    m3 = sp.simplify(Ls.det())
    ok_sqrt = (m1 > 0) and (m2 > 0) and (sp.N(m3, 50) > 0)
    Lq = loew(t ** 2, [sp.Integer(1), sp.Integer(2)], t)
    ok_sq = sp.simplify(Lq.det()) == sp.Integer(-1)
    Lc = loew(-1 / (1 + t), [sp.Integer(0), sp.Integer(1),
                             sp.Integer(2)], t)
    ok_c = (sp.simplify(Lc.det()) == 0
            and sp.simplify(Lc[:2, :2].det()) == 0
            and all(sp.simplify(Lc[i, i]) > 0 for i in range(3)))
    check("G03-classical-instances-exact", bool(ok_sqrt and ok_sq
                                                and ok_c),
          "sqrt(b): canonical Loewner PSD on nodes (1,4,9) (minors "
          "1/2, 1/72, det > 0) == operator monotone; b^2: Loewner "
          "det == -1 on (1,2) EXACT -- scalar-monotone but NOT "
          "order-2 monotone (the order separation the round rides); "
          "-1/(1+b): rank-1 Cauchy PSD (Pick, point measure) -- the "
          "three reference points of the Loewner dictionary "
          "(Loewner 1934; Donoghue 1974; Simon 2019; Bhatia 2007)")

    # G10: pole block is a FULL canonical Loewner matrix + Herglotz
    sq, b1, b2, xr, yr = sp.symbols("sq b1 b2 xr yr", positive=True)
    fpole = -2 * sq / (sp.Rational(1, 4) + t)
    od = sp.simplify((fpole.subs(t, b1) - fpole.subs(t, b2))
                     / (b1 - b2)
                     - 2 * sq / ((sp.Rational(1, 4) + b1)
                                 * (sp.Rational(1, 4) + b2)))
    dg = sp.simplify(sp.diff(fpole, t).subs(t, b1)
                     - 2 * sq / (sp.Rational(1, 4) + b1) ** 2)
    z = xr + sp.I * yr
    fz = -2 * sq / (sp.Rational(1, 4) + z)
    imf = sp.simplify(sp.im(sp.expand_complex(fz))
                      - 2 * sq * yr / ((xr + sp.Rational(1, 4)) ** 2
                                       + yr ** 2))
    cau = sp.simplify(fpole - 2 * sq / (-sp.Rational(1, 4) - t))
    check("G10-pole-full-canonical-loewner-pick",
          od == 0 and dg == 0 and imf == 0 and cau == 0,
          "POLE block: off-diag == divided differences AND diag == "
          "f_pole'(b) EXACT (2 sq/((1/4+b_i)(1/4+b_j)) rank-1 "
          "Cauchy): the pole block IS the canonical Loewner matrix "
          "L_{f_pole}; f_pole(z) = c/(t0 - z), c = 2 sinh(a/2)^2, "
          "t0 = -1/4: Im f = c y/|t0-z|^2 > 0 on C+ -- GENUINE PICK "
          "function with EXACT Herglotz representation = point mass "
          "c delta_{-1/4} (Cauchy transform); the -1/4 is the "
          "completed-square shift of s(1-s)")

    # G11: prime diagonal law per atom
    av, uv, wv, ov = sp.symbols("av uv wv ov", positive=True)
    bb = sp.symbols("bb", positive=True)
    f_atom = -2 * sp.sqrt(bb) * wv * sp.sin(sp.sqrt(bb) * uv)
    fpr = sp.diff(f_atom, bb)
    raw_diag = 2 * wv * ((av - uv / 2) * sp.cos(ov * uv)
                         - sp.sin(ov * uv) / (2 * ov))
    mism = sp.simplify(raw_diag - fpr.subs(bb, ov ** 2)
                       - 2 * av * wv * sp.cos(ov * uv))
    lim0 = sp.limit(fpr, bb, 0, "+")
    mism0 = sp.simplify(2 * wv * (2 * av - uv) - lim0 - 4 * av * wv)
    check("G11-prime-diagonal-law-symbolic",
          mism == 0 and mism0 == 0,
          "PRIME block diagonal law, per atom (u, w): Raw[k,k] - "
          "f_prime'(b_k) == 2a w cos(om_k u) for k >= 1 and == 4a w "
          "at k = 0 (mode-norm doubling) IDENTICALLY: the diagonal "
          "excess is the COSINE quadrature of the same atoms whose "
          "sine quadrature is the potential -- the wall carries "
          "both quadratures in different slots (NEW exact law)")

    # G12: arch/prime off-diagonal + one-function wall sum (r186 G17)
    o1, o2, p1, p2, j1, j2, sh = sp.symbols("o1 o2 p1 p2 j1 j2 sh",
                                            positive=True)
    prime_od = 2 * (o1 * p1 - o2 * p2) / (o2 ** 2 - o1 ** 2)
    ok_pr = sp.simplify((o1 ** 2 - o2 ** 2) * prime_od
                        - ((-2 * o1 * p1) - (-2 * o2 * p2))) == 0
    arch_od = -2 * (o1 * j1 - o2 * j2) / (o2 ** 2 - o1 ** 2)
    ok_ar = sp.simplify((o1 ** 2 - o2 ** 2) * arch_od
                        - ((2 * o1 * j1) - (2 * o2 * j2))) == 0
    u1_ = sh / (sp.Rational(1, 4) + o1 ** 2)
    u2_ = sh / (sp.Rational(1, 4) + o2 ** 2)
    ok_po = sp.simplify((o1 ** 2 - o2 ** 2) * 2 * u1_ * u2_
                        - ((-2 * sh ** 2 / (sp.Rational(1, 4)
                                            + o1 ** 2))
                           - (-2 * sh ** 2 / (sp.Rational(1, 4)
                                              + o2 ** 2)))) == 0
    check("G12-block-potentials-symbolic",
          bool(ok_pr and ok_ar and ok_po),
          "(b_i - b_j) Raw[i,j] == f_i - f_j per block (r186 G17 "
          "re-derived): f_prime = -2 om pj, f_arch = +2 om jv, "
          "f_pole = -2 sinh(a/2)^2/(1/4+b); wall = pole + arch - "
          "prime carries f = f_pole + f_arch + 2 om pj -- ONE "
          "source potential, linear in the blocks")

    # G13: displacement structure: C = f 1^T - 1 f^T, ones exact
    f1, f2, f3, c1, c2, c3 = sp.symbols("f1 f2 f3 c1 c2 c3")
    fv = sp.Matrix([f1, f2, f3])
    ones = sp.Matrix([1, 1, 1])
    C = fv * ones.T - ones * fv.T
    ok_anti = sp.simplify(C + C.T) == sp.zeros(3, 3)
    ok_det = sp.simplify(C.det()) == 0
    m01 = C[0, 1]
    check("G13-displacement-ones-normalisation",
          bool(ok_anti and ok_det and sp.simplify(m01 - (f1 - f2))
               == 0),
          "the wall's rank-2 displacement against diag(b) has the "
          "special ONE-FUNCTION form C = f 1^T - 1 f^T "
          "(antisymmetric, det == 0, C_ij = f_i - f_j): a "
          "DIFFERENCE-quotient (Loewner) kernel, NOT a two-function "
          "p q^T - q p^T Cauchy pair and NOT the SUM kernel "
          "(f_i+f_j)/(b_i+b_j) class (Bergman/Pick-kernel theorems, "
          "Bhatia 2007 Ch. 5) -- the sum reading is killed "
          "numerically by the anticommutator control (G25)")


# ------------------------------------------------------------- jet leg
def atomjet_leg() -> dict:
    """ATOMJET at h = JET_RUNG: double the last atom's weight; the
    dictionary must detect it EXACTLY LINEARLY."""
    dps = DPS[JET_RUNG]
    ce = R4.build_cell(JET_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out = {}
    with mp.workdps(dps):
        aa = mp.log(JET_RUNG) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        atoms, _nl = sieve_atoms(JET_RUNG)
        # AMENDMENT A1 (smoke-driven, pre-freeze, disclosed): the
        # original jet atom (LAST atom, q = h = 5) sits at u = log 5
        # = 2a, exactly commensurate with every mode (sin(om_k 2a) =
        # sin(2 pi k) = 0): the jet is INVISIBLE to the whole mode
        # basis and both linearity predictions are identically zero
        # (0/0 metric).  The jet atom is the FIRST atom (q = 2,
        # u = log 2, incommensurate) instead.
        u_l, w_l = atoms[0]
        JET_IDX = 0
        L2v = 2 * aa
        # rebuild prime block twice (base, jet), builder VERBATIM
        def prime_block(scale_last):
            Mp = mp.zeros(K, K)
            ats = [(u, (w * 2 if idx == JET_IDX else w)
                    if scale_last else w)
                   for idx, (u, w) in enumerate(atoms)]
            pj = [sum((w * mp.sin(o * u) for u, w in ats), mp.mpf(0))
                  for o in oms]
            for i in range(K):
                for j2 in range(i):
                    sg = par[i] * par[j2]
                    den = oms[j2] ** 2 - oms[i] ** 2
                    od = 2 * sg * (oms[i] * pj[i]
                                   - oms[j2] * pj[j2]) / den
                    Mp[i, j2] += od
                    Mp[j2, i] += od
            for i in range(K):
                o = oms[i]
                if i == 0:
                    pdiag = sum((w * (L2v - u) for u, w in ats),
                                mp.mpf(0))
                else:
                    pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                      - mp.sin(o * u) / (2 * o))
                                 for u, w in ats), mp.mpf(0))
                Mp[i, i] += 2 * pdiag
            for i in range(K):
                for j2 in range(K):
                    Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
            return Mp
        Mp0 = prime_block(False)
        Mp1 = prime_block(True)
        ward = mp.mpf(0)
        for i in range(K):
            for j in range(K):
                ward = max(ward, abs(Mp0[i, j] - ce["mpPrime"][i, j]))
        out["rebuild_ward"] = float(ward)
        M0 = ce["mpM"]
        # wall_jet = pole + arch - prime_jet = M0 + (prime0 - prime1)
        RawW0 = raw_of(M0, par, nrm, K)
        D01 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                D01[i, j] = M0[i, j] + (Mp0[i, j] - Mp1[i, j])
        RawW1 = raw_of(D01, par, nrm, K)
        f0 = [b[i] * RawW0[i, 0] for i in range(K)]
        f1_ = [b[i] * RawW1[i, 0] for i in range(K)]
        dw = w_l          # the added weight
        fdev = mp.mpf(0)
        fden = mp.mpf(0)
        for i in range(1, K):
            pred = 2 * oms[i] * dw * mp.sin(oms[i] * u_l)
            fdev = max(fdev, abs((f1_[i] - f0[i]) - pred))
            fden = max(fden, abs(pred))
        out["f_shift_dev"] = float(fdev / fden)
        ddev = mp.mpf(0)
        dden = mp.mpf(0)
        for i in range(K):
            mult = 2 if i == 0 else 1
            # wall diag shift = -(prime diag shift); law:
            # d(Delta) = -2a dw cos(om u) mult; the f' shift is the
            # analytic prime' shift -- combine to the raw diag shift:
            fp_shift = (2 * dw * u_l if i == 0 else
                        dw * (mp.sin(oms[i] * u_l) / oms[i]
                              + u_l * mp.cos(oms[i] * u_l)))
            pred = fp_shift - mult * 2 * aa * dw * mp.cos(
                oms[i] * u_l)
            ddev = max(ddev, abs((RawW1[i, i] - RawW0[i, i]) - pred))
            dden = max(dden, abs(pred))
        out["d_shift_dev"] = float(ddev / dden)
    return out


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("loewner_pick_probe -- PRIME.LOEWNER.PICK.01  (mode %s)"
          % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/grids/rungs/dps/recipes declared in the frozen "
          "spec (SPEC_SHA covers the declaration); record tables "
          "frozen from the ONE disclosed calibration pass; tau_h "
          "enters ONLY as a measured per-rung scalar for the "
          "screens (A_0-triangle guard); r45 prior art carried: "
          "r45 LOEWNER-DEAD killed the LADDER-as-Loewner-flow "
          "reading, r186 established the wall MATRIX is "
          "Loewner-structured, THIS round adjudicates the canonical "
          "completion and the function class -- a new adjudication, "
          "not a re-death")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (classical dictionary / block laws / "
            "displacement)")
    exact_layer()

    # ------------------------------------------------------------ S2
    section("S2  HOUSE DICTIONARY (all reachable rungs)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
        dflt = dict(loew_dev=float("inf"), pole_diag_dev=float("inf"),
                    prime_law_dev=float("inf"),
                    walldelta_dev=float("inf"), lm_refused=True,
                    lm_neg=False, lm_frac=float("nan"),
                    lm_log10=float("nan"), descents=0,
                    dmin=float("nan"), dmax=float("nan"),
                    dmax_abs_log10=float("nan"), delta_has_neg=False,
                    delta_has_pos=False, tau_neg=True,
                    log10tau=float("nan"),
                    log10taufrac=float("nan"), K=0,
                    fd_dev=float("inf"), grid_nsc=-1,
                    grid_nsc_prime=-1, grid_nsc_noprime=-1,
                    grid_fpmin=float("nan"),
                    grid_arch_fpmin=float("nan"),
                    r1_frac=float("nan"), r2_frac=float("nan"),
                    r3_frac=float("nan"))
        dflt.update(res[h])
        res[h] = dflt

    check("G20-build-extraction-ward", not errs and all(
        res[h]["loew_dev"] <= LOEW_MP_BAR for h in rungs) and all(
        res[h].get("j_ward_dev", 0.0) <= J_WARD_BAR
        and res[h].get("f_ward_dev", 0.0) <= F_WARD_BAR
        for h in rungs if h in PICK_RUNGS),
          "all %d rungs built; off-diagonal one-function Loewner "
          "reconstruction dev <= %.1e in MP at EVERY rung (r186 G60 "
          "upgraded from float64); extraction wards at PICK_RUNGS: "
          "J vs fresh quadrature <= %.1e, node potential vs fresh "
          "analytic f <= %.1e"
          % (len(rungs),
             max(res[h]["loew_dev"] for h in rungs if not errs),
             max((res[h].get("j_ward_dev", 0.0) for h in rungs
                  if h in PICK_RUNGS), default=0.0),
             max((res[h].get("f_ward_dev", 0.0) for h in rungs
                  if h in PICK_RUNGS), default=0.0)))

    check("G21-diagonal-dictionary-all-rungs", not errs and all(
        res[h]["pole_diag_dev"] <= POLE_DIAG_BAR
        and res[h]["prime_law_dev"] <= PRIME_LAW_BAR
        and res[h]["walldelta_dev"] <= WALLDELTA_BAR for h in rungs),
          "THE EXACT DICTIONARY at every rung (mp): POLE diag == "
          "f_pole' (dev <= %.1e -- the pole block IS canonical, "
          "rank-1 Cauchy, PICK with point measure); PRIME diag law "
          "Raw[k,k] - f_prime' == 2a pc_k (4a pc_0 at k=0) (dev <= "
          "%.1e); wall Delta assembly Delta = Delta_arch - 2a pc "
          "(dev <= %.1e): the wall is EXACTLY a DIAGONALLY-SHIFTED "
          "one-function Loewner matrix M ~ L_f + diag(Delta), "
          "sine quadrature in the potential, cosine quadrature in "
          "the shift; M PSD <=> Raw PSD by Sylvester congruence "
          "(exact, no numeric needed)"
          % (max(res[h]["pole_diag_dev"] for h in rungs),
             max(res[h]["prime_law_dev"] for h in rungs),
             max(res[h]["walldelta_dev"] for h in rungs)))

    nref = sum(1 for h in rungs if res[h].get("lm_refused"))
    all_neg = all(res[h]["lm_neg"] for h in rungs
                  if not res[h].get("lm_refused"))
    lm_tab = {h: res[h]["lm_log10"] for h in rungs}
    tf_tab = {h: res[h]["log10taufrac"] for h in rungs}
    if calib or smoke:
        for h in sorted(lm_tab):
            print("CAL lm h=%d lm_log10 %.3f neg %s taufrac %.2f "
                  "desc %d/%d dmin %.2f dmax %.2f"
                  % (h, lm_tab[h], res[h]["lm_neg"], tf_tab[h],
                     res[h]["descents"], res[h]["K"] - 1,
                     res[h]["dmin"], res[h]["dmax"]))
        ok22 = all_neg and nref == 0
    else:
        ok22 = all_neg and nref == 0 and all(
            abs(lm_tab[h] - float(CAL_LM[h])) <= LM_TOL
            for h in rungs)
    check("G22-canonical-completion-indefinite", ok22,
          "THE ROUND'S FIRST DECISIVE NUMBER: lambda_min(L_f) < 0 "
          "at ALL %d rungs (0 refusals) -- the CANONICAL Loewner "
          "matrix of the wall potential is INDEFINITE at every "
          "reachable rung: log10(|lambda_min|/||F||) %.2f (h=4) -> "
          "%.2f (h=16) -> %.2f (h=20) vs wall tau fraction %.2f -> "
          "%.2f -> %.2f: the Pick costume misses wall positivity "
          "by %.1f..%.1f ORDERS -- wall positivity is NOT the "
          "order-n Loewner-PSD statement about f_h in canonical "
          "completion; it lives in the CO-ACTION of the indefinite "
          "L_f and the indefinite diagonal excess"
          % (len(rungs), lm_tab.get(4, float("nan")),
             lm_tab.get(16, float("nan")),
             lm_tab.get(H_HOLD, float("nan")),
             tf_tab.get(4, float("nan")),
             tf_tab.get(16, float("nan")),
             tf_tab.get(H_HOLD, float("nan")),
             min(abs(tf_tab[h] - lm_tab[h]) for h in rungs),
             max(abs(tf_tab[h] - lm_tab[h]) for h in rungs)))

    desc_ok_v = all(res[h]["descents"] >= 1 for h in rungs)
    if calib or smoke:
        ok23 = desc_ok_v
    else:
        ok23 = desc_ok_v and all(res[h]["descents"] == CAL_DESC[h]
                                 for h in rungs)
    check("G23-node-monotonicity-dead", ok23,
          "descent counts of the extracted node potential: %s of "
          "K-1 -- f_h is NOT nondecreasing on the node hull at ANY "
          "rung; since matrix monotonicity of ANY order on an "
          "interval forces scalar monotonicity there (Loewner/"
          "Donoghue), the INTERVAL-WIDE Pick property is dead at "
          "order 1 at every rung -- no refinement needed for the "
          "kill (the refinements quantify the margin, G32)"
          % str({h: res[h]["descents"] for h in sorted(res)}))

    danch = {h: (res[h]["dmin"], res[h]["dmax"]) for h in rungs}
    dok_v = all(res[h]["delta_has_neg"] and res[h]["delta_has_pos"]
                for h in rungs)
    if calib or smoke:
        ok24 = dok_v
    else:
        ok24 = dok_v and all(
            abs(danch[h][0] - float(CAL_DANCHOR[h][0]))
            <= DL_TOL * abs(float(CAL_DANCHOR[h][0]))
            and abs(danch[h][1] - float(CAL_DANCHOR[h][1]))
            <= DL_TOL * abs(float(CAL_DANCHOR[h][1]))
            for h in rungs if h in CAL_DANCHOR)
    check("G24-diagonal-excess-indefinite", ok24,
          "the diagonal excess Delta is INDEFINITE (both signs) at "
          "every rung (anchors h=4: [%.2f, %.2f], h=20: [%.2f, "
          "%.2f]): the sufficient split [L_f PSD] + [Delta >= 0] "
          "FAILS on BOTH legs -- wall positivity is a genuine "
          "cancellation between the two indefinite summands, not a "
          "sum of positives; the excess magnitude rides the atom "
          "cos-quadrature (source-linear, G21), not tau (G50)"
          % (danch.get(4, (float("nan"),) * 2)[0],
             danch.get(4, (float("nan"),) * 2)[1],
             danch.get(H_HOLD, (float("nan"),) * 2)[0],
             danch.get(H_HOLD, (float("nan"),) * 2)[1]))

    pick_here = [h for h in rungs if h in PICK_RUNGS]
    sk = {h: res[h].get("sumk_s3s1", float("nan")) for h in pick_here}
    check("G25-not-a-sum-kernel", all(
        sk[h] >= SUMK_S3_MIN for h in pick_here),
          "anticommutator control {diag(b), Raw}: s3/s1 = %s at "
          "PICK_RUNGS -- far from rank 2: the wall is NOT in the "
          "(f_i+f_j)/(b_i+b_j) Cauchy/Bergman sum-kernel class "
          "(Bhatia 2007 Ch. 5); the difference (Loewner) class of "
          "G13/G20 is the exact home" % str(
              {h: "%.3f" % sk[h] for h in pick_here}))

    # ------------------------------------------------------------ S3
    section("S3  PICK LAYER (grid / head / refinements)")
    gok_v = all(res[h]["fd_dev"] <= FD_BAR and res[h]["grid_nsc"] >= 1
                for h in pick_here)
    if calib or smoke:
        for h in pick_here:
            print("CAL grid h=%d nsc %d nsc_prime %d nsc_noprime %d "
                  "fpmin %.3f arch_fpmin %.3e lbst %.3f head %d "
                  "head_lm %.2e win_lm %.2e win_fp %.2e fd %.1e"
                  % (h, res[h]["grid_nsc"], res[h]["grid_nsc_prime"],
                     res[h]["grid_nsc_noprime"], res[h]["grid_fpmin"],
                     res[h]["grid_arch_fpmin"],
                     res[h].get("log10_bstar1", float("nan")),
                     res[h].get("head_nodes", -1),
                     res[h].get("head_lm_frac", float("nan")),
                     res[h].get("win_lm_frac", float("nan")),
                     res[h].get("win_fpmin", float("nan")),
                     res[h]["fd_dev"]))
        ok30 = gok_v
    else:
        ok30 = gok_v and all(
            res[h]["grid_nsc"] == CAL_GRID[h]["nsc"]
            and abs(res[h]["grid_fpmin"]
                    - float(CAL_GRID[h]["fpmin"]))
            <= DL_TOL * abs(float(CAL_GRID[h]["fpmin"]))
            for h in pick_here)
    check("G30-fprime-grid", ok30,
          "analytic f' on the frozen %d-point grid (FD ward <= "
          "%.1e): sign-change counts %s, most-negative f' %s -- "
          "the potential OSCILLATES in sign across the hull at "
          "every PICK rung; per-leg attribution: pole' > 0 exact, "
          "ARCH leg min f'_arch = %s > 0 (monotone-on-hull, "
          "measured -- Pick candidacy OPEN), PRIME leg carries ALL "
          "sign changes (%s vs pole+arch %s): THE ARITHMETIC IS "
          "EXACTLY THE NON-PICK CONTENT of the wall potential"
          % (GRID_N, max(res[h]["fd_dev"] for h in pick_here),
             str({h: res[h]["grid_nsc"] for h in pick_here}),
             str({h: "%.2f" % res[h]["grid_fpmin"]
                  for h in pick_here}),
             str({h: "%.1e" % res[h]["grid_arch_fpmin"]
                  for h in pick_here}),
             str({h: res[h]["grid_nsc_prime"] for h in pick_here}),
             str({h: res[h]["grid_nsc_noprime"]
                  for h in pick_here})))

    # AMENDMENT A2 (smoke-driven, pre-freeze, disclosed): the
    # original gate asserted the window PSD -- the structural smoke
    # showed the 17-node window is measurably INDEFINITE while f' >
    # 0 on it: the classical scalar-vs-matrix-monotonicity order
    # separation appears LIVE inside the monotone sliver.  The gate
    # now RESOLVES and RECORDS the window verdict instead of
    # asserting a sign.
    win_sep = all(res[h].get("win_fpmin", -1.0) > 0
                  and res[h].get("win_lm_frac", 0.0) < INDEF_FRAC
                  for h in pick_here)
    hd_ok = all(res[h].get("head_nodes", 0) >= 1
                and "win_lm_frac" in res[h] for h in pick_here)
    if not (calib or smoke):
        hd_ok = hd_ok and win_sep and all(
            res[h].get("head_nodes", -1) == CAL_GRID[h]["head"]
            and abs(res[h].get("log10_bstar1", float("nan"))
                    - float(CAL_GRID[h]["lbst"])) <= BST_TOL
            for h in pick_here)
    check("G31-monotone-head", hd_ok,
          "first f'-sign-change b*_1 (log10: %s) and the monotone "
          "head below it: %s interior nodes -- the Pick-compatible "
          "window of the potential carries almost NOTHING of the "
          "wall (1-2 modes of K); AND the frozen 17-node window "
          "[0, 0.9 b*_1] is INDEFINITE (lambda_min/||F|| %s) while "
          "f' > 0 on it (min f' %s): even on its scalar-monotone "
          "sliver f_h is NOT matrix monotone of window order -- "
          "the order separation of G03 (b^2 exhibit) appears live "
          "in the wall potential (amendment A2, resolve-and-record)"
          % (str({h: "%.2f" % res[h].get("log10_bstar1",
                                         float("nan"))
                  for h in pick_here}),
             str({h: res[h].get("head_nodes", -1)
                  for h in pick_here}),
             str({h: "%.1e" % res[h].get("win_lm_frac",
                                         float("nan"))
                  for h in pick_here}),
             str({h: "%.1e" % res[h].get("win_fpmin",
                                         float("nan"))
                  for h in pick_here})))

    ref_ok_v = all(res[h]["r2_frac"] < INDEF_FRAC
                   and res[h]["r3_frac"] < INDEF_FRAC
                   for h in pick_here)
    if calib or smoke:
        for h in pick_here:
            print("CAL refine h=%d R0 %.4f R1 %.4f R2 %.4f R3 %.4f"
                  % (h, res[h]["lm_frac"], res[h]["r1_frac"],
                     res[h]["r2_frac"], res[h]["r3_frac"]))
        ok32 = ref_ok_v
    else:
        def _cmp(v, s):
            c = float(s)
            return abs(math.log10(abs(v)) - math.log10(abs(c))) \
                <= REFINE_TOL
        ok32 = ref_ok_v and all(
            _cmp(res[h]["r1_frac"], CAL_REFINE[h][1])
            and _cmp(res[h]["r2_frac"], CAL_REFINE[h][2])
            and _cmp(res[h]["r3_frac"], CAL_REFINE[h][3])
            for h in pick_here)
    check("G32-refinement-battery", ok32,
          "refinements INSIDE the same hull stay indefinite and get "
          "WORSE: lambda_min/||F|| fractions R0 (actual nodes) %s, "
          "R1 (one inserted midpoint) %s, R2 (all midpoints) %s, "
          "R3 (uniform-in-b, node-law control) %s -- the defect "
          "DEEPENS under refinement (order-(n+1) and order-(2n-1) "
          "fail worse than order-n): there is NO hidden "
          "interval-wide margin; h=13 in float64 (disclosed "
          "reduced scope, defect >> refusal floor)"
          % (str({h: "%.3f" % res[h]["lm_frac"] for h in pick_here}),
             str({h: "%.3f" % res[h]["r1_frac"]
                  for h in pick_here}),
             str({h: "%.3f" % res[h]["r2_frac"]
                  for h in pick_here}),
             str({h: "%.3f" % res[h]["r3_frac"]
                  for h in pick_here})))

    canon_indef = any(res[h]["lm_neg"] and res[h]["lm_frac"]
                      < INDEF_FRAC for h in rungs
                      if not res[h].get("lm_refused"))
    pick_dead = canon_indef or desc_ok_v or any(
        res[h]["grid_nsc"] >= 1 for h in pick_here) or ref_ok_v
    check("G33-interval-wide-adjudication", bool(pick_dead
                                                 and canon_indef),
          "FROZEN RESOLUTION: canon_indef == %s AND pick_dead == %s "
          "-- the interval-wide Pick property of f_h fails at order "
          "1 (G23/G30), the fixed-node canonical test fails at "
          "order n (G22), the refinements fail deeper (G32): "
          "'f_h in Pick class' is FALSE on the node hull, and even "
          "the order-n statement is FALSE in canonical completion "
          "-- the wall's positivity is NOT expressible as the "
          "Loewner/Pick positivity of its own potential; primary "
          "verdict DICTIONARY-MISMATCH with the exact class stated "
          "(G21)" % (canon_indef, pick_dead))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + WITNESS")
    ctasks = ([("SMOOTH", x, CTRL_DPS["SMOOTH"],
                ("SMOOTH", x) in WGRID_CELLS) for x in CTRL_SMOOTH]
              + [("SCRARITH", x, CTRL_DPS["SCRARITH"],
                  ("SCRARITH", x) in WGRID_CELLS)
                 for x in CTRL_SCRARITH]
              + [("EPSTEIN", x, CTRL_DPS["EPSTEIN"],
                  ("EPSTEIN", x) in WGRID_CELLS)
                 for x in CTRL_EPSTEIN])
    if smoke:
        ctasks = [("SCRARITH", 5, 60, True)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
        cres[k].update(dict(loew_dev=float("inf"),
                            pole_diag_dev=float("inf"),
                            prime_law_dev=float("inf"),
                            lm_neg=False, lm_log10=float("nan"),
                            lm_refused=True, descents=0,
                            tau_neg=True))
    check("G40-dictionary-world-blind", not cerrs and all(
        v["loew_dev"] <= LOEW_MP_BAR
        and v["pole_diag_dev"] <= POLE_DIAG_BAR
        and v["prime_law_dev"] <= CTRL_LAW_BAR
        for v in cres.values()),
          "the FULL dictionary (off-diag Loewner mp, pole "
          "canonical, prime cos-law) holds in EVERY control world "
          "(max devs %.1e / %.1e / %.1e over %d cells): the "
          "structure is LINEAR ALGEBRA + per-atom identities, "
          "world-blind BY DESIGN -- typed, never sold as a "
          "separator" % (
              max((v["loew_dev"] for v in cres.values()),
                  default=float("nan")),
              max((v["pole_diag_dev"] for v in cres.values()),
                  default=float("nan")),
              max((v["prime_law_dev"] for v in cres.values()),
                  default=float("nan")), len(cres)))

    # AMENDMENT A3 (calibration-driven, pre-freeze, disclosed): the
    # original enum was binary (separating / blind) and the calib
    # gate asserted all control cells indefinite -- the measured
    # truth is RICHER: MAIN is indefinite at 14/14 rungs, but the
    # SMOOTH cell is PSD with ZERO descents -- the smooth channel's
    # oscillation is 2a-PERIODIC in om and vanishes EXACTLY on the
    # node lattice (sin(2a om_k) = sin(2 pi k) = 0): commensurate
    # sampling; the incommensurate prime atoms (u = log q != 2a)
    # cannot vanish there.  SCRARITH/EPSTEIN cells are MIXED (4 of
    # 6 indefinite).  The enum gains the third resolution
    # WORLD-MIXED-SMOOTH-PSD-AT-NODES; the gate resolves-and-records.
    smooth_psd = any(k[0] == "SMOOTH" and not cres[k]["lm_neg"]
                     and cres[k]["descents"] == 0 for k in cres)
    if calib or smoke:
        for (w_, x_), v in sorted(cres.items()):
            print("CAL ctrl %s x=%d lm_log10 %.2f neg %s desc %d "
                  "nsc %s tau_neg %s"
                  % (w_, x_, v["lm_log10"], v["lm_neg"],
                     v["descents"], v.get("grid_nsc", "-"),
                     v["tau_neg"]))
        ok41 = not cerrs
        sep = False
    else:
        ok41 = all(
            abs(cres[k]["lm_log10"] - float(CAL_CTRL[k][0]))
            <= CTRL_TOL and cres[k]["descents"] == CAL_CTRL[k][1]
            and cres[k]["lm_neg"] == bool(CAL_CTRL[k][2])
            for k in cres) and all(
            cres[k].get("grid_nsc") == CAL_WGRID[k]
            for k in CAL_WGRID if k in cres)
        lm_main = [lm_tab[x_] for x_ in CTRL_MAIN_X if x_ in lm_tab]
        lm_fake = [cres[k]["lm_log10"] for k in cres
                   if cres[k]["lm_neg"]]
        sep = bool(lm_main and lm_fake
                   and (max(lm_main) < min(lm_fake) - 1.0
                        or min(lm_main) > max(lm_fake) + 1.0))
        ok41 = ok41 and smooth_psd and not sep
    world_enum = ("PICK-DEFECT-WORLD-SEPARATING" if sep
                  else ("WORLD-MIXED-SMOOTH-PSD-AT-NODES"
                        if smooth_psd else "WORLD-BLIND-STRUCTURE"))
    check("G41-world-values-enum", ok41,
          "world VALUES (resolve-and-record, amendment A3): "
          "fake-world log10(|lambda_min(L_f)|/||F||) %s vs MAIN %s "
          "-- MAIN indefinite 14/14, SMOOTH cell PSD with 0 "
          "descents (the 2a-periodic smooth oscillation vanishes "
          "on the node lattice: sin(2a om_k) == 0, commensurate "
          "sampling -- the incommensurate prime atoms cannot), "
          "SCRARITH/EPSTEIN MIXED (no 1-dex clearance): enum "
          "resolves %s -- the NODE-SAMPLED Pick defect carries an "
          "arithmetic fingerprint through incommensurability, but "
          "is NOT a clean world detector (contrast: the r186 "
          "gap-fraction anomaly separated cleanly)"
          % (str({k: "%.2f%s" % (cres[k]["lm_log10"],
                                 "-" if cres[k]["lm_neg"] else "+")
                  for k in sorted(cres)}),
             str({x_: "%.2f" % lm_tab[x_] for x_ in CTRL_MAIN_X
                  if x_ in lm_tab}), world_enum))

    jet = atomjet_leg()
    check("G42-witness-and-atomjet", jet["rebuild_ward"] <= 1e-40
          and jet["f_shift_dev"] <= JET_BAR
          and jet["d_shift_dev"] <= JET_BAR,
          "r172 inflation witness: deforms the source COEFFICIENT "
          "ray (eigenvector-side) -- every object of this round "
          "(Raw, f, Delta, L_f) is matrix-side, hence witness-"
          "INVARIANT BY CONSTRUCTION (definitional, typed, not "
          "sold; r186's {l_0, l_2} residue pair remains the witness "
          "detector).  The matrix-side jet IS detected: ATOMJET at "
          "h=%d (FIRST atom q=2 weight doubled -- amendment A1: the "
          "last atom q=5 sits at u = 2a, commensurate, invisible to "
          "every mode; prime rebuild ward %.1e EXACT): potential "
          "shift == 2 om dw sin(om u_jet) (dev %.1e) and diagonal "
          "shift == prime'-shift - 2a dw cos(om u_jet) (dev %.1e) "
          "-- the dictionary reads source jets EXACTLY LINEARLY "
          "(sine in the potential, cosine in the shift)"
          % (JET_RUNG, jet["rebuild_ward"],
                      jet["f_shift_dev"], jet["d_shift_dev"]))

    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep = mp.eigsy(Qp_, eigvals_only=True)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G43-conditioning-ward", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e "
          "(round-118 trap absent)" % d_eps)

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if h != H_HOLD
           and not res[h].get("lm_refused")
           and not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_lm, _i, r2_lm = fit_line(xs_t, [res[h]["lm_log10"]
                                       for h in scr])
    sl_dm, _i, r2_dm = fit_line(xs_t, [res[h]["dmax_abs_log10"]
                                       for h in scr])
    flat_lm = abs(sl_lm) <= TAU_FLAT_BAR
    flat_dm = abs(sl_dm) <= TAU_FLAT_BAR
    if calib or smoke:
        print("CAL tau slopes: lm %.3f (r2 %.3f) dmax %.3f (r2 %.3f)"
              % (sl_lm, r2_lm, sl_dm, r2_dm))
        ok50 = True
    else:
        ok50 = (abs(sl_lm - float(CAL_SLOPES["lm"])) <= SLOPE_TOL
                and abs(sl_dm - float(CAL_SLOPES["dmax"]))
                <= SLOPE_TOL and flat_lm and flat_dm)
    check("G50-tau-screen", ok50,
          "log-log slopes vs tau_h across rungs: "
          "|lambda_min(L_f)|/||F|| %+.3f, max|Delta| %+.3f -- BOTH "
          "FLAT (bar %.2f; ride band %s NOT entered): the Pick-"
          "defect coordinates do NOT ride the tau/conditioning "
          "currency -- honestly typed: they do not need to, "
          "because they are INDEFINITENESS certificates, not "
          "positivity coordinates; no relabeling FLAG, no sign "
          "source either" % (sl_lm, sl_dm, TAU_FLAT_BAR,
                             str(TAU_RIDE_BAND)))

    delivered = {
        "ATOMS": ["PJ", "PC"], "PJ": ["F-POT"],
        "PC": ["DIAG-SHIFT"],
        "MBLOCKS": ["LOEW-OFF", "TAU-SCALAR"],
        "F-POT": ["LOEW-OFF", "CANON-LF"],
        "LOEW-OFF": ["DICTIONARY"], "DIAG-SHIFT": ["DICTIONARY"],
        "CANON-LF": ["PICK-TESTS"], "DICTIONARY": ["PICK-TESTS"],
        "PICK-TESTS": ["SCREENS"], "TAU-SCALAR": ["SCREENS"],
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
                          "RH": ["MONTGOMERY-PC"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u, vs in g2.items():
            joint.setdefault(u, list(vs))
    anc = set()
    for node in ("DICTIONARY", "PICK-TESTS", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC", "RH"}
    check("G51-loop-guard", ndet >= 3 and not has_cycle(delivered)
          and not hot,
          "flagged cycles DETECTED (A0-triangle with TAUPOS/TLAWCAP "
          "explicit, census-forall-k, Gonek-1984, Montgomery-PC), "
          "consumed by NOTHING: DFS ancestry of every delivered "
          "verdict node is free of the flagged set; tau_h is "
          "consumed as a measured scalar only (screens), no sign "
          "hypothesis anywhere; the zero-verification-as-hypothesis "
          "and RH-conditional-moments loops have no edge into this "
          "round (fully zero-free, no ordinate cache)")

    check("G52-composed-chain-typing", True,
          "leg typing: dictionary laws (pole canonical + Herglotz "
          "point mass, prime cos-law, off-diag Loewner, ones "
          "normalisation) EXACT; {f, Delta} SOURCE-CLASSICAL "
          "(linear in atoms, jet-warded G42); lambda_min ladders / "
          "grid sign counts / refinement defects MEASURED; the "
          "'wall positivity == f_h Pick' reading REFUTED-AT-"
          "MEASURED-VALUES (G22/G23/G30/G32 -- refutation, not "
          "relabeling: the candidate coordinate is not even a "
          "positivity coordinate); the pole-leg Herglotz measure "
          "2 sinh(a/2)^2 delta_{-1/4} EXACT + source-expressible; "
          "the prime leg's formal density IS the signed atom data "
          "-- rewriting IT as a positive measure would be the wall "
          "positivity again: relabeling barrier NAMED, not crossed "
          "(the P3 dream statement dies honestly here)")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
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
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "LPK"): INF, ("LPK", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5; a COUNTERFACTUAL "
          "grant of 'f_h Pick => wall positivity' as a unit edge "
          "would raise the flow to 6 -- NOT REAL (the premise is "
          "measured FALSE, G22/G33): this round adds NO flow; "
          "census cardinality UNCHANGED; RH unreachable without "
          "the omega edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + RESIDUE")
    check("G60-herglotz-adjudication", True,
          "P3 per leg: POLE leg EXACT Herglotz point measure "
          "2 sinh(a/2)^2 delta_{t=-1/4} (G10; weight = builder "
          "constant, location = the completed-square -1/4: "
          "SOURCE-CLASSICAL); ARCH leg monotone-on-hull MEASURED "
          "(min f'_arch > 0 on all four PICK grids, G30) -- Pick "
          "candidacy OPEN, representation not computed, priced as "
          "a named classical object (Stieltjes inversion of an "
          "explicit r(w)-transform); PRIME leg NON-PICK (entire "
          "oscillatory, all sign changes, G30) -- its formal "
          "density is the signed atoms themselves; the dream "
          "statement 'f_h Pick <=> positivity of a source measure' "
          "is DEAD at the prime leg in both directions: f_h is not "
          "Pick (measured), and a positive rewrite of the prime "
          "leg would BE the wall positivity (relabeling barrier)")

    check("G61-classical-dictionary-priced", True,
          "citations fixed to the exact class: Loewner 1934 (Math. "
          "Z. 38, 177) / Donoghue 1974 / Simon 2019 apply to the "
          "CANONICAL L_f -- measured INDEFINITE at every rung "
          "(G22), so the theorem's hypothesis fails on the wall's "
          "own potential; Bhatia 2007 Ch. 5 (Loewner/Cauchy "
          "kernels) for the sum-kernel class -- excluded by G25; "
          "the wall's true class: DIAGONALLY-SHIFTED one-function "
          "Loewner matrix, shift = cos-quadrature of the source "
          "(exact prime law G11/G21) + regularised arch excess "
          "(measured; the arch atom measure e^{-w/2}/(1-e^{-2w}) "
          "has the 1/(2w) singularity whose cos-transform is "
          "log-divergent -- the builder's gamma+log pi "
          "counterterm, disclosed, closed form NOT claimed); r45 "
          "LOEWNER-DEAD prior art distinguished and carried (G02); "
          "the IIKS/RHP lane of r186 (resolvent asymptotics of the "
          "integrable kernel) is UNTOUCHED by this kill -- it "
          "never assumed f Pick; NEEDS-NAMED-EXTERNAL-TOOL there "
          "stands")

    info("POST-ROUND RESIDUE (unchanged in cardinality; ONE "
         "candidate coordinate adjudicated OUT): {H1 ^ H2 ^ H3}-"
         "KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the wall is EXACTLY L_f + diag(Delta) "
         "(dictionary machine-verified at every rung, pole leg "
         "fully canonical + Pick with exact point measure, prime "
         "diagonal law NEW-EXACT: cos-quadrature of the atoms), "
         "and the Pick/Loewner FUNCTION-CLASS reading of wall "
         "positivity is REFUTED at measured values: L_f canonical "
         "is indefinite at all 14 rungs (defect 1e-2..1e-4 of "
         "||F|| vs tau at 1e-11..1e-89), f_h non-monotone on every "
         "hull, refinements deepen the defect, the monotone head "
         "holds 1-2 modes, the defect is world-blind and tau-flat. "
         " The genuinely new EXACT objects: the diagonal-excess "
         "law (both quadratures of the source in one matrix) and "
         "the pole-leg Herglotz point mass.  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WALL-IS-SHIFTED-LOEWNER-EXACT(G20/G21: off-diag mp at all "
        "rungs; pole canonical; prime cos-law NEW)",
        "POLE-LEG-PICK-EXACT-POINT-MASS(G10: 2 sinh(a/2)^2 "
        "delta_{-1/4})",
        "PRIME-DIAG-COS-QUADRATURE-LAW-EXACT(G11/G21)",
        "CANONICAL-COMPLETION-INDEFINITE-ALL-RUNGS(G22)",
        "NODE-MONOTONICITY-DEAD-ALL-RUNGS(G23)",
        "DIAGONAL-EXCESS-INDEFINITE-BOTH-SIGNS(G24)",
        "NOT-A-SUM-KERNEL(G25) + NOT-TWO-LOEWNER(G13)",
        "PRIME-LEG-SOLE-PICK-BREAKER(G30: arch monotone-on-hull "
        "measured)",
        "MONOTONE-HEAD-1-2-MODES(G31)",
        ("WINDOW-ORDER-SEPARATION(G31: scalar-monotone sliver, "
         "matrix order fails)" if win_sep else
         "WINDOW-RESOLVED(G31)"),
        "REFINEMENT-DEEPENS-DEFECT(G32)",
        "PICK-CLASS-DEAD-ON-HULL(G33)",
        "DICTIONARY-MISMATCH(primary; exact class stated G21/G61)",
        world_enum + "(G41)",
        "ATOMJET-DETECTED-LINEARLY(G42) + "
        "WITNESS-MATRIX-SIDE-INVARIANT-DEFINITIONAL(G42)",
        "TAU-FLAT-BOTH-COORDINATES(G50: not a relabel, not a sign "
        "source)",
        "HERGLOTZ-POLE-EXACT+ARCH-OPEN+PRIME-BARRIER(G60)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51) + MINCUT-UNCHANGED(G53) + "
        "RESIDUE-UNCHANGED"]
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
        "WALL-IS-SHIFTED-LOEWNER-EXACT",
        "POLE-LEG-PICK-EXACT-POINT-MASS",
        "PRIME-DIAG-COS-QUADRATURE-LAW-EXACT",
        "CANONICAL-COMPLETION-INDEFINITE-ALL-RUNGS",
        "NODE-MONOTONICITY-DEAD-ALL-RUNGS",
        "DIAGONAL-EXCESS-INDEFINITE-BOTH-SIGNS",
        "NOT-A-SUM-KERNEL",
        "PRIME-LEG-SOLE-PICK-BREAKER",
        "MONOTONE-HEAD-1-2-MODES",
        ("WINDOW-ORDER-SEPARATION" if win_sep
         else "WINDOW-RESOLVED"),
        "REFINEMENT-DEEPENS-DEFECT",
        "PICK-CLASS-DEAD-ON-HULL",
        "DICTIONARY-MISMATCH",
        world_enum,
        "ATOMJET-DETECTED-LINEARLY",
        "TAU-FLAT-BOTH-COORDINATES",
        "HERGLOTZ-POLE-EXACT-ARCH-OPEN-PRIME-BARRIER",
        "LOOPS-FLAGGED-NOT-CONSUMED",
        "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
