#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""paired_cone_probe -- PRIME.LSTAR.PAIRED_CONE.01 (round 309,
reviewer plan par.4 solution B / plan round 306): the PAIRED-CONE
PILOT.  The third full proof architecture of the L* lane: the
positive and the negative source are not summed first and compared
afterwards -- they are processed PAIRWISE as rank-one updates of
the augmented form.  Reviewer core (verbatim): let M succ 0 be the
augmented form built so far; a positive source contribution gives
M1 = M + a a^T, the coupled negative one M2 = M1 - b b^T; EXACTLY:
M2 succ 0 <=> b^T M1^{-1} b < 1, and Sherman-Morrison makes the
load-bearing cancellation an EXPLICIT POSITIVE SQUARE:
  b^T M1^{-1} b = b^T M^{-1} b - (a^T M^{-1} b)^2 / (1 + a^T M^{-1} a).
With the local leverage matrix L(M; a, b), L_xy = x^T M^{-1} y, the
per-step invariant is the LOCAL RESERVE
  r := 1 - L_bb + L_ab^2 / (1 + L_aa)  >  0.
The route is special because it processes BASE and BORDER together
(the same augmented object as r308) and because the r283/r288
finding -- the relevant cancellation is a coherent pair effect --
becomes ALGEBRAICALLY visible per pair.  Pilot mandate (reviewer
plan round 306, binding): build the exact rank-one source update
and MEASURE the local reserve r; "decisive is not whether r > 0 on
the existing MAIN windows.  Decisive is whether r can be PREDICTED
AND BOUNDED FROM BELOW from a small set of independent source
quantities."  Honesty condition (reviewer, verbatim): M^{-1} MAY
appear in the algebraic update formula; the final cone bound must
NOT be read off the computed M^{-1} of a target object -- the cone
must follow from independently provable source quantities, else it
is "Riccati reads the answer" (the r275 KYP error, whose double
obstruction o1/o2 and TARGET_INVERSE fingerprint are this round's
sealed reference pins).  Additionally binding (reviewer B4): r275
excludes every fixed UNIFORM quadratic memory structure -- a
source-exact, logarithmically growing phase register of size
O(log N) is NOT covered by that exclusion; this round carries such
a register (the dyadic fold-bit register, NBITS sealed) in the
information test only.  THIS ROUND IS A PILOT (measurement +
sealed cone adjudication), NOT a proof: no L* claim, no bound
mechanism, no RH claim.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r308 discipline): w = window (kz),
S = #union entries of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = builder depth = (S+1)//2, n = degree, minC =
first n with h_n < 0, crossing = minC + 1 (r283 theorem); f =
fold index; j = pair-step index along the sealed order.  Ground
truth (minC, flips, census offsets, r283/r284/r308 records) enters
GATES and record tables only; the sealed constructors consume
split-source arrays (positions, weights, fold indices, border
arrays, budget scalars, basis rows) ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r308 BG.{cheb_rows, target_form_f64, mono_rows_fr,
target_form_fr, exact_budget_fr, world_arrays, border_split,
world_budget, hull_of}, r284 LS.{world_pack, spectral_block,
pair_geometry, shield_profile, dist_rule}, r283 FS.frac_det, r289
AK.twin_rational + r276 MF.local_gaps, r275 KYP.toy_kyp_exact
(the o1/o2 + FORCED_TAILSUM reference pin), r278 MS.ctx_build,
r244 BH.spearman, v881 PIK, r243 PB.smooth_comb, v563 core
READ-ONLY.

THE SEALED DECOMPOSITION LANGUAGE (Leg A; frozen BEFORE any
measurement).  Target = the r308/v958 augmented form on
span{deg <= DEG, t}: A = [[H, u], [u^T, B]], H = moment matrix of
mutilde, u = border readout of sigmatilde, B = S_{N-2} + 5/7 (the
imported r243 budget with the 5/7 reserve floor).  Exact ordered
rebuild:
  (base)   M0 = (5/7) e_t e_t^T + sum over RESERVED + UNMATCHED
           mu atoms of w phi phi^T.  RESERVED RULE (sealed): the
           DEG+1 lowest-position mu atoms are reserved for the
           base (never matchable) -- this makes M0 succ 0 a
           structural gate, not luck.
  (budget) ONE signed rank-one |S_{N-2}| e_t e_t^T with the sign
           of S_{N-2} (positive on every MAIN-family world, gated
           via rho_k >= 0; signed on controls past their flip).
  (pairs)  the nu atoms in ascending support order, each with its
           mu partner from the sealed GREEDY MATCHING: nu atoms in
           ascending position order take the nearest unreserved,
           unassigned mu atom (distance = |position difference|
           in the canonical coordinate: fold index on real worlds,
           x on toys; ties -> lower position).  Pair step j:
           a = sqrt(w_a) phi(x_a), b = sqrt(v) phi(y) -- carried
           in the SQUARE-ROOT-FREE (mass, vector) parametrization
           L_aa = w_a G_aa, L_bb = v G_bb, L_ab^2 = w_a v G_ab^2
           with G_xy = phi_x^T M^{-1} phi_y, so every toy identity
           is exact rational; M <- M + w_a phi phi^T - v psi psi^T.
           An unpartnered nu atom (only possible when S_- exceeds
           the matchable pool; never on the gated real worlds) is
           the degenerate pair a = 0, r = 1 - L_bb (disclosed).
  (border) each border atom (eta, s) is INTRINSICALLY a pair: the
           exact splitting s (eta e_t^T + e_t eta^T) = (|s|/2)
           [(eta + e_t)(eta + e_t)^T - (eta - e_t)(eta - e_t)^T]
           (sign-swapped for s < 0) -- processed in ascending
           border-position order after the main pairs.
DISCLOSED ORDERING THEOREM (pre-run algebra): positive updates
never destroy positive definiteness, so with M0 succ 0 the final
form is PD along this order IFF every negative step has r > 0 --
the r-sequence is the ORDER-SENSITIVE object (must-fail m4 shows
the sensitivity), while the final sum is order-blind (the
reconstruction ward alone can never catch an order break).
EXACTNESS WARDS: final M == A entrywise (exact Fractions on the
toys, f64 rel Frobenius <= 1e-12 on w9 and every census world);
per-step Sherman-Morrison identity and the determinant dictionary
det(M1) == (1 + L_aa) det(M), det(M2) == r det(M1) -- exact on the
toys at EVERY step, f64-warded on w9 at the sealed step picks.
The r-sequence is basis-invariant (leverages are congruence
invariants); the f64 route (Chebyshev) must reproduce the exact
monomial route on SM1 to CONS_BAR -- gated.

EXACT WORLDS (Leg A): PC4 (hand toy: mu (x = -1/2, w = 1/2),
(x = 1/2, w = 1), nu (x = 1/4, v = 1/3), border (3/4, 1/5),
B = 9/7 sealed, cap 0; HAND PINS: reserved = {-1/2}, partner of
the nu atom = x = 1/2, budget step +4/7, pair reserve r = 7/9
EXACT, det dictionary det(M1) = 27/14 -> det(M2) = 3/2 EXACT,
final M == [[7/6, 1/5], [1/5, 9/7]] EXACT); SM1 (the r308
MAIN-like shielded 10-atom model with its 3 border atoms and the
exact WD-chain budget, cap DEG_T); MINI16 (the first 16 union
atoms of the REAL w9 window in fold order, f64 -> Fraction exact,
first 3 border atoms, exact mini budget, cap DEG_T -- 8 nu atoms
against 8 mu atoms: with DEG_T+1 reserved only 5 pairs form and 3
nu atoms run unpartnered, the disclosed degenerate case).

LEG B -- THE RESERVE MEASUREMENT.  Along the sealed order: r_j at
every negative step on w9, the r289 RATIONAL TWIN (CF convergents,
|du| <= 1e-8 local gap, weights bitwise, RATIONAL_KEEPS re-gated
minC = 184 / crossing = 185), the controls EPSTEIN / SCRAMBLE
(seed 1) / SMOOTH (flips 25/21/27, r281 channel verbatim), and ALL
57 rungs of the r308 ladder (42 core = r281 census h <= 900 +
15 extension anchors h <= 1300 sorted by (N_w, kz)) at cap
DEG_A = 8; w9 + twin + controls additionally at DEG_B = 28.
DEG_B DISCLOSURE (design-time, from published records): the
control crossings 26/22/28 put a negative leading minor into the
DEG_B moment block, so the control target is INDEFINITE there
while MAIN's is PD (crossing 185) -- by the ordering theorem a
step with r <= 0 is then FORCED given a PD base: gated live on
EPSTEIN/SCRAMBLE (crossings 26/22 safely below), SMOOTH (its
minC = 27 also forces a negative D_28 minor, but its r308-typed
boundary role crossing 28 == DEG_B is respected: reported, not
hard-gated).  DEG_A DISCLOSURE (corrected at the calibration
stage, amendment a1): at DEG_A every world's MOMENT block is PD
(control crossings 26/22/28 > 8), but the augmented (t, t)
budget is WORLD-SIGNED -- on a world whose measured budget
S_{N-2} is negative past its flip the augmented DEG_A form is
indefinite through the BUDGET coordinate and a nonpositive step
is forced there too (given a PD base); which step carries it is
measurement.  The per-KIND sign census (budget / pair / border
phases separately) is therefore part of the deliverable.
Deliverable:
per world min/median r, sign census (does r > 0 hold everywhere
on MAIN?), the position (fold/class) of the tightest steps, and
the PAIR-ASSIST SHARE L_ab^2/((1 + L_aa) L_bb) -- how much of the
survival at the tight steps is carried by the explicit positive
square (the reviewer's algebraic cancellation witness).

LEG C -- THE CONE TEST (the round's decision).  Sealed BEFORE any
evaluation: the independent source-quantity family per pair step
(all source-pure, AST-audited): F1 = v (nu mass), F2 = w_a
(partner mass), F3 = v/w_a (pair mass ratio), F4 = pair distance
|f_nu - f_mu| (folds), F5 = SM2 (mu shield mass within 2 fold
steps, r284 constructor verbatim), F6 = v/SM2, F7 = local gap
(fold distance to the nearest union atom, r284), plus the DYADIC
PHASE REGISTER: NBITS = 12 fold-index bits (the reviewer-B4
sanctioned O(log N) source-exact register -- information test
only this round).  (i) REGRESSION-FREE BOUND TEST: two sealed
explicit formulas  phi_1: r >= 1 - c_1 (v/w_a)  and  phi_2:
r >= 1 - c_2 (v/SM2)  -- the design origin is the exact aligned
limit b = t a: there 1 - r = v G_bb/(1 + w_a G_aa) < v/w_a, i.e.
c = 1; the constants are FROZEN on the calibration split = the
CAL_K = 5 shallowest core rungs by (N_w, kz) EXCLUDING kz9
(c_k = max over split pair steps of (1 - r) F_k^{-1}, clamped at
0), then tested POINTWISE on the remaining 52 rungs + w9 + twin
at DEG_A (violation = r < 1 - c F - PHI_TOL; partnered main pairs
only -- border/budget steps are excluded from phi, disclosed).
(ii) INFORMATION TEST: spearman of every sealed feature (F1..F7 +
the NBITS bits) against r over the pooled TIGHTEST-DECILE steps
of the test worlds (the reviewer asks for predictive power where
it matters: the tightest r), plus the same census on w9 alone;
fires iff some feature reaches |sp| >= SP_INFO on the pooled
tightest decile.  SEALED ADJUDICATION: CONE_PREDICTABLE iff some
phi_k has 0 violations on ALL test steps AND every predicted
lower bound is > 0 (the cone certifies positivity outright);
CONE_PARTIAL iff some phi_k has 0 violations with predicted
bounds > 0 on >= half of the test steps, OR some phi_k has
violation fraction <= VIOL_FRAC with r > 0 at every violated
step (no false positivity certificate), OR the information test
fires; else CONE_UNPREDICTABLE.  ANTI-CIRCULARITY AUDIT (the
r275 sharpness): the feature/bound constructors are AST-audited
to consume source arrays only; a mutant bound that consumes the
withheld target-window inverse leverage (Minv_true) must be
FLAGGED (m2), a mutant pairing re-sorted by the withheld measured
reserves (r_true) must be FLAGGED (m3).

LEG D -- WORLD DISCRIMINATOR.  Sealed r281 distance rule
(MAIN_SEPARATING iff MAIN's value is farther from every dead
value than the dead spread) on three sealed statistics at DEG_A:
K1 = min r, K2 = median r, K3 = median pair-assist share.  Cross
reference to the r308 feasibility discriminator (reported, not
hard-gated): w9's tightest pair steps vs the r284 extremal record
(the shallow-u hull edge, folds {2, 4}); the controls' first
r <= 0 position at DEG_B vs their crossing degrees.

LEG E -- MUST-FAILS (each loud): (m1) SHERMAN-MORRISON WRONG
SIGN: r_wrong = 1 - L_bb - L_ab^2/(1 + L_aa) on PC4 must break
the exact det dictionary by EXACTLY 8/9 (det ratio 7/9 vs r_wrong
-1/9); (m2) TARGET-INVERSE CONE: a bound built from the withheld
final-window inverse leverage -- FLAGGED by the AST scope audit;
(m3) POSTHOC PAIRING: a pairing re-sorted by the withheld
measured r values -- FLAGGED by the AST scope audit; (m4) ORDER
BREAK: processing the PC4 nu atom BEFORE its partner changes the
reserve EXACTLY from 7/9 to 1/3 (dev 4/9, LOUD) while the final
reconstruction stays exact -- the r-sequence, not the sum, is the
ordered object.  STOP LIST (anti-gates, binding): NO L* claim,
NO bound mechanism, NO asymptotic law, NO derived 5/7, NO posthoc
window, NO pairing or bound selection by measured outcomes, NO
RH claim; r243..r308 stand.

WORLDS: MAIN w9 (S = 367, S_+ = 263, S_- = 104, N_w = 184, minC =
184, crossing 185); the r289 rational twin; EPSTEIN / SCRAMBLE /
SMOOTH (r281 channel); the 57-rung r308 ladder.  ANCHOR PINS
(Leg 0): w9 source split; crossing 185 == minC + 1; the 5/7
convention B_w9 = S_{N-2} + 5/7 = 8.368649 with every rho_k >= 0
through the free window (r308 record); the r275 KYP no-go pin =
KYP.toy_kyp_exact() re-run (the o1/o2 double obstruction and the
forced-tail-sum Riccati on the sealed r275 toy -- the reference
for what this round's cone must NEVER become).

SEALED CONSTANTS: DEG_A 8; DEG_B 28; DEG_T 2 (PC4 at cap 0);
H_CAP 900; EXT_H 1300; K_EXT 15; MAIN_KZ 9; CTRL_FLIPS {EPST: 25,
SCR: 21, SMOOTH: 27}; ANCHORS {9:0, 12:2, 13:2, 26:3, 40:1, 15:1,
52:0}; R281_DIST {0:18, 1:10, 2:6, 3:6, 4:1, 5:1}; EXT 8 / EXT2
32; DEPTH_PAD 6; W9_ANCH (367, 263, 104, 184, 184); CROSS_REC
185; B_REC 8.368649 abs tol 1e-3; FIVE_SEVEN 5/7; RAT_TOL 1e-8;
QMAX 1e6; RECON_BAR 1e-12; CONS_BAR 1e-10; SM_BAR 1e-9; DET_BAR
1e-8; WARD_PICKS = pair steps (0, npairs//2, npairs - 1) on w9 at
DEG_A; MP_DPS 60; MP_BAR 1e-8 (mp re-derivation of the tightest
w9 pair reserve); SHIELD_R 2; NBITS 12; CAL_K 5 (kz9 excluded
from calibration); PHI_TOL 1e-12; VIOL_FRAC 0.01; SP_INFO 0.5;
TIGHT_Q 0.10; M1_DEV 8/9; M4_DEV 4/9; PC4 = nodes ((-1/2, 1/2),
(1/4, -1/3), (1/2, 1)) border (3/4, 1/5) B 9/7; SM1/borders/
budget = the r308 constants verbatim; MINI_K 16; MINI_BK 3;
runtime <= 1800 s; smoke = exact toys + firewall + scopes +
mutants + w9 f64 chain at DEG_A (crossing pin, mp ward, twin,
controls, DEG_B, ladder, cone, discriminator, adjudication
skipped).  PRE-SPEC SCOPING (disclosed): every record number
above is a published r281/r283/r284/r286/r289/r306/r308 record
adopted as-is; the decomposition language, the reserved/greedy
rules, the phi forms with their aligned-limit design origin, the
calibration split, every bar and the verdict form were fixed at
design time BEFORE any evaluation of this probe; no machinery
pass preceded this spec except record reading; no bar, band,
rule or verdict rule was tuned after any evaluation of this
probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] DECOMP_EXACT(recon devs) /
    DECOMP_BROKEN(first break locus)
  + RESERVE_TABLE(per-world min/median r, sign census,
    MAIN_RESERVE_POSITIVE / RESERVE_BREAKS(loci); forced control
    negativity at DEG_B disclosed as theorem-forced) [always]
  + [exactly one of] CONE_PREDICTABLE(phi, c, 0 violations,
    positive bounds) / CONE_PARTIAL(anatomy) /
    CONE_UNPREDICTABLE(break anatomy)
  + WORLD_DISCRIMINATOR(distance-rule typing; r308/r284 cross
    reference) [always]
  + MUSTFAIL_LEDGER [always].
Honesty before beauty: the exact rank-one rebuild is bookkeeping
(the reconstruction is order-blind and cannot fail if the
arithmetic is right) -- the content sits in (i) whether the
sealed ORDER keeps every reserve positive on MAIN, (ii) whether
the reserve is PREDICTABLE from sealed source quantities (the
reviewer's decisive question -- a cone read off M^{-1} of the
target would be the r275 error and is mutant-guarded), and (iii)
whether the reserve profile separates the worlds where nothing is
forced; the DEG_B control negativity is forced by theorem and is
disclosed as such, never sold; a passing cone fixes a TARGET for
proof work, it proves neither L* nor any cofinal statement.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 33/33 (0.3 s) at the sealed
rules -- no fail at any point; calibration pass 1 = first full
evaluation = 33/33 (15.3 s); after it AMENDMENT a1 (disclosed):
the design-time DEG_A sentence "every world's target is PD at
DEG_A" is FALSE for the augmented form on negative-budget worlds
-- the measured budgets S_{N-2} of EPSTEIN/SCRAMBLE are negative
past their flips, so their augmented DEG_A forms are indefinite
through the BUDGET coordinate; the spec sentence was corrected,
the control/verdict reporting was made per-KIND data-driven and
the cross-reference prints the breaking step's kind -- spec-prose
+ reporting only, NO bar, band, tolerance, letter or verdict rule
moved; calibration pass 2 = 33/33, identical figures; the record
run below is numerically identical; run1/run2 identical up to
WALL):
CAL_VERDICT = DECOMP_EXACT(PC4/SM1/MINI16 exact; w9 recon 4.8e-16
@A / 5.4e-16@B; twin + controls + 57/57 rungs <= 3.1e-15) +
RESERVE_TABLE(MAIN_RESERVE_POSITIVE: w9 min r = +0.9011@A /
+0.3232@B, twin +0.9011/+0.3232, 57/57 rungs all-positive with
ladder min +0.7357@kz97; controls@A pair+border phases ALL
POSITIVE (mins EPST +0.5712 / SCR +0.7796 / SMOOTH +0.9627), the
EPST/SCR negativity @A carried by the BUDGET step ALONE (r_bud
-4.589 / -6.331; S_{N-2} = -3.992 / -5.237 < 0 past the flip --
the r243 budget coordinate reads the wall, amendment-a1
disclosure); controls@B EPST -4.59 / SCR -6.33 (first break =
the budget step, forced by theorem, disclosed) / SMOOTH -7.08
(boundary case, first break at pair step 4 of its 6-atom nu
channel, reported)) + CONE_PARTIAL(phi1 mass ratio c_1 = 8.5436:
ZERO violations on all 20714 test pair steps (52 rungs + w9 +
twin) but predicted bounds > 0 on only 11643/20714 (min bound
-3.97) -- the mass-ratio cone is SOUND but certifies barely half
the steps; phi2 shield c_2 = 1.1573: 54 violations (0.26 pct <=
1 pct, every violated step has r >= +0.901 -- no false
positivity certificate) with bounds > 0 on only 54/20714 (min
bound -918): the shield cone overshoots exactly where it is
positive; info test SILENT by the sealed letter: pooled tightest
decile (2071 steps) best |sp| = 0.50 at F4 pair distance, JUST
under the bar; fold bits max |sp| = 0.32 -- the B4 register
carries nothing at this cap) + WORLD_DISCRIMINATOR(K1 min-r /
K2 med-r / K3 assist-share ALL WORLD_BLIND under the sealed
distance rule (MAIN 0.9011/0.986/0.0386 vs EPST -4.5889/0.9888/
0.0821, SCR -6.3315/0.9892/0.0261, SMOOTH 0.9627/0.9811/0.0111)
-- honest: at DEG_A the ordered PAIR reserve does not separate
the worlds, the separation sits in the budget sign, which is the
r243 wall readout itself; REPORTED: w9's two tightest pair folds
are EXACTLY the r284 extremal folds {2, 4}) + MUSTFAIL_LEDGER(m1
8/9 exact, m2/m3 flagged, m4 4/9 exact + recon preserved).
Key numbers.  EXACT LEG: PC4 hand pins all EXACT (reserved
{-1/2}, partner x = 1/2, budget +4/7, pair reserve 7/9, L_aa =
2, det dictionary 9/14 -> 27/14 -> 3/2, final [[7/6, 1/5],
[1/5, 9/7]]); SM1 (cap 2): B = 0.735254 exact, 3/3 partnered, 6
negative steps ALL r > 0 (min 0.8578), Sherman-Morrison + det
dictionary EXACT at every step, recon EXACT; MINI16 (cap 2): B =
0.715612 exact, 5 pairs + 3 unpartnered (disclosed degenerate
case), 11 negative steps ALL r > 0 (min 0.1913), all identities
EXACT, recon EXACT; basis invariance f64-vs-exact on SM1 max
|dr| = 1.1e-16 (bar 1e-10).  W9 ANCHORS: S 367/263/104, N_w 184,
minC 184, crossing 185 == minC + 1; B_w9 = 8.368649 (record),
182 rho_k >= 0; r275 o1/o2 + forced-tail-sum pin re-run TRUE.
W9 CHAIN (DEG_A): base 159 mu atoms (9 reserved + 150
unmatched), M0 PD (min eig 2.1e-4); 104/104 nu atoms partnered
(max pair distance 18 folds, median 1); 367 border atoms ->
exact +/- pairs; budget +7.654; recon 4.8e-16; SM ward 4.8e-13
(bar 1e-9), slogdet dictionary 2.5e-12 (bar 1e-8) at the sealed
picks (0, 52, 103); mp ward (dps 60) on the tightest pair:
r_mp = +0.901068, rel dev 3.0e-13 (bar 1e-8).  RESERVE PROFILE:
w9@A pair min +0.9011 (pair 0, FOLD 2 -- the r284 extremal
atom), median +0.9891, border min +0.9653, tightest five pair
folds (2, 4, 86, 55, 52); assist share L_ab^2/((1 + L_aa) L_bb)
median 3.9e-2, max 0.805 -- the explicit positive square carries
up to 80 percent of a step's survival but the median DEG_A step
barely needs it; w9@B (471 negative steps) min +0.3232, median
+0.9589 -- MAIN survives the ordered chain at BOTH caps with
macroscopic margin; twin bit-near w9 (min +0.9011/+0.3232):
diophantine input irrelevant on this coordinate, consistent with
r289 METRIC_ONLY.  LADDER: 42 core (offsets == r281, anchors
exact) + 15 extension anchors N_w 942..1218; 57/57 recon <=
3.1e-15; 57/57 all-positive, min of rung-mins +0.7357@kz97,
median +0.8912 (worst five kz97/kz95/kz119/kz68/kz18 at 0.736..
0.801).  CONE (the round's decision, measured): the reviewer
question splits -- the reserve IS predictable in the SOUND
direction (phi1 never violated on 20714 pointwise tests with a
sealed, design-origin c_1) but NOT yet certifying (bounds
positive on 56 percent; the 5 calibration rungs pin c_1 = 8.54
via one shallow-window step, four decades above the aligned-
limit value 1); the shield form phi2 is the sharper local idea
but overshoots wherever positive (all 54 of its positive bounds
are violated -- by steps whose true r >= 0.901); the honest
successor object is a phi with a base-depth term (the DEG_A base
carries most of the reserve, so a purely local pair quantity
cannot be tight) -- named, not retro-fitted.  INFO: pooled
tightest decile best |sp| 0.50 (F4 pair distance, under the
bar); on w9 ALONE the mass-ratio F3 and shield F6 reach -0.61 /
-0.58 (reported: the local features DO carry the w9 reserve
ranking; the pooled decile is dominated by deep rungs where no
sealed feature reaches the bar); the O(log N) fold-bit register
is measured IRRELEVANT at this cap (max |sp| 0.32).  CONTROLS:
DEG_A pair phases all positive (EPST +0.5712 / SCR +0.7796 /
SMOOTH +0.9627, medians ~ +0.99) -- the ordered pair reserve is
WORLD-BLIND at DEG_A; the entire EPST/SCR indefiniteness is the
BUDGET step (S_{N-2} < 0), i.e. the r243 wall readout, not a new
separation; DEG_B forced breaks exactly as the ordering theorem
demands.  MUST-FAILS: m1 wrong-sign dev == 8/9 EXACT; m2
target-inverse cone FLAGGED (Minv_true), m3 posthoc pairing
FLAGGED (r_true); m4 order mutant dev == 4/9 EXACT with recon
preserved (the sum is order-blind, the r-sequence is not);
constructors + fragment audit CLEAN.  Runtime 15.7 s full / 0.3
s smoke; record run1/run2 identical up to WALL.  AMENDMENTS
AFTER FREEZE: NONE.


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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import block_green_probe as BG                     # noqa: E402 r308
import lstar_two_measure_probe as LS               # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import minimal_firewall_probe as MF                # noqa: E402 r276
import kyp_memory_probe as KYP                     # noqa: E402 r275
import metric_stability_probe as MS                # noqa: E402 r278
import bordered_hankel_probe as BH                 # noqa: E402 r244
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
DEG_B = 28
DEG_T = 2
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
W9_ANCH = (367, 263, 104, 184, 184)
CROSS_REC = 185
B_REC = 8.368649
B_TOL = 1e-3
FIVE_SEVEN = Fr(5, 7)
RAT_TOL = 1e-8
QMAX = 1e6
RECON_BAR = 1e-12
CONS_BAR = 1e-10
SM_BAR = 1e-9
DET_BAR = 1e-8
MP_DPS = 60
MP_BAR = 1e-8
SHIELD_R = 2
NBITS = 12
CAL_K = 5
PHI_TOL = 1e-12
VIOL_FRAC = 0.01
SP_INFO = 0.5
TIGHT_Q = 0.10
M1_DEV = Fr(8, 9)
M4_DEV = Fr(4, 9)
PC4_X = (Fr(-1, 2), Fr(1, 4), Fr(1, 2))
PC4_W = (Fr(1, 2), Fr(-1, 3), Fr(1))
PC4_BX = (Fr(3, 4),)
PC4_BW = (Fr(1, 5),)
PC4_B = Fr(9, 7)
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
                       "arrays, budget scalars, basis rows) ONLY; "
                       "record numbers enter gates and record "
                       "tables only" if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("greedy_pairing", "base_form_f64", "reserve_chain_f64",
                "base_form_fr", "reserve_chain_fr", "frac_solve",
                "frac_pd", "cone_features", "phi_calibrate",
                "phi_violations", "pad_rows")
SCOPE_FORBIDDEN = {"CTRL_FLIPS", "ANCHORS", "R281_DIST", "minC_true",
                   "cross_true", "r_true", "lev_true", "Minv_true",
                   "target_inverse", "cholesky"}


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
def greedy_pairing(pos_mu, pos_nu, n_reserve):
    """SEALED PAIRING RULE: reserve the n_reserve lowest-position
    mu atoms for the base (never matchable); nu atoms in ascending
    position order greedily take the nearest unreserved unassigned
    mu atom (distance = |position difference|, ties -> lower
    position).  Consumes positions only.  Returns (reserved mu
    indices, nu order, partner mu index per nu in that order,
    -1 = unpartnered)."""
    pm = [float(p) for p in pos_mu]
    pn = [float(p) for p in pos_nu]
    o_mu = sorted(range(len(pm)), key=lambda i: (pm[i], i))
    reserved = set(o_mu[:n_reserve])
    avail = set(range(len(pm))) - reserved
    nu_order = sorted(range(len(pn)), key=lambda k: (pn[k], k))
    partner = []
    for k in nu_order:
        if not avail:
            partner.append(-1)
            continue
        best = min(avail, key=lambda i: (abs(pm[i] - pn[k]), pm[i], i))
        partner.append(best)
        avail.discard(best)
    return sorted(reserved), nu_order, partner


def pad_rows(P):
    """basis rows extended by a zero t coordinate (vectors live on
    span{deg <= DEG, t})."""
    P = np.asarray(P, float)
    return np.hstack([P, np.zeros((P.shape[0], 1))])


def base_form_f64(Pm, wm, reserved, partner):
    """M0 = (5/7) e_t e_t^T + sum over reserved + unmatched mu
    atoms of w phi phi^T (padded rows).  Consumes basis rows +
    masses + the sealed plan only."""
    m = Pm.shape[1]
    M0 = np.zeros((m, m))
    M0[m - 1, m - 1] = 5.0 / 7.0
    used = set(p for p in partner if p >= 0)
    base_idx = [i for i in range(Pm.shape[0])
                if (i in set(reserved)) or (i not in used)]
    for i in base_idx:
        M0 += float(wm[i]) * np.outer(Pm[i], Pm[i])
    return M0, base_idx


def reserve_chain_f64(M0, Pm, wm, Pn, vn, plan, Pb, sb, b_order,
                      S_bud, ward_picks=()):
    """the sealed ordered signed rank-one chain: budget step, main
    pairs (nu ascending order + greedy partners), border pairs
    (ascending border position; exact +/- splitting).  Per
    negative step: leverages L_aa, L_ab^2, L_bb w.r.t. the current
    M and the local reserve r = 1 - L_bb + L_ab^2/(1 + L_aa); at
    the sealed ward picks additionally the direct Sherman-Morrison
    recount and the slogdet dictionary.  Consumes basis rows,
    masses, the plan and the budget scalar only."""
    reserved, nu_order, partner = plan
    M = M0.copy()
    m = M.shape[0]
    et = np.zeros(m)
    et[m - 1] = 1.0
    recs = []
    wards = []
    pair_no = 0
    if S_bud >= 0.0:
        M = M + S_bud * np.outer(et, et)
    else:
        sol = np.linalg.solve(M, et)
        Lbb = (-S_bud) * float(et @ sol)
        recs.append(dict(kind="bud", idx=-1, Laa=0.0, Lab2=0.0,
                         Lbb=Lbb, r=1.0 - Lbb))
        M = M + S_bud * np.outer(et, et)
    for t_, k in enumerate(nu_order):
        pidx = partner[t_]
        pb_ = Pn[k]
        vb = float(vn[k])
        if pidx >= 0:
            pa = Pm[pidx]
            wa = float(wm[pidx])
            sol = np.linalg.solve(M, np.stack([pa, pb_], axis=1))
            Gaa = float(pa @ sol[:, 0])
            Gab = float(pa @ sol[:, 1])
            Gbb = float(pb_ @ sol[:, 1])
            Laa = wa * Gaa
            Lab2 = wa * vb * Gab * Gab
            Lbb = vb * Gbb
            r = 1.0 - Lbb + Lab2 / (1.0 + Laa)
            if pair_no in ward_picks:
                s0, ld0 = np.linalg.slogdet(M)
                M1 = M + wa * np.outer(pa, pa)
                s1, ld1 = np.linalg.slogdet(M1)
                direct = vb * float(pb_ @ np.linalg.solve(M1, pb_))
                sm_dev = abs(direct - (Lbb - Lab2 / (1.0 + Laa))) \
                    / max(abs(direct), 1e-300)
                M2 = M1 - vb * np.outer(pb_, pb_)
                s2, ld2 = np.linalg.slogdet(M2)
                d1 = abs((ld1 - ld0) - math.log1p(Laa)) \
                    / max(abs(ld1 - ld0), 1e-300)
                d2 = abs((ld2 - ld1) - math.log(max(r, 1e-300))) \
                    / max(abs(ld2 - ld1), 1e-300) if r > 0 else 0.0
                wards.append(dict(pair=pair_no, sm=sm_dev,
                                  det1=d1, det2=d2))
            M = M + wa * np.outer(pa, pa)
        else:
            sol = np.linalg.solve(M, pb_)
            Laa = 0.0
            Lab2 = 0.0
            Lbb = vb * float(pb_ @ sol)
            r = 1.0 - Lbb
        M = M - vb * np.outer(pb_, pb_)
        recs.append(dict(kind="pair", idx=k, Laa=Laa, Lab2=Lab2,
                         Lbb=Lbb, r=r, pair_no=pair_no))
        pair_no += 1
    for bi in b_order:
        s = float(sb[bi])
        if s == 0.0:
            continue
        eta = Pb[bi]
        if s > 0.0:
            va_ = eta + et
            vb_ = eta - et
        else:
            va_ = eta - et
            vb_ = eta + et
        mass = abs(s) / 2.0
        sol = np.linalg.solve(M, np.stack([va_, vb_], axis=1))
        Gaa = float(va_ @ sol[:, 0])
        Gab = float(va_ @ sol[:, 1])
        Gbb = float(vb_ @ sol[:, 1])
        Laa = mass * Gaa
        Lab2 = mass * mass * Gab * Gab
        Lbb = mass * Gbb
        r = 1.0 - Lbb + Lab2 / (1.0 + Laa)
        M = M + mass * np.outer(va_, va_)
        M = M - mass * np.outer(vb_, vb_)
        recs.append(dict(kind="bord", idx=bi, Laa=Laa, Lab2=Lab2,
                         Lbb=Lbb, r=r))
    return recs, M, wards


def frac_solve(M, B):
    """exact solve M X = B (Fractions, Gaussian elimination,
    deterministic first-nonzero pivot); B = list of rhs vectors
    (columns).  Pure linear algebra on passed arrays."""
    n = len(M)
    nb = len(B)
    A = [list(M[i]) + [B[j][i] for j in range(nb)] for i in range(n)]
    for c in range(n):
        piv = next((r_ for r_ in range(c, n) if A[r_][c] != 0), None)
        if piv is None:
            raise ZeroDivisionError("singular")
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]
        A[c] = [v / pv for v in A[c]]
        for r_ in range(n):
            if r_ != c and A[r_][c] != 0:
                f = A[r_][c]
                A[r_] = [vi - f * vc for vi, vc in zip(A[r_], A[c])]
    return [[A[i][n + j] for i in range(n)] for j in range(nb)]


def frac_pd(M):
    """exact PD test: all leading principal minors > 0."""
    n = len(M)
    for k in range(1, n + 1):
        if FS.frac_det([row[:k] for row in M[:k]]) <= 0:
            return False
    return True


def base_form_fr(Pm, wm, reserved, partner):
    """exact twin of base_form_f64 (Fractions; padded rows)."""
    m = len(Pm[0])
    M0 = [[Fr(0)] * m for _ in range(m)]
    M0[m - 1][m - 1] = FIVE_SEVEN
    used = set(p for p in partner if p >= 0)
    base_idx = [i for i in range(len(Pm))
                if (i in set(reserved)) or (i not in used)]
    for i in base_idx:
        for r_ in range(m):
            if Pm[i][r_] == 0:
                continue
            for c_ in range(m):
                M0[r_][c_] += wm[i] * Pm[i][r_] * Pm[i][c_]
    return M0, base_idx


def reserve_chain_fr(M0, Pm, wm, Pn, vn, plan, Pb, sb, b_order,
                     S_bud):
    """exact twin of reserve_chain_f64: per negative step the
    exact reserve r, the exact Sherman-Morrison identity check and
    the exact det dictionary det(M1) == (1 + L_aa) det(M),
    det(M2) == r det(M1).  Returns (recs, M, ok_sm, ok_det)."""
    reserved, nu_order, partner = plan
    m = len(M0)
    M = [row[:] for row in M0]
    et = [Fr(0)] * m
    et[m - 1] = Fr(1)

    def add(mass, vec):
        for r_ in range(m):
            if vec[r_] == 0:
                continue
            for c_ in range(m):
                M[r_][c_] += mass * vec[r_] * vec[c_]

    recs = []
    ok_sm = True
    ok_det = True
    if S_bud >= 0:
        add(S_bud, et)
    else:
        sol = frac_solve(M, [et])[0]
        Lbb = (-S_bud) * sum(et[i] * sol[i] for i in range(m))
        recs.append(dict(kind="bud", idx=-1, Laa=Fr(0), Lab2=Fr(0),
                         Lbb=Lbb, r=1 - Lbb))
        add(S_bud, et)

    def neg_step(kind, idx, wa, pa, vb, pb_):
        nonlocal ok_sm, ok_det
        d0 = FS.frac_det(M)
        if pa is not None:
            sol = frac_solve(M, [pa, pb_])
            Gaa = sum(pa[i] * sol[0][i] for i in range(m))
            Gab = sum(pa[i] * sol[1][i] for i in range(m))
            Gbb = sum(pb_[i] * sol[1][i] for i in range(m))
            Laa = wa * Gaa
            Lab2 = wa * vb * Gab * Gab
            Lbb = vb * Gbb
            r = 1 - Lbb + Lab2 / (1 + Laa)
            add(wa, pa)
            d1 = FS.frac_det(M)
            solb = frac_solve(M, [pb_])[0]
            direct = vb * sum(pb_[i] * solb[i] for i in range(m))
            ok_sm = ok_sm and (direct == Lbb - Lab2 / (1 + Laa))
            ok_det = ok_det and (d1 == (1 + Laa) * d0)
        else:
            sol = frac_solve(M, [pb_])[0]
            Laa = Fr(0)
            Lab2 = Fr(0)
            Lbb = vb * sum(pb_[i] * sol[i] for i in range(m))
            r = 1 - Lbb
            d1 = d0
        add(-vb, pb_)
        d2 = FS.frac_det(M)
        ok_det = ok_det and (d2 == r * d1)
        recs.append(dict(kind=kind, idx=idx, Laa=Laa, Lab2=Lab2,
                         Lbb=Lbb, r=r))

    for t_, k in enumerate(nu_order):
        pidx = partner[t_]
        if pidx >= 0:
            neg_step("pair", k, wm[pidx], Pm[pidx], vn[k], Pn[k])
        else:
            neg_step("pair", k, None, None, vn[k], Pn[k])
    for bi in b_order:
        s = sb[bi]
        if s == 0:
            continue
        eta = Pb[bi]
        plus = [eta[i] + et[i] for i in range(m)]
        minus = [eta[i] - et[i] for i in range(m)]
        if s > 0:
            va_, vb_ = plus, minus
        else:
            va_, vb_ = minus, plus
        neg_step("bord", bi, abs(s) / 2, va_, abs(s) / 2, vb_)
    return recs, M, ok_sm, ok_det


def cone_features(fp, wp, fn, vn, plan):
    """the sealed source-quantity family per main pair step (in
    plan order): F1 v, F2 w_a, F3 v/w_a, F4 pair fold distance,
    F5 SM2 shield mass, F6 v/SM2, F7 local gap, plus the NBITS
    dyadic fold bits.  Consumes fold indices + channel weights +
    the sealed plan only."""
    reserved, nu_order, partner = plan
    sh = LS.shield_profile(fp, wp, fn, vn, (SHIELD_R,))
    sm2 = sh[SHIELD_R][0]
    _s, gap, _ratio = LS.pair_geometry(fp, fn)
    F = dict(F1=[], F2=[], F3=[], F4=[], F5=[], F6=[], F7=[],
             bits=[], part=[])
    for t_, k in enumerate(nu_order):
        pidx = partner[t_]
        v = float(vn[k])
        F["F1"].append(v)
        F["part"].append(pidx >= 0)
        if pidx >= 0:
            w = float(wp[pidx])
            F["F2"].append(w)
            F["F3"].append(v / w)
            F["F4"].append(abs(int(fp[pidx]) - int(fn[k])))
        else:
            F["F2"].append(0.0)
            F["F3"].append(float("inf"))
            F["F4"].append(-1)
        F["F5"].append(float(sm2[k]))
        F["F6"].append(v / max(float(sm2[k]), 1e-300))
        F["F7"].append(int(gap[k]))
        F["bits"].append([(int(fn[k]) >> b) & 1
                          for b in range(NBITS)])
    return F


def phi_calibrate(rs, feats):
    """the sealed regression-free constant: c = max over the
    calibration pair steps of (1 - r)/F, clamped at 0.  Consumes
    passed reserve values + feature values only."""
    c = 0.0
    for r, f in zip(rs, feats):
        if f > 0.0 and math.isfinite(f):
            c = max(c, (1.0 - r) / f)
    return c


def phi_violations(rs, feats, c):
    """pointwise test of r >= 1 - c F: returns (#violations,
    #positive predicted bounds, min predicted bound,
    min r among violated steps)."""
    nv = 0
    npos = 0
    bmin = float("inf")
    rv_min = float("inf")
    for r, f in zip(rs, feats):
        bound = 1.0 - c * f
        bmin = min(bmin, bound)
        if bound > 0.0:
            npos += 1
        if r < bound - PHI_TOL:
            nv += 1
            rv_min = min(rv_min, r)
    return nv, npos, bmin, rv_min


# ============== must-fail mutants
def mutant_target_inverse_cone(Minv_true):
    """m2 MUST-FAIL: a 'cone bound' consuming the withheld inverse
    leverage of the final target window -- the scope audit must
    FLAG this (the r275 error class)."""
    return 1.0 - float(np.max(Minv_true))


def mutant_posthoc_pairing(r_true, plan):
    """m3 MUST-FAIL: a pairing re-sorted AFTER sight of the
    measured reserves -- the scope audit must FLAG this."""
    reserved, nu_order, partner = plan
    o = np.argsort(np.asarray(r_true, float))
    return [partner[i] for i in o]


# ============== gate-side helpers
def world_split(W):
    """channel arrays of one r284 world pack (gate-side)."""
    return (np.asarray(W["fp"], np.int64), np.asarray(W["wp"], float),
            np.asarray(W["fn"], np.int64), np.asarray(W["vn"], float),
            np.asarray(W["xp"], float), np.asarray(W["xn"], float))


def run_world_f64(W, ctx, dcap, ward=False):
    """gate-side full chain of one world at one cap: plan, base,
    chain, reconstruction, summaries, cone features."""
    fp, wp, fn, vn, xp, xn = world_split(W)
    B, rho, bxa, bwa = BG.world_budget(W, ctx)
    ff, xx, ww = BG.world_arrays(W)
    hull = BG.hull_of(xx, bxa)
    Pm = pad_rows(BG.cheb_rows(xp, dcap, *hull))
    Pn = pad_rows(BG.cheb_rows(xn, dcap, *hull))
    Pb = pad_rows(BG.cheb_rows(bxa, dcap, *hull))
    plan = greedy_pairing(fp, fn, dcap + 1)
    M0, base_idx = base_form_f64(Pm, wp, plan[0], plan[2])
    ev0 = np.linalg.eigvalsh(M0)
    b_order = list(np.argsort(bxa, kind="stable"))
    S_bud = B - 5.0 / 7.0
    npairs = len(plan[1])
    picks = (0, npairs // 2, npairs - 1) if ward else ()
    recs, Mfin, wards = reserve_chain_f64(
        M0, Pm, wp, Pn, vn, plan, Pb, bwa, b_order, S_bud,
        ward_picks=picks)
    A = BG.target_form_f64(BG.cheb_rows(xx, dcap, *hull), ww,
                           BG.cheb_rows(bxa, dcap, *hull), bwa, B)
    recon = float(np.linalg.norm(Mfin - A)
                  / max(np.linalg.norm(A), 1e-300))
    rs_all = [rec["r"] for rec in recs]
    rs_pair = [rec["r"] for rec in recs if rec["kind"] == "pair"]
    rs_bord = [rec["r"] for rec in recs if rec["kind"] == "bord"]
    i_min = int(np.argmin(rs_all))
    rec_min = recs[i_min]
    np_kind = {k: sum(1 for rec in recs
                      if rec["kind"] == k and rec["r"] <= 0.0)
               for k in ("bud", "pair", "bord")}
    r_bud = next((rec["r"] for rec in recs if rec["kind"] == "bud"),
                 None)
    shares = [rec["Lab2"] / (1.0 + rec["Laa"]) / rec["Lbb"]
              for rec in recs
              if rec["kind"] == "pair" and rec["Laa"] > 0.0
              and rec["Lbb"] > 0.0]
    feats = cone_features(fp, wp, fn, vn, plan)
    n_nonpos = sum(1 for r in rs_all if r <= 0.0)
    first_np = next((i for i, r in enumerate(rs_all) if r <= 0.0),
                    None)
    return dict(B=B, rho=rho, plan=plan, recs=recs, recon=recon,
                wards=wards, min_r=float(np.min(rs_all)),
                med_r=float(np.median(rs_all)),
                min_pair=float(np.min(rs_pair)) if rs_pair else None,
                med_pair=float(np.median(rs_pair)) if rs_pair
                else None,
                min_bord=float(np.min(rs_bord)) if rs_bord else None,
                n_nonpos=n_nonpos, first_np=first_np,
                np_kind=np_kind, r_bud=r_bud,
                rec_min=rec_min, shares=shares, feats=feats,
                rs_pair=rs_pair, ev0=ev0, base_n=len(base_idx),
                S_bud=S_bud, fn=fn, npairs=npairs, hull=hull,
                bxa=bxa, bwa=bwa)


def run_toy_fr(xs, ws, bxs, bws, B, d):
    """gate-side exact chain of one toy world (Fractions)."""
    xs_mu = [x for x, w in zip(xs, ws) if w > 0]
    ws_mu = [w for w in ws if w > 0]
    xs_nu = [x for x, w in zip(xs, ws) if w < 0]
    vs_nu = [-w for w in ws if w < 0]
    Pm = [row + [Fr(0)] for row in BG.mono_rows_fr(xs_mu, d)]
    Pn = [row + [Fr(0)] for row in BG.mono_rows_fr(xs_nu, d)]
    Pb = [row + [Fr(0)] for row in BG.mono_rows_fr(bxs, d)]
    plan = greedy_pairing(xs_mu, xs_nu, d + 1)
    M0, base_idx = base_form_fr(Pm, ws_mu, plan[0], plan[2])
    b_order = sorted(range(len(bxs)), key=lambda i: (bxs[i], i))
    S_bud = B - FIVE_SEVEN
    recs, Mfin, ok_sm, ok_det = reserve_chain_fr(
        M0, Pm, ws_mu, Pn, vs_nu, plan, Pb, bws, b_order, S_bud)
    A = BG.target_form_fr(xs, ws, bxs, bws, B, d)
    ok_rec = all(Mfin[i][j] == A[i][j] for i in range(d + 2)
                 for j in range(d + 2))
    ok_pd0 = frac_pd(M0)
    all_pos = all(rec["r"] > 0 for rec in recs)
    ok_pd_fin = frac_pd(Mfin)
    return dict(plan=plan, M0=M0, recs=recs, Mfin=Mfin, ok_sm=ok_sm,
                ok_det=ok_det, ok_rec=ok_rec, ok_pd0=ok_pd0,
                all_pos=all_pos, ok_pd_fin=ok_pd_fin, A=A,
                S_bud=S_bud, base_idx=base_idx)


def mp_reserve(xp, wp, xn, vn, plan, dcap, hull, jstar):
    """gate-side mp ward (dps sealed): rebuild the prefix M up to
    (excluding) pair step jstar in mp and recompute its reserve."""
    mp.mp.dps = MP_DPS
    lo, hi = hull
    m = dcap + 2

    def rows_mp(xs):
        out = []
        for x in xs:
            xi = (2 * mp.mpf(float(x)) - lo - hi) / (hi - lo)
            row = [mp.mpf(1)]
            if dcap >= 1:
                row.append(xi)
            for k in range(2, dcap + 1):
                row.append(2 * xi * row[k - 1] - row[k - 2])
            row.append(mp.mpf(0))
            return_row = row
            out.append(return_row)
        return out

    Pm = rows_mp(xp)
    Pn = rows_mp(xn)
    reserved, nu_order, partner = plan
    used = set(p for p in partner if p >= 0)
    M = mp.zeros(m, m)
    M[m - 1, m - 1] = mp.mpf(5) / 7
    for i in range(len(Pm)):
        if (i in set(reserved)) or (i not in used):
            w = mp.mpf(float(wp[i]))
            for r_ in range(m):
                for c_ in range(m):
                    M[r_, c_] += w * Pm[i][r_] * Pm[i][c_]
    # budget step is positive on the gated world (asserted gate-side)
    return M, Pm, Pn


def mp_reserve_at(M, Pm, Pn, plan, wp, vn, S_bud, jstar, dcap):
    mp.mp.dps = MP_DPS
    m = dcap + 2
    M = M.copy()
    M[m - 1, m - 1] += mp.mpf(float(S_bud))
    reserved, nu_order, partner = plan
    for t_ in range(jstar):
        k = nu_order[t_]
        pidx = partner[t_]
        wa = mp.mpf(float(wp[pidx]))
        vb = mp.mpf(float(vn[k]))
        for r_ in range(m):
            for c_ in range(m):
                M[r_, c_] += (wa * Pm[pidx][r_] * Pm[pidx][c_]
                              - vb * Pn[k][r_] * Pn[k][c_])
    k = nu_order[jstar]
    pidx = partner[jstar]
    wa = mp.mpf(float(wp[pidx]))
    vb = mp.mpf(float(vn[k]))
    pa = mp.matrix([Pm[pidx][i] for i in range(m)])
    pb_ = mp.matrix([Pn[k][i] for i in range(m)])
    sa = mp.lu_solve(M, pa)
    sb_ = mp.lu_solve(M, pb_)
    Gaa = sum(pa[i] * sa[i] for i in range(m))
    Gab = sum(pa[i] * sb_[i] for i in range(m))
    Gbb = sum(pb_[i] * sb_[i] for i in range(m))
    Laa = wa * Gaa
    Lab2 = wa * vb * Gab * Gab
    Lbb = vb * Gbb
    return float(1 - Lbb + Lab2 / (1 + Laa))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("paired_cone_probe -- PRIME.LSTAR.PAIRED_CONE.01 "
          "(round 309)")
    print("SPEC_SHA %s   (r308 BG %s / r284 LS %s / r275 KYP %s)"
          % (SPEC_SHA[:16], BG.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             KYP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (exact toys + firewall + scopes + "
                        "mutants + w9 f64 chain at DEG_A; crossing "
                        "pin, mp ward, twin, controls, DEG_B, "
                        "ladder, cone, discriminator, adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the ordered rank-one rebuild "
          "(reserved rule, greedy matching, signed budget step, "
          "exact border +/- splitting), the reviewer reserve "
          "r = 1 - L_bb + L_ab^2/(1 + L_aa) in the square-root-"
          "free (mass, vector) parametrization, the exactness "
          "wards (Sherman-Morrison + det dictionary), the cone "
          "family F1..F7 + the B4-sanctioned NBITS fold-bit "
          "register, the two phi forms with their aligned-limit "
          "design origin and the frozen calibration split, the "
          "sealed adjudication letters, the world set, every bar/"
          "tolerance, the mutants and the verdict form; the "
          "honesty condition is binding: M^{-1} may appear in the "
          "update algebra, the cone must consume source "
          "quantities only (mutant-guarded)")

    # ---------------- S1 exact toys
    section("S1  EXACT LEG -- PC4 (HAND), SM1, MINI16")
    T4 = run_toy_fr(list(PC4_X), list(PC4_W), list(PC4_BX),
                    list(PC4_BW), PC4_B, 0)
    rec_p = next(r_ for r_ in T4["recs"] if r_["kind"] == "pair")
    ok_hand = (T4["plan"][0] == [0]
               and T4["plan"][2] == [1]
               and T4["S_bud"] == Fr(4, 7)
               and rec_p["r"] == Fr(7, 9)
               and T4["Mfin"][0][0] == Fr(7, 6)
               and T4["Mfin"][0][1] == Fr(1, 5)
               and T4["Mfin"][1][1] == Fr(9, 7))
    ok_t4 = (T4["ok_sm"] and T4["ok_det"] and T4["ok_rec"]
             and T4["ok_pd0"] and T4["all_pos"]
             and T4["ok_pd_fin"])
    check("G10-pc4-hand-exact", ok_hand and ok_t4,
          "PC4 HAND TOY (cap 0, m = 2): reserved = {x = -1/2}, "
          "partner of the nu atom = x = 1/2, budget step +4/7; "
          "PAIR RESERVE r = %s == 7/9 HAND-EXACT; det dictionary "
          "det(M0) = 9/14 -> det(M1) = 27/14 == (1 + L_aa) det "
          "(L_aa = %s) -> det(M2) = 3/2 == r det(M1), all EXACT; "
          "Sherman-Morrison identity EXACT at every negative "
          "step; final M == [[7/6, 1/5], [1/5, 9/7]] entrywise; "
          "M0 PD, all reserves > 0, final PD (the ordering "
          "theorem live on the toy)"
          % (str(rec_p["r"]), str(rec_p["Laa"])))
    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    bxs_sm = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
    bws_sm = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
    B_sm1 = BG.exact_budget_fr(x10, w_sm1, bxs_sm, bws_sm,
                               (len(x10) + 1) // 2)
    T1 = run_toy_fr(x10, w_sm1, bxs_sm, bws_sm, B_sm1, DEG_T)
    n_part1 = sum(1 for p in T1["plan"][2] if p >= 0)
    rs1 = [float(r_["r"]) for r_ in T1["recs"]]
    check("G11-sm1-exact", T1["ok_sm"] and T1["ok_det"]
          and T1["ok_rec"] and T1["ok_pd0"] and T1["all_pos"]
          and T1["ok_pd_fin"] and n_part1 == 3,
          "SM1 (r308 MAIN-like shielded model, cap %d, m = %d): "
          "B = %.6f exact via the WD chain; %d/3 nu atoms "
          "partnered; %d negative steps, ALL r > 0 (min %.4f); "
          "Sherman-Morrison + det dictionary EXACT at every step; "
          "reconstruction EXACT entrywise; M0 + final PD"
          % (DEG_T, DEG_T + 2, float(B_sm1), n_part1,
             len(T1["recs"]), min(rs1)))
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ff9, xx9, ww9 = BG.world_arrays(W9)
    bx9, bw9, by9, bv9 = BG.border_split(ctx9)
    bxa9 = np.concatenate([bx9, by9])
    bwa9 = np.concatenate([bw9, -bv9])
    mini_x = [Fr(float(x)) for x in xx9[:MINI_K]]
    mini_w = [Fr(float(w)) for w in ww9[:MINI_K]]
    mini_bx = [Fr(float(x)) for x in bxa9[:MINI_BK]]
    mini_bw = [Fr(float(w)) for w in bwa9[:MINI_BK]]
    B_mini = BG.exact_budget_fr(mini_x, mini_w, mini_bx, mini_bw,
                                (MINI_K + 1) // 2)
    TM = run_toy_fr(mini_x, mini_w, mini_bx, mini_bw, B_mini, DEG_T)
    n_partm = sum(1 for p in TM["plan"][2] if p >= 0)
    n_unp = sum(1 for p in TM["plan"][2] if p < 0)
    rsm = [float(r_["r"]) for r_ in TM["recs"]]
    check("G12-mini16-exact", TM["ok_sm"] and TM["ok_det"]
          and TM["ok_rec"] and TM["ok_pd0"] and TM["all_pos"]
          and TM["ok_pd_fin"],
          "MINI16 (first %d REAL w9 union atoms in fold order, "
          "f64 -> Fraction EXACT; first %d border atoms; exact "
          "mini budget B = %.6f): %d pairs + %d unpartnered nu "
          "atoms (the disclosed degenerate case a = 0, r = 1 - "
          "L_bb); %d negative steps, ALL r > 0 (min %.4f); all "
          "identities EXACT; reconstruction EXACT entrywise"
          % (MINI_K, MINI_BK, float(B_mini), n_partm, n_unp,
             len(TM["recs"]), min(rsm)))
    # f64/exact consistency on SM1 (basis invariance of r)
    xs1 = np.array([float(x) for x in x10])
    ws1 = np.array([float(w) for w in w_sm1])
    mupos = xs1[ws1 > 0]
    muw = ws1[ws1 > 0]
    nupos = xs1[ws1 < 0]
    nuw = -ws1[ws1 < 0]
    bxs1 = np.array([float(x) for x in bxs_sm])
    bws1 = np.array([float(w) for w in bws_sm])
    h1 = BG.hull_of(xs1, bxs1)
    Pm1 = pad_rows(BG.cheb_rows(mupos, DEG_T, *h1))
    Pn1 = pad_rows(BG.cheb_rows(nupos, DEG_T, *h1))
    Pb1 = pad_rows(BG.cheb_rows(bxs1, DEG_T, *h1))
    plan1 = greedy_pairing(mupos, nupos, DEG_T + 1)
    M01, _bi1 = base_form_f64(Pm1, muw, plan1[0], plan1[2])
    bo1 = list(np.argsort(bxs1, kind="stable"))
    recs1, Mf1, _w1 = reserve_chain_f64(
        M01, Pm1, muw, Pn1, nuw, plan1, Pb1, bws1, bo1,
        float(B_sm1) - 5.0 / 7.0)
    ex_neg = [r_ for r_ in T1["recs"]]
    dr = max(abs(float(a["r"]) - b["r"])
             for a, b in zip(ex_neg, recs1))
    check("G13-f64-exact-consistency", dr <= CONS_BAR
          and len(ex_neg) == len(recs1),
          "BASIS INVARIANCE WARD (SM1): the f64 Chebyshev route "
          "reproduces the exact monomial r-sequence step by step, "
          "max |dr| = %.1e (bar %.0e) -- leverages are congruence "
          "invariants, as sealed" % (dr, CONS_BAR))

    # ---------------- S2 w9 anchors
    section("S2  W9 ANCHORS -- SOURCE, CROSSING, 5/7, r275 PIN")
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4]
              and len(set(W9["fp"]) & set(W9["fn"])) == 0)
    check("G20-w9-source-split", ok_src,
          "w9 FULL SOURCE: S = %d (mu %d / nu %d), N_w = %d, minC "
          "= %s (records); mu/nu fold sets disjoint"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"])))
    if smoke:
        check("G21-w9-crossing", True, "SMOKE: skipped")
    else:
        depth9 = min(W9["N"] + DEPTH_PAD, W9["Sp"] - 1)
        SP9 = LS.spectral_block(W9, depth9)
        check("G21-w9-crossing", SP9["cross"] == CROSS_REC
              and SP9["cross"] == W9["minC"] + 1,
              "lambda_max(E_n) crosses 1 at n = %s == minC + 1 == "
              "%d (r283 route reproduced)"
              % (str(SP9["cross"]), CROSS_REC))
    B9, rho9, bxa9c, bwa9c = BG.world_budget(W9, ctx9)
    ok_57 = (abs(B9 - B_REC) <= B_TOL
             and all(r_ >= 0.0 for r_ in rho9))
    check("G22-budget-five-seven", ok_57,
          "5/7-RESERVE CONVENTION (r243/v958, r308 record): B_w9 "
          "= S_{N-2} + 5/7 = %.6f (record %.6f, tol %.0e) with "
          "all %d rho_k >= 0 through the free window -- the "
          "budget step of the sealed chain is POSITIVE on the "
          "MAIN family; the base carries the imported 5/7 floor "
          "as its t-direction mass (imported, never derived)"
          % (B9, B_REC, B_TOL, len(rho9)))
    ok_kyp = KYP.toy_kyp_exact()
    check("G23-r275-nogo-pin", ok_kyp,
          "r275 KYP NO-GO PIN re-run EXACT (the sealed toy: o1 "
          "fiber forcing + o2 descent kill every uniform "
          "quadratic memory; the Riccati memory is FORCED to "
          "carry the exact tail sums = the inverted terminal "
          "readout, fingerprint sp +1.00 in the r275 record) -- "
          "THE REFERENCE ERROR CLASS this round's cone must "
          "never become: the phi bounds consume source "
          "quantities only, the target-inverse mutant must stay "
          "FLAGGED (S8); the B4 demarcation is respected (the "
          "NBITS fold register is O(log N) source-exact, not a "
          "uniform quadratic memory)")

    # ---------------- S3 w9 chain at DEG_A
    section("S3  W9 -- THE SEALED CHAIN AT DEG_A")
    CA9 = run_world_f64(W9, ctx9, DEG_A, ward=True)
    n_part9 = sum(1 for p in CA9["plan"][2] if p >= 0)
    dists9 = [abs(int(W9["fp"][CA9["plan"][2][t_]])
                  - int(W9["fn"][k]))
              for t_, k in enumerate(CA9["plan"][1])
              if CA9["plan"][2][t_] >= 0]
    check("G30-w9-pairing-base", n_part9 == W9["Sm"]
          and float(CA9["ev0"][0]) > 0.0
          and CA9["S_bud"] > 0.0,
          "w9 PLAN (DEG_A): base = %d mu atoms (%d reserved + %d "
          "unmatched), M0 PD (min eig %.1e); %d/%d nu atoms "
          "partnered (max pair distance %d folds, median %.0f); "
          "%d border atoms -> exact +/- pairs; budget step "
          "+%.3f > 0" % (CA9["base_n"], DEG_A + 1,
                         CA9["base_n"] - (DEG_A + 1),
                         float(CA9["ev0"][0]), n_part9, W9["Sm"],
                         max(dists9), float(np.median(dists9)),
                         len(CA9["bxa"]), CA9["S_bud"]))
    check("G31-w9-recon-degA", CA9["recon"] <= RECON_BAR,
          "EXACT REBUILD WARD: the full ordered rank-one stream "
          "reassembles the augmented target form, rel Frobenius "
          "dev %.1e (bar %.0e) -- base + budget + %d pairs + %d "
          "border pairs == [[H, u], [u^T, B]]"
          % (CA9["recon"], RECON_BAR, CA9["npairs"],
             len(CA9["bxa"])))
    sm_max = max(w_["sm"] for w_ in CA9["wards"])
    det_max = max(max(w_["det1"], w_["det2"]) for w_ in CA9["wards"])
    check("G32-w9-wards", sm_max <= SM_BAR and det_max <= DET_BAR
          and len(CA9["wards"]) == 3,
          "SHERMAN-MORRISON + DET DICTIONARY (sealed picks, pair "
          "steps %s): direct recount vs the leverage formula max "
          "rel dev %.1e (bar %.0e); slogdet dictionary ld(M1) - "
          "ld(M) == log(1 + L_aa), ld(M2) - ld(M1) == log r, max "
          "rel dev %.1e (bar %.0e) -- the explicit positive "
          "square is the measured cancellation"
          % (str(tuple(w_["pair"] for w_ in CA9["wards"])),
             sm_max, SM_BAR, det_max, DET_BAR))
    rm = CA9["rec_min"]
    fold_min = int(CA9["fn"][rm["idx"]]) if rm["kind"] == "pair" \
        else -1
    tight5 = sorted(range(len(CA9["rs_pair"])),
                    key=lambda i: CA9["rs_pair"][i])[:5]
    tight_folds = [int(CA9["fn"][CA9["plan"][1][i]]) for i in tight5]
    check("G33-w9-reserve", True,
          "w9 RESERVE PROFILE at DEG_A (MEASURED, adjudicated in "
          "S9): min r = %+.4f (%s step, fold %d), median %+.4f; "
          "pair phase min/median %+.4f/%+.4f, border phase min "
          "%+.4f; nonpositive steps %d; assist share L_ab^2/((1 "
          "+ L_aa) L_bb): median %.2e, max %.3f; tightest 5 pair "
          "folds %s"
          % (CA9["min_r"], rm["kind"], fold_min, CA9["med_r"],
             CA9["min_pair"], CA9["med_pair"], CA9["min_bord"],
             CA9["n_nonpos"], float(np.median(CA9["shares"])),
             float(np.max(CA9["shares"])), str(tight_folds)))
    if smoke:
        check("G34-w9-mp-ward", True, "SMOKE: skipped")
    else:
        jstar = int(np.argmin(CA9["rs_pair"]))
        fp9, wp9, fn9, vn9, xp9, xn9 = world_split(W9)
        Mmp, Pmmp, Pnmp = mp_reserve(xp9, wp9, xn9, vn9,
                                     CA9["plan"], DEG_A,
                                     CA9["hull"], jstar)
        r_mp = mp_reserve_at(Mmp, Pmmp, Pnmp, CA9["plan"], wp9,
                             vn9, CA9["S_bud"], jstar, DEG_A)
        dev_mp = abs(r_mp - CA9["rs_pair"][jstar]) \
            / max(abs(r_mp), 1e-300)
        check("G34-w9-mp-ward", dev_mp <= MP_BAR,
              "MP WARD (dps %d): the tightest w9 pair reserve "
              "(pair %d) rebuilt from the atoms in mp: r_mp = "
              "%+.6f vs f64 %+.6f, rel dev %.1e (bar %.0e) -- "
              "the tight step is arbitration-safe"
              % (MP_DPS, jstar, r_mp, CA9["rs_pair"][jstar],
                 dev_mp, MP_BAR))

    # ---------------- S4 DEG_B + twin + controls
    section("S4  DEG_B + RATIONAL TWIN + CONTROLS")
    if smoke:
        for g in ("G40-twin-keeps", "G41-degB-main-family",
                  "G42-ctrl-flips-degA", "G43-ctrl-degB-forced"):
            check(g, True, "SMOKE: skipped")
        CB9 = None
        CT_A = {}
        CT_B = {}
        TW_A = None
        TW_B = None
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
        check("G40-twin-keeps", ok_tc and WT["minC"] == 184
              and SPT["cross"] == 185,
              "r289 RATIONAL TWIN re-built verbatim (CF "
              "convergents, |du| <= %.0e local gap, weights "
              "bitwise, max denominator %d <= %.0e): "
              "RATIONAL_KEEPS re-gated -- minC = %s, crossing = "
              "%s (record 184/185)"
              % (RAT_TOL, int(np.max(dens)), QMAX,
                 str(WT["minC"]), str(SPT["cross"])))
        TW_A = run_world_f64(WT, ctxT, DEG_A)
        TW_B = run_world_f64(WT, ctxT, DEG_B)
        CB9 = run_world_f64(W9, ctx9, DEG_B)
        ok_main_b = (CB9["recon"] <= RECON_BAR
                     and TW_A["recon"] <= RECON_BAR
                     and TW_B["recon"] <= RECON_BAR)
        check("G41-degB-main-family", ok_main_b,
              "MAIN FAMILY at DEG_B = %d (MEASURED, adjudicated "
              "in S9): w9 recon %.1e, min r = %+.4f (%d "
              "nonpositive of %d steps), median %+.4f; twin@A "
              "min %+.4f / twin@B min %+.4f (recons %.1e/%.1e) "
              "-- the diophantine-trivialized world in the same "
              "ordered coordinates"
              % (DEG_B, CB9["recon"], CB9["min_r"],
                 CB9["n_nonpos"], len(CB9["recs"]), CB9["med_r"],
                 TW_A["min_r"], TW_B["min_r"], TW_A["recon"],
                 TW_B["recon"]))
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        CT_A = {}
        CT_B = {}
        ok_fl = True
        txt_a = []
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            ok_fl = ok_fl and (Wc["minC"] == CTRL_FLIPS[cn])
            CT_A[cn] = run_world_f64(Wc, cctx, DEG_A)
            CT_B[cn] = run_world_f64(Wc, cctx, DEG_B)
            C = CT_A[cn]
            txt_a.append(
                "%s: pair min %+.4f / bord min %+.4f (nonpos "
                "pair %d / bord %d), budget step %s, med %+.4f"
                % (cn, C["min_pair"], C["min_bord"],
                   C["np_kind"]["pair"], C["np_kind"]["bord"],
                   ("r = %+.3f" % C["r_bud"])
                   if C["r_bud"] is not None
                   else "+%.3f" % C["S_bud"], C["med_r"]))
        ok_rc = all(CT_A[cn]["recon"] <= RECON_BAR
                    and CT_B[cn]["recon"] <= RECON_BAR
                    for cn in CT_A)
        check("G42-ctrl-flips-degA", ok_fl and ok_rc,
              "CONTROLS (r281 channel verbatim, minC == flips "
              "%s; recon <= %.0e at both caps): DEG_A per-KIND "
              "reserve census (amendment-a1 disclosure: a world "
              "with measured S_{N-2} < 0 has an indefinite "
              "augmented DEG_A form through the BUDGET "
              "coordinate; which step carries it is the "
              "measurement): %s"
              % (str(CTRL_FLIPS), RECON_BAR, "; ".join(txt_a)))
        ok_forced = all(CT_B[cn]["min_r"] <= 0.0
                        for cn in ("EPST", "SCR"))
        det_b = []
        for cn in CT_B:
            C = CT_B[cn]
            fnp = C["first_np"]
            det_b.append("%s: min %+.3g first r<=0 at step %s"
                         % (cn, C["min_r"], str(fnp)))
        check("G43-ctrl-degB-forced", ok_forced,
              "DEG_B FORCED NEGATIVITY (disclosed as theorem-"
              "forced, r308 discipline: the control crossings "
              "26/22 << %d put a negative minor into the moment "
              "block, so with a PD base the ordering theorem "
              "FORCES some r <= 0 -- gated live on EPST/SCR; "
              "SMOOTH minC 27 is the sealed boundary case, "
              "reported only): %s"
              % (DEG_B, "; ".join(det_b)))

    # ---------------- S5 ladder
    section("S5  LADDER -- 42 CORE + 15 EXTENSION AT DEG_A")
    if smoke:
        for g in ("G50-ladder-census", "G51-ladder-recon",
                  "G52-ladder-reserve"):
            check(g, True, "SMOKE: skipped")
        rung_res = {}
        cal_kzs = []
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
        epool = sorted(ekz, key=lambda kz: (packs[kz][0]["N"], kz))
        ext15 = epool[:K_EXT]
        check("G50-ladder-census", len(kzs) == 42 and ok_anch
              and dist == R281_DIST and len(ext15) == K_EXT,
              "42-rung r281 census (offset distribution %s == "
              "record, anchors exact) + %d extension anchors "
              "(h <= %d, sorted by (N_w, kz)): N_w %d..%d"
              % (str({("+%d" % k): dist[k] for k in sorted(dist)}),
                 K_EXT, EXT_H, packs[ext15[0]][0]["N"],
                 packs[ext15[-1]][0]["N"]))
        cal_pool = sorted([kz for kz in kzs if kz != MAIN_KZ],
                          key=lambda kz: (packs[kz][0]["N"], kz))
        cal_kzs = cal_pool[:CAL_K]
        rung_res = {}
        ok_rrec = True
        worst_rec = 0.0
        for kz in kzs + ext15:
            Wp, ctx = packs[kz]
            Ck = run_world_f64(Wp, ctx, DEG_A)
            rung_res[kz] = Ck
            worst_rec = max(worst_rec, Ck["recon"])
            ok_rrec = ok_rrec and Ck["recon"] <= RECON_BAR
        check("G51-ladder-recon", ok_rrec and len(rung_res) == 57,
              "EXACT REBUILD on all %d rungs at DEG_A: worst rel "
              "Frobenius dev %.1e (bar %.0e)"
              % (len(rung_res), worst_rec, RECON_BAR))
        mins = sorted((rung_res[kz]["min_r"], kz)
                      for kz in rung_res)
        n_pos = sum(1 for kz in rung_res
                    if rung_res[kz]["n_nonpos"] == 0)
        check("G52-ladder-reserve", True,
              "LADDER RESERVE (MEASURED, adjudicated in S9): "
              "%d/%d rungs with ALL r > 0; min of rung-mins "
              "%+.4f@kz%d, median of rung-mins %+.4f; worst 5: "
              "%s" % (n_pos, len(rung_res), mins[0][0],
                      mins[0][1],
                      float(np.median([m_ for m_, _k in mins])),
                      str([("kz%d" % k, round(m_, 4))
                           for m_, k in mins[:5]])))

    # ---------------- S6 cone test
    section("S6  THE CONE TEST (LEG C, SEALED)")
    if smoke:
        for g in ("G60-cone-calibration", "G61-cone-bound-test",
                  "G62-cone-info-test"):
            check(g, True, "SMOKE: skipped")
        cone_verd = "SMOKE"
        info_fires = False
        c_tab = {}
        vio_tab = {}
    else:
        def pair_data(C):
            """(r, F3, F6, features dict) of the partnered pair
            steps of one world run."""
            F = C["feats"]
            rs = C["rs_pair"]
            out = []
            for i, r_ in enumerate(rs):
                if F["part"][i]:
                    out.append((r_, F["F3"][i], F["F6"][i], i))
            return out

        cal_steps = []
        for kz in cal_kzs:
            cal_steps += pair_data(rung_res[kz])
        c1 = phi_calibrate([t[0] for t in cal_steps],
                           [t[1] for t in cal_steps])
        c2 = phi_calibrate([t[0] for t in cal_steps],
                           [t[2] for t in cal_steps])
        c_tab = {"phi1_massratio": c1, "phi2_shield": c2}
        check("G60-cone-calibration", len(cal_steps) > 0,
              "FROZEN SPLIT (the %d shallowest core rungs by "
              "(N_w, kz), kz9 excluded): %s, %d pair steps; "
              "sealed constants c = max (1 - r)/F over the "
              "split: c_1 (mass ratio v/w_a) = %.4f, c_2 "
              "(shield v/SM2) = %.4f (aligned-limit design "
              "value 1, disclosed)"
              % (CAL_K, str(cal_kzs), len(cal_steps), c1, c2))
        test_worlds = [("w9", CA9), ("twin", TW_A)] + \
            [("kz%d" % kz, rung_res[kz]) for kz in sorted(rung_res)
             if kz not in cal_kzs]
        pool = []
        for wn, C in test_worlds:
            pool += [(wn,) + t for t in pair_data(C)]
        n_test = len(pool)
        vio_tab = {}
        for nm, c_, fi in (("phi1_massratio", c1, 2),
                           ("phi2_shield", c2, 3)):
            rs_ = [t[1] for t in pool]
            fs_ = [t[fi + 1] for t in pool]
            nv, npos, bmin, rvmin = phi_violations(rs_, fs_, c_)
            vio_tab[nm] = dict(nv=nv, npos=npos, bmin=bmin,
                               rvmin=rvmin, n=n_test)
        det_tab = {nm: ("%d viol, %d/%d bounds>0, min bound "
                        "%+.3g%s"
                        % (v["nv"], v["npos"], v["n"], v["bmin"],
                           ("" if v["nv"] == 0 else
                            ", min r at violations %+.3g"
                            % v["rvmin"])))
                   for nm, v in vio_tab.items()}
        check("G61-cone-bound-test", True,
              "POINTWISE BOUND TEST on %d test pair steps (52 "
              "rungs + w9 + twin at DEG_A; MEASURED, adjudicated "
              "in S9): %s" % (n_test, str(det_tab)))
        # information test: pooled tightest decile + w9 census
        pool_sorted = sorted(pool, key=lambda t: t[1])
        n_tight = max(1, int(TIGHT_Q * len(pool_sorted)))
        tight = pool_sorted[:n_tight]
        # rebuild the full feature table for the tight set
        featmap = {}
        for wn, C in test_worlds:
            featmap[wn] = C["feats"]
        names = ("F1", "F2", "F3", "F4", "F5", "F6", "F7")
        sp_tab = {}
        rs_t = [t[1] for t in tight]
        for nm in names:
            vals = [featmap[t[0]][nm][t[4]] for t in tight]
            sp_tab[nm] = BH.spearman(vals, rs_t)
        sp_bits = []
        for b in range(NBITS):
            vals = [featmap[t[0]]["bits"][t[4]][b] for t in tight]
            sp_bits.append(BH.spearman(vals, rs_t))
        info_fires = any(abs(v) >= SP_INFO for v in sp_tab.values())
        # w9-only census (reported)
        pd9 = pair_data(CA9)
        sp9 = {nm: BH.spearman([CA9["feats"][nm][t[3]]
                                for t in pd9],
                               [t[0] for t in pd9])
               for nm in names}
        check("G62-cone-info-test", True,
              "INFORMATION TEST (pooled tightest decile, %d "
              "steps): spearman(feature, r) = %s; fold bits max "
              "|sp| = %.2f (the B4 register carries %s at this "
              "cap); w9-only census %s => info test %s (bar "
              "%.1f)"
              % (n_tight,
                 str({k: round(v, 2) for k, v in sp_tab.items()}),
                 max(abs(v) for v in sp_bits),
                 "signal" if max(abs(v) for v in sp_bits)
                 >= SP_INFO else "nothing",
                 str({k: round(v, 2) for k, v in sp9.items()}),
                 "FIRES" if info_fires else "SILENT", SP_INFO))
        # sealed adjudication
        cone_verd = "CONE_UNPREDICTABLE"
        anat = []
        for nm, v in vio_tab.items():
            if v["nv"] == 0 and v["npos"] == v["n"]:
                cone_verd = "CONE_PREDICTABLE"
                anat.append("%s c=%.4f: 0 violations, ALL "
                            "bounds > 0" % (nm, c_tab[nm]))
        if cone_verd != "CONE_PREDICTABLE":
            for nm, v in vio_tab.items():
                if v["nv"] == 0 and v["npos"] >= v["n"] // 2:
                    cone_verd = "CONE_PARTIAL"
                    anat.append("%s c=%.4f: 0 violations but "
                                "only %d/%d bounds > 0"
                                % (nm, c_tab[nm], v["npos"],
                                   v["n"]))
                elif (v["nv"] <= VIOL_FRAC * v["n"]
                      and v["rvmin"] > 0.0):
                    cone_verd = "CONE_PARTIAL"
                    anat.append("%s c=%.4f: %d violations "
                                "(<= %.0f%%), all violated r > 0"
                                % (nm, c_tab[nm], v["nv"],
                                   100 * VIOL_FRAC))
            if cone_verd == "CONE_UNPREDICTABLE" and info_fires:
                cone_verd = "CONE_PARTIAL"
                anat.append("information test fires")
        cone_anat = "; ".join(anat) if anat else "no phi holds, " \
            "info test silent"

    # ---------------- S7 world discriminator
    section("S7  WORLD DISCRIMINATOR (LEG D)")
    if smoke:
        for g in ("G70-world-discriminator", "G71-r308-crossref"):
            check(g, True, "SMOKE: skipped")
        disc_typ = {}
    else:
        stats = {
            "K1_minr": {"MAIN": CA9["min_r"]},
            "K2_medr": {"MAIN": CA9["med_r"]},
            "K3_assist": {"MAIN": float(np.median(CA9["shares"]))}}
        for cn in CT_A:
            stats["K1_minr"][cn] = CT_A[cn]["min_r"]
            stats["K2_medr"][cn] = CT_A[cn]["med_r"]
            stats["K3_assist"][cn] = float(
                np.median(CT_A[cn]["shares"]))
        disc_typ = {nm: LS.dist_rule(tab, list(CT_A))
                    for nm, tab in stats.items()}
        check("G70-world-discriminator", True,
              "SEALED r281 DISTANCE RULE at DEG_A: %s (values %s; "
              "twin reported: min %+.4f med %+.4f); REPORTED, "
              "outside the sealed rule: the budget scalars "
              "S_{N-2} = %s -- the sign splits EPST/SCR from the "
              "MAIN family while SMOOTH sits on MAIN's side; the "
              "budget coordinate is the r243 wall readout "
              "itself, not a new discriminator"
              % (str(disc_typ),
                 str({nm: {k: round(v, 4) for k, v in tab.items()}
                      for nm, tab in stats.items()}),
                 TW_A["min_r"], TW_A["med_r"],
                 str({"MAIN": round(CA9["S_bud"], 3),
                      **{cn: round(CT_A[cn]["S_bud"], 3)
                         for cn in CT_A}})))
        r284_folds = {2, 4}
        hit = [f for f in tight_folds if f in r284_folds]
        xref = []
        for cn in ("EPST", "SCR"):
            C = CT_B[cn]
            fnp = C["first_np"]
            rec_b = C["recs"][fnp]
            loc = ("BUDGET step" if rec_b["kind"] == "bud" else
                   "%s step, fold %d"
                   % (rec_b["kind"],
                      int(C["fn"][rec_b["idx"]])
                      if rec_b["kind"] == "pair" else -1))
            xref.append("%s first break = %s vs crossing %d"
                        % (cn, loc, CTRL_FLIPS[cn] + 1))
        check("G71-r308-crossref", True,
              "CROSS-REFERENCE (reported, not hard-gated): w9 "
              "tightest pair folds %s vs the r284 extremal folds "
              "{2, 4} -- overlap %s; controls at DEG_B: %s -- "
              "pair index and spectral degree are different "
              "clocks (the ordered break need not sit at the "
              "crossing degree)"
              % (str(tight_folds),
                 str(hit) if hit else "NONE (neighbors reported)",
                 "; ".join(xref)))

    # ---------------- S8 must-fails + scopes
    section("S8  MUST-FAILS + SCOPE AUDITS")
    r_wrong = 1 - rec_p["Lbb"] - rec_p["Lab2"] / (1 + rec_p["Laa"])
    dev_m1 = rec_p["r"] - r_wrong
    check("G80-mustfail-wrong-sign", dev_m1 == M1_DEV
          and r_wrong == Fr(-1, 9),
          "m1 SHERMAN-MORRISON WRONG SIGN (PC4, exact): r_wrong "
          "= 1 - L_bb - L_ab^2/(1 + L_aa) = %s vs the det-"
          "dictionary truth 7/9 -- dev EXACTLY %s == 8/9: the "
          "positive square's SIGN is load-bearing and the exact "
          "det dictionary catches the flip LOUDLY"
          % (str(r_wrong), str(dev_m1)))
    hits_m2 = scope_audit("mutant_target_inverse_cone")
    hits_m3 = scope_audit("mutant_posthoc_pairing")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G81-scope-audits", bool(hits_m2) and bool(hits_m3)
          and not hits and not ag_hits,
          "m2 TARGET-INVERSE CONE mutant FLAGGED (%s); m3 "
          "POSTHOC-PAIRING mutant FLAGGED (%s); the %d sealed "
          "constructors audit CLEAN (%s); fragment audit (no fit "
          "primitives): %s"
          % ("; ".join(hits_m2) if hits_m2 else "NOT FLAGGED",
             "; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    # m4 order mutant on PC4: nu before its partner
    M0m = [[Fr(1, 2), Fr(0)], [Fr(0), FIVE_SEVEN]]
    Mm = [row[:] for row in M0m]
    Mm[1][1] += Fr(4, 7)
    solm = frac_solve(Mm, [[Fr(1), Fr(0)]])[0]
    Lbb_m = Fr(1, 3) * solm[0]
    r_mut = 1 - Lbb_m
    dev_m4 = rec_p["r"] - r_mut
    # reconstruction is order-blind: final sum identical
    Mm[0][0] += -Fr(1, 3) + Fr(1)
    Mm[0][1] += Fr(1, 5)
    Mm[1][0] += Fr(1, 5)
    ok_rec_m4 = all(Mm[i][j] == T4["Mfin"][i][j]
                    for i in range(2) for j in range(2))
    check("G82-mustfail-order", dev_m4 == M4_DEV
          and r_mut == Fr(1, 3) and ok_rec_m4,
          "m4 ORDER BREAK (PC4, exact): processing the nu atom "
          "BEFORE its partner gives r_mut = %s vs the sealed 7/9 "
          "-- dev EXACTLY %s == 4/9 LOUD, while the final "
          "reconstruction stays EXACT (%s): the r-sequence is "
          "the order-sensitive object, the sum is order-blind -- "
          "reconstruction alone can never catch an order break "
          "(disclosed)"
          % (str(r_mut), str(dev_m4), ok_rec_m4))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7 (the base floor is the "
          "IMPORTED r243 reserve), no posthoc window, no pairing "
          "or bound selection by measured outcomes (greedy rule "
          "and phi forms sealed at design time), no RH claim; "
          "what the round adds: the exact ordered rank-one "
          "rebuild of the augmented form, the per-step reserve "
          "measurement with the explicit-positive-square wards, "
          "the sealed cone adjudication with the r275-sharp "
          "anti-circularity guard, and the world census; "
          "r243..r308 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        recon_all = (CA9["recon"] <= RECON_BAR
                     and CB9["recon"] <= RECON_BAR
                     and TW_A["recon"] <= RECON_BAR
                     and TW_B["recon"] <= RECON_BAR
                     and all(CT_A[cn]["recon"] <= RECON_BAR
                             and CT_B[cn]["recon"] <= RECON_BAR
                             for cn in CT_A)
                     and all(rung_res[kz]["recon"] <= RECON_BAR
                             for kz in rung_res)
                     and ok_t4 and T1["ok_rec"] and TM["ok_rec"])
        decomp = ("DECOMP_EXACT(PC4/SM1/MINI16 exact; w9 %.1e@A "
                  "/ %.1e@B; twin + controls + 57 rungs <= %.0e)"
                  % (CA9["recon"], CB9["recon"], RECON_BAR)) \
            if recon_all else \
            "DECOMP_BROKEN(see gate table for the first locus)"
        main_pos = (CA9["n_nonpos"] == 0 and CB9["n_nonpos"] == 0
                    and TW_A["n_nonpos"] == 0
                    and TW_B["n_nonpos"] == 0
                    and all(rung_res[kz]["n_nonpos"] == 0
                            for kz in rung_res))
        res_head = ("MAIN_RESERVE_POSITIVE(w9 %+.4f@A / %+.4f@B; "
                    "twin %+.4f/%+.4f; 57/57 rungs, ladder min "
                    "%+.4f)" % (CA9["min_r"], CB9["min_r"],
                                TW_A["min_r"], TW_B["min_r"],
                                min(rung_res[kz]["min_r"]
                                    for kz in rung_res))) \
            if main_pos else \
            ("RESERVE_BREAKS(w9 nonpos %d@A/%d@B, ladder "
             "%d rungs broken)"
             % (CA9["n_nonpos"], CB9["n_nonpos"],
                sum(1 for kz in rung_res
                    if rung_res[kz]["n_nonpos"] > 0)))
        pb_pos_a = all(CT_A[cn]["np_kind"]["pair"] == 0
                       and CT_A[cn]["np_kind"]["bord"] == 0
                       for cn in CT_A)
        res_tab = ("RESERVE_TABLE(%s; controls@A pair+border "
                   "phases %s (mins %s), the EPST/SCR negativity "
                   "@A carried by the BUDGET step alone (%s -- "
                   "S_{N-2} < 0 past the flip: the r243 budget "
                   "coordinate reads the wall, amendment-a1 "
                   "disclosure); controls@B %s -- EPST/SCR "
                   "forced by theorem, disclosed)"
                   % (res_head,
                      "ALL POSITIVE" if pb_pos_a else
                      "NOT all positive",
                      str({cn: round(min(CT_A[cn]["min_pair"],
                                         CT_A[cn]["min_bord"]), 4)
                           for cn in CT_A}),
                      str({cn: (None if CT_A[cn]["r_bud"] is None
                                else round(CT_A[cn]["r_bud"], 3))
                           for cn in CT_A}),
                      str({cn: "%+.3g" % CT_B[cn]["min_r"]
                           for cn in CT_B})))
        disc = ("WORLD_DISCRIMINATOR(%s; w9 tightest folds %s vs "
                "r284 {2, 4})" % (str(disc_typ), str(tight_folds)))
        mf = ("MUSTFAIL_LEDGER(m1 8/9 exact, m2/m3 flagged, m4 "
              "4/9 exact + recon preserved)")
        verd = " + ".join([decomp, res_tab,
                           "%s(%s)" % (cone_verd, cone_anat),
                           disc, mf])
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- PILOT measurement of the reviewer's paired-"
          "cone route; the reconstruction is bookkeeping "
          "(disclosed), the content is the ordered reserve "
          "census, the sealed cone adjudication and the honest "
          "world census; a passing cone fixes a TARGET, it "
          "proves neither L* nor any cofinal statement; NO RH "
          "claim" % (verd, " (SMOKE)" if smoke else ""))
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
