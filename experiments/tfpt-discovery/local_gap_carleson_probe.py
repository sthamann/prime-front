#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""local_gap_carleson_probe --
PRIME.L2.K2.LOCAL_GAP_CARLESON.01 (round 358): THE WEIGHTED
SMALL-GAP CARLESON PACKING -- reviewer contract T1, theorem-first.

CONTEXT (binding, from the DCCX theorem-first adjudication after
r334..r357 and the sealed records r351/r353/r355/r357).  The K2
error so far: FAB grel <= C_K was composed with the GLOBAL minimum
gap g_min -- one single small gap sets the bound for the entire
mass, hence supercritical (r355: e_impl +0.286 > CRIT_EXP 0.224;
the growing-law m_0* is NONE).  For a third moment one does not
need a global minimal-gap bound but the WEIGHTED DISTRIBUTION of
the small gaps.  The reviewer contract (verbatim, binding):
  T1 (localization): (m q_i / log m) g_i <= C_K for EVERY
     canonical fold group/atom i (not only the maximum), with
     q_i = a_i / sum_j a_j the relative block mass and g_i the
     normalized LOCAL small gap of atom i;
  T2 (the new arithmetic): sum_i q_i / g_i^2 <= C_G (log m)^A;
  T2' (equivalent dyadic packing): sum_{i: g_i <= 2^-r} q_i <=
     C 2^{-2r} (1+r)^A -- the normalized mass on gaps of size
     2^-r must fall QUADRATICALLY ("very tight coincidences may
     exist, but not with mass"); dyadic summation gives T2 up to
     a log factor (warded EXACT one-sided, live);
  COMPOSITION: q_i^2 <= C_K^2 (log m)^2 / (m^2 g_i^2)  ==>
     M_3 = sum q_i^3 <= C_K^2 C_G (log m)^{A+2} / m^2  ==>
     N_3 >= m / (C (log m)^{(A+2)/2})  ==>  N_2 >= N_3 (power
     mean, exact)  ==>  Fejer/vdC  ==>  H5  ==>  q_N < 1 --
     WITHOUT premature powerization; the existing exact finite
     certificates close the head.
HARD GATES (reviewer verbatim): no global minimal-gap bound
anywhere in the composition; no frame-A constant (per-family
first-K freezes only, the r306 convention); no target evaluation
(AST); the SAME statement must hold on frame A, frame B, chi mod 3
and chi mod 4 (the r357 worlds -- the machinery exists); the
matched SCRAMBLE must break at a NAMED source precondition; direct
composition to q_N < 1.

THE SEALED g_i COORDINATE (source-pure, frozen BEFORE any
evaluation; from the mesh identity, not fitted).  Every admitted
window carries the canonical level-2 block presentation (r287/
r298) with the r314 fold genealogy (fold multiplicity <= 2 warded
live).  All fold-group positions lie EXACTLY on the theta grid of
LL = 4 N_w - 2 points (theta_k = 2 pi k / LL; x = cos theta) --
the grid step is set by the mesh D = 0.5 gap/NU through the EXACT
mesh identity h - NU u in (0, 3/2] (r355 mesh_h, imported verbatim
and re-warded): the zone's Klein gap parametrizes the finest
possible local separation, fit-free.  Definition (per window):
  (i)   block center c_i = the unweighted mean of the DISTINCT
        fold-group theta-grid positions of block i (positions +
        block ids only -- NO values consumed);
  (ii)  local gap gap_i = min distance to the adjacent block
        centers (one-sided at the two edge blocks), in grid units;
  (iii) g_i = gap_i / median{gap_k : |k - i| <= W_LOC, k != i}
        -- EFA.grel_col applied VERBATIM (w = GAP_W = 5, the r317/
        r329 W-window convention) to the block-gap column: the
        SAME normalization that defines the zone grel, one level
        down.  g_i > 0 always (centers strictly separated).
  q_i = |x_i| / sum_j |x_j| (the r339 FDD leaf convention,
        y_i = m q_i; dictionary ward ymx/m == q_max live).
  DISCLOSED: g_i is the BLOCK-local gap, NOT the zone grel; the
  zone grel enters this round as anchor columns only.  At the
  argmax block T1 reads FAB g_{i*} <= C_K -- the localization of
  K2 with the local coordinate replacing the zone coordinate.

THE FOUR WORLD FAMILIES (Leg 0 anchors bit-near, same code path):
  FRAME A: the sealed 89-row r351 surface (42-rung ladder h <=
    900 + 15 extension + <= 8 EXT2 + EXT3 12 + EXT4 6 + EXT5 6,
    all adopted as-is, BH.wpack) -- anchor: C_K2X = max FAB grel
    = 11.87 at kz111 (r353/r355 record, tol 0.02).
  FRAME B: the 8 sealed r353 anchors (69, 80, 133, 129, 124, 117,
    107, 101) ADOPTED AS-IS (the EXT5 adoption convention),
    SFE.wpack_b at NU_B = 2, admission re-verified -- anchor: the
    8-row FAB/grel table (tol 0.02/0.003) + K2 max 5.95.
  CHI3 / CHI4: the 42 matched Dirichlet terminal rows per
    character (r357 DMF.chi_window_comb + DMF.chi_wpack at a = 1,
    conductor log(pi/q), verbatim) -- anchors: max FABg 4.73 at
    kz32 (chi3) / 5.16 (chi4), MAIN-42 max 6.95 (r357 record,
    tol 0.02).  The r357 K2/counting channel DMF.k2_rows is
    reused VERBATIM for the FAB columns and the exact FAB-
    identity + one-sided K2-chain wards on ALL four families.

THE LEGS:
  LEG A -- T1: per family the rows are sorted by (N, kz); C_K(F)
    is frozen by the r306 first-K rule (max row-max product over
    the first N_CAL_T1 = 5 rows; frame B: N_CAL_FB = 2 of its 8)
    -- NO frame-A constant is applied to any other family; T1 is
    then tested POINTWISE on every remaining row of that family
    (violation iff any atom's (m q_i/log m) g_i > C_K(F) +
    K2_EPS).  0 violations on all four families = the T1 census.
  LEG B -- T2'/T2 (the core): per row and r = 1..R_MAX = 12 the
    dyadic gap-mass S_r = sum_{g_i <= 2^-r} q_i against the
    SEALED bar C_PACK 2^{-2r} (1+r)^{A_PACK} (C_PACK = 1.0,
    A_PACK = 2.0, a-priori); the FULL r-table per family is
    printed (max_w S_r vs bar); 0 violations over all rows of
    all four families = the quadratic law as census theorem.
    T2 census: max_w sum q_i/g_i^2 and C_G_cens = max_w T2val /
    (log m)^{A_PACK} per family; the dyadic-summation bound
    T2val <= sum_shells 4^{r+1} M_r + M_{g>1} is warded EXACT
    one-sided on every live row (the T2' => T2 satz link).
    SMALL-BALL (building block D): per row the blocks are banded
    dyadically by atom mass A1_i (band s = floor(log2 Amax/A1_i)
    <= S_BAND_MAX = 20; bands with >= BAND_MIN = 5 members);
    within each band SB_r = sum_{i in B, g_i <= 2^-r} A1_i /
    sum_{i in B} A1_i against C_SB 2^{-2r} (1+r)^{B_SB} (C_SB =
    1.0, B_SB = 2.0, a-priori) -- census where the quadratic
    small-ball form carries and where it breaks; the small-gap
    spikes kz51/kz111 (frame A) are printed as the stress test
    with their full band tables.  Band comparability (building
    block C): per band the median alignment |x_i|/A1_i (census
    bar ALIGN_FLOOR = 0.5).
  LEG C -- the proof-sketch typing on the four structures:
    (A) fold multiplicity exactly <= 2: EXACT (warded live);
    (B) the mesh identity h - NU u in (0, 3/2] + the theta-grid
        quantization of every fold-group position (QUANT_BAR
        1e-6 grid units): EXACT (warded live) -- the coincidence
        is parametrized fit-free;
    (C) dyadic source bands + alignment comparability:
        DICTIONARY-grade (census-warded);
    (D) the large-sieve/small-ball IN THE MEAN: the OPEN core --
        typed honestly; NO Baker point bounds (r289/r331).
  LEG D -- the composition: per live row the chain M_3 <=
    PK_row^2 (log m)^2/m^2 x T2val is warded EXACT one-sided
    (pure algebra) and N_2 >= N_3 is warded EXACT; at 0
    violations the new m_0* is solved as a PURE POLYLOG:
    CRIT_EXP t >= 2 log C_K^max + log C_G_cens + A_PACK log t
    (solve_m0 body, r351 convention) and printed against the
    r351 10^18.9, the r353 10^20.5 and the r306 census 10^13.5;
    the cofinal typing names the precise sieve question for
    specialists.  NO global g_min appears anywhere.
  LEG E -- worlds + must-fails: matched SCRAMBLEs through all
    three construction channels (frame-A w9 seed 1 via BH.wpack;
    frame-B kz80 seed 1 via SFE.wpack_b, the r353 record; matched
    chi3 w9 seed 1 via DMF machinery, the r357 record) -- each
    adjudicated by the SEALED PRECONDITION ORDER (P1
    POSITIVE_PREFIX admission > P2 fold multiplicity <= 2 > P3
    theta-grid quantization > P4 band alignment comparability >
    P5 the packing itself); the letter names the FIRST failing
    source precondition (expected P1 = admission, the r353/r355/
    r357 records; the P2-P4 censuses are printed regardless).
    The rational twin of the chi3 comb (AKD.twin_rational at
    1e-8, r357 verbatim) must carry the gap columns bit-near
    (T1 row-max + T2val devs <= TWIN_BAR = 1e-3).

LEG E MUST-FAILS (>= 5 mutants + 2 scope mutants):
(e1) g_i READ BACK FROM q_i (protocol): mutant_g_from_q returns
  the inverse-mass column (consumes rho) -- AST-FLAGGED and on
  the sealed toy returns (2.0, 4.0) != the sealed positional
  column (2.0, 0.5) -- protocol-CAUGHT twice.
(e2) GLOBAL g_min AS SUBSTITUTE (the r355 error as a mutant):
  mutant_global_gmin replaces the per-atom column by min(g)
  replicated -- on the sealed toy (g (1.0, 0.25, 0.5), q uniform)
  it returns (0.25, 0.25, 0.25) != the per-atom column AND its
  packing mass S_2 = 1.0 breaks the sealed bar 0.5625 where the
  true column passes at 1/3 -- CAUGHT exact (the one-gap-kills-
  all-mass supercriticality reproduced as a mutant).
(e3) FRAME-A CONSTANT HIDDEN (protocol): mutant_ck_framea applies
  the withheld frame-A record literal to every family (consumes
  rho AND the withheld identifier CK_FRAMEA_LIT) -- AST-FLAGGED
  and on the sealed toy returns 11.87 != the sealed per-family
  toy freeze 1.0 -- protocol-CAUGHT twice.
(e4) DYADIC BARS AFTER SIGHT (protocol): mutant_bars_posthoc sets
  C_PACK at the seen mass column (consumes rho) -- AST-FLAGGED
  and on the sealed toy (S = 0.9 at r = 4, A = 2) returns 9.216
  != the sealed C_PACK 1.0 -- protocol-CAUGHT twice.
(e5) MESH IDENTITY WITH THE WRONG INTERVAL: mutant_mesh_interval
  claims h - NU u in (0, 0.5] -- on the sealed by-hand toy
  (alpha 10, gap 1, nu 2 -> h 21, dev 1.0) it REJECTS the valid
  mesh while the true interval (0, 1.5] accepts -- CAUGHT exact.
(m6a/m6b) WORLD-BLINDNESS BREAK (r355 verbatim): builders
  consuming the withheld terminal drive key / the branch label
  are both FLAGGED by the AST scope audit.

SEALED VERDICTS (main letter: exactly one fires, total order;
flags appended with '+', combinations allowed; the contract enum
GAP_CARLESON_CERTIFIED / QUADRATIC_LAW_PARTIAL / SIEVE_CORE_OPEN /
PACKING_FAILS / TARGET_LEAK is extended by the house exactness
guard LAW_STATE_NOT_EXACT, disclosed):
  TARGET_LEAK  iff any firewall/scope/fragment/literal audit hit
    on the module-own builders;
  LAW_STATE_NOT_EXACT(named)  iff an exact ward breaks on a live
    world (quantization, multiplicity filter empty, FAB identity,
    K2 chain, FDD dictionary, N2 >= N3, T2 dyadic summation, M3
    composition, mesh identity, frame reproductions, toys);
  PACKING_FAILS(families)  iff T2' has >= 1 violation at the
    sealed (C_PACK, A_PACK) bars in any family -- the quadratic
    law breaks: honestly the most important negative;
  QUADRATIC_LAW_PARTIAL(loci)  iff T2' holds 0-violation on all
    four families but T1 has violations somewhere (the loci);
  GAP_CARLESON_CERTIFIED  iff T1 AND T2' hold with 0 violations
    on all four families (census certificate; the composition is
    then printed as pure polylog).
  APPENDED ALWAYS at CERTIFIED/PARTIAL: SIEVE_CORE_OPEN (the
    in-the-mean small-ball sieve (D) is the named theorem rest --
    no census can settle it) + T1(per-family C_K spread) +
    PACK(r-table summary) + SMALLBALL(band census) +
    COMPOSITION(m_0* vs 18.9/20.5/13.5) + SCRAMBLE(named
    precondition per channel) + TWIN(devs) + MUSTFAIL_LEDGER.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r355
KSF.mesh_h + KSF.R353_FB_TABLE + KSF.FRAMEB_KZ + KSF constants
(1f14bd93); r357 DMF.{chi_window_comb, chi_wpack, eval_k2,
k2_rows, LPQ3, LPQ4} (4bf1a94b); r353 SFE.{wpack_b, frameb_pool}
(bd89e331); r351 QGL.fab_of + bars (67102e4c); r330
DSW.{rung_rec, EDGE_F, DEG_FLOOR} (66526018); r329
EFA.{grel_col, GAP_W} (bbfaf199); r314 SCF.fold_genealogy; r324
QMO.pileup_state + FAP.m2_qmax_state; r327
GMC.{group_mass_ledger, heavy_state}; r339
FDD.martingale_moment_dictionary; r306 RY3; r269 PBB; r298 WBT;
r244 BH; r243 PB; r289 AKD.twin_rational; r276 MF.local_gaps;
v881 PIK; v563 core READ-ONLY; FTS/TSL constants.  NEW module-own
(source-pure, AST-audited): theta_col, gap_ledger, g_norm (the
EFA.grel_col wrapper), pack_bar, sb_bar, t1_tree, main_tree_358,
scr_letter.  q columns, FAB, products, S_r, T2val, bands and
every census on them are TARGET-SIDE DIAGNOSTICS computed in the
gate section (r321/r349/r351/r353/r355 convention, disclosed) --
the module-own builders consume atom positions, block ids, window
depth and SEALED thresholds only.

INDEX FIREWALL (binding, r238-r357 discipline): w = window (kz),
N_w = builder depth, m = block count; ground truth (records, the
frozen r353/r357 anchor literals) enters GATES and census tables
only, never a builder (AST scope audit; withheld identifiers
rho / t_term / g_branch / CK_FRAMEA_LIT); no zero/prime oracles
anywhere (AST firewall; the prime-power anchor grid U_ALL/G_ALL
is the sealed source comb, r238 convention); no fit primitives
(fragment audit; NO slopes are fitted this round -- the bars are
a-priori, the medians are medians).  Budget <= 1800 s.

SEALED CONSTANTS (everything not listed is imported verbatim):
W_LOC = EFA.GAP_W = 5; N_CAL_T1 = 5; N_CAL_FB = 2; K2_EPS 1e-9;
PACK_EPS 1e-12; C_PACK 1.0; A_PACK 2.0; R_MAX 12; C_SB 1.0;
B_SB 2.0; BAND_MIN 5; S_BAND_MAX 20; ALIGN_FLOOR 0.5; QUANT_BAR
1e-6 (grid units); MESH_DEV_HI = KSF 1.5; CHI_TB_BAR 1e-3
(a-priori); TWIN_BAR 1e-3; TWIN_TOL 1e-8; SCR_SEED 1
(r-convention); MULT_CAP = FTS 2; STRESS_KZ (51, 111); anchor
records (gate-side literals): R353_CK2X 11.87 tol 0.02 at kz111;
R353_FB_TABLE (KSF verbatim) FAB tol 0.02 / grel tol 0.003;
R353_FB_K2MAX 5.95 tol 0.02; R357_CHI3_MAX 4.73 at kz32 tol
0.02; R357_CHI4_MAX 5.16 tol 0.02; R357_MAIN_MAX 6.95 tol 0.02;
M0 references printed: 18.9 / 20.5 / 13.5; import-integrity
prefixes KSF 1f14bd93 / DMF 4bf1a94b / SFE bd89e331 / QGL
67102e4c / EFA bbfaf199 / DSW 66526018; R358_TABLE_LITERALS =
KSF.R355_TABLE_LITERALS UNION {4.73, 5.16, 6.95} (collision-prone
small values curated out, r337..r355 convention); runtime <=
1800 s; smoke = toys + trees + mutants + scope/purity audits +
the four w9 worlds (frame A / frame B / chi3 / chi4) with full
eval, gap columns, quantization + multiplicity + dictionary +
N2N3 + T2-summation + M3-composition wards, the NU = 4 and chi
trivial frame reproductions, and the eval cross-ward against
DMF.eval_k2; ladders, T1/T2 adjudication, bands, composition,
scrambles, twin and verdict skipped.

DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe's sealed
adjudication): every anchor band is an r306..r357 RECORD number
adopted as-is; ONE SCOPING PASS (machinery validation at w9 only,
r353/r355/r357 precedent, numbers disclosed): theta-grid
quantization dev 5.7e-14 at LL = 4 N_w - 2 (the ward is real);
fold multiplicity max 2; block centers strictly monotone in
theta; w9 frame A m = 35, gaps 3.5..6.0 grid units, g in [0.875,
1.5], T1 row-max 1.24, T2val 0.978, S_r = 0 for all r >= 1 (the
shallow anchor world has NO small-gap mass -- every deep column,
every T1/T2'/band adjudication and every composed number is
GENUINELY OPEN); frame-B w9 N 92 nf None; chi3 w9 N 184 nf None;
timing: the w9 pass 0.5 s, one frame-B deep build 47 s (r353
record timing adopted).  The sealed toys are computed BY HAND:
gap toy centers (2, 4, 5, 9, 12) -> gaps (2, 1, 1, 3, 3) -> g at
w = 2: (2.0, 0.5, 0.4, 3.0, 1.5); pack toy A q (0.5, 0.3, 0.2) /
g (1.0, 0.4, 0.2) -> S_1 0.5 / S_2 0.2 / S_3 0, 0 violations;
pack toy B q (0.1, 0.9) / g (1.0, 0.05) -> S_2 = S_3 = S_4 =
0.9 -> 3 violations (r 2, 3, 4) CAUGHT; T2-summation Fractions
toy q (1/2, 1/4, 1/4) / g (1, 1/2, 1/2): T2val 5/2 <= shell
bound 10 EXACT; M3 composition Fractions toy (same, m 4, lg 2,
PK 1): M3 = 5/32 <= 5/8 EXACT; N2N3 toy: N2^2 = 64/9 >= N3^2 =
32/5 (320 >= 288) EXACT; mesh toy alpha 10 / gap 1 / nu 2 -> h
21, dev 1.0 in (0, 1.5]; e1 pin (2.0, 4.0) vs (2.0, 0.5); e2 pin
(0.25, 0.25, 0.25) + mutant S_2 1.0 > 0.5625 vs true 1/3; e3 pin
11.87 vs 1.0; e4 pin 9.216 vs 1.0; e5 pin False vs True; the
five main branches, the T1 tree and the scramble letters EXACT.
N_CAL_T1, N_CAL_FB, C_PACK, A_PACK, R_MAX, C_SB, B_SB, BAND_MIN,
S_BAND_MAX, ALIGN_FLOOR, QUANT_BAR, CHI_TB_BAR and TWIN_BAR are
coarse a-priori choices fixed BEFORE any evaluation; the letters
are symmetric and total by CONTRACT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: R359 (L* dual Wronskian) and a Lean block (C1) run
in parallel -- own files only; git pull before the strictly
additive rh-sync.  Two-commit freeze protocol (r329 convention):
spec committed pre-freeze, record tables the only post-freeze
edit, committed again.

Honesty before beauty: the quantization, the multiplicity, the
mesh identity, the dictionary, N2 >= N3, the dyadic summation,
the M3 composition algebra, the Fractions toys, the frame
reproductions and the purity audits are EXACT (Fractions/AST-
decided); every C_K, S_r, T2val, band mass and violation count
is MEASURED on the finite 89 + 8 + 42 + 42 row surface only; a
certified packing fixes a CENSUS THEOREM with frozen a-priori
bars -- it proves NO cofinal law; the in-the-mean sieve (D)
stays OPEN mathematics by contract; g_i is a construction-local
coordinate, said out loud; r243..r357 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA 8831b1410849f1b4,
pre-freeze commit 9141d3e7; protocol: smoke pass 1 = 20/20
(0.6 s, run twice pre-commit, byte-identical up to the WALL
line, disclosed in the commit message); calibration pass 1 =
FIRST full evaluation = 20/20, wall 711.3 s, NO amendment -- no
bar, band, rule or verdict rule moved at any point; record
run1/run2 after this insertion, byte-identical up to WALL):
MAIN VERDICT: QUADRATIC_LAW_PARTIAL(T1@[FRAME_A, FRAME_B, CHI3,
CHI4]) + SIEVE_CORE_OPEN + T1(C_K 2.45/4.91/1.52/1.62, viol
27/84 + 6/6 + 14/37 + 12/37, global product ceiling 23.70) +
PACK(0 violations, min g 0.375) + SMALLBALL(1033 bands, 0
violations; align med 0.24..0.28 below the 0.5 floor) +
COMPOSITION(m_0* 10^23.5 census) + SCRAMBLE(P1_ADMISSION x3) +
TWIN(1.0e-07) + MUSTFAIL_LEDGER.
THE HEADLINE FINDINGS:
(1) THE CORE HOLDS -- T2' IS A 0-VIOLATION CENSUS THEOREM ON
ALL FOUR ARITHMETIC/FAMILY WORLDS: the quadratic packing law
S_r <= 2^{-2r}(1+r)^2 holds POINTWISE on every one of the 181
admitted rows (89 frame A + 8 frame B + 42 chi3 + 42 chi4) at
every dyadic level r = 1..12, with enormous headroom: the
whole small-gap mass of the lane lives at r = 1 (g in (1/4,
1/2]: max S_1 = 0.0170 frame A / 0.0052 frame B / 0.0238 chi3
/ 0.0439 chi4, carried by 12 + 4 + 1 + 3 rows) and S_r = 0
IDENTICALLY for r >= 2 on ALL 181 rows -- the minimal
normalized local gap of the entire round is 0.375: gaps below
ONE QUARTER of the local median DO NOT OCCUR, in either
construction family or any of the three arithmetics.  "Very
tight coincidences may exist, but not with mass" is a measured
fact -- and stronger: below g = 3/8 they do not exist AT ALL
on the admitted surface.  The dyadic summation T2' => T2 is
exact (warded one-sided 0.0): T2val max 1.29/1.33/1.14/1.13
per family, C_G_cens = 0.100 at A = 2.
(2) T1 IS DEPTH-GRADED CENSUS, NOT A FIRST-K LAW (the honest
partial): the r306 first-K freeze fails the localization on
ALL FOUR families -- frame A C_K(cal-5) = 2.45 vs test max
15.93 at kz111 (27/84 above), frame B 4.91 vs 23.70 at kz117
(6/6 -- every deep row exceeds its two shallow anchors), chi3
1.52 vs 3.91 at kz32 (14/37), chi4 1.62 vs 3.09 (12/37).  The
LOCAL product (m q_i/log m) g_i grows with depth exactly like
the K2 product FAB grel does (the max rows ARE the K2 spike
rows kz111/kz117/kz32) -- the localization is the right
coordinate but inherits the K2 growth: a first-shallow-rows
freeze is the wrong constant rule at every localization level
(the r324/r351 lesson, now measured locally).  T2' needed NO
calibration at all -- the PACKING FORM with a-priori bars is
the family-robust statement of the lane.
(3) THE SMALL-BALL BAND STRUCTURE (D) CARRIES AS CENSUS: 1033
dyadic source bands (>= 5 members) across the 181 rows, 0
band-level violations of SB_r <= 2^{-2r}(1+r)^2; the stress
spikes kz51 (min g 0.533) and kz111 (min g 0.571) have NO
sub-half gap at all -- the spike atoms are NOT tight-gap
atoms, the r = 1 mass sits on other, non-spike rows.  Band
alignment |x_i|/A1_i med 0.27/0.24/0.28/0.26 per family:
BELOW the 0.5 floor -- within-band comparability holds in
MASS form, NOT in signed-survival form (typed honestly; the
sieve target (D) is the mass form, which is what carries).
(4) THE COMPOSITION IS PURE POLYLOG BUT CENSUS-EXPENSIVE: with
the measured global product ceiling C_K = 23.70 (census, NOT a
frozen law -- the per-family freezes top out at 4.91) and
C_G_cens = 0.100, M_3 <= C_K^2 C_G (log m)^4/m^2 gives m_0* =
10^23.5 vs r351 10^18.9 / r353 10^20.5 / r306 census 10^13.5:
the Carleson detour does not yet beat the direct census
because C_K enters SQUARED where FAB enters once -- the
winning form needs a T1 constant RULE (family-uniform), which
is the second named open item.  All exact wards close: M3
composition 0.0 one-sided, N2 >= N3 181/181, T2 summation 0.0,
quantization 9.1e-13 (bar 1e-6), multiplicity <= 2 on 181/181
(0 drops), FAB identity 2.0e-16, K2 chain 0.0, FDD dictionary
2.5e-16, contribution wards green on all four families.
(5) THE PROOF-SKETCH TYPING AFTER THIS ROUND: SATZ = fold
multiplicity <= 2 (A), mesh identity + theta-grid quantization
(B), dyadic summation T2' => T2, N2 >= N3, the M3 composition
algebra; DICTIONARY = FDD q_i, band MASS comparability;
CERTIFIED CENSUS = T2' at the sealed (1.0, 2.0) bars (0/181 x
12), the small-ball band form (0/1033), the min-g floor 0.375;
OPEN (the named specialist questions) = (i) the in-the-mean
sieve (D) as a theorem: for the folded log p^k phases prove
sum_{i in B, g_i <= t} a_i <= C t^2 (log m)^B sum_B a_i per
dyadic source band (small-ball / large sieve on average, NO
pointwise Baker bounds), and (ii) the family-uniform T1
constant rule.  SCRAMBLES: all three matched channels break at
P1 = POSITIVE_PREFIX ADMISSION (frame-A w9 nf 21, frame-B kz80
nf 3, chi3 w9 nf 37 -- the r353/r355/r357 records reproduced):
the packing's binding source precondition is the ADMISSION of
the arithmetic comb itself, named precisely.  TWIN devs 1.0e-7.
ANCHORS bit-near: C_K2X 11.87 at kz111 (89 rows); frame-B 8/8
re-admitted, FAB/grel table within tol, K2 max 5.95; chi3
42/42 max FABg 4.73 at kz32; chi4 42/42 max 5.16; MAIN-42 max
6.95.  Must-fails: e1 protocol-CAUGHT twice (AST rho@663 +
pin (2.0, 4.0) vs (2.0, 0.5)) / e2 CAUGHT exact (the global-
min mutant breaks the sealed bar at S_2 1.00 > 0.5625 where
the true column passes at 0.33 -- the r355 supercriticality
reproduced as a mutant) / e3 protocol-CAUGHT twice (AST + pin
11.87 vs 1.0) / e4 protocol-CAUGHT twice (pin 9.216 vs 1.0) /
e5 CAUGHT exact (rejects the valid mesh dev 1.0) + m6a/m6b
FLAGGED (t_term@703 / g_branch@710).  Runtime 711.3 s
calibration / record run1/run2 byte-identical up to WALL /
0.6 s smoke.  AMENDMENTS AFTER FREEZE: NONE except this
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
import principal_bessel_probe as PB            # noqa: E402 r243
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import window_border_transfer_probe as WBT     # noqa: E402 r298
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import companion_orbit_packing_probe as COP    # noqa: E402 r333
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import fold_density_dictionary_probe as FDD    # noqa: E402 r339
import fold_two_scale_balance_probe as FTS     # noqa: E402 r344
import thirdarm_spike_law_probe as TSL         # noqa: E402 r349
import qmax_growth_law_probe as QGL            # noqa: E402 r351
import second_family_erosion_probe as SFE      # noqa: E402 r353
import k2_source_formula_probe as KSF          # noqa: E402 r355
import dirichlet_secondworld_probe as DSW      # noqa: E402 r330
import dirichlet_matched_frame_probe as DMF    # noqa: E402 r357
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import lstar_margin_scaling_probe as LM        # noqa: E402 r286 READ-ONLY
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import verify_lstar_instance as V              # noqa: E402 document

# ---------------- imported constants (verbatim)
H_CAP = FTS.H_CAP
EXT_H_MAX = FTS.EXT_H_MAX
EXT2_H_MAX = FTS.EXT2_H_MAX
K_EXT = FTS.K_EXT
EXT2_POOL_CAP = FTS.EXT2_POOL_CAP
K_EXT2 = FTS.K_EXT2
EXT3_KZ_B = FTS.EXT3_KZ_B
EXT3_KZ_A = FTS.EXT3_KZ_A
EXT4_KZ = TSL.EXT4_KZ
EXT5_KZ_B = SFE.EXT5_KZ_B
EXT5_KZ_A = SFE.EXT5_KZ_A
MULT_CAP = FTS.MULT_CAP
CRIT_EXP = FTS.CRIT_EXP
TOY_BAR = FTS.TOY_BAR
TB_WARD_BAR = FTS.TB_WARD_BAR
TB_WARD_BAR_DEEP = FTS.TB_WARD_BAR_DEEP
TB_WARD_BAR_X345 = max(FTS.TB_WARD_BAR_X3, TSL.TB_WARD_BAR_X4,
                       QGL.TB_WARD_BAR_X5)
TB_WARD_BAR_B = SFE.TB_WARD_BAR_B
DEEP_N = FTS.DEEP_N
FAB_ID_BAR = QGL.FAB_ID_BAR
CHAIN_BAR = FTS.CHAIN_BAR
DICT_BAR = FTS.DICT_BAR
NU_A = core.NU_MAIN
NU_B = SFE.NU_B
FRAMEB_KZ = KSF.FRAMEB_KZ
MESH_DEV_HI = KSF.MESH_DEV_HI
W_LOC = EFA.GAP_W
LPQ3 = DMF.LPQ3
LPQ4 = DMF.LPQ4
Q_CHI3 = DMF.Q_CHI3
Q_CHI4 = DMF.Q_CHI4

# ---------------- NEW sealed constants of this round (spec above)
N_CAL_T1 = 5
N_CAL_FB = 2
K2_EPS = 1.0e-9
PACK_EPS = 1.0e-12
C_PACK = 1.0
A_PACK = 2.0
R_MAX = 12
C_SB = 1.0
B_SB = 2.0
BAND_MIN = 5
S_BAND_MAX = 20
ALIGN_FLOOR = 0.5
QUANT_BAR = 1.0e-6
CHI_TB_BAR = 1.0e-3
TWIN_BAR = 1.0e-3
TWIN_TOL = 1.0e-8
SCR_SEED = 1
STRESS_KZ = (51, 111)
RUNTIME_BAR = 1800.0
# anchor records (gate-side literals)
R353_CK2X = 11.87
R353_CK2X_TOL = 0.02
R353_CK2X_KZ = 111
R353_FB_TABLE = KSF.R353_FB_TABLE
R353_FB_FAB_TOL = 0.02
R353_FB_GREL_TOL = 0.003
R353_FB_K2MAX = 5.95
R353_FB_K2MAX_TOL = 0.02
R357_CHI3_MAX = 4.73
R357_CHI3_MAX_KZ = 32
R357_CHI4_MAX = 5.16
R357_MAIN_MAX = 6.95
R357_TOL = 0.02
M0_REFS = (18.9, 20.5, 13.5)
CK_FRAMEA_LIT = 11.87          # e3 withheld marker (forbidden in scope)
# import-integrity SHA prefixes (sealed)
KSF_SHA_PREFIX = "1f14bd93"
DMF_SHA_PREFIX = "4bf1a94b"
SFE_SHA_PREFIX = "bd89e331"
QGL_SHA_PREFIX = "67102e4c"
EFA_SHA_PREFIX = "bbfaf199"
DSW_SHA_PREFIX = "66526018"

R358_TABLE_LITERALS = frozenset(KSF.R355_TABLE_LITERALS
                                | {4.73, 5.16, 6.95})

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
    return (not bad), ("NO zero/prime oracles; the gap builders "
                       "consume atom positions + block ids + window "
                       "depth + sealed thresholds ONLY; ground truth "
                       "and record literals enter gates and census "
                       "tables only"
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


BOUND_FORBIDDEN = COP.BOUND_FORBIDDEN
PHI3_FORBIDDEN = COP.PHI3_FORBIDDEN
QMAX_FORBIDDEN = COP.QMAX_FORBIDDEN
SCOPE_FORBIDDEN_358 = {"rho", "t" + "_term", "g" + "_branch",
                       "CK_FRAMEA" + "_LIT", "fabg" + "_true"}


def scope_audit(funcname, forbidden):
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
                            in R358_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders (source-pure, AST-audited):
# ---------------- consume atom POSITIONS, BLOCK IDS, window DEPTH
# ---------------- and SEALED thresholds only.  q columns, FAB,
# ---------------- products, S_r, T2val, bands and every census on
# ---------------- them are TARGET-SIDE DIAGNOSTICS computed in
# ---------------- the gate section (disclosed).
def theta_col(pos, n_w):
    """fold positions -> theta-grid units: t = arccos(x) LL/(2 pi)
    with LL = 4 N_w - 2 (the frame mesh, exact by construction --
    warded near-integer downstream).  Consumes positions + depth
    only."""
    ll = 4 * int(n_w) - 2
    th = np.arccos(np.clip(np.asarray(pos, float), -1.0, 1.0))
    return th * float(ll) / (2.0 * math.pi)


def gap_ledger(pos, blk, m, n_w):
    """THE SEALED LOCAL-GAP LEDGER: distinct fold-group positions
    per block (the r314 lexsort segmentation on (block, position),
    values NOT consumed) -> unweighted block centers on the theta
    grid -> per-block one-sided min distance to the adjacent block
    centers (grid units).  Returns centers (theta order), gaps,
    the theta-order permutation of block ids, and the worst
    grid-quantization deviation of the group positions.  Consumes
    positions + block ids + depth only."""
    pos = np.asarray(pos, float)
    blk = np.asarray(blk, int)
    o = np.lexsort((pos, blk))
    pb = blk[o]
    pp = pos[o]
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gpos = pp[new]
    gblk = pb[new]
    tg = theta_col(gpos, n_w)
    qdev = float(np.max(np.abs(tg - np.round(tg)))) if len(tg) \
        else 0.0
    cent = np.zeros(m)
    cnt = np.zeros(m)
    np.add.at(cent, gblk, tg)
    np.add.at(cnt, gblk, 1.0)
    cent = cent / np.maximum(cnt, 1.0)
    oc = np.argsort(cent, kind="stable")
    cs = cent[oc]
    if m >= 2:
        d = np.diff(cs)
        gaps = np.empty(m)
        gaps[0] = d[0]
        gaps[-1] = d[-1]
        if m > 2:
            gaps[1:-1] = np.minimum(d[:-1], d[1:])
    else:
        gaps = np.ones(m)
    mono = bool(np.all(np.diff(cs) > 0.0)) if m >= 2 else True
    return dict(cent=cs, gaps=gaps, oc=oc, qdev=qdev, mono=mono,
                ng=int(len(gpos)))


def g_norm(gaps):
    """the sealed normalization: EFA.grel_col VERBATIM (w = GAP_W)
    applied to the block-gap column -- the zone-grel convention
    one level down.  Consumes the passed gap column only."""
    m = len(gaps)
    return np.asarray(EFA.grel_col(list(range(m)), list(gaps),
                                   w=W_LOC), float)


def pack_bar(r):
    """the sealed T2' dyadic packing bar C_PACK 2^{-2r}
    (1+r)^{A_PACK} (a-priori, never moved)."""
    return C_PACK * (4.0 ** (-r)) * (1.0 + r) ** A_PACK


def sb_bar(r):
    """the sealed small-ball band bar C_SB 2^{-2r} (1+r)^{B_SB}
    (a-priori, never moved)."""
    return C_SB * (4.0 ** (-r)) * (1.0 + r) ** B_SB


def t1_tree(cal_max, test_max, eps):
    """the sealed T1 per-family rule: C_K = the calibration
    maximum; violation iff the test maximum exceeds C_K + eps
    (booleans decided by the caller per row; this is the frozen
    constant rule, r306 first-K convention)."""
    return cal_max, bool(test_max > cal_max + eps)


def main_tree_358(leak, brk, pack_fams, t1_fams):
    """the sealed main-letter tree (total, exactly one fires;
    order sealed): TARGET_LEAK > LAW_STATE_NOT_EXACT >
    PACKING_FAILS > QUADRATIC_LAW_PARTIAL >
    GAP_CARLESON_CERTIFIED."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if pack_fams:
        return "PACKING_FAILS"
    if t1_fams:
        return "QUADRATIC_LAW_PARTIAL"
    return "GAP_CARLESON_CERTIFIED"


def scr_letter(p1_ok, mult_ok, quant_ok, band_ok, pack_ok):
    """the sealed scramble precondition order (first failing named):
    P1 POSITIVE_PREFIX admission > P2 fold multiplicity > P3 grid
    quantization > P4 band alignment > P5 packing."""
    if not p1_ok:
        return "P1_ADMISSION"
    if not mult_ok:
        return "P2_FOLD_MULT"
    if not quant_ok:
        return "P3_QUANTIZATION"
    if not band_ok:
        return "P4_BAND_ALIGN"
    if not pack_ok:
        return "P5_PACKING"
    return "NO_BREAK"


# ---------------- must-fail mutants
def mutant_g_from_q(rho):
    """e1 MUST-FAIL (protocol): the g column read back from the
    mass column (consumes rho) -- AST-FLAGGED; on the sealed toy
    returns (2.0, 4.0) != the sealed positional column
    (2.0, 0.5)."""
    return tuple(1.0 / max(float(v), 1e-300) for v in rho)


def mutant_global_gmin(g):
    """e2 MUST-FAIL (the r355 error as a mutant): the per-atom gap
    column replaced by the GLOBAL minimum replicated -- one small
    gap sets the bound for the entire mass; on the sealed toy the
    mutant packing mass breaks the sealed bar where the true
    column passes -- CAUGHT exact."""
    mn = min(float(v) for v in g)
    return tuple(mn for _ in g)


def mutant_ck_framea(rho):
    """e3 MUST-FAIL (protocol): the frame-A record constant applied
    to every family (consumes rho AND the withheld literal) --
    AST-FLAGGED; on the sealed toy returns 11.87 != the sealed
    per-family toy freeze 1.0."""
    _ = rho
    return CK_FRAMEA_LIT


def mutant_bars_posthoc(rho, rs):
    """e4 MUST-FAIL (protocol): C_PACK set at the seen mass column
    (consumes rho) -- AST-FLAGGED; on the sealed toy returns 9.216
    != the sealed C_PACK 1.0."""
    return max(float(rho[i]) * (4.0 ** rs[i])
               / (1.0 + rs[i]) ** A_PACK for i in range(len(rho)))


def mutant_mesh_interval(dev):
    """e5 MUST-FAIL: the mesh identity with the WRONG interval
    (0, 0.5] instead of (0, 1.5] -- rejects the valid by-hand mesh
    toy (dev 1.0) -- CAUGHT exact."""
    return 0.0 < float(dev) <= 0.5


def mutant_gift_bound(rc, P):
    """m6a MUST-FAIL (r355 verbatim): a builder consuming the
    withheld ground-truth terminal drive key -- AST-FLAGGED."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m6b MUST-FAIL (r355 verbatim): a builder consuming the
    branch label -- AST-FLAGGED."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- gate-side evaluation (r357 eval_k2 body extended
# ---------------- by the genealogy/position surface; cross-warded
# ---------------- bitwise against DMF.eval_k2 at w9)
def eval_gap(rc):
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    cb = cts[~ed]
    xb = bxs[~ed]
    runs = PBB.runs_split(cb)
    brk, m, jb = WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=m) if m \
        else np.zeros(0)
    Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                              rc["hi"], brk, m)
    Pd = Pb - Pw
    cm = RY3.cubic_moments(Pd)
    absm = float(np.sum(np.abs(rc["ct"]))) \
        + float(np.sum(np.abs(rc["cw"])))
    tb_dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
        / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
    degenerate = (cm["L1"] <= DSW.DEG_FLOOR * absm) or (m < 2)
    if degenerate:
        return dict(degenerate=True, m=m, tb_dev=tb_dev)
    edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], DSW.EDGE_F)
    xw = rc["xu"][~edw]
    vw = -rc["cw"][~edw]
    jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
    pos_all = np.concatenate([xb, xw])
    val_all = np.concatenate([cb, vw])
    blk_all = np.concatenate([jb, jw]).astype(int)
    src_all = np.concatenate([np.zeros(len(xb)), np.ones(len(xw))])
    gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
    sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
    x_dev = float(np.max(np.abs(sct["x"] - Pd))
                  / max(np.max(np.abs(Pd)), 1e-300))
    rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
    mqs = FAP.m2_qmax_state(sct["x"])
    led = GMC.group_mass_ledger(pos_all, val_all, blk_all,
                                src_all, m)
    pst = QMO.pileup_state(sct["x"], val_all, blk_all)
    hst = GMC.heavy_state(sct["x"], led)
    dic = FDD.martingale_moment_dictionary(sct["x"])
    A1 = np.bincount(blk_all, weights=np.abs(val_all), minlength=m)
    mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
    gl = gap_ledger(pos_all, blk_all, m, rc["N"])
    return dict(degenerate=False, m=m, rho2=rho2, mqs=mqs,
                pst=pst, hst=hst, x_dev=x_dev, tb_dev=tb_dev,
                x=sct["x"], A1=A1, mx_mult=mx_mult, gen_ng=gen["ng"],
                gl=gl, dic=dic)


def gap_columns(ev):
    """gate-side diagnostics: the q and g columns of one live row
    in theta order + the derived T1/T2'/T2/band columns."""
    m = ev["m"]
    gl = ev["gl"]
    oc = gl["oc"]
    ax = np.abs(np.asarray(ev["x"], float))
    tot = float(np.sum(ax))
    q = (ax / max(tot, 1e-300))[oc]
    a1 = np.asarray(ev["A1"], float)[oc]
    align = ax[oc] / np.maximum(a1, 1e-300)
    g = g_norm(gl["gaps"])
    lg = math.log(float(m))
    prod = (float(m) * q / lg) * g
    Sr = []
    for r in range(1, R_MAX + 1):
        Sr.append(float(np.sum(q[g <= 2.0 ** (-r)])))
    t2v = float(np.sum(q / g ** 2))
    # exact one-sided dyadic-summation bound (shells on g)
    bound = float(np.sum(q[g > 1.0]))
    rr = np.floor(-np.log2(np.maximum(g, 1e-300))).astype(int)
    for r in sorted(set(int(v) for v in rr[g <= 1.0])):
        msk = (rr == r) & (g <= 1.0)
        bound += float(np.sum(q[msk])) * 4.0 ** (r + 1)
    m3 = float(np.sum(q ** 3))
    n2 = 1.0 / max(float(np.sum(q ** 2)), 1e-300)
    n3 = m3 ** (-0.5) if m3 > 0 else 0.0
    # dyadic source bands on the block atom mass A1
    amax = float(np.max(a1)) if len(a1) else 0.0
    band = np.minimum(np.floor(np.log2(
        max(amax, 1e-300) / np.maximum(a1, 1e-300))).astype(int),
        S_BAND_MAX)
    bands = {}
    for s in sorted(set(int(v) for v in band)):
        msk = band == s
        if int(np.sum(msk)) < BAND_MIN:
            continue
        tot_b = float(np.sum(a1[msk]))
        sbr = [float(np.sum(a1[msk & (g <= 2.0 ** (-r))]))
               / max(tot_b, 1e-300) for r in range(1, R_MAX + 1)]
        bands[s] = dict(n=int(np.sum(msk)), sbr=sbr,
                        align_med=float(np.median(align[msk])))
    return dict(q=q, g=g, prod=prod, maxprod=float(np.max(prod)),
                Sr=Sr, t2v=t2v, t2bound=bound, m3=m3, n2=n2, n3=n3,
                lg=lg, bands=bands, ming=float(np.min(g)),
                align_med=float(np.median(align)))


def solve_m0(log_rhs):
    t = math.log(73.0)
    while t < 1e7:
        if CRIT_EXP * t >= log_rhs(t):
            return t / math.log(10.0)
        t *= 1.02
    return None


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("local_gap_carleson_probe -- "
          "PRIME.L2.K2.LOCAL_GAP_CARLESON.01 (round 358)")
    print("SPEC_SHA %s   (KSF %s / DMF %s / SFE %s)"
          % (SPEC_SHA[:16], KSF.SPEC_SHA[:16], DMF.SPEC_SHA[:16],
             SFE.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + trees + mutants + audits + "
                        "the four w9 worlds with full eval + exact "
                        "wards; ladders, T1/T2', bands, "
                        "composition, scrambles, twin and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (KSF.SPEC_SHA.startswith(KSF_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX)
              and QGL.SPEC_SHA.startswith(QGL_SHA_PREFIX)
              and EFA.SPEC_SHA.startswith(EFA_SHA_PREFIX)
              and DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "sealed BEFORE evaluation: the g_i coordinate (block "
          "centers on the theta grid LL = 4N-2, one-sided min "
          "gaps, EFA.grel_col normalization w = %d verbatim), the "
          "T1 per-family first-K freezes (N_CAL %d / frame-B %d "
          "-- NO frame-A constant on any other family), the T2' "
          "bars (C %.1f, A %.1f, r <= %d, a-priori), the "
          "small-ball band bars (C %.1f, B %.1f, band floor %d), "
          "the precondition order, all letters; import integrity "
          "KSF %s / DMF %s / SFE %s / QGL %s / EFA %s / DSW %s"
          % (W_LOC, N_CAL_T1, N_CAL_FB, C_PACK, A_PACK, R_MAX,
             C_SB, B_SB, BAND_MIN, KSF.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], SFE.SPEC_SHA[:8], QGL.SPEC_SHA[:8],
             EFA.SPEC_SHA[:8], DSW.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("theta_col", "gap_ledger", "g_norm",
                    "pack_bar", "sb_bar", "t1_tree",
                    "main_tree_358", "scr_letter")
    sc_own = []
    pure_lits = []
    for fn in own_builders:
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
        sc_own += scope_audit(fn, SCOPE_FORBIDDEN_358)
        pure_lits += literal_audit(fn)
    sc_e1 = scope_audit("mutant_g_from_q", SCOPE_FORBIDDEN_358)
    sc_e3 = scope_audit("mutant_ck_framea", SCOPE_FORBIDDEN_358)
    sc_e4 = scope_audit("mutant_bars_posthoc", SCOPE_FORBIDDEN_358)
    sc_m6a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_m6b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    leak = bool(frag) or bool(sc_own) or bool(pure_lits) or not okf
    check("G03-scope-audits", (not frag) and (not sc_own)
          and (not pure_lits) and len(sc_e1) >= 1
          and len(sc_e3) >= 2 and len(sc_e4) >= 1
          and len(sc_m6a) >= 1 and len(sc_m6b) >= 1,
          "fragment audit clean (%d); the %d module-own builders "
          "clean vs BOUND/PHI3/QMAX/358 sets (%d id hits) and vs "
          "the sealed record-literal set (%d literal hits); e1 "
          "FLAGGED (%s); e3 FLAGGED twice (%s); e4 FLAGGED (%s); "
          "m6a/m6b FLAGGED (%s / %s)"
          % (len(frag), len(own_builders), len(sc_own),
             len(pure_lits), sc_e1[0] if sc_e1 else "MISS",
             sc_e3[0] if sc_e3 else "MISS",
             sc_e4[0] if sc_e4 else "MISS",
             sc_m6a[0] if sc_m6a else "MISS",
             sc_m6b[0] if sc_m6b else "MISS"))

    # ---------------- S1 toys + trees + mutant pins
    section("S1  SEALED TOYS + TREES + MUTANT PINS (all by hand)")
    # gap toy: centers (2, 4, 5, 9, 12) -> gaps (2, 1, 1, 3, 3)
    toy_gaps = [2.0, 1.0, 1.0, 3.0, 3.0]
    toy_g = EFA.grel_col(list(range(5)), toy_gaps, w=2)
    toy_g_pin = (2.0, 0.5, 0.4, 3.0, 1.5)
    gaptoy_ok = all(abs(toy_g[i] - toy_g_pin[i]) <= TOY_BAR
                    for i in range(5))
    # pack toy A (0 violations) + toy B (3 violations at r 2..4)
    qA = np.array([0.5, 0.3, 0.2])
    gA = np.array([1.0, 0.4, 0.2])
    violA = sum(1 for r in range(1, 5)
                if float(np.sum(qA[gA <= 2.0 ** -r]))
                > pack_bar(r) + PACK_EPS)
    qB = np.array([0.1, 0.9])
    gB = np.array([1.0, 0.05])
    violB = [r for r in range(1, 5)
             if float(np.sum(qB[gB <= 2.0 ** -r]))
             > pack_bar(r) + PACK_EPS]
    packtoy_ok = (violA == 0 and violB == [2, 3, 4]
                  and abs(pack_bar(2) - 0.5625) <= TOY_BAR)
    # T2 dyadic-summation + M3-composition + N2N3 Fractions toys
    qF = (Fr(1, 2), Fr(1, 4), Fr(1, 4))
    gF = (Fr(1), Fr(1, 2), Fr(1, 2))
    t2F = sum(q / (g * g) for q, g in zip(qF, gF))
    shellF = qF[0] * 4 + (qF[1] + qF[2]) * 16
    m3F = sum(q ** 3 for q in qF)
    compF = (Fr(1) * Fr(2) ** 2 / Fr(4) ** 2) * t2F
    n2F = 1 / sum(q * q for q in qF)
    n3sqF = 1 / m3F
    fr_ok = (t2F == Fr(5, 2) and shellF <= 10
             and t2F <= shellF
             and m3F == Fr(5, 32) and compF == Fr(5, 8)
             and m3F <= compF
             and n2F ** 2 == Fr(64, 9) and n3sqF == Fr(32, 5)
             and n2F ** 2 >= n3sqF)
    # mesh toy (r355 verbatim by hand)
    t_dk = 0.5 * 1.0 / 2.0
    t_mz = int(math.ceil(10.0 / t_dk - 1.0e-9)) + 1
    if t_mz % 2:
        t_mz += 1
    t_h = t_mz // 2
    t_dev = float(t_h) - 2.0 * (10.0 / 1.0)
    meshtoy_ok = (t_h == 21 and abs(t_dev - 1.0) <= TOY_BAR
                  and 0.0 < t_dev <= MESH_DEV_HI)
    # mutant pins
    mut1 = mutant_g_from_q((0.5, 0.25))
    toy1_sealed = (2.0, 0.5)
    mut2 = mutant_global_gmin((1.0, 0.25, 0.5))
    qE = np.array([1.0, 1.0, 1.0]) / 3.0
    gE_true = np.array([1.0, 0.25, 0.5])
    gE_mut = np.array(mut2)
    S2_true = float(np.sum(qE[gE_true <= 0.25]))
    S2_mut = float(np.sum(qE[gE_mut <= 0.25]))
    e2_ok = (mut2 == (0.25, 0.25, 0.25)
             and S2_true <= pack_bar(2) + PACK_EPS
             and S2_mut > pack_bar(2) + PACK_EPS)
    mut3 = mutant_ck_framea((1.0, 2.0))
    toy3_sealed = 1.0
    mut4 = mutant_bars_posthoc((0.9,), (4,))
    toy4_sealed = C_PACK
    mut5 = mutant_mesh_interval(1.0)
    e5_truth = (0.0 < 1.0 <= MESH_DEV_HI)
    # sealed trees
    tr = (main_tree_358(True, True, True, True),
          main_tree_358(False, True, True, True),
          main_tree_358(False, False, True, True),
          main_tree_358(False, False, False, True),
          main_tree_358(False, False, False, False))
    tr_ok = tr == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                   "PACKING_FAILS", "QUADRATIC_LAW_PARTIAL",
                   "GAP_CARLESON_CERTIFIED")
    sc_br = (scr_letter(False, True, True, True, True),
             scr_letter(True, False, True, True, True),
             scr_letter(True, True, False, True, True),
             scr_letter(True, True, True, False, True),
             scr_letter(True, True, True, True, False),
             scr_letter(True, True, True, True, True))
    sc_ok = sc_br == ("P1_ADMISSION", "P2_FOLD_MULT",
                      "P3_QUANTIZATION", "P4_BAND_ALIGN",
                      "P5_PACKING", "NO_BREAK")
    t1a, t1v = t1_tree(1.0, 1.2, K2_EPS)
    t1b, t1w = t1_tree(1.0, 0.8, K2_EPS)
    t1_ok = (t1a == 1.0 and t1v and t1b == 1.0 and not t1w)
    check("G10-toy-exactness", gaptoy_ok and packtoy_ok and fr_ok
          and meshtoy_ok and tr_ok and sc_ok and t1_ok,
          "gap toy g = %s == pin %s; pack toy A 0 viol / toy B "
          "viol %s == [2, 3, 4] (bar(2) %.4f); Fractions toys "
          "EXACT: T2 %s <= shell %s, M3 %s <= comp %s, N2^2 %s "
          ">= N3^2 %s; mesh toy h %d dev %.1f in (0, %.1f]; main "
          "tree %s; scramble letters %s; T1 rule (viol %s / pass "
          "%s)"
          % (str(tuple(round(v, 3) for v in toy_g)),
             str(toy_g_pin), str(violB), pack_bar(2), t2F, shellF,
             m3F, compF, n2F ** 2, n3sqF, t_h, t_dev, MESH_DEV_HI,
             "OK" if tr_ok else str(tr),
             "OK" if sc_ok else str(sc_br), t1v, not t1w))
    check("G11-mutant-pins", tuple(mut1) == (2.0, 4.0)
          and mut1 != toy1_sealed and e2_ok
          and abs(mut3 - CK_FRAMEA_LIT) <= TOY_BAR
          and mut3 != toy3_sealed
          and abs(mut4 - 9.216) <= 1e-9 and mut4 != toy4_sealed
          and (mut5 is False) and e5_truth,
          "e1 pin %s != sealed %s; e2 pin %s (mutant S_2 %.2f > "
          "bar %.4f, true %.2f passes -- the r355 global-min "
          "supercriticality reproduced); e3 pin %.2f != family "
          "freeze %.1f; e4 pin %.3f != sealed C_PACK %.1f; e5 "
          "mutant rejects the valid mesh (False vs truth True)"
          % (str(tuple(mut1)), str(toy1_sealed), str(mut2),
             S2_mut, pack_bar(2), S2_true, mut3, toy3_sealed,
             mut4, toy4_sealed, ))

    # ---------------- S2 world construction
    section("S2  THE FOUR WORLD FAMILIES (construction + "
            "admission + frame reproductions)")
    # trivial frame reproductions (exact, live, cheap)
    pb4 = SFE.wpack_b(9, NU_A)
    pa9 = BH.wpack(9)
    frb_ok = (pb4["N"] == pa9["N"] and pb4["nf"] == pa9["nf"])
    alpha9c = float(core.U_ALL[9])
    ka9c = core.atoms_in(alpha9c)
    db_v = SFE.window_data_b(9, NU_A)
    db_chi = DMF.chi_window_data(9, 0.0, math.log(math.pi),
                                 (core.U_ALL[:ka9c].copy(),
                                  core.MU_ALL[:ka9c].copy()))
    chi_ok = all(np.array_equal(db_v[k], db_chi[k])
                 for k in ("xs", "ws", "ys", "vs"))
    # mesh identity ward (r355 verbatim, slim: NU 2 + 4 pools)
    mesh_bad = []
    mesh_n = {}
    for nu, hcap in ((NU_B, SFE.H_B_CAP), (NU_A, core.HCAP)):
        zones_nu = SFE.frameb_pool(nu, core.H_MIN, hcap,
                                   SFE.Z2_CAP if nu == NU_B
                                   else None)
        mesh_n[nu] = len(zones_nu)
        for h, kz in zones_nu:
            hh, dev = KSF.mesh_h(kz, nu)
            if hh != h or not (0.0 < dev <= MESH_DEV_HI + 1e-9):
                mesh_bad.append((kz, nu, hh, h, dev))
    check("G20-frame-reproductions", frb_ok and chi_ok
          and not mesh_bad,
          "NU = %d reproduction (SFE.wpack_b == BH.wpack at w9: N "
          "%d == %d, nf %s == %s); chi trivial frame (a = 0, q = "
          "1) == SFE.window_data_b BITWISE at w9 [%s]; THE MESH "
          "IDENTITY h - NU u in (0, %.1f] EXACT on %s pool zones "
          "at NU (%d, %d) (violations %s) -- the local gap "
          "quantization is mesh-parametrized, fit-free"
          % (NU_A, pb4["N"], pa9["N"], str(pb4["nf"]),
             str(pa9["nf"]), "OK" if chi_ok else "BROKEN",
             MESH_DEV_HI,
             str(tuple(mesh_n[k] for k in sorted(mesh_n))),
             NU_B, NU_A,
             str(mesh_bad[:3]) if mesh_bad else "0"))
    if smoke:
        packs_a = [pa9]
        packs_b = [SFE.wpack_b(9, NU_B)]
        u3, w3c, _nn3, _c3 = DMF.chi_window_comb(9, Q_CHI3)
        u4, w4c, _nn4, _c4 = DMF.chi_window_comb(9, Q_CHI4)
        packs_c3 = [DMF.chi_wpack(9, 1.0, LPQ3, (u3, w3c))]
        packs_c4 = [DMF.chi_wpack(9, 1.0, LPQ4, (u4, w4c))]
        check("G21-family-census", all(
            p["nf"] is None and p.get("complete", True)
            for p in packs_a + packs_b + packs_c3 + packs_c4),
            "SMOKE: the four w9 worlds built (frame A N %d / "
            "frame B N %d / chi3 N %d / chi4 N %d, all "
            "POSITIVE_PREFIX + chain-complete); ladders skipped"
            % (packs_a[0]["N"], packs_b[0]["N"],
               packs_c3[0]["N"], packs_c4[0]["N"]))
    else:
        # FRAME A: the sealed 89-row surface (r353/r355 verbatim)
        kzs_l = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs_l.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
            elif h <= EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs_l]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        ekz2.sort()
        pool2 = epool[K_EXT:] + [BH.wpack(kz)
                                 for _h, kz in ekz2[:EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:K_EXT2]
        ext3 = [BH.wpack(kz) for kz in EXT3_KZ_B + EXT3_KZ_A]
        ext4 = [BH.wpack(kz) for kz in EXT4_KZ]
        ext5 = [BH.wpack(kz) for kz in EXT5_KZ_B + EXT5_KZ_A]
        packs_a = ladder + ext + ext2 + ext3 + ext4 + ext5
        okA = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder)
               and len(ext) == K_EXT
               and all(p["nf"] is None for p in packs_a))
        # FRAME B: the 8 sealed r353 anchors ADOPTED AS-IS
        packs_b = [SFE.wpack_b(kz, NU_B) for kz in FRAMEB_KZ]
        okB = all(p["nf"] is None and p["complete"]
                  for p in packs_b)
        # CHI3 / CHI4: the 42 matched terminal rows each
        kzs_c = list(V.admissible_indices())
        packs_c3 = []
        packs_c4 = []
        excl = []
        for kz in kzs_c:
            u3, w3c, _nn, _ch = DMF.chi_window_comb(kz, Q_CHI3)
            if len(u3) < V.N_ATOM_MIN:
                excl.append((kz, 3))
                continue
            packs_c3.append(DMF.chi_wpack(kz, 1.0, LPQ3,
                                          (u3, w3c)))
        for kz in kzs_c:
            u4, w4c, _nn, _ch = DMF.chi_window_comb(kz, Q_CHI4)
            if len(u4) < V.N_ATOM_MIN:
                excl.append((kz, 4))
                continue
            packs_c4.append(DMF.chi_wpack(kz, 1.0, LPQ4,
                                          (u4, w4c)))
        okC = (len(packs_c3) == 42 and len(packs_c4) == 42
               and all(p["complete"]
                       for p in packs_c3 + packs_c4))
        check("G21-family-census", okA and okB and okC,
              "FRAME A: %d rows (42 ladder + %d ext + %d ext2 + "
              "%d EXT3 + %d EXT4 + %d EXT5, all adopted as-is, "
              "all POSITIVE_PREFIX); FRAME B: %d/8 sealed r353 "
              "anchors re-admitted %s; CHI3 %d/42 + CHI4 %d/42 "
              "built (kept-atom exclusions %s); nf-None chi3 "
              "%d/42, chi4 %d/42 (census)"
              % (len(packs_a), len(ext), len(ext2), len(ext3),
                 len(ext4), len(ext5), len(packs_b),
                 str(sorted(p["kz"] for p in packs_b)),
                 len(packs_c3), len(packs_c4),
                 str(excl) if excl else "none",
                 sum(1 for p in packs_c3 if p["nf"] is None),
                 sum(1 for p in packs_c4 if p["nf"] is None)))

    # ---------------- S3 eval + exact wards
    section("S3  EVAL + EXACT LIVE WARDS (quantization, "
            "multiplicity, dictionary, N2N3, T2-sum, M3-comp)")
    fams = (("FRAME_A", packs_a), ("FRAME_B", packs_b),
            ("CHI3", packs_c3), ("CHI4", packs_c4))
    all_kz = sorted(set(p["kz"] for _f, ps in fams for p in ps))
    grel_map = {kz: g for kz, g in zip(
        all_kz, EFA.grel_col(all_kz, core.G_ALL))}
    frecs = {}
    for fam, ps in fams:
        recs = []
        for p in ps:
            rc = DSW.rung_rec(p)
            rc["ev"] = eval_gap(rc)
            recs.append(rc)
        recs.sort(key=lambda r: (r["N"], r["kz"]))
        frecs[fam] = recs
    # eval cross-ward vs DMF.eval_k2 at w9 (bitwise)
    rc9 = frecs["FRAME_A"][0] if smoke else next(
        rc for rc in frecs["FRAME_A"] if rc["kz"] == 9)
    ev9 = rc9["ev"]
    evk9 = DMF.eval_k2(rc9)
    xw_ok = (ev9["m"] == evk9["m"]
             and ev9["rho2"] == evk9["rho2"]
             and ev9["mqs"]["qm"] == evk9["mqs"]["qm"]
             and ev9["pst"]["nsc_rel"] == evk9["pst"]["nsc_rel"]
             and ev9["hst"]["ngj"] == evk9["hst"]["ngj"])
    # ward accumulators over all live rows
    tb_bad = []
    qdev_w = 0.0
    mult_drop = []
    dict_w = 0.0
    fabid_w = 0.0
    k2ch_w = 0.0
    xdev_w = 0.0
    t2sum_w = 0.0
    comp_w = 0.0
    n2n3_bad = 0
    mono_bad = 0
    live = {}
    for fam in frecs:
        rows = []
        for rc in frecs[fam]:
            ev = rc["ev"]
            bar = (TB_WARD_BAR_B if fam == "FRAME_B"
                   else CHI_TB_BAR if fam.startswith("CHI")
                   else TB_WARD_BAR if rc["N"] <= DEEP_N
                   else max(TB_WARD_BAR_DEEP, TB_WARD_BAR_X345))
            if ev["tb_dev"] > bar:
                tb_bad.append((fam, rc["kz"], ev["tb_dev"]))
            if ev["degenerate"]:
                mult_drop.append((fam, rc["kz"], "degenerate"))
                continue
            if ev["mx_mult"] > MULT_CAP:
                mult_drop.append((fam, rc["kz"], "mult"))
                continue
            qdev_w = max(qdev_w, ev["gl"]["qdev"])
            if not ev["gl"]["mono"]:
                mono_bad += 1
            xdev_w = max(xdev_w, ev["x_dev"])
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            qm = ev["mqs"]["qm"]
            dic = ev["dic"]
            dict_w = max(dict_w, abs(dic["ymx"] / float(mloc) - qm)
                         / max(qm, 1e-300))
            fab = QGL.fab_of(float(mloc), qm, lgl)
            fabid_w = max(fabid_w, abs(fab * lgl - mloc * qm)
                          / max(mloc * qm, 1e-300))
            gz = grel_map[rc["kz"]]
            hst = ev["hst"]
            if hst["ngj"]:
                rhs = (hst["ngj"] / lgl) * (hst["hgn"] * gz)
                k2ch_w = max(k2ch_w, max(0.0, fab * gz - rhs)
                             / max(rhs, 1e-300))
            gc = gap_columns(ev)
            t2sum_w = max(t2sum_w,
                          max(0.0, gc["t2v"] - gc["t2bound"])
                          / max(gc["t2bound"], 1e-300))
            comp_rhs = (gc["maxprod"] ** 2) * gc["lg"] ** 2 \
                / float(mloc) ** 2 * gc["t2v"]
            comp_w = max(comp_w, max(0.0, gc["m3"] - comp_rhs)
                         / max(comp_rhs, 1e-300))
            if gc["n2"] + 1e-15 < gc["n3"]:
                n2n3_bad += 1
            row = dict(kz=rc["kz"], N=rc["N"], m=mloc, lg=lgl,
                       qm=qm, fab=fab, grel=gz, fabg=fab * gz,
                       gc=gc)
            rows.append(row)
        live[fam] = rows
    n_live = sum(len(live[f]) for f in live)
    brk_struct = (bool(tb_bad) or qdev_w > QUANT_BAR
                  or mono_bad > 0 or not xw_ok
                  or dict_w > DICT_BAR or fabid_w > FAB_ID_BAR
                  or k2ch_w > CHAIN_BAR or xdev_w > 1e-12
                  or t2sum_w > 0.0 or comp_w > 0.0
                  or n2n3_bad > 0 or not frb_ok or not chi_ok
                  or bool(mesh_bad) or not gaptoy_ok
                  or not packtoy_ok or not fr_ok or not meshtoy_ok
                  or n_live == 0)
    check("G30-exact-live-wards", not brk_struct,
          "on %d live rows (drops %s): eval cross-ward vs "
          "DMF.eval_k2 at w9 EXACT [%s]; theta-grid quantization "
          "worst %.1e (bar %.0e); centers monotone (%d bad); "
          "genealogy cover %.1e; FDD dictionary ymx/m == q_max "
          "%.1e; FAB identity %.1e; K2 chain one-sided %.1e; T2 "
          "dyadic summation one-sided %.1e; M3 composition "
          "one-sided %.1e; N2 >= N3 %d/%d; contribution ward %s"
          % (n_live, str(mult_drop) if mult_drop else "none",
             "OK" if xw_ok else "BROKEN", qdev_w, QUANT_BAR,
             mono_bad, xdev_w, dict_w, fabid_w, k2ch_w, t2sum_w,
             comp_w, n_live - n2n3_bad, n_live,
             "OK" if not tb_bad else "BROKEN %s" % str(tb_bad[:3])))

    # ---------------- S4 anchors (slim, bit-near)
    section("S4  LEG 0 -- ANCHORS (r353 / r355 / r357, slim set)")
    if smoke:
        check("G40-anchors", True, "SMOKE: skipped")
    else:
        rowsA = live["FRAME_A"]
        ck2x = max(r["fabg"] for r in rowsA)
        ck2x_kz = max(rowsA, key=lambda r: r["fabg"])["kz"]
        rowsB = live["FRAME_B"]
        fb_ok = all(
            abs(next(r["fab"] for r in rowsB if r["kz"] == kz)
                - R353_FB_TABLE[kz][0]) <= R353_FB_FAB_TOL
            and abs(next(r["grel"] for r in rowsB
                         if r["kz"] == kz)
                    - R353_FB_TABLE[kz][1]) <= R353_FB_GREL_TOL
            for kz in R353_FB_TABLE)
        fbk2 = max(r["fabg"] for r in rowsB)
        rows3 = live["CHI3"]
        rows4 = live["CHI4"]
        c3max = max(r["fabg"] for r in rows3)
        c3kz = max(rows3, key=lambda r: r["fabg"])["kz"]
        c4max = max(r["fabg"] for r in rows4)
        mainmax = max(r["fabg"] for r in rowsA
                      if r["N"] <= H_CAP)
        check("G40-anchors",
              abs(ck2x - R353_CK2X) <= R353_CK2X_TOL
              and ck2x_kz == R353_CK2X_KZ and fb_ok
              and abs(fbk2 - R353_FB_K2MAX) <= R353_FB_K2MAX_TOL
              and abs(c3max - R357_CHI3_MAX) <= R357_TOL
              and c3kz == R357_CHI3_MAX_KZ
              and abs(c4max - R357_CHI4_MAX) <= R357_TOL
              and abs(mainmax - R357_MAIN_MAX) <= R357_TOL,
              "C_K2X = %.2f at kz%d (rec %.2f at kz%d); frame-B "
              "8-row FAB/grel table within tol %s, K2 max %.2f "
              "(rec %.2f); chi3 max FABg %.2f at kz%d (rec %.2f "
              "at kz%d); chi4 max %.2f (rec %.2f); MAIN-42 max "
              "%.2f (rec %.2f) -- the r353/r355/r357 records "
              "reproduce through THIS channel"
              % (ck2x, ck2x_kz, R353_CK2X, R353_CK2X_KZ,
                 "OK" if fb_ok else "BROKEN", fbk2,
                 R353_FB_K2MAX, c3max, c3kz, R357_CHI3_MAX,
                 R357_CHI3_MAX_KZ, c4max, R357_CHI4_MAX, mainmax,
                 R357_MAIN_MAX))

    # ---------------- S5 Leg A: T1
    section("S5  LEG A -- T1: THE LOCALIZED PRODUCT AT THE "
            "PER-FAMILY FIRST-K FREEZE")
    t1_fams = []
    t1_txt = []
    if smoke:
        check("G50-t1", True, "SMOKE: skipped")
    else:
        for fam in ("FRAME_A", "FRAME_B", "CHI3", "CHI4"):
            rows = live[fam]
            ncal = N_CAL_FB if fam == "FRAME_B" else N_CAL_T1
            cal = rows[:ncal]
            test = rows[ncal:]
            ck = max(r["gc"]["maxprod"] for r in cal)
            viol = [(r["kz"], round(r["gc"]["maxprod"], 2))
                    for r in test
                    if r["gc"]["maxprod"] > ck + K2_EPS]
            tmax = max(r["gc"]["maxprod"] for r in test)
            tmax_kz = max(test,
                          key=lambda r: r["gc"]["maxprod"])["kz"]
            if viol:
                t1_fams.append(fam)
            t1_txt.append("%s C_K %.2f | test max %.2f @ kz%d | "
                          "viol %d/%d%s"
                          % (fam, ck, tmax, tmax_kz, len(viol),
                             len(test),
                             (" " + str(viol[:6])) if viol
                             else ""))
            live[fam + "_CK"] = ck
        for t in t1_txt:
            info("T1 " + t)
        gmax = max(r["gc"]["maxprod"] for f in
                   ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
                   for r in live[f])
        check("G50-t1", True,
              "T1 (m q_i/log m) g_i <= C_K(F) at the per-family "
              "first-K freeze (NO frame-A constant crosses a "
              "family): %s; violating families %s; the GLOBAL "
              "measured product ceiling over all %d rows: %.2f "
              "(census)"
              % ("; ".join(t1_txt),
                 str(t1_fams) if t1_fams else "NONE", n_live,
                 gmax))

    # ---------------- S6 Leg B: T2' + T2 + small-ball bands
    section("S6  LEG B -- T2'/T2: THE DYADIC GAP-MASS PACKING + "
            "THE SMALL-BALL BANDS")
    pack_fams = []
    if smoke:
        check("G60-pack-table", True, "SMOKE: skipped")
        check("G61-t2-census", True, "SMOKE: skipped")
        check("G62-smallball", True, "SMOKE: skipped")
    else:
        fam_order = ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
        info("THE T2' r-TABLE (per family: max_w S_r | rows with "
             "S_r > 0; sealed bar C 2^-2r (1+r)^A):")
        pack_viol = {f: [] for f in fam_order}
        for r in range(1, R_MAX + 1):
            cells = []
            for fam in fam_order:
                col = [row["gc"]["Sr"][r - 1] for row in live[fam]]
                mx = max(col)
                nz = sum(1 for v in col if v > 0.0)
                for row in live[fam]:
                    if row["gc"]["Sr"][r - 1] \
                            > pack_bar(r) + PACK_EPS:
                        pack_viol[fam].append((row["kz"], r))
                cells.append("%s %.5f|%d" % (fam[:2], mx, nz))
            info("  r %2d bar %.5f : %s"
                 % (r, pack_bar(r), "  ".join(cells)))
        pack_fams = [f for f in fam_order if pack_viol[f]]
        ming_all = min(row["gc"]["ming"] for f in fam_order
                       for row in live[f])
        check("G60-pack-table", True,
              "T2' at the SEALED bars (C %.1f, A %.1f): "
              "violations %s; min g over the whole round %.3f; "
              "the quadratic fall law is %s on all %d rows x %d "
              "dyadic levels"
              % (C_PACK, A_PACK,
                 str({f: pack_viol[f][:4] for f in fam_order
                      if pack_viol[f]}) if pack_fams else "0",
                 ming_all,
                 "a 0-violation census theorem" if not pack_fams
                 else "BROKEN on %s" % str(pack_fams), n_live,
                 R_MAX))
        t2cells = []
        cg_cens = 0.0
        for fam in fam_order:
            mx = max(row["gc"]["t2v"] for row in live[fam])
            cg = max(row["gc"]["t2v"] / row["lg"] ** A_PACK
                     for row in live[fam])
            cg_cens = max(cg_cens, cg)
            t2cells.append("%s max T2val %.2f (C_G %.3f)"
                           % (fam, mx, cg))
        check("G61-t2-census", True,
              "T2 census sum q_i/g_i^2: %s; C_G_cens = %.3f at "
              "A = %.1f (the dyadic summation T2' => T2 is warded "
              "EXACT one-sided on every row, G30)"
              % ("; ".join(t2cells), cg_cens, A_PACK))
        sb_viol = 0
        sb_bands = 0
        align_meds = {}
        for fam in fam_order:
            am = []
            for row in live[fam]:
                for s, bd in row["gc"]["bands"].items():
                    sb_bands += 1
                    am.append(bd["align_med"])
                    for r in range(1, R_MAX + 1):
                        if bd["sbr"][r - 1] > sb_bar(r) + PACK_EPS:
                            sb_viol += 1
            align_meds[fam] = float(np.median(am)) if am else 0.0
        for kz_s in STRESS_KZ:
            row = next((r for r in live["FRAME_A"]
                        if r["kz"] == kz_s), None)
            if row is None:
                continue
            info("STRESS kz%d (m %d, min g %.3f): band s | n | "
                 "SB_1 SB_2 SB_3 | align med"
                 % (kz_s, row["m"], row["gc"]["ming"]))
            for s in sorted(row["gc"]["bands"]):
                bd = row["gc"]["bands"][s]
                info("  s %2d | %4d | %.4f %.4f %.4f | %.3f"
                     % (s, bd["n"], bd["sbr"][0], bd["sbr"][1],
                        bd["sbr"][2], bd["align_med"]))
        check("G62-smallball", True,
              "SMALL-BALL (building block D, census): %d tested "
              "bands (>= %d members), %d band-level violations "
              "of SB_r <= C 2^-2r (1+r)^B; band alignment "
              "|x_i|/A1_i med per family %s vs the %.1f census "
              "floor -- the band comparability (C) carries in "
              "MASS form%s"
              % (sb_bands, BAND_MIN, sb_viol,
                 str({f: round(align_meds[f], 2)
                      for f in fam_order}), ALIGN_FLOOR,
                 "" if all(v >= ALIGN_FLOOR
                           for v in align_meds.values())
                 else ", NOT in signed-survival form (said "
                 "honestly)"))

    # ---------------- S7 Leg C typing + S8 Leg D composition
    section("S7/S8  LEG C + LEG D -- TYPING + THE COMPOSITION")
    if smoke:
        check("G70-typing", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        check("G70-typing", True,
              "PROOF-SKETCH TYPING: SATZ = fold multiplicity <= "
              "2 (0 drops beyond filter, warded), mesh identity "
              "+ grid quantization (%.1e), dyadic summation T2' "
              "=> T2 (one-sided %.1e), N2 >= N3, the M3 "
              "composition algebra (one-sided %.1e); DICTIONARY "
              "= FDD q_i (%.1e), band MASS comparability; "
              "CERTIFIED CENSUS = T2' at the sealed (%.1f, %.1f) "
              "bars [%s], the small-ball band form, the measured "
              "min-g floor; OPEN = the in-the-mean sieve (D) as "
              "a theorem AND the family-uniform T1 constant rule "
              "-- named in G71"
              % (qdev_w, t2sum_w, comp_w, dict_w, C_PACK, A_PACK,
                 "0 viol" if not pack_fams else "BROKEN"))
        ck_max = max(live[f + "_CK"] for f in
                     ("FRAME_A", "FRAME_B", "CHI3", "CHI4"))
        gmax = max(r["gc"]["maxprod"] for f in
                   ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
                   for r in live[f])
        ck_use = gmax  # the honest ceiling: measured, census
        m0 = solve_m0(lambda t: 2.0 * math.log(max(ck_use, 1e-300))
                      + math.log(max(cg_cens, 1e-300))
                      + A_PACK * math.log(t))
        n3_min = min(r["gc"]["n3"] for f in
                     ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
                     for r in live[f])
        check("G71-composition", True,
              "THE COMPOSITION (no global g_min anywhere): M_3 "
              "<= C_K^2 C_G (log m)^{A+2}/m^2 with the MEASURED "
              "ceilings C_K = %.2f (global product census; "
              "per-family freezes %.2f max) and C_G_cens = %.3f "
              "=> rho_2 <= C_K^2 C_G (log m)^%.0f => m_0* = %s "
              "(pure polylog) vs r351 10^%.1f / r353 10^%.1f / "
              "r306 census 10^%.1f; N_3 >= m/(C (log m)^%.1f), "
              "min measured N_3 %.1f; N_2 >= N_3 EXACT => "
              "Fejer/vdC => H5 => q_N < 1 stays the CONDITIONAL "
              "chain (typed, not claimed); THE NAMED SPECIALIST "
              "QUESTION: for the folded log p^k phases prove "
              "sum_{i in B, g_i <= t} a_i <= C t^2 (log m)^B "
              "sum_B a_i per dyadic source band (small-ball / "
              "large sieve in the mean; NO pointwise Baker "
              "bounds) + a family-uniform T1 constant rule"
              % (ck_use, ck_max, cg_cens, A_PACK + 2.0,
                 ("10^%.1f" % m0) if m0 is not None else "NONE",
                 M0_REFS[0], M0_REFS[1], M0_REFS[2],
                 (A_PACK + 2.0) / 2.0, n3_min))
        verdict_main = main_tree_358(leak, brk_struct,
                                     bool(pack_fams),
                                     bool(t1_fams))

    # ---------------- S9 Leg E: scrambles + twin
    section("S9  LEG E -- MATCHED SCRAMBLES (named precondition) "
            "+ TWIN")
    if smoke:
        check("G80-scrambles", True, "SMOKE: skipped")
        check("G81-twin", True, "SMOKE: skipped")
        scr_txt = "SMOKE"
    else:
        alpha9 = float(core.U_ALL[9])
        ka9 = core.atoms_in(alpha9)
        rng = np.random.default_rng(SCR_SEED)
        scr_worlds = []
        # frame-A w9 scramble (BH channel, r-convention seed)
        pA = BH.wpack(9, base_kw=dict(scramble_seed=SCR_SEED))
        scr_worlds.append(("FRAME_A_w9", pA))
        # frame-B kz80 scramble (r353 verbatim)
        alpha80 = float(core.U_ALL[80])
        ka80 = core.atoms_in(alpha80)
        uu_scr = np.sort(rng.uniform(0.0, 2.0 * alpha80,
                                     size=ka80))
        pBv = SFE.wpack_b(80, NU_B,
                          comb=(uu_scr, core.MU_ALL[:ka80].copy()))
        scr_worlds.append(("FRAME_B_kz80", pBv))
        # matched chi3 w9 scramble (r357 verbatim)
        u3, w3c, _nn, _ch = DMF.chi_window_comb(9, Q_CHI3)
        u_scr = np.sort(np.random.default_rng(SCR_SEED).uniform(
            0.0, 2.0 * alpha9, size=len(w3c)))
        try:
            pC = DMF.chi_wpack(9, 1.0, LPQ3, (u_scr, w3c))
        except Exception as exc:            # noqa: BLE001
            pC = dict(kz=9, N=0, nf="build-fail: %s" % exc,
                      complete=False)
        scr_worlds.append(("CHI3_w9", pC))
        scr_letters = []
        for lab, p in scr_worlds:
            p1_ok = (p.get("nf") is None and p.get("complete",
                                                   True))
            mult_ok = True
            quant_ok = True
            band_ok = True
            pack_ok = True
            if p.get("rows"):
                rc = DSW.rung_rec(p)
                ev = eval_gap(rc)
                if not ev["degenerate"]:
                    mult_ok = ev["mx_mult"] <= MULT_CAP
                    quant_ok = ev["gl"]["qdev"] <= QUANT_BAR
                    gc = gap_columns(ev)
                    ams = [bd["align_med"]
                           for bd in gc["bands"].values()]
                    band_ok = (min(ams) >= ALIGN_FLOOR
                               if ams else True)
                    pack_ok = all(
                        gc["Sr"][r - 1] <= pack_bar(r) + PACK_EPS
                        for r in range(1, R_MAX + 1))
            let = scr_letter(p1_ok, mult_ok, quant_ok, band_ok,
                             pack_ok)
            scr_letters.append("%s -> %s (nf %s)"
                               % (lab, let, str(p.get("nf"))))
        scr_txt = "; ".join(scr_letters)
        check("G80-scrambles", all("NO_BREAK" not in s
                                   for s in scr_letters),
              "MATCHED SCRAMBLES through all three construction "
              "channels, adjudicated by the SEALED precondition "
              "order (P1 admission > P2 mult > P3 quantization > "
              "P4 band align > P5 packing): %s -- the packing's "
              "binding source precondition is NAMED per channel"
              % scr_txt)
        # rational twin of the chi3 comb (r357 verbatim channel)
        gaps3 = MF.local_gaps(u3)
        _a, _M, _L, _Nw, D9 = V.window_shape(9)
        u3t, w3t, _d, _du = AKD.twin_rational(u3, w3c, gaps3, D9,
                                              TWIN_TOL)
        pk3 = DMF.chi_wpack(9, 1.0, LPQ3, (u3, w3c))
        pk3t = DMF.chi_wpack(9, 1.0, LPQ3, (u3t, w3t))
        rcT = DSW.rung_rec(pk3)
        rcTt = DSW.rung_rec(pk3t)
        evT = eval_gap(rcT)
        evTt = eval_gap(rcTt)
        gcT = gap_columns(evT)
        gcTt = gap_columns(evTt)
        devT = max(abs(gcT["maxprod"] - gcTt["maxprod"])
                   / max(gcT["maxprod"], 1e-300),
                   abs(gcT["t2v"] - gcTt["t2v"])
                   / max(gcT["t2v"], 1e-300))
        check("G81-twin", devT <= TWIN_BAR,
              "RATIONAL TWIN of the chi3 comb (tol %.0e) through "
              "the matched terminal channel at w9: T1 row-max + "
              "T2val devs %.1e (bar %.0e) -- the gap columns "
              "carry bit-near" % (TWIN_TOL, devT, TWIN_BAR))

    # ---------------- S10 verdict
    section("S10  VERDICT")
    check("G97-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed local gap coordinate g_i, the T1 "
          "per-family census, the T2' dyadic packing table at "
          "a-priori bars, the small-ball band census, the exact "
          "composition algebra and the named sieve question -- "
          "NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rows")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        flags = []
        if verdict_main in ("GAP_CARLESON_CERTIFIED",
                            "QUADRATIC_LAW_PARTIAL"):
            flags.append("SIEVE_CORE_OPEN")
        if verdict_main == "PACKING_FAILS":
            verdict_main += "(%s)" % ",".join(pack_fams)
        if verdict_main == "QUADRATIC_LAW_PARTIAL":
            verdict_main += "(T1@%s)" % str(t1_fams)
        flags.append("T1(%s)" % "; ".join(t1_txt))
        flags.append("PACK(%s viol, min g %.3f)"
                     % ("0" if not pack_fams else str(pack_fams),
                        ming_all))
        flags.append("SMALLBALL(%d bands, %d viol)"
                     % (sb_bands, sb_viol))
        flags.append("COMPOSITION(m_0* %s vs 10^%.1f/10^%.1f/"
                     "10^%.1f)"
                     % (("10^%.1f" % m0) if m0 is not None
                        else "NONE", M0_REFS[0], M0_REFS[1],
                        M0_REFS[2]))
        flags.append("SCRAMBLE(%s)" % scr_txt)
        flags.append("TWIN(%.1e)" % devT)
        flags.append("MUSTFAIL_LEDGER(e1-e5 + m6a/m6b)")
        verd = verdict_main + "".join(" + " + f for f in flags)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G98-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): quantization, "
          "multiplicity, mesh identity, dictionary, N2 >= N3, "
          "dyadic summation, M3 composition, Fractions toys, "
          "frame reproductions, purity audits (exact/AST-"
          "decided); MEASURED: every C_K, S_r, T2val, band mass "
          "and violation count (the finite 89 + 8 + 42 + 42 row "
          "surface); OPEN: the in-the-mean sieve, the family-"
          "uniform T1 rule, any cofinal law, the actual proof; "
          "NO RH claim"
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
