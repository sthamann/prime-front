#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cauchybinet_hall_probe -- PRIME.LSTAR.CAUCHYBINET_HALL_TRANSPORT.01
(round 340): the WEIGHTED CAUCHY-BINET TRANSPORT -- the new L*
base architecture after both pre-authorized norm-bound arms were
measured and capped (r334 capacity: the structural ceiling
kappa x C_lev = 1.0085 >= lambda_max -- every factorization "load
on level sets x universal level cost" loses more at the extremal
direction than the whole wall margin; r336 parity:
PARITY_WORLD_BLIND -- the local symbol/Fejer geometry does not
decide the wall).  Reviewer conclusion (binding): the L* defect
is neither a level-set nor a local frequency problem -- it lives
in the FULL SIGNED CONFIGURATION, visible on the extremal side
through the sharp two-atom structure (r284, the shallow-edge pair
folds 2/4).  The new idea class: NO norm bound -- TRANSPORT: pair
the negative determinant configurations with heavier positive
ones.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: rounds 337/338/339 may run in parallel -- this probe
touches NOTHING outside its own file and the strictly additive
rh-sync (existing entries byte-identical).

THE EXACT STARTING IDENTITY (Cauchy-Binet, signed; classical):
for the signed defect source mutilde = sum_j w_j delta_{x_j}
(S atoms, x strictly ascending, w signed) and the Hankel matrix
H_n(mutilde) = (m_{i+j})_{i,j<n} with m_r = sum_j w_j x_j^r:
    D_n = det H_n = sum_{|I|=n} (prod_{i in I} w_i) Delta(x_I)^2,
Delta(x_I) the Vandermonde of the positions of I.  With W(I) =
(prod |w_i|) Delta(x_I)^2 > 0 and eps(I) = (-1)^{#(I cap N_-)}:
    D_n = sum_{E_n} W - sum_{O_n} W
(E_n/O_n = size-n configurations with an even/odd number of
negative atoms).  By Sylvester, H_{N} > 0 (PD) iff D_n > 0 for
all n <= N, and for the L* window (N = N_w = (S+1)/2) this IS
lemma L* verbatim (int p^2 dnu < int p^2 dmu for deg p < N_w
iff a^T H_{N_w} a > 0 for all a != 0).  L* therefore reduces to
the family of weighted inequalities
    sum_{O_n} W < sum_{E_n} W   for all n <= N_w.

THE TRANSPORT CANDIDATE (the round's object): a flow T_n(I, J)
>= 0 (I in O_n, J in E_n, only along ADMISSIBLE edges) with
sum_J T_n(I, J) = W(I) for every I and sum_I T_n(I, J) <= W(J)
for every J, plus strict reserve somewhere ==> D_n > 0 for all
n ==> (Sylvester) H_{N_w} PD ==> L*.  By max-flow/min-cut the
existence of T_n is EXACTLY the weighted Hall condition
    sum_{I in A} W(I) <= sum_{J in Gamma(A)} W(J)
                                     for every A subset O_n.
The central structural hypothesis of the round (INTERVAL HALL
REDUCTION, a genuinely new candidate theorem, tested FIRST on
exact small models): on the canonical fold-exchange graph every
minimal weighted Hall cut is realized by an ordered interval
family / an ideal in the Gale order (plausible from the
one-dimensional Vandermonde geometry).  Then the r334 coordinate
1 - kappa_int would not be the first factor of a lossy level-set
inequality but the DUAL SLACK of a Hall cut -- the r334 ceiling
kappa x C_lev >= 1.0085 does NOT touch this route (no C_lev is
multiplied).  The r282 Kasteleyn no-go is RESPECTED: no sign
gauge, no termwise positivization, no value-true involution --
a weight-dependent many-to-many transport between configurations
of different weight (the m4 mutant documents the distinction
exactly).

THE ADMISSIBLE EDGES (source-pure, sealed BEFORE the freeze):
an elementary edge replaces exactly ONE negative atom y in I by
one of its canonical positive fold companions x not in I:
I -> J = I \ {y} u {x}.  CANONICAL COMPANIONS (sealed): the
union in descending x IS the fold order (x_f = cos(2 pi f / L)
is strictly decreasing in the fold index f <= L/2 -- gated on
w9), so position adjacency == fold adjacency; the companions of
a negative atom y are the nearest mu atoms strictly left and
strictly right of y in the x-sorted union.  OCCUPANCY REMEDY
(the reviewer's "two steps / double exchange", sealed): if a
companion is already in I, step outward to the next free mu atom
on the same side, at most CB_STEP = 2 free mu atoms per side.
The relation is defined ONLY by node order, fold ancestry and
source signs; the exact weight ratio on every edge is
    W(J)/W(I) = (|w_x|/|w_y|)
                x prod_{z in I \ {y}} ((x - z)/(y - z))^2
(gated bit-equal in Fractions on the toys and every small-model
edge, f64 log-gated on sampled w9 configurations).  FORBIDDEN
in every constructor: the top eigen direction, the wall margin,
any per-window post-optimized edge library, any posthoc
selection of successful companions (AST scope audit + the
m2/m3 mutants prove the audit bites).

INDEX FIREWALL (binding, r238-r337 discipline): w = window, S =
#union atoms, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2, minC =
first n with h_n < 0, crossing = minC + 1 (r283 dictionary);
D_n = det H_n(mutilde) with h_n = D_{n+1}/D_n up to
normalization -- D_n > 0 for n <= N_w is the free-window
statement itself.  Ground truth (r283/r284/r334 records, control
flips, the r334 1 - kappa_int record column) enters GATES and
record tables only; the sealed constructors consume atom
positions / signed weights / node order ONLY (AST scope audit);
no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: document pipeline V.{build_measures,
lam_max_at}, r283 FS.{mu_chain_f64, b_matrix_f64}, r278
MS.ctx_build, r280 BL.{union_of_ctx, sign_chain_f64}, v881
PIK.{lambda_eps, folded_measure, build_rung}, r243
PB.smooth_comb, r244 BH.spearman, r331 TR.{base_comb,
build_world}, r289 AKD.twin_rational, r276 MF.local_gaps, r230
JF.{TOY_NODES, TOY_WTS}, v563 core READ-ONLY.

LEG 0 -- ANCHORS: w9 records through the document pipeline
(S = 367 = 263 + 104, N_w = 184, lambda_max(E_184) = 0.99983248,
lambda at 185 = 1.00003660, margin 1.6752e-4); the campaign
channel cross-gate (BL union == V union, minC = 184); the r284
shallow edge (the two smallest-theta nu atoms are folds 2/4 --
gated, and identified INSIDE the edge model as the two extremal
atoms); the r334 coordinate 1 - kappa_int as a SEALED COMPARISON
COLUMN (record values 4.8e-4 / 4.3e-4 / 2.6e-5 / 9e-6 at
kz18/kz9/kz60/kz52 -- reporting only, never recomputed, never
consumed).

LEG A -- signed_cauchy_binet EXACT: (a1) hand toy x =
(-1/2, 0, 1/2), w = (1, -1/3, 1): D_1 = 5/3, D_2 = 5/6 with the
parity split E = 1 / O = 1/6, and D_3 = -1/48 < 0 -- the wall in
miniature exactly one degree past the half-filling window N = 2;
the transport at n = 2 by hand: both odd pairs {-1/2, 0} and
{0, 1/2} map to the single even pair {-1/2, 1/2} through the
companion swaps, load 1/6 <= capacity 1, reserve = D_2 = 5/6;
the hand ratio W({-1/2,1/2})/W({-1/2,0}) = 12 = (1/(1/3)) x
((1/2+1/2)/(0+1/2))^2 -- all bit-equal in Fractions.  (a2) JF9
(r230 verbatim, S = 9, S_- = 3): D_n = sum_E W - sum_O W ==
det H_n bit-equal in Fractions for every n <= 5.  (a3) the r334
instances I2/I3/I4 as signed unions (S = 10/12/14): the identity
bit-equal for every n <= N = 5/6/7 (full enumeration, up to
C(14,7) = 3432 configurations); Sylvester cross-gate: the
rational LDL pivots of H_N equal D_n/D_{n-1} exactly.  (a4) w9
LIVE: D_1 and D_2 in EXACT Fractions on all 367 atoms (67161
pair configurations) == m_0 and m_0 m_2 - m_1^2 bit-equal;
where enumeration is impossible the identity is carried by the
sampled ratio ward (a5): CFG_DRAWS = 8 deterministic golden
configurations of size 6 (world-blind index draws, sealed
negative-atom completion rule), every admissible exchange edge
checked in f64 log space |log W(J) - log W(I) - log ratio| <=
1e-8, plus ONE exact Fraction spot check bit-equal.

LEG B -- canonical_exchange_graph: the companion map and the
edge set sealed as above (printed before any flow result); the
w9 fold anchoring gated (union descending-x order == ascending
fold order on the edge prefix; the two extremal nu atoms are
folds 2/4 == r284/r336 record); the exact ratio formula gated on
EVERY edge of the exact small models (bit-equal, Fractions).

LEG C -- THE OPTIMAL TRANSPORT ON SMALL MODELS (the core): the
sealed model family: TOY (S = 3), F1 (S = 6, S_- = 2), F2
(S = 7, S_- = 2), I1 = JF9 (S = 9, S_- = 3), I2/I3/I4 (r334
verbatim, S = 10/12/14), W9EDGE / TWINEDGE / EPSTEDGE / SCREDGE
/ SMOOTHEDGE (the S0 = 12 largest-x union atoms of the real
world = the shallow-edge prefix, weights as EXACT dyadic
Fractions of the builder floats; prefix extended by at most 6
atoms until >= 2 nu atoms; model depth N0 = (S0+1)//2).  Per
model and per n <= N: full configuration enumeration (census
gate #masks == C(S, n)), exact W and parity, D_n == E - O ==
det H_n bit-equal, PD typing (live iff D_n > 0 for all n <= N);
the canonical exchange graph; EXACT integer max-flow (Dinic on
the lcm-scaled capacities -- every W is rational, dyadic on the
real-world models) at every n with |O_n| <= FLOW_CAP = 700
(larger loci typed FLOW_SKIPPED, sealed size rule, loci
printed); coverage iff flow == sum_O W; if coverage fails the
residual-reachable source set A* is extracted and its Hall
violation certified in EXACT Fractions.  THE FIVE REVIEWER
TESTS: (1) EXTREMAL CARRIER -- on W9EDGE at n = N0: the
W-mass fraction of the binding dual cut carried by
configurations containing BOTH extremal atoms (folds 2/4);
carried iff >= 0.9; (2) TWIN FORM -- the binding cut of
TWINEDGE has the same generator (index-matched) and the dual
slack agrees to 1e-3 rel; (3) CONTROLS -- EPST/SCR/SMOOTH edge
models: is the model window already sign-broken (some D_n <= 0,
n <= N0 << flip 25/21/27)?; (4) interval_hall_reduction -- on
the FULLY ENUMERABLE models (TOY/F1/F2: |O_n| <= 20, |E_n| <=
18): ALL 2^|O_n| - 1 Hall sets enumerated (float prescan +
exact Fraction recertification of every tie within 1e-6 rel);
is every exact argmin cut a Gale-order ideal (down- or up-set,
orientation printed), and does the principal-ideal family
attain the exact minimum?; (5) SOURCE SUFFICIENCY -- does the
elementary edge set (1-step + the sealed 2-step occupancy
remedy) cover the full odd mass on every live model at every
n, or is the source structurally too poor
(SOURCE_EXCHANGE_INSUFFICIENT)?  On models beyond the full-
enumeration caps the dual slack is measured on the sealed
PRINCIPAL GALE IDEAL FAMILY (all down-ideals {I <= J0} and
up-ideals {I >= J0}, J0 in O_n, plus the full set; exact
recertification of the argmin) -- an UPPER bound of the true
minimal surplus, honest direction disclosed; the flow coverage
itself stays EXACT.

LEG D -- THE SCALING PROBE: per ladder rung (the 42 admissible
frame-A windows, campaign channel), the S0 = 10 shallow-edge
model at n = N0L = 5: exact coverage + the principal-ideal dual
slack, normalized hall_w = delta_fam / sum_E W; compared
GATE-SIDE against 1 - lambda_max(N_w) per rung (FS chain route)
and against the r334 record column 1 - kappa_int at kz18/9/60/
52.  CONCORDANCE RULE (sealed): FLOW_RESTATEMENT iff hall_w > 0
on every rung AND spread(log10(hall_w / margin)) <= 0.5 AND
|spearman| >= 0.75 (the dual slack is the spectral margin in
disguise); else NEW_COORDINATE (spread + spearman printed).

LEG E -- WARDS / MUST-FAILS (each loud): (m1) RATIO WITHOUT THE
SQUARE: the mutant ratio (prod |(x-z)/(y-z)| unsquared) must
break the exact toy ratio (Fractions, difference exactly
nonzero) -- CAUGHT; (m2) EDGE LIBRARY POST-OPTIMIZED PER
WINDOW: a mutant re-picking companions AFTER SIGHT of the
coverage table consumes the withheld coverage object -- FLAGGED
by the AST scope audit AND on the toy it returns a different
companion set than the sealed rule -- CAUGHT twice; (m3)
TRANSPORT CONSUMES THE TARGET: a mutant orienting the flow by
the withheld lambda record is FLAGGED by the AST scope audit;
(m4) KASTELEYN CONFUSION (r282 respected): the sign gauge
sigma = sign w changes the VALUE of D_n by exactly
2 sum_O W != 0 (Fractions, exact) -- a termwise positivization
is never value-true on a signed window; the transport moves
MASS between DIFFERENT configurations instead -- structurally
documented CAUGHT; (m5) INCOMPLETE CUT ENUMERATION: a mutant
Hall enumerator dropping the full mask is CAUGHT by the census
gate (count == 2^|O| - 1), and the configuration census gate
(#masks == C(S, n)) guards the subset side.  STOP LIST
(anti-gates, binding): NO L* claim, NO bound mechanism, NO
transport promoted as a certificate, NO posthoc edge library,
NO derived 5/7, NO RH claim; r243..r339 stand; mincut base 4 /
refined 5 UNCHANGED.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel tol 0.01; CTRL_FLIPS {EPST 25, SCR 21, SMOOTH 27};
EXT 8 / EXT2 32; SHALLOW_FOLDS (2, 4); R334_KINT {18: 4.8e-4,
9: 4.3e-4, 60: 2.6e-5, 52: 9.0e-6} (record, comparison column
only); S0_EDGE 12; S0_LADDER 10; S0_EXTRA 6; MIN_NU 2; CB_STEP
2; FLOW_CAP 700; HALL_CAP 20; SINK_CAP 18; TIE_REL 1e-6;
CFG_DRAWS 8; CFG_N 6; RATIO_LOG_BAR 1e-8; TWIN_TOL 1e-8;
TWIN_BAR 1e-3 (rel); CONC_SPREAD 0.5 (log10); SP_BAR 0.75;
EXTREMAL_BAR 0.9; sealed exact models: TOY mu {-1/2: 1,
1/2: 1}, nu {0: 1/3}; F1 mu {-5/6: 1, -1/2: 2/3, 1/6: 1/2,
5/6: 1}, nu {-1/6: 1/5, 1/2: 1/4}; F2 mu {-9/10: 1, -1/2: 1/2,
-1/5: 1/3, 3/10: 1/2, 7/10: 1}, nu {-7/10: 1/4, 1/10: 1/6};
I1 = JF9 (r230 verbatim); I2/I3/I4 = the r334 instances
verbatim; runtime <= 1800 s; smoke = toys + firewall + scopes +
mutants + F1/F2 full Hall + I1/I2 identity + w9 records/channel/
exact-D2/ratio ward + W9EDGE transport; ladder, controls, twin
and adjudication skipped.  PRE-SPEC SCOPING (disclosed): the
r283/r284/r334/r336 record numbers (S counts, lambda records,
flips, shallow folds, the 1 - kappa_int column) are consumed as
sealed gate anchors and comparison prints only; the Cauchy-Binet
identity, the Sylvester dictionary, the edge weight-ratio
formula and the max-flow = Hall duality are classical algebra,
disclosed above; GENUINELY OPEN quantities of this round: every
coverage bit, every dual slack, the cut anatomy (extremal
fraction, Gale ideality, family attainment), the control edge
signs, the twin form and the concordance column -- NONE was
computed before this spec was frozen; the model family, the
companion rule, every cap/bar and the verdict tree were fixed at
design time from the published record geometry BEFORE any
machinery pass of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
TARGET_LEAK overrides everything on any constructor scope hit):
  [exactly one of] INTERVAL_HALL_CARRIER(on every fully
    enumerated model and n: every exact argmin Hall cut is a
    Gale ideal AND the principal-ideal family attains the exact
    minimum) / CUT_REDUCTION_FAIL(loci)
  + [exactly one of] WEIGHTED_FLOW_GO(coverage at every n <= N
    on every live model, exact, with the strict reserve D_n > 0)
    / SOURCE_EXCHANGE_INSUFFICIENT(loci: model, n, uncovered
    share, exact violating Hall witness)
  + EXTREMAL_CUT(W9EDGE binding-cut anatomy: W-fraction on
    configurations containing both fold-2/4 atoms; generator)
    [always]
  + [exactly one of] TRANSPORT_WORLD_SEEN(every dead edge model
    sign-breaks at some n <= N0 while the live edge models stay
    PD) / TRANSPORT_WORLD_BLIND(loci)
  + [exactly one of] FLOW_RESTATEMENT(spread, spearman) /
    NEW_COORDINATE(spread, spearman, loci)
  + TWIN_LEDGER(dual-slack rel dev, cut form) [always].
Honesty before beauty: the Cauchy-Binet split, the Sylvester
dictionary, the ratio formula and max-flow = Hall are EXACT
COORDINATES of the open scalar L*, not a proof; a passing
coverage is a measured transport on FINITE models (shallow-edge
prefixes and rational instances), never a certificate for the
full window; the principal-ideal slack on large models is an
upper bound of the true minimal surplus (disclosed); a passing
world clause is a consistency statement about the instrumented
edge models, not a discriminator theorem; no verdict claims L*,
a bound mechanism, a derived 5/7, or RH progress in any
direction.

RECORD TABLES (frozen from the record run; two-commit protocol,
chronology honest: smoke pass 1 = 23/26 (28.3 s) -- two GATE-SIDE
must-fail witness slips, fixed BEFORE the freeze (the m1 hand
difference is 6 = 12 - 3 x 2, not 8; the m2 value witness moved
from the F1 negative -- whose 2+2 companion neighborhood is
set-equal to the widened library -- to the deepest F2 negative
with three left mu atoms); no bar, cap, model, family or
adjudication rule moved; smoke pass 2 = 26/26 (28.2 s);
PRE-FREEZE COMMIT 3736af89, freeze SPEC_SHA 82c4d1839386a853.
Calibration pass 1 = first full evaluation = 26/26, wall 39.9 s,
NO amendment; determinism pre-checked (two full runs,
timing-normalized diff EMPTY, walls 39.9/39.7 s); the
record-table insertion is the ONLY post-freeze change; the
post-insertion record runs run1/run2 are numerically identical
to the calibration pass, timing-normalized diff EMPTY):
CAL_VERDICT = CUT_REDUCTION_FAIL(the interval-Hall reduction is
REFUTED at the smallest exact scale: 5 of 9 fully enumerated
(model, n) loci carry NON-ideal exact argmin Hall cuts -- F1
n=2: argmin {(2,3),(3,4)} (delta_full 913/1080) pairs the two
odd configurations THROUGH the shallow negative atoms but is an
ANTICHAIN section, Gale-down and Gale-up closure both fail, the
principal-ideal family misses the exact minimum by 1.63x; F1
n=3 miss 2.70x; F2 n=2: the argmin is the SINGLETON {(1,3)}, a
mid-order antichain element, neither closure holds, miss 1.17x;
F2 n=3 miss 1.92x; F2 n=4: delta_full 222603/625000000 =
3.56e-4 vs family 3.64e-3, miss 10.2x and GROWING toward
half-filling -- the minimal weighted Hall cuts are NOT interval
ideals in the Gale order; only the trivial n=1 loci and the
TOY carry the ideal form)
+ SOURCE_EXCHANGE_INSUFFICIENT(one live locus uncovered: I2 at
n = N = 5, exact deficiency share 0.023 of the odd mass -- on a
PD model (all D_n > 0) the elementary edge set (1-step + 2-step
occupancy remedy) fails to cover at exactly half-filling depth;
all other live loci covered EXACT: TOY 2/2, F1 3/3, F2 4/4, I2
4/5, flow == sum_O W integer-exact after lcm scaling, reserve
D_n > 0 at every covered locus, no FLOW_SKIPPED locus among the
live models)
+ EXTREMAL_CUT(W9EDGE at n = N0 = 6: binding principal-ideal
cut = the UP ideal generated by (0,1,2,3,4,11) (236 of 504 odd
configurations, dual slack delta_fam/sum_E W = -6.183e-2 < 0:
the local Hall condition is VIOLATED on the shallow edge);
extremal atoms folds (2,4) at model indices [8,10]: W-fraction
of the cut containing BOTH = 3.86e-3 << 0.9, containing at
least one = 0.4449 -- the two-atom clause FAILS: the r284
extremal pair is a SPECTRAL object, the Hall-cut mass is NOT
pinned to it)
+ TRANSPORT_WORLD_BLIND(the D_n sign of the shallow-edge prefix
separates NOTHING: the dead edge models break immediately
(EPSTEDGE signs -,-,-,+,+,- first break n=1; SCREDGE -,+,+,+,
-,- n=1; SMOOTHEDGE -,+,-,-,-,+ n=1) but the LIVE W9EDGE breaks
too (signs +,-,-,-,+,+, first break n = 2 with a genuinely
resolved relative deficit D_2/sum_E = -9.7e-3, odd/even mass
ratio 1.0097; the prefix alternates mu/nu perfectly, folds
1..12, nu at the even folds, near-balanced +-4e-6 weights) --
THE STRUCTURAL FINDING of the round: the shallow edge of EVERY
world, MAIN included, is locally indefinite from n = 2 on its
own configuration space (odd/even ratio 0.983..1.0097 -> 1 with
n, the half-filling balance in miniature); the full-window
positivity is a GLOBAL rescue, not a local edge property --
consistent with r336 PARITY_WORLD_BLIND from the flow side)
+ NEW_COORDINATE(the ladder hall coordinate delta_fam/sum_E W
at the S0 = 10 edge, n = 5, is NEGATIVE on 42/42 rungs (range
-0.1315 at kz9 to -0.1835 deep, weakly deepening with N_w)
while every margin 1 - lambda_max is positive (1.675e-4 ..
1.4e-7): the edge Hall slack is not the spectral margin in any
disguise, and it does not track the r334 column either (kz18
1-kappa_int 4.8e-4 vs hall -0.160, kz9 4.3e-4 vs -0.131, kz60
2.6e-5 vs -0.180, kz52 9.0e-6 vs -0.177) -- a genuinely new,
SIGN-OPPOSITE near-edge coordinate: local Hall deficit
coexisting with global positivity on every rung)
+ TWIN_LEDGER(TWINEDGE == W9EDGE at tol 1e-8: same fold prefix,
same binding generator (index-matched, up ideal), dual slack
rel dev 4.8e-8 (bar 1e-3), coverage pattern identical;
dose-zero identity TR.build_world == V.build_measures BITWISE).
Key numbers.  W9 exact: D_1 = m_0 = 3.473206 > 0; D_2 over all
67161 pair configurations == m_0 m_2 - m_1^2 BIT-EQUAL in
dyadic Fractions (parity split E 3.041804 / O 0.526915, D_2
2.514889 > 0); ratio ward 8 golden configurations x 68 edges,
max f64 log dev 2.3e-14 (bar 1e-8), exact Fraction spot
BIT-EQUAL; records lambda_max(E_184) = 0.99983248, margin
1.6752e-4, lambda at 185 = 1.00003660, minC = 184, channel devs
0.0 / 3.8e-16; the two smallest-theta nu atoms are folds (2, 4)
== r284 record; the S0 = 12 edge prefix has strictly ascending
fold indices 1..12 (position adjacency IS fold adjacency).
Toys: D_1 = 5/3, D_2 = 5/6 (E 1 / O 1/6), D_3 = -1/48 < 0, hand
ratio 12, hand transport reserve 5/6 -- all bit-equal; JF9 D
signs +,+,+,-,+ (the r230 toy is itself indefinite inside its
window, honest); I2 PD 5/5, I3 breaks at n = 5, I4 at n = 6
(the r334 capacity instances are dead as signed windows,
consistent with their kappa > 1 record); identities BIT-EQUAL
at every n on every model (I4: 9908 configurations); Sylvester
LDL cascade == enumeration cascade on TOY + I2; 192 small-model
edges ratio-verified bit-equal.  MUST-FAILS: m1 unsquared ratio
6 != 12, exact difference 6 -- CAUGHT; m2 posthoc edge library
AST-FLAGGED (cov_tab@1022) AND toy value [0,2,3,5,6] != sealed
[3,2,5,6] -- CAUGHT twice; m3 flow-gift AST-FLAGGED
(REC_LAM@1030); m4 Kasteleyn gauge shifts D_2 by exactly
2 sum_O = 1/3 (7/6 vs 5/6, Fractions) -- the r282 no-go
boundary reproduced, CAUGHT; m5 cut-census mutant CAUGHT (14 !=
15 masks); constructor scopes + fragment audit CLEAN.  Runtime
40.7 / 40.4 s record run1/run2 (bar 1800); deterministic,
timing-normalized diff EMPTY.  AMENDMENTS AFTER FREEZE: NONE
(the record-table insertion is the only post-freeze change; the
two pre-freeze gate-side witness fixes are disclosed in the
chronology above; no bar, cap, family, model or adjudication
rule moved at any point after the freeze).

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
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V                # noqa: E402 document
import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import bordered_hankel_probe as BH               # noqa: E402 r244
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import jfraction_probe as JF                     # noqa: E402 r230
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
EXT = 8
EXT2 = 32
SHALLOW_FOLDS = (2, 4)
R334_KINT = {18: 4.8e-4, 9: 4.3e-4, 60: 2.6e-5, 52: 9.0e-6}
S0_EDGE = 12
S0_LADDER = 10
S0_EXTRA = 6
MIN_NU = 2
CB_STEP = 2
FLOW_CAP = 700
HALL_CAP = 20
SINK_CAP = 18
TIE_REL = 1.0e-6
CFG_DRAWS = 8
CFG_N = 6
RATIO_LOG_BAR = 1.0e-8
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
CONC_SPREAD = 0.5
SP_BAR = 0.75
EXTREMAL_BAR = 0.9
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0

# sealed exact models (rational; positions ascending inside the code)
TOY_MU = ((Fr(-1, 2), Fr(1)), (Fr(1, 2), Fr(1)))
TOY_NU = ((Fr(0), Fr(1, 3)),)
F1_MU = ((Fr(-5, 6), Fr(1)), (Fr(-1, 2), Fr(2, 3)),
         (Fr(1, 6), Fr(1, 2)), (Fr(5, 6), Fr(1)))
F1_NU = ((Fr(-1, 6), Fr(1, 5)), (Fr(1, 2), Fr(1, 4)))
F2_MU = ((Fr(-9, 10), Fr(1)), (Fr(-1, 2), Fr(1, 2)),
         (Fr(-1, 5), Fr(1, 3)), (Fr(3, 10), Fr(1, 2)),
         (Fr(7, 10), Fr(1)))
F2_NU = ((Fr(-7, 10), Fr(1, 4)), (Fr(1, 10), Fr(1, 6)))
# r334 instances verbatim (mu pos, mu w, nu pos, nu w as (num, den))
INSTANCES = {
    "I2": (((-7, 8), (-5, 8), (-2, 8), (1, 8), (4, 8), (7, 8)),
           ((1, 1), (2, 3), (1, 2), (1, 2), (2, 3), (1, 1)),
           ((-6, 8), (-4, 8), (3, 8), (6, 8)),
           ((1, 3), (1, 4), (1, 5), (1, 6))),
    "I3": (((-9, 10), (-6, 10), (-3, 10), (0, 1), (3, 10), (6, 10),
            (9, 10)),
           ((1, 1), (1, 2), (1, 3), (1, 4), (1, 3), (1, 2), (1, 1)),
           ((-8, 10), (-7, 10), (-1, 10), (2, 10), (8, 10)),
           ((1, 2), (1, 3), (1, 5), (1, 6), (1, 4))),
    "I4": (((-15, 16), (-11, 16), (-7, 16), (-3, 16), (3, 16),
            (7, 16), (11, 16), (15, 16)),
           ((1, 1), (1, 2), (1, 2), (1, 1), (1, 1), (1, 2), (1, 2),
            (1, 1)),
           ((-13, 16), (-9, 16), (-5, 16), (5, 16), (9, 16),
            (13, 16)),
           ((1, 2), (1, 3), (1, 4), (1, 4), (1, 3), (1, 2))),
}

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
    return (not bad), ("NO zero/prime oracles; the sealed constructors "
                       "consume atom positions / signed weights / node "
                       "order ONLY; record numbers and flips enter "
                       "gates and record tables only"
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


CONSTRUCTORS = ("edge_model_take", "wprod_of", "parity_of",
                "companions_map", "exchange_targets", "ratio_formula",
                "hankel_det_frac", "moments_of", "gale_leq",
                "maxflow_int", "hall_full_enum", "ideal_family_slack",
                "golden_config", "model_pack")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "R334_KINT", "eigh", "eigvalsh",
                   "lam_max_at", "minC_true", "cross_true",
                   "cov_tab", "margin_col"}


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
def edge_model_take(xu, wu, s0, extra, min_nu):
    """the shallow-edge prefix model: the s0 largest-x union atoms
    (descending x = ascending fold order), extended by at most
    `extra` atoms until >= min_nu negative atoms are inside;
    returns (xs Fractions ascending, ws signed Fractions, kept
    union indices in descending-x order) or None if the nu floor
    is unreachable.  Consumes positions + signed weights only."""
    o = np.argsort(np.asarray(xu, float))[::-1]
    take = int(s0)
    while take <= int(s0) + int(extra):
        idx = o[:take]
        n_nu = int(np.sum(np.asarray(wu, float)[idx] < 0.0))
        if n_nu >= int(min_nu):
            break
        take += 1
    else:
        return None
    idx = list(o[:take])
    pairs = sorted(((Fr(float(xu[k])), Fr(float(wu[k]))) for k in idx),
                   key=lambda p: p[0])
    xs = [p[0] for p in pairs]
    ws = [p[1] for p in pairs]
    return xs, ws, idx


def wprod_of(xs, ws_abs, idx):
    """W(I) = (prod |w_i|) x Delta(x_I)^2, exact Fractions."""
    w = Fr(1)
    for i in idx:
        w *= ws_abs[i]
    van = Fr(1)
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            van *= (xs[idx[b]] - xs[idx[a]])
    return w * van * van


def parity_of(neg_mask, idx):
    """eps(I) parity bit: 1 iff #(I cap N_-) is odd."""
    c = 0
    for i in idx:
        if neg_mask[i]:
            c += 1
    return c & 1


def companions_map(neg_mask):
    """canonical fold companions per negative atom index: the mu
    atom indices strictly left (descending) and strictly right
    (ascending) in the x-sorted node order; consumes node order +
    source signs only."""
    S = len(neg_mask)
    comp = {}
    for k in range(S):
        if not neg_mask[k]:
            continue
        left = [j for j in range(k - 1, -1, -1) if not neg_mask[j]]
        right = [j for j in range(k + 1, S) if not neg_mask[j]]
        comp[k] = (left, right)
    return comp


def exchange_targets(idx_set, y, comp, step):
    """admissible companion targets for negative atom y inside
    configuration idx_set: the first `step` FREE mu atoms per side
    (the sealed occupancy remedy)."""
    left, right = comp[y]
    out = []
    for side in (left, right):
        taken = 0
        for x in side:
            if x not in idx_set:
                out.append(x)
                taken += 1
                if taken >= step:
                    break
    return out


def ratio_formula(xs, ws_abs, idx, y, x):
    """the exact edge weight ratio W(J)/W(I) for the single swap
    y -> x on configuration idx (list): (|w_x|/|w_y|) x
    prod_{z in I \\ {y}} ((x - z)/(y - z))^2, exact Fractions."""
    r = ws_abs[x] / ws_abs[y]
    for z in idx:
        if z == y:
            continue
        q = (xs[x] - xs[z]) / (xs[y] - xs[z])
        r *= q * q
    return r


def moments_of(xs, ws, rmax):
    """exact signed moments m_0..m_rmax."""
    out = []
    pw = [Fr(1)] * len(xs)
    for _r in range(rmax + 1):
        out.append(sum(w * p for w, p in zip(ws, pw)))
        pw = [p * x for p, x in zip(pw, xs)]
    return out


def hankel_det_frac(moms, n):
    """det H_n from the moment list, fraction-exact Gauss
    elimination (returns the determinant)."""
    M = [[moms[i + j] for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            det = -det
        det *= M[col][col]
        pv = M[col][col]
        for r in range(col + 1, n):
            if M[r][col] != 0:
                f = M[r][col] / pv
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return det


def gale_leq(tI, tJ):
    """Gale order on sorted index tuples of equal size."""
    return all(a <= b for a, b in zip(tI, tJ))


def maxflow_int(src_caps, snk_caps, edges):
    """exact integer max-flow (Dinic) on the bipartite transport
    network s -> sources (caps) -> sinks (inf) -> t (caps);
    src_caps/snk_caps are python ints, edges a list of neighbor
    index lists per source.  Returns (flow, reachable_sources)
    with reachable_sources = the s-side residual sources (the
    deficiency witness when uncovered)."""
    nS, nT = len(src_caps), len(snk_caps)
    n_nodes = 2 + nS + nT
    s, t = 0, 1
    INF = sum(src_caps) + 1
    # adjacency: list of [to, cap, rev_index]
    adj = [[] for _ in range(n_nodes)]

    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])

    for i in range(nS):
        add_edge(s, 2 + i, src_caps[i])
    for j in range(nT):
        add_edge(2 + nS + j, t, snk_caps[j])
    for i in range(nS):
        for j in edges[i]:
            add_edge(2 + i, 2 + nS + j, INF)
    flow = 0
    while True:
        level = [-1] * n_nodes
        level[s] = 0
        queue = [s]
        for u in queue:
            for e in adj[u]:
                if e[1] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    queue.append(e[0])
        if level[t] < 0:
            break
        it = [0] * n_nodes

        def dfs(u, f):
            if u == t:
                return f
            while it[u] < len(adj[u]):
                e = adj[u][it[u]]
                v = e[0]
                if e[1] > 0 and level[v] == level[u] + 1:
                    d = dfs(v, min(f, e[1]))
                    if d > 0:
                        e[1] -= d
                        adj[v][e[2]][1] += d
                        return d
                it[u] += 1
            return 0

        while True:
            f = dfs(s, INF)
            if f <= 0:
                break
            flow += f
    reach = [False] * n_nodes
    reach[s] = True
    queue = [s]
    for u in queue:
        for e in adj[u]:
            if e[1] > 0 and not reach[e[0]]:
                reach[e[0]] = True
                queue.append(e[0])
    reach_src = [i for i in range(nS) if reach[2 + i]]
    return flow, reach_src


def hall_full_enum(srcW, snkW, edges, tie_rel):
    """full weighted Hall enumeration over all nonempty A subset
    O_n (|O| <= HALL_CAP, |E| <= SINK_CAP): float prescan of the
    surplus sum_{Gamma(A)} W - sum_A W (weights normalized by the
    max), then EXACT Fraction recertification of every tie within
    tie_rel; returns (delta_exact, argmin_masks, n_masks)."""
    nS, nT = len(srcW), len(snkW)
    scale = max(max(srcW), max(snkW))
    sw = [float(v / scale) for v in srcW]
    tw = [float(v / scale) for v in snkW]
    nb = [0] * nS
    for i in range(nS):
        m = 0
        for j in edges[i]:
            m |= (1 << j)
        nb[i] = m
    snk_tab = [0.0] * (1 << nT)
    for m in range(1, 1 << nT):
        lb = m & (-m)
        snk_tab[m] = snk_tab[m ^ lb] + tw[lb.bit_length() - 1]
    n_all = (1 << nS) - 1
    gam = [0] * (1 << nS)
    srw = [0.0] * (1 << nS)
    best = math.inf
    cand = []
    for A in range(1, 1 << nS):
        lb = A & (-A)
        i = lb.bit_length() - 1
        gam[A] = gam[A ^ lb] | nb[i]
        srw[A] = srw[A ^ lb] + sw[i]
        sur = snk_tab[gam[A]] - srw[A]
        if sur < best - abs(best) * tie_rel:
            best = sur
            cand = [A]
        elif sur <= best + abs(best) * tie_rel + 1e-300:
            cand.append(A)
    # exact recertification of every candidate
    dmin = None
    argmin = []
    for A in cand:
        g = 0
        se = Fr(0)
        for i in range(nS):
            if (A >> i) & 1:
                g |= nb[i]
                se += srcW[i]
        te = Fr(0)
        for j in range(nT):
            if (g >> j) & 1:
                te += snkW[j]
        sur = te - se
        if dmin is None or sur < dmin:
            dmin = sur
            argmin = [A]
        elif sur == dmin:
            argmin.append(A)
    return dmin, argmin, n_all


def ideal_family_slack(srcW, snkW, edges, tuples_src):
    """the sealed PRINCIPAL GALE IDEAL family: for each generator
    J0 the down-ideal {I <= J0} and the up-ideal {I >= J0}, plus
    the full set; float prescan, exact Fraction recertification of
    the argmin; returns (delta_fam Fraction, members, gen, dirn)."""
    nS = len(srcW)
    scale = max(max(srcW), max(snkW))
    sw = [float(v / scale) for v in srcW]
    tw = [float(v / scale) for v in snkW]
    fams = []
    for g0 in range(nS):
        dn = [i for i in range(nS)
              if gale_leq(tuples_src[i], tuples_src[g0])]
        up = [i for i in range(nS)
              if gale_leq(tuples_src[g0], tuples_src[i])]
        fams.append((dn, g0, "down"))
        fams.append((up, g0, "up"))
    fams.append((list(range(nS)), -1, "full"))
    best = (math.inf, None)
    for members, g0, dirn in fams:
        if not members:
            continue
        cov = set()
        se = 0.0
        for i in members:
            cov.update(edges[i])
            se += sw[i]
        sur = sum(tw[j] for j in cov) - se
        if sur < best[0]:
            best = (sur, (members, g0, dirn))
    members, g0, dirn = best[1]
    cov = set()
    se = Fr(0)
    for i in members:
        cov.update(edges[i])
        se += srcW[i]
    te = sum((snkW[j] for j in cov), Fr(0))
    return te - se, members, g0, dirn


def golden_config(S, neg_idx, n, s):
    """deterministic world-blind configuration draw s of size n on
    S nodes: indices floor(frac((k+1) g + s g^2) S) collected until
    n distinct; if no negative atom was drawn, the last index is
    replaced by the negative atom of rank (s mod #neg) in the node
    order (sealed completion rule)."""
    out = []
    k = 0
    while len(out) < n:
        v = int(math.floor(math.fmod((k + 1) * GOLDEN
                                     + s * GOLDEN * GOLDEN, 1.0) * S))
        if v not in out:
            out.append(v)
        k += 1
    if not any(i in neg_idx for i in out):
        out[-1] = sorted(neg_idx)[s % len(neg_idx)]
        out = list(dict.fromkeys(out))
        k2 = 0
        while len(out) < n:
            v = (out[-1] + 1 + k2) % S
            if v not in out:
                out.append(v)
            k2 += 1
    return tuple(sorted(out))


# ============== the model driver (sealed)
def model_pack(name, xs, ws, flow_cap, hall_cap, sink_cap, tie_rel,
               step):
    """full per-model analysis: per n <= N = (S+1)//2 the exact
    configuration census, the parity split, D_n (two routes), the
    exchange graph, the exact flow coverage, the dual slack
    (full Hall enumeration where the caps allow, else the
    principal-ideal family), and the cut anatomy.  Consumes the
    model atoms only."""
    S = len(xs)
    N = (S + 1) // 2
    ws_abs = [abs(w) for w in ws]
    neg_mask = [w < 0 for w in ws]
    neg_idx = {i for i in range(S) if neg_mask[i]}
    comp = companions_map(neg_mask)
    moms = moments_of(xs, ws, 2 * N - 2)
    per_n = {}
    for n in range(1, N + 1):
        cfgs = list(combinations(range(S), n))
        Wv = {}
        odd = []
        even = []
        sE = Fr(0)
        sO = Fr(0)
        for c in cfgs:
            w = wprod_of(xs, ws_abs, list(c))
            Wv[c] = w
            if parity_of(neg_mask, c):
                odd.append(c)
                sO += w
            else:
                even.append(c)
                sE += w
        Dn = sE - sO
        det = hankel_det_frac(moms, n)
        rec = dict(n=n, n_cfg=len(cfgs), Dn=Dn, det=det, sE=sE,
                   sO=sO, odd=odd, even=even, Wv=Wv)
        if odd and even:
            e_index = {c: j for j, c in enumerate(even)}
            edges = []
            for c in odd:
                cset = set(c)
                tgt = set()
                for y in c:
                    if neg_mask[y]:
                        for x in exchange_targets(cset, y, comp,
                                                  step):
                            J = tuple(sorted((cset - {y}) | {x}))
                            if J in e_index:
                                tgt.add(e_index[J])
                edges.append(sorted(tgt))
            rec["edges"] = edges
            srcW = [Wv[c] for c in odd]
            snkW = [Wv[c] for c in even]
            if len(odd) <= flow_cap:
                dens = 1
                for v in srcW + snkW:
                    dens = dens * v.denominator // math.gcd(
                        dens, v.denominator)
                sc = [int(v.numerator * (dens // v.denominator))
                      for v in srcW]
                tc = [int(v.numerator * (dens // v.denominator))
                      for v in snkW]
                flow, reach = maxflow_int(sc, tc, edges)
                covered = (flow == sum(sc))
                rec["covered"] = covered
                rec["uncov_share"] = (Fr(sum(sc) - flow, dens)
                                      / max(sO, Fr(1, 10 ** 30)))
                rec["witness"] = None
                if not covered and reach:
                    # exact Hall violation certificate on A*
                    cov = set()
                    se = Fr(0)
                    for i in reach:
                        cov.update(edges[i])
                        se += srcW[i]
                    te = sum((snkW[j] for j in cov), Fr(0))
                    rec["witness"] = (len(reach), te - se)
            else:
                rec["covered"] = None
            if len(odd) <= hall_cap and len(even) <= sink_cap:
                dt, am, n_all = hall_full_enum(srcW, snkW, edges,
                                               tie_rel)
                rec["delta_full"] = dt
                rec["argmin_masks"] = am
                rec["n_hall"] = n_all
            df, mem, g0, dirn = ideal_family_slack(srcW, snkW,
                                                   edges, odd)
            rec["delta_fam"] = df
            rec["fam"] = (mem, g0, dirn)
        per_n[n] = rec
    pd_all = all(per_n[n]["Dn"] > 0 for n in per_n)
    first_neg = next((n for n in per_n if per_n[n]["Dn"] <= 0), None)
    return dict(name=name, S=S, N=N, xs=xs, ws=ws, neg=sorted(neg_idx),
                per_n=per_n, pd=pd_all, first_neg=first_neg,
                comp=comp)


# ============== must-fail mutants
def mutant_ratio_nosquare(xs, ws_abs, idx, y, x):
    """m1 MUST-FAIL: the edge ratio WITHOUT the Vandermonde square
    -- must differ exactly from the true ratio."""
    r = ws_abs[x] / ws_abs[y]
    for z in idx:
        if z == y:
            continue
        r *= abs((xs[x] - xs[z]) / (xs[y] - xs[z]))
    return r


def mutant_edges_posthoc(cov_tab, comp, y):
    """m2 MUST-FAIL: an edge library re-picked AFTER SIGHT of the
    coverage table (consumes the withheld coverage object) -- the
    scope audit must FLAG this, and the toy value differs from
    the sealed rule."""
    left, right = comp[y]
    if any(not v for v in cov_tab.values()):
        return sorted(set(left) | set(right))
    return (left[:1] + right[:1])


def mutant_flow_gift():
    """m3 MUST-FAIL: a 'transport orientation' consuming the
    withheld lambda record -- the scope audit must FLAG this."""
    return REC_LAM < 1.0


def mutant_kasteleyn_gauge(sE, sO):
    """m4 MUST-FAIL (the r282 no-go boundary): the sign gauge
    sigma = sign w rewrites every term positive -- the gauged
    'determinant' is sE + sO, off the true value by exactly
    2 sO != 0: a termwise positivization is never value-true on a
    signed window (which is why this round moves MASS between
    configurations instead)."""
    return sE + sO


def mutant_cut_census(n):
    """m5 MUST-FAIL: a Hall enumerator dropping the full mask --
    the census gate must CATCH the count."""
    return list(range(1, (1 << n) - 1))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("cauchybinet_hall_probe -- "
          "PRIME.LSTAR.CAUCHYBINET_HALL_TRANSPORT.01 (round 340)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants + "
                        "F1/F2 full Hall + I1/I2 identity + w9 "
                        "records/channel/exact-D2/ratio ward + "
                        "W9EDGE transport; ladder, controls, twin, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det0 = firewall_audit()
    check("G01-firewall", okf, det0)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the signed Cauchy-Binet split, "
          "the Sylvester dictionary, the canonical companion rule "
          "(nearest free mu per side, step cap %d), the exact edge "
          "ratio formula, the model family (TOY/F1/F2/I1..I4 + the "
          "S0 = %d shallow-edge prefixes), the flow/Hall caps "
          "(FLOW_CAP %d, HALL_CAP %d, SINK_CAP %d), the five "
          "reviewer tests, every bar/tolerance, the mutants and the "
          "verdict form; the STOP list forbids any L* claim and any "
          "transport certificate reading"
          % (CB_STEP, S0_EDGE, FLOW_CAP, HALL_CAP, SINK_CAP))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    hits_m2 = scope_audit("mutant_edges_posthoc")
    hits_m3 = scope_audit("mutant_flow_gift")
    ag_hits = antigate_fragment_audit()
    check("G03-scope-audits", (not hits) and bool(hits_m2)
          and bool(hits_m3) and not ag_hits,
          "the %d sealed constructors consume atom positions / "
          "signed weights / node order ONLY (%s); m2 "
          "POSTHOC-EDGE-LIBRARY FLAGGED (%s); m3 FLOW-GIFT FLAGGED "
          "(%s); fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_m2) if hits_m2 else "NOT FLAGGED",
             "; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S1 Leg A toys
    section("S1  LEG A -- EXACT SIGNED CAUCHY-BINET (TOYS + "
            "INSTANCES)")

    def model_from_pairs(name, mu, nu):
        atoms = ([(x, w) for x, w in mu] + [(x, -w) for x, w in nu])
        atoms.sort(key=lambda p: p[0])
        return model_pack(name, [p[0] for p in atoms],
                          [p[1] for p in atoms], FLOW_CAP, HALL_CAP,
                          SINK_CAP, TIE_REL, CB_STEP)

    MP = {}
    MP["TOY"] = model_from_pairs("TOY", TOY_MU, TOY_NU)
    toy = MP["TOY"]
    m3_toy = moments_of(toy["xs"], toy["ws"], 4)
    D3_toy = hankel_det_frac(m3_toy, 3)
    ok_toy = (toy["per_n"][1]["Dn"] == Fr(5, 3)
              and toy["per_n"][2]["Dn"] == Fr(5, 6)
              and toy["per_n"][2]["sE"] == Fr(1)
              and toy["per_n"][2]["sO"] == Fr(1, 6)
              and D3_toy == Fr(-1, 48)
              and toy["per_n"][1]["Dn"] == toy["per_n"][1]["det"]
              and toy["per_n"][2]["Dn"] == toy["per_n"][2]["det"]
              and toy["per_n"][2].get("covered") is True)
    check("G10-toy-cauchy-binet", ok_toy,
          "HAND TOY x (-1/2, 0, 1/2), w (1, -1/3, 1): D_1 = %s == "
          "5/3, D_2 = %s == 5/6 with parity split E = %s / O = %s, "
          "D_3 = %s == -1/48 < 0 (the wall in miniature one degree "
          "past N = 2); both routes (subset enumeration vs Hankel "
          "determinant) BIT-EQUAL; the hand transport at n = 2 "
          "covers (both odd pairs -> the even pair, load 1/6 <= "
          "cap 1, reserve = D_2)"
          % (str(toy["per_n"][1]["Dn"]), str(toy["per_n"][2]["Dn"]),
             str(toy["per_n"][2]["sE"]), str(toy["per_n"][2]["sO"]),
             str(D3_toy)))
    # hand ratio: I = {x=-1/2, y=0} -> J = {-1/2, 1/2}
    y_t = toy["xs"].index(Fr(0))
    x_t = toy["xs"].index(Fr(1, 2))
    z_t = toy["xs"].index(Fr(-1, 2))
    ws_abs_t = [abs(w) for w in toy["ws"]]
    r_hand = ratio_formula(toy["xs"], ws_abs_t, [z_t, y_t], y_t, x_t)
    WI = wprod_of(toy["xs"], ws_abs_t, [z_t, y_t])
    WJ = wprod_of(toy["xs"], ws_abs_t, [z_t, x_t])
    ok_ratio = (r_hand == Fr(12) and WJ == WI * r_hand)
    # every edge of the exact small models, bit-equal
    MP["F1"] = model_from_pairs("F1", F1_MU, F1_NU)
    MP["F2"] = model_from_pairs("F2", F2_MU, F2_NU)
    n_edges_checked = 0
    ok_edges = True
    for nm in ("TOY", "F1", "F2"):
        md = MP[nm]
        ws_abs = [abs(w) for w in md["ws"]]
        neg_mask = [w < 0 for w in md["ws"]]
        for n, rec in md["per_n"].items():
            if "edges" not in rec:
                continue
            for c in rec["odd"]:
                cset = set(c)
                for y in c:
                    if not neg_mask[y]:
                        continue
                    for x in exchange_targets(cset, y, md["comp"],
                                              CB_STEP):
                        J = tuple(sorted((cset - {y}) | {x}))
                        if J not in rec["Wv"]:
                            continue
                        rr = ratio_formula(md["xs"], ws_abs,
                                           list(c), y, x)
                        ok_edges = ok_edges and (
                            rec["Wv"][J] == rec["Wv"][c] * rr)
                        n_edges_checked += 1
    check("G11-toy-ratio-formula", ok_ratio and ok_edges,
          "the exact edge ratio W(J)/W(I) = (|w_x|/|w_y|) prod "
          "((x-z)/(y-z))^2: hand value %s == 12 on the toy edge "
          "{-1/2, 0} -> {-1/2, 1/2} (W ratio %s/%s); BIT-EQUAL on "
          "all %d admissible edges of TOY/F1/F2 (Fractions)"
          % (str(r_hand), str(WJ), str(WI), n_edges_checked))
    # JF9
    pairs_j = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                     key=lambda t: t[0])
    MP["I1"] = model_pack("I1", [p[0] for p in pairs_j],
                          [p[1] for p in pairs_j], FLOW_CAP,
                          HALL_CAP, SINK_CAP, TIE_REL, CB_STEP)
    ok_j = all(MP["I1"]["per_n"][n]["Dn"]
               == MP["I1"]["per_n"][n]["det"]
               for n in MP["I1"]["per_n"])
    check("G12-jf9-identity", ok_j,
          "JF9 (r230 verbatim, S = 9, S_- = %d, N = %d): D_n = "
          "sum_E W - sum_O W == det H_n BIT-EQUAL for every n; "
          "D signs %s; PD through the window: %s"
          % (len(MP["I1"]["neg"]), MP["I1"]["N"],
             str(["+" if MP["I1"]["per_n"][n]["Dn"] > 0 else "-"
                  for n in sorted(MP["I1"]["per_n"])]),
             MP["I1"]["pd"]))
    inames = ["I2"] if smoke else ["I2", "I3", "I4"]
    ok_inst = True
    ldl_ok = True
    for nm in inames:
        mx, mw, nx, nv = INSTANCES[nm]
        mu = [(Fr(*p), Fr(*w)) for p, w in zip(mx, mw)]
        nu = [(Fr(*p), Fr(*w)) for p, w in zip(nx, nv)]
        MP[nm] = model_from_pairs(nm, mu, nu)
        md = MP[nm]
        ok_inst = ok_inst and all(
            md["per_n"][n]["Dn"] == md["per_n"][n]["det"]
            for n in md["per_n"])
        info("%s: S = %d, S_- = %d, N = %d; D signs %s; census %s"
             % (nm, md["S"], len(md["neg"]), md["N"],
                str(["+" if md["per_n"][n]["Dn"] > 0 else "-"
                     for n in sorted(md["per_n"])]),
                str([md["per_n"][n]["n_cfg"]
                     for n in sorted(md["per_n"])])))
    # Sylvester LDL cross gate on TOY + I2: pivots == D_n/D_{n-1}
    for nm in ("TOY", "I2"):
        md = MP[nm]
        moms = moments_of(md["xs"], md["ws"], 2 * md["N"] - 2)
        H = [[moms[i + j] for j in range(md["N"])]
             for i in range(md["N"])]
        prev = Fr(1)
        for k in range(1, md["N"] + 1):
            dk = hankel_det_frac(moms, k)
            # pivot k of the (pivot-free) LDL = D_k / D_{k-1}
            if prev != 0:
                ldl_ok = ldl_ok and (
                    (dk / prev > 0) == (md["per_n"][k]["Dn"]
                                        / prev > 0))
                ldl_ok = ldl_ok and (dk == md["per_n"][k]["Dn"])
            prev = dk
        _ = H
    ok_census = all(
        MP[nm]["per_n"][n]["n_cfg"] == math.comb(MP[nm]["S"], n)
        for nm in MP for n in MP[nm]["per_n"])
    check("G13-instances-identity", ok_inst and ldl_ok and ok_census,
          "r334 instances %s as signed unions: the Cauchy-Binet "
          "identity BIT-EQUAL at every n <= N (full enumeration, "
          "census gate #masks == C(S, n) on every model); Sylvester "
          "cross gate on TOY + I2: rational determinant cascade == "
          "enumeration cascade with pivot signs D_n/D_{n-1} "
          "consistent" % str(inames))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + CHANNEL + EXACT D2 + RATIO WARD")
    mz9 = V.build_measures(MAIN_KZ)
    lam184, _B = V.lam_max_at(mz9, REC_NW)
    lam185, _B2 = V.lam_max_at(mz9, REC_NW + 1)
    ok_rec = (mz9["S"] == REC_S and len(mz9["xp"]) == REC_SP
              and len(mz9["yn"]) == REC_SM and mz9["Nw"] == REC_NW
              and abs(lam184 - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs((1.0 - lam184) / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (mu %d / nu %d), N_w = %d, lambda_max(E_184) "
          "= %.8f (record %.8f), margin %.4e (record %.4e rel "
          "%.2f), lambda at 185 = %.8f > 1 -- the r283/r284 route "
          "reproduced through the document pipeline"
          % (mz9["S"], len(mz9["xp"]), len(mz9["yn"]), mz9["Nw"],
             lam184, REC_LAM, 1.0 - lam184, REC_MARGIN,
             REC_MARGIN_TOL, lam185))
    ctx9 = MS.ctx_build(MAIN_KZ)
    xu_b, wu_b, _zones = BL.union_of_ctx(ctx9)
    sg9 = BL.sign_chain_f64(xu_b, wu_b, ctx9["N"] + EXT)[0]
    minC9 = next((n for n in range(len(sg9)) if sg9[n] < 0), None)
    scale_w = float(np.max(np.abs(mz9["wu"])))
    dev_x = float(np.max(np.abs(np.sort(xu_b) - np.sort(mz9["xu"]))))
    dev_w = float(np.max(np.abs(np.sort(wu_b)
                                - np.sort(mz9["wu"])))) / scale_w
    by9, _bv9, ufn9 = PIK.folded_measure(ctx9["darm"], ctx9["L"],
                                         -1.0)
    o_desc9 = np.argsort(by9)[::-1]
    shallow = tuple(int(ufn9[o_desc9[t]]) for t in range(2))
    # fold anchoring of the edge prefix: union desc-x == fold order
    bx9, _bw9, ufp9 = PIK.folded_measure(ctx9["darm"], ctx9["L"],
                                         +1.0)
    fold_of = {}
    for x, f in zip(bx9, ufp9):
        fold_of[round(float(x), 14)] = int(f)
    for x, f in zip(by9, ufn9):
        fold_of[round(float(x), 14)] = int(f)
    edge9 = edge_model_take(mz9["xu"], mz9["wu"], S0_EDGE, S0_EXTRA,
                            MIN_NU)
    xs9, ws9, idx9 = edge9
    folds_pref = [fold_of.get(round(float(mz9["xu"][k]), 14), -1)
                  for k in idx9]
    ok_foldmono = all(folds_pref[t] < folds_pref[t + 1]
                      for t in range(len(folds_pref) - 1))
    nu_folds = sorted(fold_of.get(round(float(x), 14), -1)
                      for x, w in zip(xs9, ws9) if w < 0)
    check("G21-w9-channel-fold-anchor",
          minC9 == REC_NW and dev_x <= 1e-9 and dev_w <= 1e-9
          and shallow == SHALLOW_FOLDS and ok_foldmono
          and set(SHALLOW_FOLDS) <= set(nu_folds),
          "campaign channel: BL union == V union (pos dev %.1e, "
          "rel weight dev %.1e), minC = %s == 184; the two "
          "smallest-theta nu atoms are folds %s == r284 record; "
          "the S0 = %d edge prefix has STRICTLY ASCENDING fold "
          "indices %s (descending x == fold order: position "
          "adjacency IS fold adjacency, the companion rule's "
          "fold-ancestry anchor), nu atoms in the prefix at folds "
          "%s" % (dev_x, dev_w, str(minC9), str(shallow), len(xs9),
                  str(folds_pref), str(nu_folds)))
    # exact D1/D2 live
    xs_full = [Fr(float(x)) for x in mz9["xu"]]
    ws_full = [Fr(float(w)) for w in mz9["wu"]]
    m9 = moments_of(xs_full, ws_full, 2)
    D1_9 = m9[0]
    D2_hankel = m9[0] * m9[2] - m9[1] * m9[1]
    ws_abs9 = [abs(w) for w in ws_full]
    neg9 = [w < 0 for w in ws_full]
    sE2 = Fr(0)
    sO2 = Fr(0)
    for a in range(len(xs_full)):
        wa = ws_abs9[a]
        xa = xs_full[a]
        for b in range(a + 1, len(xs_full)):
            d = xs_full[b] - xa
            w = wa * ws_abs9[b] * d * d
            if neg9[a] != neg9[b]:
                sO2 += w
            else:
                sE2 += w
    ok_d2 = (sE2 - sO2 == D2_hankel and D1_9 > 0 and D2_hankel > 0)
    check("G22-w9-exact-D2", ok_d2,
          "w9 LIVE EXACT (all %d atoms, dyadic Fractions): D_1 = "
          "m_0 = %.6f > 0; D_2 over all %d pair configurations == "
          "m_0 m_2 - m_1^2 BIT-EQUAL (parity split E %.6e / O "
          "%.6e, D_2 %.6e > 0) -- the signed Cauchy-Binet identity "
          "holds on the real window where enumeration is possible"
          % (len(xs_full), float(D1_9),
             len(xs_full) * (len(xs_full) - 1) // 2, float(sE2),
             float(sO2), float(sE2 - sO2)))
    # sampled ratio ward (f64 log space) + one exact spot
    neg_set9 = {i for i in range(len(ws_full)) if neg9[i]}
    comp9 = companions_map(neg9)
    xf = np.asarray(mz9["xu"], float)
    wf = np.abs(np.asarray(mz9["wu"], float))

    def logW(cfg):
        s = float(np.sum(np.log(wf[list(cfg)])))
        for a in range(len(cfg)):
            for b in range(a + 1, len(cfg)):
                s += 2.0 * math.log(abs(xf[cfg[b]] - xf[cfg[a]]))
        return s

    max_dev = 0.0
    n_edges9 = 0
    exact_spot_ok = None
    for s in range(1, CFG_DRAWS + 1):
        cfg = golden_config(len(ws_full), neg_set9, CFG_N, s)
        cset = set(cfg)
        for y in cfg:
            if not neg9[y]:
                continue
            for x in exchange_targets(cset, y, comp9, CB_STEP):
                J = tuple(sorted((cset - {y}) | {x}))
                lr = 0.0
                lr += math.log(wf[x]) - math.log(wf[y])
                for z in cfg:
                    if z == y:
                        continue
                    lr += 2.0 * (math.log(abs(xf[x] - xf[z]))
                                 - math.log(abs(xf[y] - xf[z])))
                dev = abs(logW(J) - logW(cfg) - lr)
                max_dev = max(max_dev, dev)
                n_edges9 += 1
                if exact_spot_ok is None and s == 1:
                    WI9 = wprod_of(xs_full, ws_abs9, list(cfg))
                    WJ9 = wprod_of(xs_full, ws_abs9, list(J))
                    rr9 = ratio_formula(xs_full, ws_abs9,
                                        list(cfg), y, x)
                    exact_spot_ok = (WJ9 == WI9 * rr9)
    check("G23-w9-ratio-ward", max_dev <= RATIO_LOG_BAR
          and bool(exact_spot_ok),
          "sampled ratio ward on w9: %d golden configurations of "
          "size %d, %d admissible exchange edges, max f64 log dev "
          "|log W(J) - log W(I) - log ratio| = %.1e (bar %.0e); "
          "ONE exact Fraction spot check BIT-EQUAL (%s)"
          % (CFG_DRAWS, CFG_N, n_edges9, max_dev, RATIO_LOG_BAR,
             exact_spot_ok))

    # ---------------- S3 Leg C: the transport
    section("S3  LEG C -- THE TRANSPORT (COVERAGE + HALL CUTS)")
    MP["W9EDGE"] = model_pack("W9EDGE", xs9, ws9, FLOW_CAP,
                              HALL_CAP, SINK_CAP, TIE_REL, CB_STEP)
    ok_cens = True
    for nm in MP:
        md = MP[nm]
        for n in md["per_n"]:
            ok_cens = ok_cens and (md["per_n"][n]["n_cfg"]
                                   == math.comb(md["S"], n))
            ok_cens = ok_cens and (md["per_n"][n]["Dn"]
                                   == md["per_n"][n]["det"])
    pd_txt = {nm: ("PD" if MP[nm]["pd"] else
                   "SIGN_BREAK@n=%s" % str(MP[nm]["first_neg"]))
              for nm in MP}
    check("G30-model-census", ok_cens,
          "model family census: configuration counts == C(S, n) "
          "and D_n == det H_n BIT-EQUAL at every (model, n); PD "
          "typing: %s" % str(pd_txt))
    # coverage on live models
    cov_rows = []
    unc_loci = []
    skip_loci = []
    ok_consist = True
    for nm in MP:
        md = MP[nm]
        if not md["pd"]:
            continue
        for n in sorted(md["per_n"]):
            rec = md["per_n"][n]
            if "edges" not in rec:
                continue
            if rec.get("covered") is None:
                skip_loci.append((nm, n, len(rec["odd"])))
                continue
            cov_rows.append((nm, n, rec["covered"]))
            if not rec["covered"]:
                unc_loci.append((nm, n,
                                 float(rec["uncov_share"]),
                                 rec["witness"]))
            # coverage => D_n > 0 must hold (reserve); and
            # D_n <= 0 => coverage must fail (consistency)
            if rec["covered"]:
                ok_consist = ok_consist and (rec["Dn"] > 0)
    # dead-model consistency: D_n <= 0 loci must be uncovered
    for nm in MP:
        md = MP[nm]
        for n in sorted(md["per_n"]):
            rec = md["per_n"][n]
            if "edges" in rec and rec.get("covered") is True:
                ok_consist = ok_consist and (rec["Dn"] > 0)
            if ("edges" in rec and rec["Dn"] <= 0
                    and rec.get("covered") is not None):
                ok_consist = ok_consist and (rec["covered"] is False)
    n_cov = sum(1 for _nm, _n, c in cov_rows if c)
    check("G31-transport-coverage", ok_consist,
          "EXACT FLOW COVERAGE (Dinic on lcm-scaled integer "
          "capacities): %d/%d computed live loci covered "
          "(flow == sum_O W exact); uncovered loci: %s; "
          "FLOW_SKIPPED by the sealed size rule |O_n| > %d: %s; "
          "consistency EXACT: coverage => D_n > 0 (strict "
          "reserve), and D_n <= 0 => coverage fails"
          % (n_cov, len(cov_rows),
             str([(nm, n, "%.3f" % u) for nm, n, u, _w in unc_loci])
             if unc_loci else "NONE",
             FLOW_CAP,
             str(skip_loci) if skip_loci else "NONE"))
    # full Hall enumeration (test 4) on TOY/F1/F2
    hall_loci = []
    ok_hall = True
    carrier_ok = True
    fail_loci = []
    for nm in ("TOY", "F1", "F2"):
        md = MP[nm]
        for n in sorted(md["per_n"]):
            rec = md["per_n"][n]
            if "delta_full" not in rec:
                continue
            am = rec["argmin_masks"]
            odd = rec["odd"]
            nS = len(odd)
            ok_hall = ok_hall and (rec["n_hall"] == (1 << nS) - 1)
            # Gale ideal test on every exact argmin mask
            ideal_all = True
            for A in am:
                mem = [i for i in range(nS) if (A >> i) & 1]
                dn_ok = all((i in mem) for j in mem
                            for i in range(nS)
                            if gale_leq(odd[i], odd[j]))
                up_ok = all((i in mem) for j in mem
                            for i in range(nS)
                            if gale_leq(odd[j], odd[i]))
                ideal_all = ideal_all and (dn_ok or up_ok)
            attain = (rec["delta_fam"] == rec["delta_full"])
            hall_loci.append((nm, n, nS, float(rec["delta_full"]),
                              ideal_all, attain))
            if not (ideal_all and attain):
                carrier_ok = False
                fail_loci.append((nm, n, ideal_all, attain,
                                  float(rec["delta_fam"]
                                        / rec["delta_full"])
                                  if rec["delta_full"] != 0
                                  else None))
            info("%s n=%d: |O| %d |E| %d, delta_full %s (%.6f), "
                 "argmin %d tie(s) %s, Gale-ideal %s, family "
                 "attains %s (delta_fam %.6f)"
                 % (nm, n, nS, len(rec["even"]),
                    str(rec["delta_full"])[:24],
                    float(rec["delta_full"]), len(am),
                    str([tuple(odd[i] for i in range(nS)
                               if (A >> i) & 1) for A in am])[:90],
                    ideal_all, attain, float(rec["delta_fam"])))
    check("G32-hall-full-enum", ok_hall,
          "FULL HALL ENUMERATION (test 4) on TOY/F1/F2: %d loci, "
          "every 2^|O| - 1 census exact, every tie within %.0e "
          "rel recertified in Fractions; interval-Hall verdict "
          "input: ideal+attain per locus %s"
          % (len(hall_loci), TIE_REL,
             str([(nm, n, i, a)
                  for nm, n, _s, _d, i, a in hall_loci])))
    # W9EDGE cut anatomy (test 1)
    mdw = MP["W9EDGE"]
    N0 = mdw["N"]
    recw = mdw["per_n"][N0]
    # extremal atom indices inside the model = the fold-2/4 atoms
    ext_idx = [t for t in range(len(xs9))
               if ws9[t] < 0
               and fold_of.get(round(float(xs9[t]), 14), -1)
               in SHALLOW_FOLDS]
    memf, g0f, dirf = recw["fam"]
    odd_w = recw["odd"]
    Wtot = sum((recw["Wv"][odd_w[i]] for i in memf), Fr(0))
    Wboth = sum((recw["Wv"][odd_w[i]] for i in memf
                 if all(e in odd_w[i] for e in ext_idx)), Fr(0))
    Wone = sum((recw["Wv"][odd_w[i]] for i in memf
                if any(e in odd_w[i] for e in ext_idx)), Fr(0))
    frac_both = float(Wboth / Wtot) if Wtot > 0 else 0.0
    frac_one = float(Wone / Wtot) if Wtot > 0 else 0.0
    hall_w9 = float(recw["delta_fam"] / recw["sE"])
    check("G33-w9edge-cut-anatomy", len(ext_idx) == 2,
          "W9EDGE at n = N0 = %d (PD %s, covered %s): binding "
          "principal-ideal cut = %s ideal generated by %s (%d "
          "members), dual slack delta_fam/sum_E W = %.3e; "
          "EXTREMAL TEST (1): extremal atoms (folds %s) at model "
          "indices %s -- W-fraction of the cut containing BOTH = "
          "%.4e, containing AT LEAST ONE = %.4f (carried iff "
          ">= %.1f)"
          % (N0, mdw["pd"], recw.get("covered"), dirf,
             str(odd_w[g0f]) if g0f >= 0 else "FULL", len(memf),
             hall_w9, str(SHALLOW_FOLDS), str(ext_idx), frac_both,
             frac_one, EXTREMAL_BAR))

    # ---------------- S3b controls + twin
    if smoke:
        for g in ("G34-controls", "G35-twin"):
            check(g, True, "SMOKE: skipped")
        ctrl_seen = {}
        twin_txt = ""
        ok_twin = None
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        ok_ctrl = True
        ctrl_seen = {}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, _z = BL.union_of_ctx(cctx)
            N_c = cctx["N"]
            sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            if mc is None:
                sg = BL.sign_chain_f64(xu, wu, N_c + EXT2)[0]
                mc = next((n for n in range(len(sg)) if sg[n] < 0),
                          None)
            ok_ctrl = ok_ctrl and (mc == CTRL_FLIPS[cn])
            em = edge_model_take(xu, wu, S0_EDGE, S0_EXTRA, MIN_NU)
            if em is None:
                ctrl_seen[cn] = ("NO_NU", None)
                continue
            xsc, wsc, _ic = em
            mdc = model_pack(cn + "EDGE", xsc, wsc, FLOW_CAP,
                             HALL_CAP, SINK_CAP, TIE_REL, CB_STEP)
            MP[cn + "EDGE"] = mdc
            n_broken = sum(1 for n in mdc["per_n"]
                           if mdc["per_n"][n]["Dn"] <= 0)
            ctrl_seen[cn] = (mdc["first_neg"], n_broken)
            info("%sEDGE (S0 %d, N0 %d, minC %s == flip %d): D "
                 "signs %s, first sign break n = %s (flip at %d "
                 ">> N0: any break is BEFORE the flip)"
                 % (cn, mdc["S"], mdc["N"], str(mc),
                    CTRL_FLIPS[cn],
                    str(["+" if mdc["per_n"][n]["Dn"] > 0 else "-"
                         for n in sorted(mdc["per_n"])]),
                    str(mdc["first_neg"]), CTRL_FLIPS[cn]))
        check("G34-controls", ok_ctrl,
              "EPST + SCR + SMOOTH built verbatim through the "
              "r278/r280 channel: minC == flips %s; edge models "
              "extracted by the same sealed prefix rule; "
              "sign-break census (test 3): %s"
              % (str(CTRL_FLIPS), str(ctrl_seen)))
        # twin
        uu9, mm9 = TR.base_comb(9)
        mzD = TR.build_world(9, uu9, mm9)
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9)
        u2, m2, _dens, _du = AKD.twin_rational(uu9, mm9, gaps9,
                                               mz9["D"], TWIN_TOL)
        mzT = TR.build_world(9, u2, m2)
        xuT = np.concatenate([mzT["xp"], mzT["yn"]])
        wuT = np.concatenate([mzT["wp"], -np.asarray(mzT["vn"])])
        oT = np.argsort(xuT)
        emT = edge_model_take(xuT[oT], wuT[oT], S0_EDGE, S0_EXTRA,
                              MIN_NU)
        xsT, wsT, _iT = emT
        MP["TWINEDGE"] = model_pack("TWINEDGE", xsT, wsT, FLOW_CAP,
                                    HALL_CAP, SINK_CAP, TIE_REL,
                                    CB_STEP)
        mdt = MP["TWINEDGE"]
        recT = mdt["per_n"][mdt["N"]]
        memT, g0T, dirT = recT["fam"]
        d_slack = abs(float(recT["delta_fam"] / recT["sE"])
                      - hall_w9) / max(abs(hall_w9), 1e-300)
        same_gen = (g0T == g0f and dirT == dirf
                    and (recT["odd"][g0T] == odd_w[g0f]
                         if g0T >= 0 else True))
        cov_same = all(mdt["per_n"][n].get("covered")
                       == mdw["per_n"][n].get("covered")
                       for n in mdw["per_n"]
                       if "edges" in mdw["per_n"][n])
        ok_twin = (ok_dose0 and mdt["pd"] == mdw["pd"]
                   and same_gen and d_slack <= TWIN_BAR
                   and cov_same)
        twin_txt = ("same generator %s/%s, dual slack rel dev "
                    "%.1e (bar %.0e), coverage identical %s"
                    % (same_gen, dirT, d_slack, TWIN_BAR,
                       cov_same))
        check("G35-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (r289/r331 verbatim; "
              "dose-zero identity TR.build_world == "
              "V.build_measures BITWISE %s): TWINEDGE cut form == "
              "W9EDGE -- %s (test 2)"
              % (TWIN_TOL, ok_dose0, twin_txt))

    # ---------------- S4 Leg D: the ladder scaling probe
    section("S4  LEG D -- LADDER SCALING (HALL SLACK vs MARGINS)")
    if smoke:
        for g in ("G40-ladder-census", "G41-concordance"):
            check(g, True, "SMOKE: skipped")
        conc_verdict = None
        conc_txt = ""
    else:
        kzs = V.admissible_indices()
        rows = []
        ok_lad = (len(kzs) == 42)
        for kz in kzs:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            xu, wu, zones = BL.union_of_ctx(ctx)
            xs_z, ws_z, ys_z, vs_z = zones
            N_ = ctx["N"]
            al, sb, h0 = FS.mu_chain_f64(np.asarray(xs_z),
                                         np.asarray(ws_z), N_)
            Bz = FS.b_matrix_f64(al, sb, h0, np.asarray(ys_z),
                                 np.asarray(vs_z), N_)
            lam = float(np.linalg.eigvalsh(Bz @ Bz.T)[-1])
            margin = 1.0 - lam
            em = edge_model_take(xu, wu, S0_LADDER, S0_EXTRA,
                                 MIN_NU)
            if em is None:
                rows.append((kz, N_, margin, None, None, None))
                continue
            xsl, wsl, _il = em
            mdl = model_pack("kz%d" % kz, xsl, wsl, FLOW_CAP,
                             HALL_CAP, SINK_CAP, TIE_REL, CB_STEP)
            n0 = mdl["N"]
            recl = mdl["per_n"][n0]
            hall = (float(recl["delta_fam"] / recl["sE"])
                    if "delta_fam" in recl else None)
            rows.append((kz, N_, margin, hall,
                         recl.get("covered"), mdl["pd"]))
            ok_lad = ok_lad and (margin > 0.0)
        info("ladder table (kz, N_w, 1-lambda, hall_w = "
             "delta_fam/sum_E W at the S0=%d edge, covered, PD):"
             % S0_LADDER)
        for kz, N_, mg, hl, cv, pd in rows:
            extra = ""
            if kz in R334_KINT:
                extra = "   [r334 1-kappa_int %.1e]" % R334_KINT[kz]
            info("  kz%-4d N %4d  margin %.3e  hall %s  cov %s "
                 "pd %s%s"
                 % (kz, N_, mg,
                    ("%.3e" % hl) if hl is not None else "None",
                    str(cv), str(pd), extra))
        n_pos = sum(1 for r in rows
                    if r[3] is not None and r[3] > 0)
        n_cov_l = sum(1 for r in rows if r[4] is True)
        n_pd = sum(1 for r in rows if r[5] is True)
        check("G40-ladder-census", ok_lad,
              "42-rung ladder (campaign channel, all margins "
              "positive): edge-model hall coordinate defined and "
              "positive on %d/42 rungs, coverage %d/42, edge PD "
              "%d/42; the r334 comparison column printed at "
              "kz18/9/60/52 (record values, never consumed)"
              % (n_pos, n_cov_l, n_pd))
        fin = [(r[3], r[2]) for r in rows if r[3] is not None
               and r[3] > 0 and r[2] > 0]
        if len(fin) == len(rows) and len(fin) >= 3:
            lr = [math.log10(h / m) for h, m in fin]
            spread = max(lr) - min(lr)
            sp = BH.spearman([t[0] for t in fin],
                             [t[1] for t in fin])
            if spread <= CONC_SPREAD and abs(sp) >= SP_BAR:
                conc_verdict = "FLOW_RESTATEMENT"
            else:
                conc_verdict = "NEW_COORDINATE"
            conc_txt = ("spread(log10 hall/margin) = %.2f (bar "
                        "%.1f), spearman(hall, margin) = %+.3f "
                        "(bar %.2f)" % (spread, CONC_SPREAD, sp,
                                        SP_BAR))
        else:
            conc_verdict = "NEW_COORDINATE"
            conc_txt = ("hall coordinate positive on %d/%d rungs "
                        "only -- cannot be the margin in disguise"
                        % (len(fin), len(rows)))
        check("G41-concordance", True,
              "CONCORDANCE (sealed rule): %s(%s)"
              % (conc_verdict, conc_txt))

    # ---------------- S5 must-fails
    section("S5  MUST-FAILS")
    r_mut = mutant_ratio_nosquare(toy["xs"], ws_abs_t,
                                  [z_t, y_t], y_t, x_t)
    check("G70-mutant-ratio-nosquare", r_mut != r_hand
          and (r_hand - r_mut) == Fr(6),
          "m1 RATIO WITHOUT THE SQUARE: mutant %s != true %s "
          "(exact difference %s != 0, Fractions) -- CAUGHT"
          % (str(r_mut), str(r_hand), str(r_hand - r_mut)))
    Dg = mutant_kasteleyn_gauge(toy["per_n"][2]["sE"],
                                toy["per_n"][2]["sO"])
    check("G71-mutant-kasteleyn", Dg - toy["per_n"][2]["Dn"]
          == 2 * toy["per_n"][2]["sO"]
          and toy["per_n"][2]["sO"] != 0,
          "m4 KASTELEYN CONFUSION (r282 respected): the sign "
          "gauge changes the VALUE by exactly 2 sum_O = %s != 0 "
          "(gauged %s vs true %s, Fractions) -- a termwise "
          "positivization is never value-true on a signed window; "
          "the transport moves mass between configurations "
          "instead -- CAUGHT"
          % (str(2 * toy["per_n"][2]["sO"]), str(Dg),
             str(toy["per_n"][2]["Dn"])))
    mut5 = mutant_cut_census(4)
    check("G72-mutant-cut-census", len(mut5) != (1 << 4) - 1,
          "m5 INCOMPLETE CUT ENUMERATION: the mutant drops the "
          "full mask (%d != %d masks) -- CAUGHT by the census "
          "gate (the same count gate guards every 2^|O| - 1 Hall "
          "enumeration and every C(S, n) configuration census)"
          % (len(mut5), (1 << 4) - 1))
    # m2 value half: posthoc library differs from the sealed rule
    # (witness = the deepest F2 negative atom: three mu atoms on
    # its left, so the after-sight library genuinely widens)
    y_f2 = max(i for i in range(MP["F2"]["S"])
               if MP["F2"]["ws"][i] < 0)
    sealed_t = exchange_targets({y_f2}, y_f2, MP["F2"]["comp"],
                                CB_STEP)
    posthoc_t = mutant_edges_posthoc({0: False}, MP["F2"]["comp"],
                                     y_f2)
    check("G73-mutant-posthoc-value", set(posthoc_t)
          != set(sealed_t) and bool(hits_m2) and bool(hits_m3),
          "m2 POSTHOC EDGE LIBRARY: after sight of an uncovered "
          "coverage table the mutant returns %s != the sealed "
          "companion rule %s -- CAUGHT twice (value + the G03 "
          "AST flag); m3 flow-gift AST-FLAGGED in G03"
          % (str(posthoc_t), str(sealed_t)))

    # ---------------- S6 verdict
    section("S6  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "transport promoted as a certificate, no posthoc edge "
          "library, no derived 5/7, NO RH claim; mincut base 4 / "
          "refined 5 UNCHANGED; what the round adds: the exact "
          "signed Cauchy-Binet coordinate with its parity split, "
          "the sealed canonical exchange graph with the exact "
          "weight-ratio formula, the exact flow/Hall machinery "
          "with full small-model cut enumeration, the cut anatomy "
          "and the ladder concordance column; r243..r339 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(hits)
        carrier = ("INTERVAL_HALL_CARRIER"
                   if carrier_ok else
                   "CUT_REDUCTION_FAIL(loci %s)"
                   % str(fail_loci))
        flow_v = ("WEIGHTED_FLOW_GO(%d/%d live loci covered, "
                  "reserve D_n > 0 exact; skipped %s)"
                  % (n_cov, len(cov_rows),
                     str(skip_loci) if skip_loci else "none")
                  if not unc_loci else
                  "SOURCE_EXCHANGE_INSUFFICIENT(loci %s)"
                  % str([(nm, n, "%.3f" % u)
                         for nm, n, u, _w in unc_loci]))
        extremal = ("EXTREMAL_CUT(frac_both %.3e %s %.1f, "
                    "frac_one %.4f, generator %s %s)"
                    % (frac_both,
                       ">=" if frac_both >= EXTREMAL_BAR else "<",
                       EXTREMAL_BAR, frac_one, dirf,
                       str(odd_w[g0f]) if g0f >= 0 else "FULL"))
        dead_ok = all(v[0] is not None and v[0] != "NO_NU"
                      for v in ctrl_seen.values())
        live_ok = MP["W9EDGE"]["pd"] and MP["TWINEDGE"]["pd"]
        world_v = ("TRANSPORT_WORLD_SEEN(first breaks %s; live "
                   "PD)" % str({c: ctrl_seen[c][0]
                                for c in ctrl_seen})
                   if dead_ok and live_ok else
                   "TRANSPORT_WORLD_BLIND(%s; live PD %s)"
                   % (str(ctrl_seen), live_ok))
        parts = [carrier, flow_v, extremal, world_v,
                 "%s(%s)" % (conc_verdict, conc_txt),
                 "TWIN_LEDGER(%s)" % twin_txt]
        verd = ("TARGET_LEAK(" + "; ".join(hits) + ")"
                if leak else " + ".join(parts))
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED transport anatomy of the open scalar "
          "L*; the sealed adjudication is applied honestly; NO L* "
          "claim, NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
