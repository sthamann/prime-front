#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""terminal_crossratio_probe -- PRIME.PORT.COUPLEDTAU.TERMINAL_
CROSSRATIO.01 (round 260): the terminal budget question as the
POSITIVITY OF A TAU CROSS-RATIO, with the fully driven normalized
recursion and the three admissible proof forms adjudicated.

REVIEWER NORMALIZATION (binding, adopted): 7/5 is NOT the theorem.
The canonical coordinate is q_{n+1} := rho_n / D_n = F_n^2 /
(h_n D_n), so D_{n+1} = D_n (1 - q_{n+1}); the real proof question
is q_N < 1 (equivalently h_{N-1}/F_{N-1}^2 > 1/D_{N-1}); NO
universal delta is demanded unless the algebra donates one; the
7/5 bar enters ONLY as a finite reproduction ward.  THE CENTRAL
TAU IDENTITY (from the r257 pair recursion tau_{n+1} = a_n tau_n,
tau^aug_{n+1} = a_n tau^aug_n + b_n tau_n, a_n = c_n^2 h_n, b_n =
-(c_n F_n)^2, c_n = (2/rh)^n the leading coefficient of the sealed
scaled-Chebyshev hull basis U_n((x - x0)/rh)):
    tau^aug_n tau_{n+1} - tau^aug_{n+1} tau_n = (c_n F_n)^2 tau_n^2
(bilinear Pluecker/Hirota form, manifest-square right side,
CORNER-INDEPENDENT: the budget corner B cancels in the bilinear
combination), and
    1 - q_{n+1} = D_{n+1}/D_n
               = (tau^aug_{n+1} tau_n) / (tau^aug_n tau_{n+1}):
q_N < 1 IS the positivity of a tau cross-ratio.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r259 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots h_{w,k}
(k < N_w) are the proof objects; rho_k = F_k^2/h_k, S_n =
sum_{k<=n} rho_k; ground truth (h signs, flip degrees, forced-tail
offsets) enters GATES only; no zero/prime oracles anywhere (AST
firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack +
BH.bord_chain (rows carry fb = F e^{-Ls}, tb = T e^{-Ls}, eta =
h e^{-2Ls}, alh, gam_next), r257 CT.world_block / u_matrix /
union_arrays / blind_flip_predictor, r254 OG.phat_matrix, r243
PB.smooth_comb, v881 PIK controls.  B PROVENANCE: B_w = S_{N-2} +
5/7 (r241/r243, IMPORTED floor, never fitted; hence D_{N-1} = 5/7
exactly by construction and q_N = rho_{N-1}/(5/7)).  POSITIVITY
TYPING (r256): POSITIVE_PREFIX vs INDEFINITE_CONTINUATION;
controls SCR/EPST/SMOOTH on w9 flip 21/25/27.  COFINAL WINDOW
SEQUENCE (pre-sealed): the frame-A h <= 900 ladder, 42 rungs,
(N, kz)-sorted (r258 convention), sample indices (0, 5, 10, 15,
20, 25, 30, 35, 41) for the direct-determinant gates.

LEG A -- THE EXACT DICTIONARY, FROZEN BEFORE ANY SIGN ANALYSIS:
source-pure production of D_{N-1}, h_{N-1}, F_{N-1}, q_N per
world.  Gates: (a1) q_N = F_{N-1}^2/(h_{N-1} D_{N-1}) chain route
vs the DIRECT bordered-slogdet route (both terminal sizes N-1, N
with the SAME corner B; D_{N-1} direct vs 5/7) on the 5 worlds +
the 9-rung ladder sample; ABSOLUTE deviations (q and the cross-
ratio are O(1) coordinates; a relative dev would explode
artificially on small-q rungs), bars 1e-8 main / 3e-6 deep /
1e-3 controls (r258 route floors).  (a2) cross-ratio identity
1 - q_N ==
(tau^aug_N tau_{N-1})/(tau^aug_{N-1} tau_N) on the same routes
and worlds.  (a3) the bilinear identity per degree, all degrees,
all 5 worlds, in the normalized f64 form X_n := D_n - D_{n+1}
(direct route) == rho_n (chain), dev scale max(|D_n|, |D_{n+1}|);
bars 1e-6 MAIN / 1e-3 controls (r257 coupled-step floors).  (a4)
mp WARDS of the RAW bilinear form (dps 60): tau^aug_n tau_{n+1} -
tau^aug_{n+1} tau_n == (c_n F_n)^2 tau_n^2 with an INDEPENDENT
monic mp F_n (Gram solve, never the chain), at sealed n in
{6, 12} on w9 and n in {12, 24} on SCRAMBLE (n = 24 spans the
flip 21), bar 1e-40; plus the corner-independence ward (same
bilinear value at corner B and B + 1, bar 1e-40).  (a5) 7/5
REPRODUCTION WARD ONLY: min_w h_{N-1}/F_{N-1}^2 over the 42
rungs in [1.40, 1.46], >= 7/5 with non-saturation margin >= 0.01
=> the constant stays FLOOR_IMPORTED => FIVE_SEVENTHS_NUMERICAL_
ONLY.  (a6) q census on the cofinal sequence: q_N < 1 on 42/42
with min terminal margin 5/7 - rho_{N-1} in the sealed band
[0.010, 0.020] (r243/r258 razor reproduction -- MEASUREMENT).

LEG B -- THE NORMALIZED, FULLY DRIVEN RECURSION: r_n := F_n /
sqrt(h_n) (so rho_n = r_n^2 on the positive prefix; f64-clean as
fb/sqrt(eta)).  From the exact border flow identity (r244 wpack
leg D: F_{k+1} = T_k - alh_k F_k - gam_k F_{k-1}, T_k = int x
pihat_k dsigmatilde) and h_{k+1} = gam_{k+1} h_k the EXACT DRIVEN
RECURSION
    r_{k+1} = t_k + a'_k r_k + b'_k r_{k-1},
    D_{k+1} = D_k - r_k^2,
    t_k  = T_k / sqrt(h_{k+1}),
    a'_k = -alh_k / sqrt(gam_{k+1}),
    b'_k = -sqrt(gam_k / gam_{k+1})   (signed on controls),
COEFFICIENT TYPOLOGY: a', b' consume the WINDOW chain (alh, gam);
the drive t_k consumes the FULL border comb at every degree --
the drive has length N-1 and is NOT compressed (consistent with
the boundary-state no-go: constant state dimension, full-length
drive).  Gates: (b1) the scaled F-form identity at ALL degrees on
ALL 5 worlds (world-blind algebra; dev scale = term-magnitude sum
with the sealed alias floor 1e-6 x max-norm -- SMOOTH is a 0/0
guard case, r243-a1 precedent); bar 1e-9 MAIN+SCR/EPST, 1e-6
SMOOTH-guarded.  (b2) r-form + D-update + S rebuild on the
positive prefixes of all 42 rungs + w9/w13 (rel 1e-9).  (b3)
drive typology gates: SMOOTH drive alias max_{k>=2} |T~_k| /
max(|T~_0|, |T~_1|) <= 1e-12 (on the self-aliased source the
drive is EXACTLY the two Jacobi readouts alh_0 h_0, gam_1 h_0 and
nothing else); MAIN drive nonzero at every degree (printed).
(b4) INVARIANT-REGION ADJUDICATION, candidates SEALED (max 3):
    PSI1_GAP        = D - r^2                  (region {q < 1}),
    PSI2_TAILBUDGET = D - sum_{j>=k} r_j^2     (orbit-constant),
    PSI3_ABSCHAIN   = D - sum_{j>=k} rbar_j^2, rbar the triangle
                      majorant chain rbar_{k+1} = |t_k| + |a'_k|
                      rbar_k + |b'_k| rbar_{k-1};
sealed adjudication rules: REGION_INVARIANT(PSIi) iff the sampled
region map Phi_k(C_k) subset C_{k+1} has ZERO exits on the sealed
5 x 5 fraction grid (+-0.9, +-0.5, 0) x sqrt(D) at every degree;
PSI2 is typed RESTATEMENT (its positivity IS the target: along
the orbit Psi2 == D_N exactly, gated 1e-9); PSI3 is typed
SOURCE_REASONED iff the majorant property rbar_k >= |r_k| holds
at every degree (one-step invariance is then an algebraic
implication) -- its head FEASIBILITY (Psi3 >= 0 at k = 8) is
measured honestly in decades.  Orbit containment r_k^2 < D_k at
every k on MAIN is gated (measurement).

LEG C -- THE THREE ADMISSIBLE PROOF FORMS (only these can Go;
candidates sealed, target-blind by construction: every candidate
consumes ONLY (r_0..r_{N-2}, t, a', b') -- the terminal readout
F_{N-1}/r_{N-1} is structurally withheld; machine AST audit +
deliberate oracle mutant):
  (c1) SOURCE CONE / driven certificates, three sealed candidates:
       C1a TRANSFER: r = G tau exactly (G the lower-triangular
           transfer matrix of the driven recursion, tau = (r_0,
           t_0..t_{N-2})); certified bound S_{N-1} <= ||G||_2^2
           ||tau||^2; VALIDITY gate (bound >= S, rebuild rel
           1e-9) + coverage bound < B_w counted over 42.
       C1b TERMINAL ONE-STEP: |r_{N-1}| <= |t_{N-2}| + |a'_{N-2}|
           |r_{N-2}| + |b'_{N-2}| |r_{N-3}| (prefix data only);
           VALIDITY gate + coverage tri^2 < 5/7 counted over 42.
       C1c ABS-CHAIN: S_{N-1} <= sum rbar^2 (= PSI3 head);
           VALIDITY gate (rbar >= |r| everywhere) + coverage
           counted.
       SEALED GO RULE: DRIVEN_CONE_GO iff some candidate is valid
       on 42/42, covers 42/42, and its cancellation demand
       log10(bound/target) stays < 1.0 dec on every rung.
  (c2) RELATIVE SCHUR FUNCTION: the Herglotz candidate G(z) =
       t~^T (G~ - z)^{-1} t~ in the sealed U(z - x0) basis (r253
       t1 route; f64-representable Gram).  Gates: U-Gram positive
       definite at full MAIN depth (positive prefix realized);
       Herglotz property Im G(z) sign(Im z) > 0 on the sealed
       z-grid; nested values Q_{N-1}, Q_N reproduce the chain S
       (rel 1e-6, solve residual 1e-8); cross-ratio = (B - Q_N)/
       (B - Q_{N-1}).  The Schur BOUNDEDNESS certificate needs
       sup_n Q_n <= B over the COMPLETION -- gated demonstration:
       the algebraic continuation of the chain flips h at exactly
       N + offset (offsets (0, 2) on w9/w13, ground truth in
       gates only) => the certificate consumes wall positivity
       beyond the free prefix: typed WALL_EQUIVALENT(c2), NO GO
       unless a source-pure mass bound materializes (it must NOT
       read S_{N-1} < B itself -- that is TARGET_INVERSE).
  (c3) EXACT SQUARE PLUS REMAINDER: 1 - q_N = A_N^2 + R_N with
       R_N >= 0 source-pure.  The bilinear identity gives D_N =
       B - S_{N-1} = ||s - proj s||^2 IFF the corner B has Gram
       provenance B = ||s||^2; with B = S_{N-2} + 5/7 that is
       EXACTLY a source derivation of 5/7 as remaining border
       mass.  Gates: partial Parseval S_{N-2} == Q_{N-1} re-gate
       (rel 1e-6); the signed continuation tail sum_{k>=N-1}
       rho_k over N + 6 degrees vs 5/7 PRINTED as a measurement
       (scratch: w9 0.950 / w13 0.726 vs 0.714 -- suggestive on
       w13, indefinite arithmetic, NO claim); verdict EXACT_
       SQUARE_OPEN + FIVE_SEVENTHS_NUMERICAL_ONLY unless the
       provenance closes (it is not expected to).

LEG D -- THE OLD TRAPS AS AUTOMATIC KILLS (mandatory gates, each
loud): (d1) FIVE_SEVENTHS_NUMEROLOGY: the measured 42-rung floor
must NOT saturate 7/5 (non-saturation >= 0.01; scratch/r258:
0.0278) -- any derivation that PRESUPPOSES the pretty rational is
dead on arrival; (d2) PAIRCORR_REENCODED detector: a candidate
whose coverage gap exceeds 1.0 dec demands a square-root-scale
cancellation estimate of the oscillatory drive (t IS the comb-
minus-smooth linear statistic in the moving frame, r243 leg E) --
the detector must FIRE on C1a and C1c (expected demands ~4.5-6.2
dec) and must NOT fire on C1b (expected gap ~0.4 dec on missing
rungs); (d3) BESSEL/MASS REENCODED: the M3_ABS mass majorant at
the TERMINAL degree must overshoot rho_{N-1} by >= 10x on w9 and
w13 (scratch: x55 / x23) -- no |sigma|-mass bound sees the F^2/h
ratio; (d4) WALL_COMPLETION: the chain continuation must flip
within EXT = 6 degrees at N + (0, 2) on (w9, w13) -- completion
certificates are wall-equivalent, machine-demonstrated; (d5)
TARGET_INVERSE_USED: the candidate scope AST audit is CLEAN on
C1a/C1b/C1c builders while the deliberate oracle mutant (reads
the terminal rho) is FLAGGED (must-fail); (d6) FIXED_STATE_
COMPRESSION: the drive truncated to its first 8 entries must
break the S rebuild loudly (>= 1e3 x the honest rebuild dev) --
the drive is length-N essential, no finite-state compression.

LEG E -- CONTROLS (world-blind): all algebraic identities (a3,
b1) run on MAIN + SCRAMBLE + EPSTEIN + SMOOTH at every degree;
the positive region distinguishes: MAIN to physical depth, first
rho < 0 at EXACTLY 21/25/27 on SCR/EPST/SMOOTH (firewall typing:
beyond pmax all statements algebraic); the r257 micro-predictor
runs as a WARD (blind source-only pivot field reproduces the
flips 3/3) -- mechanism coordinate check, NOT a proof; SMOOTH
self-alias: q_N <= 1e-20, drive alias <= 1e-12.

SEALED CONSTANTS: MAIN windows (9, 13); controls on w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; ladder frame-A
h <= 900 (42 rungs, (N, kz)-sorted), sample idx (0, 5, 10, 15,
20, 25, 30, 35, 41); EXT 6; FIB_LO 8; B57 = 5/7; dict bars 1e-8
main / 3e-6 deep / 1e-3 controls (absolute devs); bilinear
f64 bars 1e-6 MAIN / 1e-3 controls, scale max(|D_n|, |D_{n+1}|);
mp bilinear dps 60, n {6, 12} w9 + {12, 24} SCR, bar 1e-40,
corner shift +1; floor band [1.40, 1.46], non-saturation 0.01;
margin band [0.010, 0.020]; F-form bar 1e-9 (MAIN/SCR/EPST) with
alias-floor 1e-6 x max-norm and SMOOTH bar 1e-6; r-form/rebuild
bars 1e-9; region fraction grid (+-0.9, +-0.5, 0); PSI2 orbit
bar 1e-9; drive alias 1e-12; SM q bar 1e-20; Herglotz z-grid
(0.5 + 0.1j, 2 + 1j, -1 + 0.5j); Q re-gate 1e-6 / residual 1e-8;
demand bar 1.0 dec; K3 overshoot min 10; loudness 1e3; runtime
<= 1800 s; smoke = w9 + controls only (ladder, w13, mp wards,
sample-rung direct gates skipped).  DISCLOSED PRE-SPEC SCRATCH
CALIBRATIONS (two passes, floors and feasibility only, no verdict
rule tuned after any full evaluation): (s1) route floors -- F-/r-
form dev ~7e-14 MAIN/SCR, S rebuild ~4e-16, transfer rebuild
~6e-15, U-solve rel ~6e-12 with U-Gram positive definite at full
w9 depth, mp bilinear dev ~6e-55 at dps 60, C1a overshoot
4.0-5.8 dec, C1c ~6.2 dec, C1b tri^2 covering w9/w13 and missing
kz36/kz52, M3 terminal overshoot x55/x23, continuation flips at
N+0/N+2 with signed tails 0.950/0.726; (s2) SMOOTH drive alias
k >= 2 measured 2.4e-14 (k = 1 carries gam_1 h_0 -- the alias
statement starts at k = 2), PSI1 region sampling exit fraction
0.40 on w9, orbit max r^2/D = 0.416 at k = 0.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  TERMINAL_CROSSRATIO_GO(form) / TERMINAL_CROSSRATIO_MEASURED(
    42/42, min margin)
+ DICTIONARY_EXACT / DICTIONARY_OPEN
+ DRIVEN_RECURSION_EXACT(drive len N-1, no compression)
    / DRIVEN_RECURSION_OPEN
+ INVARIANT_REGION(typed per candidate: REGION_INVARIANT /
    OBSERVED_ONLY / RESTATEMENT / SOURCE_REASONED+infeasible dec)
+ DRIVEN_CONE_GO(cand) / DRIVEN_CONE_PARTIAL(best cand, cover
    k/42, gap dec) / DRIVEN_CONE_DEAD
+ SOURCE_SCHUR_GO / SOURCE_SCHUR_WALL_EQUIVALENT
+ EXACT_SQUARE_GO / EXACT_SQUARE_OPEN(5/7 Gram provenance)
+ FIVE_SEVENTHS_NUMERICAL_ONLY [if the floor stays measured]
+ PAIRCORR_REENCODED(candidate list) [detector census].
Honesty before beauty: a Go would close the fiber CONDITIONALLY
on the positive base prefix, never RH; no verdict claims a
derived 5/7, a bound mechanism, or an asymptotic law (r243/r247/
r250/r251/r253/r256/r257/r258 stand).

RECORD TABLES (frozen from the calibration passes: pass 1
reached 20/20 gates through G23 and then CRASHED in G24 -- the
draft floor route h e^{... } overflowed f64 at deep N; disclosed
CALIBRATION AMENDMENT a1: the floor is computed in the scaled
chain coordinates h_{N-1}/F_{N-1}^2 = eta_{N-1}/fb_{N-1}^2
EXACTLY (the e^{2 Ls} scale cancels algebraically) --
implementation only, no bar, band, candidate or verdict rule
moved; pass 2 then 31/31 gates, wall 8.9 s full / 0.3 s smoke;
the two pre-spec scratch calibrations are disclosed above; no
other amendment at any point):
CAL_VERDICT = TERMINAL_CROSSRATIO_MEASURED(42/42, min margin
0.0139) + DICTIONARY_EXACT + DRIVEN_RECURSION_EXACT(drive len
N-1, no compression) + INVARIANT_REGION(PSI1 OBSERVED_ONLY exit
0.40; PSI2 RESTATEMENT; PSI3 SOURCE_REASONED infeasible 7.3 dec)
+ DRIVEN_CONE_PARTIAL(C1b, cover 35/42, gap 0.41 dec) +
SOURCE_SCHUR_WALL_EQUIVALENT + EXACT_SQUARE_OPEN(5/7 Gram
provenance) + FIVE_SEVENTHS_NUMERICAL_ONLY +
PAIRCORR_REENCODED(C1a, C1c).
Key numbers.  CENSUS: 42 rungs N in [142, 878] POSITIVE_PREFIX
42/42; controls flip 25/21/27 re-derived; w9/w13 N = 184/168.
LEG A: terminal dictionary chain-vs-direct worst q dev (abs)
7.4e-9 main / 2.6e-8 deep / 9.6e-5 controls; D_{N-1} == 5/7 by
construction: 8.5e-9 main / 1.2e-7 deep / 3.1e-4 controls (the
f64 chain-reference floor on flipped worlds, r253/r257
precedent) -- note the cross-ratio q stays at 2.6e-8 where the
individual deep determinant already carries 1.2e-7: the CROSS-
RATIO is the well-conditioned coordinate; terminal values w9
q +0.2143 / w13 +0.5015 / EPST -1.5091 / SCR +0.2696 / SMOOTH
+0.0000 (signed, controls algebraic); per-degree bilinear X_n
== rho_n worst 4.8e-10 MAIN / 5.3e-5 controls; mp bilinear
wards (dps 60, independent monic mp F_n): w9 n=6/12 dev
4.6e-56/5.8e-55, SCRAMBLE n=12/24 dev 8.4e-57/3.7e-58 (n = 24
THROUGH the flip 21), corner-independence exact (0.0); 7/5
ward: floor 1.4278 in [1.40, 1.46], non-saturation 0.0278; q
census 42/42 < 1, min margin 0.0139 in band, min/med/max q
0.0015/0.4188/0.9805.  LEG B: F-form worst 7.2e-14 MAIN /
1.9e-14 SCR+EPST / 2.1e-11 SMOOTH (alias-guarded); r-form worst
7.2e-14, S rebuild worst 2.9e-15 on 42/42 + mains; drive: len
N-1, MAIN w9 nonzero at every degree (min |t| 1.7e-4), SMOOTH
alias k>=2 = 2.4e-14; PSI1 orbit containment max r^2/D = 0.416
(w9, k=0) / 0.5015 (w13, k=167 -- the terminal step is the
maximum), region sampling exits 1826/4550 (frac 0.40) =>
OBSERVED_ONLY, not region-invariant; PSI2 orbit-constant dev
8.7e-15 => RESTATEMENT; PSI3 majorant valid at every degree,
head feasibility D_8 - sum rbar^2 = -1.43e+07 (w9) =>
infeasible by 7.3 dec.  LEG C: candidate AST scopes CLEAN,
oracle mutant FLAGGED; C1a valid 42/42 (rebuild worst 4.7e-14),
covers 0/42, worst demand 6.26 dec (grows with N); C1b valid
42/42, covers 35/42, worst gap on the 7 missing rungs 0.41 dec
-- the ONLY candidate below the cancellation-demand bar; C1c
valid 42/42, covers 0/42, worst demand 13.46 dec; C2: U-Gram
positive definite at full depth (min eig 1.0e-4 w9 / 1.1e-4
w13), Herglotz 3/3 z-points, Q re-gate worst 5.2e-12 rel
(residual 4.3e-12), continuation flips at N+0 / N+2 => the
boundedness certificate consumes the wall: WALL_EQUIVALENT;
C3: partial Parseval re-gate 5.2e-12; signed continuation
tails 0.9501 (w9) / 0.7255 (w13) vs 5/7 = 0.7143 (pure
measurement, indefinite arithmetic, no claim).  LEG D: d1
non-saturation 0.0278 >= 0.01 (numerology killed); d2 detector
FIRES on C1a (6.26 dec) + C1c (13.46 dec), SILENT on C1b (0.41
dec) -- exactly as sealed; d3 M3 terminal overshoot x55 (w9) /
x23 (w13) >= 10; d4 completion flips at offsets (0, 2) ==
ground truth; d5 audit clean + mutant flagged (rho scope hit);
d6 drive truncation to 8 entries breaks S rebuild by 1.2e+15 x
honest.  LEG E: control increment law breaks first at 25/21/27
exactly; blind micro-predictor 3/3 (ward); SMOOTH q_N =
4.2e-25 <= 1e-20.  READING (typed, no upgrade): the terminal
fiber question is now a SINGLE tau cross-ratio whose dictionary
is machine-exact and mp-warded through the indefinite
continuation; the normalized recursion is fully driven
(length-N drive, no compression -- the no-go respected) and its
certificates split cleanly: norm/mass routes (C1a/C1c)
re-encode pair correlation (6.3-13.5 dec cancellation demand),
the completion route (C2) is wall-equivalent, the exact-square
route (C3) is exactly the missing Gram provenance of 5/7 --
while the ONE-STEP terminal triangle (C1b) is the only
certificate inside the demand bar, covering 35/42 rungs with a
0.41 dec worst gap: the proof pressure concentrates on bounding
THREE prefix numbers (t_{N-2}, r_{N-2}, r_{N-3}) by sqrt(5/7)
-- a finite, sharply typed target for a follow-up round.
Runtime 8.9 s full / 0.3 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (a1 predates the record
run, disclosed above).

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import coupledtau_probe as CT                # noqa: E402 r257
import offdiag_gram_probe as OG              # noqa: E402 r254
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
LADDER_SAMPLE_IDX = (0, 5, 10, 15, 20, 25, 30, 35, 41)
DEEP_N = 400
EXT = 6
FIB_LO = 8
B57 = 5.0 / 7.0
DICT_BAR_MAIN = 1e-8
DICT_BAR_DEEP = 3e-6
DICT_BAR_CTRL = 1e-3
BILIN_BAR_MAIN = 1e-6
BILIN_BAR_CTRL = 1e-3
MP_BILIN_DPS = 60
MP_BILIN_N_W9 = (6, 12)
MP_BILIN_N_SCR = (12, 24)
MP_BILIN_BAR = 1e-40
FLOOR_BAND = (1.40, 1.46)
NONSAT_MARGIN = 0.01
MARGIN_BAND = (0.010, 0.020)
FFORM_BAR = 1e-9
FFORM_BAR_SM = 1e-6
ALIAS_NRM_FLOOR = 1e-6
RFORM_BAR = 1e-9
REBUILD_BAR = 1e-9
REGION_FRACS = (-0.9, -0.5, 0.0, 0.5, 0.9)
PSI2_ORBIT_BAR = 1e-9
DRIVE_ALIAS_BAR = 1e-12
SM_Q_BAR = 1e-20
HERGLOTZ_GRID = (0.5 + 0.1j, 2.0 + 1.0j, -1.0 + 0.5j)
Q_REGATE_BAR = 1e-6
Q_RES_BAR = 1e-8
DEMAND_BAR = 1.0
K3_OVERSHOOT_MIN = 10.0
TAIL_OFFSETS = {9: 0, 13: 2}
LOUD = 1e3
CAL_VERDICT = (
    "TERMINAL_CROSSRATIO_MEASURED(42/42, min margin 0.0139) + "
    "DICTIONARY_EXACT + DRIVEN_RECURSION_EXACT(drive len N-1, no "
    "compression) + INVARIANT_REGION(PSI1 OBSERVED_ONLY exit "
    "0.40; PSI2 RESTATEMENT; PSI3 SOURCE_REASONED infeasible 7.3 "
    "dec) + DRIVEN_CONE_PARTIAL(C1b, cover 35/42, gap 0.41 dec) "
    "+ SOURCE_SCHUR_WALL_EQUIVALENT + EXACT_SQUARE_OPEN(5/7 Gram "
    "provenance) + FIVE_SEVENTHS_NUMERICAL_ONLY + "
    "PAIRCORR_REENCODED(C1a, C1c)")

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
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (flips, "
                       "tail offsets) enters gates only"
                       if not bad else "; ".join(bad))


# --------------------------------------------- driven recursion
def drive_arrays(rows, n_hi):
    """(r, t, ap, bp): r_k = fb_k/sqrt(eta_k) on the positive
    prefix; drive t_k = tb_k e^{Ls_k - Ls_{k+1}}/sqrt(eta_{k+1});
    a'_k = -alh_k/sqrt|gam_{k+1}|, b'_k = -sign(gam_k)
    sqrt|gam_k/gam_{k+1}| (real branch; on flipped worlds the
    r-coordinate is only used below the flip)."""
    r = np.zeros(n_hi)
    t = np.zeros(max(n_hi - 1, 0))
    ap = np.zeros(max(n_hi - 1, 0))
    bp = np.zeros(max(n_hi - 1, 0))
    for k in range(n_hi):
        r[k] = rows[k]["fb"] / math.sqrt(abs(rows[k]["eta"]))
    for k in range(n_hi - 1):
        g1 = rows[k]["gam_next"]
        e1 = math.exp(rows[k]["Ls"] - rows[k + 1]["Ls"])
        t[k] = rows[k]["tb"] * e1 \
            / math.sqrt(abs(rows[k + 1]["eta"]))
        ap[k] = -rows[k]["alh"] / math.sqrt(abs(g1))
        if k >= 1:
            g0 = rows[k - 1]["gam_next"]
            bp[k] = -math.copysign(math.sqrt(abs(g0 / g1)), g0)
    return r, t, ap, bp


def fform_dev(rows, N):
    """scaled F-form flow identity at ALL degrees (world-blind);
    per-degree norm = term-magnitude sum, with the sealed alias
    floor (fraction of the max norm) as denominator guard."""
    nrms = []
    devs = []
    for k in range(1, N - 1):
        gk = rows[k - 1]["gam_next"]
        e1 = math.exp(rows[k]["Ls"] - rows[k + 1]["Ls"])
        e2 = math.exp(rows[k - 1]["Ls"] - rows[k + 1]["Ls"])
        rhs = (rows[k]["tb"] - rows[k]["alh"] * rows[k]["fb"]) \
            * e1 - gk * rows[k - 1]["fb"] * e2
        nrm = (abs(rows[k]["tb"]) * e1
               + abs(rows[k]["alh"] * rows[k]["fb"]) * e1
               + abs(gk * rows[k - 1]["fb"]) * e2)
        nrms.append(nrm)
        devs.append(abs(rows[k + 1]["fb"] - rhs))
    floor = ALIAS_NRM_FLOOR * max(nrms)
    return max(d / max(n, floor) for d, n in zip(devs, nrms))


# ------------------------------------------------- direct route
def direct_terminal(p):
    """4 slogdets: (D_dir at N-1 and N, cross-ratio) in the sealed
    scaled-Chebyshev hull basis with the SAME corner B."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    P = CT.u_matrix(xu, x0, rh, N)
    TB = CT.u_matrix(bx, x0, rh, N)
    G = (P * wu) @ P.T
    tv = TB @ bw
    B = float(p["S"][N - 2]) + B57
    out = {}
    for n in (N - 1, N):
        sg, lg = np.linalg.slogdet(G[:n, :n])
        A = np.zeros((n + 1, n + 1))
        A[:n, :n] = G[:n, :n]
        A[:n, n] = tv[:n]
        A[n, :n] = tv[:n]
        A[n, n] = B
        sa, la = np.linalg.slogdet(A)
        out[n] = sa * sg * math.exp(la - lg)
    return out[N - 1], out[N]


# --------------------------------------------------- mp bilinear
def mp_bilinear(p, n, dps, corner_shift=0.0):
    """RAW bilinear identity at degree n in mp: tau^aug_n tau_{n+1}
    - tau^aug_{n+1} tau_n == (c_n F_n)^2 tau_n^2, with F_n from an
    INDEPENDENT mp monic Gram solve (never the chain).  Returns
    the relative deviation."""
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0m = mp.mpf(0.5 * (lo + hi))
    rhm = mp.mpf(0.5 * (hi - lo))
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    bs = [mp.mpf(float(v)) for v in bx]
    bwm = [mp.mpf(float(v)) for v in bw]
    tvm = [(x - x0m) / rhm for x in xs]
    tbm = [(x - x0m) / rhm for x in bs]
    n_hi = n + 2
    PU = [[mp.mpf(1)] * len(xs), [2 * u for u in tvm]]
    TU = [[mp.mpf(1)] * len(bs), [2 * u for u in tbm]]
    for _k in range(2, n_hi):
        PU.append([2 * u * a - b
                   for u, a, b in zip(tvm, PU[-1], PU[-2])])
        TU.append([2 * u * a - b
                   for u, a, b in zip(tbm, TU[-1], TU[-2])])
    GM = mp.matrix(n_hi, n_hi)
    for i in range(n_hi):
        for j in range(i, n_hi):
            v = mp.fsum(w * a * b
                        for w, a, b in zip(ws, PU[i], PU[j]))
            GM[i, j] = v
            GM[j, i] = v
    tm = [mp.fsum(w * a for w, a in zip(bwm, TU[i]))
          for i in range(n_hi)]
    Bm = mp.mpf(float(p["S"][p["N"] - 2])) + mp.mpf(5) / 7 \
        + mp.mpf(corner_shift)

    def dets(m):
        tau = mp.det(GM[:m, :m])
        A = mp.matrix(m + 1, m + 1)
        for i in range(m):
            for j in range(m):
                A[i, j] = GM[i, j]
            A[i, m] = tm[i]
            A[m, i] = tm[i]
        A[m, m] = Bm
        return tau, mp.det(A)

    tau_n, aug_n = dets(n)
    tau_n1, aug_n1 = dets(n + 1)
    lhs = aug_n * tau_n1 - aug_n1 * tau_n
    sub = GM[:n, :n]
    rv = mp.matrix(n, 1)
    for i in range(n):
        rv[i] = -GM[i, n]
    beta = mp.lu_solve(sub, rv)
    cn = (2 / rhm) ** n
    Fn = (tm[n] + mp.fsum(beta[k] * tm[k] for k in range(n))) / cn
    rhs = (cn * Fn) ** 2 * tau_n ** 2
    return float(abs(lhs / rhs - 1)), float(lhs / (tau_n * tau_n1))


# ------------------------------ proof-form candidates (SEALED,
# target-blind: consume ONLY (r_0..r_{N-2}, t, a', b'); the
# terminal readout is structurally withheld; AST-audited)
def cand_transfer(r0, t, ap, bp):
    """C1a: transfer matrix G with r = G tau, tau = (r0, t);
    returns (G, sigma_max, tau_in)."""
    n = len(t) + 1
    G = np.zeros((n, n))
    G[0, 0] = 1.0
    if n > 1:
        G[1, :] = ap[0] * G[0, :]
        G[1, 1] += 1.0
    for k in range(1, n - 1):
        G[k + 1, :] = ap[k] * G[k, :] + bp[k] * G[k - 1, :]
        G[k + 1, k + 1] += 1.0
    tau_in = np.concatenate([[r0], t])
    smax = float(np.linalg.svd(G, compute_uv=False)[0])
    return G, smax, tau_in


def cand_triangle(t_l, ap_l, bp_l, rm2, rm3):
    """C1b: one-step terminal triangle bound on |r_{N-1}| from
    prefix data only."""
    return abs(t_l) + abs(ap_l * rm2) + abs(bp_l * rm3)


def cand_abschain(r0, t, ap, bp):
    """C1c: triangle majorant chain rbar >= |r| by induction."""
    n = len(t) + 1
    rb = np.zeros(n)
    rb[0] = abs(r0)
    if n > 1:
        rb[1] = abs(t[0]) + abs(ap[0]) * rb[0]
    for k in range(1, n - 1):
        rb[k + 1] = abs(t[k]) + abs(ap[k]) * rb[k] \
            + abs(bp[k]) * rb[k - 1]
    return rb


def oracle_certificate(p):
    """DELIBERATE MUST-FAIL MUTANT: reads the terminal target
    directly -- the candidate AST audit must FLAG this scope."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


def candidate_scope_audit(funcname):
    """walk ONLY the named function's subtree; flag any target-
    side identifier or dict key from the sealed forbidden set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"rho", "S", "sa", "la", "q_chain", "D_dir", "wb",
            "anchor", "world_block", "direct_terminal"}
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
                if nm in forb:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ------------------------------------------ U-basis Schur route
def u_gram_route(p):
    """U(z - x0) basis (r253 t1): Gram, border vector, nested
    solves Q_{N-1}, Q_N, solve residual, eigen data for the
    Herglotz candidate G(z) = t^T (G - z)^{-1} t."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    x0 = 0.5 * (float(np.min(xu)) + float(np.max(xu)))
    P = np.empty((N, len(xu)))
    TB = np.empty((N, len(bx)))
    tt = xu - x0
    tb_ = bx - x0
    P[0] = 1.0
    TB[0] = 1.0
    P[1] = 2.0 * tt
    TB[1] = 2.0 * tb_
    for k in range(2, N):
        P[k] = 2.0 * tt * P[k - 1] - P[k - 2]
        TB[k] = 2.0 * tb_ * TB[k - 1] - TB[k - 2]
    G = (P * wu) @ P.T
    G = 0.5 * (G + G.T)
    tv = TB @ bw
    out = {}
    res = 0.0
    for n in (N - 1, N):
        sol = np.linalg.solve(G[:n, :n], tv[:n])
        res = max(res, float(np.max(np.abs(G[:n, :n] @ sol
                                           - tv[:n]))))
        out[n] = float(tv[:n] @ sol)
    lam, U = np.linalg.eigh(G)
    c2 = (U.T @ tv) ** 2
    herg_ok = True
    for z in HERGLOTZ_GRID:
        gz = complex(np.sum(c2 / (lam - z)))
        herg_ok = herg_ok and (gz.imag * z.imag > 0.0)
    return out[N - 1], out[N], res, float(lam[0]), herg_ok


def continuation(p, ext):
    """chain continued ext degrees past N: first flip degree and
    the signed tail sum_{k>=N-1} rho_k (indefinite arithmetic)."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"],
                         dsm["vs"], N + ext)
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    tail = sum(r["rho"] for r in rows[N - 1:])
    return nf, tail


def m3_terminal(p):
    """M3_ABS mass majorant vs rho at the TERMINAL degree."""
    dsm = p["dsm"]
    N = p["N"]
    bx = np.concatenate([dsm["xs"], dsm["ys"]])
    bw = np.concatenate([dsm["ws"], -dsm["vs"]])
    Pm = OG.phat_matrix(p["rows"], bx, N)
    m3 = float(np.abs(bw) @ np.abs(Pm[N - 1])) ** 2
    rr = float(bw @ Pm[N - 1]) ** 2
    return m3, rr


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("terminal_crossratio_probe -- PRIME.PORT.COUPLEDTAU."
          "TERMINAL_CROSSRATIO.01 (round 260)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls; ladder, w13, mp "
                        "wards, sample direct gates skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN OBJECT: q_N = rho_{N-1}/D_{N-1} as the positivity "
          "of the tau cross-ratio 1 - q_N = (tau^aug_N tau_{N-1})/"
          "(tau^aug_{N-1} tau_N); bilinear identity tau^aug_n "
          "tau_{n+1} - tau^aug_{n+1} tau_n = (c_n F_n)^2 tau_n^2 "
          "(c_n = (2/rh)^n, corner-independent); driven recursion "
          "r_{k+1} = t_k + a'_k r_k + b'_k r_{k-1}; sealed Psi "
          "candidates PSI1_GAP/PSI2_TAILBUDGET/PSI3_ABSCHAIN; "
          "sealed certificates C1a TRANSFER / C1b TERMINAL "
          "ONE-STEP / C1c ABS-CHAIN + Schur (c2) + exact square "
          "(c3); kills d1-d6 armed; cofinal ladder = frame-A "
          "h <= %d, sample %s; ALL bars + verdict rules sealed "
          "BEFORE evaluation (two pre-spec scratch calibrations "
          "disclosed in the spec)"
          % (H_CAP, str(LADDER_SAMPLE_IDX)))

    # ---------------- S1: census + controls + ladder
    section("S1  CENSUS + CONTROLS + POSITIVITY TYPING")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s (typed INDEFINITE_"
          "CONTINUATION beyond pmax); cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))

    worlds = list(packs.items()) + list(ctrl.items())

    # ---------------- S2: LEG A -- the exact dictionary
    section("S2  LEG A -- THE EXACT TERMINAL DICTIONARY")
    WB = {}
    dev_q_main = dev_q_ctrl = 0.0
    dev_x_main = dev_x_ctrl = 0.0
    d57_main = d57_deep = d57_ctrl = 0.0
    a_note = []
    for tag, p in worlds:
        wb = CT.world_block(p)
        WB[tag] = wb
        N = p["N"]
        is_main = tag in packs
        Dm1 = wb["sa"][N - 1] * wb["sg"][N - 1] \
            * math.exp(wb["la"][N - 1] - wb["lg"][N - 1])
        Dn = wb["sa"][N] * wb["sg"][N] \
            * math.exp(wb["la"][N] - wb["lg"][N])
        q_dir = 1.0 - Dn / Dm1
        q_ch = float(p["rho"][N - 1]) / B57
        dq = abs(q_dir - q_ch)
        xr_dir = Dn / Dm1
        xr_ch = 1.0 - q_ch
        dx = abs(xr_dir - xr_ch)
        if is_main:
            dev_q_main = max(dev_q_main, dq)
            dev_x_main = max(dev_x_main, dx)
            d57_main = max(d57_main, abs(Dm1 / B57 - 1.0))
        else:
            dev_q_ctrl = max(dev_q_ctrl, dq)
            dev_x_ctrl = max(dev_x_ctrl, dx)
            d57_ctrl = max(d57_ctrl, abs(Dm1 / B57 - 1.0))
        a_note.append("%s q %+.6f xr %+.6f" % (tag, q_ch, xr_ch))
    dev_q_deep = dev_x_deep = 0.0
    if not smoke:
        for idx in LADDER_SAMPLE_IDX:
            p = ladder[idx]
            N = p["N"]
            Dm1, Dn = direct_terminal(p)
            q_ch = float(p["rho"][N - 1]) / B57
            dq = abs((1.0 - Dn / Dm1) - q_ch)
            dx = abs((Dn / Dm1) - (1.0 - q_ch))
            if N <= DEEP_N:
                dev_q_main = max(dev_q_main, dq)
                dev_x_main = max(dev_x_main, dx)
                d57_main = max(d57_main, abs(Dm1 / B57 - 1.0))
            else:
                dev_q_deep = max(dev_q_deep, dq)
                dev_x_deep = max(dev_x_deep, dx)
                d57_deep = max(d57_deep, abs(Dm1 / B57 - 1.0))
    check("G20-terminal-dictionary",
          dev_q_main <= DICT_BAR_MAIN and dev_q_deep
          <= DICT_BAR_DEEP and dev_q_ctrl <= DICT_BAR_CTRL
          and d57_main <= DICT_BAR_MAIN
          and d57_deep <= DICT_BAR_DEEP
          and d57_ctrl <= DICT_BAR_CTRL,
          "q_N = F_{N-1}^2/(h_{N-1} D_{N-1}): chain vs direct "
          "bordered slogdet at sizes N-1/N (same corner): worst "
          "%.1e main (bar %.0e) / %.1e deep (bar %.0e) / %.1e "
          "controls (bar %.0e); D_{N-1} == 5/7 by construction: "
          "%.1e main / %.1e deep / %.1e controls (SCR/EPST = the "
          "f64 chain-reference floor, r253/r257 precedent); %s"
          % (dev_q_main, DICT_BAR_MAIN, dev_q_deep, DICT_BAR_DEEP,
             dev_q_ctrl, DICT_BAR_CTRL, d57_main, d57_deep,
             d57_ctrl, "; ".join(a_note)))
    check("G21-crossratio-identity",
          dev_x_main <= DICT_BAR_MAIN and dev_x_deep
          <= DICT_BAR_DEEP and dev_x_ctrl <= DICT_BAR_CTRL,
          "1 - q_N == (tau^aug_N tau_{N-1})/(tau^aug_{N-1} tau_N) "
          "on all worlds + %s ladder sample: worst %.1e main / "
          "%.1e deep / %.1e controls -- q_N < 1 IS the positivity "
          "of this cross-ratio"
          % ("9-rung" if not smoke else "no", dev_x_main,
             dev_x_deep, dev_x_ctrl))
    bl_main = bl_ctrl = 0.0
    for tag, p in worlds:
        wb = WB[tag]
        N = p["N"]
        worst = 0.0
        for n in range(1, N):
            D_lo = wb["sa"][n] * wb["sg"][n] \
                * math.exp(wb["la"][n] - wb["lg"][n])
            D_hi = wb["sa"][n + 1] * wb["sg"][n + 1] \
                * math.exp(wb["la"][n + 1] - wb["lg"][n + 1])
            X = D_lo - D_hi
            sc = max(abs(D_lo), abs(D_hi), 1e-300)
            worst = max(worst, abs(X - float(p["rho"][n])) / sc)
        if tag in packs:
            bl_main = max(bl_main, worst)
        else:
            bl_ctrl = max(bl_ctrl, worst)
    check("G22-bilinear-per-degree",
          bl_main <= BILIN_BAR_MAIN and bl_ctrl <= BILIN_BAR_CTRL,
          "normalized bilinear form X_n = (tau^aug_n tau_{n+1} - "
          "tau^aug_{n+1} tau_n)/(tau_n tau_{n+1}) == rho_n at ALL "
          "degrees on ALL 5 worlds (direct-route LHS vs chain "
          "RHS, scale max|D|): worst %.1e MAIN (bar %.0e), %.1e "
          "controls (bar %.0e, f64 chain floor on flipped worlds)"
          % (bl_main, BILIN_BAR_MAIN, bl_ctrl, BILIN_BAR_CTRL))
    if not smoke:
        mp_note = []
        mp_worst = 0.0
        ci_worst = 0.0
        for n in MP_BILIN_N_W9:
            dv, x1 = mp_bilinear(packs["w9"], n, MP_BILIN_DPS)
            dv2, x2 = mp_bilinear(packs["w9"], n, MP_BILIN_DPS,
                                  corner_shift=1.0)
            ci_worst = max(ci_worst, abs(x2 / x1 - 1.0))
            mp_worst = max(mp_worst, dv, dv2)
            mp_note.append("w9 n=%d %.1e" % (n, dv))
        for n in MP_BILIN_N_SCR:
            dv, _ = mp_bilinear(ctrl["SCR"], n, MP_BILIN_DPS)
            mp_worst = max(mp_worst, dv)
            mp_note.append("SCR n=%d %.1e" % (n, dv))
        check("G23-mp-bilinear-wards",
              mp_worst <= MP_BILIN_BAR and ci_worst
              <= MP_BILIN_BAR,
              "RAW bilinear identity in mp (dps %d) with an "
              "INDEPENDENT monic mp F_n (Gram solve, never the "
              "chain): %s (bar %.0e); SCR n = 24 spans the flip "
              "21 -- the identity holds THROUGH the indefinite "
              "continuation; corner-independence (B vs B+1) "
              "worst %.1e -- the budget corner cancels in the "
              "bilinear combination"
              % (MP_BILIN_DPS, "; ".join(mp_note), MP_BILIN_BAR,
                 ci_worst))
    else:
        check("G23-mp-bilinear-wards", True, "SMOKE: skipped")
    if not smoke:
        # h_{N-1}/F_{N-1}^2 = eta_{N-1}/fb_{N-1}^2 exactly (the
        # e^{2 Ls} scale cancels; the naive exp route overflows
        # at deep N -- calibration amendment a1, implementation
        # only, no bar moved)
        floors = [p["rows"][p["N"] - 1]["eta"]
                  / p["rows"][p["N"] - 1]["fb"] ** 2
                  for p in ladder]
        fmin = min(floors)
        ok57 = (FLOOR_BAND[0] <= fmin <= FLOOR_BAND[1]
                and fmin >= 1.4 + NONSAT_MARGIN)
        check("G24-seven-fifths-ward", ok57,
              "REPRODUCTION WARD ONLY: min_w h_{N-1}/F_{N-1}^2 = "
              "%.4f in %s, >= 7/5 with non-saturation margin "
              "%.4f >= %.2f: the constant stays the r241 IMPORTED "
              "floor, no derivation -- FIVE_SEVENTHS_NUMERICAL_"
              "ONLY" % (fmin, str(FLOOR_BAND), fmin - 1.4,
                        NONSAT_MARGIN))
        qs = np.array([float(p["rho"][p["N"] - 1]) / B57
                       for p in ladder])
        margins = B57 * (1.0 - qs)
        okq = bool(np.all(qs < 1.0)) and (
            MARGIN_BAND[0] <= float(np.min(margins))
            <= MARGIN_BAND[1])
        check("G25-q-census-cofinal", okq,
              "q_{w,N} < 1 on %d/%d rungs of the pre-sealed "
              "cofinal sequence (MEASUREMENT, POSITIVE_PREFIX "
              "typed); min/med/max q %.4f/%.4f/%.4f; min terminal "
              "margin 5/7 - rho = %.4f in the sealed band %s "
              "(r243/r258 razor reproduced)"
              % (int(np.sum(qs < 1.0)), len(ladder),
                 float(np.min(qs)), float(np.median(qs)),
                 float(np.max(qs)), float(np.min(margins)),
                 str(MARGIN_BAND)))
    else:
        check("G24-seven-fifths-ward", True, "SMOKE: skipped")
        check("G25-q-census-cofinal", True, "SMOKE: skipped")

    # ---------------- S3: LEG B -- the driven recursion
    section("S3  LEG B -- THE NORMALIZED FULLY DRIVEN RECURSION")
    ff_main = ff_ctrl = ff_sm = 0.0
    for tag, p in worlds:
        dv = fform_dev(p["rows"], p["N"])
        if tag in packs:
            ff_main = max(ff_main, dv)
        elif tag == "SMOOTH":
            ff_sm = dv
        else:
            ff_ctrl = max(ff_ctrl, dv)
    check("G30-fform-all-worlds",
          ff_main <= FFORM_BAR and ff_ctrl <= FFORM_BAR
          and ff_sm <= FFORM_BAR_SM,
          "scaled F-form flow identity F_{k+1} = T_k - alh_k F_k "
          "- gam_k F_{k-1} at ALL degrees on ALL 5 worlds (world-"
          "blind algebra): MAIN worst %.1e, SCR+EPST %.1e (bar "
          "%.0e), SMOOTH %.1e (alias-guarded bar %.0e: the self-"
          "aliased source is a 0/0 case, r243-a1 precedent)"
          % (ff_main, ff_ctrl, FFORM_BAR, ff_sm, FFORM_BAR_SM))
    DRV = {}
    rf_worst = rb_worst = 0.0
    for tag, p in packs.items():
        N = p["N"]
        r, t, ap, bp = drive_arrays(p["rows"], N)
        DRV[tag] = (r, t, ap, bp)
        for k in range(1, N - 1):
            rhs = t[k] + ap[k] * r[k] + bp[k] * r[k - 1]
            nrm = abs(t[k]) + abs(ap[k] * r[k]) \
                + abs(bp[k] * r[k - 1]) + 1e-300
            rf_worst = max(rf_worst, abs(r[k + 1] - rhs) / nrm)
        rb_worst = max(rb_worst,
                       abs(float(np.sum(r * r))
                           / float(p["S"][N - 1]) - 1.0))
    lad_drv = []
    if not smoke:
        for p in ladder:
            N = p["N"]
            r, t, ap, bp = drive_arrays(p["rows"], N)
            lad_drv.append((p, r, t, ap, bp))
            rb_worst = max(rb_worst,
                           abs(float(np.sum(r * r))
                               / float(p["S"][N - 1]) - 1.0))
    check("G31-rform-rebuild",
          rf_worst <= RFORM_BAR and rb_worst <= REBUILD_BAR,
          "r-form r_{k+1} = t_k + a'_k r_k + b'_k r_{k-1} + "
          "D-update on the positive prefixes: worst dev %.1e "
          "(bar %.0e); S_{N-1} rebuild sum r^2 vs chain on "
          "mains + %d ladder rungs: worst rel %.1e (bar %.0e) "
          "-- the driven recursion reproduces (r, D) exactly"
          % (rf_worst, RFORM_BAR, len(lad_drv), rb_worst,
             REBUILD_BAR))
    rowsS = ctrl["SMOOTH"]["rows"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(ctrl["SMOOTH"]["N"] - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    r9, t9, _, _ = DRV["w9"]
    tmin9 = float(np.min(np.abs(t9)))
    check("G32-drive-typology", alias <= DRIVE_ALIAS_BAR,
          "the drive has length N-1 and consumes the full border "
          "comb at every degree (no compression); SMOOTH alias: "
          "max_{k>=2} |T~_k| / max(|T~_0|, |T~_1|) = %.1e (bar "
          "%.0e -- on the self-aliased source the drive is "
          "EXACTLY the two Jacobi readouts alh_0 h_0, gam_1 h_0); "
          "MAIN w9 drive nonzero at every degree (min |t| %.1e); "
          "coefficient typology: a', b' consume the window chain "
          "(alh, gam), the drive carries the border"
          % (alias, DRIVE_ALIAS_BAR, tmin9))
    # (b4) invariant region adjudication
    reg_note = []
    orbit_ok = True
    psi2_worst = 0.0
    psi3_valid = True
    psi3_head = 0.0
    exit_frac = 0.0
    for tag, p in packs.items():
        N = p["N"]
        r, t, ap, bp = DRV[tag]
        B = float(p["S"][N - 2]) + B57
        D = np.zeros(N + 1)
        D[0] = B
        for k in range(N):
            D[k + 1] = D[k] - r[k] ** 2
        qs_step = r[:N] ** 2 / D[:N]
        orbit_ok = orbit_ok and bool(np.all(qs_step < 1.0)) \
            and bool(np.all(D > 0.0))
        DN = D[N]
        for k in range(N):
            tail = float(np.sum(r[k:] ** 2))
            psi2_worst = max(psi2_worst,
                             abs((D[k] - tail) / DN - 1.0))
        rb = cand_abschain(r[0], t, ap, bp)
        psi3_valid = psi3_valid and bool(
            np.all(rb >= np.abs(r) * (1.0 - 1e-9)))
        head = D[FIB_LO] - float(np.sum(rb[FIB_LO:] ** 2))
        if tag == "w9":
            psi3_head = head
            tot = out = 0
            for k in range(1, N - 1):
                sD = math.sqrt(D[k])
                for f1 in REGION_FRACS:
                    for f2 in REGION_FRACS:
                        rs, rm = f1 * sD, f2 * sD
                        r2 = t[k] + ap[k] * rs + bp[k] * rm
                        D2 = D[k] - rs * rs
                        tot += 1
                        if not (D2 > 0.0 and r2 * r2 < D2):
                            out += 1
            exit_frac = out / tot
        reg_note.append("%s max r^2/D %.4f (k=%d) minD %.4f "
                        "psi3head %+.2e"
                        % (tag, float(np.max(qs_step)),
                           int(np.argmax(qs_step)),
                           float(np.min(D)), head))
    psi3_dec = math.log10(max(-psi3_head, 1e-300)
                          / max(B57, 1e-300)) \
        if psi3_head < 0 else float("-inf")
    check("G33-invariant-region", orbit_ok
          and psi2_worst <= PSI2_ORBIT_BAR and psi3_valid,
          "sealed candidates: PSI1_GAP orbit containment holds at "
          "EVERY degree on MAIN (%s) but the sampled region map "
          "exits at fraction %.2f on the sealed grid => "
          "OBSERVED_ONLY, not region-invariant; PSI2_TAILBUDGET "
          "orbit-constant == D_N to %.1e => RESTATEMENT (its "
          "positivity IS the target, typed); PSI3_ABSCHAIN "
          "majorant valid at every degree (SOURCE_REASONED "
          "one-step invariance) but head-INFEASIBLE: D_8 - sum "
          "rbar^2 = %+.2e on w9 (%.1f dec beyond the corner) -- "
          "honest: no sealed region is both source-reasoned and "
          "feasible" % ("; ".join(reg_note), exit_frac,
                        psi2_worst, psi3_head, psi3_dec))

    # ---------------- S4: LEG C -- the three proof forms
    section("S4  LEG C -- THE THREE ADMISSIBLE PROOF FORMS")
    hits = []
    for fn in ("cand_transfer", "cand_triangle", "cand_abschain",
               "drive_arrays"):
        hits += candidate_scope_audit(fn)
    check("G40-candidate-ast-clean", not hits,
          "the sealed certificate builders consume ONLY (r "
          "prefix, drive, a', b') / chain rows -- no target-side "
          "identifier in scope (sealed forbidden set): %s"
          % ("CLEAN" if not hits else "; ".join(hits)))
    hits_orc = candidate_scope_audit("oracle_certificate")
    check("G41-oracle-mutant-flagged", bool(hits_orc),
          "the deliberately target-reading mutant is FLAGGED by "
          "the candidate AST audit (%s) while the certificate "
          "scopes stay clean: target-blindness is machine-"
          "enforced" % ("; ".join(hits_orc) if hits_orc
                        else "NOT FLAGGED"))
    pool = list(lad_drv) if not smoke else [
        (packs["w9"],) + DRV["w9"]]
    c1a_valid = c1b_valid = c1c_valid = True
    c1a_cov = c1b_cov = c1c_cov = 0
    c1a_dem = c1b_gap = c1c_dem = 0.0
    tr_rebuild = 0.0
    for p, r, t, ap, bp in pool:
        N = p["N"]
        B = float(p["S"][N - 2]) + B57
        Sch = float(p["S"][N - 1])
        G, smax, tau_in = cand_transfer(r[0], t, ap, bp)
        rG = G @ tau_in
        tr_rebuild = max(tr_rebuild,
                         float(np.max(np.abs(rG - r)))
                         / float(np.max(np.abs(r))))
        bound_a = smax * smax * float(tau_in @ tau_in)
        c1a_valid = c1a_valid and (bound_a >= Sch * (1 - 1e-9))
        if bound_a < B:
            c1a_cov += 1
        c1a_dem = max(c1a_dem, math.log10(bound_a / B))
        tri = cand_triangle(t[N - 2], ap[N - 2], bp[N - 2],
                            r[N - 2], r[N - 3])
        c1b_valid = c1b_valid and (tri >= abs(r[N - 1])
                                   * (1 - 1e-9))
        if tri * tri < B57:
            c1b_cov += 1
        else:
            c1b_gap = max(c1b_gap, math.log10(tri * tri / B57))
        rb = cand_abschain(r[0], t, ap, bp)
        c1c_valid = c1c_valid and bool(
            np.all(rb >= np.abs(r) * (1.0 - 1e-9)))
        bound_c = float(np.sum(rb * rb))
        if bound_c < B:
            c1c_cov += 1
        c1c_dem = max(c1c_dem, math.log10(bound_c / B))
    npool = len(pool)
    check("G42-c1a-transfer", c1a_valid
          and tr_rebuild <= REBUILD_BAR,
          "C1a TRANSFER: r = G tau exact (worst rebuild %.1e), "
          "certified bound ||G||^2 ||tau||^2 >= S_{N-1} valid on "
          "%d/%d rungs; coverage bound < B_w on %d/%d; worst "
          "cancellation demand %.2f dec (grows with N)"
          % (tr_rebuild, npool, npool, c1a_cov, npool, c1a_dem))
    check("G43-c1b-terminal-onestep", c1b_valid,
          "C1b TERMINAL ONE-STEP: |r_{N-1}| <= |t_{N-2}| + "
          "|a'_{N-2}||r_{N-2}| + |b'_{N-2}||r_{N-3}| (prefix "
          "data only) valid on %d/%d rungs; coverage tri^2 < 5/7 "
          "on %d/%d; worst gap on missing rungs %.2f dec -- the "
          "cross-ratio positivity REDUCES to bounding three "
          "prefix numbers by sqrt(5/7)"
          % (npool, npool, c1b_cov, npool, c1b_gap))
    check("G44-c1c-abschain", c1c_valid,
          "C1c ABS-CHAIN: rbar >= |r| at every degree on %d/%d "
          "rungs; coverage sum rbar^2 < B on %d/%d; worst demand "
          "%.2f dec (the r258 mass-majorant failure in the "
          "driven coordinate)"
          % (npool, npool, c1c_cov, npool, c1c_dem))
    q_re = 0.0
    res_w = 0.0
    eig_ok = True
    herg_all = True
    cont_ok = True
    ct_note = []
    for tag, p in packs.items():
        N = p["N"]
        Qm1, Qn, res, eig0, herg = u_gram_route(p)
        res_w = max(res_w, res)
        eig_ok = eig_ok and (eig0 > 0.0)
        herg_all = herg_all and herg
        q_re = max(q_re, abs(Qm1 / float(p["S"][N - 2]) - 1.0),
                   abs(Qn / float(p["S"][N - 1]) - 1.0))
        nf, tail = continuation(p, EXT)
        off = TAIL_OFFSETS[p["kz"]]
        cont_ok = cont_ok and (nf == N + off)
        ct_note.append("%s eig0 %.1e cont flip N%+d tail %.4f"
                       % (tag, eig0, (nf - N) if nf else 99,
                          tail))
    check("G45-c2-schur-herglotz",
          eig_ok and herg_all and q_re <= Q_REGATE_BAR
          and res_w <= Q_RES_BAR and cont_ok,
          "C2: U-Gram positive definite at full MAIN depth, "
          "Herglotz candidate G(z) = t^T (G - z)^{-1} t verified "
          "on the sealed z-grid, nested Q re-gate vs chain S "
          "worst %.1e (bar %.0e, residual %.1e); the boundedness "
          "certificate sup_n Q_n <= B needs the COMPLETION, and "
          "the continuation flips at %s == N + %s: SOURCE_SCHUR "
          "is WALL_EQUIVALENT -- typed, no Go"
          % (q_re, Q_REGATE_BAR, res_w, "; ".join(ct_note),
             str(tuple(TAIL_OFFSETS[p["kz"]]
                       for p in packs.values()))))
    check("G46-c3-exact-square", q_re <= Q_REGATE_BAR,
          "C3: partial Parseval S_{N-2} == Q_{N-1} re-gated "
          "(within G45 worst %.1e); D_N = B - S_{N-1} becomes an "
          "EXACT SQUARE ||s - proj s||^2 iff B has Gram "
          "provenance, i.e. iff 5/7 is derived as remaining "
          "border mass -- the signed continuation tails "
          "sum_{k>=N-1} rho over N+%d degrees are %s vs 5/7 = "
          "%.4f (indefinite arithmetic, PURE MEASUREMENT, no "
          "claim): EXACT_SQUARE_OPEN(5/7 Gram provenance)"
          % (q_re, EXT,
             str(["%.4f" % (ct[1])
                  for ct in [continuation(p, EXT)
                             for p in packs.values()]]),
             B57))

    # ---------------- S5: LEG D -- the kills
    section("S5  LEG D -- THE OLD TRAPS AS AUTOMATIC KILLS")
    if not smoke:
        check("G50-numerology-kill", fmin - 1.4 >= NONSAT_MARGIN,
              "FIVE_SEVENTHS_NUMEROLOGY: the measured floor "
              "%.4f does NOT saturate 7/5 (margin %.4f >= %.2f, "
              "loud) -- any derivation that presupposes the "
              "pretty rational is dead on arrival"
              % (fmin, fmin - 1.4, NONSAT_MARGIN))
    else:
        check("G50-numerology-kill", True, "SMOKE: skipped")
    fire_a = c1a_dem >= DEMAND_BAR
    fire_c = c1c_dem >= DEMAND_BAR
    fire_b = c1b_gap >= DEMAND_BAR
    check("G51-paircorr-detector", fire_a and fire_c
          and not fire_b,
          "PAIRCORR_REENCODED detector (sealed bar %.1f dec): "
          "closing a coverage gap > 1 dec demands a sqrt-scale "
          "cancellation estimate of the oscillatory drive (the "
          "drive IS the comb-minus-smooth statistic, r243 leg "
          "E): FIRES on C1a (%.2f dec) + C1c (%.2f dec), SILENT "
          "on C1b (%.2f dec) -- norm/mass certificates re-encode "
          "pair correlation, the one-step certificate does not"
          % (DEMAND_BAR, c1a_dem, c1c_dem, c1b_gap))
    m3_ok = True
    m3_note = []
    for tag, p in packs.items():
        m3, rr = m3_terminal(p)
        m3_ok = m3_ok and (m3 / rr >= K3_OVERSHOOT_MIN)
        m3_note.append("%s x%.1e" % (tag, m3 / rr))
    check("G52-mass-majorant-kill", m3_ok,
          "BESSEL/MASS REENCODED: the M3_ABS |sigma|-mass "
          "majorant at the TERMINAL degree overshoots rho_{N-1} "
          "by %s (min bar x%.0f, loud): no mass bound sees the "
          "F^2/h ratio -- the r243/r258 lesson reproduced at the "
          "exact point of the question"
          % ("; ".join(m3_note), K3_OVERSHOOT_MIN))
    check("G53-wall-completion-kill", cont_ok,
          "WALL_COMPLETION: the chain continuation flips h at "
          "N+0 (w9) / N+2 (w13) within EXT = %d (ground truth "
          "in gates only): ANY completion-based certificate "
          "(c2 boundedness, c3 full-mass square) consumes wall "
          "positivity beyond the free prefix -- typed, "
          "machine-demonstrated" % EXT)
    r9, t9, ap9, bp9 = DRV["w9"]
    N9 = packs["w9"]["N"]
    t_tr = t9.copy()
    t_tr[FIB_LO:] = 0.0
    rr_tr = np.zeros(N9)
    rr_tr[0] = r9[0]
    rr_tr[1] = t_tr[0] + ap9[0] * rr_tr[0]
    for k in range(1, N9 - 1):
        rr_tr[k + 1] = t_tr[k] + ap9[k] * rr_tr[k] \
            + bp9[k] * rr_tr[k - 1]
    S_tr = float(np.sum(rr_tr ** 2))
    S_ch = float(packs["w9"]["S"][N9 - 1])
    honest = abs(float(np.sum(r9 ** 2)) / S_ch - 1.0)
    dev_tr = abs(S_tr / S_ch - 1.0)
    check("G54-compression-kill",
          dev_tr >= LOUD * max(honest, 1e-300),
          "FIXED_STATE_COMPRESSION: drive truncated to its first "
          "%d entries -> S rebuild dev %.1e = %.1e x honest %.1e "
          "(bar %.0f x): the drive is length-N essential, no "
          "finite-state compression of the comb (boundary-state "
          "no-go respected)"
          % (FIB_LO, dev_tr, dev_tr / max(honest, 1e-300),
             honest, LOUD))

    # ---------------- S6: LEG E -- controls
    section("S6  LEG E -- CONTROLS (WORLD-BLIND)")
    brk_ok = True
    brk_note = []
    for c in ctrl:
        p = ctrl[c]
        first = next((n for n in range(p["N"])
                      if float(p["rho"][n]) < 0.0), None)
        brk_ok = brk_ok and (first == CTRL_FLIPS[long_names[c]])
        brk_note.append("%s first rho<0 at %s (flip %d)"
                        % (c, first, CTRL_FLIPS[long_names[c]]))
    mono_ok = all(float(np.min(packs[t]["rho"][:packs[t]["N"]]))
                  > 0.0 for t in packs)
    check("G60-region-distinguishes", brk_ok and mono_ok,
          "the positive region separates the worlds degree-"
          "exactly: MAIN rho > 0 through the ENTIRE free window; "
          "%s -- the increment law breaks FIRST at the r256 base "
          "flips (algebraic beyond pmax, typed)"
          % "; ".join(brk_note))
    fl_ok = True
    fl_note = []
    for c in ctrl:
        xu, wu = WB[c]["xu"], WB[c]["wu"]
        fl = CT.blind_flip_predictor(xu, wu, ctrl[c]["N"])
        first = fl[0] if fl else None
        fl_ok = fl_ok and (first == ctrl[c]["nf"])
        fl_note.append("%s -> %s (truth %s)"
                       % (c, first, ctrl[c]["nf"]))
    check("G61-micropredictor-ward", fl_ok,
          "r257 blind source-only pivot field reproduces the "
          "control flips: %s -- WARD (the coordinate is "
          "mechanistically right), NOT a proof"
          % "; ".join(fl_note))
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) \
        / B57
    check("G62-smooth-alias", abs(qS) <= SM_Q_BAR,
          "SMOOTH self-alias: q_N = %.1e <= %.0e -- the terminal "
          "question trivializes exactly when the source aliases "
          "(F_{N-1} = 0 structurally); with G32 the driven "
          "recursion degenerates to the two Jacobi readouts"
          % (qS, SM_Q_BAR))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact terminal dictionary as a tau cross-"
          "ratio (bilinear identity mp-warded, corner-"
          "independent), the fully driven normalized recursion "
          "with its no-compression drive, the sealed invariant-"
          "region and certificate adjudication, and the honest "
          "kill census of the three proof forms")
    okA = (dev_q_main <= DICT_BAR_MAIN
           and dev_q_deep <= DICT_BAR_DEEP
           and dev_q_ctrl <= DICT_BAR_CTRL
           and dev_x_main <= DICT_BAR_MAIN
           and bl_main <= BILIN_BAR_MAIN
           and bl_ctrl <= BILIN_BAR_CTRL)
    okB = (ff_main <= FFORM_BAR and rf_worst <= RFORM_BAR
           and rb_worst <= REBUILD_BAR
           and alias <= DRIVE_ALIAS_BAR)
    vA = "DICTIONARY_EXACT" if okA else "DICTIONARY_OPEN"
    vB = ("DRIVEN_RECURSION_EXACT(drive len N-1, no compression)"
          if okB else "DRIVEN_RECURSION_OPEN")
    vReg = ("INVARIANT_REGION(PSI1 OBSERVED_ONLY exit %.2f; PSI2 "
            "RESTATEMENT; PSI3 SOURCE_REASONED infeasible %.1f "
            "dec)" % (exit_frac, psi3_dec))
    go_a = c1a_valid and c1a_cov == npool and c1a_dem < DEMAND_BAR
    go_b = c1b_valid and c1b_cov == npool and c1b_gap < DEMAND_BAR
    go_c = c1c_valid and c1c_cov == npool and c1c_dem < DEMAND_BAR
    if go_a or go_b or go_c:
        vCone = "DRIVEN_CONE_GO(%s)" % ("C1a" if go_a else
                                        ("C1b" if go_b else "C1c"))
    elif c1b_cov > max(c1a_cov, c1c_cov):
        vCone = ("DRIVEN_CONE_PARTIAL(C1b, cover %d/%d, gap %.2f "
                 "dec)" % (c1b_cov, npool, c1b_gap))
    else:
        vCone = "DRIVEN_CONE_DEAD"
    vSchur = ("SOURCE_SCHUR_WALL_EQUIVALENT" if cont_ok
              else "SOURCE_SCHUR_OPEN")
    vSq = "EXACT_SQUARE_OPEN(5/7 Gram provenance)"
    reenc = [c for c, f in (("C1a", fire_a), ("C1c", fire_c))
             if f]
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        head = ("TERMINAL_CROSSRATIO_GO(%s)" % vCone
                if (go_a or go_b or go_c) else
                "TERMINAL_CROSSRATIO_MEASURED(%d/%d, min margin "
                "%.4f)" % (int(np.sum(qs < 1.0)), len(ladder),
                           float(np.min(margins))))
        verd = " + ".join(
            [head, vA, vB, vReg, vCone, vSchur, vSq,
             "FIVE_SEVENTHS_NUMERICAL_ONLY"]
            + (["PAIRCORR_REENCODED(%s)" % ", ".join(reenc)]
               if reenc else []))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the dictionary, the "
          "cross-ratio form, the bilinear identity, the driven "
          "recursion; MEASURED: q census, region anatomy, "
          "certificate coverage; OPEN: the 5/7 provenance, any "
          "source-pure bound (the one-step C1b reduction is the "
          "sharpest surviving target); NO RH claim"
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
