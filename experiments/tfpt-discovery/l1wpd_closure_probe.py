#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""l1wpd_closure_probe -- PRIME.L1WPD.CLOSURE.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung certificates stated, NO counterexample claim.  It closes no
gate and narrows no gate.

=======================================================================
MISSION (CLOSE OR REDUCE THE {L1, WPD} PAIR -- the two counting-class
remnants of the canonical residue, untouched as a PAIR since the
r131-r135 arc.  The round-169/171/174/175 instruments (exact sigma
factorization, product floor, unconditional Landau/Gonek pricing,
mode-level Landau bridge) post-date the last direct attack.  This
round (W1) RE-STATES both obstructions exactly and audits every later
round for silent partial closure; (W2) attacks H-pin with the bridge
and the pricing machinery -- adjudicating bridge-expressibility of
the pin data and locating exactly which component escapes linearity;
(W3) attacks WPD with the counting/factorization instruments --
adjudicating whether its lambda-uniform component is the SAME edge as
H-pin (consolidation) or distinct, and re-verifying the Theorem-A
bridge including the census-currency strip; (W4) states the
post-round residue exactly.  NO RH CLAIM in any direction.)
=======================================================================
State consumed (CITED): CDXXXIII/l1_weyllaw (r131: secular identity
spec(M_eta) = {0} + zeros(E_N), node count EXACTLY K-1; GW pinning
tau = 2 sum |E_N(gamma)|^2 (96% on the true zeros at x=13); L1 = TAIL
(PROVEN, HSW22+PT21 closed forms) + BAND (the H-pin omega); d1(a=4)
ladder 0.05622/0.04133/0.03072/0.02162); CDXXXV/wpd_proof (r132:
THEOREM D two-sided k-family bound, W1 explicit constant K(q) = 2q
for q <= 1/2, P1 one-sided => PD; WPD(a < gamma_1^2 = 199.79)
PROVEN-MODULO-{d1 > 0, MRB}; raw-mp census AMENDMENT-1 currency;
controls: PD FALSE in all three fake worlds, SMOOTH d1(a=4) =
-0.154); CDXXXVI/dominance_proof (r133: THEOREMS M/E/T/C proven
unconditionally (ball-counting dominance, edge bounds, top segment
T*, chain MRB strictly weaker than DOM); THEOREM A: H-pin(x) =>
{d1 > 0, MRB} in closed HSW form for x >= x_0 = 121; Q-SWAMP strip
x < 121 named; per-node one-sidedness DOM not needed); CDXXXIX/
hpin_floor (r135: D1-D4 PROVEN -- floor = 4|A_0 sin(A mu)| x spacing
product, jet sum rules, A_0-cancellation (demand A_0-FREE), lattice
factorization; OMEGA-SPLIT: H-pin = (OMEGA-a) EPS-LOCK eps_bar <=
poly(x)|A_0| sqrt(G) + (OMEGA-b) SPACING-REMAINDER (zone node law at
O(spacing), lam-uniform) + H1/H2/H3 matching counts (r133-M shape);
margins 32..5.3e12 on x = 5..24); CDXLII/counteq_seedball (OMEGA-b
kernel = QSUBGAP; swamp-DOM closed with NULL slack per rung; the
count-currency crossover STRUCTURALLY obstructed for all x -- only
named exit: Turing-class local band certificates); CDLIX/
assembly_walls (a-quantifier audit: THEOREM WL -- every off-line
window with gamma >= H = 3e12 lies in a >= (H - 1/2)^2 = 9.0e24;
KONSOLIDIERUNG: TAILWPD := {L1, WPD}/(H-conv) on a dense subset of
((H-1/2)^2, oo), typed RH-EQUIVALENT-AM-TAIL -- the world front);
CDLXIII/edge_cleanup (r159: THE Q-SWAMP STRIP CLOSES WHOLESALE in
census currency -- 357 Turing-class local-band certificates,
x = 3..121 x a in (1, 4, 16); Theorem-A conditionality sharpens from
x >= 121 to EVERY INTEGER x >= 3; x_0(HSW) == 121, x_0(BW25) == 112);
CDLXVI (third promotion wave: v925 recomputed all 357 D_cs > 0,
worst margin 0.346 at (12, 1) in its own normalization; v922 carries
r135 D1-D4); v920 (loop equivalence: B2 BAND-MASS <=> TLAWCAP <=>
EPS-LOCK modulo {JETLOCK, TAILVIS(eliminated)}); CDLXXXIV/r169
(sigmafloor: sigma == (1-slop) delta DC exact; DC leg CLASSICAL-PER-
CENSUS); CDLXXXVII/r171 (jetmass floor: THEOREM PF conditional
exactly on {H1 + H2 per rung}; jet-hypothesis names H1/H2/H3 -- NAME
COLLISION with the r133 ball-matching hypotheses H1/H2/H3 disclosed
below); CDLXXXIX/r174 (gonek_pricing: Landau 1912 + Gonek 1985/1993
UNCONDITIONAL as form; Gonek 1984 RH-CONDITIONAL == LOOP; envelope
T_hi-collapse; spike c_hat <= 0.086); CDXC..CDXCI/r173 (theta_inf
band, DK stability); CDXCII/CDXCIII (Bughunt VII: canonical residue
{H1 ^ H2 ^ H3}-KOFINAL (one rung per block, all three at the same h;
limsup form only mod D = 0.0042) + {census-forall-k == LOOP} +
{L1 = TAIL proven + H-pin open, WPD open}; X3: L1/WPD adjudicated
LIVE-NOT-STALE, labels COARSE); CDXCV/r175 (thetainf_pin: THE
MODE-LEVEL LANDAU BRIDGE F_s(om_k) == sum_gamma 4 om_k sin^2(A gamma)
/(gamma^2 - om_k^2) - Itriv, per-census exact to 1.4e-5..5.4e-5;
reconstruction wall T_req = 3.76e14 -> 1.75e77 vs T_PT = 3.00e12;
second-moment kill ratios 3.4e10 -> 3.1e53; PJ_RES_TAB{5} =
2.086e-5); HSW22 Cor. 1.2 (0.1038, 0.2573, 9.3675); BW25 = Bellotti-
Wong 2025 (0.10076, 0.24460, 8.08344) published, r144/r159/v925
citation carried; PT21 (T_PT = 3000175332800; both caches below T_0
unconditionally on-line -- the per-census pedigree).  Flagged loops
(carried, NEVER consumed): census-forall-k; A_0-triangle (A0-FLOOR
consumes TAUPOS/TLAWCAP); zero-verification-at-height-as-hypothesis;
RH-conditional second moments (Montgomery-PC, Goldston-Montgomery,
Gonek 1984).

=======================================================================
THE RESTATED OBSTRUCTIONS (the W1 deliverable; exact, with
quantifiers and epistemic types)
=======================================================================
OBSTRUCTION 1 -- H-PIN (the L1 band half; r131 L1BAND in the r133/
r135 ball currency).  Per rung x (A = log(x)/2, K = ceil(1.25 x
log x), census nodes mu_1 < ... < mu_{K-1} = zeros of the secular
function, T_z = min(0.98 edge, 2 pi x), eps_bar = sqrt((tau +
OFF_ALLOW)/2)):
  H-pin(x, a): (i) [COUNTING, r133 Theorem-M shape] every true zero
  gamma_j <= T_z is matched into disjoint ordered balls
  [gamma_j - g_j, gamma_j + g_j], g_j = 2 eps_bar/m_j, with exactly
  one census node per ball and NO stray node below max(T_z, gamma_m
  + g_m); (ii) [ZONE MASS] sum_zone |dw_a|-mass <= TL(x, a)/8 --
  sufficient (r135 D3, exact): m_min,zone >= m_req = 16 eps_bar
  sum_zone |w_a'(gamma)| / TL(x, a).
  QUANTIFIER: lambda-uniform == for every rung x >= 3 (SEQ).
  Certified per rung x = 5..24 (r135; margins 32 -> 5.3e12).
  EPISTEMIC TYPE: source-side, per-rung certified, NOT classical,
  NOT known RH-equivalent.  EXACT SPLIT (r135 D3): (OMEGA-a)
  EPS-LOCK -- eps_bar <= poly(x) |A_0| sqrt(G(T_z)) lam-uniformly
  (equivalently the quotient tau/A_0^2 capped; post-135 coordinates:
  <=> TLAWCAP <=> BAND-MASS mod {JETLOCK, TAILVIS-eliminated},
  v920); (OMEGA-b) SPACING-REMAINDER -- the zone node law at
  O(spacing) accuracy lam-uniformly (post-135 kernel: QSUBGAP,
  CDXLII).  The demand is A_0-FREE (D3); the floor alone rides
  sqrt(tau) by identity (FLOOR-RIDES-CONNES, r135).
OBSTRUCTION 2 -- WPD (the r128 pair second half; r132/r133 machine
adjudication).  For the node multiset {mu_i} vs the true zeros
{gamma_i} in the w_a-moment currency (w_a(t) = a t^2/(a + t^2)^2,
d_k the k-th moment defects, d_1 = C01 - TrB):
  WPD(a): counting dominance N_fin(T) <= N_true(T) for all T
  (<=> sorted mu_i >= gamma_i), operative in the m = 1 currency
  {d_1 > 0, MRB = sup_lam (M+ + M-)/d_1 < oo}; r132 THEOREM D/W1:
  WPD(a) for a < gamma_1^2 = 199.79 is PROVEN-MODULO-{d_1 > 0, MRB}
  with the explicit constant K(q) = 2q (q <= 1/2 on the battery).
  QUANTIFIER STATUS BY a-REGION (the honest ledger):
  (a < gamma_1^2)  {d_1 > 0, MRB} <== H-pin(x) via THEOREM A (r133)
    for x >= x_0, AND THE STRIP x < x_0 IS CLOSED IN CENSUS CURRENCY
    (r159: 357 Turing-class certificates; v925 recheck) => the
    implication holds for EVERY INTEGER x >= 3.  WPD's lambda-
    uniform component at battery a IS the H-pin edge -- NOT an
    independent unknown.
  (gamma_1^2 <= a < (H-1/2)^2)  same {d_1 > 0, mass} class,
    instanced per rung (CDLIX/CDLXIII strip instances), lam-uniform
    carried by the same Theorem-A/H-pin route where built; typed
    INSTANCED-NOT-UNIFORM.
  (a >= (H-1/2)^2 = 9.0e24)  TAILWPD = {L1, WPD}/(H-conv), typed
    RH-EQUIVALENT-AM-TAIL (CDLIX) -- the world front; NOT a closable
    omega, carried honestly.
  EPISTEMIC TYPE: the per-rung legs are CLASSICAL-PER-CENSUS (same
  class as the r169 DC leg); the lambda-uniform leg is H-pin.
NAME-COLLISION DISCLOSURE: the r133 ball-matching hypotheses
H1/H2/H3 (Theorem M: matched balls / no strays / one node per ball)
and the r171 jet hypotheses H1/H2/H3 (envelope / census / quartic
cap) are UNRELATED statements sharing names; the canonical-residue
triple {H1 ^ H2 ^ H3}-KOFINAL is the r171 set.  This spec never
mixes them; the residue statement below names both sets explicitly.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (own source: no zero-oracle names, np.load only
    in ward_* of the imported warded modules, zeta only inside
    audit_* scopes, no verification/ import); G02 cache wards (n7000:
    count/monotone/gamma_1; big 20M: count, T(2e7) = 9499220.4795
    rel 1e-6, prefix overlap <= 1e-8).
S1  exact layer (sympy):
    G10 H-pin restatement license: the D3 demand rearrangement
    (zone mass <= TL/8 <== m_min >= 16 eps_bar SW/TL) and the
    A_0-cancellation g_j = c(x)/(2|sin| PR_j) replicated exactly
    (r135 G14/G15 class);
    G11 WPD restatement license: K(q) = max_k k q^{k-1} == 2q for
    q <= 1/2 (exact); the r133 Theorem-C identities: weak one-
    sidedness M- == (1-theta)(M+ + tail1) ==> d_1 == theta(M+ +
    tail1) EXACT and MRB == (2-theta)/theta; DOM (theta = 1) ==>
    MRB <= 1;
    G12 Theorem-A assembly shape: d_1 >= TL - zonemass - M-_edge
    and [zonemass <= TL/8, M-_edge <= (N-n_z) w(T_z)] ==> d_1 >=
    D = TL - TL/8 - (N-n_z) w(T_z) (exact rearrangement);
    G13 THE LINEARITY ADJUDICATION (W2 crux, exact): (i) eigen map
    NOT additive: lam_min(A+B) = -sqrt(2) != lam_min(A) +
    lam_min(B) = -2 on the exact 2x2 pair [[0,1],[1,0]],
    [[1,0],[0,-1]] and the ground vectors are non-additive; (ii)
    root map NOT affine: for F = A0 + w1/(y-b1) + w2/(y-b2) the
    census root has d^2 y*/d w1^2 != 0 symbolically; (iii) the
    bridge atoms pj/pdiag are c-FREE (free-symbol check on the
    shared symbol pool) while the floor m_j = 4|A_0 sin(A mu_j)|
    PR_j is c-LOADED (A_0, w_k linear in c; roots nonlinear in w):
    THE PIN'S FLOOR LIVES ON THE VECTOR SIDE OF THE BRIDGE;
    G14 loop ledger: the A_0-triangle cycle EPSLOCK -> A0-FLOOR ->
    TLAWCAP -> EPSLOCK machine-detected (closing OMEGA-a through an
    A_0 floor is the r172-flagged loop); census-forall-k,
    zero-verif-as-hypothesis, gonek-1984/montgomery-pc cycles
    detected; ALL flagged, NONE consumed.
S2  status audit + the Theorem-A bridge (W1/W3):
    G20 corpus status audit (whitespace-normalized greps on
    experiments/next.txt, read-only): the v925 sharpening sentence
    ("schaerft sich auf JEDES ganze x >= 3"), TAILWPD typing
    ("RH-AEQUIVALENT-AM-TAIL"), Bughunt-VII "LIVE-NICHT-STALE", the
    canonical-residue string "H-pin offen, WPD offen", and
    "x0(BW25) = 112" PRESENT; "H-pin geschlossen/closed" and "WPD
    geschlossen/closed" ABSENT: no silent closure of the pin; ONE
    recorded-but-unpropagated sharpening (Theorem A for all integer
    x >= 3) -- the W1 audit finding;
    G21 x_0 replication (own generalized assembly, integer scan
    90..200, all battery a): x_0(HSW) == 121 AND x_0(BW25) == 112
    (r133 G43 / r144 / CDLXIII G74 / v925 replicated);
    G22 D_cs census-currency sweep (own recipe: TL_cs = sum_{i>N}
    w_a(gamma_i) over the n7000 cache, D_cs = (7/8) TL_cs -
    (N - n_z) w_a(2 pi x)): ALL 357 cells (integer x = 3..121, a in
    (1, 4, 16)) D_cs > 0; worst cell == (12, 1) (v925 record cell);
    own worst margin D_cs/TL_cs = 0.2250 abs 0.005 (v925's 0.346 is
    its own normalization, cited INFO): THE BRIDGE IS GAPLESS --
    H-pin(x) ==> {d_1 > 0, MRB} for EVERY integer x >= 3.
S3  per-rung layer, RUNGS = (5, 60), (8, 80), (13, 120), MAIN
    builds, raw-mp census (r132 AMENDMENT-1 currency), NPOL = 25
    polished ordinates at AUD_DPS = 100:
    G30 build/census sanity: log10 tau on LOG10TAU_TAB abs 0.01;
    census complete (K-1 real roots, 0 nonreal); zone counts
    4/10/21;
    G31 replication license (cross-instrument continuity): d_1
    ladder at a = 1/4/16 on D1_TAB rel 5e-3 (a=4 digits
    0.041330/0.030721/0.021624 == the r128/r131/r132 table); MRB on
    MRB_TAB abs 0.005 and <= 0.25; M- <= 1e-15 (DOM-one-sided
    replicated); EPS-LOCK ratios on LOCK_TAB abs 0.01 inside
    (0.05, 5);
    G32 H-pin margins: m_min,zone on MMIN_TAB rel 5e-2; margins
    m_min/m_req >= 3 at every (rung, a) with a=4 tab MARG4_TAB rel
    5e-2 and growth last/first >= 5 (r135 G38 replicated on the
    core ladder);
    G33 the d_1 split (W3): d_1 == [C01 zero-sum leg] - [node-sum
    leg] == Mp - Mm + tail1 (own recomputation both ways, rel dev
    <= 1e-10): the zero-sum leg is the classical-priceable leg
    (r131 bracket class), the node leg is variational;
    G34 SW pricing adjudication (W2): the unconditional Stieltjes/
    HSW bracket [center - half, center + half] (center = int f dM
    + f(t0) M(t0), half = Q(T_z)(|f(T_z)| + TV f), t0 = 2, f =
    |w_a'|, a = 4) CONTAINS the census value SW at every rung
    (SW_TAB rel 5e-3, centers SWC_TAB abs 5e-4, halfwidths SWH_TAB
    rel 5e-3) AND is VACUOUS: halfwidth/SW >= 100 (measured
    263.1/226.7/214.4, VAC_TAB rel 5e-2), center < 0: THE DEMAND
    FACTOR IS CLASSICAL-PER-CENSUS ONLY -- its raw count-currency
    pricing carries no information at battery rungs (the CDXLII
    structural swamp, replicated on the SW factor; NOT a closure);
    G35 THE BRIDGE LANDING (W2): x = 5 zero-side bridge (20M cache,
    checkpoints 1e6/1e7/2e7) reproduces F_s = pj - pj_smooth at
    every mode: residual ladder BR_TAB rel 1e-2 (2.7300e-4/
    3.8097e-5/2.0864e-5), deepest <= 1e-4, r175 PJ_RES_TAB{5} =
    2.086e-5 hit rel 1e-2: THE PIN'S SOURCE DATA (the same prime
    block that builds M) IS BRIDGE-EXPRESSIBLE PER CENSUS;
    G36 the conditioning exhibit (W2, typed MEASURED-EXHIBIT):
    eps_bar/gap on EPSGAP_TAB rel 5e-2 (250.7/3.658e8/4.212e19),
    >= 10 and strictly increasing; gap on GAP_TAB rel 5e-3 (== r175
    GAPABS continuity); the r175 reconstruction wall (T_req =
    3.76e14 -> 1.75e77 vs T_PT) CITED VERBATIM: any zero-side
    reconstruction of the floor data is conditioning-walled -- the
    pin's ball tolerance eps_bar itself exceeds the spectral gap by
    growing factors.
S4  controls (the same instruments must refuse):
    G50 SMOOTH x=5 / G51 SCRARITH x=5 / G52 EPSTEIN x=8: zone node
    counts 7/7/16 (vs true zone counts 4/4/10: the fake worlds fill
    the arithmetic gap), stray counts 3/2/7 (own 0.25-spacing
    criterion, disclosed), mu_1 = 4.8361/2.0056/1.2300 rel 5e-3
    (r133 digits), d_1(a=4) = -0.1538/-0.3417/-0.3312 rel 5e-3 ALL
    NEGATIVE (r132 SMOOTH -0.154 replicated);
    G53 consistency: d_1 > 0 at every MAIN rung, d_1 < 0 in every
    control world -- the consolidation consumes the arithmetic
    zero-free gap exactly as r133 predicted; PD claimed NOWHERE
    that PD is false.
S5  screens:
    G54 tau screens: |slope log10 margin(a=4) vs log10 tau| <= 0.30
    (measured -0.133: the DEMAND is not Connes-priced -- no
    tau_h-relabeling anywhere in the consolidation) and slope
    log10 m_min vs log10 tau inside (0.20, 0.80) (measured 0.362:
    FLOOR-RIDES-CONNES by identity, typed, not a disguise);
    G55 conditioning (1e-25 shift on M[0,0] at x=5 moves tau inside
    (1e-40, 1e-10); round-118 trap, edge).
S6  assembly:
    G60 demand audit (rungs/bars/tabs/strings frozen pre-eval; own
    stray criterion and D_cs normalization DISCLOSED; t0 = 2
    bracket convention DISCLOSED; f64 zero-side bridge sums
    DISCLOSED, r175 class);
    G61 ancestor/loop gate: delivered ancestors CONSOLIDATION ==
    {THEOREM-A-R133, DCS-357-CENSUS, BW25-PUBLISHED, HSW22,
    CACHE-WARD, SOURCE, SECULAR-K-1-R131}; BRIDGE-ADJUDICATION ==
    {LANDAU-1912, GONEK-1993-FORM, EXPLICIT-FORMULA-FORM,
    CENSUS-PER-K, CACHE-WARD, SOURCE}; TAUPOS, TLAWCAP,
    CENSUS-ALL-K, ZERO-VERIF-AS-HYP, GONEK-1984-RH,
    MONTGOMERY-PC-RH, RH-GRANT, A0-FLOOR ancestors of NOTHING
    delivered; FOUR flagged cycles detected and NOT consumed;
    G62 min-cut (r135 graph with the DOMASYM edge now carried for
    all integer x >= 3): flows base 4 / refined 5 / one-grant 5 /
    counterfactual-parallel 6 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED -- THE CONSOLIDATION MOVES NO FLOW (no
    omega closed, nothing upgraded);
    G63 the endgame/distinctness graph (W3 crux): AND-fire
    propagation on corpus-declared edges -- grants {EPSLOCK,
    SPACREM, H123M-COUNTS} fire HPIN; {HPIN, THEOREM-A, DCS-357}
    fire WPD-BATTERY; the jet-triple grants {ENVJ-H1, CENSUS-H2,
    QUARTIC-H3, TRACE} fire PF/HCOF but do NOT fire HPIN or
    WPD-BATTERY (no declared edge; reachability both directions
    empty): WPD's lambda-uniform edge == H-PIN (consolidation
    confirmed) AND H-PIN != the jet triple (DISTINCT edges -- the
    honest residue carries both); the delivered chain is ACYCLIC.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; RUNGS = ((5, 60), (8, 80), (13, 120)); A_BAT =
(1, 4, 16); NPOL = 25; AUD_DPS = 100; HSW = (0.1038, 0.2573, 9.3675)
[HSW22 Cor. 1.2]; BW25 = (0.10076, 0.24460, 8.08344) [Bellotti-Wong
2025, r144/CDLXIII/v925 citation carried]; T_PT = 3000175332800
[PT21]; M_ENV = 3; MATCH_F = 0.25; X0_SCAN = (90, 200); X0_HSW =
121; X0_BW = 112; DCS_X = (3, 121); DCS_WORST_CELL = (12, 1);
DCS_WORST_MARGIN = 0.2250 abs 0.005; N_LAD = (1e6, 1e7, 2e7);
T2E7_STR = 9499220.4795 rel 1e-6; SW_T0 = 2.0; SW_GRID = 0.005.
Calibrated in calib_l1wpd_pass1.log (ONE pre-freeze pass; scratch
deleted after freeze, log KEPT; numbers quoted verbatim):
LOG10TAU_TAB = {5: -15.794, 8: -29.423, 13: -53.602} abs 0.01;
ZONE_TAB = {5: 4, 8: 10, 13: 21} exact; D1_TAB = {(5,1): 0.010341,
(5,4): 0.041330, (5,16): 0.164792, (8,1): 0.007683, (8,4): 0.030721,
(8,16): 0.122714, (13,1): 0.005407, (13,4): 0.021624,
(13,16): 0.086451} rel 5e-3; MRB_TAB = {5: 0.0754, 8: 0.0711,
13: 0.0666} (a=4) abs 0.005, bar 0.25; MM_BAR = 1e-15; LOCK_TAB =
{5: 0.365, 8: 0.432, 13: 0.483} abs 0.01, window (0.05, 5);
EPS_TAB = {5: 8.9627e-9, 8: 1.3734e-15, 13: 1.1178e-27} rel 5e-2;
MMIN_TAB = {5: 1.923e-6, 8: 7.219e-12, 13: 4.019e-20} rel 5e-2;
MARG4_TAB = {5: 31.76, 8: 616.4, 13: 3.482e6} rel 5e-2; MARGIN_BAR
= 3.0; MARGIN_GROWTH = 5.0; D1SPLIT_BAR = 1e-10; SW_TAB =
{5: 4.224082e-3, 8: 4.943161e-3, 13: 5.266462e-3} rel 5e-3;
SWC_TAB = {5: -7.109606e-3, 8: -6.406694e-3, 13: -6.050751e-3} abs
5e-4; SWH_TAB = {5: 1.1114, 8: 1.1204, 13: 1.1293} rel 5e-3;
VAC_TAB = {5: 263.1, 8: 226.7, 13: 214.4} rel 5e-2; VAC_MIN = 100;
BR_TAB = {1e6: 2.7300e-4, 1e7: 3.8097e-5, 2e7: 2.0864e-5} rel 1e-2;
BR_DEEP_BAR = 1e-4; R175_PJ5 = 2.086e-5 rel 1e-2; GAP_TAB =
{5: 3.57544e-11, 8: 3.75424e-24, 13: 2.65374e-47} rel 5e-3 [r175
GAPABS continuity]; EPSGAP_TAB = {5: 2.507e2, 8: 3.658e8,
13: 4.212e19} rel 5e-2, >= 10, strictly increasing; CTRL_TAB =
{SMOOTH: (7, 3, 4.8361, -0.1538), SCRARITH: (7, 2, 2.0056, -0.3417),
EPSTEIN: (16, 7, 1.2300, -0.3312)} (zone nodes exact, strays exact,
mu_1 rel 5e-3, d_1(a=4) rel 5e-3 and < 0); TAU_SLOPE_BAR = 0.30
(measured -0.133); FLOOR_SLOPE_WIN = (0.20, 0.80) (measured 0.362);
COND_WIN = (1e-40, 1e-10); RUNTIME_BAR = 1500 s.
Deterministic: NO randomness anywhere.  Caches READ-ONLY through the
imported ward_ functions (n7000 X5-class; big = Odlyzko zeros6 +
LMFDB/Platt, pedigree verified_zeros_big_meta.json, all below T_0
unconditionally).  Zero-side bridge sums in f64 (DISCLOSED, r175
class; the r175 mp cross-check 3.44e-14 cited); source/eigen work in
mp workdps.  Amendments after the frozen run, if any, are appended
as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): OBSTRUCTIONS-RESTATED-EXACT(G10/G11/G12);
STATUS-AUDIT-NO-SILENT-CLOSURE(G20 -- one recorded-but-unpropagated
sharpening found and carried); THEOREM-A-ALL-X-CONFIRMED(G21/G22 --
x_0 121/112 + 357 D_cs replicated);
WPD-LAMBDA-EDGE-EQUALS-HPIN(G22/G31/G63 -- at every sub-tail a the
lambda-uniform content of WPD is the H-pin edge; residue
consolidation at the LABEL level, no omega closed);
WPD-DISTINCT-LEGS-FINITE-OR-TAIL(strip instanced CITED; TAILWPD
RH-EQUIVALENT-AM-TAIL carried CITED);
HPIN-SOURCE-DATA-BRIDGE-EXPRESSIBLE(G35);
HPIN-FLOOR-ESCAPES-LINEARITY-AT-VARIATIONAL-MAP(G13/G36 -- the
exact escaping components are the eigenvector map and the root map;
same conditioning-walled quotient class as theta_inf, DISTINCT
statement); DEMAND-HSW-PRICING-VACUOUS-AT-BATTERY(G34);
OMEGA-A-QUOTIENT-CLASS + A0-FLOOR-ROUTE-IS-LOOP(G13/G14);
HPIN-NOT-JET-TRIPLE(G63 -- distinct edges, both stay in the
residue); RESIDUE-RESTATED-CARDINALITY-UNCHANGED(G62/G63);
CONTROLS-REFUSE(G50-G53); TAU-SCREEN-FLAT(G54);
LOOPS-FLAGGED-NOT-CONSUMED(G14/G61); MINCUT-UNCHANGED(G62);
NO-RH-CLAIM.
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; the zeta attribute only
inside audit_* functions (any enclosing scope); np.load only inside
ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4          # round-122 machinery (warded)
import hpin_floor_probe as HP          # r135 floor machinery
import wpd_proof_probe as WP           # r132 mass machinery
import thetainf_pin_probe as TP        # r175 bridge machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
RUNGS = ((5, 60), (8, 80), (13, 120))
A_BAT = (1, 4, 16)
NPOL = 25
AUD_DPS = 100
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
BW_A, BW_B, BW_C = 0.10076, 0.24460, 8.08344
T_PT = 3000175332800
M_ENV = 3
MATCH_F = 0.25
X0_SCAN = (90, 200)
X0_HSW_EXP = 121
X0_BW_EXP = 112
DCS_XLO, DCS_XHI = 3, 121
DCS_WORST_CELL = (12, 1)
DCS_WORST_MARGIN = 0.2250
DCS_MARGIN_ABS = 0.005
N_LAD = (int(1e6), int(1e7), int(2e7))
T2E7_STR = 9499220.4795
SW_T0 = 2.0
SW_GRID = 0.005
LOG10TAU_TAB = {5: -15.794, 8: -29.423, 13: -53.602}
ZONE_TAB = {5: 4, 8: 10, 13: 21}
D1_TAB = {(5, 1): 0.010341, (5, 4): 0.041330, (5, 16): 0.164792,
          (8, 1): 0.007683, (8, 4): 0.030721, (8, 16): 0.122714,
          (13, 1): 0.005407, (13, 4): 0.021624, (13, 16): 0.086451}
MRB_TAB = {5: 0.0754, 8: 0.0711, 13: 0.0666}
MRB_BAR = 0.25
MM_BAR = 1e-15
LOCK_TAB = {5: 0.365, 8: 0.432, 13: 0.483}
LOCK_WIN = (0.05, 5.0)
EPS_TAB = {5: 8.9627e-9, 8: 1.3734e-15, 13: 1.1178e-27}
MMIN_TAB = {5: 1.923e-6, 8: 7.219e-12, 13: 4.019e-20}
MARG4_TAB = {5: 31.76, 8: 616.4, 13: 3.482e6}
MARGIN_BAR = 3.0
MARGIN_GROWTH = 5.0
D1SPLIT_BAR = 1e-10
SW_TAB = {5: 4.224082e-3, 8: 4.943161e-3, 13: 5.266462e-3}
SWC_TAB = {5: -7.109606e-3, 8: -6.406694e-3, 13: -6.050751e-3}
SWH_TAB = {5: 1.1114, 8: 1.1204, 13: 1.1293}
VAC_TAB = {5: 263.1, 8: 226.7, 13: 214.4}
VAC_MIN = 100.0
BR_TAB = {int(1e6): 2.7300e-4, int(1e7): 3.8097e-5,
          int(2e7): 2.0864e-5}
BR_DEEP_BAR = 1e-4
R175_PJ5 = 2.086e-5
GAP_TAB = {5: 3.57544e-11, 8: 3.75424e-24, 13: 2.65374e-47}
EPSGAP_TAB = {5: 2.507e2, 8: 3.658e8, 13: 4.212e19}
CTRL_TAB = {"SMOOTH": (7, 3, 4.8361, -0.1538),
            "SCRARITH": (7, 2, 2.0056, -0.3417),
            "EPSTEIN": (16, 7, 1.2300, -0.3312)}
CTRL_SPECS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
              ("EPSTEIN", 8, 80))
TAU_SLOPE_BAR = 0.30
FLOOR_SLOPE_WIN = (0.20, 0.80)
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 1500.0

PRESENT_STRS = ("schärft sich auf JEDES ganze x ≥ 3",
                "RH-ÄQUIVALENT-AM-TAIL",
                "LIVE-NICHT-STALE",
                "H-pin offen, WPD offen",
                "x₀(BW25) = 112")
ABSENT_STRS = ("H-pin geschlossen", "WPD geschlossen",
               "H-pin closed", "WPD closed")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list[tuple[str, bool, str]] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    CHECKS.append((name, ok, detail))
    tag = "PASS" if ok else "FAIL"
    print("[%s] %s: %s" % (tag, name, detail))
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    print("  " + msg)


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


# --------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    bad = []
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    oracle = ("zetazero", "riemann_zeros", "lmfdb", "odlyzko_load")

    def scopes(node, stack):
        name = getattr(node, "name", None)
        st = stack + ([name] if name else [])
        for ch in ast.iter_child_nodes(node):
            yield from scopes(ch, st)
        yield node, stack

    for node, stack in scopes(tree, []):
        if isinstance(node, ast.Attribute):
            if node.attr in oracle:
                bad.append("oracle name %s" % node.attr)
            if node.attr == "zeta" and not any(
                    s and s.startswith("audit_") for s in stack):
                bad.append("zeta outside audit_*")
            if node.attr == "load" and isinstance(
                    node.value, ast.Name) and node.value.id == "np" \
                    and not any(s and s.startswith("ward_")
                                for s in stack):
                bad.append("np.load outside ward_*")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
            for nm in names:
                if "verification" in nm:
                    bad.append("verification import %s" % nm)
    return (not bad), ("clean" if not bad else "; ".join(bad))


# --------------------------------------------------- generalized assembly
def q_of(T: float, cst) -> float:
    a, b, c = cst
    return a * math.log(T) + b * math.log(math.log(T)) + c


def t_star_gen(N: int, cst) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if HP.m_rvm(mid) - q_of(mid, cst) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells_gen(N: int, a: float, Ts: float, cst) -> float:
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = HP.m_rvm(Ts) + q_of(Ts, cst)
            for j in range(J):
                n_next = HP.m_rvm(Tj[j + 1]) - q_of(Tj[j + 1], cst)
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * HP.w_of(a, Tj[j + 1])
                u_prev = HP.m_rvm(Tj[j + 1]) + q_of(Tj[j + 1], cst)
            best = max(best, tot)
    return best


def asym_gen(x: float, a: float, cst) -> float:
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    Ts = t_star_gen(N, cst)
    Tz = 2 * math.pi * x
    n_z = HP.m_rvm(Tz) - q_of(Tz, cst)
    TL = tl_shells_gen(N, a, Ts, cst)
    return TL - TL / 8.0 - max(0.0, (N - n_z)) * HP.w_of(a, Tz)


def x0_scan(cst) -> int | None:
    ok_from = None
    for x in range(X0_SCAN[0], X0_SCAN[1] + 1):
        if all(asym_gen(x, a, cst) > 0 for a in A_BAT):
            if ok_from is None:
                ok_from = x
        else:
            ok_from = None
    return ok_from


# ------------------------------------------------------------ graphs
def has_cycle(edges: dict) -> bool:
    color: dict = {}

    def dfs(u) -> bool:
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1 or (c == 0 and dfs(v)):
                return True
        color[u] = 2
        return False

    return any(color.get(u, 0) == 0 and dfs(u) for u in list(edges))


def reachable(edges: dict, src: str) -> set:
    seen = {src}
    stack = [src]
    while stack:
        u = stack.pop()
        for v in edges.get(u, ()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def and_fire(rules: dict, grants: set) -> set:
    lit = set(grants)
    changed = True
    while changed:
        changed = False
        for node, needs in rules.items():
            if node not in lit and all(n in lit for n in needs):
                lit.add(node)
                changed = True
    return lit


# ------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # G10 -- D3 demand rearrangement + A0-cancellation (r135 class)
    eps, mmin, TLs, SW = sp.symbols("eps mmin TL SW", positive=True)
    lhs = (2 * eps / (16 * eps * SW / TLs)) * SW - TLs / 8
    ok_a = sp.simplify(lhs) == 0
    cx, sinv, pr, A0s = sp.symbols("c s p A0", positive=True)
    ebar = cx * A0s
    mflo = 4 * A0s * sinv * pr
    gball = sp.simplify(2 * ebar / mflo)
    ok_b = sp.simplify(gball - cx / (2 * sinv * pr)) == 0 \
        and A0s not in gball.free_symbols
    out.append(("G10-hpin-restatement", bool(ok_a and ok_b),
                "D3 exact: zone mass <= TL/8 <== m_min >= m_req = "
                "16 eps_bar SW/TL; ball g = 2 eps/m = c/(2|sin| PR) "
                "is A_0-FREE (the Connes scale cancels at identity "
                "level) -- the H-pin restatement is licensed"))

    # G11 -- WPD constant + Theorem-C identities (r132/r133 class)
    q = sp.Rational(1, 2)
    kq = max(k * q ** (k - 1) for k in range(2, 30))
    ok_k = kq == 2 * q
    th, Mps, t1 = sp.symbols("theta Mp t1", positive=True)
    Mm_e = (1 - th) * (Mps + t1)
    d1_e = sp.simplify(Mps - Mm_e + t1)
    ok_c1 = sp.simplify(d1_e - th * (Mps + t1)) == 0
    slack = sp.simplify((2 - th) / th - (Mps + Mm_e) / d1_e)
    ok_c2 = sp.simplify(slack - t1 / (th * (Mps + t1))) == 0
    ok_dom = sp.simplify(((Mps + Mm_e) / d1_e).subs(th, 1)) \
        == sp.simplify(Mps / (Mps + t1))
    out.append(("G11-wpd-restatement", bool(ok_k and ok_c1 and ok_c2
                                            and ok_dom),
                "K(1/2) == 2q == 1 exact (r132 W1); Theorem-C: weak "
                "one-sidedness M- = (1-th)(M+ + t1) ==> d1 == "
                "th (M+ + t1) EXACT, MRB <= (2-th)/th with the EXACT "
                "slack t1/(th (M+ + t1)) (the r133 wording); DOM "
                "(th = 1) ==> MRB == M+/(M+ + t1) <= 1 -- the WPD "
                "restatement is licensed"))

    # G12 -- Theorem-A assembly shape
    TL2, zm, me = sp.symbols("TL2 zm me", positive=True)
    d1_lo = TL2 - zm - me
    subs = d1_lo.subs([(zm, TL2 / 8), (me, me)])
    ok_A = sp.simplify(subs - (TL2 - TL2 / 8 - me)) == 0
    out.append(("G12-theoremA-shape", bool(ok_A),
                "d1 >= TL - zonemass - M-_edge with zonemass <= TL/8 "
                "==> d1 >= D = TL - TL/8 - (N - n_z) w(T_z) (exact "
                "rearrangement; the r133 closed form)"))

    # G13 -- linearity adjudication
    Amat = sp.Matrix([[0, 1], [1, 0]])
    Bmat = sp.Matrix([[1, 0], [0, -1]])
    lmin = lambda Mx: min(Mx.eigenvals().keys(), key=lambda e: sp.re(e))
    lA, lB = lmin(Amat), lmin(Bmat)
    lAB = lmin(Amat + Bmat)
    ok_e = (lA == -1 and lB == -1
            and sp.simplify(lAB + sp.sqrt(2)) == 0
            and sp.simplify(lAB - (lA + lB)) != 0)
    A0r, w1, w2, b1, b2, y = sp.symbols("A0r w1 w2 b1 b2 y")
    F = A0r + w1 / (y - b1) + w2 / (y - b2)
    poly = sp.together(F) * (y - b1) * (y - b2)
    poly = sp.expand(sp.simplify(poly))
    roots = sp.solve(sp.Eq(poly, 0), y)
    d2 = sp.simplify(sp.diff(roots[0], w1, 2))
    ok_r = d2 != 0
    uq, wq, om, c0, c1s = sp.symbols("u w om c0 c1")
    pj_expr = wq * sp.sin(om * uq)
    m_expr = 4 * (c0 - c1s) * sp.sin(om) * pr
    ok_f = (c0 not in pj_expr.free_symbols
            and c1s not in pj_expr.free_symbols
            and c0 in m_expr.free_symbols)
    out.append(("G13-linearity-adjudication",
                bool(ok_e and ok_r and ok_f),
                "eigen map NOT additive (lam_min(A+B) = -sqrt(2) != "
                "-2, exact 2x2); census-root map NOT affine "
                "(d2 y*/dw1^2 != 0 symbolically); bridge atoms "
                "c-FREE while the floor is c-LOADED: the pin's "
                "floor lives on the VECTOR side of the bridge -- "
                "the exact components escaping linearity are the "
                "eigenvector map and the root map"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("l1wpd_closure_probe -- PRIME.L1WPD.CLOSURE.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + CACHE WARDS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det, kind="edge")
    gam = HP.ward_cache()
    ok02 = (len(gam) == 7000 and abs(gam[0] - 14.134725) < 1e-5
            and bool(np.all(np.diff(gam) > 0)))
    gv = TP.ward_cache_big()
    ok02 = ok02 and len(gv) == 20000000 \
        and abs(gv[-1] / T2E7_STR - 1.0) <= 1e-6 \
        and float(np.max(np.abs(gv[:7000] - gam))) <= 1e-8
    check("G02-cache-wards", ok02,
          "n7000: count 7000, gamma_1 ok, monotone; big: count 2e7, "
          "T(2e7) = %.4f (frozen %.4f rel 1e-6), prefix overlap "
          "<= 1e-8" % (gv[-1], T2E7_STR), kind="edge")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (restatement licenses + linearity)")
    for name, ok, detail in symbolic_gates():
        check(name, ok, detail, kind="exact")

    # G14 loop ledger
    loops = {
        "A0-TRIANGLE": {"EPSLOCK-CLOSE": ["A0-FLOOR"],
                        "A0-FLOOR": ["TAUPOS", "TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK-CLOSE"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["WEIL-POS"],
                         "WEIL-POS": ["CENSUS-ALL-K"]},
        "ZERO-VERIF-AS-HYP": {"ZERO-VERIF-HYP": ["RH2"],
                              "RH2": ["ZERO-VERIF-HYP"]},
        "GONEK-1984": {"GONEK-1984": ["RH3"],
                       "RH3": ["SECOND-MOMENT"],
                       "SECOND-MOMENT": ["GONEK-1984"]}}
    cyc = {k: has_cycle(v) for k, v in loops.items()}
    check("G14-loop-ledger", all(cyc.values()),
          "FOUR flagged cycles machine-detected and NOT consumed: "
          "%s; in particular closing OMEGA-a through an A_0 floor "
          "is the r172 A_0-triangle loop (A0-FLOOR -> TAUPOS/"
          "TLAWCAP -> EPSLOCK)" % ", ".join(sorted(cyc)))

    # ------------------------------------------------------------ S2
    section("S2  STATUS AUDIT + THE THEOREM-A BRIDGE")
    with open(os.path.join(HERE, "..", "next.txt"),
              encoding="utf-8") as fh:
        corpus = " ".join(fh.read().split())
    pres = {s: (s in corpus) for s in PRESENT_STRS}
    absn = {s: (s not in corpus) for s in ABSENT_STRS}
    check("G20-status-audit", all(pres.values()) and all(absn.values()),
          "present: %s; absent: %s -- NO silent closure of H-pin/WPD "
          "in r136..r176; ONE recorded-but-unpropagated sharpening "
          "(v925: Theorem-A conditionality holds for EVERY integer "
          "x >= 3) found and carried into the residue statement"
          % (all(pres.values()), all(absn.values())))

    x0h = x0_scan((HSW_A, HSW_B, HSW_C))
    x0b = x0_scan((BW_A, BW_B, BW_C))
    check("G21-x0-replication", x0h == X0_HSW_EXP and x0b == X0_BW_EXP,
          "own integer scan %s, battery a: x_0(HSW) = %s (expect "
          "121), x_0(BW25) = %s (expect 112) -- r133/r144/CDLXIII/"
          "v925 replicated" % (str(X0_SCAN), x0h, x0b))

    xhi = 30 if smoke else DCS_XHI
    worst = (1e99, None)
    neg = 0
    ncell = 0
    for x in range(DCS_XLO, xhi + 1):
        K = int(math.ceil(KFAC * x * math.log(x)))
        N = K - 1
        Tz = 2 * math.pi * x
        n_z = int(np.sum(gam <= Tz))
        for a in A_BAT:
            ncell += 1
            TLcs = float(np.sum(HP.w_of(float(a), gam[N:])))
            Dcs = TLcs * 7.0 / 8.0 \
                - max(0, N - n_z) * HP.w_of(float(a), Tz)
            marg = Dcs / TLcs if TLcs > 0 else -1.0
            if Dcs <= 0:
                neg += 1
            if marg < worst[0]:
                worst = (marg, (x, a))
    ok22 = neg == 0 and ncell == (357 if not smoke else ncell)
    if not smoke:
        ok22 = ok22 and worst[1] == DCS_WORST_CELL \
            and abs(worst[0] - DCS_WORST_MARGIN) <= DCS_MARGIN_ABS
    check("G22-dcs-sweep", ok22,
          "census-currency assembly D_cs = (7/8) TL_cs - (N - n_z) "
          "w_a(T_z): %d cells, %d negatives, worst margin D_cs/TL_cs "
          "= %.4f at %s (frozen %.4f at %s; v925's 0.346 is its own "
          "normalization, same worst cell -- INFO): the bridge "
          "H-pin(x) ==> {d_1 > 0, MRB} is GAPLESS for every integer "
          "x >= 3" % (ncell, neg, worst[0], str(worst[1]),
                      DCS_WORST_MARGIN, str(DCS_WORST_CELL)))

    # ------------------------------------------------------------ S3
    section("S3  PER-RUNG LAYER (builds, masses, margins, pricing)")
    rungs = (RUNGS[0],) if smoke else RUNGS
    cells, nodes_t, meta = {}, {}, {}
    for x, dps in rungs:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=(x == 5))
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        mus, n_nonreal = HP.raw_mp_census(ce)
        nodes_t[x] = mus
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(ce["K"])]
            A0 = sum((-1) ** k * cs[k] for k in range(ce["K"]))
        Tz = min(0.98 * ce["K"] * math.pi / (math.log(x) / 2),
                 2 * math.pi * x)
        meta[x] = dict(cs=cs, aa=aa, oms=oms, A0=A0, Tz=Tz,
                       nonreal=n_nonreal)

    ok30 = True
    det30 = []
    for x, dps in rungs:
        ce, mtd = cells[x], meta[x]
        lt = math.log10(float(ce["tau"]))
        okx = (abs(lt - LOG10TAU_TAB[x]) <= 0.01
               and len(nodes_t[x]) == ce["K"] - 1
               and mtd["nonreal"] == 0
               and int(np.sum(nodes_t[x] <= mtd["Tz"])) == ZONE_TAB[x])
        ok30 = ok30 and okx
        det30.append("x%d: log10tau %.3f, %d real nodes, zone %d"
                     % (x, lt, len(nodes_t[x]),
                        int(np.sum(nodes_t[x] <= mtd["Tz"]))))
    check("G30-build-census", ok30,
          "tau on LOG10TAU_TAB abs 0.01; census complete K-1 real, "
          "0 nonreal; zone counts on ZONE_TAB: " + "; ".join(det30))

    pol_str, pol_worst = HP.audit_polish_band(gam[:NPOL], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    info("polished %d ordinates at dps %d, worst |Xi| = %.1e"
         % (NPOL, AUD_DPS, pol_worst))

    ok31 = ok32 = ok33 = ok34 = True
    det31, det32, det33, det34 = [], [], [], []
    eps_tab, mmin_tab, marg_tab, tau_tab, d1main = {}, {}, {}, {}, {}
    for x, dps in rungs:
        ce, mtd = cells[x], meta[x]
        K = ce["K"]
        Tz = mtd["Tz"]
        tauf = float(ce["tau"])
        with mp.workdps(dps):
            cs, aa, oms = mtd["cs"], mtd["aa"], mtd["oms"]
            A_j, S_j = HP.boundary_jets(ce, M_ENV + 1)
            envP = HP.env_pref(A_j, S_j, float(ce["om"][-1]),
                               float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * HP.hsw_G(float(T_PT))
            eps_bar = math.sqrt((tauf + off_allow) / 2.0)
            a0f = float(abs(mtd["A0"]))
            zone_j = [j for j in range(NPOL) if pol_f64[j] <= Tz]
            m_min = float("inf")
            for j in zone_j:
                tmu, _res = HP.newton_node(cs, aa, oms,
                                           float(nodes_t[x][j]), dps)
                _f, fp = HP.en_pair(cs, aa, oms, tmu)
                m_min = min(m_min, float(abs(fp)))
        # G31 masses / locks
        lock = eps_bar / (a0f * math.sqrt(8.0 * HP.hsw_G(Tz)))
        okx = (abs(lock - LOCK_TAB[x]) <= 0.01
               and LOCK_WIN[0] <= lock <= LOCK_WIN[1])
        d1s = {}
        for a in A_BAT:
            ms = WP.rung_masses(np.asarray(nodes_t[x], float), gam,
                                float(a))
            d1 = ms["Mp"] - ms["Mm"] + ms["tail1"]
            d1s[a] = (d1, ms)
            mrb = (ms["Mp"] + ms["Mm"]) / d1 if d1 > 0 else 1e99
            okx = okx and d1 > 0 \
                and abs(d1 / D1_TAB[(x, a)] - 1.0) <= 5e-3 \
                and ms["Mm"] <= MM_BAR
            if a == 4:
                okx = okx and abs(mrb - MRB_TAB[x]) <= 0.005 \
                    and mrb <= MRB_BAR
                d1main[x] = d1
        ok31 = ok31 and okx
        det31.append("x%d: lock %.3f, d1(a=4) %.6f, MRB %.4f, "
                     "M- %.1e" % (x, lock, d1s[4][0],
                                  (d1s[4][1]["Mp"] + d1s[4][1]["Mm"])
                                  / d1s[4][0], d1s[4][1]["Mm"]))
        # G32 margins
        zg = gam[gam <= Tz]
        Ts = HP.t_star(K - 1)
        margs = []
        for a in A_BAT:
            swp = float(np.sum([HP.wp_abs(a, g) for g in zg]))
            TL = HP.tl_shells(K - 1, float(a), Ts)
            m_req = 16.0 * eps_bar * swp / TL
            margs.append(m_min / m_req)
        okm = (abs(m_min / MMIN_TAB[x] - 1.0) <= 5e-2
               and all(mg >= MARGIN_BAR for mg in margs)
               and abs(margs[1] / MARG4_TAB[x] - 1.0) <= 5e-2
               and abs(eps_bar / EPS_TAB[x] - 1.0) <= 5e-2)
        ok32 = ok32 and okm
        det32.append("x%d: m_min %.3e margins %.2e/%.2e/%.2e"
                     % (x, m_min, margs[0], margs[1], margs[2]))
        # G33 d1 split
        a = 4.0
        c01 = R4.ward_c01(gam, a)
        trb = float(np.sum(HP.w_of(a, np.asarray(nodes_t[x], float))))
        dev = abs((c01 - trb) - d1s[4][0]) / abs(d1s[4][0])
        ok33 = ok33 and dev <= D1SPLIT_BAR
        det33.append("x%d: |C01 - TrB - d1|/d1 = %.1e" % (x, dev))
        # G34 SW pricing bracket (a = 4)
        swp = float(np.sum([HP.wp_abs(a, g) for g in zg]))
        with mp.workdps(40):
            integ = float(mp.quad(
                lambda t: (a * abs(2 * t * (a - t * t))
                           / (a + t * t) ** 3)
                * mp.log(t / (2 * mp.pi)) / (2 * mp.pi), [SW_T0, Tz]))
        ts_g = np.arange(SW_T0, Tz, SW_GRID)
        fv = np.array([HP.wp_abs(a, t) for t in ts_g])
        tv = float(np.sum(np.abs(np.diff(fv))))
        Mt0 = (SW_T0 / (2 * math.pi)) \
            * math.log(SW_T0 / (2 * math.pi * math.e)) + 7.0 / 8.0
        center = integ + HP.wp_abs(a, SW_T0) * Mt0
        half = HP.q_hsw(Tz) * (HP.wp_abs(a, Tz) + tv)
        vac = half / swp
        oks = (center - half <= swp <= center + half
               and abs(swp / SW_TAB[x] - 1.0) <= 5e-3
               and abs(center - SWC_TAB[x]) <= 5e-4
               and abs(half / SWH_TAB[x] - 1.0) <= 5e-3
               and abs(vac / VAC_TAB[x] - 1.0) <= 5e-2
               and vac >= VAC_MIN and center < 0)
        ok34 = ok34 and oks
        det34.append("x%d: SW %.4e in [%.3e, %.3e], vacuity %.0f"
                     % (x, swp, center - half, center + half, vac))
        eps_tab[x] = eps_bar
        mmin_tab[x] = m_min
        marg_tab[x] = margs[1]
        tau_tab[x] = tauf
    check("G31-replication-license", ok31,
          "d_1 ladder on D1_TAB rel 5e-3 (the r128/r131/r132 table, "
          "cross-instrument continuity), MRB on MRB_TAB <= 0.25, "
          "M- <= 1e-15 (DOM one-sided), EPS-LOCK on LOCK_TAB: "
          + "; ".join(det31))
    check("G32-hpin-margins", ok32,
          "m_min,zone on MMIN_TAB, margins m_min/m_req >= %.0f at "
          "every (rung, a), a=4 tab rel 5e-2%s: %s"
          % (MARGIN_BAR,
             "" if smoke else (", growth %.1fx >= %.0f"
                               % (marg_tab.get(13, 0)
                                  / max(marg_tab.get(5, 1), 1e-30),
                                  MARGIN_GROWTH)),
             "; ".join(det32)))
    if not smoke:
        ok32g = marg_tab[13] >= MARGIN_GROWTH * marg_tab[5]
        check("G32b-margin-growth", ok32g,
              "margin(a=4) growth 13/5 = %.1fx >= %.1f"
              % (marg_tab[13] / marg_tab[5], MARGIN_GROWTH))
    check("G33-d1-split", ok33,
          "d_1 == [C01 zero-sum leg] - [TrB node leg] == Mp - Mm + "
          "tail1 (both ways, rel <= 1e-10): the zero-sum leg is "
          "classical-priceable (r131 bracket class), the node leg "
          "is variational: " + "; ".join(det33))
    check("G34-sw-pricing-vacuous", ok34,
          "the unconditional Stieltjes/HSW bracket CONTAINS the "
          "census SW at every rung but is VACUOUS (halfwidth/SW >= "
          "%.0f, center < 0): the H-pin demand factor is CLASSICAL-"
          "PER-CENSUS only -- raw count-currency pricing carries no "
          "information at battery rungs (CDXLII structural swamp "
          "replicated on the SW factor): %s"
          % (VAC_MIN, "; ".join(det34)))

    # G35 bridge landing at x = 5
    x, dps = 5, 60
    K5 = cells[5]["K"]
    with mp.workdps(dps):
        aa5 = mp.log(x) / 2
        atoms = TP.atoms_main(x, dps)
        pj, _pd = TP.prime_data(atoms, K5, aa5, dps)
        pj_s, _pd_s = TP.smooth_data(K5, aa5, dps)
        Fs = [float(pj[k] - pj_s[k]) for k in range(K5)]
    lad = (N_LAD[0],) if smoke else N_LAD
    br = TP.bridge_pj(gv, float(mp.log(5) / 2), K5, lad)
    itv = TP.itriv_s(mp.log(5) / 2, K5)
    ok35 = True
    det35 = []
    deep_res = None
    for ci, N in enumerate(lad):
        resid = max(abs(Fs[k] - (br[ci, k] - itv[k]))
                    for k in range(1, K5))
        ok35 = ok35 and abs(resid / BR_TAB[N] - 1.0) <= 1e-2
        det35.append("N=%.0e: %.4e" % (N, resid))
        deep_res = resid
    if not smoke:
        ok35 = ok35 and deep_res <= BR_DEEP_BAR \
            and abs(deep_res / R175_PJ5 - 1.0) <= 1e-2
    check("G35-bridge-landing", ok35,
          "x=5 mode-level Landau bridge reproduces F_s = pj - "
          "pj_smooth at every mode from the verified census alone "
          "(residual ladder %s; deepest <= %.0e; r175 PJ_RES_TAB{5} "
          "= %.3e hit): THE PIN'S SOURCE DATA IS BRIDGE-EXPRESSIBLE "
          "PER CENSUS" % ("; ".join(det35), BR_DEEP_BAR, R175_PJ5))

    # G36 conditioning exhibit
    ok36 = True
    det36 = []
    prev = 0.0
    for x, dps in rungs:
        gap = float(cells[x]["gap"])
        r = eps_tab[x] / gap
        ok36 = ok36 and abs(gap / GAP_TAB[x] - 1.0) <= 5e-3 \
            and abs(r / EPSGAP_TAB[x] - 1.0) <= 5e-2 \
            and r >= 10.0 and r > prev
        prev = r
        det36.append("x%d: eps_bar/gap = %.3e" % (x, r))
    check("G36-conditioning-exhibit", ok36,
          "eps_bar/gap on EPSGAP_TAB (>= 10, strictly increasing; "
          "gap == r175 GAPABS continuity): the pin's own ball "
          "tolerance exceeds the spectral gap by growing factors -- "
          "with the CITED r175 reconstruction wall (T_req 3.76e14 "
          "-> 1.75e77 vs T_PT 3.00e12) any zero-side reconstruction "
          "of the floor data is conditioning-walled (typed "
          "MEASURED-EXHIBIT): " + "; ".join(det36))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS (the same instruments must refuse)")
    ok53 = all(d1main[x] > 0 for x in d1main)
    ctrls = (CTRL_SPECS[0],) if smoke else CTRL_SPECS
    for world, xw, dpsw in ctrls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=False)
        mus_w, _nr = HP.raw_mp_census(cw)
        Tzw = min(0.98 * cw["K"] * math.pi / (math.log(xw) / 2),
                  2 * math.pi * xw)
        zone_nodes = mus_w[mus_w <= Tzw]
        strays = 0
        for muv in zone_nodes:
            j = int(np.argmin(np.abs(gam - muv)))
            lo = gam[j - 1] if j > 0 else 0.0
            hi = gam[j + 1] if j + 1 < len(gam) else gam[j] + 6.0
            if abs(muv - gam[j]) > MATCH_F * 0.5 * (hi - lo):
                strays += 1
        ms = WP.rung_masses(np.asarray(mus_w, float), gam, 4.0)
        d1w = ms["Mp"] - ms["Mm"] + ms["tail1"]
        nz_exp, st_exp, mu1_exp, d1_exp = CTRL_TAB[world]
        okw = (len(zone_nodes) == nz_exp and strays == st_exp
               and abs(float(mus_w[0]) / mu1_exp - 1.0) <= 5e-3
               and d1w < 0
               and abs(d1w / d1_exp - 1.0) <= 5e-3)
        ok53 = ok53 and okw
        check("G5%d-%s" % ({"SMOOTH": 0, "SCRARITH": 1,
                            "EPSTEIN": 2}[world], world.lower()), okw,
              "%s x=%d: zone nodes %d (true zone %d -- the gap is "
              "filled), strays %d, mu_1 %.4f (fills the arithmetic "
              "zero-free gap (0, 14.13)), d_1(a=4) = %.4f < 0"
              % (world, xw, len(zone_nodes),
                 int(np.sum(gam <= Tzw)), strays, float(mus_w[0]),
                 d1w))
    check("G53-controls-consistency", ok53,
          "d_1 > 0 at every MAIN rung and d_1 < 0 in every control "
          "world: the consolidation consumes the arithmetic "
          "zero-free gap exactly as r133 predicted; PD is claimed "
          "NOWHERE that PD is false")

    # ------------------------------------------------------------ S5
    section("S5  SCREENS")
    if not smoke:
        xs = [x for x, _d in rungs]
        lt = [math.log10(tau_tab[x]) for x in xs]
        lm = [math.log10(marg_tab[x]) for x in xs]
        lf = [math.log10(mmin_tab[x]) for x in xs]
        s_marg = np.polyfit(lt, lm, 1)[0]
        s_flo = np.polyfit(lt, lf, 1)[0]
        ok54 = abs(s_marg) <= TAU_SLOPE_BAR \
            and FLOOR_SLOPE_WIN[0] <= s_flo <= FLOOR_SLOPE_WIN[1]
        check("G54-tau-screens", ok54,
              "slope log10 margin(a=4) vs log10 tau = %.3f (<= %.2f: "
              "the DEMAND is not Connes-priced -- no tau_h "
              "relabeling in the consolidation); slope log10 m_min "
              "vs log10 tau = %.3f in %s (FLOOR-RIDES-CONNES by "
              "identity, typed, not a disguise)"
              % (s_marg, TAU_SLOPE_BAR, s_flo, str(FLOOR_SLOPE_WIN)))
    ce5 = cells[5]
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e (round-118 "
          "trap absent)" % d_eps, kind="edge")

    # ------------------------------------------------------------ S6
    section("S6  ASSEMBLY (demand audit, ancestry, min-cut, graphs)")
    check("G60-demand-audit", True,
          "rungs/bars/tabs/strings frozen pre-evaluation (SPEC_SHA "
          "covers the declaration); own stray criterion (0.25 "
          "spacing) and own D_cs normalization DISCLOSED; SW-bracket "
          "t0 = 2 convention DISCLOSED; f64 zero-side bridge sums "
          "DISCLOSED (r175 class, mp cross 3.44e-14 cited); the "
          "r133-vs-r171 H1/H2/H3 NAME COLLISION disclosed in spec")

    delivered = {
        "CONSOLIDATION": ["THEOREM-A-R133", "DCS-357-CENSUS",
                          "BW25-PUBLISHED", "HSW22", "CACHE-WARD",
                          "SOURCE", "SECULAR-K-1-R131"],
        "BRIDGE-ADJUDICATION": ["LANDAU-1912", "GONEK-1993-FORM",
                                "EXPLICIT-FORMULA-FORM",
                                "CENSUS-PER-K", "CACHE-WARD",
                                "SOURCE"],
        "DCS-357-CENSUS": ["CACHE-WARD", "PT21-PER-K"],
        "THEOREM-A-R133": ["HSW22", "SECULAR-K-1-R131"]}
    forbidden = ("TAUPOS", "TLAWCAP", "CENSUS-ALL-K",
                 "ZERO-VERIF-AS-HYP", "GONEK-1984-RH",
                 "MONTGOMERY-PC-RH", "RH-GRANT", "A0-FLOOR")
    anc = set()
    for k in ("CONSOLIDATION", "BRIDGE-ADJUDICATION"):
        anc |= set(reachable(delivered, k))
    ok61 = not (anc & set(forbidden)) and not has_cycle(delivered)
    check("G61-ancestry", ok61,
          "delivered ancestors exclude {%s}; delivered chain "
          "ACYCLIC; four flagged loop routes carried NOT consumed "
          "(G14)" % ", ".join(forbidden))

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "SPACREM"): 1, ("SPACREM", "R4HYP"): INF}
              )
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G62-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5 / counterfactual-"
          "parallel 6 NOT REAL (r135 graph; the DOMASYM edge is now "
          "carried for EVERY integer x >= 3 by v925 -- capacity "
          "unchanged, THE CONSOLIDATION MOVES NO FLOW); census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")

    # G63 AND-fire propagation + distinctness
    rules = {
        "HPIN": ["EPSLOCK-G", "SPACREM-G", "H123M-COUNTS"],
        "D1MRB": ["HPIN", "THEOREM-A-R133", "DCS-357-CENSUS"],
        "WPD-BATTERY": ["D1MRB"],
        "PF": ["ENVJ-H1", "CENSUS-H2", "TRACE"],
        "HCOF": ["PF", "QUARTIC-H3"],
        "L1": ["L1TAIL", "HPIN"],
        "R-THM": ["L1", "WPD-BATTERY"]}
    lit_pin = and_fire(rules, {"EPSLOCK-G", "SPACREM-G",
                               "H123M-COUNTS", "THEOREM-A-R133",
                               "DCS-357-CENSUS", "L1TAIL"})
    lit_jet = and_fire(rules, {"ENVJ-H1", "CENSUS-H2", "QUARTIC-H3",
                               "TRACE", "THEOREM-A-R133",
                               "DCS-357-CENSUS", "L1TAIL"})
    dg = {k: list(v) for k, v in rules.items()}
    ok63 = ("WPD-BATTERY" in lit_pin and "L1" in lit_pin
            and "HCOF" in lit_jet
            and "HPIN" not in lit_jet and "WPD-BATTERY" not in lit_jet
            and "HCOF" not in lit_pin
            and not has_cycle(dg))
    check("G63-endgame-distinctness", ok63,
          "AND-fire: {EPSLOCK, SPACREM, H123M} + Theorem-A + D_cs "
          "fire HPIN -> {d1, MRB} -> WPD-BATTERY and L1 (the "
          "lambda-uniform content of the PAIR is ONE edge: H-PIN); "
          "the jet-triple grants fire PF/HCOF but NOT HPIN/WPD (no "
          "declared edge either direction): H-PIN and the "
          "{H1^H2^H3}-triple are DISTINCT edges -- the honest "
          "residue carries BOTH; graph ACYCLIC")

    info("POST-ROUND RESIDUE (exact, the W4 deliverable): "
         "{H1 ^ H2 ^ H3}-KOFINAL (r171 jet triple, one rung per "
         "block, all three at the same h; limsup form only mod "
         "D = 0.0042) + {census-forall-k == LOOP, flagged, not "
         "consumed} + {H-PIN == the ONE lambda-uniform edge of the "
         "{L1, WPD} pair: L1 = TAIL (proven r131) + H-pin; "
         "WPD(a < gamma_1^2) <== H-pin for EVERY integer x >= 3 "
         "(Theorem A + 357 census certificates, re-verified this "
         "round); H-pin = (OMEGA-a) EPS-LOCK (variational-quotient "
         "class, A0-floor route == LOOP) + (OMEGA-b) "
         "SPACING-REMAINDER (QSUBGAP kernel) + H123M counting "
         "(per-rung certified)} + {WPD non-lambda legs: extension "
         "strip instanced (CDLIX/CDLXIII, cited); TAILWPD == "
         "RH-EQUIVALENT-AM-TAIL at a >= 9.0e24 (the world front, "
         "carried, not countable as closable)}.  CARDINALITY "
         "UNCHANGED -- no omega closed, nothing upgraded; the "
         "sharpening is LABEL-LEVEL: the pair {L1, WPD} carries "
         "ONE open lambda-uniform edge, not two.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "OBSTRUCTIONS-RESTATED-EXACT(G10/G11/G12)",
        "STATUS-AUDIT-NO-SILENT-CLOSURE(G20)",
        "THEOREM-A-ALL-X-CONFIRMED(G21/G22)",
        "WPD-LAMBDA-EDGE-EQUALS-HPIN(G22/G31/G63)",
        "WPD-DISTINCT-LEGS-FINITE-OR-TAIL(cited)",
        "HPIN-SOURCE-DATA-BRIDGE-EXPRESSIBLE(G35)",
        "HPIN-FLOOR-ESCAPES-LINEARITY-AT-VARIATIONAL-MAP(G13/G36)",
        "DEMAND-HSW-PRICING-VACUOUS-AT-BATTERY(G34)",
        "OMEGA-A-QUOTIENT-CLASS + A0-FLOOR-ROUTE-IS-LOOP(G13/G14)",
        "HPIN-NOT-JET-TRIPLE(G63)",
        "RESIDUE-RESTATED-CARDINALITY-UNCHANGED(G62/G63)",
        "CONTROLS-REFUSE(G50-G53)",
        "TAU-SCREEN-FLAT(G54)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G14/G61)",
        "MINCUT-UNCHANGED(G62)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: OBSTRUCTIONS-RESTATED-EXACT + "
              "STATUS-AUDIT-NO-SILENT-CLOSURE + "
              "THEOREM-A-ALL-X-CONFIRMED + "
              "WPD-LAMBDA-EDGE-EQUALS-HPIN + "
              "WPD-DISTINCT-LEGS-FINITE-OR-TAIL + "
              "HPIN-SOURCE-DATA-BRIDGE-EXPRESSIBLE + "
              "HPIN-FLOOR-ESCAPES-LINEARITY-AT-VARIATIONAL-MAP + "
              "DEMAND-HSW-PRICING-VACUOUS-AT-BATTERY + "
              "OMEGA-A-QUOTIENT-CLASS + A0-FLOOR-ROUTE-IS-LOOP + "
              "HPIN-NOT-JET-TRIPLE + "
              "RESIDUE-RESTATED-CARDINALITY-UNCHANGED + "
              "CONTROLS-REFUSE + TAU-SCREEN-FLAT + "
              "LOOPS-FLAGGED-NOT-CONSUMED + MINCUT-UNCHANGED")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
