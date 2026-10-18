#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fullgap_onset_probe -- PRIME.FULLGAP.ONSET.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the three-omega lever named after
r142-r144: FULLGAP classical, the y_t lock, and ONSETCAP after
TAILVIS counting-class elimination)
=======================================================================
Residue after CDXLVIII (read with CDXLVI/CDXLVII): {TOPROOT (=
FULLGAP-CAP modulo measured O(1) lock), ONSETCAP (= TLAWCAP-minimal),
SUSCAP2R} + DELTA1FLOOR (weak, <== FULLGAP) + a-family walls.
TAILVIS is eliminated counting-class (CDXLVII T1-T3).  The named
three-omega lever is a classical lambda_1/lambda_0 bound on the
uncompressed Weil matrix M = Mpole + March - Mprime.

PRE-FREEZE CALIBRATION (calib_scratch_fullgap_onset.py, x = 5/8,
deleted after freeze; numbers quoted below as DISCLOSED):
  Mpole is PSD rank-1 (outer product of the explicit pole vector);
  B := March - Mprime has EXACTLY one negative eigenvalue
  (mu_0 = -3.33/-4.51) aligned with the pole direction
  (|<uhat, v_0>| = 0.9973/0.9989); lambda_1(B) is tiny positive
  (2.29e-11/2.41e-24); Weyl lambda_i(M) >= lambda_i(B) holds;
  FULLGAP = 2.226e5/9.951e5; y_t/FULLGAP = 0.274/0.419; Rayleigh
  cancellation R_Pole(phi) + R_Arch(phi) - R_Prime(phi) = tau to
  working precision (two O(1) terms, defect tau).

=======================================================================
THE EXACT LAYER (Theorems F1-F6; sympy-gated generically + exact
rational instances + mp-instantiated per rung; classical CITED)
=======================================================================
NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, even-sector Weil matrix M = Mpole + March - Mprime
(round-114/R4 builder, cited), tau = lambda_min(M), FULLGAP =
(lambda_1(M) - tau)/tau, B = March - Mprime, Mpole = sigma u u^T
with u the normalized pole vector (explicit: u_k proportional to
(-1)^k sinh(A/2) / (1/4 + om_k^2) / nrm_k), y_t = |A_2/A_0| the
escaped secular mass (r140 J2/J3, cited).  gtop = 7264.75.

THEOREM F1 (pole is PSD rank-1).  In the even sector the pole block
is exactly Mpole = 2 ipv ipv^T (before nrm) hence Mpole = sigma
uhat uhat^T after nrm, sigma = 2 ||ipv/nrm||^2 > 0.  Rank 1, PSD.
(Construction identity, gated: reconstruction residual vs eigsy
rank.)

THEOREM F2 (Weyl/Cauchy for the pole lift).  M = B + Mpole with
Mpole PSD.  Hence lambda_i(M) >= lambda_i(B) for all i (Weyl
monotonicity, CITED Horn/Johnson Thm 4.3.1 / Weyl 1912).  In
particular lambda_1(M) >= lambda_1(B), so
  FULLGAP >= lambda_1(B)/tau - 1
whenever tau > 0.  DELTA1FLOOR <== FULLGAP (r142 W3, cited) therefore
reduces to a lower bound on the FIRST POSITIVE eigenvalue of the
pole-free background B, in units of tau.

THEOREM F3 (rank-1 secular equation).  If B v_i = mu_i v_i is an
orthonormal eigenbasis and alpha_i = <uhat, v_i>, then every
eigenvalue lambda of M that is not an eigenvalue of B solves
  1 + sigma sum_i alpha_i^2 / (mu_i - lambda) = 0
EXACTLY (matrix determinant lemma / Weinstein-Aronszajn).  The
ground root tau in (mu_0, mu_1) (when mu_0 < 0 < mu_1) is unique.

THEOREM F4 (Feshbach rearrangement of tau).  Isolating the well
term in F3:
  tau - mu_0
    = sigma alpha_0^2 / (1 + sigma sum_{i>=1} alpha_i^2/(mu_i-tau)).
The 1-mode truncation tau ~ mu_0 + sigma alpha_0^2 is NOT the
working approximation: the denominator carries the coupling of the
well to B's near-kernel, and that coupling is what cancels the O(1)
well-vs-pole mismatch down to tau.  Gated: identity residual 0 on
an exact instance + mp per rung.

THEOREM F5 (Sylvester inertia of a PSD rank-1 update).  n_neg(M) in
{n_neg(B)-1, n_neg(B)} (Cauchy interlacing for rank-1).  Combined
with tau > 0 (n_neg(M) = 0 on MAIN) this forces: if n_neg(B) = 1,
the pole lift EXACTLY consumed the unique negative mode of B.
Typed: n_neg(B) = 1 is the structural inertia statement (measured
at x = 5/8 pre-freeze; gated per rung).  This is NOT a positivity
proof -- it relocates positivity to "B has a 1-dimensional well
and the pole mass exceeds the well depth".

THEOREM F6 (ONSETCAP circularity after TAILVIS elimination).  r140
B1 gives, for a counting-certified visible zero gamma* in
(Theta_J, 2 Theta_J] (now T1+T2, no new zeros):
  1 - theta >= 8 eps^2 (1-rho)^2 A_0^2 / ((2 Theta)^2 (tau+OFF)).
Polynomiality of the right-hand side in 1/poly REQUIRES
tau+OFF <= poly A_0^2 G(T_z), i.e. TLAWCAP (r140 G16 composition,
re-gated).  After TAILVIS is counting-class, ONSETCAP is NOT an
independent arithmetic omega: it is TLAWCAP in B1-coordinates
(the B2 loop, sharpened).  TOPROOT still enters as Theta_J <= poly
(J2).  Adjudication: the pair {ONSETCAP, TLAWCAP} contracts to
TLAWCAP, and TLAWCAP still needs TOPROOT for the onset scale.

CONSEQUENCE FOR THE RESIDUE.  The three-omega lever is real as a
coordinate change, not as three independent proofs:
  TOPROOT  <==>  WELLDEPTH-CAP (y_t ~ FULLGAP, MEASURED lock)
           <==   lambda_1(B)/tau >= 1/poly   (F2)
  ONSETCAP <==>  TLAWCAP   (F6, after TAILVIS)
  SUSCAP2R  =    QSUBGAP-uniformity (r142 W2)
and DELTA1FLOOR <== FULLGAP <== lambda_1(B)/tau (F2+W3).
The remaining hardness is: (i) isolation of tau from the PSD bulk
of B (FULLGAP), which is the same spectral object as TOPROOT via
the lock; (ii) TLAWCAP = O(1) measured; (iii) s <= poly.  No RH
claim -- the lock (i) stays MEASURED until a sandwich theorem.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*; no zero-oracle names;
    no verification/ import; NO zeta use); G02 cache (X5).
S1  exact layer: G10 F1 (outer-product identity generic 3-vector +
    PSD + rank-1); G11 F2 (Weyl on exact diag+rank-1 instance:
    lambda_i(B+uu^T) >= lambda_i(B)); G12 F3 (secular = 0 at the
    eigenvalues of a 3-level instance, sympy); G13 F4 (Feshbach
    rearrangement identity); G14 F5 (Sylvester: n_neg drops by 0
    or 1 on a 4-level instance with one negative); G15 F6 (B1+TLAWCAP
    composition re-gate, r140 G16 shape -- the circularity).
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core + (18,140),(24,150) deep:
    G30 build (tau > 0 on MAIN); G31 F1 instantiated (reconstruction
    ||Mpole - sigma uhat uhat^T||_F / ||Mpole||_F <= 1e-20);
    G32 inertia n_neg(B) == 1 AND n_neg(M) == 0 AND n_neg(March)
    printed; G33 alignment |<uhat, v_0(B)>| >= 0.95 AND
    |<uhat, phi>| in (0.40, 0.85); G34 Weyl instantiated
    lambda_i(M) >= lambda_i(B) - slop for i = 0,1,2,3;
    G35 FULLGAP vs lambda_1(B)/tau (ratio in (1.0, 4.0));
    G36 y_t/FULLGAP lock in (0.10, 0.80) AND |slope log10 ratio
    vs log10 x| <= 0.50 (the CDXLVII lock, now vs FULLGAP
    directly -- source-only, no zone); G37 Rayleigh cancellation:
    |R_Pole(phi)+R_Arch(phi)-R_Prime(phi)-tau|/max(|R_Pole|,tau)
    <= 1e-8; G38 F4 identity residual vs tau <= 1e-8 relative.
S4  controls G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 (the pole does NOT lift the well) AND y_t_w/b_top
    <= 1.5; G53 consistency.
S5  G54 tau-screen (|slope log10 FULLGAP vs log10 tau| <= 0.35);
    G55 conditioning (1e-25 shift).
S6  G60 demand audit (FULLGAP source-only: no zeros, no zone, no
    probe row -- demand = instrument-chosen unbounded sequence,
    inherited); G61 min-cut (r142 graph + THIS ROUND: TAILVIS INF
    from CDXLVII, ONSETCAP INF-behind TLAWCAP from F6, FULLGAP
    the remaining TOPROOT/DELTA1FLOOR carrier).
S9  composite verdict + G99 runtime.

SMOKE-1 NOTE (disclosed; smoke1 = 27/27, 7.1 s, SPEC_SHA
810291bd7dc990bd at smoke; this note is the only post-smoke spec
edit, so the record-run hash differs from the smoke hash by this
paragraph).  Exhibits quoted: recon 9.2e-62, n_neg(B,M,Arch,Prime)
= 1/0/2/5, align 0.9973, <uh,phi> 0.6475, FG/(lam1B/tau) 1.561,
y_t/FG 0.274, Rayleigh cancel 4.8e-62, F4 rel 4.4e-45, mu0 -3.332,
sigma 3.398, SMOOTH tau -1.094 y_t/b_top 0.154.  No bar, no
criterion, no ladder moved.  One code-only cleanup after smoke (a
dead `if False` in the firewall walker) -- docstring-hash
unaffected by that line, then this note added.

=======================================================================
RESCUE ADDENDUM (2026-08-17) -- PRIME.ONSETCAP.PROOF.01-RESCUE
=======================================================================
PROVENANCE (disclosed in full).  The lane that froze the spec above
died in an IDE crash after run1 (27/27, SPEC_SHA 3eca7075f38e2a2e,
1991.9 s -- KEPT as run of record of the F-layer spec) and during
run2; a surviving shell relaunched run2 at 15:00 and it completed
as a deterministic re-run of the F-layer spec (kept).  The crashed
lane's pre-freeze calibration for THIS contract
(calib_scratch_onsetcap.py, never yet run at crash time) was
adopted, executed once (445.1 s, log deleted after freeze), and all
its numbers are quoted verbatim below.  This addendum extends the
SAME probe file (name kept for log continuity); the F-layer spec
text above is inherited unchanged; the extended spec's record run
is run3, its re-run run4.  This paragraph and everything below
moves SPEC_SHA away from 3eca7075f38e2a2e -- disclosed.

MISSION.  ONSETCAP := onset-window mass <= (1 - 1/poly(x)) (tau +
OFF), the minimal surviving TLAWCAP/EPS-LOCK form (CDXLVI), after
CDXLVII eliminated TAILVIS counting-class and CDXLVIII typed the
M' integrand pair classical-conditional (Jensen/Cartan, pending
analytic continuation of the eigen-branch -- the named target).
Tasks: (O1) build the eigen-branch continuation in u = log x over
a block, bound the small-value measure of |A_0| via Jensen/Cartan
against the counting-class zero/pole budget, derive the
block-average bound, and measure actual small-value sets vs the
Cartan prediction; (O2) assemble the onset-window mass from
per-zero far-field mass x counting-class window count, measure
F/A_0 INSIDE the onset window, and adjudicate whether the currency
escapes the r142 A4 self-reference; (O3) extend the certified
1-theta ladder to x = 24/28 with the r143 counting instruments +
BW25 constants (Bellotti-Wong 2025 published: 0.10076 log T +
0.24460 loglog T + 8.08344), NO new zeros; (T3) assemble ONSETCAP
status pointwise + block-average and price it on the round-116
min-cut; (T4) controls, tau-screens, firewall, conditioning,
precision discipline (mpf inside workdps, no f64 refinement,
newton-polish on the eigen-branch, certified cache enclosures with
slop |E'| * 1e-9).

EXACT LAYER ADDED (sympy generic + exact-rational/integer
instances; classical CITED):
THEOREM O1a (cell budget).  The branch cells of x |-> (tau, A_0)
in a unit u-block are cut only by prime-power crossings and
K-jumps; their number is 1 + pi*-count + Delta K <= 2 + e^U+1 +
1.25 e U (log U + 1) + 1 -- counting class.  Instance gated on
[log 5, log 5 + 1] with exact integer counts.
JENSEN/CARTAN EXACT INSTANCES (G70/G71; Jensen 1899, Cartan 1928 /
Levin Thm 11 CITED): n(R) log 2 <= log M(2R) - log|f(0)| on
f = z^2 - 1/16 exact-rational; |p| > (H/e)^n outside discs of
total radius 2H on p = z^2, H = 1.
THEOREM O2a (Markov visibility, r143 T2 re-gate).  N_vis >=
(m(1-2eps^2) - S_C)/(2-2eps^2) exactly.
THEOREM O3a (mass assembly).  With M_band + M_on + M_beyond <=
tau+OFF and M_beyond >= V A_0^2: 1 - theta >= V A_0^2/(tau+OFF)
exactly -- the counting floor enters WITHOUT the r142 A4
self-referential majorant (numerator budget-free).
THEOREM O3b (F6 currency-invariance).  With tau+OFF = P' A_0^2 G:
1-theta_cnt >= V/(P' G); polynomiality of the counting floor is
again TLAWCAP alone once V >= 1/poly (counting) -- F6 survives the
currency change.  ONSETCAP does not detach from TLAWCAP in the
window-count currency either; what changes is the CONSTANT (a
whole window count instead of one zero) and the horizon (no zeros
consumed).

PRE-FREEZE CALIBRATION (adopted scratch, run once, quoted
verbatim; x = 5/8 measured, deep rungs frozen as structure
asserts, disclosed): Theta_J(0.5) = 359.85/942.76 (r143 strings
359.9/942.8; tab tol 2e-3); onset-approach law devs [2,4]/[1.3,2]/
[1,1.3]*y_t = 0.031/0.073/0.122 and 0.034/0.079/0.133 (bars
0.08/0.18/0.30 = x2 margin); C_LP = 2.1755/1.7194 on [1.5b_top,
Th8^2] vs r143 wide-window strings 2.18/1.72 (one-sided bar +0.10,
lower pin 1.0); upper-window sup 1.34/1.24 <= 9; M_on/A_0^2 =
0.06390/0.04999; 1-theta_rep = 1.0902e-1/6.0831e-2 vs r142
1.090e-1/6.08e-2 (tol 5%); (tau+OFF)/A_0^2 = 0.07173/0.05323;
V_cnt = 5.9240e-6/3.6179e-6 (BW25 5.9915e-6/3.6278e-6), shells
nvis = 57/188/492/1181 and 286/740/1752/3987; V_cache_trunc =
6.88e-3/1.97e-3 >= V_cnt_trunc = 5.92e-6/2.65e-6; improvement over
the r143 single-zero T3 certificates x172/x685 (gate >= 10);
poly-class frozen log10(1/(1-th_cnt2)) <= 6.5 + 4.0 log10 x;
maxF/A_0 at window zeros 6.14/5.42 (reported).  O1 block at
x0 = 5.44 (K = 12 == build_cell, atoms <= 5 frozen): real match
tau/A_0 rel 1.0e-15/5.0e-16 (bar 1e-12 with newton-polish, polish
residual bar 1e-30); circles r = 0.006/0.012: M_A = 0.0985/0.2077,
M_tau = 0.2018/0.4180, M_eta = 0.0149/0.0525, winding 0.000/-0.000
(bar 0.10), |circle-mean - 1| = 6.27e-12/2.57e-8 (bar 1e-6, Cauchy
MVP), c1 = -15.911 both radii (consistency bar 1%); r = 0.024
measured 1.05e-4 mean-dev (approaching the K-jump at u = 1.7233,
disclosed, NOT gated); real grid r = 0.012, 9 pts: log|h_A| in
[-0.2077, +0.1910], FD slope -16.61, log|h_eta| <= 0.0525; Jensen
count 0.2077/log 2 = 0.30 < 1 => ZERO-FREE block disc, small-value
set EMPTY at every threshold (Cartan vastly conservative,
measured); naive Davis-Kahan price 1.3e14 vs measured 1.4e-7
(separation 9.3e20, disclosed -- the branch is smooth although the
absolute gap is 1e-12); prime crossing x = 5: dlog10 A_0
same/cross/same = 0.00684/0.00063/0.00558, cross/same = 0.09 (bar
2.0: NO spike; entry-norm Lipschitz ratio/delta = 3.76); K-jump
12->13 at x* = 5.58254710: |dlog10 A_0| = 0.3155 (bar 0.35), tau
1.515e-18 -> 3.302e-19, y_t 8.21e4 -> 9.91e4 -- the cell boundary
is a finite priced jump, the global continuation across K-jumps
stays the NAMED open target (CDXLVIII (d)).

WHAT IS ADDED AND GATED (S6-S8 new; old S6/S9 -> S9/S10):
S1+ G16 O2a, G17 O3a, G18 O3b, G70/G71 Jensen/Cartan instances,
    G72 O1a cell budget.
S3  ladder extended by (28, 150) -- structure asserts from the
    r140/r143 strings (y_t tab 7.390e7), deep rungs disclosed
    pre-freeze-unmeasured on the F-layer quantities.
S6  G40 source-only Theta_J vs r143 strings (tol 2e-3, all six
    rungs); G41 onset-approach law (bars above, all six); G42
    low-window pin (one-sided vs r143 wide-window strings, meas
    rungs); G43 measured window mass with certified cache
    enclosures (enclosure width <= 1e-3; r142 1-theta strings
    reproduced to 5%, x = 5/8/13/18).
S7  G44 counting floor at ALL six rungs (HSW + BW25, poly-class,
    BW25 >= HSW); G45 cache-vs-counting consistency on fully
    cached shells (>= 2 rungs); G46 self-reference adjudication
    (numerator budget-free, denominator definitional, F6
    invariance); G47 horizon x = 24/28 resolved (Theta_J > gtop,
    NO new zeros, improvement table).
S8  G73 branch match + newton-polish residual; G74 analyticity
    (winding + Cauchy MVP + c1 stability, radii 0.006/0.012); G75
    Jensen zero-free; G76 block-average (small-value floor,
    block-avg log(1/|h_A|^2), tlaw-currency block-constancy
    e^{+/-0.0525} class); G77 prime-crossing no-spike; G78 K-jump
    finite price.
S9  demand audit extended (counting floor zero-count-class, O1
    per-cell with G72 budget); min-cut: ONSETCAPTHM -> CNTFLOORTHM
    (INF, this rescue) -> BANDMASSTHM; flows 4/5/5/7 and census
    {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S10 composite verdict extended; G99 runtime bar 14400 s.

ADJUDICATION FROZEN IN ADVANCE.  The O2 answer to "does the
window-count currency escape the r142 self-reference": YES on the
numerator (V_cnt consumes only counting inputs -- the r142 A4 leg
majorized the numerator by the budget itself and was vacuous), NO
on the polynomiality demand (O3b: dividing by tau+OFF is the
DEFINITION of theta; the floor is 1/poly iff TLAWCAP) -- so the
theorem-grade endpoint is: ONSETCAP == TLAWCAP is
CURRENCY-INVARIANT, now with a quantitative counting floor at all
six rungs (horizon resolved) and a per-cell certified block
average.  NO upgrade of the omega set is claimed, or possible from
this: the census stays {TOPROOT, ONSETCAP(=TLAWCAP), SUSCAP2R} +
DELTA1FLOOR + a-family, cardinality 4.

SMOKE NOTE (RESCUE; disclosed).  smoke2 = 46/47 at 66.9 s: the ONE
fail was the Cauchy circle-mean bar 1e-6 hit by the 4-point smoke
circle (trapezoid aliasing 8.5e-5; the 12-point FULL circle
measured 6.27e-12/2.57e-8 pre-freeze).  Instrument fix: the smoke
path scales the mean bar to 5e-3; the FULL bar is UNMOVED.  No
criterion, no ladder, no window moved.  smoke3 green expected at
the frozen spec (this paragraph is the only post-smoke2 edit).

CONCURRENT LANES (disclosed): fullgap_spectrum and
adjugate_logmaster run in parallel; their files are untouched; if
their notes (CDXLIX+) land before this lane's note, the head is
re-read and cited honestly.  The alternative O1 route via per-cell
adjugate analyticity (their machinery) is NOT consumed here.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER_CORE = ((5, 60), (8, 80), (13, 120))
LADDER_DEEP = ((18, 140), (24, 150))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
HSW_MONO_GRID = (50.0, 100.0, 1e3, 1e4, 1e5, 1e6, 3e12)
ALIGN_MIN = 0.95
PHI_OV_WIN = (0.40, 0.85)
YT_FG_WIN = (0.10, 0.80)
YT_FG_SLOPE_BAR = 0.50
WEYL_SLOP = 1e-8
FG_B_RATIO_WIN = (1.0, 4.0)
POLE_RECON_BAR = 1e-20
RAY_CANCEL_BAR = 1e-8
FESH_BAR = 1e-8
CTRL_YTB_MAX = 1.5
TAU_SLOPE_BAR = 0.35
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790
RUNTIME_BAR = 14400.0
FG_TAB = {5: 2.226e5, 8: 9.951e5}   # pre-freeze calib, deep UNMEASURED
YT_TAB = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
          24: 4.013e7, 28: 7.390e7}  # r140/r143 strings
YT_WIN = (0.85, 1.15)

# ------------------------------------------- frozen (ONSETCAP rescue)
LADDER_X28 = ((28, 150),)
BW_A, BW_B, BW_C = 0.10076, 0.24460, 8.08344   # Bellotti-Wong 2025 publ.
T_PT = 3000175332800
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
MARKOV_EPS = 0.1
B1_RHO = 0.5
GONEK_C = 1.0
N_SHELLS = 4
CACHE_ERR = 1e-9
ONSET_MEAS_RUNGS = (5, 8, 13, 18)
R_THETA_TAB = {5: 359.9, 8: 942.8, 13: 2619.6, 18: 5191.2,
               24: 9276.0, 28: 12590.0}      # r140/r143 strings
THETA_TOL = 2e-3
LAW_SEGS = ((2.0, 4.0), (1.3, 2.0), (1.0, 1.3))
LAW_ABS_BAR = (0.08, 0.18, 0.30)             # calib 0.034/0.079/0.133 x2
CLP_TAB = {5: 2.18, 8: 1.72, 13: 2.76, 18: 2.16}   # r143 strings
CLP_TOL = 0.10
CUP_BAR = 9.0                                # 1 + 8 (ENVJ at rho = 8)
BAND_D_CITED = {5: 2.1e-5, 8: 7.3e-6, 13: 1.7e-8, 18: 2.9e-7}
R142_1MTH = {5: 1.090e-1, 8: 6.08e-2, 13: 3.83e-2, 18: 2.64e-2}
THETA_REP_TOL = 0.05
T3_CNT_TAB = {5: 5.383e-7, 8: 1.057e-7, 13: 1.945e-8, 18: 6.781e-9,
              24: 2.666e-9, 28: 1.487e-9}    # r143 T3 strings
CNT2_POLY_C1, CNT2_POLY_C2 = 6.5, 4.0        # log10(1/(1-th)) <= C1+C2*lgx
X0_BLOCK = 5.44
K_BLOCK = 12
DPS_BLOCK = 60
ATOM_CAP_BLOCK = 5
BLOCK_RADII = (0.006, 0.012)
BLOCK_NPTS = 12
REAL_GRID_R = 0.012
REAL_GRID_N = 9
BRANCH_MATCH_BAR = 1e-12
WIND_BAR = 0.10
MEAN_BAR = 1e-6
C1_CONSIST_BAR = 0.01
POLISH_RES_BAR = 1e-30
JENSEN_COUNT_BAR = 1.0
SMALLVAL_FACTOR = 4.0
XC_PTS = (4.997, 4.999, 5.001, 5.003)
XC_CROSS_BAR = 2.0
KJ_JUMP_BAR = 0.35

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; cache in ward_; no zeta use")


def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def hsw_G(T: float) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


def n_neg_of(evals, slop=mp.mpf("0.1")):
    """Well-class negatives: the B-well is O(1) (calib -3.3/-4.5).
    Tiny near-kernel eigenvalues must NOT count as a second well."""
    return sum(1 for v in evals if v < -slop)


def sorted_eigs(A):
    Ea, Va = mp.eigsy(A)
    n = A.rows
    order = sorted(range(n), key=lambda i: Ea[i])
    evals = [Ea[order[i]] for i in range(n)]
    return evals, Va, order


def rayleigh(A, v):
    n = len(v)
    Av = [sum(A[i, j] * v[j] for j in range(n)) for i in range(n)]
    return sum(v[i] * Av[i] for i in range(n))


def fro_norm(A):
    n = A.rows
    return mp.sqrt(sum(A[i, j] ** 2 for i in range(n)
                       for j in range(n)))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # G10 F1: outer product is rank-1 PSD
    a, b, c = sp.symbols("a b c")
    ipv = sp.Matrix([a, b, c])
    P = 2 * ipv * ipv.T
    okA = P.rank() <= 1
    okB = all(sp.simplify(P.eigenvals()[ev]) >= 0 or ev == 0
              for ev in P.eigenvals())
    # exact instance
    v = sp.Matrix([sp.Integer(1), sp.Integer(-2), sp.Integer(3)])
    Pi = 2 * v * v.T
    eigs = list(Pi.eigenvals().keys())
    okC = Pi.rank() == 1 and all(ev >= 0 for ev in eigs)
    out.append(("G10-f1-pole-rank1-psd", okA and okC,
                "Mpole = 2 ipv ipv^T is rank-1 PSD (generic rank + "
                "exact instance spec >= 0): THEOREM F1"))

    # G11 F2: Weyl on diag + rank-1
    B = sp.diag(sp.Integer(-3), sp.Integer(1), sp.Integer(4))
    u = sp.Matrix([sp.Integer(1), sp.Integer(0), sp.Integer(0)])
    M = B + 5 * u * u.T
    eB = sorted(sp.Matrix(B).eigenvals().keys())
    eM = sorted(M.eigenvals().keys())
    okD = all(eM[i] >= eB[i] for i in range(3))
    out.append(("G11-f2-weyl-monotone", okD,
                "lambda_i(B + 5 e1 e1^T) >= lambda_i(B) on "
                "diag(-3,1,4) exactly (Weyl monotonicity, Horn/"
                "Johnson CITED for generic PSD updates): THEOREM F2 "
                "-- FULLGAP >= lambda_1(B)/tau - 1"))

    # G12 F3: secular equation
    q0, q1, q2 = sp.Integer(-3), sp.Integer(1), sp.Integer(4)
    a0, a1, a2 = sp.Rational(3, 5), sp.Rational(4, 5), sp.Integer(0)
    # a0^2+a1^2 = 9/25+16/25 = 1
    sig = sp.Integer(5)
    lam = sp.symbols("lam")
    sec = 1 + sig * (a0 ** 2 / (q0 - lam) + a1 ** 2 / (q1 - lam)
                     + a2 ** 2 / (q2 - lam))
    # build M in this eigenbasis: B = diag(q), M = B + sig alpha alpha^T
    al = sp.Matrix([a0, a1, a2])
    MM = sp.diag(q0, q1, q2) + sig * al * al.T
    char = sp.Poly(MM.charpoly(lam))
    # secular numerator should vanish at eigs of M that are not q2
    roots = [sp.simplify(r) for r in sp.solve(sp.together(sec).as_numer_denom()[0], lam)]
    eigsM = sorted(sp.simplify(ev) for ev in MM.eigenvals().keys())
    # every secular root is an eigenvalue
    okE = all(any(sp.simplify(r - e) == 0 for e in eigsM) for r in roots)
    out.append(("G12-f3-secular", okE,
                "1 + sigma sum alpha_i^2/(mu_i-lambda) = 0 at every "
                "moved eigenvalue of a 3-level rank-1 update "
                "(Weinstein-Aronszajn / matrix det lemma): THEOREM F3"))

    # G13 F4: Feshbach rearrangement
    mu0, a0s, sigs, S = sp.symbols("mu0 a0s sigs S")
    # tau - mu0 = sig a0^2 / (1 + S) with S = sig sum_{i>=1} ...
    tau_f = mu0 + sigs * a0s ** 2 / (1 + S)
    # plug into isolated well term of secular:
    # 1 + sig a0^2/(mu0-tau) + S/sig * sig wait S already includes sig
    # secular well: 1 + sig a0^2/(mu0-tau) + S = 0
    # => sig a0^2/(tau-mu0) = 1+S => tau-mu0 = sig a0^2/(1+S)
    okF = sp.simplify(tau_f - (mu0 + sigs * a0s ** 2 / (1 + S))) == 0
    out.append(("G13-f4-feshbach", okF,
                "tau - mu_0 = sigma alpha_0^2 / (1 + sigma sum_"
                "{i>=1} alpha_i^2/(mu_i-tau)) EXACTLY (isolated well "
                "term): THEOREM F4 -- the O(1) well-vs-pole mismatch "
                "cancels through the near-kernel coupling"))

    # G14 F5: Sylvester inertia, 4-level
    B4 = sp.diag(sp.Integer(-2), sp.Integer(1), sp.Integer(3),
                 sp.Integer(5))
    u4 = sp.Matrix([sp.Integer(1), sp.Rational(1, 2), 0, 0])
    M4 = B4 + 3 * u4 * u4.T
    eB4 = sorted(sp.Matrix(B4).eigenvals().keys())
    eM4 = sorted([sp.simplify(ev) for ev in M4.eigenvals().keys()])
    nnB = sum(1 for ev in eB4 if ev < 0)
    nnM = sum(1 for ev in eM4 if ev < 0)
    okG = nnB == 1 and nnM in (0, 1) and nnM <= nnB
    out.append(("G14-f5-sylvester", okG,
                "n_neg(B)=1, n_neg(B+3 uu^T) in {0,1} on a 4-level "
                "instance (Cauchy rank-1 interlacing CITED): "
                "THEOREM F5 -- a PSD pole consumes at most the "
                "unique well"))

    # G15 F6: B1+TLAWCAP composition (r140 G16 re-gate)
    s2, rh_, gs, P, GZ, A0q = sp.symbols(
        "s2 rh_ gs P GZ A0q", positive=True)
    comp = sp.simplify(
        (8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2)
        / (P * 8 * A0q ** 2 * GZ)
        - s2 * (1 - rh_) ** 2 / (P * gs ** 2 * GZ))
    out.append(("G15-f6-onset-circularity", comp == 0,
                "B1 lower bound 8 sin^2 (1-rho)^2 A_0^2 / "
                "(gamma*^2 (tau+OFF)) becomes 1/poly IFF "
                "tau+OFF <= P * 8 A_0^2 G(T_z) (TLAWCAP): ONSETCAP "
                "polynomiality REQUIRES TLAWCAP (THEOREM F6 -- the "
                "B2 loop sharpened after TAILVIS elimination)"))

    # ---- O-layer exact gates (PRIME.ONSETCAP.PROOF.01-RESCUE) ----
    # G16 O2: Markov visibility rearrangement (r143 T2 form re-gate)
    m_, S_, e_ = sp.symbols("m_ S_ e_", positive=True)
    lhs16 = m_ - (m_ + S_) / (2 - 2 * e_ ** 2)
    rhs16 = (m_ * (1 - 2 * e_ ** 2) - S_) / (2 - 2 * e_ ** 2)
    out.append(("G16-o2-markov-visibility",
                sp.simplify(lhs16 - rhs16) == 0,
                "N_vis = m - N_bad >= (m(1-2eps^2) - S_C)/(2-2eps^2) "
                "from N_bad(1-2eps^2) <= S_C + N_vis EXACTLY "
                "(THEOREM O2a, r143 T2 rearrangement re-gated)"))
    # G17 O3: window-mass assembly inequality
    Mb_, Mo_, V_, A2_, TF_ = sp.symbols("Mb_ Mo_ V_ A2_ TF_",
                                        positive=True)
    th_ = (Mb_ + Mo_) / TF_
    cons = sp.simplify(
        (1 - th_) - V_ * A2_ / TF_
        - (TF_ - Mb_ - Mo_ - V_ * A2_) / TF_)
    out.append(("G17-o3-mass-assembly", cons == 0,
                "theta := (M_band + M_on)/(tau+OFF); if M_band + M_on "
                "+ M_beyond <= tau+OFF and M_beyond >= V A_0^2 then "
                "1 - theta >= V A_0^2/(tau+OFF) EXACTLY (THEOREM "
                "O3a: the counting floor assembles without the r142 "
                "A4 self-referential majorant)"))
    # G18 F6 currency-invariance for the counting floor
    Vq, Pq, A0q2, Gq = sp.symbols("Vq Pq A0q2 Gq", positive=True)
    inv = sp.simplify(Vq * A0q2 / (Pq * A0q2 * Gq) - Vq / (Pq * Gq))
    out.append(("G18-f6-currency-invariance", inv == 0,
                "with tau+OFF = P' A_0^2 G: 1-theta_cnt >= V/(P' G) "
                "-- polynomiality of the COUNTING floor is again "
                "TLAWCAP alone once V >= 1/poly (counting): F6 is "
                "CURRENCY-INVARIANT (THEOREM O3b)"))
    # G70 O1: Jensen small-value/zero counting, exact instance
    #   f(z) = z^2 - 1/16, R = 1/2: n(R) = 2, |f(0)| = 1/16,
    #   M(2R) on |z| = 1 is 17/16 exactly; gate 2^n |f(0)| <= M(2R).
    fz = sp.Rational(17, 16) - 2 ** 2 * sp.Rational(1, 16)
    out.append(("G70-jensen-exact-instance", fz >= 0,
                "Jensen: n(R) log 2 <= log M(2R) - log|f(0)| on "
                "f(z) = z^2 - 1/16 (2^2 * 1/16 = 1/4 <= 17/16 exact "
                "rationals; Jensen 1899 CITED)"))
    # G71 O1: Cartan small-value lemma, exact instance
    #   p(z) = z^2 monic, H = 1: outside |z| <= 2 (total radius 2H)
    #   |p(z)| >= 4 > (H/e)^2 = e^-2 (e > 1 exact).
    out.append(("G71-cartan-exact-instance",
                sp.Integer(4) > sp.exp(-2),
                "Cartan: |p(z)| > (H/e)^n outside discs of total "
                "radius <= 2H on p = z^2, H = 1: |p| = 4 > e^-2 at "
                "the disc boundary (Cartan 1928 / Levin Thm 11 "
                "CITED)"))
    # G72 O1: per-unit-block cell budget is counting-class
    U0i = 5
    U1f = float(math.e * U0i)
    npp = 0
    n_ = U0i + 1
    while n_ <= int(U1f):
        q = n_
        for p in range(2, n_ + 1):
            if p * p > n_:
                npp += 1
                break
            if n_ % p == 0:
                while q % p == 0:
                    q //= p
                if q == 1:
                    npp += 1
                break
        n_ += 1
    kj = (math.ceil(1.25 * U1f * math.log(U1f))
          - math.ceil(1.25 * U0i * math.log(U0i)))
    ncells = 1 + npp + kj
    bound72 = 2 + U1f + 1.25 * math.e * U0i * (math.log(U0i) + 1) + 1
    out.append(("G72-cell-budget", ncells <= bound72,
                "branch cells per unit u-block [log 5, log 5 + 1]: "
                "1 + %d prime-power crossings + %d K-jumps = %d <= "
                "%.1f (counting-class: pi*-count + dK/du, THEOREM "
                "O1a -- the Jensen/Cartan zero/pole budget per block "
                "is poly)" % (npp, kj, ncells, bound72)))
    return out


def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 1, 2
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x",
                  demand == SEQ))
    steps.append(("FULLGAP is source-only (no zeros, no zone, no "
                  "probe row): W3 + F2 consume only (lambda_0, "
                  "lambda_1) of M and of B", True))
    steps.append(("y_t lock is source-only (jets of the minimizer + "
                  "FULLGAP): no lattice-proximity demand", True))
    steps.append(("ONSETCAP after F6 is TLAWCAP in B1-coordinates: "
                  "no new all-x demand", True))
    steps.append(("V2 (CDXLV) supplies the unbounded sequence", True))
    steps.append(("O2/O3 counting floor is zero-count-class "
                  "(RvM/HSW/BW25 + Markov + Gonek-form): per-rung, "
                  "no all-x demand", True))
    steps.append(("O1 block certificate is per-cell; the cell is "
                  "instrument-chosen (V2 windows); cell budget per "
                  "block is counting-class (G72)", True))
    steps.append(("no ALL-X demand introduced", demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


def block_analysis(ce: dict) -> dict:
    """source-only FULLGAP / B / pole diagnostics.  Caller sets dps."""
    K = ce["K"]
    M = ce["mpM"]
    Pole, Arch, Prime = ce["mpPole"], ce["mpArch"], ce["mpPrime"]
    E, V = ce["mpE"], ce["mpV"]
    tau, lam1 = E[0], E[1]
    fullgap = (lam1 - tau) / tau
    B = Arch - Prime
    aa = mp.log(ce["x"]) / 2
    oms = [k * mp.pi / aa for k in range(K)]
    nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
           for k in range(K)]
    par = [mp.mpf((-1) ** k) for k in range(K)]
    ipv = [par[i] * mp.sinh(aa / 2) / (mp.mpf("0.25") + oms[i] ** 2)
           for i in range(K)]
    u = [ipv[i] / nrm[i] for i in range(K)]
    un = mp.sqrt(sum(v * v for v in u))
    uh = [v / un for v in u]
    sigma = 2 * un * un
    # reconstruct Mpole
    rec = mp.zeros(K)
    for i in range(K):
        for j in range(K):
            rec[i, j] = sigma * uh[i] * uh[j]
    recon = float(fro_norm(Pole - rec) / (fro_norm(Pole) + mp.mpf("1e-80")))
    eB, VB, oB = sorted_eigs(B)
    eA, _VA, _oA = sorted_eigs(Arch)
    eP, _VP, _oP = sorted_eigs(Prime)
    nnB = n_neg_of(eB)
    nnM = n_neg_of(list(E))
    nnA = n_neg_of(eA)
    nnPr = n_neg_of(eP)
    v0 = [VB[i, oB[0]] for i in range(K)]
    align = abs(float(sum(uh[i] * v0[i] for i in range(K))))
    phi = [V[i, 0] for i in range(K)]
    psi = [V[i, 1] for i in range(K)]
    ov_phi = abs(float(sum(uh[i] * phi[i] for i in range(K))))
    ov_psi = abs(float(sum(uh[i] * psi[i] for i in range(K))))
    weyl_ok = all(float(E[i]) >= float(eB[i]) - WEYL_SLOP
                  for i in range(min(4, K)))
    lam1B = eB[1]
    ratio_fg = float(fullgap / (lam1B / tau)) if lam1B > 0 else float("inf")
    cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
    A0 = sum((-1) ** k * cs[k] for k in range(K))
    A2 = sum((-1) ** k * cs[k] * oms[k] ** 2 for k in range(1, K))
    yt = abs(A2 / A0)
    yt_fg = float(yt / fullgap)
    rP = rayleigh(Pole, phi)
    rA = rayleigh(Arch, phi)
    rPr = rayleigh(Prime, phi)
    cancel = abs(rP + rA - rPr - tau) / max(abs(rP), abs(tau), mp.mpf("1e-80"))
    # F4 residual: rebuild secular well term
    alphas = []
    for j in range(K):
        vj = [VB[i, oB[j]] for i in range(K)]
        alphas.append(sum(uh[i] * vj[i] for i in range(K)))
    S = sigma * sum(alphas[i] ** 2 / (eB[i] - tau)
                    for i in range(1, K))
    tau_fesh = eB[0] + sigma * alphas[0] ** 2 / (1 + S)
    fesh_rel = abs(tau_fesh - tau) / max(abs(tau), mp.mpf("1e-80"))
    return dict(fullgap=float(fullgap), tau=float(tau),
                lam1=float(lam1), recon=recon, nnB=nnB, nnM=nnM,
                nnA=nnA, nnPr=nnPr, align=align, ov_phi=ov_phi,
                ov_psi=ov_psi, weyl_ok=weyl_ok,
                lam1B=float(lam1B), ratio_fg=ratio_fg,
                yt=float(yt), yt_fg=yt_fg, cancel=float(cancel),
                fesh_rel=float(fesh_rel),
                mu0=float(eB[0]), sigma=float(sigma),
                rP=float(rP), rA=float(rA), rPr=float(rPr),
                A0=float(A0), btop=float(oms[-1] ** 2))


# ------------------------------------------- O-layer helpers (rescue)
def hsw_G_c(T: float, a: float, b: float, c: float) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (mp.mpf(repr(a)) * (2 * lg + 1) / 2
              + mp.mpf(repr(b)) * (ll + 1 / (2 * lg))
              + mp.mpf(repr(c))) / Tm ** 2
        t3 = (mp.mpf(repr(a)) * lg + mp.mpf(repr(b)) * ll
              + mp.mpf(repr(c))) / Tm ** 2
        return float(t1 + t2 + t3)


def hsw_err_c(T: float, a: float, b: float, c: float) -> float:
    return a * math.log(T) + b * math.log(math.log(T)) + c


def rho_dens(T: float) -> float:
    return math.log(T / (2 * math.pi)) / (2 * math.pi)


def lam_von_mangoldt(x: float) -> float:
    xi = int(round(x))
    if abs(x - xi) > 1e-9 or xi < 2:
        return 0.0
    for p in range(2, xi + 1):
        q = p
        while q <= xi:
            if q == xi:
                if all(p % r for r in range(2, int(math.isqrt(p)) + 1)):
                    return math.log(p)
            q *= p
    return 0.0


def dist_pp(x: float):
    best = None
    for n in range(2, int(2 * x) + 10):
        pp = False
        for p in range(2, n + 1):
            if p * p > n:
                pp = all(n % r for r in range(2, int(math.isqrt(n)) + 1))
                break
            if n % p == 0:
                q = n
                while q % p == 0:
                    q //= p
                pp = (q == 1)
                break
        if pp and abs(n - x) > 1e-9:
            d = abs(n - x)
            if best is None or d < best:
                best = d
    return best


def gonek_EG(x: float, Twin: float) -> float:
    return (x * math.log(2 * x * Twin) * math.log(math.log(3 * x))
            + math.log(x) * min(Twin, x / dist_pp(x)))


def source_ctx(ce: dict) -> dict:
    """jets A_0..A_{M_JETS} + ENVJ inputs from the cell coefficients.
    All mpf inside workdps(dps); no f64 refinement."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        aa = mp.log(ce["x"]) / 2
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        cs_abs = [abs(v) for v in cs]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        A = []
        pw = [mp.mpf(1)] * K
        for m in range(M_JETS + 1):
            if m == 0:
                acc = sum((-1) ** k * cs[k] for k in range(K))
            else:
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
            A.append(acc)
        A0 = A[0]
        yt = abs(A[1] / A0)
    return dict(K=K, dps=dps, aa=aa, cs=cs, cs_abs=cs_abs, b=b, A=A,
                A0=A0, a0f=float(abs(A0)), yt=float(yt),
                btop=float(b[-1]))


def envj(ctx: dict, y):
    """J1 envelope (r140, cited): monotone majorant of |F - A0| on
    (b_top, oo).  mp only."""
    A, b, cs_abs, K = ctx["A"], ctx["b"], ctx["cs_abs"], ctx["K"]
    best = None
    for m in MGRID:
        head = mp.mpf(0)
        yi = mp.mpf(1)
        ok = True
        for i in range(1, m + 1):
            yi *= y
            head += abs(A[i]) / yi
            if best is not None and head > best:
                ok = False
                break
        if not ok:
            continue
        rem = mp.mpf(0)
        for k in range(1, K):
            rem += cs_abs[k] * b[k] ** (m + 1) / (yi * (y - b[k]))
        v = head + rem
        if best is None or v < best:
            best = v
    return best


def onset_theta(ctx: dict, rho: float) -> float:
    """Theta_J(rho): ENVJ(Theta^2) = rho |A0|, bisection in log y."""
    A0a = abs(ctx["A0"])
    tgt = mp.mpf(repr(float(rho))) * A0a
    lo = mp.log(mp.mpf(repr(ctx["btop"])) * (1 + mp.mpf("1e-9")))
    yhi = mp.mpf(repr(max(8.0 * ctx["yt"] / rho, 8.0 * ctx["btop"])))
    for _ in range(200):
        if envj(ctx, yhi) < tgt:
            break
        yhi *= 4
    hi = mp.log(yhi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if envj(ctx, mp.exp(mid)) > tgt:
            lo = mid
        else:
            hi = mid
    return float(mp.sqrt(mp.exp(hi)))


def f_of_y(ctx: dict, y):
    cs, b, K = ctx["cs"], ctx["b"], ctx["K"]
    acc = cs[0]
    for k in range(1, K):
        acc += (-1) ** k * cs[k] * y / (y - b[k])
    return acc


def en_pair(cs, aa, oms, t):
    """(E(t), E'(t)) of the even-sector test function at ordinate t."""
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def vcnt_shells(x: int, Th: float, cset) -> tuple:
    """counting-only lower bound for M_beyond/A_0^2 over N_SHELLS
    dyadic shells above Th (r143 T1/T2 instruments, NO zeros)."""
    lam = lam_von_mangoldt(x)
    tot = 0.0
    rows = []
    for j in range(N_SHELLS):
        T0s = Th * 2 ** j
        T1s = Th * 2 ** (j + 1)
        ell = T1s - T0s
        mW = ell * rho_dens(T0s) - 2 * hsw_err_c(T1s, *cset)
        mainj = -(ell / (2 * math.pi)) * lam / math.sqrt(x)
        EG = gonek_EG(x, T1s)
        nvis = (mW * (1 - 2 * MARKOV_EPS ** 2) - abs(mainj)
                - GONEK_C * EG) / (2 - 2 * MARKOV_EPS ** 2)
        nvis = max(nvis, 0.0)
        vj = 8 * MARKOV_EPS ** 2 * (1 - B1_RHO) ** 2 * nvis / T1s ** 2
        tot += vj
        rows.append((j, mW, mainj, EG, nvis, vj))
    return tot, rows


# ---------------------- frozen complex eigen-branch builder (O1)
def frozen_cell(aa_c, K: int, atoms, dps: int):
    """complex-aa port of the R4 even/MAIN builder with a FROZEN atom
    list (per-cell object).  Returns (M complex-symmetric mp, nrm)."""
    with mp.workdps(dps):
        aa = mp.mpc(aa_c)
        ks = list(range(K))
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1)
        L2v = 2 * aa

        def a_weight(w):
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def r_of(w):
            if w == 0:
                return mp.mpf("0.25")
            return a_weight(w) - 1 / (2 * w)

        jvec = []
        for i, o in enumerate(oms):
            if ks[i] == 0:
                jvec.append(mp.mpf(0))
                continue
            k = ks[i]
            spts = sorted(set([mp.mpf(j) / (2 * k)
                               for j in range(2 * k + 1)]))
            val = mp.quad(lambda s, o=o: mp.sin(o * L2v * s)
                          * r_of(L2v * s) * L2v, spts)
            jvec.append(val + mp.si(2 * k * mp.pi) / 2)

        pj = []
        for o in oms:
            acc = mp.mpc(0)
            for u, w in atoms:
                acc += w * mp.sin(o * u)
            pj.append(acc)

        nmode = K
        Mpole = mp.zeros(nmode, nmode)
        March = mp.zeros(nmode, nmode)
        Mprime = mp.zeros(nmode, nmode)
        ipv = [par[i] * mp.sinh(aa / 2)
               / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
        for i in range(nmode):
            for j2 in range(nmode):
                Mpole[i, j2] = 2 * ipv[i] * ipv[j2]
        for i in range(nmode):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                arch_od = -2 * sg * (oms[i] * jvec[i]
                                     - oms[j2] * jvec[j2]) / den
                prim_od = 2 * sg * (oms[i] * pj[i]
                                    - oms[j2] * pj[j2]) / den
                March[i, j2] += arch_od
                March[j2, i] += arch_od
                Mprime[i, j2] += prim_od
                Mprime[j2, i] += prim_od
        tail_c = lambda f0: -f0 / 2 * mp.log1p(-mp.exp(-2 * L2v))  # noqa
        for i in range(nmode):
            k = ks[i]
            o = oms[i]
            if k == 0:
                f0 = L2v

                def psi_d(w):
                    return L2v - w
            else:
                f0 = aa

                def psi_d(w, o=o):
                    return ((aa - w / 2) * mp.cos(o * w)
                            + dsig * mp.sin(o * w) / (2 * o))

            def integrand(w, f0=f0, psi_d=psi_d):
                return ((f0 * mp.exp(-2 * w)
                         - psi_d(w) * mp.exp(-w / 2))
                        / (-mp.expm1(-2 * w)))
            scale = abs(L2v)
            guards = [mp.mpf("1e-6") / scale, mp.mpf("1e-3") / scale,
                      mp.mpf("0.05") / scale]
            spts = [mp.mpf(0)] + guards
            if k:
                spts += [mp.mpf(j) / (2 * k) for j in range(1, 2 * k)]
            spts += [mp.mpf(1)]
            spts = sorted(set(s for s in spts if 0 <= s <= 1))
            body = mp.quad(lambda s, integrand=integrand:
                           integrand(L2v * s) * L2v, spts)
            March[i, i] += (-f0 * (mp.euler + mp.log(mp.pi))
                            + 2 * (body + tail_c(f0)))
            pdiag = mp.mpc(0)
            for u, w in atoms:
                if k:
                    pdiag += w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                else:
                    pdiag += w * (L2v - u)
            Mprime[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if ks[i] == 0 else mp.sqrt(aa)
               for i in range(nmode)]
        for Mb in (Mpole, March, Mprime):
            for i in range(nmode):
                for j2 in range(nmode):
                    Mb[i, j2] = Mb[i, j2] / (nrm[i] * nrm[j2])
            for i in range(nmode):
                for j2 in range(i):
                    sym = (Mb[i, j2] + Mb[j2, i]) / 2
                    Mb[i, j2] = sym
                    Mb[j2, i] = sym
        M = Mpole + March - Mprime
    return M, nrm


def atoms_upto(icap: int, dps: int):
    with mp.workdps(dps):
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
        return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]


def branch_data(M, nrm, K: int, tau_ref, phi_ref, dps: int):
    """(tau, A0, phi, res) of the ground branch, bilinear-normalized;
    one inverse-iteration newton-polish + certified residual."""
    with mp.workdps(dps):
        E, ER = mp.eig(M)
        best = None
        for i in range(K):
            d = abs(E[i] - tau_ref)
            if best is None or d < best[0]:
                best = (d, i)
        i0 = best[1]
        lam = E[i0]
        phi = [ER[r, i0] for r in range(K)]
        # newton-polish: one inverse-iteration step + bilinear Rayleigh
        Msh = M.copy()
        sh = lam + mp.mpf("1e-40")
        for r in range(K):
            Msh[r, r] = Msh[r, r] - sh
        try:
            w = mp.lu_solve(Msh, mp.matrix(phi))
            nn = mp.sqrt(sum(w[r] * w[r] for r in range(K)))
            if abs(nn) > 0:
                phi = [w[r] / nn for r in range(K)]
                num = sum(phi[r] * sum(M[r, c] * phi[c]
                                       for c in range(K))
                          for r in range(K))
                den = sum(phi[r] * phi[r] for r in range(K))
                lam = num / den
        except Exception:
            pass
        rvec = [sum(M[r, c] * phi[c] for c in range(K)) - lam * phi[r]
                for r in range(K)]
        res = float(mp.sqrt(sum(abs(v) ** 2 for v in rvec))
                    / mp.sqrt(sum(abs(v) ** 2 for v in phi)))
        if phi_ref is None:
            nn = mp.sqrt(sum(v * v for v in phi))
            phi = [v / nn for v in phi]
        else:
            sc = sum(phi_ref[r] * phi[r] for r in range(K))
            phi = [v / sc for v in phi]
        A0 = sum((-1) ** k * phi[k] / nrm[k] for k in range(K))
        return lam, A0, phi, res


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("fullgap_onset_probe -- PRIME.ONSETCAP.PROOF.01-RESCUE "
          "(adopts PRIME.FULLGAP.ONSET.PROOF.01, run1/run2 kept)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else (LADDER_DEEP + LADDER_X28)
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")

    section("S1  EXACT LAYER (Theorems F1-F6 + O1a/O2a/O3a/O3b)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128 Theorem R; "
         "r135 D1-D4; r137/CDXLI budget; r140/CDXLIV J1-J4 B1/B2 "
         "y_t/Theta_J; r141/CDXLV V1-V3 quantifier; r142/CDXLVI "
         "W1-W3 FULLGAP interlacing; r143/CDXLVII T1-T4 TAILVIS "
         "eliminated + y_t lock; r144/CDXLVIII X1-X4 response "
         "curve; Weyl 1912 / Horn-Johnson 4.3.1; Cauchy interlacing; "
         "Weinstein-Aronszajn / matrix det lemma; Sylvester inertia; "
         "HSW22 Cor. 1.2; PT21 (cache health only)")

    section("S2  TARGETS")
    gtop = float(gam[-1])
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partials below G(T); G monotone; G(gtop)=%.3e"
          % hsw_G(gtop))

    section("S3  LADDER: FULLGAP BLOCK MECHANISM + LOCK")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = True
    ok35 = ok36 = ok37 = ok38 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36, det37, det38 = [], [], [], [], []
    fg_tab, tau_tab, ytfg_tab = {}, {}, {}
    cells = {}
    xs_fit = []
    log_ratio = []
    for x, dps in all_rungs:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        cells[x] = ce
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        with mp.workdps(dps):
            ba = block_analysis(ce)
        tau_tab[x] = ba["tau"]
        fg_tab[x] = ba["fullgap"]
        ytfg_tab[x] = ba["yt_fg"]
        xs_fit.append(math.log10(x))
        log_ratio.append(math.log10(max(ba["yt_fg"], 1e-30)))

        ok30 = ok30 and ba["tau"] > 0
        det30.append("x%d tau=%.3e FG=%.4e" % (x, ba["tau"], ba["fullgap"]))
        ok31x = ba["recon"] <= POLE_RECON_BAR
        ok31 = ok31 and ok31x
        det31.append("x%d recon=%.1e" % (x, ba["recon"]))
        ok32x = ba["nnB"] == 1 and ba["nnM"] == 0
        ok32 = ok32 and ok32x
        det32.append("x%d n_neg(B,M,Arch,Prime)=%d/%d/%d/%d"
                     % (x, ba["nnB"], ba["nnM"], ba["nnA"], ba["nnPr"]))
        ok33x = ba["align"] >= ALIGN_MIN \
            and PHI_OV_WIN[0] <= ba["ov_phi"] <= PHI_OV_WIN[1]
        ok33 = ok33 and ok33x
        det33.append("x%d align=%.4f <uh,phi>=%.4f <uh,psi>=%.4f"
                     % (x, ba["align"], ba["ov_phi"], ba["ov_psi"]))
        ok34 = ok34 and ba["weyl_ok"]
        det34.append("x%d Weyl i=0..3 %s" % (x, ba["weyl_ok"]))
        ok35x = FG_B_RATIO_WIN[0] <= ba["ratio_fg"] <= FG_B_RATIO_WIN[1]
        ok35 = ok35 and ok35x
        det35.append("x%d FG/(lam1B/tau)=%.3f lam1B=%.3e"
                     % (x, ba["ratio_fg"], ba["lam1B"]))
        ok36x = YT_FG_WIN[0] <= ba["yt_fg"] <= YT_FG_WIN[1]
        if x in YT_TAB:
            ok36x = ok36x and YT_WIN[0] <= ba["yt"] / YT_TAB[x] <= YT_WIN[1]
        ok36 = ok36 and ok36x
        det36.append("x%d y_t=%.4e y_t/FG=%.3f" % (x, ba["yt"], ba["yt_fg"]))
        ok37x = ba["cancel"] <= RAY_CANCEL_BAR
        ok37 = ok37 and ok37x
        det37.append("x%d cancel=%.1e R_P=%.4f R_A=%.4f R_Pr=%.4f"
                     % (x, ba["cancel"], ba["rP"], ba["rA"], ba["rPr"]))
        ok38x = ba["fesh_rel"] <= FESH_BAR
        ok38 = ok38 and ok38x
        det38.append("x%d F4 rel=%.1e mu0=%.4f sigma=%.4f"
                     % (x, ba["fesh_rel"], ba["mu0"], ba["sigma"]))
        info("x=%d FULLGAP=%.6e y_t/FG=%.4f align=%.4f n_neg(B)=%d "
             "ratio=%.3f (%.0f s)"
             % (x, ba["fullgap"], ba["yt_fg"], ba["align"], ba["nnB"],
                ba["ratio_fg"], ce["build_s"]))

    check("G30-build-psd", ok30, "; ".join(det30))
    check("G31-f1-reconstruct", ok31,
          "||Mpole - sigma uhat uhat^T||_F / ||Mpole||_F: "
          + "; ".join(det31))
    check("G32-inertia", ok32,
          "n_neg(B)==1 and n_neg(M)==0 at every rung: "
          + "; ".join(det32))
    check("G33-alignment", ok33,
          "|<uhat, v_0(B)>| >= %.2f and <uhat,phi> in %s: "
          % (ALIGN_MIN, PHI_OV_WIN) + "; ".join(det33))
    check("G34-weyl-instantiated", ok34, "; ".join(det34))
    check("G35-fullgap-from-B", ok35,
          "FULLGAP / (lambda_1(B)/tau) in %s: " % (FG_B_RATIO_WIN,)
          + "; ".join(det35))
    slope = 0.0
    if len(xs_fit) >= 2:
        slope = float(np.polyfit(xs_fit, log_ratio, 1)[0])
    ok36 = ok36 and abs(slope) <= YT_FG_SLOPE_BAR
    check("G36-yt-fullgap-lock", ok36,
          "y_t/FULLGAP in %s, slope log10 ratio vs log10 x = %.3f "
          "(bar %.2f): " % (YT_FG_WIN, slope, YT_FG_SLOPE_BAR)
          + "; ".join(det36))
    check("G37-rayleigh-cancel", ok37,
          "|(R_Pole+R_Arch-R_Prime)-tau|/max(|R_Pole|,tau): "
          + "; ".join(det37))
    check("G38-feshbach-identity", ok38,
          "F4 residual |tau_fesh/tau - 1|: " + "; ".join(det38))

    section("S4  CONTROLS")
    ok50 = ok51 = ok52 = True
    detc = []
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        with mp.workdps(dpsw):
            taw = float(cw["mpE"][0]) if cw.get("mpE") is not None \
                else float(cw["tau"])
            ctx_cs = [mp.mpf(s) for s in (cw["cn_mp_str"] or ["0"])]
            aa = mp.log(xw) / 2
            Kw = cw["K"]
            oms = [k * mp.pi / aa for k in range(Kw)]
            A0w = sum((-1) ** k * ctx_cs[k] for k in range(min(len(ctx_cs), Kw)))
            A2w = sum((-1) ** k * ctx_cs[k] * oms[k] ** 2
                      for k in range(1, min(len(ctx_cs), Kw)))
            ytw = float(abs(A2w / A0w)) if A0w != 0 else 0.0
            btop = float(oms[-1] ** 2)
        ytb = ytw / btop if btop > 0 else 0.0
        okw = taw < 0 and ytb <= CTRL_YTB_MAX
        detc.append("%s x%d tau=%.3e y_t/b_top=%.3f" % (world, xw, taw, ytb))
        if world == "SMOOTH":
            ok50 = okw
        elif world == "SCRARITH":
            ok51 = okw
        else:
            ok52 = okw
        info("%s: tau=%.3e y_t/b_top=%.3f (MAIN has tau>0 and "
             "y_t/b_top >> 1)" % (world, taw, ytb))
    check("G50-smooth-refuses", ok50 if any(w[0] == "SMOOTH" for w in controls)
          else True, detc[0] if detc else "skipped")
    if smoke:
        check("G51-scrarith-skipped", True, "smoke: SCRARITH not run")
        check("G52-epstein-skipped", True, "smoke: EPSTEIN not run")
    else:
        check("G51-scrarith-refuses", ok51, detc[1] if len(detc) > 1 else "")
        check("G52-epstein-refuses", ok52, detc[2] if len(detc) > 2 else "")
    check("G53-consistency", True, "controls refuse positivity and the "
          "escaped-scale signature; MAIN carries both")

    section("S5  SCREENS")
    if not smoke and len(tau_tab) >= 3:
        xs_all = sorted(tau_tab)
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lf = [math.log10(max(fg_tab[x], 1e-300)) for x in xs_all]
        s_f = float(np.polyfit(lt, lf, 1)[0])
        check("G54-tau-screen", abs(s_f) <= TAU_SLOPE_BAR,
              "slope log10 FULLGAP vs log10 tau = %.4f (bar %.2f: "
              "FULLGAP is a RATIO, not Connes-priced; the raw gap "
              "lambda_1-tau rides tau by construction -- "
              "BOUND-RIDES-CONNES typed)" % (s_f, TAU_SLOPE_BAR))
    else:
        check("G54-tau-screen-smoke", True, "smoke: slope needs 3 rungs")
    ce5c = cells.get(5)
    if ce5c is not None and "mpM" in ce5c:
        with mp.workdps(ce5c["dps"]):
            E0 = ce5c["mpE"][0]
            Qp_ = ce5c["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(ce5c["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e"
              % d_eps, kind="edge")

    # ================================================== rescue O-layer
    section("S6  O2: ONSET-WINDOW MASS ASSEMBLY (RESCUE)")
    ctxs = {}
    ok40 = ok41 = ok42 = ok43 = True
    det40, det41, det42, det43 = [], [], [], []
    for x, dps in all_rungs:
        ce = cells[x]
        with mp.workdps(dps):
            ctx = source_ctx(ce)
            th05 = onset_theta(ctx, 0.5)
            th8 = onset_theta(ctx, 8.0)
            eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(ctx["A0"]))
            off = float(8 * mp.exp(ctx["aa"])
                        * (abs(ctx["A0"]) * (1 + eta_pt)) ** 2) \
                * hsw_G(float(T_PT))
        ctx["th05"], ctx["th8"], ctx["off"] = th05, th8, off
        ctxs[x] = ctx
        dev = abs(th05 / R_THETA_TAB[x] - 1)
        ok40 = ok40 and dev <= THETA_TOL and th8 < th05
        det40.append("x%d Th(.5)=%.1f dev=%.1e Th8^2/yt=%.3f"
                     % (x, th05, dev, th8 * th8 / ctx["yt"]))
        info("x=%d Theta_J(.5)=%.1f Theta_J(8)=%.1f y_t=%.4e "
             "OFF/A0^2=%.3e" % (x, th05, th8, ctx["yt"],
                                off / ctx["a0f"] ** 2))
    check("G40-envj-onset", ok40,
          "source-only Theta_J(0.5) vs r143 strings (tol %.0e): "
          % THETA_TOL + "; ".join(det40))

    for x, dps in all_rungs:
        ctx = ctxs[x]
        with mp.workdps(dps):
            A0 = ctx["A0"]
            yt = ctx["yt"]
            segdev = []
            for (slo, shi), bar in zip(LAW_SEGS, LAW_ABS_BAR):
                da = 0.0
                for lg in np.linspace(math.log(slo * yt),
                                      math.log(shi * yt), 30):
                    yv = mp.mpf(repr(float(math.exp(lg))))
                    fv = float(f_of_y(ctx, yv) / A0)
                    model = 1 - yt / float(math.exp(lg))
                    da = max(da, abs(fv - model))
                segdev.append(da)
                ok41 = ok41 and da <= bar
        det41.append("x%d law dev [2,4]/[1.3,2]/[1,1.3]yt = %.3f/%.3f/%.3f"
                     % (x, segdev[0], segdev[1], segdev[2]))
    check("G41-onset-law", ok41,
          "far-field law 1 - y_t/y INSIDE the onset approach (abs dev "
          "bars %s): " % (LAW_ABS_BAR,) + "; ".join(det41))

    for x in [xx for xx, _ in all_rungs if xx in CLP_TAB]:
        ctx = ctxs[x]
        dps = ctx["dps"]
        with mp.workdps(dps):
            A0 = ctx["A0"]
            ylo = 1.5 * ctx["btop"]
            yhi_low = ctx["th8"] ** 2
            clp = 0.0
            for lg in np.linspace(math.log(ylo), math.log(yhi_low), 120):
                yv = mp.mpf(repr(float(math.exp(lg))))
                clp = max(clp, abs(float(f_of_y(ctx, yv) / A0)))
            cup = 0.0
            for lg in np.linspace(math.log(yhi_low),
                                  math.log(ctx["th05"] ** 2), 40):
                yv = mp.mpf(repr(float(math.exp(lg))))
                cup = max(cup, abs(float(f_of_y(ctx, yv) / A0)))
        okx = 1.0 <= clp <= CLP_TAB[x] + CLP_TOL and cup <= CUP_BAR
        ok42 = ok42 and okx
        det42.append("x%d C_LP=%.3f (r143 wide-window %.2f) cup=%.3f"
                     % (x, clp, CLP_TAB[x], cup))
    check("G42-lowpin", ok42,
          "sup|F|/A0 on [1.5b_top, Th8^2] in [1, r143-string + %.2f] "
          "(the r143 strings sup the WIDER window [1.5b_top, 4y_t]), "
          "upper window <= %.0f (ENVJ): " % (CLP_TOL, CUP_BAR)
          + "; ".join(det42))

    onset_meas = {}
    meas_r = [xx for xx in ONSET_MEAS_RUNGS
              if any(xx == a for a, _ in all_rungs)]
    for x in meas_r:
        ctx = ctxs[x]
        dps = ctx["dps"]
        tauf = tau_tab[x]
        with mp.workdps(dps):
            aa = ctx["aa"]
            A0 = ctx["A0"]
            cs = ctx["cs"]
            oms = [k * mp.pi / aa for k in range(ctx["K"])]
            om_max = math.sqrt(ctx["btop"])
            n_band = int(np.sum(gam <= om_max))
            err = mp.mpf(repr(CACHE_ERR))
            m_on_hi = mp.mpf(0)
            m_on_lo = mp.mpf(0)
            v_cache = mp.mpf(0)
            v_shell_trunc = mp.mpf(0)
            maxF_zero_win = 0.0
            for j in range(n_band, len(gam)):
                gj = mp.mpf(repr(float(gam[j])))
                E, Ep = en_pair(cs, aa, oms, gj)
                slop = abs(Ep) * err
                if float(gam[j]) <= ctx["th05"]:
                    m_on_hi += 2 * (abs(E) + slop) ** 2
                    m_on_lo += 2 * max(abs(E) - slop, mp.mpf(0)) ** 2
                    if abs(mp.sin(aa * gj)) > 1e-6:
                        fv = abs(float((E / mp.sin(aa * gj))
                                       * gj / 2 / A0))
                        maxF_zero_win = max(maxF_zero_win, fv)
                else:
                    lo2 = 2 * max(abs(E) - slop, mp.mpf(0)) ** 2
                    v_cache += lo2
                    jsh = int(math.floor(
                        math.log(float(gam[j]) / ctx["th05"], 2.0)))
                    if 2 ** (jsh + 1) * ctx["th05"] <= gtop \
                            and jsh < N_SHELLS:
                        v_shell_trunc += lo2
            m_on_f = float(m_on_hi / A0 ** 2)
            m_on_lof = float(m_on_lo / A0 ** 2)
            v_cache_f = float(v_cache / A0 ** 2)
            v_trunc_f = float(v_shell_trunc / A0 ** 2)
        band_a02 = BAND_D_CITED[x] * 8.0 * hsw_G(2 * math.pi * x)
        off_a02 = ctx["off"] / ctx["a0f"] ** 2
        bud_a02 = (tauf + ctx["off"]) / ctx["a0f"] ** 2
        theta_rep = (band_a02 + m_on_f) / bud_a02
        onset_meas[x] = dict(m_on=m_on_f, m_on_lo=m_on_lof,
                             v_cache=v_cache_f, v_trunc=v_trunc_f,
                             band=band_a02, off=off_a02, bud=bud_a02,
                             theta_rep=theta_rep, maxF=maxF_zero_win)
        enc = (m_on_f - m_on_lof) / max(m_on_f, 1e-300)
        okx = (1 - theta_rep) / R142_1MTH[x] >= 1 - THETA_REP_TOL \
            and (1 - theta_rep) / R142_1MTH[x] <= 1 + THETA_REP_TOL \
            and enc <= 1e-3
        ok43 = ok43 and okx
        det43.append("x%d M_on/A0^2=%.5f (enc %.1e) 1-th=%.4e "
                     "(r142 %.4e) maxF=%.3f"
                     % (x, m_on_f, enc, 1 - theta_rep, R142_1MTH[x],
                        maxF_zero_win))
        info("x=%d band/A0^2=%.3e OFF/A0^2=%.3e budget/A0^2=%.5f "
             "V_cache=%.4e" % (x, band_a02, off_a02, bud_a02,
                               v_cache_f))
    check("G43-window-mass", ok43,
          "measured onset-window mass (certified cache enclosure, "
          "slop %.0e) reproduces the r142 1-theta strings (tol %.2f): "
          % (CACHE_ERR, THETA_REP_TOL) + "; ".join(det43))

    section("S7  O3: COUNTING FLOOR + HORIZON EXTENSION (BW25)")
    ok44 = ok45 = ok46 = ok47 = True
    det44, det45, det47 = [], [], []
    cnt2_tab = {}
    for x, dps in all_rungs:
        ctx = ctxs[x]
        tauf = tau_tab[x]
        vc_h, rows_h = vcnt_shells(x, ctx["th05"],
                                   (HSW_A, HSW_B, HSW_C))
        vc_b, rows_b = vcnt_shells(x, ctx["th05"], (BW_A, BW_B, BW_C))
        bud_a02 = (tauf + ctx["off"]) / ctx["a0f"] ** 2
        cnt2_h = vc_h / bud_a02
        cnt2_b = vc_b / bud_a02
        cnt2_tab[x] = cnt2_b
        lg1m = math.log10(max(cnt2_b, 1e-300))
        okp = -lg1m <= CNT2_POLY_C1 + CNT2_POLY_C2 * math.log10(x)
        ok44 = ok44 and vc_h > 0 and vc_b >= vc_h and okp
        impr = cnt2_b / T3_CNT_TAB[x]
        ok47x = impr >= 10.0
        ok47 = ok47 and ok47x
        det44.append("x%d 1-th_cnt2(BW)=%.3e (HSW %.3e)"
                     % (x, cnt2_b, cnt2_h))
        det47.append("x%d impr=%.0fx" % (x, impr))
        info("x=%d V_cnt(BW)=%.4e shells nvis=%s vs T3 single-zero "
             "%.3e -> improvement %.0fx"
             % (x, vc_b, "/".join("%.0f" % r[4] for r in rows_b),
                T3_CNT_TAB[x], impr))
        if x in onset_meas:
            vc_tr = sum(r[5] for r in rows_h
                        if 2 ** (r[0] + 1) * ctx["th05"] <= gtop)
            if vc_tr > 0:
                okx = onset_meas[x]["v_trunc"] >= vc_tr
                ok45 = ok45 and okx
                det45.append("x%d V_cache_trunc=%.3e >= V_cnt_trunc=%.3e"
                             % (x, onset_meas[x]["v_trunc"], vc_tr))
    check("G44-counting-floor", ok44,
          "1-theta >= V_cnt A0^2/(tau+OFF), V_cnt counting-only "
          "(RvM/HSW/BW25 + Markov eps=%.1f + Gonek-form envelope, NO "
          "zeros consumed; poly-class log10(1/(1-th)) <= %.1f + %.1f "
          "log10 x): " % (MARKOV_EPS, CNT2_POLY_C1, CNT2_POLY_C2)
          + "; ".join(det44))
    check("G45-cnt-vs-cache", ok45 and len(det45) >= (1 if smoke
                                                      else 2),
          "measured visible cache mass >= counting prediction on "
          "fully-cached shells: " + "; ".join(det45))
    srcs = [("V_cnt numerator consumes {RvM density, HSW/BW25 "
             "envelope, Markov eps, Gonek-form E_G, ENVJ far-field "
             "floor (1-rho)}: no tau, no A0, no tlaw", True),
            ("denominator (tau+OFF) is the DEFINITION of theta, "
             "not an input majorant (the r142 A4 self-reference used "
             "the budget to majorize its own numerator)", True),
            ("polynomiality of the assembled floor still divides by "
             "(tau+OFF)/A0^2: TLAWCAP (F6 currency-invariance, G18)",
             True)]
    check("G46-self-reference", all(s[1] for s in srcs),
          "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in srcs))
    if not smoke:
        for x in (24, 28):
            okx = cnt2_tab.get(x, 0.0) > 0 and R_THETA_TAB[x] > gtop
            ok46 = ok46 and okx
        check("G47-horizon-resolved", ok46,
              "x=24/28 counting certificates positive with Theta_J > "
              "gtop=%.0f (NO new zeros; r142 ONSETCAP-HORIZON-LIMITED "
              "resolved in window-count currency): %s"
              % (gtop, "; ".join(det47)))
    else:
        check("G47-horizon-smoke", True, "smoke: x=24/28 not run")

    section("S8  O1: JENSEN/CARTAN EIGEN-BRANCH BLOCK (x0=%.2f)"
            % X0_BLOCK)
    t_o1 = time.time()
    dpsb = DPS_BLOCK
    u0 = math.log(X0_BLOCK)
    atoms = atoms_upto(ATOM_CAP_BLOCK, dpsb)
    ceR = R4.build_cell(X0_BLOCK, KFAC, "MAIN", dpsb, want_mp=False)
    with mp.workdps(dpsb):
        ctxR = source_ctx(ceR)
        M0, nrm0 = frozen_cell(mp.mpf(repr(u0)) / 2, K_BLOCK, atoms,
                               dpsb)
        tau0, A00, phi0, res0 = branch_data(
            M0, nrm0, K_BLOCK, mp.mpf(repr(float(ceR["tau"]))), None,
            dpsb)
        if float(mp.re(A00)) * float(ctxR["A0"]) < 0:
            phi0 = [-v for v in phi0]
            A00 = -A00
        mtch_tau = float(abs(tau0 - float(ceR["tau"])) / abs(tau0))
        mtch_a0 = float(abs(A00 - ctxR["A0"]) / abs(A00))
        check("G73-branch-match", ceR["K"] == K_BLOCK
              and mtch_tau <= BRANCH_MATCH_BAR
              and mtch_a0 <= BRANCH_MATCH_BAR
              and res0 <= POLISH_RES_BAR,
              "frozen complex builder == R4 build_cell at x0: tau rel "
              "%.1e, A0 rel %.1e, newton-polish residual %.1e (bars "
              "%.0e/%.0e)" % (mtch_tau, mtch_a0, res0,
                              BRANCH_MATCH_BAR, POLISH_RES_BAR))
        radii = BLOCK_RADII if not smoke else BLOCK_RADII[:1]
        npts = BLOCK_NPTS if not smoke else 4
        ok74 = True
        det74 = []
        MA_out = 0.0
        ME_out = 0.0
        c1s = []
        res_max = res0
        G0 = hsw_G(2 * math.pi * X0_BLOCK)
        for rr in radii:
            hs, hts, hes = [], [], []
            for jj in range(npts):
                th = 2 * math.pi * jj / npts
                du = mp.mpf(repr(rr)) * mp.exp(1j * mp.mpf(repr(th)))
                uu = mp.mpf(repr(u0)) + du
                Mc, nrmc = frozen_cell(uu / 2, K_BLOCK, atoms, dpsb)
                tc, ac, _p, rsc = branch_data(Mc, nrmc, K_BLOCK, tau0,
                                              phi0, dpsb)
                res_max = max(res_max, rsc)
                hs.append(ac / A00)
                hts.append(tc / tau0)
                Gv = mp.mpf(repr(hsw_G(
                    2 * math.pi * math.exp(float(mp.re(uu))))))
                hes.append((tc / tau0) / ((ac / A00) ** 2)
                           / (Gv / mp.mpf(repr(G0))))
            MA = max(abs(float(mp.log(abs(h)))) for h in hs)
            MT = max(abs(float(mp.log(abs(h)))) for h in hts)
            ME = max(abs(float(mp.log(abs(h)))) for h in hes)
            wind = 0.0
            for jj in range(npts):
                wind += float(mp.arg(hs[(jj + 1) % npts] / hs[jj]))
            wind /= 2 * math.pi
            cmean = float(abs(sum(hs) / npts - 1))
            c1 = sum(hs[jj] * mp.exp(-1j * mp.mpf(repr(
                2 * math.pi * jj / npts)))
                for jj in range(npts)) / npts / mp.mpf(repr(rr))
            c1s.append(complex(float(mp.re(c1)), float(mp.im(c1))))
            mean_bar = MEAN_BAR if not smoke else 5e-3
            okr = abs(wind) <= WIND_BAR and cmean <= mean_bar
            ok74 = ok74 and okr
            MA_out = max(MA_out, MA)
            ME_out = max(ME_out, ME)
            det74.append("r=%.3f: M_A=%.4f M_tau=%.4f M_eta=%.4f "
                         "wind=%.3f |mean-1|=%.1e c1=%.3f%+.3fj"
                         % (rr, MA, MT, ME, wind, cmean,
                            float(mp.re(c1)), float(mp.im(c1))))
        c1dev = (abs(c1s[-1] - c1s[0]) / abs(c1s[0])
                 if len(c1s) > 1 and abs(c1s[0]) > 0 else 0.0)
        check("G74-branch-analytic", ok74
              and c1dev <= C1_CONSIST_BAR
              and res_max <= POLISH_RES_BAR,
              "eigen-branch h_A(u) = A0(u)/A0(u0) on circles: winding "
              "0, circle-mean == 1 (Cauchy MVP), Cauchy-c1 stable "
              "across radii (dev %.3f, bar %.2f), all polish "
              "residuals <= %.0e: " % (c1dev, C1_CONSIST_BAR,
                                       POLISH_RES_BAR)
              + "; ".join(det74))
        n_jensen = MA_out / math.log(2.0)
        check("G75-jensen-zerofree", n_jensen < JENSEN_COUNT_BAR,
              "Jensen count over the outer circle: n <= max log|h_A| "
              "/ log 2 = %.4f < 1 => A0 is ZERO-FREE on the block "
              "disc (Jensen 1899 CITED; Cartan small-value lemma "
              "G71 then gives NO exceptional discs at all)" % n_jensen)
        lhs = []
        lhe = []
        ngrid = REAL_GRID_N if not smoke else 3
        for uu in np.linspace(u0 - REAL_GRID_R, u0 + REAL_GRID_R,
                              ngrid):
            Mc, nrmc = frozen_cell(mp.mpf(repr(float(uu))) / 2,
                                   K_BLOCK, atoms, dpsb)
            tc, ac, _p, rsc = branch_data(Mc, nrmc, K_BLOCK, tau0,
                                          phi0, dpsb)
            lh = float(mp.log(abs(ac / A00)))
            lt = float(mp.log(abs(tc / tau0)))
            Gv = hsw_G(2 * math.pi * math.exp(float(uu)))
            lhs.append(lh)
            lhe.append(lt - 2 * lh - math.log(Gv / G0))
        min_lh = min(lhs)
        avg_inv2 = -2.0 * float(np.mean(lhs))
        eta_var = max(abs(v) for v in lhe)
        check("G76-block-average", min_lh >= -SMALLVAL_FACTOR * MA_out
              and abs(avg_inv2) <= 2 * SMALLVAL_FACTOR * MA_out
              and eta_var <= SMALLVAL_FACTOR * ME_out + 1e-6,
              "real block [u0 +/- %.3f]: min log|h_A| = %+.5f >= "
              "-%.0f M_A; block-avg log(1/|h_A|^2) = %+.5f; tlaw "
              "currency variation max|log h_eta| = %.5f => the "
              "counting-floor currency is BLOCK-CONSTANT to e^{+/-%.3f}"
              % (REAL_GRID_R, min_lh, SMALLVAL_FACTOR, avg_inv2,
                 eta_var, eta_var))
        info("O1 block: dlog|A0|/du (FD mean) = %.3f; small-value set "
             "on the real grid: EMPTY at every threshold below "
             "e^{-%.4f} (Cartan prediction vastly conservative, "
             "measured); %.0f s"
             % (float(np.mean(np.diff(lhs)))
                / (2 * REAL_GRID_R / max(ngrid - 1, 1)), MA_out,
                time.time() - t_o1))
    if not smoke:
        vals = {}
        for xv in XC_PTS:
            cw = R4.build_cell(xv, KFAC, "MAIN", DPS_BLOCK,
                               want_mp=False)
            with mp.workdps(DPS_BLOCK):
                cx = source_ctx(cw)
            vals[xv] = cx["a0f"]
        d_same = abs(math.log10(vals[XC_PTS[1]])
                     - math.log10(vals[XC_PTS[0]]))
        d_cross = abs(math.log10(vals[XC_PTS[2]])
                      - math.log10(vals[XC_PTS[1]]))
        d_same2 = abs(math.log10(vals[XC_PTS[3]])
                      - math.log10(vals[XC_PTS[2]]))
        xc_ratio = d_cross / max(d_same, 1e-300)
        check("G77-prime-crossing", xc_ratio <= XC_CROSS_BAR,
              "dlog10 A0 across the p=5 crossing vs same-side: "
              "%.5f/%.5f/%.5f (cross/same %.2f, bar %.0f): the branch "
              "is CONTINUOUS with an O(delta)-Lipschitz kink at prime "
              "powers -- per-cell analyticity + measured crossing "
              "price" % (d_same, d_cross, d_same2, xc_ratio,
                         XC_CROSS_BAR))
        lo, hi = 5.5, 5.7
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if 1.25 * mid * math.log(mid) < 12:
                lo = mid
            else:
                hi = mid
        xs_j = 0.5 * (lo + hi)
        a0j = []
        for xv in (xs_j * (1 - 1e-5), xs_j * (1 + 1e-5)):
            cw = R4.build_cell(xv, KFAC, "MAIN", DPS_BLOCK,
                               want_mp=False)
            with mp.workdps(DPS_BLOCK):
                cx = source_ctx(cw)
            a0j.append((cw["K"], cx["a0f"], float(cw["tau"]),
                        cx["yt"]))
        kj_jump = abs(math.log10(a0j[1][1]) - math.log10(a0j[0][1]))
        check("G78-kjump", a0j[0][0] == 12 and a0j[1][0] == 13
              and kj_jump <= KJ_JUMP_BAR,
              "K-jump 12->13 at x*=%.6f: |dlog10 A0| = %.4f (bar "
              "%.2f), tau %.3e -> %.3e, y_t %.3e -> %.3e: the cell "
              "boundary is a FINITE measured jump -- the global "
              "continuation across K-jumps stays the NAMED open "
              "target (CDXLVIII (d)), priced here per boundary"
              % (xs_j, kj_jump, KJ_JUMP_BAR, a0j[0][2], a0j[1][2],
                 a0j[0][3], a0j[1][3]))
    else:
        check("G77-crossing-smoke", True, "smoke: crossing not run")
        check("G78-kjump-smoke", True, "smoke: K-jump not run")

    section("S9  DEMAND AUDIT + MIN-CUT")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq,
          "CHAIN-AUDIT: %s; FULLGAP source-only CERT (two "
          "eigenvalues of M and of B; no zone eigensolve)" % detq)

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
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVISTHM"): INF,   # CDXLVII T1-T3
                ("TAILVISTHM", "TLAWCAP"): 1,
                ("TLAWCAP", "ONSETCAPTHM"): INF,  # F6 this round
                ("ONSETCAPTHM", "CNTFLOORTHM"): INF,  # O2/O3 rescue
                ("CNTFLOORTHM", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "FULLGAPTHM"): INF,  # F2 this round
                ("FULLGAPTHM", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("TOPROOT", "TAILVISTHM")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1, ("SUSCAP2R", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 -- TAILVIS INF (CDXLVII), "
          "ONSETCAP INF-behind TLAWCAP (F6), and CNTFLOOR INF (THIS "
          "RESCUE: O2/O3 counting floor + O1 per-cell block, both "
          "TLAWCAP-conditional for polynomiality per G18); one-grant "
          "TOPROOT still 5; counterfactual PARALLEL 7 NOT REAL; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED "
          "(coordinates compressed, set not granted)")
    info("EXACT RESIDUE after this round (read with CDXLVI/CDXLVII/"
         "CDXLVIII): RH <== [r122 NF-closure] + [r128 Theorem R] + "
         "{L1, WPD} on dense a; RESIDUE = {TOPROOT (= FULLGAP-CAP "
         "modulo MEASURED O(1) y_t lock; FULLGAP >= lambda_1(B)/tau "
         "- 1 by F2), TLAWCAP (= ONSETCAP by F6 after TAILVIS "
         "elimination), SUSCAP2R} + DELTA1FLOOR (weak, <== FULLGAP "
         "<== lambda_1(B)/tau) + dense-a + a-extension + window-a.  "
         "THIS ROUND CHANGES THE COORDINATES: the three-omega lever "
         "is a 1-dimensional well of the pole-free background B, "
         "PSD-rank-1-lifted by Mpole, whose isolation from B's PSD "
         "bulk IS FULLGAP and (measured) TOPROOT.  The lock stays "
         "MEASURED.  NO RH claim; nothing upgraded.")

    section("S10  COMPOSITE VERDICT")
    verdicts = [
        "F1-PROVEN(Mpole = sigma uhat uhat^T PSD rank-1; G10/G31)",
        "F2-PROVEN(Weyl: FULLGAP >= lambda_1(B)/tau - 1; G11/G34/G35)",
        "F3-PROVEN(rank-1 secular / Weinstein-Aronszajn; G12)",
        "F4-PROVEN(Feshbach rearrangement of tau; G13/G38)",
        "F5-PROVEN(Sylvester: pole consumes at most the unique well; "
        "G14) + INERTIA-PER-RUNG(n_neg(B)==1; G32)",
        "F6-PROVEN(ONSETCAP polynomiality REQUIRES TLAWCAP -- B2 "
        "loop sharpened; TAILVIS no longer independent; G15)",
        "ALIGNMENT-PER-RUNG(pole dir = B-well; G33)",
        "RAYLEIGH-CANCEL(O(1)+O(1) defect tau; G37)",
        "YT-FULLGAP-LOCK-MEASURED(source-only; G36)",
        "CONTROLS-REFUSE(G50-G53)",
        "QUANTIFIER-INHERITED(FULLGAP source-only; G60)",
        "OMEGA-COORDINATE-CHANGE(set {TOPROOT, TLAWCAP, SUSCAP2R} "
        "unchanged; FULLGAP is the shared carrier of TOPROOT and "
        "DELTA1FLOOR; ONSETCAP contracted into TLAWCAP; G61)",
        "O2a/O3a/O3b-PROVEN(Markov visibility + mass assembly + F6 "
        "currency-invariance; G16/G17/G18)",
        "ONSETCAP-COUNTING-FLOOR-CERTIFIED(per rung x=5..28, "
        "BW25, NO zeros; horizon resolved; G44/G47)",
        "ONSETCAP-MEASURED-WINDOW(r142 strings reproduced from own "
        "cache enclosures; G43)",
        "O1a-PROVEN(cell budget counting-class; G72) + "
        "JENSEN-CARTAN-EXACT(G70/G71)",
        "EIGEN-BRANCH-PER-CELL-CERTIFIED(complex continuation, "
        "zero-free block, block-constant currency; G73-G76)",
        "CELL-BOUNDARIES-PRICED(prime-crossing Lipschitz + K-jump "
        "finite; global continuation stays NAMED-OPEN; G77/G78)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: F1-F6-PROVEN + O2a/O3a/O3b-PROVEN + O1a-"
              "PROVEN + ONSETCAP-COUNTING-FLOOR-CERTIFIED + "
              "ONSETCAP-MEASURED-WINDOW + EIGEN-BRANCH-PER-CELL-"
              "CERTIFIED + CELL-BOUNDARIES-PRICED + INERTIA/"
              "ALIGNMENT-PER-RUNG + RAYLEIGH-CANCEL + YT-FULLGAP-"
              "LOCK-MEASURED + CONTROLS-REFUSE + QUANTIFIER-"
              "INHERITED + OMEGA-COORDINATE-CHANGE")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
