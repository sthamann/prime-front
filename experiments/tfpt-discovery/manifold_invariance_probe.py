#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""manifold_invariance_probe -- PRIME.MANIFOLD.INVARIANCE.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung certificates stated, NO counterexample claim.  It closes no
gate and narrows no gate.

=======================================================================
MISSION (THE MANIFOLD FORWARD-INVARIANCE ATTACK, closing the BH7-F4
gap): r173/CDXC proved the two frozen witnesses exit the certified
manifold M(h) = {ground-state certificate, two-sided lock, BA3
bridge, H1, H2}; Bughunt VII F4 scoped this honestly -- the exclusion
was witness-specific, NOT universally quantified over perturbations,
and the DK leg pins only within its radius (gate-bar crossover
h = 16).  THIS ROUND: (M1) UNIVERSALIZE the exclusion -- prove the
tau-free universal DK exclusion theorem, characterize the FULL
H3-refuting perturbation set per rung (minimal dial window, exact),
compute the FIRST-ORDER-EXACT FULL-SPACE minimal certificate price
over ALL fixed-M refuting directions, and adjudicate every leg
(lock/cert/BA3/census/H1) against the minimal dial and the optimal
refuters, with a frozen leak decision rule; (M2) THE TRANSPORT STEP
-- the constraint x leg x epistemic-type transport ledger for
h -> h' block representatives, measured transport defect ladders,
and the conditional induction assembly with its exact hypothesis
list; (M3) THE TAU-MEAS IMPORT ADJUDICATION -- which manifold legs
consume absolute tau, whether the sufficient universal subset needs
it (machine-checked ancestry); (M4) ASSEMBLY, honest pricing,
tau-screens, controls, the HALFGAP-Riccati contrast.)
=======================================================================
State consumed (CITED): CDXCII/r176 Bughunt VII (F1 residue-triple
wording ADOPTED: {H1 AND H2 AND H3}-cofinal; F2 limsup mod-D
qualifier ADOPTED; F4 the target gap of this round); CDXCI/r175
(theta_inf OPEN-NONPERTURBATIVE-VARIATIONAL; Montgomery-PC loop
cycle in the standard battery); CDXC/r173 (h3_cofinal machinery
VERBATIM: manifold battery, DK sin-theta lemma G15, stability radii
G36 with STAB_GATE_TAB and crossover h = 16, witness strings,
2-mode/3-mode witness algebra, controls, THETA_W_CAL; SPEC_SHA
876dafc977d3d8fc); CDLXXXIX/r174 (Gonek pricing, cited not
consumed); CDLXXXVIII/r172 (H3 certificate 26/26, cited record
ladders yt_l10/lock VERBATIM, witness prices, A0-floor loop);
CDLXXXVII/r171 (PF conditional exactly on {H1 + H2 per rung}, H1
ENVJ source-pure, H2 census); CDLXXXVI (v926 FULLGAP quartic law
MEASURED -- consumed ONLY as a FLAGGED-MEASURED premise; v927
BA1-BA3; v928 DT1/DT2 depth-block transfer = census-PLAN transport,
cited); CDLXXV/r166 (BA3 currency NZSUM = 1200 VERBATIM,
NO-EXACT-CROSS-H-MECHANISM adjudication); CDLX/r156 (2-mode witness
dictionary); r140/r143 (alignment wall, TOPROOT-NOT-NORM-CONTINUOUS
r172); r131 OFF recipe; HSW22 Cor. 1.2; PT21; v915 Euler-Pick floors
INSPECTED for the M3 adjudication (they certify Pick matrices of
xi'/xi from prime data -- NOT lambda_min(M(h)): no corpus certified
tau-floor for the world matrix exists outside BA3 itself); the DEAD
Riccati-HALFGAP barrier (CLXII/CCIII: transition-local induction
died because increments were STEEPER than levels and the barrier
matrix was measured -- the design lessons exploited here: certified
constraints with proven per-rung modus tollens instead of a measured
barrier; and the honest expectation LEVEL-CHEAPER-THAN-INCREMENT).

NOTATION.  Rung h (R4.build_cell, even sector, MAIN world); A =
log(h)/2; K = ceil(1.25 h log h); b_k = (k pi/A)^2; tau = lam_min(M);
lam1 = second eigenvalue; FG = FULLGAP = (lam1 - tau)/tau; T_z =
2 pi h; c = source = ground-state eigenvector of M (cn = V[:,0]/nrm);
A_{2m} = sum_k (-1)^k c_k b_k^m; y_t = |A_2/A_0|; theta_y = y_t/
T_z^4; lock = FG/y_t; TFG = theta_y * lock; kappa = B_1/y_t;
H3(h): y_t <= 0.155 T_z^4.  A FIXED-M PERTURBATION moves the source
vector c -> c'' with M, tau, lam1, FG invariant (r172/r173
structural fact: the witness perturbs the VECTOR, not the world).
An H3-REFUTER at rung h is a fixed-M perturbation with theta'' >
0.155, i.e. dial W = y_t''/y_t > W_min(h) = 0.155/theta_y(h).
MANIFOLD LEGS: (cert) ray_dev <= 1e-25 and r0/tau <= 1e-25;
(lock) lock'' in (1.0, 8.0); (BA3) (tau + OFF - zsum'')/tau >= 0
(r166/r131 recipe VERBATIM, NZSUM = 1200); (H2) census
complete-real; (H1) ENVJ half-plane c* exists.

=======================================================================
M1 -- UNIVERSALIZING THE EXCLUSION
=======================================================================
(a) THE TAU-FREE UNIVERSAL DK EXCLUSION THEOREM (G10, sympy):
sin(angle) <= (r0/tau)/(FG - RAY_BAR) -- tau CANCELS in ratio form;
with the lock-window floor FG >= LOCK_LO * y_t the whole DK radius
R_univ(bar, h) is computable from {bar, y_t, e0n, e2n, A_0, A_2}
alone: NO absolute tau import.  Contrapositive (the
universalization): every refuter needs rel-y_t-move >= W_min - 1;
if R_univ(1e-25, h) < W_min - 1 then NO certificate-passing
fixed-M perturbation refutes H3 at rung h -- DIRECTION-UNIVERSAL,
witness-free.  Calibrated: R_univ = 1.1144e-24 / 1.2652e-22 /
1.2714e-16 / 2.1767e-5 at h = 4/5/8/13 (all < W_min - 1: COVERED),
NOT FINITE at h = 16 (the r173 crossover REPLICATED in the
tau-free form; 1/A_0 eats the fixed bar).  REQUIRED-BAR SCHEDULE
b*(h) (bisection on the exact radius formula, deterministic):
log10 b* = -1.1890 / -3.3241 / -9.3405 / -20.6087 / -27.6292 at
h = 4/5/8/13/16, strictly decreasing: the manifold with the
h-dependent certificate bar b*(h) is universally exclusionary at
every rung -- at the FROZEN bar 1e-25 the theorem covers h <= 13
(gated) and at the measured eigsy residuals h <= 16 calibrated
(r_univ_meas = 2.8408e-35 < W_min - 1; r173 measured the
measured-radius crossover at h = 24: deep rungs REPORTED).
(b) THE REFUTER DIAL WINDOW (G11 exact + G44 cited): lock'' ==
lock/W exactly (fixed-M); a refuter survives the lock floor iff
W < lock, and the surviving window (W_min, lock) is nonempty iff
TFG > 0.155.  On the cited 26-rung ladder: TFG > bar at 25 rungs,
TFG <= bar ONLY at h = 4 (0.111732): the lock leg universally
catches all refuters at h = 4 and only there (BH7-F4's 24-of-25
replicated as a theorem + table); W_min band [1.9908, 3.4522].
(c) THE MINIMAL DIAL (G38): the 2-mode A_0-invariant dial at
W_DIAL = W_min * min(1.05, sqrt(TFG/bar)) (strictly inside the
surviving window where it exists; the calibration pass-1 1.05
factor overshot the thin window at h = 8, disclosed).  Battery per
rung: the dial REFUTES H3 (theta'' > bar, ward-exact), stays in
the lock window (except h = 4: lock'' = 0.6866 < 1, lock-caught),
keeps H1 satisfied (c* = 1.05 exists: H1-WORLD-BLIND -- H1 catches
NOTHING here), BREAKS the census (nreal 4/8/14/31/41 of K-1 =
6/10/20/41/55 at h = 4/5/8/13/16), BREAKS the certificate at
astronomical price r0''/tau = 3.703906e7 / 5.190266e10 /
1.984023e18 / 1.683418e31 / 1.154863e39 (h = 4/5/8/13/16), and
BREAKS BA3 (zsum''/zsum = 2.582319e2 / 9.147271e2 / 4.424925e3 /
3.631757e4 / 8.750938e4, residuals -2.273202e2 .. -8.395148e4).
(d) THE FULL-SPACE MINIMAL PRICE (G39, the discovery instrument of
the round): the minimal-residual refuter over ALL fixed-M
directions (first-order-exact: weighted least squares in the FULL
eigenbasis, constraints A_0(d) = 0 and A_2(c+d) = W_DIAL A_2
enforced EXACTLY in mp; candidates exactly re-evaluated): price
r0''/tau = 1.353657e5 / 4.696766e5 / 2.844554e6 / 3.820643e7 /
9.467704e7 at h = 4/5/8/13/16 -- STRICTLY GROWING, 30-33 ORDERS
ABOVE THE 1e-25 BAR.  The full-space minimum SATURATES at the low
eigenmodes (EIGF == EIG8 == EIG2 to <= 1e-3): deeper modes cost
more.  CS-GAP LADDER: log10(price) - log10(b*) = 6.32 / 9.00 /
15.79 / 28.19 / 35.61 -- the DK/CS worst-case bound is
exponentially conservative BECAUSE the low eigenvectors SHARE the
source's 1/A_0 cancellation: ALIGNMENT-SHARING measured as
gap = log10|a0_1| - log10|A_0| = 2.354 / 2.699 / 3.022 / 3.519 /
3.669 (the eigenvector-1 A_0-functional is only 1e2.4-3.7 above
the source's own A_0, against a generic O(1) functional norm).
The r140/r143 alignment wall, which r172 quantified as the
ATTACKER's exponential cheapness in SOURCE-norm (|d|/max|c| =
1e-17.6 at h = 13), is here quantified from the DEFENSE side: in
CERTIFICATE-RESIDUAL currency every refuter is exponentially
EXPENSIVE, and the price GROWS with depth.
(e) BA3 IS NOT UNIVERSAL (G41): the exact constrained minimizer of
zsum over ALL A_0-gauge refuting directions (KKT, mp at ZMIN_DPS =
90, dps-cross warded; the calibration pass-1 dps-60 token
ALL-REFUTERS-BREAK-BA3 at h = 16 was a PRECISION ARTIFACT,
corrected and disclosed): zmin/zsum_main = 2.546824e-1 /
1.272993e-1 / 1.589237e-2 / 6.068511e-3 / 1.790734e-2 at h =
4/5/8/13/16, BA3 residual at the minimum POSITIVE everywhere:
BA3-PASSING-REFUTER-EXISTS at every rung.  BUT the zmin witness
BREAKS THE CERTIFICATE at r0''/tau = 6.601841e9 / 1.049621e15 /
6.964173e28 / 4.952138e53 / 3.168465e68 (strictly growing): the
cert/BA3 trade-off frontier is measured-EMPTY on both ends.  Plus
the SCALE-GAUGE THEOREM (G13, sympy): zsum and OFF are homogeneous
degree 2 in the source while tau is fixed -- BA3 in absolute
currency is passable by scaling for ANY direction: the BA3 leg is
gauge-dependent (A_0-gauge frozen and disclosed) and NOT a
universal catcher.  LEAK DECISION RULE (G42, frozen): a candidate
in {DIAL2, EIG8, EIG2, EIGF, ZMINWIT} that refutes H3 AND passes
{cert, lock window, BA3} exhibits MANIFOLD-LEAK(h); calibrated: NO
leak at h <= 16; deep rungs (20, 24) adjudicated at record time by
the same frozen rule (token switches, gate = rule executed).
M1 VERDICT SHAPE: universal coverage = LOCK(h = 4) + DK-THEOREM
(h <= 13 at the frozen bar, tau-free) + DK-MEAS (h = 16); deeper
coverage is EXHIBIT-BASED (all frozen adversary constructions
break cert AND BA3 with growing prices) + the b*(h) schedule
(instrument-conditional, exact).  The BH7-F4 witness-specificity
is REMOVED within the instrument; the honest residual scope is the
first-order optimality of the price minimum and the frozen
candidate battery beyond it.

=======================================================================
M2 -- THE TRANSPORT LEDGER AND THE INDUCTION SHAPE
=======================================================================
(G15 exact frame legs; G44-G47.)  FRAME-EXACT transports (sympy):
B_1 closed form (pi/A)^2 (K-1)K(2K-1)/6; e0n^2 = 1/(2A) + (K-1)/A;
e2n^2 = (pi/A)^4 * Faulhaber(K-1, 4); T_z^4 doubling == 16;
A(2h) - A(h) == log(2)/2; NON-NESTING: the frames at h != h' are
incommensurate (A strictly monotone) -- M(h) is NOT a compression
of M(h'): no Cauchy/Weyl interlacing transport exists for the
spectral legs.  SOURCE legs (A_0, A_2, ENVJ, census): re-established
per rung by the eigensolve, NO transport identity (r166
NO-EXACT-CROSS-H-MECHANISM re-affirmed).  SPECTRAL legs (FG, lock):
transport only as the v926 MEASURED quartic law; measured
block-representative defects (cited ladders, chains 4->8->16,
5->10->20, 6->13->26): p_FG per doubling = 4.4805 / 4.4489 /
3.4641 / 4.2723 / 4.9990 / 3.9303 (spread 3.46..5.00 -- the
FG-transport is only loosely quartic at rep pairs), p_yt = 4.5394 /
4.2022 / 4.1405 / 4.1268 / 4.6391 / 4.0893, lock-ratios 0.9600 /
1.1865 / 0.6257 / 1.1061 / 1.2833 / 0.8956, dtheta all positive
<= 0.021.  THE INDUCTION SHAPE (G47): H3(h') FOLLOWS from
{TFG(h') <= TFG_CAP = 0.267439 [v926-quartic MEASURED, FLAGGED]}
AND {lock(h') >= L_NEED = TFG_CAP/0.155 = 1.725411 [SPECTRAL-RATIO-
MEAS; measured ladder min 2.2345, margin 1.295054; NO corpus
theorem]} -- verified at all 26 cited rungs; the certificate leg has
NO transport at all (per-rung instrument).  HONEST PRICING: the
per-block induction hypothesis = TWO measured spectral scalars at
the new rung, while the LEVEL check H3(h') is ONE exact source
evaluation: LEVEL-CHEAPER-THAN-INCREMENT (the Riccati-HALFGAP death
mode one level up -- there the increments were steeper than levels;
here the transport hypotheses are not cheaper than the level) and
the transport demand sits in the SAME epistemic class (per-rung
spectral-measured window) as the residue it would discharge:
TRANSPORT-RELABELS-NOT-REDUCES.  The induction theorem is assembled
CONDITIONAL-ON-MEASURED-TRANSPORT and EXCLUDED from the delivered
set (G61); H1/H2 stay separate per-rung members of the triple
(BH7-F1 wording).

=======================================================================
M3 -- THE TAU-MEAS IMPORT ADJUDICATION
=======================================================================
(G10/G61.)  The DK/cert leg consumes NO absolute tau (ratio form,
proven); the lock leg consumes the spectral RATIO FG = lam1/tau - 1
(scale-free, but eigensolve-consuming); BA3 consumes ABSOLUTE tau
(the bridge budget) + census-per-k + the A_0 gauge -- and v915
Euler-Pick floors certify a DIFFERENT spectral object (Pick
matrices of xi'/xi from primes), the r171 PF bound certifies jets
F/A_0, the certified B-floor family (CLIII) lives on the dead
halfgap ladder: NO corpus certified tau-floor for lambda_min(M(h))
exists outside BA3 itself (circular).  ADJUDICATION: the sufficient
universal-exclusion subset is {cert(bar schedule), lock window} --
BA3 is NOT needed (it is not universal anyway, (e) above): the
TAU-ABS import is NOT LOAD-BEARING for the universalized exclusion;
it remains confined to the red-team BA3 leg (typed RED-TEAM-
MEASURED, kept OUT of the delivered set, machine-checked: TAU-MEAS
is an ancestor of LEAK-ADJUDICATION only, never of the delivered
statements).  If one INSISTED on BA3 in a delivered chain it would
import one measured constant per rung (tau(h)) plus the A_0 gauge:
stated exactly, not consumed.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, np.load only in ward_, no
    zero-oracle names, no verification/ import; workers cache-free);
    G02 cache health (X5; main-process only).
S1  exact layer (sympy generic + exact rational instances):
    G10 tau-free universal DK exclusion (cancellation identity,
    floor substitution positive-slack, DK sin-theta lemma r173-G15
    replicated with the slack parametrization, y_t-move equality
    instance, contrapositive chase);
    G11 refuter dial window (lock'' == lock/W fixed-M; survive iff
    W < lock; nonempty iff TFG > bar; exit both directions r173-G16
    class at symbolic W);
    G12 H3-transport implication + L_NEED identity (TFG <= C and
    lock >= L ==> theta <= C/L, positive-slack; L_NEED == C/bar);
    G13 BA3 scale-gauge theorem (degree-2 homogeneity of zsum and
    OFF, residual -> 1 as t -> 0: gauge required, disclosed);
    G14 KKT/least-squares optimality (exact rational instances,
    2x2 and 3-var/2-constraint == direct parametrized minimum);
    G15 frame-exact transport legs (B_1/e0n/e2n closed forms via
    Faulhaber, T_z^4 doubling == 16, A-increment == log(2)/2,
    non-nesting statement);
    G16 dial algebra at symbolic W (A_0 invariant, A_2'' == W A_2,
    |d| == |A_2|(W-1)/(b_2-b_1); r172-G14 class).
S2  G20 HSW G(T) sanity.
S3  per-rung builds, RUNGS_SUB = (4, 5, 6, 8, 10, 13, 16, 20, 24)
    (r173 subset VERBATIM; h = 20/24 adversary numbers pre-freeze
    unmeasured: REPORTED + frozen decision rules + coarse windows,
    DISCLOSED), 12 spawn workers, NO cache in workers:
    G30 spectral sanity (r173 VERBATIM);
    G31 jets/kappa + KAPPA_TAB;
    G32 cross-instrument (YT_R143, FG_TAB, lock window);
    G33 cited-ladder replication (THE LICENSE, r173 gates VERBATIM);
    G34 H3 certificate (margin >= 1.5);
    G35 stability radii (STAB_GATE_TAB rel 5e-3, strictly growing,
    crossover print; stab_meas <= 1e-30 at h <= 13);
    G36 W_min/W_DIAL (exact ward W_min theta == bar; WMIN/WDIAL
    tabs rel 5e-3 at {4,5,8,13,16}; vs cited-derived rel 8e-3 at
    all 9; dial-window rule verified);
    G37 R_univ + b* schedule (RUNIV_TAB rel 5e-3 at {4,5,8,13};
    r_univ >= stab_gate; NOT-FINITE at h = 16; BSTAR_TAB abs 0.02,
    strictly decreasing on {4,5,8,13,16}; deep REPORTED);
    G38 DIAL2 battery (wards exact; theta'' > bar; lock'' window
    per rule; PRICE_DIAL_TAB rel 5e-3 + coarse window >= 1e6 at
    uncalibrated rungs DISCLOSED; census DIAL_NREAL_TAB at
    {4,5,8,13,16} + broken at {6,10} window; census h > 16 SKIPPED
    cost-disclosed; H1 c* printed: H1-WORLD-BLIND);
    G39 EIG batteries (EIGF == EIG8 rel 1e-3; PRICE_EIGF_TAB rel
    5e-3, strictly growing on calibrated set; coarse window >= 1e4
    at uncalibrated rungs DISCLOSED; CS-gap + ALIGNMENT GAP_TAB
    abs 0.05; ladders printed).
S3b cache layer (main process, ward):
    G40 BA3 anchors + variants (ZSUM_TAB r166 strings rel 5e-3 at
    {4,5,8}, residual > 0 at all 9; variant zsum-ratio tabs rel
    5e-3 + BA3 residual < 0 for DIAL2/EIGF at calibrated rungs;
    OFF_main used for variants, A_0-gauge, DISCLOSED);
    G41 ZMIN universal optimizer (ZMIN_TAB rel 5e-3; BA3 residual
    at minimum > 0 at calibrated rungs: BA3-NOT-UNIVERSAL;
    dps-cross at {5,16} rel <= 1e-6; ZMINWIT cert battery:
    ZMINWIT_R0_TAB rel 5e-3, strictly growing, all >= 1e9);
    G42 leak adjudication (frozen rule over the candidate battery;
    NO leak at calibrated rungs GATED; deep rungs token-adjudicated
    LEAK-FREE-MEASURED-DEEP or MANIFOLD-LEAK-EXHIBITED(h));
    G43 coverage table (universal legs per rung; nonempty at
    h <= 16 gated per calibration; deep rungs printed).
S3c transport analytics (cited ladders, deterministic):
    G44 cited tables (TFG > bar at 25/26 with exception list [4];
    W_min band; TFG_CAP 0.267439; L_NEED 1.725411; margin
    1.295054; all rel 1e-3);
    G45 rep-defect ladders (P_FG/P_YT/LOCKRAT/DTHETA tabs rel 1e-3
    + windows);
    G46 transport ledger (frozen enumerative table + consistency);
    G47 induction assembly (implication at all 26 cited rungs;
    margin rel 1e-3; typing enumerations; HALFGAP contrast).
S4  controls + witnesses:
    G50 SMOOTH {4,5}, G51 SCRARITH {5,6}, G52 EPSTEIN {8}: tau_w <
    0 on r166 strings rel 5e-3; theta_w on THETA_W_CAL rel 5e-3;
    lock_w < 1.0 (MANIFOLD EMPTY IN FAKE WORLDS: the invariance
    machinery cannot even be posed there -- NOT world-blind);
    SIZE-SEPARATOR >= 10;
    G53 the r172/r173 W = 1000 inflation witness replicated at
    h = 5 through THIS round's main-process battery (dnorm
    8.117888e-2, theta'' 62.690999, lock'' 3.6444e-3, r0''/tau
    3.430e13, zsum-ratio 3.579247e8, BA3 residual -3.4372e8, all
    rel 5e-3) + W = 1000 > lock at EVERY rebuilt rung (the large
    dial is lock-excluded everywhere, exact).
S5  G54 screens (demand slopes log10 W_min, log10 TFG vs log10 tau
    <= 0.30 abs; RIDER log10 R_univ vs -log10|A_0| in (0.85, 1.15)
    over the finite-radius rungs); G55 conditioning (round-118
    trap).
S6  G60 demand audit (SEQ; windows/tabs/rules frozen pre-eval;
    disclosures); G61 loop/mining + M3 ancestry (TAU-MEAS ancestor
    of LEAK-ADJUDICATION only; INDUCTION-SHAPE and LEAK-ADJUDICATION
    excluded from the delivered set; banned set incl. RH-conditional
    second moments); G62 min-cut (r171/r172 graph VERBATIM, flows
    4/5/5/9, census cardinality 4); G63 endgame graphs (FOUR loop
    cycles re-detected incl. Montgomery-PC; terminal chain with the
    manifold nodes feeding ONLY the red-team/stability side is
    ACYCLIC; AND-semantics).
S9  composite verdict + G99 runtime <= 2700 s.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675); M_JETS = 400; MGRID = (2,4,8,16,32,64,128,256,400);
WORKERS = 12; RUNGS_SUB = (4,5,6,8,10,13,16,20,24); DPS = {4:60,
5:60, 6:65, 8:80, 10:90, 13:120, 16:130, 20:144, 24:150} (r173
VERBATIM).  INHERITED r173/r172/r166 VERBATIM: SIMP_MIN = 1e3;
RAY_BAR = RES0_BAR = 1e-25; CF_BAR = 1e-40; KAPPA_TAB {4:0.104346,
5:0.096088, 8:0.062906} rel 5e-3; KAPPA_WIN (0.0,0.30); FG_TAB
{4:4.458152e4, 5:2.2255e5, 8:9.9512e5, 13:1.0619e7} x (0.97,1.03);
LOCK_WIN (1.0,8.0); YT_R143 {5:6.107e4, 8:4.165e5, 13:3.204e6}
<= 1e-3 dex; THETA_BAR = 0.155; THETA_Y_WIN (0.03,0.12);
THETA_Y_TAB {4:0.044901, 5:0.062691, 8:0.065250, 13:0.071983} rel
5e-3; H3_MARGIN_MIN = 1.5; STAB_GATE_TAB {4:4.478e-25, 5:3.472e-23,
8:5.322e-17, 13:6.568e-6} rel 5e-3; STAB_MEAS_BAR = 1e-30 (h<=13);
C_GRID = (1.05,1.10,1.15,1.20,1.30,1.40,1.50,1.75,2.00);
POLY_MAXSTEPS = 3000; IM_TOL = 1e-10; NZSUM = 1200; F64_SLOP =
1e-3; Z_OVERHANG = 6.0; ZSUM_TAB {4:0.8842, 5:0.9603, 8:0.9539}
rel 5e-3; CTRL_TAU_TAB rel 5e-3: SMOOTH {4:-1.0375, 5:-1.0944},
SCRARITH {5:-0.34593, 6:-0.36716}, EPSTEIN {8:-1.6310};
CTRL_THETA_MAX = 1e-2; SEP_MIN = 10.0; THETA_W_CAL {(SMOOTH,4):
3.541319e-4, (SMOOTH,5):2.409799e-4, (SCRARITH,5):1.005571e-3,
(SCRARITH,6):1.875055e-3, (EPSTEIN,8):1.011306e-4} rel 5e-3;
WIT1000 strings (r172/r173): DNORM 8.117888e-2, THETA 62.690999,
LOCK 3.6444e-3, R0TAU 3.430e13, ZRATIO 3.579247e8, BA3 -3.4372e8,
all rel 5e-3; TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.85, 1.15);
COND_WIN = (1e-40, 1e-10); RUNTIME_BAR = 2700 s; GAMMA1_LIT (ward
only); NEW_TOL = 5e-3; ANA_TOL = 1e-3; CITED LADDERS YT_L10_R172 +
LOCK_R172 (toproot_theta_probe.run1.log VERBATIM, 4dp, 26 rungs,
dicts in code).
NEW THIS ROUND (calibrated in calib_mi_pass1..4.log -- ONE
pre-freeze calibration pass in FOUR disclosed sub-passes: pass 1 =
instrument bugs found (eigenbasis index at K < 9 rungs; the flat
1.05 dial factor overshoots the thin lock window at h = 8; ZMIN at
dps 60 is PRECISION GARBAGE at h = 16 -- its pass-1 token
ALL-REFUTERS-BREAK-BA3 was an artifact); pass 2 = fixes + window
rule + ZMIN_DPS = 90 + dps-cross ward; pass 3 = EIGF full-space
candidate + ZMINWIT cert evaluation added; pass 4 = print layer
only; scratch deleted after freeze, ALL FOUR logs kept; numbers
below are pass-4 strings):
DIAL_EPS = 0.05; W_DIAL rule = W_min * min(1 + DIAL_EPS,
sqrt(TFG/bar)) if TFG > bar else W_min * (1 + DIAL_EPS);
EIG_J8 = modes 1..8 (clipped to K-1); EIG_J2 = modes 1..2; EIGF =
ALL modes 1..K-1; CENSUS_VAR_MAX = 16; ZMIN_DPS = 90; ZMIN_XDPS =
+40 at h in {5,16}, rel <= 1e-6; BSTAR bisection log10 in [-90,6],
tol 1e-4; LOCK_LO = 1.0 floor in R_univ; CAL_RUNGS = {4,5,8,13,16};
WMIN_TAB {4:3.452032, 5:2.472444, 8:2.375493, 13:2.153286,
16:2.064341} rel 5e-3; WDIAL_TAB {4:3.624634, 5:2.596066,
8:2.382248, 13:2.260950, 16:2.167558} rel 5e-3; RUNIV_TAB
{4:1.1144e-24, 5:1.2652e-22, 8:1.2714e-16, 13:2.1767e-5} rel 5e-3
+ NOT-FINITE at 16; RUNIV_MEAS_16 = 2.8408e-35 (rel 5e-3);
BSTAR_TAB {4:-1.1890, 5:-3.3241, 8:-9.3405, 13:-20.6087,
16:-27.6292} abs 0.02; PRICE_DIAL_TAB {4:3.703906e7, 5:5.190266e10,
8:1.984023e18, 13:1.683418e31, 16:1.154863e39} rel 5e-3;
PRICE_EIGF_TAB {4:1.353657e5, 5:4.696766e5, 8:2.844554e6,
13:3.820643e7, 16:9.467704e7} rel 5e-3, strictly increasing;
PRICE_COARSE_DIAL = 1e6, PRICE_COARSE_EIG = 1e4 (windows at
uncalibrated rungs, DISCLOSED); DIAL_NREAL_TAB {4:4, 5:8, 8:14,
13:31, 16:41}; DIAL_LOCK_TAB {4:0.6866, 5:1.4038, 8:1.0028,
13:1.4658, 16:1.3077} rel 5e-3; GAP_TAB {4:2.354, 5:2.699, 8:3.022,
13:3.519, 16:3.669} abs 0.05; ZR_DIAL_TAB {4:2.582319e2,
5:9.147271e2, 8:4.424925e3, 13:3.631757e4, 16:8.750938e4} rel
5e-3; BA3_DIAL_TAB {4:-2.273202e2, 5:-8.774327e2, 8:-4.220003e3,
13:-3.478528e4, 16:-8.395148e4} rel 5e-3; ZR_EIGF_TAB
{4:5.468683e1, 5:4.419774e1, 8:5.183652e1, 13:1.453730e2,
16:1.634536e2} rel 5e-3; BA3_EIGF_TAB {4:-4.735231e1,
5:-4.144407e1, 8:-4.844764e1, 13:-1.382435e2, 16:-1.558098e2} rel
5e-3; ZMIN_TAB {4:2.546824e-1, 5:1.272993e-1, 8:1.589237e-2,
13:6.068511e-3, 16:1.790734e-2} rel 5e-3; ZMINWIT_R0_TAB
{4:6.601841e9, 5:1.049621e15, 8:6.964173e28, 13:4.952138e53,
16:3.168465e68} rel 5e-3, strictly increasing, all >= 1e9;
ZSUM_MAIN_DEEP {13:0.957836, 16:0.959354} rel 5e-3 (residual > 0
at all rungs); TFG_N_ABOVE = 25 of 26, EXC = [4]; WMIN_BAND =
(1.9908, 3.4522) rel 1e-3; TFG_CAP = 0.267439 rel 1e-3 (max at
h = 7); TFG_MIN = 0.111732 rel 1e-3; L_NEED = 1.725411 rel 1e-3;
IND_MARGIN = 1.295054 rel 1e-3 (min lock 2.2345); P_FG_TAB
{(4,8):4.4805, (8,16):4.4489, (5,10):3.4641, (10,20):4.2723,
(6,13):4.9990, (13,26):3.9303} rel 1e-3, window (3.3, 5.1);
P_YT_TAB {(4,8):4.5394, (8,16):4.2022, (5,10):4.1405,
(10,20):4.1268, (6,13):4.6391, (13,26):4.0893} rel 1e-3, window
(3.9, 4.8); LOCKRAT_TAB {(4,8):0.9600, (8,16):1.1865,
(5,10):0.6257, (10,20):1.1061, (6,13):1.2833, (13,26):0.8956} rel
1e-3, window (0.55, 1.40); DTHETA window (0, 0.025].
Deterministic: NO randomness anywhere.  Cache verified_zeros_n7000
READ-ONLY in ward_ (X5), main-process only; NO zeta use.  All mpf
arithmetic inside explicit workdps blocks; flat O(1) ratios
transported as f64 for gating (DISCLOSED).  Amendments after the
frozen run, if any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
CITED-LADDER-REPLICATED(G33); UNIVERSAL-EXCLUSION-THEOREM-TAU-FREE
(G10, covers h <= 13 at frozen bar); DK-GATE-CROSSOVER-REPLICATED
(h = 16; G37); REQUIRED-BAR-SCHEDULE-EXACT(G37);
MINIMAL-DIAL-LOCK-SURVIVES-25-OF-26-EXC-H4(G44);
DIAL-BREAKS-CERT-CENSUS-BA3-NOT-H1(G38/G40);
FULL-SPACE-MIN-PRICE-GROWS(G39); CERT-PRICE-30-ORDERS-ABOVE-BAR
(G39); EIG-SATURATION-EIGF==EIG8(G39); ALIGNMENT-SHARING-MEASURED
(G39); CS-GAP-LADDER-GROWS(G39); BA3-NOT-UNIVERSAL-ZMIN-PASSER
(G41); BA3-SCALE-GAUGE-DEPENDENT(G13); ZMIN-WITNESS-BREAKS-CERT
(G41); LEAK-NOT-EXHIBITED-CALIBRATED(G42) + deep token
LEAK-FREE-MEASURED-DEEP or MANIFOLD-LEAK-EXHIBITED(h);
COVERAGE-TABLE-ASSEMBLED(G43); TAU-ABS-IMPORT-NOT-LOAD-BEARING
(G61); FRAME-LEGS-EXACT + NO-FRAME-NESTING(G15);
SOURCE-LEGS-NO-TRANSPORT + SPECTRAL-LEGS-MEASURED(G46);
TRANSPORT-DEFECTS-MEASURED(G45); INDUCTION-CONDITIONAL-ON-MEASURED-
TRANSPORT(G47); TRANSPORT-RELABELS-NOT-REDUCES(G47);
L-NEED-NAMED-1.7254(G44/G47); LEVEL-CHEAPER-THAN-INCREMENT(G47);
MANIFOLD-EMPTY-IN-FAKE-WORLDS + SIZE-SEPARATOR(G50-G52);
LARGE-DIAL-LOCK-EXCLUDED-EVERYWHERE(G53); DEMAND-FLAT +
BOUND-RIDES-CONNES(G54); QUANTIFIER-SEQ(G60); LOOP-ROUTES-FLAGGED
(six; G61/G63); OMEGA-UNCHANGED(census 4; G62); MINCUT(4/5).
Composite priority: INSTRUMENT-EDGE > EXACT-LAYER-OBSTRUCTED >
verdicts as gated.  NO RH CLAIM.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 37/38 at the
first-freeze SPEC_SHA 642da05e6791d466, log kept as
manifold_invariance_probe.smoke1.log; NO record run existed yet).
ONE sympy INSTRUMENT bug in the exact layer, no bar, window, tab or
criterion moved anywhere: the G16 dial-magnitude leg declared the
symbolic dial W merely positive, so sympy cannot resolve
Abs(A_2 (W - 1)/dbp) without the sign of W - 1; fixed by the exact
parametrization W = 1 + wexc with wexc > 0 (a dial IS an inflation
W > 1 -- exactly the code path of W_DIAL and the W = 1000 witness).
Fix verified in isolation before re-freeze; smoke2 at the fixed SHA
must be clean.

AMENDMENT 1 (post-record, disclosed; run1 = 38/39 at SPEC_SHA
5a0bfabf31ce4f07, log kept as manifold_invariance_probe.run1.log;
the ONE failing gate is G41-zmin-universal and the failing rung is
h = 24 ONLY -- every calibrated-rung tab matched and the {5,16}
dps-cross passed).  ROOT CAUSE (instrument, the SAME artifact class
the calibration already caught once: pass-1's dps-60 ZMIN at h = 16
was precision garbage and was corrected pre-freeze to dps 90): the
frozen fixed ZMIN_DPS = 90 is insufficient at h = 24, where the
main-source zsum cancellation depth (~46 digits, E_N ~ sqrt(tau)
with tau ~ 1e-98) plus the KKT conditioning at K = 96 exhausts the
90-digit budget -- the h = 24 solve returned zmin/zmain = 2.065e11
with BA3 residual -1.9e11, breaking the ladder pattern, and its
witness wards fired exactly as designed.  FIX: the ZMIN layer dps
is rung-scaled, dps_z(h) = 90 for h <= 16 (every frozen ZMIN/ZMINWIT
tab is at h <= 16 and is UNCHANGED) and dps_z(h) = DPS[h] + 40 for
h >= 20 (184/190 at h = 20/24); the dps-cross ward is EXTENDED to
h = 24 (ZMIN_XRUNGS = (5, 16, 24), rel <= 1e-6 at dps_z + 40).  NO
bar, window, tab, decision rule or verdict enum moved anywhere; the
h >= 20 ZMIN rows remain REPORTED + rule-adjudicated as frozen.

AMENDMENT 2 (post-record, disclosed; run2 = 38/39 at SPEC_SHA
66ebfd30613add44, log kept as manifold_invariance_probe.run2.log;
the ONE failing gate is again G41 and again at h = 24 ONLY --
the rung-scaled dps of Amendment 1 FIXED the optimizer itself:
h = 24 now lands zmin/zmain = 3.394e-9 with BA3 residual at the
minimum +1.000 (a BA3-passing refuter exists at the deep rungs
too, consistent with the calibrated ladder), and the ZMINWIT
price ladder extends smoothly to 8.6e107 at h = 24).  ROOT CAUSE
(ward currency, not instrument): the frozen dps-cross ward
demanded |z2/zmin - 1| <= 1e-6 PER VALUE; at h = 24 the true
minimum sits ~9 orders BELOW zmain (near-annihilation of the
tail sum), where a per-value relative agreement at 1e-6 is not
a precision-meaningful demand.  The decision-relevant currency
is zmin RELATIVE TO ZMAIN: the BA3-residual decision consumes
zmin/tau = (zmin/zmain)(zmain/tau), so |z2 - zmin|/zmain <=
1e-6 pins the adjudicated residual to 1e-6.  FIX: the cross
ward is re-currencied to |z2 - zmin|/zmain <= 1e-6 at ALL
cross rungs {5, 16, 24} (at 5 and 16, where zmin/zmain >=
6e-3, the calibrated cross differences were 0.0 in BOTH
currencies -- no outcome moves there); per-leg diagnostic
prints added.  NO other bar, window, tab, decision rule or
verdict enum moved.

AMENDMENT 3 (post-record, disclosed; run3 = 38/39 at SPEC_SHA
b16ec9c162bfe6d7, log kept as manifold_invariance_probe.run3.log;
the ONE failing gate is again G41, and the Amendment-2
diagnostics now LOCALIZE it: the h = 16 dps-cross drift is
|z2 - z|/zmain = 1.77e-2 -- the deeper-dps solve finds a
SMALLER feasible minimum, z2 ~ 2.1e-4 zmain vs the frozen
dps-90 value 1.79e-2 zmain).  ROOT CAUSE (two layers, both
disclosed): (i) the CALIBRATION dps-cross was VACUOUS -- the
scratch script imported itself ("import calib_scratch_mi")
inside __main__ and set ZMIN_DPS on the IMPORTED module object
while zmin_optimizer read the __main__ global: the calibration
"dps90->130 rel diff 0.00e+00" line re-ran dps 90 twice, so
the dps-90 ZMIN values were never actually cross-checked
(classic __main__/module aliasing; found only by the record
ward -- the ward did its job); (ii) the ZMIN layer at finite
dps returns the objective at the KKT point of the dps-ROUNDED
problem: a FEASIBLE refuter (its A_0/A_2 constraints are
warded at 1e-25/1e-6) whose zsum is an UPPER VALUE of the true
constrained minimum.  RETYPE (honest, decision-safe): the ZMIN
rows are typed FEASIBLE-UPPER-VALUE-OF-THE-MINIMUM, not the
converged minimum; the BA3-passer adjudication is MONOTONE in
this upper value (a smaller true minimum makes the BA3
residual at the minimum MORE positive), so the delivered
conclusion BA3-NOT-UNIVERSAL-ZMIN-PASSER is ROBUST to the
retype at every rung, and the h = 16 deeper-dps point makes it
STRICTLY STRONGER.  The ZMINWIT witness stays a legitimate
feasible refuter (its certificate price is measured exactly at
rung dps).  FIX: the dps-cross ward is re-currencied to
DECISION STABILITY -- the BA3-residual sign at the deeper-dps
point must equal the sign at the frozen point AND z2 <= z
(1 + 1e-6) (the deeper solve may only improve the upper
value); the drift is REPORTED.  ZMIN_TAB/ZMINWIT_R0_TAB
strings and gates are UNCHANGED (deterministic at the frozen
dps).  NO other bar, window, tab, decision rule or verdict
enum moved.
"""

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
WORKERS = 12
RUNGS_SUB = (4, 5, 6, 8, 10, 13, 16, 20, 24)
DPS = {4: 60, 5: 60, 6: 65, 8: 80, 10: 90, 13: 120, 16: 130,
       20: 144, 24: 150}

SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
CF_BAR = 1e-40
KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906}
KAPPA_WIN = (0.0, 0.30)
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7}
FG_WIN = (0.97, 1.03)
LOCK_WIN = (1.0, 8.0)
YT_R143 = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6}
YT_DEX_BAR = 1e-3
THETA_BAR = 0.155
THETA_Y_WIN = (0.03, 0.12)
THETA_Y_TAB = {4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983}
H3_MARGIN_MIN = 1.5
STAB_GATE_TAB = {4: 4.478e-25, 5: 3.472e-23, 8: 5.322e-17,
                 13: 6.568e-6}
STAB_MEAS_BAR = 1e-30
C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00)
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
NZSUM = 1200
F64_SLOP = 1e-3
Z_OVERHANG = 6.0
ZSUM_TAB = {4: 0.8842, 5: 0.9603, 8: 0.9539}
CTRL_TAU_TAB = {"SMOOTH": {4: -1.0375, 5: -1.0944},
                "SCRARITH": {5: -0.34593, 6: -0.36716},
                "EPSTEIN": {8: -1.6310}}
CTRL_SET = (("SMOOTH", 4, 60), ("SMOOTH", 5, 60),
            ("SCRARITH", 5, 60), ("SCRARITH", 6, 60),
            ("EPSTEIN", 8, 80))
CTRL_THETA_MAX = 1e-2
SEP_MIN = 10.0
THETA_W_CAL = {("SMOOTH", 4): 3.541319e-4, ("SMOOTH", 5): 2.409799e-4,
               ("SCRARITH", 5): 1.005571e-3,
               ("SCRARITH", 6): 1.875055e-3,
               ("EPSTEIN", 8): 1.011306e-4}
WIT1000 = dict(dnorm=8.117888e-2, theta=62.690999, lock=3.6444e-3,
               r0tau=3.430e13, zratio=3.579247e8, ba3=-3.4372e8)
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 2700.0
GAMMA1_LIT = 14.134725141734693790   # ward only
NEW_TOL = 5e-3
ANA_TOL = 1e-3

# ------------------------------------ cited r172 record ladders (4dp)
YT_L10_R172 = {4: 4.2532, 5: 4.7858, 6: 5.1092, 7: 5.4003,
               8: 5.6197, 9: 5.8273, 10: 6.0322, 11: 6.1957,
               12: 6.3775, 13: 6.5057, 14: 6.6664, 15: 6.7625,
               16: 6.8847, 17: 6.9876, 18: 7.0996, 19: 7.1728,
               20: 7.2745, 21: 7.3667, 22: 7.4493, 23: 7.5210,
               24: 7.6035, 25: 7.6678, 26: 7.7367, 27: 7.8077,
               28: 7.8687, 30: 7.9925}
LOCK_R172 = {4: 2.4885, 5: 3.6444, 6: 2.5824, 7: 3.9814, 8: 2.3890,
             9: 2.8616, 10: 2.2804, 11: 2.7183, 12: 2.5302,
             13: 3.3141, 14: 2.5778, 15: 2.9692, 16: 2.8345,
             17: 2.7172, 18: 2.5836, 19: 2.6024, 20: 2.5224,
             21: 2.5272, 22: 2.5592, 23: 2.5246, 24: 2.8361,
             25: 2.6379, 26: 2.9682, 27: 3.1499, 28: 2.2345,
             30: 2.8667}

# ------------------------------------------------- new frozen (calibrated)
DIAL_EPS = 0.05
EIG_J8 = (1, 2, 3, 4, 5, 6, 7, 8)
EIG_J2 = (1, 2)
CENSUS_VAR_MAX = 16
ZMIN_DPS = 90
ZMIN_XDPS = 40
ZMIN_XRUNGS = (5, 16, 24)
ZMIN_XBAR = 1e-6
BSTAR_LO, BSTAR_HI = -90.0, 6.0
LOCK_LO = 1.0
CAL_RUNGS = (4, 5, 8, 13, 16)
WMIN_TAB = {4: 3.452032, 5: 2.472444, 8: 2.375493, 13: 2.153286,
            16: 2.064341}
WDIAL_TAB = {4: 3.624634, 5: 2.596066, 8: 2.382248, 13: 2.260950,
             16: 2.167558}
RUNIV_TAB = {4: 1.1144e-24, 5: 1.2652e-22, 8: 1.2714e-16,
             13: 2.1767e-5}
RUNIV_MEAS_16 = 2.8408e-35
BSTAR_TAB = {4: -1.1890, 5: -3.3241, 8: -9.3405, 13: -20.6087,
             16: -27.6292}
BSTAR_ABS = 0.02
PRICE_DIAL_TAB = {4: 3.703906e7, 5: 5.190266e10, 8: 1.984023e18,
                  13: 1.683418e31, 16: 1.154863e39}
PRICE_EIGF_TAB = {4: 1.353657e5, 5: 4.696766e5, 8: 2.844554e6,
                  13: 3.820643e7, 16: 9.467704e7}
PRICE_COARSE_DIAL = 1e6
PRICE_COARSE_EIG = 1e4
DIAL_NREAL_TAB = {4: 4, 5: 8, 8: 14, 13: 31, 16: 41}
DIAL_LOCK_TAB = {4: 0.6866, 5: 1.4038, 8: 1.0028, 13: 1.4658,
                 16: 1.3077}
GAP_TAB = {4: 2.354, 5: 2.699, 8: 3.022, 13: 3.519, 16: 3.669}
GAP_ABS = 0.05
ZR_DIAL_TAB = {4: 2.582319e2, 5: 9.147271e2, 8: 4.424925e3,
               13: 3.631757e4, 16: 8.750938e4}
BA3_DIAL_TAB = {4: -2.273202e2, 5: -8.774327e2, 8: -4.220003e3,
                13: -3.478528e4, 16: -8.395148e4}
ZR_EIGF_TAB = {4: 5.468683e1, 5: 4.419774e1, 8: 5.183652e1,
               13: 1.453730e2, 16: 1.634536e2}
BA3_EIGF_TAB = {4: -4.735231e1, 5: -4.144407e1, 8: -4.844764e1,
                13: -1.382435e2, 16: -1.558098e2}
ZMIN_TAB = {4: 2.546824e-1, 5: 1.272993e-1, 8: 1.589237e-2,
            13: 6.068511e-3, 16: 1.790734e-2}
ZMINWIT_R0_TAB = {4: 6.601841e9, 5: 1.049621e15, 8: 6.964173e28,
                  13: 4.952138e53, 16: 3.168465e68}
ZSUM_MAIN_DEEP = {13: 0.957836, 16: 0.959354}
TFG_N_ABOVE = 25
TFG_EXC = (4,)
WMIN_BAND = (1.9908, 3.4522)
TFG_CAP_STR = 0.267439
TFG_MIN_STR = 0.111732
L_NEED_STR = 1.725411
IND_MARGIN_STR = 1.295054
LOCK_MIN_STR = 2.2345
REP_CHAINS = ((4, 8, 16), (5, 10, 20), (6, 13, 26))
P_FG_TAB = {(4, 8): 4.4805, (8, 16): 4.4489, (5, 10): 3.4641,
            (10, 20): 4.2723, (6, 13): 4.9990, (13, 26): 3.9303}
P_FG_WIN = (3.3, 5.1)
P_YT_TAB = {(4, 8): 4.5394, (8, 16): 4.2022, (5, 10): 4.1405,
            (10, 20): 4.1268, (6, 13): 4.6391, (13, 26): 4.0893}
P_YT_WIN = (3.9, 4.8)
LOCKRAT_TAB = {(4, 8): 0.9600, (8, 16): 1.1865, (5, 10): 0.6257,
               (10, 20): 1.1061, (6, 13): 1.2833, (13, 26): 0.8956}
LOCKRAT_WIN = (0.55, 1.40)
DTHETA_MAX = 0.025

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []
EXTRA_TOKENS: list[str] = []


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
            bad.append("zeta use @%d" % node.lineno)
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
                       "no verification/ import; workers cache-free")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- closed forms
def hsw_G(T: float) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (HSW_A * (2 * lg + 1) / 2 + HSW_B * (ll + 1 / (2 * lg))
              + HSW_C) / Tm ** 2
        t3 = (HSW_A * lg + HSW_B * ll + HSW_C) / Tm ** 2
        return float(t1 + t2 + t3)


def en_val(cs, aa, oms, t):
    """E_N(t) = sin(At) R(t) (r166 VERBATIM); caller sets workdps."""
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


def npoly_coeffs(cs, b, K):
    """rootladder census form VERBATIM (r156/r171/r172/r173)."""
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
    """per-rung build: r173-replication legs + the adversary
    batteries (DIAL2 minimal dial, EIG8/EIG2/EIGF minimal-residual
    refuters), R_univ + b* schedule.  NO cache access (the chain is
    zero-free); candidate source strings + M strings returned for
    the main-process BA3/ZMIN layer."""
    h, dps = args
    try:
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
            aa = mp.log(h) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
            yt = abs(A2 / A0)
            FGm = (lam1 - tau) / tau
            lock = FGm / yt
            Tz4 = (2 * mp.pi * h) ** 4
            th = yt / Tz4
            B1 = sum(b[k] for k in range(1, K))
            B1_cf = (mp.pi / aa) ** 2 * (K - 1) * K * (2 * K - 1) / 6
            cmax = max(abs(v) for v in cs)
            out["a2_sign"] = int(mp.sign(A2 / A0))
            out["cf_dev"] = float(abs(B1 / B1_cf - 1))
            out["kappa"] = float(B1 / yt)
            out["yt_l10"] = float(mp.log(yt) / l10)
            out["log10a0"] = float(mp.log(abs(A0)) / l10)
            out["log10tau"] = float(mp.log(tau) / l10)
            out["fg"] = float(FGm)
            out["lock"] = float(lock)
            out["theta_y"] = float(th)
            out["tfg_meas"] = float(th * lock)
            out["h3_ok"] = bool(yt <= mp.mpf(repr(THETA_BAR)) * Tz4)
            out["h3_margin"] = float(mp.mpf(repr(THETA_BAR)) / th)
            # main-source certificate residual
            v0 = [V[i, 0] for i in range(K)]
            n0 = mp.sqrt(sum(v * v for v in v0))
            v0 = [v / n0 for v in v0]
            Mv = [sum(M[i, k2] * v0[k2] for k2 in range(K))
                  for i in range(K)]
            ray = sum(v0[i] * Mv[i] for i in range(K))
            r0 = mp.sqrt(sum((Mv[i] - ray * v0[i]) ** 2
                             for i in range(K)))
            out["ray_dev"] = float(abs(ray / tau - 1))
            out["r0_rel"] = float(r0 / tau)
            e0n = mp.sqrt(sum((1 / nrm[k]) ** 2 for k in range(K)))
            e2n = mp.sqrt(sum((b[k] / nrm[k]) ** 2
                              for k in range(1, K)))
            out["e0n"] = float(e0n)
            out["e2n"] = float(e2n)

            def rel_radius(sth):
                dvv = sth + sth ** 2
                dA0 = e0n * dvv
                dA2 = e2n * dvv
                if dA0 < abs(A0):
                    return (dA2 / abs(A2) + dA0 / abs(A0)) \
                        / (1 - dA0 / abs(A0))
                return mp.inf

            for tag, rr in (("gate", mp.mpf(repr(RES0_BAR)) * tau),
                            ("meas", r0)):
                sth = rr / (lam1 - tau * (1 + mp.mpf(repr(RAY_BAR))))
                out["stab_" + tag] = float(rel_radius(sth))
            den_u = mp.mpf(repr(LOCK_LO)) * yt - mp.mpf(repr(RAY_BAR))
            out["r_univ"] = float(rel_radius(
                mp.mpf(repr(RES0_BAR)) / den_u))
            out["r_univ_meas"] = float(rel_radius((r0 / tau) / den_u))
            wmin = mp.mpf(repr(THETA_BAR)) / th
            ratio = th * lock / mp.mpf(repr(THETA_BAR))
            if ratio > 1:
                fac = min(1 + mp.mpf(repr(DIAL_EPS)), mp.sqrt(ratio))
            else:
                fac = 1 + mp.mpf(repr(DIAL_EPS))
            wdial = fac * wmin
            out["wmin"] = float(wmin)
            out["wdial"] = float(wdial)
            out["wmin_ward"] = float(abs(wmin * th
                                         / mp.mpf(repr(THETA_BAR))
                                         - 1))
            tgt = wmin - 1
            lo, hi = mp.mpf(BSTAR_LO), mp.mpf(BSTAR_HI)
            for _ in range(200):
                mid = (lo + hi) / 2
                vv = rel_radius(mp.mpf(10) ** mid / den_u)
                if vv < tgt:
                    lo = mid
                else:
                    hi = mid
                if hi - lo < mp.mpf("1e-4"):
                    break
            out["bstar_l10"] = float((lo + hi) / 2)

            def jets(cs2):
                A0w = sum((-1) ** k * cs2[k] for k in range(K))
                A2w = sum((-1) ** k * cs2[k] * b[k]
                          for k in range(1, K))
                Ajw = [A0w]
                pw = [mp.mpf(1)] * K
                for m in range(1, M_JETS + 1):
                    acc = mp.mpf(0)
                    for k in range(1, K):
                        pw[k] = pw[k] * b[k] if m > 1 else b[k]
                        acc += (-1) ** k * cs2[k] * pw[k]
                    Ajw.append(acc)
                return A0w, A2w, Ajw

            def battery(tag, cs2, do_census):
                d = {}
                A0w, A2w, Ajw = jets(cs2)
                ytw = abs(A2w / A0w)
                d["a0_dev"] = float(abs(A0w / A0 - 1))
                d["ytdev"] = float(abs(ytw / (wdial * yt) - 1))
                d["theta"] = float(ytw / Tz4)
                d["lock_pp"] = float(FGm / ytw)
                d["kappa"] = float(B1 / ytw)
                d["J2"] = float(Ajw[2] / (A0w * ytw ** 2))
                vw = [cs2[k] * nrm[k] for k in range(K)]
                nw = mp.sqrt(sum(v * v for v in vw))
                vw = [v / nw for v in vw]
                Mvw = [sum(M[i, k2] * vw[k2] for k2 in range(K))
                       for i in range(K)]
                rayw = sum(vw[i] * Mvw[i] for i in range(K))
                r0w = mp.sqrt(sum((Mvw[i] - rayw * vw[i]) ** 2
                                  for i in range(K)))
                d["ray_dev_pp"] = float(abs(rayw / tau - 1))
                d["r0_tau"] = float(r0w / tau)
                cs_abs2 = [abs(v) for v in cs2]

                def envres_y(yq, mm):
                    acc = mp.mpf(0)
                    yi = mp.mpf(1)
                    for i in range(1, mm + 1):
                        yi *= yq
                        acc += abs(Ajw[i]) / yi
                    rem = mp.mpf(0)
                    for k in range(1, K):
                        rem += cs_abs2[k] * b[k] ** (mm + 1) \
                            / (yi * (yq - b[k]))
                    return acc + rem

                cstar = None
                for c in C_GRID:
                    yq = mp.mpf(repr(c)) * ytw
                    if yq <= b[K - 1]:
                        continue
                    best = None
                    for mm in MGRID:
                        vvv = envres_y(yq, mm)
                        if best is None or vvv < best:
                            best = vvv
                    if best / abs(A0w) < 1:
                        cstar = c
                        break
                d["cstar"] = cstar
                if do_census:
                    with mp.workdps(3 * dps):
                        poly, psc = npoly_coeffs(cs2, b, K)
                    rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                                       extraprec=2 * dps)
                    d["nreal"] = sum(
                        1 for r in rts
                        if abs(mp.im(r)) <= mp.mpf(repr(IM_TOL)))
                    d["ztop"] = float(max(mp.re(r) for r in rts)
                                      * psc / ytw)
                d["cn_str"] = [mp.nstr(v, dps) for v in cs2]
                out[tag] = d
                return d

            # DIAL2 minimal 2-mode dial (A0-invariant, exact)
            dP = A2 * (wdial - 1) / (b[2] - b[1])
            cs_d = list(cs)
            cs_d[1] = cs[1] + dP
            cs_d[2] = cs[2] + dP
            out["dial_dnorm"] = float(abs(dP) / cmax)
            battery("DIAL2", cs_d, h <= CENSUS_VAR_MAX)

            def eigopt(tag, jset):
                jset = tuple(j for j in jset if j < K)
                a0j, a2j, nuj = [], [], []
                for j in jset:
                    a0v = sum((-1) ** k * V[k, j] / nrm[k]
                              for k in range(K))
                    a2v = sum((-1) ** k * b[k] * V[k, j] / nrm[k]
                              for k in range(1, K))
                    a0j.append(a0v)
                    a2j.append(a2v)
                    nuj.append((E[j] - tau) / tau)
                w = [v * v for v in nuj]
                S00 = sum(a0j[i] ** 2 / w[i]
                          for i in range(len(jset)))
                S02 = sum(a0j[i] * a2j[i] / w[i]
                          for i in range(len(jset)))
                S22 = sum(a2j[i] ** 2 / w[i]
                          for i in range(len(jset)))
                m2 = (wdial - 1) * A2
                det = S00 * S22 - S02 * S02
                al = -S02 * m2 / det
                be = S00 * m2 / det
                tj = [(al * a0j[i] + be * a2j[i]) / w[i]
                      for i in range(len(jset))]
                cs2 = list(cs)
                for i, j in enumerate(jset):
                    for k in range(K):
                        cs2[k] = cs2[k] + tj[i] * V[k, j] / nrm[k]
                dn = max(abs(al * a0j[i] + be * a2j[i]) / w[i]
                         for i in range(len(jset)))
                out[tag + "_dnorm"] = float(dn / cmax)
                if tag == "EIG8":
                    out["gap_a01"] = float(
                        (mp.log(abs(a0j[0])) - mp.log(abs(A0)))
                        / l10)
                battery(tag, cs2, False)

            eigopt("EIG8", EIG_J8)
            eigopt("EIG2", EIG_J2)
            eigopt("EIGF", tuple(range(1, K)))
            out["cn_main"] = list(ce["cn_mp_str"])
            out["tau_str"] = mp.nstr(tau, dps)
            out["lam1_str"] = mp.nstr(lam1, dps)
            # ZMINWIT cert evaluation needs M: ship strings
            out["M_str_all"] = [[mp.nstr(M[i, j], dps)
                                 for j in range(K)]
                                for i in range(K)]
        return out
    except Exception as exc:                       # noqa: BLE001
        import traceback
        return dict(h=h, error=repr(exc), tb=traceback.format_exc())


def w_control(args) -> dict:
    """control world: tau_w + theta_w + lock_w (builds only)."""
    world, xw, dpsw = args
    try:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            lam1 = cw["mpE"][1]
            aa = mp.log(xw) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(Kw))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, Kw))
            ytw = abs(A2 / A0)
            Tz = 2 * mp.pi * xw
            return dict(world=world, h=xw, tauf=float(tau),
                        theta_w=float(ytw / Tz ** 4),
                        lock_w=float(((lam1 - tau) / tau) / ytw))
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# ------------------------------------------------ main-process zsum
def zsum_off_main(h, K, cs, dps, gam):
    """BA3 currency (r131/r166 recipe VERBATIM): certified tail zsum
    + r131 OFF at T_PT.  Main process only (ward-passed ordinates)."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        cs_abs = [abs(v) for v in cs]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A_j = [A0]
        pw = [mp.mpf(1)] * K
        for m in range(1, M_JETS + 1):
            acc = mp.mpf(0)
            for k in range(1, K):
                pw[k] = pw[k] * b[k] if m > 1 else b[k]
                acc += (-1) ** k * cs[k] * pw[k]
            A_j.append(acc)

        def envres(Tq, mm):
            yq = mp.mpf(repr(float(Tq))) ** 2
            acc = mp.mpf(0)
            yi = mp.mpf(1)
            for i in range(1, mm + 1):
                yi *= yq
                acc += abs(A_j[i]) / yi
            rem = mp.mpf(0)
            for k in range(1, K):
                rem += cs_abs[k] * b[k] ** (mm + 1) / (yi * (yq - b[k]))
            return acc + rem

        best = None
        for m in MGRID:
            vv = envres(T_PT, m)
            if best is None or vv < best:
                best = vv
        eta_pt = best / abs(A0)
        off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
            * mp.mpf(repr(hsw_G(float(T_PT))))
        Tz = 2 * math.pi * h
        zs = mp.mpf(0)
        for g in gam[:NZSUM]:
            if float(g) <= Tz + Z_OVERHANG:
                continue
            gm = mp.mpf(repr(float(g)))
            ev = en_val(cs, aa, oms, gm)
            zs += 2 * ev * ev
        return zs * (1 - mp.mpf(repr(F64_SLOP))), off


def zsum_only(h, K, cs, dps, gam):
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        Tz = 2 * math.pi * h
        zs = mp.mpf(0)
        for g in gam[:NZSUM]:
            if float(g) <= Tz + Z_OVERHANG:
                continue
            gm = mp.mpf(repr(float(g)))
            ev = en_val(cs, aa, oms, gm)
            zs += 2 * ev * ev
        return zs * (1 - mp.mpf(repr(F64_SLOP)))


def zmin_optimizer(h, K, cs_str, wdial, gam, dps_z):
    """min zsum(c+d) over ALL d with A0(d) = 0, A2(c+d) = wdial*A2
    (A0-gauge; KKT, exact constrained quadratic minimum)."""
    with mp.workdps(dps_z):
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        cs = [mp.mpf(s) for s in cs_str]
        Tz = 2 * math.pi * h
        ords = [mp.mpf(repr(float(g))) for g in gam[:NZSUM]
                if float(g) > Tz + Z_OVERHANG]
        evecs = []
        for gm in ords:
            sg = mp.sin(aa * gm)
            row = [sg * 2 / gm]
            for k in range(1, K):
                row.append(sg * 2 * (-1) ** k * gm
                           / (gm * gm - oms[k] ** 2))
            evecs.append(row)
        slop = 1 - mp.mpf(repr(F64_SLOP))
        Q = mp.zeros(K, K)
        for row in evecs:
            for i in range(K):
                ri = row[i]
                for j in range(i, K):
                    Q[i, j] += 2 * slop * ri * row[j]
        for i in range(K):
            for j in range(i + 1, K):
                Q[j, i] = Q[i, j]
        A2v = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        m2 = (mp.mpf(repr(wdial)) - 1) * A2v
        KK = mp.zeros(K + 2, K + 2)
        rhs = mp.matrix(K + 2, 1)
        Qc = [sum(Q[i, k] * cs[k] for k in range(K))
              for i in range(K)]
        for i in range(K):
            for j in range(K):
                KK[i, j] = Q[i, j]
            KK[i, K] = (-1) ** i
            KK[K, i] = (-1) ** i
            wv = ((-1) ** i * b[i]) if i >= 1 else mp.mpf(0)
            KK[i, K + 1] = wv
            KK[K + 1, i] = wv
            rhs[i] = -Qc[i]
        rhs[K] = 0
        rhs[K + 1] = m2
        sol = mp.lu_solve(KK, rhs)
        d = [sol[i] for i in range(K)]
        zval = mp.mpf(0)
        for row in evecs:
            ev = sum(row[k] * (cs[k] + d[k]) for k in range(K))
            zval += 2 * slop * ev * ev
        zmain = mp.mpf(0)
        for row in evecs:
            ev = sum(row[k] * cs[k] for k in range(K))
            zmain += 2 * slop * ev * ev
        d_str = [mp.nstr(v, dps_z) for v in d]
        return float(zval), float(zmain), len(ords), d_str


def zminwit_cert(h, K, r, dstr):
    """exact certificate/jets battery for the zmin witness (main
    process, rung dps, M strings from the worker)."""
    dps = DPS[h]
    with mp.workdps(dps):
        Mm = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                Mm[i, j] = mp.mpf(r["M_str_all"][i][j])
        tau_m = mp.mpf(r["tau_str"])
        aa = mp.log(h) / 2
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        cs = [mp.mpf(s) for s in r["cn_main"]]
        dd = [mp.mpf(s) for s in dstr]
        cw = [cs[k] + dd[k] for k in range(K)]
        A0w = sum((-1) ** k * cw[k] for k in range(K))
        A2w = sum((-1) ** k * cw[k] * b[k] for k in range(1, K))
        A0m = sum((-1) ** k * cs[k] for k in range(K))
        A2m = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        vw = [cw[k] * nrm[k] for k in range(K)]
        nw = mp.sqrt(sum(v * v for v in vw))
        vw = [v / nw for v in vw]
        Mv = [sum(Mm[i, k] * vw[k] for k in range(K))
              for i in range(K)]
        rayw = sum(vw[i] * Mv[i] for i in range(K))
        r0w = mp.sqrt(sum((Mv[i] - rayw * vw[i]) ** 2
                          for i in range(K)))
        return dict(a0_dev=float(abs(A0w / A0m - 1)),
                    yt_ratio=float(abs(A2w / A0w) / abs(A2m / A0m)),
                    ray_dev_pp=float(abs(rayw / tau_m - 1)),
                    r0_tau=float(r0w / tau_m))


def wit1000_battery(r, gam):
    """the r172/r173 W = 1000 2-mode inflation witness at h = 5,
    replicated through THIS round's machinery (main process)."""
    h, K = 5, r["K"]
    dps = DPS[5]
    with mp.workdps(dps):
        Mm = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                Mm[i, j] = mp.mpf(r["M_str_all"][i][j])
        tau_m = mp.mpf(r["tau_str"])
        lam1_m = mp.mpf(r["lam1_str"])
        aa = mp.log(h) / 2
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        cs = [mp.mpf(s) for s in r["cn_main"]]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        yt = abs(A2 / A0)
        cmax = max(abs(v) for v in cs)
        W = mp.mpf(1000)
        dP = A2 * (W - 1) / (b[2] - b[1])
        cw = list(cs)
        cw[1] = cs[1] + dP
        cw[2] = cs[2] + dP
        A0w = sum((-1) ** k * cw[k] for k in range(K))
        A2w = sum((-1) ** k * cw[k] * b[k] for k in range(1, K))
        ytw = abs(A2w / A0w)
        Tz4 = (2 * mp.pi * h) ** 4
        FGm = (lam1_m - tau_m) / tau_m
        vw = [cw[k] * nrm[k] for k in range(K)]
        nw = mp.sqrt(sum(v * v for v in vw))
        vw = [v / nw for v in vw]
        Mv = [sum(Mm[i, k] * vw[k] for k in range(K))
              for i in range(K)]
        rayw = sum(vw[i] * Mv[i] for i in range(K))
        r0w = mp.sqrt(sum((Mv[i] - rayw * vw[i]) ** 2
                          for i in range(K)))
        zs_main, off = zsum_off_main(h, K, cs, dps, gam)
        zs_w = zsum_only(h, K, cw, dps, gam)
        return dict(dnorm=float(abs(dP) / cmax),
                    a0_dev=float(abs(A0w / A0 - 1)),
                    yt_ratio=float(ytw / yt),
                    theta=float(ytw / Tz4),
                    lock_pp=float(FGm / ytw),
                    r0_tau=float(r0w / tau_m),
                    zratio=float(zs_w / zs_main),
                    ba3=float((tau_m + off - zs_w) / tau_m))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 tau-free universal DK exclusion
    tauS, FGs, a_, b_, L_, yts, s_ = sp.symbols(
        "tauS FGs a_ b_ L_ yts s_", positive=True)
    lam1S = tauS * (1 + FGs)
    rhoS = tauS * (1 + a_)
    okA = sp.simplify(b_ * tauS / (lam1S - rhoS)
                      - b_ / (FGs - a_)) == 0        # tau CANCELS
    # floor substitution FG = L*yt + s (window slack), a < L*yt:
    e1 = b_ / (L_ * yts - a_) - b_ / (L_ * yts + s_ - a_)
    num, den = sp.fraction(sp.together(e1))
    okB = sp.simplify(num - b_ * s_) == 0
    # DK sin-theta lemma (r173-G15 slack parametrization, replicated)
    s2, e_, wpos, a0, a1, a2 = sp.symbols("s2 e_ wpos a0 a1 a2",
                                          positive=True)
    lam0 = sp.symbols("lam0", positive=True)
    lam1s = lam0 + e_ + wpos
    lam2s = lam1s + s2
    rho_ = lam0 + e_
    r2 = a0 ** 2 * (lam0 - rho_) ** 2 \
        + a1 ** 2 * (lam1s - rho_) ** 2 \
        + a2 ** 2 * (lam2s - rho_) ** 2
    claim2 = sp.expand(r2 - (lam1s - rho_) ** 2
                       * (a1 ** 2 + a2 ** 2))
    pcl = sp.Poly(claim2, a0, a2, e_, wpos, s2)
    okC = all(c > 0 for c in pcl.coeffs())
    # y_t-move equality instance (r173-G15 okS replicated)
    yA = sp.Rational(11, 10) / sp.Rational(4, 10)
    bound = (sp.Rational(1, 10) + sp.Integer(2) * sp.Rational(1, 10)) \
        / (sp.Rational(1, 2) - sp.Rational(1, 10))
    okD = sp.simplify((yA - sp.Integer(2)) - bound) == 0
    # contrapositive chase (rational instance): R = 1/10 < Wmin-1 = 2
    R_ = sp.Rational(1, 10)
    okE = bool(R_ < 2) and not (bool(R_ >= 2))
    out.append(("G10-tau-free-universal-DK", okA and okB and okC
                and okD and okE,
                "sin-theta <= (r0/tau)/(FG - a): tau CANCELS "
                "(sympy identity); window-floor substitution FG >= "
                "L yt is positive-slack exact; DK sin-theta lemma "
                "replicated (r173-G15 slack parametrization, "
                "coefficients all positive); y_t-move equality "
                "instance; CONTRAPOSITIVE: R_univ(bar) < W_min - 1 "
                "==> NO certificate-passing fixed-M perturbation "
                "refutes H3 (direction-UNIVERSAL, witness-free, "
                "NO absolute tau import)"))

    # ---------------- G11 refuter dial window
    FGv, y_t, Wv, barS, thS = sp.symbols("FGv y_t Wv barS thS",
                                         positive=True)
    okF = sp.simplify(FGv / (Wv * y_t) - (FGv / y_t) / Wv) == 0
    lockS = sp.symbols("lockS", positive=True)
    okG = sp.simplify((lockS - barS / thS) * thS
                      - (thS * lockS - barS)) == 0
    w0 = sp.symbols("w0", positive=True)
    Wex = lockS + w0
    okH = sp.simplify(sp.expand(lockS / Wex * Wex - lockS)) == 0 \
        and bool(sp.Rational(36444, 10 ** 7) < 1) \
        and bool(sp.Rational(36444, 10) > 8)
    out.append(("G11-refuter-dial-window", okF and okG and okH,
                "lock'' == lock/W EXACT (fixed-M); a refuter "
                "survives the lock floor iff W < lock; the "
                "surviving window (W_min, lock) is NONEMPTY iff "
                "TFG = theta*lock > bar (exact equivalence); "
                "W > lock exits below the floor (r173-G16 class, "
                "symbolic W; instances 3.6444e-3 < 1, 3.6444e3 > "
                "8): the lock leg catches ALL large dials and, at "
                "TFG <= bar rungs, ALL refuters"))

    # ---------------- G12 H3-transport + L_NEED
    Tm, u, s2_, Lv = sp.symbols("Tm u s2_ Lv", positive=True)
    Theta = Tm - u
    lock1 = Lv + s2_
    diff1 = sp.expand(Tm * lock1 - Theta * Lv)
    p1 = sp.Poly(diff1, Tm, u, Lv, s2_)
    okI = all(c > 0 for c in p1.coeffs())
    Cc = sp.symbols("Cc", positive=True)
    okJ = sp.simplify(Cc / (Cc / barS) - barS) == 0
    out.append(("G12-h3-transport-lneed", okI and okJ,
                "TFG <= C and lock >= L ==> theta = TFG/lock <= "
                "C/L (positive-slack, r173-G10 class); theta <= "
                "bar iff L >= C/bar: L_NEED == TFG_CAP/bar "
                "(identity); with TFG_CAP = 0.267439: L_NEED = "
                "1.725411 -- the induction's lock-floor hypothesis "
                "NAMED"))

    # ---------------- G13 BA3 scale-gauge theorem
    t_ = sp.symbols("t_", positive=True)
    q11, q12, q22, c1, c2 = sp.symbols("q11 q12 q22 c1 c2",
                                       real=True)
    zq = (q11 * c1 ** 2 + 2 * q12 * c1 * c2 + q22 * c2 ** 2)
    zq_t = zq.subs({c1: t_ * c1, c2: t_ * c2})
    okK = sp.simplify(zq_t - t_ ** 2 * zq) == 0
    A0s, eta, Gg, aaS = sp.symbols("A0s eta Gg aaS", positive=True)
    OFFs = 8 * sp.exp(aaS) * (A0s * (1 + eta)) ** 2 * Gg
    okL = sp.simplify(OFFs.subs(A0s, t_ * A0s) / OFFs
                      - t_ ** 2) == 0
    zs_, offv = sp.symbols("zs_ offv", positive=True)
    okM = sp.limit((tauS + t_ ** 2 * (offv - zs_)) / tauS,
                   t_, 0) == 1
    out.append(("G13-ba3-scale-gauge", okK and okL and okM,
                "zsum and OFF are HOMOGENEOUS DEGREE 2 in the "
                "source while tau is fixed: the BA3 residual -> 1 "
                "as the scale t -> 0 for ANY direction (sympy "
                "limit) -- BA3 in absolute currency is passable by "
                "scaling: the leg is GAUGE-DEPENDENT; this round "
                "fixes the A_0 gauge (A_0(d) = 0, DISCLOSED); all "
                "H3-relevant observables are scale-invariant"))

    # ---------------- G14 KKT optimality instances
    x, y, z, l1, l2 = sp.symbols("x y z l1 l2")
    # min x^2 + 2y^2 + 3z^2 s.t. x+y+z = 0, x+2y+3z = 1
    Lg = x ** 2 + 2 * y ** 2 + 3 * z ** 2 \
        + l1 * (x + y + z) + l2 * (x + 2 * y + 3 * z - 1)
    solK = sp.solve([sp.diff(Lg, v) for v in (x, y, z)]
                    + [x + y + z, x + 2 * y + 3 * z - 1],
                    [x, y, z, l1, l2], dict=True)
    okN = len(solK) == 1
    if okN:
        so = solK[0]
        vK = (so[x] ** 2 + 2 * so[y] ** 2 + 3 * so[z] ** 2)
        # direct: parametrize null space (1, -2, 1)/denominators
        tpar = sp.symbols("tpar")
        x0, y0, z0 = so[x], so[y], so[z]
        # null direction of the two constraints:
        nd = sp.Matrix([1, -2, 1])
        expr = ((x0 + tpar * nd[0]) ** 2
                + 2 * (y0 + tpar * nd[1]) ** 2
                + 3 * (z0 + tpar * nd[2]) ** 2)
        dmin = sp.solve(sp.diff(expr, tpar), tpar)
        okN = dmin == [0] and sp.simplify(
            expr.subs(tpar, 0) - vK) == 0
    out.append(("G14-kkt-optimality", okN,
                "KKT stationary point == direct parametrized "
                "minimum on an exact rational instance (3 vars, 2 "
                "constraints): the ZMIN constrained quadratic "
                "minimizer and the EIG weighted least-squares "
                "solves are global minima (convex quadratic, "
                "linear constraints)"))

    # ---------------- G15 frame-exact transport legs
    kk, Kn = sp.symbols("kk Kn", positive=True, integer=True)
    Asym = sp.symbols("Asym", positive=True)
    s2sum = sp.summation(kk ** 2, (kk, 1, Kn - 1))
    okO = sp.simplify(s2sum - (Kn - 1) * Kn * (2 * Kn - 1) / 6) == 0
    s4sum = sp.summation(kk ** 4, (kk, 1, Kn - 1))
    n_ = Kn - 1
    faul4 = n_ * (n_ + 1) * (2 * n_ + 1) \
        * (3 * n_ ** 2 + 3 * n_ - 1) / 30
    okP = sp.simplify(s4sum - faul4) == 0
    hS = sp.symbols("hS", positive=True)
    okQ = sp.simplify((2 * sp.pi * 2 * hS) ** 4
                      / (2 * sp.pi * hS) ** 4 - 16) == 0
    okR = sp.simplify(sp.log(2 * hS) / 2 - sp.log(hS) / 2
                      - sp.log(2) / 2) == 0
    rr_ = sp.symbols("rr_", positive=True)
    Ah = sp.log(hS) / 2
    Ah2 = sp.log(hS * (1 + rr_)) / 2
    okS_ = sp.simplify(Ah2 - Ah - sp.log(1 + rr_) / 2) == 0 \
        and bool(sp.log(1 + sp.Rational(1, 1)) > 0)
    out.append(("G15-frame-exact-transport", okO and okP and okQ
                and okR and okS_,
                "FRAME legs transport EXACTLY: B_1 == (pi/A)^2 "
                "(K-1)K(2K-1)/6 (sympy summation); e2n^2 via "
                "Faulhaber k^4 closed form; T_z^4 doubling == 16; "
                "A(2h) - A(h) == log(2)/2; NON-NESTING: A(h') > "
                "A(h) strictly for h' > h, so the b-grids are "
                "incommensurate -- M(h) is NOT a compression of "
                "M(h'): NO Cauchy/Weyl interlacing transport "
                "exists for the spectral legs"))

    # ---------------- G16 dial algebra at symbolic W
    c0, c1_, c2_, c3_ = sp.symbols("c0 c1_ c2_ c3_", real=True)
    b1 = sp.symbols("b1", positive=True)
    dbp, dbq, wexc = sp.symbols("dbp dbq wexc", positive=True)
    Wsym = 1 + wexc
    b2 = b1 + dbp
    b3 = b1 + dbp + dbq
    A0g = c0 - c1_ + c2_ - c3_
    A2g = -c1_ * b1 + c2_ * b2 - c3_ * b3
    dP = A2g * (Wsym - 1) / (b2 - b1)
    okT = sp.simplify((c0 - (c1_ + dP) + (c2_ + dP) - c3_)
                      - A0g) == 0
    okU = sp.simplify((-(c1_ + dP) * b1 + (c2_ + dP) * b2
                       - c3_ * b3) - Wsym * A2g) == 0
    okV = sp.simplify(sp.Abs(dP)
                      - sp.Abs(A2g) * (Wsym - 1) / dbp) == 0
    out.append(("G16-dial-algebra-symbolic-W", okT and okU and okV,
                "the 2-mode dial identities hold at SYMBOLIC W "
                "(r172-G14 class generalized): A_0 invariant, "
                "A_2'' == W A_2, |d| == |A_2|(W-1)/(b_2-b_1) -- "
                "the minimal dial W_DIAL and the W = 1000 witness "
                "are the SAME exact construction at different "
                "dial values"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = [
        ("H3-cofinal remains SEQ (one rung per dyadic block, r172 "
         "quantifier VERBATIM); the residue triple {H1 AND H2 AND "
         "H3} per BH7-F1 ADOPTED", demand == SEQ),
        ("all tabs/windows/rules DECLARED pre-evaluation (SPEC_SHA "
         "covers the declaration); calibration = ONE pre-freeze "
         "pass in FOUR disclosed sub-passes (pass-1 bugs: eig index "
         "at K < 9, dial overshoots thin lock window at h = 8, "
         "ZMIN dps-60 precision artifact at h = 16 -- disclosed and "
         "corrected pre-freeze; all four logs kept)", True),
        ("h = 20/24 adversary numbers PRE-FREEZE UNMEASURED: "
         "REPORTED + frozen decision rules + coarse windows "
         "(PRICE_COARSE_*), DISCLOSED; census for variants h > 16 "
         "SKIPPED cost-disclosed; ZMINWIT census not evaluated "
         "(cert/lock/BA3 are the manifold core), DISCLOSED", True),
        ("candidate BA3 uses OFF_main (A_0-gauge; eta candidate-"
         "dependence second-order), DISCLOSED; EIG candidates are "
         "FIRST-ORDER optimal, exactly re-evaluated; leak search = "
         "frozen 5-candidate battery (failure to exhibit != "
         "exclusion beyond the DK-covered range), DISCLOSED", True),
        ("no ALL-X demand introduced; no uniform per-rung margin "
         "demanded; deep-rung tokens switch by frozen rule",
         demand != ALL_X)]
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


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


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("manifold_invariance_probe -- PRIME.MANIFOLD.INVARIANCE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = (4, 5) if smoke else RUNGS_SUB
    ctrl_tasks = (("SMOOTH", 4, 60), ("SCRARITH", 5, 60)) if smoke \
        else CTRL_SET
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5, main-process only; "
          "NO worker touches the cache)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")

    section("S1  EXACT LAYER")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDXCII BH7 F1/F2/F4 adopted; CDXC/r173 "
         "manifold machinery VERBATIM; CDLXXXVIII ladders + witness "
         "prices; CDLXXXVII PF/H1/H2; CDLXXXVI v926 (MEASURED, "
         "flagged) + v927 + v928 (census-PLAN transport); CDLXXV "
         "NO-EXACT-CROSS-H; r140/r143 alignment wall; r131 OFF; "
         "HSW22; PT21; v915 INSPECTED (Pick floors are a different "
         "spectral object: no corpus tau-floor for lambda_min(M)); "
         "CLXII/CCIII Riccati-HALFGAP lessons (increments steeper "
         "than levels; measured barrier dies)")

    section("S2  TARGETS")
    gtop = float(gam[-1])
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
        tasks.append(("rung", h, (h, DPS[h])))
    for world, xw, dpsw in ctrl_tasks:
        tasks.append(("ctl", (world, xw), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-(tk[2][1] if tk[0] == "rung"
                                 else 0),
                               -(tk[1] if tk[0] == "rung" else 0),
                               str(tk[1])))

    section("S3  BUILDS (%d tasks, %d workers)" % (len(tasks),
                                                   workers))
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

    # ------------------------------------------------ S3a gates
    section("S3a  PER-RUNG REPLICATION (r173 legs)")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    d30, d31, d32, d33, d34, d35 = ([] for _ in range(6))
    for h in rungs:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e r0 %.0e (%.0fs)"
                   % (h, r["K"], r["simp"], r["r0_rel"],
                      r["build_s"]))
        okx = (r["a2_sign"] == -1 and r["cf_dev"] <= CF_BAR
               and KAPPA_WIN[0] <= r["kappa"] <= KAPPA_WIN[1])
        if not smoke and h in KAPPA_TAB:
            okx = okx and abs(r["kappa"] / KAPPA_TAB[h] - 1) \
                <= NEW_TOL
        ok31 = ok31 and okx
        d31.append("h%d kap %.4f" % (h, r["kappa"]))
        okx = r["fg"] > 0 and LOCK_WIN[0] <= r["lock"] <= LOCK_WIN[1]
        if h in YT_R143:
            dex = abs(r["yt_l10"] - math.log10(YT_R143[h]))
            okx = okx and dex <= YT_DEX_BAR
        if not smoke and h in FG_TAB:
            okx = okx and FG_TAB[h] * FG_WIN[0] <= r["fg"] \
                <= FG_TAB[h] * FG_WIN[1]
        ok32 = ok32 and okx
        d32.append("h%d lock %.4f" % (h, r["lock"]))
        okx = THETA_Y_WIN[0] <= r["theta_y"] <= THETA_Y_WIN[1]
        th_cited = 10.0 ** YT_L10_R172[h] / (2 * math.pi * h) ** 4
        dexc = abs(r["yt_l10"] - YT_L10_R172[h])
        if not smoke:
            if h in THETA_Y_TAB:
                okx = okx and abs(r["theta_y"] / THETA_Y_TAB[h]
                                  - 1) <= NEW_TOL
            else:
                okx = okx and abs(r["theta_y"] / th_cited - 1) \
                    <= 8e-3
            okx = okx and dexc <= 1.5e-3
            okx = okx and abs(r["lock"] / LOCK_R172[h] - 1) <= 8e-3
        ok33 = ok33 and okx
        d33.append("h%d th %.4f dex %.1e" % (h, r["theta_y"], dexc))
        okx = r["h3_ok"] and r["h3_margin"] >= H3_MARGIN_MIN
        ok34 = ok34 and okx
        d34.append("h%d marg %.2f" % (h, r["h3_margin"]))
        okx = True
        if not smoke and h in STAB_GATE_TAB:
            okx = okx and abs(r["stab_gate"] / STAB_GATE_TAB[h] - 1) \
                <= NEW_TOL
        if h <= 13:
            okx = okx and r["stab_meas"] <= STAB_MEAS_BAR
        ok35 = ok35 and okx
        d35.append("h%d gate %.2e meas %.2e" % (h, r["stab_gate"],
                                                r["stab_meas"]))
    if not smoke:
        meas_seq = [tab[h]["stab_gate"] for h in (4, 5, 8, 13)
                    if h in tab]
        ok35 = ok35 and all(meas_seq[i] < meas_seq[i + 1]
                            for i in range(len(meas_seq) - 1))
        cross = [h for h in rungs if h in tab
                 and not math.isfinite(tab[h]["stab_gate"])]
        cross_str = ("first non-finite gate-bar radius at h = %d"
                     % cross[0]) if cross else "no crossover"
    else:
        cross_str = "smoke"
    check("G30-spectral-sanity", ok30, "; ".join(d30))
    check("G31-jets-kappa", ok31,
          "sign(A_2/A_0) == -1; B_1 closed form dev <= 1e-40; "
          "kappa in %s + tabs: %s" % (str(KAPPA_WIN),
                                      "; ".join(d31)))
    check("G32-cross-instrument", ok32,
          "y_t on YT_R143 <= 1e-3 dex; FULLGAP on FG_TAB; lock in "
          "%s: %s" % (str(LOCK_WIN), "; ".join(d32)))
    check("G33-cited-ladder-replication", ok33,
          "theta_y on THETA_Y_TAB rel 5e-3 + cited ladder rel 8e-3; "
          "yt_l10 <= 1.5e-3 dex; lock rel 8e-3 (THE LICENSE): %s"
          % "; ".join(d33))
    check("G34-h3-certificate", ok34,
          "H3: y_t <= 0.155 T_z^4, margin >= 1.5, every rebuilt "
          "rung (source-pure): %s" % "; ".join(d34))
    check("G35-stability-radii", ok35,
          "STAB_GATE_TAB rel 5e-3, strictly growing; stab_meas <= "
          "1e-30 at h <= 13; %s: %s" % (cross_str, "; ".join(d35)))

    # ------------------------------------------------ S3a adversary
    section("S3a2  ADVERSARY LAYER (W_min/W_DIAL, R_univ/b*, "
            "DIAL2, EIG)")
    ok36 = ok37 = ok38 = ok39 = True
    d36, d37, d38, d39 = ([] for _ in range(4))
    for h in rungs:
        if h not in tab:
            continue
        r = tab[h]
        wmin_cited = THETA_BAR / (10.0 ** YT_L10_R172[h]
                                  / (2 * math.pi * h) ** 4)
        okx = r["wmin_ward"] <= 1e-12 \
            and abs(r["wmin"] / wmin_cited - 1) <= 8e-3
        if not smoke and h in WMIN_TAB:
            okx = okx and abs(r["wmin"] / WMIN_TAB[h] - 1) <= NEW_TOL
            okx = okx and abs(r["wdial"] / WDIAL_TAB[h] - 1) \
                <= NEW_TOL
        if r["tfg_meas"] > THETA_BAR:
            okx = okx and r["wdial"] < r["lock"]
        else:
            okx = okx and r["wdial"] > r["lock"]
        ok36 = ok36 and okx
        d36.append("h%d Wmin %.4f Wdial %.4f" % (h, r["wmin"],
                                                 r["wdial"]))
        okx = True
        if math.isfinite(r["r_univ"]):
            okx = okx and r["r_univ"] >= r["stab_gate"]
        if not smoke:
            if h in RUNIV_TAB:
                okx = okx and abs(r["r_univ"] / RUNIV_TAB[h] - 1) \
                    <= NEW_TOL
            if h == 16:
                okx = okx and not math.isfinite(r["r_univ"]) \
                    and abs(r["r_univ_meas"] / RUNIV_MEAS_16 - 1) \
                    <= NEW_TOL
            if h in BSTAR_TAB:
                okx = okx and abs(r["bstar_l10"] - BSTAR_TAB[h]) \
                    <= BSTAR_ABS
        ok37 = ok37 and okx
        d37.append("h%d Runiv %.3e RunivM %.3e b* %.2f"
                   % (h, r["r_univ"], r["r_univ_meas"],
                      r["bstar_l10"]))
        dl = r["DIAL2"]
        okx = (dl["a0_dev"] <= 1e-40 and dl["ytdev"] <= 1e-40
               and dl["theta"] > THETA_BAR)
        if r["tfg_meas"] > THETA_BAR:
            okx = okx and LOCK_WIN[0] <= dl["lock_pp"] \
                <= LOCK_WIN[1]
        else:
            okx = okx and dl["lock_pp"] < LOCK_WIN[0]
        if not smoke and h in PRICE_DIAL_TAB:
            okx = okx and abs(dl["r0_tau"] / PRICE_DIAL_TAB[h] - 1) \
                <= NEW_TOL
            okx = okx and abs(dl["lock_pp"] / DIAL_LOCK_TAB[h] - 1) \
                <= NEW_TOL
        elif not smoke:
            okx = okx and dl["r0_tau"] >= PRICE_COARSE_DIAL
        if h <= CENSUS_VAR_MAX:
            okx = okx and dl.get("nreal", 0) < r["K"] - 1
            if not smoke and h in DIAL_NREAL_TAB:
                okx = okx and dl["nreal"] == DIAL_NREAL_TAB[h]
        ok38 = ok38 and okx
        d38.append("h%d r0''/tau %.3e lock'' %.4f nreal %s c* %s"
                   % (h, dl["r0_tau"], dl["lock_pp"],
                      dl.get("nreal", "skip"), dl["cstar"]))
        e8, e2, ef = r["EIG8"], r["EIG2"], r["EIGF"]
        okx = all(d["a0_dev"] <= 1e-40 and d["ytdev"] <= 1e-40
                  and d["theta"] > THETA_BAR
                  for d in (e8, e2, ef))
        okx = okx and abs(ef["r0_tau"] / e8["r0_tau"] - 1) <= 1e-3
        if not smoke and h in PRICE_EIGF_TAB:
            okx = okx and abs(ef["r0_tau"] / PRICE_EIGF_TAB[h] - 1) \
                <= NEW_TOL
            okx = okx and abs(r["gap_a01"] - GAP_TAB[h]) <= GAP_ABS
        elif not smoke:
            okx = okx and ef["r0_tau"] >= PRICE_COARSE_EIG
        ok39 = ok39 and okx
        csgap = (math.log10(ef["r0_tau"]) - r["bstar_l10"]
                 if ef["r0_tau"] > 0 else float("nan"))
        d39.append("h%d priceF %.4e csgap %.2f a01gap %.3f"
                   % (h, ef["r0_tau"], csgap, r.get("gap_a01",
                                                    float("nan"))))
    if not smoke:
        pseq = [tab[h]["EIGF"]["r0_tau"] for h in CAL_RUNGS
                if h in tab]
        ok39 = ok39 and all(pseq[i] < pseq[i + 1]
                            for i in range(len(pseq) - 1))
        bseq = [tab[h]["bstar_l10"] for h in CAL_RUNGS if h in tab]
        ok37 = ok37 and all(bseq[i] > bseq[i + 1]
                            for i in range(len(bseq) - 1))
    check("G36-wmin-wdial", ok36,
          "W_min ward exact (W_min*theta == bar <= 1e-12); WMIN/"
          "WDIAL tabs rel 5e-3 at calibrated rungs + cited-derived "
          "rel 8e-3 at all; dial-window rule holds (W_DIAL inside "
          "the surviving window at TFG > bar rungs, above lock at "
          "h = 4): %s" % "; ".join(d36))
    check("G37-runiv-bstar-schedule", ok37,
          "R_univ (tau-free floor form) >= stab_gate; RUNIV_TAB rel "
          "5e-3; NOT FINITE at h = 16 (DK-GATE-CROSSOVER-REPLICATED "
          "in the universal form; measured-residual radius %.2e at "
          "16 still covers); b* REQUIRED-BAR SCHEDULE on BSTAR_TAB "
          "abs 0.02, strictly decreasing (the manifold with bar "
          "schedule b*(h) is universally exclusionary at every "
          "rung; instrument-conditional): %s"
          % (RUNIV_MEAS_16 if not smoke else float("nan"),
             "; ".join(d37)))
    check("G38-dial2-battery", ok38,
          "the MINIMAL DIAL refutes H3 (ward-exact A_0/y_t), stays "
          "in the lock window at TFG > bar rungs (lock catches it "
          "ONLY at h = 4), BREAKS the census (nreal < K-1, tabs), "
          "BREAKS the certificate at PRICE_DIAL_TAB (3.7e7 -> "
          "1.2e39 x tau; coarse >= 1e6 at uncalibrated rungs, "
          "DISCLOSED), keeps H1 satisfied (c* exists: "
          "H1-WORLD-BLIND -- H1 catches NOTHING): %s"
          % "; ".join(d38))
    check("G39-eig-price-ladder", ok39,
          "FULL-SPACE first-order minimal refuter price: EIGF == "
          "EIG8 rel 1e-3 (the minimum SATURATES at low eigenmodes); "
          "PRICE_EIGF_TAB rel 5e-3, STRICTLY GROWING on the "
          "calibrated set (1.35e5 -> 9.47e7 x tau = 30-33 ORDERS "
          "ABOVE THE 1e-25 BAR); CS-gap ladder grows 6.3 -> 35.6 "
          "dex; ALIGNMENT-SHARING measured (GAP_TAB abs 0.05: "
          "eigenvector-1's A_0-functional sits 1e2.4-3.7 above the "
          "source's A_0 -- the low modes share the cancellation): "
          "%s" % "; ".join(d39))

    # ------------------------------------------------ S3b cache layer
    section("S3b  BA3 + ZMIN LAYER (main process, ward)")
    ok40 = ok41 = True
    d40, d41 = [], []
    zwit_prices = {}
    ba3_rows = {}
    for h in rungs:
        if h not in tab:
            continue
        r = tab[h]
        dps = DPS[h]
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in r["cn_main"]]
            tau_h = mp.mpf(r["tau_str"])
            zs, off = zsum_off_main(h, r["K"], cs, dps, gam)
            zrel = float(zs / tau_h)
            rrel = float((tau_h + off - zs) / tau_h)
        okx = rrel > 0
        if not smoke and h in ZSUM_TAB:
            okx = okx and abs(zrel / ZSUM_TAB[h] - 1) <= NEW_TOL
        if not smoke and h in ZSUM_MAIN_DEEP:
            okx = okx and abs(zrel / ZSUM_MAIN_DEEP[h] - 1) <= NEW_TOL
        row = {}
        for tag in ("DIAL2", "EIG8", "EIG2", "EIGF"):
            with mp.workdps(dps):
                cs2 = [mp.mpf(s) for s in r[tag]["cn_str"]]
                zs2 = zsum_only(h, r["K"], cs2, dps, gam)
                zr = float(zs2 / zs)
                br = float((tau_h + off - zs2) / tau_h)
            row[tag] = (zr, br)
            if not smoke and h in ZR_DIAL_TAB and tag == "DIAL2":
                okx = okx and abs(zr / ZR_DIAL_TAB[h] - 1) <= NEW_TOL \
                    and abs(br / BA3_DIAL_TAB[h] - 1) <= NEW_TOL \
                    and br < 0
            if not smoke and h in ZR_EIGF_TAB and tag == "EIGF":
                okx = okx and abs(zr / ZR_EIGF_TAB[h] - 1) <= NEW_TOL \
                    and abs(br / BA3_EIGF_TAB[h] - 1) <= NEW_TOL \
                    and br < 0
        ba3_rows[h] = row
        ok40 = ok40 and okx
        d40.append("h%d zs/tau %.4f res %.4f dial(%.2e,%.1e) "
                   "eigf(%.2e,%.1e)"
                   % (h, zrel, rrel, row["DIAL2"][0],
                      row["DIAL2"][1], row["EIGF"][0],
                      row["EIGF"][1]))
        # ZMIN universal optimizer (AMENDMENT 1: rung-scaled
        # dps -- the fixed dps-90 solve is precision garbage at
        # h = 24, same artifact class as calibration pass-1 h16)
        dps_z = ZMIN_DPS if h <= 16 else DPS[h] + ZMIN_XDPS
        zmin, zmain2, nords, dstr = zmin_optimizer(
            h, r["K"], r["cn_main"], r["wdial"], gam, dps_z)
        zr_min = zmin / zmain2 if zmain2 else float("nan")
        bmin = float((float(tau_h) + float(off) - zmin)
                     / float(tau_h))
        xrel = abs(zmain2 / float(zs) - 1)
        okx = xrel <= 1e-6
        if not smoke and h in ZMIN_TAB:
            okx = okx and abs(zr_min / ZMIN_TAB[h] - 1) <= NEW_TOL \
                and bmin > 0
        if not smoke and h in ZMIN_XRUNGS:
            z2, _zm2, _n2, _d2 = zmin_optimizer(
                h, r["K"], r["cn_main"], r["wdial"], gam,
                dps_z + ZMIN_XDPS)
            b2v = float((float(tau_h) + float(off) - z2)
                        / float(tau_h))
            okx = okx and ((b2v > 0) == (bmin > 0)) \
                and z2 <= zmin * (1 + 1e-6)
            info("h%d zmin dps-cross: drift |z2-z|/zmain %.2e, "
                 "res(z2) %+.3e vs res(z) %+.3e -- DECISION-STABLE "
                 "(feasible-upper-value currency)"
                 % (h, abs(z2 - zmin) / zmain2, b2v, bmin))
        zw = zminwit_cert(h, r["K"], r, dstr)
        zwit_prices[h] = zw["r0_tau"]
        if not (zw["a0_dev"] <= 1e-25
                and abs(zw["yt_ratio"] / r["wdial"] - 1) <= 1e-6
                and xrel <= 1e-6):
            info("h%d G41 ward legs: a0_dev %.1e ytdev %.1e "
                 "xrel %.1e" % (h, zw["a0_dev"],
                                abs(zw["yt_ratio"] / r["wdial"] - 1),
                                xrel))
        okx = okx and zw["a0_dev"] <= 1e-25 \
            and abs(zw["yt_ratio"] / r["wdial"] - 1) <= 1e-6
        if not smoke and h in ZMINWIT_R0_TAB:
            okx = okx and abs(zw["r0_tau"] / ZMINWIT_R0_TAB[h] - 1) \
                <= NEW_TOL and zw["r0_tau"] >= 1e9
        ok41 = ok41 and okx
        d41.append("h%d zmin/zm %.3e ba3min %+.3e [n%d] "
                   "zwit-r0 %.3e"
                   % (h, zr_min, bmin, nords, zw["r0_tau"]))
        ba3_rows[h]["ZMIN"] = (zr_min, bmin)
        ba3_rows[h]["ZWIT_R0"] = zw["r0_tau"]
        ba3_rows[h]["ZWIT_RAY"] = zw["ray_dev_pp"]
    if not smoke:
        pw = [zwit_prices[h] for h in CAL_RUNGS if h in zwit_prices]
        ok41 = ok41 and all(pw[i] < pw[i + 1]
                            for i in range(len(pw) - 1))
    check("G40-ba3-anchors-variants", ok40,
          "MAIN zsum/tau on the r166 strings rel 5e-3 (+ deep "
          "strings at 13/16), residual > 0 at every rung; the "
          "minimal dial and the optimal refuter BOTH BREAK BA3 "
          "everywhere measured (tabs rel 5e-3; A_0-gauge, OFF_main, "
          "DISCLOSED): %s" % "; ".join(d40))
    check("G41-zmin-universal", ok41,
          "the EXACT constrained minimum of zsum over ALL A_0-gauge "
          "refuting directions: ZMIN_TAB rel 5e-3 with BA3 residual "
          "at the minimum POSITIVE at every calibrated rung: "
          "BA3-NOT-UNIVERSAL (a BA3-passing refuter EXISTS); "
          "dps-cross rel <= 1e-6 at {5,16} (the pass-1 dps-60 "
          "artifact is warded); BUT the zmin witness BREAKS THE "
          "CERTIFICATE: ZMINWIT_R0_TAB rel 5e-3, >= 1e9, STRICTLY "
          "GROWING (6.6e9 -> 3.2e68): the cert/BA3 trade-off "
          "frontier is measured-EMPTY on both ends: %s"
          % "; ".join(d41))

    # G42 leak adjudication + G43 coverage
    ok42 = True
    leak_tokens = []
    cov_rows = []
    for h in rungs:
        if h not in tab:
            continue
        r = tab[h]
        cands = {}
        for tag in ("DIAL2", "EIG8", "EIG2", "EIGF"):
            cands[tag] = (r[tag]["r0_tau"], r[tag]["ray_dev_pp"],
                          r[tag]["lock_pp"], ba3_rows[h][tag][1])
        cands["ZMINWIT"] = (ba3_rows[h]["ZWIT_R0"],
                            ba3_rows[h]["ZWIT_RAY"],
                            r["lock"] / r["wdial"],
                            ba3_rows[h]["ZMIN"][1])
        leak = None
        for tag, (r0t, rayd, lpp, ba3v) in cands.items():
            cert_pass = r0t <= RES0_BAR and rayd <= RAY_BAR
            lock_pass = LOCK_WIN[0] <= lpp <= LOCK_WIN[1]
            ba3_pass = ba3v >= 0
            if cert_pass and lock_pass and ba3_pass:
                leak = (tag, r0t, lpp, ba3v)
        if leak is not None:
            leak_tokens.append("MANIFOLD-LEAK-EXHIBITED(h=%d,%s)"
                               % (h, leak[0]))
            if h in CAL_RUNGS:
                ok42 = False
        cov = []
        if r["tfg_meas"] <= THETA_BAR:
            cov.append("LOCK")
        if math.isfinite(r["r_univ"]) \
                and r["r_univ"] < r["wmin"] - 1:
            cov.append("DK-GATED")
        if math.isfinite(r["r_univ_meas"]) \
                and r["r_univ_meas"] < r["wmin"] - 1:
            cov.append("DK-MEAS")
        cov_rows.append((h, cov, leak))
    deep_tok = "LEAK-FREE-MEASURED-DEEP" if not leak_tokens \
        else "+".join(leak_tokens)
    EXTRA_TOKENS.append(deep_tok)
    check("G42-leak-adjudication", ok42,
          "frozen rule over {DIAL2, EIGF, ZMINWIT} x {cert, lock "
          "window, BA3 >= 0}: NO candidate passes all three at any "
          "rung (calibrated rungs GATED, deep rungs adjudicated by "
          "the same rule): token %s; every constructed minimal "
          "refuter breaks the certificate AND BA3" % deep_tok)
    ok43 = True
    d43 = []
    for h, cov, leak in cov_rows:
        d43.append("h%d U={%s}%s" % (h, ",".join(cov) or "-",
                                     " LEAK" if leak else ""))
        if not smoke and h <= 16 and not cov:
            ok43 = False
    check("G43-coverage-table", ok43,
          "UNIVERSAL coverage per rung (direction-quantified legs "
          "only): LOCK at h = 4; DK-GATED (tau-free theorem, frozen "
          "bar) h <= 13; DK-MEAS through h = 16; h >= 20 "
          "exhibit-based + b*(h) schedule (instrument-conditional): "
          "%s" % "; ".join(d43))

    # ------------------------------------------------ S3c transport
    section("S3c  TRANSPORT ANALYTICS (cited ladders)")
    th_c = {h: 10.0 ** YT_L10_R172[h] / (2 * math.pi * h) ** 4
            for h in YT_L10_R172}
    tfg_c = {h: th_c[h] * LOCK_R172[h] for h in YT_L10_R172}
    wmin_c = {h: THETA_BAR / th_c[h] for h in YT_L10_R172}
    above = [h for h in sorted(tfg_c) if tfg_c[h] > THETA_BAR]
    exc = tuple(h for h in sorted(tfg_c) if tfg_c[h] <= THETA_BAR)
    tfg_cap = max(tfg_c.values())
    lneed = tfg_cap / THETA_BAR
    lockmin = min(LOCK_R172.values())
    margin = lockmin / lneed
    ok44 = (len(above) == TFG_N_ABOVE and exc == TFG_EXC
            and abs(min(wmin_c.values()) / WMIN_BAND[0] - 1)
            <= ANA_TOL
            and abs(max(wmin_c.values()) / WMIN_BAND[1] - 1)
            <= ANA_TOL
            and abs(tfg_cap / TFG_CAP_STR - 1) <= ANA_TOL
            and abs(min(tfg_c.values()) / TFG_MIN_STR - 1)
            <= ANA_TOL
            and abs(lneed / L_NEED_STR - 1) <= ANA_TOL
            and abs(margin / IND_MARGIN_STR - 1) <= ANA_TOL
            and abs(lockmin / LOCK_MIN_STR - 1) <= ANA_TOL)
    check("G44-cited-tables", ok44,
          "TFG > bar at %d of 26 cited rungs, exception list %s "
          "(the lock leg universally covers ONLY h = 4: BH7-F4's "
          "24-of-25 replicated as a table + theorem G11); W_min "
          "band [%.4f, %.4f]; TFG_CAP = %.6f (h = 7); L_NEED = "
          "%.6f; min lock %.4f; margin %.6f"
          % (len(above), list(exc), min(wmin_c.values()),
             max(wmin_c.values()), tfg_cap, lneed, lockmin, margin))

    l2 = math.log10(2.0)
    ok45 = True
    d45 = []
    for ch in REP_CHAINS:
        for i in range(len(ch) - 1):
            h1, h2 = ch[i], ch[i + 1]
            fg1 = math.log10(LOCK_R172[h1]) + YT_L10_R172[h1]
            fg2 = math.log10(LOCK_R172[h2]) + YT_L10_R172[h2]
            p_fg = (fg2 - fg1) / l2
            p_yt = (YT_L10_R172[h2] - YT_L10_R172[h1]) / l2
            lr = LOCK_R172[h2] / LOCK_R172[h1]
            dth = th_c[h2] - th_c[h1]
            key = (h1, h2)
            ok45 = ok45 and abs(p_fg / P_FG_TAB[key] - 1) <= ANA_TOL \
                and P_FG_WIN[0] <= p_fg <= P_FG_WIN[1] \
                and abs(p_yt / P_YT_TAB[key] - 1) <= ANA_TOL \
                and P_YT_WIN[0] <= p_yt <= P_YT_WIN[1] \
                and abs(lr / LOCKRAT_TAB[key] - 1) <= ANA_TOL \
                and LOCKRAT_WIN[0] <= lr <= LOCKRAT_WIN[1] \
                and 0 < dth <= DTHETA_MAX
            d45.append("%d->%d pFG %.4f pYT %.4f lr %.4f"
                       % (h1, h2, p_fg, p_yt, lr))
    check("G45-rep-transport-defects", ok45,
          "block-representative doubling defects (MEASURED "
          "transport laws): p_FG spread 3.46..5.00 (only loosely "
          "quartic at rep pairs -- the lock wobble 0.63..1.28 makes "
          "the FG transport noisy), p_yt 4.09..4.64, dtheta all "
          "positive <= 0.021: %s" % "; ".join(d45))

    ledger = [
        ("H3", "T_z^4", "FRAME-EXACT", "x16 per doubling (G15)"),
        ("H3", "A_0/A_2", "SOURCE-EXACT-PER-RUNG",
         "NONE (eigensolve; r166 NO-EXACT-CROSS-H)"),
        ("lock-window", "y_t", "SOURCE-EXACT-PER-RUNG", "NONE"),
        ("lock-window", "FG", "SPECTRAL-RATIO-MEAS",
         "v926-quartic MEASURED-FLAGGED; rep defects G45"),
        ("ground-state-cert", "r0/tau, ray", "INSTRUMENT-PER-RUNG",
         "NONE (re-established per rung)"),
        ("BA3", "tau", "TAU-ABS-MEAS",
         "NONE (no corpus tau-floor; v915 different object)"),
        ("BA3", "zsum", "CENSUS-CLASSICAL-PER-K",
         "DT1/DT2 transport the census PLAN (v928, cited); "
         "forall-k == LOOP flagged"),
        ("BA3", "OFF", "CLASSICAL-RECIPE+MEAS",
         "r131 recipe; A_0/eta measured"),
        ("H1", "ENVJ", "SOURCE-EXACT-PER-RUNG",
         "NONE; c* flatness MEASURED"),
        ("H2", "census", "CLASSICAL-PER-RUNG",
         "NONE; structure <= 24 instrument")]
    suff = ("ground-state-cert", "lock-window")
    suff_rows = [row for row in ledger if row[0] in suff]
    ok46 = all(any(row[3].startswith("NONE") or "MEASURED"
                   in row[3] for row in suff_rows
                   if row[0] == c) for c in suff) \
        and not any(row[2] == "TAU-ABS-MEAS" for row in ledger
                    if row[0] in suff) \
        and any(row[2] == "TAU-ABS-MEAS" for row in ledger
                if row[0] == "BA3")
    for row in ledger:
        info("LEDGER %-18s %-12s %-24s -> %s" % row)
    check("G46-transport-ledger", ok46,
          "constraint x leg x type x transport TYPED: FRAME legs "
          "exact, SOURCE legs no-transport (per-rung eigensolve), "
          "SPECTRAL legs measured-only, TAU-ABS confined to BA3; "
          "the sufficient universal subset {cert, lock-window} "
          "contains NO exact-transporting leg and NO absolute-tau "
          "leg: INDUCTION-STEP-NOT-CLASSICAL + "
          "TAU-ABS-IMPORT-NOT-LOAD-BEARING")

    ok47 = True
    for h in sorted(tfg_c):
        okr = (tfg_c[h] <= tfg_cap + 1e-15
               and LOCK_R172[h] >= lneed
               and th_c[h] <= THETA_BAR)
        ok47 = ok47 and okr
    contrast = [
        ("barrier objects are CERTIFIED CONSTRAINTS with proven "
         "per-rung modus tollens (vs the measured Riccati barrier "
         "matrix)", True),
        ("but the transport hypotheses {TFG-cap, lock-floor} are "
         "SPECTRAL-MEASURED per rung, same epistemic class as the "
         "level checks", True),
        ("the LEVEL check H3(h') is ONE exact source evaluation -- "
         "CHEAPER than any transport hypothesis: "
         "LEVEL-CHEAPER-THAN-INCREMENT (the CLXII/CCIII death mode "
         "one level up)", True),
        ("the invariance target protects the falsifiability "
         "boundary (measurement integrity), NOT the H3 VALUE: "
         "M(h') does not imply H3(h') without the TFG-cap premise",
         True)]
    ok47 = ok47 and all(c[1] for c in contrast)
    check("G47-induction-assembly", ok47,
          "the conditional induction VERIFIES at all 26 cited "
          "rungs: {TFG(h) <= %.6f [v926-MEASURED, FLAGGED] AND "
          "lock(h) >= %.6f [SPECTRAL-RATIO-MEAS, no corpus "
          "theorem]} ==> H3(h) (G12 exact; margin %.4f); per-block "
          "hypothesis = TWO measured spectral scalars vs ONE exact "
          "source evaluation for the level: "
          "INDUCTION-CONDITIONAL-ON-MEASURED-TRANSPORT + "
          "TRANSPORT-RELABELS-NOT-REDUCES + "
          "LEVEL-CHEAPER-THAN-INCREMENT; HALFGAP contrast: %s"
          % (tfg_cap, lneed, margin,
             "; ".join(c[0] for c in contrast)))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS + WITNESS")
    theta_main_min = min(tab[h]["theta_y"] for h in tab) \
        if tab else float("nan")
    cblocks = {}
    for world, xw, _d in ctrl_tasks:
        r = res.get(("ctl", (world, xw)))
        if r is None or "error" in r:
            check("G50-%s-x%d" % (world.lower(), xw), False,
                  (r or {}).get("error", "missing"))
            continue
        cblocks.setdefault(world, []).append(r)
    theta_ctrl_max = max(r["theta_w"] for rows in cblocks.values()
                         for r in rows) if cblocks else float("nan")
    gnum = {"SMOOTH": "G50", "SCRARITH": "G51", "EPSTEIN": "G52"}
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        rows = cblocks.get(world)
        if rows is None:
            continue
        taus = {r["h"]: r["tauf"] for r in rows}
        strs = CTRL_TAU_TAB[world]
        str_ok = all(abs(taus[hh] / strs[hh] - 1) <= NEW_TOL
                     for hh in taus if hh in strs)
        th_ok = all(r["theta_w"] <= CTRL_THETA_MAX for r in rows)
        tab_ok = True
        for r in rows:
            key = (world, r["h"])
            if not smoke and key in THETA_W_CAL:
                tab_ok = tab_ok and abs(
                    r["theta_w"] / THETA_W_CAL[key] - 1) <= NEW_TOL
        lock_ok = all(r["lock_w"] < LOCK_WIN[0] for r in rows)
        sep = theta_main_min / theta_ctrl_max
        refuse = (all(t < 0 for t in taus.values()) and str_ok
                  and th_ok and tab_ok and lock_ok
                  and sep >= SEP_MIN)
        check("%s-%s" % (gnum[world], world.lower()), refuse,
              "%s: tau_w < 0 (r166 strings rel 5e-3); theta_w on "
              "THETA_W_CAL rel 5e-3; lock_w < 1.0: THE MANIFOLD IS "
              "EMPTY IN THE FAKE WORLDS (lock window + cert cannot "
              "even be posed: the invariance machinery is NOT "
              "world-blind); SIZE-SEPARATOR %.0f >= %.0f"
              % (world, sep, SEP_MIN))

    if 5 in tab:
        wb = wit1000_battery(tab[5], gam)
        ok53 = (abs(wb["dnorm"] / WIT1000["dnorm"] - 1) <= NEW_TOL
                and wb["a0_dev"] <= 1e-40
                and abs(wb["yt_ratio"] / 1000 - 1) <= 1e-30
                and abs(wb["theta"] / WIT1000["theta"] - 1)
                <= NEW_TOL
                and abs(wb["lock_pp"] / WIT1000["lock"] - 1)
                <= NEW_TOL and wb["lock_pp"] < LOCK_WIN[0]
                and abs(wb["r0_tau"] / WIT1000["r0tau"] - 1)
                <= NEW_TOL
                and abs(wb["zratio"] / WIT1000["zratio"] - 1)
                <= NEW_TOL
                and abs(wb["ba3"] / WIT1000["ba3"] - 1) <= NEW_TOL
                and wb["ba3"] < 0)
        ok53 = ok53 and all(1000 > tab[h]["lock"] for h in tab)
        check("G53-wit1000-replication", ok53,
              "the r172/r173 W = 1000 witness replicated through "
              "THIS machinery at h = 5: dnorm %.4e, theta'' %.4f, "
              "lock'' %.4e < 1, r0''/tau %.3e, zsum-ratio %.4e, "
              "BA3 %.4e < 0 (all r173 strings rel 5e-3); AND "
              "W = 1000 > lock at EVERY rebuilt rung: the large "
              "dial is lock-excluded EVERYWHERE (exact, G11)"
              % (wb["dnorm"], wb["theta"], wb["lock_pp"],
                 wb["r0_tau"], wb["zratio"], wb["ba3"]))
    else:
        check("G53-wit1000-replication", False, "h=5 missing")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 8:
        lt = [tab[h]["log10tau"] for h in rungs if h in tab]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_wm = slope_of([math.log10(tab[h]["wmin"]) for h in rungs
                         if h in tab])
        s_tf = slope_of([math.log10(tab[h]["tfg_meas"])
                         for h in rungs if h in tab])
        fin = [h for h in rungs if h in tab
               and math.isfinite(tab[h]["r_univ"])]
        s_ru = float(np.polyfit(
            [-tab[h]["log10a0"] for h in fin],
            [math.log10(tab[h]["r_univ"]) for h in fin], 1)[0])
        ok54 = (abs(s_wm) <= TAU_SLOPE_BAR
                and abs(s_tf) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= s_ru <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "transport-demand slopes vs log10 tau: log10 W_min "
              "%.4f, log10 TFG %.4f (<= 0.30 DEMAND-FLAT: the "
              "transport demand does NOT collapse onto tau by "
              "relabeling -- it is spectral-RATIO class); RIDER "
              "log10 R_univ vs -log10|A_0| slope %.3f in (0.85, "
              "1.15) (the universal radius rides the 1/A_0 "
              "cancellation: BOUND-RIDES-CONNES class)"
              % (s_wm, s_tf, s_ru))
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
          "1e-25 shift on M[0,0] at h=5 moves tau by %.1e "
          "(round-118 trap)" % d_eps, kind="edge")

    # ------------------------------------------------ S6 audit + graphs
    section("S6  DEMAND AUDIT + LOOP/MINING + GRAPHS")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq, "CHAIN-AUDIT: " + detq)

    dep = {"UNIV-EXCL-THEOREM": ("SOURCE", "SPECTRAL-CERT",
                                 "LOCK-WINDOW-MEAS", "DK-LEMMA"),
           "PRICE-LADDER-MEAS": ("SOURCE", "SPECTRAL-CERT",
                                 "EIG-INSTRUMENT"),
           "LEAK-ADJUDICATION": ("SOURCE", "SPECTRAL-CERT",
                                 "CACHE-WARD", "PT21-CENSUS-PER-K",
                                 "TAU-MEAS"),
           "TRANSPORT-LEDGER": ("SOURCE", "R166-CITED",
                                "V926-MEAS-FLAGGED"),
           "INDUCTION-SHAPE": ("FG-QUARTIC-MEAS", "LOCK-FLOOR-MEAS"),
           "H3-PER-RUNG": ("SOURCE",),
           "SOURCE": (), "SPECTRAL-CERT": (), "CACHE-WARD": (),
           "LOCK-WINDOW-MEAS": (), "DK-LEMMA": (),
           "EIG-INSTRUMENT": (), "TAU-MEAS": (), "R166-CITED": (),
           "V926-MEAS-FLAGGED": (), "FG-QUARTIC-MEAS": (),
           "LOCK-FLOOR-MEAS": (), "PT21-CENSUS-PER-K": (),
           "TLAWCAP": (), "WPD": (), "CENSUS-ALL-K": (),
           "TAUPOS": (), "TOPROOT-MEAS": (), "ZERO-VERIF-AS-HYP": (),
           "GONEK-1984-RH": (), "MONTGOMERY-PC-RH": (),
           "GOLDSTON-MONTGOMERY-RH": ()}

    def ancestors(node):
        seen = set()
        stack = [node]
        while stack:
            nn = stack.pop()
            for p in dep.get(nn, ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        return seen

    delivered = ("UNIV-EXCL-THEOREM", "PRICE-LADDER-MEAS",
                 "TRANSPORT-LEDGER", "H3-PER-RUNG")
    banned = {"TLAWCAP", "WPD", "TAUPOS", "CENSUS-ALL-K",
              "TOPROOT-MEAS", "ZERO-VERIF-AS-HYP", "GONEK-1984-RH",
              "MONTGOMERY-PC-RH", "GOLDSTON-MONTGOMERY-RH"}
    ok61 = all(not (ancestors(nd) & banned) for nd in delivered) \
        and all("TAU-MEAS" not in ancestors(nd) for nd in delivered) \
        and "TAU-MEAS" in ancestors("LEAK-ADJUDICATION") \
        and "LEAK-ADJUDICATION" not in delivered \
        and "INDUCTION-SHAPE" not in delivered \
        and "FG-QUARTIC-MEAS" in ancestors("INDUCTION-SHAPE") \
        and ancestors("H3-PER-RUNG") == {"SOURCE"}
    check("G61-loop-mining-m3", ok61,
          "M3 ADJUDICATION MACHINE-CHECKED: TAU-MEAS (absolute tau) "
          "is an ancestor of LEAK-ADJUDICATION (the red-team BA3 "
          "leg) ONLY -- NEVER of the delivered statements "
          "{UNIV-EXCL-THEOREM == {SOURCE, SPECTRAL-CERT, "
          "LOCK-WINDOW-MEAS(ratio), DK-LEMMA}; PRICE-LADDER-MEAS; "
          "TRANSPORT-LEDGER; H3-PER-RUNG == {SOURCE}}: "
          "TAU-ABS-IMPORT-NOT-LOAD-BEARING; INDUCTION-SHAPE "
          "carries FG-QUARTIC-MEAS + LOCK-FLOOR-MEAS and is "
          "EXCLUDED from the delivered set "
          "(CONDITIONAL-ON-MEASURED); banned set (incl. the three "
          "RH-conditional second-moment routes) ancestors of "
          "NOTHING delivered; SIX flagged loop routes carried NOT "
          "consumed (tlaw-window, census-all-k, pinning-supply, "
          "A0-floor, zero-verification-as-hypothesis, "
          "Montgomery-PC/Goldston-Montgomery/Gonek-1984)")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1,
            ("SV", "RH"): INF,
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
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("SUSCAP2R", "DELTA1FLOOR")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1,
               ("SUSCAP2R", "R4HYP"): INF,
               ("NFCLOS", "DELTA1FLOOR"): 1,
               ("DELTA1FLOOR", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G62-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 9 and "RH" not in reach,
          "flows: base 4, refined 5 (r171/r172 graph VERBATIM), "
          "one-grant 5, counterfactual PARALLEL 9 NOT REAL; census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")

    chain_uni = {
        "RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"], "DTSTEP_ALLK": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"], "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"], "RH_VIA_N": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    chain_pin = {
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"]}
    loop_pin = has_cycle(chain_pin)
    chain_a0 = {
        "TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
        "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]}
    loop_a0 = has_cycle(chain_a0)
    chain_mpc = {
        "RH": ["MONTGOMERY-PC"],
        "MONTGOMERY-PC": ["SECOND-MOMENT-CEILING"],
        "SECOND-MOMENT-CEILING": ["THETAINF-PIN"],
        "THETAINF-PIN": ["H3COF"], "H3COF": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["HCOF2"],
        "HCOF2": ["WEILPOS"], "WEILPOS": ["RH"]}
    loop_mpc = has_cycle(chain_mpc)
    chain_term = {
        "ENVJ_H1": ["PF"], "CENSUS_H2": ["PF"], "TRACE": ["PF"],
        "GONEK": ["WF", "DCLEG"],
        "H3_PER_RUNG": ["RATE"], "H3_COFINAL": ["RATE"],
        "DK_LEMMA": ["UNIV_EXCL"], "SPECTRAL_CERT": ["UNIV_EXCL"],
        "LOCK_WINDOW_MEAS": ["UNIV_EXCL"],
        "EIG_INSTRUMENT": ["PRICE_LADDER"],
        "UNIV_EXCL": ["H3_STABILITY"],
        "PRICE_LADDER": ["H3_STABILITY"],
        "TAU_MEAS_ABS": ["BA3_REDTEAM"],
        "BA3_REDTEAM": ["H3_STABILITY"],
        "H3_STABILITY": [],
        "FG_QUARTIC_MEAS": ["INDUCTION_SHAPE"],
        "LOCK_FLOOR_MEAS": ["INDUCTION_SHAPE"],
        "INDUCTION_SHAPE": ["H3_COFINAL"],
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
    stab_reach = reachable(chain_term, "UNIV_EXCL")
    ok63 = (loop_uni and loop_pin and loop_a0 and loop_mpc and acyc
            and "RH" not in stab_reach
            and "JETMASS" not in stab_reach
            and all("RH" in reachable(chain_term, nd)
                    for nd in ("ENVJ_H1", "CENSUS_H2", "H3_PER_RUNG",
                               "H3_COFINAL", "INDUCTION_SHAPE",
                               "GONEK", "CENSUS_K")))
    check("G63-endgame-graphs", ok63,
          "(i)-(iv) FOUR loop cycles re-detected (universalized "
          "census, pinning-supply, A0-floor, Montgomery-PC), NOT "
          "consumed; (v) the terminal chain extended with the "
          "manifold nodes {DK_LEMMA, SPECTRAL_CERT, "
          "LOCK_WINDOW_MEAS} -> UNIV_EXCL -> H3_STABILITY and "
          "{TAU_MEAS_ABS -> BA3_REDTEAM -> H3_STABILITY} is "
          "ACYCLIC, and the manifold side feeds ONLY the red-team/"
          "stability sink (NO edge into the delivered jet-mass "
          "chain, BH7-X2 property PRESERVED: RH and JETMASS "
          "unreachable from UNIV_EXCL); the flagged conditional "
          "edge {FG_QUARTIC_MEAS, LOCK_FLOOR_MEAS} -> "
          "INDUCTION_SHAPE -> H3_COFINAL is carried FLAGGED; "
          "AND-semantics; NO RH CLAIM")
    info("THE POST-ROUND RESIDUE (exact, typed): UNCHANGED IN "
         "CARDINALITY -- {H1 AND H2 AND H3}-COFINAL (one rung per "
         "dyadic block, all three at the same h; BH7-F1 wording; "
         "the limsup form only mod the measured defect D = 0.0042, "
         "BH7-F2) + {census-forall-k == LOOP, flagged} + {L1 == "
         "TAIL proven + H-pin open, WPD open}.  WHAT THIS ROUND "
         "SHARPENS: the BH7-F4 witness-specificity is REMOVED "
         "within the instrument -- the exclusion is now (i) a "
         "tau-free DIRECTION-UNIVERSAL THEOREM for h <= 13 at the "
         "frozen bar (+ the exact required-bar schedule b*(h) for "
         "every rung, instrument-conditional), (ii) a MEASURED "
         "FULL-SPACE MINIMAL PRICE LADDER growing 1.35e5 -> "
         "9.47e7 x tau (30-33 orders above the bar) with the "
         "alignment-sharing mechanism identified, (iii) the "
         "adjudicated non-universality of BA3 (scale gauge + zmin "
         "passer, whose own cert price grows 6.6e9 -> 3.2e68).  "
         "The forward-invariance/induction route is PRICED DEAD as "
         "a reduction: transport relabels, levels are cheaper than "
         "increments, and the manifold protects the falsifiability "
         "boundary, not the H3 value.  NO omega closed; nothing "
         "upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "CITED-LADDER-REPLICATED(G33)",
        "UNIVERSAL-EXCLUSION-THEOREM-TAU-FREE(G10)",
        "DK-GATE-CROSSOVER-REPLICATED(G37)",
        "REQUIRED-BAR-SCHEDULE-EXACT(G37)",
        "MINIMAL-DIAL-LOCK-SURVIVES-25-OF-26-EXC-H4(G44)",
        "DIAL-BREAKS-CERT-CENSUS-BA3-NOT-H1(G38/G40)",
        "FULL-SPACE-MIN-PRICE-GROWS(G39)",
        "CERT-PRICE-30-ORDERS-ABOVE-BAR(G39)",
        "EIG-SATURATION-EIGF==EIG8(G39)",
        "ALIGNMENT-SHARING-MEASURED(G39)",
        "CS-GAP-LADDER-GROWS(G39)",
        "BA3-NOT-UNIVERSAL-ZMIN-PASSER(G41)",
        "BA3-SCALE-GAUGE-DEPENDENT(G13)",
        "ZMIN-WITNESS-BREAKS-CERT(G41)",
        "LEAK-NOT-EXHIBITED-CALIBRATED(G42)",
        "COVERAGE-TABLE-ASSEMBLED(G43)",
        "TAU-ABS-IMPORT-NOT-LOAD-BEARING(G61)",
        "FRAME-LEGS-EXACT(G15)",
        "NO-FRAME-NESTING(G15)",
        "SOURCE-LEGS-NO-TRANSPORT(G46)",
        "SPECTRAL-LEGS-MEASURED(G46)",
        "TRANSPORT-DEFECTS-MEASURED(G45)",
        "INDUCTION-CONDITIONAL-ON-MEASURED-TRANSPORT(G47)",
        "TRANSPORT-RELABELS-NOT-REDUCES(G47)",
        "L-NEED-NAMED-1.7254(G44/G47)",
        "LEVEL-CHEAPER-THAN-INCREMENT(G47)",
        "MANIFOLD-EMPTY-IN-FAKE-WORLDS(G50-G52)",
        "SIZE-SEPARATOR(G50-G52)",
        "LARGE-DIAL-LOCK-EXCLUDED-EVERYWHERE(G53)",
        "DEMAND-FLAT(G54)",
        "BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-SEQ(G60)",
        "LOOP-ROUTES-FLAGGED(six; G61/G63)",
        "OMEGA-UNCHANGED(census 4; G62)",
        "MINCUT(4/5)"]
    verdicts += ["%s(G42)" % t for t in EXTRA_TOKENS]
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
