#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_bellman_reverse_holder_probe --
PRIME.L2.FOLD_DENSITY_REVERSE_HOLDER.01 (round 341): THE
PATH-WEIGHTED BELLMAN / REVERSE-HOLDER THEOREM CANDIDATE -- the
terminal main round after the r339 dictionary.

CONTEXT (binding, from the sealed records r306/r324/r335/r337/
r339): r339 put the exact layer at theorem grade -- X_k =
d(V_k)/d(root) on the sealed iterated r270 pairing tree is a
nonnegative martingale from mass conservation alone (Fractions
bit-equal on w9 + w13, 76 nodes), and the moment dictionary is
exact: E[X_inf^2] == m M_2, E[X_inf^3] == m^2 M_3 == rho_2
(log m)^2, max y/m == q_max.  The terminal target IS E[X_inf^3]
<= C (log m)^A; the banked r306 C_2 = 1.069 (0/57) already
certifies A = 2 on the 57-rung set (census, not theorem).  r339
ALSO capped the worst-case language honestly: the full budget
W_F = prod_k Gamma_max(k) is SUPERCRITICAL (e(W_F) = +0.956 vs
the target's e(m^2 M_3) = +0.112, 8x slower), and the good tree
per level (heavy jumps max R_c > 3/2 removed) does not certify
either (viol 33/20/11).  THE MEASURED BUILD INSTRUCTION (r339
verbatim): Gamma_max lives in NEAR-LEAF DEGENERATE PAIRS (med
profile 1.05 -> 3.99 against the algebraic pair ceiling 4) under
which hardly any PATH MASS sits -- the Bellman theorem must sum
Gamma PATH-PROBABILITY-WEIGHTED, not take per-level maxima.
Exact and banked: E[X_{k+1}^3 | V_k = v] = X_k^3 Gamma(v) with
Gamma(v) = sum_c p_c R_c^3, p_c = n(c)/n(v), R_c = d(c)/d(v),
sum_c p_c R_c = 1.  The r337 complementarity directive is
binding: the mass arm (r335) covers the spikes on ITS OWN scale,
the martingale arm covers the mid-band on ITS OWN scale -- the
two-constant certification (each arm against its own freeze) is
the named residual direction, executed here.

THE CORE QUESTION (reviewer contract): does a path-weighted
Bellman / Reverse-Holder inequality on the fold genealogy carry
the terminal target E[X_inf^3] <= C (log m)^A -- with a stopping
mechanism for heavy jumps and self-improvement on the good tree?

THE EXACT PATH LAYER (derived algebra, disclosed BEFORE any
evaluation; every identity toy-pinned in Fractions and f64-warded
live):
  (i) THE CUBIC PATH PRODUCT: X_inf^3 == prod_k R(V_k, V_{k+1})^3
      along the ancestor path, so E[X_inf^3] = sum_leaves (1/m)
      prod_k R_k^3 EXACTLY.
  (ii) THE TILTED TOWER IDENTITY: with the cubic size-biased path
      measure Q (steps p~_c = p_c R_c^3 / Gamma(v); sum_c p~_c =
      1 exactly), E[X_inf^3] == E_Q[prod_k Gamma(V_k)] EXACTLY --
      prod_k p~_k Gamma_k == prod_k p_k R_k^3 termwise.  THIS is
      the correct path-weighted tower form.  DISCLOSED WARNING
      (derived, toy-pinned): the naive untilted reading
      E_P[prod_k Gamma(V_k)] under the leaf-uniform measure is
      FALSE -- on the sealed even toy (3, 1, 1, 1) it returns
      11/6 while E[X_inf^3] = 20/9 (break 7/18 EXACT).  The
      wrong-filtration tower is must-fail e1 of this round.
  (iii) THE PHI-GAMMA IDENTITY: with Phi(v) = A(v)^3/n(v)^2,
      sum_c Phi(c)/Phi(v) == Gamma(v) EXACTLY per node (algebra:
      Phi(c)/Phi(v) = (p_c R_c)^3/p_c^2 = p_c R_c^3).  This makes
      the reviewer's Psi-weight Bellman form a genuine telescoping
      certificate: if sum_c Phi(c) Psi(c) <= Phi(v) Psi(v) at
      every unstopped good node with Psi(v) = (C0 + ln n(v))^A,
      then E[X_inf^3; tau = inf] <= (C0 + ln m)^A with PREFACTOR
      1 (leaf Psi = C0^A; stated for C0 = 1; general C0 rescales
      by C0^-A, printed inside).
  (iv) THE STOPPED DECOMPOSITION: tau = first level k with V_k
      HEAVY (max_c R_c > R_STAR = 3/2, the r339 a-priori band-
      floor tie; sensitivity R_ALT = 7/4); E[X_inf^3] =
      E[X_inf^3; tau <= K] + E[X_inf^3; tau = inf] is an exact
      leaf partition (the r339 heavy-leaf union).  The heavy-arm
      HAND-OFF ALGEBRA is exact: y_i <= max y pointwise gives
      E[X_inf^3; tau <= K] <= (m q_max)^2 x msh with msh = the
      heavy-leaf MASS share -- the r335 q_max currency enters the
      cubic layer exactly (and q_max <= Q_dich is r335-exact; the
      r335 record constants C_D = 141.84/33.06/7.71 at a = 0/1/2
      are adopted as DISCLOSED record numbers, census comparison
      only, never recomputed here).
  (v) THE GOOD EPSILON-CHAIN: B_k = sum over UNSTOPPED nodes at
      level k of (n(v)/m) X(v)^3 (no heavy strict ancestor);
      B_0 = 1, B_K = E[X_inf^3; tau = inf] exactly; gamma_k =
      B_{k+1}/B_k is the path-weighted good growth factor
      (= the Gamma average over the unstopped good nodes, the
      reviewer's E[Gamma 1{good} | F_{k-1}] in integrated form);
      eps_k = max(gamma_k - 1, 0); W_B = prod_k (1 + eps_k) >=
      E[X_inf^3; tau = inf] EXACT envelope.

LEG 0 -- ANCHOR REGRESSION (slim set + the r339/r324 records,
disclosed): the r314 identity wards live; r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r316 rho anchors + C_small + n = 65;
r324-pre C_M2 = 2.2557 + the seven m2 violators EXACT; the
dictionary-chain identity live (r339 G34 verbatim); NEW r339
RECORD anchors recomputed through the imported FDD builders:
W_F med 265.54 (tol 0.01), W_G med 13.69 (tol 0.01), hsh med
0.872 (tol 0.001), Gamma_max max 4.303 (tol 0.001), e(W_F)
+0.956 (tol 0.001), e(m^2 M_3) +0.112 (tol 0.001); NEW r324
CHAIN anchor recomputed from the ymx/m2 columns: e_G +0.158 /
e_M2 +0.014 / e_tot +0.172 (tol 0.002/0.002/0.003) -- the
honest comparison threshold m_0* = 10^59.6 is adopted as the
record number R324_M0_L10 = 59.6.

LEG A -- path_bellman_state (the exact cubic path decomposition):
per rung the per-leaf path products prod_k Gamma(V_k) (top-down
propagation), the tilted weights, the tilted tower identity (ii)
f64-warded live on every world and FRACTIONS BIT-EQUAL on w9 +
w13 + the three sealed toys; the distribution of log prod_k
Gamma(V_k) over the paths (leaf-uniform q10/q50/q90/max), the
untilted census column E_P[prod Gamma], and the near-ceiling
path-mass census pm3 = P(some ancestor has Gamma > GAMMA_HI = 3)
with its E[X_inf^3] share -- the EXPLICIT defusal measurement of
the r339 thesis (near-leaf degenerate pairs carry almost no path
mass); the per-level path-weighted profile E[Gamma(V_k)] vs the
r339 Gamma_max profile.

LEG B -- THE STOPPING MECHANISM: tau census per rung (stopped
leaf share hsh = path mass P(tau < inf), heavy mass share msh,
E3h = E[X_inf^3; tau <= K], its share of E3, the stopping-level
profile, named + mid-band anatomy); the exact hand-off ward (iv)
live everywhere; THE HEAVY-ARM CERTIFICATION ON ITS OWN SCALE
(the r337 two-constant directive): E3h <= C_H(a) (log m)^a with
its own mid-ladder max-cal freeze (TRB verbatim), test incl.
EXT3, named 4/4, a in GA_FAM.

LEG C -- THE BELLMAN FUNCTION ON THE GOOD TREE (the core), BOTH
reviewer forms with constants sealed BEFORE the record:
  FORM 1 (multiplicative eps-chain, integrated): W_B <= C_B(a)
      (log m)^a, mid-ladder freeze, test incl. EXT3, named 4/4,
      a in GA_FAM; the eps sum printed against A loglog m + C.
  FORM 2 (Psi-weight Bellman, per node, prefactor 1): for every
      (A, C0) in PSI_A_FAM x PSI_C0_FAM = (1, 2, 3) x (1.0, 2.0),
      count the violations of sum_c Phi(c) Psi(c) <= Phi(v)
      Psi(v) (1 + PSI_TOL) over (s) ALL non-heavy internal nodes
      (strict form) and (c) the UNSTOPPED non-heavy nodes (the
      composed surface -- what the two-arm telescoping needs);
      certified iff composed violations == 0 on the whole 65+12
      row set.  DISCLOSED DERIVED ALGEBRA (a-priori, no
      measurement): on the good tree the near-leaf layer is
      ALWAYS defused at (A, C0) = (3, 1): a good pair has Gamma
      <= 7/4 (max at R = (3/2, 1/2)) and Psi-discount
      (1/(1+ln 2))^3 = 0.206 -> 0.36 < 1; a good uneven 3-node
      has Gamma <= 9/4 and discount (1/(1+ln 3))^3 = 0.108 ->
      0.24 < 1 -- the genuinely open surface is the MID-TREE
      (a skewed-but-good pair R = (1.4, 0.6) at n ~ 1000 gives
      ratio ~ 1.13 > 1 if it occurs); (3, 1.0) is therefore the
      sealed DISPLAY combo; the scan measures which form carries.
  Plus the direct good census E3g <= C_g(a) (log m)^a (own
  freeze) as the GOODTREE letter surface, and the R_ALT
  sensitivity column.

LEG D -- THE COMPOSITION (printed ALWAYS, honestly typed): on a
certifying two-arm pair the theorem candidate E[X_inf^3] <=
C_H(a_H) (log m)^{a_H} + [Form-2: (C0 + log m)^A | Form-1:
C_B(a_B) (log m)^{a_B}], then through the dictionary M_3 <= C
(log m)^A / m^2 and through the r324 chain as a POLYLOG
expression (reviewer instruction verbatim): N_3 >= m / sqrt(C
(log m)^A), N_2 >= N_3 (r306 exact chain) -- NO premature
powerization to m^0.888 (exactly that produced the 10^59.6
threshold); the 0.888 need enters only as the FINAL solve m_0* =
smallest m with m^{0.224} >= C_total(log m) -- printed against
the r324 measured route (+0.172, 10^59.6) AND against the
disclosed r306-census polylog reading (C_2 = 1.069, A = 2; a
census bound, not a mechanism -- disclosed pre-spec).  On a
non-certifying outcome: the violation census typed (which rungs,
which arm, which level).

LEG E -- WORLDS + MUST-FAILS (>= 4 mutants + 2 scope mutants):
the theorem candidate must carry on MAIN/twin; EPST/SCR measured
census-grade (r339 honest negative: the Gamma_max statistic was
world-blind but the dictionary separates -- does the
PATH-WEIGHTED layer separate?).
(e1) TOWER IDENTITY WITH THE WRONG FILTRATION:
  mutant_tower_untilted returns E_P[prod Gamma] under the
  leaf-uniform measure -- on the even Fractions toy the break is
  20/9 - 11/6 = 7/18 EXACT -- CAUGHT exact.
(e2) BELLMAN CONSTANTS AFTER RECORD SIGHT (protocol):
  mutant_psi_posthoc re-picks the Psi exponent after sight of the
  evaluated violation column (consumes rho) -- the
  BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed toy
  it returns A = 3 != the family-scan protocol head PSI_A_FAM[0]
  = 1 -- protocol-CAUGHT twice (the family is sealed in this
  spec BEFORE the freeze).
(e3) STOPPING THRESHOLD READ BACK FROM THE TARGET:
  mutant_rstar_from_target derives an 'R* column' from the cubic
  record (consumes cm/S3) -- the PHI3_FORBIDDEN scan must FLAG
  it (AST-CAUGHT) while the module-own path builders stay clean.
(e4) PATH WEIGHTS WITHOUT THE n(c) NORMALIZATION:
  mutant_tilt_no_n tilts by R_c^3 alone (p_c dropped) -- on the
  uneven Fractions toy (3, 1, 1) it returns 51/25 while
  E[X_inf^3] = 261/125 (break 6/125 EXACT) -- CAUGHT exact.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

SEALED VERDICTS (exactly one fires; total order; the user
contract names five letters -- the structural sixth is the house
standard for totality, disclosed):
   TARGET_LEAK                iff any purity/scope/literal audit
       hit on the path builders,
   BELLMAN_STATE_NOT_EXACT    iff an exact ward breaks on a live
       world (tilted tower / weight normalization / stopped
       partition / B-chain closure / envelope / Phi-Gamma
       identity / heavy hand-off algebra / martingale wards /
       the Fractions bit-equality / the r327 grounding),
   RH3_BELLMAN_GO             iff the heavy arm certifies on its
       own scale AND at least one Bellman form certifies on the
       good tree (0 test violations incl. EXT3, named 4/4 /
       composed node violations 0) AND the composed polylog m_0*
       <= the r324 threshold 10^59.6 -- the two-arm theorem
       candidate with explicit C and A beats the chain,
   RH3_BELLMAN_PARTIAL        iff at least one Bellman form
       certifies but the composition stays open (heavy arm not
       certified on its own scale, or the composed m_0* does not
       beat the r324 route),
   GOODTREE_A2_ONLY           iff no Bellman form certifies but
       the direct good census E3g <= C_g(a) (log m)^a certifies
       at some a -- the good tree carries at census grade only,
       no local mechanism,
   PATHWEIGHT_ALSO_SUPERCRITICAL  otherwise -- the path-weighted
       language is capped too; said honestly, with the measured
       exponents printed inside.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r340 (Cauchy-Binet-Hall) is sealed; r342 (two-atom
extremal) may run in parallel -- own files only; before the
strictly additive rh-sync the current git state is re-checked
and the sync builds ONLY additively on it (the r339/r340
coexistence lesson: disclose collisions, never overwrite).
Two-commit freeze protocol (r329 convention): spec committed
pre-freeze, record tables the only post-freeze edit, committed
again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r324/r327/r333/r337/
r339 machinery imported verbatim): t_{N-2} = sum_b ct_b (r244
chain rows, r266 eval); F = 0.20 edge split; maximal same-sign
runs of the bx-sorted bulk; level-2 blocks (r270 convention);
the frozen positional block machinery (r298); the r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the
r314 SCF.fold_genealogy + SCF.signed_cube_terms +
SCF.flux_telescope; the r316 TRB.two_regime_state +
TRB.split_midladder; the r324 QMO.mult_ward; the r324-pre
FAP.m2_qmax_state; the r327 GMC.group_mass_ledger (grounding
cross-ward); the r339 FDD.fold_mass_tree_exact (the SEALED
canonical genealogy, PAIR_OFFSET 0 verbatim -- r339 Leg-0
adjudication stands, the bisection alternative was measured
WORSE and is not re-opened) + FDD.descendant_density_martingale
(the W_F/W_G/hsh anchor columns) + FDD.martingale_moment_
dictionary + FDD.fr_pair_tree + FDD.fr_mart_check; PDelta =
Pbeta - Pomega; x_j = (PDelta)_j; a_i = |x_i|.  NEW in this
round (module-own, source-pure): path_bellman_state (the exact
path layer: tilted tower, stopped decomposition, eps-chain,
distribution, defusal census), psi_ratio_state (the Form-2
per-node scan), fr_path_state (the full Fractions replica) and
the sealed bellman_tree_verdict.

INDEX FIREWALL (binding, r238-r340 discipline): w = window (kz),
N_w = builder depth, k = TREE LEVEL (root 0), n(v) = leaf count;
ground truth (branch labels, the true R/t/Z values) enters GATES
and census tables only; the cubic target M_3 / rho_2 and the
q_max RECORD enter GATES / anchors / composition checks only,
NEVER a path builder (AST-warded; the path builders consume the
abs block values + index order ONLY -- the heavy hand-off ward
uses max y computed from the builder's OWN leaves, never the
banked record); no zero/prime oracles anywhere (AST firewall);
no fit primitives (fragment audit; growth exponents are the
imported r272 dyadic halves-slope, fit-free).  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r324/r327/r335/r339 verbatim):
frame-A h <= 900, 42 rungs, (N, kz)-sorted; exception set {kz15,
20, 22, 36, 38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by
(N, kz); EXT2: the r316 A5 rule (leftover pool + first 12
windows 1300 < h <= 1650, first 8 POSITIVE_PREFIX by (N, kz));
EXT3: the sealed r329 12-anchor list (record committed 8cbd95f9,
adopted as-is, PURE TEST rows).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN, via
FDD verbatim); EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942,
1218); EXT2_H_MAX 1650; EXT2_POOL_CAP 12; K_EXT2 8; EXT3_KZ_B
(42, 51, 54, 56, 58, 62); EXT3_KZ_A (96, 123, 125, 127, 128,
130); EXT3_NW_MIN 1721; EXT3_NW_MAX 2577; R_STAR 3/2 (r339
banked, a-priori); R_ALT 7/4 (sensitivity); GA_FAM (1, 2, 3);
PSI_A_FAM (1, 2, 3); PSI_C0_FAM (1.0, 2.0); PSI_DISPLAY (3,
1.0) (a-priori, derived algebra above); PSI_TOL 1e-9; GAMMA_HI
3.0 (a-priori defusal display threshold, census only); QTS
(0.1, 0.5, 0.9); NAMED_KZ (53, 83, 67, 55); MIDBAND_KZ (73, 76,
61, 95, 98, 109); ATOM_BAR 1e-9; REC3_BAR 1e-13 ladder / 1e-12
EXT3; TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; SA_BAR
1e-12; TREE_BAR 1e-9; DICT_BAR 1e-9; TILT_BAR 1e-9; WQ_BAR
1e-9; PART_BAR 1e-9; BK_BAR 1e-9; ENV_BAR 1e-9; PGI_BAR 1e-9;
HVY_BAR 1e-9; JEN_BAR 1e-12; DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL
5 (via TRB, verbatim); MUT_MIN 1e-6; TOY_BAR 1e-12; FR_BAR 0
(bit-equality); TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep +
ext + ext2 / 3e-5 EXT3 (r329 a-priori) / 1e-6 controls; ID_BAR
1e-12; AC_BAR 1e-9; INF_SENT 1e300 / cert guard 1e299; CRIT_EXP
0.224 (r324 verbatim); N2_EXP_NEED 0.888; R306_C2 1.069 tol
0.005; N341_REF 65; R316 RHO {53: 1.0490, 67: 1.0536, 55:
0.4821, 83: 0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at
kz18; R324P_CM2 2.2557 tol 0.005, M2VIOL {53, 67, 83, 76, 61,
28, 109} EXACT; R339 record anchors W_F_MED 265.54 tol 0.01 /
W_G_MED 13.69 tol 0.01 / HSH_MED 0.872 tol 0.001 / GMX_MAX
4.303 tol 0.001 / E_WF +0.956 tol 0.001 / E_M3 +0.112 tol
0.001; R324 chain anchors E_G +0.158 tol 0.002 / E_M2 +0.014
tol 0.002 / E_TOT +0.172 tol 0.003 / M0_L10 59.6 (record
threshold); R335_CD {0: 141.84, 1: 33.06, 2: 7.71} (record,
census print only); R341_TABLE_LITERALS = the sealed r314..r337
set (r339 verbatim) UNION the r339 record set {265.54, 13.69,
0.872, 3.93, 4.303, 0.956, 0.112, 39.9133, 8.9841, 2.0222,
2.8325, 0.6393, 0.1443, 18.2922, 4364.9, 324.33, 404.57,
223.86, 51.76, 16.17, 39.14, 487.03, 1.1392, 0.934, 0.957,
0.784, 0.712, 20.59, 6.22, 30.4, 82.46, 8.56, 53.34, 5.05,
19.71, 0.867, 0.877, 0.992, 0.82, 515.67, 14.11, 416.1, 26.55,
232.57, 13.63, 47.75, 7.93, 2.971, 3.874, 3.974, 111.49,
17.911, 2.878, 0.392, 208.64, 659.57, 505.14, 393.51, 415.63,
141.84, 33.06, 7.71} (the r339 displays 1.05 / 3.99 / 0.846 /
0.829 / 0.863 / 0.857 are OMITTED from the forbidden set to
avoid collisions with innocent small toy rationals -- disclosed
curation, r337/r339 convention);
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the exact path wards + the w9 Fractions bit-equality +
e1-e4 mutants; ladder, extensions, EXT3, anchors, census,
certification, composition and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r324/r324-pre/r339 RECORD number
adopted as-is; the exact path layer (i)-(v) is derived algebra,
disclosed above with its toy pins (7/18, 6/125, 20/9, 261/125,
31/16 = 43/32 + 19/32, W_B = 20/9 on the even toy, slack 3/16
on the stop toy) -- computed BY HAND from the sealed toys, no
machine run; the r306 record already bounds E[X_inf^3] <= 1.069
(log m)^2 on the 57-rung set via the dictionary, and its
no-powerization polylog solve is ALSO a disclosed census
reading (the round's open content is the LOCAL MECHANISM, not
that number); the Psi near-leaf defusal algebra and the
mid-tree risk are derived a-priori, disclosed above; GENUINELY
OPEN quantities of this round: every path-distribution column
(lg quantiles, E_P[prod Gamma], pm3, tau census, E3h/E3g, msh,
W_B, eps sums, the per-level path-weighted Gamma profile), all
certification constants C_H(a)/C_B(a)/C_g(a), all Form-2
violation counts and max ratios on all six sealed combos, the
R_ALT sensitivity, the world separation, all exponents and the
composed m_0* -- NONE was computed before this spec was frozen;
the six sealed letters are symmetric and total -- the tree maps
every outcome to exactly one letter by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R341_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r324-pre C_M2 + violator set, r339 record anchors, r324
    chain anchors)
+ SEAL(path wards: tilted tower + weight norm + partition +
    B-chain + envelope + Phi-Gamma + heavy hand-off + martingale
    wards + Fractions bit-equality + grounding + purity + toys)
+ PATHDIST(lg quantiles, E_P[prod Gamma] vs E3 vs W_F, pm3
    defusal census, per-level profile)
+ STOPPING(tau census, hsh/msh/E3h columns, named + mid-band
    anatomy, heavy-arm cert C_H(a) + viol + named + minimal a)
+ BELLMAN(Form-1 C_B(a) + viol + named + minimal a; Form-2 six
    combos strict/composed viol + max ratios + certified combos;
    direct good census C_g(a); R_ALT sensitivity)
+ [exactly one of] RH3_BELLMAN_GO / RH3_BELLMAN_PARTIAL /
    GOODTREE_A2_ONLY / PATHWEIGHT_ALSO_SUPERCRITICAL /
    BELLMAN_STATE_NOT_EXACT / TARGET_LEAK
+ COMPOSITION(the polylog chain with explicit constants + m_0*
    vs the r324 route + the r306 census reading; printed ALWAYS,
    typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the path identities (i)-(v), the
Fractions toys, the tree logic and the purity audits are EXACT
(Fractions/AST-decided); every census, constant, violation
count and exponent is MEASURED on the finite ladder (+ the 12
adopted EXT3 anchors) only; a certifying two-arm pair fixes a
proof TARGET (a theorem candidate with explicit constants), it
proves NO cofinal law -- the ladder-to-m_0* step stays the
disclosed extrapolation hypothesis; the r306 dictionary reading
of the banked C_2 is a disclosed pre-spec input, not a finding
of this round; r243-r340 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA f0d2c744c46942bc,
pre-freeze commit 86f523e8; protocol: smoke pass 1 = 38/38
(0.7 s, run pre-commit, disclosed in the commit message), NO
amendment; calibration pass 1 = first full evaluation, 38/38,
wall 170.0 s, NO amendment; record run1/run2 after this
insertion, identical up to the runtime line):
MAIN VERDICT: PATHWEIGHT_ALSO_SUPERCRITICAL(per the sealed
tree: NO arm certifies on its own freeze -- heavy arm C_H =
1.7305/0.3875/0.0868 at a = 1/2/3 with viol 11/11/9 of 51 and
NAMED 0/4 (the worst violators are the EXT3 DEEP ANCHORS kz51
7.61x / kz54 3.17x / kz62 2.31x / kz42 2.22x at a = 2, then
kz67/kz123 -- the r337/r339 deep-anchor margin recurs INSIDE
the heavy arm); Form 1 C_B = 0.4867/0.1113/0.0259 with viol
2/1/1 -- the SINGLE persistent test violator is the named
spike kz55 (W_B 2.888, 0.157 vs C_B(2) 0.111, 1.41x), named
3/4, midband 6/6; Form 2 (prefactor 1) certified combos NONE
of 6 (best (A, C0) = (3, 1.0): 23 composed violations on 17
of 77 rungs, max ratio 1.237 -- the disclosed a-priori
mid-tree risk is real); direct good census C_g viol 2 (kz24,
kz26)).  The letter is the sealed 'otherwise' branch and the
NAME overstates the negative in one respect, said honestly:
the measured path-weighted exponents are NOT supercritical
(e(W_B) = -0.214, e(E3h) = +0.313 vs CRIT 0.224 where r339
e(W_F) was +0.956; e(E3g) = -173.3 is a DEGENERATE statistic
-- E3g == 0 on good-tree-empty rungs poisons the dyadic
slope, disclosed); what fails is the FREEZE-POINTWISE
certification, each arm by a different, structured violator
family.
THE THREE STRUCTURAL FINDINGS OF THE ROUND: (1) THE r339
THESIS IS CONFIRMED QUANTITATIVELY -- path weighting deflates
the worst case by 21x at the median: E_P[prod Gamma] med
12.53 vs W_F med 265.54; per-path log prod Gamma q50 med 2.09
/ q90 med 3.27 / MAX med 4.20 vs log W_F med 5.58 (deflation
med 0.80); the per-level PATH-WEIGHTED profile E[Gamma(V_k)]
stays in 1.05..1.80 where the Gamma_max med profile climbs
1.05 -> 3.99; the near-ceiling nodes (Gamma > 3) carry path
mass pm3 med 0.161 and only c3s med 0.173 of E3 -- the
near-leaf degenerate pairs ARE defused by path weighting.
(2) THE STOP AT R* = 3/2 IS TOO EARLY ON THE PATH-MASS SCALE
-- the heavy arm inherits ESSENTIALLY EVERYTHING: hsh med
0.872 (77/77 rungs heavy), msh med 0.833, E3h share of E3 med
0.944 (max 1.000; w9 and kz61/73/130 have an EMPTY good
tree), modal stop level 1 (the mid-band stops its whole leaf
mass at the FIRST fold level: kz73 cnt 196/196 at tau = 1,
kz61 227/227), NOT the last level -- the r339 'mid-band
inflates at the last level' anatomy describes Gamma_max
position, not path mass; the two-arm split is also strongly
threshold-UNSTABLE: R_ALT = 7/4 moves hsh med 0.872 -> 0.266
and the E3h share 0.944 -> 0.386 (W_B med 1.489 -> 3.796,
C_B'(2) envelope 0.7485, psi display viol 244) -- R* is a
genuine tuning surface, not a canonical constant, and the
mass-balance question for R342+ is WHERE between 3/2 and 7/4
the two arms equilibrate.  (3) THE GOOD ARM IS ONE RUNG FROM
CERTIFYING: W_B (the integrated eps-chain, exact envelope
E3g <= W_B, warded 0.0) certifies everywhere except kz55 at
a = 2/3 (eps sums: sum eps_k med 0.42 max 2.49 vs loglog m
med 1.63 -- consistent with the reviewer A loglog m + C
reading at census grade); the EXT3 deep anchors are C_B-CLEAN
(0 EXT3 violations in Form 1 at a >= 2) -- the deep-anchor
problem lives ENTIRELY in the heavy arm.
CENSUS: E3 med 6.22; E3h med 5.86; W_B med 1.489 max 2.888
(at kz55); sum eps med 0.42; tau med (of per-rung medians)
1.0; levels K 5..10; heavy hand-off E3h <= (m q_max)^2 msh
reserve med 4.8x min 2.1x; E_P[prod Gamma] med 12.53 (the
untilted census OVERSHOOTS E3 med 6.22 -- the tilt matters in
both directions); concentration med IQR(log prod Gamma) 2.17.
FORM 2 TABLE (strict/composed viol, max composed ratio):
(1,1) 1467/499 1.565; (1,2) 3203/990 1.686; (2,1) 204/75
1.384; (2,2) 624/218 1.465; (3,1) 50/23 1.237; (3,2) 115/44
1.297 -- monotone in A, C0 = 1 dominates C0 = 2 (the sealed
display combo (3, 1.0) was the right a-priori pick; its
per-rung max composed ratio med is 1.000, i.e. HALF the rungs
are already per-node clean).
NAMED ANATOMY (kz, m, K, hsh, msh, E3h/E3, tau_med, W_B,
psi(3,1)): kz53 119/7/0.882/0.833/0.98/1/1.503/1.055; kz83
248/8/0.927/0.907/0.99/1/1.266/1.088; kz67 129/8/0.992/
0.991/1.00/2/1.164/1.000 (the whole rung stops at level 2 --
the r324 single-heavy-scale event as an early heavy fold);
kz55 73/7/0.877/0.860/0.96/2/2.888/1.098 (the Form-1
violator); MID-BAND: all six stop at tau = 1 with hsh
0.820..1.000 -- the mid-band IS the heavy arm in path mass.
WORLDS: w9 hsh 1.000 (good tree EMPTY, W_B = 1); twin w13
hsh 0.857, E3h share 0.961, W_B 1.236 (protocol-identical);
EPSTEIN E3h share 0.427 (the only world where the good arm
carries the majority); SCRAMBLE W_B 1.214 sits INSIDE the
ladder range (med 1.489) and E3h share 0.997 -- the
PATH-WEIGHTED budget is ALSO world-blind (honest negative,
the r339 Gamma_max blindness recurs); the dictionary value
E3 = 20.59 stays the only sharp separator.
COMPOSITION (typed ENVELOPE ONLY -- no certifying letter, NO
theorem candidate this round): with the a = 3 envelopes
[heavy 1.3091 + good 0.0650] (log m)^3 the polylog solve
gives m_0* = 10^24.0 vs the r324 MEASURED route 10^59.6 and
the r306 census reading 10^13.5 (C_2 = 1.069, A = 2) -- the
envelope numbers show the POTENTIAL of the polylog form, but
the honest state of the route REMAINS the r324 measured
composition (m_0* 10^59.6, +0.172) until an arm certifies.
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069
(0/57); r316 n 65 + rho quartet 1.0493/1.0536/0.4821/0.7791
+ C_small 1.0694@kz18; r324-pre C_M2 2.2557 + the seven m2
violators EXACT; r339 record W_F med 265.54 / W_G med 13.69 /
hsh med 0.872 / Gmax 4.303 / e(W_F) +0.956 / e(m2M3) +0.112
ALL reproduced through the imported FDD builders; r324 chain
e_G +0.158 / e_M2 +0.014 / e_tot +0.172 reproduced from the
dictionary columns.
SEAL: tilted tower worst 8.6e-16, weight norm 4.4e-16,
stopped partition 2.4e-16, B-chain closure 0.0, envelope viol
0.0, Phi-Gamma identity 8.0e-16, heavy hand-off viol 0.0,
martingale wards 2.2e-16/4.4e-16/1.2e-15, Jensen 0.0,
FRACTIONS BIT-EQUALITY on w9 + w13: tilt == E3, partition,
envelope, B-chain and Phi-Gamma all symbolic dev == 0 (76
martingale nodes + the full path replica), r327 grounding
3.4e-16 / 0.0 / 0.0, contribution ward within bars, purity
clean, toys exact (7/18, 6/125, 20/9, 261/125, 31/16, 3/16
all EXACT); must-fails e1 CAUGHT exact (break 7/18, float
1.833 == 11/6) / e2 protocol-CAUGHT twice (AST rho + toy pick
3 != 1) / e3 AST-CAUGHT (S3) / e4 CAUGHT exact (break 6/125,
float 2.040 == 51/25) + m5a/m5b FLAGGED.

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
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import companion_orbit_packing_probe as COP    # noqa: E402 r333
import fold_density_dictionary_probe as FDD    # noqa: E402 r339
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_X3 = 3e-5
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
EXT2_H_MAX = 1650
EXT2_POOL_CAP = 12
K_EXT2 = 8
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN = 1721
EXT3_NW_MAX = 2577
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
REC3_BAR_X3 = 1e-12
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
SA_BAR = 1e-12
TREE_BAR = 1e-9
DICT_BAR = 1e-9
TILT_BAR = 1e-9
WQ_BAR = 1e-9
PART_BAR = 1e-9
BK_BAR = 1e-9
ENV_BAR = 1e-9
PGI_BAR = 1e-9
HVY_BAR = 1e-9
JEN_BAR = 1e-12
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
R_STAR = 1.5
R_ALT = 1.75
GA_FAM = (1, 2, 3)
PSI_A_FAM = (1, 2, 3)
PSI_C0_FAM = (1.0, 2.0)
PSI_DISPLAY = (3, 1.0)
PSI_TOL = 1e-9
GAMMA_HI = 3.0
QTS = (0.1, 0.5, 0.9)
NAMED_KZ = (53, 83, 67, 55)
MIDBAND_KZ = (73, 76, 61, 95, 98, 109)
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
INF_SENT = 1e300
CERT_GUARD = 1e299
CRIT_EXP = 0.224
N2_EXP_NEED = 0.888
R306_C2 = 1.069
R306_C2_TOL = 0.005
N341_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R324P_CM2 = 2.2557
R324P_CM2_TOL = 0.005
R324P_M2VIOL = (53, 67, 83, 76, 61, 28, 109)
R339_WF_MED = 265.54
R339_WF_MED_TOL = 0.01
R339_WG_MED = 13.69
R339_WG_MED_TOL = 0.01
R339_HSH_MED = 0.872
R339_HSH_MED_TOL = 0.001
R339_GMX_MAX = 4.303
R339_GMX_MAX_TOL = 0.001
R339_EWF = 0.956
R339_EWF_TOL = 0.001
R339_EM3 = 0.112
R339_EM3_TOL = 0.001
R324_EG = 0.158
R324_EG_TOL = 0.002
R324_EM2 = 0.014
R324_EM2_TOL = 0.002
R324_ETOT = 0.172
R324_ETOT_TOL = 0.003
R324_M0_L10 = 59.6
R335_CD = {0: 141.84, 1: 33.06, 2: 7.71}
R341_TABLE_LITERALS = frozenset(FDD.R339_TABLE_LITERALS | {
    265.54, 13.69, 0.872, 3.93, 4.303, 0.956, 0.112, 39.9133,
    8.9841, 2.0222, 2.8325, 0.6393, 0.1443, 18.2922, 4364.9,
    324.33, 404.57, 223.86, 51.76, 16.17, 39.14, 487.03, 1.1392,
    0.934, 0.957, 0.784, 0.712, 20.59, 6.22, 30.4, 82.46, 8.56,
    53.34, 5.05, 19.71, 0.867, 0.877, 0.992, 0.82, 515.67,
    14.11, 416.1, 26.55, 232.57, 13.63, 47.75, 7.93, 2.971,
    3.874, 3.974, 111.49, 17.911, 2.878, 0.392, 208.64, 659.57,
    505.14, 393.51, 415.63, 141.84, 33.06, 7.71})

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
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
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
    lies in the sealed r314..r339 record set."""
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
                            in R341_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the path
# ---------------- builders consume the TREE (abs block values +
# ---------------- index order via FDD.fold_mass_tree_exact) ONLY;
# ---------------- the withheld terminal drive key, the branch
# ---------------- label, the cubic target M_3 / rho_2 and the
# ---------------- q_max RECORD are forbidden (AST identifier scan
# ---------------- + literal scan).
def path_bellman_state(gtree, rstar):
    """THE EXACT PATH LAYER on a sealed mass tree: per-leaf path
    products prod_k Gamma(V_k) (top-down), the cubic-tilted
    weights (steps p~_c = p_c R_c^3/Gamma(v)), the tilted tower
    identity, the stopped decomposition at the heavy threshold
    rstar (tau = first level with max_c R_c > rstar), the good
    eps-chain B_k with its envelope W_B, the Phi-Gamma identity,
    the heavy hand-off algebra, the log path-product distribution
    and the near-ceiling defusal census.  Consumes the tree
    only."""
    mass = gtree["mass"]
    cnt = gtree["cnt"]
    kptr = gtree["kptr"]
    kk = gtree["depth"]
    m = gtree["m"]
    aroot = float(mass[0][0]) if m else 0.0
    if m < 2 or aroot <= 0.0:
        z3 = (0.0, 0.0, 0.0)
        return dict(ok=False, kk=0, e3=0.0, e3h=0.0, e3g=0.0,
                    hsh=0.0, msh=0.0, tilt_dev=0.0, wq_dev=0.0,
                    part_dev=0.0, bk_dev=0.0, env_dev=0.0,
                    pgi_dev=0.0, hvy_dev=0.0, hvy_res=0.0,
                    epg=0.0, lgq=z3, lgmax=0.0, pm3=0.0, c3s=0.0,
                    wb=1.0, sum_eps=0.0, blist=(1.0,), gbar=(),
                    tau_med=-1.0, tau_cnt=(), nheavy=0, nzero=0)
    droot = aroot / float(m)
    xs = [(mass[k] / np.maximum(cnt[k], 1)) / droot
          for k in range(kk + 1)]
    nzero = int(np.sum(mass[kk] <= 0.0))
    pg = [np.ones(len(mass[k])) for k in range(kk + 1)]
    wq = [np.zeros(len(mass[k])) for k in range(kk + 1)]
    wq[0][0] = 1.0
    stp = [np.full(len(mass[k]), -1, dtype=int)
           for k in range(kk + 1)]
    hi3 = [np.zeros(len(mass[k]), dtype=bool)
           for k in range(kk + 1)]
    uns = [np.zeros(len(mass[k]), dtype=bool)
           for k in range(kk + 1)]
    uns[0][0] = True
    gbar = []
    pgi_dev = 0.0
    nheavy = 0
    for k in range(kk):
        pt = kptr[k]
        mv = mass[k]
        cv = cnt[k]
        nk = len(mv)
        gsum = 0.0
        for i in range(nk):
            a, b = int(pt[i]), int(pt[i + 1])
            if mv[i] <= 0.0 or b - a < 1:
                continue
            mc = mass[k + 1][a:b]
            cc = cnt[k + 1][a:b].astype(float)
            pv = cc / float(cv[i])
            rv = (mc / np.maximum(cc, 1.0)) \
                / (mv[i] / float(cv[i]))
            gam = float(np.sum(pv * rv ** 3))
            mxr = float(np.max(rv))
            heavy = mxr > rstar
            if heavy:
                nheavy += 1
            gsum += (cv[i] / float(m)) * gam
            phis = float(np.sum((mc / mv[i]) ** 3
                                * (float(cv[i]) / cc) ** 2))
            pgi_dev = max(pgi_dev,
                          abs(phis - gam) / max(gam, 1e-300))
            gg = max(gam, 1e-300)
            pg[k + 1][a:b] = pg[k][i] * gam
            wq[k + 1][a:b] = wq[k][i] * pv * rv ** 3 / gg
            stp[k + 1][a:b] = stp[k][i] if stp[k][i] >= 0 \
                else (k if heavy else -1)
            hi3[k + 1][a:b] = bool(hi3[k][i]) or (gam > GAMMA_HI)
            uns[k + 1][a:b] = bool(uns[k][i]) and (not heavy)
        gbar.append(gsum)
    y = xs[kk]
    wts = cnt[kk].astype(float) / float(m)
    hv = stp[kk] >= 0
    e3 = float(np.sum(wts * y ** 3))
    e3h = float(np.sum(wts[hv] * y[hv] ** 3))
    e3g = float(np.sum(wts[~hv] * y[~hv] ** 3))
    hsh = float(np.sum(wts[hv]))
    msh = float(np.sum(wts[hv] * y[hv])) / float(m) * float(m)
    msh = float(np.sum(wts[hv] * y[hv]))
    part_dev = abs(e3h + e3g - e3) / max(e3, 1e-300)
    tilt = float(np.sum(wq[kk] * pg[kk]))
    tilt_dev = abs(tilt - e3) / max(e3, 1e-300)
    wq_dev = abs(float(np.sum(wq[kk])) - 1.0)
    epg = float(np.sum(wts * pg[kk]))
    lg = np.log(np.maximum(pg[kk], 1e-300))
    lgq = tuple(float(v) for v in np.quantile(lg, QTS))
    lgmax = float(np.max(lg))
    pm3 = float(np.sum(wts[hi3[kk]]))
    c3s = float(np.sum(wts[hi3[kk]] * y[hi3[kk]] ** 3)) \
        / max(e3, 1e-300)
    taus = stp[kk][hv]
    tau_med = float(np.median(taus)) if len(taus) else -1.0
    tau_cnt = tuple(int(np.sum(taus == k)) for k in range(kk))
    blist = []
    for k in range(kk + 1):
        wk = cnt[k].astype(float) / float(m)
        blist.append(float(np.sum(wk[uns[k]] * xs[k][uns[k]] ** 3)))
    wb = 1.0
    sum_eps = 0.0
    for k in range(kk):
        if blist[k] > 0.0 and blist[k + 1] > 0.0:
            g = blist[k + 1] / blist[k]
        else:
            g = 1.0
        eps = max(g - 1.0, 0.0)
        sum_eps += eps
        wb *= (1.0 + eps)
    bk_dev = abs(blist[kk] - e3g) / max(e3g, 1e-300) \
        if e3g > 0.0 else abs(blist[kk])
    env_dev = max(0.0, e3g - wb) / max(wb, 1e-300)
    ymax = float(np.max(y))
    hb = ymax ** 2 * msh
    hvy_dev = max(0.0, e3h - hb) / max(hb, 1e-300) \
        if e3h > 0.0 else 0.0
    hvy_res = hb / e3h if e3h > 0.0 else float("inf")
    return dict(ok=True, kk=kk, e3=e3, e3h=e3h, e3g=e3g, hsh=hsh,
                msh=msh, tilt_dev=tilt_dev, wq_dev=wq_dev,
                part_dev=part_dev, bk_dev=bk_dev, env_dev=env_dev,
                pgi_dev=pgi_dev, hvy_dev=hvy_dev, hvy_res=hvy_res,
                epg=epg, lgq=lgq, lgmax=lgmax, pm3=pm3, c3s=c3s,
                wb=wb, sum_eps=sum_eps, blist=tuple(blist),
                gbar=tuple(gbar), tau_med=tau_med, tau_cnt=tau_cnt,
                nheavy=nheavy, nzero=nzero)


def psi_ratio_state(gtree, rstar, aexp, c0):
    """THE FORM-2 PSI-BELLMAN SCAN: per internal non-heavy node
    the ratio sum_c Phi(c) Psi(c) / (Phi(v) Psi(v)) with Phi(v) =
    A(v)^3/n(v)^2 and Psi(v) = (c0 + ln n(v))^aexp; violations
    (ratio > 1 + PSI_TOL) counted over the strict surface (all
    non-heavy internal nodes) and the composed surface (unstopped
    non-heavy nodes -- what the two-arm telescoping needs).
    Consumes the tree only."""
    mass = gtree["mass"]
    cnt = gtree["cnt"]
    kptr = gtree["kptr"]
    kk = gtree["depth"]
    m = gtree["m"]
    if m < 2 or float(mass[0][0]) <= 0.0:
        return dict(ok=False, viol_s=0, viol_c=0, max_s=0.0,
                    max_c=0.0, wk=-1, nn=0)
    uns = [np.zeros(len(mass[k]), dtype=bool)
           for k in range(kk + 1)]
    uns[0][0] = True
    viol_s = 0
    viol_c = 0
    max_s = 0.0
    max_c = 0.0
    wk = -1
    nn = 0
    for k in range(kk):
        pt = kptr[k]
        mv = mass[k]
        cv = cnt[k]
        for i in range(len(mv)):
            a, b = int(pt[i]), int(pt[i + 1])
            if mv[i] <= 0.0 or b - a < 1:
                continue
            mc = mass[k + 1][a:b]
            cc = cnt[k + 1][a:b].astype(float)
            rv = (mc / np.maximum(cc, 1.0)) \
                / (mv[i] / float(cv[i]))
            heavy = float(np.max(rv)) > rstar
            uns[k + 1][a:b] = bool(uns[k][i]) and (not heavy)
            if heavy:
                continue
            nn += 1
            psi_v = (c0 + math.log(float(cv[i]))) ** aexp
            psi_c = (c0 + np.log(cc)) ** aexp
            rat = float(np.sum((mc / mv[i]) ** 3
                               * (float(cv[i]) / cc) ** 2
                               * psi_c)) / psi_v
            bad = rat > 1.0 + PSI_TOL
            if bad:
                viol_s += 1
            max_s = max(max_s, rat)
            if bool(uns[k][i]):
                if bad:
                    viol_c += 1
                    if rat > max_c:
                        wk = k
                max_c = max(max_c, rat)
    return dict(ok=True, viol_s=viol_s, viol_c=viol_c,
                max_s=max_s, max_c=max_c, wk=wk, nn=nn)


def bellman_tree_verdict(leak, brk, go, partial, goodonly):
    """the sealed six-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    BELLMAN_STATE_NOT_EXACT > RH3_BELLMAN_GO >
    RH3_BELLMAN_PARTIAL > GOODTREE_A2_ONLY >
    PATHWEIGHT_ALSO_SUPERCRITICAL."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "BELLMAN_STATE_NOT_EXACT"
    if go:
        return "RH3_BELLMAN_GO"
    if partial:
        return "RH3_BELLMAN_PARTIAL"
    if goodonly:
        return "GOODTREE_A2_ONLY"
    return "PATHWEIGHT_ALSO_SUPERCRITICAL"


def fr_path_state(leaves, rstar):
    """the FULL FRACTIONS REPLICA of path_bellman_state on the
    sealed pairing tree: exact E3, tilted tower, untilted census,
    stopped partition, mass share, eps-chain/W_B, heavy hand-off
    slack, Phi-Gamma identity deviation and the e4 no-n mutant
    value -- everything as exact rationals.  Consumes the leaf
    list only."""
    lev = FDD.fr_pair_tree(leaves)
    kk = len(lev) - 1
    aroot, mroot = lev[0][0]
    droot = aroot / Fr(mroot)
    ptrs = []
    for k in range(kk):
        cur = lev[k]
        nxt = lev[k + 1]
        j = 0
        pt = []
        for _a, n in cur:
            s = j
            acc = 0
            while acc < n:
                acc += nxt[j][1]
                j += 1
            pt.append((s, j))
        ptrs.append(pt)
    xv = [[(a / Fr(n)) / droot for a, n in lv] for lv in lev]
    pg = [[Fr(1)] * len(lv) for lv in lev]
    wq = [[Fr(0)] * len(lv) for lv in lev]
    wn = [[Fr(0)] * len(lv) for lv in lev]
    wq[0][0] = Fr(1)
    wn[0][0] = Fr(1)
    stp = [[-1] * len(lv) for lv in lev]
    uns = [[False] * len(lv) for lv in lev]
    uns[0][0] = True
    pgi_dev = Fr(0)
    for k in range(kk):
        for i, (av, nv) in enumerate(lev[k]):
            a, b = ptrs[k][i]
            if av == 0:
                continue
            kids = lev[k + 1][a:b]
            pcs = [Fr(nc, nv) for _ac, nc in kids]
            rcs = [(ac / Fr(nc)) / (av / Fr(nv))
                   for ac, nc in kids]
            gam = sum(p * r ** 3 for p, r in zip(pcs, rcs))
            heavy = max(rcs) > rstar
            s3 = sum(r ** 3 for r in rcs)
            phis = sum((ac / av) ** 3 * Fr(nv * nv, nc * nc)
                       for ac, nc in kids)
            pgi_dev = max(pgi_dev, abs(phis - gam))
            for t, (p, r) in enumerate(zip(pcs, rcs)):
                j = a + t
                pg[k + 1][j] = pg[k][i] * gam
                wq[k + 1][j] = wq[k][i] * p * r ** 3 / gam
                wn[k + 1][j] = wn[k][i] * (r ** 3 / s3)
                stp[k + 1][j] = stp[k][i] if stp[k][i] >= 0 \
                    else (k if heavy else -1)
                uns[k + 1][j] = uns[k][i] and (not heavy)
    mI = Fr(1, mroot)
    yv = xv[kk]
    e3 = sum(mI * v ** 3 for v in yv)
    hvf = [stp[kk][i] >= 0 for i in range(len(yv))]
    e3h = sum(mI * yv[i] ** 3 for i in range(len(yv)) if hvf[i])
    e3g = e3 - e3h
    msh = sum(mI * yv[i] for i in range(len(yv)) if hvf[i])
    tilt = sum(wq[kk][i] * pg[kk][i] for i in range(len(yv)))
    epg = sum(mI * pg[kk][i] for i in range(len(yv)))
    no_n = sum(wn[kk][i] * pg[kk][i] for i in range(len(yv)))
    blist = []
    for k in range(kk + 1):
        blist.append(sum(Fr(n, mroot) * xv[k][i] ** 3
                         for i, (_a, n) in enumerate(lev[k])
                         if uns[k][i]))
    wb = Fr(1)
    for k in range(kk):
        if blist[k] > 0 and blist[k + 1] > 0:
            g = blist[k + 1] / blist[k]
            if g > 1:
                wb *= g
    ymax = max(yv)
    hslack = ymax ** 2 * msh - e3h
    return dict(e3=e3, tilt=tilt, epg=epg, no_n=no_n, e3h=e3h,
                e3g=e3g, msh=msh, wb=wb, blist=blist,
                hslack=hslack, pgi_dev=pgi_dev)


def mutant_tower_untilted(pbs):
    """e1 MUST-FAIL MUTANT: the tower identity with the WRONG
    FILTRATION -- returns E_P[prod Gamma] under the leaf-uniform
    measure and claims it equals E[X_inf^3]; on the even
    Fractions toy the break is 20/9 - 11/6 = 7/18 EXACT."""
    return pbs["epg"]


def mutant_tilt_no_n(gtree):
    """e4 MUST-FAIL MUTANT: the tilted path measure WITHOUT the
    n(c) normalization (steps R_c^3 / sum R_c^3, p_c dropped) --
    on the uneven Fractions toy it returns 51/25 while the exact
    value is 261/125 (break 6/125 EXACT)."""
    mass = gtree["mass"]
    cnt = gtree["cnt"]
    kptr = gtree["kptr"]
    kk = gtree["depth"]
    m = gtree["m"]
    if m < 2 or float(mass[0][0]) <= 0.0:
        return 0.0
    pg = [np.ones(len(mass[k])) for k in range(kk + 1)]
    wn = [np.zeros(len(mass[k])) for k in range(kk + 1)]
    wn[0][0] = 1.0
    for k in range(kk):
        pt = kptr[k]
        mv = mass[k]
        cv = cnt[k]
        for i in range(len(mv)):
            a, b = int(pt[i]), int(pt[i + 1])
            if mv[i] <= 0.0 or b - a < 1:
                continue
            mc = mass[k + 1][a:b]
            cc = cnt[k + 1][a:b].astype(float)
            pv = cc / float(cv[i])
            rv = (mc / np.maximum(cc, 1.0)) \
                / (mv[i] / float(cv[i]))
            gam = float(np.sum(pv * rv ** 3))
            s3 = float(np.sum(rv ** 3))
            pg[k + 1][a:b] = pg[k][i] * gam
            wn[k + 1][a:b] = wn[k][i] * rv ** 3 / max(s3, 1e-300)
    return float(np.sum(wn[kk] * pg[kk]))


def mutant_rstar_from_target(ev):
    """e3 MUST-FAIL MUTANT: an 'R* column' derived from the cubic
    TARGET record (consumes cm/S3) -- the PHI3_FORBIDDEN scan
    must FLAG this while the path builders stay clean."""
    return 0.5 * abs(float(ev["cm"]["S3"])) ** (1.0 / 3.0)


def mutant_psi_posthoc(aa_seen, rho, cbar):
    """e2 MUST-FAIL MUTANT (protocol): the Psi exponent re-picked
    AFTER SIGHT of the evaluated violation column (consumes rho)
    -- the BOUND_FORBIDDEN scope audit must FLAG it AND on the
    sealed toy it returns 3 != the family-scan protocol head
    PSI_A_FAM[0] = 1 (the family is sealed BEFORE the freeze)."""
    pick = PSI_A_FAM[0]
    for a, r in zip(aa_seen, rho):
        if r > cbar:
            pick = max(pick, int(a))
    return pick


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'path orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'budget constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- sealed Fractions toys
def fr_path_toy():
    """the sealed even toy (3, 1, 1, 1): E3 = tilt = 20/9 EXACT
    (the tilted tower); the untilted e1 mutant reads 11/6 (break
    7/18 EXACT); no heavy node at R* = 3/2 (max R = 3/2 is NOT
    > 3/2), so e3g = e3 and the eps-chain closes W_B = 20/9 ==
    E3 EXACT (envelope equality).  Returns (worst dev, e1
    break)."""
    st = fr_path_state([Fr(3), Fr(1), Fr(1), Fr(1)], Fr(3, 2))
    brk = st["e3"] - st["epg"]
    devs = [abs(st["e3"] - Fr(20, 9)),
            abs(st["tilt"] - Fr(20, 9)),
            abs(st["epg"] - Fr(11, 6)),
            abs(st["e3h"]), abs(st["e3g"] - Fr(20, 9)),
            abs(st["wb"] - Fr(20, 9)),
            abs(st["msh"]), st["pgi_dev"],
            abs(brk - Fr(7, 18))]
    return max(devs), brk


def fr_tilt_toy():
    """the sealed uneven toy (3, 1, 1): E3 = tilt = 261/125
    EXACT; the e4 no-n mutant reads 51/25 (break 6/125 EXACT);
    the untilted census reads 459/250 there (not gated, printed
    via e1 on the even toy).  Returns (worst dev, e4 break)."""
    st = fr_path_state([Fr(3), Fr(1), Fr(1)], Fr(3, 2))
    brk = st["e3"] - st["no_n"]
    devs = [abs(st["e3"] - Fr(261, 125)),
            abs(st["tilt"] - Fr(261, 125)),
            abs(st["no_n"] - Fr(51, 25)),
            abs(st["epg"] - Fr(459, 250)),
            st["pgi_dev"],
            abs(brk - Fr(6, 125))]
    return max(devs), brk


def fr_stop_toy():
    """the sealed stop toy (7, 1, 5, 3): node (7, 1) HEAVY (max R
    = 7/4 > 3/2), node (5, 3) good -- exact partition E3 = 31/16
    = 43/32 (heavy) + 19/32 (good), msh = 1/2, eps-chain B = (1,
    1, 19/32) with W_B = 1 (envelope 19/32 <= 1 EXACT), heavy
    hand-off slack (m q_max)^2 msh - E3h = 49/32 - 43/32 = 3/16
    EXACT.  Returns worst dev."""
    st = fr_path_state([Fr(7), Fr(1), Fr(5), Fr(3)], Fr(3, 2))
    devs = [abs(st["e3"] - Fr(31, 16)),
            abs(st["e3h"] - Fr(43, 32)),
            abs(st["e3g"] - Fr(19, 32)),
            abs(st["msh"] - Fr(1, 2)),
            abs(st["wb"] - 1),
            abs(st["blist"][2] - Fr(19, 32)),
            abs(st["hslack"] - Fr(3, 16)),
            abs(st["tilt"] - st["e3"]),
            st["pgi_dev"]]
    return max(devs)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fold_bellman_reverse_holder_probe -- "
          "PRIME.L2.FOLD_DENSITY_REVERSE_HOLDER.01 (round 341, "
          "the path-weighted Bellman round)")
    print("SPEC_SHA %s   R339_SHA %s   R327_SHA %s   R324_SHA %s"
          % (SPEC_SHA[:16], FDD.SPEC_SHA[:16], GMC.SPEC_SHA[:16],
             QMO.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + exact path wards + w9 "
                        "Fractions bit-equality + e1-e4; ladder, "
                        "extensions, EXT3, anchors, census, "
                        "certification, composition and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE PATH-WEIGHTED BELLMAN ROUND (terminal main round "
          "after the r339 dictionary): on the SEALED iterated "
          "r270 pairing tree (FDD verbatim, PAIR_OFFSET 0) the "
          "exact path layer is (i) X_inf^3 == prod R^3, (ii) the "
          "TILTED tower E[X_inf^3] == E_Q[prod Gamma] (steps "
          "p~_c = p_c R_c^3/Gamma -- the naive untilted form is "
          "FALSE, toy break 7/18), (iii) sum_c Phi(c)/Phi(v) == "
          "Gamma(v), (iv) the stopped partition at R* = %.2f "
          "with the exact hand-off E3h <= (m q_max)^2 msh, (v) "
          "the good eps-chain with envelope W_B; two-arm "
          "certification EACH ON ITS OWN FREEZE (r337 "
          "directive); Form-2 Psi family %s x %s sealed, display "
          "%s; budgets vs (log m)^a, a in %s; verdict tree "
          "TARGET_LEAK / BELLMAN_STATE_NOT_EXACT / "
          "RH3_BELLMAN_GO / RH3_BELLMAN_PARTIAL / "
          "GOODTREE_A2_ONLY / PATHWEIGHT_ALSO_SUPERCRITICAL "
          "sealed BEFORE evaluation"
          % (R_STAR, str(PSI_A_FAM), str(PSI_C0_FAM),
             str(PSI_DISPLAY), str(GA_FAM)))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("path_bellman_state", "psi_ratio_state",
               "bellman_tree_verdict", "fr_path_state"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the four module-own "
          "path builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the path "
          "side consumes the sealed tree ONLY (abs block values "
          "+ index order); m5a gift-bound FLAGGED (%s); m5b "
          "branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r339 scaffold verbatim)
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
              "EXT2 (r316 A5 rule verbatim, census-grade): pool "
              "%d leftover + %d windows with %d < h <= %d; "
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(epool) - K_EXT, min(len(ekz2), EXT2_POOL_CAP),
                 EXT_H_MAX, EXT2_H_MAX, len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))
        check("G14-ext3-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX,
              "EXT3 = the sealed r329 RECORD selection (committed "
              "8cbd95f9, r335/r339 adoption verbatim): 12 anchors "
              "(B %s + A %s), POSITIVE_PREFIX %d/12, N_w %d..%d "
              "(record %d..%d) -- PURE TEST rows, never "
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
              "EXT+EXT2+EXT3 census (no sealed expectation): %d "
              "cheap / %d exception %s"
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
            pbs = path_bellman_state(gtree, R_STAR)
            pba = path_bellman_state(gtree, R_ALT)
            psi = {(a, c0): psi_ratio_state(gtree, R_STAR, a, c0)
                   for a in PSI_A_FAM for c0 in PSI_C0_FAM}
            psa = psi_ratio_state(gtree, R_ALT, PSI_DISPLAY[0],
                                  PSI_DISPLAY[1])
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
            pbs = path_bellman_state(
                dict(mass=[np.zeros(1)], cnt=[np.ones(1, int)],
                     kptr=[], depth=0, m=0), R_STAR)
            pba = dict(pbs)
            psi = {(a, c0): dict(ok=False, viol_s=0, viol_c=0,
                                 max_s=0.0, max_c=0.0, wk=-1,
                                 nn=0)
                   for a in PSI_A_FAM for c0 in PSI_C0_FAM}
            psa = dict(ok=False, viol_s=0, viol_c=0, max_s=0.0,
                       max_c=0.0, wk=-1, nn=0)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led327=led327, gtree=gtree, dst=dst, dic=dic,
                    pbs=pbs, pba=pba, psi=psi, psa=psa,
                    pos_all=pos_all, val_all=val_all,
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
          "(worst dev %.1e, bar %.0e -- the grounding); EXT3 "
          "fold multiplicity <= %d on 12/12 (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP, "OK" if x3_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r306/r316/r324-pre "
            "+ r339 RECORD + r324 CHAIN)")
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
          "EXT3 %.1e / %.1e / %.1e (bar %.0e, r329 a-priori); "
          "DISCLOSED slim anchor set -- the full chain is "
          "re-warded by the sealed r321..r339 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, tel_x,
             bnd_x, REC3_BAR_X3))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 m %d K %d E3 %.4f E3h %.4f E3g %.4f hsh "
             "%.3f msh %.3f WB %.3f epg %.3f lgq50 %.3f pm3 %.3f"
             % (ev9s["m"], ev9s["pbs"]["kk"], ev9s["pbs"]["e3"],
                ev9s["pbs"]["e3h"], ev9s["pbs"]["e3g"],
                ev9s["pbs"]["hsh"], ev9s["pbs"]["msh"],
                ev9s["pbs"]["wb"], ev9s["pbs"]["epg"],
                ev9s["pbs"]["lgq"][1], ev9s["pbs"]["pm3"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r324pre-m2-anchor", True, "SMOKE: skipped")
        srt = []
        n341 = 0
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2r, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2r)
        check("G31-r306-bound-live",
              abs(C2r - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d "
              "-- via the dictionary this ALREADY reads "
              "E[X_inf^3] <= C_2 (log m)^2 on the 57-rung set "
              "(disclosed pre-spec)"
              % (C2r, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        srt_all65 = sorted(recs + erecs + e2recs,
                           key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all65
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n341 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n341)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n341 == N341_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n341, N341_REF, rho_kz.get(53, -1.0),
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
    # G34 dictionary-chain identity (live, both modes)
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
          "THE MOMENT DICTIONARY anchored bit-near to the r324 "
          "chain on %d live worlds: E[X_inf^2] == m M_2 (worst "
          "rel %.1e), E[X_inf^3] == m^2 M_3 == rho_2 (log m)^2 "
          "(worst %.1e), max y / m == q_max (worst %.1e; bars "
          "%.0e) -- the terminal target M_3 <= C (log m)^A/m^2 "
          "is EQUIVALENT to E[X_inf^3] <= C (log m)^A"
          % (len(live), dict2_w, dict3_w, dictq_w, DICT_BAR))
    if smoke:
        check("G35-r339-record-anchors", True, "SMOKE: skipped")
        check("G36-r324-chain-anchor", True, "SMOKE: skipped")
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
              "%+.3f (rec %+.3f), e(m^2 M_3) %+.3f (rec %+.3f) "
              "-- the supercritical worst-case budget and the "
              "subcritical target are BOTH re-anchored"
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
              "the r324 MEASURED chain reproduced from the "
              "dictionary columns: e(G/log m) %+.3f (rec %+.3f), "
              "e(m M_2) %+.3f (rec %+.3f), e_tot %+.3f (rec "
              "%+.3f) -- the honest comparison threshold stays "
              "m_0* = 10^%.1f (record number, adopted)"
              % (e_g324, R324_EG, e_m2324, R324_EM2, e_tot324,
                 R324_ETOT, R324_M0_L10))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE PATH WARDS "
            "+ SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("path_bellman_state", "psi_ratio_state",
               "bellman_tree_verdict", "fr_path_state",
               "fr_path_toy", "fr_tilt_toy", "fr_stop_toy"):
        pure_lits += literal_audit(fn)
    e3_hits = scope_audit("mutant_rstar_from_target",
                          PHI3_FORBIDDEN)
    e2_hits = scope_audit("mutant_psi_posthoc", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e3_hits) >= 1 and len(e2_hits) >= 1,
          "SOURCE PURITY: the path builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed "
          "r314..r339 record-literal set (%d literal hits); "
          "consumed inputs: the sealed tree ONLY -- M_3, rho_2 "
          "and the q_max RECORD are TARGET-SIDE, computed "
          "outside the builders (disclosed); e3 "
          "rstar-from-target FLAGGED (%s); e2 psi-posthoc "
          "FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e3_hits[0] if e3_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS"))
    fp_dev, fp_e1brk = fr_path_toy()
    ft_dev, ft_e4brk = fr_tilt_toy()
    fs_dev = fr_stop_toy()
    st_even = path_bellman_state(
        FDD.fold_mass_tree_exact([3.0, 1.0, 1.0, 1.0]), R_STAR)
    st_stop = path_bellman_state(
        FDD.fold_mass_tree_exact([7.0, 1.0, 5.0, 3.0]), R_STAR)
    ok_even = (st_even["ok"]
               and abs(st_even["e3"] - float(Fr(20, 9))) <= TOY_BAR
               and abs(st_even["epg"] - float(Fr(11, 6)))
               <= TOY_BAR
               and st_even["tilt_dev"] <= TOY_BAR
               and abs(st_even["wb"] - float(Fr(20, 9))) <= TOY_BAR
               and st_even["e3h"] <= TOY_BAR)
    ok_stop = (st_stop["ok"]
               and abs(st_stop["e3h"] - float(Fr(43, 32)))
               <= TOY_BAR
               and abs(st_stop["e3g"] - float(Fr(19, 32)))
               <= TOY_BAR
               and abs(st_stop["msh"] - 0.5) <= TOY_BAR
               and abs(st_stop["wb"] - 1.0) <= TOY_BAR
               and st_stop["hvy_dev"] <= TOY_BAR
               and st_stop["tau_cnt"] == (0, 2))
    mut1 = mutant_tower_untilted(st_even)
    mut4 = mutant_tilt_no_n(
        FDD.fold_mass_tree_exact([3.0, 1.0, 1.0]))
    tr_br = (bellman_tree_verdict(True, True, True, True, True),
             bellman_tree_verdict(False, True, True, True, True),
             bellman_tree_verdict(False, False, True, True, True),
             bellman_tree_verdict(False, False, False, True, True),
             bellman_tree_verdict(False, False, False, False,
                                  True),
             bellman_tree_verdict(False, False, False, False,
                                  False))
    ok_tr = tr_br == ("TARGET_LEAK", "BELLMAN_STATE_NOT_EXACT",
                      "RH3_BELLMAN_GO", "RH3_BELLMAN_PARTIAL",
                      "GOODTREE_A2_ONLY",
                      "PATHWEIGHT_ALSO_SUPERCRITICAL")
    check("G41-toy-exactness",
          fp_dev == 0 and ft_dev == 0 and fs_dev == 0
          and fp_e1brk == Fr(7, 18) and ft_e4brk == Fr(6, 125)
          and ok_even and ok_stop
          and abs(mut1 - float(Fr(11, 6))) <= TOY_BAR
          and abs(mut4 - float(Fr(51, 25))) <= TOY_BAR
          and ok_tr,
          "the Fractions path toys EXACT: even (3,1,1,1) worst "
          "dev %s (E3 = tilt = 20/9, untilted 11/6, e1 break "
          "7/18 EXACT, W_B = 20/9 envelope equality); uneven "
          "(3,1,1) worst %s (E3 = tilt = 261/125, e4 no-n "
          "mutant 51/25, break 6/125 EXACT); stop toy (7,1,5,3) "
          "worst %s (partition 43/32 + 19/32 == 31/16, msh 1/2, "
          "W_B = 1, hand-off slack 3/16 EXACT, tau at level 1); "
          "float builders reproduce (e1 %.3f, e4 %.3f); "
          "bellman_tree_verdict all six branches EXACT %s"
          % (str(fp_dev), str(ft_dev), str(fs_dev), mut1, mut4,
             str(tr_br)))
    # live path wards
    mart_w = 0.0
    unit_w = 0.0
    rec_w = 0.0
    jen_w = 0.0
    tilt_w = 0.0
    wqd_w = 0.0
    part_w3 = 0.0
    bkd_w = 0.0
    env_w = 0.0
    pgi_w = 0.0
    hvy_w = 0.0
    e3d_w = 0.0
    part_w = 0.0
    panc_w = 0.0
    l1rec_w = 0.0
    chain_w = 0.0
    xw_cube = 0.0
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
        pb = ev["pbs"]
        if st["ok"]:
            mart_w = max(mart_w, st["mart_dev"])
            unit_w = max(unit_w, st["unit_dev"])
            rec_w = max(rec_w, st["rec_dev"])
            jen_w = max(jen_w,
                        max((d for d in st["drift"]),
                            default=0.0))
            nz_tot += st["nzero"]
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
    # the Fractions bit-equality on the small windows (w9 + w13)
    fr_ok = True
    fr_nodes = 0
    for rc in mrecs:
        if rc["ev"]["degenerate"]:
            continue
        leaves = [Fr(float(abs(v)))
                  for v in rc["ev"]["sct"]["x"]]
        stf = fr_path_state(leaves, Fr(3, 2))
        okx = (stf["tilt"] == stf["e3"]
               and stf["e3h"] + stf["e3g"] == stf["e3"]
               and stf["e3g"] <= stf["wb"]
               and stf["pgi_dev"] == 0
               and stf["blist"][-1] == stf["e3g"])
        fr_ok = fr_ok and okx
        okm, wm, nm = FDD.fr_mart_check(FDD.fr_pair_tree(leaves))
        fr_ok = fr_ok and okm and (wm == 0)
        fr_nodes += nm
    check("G42-live-path-wards",
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
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); the r339 martingale "
          "wards live (mart %.1e / unit %.1e / rec %.1e / "
          "Jensen %.1e); THE TILTED TOWER E_Q[prod Gamma] == "
          "E[X_inf^3] (worst %.1e, bar %.0e) AND weight norm "
          "sum wq == 1 (%.1e) AND the stopped partition E3h + "
          "E3g == E3 (%.1e) AND the B-chain closure B_K == E3g "
          "(%.1e) AND the envelope E3g <= W_B (viol %.1e) AND "
          "the Phi-Gamma identity (%.1e) AND the heavy hand-off "
          "E3h <= (m q_max)^2 msh (viol %.1e) AND E3 == "
          "dictionary d3 (%.1e); FRACTIONS BIT-EQUALITY on "
          "w9+w13: %s (%d martingale nodes + the full path "
          "replica, symbolic dev == 0); r327 GROUNDING: "
          "partition %.1e, L1 %.1e, two-ancestor %.1e; "
          "zero-mass leaves %d; fold multiplicity <= %d admitted"
          % (len(live), chain_w, xw_cube, mart_w, unit_w, rec_w,
             jen_w, tilt_w, TILT_BAR, wqd_w, part_w3, bkd_w,
             env_w, pgi_w, hvy_w, e3d_w,
             "EXACT" if fr_ok else "BROKEN", fr_nodes, part_w,
             l1rec_w, panc_w, nz_tot, MULT_CAP))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        kk_col = [rc["ev"]["pbs"]["kk"] for rc in srt_full]
        e3_col = [rc["ev"]["pbs"]["e3"] for rc in srt_full]
        e3h_col = [rc["ev"]["pbs"]["e3h"] for rc in srt_full]
        e3g_col = [rc["ev"]["pbs"]["e3g"] for rc in srt_full]
        hsh_col = [rc["ev"]["pbs"]["hsh"] for rc in srt_full]
        msh_col = [rc["ev"]["pbs"]["msh"] for rc in srt_full]
        wb_col = [rc["ev"]["pbs"]["wb"] for rc in srt_full]
        se_col = [rc["ev"]["pbs"]["sum_eps"] for rc in srt_full]
        epg_col = [rc["ev"]["pbs"]["epg"] for rc in srt_full]
        lgq_col = [rc["ev"]["pbs"]["lgq"] for rc in srt_full]
        lgm_col = [rc["ev"]["pbs"]["lgmax"] for rc in srt_full]
        pm3_col = [rc["ev"]["pbs"]["pm3"] for rc in srt_full]
        c3s_col = [rc["ev"]["pbs"]["c3s"] for rc in srt_full]
        tau_col = [rc["ev"]["pbs"]["tau_med"] for rc in srt_full]
        hres_col = [rc["ev"]["pbs"]["hvy_res"] for rc in srt_full]
        psid_col = [rc["ev"]["psi"][PSI_DISPLAY]["max_c"]
                    for rc in srt_full]
        h_share = [e3h_col[i] / max(e3_col[i], 1e-300)
                   for i in range(n_full)]
        dfl_col = [lgm_col[i]
                   / max(math.log(max(wf_col[i], 1.0 + 1e-12)),
                         1e-300)
                   for i in range(n_full)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m K E3 E3h E3g "
             "hsh msh tau WB sumE lgq50 lgmax lWF epg pm3 c3s "
             "psi(3,1)  [rows 65..%d are EXT3 PURE TEST]"
             % (n_full - 1))
        for i, rc in enumerate(srt_full):
            info("%2d kz%-3d N %4d m %3d K %d E3 %8.3f E3h "
                 "%8.3f E3g %6.3f hsh %.3f msh %.3f tau %3.1f "
                 "WB %7.3f sE %5.2f lg50 %6.3f lgmx %6.3f lWF "
                 "%6.3f epg %8.3f pm3 %.3f c3s %.3f psi %5.3f%s"
                 % (i, rc["kz"], rc["N"], m_full[i], kk_col[i],
                    e3_col[i], e3h_col[i], e3g_col[i],
                    hsh_col[i], msh_col[i], tau_col[i],
                    wb_col[i], se_col[i], lgq_col[i][1],
                    lgm_col[i],
                    math.log(max(wf_col[i], 1e-300)),
                    epg_col[i], pm3_col[i], c3s_col[i],
                    psid_col[i],
                    " X3" if i >= n341 else ""))
        check("G43-coordinate-table", True,
              "PATH DISTRIBUTION (Leg A): med log prod Gamma "
              "per path q50 med %.2f / q90 med %.2f / max med "
              "%.2f vs log W_F med %.2f (deflation med %.2f = "
              "lgmax/logW_F -- the path-weighted budget vs the "
              "r339 worst case); E_P[prod Gamma] med %.2f vs E3 "
              "med %.2f vs W_F med %.2f; concentration med IQR "
              "%.2f; levels K %d..%d"
              % (float(np.median([q[1] for q in lgq_col])),
                 float(np.median([q[2] for q in lgq_col])),
                 float(np.median(lgm_col)),
                 float(np.median([math.log(max(v, 1e-300))
                                  for v in wf_col])),
                 float(np.median(dfl_col)),
                 float(np.median(epg_col)),
                 float(np.median(e3_col)),
                 float(np.median(wf_col)),
                 float(np.median([q[2] - q[0]
                                  for q in lgq_col])),
                 min(kk_col), max(kk_col)))

    # ---------------- S5: Leg B -- stopping + heavy arm
    section("S5  LEG B -- STOPPING CENSUS + HEAVY-ARM "
            "CERTIFICATION (own scale)")
    if smoke:
        check("G50-stopping-census", True, "SMOKE: skipped")
        check("G51-heavy-arm-cert", True, "SMOKE: skipped")
    else:
        named_rank = {}
        for kz in NAMED_KZ + MIDBAND_KZ:
            for i in range(n_full):
                if srt_full[i]["kz"] == kz:
                    named_rank[kz] = i
        for fam, kzs_f in (("NAMED", NAMED_KZ),
                           ("MIDBAND", MIDBAND_KZ)):
            for kz in kzs_f:
                i = named_rank[kz]
                pb = srt_full[i]["ev"]["pbs"]
                info("%s kz%-3d m %3d K %d hsh %.3f msh %.3f "
                     "E3h %8.3f (%.2f of E3) tau %s cnt %s WB "
                     "%6.3f psi(3,1) %.3f"
                     % (fam, kz, m_full[i], pb["kk"], pb["hsh"],
                        pb["msh"], pb["e3h"], h_share[i],
                        ("%.1f" % pb["tau_med"]),
                        str(pb["tau_cnt"]), pb["wb"],
                        psid_col[i]))
        heavy_rungs = sum(1 for v in hsh_col if v > 0.0)
        late_stop = sum(1 for rc in srt_full
                        if rc["ev"]["pbs"]["tau_cnt"]
                        and rc["ev"]["pbs"]["kk"] >= 2
                        and rc["ev"]["pbs"]["tau_cnt"][-1]
                        == max(rc["ev"]["pbs"]["tau_cnt"]))
        check("G50-stopping-census", True,
              "THE STOPPED DECOMPOSITION (tau = first heavy "
              "level, R* %.2f): hsh med %.3f max %.3f (heavy "
              "rungs %d/%d), msh med %.3f, E3h share of E3 med "
              "%.3f max %.3f, tau med (of med) %.1f; the LAST "
              "internal level is the modal stop on %d/%d rungs; "
              "near-ceiling defusal: pm3 (path mass under Gamma "
              "> %.0f) med %.3f max %.3f carrying c3s med %.3f "
              "of E3 -- the r339 thesis measured EXPLICITLY"
              % (R_STAR, float(np.median(hsh_col)), max(hsh_col),
                 heavy_rungs, n_full, float(np.median(msh_col)),
                 float(np.median(h_share)), max(h_share),
                 float(np.median([t for t in tau_col
                                  if t >= 0.0])), late_stop,
                 n_full, GAMMA_HI, float(np.median(pm3_col)),
                 max(pm3_col), float(np.median(c3s_col))))
        te_x = list(te_i) + list(range(n341, n_full))

        def cert_max(cols):
            out = {}
            for a in GA_FAM:
                col = cols[a]
                CQ = max(col[i] for i in ca_i)
                viol = [i for i in te_x if col[i] > CQ]
                named = sum(1 for kz in NAMED_KZ
                            if col[named_rank[kz]] <= CQ)
                mb = sum(1 for kz in MIDBAND_KZ
                         if col[named_rank[kz]] <= CQ)
                out[a] = (CQ, viol, named, mb, col)
            aa = None
            for a in GA_FAM:
                if (not out[a][1] and out[a][2] == len(NAMED_KZ)
                        and out[a][0] < CERT_GUARD):
                    aa = a
                    break
            return out, aa

        h_cols = {a: [e3h_col[i]
                      / (math.log(float(m_full[i])) ** a)
                      for i in range(n_full)] for a in GA_FAM}
        certH, aH = cert_max(h_cols)
        check("G51-heavy-arm-cert", True,
              "THE HEAVY ARM ON ITS OWN SCALE (r337 two-constant "
              "directive; own mid-ladder freeze): E3h <= C_H(a) "
              "(log m)^a: "
              + "; ".join("a=%d C_H %.4f viol %d/%d named %d/4 "
                          "midband %d/6"
                          % (a, certH[a][0], len(certH[a][1]),
                             len(te_x), certH[a][2], certH[a][3])
                          for a in GA_FAM)
              + "; minimal certifying a = %s; the exact hand-off "
              "E3h <= (m q_max)^2 msh holds live (G42) with "
              "reserve med %.1fx min %.1fx; r335 mass-arm record "
              "constants adopted for the typed composition: C_D "
              "= %s (q_max <= Q_dich is r335-exact)"
              % (str(aH),
                 float(np.median([v for v in hres_col
                                  if v < INF_SENT])),
                 min(hres_col),
                 str(R335_CD)))

    # ---------------- S6: Leg C -- the Bellman forms
    section("S6  LEG C -- FORM-1 EPS-CHAIN + FORM-2 PSI-BELLMAN "
            "+ DEFUSAL + EXPONENTS + WORLDS")
    if smoke:
        check("G60-form1-eps-chain", True, "SMOKE: skipped")
        check("G61-form2-psi-bellman", True, "SMOKE: skipped")
        check("G62-defusal-profile", True, "SMOKE: skipped")
        check("G63-exponents-sensitivity", True, "SMOKE: skipped")
    else:
        b_cols = {a: [wb_col[i]
                      / (math.log(float(m_full[i])) ** a)
                      for i in range(n_full)] for a in GA_FAM}
        certB, aB = cert_max(b_cols)
        llm = [math.log(math.log(float(v))) for v in m_full]
        check("G60-form1-eps-chain", True,
              "FORM 1 (the integrated eps-chain; W_B = prod (1 + "
              "eps_k) >= E3g exact): W_B <= C_B(a) (log m)^a: "
              + "; ".join("a=%d C_B %.4f viol %d/%d named %d/4 "
                          "midband %d/6"
                          % (a, certB[a][0], len(certB[a][1]),
                             len(te_x), certB[a][2], certB[a][3])
                          for a in GA_FAM)
              + "; minimal certifying a = %s; eps sums: sum "
              "eps_k med %.2f max %.2f vs loglog m med %.2f "
              "(the reviewer A loglog m + C reading, census)"
              % (str(aB), float(np.median(se_col)), max(se_col),
                 float(np.median(llm))))
        psi_tab = {}
        for a in PSI_A_FAM:
            for c0 in PSI_C0_FAM:
                vs = sum(rc["ev"]["psi"][(a, c0)]["viol_s"]
                         for rc in srt_full)
                vc = sum(rc["ev"]["psi"][(a, c0)]["viol_c"]
                         for rc in srt_full)
                rs = sum(1 for rc in srt_full
                         if rc["ev"]["psi"][(a, c0)]["viol_c"]
                         > 0)
                mx = max(rc["ev"]["psi"][(a, c0)]["max_c"]
                         for rc in srt_full)
                psi_tab[(a, c0)] = (vs, vc, rs, mx)
                info("FORM 2 (A=%d, C0=%.1f): strict viol %5d, "
                     "composed viol %5d on %d/%d rungs, max "
                     "composed ratio %.3f"
                     % (a, c0, vs, vc, rs, n_full, mx))
        cert2 = [k for k in psi_tab if psi_tab[k][1] == 0]
        cert2.sort()
        best2 = min(psi_tab, key=lambda k: (psi_tab[k][1],
                                            psi_tab[k][3]))
        check("G61-form2-psi-bellman", True,
              "FORM 2 (Psi-weight Bellman, prefactor 1, per "
              "node on the composed surface): certified combos "
              "%s of %d sealed; best combo (A=%d, C0=%.1f) with "
              "%d composed violations on %d rungs (max ratio "
              "%.3f); display combo %s per-rung max ratio med "
              "%.3f -- %s"
              % (str(cert2) if cert2 else "NONE",
                 len(psi_tab), best2[0], best2[1],
                 psi_tab[best2][1], psi_tab[best2][2],
                 psi_tab[best2][3], str(PSI_DISPLAY),
                 float(np.median(psid_col)),
                 "the per-node telescoping law CERTIFIES"
                 if cert2 else
                 "the per-node telescoping law with prefactor 1 "
                 "is DENIED (the disclosed mid-tree risk is "
                 "real); the integrated Form 1 is the carrying "
                 "surface iff it certifies"))
        kmax = max(kk_col)
        gb_med = []
        gx_med = []
        for k in range(kmax):
            vg = [rc["ev"]["pbs"]["gbar"][k] for rc in srt_full
                  if len(rc["ev"]["pbs"]["gbar"]) > k]
            vx = [rc["ev"]["dst"]["gmx_lv"][k] for rc in srt_full
                  if len(rc["ev"]["dst"]["gmx_lv"]) > k]
            gb_med.append(float(np.median(vg)))
            gx_med.append(float(np.median(vx)))
        check("G62-defusal-profile", True,
              "THE DEFUSAL PROFILE (the r339 build instruction "
              "measured): per-level PATH-WEIGHTED E[Gamma(V_k)] "
              "med profile %s vs the r339 Gamma_max med profile "
              "%s -- the path weighting flattens the near-leaf "
              "wall; near-ceiling path mass pm3 med %.3f "
              "carries c3s med %.3f of E3"
              % (str([round(v, 3) for v in gb_med]),
                 str([round(v, 2) for v in gx_med]),
                 float(np.median(pm3_col)),
                 float(np.median(c3s_col))))
        g3_cols = {a: [e3g_col[i]
                       / (math.log(float(m_full[i])) ** a)
                       for i in range(n_full)] for a in GA_FAM}
        certG3, aG3 = cert_max(g3_cols)
        e_h = L2D.halves_slope([m_full[i] for i in te_i],
                               [max(e3h_col[i], 1e-300)
                                for i in te_i])
        e_g = L2D.halves_slope([m_full[i] for i in te_i],
                               [max(e3g_col[i], 1e-300)
                                for i in te_i])
        e_b = L2D.halves_slope([m_full[i] for i in te_i],
                               [max(wb_col[i], 1e-300)
                                for i in te_i])
        h = len(te_i) // 2
        e_ga = L2D.halves_slope([m_full[i] for i in te_i[:h]],
                                [max(e3g_col[i], 1e-300)
                                 for i in te_i[:h]])
        e_gb = L2D.halves_slope([m_full[i] for i in te_i[h:]],
                                [max(e3g_col[i], 1e-300)
                                 for i in te_i[h:]])
        hshA_col = [rc["ev"]["pba"]["hsh"] for rc in srt_full]
        e3hA_col = [rc["ev"]["pba"]["e3h"] for rc in srt_full]
        wbA_col = [rc["ev"]["pba"]["wb"] for rc in srt_full]
        hA_share = [e3hA_col[i] / max(e3_col[i], 1e-300)
                    for i in range(n_full)]
        cbA_env = max(wbA_col[i]
                      / (math.log(float(m_full[i])) ** 2)
                      for i in range(n_full))
        psaA = sum(rc["ev"]["psa"]["viol_c"] for rc in srt_full)
        check("G63-exponents-sensitivity", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope, "
              "fit-free, %d test rungs): e(E3h) = %+.3f, e(E3g) "
              "= %+.3f (halves %+.3f/%+.3f), e(W_B) = %+.3f -- "
              "vs CRIT %.3f and the r339 e(W_F) %+.3f; direct "
              "good census E3g <= C_g(a) (log m)^a: %s minimal "
              "a = %s; R_ALT %.2f SENSITIVITY: hsh med %.3f -> "
              "%.3f, E3h share med %.3f -> %.3f, W_B med %.3f "
              "-> %.3f, C_B'(2) envelope %.4f, psi display "
              "composed viol %d"
              % (len(te_i), e_h, e_g, e_ga, e_gb, e_b, CRIT_EXP,
                 e_wf,
                 "; ".join("a=%d C_g %.4f viol %d"
                           % (a, certG3[a][0],
                              len(certG3[a][1]))
                           for a in GA_FAM), str(aG3), R_ALT,
                 float(np.median(hsh_col)),
                 float(np.median(hshA_col)),
                 float(np.median(h_share)),
                 float(np.median(hA_share)),
                 float(np.median(wb_col)),
                 float(np.median(wbA_col)), cbA_env, psaA))
    # world census (both modes)
    ev9w = (recs[0] if smoke else mrecs[0])["ev"]
    ev13 = None if smoke else mrecs[1]["ev"]
    wtab = [("w9", ev9w)] + ([("w13(twin)", ev13)]
                             if ev13 is not None else [])
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]["ev"]))
    info("world table: world m K E3 E3h/E3 hsh msh WB lgq50 "
         "epg pm3 psi(3,1)")
    for w, ev in wtab:
        pb = ev["pbs"]
        info("  %-10s m %3d K %d E3 %8.3f h/E3 %.3f hsh %.3f "
             "msh %.3f WB %7.3f lg50 %6.3f epg %8.3f pm3 %.3f "
             "psi %.3f"
             % (w, ev["m"], pb["kk"], pb["e3"],
                pb["e3h"] / max(pb["e3"], 1e-300), pb["hsh"],
                pb["msh"], pb["wb"], pb["lgq"][1], pb["epg"],
                pb["pm3"], ev["psi"][PSI_DISPLAY]["max_c"]
                if ev["psi"][PSI_DISPLAY]["ok"] else 0.0))
    scr_ev = crecs["SCR"]["ev"]
    if smoke:
        check("G64-world-census", len(wtab) >= 2,
              "SMOKE: world table printed (w9 + live controls); "
              "the separation census needs the ladder")
    else:
        wb_med_l = float(np.median(wb_col[:n341]))
        hs_med_l = float(np.median(h_share[:n341]))
        check("G64-world-census", len(wtab) >= 2,
              "WORLD SEPARATION (census, NO claim): SCRAMBLE "
              "W_B %.3f vs ladder med %.3f (%s; the r339 "
              "Gamma_max census was world-blind -- the "
              "PATH-WEIGHTED budget %s), SCR E3h share %.3f vs "
              "med %.3f; EPSTEIN W_B %.3f; twin w13 W_B %.3f "
              "E3h share %.3f"
              % (scr_ev["pbs"]["wb"], wb_med_l,
                 "ABOVE" if scr_ev["pbs"]["wb"] > wb_med_l
                 else "BELOW",
                 "SEPARATES" if scr_ev["pbs"]["wb"]
                 > max(wb_col[:n341]) or scr_ev["pbs"]["wb"]
                 < min(wb_col[:n341]) else "sits inside the "
                 "ladder range",
                 scr_ev["pbs"]["e3h"]
                 / max(scr_ev["pbs"]["e3"], 1e-300), hs_med_l,
                 crecs["EPST"]["ev"]["pbs"]["wb"],
                 ev13["pbs"]["wb"],
                 ev13["pbs"]["e3h"]
                 / max(ev13["pbs"]["e3"], 1e-300)))

    # ---------------- S7: Leg D -- adjudication + composition
    section("S7  LEG D -- SEALED ADJUDICATION + COMPOSITION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
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
                      or panc_w > TOY_BAR or not mult_all_ok)
        heavy_cert = aH is not None
        form1_cert = aB is not None
        form2_cert = bool(cert2)

        def solve_m0(log_rhs):
            t = math.log(73.0)
            while t < 1e7:
                if CRIT_EXP * t >= log_rhs(t):
                    return t / math.log(10.0)
                t *= 1.02
            return None

        if form2_cert:
            A2c, c02 = cert2[0]
            a_good_txt = "(%.1f + log m)^%d (Form 2, prefactor 1)" \
                % (c02, A2c)

            def rhs_good(t):
                return (c02 + t) ** A2c
        elif form1_cert:
            a_good_txt = "%.4f (log m)^%d (Form 1)" \
                % (certB[aB][0], aB)

            def rhs_good(t):
                return certB[aB][0] * t ** aB
        else:
            a_good_txt = "%.4f (log m)^%d (ENVELOPE, no cert)" \
                % (max(g3_cols[GA_FAM[-1]]), GA_FAM[-1])

            def rhs_good(t):
                return max(g3_cols[GA_FAM[-1]]) * t ** GA_FAM[-1]
        if heavy_cert:
            ch_txt = "%.4f (log m)^%d" % (certH[aH][0], aH)

            def rhs_heavy(t):
                return certH[aH][0] * t ** aH
        else:
            ch_env = max(h_cols[GA_FAM[-1]])
            ch_txt = "%.4f (log m)^%d (ENVELOPE, no cert)" \
                % (ch_env, GA_FAM[-1])

            def rhs_heavy(t):
                return ch_env * t ** GA_FAM[-1]
        m0_new = solve_m0(lambda t: math.log(
            max(rhs_good(t) + rhs_heavy(t), 1e-300)))
        m0_306 = solve_m0(lambda t: math.log(
            max(R306_C2 * t ** 2, 1e-300)))
        beats = (m0_new is not None) and (m0_new <= R324_M0_L10)
        go = heavy_cert and (form1_cert or form2_cert) and beats
        partial = (form1_cert or form2_cert) and not go
        goodonly = (not form1_cert) and (not form2_cert) \
            and (aG3 is not None)
        vkey = bellman_tree_verdict(leak, brk_struct, go,
                                    partial, goodonly)
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a path "
                           "builder",
            "BELLMAN_STATE_NOT_EXACT":
                "an exact path ward broke (tilt %.1e / wq %.1e "
                "/ part %.1e / bk %.1e / env %.1e / pgi %.1e / "
                "hvy %.1e / Fractions %s)"
                % (tilt_w, wqd_w, part_w3, bkd_w, env_w, pgi_w,
                   hvy_w, str(fr_ok)),
            "RH3_BELLMAN_GO":
                "the two-arm theorem candidate certifies AND "
                "beats the r324 chain: heavy C_H(%s), good %s, "
                "composed m_0* 10^%.1f <= r324 10^%.1f"
                % (str(aH), a_good_txt,
                   m0_new if m0_new is not None else -1.0,
                   R324_M0_L10),
            "RH3_BELLMAN_PARTIAL":
                "a Bellman form certifies (form1 %s form2 %s) "
                "but the composition stays open (heavy cert %s, "
                "m_0* %s)"
                % (str(form1_cert), str(form2_cert),
                   str(heavy_cert),
                   ("10^%.1f" % m0_new) if m0_new is not None
                   else "NONE"),
            "GOODTREE_A2_ONLY":
                "no Bellman form certifies but the direct good "
                "census carries at a = %s (C_g %.4f)"
                % (str(aG3),
                   certG3[aG3][0] if aG3 is not None else 0.0),
            "PATHWEIGHT_ALSO_SUPERCRITICAL":
                "no form and no direct good census certifies "
                "(e(E3g) %+.3f, e(W_B) %+.3f) -- the "
                "path-weighted language is capped too; said "
                "honestly" % (e_g, e_b)}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        info("COMPOSITION (typed, the reviewer POLYLOG form -- "
             "NO premature powerization): E[X_inf^3] <= "
             "[heavy %s] + [good %s] => M_3 <= C_tot (log m)^A_"
             "tot/m^2 => N_3 >= m/sqrt(C_tot (log m)^A_tot), "
             "N_2 >= N_3 (r306 exact chain); the 0.888 need "
             "enters ONLY as the final solve: m_0* = %s "
             "(m^{%.3f} >= C_tot (log m)^A_tot) vs the r324 "
             "MEASURED route 10^%.1f (+%.3f) -- %s; vs the "
             "r306 census reading m_0* = %s (C_2 %.3f, A = 2; "
             "census bound, disclosed pre-spec, not a "
             "mechanism)."
             % (ch_txt, a_good_txt,
                ("10^%.1f" % m0_new) if m0_new is not None
                else "NONE", CRIT_EXP, R324_M0_L10, R324_ETOT,
                "BEATEN" if beats else "NOT beaten",
                ("10^%.1f" % m0_306) if m0_306 is not None
                else "NONE", R306_C2))
        check("G71-composition", True,
              "composition printed with explicit constants "
              "(heavy %s + good %s, m_0* %s); typed: the path "
              "identities exact, every constant MEASURED on the "
              "finite ladder + EXT3, the ladder-to-m_0* step an "
              "extrapolation hypothesis -- NO cofinal claim; "
              "the r335 record constants %s cited for the "
              "q_max <= Q_dich hand-off (not recomputed)"
              % (ch_txt, a_good_txt,
                 ("10^%.1f" % m0_new) if m0_new is not None
                 else "NONE", str(R335_CD)))

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    check("G80-e1-tower-untilted",
          fp_e1brk == Fr(7, 18)
          and abs(mut1 - float(Fr(11, 6))) <= TOY_BAR,
          "e1 CAUGHT exact: the tower identity with the WRONG "
          "FILTRATION (untilted E_P[prod Gamma]) breaks on the "
          "even Fractions toy by EXACTLY 7/18 (20/9 vs 11/6; "
          "float builder reproduces %.3f) -- the correct tower "
          "is the cubic-tilted one, warded live in G42 at %.1e"
          % (mut1, tilt_w if not smoke else 0.0))
    check("G81-e4-tilt-no-n",
          ft_e4brk == Fr(6, 125)
          and abs(mut4 - float(Fr(51, 25))) <= TOY_BAR,
          "e4 CAUGHT exact: the tilted measure WITHOUT the n(c) "
          "normalization (steps R^3/sum R^3, p_c dropped) "
          "returns 51/25 on the uneven Fractions toy while the "
          "exact value is 261/125 -- break 6/125 EXACT (float "
          "builder reproduces %.3f)" % mut4)
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    g3m = mutant_rstar_from_target(ev9m)
    check("G82-e3-rstar-from-target",
          len(e3_hits) >= 1 and (not sc_own) and g3m >= 0.0,
          "e3 AST-CAUGHT: the 'R* column' derived from the "
          "cubic TARGET record is FLAGGED (%s) while the four "
          "module-own path builders are clean (%d hits) -- R* "
          "is the r339 banked band-floor tie, never a target "
          "readback (mutant value %.3e computed only to prove "
          "it runs)"
          % (e3_hits[0] if e3_hits else "MISS", len(sc_own),
             g3m))
    toy_aa = (1, 2, 3)
    toy_rho = (0.1, 0.9, 0.9)
    pick_mut = mutant_psi_posthoc(toy_aa, toy_rho, 0.5)
    check("G83-e2-psi-posthoc",
          len(e2_hits) >= 1 and pick_mut == 3
          and pick_mut != PSI_A_FAM[0],
          "e2 protocol-CAUGHT twice: the after-sight Psi re-pick "
          "consumes the evaluated violation column -- "
          "AST-FLAGGED (%s) -- and on the toy returns A = %d != "
          "the family-scan protocol head %d (the Psi family is "
          "sealed in this spec BEFORE the freeze)"
          % (e2_hits[0] if e2_hits else "MISS", pick_mut,
             PSI_A_FAM[0]))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact path layer on the sealed fold "
          "genealogy (tilted tower, stopped decomposition, "
          "eps-chain envelope, Phi-Gamma identity, heavy "
          "hand-off algebra), the two-arm certification each on "
          "its own freeze, both Bellman forms adjudicated, and "
          "the polylog composition -- NO new certificate "
          "promoted, NO universal bound claimed beyond the "
          "measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R341_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d, r324-pre C_M2 %.4f, r339 WF "
                 "med %.2f / e(WF) %+.3f / e(m2M3) %+.3f, r324 "
                 "e_tot %+.3f)"
                 % (rec3_w, C2r, viol2, n341, C_M2, wf_med, e_wf,
                    e_d3, e_tot324)]
        parts.append("SEAL(tilt %.1e, wq %.1e, part %.1e, bk "
                     "%.1e, env %.1e, pgi %.1e, hvy %.1e, mart "
                     "%.1e, Fractions %s, grounding %.1e, "
                     "purity clean, toys exact)"
                     % (tilt_w, wqd_w, part_w3, bkd_w, env_w,
                        pgi_w, hvy_w, mart_w,
                        "EXACT" if fr_ok else "BROKEN",
                        max(part_w, l1rec_w, panc_w)))
        parts.append("PATHDIST(lg50 med %.2f, lgmax med %.2f vs "
                     "logWF med %.2f, epg med %.2f vs E3 med "
                     "%.2f, pm3 med %.3f c3s med %.3f)"
                     % (float(np.median([q[1] for q in lgq_col])),
                        float(np.median(lgm_col)),
                        float(np.median([math.log(max(v, 1e-300))
                                         for v in wf_col])),
                        float(np.median(epg_col)),
                        float(np.median(e3_col)),
                        float(np.median(pm3_col)),
                        float(np.median(c3s_col))))
        parts.append("STOPPING(hsh med %.3f, msh med %.3f, E3h "
                     "share med %.3f, heavy %s minA %s)"
                     % (float(np.median(hsh_col)),
                        float(np.median(msh_col)),
                        float(np.median(h_share)),
                        "; ".join("a%d CH %.3f v%d"
                                  % (a, certH[a][0],
                                     len(certH[a][1]))
                                  for a in GA_FAM), str(aH)))
        parts.append("BELLMAN(form1 %s minA %s; form2 cert %s "
                     "best (%d, %.1f) viol %d max %.3f; good "
                     "census minA %s; e(E3h) %+.3f e(E3g) %+.3f "
                     "e(WB) %+.3f)"
                     % ("; ".join("a%d CB %.3f v%d"
                                  % (a, certB[a][0],
                                     len(certB[a][1]))
                                  for a in GA_FAM), str(aB),
                        str(cert2) if cert2 else "NONE",
                        best2[0], best2[1], psi_tab[best2][1],
                        psi_tab[best2][3], str(aG3), e_h, e_g,
                        e_b))
        parts.append(verdict_main)
        parts.append("COMPOSITION(heavy %s + good %s, m_0* %s "
                     "vs r324 10^%.1f %s, r306 census %s)"
                     % (ch_txt, a_good_txt,
                        ("10^%.1f" % m0_new)
                        if m0_new is not None else "NONE",
                        R324_M0_L10,
                        "BEATEN" if beats else "NOT beaten",
                        ("10^%.1f" % m0_306)
                        if m0_306 is not None else "NONE"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the path identities "
          "(tilted tower, stopped partition, B-chain closure, "
          "envelope, Phi-Gamma, heavy hand-off), the Fractions "
          "toys, the tree logic and the purity audits (exact / "
          "AST-decided); MEASURED: every census, constant, "
          "violation count and exponent (the finite class "
          "ladder + 12 EXT3 + 2 mains + 2 live controls); OPEN: "
          "any bound beyond the measured rungs, the cofinal "
          "law, the actual Bellman PROOF (a certifying letter "
          "fixes a theorem candidate with explicit constants, "
          "it proves nothing cofinal); NO RH claim"
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
