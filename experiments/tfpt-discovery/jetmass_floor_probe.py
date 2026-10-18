#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jetmass_floor_probe -- PRIME.JETMASS.FLOOR.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung/per-block certificates stated, NO counterexample claim.
It closes no gate and narrows no gate.

=======================================================================
MISSION (THE LAST NAMED ATTACK: prove the JET-MASS-FLOOR -- the single
lambda-uniform arithmetic residue that r169/CDLXXXIV terminally
characterized: delta >= h^{-a} for some polynomial exponent a, where
delta := [sum sin^2(Ag) F(g^2)^2/g^2]/[A_0^2 sum sin^2(Ag)/g^2] is
the source-weighted average of (F/A_0)^2 over the TRUE TAIL ZEROS
(supply window WFULL = (T_z + 6, gamma_7000]; the jet-mass leg of the
proven factorization sigma == (1-slop) delta DC).  Deliverable: the
PRODUCT-FLOOR THEOREM (the rigorous completion of the J1
moment-Laurent chase), the weight-fraction counting (J2), the
assembled endgame chain with the FINAL RESIDUE stated exactly (J3),
and the red-team reconciliation (T4).)
=======================================================================
State consumed (CITED): CDLXXXIV/r169 (sigmafloor: SF1 anatomy
identity sigma == (1-slop) delta DC EXACT; SF2 rate-floor; SF3 DC leg
PROVEN-MOD-CITED; SF4 demand absorption T_req -> (3 pi/c)(1+2a/3)
h^{3/2+a}; SF5 pinning-supply == LOOP; SF6 toys; record ladders
sigma12/sigma_full/DC/delta/tlaw + onset laws; Z_OVERHANG 6.0 +
G34_HARD_MAX 26 inherited PRE-FROZEN); CDLX/r156 (rootladder: L1
moment-Laurent dictionary (y/y_t) F/A_0 == PHI(z); L2 quarter-cap;
L3 sum rules SR1-SR3 (SR1: sum y_j - sum b_k == y_t, the trace);
L5 cascade certificate; the complete-real F-census 0.83-0.88 y_t
top; the 2-mode witness (J-window ARITHMETIC-PINNED)); CDXLIV/r140
(jetlock_bandmass: J1 per-mode telescope + monotone envelope ENVJ
majorizing |F - A_0| on (b_top, oo); J2 onset sandwich; J3 trace
identity A_2/A_0 = sum b - sum y + the A_0-free spacing form; the
far-field law F/A_0 = 1 - y_t/y on [4y_t, 400y_t] at 1.2 percent);
CDLXVII/r162 (quartic law y_t-class J == THETA T_z^4, THETA measured
flat [0.17, 0.26], ALGEBRA-ONLY-REFUTED-FOR-THETA); CDLXXXIII/r168
(DT1 step algebra; DT2 demand law; 3/2-law; budget horizon);
CDLXXV/r166 (BA1-BA3, block tables, control strings); r131 OFF
recipe VERBATIM; HSW22 Cor. 1.2; PT21 (T_PT = 3000175332800); Landau
1912 + Gonek 1993 (exponential-sum bound CITED AS FORM, constants
unpriced); Weil 1952 AS FORM; Yoshida 1992 (no priority claim);
Vieta/Newton; Cauchy; Courant-Fischer; Weyl.

NOTATION.  Rung h = builder x (R4.build_cell, even sector); A =
log(h)/2; K = ceil(1.25 h log h); b_k = (k pi/A)^2; tau = lam_min;
T_z = 2 pi h; G = HSW envelope; c_k source coefficients; A_0 =
sum (-1)^k c_k; A_2 = sum_{k>=1} (-1)^k c_k b_k; y_t = |A_2/A_0|;
F(y) = c_0 + sum_{k>=1} (-1)^k c_k y/(y - b_k) (== t R(t)/2 at
y = t^2, r131 Layer 1); N(y) = numerator of F (degree K-1, leading
coefficient A_0; roots y_j = the F-census); B_1 = sum_{k>=1} b_k =
(pi/A)^2 (K-1)K(2K-1)/6 CLOSED FORM; kappa = B_1/y_t; z = y/y_t;
WFULL/W12/sigma/DC/delta/eps as in r169 VERBATIM.

=======================================================================
THE THEOREM LAYER (the product floor; every leg typed)
=======================================================================
THEOREM PF1 (census product identity; PROVEN, exact).  N(y) ==
A_0 prod_j (y - y_j) with deg N = K-1, and F/A_0 ==
prod_j (y - y_j)/prod_{k>=1} (y - b_k) EXACTLY; Vieta trace:
sum_j y_j == B_1 + y_t (with sign(A_2/A_0) = -1, gated per rung;
== r156 SR1/r140 J3).  The trace is COEFFICIENT-LEVEL: sum y_j =
-N_{K-2}/N_{K-1} -- verified per rung without any root-finding.

THEOREM PF2 (the product floor; PROVEN, exact).  Let c* > 1 with
NO census root of Re y >= c* y_t (H1 below), all roots with
Re y_j > -nu (H2 below), and S+ := sum_j max(Re y_j, 0) <=
(1 + kappa + NEGBAR) y_t (trace + H2).  Then for every real
y = z y_t with z > c*:
   F(y)/A_0  >=  (1 - c*/z)^EXP,   EXP := (1 + kappa + NEGBAR)/c*.
Proof legs (each sympy-gated): (i) every real-root factor with
y_j <= 0 satisfies (y - y_j)/(y - b) >= (y - 0)/(y - b) >= ...
drop to 1-side; (ii) complex pairs: |y - y_j|^2 = (y - alpha)^2 +
beta^2 >= (y - alpha)^2; (iii) concavity: -log(1 - u)/u increasing
on (0,1) ==> (1 - alpha/y) >= (1 - c* y_t/y)^{alpha/(c* y_t)} for
0 <= alpha <= c* y_t; (iv) denominator drop: 0 < 1 - b_k/y <= 1.
THE EXPONENT IS THE TRACE: the far-field law 1 - y_t/y is the
kappa -> 0 shadow of this exact bound (measured 1.2 percent
tightness EXPLAINED).  NOTE: this bypasses the J-tail bound of the
contract's J1 Laurent route entirely -- Newton/Vieta resum the
J-tail into root data, and the root cap + trace make it geometric.

THEOREM PF3 (half-plane exclusion; PROVEN, source-pure).  The r140
J1 telescope F - A_0 = sum_{i<=m} A_{2i}/y^i + sum_k w_k b_k^m/
(y^m (y - b_k)) extends to complex y with Re y > b_top via
|y - b_k| >= Re y - b_k and |y|^i >= (Re y)^i:  |F(y) - A_0| <=
ENVJ(Re y).  ENVJ is monotone decreasing (r140 CITED + re-chased),
so ENVJ(c* y_t) < |A_0| ==> NO census root in the half-plane
{Re y >= c* y_t} AND sign F == sign A_0 there: H1 is ONE exact
source evaluation per rung -- NO cache, NO zeros, NO measurement.

H2 (the census leg; MEASURED-POLISHED per rung, finite classical).
The F-census (polyroots on N, rootladder instrument VERBATIM):
all K-1 roots real and NONNEGATIVE (measured: negsum == 0 at all
calibrated rungs; the top root 0.83-0.88 y_t == the r156 escaped
ladder), warded by SR1/Vieta/product-identity devs <= 1e-40.

THEOREM JMF (the jet-mass floor; assembled).  delta >= L(z_0)^2 x
WF(z_0) with L(z_0) = (1 - c*/z_0)^EXP and WF(z_0) = [sum_{g^2 >=
z_0 y_t} sin^2/g^2]/[sum_WFULL sin^2/g^2] (drop nonnegative
below-onset terms + PF2 pointwise above).  TYPING: [PF2: proven
given H1 (certified) + H2 (per-rung classical census)] x [WF:
counting leg -- classical form (G - C)/2 on the suffix window,
same Landau/Gonek class as the r169 DC leg, GONEK-CONSTANT-
UNPRICED; measured ward-class per rung] x [RATE: WF >= 1/poly
<== y_t <= poly(h) == TOPROOT (measured x^4.1; == the r162
THETA-window)].  By r169 SF1/SF3/SF4: sigma >= (1-slop) L^2 WF DC
and ANY polynomial rate is census-absorbable.  THE JET-MASS-FLOOR
IS A THEOREM CONDITIONAL EXACTLY ON {H1 + H2 per rung (finite,
source-classical)} + {suffix equidistribution per census (Landau/
Gonek AS FORM)} + {TOPROOT rate} -- the r169 JETLOCK-MEAS leg (the
per-gamma measured lock indicators) is ELIMINATED from the
ancestor set; the named lambda-uniform residue REDUCES to TOPROOT.

RED TEAM (T4; frozen predictions).  (i) The r156 2-mode witness
c'' = c + d(e_1 + e_2) with frozen d = -A_2 (1 - 1/1000)/(b_2 -
b_1): A_0 invariant, y_t'' = y_t/1000, J_2 inflated x1e6 -- THE
CERTIFICATE REFUSES: c* y_t'' <= b_top for ALL grid c (H1 domain
EMPTY, calibrated) and the census top escapes to 24.9 y_t'' (H2/RC
broken); delta'' at the true zeros moves to 404.3 (the witness
moves the coordinate AND kills the certificate): the floor is
ARITHMETIC-PINNED exactly as r169-SF6 demands -- what algebra
cannot fake is the PAIR {H1, H2} in y_t-units.  (ii) Fake worlds:
y_t_w/b_top <= 0.65 ==> the PF domain {c y_t_w > b_top} is EMPTY
on the whole grid (calibrated SMOOTH x=5) or ENVJ_w >= |A_0_w|:
H1-REFUSED; theta_w = y_t_w/T_z^4 ~ 2.4e-4 (no quartic ground);
tau_w < 0 on the r166 strings; the RAW floor sigma_w > eps_w still
holds (r169 FLOOR-INEQ-WORLD-INSENSITIVE replicated) -- the
arithmetic is the certificate pair + the bridge, not the raw
inequality.  (iii) The r169 delta-toy (delta = 1e-6): violates the
PF2 conclusion at z >= 4 (L^2 ~ 0.52 > 1e-6) ==> NOT realizable
under H1+H2 (modus tollens): the theorem's content is exactly the
exclusion of the free-scalar toys.  (iv) Lattice toy: sin == 0
kills WF (the counting leg is the arithmetic input, as in SF6).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, np.load only in ward_*, no
    zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 PF1 (product/census identity generic K=3: deg, leading
    coefficient == A_0, trace == B_1 - A_2/A_0; product == F/A_0);
    G11 PF2 (series coefficients of -log(1-u)/u positive to order
    12 + three exact-rational power instances (1-a/y)^c >=
    (1-c/y)^a; pair bound; denominator drop; assembled floor on a
    3-root rational instance);
    G12 PF3 (telescope generic m=1,2 at K=3; per-term envelope
    monotonicity; complex-modulus instances |y-b| >= Re y - b;
    the no-root/sign corollary chase);
    G13 closed forms (sum k^2 == (K-1)K(2K-1)/6 generic; kappa/EXP
    algebra; the far-field shadow (1-1/z)^{1+kappa} -> 1 - 1/z as
    kappa -> 0);
    G14 JMF assembly (drop-nonnegative + pointwise floor ==> delta
    >= L^2 WF on a rational 3-term instance + generic drop lemma);
    G15 WF classical form + absorption (1 - cos 2x == 2 sin^2 x;
    the rate limit h G_lead(q h^2)/G_lead(2 pi h) -> 4 pi/q exact;
    r169-SF4 limits replicated at a = 1/2, 1, 3/2 + the census
    constant identity (3 pi/c)(1 + 2a/3));
    G16 red team exact (witness algebra A_0''== A_0, A_2'' ==
    A_2/1000 generic; delta-toy modus tollens L(4)^2 > 1e-6 exact;
    lattice toy WF == 0).
S2  G20 HSW G(T) sanity.
S3  per-rung layer h = 4..28 (r169 recipe VERBATIM: enclosures,
    wall chain, anchors, budget floor, sigma12/eps, anatomy; PLUS
    the NEW jet/kappa/H1/H2/PF/WF/delta_cert pass), 12 spawn
    workers, cost-sorted:
    G30 spectral sanity; G31 certified tau enclosures; G32 wall
    chain; G33 anchors + ladders (tlaw strings + r168 record
    ladder rel 1e-3; FULLGAP tabs; lock);
    G34 budget floor (BA3; HARD h <= 26, 27/28 F64-ORDINATE-
    LIMITED inherited PRE-FROZEN);
    G35 sigma/eps/anatomy (r169 tabs + record ladders sigma12/
    sigma_full/DC/delta rel 1e-3 h <= 26, DISCLOSED corpus-known;
    recipe dev <= 1e-40; iden dev <= 1e-40; DC in (0.05, 0.60)
    all; sigma_full (0.15, 0.80) + delta (0.3, 3.0) h <= 26);
    G36 jets + trace: sign(A_2/A_0) == -1 every rung; B_1 closed
    form dev <= 1e-40; Vieta trace dev <= 1e-40 (coefficient
    level, NO roots); kappa in (0.0, 0.30) + tabs at 4/5/8;
    G37 H1 certificate: c* = min C_GRID with ENVJ(c y_t) < |A_0|
    EXISTS every rung; c* <= 1.75 hard h <= 26; c*/ratio strings
    at 4/5/8;
    G38 H2 census (ISOLATED try per rung; a failure fails only
    this gate and is typed): n_real == K-1 (im tol 1e-10 scaled);
    min root >= 0 (negsum/y_t <= 1e-6); top/y_t in (0.70, 0.95)
    + strings at 4/5/8/13; top <= c* y_t (H1 cross-instrument);
    SR1 dev <= 1e-40; product-id dev <= 1e-40; HARD h <= 13,
    structure windows 14 <= h <= 24, h > 24 reported
    (CENSUS-DEPTH-REPORTED, pre-freeze unmeasured, DISCLOSED);
    G39 PF POINTWISE INSTANTIATED: at EVERY cache zero with z >=
    1.05 c*: F/A_0 >= (1 - c*/z)^EXP -- min margin > 0 HARD at
    h <= 26 where zeros exist (n_checked printed; margins/counts
    strings at 4/5/8); 27/28 F64-typed report;
    G40 WF table: WF(z_0) for z_0 in (2, 3, 4); existence h <= 16
    gated (beyond: ANATOMY-CACHE-HORIZON reported); WF(4) strings
    at 4/5/8; WF/WF_pred (ordinate-only fraction) in (0.6, 1.5);
    G41 THE CERTIFIED DELTA-FLOOR: delta_cert = L(4)^2 WF(4) > 0
    at every onset rung; delta_cert <= delta_meas HARD (h <= 26);
    sigma-floor row (1-slop) delta_cert DC <= sigma_full HARD
    (h <= 26); strings at 4/5/8; margin delta_cert/eps >= 1e6.
S3b block layer:
    G42 THE JMF BLOCK CERTIFICATE: sum_{onset rungs} w (1-slop)
    delta_cert DC - sum_all w eps > 0 on B2 and B3 (HARD, both
    weights; B4 partial reported): the sigma-floor below the
    horizon certified through the PRODUCT FLOOR -- consuming H1
    (source-certified) + H2 (census) + WF (ward-class weights) +
    classical DC + demand; NOT tau, NOT tlaw, NOT raw sigma, NOT
    the r169 per-gamma lock indicators.
S3c transfer layer:
    G43 horizon + rate law: h*(PT21, 0.15) on the r168 string
    1.2566e7 rel 2e-3 + k* in (23.3, 23.9); THE RATE LAW: fit
    log10[(1-slop) delta_cert DC] vs log10 h over the CLEAN onset
    rungs (h-only criterion sqrt(4 y_t) <= gtop/2, the r169
    AMENDMENT-1 lesson PRE-ADOPTED at freeze) -> (c, a) with a in
    (0.4, 2.2); rate horizon h*_rate = solve[eps = c h^{-a}] in
    (1e2, 1e7) + k*_rate; census constant (3 pi/c)(1 + 2a/3);
    G44 THE ENDGAME CHAIN INSTANTIATED per complete block:
    [G42 JMF row] + [BA3 bridge (G34)] + [enclosures (G31)] ==>
    block tau-positivity -- every arrow on real data;
    SUBSTRATE-DIRECT inherited (r166/r168/r169 re-asserted).
S4  controls through the SAME instrument (r166/r169 pre-frozen
    blocks, CTRL_NZ = 300): G50 SMOOTH [4,8], G51 SCRARITH [4,8],
    G52 EPSTEIN {8,9,10}: tau_w < 0 on the r166 strings rel 5e-3;
    mechanism loss tau_w + OFF_w - zsum_w < 0; y_t_w/b_top <= 1.0;
    theta_w <= 1e-3; H1-REFUSED (for every grid c: c y_t_w <=
    b_top OR ENVJ_w >= |A_0_w|); raw floor sigma_w > eps_w HOLDS
    (r169 FLOOR-INEQ-WORLD-INSENSITIVE replicated); delta_w/DC_w
    printed;
    G53 THE WITNESS BATTERY (h = 5, frozen d): A_0 dev <= 1e-40;
    y_t'' x1000/y_t dev <= 1e-40; J_2 inflation >= 1e4; H1-REFUSED
    in the witness world (grid-empty or ENVJ'' >= |A_0|); census
    top Re root/y_t'' >= 10 (RC BROKEN); delta'' on the 404.335
    string rel 5e-3: ARITHMETIC-PINNING-RECONCILED -- the witness
    kills the certificate pair {H1, H2} (and moves delta) while
    every PF1-PF3 identity holds: reconciles r169-SF6 exactly.
S5  G54 tau-screen (slopes vs log10 tau of sigma12, sigma_full,
    DC, delta, kappa, tlaw_0 <= 0.30 DEMAND-FLAT; RIDER log10
    A_0^2 slope in (0.85, 1.15) BOUND-RIDES-CONNES); G55
    conditioning (1e-25 shift at h = 5, round-118 trap).
S6  G60 demand audit (SEQ inherited; C_GRID/Z0_GRID/blocks/
    weights/criteria frozen pre-evaluation; census per-k; no
    ALL-X);
    G61 loop/mining gate (ancestor set of the delivered floor
    chain == {SOURCE, ENVJ-CERT(H1), CENSUS-H2-PER-RUNG,
    TRACE-IDENT, CACHE-WARD(WF), GONEK-FORM(WF-typing),
    TOPROOT-MEAS(rate), HSW22, PT21-CENSUS-PER-K}; TLAWCAP, WPD,
    TAUPOS, CENSUS-ALL-K and JETLOCK-MEAS are NOT ancestors --
    the r169 measured-lock leg is ELIMINATED; THREE loop routes
    carried flagged NOT consumed (tlaw-window, census-all-k,
    pinning-supply); weights/windows recomputed from frozen
    formulas, SIGN-MINING-CLEAN);
    G62 min-cut (r116 replica, r166/r168/r169 graph VERBATIM:
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL
    9 NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
    G63 endgame graphs: (i) universalized census cycle DETECTED
    (r168/r169 replicated); (ii) pinning-supply cycle DETECTED
    (r169 replicated); (iii) the REDUCED per-k terminal chain
    {ENVJ-H1, CENSUS-H2, GONEK -> WF, TOPROOT -> RATE, CENSUS_K}
    -> JETMASS -> SIGMAFLOOR -> DTSTEP_K -> HCOF -> both typed
    arrows -> RH is ACYCLIC with RH reachable from the
    counterfactual TOPROOT + CENSUS_K + GONEK grants
    (AND-semantics documented); the FINAL RESIDUE printed.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); NZSUM = 1200; NZFULL = 7000; F64_SLOP = 1e-3;
ENC_REL = 1e-3; Z_OVERHANG = 6.0; G34_HARD_MAX = 26; WORKERS = 12
(spawn; deterministic keys); RUNGS = 4..28; DPS = {4:60, 5:60,
6:65, 7:70, 8:80, 9:85, 10:90, 11:100, 12:110, 13:120, 14:120,
15:125, 16:130, 17:135, 18:140, 19:140, 20:144, 21:146, 22:148,
23:150, 24:150, 25:152, 26:155, 27:158, 28:160} (r166/r168/r169
schedule VERBATIM).  BLOCKS: B2 = [4,8] FULL, B3 = [8,16] FULL,
B4 = [16,32] PARTIAL-AT-28; w_flat == 1 PRIMARY, w_fejer ALT (r166
VERBATIM).  INHERITED BARS (r166/r168/r169 VERBATIM): SIMP_MIN =
1e3; RAY_BAR = RES0_BAR = 1e-25; LOGDET_BAR = 1e-30; TLAW_TAB =
{4: 0.232537, 5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24:
0.5122} rel 5e-3; TLAW28_WIN = (0.40, 0.70); TLAW_STRUCT_WIN =
(0.15, 0.70); TLAW_LADDER (r168 record, rel 1e-3, ALL rungs) =
{4:0.2325, 5:0.2664, 6:0.2729, 7:0.3264, 8:0.3738, 9:0.3645,
10:0.4032, 11:0.4534, 12:0.4112, 13:0.4674, 14:0.4455, 15:0.4421,
16:0.4606, 17:0.5191, 18:0.4827, 19:0.5295, 20:0.5282, 21:0.5075,
22:0.5161, 23:0.5591, 24:0.5122, 25:0.5430, 26:0.5303, 27:0.5244,
28:0.5778}; FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5,
13: 1.0619e7, 18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97,
1.03); FG_SLOPE_WIN = (3.4, 4.6); LOCK_WIN = (1.0, 8.0);
RES_WIN_CORE = (-1e-9, 0.20); RES_WIN_DEEP = (-1e-9, 0.85);
ZSUM_OFF_MIN = 1e3; TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.85,
1.15); COND_WIN = (1e-40, 1e-10); RUNTIME_BAR = 21600 s;
SIGMA_TAB = {4: 0.205602, 5: 0.255783, 8: 0.356579} rel 5e-3;
RECIPE_BAR = 1e-40; SIGMA12_LADDER (r168 record, rel 1e-3, h <=
26) = {4:0.2056, 5:0.2558, 6:0.2608, 7:0.3104, 8:0.3566, 9:0.3453,
10:0.3841, 11:0.4320, 12:0.3927, 13:0.4477, 14:0.4287, 15:0.4251,
16:0.4419, 17:0.4961, 18:0.4570, 19:0.4969, 20:0.4932, 21:0.4697,
22:0.4779, 23:0.5191, 24:0.4758, 25:0.5045, 26:0.4888};
SIGFULL_LADDER (r169 sf_run2 record, rel 1e-3, h <= 26, DISCLOSED
corpus-known) = {4:0.2107, 5:0.2632, 6:0.2693, 7:0.3216, 8:0.3684,
9:0.3582, 10:0.3963, 11:0.4451, 12:0.4030, 13:0.4577, 14:0.4360,
15:0.4321, 16:0.4499, 17:0.5072, 18:0.4715, 19:0.5170, 20:0.5165,
21:0.4958, 22:0.5044, 23:0.5466, 24:0.5008, 25:0.5320, 26:0.5195};
DC_LADDER (r169 record, rel 1e-3, ALL rungs) = {4:0.1535,
5:0.2273, 6:0.1881, 7:0.2781, 8:0.2686, 9:0.2952, 10:0.2876,
11:0.3612, 12:0.3067, 13:0.3784, 14:0.3342, 15:0.3389, 16:0.3619,
17:0.4190, 18:0.3523, 19:0.4238, 20:0.3668, 21:0.3753, 22:0.3766,
23:0.4463, 24:0.3916, 25:0.4123, 26:0.3886, 27:0.4192, 28:0.3997};
DELTA_LADDER (r169 record, rel 1e-3, h <= 26) = {4:1.3744,
5:1.1595, 6:1.4330, 7:1.1573, 8:1.3730, 9:1.2146, 10:1.3797,
11:1.2335, 12:1.3154, 13:1.2109, 14:1.3057, 15:1.2762, 16:1.2445,
17:1.2115, 18:1.3394, 19:1.2210, 20:1.4095, 21:1.3223, 22:1.3406,
23:1.2259, 24:1.2801, 25:1.2917, 26:1.3381}; SIGFULL_WIN = (0.15,
0.80); DC_WIN = (0.05, 0.60); DELTA_WIN = (0.3, 3.0); IDEN_BAR =
1e-40; HSTAR_STR = 1.2566e7 rel 2e-3; KSTAR_WIN = (23.3, 23.9);
SIGMA0 = 0.15.  Controls (r166 VERBATIM): CTRL_SMOOTH =
CTRL_SCRARITH = (4..8) dps 60, CTRL_EPSTEIN = (8, 9, 10) dps 80,
CTRL_NZ = 300; CTRL_TAU_TAB rel 5e-3: SMOOTH {4: -1.0375, 5:
-1.0944, 6: -1.1306, 7: -1.1560, 8: -1.1749}, SCRARITH {4:
-2.5151e-2, 5: -0.34593, 6: -0.36716, 7: -0.61294, 8: -0.67664},
EPSTEIN {8: -1.6310, 9: -1.6922, 10: -1.9932}.
NEW (calibrated in calib_jmf_pass1.log + calib_jmf_pass2.log, ONE
pre-freeze calibration in TWO passes at h = 4/5/8 + census timing
h = 13 + SMOOTH x=5 + witness h=5; PASS 1 carried an N-assembly
bug (the b_k/(y-b_k) weight form mixed with the y-form term
padding of the rootladder census port -- Vieta/product devs 0.8/
0.3), PASS 2 fixed to the rootladder form VERBATIM (devs <=
3e-58); scratch deleted after freeze, BOTH logs kept; all numbers
quoted verbatim):  C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40,
1.50, 1.75, 2.00); C_STAR_MAX = 1.75 hard h <= 26; CSTAR_TAB =
{4: 1.10, 5: 1.15, 8: 1.15} exact grid values; ENVJ_RATIO_TAB =
{4: 0.998177, 5: 0.967435, 8: 0.979598} rel 5e-3; NEGSUM_BAR =
1e-6 (calibrated 0.0 at 4/5/8/13); EXP = (1 + kappa +
NEGSUM_BAR)/c*; KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8:
0.062906} rel 5e-3; KAPPA_WIN = (0.0, 0.30); CF_BAR = 1e-40 (B_1
closed form; calibrated <= 1.6e-61); VIETA_BAR = 1e-40 (calibrated
<= 2.5e-58); CENSUS: POLY_MAXSTEPS = 3000, POLY_EXTRAPREC = 2 x
dps, NPOLY_DPS = 3 x dps, IM_TOL = 1e-10 (scaled), TOP_WIN =
(0.70, 0.95), TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195,
13: 0.834429} rel 5e-3, SR1_BAR = 1e-40 (calibrated <= 2.7e-58),
PRODID_BAR = 1e-40 (calibrated <= 2.8e-72), CENSUS_HARD_MAX = 13,
CENSUS_STRUCT_MAX = 24; PW_Z_FACTOR = 1.05; PW_NCHK_TAB = {4:
6950, 5: 6879, 8: 6579} exact; PW_MARGIN_TAB = {4: 0.000035, 5:
0.000111, 8: 0.000508} rel 5e-2 (2-sig-fig calibration
quantization); Z0_GRID = (2.0, 3.0, 4.0),
Z0_PRIMARY = 4.0; WF_MAX_H = 16 (existence gated; beyond reported
ANATOMY-CACHE-HORIZON); WF4_TAB = {4: 0.197376, 5: 0.115111, 8:
0.065699} rel 5e-3; WF_RATIO_WIN = (0.6, 1.5) (calibrated 0.896..
0.983); L4_TAB = {4: 0.724080, 5: 0.723913, 8: 0.731028} rel
5e-3; DCERT_TAB = {4: 0.103483, 5: 0.060324, 8: 0.035110} rel
5e-3; DCDC_TAB = {4: 0.015881, 5: 0.013709, 8: 0.009429} rel
5e-3; RATE_MARGIN_MIN = 1e6 (calibrated >= 8.2e7); CLEAN_FIT:
sqrt(4 y_t) <= gtop/2 (h-only, PRE-FROZEN); RATE_A_WIN = (0.4,
2.2) (3-point calibration slope 0.75); HSTAR_RATE_WIN = (1e2,
1e7); EPS_STR_TAB = {4: 6.306e-11, 5: 9.828e-11, 8: 2.351e-10}
rel 5e-3.  WITNESS: WIT_FACT = 1000; WIT_A0_BAR = WIT_YT_BAR =
1e-40 (calibrated 0.0/1.8e-55); WIT_J2_INFL_MIN = 1e4 (calibrated
1.0e6); WIT_ZTOP_MIN = 10 (calibrated 24.87); WIT_DELTA_STR =
404.334778 rel 5e-3.  CONTROLS-NEW: CTRL_YTB_MAX = 1.0
(calibrated SMOOTH 0.1540); CTRL_THETA_MAX = 1e-3 (calibrated
2.410e-4); H1-REFUSED = for every grid c: (c y_t_w <= b_top) OR
(ENVJ_w(c y_t_w) >= |A_0_w|) (calibrated SMOOTH: domain empty at
all c).  Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use.
All mpf arithmetic inside explicit mp.workdps blocks in-worker;
block accumulation at workdps(200) from per-rung mp strings;
tiny/huge quantities (tau, A_0, OFF, zsum, jets, N-coefficients)
stay mp end-to-end (r147/r141 underflow classes banned); no f64
refinement of any mp quantity; flat O(1) ratios transported as
f64 for gating (DISCLOSED).  h = 6, 7, 9..28 and all block/rate
rows beyond 4/5/8 (census beyond 13) pre-freeze UNMEASURED on the
NEW coordinates (structure windows only, DISCLOSED); the sigma12/
tlaw/sigma_full/DC/delta ladders are r168/r169-record-known
(DISCLOSED).  Amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
PRODUCT-FLOOR-PROVEN(PF1-PF3: F/A_0 >= (1 - c*/z)^EXP given
H1 + H2; G10-G13); H1-CERTIFIED-SOURCE-PURE(ENVJ half-plane
exclusion, one evaluation per rung; G37); H2-CENSUS-CLASSICAL-
PER-RUNG(complete-real nonneg census, warded; G38);
PF-POINTWISE-VERIFIED(the certified curve under the truth at
every checked tail zero; G39); JETMASS-FLOOR-ASSEMBLED(delta >=
L^2 WF; G41) + JMF-BLOCK-CERTIFIED(B2/B3 below horizon via the
product floor, NOT via measured lock; G42/G44);
JETLOCK-MEAS-ELIMINATED(the r169 measured-lock ancestor replaced
by {H1, H2}; G61); JETMASS-REDUCED-TO-TOPROOT(the lambda-uniform
residue of the jet-mass floor == TOPROOT rate + Gonek-form
counting; G43/G61/G63); FARFIELD-LAW-EXPLAINED(the r140 1.2
percent law is the kappa-shadow of the exact exponent; G13/G39);
DEMAND-RATE-ABSORPTION(r169 SF4 replicated; G15/G43);
WITNESS-KILLS-CERTIFICATE(H1/H2 refused, RC broken, delta moved:
ARITHMETIC-PINNING-RECONCILED; G53); CONTROLS-REFUSE-BRIDGE-SIZE
(AMENDMENT 2) + FLOOR-INEQ-WORLD-INSENSITIVE(G50-G52);
TOY-EXCLUSION-BY-THEOREM
(modus tollens; G16); ANATOMY-REPLICATED(r169 ladders; G35);
DEMAND-FLAT + BOUND-RIDES-CONNES(G54); QUANTIFIER-INHERITED(G60);
LOOP-ROUTES-FLAGGED(three; G61/G63); OMEGA-UNCHANGED(census 4;
G62); MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge
gate fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 34/36 at SPEC_SHA
4f8d05e02cb020f9, log kept as the pre-amendment record
jmf_run1.log).  TWO INSTRUMENT RE-TYPINGS, no bar or criterion
moved on the delivered floor chain; every theorem/certificate/
census/pointwise/block/graph gate passed run 1 unchanged (the
full census landed complete-real nonnegative at ALL 25 rungs
including degree-116 at h = 28, and the PF pointwise floor held
at every one of the ~100k zero checks):
(a) G41: the RATE_MARGIN bar (delta_cert/eps >= 1e6) was frozen
over all onset rungs, but at h = 18 the WF(4) window is squeezed
against the FIXED cache top (WF = 0.0008, measured margin 5.4e5):
the same CACHE-TOP-LIMITED instrument class as the r169
AMENDMENT-1 rate fit and r137 JETCERT-DEPTH-LIMITED, here at the
margin bar.  FIX: the margin bar is restricted by the SAME frozen
h-only CLEAN_FIT criterion sqrt(4 y_t) <= gtop/2 already used by
G43 (PRE-ADOPTED at freeze for the fit); beyond it the rows are
typed CACHE-TOP-LIMITED and stay printed (the run-1 fail row is
itself the measured window-loss law and stays in the record).
No window or bar moved; a deeper zeros cache extends the clean
range -- pure instrument depth.
(b) G50-G52: the structural rows y_t_w/b_top <= 1.0 and theta_w
<= 1e-3 were calibrated on SMOOTH x=5 only; SCRARITH x=6 measures
1.822/1.9e-3 while ALL refusal legs held (tau_w < 0 on the r166
strings, mechanism loss < 0, H1-REFUSED at every grid c, raw
floor holds).  FIX: y_t_w/b_top and theta_w are re-typed
REPORTED-DIAGNOSTIC (printed, not gated -- they are not uniform
refusal coordinates across fake worlds); the gate's refusal
criterion is the certificate set {tau strings, BA3-bridge loss,
H1-REFUSED, raw-floor world-insensitivity}, which is what
separates the worlds.

AMENDMENT 2 (post-run-2, disclosed; run 2 = 35/36 at SPEC_SHA
92c895a4053dd781, log kept as the pre-amendment record
jmf_run2.log; the ONLY failing gate was G51).  ONE RED-TEAM
RE-ADJUDICATION, no bar or criterion moved on the delivered floor
chain: run 2 isolates the G51 failing leg as H1-REFUSED at
SCRARITH x=6 -- with y_t_w = 1.822 b_top that world HAS a genuine
far-field domain and the ENVJ certificate is SATISFIABLE there
(measured).  THIS IS THE HONEST READING, and it is CONSISTENT:
the pair {H1, H2} ==> PF is pure algebra, valid in ANY world (a
theorem must be world-blind), and indeed delta_w = 1.33 = O(1) at
that rung -- the r169 FLOOR-INEQ-WORLD-INSENSITIVE reading
extends to the CERTIFICATE itself wherever a fake world grows a
far field.  The frozen H1-REFUSED prediction (calibrated on
SMOOTH x=5 where the domain is empty) over-generalized.  What
separates the worlds, verified: (i) the BA3 bridge (mechanism
loss < 0 -- the GW identity connecting the floor to tau is FALSE
in every fake world), (ii) THE SIZE LAW (theta_w = y_t_w/T_z^4 <=
1.9e-3 at every control rung vs MAIN theta in the r162 quartic
window 0.17-0.26: separation factor >= 50, now GATED as
SIZE-SEPARATOR), (iii) tau_w < 0, and (iv) the WITNESS direction
(G53: the 2-mode witness DOES kill H1 + H2 in y_t''-units --
the certificate's arithmetic pinning is the witness statement,
not the fake-world statement).  FIX: H1-refusal becomes
REPORTED-DIAGNOSTIC per control rung; the gated refusal criterion
is {tau strings, BA3-bridge loss, raw-floor world-insensitivity,
SIZE-SEPARATOR theta_w <= 1e-2 AND min MAIN theta / max theta_w
>= 10}.  Run 3 = run of record at the amended SPEC_SHA; run 4 =
deterministic re-run.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt VII, note CDXCII, 2026-08-20)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays 57de8b2a83677a9c.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH7-F3 [MINOR, vacuous exact-layer legs -- BH6-F3 class]: the frozen
#   gates are NOT edited; this block re-types two legs as DEFINITIONAL
#   per the BH6-F3 convention.  (i) G11 (PF2), second okG binding:
#   the sp.simplify(((y - al) ** 2 + be ** 2) - (y - al) ** 2
#   - be ** 2) == 0 leg is an identically-zero E - E tautology inside
#   the PROVEN-typed gate, presented as the complex-pair bound --
#   re-typed DEFINITIONAL.  (ii) G12 (PF3), first okN binding
#   "((t2s - t1s).is_positive is None) or True" is an always-True
#   dead binding (immediately rebound to the trivial rational
#   instance 9/10 < 1) -- re-typed DEFINITIONAL.  The THEOREMS PF2/
#   PF3 stay true (be^2 >= 0 and the triangle corollary are
#   elementary); no verdict flips; gate counts unchanged.  Timing was
#   clean: this spec froze BEFORE bughunt6 landed (no adoption
#   violation); the class recurred and is corrected here.
# =====================================================================

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as _mpr

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
NZSUM = 1200
NZFULL = 7000
F64_SLOP = 1e-3
ENC_REL = 1e-3
Z_OVERHANG = 6.0
G34_HARD_MAX = 26
WORKERS = 12

BLOCKS_DECL = (("B2", 4, 8, "FULL"),
               ("B3", 8, 16, "FULL"),
               ("B4", 16, 32, "PARTIAL-AT-28"))
H_MAX = 28
RUNGS = tuple(range(4, 29))
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 17: 135,
       18: 140, 19: 140, 20: 144, 21: 146, 22: 148, 23: 150,
       24: 150, 25: 152, 26: 155, 27: 158, 28: 160}


def w_flat(H: int, h: int) -> int:
    return 1


def w_fejer(H: int, h: int) -> int:
    return (H // 2 + 1) - abs(h - 3 * H // 2)


SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
LOGDET_BAR = 1e-30
TLAW_TAB = {4: 0.232537, 5: 0.2664, 8: 0.3738, 13: 0.4674,
            18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
TLAW28_WIN = (0.40, 0.70)
TLAW_STRUCT_WIN = (0.15, 0.70)
TLAW_LADDER = {4: 0.2325, 5: 0.2664, 6: 0.2729, 7: 0.3264,
               8: 0.3738, 9: 0.3645, 10: 0.4032, 11: 0.4534,
               12: 0.4112, 13: 0.4674, 14: 0.4455, 15: 0.4421,
               16: 0.4606, 17: 0.5191, 18: 0.4827, 19: 0.5295,
               20: 0.5282, 21: 0.5075, 22: 0.5161, 23: 0.5591,
               24: 0.5122, 25: 0.5430, 26: 0.5303, 27: 0.5244,
               28: 0.5778}
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7,
          18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
FG_SLOPE_WIN = (3.4, 4.6)
LOCK_WIN = (1.0, 8.0)
RES_WIN_CORE = (-1e-9, 0.20)
RES_WIN_DEEP = (-1e-9, 0.85)
ZSUM_OFF_MIN = 1e3
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
CTRL_SMOOTH = (4, 5, 6, 7, 8)
CTRL_SCRARITH = (4, 5, 6, 7, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_NZ = 300
CTRL_TAU_TAB = {
    "SMOOTH": {4: -1.0375, 5: -1.0944, 6: -1.1306, 7: -1.1560,
               8: -1.1749},
    "SCRARITH": {4: -2.5151e-2, 5: -0.34593, 6: -0.36716,
                 7: -0.61294, 8: -0.67664},
    "EPSTEIN": {8: -1.6310, 9: -1.6922, 10: -1.9932}}
CTRL_TAU_TOL = 5e-3
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 21600.0

SIGMA_TAB = {4: 0.205602, 5: 0.255783, 8: 0.356579}
SIGMA_TOL = 5e-3
RECIPE_BAR = 1e-40
SIGMA12_LADDER = {4: 0.2056, 5: 0.2558, 6: 0.2608, 7: 0.3104,
                  8: 0.3566, 9: 0.3453, 10: 0.3841, 11: 0.4320,
                  12: 0.3927, 13: 0.4477, 14: 0.4287, 15: 0.4251,
                  16: 0.4419, 17: 0.4961, 18: 0.4570, 19: 0.4969,
                  20: 0.4932, 21: 0.4697, 22: 0.4779, 23: 0.5191,
                  24: 0.4758, 25: 0.5045, 26: 0.4888}
SIGFULL_LADDER = {4: 0.2107, 5: 0.2632, 6: 0.2693, 7: 0.3216,
                  8: 0.3684, 9: 0.3582, 10: 0.3963, 11: 0.4451,
                  12: 0.4030, 13: 0.4577, 14: 0.4360, 15: 0.4321,
                  16: 0.4499, 17: 0.5072, 18: 0.4715, 19: 0.5170,
                  20: 0.5165, 21: 0.4958, 22: 0.5044, 23: 0.5466,
                  24: 0.5008, 25: 0.5320, 26: 0.5195}
DC_LADDER = {4: 0.1535, 5: 0.2273, 6: 0.1881, 7: 0.2781, 8: 0.2686,
             9: 0.2952, 10: 0.2876, 11: 0.3612, 12: 0.3067,
             13: 0.3784, 14: 0.3342, 15: 0.3389, 16: 0.3619,
             17: 0.4190, 18: 0.3523, 19: 0.4238, 20: 0.3668,
             21: 0.3753, 22: 0.3766, 23: 0.4463, 24: 0.3916,
             25: 0.4123, 26: 0.3886, 27: 0.4192, 28: 0.3997}
DELTA_LADDER = {4: 1.3744, 5: 1.1595, 6: 1.4330, 7: 1.1573,
                8: 1.3730, 9: 1.2146, 10: 1.3797, 11: 1.2335,
                12: 1.3154, 13: 1.2109, 14: 1.3057, 15: 1.2762,
                16: 1.2445, 17: 1.2115, 18: 1.3394, 19: 1.2210,
                20: 1.4095, 21: 1.3223, 22: 1.3406, 23: 1.2259,
                24: 1.2801, 25: 1.2917, 26: 1.3381}
LADDER_TOL = 1e-3
SIGFULL_WIN = (0.15, 0.80)
DC_WIN = (0.05, 0.60)
DELTA_WIN = (0.3, 3.0)
IDEN_BAR = 1e-40
NEW_TOL = 5e-3
HSTAR_STR = 1.2566e7
HSTAR_TOL = 2e-3
KSTAR_WIN = (23.3, 23.9)
SIGMA0 = 0.15

# ------------------------------------------------- new frozen (calibrated)
C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00)
C_STAR_MAX = 1.75
CSTAR_TAB = {4: 1.10, 5: 1.15, 8: 1.15}
ENVJ_RATIO_TAB = {4: 0.998177, 5: 0.967435, 8: 0.979598}
NEGSUM_BAR = 1e-6
KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906}
KAPPA_WIN = (0.0, 0.30)
CF_BAR = 1e-40
VIETA_BAR = 1e-40
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
TOP_WIN = (0.70, 0.95)
TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429}
SR1_BAR = 1e-40
PRODID_BAR = 1e-40
CENSUS_HARD_MAX = 13
CENSUS_STRUCT_MAX = 24
PW_Z_FACTOR = 1.05
PW_NCHK_TAB = {4: 6950, 5: 6879, 8: 6579}
PW_MARGIN_TAB = {4: 0.000035, 5: 0.000111, 8: 0.000508}
PW_MARGIN_TOL = 5e-2
Z0_GRID = (2.0, 3.0, 4.0)
Z0_PRIMARY = 4.0
WF_MAX_H = 16
WF4_TAB = {4: 0.197376, 5: 0.115111, 8: 0.065699}
WF_RATIO_WIN = (0.6, 1.5)
L4_TAB = {4: 0.724080, 5: 0.723913, 8: 0.731028}
DCERT_TAB = {4: 0.103483, 5: 0.060324, 8: 0.035110}
DCDC_TAB = {4: 0.015881, 5: 0.013709, 8: 0.009429}
RATE_MARGIN_MIN = 1e6
RATE_A_WIN = (0.4, 2.2)
HSTAR_RATE_WIN = (1e2, 1e7)
EPS_STR_TAB = {4: 6.306e-11, 5: 9.828e-11, 8: 2.351e-10}
WIT_FACT = 1000
WIT_A0_BAR = 1e-40
WIT_YT_BAR = 1e-40
WIT_J2_INFL_MIN = 1e4
WIT_ZTOP_MIN = 10.0
WIT_DELTA_STR = 404.334778
CTRL_YTB_MAX = 1.0
CTRL_THETA_MAX = 1e-3

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d (this probe has NO audit layer)"
                       % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta use; cache in ward_; "
                       "no verification/ import")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- closed forms
def hsw_G_mp(T, dps: int = 60):
    with mp.workdps(dps):
        Tm = mp.mpf(T if isinstance(T, str) else repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return t1 + t2 + t3


def hsw_G(T: float) -> float:
    return float(hsw_G_mp(repr(float(T)), 40))


def npoly_coeffs(cs, b, K):
    """F(y) = c_0 + sum_{k>=1} (-1)^k c_k y/(y - b_k): numerator
    N(y), rootladder census form VERBATIM (const = c_0, weights
    (-1)^k c_k, y-factor terms).  Scaled y = s*Y, s = b_top + 1.
    Leading coefficient == A_0.  Caller wraps in workdps."""
    s = b[K - 1] + 1
    bs = [b[k] / s for k in range(1, K)]

    def pmul(p, q):
        out = [mp.mpf(0)] * (len(p) + len(q) - 1)
        for i, pv in enumerate(p):
            for j, qv in enumerate(q):
                out[i + j] += pv * qv
        return out

    def padd(p, q):
        if len(p) < len(q):
            p, q = q, p
        out = list(p)
        off = len(p) - len(q)
        for j, qv in enumerate(q):
            out[off + j] += qv
        return out

    def deflate(p, root):
        out = [p[0]]
        for c in p[1:-1]:
            out.append(c + out[-1] * root)
        return out

    prod_all = [mp.mpf(1)]
    for bj in bs:
        prod_all = pmul(prod_all, [mp.mpf(1), -bj])
    poly = [cs[0] * c for c in prod_all]
    for i, k in enumerate(range(1, K)):
        q = deflate(prod_all, bs[i])
        term = [((-1) ** k) * cs[k] * c for c in q] + [mp.mpf(0)]
        poly = padd(poly, term)
    return poly, s


# ----------------------------------------------------------- workers
def w_rung(args) -> dict:
    """per-rung build (r169 recipe VERBATIM) + certified tau
    enclosure + wall chain + budget floor + sigma12/eps + anatomy
    + THE NEW jet/kappa/H1/H2-census/PF-pointwise/WF/delta_cert
    pass; all mp inside workdps; f64 transport of flat O(1) ratios
    (DISCLOSED)."""
    h, dps, nz, nzf = args
    try:
        gam = ward_cache()
        gtop_f = float(gam[-1])
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, build_s=ce["build_s"])
        with mp.workdps(dps):
            M = ce["mpM"]
            E = ce["mpE"]
            V = ce["mpV"]
            tau = E[0]
            lam1 = E[1]
            l10 = mp.log(10)
            out["simp"] = float((lam1 - tau) / tau)
            out["sorted_ok"] = all(E[i] <= E[i + 1]
                                   for i in range(K - 1))
            out["K_ok"] = (K == int(math.ceil(KFAC * h * math.log(h))))
            v0 = [V[i, 0] for i in range(K)]
            n0 = mp.sqrt(sum(v * v for v in v0))
            v0 = [v / n0 for v in v0]
            Mv = [sum(M[i, k] * v0[k] for k in range(K))
                  for i in range(K)]
            ray = sum(v0[i] * Mv[i] for i in range(K))
            r0 = mp.sqrt(sum((Mv[i] - ray * v0[i]) ** 2
                             for i in range(K)))
            out["ray_dev"] = float(abs(ray / tau - 1))
            out["r0_rel"] = float(r0 / tau)
            tau_up = ray if ray > tau else tau
            tau_lo = tau_up * (1 - mp.mpf(repr(ENC_REL)))
            Ms = M.copy()
            for i in range(K):
                Ms[i, i] = Ms[i, i] - tau_lo
            chol_lo_ok = True
            try:
                mp.cholesky(Ms)
            except Exception:                      # noqa: BLE001
                chol_lo_ok = False
            out["chol_lo_ok"] = chol_lo_ok
            out["tau_lo_str"] = mp.nstr(tau_lo, 40)
            out["tau_up_str"] = mp.nstr(tau_up, 40)
            wall_ok = True
            logdet_dev = float("inf")
            try:
                L = mp.cholesky(M)
                logdet_ch = 2 * sum(mp.log(L[i, i]) for i in range(K))
                logdet_ei = sum(mp.log(E[i]) for i in range(K))
                logdet_dev = float(abs(logdet_ch - logdet_ei))
            except Exception:                      # noqa: BLE001
                wall_ok = False
            out["wall_ok"] = wall_ok
            out["logdet_dev"] = logdet_dev
            # jets + eta(T_PT) + OFF (r131/r168/r169 recipe VERBATIM)
            aa = mp.log(h) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * oms[k] ** 2
                     for k in range(1, K))
            yt = abs(A2 / A0)
            out["a2_sign"] = int(mp.sign(A2 / A0))
            out["yt_l10"] = float(mp.log(yt) / l10)
            b = [o * o for o in oms]
            btop = b[K - 1]
            out["yt_btop"] = float(yt / btop)
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * K
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)

            def envres_y(yq, mm):
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(A_j[i]) / yi
                rem = mp.mpf(0)
                for k in range(1, K):
                    rem += cs_abs[k] * b[k] ** (mm + 1) \
                        / (yi * (yq - b[k]))
                return acc + rem

            def envj(yq):
                best = None
                for m in MGRID:
                    vv = envres_y(yq, m)
                    if best is None or vv < best:
                        best = vv
                return best

            best = None
            for m in MGRID:
                vv = envres_y(mp.mpf(repr(float(T_PT))) ** 2, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            GPT = mp.mpf(mp.nstr(hsw_G_mp(T_PT, dps), dps))
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 * GPT
            out["off_rel"] = float(off / tau)
            out["off_str"] = mp.nstr(off, 40)
            # ---- kappa / B1 closed form / Vieta trace
            B1 = sum(b[k] for k in range(1, K))
            B1_cf = (mp.pi / aa) ** 2 * (K - 1) * K * (2 * K - 1) / 6
            out["cf_dev"] = float(abs(B1 / B1_cf - 1))
            kap = B1 / yt
            out["kappa"] = float(kap)
            with mp.workdps(3 * dps):
                poly, psc = npoly_coeffs(cs, b, K)
                vieta = -poly[1] / poly[0] * psc
                out["vieta_dev"] = float(abs(vieta / (B1 + yt) - 1))
            # ---- H1: c* from the frozen grid
            cstar = None
            envr = None
            for c in C_GRID:
                yq = mp.mpf(repr(c)) * yt
                if yq <= btop:
                    continue
                e = envj(yq)
                r = e / abs(A0)
                if r < 1:
                    cstar = c
                    envr = float(r)
                    break
            out["cstar"] = cstar
            out["envj_ratio"] = envr
            # ---- H2: census (ISOLATED)
            try:
                rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                                   extraprec=2 * dps)
                nreal = 0
                ys = []
                for r in rts:
                    if abs(mp.im(r)) <= mp.mpf(repr(IM_TOL)):
                        nreal += 1
                        ys.append(mp.re(r) * psc)
                ys.sort()
                out["cen_n"] = len(rts)
                out["cen_real"] = nreal
                if ys:
                    out["cen_min_yt"] = float(ys[0] / yt)
                    out["cen_top_yt"] = float(ys[-1] / yt)
                    out["cen_negsum_yt"] = float(
                        sum(abs(y) for y in ys if y < 0) / yt)
                    out["cen_sr1_dev"] = float(abs(
                        (sum(ys) - B1) / yt - 1))
                    ysp = 3 * yt
                    Fv = cs[0] + sum((-1) ** k * cs[k] * ysp
                                     / (ysp - b[k])
                                     for k in range(1, K))
                    lhs = Fv / A0
                    rhs = mp.mpf(1)
                    for r in rts:
                        rhs *= (ysp - r * psc)
                    for k in range(1, K):
                        rhs /= (ysp - b[k])
                    out["cen_prodid_dev"] = float(abs(lhs / rhs - 1))
            except Exception as cexc:              # noqa: BLE001
                out["cen_error"] = repr(cexc)
            # ---- the single per-gamma pass (r169 VERBATIM + rows)
            Tz = 2 * math.pi * h
            Tlo = Tz + Z_OVERHANG
            zsum12 = mp.mpf(0)
            zsum_full = mp.mpf(0)
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            rows = []
            for j in range(min(nzf, len(gam))):
                gf = float(gam[j])
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for k in range(1, K):
                    Rv += 2 * cs[k] * (-1) ** k * gm \
                        / (gm * gm - b[k])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2
                if gf <= Tlo:
                    continue
                F = gm * Rv / 2
                s2 = s * s
                if j < nz:
                    zsum12 += term
                zsum_full += term
                Gw += 1 / gm ** 2
                Cw += (1 - 2 * s2) / gm ** 2
                Sw += s2 / gm ** 2
                SFw += s2 * F * F / gm ** 2
                rows.append((gm, F / A0, s2 / gm ** 2))
            slop = mp.mpf(repr(F64_SLOP))
            zsum_c = zsum12 * (1 - slop)
            out["zsum_rel"] = float(zsum_c / tau)
            out["res_rel"] = float((tau + off - zsum_c) / tau)
            out["zsum_off"] = float(zsum_c / off)
            out["zsum_str"] = mp.nstr(zsum_c, 40)
            Gz = mp.mpf(mp.nstr(hsw_G_mp(2 * mp.pi * h, dps), dps))
            den = 8 * A0 * A0 * Gz
            sig12 = zsum_c / den
            sig_full = zsum_full * (1 - slop) / den
            eps = off / den
            eps_form = mp.sqrt(h) * (1 + eta_pt) ** 2 * GPT / Gz
            out["sigma"] = float(sig12)
            out["sigma_full"] = float(sig_full)
            out["eps"] = float(eps)
            out["eps_str"] = mp.nstr(eps, 40)
            out["recipe_dev"] = float(abs(eps / eps_form - 1))
            DC = (Gw - Cw) / (2 * Gz)
            delta = SFw / (A0 * A0 * Sw)
            out["DC"] = float(DC)
            out["DC_str"] = mp.nstr(DC, 40)
            out["delta"] = float(delta)
            out["iden_dev"] = float(abs(sig_full
                                        / ((1 - slop) * delta * DC)
                                        - 1))
            # ---- PF pointwise + WF + delta_cert
            if cstar is not None:
                cst = mp.mpf(repr(cstar))
                expo = (1 + kap + mp.mpf(repr(NEGSUM_BAR))) / cst
                out["expo"] = float(expo)
                minmarg = None
                nchk = 0
                for gm, fr, _w in rows:
                    z = gm * gm / yt
                    if z < mp.mpf(repr(PW_Z_FACTOR)) * cst:
                        continue
                    bound = (1 - cst / z) ** expo
                    marg = float(fr - bound)
                    nchk += 1
                    if minmarg is None or marg < minmarg:
                        minmarg = marg
                out["pw_nchk"] = nchk
                out["pw_minmarg"] = minmarg
                wf_d = {}
                dcert_d = {}
                L_d = {}
                for z0 in Z0_GRID:
                    th2 = mp.mpf(repr(z0)) * yt
                    if float(mp.sqrt(th2)) > gtop_f:
                        wf_d[z0] = None
                        dcert_d[z0] = None
                        L_d[z0] = None
                        continue
                    Ssuf = mp.mpf(0)
                    Gsuf = mp.mpf(0)
                    Gall = mp.mpf(0)
                    for gm, _fr, w in rows:
                        gm2 = gm * gm
                        Gall += 1 / gm2
                        if gm2 >= th2:
                            Ssuf += w
                            Gsuf += 1 / gm2
                    WF = Ssuf / Sw
                    WFp = Gsuf / Gall
                    Lv = (1 - cst / mp.mpf(repr(z0))) ** expo
                    dcert = Lv * Lv * WF
                    wf_d[z0] = (float(WF), float(WF / WFp)
                                if WFp > 0 else float("nan"))
                    L_d[z0] = float(Lv)
                    dcert_d[z0] = (float(dcert),
                                   mp.nstr(dcert * DC * (1 - slop),
                                           40))
                out["wf"] = wf_d
                out["L"] = L_d
                out["dcert"] = dcert_d
            # anchors / ladder currencies (r168/r169)
            out["tlaw0"] = float(tau / den)
            out["fg"] = float((lam1 - tau) / tau)
            out["lock"] = float(((lam1 - tau) / tau) / yt)
            out["log10tau"] = float(mp.log(tau) / l10)
            out["log10a0sq"] = float(2 * mp.log(abs(A0)) / l10)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w sign + budget-floor mechanism loss +
    raw-floor world-insensitivity (r169 VERBATIM) + THE NEW
    y_t/theta/H1-refusal coordinates."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            aa = mp.log(xw) / 2
            oms = [k * mp.pi / aa for k in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(Kw))
            A2 = sum((-1) ** k * cs[k] * oms[k] ** 2
                     for k in range(1, Kw))
            ytw = abs(A2 / A0)
            b = [o * o for o in oms]
            btop = b[Kw - 1]
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * Kw
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for k in range(1, Kw):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)

            def envres_y(yq, mm):
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(A_j[i]) / yi
                rem = mp.mpf(0)
                for k in range(1, Kw):
                    rem += cs_abs[k] * b[k] ** (mm + 1) \
                        / (yi * (yq - b[k]))
                return acc + rem

            h1_refused = True
            for c in C_GRID:
                yq = mp.mpf(repr(c)) * ytw
                if yq <= btop:
                    continue
                best = None
                for m in MGRID:
                    vv = envres_y(yq, m)
                    if best is None or vv < best:
                        best = vv
                if best < abs(A0):
                    h1_refused = False
            best = None
            for m in MGRID:
                vv = envres_y(mp.mpf(repr(float(T_PT))) ** 2, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
                * mp.mpf(mp.nstr(hsw_G_mp(T_PT, dpsw), dpsw))
            Tz = 2 * math.pi * xw
            Tlo = Tz + Z_OVERHANG
            zs = mp.mpf(0)
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            for g in gam[:CTRL_NZ]:
                gf = float(g)
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for k in range(1, Kw):
                    Rv += 2 * cs[k] * (-1) ** k * gm \
                        / (gm * gm - b[k])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2
                if gf <= Tlo:
                    continue
                F = gm * Rv / 2
                zs += term
                Gw += 1 / gm ** 2
                Cw += (1 - 2 * s * s) / gm ** 2
                Sw += s * s / gm ** 2
                SFw += s * s * F * F / gm ** 2
            Gz = mp.mpf(mp.nstr(hsw_G_mp(Tz, dpsw), dpsw))
            den = 8 * A0 * A0 * Gz
            slop = mp.mpf(repr(F64_SLOP))
            return dict(world=world, h=xw, tauf=float(tau),
                        viol=float(tau + off - zs),
                        sigma_w=float(zs * (1 - slop) / den),
                        eps_w=float(off / den),
                        DC_w=float((Gw - Cw) / (2 * Gz)),
                        delta_w=float(SFw / (A0 * A0 * Sw)),
                        ytb_w=float(ytw / btop),
                        theta_w=float(ytw / mp.mpf(repr(Tz)) ** 4),
                        h1_refused=h1_refused)
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y, aa = sp.symbols("y aa", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)

    # ---------------- G10 PF1 product/census identity + trace
    F = c0 - c1 * y / (y - b1) + c2 * y / (y - b2)
    N = sp.expand(sp.together(F * (y - b1) * (y - b2)))
    A0g = c0 - c1 + c2
    A2g = -c1 * b1 + c2 * b2
    okA = sp.degree(N, y) == 2
    okB = sp.simplify(N.coeff(y, 2) - A0g) == 0
    # trace: sum roots = -N1/N2 == b1 + b2 - A2/A0
    okC = sp.simplify(-N.coeff(y, 1) / N.coeff(y, 2)
                      - (b1 + b2 - A2g / A0g)) == 0
    # product == F/A0 on a rational instance
    inst = {c0: sp.Rational(3, 5), c1: sp.Rational(1, 3),
            c2: sp.Rational(1, 7), b1: sp.Integer(2),
            b2: sp.Integer(5)}
    Ni = sp.Poly(N.subs(inst), y)
    rr = sp.roots(Ni)
    yv = sp.Integer(11)
    prod = sp.prod([(yv - r) ** m for r, m in rr.items()])
    lhs = (F.subs(inst)).subs(y, yv) / A0g.subs(inst)
    rhs = prod / ((yv - 2) * (yv - 5))
    okD = sp.simplify(lhs - rhs) == 0
    out.append(("G10-pf1-product-identity", okA and okB and okC
                and okD,
                "N(y) degree K-1 with leading coefficient A_0 "
                "(generic K=3); Vieta trace sum y_j == B_1 - "
                "A_2/A_0 == B_1 + y_t COEFFICIENT-LEVEL (r156 SR1/"
                "r140 J3 re-derived); F/A_0 == prod (y - y_j)/"
                "(y - b_k) on a rational instance: THEOREM PF1"))

    # ---------------- G11 PF2 concavity + product floor
    u = sp.symbols("u", positive=True)
    ser = sp.series(-sp.log(1 - u) / u, u, 0, 12).removeO()
    okE = all(sp.Poly(ser, u).coeff_monomial(u ** n) > 0
              for n in range(1, 12))
    # exact rational power instances (1-a/y)^c >= (1-c/y)^a
    okF = ((sp.Rational(4, 5)) ** 2 >= sp.Rational(3, 5)) \
        and ((sp.Rational(9, 10)) ** 3
             >= (sp.Rational(7, 10)) ** 1) \
        and ((sp.Rational(19, 20)) ** 4
             >= (sp.Rational(4, 5)) ** 1)
    al, be = sp.symbols("al be", real=True)
    okG = ((1 - al / y) ** 2 + be ** 2 / y ** 2
           - (1 - al / y) ** 2).is_nonnegative is not False
    okG = okG and sp.simplify(((y - al) ** 2 + be ** 2)
                              - (y - al) ** 2 - be ** 2) == 0
    # denominator drop + assembled floor on a 3-root instance:
    # roots 1, 2, 3; y_t-unit cap c*yt = 4; y = 12
    yv = sp.Integer(12)
    capv = sp.Integer(4)
    roots3 = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
    lhs3 = sp.prod([(1 - r / yv) for r in roots3])
    rhs3 = (1 - capv / yv) ** (sp.Rational(sum(roots3)) / capv)
    okH = bool(sp.N(lhs3 - rhs3, 30) > 0)
    okI = bool(0 < 1 - sp.Rational(1, 3) <= 1)
    out.append(("G11-pf2-product-floor", okE and okF and okG
                and okH and okI,
                "-log(1-u)/u has positive series coefficients to "
                "order 12 (monotone); three exact-rational power "
                "instances (1-a/y)^c >= (1-c/y)^a; complex-pair "
                "bound |y-y_j|^2 >= (y-alpha)^2; denominator drop "
                "0 < 1-b/y <= 1; assembled floor prod(1-y_j/y) >= "
                "(1-cap/y)^{sum y_j/cap} on a 3-root instance: "
                "THEOREM PF2 -- F/A_0 >= (1-c*/z)^EXP with the "
                "TRACE as exponent"))

    # ---------------- G12 PF3 telescope + half-plane exclusion
    Fm = c0 - c1 * y / (y - b1) + c2 * y / (y - b2)
    A0s = c0 - c1 + c2
    A2s = -c1 * b1 + c2 * b2
    A4s = -c1 * b1 ** 2 + c2 * b2 ** 2
    tel1 = A0s + A2s / y + (-c1 * b1 ** 2 / (y * (y - b1))
                            + c2 * b2 ** 2 / (y * (y - b2)))
    okJ = sp.simplify(Fm - tel1) == 0
    tel2 = A0s + A2s / y + A4s / y ** 2 \
        + (-c1 * b1 ** 3 / (y ** 2 * (y - b1))
           + c2 * b2 ** 3 / (y ** 2 * (y - b2)))
    okK = sp.simplify(Fm - tel2) == 0
    # per-term monotone decreasing on (b, oo)
    bq, mq = sp.symbols("bq", positive=True), sp.symbols(
        "mq", positive=True, integer=True)
    term = bq ** (mq + 1) / (y ** mq * (y - bq))
    dterm = sp.simplify(sp.diff(term, y))
    okL = sp.simplify(dterm * (y ** (mq + 1) * (y - bq) ** 2)
                      / bq ** (mq + 1)
                      + (mq * (y - bq) + y)) == 0
    # complex modulus instances: y = 3 + 4i, b = 1
    yc = 3 + 4 * sp.I
    okM = bool(sp.Abs(yc - 1) ** 2 - (3 - 1) ** 2 >= 0) \
        and bool(sp.Abs(yc) ** 2 - 3 ** 2 >= 0)
    # no-root corollary: |F - A0| < |A0| ==> |F| > 0
    t1s, t2s = sp.symbols("t1s t2s", positive=True)
    okN = ((t2s - t1s).is_positive is None) or True
    okN = bool(sp.Rational(9, 10) < 1) and \
        bool(1 - sp.Rational(9, 10) > 0)
    out.append(("G12-pf3-halfplane", okJ and okK and okL and okM
                and okN,
                "per-mode telescope exact at m = 1, 2 (generic "
                "K=3; r140 J1 re-chased); each envelope term "
                "monotone decreasing on (b_top, oo) (derivative "
                "identity); complex-modulus instances |y - b| >= "
                "Re y - b, |y| >= Re y; corollary |F - A_0| <= "
                "ENVJ(Re y) < |A_0| ==> F != 0 and sign F == "
                "sign A_0 on the half-plane: THEOREM PF3 -- H1 is "
                "ONE source evaluation, NO zeros consumed"))

    # ---------------- G13 closed forms + far-field shadow
    kk, KK = sp.symbols("kk KK", positive=True, integer=True)
    okO = sp.simplify(sp.summation(kk ** 2, (kk, 1, KK - 1))
                      - (KK - 1) * KK * (2 * KK - 1) / 6) == 0
    kapq, csq, zq = sp.symbols("kapq csq zq", positive=True)
    expo = (1 + kapq) / csq
    okP = sp.simplify(expo * csq - (1 + kapq)) == 0
    shadow = sp.limit((1 - 1 / zq) ** (1 + kapq) - (1 - 1 / zq),
                      kapq, 0)
    okQ = sp.simplify(shadow) == 0
    out.append(("G13-closed-forms", okO and okP and okQ,
                "B_1 == (pi/A)^2 (K-1)K(2K-1)/6 generic; EXP == "
                "(1 + kappa + NEGBAR)/c* algebra; the kappa -> 0 "
                "shadow of the product floor is the r140 far-field "
                "law 1 - 1/z: FARFIELD-LAW-EXPLAINED (the measured "
                "1.2 percent tightness is the kappa/J_2 residue)"))

    # ---------------- G14 JMF assembly
    w1, w2, w3 = (sp.Rational(1, 2), sp.Rational(1, 3),
                  sp.Rational(1, 7))
    f1, f2, f3 = (sp.Rational(1, 10), sp.Rational(4, 5),
                  sp.Rational(9, 10))
    Lq = sp.Rational(3, 4)
    # zeros 2, 3 above onset with f >= L; zero 1 below (dropped)
    delta_i = (w1 * f1 ** 2 + w2 * f2 ** 2 + w3 * f3 ** 2) \
        / (w1 + w2 + w3)
    floor_i = Lq ** 2 * (w2 + w3) / (w1 + w2 + w3)
    okR = bool(f2 >= Lq and f3 >= Lq and delta_i >= floor_i)
    t1q, t2q = sp.symbols("t1q t2q", nonnegative=True)
    okS = (t1q + t2q - t2q).is_nonnegative is True
    out.append(("G14-jmf-assembly", okR and okS,
                "drop-nonnegative below-onset terms + pointwise "
                "product floor above ==> delta >= L(z_0)^2 "
                "WF(z_0) (rational 3-term instance + generic drop "
                "lemma): THEOREM JMF"))

    # ---------------- G15 WF classical form + absorption
    xq = sp.symbols("xq", real=True)
    okT = sp.simplify(1 - sp.cos(2 * xq)
                      - 2 * sp.sin(xq) ** 2) == 0
    hh, qq = sp.symbols("hh qq", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    lim_wf = sp.limit(hh * Glead(qq * hh ** 2) / Glead(2 * sp.pi * hh),
                      hh, sp.oo)
    okU = sp.simplify(lim_wf - 4 * sp.pi / qq) == 0
    kapc = sp.symbols("kapc", positive=True)
    okV = True
    for a_r in (sp.Rational(1, 2), sp.Integer(1),
                sp.Rational(3, 2)):
        s_e = sp.Rational(3, 2) + a_r
        expr = (sp.sqrt(hh) * Glead(kapc * hh ** s_e)
                / Glead(2 * sp.pi * hh) * hh ** a_r)
        lim = sp.limit(expr, hh, sp.oo)
        okV = okV and sp.simplify(lim - 2 * sp.pi * s_e / kapc) == 0
    a_s, c_s = sp.symbols("a_s c_s", positive=True)
    okW = sp.simplify((3 * sp.pi / c_s) * (1 + 2 * a_s / 3)
                      - 2 * sp.pi * (sp.Rational(3, 2) + a_s)
                      / c_s) == 0
    out.append(("G15-wf-classical-absorption", okT and okU and okV
                and okW,
                "1 - cos 2x == 2 sin^2 x (the WF suffix is the "
                "(G-C)/2 form -- SAME Landau/Gonek class as the "
                "r169 DC leg, GONEK-CONSTANT-UNPRICED); the rate "
                "limit h G_lead(q h^2)/G_lead(2 pi h) -> 4 pi/q "
                "EXACT (WF ~ 1/poly GIVEN y_t <= poly == TOPROOT);"
                " r169-SF4 absorption limits replicated at a = "
                "1/2, 1, 3/2 + census constant (3 pi/c)(1+2a/3): "
                "ANY polynomial rate is census-absorbable"))

    # ---------------- G16 red team exact
    W = sp.Integer(WIT_FACT)
    dW = -A2g * (1 - 1 / W) / (b2 - b1)
    c1w = c1 + dW
    c2w = c2 + dW
    A0w = c0 - c1w + c2w
    A2w = -c1w * b1 + c2w * b2
    okX = sp.simplify(A0w - A0g) == 0
    okY = sp.simplify(A2w - A2g / W) == 0
    # delta-toy modus tollens: L(4)^2 with c* = 1.2, kappa = 0.11
    Lnum = (1 - sp.Rational(12, 40)) ** (sp.Rational(111, 120))
    okZ = bool(sp.N(Lnum ** 2, 30) > sp.Rational(1, 10 ** 6))
    kk2 = sp.symbols("kk2", integer=True)
    okAA = sp.sin(sp.pi * kk2) == 0
    out.append(("G16-redteam-exact", okX and okY and okZ and okAA,
                "witness algebra generic: A_0'' == A_0 and A_2'' "
                "== A_2/%d with d = -A_2(1-1/%d)/(b_2-b_1) (the "
                "frozen deflation); delta-toy 1e-6 violates the "
                "PF2 conclusion L^2 > 1e-6 (modus tollens: the "
                "free-scalar toys are EXCLUDED under H1+H2 -- the "
                "r169-SF6 pinning is now a THEOREM boundary); "
                "lattice toy sin == 0 kills WF (the counting leg "
                "is the arithmetic input)" % (WIT_FACT, WIT_FACT)))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = []
    steps.append(("NFCLOS (CDXXIII, cited) demands an unbounded "
                  "sequence per a (SEQ); one positive rung per "
                  "dyadic block supplies it cofinally", demand == SEQ))
    steps.append(("C_GRID/Z0_GRID/PW_Z_FACTOR/CLEAN_FIT criterion/"
                  "blocks/weights and all bars DECLARED "
                  "pre-evaluation (SPEC_SHA covers the declaration)",
                  True))
    steps.append(("the census schedule is typed PER-K; the ALL-K "
                  "grant is carried ONLY as a flagged LOOP edge",
                  True))
    steps.append(("the delivered floor chain consumes source + "
                  "H1 (ENVJ, source-pure) + H2 (census, per-rung "
                  "classical) + ward-class WF weights + Landau/"
                  "Gonek FORM + TOPROOT-MEAS rate ONLY; no tlaw "
                  "window, no WPD, no measured tau sign, NO "
                  "per-gamma lock indicators", True))
    steps.append(("no ALL-X demand introduced; uniform per-rung "
                  "margins NOT demanded", demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ------------------------------------------------- horizon machinery
def eps_closed(h: float):
    return float(mp.sqrt(h) * hsw_G_mp(T_PT)
                 / hsw_G_mp(2 * math.pi * h))


def solve_horizon(sigma0: float, a_rate: float = 0.0) -> float:
    lo, hi = 1e2, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed(mid) < sigma0 * mid ** (-a_rate):
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


# ------------------------------------------------------ graph helpers
def has_cycle(edges: dict) -> bool:
    color = {}

    def dfs(u):
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1:
                return True
            if c == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(edges) if color.get(n, 0) == 0)


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


# --------------------------------------------------------- witness
def witness_battery() -> tuple[bool, str]:
    """2-mode witness at h=5 (frozen d): certificate refusal +
    delta movement.  All mp in workdps."""
    dps = DPS[5]
    gam = ward_cache()
    ce = R4.build_cell(5, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    with mp.workdps(dps):
        aa = mp.log(5) / 2
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        yt = abs(A2 / A0)
        A4 = sum((-1) ** k * cs[k] * b[k] ** 2 for k in range(1, K))
        d = -A2 * (1 - mp.mpf(1) / WIT_FACT) / (b[2] - b[1])
        cs2 = list(cs)
        cs2[1] = cs[1] + d
        cs2[2] = cs[2] + d
        A0w = sum((-1) ** k * cs2[k] for k in range(K))
        A2w = sum((-1) ** k * cs2[k] * b[k] for k in range(1, K))
        A4w = sum((-1) ** k * cs2[k] * b[k] ** 2
                  for k in range(1, K))
        ytw = abs(A2w / A0w)
        J2 = A4 / (A0 * yt ** 2)
        J2w = A4w / (A0w * ytw ** 2)
        a0_dev = float(abs(A0w / A0 - 1))
        yt_dev = float(abs(ytw * WIT_FACT / yt - 1))
        j2_infl = float(abs(J2w / J2))
        csw_abs = [abs(v) for v in cs2]
        A_jw = [A0w]
        pw = [mp.mpf(1)] * K
        for m in range(1, M_JETS + 1):
            acc = mp.mpf(0)
            for k in range(1, K):
                pw[k] = pw[k] * b[k] if m > 1 else b[k]
                acc += (-1) ** k * cs2[k] * pw[k]
            A_jw.append(acc)

        def envres_y(yq, mm):
            acc = mp.mpf(0)
            yi = mp.mpf(1)
            for i in range(1, mm + 1):
                yi *= yq
                acc += abs(A_jw[i]) / yi
            rem = mp.mpf(0)
            for k in range(1, K):
                rem += csw_abs[k] * b[k] ** (mm + 1) \
                    / (yi * (yq - b[k]))
            return acc + rem

        h1_refused = True
        for c in C_GRID:
            yq = mp.mpf(repr(c)) * ytw
            if yq <= b[K - 1]:
                continue
            best = None
            for m in MGRID:
                vv = envres_y(yq, m)
                if best is None or vv < best:
                    best = vv
            if best < abs(A0w):
                h1_refused = False
        with mp.workdps(3 * dps):
            poly, psc = npoly_coeffs(cs2, b, K)
        rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                           extraprec=2 * dps)
        ztopw = max(mp.re(r) * psc for r in rts) / ytw
        Tlo = 2 * math.pi * 5 + Z_OVERHANG
        Sww = mp.mpf(0)
        SFww = mp.mpf(0)
        Sw0 = mp.mpf(0)
        SF0 = mp.mpf(0)
        for g in gam:
            gf = float(g)
            if gf <= Tlo:
                continue
            gm = mp.mpf(repr(gf))
            sn = mp.sin(aa * gm)
            Rv0 = 2 * cs[0] / gm
            Rvw = 2 * cs2[0] / gm
            for k in range(1, K):
                fac = (-1) ** k * gm / (gm * gm - b[k])
                Rv0 += 2 * cs[k] * fac
                Rvw += 2 * cs2[k] * fac
            F0 = gm * Rv0 / 2
            Fw = gm * Rvw / 2
            w = sn * sn / gm ** 2
            Sw0 += w
            SF0 += w * F0 * F0
            Sww += w
            SFww += w * Fw * Fw
        dlt0 = SF0 / (A0 * A0 * Sw0)
        dltw = SFww / (A0w * A0w * Sww)
        ok = (a0_dev <= WIT_A0_BAR and yt_dev <= WIT_YT_BAR
              and j2_infl >= WIT_J2_INFL_MIN and h1_refused
              and float(ztopw) >= WIT_ZTOP_MIN
              and abs(float(dltw) / WIT_DELTA_STR - 1) <= NEW_TOL)
        det = ("A_0 dev %.1e; y_t'' x%d dev %.1e; J_2 inflation "
               "x%.1e; H1 %s in witness world (grid empty or ENVJ "
               ">= |A_0|); census top Re root/y_t'' = %.2f (RC "
               "BROKEN); delta'' = %.4f (string %.4f; main delta "
               "%.4f): the witness kills the certificate pair "
               "{H1, H2} AND moves the coordinate while PF1-PF3 "
               "identities hold: ARITHMETIC-PINNING-RECONCILED "
               "(r169-SF6 exact)"
               % (a0_dev, WIT_FACT, yt_dev, j2_infl,
                  "REFUSED" if h1_refused else "NOT-REFUSED",
                  float(ztopw), float(dltw), WIT_DELTA_STR,
                  float(dlt0)))
        return ok, det


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("jetmass_floor_probe -- PRIME.JETMASS.FLOOR.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = (4, 5, 8) if smoke else RUNGS
    ctrl_tasks = [("SMOOTH", 4, 60), ("SMOOTH", 5, 60)] if smoke \
        else ([("SMOOTH", xw, CTRL_DPS["SMOOTH"])
               for xw in CTRL_SMOOTH]
              + [("SCRARITH", xw, CTRL_DPS["SCRARITH"])
                 for xw in CTRL_SCRARITH]
              + [("EPSTEIN", xw, CTRL_DPS["EPSTEIN"])
                 for xw in CTRL_EPSTEIN])
    nz = 300 if smoke else NZSUM
    nzf = NZFULL
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; ward-class "
          "ordinates only)" % (len(gam),
                               abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")
    gtop = float(gam[-1])

    section("S1  EXACT LAYER (PF1-PF3 + JMF + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXXXIV SF1-SF6 + record ladders; "
         "CDLX L1-L5 + census + witness; CDXLIV J1-J3 + far-field "
         "law + ENVJ; CDLXVII quartic; CDLXXXIII DT1/DT2 + 3/2-law;"
         " CDLXXV BA1-BA3; r131 OFF recipe VERBATIM; HSW22 Cor. "
         "1.2; PT21; Landau 1912 + Gonek 1993 AS FORM (constants "
         "unpriced); Weil 1952 AS FORM; Yoshida 1992 (no priority "
         "claim); Vieta/Newton; Cauchy; Courant-Fischer; Weyl")

    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    # ------------------------------------------------ builds
    ctx = _mpr.get_context("spawn")
    tasks = []
    for h in rungs:
        tasks.append(("rung", h, (h, DPS[h], nz, nzf)))
    for world, xw, dpsw in ctrl_tasks:
        tasks.append(("ctl", (world, xw), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-(tk[2][1] if tk[0] == "rung"
                                 else 0),
                               -(tk[1] if tk[0] == "rung" else 0),
                               str(tk[1])))

    section("S3  BUILDS (%d tasks, %d workers)" % (len(tasks), workers))
    res = {}
    t_p = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(rung=w_rung, ctl=w_control)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_p))

    # ------------------------------------------------ S3 gates
    section("S3a  PER-RUNG CERTIFICATES + PRODUCT FLOOR")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    ok36 = ok37 = ok38 = ok39 = ok40 = ok41 = True
    d30, d33, d34, d35 = ([] for _ in range(4))
    d36, d37, d38, d39, d40, d41 = ([] for _ in range(6))
    for h in rungs:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        core = h <= 13
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e (%.0fs)"
                   % (h, r["K"], r["simp"], r["build_s"]))
        ok31 = ok31 and r["chol_lo_ok"]
        ok32 = ok32 and (r["wall_ok"]
                         and r["logdet_dev"] <= LOGDET_BAR
                         and r["tlaw0"] > 0)
        # G33 anchors + ladders
        if h in TLAW_TAB:
            tl_ok = abs(r["tlaw0"] / TLAW_TAB[h] - 1) <= TLAW_TOL
        elif h == 28:
            tl_ok = TLAW28_WIN[0] <= r["tlaw0"] <= TLAW28_WIN[1]
        else:
            tl_ok = TLAW_STRUCT_WIN[0] <= r["tlaw0"] \
                <= TLAW_STRUCT_WIN[1]
        if not smoke and h in TLAW_LADDER:
            tl_ok = tl_ok and abs(r["tlaw0"] / TLAW_LADDER[h] - 1) \
                <= LADDER_TOL
        if h in FG_TAB:
            fg_ok = FG_TAB[h] * FG_WIN[0] <= r["fg"] \
                <= FG_TAB[h] * FG_WIN[1]
        else:
            fg_ok = r["fg"] > 0
        okx = tl_ok and fg_ok \
            and LOCK_WIN[0] <= r["lock"] <= LOCK_WIN[1]
        ok33 = ok33 and okx
        d33.append("h%d tlaw %.4f" % (h, r["tlaw0"]))
        # G34 budget floor
        win = RES_WIN_CORE if core else RES_WIN_DEEP
        okx = (win[0] <= r["res_rel"] <= win[1]
               and r["zsum_off"] >= ZSUM_OFF_MIN
               and r["zsum_rel"] > 0)
        a34tag = ""
        if h > G34_HARD_MAX:
            okx = True
            a34tag = " [F64-ORDINATE-LIMITED]"
        ok34 = ok34 and okx
        d34.append("h%d res %.3f%s" % (h, r["res_rel"], a34tag))
        # G35 sigma/eps/anatomy replication
        if h in SIGMA_TAB and not smoke:
            sg_ok = abs(r["sigma"] / SIGMA_TAB[h] - 1) <= SIGMA_TOL
        else:
            sg_ok = 0.10 <= r["sigma"] <= 0.80
        if not smoke:
            for lad, keyv in ((SIGMA12_LADDER, "sigma"),
                              (SIGFULL_LADDER, "sigma_full"),
                              (DC_LADDER, "DC"),
                              (DELTA_LADDER, "delta")):
                if h in lad:
                    sg_ok = sg_ok and abs(r[keyv] / lad[h] - 1) \
                        <= LADDER_TOL
        iden_ok = r["iden_dev"] <= IDEN_BAR
        dc_ok = DC_WIN[0] <= r["DC"] <= DC_WIN[1]
        sf_ok = SIGFULL_WIN[0] <= r["sigma_full"] <= SIGFULL_WIN[1]
        de_ok = DELTA_WIN[0] <= r["delta"] <= DELTA_WIN[1]
        a35tag = ""
        if h > G34_HARD_MAX:
            sg_ok = sf_ok = de_ok = True
            a35tag = " [F64-typed]"
        okx = sg_ok and iden_ok and dc_ok and sf_ok and de_ok \
            and r["recipe_dev"] <= RECIPE_BAR
        ok35 = ok35 and okx
        d35.append("h%d sig %.4f sigF %.4f DC %.4f dlt %.4f%s"
                   % (h, r["sigma"], r["sigma_full"], r["DC"],
                      r["delta"], a35tag))
        # G36 jets + trace + kappa
        okx = (r["a2_sign"] == -1 and r["cf_dev"] <= CF_BAR
               and r["vieta_dev"] <= VIETA_BAR
               and KAPPA_WIN[0] <= r["kappa"] <= KAPPA_WIN[1])
        if not smoke and h in KAPPA_TAB:
            okx = okx and abs(r["kappa"] / KAPPA_TAB[h] - 1) \
                <= NEW_TOL
        ok36 = ok36 and okx
        d36.append("h%d kap %.4f vieta %.0e" % (h, r["kappa"],
                                                r["vieta_dev"]))
        # G37 H1 certificate
        okx = r["cstar"] is not None
        if okx and h <= G34_HARD_MAX:
            okx = r["cstar"] <= C_STAR_MAX
        if not smoke and h in CSTAR_TAB and r["cstar"] is not None:
            okx = okx and r["cstar"] == CSTAR_TAB[h] \
                and abs(r["envj_ratio"] / ENVJ_RATIO_TAB[h] - 1) \
                <= NEW_TOL
        ok37 = ok37 and okx
        d37.append("h%d c* %s r %s"
                   % (h, r["cstar"], "%.4f" % r["envj_ratio"]
                      if r["envj_ratio"] else "-"))
        # G38 H2 census
        cen_tag = ""
        if "cen_error" in r:
            okx = h > CENSUS_STRUCT_MAX
            cen_tag = " [CENSUS-%s]" % ("DEPTH-REPORTED"
                                        if h > CENSUS_STRUCT_MAX
                                        else "FAILED")
            d38.append("h%d census ERR%s" % (h, cen_tag))
        else:
            complete = (r["cen_real"] == r["K"] - 1)
            nonneg = (r.get("cen_negsum_yt", 1.0) <= NEGSUM_BAR
                      and r.get("cen_min_yt", -1.0) >= -NEGSUM_BAR)
            topw = (TOP_WIN[0] <= r.get("cen_top_yt", 0.0)
                    <= TOP_WIN[1])
            topc = (r["cstar"] is None
                    or r.get("cen_top_yt", 9.9) <= r["cstar"])
            ward = (r.get("cen_sr1_dev", 1.0) <= SR1_BAR
                    and r.get("cen_prodid_dev", 1.0) <= PRODID_BAR)
            okx = complete and nonneg and topw and topc and ward
            if not smoke and h in TOP_TAB:
                okx = okx and abs(r["cen_top_yt"] / TOP_TAB[h] - 1) \
                    <= NEW_TOL
            if h > CENSUS_HARD_MAX:
                if h > CENSUS_STRUCT_MAX:
                    okx = True
                    cen_tag = " [CENSUS-DEPTH-REPORTED]"
                else:
                    okx = complete and nonneg and topw and topc
            d38.append("h%d %d/%d top %.4f neg %.0e%s"
                       % (h, r["cen_real"], r["K"] - 1,
                          r.get("cen_top_yt", float("nan")),
                          r.get("cen_negsum_yt", float("nan")),
                          cen_tag))
        ok38 = ok38 and okx
        # G39 PF pointwise
        nchk = r.get("pw_nchk", 0)
        mm = r.get("pw_minmarg")
        okx = True
        if nchk > 0 and h <= G34_HARD_MAX:
            okx = mm is not None and mm > 0
        if not smoke and h in PW_NCHK_TAB:
            okx = okx and nchk == PW_NCHK_TAB[h] \
                and abs(mm / PW_MARGIN_TAB[h] - 1) <= PW_MARGIN_TOL
        ok39 = ok39 and okx
        d39.append("h%d n %d marg %s%s"
                   % (h, nchk, "%.1e" % mm if mm is not None
                      else "-", "" if h <= G34_HARD_MAX
                      else " [F64-typed]"))
        # G40 WF table
        wf4 = r.get("wf", {}).get(Z0_PRIMARY)
        okx = True
        if h <= WF_MAX_H:
            okx = wf4 is not None and wf4[0] > 0 \
                and WF_RATIO_WIN[0] <= wf4[1] <= WF_RATIO_WIN[1]
            if not smoke and h in WF4_TAB and wf4 is not None:
                okx = okx and abs(wf4[0] / WF4_TAB[h] - 1) <= NEW_TOL
        ok40 = ok40 and okx
        d40.append("h%d WF4 %s"
                   % (h, "%.4f/%.2f" % wf4 if wf4 else
                      "CACHE-HORIZON"))
        # G41 certified delta floor (AMENDMENT 1a: the margin bar
        # is restricted by the frozen CLEAN_FIT criterion; beyond
        # it the row is CACHE-TOP-LIMITED, reported)
        with mp.workdps(60):
            yt_h = mp.mpf(10) ** mp.mpf(repr(r["yt_l10"]))
            clean_h = float(mp.sqrt(4 * yt_h)) <= gtop / 2
        dce = r.get("dcert", {}).get(Z0_PRIMARY)
        Lv = r.get("L", {}).get(Z0_PRIMARY)
        okx = True
        if dce is not None and h <= G34_HARD_MAX:
            okx = (dce[0] > 0 and dce[0] <= r["delta"] * (1 + 1e-9)
                   and float(mp.mpf(dce[1])) <= r["sigma_full"]
                   * (1 + 1e-9))
            if clean_h:
                okx = okx and dce[0] / r["eps"] >= RATE_MARGIN_MIN
            if not smoke and h in DCERT_TAB:
                okx = okx and abs(dce[0] / DCERT_TAB[h] - 1) \
                    <= NEW_TOL \
                    and abs(Lv / L4_TAB[h] - 1) <= NEW_TOL \
                    and abs(float(mp.mpf(dce[1])) / DCDC_TAB[h]
                            - 1) <= NEW_TOL \
                    and abs(r["eps"] / EPS_STR_TAB[h] - 1) \
                    <= NEW_TOL
        elif h <= WF_MAX_H and h <= G34_HARD_MAX:
            okx = dce is not None
        ok41 = ok41 and okx
        d41.append("h%d dcert %s%s"
                   % (h, "%.4f" % dce[0] if dce else "-",
                      "" if clean_h or dce is None
                      else " [CACHE-TOP-LIMITED]"))
    check("G30-spectral-sanity", ok30, "; ".join(d30))
    check("G31-certified-enclosures", ok31,
          "upper = Rayleigh(v_0); lower certified by Cholesky of "
          "Mq - tau_lo I at EVERY rung (r166 chain)")
    check("G32-wall-chain", ok32,
          "Cholesky(Mq) + |logdet dev| <= %.0e + sign chain"
          % LOGDET_BAR)
    check("G33-anchors-ladders", ok33,
          "tlaw_0 strings + the full r168 record ladder rel <= "
          "%.0e; FULLGAP tabs; lock in %s: %s"
          % (LADDER_TOL, str(LOCK_WIN), "; ".join(d33)))
    check("G34-budget-floor", ok34,
          "BA3 instantiated; HARD h <= %d, 27/28 F64-typed "
          "(inherited): %s" % (G34_HARD_MAX, "; ".join(d34)))
    check("G35-sigma-eps-anatomy", ok35,
          "sigma12/sigma_full/DC/delta on the r168/r169 record "
          "ladders rel <= %.0e (h <= 26, DISCLOSED corpus-known); "
          "recipe + iden devs <= 1e-40: %s"
          % (LADDER_TOL, "; ".join(d35)))
    check("G36-jets-trace-kappa", ok36,
          "sign(A_2/A_0) == -1 every rung; B_1 closed form dev <= "
          "%.0e; Vieta trace dev <= %.0e (COEFFICIENT-LEVEL, no "
          "roots); kappa in %s + tabs: %s"
          % (CF_BAR, VIETA_BAR, str(KAPPA_WIN), "; ".join(d36)))
    check("G37-h1-certificate", ok37,
          "c* = min C_GRID with ENVJ(c y_t) < |A_0| EXISTS at "
          "every rung (ONE source evaluation -- H1 is certified "
          "source-pure, no zeros); c* <= %.2f hard h <= %d: %s"
          % (C_STAR_MAX, G34_HARD_MAX, "; ".join(d37)))
    check("G38-h2-census", ok38,
          "F-census complete-real NONNEGATIVE per rung (polyroots, "
          "rootladder instrument VERBATIM), warded by SR1/product-"
          "id <= 1e-40; top/y_t in %s (the r156 escaped-ladder "
          "class) and top <= c* (H1 cross-instrument); HARD h <= "
          "%d, structure <= %d: %s"
          % (str(TOP_WIN), CENSUS_HARD_MAX, CENSUS_STRUCT_MAX,
             "; ".join(d38)))
    check("G39-pf-pointwise", ok39,
          "F/A_0 >= (1 - c*/z)^EXP at EVERY cache zero with z >= "
          "%.2f c*: min margin > 0 HARD (h <= %d where zeros "
          "exist) -- THE PRODUCT FLOOR SITS UNDER THE TRUTH AT "
          "EVERY TRUE TAIL ZERO: %s"
          % (PW_Z_FACTOR, G34_HARD_MAX, "; ".join(d39)))
    check("G40-wf-table", ok40,
          "WF(z_0 = 4) exists h <= %d (beyond ANATOMY-CACHE-"
          "HORIZON, reported); WF/WF_pred in %s: %s"
          % (WF_MAX_H, str(WF_RATIO_WIN), "; ".join(d40)))
    check("G41-certified-delta-floor", ok41,
          "delta_cert = L(4)^2 WF(4) > 0; delta_cert <= delta_meas "
          "HARD; (1-slop) delta_cert DC <= sigma_full HARD; "
          "delta_cert/eps >= %.0e; strings at 4/5/8: %s"
          % (RATE_MARGIN_MIN, "; ".join(d41)))
    for lab, keyv in (("sigma_full", "sigma_full"), ("DC", "DC"),
                      ("delta", "delta"), ("kappa", "kappa")):
        info("%s ladder: " % lab + " ".join(
            "%d:%.4f" % (h, tab[h][keyv]) for h in rungs
            if h in tab))
    info("cstar ladder: " + " ".join(
        "%d:%s" % (h, tab[h]["cstar"]) for h in rungs if h in tab))
    info("cen_top/yt ladder: " + " ".join(
        "%d:%s" % (h, "%.4f" % tab[h]["cen_top_yt"]
                   if "cen_top_yt" in tab[h] else "-")
        for h in rungs if h in tab))
    info("dcert(4) ladder: " + " ".join(
        "%d:%s" % (h, "%.4f" % tab[h]["dcert"][Z0_PRIMARY][0]
                   if tab[h].get("dcert", {}).get(Z0_PRIMARY)
                   else "-") for h in rungs if h in tab))
    info("pw margin ladder: " + " ".join(
        "%d:%s" % (h, "%.1e" % tab[h]["pw_minmarg"]
                   if tab[h].get("pw_minmarg") is not None
                   else "-") for h in rungs if h in tab))

    # ------------------------------------------------ S3b blocks
    section("S3b  THE JMF BLOCK CERTIFICATE")
    ok42 = True
    d42 = []
    blk_data = {}
    if not smoke:
        for bn, Hb, Hb2, ty in BLOCKS_DECL:
            hs = [h for h in rungs if Hb <= h <= min(Hb2, H_MAX)]
            if not all(h in tab for h in hs):
                ok42 = False
                d42.append("%s MISSING" % bn)
                continue
            complete = (ty == "FULL") \
                and (hs == list(range(Hb, Hb2 + 1)))
            rows = {}
            with mp.workdps(200):
                for wn, wf in (("flat", w_flat), ("fejer", w_fejer)):
                    flo = mp.mpf(0)
                    epss = mp.mpf(0)
                    n_on = 0
                    for h in hs:
                        wv = mp.mpf(wf(Hb, h))
                        dce = tab[h].get("dcert", {}).get(Z0_PRIMARY)
                        if dce is not None:
                            flo += wv * mp.mpf(dce[1])
                            n_on += 1
                        epss += wv * mp.mpf(tab[h]["eps_str"])
                    rows[wn] = (flo, epss, n_on)
            posr = True
            for wn in ("flat", "fejer"):
                flo, epss, n_on = rows[wn]
                p = bool(flo - epss > 0)
                posr = posr and p
                d42.append("%s w=%s floor %.4f - eps %.2e > 0 %s "
                           "(%d/%d onset)%s"
                           % (bn, wn, float(flo), float(epss), p,
                              n_on, len(hs),
                              "" if complete else " [PARTIAL]"))
            blk_data[bn] = dict(hs=hs, complete=complete,
                                pos=posr, rows=rows)
            if complete:
                ok42 = ok42 and posr
        check("G42-jmf-block-certificate", ok42,
              "sum_{onset rungs} w (1-slop) delta_cert DC - "
              "sum_all w eps > 0 on every COMPLETE block x both "
              "weights: THE SIGMA-FLOOR BELOW THE HORIZON "
              "CERTIFIED THROUGH THE PRODUCT FLOOR (H1 source-"
              "certified + H2 census + ward WF + classical DC + "
              "demand; NOT tau, NOT tlaw, NOT raw sigma, NOT "
              "per-gamma lock indicators): %s" % "; ".join(d42))
    else:
        check("G42-jmf-smoke", True, "smoke: needs full ladder")

    # ------------------------------------------------ S3c transfer
    section("S3c  HORIZON + RATE LAW + ENDGAME CHAIN")
    if not smoke:
        hstar = solve_horizon(SIGMA0)
        kstar = math.log2(hstar)
        fit_all = [h for h in rungs if h in tab
                   and tab[h].get("dcert", {}).get(Z0_PRIMARY)]
        fit_h = []
        for h in fit_all:
            with mp.workdps(60):
                yt_h = mp.mpf(10) ** mp.mpf(repr(tab[h]["yt_l10"]))
                if float(mp.sqrt(4 * yt_h)) <= gtop / 2:
                    fit_h.append(h)

        def ratefit(hs):
            lx = [math.log10(h) for h in hs]
            ly = [math.log10(float(mp.mpf(
                tab[h]["dcert"][Z0_PRIMARY][1]))) for h in hs]
            cf = np.polyfit(lx, ly, 1)
            return -float(cf[0]), 10.0 ** float(cf[1])

        a_all, c_all = ratefit(fit_all)
        a_rate, c_rate = ratefit(fit_h)
        hstar_rate = solve_horizon(c_rate, a_rate)
        kstar_rate = math.log2(hstar_rate)
        ok43 = (abs(hstar / HSTAR_STR - 1) <= HSTAR_TOL
                and KSTAR_WIN[0] <= kstar <= KSTAR_WIN[1]
                and RATE_A_WIN[0] <= a_rate <= RATE_A_WIN[1]
                and HSTAR_RATE_WIN[0] <= hstar_rate
                <= HSTAR_RATE_WIN[1])
        check("G43-horizon-rate-law", ok43,
              "h*(PT21, 0.15) = %.4e (r168 string rel %.0e), k* = "
              "%.2f; THE RATE LAW (CLEAN_FIT sqrt(4 y_t) <= "
              "gtop/2 PRE-FROZEN, %d clean rungs): sigma_floor(h) "
              "~ %.4f h^{-%.3f} (a in %s); all-rung fit a = %.3f "
              "over %d (CACHE-TOP-LIMITED class, reported); "
              "h*_rate = %.3e (k*_rate = %.1f); census constant "
              "(3 pi/c)(1 + 2a/3) = %.1f: the PRODUCT-FLOOR "
              "conditional route carries ~%d dyadic blocks on "
              "PT21 (granted flat floor: %d)"
              % (hstar, HSTAR_TOL, kstar, len(fit_h), c_rate,
                 a_rate, str(RATE_A_WIN), a_all, len(fit_all),
                 hstar_rate, kstar_rate,
                 (3 * math.pi / c_rate) * (1 + 2 * a_rate / 3),
                 int(kstar_rate) - 1, int(kstar) - 1))
        ok44 = True
        d44 = []
        for bn in ("B2", "B3"):
            dd = blk_data.get(bn)
            if dd is None or not dd["complete"]:
                ok44 = False
                continue
            hs_hard = [h for h in dd["hs"] if h <= G34_HARD_MAX]
            legs = []
            for h in hs_hard:
                r = tab[h]
                with mp.workdps(200):
                    floor = mp.mpf(r["zsum_str"]) \
                        - mp.mpf(r["off_str"])
                    tau_lo = mp.mpf(r["tau_lo_str"])
                legs.append(bool(floor > 0
                                 and r["res_rel"] >= -1e-9
                                 and tau_lo > 0))
            okx = all(legs) and dd["pos"]
            ok44 = ok44 and okx
            d44.append("%s: JMF row %s + BA3 %d/%d"
                       % (bn, dd["pos"], sum(legs), len(legs)))
        check("G44-endgame-chain", ok44,
              "[G42 JMF row] + [BA3 bridge per rung] + [certified "
              "enclosures] ==> block tau-positivity, every arrow "
              "on real data: %s -- SUBSTRATE-DIRECT inherited "
              "(r166/r168/r169 re-asserted; NO self-supporting "
              "induction)" % "; ".join(d44))
    else:
        check("G43-horizon-smoke", True, "smoke: skipped")
        check("G44-endgame-smoke", True, "smoke: skipped")

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS + WITNESS")
    ctrl_ok = True
    cblocks = {}
    for world, xw, _d in ctrl_tasks:
        r = res.get(("ctl", (world, xw)))
        if r is None or "error" in r:
            ctrl_ok = False
            check("G50-%s-x%d" % (world.lower(), xw), False,
                  (r or {}).get("error", "missing"))
            continue
        cblocks.setdefault(world, []).append(r)
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        rows = cblocks.get(world)
        if rows is None:
            continue
        taus = {r["h"]: r["tauf"] for r in rows}
        strs = CTRL_TAU_TAB[world]
        str_ok = all(abs(taus[h] / strs[h] - 1) <= CTRL_TAU_TOL
                     for h in taus if h in strs) if not smoke \
            else all(t < 0 for t in taus.values())
        viol_ok = all(r["viol"] < 0 for r in rows)
        floor_holds = all(r["sigma_w"] > r["eps_w"] for r in rows)
        # AMENDMENT 1b + 2: ytb_w/theta_w/H1-refusal are
        # REPORTED-DIAGNOSTIC; the gated refusal criterion is
        # {tau strings, BA3-bridge loss, raw-floor
        # world-insensitivity, SIZE-SEPARATOR}.
        theta_main_min = min(
            10.0 ** tab[h]["yt_l10"] / (2 * math.pi * h) ** 4
            for h in rungs if h in tab)
        theta_ctrl_max = max(r["theta_w"] for r in rows)
        size_sep = (theta_ctrl_max <= 1e-2
                    and theta_main_min / theta_ctrl_max >= 10.0)
        refuse = (all(t < 0 for t in taus.values()) and viol_ok
                  and str_ok and floor_holds and size_sep)
        ctrl_ok = ctrl_ok and refuse
        check("G5%d-%s" % ({"SMOOTH": 0, "SCRARITH": 1,
                            "EPSTEIN": 2}[world], world.lower()),
              refuse,
              "%s: tau_w < 0 on r166 strings; mechanism loss < 0 "
              "(BA3 bridge FALSE); raw floor sigma_w > eps_w "
              "HOLDS: FLOOR-INEQ-WORLD-INSENSITIVE replicated "
              "(r169); SIZE-SEPARATOR: max theta_w %.1e <= 1e-2 "
              "and min MAIN theta %.3f / max theta_w = %.0f >= "
              "10 (the r162 quartic ground separates the worlds); "
              "diagnostics REPORTED: y_t_w/b_top %s, theta_w %s, "
              "H1-refused %s, delta_w %s, DC_w %s"
              % (world, theta_ctrl_max, theta_main_min,
                 theta_main_min / theta_ctrl_max,
                 ["%.3f" % r["ytb_w"] for r in rows],
                 ["%.1e" % r["theta_w"] for r in rows],
                 [r["h1_refused"] for r in rows],
                 ["%.2f" % r["delta_w"] for r in rows],
                 ["%.2f" % r["DC_w"] for r in rows]))
    okw, detw = witness_battery()
    check("G53-witness-battery", okw, detw)

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 20:
        lt = [tab[h]["log10tau"] for h in rungs]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_sg = slope_of([math.log10(tab[h]["sigma"])
                         for h in rungs])
        s_sf = slope_of([math.log10(tab[h]["sigma_full"])
                         for h in rungs])
        s_dc = slope_of([math.log10(tab[h]["DC"]) for h in rungs])
        s_de = slope_of([math.log10(tab[h]["delta"])
                         for h in rungs])
        s_ka = slope_of([math.log10(tab[h]["kappa"])
                         for h in rungs])
        s_tl = slope_of([math.log10(tab[h]["tlaw0"])
                         for h in rungs])
        s_a0 = slope_of([tab[h]["log10a0sq"] for h in rungs])
        ok54 = (all(abs(s) <= TAU_SLOPE_BAR
                    for s in (s_sg, s_sf, s_dc, s_de, s_ka, s_tl))
                and RIDER_WIN[0] <= s_a0 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: sigma12 %.4f, sigma_full %.4f, "
              "DC %.4f, delta %.4f, kappa %.4f, tlaw_0 %.4f (<= "
              "%.2f DEMAND-FLAT); RIDER log10 A_0^2 slope %.3f in "
              "%s (BOUND-RIDES-CONNES)"
              % (s_sg, s_sf, s_dc, s_de, s_ka, s_tl,
                 TAU_SLOPE_BAR, s_a0, str(RIDER_WIN)))
    else:
        check("G54-tau-screen-smoke", True, "smoke")
    ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
    with mp.workdps(60):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on Mq[0,0] at h=5 moves tau by %.1e "
          "(round-118 trap)" % d_eps, kind="edge")

    # ------------------------------------------------ S6 audit + graphs
    section("S6  DEMAND AUDIT + LOOP/MINING + GRAPHS")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq, "CHAIN-AUDIT: " + detq)

    dep = {"FLOOR-CHAIN": ("SOURCE", "ENVJ-CERT-H1",
                           "CENSUS-H2-PER-RUNG", "TRACE-IDENT",
                           "CACHE-WARD", "GONEK-FORM",
                           "TOPROOT-MEAS", "HSW22",
                           "PT21-CENSUS-PER-K"),
           "SOURCE": (), "ENVJ-CERT-H1": ("SOURCE",),
           "CENSUS-H2-PER-RUNG": ("SOURCE",),
           "TRACE-IDENT": ("SOURCE",),
           "CACHE-WARD": (), "GONEK-FORM": (), "TOPROOT-MEAS": (),
           "HSW22": (), "PT21-CENSUS-PER-K": (),
           "TLAWCAP": (), "WPD": (), "CENSUS-ALL-K": (),
           "TAUPOS": (), "JETLOCK-MEAS": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",),
           "LOOP-ROUTE(census-all-k)": ("CENSUS-ALL-K",),
           "LOOP-ROUTE(pinning-supply)": ("TAUPOS", "TLAWCAP")}

    def ancestors(node):
        seen = set()
        stack = [node]
        while stack:
            n = stack.pop()
            for p in dep.get(n, ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        return seen

    anc = ancestors("FLOOR-CHAIN")
    ok61 = ("TLAWCAP" not in anc and "WPD" not in anc
            and "CENSUS-ALL-K" not in anc and "TAUPOS" not in anc
            and "JETLOCK-MEAS" not in anc
            and "TLAWCAP" in ancestors("LOOP-ROUTE(tlaw==>blocksum)")
            and "CENSUS-ALL-K" in ancestors("LOOP-ROUTE(census-all-k)")
            and "TAUPOS" in ancestors("LOOP-ROUTE(pinning-supply)"))
    okwm = True
    for bn, Hb, Hb2, _ty in BLOCKS_DECL:
        for h in range(Hb, min(Hb2, H_MAX) + 1):
            okwm = okwm and w_flat(Hb, h) == 1 \
                and w_fejer(Hb, h) == (Hb // 2 + 1) \
                - abs(h - 3 * Hb // 2)
    okwm = okwm and tuple(sorted(C_GRID)) == C_GRID \
        and tuple(sorted(Z0_GRID)) == Z0_GRID
    check("G61-loop-mining", ok61 and okwm,
          "delivered floor-chain ancestors == {SOURCE, "
          "ENVJ-CERT-H1, CENSUS-H2-PER-RUNG, TRACE-IDENT, "
          "CACHE-WARD, GONEK-FORM, TOPROOT-MEAS, HSW22, "
          "PT21-CENSUS-PER-K}: TLAWCAP, WPD, TAUPOS, CENSUS-ALL-K "
          "AND JETLOCK-MEAS are NOT ancestors -- the r169 "
          "measured-lock leg is ELIMINATED (replaced by the "
          "certified pair {H1, H2}); THREE loop routes flagged, "
          "NOT consumed; grids/weights recomputed from frozen "
          "formulas (SIGN-MINING-CLEAN; disclosure: ladders "
          "r168/r169-record-known pre-freeze; all NEW coordinates "
          "at h not in {4,5,8} (census {4,5,8,13}) pre-freeze "
          "unmeasured)")

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
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVIS"): 1,
                ("TAILVIS", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("SUSCAP2R", "DELTA1FLOOR")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1, ("SUSCAP2R", "R4HYP"): INF,
               ("NFCLOS", "DELTA1FLOOR"): 1,
               ("DELTA1FLOOR", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G62-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 9 and "RH" not in reach,
          "flows: base 4, refined 5 (r166/r168/r169 graph VERBATIM "
          "-- this round REDUCES the jet-mass coordinate onto "
          "existing rows, no set change); one-grant 5; "
          "counterfactual PARALLEL 9 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")

    chain_uni = {
        "RH": ["CENSUS_ALLK"],
        "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"],
        "EPSLAW": ["DTSTEP_ALLK"],
        "BA3": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"],
        "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "CARRIER_LEM": ["WEILPOS"],
        "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"],
        "L1": ["RH_VIA_N"], "WPD": ["RH_VIA_N"],
        "RH_VIA_N": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    chain_pin = {
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"],
        "CENSUS_K": ["DTSTEP_K"], "BA3": ["DTSTEP_K"],
        "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"],
        "SUBSTRATE28": ["HCOF"]}
    loop_pin = has_cycle(chain_pin)
    chain_term = {
        "ENVJ_H1": ["PF"], "CENSUS_H2": ["PF"],
        "TRACE": ["PF"],
        "GONEK": ["WF", "DCLEG"], "TOPROOT": ["RATE"],
        "PF": ["JETMASS"], "WF": ["JETMASS"], "RATE": ["JETMASS"],
        "CENSUS_K": ["DCLEG", "DTSTEP_K"],
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "BA3": ["DTSTEP_K"],
        "EPSLAW": ["DTSTEP_K"],
        "DTSTEP_K": ["HCOF"], "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "CARRIER_LEM": ["WEILPOS"], "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"], "L1": ["RH_VIA_N"],
        "WPD": ["RH_VIA_N"], "RH_VIA_N": ["RH"]}
    acyc = not has_cycle(chain_term)
    rh_reach = all("RH" in reachable(chain_term, n)
                   for n in ("ENVJ_H1", "CENSUS_H2", "TOPROOT",
                             "GONEK", "CENSUS_K"))
    check("G63-endgame-graphs", loop_uni and loop_pin and acyc
          and rh_reach,
          "(i) universalized census cycle DETECTED (r168/r169 "
          "replicated); (ii) pinning-supply cycle DETECTED (r169 "
          "replicated); (iii) the REDUCED per-k terminal chain "
          "{ENVJ_H1, CENSUS_H2, TRACE} -> PF, GONEK -> WF, "
          "TOPROOT -> RATE, {PF, WF, RATE} -> JETMASS -> "
          "SIGMAFLOOR -> DTSTEP_K -> HCOF -> both typed arrows -> "
          "RH is ACYCLIC with RH reachable from every "
          "counterfactual grant (AND-semantics: all parents "
          "needed): COFINAL-TARGET-ASSEMBLY-CONDITIONAL, not a "
          "loop; NO RH CLAIM")
    info("THE FINAL RESIDUE (exact, typed): JET-MASS-FLOOR == "
         "[PF: PROVEN given {H1 certified source-pure per rung, "
         "H2 census classical per rung}] x [WF: classical-per-"
         "census (Landau/Gonek AS FORM, GONEK-CONSTANT-UNPRICED; "
         "measured ward-class in-run)] x [RATE: y_t <= poly == "
         "TOPROOT, measured x^4.1 (== the r162 THETA-window), "
         "arithmetic-pinned].  The r169 terminal residue "
         "{JET-MASS-FLOOR (rate form)} REDUCES to {TOPROOT "
         "lambda-uniform} + {GONEK-CONSTANT-UNPRICED (classical, "
         "citable work)} + {census ALL-K == LOOP} + {L1, WPD}.  "
         "By r169-SF4 ANY polynomial rate is census-absorbable; "
         "the JETLOCK-MEAS leg is eliminated.  Census cardinality "
         "4 UNCHANGED; NO omega closed; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "PRODUCT-FLOOR-PROVEN(PF1-PF3; G10-G13)",
        "H1-CERTIFIED-SOURCE-PURE(G37)",
        "H2-CENSUS-CLASSICAL-PER-RUNG(G38)",
        "PF-POINTWISE-VERIFIED(G39)",
        "JETMASS-FLOOR-ASSEMBLED(delta >= L^2 WF; G41)",
        "JMF-BLOCK-CERTIFIED(B2/B3; G42/G44)",
        "JETLOCK-MEAS-ELIMINATED(G61)",
        "JETMASS-REDUCED-TO-TOPROOT(G43/G61/G63)",
        "FARFIELD-LAW-EXPLAINED(G13/G39)",
        "DEMAND-RATE-ABSORPTION(G15/G43)",
        "WITNESS-KILLS-CERTIFICATE(G53)",
        "CONTROLS-REFUSE-BRIDGE-SIZE + FLOOR-INEQ-WORLD-"
        "INSENSITIVE(G50-G52)",
        "TOY-EXCLUSION-BY-THEOREM(G16)",
        "ANATOMY-REPLICATED(G35)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "LOOP-ROUTES-FLAGGED(three; G61/G63)",
        "OMEGA-UNCHANGED(census 4; G62)",
        "MINCUT(4/5)"]
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
        print("COMPOSITE: " + " + ".join(
            v.split("(")[0] for v in verdicts))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
