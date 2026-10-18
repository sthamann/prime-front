#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""thirdarm_spike_law_probe --
PRIME.L2.THIRDARM_LAW.01 (round 349): THE THIRD-ARM COVERAGE OF
THE SPIKE FAMILY AS A LAW -- the named residue after r346.

CONTEXT (binding, from the sealed r346 record SPEC_SHA 306dba57,
COVER_CANONIZED + PREDICTOR_FOUND(P02)): the terminal three-arm
min-coverage certifies 0/51 at a = 1 (heavy arm = the hand-off
column (m q_max)^2 msh, good arm = the eps-chain column W_B,
third arm = the banked r321 sliding bound rho_2 <= GSQ x F_A^2
with GSQ = 1.3056 FROZEN); the stop rule is canonized by K1
(R_ALG = 4^(1/3), data-free) and K4 (R-free envelope, C_G_ENV
0.4867); the working partition is SPIKE-VS-REST in F_A: P02
(F_A >= 1.5 -> third arm, else heavy) predicts a covering arm on
51/51 (core 39/39, EXT3 12/12 out-of-sample).  THE OPEN RESIDUE
(this round's object): the six sharp spikes kz53/kz67/kz51/kz54/
kz42/kz62 are covered ONLY by the third arm at EVERY a; the
uniform constant therefore inherits F_Amax = 5.54 -> m_0* =
10^22.6, while the class-conditional reading (QUIET cap 1.39)
would give 10^16.1 but is NO uniform bound (13 named test-row
exceptions).  THE CORE QUESTION (contract): is the r321 sliding
coverage of the F_A >= 1.5 family a derivable LAW (source-side,
or a clean class theorem with sealed premises) -- and what is
the honest m_0* of the two-statement structure?

THE EXACT ALGEBRA OF THIS ROUND (derived, disclosed, no
measurement -- the r321/r324 records restated): with q_j =
|x_j|/L, pk = max q (the r316 QMAX column), M2q = sum q^2, c3q =
sum q^3, lg = log m, the r306 scale rho_2 = m^2 c3q / lg^2, the
r321 coordinate F_A = pk/medloc and baseline B = medloc m/lg
(r324 identity F_A B lg == m pk EXACT):
  (i) THE RESERVE FACTORIZES EXACTLY:
        RSV := GSQ F_A^2 / rho_2 = S_const x S_M2 x S_dom,
        S_const = GSQ/B^2       (the calibration slack: the
                                 frozen (max cal B)^2 over the
                                 rung's own B^2 -- can be < 1,
                                 the r321 honest caveat),
        S_M2   = pk/M2q         (the r324 interpolation slack
                                 c3q <= pk M2q, >= 1 always),
        S_dom  = pk M2q/c3q     (the dominance slack of the
                                 chain c3q <= pk M2q, >= 1),
      and S_M2 x S_dom = pk^2/c3q = 1/(D pk) with the DOMINANCE
      RATIO D := c3q/pk^3 >= 1 (D == 1 iff a single atom carries
      the cube).
  (ii) THE DOMINANCE FORM OF THE TARGET (exact):
        rho_2 = D x pk x (F_A B)^2  and  RSV = GSQ/(D pk B^2);
      via the r324 identity pk = F_A B lg / m this reads
        RSV = GSQ m / (D F_A B^3 lg):
      the spike coverage is the r324 identity ITSELF plus the
      dominance/concentration structure -- large F_A on this
      family comes WITH a dominant atom (D near 1) and a small
      pk B^2, and THAT is where the reserve lives.  Whether the
      family really is dominance-concentrated is Leg C's
      measurement; the identities are warded live.

THE SEALED MACHINERY (disclosed BEFORE any evaluation):
  LEG A -- THE RESERVE ANATOMY: per row the exact decomposition
      (S_const, S_M2, S_dom) via the module-own res_decomp
      (Fractions toy pinned), warded EXACT against RSV on every
      family row; the reserve-vs-F_A monotonicity: rc_fam =
      Spearman(F_A, RSV) over the family rows plus the fit-free
      LOWER envelope over NB_RES = 4 equal-count F_A-rank bins
      of the family (module-own lower_env_min, declared-set
      warded).  MONO_OK iff rc_fam >= RC_MONO = +0.5 OR (the
      bin-min Spearman >= +0.5 AND the envelope argmin is the
      first bin) -- the family is safe upward by monotonicity.
      FALLING flag iff rc_fam <= -0.5; else FLAT.  The
      reserve-source census: median log10 shares of the three
      factors on the family vs the quiet rest.
  LEG B -- THE CLASS THEOREM CANDIDATE (sealed bars): "for every
      rung with F_A >= F0_SPLIT = 1.5 (the r329 SPIKE_FA record
      constant, boundary inclusive): rho_2 <= GSQ x F_A^2 with
      reserve >= RHO_BAR = 1.5" (RHO_BAR a-priori, below the
      contract-quoted family minimum 1.6).  Tested POINTWISE on
      ALL available rows: the 65-rung ladder + the 12 EXT3
      anchors (F_A convention: ladder = EFP.local_ratio, EXT3 =
      the r321 insertion rule CCP.world_coord -- the r344/r346
      third-arm convention VERBATIM) + the 6 EXT4 anchors (the
      r343/r345 L*-lane fresh list kz72/75/66/113/111/108, N_w
      2656..3181, adopted as-is as PURE TEST rows -- never seen
      by any cubic-lane calibration; admission POSITIVE_PREFIX +
      mult <= 2 + non-degenerate, failures dropped with census).
      CERT iff 0 family rows below RHO_BAR (two tiers printed:
      hard violations RSV < 1, bar violations RSV < RHO_BAR).
      THE BOUNDARY CENSUS: rows with F_A in [F0/BND_FAC, F0 x
      BND_FAC], BND_FAC = 4/3, listed from both sides with their
      covering arms at the r346 cover point (grid index 4, a=1).
      HAND-OFF iff every test row below F0 is heavy- or
      good-covered there (the P02 complementarity as exact
      hand-over).  THE 13 EXCEPTIONS of the r346 class-
      conditional reading adjudicated INDIVIDUALLY: dissolved
      iff covered by the spike statement with RSV >= RHO_BAR;
      remaining holes NAMED.
  LEG C -- THE SOURCE DERIVATION (the dominance test): D per
      row; cohort census family / quiet / six-sharp.  DOM_OK iff
      med D(family) <= D_FAM_MED_BAR = 2.5 AND max D(family) <=
      D_FAM_MAX_BAR = 6.0 AND med D(quiet)/med D(family) >=
      DOM_CONTRAST = 3.0 -- the family is the dominant-atom
      class and the chain rho_2 = D pk (F_A B)^2 closes with
      D = O(1): the coverage is the r324 identity + dominance +
      the measured concentration ceiling pk B^2 <= GSQ/(RHO_BAR
      D) (the remaining census-grade premise, typed honestly).
      The exact chain wards: rho_2 lg^2/m^2 == c3q (the r306
      NORM identity, independent recomputation of sum|x|^3/L^3
      from the r314 genealogy column);
      RSV == GSQ/(D pk B^2) EXACT; the r324 identity F_A x
      medloc == pk EXACT on the ladder (EFP-vs-CCP cross-ward).
  LEG D -- THE HONEST m_0* OF THE TWO-STATEMENT STRUCTURE: the
      m_0* table (r344/r346 uniform 10^22.6; V1 class-
      conditional QUIET 10^16.1 / V2 10^17.5; the spike-side
      solve with the family census ceiling F_Amax; the two-
      statement composite = max(quiet statement, spike
      statement)); the cofinal typing per building block (r346
      convention: census / law candidate / missing) -- the
      uniform number is NOT expected to move (the family F_A
      ceiling stays a census number); the honest gain is the
      TYPE upgrade of the 10^16.1 reading iff the exceptions
      dissolve, said out loud.
  LEG E -- WORLDS + MUST-FAILS: the class rule + class statement
      evaluated on MAIN w9 / twin w13 / EPSTEIN / SCRAMBLE via
      the r321 insertion coordinate (census, NO letter);
      SCRAMBLE is SPIKE-flagged (F_A(ins) 2.00, r346 record) --
      whether the statement covers it is typed honestly: a
      covering statement is then ARITHMETIC-FREE, a pure size
      statement about concentration, no world separation claimed.

LEG 0 -- ANCHOR REGRESSION (bit-near; slim set + the COMPLETE
r344/r346 record surface of this lane, disclosed): the r314
identity wards live; r306 C_2 = 1.069 (tol 0.005) first-5 freeze
0/57; r316 rho anchors + C_small + n = 65; the dictionary-chain
identity live; the r321 F_A top-3 kz53 2.47 / kz83 2.39 / kz67
2.38 through EFP.local_ratio; THE r344 BALANCE + COVER RECORD
COMPLETE through the same code path (curve + R_HAT 7/4 + halves
(8/5, 7/4) + C_H/C_G 3.9859/1.1409 + 0/51 at every grid point at
a = 1 + third-only 8 + EXT3-B 6/6 + F_Amax 5.54 + m_0* 10^22.6);
THE r346 RECORD (K1 pick index 1 + certification with C 6.8806 +
1.0151; K4 envelope C_H_ENV 3.9859 + C_G_ENV 0.4867 certifying;
P02 core 39/39 + EXT3 12/12; V1 13 test-row spikes + QUIET cap
1.39 + rescue FAILS + m_0*(class) 10^16.1; V2 cap 1.917 +
10^17.5; the six sharp spikes {53, 67, 51, 54, 42, 62} ONLY
third-covered at every a); the r344 third-arm ratios of the four
sharp EXT3-B spikes kz51 0.19 / kz54 0.16 / kz42 0.29 / kz62
0.31 (tol 0.01) -- the r329 out-of-sample reserves restated
under the insertion convention.

LEG E MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) RESERVE BAR READ FROM THE TARGET (protocol):
  mutant_reserve_bar_posthoc sets the bar at the seen minimum
  reserve (consumes rho) -- the BOUND_FORBIDDEN scope audit must
  FLAG it AND on the sealed toy it returns 0.5 != the sealed
  RHO_BAR 1.5 -- protocol-CAUGHT twice.
(e2) F0 CHOSEN AFTER SIGHT (protocol): mutant_f0_posthoc re-
  picks the family threshold to minimize the seen violations
  (consumes rho) -- AST-FLAGGED and on the sealed toy returns
  2.0 != the sealed F0_SPLIT 1.5 -- protocol-CAUGHT twice.
(e3) DOMINANCE WITH CIRCULAR QMAX: mutant_dom_circular reads the
  qmax RECORD column instead of recomputing from the same block
  vector -- the QMAX_FORBIDDEN scope audit must FLAG it AND on
  the sealed Fractions toy (q = (3/4, 1/4), stale record value
  1/2) it returns 7/2 while the true dominance is 28/27 --
  CAUGHT twice.
(e4) CHAIN WITH THE WRONG LOG POWER: mutant_chain_wrong_log
  claims rho_2 = m^2 c3q/lg (power 1) -- on the sealed Fractions
  toy (m = 3, c3q = 1/6, pseudo-log lg = 2) it returns 3/4 while
  the exact chain gives 3/8 -- break factor == lg == 2 EXACT.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

SEALED VERDICTS (main letter: exactly one fires, total order;
flags appended with '+', combinations allowed by the contract):
   TARGET_LEAK            iff any purity/scope/literal audit hit
       on the module-own law builders,
   LAW_STATE_NOT_EXACT    iff an exact ward breaks on a live
       world (the r344/r346 path layer / the NORM identity / the
       reserve decomposition / the dominance chain / the r324
       identity / the Fractions pins / the toys),
   THIRDARM_LAW_DERIVED   iff CERT AND HAND-OFF AND DOM_OK (the
       dominance route closes: the spike coverage is the r324
       identity + dominance, theorem-candidate grade with the
       named census premise),
   CLASS_THEOREM_CERTIFIED iff CERT AND HAND-OFF AND MONO_OK
       (0 violations at the sealed bars, seamless hand-over,
       monotone-safe family -- but the dominance structure does
       not meet the sealed bars),
   RESERVE_ACCIDENTAL     iff CERT AND HAND-OFF but neither
       DOM_OK nor MONO_OK -- the numbers hold, the class
       threshold has no certified structure, said honestly,
   EXCEPTIONS_REMAIN      otherwise -- violations or hand-off
       holes; every hole NAMED.
   FLAGS: +RESERVE_MONOTONE/FLAT/FALLING(rc) /
       +DOMINANT_FAMILY(med_fam, med_quiet) /
       +EXCEPTIONS_DISSOLVED(k/13) / +HOLES(kz list) /
       +SCRAMBLE_IN_CLASS(rsv) / +EXT4_CLEAN(n).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in either
direction.  Coexistence: r348 (delta source anatomy, L*) may run
in parallel -- own files only; before the strictly additive
rh-sync the current git state is re-checked.  Two-commit freeze
protocol (r329 convention): spec committed pre-freeze, record
tables the only post-freeze edit, committed again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r317/r321/r324/r327/
r333/r337/r339/r341/r344/r346 machinery imported verbatim; the
ENTIRE r344/r346 scaffold -- census, controls, extensions, EXT3,
decomposition wards, path layer at every sealed grid R,
Fractions pins, two-scale freezes, min-coverage, predictor,
class split -- is re-executed through the same code path and
anchor-gated against the r344/r346 records): t_{N-2} = sum_b
ct_b; F = 0.20 edge split; level-2 blocks; the r306 RY3 layer;
the r314 SCF layer; the r316 TRB layer; the r317
EFP.local_ratio; the r321 CCP.local_median + CCP.world_coord +
CCP.spearman_rank; the r324 QMO/FAP layers; the r327 GMC
grounding; the r339 FDD tree layer; the r341 FBR path layer; the
r344 FTS balance layer; the r346 FCC canonization layer
(rhat_intrinsic, env_min_col, pred_rule, cls_rule -- imported
verbatim); the r329 EFA.grel_col + EFA.gap_class.  NEW in this
round (module-own): res_decomp (the exact reserve
factorization), lower_env_min (the fit-free lower envelope with
declared-set ward), bnd_rule (the sealed boundary-band letter),
law_tree_verdict (the sealed verdict tree) and fr_decomp_toy
(the Fractions decomposition pin).  The reserve, the dominance
ratio D and every census on them are TARGET-SIDE DIAGNOSTICS
computed in the gate section (the r321 qmax-share convention,
disclosed) -- the module-own builders consume passed values,
sealed thresholds and the F_A column only.

INDEX FIREWALL (binding, r238-r348 discipline): w = window (kz),
N_w = builder depth, k = tree level, n(v) = leaf count; ground
truth enters GATES and census tables only; the cubic target M_3
/ rho_2 and the q_max RECORD enter GATES / anchors / coverage
checks / reserve diagnostics only, NEVER a law builder
(AST-warded); no zero/prime oracles anywhere (AST firewall); no
fit primitives (fragment audit; exponents are the imported r272
dyadic halves-slope, fit-free; Spearman is the imported r321
rank correlation, fit-free).  B PROVENANCE: B_w = S_{N-2} + 5/7
(imported floor, never fitted).  COFINAL LADDER (pre-sealed,
r316/r324/r329/r339/r341/r344/r346 verbatim): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}; EXTENSION 900 < h <= 1300 first 15; EXT2 r316 A5 rule;
EXT3 = the sealed r329 12-anchor list (adopted as-is, PURE TEST
rows); EXT4 = the sealed r343/r345 6-anchor list (adopted as-is,
PURE TEST rows of THIS round, census-admitted).

SEALED CONSTANTS (everything not listed here is the r344/r346
constant set imported verbatim from FTS/FCC): F0_SPLIT 1.5 (=
the r329 SPIKE_FA record constant, = FCC.FA_SPLIT); RHO_BAR 1.5
(a-priori); BND_FAC 4/3; NB_RES 4; RC_MONO 0.5; RC_FALL -0.5;
D_FAM_MED_BAR 2.5; D_FAM_MAX_BAR 6.0; DOM_CONTRAST 3.0; EXT4_KZ
(72, 75, 66, 113, 111, 108); EXT4_NW (2656, 3181);
TB_WARD_BAR_X4 1e-4 (a-priori, one notch above the EXT3 bar for
up to 1.24x the depth); REC3_BAR_X4 1e-12; DEC_BAR 1e-9 (the
decomposition/chain ward bar); R346 record anchors (tol): K1_IDX
1 EXACT; K1_CH 6.8806 / K1_CG 1.0151 tol 0.001; K4_CH 3.9859 /
K4_CG 0.4867 tol 0.001; P02_CORE 39 / P02_OOS 12 EXACT; V1_NSPK
13 EXACT; V1_FAMQ 1.39 tol 0.01; V1_M0 16.1 tol 0.2; V2_CAP
1.917 tol 0.005; V2_M0 17.5 tol 0.2; SIX_KZ (53, 67, 51, 54, 42,
62) EXACT (the only-third-at-every-a set); SIX_RATIO {51: 0.19,
54: 0.16, 42: 0.29, 62: 0.31} tol 0.01; R349_TABLE_LITERALS =
the sealed r314..r346 set (FCC verbatim) UNION the r346 record
set {6.8806, 1.0151, 16.1, 17.5, 1.917} (the collision-prone
small ratios/reserves 1.39, 0.19, 0.16, 0.29, 0.31, 5.3, 6.2,
3.5, 3.2 are curated OUT of the forbidden set, r337..r346
convention, disclosed); runtime <= 1800 s; smoke = w9 + controls
+ toys + scope/purity audits + the exact path wards + the w9
Fractions pins + e1-e4 mutants; ladder, extensions, EXT3, EXT4,
anchors, coverage, anatomy, class census, dominance, composition
and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r321/r324/r329/r344/r346 RECORD
number adopted as-is; the reserve factorization, the dominance
form and the r324-identity reading are DERIVED ALGEBRA from the
sealed r321/r324 identities (disclosed above); record-derived
EXPECTATIONS disclosed as such (never computed by this probe):
from the r329/r344 record numbers kz51 (pk 0.1291, rho_2 7.6196,
m 335, F_ins 5.54) one derives BY HAND D ~ 1.07 and RSV ~ 5.3 --
the sharp-spike family is EXPECTED dominance-concentrated; the
GENUINELY OPEN quantities: every D value, every decomposition
row, the family census on 65 + 12 + 6 rows, the monotonicity
correlation, the boundary census, the 13-exception adjudication,
the EXT4 columns and every composed number -- NONE was computed
before this spec froze; the sealed toys are computed BY HAND
(res_decomp toy q = (1/2, 1/3, 1/6), gsq = 2, b2 = 1: S = (2,
9/7, 7/6), product 3 EXACT; dominance toys q = (1/2, 1/3, 1/6)
-> D = 4/3, one-block -> 1; e3 toy 7/2 vs 28/27; e4 toy 3/4 vs
3/8, break factor 2; boundary toys 0.5 -> BELOW, 1.2 -> BAND_LO,
1.6 -> BAND_HI, 1.5 -> BAND_HI inclusive, 2.5 -> ABOVE;
lower-envelope rising/falling toys argmin first/last with bin
Spearman +1/-1; the six verdict-tree branches EXACT); the sealed
bars RHO_BAR / BND_FAC / NB_RES / RC bars / D bars are coarse
a-priori choices sized BEFORE any evaluation; the six letters
are symmetric and total by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R349_ANCHORS(identity wards, r306 C_2, r316, dictionary, r321
    F_A top-3, THE r344 RECORD COMPLETE, THE r346 RECORD: K1 +
    K4 + P02 + V1/V2 + six spikes + ratios)
+ SEAL(path wards + Fractions pins + NORM identity + r324
    identity + decomposition ward + purity + toys)
+ ANATOMY(the reserve table + factor census + monotonicity:
    rc_fam, envelope bins, MONO/FLAT/FALLING)
+ CLASSLAW(the family census on 65 + 12 + 6 rows: hard/bar
    violations; boundary census; hand-off; the 13 exceptions
    adjudicated)
+ DOMINANCE(D cohort census + contrast + DOM_OK + the source-
    side reading)
+ [exactly one of] THIRDARM_LAW_DERIVED / CLASS_THEOREM_
    CERTIFIED / RESERVE_ACCIDENTAL / EXCEPTIONS_REMAIN /
    LAW_STATE_NOT_EXACT / TARGET_LEAK  [+ flags]
+ COMPOSITION(the m_0* table + the two-statement composite + the
    cofinal typing)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the factorization, the dominance form,
the r324 identity, the Fractions toys and the purity audits are
EXACT (Fractions/AST-decided); every census, constant, reserve,
D value and violation count is MEASURED on the finite ladder +
the 12 EXT3 + the 6 EXT4 anchors only; a certified class
statement fixes a theorem CANDIDATE with explicit constants and
sealed premises, it proves NO cofinal law -- the family F_A
ceiling and the pk B^2 ceiling stay census numbers, the
ladder-to-m_0* step stays the disclosed extrapolation
hypothesis; a covering statement on SCRAMBLE makes the class
statement arithmetic-free BY MEASUREMENT and is typed as such;
r243-r348 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA 0016e2f1596978da,
pre-freeze commit b2ef45ea; protocol: smoke pass 1 = 44/44
(1.1 s, run pre-commit, disclosed in the commit message,
together with the pre-run placeholder removal -- the r321
protocol-error class, disclosed there and here); calibration
pass 1 = FIRST full evaluation = 44/44, wall 329.5 s;
DISCLOSED AMENDMENT a1 (code-only, print-level, between
calibration passes): the sealed EXCEPTIONS_REMAIN contract
demands EVERY hole NAMED -- the letter's detail text and the
HOLES flag had only listed ladder/EXT3 holes and were extended
to name the EXT4 bar misses; NO bar, band, rule or verdict rule
moved at any point; calibration pass 2 = 44/44, wall 334.4 s,
numerically identical; record run1/run2 after this insertion,
identical up to the runtime line):
MAIN VERDICT: EXCEPTIONS_REMAIN(hard [] bar [] hand-off holes
[] EXT4 bar misses [(kz111, 1.11), (kz75, 1.07)]) +
RESERVE_FLAT(-0.33) + EXCEPTIONS_DISSOLVED(13/13) +
HOLES([111, 75]) + SCRAMBLE_IN_CLASS(rsv 2.9, world census).
THE HEADLINE FINDINGS:
(1) THE RAW LAW HOLDS EVERYWHERE, THE SEALED RESERVE FLOOR IS
UNDERCUT OUT-OF-SAMPLE: the class statement rho_2 <= 1.3056
F_A^2 on F_A >= 1.5 holds with ZERO hard violations on ALL 23
family rows across 65 ladder + 12 EXT3 + 6 EXT4 (even at the
new out-of-sample record F_ins = 6.68, kz111) -- the r321 form
itself never breaks on a spike; but the sealed reserve bar
RHO_BAR = 1.5 is undercut by exactly the two deepest FRESH
EXT4 spikes kz111 (rsv 1.11) and kz75 (rsv 1.07) -> CERT False
by the sealed letter, the reserve floor is NOT >= 1.5
uniformly: the honest floor on the fresh cohort is ~1.1.  The
EXT4 cohort is itself a finding: ALL SIX r343/r345 L*-lane
fresh anchors are SPIKE-class under the insertion coordinate
(F_ins 1.58/2.03/3.11/4.22/5.53/6.68, reserves 3.1/5.6/2.4/
2.4/1.1/1.1) -- the deep fresh pool is spike-dominated, and
the family F_A ceiling GROWS out-of-sample (5.54 -> 6.68): the
r346 census ceiling is not stable, said honestly.
(2) LEG A -- THE RESERVE ANATOMY (exact factorization warded
5.9e-16 on 77 rows): family (17 rows: 11 ladder + 6 EXT3) RSV
min/med/max 3.19/7.03/12.06; median log10 shares S_const/S_M2/
S_dom = +0.01/+0.64/+0.26 -- THE RESERVE IS THE CONCENTRATION
DEPTH 1/(D pk) (S_M2 x S_dom med 8.5x), NOT the calibration
slack (B^2 > GSQ on 7/17 family rows -- the pure-algebra route
does not close, the r321 caveat restated) and NOT log factors
(none appear in the exact factorization).  MONOTONICITY: the
sealed bars stay SILENT -- rc_fam = -0.331 (FLAT letter; bins
(1.60, 5.72) (1.82, 4.39) (2.38, 3.19) (3.19, 3.46), argmin
bin 2, bin Spearman -0.80): the reserve mildly ERODES with
F_A on the measured family and the EXT4 rows continue that
trend (rsv ~ 1.1 at F_ins 5.5-6.7) -- the family is NOT
monotone-safe upward; safety comes only from the measured
D pk B^2 ceiling.
(3) LEG C -- THE DOMINANCE STRUCTURE IS REAL BUT MISSES THE
SEALED CONTRAST BAR: family med D = 1.79 (bar <= 2.5 MET), max
D = 2.13 at kz76 (bar <= 6.0 MET), six-sharp D = 1.07..2.06
(near-single-atom cubes, the record-derived expectation
confirmed); BUT med D(quiet) = 5.03 -> contrast 2.8x < the
sealed 3.0 -> DOM_OK False by the sealed letter.  The exact
chain rho_2 = D pk (F_A B)^2 and RSV = GSQ/(D pk B^2) is
warded to 9.3e-16, the r324 identity F_A medloc == pk to
1.6e-16, the r306 NORM identity (independent genealogy
recomputation) to 8.4e-16; on the 77 sealed rows the closing
inequality D pk B^2 <= GSQ/1.5 = 0.870 CLOSES with max 0.409
-- but the two EXT4 misses sit at D pk B^2 ~ 1.2: the
concentration ceiling is a CENSUS premise that the fresh deep
cohort already erodes.  Honest reading: the spike coverage IS
the r324 identity + near-dominance as MECHANISM (D never
exceeds 2.13 on any family row incl. EXT4), but neither the
sealed contrast bar nor a stable reserve floor certifies --
the theorem-grade letters stay unfired.
(4) LEG B -- HAND-OFF SEAMLESS + THE 13 EXCEPTIONS DISSOLVE ON
THE SEALED ROWS: every test row below F0 = 1.5 is heavy/good-
covered at (R_HAT, a = 1) (0 holes; boundary band [1.125, 2.0]
census 22 rows: BAND_LO all heavy-covered with RSV 3.8-10.0
headroom, BAND_HI carries both heavy- and third-covered rows);
the 13 r346 class-conditional exceptions are each covered by
the spike statement with reserves 3.2..12.1 -> 13/13 DISSOLVED
on the r346 cohort -- the two-statement reading of the sealed
51-row cover carries WITHOUT exceptions; the new holes live
strictly in the FRESH EXT4 cohort (kz111/kz75 at the sealed
reserve tier only, never at the raw-coverage tier).
(5) LEG D -- THE HONEST m_0*: uniform 10^22.6 UNCHANGED;
two-statement composite max(QUIET 10^16.1, SPIKE-side 10^22.6)
= 10^22.6 (the spike statement is the binding side through GSQ
F_Amax^2 (log m)^2, and F_Amax is now 6.68 out-of-sample);
V1 10^16.1 / V2 10^17.5 reprinted; vs r324 10^59.6, r306
census 10^13.5.  COFINAL TYPING: census = all freeze
constants, family reserves/D tables, the family F_A ceiling
(5.54 -> 6.68 OOS, UNSTABLE), the D pk B^2 ceiling (0.409 ->
~1.2 OOS); law candidates = the RAW class coverage (0 hard
violations on 23/23 family rows incl. fresh EXT4 -- the
strongest out-of-sample asset of the lane), P02 (r346), K1
(r346); missing = the family growth law m q_max <= C log m AND
a stable reserve floor -- the round REFUTES the hoped floor
1.5 honestly rather than certifying it.
(6) WORLDS (census, no letter): w9 F_ins 0.83 QUIET D 4.92 rsv
2.0; w13 1.09 QUIET 2.20/3.4; EPSTEIN 1.00 QUIET 4.42/3.5;
SCRAMBLE F_ins 2.00 SPIKE D 1.72 rsv 2.9 -- the class
statement COVERS SCRAMBLE: it is ARITHMETIC-FREE by
measurement (a pure concentration-size statement, no world
separation claimed; the r321 class-side rejection continues to
carry that load).
ANCHORS bit-near: r314 identity 4.5e-17 (EXT3 1.0e-16, EXT4
5.0e-17); r306 C_2 1.069 (0/57); r316 n 65 + rho quartet +
C_small 1.0694 @ kz18; dictionary 7.8e-16; r321 F_A top-3
2.47/2.39/2.38; THE r344 RECORD COMPLETE (curve + R_HAT 7/4 +
halves (8/5, 7/4) + C_H/C_G 3.9859/1.1409 + 0/51 at every grid
point at a = 1 + third-only 8 + EXT3-B 6/6 + F_Amax 5.54 +
m_0* 10^22.6); THE r346 RECORD (K1 index 1 CERT 6.8806 +
1.0151; K4 3.9859 + 0.4867 CERT viol 0 named 4/4; P02 39/39 +
12/12; V1 13 spikes [24, 53, 67, 98, 76, 61, 83, 51, 54, 123,
125, 42, 62] cap 1.39 rescue FAILS m_0* 10^16.1; V2 1.917 ->
10^17.5; six-spike set {42, 51, 53, 54, 62, 67} EXACT; ratios
kz51 0.19 / kz54 0.16 / kz42 0.29 / kz62 0.31).
SEAL: grid tilt 8.6e-16, part 4.0e-16, env 4.2e-16, hvy 0.0,
mart 2.2e-16/4.4e-16/1.2e-15, FRACTIONS pins 3/2 + 12/7 on
w9 + w13 EXACT (76 nodes), NORM identity 8.4e-16, r324
identity 1.6e-16, decomposition 8.8e-16, dominance chain
9.3e-16, purity clean (0 id + 0 literal hits on the five law
builders), toys exact (res_decomp pin 3, dominance 4/3, e3 pin
7/2 vs 28/27, e4 break 2, tree 6/6); must-fails e1
protocol-CAUGHT twice (AST rho + toy 0.5 != 1.5) / e2
protocol-CAUGHT twice (AST rho + toy 2.0 != 1.5) / e3 CAUGHT
twice (AST qm + Fractions pin 7/2 vs 28/27) / e4 CAUGHT exact
(break == 2) + m5a/m5b FLAGGED.  Runtime 329.5/334.4 s cal /
record run1/run2 identical up to WALL / 1.1 s smoke.
AMENDMENTS AFTER FREEZE: the disclosed print-level a1 above +
this record-table insertion; nothing else.

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
import fold_cover_canonization_probe as FCC    # noqa: E402 r346
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

# ---------------- the r344/r346 constant set, imported verbatim
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
FR_PIN_IDX = FTS.FR_PIN_IDX
ELIG_FRAC = FTS.ELIG_FRAC
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
N349_REF = FTS.N344_REF
R316_RHO = FTS.R316_RHO
R316_RHO_TOL = FTS.R316_RHO_TOL
R316_CSMALL = FTS.R316_CSMALL
R316_CSMALL_TOL = FTS.R316_CSMALL_TOL
R316_CSMALL_KZ = FTS.R316_CSMALL_KZ
R324_M0_L10 = FTS.R324_M0_L10
R306_M0_L10 = FTS.R306_M0_L10
R306_M0_TOL = FTS.R306_M0_TOL
R321_FA_TOP = FTS.R321_FA_TOP
R321_FA_TOL = FTS.R321_FA_TOL
# the r344 record anchors (FCC verbatim)
R344_HSH_CURVE = FCC.R344_HSH_CURVE
R344_SHR_CURVE = FCC.R344_SHR_CURVE
R344_WB_CURVE = FCC.R344_WB_CURVE
R344_EH_CURVE = FCC.R344_EH_CURVE
R344_EG_CURVE = FCC.R344_EG_CURVE
R344_CURVE_TOL_HSH = FCC.R344_CURVE_TOL_HSH
R344_CURVE_TOL_SHR = FCC.R344_CURVE_TOL_SHR
R344_CURVE_TOL_WB = FCC.R344_CURVE_TOL_WB
R344_CURVE_TOL_E = FCC.R344_CURVE_TOL_E
R344_EMPTYG = FCC.R344_EMPTYG
R344_EMPTYH = FCC.R344_EMPTYH
R344_JHAT = FCC.R344_JHAT
R344_HALVES = FCC.R344_HALVES
R344_CH1 = FCC.R344_CH1
R344_CG1 = FCC.R344_CG1
R344_C_TOL = FCC.R344_C_TOL
R344_AA = FCC.R344_AA
R344_THIRD_ONLY = FCC.R344_THIRD_ONLY
R344_FA_MAX = FCC.R344_FA_MAX
R344_FA_TOL = FCC.R344_FA_TOL
M0_R344 = FCC.M0_R344
M0_R344_TOL = FCC.M0_R344_TOL
GAMMA_CEIL = FCC.GAMMA_CEIL
HENV_IDX = FCC.HENV_IDX
FA_PCTL = FCC.FA_PCTL
PRED_TH = FCC.PRED_TH

# ---------------- NEW sealed constants of this round (spec above)
F0_SPLIT = FCC.FA_SPLIT
RHO_BAR = 1.5
BND_FAC = 4.0 / 3.0
NB_RES = 4
RC_MONO = 0.5
RC_FALL = -0.5
D_FAM_MED_BAR = 2.5
D_FAM_MAX_BAR = 6.0
DOM_CONTRAST = 3.0
EXT4_KZ = (72, 75, 66, 113, 111, 108)
EXT4_NW_MIN = 2656
EXT4_NW_MAX = 3181
TB_WARD_BAR_X4 = 1e-4
REC3_BAR_X4 = 1e-12
DEC_BAR = 1e-9
K1_IDX_REF = 1
K1_CH_REF = 6.8806
K1_CG_REF = 1.0151
K4_CH_REF = 3.9859
K4_CG_REF = 0.4867
R346_C_TOL = 0.001
P02_CORE_REF = 39
P02_OOS_REF = 12
V1_NSPK_REF = 13
V1_FAMQ_REF = 1.39
V1_FAMQ_TOL = 0.01
V1_M0_REF = 16.1
V2_CAP_REF = 1.917
V2_CAP_TOL = 0.005
V2_M0_REF = 17.5
M0_CLS_TOL = 0.2
SIX_KZ = (53, 67, 51, 54, 42, 62)
SIX_RATIO = {51: 0.19, 54: 0.16, 42: 0.29, 62: 0.31}
SIX_RATIO_TOL = 0.01

R349_TABLE_LITERALS = frozenset(FCC.R346_TABLE_LITERALS | {
    6.8806, 1.0151, 16.1, 17.5, 1.917})

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
    lies in the sealed r314..r346 record set."""
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
                            in R349_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source hygiene: the law
# ---------------- builders consume PASSED values, the F_A column
# ---------------- and SEALED thresholds only; the withheld
# ---------------- terminal drive key, the branch label, the cubic
# ---------------- target record and the q_max record identifiers
# ---------------- are forbidden (AST identifier scan + literal
# ---------------- scan).  The reserve and dominance diagnostics
# ---------------- themselves are TARGET-SIDE and are computed in
# ---------------- the gate section (r321 convention, disclosed).
def res_decomp(gsq, b2, pk, m2q, c3q):
    """THE EXACT RESERVE FACTORIZATION (derived algebra, spec):
    returns (S_const, S_M2, S_dom) = (gsq/b2, pk/m2q, pk m2q/c3q)
    whose product is EXACTLY gsq pk^2/(b2 c3q) = the sliding
    reserve GSQ F_A^2/rho_2 (via PhiH1 == (F_A B)^2).  Consumes
    the five passed values only; exact in Fractions."""
    s_const = gsq / b2
    s_m2 = pk / m2q
    s_dom = pk * m2q / c3q
    return s_const, s_m2, s_dom


def lower_env_min(fvals, vals, idx, nb):
    """the fit-free LOWER envelope: over EXACTLY the declared
    index tuple, sort by the coordinate, split into nb equal-count
    rank bins, per bin (median coordinate, MIN value); returns
    (bins, declared) -- the declared set is warded against the
    sealed family set."""
    idx = tuple(idx)
    o = sorted(idx, key=lambda i: float(fvals[i]))
    parts = np.array_split(np.arange(len(o)), nb)
    bins = []
    for p in parts:
        if len(p) == 0:
            continue
        mem = [o[int(k)] for k in p]
        bins.append((float(np.median([float(fvals[i])
                                      for i in mem])),
                     min(float(vals[i]) for i in mem)))
    return bins, idx


def bnd_rule(fv, f0, fac):
    """the sealed boundary-band letter: BELOW iff fv < f0/fac;
    BAND_LO iff f0/fac <= fv < f0; BAND_HI iff f0 <= fv <=
    f0 x fac (boundary inclusive on the family side); ABOVE
    else.  Consumes the value + sealed thresholds only."""
    if fv < f0 / fac:
        return "BELOW"
    if fv < f0:
        return "BAND_LO"
    if fv <= f0 * fac:
        return "BAND_HI"
    return "ABOVE"


def law_tree_verdict(leak, brk, cert, hand, dom, mono):
    """the sealed main-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    LAW_STATE_NOT_EXACT > THIRDARM_LAW_DERIVED >
    CLASS_THEOREM_CERTIFIED > RESERVE_ACCIDENTAL >
    EXCEPTIONS_REMAIN."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if cert and hand and dom:
        return "THIRDARM_LAW_DERIVED"
    if cert and hand and mono:
        return "CLASS_THEOREM_CERTIFIED"
    if cert and hand:
        return "RESERVE_ACCIDENTAL"
    return "EXCEPTIONS_REMAIN"


def fr_decomp_toy():
    """the sealed Fractions decomposition pin (by hand, spec):
    q = (1/2, 1/3, 1/6): pk = 1/2, m2q = 7/18, c3q = 1/6; with
    gsq = 2, b2 = 1: S = (2, 9/7, 7/6), product 3 EXACT ==
    gsq pk^2/(b2 c3q).  Returns worst deviation (0 demanded)."""
    pk = Fr(1, 2)
    m2q = Fr(1, 4) + Fr(1, 9) + Fr(1, 36)
    c3q = Fr(1, 8) + Fr(1, 27) + Fr(1, 216)
    sc, sm, sd = res_decomp(Fr(2), Fr(1), pk, m2q, c3q)
    devs = [abs(sc - Fr(2)), abs(sm - Fr(9, 7)),
            abs(sd - Fr(7, 6)),
            abs(sc * sm * sd - Fr(3)),
            abs(sc * sm * sd
                - Fr(2) * pk * pk / (Fr(1) * c3q))]
    return max(devs)


def mutant_reserve_bar_posthoc(rho, fa2b):
    """e1 MUST-FAIL MUTANT (protocol): the reserve bar set at the
    SEEN minimum reserve (consumes rho) -- the BOUND_FORBIDDEN
    scope audit must FLAG it AND on the sealed toy it returns
    0.5 != the sealed RHO_BAR."""
    return min(fa2b[i] / max(rho[i], 1e-300)
               for i in range(len(rho)))


def mutant_f0_posthoc(rho, fvals, gsq, cands):
    """e2 MUST-FAIL MUTANT (protocol): the family threshold
    re-picked to minimize the seen violations (consumes rho) --
    AST-FLAGGED and on the sealed toy returns 2.0 != the sealed
    F0_SPLIT."""
    best = None
    bestv = None
    for c in cands:
        v = sum(1 for i in range(len(rho))
                if fvals[i] >= c
                and rho[i] > gsq * fvals[i] ** 2)
        if bestv is None or v < bestv:
            best = c
            bestv = v
    return best


def mutant_dom_circular(mqs_rec, c3q):
    """e3 MUST-FAIL MUTANT: a 'dominance ratio' consuming the
    q_max RECORD column (stale, circular) instead of recomputing
    from the same block vector -- the QMAX_FORBIDDEN scope audit
    must FLAG it AND on the sealed Fractions toy it returns 7/2
    while the true dominance is 28/27."""
    stale = mqs_rec["qm"]
    return c3q / stale ** 3


def mutant_chain_wrong_log(mm, c3q, ell):
    """e4 MUST-FAIL MUTANT: the chain with the WRONG log power
    (rho_2 = m^2 c3q/lg instead of /lg^2) -- on the sealed
    Fractions toy it returns 3/4 while the exact chain gives 3/8
    (break factor == lg EXACT)."""
    return mm * mm * c3q / ell


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'law orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'class constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("thirdarm_spike_law_probe -- PRIME.L2.THIRDARM_LAW.01 "
          "(round 349,")
    print("the third-arm coverage of the spike family as a law)")
    print("SPEC_SHA %s   R346_SHA %s   R344_SHA %s   R329_SHA %s"
          % (SPEC_SHA[:16], FCC.SPEC_SHA[:16], FTS.SPEC_SHA[:16],
             EFA.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + grid path wards + w9 "
                        "Fractions pins + e1-e4; ladder, "
                        "extensions, EXT3, EXT4, anchors, "
                        "coverage, anatomy, class census, "
                        "dominance, composition and adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE THIRD-ARM LAW ROUND (the named r346 residue): on "
          "the SEALED r346 cover (grid %s, third arm = banked "
          "r321 %.4f F_A^2) the spike-family coverage is "
          "adjudicated as a LAW with sealed machinery: LEG A "
          "reserve factorization RSV = (GSQ/B^2)(pk/M2q)"
          "(pk M2q/c3q) + monotonicity (RC bars %.1f/%.1f, "
          "NB_RES %d); LEG B class statement F_A >= %.1f -> "
          "rho_2 <= GSQ F_A^2 with reserve >= %.1f on 65 + 12 + "
          "6 rows, boundary band factor %.3f, hand-off at the "
          "r346 cover point; LEG C dominance D = c3q/pk^3 with "
          "bars med <= %.1f, max <= %.1f, contrast >= %.1f; "
          "verdict tree THIRDARM_LAW_DERIVED / "
          "CLASS_THEOREM_CERTIFIED / RESERVE_ACCIDENTAL / "
          "EXCEPTIONS_REMAIN / LAW_STATE_NOT_EXACT / TARGET_LEAK "
          "+ flags sealed BEFORE evaluation"
          % (str(tuple(round(r, 4) for r in R_GRID)), GSQ_R321,
             RC_MONO, RC_FALL, NB_RES, F0_SPLIT, RHO_BAR,
             BND_FAC, D_FAM_MED_BAR, D_FAM_MAX_BAR,
             DOM_CONTRAST))
    frag = antigate_fragment_audit()
    own_builders = ("res_decomp", "lower_env_min", "bnd_rule",
                    "law_tree_verdict", "fr_decomp_toy")
    sc_own = []
    for fn in own_builders:
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the module-own law "
          "builders clean vs BOUND_FORBIDDEN + PHI3_FORBIDDEN + "
          "QMAX_FORBIDDEN (%d hits) -- the law side consumes "
          "passed values + the F_A column + sealed thresholds "
          "ONLY; m5a gift-bound FLAGGED (%s); m5b branch-peek "
          "FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r344/r346 verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3 + EXT4")
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
        ext4 = []
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
        ext4 = [BH.wpack(kz) for kz in EXT4_KZ]
        ext4.sort(key=lambda p: (p["N"], p["kz"]))
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
        check("G14-ext3-admission", True, "SMOKE: skipped")
        check("G15-ext4-admission", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext)
              and len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d); EXT2 (r316 A5 rule verbatim): "
              "%d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1], len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))
        check("G14-ext3-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX,
              "EXT3 = the sealed r329 RECORD selection (r335/"
              "r339/r341/r344/r346 adoption verbatim): 12 "
              "anchors (B %s + A %s), POSITIVE_PREFIX %d/12, "
              "N_w %d..%d (record %d..%d) -- PURE TEST rows"
              % (str(EXT3_KZ_B), str(EXT3_KZ_A),
                 sum(1 for p in ext3 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3),
                 EXT3_NW_MIN, EXT3_NW_MAX))
        ext4_admit = [p for p in ext4 if p["nf"] is None]
        ext4_drop = [(p["kz"], p["nf"]) for p in ext4
                     if p["nf"] is not None]
        check("G15-ext4-admission",
              len(ext4) == 6
              and min(p["N"] for p in ext4) == EXT4_NW_MIN
              and max(p["N"] for p in ext4) == EXT4_NW_MAX,
              "EXT4 = the sealed r343/r345 L*-lane fresh list "
              "%s adopted as-is (PURE TEST rows of THIS round, "
              "never seen by any cubic-lane calibration): N_w "
              "%d..%d (record %d..%d); POSITIVE_PREFIX admitted "
              "%d/6%s"
              % (str(EXT4_KZ), min(p["N"] for p in ext4),
                 max(p["N"] for p in ext4), EXT4_NW_MIN,
                 EXT4_NW_MAX, len(ext4_admit),
                 ("; DROPPED (census, sealed admission): %s"
                  % str(ext4_drop)) if ext4_drop else ""))
        ext4 = ext4_admit

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
    x4recs = [rung_rec(p) for p in ext4] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs + e2recs + x3recs + x4recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 + x4recs if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2+EXT3+EXT4 census: %d cheap / %d "
              "exception %s"
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
    tb_x4 = 0.0
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
    for rc in x4recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x4 = max(tb_x4, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_x3 <= TB_WARD_BAR_X3
          and tb_x4 <= TB_WARD_BAR_X4
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d ext3 + %d ext4 + %d mains + 3 controls: worst "
          "dev/absmass %.1e main N<=%d (bar %.0e) / %.1e deep / "
          "%.1e ext+ext2 (bar %.0e) / %.1e ext3 (bar %.0e) / "
          "%.1e ext4 (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(x3recs),
             len(x4recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, tb_ext, TB_WARD_BAR_DEEP,
             tb_x3, TB_WARD_BAR_X3, tb_x4, TB_WARD_BAR_X4,
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

    all_rc = recs + mrecs + erecs + e2recs + x3recs + x4recs
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
    x34_mult_ok = True
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
    for rc in x3recs + x4recs:
        if rc["ev"]["mx_mult"] > MULT_CAP:
            x34_mult_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and x34_mult_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r327 GMC ledger segments IDENTICALLY to the genealogy "
          "(worst dev %.1e, bar %.0e); EXT3+EXT4 fold "
          "multiplicity <= %d (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP, "OK" if x34_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim set)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim: r306/r316 + "
            "dictionary + r321 F_A; the full r344/r346 record "
            "follows in S5)")
    x34_ids = set(id(rc) for rc in x3recs + x4recs)
    live_69 = [rc for rc in live if id(rc) not in x34_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    rec3_x4 = max((rc["ev"]["rec3"] for rc in x4recs),
                  default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and rec3_x4 <= REC3_BAR_X4,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e (bars %.0e); "
          "EXT3 %.1e (bar %.0e); EXT4 %.1e (bar %.0e); DISCLOSED "
          "slim anchor set -- the full chain is re-warded by the "
          "sealed r321..r346 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, REC3_BAR_X3,
             rec3_x4, REC3_BAR_X4))
    if smoke:
        ev9s = recs[0]["ev"]
        pb0 = ev9s["pbg"][R_STAR_IDX]
        info("SMOKE: w9 m %d K %d E3 %.4f grid hsh %s"
             % (ev9s["m"], pb0["kk"], pb0["e3"],
                str([round(p["hsh"], 3) for p in ev9s["pbg"]])))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        srt = []
        n349 = 0
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
        n349 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n349)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n349 == N349_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n349, N349_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
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
        check("G39-r321-fa-anchors", True, "SMOKE: skipped")
    else:
        srt_x = sorted(x3recs, key=lambda rc: (rc["N"], rc["kz"]))
        srt_x = [rc for rc in srt_x
                 if rc["ev"]["mx_mult"] <= MULT_CAP
                 and not rc["ev"]["degenerate"]]
        srt_x4 = sorted(x4recs,
                        key=lambda rc: (rc["N"], rc["kz"]))
        srt_x4 = [rc for rc in srt_x4
                  if rc["ev"]["mx_mult"] <= MULT_CAP
                  and not rc["ev"]["degenerate"]]
        n_x3 = len(srt_x)
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        lg_full = [math.log(float(v)) for v in m_full]
        q_lad = [srt[i]["ev"]["mqs"]["qm"] for i in range(n349)]
        fa_lad = EFP.local_ratio(q_lad)
        medloc_lad = CCP.local_median(q_lad)
        N_lad = [srt[i]["N"] for i in range(n349)]
        fa_full = list(fa_lad)
        for rc in srt_x:
            fa_full.append(CCP.world_coord(rc["ev"]["mqs"]["qm"],
                                           rc["N"], N_lad, q_lad))
        fa_kz = {srt_full[i]["kz"]: fa_full[i]
                 for i in range(n_full)}
        kz_rank = {rc["kz"]: i for i, rc in enumerate(srt_full)}
        fa_x4 = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_x4]
        check("G39-r321-fa-anchors",
              all(abs(fa_kz[kz] - R321_FA_TOP[kz]) <= R321_FA_TOL
                  for kz in R321_FA_TOP),
              "the r321/r317 F_A coordinate reproduced through "
              "EFP.local_ratio on the module-own q_max column: "
              "top-3 kz53 %.2f / kz83 %.2f / kz67 %.2f (rec "
              "%.2f/%.2f/%.2f tol %.2f); EXT3 + EXT4 rows via "
              "the r321 INSERTION RULE (CCP.world_coord, the "
              "r329/r344 convention); F_A range full "
              "%.2f..%.2f, EXT4 %.2f..%.2f; the third-arm "
              "constant GSQ = %.4f is the BANKED r321 record, "
              "never recalibrated here"
              % (fa_kz[53], fa_kz[83], fa_kz[67],
                 R321_FA_TOP[53], R321_FA_TOP[83],
                 R321_FA_TOP[67], R321_FA_TOL, min(fa_full),
                 max(fa_full),
                 min(fa_x4) if fa_x4 else 0.0,
                 max(fa_x4) if fa_x4 else 0.0, GSQ_R321))

    # ---------------- S4: seal + purity + toys + live wards
    section("S4  LEG 0b -- SEAL + PURITY + TOYS + LIVE WARDS")
    pure_lits = []
    for fn in own_builders:
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_reserve_bar_posthoc",
                          BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_f0_posthoc", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_dom_circular", QMAX_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e3_hits) >= 1,
          "SOURCE HYGIENE: the law builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed "
          "r314..r346 record-literal set (%d literal hits); e1 "
          "reserve-bar-posthoc FLAGGED (%s); e2 f0-posthoc "
          "FLAGGED (%s); e3 dom-circular FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    # sealed toys (Fractions + by-hand pins, spec above)
    fd_dev = fr_decomp_toy()
    toy_dom_a = (Fr(1, 8) + Fr(1, 27) + Fr(1, 216)) / Fr(1, 2) ** 3
    toy_dom_b = Fr(1) / Fr(1) ** 3
    mut3 = mutant_dom_circular(dict(qm=Fr(1, 2)),
                               Fr(27, 64) + Fr(1, 64))
    dom3_true = (Fr(27, 64) + Fr(1, 64)) / Fr(3, 4) ** 3
    mut4 = mutant_chain_wrong_log(Fr(3), Fr(1, 6), Fr(2))
    chain4_true = Fr(3) ** 2 * Fr(1, 6) / Fr(2) ** 2
    mut1 = mutant_reserve_bar_posthoc((2.0, 1.0), (1.0, 3.0))
    mut2 = mutant_f0_posthoc((10.0, 1.0), (1.6, 2.5), 1.0,
                             (1.0, 1.5, 2.0))
    toy_bnd = (bnd_rule(0.5, F0_SPLIT, BND_FAC),
               bnd_rule(1.2, F0_SPLIT, BND_FAC),
               bnd_rule(1.6, F0_SPLIT, BND_FAC),
               bnd_rule(1.5, F0_SPLIT, BND_FAC),
               bnd_rule(2.5, F0_SPLIT, BND_FAC))
    env_r, dec_r = lower_env_min((1.0, 2.0, 3.0, 4.0),
                                 (1.0, 2.0, 3.0, 4.0),
                                 (0, 1, 2, 3), 2)
    env_f, _ = lower_env_min((1.0, 2.0, 3.0, 4.0),
                             (4.0, 3.0, 2.0, 1.0),
                             (0, 1, 2, 3), 2)
    rc_r = CCP.spearman_rank([b[0] for b in env_r],
                             [b[1] for b in env_r])
    rc_f = CCP.spearman_rank([b[0] for b in env_f],
                             [b[1] for b in env_f])
    tr_br = (law_tree_verdict(True, True, True, True, True, True),
             law_tree_verdict(False, True, True, True, True,
                              True),
             law_tree_verdict(False, False, True, True, True,
                              False),
             law_tree_verdict(False, False, True, True, False,
                              True),
             law_tree_verdict(False, False, True, True, False,
                              False),
             law_tree_verdict(False, False, False, True, True,
                              True))
    ok_tr = tr_br == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                      "THIRDARM_LAW_DERIVED",
                      "CLASS_THEOREM_CERTIFIED",
                      "RESERVE_ACCIDENTAL", "EXCEPTIONS_REMAIN")
    check("G41-toy-exactness",
          fd_dev == 0
          and toy_dom_a == Fr(4, 3) and toy_dom_b == 1
          and mut3 == Fr(7, 2) and dom3_true == Fr(28, 27)
          and mut3 != dom3_true
          and mut4 == Fr(3, 4) and chain4_true == Fr(3, 8)
          and mut4 / chain4_true == Fr(2)
          and abs(mut1 - 0.5) <= TOY_BAR and mut1 != RHO_BAR
          and mut2 == 2.0 and mut2 != F0_SPLIT
          and toy_bnd == ("BELOW", "BAND_LO", "BAND_HI",
                          "BAND_HI", "ABOVE")
          and env_r[0][1] == 1.0 and env_f[0][1] == 3.0
          and abs(rc_r - 1.0) <= TOY_BAR
          and abs(rc_f + 1.0) <= TOY_BAR
          and dec_r == (0, 1, 2, 3)
          and ok_tr,
          "the sealed toys EXACT: res_decomp Fractions pin "
          "(2, 9/7, 7/6) product 3 dev %s; dominance toys 4/3 "
          "and 1; e3 circular pin %s != true %s; e4 wrong-log "
          "pin %s != true %s (break factor %s == lg); e1 toy "
          "%.1f != sealed %.1f; e2 toy %.1f != sealed %.1f; "
          "boundary toys %s; lower-envelope rising/falling "
          "Spearman %+.0f/%+.0f with declared set warded; the "
          "six verdict-tree branches EXACT %s"
          % (str(fd_dev), str(mut3), str(dom3_true), str(mut4),
             str(chain4_true), str(mut4 / chain4_true), mut1,
             RHO_BAR, mut2, F0_SPLIT, str(toy_bnd), rc_r, rc_f,
             str(tr_br)))
    # live grid wards (r344/r346 verbatim, slim print)
    tilt_w = wqd_w = part_w3 = bkd_w = env_w = pgi_w = hvy_w = 0.0
    e3d_w = 0.0
    mart_w = unit_w = rec_w = jen_w = 0.0
    chain_w = xw_cube = 0.0
    nz_tot = 0
    mult_all_ok = True
    brk_lo_w = 0.0
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
        brk_lo_w = max(brk_lo_w,
                       max(0.0, ev["mqs"]["qm"] * trs["phiH1"]
                           - ev["rho2"])
                       / max(ev["rho2"], 1e-300))
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
    # THE ROUND'S OWN EXACT WARDS: the r306 NORM identity
    # (independent S3/L1^3 recomputation), the r321 bracket lower
    # side, the r324 identity on the ladder, the reserve
    # decomposition + dominance chain on every live world.
    norm_w = 0.0
    dec_w = 0.0
    chainD_w = 0.0
    id324_w = 0.0
    for rc in live:
        ev = rc["ev"]
        mloc = ev["m"]
        lgl = math.log(float(mloc))
        ax_i = np.abs(ev["sct"]["x"])
        Lx_i = float(np.sum(ax_i))
        c3q_i = float(np.sum(ax_i ** 3)) / max(Lx_i ** 3, 1e-300)
        norm_w = max(norm_w,
                     abs(ev["rho2"] * lgl ** 2 / mloc ** 2
                         - c3q_i) / max(c3q_i, 1e-300))
        pk_i = ev["mqs"]["qm"]
        m2q_i = ev["mqs"]["m2"] / float(mloc)
        if pk_i <= 0.0 or c3q_i <= 0.0:
            continue
        dd_i = c3q_i / pk_i ** 3
        # reserve decomposition vs the direct sliding reserve at
        # a NEUTRAL coordinate (F = 1, B^2 = (pk m/lg)^2): the
        # decomposition identity is coordinate-free.
        b2_i = (pk_i * mloc / lgl) ** 2
        sc_i, sm_i2, sd_i = res_decomp(GSQ_R321, b2_i, pk_i,
                                       m2q_i, c3q_i)
        rsv_dir = GSQ_R321 * 1.0 / max(ev["rho2"], 1e-300)
        dec_w = max(dec_w,
                    abs(sc_i * sm_i2 * sd_i - rsv_dir)
                    / max(rsv_dir, 1e-300))
        chainD_w = max(chainD_w,
                       abs(dd_i * pk_i ** 3 * mloc ** 2
                           / lgl ** 2 - ev["rho2"])
                       / max(ev["rho2"], 1e-300))
    if not smoke:
        for i in range(n349):
            id324_w = max(id324_w,
                          abs(fa_lad[i] * medloc_lad[i] - q_lad[i])
                          / max(q_lad[i], 1e-300))
    check("G42-live-grid-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and brk_lo_w <= CHAIN_BAR
          and mart_w <= TREE_BAR and unit_w <= TREE_BAR
          and rec_w <= TREE_BAR and jen_w <= JEN_BAR
          and tilt_w <= TILT_BAR and wqd_w <= WQ_BAR
          and part_w3 <= PART_BAR and bkd_w <= BK_BAR
          and env_w <= ENV_BAR and pgi_w <= PGI_BAR
          and hvy_w <= HVY_BAR and e3d_w <= DICT_BAR
          and fr_ok and nz_tot == 0 and mult_all_ok
          and norm_w <= DEC_BAR and dec_w <= DEC_BAR
          and chainD_w <= DEC_BAR and id324_w <= CHAIN_BAR,
          "the FULL r341/r344 exact path layer live at EVERY "
          "sealed grid R on %d live worlds: tilt %.1e, weight "
          "norm %.1e, partition %.1e, B-chain %.1e, envelope "
          "%.1e, Phi-Gamma %.1e, heavy hand-off %.1e, E3 == d3 "
          "%.1e; martingale %.1e/%.1e/%.1e, Jensen %.1e; r316 "
          "chain %.1e + bracket lower side %.1e; FRACTIONS "
          "BIT-EQUALITY at pins 3/2 + 12/7 on the mains: %s (%d "
          "nodes); THE ROUND'S OWN EXACT WARDS: r306 NORM "
          "identity (independent genealogy sum|x|^3/L^3) %.1e, "
          "reserve "
          "decomposition %.1e, dominance chain rho_2 == D pk^3 "
          "m^2/lg^2 %.1e (bars %.0e), r324 identity F_A medloc "
          "== pk on the ladder %.1e"
          % (len(live), tilt_w, wqd_w, part_w3, bkd_w, env_w,
             pgi_w, hvy_w, e3d_w, mart_w, unit_w, rec_w, jen_w,
             chain_w, brk_lo_w,
             "EXACT" if fr_ok else "BROKEN", fr_nodes, norm_w,
             dec_w, chainD_w, DEC_BAR, id324_w))

    # ---------------- S5: the r344/r346 record reproduction
    section("S5  LEG 0c -- THE r344 COVER + THE r346 RECORD "
            "(SAME CODE PATH)")

    def solve_m0(log_rhs):
        t = math.log(73.0)
        while t < 1e7:
            if CRIT_EXP * t >= log_rhs(t):
                return t / math.log(10.0)
            t *= 1.02
        return None

    if smoke:
        check("G50-r344-balance-record", True, "SMOKE: skipped")
        check("G51-r344-cover-record", True, "SMOKE: skipped")
        check("G52-r346-predictor-record", True, "SMOKE: skipped")
        check("G53-r346-class-record", True, "SMOKE: skipped")
        check("G54-r346-six-spikes", True, "SMOKE: skipped")
        check("G55-r346-k1-k4", True, "SMOKE: skipped")
    else:
        te_x = list(te_i) + list(range(n349, n_full))
        e3_col = [rc["ev"]["pbg"][R_STAR_IDX]["e3"]
                  for rc in srt_full]
        named_rank = {}
        for kz in NAMED_KZ + MIDBAND_KZ:
            named_rank[kz] = kz_rank[kz]
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
              "same code path: hsh med %s, share med %s, W_B "
              "med %s, empty-good %s, empty-heavy %s; e_H %s, "
              "e_G %s; R_HAT = %.4f (index %d, rec %d), halves "
              "(%s, %s) (rec %s) -> NOT halves-stable, the r344 "
              "instability reproduced"
              % (str([round(v, 3) for v in hsh_meds]),
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
        third_ok = [srt_full[i]["ev"]["rho2"]
                    <= GSQ_R321 * fa_full[i] ** 2
                    for i in range(n_full)]
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
        pa_hat = cover_by_r[j_hat]["per_a"][R344_AA]
        fa_max = max(fa_full)
        i51 = kz_rank[51]
        x3b_third = sum(1 for kz in EXT3_KZ_B
                        if third_ok[kz_rank[kz]])
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
              "kz51 insertion (rec %.2f); composed m_0* 10^%.1f "
              "(rec 10^%.1f)"
              % (R344_AA, R_GRID[j_hat], CHs0, R344_CH1, CGs0,
                 R344_CG1, pa_hat["third_used"],
                 R344_THIRD_ONLY, x3b_third, fa_max,
                 R344_FA_MAX,
                 m0_r344 if m0_r344 is not None else -1.0,
                 M0_R344))
        # the r346 P02 predictor record (fa feature only)
        core_rows = list(te_i)
        x3_rows = list(range(n349, n_full))

        def p02_acc(rows):
            good = 0
            for i in rows:
                p = FCC.pred_rule(2, dict(fa=fa_full[i]),
                                  PRED_TH)
                ok_i = (pa_hat["covH"][i] if p == "H"
                        else third_ok[i])
                if ok_i:
                    good += 1
            return good
        p02_core = p02_acc(core_rows)
        p02_x3 = p02_acc(x3_rows)
        check("G52-r346-predictor-record",
              p02_core == P02_CORE_REF and p02_x3 == P02_OOS_REF,
              "THE r346 P02 RECORD reproduced: P02 (F_A >= %.1f "
              "-> third arm, else heavy) predicts a covering "
              "arm on core %d/%d (rec %d) + EXT3 OUT-OF-SAMPLE "
              "%d/%d (rec %d) = full %d/51 -- the working "
              "partition is SPIKE-VS-REST in F_A"
              % (F0_SPLIT, p02_core, len(core_rows),
                 P02_CORE_REF, p02_x3, len(x3_rows), P02_OOS_REF,
                 p02_core + p02_x3))
        # the r346 V1/V2 class-conditional record
        lab = ["H" if pa_hat["covH"][i] else
               ("G" if pa_hat["covG"][i] else
                ("T" if third_ok[i] else "-"))
               for i in range(n_full)]

        def defuse_variant(split_val, strict):
            spk = [i for i in range(n_full)
                   if (fa_full[i] > split_val if strict
                       else FCC.cls_rule(fa_full[i], split_val)
                       == "SPIKE")]
            spk_set = set(spk)
            fam_q = max((fa_full[i] for i in range(n_full)
                         if i not in spk_set), default=0.0)
            rescue = {}
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
            rescue_ok = all(v is not None
                            for v in rescue.values())

            def rhs_gen(t):
                return (CHs0 + CGs0) * t \
                    + GSQ_R321 * fam_q ** 2 * t ** 2
            m0_gen = solve_m0(lambda t: math.log(
                max(rhs_gen(t), 1e-300)))
            spk_kz = [(srt_full[i]["kz"], round(fa_full[i], 2),
                       lab[i]) for i in spk if i in set(te_x)]
            return dict(spk=spk, fam_q=fam_q,
                        rescue_ok=rescue_ok, m0_gen=m0_gen,
                        spk_kz=spk_kz)
        v1 = defuse_variant(F0_SPLIT, False)
        cap2 = float(np.percentile(np.asarray(fa_full), FA_PCTL))
        v2 = defuse_variant(cap2, True)
        check("G53-r346-class-record",
              len(v1["spk_kz"]) == V1_NSPK_REF
              and abs(v1["fam_q"] - V1_FAMQ_REF) <= V1_FAMQ_TOL
              and (not v1["rescue_ok"])
              and abs(v1["m0_gen"] - V1_M0_REF) <= M0_CLS_TOL
              and abs(cap2 - V2_CAP_REF) <= V2_CAP_TOL
              and (not v2["rescue_ok"])
              and abs(v2["m0_gen"] - V2_M0_REF) <= M0_CLS_TOL,
              "THE r346 CLASS RECORD reproduced: V1 test-row "
              "spike family %d rows (rec %d) %s; QUIET cap %.2f "
              "(rec %.2f); uniform rescue FAILS (rec: fails); "
              "m_0*(class) 10^%.1f (rec 10^%.1f); V2 cap P%d = "
              "%.3f (rec %.3f), rescue FAILS, 10^%.1f (rec "
              "10^%.1f)"
              % (len(v1["spk_kz"]), V1_NSPK_REF,
                 str([t[0] for t in v1["spk_kz"]]), v1["fam_q"],
                 V1_FAMQ_REF, v1["m0_gen"], V1_M0_REF,
                 int(FA_PCTL), cap2, V2_CAP_REF, v2["m0_gen"],
                 V2_M0_REF))
        # the six sharp spikes: only-third at EVERY a
        only_third_every_a = []
        for i in te_x:
            if all((not cover_by_r[j_hat]["per_a"][a]["covH"][i])
                   and (not cover_by_r[j_hat]["per_a"][a]
                        ["covG"][i])
                   and third_ok[i] for a in GA_FAM):
                only_third_every_a.append(srt_full[i]["kz"])
        six_set_ok = (tuple(sorted(only_third_every_a))
                      == tuple(sorted(SIX_KZ)))
        ratio_ok = True
        ratio_txt = []
        for kz in SIX_RATIO:
            i = kz_rank[kz]
            rat = srt_full[i]["ev"]["rho2"] \
                / (GSQ_R321 * fa_full[i] ** 2)
            ratio_txt.append("kz%d %.2f" % (kz, rat))
            if abs(rat - SIX_RATIO[kz]) > SIX_RATIO_TOL:
                ratio_ok = False
        check("G54-r346-six-spikes", six_set_ok and ratio_ok,
              "THE SIX SHARP SPIKES reproduced: only-third-"
              "covered at EVERY a in %s == %s (rec %s); the "
              "r344 third-arm ratios %s (rec %s tol %.2f) -- "
              "the r329 out-of-sample reserves restated under "
              "the insertion convention"
              % (str(GA_FAM), str(sorted(only_third_every_a)),
                 str(sorted(SIX_KZ)), "; ".join(ratio_txt),
                 str(SIX_RATIO), SIX_RATIO_TOL))
        # K1 + K4 (r346 canonization anchors, FCC verbatim)
        k1_j, ralg = FCC.rhat_intrinsic(R_GRID, GAMMA_CEIL)
        k1_cert = cover_by_r[k1_j]["aa"] is not None
        pa_k1 = cover_by_r[k1_j]["per_a"][R344_AA]
        hb_env = FCC.env_min_col([cols_by_r[j]["hb"]
                                  for j in range(len(R_GRID))],
                                 HENV_IDX)
        wb_env = FCC.env_min_col([cols_by_r[j]["wb"]
                                  for j in range(len(R_GRID))],
                                 tuple(range(len(R_GRID))))
        CHe = max(hb_env[i] / lg_full[i] ** R344_AA
                  for i in ca_i)
        CGe = max(wb_env[i] / lg_full[i] ** R344_AA
                  for i in ca_i)
        covHe = [e3_col[i] <= CHe * lg_full[i] ** R344_AA
                 for i in range(n_full)]
        covGe = [e3_col[i] <= CGe * lg_full[i] ** R344_AA
                 for i in range(n_full)]
        viole = [i for i in te_x
                 if not (covHe[i] or covGe[i] or third_ok[i])]
        namede = sum(1 for kz in NAMED_KZ
                     if covHe[named_rank[kz]]
                     or covGe[named_rank[kz]]
                     or third_ok[named_rank[kz]])
        k4_cert = (not viole) and namede == len(NAMED_KZ) \
            and CHe < CERT_GUARD and CGe < CERT_GUARD
        check("G55-r346-k1-k4",
              k1_j == K1_IDX_REF and k1_cert
              and abs(pa_k1["CH"] - K1_CH_REF) <= R346_C_TOL
              and abs(pa_k1["CG"] - K1_CG_REF) <= R346_C_TOL
              and k4_cert
              and abs(CHe - K4_CH_REF) <= R346_C_TOL
              and abs(CGe - K4_CG_REF) <= R346_C_TOL,
              "THE r346 CANONIZATION RECORD reproduced: K1 "
              "(R_ALG = %.4f) picks grid index %d (rec %d), "
              "CERTIFIES at a = %d with C %.4f + %.4f (rec "
              "%.4f + %.4f); K4 R-free envelope CERTIFIES at "
              "a = %d with C_H_ENV %.4f + C_G_ENV %.4f (rec "
              "%.4f + %.4f, viol %d, named %d/4)"
              % (ralg, k1_j, K1_IDX_REF, R344_AA, pa_k1["CH"],
                 pa_k1["CG"], K1_CH_REF, K1_CG_REF, R344_AA,
                 CHe, CGe, K4_CH_REF, K4_CG_REF, len(viole),
                 namede))

    # ---------------- S6: Leg A -- the reserve anatomy
    section("S6  LEG A -- THE RESERVE ANATOMY OF THE SLIDING "
            "COVERAGE")
    if smoke:
        check("G60-reserve-table", True, "SMOKE: skipped")
        check("G61-reserve-monotonicity", True, "SMOKE: skipped")
        check("G62-reserve-source-census", True,
              "SMOKE: skipped")
        rc_fam = 0.0
        mono_ok = False
        fall_flag = False
    else:
        # the full-row diagnostic columns (target-side, disclosed)
        pk_col = []
        m2q_col = []
        c3q_col = []
        dd_col = []
        bb_col = []
        rsv_col = []
        dec_worst = 0.0
        for i in range(n_full):
            ev = srt_full[i]["ev"]
            mloc = ev["m"]
            lgl = lg_full[i]
            pk = ev["mqs"]["qm"]
            m2q = ev["mqs"]["m2"] / float(mloc)
            c3q = ev["cm"]["S3"]
            dd = c3q / max(pk ** 3, 1e-300)
            bb = pk * mloc / (max(fa_full[i], 1e-300) * lgl)
            rsv = GSQ_R321 * fa_full[i] ** 2 \
                / max(ev["rho2"], 1e-300)
            sc_i, sm_i2, sd_i = res_decomp(GSQ_R321, bb * bb,
                                           pk, m2q, c3q)
            dec_worst = max(dec_worst,
                            abs(sc_i * sm_i2 * sd_i - rsv)
                            / max(rsv, 1e-300))
            pk_col.append(pk)
            m2q_col.append(m2q)
            c3q_col.append(c3q)
            dd_col.append(dd)
            bb_col.append(bb)
            rsv_col.append(rsv)
        fam_idx = [i for i in range(n_full)
                   if FCC.cls_rule(fa_full[i], F0_SPLIT)
                   == "SPIKE"]
        quiet_idx = [i for i in range(n_full)
                     if i not in set(fam_idx)]
        grel_full = EFA.grel_col([rc["kz"] for rc in srt_full],
                                 core.G_ALL)
        info("THE FAMILY TABLE (F_A >= %.1f; kz gap-class F_A "
             "pk B D | S_const S_M2 S_dom | RSV):" % F0_SPLIT)
        for i in sorted(fam_idx, key=lambda i: -fa_full[i]):
            sc_i, sm_i2, sd_i = res_decomp(
                GSQ_R321, bb_col[i] ** 2, pk_col[i], m2q_col[i],
                c3q_col[i])
            info("  kz%-4d %-5s F_A %5.2f pk %.4f B %.3f D "
                 "%5.2f | %.3f x %.3f x %.3f | RSV %6.2f %s"
                 % (srt_full[i]["kz"],
                    EFA.gap_class(grel_full[i]), fa_full[i],
                    pk_col[i], bb_col[i], dd_col[i], sc_i,
                    sm_i2, sd_i, rsv_col[i],
                    "(EXT3)" if i >= n349 else ""))
        check("G60-reserve-table", dec_worst <= DEC_BAR,
              "THE EXACT FACTORIZATION warded on all %d rows: "
              "RSV == S_const x S_M2 x S_dom == GSQ pk^2/(B^2 "
              "c3q) worst dev %.1e (bar %.0e); family size %d "
              "(%d ladder + %d EXT3); family RSV min/med/max "
              "%.2f/%.2f/%.2f; family pk B^2 min/med/max "
              "%.3f/%.3f/%.3f -- the concentration ceiling that "
              "carries the closing inequality"
              % (n_full, dec_worst, DEC_BAR, len(fam_idx),
                 sum(1 for i in fam_idx if i < n349),
                 sum(1 for i in fam_idx if i >= n349),
                 min(rsv_col[i] for i in fam_idx),
                 float(np.median([rsv_col[i] for i in fam_idx])),
                 max(rsv_col[i] for i in fam_idx),
                 min(pk_col[i] * bb_col[i] ** 2
                     for i in fam_idx),
                 float(np.median([pk_col[i] * bb_col[i] ** 2
                                  for i in fam_idx])),
                 max(pk_col[i] * bb_col[i] ** 2
                     for i in fam_idx)))
        rc_fam = CCP.spearman_rank([fa_full[i] for i in fam_idx],
                                   [rsv_col[i] for i in fam_idx])
        env_bins, dec_set = lower_env_min(fa_full, rsv_col,
                                          fam_idx, NB_RES)
        env_ward_ok = (dec_set == tuple(fam_idx))
        rc_env = CCP.spearman_rank([b[0] for b in env_bins],
                                   [b[1] for b in env_bins])
        argmin_bin = min(range(len(env_bins)),
                         key=lambda k: env_bins[k][1])
        mono_ok = (rc_fam >= RC_MONO) \
            or (rc_env >= RC_MONO and argmin_bin == 0)
        fall_flag = rc_fam <= RC_FALL
        check("G61-reserve-monotonicity", env_ward_ok,
              "MONOTONICITY (sealed bars +/-%.1f): rc_fam = "
              "Spearman(F_A, RSV | family) = %+.3f; lower "
              "envelope bins (F_med, min RSV) = %s, argmin bin "
              "%d, bin Spearman %+.3f; declared-set ward %s; "
              "MONO_OK %s / FALLING %s -> the family is %s"
              % (RC_MONO, rc_fam,
                 str([(round(f, 2), round(v, 2))
                      for f, v in env_bins]), argmin_bin, rc_env,
                 "EXACT" if env_ward_ok else "BROKEN",
                 str(mono_ok), str(fall_flag),
                 "monotone-safe upward" if mono_ok else
                 ("reserve-FALLING in F_A" if fall_flag else
                  "reserve-FLAT in F_A (neither bar fires)")))
        sh_fam = [(math.log10(GSQ_R321 / bb_col[i] ** 2),
                   math.log10(pk_col[i] / m2q_col[i]),
                   math.log10(pk_col[i] * m2q_col[i]
                              / c3q_col[i]))
                  for i in fam_idx]
        sh_qui = [(math.log10(GSQ_R321 / bb_col[i] ** 2),
                   math.log10(max(pk_col[i], 1e-300)
                              / max(m2q_col[i], 1e-300)),
                   math.log10(max(pk_col[i] * m2q_col[i],
                                  1e-300)
                              / max(c3q_col[i], 1e-300)))
                  for i in quiet_idx
                  if pk_col[i] > 0 and c3q_col[i] > 0]
        med_f = [float(np.median([s[k] for s in sh_fam]))
                 for k in range(3)]
        med_q = [float(np.median([s[k] for s in sh_qui]))
                 for k in range(3)]
        b_over = sum(1 for i in fam_idx
                     if bb_col[i] ** 2 > GSQ_R321)
        check("G62-reserve-source-census", True,
              "WHERE THE RESERVE LIVES (median log10 shares "
              "S_const/S_M2/S_dom): family %+.2f/%+.2f/%+.2f "
              "vs quiet rest %+.2f/%+.2f/%+.2f -- the family "
              "reserve is the CONCENTRATION DEPTH 1/(D pk) "
              "(S_M2 x S_dom med %.1fx), NOT the calibration "
              "slack (B^2 > GSQ on %d/%d family rows: the "
              "pure-algebra route rho_2 <= (F_A B)^2 <= GSQ "
              "F_A^2 does NOT close, the r321 caveat restated) "
              "and NOT the log factors (none appear in the "
              "exact factorization)"
              % (med_f[0], med_f[1], med_f[2], med_q[0],
                 med_q[1], med_q[2],
                 float(np.median([pk_col[i] ** 2 / c3q_col[i]
                                  for i in fam_idx])),
                 b_over, len(fam_idx)))

    # ---------------- S7: Leg B -- the class theorem candidate
    section("S7  LEG B -- THE CLASS THEOREM CANDIDATE AT THE "
            "SEALED BARS")
    if smoke:
        check("G70-class-census", True, "SMOKE: skipped")
        check("G71-boundary-handoff", True, "SMOKE: skipped")
        check("G72-exceptions-adjudicated", True,
              "SMOKE: skipped")
        check("G73-ext4-outofsample", True, "SMOKE: skipped")
        cert = False
        hand = False
        exc_dissolved = False
        n_exc_ok = 0
        ext4_fam_clean = 0
        holes = []
    else:
        hard_v = [srt_full[i]["kz"] for i in fam_idx
                  if rsv_col[i] < 1.0]
        bar_v = [srt_full[i]["kz"] for i in fam_idx
                 if 1.0 <= rsv_col[i] < RHO_BAR]
        # EXT4 pure test rows (own columns)
        x4_rows = []
        for k, rc in enumerate(srt_x4):
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            c3q = ev["cm"]["S3"]
            fa4 = fa_x4[k]
            rsv4 = GSQ_R321 * fa4 ** 2 / max(ev["rho2"], 1e-300)
            dd4 = c3q / max(pk ** 3, 1e-300)
            cls4 = FCC.cls_rule(fa4, F0_SPLIT)
            hb4 = ev["dic"]["ymx"] ** 2 \
                * ev["pbg"][j_hat]["msh"]
            covh4 = ev["pbg"][R_STAR_IDX]["e3"] \
                <= CHs0 * lgl ** R344_AA
            covg4 = ev["pbg"][R_STAR_IDX]["e3"] \
                <= CGs0 * lgl ** R344_AA
            x4_rows.append(dict(kz=rc["kz"], N=rc["N"], fa=fa4,
                                rsv=rsv4, dd=dd4, cls=cls4,
                                hb=hb4, covh=covh4, covg=covg4))
        x4_fam = [r for r in x4_rows if r["cls"] == "SPIKE"]
        x4_fam_v = [r["kz"] for r in x4_fam
                    if r["rsv"] < RHO_BAR]
        ext4_fam_clean = len(x4_fam) - len(x4_fam_v)
        cert = (not hard_v) and (not bar_v) and (not x4_fam_v)
        check("G70-class-census", True,
              "THE CLASS STATEMENT [F_A >= %.1f => rho_2 <= "
              "%.4f F_A^2 with reserve >= %.1f] on ALL rows "
              "(65 ladder + 12 EXT3 + %d EXT4): family %d + %d "
              "EXT4-family rows; HARD violations (RSV < 1): %d "
              "%s; BAR violations (1 <= RSV < %.1f): %d %s; "
              "EXT4 family violations: %d %s -> CERT %s"
              % (F0_SPLIT, GSQ_R321, RHO_BAR, len(srt_x4),
                 len(fam_idx), len(x4_fam), len(hard_v),
                 str(hard_v), RHO_BAR, len(bar_v), str(bar_v),
                 len(x4_fam_v), str(x4_fam_v), str(cert)))
        # boundary census + hand-off
        bnd_rows = [(srt_full[i]["kz"], fa_full[i],
                     bnd_rule(fa_full[i], F0_SPLIT, BND_FAC),
                     lab[i], round(rsv_col[i], 1))
                    for i in range(n_full)
                    if bnd_rule(fa_full[i], F0_SPLIT, BND_FAC)
                    in ("BAND_LO", "BAND_HI")]
        bnd_rows += [(r["kz"], r["fa"],
                      bnd_rule(r["fa"], F0_SPLIT, BND_FAC),
                      "H" if r["covh"] else
                      ("G" if r["covg"] else "T"),
                      round(r["rsv"], 1)) for r in x4_rows
                     if bnd_rule(r["fa"], F0_SPLIT, BND_FAC)
                     in ("BAND_LO", "BAND_HI")]
        bnd_rows.sort(key=lambda t: t[1])
        for kz, fv, band, arm, rsv in bnd_rows:
            info("BOUNDARY kz%-4d F_A %5.2f %s arm %s RSV %s"
                 % (kz, fv, band, arm, str(rsv)))
        holes = [srt_full[i]["kz"] for i in te_x
                 if fa_full[i] < F0_SPLIT
                 and not (pa_hat["covH"][i]
                          or pa_hat["covG"][i])]
        hand = not holes
        check("G71-boundary-handoff", True,
              "BOUNDARY CENSUS (band [%.3f, %.3f]): %d rows "
              "listed above from both sides; HAND-OFF (every "
              "test row below F0 heavy/good-covered at (R_HAT, "
              "a = %d)): %s, holes %s -- the P02 "
              "complementarity as exact hand-over"
              % (F0_SPLIT / BND_FAC, F0_SPLIT * BND_FAC,
                 len(bnd_rows), R344_AA,
                 "SEAMLESS" if hand else "HOLES", str(holes)))
        # the 13 r346 exceptions adjudicated individually
        n_exc_ok = 0
        exc_txt = []
        for kz, fv, arm in v1["spk_kz"]:
            i = kz_rank[kz]
            ok_i = rsv_col[i] >= RHO_BAR
            if ok_i:
                n_exc_ok += 1
            exc_txt.append("kz%d rsv %.1f %s"
                           % (kz, rsv_col[i],
                              "DISSOLVED" if ok_i else "HOLE"))
        exc_dissolved = n_exc_ok == len(v1["spk_kz"])
        check("G72-exceptions-adjudicated", True,
              "THE 13 r346 EXCEPTIONS adjudicated individually "
              "under the two-statement structure: %s -> "
              "dissolved %d/%d %s"
              % ("; ".join(exc_txt), n_exc_ok,
                 len(v1["spk_kz"]),
                 "(the class-conditional reading carries "
                 "WITHOUT exceptions)" if exc_dissolved else
                 "(real holes remain, NAMED above)"))
        x4_quiet_cov = sum(1 for r in x4_rows
                           if r["cls"] == "QUIET"
                           and (r["covh"] or r["covg"]))
        check("G73-ext4-outofsample", True,
              "EXT4 OUT-OF-SAMPLE (PURE TEST, %d admitted): %s "
              "-- family members %d (violations %d); quiet "
              "members %d, heavy/good-covered %d at the frozen "
              "r344 freezes (census; the quiet side is NOT "
              "part of the class statement)"
              % (len(x4_rows),
                 "; ".join("kz%d F_ins %.2f %s rsv %.1f"
                           % (r["kz"], r["fa"], r["cls"],
                              r["rsv"]) for r in x4_rows),
                 len(x4_fam), len(x4_fam_v),
                 len(x4_rows) - len(x4_fam), x4_quiet_cov))

    # ---------------- S8: Leg C -- the dominance derivation
    section("S8  LEG C -- THE SOURCE DERIVATION (DOMINANCE + "
            "THE r324 IDENTITY)")
    if smoke:
        check("G80-dominance-census", True, "SMOKE: skipped")
        check("G81-source-side-reading", True, "SMOKE: skipped")
        dom_ok = False
        medDf = medDq = 0.0
    else:
        six_idx = [kz_rank[kz] for kz in SIX_KZ]
        dd_fam = [dd_col[i] for i in fam_idx]
        dd_six = [dd_col[i] for i in six_idx]
        dd_qui = [dd_col[i] for i in quiet_idx
                  if pk_col[i] > 0 and c3q_col[i] > 0]
        medDf = float(np.median(dd_fam))
        maxDf = max(dd_fam)
        medDq = float(np.median(dd_qui))
        contrast = medDq / max(medDf, 1e-300)
        dom_ok = (medDf <= D_FAM_MED_BAR
                  and maxDf <= D_FAM_MAX_BAR
                  and contrast >= DOM_CONTRAST)
        check("G80-dominance-census", True,
              "THE DOMINANCE CENSUS D = c3q/pk^3 (sealed bars "
              "med <= %.1f, max <= %.1f, contrast >= %.1f): "
              "family med %.2f max %.2f (argmax kz%d); "
              "six-sharp %s; quiet med %.2f -> contrast %.1fx; "
              "DOM_OK %s -- %s"
              % (D_FAM_MED_BAR, D_FAM_MAX_BAR, DOM_CONTRAST,
                 medDf, maxDf,
                 srt_full[max(fam_idx,
                              key=lambda i: dd_col[i])]["kz"],
                 str([round(v, 2) for v in dd_six]), medDq,
                 contrast, str(dom_ok),
                 "the family IS the dominant-atom class"
                 if dom_ok else
                 "the dominance bars do NOT fire"))
        pkb2_max = max(dd_col[i] * pk_col[i] * bb_col[i] ** 2
                       for i in fam_idx)
        check("G81-source-side-reading", True,
              "THE SOURCE-SIDE READING (exact, warded in G42): "
              "rho_2 = D pk (F_A B)^2 and RSV = GSQ/(D pk B^2) "
              "= GSQ m/(D F_A B^3 log m) via the r324 identity "
              "pk = F_A B log m/m -- the class statement with "
              "reserve %.1f closes iff D pk B^2 <= GSQ/%.1f = "
              "%.3f on the family; MEASURED max family D pk "
              "B^2 = %.3f (%s); the remaining census-grade "
              "premise is the family concentration ceiling "
              "(pk <= 1 alone does NOT suffice: B_max %.2f "
              "gives the pure-algebra floor GSQ/B^2 = %.2f)"
              % (RHO_BAR, RHO_BAR, GSQ_R321 / RHO_BAR, pkb2_max,
                 "CLOSES" if pkb2_max <= GSQ_R321 / RHO_BAR
                 else "does NOT close",
                 max(bb_col[i] for i in fam_idx),
                 GSQ_R321 / max(bb_col[i] for i in fam_idx) ** 2))

    # ---------------- S9: Leg D -- composition + adjudication
    section("S9  LEG D -- THE HONEST m_0* + SEALED ADJUDICATION")
    if smoke:
        check("G85-composition", True, "SMOKE: skipped")
        check("G86-cofinal-typing", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        fam_fa_max = max(fa_full[i] for i in fam_idx)

        def rhs_spike(t):
            return GSQ_R321 * fam_fa_max ** 2 * t ** 2
        m0_spike = solve_m0(lambda t: math.log(
            max(rhs_spike(t), 1e-300)))
        m0_two = max(v1["m0_gen"],
                     m0_spike if m0_spike is not None else 0.0)
        m0_306 = solve_m0(lambda t: math.log(
            max(R306_C2 * t ** 2, 1e-300)))
        info("THE m_0* TABLE (typed):")
        info("  r344/r346 uniform (F_Amax %.2f):        "
             "10^%.1f (record 10^%.1f) -- UNCHANGED"
             % (fa_max, m0_r344, M0_R344))
        info("  V1 class-conditional QUIET (cap %.2f):  10^%.1f"
             % (v1["fam_q"], v1["m0_gen"]))
        info("  V2 percentile (cap %.3f):               10^%.1f"
             % (cap2, v2["m0_gen"]))
        info("  SPIKE-side solve (family ceiling %.2f): %s"
             % (fam_fa_max,
                ("10^%.1f" % m0_spike)
                if m0_spike is not None else "NONE"))
        info("  TWO-STATEMENT composite max(quiet, spike): "
             "10^%.1f" % m0_two)
        info("  comparisons: r324 route 10^%.1f; r306 census "
             "10^%.1f" % (R324_M0_L10, m0_306))
        check("G85-composition", True,
              "THE HONEST m_0* OF THE TWO-STATEMENT STRUCTURE: "
              "the uniform number stays 10^%.1f (the family "
              "F_A ceiling %.2f is a CENSUS number, not a law); "
              "the two-statement composite is 10^%.1f (binding "
              "side: the spike statement through GSQ F_Amax^2 "
              "(log m)^2); the honest yield is the TYPE UPGRADE "
              "of the class-conditional 10^%.1f reading: %s"
              % (m0_r344, fam_fa_max, m0_two, v1["m0_gen"],
                 "13/13 exceptions dissolve -> a two-theorem "
                 "structure without exceptions"
                 if exc_dissolved else
                 "exceptions REMAIN -> the reading keeps its "
                 "exception family"))
        check("G86-cofinal-typing", True,
              "COFINAL TYPING (r346 convention): CENSUS = every "
              "freeze constant, the family reserves/D tables, "
              "the family F_A ceiling %.2f, the pk B^2 ceiling "
              "%.3f; LAW CANDIDATES = the class statement "
              "(CERT %s at sealed bars, EXT3 in-family "
              "out-of-sample, dominance-typed %s), P02 (r346 "
              "OOS-confirmed), the K1 formula (r346); MISSING = "
              "a family growth law (m q_max <= C log m on the "
              "family) -- without it the uniform m_0* stays "
              "10^%.1f and the ladder-to-m_0* step stays the "
              "disclosed extrapolation hypothesis"
              % (fam_fa_max,
                 max(dd_col[i] * pk_col[i] * bb_col[i] ** 2
                     for i in fam_idx),
                 str(cert), str(dom_ok), m0_r344))
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (tilt_w > TILT_BAR or wqd_w > WQ_BAR
                      or part_w3 > PART_BAR or bkd_w > BK_BAR
                      or env_w > ENV_BAR or pgi_w > PGI_BAR
                      or hvy_w > HVY_BAR or e3d_w > DICT_BAR
                      or mart_w > TREE_BAR or unit_w > TREE_BAR
                      or rec_w > TREE_BAR or not fr_ok
                      or not mult_all_ok
                      or norm_w > DEC_BAR or dec_w > DEC_BAR
                      or chainD_w > DEC_BAR
                      or id324_w > CHAIN_BAR
                      or dec_worst > DEC_BAR or fd_dev != 0)
        vkey = law_tree_verdict(leak, brk_struct, cert, hand,
                                dom_ok, mono_ok)
        flags = []
        if mono_ok:
            flags.append("RESERVE_MONOTONE(%+.2f)" % rc_fam)
        elif fall_flag:
            flags.append("RESERVE_FALLING(%+.2f)" % rc_fam)
        else:
            flags.append("RESERVE_FLAT(%+.2f)" % rc_fam)
        if dom_ok:
            flags.append("DOMINANT_FAMILY(%.2f, %.2f)"
                         % (medDf, medDq))
        if exc_dissolved:
            flags.append("EXCEPTIONS_DISSOLVED(%d/13)"
                         % n_exc_ok)
        if holes or n_exc_ok < len(v1["spk_kz"]) or x4_fam_v:
            flags.append("HOLES(%s)"
                         % str(holes
                               + [kz for kz, _f, _a
                                  in v1["spk_kz"]
                                  if rsv_col[kz_rank[kz]]
                                  < RHO_BAR]
                               + list(x4_fam_v)))
        if ext4_fam_clean == len(x4_fam):
            flags.append("EXT4_CLEAN(%d)" % len(x4_rows))
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a law "
                           "builder",
            "LAW_STATE_NOT_EXACT":
                "an exact ward broke (path %.1e / NORM %.1e / "
                "decomposition %.1e / chain %.1e / Fractions "
                "%s)" % (tilt_w, norm_w, dec_worst, chainD_w,
                         str(fr_ok)),
            "THIRDARM_LAW_DERIVED":
                "CERT (0 family violations at reserve >= %.1f "
                "on 65 + 12 + %d rows) AND seamless hand-off "
                "AND the dominance structure fires (med D fam "
                "%.2f vs quiet %.2f) -- the spike coverage IS "
                "the r324 identity + dominance + the named "
                "census ceiling"
                % (RHO_BAR, len(srt_x4), medDf, medDq),
            "CLASS_THEOREM_CERTIFIED":
                "CERT + hand-off + monotone-safe family (the "
                "dominance bars did not fire)",
            "RESERVE_ACCIDENTAL":
                "the numbers hold (CERT + hand-off) but "
                "neither the dominance nor the monotonicity "
                "structure fires at the sealed bars -- the "
                "class threshold carries no certified "
                "structure, said honestly",
            "EXCEPTIONS_REMAIN":
                "violations or hand-off holes remain (every "
                "hole NAMED): hard %s bar %s hand-off holes %s "
                "EXT4 bar misses %s"
                % (str(hard_v), str(bar_v), str(holes),
                   str([(r["kz"], round(r["rsv"], 2))
                        for r in x4_fam
                        if r["rsv"] < RHO_BAR]))}
        verdict_main = "%s(%s)%s" % (
            vkey, det_v[vkey],
            ("".join(" + " + f for f in flags)) if flags else "")

    # ---------------- S10: Leg E -- worlds + must-fails + verdict
    section("S10  LEG E -- WORLD CENSUS + MUST-FAILS + VERDICT")
    wtab = [("w9", mrecs[0])]
    if not smoke:
        wtab.append(("w13(twin)", mrecs[1]))
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]))
    scr_flag_txt = ""
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
            c3q_w = ev["cm"]["S3"]
            dd_w = c3q_w / max(ev["mqs"]["qm"] ** 3, 1e-300)
            rsv_w = GSQ_R321 * fa_w ** 2 \
                / max(ev["rho2"], 1e-300)
            cls_w = FCC.cls_rule(fa_w, F0_SPLIT)
            info("world %-10s m %3d F_A(ins) %.2f class %-5s "
                 "D %5.2f rho2 %.3f RSV %.1f %s"
                 % (w, ev["m"], fa_w, cls_w, dd_w, ev["rho2"],
                    rsv_w,
                    ("<- the class statement %s SCRAMBLE"
                     % ("COVERS" if rsv_w >= RHO_BAR
                        else "does NOT cover"))
                    if w == "SCR" else ""))
            if w == "SCR" and cls_w == "SPIKE" \
                    and rsv_w >= RHO_BAR:
                scr_flag_txt = " + SCRAMBLE_IN_CLASS(rsv %.1f)" \
                    % rsv_w
        check("G90-world-census", len(wtab) >= 2,
              "WORLD CENSUS (NO letter): the class rule + class "
              "statement evaluated on %d worlds via the r321 "
              "insertion coordinate%s -- a covering statement "
              "on SCRAMBLE makes the class statement "
              "ARITHMETIC-FREE by measurement (a pure "
              "concentration-size statement; no world "
              "separation claimed -- the r321 class-side "
              "rejection continues to carry that load), typed "
              "honestly"
              % (len(wtab), scr_flag_txt))
    check("G91-e1-reserve-bar-posthoc",
          len(e1_hits) >= 1 and abs(mut1 - 0.5) <= TOY_BAR
          and mut1 != RHO_BAR,
          "e1 protocol-CAUGHT twice: the reserve bar read from "
          "the evaluated target column -- AST-FLAGGED (%s) -- "
          "and on the toy returns %.1f != the sealed RHO_BAR "
          "%.1f (the bar is sealed in this spec BEFORE the "
          "freeze)"
          % (e1_hits[0] if e1_hits else "MISS", mut1, RHO_BAR))
    check("G92-e2-f0-posthoc",
          len(e2_hits) >= 1 and mut2 == 2.0
          and mut2 != F0_SPLIT,
          "e2 protocol-CAUGHT twice: the family threshold "
          "re-picked after sight of the violation column -- "
          "AST-FLAGGED (%s) -- and on the toy returns %.1f != "
          "the sealed F0_SPLIT %.1f (the r329 SPIKE_FA record "
          "constant, adopted a-priori)"
          % (e2_hits[0] if e2_hits else "MISS", mut2, F0_SPLIT))
    check("G93-e3-dom-circular",
          len(e3_hits) >= 1 and mut3 == Fr(7, 2)
          and mut3 != dom3_true,
          "e3 CAUGHT twice: the circular dominance consuming "
          "the q_max RECORD -- AST-FLAGGED (%s) -- and on the "
          "sealed Fractions toy returns %s != the true "
          "dominance %s (the real diagnostic recomputes peak "
          "and cube from the SAME block vector)"
          % (e3_hits[0] if e3_hits else "MISS", str(mut3),
             str(dom3_true)))
    check("G94-e4-chain-wrong-log",
          mut4 == Fr(3, 4) and chain4_true == Fr(3, 8)
          and mut4 / chain4_true == Fr(2),
          "e4 CAUGHT exact: the chain with the wrong log power "
          "returns %s on the sealed Fractions toy while the "
          "exact chain gives %s -- break factor %s == the "
          "pseudo-log EXACT (the (log m)^2 power of the r306 "
          "scale is load-bearing)"
          % (str(mut4), str(chain4_true),
             str(mut4 / chain4_true)))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact reserve factorization with "
          "monotonicity adjudication, the class theorem "
          "candidate at sealed (F0, reserve) bars on 65 + 12 + "
          "6 rows with boundary hand-off and the 13-exception "
          "adjudication, the dominance derivation with the "
          "r324-identity reading, and the honest two-statement "
          "m_0* typing -- NO new certificate promoted, NO "
          "universal bound claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R349_ANCHORS(identity %.1e, r306 C2 %.3f v%d, "
                 "r316 n %d, dict %.1e, r321 FA %.2f/%.2f/%.2f, "
                 "r344 COMPLETE: R_HAT %d halves (%d, %d) C "
                 "%.4f/%.4f third-only %d F_Amax %.2f m0 "
                 "10^%.1f, r346: K1 idx %d cert %.4f+%.4f, K4 "
                 "%.4f+%.4f, P02 %d/39+%d/12, V1 %d spikes cap "
                 "%.2f m0 10^%.1f, V2 %.3f 10^%.1f, six %s)"
                 % (rec3_w, C2r, viol2, n349, dict3_w,
                    fa_kz[53], fa_kz[83], fa_kz[67], j_hat, j_a,
                    j_b, CHs0, CGs0, pa_hat["third_used"],
                    fa_max, m0_r344, k1_j, pa_k1["CH"],
                    pa_k1["CG"], CHe, CGe, p02_core, p02_x3,
                    len(v1["spk_kz"]), v1["fam_q"], v1["m0_gen"],
                    cap2, v2["m0_gen"],
                    str(sorted(only_third_every_a)))]
        parts.append("SEAL(tilt %.1e, NORM %.1e, r324 id %.1e, "
                     "decomp %.1e, chain %.1e, Fractions %s, "
                     "purity clean, toys exact)"
                     % (tilt_w, norm_w, id324_w, dec_worst,
                        chainD_w, "EXACT" if fr_ok else "BROKEN"))
        parts.append("ANATOMY(family %d rows, RSV min/med/max "
                     "%.2f/%.2f/%.2f, factors med %+.2f/%+.2f/"
                     "%+.2f, rc_fam %+.3f, env argmin %d)"
                     % (len(fam_idx),
                        min(rsv_col[i] for i in fam_idx),
                        float(np.median([rsv_col[i]
                                         for i in fam_idx])),
                        max(rsv_col[i] for i in fam_idx),
                        med_f[0], med_f[1], med_f[2], rc_fam,
                        argmin_bin))
        parts.append("CLASSLAW(hard %d bar %d ext4-fam %d/%d, "
                     "hand-off %s holes %s, exceptions %d/%d "
                     "dissolved, CERT %s)"
                     % (len(hard_v), len(bar_v), len(x4_fam_v),
                        len(x4_fam), str(hand), str(holes),
                        n_exc_ok, len(v1["spk_kz"]), str(cert)))
        parts.append("DOMINANCE(fam med %.2f max %.2f quiet med "
                     "%.2f contrast %.1fx, DOM_OK %s, max D pk "
                     "B^2 %.3f vs %.3f)"
                     % (medDf, maxDf, medDq,
                        medDq / max(medDf, 1e-300), str(dom_ok),
                        pkb2_max, GSQ_R321 / RHO_BAR))
        parts.append(verdict_main)
        parts.append("COMPOSITION(uniform 10^%.1f unchanged, "
                     "two-statement 10^%.1f, V1 10^%.1f, V2 "
                     "10^%.1f, r306 10^%.1f)"
                     % (m0_r344, m0_two, v1["m0_gen"],
                        v2["m0_gen"], m0_306))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the reserve "
          "factorization, the dominance form, the r324 "
          "identity, the Fractions toys and the purity audits "
          "(exact / AST-decided); MEASURED: every census, "
          "reserve, D value and violation count (the finite "
          "class ladder + 12 EXT3 + 6 EXT4 + 2 mains + 2 live "
          "controls); OPEN: any bound beyond the measured "
          "rungs, the family growth law, the cofinal law, the "
          "actual proof (a certified class statement fixes a "
          "theorem candidate with sealed premises, it proves "
          "nothing cofinal); NO RH claim"
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
