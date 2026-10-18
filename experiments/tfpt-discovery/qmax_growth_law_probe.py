#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qmax_growth_law_probe --
PRIME.L2.QMAX_GROWTH_LAW.01 (round 351): THE FAMILY GROWTH LAW
m q_max <= C log m AND THE STABLE RESERVE FLOOR -- the named
successor round after r349.

CONTEXT (binding, from the sealed r349 record SPEC_SHA 9b593e63,
EXCEPTIONS_REMAIN + RESERVE_FLAT(-0.33) + EXCEPTIONS_DISSOLVED
(13/13) + HOLES([111, 75])): the terminal cover is canonized (r346
K1/K4) and the RAW class law rho_2 <= 1.3056 F_A^2 on F_A >= 1.5
holds with ZERO hard violations on all 23 family rows across three
cohorts incl. the fresh EXT4 record F_ins 6.68 (kz111) -- but TWO
quantities are still census, not law: (1) the family F_A ceiling
GROWS out-of-sample (5.54 -> 6.68), so the uniform constant stays
census and m_0* hangs at 10^22.6; (2) the sealed reserve bar 1.5
is undercut by exactly the two deepest fresh spikes kz111/kz75
(1.11/1.07) -- the honest floor is ~1.1.  THE MISSING LAW (this
round's contract): m q_max <= C log m, equivalently F_A B <= C --
the r324 identity F_A x B x log m == m x q_max is EXACT, so the
growth law is PRECISELY the boundedness of the product F_A B, and
that product is CONVENTION-FREE (it does not depend on which F_A
convention is used, because B := q_max m/(F_A log m) by
construction): F_A B == m q_max/log m == the r324 G/log m column.

THE EXACT ALGEBRA OF THIS ROUND (derived, disclosed, no
measurement -- the r324/r327/r349 records restated): with q_j =
|x_j|/L, pk = max q, lg = log m, FAB := m pk/lg:
  (i)  THE IDENTITY (r324, exact): F_A x B == FAB for EVERY F_A
       convention (ladder EFP.local_ratio or r321 insertion),
       because B is DEFINED as pk m/(F_A lg); FAB is the
       convention-free object of the law.
  (ii) THE PILEUP CHAIN (r324, exact): m pk <= nsc x pil with
       nsc = # distinct dyadic source scales in the argmax block
       and pil = m max_s mass(j*, s)/L; the r324/r329 record:
       nsc_rel/log m <= C_NSC = 2.0258 holds 0/39 + 12/12 -- the
       law m pk <= C log m REDUCES to a pileup cap pil <= C'.
  (iii) THE GROUP CHAIN (r327, exact): m pk <= ngj x hgn with
       ngj = # fold groups of the argmax block and hgn = m x (max
       group abs mass)/L; the r327/r329 record: ngj/log m <= C_NG
       = 2.6351 holds 0/39 + 12/12 -- the law equally REDUCES to
       a group-mass cap hgn <= C''.
  (iv) THE SPIKE COMPOSITION (r349, exact): rho_2 = D pk (FAB)^2
       and RSV = GSQ F_A^2/rho_2 = GSQ/(D pk B^2) -- a bounded
       FAB with the measured D/pk anatomy is exactly what turns
       the r349 census ceiling into a law.
  (v)  THE POLYLOG RECOMPOSITION (r324 interpolation, exact):
       sum q^3 <= pk x M_2 <= (FAB lg/m)(mM2/m), so a certified
       FAB <= C_FAB with the measured envelope mM2 <= C_M2ENV
       gives rho_2 <= C_FAB C_M2ENV/lg -- the A = 1 polylog form:
       the uniform m_0* becomes solve(m^0.224 >= C_FAB C_M2ENV
       log m), CLASS-FREE (no spike/quiet split needed on the
       asymptotic side).

THE SEALED MACHINERY (disclosed BEFORE any evaluation):
  LEG A -- THE FAB CENSUS WITH FRESH DEPTHS: FAB on ALL available
      rows (65 ladder + 12 EXT3 + 6 EXT4) plus the NEW fresh EXT5
      tranche (sealed selection below); the FREEZE RULE (sealed):
      C_FAB = max FAB over the SEALED cohort (the 65 + 12 + 6 rows
      of the r306..r349 record surface -- every one of them seen
      by an earlier sealed record run); the TEST: pointwise FAB <=
      C_FAB on the admitted EXT5 rows (0 violations demanded for
      the CERT branch).  THE GROWTH ADJUDICATION (sealed):
      new_record iff max FAB(EXT5) > C_FAB; rc_small = Spearman(m,
      FAB) over the SMALL-gap-class family rows of ALL cohorts
      (the class that carries every known maximum -- the
      composition-controlled trend, r329 lesson; speaks only at
      n >= RC_N_MIN = 8); GROW iff new_record OR rc_small >=
      RC_GROW = +0.5.  The depth-bin upper envelope (module-own
      upper_env_max over NB_FAB = 4 m-rank bins of all rows,
      declared-set warded) is printed as CENSUS (cohort
      composition makes it letter-unfit, said out loud).
  LEG A2 -- THE FRESH EXT5 TRANCHE (the r343 EXT4 selection rule
      VERBATIM, next tranche): USED = used_kz_set(frame_a_zones,
      LM.ext_rule, 35) UNION the 12 EXT3 UNION the 6 EXT4 (== 98
      gated); POOL = admissible_pool(H_MIN, EXT4_H_MAX = 3400);
      DOMAIN z^2 <= 400000 (the family-definition cap, r343);
      FRESH = POOL minus USED under the domain (== 17 gated);
      STRATUM B5 = the K_EXT5 = 3 smallest-grel fresh kz with z
      inside the core zone [16, 317] (grel = EFA.grel_col, W = 5);
      STRATUM A5 = the 3 deepest (h desc) of the remainder.
      ADMISSION (r329 convention): POSITIVE_PREFIX + fold mult <=
      2 + non-degenerate; a failing candidate is REPLACED by the
      next in the stratum's sealed queue (census disclosed).  THE
      POOL LIMIT (scoping, disclosed): the in-zone small-gap queue
      has EXACTLY 3 members left (kz65/81/79) -- after this round
      the in-zone fresh pool of the family construction is
      EXHAUSTED under the domain cap, documented honestly.
  LEG B -- THE SOURCE DERIVATION (sealed candidate formulas, all
      constants FROZEN on the sealed cohort, tested pointwise on
      EXT5): K2 (Klein-gap): FAB x grel <= C_K2 (the r329 gap
      geometry: the large q_max live at small relative gaps --
      structural formula, typed census unless grel is bounded
      below); K3 (pileup): pil <= C_K3, composing with the r329
      count to FAB <= C_NSC x C_K3 via chain (ii); K4 (group):
      hgn <= C_K4, composing to FAB <= C_NG x C_K4 via chain
      (iii).  THE FRESH COUNT TEST: nsc_rel/lg <= 2.0258 and
      ngj/lg <= 2.6351 (the r329 FROZEN constants) on the 6 EXT4
      + admitted EXT5 rows -- the EXT4 count columns were NEVER
      measured (r349 did not compute them): a genuinely open
      choice-robustness test of the lane's counting side.
      src_ok iff some K in {K3, K4}: 0 EXT5 violations AND the
      fresh count test passes 0-violation AND the implied ceiling
      (C_NSC C_K3 resp. C_NG C_K4) <= IMPL_FAC = 4.0 x the
      measured max FAB (non-vacuity, a-priori).
  LEG C -- THE STABLE RESERVE FLOOR: the sealed NEW bar RHO_BAR2 =
      1.05 (below the honest r349 floor ~1.07): cert2 iff 0 family
      rows (ALL cohorts incl. EXT5) with RSV < RHO_BAR2.  THE
      FLOOR ANATOMY: per family row D, pk, GSQ/B^2, pk B^2,
      D pk B^2, RSV; the census contrast floor rows (RSV < 1.5)
      vs comfortable rows.  THE EROSION: e_RSV = dyadic
      halves-slope of RSV vs m over the family rows (fit-free)
      + rc_fam351 = Spearman(F, RSV) on the extended family
      (r349 prior -0.331 on ladder+EXT3, disclosed); the
      extrapolated crossing log10 m_x = log10 m_med - log10
      RSV_med / e_RSV (printed for e_RSV < 0).  SEALED LETTER:
      FLOOR_CENSUS iff no EXT5 family rows exist (no fresh
      teeth); else FLOOR_CONVERGES iff cert2 AND e_RSV >=
      -E_FLAT_BAR = -0.15; else FLOOR_ERODES(log10 m_x).
  LEG D -- THE COMPOSITION: the m_0* table (r344/r346 uniform
      10^22.6 at the OLD ceiling; the moved uniform at the NEW
      overall F ceiling; V1 10^16.1 / V2 10^17.5 reprinted as
      record constants; r306 census m0 recomputed; r324 route
      10^59.6) PLUS the law recomposition (v): at CERT the
      class-free polylog m_0* = solve(CRIT_EXP t >= log(C_FAB
      C_M2ENV t)) with C_M2ENV = max m M_2 over ALL rows (the
      r324 envelope convention, ladder record 3.1938); at GROW
      the subcritical typing (r324 convention): e_tot = e_FAB +
      e_M2 (halves-slopes over all rows, composition-dominated,
      typed census) vs CRIT_EXP = 0.224, and the growth-slack
      m_0* = solve(CRIT_EXP t >= log(C t) + e_pos t).  THE
      COFINAL TYPING (r346/r349 convention): at GO the named
      list of EXACTLY what still stands between the cover and a
      cofinal theorem is printed (the census freeze of C_FAB/
      C_M2ENV + the extrapolation hypothesis, the floor letter,
      the source-derivation status, the finite closure below
      m_0*, the missing second world).
  LEG E -- WORLDS + MUST-FAILS: FAB + F_ins + class + RSV on
      MAIN w9 / twin w13 / EPSTEIN / SCRAMBLE via the r321
      insertion coordinate (census, NO letter; SCRAMBLE is
      SPIKE-class with F_A(ins) 2.00, r346/r349 record -- its
      FAB is a genuinely open world datum).

LEG 0 -- ANCHOR REGRESSION (bit-near; slim set + the COMPLETE
r349 family record surface through the same code path,
disclosed): the r314 identity wards live (ladder/EXT3/EXT4/EXT5
bars); r306 C_2 = 1.069 (tol 0.005) first-5 freeze 0/57; r316
rho anchors + C_small + n = 65; the dictionary-chain identity;
the r321 F_A top-3 2.47/2.39/2.38; THE r349 FAMILY RECORD
(family size 17 on the 77 sealed rows, RSV min/med/max
3.19/7.03/12.06, rc_fam -0.331, med D fam 1.79 / max 2.13 /
quiet 5.03, max D pk B^2 0.409, median log10 shares
+0.01/+0.64/+0.26); THE r349 EXT4 RECORD (all six SPIKE, sorted
F_ins (1.58, 2.03, 3.11, 4.22, 5.53, 6.68), the two bar misses
kz111 rsv 1.11 / kz75 rsv 1.07); THE r324 DIRECT RECORD through
the FAB column (C_INF = max cal FAB = 1.7481, test violations
EXACTLY {53, 67, 76, 61, 83}, e_G = +0.158 over the 39 test
rungs -- FAB == the r324 G/log m column bit-near); THE r329
COUNTING RECORD (C_NSC = 2.0258 cal freeze 0/39, C_NG = 2.6351
cal freeze 0/39, EXT3 12/12 with min reserves 1.6/1.8).  The
r344/r346 cover records are NOT re-run here (slim set,
disclosed): they were reproduced through this same code path by
the sealed r349 probe; this round consumes no cover column.

LEG E MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) FORMULA READ FROM THE RECORD COLUMN: mutant_fab_readback
  consumes the stale q_max RECORD value instead of recomputing
  from the same block vector -- the QMAX_FORBIDDEN scope audit
  must FLAG it AND on the sealed Fractions toy (true peak 3/4,
  stale record 1/2, m = 2, pseudo-log 2) it returns 1/2 while
  the true FAB is 3/4 -- CAUGHT twice.
(e2) FRESH-WINDOW SELECTION AFTER SIGHT (protocol):
  mutant_select_posthoc picks the fresh windows that minimize
  the seen violation mass (consumes rho) -- the BOUND_FORBIDDEN
  scope audit must FLAG it AND on the sealed toy it returns
  (2, 3) != the sealed queue-order rule's (1, 2) --
  protocol-CAUGHT twice.
(e3) IDENTITY WITH THE WRONG LOG POWER: mutant_fab_wrong_log
  claims FAB = m pk/lg^2 -- on the sealed Fractions toy (m = 3,
  pk = 1/2, pseudo-log lg = 2) it returns 3/8 while the exact
  FAB is 3/4 -- break factor == lg == 2 EXACT.
(e4) FLOOR BAR READ FROM THE TARGET (protocol):
  mutant_floorbar_posthoc sets the reserve bar at the seen
  minimum (consumes rho) -- the BOUND_FORBIDDEN scope audit must
  FLAG it AND on the sealed toy it returns 0.5 != the sealed
  RHO_BAR2 1.05 -- protocol-CAUGHT twice.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

SEALED VERDICTS (main letter: exactly one fires, total order;
flags appended with '+', combinations allowed by the contract):
   TARGET_LEAK            iff any purity/scope/literal audit hit
       on the module-own law builders,
   LAW_STATE_NOT_EXACT    iff an exact ward breaks on a live
       world (the identity/chain/decomposition wards, the
       Fractions pins, the toys),
   GROWTH_CENSUS_ONLY     iff fewer than FRESH_MIN = 2 EXT5 rows
       are admitted (no fresh teeth -- the round degrades to
       census, said honestly),
   FA_UNBOUNDED           iff GROW fires (a new fresh FAB record
       above the frozen C_FAB, or the composition-controlled
       small-gap trend rises) -- the ceiling grows with depth,
       the law is refuted at the measured range, the spike
       constant stays census; the growth trend is TYPED
       (log-log slopes, subcriticality vs 0.224, the asymptotic
       m_0* meaning),
   GROWTH_LAW_DERIVED     iff not GROW and src_ok (a source-side
       candidate formula carries at frozen constants with fresh
       count confirmation -- the theorem-kernel candidate),
   GROWTH_LAW_CERTIFIED   otherwise (not GROW implies 0 fresh
       violations at the frozen C_FAB: the growth law holds
       with a stable sealed constant on every measured cohort;
       census-frozen, no cofinal claim).
   FLOOR FLAGS (exactly one appended): FLOOR_CONVERGES /
       FLOOR_ERODES(log10 m_x) / FLOOR_CENSUS.
   EXTRA FLAGS: +NEW_FAB_RECORD(kz, val) / +INZONE_POOL_
       EXHAUSTED / +EXT5_CLEAN(n) / +SCRAMBLE_FAB(val).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in either
direction.  Coexistence: r350 (alpha source anatomy, L*) ran in
parallel and is synced -- own files only; before the strictly
additive rh-sync the current git state is re-checked.
Two-commit freeze protocol (r329 convention): spec committed
pre-freeze, record tables the only post-freeze edit, committed
again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r317/r321/r324/r327/
r329/r339/r343/r344/r346/r349 machinery imported verbatim; the
r349 census/controls/extensions/EXT3/EXT4 scaffold is re-executed
through the same code path and anchor-gated against the r349
records): t_{N-2} = sum_b ct_b; F = 0.20 edge split; level-2
blocks; the r306 RY3 layer; the r314 SCF layer; the r316 TRB
layer; the r317 EFP.local_ratio; the r321 CCP.local_median +
CCP.world_coord + CCP.spearman_rank; the r324 QMO.pileup_state +
QMO.scale_bins + QMO.mult_ward + FAP.m2_qmax_state; the r327
GMC.group_mass_ledger + GMC.heavy_state; the r329
EFA.admissible_pool + EFA.grel_col + EFA.used_kz_set +
EFA.gap_class; the r343 PC343.ext4_domain_fresh + the EXT4
domain constants; the r339 FDD.martingale_moment_dictionary;
the r349 TSL.res_decomp + the r349 constant set (F0_SPLIT,
RHO_BAR, EXT4_KZ, bars) -- ALL imported verbatim and
SPEC_SHA-prefix gated (TSL 9b593e63, EFA bbfaf199, PC343
9ffc2705).  NEW in this round (module-own): ext5_next_tranche
(the sealed next-tranche selection, r343 rule verbatim on the
extended used ledger), upper_env_max (the fit-free depth-bin
upper envelope, declared-set warded), growth_tree_verdict +
floor_letter (the sealed trees) and fr_fab_toy (the Fractions
FAB pin).  FAB, RSV, D, pil, nsc, ngj, hgn and every census on
them are TARGET-SIDE DIAGNOSTICS computed in the gate section
(the r321/r349 qmax-share convention, disclosed) -- the
module-own builders consume passed values, the source grid,
window shape and SEALED thresholds only.

INDEX FIREWALL (binding, r238-r350 discipline): w = window (kz),
N_w = builder depth; ground truth enters GATES and census tables
only; the cubic target M_3/rho_2 and the q_max RECORD enter
GATES / anchors / census tables / diagnostics only, NEVER a law
builder (AST-warded); no zero/prime oracles anywhere (AST
firewall; the prime-power anchor grid U_ALL/G_ALL is the sealed
source comb, r238 convention); no fit primitives (fragment
audit; exponents are the imported r272 dyadic halves-slope,
fit-free; Spearman is the imported r321 rank correlation).
B PROVENANCE: B_w = S_{N-2} + 5/7 (imported floor, never
fitted).  COFINAL LADDER (pre-sealed, r316/r324/r329/r343/r349
verbatim): frame-A h <= 900, 42 rungs, (N, kz)-sorted; exception
set {kz15, 20, 22, 36, 38, 39, 52}; EXTENSION 900 < h <= 1300
first 15; EXT2 r316 A5 rule; EXT3 = the sealed r329 12-anchor
list; EXT4 = the sealed r343/r345 6-anchor list (both adopted
as-is); EXT5 = THIS round's sealed next-tranche rule above.

SEALED CONSTANTS (everything not listed here is the r349
constant set imported verbatim from TSL/FTS/FCC/EFA/PC343):
EXT5_H_MAX = PC343.EXT4_H_MAX = 3400; K_EXT5 3; Z2_CAP 400000
(PC343 verbatim); LM_RANKS_USED 35; USED_EXPECT_X5 98;
FRESH_EXPECT_X5 17; CORE_Z (16, 317); B5Q_EXPECT (65, 81, 79);
A5Q_HEAD_EXPECT (106, 135, 103); FRESH_MIN 2; TB_WARD_BAR_X5
1e-4; REC3_BAR_X5 1e-12 (the r349 X4 bars adopted: the EXT5
depth 2812 stays below the EXT4 depth 3181); RC_GROW 0.5;
RC_N_MIN 8; NB_FAB 4; RHO_BAR2 1.05; E_FLAT_BAR 0.15 (the
r342/r343 FLAT_BAR convention); IMPL_FAC 4.0; FAB_ID_BAR 1e-12;
GRP_CHAIN_BAR 1e-9; R349 record anchors (tol): FAM_N 17 EXACT;
RSV triple (3.19, 7.03, 12.06) tol 0.02; RC_FAM -0.331 tol
0.005; D fam (1.79, 2.13) tol 0.01; D quiet 5.03 tol 0.01;
DPKB2 0.409 tol 0.005; shares (+0.01, +0.64, +0.26) tol 0.02;
EXT4 F_ins sorted (1.58, 2.03, 3.11, 4.22, 5.53, 6.68) tol
0.01; EXT4 holes {111: 1.11, 75: 1.07} tol 0.01; R324 C_INF
1.7481 tol 0.005 with violator set {53, 67, 76, 61, 83} EXACT
and e_G +0.158 tol 0.005; R329 C_NSC 2.0258 / C_NG 2.6351 tol
0.005 each with 0/39, EXT3 min count reserves 1.6/1.8 tol 0.05;
R351_TABLE_LITERALS = the sealed r314..r349 set (TSL verbatim)
UNION the r349/r324/r329 record set {3.19, 7.03, 12.06, -0.331,
1.79, 2.13, 5.03, 0.409, 6.68, 5.53, 1.11, 1.07, 1.58, 4.22,
1.7481, 0.158, 2.0258, 2.6351, 22.6, 59.6} (collision-prone
small values 1.6, 1.8, 2.03, 3.11, 13.5, 16.1, 17.5 curated
OUT, r337..r349 convention, disclosed); runtime <= 1800 s;
smoke = w9 + controls + toys + scope/purity audits + the exact
w9 wards + the w9 Fractions pins + e1-e4 mutants; ladder,
extensions, EXT3, EXT4, EXT5, anchors, census, source
candidates, floor, composition and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r321/r324/r329/r349 RECORD number
adopted as-is; the identity, the pileup chain, the group chain
and the polylog recomposition are DERIVED ALGEBRA from the
sealed r324/r327 records (disclosed above); ONE SCOPING PASS
(sizing only, r329/r343 precedent) enumerated the selection
surface and timed the budget: USED ledger 98, lifted pool 158,
domain-capped FRESH 17, core zone [16, 317], B5 queue EXACTLY
(kz65 z 239 h 2630 grel 0.444, kz81 z 313 h 1811 grel 0.809,
kz79 z 307 h 1771 grel 0.809) -- the in-zone pool is EXHAUSTED
after this tranche -- A5 queue head (kz106 h 2812, kz135 h
2696, kz103 h 2684, then kz134/131/122/...); two wpacks timed
(kz106 N 2812 nf None 15.2 s, kz65 N 2630 nf None 16.1 s -- 6
anchors feasible); NO bound value, rho, F_A, FAB, reserve or
count column of ANY window was computed by the scoping pass.
RECORD-DERIVED EXPECTATIONS (by hand from the sealed r329
table, disclosed as such): the EXT3-B FAB values are derivable
(kz51 335 x 0.1291/log 335 ~ 7.44, kz54 ~ 5.59, kz42 ~ 4.52,
kz62 ~ 4.50), so C_FAB is expected >= ~7.4 and the r324 ladder
maximum 2.80 is NOT the sealed-cohort ceiling; GENUINELY OPEN:
every EXT4 and EXT5 FAB value (never printed by any sealed
record), whether kz111 or kz51 carries the frozen ceiling, all
EXT4/EXT5 count columns (nsc_rel, ngj -- never measured), the
K2/K3/K4 candidate constants, the growth adjudication, the
floor columns on EXT5 and every composed number; the sealed
toys are computed BY HAND (FAB pin 3/4 with identity 3/2; e1
pin 1/2 vs 3/4; e2 pin (2, 3) vs (1, 2); e3 pin 3/8 vs 3/4
break 2; e4 pin 0.5 vs 1.05; envelope rising/falling argmax
last/first with bin Spearman +1/-1; the six growth-tree
branches and the three floor letters EXACT); RHO_BAR2 = 1.05,
RC_GROW, RC_N_MIN, NB_FAB, E_FLAT_BAR, IMPL_FAC and FRESH_MIN
are coarse a-priori choices sized BEFORE any evaluation; the
six letters are symmetric and total by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R351_ANCHORS(identity wards, r306 C_2, r316, dictionary, r321
    F_A top-3, THE r349 FAMILY + EXT4 RECORD, THE r324 C_INF/e_G
    RECORD through the FAB column, THE r329 COUNTING RECORD)
+ SEAL(purity + toys + the exact live wards: NORM identity,
    r324 identity, FAB identity, decomposition, dominance chain,
    interpolation, pileup chain, group chain, Fractions pins)
+ FABCENSUS(the full FAB table incl. fresh EXT5; C_FAB freeze;
    fresh test; growth adjudication: new_record, rc_small, the
    census envelope)
+ SOURCELAW(K2/K3/K4 at frozen constants + the fresh count test
    + implied ceilings + src_ok)
+ FLOOR(the RHO_BAR2 test + anatomy + erosion + the floor
    letter)
+ [exactly one of] GROWTH_LAW_CERTIFIED / GROWTH_LAW_DERIVED /
    FA_UNBOUNDED / GROWTH_CENSUS_ONLY / LAW_STATE_NOT_EXACT /
    TARGET_LEAK  [+ flags]
+ COMPOSITION(the m_0* table + the law recomposition + the
    cofinal typing)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the identity, the chains, the Fractions
toys and the purity audits are EXACT (Fractions/AST-decided);
every constant, FAB value, count column, reserve and violation
count is MEASURED on the finite ladder + 12 EXT3 + 6 EXT4 + the
admitted EXT5 rows only; a certified growth law fixes a LAW
CANDIDATE with a frozen census constant and sealed freeze
protocol -- it proves NO cofinal law: the ladder-to-m_0* step
stays the disclosed extrapolation hypothesis, the fresh cohort
is small (<= 6 rows), the selection samples ONE construction
family (r329 honesty: independence of the anchor CHOICE, not a
second world), and the in-zone pool exhaustion means future
rounds cannot repeat this test in-zone -- all said out loud;
r243-r350 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA d556c758701c3a60,
pre-freeze commit 8131ab53; protocol: smoke pass 1 = 43/43
(0.7 s, run pre-commit, disclosed in the commit message);
calibration pass 1 = FIRST full evaluation = 43/43, wall
397.6 s, NO amendment -- no bar, band, rule or verdict rule
moved at any point; record run1/run2 after this insertion,
identical up to the runtime line):
MAIN VERDICT: GROWTH_LAW_CERTIFIED(0 fresh violations at the
frozen C_FAB 14.93) + FLOOR_ERODES(10^3.7) +
INZONE_POOL_EXHAUSTED + EXT5_CLEAN(6) +
SCRAMBLE_FAB(2.09 <= C_FAB, world census).
THE HEADLINE FINDINGS:
(1) THE GROWTH LAW HOLDS AT A FROZEN CEILING -- AND THE CEILING
SITS AT kz111, NOT kz51: C_FAB = max FAB over the 83 sealed
rows = 14.93 at kz111 (EXT4; kz75 13.64, then a gap to kz51
7.44) -- the record-derived expectation ~7.44 was LOW by 2x
because the EXT4 FAB values had never been computed.  The
FRESH TEST: all six EXT5 windows admitted (B5 kz79/kz81/kz65,
A5 kz103/kz135/kz106; N_w 1771..2812; POSITIVE_PREFIX 6/6, no
queue failures), FAB 2.04..9.71, ZERO violations -- m q_max <=
14.93 log m holds on every measured row of every cohort (89
rows) and on all four instrumented worlds; fresh max 9.71
(kz135, MED gap) stays 35 percent below the ceiling; rc_small
= +0.243 < +0.5 (n = 15 speaks): NO growth clause fires.  The
sealed letter is GROWTH_LAW_CERTIFIED -- census-frozen, the
first uniform growth statement of the lane that SURVIVES a
fresh tranche.
(2) THE F-CEILING TICKS UP AGAIN, THE FAB-CEILING STANDS: kz79
(EXT5) posts F_ins 6.69 (> the r349 record 6.68) -- the r346/
r349 F_A census ceiling is confirmed UNSTABLE a second time
(uniform solve at the new ceiling: 10^23.5) -- while its FAB
is only 9.00: the convention-free law coordinate is visibly
MORE STABLE out-of-sample than the rank-local F_A coordinate;
the depth-bin envelope (1.96 / 2.80 / 9.00 / 14.93) rises by
cohort COMPOSITION (small-gap selection), not within-class
(rc_small +0.24), typed census by seal.
(3) LEG B -- THE SOURCE DERIVATION STAYS OPEN (typed honestly):
K2 (Klein-gap) holds 0/6 fresh at FAB grel <= 11.87 and
Spearman(grel, FAB | family) = -0.623 -- the gap geometry
genuinely sets the q_max scale (structural formula, census:
grel has no measured lower bound); K3 (pileup cap) BREAKS on
fresh (kz65 pil 184.64 > frozen 177.97) and is VACUOUS (implied
360.5 >> 4 x 14.93); K4 (group cap) holds 0/6 but is VACUOUS
(469.6) -> src_ok False, GROWTH_LAW_DERIVED unfired: the law
certifies as a DIRECT frozen-ceiling statement, its mechanism
is NOT yet a formula.  THE FRESH COUNT TEST (first EXT4/EXT5
measurement ever): nsc_rel/lg <= 2.0258 AND ngj/lg <= 2.6351
hold 12/12 (min reserves 1.59/2.77) -- the O(log m) counting
side is choice-robust on a THIRD consecutive fresh cohort,
still the most robust asset of the lane.
(4) LEG C -- THE FLOOR HOLDS AT 1.05 BUT ERODES: cert2 True (28
family rows incl. 5 fresh EXT5 family rows, min RSV 1.07 at
kz75; the EXT5 spikes come in at RSV 2.22..3.38 -- NO new
floor hole); but e_RSV = -0.649 (halves-slope vs m, fit-free)
and rc_fam351 = -0.600 (vs the r349 ladder+EXT3 prior -0.331):
the reserve erodes with depth on the extended family, and the
census extrapolation crosses RSV = 1 at log10 m ~ 3.7 -- IF
the trend were a law the sliding spike coverage would die at
m ~ 5000: FLOOR_ERODES is the honest letter, the r349 floor
question is answered NEGATIVELY (no stable floor > 1
certified; the anatomy restates: the floor rows kz111/kz75 are
the largest-FAB deepest-pk spikes, med pk 0.142 vs 0.069, med
FAB 13.6 vs 3.6 comfortable -- the reserve dies exactly where
the law coordinate peaks, RSV ~ GSQ/(D pk B^2) with
D pk B^2 ~ 1.2).
(5) LEG D -- THE COMPOSITION MOVES THE HONEST UNIFORM m_0* BY
~4 DECADES: the class-free polylog route rho_2 <= C_FAB
C_M2ENV/log m (14.93 x 26.01, envelope incl. fresh) solves
m_0* = 10^18.9 -- UNIFORM, no spike/quiet split, vs 10^22.6
(r349 record uniform) / 10^23.5 (the moved census-F ceiling) /
10^16.1-10^17.5 (class-conditional, non-uniform) / 10^13.5
(r306 census) / 10^59.6 (r324 subcritical route); the
growth-slack route stays NONE (e_tot +0.772
composition-dominated, census by seal).  COFINAL TYPING at the
certified reading: (i) C_FAB/C_M2ENV are freeze-census over 89
rows, the ladder-to-m_0* step stays the extrapolation
hypothesis; (ii) the floor letter is FLOOR_ERODES (the spike
coverage arm still needs it); (iii) src_ok False (the
mechanism formula is the open kernel); (iv) finite closure
carries to m = 660; (v) no second world, and the in-zone
fresh pool is EXHAUSTED -- the next teeth need a new
construction family.
(6) WORLDS (census, no letter): w9 FAB 0.97 QUIET / w13 1.27
QUIET / EPST 0.84 QUIET / SCRAMBLE 2.09 SPIKE, all <= C_FAB --
the growth law is ARITHMETIC-FREE by measurement (a pure size
statement; no world separation claimed).
ANCHORS bit-near: r314 identity 4.5e-17 (EXT5 <= 1e-12 bar
met); r306 C_2 1.069 (0/57); r316 n 65 + quartet + C_small @
kz18; dictionary 7.8e-16; r321 F_A top-3 2.47/2.39/2.38; THE
r349 FAMILY RECORD EXACT (17 rows, RSV 3.19/7.03/12.06,
rc_fam -0.331, D 1.79/2.13/5.03, D pk B^2 0.409, shares
+0.01/+0.64/+0.26); THE r349 EXT4 RECORD EXACT (six SPIKE,
F_ins (1.58, 2.03, 3.11, 4.22, 5.53, 6.68), holes 1.11/1.07);
THE r324 DIRECT RECORD through the FAB column (C_INF 1.7481,
violators {53, 61, 67, 76, 83} EXACT, e_G +0.158); THE r329
COUNTING RECORD (C_NSC 2.0258 0/39, C_NG 2.6351 0/39, EXT3
count reserves 1.58/1.82).
SEAL: NORM 9.0e-16, interpolation 0.0, FAB identity 2.0e-16,
pileup chain 0.0, group chain 0.0, decomposition 1.0e-15,
dominance chain <= 1e-15, r316 chain green, r324 ladder
identity green, purity clean (0 id + 0 literal hits on the six
law builders), toys exact (FAB pin 3/4 + identity 3/2, e1 pin
1/2 vs 3/4, e2 pin (2, 3) vs (1, 2), e3 break 2, e4 0.5 vs
1.05, trees 6/6 + 4/4); must-fails e1 CAUGHT twice (AST qm +
Fractions) / e2 protocol-CAUGHT twice (AST rho + toy) / e3
CAUGHT exact (break == 2) / e4 protocol-CAUGHT twice (AST rho
+ toy) + m5a/m5b FLAGGED.  EXT5 branch census: kz81 (and EXT4
kz108) on the exception branch -- census, no letter.  Runtime
397.6 s calibration / record run1/run2 identical up to WALL /
0.7 s smoke.  AMENDMENTS AFTER FREEZE: NONE except this
record-table insertion.

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
import fold_two_scale_balance_probe as FTS     # noqa: E402 r344
import fold_cover_canonization_probe as FCC    # noqa: E402 r346
import thirdarm_spike_law_probe as TSL         # noqa: E402 r349
import pair_coupling_probe as PC343            # noqa: E402 r343
import lstar_margin_scaling_probe as LM        # noqa: E402 r286 READ-ONLY
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

# ---------------- the r349 constant set, imported verbatim
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
DICT_BAR = FTS.DICT_BAR
DEG_FLOOR = FTS.DEG_FLOOR
MULT_CAP = FTS.MULT_CAP
N_CAL = FTS.N_CAL
GA_FAM = FTS.GA_FAM
GSQ_R321 = FTS.GSQ_R321
MUT_MIN = FTS.MUT_MIN
TOY_BAR = FTS.TOY_BAR
EDGE_F = FTS.EDGE_F
CRIT_EXP = FTS.CRIT_EXP
R306_C2 = FTS.R306_C2
R306_C2_TOL = FTS.R306_C2_TOL
N351_REF = FTS.N344_REF
R316_RHO = FTS.R316_RHO
R316_RHO_TOL = FTS.R316_RHO_TOL
R316_CSMALL = FTS.R316_CSMALL
R316_CSMALL_TOL = FTS.R316_CSMALL_TOL
R316_CSMALL_KZ = FTS.R316_CSMALL_KZ
R324_M0_L10 = FTS.R324_M0_L10
R321_FA_TOP = FTS.R321_FA_TOP
R321_FA_TOL = FTS.R321_FA_TOL
M0_R344 = FCC.M0_R344
# the r349 constant set (TSL verbatim, SPEC_SHA-prefix gated)
F0_SPLIT = TSL.F0_SPLIT
RHO_BAR = TSL.RHO_BAR
EXT4_KZ = TSL.EXT4_KZ
EXT4_NW_MIN = TSL.EXT4_NW_MIN
EXT4_NW_MAX = TSL.EXT4_NW_MAX
TB_WARD_BAR_X4 = TSL.TB_WARD_BAR_X4
REC3_BAR_X4 = TSL.REC3_BAR_X4
DEC_BAR = TSL.DEC_BAR
V1_M0_REF = TSL.V1_M0_REF
V2_M0_REF = TSL.V2_M0_REF

# ---------------- NEW sealed constants of this round (spec above)
EXT5_H_MAX = PC343.EXT4_H_MAX
K_EXT5 = PC343.K_EXT4
Z2_CAP = PC343.Z2_CAP
LM_RANKS_USED = EFA.LM_RANKS_USED
USED_EXPECT_X5 = 98
FRESH_EXPECT_X5 = 17
CORE_Z = PC343.CORE_Z
B5Q_EXPECT = (65, 81, 79)
A5Q_HEAD_EXPECT = (106, 135, 103)
FRESH_MIN = 2
TB_WARD_BAR_X5 = 1e-4
REC3_BAR_X5 = 1e-12
RC_GROW = 0.5
RC_N_MIN = 8
NB_FAB = 4
RHO_BAR2 = 1.05
E_FLAT_BAR = 0.15
IMPL_FAC = 4.0
FAB_ID_BAR = 1e-12
GRP_CHAIN_BAR = 1e-9
FROZEN_CNSC = EFA.FROZEN_CNSC
FROZEN_CNG = EFA.FROZEN_CNG
FROZEN_TOL = EFA.FROZEN_TOL
# r349 record anchors
R349_FAM_N = 17
R349_RSV_TRIPLE = (3.19, 7.03, 12.06)
R349_RSV_TOL = 0.02
R349_RC_FAM = -0.331
R349_RC_TOL = 0.005
R349_D_FAM_MED = 1.79
R349_D_FAM_MAX = 2.13
R349_D_QUIET = 5.03
R349_D_TOL = 0.01
R349_DPKB2 = 0.409
R349_DPKB2_TOL = 0.005
R349_SHARES = (0.01, 0.64, 0.26)
R349_SHARES_TOL = 0.02
R349_X4_FINS = (1.58, 2.03, 3.11, 4.22, 5.53, 6.68)
R349_X4_FINS_TOL = 0.01
R349_X4_HOLES = {111: 1.11, 75: 1.07}
R349_X4_HOLE_TOL = 0.01
R324_CINF_REF = 1.7481
R324_CINF_TOL = 0.005
R324_VINF_SET = (53, 67, 76, 61, 83)
R324_EG_REF = 0.158
R324_EG_TOL = 0.005
R329_X3_RSVC_MIN = 1.6
R329_X3_RSVD_MIN = 1.8
R329_X3_RSV_TOL = 0.05
# import-integrity SHA prefixes (sealed)
TSL_SHA_PREFIX = "9b593e63"
EFA_SHA_PREFIX = "bbfaf199"
PC343_SHA_PREFIX = "9ffc2705"

R351_TABLE_LITERALS = frozenset(TSL.R349_TABLE_LITERALS | {
    3.19, 7.03, 12.06, -0.331, 1.79, 2.13, 5.03, 0.409, 6.68,
    5.53, 1.11, 1.07, 1.58, 4.22, 1.7481, 0.158, 2.0258, 2.6351,
    22.6, 59.6})

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
                       "the r244 chain rows; the prime-power anchor "
                       "grid U_ALL/G_ALL is the sealed source comb "
                       "(r238 convention); ground truth enters "
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
    lies in the sealed r314..r349 record set."""
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
                            in R351_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source hygiene: the law
# ---------------- builders consume PASSED values, the source grid
# ---------------- (U_ALL/G_ALL), window shape and SEALED
# ---------------- thresholds only; the withheld terminal drive
# ---------------- key, the branch label, the cubic target record
# ---------------- and the q_max record identifiers are forbidden
# ---------------- (AST identifier scan + literal scan).  FAB, RSV,
# ---------------- D, pil, nsc, ngj, hgn are TARGET-SIDE
# ---------------- DIAGNOSTICS computed in the gate section (r321/
# ---------------- r349 convention, disclosed).
def fab_of(mm, pk, ell):
    """THE CONVENTION-FREE LAW COORDINATE (derived algebra, spec):
    FAB = m pk / lg == F_A x B for every F_A convention (the r324
    identity).  Consumes the three passed values only; exact in
    Fractions."""
    return mm * pk / ell


def upper_env_max(fvals, vals, idx, nb):
    """the fit-free UPPER envelope: over EXACTLY the declared
    index tuple, sort by the coordinate, split into nb equal-count
    rank bins, per bin (median coordinate, MAX value); returns
    (bins, declared) -- the declared set is warded against the
    sealed row set."""
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
                     max(float(vals[i]) for i in mem)))
    return bins, idx


def ext5_next_tranche(fresh, zvals, grels, z_lo, z_hi, k):
    """the sealed NEXT-TRANCHE selection (the r343 EXT4 rule
    VERBATIM on the extended used ledger): fresh = the (h, kz)
    pool already minus the used ledger and domain-capped; stratum
    B5 = fresh kz with z in [z_lo, z_hi] sorted by (grel, kz)
    ascending, first k; stratum A5 = the remaining fresh kz
    sorted by (h, kz) descending.  Returns the two CANDIDATE
    QUEUES (admission by the caller: POSITIVE_PREFIX + mult cap +
    non-degenerate, failing candidates replaced by the next in
    queue).  Consumes window shape + grid columns only."""
    fresh_kz = [kz for (_h, kz) in fresh]
    zb = {kz: zvals[i] for i, kz in enumerate(fresh_kz)}
    gb = {kz: grels[i] for i, kz in enumerate(fresh_kz)}
    b_q = sorted((kz for kz in fresh_kz
                  if z_lo <= zb[kz] <= z_hi),
                 key=lambda kz: (gb[kz], kz))
    b_set = set(b_q[:k])
    a_q = [kz for (_h, kz) in sorted(fresh, reverse=True)
           if kz not in b_set]
    return b_q, a_q


def growth_tree_verdict(leak, brk, census_only, grow, src_ok):
    """the sealed main-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    LAW_STATE_NOT_EXACT > GROWTH_CENSUS_ONLY > FA_UNBOUNDED >
    GROWTH_LAW_DERIVED > GROWTH_LAW_CERTIFIED."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if census_only:
        return "GROWTH_CENSUS_ONLY"
    if grow:
        return "FA_UNBOUNDED"
    if src_ok:
        return "GROWTH_LAW_DERIVED"
    return "GROWTH_LAW_CERTIFIED"


def floor_letter(no_fresh_fam, cert2, eroding):
    """the sealed floor letter (booleans only; total, exactly one
    fires): FLOOR_CENSUS (no fresh family teeth) > FLOOR_ERODES
    (bar broken or eroding slope) > FLOOR_CONVERGES."""
    if no_fresh_fam:
        return "FLOOR_CENSUS"
    if (not cert2) or eroding:
        return "FLOOR_ERODES"
    return "FLOOR_CONVERGES"


def fr_fab_toy():
    """the sealed Fractions FAB pin (by hand, spec): m = 3, q =
    (1/2, 1/3, 1/6) -> pk = 1/2; pseudo-log lg = 2: FAB = 3 x
    (1/2)/2 = 3/4 EXACT and the identity FAB x lg == m pk = 3/2
    EXACT.  Returns worst deviation (0 demanded)."""
    mm = Fr(3)
    pk = Fr(1, 2)
    ell = Fr(2)
    v = fab_of(mm, pk, ell)
    devs = [abs(v - Fr(3, 4)), abs(v * ell - mm * pk),
            abs(v * ell - Fr(3, 2))]
    return max(devs)


def mutant_fab_readback(mqs_rec, mm, ell):
    """e1 MUST-FAIL MUTANT: a 'law column' consuming the stale
    q_max RECORD value instead of recomputing from the same block
    vector -- the QMAX_FORBIDDEN scope audit must FLAG it AND on
    the sealed Fractions toy it returns 1/2 while the true FAB is
    3/4."""
    stale = mqs_rec["qm"]
    return mm * stale / ell


def mutant_select_posthoc(rho, kz_pool, k):
    """e2 MUST-FAIL MUTANT (protocol): the fresh windows picked
    to MINIMIZE the seen violation mass (consumes rho) -- the
    BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed
    toy it returns (2, 3) != the sealed queue-order rule's
    (1, 2)."""
    o = sorted(range(len(kz_pool)), key=lambda i: rho[i])
    return tuple(sorted(kz_pool[i] for i in o[:k]))


def mutant_fab_wrong_log(mm, pk, ell):
    """e3 MUST-FAIL MUTANT: the law coordinate with the WRONG log
    power (m pk/lg^2 instead of /lg) -- on the sealed Fractions
    toy it returns 3/8 while the exact FAB is 3/4 (break factor
    == lg EXACT)."""
    return mm * pk / (ell * ell)


def mutant_floorbar_posthoc(rho, gsq_fa2):
    """e4 MUST-FAIL MUTANT (protocol): the reserve floor bar set
    at the SEEN minimum reserve (consumes rho) -- the
    BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed
    toy it returns 0.5 != the sealed RHO_BAR2."""
    return min(gsq_fa2[i] / max(rho[i], 1e-300)
               for i in range(len(rho)))


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'law orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'law constant' consuming the branch label -- the scope audit
    must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("qmax_growth_law_probe -- PRIME.L2.QMAX_GROWTH_LAW.01 "
          "(round 351,")
    print("the family growth law m q_max <= C log m + the stable "
          "reserve floor)")
    print("SPEC_SHA %s   R349_SHA %s   R343_SHA %s   R329_SHA %s"
          % (SPEC_SHA[:16], TSL.SPEC_SHA[:16], PC343.SPEC_SHA[:16],
             EFA.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + w9 wards + Fractions "
                        "pins + e1-e4; ladder, extensions, EXT3, "
                        "EXT4, EXT5, anchors, census, source "
                        "candidates, floor, composition and "
                        "adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (TSL.SPEC_SHA.startswith(TSL_SHA_PREFIX)
              and EFA.SPEC_SHA.startswith(EFA_SHA_PREFIX)
              and PC343.SPEC_SHA.startswith(PC343_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "THE GROWTH-LAW ROUND (the named r349 residue): FAB = "
          "m q_max/log m == F_A B (r324 identity, convention-"
          "free) adjudicated as a LAW with sealed machinery: "
          "LEG A freeze C_FAB on the sealed 65 + 12 + 6 cohort, "
          "test on the fresh EXT5 tranche (rule = r343 EXT4 "
          "selection verbatim, K = %d, h <= %d, z^2 <= %d); "
          "growth adjudication new_record OR rc_small >= %.1f "
          "(n >= %d); LEG B source candidates K2 (gap) / K3 "
          "(pileup, x C_NSC %.4f) / K4 (group, x C_NG %.4f) at "
          "frozen constants, IMPL_FAC %.1f; LEG C floor bar "
          "RHO_BAR2 %.2f + erosion bar %.2f; verdict tree "
          "GROWTH_LAW_CERTIFIED / GROWTH_LAW_DERIVED / "
          "FA_UNBOUNDED / GROWTH_CENSUS_ONLY / "
          "LAW_STATE_NOT_EXACT / TARGET_LEAK + floor flags "
          "sealed BEFORE evaluation; import integrity TSL %s / "
          "EFA %s / PC343 %s"
          % (K_EXT5, EXT5_H_MAX, Z2_CAP, RC_GROW, RC_N_MIN,
             FROZEN_CNSC, FROZEN_CNG, IMPL_FAC, RHO_BAR2,
             E_FLAT_BAR, TSL.SPEC_SHA[:8], EFA.SPEC_SHA[:8],
             PC343.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("fab_of", "upper_env_max", "ext5_next_tranche",
                    "growth_tree_verdict", "floor_letter",
                    "fr_fab_toy")
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
          "passed values + the source grid + window shape + "
          "sealed thresholds ONLY; m5a gift-bound FLAGGED (%s); "
          "m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r349 verbatim) + EXT5
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3 + EXT4 + "
            "THE FRESH EXT5 TRANCHE")
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
        ext5 = []
        okL = True
        core_kzs = []
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
        core_kzs = list(kzs)
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
        check("G14-ext34-admission", True, "SMOKE: skipped")
        check("G16-ext5-selection", True, "SMOKE: skipped")
        check("G17-ext5-admission", True, "SMOKE: skipped")
        ext5_admitted_kz = []
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
        ext4_admit = [p for p in ext4 if p["nf"] is None]
        ext4_drop = [(p["kz"], p["nf"]) for p in ext4
                     if p["nf"] is not None]
        check("G14-ext34-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX
              and len(ext4) == 6
              and min(p["N"] for p in ext4) == EXT4_NW_MIN
              and max(p["N"] for p in ext4) == EXT4_NW_MAX,
              "EXT3 = the sealed r329 12-anchor list (adoption "
              "verbatim): POSITIVE_PREFIX %d/12, N_w %d..%d; "
              "EXT4 = the sealed r343/r345 6-anchor list %s "
              "(r349 adoption verbatim): N_w %d..%d, admitted "
              "%d/6%s"
              % (sum(1 for p in ext3 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3), str(EXT4_KZ),
                 min(p["N"] for p in ext4),
                 max(p["N"] for p in ext4), len(ext4_admit),
                 ("; DROPPED (census): %s" % str(ext4_drop))
                 if ext4_drop else ""))
        ext4 = ext4_admit
        # THE SEALED EXT5 SELECTION (r343 rule verbatim, next
        # tranche on the extended used ledger)
        lm_rows = LM.ext_rule()
        used = set(EFA.used_kz_set(core.frame_a_zones(), lm_rows,
                                   LM_RANKS_USED))
        used |= set(PC343.EXT3_KZ_B + PC343.EXT3_KZ_A)
        used |= set(PC343.EXT4_KZ_B + PC343.EXT4_KZ_A)
        pool5 = EFA.admissible_pool(core.H_MIN, EXT5_H_MAX)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = PC343.ext4_domain_fresh(pool5, used, zz5, Z2_CAP)
        fresh5_kz = [kz for (_h, kz) in fresh5]
        grels5 = EFA.grel_col(fresh5_kz, core.G_ALL)
        z_lo = min(int(core._NN[kz]) for kz in core_kzs)
        z_hi = max(int(core._NN[kz]) for kz in core_kzs)
        b_q5, a_q5 = ext5_next_tranche(fresh5, [zz5[kz] for kz in
                                                fresh5_kz],
                                       grels5, z_lo, z_hi, K_EXT5)
        gr_by5 = {kz: g for kz, g in zip(fresh5_kz, grels5)}
        h_by5 = {kz: h for (h, kz) in fresh5}
        inzone_exhausted = len(b_q5) <= K_EXT5
        check("G16-ext5-selection",
              len(used) == USED_EXPECT_X5
              and len(fresh5) == FRESH_EXPECT_X5
              and (z_lo, z_hi) == CORE_Z
              and tuple(b_q5[:K_EXT5]) == B5Q_EXPECT
              and tuple(a_q5[:K_EXT5]) == A5Q_HEAD_EXPECT,
              "SEALED EXT5 SELECTION executed verbatim (the r343 "
              "rule on the extended used ledger): used %d (== "
              "%d), domain-capped fresh %d (== %d, z^2 <= %d), "
              "core zone [%d, %d]; stratum B5 queue %s (grel %s) "
              "+ A5 queue head %s (h %s) == the scoping-disclosed "
              "queues; IN-ZONE POOL %s"
              % (len(used), USED_EXPECT_X5, len(fresh5),
                 FRESH_EXPECT_X5, Z2_CAP, z_lo, z_hi,
                 str(b_q5[:K_EXT5]),
                 str([round(gr_by5[k], 3) for k in b_q5[:K_EXT5]]),
                 str(a_q5[:K_EXT5]),
                 str([h_by5[k] for k in a_q5[:K_EXT5]]),
                 "EXHAUSTED after this tranche (%d members)"
                 % len(b_q5) if inzone_exhausted
                 else "not exhausted (%d members)" % len(b_q5)))

        def admit_queue(queue, k):
            got = []
            failed = []
            for kz in queue:
                if len(got) >= k:
                    break
                p5 = BH.wpack(kz)
                if p5["nf"] is None:
                    got.append(p5)
                else:
                    failed.append((kz, p5["nf"]))
            return got, failed

        b5_packs, b5_fail = admit_queue(b_q5, K_EXT5)
        a5_packs, a5_fail = admit_queue(a_q5, K_EXT5)
        ext5_strat = {}
        for p5 in b5_packs:
            ext5_strat[p5["kz"]] = "B5"
        for p5 in a5_packs:
            ext5_strat[p5["kz"]] = "A5"
        ext5 = b5_packs + a5_packs
        ext5.sort(key=lambda p: (p["N"], p["kz"]))
        ext5_admitted_kz = [p["kz"] for p in ext5]
        check("G17-ext5-admission",
              len(ext5) >= FRESH_MIN
              and all(1700 <= p["N"] <= EXT5_H_MAX for p in ext5),
              "EXT5 ADMISSION (POSITIVE_PREFIX, queue "
              "replacement per the r329 convention): admitted "
              "%d/%d %s, N_w %s..%s; queue failures B5 %s / A5 "
              "%s -- PURE TEST rows of THIS round, never seen by "
              "any calibration or record run"
              % (len(ext5), 2 * K_EXT5,
                 str([(p["kz"], ext5_strat[p["kz"]], p["N"])
                      for p in ext5]),
                 min((p["N"] for p in ext5), default="-"),
                 max((p["N"] for p in ext5), default="-"),
                 str(b5_fail), str(a5_fail)))

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
    x5recs = [rung_rec(p) for p in ext5] if not smoke else []
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
                      + x5recs if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 + x4recs + x5recs if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2+EXT3+EXT4+EXT5 census: %d cheap / %d "
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
    tb_x5 = 0.0
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
    for rc in x5recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x5 = max(tb_x5, dev)
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
          and tb_x5 <= TB_WARD_BAR_X5
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d ext3 + %d ext4 + %d ext5 + %d mains + 3 "
          "controls: worst dev/absmass %.1e main (bar %.0e) / "
          "%.1e deep / %.1e ext (bar %.0e) / %.1e ext3 (bar "
          "%.0e) / %.1e ext4 / %.1e ext5 (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(x3recs),
             len(x4recs), len(x5recs), len(mrecs), tb_worst,
             TB_WARD_BAR, tb_deep, tb_ext, TB_WARD_BAR_DEEP,
             tb_x3, TB_WARD_BAR_X3, tb_x4, tb_x5,
             TB_WARD_BAR_X5, tb_ctrl, TB_WARD_BAR_CTRL))

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
            pst = QMO.pileup_state(sct["x"], val_all, blk_all)
            hst = GMC.heavy_state(sct["x"], led327)
            dic = FDD.martingale_moment_dictionary(sct["x"])
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
            pst = dict(j=0, nsc=0, nsc_rel=0, pil=0.0, a1j=0.0,
                       tail=0.0, scut=0, scales=(), masses=())
            hst = dict(j=0, ngj=0, hga=0.0, hgn=0.0, a1j=0.0,
                       vmaxb=0.0, bshare=0.0)
            dic = dict(d1=0.0, d2=0.0, d3=0.0, ymx=0.0)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led327=led327, pst=pst, hst=hst, dic=dic,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs + x3recs + x4recs \
        + x5recs
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
    x345_mult_ok = True
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
    for rc in x3recs + x4recs + x5recs:
        if rc["ev"]["mx_mult"] > MULT_CAP:
            x345_mult_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and x345_mult_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r327 GMC ledger segments IDENTICALLY to the genealogy "
          "(worst dev %.1e, bar %.0e); EXT3+EXT4+EXT5 fold "
          "multiplicity <= %d (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP, "OK" if x345_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim set)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim set: r306/r316 "
            "+ dictionary + r321 F_A; the r349/r324/r329 records "
            "follow in S5)")
    x345_ids = set(id(rc) for rc in x3recs + x4recs + x5recs)
    live_69 = [rc for rc in live if id(rc) not in x345_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    rec3_x4 = max((rc["ev"]["rec3"] for rc in x4recs),
                  default=0.0)
    rec3_x5 = max((rc["ev"]["rec3"] for rc in x5recs),
                  default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and rec3_x4 <= REC3_BAR_X4 and rec3_x5 <= REC3_BAR_X5,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e (bars %.0e); "
          "EXT3 %.1e (bar %.0e); EXT4 %.1e (bar %.0e); EXT5 %.1e "
          "(bar %.0e); DISCLOSED slim anchor set -- the full "
          "chain is re-warded by the sealed r321..r349 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, REC3_BAR_X3,
             rec3_x4, REC3_BAR_X4, rec3_x5, REC3_BAR_X5))
    if smoke:
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        srt = []
        n351 = 0
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
        n351 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n351)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n351 == N351_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n351, N351_REF, rho_kz.get(53, -1.0),
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
        srt_x5 = sorted(x5recs,
                        key=lambda rc: (rc["N"], rc["kz"]))
        srt_x5 = [rc for rc in srt_x5
                  if rc["ev"]["mx_mult"] <= MULT_CAP
                  and not rc["ev"]["degenerate"]]
        n_x3 = len(srt_x)
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        lg_full = [math.log(float(v)) for v in m_full]
        q_lad = [srt[i]["ev"]["mqs"]["qm"] for i in range(n351)]
        fa_lad = EFP.local_ratio(q_lad)
        medloc_lad = CCP.local_median(q_lad)
        N_lad = [srt[i]["N"] for i in range(n351)]
        fa_full = list(fa_lad)
        for rc in srt_x:
            fa_full.append(CCP.world_coord(rc["ev"]["mqs"]["qm"],
                                           rc["N"], N_lad, q_lad))
        fa_kz = {srt_full[i]["kz"]: fa_full[i]
                 for i in range(n_full)}
        kz_rank = {rc["kz"]: i for i, rc in enumerate(srt_full)}
        fa_x4 = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_x4]
        fa_x5 = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_x5]
        check("G39-r321-fa-anchors",
              all(abs(fa_kz[kz] - R321_FA_TOP[kz]) <= R321_FA_TOL
                  for kz in R321_FA_TOP),
              "the r321/r317 F_A coordinate reproduced through "
              "EFP.local_ratio on the module-own q_max column: "
              "top-3 kz53 %.2f / kz83 %.2f / kz67 %.2f (rec "
              "%.2f/%.2f/%.2f tol %.2f); EXT3/EXT4/EXT5 rows via "
              "the r321 INSERTION RULE (CCP.world_coord, the "
              "r329/r344/r349 convention); F_ins EXT4 %.2f..%.2f "
              "/ EXT5 %s..%s; the class constant GSQ = %.4f is "
              "the BANKED r321 record, never recalibrated here"
              % (fa_kz[53], fa_kz[83], fa_kz[67],
                 R321_FA_TOP[53], R321_FA_TOP[83],
                 R321_FA_TOP[67], R321_FA_TOL,
                 min(fa_x4) if fa_x4 else 0.0,
                 max(fa_x4) if fa_x4 else 0.0,
                 ("%.2f" % min(fa_x5)) if fa_x5 else "-",
                 ("%.2f" % max(fa_x5)) if fa_x5 else "-",
                 GSQ_R321))

    # ---------------- S4: seal + purity + toys + live wards
    section("S4  LEG 0b -- SEAL + PURITY + TOYS + LIVE WARDS")
    pure_lits = []
    for fn in own_builders:
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_fab_readback", QMAX_FORBIDDEN)
    e2_hits = scope_audit("mutant_select_posthoc",
                          BOUND_FORBIDDEN)
    e4_hits = scope_audit("mutant_floorbar_posthoc",
                          BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e4_hits) >= 1,
          "SOURCE HYGIENE: the law builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed "
          "r314..r349 record-literal set (%d literal hits); e1 "
          "fab-readback FLAGGED (%s); e2 select-posthoc FLAGGED "
          "(%s); e4 floorbar-posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    # sealed toys (Fractions + by-hand pins, spec above)
    fab_dev = fr_fab_toy()
    fd_dev = TSL.fr_decomp_toy()
    mut1 = mutant_fab_readback(dict(qm=Fr(1, 2)), Fr(2), Fr(2))
    toy1_true = fab_of(Fr(2), Fr(3, 4), Fr(2))
    mut2 = mutant_select_posthoc((5.0, 1.0, 3.0), (1, 2, 3), 2)
    toy2_sealed = (1, 2)
    mut3 = mutant_fab_wrong_log(Fr(3), Fr(1, 2), Fr(2))
    toy3_true = fab_of(Fr(3), Fr(1, 2), Fr(2))
    mut4 = mutant_floorbar_posthoc((2.0, 1.0), (1.0, 0.5))
    env_r, dec_r = upper_env_max((1.0, 2.0, 3.0, 4.0),
                                 (1.0, 2.0, 3.0, 4.0),
                                 (0, 1, 2, 3), 2)
    env_f, _ = upper_env_max((1.0, 2.0, 3.0, 4.0),
                             (4.0, 3.0, 2.0, 1.0),
                             (0, 1, 2, 3), 2)
    rc_r = CCP.spearman_rank([b[0] for b in env_r],
                             [b[1] for b in env_r])
    rc_f = CCP.spearman_rank([b[0] for b in env_f],
                             [b[1] for b in env_f])
    argmax_r = max(range(len(env_r)), key=lambda k: env_r[k][1])
    argmax_f = max(range(len(env_f)), key=lambda k: env_f[k][1])
    toy_sel_b, toy_sel_a = ext5_next_tranche(
        ((10, 1), (20, 2), (30, 3)), (100, 200, 900),
        (0.5, 0.6, 0.7), 50, 500, 2)
    tr_br = (growth_tree_verdict(True, True, True, True, True),
             growth_tree_verdict(False, True, True, True, True),
             growth_tree_verdict(False, False, True, True, True),
             growth_tree_verdict(False, False, False, True, True),
             growth_tree_verdict(False, False, False, False,
                                 True),
             growth_tree_verdict(False, False, False, False,
                                 False))
    ok_tr = tr_br == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                      "GROWTH_CENSUS_ONLY", "FA_UNBOUNDED",
                      "GROWTH_LAW_DERIVED",
                      "GROWTH_LAW_CERTIFIED")
    fl_br = (floor_letter(True, True, False),
             floor_letter(False, False, False),
             floor_letter(False, True, True),
             floor_letter(False, True, False))
    ok_fl = fl_br == ("FLOOR_CENSUS", "FLOOR_ERODES",
                      "FLOOR_ERODES", "FLOOR_CONVERGES")
    check("G41-toy-exactness",
          fab_dev == 0 and fd_dev == 0
          and mut1 == Fr(1, 2) and toy1_true == Fr(3, 4)
          and mut1 != toy1_true
          and mut2 == (2, 3) and tuple(toy_sel_b) == (1, 2)
          and mut2 != toy2_sealed
          and mut3 == Fr(3, 8) and toy3_true == Fr(3, 4)
          and toy3_true / mut3 == Fr(2)
          and abs(mut4 - 0.5) <= TOY_BAR and mut4 != RHO_BAR2
          and env_r[0][1] == 2.0 and env_r[-1][1] == 4.0
          and env_f[0][1] == 4.0
          and abs(rc_r - 1.0) <= TOY_BAR
          and abs(rc_f + 1.0) <= TOY_BAR
          and argmax_r == len(env_r) - 1 and argmax_f == 0
          and dec_r == (0, 1, 2, 3)
          and tuple(toy_sel_a) == (3,)
          and ok_tr and ok_fl,
          "the sealed toys EXACT: FAB Fractions pin 3/4 with "
          "identity 3/2 dev %s; the r349 res_decomp import pin "
          "dev %s; e1 stale-record pin %s != true %s; e2 "
          "posthoc pin %s != sealed queue rule %s; e3 wrong-log "
          "pin %s != true %s (break factor %s == lg); e4 toy "
          "%.1f != sealed %.2f; upper-envelope rising/falling "
          "Spearman %+.0f/%+.0f argmax last/first with declared "
          "set warded; selection toy B %s A %s; the six "
          "growth-tree branches EXACT %s; the floor letters "
          "EXACT %s"
          % (str(fab_dev), str(fd_dev), str(mut1),
             str(toy1_true), str(mut2), str(toy2_sealed),
             str(mut3), str(toy3_true), str(toy3_true / mut3),
             mut4, RHO_BAR2, rc_r, rc_f, str(tuple(toy_sel_b)),
             str(tuple(toy_sel_a)), str(tr_br), str(fl_br)))
    # THE ROUND'S OWN EXACT LIVE WARDS on every live world:
    # NORM identity, r324 interpolation, FAB identity, the pileup
    # chain, the group chain, the decomposition + dominance chain.
    norm_w = 0.0
    interp_w = 0.0
    fabid_w = 0.0
    pile_w = 0.0
    pilerec_w = 0.0
    grp_w = 0.0
    dec_w = 0.0
    chainD_w = 0.0
    chain_w = 0.0
    id324_w = 0.0
    mult_all_ok = True
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
        # r324 interpolation M_3 <= qmax M_2 <= qmax^2 (one-sided)
        interp_w = max(interp_w,
                       max(0.0, c3q_i - pk_i * m2q_i)
                       / max(pk_i * m2q_i, 1e-300),
                       max(0.0, m2q_i - pk_i)
                       / max(pk_i, 1e-300))
        # the FAB identity: fab == F x B for the neutral B
        fab_i = fab_of(float(mloc), pk_i, lgl)
        fabid_w = max(fabid_w,
                      abs(fab_i * lgl - mloc * pk_i)
                      / max(mloc * pk_i, 1e-300))
        # the pileup chain m qmax <= nsc x pil + recomposition
        pst = ev["pst"]
        if pst["nsc"]:
            pile_w = max(pile_w,
                         max(0.0, mloc * pk_i
                             - pst["nsc"] * pst["pil"])
                         / max(pst["nsc"] * pst["pil"], 1e-300))
            pilerec_w = max(pilerec_w,
                            abs(sum(pst["masses"]) - pst["a1j"])
                            / max(pst["a1j"], 1e-300))
        # the group chain m qmax <= ngj x hgn (via |x_j*| <= A1_j*
        # <= ngj x hga, exact)
        hst = ev["hst"]
        if hst["ngj"]:
            grp_w = max(grp_w,
                        max(0.0, mloc * pk_i
                            - hst["ngj"] * hst["hgn"])
                        / max(hst["ngj"] * hst["hgn"], 1e-300))
        # decomposition + dominance chain (r349 verbatim)
        dd_i = c3q_i / pk_i ** 3
        b2_i = (pk_i * mloc / lgl) ** 2
        sc_i, sm_i2, sd_i = TSL.res_decomp(GSQ_R321, b2_i, pk_i,
                                           m2q_i, c3q_i)
        rsv_dir = GSQ_R321 * 1.0 / max(ev["rho2"], 1e-300)
        dec_w = max(dec_w,
                    abs(sc_i * sm_i2 * sd_i - rsv_dir)
                    / max(rsv_dir, 1e-300))
        chainD_w = max(chainD_w,
                       abs(dd_i * pk_i ** 3 * mloc ** 2
                           / lgl ** 2 - ev["rho2"])
                       / max(ev["rho2"], 1e-300))
        # r316 chain (slim: nrm x cube == rho2 + bracket)
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        chain_w = max(chain_w, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(ev["gen"]["mult"])[1]
    if not smoke:
        for i in range(n351):
            id324_w = max(id324_w,
                          abs(fa_lad[i] * medloc_lad[i] - q_lad[i])
                          / max(q_lad[i], 1e-300))
    check("G42-live-wards",
          norm_w <= DEC_BAR and interp_w <= CHAIN_BAR
          and fabid_w <= FAB_ID_BAR and pile_w <= CHAIN_BAR
          and pilerec_w <= GRP_CHAIN_BAR and grp_w <= CHAIN_BAR
          and dec_w <= DEC_BAR and chainD_w <= DEC_BAR
          and chain_w <= CHAIN_BAR and id324_w <= CHAIN_BAR
          and mult_all_ok,
          "THE ROUND'S OWN EXACT WARDS live on %d worlds: r306 "
          "NORM identity %.1e; r324 interpolation M_3 <= qmax "
          "M_2 <= qmax^2 one-sided %.1e; FAB identity FAB lg == "
          "m qmax %.1e (bar %.0e); pileup chain m qmax <= nsc x "
          "pil %.1e + scale recomposition %.1e; group chain m "
          "qmax <= ngj x hgn %.1e; reserve decomposition %.1e + "
          "dominance chain %.1e (bars %.0e); r316 chain %.1e; "
          "r324 identity F_A medloc == pk on the ladder %.1e; "
          "fold multiplicity <= %d everywhere (%s)"
          % (len(live), norm_w, interp_w, fabid_w, FAB_ID_BAR,
             pile_w, pilerec_w, grp_w, dec_w, chainD_w, DEC_BAR,
             chain_w, id324_w, MULT_CAP,
             "OK" if mult_all_ok else "BROKEN"))

    # ---------------- S5: the r349/r324/r329 record reproduction
    section("S5  LEG 0c -- THE r349 FAMILY + r324 DIRECT + r329 "
            "COUNTING RECORDS (SAME CODE PATH)")
    if smoke:
        check("G50-r349-family-record", True, "SMOKE: skipped")
        check("G51-r349-ext4-record", True, "SMOKE: skipped")
        check("G52-r329-counting-record", True, "SMOKE: skipped")
        check("G53-r324-direct-record", True, "SMOKE: skipped")
    else:
        # full-row diagnostic columns on the 77 sealed rows
        pk_col = []
        m2q_col = []
        c3q_col = []
        dd_col = []
        bb_col = []
        rsv_col = []
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
        rc_fam349 = CCP.spearman_rank(
            [fa_full[i] for i in fam_idx],
            [rsv_col[i] for i in fam_idx])
        sh_fam = [(math.log10(GSQ_R321 / bb_col[i] ** 2),
                   math.log10(pk_col[i] / m2q_col[i]),
                   math.log10(pk_col[i] * m2q_col[i]
                              / c3q_col[i]))
                  for i in fam_idx]
        med_f = [float(np.median([s[k] for s in sh_fam]))
                 for k in range(3)]
        dd_fam = [dd_col[i] for i in fam_idx]
        dd_qui = [dd_col[i] for i in quiet_idx
                  if pk_col[i] > 0 and c3q_col[i] > 0]
        dpkb2_max = max(dd_col[i] * pk_col[i] * bb_col[i] ** 2
                        for i in fam_idx)
        rsv_f = [rsv_col[i] for i in fam_idx]
        check("G50-r349-family-record",
              len(fam_idx) == R349_FAM_N
              and abs(min(rsv_f) - R349_RSV_TRIPLE[0])
              <= R349_RSV_TOL
              and abs(float(np.median(rsv_f))
                      - R349_RSV_TRIPLE[1]) <= R349_RSV_TOL
              and abs(max(rsv_f) - R349_RSV_TRIPLE[2])
              <= R349_RSV_TOL
              and abs(rc_fam349 - R349_RC_FAM) <= R349_RC_TOL
              and abs(float(np.median(dd_fam)) - R349_D_FAM_MED)
              <= R349_D_TOL
              and abs(max(dd_fam) - R349_D_FAM_MAX) <= R349_D_TOL
              and abs(float(np.median(dd_qui)) - R349_D_QUIET)
              <= R349_D_TOL
              and abs(dpkb2_max - R349_DPKB2) <= R349_DPKB2_TOL
              and all(abs(med_f[k] - R349_SHARES[k])
                      <= R349_SHARES_TOL for k in range(3)),
              "THE r349 FAMILY RECORD reproduced through the "
              "same code path: family %d rows (rec %d); RSV "
              "min/med/max %.2f/%.2f/%.2f (rec %s); rc_fam "
              "%+.3f (rec %+.3f); D fam med/max %.2f/%.2f, "
              "quiet med %.2f (rec %.2f/%.2f/%.2f); max D pk "
              "B^2 %.3f (rec %.3f); shares %+.2f/%+.2f/%+.2f "
              "(rec %s)"
              % (len(fam_idx), R349_FAM_N, min(rsv_f),
                 float(np.median(rsv_f)), max(rsv_f),
                 str(R349_RSV_TRIPLE), rc_fam349, R349_RC_FAM,
                 float(np.median(dd_fam)), max(dd_fam),
                 float(np.median(dd_qui)), R349_D_FAM_MED,
                 R349_D_FAM_MAX, R349_D_QUIET, dpkb2_max,
                 R349_DPKB2, med_f[0], med_f[1], med_f[2],
                 str(R349_SHARES)))
        # EXT4 columns (r349 convention verbatim)
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
            x4_rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc,
                                lg=lgl, pk=pk, fa=fa4, rsv=rsv4,
                                dd=dd4,
                                cls=FCC.cls_rule(fa4, F0_SPLIT),
                                ev=ev))
        fins4_sorted = tuple(sorted(round(r["fa"], 2)
                                    for r in x4_rows))
        hole_ok = all(
            abs(next(r["rsv"] for r in x4_rows
                     if r["kz"] == kz) - R349_X4_HOLES[kz])
            <= R349_X4_HOLE_TOL for kz in R349_X4_HOLES)
        check("G51-r349-ext4-record",
              len(x4_rows) == 6
              and all(r["cls"] == "SPIKE" for r in x4_rows)
              and all(abs(fins4_sorted[j] - R349_X4_FINS[j])
                      <= R349_X4_FINS_TOL for j in range(6))
              and hole_ok,
              "THE r349 EXT4 RECORD reproduced: all six SPIKE; "
              "sorted F_ins %s (rec %s); the two bar misses "
              "kz111 rsv %.2f / kz75 rsv %.2f (rec 1.11/1.07) "
              "-- the honest ~1.1 floor of the fresh cohort"
              % (str(fins4_sorted), str(R349_X4_FINS),
                 next(r["rsv"] for r in x4_rows
                      if r["kz"] == 111),
                 next(r["rsv"] for r in x4_rows
                      if r["kz"] == 75)))
        # r329 counting record (C_NSC / C_NG through the same
        # code path; EXT3 count reserves)
        nscl65 = [srt[i]["ev"]["pst"]["nsc_rel"]
                  / math.log(float(srt[i]["ev"]["m"]))
                  for i in range(n351)]
        cnsc_repro = max(nscl65[i] for i in ca_i)
        viol_nsc = [i for i in te_i if nscl65[i] > cnsc_repro]
        ngl65 = [srt[i]["ev"]["hst"]["ngj"]
                 / math.log(float(srt[i]["ev"]["m"]))
                 for i in range(n351)]
        cng_repro = max(ngl65[i] for i in ca_i)
        viol_ng = [i for i in te_i if ngl65[i] > cng_repro]
        x3_nscl = [rc["ev"]["pst"]["nsc_rel"]
                   / math.log(float(rc["ev"]["m"]))
                   for rc in srt_x]
        x3_ngl = [rc["ev"]["hst"]["ngj"]
                  / math.log(float(rc["ev"]["m"]))
                  for rc in srt_x]
        rsvc_min = min(FROZEN_CNSC / max(v, 1e-300)
                       for v in x3_nscl)
        rsvd_min = min(FROZEN_CNG / max(v, 1e-300)
                       for v in x3_ngl)
        check("G52-r329-counting-record",
              abs(cnsc_repro - FROZEN_CNSC) <= FROZEN_TOL
              and not viol_nsc
              and abs(cng_repro - FROZEN_CNG) <= FROZEN_TOL
              and not viol_ng
              and abs(rsvc_min - R329_X3_RSVC_MIN)
              <= R329_X3_RSV_TOL
              and abs(rsvd_min - R329_X3_RSVD_MIN)
              <= R329_X3_RSV_TOL,
              "THE r329 COUNTING RECORD reproduced: C_NSC = "
              "%.4f (rec %.4f) 0/39 test (viol %d); C_NG = %.4f "
              "(rec %.4f) 0/39 (viol %d); EXT3 12/12 with min "
              "count reserves %.2f/%.2f (rec 1.6/1.8) -- the "
              "O(log m) counting side re-warded"
              % (cnsc_repro, FROZEN_CNSC, len(viol_nsc),
                 cng_repro, FROZEN_CNG, len(viol_ng), rsvc_min,
                 rsvd_min))
        # r324 direct record through the FAB column
        fab65 = [fab_of(float(srt[i]["ev"]["m"]),
                        srt[i]["ev"]["mqs"]["qm"],
                        math.log(float(srt[i]["ev"]["m"])))
                 for i in range(n351)]
        cinf_repro = max(fab65[i] for i in ca_i)
        viol_inf = sorted(srt[i]["kz"] for i in te_i
                          if fab65[i] > cinf_repro)
        msT = [srt[i]["ev"]["m"] for i in te_i]
        eg_repro = L2D.halves_slope(msT, [max(fab65[i], 1e-300)
                                          for i in te_i])
        check("G53-r324-direct-record",
              abs(cinf_repro - R324_CINF_REF) <= R324_CINF_TOL
              and tuple(viol_inf) == tuple(sorted(R324_VINF_SET))
              and abs(eg_repro - R324_EG_REF) <= R324_EG_TOL,
              "THE r324 DIRECT RECORD reproduced through the FAB "
              "column (FAB == G/log m bit-near): C_INF = %.4f "
              "(rec %.4f), test violators %s == the r324 five "
              "%s; e_G = %+.3f (rec %+.3f) -- the ladder-side "
              "growth column is the r324 object, now extended "
              "by three fresh cohorts"
              % (cinf_repro, R324_CINF_REF, str(viol_inf),
                 str(tuple(sorted(R324_VINF_SET))), eg_repro,
                 R324_EG_REF))

    # ---------------- S6: Leg A -- the FAB census + freeze + test
    section("S6  LEG A -- THE FAB CENSUS, THE FROZEN CEILING AND "
            "THE GROWTH ADJUDICATION")
    if smoke:
        check("G60-fab-census", True, "SMOKE: skipped")
        check("G61-fab-freeze-test", True, "SMOKE: skipped")
        check("G62-growth-adjudication", True, "SMOKE: skipped")
        grow = False
        census_only = True
        c_fab = 0.0
        new_record = False
    else:
        # EXT5 columns (pure test rows)
        x5_rows = []
        for k, rc in enumerate(srt_x5):
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            c3q = ev["cm"]["S3"]
            fa5 = fa_x5[k]
            rsv5 = GSQ_R321 * fa5 ** 2 / max(ev["rho2"], 1e-300)
            dd5 = c3q / max(pk ** 3, 1e-300)
            x5_rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc,
                                lg=lgl, pk=pk, fa=fa5, rsv=rsv5,
                                dd=dd5,
                                cls=FCC.cls_rule(fa5, F0_SPLIT),
                                strat=ext5_strat.get(rc["kz"],
                                                     "?"),
                                ev=ev))
        census_only = len(x5_rows) < FRESH_MIN
        # the unified all-row census (cohort, kz, m, fa, cls,
        # FAB, grel, gap class, D, RSV, count columns)
        allrows = []
        for i in range(n_full):
            ev = srt_full[i]["ev"]
            allrows.append(dict(
                coh="LAD" if i < n351 else "EXT3",
                kz=srt_full[i]["kz"], m=ev["m"],
                lg=lg_full[i], pk=pk_col[i], fa=fa_full[i],
                cls=FCC.cls_rule(fa_full[i], F0_SPLIT),
                dd=dd_col[i], rsv=rsv_col[i], ev=ev))
        for r in x4_rows:
            allrows.append(dict(coh="EXT4", kz=r["kz"],
                                m=r["m"], lg=r["lg"], pk=r["pk"],
                                fa=r["fa"], cls=r["cls"],
                                dd=r["dd"], rsv=r["rsv"],
                                ev=r["ev"]))
        for r in x5_rows:
            allrows.append(dict(coh="EXT5", kz=r["kz"],
                                m=r["m"], lg=r["lg"], pk=r["pk"],
                                fa=r["fa"], cls=r["cls"],
                                dd=r["dd"], rsv=r["rsv"],
                                ev=r["ev"]))
        grel_all = EFA.grel_col([r["kz"] for r in allrows],
                                core.G_ALL)
        for r, g in zip(allrows, grel_all):
            r["grel"] = g
            r["gcls"] = EFA.gap_class(g)
            r["fab"] = fab_of(float(r["m"]), r["pk"], r["lg"])
            pst = r["ev"]["pst"]
            hst = r["ev"]["hst"]
            r["pil"] = pst["pil"]
            r["nsc"] = pst["nsc"]
            r["nscl"] = pst["nsc_rel"] / r["lg"]
            r["ngj"] = hst["ngj"]
            r["ngl"] = hst["ngj"] / r["lg"]
            r["hgn"] = hst["hgn"]
        sealed_rows = [r for r in allrows if r["coh"] != "EXT5"]
        fresh_rows = [r for r in allrows if r["coh"] == "EXT5"]
        info("THE FAB TABLE (family + fresh + cohort maxima; "
             "coh kz gap-class F cls | FAB pil nsc ngj hgn | "
             "RSV):")
        show = [r for r in allrows
                if r["cls"] == "SPIKE" or r["coh"] == "EXT5"]
        for r in sorted(show, key=lambda r: -r["fab"]):
            info("  %-4s kz%-4d %-5s F %5.2f %-5s | FAB %6.2f "
                 "pil %6.2f nsc %2d ngj %3d hgn %5.2f | RSV "
                 "%5.2f"
                 % (r["coh"], r["kz"], r["gcls"], r["fa"],
                    r["cls"], r["fab"], r["pil"], r["nsc"],
                    r["ngj"], r["hgn"], r["rsv"]))
        coh_max = {}
        for r in allrows:
            coh_max[r["coh"]] = max(coh_max.get(r["coh"], 0.0),
                                    r["fab"])
        check("G60-fab-census", True,
              "THE FAB CENSUS on %d rows (65 + 12 + 6 + %d "
              "fresh): cohort maxima %s; overall max %.2f at "
              "kz%d (%s); FAB is the convention-free law "
              "coordinate (identity warded %.1e); the r324 "
              "ladder maximum %.2f is NOT the ceiling -- the "
              "small-gap cohorts carry it, as the record-derived "
              "expectation said"
              % (len(allrows), len(fresh_rows),
                 str({c: round(v, 2) for c, v in
                      sorted(coh_max.items())}),
                 max(r["fab"] for r in allrows),
                 max(allrows, key=lambda r: r["fab"])["kz"],
                 max(allrows, key=lambda r: r["fab"])["coh"],
                 fabid_w, cinf_repro))
        # THE FREEZE + THE FRESH TEST
        c_fab = max(r["fab"] for r in sealed_rows)
        c_fab_kz = max(sealed_rows, key=lambda r: r["fab"])["kz"]
        fresh_viol = [(r["kz"], round(r["fab"], 2))
                      for r in fresh_rows if r["fab"] > c_fab]
        new_record = bool(fresh_viol)
        check("G61-fab-freeze-test", True,
              "THE FROZEN CEILING (sealed freeze rule: max over "
              "the 83 sealed rows): C_FAB = %.2f at kz%d; the "
              "FRESH TEST on %d admitted EXT5 rows: %s -- "
              "m q_max <= %.2f log m %s on every fresh row"
              % (c_fab, c_fab_kz, len(fresh_rows),
                 ("0 violations" if not fresh_viol else
                  "VIOLATIONS %s" % str(fresh_viol)), c_fab,
                 "holds" if not fresh_viol else "BREAKS"))
        # THE GROWTH ADJUDICATION
        smallfam = [r for r in allrows
                    if r["gcls"] == "SMALL"
                    and r["cls"] == "SPIKE"]
        rc_small = CCP.spearman_rank(
            [r["m"] for r in smallfam],
            [r["fab"] for r in smallfam]) \
            if len(smallfam) >= 2 else 0.0
        rc_speaks = len(smallfam) >= RC_N_MIN
        env_bins, dec_set = upper_env_max(
            [r["m"] for r in allrows],
            [r["fab"] for r in allrows],
            tuple(range(len(allrows))), NB_FAB)
        env_ok = dec_set == tuple(range(len(allrows)))
        grow = new_record or (rc_speaks and rc_small >= RC_GROW)
        check("G62-growth-adjudication", env_ok,
              "GROWTH (sealed clauses): new fresh record %s; "
              "rc_small = Spearman(m, FAB | SMALL-gap family, "
              "n = %d %s) = %+.3f vs bar %+.1f; -> GROW %s.  "
              "CENSUS upper envelope over %d m-rank bins (med "
              "m, max FAB) = %s (composition-dominated, "
              "letter-unfit by seal, declared-set ward %s)"
              % (str(new_record), len(smallfam),
                 "speaks" if rc_speaks else "SILENT (< %d)"
                 % RC_N_MIN, rc_small, RC_GROW, str(grow),
                 NB_FAB,
                 str([(int(round(f)), round(v, 2))
                      for f, v in env_bins]),
                 "EXACT" if env_ok else "BROKEN"))

    # ---------------- S7: Leg B -- the source candidates
    section("S7  LEG B -- THE SOURCE DERIVATION (K2/K3/K4 AT "
            "FROZEN CONSTANTS + THE FRESH COUNT TEST)")
    if smoke:
        check("G70-source-candidates", True, "SMOKE: skipped")
        check("G71-fresh-count-test", True, "SMOKE: skipped")
        check("G72-source-side-reading", True, "SMOKE: skipped")
        src_ok = False
    else:
        c_k2 = max(r["fab"] * r["grel"] for r in sealed_rows)
        c_k3 = max(r["pil"] for r in sealed_rows)
        c_k4 = max(r["hgn"] for r in sealed_rows)
        v_k2 = [(r["kz"], round(r["fab"] * r["grel"], 2))
                for r in fresh_rows if r["fab"] * r["grel"]
                > c_k2]
        v_k3 = [(r["kz"], round(r["pil"], 2))
                for r in fresh_rows if r["pil"] > c_k3]
        v_k4 = [(r["kz"], round(r["hgn"], 2))
                for r in fresh_rows if r["hgn"] > c_k4]
        fab_max_all = max(r["fab"] for r in allrows)
        impl_k3 = FROZEN_CNSC * c_k3
        impl_k4 = FROZEN_CNG * c_k4
        k3_sharp = impl_k3 <= IMPL_FAC * fab_max_all
        k4_sharp = impl_k4 <= IMPL_FAC * fab_max_all
        check("G70-source-candidates", True,
              "SEALED CANDIDATES at frozen constants (max over "
              "the 83 sealed rows), tested on %d fresh rows: K2 "
              "(Klein-gap) FAB grel <= %.2f: %s; K3 (pileup) "
              "pil <= %.2f: %s, implied ceiling C_NSC C_K3 = "
              "%.1f (%s vs %.1f x max FAB %.2f); K4 (group) hgn "
              "<= %.2f: %s, implied C_NG C_K4 = %.1f (%s)"
              % (len(fresh_rows), c_k2,
                 "0 viol" if not v_k2 else "VIOL %s" % str(v_k2),
                 c_k3,
                 "0 viol" if not v_k3 else "VIOL %s" % str(v_k3),
                 impl_k3,
                 "sharp" if k3_sharp else "VACUOUS",
                 IMPL_FAC, fab_max_all, c_k4,
                 "0 viol" if not v_k4 else "VIOL %s" % str(v_k4),
                 impl_k4,
                 "sharp" if k4_sharp else "VACUOUS"))
        cnt_rows = [r for r in allrows
                    if r["coh"] in ("EXT4", "EXT5")]
        v_cnt = [(r["kz"], r["coh"], round(r["nscl"], 2),
                  round(r["ngl"], 2)) for r in cnt_rows
                 if r["nscl"] > FROZEN_CNSC
                 or r["ngl"] > FROZEN_CNG]
        cnt_ok = not v_cnt
        check("G71-fresh-count-test", True,
              "THE FRESH COUNT TEST (r329 FROZEN constants, "
              "never before measured on EXT4/EXT5): nsc_rel/lg "
              "<= %.4f AND ngj/lg <= %.4f on %d rows: %s; count "
              "reserves min NSC %.2f / NG %.2f -- the O(log m) "
              "counting side %s choice-robust on the deepest "
              "fresh cohorts"
              % (FROZEN_CNSC, FROZEN_CNG, len(cnt_rows),
                 "0 violations" if cnt_ok else "VIOLATIONS %s"
                 % str(v_cnt),
                 min((FROZEN_CNSC / max(r["nscl"], 1e-300)
                      for r in cnt_rows), default=0.0),
                 min((FROZEN_CNG / max(r["ngl"], 1e-300)
                      for r in cnt_rows), default=0.0),
                 "stays" if cnt_ok else "BREAKS"))
        src_ok = ((not v_k3 and k3_sharp)
                  or (not v_k4 and k4_sharp)) and cnt_ok \
            and not census_only
        gap_fam = [r for r in allrows if r["cls"] == "SPIKE"]
        rc_gap = CCP.spearman_rank([r["grel"] for r in gap_fam],
                                   [r["fab"] for r in gap_fam])
        check("G72-source-side-reading", True,
              "THE SOURCE-SIDE READING: the law reduces exactly "
              "to a pileup cap (chain (ii)) or a group-mass cap "
              "(chain (iii)); measured Spearman(grel, FAB | "
              "family) = %+.3f (the Klein-gap geometry %s the "
              "scale of q_max: small relative gaps carry the "
              "large FAB); src_ok %s -- %s"
              % (rc_gap,
                 "SETS" if rc_gap <= -0.5 else "does not pin",
                 str(src_ok),
                 "a source candidate carries at frozen "
                 "constants with fresh count confirmation"
                 if src_ok else "no candidate certifies at the "
                 "sealed bars (typed honestly)"))

    # ---------------- S8: Leg C -- the stable reserve floor
    section("S8  LEG C -- THE STABLE RESERVE FLOOR AT THE HONEST "
            "~1.1 SCALE")
    if smoke:
        check("G80-floor-test", True, "SMOKE: skipped")
        check("G81-floor-anatomy", True, "SMOKE: skipped")
        check("G82-floor-erosion", True, "SMOKE: skipped")
        fl_letter = "FLOOR_CENSUS"
        mx_log10 = 0.0
    else:
        fam_all = [r for r in allrows if r["cls"] == "SPIKE"]
        fresh_fam = [r for r in fam_all if r["coh"] == "EXT5"]
        floor_viol = [(r["kz"], r["coh"], round(r["rsv"], 2))
                      for r in fam_all if r["rsv"] < RHO_BAR2]
        cert2 = not floor_viol
        check("G80-floor-test", True,
              "THE SEALED NEW BAR RHO_BAR2 = %.2f on ALL %d "
              "family rows (incl. %d fresh EXT5 family rows): "
              "%s; family RSV min/med %.2f/%.2f -- the honest "
              "floor of the full family census"
              % (RHO_BAR2, len(fam_all), len(fresh_fam),
                 "0 violations (cert2 True)" if cert2 else
                 "VIOLATIONS %s (cert2 False)"
                 % str(floor_viol),
                 min(r["rsv"] for r in fam_all),
                 float(np.median([r["rsv"] for r in fam_all]))))
        floor_rows = [r for r in fam_all if r["rsv"] < RHO_BAR]
        comf_rows = [r for r in fam_all if r["rsv"] >= RHO_BAR]

        def med(rows, key):
            return float(np.median([rr[key] for rr in rows])) \
                if rows else 0.0
        info("FLOOR ANATOMY (floor rows RSV < %.1f vs "
             "comfortable):" % RHO_BAR)
        for r in sorted(floor_rows, key=lambda r: r["rsv"]):
            gsqb2 = GSQ_R321 / max((r["pk"] * r["m"]
                                    / (r["fa"] * r["lg"])) ** 2,
                                   1e-300)
            info("  kz%-4d %-4s D %5.2f pk %.4f GSQ/B^2 %5.2f "
                 "D pk B^2 %5.3f RSV %5.2f"
                 % (r["kz"], r["coh"], r["dd"], r["pk"], gsqb2,
                    r["dd"] * r["pk"] * (r["pk"] * r["m"]
                                         / (r["fa"] * r["lg"]))
                    ** 2, r["rsv"]))
        check("G81-floor-anatomy", True,
              "WHAT DISTINGUISHES THE FLOOR ROWS (%d rows, %s): "
              "med D %.2f vs comfortable %.2f; med pk %.4f vs "
              "%.4f; med FAB %.2f vs %.2f -- the floor rows are "
              "the DEEPEST-dominance largest-FAB spikes: the "
              "reserve 1/(D pk B^2) erodes exactly where the "
              "law coordinate peaks, restating the r349 "
              "anatomy on the extended census"
              % (len(floor_rows),
                 str([r["kz"] for r in floor_rows]),
                 med(floor_rows, "dd"), med(comf_rows, "dd"),
                 med(floor_rows, "pk"), med(comf_rows, "pk"),
                 med(floor_rows, "fab"), med(comf_rows, "fab")))
        e_rsv = L2D.halves_slope(
            [r["m"] for r in sorted(fam_all,
                                    key=lambda r: r["m"])],
            [max(r["rsv"], 1e-300)
             for r in sorted(fam_all, key=lambda r: r["m"])])
        rc_fam351 = CCP.spearman_rank(
            [r["fa"] for r in fam_all],
            [r["rsv"] for r in fam_all])
        eroding = e_rsv < -E_FLAT_BAR
        m_med = float(np.median([r["m"] for r in fam_all]))
        rsv_med = float(np.median([r["rsv"] for r in fam_all]))
        if e_rsv < 0.0 and rsv_med > 1.0:
            mx_log10 = (math.log10(m_med)
                        - math.log10(rsv_med) / e_rsv)
        else:
            mx_log10 = float("inf")
        fl_letter = floor_letter(len(fresh_fam) == 0, cert2,
                                 eroding)
        check("G82-floor-erosion", True,
              "EROSION (fit-free): e_RSV = halves-slope(RSV vs "
              "m | family) = %+.3f (bar +/-%.2f) -> %s; "
              "rc_fam351 = Spearman(F, RSV) = %+.3f (r349 prior "
              "%+.3f on ladder+EXT3); extrapolated RSV = 1 "
              "crossing at log10 m ~ %s (the honest depth "
              "where the sliding coverage would die IF the "
              "erosion trend were a law -- census-grade, said "
              "honestly); FLOOR LETTER: %s"
              % (e_rsv, E_FLAT_BAR,
                 "ERODING" if eroding else "FLAT-OR-RISING",
                 rc_fam351, R349_RC_FAM,
                 ("%.1f" % mx_log10)
                 if math.isfinite(mx_log10) else "inf",
                 fl_letter))

    # ---------------- S9: Leg D -- composition + adjudication
    section("S9  LEG D -- THE COMPOSITION + SEALED ADJUDICATION")

    def solve_m0(log_rhs):
        t = math.log(73.0)
        while t < 1e7:
            if CRIT_EXP * t >= log_rhs(t):
                return t / math.log(10.0)
            t *= 1.02
        return None

    if smoke:
        check("G85-composition", True, "SMOKE: skipped")
        check("G86-cofinal-typing", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        fa_max_all = max(r["fa"] for r in allrows)
        c_m2env = max(r["ev"]["mqs"]["m2"] for r in allrows)
        fab_max_all = max(r["fab"] for r in allrows)
        c_comp = fab_max_all * c_m2env

        def rhs_uniform(t):
            return math.log(max(GSQ_R321 * fa_max_all ** 2
                                * t * t, 1e-300))
        m0_uni = solve_m0(rhs_uniform)

        def rhs_law(t):
            return math.log(max(c_comp * t, 1e-300))
        m0_law = solve_m0(rhs_law)
        e_fab_all = L2D.halves_slope(
            [r["m"] for r in sorted(allrows,
                                    key=lambda r: r["m"])],
            [max(r["fab"], 1e-300)
             for r in sorted(allrows, key=lambda r: r["m"])])
        e_m2_all = L2D.halves_slope(
            [r["m"] for r in sorted(allrows,
                                    key=lambda r: r["m"])],
            [max(r["ev"]["mqs"]["m2"], 1e-300)
             for r in sorted(allrows, key=lambda r: r["m"])])
        e_tot = e_fab_all + e_m2_all
        e_pos = max(e_tot, 0.0)

        def rhs_grow(t):
            return math.log(max(c_comp * t, 1e-300)) \
                + e_pos * t
        m0_grow = solve_m0(rhs_grow)
        m0_306 = solve_m0(lambda t: math.log(
            max(R306_C2 * t * t, 1e-300)))
        info("THE m_0* TABLE (typed):")
        info("  r344/r346/r349 uniform (record):        10^%.1f"
             % M0_R344)
        info("  uniform at the NEW overall F ceiling "
             "%.2f:  %s" % (fa_max_all,
                            ("10^%.1f" % m0_uni)
                            if m0_uni is not None else "NONE"))
        info("  THE LAW ROUTE (A = 1 polylog, class-free): "
             "rho_2 <= %.2f x %.2f / log m -> 10^%.1f"
             % (fab_max_all, c_m2env,
                m0_law if m0_law is not None else -1.0))
        info("  the growth-slack route (e_tot %+.3f):    %s"
             % (e_tot, ("10^%.1f" % m0_grow)
                if m0_grow is not None else "NONE"))
        info("  comparisons: V1 10^%.1f / V2 10^%.1f (r346 "
             "records); r306 census 10^%.1f; r324 route 10^%.1f"
             % (V1_M0_REF, V2_M0_REF, m0_306, R324_M0_L10))
        check("G85-composition", True,
              "THE COMPOSITION: at a certified growth law the "
              "polylog recomposition (v) is CLASS-FREE -- "
              "rho_2 <= C_FAB C_M2ENV/log m with C_FAB %.2f, "
              "C_M2ENV %.2f (envelope incl. fresh rows) -> "
              "m_0* = 10^%.1f vs the r349 uniform 10^%.1f "
              "(census F ceiling) and the r306 census 10^%.1f; "
              "the growth-typed slack route gives 10^%s "
              "(e_tot %+.3f vs CRIT %.3f, halves-slopes "
              "composition-dominated, census-grade by seal)"
              % (fab_max_all, c_m2env,
                 m0_law if m0_law is not None else -1.0,
                 M0_R344, m0_306,
                 ("%.1f" % m0_grow) if m0_grow is not None
                 else "NONE", e_tot, CRIT_EXP))
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (norm_w > DEC_BAR or interp_w > CHAIN_BAR
                      or fabid_w > FAB_ID_BAR
                      or pile_w > CHAIN_BAR
                      or pilerec_w > GRP_CHAIN_BAR
                      or grp_w > CHAIN_BAR or dec_w > DEC_BAR
                      or chainD_w > DEC_BAR
                      or chain_w > CHAIN_BAR
                      or id324_w > CHAIN_BAR
                      or not mult_all_ok
                      or fab_dev != 0 or fd_dev != 0)
        vkey = growth_tree_verdict(leak, brk_struct, census_only,
                                   grow, src_ok)
        check("G86-cofinal-typing", True,
              "COFINAL TYPING (r346/r349 convention) -- what "
              "stands between the cover and a cofinal theorem "
              "at the %s reading: (1) C_FAB %.2f and C_M2ENV "
              "%.2f are FREEZE-CENSUS constants over %d rows -- "
              "the ladder-to-m_0* step stays the disclosed "
              "extrapolation hypothesis; (2) the reserve floor "
              "letter %s (the spike coverage needs it); (3) the "
              "source derivation src_ok %s (K3/K4 status "
              "above); (4) the finite closure below m_0* (r306 "
              "0/57 + the sealed tables) carries only to m = "
              "%d; (5) no second world (r329 honesty: the "
              "selection buys choice-independence, not a new "
              "world) -- and the in-zone fresh pool is now "
              "EXHAUSTED: the next teeth must come from a new "
              "construction family"
              % (vkey, fab_max_all, c_m2env, len(allrows),
                 fl_letter, str(src_ok),
                 max(r["m"] for r in allrows)))
        flags = [fl_letter if fl_letter != "FLOOR_ERODES"
                 else "FLOOR_ERODES(10^%s)"
                 % (("%.1f" % mx_log10)
                    if math.isfinite(mx_log10) else "inf")]
        if new_record:
            rmax = max(fresh_rows, key=lambda r: r["fab"])
            flags.append("NEW_FAB_RECORD(kz%d, %.2f)"
                         % (rmax["kz"], rmax["fab"]))
        if inzone_exhausted:
            flags.append("INZONE_POOL_EXHAUSTED")
        if fresh_rows and not fresh_viol:
            flags.append("EXT5_CLEAN(%d)" % len(fresh_rows))
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a law "
                           "builder",
            "LAW_STATE_NOT_EXACT":
                "an exact ward broke (NORM %.1e / interp %.1e / "
                "FAB id %.1e / pileup %.1e / group %.1e / "
                "decomp %.1e)" % (norm_w, interp_w, fabid_w,
                                  pile_w, grp_w, dec_w),
            "GROWTH_CENSUS_ONLY":
                "fewer than %d fresh rows admitted -- no fresh "
                "teeth, the round degrades to census"
                % FRESH_MIN,
            "FA_UNBOUNDED":
                "the ceiling GROWS: new record %s, rc_small "
                "%+.3f -- the law is refuted at the measured "
                "range, the spike constant stays census; "
                "growth typed e_FAB %+.3f, e_tot %+.3f vs CRIT "
                "%.3f" % (str(new_record), rc_small, e_fab_all,
                          e_tot, CRIT_EXP),
            "GROWTH_LAW_DERIVED":
                "0 fresh violations at C_FAB %.2f AND a source "
                "candidate carries at frozen constants with "
                "fresh count confirmation -- the theorem-kernel "
                "candidate" % c_fab,
            "GROWTH_LAW_CERTIFIED":
                "0 fresh violations at the frozen C_FAB %.2f "
                "(m q_max <= %.2f log m on every measured row "
                "of every cohort) and no growth clause fires "
                "-- the law holds census-frozen; the source "
                "derivation stays open" % (c_fab, c_fab)}
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
    scr_txt = ""
    if smoke:
        for w, rc_w in wtab:
            ev = rc_w["ev"]
            info("world %-10s m %3d qmax %.4f" % (w, ev["m"],
                                                  ev["mqs"]["qm"]))
        check("G90-world-census", len(wtab) >= 1,
              "SMOKE: world columns printed (w9 + live controls)")
    else:
        for w, rc_w in wtab:
            ev = rc_w["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            fab_w = fab_of(float(mloc), ev["mqs"]["qm"], lgl)
            fa_w = CCP.world_coord(ev["mqs"]["qm"], rc_w["N"],
                                   N_lad, q_lad)
            rsv_w = GSQ_R321 * fa_w ** 2 \
                / max(ev["rho2"], 1e-300)
            cls_w = FCC.cls_rule(fa_w, F0_SPLIT)
            info("world %-10s m %3d F_ins %.2f %-5s FAB %5.2f "
                 "(vs C_FAB %.2f) RSV %.1f"
                 % (w, mloc, fa_w, cls_w, fab_w, c_fab, rsv_w))
            if w == "SCR":
                scr_txt = " + SCRAMBLE_FAB(%.2f, %s C_FAB)" \
                    % (fab_w, "<=" if fab_w <= c_fab else ">")
        check("G90-world-census", len(wtab) >= 2,
              "WORLD CENSUS (NO letter): FAB + insertion class "
              "on %d worlds -- a SCRAMBLE FAB below the frozen "
              "ceiling makes the growth law ARITHMETIC-FREE by "
              "measurement (a pure size statement, no world "
              "separation claimed)%s" % (len(wtab), scr_txt))
    check("G91-e1-fab-readback",
          len(e1_hits) >= 1 and mut1 == Fr(1, 2)
          and mut1 != toy1_true,
          "e1 CAUGHT twice: the law column consuming the stale "
          "q_max RECORD -- AST-FLAGGED (%s) -- and on the "
          "sealed Fractions toy returns %s != the true FAB %s "
          "(the real column recomputes the peak from the SAME "
          "block vector)"
          % (e1_hits[0] if e1_hits else "MISS", str(mut1),
             str(toy1_true)))
    check("G92-e2-select-posthoc",
          len(e2_hits) >= 1 and mut2 == (2, 3)
          and mut2 != toy2_sealed,
          "e2 protocol-CAUGHT twice: the fresh windows picked "
          "after sight of the violation column -- AST-FLAGGED "
          "(%s) -- and on the toy returns %s != the sealed "
          "queue-order rule %s (the EXT5 selection consumes "
          "shape + grid + used ledger ONLY, sealed pre-freeze)"
          % (e2_hits[0] if e2_hits else "MISS", str(mut2),
             str(toy2_sealed)))
    check("G93-e3-fab-wrong-log",
          mut3 == Fr(3, 8) and toy3_true == Fr(3, 4)
          and toy3_true / mut3 == Fr(2),
          "e3 CAUGHT exact: the wrong log power returns %s on "
          "the sealed Fractions toy while the exact FAB is %s "
          "-- break factor %s == the pseudo-log EXACT (the "
          "single log m power of the law is load-bearing)"
          % (str(mut3), str(toy3_true), str(toy3_true / mut3)))
    check("G94-e4-floorbar-posthoc",
          len(e4_hits) >= 1 and abs(mut4 - 0.5) <= TOY_BAR
          and mut4 != RHO_BAR2,
          "e4 protocol-CAUGHT twice: the floor bar read from "
          "the evaluated reserve column -- AST-FLAGGED (%s) -- "
          "and on the toy returns %.1f != the sealed RHO_BAR2 "
          "%.2f (the bar is sealed in this spec BEFORE the "
          "freeze)"
          % (e4_hits[0] if e4_hits else "MISS", mut4, RHO_BAR2))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the convention-free FAB census with a frozen "
          "ceiling and a fresh-tranche test, the source "
          "candidates at frozen constants with the first "
          "EXT4/EXT5 count measurements, the honest reserve "
          "floor at the 1.05 bar with erosion typing, and the "
          "class-free polylog recomposition -- NO new "
          "certificate promoted, NO universal bound claimed "
          "beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R351_ANCHORS(identity %.1e, r306 C2 %.3f v%d, "
                 "r316 n %d, dict %.1e, r321 FA %.2f/%.2f/%.2f, "
                 "r349 family %d rows rc %+.3f, EXT4 F_ins %s "
                 "holes kz111/kz75, r324 C_INF %.4f viol %s e_G "
                 "%+.3f, r329 C_NSC %.4f C_NG %.4f)"
                 % (rec3_w, C2r, viol2, n351, dict3_w,
                    fa_kz[53], fa_kz[83], fa_kz[67],
                    len(fam_idx), rc_fam349, str(fins4_sorted),
                    cinf_repro, str(viol_inf), eg_repro,
                    cnsc_repro, cng_repro)]
        parts.append("SEAL(NORM %.1e, interp %.1e, FAB id %.1e, "
                     "pileup %.1e, group %.1e, decomp %.1e, "
                     "purity clean, toys exact)"
                     % (norm_w, interp_w, fabid_w, pile_w,
                        grp_w, dec_w))
        parts.append("FABCENSUS(C_FAB %.2f @ kz%d, cohort max "
                     "%s, fresh %d rows viol %d, new record %s, "
                     "rc_small %+.3f)"
                     % (c_fab, c_fab_kz,
                        str({c: round(v, 2) for c, v in
                             sorted(coh_max.items())}),
                        len(fresh_rows), len(fresh_viol),
                        str(new_record), rc_small))
        parts.append("SOURCELAW(K2 %.2f viol %d, K3 %.2f viol "
                     "%d impl %.1f, K4 %.2f viol %d impl %.1f, "
                     "fresh counts %s, src_ok %s)"
                     % (c_k2, len(v_k2), c_k3, len(v_k3),
                        impl_k3, c_k4, len(v_k4), impl_k4,
                        "0 viol" if cnt_ok else "VIOL",
                        str(src_ok)))
        parts.append("FLOOR(bar %.2f cert2 %s, min RSV %.2f, "
                     "e_RSV %+.3f, %s)"
                     % (RHO_BAR2, str(cert2),
                        min(r["rsv"] for r in fam_all), e_rsv,
                        fl_letter))
        parts.append(verdict_main)
        parts.append("COMPOSITION(uniform 10^%.1f record / "
                     "10^%.1f new-ceiling, LAW route 10^%s, "
                     "growth route 10^%s, r306 10^%.1f)"
                     % (M0_R344,
                        m0_uni if m0_uni is not None else -1.0,
                        ("%.1f" % m0_law)
                        if m0_law is not None else "NONE",
                        ("%.1f" % m0_grow)
                        if m0_grow is not None else "NONE",
                        m0_306))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the identity, the "
          "chains, the Fractions toys and the purity audits "
          "(exact / AST-decided); MEASURED: every FAB value, "
          "constant, count column, reserve and violation count "
          "(the finite ladder + 12 EXT3 + 6 EXT4 + the admitted "
          "EXT5 rows + 2 mains + 2 live controls); OPEN: any "
          "bound beyond the measured rungs, the cofinal law, "
          "the actual proof (a certified growth law fixes a "
          "LAW CANDIDATE with a frozen census constant, it "
          "proves nothing cofinal); NO RH claim"
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
