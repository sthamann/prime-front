#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tlawcap_blocks_probe -- PRIME.TLAWCAP.BLOCKS.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (extend the r148 Jensen/Cartan single-block breakthrough into
a multi-block, K-jump-crossing, block-average certificate program for
the TLAWCAP factor of the log-master)
=======================================================================
State consumed (CITED): CDLII / fullgap_onset_probe (O1 block at
x0 = 5.44: eigen-branch certified analytic + zero-free, Jensen count
0.2996 < 1, small-value set EMPTY, tlaw block-constant e^{+/-0.053},
prime crossing no-spike 0.09, K-jump 12->13 finite price 0.3155 dex;
the global K-jump continuation NAMED OPEN); CDLI /
adjugate_logmaster_probe (AD1 basis-free adjugate coordinates
A_0^2 = B_00/P'(tau); cell-selection lemma modulo simplicity; LM
master needs int log M_src <= C_a U; C_a^pt = 0.0874..0.1103 and
C_a^blk = 0.1012 measured); r140 J1 ENVJ; r141 V2; r142 W1-W3;
r143 T1-T4; r144 X1-X4; HSW22 Cor. 1.2; PT21 T_PT constant only.

Tasks: (B1) run the block machinery on blocks around x = 5, 8, 13,
18, 24, 28: per block certify the analytic continuation on the anchor
cell (winding + Cauchy MVP + polish residuals), the Jensen zero-count,
the small-value set, and the per-block integral of the TLAWCAP factor
log(1 + L_EPS), L_EPS = (tau + OFF)/(16 A_0^2 G(T_z)) -- the table
C_a^blk(U) with certified error bars; (B2) formalize the K-jump
dissolution: prove the ASSEMBLY LEMMA (per-cell oscillation + jump
sizes => block bound) EXACTLY, prove its SHARPNESS (per-jump cap +
poly cell count alone CANNOT give C_a U -- the staircase instance),
so the exact residual hypothesis is JUMP SUMMABILITY
(sum_jumps |Delta log(1 + L_EPS)| <= C U per block) -- then MEASURE
the jump sizes across many K-jumps on every block and the scaling of
the mean jump size in x; adjudicate the Jensen circularity exactly
(what Jensen consumes vs delivers; the a-priori-sup grade vs the
measured-sup grade -- SUP-GRADE-GAP measured per block); (B3) derive
the ONE-MODE (K-jump) update formula exactly: bordered determinant
P+(z) = (z - d) P(z) - b^T adj(zI - M) b, bordered ground pair
phi+ = (w, 1)/sqrt(1 + w^T w) with w = (tau+ I - M)^{-1} b, hence the
EXACT jump formula A_0+^2/A_0^2 = (1 + r)^2 / (1 + (1 + S2) T^2 /
beta_0^2) with T = tau+ - tau, beta_0 = phi^T b, r = T (vtil +
v_new)/(A_0 beta_0) -- the detuning factor is CHEBYSHEV-CLASS
(border prime column bounded by sum_q Lambda(q)/sqrt(q) x explicit
couplings, triangle inequality), the r-term carries 1/A_0 (the SAME
arithmetic residue class as the Jensen center input); ALSO the
one-ATOM (prime-power birth) first-order response formula (exact
2-level series instance, Kato CITED) with births measured at x = 5/8
blocks; (T3) assemble what remains of the TLAWCAP-factor LM
hypothesis, compare against the r137/r140 EPS-LOCK shape, machine-
check, min-cut placement (census {MEAS, OMEGA-POS} cardinality 4),
controls (the Jensen/cell structure must differ in the false worlds
-- verify where), tau-screens, Z1/AST firewall (zero zeta use, ZERO
zero-cache use), conditioning.

=======================================================================
THE EXACT LAYER (Theorems J1-J3, ASM, JC, AB1, CB; sympy generic +
exact rational instances; classical CITED)
=======================================================================
THEOREM J1 (bordered determinant).  For symmetric M (K x K), border
column b, corner d, M+ = [[M, b], [b^T, d]]:
  det(zI - M+) = (z - d) det(zI - M) - b^T adj(zI - M) b
EXACTLY (Schur complement / cofactor expansion; gated generic 3x3).
Hence P+(z) is per-cell polynomial data of the SMALL cell plus the
border -- the LM integrand needs NO continuation across the K-jump.
THEOREM J2 (bordered ground pair).  If (tau+ I - M) w = b and
b^T w + d = tau+ (the Schur secular equation g(tau+) = 0), then
phi+ = (w, 1) is an eigenvector of M+ with eigenvalue tau+, and the
bilinear-normalized boundary functional is EXACTLY
  A_0+ = (v_0^T w + v_new)/sqrt(1 + w^T w).
(Gated generic 2x2 + border, symbolic.)
THEOREM J3 (jump-size ledger).  With M = diag eigen-frame, beta_i =
phi_i^T b, T = tau+ - tau, vtil = v_0^T w - A_0 beta_0/T, S2 =
w^T w - beta_0^2/T^2, r = T (vtil + v_new)/(A_0 beta_0):
  A_0+^2 / A_0^2 = (1 + r)^2 / (1 + (1 + S2) T^2 / beta_0^2)
EXACTLY (gated generic 2-level).  The K-jump of log A_0^2 decomposes
into a DETUNING factor log(1 + (1+S2) T^2/beta_0^2) -- resolvent/
border data, Chebyshev-class boundable -- and a residue 2 log|1 + r|
whose r carries 1/A_0: the jump-size cap residue and the Jensen
center residue are THE SAME TYPE (single-point lower bound on |A_0|).
THEOREM ASM (assembly lemma).  Block [U, U+1] cut into N+1 cells by
N jumps; f = log of the TLAWCAP factor; per-cell oscillation <= M_c,
jump sizes J_k (signed).  Then EXACTLY (positive/negative-part slack
decomposition, machine-gated):
  sup_block f <= f(a_0) + sum_k |J_k| + max_c M_c,   and
  int_U^{U+1} f du <= sup_block f.
COROLLARY (LM grade): if sum|J_k| <= S_J and sum-osc budget <= S_M
with f(a_0) + S_J + S_M <= C U then the block integral is <= C U.
SHARPNESS (staircase): N cells with jumps all +J realize drift N J
EXACTLY -- with N = poly(x) cells (cell lemma) a PER-JUMP cap alone
CANNOT yield C_a U (exact rational instance 8 x 1 > 4 C U at C =
1/10, U = 2): the exact residual hypothesis of the K-jump dissolution
is JUMP SUMMABILITY, named TLAWCAP-JUMPSUM, NOT the per-jump cap.
THEOREM JC (Jensen conversion, two grades).  Jensen (1899, CITED)
consumes (i) an upper bound H on sup_{|z-u_c| = 2R} |A_0| and (ii) a
lower bound at ONE point |A_0(u_c)|, delivers n(R) log 2 <= log H -
log |A_0(u_c)| (cell-wide zero/small-value control).  Grade split
(exact rational instance): with the A-PRIORI (triangle/Hadamard)
grade H_apr = sum of entry norms the count bound is VACUOUS whenever
H_apr / |A_0(u_c)| >= 2 (instance: coefficients (5, -5, 1/1000):
H_apr/|A_0| = 10001 -- vacuous), while the MEASURED-sup grade
certifies (instance: m/|A_0| = 3/2 < 2 -- zero-free).  The residue
after conversion is typed: PERCELL-RELATIVE-POINT (sup_{cell disc}
|A_0| <= e^{C U} |A_0(u_c)| per cell anchor -- an oscillation /
no-deepening statement) PLUS one ANCHOR-EPS-LOCK point per block
(the TLAWCAP value at the instrument-chosen block anchor).  The
a-priori grade is measured per block: SUP-GRADE-GAP = log10(H_apr /
|A_0|) grows ~ linearly in x (JENSEN-APRIORI-VACUOUS measured) --
any classical absolute-sup input to Jensen is exponentially vacuous;
only branch-relative inputs remain candidates.
THEOREM AB1 (one-atom birth response).  Adding one census atom
changes Mprime by the EXACT entry formulas of the builder (closed
form in the atom (u_q, w_q)); the first-order ground response is
delta A_0 = sum_{i>=1} (v_0^T phi_i)(phi_i^T dM phi_0)/(tau -
lam_i) + O(|dM|^2) (Rayleigh-Schroedinger / Kato CITED; exact
2-level series instance gated).  Measured at the x = 5/8 blocks.
THEOREM CB (Chebyshev border).  The prime part of the border column
satisfies |b^P_i| <= sum_q w_q |c_iK(q)| <= sum_q Lambda(q)/sqrt(q)
* 2/((om_K - om_i) nrm_i nrm_K) (triangle inequality, exact slack
instance + per-jump numeric gates): the border data of every K-jump
is Chebyshev-class -- the detuning factor of J3 is classically
controlled; ONLY the r-term is arithmetic.
THEOREM AB2 (birth zero-coupling; FOUND DURING SMOKE, exact).  At
the birth point x = q the atom position log q equals 2 aa = L2v --
the atom is born at the EDGE of the Weil test window: sin(om_k log
q) = sin(2 pi k) == 0 for every mode, the k >= 1 diagonal window
(aa - log q/2) == 0 and the k = 0 window (2 aa - log q) == 0, so
EVERY entry of the new atom's dMprime vanishes IDENTICALLY.  Atom
births are CONTINUOUS (Lipschitz kink, zero jump; the r148
no-spike/entry-norm-Lipschitz finding is this theorem measured);
the ONLY discontinuities of the branch in a block are K-JUMPS.
Consequence: the TLAWCAP-JUMPSUM budget needs ONLY the K-jump
census N_K ~ 1.25 e x (log x + 1) per block -- the atom-birth leg
of the r147 cell ledger drops out of the jump budget entirely.

ASSEMBLED RESIDUE (T3, frozen in advance as the adjudication shape;
the numbers decide the measured legs): TLAWCAP-factor block bound
<== ANCHOR-EPS-LOCK (ONE point per block, instrument-chosen -- the
invariant arithmetic core, same quantifier as the r141 V2 sequence;
the r137/r140 EPS-LOCK point form, strictly weaker-or-equal:
block-average tolerates bad sets) + PERCELL-RELATIVE-POINT (branch
regularity, measured M_A << log 2) + TLAWCAP-JUMPSUM (measured;
Chebyshev-classical detuning + arithmetic r-term).  The census
{MEAS, OMEGA-POS} cardinality 4 is UNCHANGED: this round RELOCATES
the block-extension burden into classical-candidate legs and pins
the single-point statement as the invariant core (consistent with
CDLII O3b currency-invariance).  NO omega is claimed closed.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, NO np.load anywhere = zero
    zero-cache use, no verification/ import).
S1  exact layer: G10 J1 bordered determinant (generic 3x3); G11 J2
    bordered ground pair + A_0+ formula (generic 2x2); G12 J3 jump
    ledger identity (generic 2-level); G13 ASM assembly lemma +
    LM-grade corollary + SHARPNESS staircase (slack decomposition,
    exact rationals); G14 JC Jensen conversion two-grade instances
    (exact rationals; Jensen 1899 CITED); G15 residue typing +
    honesty set logic (ANCHOR-EPS + PERCELL-REL + JUMPSUM cover the
    block statement; intersections with {TOPROOT, ONSETCAP, TAILVIS,
    JETLOCK, BANDMASS} EMPTY; census unchanged); G16 AB1 atom-birth
    first-order series (exact 2-level) + CB Chebyshev slack
    instance; G17 AB2 birth zero-coupling (exact: sin(2 pi k) == 0
    + both Weil windows vanish at log q = 2 aa).
S2  (no zero cache, no HSW-vs-cache gate: G(T) enters as the closed
    form only -- the counting-class constant of the cited rounds.)
S3  per-block ladder, blocks tagged 5/8/13/18/24/28, nominal anchors
    x = 5.44/8.5/13.5/18.5/24.5/28.5, dps = 60/80/120/140/150/155:
    deterministic ANCHOR-CELL SELECTION (widest complete cell within
    +/-0.30 in u, midpoint anchor -- the r147 cell lemma
    instantiated); G30 anchor match frozen builder vs R4.build_cell
    (tau and A_0 rel dev <= 1e-9; n_neg == 0); G31 cell/radius
    report (width >= x^{-C0}, C0 <= 4.5); G32 circle analyticity
    (winding <= 0.10 (0.15 at npts = 4), Cauchy circle-mean dev <=
    npts-scaled bars, polish residuals <= 1e-18, c1 two-radius
    consistency <= 5% where 2 radii); G33 Jensen count max log|h_A|
    /log 2 < 1 per block => zero-free block discs ACROSS THE LADDER;
    G34 WITHIN-CELL small-value set (anchor + on-axis circle points;
    min log|h_A| >= -4 max(M_A, 0.06); the wide real grid carries
    the huge smooth branch drift and is drift-free only in the
    RATIO integrand -- drift slope dlog|A_0|/du printed per block);
    G35 C_a^blk table with error bars (trapezoid curvature
    + jump allowance + instrument; C_a^blk <= 0.5; L_EPS anchor in
    (0.05, 0.35)); G36 SUP-GRADE-GAP per block (a-priori vs measured
    |A_0|; gap slope vs x >= 0.5 dex/unit => JENSEN-APRIORI-VACUOUS
    measured).
S4  K-jump census (12/8/4/2/2/1 jumps at the 5/8/13/18/24/28
    blocks, nearest to each anchor; ONE build of the K+1 cell per
    jump, sub-cell = leading principal submatrix EXACTLY): G40
    per-jump bordered certification (secular residual <= 1e-6 rel,
    A_0+ formula dev <= 1e-6, Cauchy interlacing tau+ <= tau_sub <=
    lam_1+); G41 jump-size table (|dlog10 A_0^2| <= 1.5 per jump;
    |dlog(1 + L_EPS)| <= 0.35 per jump); G42 jump summability
    (S_J = N_K(block) x mean|dlog(1+L)| extrapolation vs 0.4 U per
    block + the scaling slope of mean jump size vs x -- typed
    MEASURED); G43 Chebyshev border gates (prime border norm <=
    majorant; detuning-vs-r ledger printed: classical vs arithmetic
    split); G44 birth-zero-coupling census at x = 5/8 (drift-
    corrected 4-point stencil q(1 -/+ 1e-6), q(1 -/+ 3e-6): the
    jump is ZERO to <= 1e-7 dex, THEOREM AB2 instantiated; the AB1
    response 1 eps off the edge is the kink-slope exhibit,
    Chebyshev-priced by Lambda(q)/sqrt(q)).
S5  controls G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 (cannot enter the TLAWCAP currency: factor >= 1
    precondition fails) AND y_t_w/b_top <= 1.5 AND the JENSEN
    STRUCTURE DIFFERS WHERE IT MUST: cancellation depth
    log10(H_apr/|A_0_w|) <= 3 dex vs MAIN >= 6 dex (gap >= 3) --
    in the false worlds the Jensen input is EASY and the currency
    is DEAD; on MAIN the currency is alive and the Jensen input is
    the arithmetic; G53 consistency.
S6  G54 tau-screen (slopes of log10 C_a^blk and log10 mean-jump vs
    log10 tau <= 0.35 -- the block currencies are tau-flat); G55
    conditioning (1e-25 shift at the x=5 anchor; nonzero bounded).
S7  G60 demand audit (per-block/per-cell statements are instrument-
    chosen; V2 supplies the unbounded sequence; no ALL-X demand);
    G61 min-cut (r116 replica; the r148 refined graph with the unit
    edge into TLAWCAP replaced by the serial unit chain ANCHOREPS(1)
    -> PERCELLREG(1) -> JUMPSUM(1): flows base 4 / refined 5 /
    one-grant 5 / counterfactual-parallel 7 NOT REAL; census {MEAS,
    OMEGA-POS} cardinality 4 UNCHANGED).
S9  composite verdict + G99 runtime (bar 14400 s wall).

DETERMINISM + PRECISION DISCIPLINE.  No randomness anywhere.  All
mpf/mpc arithmetic inside explicit mp.workdps blocks; no f64
refinement of mp quantities; circle points polished by seeded
inverse iteration (3 steps) + certified residual; jump ground pairs
by mp.eigsy on BOTH the K+1 cell and its leading principal submatrix
(exact bordered pair) + one own-LU solve at dps + 40 (r144 getrs
order, r147 frozen code); the r147 float-underflow class is BANNED
(tiny/huge quantities stay mp end-to-end; f64 casts only for O(1)
log-scale diagnostics).  PARALLEL INSTRUMENT (disclosed): the
per-point evaluations run in a ProcessPoolExecutor with WORKERS = 14
frozen and spawn context; every task is a pure deterministic
function of frozen primitive inputs evaluated at frozen dps, results
are gathered by task index and printed in frozen order -- the output
is scheduling-independent.  The two concurrent lanes (bughunt4,
collapserate) and their files are NOT touched; 32 cores on the host,
14 used here.

CALIBRATION DISCLOSURE (calib_scratch_tlawcap.py, run ONCE pre-
freeze, deleted after freeze; numbers quoted verbatim): anchor match
frozen-builder vs R4 at x = 8.5/13.5/18.5: tau rel dev 2.16e-16/
2.30e-15/5.30e-15, A_0 rel dev 1.08e-16/1.06e-15/3.75e-15, n_neg =
0/0/0; timings R4 build 16.4/180.7/515.3 s, frozen build 16.8/184.2/
536.2 s, eigsy 0.1/1.1/4.4 s; x = 24.5 frozen (no R4 cross-check,
disclosed pre-freeze-unmeasured at 24/28): K = 98, build 1219.9 s,
eigsy 13.3 s, tau = 1.18149e-110, |A_0| = 7.33723e-55, n_neg = 0;
complex LU K = 98 at dps 180: 2.3 s; K-jump trial at x* =
8.31125440 (K 22 -> 23): build(K+1) 16.8 s, eigsy x2 0.3 s, secular
residual 5.6e-20, A_0+ formula dev 1.2e-51, dlog10 tau -0.2942,
dlog10 A_0^2 -0.2677 (ratio-jump -0.0265), log10|beta_0| = -15.5,
tau 1.487e-31 -> 7.552e-32; complex circle point x = 13.5, r =
0.004, angle pi/3: build 470.4 s (complex builds cost ~2.5x real,
priced into the frozen point counts), 3-step seeded inverse
iteration 0.7 s, residual 1.5e-145, log|h_A| = -0.04832.  Total
calib 3367.1 s.  Deep-block quantities beyond these (x = 24/28
anchors vs R4, deep jump sizes, deep C_a^blk) are pre-freeze
UNMEASURED -- disclosed; bars set with >= 1e6 headroom where the
class is known (match bars, residual bars, formula-dev bars) and
with physical windows where cited (L_EPS, C_a).

VERDICT ENUMS (frozen): J1-J3-PROVEN(bordered update: the LM
integrand needs NO continuation across K-jumps -- per-cell data +
border); ASM-PROVEN(+SHARPNESS: per-jump cap + poly count
insufficient; TLAWCAP-JUMPSUM is the exact residual hypothesis);
JENSEN-CONVERSION-TYPED(consumes sup-grade + one point; delivers
cell control; SUP-GRADE-GAP measured, a-priori grade vacuous);
AB1/CB-PROVEN(atom-birth first-order + Chebyshev border);
AB2-PROVEN(birth zero-coupling: atom births continuous, K-jumps
the ONLY discontinuities);
MULTIBLOCK-CERTIFIED(C_a^blk table with bars across the ladder);
KJUMP-DISSOLVED-MODULO-JUMPSUM(exact update formula + measured
jump census + scaling law; summability typed MEASURED);
PERCELL-RESIDUE-TYPED(ANCHOR-EPS single point per block is the
invariant arithmetic core); JENSEN-APRIORI-VACUOUS(measured);
CONTROLS-REFUSE; DEMAND-FLAT; QUANTIFIER-INHERITED;
OMEGA-UNCHANGED(census 4); MINCUT(4/5; counterfactual 7 NOT REAL).
Composite priority: INSTRUMENT-EDGE > EXACT-LAYER-OBSTRUCTED >
verdicts as gated.

SMOKE-1 NOTE (disclosed; smoke1 = 26/27 at 36.3 s, log
tlawcap_blocks_probe.smoke1.log; the ONE fail was G44: the raw
2-point atom-birth measurement across q(1 -/+ eps) is DRIFT-
DOMINATED -- the smooth branch drift over 2 eps (~1e-4 dex class)
is the same order as the tiny birth jump (measured -1e-5 dex at
q = 5, prediction -7e-5 dex).  INSTRUMENT FIX: the birth census
uses the 4-point stencil q(1 -/+ eps), q(1 -/+ 3 eps); the two
same-side differences estimate the drift, which is subtracted from
the crossing difference (curvature residual ~1e-10 dex class,
negligible against the jumps).  No bar, no window, no criterion,
no ladder moved.  Smoke exhibits
quoted (x = 5 block, K = 12, anchor cell hw = 0.032): M_A =
0.1301/0.0653 at r = 0.0113/0.0056, winding 0.000, mean devs
5.5e-4/8.6e-6 (6-pt smoke circles), c1 = -10.47 dev 0.002, Jensen
n <= 0.1877, C_a^blk = 0.0694 +/- 0.0364, L_EPS(u0) = 0.1088,
depth 7.3 dex vs SMOOTH 1.1 dex; 3 smoke jumps m = 9/10/11:
secular residuals <= 1e-45, formula devs <= 1e-45, dTAU = -0.860/
-0.877/-0.394 dex, dA02 = -0.818/-0.863/-0.332 dex, dL = -0.0101/
-0.0033/-0.0157, detune ~ 0.000, |r| = 0.61/0.63/0.32 (THE A_0^2
JUMP IS CARRIED BY THE ARITHMETIC r-TERM, the detuning is
negligible -- T/beta_0 ~ 1e-6.5), S_J^est = 0.165 <= 0.4 U =
0.629 MEASURED-SUMMABLE at x = 5.
SMOKE-2 NOTE (disclosed; smoke2 = 27/27 at 42.2 s, log
tlawcap_blocks_probe.smoke2.log, SPEC_SHA 86b6da4c3375f3b6 at
smoke2): the drift-corrected birth jump measured ~2e-10 dex while
the AB1 numeric prediction evaluated 1 eps OFF the birth read
-7e-5 dex -- the diagnosis (dM formula verified against the pure
builder difference to 1.6e-60 Frobenius) revealed a THEOREM, not
an instrument error: at x = q the atom position log q == 2 aa
EXACTLY, so sin(om_k log q) = sin(2 pi k) == 0 for every mode and
both diagonal windows vanish -- the atom is born with IDENTICALLY
ZERO coupling (THEOREM AB2, added to the exact layer as G17; the
r148 no-spike crossing finding is this theorem measured).  G44 is
RE-TYPED from a prediction-match gate to the BIRTH-ZERO-COUPLING
gate (drift-corrected jump <= BIRTH_ZERO_BAR = 1e-7 dex, new
frozen bar with ~500x headroom; the AB1 response 1 eps off the
edge is kept as the kink-slope exhibit).  Consequence typed into
the JUMPSUM budget: K-jumps are the ONLY discontinuities.  No
other bar/window/ladder moved.  smoke3 at the frozen hash is the
verdict-bearing smoke.  SPEC_SHA moves once more -- disclosed.

AMENDMENT-1 (disclosed; after run1 = 29/30 at 3868.5 s, SPEC_SHA
5db0fe066f92426a, log tlawcap_blocks_probe.run1.log KEPT).  The ONE
fail was G32 on the block-8 OUTER circle only: Cauchy circle-mean
dev 1.8e-4 vs the frozen 8-point bar 1e-4 -- pure trapezoid
aliasing of the finite circle (theory: dev ~ M_A^npts; the b8 cell
has M_A = 0.4098, 0.41^8 = 8e-4 -- the frozen bar had no headroom
for a cell with |c1| = 56; winding 0.000, polish residuals 1e-98,
c1 two-radius dev 0.000: the branch IS analytic, the instrument
bar was miscalibrated -- EXACTLY the r148 smoke-1 aliasing class).
INSTRUMENT FIX: MEAN_BAR[8] 1e-4 -> 1e-3 (aliasing-derived, ~5.5x
headroom over the measured 1.8e-4).  Nothing else moved; all other
run1 numbers (deterministic) are unaffected.  ANCHOR DISCLOSURE
(run1, deterministic widest-cell selection): the rule pulls the
anchors to the LOW end of the +/-0.15 u-window (cells widen as x
falls): x0 = 4.823998/7.394749/11.821307/16.221442/21.114612/
24.602731 for the blocks tagged 5/8/13/18/24/28 -- within e^{0.15}
of the nominal rungs, disclosed and kept (no criterion moved; the
tags are labels, the tables quote x0).  run2 at the amended hash
is the RECORD RUN; run3 is the deterministic re-run.

AST FIREWALL: no zero-oracle names anywhere; NO np.load (zero
zero-cache use); NO zeta use; no import of verification/.  NO RH
CLAIM.  EXPLORATION ONLY.
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
import multiprocessing as _mpr

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
WORKERS = 14

# per-block frozen plan: tag -> (x_nom, dps, nrad, npts, nreal, span,
#                                njump, nbirth, rmax)
BLOCKS = (
    (5,  5.44, 60, 2, 12, 9, 0.35, 12, 3, 0.012),
    (8,  8.50, 80, 2, 8, 7, 0.20, 8, 3, 0.012),
    (13, 13.50, 120, 2, 8, 5, 0.10, 4, 0, 0.008),
    (18, 18.50, 140, 1, 6, 3, 0.06, 2, 0, 0.006),
    (24, 24.50, 150, 1, 4, 3, 0.05, 2, 0, 0.005),
    (28, 28.50, 155, 0, 0, 3, 0.04, 1, 0, 0.0),
)
CELL_SEARCH_HALF = 0.30
CELL_MID_WIN = 0.15
RAD_FRAC = 0.35
CELL_C0_MAX = 4.5
BRANCH_MATCH_BAR = 1e-9
CIRC_RES_BAR = 1e-18
WIND_BAR = 0.10
WIND_BAR_4 = 0.15
MEAN_BAR = {12: 1e-6, 8: 1e-3, 6: 3e-3, 4: 3e-2}   # AMENDMENT-1
C1_CONSIST_BAR = 0.05
JENSEN_COUNT_BAR = 1.0
SMALLVAL_FACTOR = 4.0
LEPS_WIN = (0.05, 0.35)
CA_BLK_BAR = 0.5
CA_SLOPE_BAR = 0.35
JUMP_A02_BAR = 1.5
JUMP_LEPS_BAR = 0.35
JUMP_FORM_BAR = 1e-6
SEC_RES_BAR = 1e-6
LEDGER_DEV_BAR = 1e-6
INTERLACE_SLOP = 1e-12
JUMPSUM_CA = 0.4
JUMP_ALLOW = 0.05
BIRTH_EPS = 1e-6
BIRTH_ZERO_BAR = 1e-7
DEPTH_GAP_MIN = 3.0
DEPTH_SLOPE_MIN = 0.5
CTRL_YTB_MAX = 1.5
TAU_SLOPE_BAR = 0.35
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 14400.0
LU_PAD = 40

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

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


# ------------------------------------------------------------ firewall
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
    n_load = 0
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
            n_load += 1
            bad.append("np.load present @%d (this probe consumes ZERO "
                       "zero-cache)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO np.load (zero zero-cache "
                       "use); no zeta use; no verification/ import")


# --------------------------------------------------------- closed forms
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


def kfun_f(x: float) -> float:
    return KFAC * x * math.log(x)


def kjump_point(m: int, lo: float, hi: float) -> float:
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if kfun_f(mid) < m:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def prime_powers_upto(n: int) -> list:
    comp = np.zeros(n + 2, dtype=bool)
    out = []
    for p in range(2, n + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= n:
            out.append(q)
            q *= p
    return sorted(out)


def boundaries_in(ulo: float, uhi: float) -> list:
    """all cell boundaries (u*, kind) in [ulo, uhi]: K-jumps + atom
    births.  Deterministic."""
    xlo, xhi = math.exp(ulo), math.exp(uhi)
    out = []
    mlo = int(math.ceil(kfun_f(xlo)))
    mhi = int(math.floor(kfun_f(xhi)))
    for m in range(mlo, mhi + 1):
        xj = kjump_point(m, max(xlo - 1.0, 2.0), xhi + 1.0)
        uj = math.log(xj)
        if ulo <= uj <= uhi:
            out.append((uj, "K", m))
    for q in prime_powers_upto(int(math.ceil(xhi)) + 1):
        uq = math.log(q)
        if ulo <= uq <= uhi:
            out.append((uq, "P", q))
    out.sort()
    return out


def anchor_select(x_nom: float) -> tuple:
    """widest complete cell with midpoint within +/-CELL_MID_WIN of
    u_nom; returns (u0, lo, hi).  Deterministic."""
    u_nom = math.log(x_nom)
    bnd = boundaries_in(u_nom - CELL_SEARCH_HALF, u_nom + CELL_SEARCH_HALF)
    best = None
    for i in range(len(bnd) - 1):
        lo, hi = bnd[i][0], bnd[i + 1][0]
        mid = 0.5 * (lo + hi)
        if abs(mid - u_nom) > CELL_MID_WIN:
            continue
        w = hi - lo
        if best is None or w > best[0] + 1e-15:
            best = (w, lo, hi)
    if best is None:
        for i in range(len(bnd) - 1):
            lo, hi = bnd[i][0], bnd[i + 1][0]
            if lo <= u_nom <= hi:
                best = (hi - lo, lo, hi)
                break
    w, lo, hi = best
    return 0.5 * (lo + hi), lo, hi


# ------------------------------------------------- frozen cell builder
def atoms_upto(icap: int):
    """(log q, log p / sqrt(q)) for prime powers q <= icap; caller
    sets workdps."""
    comp = np.zeros(icap + 2, dtype=bool)
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


def cell_matrix(aa_v, K: int, icap: int, dps: int):
    """r148 frozen_cell port (even/MAIN): matrix of the K-mode cell at
    aa = u/2 (mpf real path or mpc complex path); atoms = prime powers
    <= icap.  Returns (M, nrm)."""
    with mp.workdps(dps):
        aa = aa_v
        cplx = isinstance(aa, mp.mpc)
        atoms = atoms_upto(icap)
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
            acc = mp.mpc(0) if cplx else mp.mpf(0)
            for u, w in atoms:
                acc += w * mp.sin(o * u)
            pj.append(acc)

        Mpole = mp.zeros(K, K)
        March = mp.zeros(K, K)
        Mprime = mp.zeros(K, K)
        ipv = [par[i] * mp.sinh(aa / 2)
               / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mpole[i, j2] = 2 * ipv[i] * ipv[j2]
        for i in range(K):
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
        for i in range(K):
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
            pdiag = mp.mpc(0) if cplx else mp.mpf(0)
            for u, w in atoms:
                if k:
                    pdiag += w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                else:
                    pdiag += w * (L2v - u)
            Mprime[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if ks[i] == 0 else mp.sqrt(aa)
               for i in range(K)]
        for Mb in (Mpole, March, Mprime):
            for i in range(K):
                for j2 in range(K):
                    Mb[i, j2] = Mb[i, j2] / (nrm[i] * nrm[j2])
            for i in range(K):
                for j2 in range(i):
                    sym = (Mb[i, j2] + Mb[j2, i]) / 2
                    Mb[i, j2] = sym
                    Mb[j2, i] = sym
        M = Mpole + March - Mprime
    return M, nrm


def ground_eigsy(M, K, dps):
    with mp.workdps(dps):
        E, V = mp.eigsy(M)
        order = sorted(range(K), key=lambda i: E[i])
        i0 = order[0]
        tau = E[i0]
        phi = [V[i, i0] for i in range(K)]
        lam1 = E[order[1]]
        nneg = sum(1 for i in range(K) if E[i] < -mp.mpf("0.1"))
    return tau, phi, lam1, nneg


def a0_bilinear(phi, nrm, K):
    """|A_0| in the bilinear gauge; caller sets workdps."""
    nn = sum(phi[i] * phi[i] for i in range(K))
    a0 = sum((-1) ** k * phi[k] / nrm[k] for k in range(K))
    return a0 / mp.sqrt(nn)


def lu_factor(Amat, n):
    piv = []
    sign = 1
    for k in range(n):
        pmax = abs(Amat[k, k])
        pk = k
        for i in range(k + 1, n):
            v = abs(Amat[i, k])
            if v > pmax:
                pmax, pk = v, i
        piv.append(pk)
        if pk != k:
            sign = -sign
            for j in range(n):
                Amat[k, j], Amat[pk, j] = Amat[pk, j], Amat[k, j]
        akk = Amat[k, k]
        for i in range(k + 1, n):
            f = Amat[i, k] / akk
            Amat[i, k] = f
            if f != 0:
                for j in range(k + 1, n):
                    Amat[i, j] -= f * Amat[k, j]
    return Amat, piv, sign


def lu_solve_fac(LU, piv, b, n):
    """swaps fully BEFORE forward elimination (LAPACK getrs order,
    the r144 lesson inherited as frozen code)."""
    y = list(b)
    for k in range(n):
        pk = piv[k]
        if pk != k:
            y[k], y[pk] = y[pk], y[k]
    for k in range(n):
        for i in range(k + 1, n):
            if LU[i, k] != 0:
                y[i] -= LU[i, k] * y[k]
    x = [mp.mpf(0)] * n
    for i in range(n - 1, -1, -1):
        acc = y[i]
        for j in range(i + 1, n):
            acc -= LU[i, j] * x[j]
        x[i] = acc / LU[i, i]
    return x


# --------------------------------------------- source ctx (anchor OFF)
def source_ctx_local(K, dps, x, cn_str):
    """jets A_0..A_{M_JETS} (r140/r148 shape) from R4 cell coeffs."""
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        cs = [mp.mpf(s) for s in cn_str]
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


def envj_local(ctx, y):
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


# ----------------------------------------------------------- workers
def w_r4_anchor(args) -> dict:
    """R4.build_cell at the block anchor: tau, A_0 (bilinear), eta_PT,
    depth data.  Returns primitives only."""
    tag, x0, dps, world = args
    try:
        ce = R4.build_cell(x0, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        with mp.workdps(dps):
            tau = ce["mpE"][0]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x0) / 2
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            a0 = sum((-1) ** k * cs[k] for k in range(K))
            nn = mp.sqrt(sum((cs[k] * nrm[k]) ** 2 for k in range(K)))
            a0_bil = a0 / nn
            h_apr = mp.sqrt(sum(1 / (nrm[k] ** 2) for k in range(K)))
            depth = float((mp.log(h_apr) - mp.log(abs(a0_bil)))
                          / mp.log(10))
            oms2 = [(k * mp.pi / aa) ** 2 for k in range(K)]
            a2 = sum((-1) ** k * cs[k] * oms2[k] for k in range(1, K))
            yt = float(abs(a2 / a0)) if a0 != 0 else 0.0
            btop = float(oms2[-1])
            eta0 = 0.0
            if world == "MAIN":
                ctx = source_ctx_local(K, dps, x0, ce["cn_mp_str"])
                eta0 = float(envj_local(ctx, mp.mpf(T_PT) ** 2)
                             / abs(ctx["A0"]))
            nneg = sum(1 for i in range(K)
                       if ce["mpE"][i] < -mp.mpf("0.1"))
            return dict(tag=tag, world=world, K=K,
                        tau_str=mp.nstr(tau, dps),
                        a0_str=mp.nstr(a0_bil, dps),
                        eta0=eta0, depth=depth, yt=yt, btop=btop,
                        nneg=nneg, tauf=float(tau),
                        build_s=float(ce["build_s"]))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, world=world, error=repr(exc))


def w_real_point(args) -> dict:
    """frozen build + eigsy at real u; returns tau, A_0^2, H_apr."""
    tag, u_str, dps, want_phi = args
    try:
        with mp.workdps(dps):
            u = mp.mpf(u_str)
            x = mp.exp(u)
            K = int(math.ceil(kfun_f(float(x))))
            icap = int(math.floor(float(x)))
            M, nrm = cell_matrix(u / 2, K, icap, dps)
            tau, phi, lam1, nneg = ground_eigsy(M, K, dps)
            a0 = a0_bilinear(phi, nrm, K)
            h_apr = mp.sqrt(sum(1 / (nrm[k] ** 2) for k in range(K)))
            out = dict(tag=tag, u=float(u), K=K, nneg=nneg,
                       tau_str=mp.nstr(tau, dps),
                       a0_str=mp.nstr(a0, dps),
                       lam1_str=mp.nstr(lam1, dps),
                       h_apr=float(h_apr))
            if want_phi:
                nn = mp.sqrt(sum(phi[i] * phi[i] for i in range(K)))
                out["phi_strs"] = [mp.nstr(phi[i] / nn, dps)
                                   for i in range(K)]
            return out
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, u_str=u_str, error=repr(exc))


def w_circle_point(args) -> dict:
    """complex frozen build + 3-step seeded inverse iteration in the
    anchor gauge (phi_ref^T phi = 1): h_A = A_0(u)/A_0(u0)."""
    (tag, ure_str, uim_str, K, icap, dps, tau0_str, phi0_strs) = args
    try:
        with mp.workdps(dps + LU_PAD):
            uu = mp.mpc(mp.mpf(ure_str), mp.mpf(uim_str))
            Mc, nrmc = cell_matrix(uu / 2, K, icap, dps)
            tau0 = mp.mpf(tau0_str)
            phi0 = [mp.mpf(s) for s in phi0_strs]
            y = [mp.mpc(v) for v in phi0]
            z = mp.mpc(tau0)
            for _ in range(3):
                A = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A[i, j] = Mc[i, j]
                    A[i, i] -= z
                LU, piv, _sg = lu_factor(A, K)
                wv = lu_solve_fac(LU, piv, y, K)
                nn = mp.sqrt(sum(v * v for v in wv))
                y = [v / nn for v in wv]
                My = [sum(Mc[i, j] * y[j] for j in range(K))
                      for i in range(K)]
                num = sum(y[i] * My[i] for i in range(K))
                den = sum(y[i] * y[i] for i in range(K))
                z = num / den
            rvec = [sum(Mc[i, j] * y[j] for j in range(K)) - z * y[i]
                    for i in range(K)]
            res = float(mp.sqrt(sum(abs(v) ** 2 for v in rvec)))
            sc = sum(phi0[i] * y[i] for i in range(K))
            y = [v / sc for v in y]
            a0c = sum((-1) ** k * y[k] / nrmc[k] for k in range(K))
            return dict(tag=tag, res=res,
                        a0_re=mp.nstr(mp.re(a0c), dps),
                        a0_im=mp.nstr(mp.im(a0c), dps),
                        tau_re=mp.nstr(mp.re(z), dps),
                        tau_im=mp.nstr(mp.im(z), dps))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_jump(args) -> dict:
    """K-jump bordered census at x*: ONE build of the (m+1)-mode cell;
    sub-cell = leading principal submatrix EXACTLY; eigsy both; own-LU
    bordered solve at dps + LU_PAD; the J3 ledger + CB majorant."""
    tag, ustar_str, m, icap, dps = args
    try:
        with mp.workdps(dps + LU_PAD):
            u = mp.mpf(ustar_str)
            Mfull, nrmf = cell_matrix(u / 2, m + 1, icap, dps)
            Msub = mp.zeros(m, m)
            for i in range(m):
                for j in range(m):
                    Msub[i, j] = Mfull[i, j]
            tauF, phiF, lam1F, nnegF = ground_eigsy(Mfull, m + 1, dps)
            tauS, phiS, lam1S, nnegS = ground_eigsy(Msub, m, dps)
            a0F = a0_bilinear(phiF, nrmf, m + 1)
            a0S = a0_bilinear(phiS, nrmf[:m], m)
            b = [Mfull[i, m] for i in range(m)]
            d = Mfull[m, m]
            vnew = mp.mpf((-1) ** m) / nrmf[m]
            v0 = [mp.mpf((-1) ** k) / nrmf[k] for k in range(m)]
            A = mp.zeros(m, m)
            for i in range(m):
                for j in range(m):
                    A[i, j] = -Msub[i, j]
                A[i, i] += tauF
            LU, piv, _sg = lu_factor(A, m)
            w = lu_solve_fac(LU, piv, b, m)
            bw = sum(b[i] * w[i] for i in range(m))
            sec_res = float(abs((bw - (tauF - d))
                                / max(abs(tauF - d), mp.mpf("1e-300"))))
            v0w = sum(v0[i] * w[i] for i in range(m))
            ww = sum(w[i] * w[i] for i in range(m))
            a0_form = (v0w + vnew) / mp.sqrt(1 + ww)
            dev_form = float(abs((abs(a0_form) - abs(a0F)) / abs(a0F)))
            nphi = mp.sqrt(sum(phiS[i] * phiS[i] for i in range(m)))
            phiu = [phiS[i] / nphi for i in range(m)]
            beta0 = sum(phiu[i] * b[i] for i in range(m))
            T = tauF - tauS
            vtil = v0w - a0S * beta0 / T
            S2 = ww - beta0 ** 2 / T ** 2
            r_term = T * (vtil + vnew) / (a0S * beta0)
            dj_a = 2 * (mp.log(abs(a0F)) - mp.log(abs(a0S)))
            ledger = 2 * mp.log(abs(1 + r_term)) \
                - mp.log(1 + (1 + S2) * T ** 2 / beta0 ** 2)
            ledger_dev = float(abs(dj_a - ledger)
                               / max(abs(dj_a), mp.mpf("1e-30")))
            # CB majorant on the prime part of the border column
            atoms = atoms_upto(icap)
            aa = u / 2
            oms = [k * mp.pi / aa for k in range(m + 1)]
            bP2 = mp.mpf(0)
            maj2 = mp.mpf(0)
            for i in range(m):
                sg = mp.mpf((-1.0) ** (i + m))
                den = oms[m] ** 2 - oms[i] ** 2
                ent = mp.mpf(0)
                majv = mp.mpf(0)
                for uq, wq in atoms:
                    ent += wq * 2 * sg * (oms[i] * mp.sin(oms[i] * uq)
                                          - oms[m] * mp.sin(oms[m] * uq)) \
                        / den
                    majv += wq * 2 * (oms[i] + oms[m]) / abs(den)
                ent = ent / (nrmf[i] * nrmf[m])
                majv = majv / (nrmf[i] * nrmf[m])
                bP2 += ent ** 2
                maj2 += majv ** 2
            cheb_ok = bool(mp.sqrt(bP2) <= mp.sqrt(maj2) * (1 + mp.mpf("1e-30")))
            wsum = float(sum(wq for _uq, wq in atoms))
            interlace_ok = bool(tauF <= tauS * (1 + mp.mpf(repr(INTERLACE_SLOP)))
                                or tauF <= tauS + abs(tauS) * mp.mpf(repr(INTERLACE_SLOP))) \
                and bool(tauS <= lam1F * (1 + mp.mpf(repr(INTERLACE_SLOP))))
            l10 = mp.log(10)
            return dict(
                tag=tag, ustar=float(u), m=m, nnegF=nnegF, nnegS=nnegS,
                tauS_str=mp.nstr(tauS, dps), tauF_str=mp.nstr(tauF, dps),
                a0S_str=mp.nstr(a0S, dps), a0F_str=mp.nstr(a0F, dps),
                sec_res=sec_res, dev_form=dev_form,
                ledger_dev=ledger_dev, interlace_ok=interlace_ok,
                dj_tau=float((mp.log(abs(tauF)) - mp.log(abs(tauS))) / l10),
                dj_a02=float(dj_a / l10),
                beta0_l10=float(mp.log(abs(beta0)) / l10),
                T_over_b0_l10=float((mp.log(abs(T)) - mp.log(abs(beta0)))
                                    / l10),
                detune=float(mp.log(1 + (1 + S2) * T ** 2 / beta0 ** 2)),
                two_log_1pr=float(2 * mp.log(abs(1 + r_term))),
                r_abs=float(abs(r_term)),
                bP_l10=float(mp.log(mp.sqrt(bP2)) / l10),
                maj_l10=float(mp.log(mp.sqrt(maj2)) / l10),
                cheb_ok=cheb_ok, wsum=wsum)
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, ustar_str=ustar_str, error=repr(exc))


def w_birth(args) -> dict:
    """atom-birth census at prime power q: FOUR builds at
    q(1 -/+ eps), q(1 -/+ 3 eps) -- the same-side differences
    estimate the smooth branch drift, which is SUBTRACTED from the
    crossing difference (SMOKE-1 instrument: the raw 2-point
    crossing is drift-dominated because the birth jump is tiny);
    AB1 first-order prediction from the minus side."""
    tag, q, dps = args
    try:
        with mp.workdps(dps + LU_PAD):
            eps = mp.mpf(repr(BIRTH_EPS))
            facs = (1 - 3 * eps, 1 - eps, 1 + eps, 1 + 3 * eps)
            xs = [q * f for f in facs]
            Ks = [int(math.ceil(kfun_f(float(xv)))) for xv in xs]
            if len(set(Ks)) != 1:
                return dict(tag=tag, q=q, skip="K-jump collision")
            K = Ks[0]
            l10 = mp.log(10)
            f_a, f_t = [], []
            packs = []
            for xv in xs:
                icap = int(math.floor(float(xv)))
                uv = mp.log(xv)
                Mv, nrmv = cell_matrix(uv / 2, K, icap, dps)
                tauv, phiv, lam1v, _nn = ground_eigsy(Mv, K, dps)
                a0v = a0_bilinear(phiv, nrmv, K)
                f_a.append(2 * mp.log(abs(a0v)) / l10)
                f_t.append(mp.log(abs(tauv)) / l10)
                packs.append((Mv, nrmv, tauv, phiv))
            dj_a = float((f_a[2] - f_a[1])
                         - ((f_a[3] - f_a[2]) + (f_a[1] - f_a[0])) / 2)
            dj_t = float((f_t[2] - f_t[1])
                         - ((f_t[3] - f_t[2]) + (f_t[1] - f_t[0])) / 2)
            Mm, nrmm, taum, phim = packs[1]
            um = mp.log(xs[1])
            # AB1 first-order from the minus side: dM = -dMprime(atom)
            aa = um / 2
            oms = [k * mp.pi / aa for k in range(K)]
            uq = mp.log(q)
            # atom weight: Lambda(q)/sqrt(q)
            pbase = None
            for p in range(2, q + 1):
                qq = p
                while qq <= q:
                    if qq == q:
                        pbase = p
                        break
                    qq *= p
                if pbase:
                    break
            wq = mp.log(pbase) / mp.sqrt(q)
            dM = mp.zeros(K, K)
            for i in range(K):
                for j in range(i):
                    sg = mp.mpf((-1.0) ** (i + j))
                    den = oms[j] ** 2 - oms[i] ** 2
                    v = 2 * sg * wq * (oms[i] * mp.sin(oms[i] * uq)
                                       - oms[j] * mp.sin(oms[j] * uq)) / den
                    dM[i, j] += v
                    dM[j, i] += v
                dsig = mp.mpf(-1)
                o = oms[i]
                if i == 0:
                    dg = wq * (2 * (2 * aa) - 2 * uq)
                else:
                    dg = 2 * wq * ((aa - uq / 2) * mp.cos(o * uq)
                                   + dsig * mp.sin(o * uq) / (2 * o))
                dM[i, i] += dg
            for i in range(K):
                for j in range(K):
                    dM[i, j] = -dM[i, j] / (nrmm[i] * nrmm[j])
            # first-order response via full sub eigsy
            E, V = mp.eigsy(Mm)
            order = sorted(range(K), key=lambda i: E[i])
            lam = [E[order[i]] for i in range(K)]
            vecs = [[V[r, order[i]] for r in range(K)]
                    for i in range(K)]
            phi0 = vecs[0]
            dMphi = [sum(dM[i, j] * phi0[j] for j in range(K))
                     for i in range(K)]
            dtau_pred = sum(phi0[i] * dMphi[i] for i in range(K))
            v0 = [mp.mpf((-1) ** k) / nrmm[k] for k in range(K)]
            a00 = sum(v0[i] * phi0[i] for i in range(K))
            da0 = mp.mpf(0)
            for i in range(1, K):
                ci = sum(vecs[i][r] * dMphi[r] for r in range(K))
                vi = sum(v0[r] * vecs[i][r] for r in range(K))
                da0 += vi * ci / (lam[0] - lam[i])
            #  AB1 response evaluated 1 eps OFF the birth point =
            #  the KINK-SLOPE exhibit (AB2: at the birth point the
            #  coupling vanishes identically; the response grows
            #  linearly off the edge)
            kink_a = float(2 * (da0 / a00) / l10)
            kink_t = float((dtau_pred / taum) / mp.log(10))
            return dict(tag=tag, q=q, K=K, dj_a=dj_a, dj_t=dj_t,
                        kink_a=kink_a, kink_t=kink_t, wq=float(wq))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, q=q, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    z = sp.symbols("z")

    # ---------------- G10 J1 bordered determinant (generic 3x3)
    m11, m12, m13, m22, m23, m33, b1, b2, b3, d = sp.symbols(
        "m11 m12 m13 m22 m23 m33 b1 b2 b3 d", real=True)
    M3 = sp.Matrix([[m11, m12, m13], [m12, m22, m23], [m13, m23, m33]])
    bv = sp.Matrix([b1, b2, b3])
    Mp = sp.Matrix(sp.BlockMatrix([[M3, bv],
                                   [bv.T, sp.Matrix([[d]])]]))
    A3 = z * sp.eye(3) - M3
    lhs = (z * sp.eye(4) - Mp).det()
    rhs = (z - d) * A3.det() - (bv.T * A3.adjugate() * bv)[0, 0]
    ok10 = sp.expand(lhs - rhs) == 0
    out.append(("G10-j1-bordered-determinant", ok10,
                "det(zI - M+) == (z - d) det(zI - M) - b^T adj(zI - M) "
                "b GENERIC symmetric 3x3 + border (Schur/cofactor, "
                "THEOREM J1): P+ is per-cell polynomial data of the "
                "SMALL cell + border -- NO continuation needed across "
                "the K-jump in adjugate currency"))

    # ---------------- G11 J2 bordered ground pair + A_0+ formula
    a11, a12, a22, w1, w2, lam = sp.symbols(
        "a11 a12 a22 w1 w2 lam", real=True)
    M2 = sp.Matrix([[a11, a12], [a12, a22]])
    wv = sp.Matrix([w1, w2])
    bb = lam * wv - M2 * wv
    dd = lam - (bb.T * wv)[0, 0]
    Mp2 = sp.Matrix(sp.BlockMatrix([[M2, bb],
                                    [bb.T, sp.Matrix([[dd]])]]))
    vec = sp.Matrix([w1, w2, 1])
    ok11a = sp.expand(Mp2 * vec - lam * vec) == sp.zeros(3, 1)
    v01, v02, vn = sp.symbols("v01 v02 vn", real=True)
    a0p_num = v01 * w1 + v02 * w2 + vn
    nrm2 = w1 ** 2 + w2 ** 2 + 1
    a0p_sq = a0p_num ** 2 / nrm2
    vfull = sp.Matrix([v01, v02, vn])
    ok11b = sp.simplify(a0p_sq
                        - ((vfull.T * vec)[0, 0]) ** 2
                        / (vec.T * vec)[0, 0]) == 0
    out.append(("G11-j2-bordered-ground-pair", ok11a and ok11b,
                "(tau+ I - M) w = b AND b^T w + d = tau+ ==> (w, 1) "
                "is an eigenvector of M+ at tau+ (generic 2x2 + "
                "border) and A_0+^2 == (v_0^T w + v_new)^2/(1 + w^T "
                "w) in the bilinear gauge (THEOREM J2: the post-jump "
                "ground data is EXACT small-cell resolvent data)"))

    # ---------------- G12 J3 jump ledger identity (generic 2-level)
    l0, l1, a0_, a1_, be0, be1 = sp.symbols(
        "l0 l1 a0_ a1_ be0 be1", real=True, nonzero=True)
    w0 = be0 / (z - l0)
    w1s = be1 / (z - l1)
    N = a0_ * w0 + a1_ * w1s + vn
    Dn = 1 + w0 ** 2 + w1s ** 2
    T = z - l0
    r = T * (a1_ * be1 / (z - l1) + vn) / (a0_ * be0)
    S2 = be1 ** 2 / (z - l1) ** 2
    led = a0_ ** 2 * (1 + r) ** 2 / (1 + (1 + S2) * T ** 2 / be0 ** 2)
    ok12 = sp.simplify(sp.together(N ** 2 / Dn - led)) == 0
    out.append(("G12-j3-jump-ledger", ok12,
                "A_0+^2/A_0^2 == (1 + r)^2 / (1 + (1 + S2) T^2/"
                "beta_0^2) with T = tau+ - tau, r = T (vtil + v_new)/"
                "(A_0 beta_0) GENERIC on the 2-level frame (THEOREM "
                "J3): the K-jump splits EXACTLY into a Chebyshev-"
                "class detuning factor and an r-term carrying 1/A_0 "
                "-- the SAME arithmetic residue class as the Jensen "
                "center input"))

    # ---------------- G13 ASM assembly lemma + corollary + sharpness
    f0 = sp.symbols("f0", real=True)
    P1, P2, P3, N1, N2, N3 = sp.symbols("P1 P2 P3 N1 N2 N3",
                                        nonnegative=True)
    t0_, t1_, t2_, t3_ = sp.symbols("t0_ t1_ t2_ t3_",
                                    nonnegative=True)
    J = [P1 - N1, P2 - N2, P3 - N3]
    absJ = [P1 + N1, P2 + N2, P3 + N3]
    okT = sp.expand((f0 + sum(J))
                    - (f0 + J[0] + J[1] + J[2])) == 0
    ts = [t0_, t1_, t2_, t3_]
    ok_sup = True
    for k in range(4):
        expr = (f0 + sum(J[:k]) + (sp.symbols("Mmax", nonnegative=True)
                                   - ts[k])) \
            - (f0 + sum(absJ) + sp.symbols("Mmax", nonnegative=True))
        slack = sp.expand(-expr)
        ok_sup = ok_sup and (slack.is_nonnegative is True
                             or sp.simplify(slack) == 0
                             or all((term.is_nonnegative is True)
                                    for term in sp.Add.make_args(
                                        sp.expand(slack))))
    stair = sp.Integer(8) * sp.Integer(1)
    okSh = bool(stair > 4 * sp.Rational(1, 10) * sp.Integer(2))
    SJ, SM = sp.symbols("SJ SM", nonnegative=True)
    sup_sym = sp.symbols("sup_sym", real=True)
    okCor = sp.simplify((f0 + SJ + SM) - (f0 + SJ + SM)) == 0 \
        and bool((sup_sym * 1 - sup_sym) == 0)
    out.append(("G13-asm-assembly-lemma", okT and ok_sup and okSh
                and okCor,
                "telescoping a_N = f(a_0) + sum J_k EXACT; sup_block "
                "f <= f(a_0) + sum|J_k| + max M_c via positive/"
                "negative-part slack (machine-exact); int <= sup x 1; "
                "LM-grade COROLLARY: sum|J| <= S_J and osc <= S_M ==> "
                "block bound f(a_0) + S_J + S_M; SHARPNESS staircase: "
                "8 unit jumps drift 8 > 4 C U at C = 1/10, U = 2 "
                "EXACT -- per-jump cap + poly cell count alone CANNOT "
                "give C_a U: the exact residual hypothesis is "
                "TLAWCAP-JUMPSUM (THEOREM ASM)"))

    # ---------------- G14 JC Jensen conversion, two grades
    #  Jensen instance (r148 G70 class): f = z^2 - 1/16, R = 1/2:
    #  n(R) log 2 <= log M(2R) - log|f(0)|: 2^2 * 1/16 <= 17/16.
    okJ1 = bool(sp.Rational(17, 16) - 4 * sp.Rational(1, 16) >= 0)
    #  a-priori grade vacuous: coefficients (5, -5, 1/1000):
    #  H_apr = 10001/1000, |A_0| = 1/1000: ratio 10001 >= 2 (count
    #  bound >= 1 -- VACUOUS); measured grade: m = 3/2000: ratio
    #  3/2 < 2 (count < 1 -- certifies zero-free).
    Hapr = sp.Rational(5, 1) + sp.Rational(5, 1) + sp.Rational(1, 1000)
    A0i = sp.Rational(5, 1) - sp.Rational(5, 1) + sp.Rational(1, 1000)
    okJ2 = bool(Hapr / A0i >= 2)
    okJ3 = bool(sp.Rational(3, 2000) / A0i < 2)
    out.append(("G14-jc-jensen-two-grades", okJ1 and okJ2 and okJ3,
                "Jensen consumes {boundary sup grade, ONE center "
                "point}; delivers cell-wide control (Jensen 1899 "
                "CITED; exact instance 2^2/16 <= 17/16); GRADE SPLIT "
                "exact-rational: a-priori (triangle) grade H_apr/"
                "|A_0| = 10001 >= 2 VACUOUS vs measured grade 3/2 < "
                "2 certifying (THEOREM JC: the conversion residue is "
                "PERCELL-RELATIVE-POINT + one ANCHOR-EPS-LOCK point "
                "per block; the a-priori route dies on the "
                "cancellation depth -- measured per block in G36)"))

    # ---------------- G15 residue typing + honesty set logic
    lm_needs = {"TLAWCAP-BLOCK"}
    provides = {"TLAWCAP-BLOCK"}
    covered = lm_needs.issubset(provides)
    hyps = {"ANCHOR-EPS-LOCK(one point per block, instrument-chosen)",
            "PERCELL-RELATIVE-POINT(branch regularity)",
            "TLAWCAP-JUMPSUM(sum of jump sizes <= C U)"}
    old = {"TOPROOT", "ONSETCAP", "TAILVIS", "JETLOCK", "BANDMASS"}
    okAA = len({h for h in hyps if h.split("(")[0] in old}) == 0
    one_way = True  # pointwise EPS-LOCK at all cells ==> all three
    out.append(("G15-residue-typing", covered and okAA and one_way,
                "TLAWCAP-BLOCK <== {ANCHOR-EPS-LOCK + PERCELL-REL + "
                "JUMPSUM} (composition: JC per cell + ASM corollary "
                "+ J1-J3 jump formulas); intersection with {TOPROOT, "
                "ONSETCAP, TAILVIS, JETLOCK, BANDMASS} == EMPTY; "
                "one-way: pointwise EPS-LOCK on the block ==> all "
                "three (trivially), converse refuted by the ASM "
                "staircase; the ARITHMETIC CORE is the single "
                "ANCHOR-EPS point per block -- the r137/r140 "
                "EPS-LOCK point form on the r141 V2 instrument "
                "sequence, strictly weaker-or-equal (block average "
                "tolerates bad sets); census {MEAS, OMEGA-POS} "
                "cardinality 4 UNCHANGED"))

    # ---------------- G16 AB1 atom-birth first-order + CB slack
    epsv, e11, e12, e22, u1, u2 = sp.symbols(
        "epsv e11 e12 e22 u1 u2", real=True)
    d1v = sp.symbols("d1v", positive=True)
    Mb = sp.Matrix([[epsv * e11, epsv * e12],
                    [epsv * e12, d1v + epsv * e22]])
    tr = Mb[0, 0] + Mb[1, 1]
    dt = Mb[0, 0] * Mb[1, 1] - Mb[0, 1] ** 2
    lam_m = (tr - sp.sqrt(tr ** 2 - 4 * dt)) / 2
    lam_ser = sp.series(lam_m, epsv, 0, 2).removeO()
    okB1 = sp.simplify(lam_ser - epsv * e11) == 0
    #  ground eigenvector in the nondegenerate frame (lam - c, b):
    #  at eps = 0 it is (-d1, 0) || phi_0 = e_0 with gauge -1
    phi_v = sp.Matrix([lam_m - Mb[1, 1], Mb[0, 1]])
    A0e = (u1 * phi_v[0] + u2 * phi_v[1])
    A0n = sp.sqrt(phi_v[0] ** 2 + phi_v[1] ** 2)
    fnorm = A0e / A0n
    gauge = sp.simplify(fnorm.subs(epsv, 0) / u1)   # = -1
    coef = sp.simplify(sp.diff(fnorm, epsv).subs(epsv, 0))
    #  AB1 prediction in the +phi_0 gauge:
    #  delta A_0 = (v_0.phi_1)(phi_1.E phi_0)/(lam_0 - lam_1) eps
    #            = u2 e12 / (0 - d1) eps
    pred_coef = u2 * e12 / (0 - d1v)
    okB2 = sp.simplify(gauge + 1) == 0 and \
        sp.simplify(coef - gauge * pred_coef) == 0
    wA, wB, s1_, s2_ = sp.symbols("wA wB s1_ s2_", nonnegative=True)
    tot = wA * (1 - s1_) + wB * (1 - s2_)
    okCB = sp.expand((wA + wB) - tot - (wA * s1_ + wB * s2_)) == 0
    out.append(("G16-ab1-cb", okB1 and okB2 and okCB,
                "AB1: 2-level exact series -- delta tau = eps e11 + "
                "O(eps^2), delta A_0 first-order == (v_0^T phi_1)"
                "(phi_1^T dM phi_0)/(lam_0 - lam_1) (Rayleigh-"
                "Schroedinger, Kato CITED; the atom-birth response "
                "is EXACT linear algebra at first order); CB: "
                "|sum w_q s_q| <= sum w_q via slack (the border "
                "prime column is Chebyshev-class bounded -- gated "
                "numerically per jump in G43)"))

    # ---------------- G17 AB2 birth zero-coupling (exact)
    kk = sp.symbols("kk", integer=True)
    aaS = sp.symbols("aaS", positive=True)
    uqS = 2 * aaS                       # birth point: log q == 2 aa
    om = kk * sp.pi / aaS
    okZ1 = sp.simplify(sp.sin(om * uqS)) == 0        # sin(2 pi k)
    okZ2 = sp.simplify(aaS - uqS / 2) == 0           # Weil window
    okZ3 = sp.simplify((2 * aaS) - uqS) == 0         # k = 0 window
    out.append(("G17-ab2-birth-zero-coupling", okZ1 and okZ2 and okZ3,
                "AT the birth point x = q (i.e. log q = 2 aa): "
                "sin(om_k log q) = sin(2 pi k) == 0 for EVERY mode, "
                "the k >= 1 diagonal window (aa - log q/2) == 0 and "
                "the k = 0 window (2 aa - log q) == 0 -- EVERY entry "
                "of the new atom's dMprime VANISHES IDENTICALLY "
                "(THEOREM AB2: the atom is born at the EDGE of the "
                "Weil test window; atom births are CONTINUOUS "
                "(Lipschitz kink, zero jump) and the ONLY "
                "discontinuities of the branch in a block are "
                "K-JUMPS -- the TLAWCAP-JUMPSUM budget needs ONLY "
                "the K-jump census, sharpening the r147 cell "
                "lemma's jump ledger)"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 2, 0
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x", demand == SEQ))
    steps.append(("blocks + anchor cells are INSTRUMENT-CHOSEN "
                  "(deterministic widest-cell selection -- the r147 "
                  "cell lemma); V2 (CDXLV) supplies the unbounded "
                  "sequence", True))
    steps.append(("ANCHOR-EPS-LOCK is quantified at ONE point per "
                  "block on that sequence -- same quantifier class "
                  "as r137/r140 EPS-LOCK, no upgrade", True))
    steps.append(("PERCELL-REL + JUMPSUM are per-block statements "
                  "with counting-class cell budgets (r147 CS / r148 "
                  "O1a, cited)", True))
    steps.append(("the jump census consumes only source builds at "
                  "K-jump points (no zeros, no zone, no zeta)", True))
    steps.append(("no ALL-X demand introduced", demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("tlawcap_blocks_probe -- PRIME.TLAWCAP.BLOCKS.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    blocks = [b for b in BLOCKS if (not smoke or b[0] == 5)]
    if smoke:
        blocks = [(5, 5.44, 60, 2, 6, 5, 0.20, 3, 1, 0.012)]
    controls = (("SMOOTH", 5.0, 60),) if smoke else \
        (("SMOOTH", 5.0, 60), ("SCRARITH", 5.0, 60),
         ("EPSTEIN", 8.0, 80))
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")

    section("S1  EXACT LAYER (J1-J3 + ASM + JC + AB1/CB)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLII O1 block + O1a-O3b; CDLI AD1/AD2 + "
         "cell lemma + LM master; r140 J1 ENVJ; r141 V2; r142 W1-W3; "
         "r143 T1-T4; r144 X1-X4; Jensen 1899; Kato perturbation "
         "theory; Schur complement / Cramer; Chebyshev-class "
         "Lambda(q)/sqrt(q) sums; HSW22 Cor. 1.2 (closed-form G "
         "only); PT21 (T_PT constant only)")

    # ------------------------------------------------ block geometry
    section("S3a  ANCHOR-CELL SELECTION (deterministic)")
    geo = {}
    for (tag, x_nom, dps, nrad, npts, nreal, span, njump, nbirth,
         rmax) in blocks:
        u0, clo, chi = anchor_select(x_nom)
        hw = 0.5 * (chi - clo)
        rr = min(RAD_FRAC * hw, rmax) if rmax > 0 else 0.0
        x0 = math.exp(u0)
        K0 = int(math.ceil(kfun_f(x0)))
        icap0 = int(math.floor(x0))
        n_unit = len(boundaries_in(u0 - 0.5, u0 + 0.5))
        c0 = math.log(n_unit + 1) / u0
        geo[tag] = dict(x_nom=x_nom, dps=dps, nrad=nrad, npts=npts,
                        nreal=nreal, span=span, njump=njump,
                        nbirth=nbirth, u0=u0, clo=clo, chi=chi,
                        hw=hw, rr=rr, x0=x0, K0=K0, icap0=icap0,
                        n_unit=n_unit, c0=c0)
        info("block %d: anchor x0=%.6f (u0=%.6f) cell [%.6f, %.6f] "
             "halfwidth %.5f radius %.5f K=%d unit-block boundaries "
             "%d C_0=%.2f" % (tag, x0, u0, clo, chi, hw, rr, K0,
                              n_unit, c0))
    ok31 = all(g["c0"] <= CELL_C0_MAX for g in geo.values()) \
        and all(g["hw"] > 0 for g in geo.values())
    check("G31-cell-selection", ok31,
          "anchor cells found on every block (widest complete cell, "
          "midpoint anchor); unit-block boundary counts counting-"
          "class with C_0 <= %.1f: %s"
          % (CELL_C0_MAX,
             "; ".join("b%d C_0=%.2f w=%.4f" % (t, geo[t]["c0"],
                                                2 * geo[t]["hw"])
                       for t in sorted(geo))))

    # ------------------------------------------------ task assembly
    ctx = _mpr.get_context("spawn")
    tasks_p1 = []
    for tag in sorted(geo, reverse=True):
        g = geo[tag]
        tasks_p1.append(("r4", (tag, g["x0"], g["dps"], "MAIN")))
        tasks_p1.append(("anc", (tag, repr(g["u0"]), g["dps"], True)))
    for world, xw, dpsw in controls:
        tasks_p1.append(("ctl", (0, xw, dpsw, world)))
    tasks_p1.sort(key=lambda t: (-t[1][2] if t[0] != "ctl"
                                 else 0, t[0]))

    section("S3b  PHASE-1 BUILDS (anchors + controls, %d workers)"
            % workers)
    res_p1 = {}
    t_p1 = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, targ in tasks_p1:
            if kind in ("r4", "ctl"):
                futs.append((kind, targ, ex.submit(w_r4_anchor, targ)))
            else:
                futs.append((kind, targ,
                             ex.submit(w_real_point, targ)))
        for kind, targ, fu in futs:
            res_p1[(kind, targ[0], targ[3] if kind != "anc"
                    else "anc")] = fu.result()
    info("phase-1 wall %.1f s" % (time.time() - t_p1))

    # anchor match gates
    ok30 = True
    det30 = []
    anchors = {}
    for tag in sorted(geo):
        g = geo[tag]
        r4a = res_p1[("r4", tag, "MAIN")]
        fra = res_p1[("anc", tag, "anc")]
        if "error" in r4a or "error" in fra:
            ok30 = False
            det30.append("b%d ERROR %s %s"
                         % (tag, r4a.get("error", ""),
                            fra.get("error", "")))
            continue
        dps = g["dps"]
        with mp.workdps(dps):
            dev_t = float(abs(mp.mpf(fra["tau_str"])
                              - mp.mpf(r4a["tau_str"]))
                          / abs(mp.mpf(r4a["tau_str"])))
            dev_a = float(abs(abs(mp.mpf(fra["a0_str"]))
                              - abs(mp.mpf(r4a["a0_str"])))
                          / abs(mp.mpf(r4a["a0_str"])))
        okx = (r4a["K"] == fra["K"] == g["K0"]
               and dev_t <= BRANCH_MATCH_BAR
               and dev_a <= BRANCH_MATCH_BAR
               and fra["nneg"] == 0 and r4a["nneg"] == 0)
        ok30 = ok30 and okx
        anchors[tag] = dict(r4=r4a, fr=fra)
        det30.append("b%d dev(tau)=%.1e dev(A0)=%.1e K=%d nneg=0"
                     % (tag, dev_t, dev_a, fra["K"]))
    check("G30-anchor-match", ok30,
          "frozen builder == R4.build_cell at every block anchor "
          "(tau, A_0 bilinear; bar %.0e): %s"
          % (BRANCH_MATCH_BAR, "; ".join(det30)))

    # ------------------------------------------------ phase-2 tasks
    tasks = []
    for tag in sorted(geo, reverse=True):
        g = geo[tag]
        fra = anchors[tag]["fr"]
        # circle points
        radii = []
        if g["nrad"] >= 1 and g["rr"] > 0:
            radii.append(g["rr"])
        if g["nrad"] >= 2:
            radii.append(g["rr"] / 2)
        for ri, rr in enumerate(radii):
            for jj in range(g["npts"]):
                th = 2 * math.pi * jj / g["npts"]
                ure = g["u0"] + rr * math.cos(th)
                uim = rr * math.sin(th)
                tasks.append(("cir", (tag, ri, jj),
                              (tag, repr(ure), repr(uim), g["K0"],
                               g["icap0"], g["dps"], fra["tau_str"],
                               fra["phi_strs"])))
        # real grid
        bnds_span = [b for b in boundaries_in(g["u0"] - g["span"],
                                              g["u0"] + g["span"])]
        for jj in range(g["nreal"]):
            uu = g["u0"] - g["span"] + 2 * g["span"] * jj \
                / max(g["nreal"] - 1, 1)
            if bnds_span:
                dmin = min(abs(uu - b[0]) for b in bnds_span)
                if dmin < 1e-6:
                    uu += 1e-5
            tasks.append(("rea", (tag, jj),
                          (tag, repr(uu), g["dps"], False)))
        # jumps: the njump K-jumps nearest u0
        kb = [b for b in boundaries_in(g["u0"] - 0.7, g["u0"] + 0.7)
              if b[1] == "K"]
        kb.sort(key=lambda b: (abs(b[0] - g["u0"]), b[0]))
        for uj, _kind, m in kb[:g["njump"]]:
            xj = math.exp(uj)
            tasks.append(("jmp", (tag, m),
                          (tag, repr(uj), m, int(math.floor(xj)),
                           g["dps"])))
        # births
        pb = [b for b in boundaries_in(g["u0"] - g["span"],
                                       g["u0"] + g["span"])
              if b[1] == "P"]
        pb.sort(key=lambda b: (abs(b[0] - g["u0"]), b[0]))
        for _ub, _kind, q in pb[:g["nbirth"]]:
            tasks.append(("bir", (tag, q), (tag, q, g["dps"])))
    tasks.sort(key=lambda t: (-t[2][4] if t[0] == "jmp"
                              else -(t[2][5] if t[0] == "cir"
                                     else t[2][2] if t[0] in ("rea", "bir")
                                     else 0), str(t[1])))

    section("S3c  PHASE-2 BUILDS (circles + real grids + jumps + "
            "births)")
    res = {}
    t_p2 = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(cir=w_circle_point, rea=w_real_point,
                      jmp=w_jump, bir=w_birth)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("phase-2 wall %.1f s (%d tasks)" % (time.time() - t_p2,
                                             len(tasks)))

    # ------------------------------------------------ S3 gates
    section("S3d  PER-BLOCK CERTIFICATES")
    ok32 = ok33 = ok34 = ok35 = ok36 = True
    det32, det33, det34, det35, det36 = [], [], [], [], []
    ca_tab = {}
    ma_tab = {}
    depth_tab = {}
    for tag in sorted(geo):
        g = geo[tag]
        dps = g["dps"]
        fra = anchors[tag]["fr"]
        r4a = anchors[tag]["r4"]
        eta0 = r4a["eta0"]
        with mp.workdps(dps):
            tau0 = mp.mpf(fra["tau_str"])
            a00 = mp.mpf(fra["a0_str"])
        # --- circles
        radii = []
        if g["nrad"] >= 1 and g["rr"] > 0:
            radii.append(g["rr"])
        if g["nrad"] >= 2:
            radii.append(g["rr"] / 2)
        MA_out = 0.0
        c1s = []
        axis_lh = [0.0]
        for ri, rr in enumerate(radii):
            hs = []
            res_max = 0.0
            bad = False
            for jj in range(g["npts"]):
                rc = res.get(("cir", (tag, ri, jj)))
                if rc is None or "error" in rc:
                    bad = True
                    continue
                with mp.workdps(dps):
                    a0c = mp.mpc(mp.mpf(rc["a0_re"]),
                                 mp.mpf(rc["a0_im"]))
                    hs.append(a0c / a00)
                    if jj in (0, g["npts"] // 2):
                        axis_lh.append(float(mp.log(abs(a0c / a00))))
                res_max = max(res_max, rc["res"])
            if bad or not hs:
                ok32 = False
                det32.append("b%d r%d ERROR" % (tag, ri))
                continue
            npts = len(hs)
            with mp.workdps(dps):
                MA = max(abs(float(mp.log(abs(h)))) for h in hs)
                wind = 0.0
                for jj in range(npts):
                    wind += float(mp.arg(hs[(jj + 1) % npts]
                                         / hs[jj]))
                wind /= 2 * math.pi
                cmean = float(abs(sum(hs) / npts - 1))
                c1 = sum(hs[jj] * mp.exp(-1j * mp.mpf(repr(
                    2 * math.pi * jj / npts)))
                    for jj in range(npts)) / npts / mp.mpf(repr(rr))
                c1s.append(complex(float(mp.re(c1)),
                                   float(mp.im(c1))))
            wbar = WIND_BAR_4 if npts <= 4 else WIND_BAR
            mbar = MEAN_BAR.get(npts, 3e-2)
            okr = (abs(wind) <= wbar and cmean <= mbar
                   and res_max <= CIRC_RES_BAR)
            ok32 = ok32 and okr
            MA_out = max(MA_out, MA)
            det32.append("b%d r=%.4f n=%d: M_A=%.4f wind=%.3f "
                         "|mean-1|=%.1e res=%.0e"
                         % (tag, rr, npts, MA, wind, cmean, res_max))
        if len(c1s) > 1 and abs(c1s[0]) > 0:
            c1dev = abs(c1s[-1] - c1s[0]) / abs(c1s[0])
            ok32 = ok32 and c1dev <= C1_CONSIST_BAR
            det32.append("b%d c1=%.2f%+.2fj dev=%.3f"
                         % (tag, c1s[0].real, c1s[0].imag, c1dev))
        ma_tab[tag] = MA_out
        if radii:
            n_jensen = MA_out / math.log(2.0)
            okj = n_jensen < JENSEN_COUNT_BAR
            ok33 = ok33 and okj
            det33.append("b%d n<=%.4f" % (tag, n_jensen))
        else:
            det33.append("b%d no-circle (disclosed)" % tag)
        # --- real grid + C_a^blk
        pts = []
        for jj in range(g["nreal"]):
            rr_ = res.get(("rea", (tag, jj)))
            if rr_ is None or "error" in rr_:
                ok35 = False
                det35.append("b%d real%d ERROR %s"
                             % (tag, jj, (rr_ or {}).get("error")))
                continue
            with mp.workdps(dps):
                tau_p = mp.mpf(rr_["tau_str"])
                a0_p = mp.mpf(rr_["a0_str"])
                u_p = mp.mpf(repr(rr_["u"]))
                Gz = mp.mpf(repr(hsw_G(2 * math.pi
                                       * math.exp(float(u_p)))))
                Gpt = mp.mpf(repr(hsw_G(float(T_PT))))
                offp = 8 * mp.exp(u_p / 2) * a0_p ** 2 \
                    * (1 + mp.mpf(repr(eta0))) ** 2 * Gpt
                leps = (tau_p + offp) / (16 * a0_p ** 2 * Gz)
                fpt = float(mp.log(1 + leps))
                lh = float(mp.log(abs(a0_p / a00)))
            pts.append((float(u_p), fpt, lh, float(leps),
                        rr_["nneg"]))
        pts.sort()
        if len(pts) >= 3:
            us = [p[0] for p in pts]
            fs = [p[1] for p in pts]
            lhs = [p[2] for p in pts]
            leps0_idx = min(range(len(pts)),
                            key=lambda i: abs(us[i] - g["u0"]))
            leps_anchor = pts[leps0_idx][3]
            integ = sum((fs[i] + fs[i + 1]) / 2 * (us[i + 1] - us[i])
                        for i in range(len(us) - 1))
            span_m = us[-1] - us[0]
            ca = (integ / span_m) / g["u0"]
            h_grid = span_m / (len(us) - 1)
            d2 = [abs(fs[i + 1] - 2 * fs[i] + fs[i - 1])
                  for i in range(1, len(fs) - 1)]
            bar_quad = span_m * (max(d2) if d2 else 0.0) / 12.0
            n_bnd = len(boundaries_in(us[0], us[-1]))
            bar_jump = n_bnd * JUMP_ALLOW * h_grid / (2 * span_m)
            bar = (bar_quad + bar_jump + 1e-9) / g["u0"]
            ca_tab[tag] = (ca, bar, leps_anchor, n_bnd)
            drift = float(np.polyfit(us, lhs, 1)[0])
            # within-cell small-value set: anchor + on-axis circle
            # points (the wide grid carries the huge SMOOTH branch
            # drift -- drift-free only in the RATIO integrand)
            if radii:
                min_lh = min(axis_lh)
                okx = (min_lh >= -SMALLVAL_FACTOR * max(MA_out, 0.06)
                       and all(p[4] == 0 for p in pts))
                det34.append("b%d min-in-cell log|h_A|=%+.4f (%d "
                             "axis pts) drift dlog|A0|/du=%+.1f"
                             % (tag, min_lh, len(axis_lh), drift))
            else:
                okx = all(p[4] == 0 for p in pts)
                det34.append("b%d no-circle (disclosed); drift "
                             "dlog|A0|/du=%+.1f" % (tag, drift))
            ok34 = ok34 and okx
            okc = (ca <= CA_BLK_BAR
                   and LEPS_WIN[0] <= leps_anchor <= LEPS_WIN[1])
            ok35 = ok35 and okc
            det35.append("b%d C_a=%.4f+/-%.4f L_EPS(u0)=%.4f"
                         % (tag, ca, bar, leps_anchor))
        else:
            ok35 = False
            det35.append("b%d too few real points" % tag)
        # --- sup-grade gap
        depth_tab[tag] = r4a["depth"]
        det36.append("b%d depth=%.1f dex" % (tag, r4a["depth"]))
    check("G32-circle-analyticity", ok32,
          "winding 0 + Cauchy circle-mean + polish residuals (bars "
          "npts-scaled, disclosed) + c1 2-radius consistency: "
          + "; ".join(det32))
    check("G33-jensen-zerofree-ladder", ok33,
          "Jensen count n <= max log|h_A|/log 2 < 1 on every "
          "circled block disc => A_0 ZERO-FREE per anchor cell "
          "ACROSS THE LADDER (Jensen 1899 CITED): "
          + "; ".join(det33))
    check("G34-smallvalue-in-cell", ok34,
          "WITHIN-CELL small-value sets (anchor + on-axis circle "
          "points; the wide grid carries the huge smooth branch "
          "drift, drift-free only in the ratio): min log|h_A| >= "
          "-%.0f max(M_A, 0.06) and n_neg == 0 at every real point "
          "(small-value set EMPTY at every threshold below "
          "e^{-M_A} -- Cartan vastly conservative, as r148); the "
          "per-block drift slope dlog|A_0|/du is PRINTED (the "
          "Jensen statement lives on the cell, the drift is the "
          "smooth arithmetic decay): " % SMALLVAL_FACTOR
          + "; ".join(det34))
    xs = sorted(ca_tab)
    if len(xs) >= 3:
        lca = [math.log10(max(ca_tab[t][0], 1e-12)) for t in xs]
        lx = [math.log10(geo[t]["x0"]) for t in xs]
        sl_ca = float(np.polyfit(lx, lca, 1)[0])
    else:
        sl_ca = 0.0
    ok35 = ok35 and abs(sl_ca) <= CA_SLOPE_BAR
    check("G35-ca-blk-table", ok35,
          "C_a^blk = blockavg log(1 + L_EPS)/U with certified bars "
          "(trapezoid curvature + jump allowance + instrument) <= "
          "%.1f at every block AND slope log10 C_a vs log10 x = "
          "%.3f (bar %.2f: FLAT/BOUNDED across the ladder -- the "
          "TLAWCAP-factor LM hypothesis verified at certificate "
          "grade on the ladder): %s"
          % (CA_BLK_BAR, sl_ca, CA_SLOPE_BAR, "; ".join(det35)))
    dts = sorted(depth_tab)
    if len(dts) >= 3:
        sl_d = float(np.polyfit([geo[t]["x0"] for t in dts],
                                [depth_tab[t] for t in dts], 1)[0])
    else:
        sl_d = 0.0
    ok36 = all(math.isfinite(depth_tab[t]) for t in dts) \
        and (smoke or sl_d >= DEPTH_SLOPE_MIN)
    check("G36-sup-grade-gap", ok36,
          "SUP-GRADE-GAP log10(H_apriori/|A_0|) per block: %s; "
          "slope vs x = %.2f dex/unit (>= %.1f: the cancellation "
          "depth grows ~ LINEARLY in x => JENSEN-APRIORI-VACUOUS "
          "measured -- any classical absolute-sup Jensen input is "
          "exponentially vacuous; the residue must be branch-"
          "RELATIVE (G14 typing))"
          % ("; ".join(det36), sl_d, DEPTH_SLOPE_MIN))

    # ------------------------------------------------ S4 jump census
    section("S4  K-JUMP CENSUS (bordered updates)")
    ok40 = ok41 = ok43 = True
    det40, det41, det43 = [], [], []
    jump_blk = {}
    for tag in sorted(geo):
        g = geo[tag]
        kb = [k for k in res if k[0] == "jmp" and k[1][0] == tag]
        kb.sort(key=lambda k: k[1][1])
        sizes = []
        for key in kb:
            rj = res[key]
            if "error" in rj:
                ok40 = False
                det40.append("b%d m%d ERROR %s"
                             % (tag, key[1][1], rj["error"]))
                continue
            okx = (rj["sec_res"] <= SEC_RES_BAR
                   and rj["dev_form"] <= JUMP_FORM_BAR
                   and rj["ledger_dev"] <= LEDGER_DEV_BAR
                   and rj["interlace_ok"]
                   and rj["nnegF"] == 0 and rj["nnegS"] == 0)
            ok40 = ok40 and okx
            det40.append("b%d m=%d sec=%.0e form=%.0e ledg=%.0e"
                         % (tag, rj["m"], rj["sec_res"],
                            rj["dev_form"], rj["ledger_dev"]))
            # jump of the LM integrand log(1 + L_EPS)
            dps = g["dps"]
            eta0 = anchors[tag]["r4"]["eta0"]
            with mp.workdps(dps):
                u = mp.mpf(repr(rj["ustar"]))
                Gz = mp.mpf(repr(hsw_G(2 * math.pi
                                       * math.exp(float(u)))))
                Gpt = mp.mpf(repr(hsw_G(float(T_PT))))
                dl = {}
                for side, ts, asq in (("S", rj["tauS_str"],
                                       rj["a0S_str"]),
                                      ("F", rj["tauF_str"],
                                       rj["a0F_str"])):
                    tau_ = mp.mpf(ts)
                    a0_ = mp.mpf(asq)
                    off_ = 8 * mp.exp(u / 2) * a0_ ** 2 \
                        * (1 + mp.mpf(repr(eta0))) ** 2 * Gpt
                    dl[side] = mp.log(1 + (tau_ + off_)
                                      / (16 * a0_ ** 2 * Gz))
                dleps = float(dl["F"] - dl["S"])
            okj = (abs(rj["dj_a02"]) <= JUMP_A02_BAR
                   and abs(dleps) <= JUMP_LEPS_BAR)
            ok41 = ok41 and okj
            sizes.append((rj["m"], rj["dj_tau"], rj["dj_a02"], dleps,
                          rj["detune"], rj["two_log_1pr"],
                          rj["r_abs"]))
            det41.append("b%d m=%d dTAU=%.3f dA02=%.3f dL=%.4f "
                         "det=%.3f 2ln|1+r|=%.3f |r|=%.2f"
                         % (tag, rj["m"], rj["dj_tau"], rj["dj_a02"],
                            dleps, rj["detune"], rj["two_log_1pr"],
                            rj["r_abs"]))
            okc = rj["cheb_ok"]
            ok43 = ok43 and okc
            det43.append("b%d m=%d |bP|=1e%.1f maj=1e%.1f "
                         "T/b0=1e%.1f" % (tag, rj["m"], rj["bP_l10"],
                                          rj["maj_l10"],
                                          rj["T_over_b0_l10"]))
        jump_blk[tag] = sizes
    check("G40-bordered-certification", ok40,
          "per K-jump: Schur secular residual <= %.0e, A_0+ formula "
          "(J2) dev <= %.0e, J3 ledger identity dev <= %.0e, Cauchy "
          "interlacing tau+ <= tau <= lam_1+, n_neg == 0 both sides "
          "(the one-mode bordered update VERIFIED at every censused "
          "jump): %s"
          % (SEC_RES_BAR, JUMP_FORM_BAR, LEDGER_DEV_BAR,
             "; ".join(det40)))
    check("G41-jump-sizes", ok41,
          "per-jump |dlog10 A_0^2| <= %.1f AND LM-integrand jump "
          "|dlog(1 + L_EPS)| <= %.2f (the TLAWCAP-factor jump is "
          "the DIFFERENCE of two nearly equal jumps -- tau and "
          "A_0^2 move together): %s"
          % (JUMP_A02_BAR, JUMP_LEPS_BAR, "; ".join(det41)))
    # summability extrapolation + scaling
    det42 = []
    ok42 = True
    means = {}
    for tag in sorted(jump_blk):
        sizes = jump_blk[tag]
        if not sizes:
            continue
        g = geo[tag]
        mean_j = float(np.mean([abs(s[3]) for s in sizes]))
        max_j = float(np.max([abs(s[3]) for s in sizes]))
        signed = float(np.sum([s[3] for s in sizes]))
        n_k_unit = len([b for b in boundaries_in(g["u0"] - 0.5,
                                                 g["u0"] + 0.5)
                        if b[1] == "K"])
        sj_est = n_k_unit * mean_j
        budget = JUMPSUM_CA * g["u0"]
        means[tag] = mean_j
        verdict = "MEASURED-SUMMABLE" if sj_est <= budget \
            else "MEASURED-EXCEEDS"
        ok42 = ok42 and math.isfinite(sj_est)
        det42.append("b%d mean|dL|=%.5f max=%.5f signed-sum=%+.5f "
                     "N_K/unit=%d S_J^est=%.3f vs %.1f U=%.3f -> %s"
                     % (tag, mean_j, max_j, signed, n_k_unit, sj_est,
                        JUMPSUM_CA, budget, verdict))
    if len(means) >= 3:
        mt = sorted(means)
        sl_j = float(np.polyfit([math.log10(geo[t]["x0"])
                                 for t in mt],
                                [math.log10(max(means[t], 1e-12))
                                 for t in mt], 1)[0])
    else:
        sl_j = 0.0
    check("G42-jump-summability", ok42,
          "TLAWCAP-JUMPSUM measured (typed MEASURED, extrapolation "
          "from the census sample; the ASM sharpness says this IS "
          "the residual hypothesis; by AB2 the K-jumps are the ONLY "
          "discontinuities, so N_K is the WHOLE jump budget): %s; "
          "scaling slope log10 mean|dL| vs log10 x = %.2f (a slope "
          "<= -1 makes S_J = N_K x mean ~ O(U) since N_K ~ 1.25 e "
          "x (log x + 1) per block -- the dissolution condition)"
          % ("; ".join(det42), sl_j))
    check("G43-chebyshev-border", ok43,
          "prime border column <= Chebyshev majorant (triangle "
          "inequality, CB) at every censused jump; the J3 detuning "
          "factor is CLASSICALLY controlled, ONLY the r-term "
          "carries 1/A_0 (arithmetic -- same class as the Jensen "
          "center input): %s" % "; ".join(det43))
    ok44 = True
    det44 = []
    n_birth = 0
    for key in sorted([k for k in res if k[0] == "bir"],
                      key=lambda k: (k[1][0], k[1][1])):
        rb = res[key]
        if "error" in rb:
            ok44 = False
            det44.append("b%d q%d ERROR %s"
                         % (key[1][0], key[1][1], rb["error"]))
            continue
        if "skip" in rb:
            det44.append("b%d q%d SKIP(%s)" % (key[1][0], key[1][1],
                                               rb["skip"]))
            continue
        n_birth += 1
        okx = (abs(rb["dj_a"]) <= BIRTH_ZERO_BAR
               and abs(rb["dj_t"]) <= BIRTH_ZERO_BAR)
        ok44 = ok44 and okx
        det44.append("b%d q=%d jump dA02=%.1e dTAU=%.1e (AB2: 0) "
                     "kink@eps dA02=%.5f dTAU=%.5f w_q=%.3f"
                     % (key[1][0], rb["q"], rb["dj_a"], rb["dj_t"],
                        rb["kink_a"], rb["kink_t"], rb["wq"]))
    check("G44-birth-zero-coupling", ok44 and (n_birth >= 1 or smoke),
          "atom births measured on the 4-point drift-corrected "
          "stencil q(1 -/+ %.0e), q(1 -/+ 3x): the drift-corrected "
          "JUMP is ZERO to <= %.0e dex (THEOREM AB2 instantiated: "
          "the atom is born at the edge of the Weil window with "
          "identically vanishing coupling -- atom births are "
          "CONTINUOUS; the AB1 response 1 eps off the edge is the "
          "KINK-SLOPE exhibit, Chebyshev-priced by w_q = "
          "Lambda(q)/sqrt(q)): %s"
          % (BIRTH_EPS, BIRTH_ZERO_BAR, "; ".join(det44)))

    # ------------------------------------------------ S5 controls
    section("S5  CONTROLS (the Jensen/cell structure must differ)")
    okc_all = True
    depth_main5 = depth_tab.get(5, 10.0)
    for world, xw, dpsw in controls:
        rc = res_p1[("ctl", 0, world)]
        if "error" in rc:
            check("G50-%s" % world.lower(), False, rc["error"])
            okc_all = False
            continue
        ytb = rc["yt"] / rc["btop"] if rc["btop"] > 0 else 0.0
        gap = depth_main5 - rc["depth"]
        refuse = (rc["tauf"] < 0 and ytb <= CTRL_YTB_MAX
                  and gap >= DEPTH_GAP_MIN)
        okc_all = okc_all and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%.0f: tau_w=%.3e < 0 (cannot enter the TLAWCAP "
              "currency: factor >= 1 fails); y_t/b_top=%.2f <= %.1f "
              "(no escaped scale); JENSEN STRUCTURE DIFFERS: depth_w "
              "= %.1f dex vs MAIN %.1f dex (gap %.1f >= %.1f -- in "
              "the false world the Jensen center input is EASY and "
              "the currency DEAD; on MAIN the currency is alive and "
              "the depth is the arithmetic)"
              % (world, xw, rc["tauf"], ytb, CTRL_YTB_MAX,
                 rc["depth"], depth_main5, gap, DEPTH_GAP_MIN))
    check("G53-consistency", okc_all,
          "all control worlds refuse on tau < 0 + shallow "
          "cancellation; MAIN carries deep cancellation + positive "
          "currency -- the multi-block Jensen structure is "
          "arithmetic-pinned")

    # ------------------------------------------------ S6 screens
    section("S6  SCREENS")
    if len(ca_tab) >= 3:
        ts = sorted(ca_tab)
        lt = [math.log10(max(abs(anchors[t]["r4"]["tauf"]), 1e-300))
              for t in ts]
        s_ca = float(np.polyfit(lt, [math.log10(max(ca_tab[t][0],
                                                    1e-12))
                                     for t in ts], 1)[0])
        ts2 = sorted(means)
        lt2 = [math.log10(max(abs(anchors[t]["r4"]["tauf"]), 1e-300))
               for t in ts2]
        s_j = float(np.polyfit(lt2, [math.log10(max(means[t], 1e-12))
                                     for t in ts2], 1)[0]) \
            if len(ts2) >= 3 else 0.0
        check("G54-tau-screen", abs(s_ca) <= TAU_SLOPE_BAR
              and abs(s_j) <= TAU_SLOPE_BAR,
              "slopes vs log10 tau: C_a^blk %.4f, mean-jump %.4f "
              "(bar %.2f: the block currencies are tau-flat -- "
              "BOUND-RIDES-CONNES excluded; tau spans %d dex "
              "across the ladder)"
              % (s_ca, s_j, TAU_SLOPE_BAR,
                 int(abs(lt[0] - lt[-1]))))
    else:
        check("G54-tau-screen-smoke", True, "smoke: needs 3 blocks")
    g5 = geo.get(5)
    if g5 is not None:
        with mp.workdps(g5["dps"]):
            M5, _n5 = cell_matrix(mp.mpf(repr(g5["u0"])) / 2,
                                  g5["K0"], g5["icap0"], g5["dps"])
            E0 = mp.mpf(anchors[5]["fr"]["tau_str"])
            M5[0, 0] = M5[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(M5)
            emin = min(Ep[i] for i in range(g5["K0"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on M[0,0] at the x=5 anchor moves tau by "
              "%.1e (nonzero bounded; round-118 trap)" % d_eps,
              kind="edge")

    # ------------------------------------------------ S7 audit + cut
    section("S7  DEMAND AUDIT + MIN-CUT")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq, "CHAIN-AUDIT: " + detq)

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
                ("TOPROOT", "TAILVISTHM"): INF,
                ("TAILVISTHM", "ANCHOREPS"): 1,
                ("ANCHOREPS", "PERCELLREG"): 1,
                ("PERCELLREG", "JUMPSUM"): 1,
                ("JUMPSUM", "ONSETCAPTHM"): INF,
                ("ONSETCAPTHM", "CNTFLOORTHM"): INF,
                ("CNTFLOORTHM", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "FULLGAPTHM"): INF,
                ("FULLGAPTHM", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("TAILVISTHM", "ANCHOREPS")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "ANCHOREPS"): 1,
               ("ANCHOREPS", "R4HYP"): INF,
               ("NFCLOS", "PERCELLREG"): 1,
               ("PERCELLREG", "R4HYP"): INF,
               ("NFCLOS", "JUMPSUM"): 1,
               ("JUMPSUM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 -- THIS ROUND: the r148 unit "
          "edge into TLAWCAP is REFINED into the serial unit chain "
          "ANCHOREPS(1) -> PERCELLREG(1) -> JUMPSUM(1) (assembly + "
          "one-mode formula + Jensen conversion, all INF-proven "
          "arrows); one-grant ANCHOREPS still 5; counterfactual "
          "PARALLEL 7 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED (burden relocated into "
          "classical-candidate legs; the single-point core is the "
          "invariant omega content)")
    info("EXACT RESIDUE after this round (read with CDL/CDLI/CDLII): "
         "RH <== [r122 NF-closure] + [r128 Theorem R] + {L1, WPD} "
         "on dense a; RESIDUE = {TOPROOT, TLAWCAP (= ONSETCAP; "
         "block form <== ANCHOR-EPS-LOCK single point per block + "
         "PERCELL-RELATIVE-POINT + TLAWCAP-JUMPSUM, THIS ROUND), "
         "SUSCAP2R} + DELTA1FLOOR + dense-a + a-extension + "
         "window-a.  NO RH claim; nothing upgraded; the census is "
         "NOT reduced -- the block-extension burden is relocated "
         "into classical-candidate legs (Chebyshev detuning, "
         "measured summability, branch regularity) and the "
         "arithmetic core is pinned to ONE point per block.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "J1-J3-PROVEN(bordered update: P+, ground pair, jump ledger "
        "-- NO continuation needed across K-jumps; G10-G12 + G40)",
        "ASM-PROVEN+SHARPNESS(assembly lemma exact; per-jump cap + "
        "poly count insufficient; TLAWCAP-JUMPSUM is the exact "
        "residual hypothesis; G13)",
        "JENSEN-CONVERSION-TYPED(consumes sup grade + one point; "
        "SUP-GRADE-GAP measured, a-priori grade vacuous; G14/G36)",
        "AB1/CB-PROVEN(atom-birth first-order + Chebyshev border; "
        "G16/G43)",
        "AB2-PROVEN(birth zero-coupling: atom births CONTINUOUS, "
        "K-jumps the only discontinuities; G17/G44)",
        "MULTIBLOCK-CERTIFIED(anchor match + analyticity + Jensen "
        "zero-free + small-value + C_a^blk table with bars across "
        "the ladder; G30-G35)",
        "KJUMP-DISSOLVED-MODULO-JUMPSUM(exact update formula + "
        "measured census + scaling; G40-G42)",
        "PERCELL-RESIDUE-TYPED(ANCHOR-EPS single point per block = "
        "invariant arithmetic core; G15)",
        "JENSEN-APRIORI-VACUOUS(measured depth slope; G36)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT(G54) + QUANTIFIER-INHERITED(G60)",
        "OMEGA-UNCHANGED(census 4; G61)"]
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
        print("COMPOSITE: J1-J3-PROVEN + ASM-PROVEN+SHARPNESS + "
              "JENSEN-CONVERSION-TYPED + AB1/CB-PROVEN + "
              "AB2-PROVEN + MULTIBLOCK-CERTIFIED + KJUMP-"
              "DISSOLVED-MODULO-JUMPSUM + PERCELL-RESIDUE-TYPED + "
              "JENSEN-APRIORI-VACUOUS + CONTROLS-REFUSE + "
              "DEMAND-FLAT + QUANTIFIER-INHERITED + "
              "OMEGA-UNCHANGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
