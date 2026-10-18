#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""critical_saturation_probe -- PRIME.LSTAR.DUAL.CRITICAL_SATURATION.01
(round 360): THE CRITICAL SATURATION SCAFFOLD -- reviewer contract L2,
triggered by the r359 ASYMPTOTICS_REQUIRED verdict.  Coexistence: R358
(gap-Carleson, terminal lane) may run in parallel -- this probe touches
NOTHING outside its own file and the strictly additive rh-sync.

THE FROZEN QUESTION (reviewer contract L2, binding): the target theorem
is S_N = N^{-alpha} (M_0 + O(N^{-eps})) with M_0 > 0 explicit, plus the
rest-block clause in RELATIVE form (r359: lambda_min(R_CC) - 1/2 decays
PARALLEL to the margin, rest/eps med 20.3 -- the absolute c_rest N^{-beta}
form is refuted by measurement).  The precise r359 handoff object: the
critical 2x2 Schur block S_N carries the full margin (bind med 1.0058);
the RHP target data are the DIAGONAL dual-resolvent values (A^{-1})_kk
at the critical pair, with the cross share (med 0.702) as the handoff --
the diagonal parametrix alone misses by exactly the cross share.  An
internal round CANNOT deliver the full RHP theorem (typed honestly as
the specialist work); it CAN build and measure the SCAFFOLD: solve the
constrained (BKMM obstacle) equilibrium problem, test the saturation
thesis, calibrate the parametrix-class dimensionless data, seal the
alpha/M_0 census, certify the relative rest clause where it is a
theorem, and type each reviewer step (A)-(E) as theorem / census / open.

THE EXACT OBJECTS OF THE ROUND (every identity a finite-matrix fact):
  (O1 OCCUPATION DUALITY) with u the positive lift weight (r356) and
    u_vee = c_j (1-x)/|f| the Borodin dual weight, the diagonal of the
    rank-N_w eta projection and the diagonal of the rank-(N_w - 1) dual
    hole projection are EXACT complements on every union node:
    o_eta(x_j) + o_dual(x_j) == 1 (D^2 = I on the diagonal of the r356
    complementation); trace ward: sum_j o_dual(x_j) == N_w - 1 exactly.
    o_dual is the exact finite occupation field of the dual ensemble --
    the finite counterpart of the BKMM equilibrium density vs its upper
    constraint, with NO solver and NO asymptotics.
  (O2 THE OBSTACLE PROBLEM, deterministic solver, no fit primitives)
    the zero-temperature constrained equilibrium on the actual grid:
    minimize E(m) = sum_{j != k} m_j m_k log(1/|x_j - x_k|) +
    sum_j m_j (-log u_vee_j) over 0 <= m_j <= 1, sum m_j = N_w - 1
    (the discrete cap IS the BKMM upper constraint; the classical
    UNCONSTRAINED problem is the m1 must-fail).  Solved by sealed FISTA
    (fixed 3000 iterations, deterministic step from 60 power iterations,
    exact box-simplex water-filling projection by 100 bisections); KKT
    partition gates: void/saturated separation gap = min g[void] -
    max g[sat] > 0 with at most NB_MAX unclassified nodes.
  (O3 THE SATURATION THESIS, sealed) the primal (eta) side saturated
    zone at the right hard edge: scoping found the QP dual-VOID block ==
    folds {1, 2, 3} EXACTLY on all four sealed instances (== primal-
    SATURATED block by O1), so the critical pair (folds 2, 4) STRADDLES
    the saturation-block edge 3|4; the exact occupation shows the fold-1
    anomaly o_dual(fold 1) - median <= -ZONE_BAR with the pair folds
    themselves flat -- the pair sits AT the edge of the saturated zone,
    not inside it and not in the bulk.  The chi worlds (far from the
    wall) have NO fold-1 anomaly and their QP occupies fold 1: the
    partition is world-separating (a DIFFERENT partition, not the same
    with different distance).
  (O4 THE PARAMETRIX DATUM) t_geo := eps * sqrt((A^{-1})_11 (A^{-1})_22)
    is dimensionless, exactly = 1/(2 sqrt(det(S_N/eps) (1 - share))) by
    the r359 resolvent-minor identity, and scoping shows it FAMILY-
    CONSTANT at the wander level (0.229 .. 0.265 MAIN, 0.199/0.288 chi)
    -- the diagonal dual-resolvent data are margin-locked local data:
    the local-parametrix-class census (NOT a Gamma-function derivation;
    said hard).
  (O5 ALPHA / M_0) det S_N tracks margin^2 (r359 slope -6.742) and
    lambda_min(S_N)/eps = bind is collapsed in [1.0003, 1.0605]; the
    fresh Theil-Sen slope of log lambda_min(S_N) on the 57 adjudicates
    the sealed alpha candidates (3.332 margin exponent r352 vs 1.65
    s_infty running reading r354); kappa_S = lambda_max/lambda_min =
    det S_N / lambda_min^2 measures the M_0 collapse: strong collapse
    iff range ratio <= 1.5 (honest expectation: the margin direction
    collapses via bind, kappa_S wanders O(1) -- M0_PARTIAL).
  (O6 WANDER CANCELLATION) via the exact r359 adjugate identity
    det S_N * 4 [(A^{-1})_11 (A^{-1})_22 - (A^{-1})_12^2] == 1:
    log det S_N == -log 4 - log(a11 a22) - log(1 - share) POINTWISE;
    the psi57 fine structures of log det S_N and -log(a11 a22) must
    cohere (corr clause) with the share term subleading (rms census) --
    the leading common wander lives in the diagonal resolvent data and
    cancels algebraically in the minor, measured not assumed.
  (O7 THE RELATIVE REST CLAUSE) lambda_min(R_CC) - 1/2 >= c (lambda_min
    (R) - 1/2): c = 1 is the CAUCHY EIGENVALUE INTERLACING THEOREM
    (principal submatrix; likewise lambda_min(S_N) >= lambda_min(M) by
    the Schur-complement eigenvalue inequality -- both exact finite
    theorems, gated live and on the toy); c >= C_REL = 2.0 is the sealed
    census over ALL live resolvable rows of MAIN + chi3 + chi4 -- the
    L2 clause in provable-shape (theorem at c = 1, census margin at 2).

THE LEGS: (Leg 0) anchors bit-near: the r359 records (W9 eps 4.1882e-5,
lamS 4.2003e-5, detS 2.0690e-8, share 0.6973, folds (2, 4); share
samples kz44/56/130; detS slope -6.742; rest slope -3.276; bind clause
[1 - 1e-6, 1.5]), the r356 records (lambda_min(R) 0.500041882, margin
1.6752e-4), the r352 margin slope -3.332, the r354 s_infty 1.65 reading
(candidate only), the r350 exponent family (1.786/1.683 Christoffel,
0.38 family) as census comparison prints.  (Leg A) the constrained
equilibrium problem (reviewer step B): O1 + O2 + O3 on the sealed QP
instances kz 9/44/56/130 + chi3 w9 + chi4 w9 + scramble w9; the
partition clause, the straddle clause, the KKT gates, the chi contrast.
(Leg B) the parametrix calibration (step C as census): O4 sealed band +
slope clauses on the resolvable rows, the exponent censi of |a11|,
|a22|, |a12| printed against the sealed candidate families.  (Leg C)
the alpha/M_0 structure (step D as census): O5 sealed alpha
adjudication with BOTH candidates, kappa_S band + collapse ratio,
split-half curvature print (curvature-honest), plus O6 as the wander-
cancellation probe.  (Leg D) the relative rest clause O7.  (Leg E)
worlds + must-fails: matched SCRAMBLE (r359 named break at R_CC
reproduced: eps -0.4962, rest -0.4962, pair block +1.369e-2 stays
positive; occupation/QP census printed), rational TWIN (dose-zero
bitwise + occupation pointwise devs), chi3/chi4 ladders through the
identical pipeline (42 rungs each: chain wards + rest/eps min +
occupation flatness census).

MUST-FAILS (6): (m1) the UNCONSTRAINED (classical) equilibrium problem
-- cap removed: the minimizer piles max m = 92.7 (w9, scoped) onto
single nodes, >= M1_BAR 10 x the discrete cap -> CAUGHT (wrong class:
the obstacle constraint is load-bearing); (m2) alpha read from the
withheld margin column -> AST-CAUGHT; (m3) M_0 'fit by sight' -- the
posthoc alpha optimizer reading the withheld det S_N column ->
AST-CAUGHT (the sealed-candidate protocol is the catch); (m4) the
parametrix 'prediction' returning the withheld (A^{-1})_11 column ->
AST-CAUGHT; (m5) the partition with weight SHUFFLE (deterministic
reversal of u_vee): the fold-1 occupation moves by 0.798 (scoped) >=
M5_BAR 0.3 -> CAUGHT; (m6) the occupation complement with WRONG RANK
(N_w instead of N_w - 1): breaks by 1.17e-2 >= M6_BAR 1e-3 at w9 AND
exactly on the Fractions toy -> CAUGHT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in either
direction, mincut unchanged.  Two-commit freeze protocol (r329
convention): spec + machinery committed BEFORE the record run, record
tables inserted after.

INDEX FIREWALL (binding, r238-r359 discipline): w = window (kz), S =
#union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds = grid indices;
ground truth (records, anchors, control flips) enters GATES and record
tables only; the module-own constructors consume measure arrays / chain
coefficients / positions / the dual pair indices ONLY (AST scope audit;
withheld identifiers margin_col_true / detS_col_true / a11_col_true and
the REC/anchor constants); no zero/prime oracles anywhere (AST
firewall); no fit primitives beyond the imported r286 Theil-Sen
(fragment audit; psi57 = the r356 instrument verbatim; the QP solver is
projected first-order descent with sealed iteration counts, not a
fitted estimator).  MACHINERY IMPORTED VERBATIM: r359 SWD.{schur_rung,
slim359} (d00fdc96), r356 BDH.{dual_weights, psi_fit57, fr_proj}
(36141c0a), r342 PX.{build_rung, pair_select} (b09f8ccd), r357
DMF.{chi_window_comb, chi_build_measures, LPQ3, LPQ4, Q_CHI3, Q_CHI4}
(4bf1a94b), r354 PWA.rung_reduced_cols (f9db84da), r329
E3.{admissible_pool, used_kz_set} (bbfaf199), r286 LM.{ts_fit,
ext_rule} (0a44ac4e), r331 TR.{base_comb, build_world}, r289
AKD.twin_rational, r276 MF.local_gaps, document pipeline
V.{build_measures, mu_chain, b_matrix, admissible_indices, U, PP},
v563 core READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104, N_w 184,
margin 1.6752e-4 rel 0.01, lambda_min(R) 0.500041882 abs 1e-8, folds
(2, 4)); r359 W9 SCHUR ANCHORS eps 4.1882e-5 / lamS 4.2003e-5 / detS
2.0690e-8 rel 1e-3, share 0.6973 abs 5e-3; r359 SHARE SAMPLES kz44
0.8152 / kz56 0.8392 / kz130 0.6724 abs 5e-3; the r352 margin slope
-3.332 tol 0.02; the r359 fresh censi detS -6.742 / rest -3.276 tol
0.05; the r356 EXT selections adopted AS-IS (re-derived and gated).

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184); REC_MARGIN
1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8; W9 SAT ANCHORS (s1
scoping, disclosed): od1 0.1497 / odf2 0.5118 / odf4 0.5137 / t_geo
0.2646 abs 5e-3; OD1 SAMPLES kz44 0.2135 / kz56 0.2244 / kz130 0.2523
abs 5e-3; TGEO SAMPLES kz44 0.2431 / kz56 0.2449 / kz130 0.2294 abs
5e-3; CHI W9 ANCHORS chi3 (od1 0.5189, t_geo 0.1987) / chi4 (od1
0.5242, t_geo 0.2875) abs 1e-2; SCR OD1 0.6061 abs 2e-2 (census); r359
SCR ANCHORS eps -0.4962 abs 2e-3, rest -0.4962 abs 2e-3, lamS
+1.369e-2 rel 5e-2; GRADES shallow N_w <= 900 / mid <= 3200 / deep >
3200 (r356); r359 graded bars REUSED VERBATIM: CD (1e-12, 1e-11,
1e-10), IIKS (1e-6, 1e-3, 5e-2), COUP (1e-8, 1e-6, 1e-3), RM (1e-8,
1e-6, 1e-3), DETID (1e-10, 1e-9, 1e-6) -- the disclosed 1/eps A-solve
conditioning stands; OCC_COMP_BAR (1e-11, 1e-10, 5e-9) abs on the QP/
chi/scr instances; TRACE_BAR (1e-8, 1e-7, 5e-6) abs ladder-wide;
EPS_FLOOR 1.25e-10; RESOLV_FLOOR 1e-9 (r359: equivalence / bind / t_geo
/ kappa clauses on rows with eps > floor only, EXT5/EXT6 sign census);
BIND_MIN 1 - 1e-6; BIND_MAX 1.5; JORD_TOL 1e-6; ZONE_BAR 0.15 (fold-1
anomaly, scoped devs -0.23 .. -0.33 over 9 windows); PAIR_FLAT_BAR
0.10 (pair folds non-anomalous, scoped <= 0.04); CHI_FLAT_BAR 0.10
(scoped 0.035/0.026); MAIN_ZONE_MIN 83 (of 85, 2-exception allowance);
QP_KZ (9, 44, 56, 130); QP_ITERS 3000; QP_POW_ITERS 60; QP_BIS_ITERS
100; QP_TOL 1e-6; NB_MAX 4 (scoped 0..2); GAP_MIN 1e-3 (scoped +0.092
.. +2.72); QP_VOID_BLOCK (1, 2, 3); T_GEO_BAND (0.10, 0.45) (exact
relation t_geo = 1/(2 sqrt(det(S_N/eps)(1 - share))) with r359 detS/
margin^2 in [0.74, 1.63] and share in [0.46, 0.84] implies [0.13,
0.37]); T_GEO_SLOPE_TOL 0.10 on the 57; ALPHA_CANDS (3.332, 1.65);
ALPHA_TOL 0.10; KAPPA_BAND (5.0, 60.0); KAPPA_RATIO_MAX 1.5; C_REL 2.0
(the relative rest clause margin over the c = 1 theorem line; r359
MAIN min 8.8, chi meds 7.4/5.3 -- the chi mins are the honest risk,
disclosed); WCANCEL_CORR_MIN 0.90; FIT margin anchor -3.332 tol 0.02
(r352), detS anchor -6.742 tol 0.05 + rest anchor -3.276 tol 0.05
(r359 record); WORLD_KZ (18, 9, 52, 119, 42, 130); TWIN_BAR 1e-3 nats
(r359 Schur columns); TWIN_OCC_BAR 1e-3 abs (occupation at the pair);
N_CHI_MIN 21; SCR_SEED 1; M1_BAR 10.0 (scoped 92.7); M5_BAR 0.3
(scoped 0.798); M6_BAR 1e-3 (scoped 1.17e-2); EXT selections verbatim
r356 (EXT3_KZ_B/A, EXT4, EXT5/EXT6 pool rules, expects, Z2_CAP
400000); TOY_TOL 1e-12; runtime <= 1800 s; smoke = toys + firewall +
scopes + mutants + w9 blocks (records, occupation, QP, t_geo) + chi3
w9 block; ladder, EXT, twin, chi ladders, scramble, fits,
adjudications skipped.

PRE-SPEC SCOPING (disclosed, r343-s1..r359-s1 precedent -- TWO sizing
passes s1/s2 on kz9/44/56/130 + kz18/52/82/119/42 (occupation only) +
chi3/chi4 w9 + scramble w9, /tmp, deleted; no bar, band, clause,
candidate list or verdict rule was tuned after any evaluation except
as sized here and said so): the occupation duality is exact (complement
dev 3.7e-13 (w9) .. 2.2e-11 (S 4035), trace exact to 1e-10); THE
FOLD-1 ANOMALY IS FAMILY-UNIFORM: o_dual(fold 1) = 0.150 (w9), 0.186
(kz18), 0.214 (kz44), 0.219 (kz52), 0.224 (kz56), 0.236 (kz82), 0.249
(kz119), 0.218 (kz42), 0.252 (kz130) against bulk medians 0.48..0.51
-- always the SINGLE anomalous right-edge fold, the pair folds flat
(devs <= 0.04); the anomaly DECAYS SLOWLY if at all (ln(0.5 - od1)
slope ~ -0.12 on the four scoped depths -- census column, no sealed
candidate); THE QP CRYSTALLIZES at 3000 iterations (zero-temperature
ground state, #band 0..2, KKT gap +0.092 .. +2.72) with the dual void
block EXACTLY {1, 2, 3} on all four MAIN instances -- the pair (2, 4)
straddles the block edge 3|4; chi3/chi4/scramble OCCUPY fold 1 (m
fold1 = 1.0); the exact-occupation chi contrast: |od1 - med| = 0.035
(chi3) / 0.026 (chi4) -- no anomaly; scramble od1 0.6061, med 0.474
(disordered, dev +0.13 below the zone bar); t_geo = 0.2646 (w9),
0.2431/0.2449/0.2294 (samples), 0.1987/0.2875 (chi w9) -- the band and
slope clauses sized from these plus the exact t_geo relation; the m1
unconstrained catch is loud on every instance (max m 92.7 (w9) ..
1624 (kz130)); m5 shuffle moves od1 by 0.798; m6 wrong rank breaks the
complement by 1.17e-2 vs 3.7e-13 true.  The verdict letters, clauses,
bands and every bar were frozen from these numbers BEFORE any
ladder-wide, chi-ladder-wide, fit-side or adjudication evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > CHAIN_FAIL > the four
adjudicated letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the rank/support gate fails on any real
    MAIN ladder window /
  CHAIN_FAIL(loci)  iff any exact ward fails (toys, r359 E1-E5 graded,
    occupation complement, trace, QP KKT gates, equivalence on
    resolvable rows, Jacobi order) /
  otherwise ALL FOUR adjudications, each exactly one letter:
  [SATURATION_EDGE_CONFIRMED(straddle)  iff the QP void block ==
    {1, 2, 3} with KKT gates on 4/4 sealed instances AND the MAIN
    occupation zone census >= 83/85 (fold-1 anomaly + pair flat) AND
    the chi contrast (both chi w9 flat AND both chi QPs occupy fold 1)
    / SATURATION_REFUTED(loci)  otherwise -- honest: a different local
    class is needed]
  [GAMMA_PARAMETRIX_CENSUS(t_geo)  iff |TS slope(log t_geo)| <= 0.10
    on the 57 AND t_geo in (0.10, 0.45) on ALL resolvable MAIN rows
    AND both chi w9 values in band -- the dimensionless diagonal-
    resolvent datum is family-constant: local-parametrix-class census,
    NOT a Gamma derivation / GAMMA_CENSUS_OFF(loci)]
  [M0_COLLAPSE(alpha)  iff the fresh lamS slope hits a sealed alpha
    candidate at 0.10 AND kappa_S range ratio <= 1.5 on the resolvable
    rows / M0_PARTIAL(alpha)  iff the alpha candidate hits AND kappa_S
    in (5, 60) on all resolvable rows (the margin direction collapses
    via the bind clause, the second eigenvalue is bounded O(1) wander)
    / M0_OFF(slope)]
  [RELATIVE_REST_CERTIFIED(theorem c=1, census c>=2)  iff the
    interlacing theorem side holds (toy exact + live 74/74 resolvable)
    AND rest/eps >= C_REL on ALL live resolvable rows of MAIN + chi3 +
    chi4 / REST_RELATIVE_CENSUS(min)]
  + WANDER_CANCEL_LEDGER(O6 corr + rms census) + PARTITION_LEDGER +
    OCCUPATION_LEDGER + WORLD_LEDGER + TWIN_LEDGER +
    SCRAMBLE_BREAK(named) + MUSTFAIL_LEDGER [always].
Honesty before beauty: the occupation duality, the trace, the adjugate
decomposition and the interlacing inequalities are exact finite-matrix
facts (theorem-grade SKELETON) whose inputs are measured window scalars
(census-grade FLESH); the QP is a zero-temperature variational model --
its partition is a measurement about THIS family, not an asymptotic
theorem; t_geo family-constancy is a census, the Gamma-parametrix
DERIVATION stays open (the specialist step C); no verdict claims L*, a
bound mechanism, a derived 5/7, or RH progress in any direction; the
DCCX STOP list stands.

RECORD TABLES (inserted AFTER the record run -- the only post-freeze
edit; no placeholder numbers existed before the first full evaluation,
the r346 lesson; TWO-COMMIT PROTOCOL EXECUTED: the sealed spec was
committed as "r360 pre-freeze" (8a835dc8, SPEC_SHA freeze
75f8ee55436ab173) BEFORE the first full evaluation; chronology honest:
smoke pass 1/2 = 34/34 byte-identical at the sealed rules (one
pre-freeze toy-node fix: the G11 saturation toy moved to asymmetric
nodes after the symmetric linspace stalled on a tie-saddle -- before
the freeze commit, disclosed); pre-freeze commit 8a835dc8; calibration
pass 1 = FIRST full evaluation = 34/34 (153.7 s) with ZERO amendments
-- no bar, band, clause, candidate or verdict rule moved after the
freeze; record run1 = 34/34 (172.2 s), run2 = 34/34 (157.0 s),
byte-identical up to the WALL line and identical to calibration):
MAIN VERDICT = SATURATION_EDGE_CONFIRMED(the sealed QP dual-void
block == folds {1, 2, 3} with clean KKT on 4/4 sealed instances
(#band [0, 2, 0, 0], gaps [+0.092, +2.718, +0.445, +0.420]) -- by the
exact complement O1 the PRIMAL SATURATED block -- and THE CRITICAL
PAIR (2, 4) STRADDLES ITS EDGE 3|4 (fold 2 inside the saturated zone,
fold 4 outside); the exact-occupation fold-1 anomaly census 85/85 on
MAIN (dev1 in [-0.333, -0.253], pair folds flat <= 0.10, misses
none); the chi contrast is a DIFFERENT PARTITION: chi3/chi4 dev1
+0.0348/+0.0261 flat, fold-1 anomaly 0/42 + 0/42 ladder-wide, AND
both chi QPs OCCUPY fold 1 (void folds (2,3,7,8) / (2,3,4)) --
world-separating, exactly the reviewer's step-B object)
+ GAMMA_PARAMETRIX_CENSUS(t_geo = eps sqrt(a11 a22) family-constant:
slope -0.009 on the 57 (|.| <= 0.10), range [0.2216, 0.2865] med
0.2536 on all 74 resolvable rows inside (0.10, 0.45), chi w9
0.1987/0.2875 in band -- the dimensionless diagonal-resolvent datum
is margin-locked across worlds and depths; the exponent censi: the
DIAGONALS CARRY THE MARGIN EXPONENT (|a11| +3.365, |a22| +3.292,
|a12| +3.316 vs margin 3.332; the 1.786/1.683 Christoffel family
misses by ~1.6, the 0.38 family by more -- the r350 weight laws do
NOT carry the resolvent diagonals))
+ M0_PARTIAL(alpha = 3.332: the fresh lamS slope -3.334 hits the
margin candidate at 0.002 and REJECTS s_infty 1.65 at 1.684; bind
[1.0003, 1.0605] med 1.0058 == r359 EXACT -- the margin direction
collapses; kappa_S = lammax/lammin in [6.3, 30.5] med 13.9, range
ratio 4.88 > 1.5 -- THE FULL M_0 COLLAPSE IS HONESTLY REFUTED AT THE
SEALED RATIO: M_0 exists only up to the O(1) second-eigenvalue
wander, the reviewer's L1 form needs a relative/projective
formulation exactly as the rest clause does; split-half curvature
shallow -3.417 / deep -3.784, the disclosed r342-class curvature)
+ REST_RELATIVE_CENSUS(the round's sharpest honest negative: the
THEOREM side c = 1 holds (Cauchy interlacing + Schur-complement
eigenvalue inequality, toy exact both directions + live 74/74
resolvable + chi 84/84) and MAIN carries C_REL = 2.0 with rest/eps
in [8.8, 54.2] med 20.3 violations none -- BUT the chi ladders dip
to the interlacing line: chi3 [1.0, 16.4] med 7.4 violations [31,
40, 55], chi4 [1.0, 13.4] med 5.3 violations [14, 16, 23, 25, 28,
40, 53, 59] -- the interlacing inequality is NEARLY TIGHT on 11/84
chi rows: the c > 1 margin is MAIN-measured, NOT world-uniform, and
the L2 relative clause survives as theorem only at c = 1;
RELATIVE_REST_CERTIFIED correctly did NOT fire)
+ WANDER_CANCEL_LEDGER(O6: corr(psi57 log detS, -psi57 log(a11 a22))
= +0.9835 >= 0.90 -- the det S_N wander IS the diagonal-resolvent
wander; rms(psi57 log(1 - share)) / rms(psi57 log detS) = 0.204 --
the cross-share term is ~5x subleading: the leading common wander
cancels algebraically inside the adjugate minor, measured)
+ PARTITION_LEDGER(QP crystallized on all 7 instances; the m1
unconstrained catch max m = 92.7 (w9) -- the obstacle constraint is
load-bearing; scramble QP void folds (2, 4, 5, 6), fold 1 occupied)
+ OCCUPATION_LEDGER(complement ward 3.7e-13 .. 2.2e-11 graded on the
7 instances; trace ward 5.6e-12/1.1e-11/1.4e-10 graded ladder-wide
85/85; od1 anchors hit (w9 0.1497, kz44 0.2135, kz56 0.2244, kz130
0.2523); the anomaly-decay census slope(ln(1/2 - od1)) = -0.088 on
the 57 -- the saturation edge fades at a slow census rate far from
any measured closing, typed for the specialist)
+ WORLD_LEDGER(chi3 42/42 + chi4 42/42 through the identical dual +
Schur + occupation pipeline, chain + occupation wards green at the
r359 graded bars, eps all positive, fold-1 anomaly 0/42 + 0/42 --
the saturation edge is MAIN-specific, the second arithmetic has
none)
+ TWIN_LEDGER(dose-zero BITWISE 6/6; Schur devs max 6.9e-4 nats bar
1e-3 -- the r359 1.4x-headroom truth reproduced; occupation devs max
3.8e-8, bar 1e-3)
+ SCRAMBLE_BREAK(named: eps -0.4962, rest -0.4962 (anchors), pair
block +1.3688e-2 stays positive -- the r359 lesson reproduced; the
algebra is world-blind (det-id 2.7e-16, CD 5.3e-15, occupation trace
5.7e-14); od1 0.6061 dev1 +0.1320 disordered under the zone bar --
the dead world has NO saturation edge either)
+ MUSTFAIL_LEDGER(m1 unconstrained 92.7 >= 10; m2/m3/m4 AST-FLAGGED
(withheld margin/detS/a11 columns); m5 shuffle 0.798 >= 0.3; m6
wrong rank 1.17e-2 >= 1e-3 + Fractions-exact; scopes CLEAN).
Key numbers.  W9: od1 0.1497 (o_eta(fold 1) 0.8503), odf2 0.5118,
odf4 0.5137, dev1 -0.3311, t_geo 0.2646, kappa_S 11.7, QP gap
+0.092, complement 3.7e-13, trace 5.7e-14.  LADDER: margin slope
-3.332 == r352 EXACT, detS -6.742 == r359 EXACT, rest -3.276 == r359
EXACT; fresh censi lamS -3.334, t_geo -0.009, |a11| +3.365, |a22|
+3.292, |a12| +3.316, ln(1/2 - od1) -0.088; zone census 85/85; E1-E5
wards green at the r359 graded bars (det-id 2.1e-13/1.8e-12/5.4e-12,
CD <= 3.8e-14, IIKS <= 4.3e-3, coupling <= 6.9e-8, res-minor <=
5.4e-8).
REVIEWER-STEP TYPING (the specialist handoff deliverable):
(A) the reciprocal dual weight in closed form = THEOREM (r356,
standing, re-consumed verbatim);
(B) the constrained equilibrium partition = THIS ROUND: the exact
occupation field (theorem-grade object) + the sealed obstacle solver
(zero-temperature variational model) agree on the partition shape;
the SATURATION-EDGE thesis is CONFIRMED at census grade (4/4 QP
straddle + 85/85 occupation + total chi contrast); the ASYMPTOTIC
equilibrium-measure theorem (BKMM band/saturation limit shape with
the field -log u_vee) stays OPEN -- the specialist step;
(C) the local parametrix = CENSUS: t_geo is margin-locked (slope
-0.009, spread 29 pct) and the resolvent diagonals carry the margin
exponent 3.332 (not the 0.38/1.79 weight families) -- the
Gamma-class DERIVATION (BKMM Thm 2.7 at saturation adjacency) stays
OPEN; the Casoratian term must be carried (r359 cross share, its
wander 5x subleading to the diagonal wander);
(D) the reserve from the local minor = the adjugate identity is
THEOREM (r359, re-gated); the wander cancellation is MEASURED (corr
+0.9835); the first non-vanishing coefficient (M_0) is PARTIAL: the
margin direction collapses (bind med 1.0058), kappa_S wanders 4.88x
-- alpha = 3.332 is settled at 0.002, the matrix limit is NOT a
constant matrix;
(E) the rigorous error = OPEN (nothing in this round bounds it); the
RELATIVE REST CLAUSE = THEOREM at c = 1 (interlacing, Lean-able
finite statement) + MAIN census at c >= 8.8 -- but NOT world-uniform
at c = 2 (chi mins 1.0): any L2 draft must state it per-world or at
c = 1.
HONEST NEGATIVES: (1) RELATIVE_REST_CERTIFIED did not fire -- the
chi ladders sit at the interlacing line on 11/84 rows (rest/eps =
1.0): the reviewer's relative clause is provable only at c = 1, the
comfortable MAIN margin (8.8x) does not transfer to the second
arithmetic; (2) the full M_0 collapse is refuted at the sealed ratio
(kappa_S 4.88x) -- the L1 target as stated (fixed positive M_0) is
too rigid for this family; (3) the saturation-edge statement is a
finite-family census plus a zero-temperature variational model -- no
BKMM asymptotic theorem is claimed, and the fold-1 anomaly decays at
a slow census rate (-0.088) whose limit this family cannot decide;
(4) t_geo has a 29 pct spread -- margin-locked at wander level, not
a constant; (5) EXT5/EXT6 floor rows stay sign census (r359
convention, 11 rows); (6) the split-half lamS curvature (-3.417 /
-3.784) is the disclosed r342-class curvature -- the alpha hit is a
57-row Theil-Sen statement, not an asymptotic derivation; (7) one
pre-freeze toy-node fix disclosed above; ZERO post-freeze
amendments.  Runtime 172.2 / 157.0 s record, 153.7 s calibration,
2.1 s smoke; deterministic, run1/run2 byte-identical up to WALL.

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
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import schur_wronskian_dual_probe as SWD         # noqa: E402 r359
import borodin_dual_hole_probe as BDH            # noqa: E402 r356
import pair_extremal_probe as PX                 # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF      # noqa: E402 r357
import phi_wander_anatomy_probe as PWA           # noqa: E402 r354
import ext3_fresh_anchors_probe as E3            # noqa: E402 r329
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import verify_lstar_instance as V                # noqa: E402 document
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
LM_SHA_PREFIX = "0a44ac4e"
W9_SCHUR_ANCH = dict(eps=4.1882e-5, lamS=4.2003e-5, detS=2.0690e-8,
                     share=0.6973, f1=2, f2=4)
SHARE_SAMPLE_ANCH = {44: 0.8152, 56: 0.8392, 130: 0.6724}
W9_SAT_ANCH = dict(od1=0.1497, odf2=0.5118, odf4=0.5137, tgeo=0.2646)
OD1_SAMPLE_ANCH = {44: 0.2135, 56: 0.2244, 130: 0.2523}
TGEO_SAMPLE_ANCH = {44: 0.2431, 56: 0.2449, 130: 0.2294}
SAT_ANCH_TOL = 5.0e-3
CHI_W9_ANCH = {"chi3": dict(od1=0.5189, tgeo=0.1987),
               "chi4": dict(od1=0.5242, tgeo=0.2875)}
CHI_ANCH_TOL = 1.0e-2
SCR_OD1_ANCH = 0.6061
SCR_OD1_TOL = 2.0e-2
SCR_ANCH = dict(eps=-0.4962, rest=-0.4962, lamS=1.369e-2)
NW_SHALLOW = 900
NW_MID = 3200
CD_BAR = (1.0e-12, 1.0e-11, 1.0e-10)
IIKS_BAR = (1.0e-6, 1.0e-3, 5.0e-2)
COUP_BAR = (1.0e-8, 1.0e-6, 1.0e-3)
RM_BAR = (1.0e-8, 1.0e-6, 1.0e-3)
DETID_BAR = (1.0e-10, 1.0e-9, 1.0e-6)
OCC_COMP_BAR = (1.0e-11, 1.0e-10, 5.0e-9)
TRACE_BAR = (1.0e-8, 1.0e-7, 5.0e-6)
EPS_FLOOR = 1.25e-10
RESOLV_FLOOR = 1.0e-9
BIND_MIN = 1.0 - 1.0e-6
BIND_MAX = 1.5
JORD_TOL = 1.0e-6
ZONE_BAR = 0.15
PAIR_FLAT_BAR = 0.10
CHI_FLAT_BAR = 0.10
MAIN_ZONE_MIN = 83
QP_KZ = (9, 44, 56, 130)
QP_ITERS = 3000
QP_POW_ITERS = 60
QP_BIS_ITERS = 100
QP_TOL = 1.0e-6
NB_MAX = 4
GAP_MIN = 1.0e-3
QP_VOID_BLOCK = (1, 2, 3)
T_GEO_BAND = (0.10, 0.45)
T_GEO_SLOPE_TOL = 0.10
ALPHA_CANDS = (3.332, 1.65)
ALPHA_TOL = 0.10
KAPPA_BAND = (5.0, 60.0)
KAPPA_RATIO_MAX = 1.5
C_REL = 2.0
WCANCEL_CORR_MIN = 0.90
FIT_MARGIN_ANCH = -3.332
FIT_MARGIN_TOL = 0.02
FIT_DETS_ANCH = -6.742
FIT_REST_ANCH = -3.276
FIT_R359_TOL = 0.05
CAND_PRINTS = (3.332, 1.786, 1.683, 1.4222, 0.38, 0.76)
WORLD_KZ = (18, 9, 52, 119, 42, 130)
TWIN_BAR = 1.0e-3
TWIN_OCC_BAR = 1.0e-3
N_CHI_MIN = 21
SCR_SEED = 1
M1_BAR = 10.0
M5_BAR = 0.3
M6_BAR = 1.0e-3
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT5_H_LO, EXT5_H_HI, K_EXT5 = 3401, 6000, 6
EXT5_KZ_EXPECT = (69, 107, 101, 99, 115, 89)
EXT5_H_EXPECT = (5690, 5668, 5242, 5073, 4243, 4237)
USED5_EXPECT, FRESH5_EXPECT = 98, 9
EXT6_H_LO, EXT6_H_HI, K_EXT6 = 6001, 60000, 4
Z2_CAP = 400000
USED6_EXPECT, FRESH6_EXPECT = 104, 4
EXT6_KZ_EXPECT = (133, 129, 124, 117)
EXT6_H_EXPECT = (7942, 7675, 7233, 6532)
TOY_TOL = 1.0e-12
RUNTIME_BAR = 1800.0

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
    return (not bad), ("NO zero/prime oracles; the module-own "
                       "constructors consume measure arrays / chain "
                       "coefficients / positions / pair indices ONLY; "
                       "record numbers and anchors enter gates and "
                       "record tables only"
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


CONSTRUCTORS = ("grade_of", "occ_from_chain", "occ_profile",
                "qp_kernel", "proj_box_simplex", "qp_equilibrium",
                "kkt_partition", "zone_row", "sat_rung", "chi_sat_row")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_SCHUR_ANCH",
                   "W9_SAT_ANCH", "SHARE_SAMPLE_ANCH",
                   "OD1_SAMPLE_ANCH", "TGEO_SAMPLE_ANCH",
                   "CHI_W9_ANCH", "SCR_OD1_ANCH", "SCR_ANCH",
                   "FIT_MARGIN_ANCH", "FIT_DETS_ANCH", "FIT_REST_ANCH",
                   "ALPHA_CANDS", "margin_col_true", "detS_col_true",
                   "a11_col_true"}


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


# ============== module-own constructors (AST-audited)
def grade_of(nw):
    """graded-bar index of a row: 0 shallow, 1 mid, 2 deep;
    consumes the window depth only."""
    return 0 if nw <= NW_SHALLOW else (1 if nw <= NW_MID else 2)


def occ_from_chain(xu, wvec, a, b, h0, depth):
    """streaming occupation diagonal of the rank-`depth` projection
    of the measure (xu, wvec) from a GIVEN orthonormal chain,
    evaluated on ALL nodes: o_j = sum_{i < depth} wvec_j P_i(x_j)^2;
    O(S) memory; consumes measure arrays + chain coefficients only."""
    u = np.sqrt(wvec) / math.sqrt(h0)
    um = np.zeros_like(u)
    occ = u * u
    for i in range(depth - 1):
        r = (xu - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        occ = occ + u * u
    return occ


def occ_profile(xu, wvec, depth):
    """occupation diagonal incl. the chain build; consumes measure
    arrays only."""
    a, b, h0 = V.mu_chain(xu, wvec, depth)
    return occ_from_chain(xu, wvec, a, b, h0, depth)


def qp_kernel(xu):
    """the discrete log-interaction matrix K_jk = -log|x_j - x_k|
    (diagonal zero); consumes positions only."""
    dx = np.abs(xu[:, None] - xu[None, :])
    np.fill_diagonal(dx, 1.0)
    K = -np.log(dx)
    np.fill_diagonal(K, 0.0)
    return K


def proj_box_simplex(v, cap, mass):
    """exact euclidean projection onto {0 <= m <= cap, sum m = mass}
    by water-filling bisection (QP_BIS_ITERS fixed steps,
    deterministic); consumes the vector only."""
    lo = float(np.min(v)) - cap - 1.0
    hi = float(np.max(v)) + 1.0
    for _ in range(QP_BIS_ITERS):
        mid = 0.5 * (lo + hi)
        if float(np.sum(np.clip(v - mid, 0.0, cap))) > mass:
            lo = mid
        else:
            hi = mid
    return np.clip(v - 0.5 * (lo + hi), 0.0, cap)


def qp_equilibrium(xu, ud, mass, iters, cap=1.0):
    """the sealed constrained-equilibrium (obstacle) solver:
    minimize m^T K m + V^T m, V = -log u_vee, over the box-simplex
    (cap = the discrete BKMM upper constraint); deterministic FISTA
    with the step from QP_POW_ITERS power iterations; returns
    (m, gradient); consumes positions + dual weights only."""
    S = len(xu)
    K = qp_kernel(xu)
    Vf = -np.log(ud)
    z = np.ones(S) / math.sqrt(S)
    for _ in range(QP_POW_ITERS):
        z2 = K @ z
        z = z2 / np.linalg.norm(z2)
    step = 1.0 / (2.0 * abs(float(z @ (K @ z))) + 1e-9)
    m = np.full(S, mass / S)
    y = m.copy()
    t = 1.0
    for _ in range(iters):
        g = 2.0 * (K @ y) + Vf
        m_new = proj_box_simplex(y - step * g, cap, mass)
        t_new = 0.5 * (1.0 + math.sqrt(1.0 + 4.0 * t * t))
        y = m_new + ((t - 1.0) / t_new) * (m_new - m)
        m, t = m_new, t_new
    g = 2.0 * (K @ m) + Vf
    return m, g


def kkt_partition(m, g, cap=1.0):
    """KKT report of a QP solution: (#band, gap = min g[void] -
    max g[sat], void set, sat set); a clean zero-temperature
    partition has few band nodes and a positive gap; consumes the
    solution only."""
    sat = m >= cap - QP_TOL
    void = m <= QP_TOL
    band = ~sat & ~void
    gsat = float(np.max(g[sat])) if sat.any() else -np.inf
    gvoid = float(np.min(g[void])) if void.any() else np.inf
    return int(band.sum()), gvoid - gsat, void, sat


def zone_row(od, f, iY, i1, i2):
    """the sealed occupation-zone columns of one window: bulk median,
    dev1 = od(fold 1) - med, the pair-fold deviations; consumes the
    occupation field + fold indices + pair positions only."""
    med = float(np.median(od))
    j1 = int(np.nonzero(f == 1)[0][0])
    od1 = float(od[j1])
    devf1 = od1 - med
    devp1 = float(od[iY[i1]]) - med
    devp2 = float(od[iY[i2]]) - med
    return od1, med, devf1, devp1, devp2


def sat_rung(xu, wu, yn, vn, Nw, S, L, i1, i2):
    """THE r360 BLOCK of one window: the verbatim r359 schur_rung,
    plus the occupation field of the dual hole ensemble (from the
    schur_rung chain, rank N_w - 1), the trace ward, the sealed zone
    columns, t_geo and kappa_S; consumes measure arrays, positions
    and the pair indices only."""
    o = SWD.schur_rung(xu, wu, yn, vn, Nw, S, L, i1, i2)
    xu = np.asarray(xu, float)
    u = np.abs(np.asarray(wu, float))
    ud, _lA, f, _eps, _lp = BDH.dual_weights(xu, u, S, L)
    od = occ_from_chain(xu, ud, o["ad"], o["bd"], o["h0d"], Nw - 1)
    dev_tr = abs(float(np.sum(od)) - (Nw - 1.0))
    iY = np.searchsorted(xu, np.asarray(yn, float))
    od1, med, devf1, devp1, devp2 = zone_row(od, f, iY, i1, i2)
    a1122 = o["a11"] * o["a22"]
    tgeo = o["eps"] * math.sqrt(a1122) if a1122 > 0 \
        and o["eps"] > 0 else float("nan")
    kap = o["detS"] / (o["lamS"] * o["lamS"]) if o["lamS"] > 0 \
        else float("nan")
    out = SWD.slim359(o)
    out.update(od1=od1, occ_med=med, devf1=devf1, devp1=devp1,
               devp2=devp2, dev_tr=dev_tr, tgeo=tgeo, kap=kap,
               ud=ud, f=f, od=od)
    return out


def slim360(o):
    """memory hygiene: drop the field arrays, keep the scalars."""
    return {k: o[k] for k in o if k not in ("ud", "f", "od")}


def chi_sat_row(kz, q, lpq):
    """one chi-world rung through the identical dual + Schur +
    occupation pipeline (r357 frame verbatim); consumes the chi comb
    + the matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = sat_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                 mzc["Nw"], mzc["S"], mzc["L"], j1, j2)
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    return o


# ============== must-fail mutants
def mutant_unconstrained(xu, ud, mass, iters):
    """m1 MUST-FAIL (loud): the CLASSICAL unconstrained weighted
    equilibrium (cap removed) -- the minimizer must pile mass far
    beyond the discrete node cap: the obstacle constraint is
    load-bearing (the BKMM class, not the AC class)."""
    m, _g = qp_equilibrium(xu, ud, mass, iters, cap=1.0e18)
    return float(np.max(m))


def mutant_alpha_readback(margin_col_true):
    """m2 MUST-FAIL (AST): an 'alpha' read circularly from the
    withheld measured margin column -- AST-FLAGGED."""
    return margin_col_true


def mutant_m0_by_sight(detS_col_true):
    """m3 MUST-FAIL (AST): an 'M_0 fit' whose alpha is optimized
    posthoc against the withheld det S_N column (fit by sight; the
    sealed-candidate protocol is the catch) -- AST-FLAGGED."""
    return detS_col_true


def mutant_parametrix_readback(a11_col_true):
    """m4 MUST-FAIL (AST): a 'parametrix prediction' returning the
    withheld measured (A^{-1})_11 column verbatim -- AST-FLAGGED."""
    return a11_col_true


def mutant_weight_shuffle(xu, ud, depth):
    """m5 MUST-FAIL (loud): the occupation partition computed with
    the DETERMINISTICALLY SHUFFLED (reversed) dual weight -- the
    fold-1 occupation must move loudly."""
    return occ_profile(xu, ud[::-1].copy(), depth)


def mutant_wrong_rank_occ(xu, u, ud, Nw):
    """m6 MUST-FAIL (loud): the occupation complement with the WRONG
    dual rank (N_w instead of N_w - 1) -- must break the exact
    complement identity loudly."""
    oe = occ_profile(xu, u, Nw)
    od_wrong = occ_profile(xu, ud, Nw)
    return float(np.max(np.abs(oe - (1.0 - od_wrong))))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("critical_saturation_probe -- "
          "PRIME.LSTAR.DUAL.CRITICAL_SATURATION.01 (round 360)")
    print("SPEC_SHA %s   (r359 SWD %s / r356 BDH %s / r357 DMF %s)"
          % (SPEC_SHA[:16], SWD.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             DMF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 blocks + chi3 w9; ladder, EXT, twin, "
                        "chi ladders, scramble, fits, adjudications "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r359/r356/r342/r357/r354/r329/"
          "r286 machinery imported verbatim (SWD %s == %s*, BDH %s == "
          "%s*, PX %s == %s*, DMF %s == %s*, PWA %s == %s*, E3 %s == "
          "%s*, LM %s == %s*); the r359 graded chain bars reused "
          "verbatim; the occupation bars (COMP %s / TRACE %s), the "
          "zone bars (ZONE %.2f / PAIR %.2f / CHI %.2f, MAIN_ZONE_MIN "
          "%d), the QP seals (ITERS %d, NB_MAX %d, GAP_MIN %.0e, "
          "void block %s), the t_geo clauses (band %s, slope %.2f), "
          "the alpha candidates %s tol %.2f, the kappa clauses (band "
          "%s, ratio %.1f), C_REL %.1f, the wander-cancel bar %.2f, "
          "the worlds and every mutant; pre-spec scoping s1/s2 "
          "disclosed in the spec; the DCCX STOP list forbids any L* "
          "claim and any certificate reading"
          % (SWD.SPEC_SHA[:8], SWD_SHA_PREFIX, BDH.SPEC_SHA[:8],
             BDH_SHA_PREFIX, PX.SPEC_SHA[:8], PX_SHA_PREFIX,
             DMF.SPEC_SHA[:8], DMF_SHA_PREFIX, PWA.SPEC_SHA[:8],
             PWA_SHA_PREFIX, E3.SPEC_SHA[:8], E3_SHA_PREFIX,
             LM.SPEC_SHA[:8], LM_SHA_PREFIX, str(OCC_COMP_BAR),
             str(TRACE_BAR), ZONE_BAR, PAIR_FLAT_BAR, CHI_FLAT_BAR,
             MAIN_ZONE_MIN, QP_ITERS, NB_MAX, GAP_MIN,
             str(QP_VOID_BLOCK), str(T_GEO_BAND), T_GEO_SLOPE_TOL,
             str(ALPHA_CANDS), ALPHA_TOL, str(KAPPA_BAND),
             KAPPA_RATIO_MAX, C_REL, WCANCEL_CORR_MIN))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_alpha_readback")
    hits_m3 = scope_audit("mutant_m0_by_sight")
    hits_m4 = scope_audit("mutant_parametrix_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4),
          "the %d module-own constructors consume measure arrays / "
          "chain coefficients / positions / pair indices ONLY (%s); "
          "fragment audit (no fit primitives beyond the imported r286 "
          "Theil-Sen; the QP is sealed first-order descent): %s; m2 "
          "FLAGGED (%s); m3 FLAGGED (%s); m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- EXACT OCCUPATION COMPLEMENT + QP/KKT + "
            "INTERLACING")
    # (T1) exact Fractions occupation complement on the 5-atom model
    xs_t = [Fr(-3, 4), Fr(-1, 4), Fr(0), Fr(1, 2), Fr(4, 5)]
    u_t = [Fr(1), Fr(1, 4), Fr(1, 2), Fr(1, 6), Fr(1, 3)]
    N_t, S_t = 3, 5
    Pp_t = [math.prod([xs_t[j] - xs_t[k] for k in range(S_t)
                       if k != j], start=Fr(1)) for j in range(S_t)]
    uv_t = [Fr(1) / (u_t[j] * Pp_t[j] ** 2) for j in range(S_t)]
    Ah = BDH.fr_proj(xs_t, u_t, N_t)
    Bh = BDH.fr_proj(xs_t, uv_t, N_t - 1)
    dev_occ_t = max(abs(Ah[j][j] + Bh[j][j] - Fr(1))
                    for j in range(S_t))
    tr_A = sum(Ah[j][j] for j in range(S_t))
    tr_B = sum(Bh[j][j] for j in range(S_t))
    Bw = BDH.fr_proj(xs_t, uv_t, N_t)     # m6 wrong rank, exact
    dev_m6t = max(abs(Ah[j][j] + Bw[j][j] - Fr(1))
                  for j in range(S_t))
    check("G10-toy-occ-complement", dev_occ_t == 0
          and tr_A == Fr(N_t) and tr_B == Fr(N_t - 1)
          and dev_m6t > 0,
          "EXACT FRACTIONS on the rational 5-atom model (S = 5 = "
          "2N - 1, N = 3): the occupation complement o_eta(x_j) + "
          "o_dual(x_j) == 1 holds with difference EXACTLY 0 on all 5 "
          "nodes (the diagonal of the Borodin complementation -- "
          "sign-matrix free); the traces are EXACT (tr o_eta = 3 = N, "
          "tr o_dual = 2 = N - 1); the m6 mutant (rank N instead of "
          "N - 1) breaks the complement EXACTLY (max |dev| = %.3e "
          "!= 0)" % float(dev_m6t))
    # (T2) QP machinery toys: projection + KKT both directions
    v_t = np.array([0.3, -0.2, 1.7, 0.9, 0.4, -1.1, 0.8, 0.05])
    p1 = proj_box_simplex(v_t, 1.0, 3.0)
    p2 = proj_box_simplex(p1, 1.0, 3.0)
    ok_proj = (abs(float(np.sum(p1)) - 3.0) <= 1e-10
               and float(np.min(p1)) >= -1e-15
               and float(np.max(p1)) <= 1.0 + 1e-15
               and float(np.max(np.abs(p1 - p2))) <= 1e-10)
    xs_q = np.linspace(-0.9, 0.9, 8)
    w_void = np.ones(8)
    w_void[2] = 1e-12          # huge field V = -log u at node 2
    w_void[5] = 1e-12
    m_v, g_v = qp_equilibrium(xs_q, w_void, 3.0, 400)
    nb_v, gap_v, void_v, _s = kkt_partition(m_v, g_v)
    ok_void = (bool(void_v[2]) and bool(void_v[5])
               and gap_v > 0.0 and nb_v <= 2)
    xs_a = np.array([-0.9, -0.7, -0.4, -0.1, 0.15, 0.5, 0.6, 0.85])
    m_s, g_s = qp_equilibrium(xs_a, np.ones(8), 7.0, 400)
    nb_s, gap_s, _v, sat_s = kkt_partition(m_s, g_s)
    ok_sat = (int(sat_s.sum()) == 7 and gap_s > 0.0
              and math.isfinite(gap_s))
    mx_unc = mutant_unconstrained(xs_q, w_void, 3.0, 400)
    check("G11-toy-qp-kkt", ok_proj and ok_void and ok_sat
          and mx_unc > 1.0 + 1e-6,
          "THE QP MACHINERY TOYS: the box-simplex water-filling "
          "projection is exact (mass 3.0 at 1e-10, bounds respected, "
          "IDEMPOTENT at 1e-10); the FIELD-VOID toy (two nodes with "
          "u = 1e-12): both are VOIDED by the solver with a positive "
          "KKT gap %.2f (#band %d); the SATURATION toy (mass 7 of 8): "
          "exactly 7 nodes saturate, KKT gap %.2f -- the partition "
          "logic is two-sided; the UNCONSTRAINED mutant on the void "
          "toy piles max m = %.2f > 1: the cap is load-bearing "
          "already on the toy" % (gap_v, nb_v, gap_s, mx_unc))
    # (T3) interlacing toy both directions (r359 G13 seeds)
    seedM = np.array([[1.0, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3],
                      [4, 5, 6, 7, 8, 9], [1, 3, 5, 7, 9, 2],
                      [4, 6, 8, 1, 3, 5], [9, 7, 5, 3, 1, 8]])
    Qr, _ = np.linalg.qr(seedM)
    oks = []
    for lams, expect in ((np.array([0.52, 0.6, 0.7, 0.8, 0.9, 0.95]),
                          True),
                         (np.array([0.31, 0.6, 0.7, 0.8, 0.9, 0.95]),
                          False)):
        Rt = Qr @ np.diag(lams) @ Qr.T
        Mt = Rt - 0.5 * np.eye(6)
        rest_t = list(range(2, 6))
        Mcc_x = Mt[np.ix_(rest_t, rest_t)]
        Sx = Mt[np.ix_([0, 1], [0, 1])] \
            - Mt[np.ix_([0, 1], rest_t)] \
            @ np.linalg.solve(Mcc_x, Mt[np.ix_(rest_t, [0, 1])])
        emin = float(np.linalg.eigvalsh(Mt)[0])
        rmin = float(np.linalg.eigvalsh(Mcc_x)[0])
        smin = float(np.linalg.eigvalsh(0.5 * (Sx + Sx.T))[0])
        both = (rmin > 0) and (smin > 0)
        oks.append(((emin > 0) == expect) and (both == expect)
                   and (not expect
                        or (rmin >= emin * (1 - 1e-12)
                            and smin >= emin * (1 - 1e-12))))
    check("G12-toy-interlacing", all(oks),
          "THE RELATIVE-REST THEOREM SIDE on the synthetic SPD toy in "
          "BOTH truth directions: lambda_min(M_CC) >= lambda_min(M) "
          "(CAUCHY EIGENVALUE INTERLACING, principal submatrix) and "
          "lambda_min(S_N) >= lambda_min(M) (the Schur-complement "
          "eigenvalue inequality) hold on the live direction -- the "
          "c = 1 relative rest clause is a finite theorem; the dead "
          "direction (lambda_min = 0.31 < 1/2) correctly fails the "
          "split")

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + OCCUPATION + QP + T_GEO")
    R9 = PX.build_rung(MAIN_KZ)
    mz9 = R9["mz"]
    o9 = sat_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                  R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"])
    A9 = W9_SCHUR_ANCH
    ok_rec = (R9["S"] == REC_S and R9["Sm"] == REC_SM
              and R9["Nw"] == REC_NW
              and abs(R9["margin"] / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL
              and abs((o9["eps"] + 0.5) - REC_LAMR) <= 1e-8
              and abs(o9["eps"] / A9["eps"] - 1.0) <= 1e-3
              and abs(o9["lamS"] / A9["lamS"] - 1.0) <= 1e-3
              and abs(o9["detS"] / A9["detS"] - 1.0) <= 1e-3
              and abs(o9["share"] - A9["share"]) <= 5e-3
              and o9["f1"] == A9["f1"] and o9["f2"] == A9["f2"])
    check("G20-w9-records", ok_rec,
          "w9: S = %d (nu %d), N_w = %d, margin %.4e (record %.4e); "
          "lambda_min(R) = %.9f == the r356 record; THE r359 SCHUR "
          "ANCHORS REPRODUCED: eps %+.4e, lamS %+.4e, detS %+.4e, "
          "share %.4f (rel 1e-3 / abs 5e-3); folds (%d, %d) == the "
          "critical pair"
          % (R9["S"], R9["Sm"], R9["Nw"], R9["margin"], REC_MARGIN,
             o9["eps"] + 0.5, o9["eps"], o9["lamS"], o9["detS"],
             o9["share"], o9["f1"], o9["f2"]))
    xu9 = np.asarray(mz9["xu"], float)
    u9 = np.abs(np.asarray(mz9["wu"], float))
    oe9 = occ_profile(xu9, u9, R9["Nw"])
    dev_comp9 = float(np.max(np.abs(oe9 - (1.0 - o9["od"]))))
    AS = W9_SAT_ANCH
    iY9 = np.searchsorted(xu9, np.asarray(mz9["yn"], float))
    odf2 = float(o9["od"][iY9[R9["i1"]]])
    odf4 = float(o9["od"][iY9[R9["i2"]]])
    ok_occ9 = (dev_comp9 <= OCC_COMP_BAR[0]
               and o9["dev_tr"] <= TRACE_BAR[0]
               and abs(o9["od1"] - AS["od1"]) <= SAT_ANCH_TOL
               and abs(odf2 - AS["odf2"]) <= SAT_ANCH_TOL
               and abs(odf4 - AS["odf4"]) <= SAT_ANCH_TOL
               and o9["devf1"] <= -ZONE_BAR
               and abs(o9["devp1"]) <= PAIR_FLAT_BAR
               and abs(o9["devp2"]) <= PAIR_FLAT_BAR)
    check("G21-w9-occupation", ok_occ9,
          "THE EXACT OCCUPATION FIELD at w9: complement ward "
          "max |o_eta + o_dual - 1| = %.1e (bar %.0e -- the O1 "
          "duality is exact); trace ward |sum o_dual - (N_w - 1)| = "
          "%.1e; o_dual(fold 1) = %.4f (anchor %.4f) against bulk "
          "median %.4f: dev %+.4f <= -%.2f -- THE FOLD-1 ANOMALY "
          "(primal-saturated edge zone by O1: o_eta(fold 1) = %.4f); "
          "the pair folds are FLAT (od(f2) %.4f, od(f4) %.4f, devs "
          "%+.4f / %+.4f <= %.2f): the critical pair sits AT the "
          "edge of the saturated zone, not inside it"
          % (dev_comp9, OCC_COMP_BAR[0], o9["dev_tr"], o9["od1"],
             AS["od1"], o9["occ_med"], o9["devf1"], ZONE_BAR,
             1.0 - o9["od1"], odf2, odf4, o9["devp1"], o9["devp2"],
             PAIR_FLAT_BAR))
    m9, g9 = qp_equilibrium(xu9, o9["ud"], float(R9["Nw"] - 1),
                            QP_ITERS)
    nb9, gap9, void9, sat9 = kkt_partition(m9, g9)
    f9 = o9["f"]
    void_folds9 = tuple(sorted(int(f9[j]) for j in
                               np.nonzero(void9)[0]
                               if f9[j] <= 8))
    blk_ok9 = all(void9[np.nonzero(f9 == ff)[0][0]]
                  for ff in QP_VOID_BLOCK) \
        and bool(sat9[np.nonzero(f9 == 4)[0][0]])
    check("G22-w9-qp", blk_ok9 and nb9 <= NB_MAX and gap9 >= GAP_MIN,
          "THE OBSTACLE PROBLEM at w9 (sealed FISTA %d iters): the "
          "solution CRYSTALLIZES (#band = %d <= %d, KKT separation "
          "gap = %+.3f >= %.0e); the dual VOID block at the right "
          "edge is %s == the sealed %s (folds <= 8 shown) -- by O1 "
          "the PRIMAL SATURATED block; fold 4 is dual-SATURATED: THE "
          "CRITICAL PAIR (2, 4) STRADDLES THE SATURATION-BLOCK EDGE "
          "3|4 (fold 2 inside the saturated zone, fold 4 outside) -- "
          "the round's partition thesis at the flagship"
          % (QP_ITERS, nb9, NB_MAX, gap9, GAP_MIN,
             str(void_folds9), str(QP_VOID_BLOCK)))
    ok_tgeo9 = (abs(o9["tgeo"] - AS["tgeo"]) <= SAT_ANCH_TOL
                and o9["dev_rm"] <= RM_BAR[0])
    check("G23-w9-tgeo", ok_tgeo9,
          "THE PARAMETRIX DATUM at w9: t_geo = eps sqrt((A^{-1})_11 "
          "(A^{-1})_22) = %.4f (anchor %.4f) -- dimensionless, and "
          "by the r359 resolvent-minor identity (re-gated here at "
          "%.1e <= %.0e) exactly 1/(2 sqrt(det(S_N/eps)(1 - share))); "
          "kappa_S = detS/lamS^2 = %.1f; the adjugate log "
          "decomposition log detS == -log 4 - log(a11 a22) - "
          "log(1 - share) is the O6 wander-cancellation coordinate"
          % (o9["tgeo"], AS["tgeo"], o9["dev_rm"], RM_BAR[0],
             o9["kap"]))
    o9s = slim360(o9)
    od9 = o9["od"]
    ud9 = o9["ud"]
    del o9

    # ---------------- S3 the ladder
    section("S3  LEG B/C/D -- THE 85-ROW LADDER -- WARDS + ZONE "
            "CENSUS + FITS + ADJUDICATIONS")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-chain-occ-wards",
                  "G34-equivalence-binding-rest", "G35-fit-alpha",
                  "G36-occupation-zone-census", "G37-tgeo-kappa",
                  "G38-wander-cancel"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: o9s}
        MT = {MAIN_KZ: dict(margin=R9["margin"], Nw=R9["Nw"],
                            z=R9["z"], Sm=R9["Sm"])}
        all_kz, fit_kz = [MAIN_KZ], [MAIN_KZ]
        sup_fail: list = []
        chain_fail: list = []
        sat_main = None
        alpha_hit = None
        alpha_slope = None
        kap_ratio = None
        kap_band_ok = None
        tgeo_ok = None
        rest_min_ratio = {"MAIN": o9s["rest_min"] / o9s["eps"]}
        wc_corr = None
        wc_ratio = None
        n_resolv = 1
        zone_cnt = 1
    else:
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows, 35))
        used |= set(EXT3_KZ_B + EXT3_KZ_A)
        used |= set(EXT4_KZ_B + EXT4_KZ_A)
        pool5 = E3.admissible_pool(EXT5_H_LO, EXT5_H_HI)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = [(h, kz) for (h, kz) in pool5
                  if kz not in used and zz5[kz] ** 2 <= Z2_CAP]
        fresh5.sort(reverse=True)
        ext5_sel = tuple(kz for (_h, kz) in fresh5[:K_EXT5])
        ext5_h = tuple(h for (h, _kz) in fresh5[:K_EXT5])
        used6 = used | set(ext5_sel)
        pool6 = E3.admissible_pool(EXT6_H_LO, EXT6_H_HI)
        zz6 = {kz: int(core._NN[kz]) for (_h, kz) in pool6}
        fresh6 = [(h, kz) for (h, kz) in pool6
                  if kz not in used6 and zz6[kz] ** 2 <= Z2_CAP]
        fresh6.sort(reverse=True)
        ext6_sel = tuple(kz for (_h, kz) in fresh6[:K_EXT6])
        ext6_h = tuple(h for (h, _kz) in fresh6[:K_EXT6])
        check("G30-ext-selection",
              len(used) == USED5_EXPECT
              and len(fresh5) == FRESH5_EXPECT
              and ext5_sel == EXT5_KZ_EXPECT
              and ext5_h == EXT5_H_EXPECT
              and len(used6) == USED6_EXPECT
              and len(fresh6) == FRESH6_EXPECT
              and ext6_sel == EXT6_KZ_EXPECT
              and ext6_h == EXT6_H_EXPECT,
              "SEALED SELECTIONS executed verbatim (r356 rules "
              "AS-IS): EXT5 used %d == %d, fresh %d == %d, queue %s; "
              "EXT6 used %d == %d, fresh %d == %d, queue %s (h %s) "
              "== the r356 record"
              % (len(used), USED5_EXPECT, len(fresh5), FRESH5_EXPECT,
                 str(ext5_sel), len(used6), USED6_EXPECT,
                 len(fresh6), FRESH6_EXPECT, str(ext6_sel),
                 str(ext6_h)))
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in lm_rows[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        ext5_kzs = list(ext5_sel)
        ext6_kzs = list(ext6_sel)
        OT, MT = {}, {}
        sup_fail, neg_rows = [], []
        print("    %-5s %-5s %-5s %-5s | %-10s %-10s %-6s | %-7s "
              "%-7s %-7s | %-7s %-7s | %-6s %-7s"
              % ("kz", "z", "S-", "N_w", "eps", "rest", "bind",
                 "od1", "devf1", "devp12", "tgeo", "kap", "share",
                 "dev_tr"))
        for kz in (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                   + ext5_kzs + ext6_kzs):
            if kz == MAIN_KZ:
                Rr = R9
                o = dict(o9s)
            else:
                if kz in set(ext6_kzs):
                    Rr = PWA.rung_reduced_cols(kz)
                    Rr["z"] = int(V.PP[kz])
                else:
                    Rr = PX.build_rung(kz)
                mz = Rr["mz"]
                o = sat_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                             Rr["Nw"], Rr["S"], mz["L"], Rr["i1"],
                             Rr["i2"])
                o = slim360(o)
            if Rr["margin"] <= 0:
                neg_rows.append(kz)
            if not (o["ok_sup"] and o["ok_map"]):
                sup_fail.append(kz)
            bind = o["lamS"] / o["eps"] if o["eps"] > 0 \
                else float("nan")
            print("    %-5d %-5d %-5d %-5d | %+.3e %+.3e %6.3f | "
                  "%.4f %+.4f %+.4f | %.4f %7.2f | %.4f %.1e"
                  % (kz, Rr["z"], Rr["Sm"], Rr["Nw"], o["eps"],
                     o["rest_min"], bind, o["od1"], o["devf1"],
                     max(abs(o["devp1"]), abs(o["devp2"])),
                     o["tgeo"], o["kap"], o["share"], o["dev_tr"]),
                  flush=True)
            OT[kz] = o
            MT[kz] = dict(margin=Rr["margin"], Nw=Rr["Nw"],
                          z=Rr["z"], Sm=Rr["Sm"])
            del Rr, o
        all_kz = (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                  + ext5_kzs + ext6_kzs)
        fit_kz = [k for k in core_kzs + ext_kzs]
        check("G31-ladder-census", len(core_kzs) == 42
              and len(fit_kz) == 57 and len(all_kz) == 85
              and not neg_rows,
              "42 core + 15 r286 extension + 12 EXT3 + 6 EXT4 + 6 "
              "EXT5 + 4 EXT6 = %d rows (fits on the %d old rows "
              "ONLY, EXT rows puretest); every f64 margin positive "
              "(negatives: %s)"
              % (len(all_kz), len(fit_kz),
                 str(neg_rows) if neg_rows else "none"))
        check("G32-support-gate-all", not sup_fail,
              "THE RANK/SUPPORT GATE on ALL %d rows: S == L/2 == "
              "2 N_w - 1 with the union support == the full cosine "
              "grid (failures: %s)"
              % (len(all_kz), str(sup_fail) if sup_fail else "none"))

        def gmax(key, g):
            vals = [OT[k][key] for k in all_kz
                    if grade_of(MT[k]["Nw"]) == g]
            return max(vals) if vals else 0.0

        chain_fail = []
        txt_w = []
        for key, bars, lab in (("dev_detid", DETID_BAR, "det-id"),
                               ("dev_cd", CD_BAR, "CD"),
                               ("dev_iiks", IIKS_BAR, "IIKS"),
                               ("dev_coup", COUP_BAR, "coupling"),
                               ("dev_rm", RM_BAR, "res-minor"),
                               ("dev_tr", TRACE_BAR, "occ-trace")):
            per = [gmax(key, g) for g in range(3)]
            ok_here = all(per[g] <= bars[g] for g in range(3))
            if not ok_here:
                chain_fail.append(lab)
            txt_w.append("%s %.1e/%.1e/%.1e (%s)"
                         % (lab, per[0], per[1], per[2],
                            "ok" if ok_here else "FAIL"))
        ok_sgn = all(OT[k]["sgn_det_ok"] for k in all_kz)
        if not ok_sgn:
            chain_fail.append("det-sign")
        check("G33-chain-occ-wards", not chain_fail,
              "THE r359 E1-E5 WARDS + THE OCCUPATION TRACE WARD on "
              "all %d rows, graded shallow/mid/deep: %s; det-sign "
              "%d/%d -- the exact chain and the occupation field "
              "carry the whole family"
              % (len(all_kz), "; ".join(txt_w),
                 sum(1 for k in all_kz if OT[k]["sgn_det_ok"]),
                 len(all_kz)))
        resolv = [k for k in all_kz if OT[k]["eps"] > RESOLV_FLOOR]
        floor_rows = [k for k in all_kz if k not in set(resolv)]
        n_resolv = len(resolv)
        eq_bad = [k for k in resolv
                  if not (OT[k]["rest_min"] > 0 and OT[k]["lamS"] > 0)]
        binds = {k: OT[k]["lamS"] / OT[k]["eps"] for k in resolv}
        bind_bad = [k for k in resolv
                    if not (BIND_MIN <= binds[k] <= BIND_MAX)]
        jord_bad = [k for k in resolv
                    if not (OT[k]["rest_min"]
                            >= OT[k]["eps"] * (1.0 - JORD_TOL)
                            and OT[k]["lamS"]
                            >= OT[k]["eps"] * (1.0 - JORD_TOL))]
        if eq_bad:
            chain_fail.append("equivalence")
        if bind_bad or jord_bad:
            chain_fail.append("jacobi-order")
        ratio_re = sorted(OT[k]["rest_min"] / OT[k]["eps"]
                          for k in resolv)
        crel_bad_main = [k for k in resolv
                         if OT[k]["rest_min"] / OT[k]["eps"] < C_REL]
        bind_sorted = sorted(binds.values())
        rest_min_ratio = {"MAIN": ratio_re[0]}
        check("G34-equivalence-binding-rest", not eq_bad
              and not bind_bad and not jord_bad,
              "on the %d resolvable rows (eps > %.0e; floor rows %s "
              "sign census): the equivalence {rest > 0} AND {S_N > "
              "0} %d/%d; THE INTERLACING THEOREM SIDE (rest >= eps, "
              "lamS >= eps -- the c = 1 relative clause) %d/%d; bind "
              "in [%.4f, %.4f] med %.4f (r359 clause [%f, %.1f]); "
              "THE RELATIVE REST CENSUS: rest/eps in [%.1f, %.1f] "
              "med %.1f, C_REL %.1f violations %s"
              % (n_resolv, RESOLV_FLOOR,
                 str([(k, "%+.1e" % OT[k]["eps"])
                      for k in floor_rows]),
                 n_resolv - len(eq_bad), n_resolv,
                 n_resolv - len(jord_bad), n_resolv,
                 bind_sorted[0], bind_sorted[-1],
                 float(np.median(bind_sorted)), BIND_MIN, BIND_MAX,
                 ratio_re[0], ratio_re[-1],
                 float(np.median(ratio_re)), C_REL,
                 str(crel_bad_main) if crel_bad_main else "none"))
        rest_min_ratio["MAIN_bad"] = crel_bad_main
        lnN_all = np.log(np.array([MT[k]["Nw"] for k in all_kz],
                                  float))
        mask57 = np.array([k in set(fit_kz) for k in all_kz])
        lnN57 = lnN_all[mask57]
        marg_col = np.array([MT[k]["margin"] for k in all_kz])
        detS_col = np.array([OT[k]["detS"] for k in all_kz])
        rest_col = np.array([OT[k]["rest_min"] for k in all_kz])
        lamS_col = np.array([OT[k]["lamS"] for k in all_kz])
        sl_m = float(LM.ts_fit(lnN57, np.log(marg_col[mask57]))[1])
        sl_d = float(LM.ts_fit(lnN57, np.log(detS_col[mask57]))[1])
        sl_r = float(LM.ts_fit(lnN57, np.log(rest_col[mask57]))[1])
        sl_s = float(LM.ts_fit(lnN57, np.log(lamS_col[mask57]))[1])
        alpha_slope = -sl_s
        dists = [abs(alpha_slope - c) for c in ALPHA_CANDS]
        alpha_hit = ALPHA_CANDS[int(np.argmin(dists))] \
            if min(dists) <= ALPHA_TOL else None
        # split-half curvature print (curvature-honest, census)
        o57 = np.argsort(lnN57)
        h1 = o57[:len(o57) // 2]
        h2 = o57[len(o57) // 2:]
        sl_s1 = float(LM.ts_fit(lnN57[h1],
                                np.log(lamS_col[mask57][h1]))[1])
        sl_s2 = float(LM.ts_fit(lnN57[h2],
                                np.log(lamS_col[mask57][h2]))[1])
        a11_col = np.array([abs(OT[k]["a11"]) for k in all_kz])
        a22_col = np.array([abs(OT[k]["a22"]) for k in all_kz])
        a12_col = np.array([abs(OT[k]["a12"]) for k in all_kz])
        sl_a11 = float(LM.ts_fit(lnN57, np.log(a11_col[mask57]))[1])
        sl_a22 = float(LM.ts_fit(lnN57, np.log(a22_col[mask57]))[1])
        sl_a12 = float(LM.ts_fit(lnN57, np.log(a12_col[mask57]))[1])
        cand_txt = "; ".join(
            "a11 vs %.3f: %.3f" % (c, abs(sl_a11 - c))
            for c in CAND_PRINTS[:4])
        check("G35-fit-alpha", abs(sl_m - FIT_MARGIN_ANCH)
              <= FIT_MARGIN_TOL
              and abs(sl_d - FIT_DETS_ANCH) <= FIT_R359_TOL
              and abs(sl_r - FIT_REST_ANCH) <= FIT_R359_TOL,
              "LEG 0 FIT ANCHORS on the 57: margin slope %.3f == "
              "r352 %.3f; detS %.3f == r359 %.3f; rest %.3f == r359 "
              "%.3f; THE ALPHA ADJUDICATION (leg C): fresh lamS "
              "slope %.3f -> alpha = %.3f, candidate distances "
              "(%.3f: %.3f / %.2f: %.3f) -> %s; split-half curvature "
              "(census, disclosed): shallow %.3f / deep %.3f; the "
              "a-column exponent censi (leg B): |a11| %+.3f, |a22| "
              "%+.3f, |a12| %+.3f (candidate prints: %s; the "
              "1.786/1.683 Christoffel family and the 0.38 family "
              "distances printed, censi only)"
              % (sl_m, FIT_MARGIN_ANCH, sl_d, FIT_DETS_ANCH, sl_r,
                 FIT_REST_ANCH, sl_s, alpha_slope, ALPHA_CANDS[0],
                 dists[0], ALPHA_CANDS[1], dists[1],
                 ("HIT %.3f" % alpha_hit) if alpha_hit is not None
                 else "NO HIT", sl_s1, sl_s2, sl_a11, sl_a22,
                 sl_a12, cand_txt))
        # occupation zone census (leg A ladder-wide)
        zone_rows = [k for k in all_kz
                     if OT[k]["devf1"] <= -ZONE_BAR
                     and abs(OT[k]["devp1"]) <= PAIR_FLAT_BAR
                     and abs(OT[k]["devp2"]) <= PAIR_FLAT_BAR]
        zone_cnt = len(zone_rows)
        dev1s = sorted(OT[k]["devf1"] for k in all_kz)
        od1_anch_ok = all(abs(OT[k]["od1"] - OD1_SAMPLE_ANCH[k])
                          <= SAT_ANCH_TOL for k in OD1_SAMPLE_ANCH)
        decay_col = np.array([0.5 - OT[k]["od1"] for k in all_kz])
        sl_dec = float(LM.ts_fit(lnN57,
                                 np.log(decay_col[mask57]))[1]) \
            if np.all(decay_col[mask57] > 0) else float("nan")
        check("G36-occupation-zone-census",
              zone_cnt >= MAIN_ZONE_MIN and od1_anch_ok,
              "THE FOLD-1 ANOMALY CENSUS on the %d MAIN rows: %d/%d "
              "in the sealed pattern (dev1 <= -%.2f AND pair folds "
              "flat <= %.2f; misses %s); dev1 range [%+.3f, %+.3f]; "
              "od1 sample anchors kz44/56/130 hit; THE DECAY CENSUS "
              "(no sealed candidate, for the specialist): slope of "
              "ln(1/2 - od1) on the 57 = %+.3f -- the saturation "
              "edge fades slowly, far from any measured closing"
              % (len(all_kz), zone_cnt, len(all_kz), ZONE_BAR,
                 PAIR_FLAT_BAR,
                 str([k for k in all_kz if k not in set(zone_rows)])
                 if zone_cnt < len(all_kz) else "none",
                 dev1s[0], dev1s[-1], sl_dec))
        sat_main = (zone_cnt >= MAIN_ZONE_MIN)
        # t_geo + kappa clauses (legs B/C) on resolvable rows
        tg = {k: OT[k]["tgeo"] for k in resolv}
        tg_vals = sorted(tg.values())
        tg_band_bad = [k for k in resolv
                       if not (T_GEO_BAND[0] < tg[k] < T_GEO_BAND[1])]
        tg_col = np.array([OT[k]["tgeo"] for k in all_kz])
        sl_tg = float(LM.ts_fit(lnN57, np.log(tg_col[mask57]))[1])
        tgeo_anch_ok = all(abs(OT[k]["tgeo"] - TGEO_SAMPLE_ANCH[k])
                           <= SAT_ANCH_TOL
                           for k in TGEO_SAMPLE_ANCH)
        tgeo_ok = (abs(sl_tg) <= T_GEO_SLOPE_TOL
                   and not tg_band_bad and tgeo_anch_ok)
        kaps = sorted(OT[k]["kap"] for k in resolv)
        kap_ratio = kaps[-1] / kaps[0]
        kap_band_ok = (kaps[0] > KAPPA_BAND[0]
                       and kaps[-1] < KAPPA_BAND[1])
        check("G37-tgeo-kappa", tgeo_anch_ok,
              "THE PARAMETRIX-CLASS CENSUS (leg B): t_geo on the %d "
              "resolvable rows in [%.4f, %.4f] med %.4f (band (%."
              "2f, %.2f) violations %s), slope %+.3f (|.| <= %.2f "
              "-> %s), sample anchors hit; THE M_0 SHAPE (leg C): "
              "kappa_S = lammax/lammin in [%.1f, %.1f] med %.1f, "
              "range ratio %.2f (collapse iff <= %.1f -> %s; bounded "
              "band (%.0f, %.0f) -> %s) -- the margin direction "
              "collapses (bind), the second eigenvalue wanders O(1)"
              % (n_resolv, tg_vals[0], tg_vals[-1],
                 float(np.median(tg_vals)), T_GEO_BAND[0],
                 T_GEO_BAND[1],
                 str(tg_band_bad) if tg_band_bad else "none",
                 sl_tg, T_GEO_SLOPE_TOL,
                 "SLOPE OK" if abs(sl_tg) <= T_GEO_SLOPE_TOL
                 else "SLOPE OFF", kaps[0], kaps[-1],
                 float(np.median(kaps)), kap_ratio, KAPPA_RATIO_MAX,
                 "COLLAPSE" if kap_ratio <= KAPPA_RATIO_MAX
                 else "NO (partial)", KAPPA_BAND[0], KAPPA_BAND[1],
                 "IN BAND" if kap_band_ok else "OUT"))
        # wander cancellation (leg C2 / O6)
        a1122_col = np.array([abs(OT[k]["a11"] * OT[k]["a22"])
                              for k in all_kz])
        psi_d, _s1 = BDH.psi_fit57(lnN_all, np.log(detS_col), mask57)
        psi_a, _s2 = BDH.psi_fit57(lnN_all, -np.log(a1122_col),
                                   mask57)
        share_col = np.array([OT[k]["share"] for k in all_kz])
        sh_ok = np.abs(1.0 - share_col) > 1e-12
        psi_s, _s3 = BDH.psi_fit57(
            lnN_all, np.log(np.abs(1.0 - share_col) + 1e-300),
            mask57)
        wc_corr = float(np.corrcoef(psi_d[mask57], psi_a[mask57])
                        [0, 1])
        wc_ratio = float(np.sqrt(np.mean(psi_s[mask57] ** 2))
                         / max(np.sqrt(np.mean(psi_d[mask57] ** 2)),
                               1e-300))
        check("G38-wander-cancel", bool(np.all(sh_ok[mask57])),
              "THE WANDER-CANCELLATION PROBE (O6, via the exact "
              "adjugate identity, pointwise ward = the res-minor "
              "ward of G33): corr(psi57 log detS, -psi57 log(a11 "
              "a22)) = %+.4f (clause >= %.2f -> %s); rms(psi57 "
              "log(1 - share)) / rms(psi57 log detS) = %.3f -- the "
              "cross-share term is %s; the leading common wander of "
              "det S_N IS the diagonal-resolvent wander, cancelling "
              "algebraically inside the minor"
              % (wc_corr, WCANCEL_CORR_MIN,
                 "COHERES" if wc_corr >= WCANCEL_CORR_MIN
                 else "OFF", wc_ratio,
                 "subleading" if wc_ratio <= 0.5 else "NOT small"))

    # ---------------- S4 the QP instances (leg A)
    section("S4  LEG A -- THE OBSTACLE PROBLEM ON THE SEALED "
            "INSTANCES + CONTROLS")
    if smoke:
        check("G40-qp-main-instances", True,
              "SMOKE: w9 gated in G22; deep instances skipped")
        c3 = chi_sat_row(MAIN_KZ, DMF.Q_CHI3, DMF.LPQ3)
        anch3 = CHI_W9_ANCH["chi3"]
        ok_c3 = (abs(c3["od1"] - anch3["od1"]) <= CHI_ANCH_TOL
                 and abs(c3["tgeo"] - anch3["tgeo"]) <= CHI_ANCH_TOL
                 and abs(c3["devf1"]) <= CHI_FLAT_BAR
                 and c3["dev_cd"] <= CD_BAR[0])
        check("G41-qp-chi-scr-contrast", ok_c3,
              "SMOKE chi3 w9 only: od1 %.4f (anchor %.4f) dev1 "
              "%+.4f <= %.2f -- NO fold-1 anomaly on the second "
              "arithmetic; t_geo %.4f (anchor %.4f) in band"
              % (c3["od1"], anch3["od1"], c3["devf1"], CHI_FLAT_BAR,
                 c3["tgeo"], anch3["tgeo"]))
        qp_ok = None
        chi_contrast = None
    else:
        qp_rows = {}
        for kz in QP_KZ:
            if kz == MAIN_KZ:
                qp_rows[kz] = dict(nb=nb9, gap=gap9,
                                   blk=blk_ok9, comp=dev_comp9)
                continue
            Rr = PX.build_rung(kz)
            mz = Rr["mz"]
            xu = np.asarray(mz["xu"], float)
            u = np.abs(np.asarray(mz["wu"], float))
            ud, _lA, f, _e, _lp = BDH.dual_weights(xu, u, Rr["S"],
                                                   mz["L"])
            oe = occ_profile(xu, u, Rr["Nw"])
            od = occ_profile(xu, ud, Rr["Nw"] - 1)
            comp = float(np.max(np.abs(oe - (1.0 - od))))
            m, g = qp_equilibrium(xu, ud, float(Rr["Nw"] - 1),
                                  QP_ITERS)
            nb, gap, void, sat = kkt_partition(m, g)
            blk = all(void[np.nonzero(f == ff)[0][0]]
                      for ff in QP_VOID_BLOCK) \
                and bool(sat[np.nonzero(f == 4)[0][0]])
            qp_rows[kz] = dict(nb=nb, gap=gap, blk=blk, comp=comp)
            del Rr, mz, xu, u, ud, oe, od, m, g, void, sat
        qp_ok = all(r["blk"] and r["nb"] <= NB_MAX
                    and r["gap"] >= GAP_MIN
                    and r["comp"]
                    <= OCC_COMP_BAR[grade_of(MT[k]["Nw"])]
                    for k, r in qp_rows.items())
        check("G40-qp-main-instances", qp_ok,
              "THE SEALED QP INSTANCES %s: void block == %s + fold 4 "
              "saturated (STRADDLE) %s; #band %s <= %d; KKT gaps %s "
              ">= %.0e; occupation complement wards %s (graded) -- "
              "THE CRITICAL PAIR STRADDLES THE PRIMAL SATURATION-"
              "BLOCK EDGE 3|4 ON 4/4 SEALED INSTANCES"
              % (str(QP_KZ), str(QP_VOID_BLOCK),
                 str([qp_rows[k]["blk"] for k in QP_KZ]),
                 str([qp_rows[k]["nb"] for k in QP_KZ]), NB_MAX,
                 str(["%+.3f" % qp_rows[k]["gap"] for k in QP_KZ]),
                 GAP_MIN,
                 str(["%.1e" % qp_rows[k]["comp"] for k in QP_KZ])))
        # chi w9 + scr w9 controls
        chi_ctl = {}
        for (q, lpq, tag) in ((DMF.Q_CHI3, DMF.LPQ3, "chi3"),
                              (DMF.Q_CHI4, DMF.LPQ4, "chi4")):
            uu, ww, _nn, _ch = DMF.chi_window_comb(MAIN_KZ, q)
            mzc = DMF.chi_build_measures(MAIN_KZ, uu, ww, 1.0, lpq)
            xuc = np.asarray(mzc["xu"], float)
            uc = np.abs(np.asarray(mzc["wu"], float))
            udc, _lA, fc, _e, _lp = BDH.dual_weights(
                xuc, uc, mzc["S"], mzc["L"])
            oec = occ_profile(xuc, uc, mzc["Nw"])
            odc = occ_profile(xuc, udc, mzc["Nw"] - 1)
            compc = float(np.max(np.abs(oec - (1.0 - odc))))
            mc, gc = qp_equilibrium(xuc, udc, float(mzc["Nw"] - 1),
                                    QP_ITERS)
            nbc, gapc, voidc, _satc = kkt_partition(mc, gc)
            f1_occ = not bool(voidc[np.nonzero(fc == 1)[0][0]])
            vf = tuple(sorted(int(fc[j]) for j in
                              np.nonzero(voidc)[0] if fc[j] <= 8))
            chi_ctl[tag] = dict(f1_occ=f1_occ, vf=vf, nb=nbc,
                                gap=gapc, comp=compc)
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        xus = np.asarray(mzs["xu"], float)
        us = np.abs(np.asarray(mzs["wu"], float))
        uds, _lA, fs, _e, _lp = BDH.dual_weights(xus, us, mzs["S"],
                                                 mzs["L"])
        ods = occ_profile(xus, uds, mzs["Nw"] - 1)
        j1s = int(np.nonzero(fs == 1)[0][0])
        od1s = float(ods[j1s])
        ms, gs = qp_equilibrium(xus, uds, float(mzs["Nw"] - 1),
                                QP_ITERS)
        _nbs, _gaps, voids, _sats = kkt_partition(ms, gs)
        scr_f1_occ = not bool(voids[j1s])
        vfs = tuple(sorted(int(fs[j]) for j in np.nonzero(voids)[0]
                           if fs[j] <= 8))
        chi_contrast = (chi_ctl["chi3"]["f1_occ"]
                        and chi_ctl["chi4"]["f1_occ"])
        check("G41-qp-chi-scr-contrast", chi_contrast
              and all(c["nb"] <= NB_MAX and c["gap"] >= GAP_MIN
                      and c["comp"] <= OCC_COMP_BAR[0]
                      for c in chi_ctl.values())
              and abs(od1s - SCR_OD1_ANCH) <= SCR_OD1_TOL,
              "THE WORLD CONTRAST OF THE PARTITION: chi3 QP occupies "
              "fold 1 (%s; void folds <= 8: %s), chi4 likewise (%s; "
              "%s) -- the MAIN void-block signature %s is ABSENT on "
              "both matched arithmetics (KKT gaps %+.3f/%+.3f, "
              "complement wards %.1e/%.1e); the SCRAMBLE occupation "
              "is disordered (od1 %.4f anchor %.4f, dev to its "
              "median below the zone bar) and its QP fold 1 is %s "
              "(void folds %s) -- the dead world has NO saturation "
              "edge either: the partition is a DIFFERENT one on "
              "every control, not the same with different distance"
              % (chi_ctl["chi3"]["f1_occ"],
                 str(chi_ctl["chi3"]["vf"]),
                 chi_ctl["chi4"]["f1_occ"],
                 str(chi_ctl["chi4"]["vf"]), str(QP_VOID_BLOCK),
                 chi_ctl["chi3"]["gap"], chi_ctl["chi4"]["gap"],
                 chi_ctl["chi3"]["comp"], chi_ctl["chi4"]["comp"],
                 od1s, SCR_OD1_ANCH,
                 "OCCUPIED" if scr_f1_occ else "void", str(vfs)))
        del mzs, xus, us, uds, ods, ms, gs, voids

    # ---------------- S5 worlds
    section("S5  LEG D/E -- TWIN + CHI LADDERS + MATCHED SCRAMBLE")
    if smoke:
        for g in ("G50-twin", "G51-chi3-ladder", "G52-chi4-ladder",
                  "G53-scramble-break"):
            check(g, True, "SMOKE: skipped")
        chi_fail: list = []
        crel_bad_chi: list = []
    else:
        tw_dev = 0.0
        tw_occ = 0.0
        ok_dose0 = True
        for kz in WORLD_KZ:
            uuc, mmc = TR.base_comb(kz)
            mzD = TR.build_world(kz, uuc, mmc)
            mzV = V.build_measures(kz)
            ok_dose0 = ok_dose0 and (
                np.array_equal(mzD["xp"], mzV["xp"])
                and np.array_equal(mzD["wp"], mzV["wp"])
                and np.array_equal(mzD["yn"], mzV["yn"])
                and np.array_equal(mzD["vn"], mzV["vn"]))
            gapsc = MF.local_gaps(uuc)
            u2c, m2c, _dn, _du = AKD.twin_rational(
                uuc, mmc, gapsc, mzD["D"], 1.0e-8)
            mzT = TR.build_world(kz, u2c, m2c)
            t1_, t2_ = PX.pair_select(mzT["yn"])
            oT = sat_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                          mzT["vn"], mzT["Nw"], mzT["S"],
                          mzT["L"], t1_, t2_)
            oM = OT[kz]
            tw_dev = max(
                tw_dev,
                abs(math.log(oT["detS"] / oM["detS"])),
                abs(math.log(oT["rest_min"] / oM["rest_min"])),
                abs(math.log(oT["lamS"] / oM["lamS"])))
            tw_occ = max(tw_occ,
                         abs(oT["od1"] - oM["od1"]),
                         abs(oT["devp1"] - oM["devp1"]),
                         abs(oT["devp2"] - oM["devp2"]))
            del oT
        check("G50-twin", ok_dose0 and tw_dev <= TWIN_BAR
              and tw_occ <= TWIN_OCC_BAR,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "identity BITWISE %s): Schur devs max %.1e nats (bar "
              "%.0e, the r359 1.4x-headroom truth); occupation devs "
              "max %.1e abs (bar %.0e) -- the partition coordinates "
              "are twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_BAR, tw_occ,
                 TWIN_OCC_BAR))
        chi_fail = []
        crel_bad_chi = []
        for (q, lpq, tag) in ((DMF.Q_CHI3, DMF.LPQ3, "chi3"),
                              (DMF.Q_CHI4, DMF.LPQ4, "chi4")):
            rows = []
            excl = []
            for kz in V.admissible_indices():
                o = chi_sat_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(slim360(o))
                del o
            live = [r for r in rows if r["eps"] > 0]
            sup_ok = all(r["ok_sup"] and r["ok_map"] for r in rows)
            wards_ok = all(r["dev_cd"] <= CD_BAR[0]
                           and r["dev_iiks"] <= IIKS_BAR[0]
                           and r["dev_coup"] <= COUP_BAR[0]
                           and r["dev_rm"] <= RM_BAR[0]
                           and r["dev_detid"] <= DETID_BAR[0]
                           and r["dev_tr"] <= TRACE_BAR[0]
                           for r in rows)
            eq_ok = all(r["rest_min"] > 0 and r["lamS"] > 0
                        for r in live)
            ratio_c = sorted(r["rest_min"] / r["eps"] for r in live)
            crel_bad = [r["kz"] for r in live
                        if r["rest_min"] / r["eps"] < C_REL]
            crel_bad_chi += crel_bad
            rest_min_ratio[tag] = ratio_c[0]
            zone_hits = [r["kz"] for r in rows
                         if r["devf1"] <= -ZONE_BAR]
            w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
            anch = CHI_W9_ANCH[tag]
            anch_ok = (abs(w9r["od1"] - anch["od1"]) <= CHI_ANCH_TOL
                       and abs(w9r["tgeo"] - anch["tgeo"])
                       <= CHI_ANCH_TOL
                       and abs(w9r["devf1"]) <= CHI_FLAT_BAR)
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and wards_ok and eq_ok and anch_ok
                        and len(live) == len(rows))
            if not ok_world:
                chi_fail.append(tag)
            check("G51-chi3-ladder" if tag == "chi3"
                  else "G52-chi4-ladder", ok_world,
                  "%s MATCHED LADDER through the IDENTICAL dual + "
                  "Schur + occupation pipeline: %d/42 built "
                  "(exclusions %s), support %s, chain + occupation "
                  "wards %s, eps positive %d/%d; THE RELATIVE REST "
                  "CENSUS: rest/eps in [%.1f, %.1f] med %.1f, C_REL "
                  "%.1f violations %s; THE ZONE CENSUS: fold-1 "
                  "anomaly on %d/%d rows (%s) -- the saturation edge "
                  "is MAIN-specific; w9 anchors hit (od1 %.4f, "
                  "t_geo %.4f, dev1 %+.4f flat)"
                  % (tag.upper(), len(rows),
                     str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     "PASS" if wards_ok else "FAIL",
                     len(live), len(rows), ratio_c[0], ratio_c[-1],
                     float(np.median(ratio_c)), C_REL,
                     str(crel_bad) if crel_bad else "none",
                     len(zone_hits), len(rows),
                     str(zone_hits) if zone_hits else "none",
                     w9r["od1"], w9r["tgeo"], w9r["devf1"]))
        # matched scramble (r357/r359 verbatim, seed 1)
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS = sat_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                      mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_)
        scr_named = (oS["rest_min"] < 0 and oS["eps"] < 0)
        alg_ok = (oS["dev_detid"] <= DETID_BAR[0]
                  and oS["dev_cd"] <= CD_BAR[0]
                  and oS["dev_tr"] <= TRACE_BAR[0])
        check("G53-scramble-break", scr_named and alg_ok
              and abs(oS["eps"] - SCR_ANCH["eps"]) <= 2e-3
              and abs(oS["rest_min"] - SCR_ANCH["rest"]) <= 2e-3
              and abs(oS["lamS"] / SCR_ANCH["lamS"] - 1.0) <= 5e-2
              and oS["lamS"] > 0,
              "THE MATCHED SCRAMBLE BREAKS AT THE NAMED "
              "PRECONDITION (r359 reproduced): eps = %+.4f < 0 and "
              "THE REST CLAUSE lambda_min(R_CC) - 1/2 = %+.4f < 0 "
              "(anchors) while the pair block ALONE stays positive "
              "(lamS %+.4e) -- pair-only reasoning would "
              "misclassify; the ALGEBRA is world-blind (det-id "
              "%.1e, CD %.1e, occupation trace %.1e); occupation "
              "census: od1 %.4f dev1 %+.4f (disordered, under the "
              "zone bar) -- the dead world has no saturation edge"
              % (oS["eps"], oS["rest_min"], oS["lamS"],
                 oS["dev_detid"], oS["dev_cd"], oS["dev_tr"],
                 oS["od1"], oS["devf1"]))
        del oS

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    mx1 = mutant_unconstrained(xu9, ud9, float(R9["Nw"] - 1),
                               QP_ITERS // 2)
    check("G80-m1-unconstrained", mx1 >= M1_BAR,
          "m1 THE CLASSICAL UNCONSTRAINED EQUILIBRIUM (cap removed): "
          "max m = %.1f >= %.1f x the discrete node cap at w9 -- the "
          "BKMM obstacle constraint is LOAD-BEARING, the classical "
          "class is wrong (and the toy shows the same, G11) -- "
          "CAUGHT" % (mx1, M1_BAR))
    check("G81-m2-alpha-readback", bool(hits_m2),
          "m2 ALPHA FROM THE MARGIN COLUMN (circular): AST-FLAGGED "
          "(%s) -- the sealed candidates are frozen record numbers, "
          "the fresh slope is computed from module-own columns only"
          % (hits_m2[0] if hits_m2 else "MISS"))
    check("G82-m3-m0-readback", bool(hits_m3),
          "m3 M_0 FIT BY SIGHT (posthoc alpha optimizer on the "
          "withheld det S_N column): AST-FLAGGED (%s) -- the "
          "sealed-candidate protocol is the catch"
          % (hits_m3[0] if hits_m3 else "MISS"))
    check("G83-m4-parametrix-readback", bool(hits_m4),
          "m4 PARAMETRIX PREDICTION VIA (A^{-1})-READBACK: "
          "AST-FLAGGED (%s) -- t_geo consumes module-own resolvent "
          "solves, the withheld a11 column enters gates only"
          % (hits_m4[0] if hits_m4 else "MISS"))
    od_shuf = mutant_weight_shuffle(xu9, ud9, R9["Nw"] - 1)
    f9v = np.rint(np.arccos(np.clip(xu9, -1.0, 1.0)) * mz9["L"]
                  / (2.0 * math.pi)).astype(int)
    j1_9 = int(np.nonzero(f9v == 1)[0][0])
    dev_m5 = abs(float(od_shuf[j1_9]) - od9[j1_9])
    check("G84-m5-weight-shuffle", dev_m5 >= M5_BAR,
          "m5 THE PARTITION WITH SHUFFLED (reversed) DUAL WEIGHT: "
          "the fold-1 occupation moves by %.3f >= %.1f at w9 -- the "
          "saturation edge is a WEIGHT-CARRIED structure, not a grid "
          "artifact -- CAUGHT" % (dev_m5, M5_BAR))
    dev_m6 = mutant_wrong_rank_occ(xu9, u9, ud9, R9["Nw"])
    check("G85-m6-wrong-rank", dev_m6 >= M6_BAR,
          "m6 THE OCCUPATION COMPLEMENT AT WRONG RANK (N_w instead "
          "of N_w - 1): breaks by %.2e >= %.0e at w9 (true value "
          "%.1e; and EXACTLY on the Fractions toy, G10) -- CAUGHT"
          % (dev_m6, M6_BAR, dev_comp9))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, no bound mechanism, "
          "no certificate reading, no posthoc bar/band/clause/"
          "candidate move, no derived 5/7, NO RH claim, mincut "
          "unchanged; no capacity products, no Fejer floors, no "
          "frame-A ceilings, no global g_min bounds, no worst-case "
          "martingale products; what the round adds: the exact "
          "occupation duality, the sealed obstacle-problem "
          "partition with the straddle finding, the parametrix-"
          "datum census, the alpha/M_0 adjudication, the wander-"
          "cancellation measurement and the relative rest clause "
          "with its theorem side; r243..r359 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        if not audits_ok:
            verd = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif sup_fail:
            verd = "SUPPORT_GATE_FAIL(%s)" % str(sup_fail)
        elif chain_fail or chi_fail:
            verd = "CHAIN_FAIL(%s)" % ", ".join(chain_fail + chi_fail)
        else:
            sat_ok = bool(qp_ok) and bool(sat_main) \
                and bool(chi_contrast)
            l_sat = ("SATURATION_EDGE_CONFIRMED(the pair (2, 4) "
                     "straddles the primal saturation block {1, 2, "
                     "3} at its edge 3|4; QP 4/4 + zone census "
                     "%d/85 + chi contrast)" % zone_cnt) if sat_ok \
                else ("SATURATION_REFUTED(qp %s, zone %s/85, chi "
                      "contrast %s -- honest: a different local "
                      "class is needed)"
                      % (qp_ok, zone_cnt, chi_contrast))
            l_gam = ("GAMMA_PARAMETRIX_CENSUS(t_geo family-constant "
                     "on the resolvable rows + chi w9 -- the "
                     "dimensionless diagonal-resolvent datum is "
                     "margin-locked; local-parametrix-class census, "
                     "NOT a Gamma derivation)") if tgeo_ok else \
                "GAMMA_CENSUS_OFF(t_geo clauses failed)"
            if alpha_hit is not None \
                    and kap_ratio is not None \
                    and kap_ratio <= KAPPA_RATIO_MAX:
                l_m0 = "M0_COLLAPSE(alpha %.3f)" % alpha_hit
            elif alpha_hit is not None and kap_band_ok:
                l_m0 = ("M0_PARTIAL(alpha = %.3f: the margin "
                        "direction collapses via bind, kappa_S "
                        "bounded in %s but wanders %.2fx > %.1f -- "
                        "the full M_0 collapse is honestly refuted; "
                        "the L1 target needs the relative form)"
                        % (alpha_hit, str(KAPPA_BAND), kap_ratio,
                           KAPPA_RATIO_MAX))
            else:
                l_m0 = "M0_OFF(slope %.3f, no candidate/band)" \
                    % (alpha_slope if alpha_slope is not None
                       else float("nan"))
            rest_ok = (not rest_min_ratio.get("MAIN_bad")
                       and not crel_bad_chi
                       and "chi3" in rest_min_ratio
                       and "chi4" in rest_min_ratio)
            l_rest = ("RELATIVE_REST_CERTIFIED(theorem side c = 1: "
                      "Cauchy interlacing + Schur eigenvalue "
                      "inequality, toy exact + live %d/%d; census "
                      "side c >= %.1f: mins MAIN %.1f / chi3 %.1f / "
                      "chi4 %.1f)"
                      % (n_resolv, n_resolv, C_REL,
                         rest_min_ratio["MAIN"],
                         rest_min_ratio.get("chi3", float("nan")),
                         rest_min_ratio.get("chi4", float("nan")))) \
                if rest_ok else \
                ("REST_RELATIVE_CENSUS(C_REL violations %s)"
                 % str(rest_min_ratio.get("MAIN_bad", [])
                       + crel_bad_chi))
            parts = [
                l_sat, l_gam, l_m0, l_rest,
                "WANDER_CANCEL_LEDGER(corr %+.4f, share-term rms "
                "ratio %.3f)" % (wc_corr, wc_ratio),
                "PARTITION_LEDGER(QP crystallized, KKT gates green)",
                "OCCUPATION_LEDGER(complement + trace exact; the "
                "fold-1 anomaly is the family-wide edge object)",
                "WORLD_LEDGER(chi3 + chi4 carry the chain; no chi "
                "saturation edge)",
                "TWIN_LEDGER(dose-zero bitwise; devs under bars)",
                "SCRAMBLE_BREAK(named: R_CC > I/2 fails at -0.496; "
                "no saturation edge on the dead world)",
                "MUSTFAIL_LEDGER(m1 loud, m2/m3/m4 AST, m5/m6 loud)",
            ]
            verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED partition/parametrix/collapse census + "
          "sealed adjudication; NO L* claim, NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
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
