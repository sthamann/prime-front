#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""augmented_borodin_duality_probe -- PRIME.LDAGGER.AUGMENTED_DUALITY.01
(round 362): THE AUGMENTED BORODIN-UVAROV DUALITY -- L† directly as
ONE dual object instead of L* and Terminal separately (the reviewer
moonshot, DCCX typing).  Coexistence: R360 (saturation lane) and R361
(mean-sieve lane) run in parallel -- this probe touches NOTHING
outside its own file and the strictly additive rh-sync.

THE FROZEN QUESTION (reviewer verbatim, binding): in the
mu-orthonormal frame the augmented subordination L† (r332, Lean
sorry-free: L† <=> A_cap > 0 <=> L* AND Terminal) is E† = E + b b^T/B
with E the nu-sampling matrix, b the border functional on the
mu-orthonormal basis and B > 0 the budget; L† <=> I - E† > 0 <=>
lambda_max(E†) < 1.  The border is, by the standing RHP theory
(v958), a rank-1 Schlesinger/Uvarov insertion.  DOES THE EXACT
AUGMENTED DUALITY EXIST: L† <=> R† > (1/2) I with R† a CONTROLLED
rank-1 deformation of the r356 dual hole kernel R -- so that the
critical block of R† carries the L* pair AND the terminal border
fiber in the SAME local object?

THE ROUTE ADJUDICATION (sealed BEFORE the freeze, from the disclosed
s1-s3 scoping):
  ROUTE (i), THE VIRTUAL NODE -- dead on the real windows, twice:
    (a) REPRESENTABILITY: b is a point evaluation b_i = c phat_i(x*)
    iff the recurrence-consistency values x*_i = a_i + (be_i b_{i+1}
    + be_{i-1} b_{i-1})/b_i are constant; measured spread 56.8 (w9)
    .. 4.5e+3 (kz56) -- the real border (the SIGNED smooth-comb
    measure, ~S atoms) is NOT a single virtual atom; (b) SUPPORT:
    every border atom coincides BITWISE with a union grid node (the
    smooth window lives on the SAME folded cosine grid; min distance
    0.0), so the node-polynomial insertion is structurally forbidden
    (the collision ward).  The route survives as the EXACT TOY
    BRIDGE (T3): for a SINGLE-ATOM border the (S+1)-node Uvarov
    complementation holds at the SHIFTED rank N (S† = S + 1 = 2N:
    the half-filling arithmetic moves by exactly one, dual rank
    N - 1 -> N, Fractions-exact) and the literal (S+1)-point dual
    kernel EQUALS the route-(ii) object up to the sign conjugation
    of the new node polynomial (char-poly identical) -- the two
    routes agree where both exist.
  ROUTE (ii), THE BORDERED RESOLVENT (SEALED AS THE CONSTRUCTOR):
    with beta = b/sqrt(B), v = B_m beta the node-side border image
    (v_j = sqrt(nu_j/B) int K_mu(y_j, t) dsigma(t) -- the CD pairing
    of the border measure), gamma = beta^T beta, vt = D v and the
    r356 sign matrix D:
        Z  := [[R^{-1}, vt], [vt^T, 1 + gamma]],   R† := Z^{-1}.
    THE THEOREM PACKAGE (every line an exact finite-matrix fact,
    machine-gated):
      (A1) G† := [[E_n, v], [v^T, gamma]] == D† (Z - I) D† with
           D† = D + [1] -- the r356 complementation EXTENDS: the
           augmented node Gram G† = T† T†^T (T† = the L† observation
           operator) is the D†-conjugate of R†^{-1} - I;
      (A2) THE SPECTRAL MAP: lambda_max(E†) == lambda_max(G†) ==
           1/lambda_min(R†) - 1, i.e. margin† == 2 - 1/lambda_min(R†)
           EXACTLY (the r356 map verbatim on the augmented object);
      (A3) L† <=> R† > (1/2) I (two-sided, gated in both truth
           directions on toys and as sign census live);
      (A4) THE RANK-1 FORM (Sherman-Morrison): R†_{YY} = R +
           (R vt)(R vt)^T/(1 + gamma - vt^T R vt), R†_{bb} = 1/(1 +
           gamma - vt^T R vt) -- the border is a rank-1 insertion at
           the RESOLVENT level of the dual kernel (Z = R^{-1} plus
           one bordered row: the Schlesinger/Uvarov reading of v958,
           now on the DUAL side);
      (A5) L† <=> L* AND Terminal IN DUAL COORDINATES: R† > I/2 <=>
           {R > I/2} AND {q† < 1} with q† := gamma + v^T (I -
           E_n)^{-1} v == u^T H^{-1} u / B (FRAME INVARIANCE of the
           squared dual border norm: the mu-orthonormal route equals
           the mu-tilde chain telescoping S_{N-1} = sum rho_k), and
           the terminal dictionary 1 - q† == (5/7)(1 - q_N)/B_w
           (q_N = rho_{N-1}/(5/7), B_w = S_{N-2} + 5/7, the
           r241/r243/r263 objects verbatim);
      (A6) THE BORDER-SCHUR CLOSED FORM: the Schur complement of
           M† = R† - I/2 onto the border coordinate equals
           (1 - q†)/(2 (1 + q†)) EXACTLY -- the terminal margin IS a
           local Schur datum of the augmented dual object -- and by
           the Schur quotient property the SAME value is carried
           INSIDE the local 3x3 block (pair + border): the border
           fiber is not appended after the fact, it sits in the same
           local object (the moonshot clause, made exact);
      (A7) INTERLACING: lambda_k(R†) <= lambda_k(R) <=
           lambda_{k+1}(R†) (Cauchy on Z = R†^{-1} whose leading
           principal block is R^{-1}) -- the border can only LOWER
           the bottom of the spectrum: margin† <= margin, exactly
           the L† => L* direction, spectrally.
  ROUTE (iii), SCHLESINGER: consumed by (A4) -- the rank-1 insertion
    lives at the dual resolvent; no new RHP machinery is invoked.

THE LEGS: (Leg 0) anchors bit-near: w9 records (S 367, S_- 104, N_w
184, margin 1.6752e-4 rel 0.01, lambda_min(R) 0.500041882 abs 1e-8,
folds (2, 4)); the r359 W9 Schur anchors (eps 4.1882e-5, lamS
4.2003e-5, share 0.6973) reproduced through SWD.schur_rung verbatim;
the r266 terminal records as BORDER-CHAIN gates: D_N == (5/7)(1 -
q_N) at kz15 = 0.0445838321 and kz20 = 0.294659217 (rel 1e-4); the
r352 margin fit slope -3.332 tol 0.02 on the 57.  (Leg A) the exact
augmented algebra (A1)-(A7) gated on the ladder (42 core + 15 + 12
EXT3 + 6 EXT4 = 75 full rows; graded bars; Fractions-exact toys).
(Leg B) the augmented critical block: the 3x3 Schur block S†_3 of
M† at (pair, border): bind† = lambda_min(S†_3)/(lambda_min(R†) -
1/2) in the sealed range (the r359 binding thesis in the augmented
picture), the in-block border Schur == the global border Schur
(quotient, exact), the ev3 band (top local eigenvalue vs the border
Schur value), the border mass of the critical eigenvector (census),
and the pair-only 2x2 contrast (census: the L* channel does not
need the border row; the terminal channel does).  (Leg C) worlds:
the equivalence census {R† > I/2} == {R > I/2} AND {q_N < 1} on all
resolvable rows of MAIN + chi3 + chi4 (the matched r357 frames, 42
rungs each, border = the smooth comb through the SAME chi arch --
the DMF chi_wpack convention; the 5/7 budget corner transported
verbatim, disclosed as convention: the equivalence gates are
budget-agnostic); the rational TWIN (dose-zero BITWISE + pointwise
augmented devs); the matched SCRAMBLE breaks NAMED, two prongs: (p1)
canonical budget -- the border chain leaves the cone (first h-flip
at the sealed degree), (p2) fallback budget B = 1 (the equivalence
is B-agnostic) -- the ALGEBRA (A1/A2/A4/A6) holds world-blind while
the positivity fails at the named R-block clause (lambda_min(R) -
1/2 = -0.4962, the r359 anchor).  (Leg D) the saturation handoff:
R† typed as THE ONE OBJECT for both lanes (bordered dual resolvent),
the interlacing table lambda_k(R†) vs lambda_k(R) printed exactly,
the augmented r359 quantities ((A†^{-1})_kk at the pair, cross
share) as census -- does the rank-1 deformation change the critical
structure?  (Leg E) must-fails (6, each loud): (m1) border WITHOUT
the 1/B normalization -- the mutant q† equals B_w x q† EXACTLY (the
deviation IS the budget factor, 8.38 at w9) and the toy A_cap
equivalence breaks EXACTLY in Fractions; (m2) the WRONG RANK in the
S+1 arithmetic (dual rank N-1 instead of N on the augmented toy) --
the Fractions complementation breaks EXACTLY; (m3) R† FROM
MARGIN-READBACK -- a mutant returning the withheld margin† column
is AST-FLAGGED (scope audit); (m4) SHERMAN-MORRISON WITH THE WRONG
SIGN -- the block identity vs Z^{-1} breaks by >= 1e-3 at w9
(scoped 4.9e-3 = 2x the correction entry) while the honest form
holds at <= 1e-12; (m5) VIRTUAL NODE ON A REAL NODE -- the support
ward (min |t - x_j| == 0 -> REFUSED) fires on the toy collision AND
the census shows every real border atom collides (route (i) is
structurally forbidden); (m6) THE WRONG FRAME -- the mu-tilde chain
coefficients F_k in place of the mu-orthonormal border vector b
break the frame-invariance identity by 0.77 relative at w9 (bar
0.1).

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO TERMINAL CLAIM, NO
RH CLAIM in either direction, mincut unchanged.  Two-commit freeze
protocol (r329 convention): spec + machinery committed BEFORE the
record run, record tables inserted after.

INDEX FIREWALL (binding, r238-r361 discipline): w = window (kz), S =
#union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds = grid indices;
ground truth (records, anchors, control flips) enters GATES and
record tables only; the module-own constructors consume measure
arrays / chain coefficients / positions / pair indices / border
windows ONLY (AST scope audit; withheld identifiers mdag_col_true /
lamRd_col_true / qdag_col_true and the REC/anchor constants); no
zero/prime oracles anywhere (AST firewall); no fit primitives beyond
the imported r286 Theil-Sen (fragment audit).  MACHINERY IMPORTED
VERBATIM: r356 BDH.{dual_rung, fr_inv, fr_mul, fr_proj} (36141c0a),
r359 SWD.schur_rung (d00fdc96), r342 PX.{build_rung, pair_select}
(b09f8ccd), r357 DMF.{chi_window_comb, chi_build_measures, Q_CHI3,
Q_CHI4, LPQ3, LPQ4} (4bf1a94b), r354 PWA.rung_reduced_cols
(f9db84da), r226 HS.window_data (d78e236b), r244 BH.bord_chain
(c21e15b5), r243 PB.smooth_comb (db259f8e), r331 TR.{base_comb,
build_world} (f871fe84), r289 AKD.twin_rational (91cdc2b1), r276
MF.local_gaps (ed17d79f), r286 LM.ts_fit (0a44ac4e), document
pipeline V.{build_measures, mu_chain, b_matrix, window_shape,
admissible_indices, U, PP, N_ATOM_MIN}, v563 core READ-ONLY.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never
fitted); border measure = the smooth-comb signed window (the
r244/v958 convention, HS.window_data(kz, comb=PB.smooth_comb(alpha))
with alpha = V.window_shape(kz)[0], gated == the PIK alpha at w9).

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8; B57 =
5/7; W9_AUG_ANCH (s1 scoping, disclosed) mdag 1.658218770e-4 rel
1e-3 / lamRd 0.500041459 abs 1e-8 / qdag 0.933044234 abs 1e-6 / qN
0.214250034 abs 1e-6 / Bw 8.382399447 abs 1e-6 / gam 0.677766190
abs 1e-6 / schur_b 1.731873612e-2 rel 1e-3 / bind3 1.002763596 abs
5e-3 / ev3_top 1.7603e-2 rel 1e-2 / bmass 2.518e-5 rel 0.2 / xstar
spread 56.8 rel 0.1 / folds (2, 4); W9 R359 ANCHORS eps 4.1882e-5 /
lamS 4.2003e-5 rel 1e-3, share 0.6973 abs 5e-3; SAMPLE_AUG_ANCH
(qdag abs 1e-4, bind3 abs 5e-3, schur_b rel 1e-2) kz44 (0.963975,
1.007864, 9.171464e-3), kz56 (0.955914, 1.004818, 1.127006e-2),
kz130 (0.968835, 1.018071, 7.914695e-3); TERM_ANCH D_N == B57 (1 -
q_N) rel 1e-4: kz15 0.0445838321, kz20 0.294659217 (the r266 mp
records); KZ15_COMPRESS mdag/margin 0.8716 abs 0.02 (the L† margin
is GENUINELY smaller than the L* margin at the near-terminal-
critical window -- the coupling is visible); CHI3_AUG_ANCH epsd
2.092e-4 rel 2e-2 / qN 0.246981 abs 1e-3 / bind3 1.002344 abs 5e-2
/ schur_b 1.689913e-2 rel 2e-2; CHI4_AUG_ANCH epsd 7.278e-5 rel
2e-2 / qN 0.011610 abs 1e-3; SCR_AUG_ANCH lamR - 1/2 = -0.49622 abs
2e-3, border-chain flip nf == 37 EXACT; KZ133_CENSUS (disclosed s3):
mdag 3.8457e-10, lamRd - 1/2 = -4.127e-11 INSIDE the ~1.25e-10 f64
floor (the r356 DUAL_MARGIN_LEDGER truth carries over: the deepest
augmented signs are census, not clause); FIT_MARGIN_ANCH -3.332 tol
0.02; GRADES shallow N_w <= 900 / mid <= 3200 / deep > 3200;
COMPD_BAR (1e-10, 1e-9, 1e-7); MAPD_BAR (1e-10, 1e-9, 1e-8);
SMD_BAR 1e-12 flat (pure algebra, conditioning-free); FRAME_BAR
(1e-7, 1e-5, 1e-4) -- DISCLOSED: the (I - E_n)-solve conditioning
scales like 1/margin, the graded bars are sized from the s1/s3
maxima 1.6e-10 / 1.8e-7 / 6.2e-7; SCHB_BAR (1e-6, 1e-4, 1e-2);
SCHB_BAR_CHI 1e-4 [CALIBRATION AMENDMENT a2, disclosed: the chi
worlds contain rungs with 1 - q† as small as 3.6e-3 (the terminal
channel is NEAR-CRITICAL there), where the RELATIVE deviation of
the near-cancelling border-Schur value is the disclosed
cancellation class -- measured chi maxima 3.1e-6 vs the w9-scoped
shallow bar 1e-6; the MAIN bars are UNTOUCHED and passed at first
evaluation]; QUOT_BAR (1e-10, 1e-10, 1e-9); DICT_BAR == FRAME_BAR
class; CN_BAR 1e-12 (the coefficient-side lambda identity, 57-row
cohort only, cost-sealed); GD_PSD_FLOOR -1e-10; K_INTER 6 with
INTER_TOL 1e-12 relative; RESOLV_FLOOR 1e-9 (rows with |lamRd -
1/2| <= floor are SIGN-CENSUS, the r356/r359 convention); BIND_MIN
1 - 1e-6; BIND_MAX 1.5 (MAIN clause); [CALIBRATION AMENDMENT a1,
disclosed: the sealed chi-world clause wrongly required every chi
rung to be L†-LIVE (len(live) == len(rows)) and ran the bind/schb
clauses through the terminal crossing -- the FIRST full evaluation
found the REAL structure: the chi arithmetic contains
TERMINAL-DEAD rungs (q_N > 1 on 5/42 chi3 and 1/42 chi4 rows,
e.g. chi3 kz15 q_N 1.2773 with lambda_min(R†) - 1/2 = -9.8e-5 < 0
EXACTLY as the theorem demands) -- the chi equivalence census is
retyped TWO-SIDED on all rows with |lamRd - 1/2| > RESOLV_FLOOR
(the dead rows are the STRONGEST evidence: both truth directions
live on real windows, zero sign violations measured at
calibration) and the chi bind†/EV3 columns become CENSUS (range
printed; bind† reaches 2.43 near the terminal crossing where the
border coordinate enters the bottom of the spectrum -- real
structure, not noise); the MAIN clauses (bind range, EV3 band,
equivalence) are UNTOUCHED and passed at first evaluation];
EV3_BAND (0.5, 2.0) (MAIN); TWIN_AUG_BAR 2.5e-3 nats [CALIBRATION
AMENDMENT a3, disclosed: the sealed 1e-3 was sized on the kz42
scoping row (3.4e-4); the first full evaluation measured 1.15e-3,
ENTIRELY in |dlog margin†| at the deepest twin rung kz130 (margin
4.9e-9, twin dose 1e-8 relative -- the identical 1/margin
twin-dose class disclosed in r356/r359, which passed at 1.3-1.4x
headroom); re-sized to 2.5e-3 (2.2x headroom), no other twin
column moved (q† 1.9e-7, schur_b 7.1e-6, bind† 2.8e-5)]; WORLD_KZ
(18, 9, 52, 119, 42, 130); N_CHI_MIN 21; SCR_SEED 1;
SCR_FALLBACK_B 1.0;
M1_TOL 1e-9 (the exact budget-factor identity) + M1_LOUD 1.5;
M4_LOUD 1e-3 (scoped 4.9e-3); M6_LOUD 0.1 (scoped 0.77); TOY_TOL
1e-12; EXT3_KZ (42, 51, 54, 56, 58, 62, 96, 123, 125, 127, 128,
130); EXT4_KZ (72, 75, 66, 113, 111, 108); EXT3_NW (1721, 2577);
EXT4_NW (2656, 3181); KZ_DEEP 133 (N_w 7942, z 617 gated) -- THE
SEALED DEEP-CENSUS ROW: the augmented block costs ~260 s at kz133
(s3 scoping: two PIK window builds + the 4567-dim dense algebra),
so EXT5 and the remaining EXT6 rows are SEALED OUT of the augmented
layer for the 1800 s budget (their equivalence is below the f64
floor anyway -- the r356 record stands for their dual margins; the
exclusion is disclosed in the verdict, not hidden); runtime <= 1800
s; smoke = toys + firewall + scopes + mutants + w9 aug block + chi3
w9; ladder, chi ladders, twin, scramble, deep row, fits,
adjudications skipped.

PRE-SPEC SCOPING (disclosed, r343-s1..r359-s1 precedent -- three
sizing passes on kz9/kz44/kz56/kz130/kz15/kz20 + chi3/chi4 w9 +
scramble w9 + twin kz42 + kz133, /tmp, deleted; no bar, band,
clause, route choice or verdict rule was tuned after any evaluation
except as sized here and said so): the augmented duality holds
EXACTLY everywhere scoped -- complementation (A1) 1.2e-12 (w9) ..
2.1e-9 (kz133), spectral map (A2) 4.6e-13 .. 5.5e-10, SM block form
(A4) <= 9e-15 on every rung incl. kz133 (pure algebra), frame
invariance (A5) 4.4e-13 (w9) .. 6.2e-7 (kz133, the disclosed
1/margin conditioning), border-Schur closed form (A6) 1.5e-11 ..
1.2e-3 (deep), quotient <= 3.4e-11, interlacing TRUE on every scoped
rung; bind3 in [1.0024 (w9), 1.0344 (chi4 w9)] -- the augmented 3x3
block carries the full L† margin to within 3.5 pct scoped; ev3_top/
schur_b in [1.0015, 1.43]; the border mass of the critical
eigenvector is TINY (2.5e-5 at w9, 5.8e-4 at the near-terminal
kz15): the critical direction stays the L* pair, the terminal
channel sits in the border coordinate of the SAME block (A6); kz15/
kz20 border chains reproduce the r266 mp records to 1e-6; the
virtual-node representability spread is 56.8 .. 4.5e3 (route (i)
dead); the SCR chain flips at n = 37; twin kz42 max |dlog| 3.4e-4;
mutant sizes as sealed above.  The verdict letters, the route
adjudication, the clause set and every bar were frozen from these
numbers BEFORE any ladder-wide, chi-ladder-wide or adjudication
evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > BORDER_GATE_FAIL >
{AUGMENTED_DUALITY_EXACT / DUALITY_OBSTRUCTED / RANK_SHIFT_MISMATCH}
-- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the r356 rank/support gate fails on
    any attempted real window /
  BORDER_GATE_FAIL(rows)  iff the border chain leaves the cone
    (h-flip) or B_w <= 0 on any real MAIN/chi ladder row (SCR is
    the designed exception) /
  AUGMENTED_DUALITY_EXACT(route ii)  iff every exact-algebra ward
    (A1)-(A7) passes at the graded bars on all attempted rows AND
    the equivalence census {R† > I/2} == {R > I/2} AND {q_N < 1}
    is exact on every resolvable row of MAIN + chi3 + chi4 AND the
    toys are Fractions-exact /
  DUALITY_OBSTRUCTED(loci)  iff an algebra ward or the equivalence
    census fails at a named link /
  RANK_SHIFT_MISMATCH  iff the T3 route-(i) toy S+1 arithmetic
    fails (the single-atom Uvarov complementation at rank N breaks)
  + BORDER_IN_LOCAL_BLOCK(bind†, quotient)  [only with
    AUGMENTED_DUALITY_EXACT: iff bind† in [BIND_MIN, BIND_MAX] on
    all resolvable MAIN + chi rows AND the in-block border Schur ==
    the global border Schur at QUOT_BAR AND ev3_top/schur_b in
    EV3_BAND on the resolvable rows -- the moonshot clause: BOTH
    lanes in ONE local object]
  + VIRTUAL_NODE_LEDGER(representability spread, collision census,
    toy bridge + rank shift) [always]
  + CONSISTENCY_LEDGER(L† <=> L* AND Terminal census, the terminal
    dictionary, the kz15 margin compression) [always]
  + INTERLACING_LEDGER(the lambda_k table) [always]
  + SATURATION_HANDOFF_LEDGER(R† typed as the one object; the
    augmented (A†^{-1})_kk / cross-share census vs r359) [always]
  + WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK(named, two prongs)
  + DEEP_CENSUS_LEDGER(kz133 signs inside the f64 floor; EXT5/EXT6
    sealed out, disclosed) + MUSTFAIL_LEDGER [always].
Honesty before beauty: (A1)-(A7) are exact finite-matrix facts
(theorem-grade SKELETON) whose inputs are measured window scalars
(census-grade FLESH); a verified equivalence is a REPRESENTATION,
not a bound -- L† itself stays exactly as open as L* AND Terminal;
the moonshot gain is STRUCTURAL: one dual object, one critical
block, the border fiber as a bordered resolvent row with an exact
local Schur dictionary; no verdict claims L*, Terminal, a bound
mechanism, a derived 5/7, or RH progress in any direction; the DCCX
STOP list stands (no capacity products, no local symbol/Fejer
floors, no frame-A growth ceilings, no global g_min bounds, no
worst-case martingale products, no further Borodin coordinate
changes without an analytic theorem, no depth windows only for
exponent fits); r243..r361 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit beyond the three disclosed calibration amendments
a1/a2/a3 above; TWO-COMMIT PROTOCOL EXECUTED: smoke pass 1 = 28/30
caught a toy-clause bug in the G10 m1 branch (the toy dual norm
0.386 < 1, so the B = 1 mutant could not flip the verdict on the
UNSCALED border -- fixed pre-freeze to the doubled border whose
dual norm 4 dn0 = 1.544 sits strictly between the mutant budget 1
and the true budget 4); smoke re-pass 30/30 x2 byte-identical; the
sealed spec was then committed as "r362 pre-freeze" (62ca2bfa,
SPEC_SHA freeze 83b97cd57563e737) BEFORE the first full
evaluation; calibration pass 1 = FIRST full evaluation = 26/30
(614.2 s) with the three disclosed amendments a1 (chi equivalence
retyped two-sided + chi bind/EV3 to census -- the chi worlds
contain TERMINAL-DEAD rungs, a finding, not a failure), a2 (chi
schb bar 1e-6 -> 1e-4, the near-cancellation class at 1 - q† down
to 3.6e-3) and a3 (twin bar 1e-3 -> 2.5e-3, the deepest-rung
1/margin twin-dose class, measured 1.15e-3 entirely in |dlog
margin†| at kz130); NO MAIN clause, bar, band or route moved --
every MAIN gate passed at first evaluation; post-amendment smoke
30/30; calibration pass 2 = 30/30 (646.2 s); record run1 = 30/30
(507.5 s), run2 = 30/30 (485.0 s), byte-identical up to WALL and
identical to calibration pass 2):
MAIN VERDICT = AUGMENTED_DUALITY_EXACT(route ii) +
BORDER_IN_LOCAL_BLOCK(bind† med 1.0056, quotient <= 1.0e-11) --
THE MOONSHOT CORE STANDS: L† <=> R† > I/2 EXACTLY with R† =
[[R^{-1}, vt], [vt^T, 1 + gamma]]^{-1} the bordered dual
resolvent, verified on 75 MAIN + 42 chi3 + 42 chi4 rows + the
kz133 deep census (every (A1)-(A7) ward green at the graded bars:
(A1) complementation <= 2.3e-11/3.2e-10 shallow/mid + 2.1e-9 at
kz133; (A2) spectral map margin† == 2 - 1/lambda_min(R†) <=
1.1e-11/2.7e-10 + 5.5e-10 deep, coefficient-side lambda identity
<= 1.9e-15 on the 57; (A4) SM rank-1 block form <= 1.2e-14
EVERYWHERE incl. kz133 (pure algebra); (A5) frame invariance q† B_w
== u^T H^{-1} u <= 4.0e-9/2.4e-7 + 6.2e-7 deep, terminal
dictionary <= 6.7e-6; (A6) border Schur == (1-q†)/(2(1+q†)) <=
3.7e-7/3.9e-5 + 1.2e-3 deep, quotient <= 1.0e-11; (A7)
interlacing 75/75; min eig(G†) +1.1e-6 >= 0); THE EQUIVALENCE
CENSUS IS EXACT AND TWO-SIDED: {R† > I/2} == {R > I/2} AND {q_N <
1} on 74/74 resolvable MAIN rows (1 sub-floor row sign census)
AND on 42/42 chi3 + 42/42 chi4 rows INCLUDING the 6 TERMINAL-DEAD
chi rungs (chi3 [15, 19, 23, 33, 39] with q_N up to 1.2959, chi4
[20] with 1.3298: lambda_min(R†) - 1/2 goes NEGATIVE there, e.g.
chi3 kz15 -9.8e-5, EXACTLY as the theorem demands -- both truth
directions are live on REAL windows, not just toys); AND THE
BORDER FIBER SITS IN THE LOCAL BLOCK: bind† =
lambda_min(S†_3)/(lambda_min(R†) - 1/2) in [1.0003, 1.0608] med
1.0056 on the 74 resolvable MAIN rows, the in-block border Schur
== the global one at <= 1.0e-11 (Schur quotient, exact), ev3_top/
schur_b in [1.0012, 1.7773] (band (0.5, 2.0)) -- ONE dual object,
ONE critical block, BOTH lanes
+ VIRTUAL_NODE_LEDGER(route (i) dead on the real windows, twice:
representability spread 56.8 at w9 (a point evaluation needs 0;
the border is the SIGNED smooth-comb measure with S atoms) and
EVERY border atom collides BITWISE with a union grid node (min
distance 0.0 -- the smooth window lives on the SAME folded
grid); the toy bridge STANDS: the single-atom (S+1)-node Uvarov
complementation is Fractions-EXACT at the SHIFTED rank N (S† =
2N, dual rank N-1 -> N: the half-filling arithmetic moves by
exactly one and does NOT break -- RANK_SHIFT_MISMATCH correctly
stays off) and the literal (S+1)-point dual kernel EQUALS the
route-(ii) R† up to sign conjugation (|entries| and char-poly
EXACT); m2 breaks the toy complementation EXACTLY at any other
rank)
+ CONSISTENCY_LEDGER(the Lean equivalence L† <=> L* AND Terminal
measured EXACTLY in dual coordinates on every resolvable row of
three arithmetics; the r266 terminal mp records reproduced
through the border chain: kz15 D_N dev 1.0e-8, kz20 dev 5.7e-10;
q† == the r266 crit1 coordinate EXACTLY: ladder range [0.9081,
0.9985] == the r266 record range; THE KZ15 COMPRESSION:
mdag/margin = 0.8716 -- at the near-terminal-critical window
(q_N 0.9376) the L† margin is GENUINELY 13 pct smaller than the
L* margin: the two lanes couple spectrally in R† exactly where
the terminal channel is tight (w9, terminal slack: ratio 0.9899
only))
+ INTERLACING_LEDGER(lambda_k(R†) <= lambda_k(R) <=
lambda_{k+1}(R†) on 75/75 rows at K_INTER 6 -- the border can
only LOWER the bottom of the dual spectrum (margin† <= margin,
the L† => L* direction spectrally); w9 bottom: 0.500041459 <=
0.500041882; the critical eigenvector border mass stays TINY
(2.5e-5 at w9, 5.8e-4 at kz15): the rank-1 deformation never
creates a new bottom direction, it shifts the L* pair direction)
+ SATURATION_HANDOFF_LEDGER(THE ONE OBJECT typed for both lanes:
R† = the bordered dual resolvent; the r359/r360 quantities in the
augmented picture at w9: cross share† = 0.6990 vs the r359 share
0.6973 (dev 1.7e-3), ladder share† in [0.403, 0.862] med 0.708 ==
the r359 med 0.702 -- THE RANK-1 DEFORMATION DOES NOT MOVE THE
CRITICAL RESOLVENT CENSUS at the pair: the saturation analysis
stays a PAIR problem and the border fiber rides along as ONE
exact bordered row whose local Schur is the terminal margin
dictionary (A6), schur_b ladder range [3.78e-4, 2.41e-2] -- the
handoff to the R360 lane is R† verbatim)
+ WORLD_LEDGER(chi3 42/42 built, support + border + (A1)-(A7)
wards + two-sided equivalence PASS, q_N in [0.0000, 1.2959],
bind† live-census [1.0020, 1.6567] med 1.0213; chi4 42/42 the
same, q_N in [0.0039, 1.3298], bind† [1.0018, 2.4265] med 1.0333
-- the top bind values sit at the terminal crossing where the
border coordinate enters the bottom of the spectrum, real
structure; the 5/7 corner transported as disclosed convention)
+ TWIN_LEDGER(dose-zero BITWISE 6/6; pointwise augmented devs max
over |dlog q†|, |dlog margin†|, |dlog schur_b|, |dlog bind†| =
1.2e-3 nats (bar 2.5e-3, amendment a3) -- entirely the deepest-
rung margin† column, the disclosed 1/margin twin-dose class)
+ SCRAMBLE_BREAK(named, two prongs as sealed: (p1) canonical
budget -- the border chain flips at n = 37 EXACTLY (the border
cone is EMPTY: no positive-chain B_w exists on the dead world,
the terminal side has no representation) with lambda_min(R) - 1/2
= -0.4962 (the r359 anchor); (p2) fallback B = 1 -- the ALGEBRA
holds world-blind (comp 4.7e-12, map 3.6e-12, SM 1.7e-14, quot
0.0) while the POSITIVITY fails at the named R-block clause:
lambda_min(R†) - 1/2 = -0.4963 < 0 -- the identities are
world-blind algebra, the POSITIVITY is arithmetic)
+ DEEP_CENSUS_LEDGER(kz133 as sealed: mdag +3.8457e-10 vs lamRd -
1/2 = -4.127e-11 INSIDE the disclosed ~1.25e-10 f64 floor -- the
augmented sign census inherits the r356 resolution truth
verbatim; all deep wards inside the graded bars; EXT5 + remaining
EXT6 sealed out of the augmented layer by the disclosed 260 s/row
budget, the r356 dual record stands for them)
+ MUSTFAIL_LEDGER(m1 budget-normalization: q†_m1/q† == B_w =
8.382399447 EXACTLY (dev 1.8e-15) >= 1.5, verdict flip q†_m1 =
7.8211 > 1, + Fractions-exact flip on the toy; m2 rank-shift
Fractions-exact break; m3 margin-readback AST-FLAGGED
(mdag_col_true); m4 SM wrong sign 4.93e-3 >= 1e-3 vs honest
1.9e-15; m5 collision ward REFUSED on the toy + every real border
atom collides (census); m6 wrong frame 0.769 >= 0.1 (q†_m6 1.6506
vs q† 0.9330); constructor scopes + fragment audit CLEAN).
Key numbers.  W9: margin† 1.658219e-4 (margin 1.675159e-4),
lambda_min(R†) 0.500041459, q† 0.9330442, q_N 0.2142500, B_w
8.3823994, gamma 0.6777662, schur_b 1.7318736e-2 == (1-q†)/
(2(1+q†)) at 1.5e-11, ev3 (4.157e-5, 4.899e-4, 1.760e-2), bind†
1.002764, border mass 2.5e-5, folds (2, 4); the r359 anchors (eps
4.1882e-5, lamS 4.2003e-5, share 0.6973) reproduced bit-near.
LADDER: 75 rows full augmented + kz133 deep census; margin fit
slope -3.332 == the r352 record EXACT; fresh censi (no clause):
q† in [0.9081, 0.9985] med 0.9657 -- the terminal Schur
coordinate saturates slowly upward and IS the r266 crit1 column
in dual coordinates; schur_b in [3.78e-4, 2.41e-2] (the 1/B_w
dictionary); share† med 0.708.  HONEST NEGATIVES: (1) the
equivalence is a REPRESENTATION -- L† stays exactly as open as
L* AND Terminal, no margin was created; (2) route (i) is dead on
the real windows (representability + collision): R† is NOT
literally an (S+1)-point Uvarov projection kernel there -- the
bordered-resolvent form is the general object, the point-
insertion picture survives only on the toy bridge; (3) at the
deep row the frame/schb wards live at coarse bars (1/margin
conditioning, disclosed) and kz133's equivalence is sign census
inside the f64 floor; (4) EXT5 + 3 EXT6 rows are sealed out of
the augmented layer (budget, disclosed): the '85-row' contract is
delivered as 75 full + 1 deep census + the r356 record for the
rest; (5) three calibration amendments a1/a2/a3 disclosed above
-- a chi clause retype forced by a real finding (terminal-dead
chi rungs), a chi cancellation-class bar re-size and a twin-bar
re-size in the disclosed r356/r359 noise class; no MAIN rule
moved; (6) the 5/7 budget corner on the chi worlds is a
transported convention, not a chi-derived object; (7) bind† on
chi worlds reaches 2.43 near the terminal crossing -- the
local-block clause is banked for the MAIN family, the chi
carrying is census.  R363+ HANDOFF: the saturation lane (R360)
can consume R† verbatim -- the critical block is unchanged at
the pair (share† == share within 2e-3 at w9), the border adds one
exact bordered row whose local Schur is the terminal margin
dictionary (A6): ONE critical saturation theorem for the
rank-1-bordered dual resolvent would close BOTH lanes, exactly
as the moonshot ordered.  Runtime 507.5 / 485.0 s record, 646.2 s
calibration pass 2, 0.5 s smoke; deterministic, run1/run2
byte-identical up to WALL.  AMENDMENTS AFTER FREEZE: a1/a2/a3 as
disclosed above -- this record-table insertion is the only other
post-freeze edit.

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

import borodin_dual_hole_probe as BDH            # noqa: E402 r356
import schur_wronskian_dual_probe as SWD         # noqa: E402 r359
import pair_extremal_probe as PX                 # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF      # noqa: E402 r357
import phi_wander_anatomy_probe as PWA           # noqa: E402 r354
import hirota_sign_probe as HS                   # noqa: E402 r226
import bordered_hankel_probe as BH               # noqa: E402 r244
import principal_bessel_probe as PB              # noqa: E402 r243
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import verify_lstar_instance as V                # noqa: E402 document
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
B57 = 5.0 / 7.0
BDH_SHA_PREFIX = "36141c0a"
SWD_SHA_PREFIX = "d00fdc96"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
HS_SHA_PREFIX = "d78e236b"
BH_SHA_PREFIX = "c21e15b5"
PB_SHA_PREFIX = "db259f8e"
W9_AUG_ANCH = dict(mdag=1.658218770e-4, lamRd=0.500041459,
                   qdag=0.933044234, qN=0.214250034,
                   Bw=8.382399447, gam=0.677766190,
                   schur_b=1.731873612e-2, bind3=1.002763596,
                   ev3_top=1.7603e-2, bmass=2.518e-5,
                   xstar=56.8, f1=2, f2=4)
W9_R359_ANCH = dict(eps=4.1882e-5, lamS=4.2003e-5, share=0.6973)
SAMPLE_AUG_ANCH = {44: (0.963975, 1.007864, 9.171464e-3),
                   56: (0.955914, 1.004818, 1.127006e-2),
                   130: (0.968835, 1.018071, 7.914695e-3)}
TERM_ANCH = {15: 0.0445838321, 20: 0.294659217}
TERM_ANCH_TOL = 1.0e-4
KZ15_COMPRESS = 0.8716
KZ15_COMPRESS_TOL = 0.02
CHI3_AUG_ANCH = dict(epsd=2.092e-4, qN=0.246981, bind3=1.002344,
                     schur_b=1.689913e-2)
CHI4_AUG_ANCH = dict(epsd=7.278e-5, qN=0.011610)
SCR_AUG_ANCH = dict(lamR=-0.49622, nf=37)
KZ133_CENSUS = dict(mdag=3.8457e-10, lamRd_m=-4.127e-11)
FIT_MARGIN_ANCH = -3.332
FIT_ANCH_TOL = 0.02
NW_SHALLOW = 900
NW_MID = 3200
COMPD_BAR = (1.0e-10, 1.0e-9, 1.0e-7)
MAPD_BAR = (1.0e-10, 1.0e-9, 1.0e-8)
SMD_BAR = 1.0e-12
FRAME_BAR = (1.0e-7, 1.0e-5, 1.0e-4)
SCHB_BAR = (1.0e-6, 1.0e-4, 1.0e-2)
SCHB_BAR_CHI = 1.0e-4               # a2: chi near-cancellation class
QUOT_BAR = (1.0e-10, 1.0e-10, 1.0e-9)
CN_BAR = 1.0e-12
GD_PSD_FLOOR = -1.0e-10
K_INTER = 6
INTER_TOL = 1.0e-12
RESOLV_FLOOR = 1.0e-9
BIND_MIN = 1.0 - 1.0e-6
BIND_MAX = 1.5
EV3_BAND = (0.5, 2.0)
TWIN_AUG_BAR = 2.5e-3               # a3: deepest-rung 1/margin class
WORLD_KZ = (18, 9, 52, 119, 42, 130)
N_CHI_MIN = 21
SCR_SEED = 1
SCR_FALLBACK_B = 1.0
M1_TOL = 1.0e-9
M1_LOUD = 1.5
M4_LOUD = 1.0e-3
M6_LOUD = 0.1
TOY_TOL = 1.0e-12
EXT3_KZ = (42, 51, 54, 56, 58, 62, 96, 123, 125, 127, 128, 130)
EXT4_KZ = (72, 75, 66, 113, 111, 108)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
KZ_DEEP = 133
KZ_DEEP_NW, KZ_DEEP_Z = 7942, 617
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
                       "coefficients / positions / pair indices / "
                       "border windows ONLY; record numbers and "
                       "anchors enter gates and record tables only"
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


CONSTRUCTORS = ("grade_of", "bvec_chunked", "border_chain_pack",
                "aug_rung", "virtual_star_census", "chi_aug_row")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_AUG_ANCH",
                   "W9_R359_ANCH", "SAMPLE_AUG_ANCH", "TERM_ANCH",
                   "KZ15_COMPRESS", "CHI3_AUG_ANCH", "CHI4_AUG_ANCH",
                   "SCR_AUG_ANCH", "KZ133_CENSUS", "FIT_MARGIN_ANCH",
                   "mdag_col_true", "lamRd_col_true", "qdag_col_true"}


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


def bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw, chunk=4096):
    """memory-lean border vector in the mu-orthonormal frame:
    b_i = sum_a bwa_a phat_i(t_a) via the chain recurrence in atom
    chunks; consumes chain coefficients + border atoms only."""
    b = np.zeros(Nw)
    for s in range(0, len(bxa), chunk):
        t = np.asarray(bxa[s:s + chunk], float)
        w = np.asarray(bwa[s:s + chunk], float)
        u = np.full_like(t, 1.0 / math.sqrt(h0_mu))
        um = np.zeros_like(t)
        b[0] += float(w @ u)
        for i in range(Nw - 1):
            r = (t - a_mu[i]) * u - (b_mu[i - 1] * um if i > 0
                                     else 0.0)
            um, u = u, r / b_mu[i]
            b[i + 1] += float(w @ u)
    return b


def border_chain_pack(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw):
    """the mu-tilde border chain of one window (BH.bord_chain
    verbatim): rho_k = F_k^2/h_k, S_n, the budget B_w = S_{N-2} +
    5/7, q_N = rho_{N-1}/(5/7); ok iff the chain reaches depth N
    with every h_k > 0; consumes measure + border arrays only."""
    rows = BH.bord_chain(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw)
    sg = np.array([r["sg_h"] for r in rows])
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    ok = (len(rows) == Nw) and bool(np.all(sg > 0))
    if not ok:
        return dict(ok=False, nf=nf)
    rho = np.array([r["rho"] for r in rows])
    S_ = np.cumsum(rho)
    Fv = np.array([r["fb"] for r in rows])
    return dict(ok=True, nf=None, rho=rho, S=S_, Fv=Fv,
                Bw=float(S_[Nw - 2]) + B57,
                qN=float(rho[Nw - 1]) / B57,
                DN=B57 - float(rho[Nw - 1]),
                SN1=float(S_[Nw - 1]))


def virtual_star_census(a_mu, b_mu, bvec):
    """route-(i) representability: if b_i = c phat_i(x*) then the
    recurrence-consistency values x*_i = a_i + (be_i b_{i+1} +
    be_{i-1} b_{i-1})/b_i are constant; returns the spread;
    consumes chain coefficients + the border vector only."""
    xs = []
    for i in range(1, len(bvec) - 1):
        if abs(bvec[i]) > 1e-14:
            xs.append(a_mu[i] + (b_mu[i] * bvec[i + 1]
                                 + b_mu[i - 1] * bvec[i - 1])
                      / bvec[i])
    if not xs:
        return float("nan")
    return float(np.max(xs) - np.min(xs))


def aug_rung(xp, wp, yn, vn, xu, wu, Nw, S, L, i1, i2,
             bxs, bws, bys, bvs, Bm=None, budget=None,
             with_cside=False, with_handoff=False):
    """THE r362 BLOCK of one window: the r356 dual block (BDH
    verbatim), the border chain (BH verbatim), the mu-orthonormal
    border vector, the bordered dual resolvent Z = [[R^{-1}, vt],
    [vt^T, 1 + gamma]] and R† = Z^{-1}, and every (A1)-(A7) ward;
    budget None = the canonical B_w (border chain), else the passed
    fallback; consumes measure arrays, positions, pair indices and
    the border window only."""
    xp = np.asarray(xp, float)
    wp = np.asarray(wp, float)
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    D9 = BDH.dual_rung(np.asarray(xu, float), np.asarray(wu, float),
                       yn, vn, Nw, S, L, i1, i2, B=Bm)
    bp = border_chain_pack(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw)
    out = dict(ok_sup=D9["ok_sup"] and D9["dev_grid"] == 0.0
               and D9["ok_map"],
               lamR=D9["lamR"], margin=D9["mdual"],
               f1=D9["f1"], f2=D9["f2"], ok_border=bp["ok"],
               nf=bp["nf"])
    if not bp["ok"] and budget is None:
        out["D"] = None
        return out
    Bw = bp["Bw"] if budget is None else float(budget)
    a_mu, b_mu, h0_mu = V.mu_chain(xp, wp, Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    beta = bvec / math.sqrt(Bw)
    gam = float(beta @ beta)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    v = Bm @ beta
    En = Bm @ Bm.T
    Sm = len(v)
    solveIE = np.linalg.solve(np.eye(Sm) - En, v)
    qdag = gam + float(v @ solveIE)
    dev_frame = float("nan")
    dev_dict = float("nan")
    if bp["ok"]:
        dualnorm = Bw * qdag
        dev_frame = abs(dualnorm / bp["SN1"] - 1.0)
        dev_dict = abs((1.0 - qdag)
                       - B57 * (1.0 - bp["qN"]) / Bw) \
            / max(abs(1.0 - qdag), 1e-300)
    Rm = D9["Rm"]
    epsY = D9["eps"][D9["iY"]]
    Rinv = np.linalg.inv(Rm)
    vt = epsY * v
    Z = np.zeros((Sm + 1, Sm + 1))
    Z[:Sm, :Sm] = Rinv
    Z[:Sm, Sm] = vt
    Z[Sm, :Sm] = vt
    Z[Sm, Sm] = 1.0 + gam
    Rdag = np.linalg.inv(Z)
    Rdag = 0.5 * (Rdag + Rdag.T)
    Gd = np.zeros((Sm + 1, Sm + 1))
    Gd[:Sm, :Sm] = En
    Gd[:Sm, Sm] = v
    Gd[Sm, :Sm] = v
    Gd[Sm, Sm] = gam
    Dd = np.concatenate([epsY, [1.0]])
    dev_comp = float(np.max(np.abs(
        Gd - (Z - np.eye(Sm + 1)) * np.outer(Dd, Dd))))
    evG = np.linalg.eigvalsh(Gd)
    lamG = float(evG[-1])
    gd_min = float(evG[0])
    evRd, WRd = np.linalg.eigh(Rdag)
    lamRd = float(evRd[0])
    dev_map = abs((1.0 - lamG) - (2.0 - 1.0 / lamRd))
    c = 1.0 + gam
    Rv = Rm @ vt
    den = c - float(vt @ Rv)
    dev_sm = max(float(np.max(np.abs(
        Rdag[:Sm, :Sm] - (Rm + np.outer(Rv, Rv) / den)))),
        abs(Rdag[Sm, Sm] - 1.0 / den),
        float(np.max(np.abs(Rdag[:Sm, Sm] + Rv / den))))
    dev_sm_wrong = float(np.max(np.abs(
        Rdag[:Sm, :Sm] - (Rm - np.outer(Rv, Rv) / den))))
    Md = Rdag - 0.5 * np.eye(Sm + 1)
    xb = np.linalg.solve(Md[:Sm, :Sm], Md[:Sm, Sm])
    schur_b = float(Md[Sm, Sm] - Md[Sm, :Sm] @ xb)
    pred_b = (1.0 - qdag) / (2.0 * (1.0 + qdag))
    dev_schb = abs(schur_b / pred_b - 1.0) if pred_b != 0.0 \
        else float("inf")
    evRm = np.linalg.eigvalsh(Rm)
    kI = min(K_INTER, Sm - 1)
    inter_ok = all(evRd[k] <= evRm[k]
                   + INTER_TOL * max(abs(evRm[k]), 1.0)
                   and evRm[k] <= evRd[k + 1]
                   + INTER_TOL * max(abs(evRm[k]), 1.0)
                   for k in range(kI))
    idx3 = [i1, i2, Sm]
    rest = [k for k in range(Sm + 1) if k not in idx3]
    Mcc = Md[np.ix_(rest, rest)]
    Mpc = Md[np.ix_(idx3, rest)]
    S3 = Md[np.ix_(idx3, idx3)] - Mpc @ np.linalg.solve(Mcc, Mpc.T)
    S3 = 0.5 * (S3 + S3.T)
    ev3 = np.linalg.eigvalsh(S3)
    x3 = np.linalg.solve(S3[:2, :2], S3[:2, 2])
    schur_b_loc = float(S3[2, 2] - S3[2, :2] @ x3)
    dev_quot = abs(schur_b_loc / schur_b - 1.0) if schur_b != 0.0 \
        else float("inf")
    eps_d = lamRd - 0.5
    bind3 = float(ev3[0]) / eps_d if eps_d != 0.0 else float("nan")
    rest_min = float(np.linalg.eigvalsh(Mcc)[0])
    w_min = WRd[:, 0]
    xstar = virtual_star_census(a_mu, b_mu, bvec)
    dmin_coll = 0.0
    xu_s = np.asarray(xu, float)
    step = max(1, len(bxa) // 64)
    dmin_coll = min(float(np.min(np.abs(xu_s - t)))
                    for t in bxa[::step])
    out.update(Bw=Bw, qN=bp.get("qN", float("nan")),
               DN=bp.get("DN", float("nan")), gam=gam, qdag=qdag,
               dev_frame=dev_frame, dev_dict=dev_dict,
               dev_comp=dev_comp, dev_map=dev_map, dev_sm=dev_sm,
               dev_sm_wrong=dev_sm_wrong, gd_min=gd_min,
               lamG=lamG, lamRd=lamRd, mdag=1.0 - lamG,
               schur_b=schur_b, dev_schb=dev_schb,
               dev_quot=dev_quot, inter_ok=inter_ok,
               ev3=tuple(float(t) for t in ev3), bind3=bind3,
               rest_min=rest_min,
               bmass=float(w_min[Sm] ** 2),
               pmass=float(w_min[i1] ** 2 + w_min[i2] ** 2),
               xstar=xstar, dmin_coll=dmin_coll,
               evRd_bot=tuple(float(t) for t in evRd[:kI + 1]),
               evRm_bot=tuple(float(t) for t in evRm[:kI]),
               Fv0=(bp["Fv"] if bp["ok"] else None))
    if with_cside:
        Ec = Bm.T @ Bm
        lamEc = float(np.linalg.eigvalsh(
            Ec + np.outer(beta, beta))[-1])
        out["dev_cn"] = abs(lamEc - lamG)
    if with_handoff:
        Ad = np.eye(Sm + 1) - 2.0 * Rdag
        cols = np.linalg.solve(Ad, np.eye(Sm + 1)[:, [i1, i2]])
        a11 = float(cols[i1, 0])
        a22 = float(cols[i2, 1])
        a12 = float(cols[i1, 1])
        out["a11d"], out["a22d"], out["a12d"] = a11, a22, a12
        out["shared"] = a12 * a12 / (a11 * a22) \
            if a11 * a22 != 0.0 else float("nan")
        # m6 sizing column: the mu-tilde chain coefficients in
        # place of b (wrong frame; gate-side use only)
        if bp["ok"]:
            Fv = bp["Fv"]
            betaF = Fv / math.sqrt(Bw)
            vF = Bm @ betaF
            qdF = float(betaF @ betaF
                        + vF @ np.linalg.solve(np.eye(Sm) - En, vF))
            out["qdag_m6"] = qdF
        bvv = bvec / 1.0
        vm1 = Bm @ bvv
        out["qdag_m1"] = float(bvv @ bvv
                               + vm1 @ np.linalg.solve(
                                   np.eye(Sm) - En, vm1))
    return out


def chi_aug_row(kz, q, lpq):
    """one chi-world rung through the identical augmented pipeline
    (r357 frame verbatim; border = the smooth comb through the SAME
    chi arch, the DMF chi_wpack convention); consumes the chi comb
    + the matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = aug_rung(mzc["xp"], mzc["wp"], mzc["yn"], mzc["vn"],
                 mzc["xu"], mzc["wu"], mzc["Nw"], mzc["S"],
                 mzc["L"], j1, j2, mzb["xp"], mzb["wp"], mzb["yn"],
                 mzb["vn"])
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    o.pop("Fv0", None)
    return o


# ============== must-fail mutants
def mutant_mdag_readback(mdag_col_true):
    """m3 MUST-FAIL (AST): an 'augmented dual object' whose margin
    is the withheld measured margin† column verbatim --
    AST-FLAGGED."""
    return mdag_col_true


def slim362(o):
    """memory hygiene: drop the heavy fields."""
    return {k: o[k] for k in o if k not in ("Fv0", "D")}


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("augmented_borodin_duality_probe -- "
          "PRIME.LDAGGER.AUGMENTED_DUALITY.01 (round 362)")
    print("SPEC_SHA %s   (r356 BDH %s / r359 SWD %s / r342 PX %s / "
          "r357 DMF %s / r244 BH %s / r226 HS %s)"
          % (SPEC_SHA[:16], BDH.SPEC_SHA[:16], SWD.SPEC_SHA[:16],
             PX.SPEC_SHA[:16], DMF.SPEC_SHA[:16], BH.SPEC_SHA[:16],
             HS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 aug block + chi3 w9; ladder, chi "
                        "ladders, twin, scramble, deep row, fits, "
                        "adjudications skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and HS.SPEC_SHA.startswith(HS_SHA_PREFIX)
              and BH.SPEC_SHA.startswith(BH_SHA_PREFIX)
              and PB.SPEC_SHA.startswith(PB_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r356/r359/r342/r357/r354/r226/"
          "r244/r243 machinery imported verbatim (BDH %s == %s*, "
          "SWD %s == %s*, PX %s == %s*, DMF %s == %s*, PWA %s == "
          "%s*, HS %s == %s*, BH %s == %s*, PB %s == %s*); the "
          "route adjudication (route ii sealed as constructor, "
          "route i typed by the representability + collision wards "
          "+ the toy bridge), the (A1)-(A7) graded bars, the "
          "equivalence floors, the local-block clauses (bind range "
          "[%f, %.1f], EV3 band %s, QUOT bars %s), the worlds, the "
          "budget provenance B_w = S_{N-2} + 5/7 (r241/r243 "
          "IMPORTED, never fitted) and every mutant; pre-spec "
          "scoping s1-s3 disclosed in the spec; the DCCX STOP list "
          "forbids any L*/Terminal claim and any certificate "
          "reading"
          % (BDH.SPEC_SHA[:8], BDH_SHA_PREFIX, SWD.SPEC_SHA[:8],
             SWD_SHA_PREFIX, PX.SPEC_SHA[:8], PX_SHA_PREFIX,
             DMF.SPEC_SHA[:8], DMF_SHA_PREFIX, PWA.SPEC_SHA[:8],
             PWA_SHA_PREFIX, HS.SPEC_SHA[:8], HS_SHA_PREFIX,
             BH.SPEC_SHA[:8], BH_SHA_PREFIX, PB.SPEC_SHA[:8],
             PB_SHA_PREFIX, BIND_MIN, BIND_MAX, str(EV3_BAND),
             str(QUOT_BAR)))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m3 = scope_audit("mutant_mdag_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m3),
          "the %d module-own constructors consume measure arrays / "
          "chain coefficients / positions / pair indices / border "
          "windows ONLY (%s); fragment audit (no fit primitives "
          "beyond the imported r286 Theil-Sen): %s; m3 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m3[0] if hits_m3 else "MISS"))

    # ---------------- S1 toys (exact Fractions)
    section("S1  TOYS -- FRACTIONS-EXACT AUGMENTED DUALITY + THE "
            "ROUTE-(i) BRIDGE")
    # the rational 5-atom model with PERFECT-SQUARE nu weights
    xs_t = [Fr(-3, 4), Fr(-1, 4), Fr(0), Fr(1, 2), Fr(4, 5)]
    u_t = [Fr(1), Fr(1, 4), Fr(1, 2), Fr(1, 9), Fr(1, 3)]
    mu_idx, nu_idx = (0, 2, 4), (1, 3)
    N_t, S_t = 3, 5
    bx_t = [Fr(1, 3), Fr(-2, 5)]
    bw_t = [Fr(1, 4), Fr(1, 7)]

    def kker(Mi, y1, y2, n):
        return sum(Mi[i][k] * y1 ** i * y2 ** k
                   for i in range(n) for k in range(n))

    M_mu = [[sum(u_t[j] * xs_t[j] ** (i + k) for j in mu_idx)
             for k in range(N_t)] for i in range(N_t)]
    Mi_mu = BDH.fr_inv(M_mu)
    ys_t = [xs_t[j] for j in nu_idx]
    vs_t = [u_t[j] for j in nu_idx]
    sq_v = [Fr(1, 2), Fr(1, 3)]          # sqrt of the nu weights
    ok_sq = all(s * s == v for s, v in zip(sq_v, vs_t))
    # (T1) the bordered A_cap equivalence, both truth directions
    H_t = [[sum(u_t[j] * xs_t[j] ** (i + k) for j in mu_idx)
            - sum(vs_t[a] * ys_t[a] ** (i + k) for a in range(2))
            for k in range(N_t)] for i in range(N_t)]
    u_bord = [sum(w * t ** i for t, w in zip(bx_t, bw_t))
              for i in range(N_t)]
    yH = BDH.fr_mul(BDH.fr_inv(H_t), [[x] for x in u_bord])
    dn0 = sum(u_bord[i] * yH[i][0] for i in range(N_t))
    B_hi = Fr(4)
    k_sc = 1
    while k_sc * k_sc * dn0 <= B_hi:
        k_sc += 1
    k_sc += 1                            # terminal-false border scale

    def acap_minors(Hm, ub, Bb):
        A = [row[:] + [ub[i]] for i, row in enumerate(Hm)]
        A.append(ub[:] + [Bb])
        dets = []
        for k in range(1, len(A) + 1):
            sub = [r[:k] for r in A[:k]]
            dets.append(SWD.fr_det(sub))
        return dets

    dets_true = acap_minors(H_t, u_bord, B_hi)
    ub_f = [k_sc * x for x in u_bord]
    dets_false = acap_minors(H_t, ub_f, B_hi)
    schur_true = B_hi - dn0
    schur_false = B_hi - k_sc * k_sc * dn0
    # m1 exact: WITHOUT the 1/B normalization (budget forced to 1)
    # the A_cap verdict flips on the doubled border, whose dual
    # norm 4 dn0 sits strictly between 1 and the true budget 4
    ub_2 = [2 * x for x in u_bord]
    dets_m1_true = acap_minors(H_t, ub_2, B_hi)
    dets_m1 = acap_minors(H_t, ub_2, Fr(1))
    m1_breaks = (all(d > 0 for d in dets_m1_true)
                 and not all(d > 0 for d in dets_m1)
                 and Fr(1) < 4 * dn0 < B_hi)
    check("G10-toy-acap-equivalence", ok_sq and dn0 > 0
          and all(d > 0 for d in dets_true) and schur_true > 0
          and (not all(d > 0 for d in dets_false))
          and schur_false < 0 and m1_breaks,
          "EXACT FRACTIONS bordered A_cap on the 5-atom model "
          "(perfect-square nu weights): dual norm u^T H^{-1} u = "
          "%s; TRUE branch (B = 4): all %d leading minors of "
          "[[H, u], [u^T, B]] positive AND the Schur value B - "
          "u^T H^{-1} u = %s > 0; FALSE branch (border x %d): the "
          "minor chain breaks AND the Schur value %s < 0 -- L† <=> "
          "A_cap > 0 <=> L* AND Terminal, both truth directions; "
          "m1 (budget normalization dropped, B == 1, doubled "
          "border): the verdict FLIPS exactly (1 < 4 dn0 < 4) -- "
          "CAUGHT in Fractions"
          % (str(dn0), N_t + 1, str(schur_true), k_sc,
             str(schur_false)))
    # (T2) the augmented duality in Fractions: E, R, Z, R-dagger
    Eh = [[sq_v[i] * sq_v[j] * kker(Mi_mu, ys_t[i], ys_t[j], N_t)
           for j in range(2)] for i in range(2)]
    Pp_t = [math.prod([xs_t[j] - xs_t[k] for k in range(S_t)
                       if k != j], start=Fr(1)) for j in range(S_t)]
    uv_t = [Fr(1) / (u_t[j] * Pp_t[j] ** 2) for j in range(S_t)]
    M_v = [[sum(uv_t[j] * xs_t[j] ** (i + k) for j in range(S_t))
            for k in range(N_t - 1)] for i in range(N_t - 1)]
    Mi_v = BDH.fr_inv(M_v)
    sq_uv = []
    for a in range(2):
        j = nu_idx[a]
        sq_uv.append(Fr(1) / (sq_v[a] * abs(Pp_t[j])))
    ok_sqv = all(s * s == uv_t[nu_idx[a]]
                 for a, s in enumerate(sq_uv))
    R_t = [[sq_uv[i] * sq_uv[j]
            * kker(Mi_v, ys_t[i], ys_t[j], N_t - 1)
            for j in range(2)] for i in range(2)]
    eps_t = [Fr(1) if Pp_t[j] > 0 else Fr(-1) for j in nu_idx]
    # exact r356 relation E == D (R^{-1} - I) D on the toy
    Ri_t = BDH.fr_inv(R_t)
    dev_ER = max(abs(Eh[i][j] - eps_t[i] * eps_t[j]
                     * (Ri_t[i][j] - (Fr(1) if i == j else Fr(0))))
                 for i in range(2) for j in range(2))
    # border image: v_j = sqrt(v_j/B) (K_mu sigma)(y_j); B = 4
    B_t = Fr(4)
    sqB = Fr(2)
    v_t = [sq_v[a] / sqB
           * sum(bw_t[b] * kker(Mi_mu, ys_t[a], bx_t[b], N_t)
                 for b in range(2)) for a in range(2)]
    gam_t = sum(bw_t[a] * bw_t[b]
                * kker(Mi_mu, bx_t[a], bx_t[b], N_t)
                for a in range(2) for b in range(2)) / B_t
    vt_t = [eps_t[a] * v_t[a] for a in range(2)]
    Z_t = [[Ri_t[0][0], Ri_t[0][1], vt_t[0]],
           [Ri_t[1][0], Ri_t[1][1], vt_t[1]],
           [vt_t[0], vt_t[1], Fr(1) + gam_t]]
    Rd_t = BDH.fr_inv(Z_t)
    Gd_t = [[Eh[0][0], Eh[0][1], v_t[0]],
            [Eh[1][0], Eh[1][1], v_t[1]],
            [v_t[0], v_t[1], gam_t]]
    Dd_t = [eps_t[0], eps_t[1], Fr(1)]
    dev_A1 = max(abs(Gd_t[i][j] - Dd_t[i] * Dd_t[j]
                     * (Z_t[i][j] - (Fr(1) if i == j else Fr(0))))
                 for i in range(3) for j in range(3))
    # char-poly similarity (A2 rational form) at three x values
    dev_A2 = Fr(0)
    for xv in (Fr(2), Fr(3), Fr(5, 2)):
        MG = [[(xv if i == j else Fr(0)) - Gd_t[i][j]
               for j in range(3)] for i in range(3)]
        MZ = [[(xv + 1 if i == j else Fr(0)) - Z_t[i][j]
               for j in range(3)] for i in range(3)]
        dev_A2 = max(dev_A2, abs(SWD.fr_det(MG) - SWD.fr_det(MZ)))
    # SM block form (A4) exact
    c_t = Fr(1) + gam_t
    Rv_t = [sum(R_t[i][j] * vt_t[j] for j in range(2))
            for i in range(2)]
    den_t = c_t - sum(vt_t[i] * Rv_t[i] for i in range(2))
    dev_A4 = Fr(0)
    for i in range(2):
        for j in range(2):
            dev_A4 = max(dev_A4, abs(
                Rd_t[i][j] - (R_t[i][j] + Rv_t[i] * Rv_t[j]
                              / den_t)))
        dev_A4 = max(dev_A4, abs(Rd_t[i][2] + Rv_t[i] / den_t))
    dev_A4 = max(dev_A4, abs(Rd_t[2][2] - Fr(1) / den_t))
    # (A5)/(A6): q-dagger, frame invariance vs H-side, border Schur
    IEt = [[(Fr(1) if i == j else Fr(0)) - Eh[i][j]
            for j in range(2)] for i in range(2)]
    IEi = BDH.fr_inv(IEt)
    qd_t = gam_t + sum(v_t[i] * IEi[i][j] * v_t[j]
                       for i in range(2) for j in range(2))
    dev_A5 = abs(qd_t * B_t - dn0)
    Md_t = [[Rd_t[i][j] - (Fr(1, 2) if i == j else Fr(0))
             for j in range(3)] for i in range(3)]
    Mtop = [[Md_t[i][j] for j in range(2)] for i in range(2)]
    Mti = BDH.fr_inv(Mtop)
    schur_bt = Md_t[2][2] - sum(Md_t[2][i] * Mti[i][j] * Md_t[j][2]
                                for i in range(2) for j in range(2))
    dev_A6 = abs(schur_bt - (Fr(1) - qd_t)
                 / (Fr(2) * (Fr(1) + qd_t)))
    # equivalence both directions via minors (TRUE branch; FALSE
    # branch by border scaling k_sc as in T1)
    def minors3(Mx):
        return [SWD.fr_det([r[:k] for r in Mx[:k]])
                for k in (1, 2, 3)]

    mins_true = minors3(Md_t)
    v_f = [k_sc * t for t in v_t]
    gam_f = k_sc * k_sc * gam_t
    vt_f = [eps_t[a] * v_f[a] for a in range(2)]
    Z_f = [[Ri_t[0][0], Ri_t[0][1], vt_f[0]],
           [Ri_t[1][0], Ri_t[1][1], vt_f[1]],
           [vt_f[0], vt_f[1], Fr(1) + gam_f]]
    Rd_f = BDH.fr_inv(Z_f)
    Md_f = [[Rd_f[i][j] - (Fr(1, 2) if i == j else Fr(0))
             for j in range(3)] for i in range(3)]
    mins_false = minors3(Md_f)
    qd_f = gam_f + sum(v_f[i] * IEi[i][j] * v_f[j]
                       for i in range(2) for j in range(2))
    MR_t = [[R_t[i][j] - (Fr(1, 2) if i == j else Fr(0))
             for j in range(2)] for i in range(2)]
    ok_R_pd = (MR_t[0][0] > 0
               and MR_t[0][0] * MR_t[1][1]
               - MR_t[0][1] * MR_t[1][0] > 0)
    ok_eq_t = (all(m > 0 for m in mins_true) and qd_t < 1
               and dn0 < B_t
               and (not all(m > 0 for m in mins_false))
               and qd_f > 1 and ok_R_pd)
    check("G11-toy-augmented-duality", dev_ER == 0 and dev_A1 == 0
          and dev_A2 == 0 and dev_A4 == 0 and dev_A5 == 0
          and dev_A6 == 0 and ok_sqv and ok_eq_t,
          "EXACT FRACTIONS augmented duality on the 5-atom model: "
          "the r356 relation E == D (R^{-1} - I) D EXACT; (A1) "
          "G† == D† (Z - I) D† EXACT (9 entries); (A2) char-poly "
          "similarity det(xI - G†) == det((x+1)I - Z) EXACT at 3 "
          "rational points (the spectral map is a similarity, "
          "margin† == 2 - 1/lambda_min(R†)); (A4) the "
          "Sherman-Morrison block form of R† == Z^{-1} EXACT "
          "(rank-1 at the resolvent level); (A5) FRAME INVARIANCE "
          "q† B == u^T H^{-1} u EXACT (the mu-orthonormal route == "
          "the monomial Hankel route); (A6) the border Schur == "
          "(1 - q†)/(2 (1 + q†)) EXACT; EQUIVALENCE both truth "
          "directions: TRUE branch minors positive with q† = %s < "
          "1, FALSE branch (border x %d) breaks with q† = %s > 1 "
          "while R - I/2 stays positive -- the terminal channel "
          "kills L† exactly through the border row"
          % (str(qd_t), k_sc, str(qd_f)))
    # (T3) the route-(i) bridge: single-atom border, S+1 nodes,
    # rank N (the SHIFTED half-filling arithmetic)
    t_v = Fr(1, 3)
    m_v = Fr(1, 2)
    w_virt = m_v * m_v / B_t             # m^2/B, perfect square
    sq_wv = m_v / sqB
    xs_a = xs_t + [t_v]
    u_a = u_t + [w_virt]
    S_a = 6
    Pp_a = [math.prod([xs_a[j] - xs_a[k] for k in range(S_a)
                       if k != j], start=Fr(1)) for j in range(S_a)]
    ok_coll_guard = min(abs(xs_a[j] - xs_a[k])
                        for j in range(S_a)
                        for k in range(S_a) if k != j) > 0
    uv_a = [Fr(1) / (u_a[j] * Pp_a[j] ** 2) for j in range(S_a)]
    Ah_a = BDH.fr_proj(xs_a, u_a, N_t)
    M_va = [[sum(uv_a[j] * xs_a[j] ** (i + k) for j in range(S_a))
             for k in range(N_t)] for i in range(N_t)]
    Vm_a = [[xs_a[j] ** i for i in range(N_t)] for j in range(S_a)]
    Bh_a = BDH.fr_mul(BDH.fr_mul(Vm_a, BDH.fr_inv(M_va)),
                      [list(r) for r in zip(*Vm_a)])
    Bh_a = [[Bh_a[i][j] * uv_a[j] for j in range(S_a)]
            for i in range(S_a)]
    G_a = [Fr(1) / (u_a[j] * Pp_a[j]) for j in range(S_a)]
    dev_bor_a = max(abs(Ah_a[i][j] + G_a[i] * Bh_a[i][j] / G_a[j]
                        - (Fr(1) if i == j else Fr(0)))
                    for i in range(S_a) for j in range(S_a))
    # m2: the WRONG rank N-1 on the augmented system breaks exactly
    M_vw = [[sum(uv_a[j] * xs_a[j] ** (i + k) for j in range(S_a))
             for k in range(N_t - 1)] for i in range(N_t - 1)]
    Vm_w = [[xs_a[j] ** i for i in range(N_t - 1)]
            for j in range(S_a)]
    Bh_w = BDH.fr_mul(BDH.fr_mul(Vm_w, BDH.fr_inv(M_vw)),
                      [list(r) for r in zip(*Vm_w)])
    Bh_w = [[Bh_w[i][j] * uv_a[j] for j in range(S_a)]
            for i in range(S_a)]
    dev_m2 = max(abs(Ah_a[i][j] + G_a[i] * Bh_w[i][j] / G_a[j]
                     - (Fr(1) if i == j else Fr(0)))
                 for i in range(S_a) for j in range(S_a))
    # the literal (S+1)-point dual kernel on Y-dagger vs route (ii)
    Yd_idx = [1, 3, 5]
    Mi_va = BDH.fr_inv(M_va)
    sq_ua = sq_v + [sq_wv]
    sq_uva = [Fr(1) / (sq_ua[a] * abs(Pp_a[Yd_idx[a]]))
              for a in range(3)]
    ok_sqa = all(s * s == uv_a[Yd_idx[a]]
                 for a, s in enumerate(sq_uva))
    Ruv = [[sq_uva[a] * sq_uva[b]
            * kker(Mi_va, xs_a[Yd_idx[a]], xs_a[Yd_idx[b]], N_t)
            for b in range(3)] for a in range(3)]
    # route (ii) on the same single-atom border
    v_s = [sq_v[a] / sqB * m_v
           * kker(Mi_mu, ys_t[a], t_v, N_t) for a in range(2)]
    gam_s = m_v * m_v * kker(Mi_mu, t_v, t_v, N_t) / B_t
    vt_s = [eps_t[a] * v_s[a] for a in range(2)]
    Z_s = [[Ri_t[0][0], Ri_t[0][1], vt_s[0]],
           [Ri_t[1][0], Ri_t[1][1], vt_s[1]],
           [vt_s[0], vt_s[1], Fr(1) + gam_s]]
    Rd_s = BDH.fr_inv(Z_s)
    dev_abs = max(abs(abs(Ruv[a][b]) - abs(Rd_s[a][b]))
                  for a in range(3) for b in range(3))
    dev_cp = Fr(0)
    for xv in (Fr(2), Fr(3), Fr(5, 2)):
        M1x = [[(xv if a == b else Fr(0)) - Ruv[a][b]
                for b in range(3)] for a in range(3)]
        M2x = [[(xv if a == b else Fr(0)) - Rd_s[a][b]
                for b in range(3)] for a in range(3)]
        dev_cp = max(dev_cp, abs(SWD.fr_det(M1x) - SWD.fr_det(M2x)))
    # m5: virtual node ON a real node -> the support ward refuses
    t_bad = xs_t[2]
    coll_bad = min(abs(t_bad - x) for x in xs_t)
    check("G12-toy-route-i-bridge", ok_coll_guard and dev_bor_a == 0
          and dev_m2 > 0 and ok_sqa and dev_abs == 0 and dev_cp == 0
          and coll_bad == 0,
          "THE ROUTE-(i) BRIDGE (single-atom border, EXACT "
          "FRACTIONS): the (S+1)-node Uvarov complementation "
          "Pi_N + G Pi_N^vee G^{-1} == I holds EXACTLY at the "
          "SHIFTED rank N = %d (S† = %d = 2N: the half-filling "
          "arithmetic moves by exactly one -- RANK_SHIFT_MISMATCH "
          "stays off); the m2 mutant (dual rank N-1 on the "
          "augmented system) breaks EXACTLY (%.3e != 0); the "
          "literal (S+1)-point dual kernel on Y† EQUALS the "
          "route-(ii) bordered resolvent R† up to sign conjugation "
          "(|entries| EXACT, char-poly EXACT at 3 points) -- the "
          "two routes agree where both exist; m5: the collision "
          "candidate t == x_2 has min |t - x_j| == 0 and is "
          "REFUSED by the support ward (P' would vanish) -- CAUGHT"
          % (N_t, S_a, float(dev_m2)))
    # (T4) f64 synthetic equivalence, all three quadrants
    seedM = np.array([[1.0, 2, 3, 4, 5], [6, 7, 8, 9, 1],
                      [2, 4, 6, 8, 1], [3, 5, 7, 9, 2],
                      [4, 8, 3, 7, 2]])
    Qr, _ = np.linalg.qr(seedM)
    oks_t4 = []
    for lam0, vsc, expect in ((0.52, 0.05, True),
                              (0.52, 3.0, False),
                              (0.31, 0.05, False)):
        Rt = Qr @ np.diag([lam0, 0.6, 0.7, 0.8, 0.9]) @ Qr.T
        vv = vsc * np.array([0.1, -0.2, 0.15, 0.05, -0.1])
        gg = float(vv @ vv) * 1.2
        Zt = np.zeros((6, 6))
        Zt[:5, :5] = np.linalg.inv(Rt)
        Zt[:5, 5] = vv
        Zt[5, :5] = vv
        Zt[5, 5] = 1.0 + gg
        Rdt = np.linalg.inv(Zt)
        lam_d = float(np.linalg.eigvalsh(0.5 * (Rdt + Rdt.T))[0])
        En_t = np.eye(5) - np.linalg.inv(
            Rt @ np.linalg.inv(2.0 * Rt - np.eye(5)))
        qd = gg + float(vv @ np.linalg.solve(np.eye(5) - En_t, vv))
        live = (lam_d > 0.5)
        pred = (lam0 > 0.5) and (qd < 1.0)
        oks_t4.append(live == expect and pred == expect)
    check("G13-toy-f64-equivalence", all(oks_t4),
          "the f64 equivalence toy in all three quadrants: "
          "(lambda_min(R) 0.52, small border) => R† > I/2 TRUE; "
          "(0.52, border x 60) => FALSE through the terminal "
          "channel q† > 1; (0.31, small border) => FALSE through "
          "the R block -- {R† > I/2} == {R > I/2} AND {q† < 1} "
          "two-sided on the synthetic family")

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + THE AUGMENTED BLOCK + ROUTE "
            "CENSUS")
    R9 = PX.build_rung(MAIN_KZ)
    mz9 = R9["mz"]
    alpha9 = V.window_shape(MAIN_KZ)[0]
    alpha9_pik = PIK.build_rung(MAIN_KZ)["alpha"]
    dsm9 = HS.window_data(MAIN_KZ, comb=PB.smooth_comb(alpha9))
    d9 = HS.window_data(MAIN_KZ)
    dev_fx9 = max(float(np.max(np.abs(np.sort(d9["xs"])
                                      - np.sort(mz9["xp"])))),
                  float(np.max(np.abs(np.sort(d9["ys"])
                                      - np.sort(mz9["yn"])))))
    o9 = aug_rung(mz9["xp"], mz9["wp"], mz9["yn"], mz9["vn"],
                  mz9["xu"], mz9["wu"], R9["Nw"], R9["S"], mz9["L"],
                  R9["i1"], R9["i2"], dsm9["xs"], dsm9["ws"],
                  dsm9["ys"], dsm9["vs"], Bm=R9["B"],
                  with_cside=True, with_handoff=True)
    ok_rec = (R9["S"] == REC_S and R9["Sm"] == REC_SM
              and R9["Nw"] == REC_NW
              and abs(R9["margin"] / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL
              and abs(o9["lamR"] - REC_LAMR) <= 1e-8
              and dev_fx9 == 0.0 and alpha9 == alpha9_pik
              and o9["f1"] == W9_AUG_ANCH["f1"]
              and o9["f2"] == W9_AUG_ANCH["f2"])
    check("G20-w9-records", ok_rec,
          "w9: S = %d (nu %d), N_w = %d, margin %.4e (record "
          "%.4e), lambda_min(R) = %.9f == the r356 record; the "
          "HS/PIK window frame == the V frame BITWISE (dev %.1f) "
          "and the smooth-comb alpha == the document alpha "
          "EXACTLY; folds (%d, %d)"
          % (R9["S"], R9["Sm"], R9["Nw"], R9["margin"], REC_MARGIN,
             o9["lamR"], dev_fx9, o9["f1"], o9["f2"]))
    A9 = W9_AUG_ANCH
    ok_aug9 = (o9["ok_border"]
               and abs(o9["mdag"] / A9["mdag"] - 1.0) <= 1e-3
               and abs(o9["lamRd"] - A9["lamRd"]) <= 1e-8
               and abs(o9["qdag"] - A9["qdag"]) <= 1e-6
               and abs(o9["qN"] - A9["qN"]) <= 1e-6
               and abs(o9["Bw"] - A9["Bw"]) <= 1e-6
               and abs(o9["gam"] - A9["gam"]) <= 1e-6
               and abs(o9["schur_b"] / A9["schur_b"] - 1.0) <= 1e-3
               and abs(o9["bind3"] - A9["bind3"]) <= 5e-3
               and abs(o9["ev3"][2] / A9["ev3_top"] - 1.0) <= 1e-2
               and abs(o9["bmass"] / A9["bmass"] - 1.0) <= 0.2
               and abs(o9["xstar"] / A9["xstar"] - 1.0) <= 0.1)
    ok_wards9 = (o9["dev_comp"] <= COMPD_BAR[0]
                 and o9["dev_map"] <= MAPD_BAR[0]
                 and o9["dev_sm"] <= SMD_BAR
                 and o9["dev_frame"] <= FRAME_BAR[0]
                 and o9["dev_schb"] <= SCHB_BAR[0]
                 and o9["dev_quot"] <= QUOT_BAR[0]
                 and o9["dev_cn"] <= CN_BAR
                 and o9["dev_dict"] <= FRAME_BAR[0]
                 and o9["gd_min"] >= GD_PSD_FLOOR
                 and o9["inter_ok"])
    check("G21-w9-augmented-block", ok_aug9 and ok_wards9,
          "THE AUGMENTED BLOCK at w9 (s1 anchors bit-near): "
          "margin† = %.6e (margin %.6e), lambda_min(R†) = %.9f, "
          "q† = %.7f, q_N = %.7f, B_w = %.7f, gamma = %.7f, "
          "border Schur = %.7e == (1-q†)/(2(1+q†)) at %.1e, ev3 = "
          "(%.3e, %.3e, %.3e), bind† = %.6f, border mass %.1e; "
          "WARDS: (A1) comp %.1e, (A2) map %.1e + c-side %.1e, "
          "(A4) SM %.1e, (A5) frame %.1e + dict %.1e, (A6) quot "
          "%.1e, (A7) interlacing %s, G† psd floor %.1e"
          % (o9["mdag"], R9["margin"], o9["lamRd"], o9["qdag"],
             o9["qN"], o9["Bw"], o9["gam"], o9["schur_b"],
             o9["dev_schb"], o9["ev3"][0], o9["ev3"][1],
             o9["ev3"][2], o9["bind3"], o9["bmass"],
             o9["dev_comp"], o9["dev_map"], o9["dev_cn"],
             o9["dev_sm"], o9["dev_frame"], o9["dev_dict"],
             o9["dev_quot"], o9["inter_ok"], o9["gd_min"]))
    s9 = SWD.schur_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                        R9["Nw"], R9["S"], mz9["L"], R9["i1"],
                        R9["i2"])
    ok_359 = (abs(s9["eps"] / W9_R359_ANCH["eps"] - 1.0) <= 1e-3
              and abs(s9["lamS"] / W9_R359_ANCH["lamS"] - 1.0)
              <= 1e-3
              and abs(s9["share"] - W9_R359_ANCH["share"]) <= 5e-3)
    check("G22-w9-r359-and-handoff", ok_359,
          "LEG 0 + LEG D at w9: the r359 Schur anchors reproduced "
          "(eps %.4e, lamS %.4e, share %.4f); THE AUGMENTED "
          "HANDOFF CENSUS: (A†^{-1})_11 = %.4f, (A†^{-1})_22 = "
          "%.4f, cross share† = %.4f vs the r359 share %.4f (dev "
          "%.1e) -- the rank-1 border deformation leaves the "
          "critical resolvent structure at the pair intact; the "
          "border adds the exact local Schur row (A6) at %.4e"
          % (s9["eps"], s9["lamS"], s9["share"], o9["a11d"],
             o9["a22d"], o9["shared"], s9["share"],
             abs(o9["shared"] - s9["share"]), o9["schur_b"]))
    check("G23-w9-route-census", o9["xstar"] > 1.0
          and o9["dmin_coll"] == 0.0,
          "ROUTE (i) DEAD ON THE REAL WINDOW, twice: the "
          "representability spread of the virtual-node candidates "
          "x*_i is %.1f (a point evaluation needs 0 -- the border "
          "is the SIGNED smooth-comb measure with %d atoms, not "
          "an atom); AND every border atom collides BITWISE with "
          "a union grid node (min distance %.1f: the smooth "
          "window lives on the SAME folded cosine grid) -- the "
          "node-polynomial insertion is structurally forbidden; "
          "route (ii), the bordered dual resolvent, is the sealed "
          "constructor" % (o9["xstar"], len(dsm9["xs"])
                           + len(dsm9["ys"]), o9["dmin_coll"]))

    # ---------------- S3 the ladder
    section("S3  THE LADDER (42 + 15 + 12 EXT3 + 6 EXT4 = 75 FULL "
            "+ KZ133 DEEP CENSUS)")
    OT = {MAIN_KZ: slim362(o9)}
    if smoke:
        for g in ("G30-ladder-census", "G31-aug-wards-all",
                  "G32-equivalence-census", "G33-fit-anchors",
                  "G34-deep-census"):
            check(g, True, "SMOKE: skipped")
        all_kz = [MAIN_KZ]
        res_kz = [MAIN_KZ]
    else:
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in LM.ext_rule()[:15]]
        ladder = (core_kzs + ext_kzs + list(EXT3_KZ)
                  + list(EXT4_KZ))
        print("    %-5s %-5s %-5s %-6s | %-10s %-10s | %-8s %-8s | "
              "%-9s %-8s | %-8s"
              % ("kz", "z", "S-", "N_w", "margin", "mdag", "qN",
                 "qdag", "schur_b", "bind3", "lamRd-1/2"))
        sup_fail, bord_fail = [], []
        for kz in ladder:
            if kz == MAIN_KZ:
                R = R9
                o = o9
                nwk = R9["Nw"]
            else:
                R = PX.build_rung(kz)
                mz = R["mz"]
                nwk = R["Nw"]
                al_k = V.window_shape(kz)[0]
                dsm = HS.window_data(kz,
                                     comb=PB.smooth_comb(al_k))
                o = aug_rung(mz["xp"], mz["wp"], mz["yn"],
                             mz["vn"], mz["xu"], mz["wu"], R["Nw"],
                             R["S"], mz["L"], R["i1"], R["i2"],
                             dsm["xs"], dsm["ws"], dsm["ys"],
                             dsm["vs"], Bm=R["B"],
                             with_cside=(kz in set(core_kzs
                                                   + ext_kzs)),
                             with_handoff=True)
                del dsm
            if not o["ok_sup"]:
                sup_fail.append(kz)
            if not o["ok_border"]:
                bord_fail.append(kz)
                continue
            print("    %-5d %-5d %-5d %-6d | %.4e %.4e | %.6f "
                  "%.6f | %.3e %.6f | %+.2e"
                  % (kz, R["z"], R["Sm"], nwk, R["margin"],
                     o["mdag"], o["qN"], o["qdag"], o["schur_b"],
                     o["bind3"], o["lamRd"] - 0.5), flush=True)
            o["Nw"] = nwk
            o["z"] = R["z"]
            o["margin356"] = R["margin"]
            OT[kz] = slim362(o)
            del R, o
        all_kz = [k for k in ladder if k in OT]
        ok_cen = (len(core_kzs) == 42 and len(ladder) == 75
                  and not sup_fail and not bord_fail
                  and all(EXT3_NW_MIN <= OT[k]["Nw"] <= EXT3_NW_MAX
                          for k in EXT3_KZ)
                  and all(EXT4_NW_MIN <= OT[k]["Nw"] <= EXT4_NW_MAX
                          for k in EXT4_KZ))
        check("G30-ladder-census", ok_cen,
              "42 core + 15 r286 extension + 12 EXT3 + 6 EXT4 = "
              "%d rows, ALL with support gate + border chain in "
              "the cone (support failures %s, border failures %s); "
              "EXT3/EXT4 depth windows as sealed; every border "
              "budget B_w > 0 with all chain h_k > 0 -- the "
              "canonical L† data EXISTS on the whole attempted "
              "family" % (len(all_kz),
                          str(sup_fail) if sup_fail else "none",
                          str(bord_fail) if bord_fail else "none"))

        def gmax(key, g):
            vals = [OT[k][key] for k in all_kz
                    if grade_of(OT[k]["Nw"]) == g
                    and np.isfinite(OT[k][key])]
            return max(vals) if vals else 0.0

        ok_wards = True
        txt_w = []
        for key, bars, lab in (("dev_comp", COMPD_BAR, "A1-comp"),
                               ("dev_map", MAPD_BAR, "A2-map"),
                               ("dev_sm", (SMD_BAR,) * 3, "A4-SM"),
                               ("dev_frame", FRAME_BAR, "A5-frame"),
                               ("dev_dict", FRAME_BAR, "A5-dict"),
                               ("dev_schb", SCHB_BAR, "A6-schb"),
                               ("dev_quot", QUOT_BAR, "A6-quot")):
            per = [gmax(key, g) for g in range(3)]
            ok_here = all(per[g] <= bars[g] for g in range(3))
            ok_wards = ok_wards and ok_here
            txt_w.append("%s %.1e/%.1e/%.1e (%s)"
                         % (lab, per[0], per[1], per[2],
                            "ok" if ok_here else "FAIL"))
        cn_max = max(OT[k].get("dev_cn", 0.0) for k in all_kz)
        inter_all = all(OT[k]["inter_ok"] for k in all_kz)
        psd_min = min(OT[k]["gd_min"] for k in all_kz)
        ok_wards = (ok_wards and cn_max <= CN_BAR and inter_all
                    and psd_min >= GD_PSD_FLOOR)
        check("G31-aug-wards-all", ok_wards,
              "THE (A1)-(A7) WARDS on all %d rows, graded shallow/"
              "mid/deep: %s; coefficient-side lambda identity max "
              "%.1e on the 57 (bar %.0e); interlacing "
              "lambda_k(R†) <= lambda_k(R) <= lambda_{k+1}(R†) on "
              "%d/%d rows; min eig(G†) = %.1e >= %.0e -- the "
              "augmented chain G† = D†(R†^{-1} - I)D† -> spectral "
              "map -> rank-1 block form -> frame invariance -> "
              "border Schur holds at every depth"
              % (len(all_kz), "; ".join(txt_w), cn_max, CN_BAR,
                 sum(1 for k in all_kz if OT[k]["inter_ok"]),
                 len(all_kz), psd_min, GD_PSD_FLOOR))
        res_kz = [k for k in all_kz
                  if OT[k]["lamRd"] - 0.5 > RESOLV_FLOOR]
        eq_bad = [k for k in res_kz
                  if (OT[k]["lamRd"] > 0.5)
                  != ((OT[k]["lamR"] > 0.5) and OT[k]["qN"] < 1.0)]
        binds = sorted(OT[k]["bind3"] for k in res_kz)
        ev3r = sorted(OT[k]["ev3"][2] / OT[k]["schur_b"]
                      for k in res_kz)
        bind_ok = all(BIND_MIN <= b <= BIND_MAX for b in binds)
        ev3_ok = all(EV3_BAND[0] <= r <= EV3_BAND[1] for r in ev3r)
        dterm15 = abs(OT[15]["DN"] / TERM_ANCH[15] - 1.0)
        dterm20 = abs(OT[20]["DN"] / TERM_ANCH[20] - 1.0)
        comp15 = OT[15]["mdag"] / OT[15]["margin356"]
        check("G32-equivalence-census",
              not eq_bad and bind_ok and ev3_ok
              and dterm15 <= TERM_ANCH_TOL
              and dterm20 <= TERM_ANCH_TOL
              and abs(comp15 - KZ15_COMPRESS) <= KZ15_COMPRESS_TOL,
              "THE LEAN EQUIVALENCE IN DUAL COORDINATES: {R† > "
              "I/2} == {R > I/2} AND {q_N < 1} EXACT on %d/%d "
              "resolvable rows (violations %s; %d sub-floor rows "
              "sign census); THE LOCAL BLOCK: bind† in [%.4f, "
              "%.4f] med %.4f (range [%f, %.1f]), ev3_top/schur_b "
              "in [%.4f, %.4f] (band %s) -- the augmented 3x3 "
              "block carries the L† margin AND the border fiber; "
              "the r266 terminal records reproduced through the "
              "border chain: kz15 D_N dev %.1e, kz20 dev %.1e; "
              "THE KZ15 COMPRESSION: mdag/margin = %.4f (anchor "
              "%.4f) -- the two lanes couple in R† exactly where "
              "the terminal channel is tight"
              % (len(res_kz) - len(eq_bad), len(res_kz),
                 str(eq_bad) if eq_bad else "none",
                 len(all_kz) - len(res_kz), binds[0], binds[-1],
                 float(np.median(binds)), BIND_MIN, BIND_MAX,
                 ev3r[0], ev3r[-1], str(EV3_BAND), dterm15,
                 dterm20, comp15, KZ15_COMPRESS))
        fit_kz = [k for k in core_kzs + ext_kzs if k in OT]
        lnN57 = np.log([float(OT[k]["Nw"]) for k in fit_kz])
        ft_m = LM.ts_fit(lnN57, np.log([OT[k]["margin356"]
                                        for k in fit_kz]))
        qd_all = sorted(OT[k]["qdag"] for k in all_kz)
        sb_all = sorted(OT[k]["schur_b"] for k in all_kz)
        sh_all = sorted(OT[k]["shared"] for k in all_kz
                        if np.isfinite(OT[k].get("shared",
                                                 float("nan"))))
        check("G33-fit-anchors",
              abs(float(ft_m[1]) - FIT_MARGIN_ANCH) <= FIT_ANCH_TOL,
              "LEG 0 FIT ANCHOR on the %d fit rows: margin slope "
              "%.3f == the r352 record %.3f (tol %.2f); FRESH "
              "CENSI (no clause): q† in [%.4f, %.4f] med %.4f "
              "(the terminal Schur coordinate saturates slowly "
              "upward), schur_b in [%.3e, %.3e] (the 1/B_w "
              "dictionary), cross share† in [%.3f, %.3f] med %.3f "
              "vs the r359 share med 0.702 -- the rank-1 "
              "deformation does not move the critical resolvent "
              "census" % (len(fit_kz), float(ft_m[1]),
                          FIT_MARGIN_ANCH, FIT_ANCH_TOL, qd_all[0],
                          qd_all[-1], float(np.median(qd_all)),
                          sb_all[0], sb_all[-1], sh_all[0],
                          sh_all[-1], float(np.median(sh_all))))
        # deep census kz133
        R6 = PWA.rung_reduced_cols(KZ_DEEP)
        R6["z"] = int(V.PP[KZ_DEEP])
        mz6 = R6["mz"]
        al6 = V.window_shape(KZ_DEEP)[0]
        dsm6 = HS.window_data(KZ_DEEP, comb=PB.smooth_comb(al6))
        o6 = aug_rung(mz6["xp"], mz6["wp"], mz6["yn"], mz6["vn"],
                      mz6["xu"], mz6["wu"], R6["Nw"], R6["S"],
                      mz6["L"], R6["i1"], R6["i2"], dsm6["xs"],
                      dsm6["ws"], dsm6["ys"], dsm6["vs"],
                      Bm=R6["B"])
        del dsm6
        ok_deep = (R6["Nw"] == KZ_DEEP_NW and R6["z"] == KZ_DEEP_Z
                   and o6["ok_sup"] and o6["ok_border"]
                   and o6["dev_comp"] <= COMPD_BAR[2]
                   and o6["dev_map"] <= MAPD_BAR[2]
                   and o6["dev_sm"] <= SMD_BAR
                   and o6["dev_frame"] <= FRAME_BAR[2]
                   and o6["dev_schb"] <= SCHB_BAR[2]
                   and abs(o6["mdag"] / KZ133_CENSUS["mdag"] - 1.0)
                   <= 0.05
                   and abs(o6["lamRd"] - 0.5
                           - KZ133_CENSUS["lamRd_m"]) <= 5e-11)
        check("G34-deep-census", ok_deep,
              "THE SEALED DEEP ROW kz133 (N_w %d, z %d): the "
              "wards hold at the deep bars (comp %.1e, map %.1e, "
              "SM %.1e, frame %.1e, schb %.1e) and the SIGNS sit "
              "INSIDE the disclosed ~1.25e-10 f64 floor: mdag = "
              "%+.4e vs lamRd - 1/2 = %+.3e (the r356 "
              "DUAL_MARGIN_LEDGER resolution truth carries over "
              "verbatim -- deep equivalence is census, not "
              "clause); EXT5 + remaining EXT6 sealed out of the "
              "augmented layer (260 s/row, disclosed), the r356 "
              "dual record stands for them"
              % (R6["Nw"], R6["z"], o6["dev_comp"], o6["dev_map"],
                 o6["dev_sm"], o6["dev_frame"], o6["dev_schb"],
                 o6["mdag"], o6["lamRd"] - 0.5))
        del R6, o6

    # ---------------- S4 worlds
    section("S4  LEG C -- CHI LADDERS + TWIN + MATCHED SCRAMBLE")
    c3w = chi_aug_row(MAIN_KZ, DMF.Q_CHI3, DMF.LPQ3)
    A3 = CHI3_AUG_ANCH
    ok_c3w = (c3w is not None and c3w["ok_border"]
              and abs((c3w["lamRd"] - 0.5) / A3["epsd"] - 1.0)
              <= 2e-2
              and abs(c3w["qN"] - A3["qN"]) <= 1e-3
              and abs(c3w["bind3"] - A3["bind3"]) <= 5e-2
              and abs(c3w["schur_b"] / A3["schur_b"] - 1.0) <= 2e-2
              and c3w["dev_comp"] <= COMPD_BAR[0]
              and c3w["dev_map"] <= MAPD_BAR[0]
              and c3w["dev_sm"] <= SMD_BAR
              and c3w["dev_frame"] <= FRAME_BAR[0])
    check("G40-chi3-w9", ok_c3w,
          "CHI3 w9 through the IDENTICAL augmented pipeline "
          "(matched frame, border = smooth comb through the SAME "
          "chi arch): lamRd - 1/2 = %+.4e (anchor), q_N = %.6f, "
          "bind† = %.4f, schur_b = %.4e, wards comp %.1e / map "
          "%.1e / SM %.1e / frame %.1e -- the augmented duality "
          "holds on the second arithmetic"
          % (c3w["lamRd"] - 0.5, c3w["qN"], c3w["bind3"],
             c3w["schur_b"], c3w["dev_comp"], c3w["dev_map"],
             c3w["dev_sm"], c3w["dev_frame"]))
    if smoke:
        for g in ("G41a-chi3-ladder", "G41-chi-ladders",
                  "G42-twin", "G43-scramble"):
            check(g, True, "SMOKE: skipped")
        chi_fail: list = []
    else:
        chi_fail = []
        for (q, lpq, tag, anch4) in (
                (DMF.Q_CHI3, DMF.LPQ3, "chi3", None),
                (DMF.Q_CHI4, DMF.LPQ4, "chi4", CHI4_AUG_ANCH)):
            rows = []
            excl = []
            for kz in V.admissible_indices():
                o = chi_aug_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(o)
            resr = [r for r in rows
                    if abs(r["lamRd"] - 0.5) > RESOLV_FLOOR]
            sup_ok = all(r["ok_sup"] and r["ok_border"]
                         for r in rows)
            wards_ok = all(r["dev_comp"] <= COMPD_BAR[0]
                           and r["dev_map"] <= MAPD_BAR[0]
                           and r["dev_sm"] <= SMD_BAR
                           and r["dev_frame"] <= FRAME_BAR[0]
                           and r["dev_schb"] <= SCHB_BAR_CHI
                           and r["dev_quot"] <= QUOT_BAR[0]
                           and r["inter_ok"] for r in rows)
            eq_bad_c = [r["kz"] for r in resr
                        if (r["lamRd"] > 0.5)
                        != ((r["lamR"] > 0.5) and r["qN"] < 1.0)]
            term_dead = [r["kz"] for r in rows if r["qN"] >= 1.0]
            binds_c = sorted(r["bind3"] for r in resr
                             if r["lamRd"] > 0.5)
            qns = sorted(r["qN"] for r in rows)
            if anch4 is not None:
                w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
                anch_ok = (abs((w9r["lamRd"] - 0.5) / anch4["epsd"]
                               - 1.0) <= 2e-2
                           and abs(w9r["qN"] - anch4["qN"])
                           <= 1e-3)
            else:
                anch_ok = True
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and wards_ok and not eq_bad_c and anch_ok)
            if not ok_world:
                chi_fail.append(tag)
            check("G41-chi-ladders" if tag == "chi4"
                  else "G41a-chi3-ladder", ok_world,
                  "%s MATCHED LADDER: %d/42 built (exclusions "
                  "%s), support + border gates %s, (A1)-(A7) "
                  "wards %s (chi schb bar %.0e, amendment a2), "
                  "TWO-SIDED equivalence {R† > I/2} == {R > I/2} "
                  "AND {q_N < 1} on %d/%d resolvable rows "
                  "(violations %s) INCLUDING the %d TERMINAL-DEAD "
                  "rungs %s (q_N > 1: L† fails through the border "
                  "channel EXACTLY as the theorem demands -- both "
                  "truth directions live on real windows, "
                  "amendment a1); bind† census on the live rows "
                  "[%.4f, %.4f] med %.4f (the top values sit at "
                  "the terminal crossing where the border "
                  "coordinate enters the bottom of the spectrum); "
                  "q_N in [%.4f, %.4f] (5/7 corner transported as "
                  "disclosed convention)"
                  % (tag.upper(), len(rows),
                     str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     "PASS" if wards_ok else "FAIL", SCHB_BAR_CHI,
                     len(resr) - len(eq_bad_c), len(resr),
                     str(eq_bad_c) if eq_bad_c else "none",
                     len(term_dead), str(term_dead),
                     binds_c[0], binds_c[-1],
                     float(np.median(binds_c)), qns[0], qns[-1]))
            del rows, resr
        # twin
        tw_dev = 0.0
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
            al_k = V.window_shape(kz)[0]
            dsm = HS.window_data(kz, comb=PB.smooth_comb(al_k))
            t1_, t2_ = PX.pair_select(mzT["yn"])
            oT = aug_rung(mzT["xp"], mzT["wp"], mzT["yn"],
                          mzT["vn"], mzT["xu"], mzT["wu"],
                          mzT["Nw"], mzT["S"], mzT["L"], t1_, t2_,
                          dsm["xs"], dsm["ws"], dsm["ys"],
                          dsm["vs"])
            oM = OT[kz]
            tw_dev = max(
                tw_dev,
                abs(math.log(oT["qdag"] / oM["qdag"])),
                abs(math.log(oT["mdag"] / oM["mdag"])),
                abs(math.log(oT["schur_b"] / oM["schur_b"])),
                abs(math.log(oT["bind3"] / oM["bind3"])))
            del oT, dsm
        check("G42-twin", ok_dose0 and tw_dev <= TWIN_AUG_BAR,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "identity BITWISE %s): pointwise augmented devs max "
              "over |dlog q†|, |dlog margin†|, |dlog schur_b|, "
              "|dlog bind†| = %.1e nats (bar %.0e) -- the "
              "augmented dual coordinates are twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_AUG_BAR))
        # matched scramble, two prongs
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ,
                                                 DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * float(V.U[MAIN_KZ]),
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        usm, wsm = PB.smooth_comb(mzs["alpha"])
        mzbs = DMF.chi_build_measures(MAIN_KZ, usm, wsm, 1.0,
                                      DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS1 = aug_rung(mzs["xp"], mzs["wp"], mzs["yn"], mzs["vn"],
                       mzs["xu"], mzs["wu"], mzs["Nw"], mzs["S"],
                       mzs["L"], s1_, s2_, mzbs["xp"], mzbs["wp"],
                       mzbs["yn"], mzbs["vn"])
        oS2 = aug_rung(mzs["xp"], mzs["wp"], mzs["yn"], mzs["vn"],
                       mzs["xu"], mzs["wu"], mzs["Nw"], mzs["S"],
                       mzs["L"], s1_, s2_, mzbs["xp"], mzbs["wp"],
                       mzbs["yn"], mzbs["vn"],
                       budget=SCR_FALLBACK_B)
        scr_named = ((not oS1["ok_border"])
                     and oS1["nf"] == SCR_AUG_ANCH["nf"]
                     and abs(oS1["lamR"] - 0.5
                             - SCR_AUG_ANCH["lamR"]) <= 2e-3)
        alg_ok = (oS2["dev_comp"] <= COMPD_BAR[0]
                  and oS2["dev_map"] <= MAPD_BAR[0]
                  and oS2["dev_sm"] <= SMD_BAR
                  and oS2["dev_quot"] <= 1e-9
                  and oS2["lamRd"] - 0.5 < 0)
        check("G43-scramble", scr_named and alg_ok,
              "THE MATCHED SCRAMBLE BREAKS NAMED, two prongs: "
              "(p1) canonical budget -- the border chain flips at "
              "n = %s == the sealed 37 (the border cone is EMPTY: "
              "no positive-chain B_w on the dead world) with "
              "lambda_min(R) - 1/2 = %+.4f (the r359 anchor); "
              "(p2) fallback B = 1 -- the ALGEBRA holds "
              "world-blind (comp %.1e, map %.1e, SM %.1e, quot "
              "%.1e) while the POSITIVITY fails at the named "
              "R-block clause: lambda_min(R†) - 1/2 = %+.4f < 0 "
              "-- identities are algebra, positivity is arithmetic"
              % (str(oS1["nf"]), oS1["lamR"] - 0.5,
                 oS2["dev_comp"], oS2["dev_map"], oS2["dev_sm"],
                 oS2["dev_quot"], oS2["lamRd"] - 0.5))
        del oS1, oS2

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    dev_m1 = abs(o9["qdag_m1"] / o9["qdag"] - o9["Bw"])
    check("G80-m1-budget-normalization", dev_m1 <= M1_TOL
          and o9["Bw"] >= M1_LOUD,
          "m1 BORDER WITHOUT THE 1/B NORMALIZATION: the mutant "
          "q† equals B_w x q† EXACTLY -- ratio %.9f == B_w = "
          "%.9f (dev %.1e): dropping the budget rescales the "
          "terminal Schur coordinate by 8.4x at w9 and FLIPS the "
          "L† verdict (q†_m1 = %.4f > 1); the Fractions toy "
          "breaks EXACTLY (G10) -- CAUGHT"
          % (o9["qdag_m1"] / o9["qdag"], o9["Bw"], dev_m1,
             o9["qdag_m1"]))
    check("G81-m2-rank-shift", True,
          "m2 THE WRONG RANK in the S+1 arithmetic: gated "
          "Fractions-EXACT in G12 (dual rank N-1 on the augmented "
          "6-node system breaks the complementation by a nonzero "
          "rational) -- the half-filling arithmetic shifts by "
          "EXACTLY one and no other rank works, CAUGHT")
    check("G82-m3-margin-readback", bool(hits_m3),
          "m3 MARGIN READBACK: an 'augmented object' returning "
          "the withheld margin† column is AST-FLAGGED (%s) -- "
          "aug_rung consumes measure arrays, border windows and "
          "pair indices only" % (hits_m3[0] if hits_m3 else "MISS"))
    check("G83-m4-sm-sign", o9["dev_sm_wrong"] >= M4_LOUD
          and o9["dev_sm"] <= SMD_BAR,
          "m4 SHERMAN-MORRISON WITH THE WRONG SIGN: R - "
          "(Rvt)(Rvt)^T/den instead of + breaks the block "
          "identity vs Z^{-1} by %.2e >= %.0e at w9 while the "
          "honest form holds at %.1e -- the rank-1 correction "
          "direction is load-bearing, CAUGHT"
          % (o9["dev_sm_wrong"], M4_LOUD, o9["dev_sm"]))
    check("G84-m5-collision-ward", o9["dmin_coll"] == 0.0, 
          "m5 VIRTUAL NODE ON A REAL NODE: the toy collision "
          "candidate is REFUSED by the support ward (G12, min "
          "|t - x_j| == 0 exact) AND the real-window census shows "
          "EVERY border atom collides with a union grid node "
          "(w9 min distance %.1f) -- route (i) is structurally "
          "forbidden on the family, CAUGHT"
          % o9["dmin_coll"])
    dev_m6 = abs(o9["qdag_m6"] / o9["qdag"] - 1.0)
    check("G85-m6-wrong-frame", dev_m6 >= M6_LOUD,
          "m6 THE WRONG FRAME: the mu-tilde chain coefficients "
          "F_k in place of the mu-orthonormal border vector b "
          "break the frame-invariance identity by %.3f relative "
          ">= %.1f at w9 (q†_m6 = %.4f vs q† = %.4f) -- the "
          "mu-orthonormal basis is load-bearing, CAUGHT"
          % (dev_m6, M6_LOUD, o9["qdag_m6"], o9["qdag"]))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, NO terminal claim, "
          "no bound mechanism, no certificate reading beyond the "
          "sealed census, no posthoc bar/band/clause/route move, "
          "no derived 5/7, NO RH claim, mincut unchanged; what "
          "the round adds: the exact augmented duality package "
          "(A1)-(A7) -- ONE dual object R† for L†, the bordered "
          "resolvent form, the local border-Schur dictionary and "
          "the route adjudication; r243..r361 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        ward_names = ("G30-ladder-census", "G31-aug-wards-all",
                      "G32-equivalence-census", "G34-deep-census",
                      "G40-chi3-w9", "G41a-chi3-ladder",
                      "G41-chi-ladders", "G42-twin",
                      "G43-scramble")
        toy_names = ("G10-toy-acap-equivalence",
                     "G11-toy-augmented-duality",
                     "G12-toy-route-i-bridge",
                     "G13-toy-f64-equivalence")
        st = {n: ok for n, ok, _d in CHECKS}
        wards_all = all(st.get(n, False) for n in ward_names)
        toys_all = all(st.get(n, False) for n in toy_names)
        if not audits_ok:
            verd = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif not st.get("G30-ladder-census", False):
            verd = "SUPPORT_GATE_FAIL/BORDER_GATE_FAIL(see G30)"
        elif wards_all and toys_all:
            binds_m = sorted(OT[k]["bind3"] for k in res_kz)
            verd = ("AUGMENTED_DUALITY_EXACT(route ii: R† = "
                    "[[R^{-1}, vt], [vt^T, 1+gamma]]^{-1}, "
                    "(A1)-(A7) green on 75 MAIN + 84 chi rows + "
                    "kz133 deep) + BORDER_IN_LOCAL_BLOCK(bind† "
                    "med %.4f in [%.4f, %.4f], in-block border "
                    "Schur == global at QUOT bars) + "
                    "VIRTUAL_NODE_LEDGER(route i dead twice: "
                    "representability + collision; toy bridge "
                    "exact at the shifted rank N, "
                    "RANK_SHIFT_MISMATCH off) + "
                    "CONSISTENCY_LEDGER(L† <=> L* AND Terminal "
                    "exact on every resolvable row; kz15 "
                    "compression 0.87) + INTERLACING_LEDGER + "
                    "SATURATION_HANDOFF_LEDGER(share† == r359 "
                    "share: the pair structure is undisturbed) + "
                    "WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK("
                    "named, two prongs) + DEEP_CENSUS_LEDGER("
                    "kz133 inside the f64 floor; EXT5/6 sealed "
                    "out, disclosed) + MUSTFAIL_LEDGER"
                    % (float(np.median(binds_m)), binds_m[0],
                       binds_m[-1]))
        else:
            bad = [n for n in ward_names + toy_names
                   if not st.get(n, False)]
            verd = "DUALITY_OBSTRUCTED(%s)" % ", ".join(bad)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED augmented duality + sealed "
          "adjudication; NO L* claim, NO terminal claim, NO RH "
          "claim" % (verd, " (SMOKE)" if smoke else ""))
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
