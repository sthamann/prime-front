#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mean_sieve_floor_probe --
PRIME.L2.MEAN_SIEVE.01 (round 361): THE MEAN SIEVE ON THE FOLDED
LOG-p^k PHASES -- the named theorem rest of the terminal lane
after r358, adjudicated FLOOR-FIRST.

CONTEXT (binding, from the sealed r358 record SPEC_SHA fb2d499f,
QUADRATIC_LAW_PARTIAL + SIEVE_CORE_OPEN).  T2' (the dyadic packing
sum_{g_i <= 2^-r} q_i <= 2^{-2r}(1+r)^2 at a-priori bars) is a
0-violation census theorem on all 181 rows of all four worlds
(frame A / frame B / chi3 / chi4), the whole small-gap mass lives
at r = 1, S_r == 0 for r >= 2, and THE FLOOR FINDING: the minimal
normalized local small gap of the entire round is 0.375 -- gaps
below 3/8 of the local median DO NOT EXIST on the admitted
surface, in any family, any arithmetic.  The named theorem rest is
the MEAN SIEVE: sum_{i in B, g_i <= t} a_i <= C t^2 (log m)^B
sum_B a_i per dyadic source band (small-ball in the mean on the
folded log p^k phases, NO Baker point bounds, r289/r331).  The
mesh quantization is exact (theta-grid 9.1e-13, fit-free; the mesh
identity h - NU u in (0, 3/2] is SATZ, r355); fold multiplicity <=
2 is exact; FDD q_i exact; band comparability carries in MASS form.

THE CENTRAL NEW QUESTION (adjudicated BEFORE everything else): IS
THE 0.375 FLOOR DERIVABLE FROM THE CONSTRUCTION ALGEBRA?  The
candidate chain, derived a priori from the r358 g_i definition
(read exactly: block centers = unweighted means of the DISTINCT
fold-group theta-grid positions per block; gap_i = one-sided min
distance to the adjacent centers in grid units; g_i = gap_i /
median{gap_k : |k - i| <= 5, k != i} -- EFA.grel_col verbatim):
  (SEP-SATZ, the algebraic half)  the fold-group positions are
    INTEGERS on the theta grid LL = 4 N_w - 2 (mesh identity =>
    quantization, warded exact); the level-2 blocks are
    theta-CONTIGUOUS with pairwise-DISJOINT integer supports
    (block_breaks intervals); hence for adjacent block centers,
    with n_i = #distinct grid integers of block i,
      c_{i+1} - c_i >= 1 + (n_i - 1)/2 + (n_{i+1} - 1)/2
                     = (n_i + n_{i+1})/2   (grid units, EXACT)
    -- a mean of n distinct integers below a cut sits at least
    (n-1)/2 below it.  Tested as an EXACT Fractions census on
    every adjacent pair of every live row (0 violations = the
    separation theorem holds on the surface; its preconditions --
    integrality, contiguity, disjointness -- are warded live).
  (MED-CAP, the named missing half)  the floor is a RATIO bound:
    g_i >= 3/8 needs an UPPER bound on the local median:
      med_i <= (8/3) sep_i,  sep_i = min adjacent (n_i + n_j)/2.
    The mesh algebra yields LOWER bounds only (integrality,
    separation) -- a ratio floor cannot close from below alone.
    MED-CAP is therefore the PRECISE additional assumption; it is
    tested as a sealed exact census on every atom.  If SEP-SATZ
    and MED-CAP both hold with 0 violations, the pointwise chain
      g_i = gap_i/med_i >= sep_i/med_i >= 3/8
    closes on every atom of the surface.
  (VALUE SET)  every g_i is an EXACT RATIONAL (integer positions
    => centers with denominator n_i => gaps and window medians in
    Q): the discrete value set is computed in Fractions on every
    row, printed exactly on the small w9 windows and for EVERY
    sub-half atom of the round; whether min g == 3/8 EXACTLY is a
    decidable bit -- the mesh-rationality of the floor.
FLOOR VERDICT SEMANTICS (sealed): FLOOR_THEOREM fires iff SEP-SATZ
holds exact AND MED-CAP has 0 violations AND the matched SCRAMBLE
floor is measurable and also >= 3/8 (the cap is construction-level
robust under arithmetic destruction) -- disclosed epistemics: the
chain is then pointwise-complete with the cap as a census identity
robust across arithmetics; a paper proof still needs the cap as a
lemma.  QUANTIZED_CENSUS(MED_CAP) iff the chain closes on the
surface (SEP + CAP 0-violation) but the scramble contrast is
missing or breaks -- the cap is the named Zusatzannahme.
QUANTIZED_CENSUS(SIEVE) iff the cap breaks somewhere but min g is
EXACTLY the mesh rational 3/8 (the quantization is real, the bound
is not derived -- the mean sieve is genuinely needed).
FLOOR_ACCIDENTAL iff the cap breaks and the minimum is not the
exact mesh rational.  FLOOR_ARITHMETIC is appended iff a measured
scramble floor drops below 3/8 (the floor needs the arithmetic
comb -- the sieve is genuinely needed).  SEP_SATZ_FAILS is the
loudest possible negative (the algebraic half itself breaks).

THE LEGS:
  LEG 0 -- ANCHORS bit-near (the r358 records through the SAME
    reused channel): row counts 89/8/42/42; min g 0.375; max S_1
    per family (0.0170 / 0.0052 / 0.0238 / 0.0439); the T1
    per-family freezes (2.45 / 4.91 / 1.52 / 1.62) and test maxima
    (15.93 / 23.70 / 3.91 / 3.09); the global product ceiling
    23.70; C_K2X 11.87 at kz111; stress min g kz51/kz111
    (0.533 / 0.571); band count 1033; the r355 mesh identity
    re-warded on the live pools; the NU = 4 and chi trivial frame
    reproductions (r353/r357).
  LEG A -- THE FLOOR DERIVATION (the core, above): the exact
    Fractions ledger (integer grid positions, exact centers,
    exact side gaps, exact window medians, exact g column) is
    cross-warded against the r358 float ledger (centers/gaps/g
    <= 1e-9 rel, the float ledger re-derivation bitwise-equal,
    integer collisions == 0, rounding dev <= QUANT_BAR, group
    counts matching); SEP-SATZ exact census on every adjacent
    pair; MED-CAP exact census on every atom; the exact value
    set + the sub-half table + the exact-minimum bit + the
    algebraic floor min_i sep_i/med_i.
  LEG B -- THE MEAN SIEVE IN OUR DRESS (census + the specialist
    steckbrief): the sieve statement on the folded phases, tested
    at the SEALED CONTINUOUS t-GRID t = j/32 (j = 1..16, i.e.
    t in (0, 1/2], a-priori) against bar(t) = C_SB t^2
    (1 + log2(1/t))^{B_SB} (C_SB = 1.0, B_SB = 2.0 -- at dyadic t
    the bar EQUALS the r358 pack_bar, warded exact): row-level
    S(t) = sum_{g_i <= t} q_i on all live rows AND band-level
    SB(t) = sum_{i in B, g_i <= t} A1_i / sum_B A1_i on every
    dyadic source band (>= 5 members, the r358 banding rule
    verbatim, band count cross-warded against the r358 channel)
    with EXACT g comparisons; the r358 dyadic band census (sbr,
    r = 1..12) re-run as continuity; the mean over the window
    family per family printed (the in-the-mean form).
    THE STECKBRIEF (which classical theorem carries which part):
    (i) WELL-SPACEDNESS input of the Montgomery-Vaughan large
    sieve = exactly our SEP-SATZ (block centers are
    (n_i+n_j)/2-separated on the integer mesh -- THIS round's
    algebraic half); (ii) the mass-form band bound from the large
    sieve needs the band MASS comparability = the r358 dictionary
    block (carries); (iii) Erdos-Turan discrepancy / second-moment
    Weyl sums on alpha log p carry the MEAN over the window
    family, not the per-window statement; (iv) THE MISSING PIECE,
    named precisely: the local-median regularity (MED-CAP) --
    both open parts of the sieve reduce to it on this surface.
  LEG C -- THE COMPOSITION (the direct chain of the contract):
    IF the floor holds (census or theorem), T2' TRIVIALIZES:
    S_r == 0 for r >= 2 is forced (2^{-2} < 3/8), S_1 <= 1 <=
    bar(1) is trivial -- the packing becomes SATZ modulo MED-CAP,
    and the M_3 chain needs NO T2/C_G layer: q_i <= C_K log m /
    (m g_i) <= (8/3) C_K log m / m UNIFORM on every atom
    (pointwise T1 at the measured ceiling), hence
      M_3 <= (8/3)^2 C_K^2 (log m)^2 / m^2
    -- C_G and TWO log powers drop vs the r358 Carleson route.
    Warded exact one-sided per row: q_max m g_min <= maxprod
    log m; M_3 <= q_max^2 (sum q = 1).  The new m_0* is solved
    pure-polylog (r351 solve_m0 body verbatim, rhs constant in t)
    for BOTH constants: the measured global census ceiling C_K
    (honest: census, not a rule) and the per-family first-K
    freeze max (honest: the rule r358 showed BROKEN -- the
    conditional number IF the named T1 constant rule existed);
    printed against 10^23.5 / 10^18.9 / 10^20.5 / 10^13.5.
    C_K STILL ENTERS SQUARED -- the floor removes the C_G
    (log m)^2 layer, it does NOT remove the T1 dependence: typed.
  LEG D -- WORLDS + SCRAMBLE FLOOR + TWIN: the floor/value-set
    analysis runs on all four worlds (per-family exact minima
    printed); the three matched SCRAMBLE channels (r358 S9
    verbatim: frame-A w9 seed 1 via BH.wpack, frame-B kz80 seed 1
    via SFE.wpack_b, matched chi3 w9 seed 1 via DMF) are
    adjudicated by the SEALED precondition order (LGC.scr_letter
    verbatim) AND their gap floors are MEASURED where a gap
    column exists (min g float; quantization deviation printed
    per channel -- a grid-quantized scramble would mark the
    quantization as CONSTRUCTION, not arithmetic); the rational
    twin of the chi3 comb (AKD.twin_rational 1e-8, r357/r358
    verbatim) must carry maxprod + T2val + min g bit-near
    (devs <= TWIN_BAR).

LEG E MUST-FAILS (>= 5 mutants + 2 scope mutants):
(f1) WRONG MESH UNIT: mutant_theta_wrong_mesh uses LL = 4 N_w
  (not 4 N_w - 2) -- on the sealed by-hand pin (N = 9, x =
  cos(2 pi/34)) it returns t = 18/17 (dev 1/17 = 0.0588 >>
  QUANT_BAR) where the true unit gives t = 1 exactly -- CAUGHT
  exact.
(f2) FLOOR READ BACK FROM THE g DATA (circular): mutant_floor_
  from_data returns min(column) (consumes rho) -- AST-FLAGGED and
  on the sealed r358 gap toy column (2.0, 0.5, 0.4, 3.0, 1.5)
  returns 0.4 != the sealed candidate 3/8 -- protocol-CAUGHT
  twice (a data minimum is not a derivation).
(f3) SIEVE BARS AFTER SIGHT: mutant_sieve_bar_posthoc sets C_SB
  at the seen mass column (consumes rho) -- AST-FLAGGED and on
  the sealed toy (S = 0.1 at t = 1/16, B = 2) returns 1.024 !=
  the sealed C_SB 1.0 -- protocol-CAUGHT twice.
(f4) BAND CLASSES AFTER SIGHT: mutant_bands_posthoc splits bands
  at the seen mass median instead of the sealed dyadic log2 rule
  (consumes rho) -- AST-FLAGGED and on the sealed toy a1 =
  (8, 7, 1) returns classes (0, 0, 1) != the sealed dyadic
  (0, 0, 3) -- protocol-CAUGHT twice.
(f5) MEDIAN WITH THE WRONG WINDOW: mutant_median_window applies
  w = 1 instead of the sealed W_LOC -- on the sealed r358 gap toy
  (gaps (2, 1, 1, 3, 3), sealed w = 2 pin (2.0, 0.5, 0.4, 3.0,
  1.5)) it returns (2.0, 2/3, 0.5, 1.5, 1.0) -- CAUGHT exact at
  four of five entries.
(m6a/m6b) WORLD-BLINDNESS BREAK (r355/r358 verbatim): builders
  consuming the withheld terminal drive key / the branch label
  are both FLAGGED by the AST scope audit.

SEALED VERDICTS (main letter: exactly one fires, total order;
flags appended with '+', combinations allowed; the contract enum
FLOOR_THEOREM / QUANTIZED_CENSUS(assumption) / SIEVE_PARTIAL /
FLOOR_ARITHMETIC / TARGET_LEAK is extended by the house exactness
guard LAW_STATE_NOT_EXACT and the loud negative SEP_SATZ_FAILS,
disclosed):
  TARGET_LEAK  iff any firewall/scope/fragment/literal audit hit
    on the module-own builders;
  LAW_STATE_NOT_EXACT(named)  iff an exact ward breaks on a live
    world (quantization, rounding, integer collision, Fractions
    cross-ward, ledger re-derivation, group counts, sum q, chain
    algebra, bar identity, frame reproductions, mesh identity,
    toys);
  SEP_SATZ_FAILS(loci)  iff the exact separation census has >= 1
    violation -- the algebraic half itself breaks;
  FLOOR_THEOREM  iff SEP-SATZ 0-viol AND MED-CAP 0-viol AND the
    scramble floor is measurable and >= 3/8 (semantics above);
  QUANTIZED_CENSUS(MED_CAP)  iff SEP + CAP close on the surface
    but the scramble contrast is missing or breaks;
  QUANTIZED_CENSUS(SIEVE)  iff the cap breaks but min g == 3/8
    EXACTLY as a mesh rational;
  FLOOR_ACCIDENTAL  otherwise.
  APPENDED ALWAYS: VALSET(exact minimum + exactness bit +
    sub-half census) + SEP_SATZ(census) + MED_CAP(census + worst
    ratio + algebraic floor) + SIEVE_CENSUS_HOLDS/BREAKS(t-grid
    rows + bands + dyadic continuity + mean headroom) +
    SIEVE_PARTIAL(the steckbrief import: MV large-sieve spacing =
    SEP-SATZ; missing = MED-CAP regularity) + DIRECT_CHAIN(m_0*
    census + rule-conditional vs 23.5/18.9/20.5/13.5) +
    [SCR_FLOOR_HOLDS / FLOOR_ARITHMETIC / SCR_FLOOR_UNMEASURED] +
    SCRAMBLE(named precondition + qdev + min g per channel) +
    TWIN(devs) + MUSTFAIL_LEDGER.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r358
LGC.{eval_gap, gap_columns, gap_ledger, theta_col, g_norm,
pack_bar, sb_bar, scr_letter, solve_m0, audit sets, the four-
world construction constants} (fb2d499f); r355 KSF.mesh_h +
constants (1f14bd93); r357 DMF.{chi_window_comb, chi_wpack,
chi_window_data, LPQ3, LPQ4} (4bf1a94b); r353 SFE.{wpack_b,
window_data_b, frameb_pool} (bd89e331); r329 EFA.grel_col +
GAP_W; r330 DSW.rung_rec; r269 PBB + r298 WBT (the eval position
head, verbatim lines); r244 BH; r243 PB; r289 AKD.twin_rational;
r276 MF.local_gaps; r351 QGL.fab_of; v881 PIK; v563 core
READ-ONLY.  NEW module-own (source-pure, AST-audited):
row_positions (the eval_gap position head, gate-side
re-derivation warded bitwise against the r358 ledger),
frac_center_ledger, frac_grel, sep_col, sieve_bar,
floor_tree_361, scr_floor_note.  q columns, S(t), bands, medians,
caps, seps and every census on them are TARGET-SIDE DIAGNOSTICS
computed in the gate section (r321..r358 convention, disclosed)
-- the module-own builders consume atom positions, block ids,
counts, window depth and SEALED thresholds only.

INDEX FIREWALL (binding, r238-r358 discipline): w = window (kz),
N_w = builder depth, m = block count; ground truth (records, the
frozen r358 anchor literals, the floor candidate 3/8) enters
GATES and census tables only, never a builder (AST scope audit;
withheld identifiers rho / t_term / g_branch); no zero/prime
oracles anywhere (AST firewall); no fit primitives (fragment
audit; NO slopes fitted -- the bars are a-priori, the medians are
medians, the caps are exact rationals).  Budget <= 1800 s.

SEALED CONSTANTS (everything not listed is imported verbatim via
LGC): FLOOR_CAND = 3/8 EXACT (the r358 record floor as a rational
candidate -- gate-side only; the round's question is precisely
whether it is derivable, so the candidate IS the object,
disclosed); CAP_FAC = 8/3 EXACT (the reciprocal -- MED-CAP is by
construction the weakest per-atom cap that reproduces the
candidate through SEP-SATZ, a NAMED assumption, not a fitted
constant); T_GRID = (j/32 : j = 1..16) EXACT (a-priori continuous
refinement of the r358 dyadic levels r = 1..5 on (0, 1/2];
dyadic consistency bar(2^-r) == pack_bar(r) warded exact); C_SB =
LGC.C_SB = 1.0; B_SB = LGC.B_SB = 2.0; W_LOC = EFA.GAP_W = 5;
QUANT_BAR = LGC 1e-6; FRAC_XW_BAR 1e-9 (float/exact cross-ward);
CHAIN_EPS 1e-12; PACK_EPS = LGC 1e-12; BAND_MIN = LGC 5;
S_BAND_MAX = LGC 20; N_CAL_T1 = LGC 5; N_CAL_FB = LGC 2; R_MAX =
LGC 12; TWIN_BAR 1e-3; TWIN_TOL 1e-8; SCR_SEED 1 (r-convention);
STRESS_KZ = LGC (51, 111); RUNTIME_BAR 1800 s; anchor records
(gate-side literals, r358 record): R358_ROWS (89, 8, 42, 42)
EXACT; R358_MING 0.375 tol 1e-6; R358_S1MAX (0.0170, 0.0052,
0.0238, 0.0439) tol 1.5e-3; R358_T1_CK (2.45, 4.91, 1.52, 1.62)
tol 0.02; R358_T1_TMAX (15.93, 23.70, 3.91, 3.09) tol 0.02;
R358_CEIL 23.70 tol 0.02; R358_STRESS_MING (0.533, 0.571) tol
2e-3; R358_BANDS 1033 EXACT; C_K2X = LGC.R353_CK2X 11.87 tol
0.02 at kz111; M0_REFS_361 (23.5, 18.9, 20.5, 13.5);
import-integrity prefixes LGC fb2d499f / KSF 1f14bd93 / DMF
4bf1a94b / SFE bd89e331; R361_TABLE_LITERALS =
LGC.R358_TABLE_LITERALS UNION {23.7, 15.93} (collision-prone
small values 0.375, 2.45, 4.91, 1.52, 1.62, 3.91, 3.09, 0.533,
0.571 and the S_1 maxima curated OUT, r337..r358 convention,
disclosed); smoke = toys + trees + mutants + scope/purity audits
+ the four w9 worlds (frame A / frame B / chi3 / chi4) with full
eval, the exact Fractions ledger cross-wards, SEP-SATZ + MED-CAP
+ value set + sieve census AT w9, the NU = 4 and chi trivial
frame reproductions and the mesh-pool ward; ladders, anchors,
deep censuses, composition, scrambles, twin and adjudication
skipped.

DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe's sealed
adjudication): every anchor band is an r353..r358 RECORD number
adopted as-is; the SEP-SATZ chain is DERIVED above a priori from
the sealed r358 definitions (distinct-integer means on disjoint
contiguous supports); ONE SCOPING PASS (machinery validation at
w9 only, r353..r358 precedent, numbers disclosed): frame-A w9
m = 35 with 7 distinct exact g values {7/8, 1, 16/15, 9/8, 5/4,
11/8, 3/2}; frame-B w9 m = 17 (min 5/8), chi3 w9 m = 39 / chi4
w9 m = 38 (minima 5/7); SEP-SATZ 125/125 adjacent pairs clean
over the four w9 worlds, MED-CAP 0/129 atoms (worst ratio 0.600
at frame-B w9, algebraic floor 5/8 at w9), integer collisions 0,
rounding dev 5.7e-14, exact/float cross-ward 7.2e-15,
float-ledger re-derivation bitwise, 12 bands, S(t) == 0 on the
whole w9 t-grid for all four worlds (the shallow anchor world
has NO sub-half mass -- every deep column, the whole floor
adjudication, every deep band census and every composed number
are GENUINELY OPEN); timing: the w9 smoke pass 0.6 s, the r358
record full pass 711.3 s (adopted as the deep budget estimate).  The sealed toys are computed BY HAND: frac
ledger toy blocks {0} / {2, 3} / {6} on the N = 9 grid ->
centers (0, 5/2, 6), counts (1, 2, 1), sides (5/2, 7/2), gaps
(5/2, 5/2, 7/2), seps (3/2, 3/2) -> SEP-SATZ holds, frac_grel
w = 1 g = (1, 5/6, 7/5), MED-CAP holds (worst med 3 <= 4 =
(8/3)(3/2)); cap-fail toy centers (0, 1, 10) counts (1, 1, 1) ->
gaps (1, 1, 9), g_1 = 1/5 < 3/8, med_1 = 5 > 8/3 -> exactly one
CAP violation at index 1 CAUGHT (the cap census bites on free
positions); sieve toy q = (0.1, 0.9), g = (1/16, 1) -> exactly
one violation on the t-grid at t = 1/16 (S = 0.1 > bar =
25/256), all other t clean; direct chain Fractions toy q =
(1/2, 1/4, 1/4), g = (1/2, 1, 1), m = 3, lg surrogate 1:
maxprod = 3/4, q_max m g_min = 3/4 <= 3/4 EXACT (equality),
M_3 = 5/32 <= q_max^2 = 1/4 EXACT; bar identity sieve_bar(2^-r)
== pack_bar(r) EXACT r = 1..12; mesh toy (r355 verbatim) h 21
dev 1.0 in (0, 3/2]; f1 pin 18/17 (dev 1/17) vs 1; f2 pin 0.4
vs 3/8; f3 pin 1.024 vs 1.0; f4 pin (0, 0, 1) vs (0, 0, 3); f5
pin (2.0, 2/3, 0.5, 1.5, 1.0) vs (2.0, 0.5, 0.4, 3.0, 1.5); the
seven main-tree branches, the three scramble-floor notes and the
sealed scr_letter order EXACT.  FLOOR_CAND, CAP_FAC, T_GRID,
FRAC_XW_BAR, CHAIN_EPS and all anchor tolerances are fixed
BEFORE any deep evaluation; the letters are symmetric and total
by CONTRACT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: R360 (L* saturation) and R362 (L-dagger moonshot)
run in parallel -- own files only; git pull before the strictly
additive rh-sync.  Two-commit freeze protocol (r329 convention):
spec committed pre-freeze, record tables the only post-freeze
edit, committed again.

Honesty before beauty: the quantization, the integer ledger, the
Fractions cross-wards, the separation preconditions, the chain
algebra, the bar identity, the frame reproductions, the mesh
identity and the purity audits are EXACT (Fractions/AST-decided);
SEP-SATZ and MED-CAP are censuses on the finite 89 + 8 + 42 + 42
row surface -- a 0-violation census fixes a CENSUS THEOREM, not a
cofinal law; FLOOR_THEOREM here means the pointwise chain closes
on the surface with a scramble-robust cap and is SAID SO; the
mean sieve as open mathematics stays open unless the floor
verdict removes it below 3/8; g_i is a construction-local
coordinate, said out loud; r243..r359 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA 0dafa3b962e337b3,
pre-freeze commit 7f17e3cf; protocol: smoke pass = 21/21 (0.6 s,
run twice pre-commit, byte-identical up to the WALL line,
disclosed in the commit message); calibration pass 1 = FIRST
full evaluation = 21/21, wall 655.6 s, NO amendment -- no bar,
cap, grid, rule or verdict rule moved at any point; record
run1/run2 after this insertion, byte-identical up to WALL):
MAIN VERDICT: FLOOR_THEOREM + VALSET(min g 3/8 EXACT, 5
sub-half atoms) + SEP_SATZ(0/32547 pairs) + MED_CAP(0/32728
atoms, worst ratio 1.000 -- SATURATED at the floor atom) +
SIEVE_CENSUS_HOLDS(rows 0, band cells 0, dyadic 0) +
SIEVE_PARTIAL(MV spacing = SEP-SATZ; missing = MED-CAP
regularity) + DIRECT_CHAIN(m_0* 10^16.1 census / 10^10.0
rule-conditional) + SCR_FLOOR_HOLDS + SCRAMBLE(P1_ADMISSION x3,
all grid-quantized, all floors >= 3/8) + TWIN(1.0e-07) +
MUSTFAIL_LEDGER.
THE HEADLINE FINDINGS:
(1) THE 3/8 FLOOR IS A THEOREM-GRADE CHAIN ON THE SURFACE, AND
THE CAP IS EXACTLY SATURATED: min g over all 181 rows is EXACTLY
the mesh rational 3/8 (Fractions bit) at CHI4 kz53 (two atoms:
gap = 3/2 grid units, window median = 4, n_i in {1, 2}, sep =
3/2) -- and the two-step chain g_i >= sep_i/med_i >= 3/8 closes
POINTWISE on ALL 32728 atoms: SEP-SATZ side d_i >= (n_i +
n_{i+1})/2 has 0/32547 violations (EXACT Fractions;
preconditions live: integrality 9.1e-13, integer collisions 0,
contiguity clean), and MED-CAP med_i <= (8/3) sep_i has 0/32728
violations with worst ratio EXACTLY 1.000 AT the floor atom
(med = 4 == (8/3)(3/2)): the constant 8/3 is TIGHT -- the floor
atom saturates the cap, and the algebraic floor min sep_i/med_i
equals 3/8 exactly.  The r358 floor is NOT accidental and NOT
merely empirical: below 3/8 there is nothing BECAUSE the local
median never exceeds 8/3 times the separation bound.  T2'
TRIVIALIZES modulo MED-CAP: S_r == 0 for r >= 2 is FORCED.
(2) THE SCRAMBLE CONTRAST IS MEASURABLE AND THE FLOOR SURVIVES
ARITHMETIC DESTRUCTION: all three matched channels break at P1
= POSITIVE_PREFIX admission as sealed (nf 21/3/37 -- the
r353..r358 records reproduced), but their partial builds carry
full gap columns: min g 0.778 (frame-A w9) / 0.421 (frame-B
kz80) / 0.750 (chi3 w9), ALL >= 3/8 -- and ALL THREE scrambled
worlds are STILL grid-quantized (qdev 5.7e-14 / 4.5e-13 /
5.7e-14): the theta-grid quantization and the floor are
CONSTRUCTION algebra (the fold machinery), not arithmetic of
the log p^k comb -- the FLOOR_THEOREM criterion fires.
DISCLOSED EPISTEMICS: theorem-grade = the pointwise chain
closes on the surface with the cap saturated and
scramble-robust; the paper lemma MED-CAP (why the 5-window
median of block gaps never exceeds (8/3)(n_i+n_j)/2) is the one
remaining formal step, now with a sharp, tight constant.
(3) THE VALUE SET IS SMALL-DENOMINATOR MESH-RATIONAL: all 181
rows are all-rational; only 5 sub-half atoms exist in the whole
round -- CHI4 kz53 3/8 (x2, q 3.6e-3/1.0e-2), CHI3 kz20 5/12
(q 2.4e-2), FRAME_A kz25/kz55 5/11 (q 1.4e-2/3.8e-3); frame-B
minimum 1/2; w9 value sets printed exactly in the smoke stage
(7/6/7/7 distinct values, denominators up to 15).
(4) THE SIEVE CENSUS HOLDS EVERYWHERE ON THE CONTINUOUS GRID:
0 violations on 181 rows x 16 t AND 1033 bands x 16 t (16528
band cells; r358 dyadic continuity 0/12396); the per-family
MEAN small-ball mass has headroom max_t mean S(t)/bar(t) =
0.0014 -- the in-the-mean form is satisfied with three decades
of headroom; the steckbrief reduces BOTH open sieve parts to
MED-CAP (the MV large-sieve spacing input IS SEP-SATZ).
(5) THE DIRECT CHAIN PAYS 7.4 DECADES: with the floor, M_3 <=
(8/3)^2 C_K^2 (log m)^2/m^2 (C_G and two log powers DROP):
m_0* = 10^16.1 at the measured census ceiling C_K = 23.70 (vs
the r358 Carleson 10^23.5) and 10^10.0 IF the family-uniform
T1 rule existed at the freeze max 4.91 -- BELOW the r306 census
10^13.5; C_K still enters squared: the T1 constant rule is now
THE single remaining quantitative rest of the terminal lane.
ANCHORS bit-near: rows 89/8/42/42; min g 0.3750; S_1 maxima
0.0170/0.0052/0.0238/0.0439; T1 freezes 2.45/4.91/1.52/1.62
with test maxima 15.93/23.70/3.91/3.09; ceiling 23.70; C_K2X
11.87 at kz111; stress kz51/kz111 min g 0.533/0.571; bands
1033/1033.  Exact wards: quantization 9.1e-13 (bar 1e-6),
collisions 0, exact/float cross 4.9e-13 (bar 1e-9), float
ledger re-derivation bitwise 181/181, sum q 4.4e-16, chain
algebra 0.0/0.0 one-sided, bar identity 0.0, twin 1.0e-07.
Must-fails: f1 CAUGHT exact (pin 18/17, dev 0.0588) / f2
protocol-CAUGHT twice (AST rho@699 + pin 0.4 vs 3/8) / f3
protocol-CAUGHT twice (AST rho@706 + pin 1.024 vs 1.0) / f4
protocol-CAUGHT twice (AST rho@716 + pin (0,0,1) vs (0,0,3)) /
f5 CAUGHT exact (4/5 entries differ) + m6a/m6b FLAGGED
(t_term@731 / g_branch@738).  Runtime 655.6 s calibration /
record run1/run2 byte-identical up to WALL / 0.6 s smoke.
AMENDMENTS AFTER FREEZE: NONE except this record-table
insertion.

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
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import qmax_growth_law_probe as QGL            # noqa: E402 r351
import second_family_erosion_probe as SFE      # noqa: E402 r353
import k2_source_formula_probe as KSF          # noqa: E402 r355
import dirichlet_secondworld_probe as DSW      # noqa: E402 r330
import dirichlet_matched_frame_probe as DMF    # noqa: E402 r357
import local_gap_carleson_probe as LGC         # noqa: E402 r358
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import window_border_transfer_probe as WBT     # noqa: E402 r298
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import verify_lstar_instance as V              # noqa: E402 document

# ---------------- imported constants (verbatim via LGC/EFA)
W_LOC = EFA.GAP_W
QUANT_BAR = LGC.QUANT_BAR
PACK_EPS = LGC.PACK_EPS
C_SB = LGC.C_SB
B_SB = LGC.B_SB
BAND_MIN = LGC.BAND_MIN
S_BAND_MAX = LGC.S_BAND_MAX
N_CAL_T1 = LGC.N_CAL_T1
N_CAL_FB = LGC.N_CAL_FB
R_MAX = LGC.R_MAX
TWIN_BAR = LGC.TWIN_BAR
TWIN_TOL = LGC.TWIN_TOL
SCR_SEED = LGC.SCR_SEED
STRESS_KZ = LGC.STRESS_KZ
MULT_CAP = LGC.MULT_CAP
NU_A = LGC.NU_A
NU_B = LGC.NU_B
FRAMEB_KZ = LGC.FRAMEB_KZ
MESH_DEV_HI = LGC.MESH_DEV_HI
LPQ3 = LGC.LPQ3
LPQ4 = LGC.LPQ4
Q_CHI3 = LGC.Q_CHI3
Q_CHI4 = LGC.Q_CHI4
TOY_BAR = LGC.TOY_BAR

# ---------------- NEW sealed constants of this round (spec above)
FLOOR_CAND = Fr(3, 8)
CAP_FAC = Fr(8, 3)
T_GRID = tuple(Fr(j, 32) for j in range(1, 17))
FRAC_XW_BAR = 1.0e-9
CHAIN_EPS = 1.0e-12
RUNTIME_BAR = 1800.0
# anchor records (gate-side literals, the r358 record)
R358_ROWS = (89, 8, 42, 42)
R358_MING = 0.375
R358_MING_TOL = 1.0e-6
R358_S1MAX = (0.0170, 0.0052, 0.0238, 0.0439)
R358_S1MAX_TOL = 1.5e-3
R358_T1_CK = (2.45, 4.91, 1.52, 1.62)
R358_T1_TMAX = (15.93, 23.70, 3.91, 3.09)
R358_T1_TOL = 0.02
R358_CEIL = 23.70
R358_CEIL_TOL = 0.02
R358_STRESS_MING = (0.533, 0.571)
R358_STRESS_TOL = 2.0e-3
R358_BANDS = 1033
M0_REFS_361 = (23.5, 18.9, 20.5, 13.5)
# import-integrity SHA prefixes (sealed)
LGC_SHA_PREFIX = "fb2d499f"
KSF_SHA_PREFIX = "1f14bd93"
DMF_SHA_PREFIX = "4bf1a94b"
SFE_SHA_PREFIX = "bd89e331"

R361_TABLE_LITERALS = frozenset(LGC.R358_TABLE_LITERALS
                                | {23.7, 15.93})

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
    return (not bad), ("NO zero/prime oracles; the exact ledger "
                       "builders consume atom positions + block ids "
                       "+ counts + window depth + sealed thresholds "
                       "ONLY; the r358 records and the 3/8 candidate "
                       "enter gates and census tables only"
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


SCOPE_FORBIDDEN_361 = {"rho", "t" + "_term", "g" + "_branch",
                       "fabg" + "_true"}


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
                            in R361_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders (source-pure, AST-audited):
# ---------------- consume atom POSITIONS, BLOCK IDS, COUNTS,
# ---------------- window DEPTH and SEALED thresholds only.  q
# ---------------- columns, S(t), bands, medians, caps, seps and
# ---------------- every census on them are TARGET-SIDE DIAGNOSTICS
# ---------------- computed in the gate section (disclosed).
def row_positions(rc):
    """the eval_gap position head (r358 verbatim lines, gate-side
    re-derivation): edge mask, runs, level-2 blocks, the combined
    comb + window position/block columns.  Returns (pos_all,
    blk_all, m).  Consumes the rung record only; warded BITWISE
    against LGC.eval_gap's own ledger downstream."""
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    cb = cts[~ed]
    xb = bxs[~ed]
    runs = PBB.runs_split(cb)
    brk, m, jb = WBT.block_breaks(xb, runs)
    edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], DSW.EDGE_F)
    xw = rc["xu"][~edw]
    jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
    pos_all = np.concatenate([xb, xw])
    blk_all = np.concatenate([jb, jw]).astype(int)
    return pos_all, blk_all, m


def frac_center_ledger(pos, blk, m, n_w):
    """THE EXACT LEDGER: the r358 gap_ledger dedup (lexsort on
    (block, position), values NOT consumed) -> theta-grid INTEGER
    positions (rounded, deviation returned) -> EXACT Fraction
    block centers (sum/count), sorted -> exact adjacent side
    differences d_i and per-block one-sided min gaps.  Returns
    exact centers, gaps, sides, per-block group counts and
    distinct-integer counts (theta order), the integer-collision
    count and the worst rounding deviation.  Consumes positions +
    block ids + depth only."""
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
    tg = LGC.theta_col(gpos, n_w)
    ti = np.round(tg).astype(np.int64)
    rdev = float(np.max(np.abs(tg - ti))) if len(tg) else 0.0
    sums = [0] * m
    cnts = [0] * m
    seen = [set() for _ in range(m)]
    coll = 0
    for b, t in zip(gblk.tolist(), ti.tolist()):
        if t in seen[b]:
            coll += 1
        seen[b].add(t)
        sums[b] += t
        cnts[b] += 1
    cent = [Fr(sums[b], cnts[b]) if cnts[b] else Fr(0)
            for b in range(m)]
    oc = sorted(range(m), key=lambda b: (cent[b], b))
    cs = [cent[b] for b in oc]
    cn = [cnts[b] for b in oc]
    nd = [len(seen[b]) for b in oc]
    d = [cs[i + 1] - cs[i] for i in range(m - 1)]
    if m >= 2:
        gaps = [d[0]] + [min(d[i - 1], d[i])
                         for i in range(1, m - 1)] + [d[-1]]
    else:
        gaps = [Fr(1)] * m
    return dict(cent=cs, gaps=gaps, sides=d, cnt=cn, ndist=nd,
                coll=coll, rdev=rdev, ng=int(len(gpos)))


def frac_grel(gaps, w):
    """the EXACT grel normalization (EFA.grel_col mirrored in
    Fractions, w-window, median = midpoint of the two middle
    values at even counts): returns (g_i, med_i) exact per entry.
    Consumes the passed gap column only."""
    m = len(gaps)
    out = []
    for i in range(m):
        lo = max(0, i - w)
        hi = min(m, i + w + 1)
        nb = sorted(gaps[j] for j in range(lo, hi) if j != i)
        k = len(nb)
        if k % 2:
            med = nb[k // 2]
        else:
            med = (nb[k // 2 - 1] + nb[k // 2]) / 2
        out.append((gaps[i] / med, med))
    return out


def sep_col(cnts):
    """THE SEPARATION BOUNDS (the algebraic half): for adjacent
    blocks with n_i / n_{i+1} distinct grid integers on disjoint
    contiguous supports, the exact side bound (n_i + n_{i+1})/2
    grid units.  Consumes the count column only."""
    return [Fr(cnts[i] + cnts[i + 1], 2)
            for i in range(len(cnts) - 1)]


def sieve_bar(t):
    """the sealed continuous small-ball bar C_SB t^2
    (1 + log2(1/t))^{B_SB} (a-priori, never moved; equals the
    r358 pack_bar at dyadic t, warded exact)."""
    tf = float(t)
    return C_SB * tf * tf * (1.0 + math.log2(1.0 / tf)) ** B_SB


def floor_tree_361(leak, brk, sep_fails, cap_ok, scr_alg,
                   min_exact):
    """the sealed main-letter tree (total, exactly one fires;
    order sealed): TARGET_LEAK > LAW_STATE_NOT_EXACT >
    SEP_SATZ_FAILS > FLOOR_THEOREM > QUANTIZED_CENSUS(MED_CAP) >
    QUANTIZED_CENSUS(SIEVE) > FLOOR_ACCIDENTAL."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if sep_fails:
        return "SEP_SATZ_FAILS"
    if cap_ok and scr_alg:
        return "FLOOR_THEOREM"
    if cap_ok:
        return "QUANTIZED_CENSUS(MED_CAP)"
    if min_exact:
        return "QUANTIZED_CENSUS(SIEVE)"
    return "FLOOR_ACCIDENTAL"


def scr_floor_note(known, holds):
    """the sealed scramble-floor note (total): floor measurable
    and >= the candidate / measurable and below / unmeasurable."""
    if not known:
        return "SCR_FLOOR_UNMEASURED"
    if holds:
        return "SCR_FLOOR_HOLDS"
    return "FLOOR_ARITHMETIC"


# ---------------- must-fail mutants
def mutant_theta_wrong_mesh(pos, n_w):
    """f1 MUST-FAIL: the theta map with the WRONG mesh unit
    LL = 4 N_w (not 4 N_w - 2) -- the quantization breaks loud on
    the by-hand pin -- CAUGHT exact."""
    ll = 4 * int(n_w)
    th = np.arccos(np.clip(np.asarray(pos, float), -1.0, 1.0))
    return th * float(ll) / (2.0 * math.pi)


def mutant_floor_from_data(rho):
    """f2 MUST-FAIL (protocol): the 'derived' floor read back as
    the data minimum (consumes rho) -- AST-FLAGGED; on the sealed
    toy column returns 0.4 != the sealed candidate 3/8 (a data
    minimum is not a derivation)."""
    return min(float(v) for v in rho)


def mutant_sieve_bar_posthoc(rho, ts):
    """f3 MUST-FAIL (protocol): C_SB set at the seen mass column
    (consumes rho) -- AST-FLAGGED; on the sealed toy returns
    1.024 != the sealed C_SB 1.0."""
    return max(float(rho[i]) / (float(ts[i]) ** 2
               * (1.0 + math.log2(1.0 / float(ts[i]))) ** B_SB)
               for i in range(len(rho)))


def mutant_bands_posthoc(rho):
    """f4 MUST-FAIL (protocol): band classes split at the seen
    mass median instead of the sealed dyadic log2 rule (consumes
    rho) -- AST-FLAGGED; on the sealed toy returns (0, 0, 1) !=
    the sealed (0, 0, 3)."""
    srt = sorted(float(v) for v in rho)
    med = srt[len(srt) // 2]
    return tuple(0 if float(v) >= med else 1 for v in rho)


def mutant_median_window(gaps):
    """f5 MUST-FAIL: the grel normalization with the WRONG median
    window w = 1 -- on the sealed r358 gap toy the column differs
    at four of five entries -- CAUGHT exact."""
    return EFA.grel_col(list(range(len(gaps))), list(gaps), w=1)


def mutant_gift_bound(rc, P):
    """m6a MUST-FAIL (r355/r358 verbatim): a builder consuming the
    withheld ground-truth terminal drive key -- AST-FLAGGED."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m6b MUST-FAIL (r355/r358 verbatim): a builder consuming the
    branch label -- AST-FLAGGED."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- gate-side diagnostics
def frac_row(rc, ev):
    """gate-side: the exact ledger + exact g/med/sep columns of
    one live row, cross-warded against the r358 float ledger."""
    pos_all, blk_all, m = row_positions(rc)
    fl = frac_center_ledger(pos_all, blk_all, m, rc["N"])
    gl = ev["gl"]
    gl2 = LGC.gap_ledger(pos_all, blk_all, m, rc["N"])
    bitw = (np.array_equal(gl2["cent"], gl["cent"])
            and np.array_equal(gl2["gaps"], gl["gaps"])
            and gl2["ng"] == gl["ng"])
    xw = 0.0
    for i in range(m):
        sc = max(abs(float(gl["cent"][i])), 1.0)
        xw = max(xw, abs(float(fl["cent"][i])
                         - float(gl["cent"][i])) / sc)
        scg = max(abs(float(gl["gaps"][i])), 1e-300)
        xw = max(xw, abs(float(fl["gaps"][i])
                         - float(gl["gaps"][i])) / scg)
    gm = frac_grel(fl["gaps"], W_LOC)
    gfr = [v[0] for v in gm]
    med = [v[1] for v in gm]
    gfl = LGC.g_norm(gl["gaps"])
    for i in range(m):
        xw = max(xw, abs(float(gfr[i]) - float(gfl[i]))
                 / max(abs(float(gfl[i])), 1e-300))
    sb = sep_col(fl["ndist"])
    sep_min = []
    for i in range(m):
        if i == 0:
            sep_min.append(sb[0] if m >= 2 else Fr(1))
        elif i == m - 1:
            sep_min.append(sb[m - 2])
        else:
            sep_min.append(min(sb[i - 1], sb[i]))
    sep_viol = [i for i in range(m - 1) if fl["sides"][i] < sb[i]]
    cap_viol = [i for i in range(m)
                if med[i] > CAP_FAC * sep_min[i]]
    return dict(fl=fl, gfr=gfr, med=med, sep_min=sep_min,
                sep_pairs=m - 1, sep_viol=sep_viol,
                cap_viol=cap_viol, xw=xw, bitw=bitw,
                ng_match=(fl["ng"] == gl["ng"]),
                cnt_eq_nd=(fl["cnt"] == fl["ndist"]))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("mean_sieve_floor_probe -- "
          "PRIME.L2.MEAN_SIEVE.01 (round 361)")
    print("SPEC_SHA %s   (LGC %s / KSF %s / DMF %s / SFE %s)"
          % (SPEC_SHA[:16], LGC.SPEC_SHA[:16], KSF.SPEC_SHA[:16],
             DMF.SPEC_SHA[:16], SFE.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + trees + mutants + audits + "
                        "the four w9 worlds with full eval + exact "
                        "Fractions ledger + SEP/CAP/value-set/sieve "
                        "at w9; ladders, anchors, deep censuses, "
                        "composition, scrambles, twin and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (LGC.SPEC_SHA.startswith(LGC_SHA_PREFIX)
              and KSF.SPEC_SHA.startswith(KSF_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "sealed BEFORE evaluation: the exact Fractions ledger "
          "(integer grid positions, exact centers/gaps/medians), "
          "the SEP-SATZ chain (derived a priori: distinct-integer "
          "means on disjoint contiguous supports => side bound "
          "(n_i+n_j)/2), the MED-CAP census bar 8/3 EXACT, the "
          "floor candidate 3/8 EXACT (gate-side only), the "
          "t-grid j/32 (j = 1..16), the letters; import integrity "
          "LGC %s / KSF %s / DMF %s / SFE %s"
          % (LGC.SPEC_SHA[:8], KSF.SPEC_SHA[:8], DMF.SPEC_SHA[:8],
             SFE.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("row_positions", "frac_center_ledger",
                    "frac_grel", "sep_col", "sieve_bar",
                    "floor_tree_361", "scr_floor_note")
    sc_own = []
    pure_lits = []
    for fn in own_builders:
        sc_own += scope_audit(fn, LGC.BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.QMAX_FORBIDDEN)
        sc_own += scope_audit(fn, SCOPE_FORBIDDEN_361)
        pure_lits += literal_audit(fn)
    sc_f2 = scope_audit("mutant_floor_from_data",
                        SCOPE_FORBIDDEN_361)
    sc_f3 = scope_audit("mutant_sieve_bar_posthoc",
                        SCOPE_FORBIDDEN_361)
    sc_f4 = scope_audit("mutant_bands_posthoc",
                        SCOPE_FORBIDDEN_361)
    sc_m6a = scope_audit("mutant_gift_bound", LGC.BOUND_FORBIDDEN)
    sc_m6b = scope_audit("mutant_branch_peek", LGC.BOUND_FORBIDDEN)
    leak = bool(frag) or bool(sc_own) or bool(pure_lits) or not okf
    check("G03-scope-audits", (not frag) and (not sc_own)
          and (not pure_lits) and len(sc_f2) >= 1
          and len(sc_f3) >= 1 and len(sc_f4) >= 1
          and len(sc_m6a) >= 1 and len(sc_m6b) >= 1,
          "fragment audit clean (%d); the %d module-own builders "
          "clean vs BOUND/PHI3/QMAX/361 sets (%d id hits) and vs "
          "the sealed record-literal set (%d literal hits); f2 "
          "FLAGGED (%s); f3 FLAGGED (%s); f4 FLAGGED (%s); "
          "m6a/m6b FLAGGED (%s / %s)"
          % (len(frag), len(own_builders), len(sc_own),
             len(pure_lits), sc_f2[0] if sc_f2 else "MISS",
             sc_f3[0] if sc_f3 else "MISS",
             sc_f4[0] if sc_f4 else "MISS",
             sc_m6a[0] if sc_m6a else "MISS",
             sc_m6b[0] if sc_m6b else "MISS"))

    # ---------------- S1 toys + trees + mutant pins
    section("S1  SEALED TOYS + TREES + MUTANT PINS (all by hand)")
    t_pos = np.cos(np.array([0.0, 2.0, 3.0, 6.0])
                   * 2.0 * math.pi / 34.0)
    t_blk = np.array([0, 1, 1, 2])
    t_fl = frac_center_ledger(t_pos, t_blk, 3, 9)
    fl_ok = (t_fl["cent"] == [Fr(0), Fr(5, 2), Fr(6)]
             and t_fl["cnt"] == [1, 2, 1]
             and t_fl["sides"] == [Fr(5, 2), Fr(7, 2)]
             and t_fl["gaps"] == [Fr(5, 2), Fr(5, 2), Fr(7, 2)]
             and t_fl["coll"] == 0 and t_fl["rdev"] <= QUANT_BAR)
    t_sb = sep_col(t_fl["ndist"])
    t_gm = frac_grel(t_fl["gaps"], 1)
    grel_ok = (t_sb == [Fr(3, 2), Fr(3, 2)]
               and [v[0] for v in t_gm]
               == [Fr(1), Fr(5, 6), Fr(7, 5)]
               and all(t_fl["sides"][i] >= t_sb[i]
                       for i in range(2))
               and max(v[1] for v in t_gm) <= CAP_FAC * Fr(3, 2))
    c_pos = np.cos(np.array([0.0, 1.0, 10.0])
                   * 2.0 * math.pi / 34.0)
    c_blk = np.array([0, 1, 2])
    c_fl = frac_center_ledger(c_pos, c_blk, 3, 9)
    c_gm = frac_grel(c_fl["gaps"], 1)
    c_sb = sep_col(c_fl["ndist"])
    c_sepmin = [c_sb[0], min(c_sb[0], c_sb[1]), c_sb[1]]
    c_capv = [i for i in range(3)
              if c_gm[i][1] > CAP_FAC * c_sepmin[i]]
    captoy_ok = (c_fl["gaps"] == [Fr(1), Fr(1), Fr(9)]
                 and c_gm[1][0] == Fr(1, 5)
                 and c_gm[1][0] < FLOOR_CAND
                 and c_capv == [1])
    s_q = (0.1, 0.9)
    s_g = (Fr(1, 16), Fr(1))
    s_viol = [t for t in T_GRID
              if sum(s_q[i] for i in range(2) if s_g[i] <= t)
              > sieve_bar(t) + PACK_EPS]
    sievetoy_ok = (s_viol == [Fr(1, 16)]
                   and abs(sieve_bar(Fr(1, 16)) - 25.0 / 256.0)
                   <= TOY_BAR)
    bar_id = max(abs(sieve_bar(Fr(1, 2 ** r)) - LGC.pack_bar(r))
                 for r in range(1, R_MAX + 1))
    d_q = (Fr(1, 2), Fr(1, 4), Fr(1, 4))
    d_g = (Fr(1, 2), Fr(1), Fr(1))
    d_prod = [3 * q * g for q, g in zip(d_q, d_g)]
    d_maxp = max(d_prod)
    d_lhs = max(d_q) * 3 * min(d_g)
    d_m3 = sum(q ** 3 for q in d_q)
    chain_ok = (d_maxp == Fr(3, 4) and d_lhs == Fr(3, 4)
                and d_lhs <= d_maxp and d_m3 == Fr(5, 32)
                and max(d_q) ** 2 == Fr(1, 4)
                and d_m3 <= max(d_q) ** 2)
    t_dk = 0.5 * 1.0 / 2.0
    t_mz = int(math.ceil(10.0 / t_dk - 1.0e-9)) + 1
    if t_mz % 2:
        t_mz += 1
    t_h = t_mz // 2
    t_dev = float(t_h) - 2.0 * (10.0 / 1.0)
    meshtoy_ok = (t_h == 21 and abs(t_dev - 1.0) <= TOY_BAR
                  and 0.0 < t_dev <= MESH_DEV_HI)
    m1 = mutant_theta_wrong_mesh(
        np.array([math.cos(2.0 * math.pi / 34.0)]), 9)
    m1_dev = abs(float(m1[0]) - round(float(m1[0])))
    t1c = LGC.theta_col(
        np.array([math.cos(2.0 * math.pi / 34.0)]), 9)
    f1_ok = (abs(float(m1[0]) - 18.0 / 17.0) <= TOY_BAR
             and m1_dev > QUANT_BAR
             and abs(float(t1c[0]) - 1.0) <= TOY_BAR)
    m2 = mutant_floor_from_data((2.0, 0.5, 0.4, 3.0, 1.5))
    f2_ok = (abs(m2 - 0.4) <= TOY_BAR
             and abs(m2 - float(FLOOR_CAND)) > 1e-6)
    m3 = mutant_sieve_bar_posthoc((0.1,), (Fr(1, 16),))
    f3_ok = (abs(m3 - 1.024) <= 1e-9 and m3 != C_SB)
    m4 = mutant_bands_posthoc((8.0, 7.0, 1.0))
    sealed_band = tuple(int(min(math.floor(math.log2(8.0 / v)),
                                S_BAND_MAX))
                        for v in (8.0, 7.0, 1.0))
    f4_ok = (m4 == (0, 0, 1) and sealed_band == (0, 0, 3)
             and m4 != sealed_band)
    m5 = mutant_median_window([2.0, 1.0, 1.0, 3.0, 3.0])
    m5_pin = (2.0, 2.0 / 3.0, 0.5, 1.5, 1.0)
    sealed_pin = (2.0, 0.5, 0.4, 3.0, 1.5)
    f5_ok = (all(abs(m5[i] - m5_pin[i]) <= TOY_BAR
                 for i in range(5))
             and sum(1 for i in range(5)
                     if abs(m5[i] - sealed_pin[i]) > TOY_BAR)
             == 4)
    tr = (floor_tree_361(True, True, True, True, True, True),
          floor_tree_361(False, True, True, True, True, True),
          floor_tree_361(False, False, True, True, True, True),
          floor_tree_361(False, False, False, True, True, False),
          floor_tree_361(False, False, False, True, False,
                         False),
          floor_tree_361(False, False, False, False, False,
                         True),
          floor_tree_361(False, False, False, False, False,
                         False))
    tr_ok = tr == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                   "SEP_SATZ_FAILS", "FLOOR_THEOREM",
                   "QUANTIZED_CENSUS(MED_CAP)",
                   "QUANTIZED_CENSUS(SIEVE)", "FLOOR_ACCIDENTAL")
    sn = (scr_floor_note(False, False),
          scr_floor_note(True, True),
          scr_floor_note(True, False))
    sn_ok = sn == ("SCR_FLOOR_UNMEASURED", "SCR_FLOOR_HOLDS",
                   "FLOOR_ARITHMETIC")
    sc_br = (LGC.scr_letter(False, True, True, True, True),
             LGC.scr_letter(True, True, True, True, True))
    sc_ok = sc_br == ("P1_ADMISSION", "NO_BREAK")
    check("G10-toy-exactness", fl_ok and grel_ok and captoy_ok
          and sievetoy_ok and bar_id <= TOY_BAR and chain_ok
          and meshtoy_ok and tr_ok and sn_ok and sc_ok,
          "frac ledger toy centers %s counts %s gaps %s EXACT; "
          "seps %s <= sides (SEP-SATZ toy) + grel w=1 g = %s + "
          "MED-CAP holds; cap-fail toy g_1 = %s < 3/8 with "
          "exactly one CAP violation %s CAUGHT; sieve toy viol "
          "%s == [1/16] (bar 25/256); bar identity "
          "sieve_bar(2^-r) == pack_bar(r) worst %.1e; direct "
          "chain toy maxprod %s == q_max m g_min %s, M3 %s <= "
          "q_max^2 1/4; mesh toy h %d dev %.1f in (0, %.1f]; "
          "main tree %s; floor notes %s; scr letters %s"
          % (str([str(v) for v in t_fl["cent"]]),
             str(t_fl["cnt"]),
             str([str(v) for v in t_fl["gaps"]]),
             str([str(v) for v in t_sb]),
             str([str(v[0]) for v in t_gm]),
             str(c_gm[1][0]), str(c_capv),
             str([str(v) for v in s_viol]), bar_id,
             str(d_maxp), str(d_lhs), str(d_m3), t_h, t_dev,
             MESH_DEV_HI, "OK" if tr_ok else str(tr),
             "OK" if sn_ok else str(sn),
             "OK" if sc_ok else str(sc_br)))
    check("G11-mutant-pins", f1_ok and f2_ok and f3_ok and f4_ok
          and f5_ok,
          "f1 pin t = %.6f (dev %.4f > bar %.0e) vs true 1.0 -- "
          "the wrong mesh unit breaks quantization; f2 pin %.2f "
          "!= candidate %.3f (data minimum is not a derivation); "
          "f3 pin %.3f != sealed C_SB %.1f; f4 pin %s != sealed "
          "dyadic %s; f5 pin %s differs at 4/5 entries from the "
          "sealed w = 2 column"
          % (float(m1[0]), m1_dev, QUANT_BAR, m2,
             float(FLOOR_CAND), m3, C_SB, str(m4),
             str(sealed_band),
             str(tuple(round(v, 3) for v in m5))))

    # ---------------- S2 world construction
    section("S2  THE FOUR WORLD FAMILIES (construction + "
            "admission + frame reproductions)")
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
          "at NU (%d, %d) (violations %s) -- the integer grid of "
          "the exact ledger is mesh-parametrized, fit-free"
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
        kzs_l = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= LGC.H_CAP:
                kzs_l.append(kz)
            elif h <= LGC.EXT_H_MAX:
                ekz.append(kz)
            elif h <= LGC.EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs_l]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:LGC.K_EXT]
        ekz2.sort()
        pool2 = epool[LGC.K_EXT:] + [
            BH.wpack(kz) for _h, kz in ekz2[:LGC.EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:LGC.K_EXT2]
        ext3 = [BH.wpack(kz)
                for kz in LGC.EXT3_KZ_B + LGC.EXT3_KZ_A]
        ext4 = [BH.wpack(kz) for kz in LGC.EXT4_KZ]
        ext5 = [BH.wpack(kz)
                for kz in LGC.EXT5_KZ_B + LGC.EXT5_KZ_A]
        packs_a = ladder + ext + ext2 + ext3 + ext4 + ext5
        okA = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder)
               and len(ext) == LGC.K_EXT
               and all(p["nf"] is None for p in packs_a))
        packs_b = [SFE.wpack_b(kz, NU_B) for kz in FRAMEB_KZ]
        okB = all(p["nf"] is None and p["complete"]
                  for p in packs_b)
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
        okC = (len(packs_c3) == R358_ROWS[2]
               and len(packs_c4) == R358_ROWS[3]
               and all(p["complete"]
                       for p in packs_c3 + packs_c4))
        check("G21-family-census", okA and okB and okC
              and len(packs_a) == R358_ROWS[0]
              and len(packs_b) == R358_ROWS[1],
              "FRAME A: %d rows (== %d, 42 ladder + %d ext + %d "
              "ext2 + %d EXT3 + %d EXT4 + %d EXT5, all adopted "
              "as-is, all POSITIVE_PREFIX); FRAME B: %d/%d sealed "
              "r353 anchors re-admitted %s; CHI3 %d/%d + CHI4 "
              "%d/%d built (kept-atom exclusions %s)"
              % (len(packs_a), R358_ROWS[0], len(ext), len(ext2),
                 len(ext3), len(ext4), len(ext5), len(packs_b),
                 R358_ROWS[1],
                 str(sorted(p["kz"] for p in packs_b)),
                 len(packs_c3), R358_ROWS[2], len(packs_c4),
                 R358_ROWS[3], str(excl) if excl else "none"))

    # ---------------- S3 eval + exact wards + the exact ledger
    section("S3  EVAL + EXACT LIVE WARDS (r358 wards + the exact "
            "Fractions ledger cross-wards)")
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
            rc["ev"] = LGC.eval_gap(rc)
            recs.append(rc)
        recs.sort(key=lambda r: (r["N"], r["kz"]))
        frecs[fam] = recs
    tb_bad = []
    qdev_w = 0.0
    rdev_w = 0.0
    coll_w = 0
    xw_w = 0.0
    bitw_bad = 0
    ngm_bad = 0
    cnd_bad = 0
    mult_drop = []
    mono_bad = 0
    sumq_w = 0.0
    chain_w = 0.0
    m3q_w = 0.0
    live = {}
    for fam in frecs:
        rows = []
        for rc in frecs[fam]:
            ev = rc["ev"]
            bar = (LGC.TB_WARD_BAR_B if fam == "FRAME_B"
                   else LGC.CHI_TB_BAR if fam.startswith("CHI")
                   else LGC.TB_WARD_BAR if rc["N"] <= LGC.DEEP_N
                   else max(LGC.TB_WARD_BAR_DEEP,
                            LGC.TB_WARD_BAR_X345))
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
            fr = frac_row(rc, ev)
            rdev_w = max(rdev_w, fr["fl"]["rdev"])
            coll_w += fr["fl"]["coll"]
            xw_w = max(xw_w, fr["xw"])
            if not fr["bitw"]:
                bitw_bad += 1
            if not fr["ng_match"]:
                ngm_bad += 1
            if not fr["cnt_eq_nd"]:
                cnd_bad += 1
            gc = LGC.gap_columns(ev)
            sumq_w = max(sumq_w,
                         abs(float(np.sum(gc["q"])) - 1.0))
            lhs = float(np.max(gc["q"])) * float(ev["m"]) \
                * gc["ming"]
            rhs = gc["maxprod"] * gc["lg"]
            chain_w = max(chain_w, max(0.0, lhs - rhs)
                          / max(rhs, 1e-300))
            m3q_w = max(m3q_w,
                        max(0.0, gc["m3"]
                            - float(np.max(gc["q"])) ** 2))
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            qm = ev["mqs"]["qm"]
            fab = QGL.fab_of(float(mloc), qm, lgl)
            a1s = np.asarray(ev["A1"], float)[ev["gl"]["oc"]]
            rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc,
                             lg=lgl, fab=fab,
                             grel=grel_map[rc["kz"]],
                             fabg=fab * grel_map[rc["kz"]],
                             gc=gc, fr=fr, a1s=a1s))
        live[fam] = rows
    n_live = sum(len(live[f]) for f in live)
    brk_struct = (bool(tb_bad) or qdev_w > QUANT_BAR
                  or rdev_w > QUANT_BAR or coll_w > 0
                  or xw_w > FRAC_XW_BAR or bitw_bad > 0
                  or ngm_bad > 0 or cnd_bad > 0 or mono_bad > 0
                  or sumq_w > CHAIN_EPS or chain_w > CHAIN_EPS
                  or m3q_w > CHAIN_EPS or not frb_ok
                  or not chi_ok or bool(mesh_bad)
                  or bar_id > TOY_BAR or not fl_ok or not grel_ok
                  or not captoy_ok or not sievetoy_ok
                  or not chain_ok or not meshtoy_ok
                  or n_live == 0)
    check("G30-exact-live-wards", not brk_struct,
          "on %d live rows (drops %s): float quantization worst "
          "%.1e / exact-ledger rounding worst %.1e (bar %.0e); "
          "integer collisions %d (counts == distinct on all "
          "rows: %s); exact/float cross-ward worst %.1e (bar "
          "%.0e); float ledger re-derivation BITWISE %d bad; "
          "group-count match %d bad; centers monotone (%d bad); "
          "sum q worst %.1e; chain algebra q_max m g_min <= "
          "maxprod log m one-sided %.1e; M3 <= q_max^2 one-sided "
          "%.1e; contribution ward %s -- the exact ledger IS the "
          "r358 ledger"
          % (n_live, str(mult_drop) if mult_drop else "none",
             qdev_w, rdev_w, QUANT_BAR, coll_w,
             "yes" if cnd_bad == 0 else "NO", xw_w, FRAC_XW_BAR,
             bitw_bad, ngm_bad, mono_bad, sumq_w, chain_w, m3q_w,
             "OK" if not tb_bad else "BROKEN %s"
             % str(tb_bad[:3])))

    # ---------------- S4 Leg 0 anchors
    section("S4  LEG 0 -- ANCHORS (the r358 record through the "
            "same channel, bit-near)")
    fam_order = ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
    n_bands_gc = sum(len(row["gc"]["bands"]) for f in fam_order
                     for row in live[f])
    if smoke:
        check("G40-anchors", True, "SMOKE: skipped")
        ceil = max(r["gc"]["maxprod"] for f in fam_order
                   for r in live[f])
        ck_rule = ceil
    else:
        ming_all = min(row["gc"]["ming"] for f in fam_order
                       for row in live[f])
        s1_ok = True
        s1_txt = []
        for fi, fam in enumerate(fam_order):
            s1 = max(row["gc"]["Sr"][0] for row in live[fam])
            s1_ok = s1_ok and (abs(s1 - R358_S1MAX[fi])
                               <= R358_S1MAX_TOL)
            s1_txt.append("%.4f" % s1)
        t1_ok = True
        t1_txt = []
        ck_rule = 0.0
        for fi, fam in enumerate(fam_order):
            rows = live[fam]
            ncal = N_CAL_FB if fam == "FRAME_B" else N_CAL_T1
            ck = max(r["gc"]["maxprod"] for r in rows[:ncal])
            tmax = max(r["gc"]["maxprod"] for r in rows[ncal:])
            ck_rule = max(ck_rule, ck)
            t1_ok = t1_ok and (abs(ck - R358_T1_CK[fi])
                               <= R358_T1_TOL) \
                and (abs(tmax - R358_T1_TMAX[fi])
                     <= R358_T1_TOL)
            t1_txt.append("%s %.2f/%.2f" % (fam[:2], ck, tmax))
        ceil = max(r["gc"]["maxprod"] for f in fam_order
                   for r in live[f])
        ck2x = max(r["fabg"] for r in live["FRAME_A"])
        ck2x_kz = max(live["FRAME_A"],
                      key=lambda r: r["fabg"])["kz"]
        stress_ok = True
        stress_txt = []
        for si, kz_s in enumerate(STRESS_KZ):
            row = next((r for r in live["FRAME_A"]
                        if r["kz"] == kz_s), None)
            mg = row["gc"]["ming"] if row else -1.0
            stress_ok = stress_ok and (
                abs(mg - R358_STRESS_MING[si])
                <= R358_STRESS_TOL)
            stress_txt.append("kz%d %.3f" % (kz_s, mg))
        check("G40-anchors",
              abs(ming_all - R358_MING) <= R358_MING_TOL
              and s1_ok and t1_ok
              and abs(ceil - R358_CEIL) <= R358_CEIL_TOL
              and abs(ck2x - LGC.R353_CK2X) <= LGC.R353_CK2X_TOL
              and ck2x_kz == LGC.R353_CK2X_KZ
              and stress_ok and n_bands_gc == R358_BANDS,
              "min g %.4f (rec %.3f); max S_1 per family %s (rec "
              "%s); T1 freeze/testmax %s (rec CK %s TMAX %s); "
              "global ceiling %.2f (rec %.2f); C_K2X %.2f at "
              "kz%d (rec %.2f at kz%d); stress min g %s (rec "
              "%s); bands %d (rec %d) -- the r358 record "
              "reproduces through THIS channel"
              % (ming_all, R358_MING, str(s1_txt),
                 str(R358_S1MAX), "; ".join(t1_txt),
                 str(R358_T1_CK), str(R358_T1_TMAX), ceil,
                 R358_CEIL, ck2x, ck2x_kz, LGC.R353_CK2X,
                 LGC.R353_CK2X_KZ, str(stress_txt),
                 str(R358_STRESS_MING), n_bands_gc, R358_BANDS))

    # ---------------- S5 Leg A: the floor derivation
    section("S5  LEG A -- THE FLOOR DERIVATION (SEP-SATZ + "
            "MED-CAP + the exact value set)")
    sep_pairs = sum(row["fr"]["sep_pairs"] for f in fam_order
                    for row in live[f])
    sep_viols = [(f, row["kz"], i) for f in fam_order
                 for row in live[f]
                 for i in row["fr"]["sep_viol"]]
    n_atoms = sum(row["m"] for f in fam_order for row in live[f])
    cap_viols = [(f, row["kz"], i) for f in fam_order
                 for row in live[f]
                 for i in row["fr"]["cap_viol"]]
    worst_ratio = Fr(0)
    worst_loc = ("-", 0)
    alg_floor = None
    for f in fam_order:
        for row in live[f]:
            fr = row["fr"]
            for i in range(row["m"]):
                r = fr["med"][i] / (CAP_FAC * fr["sep_min"][i])
                if r > worst_ratio:
                    worst_ratio = r
                    worst_loc = (f, row["kz"])
                fa = fr["sep_min"][i] / fr["med"][i]
                if alg_floor is None or fa < alg_floor:
                    alg_floor = fa
    sep_ok = (len(sep_viols) == 0)
    cap_ok = sep_ok and (len(cap_viols) == 0)
    check("G50-sep-satz", True,
          "SEP-SATZ (the algebraic half, EXACT Fractions): side "
          "d_i >= (n_i + n_{i+1})/2 on %d adjacent pairs of %d "
          "live rows -- violations %s; preconditions warded live "
          "(integrality worst %.1e, collisions %d, contiguity "
          "via monotone centers %d bad) -- %s"
          % (sep_pairs, n_live,
             "0" if sep_ok else str(sep_viols[:6]), rdev_w,
             coll_w, mono_bad,
             "the separation theorem holds on the surface"
             if sep_ok else "THE ALGEBRAIC HALF BREAKS"))
    min_g = None
    min_loc = ("-", 0)
    fam_min = {}
    subhalf = []
    allrat = 0
    for f in fam_order:
        fmin = None
        for row in live[f]:
            fr = row["fr"]
            allrat += 1
            for i in range(row["m"]):
                g = fr["gfr"][i]
                if fmin is None or g < fmin:
                    fmin = g
                if min_g is None or g < min_g:
                    min_g = g
                    min_loc = (f, row["kz"])
                if g < Fr(1, 2):
                    subhalf.append((f, row["kz"], i, g,
                                    fr["fl"]["gaps"][i],
                                    fr["med"][i],
                                    fr["fl"]["ndist"][i],
                                    fr["sep_min"][i],
                                    float(row["gc"]["q"][i])))
        fam_min[f] = fmin
    min_exact = (min_g == FLOOR_CAND)
    if smoke:
        for f in fam_order:
            row = live[f][0]
            vs = sorted(set(row["fr"]["gfr"]))
            info("w9 %s (m %d): exact value set (%d distinct): %s"
                 % (f, row["m"], len(vs),
                    " ".join(str(v) for v in vs)))
    info("EXACT per-family minima: %s"
         % "; ".join("%s %s" % (f, str(fam_min[f]))
                     for f in fam_order))
    info("SUB-HALF ATOMS (g < 1/2), %d total "
         "(fam kz i | g | gap | med | n_i | sep_min | q_i):"
         % len(subhalf))
    for row in sorted(subhalf, key=lambda v: (v[3], v[0], v[1],
                                              v[2]))[:80]:
        info("  %s kz%-3d i%-4d | %-7s | %-7s | %-7s | %2d | "
             "%-5s | %.2e"
             % (row[0][:2], row[1], row[2], str(row[3]),
                str(row[4]), str(row[5]), row[6], str(row[7]),
                row[8]))
    if len(subhalf) > 80:
        info("  ... %d more" % (len(subhalf) - 80))
    check("G51-value-set", True,
          "THE EXACT VALUE SET: every g of every live row is "
          "rational (%d/%d rows all-rational by construction); "
          "min g over the round = %s at %s kz%d -- EXACTLY the "
          "mesh rational 3/8: %s; %d sub-half atoms; per-family "
          "exact minima %s"
          % (allrat, n_live, str(min_g), min_loc[0], min_loc[1],
             "YES" if min_exact else "NO", len(subhalf),
             str({f: str(fam_min[f]) for f in fam_order})))
    check("G52-med-cap", True,
          "MED-CAP (the named missing half, EXACT census): med_i "
          "<= (8/3) sep_i on %d atoms -- violations %s; worst "
          "med/((8/3) sep) = %.3f at %s kz%d; the ALGEBRAIC "
          "floor min sep_i/med_i = %s %s 3/8 -- %s"
          % (n_atoms, "0" if not cap_viols
             else "%d %s" % (len(cap_viols), str(cap_viols[:5])),
             float(worst_ratio), worst_loc[0], worst_loc[1],
             str(alg_floor),
             ">=" if (alg_floor is not None
                      and alg_floor >= FLOOR_CAND) else "<",
             "the chain g_i >= sep_i/med_i >= 3/8 closes "
             "POINTWISE on the surface" if cap_ok
             else "the chain does NOT close -- the cap is the "
             "precise gap (named)"))

    # ---------------- S6 Leg B: the sieve census
    section("S6  LEG B -- THE MEAN SIEVE CENSUS (t-grid rows + "
            "bands + mean) + THE STECKBRIEF")
    row_viol = []
    mean_head = 0.0
    for fam in fam_order:
        rows = live[fam]
        for t in T_GRID:
            bar_t = sieve_bar(t)
            ss = []
            for row in rows:
                fr = row["fr"]
                q = row["gc"]["q"]
                s = float(sum(float(q[i])
                              for i in range(row["m"])
                              if fr["gfr"][i] <= t))
                ss.append(s)
                if s > bar_t + PACK_EPS:
                    row_viol.append((fam, row["kz"], str(t)))
            mean_head = max(mean_head,
                            (sum(ss) / len(ss)) / bar_t)
    band_viol = []
    n_bands_all = 0
    n_band_cells = 0
    dy_viol = 0
    for fam in fam_order:
        for row in live[fam]:
            a1 = row["a1s"]
            fr = row["fr"]
            amax = float(np.max(a1)) if len(a1) else 0.0
            band = np.minimum(np.floor(np.log2(
                max(amax, 1e-300)
                / np.maximum(a1, 1e-300))).astype(int),
                S_BAND_MAX)
            for s_id in sorted(set(int(v) for v in band)):
                msk = band == s_id
                if int(np.sum(msk)) < BAND_MIN:
                    continue
                n_bands_all += 1
                tot_b = float(np.sum(a1[msk]))
                idx = [i for i in range(row["m"]) if msk[i]]
                for t in T_GRID:
                    n_band_cells += 1
                    sbt = sum(float(a1[i]) for i in idx
                              if fr["gfr"][i] <= t) \
                        / max(tot_b, 1e-300)
                    if sbt > sieve_bar(t) + PACK_EPS:
                        band_viol.append((fam, row["kz"], s_id,
                                          str(t)))
            for s_id, bd in sorted(row["gc"]["bands"].items()):
                for r in range(1, R_MAX + 1):
                    if bd["sbr"][r - 1] \
                            > LGC.sb_bar(r) + PACK_EPS:
                        dy_viol += 1
    check("G60-sieve-rows", True,
          "THE ROW-LEVEL SIEVE CENSUS at the sealed t-grid "
          "(j/32, j = 1..16) vs bar(t) = t^2 (1 + log2(1/t))^2: "
          "%d rows x %d t -- violations %s; the per-family MEAN "
          "small-ball mass has headroom max_t mean S(t)/bar(t) "
          "= %.4f (the in-the-mean form)"
          % (n_live, len(T_GRID),
             "0" if not row_viol else "%d %s"
             % (len(row_viol), str(row_viol[:5])), mean_head))
    check("G61-sieve-bands", n_bands_all == n_bands_gc,
          "THE BAND-LEVEL SIEVE CENSUS with EXACT g: %d dyadic "
          "source bands (>= %d members, r358 banding verbatim, "
          "cross-count == %d through the r358 channel), %d band "
          "x t cells -- violations %s; r358 dyadic continuity "
          "(sbr, r = 1..%d): %d violations"
          % (n_bands_all, BAND_MIN, n_bands_gc, n_band_cells,
             "0" if not band_viol else "%d %s"
             % (len(band_viol), str(band_viol[:5])), R_MAX,
             dy_viol))
    check("G62-steckbrief", True,
          "THE SPECIALIST STECKBRIEF (typed, not proved): (i) "
          "WELL-SPACEDNESS input of the Montgomery-Vaughan large "
          "sieve == SEP-SATZ (centers (n_i+n_j)/2-separated on "
          "the integer mesh -- %s this round); (ii) the "
          "mass-form band bound needs band MASS comparability == "
          "the r358 dictionary block (carries); (iii) "
          "Erdos-Turan / second-moment Weyl on alpha log p carry "
          "the MEAN over the window family (measured headroom "
          "%.4f), NOT the per-window statement; (iv) THE MISSING "
          "PIECE, named: the local-median regularity MED-CAP "
          "med_i <= (8/3) sep_i -- BOTH open sieve parts reduce "
          "to it on this surface (%s)"
          % ("0-violation census" if sep_ok else "BROKEN",
             mean_head,
             "0-violation census" if cap_ok else "open"))

    # ---------------- S7 Leg C: the direct chain
    section("S7  LEG C -- THE DIRECT CHAIN (T2' trivializes "
            "modulo the floor)")
    if smoke:
        check("G70-direct-chain", True, "SMOKE: skipped")
        m0_cens = None
        m0_rule = None
    else:
        floor_holds = (min_g is not None
                       and min_g >= FLOOR_CAND)
        m0_cens = LGC.solve_m0(
            lambda t: 2.0 * math.log(float(CAP_FAC) * ceil))
        m0_rule = LGC.solve_m0(
            lambda t: 2.0 * math.log(float(CAP_FAC) * ck_rule))
        check("G70-direct-chain", True,
              "THE DIRECT CHAIN (floor %s on all %d rows): q_i "
              "<= C_K log m/(m g_i) <= (8/3) C_K log m/m UNIFORM "
              "=> M_3 <= (8/3)^2 C_K^2 (log m)^2/m^2 -- C_G AND "
              "two log powers DROP vs the r358 Carleson route; "
              "T2' TRIVIALIZES: S_r == 0 for r >= 2 is FORCED by "
              "g >= 3/8 (2^-2 < 3/8), S_1 <= 1 <= bar(1); m_0* "
              "= 10^%.1f at the MEASURED census ceiling C_K = "
              "%.2f (honest: census, not a rule) and 10^%.1f IF "
              "the family-uniform T1 rule existed at the freeze "
              "max %.2f (the r358-broken rule -- conditional, "
              "typed) vs r358 Carleson 10^%.1f / r351 10^%.1f / "
              "r353 10^%.1f / r306 census 10^%.1f; C_K STILL "
              "ENTERS SQUARED (the T1 constant rule stays the "
              "second named rest); chain algebra warded exact "
              "one-sided (G30: %.1e / %.1e)"
              % ("HOLDS (census)" if floor_holds else "BREAKS",
                 n_live, m0_cens if m0_cens else -1.0, ceil,
                 m0_rule if m0_rule else -1.0, ck_rule,
                 M0_REFS_361[0], M0_REFS_361[1], M0_REFS_361[2],
                 M0_REFS_361[3], chain_w, m3q_w))

    # ---------------- S8 Leg D: scrambles + twin
    section("S8  LEG D -- MATCHED SCRAMBLES (floor contrast) + "
            "TWIN")
    if smoke:
        check("G80-scrambles", True, "SMOKE: skipped")
        check("G81-twin", True, "SMOKE: skipped")
        scr_txt = "SMOKE"
        scr_known = False
        scr_holds = False
        devT = 0.0
    else:
        alpha9 = float(core.U_ALL[9])
        rng = np.random.default_rng(SCR_SEED)
        scr_worlds = []
        pA = BH.wpack(9, base_kw=dict(scramble_seed=SCR_SEED))
        scr_worlds.append(("FRAME_A_w9", pA))
        alpha80 = float(core.U_ALL[80])
        ka80 = core.atoms_in(alpha80)
        uu_scr = np.sort(rng.uniform(0.0, 2.0 * alpha80,
                                     size=ka80))
        pBv = SFE.wpack_b(80, NU_B,
                          comb=(uu_scr,
                                core.MU_ALL[:ka80].copy()))
        scr_worlds.append(("FRAME_B_kz80", pBv))
        u3s, w3s, _nn, _ch = DMF.chi_window_comb(9, Q_CHI3)
        u_scr = np.sort(np.random.default_rng(SCR_SEED).uniform(
            0.0, 2.0 * alpha9, size=len(w3s)))
        try:
            pC = DMF.chi_wpack(9, 1.0, LPQ3, (u_scr, w3s))
        except Exception as exc:            # noqa: BLE001
            pC = dict(kz=9, N=0, nf="build-fail: %s" % exc,
                      complete=False)
        scr_worlds.append(("CHI3_w9", pC))
        scr_lets = []
        scr_known = False
        scr_holds = True
        for lab, p in scr_worlds:
            p1_ok = (p.get("nf") is None
                     and p.get("complete", True))
            qdev_s = None
            ming_s = None
            mult_ok = True
            quant_ok = True
            if p.get("rows"):
                rc = DSW.rung_rec(p)
                ev = LGC.eval_gap(rc)
                if not ev["degenerate"]:
                    mult_ok = ev["mx_mult"] <= MULT_CAP
                    qdev_s = ev["gl"]["qdev"]
                    quant_ok = qdev_s <= QUANT_BAR
                    gcs = LGC.gap_columns(ev)
                    ming_s = gcs["ming"]
                    scr_known = True
                    if ming_s < float(FLOOR_CAND) - 1e-9:
                        scr_holds = False
            let = LGC.scr_letter(p1_ok, mult_ok, quant_ok, True,
                                 True)
            scr_lets.append(
                "%s -> %s (nf %s, qdev %s, min g %s)"
                % (lab, let, str(p.get("nf")),
                   ("%.1e" % qdev_s) if qdev_s is not None
                   else "n/a",
                   ("%.3f" % ming_s) if ming_s is not None
                   else "n/a"))
        scr_txt = "; ".join(scr_lets)
        check("G80-scrambles", all("NO_BREAK" not in s
                                   for s in scr_lets),
              "MATCHED SCRAMBLES through all three construction "
              "channels (sealed precondition order): %s -- THE "
              "FLOOR CONTRAST: %s (a measurable scramble floor "
              ">= 3/8 would mark the cap construction-algebraic; "
              "below 3/8 arithmetic; unmeasurable = the channels "
              "break BEFORE any gap structure exists)"
              % (scr_txt,
                 scr_floor_note(scr_known,
                                scr_known and scr_holds)))
        gaps3 = MF.local_gaps(u3s)
        _a, _M, _L, _Nw, D9 = V.window_shape(9)
        u3t, w3t, _d, _du = AKD.twin_rational(u3s, w3s, gaps3,
                                              D9, TWIN_TOL)
        pk3 = DMF.chi_wpack(9, 1.0, LPQ3, (u3s, w3s))
        pk3t = DMF.chi_wpack(9, 1.0, LPQ3, (u3t, w3t))
        rcT = DSW.rung_rec(pk3)
        rcTt = DSW.rung_rec(pk3t)
        evT = LGC.eval_gap(rcT)
        evTt = LGC.eval_gap(rcTt)
        gcT = LGC.gap_columns(evT)
        gcTt = LGC.gap_columns(evTt)
        devT = max(abs(gcT["maxprod"] - gcTt["maxprod"])
                   / max(gcT["maxprod"], 1e-300),
                   abs(gcT["t2v"] - gcTt["t2v"])
                   / max(gcT["t2v"], 1e-300),
                   abs(gcT["ming"] - gcTt["ming"])
                   / max(gcT["ming"], 1e-300))
        check("G81-twin", devT <= TWIN_BAR,
              "RATIONAL TWIN of the chi3 comb (tol %.0e) through "
              "the matched terminal channel at w9: maxprod + "
              "T2val + min g devs %.1e (bar %.0e) -- the gap "
              "floor carries bit-near" % (TWIN_TOL, devT,
                                          TWIN_BAR))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G97-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact rational gap ledger, the SEP-SATZ "
          "separation census, the MED-CAP adjudication of the "
          "3/8 floor, the continuous-t sieve census, the direct "
          "M3 chain modulo the floor and the sharpened sieve "
          "steckbrief -- NO new certificate promoted, NO "
          "universal bound claimed beyond the measured rows")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        scr_alg = scr_known and scr_holds
        verdict_main = floor_tree_361(leak, brk_struct,
                                      not sep_ok, cap_ok,
                                      scr_alg, min_exact)
        flags = []
        flags.append("VALSET(min g %s%s, %d sub-half)"
                     % (str(min_g),
                        " EXACT_3/8" if min_exact else "",
                        len(subhalf)))
        flags.append("SEP_SATZ(%s/%d pairs)"
                     % ("0" if sep_ok else str(len(sep_viols)),
                        sep_pairs))
        flags.append("MED_CAP(%s/%d atoms, worst %.3f)"
                     % ("0" if not cap_viols
                        else str(len(cap_viols)), n_atoms,
                        float(worst_ratio)))
        flags.append("SIEVE_CENSUS_%s(rows %d, band cells %d, "
                     "dyadic %d)"
                     % ("HOLDS" if not row_viol
                        and not band_viol and dy_viol == 0
                        else "BREAKS", len(row_viol),
                        len(band_viol), dy_viol))
        flags.append("SIEVE_PARTIAL(MV spacing = SEP-SATZ; "
                     "missing = MED-CAP regularity)")
        flags.append("DIRECT_CHAIN(m_0* 10^%.1f census / "
                     "10^%.1f rule-conditional vs 10^%.1f/"
                     "10^%.1f/10^%.1f/10^%.1f)"
                     % (m0_cens if m0_cens else -1.0,
                        m0_rule if m0_rule else -1.0,
                        M0_REFS_361[0], M0_REFS_361[1],
                        M0_REFS_361[2], M0_REFS_361[3]))
        flags.append(scr_floor_note(scr_known,
                                    scr_known and scr_holds))
        flags.append("SCRAMBLE(%s)" % scr_txt)
        flags.append("TWIN(%.1e)" % devT)
        flags.append("MUSTFAIL_LEDGER(f1-f5 + m6a/m6b)")
        verd = verdict_main + "".join(" + " + f for f in flags)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G98-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): integrality, the exact "
          "ledger, the Fractions cross-wards, the separation "
          "preconditions, the chain algebra, the bar identity, "
          "frame reproductions, mesh identity, purity audits "
          "(exact/AST-decided); CENSUS: SEP-SATZ, MED-CAP, the "
          "value set, every S(t), band mass and violation count "
          "(the finite 89 + 8 + 42 + 42 row surface); OPEN: the "
          "MED-CAP as a lemma, the family-uniform T1 rule, any "
          "cofinal law, the actual proof; NO RH claim"
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
