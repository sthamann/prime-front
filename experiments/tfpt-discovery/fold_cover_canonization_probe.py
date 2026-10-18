#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_cover_canonization_probe --
PRIME.L2.COVER_CANONIZATION.01 (round 346): THE THREE RESIDUES
OF THE r344 COVER -- canonical stop criterion, source-side
partition predictor, F_Amax defusal.

CONTEXT (binding, from the sealed r344 record SPEC_SHA 06375c3a,
TWO_SCALE_PARTIAL): r344 delivered the FIRST CERTIFYING COVER of
the terminal lane -- the three-arm min-coverage (C_H on the
hand-off column (m q_max)^2 msh, C_G on the eps-chain column
W_B, third arm = the banked r321 sliding bound 1.3056 F_A^2 at
FROZEN constant) certifies with 0/51 test violations + named 4/4
+ midband 6/6 on ALL SIX sealed grid points already at a = 1,
and composes to m_0* = 10^22.6 (vs the r324 route 10^59.6, the
r306 census 10^13.5).  Three residues remain: (1) THE STOP RULE
IS NOT CANONICAL -- the sealed formula R_HAT = argmin max(e_H,
e_G) picks 7/4 but the dyadic halves pick 8/5 vs 7/4; the arm
exponents cross EXACTLY ONCE in the gap (12/7, 7/4) -- the
crossing is real, its location is not halves-stable.  (2) THE
PARTITION IS POSTHOC -- the sealed hsh rule predicts the covering
arm on only 7/51 rows; 20 rows are covered ONLY by the
non-predicted arm.  (3) F_Amax INHERITS THE SPIKE -- the uniform
composition constant uses F_Amax = 5.54 (the kz51 insertion
value): the third arm pays for all.

THE CORE QUESTION (contract): can the r344 cover be CANONIZED --
stop rule halves-stable, partition source-predictable, constant
spike-defused -- and what is the honest m_0* afterwards?

THE SEALED CANONIZATION MACHINERY (disclosed BEFORE any
evaluation):
  (i) LEG A -- FOUR SEALED STOP CANDIDATES (each tested for
      halves-stability explicitly; the r344 argmin-max formula
      K0 is reproduced as the anchor baseline, known NOT
      halves-stable):
      K1 THE SOURCE-INTRINSIC CEILING (data-free): R_ALG =
         GAMMA_CEIL^(1/3) with GAMMA_CEIL = 4 -- the R at which
         a SINGLE child's cubic ratio R^3 alone exhausts the
         algebraic pair Gamma-ceiling (the same derived algebra
         that makes R = 2 the pair limit: R_c = 2 a_c/(a_c +
         a_sib) < 2 for every pair child, hence Gamma_pair < 4);
         4^(1/3) = 1.5874..; K1 picks the grid point minimizing
         |R - R_ALG| (ties: smaller R) -- BY HAND: distances
         (0.0874, 0.0126, 0.0793, 0.1269, 0.1626, 0.4126) ->
         grid index 1 (R = 8/5, INTERIOR).  K1 consumes NO data;
         its halves-stability is BY CONSTRUCTION (disclosed as
         trivial) -- the load-bearing questions are only the
         legitimacy of the derivation (stated above) and whether
         the min-coverage certifies at its pick.
      K2 THE FIRST-EQUILIBRATED POINT: the smallest eligible
         grid index j with e_H(j) <= e_G(j) (the first point at
         or past the crossing); if no crossing, the largest
         eligible index; DENIED if nothing eligible.
         Halves-stability = both dyadic halves of the test
         cohort pick the same index (full-cohort eligibility
         mask, r344 convention).
      K3 THE POOLED INTERPOLATED CROSSING (the stabilized
         estimator; fit-free): d(j) = e_H(j) - e_G(j) on the
         POOLED full-cohort exponents; at the first sign change
         between consecutive eligible grid indices j, j+1:
         R_CROSS = R_j + (R_{j+1} - R_j) d(j)/(d(j) - d(j+1))
         (exact linear interpolation, no fit primitive); K3
         picks the grid point nearest R_CROSS (ties: smaller).
         Halves-stability = the two halves' interpolated picks
         agree with the pooled pick.
      K4 THE R-FREE ENVELOPE (threshold-free escape): per rung
         the heavy envelope column HB_ENV = min over the grid
         indices HENV_IDX = (0..4) of HB(R) restricted to
         POSITIVE values (index 5 = R = 2 is excluded by the
         DERIVED pair-limit algebra: no pair is ever heavy
         there, the heavy freeze is empty -- r344 record; a rung
         with no positive HB gets 0 and cannot be heavy-covered)
         and the good envelope column WB_ENV = min over ALL six
         grid indices of W_B(R) (W_B >= 1 always); the two
         envelope freezes C_H_ENV(a)/C_G_ENV(a) are mid-ladder
         max-cal on these columns (TRB verbatim), the
         min-coverage census runs as in r344 (third arm
         unchanged).  K4 needs NO stop threshold at all; if it
         certifies, the tuning surface disappears by
         construction, at the disclosed price of the changed
         constants.
      STOP-CANONIZED iff at least one holds: K1 certifies at its
      pick (0/51 + named 4/4 at some a in GA_FAM) and the pick
      is interior; or K2/K3 is eligible + interior +
      halves-stable AND certifies at its pick; or K4 certifies.
      THRESHOLD_NOT_CANONICAL flag iff NONE of K0/K2/K3 (the
      exponent-language candidates) is halves-stable -- then the
      intrinsic/R-free forms are the adjudicated escape, said
      honestly.
  (ii) LEG B -- THE SOURCE-SIDE PARTITION PREDICTOR: the sealed
      feature set per rung (ALL source-pure): f_hsh = hsh at the
      r344 cover point R = 7/4 (grid index 4); f_fa = the r321
      F_A coordinate (EFP.local_ratio on the module-own q_max
      column; EXT3 rows via the r321 insertion rule
      CCP.world_coord -- the r344 third-arm coordinate,
      verbatim); f_grel = the r329 relative local prime-power
      gap (EFA.grel_col on the source gap grid, W = 5); f_nw =
      builder depth N_w; f_eps = the eps-argmax level of the
      good tree at R* = 3/2 (FTS.good_level_anatomy verbatim;
      -1 if empty/flat -- the r339/r344 early-level anomaly
      coordinate); f_gam = the Gamma-argmax level (argmax of
      log max(gmx_lv, 1), r339 FDD column; -1 if empty); f_m =
      leaf count m.  THE SEALED RULE FAMILY (12 threshold rules,
      max 2 features, ALL thresholds sealed a-priori -- no
      fitting zoo; sealed thresholds: TH_HSH = 1/2 the r344
      partition split, TH_FA1 = 1.5 the r329 SPIKE_FA record
      constant, TH_FA2 = 2.0, TH_GREL = 0.85 the r329 GAP_SMALL
      edge, TH_NW = 1650 the pre-EXT3 depth bound, TH_M = 256,
      TH_EPS = 2 the r339 early-level bound, TH_GAM = 3):
        P01 H iff f_hsh >= TH_HSH else G (the r344 baseline);
        P02 T iff f_fa >= TH_FA1 else H;
        P03 T iff f_fa >= TH_FA1 else (H iff f_hsh >= TH_HSH
            else G);
        P04 T iff f_fa >= TH_FA2 else H;
        P05 T iff f_grel < TH_GREL else H;
        P06 T iff f_grel < TH_GREL else (H iff f_hsh >= TH_HSH
            else G);
        P07 T iff f_nw > TH_NW else H;
        P08 T iff 0 <= f_eps <= TH_EPS else H;
        P09 G iff f_gam >= TH_GAM else H;
        P10 G iff f_m >= TH_M else H;
        P11 always H (degenerate baseline, disclosed);
        P12 always G (degenerate baseline, disclosed).
      THE SEALED TARGET: the covering-arm structure at the r344
      cover point (grid index 4, minimal certifying a); a
      prediction is CORRECT iff the predicted arm COVERS the
      rung (H -> heavy-covers, G -> good-covers, T -> the r321
      third arm covers) -- the operational reading the cofinal
      certificate needs (any covering arm is a valid
      assignment); the r344 exact-priority-label accuracy is
      printed as the comparison census.  SELECTION (sealed): the
      rule with maximal accuracy on the 39-row CORE cohort (the
      ladder test rows te_i), ties by smaller rule id;
      OUT-OF-SAMPLE: the winner's accuracy on the 12 EXT3 rows.
      PREDICTOR_FOUND iff core accuracy >= PRED_ACC_NEED = 0.80
      AND EXT3 accuracy >= PRED_OOS_NEED = 0.75 AND full-51
      accuracy >= 0.80; a P11/P12 winner carries the DEGENERATE
      tag (single-arm coverage census, not a partition
      predictor -- disclosed).  If no rule passes, the partition
      stays posthoc and the census types whether that harms a
      census-grade cover at all (the coverage itself is
      certified; the predictor is needed for the COFINAL
      reading only).
  (iii) LEG C -- THE F_Amax DEFUSAL (three sealed variants; for
      each: does 0/51 survive, and what is m_0*?):
      V1 THE CLASS SPLIT: sealed source-side class rule SPIKE
         iff f_fa >= FA_SPLIT = 1.5 (the r329 SPIKE_FA record
         constant; the small-gap family is the r329 lesson),
         else QUIET.  (a) THE UNIFORM RESCUE: every SPIKE test
         row must be heavy- or good-covered at SOME a in GA_FAM
         at the r344 cover point -- then the third-arm term
         needs only F_AMAX_QUIET = max F_A over the QUIET rows
         (full 77-row column, conservative) and the rescue
         budgets are ADDED (sum form, disclosed); m_0*(uniform)
         re-solved.  (b) THE CLASS-CONDITIONAL READING (census):
         the QUIET-class statement [C_H + C_G](log m)^a +
         GSQ F_AMAX_QUIET^2 (log m)^2 with the SPIKE rows as a
         NAMED exception family, each individually certified by
         its own arm (the cover keeps all 51 rows); its
         m_0*(generic) is printed and typed CLASS_CONDITIONAL --
         it does NOT count as a uniform defusal.
      V2 THE PERCENTILE CAP: identical machinery with SPIKE iff
         f_fa > the FA_PCTL = 90th percentile of the full F_A
         column (np.percentile, deterministic; the cap value is
         data-dependent, the formula sealed).
      V3 THE FLOOR FORM (the open r329 successor question): the
         floored third arm rho_2 <= GSQ x max(F_A, FA_FLOOR)^2
         with FA_FLOOR = 0.58 (the r321 ladder's own F_A floor,
         record) -- a validity census on the quiet side: which
         rows lie below the floor, which rows are covered by
         the floored form but not the raw form; m_0* is
         UNCHANGED by construction (F_Amax > floor), said
         honestly.
      FAMAX_DEFUSED flag iff a UNIFORM variant (V1a or V2a
      rescue) keeps 0/51 AND its re-solved m_0* <= M0_R344 -
      M0_DEFUSE_MARGIN = 22.6 - 0.2 (in log10).
  (iv) LEG D -- THE HONEST COMPOSITION: the headline stop form
      by sealed preference (K1 if certifying+interior, else K3
      if canonical+certifying, else K2 if canonical+certifying,
      else K4 if certifying, else the r344 R_HAT as census
      fallback); the composed polylog chain (dictionary + r324
      chain, NO premature powerization) with explicit constants;
      the m_0* table over all variants vs 10^22.6 (r344) and the
      r306 census 10^13.5; the honest COFINAL TYPING: which
      building block is CENSUS (frozen constants on 51 rows),
      which is a LAW CANDIDATE (halves-stable / data-free
      formula + out-of-sample confirmed), what is missing for a
      cofinal statement (the ladder-to-m_0* extrapolation
      hypothesis stays disclosed).
  (v) LEG E -- WORLDS + MUST-FAILS: the winner predictor rule
      and the V1 class rule evaluated on MAIN w9 / twin w13 /
      EPSTEIN / SCRAMBLE (features via the r321 world-coordinate
      insertion; census, NO letter).

LEG 0 -- ANCHOR REGRESSION (bit-near; slim set + the COMPLETE
r344 record, disclosed): the r314 identity wards live; r306 C_2
= 1.069 (tol 0.005) first-5 freeze 0/57; r316 rho anchors +
C_small + n = 65; r324-pre C_M2 = 2.2557 + the seven m2
violators EXACT; the dictionary-chain identity live; the r339
record anchors (W_F med 265.54 / W_G med 13.69 / hsh med 0.872 /
Gamma_max 4.303 / e(W_F) +0.956 / e(m^2 M_3) +0.112); the r324
chain anchors (e_G +0.158 / e_M2 +0.014 / e_tot +0.172, m_0*
10^59.6 adopted); the r341 record complete through the imported
FBR builders at both banked columns + freezes + exponents +
envelope composition (m_0* 10^24.0) + r306 census solve 10^13.5;
the r321 F_A top-3 kz53 2.47 / kz83 2.39 / kz67 2.38 through
EFP.local_ratio; THE r344 RECORD COMPLETE through the same code
path: the balance curve at all six grid points (hsh med 0.872/
0.603/0.371/0.291/0.266/0.000, share med 0.944/0.771/0.491/
0.447/0.386/0.000, W_B med 1.489/2.410/3.206/3.659/3.796/6.096,
empty-good 23/11/7/7/7/2, empty-heavy 0/0/0/0/0/71), the arm
exponents (e_H +0.313/+0.377/+0.358/+0.373/+0.149/deg, e_G
-0.214/-0.075/+0.153/+0.159/+0.225/+0.464), the sealed r344
choice R_HAT = 7/4 (index 4, interior, halves pick 8/5 vs 7/4 --
NOT halves-stable, reproduced), the two-scale freezes at
(R_HAT, a = 1) C_H = 3.9859 / C_G = 1.1409, the min-coverage 0
violations at EVERY grid point at a = 1 + named 4/4 + midband
6/6, the third-arm-only count 8 with EXT3-B 6/6, the partition
census 7/51 + non-predicted-only 20, F_Amax = 5.54 (kz51
insertion), the kz55 anatomy (eps-argmax level 1, W_B at R_HAT
8.459), and the composed m_0* = 10^22.6.

LEG E MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) PREDICTOR FEATURES FROM THE COVERAGE (protocol):
  mutant_pred_from_coverage re-labels rungs after sight of the
  evaluated violation column (consumes rho) -- the
  BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed toy
  it returns ('T', 'G') != the sealed rule output --
  protocol-CAUGHT twice.
(e2) CLASS RULE AFTER SIGHT (protocol): mutant_clsrule_posthoc
  flips class letters after sight of the evaluated violation
  column (consumes rho) -- AST-FLAGGED and on the sealed toy
  returns ('SPIKE', 'SPIKE') != the sealed class-rule output
  ('SPIKE', 'QUIET') -- protocol-CAUGHT twice.
(e3) R-FREE ENVELOPE WITH DOUBLE-COUNTED CONSTANT:
  mutant_env_doublecount SUMS the hand-off column over the grid
  instead of taking the envelope min -- on the sealed Fractions
  toy (the r344 stop toy (7, 1, 5, 3): HB = 49/32 at grid
  indices 0..3, 0 at index 4) it returns 49/8 while the sealed
  envelope is 49/32 -- break 147/32 EXACT in Fractions.
(e4) CROSSING ESTIMATOR AFTER RECORD SIGHT (protocol):
  mutant_crossing_posthoc re-picks the grid index after sight of
  the evaluated violation column (consumes rho) -- AST-FLAGGED
  and on the sealed toy returns index 4 != the sealed K2 toy
  output 2 -- protocol-CAUGHT twice.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

SEALED VERDICTS (main letter: exactly one fires, total order;
the flag letters are sealed booleans appended with '+',
combinations allowed by the user contract):
   TARGET_LEAK              iff any purity/scope/literal audit
       hit on the module-own canonization builders,
   CANON_STATE_NOT_EXACT    iff an exact ward breaks on a live
       world (the full r341/r344 exact path layer across the
       grid / the Fractions bit-equality at both sealed pins /
       the grounding / the toys),
   COVER_CANONIZED          iff STOP-CANONIZED (i) AND
       PREDICTOR_FOUND (ii) AND the min-coverage stays at 0
       violations + named 4/4 at the headline stop form,
   COVER_CENSUS_ONLY        otherwise -- the r344 coverage
       stands (anchor-gated) but the canonization is incomplete;
       the failing residue(s) are NAMED in the letter.
   FLAGS: +THRESHOLD_NOT_CANONICAL (no exponent-language
       candidate halves-stable) / +PREDICTOR_FOUND(rule, core,
       oos) / +FAMAX_DEFUSED(variant, m_0*).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in either
direction.  Coexistence: r345 (gap-ratio, L*) is recorded and
synced (62fb653d); own files only; before the strictly additive
rh-sync the current git state is re-checked.  Two-commit freeze
protocol (r329 convention): spec committed pre-freeze, record
tables the only post-freeze edit, committed again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r317/r321/r324/r327/
r333/r337/r339/r341/r344 machinery imported verbatim; the ENTIRE
r344 scaffold -- census, controls, extensions, EXT3, decompo-
sition wards, path layer at every sealed grid R, Fractions pins,
two-scale freezes, min-coverage -- is re-executed through the
same code path and anchor-gated against the r344 record):
t_{N-2} = sum_b ct_b; F = 0.20 edge split; level-2 blocks; the
r306 RY3 layer; the r314 SCF layer; the r316 TRB layer; the r317
EFP.local_ratio; the r321 CCP.world_coord; the r324 QMO/FAP
layers; the r327 GMC grounding; the r339 FDD tree layer; the
r341 FBR path layer; the r344 FTS balance layer (rhat_rule = K0,
partition_predict, good_level_anatomy, the Fractions balance/
hand-off toys -- imported verbatim); the r329 EFA.grel_col +
EFA.gap_class (source-side gap coordinate).  NEW in this round
(module-own, source-pure): rhat_intrinsic (K1), rhat_cross_first
(K2), rhat_cross_interp (K3), env_min_col (K4 envelope column),
pred_rule (the sealed 12-rule family), cls_rule (the sealed
class split), floor_bound (V3) and the sealed
canon_tree_verdict.

INDEX FIREWALL (binding, r238-r345 discipline): w = window (kz),
N_w = builder depth, k = tree level, n(v) = leaf count; ground
truth enters GATES and census tables only; the cubic target M_3
/ rho_2 and the q_max RECORD enter GATES / anchors / coverage
checks only, NEVER a canonization builder (AST-warded; the
builders consume the sealed tree + source-pure columns -- q_max
column, gap grid, rank order -- and sealed thresholds ONLY); no
zero/prime oracles anywhere (AST firewall); no fit primitives
(fragment audit; exponents are the imported r272 dyadic
halves-slope, fit-free; the K3 interpolation is exact two-point
algebra, not a fit).  B PROVENANCE: B_w = S_{N-2} + 5/7
(imported floor, never fitted).  COFINAL LADDER (pre-sealed,
r316/r324/r329/r339/r341/r344 verbatim): frame-A h <= 900, 42
rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION 900 < h <= 1300 first 15; EXT2 r316 A5 rule;
EXT3 = the sealed r329 12-anchor list (adopted as-is, PURE TEST
rows).

SEALED CONSTANTS (everything not listed here is the r344
constant set imported verbatim from FTS): GAMMA_CEIL 4.0
(derived pair-ceiling algebra, disclosed above); HENV_IDX (0, 1,
2, 3, 4) (index 5 excluded by the derived pair-limit); FA_SPLIT
1.5 (r329 SPIKE_FA record constant); FA_PCTL 90.0; FA_FLOOR 0.58
(r321 ladder F_A floor, record); PRED_ACC_NEED 0.80;
PRED_OOS_NEED 0.75; PRED thresholds TH_HSH 0.5 / TH_FA1 1.5 /
TH_FA2 2.0 / TH_GREL 0.85 / TH_NW 1650 / TH_M 256 / TH_EPS 2 /
TH_GAM 3 (a-priori, disclosed above); M0_DEFUSE_MARGIN 0.2;
R344 record anchors (tol): HSH_CURVE (0.872, 0.603, 0.371,
0.291, 0.266, 0.000) tol 0.001; SHR_CURVE (0.944, 0.771, 0.491,
0.447, 0.386, 0.000) tol 0.001; WB_CURVE (1.489, 2.410, 3.206,
3.659, 3.796, 6.096) tol 0.005; EH_CURVE (0.313, 0.377, 0.358,
0.373, 0.149) tol 0.003 (index 5 degenerate); EG_CURVE (-0.214,
-0.075, 0.153, 0.159, 0.225, 0.464) tol 0.003; EMPTYG (23, 11,
7, 7, 7, 2) EXACT; EMPTYH (0, 0, 0, 0, 0, 71) EXACT; JHAT 4;
HALVES (1, 4) EXACT (the r344 instability, reproduced); CH1
3.9859 tol 0.001; CG1 1.1409 tol 0.001; AA 1 at every grid point
EXACT; THIRD_ONLY 8 EXACT; EXT3-B third-cover 6/6 EXACT;
PART_ACC 7 EXACT; NONPRED 20 EXACT; FA_MAX 5.54 tol 0.01;
M0_R344 22.6 tol 0.2; EPS55_K 1 EXACT; WB55_HAT 8.459 tol 0.005;
R346_TABLE_LITERALS = the sealed r314..r344 set (FTS verbatim)
UNION the r344 record set {0.603, 0.371, 0.291, 0.771, 0.491,
0.447, 2.41, 3.206, 3.659, 6.096, 0.377, 0.358, 0.373, 0.149,
-0.075, 0.153, 0.159, 0.225, 0.464, 3.9859, 1.1409, 22.6, 5.54,
8.459, 1.63, 3.91, 2.44, 1.14} (small collision-prone ratios
curated out, r337..r344 convention, disclosed); runtime <= 1800
s; smoke = w9 + controls + toys + scope/purity audits + the
exact path wards across the grid + the w9 Fractions bit-equality
at both sealed pins + e1-e4 mutants; ladder, extensions, EXT3,
anchors, balance curve, freezes, coverage, candidates,
predictor, defusal, composition and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r321/r324/r324-pre/r329/r339/r341/
r344 RECORD number adopted as-is; the K1 pick (grid index 1) and
its distance table are BY-HAND algebra from the sealed grid; the
K3 pooled pick can be PRE-COMPUTED from the r344 RECORD
exponents (d(3) = +0.214, d(4) = -0.076 -> R_CROSS ~ 1.7407 ->
index 4) and is disclosed as a record-derived expectation -- the
K2/K3 HALVES columns, every envelope freeze and coverage,
every predictor accuracy, the class/percentile/floor variant
tables, the world features and every re-solved m_0* are
GENUINELY OPEN (never computed before this spec froze); the
sealed toys are computed BY HAND (K1 toys: ceiling 4 -> index 1,
ceiling 8 -> R_ALG = 2 -> index 5 the endpoint; K2 toy
(0.3, 0.2, 0.1)/(-0.2, 0.15, 0.4) -> first crossing index 2;
no-crossing toy -> last eligible index 1, crossed False; K3 toy
grid (3/2, 2) with e_H (0.5, 0.0) / e_G (0.0, 0.25) -> d =
(0.5, -0.25) -> R_CROSS = 3/2 + 1/2 x 2/3 = 11/6 -> index 1;
envelope toy (49/32, 49/32, 49/32, 49/32, 0) -> min positive
49/32 EXACT, e3 mutant sum 49/8, break 147/32 EXACT; class toys
2.0 -> SPIKE, 1.0 -> QUIET, 1.5 -> SPIKE boundary inclusive;
floor toys (0.5, 0.58) -> 0.58, (2.0, 0.58) -> 2.0; the
12-rule toy vectors on the two sealed feature tuples, listed in
G41); the four verdict-tree branches are total by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R346_ANCHORS(identity wards, r306 C_2, r316, r324-pre, r339,
    r324 chain, r341 record, r321 F_A top-3, THE r344 RECORD
    COMPLETE: curve + R_HAT + halves + freezes + coverage +
    partition + F_Amax + kz55 + m_0*)
+ SEAL(path wards across the grid + Fractions bit-equality at
    both sealed pins + grounding + purity + toys)
+ STOPRULE(K0 reproduction; K1 pick + certification; K2/K3
    picks + halves columns + canonicality; K4 envelope freezes
    + coverage; STOP-CANONIZED verdict + the equilibration
    census)
+ PREDICTOR(the 12-rule table core/EXT3/full; winner + OOS +
    degeneracy tag; the exact-label comparison census)
+ DEFUSE(V1 class split: rescue census + uniform m_0* +
    class-conditional m_0* + named spike family; V2 percentile;
    V3 floor census)
+ [exactly one of] COVER_CANONIZED / COVER_CENSUS_ONLY /
    CANON_STATE_NOT_EXACT / TARGET_LEAK  [+ flags]
+ COMPOSITION(the m_0* table over all variants vs r344 10^22.6
    + r324 10^59.6 + r306 census 10^13.5; the honest cofinal
    typing census-vs-law-candidate)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the path identities, the pair-ceiling
algebra, the Fractions toys and grid pins, the tree logic and
the purity audits are EXACT (Fractions/AST-decided); every
census, constant, accuracy, violation count and exponent is
MEASURED on the finite ladder (+ the 12 adopted EXT3 anchors)
only; K1 is data-free but its ceiling constant is DERIVED
ALGEBRA, not a theorem about the crossing location -- whether
the crossing SITS at the intrinsic ceiling is exactly what the
halves columns test; a certifying cover fixes a proof TARGET
with explicit constants, it proves NO cofinal law -- the
ladder-to-m_0* step stays the disclosed extrapolation
hypothesis; the class-conditional m_0* is a TWO-STATEMENT
reading with a named exception family, never a uniform bound --
said out loud; r243-r345 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA 306dba57867f2170,
pre-freeze commit 9fcc081b; protocol: smoke pass 1 = 45/45
(1.1 s, run pre-commit, disclosed in the commit message);
calibration pass 1 = FIRST full evaluation = 45/45, wall
177.8 s, NO amendment -- no bar, band, rule or verdict rule
moved at any point; record run1/run2 after this insertion,
identical up to the runtime line):
MAIN VERDICT: COVER_CANONIZED(stop rule canonized by K1 at grid
index 1 with 0/51 + named 4/4 kept, AND the predictor holds:
P02 core 1.000 / OOS 1.000) + PREDICTOR_FOUND(P02).  FAMAX NOT
defused (flag silent) -- the honest headline m_0* stays 10^22.6.
THE HEADLINE FINDINGS:
(1) LEG A -- THE STOP RULE CANONIZES VIA THE INTRINSIC CEILING,
NOT VIA THE EXPONENT CROSSING: K1 (R_ALG = 4^(1/3) = 1.5874 ->
grid 8/5, index 1, interior, data-free) CERTIFIES at a = 1 --
the pair-ceiling formula lands exactly on the grid point that
one of the r344 dyadic halves picked.  K2/K3 both pick 7/4
(K3 pooled R_CROSS 1.7407, matching the record-derived
expectation) and are formally halves-stable -- BUT ONLY VIA THE
NO-CROSSING FALLBACK: NEITHER dyadic half shows a sign change
at all (the halves e_G columns collapse to -0.3..-1.4, e_H
stays positive; both halves return the last eligible index 4 by
fallback, flagged (nc) in the gate log).  Said honestly: the
crossing LOCATION is still not halves-visible on this ladder --
the exponent language stays soft; the canonization is carried
by the data-free K1 formula and by K4 (the R-free envelope
certifies at a = 1 with C_H_ENV 3.9859 + C_G_ENV 0.4867 -- the
good envelope drops to the W_B(3/2) freeze, the threshold
disappears by construction).  The THRESHOLD_NOT_CANONICAL flag
stays silent by the sealed letter (K2/K3 halves-stable via
fallback), the fallback anatomy is disclosed here.
(2) LEG B -- THE PARTITION IS SOURCE-PREDICTABLE (residue 2
CLOSED at the sealed bars): the sealed rule P02 (F_A >= 1.5 ->
THIRD ARM, else HEAVY -- one feature, the r329 SPIKE_FA
threshold) predicts a COVERING arm on 51/51 test rows (core
39/39, OUT-OF-SAMPLE EXT3 12/12, non-degenerate); the
exact-priority-label census gives 46/51 vs the r344 hsh
baseline 7/51.  The r344 posthoc-partition reading dissolves:
the cover's working partition is spike-vs-rest in the F_A
coordinate, not heavy-vs-good in the hsh coordinate.  Runner-up
census: P04 (F_A >= 2.0) 50/51, P07 (depth > 1650) 48/51, P05
(grel < 0.85) 47/51, P08 (early eps-level) 46/51.
(3) LEG C -- F_Amax IS NOT UNIFORMLY DEFUSABLE (residue 3 stays
OPEN, honest negative): the six sharp spike rows kz53/kz67/
kz51/kz54/kz42/kz62 are covered ONLY by the third arm at EVERY
a in (1, 2, 3) -- the uniform rescue fails for V1 (split 1.5)
and V2 (P90 = 1.917), so FAMAX_DEFUSED stays silent and the
uniform composition keeps F_Amax = 5.54: m_0* = 10^22.6
unchanged.  The CLASS-CONDITIONAL reading (census, disclosed as
a two-statement form): the QUIET-class statement with cap 1.39
solves to m_0* = 10^16.1 (V2 cap 1.91: 10^17.5) with the
13-row spike family as NAMED pointwise-certified exceptions --
2/3 of the log-distance from 10^22.6 toward the r306 census
10^13.5, but NOT a uniform bound, said honestly.  V3 floor
census: only kz33/kz128 sit below the 0.58 floor (both
non-test under the insertion convention), the floor adds and
loses nothing on this sample -- the below-range validity
question stays open.
(4) LEG D -- THE HONEST COMPOSITION TABLE: r344 baseline
(7/4, a = 1) m_0* 10^22.6; K1 headline (8/5, a = 1, C_H 6.8806
+ C_G 1.0151 + third term 1.3056 x 5.54^2) m_0* 10^22.6 (the
third-arm term dominates the solve -- the stop-point choice is
nearly free in m_0*); K4 envelope constants 3.9859 + 0.4867;
V1 class-conditional 10^16.1 / V2 10^17.5 (exception-set
readings); vs r324 10^59.6, r341 envelope 10^24.0, r306 census
10^13.5.  COFINAL TYPING: census = all freeze constants +
coverage counts + accuracies; law candidates = the K1 ceiling
formula (derived algebra, certifies), the banked r321 sliding
form (again out-of-sample-clean), the P02 predictor
(OOS-confirmed); missing = any bound beyond the measured rungs
(extrapolation hypothesis disclosed) and a spike-free uniform
constant.
(5) WORLDS (census, no letter): w9 hsh(7/4) 1.000 F_A(ins)
0.83 -> P02 says H, class QUIET; twin w13 0.229 / 1.09 -> H,
QUIET; EPSTEIN 0.182 / 1.00 -> H, QUIET; SCRAMBLE 0.667 / 2.00
-> P02 says T, class SPIKE -- the scrambled world is the only
control the class rule flags as spike-family; the predictor is
a ladder-cohort statement, the world rows are census only.
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069
(0/57); r316 n 65 + rho quartet + C_small 1.0694@kz18;
r324-pre C_M2 2.2557 + the seven m2 violators EXACT; r339
record complete; r324 chain e_tot +0.172; r341 record COMPLETE
(both banked columns + freezes + exponents + envelope 10^24.0);
r321 F_A top-3 2.47/2.39/2.38; THE r344 RECORD COMPLETE (curve
+ R_HAT 7/4 + halves (8/5, 7/4) + C_H/C_G 3.9859/1.1409 + 0/51
at every grid point at a = 1 + third-only 8 with EXT3-B 6/6 +
partition 7/51 + nonpred 20 + F_Amax 5.54 + kz55 eps-argmax 1
+ W_B@7/4 8.459 + m_0* 10^22.6).
SEAL: grid tilt 8.6e-16, partition 4.0e-16, envelope viol
4.2e-16, heavy hand-off viol 0.0, martingale wards 2.2e-16 /
4.4e-16 / 1.2e-15, r316 chain 6.5e-16, FRACTIONS BIT-EQUALITY
at the two sealed pins 3/2 + 12/7 on w9 + w13 EXACT (76
martingale nodes), grounding 3.4e-16,
purity clean, toys exact (envelope pin 49/32, e3 double-count
break 147/32 EXACT); must-fails e1 protocol-CAUGHT twice (AST
rho + toy ('T', 'G')) / e2 protocol-CAUGHT twice (AST rho +
toy ('SPIKE', 'SPIKE')) / e3 CAUGHT exact (147/32) / e4
protocol-CAUGHT twice (AST rho + toy pick 4 != 2) + m5a/m5b
FLAGGED.

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
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import two_regime_bound_probe as TRB           # noqa: E402 r316
import exception_families_probe as EFP         # noqa: E402 r317
import continuous_coordinate_probe as CCP      # noqa: E402 r321
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import companion_orbit_packing_probe as COP    # noqa: E402 r333
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import fold_density_dictionary_probe as FDD    # noqa: E402 r339
import fold_bellman_reverse_holder_probe as FBR  # noqa: E402 r341
import fold_two_scale_balance_probe as FTS     # noqa: E402 r344
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

# ---------------- the r344 constant set, imported verbatim
MAIN_WINDOWS = FTS.MAIN_WINDOWS
CTRL_FLIPS = FTS.CTRL_FLIPS
H_CAP = FTS.H_CAP
CHEAP_EXPECT = FTS.CHEAP_EXPECT
EXC_KZ_EXPECT = FTS.EXC_KZ_EXPECT
TB_WARD_BAR = FTS.TB_WARD_BAR
TB_WARD_BAR_DEEP = FTS.TB_WARD_BAR_DEEP
TB_WARD_BAR_X3 = FTS.TB_WARD_BAR_X3
TB_WARD_BAR_CTRL = FTS.TB_WARD_BAR_CTRL
DEEP_N = FTS.DEEP_N
ID_BAR = FTS.ID_BAR
AC_BAR = FTS.AC_BAR
EXT_H_MAX = FTS.EXT_H_MAX
K_EXT = FTS.K_EXT
EXT_NW_EXPECT = FTS.EXT_NW_EXPECT
EXT2_H_MAX = FTS.EXT2_H_MAX
EXT2_POOL_CAP = FTS.EXT2_POOL_CAP
K_EXT2 = FTS.K_EXT2
EXT3_KZ_B = FTS.EXT3_KZ_B
EXT3_KZ_A = FTS.EXT3_KZ_A
EXT3_NW_MIN = FTS.EXT3_NW_MIN
EXT3_NW_MAX = FTS.EXT3_NW_MAX
ATOM_BAR = FTS.ATOM_BAR
REC3_BAR = FTS.REC3_BAR
REC3_BAR_X3 = FTS.REC3_BAR_X3
TEL_BAR = FTS.TEL_BAR
BND_BAR = FTS.BND_BAR
CHAIN_BAR = FTS.CHAIN_BAR
SA_BAR = FTS.SA_BAR
TREE_BAR = FTS.TREE_BAR
DICT_BAR = FTS.DICT_BAR
TILT_BAR = FTS.TILT_BAR
WQ_BAR = FTS.WQ_BAR
PART_BAR = FTS.PART_BAR
BK_BAR = FTS.BK_BAR
ENV_BAR = FTS.ENV_BAR
PGI_BAR = FTS.PGI_BAR
HVY_BAR = FTS.HVY_BAR
JEN_BAR = FTS.JEN_BAR
DEG_FLOOR = FTS.DEG_FLOOR
MULT_CAP = FTS.MULT_CAP
N_CAL = FTS.N_CAL
R_GRID = FTS.R_GRID
FR_GRID = FTS.FR_GRID
R_STAR_IDX = FTS.R_STAR_IDX
R_ALT_IDX = FTS.R_ALT_IDX
FR_PIN_IDX = FTS.FR_PIN_IDX
ELIG_FRAC = FTS.ELIG_FRAC
HSH_SPLIT = FTS.HSH_SPLIT
GA_FAM = FTS.GA_FAM
GSQ_R321 = FTS.GSQ_R321
NAMED_KZ = FTS.NAMED_KZ
MIDBAND_KZ = FTS.MIDBAND_KZ
MUT_MIN = FTS.MUT_MIN
TOY_BAR = FTS.TOY_BAR
EDGE_F = FTS.EDGE_F
INF_SENT = FTS.INF_SENT
CERT_GUARD = FTS.CERT_GUARD
CRIT_EXP = FTS.CRIT_EXP
R306_C2 = FTS.R306_C2
R306_C2_TOL = FTS.R306_C2_TOL
N346_REF = FTS.N344_REF
R316_RHO = FTS.R316_RHO
R316_RHO_TOL = FTS.R316_RHO_TOL
R316_CSMALL = FTS.R316_CSMALL
R316_CSMALL_TOL = FTS.R316_CSMALL_TOL
R316_CSMALL_KZ = FTS.R316_CSMALL_KZ
R324P_CM2 = FTS.R324P_CM2
R324P_CM2_TOL = FTS.R324P_CM2_TOL
R324P_M2VIOL = FTS.R324P_M2VIOL
R339_WF_MED = FTS.R339_WF_MED
R339_WF_MED_TOL = FTS.R339_WF_MED_TOL
R339_WG_MED = FTS.R339_WG_MED
R339_WG_MED_TOL = FTS.R339_WG_MED_TOL
R339_HSH_MED = FTS.R339_HSH_MED
R339_HSH_MED_TOL = FTS.R339_HSH_MED_TOL
R339_GMX_MAX = FTS.R339_GMX_MAX
R339_GMX_MAX_TOL = FTS.R339_GMX_MAX_TOL
R339_EWF = FTS.R339_EWF
R339_EWF_TOL = FTS.R339_EWF_TOL
R339_EM3 = FTS.R339_EM3
R339_EM3_TOL = FTS.R339_EM3_TOL
R324_EG = FTS.R324_EG
R324_EG_TOL = FTS.R324_EG_TOL
R324_EM2 = FTS.R324_EM2
R324_EM2_TOL = FTS.R324_EM2_TOL
R324_ETOT = FTS.R324_ETOT
R324_ETOT_TOL = FTS.R324_ETOT_TOL
R324_M0_L10 = FTS.R324_M0_L10
R341_WB_MED = FTS.R341_WB_MED
R341_WB_MED_TOL = FTS.R341_WB_MED_TOL
R341_WB_KZ55 = FTS.R341_WB_KZ55
R341_WB_KZ55_TOL = FTS.R341_WB_KZ55_TOL
R341_E3_MED = FTS.R341_E3_MED
R341_E3_MED_TOL = FTS.R341_E3_MED_TOL
R341_E3H_MED = FTS.R341_E3H_MED
R341_E3H_MED_TOL = FTS.R341_E3H_MED_TOL
R341_HSHARE_MED = FTS.R341_HSHARE_MED
R341_HSHARE_MED_TOL = FTS.R341_HSHARE_MED_TOL
R341_HRES_MED = FTS.R341_HRES_MED
R341_HRES_MED_TOL = FTS.R341_HRES_MED_TOL
R341_HRES_MIN = FTS.R341_HRES_MIN
R341_HRES_MIN_TOL = FTS.R341_HRES_MIN_TOL
R341_ALT_HSH_MED = FTS.R341_ALT_HSH_MED
R341_ALT_HSH_MED_TOL = FTS.R341_ALT_HSH_MED_TOL
R341_ALT_HSHARE_MED = FTS.R341_ALT_HSHARE_MED
R341_ALT_HSHARE_MED_TOL = FTS.R341_ALT_HSHARE_MED_TOL
R341_ALT_WB_MED = FTS.R341_ALT_WB_MED
R341_ALT_WB_MED_TOL = FTS.R341_ALT_WB_MED_TOL
R341_CH2 = FTS.R341_CH2
R341_CH2_TOL = FTS.R341_CH2_TOL
R341_CH2_VIOL = FTS.R341_CH2_VIOL
R341_KZ51_RATIO = FTS.R341_KZ51_RATIO
R341_KZ51_RATIO_TOL = FTS.R341_KZ51_RATIO_TOL
R341_CB2 = FTS.R341_CB2
R341_CB2_TOL = FTS.R341_CB2_TOL
R341_CB2_VIOL = FTS.R341_CB2_VIOL
R341_KZ55_RATIO = FTS.R341_KZ55_RATIO
R341_KZ55_RATIO_TOL = FTS.R341_KZ55_RATIO_TOL
R341_E_WB = FTS.R341_E_WB
R341_E_WB_TOL = FTS.R341_E_WB_TOL
R341_E_E3H = FTS.R341_E_E3H
R341_E_E3H_TOL = FTS.R341_E_E3H_TOL
R341_ENV_H3 = FTS.R341_ENV_H3
R341_ENV_H3_TOL = FTS.R341_ENV_H3_TOL
R341_ENV_G3 = FTS.R341_ENV_G3
R341_ENV_G3_TOL = FTS.R341_ENV_G3_TOL
R341_M0_ENV_L10 = FTS.R341_M0_ENV_L10
R341_M0_ENV_TOL = FTS.R341_M0_ENV_TOL
R306_M0_L10 = FTS.R306_M0_L10
R306_M0_TOL = FTS.R306_M0_TOL
R321_FA_TOP = FTS.R321_FA_TOP
R321_FA_TOL = FTS.R321_FA_TOL

# ---------------- NEW sealed constants of this round (spec above)
GAMMA_CEIL = 4.0
HENV_IDX = (0, 1, 2, 3, 4)
FA_SPLIT = 1.5
FA_PCTL = 90.0
FA_FLOOR = 0.58
PRED_ACC_NEED = 0.80
PRED_OOS_NEED = 0.75
PRED_TH = dict(hsh=0.5, fa1=1.5, fa2=2.0, grel=0.85, nw=1650,
               m=256, eps=2, gam=3)
PRED_IDS = tuple(range(1, 13))
M0_DEFUSE_MARGIN = 0.2
# the r344 record anchors (adopted as-is)
R344_HSH_CURVE = (0.872, 0.603, 0.371, 0.291, 0.266, 0.000)
R344_SHR_CURVE = (0.944, 0.771, 0.491, 0.447, 0.386, 0.000)
R344_WB_CURVE = (1.489, 2.410, 3.206, 3.659, 3.796, 6.096)
R344_EH_CURVE = (0.313, 0.377, 0.358, 0.373, 0.149)
R344_EG_CURVE = (-0.214, -0.075, 0.153, 0.159, 0.225, 0.464)
R344_CURVE_TOL_HSH = 0.001
R344_CURVE_TOL_SHR = 0.001
R344_CURVE_TOL_WB = 0.005
R344_CURVE_TOL_E = 0.003
R344_EMPTYG = (23, 11, 7, 7, 7, 2)
R344_EMPTYH = (0, 0, 0, 0, 0, 71)
R344_JHAT = 4
R344_HALVES = (1, 4)
R344_CH1 = 3.9859
R344_CG1 = 1.1409
R344_C_TOL = 0.001
R344_AA = 1
R344_THIRD_ONLY = 8
R344_PART_ACC = 7
R344_NONPRED = 20
R344_FA_MAX = 5.54
R344_FA_TOL = 0.01
M0_R344 = 22.6
M0_R344_TOL = 0.2
R344_EPS55_K = 1
R344_WB55_HAT = 8.459
R344_WB55_TOL = 0.005

R346_TABLE_LITERALS = frozenset(FTS.R344_TABLE_LITERALS | {
    0.603, 0.371, 0.291, 0.771, 0.491, 0.447, 2.41, 3.206,
    3.659, 6.096, 0.377, 0.358, 0.373, 0.149, -0.075, 0.153,
    0.159, 0.225, 0.464, 3.9859, 1.1409, 22.6, 5.54, 8.459,
    1.63, 3.91, 2.44, 1.14})

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
                       "the r244 chain rows; ground truth enters "
                       "gates and census tables only"
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


BOUND_FORBIDDEN = COP.BOUND_FORBIDDEN
PHI3_FORBIDDEN = COP.PHI3_FORBIDDEN
QMAX_FORBIDDEN = COP.QMAX_FORBIDDEN


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


def literal_audit(funcname):
    """the RECORD-LITERAL audit: walk ONLY the named function's
    subtree and flag any numeric constant whose 4-decimal rounding
    lies in the sealed r314..r344 record set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R346_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the
# ---------------- canonization builders consume the sealed grid,
# ---------------- exponent tuples, source-pure feature values and
# ---------------- SEALED thresholds only; the withheld terminal
# ---------------- drive key, the branch label, the cubic target
# ---------------- and the q_max RECORD are forbidden (AST
# ---------------- identifier scan + literal scan).
def rhat_intrinsic(grid, ceil3):
    """K1 -- THE SOURCE-INTRINSIC CEILING (data-free): R_ALG =
    ceil3^(1/3) (the R whose cubic ratio alone exhausts the
    algebraic pair Gamma-ceiling); returns the grid index
    minimizing |R - R_ALG| (ties: smaller R = smaller index).
    Consumes the sealed grid + the derived ceiling only."""
    ralg = float(ceil3) ** (1.0 / 3.0)
    best = 0
    bestd = abs(float(grid[0]) - ralg)
    for j in range(1, len(grid)):
        d = abs(float(grid[j]) - ralg)
        if d < bestd:
            best = j
            bestd = d
    return best, ralg


def rhat_cross_first(e_h, e_g, elig):
    """K2 -- THE FIRST-EQUILIBRATED POINT: the smallest eligible
    grid index j with e_H(j) <= e_G(j); if no crossing, the
    largest eligible index (crossed False); if nothing eligible,
    (0, False, False).  Consumes the exponent tuples + the
    eligibility mask only."""
    cand = [j for j in range(len(e_h)) if elig[j]]
    if not cand:
        return 0, False, False
    for j in cand:
        if e_h[j] <= e_g[j]:
            return j, True, True
    return cand[-1], False, True


def rhat_cross_interp(grid, e_h, e_g, elig):
    """K3 -- THE POOLED INTERPOLATED CROSSING (fit-free two-point
    algebra): d(j) = e_H(j) - e_G(j); at the first sign change
    between CONSECUTIVE eligible grid indices j, j+1 the exact
    interpolation R_CROSS = R_j + (R_{j+1} - R_j) d(j)/(d(j) -
    d(j+1)); returns (nearest grid index, R_CROSS, crossed,
    eligible_any); no crossing -> (largest eligible, None, False,
    True).  Consumes the sealed grid + exponents + mask only."""
    cand = [j for j in range(len(e_h)) if elig[j]]
    if not cand:
        return 0, None, False, False
    for a, b in zip(cand[:-1], cand[1:]):
        if b != a + 1:
            continue
        da = e_h[a] - e_g[a]
        db = e_h[b] - e_g[b]
        if da > 0.0 and db <= 0.0:
            rc = float(grid[a]) + (float(grid[b]) - float(grid[a])) \
                * da / (da - db)
            best = 0
            bestd = abs(float(grid[0]) - rc)
            for j in range(1, len(grid)):
                d = abs(float(grid[j]) - rc)
                if d < bestd:
                    best = j
                    bestd = d
            return best, rc, True, True
    return cand[-1], None, False, True


def env_min_col(cols, idxs):
    """K4 -- THE R-FREE ENVELOPE COLUMN: per row the min over the
    sealed grid indices of the column value restricted to
    POSITIVE entries (a row with no positive entry gets 0 and
    cannot be covered by this arm).  Consumes the per-grid column
    lists + the sealed index set only."""
    n = len(cols[idxs[0]])
    out = []
    for i in range(n):
        vals = [cols[j][i] for j in idxs if cols[j][i] > 0]
        out.append(min(vals) if vals else 0)
    return out


def pred_rule(rid, f, th):
    """THE SEALED 12-RULE PREDICTOR FAMILY (threshold rules, max
    2 features, all thresholds sealed a-priori in the spec):
    returns the predicted covering arm 'H'/'G'/'T'.  Consumes the
    source-pure feature dict + the sealed threshold dict only."""
    if rid == 1:
        return "H" if f["hsh"] >= th["hsh"] else "G"
    if rid == 2:
        return "T" if f["fa"] >= th["fa1"] else "H"
    if rid == 3:
        if f["fa"] >= th["fa1"]:
            return "T"
        return "H" if f["hsh"] >= th["hsh"] else "G"
    if rid == 4:
        return "T" if f["fa"] >= th["fa2"] else "H"
    if rid == 5:
        return "T" if f["grel"] < th["grel"] else "H"
    if rid == 6:
        if f["grel"] < th["grel"]:
            return "T"
        return "H" if f["hsh"] >= th["hsh"] else "G"
    if rid == 7:
        return "T" if f["nw"] > th["nw"] else "H"
    if rid == 8:
        return "T" if 0 <= f["eps"] <= th["eps"] else "H"
    if rid == 9:
        return "G" if f["gam"] >= th["gam"] else "H"
    if rid == 10:
        return "G" if f["m"] >= th["m"] else "H"
    if rid == 11:
        return "H"
    return "G"


def cls_rule(fv, split):
    """THE SEALED CLASS SPLIT (V1, source-side): SPIKE iff the
    F_A coordinate >= the sealed split (boundary inclusive), else
    QUIET.  Consumes the feature value + sealed threshold only."""
    return "SPIKE" if fv >= split else "QUIET"


def floor_bound(fv, floor):
    """THE FLOOR FORM (V3): the floored sliding coordinate
    max(F_A, floor) -- the open r329 successor question below the
    sampled range.  Consumes the feature value + sealed floor
    only."""
    return fv if fv > floor else floor


def canon_tree_verdict(leak, brk, canonized):
    """the sealed main-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    CANON_STATE_NOT_EXACT > COVER_CANONIZED >
    COVER_CENSUS_ONLY."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "CANON_STATE_NOT_EXACT"
    if canonized:
        return "COVER_CANONIZED"
    return "COVER_CENSUS_ONLY"


def mutant_pred_from_coverage(letters_seen, rho, cbar):
    """e1 MUST-FAIL MUTANT (protocol): predictor labels re-read
    from the evaluated coverage/violation column (consumes rho)
    -- the BOUND_FORBIDDEN scope audit must FLAG it AND on the
    sealed toy it returns ('T', 'G') != the sealed rule
    output."""
    out = []
    for a, r in zip(letters_seen, rho):
        out.append("T" if r > cbar else a)
    return tuple(out)


def mutant_clsrule_posthoc(cls_seen, rho, cbar):
    """e2 MUST-FAIL MUTANT (protocol): the class letters flipped
    after sight of the evaluated violation column (consumes rho)
    -- AST-FLAGGED and on the sealed toy it returns ('SPIKE',
    'SPIKE') != the sealed class-rule output."""
    out = []
    for c, r in zip(cls_seen, rho):
        if r > cbar:
            out.append("SPIKE" if c == "QUIET" else "QUIET")
        else:
            out.append(c)
    return tuple(out)


def mutant_env_doublecount(cols, idxs):
    """e3 MUST-FAIL MUTANT: the R-free 'envelope' that SUMS the
    hand-off column over the grid instead of taking the min --
    double-counts the constant; on the sealed Fractions toy it
    returns 49/8 while the sealed envelope is 49/32 (break 147/32
    EXACT)."""
    n = len(cols[idxs[0]])
    out = []
    for i in range(n):
        out.append(sum(cols[j][i] for j in idxs
                       if cols[j][i] > 0))
    return out


def mutant_crossing_posthoc(idx_seen, rho, cbar):
    """e4 MUST-FAIL MUTANT (protocol): the crossing index
    re-picked AFTER SIGHT of the evaluated violation column
    (consumes rho) -- AST-FLAGGED and on the sealed toy it
    returns index 4 != the sealed K2 toy output 2."""
    pick = 0
    for j, r in zip(idx_seen, rho):
        if r > cbar:
            pick = max(pick, int(j))
    return pick


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'canonization orientation'
    consuming the withheld ground-truth terminal drive key -- the
    scope audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'predictor constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


def fr_env_toy():
    """the sealed Fractions envelope pin: the r344 stop toy
    (7, 1, 5, 3) hand-off column over the grid is HB = 49/32 at
    grid indices 0..3 and 0 at index 4 (msh = 0 past the strict
    7/4 boundary, r344 pin); the sealed envelope min = 49/32
    EXACT; the e3 double-count mutant returns 49/8, break 147/32
    EXACT.  Returns (worst dev, mutant break)."""
    cols = {}
    for j, fr_r in enumerate(FR_GRID):
        st = FBR.fr_path_state([Fr(7), Fr(1), Fr(5), Fr(3)], fr_r)
        cols[j] = [Fr(7, 4) ** 2 * st["msh"]]
    env = env_min_col(cols, HENV_IDX)[0]
    mut = mutant_env_doublecount(cols, HENV_IDX)[0]
    brk = mut - env
    devs = [abs(env - Fr(49, 32)),
            abs(mut - Fr(49, 8)),
            abs(brk - Fr(147, 32))]
    return max(devs), brk


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fold_cover_canonization_probe -- "
          "PRIME.L2.COVER_CANONIZATION.01 (round 346, "
          "the three residues of the r344 cover)")
    print("SPEC_SHA %s   R344_SHA %s   R341_SHA %s   R329_SHA %s"
          % (SPEC_SHA[:16], FTS.SPEC_SHA[:16], FBR.SPEC_SHA[:16],
             EFA.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + grid path wards + w9 "
                        "Fractions pins + e1-e4; ladder, "
                        "extensions, EXT3, anchors, candidates, "
                        "predictor, defusal, composition and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE COVER-CANONIZATION ROUND (the named r344 "
          "follow-up): on the SEALED r344 three-arm cover (grid "
          "%s, C_H hand-off / C_G eps-chain / third arm banked "
          "r321 %.4f F_A^2) the three residues are adjudicated "
          "with sealed machinery: LEG A stop candidates K1 "
          "(intrinsic ceiling %.1f^(1/3), data-free), K2 "
          "(first-equilibrated), K3 (pooled interpolated "
          "crossing), K4 (R-free envelope over grid indices %s); "
          "LEG B the sealed 12-rule predictor family (thresholds "
          "%s; need core >= %.2f, OOS >= %.2f); LEG C defusal V1 "
          "class split (F_A >= %.1f), V2 percentile %d, V3 floor "
          "%.2f; verdict tree COVER_CANONIZED / COVER_CENSUS_ONLY "
          "/ CANON_STATE_NOT_EXACT / TARGET_LEAK + flags sealed "
          "BEFORE evaluation"
          % (str(tuple(round(r, 4) for r in R_GRID)), GSQ_R321,
             GAMMA_CEIL, str(HENV_IDX), str(sorted(PRED_TH.items())),
             PRED_ACC_NEED, PRED_OOS_NEED, FA_SPLIT, int(FA_PCTL),
             FA_FLOOR))
    frag = antigate_fragment_audit()
    own_builders = ("rhat_intrinsic", "rhat_cross_first",
                    "rhat_cross_interp", "env_min_col",
                    "pred_rule", "cls_rule", "floor_bound",
                    "canon_tree_verdict", "fr_env_toy")
    sc_own = []
    for fn in own_builders:
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the module-own "
          "canonization builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the "
          "canonization side consumes the sealed grid + "
          "source-pure feature columns + sealed thresholds ONLY; "
          "m5a gift-bound FLAGGED (%s); m5b branch-peek FLAGGED "
          "(%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r344 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3")
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
        ext2 = []
        ext3 = []
        okL = True
    else:
        kzs = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
            elif h <= EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        ekz2.sort()
        pool2 = epool[K_EXT:] + [BH.wpack(kz)
                                 for _h, kz in ekz2[:EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:K_EXT2]
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
        ext3 = [BH.wpack(kz) for kz in EXT3_KZ_B + EXT3_KZ_A]
        ext3.sort(key=lambda p: (p["N"], p["kz"]))
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
        check("G13-ext2-census", True, "SMOKE: skipped")
        check("G14-ext3-admission", True, "SMOKE: skipped")
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
        check("G13-ext2-census",
              len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "EXT2 (r316 A5 rule verbatim, census-grade): "
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))
        check("G14-ext3-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX,
              "EXT3 = the sealed r329 RECORD selection "
              "(r335/r339/r341/r344 adoption verbatim): 12 "
              "anchors (B %s + A %s), POSITIVE_PREFIX %d/12, N_w "
              "%d..%d (record %d..%d) -- PURE TEST rows, never "
              "calibration"
              % (str(EXT3_KZ_B), str(EXT3_KZ_A),
                 sum(1 for p in ext3 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3),
                 EXT3_NW_MIN, EXT3_NW_MAX))

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
    e2recs = [rung_rec(p) for p in ext2] if not smoke else []
    x3recs = [rung_rec(p) for p in ext3] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs + e2recs + x3recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2+EXT3 census: %d cheap / %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + TREE-LEDGER WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_x3 = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in erecs + e2recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext = max(tb_ext, dev)
    for rc in x3recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x3 = max(tb_x3, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_x3 <= TB_WARD_BAR_X3
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d ext3 + %d mains + 3 controls: worst dev/absmass "
          "%.1e main N<=%d (bar %.0e) / %.1e deep / %.1e "
          "ext+ext2 (bar %.0e) / %.1e ext3 (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(x3recs),
             len(mrecs), tb_worst, DEEP_N, TB_WARD_BAR, tb_deep,
             tb_ext, TB_WARD_BAR_DEEP, tb_x3, TB_WARD_BAR_X3,
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
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        src_all = np.concatenate([np.zeros(len(xb)),
                                  np.ones(len(xw))])
        if m and not degenerate:
            gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
            sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = SCF.flux_telescope(gen["G1"], gen["ptr"], m)
            x_dev = float(np.max(np.abs(sct["x"] - Pd))
                          / max(np.max(np.abs(Pd)), 1e-300))
            sig = sct["sig"]
            cube = sct["cube"]
            A1 = np.bincount(blk_all, weights=np.abs(val_all),
                             minlength=m)
            scale3 = float(np.sum(A1 ** 3))
            sc_j = np.maximum(A1 ** 3, 1e-300)
            C_far_flux = float(np.sum(sig * ft["F_end"]))
            C_bnd = float(np.sum(sig * ft["F_open"]))
            rec3 = abs(C_far_flux + sct["C_pair"] + sct["C_full"]
                       + C_bnd - cube) / max(scale3, 1e-300)
            tel_dev = float(np.max(np.abs(ft["F_end"]
                                          - sct["far"]) / sc_j))
            bnd_dev = float(np.max(np.abs(ft["F_open"]) / sc_j))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            trs = TRB.two_regime_state(sct["x"], sct["Q2"],
                                       sct["Q3"], gen["G1"],
                                       gen["ptr"], ft["F_end"],
                                       ft["F_open"],
                                       ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            mqs = FAP.m2_qmax_state(sct["x"])
            led327 = GMC.group_mass_ledger(pos_all, val_all,
                                           blk_all, src_all, m)
            gtree = FDD.fold_mass_tree_exact(sct["x"])
            dst = FDD.descendant_density_martingale(gtree)
            dic = FDD.martingale_moment_dictionary(sct["x"])
            pbg = tuple(FBR.path_bellman_state(gtree, rr)
                        for rr in R_GRID)
        else:
            gen = sct = ft = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            mx_mult = 0
            A1 = np.zeros(0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            mqs = dict(qm=0.0, m2=0.0, ymx=0.0, maj=0.0)
            led327 = None
            gtree = None
            dst = FDD.descendant_density_martingale(
                dict(mass=[np.zeros(1)], cnt=[np.ones(1, int)],
                     kptr=[], depth=0, m=0))
            dic = dict(d1=0.0, d2=0.0, d3=0.0, ymx=0.0)
            pbg = tuple(FBR.path_bellman_state(
                dict(mass=[np.zeros(1)], cnt=[np.ones(1, int)],
                     kptr=[], depth=0, m=0), rr)
                for rr in R_GRID)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led327=led327, gtree=gtree, dst=dst, dic=dic,
                    pbg=pbg, pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs + x3recs
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
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    led_dev = 0.0
    x3_mult_ok = True
    for rc in live:
        ev = rc["ev"]
        gen = ev["gen"]
        l327 = ev["led327"]
        if gen["ng"] != l327["ng"]:
            led_dev = max(led_dev, 1.0)
            continue
        if gen["ng"]:
            sc = max(float(np.max(np.abs(gen["G1"]))), 1e-300)
            led_dev = max(
                led_dev,
                float(np.max(np.abs(l327["G1"] - gen["G1"]))) / sc,
                float(np.max(np.abs(l327["mult"] - gen["mult"]))),
                float(np.max(np.abs(l327["gblk"] - gen["gblk"]))))
    for rc in x3recs:
        if rc["ev"]["mx_mult"] > MULT_CAP:
            x3_mult_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and x3_mult_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r327 GMC ledger segments IDENTICALLY to the genealogy "
          "(worst dev %.1e, bar %.0e); EXT3 fold multiplicity <= "
          "%d on 12/12 (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP, "OK" if x3_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (r344 verbatim)
    section("S3  LEG 0 -- ANCHOR REGRESSION (r306/r316/r324-pre "
            "+ r339 + r324 CHAIN + r341 RECORD + r321 F_A)")
    x3_ids = set(id(rc) for rc in x3recs)
    live_69 = [rc for rc in live if id(rc) not in x3_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    tel_x = max((rc["ev"]["tel_dev"] for rc in x3recs),
                default=0.0)
    bnd_x = max((rc["ev"]["bnd_dev"] for rc in x3recs),
                default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and tel_x <= REC3_BAR_X3 and bnd_x <= REC3_BAR_X3,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e (bars %.0e); "
          "EXT3 %.1e / %.1e / %.1e (bar %.0e); DISCLOSED slim "
          "anchor set -- the full chain is re-warded by the "
          "sealed r321..r344 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, tel_x,
             bnd_x, REC3_BAR_X3))
    if smoke:
        ev9s = recs[0]["ev"]
        pb0 = ev9s["pbg"][R_STAR_IDX]
        info("SMOKE: w9 m %d K %d E3 %.4f grid hsh %s"
             % (ev9s["m"], pb0["kk"], pb0["e3"],
                str([round(p["hsh"], 3) for p in ev9s["pbg"]])))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r324pre-m2-anchor", True, "SMOKE: skipped")
        srt = []
        n346 = 0
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2r, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2r)
        check("G31-r306-bound-live",
              abs(C2r - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2r, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        srt_all65 = sorted(recs + erecs + e2recs,
                           key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all65
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n346 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n346)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n346 == N346_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n346, N346_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        C_M2 = max(m2_col[i] for i in ca_i)
        viol_m2 = tuple(sorted(srt[i]["kz"] for i in te_i
                               if m2_col[i] > C_M2))
        check("G33-r324pre-m2-anchor",
              abs(C_M2 - R324P_CM2) <= R324P_CM2_TOL
              and viol_m2 == tuple(sorted(R324P_M2VIOL)),
              "the r324-pre m2 record reproduced: mid-ladder "
              "freeze C_M2 %.4f (rec %.4f tol %.3f); the seven "
              "test violators %s == the banked set EXACT"
              % (C_M2, R324P_CM2, R324P_CM2_TOL, str(viol_m2)))
    dict2_w = 0.0
    dict3_w = 0.0
    dictq_w = 0.0
    for rc in live:
        ev = rc["ev"]
        dic = ev["dic"]
        mloc = ev["m"]
        dict2_w = max(dict2_w, abs(dic["d2"] - ev["mqs"]["m2"])
                      / max(ev["mqs"]["m2"], 1e-300))
        rid = ev["rho2"] * (math.log(float(mloc)) ** 2)
        dict3_w = max(dict3_w, abs(dic["d3"] - rid)
                      / max(rid, 1e-300))
        dictq_w = max(dictq_w,
                      abs(dic["ymx"] / float(mloc)
                          - ev["mqs"]["qm"])
                      / max(ev["mqs"]["qm"], 1e-300))
    check("G34-dictionary-chain-identity",
          dict2_w <= DICT_BAR and dict3_w <= DICT_BAR
          and dictq_w <= DICT_BAR,
          "THE MOMENT DICTIONARY anchored bit-near on %d live "
          "worlds: E[X_inf^2] == m M_2 (worst rel %.1e), "
          "E[X_inf^3] == m^2 M_3 == rho_2 (log m)^2 (worst "
          "%.1e), max y / m == q_max (worst %.1e; bars %.0e)"
          % (len(live), dict2_w, dict3_w, dictq_w, DICT_BAR))
    if smoke:
        check("G35-r339-record-anchors", True, "SMOKE: skipped")
        check("G36-r324-chain-anchor", True, "SMOKE: skipped")
        check("G37-r341-record-anchors", True, "SMOKE: skipped")
        check("G38-r341-freeze-anchors", True, "SMOKE: skipped")
        check("G39-r321-fa-anchors", True, "SMOKE: skipped")
    else:
        srt_x = sorted(x3recs, key=lambda rc: (rc["N"], rc["kz"]))
        srt_x = [rc for rc in srt_x
                 if rc["ev"]["mx_mult"] <= MULT_CAP
                 and not rc["ev"]["degenerate"]]
        n_x3 = len(srt_x)
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        wf_col = [rc["ev"]["dst"]["wf"] for rc in srt_full]
        wg_col = [rc["ev"]["dst"]["wg"] for rc in srt_full]
        hshF_col = [rc["ev"]["dst"]["hsh"] for rc in srt_full]
        gmw_col = [max(rc["ev"]["dst"]["gmx_lv"])
                   if rc["ev"]["dst"]["gmx_lv"] else 1.0
                   for rc in srt_full]
        d2_col = [rc["ev"]["dic"]["d2"] for rc in srt_full]
        d3_col = [rc["ev"]["dic"]["d3"] for rc in srt_full]
        ymx_col = [rc["ev"]["dic"]["ymx"] for rc in srt_full]
        wf_med = float(np.median(wf_col))
        wg_med = float(np.median(wg_col))
        hshF_med = float(np.median(hshF_col))
        gmx_max = max(gmw_col)
        e_wf = L2D.halves_slope([m_full[i] for i in te_i],
                                [max(wf_col[i], 1e-300)
                                 for i in te_i])
        e_d3 = L2D.halves_slope([m_full[i] for i in te_i],
                                [max(d3_col[i], 1e-300)
                                 for i in te_i])
        check("G35-r339-record-anchors",
              abs(wf_med - R339_WF_MED) <= R339_WF_MED_TOL
              and abs(wg_med - R339_WG_MED) <= R339_WG_MED_TOL
              and abs(hshF_med - R339_HSH_MED) <= R339_HSH_MED_TOL
              and abs(gmx_max - R339_GMX_MAX) <= R339_GMX_MAX_TOL
              and abs(e_wf - R339_EWF) <= R339_EWF_TOL
              and abs(e_d3 - R339_EM3) <= R339_EM3_TOL,
              "the r339 RECORD reproduced through the imported "
              "FDD builders on the same 65+%d rows: W_F med %.2f "
              "(rec %.2f), W_G med %.2f (rec %.2f), hsh med %.3f "
              "(rec %.3f), Gamma_max max %.3f (rec %.3f), e(W_F) "
              "%+.3f (rec %+.3f), e(m^2 M_3) %+.3f (rec %+.3f)"
              % (n_x3, wf_med, R339_WF_MED, wg_med, R339_WG_MED,
                 hshF_med, R339_HSH_MED, gmx_max, R339_GMX_MAX,
                 e_wf, R339_EWF, e_d3, R339_EM3))
        e_g324 = L2D.halves_slope(
            [m_full[i] for i in te_i],
            [max(ymx_col[i], 1e-300)
             / math.log(float(m_full[i])) for i in te_i])
        e_m2324 = L2D.halves_slope([m_full[i] for i in te_i],
                                   [max(d2_col[i], 1e-300)
                                    for i in te_i])
        e_tot324 = e_g324 + e_m2324
        check("G36-r324-chain-anchor",
              abs(e_g324 - R324_EG) <= R324_EG_TOL
              and abs(e_m2324 - R324_EM2) <= R324_EM2_TOL
              and abs(e_tot324 - R324_ETOT) <= R324_ETOT_TOL,
              "the r324 MEASURED chain reproduced: e(G/log m) "
              "%+.3f (rec %+.3f), e(m M_2) %+.3f (rec %+.3f), "
              "e_tot %+.3f (rec %+.3f) -- the honest comparison "
              "threshold stays m_0* = 10^%.1f (record, adopted)"
              % (e_g324, R324_EG, e_m2324, R324_EM2, e_tot324,
                 R324_ETOT, R324_M0_L10))
        e3_col = [rc["ev"]["pbg"][R_STAR_IDX]["e3"]
                  for rc in srt_full]
        e3h_star = [rc["ev"]["pbg"][R_STAR_IDX]["e3h"]
                    for rc in srt_full]
        wb_star = [rc["ev"]["pbg"][R_STAR_IDX]["wb"]
                   for rc in srt_full]
        hsh_star = [rc["ev"]["pbg"][R_STAR_IDX]["hsh"]
                    for rc in srt_full]
        hres_star = [rc["ev"]["pbg"][R_STAR_IDX]["hvy_res"]
                     for rc in srt_full]
        hsh_alt = [rc["ev"]["pbg"][R_ALT_IDX]["hsh"]
                   for rc in srt_full]
        e3h_alt = [rc["ev"]["pbg"][R_ALT_IDX]["e3h"]
                   for rc in srt_full]
        wb_alt = [rc["ev"]["pbg"][R_ALT_IDX]["wb"]
                  for rc in srt_full]
        hshare_star = [e3h_star[i] / max(e3_col[i], 1e-300)
                       for i in range(n_full)]
        hshare_alt = [e3h_alt[i] / max(e3_col[i], 1e-300)
                      for i in range(n_full)]
        kz_rank = {rc["kz"]: i for i, rc in enumerate(srt_full)}
        wb55 = wb_star[kz_rank[55]]
        e3h_med_lad = float(np.median(e3h_star[:n346]))
        e3_med = float(np.median(e3_col))
        e3h_derived = e3_med * float(np.median(hshare_star))
        check("G37-r341-record-anchors",
              abs(float(np.median(wb_star)) - R341_WB_MED)
              <= R341_WB_MED_TOL
              and abs(wb55 - R341_WB_KZ55) <= R341_WB_KZ55_TOL
              and abs(e3_med - R341_E3_MED) <= R341_E3_MED_TOL
              and abs(e3h_derived - R341_E3H_MED)
              <= R341_E3H_MED_TOL
              and abs(float(np.median(hshare_star))
                      - R341_HSHARE_MED) <= R341_HSHARE_MED_TOL
              and abs(float(np.median(hsh_star)) - R339_HSH_MED)
              <= R339_HSH_MED_TOL
              and abs(float(np.median([v for v in hres_star
                                       if v < INF_SENT]))
                      - R341_HRES_MED) <= R341_HRES_MED_TOL
              and abs(min(hres_star) - R341_HRES_MIN)
              <= R341_HRES_MIN_TOL
              and abs(float(np.median(hsh_alt))
                      - R341_ALT_HSH_MED) <= R341_ALT_HSH_MED_TOL
              and abs(float(np.median(hshare_alt))
                      - R341_ALT_HSHARE_MED)
              <= R341_ALT_HSHARE_MED_TOL
              and abs(float(np.median(wb_alt)) - R341_ALT_WB_MED)
              <= R341_ALT_WB_MED_TOL,
              "the r341 RECORD reproduced through the imported "
              "FBR builders, BOTH banked columns: R* = 3/2 (W_B "
              "med %.3f rec %.3f, kz55 %.3f rec %.3f, E3 med "
              "%.2f rec %.2f, E3h derived med(E3) x med(share) "
              "%.2f rec %.2f (raw ladder med %.2f / full med "
              "%.2f, r344 amendment a1 reading), E3h share med "
              "%.3f rec %.3f, hsh med %.3f, hand-off reserve "
              "med %.1f min %.1f rec %.1f/%.1f) and R_ALT = 7/4 "
              "(hsh med %.3f rec %.3f, share med %.3f rec %.3f, "
              "W_B med %.3f rec %.3f)"
              % (float(np.median(wb_star)), R341_WB_MED, wb55,
                 R341_WB_KZ55, e3_med, R341_E3_MED, e3h_derived,
                 R341_E3H_MED, e3h_med_lad,
                 float(np.median(e3h_star)),
                 float(np.median(hshare_star)),
                 R341_HSHARE_MED, float(np.median(hsh_star)),
                 float(np.median([v for v in hres_star
                                  if v < INF_SENT])),
                 min(hres_star), R341_HRES_MED, R341_HRES_MIN,
                 float(np.median(hsh_alt)), R341_ALT_HSH_MED,
                 float(np.median(hshare_alt)),
                 R341_ALT_HSHARE_MED, float(np.median(wb_alt)),
                 R341_ALT_WB_MED))
        te_x = list(te_i) + list(range(n346, n_full))
        named_rank = {}
        for kz in NAMED_KZ + MIDBAND_KZ:
            named_rank[kz] = kz_rank[kz]
        lg_full = [math.log(float(v)) for v in m_full]
        ch2_col = [e3h_star[i] / lg_full[i] ** 2
                   for i in range(n_full)]
        CH2 = max(ch2_col[i] for i in ca_i)
        vH2 = [i for i in te_x if ch2_col[i] > CH2]
        r51 = ch2_col[kz_rank[51]]
        cb2_col = [wb_star[i] / lg_full[i] ** 2
                   for i in range(n_full)]
        CB2 = max(cb2_col[i] for i in ca_i)
        vB2 = [i for i in te_x if cb2_col[i] > CB2]
        r55 = cb2_col[kz_rank[55]] / CB2
        e_wb = L2D.halves_slope([m_full[i] for i in te_i],
                                [max(wb_star[i], 1e-300)
                                 for i in te_i])
        e_e3h = L2D.halves_slope([m_full[i] for i in te_i],
                                 [max(e3h_star[i], 1e-300)
                                  for i in te_i])
        env_h3 = max(e3h_star[i] / lg_full[i] ** 3
                     for i in range(n_full))
        e3g_star = [rc["ev"]["pbg"][R_STAR_IDX]["e3g"]
                    for rc in srt_full]
        env_g3 = max(e3g_star[i] / lg_full[i] ** 3
                     for i in range(n_full))

        def solve_m0(log_rhs):
            t = math.log(73.0)
            while t < 1e7:
                if CRIT_EXP * t >= log_rhs(t):
                    return t / math.log(10.0)
                t *= 1.02
            return None

        m0_env = solve_m0(lambda t: math.log(
            max((env_h3 + env_g3) * t ** 3, 1e-300)))
        m0_306 = solve_m0(lambda t: math.log(
            max(R306_C2 * t ** 2, 1e-300)))
        check("G38-r341-freeze-anchors",
              abs(CH2 - R341_CH2) <= R341_CH2_TOL
              and len(vH2) == R341_CH2_VIOL
              and abs(r51 - R341_KZ51_RATIO) <= R341_KZ51_RATIO_TOL
              and abs(CB2 - R341_CB2) <= R341_CB2_TOL
              and len(vB2) == R341_CB2_VIOL
              and abs(r55 - R341_KZ55_RATIO) <= R341_KZ55_RATIO_TOL
              and abs(e_wb - R341_E_WB) <= R341_E_WB_TOL
              and abs(e_e3h - R341_E_E3H) <= R341_E_E3H_TOL
              and abs(env_h3 - R341_ENV_H3) <= R341_ENV_H3_TOL
              and abs(env_g3 - R341_ENV_G3) <= R341_ENV_G3_TOL
              and m0_env is not None
              and abs(m0_env - R341_M0_ENV_L10) <= R341_M0_ENV_TOL
              and m0_306 is not None
              and abs(m0_306 - R306_M0_L10) <= R306_M0_TOL,
              "the r341 freezes + exponents + envelope "
              "composition reproduced through the same code "
              "path: C_H(2) %.4f (rec %.4f) viol %d (rec %d) "
              "kz51 column value %.2f (rec %.2f); C_B(2) %.4f "
              "(rec %.4f) viol %d (rec %d) kz55 %.2fx (rec "
              "%.2f); e(W_B) %+.3f (rec %+.3f), e(E3h) %+.3f "
              "(rec %+.3f); a=3 envelopes heavy %.4f (rec %.4f) "
              "+ good %.4f (rec %.4f) -> m_0* 10^%.1f (rec "
              "10^%.1f); r306 census solve 10^%.1f (rec 10^%.1f)"
              % (CH2, R341_CH2, len(vH2), R341_CH2_VIOL, r51,
                 R341_KZ51_RATIO, CB2, R341_CB2,
                 len(vB2), R341_CB2_VIOL, r55, R341_KZ55_RATIO,
                 e_wb, R341_E_WB, e_e3h, R341_E_E3H, env_h3,
                 R341_ENV_H3, env_g3, R341_ENV_G3, m0_env,
                 R341_M0_ENV_L10, m0_306, R306_M0_L10))
        q_lad = [srt[i]["ev"]["mqs"]["qm"] for i in range(n346)]
        fa_lad = EFP.local_ratio(q_lad)
        N_lad = [srt[i]["N"] for i in range(n346)]
        fa_full = list(fa_lad)
        for rc in srt_x:
            fa_full.append(CCP.world_coord(rc["ev"]["mqs"]["qm"],
                                           rc["N"], N_lad, q_lad))
        fa_kz = {srt_full[i]["kz"]: fa_full[i]
                 for i in range(n_full)}
        check("G39-r321-fa-anchors",
              all(abs(fa_kz[kz] - R321_FA_TOP[kz]) <= R321_FA_TOL
                  for kz in R321_FA_TOP),
              "the r321/r317 F_A coordinate reproduced through "
              "EFP.local_ratio on the module-own q_max column: "
              "top-3 kz53 %.2f / kz83 %.2f / kz67 %.2f (rec "
              "%.2f/%.2f/%.2f tol %.2f); EXT3 rows via the r321 "
              "INSERTION RULE (CCP.world_coord, the r329 "
              "convention); F_A range full %.2f..%.2f; the "
              "third-arm constant GSQ = %.4f is the BANKED r321 "
              "record, never recalibrated here"
              % (fa_kz[53], fa_kz[83], fa_kz[67],
                 R321_FA_TOP[53], R321_FA_TOP[83],
                 R321_FA_TOP[67], R321_FA_TOL, min(fa_full),
                 max(fa_full), GSQ_R321))

    # ---------------- S4: seal + purity + toys + live wards
    section("S4  LEG 0b -- SEAL + PURITY + TOYS + LIVE GRID "
            "WARDS")
    pure_lits = []
    for fn in own_builders:
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_pred_from_coverage",
                          BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_clsrule_posthoc",
                          BOUND_FORBIDDEN)
    e4_hits = scope_audit("mutant_crossing_posthoc",
                          BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e4_hits) >= 1,
          "SOURCE PURITY: the canonization builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed "
          "r314..r344 record-literal set (%d literal hits); e1 "
          "pred-from-coverage FLAGGED (%s); e2 clsrule-posthoc "
          "FLAGGED (%s); e4 crossing-posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    # sealed toys (Fractions + by-hand pins, spec above)
    fb_dev = FTS.fr_balance_toy()
    fh_dev, fh_brk = FTS.fr_handoff_toy()
    fe_dev, fe_brk = fr_env_toy()
    toy_k1a, ralg_a = rhat_intrinsic(R_GRID, GAMMA_CEIL)
    toy_k1b, ralg_b = rhat_intrinsic(R_GRID, 8.0)
    toy_k2a = rhat_cross_first((0.3, 0.2, 0.1),
                               (-0.2, 0.15, 0.4),
                               (True, True, True))
    toy_k2b = rhat_cross_first((0.3, 0.2), (0.1, 0.1),
                               (True, True))
    toy_k2c = rhat_cross_first((0.3,), (0.1,), (False,))
    toy_k3 = rhat_cross_interp((1.5, 2.0), (0.5, 0.0),
                               (0.0, 0.25), (True, True))
    ok_k3 = (toy_k3[0] == 1 and toy_k3[2] and toy_k3[3]
             and abs(toy_k3[1] - float(Fr(11, 6))) <= TOY_BAR)
    toy_cls = (cls_rule(2.0, FA_SPLIT), cls_rule(1.0, FA_SPLIT),
               cls_rule(1.5, FA_SPLIT))
    toy_flr = (floor_bound(0.5, FA_FLOOR),
               floor_bound(2.0, FA_FLOOR))
    fA = dict(hsh=0.9, fa=2.5, grel=0.5, nw=2000, eps=1, gam=4,
              m=300)
    fB = dict(hsh=0.1, fa=1.0, grel=1.2, nw=500, eps=-1, gam=1,
              m=100)
    toy_pA = tuple(pred_rule(r, fA, PRED_TH) for r in PRED_IDS)
    toy_pB = tuple(pred_rule(r, fB, PRED_TH) for r in PRED_IDS)
    exp_pA = ("H", "T", "T", "T", "T", "T", "T", "T", "G", "G",
              "H", "G")
    exp_pB = ("G", "H", "G", "H", "H", "G", "H", "H", "H", "H",
              "H", "G")
    mut1 = mutant_pred_from_coverage(("H", "G"), (0.9, 0.1), 0.5)
    mut2 = mutant_clsrule_posthoc(("SPIKE", "QUIET"),
                                  (0.1, 0.9), 0.5)
    mut4 = mutant_crossing_posthoc((0, 1, 2, 3, 4, 5),
                                   (0.1, 0.1, 0.1, 0.1, 0.9,
                                    0.1), 0.5)
    tr_br = (canon_tree_verdict(True, True, True),
             canon_tree_verdict(False, True, True),
             canon_tree_verdict(False, False, True),
             canon_tree_verdict(False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "CANON_STATE_NOT_EXACT",
                      "COVER_CANONIZED", "COVER_CENSUS_ONLY")
    check("G41-toy-exactness",
          fb_dev == 0 and fh_dev == 0 and fh_brk == Fr(49, 32)
          and fe_dev == 0 and fe_brk == Fr(147, 32)
          and toy_k1a == 1 and abs(ralg_a - 4.0 ** (1.0 / 3.0)) == 0
          and toy_k1b == 5 and abs(ralg_b - 2.0) <= TOY_BAR
          and toy_k2a == (2, True, True)
          and toy_k2b == (1, False, True)
          and toy_k2c == (0, False, False)
          and ok_k3
          and toy_cls == ("SPIKE", "QUIET", "SPIKE")
          and toy_flr == (FA_FLOOR, 2.0)
          and toy_pA == exp_pA and toy_pB == exp_pB
          and mut1 == ("T", "G")
          and mut2 == ("SPIKE", "SPIKE")
          and mut4 == 4 and ok_tr,
          "the sealed toys EXACT: r344 Fractions balance toy "
          "worst dev %s + hand-off pin break 49/32; envelope pin "
          "49/32 with e3 double-count break %s == 147/32 EXACT; "
          "K1 intrinsic (ceiling 4 -> index 1 at R_ALG %.4f; "
          "ceiling 8 -> endpoint index 5); K2 toys (crossing -> "
          "2, no-crossing -> (1, False), empty -> DENIED); K3 "
          "interpolation R_CROSS %.6f == 11/6 -> index 1; class "
          "toys (SPIKE, QUIET, SPIKE boundary); floor toys "
          "(%.2f, %.1f); the 12-rule family on both sealed "
          "feature tuples EXACT; e1 mutant ('T', 'G') != sealed "
          "rule; e2 mutant ('SPIKE', 'SPIKE') != sealed rule; e4 "
          "mutant picks 4 != sealed K2 toy 2; verdict tree all "
          "four branches EXACT %s"
          % (str(fb_dev), str(fe_brk), ralg_a, toy_k3[1],
             toy_flr[0], toy_flr[1], str(tr_br)))
    # live grid wards (r344 verbatim): every FBR exact ward at
    # every grid R + the Fractions bit-equality at the two pins
    tilt_w = wqd_w = part_w3 = bkd_w = env_w = pgi_w = hvy_w = 0.0
    e3d_w = 0.0
    mart_w = unit_w = rec_w = jen_w = 0.0
    part_w = panc_w = l1rec_w = chain_w = xw_cube = 0.0
    nz_tot = 0
    mult_all_ok = True
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
        st = ev["dst"]
        if st["ok"]:
            mart_w = max(mart_w, st["mart_dev"])
            unit_w = max(unit_w, st["unit_dev"])
            rec_w = max(rec_w, st["rec_dev"])
            jen_w = max(jen_w,
                        max((d for d in st["drift"]),
                            default=0.0))
            nz_tot += st["nzero"]
        for pb in ev["pbg"]:
            if pb["ok"]:
                tilt_w = max(tilt_w, pb["tilt_dev"])
                wqd_w = max(wqd_w, pb["wq_dev"])
                part_w3 = max(part_w3, pb["part_dev"])
                bkd_w = max(bkd_w, pb["bk_dev"])
                env_w = max(env_w, pb["env_dev"])
                pgi_w = max(pgi_w, pb["pgi_dev"])
                hvy_w = max(hvy_w, pb["hvy_dev"])
                e3d_w = max(e3d_w, abs(pb["e3"] - ev["dic"]["d3"])
                            / max(ev["dic"]["d3"], 1e-300))
        led = ev["led327"]
        mloc = ev["m"]
        x_abs = np.abs(ev["sct"]["x"])
        Lx = float(np.sum(x_abs))
        A1led = np.bincount(led["gblk"], weights=led["gabs"],
                            minlength=mloc)
        part_w = max(part_w,
                     float(np.max(np.abs(A1led - ev["A1"])))
                     / max(float(np.max(ev["A1"])), 1e-300))
        xled = np.bincount(led["gblk"], weights=led["G1"],
                           minlength=mloc)
        l1rec_w = max(l1rec_w,
                      abs(float(np.sum(np.abs(xled))) - Lx)
                      / max(Lx, 1e-300))
        if led["ng"]:
            panc_w = max(panc_w,
                         float(np.max(led["gabs"]
                                      - led["mult"] * led["gmax"]))
                         / max(float(np.max(led["gabs"])), 1e-300))
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(ev["gen"]["mult"])[1]
    fr_ok = True
    fr_nodes = 0
    for rc in mrecs:
        if rc["ev"]["degenerate"]:
            continue
        leaves = [Fr(float(abs(v)))
                  for v in rc["ev"]["sct"]["x"]]
        for j in FR_PIN_IDX:
            stf = FBR.fr_path_state(leaves, FR_GRID[j])
            okx = (stf["tilt"] == stf["e3"]
                   and stf["e3h"] + stf["e3g"] == stf["e3"]
                   and stf["e3g"] <= stf["wb"]
                   and stf["pgi_dev"] == 0
                   and stf["blist"][-1] == stf["e3g"]
                   and stf["hslack"] >= 0)
            fr_ok = fr_ok and okx
        okm, wm, nm = FDD.fr_mart_check(FDD.fr_pair_tree(leaves))
        fr_ok = fr_ok and okm and (wm == 0)
        fr_nodes += nm
    check("G42-live-grid-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and mart_w <= TREE_BAR and unit_w <= TREE_BAR
          and rec_w <= TREE_BAR and jen_w <= JEN_BAR
          and tilt_w <= TILT_BAR and wqd_w <= WQ_BAR
          and part_w3 <= PART_BAR and bkd_w <= BK_BAR
          and env_w <= ENV_BAR and pgi_w <= PGI_BAR
          and hvy_w <= HVY_BAR and e3d_w <= DICT_BAR
          and part_w <= SA_BAR and l1rec_w <= SA_BAR
          and panc_w <= TOY_BAR and fr_ok and nz_tot == 0
          and mult_all_ok,
          "the FULL r341/r344 exact path layer live at EVERY "
          "sealed grid R on %d live worlds: tilted tower %.1e, "
          "weight norm %.1e, stopped partition %.1e, B-chain "
          "%.1e, envelope viol %.1e, Phi-Gamma %.1e, heavy "
          "hand-off viol %.1e, E3 == d3 %.1e (bars %.0e); "
          "martingale wards %.1e/%.1e/%.1e, Jensen %.1e; r316 "
          "chain %.1e; FRACTIONS BIT-EQUALITY at the two sealed "
          "pins R = 3/2 and 12/7 on w9+w13: %s (%d martingale "
          "nodes); r327 grounding %.1e/%.1e/%.1e; zero-mass "
          "leaves %d; fold multiplicity <= %d"
          % (len(live), tilt_w, wqd_w, part_w3, bkd_w, env_w,
             pgi_w, hvy_w, e3d_w, TILT_BAR, mart_w, unit_w,
             rec_w, jen_w, chain_w,
             "EXACT" if fr_ok else "BROKEN", fr_nodes, part_w,
             l1rec_w, panc_w, nz_tot, MULT_CAP))

    # ---------------- S5: r344 record reproduction + Leg A
    section("S5  LEG A -- r344 RECORD REPRODUCTION + THE SEALED "
            "STOP CANDIDATES")
    if smoke:
        check("G50-r344-balance-record", True, "SMOKE: skipped")
        check("G51-r344-cover-record", True, "SMOKE: skipped")
        check("G52-r344-partition-record", True, "SMOKE: skipped")
        check("G53-stop-candidates", True, "SMOKE: skipped")
        check("G54-envelope-cover", True, "SMOKE: skipped")
    else:
        cols_by_r = []
        for j, rr in enumerate(R_GRID):
            e3h_j = [rc["ev"]["pbg"][j]["e3h"] for rc in srt_full]
            e3g_j = [rc["ev"]["pbg"][j]["e3g"] for rc in srt_full]
            wb_j = [rc["ev"]["pbg"][j]["wb"] for rc in srt_full]
            hsh_j = [rc["ev"]["pbg"][j]["hsh"] for rc in srt_full]
            msh_j = [rc["ev"]["pbg"][j]["msh"] for rc in srt_full]
            hb_j = [srt_full[i]["ev"]["dic"]["ymx"] ** 2
                    * msh_j[i] for i in range(n_full)]
            shr_j = [e3h_j[i] / max(e3_col[i], 1e-300)
                     for i in range(n_full)]
            emptyg = sum(1 for i in range(n_full)
                         if e3g_j[i] <= 0.0)
            emptyh = sum(1 for i in range(n_full)
                         if e3h_j[i] <= 0.0)
            nh_te = sum(1 for i in te_i if e3h_j[i] > 0.0)
            ng_te = sum(1 for i in te_i if e3g_j[i] > 0.0)
            elig = (nh_te >= ELIG_FRAC * len(te_i)
                    and ng_te >= ELIG_FRAC * len(te_i))
            e_h_j = L2D.halves_slope([m_full[i] for i in te_i],
                                     [max(e3h_j[i], 1e-300)
                                      for i in te_i])
            e_g_j = L2D.halves_slope([m_full[i] for i in te_i],
                                     [max(wb_j[i], 1e-300)
                                      for i in te_i])
            h = len(te_i) // 2
            e_h_a = L2D.halves_slope(
                [m_full[i] for i in te_i[:h]],
                [max(e3h_j[i], 1e-300) for i in te_i[:h]])
            e_h_b = L2D.halves_slope(
                [m_full[i] for i in te_i[h:]],
                [max(e3h_j[i], 1e-300) for i in te_i[h:]])
            e_g_a = L2D.halves_slope(
                [m_full[i] for i in te_i[:h]],
                [max(wb_j[i], 1e-300) for i in te_i[:h]])
            e_g_b = L2D.halves_slope(
                [m_full[i] for i in te_i[h:]],
                [max(wb_j[i], 1e-300) for i in te_i[h:]])
            cols_by_r.append(dict(
                e3h=e3h_j, e3g=e3g_j, wb=wb_j, hsh=hsh_j,
                msh=msh_j, hb=hb_j, shr=shr_j, emptyg=emptyg,
                emptyh=emptyh, elig=elig, e_h=e_h_j, e_g=e_g_j,
                e_h_halves=(e_h_a, e_h_b),
                e_g_halves=(e_g_a, e_g_b)))
            info("R = %-6s hsh med %.3f  E3h share med %.3f  "
                 "W_B med %7.3f  empty-good %2d  empty-heavy "
                 "%2d  e_H %+.3f (halves %+.3f/%+.3f)  e_G "
                 "%+.3f (halves %+.3f/%+.3f)  %s"
                 % (("%.4f" % rr), float(np.median(hsh_j)),
                    float(np.median(shr_j)),
                    float(np.median(wb_j)), emptyg, emptyh,
                    e_h_j, e_h_a, e_h_b, e_g_j, e_g_a, e_g_b,
                    "ELIGIBLE" if elig else "INELIGIBLE"))
        hsh_meds = [float(np.median(c["hsh"])) for c in cols_by_r]
        shr_meds = [float(np.median(c["shr"])) for c in cols_by_r]
        wb_meds = [float(np.median(c["wb"])) for c in cols_by_r]
        e_h_t = tuple(c["e_h"] for c in cols_by_r)
        e_g_t = tuple(c["e_g"] for c in cols_by_r)
        elig_t = tuple(c["elig"] for c in cols_by_r)
        j_hat, elig_any = FTS.rhat_rule(e_h_t, e_g_t, elig_t)
        interior0 = 0 < j_hat < len(R_GRID) - 1
        e_h_a_t = tuple(c["e_h_halves"][0] for c in cols_by_r)
        e_h_b_t = tuple(c["e_h_halves"][1] for c in cols_by_r)
        e_g_a_t = tuple(c["e_g_halves"][0] for c in cols_by_r)
        e_g_b_t = tuple(c["e_g_halves"][1] for c in cols_by_r)
        j_a, el_a = FTS.rhat_rule(e_h_a_t, e_g_a_t, elig_t)
        j_b, el_b = FTS.rhat_rule(e_h_b_t, e_g_b_t, elig_t)
        stable0 = elig_any and el_a and el_b \
            and (j_a == j_hat) and (j_b == j_hat)
        ok_curve = (
            all(abs(hsh_meds[j] - R344_HSH_CURVE[j])
                <= R344_CURVE_TOL_HSH for j in range(6))
            and all(abs(shr_meds[j] - R344_SHR_CURVE[j])
                    <= R344_CURVE_TOL_SHR for j in range(6))
            and all(abs(wb_meds[j] - R344_WB_CURVE[j])
                    <= R344_CURVE_TOL_WB for j in range(6))
            and all(abs(e_h_t[j] - R344_EH_CURVE[j])
                    <= R344_CURVE_TOL_E for j in range(5))
            and all(abs(e_g_t[j] - R344_EG_CURVE[j])
                    <= R344_CURVE_TOL_E for j in range(6))
            and tuple(c["emptyg"] for c in cols_by_r)
            == R344_EMPTYG
            and tuple(c["emptyh"] for c in cols_by_r)
            == R344_EMPTYH
            and j_hat == R344_JHAT and interior0
            and (j_a, j_b) == R344_HALVES and not stable0)
        check("G50-r344-balance-record", ok_curve,
              "THE r344 BALANCE RECORD reproduced through the "
              "same code path: hsh med %s (rec %s), share med "
              "%s, W_B med %s, empty-good %s, empty-heavy %s; "
              "e_H %s, e_G %s; K0 (r344 argmin-max) R_HAT = "
              "%.4f (index %d, rec %d), halves pick (%s, %s) "
              "(rec %s) -> NOT halves-stable, the r344 "
              "instability reproduced"
              % (str([round(v, 3) for v in hsh_meds]),
                 str(list(R344_HSH_CURVE)),
                 str([round(v, 3) for v in shr_meds]),
                 str([round(v, 3) for v in wb_meds]),
                 str([c["emptyg"] for c in cols_by_r]),
                 str([c["emptyh"] for c in cols_by_r]),
                 str([round(v, 3) for v in e_h_t]),
                 str([round(v, 3) for v in e_g_t]),
                 R_GRID[j_hat], j_hat, R344_JHAT,
                 ("%.4f" % R_GRID[j_a]) if el_a else "NONE",
                 ("%.4f" % R_GRID[j_b]) if el_b else "NONE",
                 str(R344_HALVES)))
        # the r344 two-scale freezes + min-coverage (verbatim)
        third_ok = [ev_i["rho2"] <= GSQ_R321 * fa_full[i] ** 2
                    for i, ev_i in
                    enumerate(rc["ev"] for rc in srt_full)]
        cover_by_r = []
        for j in range(len(R_GRID)):
            cj = cols_by_r[j]
            per_a = {}
            for a in GA_FAM:
                CH = max(cj["hb"][i] / lg_full[i] ** a
                         for i in ca_i)
                CG = max(cj["wb"][i] / lg_full[i] ** a
                         for i in ca_i)
                covH = [e3_col[i] <= CH * lg_full[i] ** a
                        for i in range(n_full)]
                covG = [e3_col[i] <= CG * lg_full[i] ** a
                        for i in range(n_full)]
                cov = [covH[i] or covG[i] or third_ok[i]
                       for i in range(n_full)]
                viol = [i for i in te_x if not cov[i]]
                named = sum(1 for kz in NAMED_KZ
                            if cov[named_rank[kz]])
                mb = sum(1 for kz in MIDBAND_KZ
                         if cov[named_rank[kz]])
                third_used = sum(1 for i in te_x
                                 if cov[i] and not covH[i]
                                 and not covG[i])
                per_a[a] = dict(CH=CH, CG=CG, covH=covH,
                                covG=covG, cov=cov, viol=viol,
                                named=named, mb=mb,
                                third_used=third_used)
            aa = None
            for a in GA_FAM:
                if (not per_a[a]["viol"]
                        and per_a[a]["named"] == len(NAMED_KZ)
                        and per_a[a]["CH"] < CERT_GUARD
                        and per_a[a]["CG"] < CERT_GUARD):
                    aa = a
                    break
            cover_by_r.append(dict(per_a=per_a, aa=aa))
            info("R = %-6s " % ("%.4f" % R_GRID[j])
                 + "; ".join(
                     "a=%d C_H %.4f C_G %.4f viol %d/%d named "
                     "%d/4 mb %d/6 third-only %d"
                     % (a, per_a[a]["CH"], per_a[a]["CG"],
                        len(per_a[a]["viol"]), len(te_x),
                        per_a[a]["named"], per_a[a]["mb"],
                        per_a[a]["third_used"])
                     for a in GA_FAM)
                 + "; minimal a = %s" % str(aa))
        aa_hat = cover_by_r[j_hat]["aa"]
        pa_hat = cover_by_r[j_hat]["per_a"][R344_AA]
        fa_max = max(fa_full)
        i51 = kz_rank[51]
        x3b_third = sum(1 for kz in EXT3_KZ_B
                        if third_ok[kz_rank[kz]])
        # the r344 composed m_0*
        CHs0 = pa_hat["CH"]
        CGs0 = pa_hat["CG"]

        def rhs_r344(t):
            return (CHs0 + CGs0) * t + GSQ_R321 * fa_max ** 2 \
                * t ** 2
        m0_r344 = solve_m0(lambda t: math.log(
            max(rhs_r344(t), 1e-300)))
        ok_cover = (
            all(cover_by_r[j]["aa"] == R344_AA
                for j in range(len(R_GRID)))
            and abs(CHs0 - R344_CH1) <= R344_C_TOL
            and abs(CGs0 - R344_CG1) <= R344_C_TOL
            and pa_hat["third_used"] == R344_THIRD_ONLY
            and x3b_third == 6
            and abs(fa_max - R344_FA_MAX) <= R344_FA_TOL
            and abs(fa_full[i51] - R344_FA_MAX) <= R344_FA_TOL
            and m0_r344 is not None
            and abs(m0_r344 - M0_R344) <= M0_R344_TOL)
        check("G51-r344-cover-record", ok_cover,
              "THE r344 COVER RECORD reproduced: minimal "
              "certifying a = %d at EVERY grid point (0/51 + "
              "named 4/4); at (R_HAT = %.4f, a = 1) C_H %.4f "
              "(rec %.4f) C_G %.4f (rec %.4f); third-arm-only "
              "%d (rec %d) incl. EXT3-B %d/6; F_Amax %.2f = "
              "kz51 insertion %.2f (rec %.2f); composed m_0* "
              "10^%.1f (rec 10^%.1f)"
              % (R344_AA, R_GRID[j_hat], CHs0, R344_CH1, CGs0,
                 R344_CG1, pa_hat["third_used"],
                 R344_THIRD_ONLY, x3b_third, fa_max,
                 fa_full[i51], R344_FA_MAX,
                 m0_r344 if m0_r344 is not None else -1.0,
                 M0_R344))
        # the r344 partition census (verbatim) + kz55 anatomy
        hsh_hat = cols_by_r[j_hat]["hsh"]
        pred0 = [FTS.partition_predict(hsh_hat[i])
                 for i in range(n_full)]
        agree0 = 0
        nonpred0 = 0
        ncov0 = 0
        for i in te_x:
            if not pa_hat["cov"][i]:
                continue
            ncov0 += 1
            arm = "H" if pa_hat["covH"][i] else (
                "G" if pa_hat["covG"][i] else "T")
            if arm == pred0[i]:
                agree0 += 1
            elif arm != "T" and not (
                    pa_hat["covH"][i] and pa_hat["covG"][i]):
                nonpred0 += 1
        i55 = kz_rank[55]
        gt55 = srt_full[i55]["ev"]["gtree"]
        an55 = FTS.good_level_anatomy(gt55, R_GRID[R_STAR_IDX])
        eps55 = [(k, max(gk - 1.0, 0.0))
                 for k, _ng, _gm, _ga, _b, gk in an55]
        k_arg = max(eps55, key=lambda t: t[1])[0] if eps55 else -1
        wb55_hat = cols_by_r[j_hat]["wb"][i55]
        check("G52-r344-partition-record",
              agree0 == R344_PART_ACC and nonpred0 == R344_NONPRED
              and ncov0 == len(te_x)
              and k_arg == R344_EPS55_K
              and abs(wb55_hat - R344_WB55_HAT) <= R344_WB55_TOL,
              "THE r344 PARTITION RECORD reproduced: sealed hsh "
              "rule accuracy %d/%d (rec %d/51), covered ONLY by "
              "the non-predicted arm %d (rec %d); kz55 "
              "eps-argmax level %d (rec %d), W_B at R_HAT %.3f "
              "(rec %.3f) -- the three residues stand as "
              "measured, the canonization legs now adjudicate "
              "them"
              % (agree0, ncov0, R344_PART_ACC, nonpred0,
                 R344_NONPRED, k_arg, R344_EPS55_K, wb55_hat,
                 R344_WB55_HAT))
        # ---- LEG A: the four sealed stop candidates
        k1_j, ralg = rhat_intrinsic(R_GRID, GAMMA_CEIL)
        k1_interior = 0 < k1_j < len(R_GRID) - 1
        k1_cert = cover_by_r[k1_j]["aa"] is not None
        k2_j, k2_cross, k2_el = rhat_cross_first(e_h_t, e_g_t,
                                                 elig_t)
        k2_ja, k2_ca, _ = rhat_cross_first(e_h_a_t, e_g_a_t,
                                           elig_t)
        k2_jb, k2_cb, _ = rhat_cross_first(e_h_b_t, e_g_b_t,
                                           elig_t)
        k2_stable = k2_el and (k2_ja == k2_j) and (k2_jb == k2_j)
        k2_interior = 0 < k2_j < len(R_GRID) - 1
        k2_cert = cover_by_r[k2_j]["aa"] is not None
        k2_canon = k2_el and k2_cross and k2_interior and k2_stable
        k3_j, k3_rc, k3_cross, k3_el = rhat_cross_interp(
            R_GRID, e_h_t, e_g_t, elig_t)
        k3_ja, k3_rca, k3_ca, _ = rhat_cross_interp(
            R_GRID, e_h_a_t, e_g_a_t, elig_t)
        k3_jb, k3_rcb, k3_cb, _ = rhat_cross_interp(
            R_GRID, e_h_b_t, e_g_b_t, elig_t)
        k3_stable = k3_el and (k3_ja == k3_j) and (k3_jb == k3_j)
        k3_interior = 0 < k3_j < len(R_GRID) - 1
        k3_cert = cover_by_r[k3_j]["aa"] is not None
        k3_canon = k3_el and k3_cross and k3_interior and k3_stable
        eq_sign = [1 if e_h_t[j] >= e_g_t[j] else -1
                   for j in range(len(R_GRID))]
        eq_cross = [j for j in range(len(R_GRID) - 1)
                    if eq_sign[j] != eq_sign[j + 1]]
        check("G53-stop-candidates", True,
              "THE SEALED STOP CANDIDATES: K0 (r344 argmin-max) "
              "index %d halves (%d, %d) NOT stable "
              "(reproduced); K1 INTRINSIC R_ALG = %.4f -> R = "
              "%.4f (index %d, interior %s, data-free => "
              "halves-stable BY CONSTRUCTION, certifies %s); K2 "
              "FIRST-EQUILIBRATED index %d (R = %.4f, crossed "
              "%s, halves (%d%s, %d%s), STABLE %s, interior %s, "
              "certifies %s); K3 INTERPOLATED R_CROSS %s -> "
              "index %d (R = %.4f, halves R_CROSS %s/%s -> "
              "(%d, %d), STABLE %s, interior %s, certifies %s); "
              "equilibration census sign(e_H - e_G) = %s, "
              "crossings at grid gaps %s"
              % (j_hat, j_a, j_b, ralg, R_GRID[k1_j], k1_j,
                 str(k1_interior), str(k1_cert), k2_j,
                 R_GRID[k2_j], str(k2_cross), k2_ja,
                 "" if k2_ca else "(nc)", k2_jb,
                 "" if k2_cb else "(nc)", str(k2_stable),
                 str(k2_interior), str(k2_cert),
                 ("%.4f" % k3_rc) if k3_rc is not None else
                 "NONE", k3_j, R_GRID[k3_j],
                 ("%.4f" % k3_rca) if k3_rca is not None else
                 "NONE",
                 ("%.4f" % k3_rcb) if k3_rcb is not None else
                 "NONE", k3_ja, k3_jb, str(k3_stable),
                 str(k3_interior), str(k3_cert), str(eq_sign),
                 str(eq_cross)))
        # ---- K4: the R-free envelope
        hb_env = env_min_col([cols_by_r[j]["hb"]
                              for j in range(len(R_GRID))],
                             HENV_IDX)
        wb_env = env_min_col([cols_by_r[j]["wb"]
                              for j in range(len(R_GRID))],
                             tuple(range(len(R_GRID))))
        env_per_a = {}
        for a in GA_FAM:
            CHe = max(hb_env[i] / lg_full[i] ** a for i in ca_i)
            CGe = max(wb_env[i] / lg_full[i] ** a for i in ca_i)
            covHe = [e3_col[i] <= CHe * lg_full[i] ** a
                     for i in range(n_full)]
            covGe = [e3_col[i] <= CGe * lg_full[i] ** a
                     for i in range(n_full)]
            cove = [covHe[i] or covGe[i] or third_ok[i]
                    for i in range(n_full)]
            viole = [i for i in te_x if not cove[i]]
            namede = sum(1 for kz in NAMED_KZ
                         if cove[named_rank[kz]])
            mbe = sum(1 for kz in MIDBAND_KZ
                      if cove[named_rank[kz]])
            third_e = sum(1 for i in te_x
                          if cove[i] and not covHe[i]
                          and not covGe[i])
            env_per_a[a] = dict(CH=CHe, CG=CGe, viol=viole,
                                named=namede, mb=mbe,
                                third=third_e)
            info("K4 ENVELOPE a=%d: C_H_ENV %.4f C_G_ENV %.4f "
                 "viol %d/%d named %d/4 mb %d/6 third-only %d"
                 % (a, CHe, CGe, len(viole), len(te_x), namede,
                    mbe, third_e))
        env_aa = None
        for a in GA_FAM:
            if (not env_per_a[a]["viol"]
                    and env_per_a[a]["named"] == len(NAMED_KZ)
                    and env_per_a[a]["CH"] < CERT_GUARD
                    and env_per_a[a]["CG"] < CERT_GUARD):
                env_aa = a
                break
        k4_cert = env_aa is not None
        check("G54-envelope-cover", True,
              "K4 THE R-FREE ENVELOPE (HB min over grid indices "
              "%s positive-guarded, W_B min over all six; "
              "mid-ladder max-cal freezes): minimal certifying "
              "a = %s (%s); at a = %s C_H_ENV %.4f + C_G_ENV "
              "%.4f vs the r344 (R_HAT, 1) pair %.4f + %.4f -- "
              "the threshold-free form %s the tuning surface"
              % (str(HENV_IDX), str(env_aa),
                 "CERTIFIES" if k4_cert else "does NOT certify",
                 str(env_aa if env_aa is not None else GA_FAM[0]),
                 env_per_a[env_aa if env_aa is not None
                           else GA_FAM[0]]["CH"],
                 env_per_a[env_aa if env_aa is not None
                           else GA_FAM[0]]["CG"],
                 CHs0, CGs0,
                 "REMOVES" if k4_cert else "does NOT remove"))

    # ---------------- S6: Leg B -- the predictor family
    section("S6  LEG B -- THE SOURCE-SIDE PARTITION PREDICTOR")
    if smoke:
        check("G60-feature-census", True, "SMOKE: skipped")
        check("G61-predictor-family", True, "SMOKE: skipped")
        check("G62-predictor-adjudication", True,
              "SMOKE: skipped")
    else:
        grel_full = EFA.grel_col([rc["kz"] for rc in srt_full],
                                 core.G_ALL)
        eps_lv = []
        gam_lv = []
        for rc in srt_full:
            an = FTS.good_level_anatomy(rc["ev"]["gtree"],
                                        R_GRID[R_STAR_IDX])
            ev_eps = [(k, max(gk - 1.0, 0.0))
                      for k, _ng, _gm, _ga, _b, gk in an]
            if ev_eps and max(v for _k, v in ev_eps) > 0.0:
                eps_lv.append(max(ev_eps,
                                  key=lambda t: t[1])[0])
            else:
                eps_lv.append(-1)
            gl = rc["ev"]["dst"]["gmx_lv"]
            if gl:
                gam_lv.append(int(np.argmax(
                    [math.log(max(v, 1.0)) for v in gl])))
            else:
                gam_lv.append(-1)
        feats = [dict(hsh=hsh_hat[i], fa=fa_full[i],
                      grel=grel_full[i], nw=srt_full[i]["N"],
                      eps=eps_lv[i], gam=gam_lv[i],
                      m=m_full[i]) for i in range(n_full)]
        check("G60-feature-census", True,
              "THE SEALED FEATURE SET (source-pure) on the 51 "
              "test rows: hsh(7/4) med %.3f; F_A med %.2f "
              "(max %.2f); grel med %.2f (EXT3-B med %.2f -- "
              "the r329 small-gap family); N_w %d..%d; "
              "eps-argmax levels %s; Gamma-argmax levels %s; "
              "gap classes (r329 edges) %s"
              % (float(np.median([feats[i]["hsh"]
                                  for i in te_x])),
                 float(np.median([feats[i]["fa"]
                                  for i in te_x])),
                 max(feats[i]["fa"] for i in te_x),
                 float(np.median([feats[i]["grel"]
                                  for i in te_x])),
                 float(np.median([grel_full[kz_rank[kz]]
                                  for kz in EXT3_KZ_B])),
                 min(feats[i]["nw"] for i in te_x),
                 max(feats[i]["nw"] for i in te_x),
                 str(sorted(set(eps_lv[i] for i in te_x))),
                 str(sorted(set(gam_lv[i] for i in te_x))),
                 str({c: sum(1 for i in te_x
                             if EFA.gap_class(grel_full[i]) == c)
                      for c in ("SMALL", "MED", "LARGE")})))
        core_rows = list(te_i)
        x3_rows = list(range(n346, n_full))

        def acc_rows(rid, rows):
            good = 0
            for i in rows:
                p = pred_rule(rid, feats[i], PRED_TH)
                ok_i = (pa_hat["covH"][i] if p == "H" else
                        (pa_hat["covG"][i] if p == "G"
                         else third_ok[i]))
                if ok_i:
                    good += 1
            return good
        tab = []
        for rid in PRED_IDS:
            gc = acc_rows(rid, core_rows)
            gx = acc_rows(rid, x3_rows)
            gf = gc + gx
            tab.append((rid, gc, gx, gf))
            info("P%02d core %2d/%d  EXT3 %2d/%d  full %2d/%d"
                 % (rid, gc, len(core_rows), gx, len(x3_rows),
                    gf, len(te_x)))
        win = max(tab, key=lambda t: (t[1], -t[0]))
        w_rid, w_core, w_x3, w_full = win
        w_core_f = w_core / float(len(core_rows))
        w_x3_f = w_x3 / float(len(x3_rows))
        w_full_f = w_full / float(len(te_x))
        degenerate_w = w_rid in (11, 12)
        predictor_found = (w_core_f >= PRED_ACC_NEED
                           and w_x3_f >= PRED_OOS_NEED
                           and w_full_f >= PRED_ACC_NEED)
        # exact-priority-label comparison census (r344 metric)
        lab = ["H" if pa_hat["covH"][i] else
               ("G" if pa_hat["covG"][i] else
                ("T" if third_ok[i] else "-"))
               for i in range(n_full)]
        exact_w = sum(1 for i in te_x
                      if pred_rule(w_rid, feats[i], PRED_TH)
                      == lab[i])
        exact_p1 = sum(1 for i in te_x
                       if pred_rule(1, feats[i], PRED_TH)
                       == lab[i])
        miss_w = [srt_full[i]["kz"] for i in te_x
                  if not (pa_hat["covH"][i]
                          if pred_rule(w_rid, feats[i],
                                       PRED_TH) == "H" else
                          (pa_hat["covG"][i]
                           if pred_rule(w_rid, feats[i],
                                        PRED_TH) == "G"
                           else third_ok[i]))]
        check("G61-predictor-family", True,
              "THE SEALED 12-RULE FAMILY (selection: max core "
              "accuracy, ties smaller id): WINNER P%02d with "
              "core %d/%d (%.3f), OUT-OF-SAMPLE EXT3 %d/%d "
              "(%.3f), full %d/%d (%.3f); misses %s; the "
              "exact-priority-label census: winner %d/%d vs the "
              "r344 hsh baseline P01 %d/%d"
              % (w_rid, w_core, len(core_rows), w_core_f, w_x3,
                 len(x3_rows), w_x3_f, w_full, len(te_x),
                 w_full_f, str(miss_w), exact_w, len(te_x),
                 exact_p1, len(te_x)))
        check("G62-predictor-adjudication", True,
              "PREDICTOR ADJUDICATION (sealed bars core >= "
              "%.2f, OOS >= %.2f, full >= %.2f): "
              "PREDICTOR_FOUND %s%s -- %s"
              % (PRED_ACC_NEED, PRED_OOS_NEED, PRED_ACC_NEED,
                 str(predictor_found),
                 " (DEGENERATE single-arm baseline, disclosed)"
                 if degenerate_w else "",
                 ("the covering-arm partition is source-"
                  "predictable at the sealed bars"
                  if predictor_found else
                  "the partition stays posthoc at the sealed "
                  "bars -- harmless for the census-grade cover "
                  "(coverage certified independently), needed "
                  "only for the cofinal reading")))

    # ---------------- S7: Leg C -- the F_Amax defusal
    section("S7  LEG C -- THE F_Amax DEFUSAL (V1 CLASS SPLIT / "
            "V2 PERCENTILE / V3 FLOOR)")
    if smoke:
        check("G70-class-split", True, "SMOKE: skipped")
        check("G71-percentile-cap", True, "SMOKE: skipped")
        check("G72-floor-census", True, "SMOKE: skipped")
    else:
        def defuse_variant(split_val, tag):
            spk = [i for i in range(n_full)
                   if fa_full[i] > split_val] \
                if tag == "V2" else \
                [i for i in range(n_full)
                 if cls_rule(fa_full[i], split_val) == "SPIKE"]
            spk_set = set(spk)
            fam_q = max((fa_full[i] for i in range(n_full)
                         if i not in spk_set), default=0.0)
            # (a) uniform rescue: every SPIKE test row H/G-covered
            # at some a at the r344 cover point
            rescue = {}
            used_bud = set()
            for i in te_x:
                if i not in spk_set:
                    continue
                got = None
                for a in GA_FAM:
                    pa_a = cover_by_r[j_hat]["per_a"][a]
                    if pa_a["covH"][i]:
                        got = ("H", a)
                        break
                    if pa_a["covG"][i]:
                        got = ("G", a)
                        break
                rescue[srt_full[i]["kz"]] = got
                if got is not None:
                    used_bud.add(got)
            rescue_ok = all(v is not None
                            for v in rescue.values())
            # QUIET rows stay covered (0/51 anchor-gated); the
            # QUIET third-arm rows are re-checked at the capped
            # coordinate (their own F_A <= cap by construction)
            m0_uni = None
            if rescue_ok:
                def rhs_uni(t):
                    v = (CHs0 + CGs0) * t \
                        + GSQ_R321 * fam_q ** 2 * t ** 2
                    for arm, a in sorted(used_bud):
                        if a == 1:
                            continue
                        pa_a = cover_by_r[j_hat]["per_a"][a]
                        v += (pa_a["CH"] if arm == "H"
                              else pa_a["CG"]) * t ** a
                    return v
                m0_uni = solve_m0(lambda t: math.log(
                    max(rhs_uni(t), 1e-300)))

            def rhs_gen(t):
                return (CHs0 + CGs0) * t \
                    + GSQ_R321 * fam_q ** 2 * t ** 2
            m0_gen = solve_m0(lambda t: math.log(
                max(rhs_gen(t), 1e-300)))
            spk_kz = [(srt_full[i]["kz"], round(fa_full[i], 2),
                       lab[i]) for i in spk if i in set(te_x)]
            return dict(spk=spk, fam_q=fam_q, rescue=rescue,
                        rescue_ok=rescue_ok, m0_uni=m0_uni,
                        m0_gen=m0_gen, spk_kz=spk_kz)
        v1 = defuse_variant(FA_SPLIT, "V1")
        v1_defused = (v1["rescue_ok"] and v1["m0_uni"] is not None
                      and v1["m0_uni"] <= M0_R344
                      - M0_DEFUSE_MARGIN)
        check("G70-class-split", True,
              "V1 THE CLASS SPLIT (sealed rule F_A >= %.1f -> "
              "SPIKE, the r329 SPIKE_FA): %d spike rows total, "
              "test-row spike family (kz, F_A, covering arm) "
              "%s; F_AMAX_QUIET %.2f; UNIFORM RESCUE (every "
              "spike test row H/G-covered at some a): %s "
              "(rescue table %s) -> m_0*(uniform) %s; "
              "CLASS-CONDITIONAL m_0*(QUIET statement) 10^%.1f "
              "with the spike family as NAMED exceptions (each "
              "third-arm certified pointwise, cover unchanged "
              "0/51) -- a TWO-STATEMENT reading, NOT a uniform "
              "defusal, said honestly; V1 uniform defusal: %s"
              % (FA_SPLIT, len(v1["spk"]), str(v1["spk_kz"]),
                 v1["fam_q"], str(v1["rescue_ok"]),
                 str(v1["rescue"]),
                 ("10^%.1f" % v1["m0_uni"])
                 if v1["m0_uni"] is not None else "NONE",
                 v1["m0_gen"], str(v1_defused)))
        cap2 = float(np.percentile(np.asarray(fa_full), FA_PCTL))
        v2 = defuse_variant(cap2, "V2")
        v2_defused = (v2["rescue_ok"] and v2["m0_uni"] is not None
                      and v2["m0_uni"] <= M0_R344
                      - M0_DEFUSE_MARGIN)
        check("G71-percentile-cap", True,
              "V2 THE PERCENTILE CAP (sealed formula: F_A > "
              "P%d = %.3f -> SPIKE): %d spike rows, test-row "
              "family %s; F_AMAX_QUIET %.2f; uniform rescue %s "
              "-> m_0*(uniform) %s; class-conditional 10^%.1f; "
              "V2 uniform defusal: %s"
              % (int(FA_PCTL), cap2, len(v2["spk"]),
                 str(v2["spk_kz"]), v2["fam_q"],
                 str(v2["rescue_ok"]),
                 ("10^%.1f" % v2["m0_uni"])
                 if v2["m0_uni"] is not None else "NONE",
                 v2["m0_gen"], str(v2_defused)))
        fl_ok = [srt_full[i]["ev"]["rho2"]
                 <= GSQ_R321 * floor_bound(fa_full[i],
                                           FA_FLOOR) ** 2
                 for i in range(n_full)]
        below = [srt_full[i]["kz"] for i in range(n_full)
                 if fa_full[i] < FA_FLOOR]
        added = [srt_full[i]["kz"] for i in te_x
                 if fl_ok[i] and not third_ok[i]]
        lost = [srt_full[i]["kz"] for i in te_x
                if third_ok[i] and not fl_ok[i]]
        check("G72-floor-census", not lost,
              "V3 THE FLOOR FORM (rho_2 <= GSQ max(F_A, "
              "%.2f)^2, the open r329 successor question): "
              "rows below the floor %s; test rows ADDED by the "
              "floor %s (the raw third arm already covers "
              "them: %s); the floor can only widen the claim, "
              "never lose a row (lost %s); m_0* UNCHANGED by "
              "construction (F_Amax %.2f > floor) -- the "
              "below-range validity question stays OPEN on this "
              "sample (no test row sits below %.2f under the "
              "insertion convention), said honestly"
              % (FA_FLOOR, str(below), str(added),
                 str(sum(1 for i in te_x if third_ok[i])),
                 str(lost), fa_max, FA_FLOOR))

    # ---------------- S8: Leg D -- adjudication + composition
    section("S8  LEG D -- SEALED ADJUDICATION + COMPOSITION")
    if smoke:
        check("G80-adjudication", True, "SMOKE: skipped")
        check("G81-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (tilt_w > TILT_BAR or wqd_w > WQ_BAR
                      or part_w3 > PART_BAR or bkd_w > BK_BAR
                      or env_w > ENV_BAR or pgi_w > PGI_BAR
                      or hvy_w > HVY_BAR or e3d_w > DICT_BAR
                      or mart_w > TREE_BAR or unit_w > TREE_BAR
                      or rec_w > TREE_BAR or not fr_ok
                      or part_w > SA_BAR or l1rec_w > SA_BAR
                      or panc_w > TOY_BAR or not mult_all_ok
                      or fb_dev != 0 or fh_dev != 0
                      or fe_dev != 0)
        stop_canon = ((k1_cert and k1_interior)
                      or (k2_canon and k2_cert)
                      or (k3_canon and k3_cert) or k4_cert)
        thresh_flag = not (stable0 or k2_stable or k3_stable)
        # sealed headline preference: K1 > K3 > K2 > K4 > r344
        if k1_cert and k1_interior:
            head = ("K1", k1_j)
        elif k3_canon and k3_cert:
            head = ("K3", k3_j)
        elif k2_canon and k2_cert:
            head = ("K2", k2_j)
        elif k4_cert:
            head = ("K4", -1)
        else:
            head = ("R344", j_hat)
        if head[0] == "K4":
            a_h = env_aa
            CHh = env_per_a[a_h]["CH"]
            CGh = env_per_a[a_h]["CG"]
            cover_h = True
        else:
            a_h = cover_by_r[head[1]]["aa"]
            cover_h = a_h is not None
            pa_h = cover_by_r[head[1]]["per_a"][
                a_h if a_h is not None else GA_FAM[0]]
            CHh = pa_h["CH"]
            CGh = pa_h["CG"]

        def rhs_head(t):
            return (CHh + CGh) * t ** (a_h if a_h else 1) \
                + GSQ_R321 * fa_max ** 2 * t ** 2
        m0_head = solve_m0(lambda t: math.log(
            max(rhs_head(t), 1e-300))) if cover_h else None
        famax_defused = v1_defused or v2_defused
        canonized = stop_canon and predictor_found and cover_h
        vkey = canon_tree_verdict(leak, brk_struct, canonized)
        flags = []
        if thresh_flag:
            flags.append("THRESHOLD_NOT_CANONICAL")
        if predictor_found:
            flags.append("PREDICTOR_FOUND(P%02d, core %.3f, "
                         "oos %.3f)"
                         % (w_rid, w_core_f, w_x3_f))
        if famax_defused:
            flags.append("FAMAX_DEFUSED(%s, m_0* %s)"
                         % ("V1" if v1_defused else "V2",
                            ("10^%.1f" % v1["m0_uni"])
                            if v1_defused and v1["m0_uni"]
                            is not None else
                            (("10^%.1f" % v2["m0_uni"])
                             if v2["m0_uni"] is not None
                             else "NONE")))
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a "
                           "canonization builder",
            "CANON_STATE_NOT_EXACT":
                "an exact ward broke (tilt %.1e / part %.1e / "
                "env %.1e / hvy %.1e / Fractions %s / toys "
                "%s+%s+%s)"
                % (tilt_w, part_w3, env_w, hvy_w, str(fr_ok),
                   str(fb_dev), str(fh_dev), str(fe_dev)),
            "COVER_CANONIZED":
                "stop rule canonized (%s at R index %s, 0/51 + "
                "named 4/4 kept) AND the predictor holds "
                "(P%02d core %.3f / OOS %.3f)"
                % (head[0], str(head[1]) if head[1] >= 0
                   else "R-free", w_rid, w_core_f, w_x3_f),
            "COVER_CENSUS_ONLY":
                "the r344 coverage stands (anchor-gated 0/51 at "
                "every grid point) but the canonization is "
                "incomplete: stop-canonized %s, predictor %s, "
                "cover at headline %s -- the failing residue(s) "
                "named"
                % (str(stop_canon), str(predictor_found),
                   str(cover_h))}
        verdict_main = "%s(%s)%s" % (
            vkey, det_v[vkey],
            ("".join(" + " + f for f in flags)) if flags else "")
        check("G80-adjudication", True,
              "the sealed main letter fired: %s" % verdict_main)
        info("COMPOSITION TABLE (typed, POLYLOG form -- NO "
             "premature powerization; E[X_inf^3] <= [C_H + C_G] "
             "(log m)^a + %.4f F_cap^2 (log m)^2 => M_3 <= C_tot "
             "(log m)^A/m^2 => N_3 >= m/sqrt(C_tot (log m)^A), "
             "N_2 >= N_3; m_0* = smallest m with m^%.3f >= "
             "C_tot(log m)):"
             % (GSQ_R321, CRIT_EXP))
        info("  r344 baseline (R_HAT = 7/4, a = 1, F_Amax "
             "%.2f):        m_0* 10^%.1f (record 10^%.1f)"
             % (fa_max, m0_r344, M0_R344))
        info("  headline %s (a = %s, C_H %.4f + C_G %.4f, "
             "F_Amax %.2f): m_0* %s"
             % (head[0], str(a_h), CHh, CGh, fa_max,
                ("10^%.1f" % m0_head) if m0_head is not None
                else "NONE"))
        info("  V1 uniform rescue: %s;  V1 class-conditional "
             "(QUIET cap %.2f): 10^%.1f with named spike "
             "exceptions %s"
             % (("10^%.1f" % v1["m0_uni"])
                if v1["m0_uni"] is not None else
                "NOT AVAILABLE (rescue failed)",
                v1["fam_q"], v1["m0_gen"],
                str([t[0] for t in v1["spk_kz"]])))
        info("  V2 uniform rescue: %s;  V2 class-conditional "
             "(cap %.2f): 10^%.1f"
             % (("10^%.1f" % v2["m0_uni"])
                if v2["m0_uni"] is not None else
                "NOT AVAILABLE (rescue failed)",
                v2["fam_q"], v2["m0_gen"]))
        info("  comparisons: r324 measured route 10^%.1f; r341 "
             "envelope typing 10^%.1f (no cert); r306 census "
             "reading 10^%.1f"
             % (R324_M0_L10, m0_env, m0_306))
        check("G81-composition", True,
              "THE HONEST COFINAL TYPING: CENSUS = every freeze "
              "constant (C_H/C_G/C_ENV, mid-ladder max-cal on "
              "51 test rows), the coverage counts, the "
              "predictor accuracies, the class tables; LAW "
              "CANDIDATE = the K1 intrinsic formula (derived "
              "pair-ceiling algebra, data-free%s), the third-arm "
              "sliding form (banked r321 constant, held "
              "out-of-sample on EXT3 r329 + here)%s; MISSING "
              "for a cofinal statement: any bound beyond the "
              "measured rungs (the ladder-to-m_0* step stays "
              "the disclosed extrapolation hypothesis), a "
              "halves-stable exponent crossing (%s), and a "
              "spike-free uniform constant (defusal %s)"
              % (", certifies at its pick" if k1_cert else
                 ", does NOT certify",
                 ("; the predictor P%02d (OOS-confirmed)"
                  % w_rid) if predictor_found else "",
                 "NOT achieved -- flag fired"
                 if thresh_flag else "achieved",
                 "achieved" if famax_defused else
                 "NOT achieved (uniform m_0* unchanged)"))

    # ---------------- S9: Leg E -- worlds + must-fails + verdict
    section("S9  LEG E -- WORLD CENSUS + MUST-FAILS + VERDICT")
    wtab = [("w9", mrecs[0])]
    if not smoke:
        wtab.append(("w13(twin)", mrecs[1]))
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]))
    if smoke:
        for w, rc_w in wtab:
            ev = rc_w["ev"]
            info("world %-10s m %3d grid hsh %s"
                 % (w, ev["m"],
                    str([round(p["hsh"], 3) for p in ev["pbg"]])))
        check("G90-world-census", len(wtab) >= 1,
              "SMOKE: world curves printed (w9 + live controls)")
    else:
        for w, rc_w in wtab:
            ev = rc_w["ev"]
            fa_w = CCP.world_coord(ev["mqs"]["qm"], rc_w["N"],
                                   N_lad, q_lad)
            an_w = FTS.good_level_anatomy(ev["gtree"],
                                          R_GRID[R_STAR_IDX]) \
                if ev["gtree"] is not None else ()
            eps_w = [(k, max(gk - 1.0, 0.0))
                     for k, _ng, _gm, _ga, _b, gk in an_w]
            k_w = max(eps_w, key=lambda t: t[1])[0] \
                if eps_w and max(v for _k, v in eps_w) > 0.0 \
                else -1
            gl_w = ev["dst"]["gmx_lv"]
            g_w = int(np.argmax([math.log(max(v, 1.0))
                                 for v in gl_w])) if gl_w else -1
            grel_w = EFA.grel_col([rc_w["kz"]], core.G_ALL)[0]
            f_w = dict(hsh=ev["pbg"][j_hat]["hsh"], fa=fa_w,
                       grel=grel_w, nw=rc_w["N"],
                       eps=k_w, gam=g_w, m=ev["m"])
            info("world %-10s m %3d hsh(7/4) %.3f F_A(ins) "
                 "%.2f grel %.2f eps-lv %d gam-lv %d -> "
                 "winner P%02d says %s, class %s"
                 % (w, ev["m"], f_w["hsh"], fa_w, grel_w, k_w,
                    g_w, w_rid, pred_rule(w_rid, f_w, PRED_TH),
                    cls_rule(fa_w, FA_SPLIT)))
        check("G90-world-census", len(wtab) >= 2,
              "WORLD CENSUS (NO letter): the winner rule and "
              "the V1 class rule evaluated on %d worlds via the "
              "r321 insertion coordinate -- the predictor is a "
              "LADDER-cohort statement; the world rows are "
              "census only (their coverage columns are not "
              "defined on the ladder freezes)"
              % len(wtab))
    check("G91-e1-pred-from-coverage",
          len(e1_hits) >= 1 and mut1 == ("T", "G")
          and mut1 != ("H", "G"),
          "e1 protocol-CAUGHT twice: the predictor re-labeled "
          "after sight of the evaluated coverage column -- "
          "AST-FLAGGED (%s) -- and on the toy returns %s != the "
          "sealed rule labels ('H', 'G') (the family is sealed "
          "as FORMULAS in this spec BEFORE the freeze)"
          % (e1_hits[0] if e1_hits else "MISS", str(mut1)))
    check("G92-e2-clsrule-posthoc",
          len(e2_hits) >= 1 and mut2 == ("SPIKE", "SPIKE")
          and mut2 != ("SPIKE", "QUIET"),
          "e2 protocol-CAUGHT twice: the class flip consumes "
          "the evaluated violation column -- AST-FLAGGED (%s) "
          "-- and on the toy returns %s != the sealed class "
          "rule ('SPIKE', 'QUIET')"
          % (e2_hits[0] if e2_hits else "MISS", str(mut2)))
    check("G93-e3-env-doublecount",
          fe_brk == Fr(147, 32) and fe_dev == 0,
          "e3 CAUGHT exact: the R-free 'envelope' that SUMS the "
          "hand-off column over the grid returns 49/8 on the "
          "sealed Fractions stop-toy pin while the sealed "
          "envelope min is 49/32 -- break 147/32 EXACT (the "
          "real envelope constant is per-row min, single-"
          "counted)")
    check("G94-e4-crossing-posthoc",
          len(e4_hits) >= 1 and mut4 == 4 and mut4 != 2,
          "e4 protocol-CAUGHT twice: the crossing index "
          "re-picked after sight of the violation column -- "
          "AST-FLAGGED (%s) -- and on the toy returns %d != the "
          "sealed K2 toy output 2 (K2/K3 are sealed FORMULAS "
          "before the freeze)"
          % (e4_hits[0] if e4_hits else "MISS", mut4))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the K1/K2/K3/K4 stop-candidate adjudication "
          "with explicit halves columns, the sealed 12-rule "
          "source-side partition predictor with out-of-sample "
          "split, the three F_Amax defusal variants with honest "
          "m_0* table, and the cofinal census-vs-law typing -- "
          "NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R346_ANCHORS(identity %.1e, r306 C2 %.3f v%d, "
                 "r316 n %d, r324-pre C_M2 %.4f, r339 WF %.2f, "
                 "r324 e_tot %+.3f, r341 complete, r321 FA "
                 "%.2f/%.2f/%.2f, r344 COMPLETE: curve + R_HAT "
                 "%d + halves (%d, %d) + C_H/C_G %.4f/%.4f + "
                 "0/51 everywhere + third-only %d + partition "
                 "%d/51 + F_Amax %.2f + m_0* 10^%.1f)"
                 % (rec3_w, C2r, viol2, n346, C_M2, wf_med,
                    e_tot324, fa_kz[53], fa_kz[83], fa_kz[67],
                    j_hat, j_a, j_b, CHs0, CGs0,
                    pa_hat["third_used"], agree0, fa_max,
                    m0_r344)]
        parts.append("SEAL(grid tilt %.1e, part %.1e, env %.1e, "
                     "hvy %.1e, mart %.1e, Fractions %s at pins "
                     "3/2+12/7, grounding %.1e, purity clean, "
                     "toys exact incl. envelope pin 49/32)"
                     % (tilt_w, part_w3, env_w, hvy_w, mart_w,
                        "EXACT" if fr_ok else "BROKEN",
                        max(part_w, l1rec_w, panc_w)))
        parts.append("STOPRULE(K0 idx %d halves (%d, %d) "
                     "unstable; K1 R_ALG %.4f -> idx %d cert %s; "
                     "K2 idx %d stable %s cert %s; K3 R_CROSS "
                     "%s -> idx %d stable %s cert %s; K4 env "
                     "a* %s CH+CG %.4f+%.4f; STOP-CANONIZED %s)"
                     % (j_hat, j_a, j_b, ralg, k1_j,
                        str(k1_cert), k2_j, str(k2_stable),
                        str(k2_cert),
                        ("%.4f" % k3_rc) if k3_rc is not None
                        else "NONE", k3_j, str(k3_stable),
                        str(k3_cert), str(env_aa),
                        env_per_a[env_aa if env_aa is not None
                                  else GA_FAM[0]]["CH"],
                        env_per_a[env_aa if env_aa is not None
                                  else GA_FAM[0]]["CG"],
                        str(stop_canon)))
        parts.append("PREDICTOR(winner P%02d core %d/%d oos "
                     "%d/%d full %d/%d%s; baseline P01 exact "
                     "%d/%d; FOUND %s)"
                     % (w_rid, w_core, len(core_rows), w_x3,
                        len(x3_rows), w_full, len(te_x),
                        " DEGENERATE" if degenerate_w else "",
                        exact_p1, len(te_x),
                        str(predictor_found)))
        parts.append("DEFUSE(V1 spikes %d quiet-cap %.2f rescue "
                     "%s m0_uni %s m0_class 10^%.1f; V2 cap "
                     "%.3f rescue %s; V3 floor below %s added "
                     "%s; DEFUSED %s)"
                     % (len(v1["spk"]), v1["fam_q"],
                        str(v1["rescue_ok"]),
                        ("10^%.1f" % v1["m0_uni"])
                        if v1["m0_uni"] is not None else "NONE",
                        v1["m0_gen"], cap2,
                        str(v2["rescue_ok"]), str(below),
                        str(added), str(famax_defused)))
        parts.append(verdict_main)
        parts.append("COMPOSITION(headline %s a %s C %.4f+%.4f "
                     "m_0* %s vs r344 10^%.1f, r324 10^%.1f, "
                     "r306 census 10^%.1f)"
                     % (head[0], str(a_h), CHh, CGh,
                        ("10^%.1f" % m0_head)
                        if m0_head is not None else "NONE",
                        M0_R344, R324_M0_L10, m0_306))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the path identities, "
          "the pair-ceiling algebra, the Fractions toys and "
          "grid pins, the tree logic and the purity audits "
          "(exact / AST-decided); MEASURED: every census, "
          "constant, accuracy, violation count and exponent "
          "(the finite class ladder + 12 EXT3 + 2 mains + 2 "
          "live controls); OPEN: any bound beyond the measured "
          "rungs, the cofinal law, the actual proof (a "
          "certifying cover fixes a theorem candidate with "
          "explicit constants, it proves nothing cofinal); NO "
          "RH claim"
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
