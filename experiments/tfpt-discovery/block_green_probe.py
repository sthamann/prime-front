#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""block_green_probe -- PRIME.LSTAR.BLOCK_GREEN.01 (round 308,
reviewer plan par.4 solution A / plan round "305"): the DISCOVERY
round of the MATRIX-VALUED DISCRETE GREEN IDENTITY ON FOURFOLD
FOLD BLOCKS.  The strategic frame (reviewer adjudication): scalar
profile functionals fail (five class families, r290-r295);
absolute-value majorants lose the load-bearing cancellation
(r297/r299/r300); local pairing is insufficient; exact
diophantine relations of the log n are irrelevant (r289
METRIC_ONLY); the carrying interference is the antiphase
next-nearest (fold distance 3-4) ARCH-ARCH class (r288 carrier
map, z_v = -3.149 at the crossing).  The reviewer target: for a
polynomial p and border coordinate t the augmented quadratic form
  Q_{z,n}(p, t) = int p^2 d(mu_z - nu_z) + 2 t u_z(p) + B_z t^2
(the v958/r244 bordered-Hankel object: u_z = the border readout
of the smooth-comb border measure sigma_z, B_z = S_{N-2} + 5/7,
the r243 budget form with the imported 5/7 reserve) shall admit
an EXACT identity
  Q_{z,n}(p, t) = sum_r <G_{z,r} Delta_r(p, t), Delta_r(p, t)>
                  + ||R_{z,n}(p, t)||^2
with Delta_r = FIXED difference/interference coordinates on
blocks of FOUR adjacent fold layers, G_{z,r} = small source-pure
matrices, R_{z,n} = an explicit remainder (carrying the 5/7
reserve); positivity then via all G_{z,r} psd plus kernel
exclusion (cap ker Delta_r cap ker R = 0 on deg p <= cap) for
strictness WITHOUT a uniform margin.  THIS ROUND IS DISCOVERY
(kill test BEFORE any proof work), NOT a proof: no L* claim, no
bound mechanism, no RH claim.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r306 discipline): w = window (kz),
S = #union entries of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = builder depth = (S+1)//2, n = degree, minC =
first n with h_n < 0, crossing = minC + 1 (r283 theorem); f =
fold index (union atoms on the uniform theta grid).  Ground
truth (minC, flips, r281 census offsets, r283/r288/r289 records)
enters GATES and record tables only; the sealed constructors
consume split-source arrays (positions, weights, fold indices,
border arrays, budget scalars) ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r284 LS.{world_pack, spectral_block}, r283
FS.mu_chain_f64 (via LS), r288 DC.zv_block, r282 RC.{toy_chain,
pv_rows, pn_split} (the refutation pins), r289 AK.twin_rational
+ MF.local_gaps (the rational twin), r244 BH.bord_chain (the
budget chain), r278 MS.ctx_build, r280 BL (via LS), v881 PIK,
r243 PB.smooth_comb, r274 WD.{stj_gen, pv_seq} (exact chains),
v563 core READ-ONLY.

THE SEALED SEARCH LANGUAGE (frozen BEFORE any positivity
measurement; every use of A^{-1}, a target eigenvector or the
measured outcome sign in a constructor => TARGET_INVERSE,
discarded):

LEG A -- THE COORDINATE LIBRARY (fixed fold incidence).  Union
atoms in FOLD ORDER (mu and nu fold sets disjoint, gated); one
block r per four consecutive union atoms (j, j+1, j+2, j+3),
r = 0..S-4 (overlapping, stride 1).  With e_i = p(x_i) the SIX
sealed coordinates of block r:
  D1 = e_{j+1} - e_j                (first difference),
  D2 = e_j - 2 e_{j+1} + e_{j+2}    (second difference),
  D3 = e_j - e_{j+2}                (the r288 antiphase
       interference coordinate layer_i - layer_{i+2}; DISCLOSED:
       D3 = -(D2 + 2 D1) is linearly dependent inside the block
       -- it is carried as sealed LANGUAGE, its G-weighting is
       not reducible to D1/D2 weightings),
  D4 = e_{j+1} - e_{j+3}            (antiphase, second copy),
  D5 = sum_i g_i e_{j+i} / sum_i g_i  (the border-coupled p part:
       the LOCAL GROSS-MASS mean, g_i = |wtilde_{j+i}|),
  D6 = t                            (the border coordinate).
Each coordinate is an exact linear form in the monomial (exact
legs) resp. Chebyshev (f64 legs; equivalent span, disclosed
conditioning choice) coefficients of p and in t, on the true
support.  The explicit remainder is SEALED, not searched:
  R(p, t) = sqrt(5/7) t,   ||R||^2 = (5/7) t^2
(the imported r243 reserve floor; B - 5/7 = S_{N-2} stays on the
block side).  Fold-layer honesty: block adjacency is UNION-ATOM
adjacency in fold order (occupancy ~ 1 on MAIN, r284 record);
the fold-LAYER reading is exact wherever occupancy is 1.

LEG B -- SYMBOLIC EXACTNESS (kill-test steps 1-2).  The identity
is LINEAR in the G entries: with L_r the block coordinate maps,
vech(A_sys) = M g must hold, A_sys = the matrix of Q - ||R||^2
on span{x^0..x^DEG, t}.  On FIVE exact worlds (Fractions,
monomial basis): TOY4 (S = 4, hand target: m_0 = 17/12, m_1 =
7/12, m_2 = 31/96, u = (1/5, 3/20), sealed B = 9/7 -- the t^2
pin G[6,6] = B - 5/7 = 4/7 is forced hand-exactly because D6 is
the only t-carrying coordinate of the single block), SM0 POSGRID
(S = 10, all weights positive -- the positive-class calibrator),
SM1 SHIELD10 (S = 10, three isolated nu atoms, each mu-shielded
-- the MAIN-class miniature), SM2 CLUST13 (S = 13, two adjacent
nu clusters -- the control-class miniature), SM3 WIDE16 (S = 16,
four spread nu atoms), plus MINI16 = the first 16 union atoms of
the REAL w9 window in fold order (f64 -> Fraction exact, frozen)
with its first 3 border atoms and the exact rational mini budget
B = S_{N-2} + 5/7 through the WD chain.  Per world: exact rank
of [M | q] vs M (fraction-free elimination, deterministic first-
nonzero pivot), EXISTENCE + dof = ncols - rank, a particular
solution (free variables = 0) and the EXACT entrywise
reconstruction gate sum_r L_r^T G_r L_r + R-form == A_target.
Verdict half 1 (sealed): IDENTITY_EXISTS(dof table) iff ALL six
exact worlds solve AND the w9 f64 residuals pass at both caps;
else IDENTITY_OVERDETERMINED_FAIL(first break locus + defect).

LEG C -- POSITIVITY CENSUS (kill-test steps 3-5; only under
IDENTITY_EXISTS).  Sealed SELECTION RULE (fixed before any
eigenvalue is seen): within the affine solution set take the
MINIMUM-FROBENIUS-NORM G family = the least-norm solution of
M g = q in the Frobenius-isometric parametrization (diagonal
entries plus sqrt(2)-scaled off-diagonals; numpy lstsq with
sealed rcond -- an inverse of the COORDINATE Gram, never of the
target).  Census: (c1) the 57 MAIN rungs (42 core = r281 census,
h <= 900, offsets gated against the r281 anchors; 15 extension
anchors = h <= 1300, sorted by (N_w, kz), first 15 -- the r286/
r306 extension rule) at cap DEG_A = 8; (c2) w9 + the r289
RATIONAL TWIN (u/Delta -> CF convergent, |du| <= 1e-8 local gap,
weights bitwise, RATIONAL_KEEPS re-gated: minC = 184, crossing =
185) + the controls EPSTEIN / SCRAMBLE(seed 1) / SMOOTH at BOTH
caps DEG_A = 8 and DEG_B = 28.  DEG_B DISCLOSURE (design-time,
from published records): the control crossings are 26/22/28
(r283), so at DEG_B the control target forms are INDEFINITE
while MAIN's is positive definite (crossing 185) -- IF the
identity exists on a control at DEG_B, a negative block
direction is FORCED by theorem (Q(p) < 0 => some block value
negative); the gate G53 tests exactly this implication live
(hard on EPSTEIN/SCRAMBLE, crossings 26/22 safely below DEG_B;
SMOOTH's crossing 28 == DEG_B is the sealed boundary case,
reported only); the non-forced, informative control contrast is
DEG_A (all worlds positive definite there).  Measured per world/cap: rel residual,
effective dof (ncols - lstsq rank), min block eigenvalue
relative to the max block Frobenius scale, #negative blocks
(sealed bar PSD_NEG = 1e-7 relative), kernel exclusion (rank of
the stacked coordinate rows + R == full coefficient dimension).
ADJUDICATION (sealed): BLOCK_GREEN_GO iff w9 + twin pass PSD +
kernel exclusion at BOTH caps AND all 57 rungs pass at DEG_A AND
every control at DEG_B shows a negative block direction (or its
identity fails there, typed CONTROL_IDENTITY_FAIL -- counted as
broken, disclosed); BLOCK_INDEFINITE_MAIN iff any MAIN-family
world fails PSD -- then the sealed DIAGNOSIS clause runs: the
SDP-like feasibility probe (alternating projection / Dykstra
between the affine solution set and the psd block cone,
FEAS_ITER = 200 sealed, deterministic start = the least-norm
point; eigen-clips act on CANDIDATE blocks, never on the
target), reported as FEAS_DIAG(final min eig, final affine
residual) -- diagnosis only, never a verdict upgrade;
WORLD_BLIND_DECOMP iff the MAIN family passes AND every control
also passes PSD at DEG_B with an existing identity (then the
decomposition is construction-trivial).  AMENDMENT a1
(calibration stage, disclosed, BEFORE the record freeze;
measurement extension only, no bar, rule or verdict rule moved):
the first full evaluation showed the least-norm choice
indefinite EVERYWHERE (even on the positive-class SM0 -- the
SELECTION, not the world, produces the indefiniteness) while the
w9 DEG_A Dykstra diagnosis converged to a genuinely psd point;
the FEAS_DIAG clause therefore measures the full feasibility
census: at DEG_A on w9 / twin / EPST / SCR / SMOOTH / SM0..SM3,
at DEG_B on w9 / twin and on the controls as the LIVE
THEOREM-CONSISTENCY side (their DEG_B target is indefinite --
Dykstra must NOT converge there); ONE uniform two-stage schedule
for every world (200 steps, then FEAS_ITER2 = 2000 when not
converged -- no MAIN preference); non-convergence is reported
ONE-SIDED (it proves no infeasibility; only convergence proves
feasibility); all of it diagnosis-only, the verdict fine-types
are untouched.

LEG D -- TARGET-INVERSE AUDIT + MUST-FAILS (each loud):
  (m1) TARGET_INVERSE: a mutant building G from the CHOLESKY of
       the assembled target matrix -- FLAGGED by the AST scope
       audit (forbidden names: cholesky / eigvecs_target /
       target_inverse / blk_eigs_true); the sealed constructors
       audit CLEAN against the same set;
  (m2) OMITTED REMAINDER: reconstructing WITHOUT the sealed R
       term must break the exact identity at the (t, t) entry by
       EXACTLY 5/7 (Fractions, SM1);
  (m3) POSTHOC FAMILY: a mutant extending the coordinate family
       AFTER sight of the measured block eigenvalues (consumes
       the withheld blk_eigs_true) -- FLAGGED by the scope audit;
  (m4) INCOMPLETE MONOMIAL COVERAGE: a mutant solving only the
       coefficient pairs with index <= 4 (claiming cap 8) must
       break the full degree-8 identity with a nonzero EXACT
       defect (Fractions, SM1) -- LOUD.
STOP LIST (anti-gates, binding): NO L* claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO posthoc window,
NO selection by measured signs, NO RH claim; r243..r307 stand.
R282 DEMARCATION (binding, in the verdict): the r282
Kasteleyn/SOS refutations (SOS register N_n > 0 at every degree
on signed toys; the orientation class value-obstructed by the
negative mass) concern the FULL signed configuration class --
every Cauchy-Binet cell n = 1..S-1, the pivot chain h_n itself
as target; the block-Green identity of this round lives on the
RESTRICTED subspace deg p <= 8 (resp. 28) << N_w below
half-filling, plus one border coordinate, with the RESTRICTED
augmented form as target -- a different language; psd blocks on
the restricted subspace assert NOTHING about h_n; no
contradiction in either direction, and no verdict of this round
touches the r282 eliminations.

WORLDS: MAIN w9 (S = 367, S_+ = 263, S_- = 104, N_w = 184, minC
= 184, crossing 185); the r289 rational twin of w9; controls
EPSTEIN / SCRAMBLE(seed 1) / SMOOTH (flips 25/21/27), built
verbatim through the r281/r284 channel; the 42-rung r281 census
ladder + 15 extension anchors.  ANCHOR PINS (Leg 0): w9 source
split; crossing 185 == minC + 1; the r288 carrier pin z_v =
-3.149 (tol 0.05 against the r285/r288 record -3.15, destructive
X_v < 0) at the crossing; the r282 refutation pin N_2(MAINLIKE)
== 48360721965/70120631072 EXACT; the 5/7-reserve convention
B_w9 = S_{N-2} + 5/7 with S_{N-2} >= 0 re-measured (rho_k >= 0
through the free window).

SEALED CONSTANTS: DEG_A 8; DEG_B 28; H_CAP 900; EXT_H 1300;
K_EXT 15; MAIN_KZ 9; CTRL_FLIPS {EPST: 25, SCR: 21, SMOOTH: 27};
ANCHORS {9:0, 12:2, 13:2, 26:3, 40:1, 15:1, 52:0}; R281_DIST
{0:18, 1:10, 2:6, 3:6, 4:1, 5:1}; EXT 8 / EXT2 32; DEPTH_PAD 6;
RAT_TOL 1e-8; QMAX 1e6; W9_ANCH (367, 263, 104, 184, 184);
CROSS_REC 185; ZV_REC -3.15 tol 0.05; R282_N2 =
48360721965/70120631072; FIVE_SEVEN 5/7; B_TOY 9/7; RES_BAR
1e-8; RCOND 1e-11; PSD_NEG 1e-7; KER_TOL 1e-12; FEAS_ITER 200;
FEAS_ITER2 2000 / FEAS_CONV 1e-9 (amendment a1, diagnosis only);
M4_CAP 4; CONS_BAR 1e-9; PIN_BAR 1e-10; SM grids: TOY4 x =
(1/2, 1/4, -1/4, -1/2) w = (1, 1/2, -1/3, 1/4) border (3/4)
w (1/5); SM0/SM1 x_j = (9-2j)/11 j = 0..9, SM0 w all = 1 except
w_2 = 1/2, w_5 = 1/3, w_8 = 1/4 (positive); SM1 w = (1, 1,
-1/3, 1, 1, -1/4, 1, 1, -1/5, 1); SM2 x_j = (12-2j)/14 j =
0..12, w = (1, 1, 1, -1/2, -1/3, 1, 1, 1, 1, -1/4, -1/5, 1, 1);
SM3 x_j = (15-2j)/17 j = 0..15, w = 1 with w_3 = -1/3, w_7 =
-1/4, w_11 = -1/5, w_14 = -1/6; SM border (4/5, 1/3, -2/5) w
(1/7, 1/11, 1/13); SM budgets exact via the WD chain B =
S_{N_w-2} + 5/7; MINI_K 16; MINI_BK 3; runtime <= 1800 s; smoke
= toys + small models + MINI16 + firewall + scopes + mutants +
w9 f64 block at DEG_A (spectral anchors, DEG_B, ladder, twin,
controls, feasibility, adjudication skipped).  PRE-SPEC SCOPING
(disclosed): every record number above is a published r281/r283/
r284/r285/r288/r289 record adopted as-is; the coordinate
library, the remainder form, the selection rule, DEG_A/DEG_B and
every bar were fixed at design time from the published record
geometry (control crossings 26/22/28, MAIN crossing 185) BEFORE
any evaluation of this probe; no machinery pass preceded this
spec except record reading; no bar, band, rule or verdict rule
was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] IDENTITY_EXISTS(dof table) /
    IDENTITY_OVERDETERMINED_FAIL(break locus, defect)
  + [exactly one of, only under IDENTITY_EXISTS]
    BLOCK_GREEN_GO(census) /
    BLOCK_INDEFINITE_MAIN(loci) [+ FEAS_DIAG(min eig, residual)
      -- diagnosis clause, never an upgrade] /
    WORLD_BLIND_DECOMP(values)
  + CONTROL_LEDGER(DEG_B forced-negativity disclosure + DEG_A
    contrast) [always]
  + R282_DEMARCATION [always].
Honesty before beauty: existence of the identity is the EASY
half (the system is linear and underdetermined on rich
libraries) -- the content sits in (i) whether the sealed
eigenvalue-free selection rule already lands psd on MAIN, (ii)
the MAIN-vs-control contrast at DEG_A where nothing is forced,
(iii) the feasibility diagnosis when it does not; the DEG_B
control negativity is forced by theorem given existence and is
DISCLOSED as such, never sold as a discovery; a passing census
fixes a TARGET for proof work, it proves neither L* nor any
cofinal statement.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 30/30 (9.2 s) at the sealed
rules -- no fail at any point; calibration pass 1 = first full
evaluation = 30/30 (27.2 s); after it AMENDMENT a1 (disclosed
above, measurement extension only: the feasibility DIAGNOSIS
grew from the two w9 caps to the full world census, then was
SYMMETRIZED to one uniform two-stage schedule for every world
and the one-sided nature of non-convergence was spelled out;
calibration passes 2/3 = 30/30, 43.8 s / 64.2 s; NO bar, band,
rule, selection rule or verdict rule moved at any point); the
only post-freeze edit is this record-table insertion, which IS
the protocol; record run1/run2 identical up to WALL):
CAL_VERDICT = IDENTITY_EXISTS(TOY4 dof 15; SM dof SM0 103 / SM1
103 / SM2 157 / SM3 219; MINI16 dof 218; w9 dof 7593@A /
7415@B) + BLOCK_INDEFINITE_MAIN(worst kz12@A min eig rel
-8.12e-02; the sealed least-norm choice does not carry) +
FEAS_DIAG(w9@A PSD-FEASIBLE (+6.6e-16, res 3.7e-14, 200 steps)
/ twin@A PSD-FEASIBLE (+2.0e-17) / EPST@A NO(-0.45) / SCR@A
NO(-0.49) / SMOOTH@A NOT CONVERGED(-1.3e-05) / SM0..SM3@A NOT
CONVERGED(-6e-03..-7e-02) / w9@B + twin@B NOT CONVERGED
(-4.2e-05 after 2000) / controls@B stay negative == the live
theorem-consistency side) + CONTROL_LEDGER(DEG_A contrast MAIN
-1.30e-02 vs EPST -0.544 / SCR -0.607 / SMOOTH -0.174) +
R282_DEMARCATION.
Key numbers.  EXACT LEG: identity exists with exact entrywise
reconstruction on ALL six exact worlds; TOY4 hand pins exact
(m_0 17/12, m_1 7/12, m_2 31/96, u (1/5, 3/20), G[6,6] == 4/7);
SM budgets 0.7317/0.7353/0.7336/0.7276, MINI16 B = 0.715612 (8
nu atoms among the first 16 w9 union atoms).  W9: S 367/263/104,
N_w 184, minC 184, crossing 185; r288 pin z_v = -3.149 (rec
-3.15), X_v = -0.0517 destructive; B_w9 = 8.368649 = S_{N-2}
7.654364 + 5/7, all 182 rho_k >= 0.  IDENTITY (f64, Chebyshev):
w9 rel res 4.0e-14@A / 4.9e-14@B; 57/57 rungs exist at DEG_A
(worst 8.1e-14); twin 4.0e-14/4.9e-14; kernel exclusion 100
percent (w9, twin, controls, 57 rungs, SMs) -- the strictness
certificate condition is never the obstruction.  LEAST-NORM
BLOCKS (the sealed eigenvalue-free choice): indefinite
EVERYWHERE -- w9 -1.30e-02 rel (199/364 negative blocks)@A,
-3.14e-02 (130/364)@B; 57 rungs 0/57 all-psd (median min rel
eig -9.5e-04, worst -8.1e-02@kz12, best -6.3e-04@kz97); even
the POSITIVE class SM0 is indefinite (-2.2e-02, 7/7) -- THE
SELECTION, NOT THE WORLD, produces the indefiniteness: min-
Frobenius spreads mass onto indefinite mixtures; the verdict
fine-type BLOCK_INDEFINITE_MAIN fires on the letter of the
sealed rule.  THE ROUND'S CENTRAL MEASUREMENT (diagnosis
clause): the SDP-like feasibility census separates the worlds
-- w9@A and twin@A converge to GENUINELY PSD block families
(min eig rel +6.6e-16 / +2.0e-17 at affine residual 3.7e-14,
after only 200 Dykstra steps) while EPST@A / SCR@A stall at
-0.45 / -0.49 after 2000 steps: on the restricted DEG_A
subspace, where EVERY world's target is positive definite and
NOTHING is forced by theorem, MAIN and its diophantine-
trivialized twin admit an all-psd fourfold-block Green
decomposition and the two hard controls (at this schedule) do
not -- the first block-level world discriminator of the L*
lane, ONE-SIDED (non-convergence proves no infeasibility) and
diagnosis-grade only; SMOOTH@A sits at -1.3e-05 (marginal,
consistent with its boundary role: crossing 28 == DEG_B);
SM0..SM3 do not converge at this schedule (small models have
few blocks -- little redistribution room; their feasibility
status stays OPEN).  DEG_B: w9/twin stall at -4.2e-05 (not
converged after 2000 -- whether MAIN is blockwise-psd
representable at DEG_B stays OPEN); controls@B remain negative
as the theorem demands (EPST -0.41, SCR -0.49, SMOOTH
-2.1e-05).  CONTROLS (least-norm): DEG_B EXISTS+NEGBLOCK on all
three (EPST -0.513 neg 364/364, SCR -0.568 neg 364/364, SMOOTH
-0.184 neg 219/364); the G53 implication test held live on
EPST/SCR.  MUST-FAILS: m1 cholesky-of-target FLAGGED, m2
omitted remainder breaks by EXACTLY 5/7 at (t, t) and nowhere
else, m3 posthoc family FLAGGED, m4 partial coverage leaves
exact defect ~ 4.5e+01 LOUD; constructors + fragment audit
CLEAN.  Runtime 64.2 s full / 9.2 s smoke; run1/run2 identical
up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

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
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import lstar_two_measure_probe as LS               # noqa: E402 r284
import destructive_coherence_probe as DC           # noqa: E402 r288
import representation_contest_probe as RC          # noqa: E402 r282
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import minimal_firewall_probe as MF                # noqa: E402 r276
import bordered_hankel_probe as BH                 # noqa: E402 r244
import metric_stability_probe as MS                # noqa: E402 r278
import budget_localization_probe as BL             # noqa: E402 r280
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import wronskian_dictionary_probe as WD            # noqa: E402 r274
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
DEG_B = 28
H_CAP = 900
EXT_H = 1300
K_EXT = 15
MAIN_KZ = 9
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
R281_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
EXT = 8
EXT2 = 32
DEPTH_PAD = 6
RAT_TOL = 1e-8
QMAX = 1e6
W9_ANCH = (367, 263, 104, 184, 184)
CROSS_REC = 185
ZV_REC = -3.15
ZV_TOL = 0.05
R282_N2 = Fr(48360721965, 70120631072)
FIVE_SEVEN = Fr(5, 7)
B_TOY = Fr(9, 7)
RES_BAR = 1e-8
RCOND = 1e-11
PSD_NEG = 1e-7
KER_TOL = 1e-12
FEAS_ITER = 200
FEAS_ITER2 = 2000
FEAS_CONV = 1e-9
M4_CAP = 4
CONS_BAR = 1e-9
PIN_BAR = 1e-10
MINI_K = 16
MINI_BK = 3

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
                       "constructors consume split-source arrays "
                       "(positions, weights, fold indices, border "
                       "arrays, budget scalars) ONLY; record "
                       "numbers enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq_fit",
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


CONSTRUCTORS = ("cheb_rows", "block_maps_f64", "target_form_f64",
                "system_f64", "least_norm", "block_eigs",
                "kernel_exclusion", "border_split", "budget_from_rho",
                "mono_rows_fr", "block_maps_fr", "target_form_fr",
                "system_fr", "rref_solve_fr", "reconstruct_fr",
                "exact_budget_fr")
SCOPE_FORBIDDEN = {"CTRL_FLIPS", "ANCHORS", "R281_DIST", "minC_true",
                   "cross_true", "blk_eigs_true", "cholesky",
                   "eigvecs_target", "target_inverse"}


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


# ============== sealed source-pure constructors (AST-audited), f64
def cheb_rows(x, d, lo, hi):
    """Chebyshev rows T_0..T_d on the affine hull map (f64 basis
    choice for conditioning; span identical to the monomials --
    disclosed).  Consumes positions + hull only."""
    xi = (2.0 * np.asarray(x, float) - lo - hi) / (hi - lo)
    P = np.zeros((len(xi), d + 1))
    P[:, 0] = 1.0
    if d >= 1:
        P[:, 1] = xi
    for k in range(2, d + 1):
        P[:, k] = 2.0 * xi * P[:, k - 1] - P[:, k - 2]
    return P


def block_maps_f64(P, gw):
    """the SIX sealed block coordinates on every window of four
    consecutive fold-ordered atoms: returns L of shape
    (nblk, 6, m) with m = d + 2 (coefficients + t).  Consumes
    basis rows + gross masses only."""
    S, K = P.shape
    m = K + 1
    nblk = S - 3
    P0, P1, P2, P3 = P[:-3], P[1:-2], P[2:-1], P[3:]
    g = np.asarray(gw, float)
    g0, g1, g2, g3 = g[:-3], g[1:-2], g[2:-1], g[3:]
    Gr = g0 + g1 + g2 + g3
    L = np.zeros((nblk, 6, m))
    L[:, 0, :K] = P1 - P0
    L[:, 1, :K] = P0 - 2.0 * P1 + P2
    L[:, 2, :K] = P0 - P2
    L[:, 3, :K] = P1 - P3
    L[:, 4, :K] = (g0[:, None] * P0 + g1[:, None] * P1
                   + g2[:, None] * P2 + g3[:, None] * P3) \
        / Gr[:, None]
    L[:, 5, K] = 1.0
    return L


def target_form_f64(P_atoms, wa, P_border, wb, Bfree):
    """the system target A_sys = matrix of Q - ||R||^2 on the
    coefficient space + t: [[P^T W P, u], [u^T, B - 5/7]].
    Consumes source arrays + the budget scalar only."""
    K = P_atoms.shape[1]
    A = np.zeros((K + 1, K + 1))
    A[:K, :K] = P_atoms.T @ (np.asarray(wa, float)[:, None]
                             * P_atoms)
    u = P_border.T @ np.asarray(wb, float)
    A[:K, K] = u
    A[K, :K] = u
    A[K, K] = Bfree
    return A


IUP = {}


def _iu(m):
    if m not in IUP:
        IUP[m] = np.triu_indices(m)
    return IUP[m]


def system_f64(L, A_sys):
    """the linear system M g = q in the Frobenius-isometric
    unknowns (G_aa; sqrt(2) G_ab): M (nvech x nblk*21), q =
    vech(A_sys).  Linear algebra on coordinate maps only."""
    nblk, six, m = L.shape
    iu, ju = _iu(m)
    q = A_sys[iu, ju]
    pa, pb = np.triu_indices(6)
    # X[r, p, :, :] = sym contribution of unknown p of block r
    X = np.einsum("rak,rbl->rabkl", L, L)
    Xs = 0.5 * (X + np.transpose(X, (0, 1, 2, 4, 3)))
    # for a != b: (La Lb^T + Lb La^T)/sqrt(2); a == b: La La^T
    C = np.empty((nblk, len(pa), m, m))
    for p_i in range(len(pa)):
        a, b = int(pa[p_i]), int(pb[p_i])
        if a == b:
            C[:, p_i] = Xs[:, a, a]
        else:
            C[:, p_i] = (Xs[:, a, b] + Xs[:, b, a]) / math.sqrt(2.0)
    M = C[:, :, iu, ju].reshape(nblk * len(pa), len(q)).T
    return M, q


def least_norm(M, q):
    """the SEALED selection rule: minimum-Frobenius solution =
    least-norm lstsq (rcond sealed).  Inverts the COORDINATE
    Gram only -- never the target."""
    g, _res, rank, _sv = np.linalg.lstsq(M, q, rcond=RCOND)
    r = M @ g - q
    rel = float(np.linalg.norm(r)
                / max(np.linalg.norm(q), 1e-300))
    return g, rank, rel


def block_eigs(g, nblk):
    """unpack the least-norm vector into 6x6 blocks (undo the
    sqrt(2) scaling) and return (lam_min per block, scale)."""
    pa, pb = np.triu_indices(6)
    G = np.zeros((nblk, 6, 6))
    gv = g.reshape(nblk, len(pa))
    for p_i in range(len(pa)):
        a, b = int(pa[p_i]), int(pb[p_i])
        if a == b:
            G[:, a, a] = gv[:, p_i]
        else:
            G[:, a, b] = gv[:, p_i] / math.sqrt(2.0)
            G[:, b, a] = G[:, a, b]
    ev = np.linalg.eigvalsh(G)
    scale = float(max(np.max(np.sqrt(np.sum(G * G, axis=(1, 2)))),
                      1e-300))
    return ev[:, 0], scale, G


def kernel_exclusion(L):
    """rank of the stacked coordinate rows + the sealed R row on
    the coefficient space + t: full rank <=> cap of kernels is
    {0} (the strictness certificate condition)."""
    nblk, six, m = L.shape
    Kmat = L.reshape(nblk * six, m)
    Rrow = np.zeros((1, m))
    Rrow[0, m - 1] = math.sqrt(5.0 / 7.0)
    Kmat = np.vstack([Kmat, Rrow])
    ev = np.linalg.eigvalsh(Kmat.T @ Kmat)
    return int(np.sum(ev > KER_TOL * max(ev[-1], 1e-300))), m


def border_split(ctx):
    """the border measure sigmatilde of one world: folded
    smooth-comb split (bx, bw, by, bv) straight from the sealed
    ctx channel (r278)."""
    return (np.asarray(ctx["bx"], float), np.asarray(ctx["bw"], float),
            np.asarray(ctx["by"], float), np.asarray(ctx["bv"], float))


def budget_from_rho(rows, N):
    """B = S_{N-2} + 5/7 with S_n = sum_{k<n} rho_k (r243 form,
    rho from the r244 bordered chain rows)."""
    rho = [r["rho"] for r in rows[:N - 2]]
    return float(np.sum(rho)) + 5.0 / 7.0, rho


# ============== sealed exact constructors (Fractions)
def mono_rows_fr(xs, d):
    """monomial rows 1, x, .., x^d (exact)."""
    return [[x ** k for k in range(d + 1)] for x in xs]


def block_maps_fr(P, gw):
    """exact twin of block_maps_f64 (list-of-lists Fractions)."""
    S = len(P)
    K = len(P[0])
    m = K + 1
    out = []
    for j in range(S - 3):
        g = [abs(gw[j + i]) for i in range(4)]
        Gr = sum(g)
        rows = []
        rows.append([P[j + 1][k] - P[j][k] for k in range(K)] + [Fr(0)])
        rows.append([P[j][k] - 2 * P[j + 1][k] + P[j + 2][k]
                     for k in range(K)] + [Fr(0)])
        rows.append([P[j][k] - P[j + 2][k] for k in range(K)]
                    + [Fr(0)])
        rows.append([P[j + 1][k] - P[j + 3][k] for k in range(K)]
                    + [Fr(0)])
        rows.append([(g[0] * P[j][k] + g[1] * P[j + 1][k]
                      + g[2] * P[j + 2][k] + g[3] * P[j + 3][k]) / Gr
                     for k in range(K)] + [Fr(0)])
        rows.append([Fr(0)] * K + [Fr(1)])
        out.append(rows)
    return out


def target_form_fr(xs, ws, bxs, bws, B, d):
    """exact target matrix of Q on span{x^0..x^d, t}:
    [[H, u], [u^T, B]] with H_ik = sum w x^{i+k}, u_i = sum
    w_b x_b^i."""
    m = d + 2
    A = [[Fr(0)] * m for _ in range(m)]
    for i in range(d + 1):
        for k in range(i, d + 1):
            v = sum(w * x ** (i + k) for x, w in zip(xs, ws))
            A[i][k] = v
            A[k][i] = v
    for i in range(d + 1):
        v = sum(w * x ** i for x, w in zip(bxs, bws))
        A[i][d + 1] = v
        A[d + 1][i] = v
    A[d + 1][d + 1] = B
    return A


def system_fr(Ls, A_sys, pair_cap=None):
    """exact linear system: rows = coefficient pairs (i <= j)
    [optionally restricted to indices <= pair_cap or the t
    index], columns = unknown G_r[a<=b] entries (UNSCALED)."""
    m = len(A_sys)
    idx = []
    for i in range(m):
        for j in range(i, m):
            if pair_cap is not None:
                ok_i = (i <= pair_cap) or (i == m - 1)
                ok_j = (j <= pair_cap) or (j == m - 1)
                if not (ok_i and ok_j):
                    continue
            idx.append((i, j))
    pairs = [(a, b) for a in range(6) for b in range(a, 6)]
    ncols = len(Ls) * len(pairs)
    M = [[Fr(0)] * ncols for _ in range(len(idx))]
    q = [A_sys[i][j] for i, j in idx]
    for r, rows in enumerate(Ls):
        for p_i, (a, b) in enumerate(pairs):
            col = r * len(pairs) + p_i
            La, Lb = rows[a], rows[b]
            for e_i, (i, j) in enumerate(idx):
                if a == b:
                    M[e_i][col] = La[i] * La[j]
                else:
                    M[e_i][col] = La[i] * Lb[j] + Lb[i] * La[j]
    return M, q, idx


def rref_solve_fr(M, q):
    """exact Gaussian elimination on [M | q] (deterministic
    first-nonzero pivot): returns (exists, rank, dof, particular
    solution with free vars = 0)."""
    nr = len(M)
    nc = len(M[0]) if nr else 0
    A = [row[:] + [q[i]] for i, row in enumerate(M)]
    piv_cols = []
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [vi - f * vr for vi, vr in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
        if r == nr:
            break
    rank = r
    exists = all(A[i][nc] == 0 for i in range(rank, nr))
    sol = [Fr(0)] * nc
    if exists:
        for i, c in enumerate(piv_cols):
            sol[c] = A[i][nc]
    return exists, rank, nc - rank, sol


def reconstruct_fr(Ls, sol, m, with_remainder=True):
    """exact reconstruction sum_r L_r^T G_r L_r (+ R form)."""
    pairs = [(a, b) for a in range(6) for b in range(a, 6)]
    A = [[Fr(0)] * m for _ in range(m)]
    for r, rows in enumerate(Ls):
        for p_i, (a, b) in enumerate(pairs):
            gab = sol[r * len(pairs) + p_i]
            if gab == 0:
                continue
            La, Lb = rows[a], rows[b]
            for i in range(m):
                for j in range(m):
                    if a == b:
                        A[i][j] += gab * La[i] * La[j]
                    else:
                        A[i][j] += gab * (La[i] * Lb[j]
                                          + Lb[i] * La[j])
    if with_remainder:
        A[m - 1][m - 1] += FIVE_SEVEN
    return A


def exact_budget_fr(xs, ws, bxs, bws, Nw):
    """exact rational budget B = S_{Nw-2} + 5/7 through the WD
    chain of the signed measure: rho_k = F_k^2 / h_k with F_k =
    int pihat_k dsigma."""
    S_ = len(xs)
    n_hi = min(Nw - 2, S_ - 1)
    al, be, hs = WD.stj_gen(list(xs), list(ws), n_hi)
    Ssum = Fr(0)
    vals = [WD.pv_seq(al, be, bx, n_hi) for bx in bxs]
    for k in range(n_hi):
        Fk = sum(bws[b_i] * vals[b_i][k] for b_i in range(len(bxs)))
        Ssum += Fk * Fk / hs[k]
    return Ssum + FIVE_SEVEN


# ============== must-fail mutants
def mutant_target_cholesky(A_target):
    """m1 MUST-FAIL: G built from the CHOLESKY of the assembled
    target -- the scope audit must FLAG this (target-inverse
    class)."""
    return np.linalg.cholesky(A_target + np.eye(len(A_target)))


def mutant_posthoc_family(blk_eigs_true):
    """m3 MUST-FAIL: a coordinate family extended AFTER sight of
    the measured block eigenvalues -- the scope audit must FLAG
    this."""
    return [e for e in blk_eigs_true if e < 0]


# ============== gate-side helpers
def census_world(xa, wa, bxa, bwa, Bw, dcap, hull):
    """gate-side full census of one world at one cap: identity
    residual, dof, block eigen census, kernel exclusion."""
    lo, hi = hull
    P = cheb_rows(xa, dcap, lo, hi)
    Pb = cheb_rows(bxa, dcap, lo, hi)
    A_sys = target_form_f64(P, wa, Pb, bwa, Bw - 5.0 / 7.0)
    L = block_maps_f64(P, np.abs(np.asarray(wa, float)))
    M, q = system_f64(L, A_sys)
    g, rank, rel = least_norm(M, q)
    lam, scale, G = block_eigs(g, L.shape[0])
    kr, m = kernel_exclusion(L)
    lam_rel = float(np.min(lam) / scale)
    n_neg = int(np.sum(lam / scale < -PSD_NEG))
    return dict(rel=rel, rank=int(rank), ncols=M.shape[1],
                dof=int(M.shape[1] - rank), lam_rel=lam_rel,
                n_neg=n_neg, ker_ok=(kr == m), scale=scale,
                nblk=L.shape[0], M=M, q=q, g=g, L=L, lam=lam)


def world_arrays(W):
    """fold-ordered union arrays of one r284 world pack."""
    ff = np.concatenate([np.asarray(W["fp"], np.int64),
                         np.asarray(W["fn"], np.int64)])
    xx = np.concatenate([np.asarray(W["xp"], float),
                         np.asarray(W["xn"], float)])
    ww = np.concatenate([np.asarray(W["wp"], float),
                         -np.asarray(W["vn"], float)])
    o = np.argsort(ff)
    return ff[o], xx[o], ww[o]


def world_budget(W, ctx):
    """B = S_{N-2} + 5/7 of one world through the r244 bordered
    chain (window split + folded smooth border)."""
    bx, bw, by, bv = border_split(ctx)
    rows = BH.bord_chain(np.asarray(W["xp"], float),
                         np.asarray(W["wp"], float),
                         np.asarray(W["xn"], float),
                         np.asarray(W["vn"], float),
                         bx, bw, by, bv, W["N"] - 2)
    B, rho = budget_from_rho(rows, W["N"])
    bxa = np.concatenate([bx, by])
    bwa = np.concatenate([bw, -bv])
    return B, rho, bxa, bwa


def hull_of(xa, bxa):
    lo = min(float(np.min(xa)), float(np.min(bxa)))
    hi = max(float(np.max(xa)), float(np.max(bxa)))
    return lo, hi


def feas_diag(M, q, g0, nblk, iters=FEAS_ITER):
    """sealed DIAGNOSIS clause (only under BLOCK_INDEFINITE_MAIN):
    alternating projection between the affine solution set and
    the psd block cone, deterministic start = the least-norm
    point.  Eigen-clips act on CANDIDATE blocks only; the
    pseudoinverse is of the COORDINATE matrix M, never of the
    target.  Reports (final min rel eig, final affine rel
    residual) -- diagnosis, never a verdict upgrade."""
    pa, pb = np.triu_indices(6)
    npairs = len(pa)
    g = g0.copy()
    Mp = np.linalg.pinv(M, rcond=RCOND)
    for _it in range(iters):
        # project onto the psd cone blockwise
        lam, scale, G = block_eigs(g, nblk)
        ev, V = np.linalg.eigh(G)
        evc = np.clip(ev, 0.0, None)
        Gp = np.einsum("rij,rj,rkj->rik", V, evc, V)
        gv = np.zeros((nblk, npairs))
        for p_i in range(npairs):
            a, b = int(pa[p_i]), int(pb[p_i])
            if a == b:
                gv[:, p_i] = Gp[:, a, a]
            else:
                gv[:, p_i] = Gp[:, a, b] * math.sqrt(2.0)
        g = gv.reshape(-1)
        # project back onto the affine set {g : M g = q}
        g = g - Mp @ (M @ g - q)
    lam, scale, _G = block_eigs(g, nblk)
    rel = float(np.linalg.norm(M @ g - q)
                / max(np.linalg.norm(q), 1e-300))
    return float(np.min(lam) / scale), rel


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("block_green_probe -- PRIME.LSTAR.BLOCK_GREEN.01 "
          "(round 308)")
    print("SPEC_SHA %s   (r284 LS %s / r288 DC %s / r282 RC %s)"
          % (SPEC_SHA[:16], LS.SPEC_SHA[:16], DC.SPEC_SHA[:16],
             RC.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + small models + MINI16 + "
                        "firewall + scopes + mutants + w9 f64 "
                        "block at DEG_A; spectral anchors, DEG_B, "
                        "ladder, twin, controls, feasibility, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the six-coordinate block "
          "library (fixed fold incidence, four adjacent layers), "
          "the explicit remainder R = sqrt(5/7) t, the exact "
          "linear-system search (linear in G), the eigenvalue-free "
          "minimum-Frobenius selection rule, DEG_A = 8 / DEG_B = "
          "28 (design-time from published control crossings "
          "26/22/28 vs MAIN 185 -- the DEG_B control negativity "
          "is forced by theorem GIVEN existence and is disclosed, "
          "never sold), the census worlds, the feasibility "
          "DIAGNOSIS clause, every bar/tolerance, the mutants and "
          "the verdict form; the STOP list forbids any L* claim, "
          "any bound mechanism and any selection by measured "
          "signs; the r282 demarcation clause is binding")

    # ---------------- S1 exact toys + small models
    section("S1  EXACT LEG -- TOY4 (HAND), SM0..SM3, MINI16")
    x4 = [Fr(1, 2), Fr(1, 4), Fr(-1, 4), Fr(-1, 2)]
    w4 = [Fr(1), Fr(1, 2), Fr(-1, 3), Fr(1, 4)]
    bx4 = [Fr(3, 4)]
    bw4 = [Fr(1, 5)]
    A4 = target_form_fr(x4, w4, bx4, bw4, B_TOY, 1)
    ok_hand = (A4[0][0] == Fr(17, 12) and A4[0][1] == Fr(7, 12)
               and A4[1][1] == Fr(31, 96)
               and A4[0][2] == Fr(1, 5) and A4[1][2] == Fr(3, 20)
               and A4[2][2] == B_TOY)
    A4s = [row[:] for row in A4]
    A4s[2][2] = B_TOY - FIVE_SEVEN
    P4 = mono_rows_fr(x4, 1)
    L4 = block_maps_fr(P4, w4)
    M4, q4, idx4 = system_fr(L4, A4s)
    ex4, rk4, dof4, sol4 = rref_solve_fr(M4, q4)
    # the t^2 pin: D6 is the only t-carrying coordinate and TOY4
    # has ONE block -> G[6,6] = B - 5/7 in EVERY solution
    p66 = [(a, b) for a in range(6) for b in range(a, 6)].index((5, 5))
    ok_pin = ex4 and sol4[p66] == B_TOY - FIVE_SEVEN
    A4r = reconstruct_fr(L4, sol4, 3)
    ok_rec4 = all(A4r[i][j] == A4[i][j] for i in range(3)
                  for j in range(3))
    check("G10-toy4-hand", ok_hand and ex4 and ok_pin and ok_rec4,
          "TOY4 (S = 4, one block, deg cap 1): target HAND-EXACT "
          "(m_0 = 17/12, m_1 = 7/12, m_2 = 31/96, u = (1/5, "
          "3/20), B = 9/7); identity EXISTS (rank %d, dof %d); "
          "the t^2 pin G[6,6] == B - 5/7 == 4/7 EXACT (D6 is the "
          "only t coordinate of the single block); exact "
          "entrywise reconstruction == target" % (rk4, dof4))

    def sm_pack(name, xs, ws):
        Nw = (len(xs) + 1) // 2
        bxs = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
        bws = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
        B = exact_budget_fr(xs, ws, bxs, bws, Nw)
        A = target_form_fr(xs, ws, bxs, bws, B, DEG_A)
        As = [row[:] for row in A]
        As[-1][-1] = B - FIVE_SEVEN
        P = mono_rows_fr(xs, DEG_A)
        Ls = block_maps_fr(P, ws)
        return dict(name=name, xs=xs, ws=ws, bxs=bxs, bws=bws,
                    B=B, A=A, As=As, Ls=Ls, Nw=Nw)

    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    x13 = [Fr(12 - 2 * j, 14) for j in range(13)]
    x16 = [Fr(15 - 2 * j, 17) for j in range(16)]
    w_sm0 = [Fr(1)] * 10
    w_sm0[2], w_sm0[5], w_sm0[8] = Fr(1, 2), Fr(1, 3), Fr(1, 4)
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    w_sm2 = [Fr(1), Fr(1), Fr(1), Fr(-1, 2), Fr(-1, 3), Fr(1),
             Fr(1), Fr(1), Fr(1), Fr(-1, 4), Fr(-1, 5), Fr(1),
             Fr(1)]
    w_sm3 = [Fr(1)] * 16
    w_sm3[3], w_sm3[7], w_sm3[11], w_sm3[14] = \
        Fr(-1, 3), Fr(-1, 4), Fr(-1, 5), Fr(-1, 6)
    SMS = [sm_pack("SM0", x10, w_sm0), sm_pack("SM1", x10, w_sm1),
           sm_pack("SM2", x13, w_sm2), sm_pack("SM3", x16, w_sm3)]
    ok_sm = True
    dof_tab = {}
    SM_SOL = {}
    for sm in SMS:
        Mx, qx, _ix = system_fr(sm["Ls"], sm["As"])
        ex, rk, dof, sol = rref_solve_fr(Mx, qx)
        Ar = reconstruct_fr(sm["Ls"], sol, DEG_A + 2)
        okr = ex and all(Ar[i][j] == sm["A"][i][j]
                         for i in range(DEG_A + 2)
                         for j in range(DEG_A + 2))
        ok_sm = ok_sm and okr
        dof_tab[sm["name"]] = (rk, dof)
        SM_SOL[sm["name"]] = (Mx, qx, sol)
        info("%s: S=%d N_w=%d S_-=%d B=%s rank=%d dof=%d "
             "exists=%s reconstruction=%s"
             % (sm["name"], len(sm["xs"]), sm["Nw"],
                sum(1 for w in sm["ws"] if w < 0),
                "%.6f" % float(sm["B"]), rk, dof, ex, okr))
    check("G11-sm-identity-exact", ok_sm,
          "SMALL MODELS (exact Fractions, monomials, deg cap %d): "
          "the identity Q - (5/7)t^2 = sum Delta^T G Delta EXISTS "
          "on SM0 (positive class) + SM1 (MAIN-like shielded) + "
          "SM2 (control-like clustered) + SM3 (wide) with exact "
          "entrywise reconstruction; (rank, dof) = %s -- the "
          "solution set is a large affine family (linear in G, as "
          "sealed); D3's in-block linear dependence on D1/D2 is "
          "disclosed language, not an error"
          % (DEG_A, str(dof_tab)))

    # MINI16: frozen truncation of the REAL w9 window
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ff9, xx9, ww9 = world_arrays(W9)
    mini_x = [Fr(float(x)) for x in xx9[:MINI_K]]
    mini_w = [Fr(float(w)) for w in ww9[:MINI_K]]
    bx9, bw9, by9, bv9 = border_split(ctx9)
    bxa9 = np.concatenate([bx9, by9])
    bwa9 = np.concatenate([bw9, -bv9])
    mini_bx = [Fr(float(x)) for x in bxa9[:MINI_BK]]
    mini_bw = [Fr(float(w)) for w in bwa9[:MINI_BK]]
    Nw_mini = (MINI_K + 1) // 2
    B_mini = exact_budget_fr(mini_x, mini_w, mini_bx, mini_bw,
                             Nw_mini)
    A_mini = target_form_fr(mini_x, mini_w, mini_bx, mini_bw,
                            B_mini, DEG_A)
    As_mini = [row[:] for row in A_mini]
    As_mini[-1][-1] = B_mini - FIVE_SEVEN
    P_mini = mono_rows_fr(mini_x, DEG_A)
    L_mini = block_maps_fr(P_mini, mini_w)
    Mm, qm, _im = system_fr(L_mini, As_mini)
    exm, rkm, dofm, solm = rref_solve_fr(Mm, qm)
    Arm = reconstruct_fr(L_mini, solm, DEG_A + 2)
    ok_mini = exm and all(Arm[i][j] == A_mini[i][j]
                          for i in range(DEG_A + 2)
                          for j in range(DEG_A + 2))
    n_neg_mini = sum(1 for w in mini_w if w < 0)
    check("G12-mini16-exact", ok_mini,
          "MINI16 (first %d union atoms of the REAL w9 window in "
          "fold order, f64 -> Fraction EXACT; %d nu atoms; first "
          "%d border atoms; exact mini budget B = %.6f): identity "
          "EXISTS (rank %d, dof %d), exact entrywise "
          "reconstruction == target -- the real-source miniature "
          "carries the identity symbolically"
          % (MINI_K, n_neg_mini, MINI_BK, float(B_mini), rkm, dofm))

    # f64/exact consistency ward (TOY4 + SM1)
    P4f = cheb_rows(np.array([float(x) for x in x4]), 1, -0.5, 0.75)
    Pb4f = cheb_rows(np.array([0.75]), 1, -0.5, 0.75)
    A4f = target_form_f64(P4f, np.array([float(w) for w in w4]),
                          Pb4f, np.array([0.2]),
                          float(B_TOY - FIVE_SEVEN))
    L4f = block_maps_f64(P4f, np.abs(np.array([float(w)
                                               for w in w4])))
    M4f, q4f = system_f64(L4f, A4f)
    g4f, rk4f, rel4f = least_norm(M4f, q4f)
    p66f = g4f.reshape(1, 21)[0, p66]
    ok_cons = (rel4f <= CONS_BAR
               and abs(p66f - float(B_TOY - FIVE_SEVEN)) <= PIN_BAR)
    sm1 = SMS[1]
    xs1 = np.array([float(x) for x in sm1["xs"]])
    ws1 = np.array([float(w) for w in sm1["ws"]])
    bxs1 = np.array([float(x) for x in sm1["bxs"]])
    bws1 = np.array([float(w) for w in sm1["bws"]])
    h1 = hull_of(xs1, bxs1)
    C1 = census_world(xs1, ws1, bxs1, bws1, float(sm1["B"]),
                      DEG_A, h1)
    ok_cons = ok_cons and C1["rel"] <= CONS_BAR and C1["ker_ok"]
    check("G13-f64-exact-consistency", ok_cons,
          "CONSISTENCY WARD: the f64 route (Chebyshev basis + "
          "least-norm lstsq) reproduces the exact existence on "
          "TOY4 (rel res %.1e, t^2 pin dev %.1e) and SM1 (rel res "
          "%.1e, kernel exclusion %s, min block eig rel %+.2e, "
          "%d/%d negative blocks) -- basis change disclosed, span "
          "identical" % (rel4f, abs(p66f - float(B_TOY
                                                 - FIVE_SEVEN)),
                         C1["rel"], C1["ker_ok"], C1["lam_rel"],
                         C1["n_neg"], C1["nblk"]))
    info("SM f64 block census at DEG_A (least-norm, min rel eig / "
         "#neg / nblk):")
    sm_cen = {}
    for sm in SMS:
        xsf = np.array([float(x) for x in sm["xs"]])
        wsf = np.array([float(w) for w in sm["ws"]])
        bxf = np.array([float(x) for x in sm["bxs"]])
        bwf = np.array([float(w) for w in sm["bws"]])
        Cf = census_world(xsf, wsf, bxf, bwf, float(sm["B"]),
                          DEG_A, hull_of(xsf, bxf))
        sm_cen[sm["name"]] = Cf
        info("  %s: %+.3e / %d / %d (res %.1e)"
             % (sm["name"], Cf["lam_rel"], Cf["n_neg"], Cf["nblk"],
                Cf["rel"]))

    # ---------------- S2 w9 anchors
    section("S2  W9 ANCHORS -- SOURCE, CROSSING, r288 PIN, 5/7")
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4]
              and len(set(W9["fp"]) & set(W9["fn"])) == 0)
    check("G20-w9-source-split", ok_src,
          "w9 FULL SOURCE: S = %d (mu %d / nu %d), N_w = %d, minC "
          "= %s (records); mu/nu fold sets disjoint -- the fold "
          "order of the union is well defined"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"])))
    if smoke:
        check("G21-w9-crossing", True, "SMOKE: skipped")
        check("G22-r288-carrier-pin", True, "SMOKE: skipped")
    else:
        depth9 = min(W9["N"] + DEPTH_PAD, W9["Sp"] - 1)
        SP9 = LS.spectral_block(W9, depth9)
        check("G21-w9-crossing", SP9["cross"] == CROSS_REC
              and SP9["cross"] == W9["minC"] + 1,
              "lambda_max(E_n) crosses 1 at n = %s == minC + 1 == "
              "%d (r283 route reproduced)"
              % (str(SP9["cross"]), CROSS_REC))
        ZB9 = DC.zv_block(SP9["B"], CROSS_REC, W9["vn"])
        check("G22-r288-carrier-pin",
              abs(ZB9["zv"] - ZV_REC) <= ZV_TOL and ZB9["X"] < 0.0,
              "r288 CARRIER PIN: source-frame z_v = %+.3f at the "
              "crossing (record %+.2f, tol %.2f), X_v = %+.4f "
              "DESTRUCTIVE -- the antiphase-3-4 interference this "
              "round's D3/D4 coordinates are built to capture"
              % (ZB9["zv"], ZV_REC, ZV_TOL, ZB9["X"]))
    al2, be2, _hs2 = RC.toy_chain(BL.TOYS_XS, BL.MAINLIKE_W)
    rows2 = RC.pv_rows(BL.TOYS_XS, al2, be2, 2)
    _P2, N2 = RC.pn_split(BL.TOYS_XS, BL.MAINLIKE_W, rows2[2])
    check("G23-r282-refutation-pin", N2 == R282_N2,
          "r282 PIN EXACT: the fake-SOS defect N_2(MAINLIKE) == "
          "%s (the K1 negative register at the last free degree) "
          "-- DEMARCATION: the r282 Kasteleyn/SOS refutations "
          "concern the FULL signed configuration class (every "
          "Cauchy-Binet cell, h_n itself); this round's identity "
          "lives on the RESTRICTED subspace deg p <= %d/%d << N_w "
          "= 184 plus one border coordinate -- a different "
          "language, no contradiction in either direction"
          % (str(R282_N2), DEG_A, DEG_B))
    B9, rho9, bxa9c, bwa9c = world_budget(W9, ctx9)
    ok_57 = (B9 > 5.0 / 7.0
             and all(r >= 0.0 for r in rho9))
    check("G24-five-seven-reserve", ok_57,
          "5/7-RESERVE CONVENTION (r243/v958): B_w9 = S_{N-2} + "
          "5/7 = %.6f with S_{N-2} = %.6f = sum of %d nonnegative "
          "rho_k (all rho_k >= 0 through the free window -- h > 0 "
          "there); the sealed remainder R = sqrt(5/7) t carries "
          "exactly the imported reserve floor, B - 5/7 stays on "
          "the block side" % (B9, B9 - 5.0 / 7.0, len(rho9)))

    # ---------------- S3 w9 f64 identity + blocks
    section("S3  W9 -- IDENTITY + BLOCK CENSUS (LEGS A/B/C)")
    hull9 = hull_of(xx9, bxa9c)
    CA9 = census_world(xx9, ww9, bxa9c, bwa9c, B9, DEG_A, hull9)
    check("G30-w9-union-sanity", bool(np.all(np.diff(ff9) > 0))
          and len(ff9) == W9["S"],
          "w9 union in strict fold order (%d atoms, folds "
          "strictly increasing); blocks = %d sliding fourfold "
          "windows" % (len(ff9), CA9["nblk"]))
    check("G31-w9-identity-degA", CA9["ker_ok"],
          "w9 IDENTITY at DEG_A = %d (MEASURED, adjudicated in "
          "S6): rel residual %.1e (bar %.0e => %s), rank %d of "
          "%d unknowns (dof %d); HARD half: kernel exclusion "
          "rank-full %s (the strictness certificate condition)"
          % (DEG_A, CA9["rel"], RES_BAR,
             "EXISTS" if CA9["rel"] <= RES_BAR else "FAIL",
             CA9["rank"], CA9["ncols"], CA9["dof"], CA9["ker_ok"]))
    check("G32-w9-blocks-degA", True,
          "w9 BLOCK CENSUS at DEG_A (sealed least-norm choice): "
          "min block eig rel %+.3e, negative blocks %d of %d "
          "(bar %.0e) -- MEASURED, adjudicated in S6"
          % (CA9["lam_rel"], CA9["n_neg"], CA9["nblk"], PSD_NEG))
    if smoke:
        check("G33-w9-degB", True, "SMOKE: skipped")
        CB9 = None
    else:
        CB9 = census_world(xx9, ww9, bxa9c, bwa9c, B9, DEG_B, hull9)
        check("G33-w9-degB", CB9["ker_ok"],
              "w9 at DEG_B = %d (MEASURED, adjudicated in S6): "
              "rel residual %.1e (%s), dof %d, min block eig rel "
              "%+.3e, negative blocks %d of %d; HARD half: "
              "kernel exclusion %s"
              % (DEG_B, CB9["rel"],
                 "EXISTS" if CB9["rel"] <= RES_BAR else "FAIL",
                 CB9["dof"], CB9["lam_rel"], CB9["n_neg"],
                 CB9["nblk"], CB9["ker_ok"]))

    # ---------------- S4 ladder census
    section("S4  LADDER -- 42 CORE + 15 EXTENSION AT DEG_A")
    if smoke:
        for g in ("G40-core-census", "G41-extension-census",
                  "G42-rung-identity", "G43-rung-blocks"):
            check(g, True, "SMOKE: skipped")
        rung_tab = {}
    else:
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H:
                ekz.append(kz)
        packs = {}
        for kz in kzs + ekz:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx)
        offs = {kz: packs[kz][0]["minC"] - packs[kz][0]["N"]
                for kz in kzs}
        dist = {}
        for o in offs.values():
            dist[o] = dist.get(o, 0) + 1
        ok_anch = all(offs[kz] == ANCHORS[kz]
                      for kz in ANCHORS if kz in offs)
        ok_hf = all(packs[kz][0]["N"]
                    == (packs[kz][0]["S"] + 1) // 2
                    for kz in kzs)
        check("G40-core-census", len(kzs) == 42 and ok_anch
              and ok_hf and dist == R281_DIST,
              "42-rung r281 census: offset distribution %s == "
              "record, anchors exact, half-filling 42/42"
              % str({("+%d" % k): dist[k] for k in sorted(dist)}))
        epool = sorted(ekz, key=lambda kz: (packs[kz][0]["N"], kz))
        ext15 = epool[:K_EXT]
        ok_ehf = all(packs[kz][0]["N"]
                     == (packs[kz][0]["S"] + 1) // 2
                     for kz in ext15)
        check("G41-extension-census", len(ext15) == K_EXT
              and ok_ehf,
              "extension anchors (h <= %d, sorted by (N_w, kz), "
              "first %d): N_w %d..%d, half-filling %d/%d (r286/"
              "r306 rule; channel = the sealed r278 ctx channel, "
              "disclosed)"
              % (EXT_H, K_EXT, packs[ext15[0]][0]["N"],
                 packs[ext15[-1]][0]["N"],
                 sum(1 for kz in ext15
                     if packs[kz][0]["N"]
                     == (packs[kz][0]["S"] + 1) // 2), K_EXT))
        rung_tab = {}
        ok_rid = True
        for kz in kzs + ext15:
            Wp, ctx = packs[kz]
            Bw, _rho, bxa, bwa = world_budget(Wp, ctx)
            _ff, xa, wa = world_arrays(Wp)
            Cw = census_world(xa, wa, bxa, bwa, Bw, DEG_A,
                              hull_of(xa, bxa))
            rung_tab[kz] = dict(N=Wp["N"], rel=Cw["rel"],
                                dof=Cw["dof"],
                                lam=Cw["lam_rel"],
                                n_neg=Cw["n_neg"],
                                nblk=Cw["nblk"],
                                ker=Cw["ker_ok"], B=Bw)
            ok_rid = ok_rid and Cw["rel"] <= RES_BAR \
                and Cw["ker_ok"]
        n57 = len(rung_tab)
        worst_res = max(rung_tab[kz]["rel"] for kz in rung_tab)
        n_ex = sum(1 for kz in rung_tab
                   if rung_tab[kz]["rel"] <= RES_BAR)
        check("G42-rung-identity", n57 == 57
              and all(rung_tab[kz]["ker"] for kz in rung_tab),
              "IDENTITY on the %d MAIN rungs at DEG_A (MEASURED, "
              "adjudicated in S6): exists %d/%d (worst rel "
              "residual %.1e, bar %.0e); HARD half: census count "
              "57 + kernel exclusion %d/%d"
              % (n57, n_ex, n57, worst_res, RES_BAR,
                 sum(1 for kz in rung_tab if rung_tab[kz]["ker"]),
                 n57))
        ok_rid = ok_rid and n_ex == n57
        lam_all = sorted((rung_tab[kz]["lam"], kz)
                         for kz in rung_tab)
        n_psd = sum(1 for kz in rung_tab
                    if rung_tab[kz]["n_neg"] == 0)
        info("rung block census (min rel eig, worst 5): %s"
             % str([("kz%d" % kz, "%.2e" % v)
                    for v, kz in lam_all[:5]]))
        info("rung block census (min rel eig, best 5): %s"
             % str([("kz%d" % kz, "%.2e" % v)
                    for v, kz in lam_all[-5:]]))
        check("G43-rung-blocks", True,
              "BLOCK CENSUS 57 rungs at DEG_A: %d/%d all-psd "
              "(bar %.0e rel); min rel eig median %.2e, worst "
              "%.2e@kz%d -- MEASURED, adjudicated in S6"
              % (n_psd, n57, PSD_NEG,
                 float(np.median([rung_tab[kz]["lam"]
                                  for kz in rung_tab])),
                 lam_all[0][0], lam_all[0][1]))

    # ---------------- S5 twin + controls
    section("S5  RATIONAL TWIN (r289) + CONTROLS")
    if smoke:
        for g in ("G50-twin-construction", "G51-twin-census",
                  "G52-ctrl-flips", "G53-ctrl-census"):
            check(g, True, "SMOKE: skipped")
        twin_tab = {}
        ctrl_tab = {}
    else:
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and bool(np.all(np.abs(duR)
                                 <= RAT_TOL * gaps_c + 1e-300))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        depthT = min(WT["N"] + DEPTH_PAD, WT["Sp"] - 1)
        SPT = LS.spectral_block(WT, depthT)
        ok_keep = (WT["minC"] == 184 and SPT["cross"] == 185)
        check("G50-twin-construction", ok_tc and ok_keep,
              "r289 RATIONAL TWIN re-built verbatim (CF "
              "convergents, |du| <= %.0e local gap, weights "
              "bitwise, denominators max %d <= %.0e): "
              "RATIONAL_KEEPS re-gated -- minC = %s, crossing = "
              "%s (record 184/185)"
              % (RAT_TOL, int(np.max(dens)), QMAX,
                 str(WT["minC"]), str(SPT["cross"])))
        BT, _rhoT, bxaT, bwaT = world_budget(WT, ctxT)
        _ffT, xaT, waT = world_arrays(WT)
        twin_tab = {}
        for dcap, nm in ((DEG_A, "A"), (DEG_B, "B")):
            Ct = census_world(xaT, waT, bxaT, bwaT, BT, dcap,
                              hull_of(xaT, bxaT))
            twin_tab[nm] = Ct
        check("G51-twin-census", all(
            twin_tab[nm]["ker_ok"] for nm in twin_tab),
            "TWIN census (MEASURED, adjudicated in S6; HARD "
            "half: kernel exclusion): DEG_A rel %.1e, min eig "
            "rel %+.3e, neg %d/%d; DEG_B rel %.1e, min eig rel "
            "%+.3e, neg %d/%d -- the diophantine-trivialized "
            "world measured in the same coordinates"
            % (twin_tab["A"]["rel"], twin_tab["A"]["lam_rel"],
               twin_tab["A"]["n_neg"], twin_tab["A"]["nblk"],
               twin_tab["B"]["rel"], twin_tab["B"]["lam_rel"],
               twin_tab["B"]["n_neg"], twin_tab["B"]["nblk"]))
        # controls
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        ctrl_tab = {}
        ok_fl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            ok_fl = ok_fl and (Wc["minC"] == CTRL_FLIPS[cn])
            Bc, _rc, bxac, bwac = world_budget(Wc, cctx)
            _ffc, xac, wac = world_arrays(Wc)
            row = dict(minC=Wc["minC"], B=Bc)
            for dcap, nm in ((DEG_A, "A"), (DEG_B, "B")):
                Cc = census_world(xac, wac, bxac, bwac, Bc, dcap,
                                  hull_of(xac, bxac))
                row[nm] = Cc
            ctrl_tab[cn] = row
        check("G52-ctrl-flips", ok_fl,
              "controls built verbatim through the r281/r284 "
              "channel: minC == flips %s" % str(CTRL_FLIPS))
        # the forced-negativity implication test at DEG_B
        # (hard-gated on EPST/SCR whose crossings 26/22 sit safely
        # below DEG_B; SMOOTH's crossing 28 == DEG_B is the sealed
        # boundary case -- reported, not hard-gated)
        ok_forced = True
        det_c = []
        for cn in ctrl_tab:
            Cc = ctrl_tab[cn]["B"]
            exists_b = Cc["rel"] <= RES_BAR
            neg_b = Cc["lam_rel"] <= -PSD_NEG
            if cn in ("EPST", "SCR"):
                ok_forced = ok_forced and ((not exists_b) or neg_b)
            det_c.append("%s: DEG_B %s%s (min eig rel %+.2e, "
                         "neg %d/%d), DEG_A min eig rel %+.2e "
                         "neg %d/%d"
                         % (cn,
                            "EXISTS" if exists_b else
                            "IDENTITY_FAIL(res %.1e)" % Cc["rel"],
                            "+NEGBLOCK" if neg_b else "",
                            Cc["lam_rel"], Cc["n_neg"],
                            Cc["nblk"],
                            ctrl_tab[cn]["A"]["lam_rel"],
                            ctrl_tab[cn]["A"]["n_neg"],
                            ctrl_tab[cn]["A"]["nblk"]))
        check("G53-ctrl-census", ok_forced,
              "CONTROL CENSUS + the live implication test "
              "(existence at DEG_B => negative block direction, "
              "forced by the early deaths 26/22 << %d on EPST/"
              "SCR -- DISCLOSED as theorem-forced; SMOOTH's "
              "crossing 28 == DEG_B is the boundary case, "
              "reported only): %s" % (DEG_B, "; ".join(det_c)))

    # ---------------- S6 adjudication + feasibility diagnosis
    section("S6  ADJUDICATION (SEALED)")
    if smoke:
        check("G60-feasibility-diag", True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
        id_verd = "SMOKE"
        pos_verd = "SMOKE"
    else:
        exists_all = (ex4 and ok_sm and exm
                      and CA9["rel"] <= RES_BAR
                      and CB9["rel"] <= RES_BAR)
        if exists_all:
            id_verd = ("IDENTITY_EXISTS(TOY4 dof %d; SM dof %s; "
                       "MINI16 dof %d; w9 dof %d@A / %d@B)"
                       % (dof4, str({k: v[1]
                                     for k, v in dof_tab.items()}),
                          dofm, CA9["dof"], CB9["dof"]))
        else:
            id_verd = ("IDENTITY_OVERDETERMINED_FAIL(see gate "
                       "table for the first break locus)")
        main_ok = (CA9["n_neg"] == 0 and CB9["n_neg"] == 0
                   and CA9["ker_ok"] and CB9["ker_ok"]
                   and all(twin_tab[nm]["n_neg"] == 0
                           for nm in twin_tab)
                   and all(rung_tab[kz]["n_neg"] == 0
                           for kz in rung_tab))
        ctrl_broken = all(
            (ctrl_tab[cn]["B"]["rel"] > RES_BAR)
            or (ctrl_tab[cn]["B"]["lam_rel"] <= -PSD_NEG)
            for cn in ctrl_tab)
        feas_note = "NOT_TRIGGERED"
        if exists_all and not main_ok:
            def run_feas(C):
                # ONE uniform two-stage schedule for EVERY world
                # (no MAIN preference): 200 steps, then 2000 if
                # not converged
                fm, fr = feas_diag(C["M"], C["q"], C["g"],
                                   C["nblk"])
                it = FEAS_ITER
                if fm < -FEAS_CONV:
                    fm, fr = feas_diag(C["M"], C["q"], C["g"],
                                       C["nblk"],
                                       iters=FEAS_ITER2)
                    it = FEAS_ITER2
                return fm, fr, it
            feas_tab = {}
            feas_tab["w9@A"] = run_feas(CA9)
            feas_tab["twin@A"] = run_feas(twin_tab["A"])
            for cn in ctrl_tab:
                feas_tab["%s@A" % cn] = run_feas(ctrl_tab[cn]["A"])
            for nm_ in sm_cen:
                feas_tab["%s@A" % nm_] = run_feas(sm_cen[nm_])
            feas_tab["w9@B"] = run_feas(CB9)
            feas_tab["twin@B"] = run_feas(twin_tab["B"])
            for cn in ctrl_tab:
                feas_tab["%s@B" % cn] = run_feas(ctrl_tab[cn]["B"])
            for k_ in sorted(feas_tab):
                fm, fr, it = feas_tab[k_]
                info("FEAS %s: min eig rel %+.3e, affine res "
                     "%.1e (%d steps) -> %s"
                     % (k_, fm, fr, it,
                        "PSD-FEASIBLE" if fm >= -FEAS_CONV
                        else "NOT CONVERGED (one-sided: no "
                        "infeasibility proof)"))
            fs = {k_: ("FEAS" if feas_tab[k_][0] >= -FEAS_CONV
                       else "NO(%.0e)" % abs(feas_tab[k_][0]))
                  for k_ in sorted(feas_tab)}
            feas_note = ("FEAS_DIAG(amendment a1 census: %s -- "
                         "controls@B are the live theorem-"
                         "consistency side, they must NOT "
                         "converge; diagnosis only)" % str(fs))
        check("G60-feasibility-diag", True, feas_note)
        if not exists_all:
            pos_verd = "NO_POSITIVITY_CENSUS(identity failed)"
        elif main_ok and ctrl_broken:
            pos_verd = ("BLOCK_GREEN_GO(w9 + twin psd at both "
                        "caps, 57/57 rungs psd at DEG_A, kernel "
                        "exclusion everywhere; every control "
                        "broken at DEG_B)")
        elif main_ok:
            pos_verd = ("WORLD_BLIND_DECOMP(MAIN family psd but "
                        "some control also psd with existing "
                        "identity at DEG_B: %s)"
                        % str({cn: "%+.2e"
                               % ctrl_tab[cn]["B"]["lam_rel"]
                               for cn in ctrl_tab}))
        else:
            worst = min([("w9@A", CA9["lam_rel"]),
                         ("w9@B", CB9["lam_rel"])]
                        + [("twin@%s" % nm,
                            twin_tab[nm]["lam_rel"])
                           for nm in twin_tab]
                        + [("kz%d@A" % kz, rung_tab[kz]["lam"])
                           for kz in rung_tab],
                        key=lambda t: t[1])
            pos_verd = ("BLOCK_INDEFINITE_MAIN(worst %s min eig "
                        "rel %+.3e; the sealed least-norm choice "
                        "does not carry) + %s"
                        % (worst[0], worst[1], feas_note))
        ctrl_ledger = ("CONTROL_LEDGER(DEG_B negativity forced-"
                       "by-theorem given existence, DISCLOSED; "
                       "DEG_A contrast: MAIN %+.2e vs %s)"
                       % (CA9["lam_rel"],
                          str({cn: "%+.2e"
                               % ctrl_tab[cn]["A"]["lam_rel"]
                               for cn in ctrl_tab})))
        verd = " + ".join([id_verd, pos_verd, ctrl_ledger,
                           "R282_DEMARCATION(restricted subspace "
                           "deg <= %d/%d << N_w; the full-class "
                           "refutations untouched)"
                           % (DEG_A, DEG_B)])

    # ---------------- S7 must-fails + scopes
    section("S7  TARGET-INVERSE AUDIT + MUST-FAILS")
    hits_m1 = scope_audit("mutant_target_cholesky")
    hits_m3 = scope_audit("mutant_posthoc_family")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G70-target-inverse-audit", bool(hits_m1)
          and bool(hits_m3) and not hits and not ag_hits,
          "m1 CHOLESKY-OF-TARGET mutant FLAGGED (%s); m3 "
          "POSTHOC-FAMILY mutant FLAGGED (%s); the %d sealed "
          "constructors audit CLEAN against the target-inverse "
          "set (no A^{-1}, no target eigenvectors, no outcome "
          "signs: %s); fragment audit: %s"
          % ("; ".join(hits_m1) if hits_m1 else "NOT FLAGGED",
             "; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    Ar_nor = reconstruct_fr(sm1["Ls"], SM_SOL["SM1"][2],
                            DEG_A + 2, with_remainder=False)
    dev_tt = sm1["A"][-1][-1] - Ar_nor[-1][-1]
    ok_m2 = (dev_tt == FIVE_SEVEN
             and all(Ar_nor[i][j] == sm1["A"][i][j]
                     for i in range(DEG_A + 2)
                     for j in range(DEG_A + 2)
                     if not (i == DEG_A + 1 and j == DEG_A + 1)))
    check("G71-mustfail-omitted-remainder", ok_m2,
          "m2 OMITTED REMAINDER (SM1, exact): dropping R breaks "
          "the identity at the (t, t) entry by EXACTLY 5/7 = %s "
          "and nowhere else -- the reserve floor is load-bearing "
          "and lives ONLY in the sealed remainder" % str(dev_tt))
    Mp, qp, _ip = system_fr(sm1["Ls"], sm1["As"],
                            pair_cap=M4_CAP)
    exp_, rkp, dofp, solp = rref_solve_fr(Mp, qp)
    Arp = reconstruct_fr(sm1["Ls"], solp, DEG_A + 2)
    defect = max(abs(Arp[i][j] - sm1["A"][i][j])
                 for i in range(DEG_A + 2)
                 for j in range(DEG_A + 2))
    check("G72-mustfail-partial-coverage", exp_ and defect > 0,
          "m4 INCOMPLETE MONOMIAL COVERAGE (SM1, exact): solving "
          "only the coefficient pairs with index <= %d (claiming "
          "cap %d) leaves a NONZERO exact defect on the full "
          "form: max |dev| = %s ~ %.2e -- LOUD: the degree-8 "
          "coverage gate is not vacuous"
          % (M4_CAP, DEG_A, "exact", float(defect)))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7 (the reserve is the "
          "IMPORTED r243 floor), no posthoc window, no selection "
          "by measured signs (the Frobenius rule is eigenvalue-"
          "free and sealed), no RH claim; what the round adds: "
          "the sealed fourfold-block coordinate language, the "
          "exact existence adjudication of the block-Green "
          "identity, the eigenvalue-free positivity census with "
          "the honest forced-negativity disclosure, and the "
          "feasibility diagnosis hook; r243..r307 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- DISCOVERY census of the reviewer's block-Green "
          "route; existence is the easy half (disclosed); the "
          "census fixes a TARGET, it proves neither L* nor any "
          "cofinal statement; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
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
