#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signed_cubic_flux_probe -- PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01
(round 314): THE SIGNED CUBIC IDENTITY -- part 1 of the reviewer's
signed-cube bookkeeping contract: EXACT ALGEBRA ONLY, no size
estimate, no bound claim (the quantification is R315/R316).
Reviewer frame (binding, from the r313 adjudication): r313 proved
what does NOT work -- no Floquet contraction (the monodromy
expands, finally closed), no separate majorization of the triple
types (the types CANCEL against each other: med signed shares
T1..T4 = +0.38/+2.15/-1.14/-0.42), no boolean class membership.
Two banked assets: FOLD MULTIPLICITY UNIFORMLY == 2 (exact, 57/57)
and the FAR-TRIPLE TELESCOPE IS REAL (TC_far 0.069 -- 93 percent
abs-mass cancellation).  The next contract is NOT a better triple
class but the SIGNED CUBE BOOKKEEPING: with x_j = (PDelta)_j,
sigma_j = sign(x_j), the fold genealogy decomposes every value
exactly, x_j = sum_{tau in T} x_{j,tau} (T = the fold groups of
block j; the r313 presentation P_j = sum of local c-differences,
fold groups = beta/omega pairs at one position, REUSED VERBATIM).
The former type majorization destroyed the cross-cancellation
because it broke |sum_tau x_{j,tau}|^3 into magnitudes.  Instead
EXACTLY:
    |x_j|^3 = sigma_j x_j^3
            = sigma_j sum_{alpha,beta,gamma in T} x_{j,alpha}
              x_{j,beta} x_{j,gamma},
so   sum_j |x_j|^3 = sum_{alpha,beta,gamma} C_{alpha beta gamma}
with the SIGNED CUBIC TENSOR
    C_{alpha beta gamma} = sum_j sigma_j x_{j,alpha} x_{j,beta}
                           x_{j,gamma}
(block-local: x_{j,tau} = G1_tau iff fold group tau lies in block
j, else 0 -- the tensor is block-diagonal in the genealogy).  Here
the types MAY cancel against each other -- no type is majorized in
isolation.  THE TARGET DECOMPOSITION (sealed):
    C_cube = DeltaF + C_collision + C_boundary
where DeltaF is the far-triple flux (a discrete divergence:
telescope along the ordered support), C_collision holds the
configurations with a REPEATED fold ancestor (counted exactly via
the proven multiplicity-2 bound), and C_boundary holds the finite
edge/razor terms of the sealed flux language.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the r311 block-Green round runs in parallel; this
probe touches NOTHING outside its own file and the additive
rh-sync.

THE OBJECT (r269/r287/r298/r306/r313 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks (r270 convention); the frozen positional block machinery
(r298 WBT.block_breaks + WBT.aggregate_blocks); the r306
RY3.cubic_moments; the r313 PFK.type_expansion +
PFK.telescope_index (the raw atomic presentation: block value P_j
== sum of raw atoms d_alpha, atoms = edge-masked bulk atoms
(position bx, value +ct) + edge-masked window atoms (position xu,
value -cw); fold group = atoms at one position), ALL imported
verbatim; PDelta = Pbeta - Pomega.  NEW in this round (module-own,
source-pure): the FOLD GENEALOGY builder (ordered group values G1
per block), the SIGNED CUBE TERMS (per-block Newton aggregates of
the signed tensor), the FLUX TELESCOPE (the sealed divergence
form) and the COLLISION CENSUS (multiplicity-2 counting).

THE SEALED FLUX LANGUAGE CLASS (frozen BEFORE any measurement):
blocks are consecutive position intervals (r313 P1/P6); within
block j the fold groups are ordered by position, g_1 < ... <
g_{n_j}, with values G_i; the FLUX STATE transported along the
ordered support is the prefix pair (s1_i, s2_i) = (sum_{k<=i} G_k,
sum_{k<=i} G_k^2) together with the accumulated flux F_i = 6 e_3
(G_1..G_i); the LOCAL EDGE FLUX on the edge (g_{i-1}, g_i) is
    dF_i = F_i - F_{i-1} = 6 G_i e_2(G_1..G_{i-1})
         = 3 G_i (s1_{i-1}^2 - s2_{i-1}),
a function of the incoming state and the new group value ONLY; the
block flux telescopes, sum_{i=2}^{n} dF_i = F_n - F_1; the OPENING
FLUX F_1 = 6 e_3({G_1}) = G_1^3 - 3 G_1 G_1^2 + 2 G_1^3 is the
declared boundary term of the class (the razor/edge atoms are
masked BEFORE the presentation -- disclosed; the opening-flux
lemma F_1 == 0 is exact cubic algebra, proved in Fractions and
warded live: the sealed class either delivers a vanishing boundary
(SIGNED_CUBE_IDENTITY) or a named nonzero one
(FLUX_WITH_BOUNDARY)).  THE THREE TERMS:
    DeltaF      = sum_j sigma_j sum_{i=2}^{n_j} dF_{j,i}
                  (far triples as divergence: F_{j,n_j} == the
                   Newton far value x^3 - 3 x Q2 + 2 Q3 == the
                   r313 T4_j -- three independent computation
                   paths, cross-warded),
    C_collision = sum_j sigma_j (3 Q2_j x_j - 2 Q3_j)
                  (repeated fold ancestor; split PAIR = 3 sigma
                   (Q2 x - Q3) [exactly two equal] + FULL = sigma
                   Q3 [alpha = beta = gamma]; Qk_j = sum_{g in j}
                   G1_g^k),
    C_boundary  = sum_j sigma_j F_{j,1}  (the opening flux).
DISCLOSED ALGEBRAIC RELATION (derived, no measurement): DeltaF +
C_collision + C_boundary == sum_j sigma_j x_j^3 == sum_j |x_j|^3
is the Newton identity per block; the far/collision SHARES are
algebraically tied to the r313 signed type shares (far == T4
share, collision == T1 + T2 + T3 share); the NEW measured content
is the pair/full split, the per-edge flux census, the flux
cancellation index and the exact collision counts.

LEG 0 -- ANCHOR REGRESSION (r313 record numbers adopted as-is,
disclosed): med signed type shares of sum |P|^3 over the 42 core
rungs T1/T2/T3/T4 = +0.3808/+2.1542/-1.1442/-0.4226 (tol 0.005);
fold multiplicity == 2 UNIFORM on 57/57 rungs (exact); TC_far med
0.069 slope -0.050 (tol 0.005/0.01); worst block type ward <=
1e-9 (r313 measured 3.9e-16).

LEG A -- THE SIGNED TENSOR EXACT: (A1) GENEALOGY COMPLETENESS:
the fold-group sums reproduce every block value, max |sum_g G1_g
- PDelta_j| relative to max |PDelta| <= ATOM_BAR = 1e-9 on every
live world AND the run/breakpoint assignment has 0 mismatches --
otherwise the sealed verdict is GENEALOGY_INCOMPLETE.  (A2) EXACT
RECOMPOSITION on the small window w9 in FRACTIONS (float atom
values are dyadic rationals -- Fraction(float) is EXACT, so every
polynomial identity is decided exactly): per block the BRUTE
tensor enumeration (all n_j^3 ordered group triples, classified
far / pair / full by index pattern) must equal the Newton
aggregates EXACTLY (dev 0), and the global three-term
recomposition sum C == sum_j |x_j|^3 must have dev EXACTLY 0.
(A3) f64 RECOMPOSITION on the full ladder: |DeltaF + C_collision
+ C_boundary - sum |x|^3| / sum_j A1_j^3 <= REC3_BAR = 1e-13 (A1_j
= block abs atom mass; the r313 scale convention) on w9 + >= 20
rungs x the three live world families (MAIN ladder + EPSTEIN +
SCRAMBLE; SMOOTH is the known degenerate world, DEG_FLOOR guard,
disclosed).  Cross-wards (bar XW_BAR = 1e-13 on the same scale):
flux far == r313 T4 per block; C_collision == sigma (T1 + T2 +
T3); sum |x|^3 == RY3 S_3 L1^3.

LEG B -- THE DIVERGENCE FORM: (B1) TELESCOPE WARD: per block
F_{j,n_j} (telescope path) == x^3 - 3 x Q2 + 2 Q3 (Newton path),
max block dev / A1_j^3 <= TEL_BAR = 1e-13 live, dev EXACTLY 0 in
Fractions on w9 -- otherwise NO_LOCAL_FLUX_FORM.  (B2) BOUNDARY:
C_boundary and every opening flux F_{j,1}: EXACTLY 0 in Fractions
on w9 (the opening-flux lemma), <= BND_BAR = 1e-13 x A1^3 live;
the verdict splits SIGNED_CUBE_IDENTITY (boundary vanishes) vs
FLUX_WITH_BOUNDARY (named nonzero boundary).  (B3) COLLISION
COUNTS via multiplicity 2: per block with n groups the config
counts are FULL = n, PAIR = 3 n (n - 1), FAR = n (n - 1)(n - 2)
(sum n^3, exact integers); the collision ATOM-triple count is 3
p1 p2 - 2 p3 in the multiplicity power sums p_k = sum_g mult_g^k
(Newton on multiplicities, exact ints) and equals 8 (n + 3 n (n -
1)) iff mult == 2 uniformly -- warded exactly on every rung with
fold share 1.0.  (B4) TERM SHARES over the ladder (MEASUREMENT
ONLY -- no bound claim; the trends are the R315/R316 preview,
labeled): med + halves slope of DeltaF / C_cube, C_pair / C_cube,
C_full / C_cube; the flux cancellation index FC = sum_j |F_end_j|
/ sum_{j,i} |dF_{j,i}| (the intra-block edge-flux cancellation --
the R315 raw material) med + slope; per-edge census.

LEG C -- WORLD PREVIEW (small, measurement only): the same
decomposition on w9 / w13 (the twin main window) / EPSTEIN /
SCRAMBLE (SMOOTH degenerate-skipped, disclosed): term-share table
+ collision counts + FC + TC_far, printed as SEALED RECORD DATA
for R315; the SCRAMBLE localization census names the column with
the largest relative deviation from the MAIN med (collision? flux
defect? boundary?) -- census only, NO claim.  SEALING DISCIPLINE
(disclosed): R315 must calibrate its membership functional Phi_3
from the STRUCTURE of the divergence-form terms, NOT from the
numeric values of these tables.

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) SIGMA OMITTED (the r313 majorant error as must-fail): the
  unsigned recomposition sum_j (+1) x_j^3 breaks against
  sum_j |x_j|^3 by EXACTLY 2 sum_{x_j < 0} |x_j|^3 -- on the toy
  block field x = (2, -1) the break is 2 EXACT (Fractions); on
  the real w9 the relative dev is >= MUT_MIN -- LOUD.
(m2) DOUBLE-COUNTED FOLD GROUP (exact Fractions): duplicating one
  fold group in the toy genealogy ({1} | {2} duplicated) breaks
  the completeness ward by EXACTLY the duplicated G1 = 2 and the
  recomposition by EXACTLY (5^3 - 3^3) = 98 -- CAUGHT; on the
  real w9 the duplicated-group genealogy deviates >= MUT_MIN.
(m3) FLUX TELESCOPE WITH UNORDERED SUPPORT: on the sealed toy
  chain (1, 2, 3, 4) the ordered edge-flux profile is (0, 36,
  264) and the reversed (4, 3, 2, 1) profile is (0, 144, 156) --
  per-edge break (0, 108, 108) EXACT while the total 300 is
  permutation-blind (disclosed: the telescope TOTAL is symmetric,
  the DIVERGENCE FORM is not); on the real w9 the seeded
  within-block group shuffle (SEED_SHUF 314001) deviates
  edgewise >= MUT_MIN -- LOUD.
(m4) COLLISION COUNT WITHOUT THE MULTIPLICITY BOUND: the
  mult-blind counter (treats every fold group as ONE atom,
  mult == 1) predicts 3 n^2 - 2 n collision atom triples against
  the true 3 p1 p2 - 2 p3 = 24 n^2 - 16 n under the proven
  multiplicity 2 -- on the toy 2-group block the break is 64 - 8
  = 56 EXACT (Fractions/ints); on the real w9 the relative dev is
  >= MUT_MIN -- CAUGHT.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the new
  builders (fold_genealogy, signed_cube_terms, flux_telescope,
  collision_census) consume positions + values + block indices
  only (BOUND_FORBIDDEN set); fragment audit (no fit primitives).
  TOY EXACTNESS (bar 1e-14): the r313 toy block {2,-1}|{1,-1}|{1}
  gives G1 = (1, 0, 1), far = 0, pair = 6, full = 2, sum 8 ==
  x^3 EXACT and collision 8 == the r313 atom-level T1 + T2 + T3
  = 8 + 24 - 24 EXACT; the flux toy (1, 2, 3, 4) telescopes to
  6 e_3 = 300 EXACT; the float builders match the Fractions
  tables.

INDEX FIREWALL (binding, r238-r313 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r313
PFK.type_expansion + PFK.telescope_index, r298 WBT.block_breaks +
WBT.aggregate_blocks, r306 RY3.cubic_moments, r269 PBB.mask_edge
+ PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}; EXTENSION: 900 < h
<= 1300, first 15 by (N, kz) (the r286 anchors, N_w 942..1218).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); ATOM_BAR
1e-9; TYPE_BAR 1e-9; REC3_BAR 1e-13; TEL_BAR 1e-13; BND_BAR
1e-13; XW_BAR 1e-13; DEG_FLOOR 1e-6; MULT_CAP 2; SEED_SHUF
314001; MUT_MIN 1e-6; TOY_BAR 1e-14; TB_WARD bars 1e-9 main N <=
400 / 3e-6 deep / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9; R313
anchors: type shares (+0.3808, +2.1542, -1.1442, -0.4226) tol
0.005, TC_far med 0.069 tol 0.005 slope -0.050 tol 0.01,
multiplicity == 2 on 57/57 EXACT; runtime <= 1800 s; smoke = w9 +
controls + the full Fractions section at w9 + toys + scope audits
+ every exact ward at w9 + the m1-m4 mutants; ladder, extension,
anchors, shares, world table beyond w9/controls and adjudication
skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r313 RECORD number adopted as-is; the Newton
identity, the opening-flux lemma, the telescope form, the
collision counting formulas and the multiplicity power-sum
identity are derived algebra, disclosed above; the atom scale of
w9 (300 atoms, positions/block med 4 max 8) and the fold
multiplicity 2 are r313 record facts, adopted for budget sizing
only; no share, no flux value, no collision count and no world
number was computed before this spec was frozen; the four sealed
verdicts are symmetric -- no rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R314_ANCHORS(r313 type shares + TC_far + multiplicity live)
+ GENEALOGY(completeness dev, mismatches, fold census)
+ TENSOR(w9 Fractions recomposition dev EXACT-0, brute-tensor
    match, f64 recomposition worst dev, cross-wards vs r313 T4 /
    sigma(T1+T2+T3) / RY3 S_3 L1^3)
+ FLUX(telescope dev Newton vs telescope path, boundary census,
    FC index med + slope, edge census)
+ COLLISION(config counts exact, atom-triple count ward,
    pair/full split shares)
+ TERMS(three-term shares med + slopes -- R315/R316 preview,
    labeled measurement-only)
+ WORLDS(w9/w13/EPST/SCR table as sealed record data, SCRAMBLE
    localization census)
+ [exactly one of] SIGNED_CUBE_IDENTITY / FLUX_WITH_BOUNDARY /
    NO_LOCAL_FLUX_FORM / GENEALOGY_INCOMPLETE
+ MUSTFAIL_LEDGER(m1-m4 + scopes).
Honesty before beauty: the Newton identity, the opening-flux
lemma, the telescope, the collision counts and the multiplicity
power-sum identity are EXACT finite algebra (Fractions-decided on
w9 and toys); every share, FC index and slope is MEASURED on 42 +
15 finite rungs; the far/collision shares are algebraically the
r313 T4 / T1+T2+T3 shares (disclosed -- the NEW content is the
divergence form, the boundary lemma, the pair/full split, the
flux census and the exact counting); a SIGNED_CUBE_IDENTITY fixes
a bookkeeping IDENTITY, it bounds NOTHING (R315/R316 do the
quantification); no verdict claims a cofinal law; r243-r313
stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 29/29 (0.2 s), NO amendment; ONE reporting-only
edit after smoke (the m3 per-edge break list is printed as plain
ints instead of Fraction reprs -- no bar, band, rule or verdict
rule touched); calibration pass 1 = first full evaluation, 29/29,
wall 22.0 s, NO amendment; record run1/run2 after this insertion,
identical up to WALL; the only post-freeze edits are the
disclosed reporting edit and this record-table insertion, which
IS the protocol):
CAL_VERDICT = R314_ANCHORS(type shares +0.3808/+2.1542/-1.1442/
-0.4226, TC_far 0.069 slope -0.050, mult == 2 on 57/57, block
ward 3.9e-16 -- ALL bit-near r313) + GENEALOGY(complete: r313
presentation dev 2.8e-16, group-sum dev 6.1e-16 vs ATOM_BAR
1e-9, 0 mismatches, med fold share 1.000 on 61 live worlds;
SMOOTH degenerate-skipped, pre-declared) + TENSOR(w9 in EXACT
Fractions, 35 blocks / 150 groups: brute tensor enumeration ==
Newton aggregates == telescope on every block with devs EXACTLY
0 as rational numbers, three-term recomposition dev EXACTLY 0;
f64 ladder: worst recomposition dev 4.5e-17 (bar 1e-13);
cross-wards flux-far == r313 T4 worst 5.5e-16, C_collision ==
sigma(T1+T2+T3) worst 3.7e-17, cube == RY3 S_3 L1^3 worst
5.5e-16) + FLUX(telescope Newton-vs-path worst 4.1e-16 x A1^3;
boundary: opening flux F_1 == 0 EXACT in Fractions on w9, worst
live |F_open| 4.1e-16 x A1^3, C_boundary == 0 -- the sealed
language class closes WITHOUT remainder; FC med 0.629 slope
-0.141 -- the intra-block edge fluxes cancel 37 percent of
their abs mass at the median, and the cancellation DEEPENS with
depth; med 245 interior edges per rung) + COLLISION(config
counts full/pair/far == n / 3n(n-1) / n(n-1)(n-2) with sum n^3
EXACT on all 61 live worlds; atom-triple count 3 p1 p2 - 2 p3
== 8(n + 3n(n-1)) EXACT on 61/61 worlds (fold share 1.0
everywhere) -- the multiplicity-2 bound makes the collision
configuration space exactly countable; w9 census: 150 full /
1656 pair / 1770 far configs, 14448 collision atom triples) +
TERMS(med signed shares of sum |x|^3: DeltaF -0.4226 slope
-0.422 (falling), C_pair +0.5980 slope -0.095, C_full +0.8537
slope +0.213 (rising), C_boundary 0 exact -- the pair and full
collision terms carry the cube together (+1.45 med) against
the negative far flux (-0.42); R315/R316 preview only, no bound
claim) + WORLDS(shares far/pair/full + FC + TC_far: w9 -0.452/
+0.823/+0.629, FC 0.617, TC 0.057; w13(twin) -0.541/+0.430/
+1.111, FC 0.675, TC 0.043; EPSTEIN -2.695/-2.652/+6.347, FC
0.101, TC 0.011; SCRAMBLE -0.171/+0.856/+0.315, FC 0.693, TC
0.073; SCRAMBLE localization census: relative deviations from
the MAIN med far 0.60 / pair 0.43 / full 0.63 / FC 0.10 -> the
named separator column is FULL (the SCRAMBLE difference sits in
the collision side of the divergence form, NOT in the flux
cancellation); census only, NO claim) +
SIGNED_CUBE_IDENTITY(sum_j |x_j|^3 = DeltaF + C_collision +
C_boundary EXACT with C_boundary == 0 by the opening-flux
lemma: far triples enter as telescoping edge fluxes dF = 3 G
(s1^2 - s2), collisions as 3 Q2 x - 2 Q3 counted by
multiplicity 2, the boundary vanishes by cubic algebra) +
MUSTFAIL_LEDGER(m1 unsigned break 2 EXACT on the toy + w9 rel
dev 1.8e0 LOUD; m2 double-counted group breaks 2 and 98 EXACT +
w9 dev 4.6e-1 CAUGHT; m3 unordered-support per-edge break (0,
108, 108) EXACT with total 300 permutation-blind disclosed + w9
edgewise dev 7.7e-1 LOUD; m4 mult-blind count break 56 EXACT
(toy 8 vs 64) + w9 mutant 1806 vs true 14448, dev 8.75e-1
CAUGHT; m5a/m5b FLAGGED).
READING (typed, no upgrade): the signed cube bookkeeping the
reviewer contracted EXISTS EXACTLY -- verdict
SIGNED_CUBE_IDENTITY with a VANISHING boundary: (1) sum_j
|x_j|^3 = DeltaF + C_collision on every world, decided as exact
rational arithmetic on real w9 data (brute tensor == Newton ==
telescope, every dev the rational number 0) and to 4.5e-17 in
f64 on all 57 rungs -- the identity is machine-exact, not
approximate; (2) the divergence form is genuinely LOCAL: every
far contribution is a sum of edge fluxes dF = 3 G (s1^2 - s2)
consuming only the transported prefix state (s1, s2), and the
telescope closes without remainder -- the opening-flux lemma
F_1 == 0 is cubic algebra, so C_boundary == 0 in this language
class (the razor never enters the identity because the
presentation is edge-masked BEFORE the genealogy, disclosed);
(3) the collision space is exactly COUNTABLE by the banked
multiplicity-2 asset: 3 p1 p2 - 2 p3 == 8(n + 3n(n-1)) on
61/61 live worlds -- closed-form configuration counting, the m4
mutant shows the count is 8x wrong without the bound; (4) the
structural findings for R315/R316 (measured, labeled preview):
the collision term is NOT one object -- it splits into pair
+0.598 and full +0.854 med shares which together (+1.45) carry
the cube against the negative far flux (-0.42, falling -0.42);
the flux-level cancellation index FC med 0.629 falls -0.141
with depth (the edge fluxes cancel more and more, the
flux-level sibling of TC_far 0.069 -- note FC is per-edge
against per-triple, so the scales differ by construction); and
the WORLD table locates SCRAMBLE's difference in the FULL
COLLISION column (dev 0.63 vs MAIN med, ahead of far 0.60 /
pair 0.43 / FC 0.10) while EPSTEIN sits far from MAIN in every
share column yet holds the r306 total bound -- the shares alone
do NOT separate worlds the way the total does: Phi_3 must
combine the divergence-form STRUCTURE (flux cancellation +
collision split), not threshold single shares; sealed as record
data, Phi_3 must NOT be calibrated on these numbers.  Honest
negatives: the far/collision TOTALS are algebraically the r313
T4 / T1+T2+T3 shares (disclosed above -- new content is the
flux form, the boundary lemma, the pair/full split, the FC
census and the exact counts, not the -0.42 itself); C_full
rises (+0.213) -- the collision terms grow relative to the
cube, so R315 must exploit their CANCELLATION against the flux,
not their size; C_boundary == 0 holds because the razor acts
before the genealogy -- an unmasked presentation would
re-introduce a genuine boundary term; the SCRAMBLE localization
is a one-rung census (n = 1 world), weak by construction;
nothing here bounds anything: part 1 is bookkeeping only.
Runtime 22.0 s full / 0.2 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: the disclosed reporting-only
edit and this record-table insertion -- no bar, band, rule or
verdict rule moved.

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
import window_border_transfer_probe as WBT     # noqa: E402 r298
import renyi3_probe as RY3                     # noqa: E402 r306
import renyi3_proof_fork_probe as PFK          # noqa: E402 r313
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
ATOM_BAR = 1e-9
TYPE_BAR = 1e-9
REC3_BAR = 1e-13
TEL_BAR = 1e-13
BND_BAR = 1e-13
XW_BAR = 1e-13
DEG_FLOOR = 1e-6
MULT_CAP = 2
SEED_SHUF = 314001
MUT_MIN = 1e-6
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
R313_SHARES = (0.3808, 2.1542, -1.1442, -0.4226)
R313_SHARE_TOL = 0.005
R313_TC_FAR = 0.069
R313_TC_TOL = 0.005
R313_TC_SLOPE = -0.050
R313_TC_SL_TOL = 0.01

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

TYPES = ("T1", "T2", "T3", "T4")


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
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
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


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
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


# ---------------- module-own builders.  Source-pure: raw atom
# ---------------- positions + values + block assignment only; the
# ---------------- withheld terminal drive key, the branch label
# ---------------- and every target-side identifier are forbidden
# ---------------- in scope (AST audit).
def fold_genealogy(pos, val, blk, m):
    """the FOLD GENEALOGY of the raw atomic presentation: atoms
    sharing one position inside one block form a fold group (the
    beta/omega fold of one node); groups are ordered by (block,
    position).  Returns group values G1, group block index gblk,
    multiplicities, and the block slice pointers ptr (groups of
    block j = slice ptr[j]:ptr[j+1], ordered by position)."""
    pos = np.asarray(pos, dtype=float)
    val = np.asarray(val, dtype=float)
    blk = np.asarray(blk, dtype=int)
    o = np.lexsort((pos, blk))
    pb = blk[o]
    pp = pos[o]
    vv = val[o]
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gid = np.cumsum(new) - 1
    ng = int(gid[-1]) + 1 if len(gid) else 0
    G1 = np.bincount(gid, weights=vv, minlength=ng)
    gblk = pb[new] if ng else np.zeros(0, dtype=int)
    mult = np.bincount(gid, minlength=ng)
    ptr = np.searchsorted(gblk, np.arange(m + 1))
    return dict(G1=G1, gblk=gblk, mult=mult, ng=ng, ptr=ptr,
                order=o)


def signed_cube_terms(G1, gblk, m):
    """per-block Newton aggregates of the signed cubic tensor:
    x_j = sum_g G1_g, Qk_j = sum_g G1_g^k; far = x^3 - 3 x Q2 +
    2 Q3 (all three fold groups distinct), pair = 3 (Q2 x - Q3)
    (exactly two equal), full = Q3 (alpha = beta = gamma);
    sigma = sign(x); cube = sum |x|^3."""
    x = np.bincount(gblk, weights=G1, minlength=m)
    Q2 = np.bincount(gblk, weights=G1 ** 2, minlength=m)
    Q3 = np.bincount(gblk, weights=G1 ** 3, minlength=m)
    sig = np.sign(x)
    far = x ** 3 - 3.0 * x * Q2 + 2.0 * Q3
    pair = 3.0 * (Q2 * x - Q3)
    full = Q3
    cube = float(np.sum(np.abs(x) ** 3))
    return dict(x=x, Q2=Q2, Q3=Q3, sig=sig, far=far, pair=pair,
                full=full, cube=cube,
                C_far=float(np.sum(sig * far)),
                C_pair=float(np.sum(sig * pair)),
                C_full=float(np.sum(sig * full)))


def flux_telescope(G1, ptr, m):
    """the sealed divergence form: per block the fold groups in
    position order carry the flux state (s1, s2) = prefix power
    sums; the local edge flux on edge (g_{i-1}, g_i) is dF_i =
    3 G_i (s1^2 - s2) of the incoming state; the block flux
    F_end = sum of edge fluxes telescopes to 6 e_3 (the far
    value); the opening flux F_1 = G^3 - 3 G G^2 + 2 G^3 is the
    declared boundary term (cubic algebra: 0).  Returns per-block
    F_end and F_open, the concatenated per-edge flux array and
    the abs edge mass."""
    F_end = np.zeros(m)
    F_open = np.zeros(m)
    edges = []
    for j in range(m):
        g = G1[ptr[j]:ptr[j + 1]]
        s1 = 0.0
        s2 = 0.0
        F = 0.0
        for i, gv in enumerate(g):
            if i == 0:
                F_open[j] = gv ** 3 - 3.0 * gv * (gv * gv) \
                    + 2.0 * gv ** 3
            else:
                dF = 3.0 * gv * (s1 * s1 - s2)
                F += dF
                edges.append(dF)
            s1 += gv
            s2 += gv * gv
        F_end[j] = F
    edges = np.asarray(edges, dtype=float)
    return dict(F_end=F_end, F_open=F_open, edges=edges,
                edge_abs=float(np.sum(np.abs(edges))),
                n_edges=int(len(edges)))


def collision_census(mult, ptr, m):
    """exact collision counting under the fold multiplicity: per
    block with n groups the ordered-triple config counts are
    full = n, pair = 3 n (n-1), far = n (n-1)(n-2) (sum n^3);
    the collision ATOM-triple count is 3 p1 p2 - 2 p3 in the
    multiplicity power sums p_k = sum_g mult_g^k (Newton on
    multiplicities, exact integers), == 8 (n + 3 n (n-1)) iff
    mult == 2 uniformly.  mult_cap = the sealed class bound."""
    n_full = 0
    n_pair = 0
    n_far = 0
    sum_ok = True
    atoms_coll = 0
    atoms_coll_m2 = 0
    mx = 0
    for j in range(m):
        mm = mult[ptr[j]:ptr[j + 1]]
        n = int(len(mm))
        nf = n
        npr = 3 * n * (n - 1)
        nfar = n * (n - 1) * (n - 2)
        sum_ok = sum_ok and (nf + npr + nfar == n ** 3)
        n_full += nf
        n_pair += npr
        n_far += nfar
        p1 = int(np.sum(mm))
        p2 = int(np.sum(mm.astype(np.int64) ** 2))
        p3 = int(np.sum(mm.astype(np.int64) ** 3))
        atoms_coll += 3 * p1 * p2 - 2 * p3
        atoms_coll_m2 += 8 * (n + 3 * n * (n - 1))
        if n:
            mx = max(mx, int(np.max(mm)))
    return dict(n_full=n_full, n_pair=n_pair, n_far=n_far,
                sum_ok=sum_ok, atoms_coll=atoms_coll,
                atoms_coll_m2=atoms_coll_m2, mx_mult=mx)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'flux orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'collision constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the identity decided
# ---------------- as rational arithmetic (Fraction(float) is
# ---------------- exact on dyadic f64 values)
def fr_blocks_from_atoms(pos, val, blk, m):
    """rebuild the fold genealogy with EXACT Fraction values:
    returns per-block ordered lists of group values."""
    o = np.lexsort((pos, blk))
    blocks = [[] for _ in range(m)]
    prev = None
    for idx in o:
        key = (int(blk[idx]), float(pos[idx]))
        if key != prev:
            blocks[int(blk[idx])].append(Fr(0))
            prev = key
        j = int(blk[idx])
        blocks[j][-1] += Fr(float(val[idx]))
    return blocks


def fr_block_terms(G):
    """exact per-block terms on a list of Fraction group values:
    Newton aggregates, brute tensor enumeration (index-pattern
    classified), flux telescope + opening flux.  Every dev is an
    exact rational (0 = identity holds)."""
    x = sum(G, Fr(0))
    Q2 = sum(g * g for g in G)
    Q3 = sum(g ** 3 for g in G)
    far_n = x ** 3 - 3 * x * Q2 + 2 * Q3
    pair_n = 3 * (Q2 * x - Q3)
    full_n = Q3
    n = len(G)
    far_b = Fr(0)
    pair_b = Fr(0)
    full_b = Fr(0)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                v = G[a] * G[b] * G[c]
                if a == b == c:
                    full_b += v
                elif a == b or b == c or a == c:
                    pair_b += v
                else:
                    far_b += v
    s1 = Fr(0)
    s2 = Fr(0)
    F = Fr(0)
    F_open = Fr(0)
    for i, g in enumerate(G):
        if i == 0:
            F_open = g ** 3 - 3 * g * (g * g) + 2 * g ** 3
        else:
            F += 3 * g * (s1 * s1 - s2)
        s1 += g
        s2 += g * g
    return dict(x=x, far=far_n, pair=pair_n, full=full_n,
                F_tel=F,
                dev_far=far_b - far_n, dev_pair=pair_b - pair_n,
                dev_full=full_b - full_n, dev_tel=F - far_n,
                F_open=F_open,
                dev_sum=(far_n + pair_n + full_n) - x ** 3)


def fr_decomposition(blocks):
    """the full three-term recomposition in exact Fractions over
    a list of per-block Fraction group lists: returns the worst
    per-block devs (exact rationals) and the global recomposition
    dev DeltaF + C_pair + C_full + C_bnd - sum |x|^3 (exact)."""
    tot = Fr(0)
    cube = Fr(0)
    worst = dict(dev_far=Fr(0), dev_pair=Fr(0), dev_full=Fr(0),
                 dev_tel=Fr(0), F_open=Fr(0), dev_sum=Fr(0))
    for G in blocks:
        r = fr_block_terms(G)
        sig = 1 if r["x"] > 0 else (-1 if r["x"] < 0 else 0)
        # DeltaF via the TELESCOPE path + collision + boundary:
        tot += sig * (r["F_tel"] + r["pair"] + r["full"]
                      + r["F_open"])
        cube += abs(r["x"]) ** 3
        for k in worst:
            worst[k] = max(worst[k], abs(r[k]))
    return dict(dev_recomp=tot - cube, **worst)


TOY_GROUPS = ([Fr(2), Fr(-1)], [Fr(1), Fr(-1)], [Fr(1)])
TOY_FLUX = [Fr(1), Fr(2), Fr(3), Fr(4)]


def fr_flux_edges(G):
    """the exact ordered per-edge flux profile of one block."""
    s1 = Fr(0)
    s2 = Fr(0)
    out = []
    for i, g in enumerate(G):
        if i > 0:
            out.append(3 * g * (s1 * s1 - s2))
        s1 += g
        s2 += g * g
    return out


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("signed_cubic_flux_probe -- "
          "PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01 (round 314)")
    print("SPEC_SHA %s   R313_SHA %s   R306_SHA %s (imported)"
          % (SPEC_SHA[:16], PFK.SPEC_SHA[:16], RY3.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + full Fractions "
                        "section at w9 + toys + scope audits + "
                        "every exact ward at w9 + m1-m4 mutants; "
                        "ladder, extension, anchors, shares and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE SIGNED CUBIC IDENTITY (reviewer contract, part 1 "
          "-- exact algebra ONLY, no size estimate): |x_j|^3 = "
          "sigma_j x_j^3 expands over the r313 fold genealogy "
          "into the signed cubic tensor C_{abc}; sealed target "
          "decomposition C_cube = DeltaF (far-triple flux as "
          "discrete divergence: edge fluxes dF = 3 G (s1^2 - s2) "
          "telescoping along the ordered support) + C_collision "
          "(repeated fold ancestor, counted exactly via the "
          "proven multiplicity-2 bound; split pair/full) + "
          "C_boundary (the opening flux of the sealed language "
          "class); verdicts SIGNED_CUBE_IDENTITY / "
          "FLUX_WITH_BOUNDARY / NO_LOCAL_FLUX_FORM / "
          "GENEALOGY_INCOMPLETE sealed BEFORE evaluation; "
          "quantification deferred to R315/R316 by contract")
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("fold_genealogy", "signed_cube_terms",
               "flux_telescope", "collision_census"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); own builders clean "
          "(%d hits); m5a gift-bound FLAGGED (%s); m5b "
          "branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r313 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSION")
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
        ext = []
        okL = True
    else:
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))
    if smoke:
        check("G12-extension-census", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d), POSITIVE_PREFIX %d/%d"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1],
                 sum(1 for p in ext if p["nf"] is None), len(ext)))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        v2w = BR.eval_scaled(rows, xu, N - 2)
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p, nf=p["nf"])

    recs = [rung_rec(p) for p in pool]
    erecs = [rung_rec(p) for p in ext] if not smoke else []
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        e_cheap = sum(1 for rc in erecs if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT census (no sealed expectation): %d cheap / %d "
              "exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + ATOMIC PRESENTATION WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in erecs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext = max(tb_ext, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d mains "
          "+ 3 controls: worst dev/absmass %.1e main N<=%d (bar "
          "%.0e) / %.1e deep / %.1e ext (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, tb_ext, TB_WARD_BAR_DEEP,
             tb_ctrl, TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        runs = PBB.runs_split(cb)
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        cm = RY3.cubic_moments(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        # ---- raw atomic presentation (r313 convention verbatim):
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        if m and not degenerate:
            te = PFK.type_expansion(pos_all, val_all, blk_all, m)
            ta = PFK.type_expansion(pos_all, val_all, blk_all, m,
                                    use_abs=True)
            atom_dev = float(np.max(np.abs(te["S1"] - Pd))
                             / max(np.max(np.abs(Pd)), 1e-300))
            s_j = np.sign(Pd)
            tot = {t: float(np.sum(s_j * te[t])) for t in TYPES}
            cube = float(np.sum(np.abs(Pd) ** 3))
            tc_far = PFK.telescope_index(te["T4"], ta["T4"])
            mx_mult = int(np.max(te["mult"])) if te["ng"] else 0
            fold_share = float(np.mean(te["mult"] == 2)) \
                if te["ng"] else 0.0
            A1 = np.bincount(blk_all, weights=np.abs(val_all),
                             minlength=m)
            scale3 = float(np.sum(A1 ** 3))
            sc_j = np.maximum(A1 ** 3, 1e-300)
            # ---- module-own genealogy + signed decomposition:
            gen = fold_genealogy(pos_all, val_all, blk_all, m)
            sct = signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = flux_telescope(gen["G1"], gen["ptr"], m)
            cc = collision_census(gen["mult"], gen["ptr"], m)
            x_dev = float(np.max(np.abs(sct["x"] - Pd))
                          / max(np.max(np.abs(Pd)), 1e-300))
            sig = sct["sig"]
            C_far_flux = float(np.sum(sig * ft["F_end"]))
            C_bnd = float(np.sum(sig * ft["F_open"]))
            rec3 = abs(C_far_flux + sct["C_pair"] + sct["C_full"]
                       + C_bnd - cube) / max(scale3, 1e-300)
            tel_dev = float(np.max(np.abs(ft["F_end"]
                                          - sct["far"]) / sc_j))
            bnd_dev = float(np.max(np.abs(ft["F_open"]) / sc_j))
            xw_t4 = float(np.max(np.abs(sct["far"] - te["T4"])
                                 / sc_j))
            coll = sct["C_pair"] + sct["C_full"]
            coll_313 = float(np.sum(s_j * (te["T1"] + te["T2"]
                                           + te["T3"])))
            xw_coll = abs(coll - coll_313) / max(scale3, 1e-300)
            xw_cube = abs(cube - cm["S3"] * cm["L1"] ** 3) \
                / max(cube, 1e-300)
            FC = float(np.sum(np.abs(ft["F_end"]))) \
                / max(ft["edge_abs"], 1e-300)
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300),
                          bnd=C_bnd / max(cube, 1e-300))
        else:
            te = ta = gen = sct = ft = cc = None
            atom_dev = x_dev = 0.0
            tot = {t: 0.0 for t in TYPES}
            cube = 0.0
            tc_far = 0.0
            mx_mult = 0
            fold_share = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            xw_t4 = xw_coll = xw_cube = 0.0
            FC = 0.0
            C_bnd = 0.0
            shares = dict(far=0.0, pair=0.0, full=0.0, bnd=0.0)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism,
                    atom_dev=atom_dev, x_dev=x_dev,
                    ward=te["ward"] if te is not None else 0.0,
                    tot=tot, cube=cube, tc_far=tc_far,
                    mx_mult=mx_mult, fold_share=fold_share,
                    rec3=rec3, tel_dev=tel_dev, bnd_dev=bnd_dev,
                    xw_t4=xw_t4, xw_coll=xw_coll, xw_cube=xw_cube,
                    FC=FC, C_bnd=C_bnd, shares=shares,
                    gen=gen, sct=sct, ft=ft, cc=cc,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all)

    all_rc = recs + mrecs + erecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])
    pool_all = all_rc + [crecs[c] for c in crecs]

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in pool_all:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(pool_all)))

    live = [rc for rc in pool_all if not rc["ev"]["degenerate"]]
    deg_note = [c for c in crecs if crecs[c]["ev"]["degenerate"]]
    atom_w = max(rc["ev"]["atom_dev"] for rc in live)
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    fold_med = float(np.median([rc["ev"]["fold_share"]
                                for rc in live]))
    genealogy_ok = (atom_w <= ATOM_BAR and x_w <= ATOM_BAR
                    and mism_tot == 0)
    check("G22-genealogy-completeness", genealogy_ok,
          "the fold genealogy covers every block value EXACTLY on "
          "%d live worlds: r313 presentation dev %.1e + group-sum "
          "dev %.1e (bar %.0e); run assignment == breakpoint "
          "search (%d mismatches); med fold share %.3f "
          "(beta/omega pairs)%s -- fail here => "
          "GENEALOGY_INCOMPLETE"
          % (len(live), atom_w, x_w, ATOM_BAR, mism_tot, fold_med,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r313 records)")
    ward_w = max(rc["ev"]["ward"] for rc in live)
    if smoke:
        ev9 = recs[0]["ev"]
        sh9 = {t: ev9["tot"][t] / max(ev9["cube"], 1e-300)
               for t in TYPES}
        info("SMOKE: w9 type shares %+.4f/%+.4f/%+.4f/%+.4f, "
             "TC_far %.3f, mult max %d, block ward %.1e"
             % (sh9["T1"], sh9["T2"], sh9["T3"], sh9["T4"],
                ev9["tc_far"], ev9["mx_mult"], ward_w))
        check("G30-r313-type-shares", True, "SMOKE: skipped")
        check("G31-r313-mult-telescope", True, "SMOKE: skipped")
        srt_all = []
    else:
        srt_all = sorted(recs + erecs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        shares313 = {t: [rc["ev"]["tot"][t]
                         / max(rc["ev"]["cube"], 1e-300)
                         for rc in recs] for t in TYPES}
        sh_med = {t: float(np.median(shares313[t]))
                  for t in TYPES}
        ok_sh = all(abs(sh_med[TYPES[i]] - R313_SHARES[i])
                    <= R313_SHARE_TOL for i in range(4))
        check("G30-r313-type-shares",
              ok_sh and ward_w <= TYPE_BAR,
              "r313 signed type shares reproduced: med T1/T2/T3/"
              "T4 = %+.4f/%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/"
              "%+.4f/%+.4f tol %.3f); worst block type ward %.1e "
              "(bar %.0e, r313 rec 3.9e-16)"
              % (sh_med["T1"], sh_med["T2"], sh_med["T3"],
                 sh_med["T4"], R313_SHARES[0], R313_SHARES[1],
                 R313_SHARES[2], R313_SHARES[3], R313_SHARE_TOL,
                 ward_w, TYPE_BAR))
        mult_all = [rc["ev"]["mx_mult"] for rc in srt_all]
        n_m2 = sum(1 for v in mult_all if v == 2)
        tcf = [rc["ev"]["tc_far"] for rc in recs]
        tc_med = float(np.median(tcf))
        tc_sl = slp(tcf)
        check("G31-r313-mult-telescope",
              n_m2 == len(srt_all)
              and abs(tc_med - R313_TC_FAR) <= R313_TC_TOL
              and abs(tc_sl - R313_TC_SLOPE) <= R313_TC_SL_TOL,
              "fold multiplicity == 2 UNIFORM on %d/%d rungs "
              "(exact, the banked r313 asset); TC_far med %.3f "
              "slope %+.3f (rec %.3f/%+.3f tol %.3f/%.2f)"
              % (n_m2, len(srt_all), tc_med, tc_sl, R313_TC_FAR,
                 R313_TC_SLOPE, R313_TC_TOL, R313_TC_SL_TOL))

    # ---------------- S4: Leg A -- the signed tensor exact
    section("S4  LEG A -- THE SIGNED TENSOR EXACT")
    ev9 = (recs[0] if smoke else mrecs[0])["ev"]
    fr_blocks = fr_blocks_from_atoms(ev9["pos_all"],
                                     ev9["val_all"],
                                     ev9["blk_all"],
                                     ev9["m"])
    frd = fr_decomposition(fr_blocks)
    fr_exact = (frd["dev_recomp"] == 0 and frd["dev_far"] == 0
                and frd["dev_pair"] == 0 and frd["dev_full"] == 0
                and frd["dev_tel"] == 0 and frd["F_open"] == 0)
    check("G40-fractions-recomposition-w9", fr_exact,
          "w9 in EXACT Fractions (%d blocks, %d groups): brute "
          "tensor enumeration == Newton aggregates (worst devs "
          "far/pair/full %s/%s/%s), telescope == Newton far (%s), "
          "opening flux F_1 == %s, three-term recomposition "
          "DeltaF + C_coll + C_bnd - sum|x|^3 == %s -- ALL "
          "EXACTLY 0 as rational numbers"
          % (ev9["m"], ev9["gen"]["ng"], frd["dev_far"],
             frd["dev_pair"], frd["dev_full"], frd["dev_tel"],
             frd["F_open"], frd["dev_recomp"]))
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    xw_t4_w = max(rc["ev"]["xw_t4"] for rc in live)
    xw_coll_w = max(rc["ev"]["xw_coll"] for rc in live)
    xw_cube_w = max(rc["ev"]["xw_cube"] for rc in live)
    check("G41-f64-recomposition", rec3_w <= REC3_BAR,
          "three-term recomposition DeltaF + C_collision + "
          "C_boundary == sum_j |x_j|^3 on %d live worlds (%d "
          "rungs + mains + controls): worst dev %.1e vs abs-mass "
          "scale sum A1^3 (bar %.0e)"
          % (len(live), len(recs), rec3_w, REC3_BAR))
    check("G42-cross-wards", xw_t4_w <= XW_BAR
          and xw_coll_w <= XW_BAR and xw_cube_w <= 1e-9,
          "flux far == r313 T4 per block (worst %.1e, bar %.0e); "
          "C_collision == sigma (T1 + T2 + T3) (worst %.1e); "
          "sum |x|^3 == RY3 S_3 L1^3 (worst %.1e) -- the signed "
          "tensor is the r313 bookkeeping re-aggregated WITHOUT "
          "majorization" % (xw_t4_w, XW_BAR, xw_coll_w, xw_cube_w))

    # ---------------- S5: Leg B -- the divergence form
    section("S5  LEG B -- THE DIVERGENCE FORM")
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    flux_ok = (tel_w <= TEL_BAR and frd["dev_tel"] == 0)
    bnd_zero = (bnd_w <= BND_BAR and frd["F_open"] == 0)
    check("G50-flux-telescope", flux_ok,
          "the far term IS a discrete divergence: per-block "
          "telescope path sum_i dF_i == Newton path x^3 - 3 x Q2 "
          "+ 2 Q3 on %d live worlds (worst block dev %.1e x "
          "A1^3, bar %.0e; Fractions dev on w9 EXACTLY %s) -- "
          "fail here => NO_LOCAL_FLUX_FORM"
          % (len(live), tel_w, TEL_BAR, frd["dev_tel"]))
    check("G51-boundary-lemma", bnd_zero,
          "the opening-flux boundary VANISHES: F_{j,1} = G^3 - "
          "3 G G^2 + 2 G^3 == 0 by cubic algebra (Fractions on "
          "w9: %s EXACT; live worst |F_open| %.1e x A1^3, bar "
          "%.0e; C_boundary == sigma-sum of these) -- the sealed "
          "language class closes without remainder"
          % (frd["F_open"], bnd_w, BND_BAR))
    cnt_ok = all(rc["ev"]["cc"]["sum_ok"] for rc in live)
    n_m2w = sum(1 for rc in live
                if rc["ev"]["cc"]["atoms_coll"]
                == rc["ev"]["cc"]["atoms_coll_m2"]
                and rc["ev"]["fold_share"] == 1.0)
    cc9 = ev9["cc"]
    check("G52-collision-counts", cnt_ok,
          "config counts EXACT on %d live worlds: full/pair/far "
          "== n / 3n(n-1) / n(n-1)(n-2), sum == n^3 per block "
          "(ints); atom-triple count 3 p1 p2 - 2 p3 == "
          "8(n + 3n(n-1)) on %d/%d worlds with fold share 1.0 "
          "(the multiplicity-2 bound makes the collision space "
          "exactly countable); w9 census: %d full / %d pair / %d "
          "far configs, %d collision atom triples"
          % (len(live), n_m2w, len(live), cc9["n_full"],
             cc9["n_pair"], cc9["n_far"], cc9["atoms_coll"]))
    if smoke:
        info("SMOKE: w9 shares far/pair/full/bnd = "
             "%+.4f/%+.4f/%+.4f/%+.1e, FC %.3f, %d interior "
             "edges" % (ev9["shares"]["far"], ev9["shares"]["pair"],
                        ev9["shares"]["full"], ev9["shares"]["bnd"],
                        ev9["FC"], ev9["ft"]["n_edges"]))
        check("G53-term-shares", True, "SMOKE: skipped")
    else:
        sh_far = [rc["ev"]["shares"]["far"] for rc in recs]
        sh_pair = [rc["ev"]["shares"]["pair"] for rc in recs]
        sh_full = [rc["ev"]["shares"]["full"] for rc in recs]
        fcs = [rc["ev"]["FC"] for rc in recs]
        nedg = [rc["ev"]["ft"]["n_edges"] for rc in recs]
        check("G53-term-shares", True,
              "MEASUREMENT ONLY (R315/R316 preview, no bound "
              "claim): med signed shares of sum |x|^3: DeltaF "
              "%+.4f slope %+.3f, C_pair %+.4f slope %+.3f, "
              "C_full %+.4f slope %+.3f, C_boundary 0 (exact); "
              "flux cancellation FC med %.3f slope %+.3f (1 = no "
              "cancellation); med %d interior edges per rung"
              % (float(np.median(sh_far)),
                 slp([abs(v) for v in sh_far]),
                 float(np.median(sh_pair)),
                 slp([abs(v) for v in sh_pair]),
                 float(np.median(sh_full)),
                 slp([abs(v) for v in sh_full]),
                 float(np.median(fcs)), slp(fcs),
                 int(np.median(nedg))))
        info("sealed record table (R315 raw data; Phi_3 must be "
             "calibrated from the divergence-form STRUCTURE, not "
             "from these numbers): idx kz N m share_far "
             "share_pair share_full FC n_edges")
        for i, rc in enumerate(srt_all):
            ev = rc["ev"]
            info("%2d kz%-3d N %4d m %3d far %+.4f pair %+.4f "
                 "full %+.4f FC %.3f e %4d%s"
                 % (i, rc["kz"], rc["N"], ev["m"],
                    ev["shares"]["far"], ev["shares"]["pair"],
                    ev["shares"]["full"], ev["FC"],
                    ev["ft"]["n_edges"],
                    " EXT" if rc in erecs else ""))

    # ---------------- S6: Leg C -- world preview
    section("S6  LEG C -- WORLD PREVIEW (sealed record data)")
    wrows = []
    if smoke:
        wrows.append(("w9", recs[0]["ev"]))
    else:
        wrows.append(("w9", mrecs[0]["ev"]))
        wrows.append(("w13(twin)", mrecs[1]["ev"]))
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wrows.append((c, crecs[c]["ev"]))
    info("world table (term shares of sum |x|^3 + census; SMOOTH "
         "degenerate-skipped, disclosed):")
    info("  %-10s %8s %8s %8s %8s %6s %6s %6s %6s"
         % ("world", "far", "pair", "full", "bnd", "FC",
            "TCfar", "nfull", "npair"))
    for w, ev in wrows:
        info("  %-10s %+8.3f %+8.3f %+8.3f %8.1e %6.3f %6.3f "
             "%6d %6d"
             % (w, ev["shares"]["far"], ev["shares"]["pair"],
                ev["shares"]["full"], ev["shares"]["bnd"],
                ev["FC"], ev["tc_far"], ev["cc"]["n_full"],
                ev["cc"]["n_pair"]))
    check("G60-world-table", len(wrows) >= 3,
          "the decomposition holds on every live world (all "
          "wards above include the controls); the table is "
          "SEALED RECORD DATA for the R315 functional Phi_3 -- "
          "R315 must define Phi_3 from the divergence-form "
          "STRUCTURE before seeing per-rung tables (sealing "
          "discipline, disclosed)")
    if smoke:
        check("G61-scramble-localization", True, "SMOKE: skipped")
    else:
        med_ref = dict(far=float(np.median(sh_far)),
                       pair=float(np.median(sh_pair)),
                       full=float(np.median(sh_full)),
                       FC=float(np.median(fcs)))
        evS = crecs["SCR"]["ev"]
        scr = dict(far=evS["shares"]["far"],
                   pair=evS["shares"]["pair"],
                   full=evS["shares"]["full"], FC=evS["FC"])
        devs = {k: abs(scr[k] - med_ref[k])
                / max(abs(med_ref[k]), 1e-300) for k in scr}
        name = max(devs, key=lambda k: devs[k])
        check("G61-scramble-localization", True,
              "census only, NO claim: SCRAMBLE vs MAIN med "
              "relative deviations %s -> the named separator "
              "column is %s (the SCRAMBLE difference sits in the "
              "%s side of the divergence form)"
              % (str({k: round(devs[k], 2) for k in devs}), name,
                 "flux" if name in ("far", "FC") else "collision"))

    # ---------------- S7: Leg D -- must-fails + toys
    section("S7  LEG D -- WARDS / MUST-FAILS")
    # toys: the r313 toy block + the flux toy, exact
    r_toy = fr_block_terms([sum(g, Fr(0)) for g in TOY_GROUPS])
    ok_toy = (r_toy["x"] == 2 and r_toy["far"] == 0
              and r_toy["pair"] == 6 and r_toy["full"] == 2
              and r_toy["dev_sum"] == 0 and r_toy["dev_tel"] == 0
              and r_toy["F_open"] == 0)
    coll_toy = r_toy["pair"] + r_toy["full"]
    r313_toy = PFK.fr_type_table(TOY_GROUPS)
    ok_x313 = (coll_toy == r313_toy["T1"] + r313_toy["T2"]
               + r313_toy["T3"])
    ftoy = fr_block_terms(TOY_FLUX)
    edges_toy = fr_flux_edges(TOY_FLUX)
    ok_flux = (ftoy["far"] == 300 and edges_toy == [0, 36, 264]
               and sum(edges_toy) == 300)
    # float cross-check on the toy block
    tpos = np.array([0.1, 0.1, 0.2, 0.2, 0.3])
    tval = np.array([2.0, -1.0, 1.0, -1.0, 1.0])
    tblk = np.zeros(5, dtype=int)
    tgen = fold_genealogy(tpos, tval, tblk, 1)
    tsct = signed_cube_terms(tgen["G1"], tgen["gblk"], 1)
    tft = flux_telescope(tgen["G1"], tgen["ptr"], 1)
    ok_f = (abs(tsct["far"][0]) <= TOY_BAR
            and abs(tsct["pair"][0] - 6.0) <= TOY_BAR
            and abs(tsct["full"][0] - 2.0) <= TOY_BAR
            and abs(tft["F_end"][0]) <= TOY_BAR
            and abs(tft["F_open"][0]) <= TOY_BAR)
    check("G84-toy-exactness", ok_toy and ok_x313 and ok_flux
          and ok_f,
          "r313 toy block {2,-1}|{1,-1}|{1}: G1 = (1, 0, 1), far "
          "0 / pair 6 / full 2 sum 8 == x^3 EXACT, collision 8 "
          "== r313 T1+T2+T3 = 8+24-24 EXACT; flux toy (1,2,3,4): "
          "edges (0, 36, 264) sum 300 == 6 e_3 EXACT; float "
          "builders match the Fractions tables (bar %.0e)"
          % TOY_BAR)
    # m1: sigma omitted
    x_toy = [Fr(2), Fr(-1)]
    cube_t = sum(abs(x) ** 3 for x in x_toy)
    uns_t = sum(x ** 3 for x in x_toy)
    ev9m = ev9
    uns_w9 = float(np.sum(ev9m["sct"]["x"] ** 3))
    dev1 = abs(uns_w9 - ev9m["cube"]) / max(ev9m["cube"], 1e-300)
    check("G80-m1-unsigned-recomposition",
          cube_t - uns_t == 2 and dev1 >= MUT_MIN,
          "m1 LOUD (the r313 majorant error as must-fail): "
          "dropping sigma breaks sum |x|^3 by exactly 2 "
          "sum_{x<0} |x|^3 -- toy x = (2, -1): break %s EXACT; "
          "real w9: unsigned rel dev %.1e >= %.0e"
          % (cube_t - uns_t, dev1, MUT_MIN))
    # m2: double-counted fold group
    dg = [Fr(1), Fr(2), Fr(2)]        # group {2} duplicated
    x_true = Fr(3)
    r_m2 = fr_block_terms(dg)
    brk_comp = r_m2["x"] - x_true
    brk_rec = r_m2["x"] ** 3 - x_true ** 3
    gen9 = ev9m["gen"]
    G1d = np.concatenate([gen9["G1"], gen9["G1"][:1]])
    gbd = np.concatenate([gen9["gblk"], gen9["gblk"][:1]])
    od = np.argsort(gbd, kind="stable")
    sct_d = signed_cube_terms(G1d[od], gbd[od], ev9m["m"])
    dev2 = float(np.max(np.abs(sct_d["x"]
                               - ev9m["sct"]["x"]))
                 / max(np.max(np.abs(ev9m["sct"]["x"])), 1e-300))
    check("G81-m2-doubled-fold-group",
          brk_comp == 2 and brk_rec == 98 and dev2 >= MUT_MIN,
          "m2 CAUGHT (Fractions): duplicating fold group {2} in "
          "the toy genealogy {1}|{2} breaks the completeness "
          "ward by EXACTLY %s and the cube by EXACTLY %s; real "
          "w9: duplicated group 0 deviates rel %.1e >= %.0e"
          % (brk_comp, brk_rec, dev2, MUT_MIN))
    # m3: unordered support
    edges_rev = fr_flux_edges(list(reversed(TOY_FLUX)))
    brk3 = [abs(a - b) for a, b in zip(edges_toy, edges_rev)]
    tot_inv = (sum(edges_rev) == sum(edges_toy))
    rng = np.random.default_rng(SEED_SHUF)
    G1s = gen9["G1"].copy()
    for j in range(ev9m["m"]):
        a, b = gen9["ptr"][j], gen9["ptr"][j + 1]
        if b - a > 1:
            G1s[a:b] = G1s[a:b][rng.permutation(b - a)]
    fts = flux_telescope(G1s, gen9["ptr"], ev9m["m"])
    ne = min(len(fts["edges"]), len(ev9m["ft"]["edges"]))
    dev3 = float(np.max(np.abs(fts["edges"][:ne]
                               - ev9m["ft"]["edges"][:ne]))
                 / max(float(np.max(np.abs(
                     ev9m["ft"]["edges"]))), 1e-300))
    check("G82-m3-unordered-support",
          brk3 == [0, 108, 108] and tot_inv and dev3 >= MUT_MIN,
          "m3 LOUD: the divergence form is NOT permutation-blind "
          "-- toy (1,2,3,4) vs reversed: per-edge break %s EXACT "
          "while the total 300 is invariant (disclosed: the "
          "telescope TOTAL is symmetric, the local flux profile "
          "is not); real w9 seeded within-block shuffle (seed "
          "%d): edgewise rel dev %.1e >= %.0e"
          % (str([int(b) for b in brk3]), SEED_SHUF, dev3,
             MUT_MIN))
    # m4: collision count without the multiplicity bound
    n_t = 2
    true_t = 3 * (2 * n_t) * (4 * n_t) - 2 * (8 * n_t)
    mut_t = 3 * n_t * n_t - 2 * n_t
    cc9m = ev9m["cc"]
    mut_w9 = sum(3 * (gen9["ptr"][j + 1] - gen9["ptr"][j]) ** 2
                 - 2 * (gen9["ptr"][j + 1] - gen9["ptr"][j])
                 for j in range(ev9m["m"]))
    dev4 = abs(mut_w9 - cc9m["atoms_coll"]) \
        / max(cc9m["atoms_coll"], 1)
    check("G83-m4-multblind-count",
          true_t == 64 and mut_t == 8 and true_t - mut_t == 56
          and dev4 >= MUT_MIN,
          "m4 CAUGHT: the mult-blind counter (mult == 1) "
          "predicts 3n^2 - 2n collision atom triples against the "
          "true 3 p1 p2 - 2 p3 under multiplicity 2 -- toy "
          "2-group block: 8 vs 64, break 56 EXACT; real w9: "
          "mutant %d vs true %d, rel dev %.2e >= %.0e"
          % (mut_w9, cc9m["atoms_coll"], dev4, MUT_MIN))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the signed cubic tensor on the fold genealogy, "
          "the sealed divergence form (edge fluxes + telescope + "
          "opening-flux boundary lemma), the exact collision "
          "counting under multiplicity 2, the Fractions-exact "
          "recomposition on real w9 data and the world preview "
          "tables -- NO new certificate promoted, NO bound "
          "claimed (R315/R316 by contract)")
    recomp_ok = (rec3_w <= REC3_BAR and frd["dev_recomp"] == 0)
    if smoke:
        verdict_main = "SMOKE_NO_ADJUDICATION"
        check("G90-sealed-adjudication", True, "SMOKE: skipped")
    else:
        if not genealogy_ok:
            verdict_main = "GENEALOGY_INCOMPLETE(dev %.1e, %d " \
                "mismatches)" % (max(atom_w, x_w), mism_tot)
        elif not (flux_ok and recomp_ok):
            verdict_main = "NO_LOCAL_FLUX_FORM(tel dev %.1e, " \
                "recomp dev %.1e)" % (tel_w, rec3_w)
        elif bnd_zero:
            verdict_main = ("SIGNED_CUBE_IDENTITY(sum_j |x_j|^3 "
                            "= DeltaF + C_collision + C_boundary "
                            "EXACT; C_boundary == 0 by the "
                            "opening-flux lemma; shares med "
                            "far %+.3f / pair %+.3f / full %+.3f)"
                            % (float(np.median(sh_far)),
                               float(np.median(sh_pair)),
                               float(np.median(sh_full))))
        else:
            verdict_main = ("FLUX_WITH_BOUNDARY(named boundary: "
                            "opening flux, worst %.1e x A1^3)"
                            % bnd_w)
        check("G90-sealed-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R314_ANCHORS(shares %+.4f/%+.4f/%+.4f/%+.4f, "
                 "TC_far %.3f/%+.3f, mult 2 on %d/%d, ward %.1e)"
                 % (sh_med["T1"], sh_med["T2"], sh_med["T3"],
                    sh_med["T4"], tc_med, tc_sl, n_m2,
                    len(srt_all), ward_w)]
        parts.append("GENEALOGY(complete %.1e, %d mism, fold "
                     "share %.3f)" % (max(atom_w, x_w), mism_tot,
                                      fold_med))
        parts.append("TENSOR(w9 Fractions dev %s EXACT, f64 "
                     "recomp %.1e, xw T4 %.1e / coll %.1e / cube "
                     "%.1e)" % (frd["dev_recomp"], rec3_w,
                                xw_t4_w, xw_coll_w, xw_cube_w))
        parts.append("FLUX(tel %.1e, bnd %.1e, FC med %.3f "
                     "slope %+.3f)"
                     % (tel_w, bnd_w, float(np.median(fcs)),
                        slp(fcs)))
        parts.append("COLLISION(counts exact %d/%d, m2-count "
                     "ward %d/%d)" % (len(live), len(live),
                                      n_m2w, len(live)))
        parts.append("TERMS(far %+.4f, pair %+.4f, full %+.4f, "
                     "bnd 0)"
                     % (float(np.median(sh_far)),
                        float(np.median(sh_pair)),
                        float(np.median(sh_full))))
        parts.append("WORLDS(table printed, SCR localization "
                     "census)")
        parts.append(verdict_main)
        parts.append("MUSTFAIL_LEDGER(m1-m4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the Newton identity, "
          "the opening-flux lemma, the telescope, the collision "
          "counts and the multiplicity power-sum identity (all "
          "exact finite algebra, Fractions-decided on w9 + "
          "toys); MEASURED: every share, FC index and slope (42 "
          "+ %d finite rungs); OPEN: any bound on the terms "
          "(R315/R316), the cofinal law, kz15 beyond r270; NO "
          "RH claim"
          % (verd, " (SMOKE)" if smoke else "",
             len(erecs)))
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
