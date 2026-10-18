#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""delta_source_anatomy_probe -- PRIME.LSTAR.DELTA_SOURCE_ANATOMY.01
(round 348): THE DELTA SOURCE ANATOMY -- the order-0 mirror as an
object, and the resolvent rate-equality theorem candidate
delta_p == delta_q == delta.  The named successor round of r347
(ALPHA_CLOSED): the ONE remaining measured exponent of the L*
margin law, delta = 2.668 (the cancellation law c'/c ~ N_w^-2.67,
r345), is put under source anatomy -- can it be derived from the
digamma/tent geometry of the mirror paths, or at least reduced to
a theorem-grade structure statement (a common dressing rate) plus
an elementary remainder?

THE CHAIN (r342/r343/r345/r347, all sealed records): r342 the
two-atom law (bare decay laws p -0.754 / q -0.645 / c -0.697;
digamma/tent weight dictionary at v_pred 9.0e-4); r343 the exact
resolvent dressing (Delta c = sum_m alpha_m beta_m/(1 - delta_m)
over the rest modes; the dressing works by the signed cancellation
Delta c ~ -c); r345 the mirror anatomy (rho_0 median 0.839: the
DIRECT path u1.u2 carries the bulk of the mirror in PATHS, yet
M90 ~ 30 modes: multi-modal in MODES) and THE CANCELLATION LAW
delta = 2.668 (halves-stable, EXT3 10/12 high-side, EXT4 6/6);
r347 the one-line closure alpha = a_c + delta (residual 0.033, all
four closures <= 0.1) plus the UNIVERSALITY CENSUS |delta_p -
delta| = 0.059, |delta_q - delta| = 0.003 -- the dressing eats p,
q and c near a COMMON rate, census-grade, honestly no law.  THE
ROUND'S CONTRACT: (Leg A) the order-0 mirror anatomy -- the exact
split of the resolvent series at order zero,
    Delta c = u1.u2 + sum_m alpha_m beta_m delta_m/(1 - delta_m)
(direct overlap + resolvent enhancement; derived from (I-D)^{-1} =
I + D (I-D)^{-1} projected onto the rest eigenmodes, verified in
exact Fractions on the hand toy and per rung in f64 on all 75
rows), the mode census of the carriers (peel pairs? arch layer?),
the dictionary reach of the overlap products (weight side vs
kernel side), and the sealed delta_0 fit of the ORDER-0 MISS
y0 = 1 - rho_0; (Leg B) THE RATE-EQUALITY THEOREM CANDIDATE made
exact: with (lambda_1, lambda_2) the top-2 eigenvalues of E and
(a_k, b_k) the pair components of their eigenvectors, the top-2
truncation of the resolvent pair block M gives EXACTLY
    p'_2 = m (g21 a2^2 + b2^2)/Dt^2,
    q'_2 = m (g21 a1^2 + b1^2)/Dt^2,
    c'_2 = m (g21 a1 a2 + b1 b2)/Dt^2,
      Dt = a1 b2 - a2 b1,  m = margin,  g21 = (1-l2)/(1-l1)
(exact 2x2 algebra of M_2^{-1} = I - A'_2; exact in Fractions on a
rank-2 rational model and through the FULL Schur chain on a
block-spectral 4x4) -- UNDER TOP-2 DOMINANCE WITH FLAT GEOMETRY
every dressed scalar is margin x an O(1) geometry factor, hence
    delta_x = alpha - a_x   for x in {p, q, c}:
THE COMMON DRESSING RATE IS THE MARGIN RATE, and the naive
statement delta_p == delta_q == delta is exactly true IFF the bare
rates coincide (a_p == a_q == a_c) -- otherwise it breaks by
exactly the bare-rate spread (proved on synthetic families with
controlled structure, and the flat-geometry hypothesis is
load-bearing: an angle drift breaks the equality loudly); (Leg C)
the delta decomposition delta == alpha - a_c with every building
block typed (theorem-grade skeleton / certified census /
fit-census) and the irreducible measured rest named; (Leg D) the
mirror-quota anatomy on MAIN/TWIN, the sealed world clause
re-gated (8 worlds incl. the r330 Dirichlet pair), and the
concentration-weak rungs kz28/kz44/kz59 as their own row family;
(Leg E) must-fails.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in either
direction, mincut unchanged.  Coexistence: R346 (cover
canonization, terminal lane) is sealed and synced -- this probe
touches NOTHING outside its own file and the strictly additive
rh-sync.  Two-commit freeze protocol (r329 convention): spec +
machinery committed BEFORE the record run, record tables inserted
after.

THE EXACT OBJECTS (all gated): per rung the r342 bundle
(PX.build_rung verbatim, SPEC_SHA prefix gated b09f8ccd), the r343
extension (PC3.extend_rung verbatim, 9ffc2705: rest eigenmodes,
Delta c, top-K shadows, K_res), the r347 closure coordinates
(DA.closure_cols verbatim, bd1aa7f3: p', q', c', bridge, c'/c,
p'/p, q'/q, the one-line identity wards); THE ORDER-0 SPLIT (this
round's first exact spine): from (I-D)^{-1} = I + D (I-D)^{-1},
Delta c = u1^T (I-D)^{-1} u2 splits EXACTLY as T0 + T+ with T0 =
u1.u2 (the order-0 direct path) and T+ = sum_m alpha_m beta_m
delta_m/(1 - delta_m) (all higher paths, mode-resolved); the
mirror quotas rho_0 = -T0/c, rho_hi = -T+/c, the ORDER-0 MISS
y0 = 1 - rho_0, and the exact bookkeeping identity c'/c = y0 -
rho_hi (gated per rung); THE TWO-LEVEL DRESSED-SCALAR SHADOWS
(this round's second exact spine): p'_2, q'_2, c'_2 as above --
exact for the top-2-truncated resolvent (Fractions), measured
against the true dressed scalars per rung (the truncation census);
THE MARGIN-PINNING RATIOS p'/margin, q'/margin, |c'|/margin --
the live signature of the rate-equality candidate, adjudicated
under the r345 curvature-honest flatness protocol verbatim
(GR.curvflat_protocol, 1f99235a); THE MODE CENSUS: per rung the
L1 profile of the mode terms alpha_m beta_m/(1 - delta_m) (top-1
share, M90 at the sealed 0.9 quantile), the arch-rim share of T0
in ATOM terms, the arch-rim mass and peel-pair mass of the top
carrying MODE; THE DICTIONARY REACH (weight side): T0 = sqrt(v1
v2) sum_j v_j K(y1, y_j) K(y2, y_j) -- the weight factors v_j are
replaced by the r342 digamma/tent prediction v_pred(theta_j)
(PX.v_predict verbatim) with the kernel rows measured: the sealed
sample census DICT_T0 (the weight side of the overlap products is
dictionary-explicit iff the median deviation over the six sample
rungs is <= 0.10; the kernel side stays census-grade -- r342
negative #4, never upgraded).

INDEX FIREWALL (binding, r238-r347 discipline): w = window (kz
into the prime-power list), S = #union atoms, S_- = #nu atoms,
N_w = (S+1)//2; ground truth (r283/r284/r286/r329/r334/r342/r343/
r345/r347 records, control flips, kappa_int records) enters GATES
and record tables only; the module-own constructors consume kernel
Gram / spectrum / weight / position arrays and measured columns
ONLY (AST scope audit; withheld identifiers are the RECORD values
DELTA_REC and the verdict-side columns); no zero/prime oracles
anywhere (AST firewall; the prime-power grid is the sealed source
comb, r238 convention); no fit primitives (fragment audit; fits
are the imported r286 Theil-Sen; the flat protocol is the imported
r345 curvflat_protocol with its module-sealed constants; the decay
instrument is the imported r347 decay_law).  MACHINERY IMPORTED
VERBATIM: r342 PX.{build_rung, pair_select, pair_eigs,
det_reserve, schur_dress, v_predict, layer_split} (b09f8ccd), r343
PC3.extend_rung (9ffc2705), r345 GR.{curvflat_protocol,
mirror_profile} (1f99235a), r347 DA.{closure_cols, decay_law,
mirror_world_row} (bd1aa7f3), r330 DSW.{dirichlet_comb,
dirichlet_abs_comb} (66526018), document pipeline
V.{build_measures, mu_chain, b_matrix, admissible_indices,
lam_max_at, U, W_VM, PP}, r286 LM.{ts_fit, ts_slope_free,
ext_rule}, r334 FC.{world_from_arrays, world_from_mz,
interval_census}, r278 MS.ctx_build, r280 BL.{union_of_ctx,
sign_chain_f64}, v881 PIK.lambda_eps, r243 PB.smooth_comb,
paircorr PC.{Grid, gen_model}, r331 TR.{base_comb, build_world},
r289 AKD.twin_rational, r276 MF.local_gaps, v563 core READ-ONLY.

LEG 0 -- ANCHORS BIT-NEAR (r342/r343/r345/r347 record numbers as
gates): w9 records (S 367, N_w 184, lambda 0.99983248, margin
1.6752e-4); the r347 w9 closure row (d1' 0.999154, d2' 0.998710,
c' 8.7234e-4, r'_det 0.302916, lambda_rest 0.996338, p' 8.4606e-4,
q' 1.2903e-3, m2' 1.6800e-4, bridge 1.0029, c'/c 2.7047e-2, g21
7.517, K_res 2, rho_32 0.9225); the r345 w9 mirror anchors (rho_0
0.5787, M90 27, top-1 mode share 0.190); the r345 cohort medians
(rho_0 0.839, M90 30, top-1 0.275) and the r343 bridge median
1.0058; the r342/r345/r347 fit slopes (margin -3.332, c -0.697, p
-0.754, q -0.645, |c'/c| -2.668, |c'| -3.401, p' -3.422, q'
-3.359, p'/p -2.609, q'/q -2.665) and curvatures (cpc -0.189,
margin -0.347, c +0.308) as DISCLOSED PRIORS; the r343 sealed
EXT3/EXT4 selections adopted AS-IS; the r334/r345 kappa_int
records and control flips.

LEG A -- THE ORDER-0 ANATOMY (sealed clauses): the split identity
T0 + T+ == Delta c at SPLIT_BAR 1e-9 (backward-error scale) and
the bookkeeping identity c'/c == y0 - rho_hi at CPC_ID_BAR 1e-6
per rung on all 75 rows; THE ORDER-0 MISS LAW: sealed r347
decay_law fit of log|y0| vs log N_w on the 57 with halves
curvature and the EXT3/EXT4 band pure tests; ORDER0_LAW iff
|curv| <= 0.35 AND EXT3 in-band >= 10/12 AND EXT4 n_low <= 1 AND
delta_0 >= DELTA0_MIN = 0.3; ORDER0_CARRIES_DELTA iff additionally
|delta_0 - delta| <= CARRY_BAR = 0.5 (the r347-sketch hypothesis
'does u1.u2/c alone already carry the N^-2.67 law?' -- adjudicated
symmetrically); rho_hi gets the same instrument as CENSUS (no
clause -- the s1 scoping shows y0 and rho_hi are BOTH slow ~N^-0.6
and their DIFFERENCE is the c'/c law: the delta cancellation is an
INTER-ORDER near-cancellation, the same motif as the pair itself,
measured by the depth census |c'/c|/y0); the mode census columns
and the sealed DICT_T0 sample clause (bar 0.10, six sample rungs).

LEG B -- THE RATE-EQUALITY CANDIDATE (sealed clauses): toys
(T1) the two-level dressed-scalar identity EXACT in Fractions on
the rank-2 rational model (lam 9/10, 3/10; vectors 3/5, 4/5 --
p' = 121/250, q' = 79/250, c' = 72/250 by hand) AND through the
FULL Schur chain on the block-spectral 4x4 at 1e-12, AND the
two-level reserve cross-tie r'_2 = 1 - c'_2^2/(p'_2 q'_2) ==
4375/9559 == the r345 formula; (T2) the rate toys: a flat-geometry
synthetic family recovers delta_x = alpha - a_x at RATE_TOL 1e-9
with dressed-slope spread 0 (equality HOLDS iff a_p == a_q == a_c,
and an unequal-rate family breaks it by EXACTLY the bare spread);
an angle-drift family (t2 ~ N^tau, tau 0.4) breaks the dressed-
slope equality by >= DRIFT_MIN 0.2 -- the flat-geometry hypothesis
is load-bearing; LIVE (the certificate side, all sealed): (E1)
CURV_FLAT on ALL THREE margin-pinning ratios p'/margin, q'/margin,
|c'|/margin (r345 protocol verbatim over all 75 arbitrated rows);
(E2) the two-level truncation census: median over the 57 of
max(sh_p, sh_q, sh_c) <= SHADOW_MED_BAR 0.20 (sh_x = |x'_2/x' -
1|); (E3) sign agreement of c'_2 with c' on >= SGN_MIN 73 of 75;
(E4) the fitted image of the theorem: max_x |delta_x - (alpha_meas
- a_x)| <= UNIV_BAR 0.1 for x in {p, q, c} (delta_p/delta_q/delta
= the sealed p'/p, q'/q, |c'/c| fits; a_x = the bare fits) -- the
r347 universality census upgraded to the exact prediction
delta_x = alpha - a_x.

LEG C -- THE DECOMPOSITION (sealed): the r347 C4 closure re-gated
(|alpha - (a_c + delta)| <= CLOSURE_BAR 0.1) and TYPED: delta ==
alpha - a_c where the two-level skeleton (exact algebra) plus the
certified margin-pinning flats carry the reduction, alpha and a_c
stay FIT-CENSUS laws (weight side of the bare scalars closed-form,
r342) -- the irreducible measured rest of the L* margin law after
this round is the PAIR {alpha, a_c} (equivalently {alpha, delta}),
one exponent fewer than r342's three, zero new exponents beyond
r347, but delta itself loses its independent-law status if Leg B
certifies; honesty: alpha has NO source derivation
(ALPHA_SOURCE_CLOSED_FORM sealed False -- the DELTA_SOURCE_DERIVED
clause exists so the enum is complete).

LEG D -- WORLDS + TWIN + WEAK RUNGS (sealed): the r347 mirror
world rule re-gated verbatim (8 worlds MAIN/TWIN/EPST/SCR/SMOOTH/
HL2/DIR/ABS; live iff lambda_rest < 1 AND |rho_32 - 1| <= 0.5)
with the NEW order-0 world column rho_0 printed (census, no bar --
the order-0 sum is finite on every world); the rational twin ward
on the new columns (rho_0, y0, shadow devs, T0) at TWIN_BAR 1e-3;
THE WEAK FAMILY: KZ_WEAK = (28, 44, 59) -- the r345 kill-census
suspects (kz28 worst two-level dev 0.4192, kz44 rest-pair-mass
argmin, kz59 pair-mass argmin) as their own row family with
columns (rho_0, sh_p/q/c, K_res, masses); sealed clause:
WEAK_FAMILY_STRAINED iff the median over the family of max(sh_x)
> WEAK_BAR 0.35, else WEAK_FAMILY_SURVIVES (printed per row).

LEG E -- MUST-FAILS (>= 5, each loud): (m1) THE WRONG RESOLVENT
WEIGHT: the enhancement with delta/(1+delta) instead of
delta/(1-delta) -- breaks the exact split identity by >= 0.1 rel
at w9 and >= 1e-6 on the hand toy; exactly CAUGHT.  (m2) MODE
SELECTION AFTER SIGHT: the census quantile re-picked from the seen
share column -- consumes the withheld column; AST-FLAGGED, and the
toy value differs from the sealed M90_Q.  (m3) DELTA_0 READ BACK
from the withheld record exponent -- AST-FLAGGED.  (m4) A
SYNTHETIC MODEL WITH BUILT-IN TARGET: a mutant family planting the
withheld record exponent -- AST-FLAGGED, and the sealed toy
exponents differ from the record value by construction
(construction-CAUGHT).  (m5) THE TWO-LEVEL FORMULA WITH THE WRONG
COUPLING SIGN (g21 a1 a2 - b1 b2) -- breaks c'_2 by >= 0.1 rel
against its own right-sign value at w9 and by 1/3 exactly on the
rational toy.  STOP LIST (anti-gates, binding): NO L* claim, NO
bound mechanism promoted, NO certificate reading of any census, NO
posthoc bar / band / family / prior move, NO derived 5/7, NO RH
claim, mincut unchanged; r243..r347 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN 1.6752e-4
rel 0.01; PX_SHA b09f8ccd; PC3_SHA 9ffc2705; GR_SHA 1f99235a;
DA_SHA bd1aa7f3; DSW_SHA 66526018; W9 ANCHORS d1p 0.999154 rel
1e-5 / d2p 0.998710 rel 1e-5 / cp 8.7234e-4 rel 1e-3 / rdetp
0.302916 rel 1e-3 / lam_rest 0.996338 abs 1e-5 / ppr 8.4606e-4
rel 1e-3 / qpr 1.2903e-3 rel 1e-3 / m2p 1.6800e-4 rel 1e-3 /
bridge 1.0029 abs 5e-3 / cpc 2.7047e-2 rel 1e-3 / g21 7.517 abs
0.01 / kres 2 / rho32 0.9225 abs 5e-3; W9 S1 ANCHORS (this
round's scoping) rho0 0.5787 abs 5e-3 / y0 0.42134 abs 5e-3 /
rho_hi 0.39430 abs 5e-3 / sh_p 0.0537 abs 5e-3 / sh_q 0.0577 abs
5e-3 / sh_c 0.0667 abs 5e-3 / t0arch 0.8474 abs 5e-3 / dict_t0
0.195 abs 0.01 / pm 5.0506 abs 0.05 / qm 7.7025 abs 0.05 / cm
5.2075 abs 0.05 / top1 0.190 abs 5e-3 / m90 27 abs 2; SAMPLE
ANCHORS rho0 (kz44 0.8290, kz56 0.8982, kz130 0.9169) abs 5e-3,
sh_p (0.1142, 0.1130, 0.0487) abs 5e-3; MED ANCHORS rho0 0.839
abs 0.01 / m90 30 abs 2 / top1 0.275 abs 0.01 / bridge 1.0058 abs
5e-3; FIT ANCH (margin -3.332, c -0.697, p -0.754, q -0.645, cpc
-2.668, cp -3.401, ppr -3.422, qpr -3.359, fp -2.609, fq -2.665)
tol 0.02; CURV ANCH (cpc -0.189, margin -0.347, c +0.308) tol
0.03; DELTA_REC 2.668 (WITHHELD record constant -- gates and m3/m4
only); EXT3_KZ_B (42, 51, 54, 56, 58, 62); EXT3_KZ_A (96, 123,
125, 127, 128, 130); EXT3_NW (1721, 2577); EXT4_KZ_B (72, 75,
66); EXT4_KZ_A (113, 111, 108); EXT4_NW (2656, 3181) (r343 sealed
selections AS-IS); SPLIT_BAR 1e-9; CPC_ID_BAR 1e-6; ID_BAR 1e-8;
RDEF_BAR 1e-12; SHADOW_MED_BAR 0.20; SGN_MIN 73; UNIV_BAR 0.1;
CLOSURE_BAR 0.1; DELTA0_MIN 0.3; CARRY_BAR 0.5; DEC_CURV_BAR
0.35; DEC_EXT3_MIN 10; DEC_EXT4_LOW 1; M90_Q 0.9; DICT_T0_BAR
0.10; KZ_WEAK (28, 44, 59); WEAK_BAR 0.35; MIRROR_LIVE_BAR 0.5
(via the r347 rule verbatim, MIRROR_K 32 in DA); ALPHA_SOURCE_
CLOSED_FORM False (sealed); TOY RATE FAMILY (N0 200, ratio 1.25,
20 points; TOY_ALPHA 3.3, TOY_AP 0.75, TOY_AQ 0.63, TOY_RC 0.7 =>
a_c 0.69, TOY_G21 7.5, TOY_A1 0.6, TOY_A2 0.78, TOY_T1 -0.55,
TOY_T2 1.05, TOY_TAU 0.4, RATE_TOL 1e-9, DRIFT_MIN 0.2);
SAMPLE_KZ (18, 9, 52, 119, 42, 130); KINT RECORDS {EPST 1793.99,
SCR 8.51e6, SMOOTH 2.193, HL2 1964} rel 0.05, live 0.999567 rel
1e-3; CTRL_FLIPS {EPST 25, SCR 21, SMOOTH 27}, HL2 seed 101 flip
25; EXT 8; TWIN_TOL 1e-8; TWIN_BAR 1e-3; M1_BAR 0.1; M5_BAR 0.1;
MUT_MIN 1e-6; TOY_TOL 1e-12; runtime <= 1800 s; smoke = toys +
firewall + scopes + mutants + w9 block (records, dressed anchors,
order-0 split live, two-level shadows live, mode census +
dictionary); ladder, twin, fits, protocols, laws, decomposition,
weak family, worlds and adjudication skipped.

PRE-SPEC SCOPING (disclosed, r343-s1/r345-s1/r347-s1 precedent --
no bar, band, threshold, family or adjudication rule was tuned
after any evaluation except as sized here and said so): (s1) FOUR
sample rungs (kz9, kz44, kz56, kz130 -- all four already printed
in the r342/r343/r345/r347 records) were probed end-to-end for
machinery and bar sizing: the order-0 split identity residual
spans 4.9e-15 .. 2.0e-14 (sizing SPLIT_BAR 1e-9); rho_0 = 0.5787 /
0.8290 / 0.8982 / 0.9169 with y0 = 1 - rho_0 = 0.4213 / 0.1710 /
0.1018 / 0.0831 and rho_hi = 0.3943 / 0.1706 / 0.1018 / 0.0831 --
y0 and rho_hi are BOTH slow (naive two-point slopes -0.615 /
-0.590) while their difference c'/c falls at -3.406: THE DELTA LAW
IS AN INTER-ORDER NEAR-CANCELLATION (the sizing observation behind
DELTA0_MIN 0.3 and the CARRY clause; the expected reading is that
order-0 alone does NOT carry delta); two-level dressed-scalar
shadow devs 0.049 .. 0.130 with sign agreement 4/4 (sizing
SHADOW_MED_BAR 0.20, SGN_MIN 73); mode census top-1 0.177..0.297,
M90 27..38, T0 arch-rim atom share 0.844..0.950, top carrying
MODE arch mass 0.157..0.286 and peel-pair mass 0.007..0.014 (the
carriers are NOT the peel-concentrated top rest mode -- disclosed,
re-measured ladder-wide below); dictionary T0 surrogate devs
0.195 (w9) / 0.048 / 0.004 / 0.006 -- depth-improving, w9 is the
honest worst (sizing DICT_T0_BAR 0.10 on the sample median,
sealed symmetric GO/census); margin-pinning ratios p'/m 3.89..
9.13, q'/m 7.70..17.73, |c'|/m 5.21..11.66 (spans 0.35..0.37
decades over the four rungs -- flat O(1) columns with ~x2.3
scatter: exactly the r345 protocol's object class); (s2) the rate
toys were sized: the flat-geometry family recovers delta_x =
alpha - a_x with dressed-slope spread 0.0 (exact powers), the
tau = 0.4 angle-drift family separates the dressed slopes by
0.453 (sizing DRIFT_MIN 0.2); (s3) the rank-2 Fractions model was
solved by hand (p' 121/250, q' 79/250, c' 72/250, r'_2 4375/9559)
-- the toy gates are exact-value gates.  Runtime scoping 5.5 s
total for the four rungs + toys; the full run is sized under the
1800 s bar (the r345 ladder pass with the same extend_rung is
62 s).  No ladder-wide fit, median, protocol clause or law was
evaluated before this spec froze; the slopes cited above are
published record numbers or the disclosed two-point scoping
values, never sealed-fit previews.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > DELTA_SOURCE_DERIVED >
RATE_EQUALITY_THEOREM > ORDER0_LAW_FOUND > DELTA_IRREDUCIBLE --
the enum is exhaustive):
  [exactly one of]
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  DELTA_SOURCE_DERIVED  iff the RATE_EQUALITY clauses fire AND
    ALPHA_SOURCE_CLOSED_FORM (sealed False this round: alpha has
    no source derivation -- the clause exists so the enum is
    complete and honest) /
  RATE_EQUALITY_THEOREM(refined statement, clauses)  iff toys T1 +
    T2 are exact AND E1 (CURV_FLAT on all three margin-pinning
    ratios) AND E2 (shadow median <= 0.20) AND E3 (sign >= 73/75)
    AND E4 (max_x |delta_x - (alpha - a_x)| <= 0.1) -- the common
    dressing rate IS the margin rate (theorem-grade skeleton on
    the small models, certified census live); the naive delta_p ==
    delta_q == delta is typed as its corollary UP TO the bare-rate
    spread, exactly /
  ORDER0_LAW_FOUND(delta_0)  iff not RATE_EQUALITY and the y0 law
    clauses hold /
  DELTA_IRREDUCIBLE(failed clauses)  otherwise -- delta resists
    the decomposition; the specialist question is final-sharpened
  + [exactly one of] ORDER0_LAW(delta_0; CARRIES_DELTA yes/no) /
    ORDER0_CENSUS(numbers)  [always -- the Leg A adjudication,
    printed additively when RATE_EQUALITY outranks it]
  + [exactly one of] DICT_T0_GO(median) / DICT_T0_CENSUS(medians,
    w9 worst)  [always]
  + [exactly one of] WEAK_FAMILY_SURVIVES / WEAK_FAMILY_STRAINED
    [always]
  + [exactly one of] MIRROR_WORLD_CLAUSE_SEALED(live 2/2, dead
    4/4, Dirichlet typed) / MIRROR_WORLD_INCOMPLETE(loci)
    [always]
  + DECOMP_LEDGER(alpha, a_c, delta, delta_0, C4 re-gate, the
    delta_x = alpha - a_x residuals, block typing, the named
    irreducible rest) [always]
  + ORDER0_LEDGER(y0/rho_hi laws, split identities, cancellation
    depth census) [always]
  + MODE_CENSUS_LEDGER(top-1/M90/arch/peel columns, dictionary
    sample) [always]
  + WEAK_LEDGER(per-row table) [always]
  + WORLD_LEDGER(lambda_rest separation, kappa_int anchors,
    mirror + rho_0 columns incl. DIR/ABS) [always]
  + TWIN_LEDGER(order-0 and shadow deviations) [always]
  + MUSTFAIL_LEDGER(m1-m5 + scopes) [always].
Honesty before beauty: the order-0 split and the two-level
dressed-scalar identity are exact finite-matrix facts
(theorem-grade SKELETON) whose inputs are measured window scalars
(census-grade FLESH); the rate-equality certificate is a sealed
census protocol on 75 finite windows, never an asymptotic theorem
-- its theorem-grade half lives on the synthetic small models
where the hypotheses (top-2 dominance, flat geometry) are exact;
delta_0, delta and alpha remain measured laws (fit-census with
sealed honesty meters); a reduction delta == alpha - a_c moves the
open analytic remainder, it does not close it: alpha and a_c stay
unexplained from the source (the kernel side has no closed form,
r342 negative #4); the mirror world clause is a measured
discriminator on eight instrumented worlds; no verdict claims L*,
a bound mechanism, a derived 5/7, or RH progress in any direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit, which IS the protocol; TWO-COMMIT PROTOCOL
EXECUTED: the sealed spec above was committed as "r348 pre-freeze"
(0d0849e6, SPEC_SHA freeze b43a635184c44d3c) BEFORE the first full
evaluation; chronology honest: smoke pass 1 = 34/34 (0.2 s) at the
sealed rules, NO amendment; smoke pass 2 byte-identical;
pre-freeze commit 0d0849e6; calibration pass 1 = FIRST full
evaluation = 34/34 (63.0 s), NO amendment; record run1 = 34/34
(63.6 s), run2 = 34/34 (63.5 s), byte-identical up to WALL and
identical to the calibration pass):
MAIN VERDICT = RATE_EQUALITY_THEOREM -- THE COMMON DRESSING RATE
IS THE MARGIN RATE: the theorem-grade skeleton (T1 the two-level
dressed-scalar identity, EXACT in Fractions on the rank-2 model
(p' 121/250, q' 79/250, c' 72/250; cross-tie r'_2 = 4375/9559 ==
the r345 formula at 2.2e-16) and through the FULL Schur chain on
the block-spectral 4x4 at 1.7e-16; T2 the rate toys: flat
geometry forces delta_x = alpha - a_x EXACTLY (Theil-Sen dev 0 at
1e-9, dressed-slope spread 4.4e-16) -- the naive delta_p ==
delta_q == delta holds IFF a_p == a_q == a_c and breaks by
EXACTLY the bare spread otherwise; the tau = 0.4 angle drift
separates the dressed slopes by 0.453: flat geometry is
load-bearing) carries LIVE as certified census on all four sealed
clauses: E1 CURV_FLAT passes on ALL THREE margin-pinning ratios
(p'/m slope -0.056 CI [-0.90, +0.74], 0 out / 0 hard of 75, max
0.323 dec; q'/m slope +0.016 CI [-0.89, +0.92], 0/0, max 0.365;
|c'|/m slope -0.025 CI [-1.03, +0.97], 0/0, max 0.400 -- every
dressed scalar is pinned to the margin scale across the whole
arbitrated ladder), E2 the two-level truncation census holds
(median max-shadow 0.0879 <= 0.20 on the 57), E3 sign agreement
75/75, E4 the fitted image of the theorem holds (delta_x -
(alpha - a_x): p +0.031 / q -0.023 / c +0.033, max 0.033 <= 0.1)
-- THE R347 UNIVERSALITY CENSUS IS UPGRADED TO ITS EXACT FORM:
the common rate is alpha, the delta_x differ by exactly the
bare-rate spread (naive |delta_p - delta| 0.059 / |delta_q -
delta| 0.003 vs bare |a_p - a_c| 0.056 / |a_q - a_c| 0.053), and
delta LOSES ITS INDEPENDENT-LAW STATUS: delta == alpha - a_c
through the two-level skeleton plus the certified pinning flats
+ ORDER0_LAW(delta_0 = 0.401 -- the ORDER-0 MISS y0 = 1 - rho_0
carries its own sealed slow law (curv +0.094, EXT3 12/12 low 0,
EXT4 6/6 low 0, delta_0 0.401 >= 0.3), and CARRIES_DELTA does NOT
fire: |delta_0 - delta| = |0.401 - 2.668| = 2.267 > 0.5 -- THE
R347-SKETCH HYPOTHESIS IS REFUTED CLEANLY: u1.u2/c alone does not
carry the N^-2.67 law; the delta law is an INTER-ORDER
NEAR-CANCELLATION: y0 (slope -0.401) and rho_hi (slope -0.393,
curv +0.080, EXT3 12/12, EXT4 6/6) are twin slow laws whose
difference is the c'/c column, pinned to the margin scale by the
resolvent -- the same two-slow-scalars motif as the pair margin
itself, one level down; cancellation depth |c'/c|/y0 median
1.48e-3: the higher orders cancel 99.85 percent of the order-0
miss at the median)
+ DICT_T0_GO(median 0.0177 <= 0.10 over the six sample rungs
(kz18 0.0560, kz9 0.1949, kz52 0.0183, kz119 0.0171, kz42 0.0024,
kz130 0.0059) -- the WEIGHT side of the order-0 overlap products
IS dictionary-explicit (r342 digamma/tent v_pred inside the
measured kernel rows), w9 the honest worst at 0.195, depth-
improving; the kernel side stays census-grade, r342 negative #4
never upgraded)
+ WEAK_FAMILY_STRAINED(median max-shadow 0.3772 > 0.35 on
kz28/kz44/kz59 -- the honest Leg D negative: the two-level SCALAR
shadows break at weak concentration (kz28 sh 0.7459/0.8231/
0.9082 with K_res 3, mass2 0.9942; kz44 0.1142/0.1211/0.1303,
K_res 3, mass2 0.6917; kz59 0.2580/0.3268/0.3772, K_res 3, pmass
0.9352), signs still agree 3/3 -- K = 2 is a MEDIAN instrument on
the scalars, not a per-row one; the ladder-wide clauses survive
via the median (0.0879) with the worst arbitrated row kz23 at
4.06 (N_w 149, K_res 3: the truncation fails locally there while
the sign and the pinning ratios stay in band -- printed, typed))
+ MIRROR_WORLD_CLAUSE_SEALED(live 2/2: MAIN/TWIN lambda_rest
0.996338 < 1, rho_32 0.9225, |rho_32 - 1| = 0.078 <= 0.5; dead
4/4 diverge; DIRICHLET typed DEAD-side: DIR lambda_rest 3.97e37
series NONFINITE, ABS 2.28e5 series -3.85e176 -- the r347 typing
reproduced bit-near; NEW rho_0 WORLD COLUMN (census, no bar):
live 0.5787/0.5787 vs dead EPST -220 / SCR -1.06e6 / SMOOTH
+1.76 / HL2 -3.05e3, DIR -3.975e37 / ABS -1.425e5 -- the ORDER-0
quota alone separates live (0.58, positive, below 1) from dead
by SIZE OR SIGN on 5 of 6 std worlds; SMOOTH sits at +1.76, same
sign wrong size -- magnitude census, honest)
+ DECOMP_LEDGER(alpha 3.332, a_c 0.697, delta 2.668, delta_0
0.401; C4 re-gate |3.332 - 3.366| = 0.033 <= 0.1; theorem-image
residuals p +0.031 / q -0.023 / c +0.033; BLOCK TYPING: order-0
split + two-level identity THEOREM-GRADE (Fractions exact, f64
split max 5.8e-14, bookkeeping max 3.6e-8 on 75/75),
margin-pinning flats + shadow median + sign CERTIFIED CENSUS (0
band violations), alpha and a_c FIT-CENSUS laws (weight side
closed-form: DICT_T0_GO here, v_pred 9.0e-4 r342) -- THE
IRREDUCIBLE MEASURED REST OF THE L* MARGIN LAW IS THE PAIR
{alpha, a_c}: delta is reduced to alpha - a_c, and the typed
specialist question shifts from 'why does the rest space mirror
at rate 2.67' to 'why alpha = 3.33 and a_c = 0.70 from the
source')
+ ORDER0_LEDGER(split identity max 5.8e-14 of 75 (bar 1e-9);
c'/c == y0 - rho_hi max 3.6e-8 (bar 1e-6); y0 fit slope -0.401 /
curv +0.094 / EXT3 12/12 / EXT4 6/6; rho_hi -0.393 / +0.080 /
12/12 / 6/6; depth census median 1.48e-3)
+ MODE_CENSUS_LEDGER(medians on the 57: top-1 share 0.2746, M90
30, T0 arch-rim ATOM share 0.8158, top-mode arch mass 0.2061,
top-mode peel-pair mass 0.0142 -- the mirror carriers are
DELOCALIZED rest modes; in ATOM terms the order-0 overlap is 82
percent arch-rim, in MODE terms no single carrier: the r345
multi-modality restated with named coordinates)
+ WEAK_LEDGER(kz28 rho_0 0.8426 sh 0.7459/0.8231/0.9082 Kres 3
mass2 0.9942 pmass 0.9800; kz44 0.8290, 0.1142/0.1211/0.1303, 3,
0.6917, 0.9916; kz59 0.8201, 0.2580/0.3268/0.3772, 3, 0.9883,
0.9352)
+ WORLD_LEDGER(lambda_rest separation re-gated 4/4 dead >= 1 vs
live 0.996338 < 1; kappa_int == records at 5 percent (EPST
1793.99 / SCR 8.509e6 / SMOOTH 2.193 / HL2 1964.35, live
0.999567); 8 instrumented worlds, the rho_0 column new)
+ TWIN_LEDGER(rho_0 dev 9.9e-9, y0 dev 1.4e-8, T0 dev 2.0e-8,
shadow devs <= 9.6e-7, margin-ratio devs <= 1.2e-5 (bar 1e-3);
dose-zero identity BITWISE)
+ MUSTFAIL_LEDGER(m1 wrong resolvent weight breaks the split by
3.2e-01 >= 0.1 at w9 + 2.8e-02 >= 1e-6 on the hand toy; m2
AST-FLAGGED share_col_true + toy quantile 0.50 != the sealed
0.9; m3 AST-FLAGGED DELTA_REC; m4 AST-FLAGGED DELTA_REC + the
sealed toy exponent 2.610 differs from the record readback 2.668
by 0.058 >= 0.01 (construction-CAUGHT); m5 wrong coupling sign
breaks c'_2 by 1.7e-01 >= 0.1 at w9 and 3.3e-01 (exact 1/3) on
the rational toy; constructor scopes + fragment audit CLEAN).
Key numbers.  W9: rho_0 0.5787, y0 0.4213, rho_hi 0.3943, c'/c
2.7047e-2 == y0 - rho_hi (dev 1.0e-13); shadows sh_p/q/c 0.0537/
0.0577/0.0667 (sign +); ratios p'/m 5.0506, q'/m 7.7025, |c'|/m
5.2075; top-1 0.1899, M90 27, t0arch 0.8474, dict_t0 0.1949 ==
the s1 scoping bit-near; the r347 closure row reproduced (bridge
1.0029, g21 7.5175, K_res 2, rho_32 0.9225).  LADDER: 75 rows,
every f64 margin positive; cohort medians rho_0 0.8392 (r345
0.839), M90 30 (== r345), top-1 0.2746 (== r345 0.275), bridge
1.0058 (== r343); FIT ANCHORS margin -3.332 / c -0.697 / p
-0.754 / q -0.645 / cpc -2.668 / cp -3.401 / p' -3.422 / q'
-3.359 / fp -2.609 / fq -2.665 all == the disclosed priors at
tol 0.02; curvatures cpc -0.189 / margin -0.347 / c +0.308 at
tol 0.03.  HONEST NEGATIVES: (1) the order-0 hypothesis of the
r347 sketch is REFUTED: delta_0 = 0.401 is not delta = 2.668
(gap 2.267) -- the direct overlap does not carry the
cancellation law; what carries it is the RESOLVENT PINNING of c'
to the margin scale, and the order-0 miss is one of two twin
slow laws whose difference is delta; (2) WEAK_FAMILY_STRAINED
fires: the two-level scalar shadows break at weak concentration
(kz28 up to 0.91; worst arbitrated row kz23 at 4.06) -- the
truncation census is a median statement (0.0879), K = 2 is NOT a
per-row instrument on the scalars, said with numbers; (3) the
RATE_EQUALITY certificate is a sealed census on 75 finite
windows, never an asymptotic theorem -- its theorem-grade half
lives on the small models where top-2 dominance and flat
geometry are exact hypotheses; live they are measured
certificates; (4) alpha and a_c remain UNDERIVED from the
source: the round reduces delta to alpha - a_c, it does not
close the lane (DELTA_SOURCE_DERIVED cannot fire,
ALPHA_SOURCE_CLOSED_FORM sealed False); (5) the rho_0 world
column separates by size-or-sign on only 5 of 6 std dead worlds
(SMOOTH +1.76 has the live sign at the wrong size) -- census, no
bar was sealed for it; (6) the w9 dictionary deviation 0.195 is
the honest sample worst (shallow window) -- the GO clause is a
median statement over the sealed sample, not a per-rung bound.
R349 SKETCH (candidates, not commitments): (i) the ALPHA source
anatomy -- with delta == alpha - a_c and the weight side
closed-form, the margin exponent is the LAST unexplained rate of
the lane: the r338 specialist package (q1 backward-CS, q2
sub-classical Christoffel growth 0.38, q3 resolution paradox) is
now one exponent thinner; (ii) the y0 slow law delta_0 ~ 0.4 as
its own object: does it tie to the bare rates (a_p + a_q - a_c ~
0.7? the coupling-row geometry?) or to the g21 gap -- a
shared-curvature ward between y0 and the margin column would tie
order zero to the spectrum; (iii) the GRH-faithful Dirichlet
frame (U5) stays the named separate follow-up.  Runtime 63.6 /
63.5 s record, 63.0 s calibration, 0.2 s smoke; deterministic,
run1/run2 byte-identical up to WALL.  AMENDMENTS AFTER FREEZE:
NONE except this record-table insertion.

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

import pair_extremal_probe as PX                 # noqa: E402 r342
import pair_coupling_probe as PC3                # noqa: E402 r343
import gap_ratio_primary_probe as GR             # noqa: E402 r345
import delta_alpha_closure_probe as DA           # noqa: E402 r347
import dirichlet_secondworld_probe as DSW        # noqa: E402 r330
import verify_lstar_instance as V                # noqa: E402 document
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import fold_capacity_probe as FC                 # noqa: E402 r334
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import paircorr_margin_probe as PC               # noqa: E402
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
PX_SHA_PREFIX = "b09f8ccd"
PC3_SHA_PREFIX = "9ffc2705"
GR_SHA_PREFIX = "1f99235a"
DA_SHA_PREFIX = "bd1aa7f3"
DSW_SHA_PREFIX = "66526018"
W9_ANCH = dict(d1p=0.999154, d2p=0.998710, cp=8.7234e-4,
               rdetp=0.302916, lam_rest=0.996338,
               ppr=8.4606e-4, qpr=1.2903e-3, m2p=1.6800e-4,
               bridge=1.0029, cpc=2.7047e-2, g21=7.517, kres=2,
               rho32=0.9225)
S1_ANCH = dict(rho0=0.5787, y0=0.42134, rho_hi=0.39430,
               sh_p=0.0537, sh_q=0.0577, sh_c=0.0667,
               t0arch=0.8474, dict_t0=0.195,
               pm=5.0506, qm=7.7025, cm=5.2075,
               top1=0.190, m90=27)
SAMPLE_ANCH = {44: dict(rho0=0.8290, sh_p=0.1142),
               56: dict(rho0=0.8982, sh_p=0.1130),
               130: dict(rho0=0.9169, sh_p=0.0487)}
MED_ANCH = dict(rho0=0.839, m90=30, top1=0.275, bridge=1.0058)
FIT_ANCH = dict(margin=-3.332, c=-0.697, p=-0.754, q=-0.645,
                cpc=-2.668, cp=-3.401, ppr=-3.422, qpr=-3.359,
                fp=-2.609, fq=-2.665)
FIT_ANCH_TOL = 0.02
CURV_ANCH = dict(cpc=-0.189, margin=-0.347, c=0.308)
CURV_ANCH_TOL = 0.03
DELTA_REC = 2.668            # WITHHELD record constant
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
SPLIT_BAR = 1.0e-9
CPC_ID_BAR = 1.0e-6
ID_BAR = 1.0e-8
RDEF_BAR = 1.0e-12
SHADOW_MED_BAR = 0.20
SGN_MIN = 73
UNIV_BAR = 0.1
CLOSURE_BAR = 0.1
DELTA0_MIN = 0.3
CARRY_BAR = 0.5
DEC_CURV_BAR = 0.35
DEC_EXT3_MIN = 10
DEC_EXT4_LOW = 1
M90_Q = 0.9
DICT_T0_BAR = 0.10
KZ_WEAK = (28, 44, 59)
WEAK_BAR = 0.35
MIRROR_LIVE_BAR = 0.5
ALPHA_SOURCE_CLOSED_FORM = False   # sealed: alpha has no source form
TOY_N0 = 200.0
TOY_RATIO = 1.25
TOY_NPTS = 20
TOY_ALPHA = 3.3
TOY_AP = 0.75
TOY_AQ = 0.63
TOY_RC = 0.7
TOY_G21 = 7.5
TOY_A1 = 0.6
TOY_A2 = 0.78
TOY_T1 = -0.55
TOY_T2 = 1.05
TOY_TAU = 0.4
RATE_TOL = 1.0e-9
DRIFT_MIN = 0.2
SAMPLE_KZ = (18, 9, 52, 119, 42, 130)
KINT_REC = {"EPST": 1793.99, "SCR": 8.51e6, "SMOOTH": 2.193,
            "HL2": 1964.0}
KINT_REC_TOL = 0.05
KINT_LIVE_REC = 0.999567
KINT_LIVE_TOL = 1.0e-3
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
EXT = 8
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
M1_BAR = 0.1
M5_BAR = 0.1
MUT_MIN = 1.0e-6
TOY_TOL = 1.0e-12

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
                       "constructors consume kernel Gram / spectrum "
                       "/ weight / position arrays and measured "
                       "columns ONLY; record numbers and flips "
                       "enter gates and record tables only"
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


CONSTRUCTORS = ("order0_split", "two_level_dressed", "mode_census",
                "dict_t0_dev")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "KINT_REC", "FIT_ANCH",
                   "CURV_ANCH", "W9_ANCH", "S1_ANCH", "MED_ANCH",
                   "SAMPLE_ANCH", "DELTA_REC", "share_col_true"}


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
def order0_split(dv, al, be, c):
    """the EXACT order-0 split of the mirror: Delta c = T0 + T+
    with T0 = sum alpha beta (= u1.u2, the direct path) and T+ =
    sum alpha beta delta/(1-delta) (all higher paths); returns the
    quotas rho_0 = -T0/c, rho_hi = -T+/c and the order-0 miss
    y0 = 1 - rho_0; consumes rest-mode arrays only."""
    ab = np.asarray(al, float) * np.asarray(be, float)
    g = 1.0 - np.asarray(dv, float)
    T0 = float(np.sum(ab))
    Tplus = float(np.sum(ab * (np.asarray(dv, float) / g)))
    rho0 = -T0 / c
    rho_hi = -Tplus / c
    return dict(T0=T0, Tplus=Tplus, rho0=rho0, rho_hi=rho_hi,
                y0=1.0 - rho0)


def two_level_dressed(m, g21, a1, a2, b1, b2):
    """the EXACT two-level dressed scalars: with M_2 = mu1 phi
    phi^T + mu2 psi psi^T the top-2 truncation of the resolvent
    pair block and I - A'_2 = M_2^{-1},
      p'_2 = m (g21 a2^2 + b2^2)/Dt^2,
      q'_2 = m (g21 a1^2 + b1^2)/Dt^2,
      c'_2 = m (g21 a1 a2 + b1 b2)/Dt^2,  Dt = a1 b2 - a2 b1;
    consumes spectrum-derived scalars only."""
    Dt = a1 * b2 - a2 * b1
    dt2 = Dt * Dt
    pp2 = m * (g21 * a2 * a2 + b2 * b2) / dt2
    qq2 = m * (g21 * a1 * a1 + b1 * b1) / dt2
    cc2 = m * (g21 * a1 * a2 + b1 * b2) / dt2
    return pp2, qq2, cc2


def mode_census(dv, al, be, WD, m_arch, j1, j2):
    """the mode census of the mirror carriers: L1 profile of the
    terms alpha beta/(1-delta) (top-1 share, M90 at the sealed
    quantile), arch-rim mass and peel-pair mass of the top
    carrying mode; consumes rest-mode arrays + eigenvectors +
    the arch mask only."""
    terms = np.asarray(al, float) * np.asarray(be, float) \
        / (1.0 - np.asarray(dv, float))
    a = np.abs(terms)
    o = np.argsort(a)[::-1]
    tot = float(np.sum(a))
    top1 = float(a[o[0]]) / max(tot, 1e-300)
    m90 = int(np.searchsorted(np.cumsum(a[o]), M90_Q * tot) + 1)
    wt = WD[:, int(o[0])]
    arch_top = float(np.sum(wt[m_arch] ** 2))
    peel_top = float(wt[j1] ** 2 + wt[j2] ** 2)
    return top1, m90, arch_top, peel_top


def dict_t0_dev(u1, u2, vn_rest, vpred):
    """the dictionary reach of the order-0 overlap: T0 with the
    measured weights v_j replaced by the r342 digamma/tent
    prediction (kernel rows measured); returns |T0_pred/T0 - 1|;
    consumes coupling rows + weight arrays only."""
    u1 = np.asarray(u1, float)
    u2 = np.asarray(u2, float)
    T0 = float(u1 @ u2)
    T0p = float(np.sum(u1 * u2 * (np.asarray(vpred, float)
                                  / np.asarray(vn_rest, float))))
    return abs(T0p / T0 - 1.0)


# ============== must-fail mutants
def mutant_wrong_weight(dv, al, be):
    """m1 MUST-FAIL: the resolvent enhancement with the WRONG
    weight delta/(1+delta) -- must break the exact split identity
    loudly."""
    ab = np.asarray(al, float) * np.asarray(be, float)
    d = np.asarray(dv, float)
    return float(np.sum(ab)) + float(np.sum(ab * (d / (1.0 + d))))


def mutant_mode_posthoc(share_col_true):
    """m2 MUST-FAIL: the mode-census quantile re-picked AFTER
    SIGHT to make the seen share column look single-mode --
    consumes the withheld column; AST-FLAGGED."""
    s = sorted(share_col_true, reverse=True)
    tot = sum(s)
    acc = 0.0
    for v in s:
        acc += v
        if acc >= 0.5 * tot:
            break
    return 0.5


def mutant_delta0_readback():
    """m3 MUST-FAIL: 'delta_0' read back from the withheld record
    exponent instead of the sealed fit -- AST-FLAGGED."""
    return DELTA_REC * 0.23


def mutant_toy_plant():
    """m4 MUST-FAIL: a synthetic family planting the withheld
    record exponent as its own -- AST-FLAGGED; the sealed toy
    exponents differ from the record by construction."""
    return DELTA_REC


def mutant_wrong_sign(m, g21, a1, a2, b1, b2):
    """m5 MUST-FAIL: the two-level coupling with the WRONG sign
    (g21 a1 a2 - b1 b2) -- must break c'_2 loudly against its own
    right-sign value."""
    Dt = a1 * b2 - a2 * b1
    return m * (g21 * a1 * a2 - b1 * b2) / (Dt * Dt)


# ============== gate-side helpers
def rung_extras(R, X, C):
    """the r348 extension of one (r342 rung, r343 extension, r347
    closure) triple: order-0 split, two-level dressed shadows,
    margin-pinning ratios, mode census."""
    E, W = X["E"], X["W"]
    i1, i2 = R["i1"], R["i2"]
    rest = X["rest"]
    D, WD = X["D"], X["WD"]
    u1 = E[i1, rest]
    u2 = E[i2, rest]
    al = WD.T @ u1
    be = WD.T @ u2
    dv = np.einsum("ij,ij->j", WD, D @ WD)
    sp0 = order0_split(dv, al, be, R["c"])
    dev_split = abs((sp0["T0"] + sp0["Tplus"]) - X["dc"]) \
        / max(abs(X["dc"]), 1e-300)
    cpc_s = R["cp"] / R["c"]
    dev_cpc = abs(cpc_s - (sp0["y0"] - sp0["rho_hi"])) \
        / max(abs(cpc_s), 1e-300)
    a1, a2 = float(W[i1, -1]), float(W[i2, -1])
    b1, b2 = float(W[i1, -2]), float(W[i2, -2])
    pp2, qq2, cc2 = two_level_dressed(R["margin"], X["g21"],
                                      a1, a2, b1, b2)
    sh_p = abs(pp2 / C["ppr"] - 1.0)
    sh_q = abs(qq2 / C["qpr"] - 1.0)
    sh_c = abs(abs(cc2) / abs(R["cp"]) - 1.0)
    sgn = (cc2 > 0) == (R["cp"] > 0)
    yn_rest = X["yn_rest"]
    L = R["mz"]["L"]
    f_rest = np.round(np.arccos(np.clip(yn_rest, -1.0, 1.0)) * L
                      / (2.0 * math.pi)).astype(int)
    m_arch = (f_rest * R["mz"]["D"]) < math.log(2.0)
    top1, m90, arch_top, peel_top = mode_census(dv, al, be, WD,
                                                m_arch, X["j1"],
                                                X["j2"])
    t0arch = float(np.sum(u1[m_arch] * u2[m_arch])) / sp0["T0"]
    return dict(rho0=sp0["rho0"], rho_hi=sp0["rho_hi"],
                y0=sp0["y0"], T0=sp0["T0"], dev_split=dev_split,
                dev_cpc=dev_cpc, cc2=cc2, sh_p=sh_p, sh_q=sh_q,
                sh_c=sh_c, sh_max=max(sh_p, sh_q, sh_c), sgn=sgn,
                pm=C["ppr"] / R["margin"],
                qm=C["qpr"] / R["margin"],
                cm=abs(R["cp"]) / R["margin"],
                top1=top1, m90=m90, arch_top=arch_top,
                peel_top=peel_top, t0arch=t0arch,
                a1=a1, a2=a2, b1=b1, b2=b2,
                u1=u1, u2=u2, dv=dv, al=al, be=be,
                f_rest=f_rest, rest=rest)


def dict_sample_dev(kz, R, Y):
    """gate-side dictionary sample: v_pred (r342 route verbatim)
    for every rest atom, fed to the audited dict_t0_dev."""
    alpha_, M_, L_, D_, ka_, _dd, _dA, _dP = PX.layer_split(kz)
    uu_ = np.asarray(V.U[:ka_], float)
    mm_ = np.asarray(V.W_VM[:ka_], float)
    vn_rest = np.asarray(R["mz"]["vn"], float)[Y["rest"]]
    vpred = np.empty_like(vn_rest)
    for j in range(len(vn_rest)):
        th = 2.0 * math.pi * float(Y["f_rest"][j]) / L_
        vp, _a, _p = PX.v_predict(th, alpha_, M_, L_, D_, uu_, mm_)
        vpred[j] = vp
    return dict_t0_dev(Y["u1"], Y["u2"], vn_rest, vpred)


def slim(R, X, C, Y):
    """drop the large matrices after the per-rung extras are
    computed (memory hygiene; kz9 keeps its full bundle)."""
    keep_R = {k: R[k] for k in ("kz", "z", "Nw", "Sm", "margin",
                                "c", "p", "q", "cp", "rdetp",
                                "lam_rest", "det_dev", "schur_dev",
                                "pmass", "m2p")}
    keep_X = {k: X[k] for k in ("g21", "k_res", "mass2", "dc",
                                "dev_res", "dev_sp")}
    keep_Y = {k: Y[k] for k in ("rho0", "rho_hi", "y0", "T0",
                                "dev_split", "dev_cpc", "cc2",
                                "sh_p", "sh_q", "sh_c", "sh_max",
                                "sgn", "pm", "qm", "cm", "top1",
                                "m90", "arch_top", "peel_top",
                                "t0arch")}
    return keep_R, keep_X, keep_Y


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("delta_source_anatomy_probe -- PRIME.LSTAR."
          "DELTA_SOURCE_ANATOMY.01 (round 348)")
    print("SPEC_SHA %s   (r342 PX %s / r343 PC3 %s / r345 GR %s / "
          "r347 DA %s / r330 DSW %s)"
          % (SPEC_SHA[:16], PX.SPEC_SHA[:16], PC3.SPEC_SHA[:16],
             GR.SPEC_SHA[:16], DA.SPEC_SHA[:16], DSW.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 block; ladder, twin, fits, "
                        "protocols, laws, decomposition, weak "
                        "family, worlds, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and PC3.SPEC_SHA.startswith(PC3_SHA_PREFIX)
              and GR.SPEC_SHA.startswith(GR_SHA_PREFIX)
              and DA.SPEC_SHA.startswith(DA_SHA_PREFIX)
              and DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r342/r343/r345/r347/r330 "
          "machinery imported verbatim (SPEC_SHA %s == %s*, %s == "
          "%s*, %s == %s*, %s == %s*, %s == %s*), the order-0 "
          "split with its Fractions toy, the two-level dressed-"
          "scalar identity with the rank-2 rational model, the "
          "rate toys, the margin-pinning protocol (r345 CURV_FLAT "
          "verbatim), the shadow census (med bar %.2f, sign >= "
          "%d), the theorem-image clause (UNIV_BAR %.1f), the y0 "
          "law clauses (DELTA0_MIN %.1f, CARRY %.1f), the "
          "dictionary sample clause (bar %.2f), the weak family "
          "%s (bar %.2f), the r347 mirror world rule verbatim, "
          "every bar/tolerance, the mutants and the verdict form; "
          "pre-spec scoping s1-s3 disclosed in the spec (four "
          "printed sample rungs + toy sizing); the STOP list "
          "forbids any L* claim and any certificate reading "
          "beyond the sealed census"
          % (PX.SPEC_SHA[:8], PX_SHA_PREFIX, PC3.SPEC_SHA[:8],
             PC3_SHA_PREFIX, GR.SPEC_SHA[:8], GR_SHA_PREFIX,
             DA.SPEC_SHA[:8], DA_SHA_PREFIX, DSW.SPEC_SHA[:8],
             DSW_SHA_PREFIX, SHADOW_MED_BAR, SGN_MIN, UNIV_BAR,
             DELTA0_MIN, CARRY_BAR, DICT_T0_BAR, str(KZ_WEAK),
             WEAK_BAR))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_mode_posthoc")
    hits_m3 = scope_audit("mutant_delta0_readback")
    hits_m4 = scope_audit("mutant_toy_plant")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4),
          "the %d module-own constructors consume kernel Gram / "
          "spectrum / weight / position arrays and measured "
          "columns ONLY (%s); fragment audit (no fit primitives "
          "beyond the imported r286 Theil-Sen + r345 protocol + "
          "r347 decay instrument): %s; m2 FLAGGED (%s); m3 "
          "FLAGGED (%s); m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- TWO-LEVEL FRACTIONS + RATE FAMILIES + "
            "ORDER-0 SPLIT + INSTRUMENTS")
    # (T1a) rank-2 rational model, EXACT Fractions
    lam1, lam2 = Fr(9, 10), Fr(3, 10)
    fa1, fa2, fb1, fb2 = Fr(3, 5), Fr(4, 5), Fr(-4, 5), Fr(3, 5)
    mu1, mu2 = 1 / (1 - lam1), 1 / (1 - lam2)
    M11 = mu1 * fa1 * fa1 + mu2 * fb1 * fb1
    M22 = mu1 * fa2 * fa2 + mu2 * fb2 * fb2
    M12 = mu1 * fa1 * fa2 + mu2 * fb1 * fb2
    detM = M11 * M22 - M12 * M12
    p_ex, q_ex, c_ex = M22 / detM, M11 / detM, M12 / detM
    m_fr = 1 - lam1
    g_fr = (1 - lam2) / (1 - lam1)
    Dt_fr = fa1 * fb2 - fa2 * fb1
    p_f = m_fr * (g_fr * fa2 * fa2 + fb2 * fb2) / (Dt_fr * Dt_fr)
    q_f = m_fr * (g_fr * fa1 * fa1 + fb1 * fb1) / (Dt_fr * Dt_fr)
    c_f = m_fr * (g_fr * fa1 * fa2 + fb1 * fb2) / (Dt_fr * Dt_fr)
    ok_fr = (p_ex == p_f == Fr(121, 250)
             and q_ex == q_f == Fr(79, 250)
             and c_ex == c_f == Fr(72, 250))
    r2_fr = 1 - c_f * c_f / (p_f * q_f)
    r2_gr = GR.two_level_formula(float(g_fr), float(fb1 / fa1),
                                 float(fb2 / fa2))
    ok_r2 = (r2_fr == Fr(4375, 9559)
             and abs(float(r2_fr) - r2_gr) <= TOY_TOL)
    # (T1b) block-spectral 4x4 through the FULL Schur chain (f64)
    w1v = np.array([0.6, 0.8, 0.0, 0.0])
    w2v = np.array([-0.8, 0.6, 0.0, 0.0])
    w3v = np.array([0.0, 0.0, 1.0, 0.0])
    w4v = np.array([0.0, 0.0, 0.0, 1.0])
    E4 = (0.9 * np.outer(w1v, w1v) + 0.3 * np.outer(w2v, w2v)
          + 0.2 * np.outer(w3v, w3v) + 0.1 * np.outer(w4v, w4v))
    Ad4, _lr4, _s1_, _s2_ = PX.schur_dress(E4, 0, 1)
    p4 = 1.0 - float(Ad4[0, 0])
    q4 = 1.0 - float(Ad4[1, 1])
    c4 = float(0.5 * (Ad4[0, 1] + Ad4[1, 0]))
    dev_chain = max(abs(p4 - float(p_f)), abs(q4 - float(q_f)),
                    abs(c4 - float(c_f)))
    pp2t, qq2t, cc2t = two_level_dressed(0.1, 7.0, 0.6, 0.8,
                                         -0.8, 0.6)
    dev_con = max(abs(pp2t - float(p_f)), abs(qq2t - float(q_f)),
                  abs(cc2t - float(c_f)))
    check("G10-toy-two-level-fractions", ok_fr and ok_r2
          and dev_chain <= TOY_TOL and dev_con <= TOY_TOL,
          "THE TWO-LEVEL DRESSED-SCALAR IDENTITY: rank-2 rational "
          "M inverted EXACTLY in Fractions == the formulas "
          "m(g21 a2^2+b2^2)/Dt^2 etc. == (121/250, 79/250, "
          "72/250) by hand; cross-tie r'_2 = 1 - c'^2/(p'q') == "
          "4375/9559 == the r345 two-level formula (dev %.1e); "
          "FULL Schur chain on the block-spectral 4x4 == the "
          "formulas at %.1e (bar %.0e); the audited constructor "
          "matches at %.1e -- every dressed scalar of a top-2 "
          "block is margin x an O(1) geometry factor, EXACTLY"
          % (abs(float(r2_fr) - r2_gr), dev_chain, TOY_TOL,
             dev_con))
    # (T2) rate toys
    Nt = TOY_N0 * TOY_RATIO ** np.arange(TOY_NPTS)
    lnNt = np.log(Nt)
    m_t = 1e-4 * (Nt / TOY_N0) ** (-TOY_ALPHA)
    p_t = 8e-4 * (Nt / TOY_N0) ** (-TOY_AP)
    q_t = 1.3e-3 * (Nt / TOY_N0) ** (-TOY_AQ)
    c_t = np.sqrt(TOY_RC * p_t * q_t)
    a_c_toy = 0.5 * (TOY_AP + TOY_AQ)
    b1_t = TOY_T1 * TOY_A1
    b2_t = TOY_T2 * TOY_A2

    def toy_slopes(b2col, pcol, qcol, ccol):
        pp2c, qq2c, cc2c = two_level_dressed(m_t, TOY_G21, TOY_A1,
                                             TOY_A2, b1_t, b2col)
        sf = {}
        for nm, num, den in (("fp", pp2c, pcol), ("fq", qq2c, qcol),
                             ("fc", np.abs(cc2c), ccol)):
            sf[nm] = float(LM.ts_fit(lnNt, np.log(num / den))[1])
        sx = [float(LM.ts_fit(lnNt, np.log(np.abs(v)))[1])
              for v in (pp2c, qq2c, cc2c)]
        return sf, max(sx) - min(sx)

    sf_u, spread_u = toy_slopes(np.full(TOY_NPTS, b2_t), p_t, q_t,
                                c_t)
    ok_uneq = (abs(sf_u["fp"] + (TOY_ALPHA - TOY_AP)) <= RATE_TOL
               and abs(sf_u["fq"] + (TOY_ALPHA - TOY_AQ))
               <= RATE_TOL
               and abs(sf_u["fc"] + (TOY_ALPHA - a_c_toy))
               <= RATE_TOL
               and spread_u <= RATE_TOL
               and abs((sf_u["fq"] - sf_u["fp"])
                       - (TOY_AQ - TOY_AP)) <= RATE_TOL)
    p_e = 8e-4 * (Nt / TOY_N0) ** (-a_c_toy)
    q_e = 1.3e-3 * (Nt / TOY_N0) ** (-a_c_toy)
    c_e = np.sqrt(TOY_RC * p_e * q_e)
    sf_e, spread_e = toy_slopes(np.full(TOY_NPTS, b2_t), p_e, q_e,
                                c_e)
    ok_eq = (max(abs(sf_e["fp"] - sf_e["fq"]),
                 abs(sf_e["fp"] - sf_e["fc"])) <= RATE_TOL
             and spread_e <= RATE_TOL)
    b2_d = TOY_T2 * TOY_A2 * (Nt / TOY_N0) ** TOY_TAU
    _sf_d, spread_d = toy_slopes(b2_d, p_t, q_t, c_t)
    check("G11-toy-rate-families", ok_uneq and ok_eq
          and spread_d >= DRIFT_MIN,
          "THE RATE TOYS (planted alpha %.1f): flat geometry "
          "forces delta_x = alpha - a_x EXACTLY (fp %.6f == "
          "-(%.2f), fq %.6f, fc %.6f at %.0e; dressed-slope "
          "spread %.1e) -- the naive equality delta_p == delta_q "
          "== delta holds IFF a_p == a_q == a_c (equal-rate "
          "family spread %.1e) and breaks by EXACTLY the bare "
          "spread otherwise (fq - fp == %.2f at %.0e); the tau = "
          "%.1f ANGLE DRIFT separates the dressed slopes by %.3f "
          ">= %.1f -- the flat-geometry hypothesis is load-"
          "bearing" % (TOY_ALPHA, sf_u["fp"], TOY_ALPHA - TOY_AP,
                       sf_u["fq"], sf_u["fc"], RATE_TOL, spread_u,
                       spread_e, TOY_AQ - TOY_AP, RATE_TOL,
                       TOY_TAU, spread_d, DRIFT_MIN))
    # (T3) order-0 split on the 3x3 hand toy: Fractions + f64
    c1_, c2_, dd_ = Fr(1, 16), Fr(1, 32), Fr(1, 8)
    T0_ex = c1_ * c2_
    Tp_ex = c1_ * c2_ * dd_ / (1 - dd_)
    dc_ex = c1_ * c2_ / (1 - dd_)
    ok_fr0 = (T0_ex + Tp_ex == dc_ex)
    sp3 = order0_split(np.array([0.125]), np.array([1.0 / 16.0]),
                       np.array([1.0 / 32.0]), 0.125)
    dev_t3 = abs((sp3["T0"] + sp3["Tplus"]) - float(dc_ex)) \
        / float(dc_ex)
    check("G12-toy-order0-split", ok_fr0 and dev_t3 <= TOY_TOL
          and abs(sp3["T0"] - float(T0_ex)) <= TOY_TOL,
          "THE ORDER-0 SPLIT on the 3x3 hand toy: Delta c = T0 + "
          "T+ == c1 c2 + c1 c2 d/(1-d) == c1 c2/(1-d) EXACT in "
          "Fractions (%s); f64 route dev %.1e (bar %.0e) -- the "
          "split is the exact resolvent-series identity "
          "(I-D)^{-1} = I + D (I-D)^{-1}, not an approximation"
          % (str(dc_ex), dev_t3, TOY_TOL))
    # (T4) instruments: r347 decay_law + r345 curvflat re-gates
    kk = np.arange(25)
    lnS = np.log(300.0 * 1.1 ** kk)
    scat = math.log(2.0) * np.sin(7.0 * kk)
    e3p_t = [(float(lnS[-1] + 0.3), float(np.log(0.3)
                                          - 3.0 * (lnS[-1] + 0.3)
                                          + 0.1))] * 12
    e4p_t = [(float(lnS[-1] + 0.5), float(np.log(0.3)
                                          - 3.0 * (lnS[-1] + 0.5)
                                          - 0.2))] * 6
    dl3 = DA.decay_law(lnS, np.log(0.3) - 3.0 * lnS + scat,
                       e3p_t, e4p_t)
    dl_flat = DA.decay_law(lnS, np.log(0.3) + scat, [], [])
    coh_toy = [("c%d" % j, list(range(5 * j, 5 * j + 5)))
               for j in range(5)]
    fitm_t = [True] * 25
    p_flat = GR.curvflat_protocol(lnS, np.log(0.30) + scat, fitm_t,
                                  coh_toy)
    p_dec3 = GR.curvflat_protocol(lnS, np.log(0.30) - 3.0 * lnS
                                  + scat, fitm_t, coh_toy)
    check("G13-toy-instruments", abs(dl3["slope"] + 3.0) <= 0.2
          and dl3["e3_in"] == 12 and dl3["e4_low"] == 0
          and (-dl_flat["slope"]) < DELTA0_MIN
          and p_flat["ok"] and not p_dec3["ok"],
          "INSTRUMENT RE-GATES: the r347 decay_law fits synthetic "
          "N^-3 with x2 scatter to %.3f (EXT3 12/12, EXT4 low 0) "
          "and refuses the flat column (delta %.3f < %.1f); the "
          "r345 CURV_FLAT protocol passes the flat column (slope "
          "%+.3f, CI [%+.2f, %+.2f]) and catches N^-3 (%+.3f) -- "
          "both instruments imported verbatim with module-sealed "
          "constants" % (dl3["slope"], -dl_flat["slope"],
                         DELTA0_MIN, p_flat["slope"],
                         p_flat["qlo"], p_flat["qhi"],
                         p_dec3["slope"]))
    S_toy = np.array([300.0 * (1.1 ** k) for k in range(25)])
    y_flat = np.log(0.30) + 0.0 * np.log(S_toy)
    ft = LM.ts_fit(np.log(S_toy), y_flat)
    ft_short = LM.ts_fit(np.arange(8.0), np.arange(8.0))
    check("G14-toy-fit", (not isinstance(ft[0], str))
          and abs(ft[1]) <= 1e-12
          and ft_short[0] == "SHORT_LADDER",
          "r286 Theil-Sen imported verbatim: synthetic FLAT "
          "column slope %.1e == 0; the guard REFUSES 8 points "
          "(%s)" % (abs(ft[1]), str(ft_short)))

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + DRESSED ANCHORS + ORDER-0 SPLIT "
            "+ SHADOWS + MODE CENSUS")
    R9 = PX.build_rung(MAIN_KZ)
    X9 = PC3.extend_rung(R9)
    C9 = DA.closure_cols(R9)
    Y9 = rung_extras(R9, X9, C9)
    lam185, _B185 = V.lam_max_at(R9["mz"], REC_NW + 1)
    ok_rec = (R9["S"] == REC_S and R9["Sm"] == REC_SM
              and R9["Nw"] == REC_NW
              and abs(R9["lam"] - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs(R9["margin"] / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (nu %d), N_w = %d, lambda_max = %.8f "
          "(record %.8f), margin %.4e (record %.4e), lambda at "
          "185 = %.8f > 1 -- the document route reproduced"
          % (R9["S"], R9["Sm"], R9["Nw"], R9["lam"], REC_LAM,
             R9["margin"], REC_MARGIN, lam185))
    A = W9_ANCH
    with np.errstate(over="ignore", invalid="ignore"):
        rho32_9 = GR.mirror_profile(X9["D"], Y9["u1"], Y9["u2"],
                                    R9["c"], (32,))[32]
    ok_anch = (abs(R9["d1p"] / A["d1p"] - 1.0) <= 1e-5
               and abs(R9["d2p"] / A["d2p"] - 1.0) <= 1e-5
               and abs(R9["cp"] / A["cp"] - 1.0) <= 1e-3
               and abs(R9["rdetp"] / A["rdetp"] - 1.0) <= 1e-3
               and abs(R9["lam_rest"] - A["lam_rest"]) <= 1e-5
               and abs(C9["ppr"] / A["ppr"] - 1.0) <= 1e-3
               and abs(C9["qpr"] / A["qpr"] - 1.0) <= 1e-3
               and abs(C9["m2p"] / A["m2p"] - 1.0) <= 1e-3
               and abs(C9["bridge"] - A["bridge"]) <= 5e-3
               and abs(C9["cpc"] / A["cpc"] - 1.0) <= 1e-3
               and abs(X9["g21"] - A["g21"]) <= 0.01
               and X9["k_res"] == A["kres"]
               and abs(rho32_9 - A["rho32"]) <= 5e-3)
    check("G21-w9-dressed-anchors", ok_anch,
          "LEG 0 BIT-NEAR: dressed (d1', d2', c') = (%.6f, %.6f, "
          "%.6e) == r343/r347; p' %.4e, q' %.4e, m2' %.4e, "
          "m2'/margin %.4f, c'/c %.4e, r'_det %.6f, lambda_rest "
          "%.6f; g21 %.4f, K_res %d, rho_32 %.4f (r345 %.4f) -- "
          "the r348 coordinates start exactly where "
          "r342/r343/r345/r347 left them"
          % (R9["d1p"], R9["d2p"], R9["cp"], C9["ppr"], C9["qpr"],
             C9["m2p"], C9["bridge"], C9["cpc"], R9["rdetp"],
             R9["lam_rest"], X9["g21"], X9["k_res"], rho32_9,
             A["rho32"]))
    S1 = S1_ANCH
    ok_split9 = (Y9["dev_split"] <= SPLIT_BAR
                 and Y9["dev_cpc"] <= CPC_ID_BAR
                 and abs(Y9["rho0"] - S1["rho0"]) <= 5e-3
                 and abs(Y9["y0"] - S1["y0"]) <= 5e-3
                 and abs(Y9["rho_hi"] - S1["rho_hi"]) <= 5e-3)
    check("G22-w9-order0-split", ok_split9,
          "THE ORDER-0 SPLIT LIVE: Delta c = T0 + T+ (residual "
          "%.1e, bar %.0e); rho_0 = %.4f (s1 %.4f), y0 = 1 - "
          "rho_0 = %.4f, rho_hi = %.4f -- and the bookkeeping "
          "identity c'/c == y0 - rho_hi holds at %.1e (bar %.0e): "
          "the cancellation law is the DIFFERENCE of the order-0 "
          "miss and the higher-order quota, exactly"
          % (Y9["dev_split"], SPLIT_BAR, Y9["rho0"], S1["rho0"],
             Y9["y0"], Y9["rho_hi"], Y9["dev_cpc"], CPC_ID_BAR))
    ok_sh9 = (abs(Y9["sh_p"] - S1["sh_p"]) <= 5e-3
              and abs(Y9["sh_q"] - S1["sh_q"]) <= 5e-3
              and abs(Y9["sh_c"] - S1["sh_c"]) <= 5e-3
              and Y9["sgn"]
              and abs(Y9["pm"] - S1["pm"]) <= 0.05
              and abs(Y9["qm"] - S1["qm"]) <= 0.05
              and abs(Y9["cm"] - S1["cm"]) <= 0.05)
    check("G23-w9-two-level-shadows", ok_sh9,
          "THE TWO-LEVEL SHADOWS LIVE: sh_p/q/c = %.4f / %.4f / "
          "%.4f (s1 %.4f / %.4f / %.4f), sign of c'_2 agrees; "
          "MARGIN-PINNING RATIOS p'/m = %.4f, q'/m = %.4f, "
          "|c'|/m = %.4f (s1 %.4f / %.4f / %.4f) -- the dressed "
          "scalars sit at O(1..10) x margin on the flagship"
          % (Y9["sh_p"], Y9["sh_q"], Y9["sh_c"], S1["sh_p"],
             S1["sh_q"], S1["sh_c"], Y9["pm"], Y9["qm"], Y9["cm"],
             S1["pm"], S1["qm"], S1["cm"]))
    dict9 = dict_sample_dev(MAIN_KZ, R9, Y9)
    ok_mc9 = (abs(Y9["top1"] - S1["top1"]) <= 5e-3
              and abs(Y9["m90"] - S1["m90"]) <= 2
              and abs(Y9["t0arch"] - S1["t0arch"]) <= 5e-3
              and abs(dict9 - S1["dict_t0"]) <= 0.01)
    check("G24-w9-mode-census-dict", ok_mc9,
          "MODE CENSUS + DICTIONARY at w9: top-1 mode share %.4f "
          "(s1 %.4f), M90 = %d (s1 %d), T0 arch-rim atom share "
          "%.4f, top-mode arch mass %.4f / peel-pair mass %.4f "
          "(the carriers are NOT the peel-concentrated top rest "
          "mode); dictionary T0 surrogate dev %.4f (s1 %.4f -- "
          "the honest worst of the sample: the weight side "
          "carries better with depth)"
          % (Y9["top1"], S1["top1"], Y9["m90"], S1["m90"],
             Y9["t0arch"], Y9["arch_top"], Y9["peel_top"], dict9,
             S1["dict_t0"]))

    # ---------------- S3 the ladder
    section("S3  LEG A/B -- THE LADDER (42 + 15 + 12 EXT3 + 6 "
            "EXT4)")
    if smoke:
        for g in ("G30-ladder-census", "G31-ladder-identities",
                  "G32-cohort-anchors"):
            check(g, True, "SMOKE: skipped")
        RT, XT, YT = {9: R9}, {9: X9}, {9: Y9}
        CT = {9: C9}
        core_kzs, ext_kzs, ext3_kzs, ext4_kzs = [9], [], [], []
        excl = []
        dict_devs = {9: dict9}
    else:
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in LM.ext_rule()[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        RT, XT, YT, CT = {}, {}, {}, {}
        dict_devs = {}
        print("    %-5s %-5s %-5s %-5s | %-10s %-7s %-9s %-9s "
              "%-9s | %-7s %-7s %-7s %-2s | %-7s %-7s %-7s | "
              "%-6s %-4s %-6s %-4s"
              % ("kz", "z", "S-", "N_w", "margin", "rho0", "y0",
                 "rho_hi", "c'/c", "sh_p", "sh_q", "sh_c", "sg",
                 "p'/m", "q'/m", "c'/m", "top1", "M90", "T0arc",
                 "Kres"))
        neg_rows = []
        for kz in core_kzs + ext_kzs + ext3_kzs + ext4_kzs:
            if kz == MAIN_KZ:
                R, X, C, Y = R9, X9, C9, Y9
            else:
                R = PX.build_rung(kz)
                X = PC3.extend_rung(R)
                C = DA.closure_cols(R)
                Y = rung_extras(R, X, C)
            if kz in SAMPLE_KZ:
                dict_devs[kz] = (dict9 if kz == MAIN_KZ
                                 else dict_sample_dev(kz, R, Y))
            if R["margin"] <= 0:
                neg_rows.append(kz)
            print("    %-5d %-5d %-5d %-5d | %.4e %7.4f %.3e "
                  "%.3e %.3e | %7.4f %7.4f %7.4f %2s | %7.4f "
                  "%7.4f %7.4f | %6.4f %4d %6.4f %4d"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["margin"],
                     Y["rho0"], Y["y0"], Y["rho_hi"], C["cpc"],
                     Y["sh_p"], Y["sh_q"], Y["sh_c"],
                     "+" if Y["sgn"] else "-", Y["pm"], Y["qm"],
                     Y["cm"], Y["top1"], Y["m90"], Y["t0arch"],
                     X["k_res"]), flush=True)
            if kz == MAIN_KZ:
                RT[kz], XT[kz], YT[kz], CT[kz] = R, X, Y, C
            else:
                rs, xs, ys = slim(R, X, C, Y)
                RT[kz], XT[kz], YT[kz], CT[kz] = rs, xs, ys, C
        excl = list(neg_rows)
        ok_cen = (len(core_kzs) == 42
                  and all(EXT3_NW_MIN <= RT[k]["Nw"]
                          <= EXT3_NW_MAX for k in ext3_kzs)
                  and all(EXT4_NW_MIN <= RT[k]["Nw"]
                          <= EXT4_NW_MAX for k in ext4_kzs))
        check("G30-ladder-census", ok_cen and not neg_rows,
              "42 core + 15 r286 extension + 12 EXT3 (N_w %d..%d) "
              "+ 6 EXT4 (N_w %d..%d, the r343 sealed selections "
              "adopted AS-IS); every f64 margin positive "
              "(contingency rows: %s)"
              % (EXT3_NW_MIN, EXT3_NW_MAX, EXT4_NW_MIN,
                 EXT4_NW_MAX,
                 str(neg_rows) if neg_rows else "none"))
        all_kz = core_kzs + ext_kzs + ext3_kzs + ext4_kzs
        kz57 = core_kzs + ext_kzs
        max_split = max(YT[k]["dev_split"] for k in all_kz)
        max_cpc = max(YT[k]["dev_cpc"] for k in all_kz)
        max_id = max(CT[k]["dev_id"] for k in all_kz)
        max_rd = max(CT[k]["dev_rdef"] for k in all_kz)
        n_sgn = sum(1 for k in all_kz if YT[k]["sgn"])
        ok_id = (max_split <= SPLIT_BAR and max_cpc <= CPC_ID_BAR
                 and max_id <= ID_BAR and max_rd <= RDEF_BAR
                 and all(RT[k]["det_dev"] <= 1e-12
                         and RT[k]["schur_dev"] <= 1e-6
                         and XT[k]["dev_res"] <= 1e-6
                         and XT[k]["dev_sp"] <= 1e-9
                         for k in all_kz))
        check("G31-ladder-identities", ok_id,
              "identities on all %d rows: the ORDER-0 SPLIT T0 + "
              "T+ == Delta c (max %.1e, bar %.0e), the "
              "bookkeeping c'/c == y0 - rho_hi (max %.1e, bar "
              "%.0e), the r347 one-line identity re-gated (dev_id "
              "%.1e / dev_rdef %.1e), r342 det/Schur + r343 "
              "resolvent/spectral wards re-gated; c'_2 sign "
              "agreement %d/%d" % (len(all_kz), max_split,
                                   SPLIT_BAR, max_cpc, CPC_ID_BAR,
                                   max_id, max_rd, n_sgn,
                                   len(all_kz)))

        def med(vals):
            return float(np.median(np.asarray(vals, float)))

        fit_kz = [k for k in kz57 if k not in excl]
        med_rho0 = med([YT[k]["rho0"] for k in fit_kz])
        med_m90 = med([YT[k]["m90"] for k in fit_kz])
        med_top1 = med([YT[k]["top1"] for k in fit_kz])
        med_br = med([CT[k]["bridge"] for k in fit_kz])
        ok_coh = (abs(med_rho0 - MED_ANCH["rho0"]) <= 0.01
                  and abs(med_m90 - MED_ANCH["m90"]) <= 2.0
                  and abs(med_top1 - MED_ANCH["top1"]) <= 0.10
                  and abs(med_br - MED_ANCH["bridge"]) <= 5e-3
                  and all(abs(YT[k]["rho0"]
                              - SAMPLE_ANCH[k]["rho0"]) <= 5e-3
                          and abs(YT[k]["sh_p"]
                                  - SAMPLE_ANCH[k]["sh_p"])
                          <= 5e-3
                          for k in SAMPLE_ANCH))
        check("G32-cohort-anchors", ok_coh,
              "LEG 0 COHORT ANCHORS: median rho_0 %.4f (r345 "
              "%.3f), median M90 %.0f (r345 %.0f +- 2), median "
              "top-1 share %.4f (r345 %.3f at tol 0.10 -- the "
              "r345 profile ordered by |alpha beta/(1-delta)| "
              "like here, the wide bar covers ordering "
              "sensitivity, disclosed); median bridge %.4f (r343 "
              "%.4f); scoped sample rho_0/sh_p (kz44/56/130) all "
              "bit-near -- Leg 0 closed"
              % (med_rho0, MED_ANCH["rho0"], med_m90,
                 MED_ANCH["m90"], med_top1, MED_ANCH["top1"],
                 med_br, MED_ANCH["bridge"]))

    # ---------------- S4 twin
    section("S4  TWIN WARD")
    if smoke:
        check("G40-twin", True, "SMOKE: skipped")
        mzT = None
    else:
        uu9c, mm9c = TR.base_comb(9)
        mzD = TR.build_world(9, uu9c, mm9c)
        mz9 = R9["mz"]
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9c)
        u2c, m2c, _dens, _du = AKD.twin_rational(uu9c, mm9c,
                                                 gaps9, mz9["D"],
                                                 TWIN_TOL)
        mzT = TR.build_world(9, u2c, m2c)
        aT, bT, h0T = V.mu_chain(mzT["xp"], mzT["wp"], mzT["Nw"])
        BT = V.b_matrix(aT, bT, h0T, mzT["yn"], mzT["vn"],
                        mzT["Nw"])
        ET = BT @ BT.T
        t1_, t2_ = PX.pair_select(mzT["yn"])
        evT, WT = np.linalg.eigh(ET)
        restT = [k for k in range(ET.shape[0])
                 if k != t1_ and k != t2_]
        DT = ET[np.ix_(restT, restT)]
        dvT, WDT = np.linalg.eigh(DT)
        u1T = ET[t1_, restT]
        u2T = ET[t2_, restT]
        alT = WDT.T @ u1T
        beT = WDT.T @ u2T
        cT = float(ET[t1_, t2_])
        spT = order0_split(dvT, alT, beT, cT)
        AdT, _lrT, _s1t, _s2t = PX.schur_dress(ET, t1_, t2_)
        ppT = 1.0 - float(AdT[0, 0])
        qqT = 1.0 - float(AdT[1, 1])
        cpT = float(0.5 * (AdT[0, 1] + AdT[1, 0]))
        mT = 1.0 - float(evT[-1])
        g21T = (1.0 - float(evT[-2])) / (1.0 - float(evT[-1]))
        pp2T, qq2T, cc2T = two_level_dressed(
            mT, g21T, float(WT[t1_, -1]), float(WT[t2_, -1]),
            float(WT[t1_, -2]), float(WT[t2_, -2]))
        devT = dict(
            rho0=abs(spT["rho0"] - Y9["rho0"]) / abs(Y9["rho0"]),
            y0=abs(spT["y0"] - Y9["y0"]) / abs(Y9["y0"]),
            T0=abs(spT["T0"] - Y9["T0"]) / abs(Y9["T0"]),
            sh=max(abs(abs(pp2T / ppT - 1.0) - Y9["sh_p"]),
                   abs(abs(qq2T / qqT - 1.0) - Y9["sh_q"]),
                   abs(abs(abs(cc2T) / abs(cpT) - 1.0)
                       - Y9["sh_c"])),
            ratio=max(abs(ppT / mT - Y9["pm"]) / Y9["pm"],
                      abs(qqT / mT - Y9["qm"]) / Y9["qm"],
                      abs(abs(cpT) / mT - Y9["cm"]) / Y9["cm"]))
        ok_twin = ok_dose0 and all(v <= TWIN_BAR
                                   for v in devT.values())
        check("G40-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (dose-zero identity "
              "BITWISE %s): rho_0 dev %.1e, y0 dev %.1e, T0 dev "
              "%.1e, shadow devs <= %.1e, margin-ratio devs <= "
              "%.1e (bar %.0e) -- the order-0 and two-level "
              "coordinates are twin-stable"
              % (TWIN_TOL, ok_dose0, devT["rho0"], devT["y0"],
                 devT["T0"], devT["sh"], devT["ratio"], TWIN_BAR))

    # ---------------- S5 fits + protocols + laws + decomposition
    section("S5  LEG B/C -- SEALED FITS + PINNING PROTOCOL + "
            "ORDER-0 LAWS + DECOMPOSITION")
    if smoke:
        for g in ("G50-fit-anchors", "G51-pinning-protocol",
                  "G52-shadow-census", "G53-order0-laws",
                  "G54-delta-decomposition", "G55-dict-sample"):
            check(g, True, "SMOKE: skipped")
        rate_eq = order0_law = order0_carries = None
        dict_go = None
        laws = {}
        exp_txt = dec_txt = dict_txt = ""
        univ_max = None
    else:
        lnN57 = np.log(np.array([RT[k]["Nw"] for k in fit_kz],
                                float))
        getters = {
            "margin": lambda k: RT[k]["margin"],
            "c": lambda k: abs(RT[k]["c"]),
            "p": lambda k: RT[k]["p"],
            "q": lambda k: RT[k]["q"],
            "cpc": lambda k: CT[k]["cpc"],
            "cp": lambda k: abs(RT[k]["cp"]),
            "ppr": lambda k: CT[k]["ppr"],
            "qpr": lambda k: CT[k]["qpr"],
            "fp": lambda k: CT[k]["fp"],
            "fq": lambda k: CT[k]["fq"],
            "y0": lambda k: abs(YT[k]["y0"]),
            "rhi": lambda k: abs(YT[k]["rho_hi"]),
            "pm": lambda k: YT[k]["pm"],
            "qm": lambda k: YT[k]["qm"],
            "cm": lambda k: YT[k]["cm"],
        }
        laws = {}
        for nm, get in getters.items():
            e3p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext3_kzs]
            e4p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext4_kzs]
            laws[nm] = DA.decay_law(lnN57,
                                    np.log([get(k)
                                            for k in fit_kz]),
                                    e3p, e4p)
        ok_fit = (all(abs(laws[nm]["slope"] - FIT_ANCH[nm])
                      <= FIT_ANCH_TOL for nm in FIT_ANCH)
                  and all(abs(laws[nm]["curv"] - CURV_ANCH[nm])
                          <= CURV_ANCH_TOL for nm in CURV_ANCH))
        check("G50-fit-anchors", ok_fit,
              "LEG 0 FIT ANCHORS on the 57 (slope | record): "
              "margin %.3f | %.3f, c %.3f | %.3f, p %.3f | %.3f, "
              "q %.3f | %.3f, cpc %.3f | %.3f, cp %.3f | %.3f, "
              "p' %.3f | %.3f, q' %.3f | %.3f, fp %.3f | %.3f, "
              "fq %.3f | %.3f (tol %.2f); CURV ANCHORS cpc %+.3f "
              "| %+.3f, margin %+.3f | %+.3f, c %+.3f | %+.3f "
              "(tol %.2f)"
              % (laws["margin"]["slope"], FIT_ANCH["margin"],
                 laws["c"]["slope"], FIT_ANCH["c"],
                 laws["p"]["slope"], FIT_ANCH["p"],
                 laws["q"]["slope"], FIT_ANCH["q"],
                 laws["cpc"]["slope"], FIT_ANCH["cpc"],
                 laws["cp"]["slope"], FIT_ANCH["cp"],
                 laws["ppr"]["slope"], FIT_ANCH["ppr"],
                 laws["qpr"]["slope"], FIT_ANCH["qpr"],
                 laws["fp"]["slope"], FIT_ANCH["fp"],
                 laws["fq"]["slope"], FIT_ANCH["fq"],
                 FIT_ANCH_TOL, laws["cpc"]["curv"],
                 CURV_ANCH["cpc"], laws["margin"]["curv"],
                 CURV_ANCH["margin"], laws["c"]["curv"],
                 CURV_ANCH["c"], CURV_ANCH_TOL))
        # E1: the margin-pinning protocol
        arb_kz = [k for k in all_kz if k not in excl]
        lnN_all = np.log(np.array([RT[k]["Nw"] for k in arb_kz],
                                  float))
        fitm = [k in set(fit_kz) for k in arb_kz]
        cohorts = [
            ("core42", [i for i, k in enumerate(arb_kz)
                        if k in set(core_kzs)]),
            ("ext15", [i for i, k in enumerate(arb_kz)
                       if k in set(ext_kzs)]),
            ("ext3B", [i for i, k in enumerate(arb_kz)
                       if k in set(EXT3_KZ_B)]),
            ("ext3A", [i for i, k in enumerate(arb_kz)
                       if k in set(EXT3_KZ_A)]),
            ("ext4", [i for i, k in enumerate(arb_kz)
                      if k in set(ext4_kzs)]),
        ]
        flat_r = {}
        for nm in ("pm", "qm", "cm"):
            flat_r[nm] = GR.curvflat_protocol(
                lnN_all, np.log([getters[nm](k) for k in arb_kz]),
                fitm, cohorts)
        e1 = all(flat_r[nm]["ok"] for nm in flat_r)
        check("G51-pinning-protocol", True,
              "E1 THE MARGIN-PINNING RATIOS under the r345 "
              "CURV_FLAT protocol (all %d arbitrated rows): %s "
              "=> %s -- %s"
              % (len(arb_kz), "; ".join(
                  "%s %s (CH1 %d out/%d hard max %.3f dec; CH2 "
                  "slope %+.3f CI [%+.2f, %+.2f]; CH3 drift %.3f)"
                  % (nm, "PASS" if flat_r[nm]["ok"] else "FAIL",
                     flat_r[nm]["n_out"], flat_r[nm]["hard"],
                     flat_r[nm]["max_dev"], flat_r[nm]["slope"],
                     flat_r[nm]["qlo"], flat_r[nm]["qhi"],
                     flat_r[nm]["drift"])
                  for nm in ("pm", "qm", "cm")),
                 "ALL THREE FLAT" if e1 else "NOT all flat",
                 "every dressed scalar is pinned to the margin "
                 "scale" if e1 else "the pinning breaks, named "
                 "above"))
        # E2/E3: shadow census + sign
        sh_med = float(np.median([YT[k]["sh_max"]
                                  for k in fit_kz]))
        e2 = sh_med <= SHADOW_MED_BAR
        e3 = n_sgn >= SGN_MIN
        check("G52-shadow-census", True,
              "E2/E3 THE TWO-LEVEL TRUNCATION CENSUS: median "
              "max-shadow %.4f on the 57 (bar %.2f) => %s; sign "
              "agreement %d/%d (bar %d) => %s; shadow span "
              "%.4f..%.4f over the arbitrated rows"
              % (sh_med, SHADOW_MED_BAR, "HOLDS" if e2 else
                 "FAILS", n_sgn, len(all_kz), SGN_MIN,
                 "HOLDS" if e3 else "FAILS",
                 min(YT[k]["sh_max"] for k in arb_kz),
                 max(YT[k]["sh_max"] for k in arb_kz)))
        # order-0 laws
        delta0 = -laws["y0"]["slope"]
        delta = -laws["cpc"]["slope"]
        order0_law = (abs(laws["y0"]["curv"]) <= DEC_CURV_BAR
                      and laws["y0"]["e3_in"] >= DEC_EXT3_MIN
                      and laws["y0"]["e4_low"] <= DEC_EXT4_LOW
                      and delta0 >= DELTA0_MIN)
        order0_carries = abs(delta0 - delta) <= CARRY_BAR
        depth_med = float(np.median([CT[k]["cpc"]
                                     / abs(YT[k]["y0"])
                                     for k in fit_kz]))
        check("G53-order0-laws", True,
              "THE ORDER-0 MISS LAW (sealed): y0 slope %.3f "
              "(delta_0 %.3f), curv %+.3f, EXT3 %d/12 low %d, "
              "EXT4 %d/6 low %d => ORDER0_LAW %s; CARRIES_DELTA "
              "|%.3f - %.3f| = %.3f (bar %.1f) => %s; rho_hi "
              "CENSUS: slope %.3f, curv %+.3f, EXT3 %d/12, EXT4 "
              "%d/6 -- twin slow laws whose DIFFERENCE is the "
              "c'/c law; cancellation depth |c'/c|/y0 median "
              "%.2e" % (laws["y0"]["slope"], delta0,
                        laws["y0"]["curv"], laws["y0"]["e3_in"],
                        laws["y0"]["e3_low"], laws["y0"]["e4_in"],
                        laws["y0"]["e4_low"],
                        "HOLDS" if order0_law else "FAILS",
                        delta0, delta, abs(delta0 - delta),
                        CARRY_BAR,
                        "FIRES" if order0_carries else
                        "does NOT fire", laws["rhi"]["slope"],
                        laws["rhi"]["curv"], laws["rhi"]["e3_in"],
                        laws["rhi"]["e4_in"], depth_med))
        # E4 + decomposition
        alpha_meas = -laws["margin"]["slope"]
        a_c = -laws["c"]["slope"]
        a_p = -laws["p"]["slope"]
        a_q = -laws["q"]["slope"]
        delta_p = -laws["fp"]["slope"]
        delta_q = -laws["fq"]["slope"]
        univ = dict(p=delta_p - (alpha_meas - a_p),
                    q=delta_q - (alpha_meas - a_q),
                    c=delta - (alpha_meas - a_c))
        univ_max = max(abs(v) for v in univ.values())
        e4 = univ_max <= UNIV_BAR
        c4 = abs(alpha_meas - (a_c + delta))
        rate_eq = e1 and e2 and e3 and e4
        dec_txt = ("alpha %.3f, a_c %.3f, delta %.3f, delta_0 "
                   "%.3f; C4 re-gate |%.3f - %.3f| = %.3f (bar "
                   "%.1f) %s; THEOREM IMAGE delta_x - (alpha - "
                   "a_x): p %+.3f / q %+.3f / c %+.3f (max %.3f, "
                   "bar %.1f) => E4 %s; the naive pairwise "
                   "spread |delta_p - delta| %.3f / |delta_q - "
                   "delta| %.3f vs the bare spread |a_p - a_c| "
                   "%.3f / |a_q - a_c| %.3f"
                   % (alpha_meas, a_c, delta, delta0, alpha_meas,
                      a_c + delta, c4, CLOSURE_BAR,
                      "HOLDS" if c4 <= CLOSURE_BAR else "FAILS",
                      univ["p"], univ["q"], univ["c"], univ_max,
                      UNIV_BAR, "HOLDS" if e4 else "FAILS",
                      abs(delta_p - delta), abs(delta_q - delta),
                      abs(a_p - a_c), abs(a_q - a_c)))
        check("G54-delta-decomposition", c4 <= CLOSURE_BAR,
              "LEG C THE DECOMPOSITION: %s -- delta == alpha - "
              "a_c through the two-level skeleton; the "
              "irreducible measured rest is the pair {alpha, "
              "a_c}, both fit-census (weight side closed-form, "
              "kernel side census -- r342 negative #4)"
              % dec_txt)
        # dictionary sample
        dvals = {k: dict_devs[k] for k in SAMPLE_KZ}
        dict_med = float(np.median(list(dvals.values())))
        dict_go = dict_med <= DICT_T0_BAR
        dict_txt = ("sample devs %s, median %.4f (bar %.2f)"
                    % (str({("kz%d" % k): round(v, 4)
                            for k, v in dvals.items()}),
                       dict_med, DICT_T0_BAR))
        check("G55-dict-sample", True,
              "THE DICTIONARY REACH of the order-0 overlap "
              "(weight side, r342 v_pred verbatim inside the "
              "measured kernel rows): %s => %s -- the kernel "
              "side stays census-grade (r342 negative #4, never "
              "upgraded)"
              % (dict_txt, "DICT_T0_GO" if dict_go
                 else "DICT_T0_CENSUS"))

    # ---------------- S6 weak family
    section("S6  LEG D -- THE WEAK FAMILY (kz28 / kz44 / kz59)")
    if smoke:
        check("G60-weak-family", True, "SMOKE: skipped")
        weak_ok = None
        weak_txt = ""
    else:
        weak_rows = []
        for k in KZ_WEAK:
            weak_rows.append((k, YT[k]["rho0"], YT[k]["sh_p"],
                              YT[k]["sh_q"], YT[k]["sh_c"],
                              XT[k]["k_res"], XT[k]["mass2"],
                              RT[k]["pmass"], YT[k]["sgn"]))
            info("weak kz%-4d rho0 %.4f sh %.4f/%.4f/%.4f Kres "
                 "%d mass2 %.4f pmass %.4f sgn %s"
                 % weak_rows[-1])
        weak_med = float(np.median([max(r[2], r[3], r[4])
                                    for r in weak_rows]))
        weak_ok = weak_med <= WEAK_BAR
        weak_txt = ("median max-shadow %.4f (bar %.2f), signs "
                    "%d/%d" % (weak_med, WEAK_BAR,
                               sum(1 for r in weak_rows if r[8]),
                               len(weak_rows)))
        check("G60-weak-family", True,
              "THE CONCENTRATION-WEAK FAMILY %s (r345 kill-census "
              "suspects): %s => %s -- the two-level reading %s at "
              "weak concentration"
              % (str(KZ_WEAK), weak_txt,
                 "WEAK_FAMILY_SURVIVES" if weak_ok
                 else "WEAK_FAMILY_STRAINED",
                 "strains but does not break" if weak_ok
                 else "BREAKS"))

    # ---------------- S7 worlds
    section("S7  LEG D -- THE WORLD CENSUS + THE MIRROR CLAUSE "
            "(8 WORLDS)")
    if smoke:
        for g in ("G70-controls", "G71-worlds"):
            check(g, True, "SMOKE: skipped")
        mirror_tag = ""
        world_txt = ""
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        comb_hl, _tag = PC.gen_model(PC.Grid(), "HL2", HL2_SEED)
        uD, wD, _nnD, _chD = DSW.dirichlet_comb(9)
        uA, wA, _nnA = DSW.dirichlet_abs_comb(9)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx]
            / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)),
            ("DIR", dict(comb=(uD, wD))),
            ("ABS", dict(comb=(uA, wA))))
        WORLDS = {}
        ok_ctrl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, zones = BL.union_of_ctx(cctx)
            xs_z, ws_z, ys_z, vs_z = zones
            N_c = cctx["N"]
            if cn in CTRL_FLIPS or cn == "HL2":
                sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
                mc = next((n for n in range(len(sg))
                           if sg[n] < 0), None)
                flip = CTRL_FLIPS.get(cn, HL2_FLIP)
                ok_ctrl = ok_ctrl and (mc == flip)
            WORLDS[cn] = FC.world_from_arrays(
                cn, xs_z, ws_z, ys_z, vs_z, N_c, int(cctx["L"]))
        check("G70-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel at THEIR own N_w: minC == "
              "flips %s + HL2 %d; DIR/ABS built through the SAME "
              "channel from the r330 combs (verbatim import)"
              % (str(CTRL_FLIPS), HL2_FLIP))
        WORLDS["MAIN"] = FC.world_from_mz("MAIN", R9["mz"])
        WORLDS["TWIN"] = FC.world_from_mz("TWIN", mzT)
        cen = {}
        order = ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH", "HL2",
                 "DIR", "ABS")
        for wn in order:
            Wd = WORLDS[wn]
            Ew = Wd["B"] @ Wd["B"].T
            lam_rw, rho32w, cw = DA.mirror_world_row(Ew, Wd["yn"])
            i1w, i2w = PX.pair_select(Wd["yn"])
            restw = [k for k in range(Ew.shape[0])
                     if k != i1w and k != i2w]
            rho0w = -float(Ew[i1w, restw] @ Ew[i2w, restw]) / cw
            exists = lam_rw < 1.0
            rtxt = ("%.4f" % rho32w if np.isfinite(rho32w)
                    and abs(rho32w) < 1e4
                    else ("NONFINITE" if not np.isfinite(rho32w)
                          else "%.3g" % rho32w))
            ki = None
            ncf = 0
            if wn in ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH",
                      "HL2"):
                ki, _loc, _nint, _kaps, ncf = \
                    FC.interval_census(Wd)
            cen[wn] = dict(lam=Wd["lam"], lam_rest=lam_rw,
                           rho32=rho32w, rho0=rho0w,
                           exists=exists, kint=ki, ncf=ncf)
            info("%s: S_- %d, lambda %.6g, lambda_rest %.6g "
                 "(mirror %s), rho_32 %s, rho_0 %.4g%s"
                 % (wn, len(Wd["yn"]), Wd["lam"], lam_rw,
                    "EXISTS" if exists else "DIVERGES", rtxt,
                    rho0w,
                    (", kappa_int %.6g" % ki)
                    if ki is not None else ""))
        lr_sep = (all(cen[wn]["lam_rest"] >= 1.0
                      for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
                  and all(cen[wn]["lam_rest"] < 1.0
                          for wn in ("MAIN", "TWIN")))
        ok_kint = (all(abs(cen[wn]["kint"] / KINT_REC[wn] - 1.0)
                       <= KINT_REC_TOL
                       for wn in ("EPST", "SCR", "SMOOTH",
                                  "HL2"))
                   and all(abs(cen[wn]["kint"] / KINT_LIVE_REC
                               - 1.0) <= KINT_LIVE_TOL
                           for wn in ("MAIN", "TWIN"))
                   and sum(cen[wn]["ncf"] for wn in cen
                           if cen[wn]["ncf"]) == 0)
        live_ok = all(cen[wn]["exists"]
                      and abs(cen[wn]["rho32"] - 1.0)
                      <= MIRROR_LIVE_BAR
                      for wn in ("MAIN", "TWIN"))
        dead_ok = all(not cen[wn]["exists"]
                      for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
        dir_side = {wn: ("DEAD-side (lambda_rest %.3g >= 1, "
                         "series %s)"
                         % (cen[wn]["lam_rest"],
                            "NONFINITE"
                            if not np.isfinite(cen[wn]["rho32"])
                            else "explodes %.3g"
                            % cen[wn]["rho32"]))
                    if not cen[wn]["exists"] else "LIVE-side"
                    for wn in ("DIR", "ABS")}
        if live_ok and dead_ok:
            mirror_tag = ("MIRROR_WORLD_CLAUSE_SEALED(live 2/2 "
                          "|rho_32 - 1| <= %.1f, dead 4/4 "
                          "diverge; DIRICHLET typed: DIR %s, ABS "
                          "%s -- the r347 typing reproduced)"
                          % (MIRROR_LIVE_BAR, dir_side["DIR"],
                             dir_side["ABS"]))
        else:
            mirror_tag = ("MIRROR_WORLD_INCOMPLETE(live_ok %s, "
                          "dead_ok %s; DIR %s, ABS %s)"
                          % (live_ok, dead_ok, dir_side["DIR"],
                             dir_side["ABS"]))
        world_txt = ("lambda_rest separates 4/4 (re-gated); "
                     "kappa_int == records at %.0f%%; NEW rho_0 "
                     "column: live %.4g/%.4g vs dead %s, DIR "
                     "%.4g / ABS %.4g (census, no bar)"
                     % (100 * KINT_REC_TOL, cen["MAIN"]["rho0"],
                        cen["TWIN"]["rho0"],
                        str({w: "%.3g" % cen[w]["rho0"]
                             for w in ("EPST", "SCR", "SMOOTH",
                                       "HL2")}),
                        cen["DIR"]["rho0"], cen["ABS"]["rho0"]))
        check("G71-worlds", lr_sep and ok_kint,
              "WORLD LEDGER: lambda_rest >= 1 on dead 4/4 and < 1 "
              "on live 2/2; kappa_int EPST %.6g / SCR %.4g / "
              "SMOOTH %.4g / HL2 %.6g == records at %.0f%%, live "
              "%.6f; THE SEALED MIRROR RULE => %s; %s"
              % (cen["EPST"]["kint"], cen["SCR"]["kint"],
                 cen["SMOOTH"]["kint"], cen["HL2"]["kint"],
                 100 * KINT_REC_TOL, cen["MAIN"]["kint"],
                 mirror_tag, world_txt))

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    mut1 = mutant_wrong_weight(Y9["dv"], Y9["al"], Y9["be"])
    dev_m1 = abs(mut1 - X9["dc"]) / abs(X9["dc"])
    mut1t = mutant_wrong_weight(np.array([0.125]),
                                np.array([1.0 / 16.0]),
                                np.array([1.0 / 32.0]))
    dev_m1t = abs(mut1t - float(dc_ex)) / float(dc_ex)
    check("G80-m1-wrong-weight", dev_m1 >= M1_BAR
          and dev_m1t >= MUT_MIN,
          "m1 THE WRONG RESOLVENT WEIGHT delta/(1+delta): breaks "
          "the exact split identity by %.1e rel at w9 (>= %.1f) "
          "and %.1e on the hand toy (>= %.0e) -- the geometric "
          "series weight is load-bearing, exactly CAUGHT"
          % (dev_m1, M1_BAR, dev_m1t, MUT_MIN))
    mut2 = mutant_mode_posthoc([0.4, 0.3, 0.2, 0.1])
    check("G81-m2-mode-posthoc", bool(hits_m2)
          and abs(mut2 - M90_Q) >= MUT_MIN,
          "m2 MODE SELECTION AFTER SIGHT: AST-FLAGGED (%s) and "
          "the toy posthoc quantile %.2f != the sealed M90_Q "
          "%.1f -- protocol-CAUGHT (the census quantile is a "
          "frozen module constant under the two-commit protocol)"
          % (hits_m2[0] if hits_m2 else "MISS", mut2, M90_Q))
    mut3 = mutant_delta0_readback()
    check("G82-m3-delta0-readback", bool(hits_m3)
          and abs(mut3 - DELTA0_MIN) >= MUT_MIN,
          "m3 DELTA_0 READ BACK from the withheld record "
          "exponent: AST-FLAGGED (%s; toy value %.3f) -- the "
          "REAL delta_0 is the sealed y0 fit, scope-audited "
          "CLEAN" % (hits_m3[0] if hits_m3 else "MISS", mut3))
    mut4 = mutant_toy_plant()
    check("G83-m4-toy-plant", bool(hits_m4)
          and abs((TOY_ALPHA - 0.5 * (TOY_AP + TOY_AQ)) - mut4)
          >= 0.01,
          "m4 SYNTHETIC MODEL WITH BUILT-IN TARGET: AST-FLAGGED "
          "(%s) and the sealed toy cancellation exponent %.3f "
          "differs from the planted record readback %.3f by >= "
          "0.01 -- the rate toys do NOT plant the record value, "
          "construction-CAUGHT"
          % (hits_m4[0] if hits_m4 else "MISS",
             TOY_ALPHA - 0.5 * (TOY_AP + TOY_AQ), mut4))
    mut5 = mutant_wrong_sign(R9["margin"], X9["g21"], Y9["a1"],
                             Y9["a2"], Y9["b1"], Y9["b2"])
    dev_m5 = abs(mut5 / Y9["cc2"] - 1.0)
    mut5t = mutant_wrong_sign(0.1, 7.0, 0.6, 0.8, -0.8, 0.6)
    dev_m5t = abs(mut5t / float(c_f) - 1.0)
    check("G84-m5-wrong-sign", dev_m5 >= M5_BAR
          and dev_m5t >= MUT_MIN,
          "m5 THE WRONG COUPLING SIGN (g21 a1 a2 - b1 b2): "
          "breaks c'_2 against its right-sign value by %.1e rel "
          "at w9 (>= %.1f) and %.1e on the rational toy (exact "
          "1/3) -- the SIGNED second-angle product is load-"
          "bearing, exactly CAUGHT" % (dev_m5, M5_BAR, dev_m5t))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism "
          "promoted, no certificate reading beyond the sealed "
          "census, no posthoc bar/band/family/prior move, no "
          "derived 5/7, NO RH claim, mincut unchanged; what the "
          "round adds: the order-0 split with its laws, the "
          "two-level dressed-scalar identity with the rate toys, "
          "the margin-pinning protocol, the dictionary sample "
          "clause, the weak family and the re-gated mirror world "
          "clause; r243..r347 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        if not audits_ok:
            main_v = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif rate_eq and ALPHA_SOURCE_CLOSED_FORM:
            main_v = "DELTA_SOURCE_DERIVED(unreachable this round)"
        elif rate_eq:
            main_v = ("RATE_EQUALITY_THEOREM(the common dressing "
                      "rate IS the margin rate: two-level "
                      "identity exact (Fractions + full chain), "
                      "rate toys exact (delta_x = alpha - a_x "
                      "iff flat geometry; naive equality holds "
                      "iff a_p == a_q == a_c, breaks by the bare "
                      "spread otherwise); LIVE certified census: "
                      "E1 pinning flats 3/3, E2 shadow med %.4f "
                      "<= %.2f, E3 sign %d/%d, E4 theorem image "
                      "max %.3f <= %.1f -- delta == alpha - a_c "
                      "loses its independent-law status)"
                      % (sh_med, SHADOW_MED_BAR, n_sgn,
                         len(all_kz), univ_max, UNIV_BAR))
        elif order0_law:
            main_v = ("ORDER0_LAW_FOUND(delta_0 %.3f; the "
                      "rate-equality clauses failed: E1 %s, E2 "
                      "%s, E3 %s, E4 %s)"
                      % (delta0, e1, e2, e3, e4))
        else:
            main_v = ("DELTA_IRREDUCIBLE(E1 %s, E2 %s, E3 %s, E4 "
                      "%s; y0 law %s -- delta resists the "
                      "decomposition, the specialist question is "
                      "final-sharpened)"
                      % (e1, e2, e3, e4, order0_law))
        o0_tag = (("ORDER0_LAW(delta_0 %.3f, curv %+.3f, EXT3 "
                   "%d/12, EXT4 %d/6; CARRIES_DELTA %s)"
                   % (delta0, laws["y0"]["curv"],
                      laws["y0"]["e3_in"], laws["y0"]["e4_in"],
                      "YES" if order0_carries else
                      "NO |%.3f - %.3f| = %.3f > %.1f"
                      % (delta0, delta, abs(delta0 - delta),
                         CARRY_BAR)))
                  if order0_law else
                  ("ORDER0_CENSUS(delta_0 %.3f, curv %+.3f, EXT3 "
                   "%d/12 low %d, EXT4 %d/6 low %d -- the y0 law "
                   "clauses fail as printed; CARRIES_DELTA %s)"
                   % (delta0, laws["y0"]["curv"],
                      laws["y0"]["e3_in"], laws["y0"]["e3_low"],
                      laws["y0"]["e4_in"], laws["y0"]["e4_low"],
                      "YES" if order0_carries else "NO")))
        parts = [
            main_v,
            o0_tag,
            ("DICT_T0_GO(%s)" if dict_go
             else "DICT_T0_CENSUS(%s)") % dict_txt,
            ("WEAK_FAMILY_SURVIVES(%s)" if weak_ok
             else "WEAK_FAMILY_STRAINED(%s)") % weak_txt,
            mirror_tag,
            "DECOMP_LEDGER(%s)" % dec_txt,
            "ORDER0_LEDGER(split max %.1e (bar %.0e), c'/c == "
            "y0 - rho_hi max %.1e (bar %.0e); y0 %.3f curv %+.3f "
            "EXT3 %d/12 EXT4 %d/6; rho_hi %.3f curv %+.3f; depth "
            "census med %.2e)"
            % (max_split, SPLIT_BAR, max_cpc, CPC_ID_BAR,
               laws["y0"]["slope"], laws["y0"]["curv"],
               laws["y0"]["e3_in"], laws["y0"]["e4_in"],
               laws["rhi"]["slope"], laws["rhi"]["curv"],
               depth_med),
            "MODE_CENSUS_LEDGER(medians: top1 %.4f, M90 %.0f, "
            "T0arch %.4f, arch_top %.4f, peel_top %.4f)"
            % (med_top1, med_m90,
               float(np.median([YT[k]["t0arch"]
                                for k in fit_kz])),
               float(np.median([YT[k]["arch_top"]
                                for k in fit_kz])),
               float(np.median([YT[k]["peel_top"]
                                for k in fit_kz]))),
            "WEAK_LEDGER(%s)"
            % "; ".join("kz%d rho0 %.4f sh %.4f/%.4f/%.4f Kres "
                        "%d mass2 %.4f pmass %.4f"
                        % r[:8] for r in weak_rows),
            "WORLD_LEDGER(%s)" % world_txt,
            "TWIN_LEDGER(rho0 dev %.1e, y0 dev %.1e, shadow "
            "devs <= %.1e, ratio devs <= %.1e)"
            % (devT["rho0"], devT["y0"], devT["sh"],
               devT["ratio"]),
            "MUSTFAIL_LEDGER(m1-m5 + scopes)",
        ]
        verd = " + ".join(p for p in parts if p)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy + sealed adjudication of the "
          "delta source; NO L* claim, NO RH claim"
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
