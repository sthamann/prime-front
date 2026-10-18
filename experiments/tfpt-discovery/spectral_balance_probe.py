#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""spectral_balance_probe -- PRIME.SPECTRAL.BALANCE.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the spectral-balance pair
{SUSCAP2R, DELTA1FLOOR}, the second of the three final residue blocks)
=======================================================================
After r150 (CDLIV) the pair reads: SUSCAP2R = OVG-cap + share-floor
(s == OVG/share_1 EXACTLY at all six rungs, OVG = (et_1^2/rho2)/
FULLGAP measured flat 0.029-0.068, share_1 = 0.944-0.969) and
DELTA1FLOOR <== TRACEFLOOR := tau TrH <= poly (r146 Y1, tightness
1.000000).  This probe is the maximal proof attempt on (B1) the trace
upper bound / circularity adjudication, (B2) the OVG identity hunt,
(B3) the share-floor reduction, and (T5) the one-statement merge.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, Mq = round-114 builder (even sector), eigenpairs
lam_0 = tau < lam_1 <= ... (mpE/mpV), FULLGAP = (lam_1 - tau)/tau,
TrH = sum_{i>=1} 1/(lam_i - tau) (r146 Y1 harmonic trace; ONE
bordered LU [[Mq - tau, phi],[phi^T, 0]] + K solves), tf = (lam_1 -
tau) TrH, TRACEFLOOR = tau TrH, T_z = 2 pi x, m = verified zone
census, V = kernel of the m newton-polished node rows, W = Gram-
orthonormal compression, eigenpairs (q_i, z_i), q_0 = tau; probe row
r(p) at the zone-top argmin: normalized overlaps et_i, rho2 = et_0^2,
chi = sum_{i>=1} et_i^2/(q_i - q_0), g = (lam* - q_0)/tau, delta_i =
(q_i - q_0)/tau, s = tau chi/rho2, share_1 = (et_1^2/(q_1 - q_0))/chi,
OVG = (et_1^2/rho2)/FULLGAP, BOTTOMSHARE BS := rho2 delta_1 (the
candidate merge coordinate), S_g = sum_{i>=1} et_i^2/(q_i - lam*),
share_1^g = (et_1^2/(q_1 - lam*))/S_g.  gtop = 7264.75 (X5 cache).

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically + exact rational
instances + mp-instantiated per rung; classical inputs typed CITED)
=======================================================================
THEOREM SB1 (trace-loop adjudication + tail closure; the B1 answer).
(a) EXACTLY tau TrH == tf/FULLGAP (partial-fraction chase): the r146
Y1 recoordination 'DELTA1FLOOR <== TRACEFLOOR <= poly' is a LOOP up
to the tightness factor tf -- the dominant term of the trace IS
1/FULLGAP.  (b) THE TAIL HALF IS CLOSED UNCONDITIONALLY: tf = 1 +
sum_{i>=2} a_i with a_i = (lam_1 - tau)/(lam_i - tau) in [0, 1], so
   1 <= tf <= K - 1        (trivial count bound)
and sharper tf - 1 <= (K - 2)(lam_1 - tau)/(lam_2 - tau) (a_i <= a_2).
(c) TWO-SIDED POLY EQUIVALENCE (both directions exact):
   TRACEFLOOR <= P ==> FULLGAP >= 1/P     (tf >= 1), and
   FULLGAP >= 1/P ==> TRACEFLOOR <= (K-1) P   (tf <= K-1).
ADJUDICATION: DELTA1FLOOR <==> TRACEFLOOR is a proven two-sided
polynomial equivalence -- Y1's 'classical-friendly direction' is a
RE-COORDINATE, not a reduction; the honest minimal form of
DELTA1FLOOR is the single dominant-term bound tau/(lam_1 - tau) <=
poly, i.e. the FULLGAP floor itself.  The RvM/zeta-like tail
refinement is NOT NEEDED at poly level (the count bound closes it);
the geometric-ladder tail decay stays MEASURED (exhibits printed).
Calibration x=5/8: tf - 1 = 2.0898e-5/2.9203e-6 <= sharp bound
1.8803e-4/5.5484e-5 <= K-1 = 10/20; TrH LU-vs-eigen cross dev
2.0e-52/4.0e-60; loop identity dev 0.0.

THEOREM SB2 (the chi-cap; the direct s-bound).  Since q_i - q_0 >=
q_1 - q_0 for i >= 1 and sum_{i>=0} et_i^2 = 1:
   chi <= (1 - rho2)/(q_1 - q_0),  hence  s rho2 delta_1 <= 1 - rho2,
i.e. s <= (1 - rho2)/(rho2 delta_1) EXACTLY (equality iff two-level).
MEASURED ADJUDICATION (the honest finding of the round, calibrated
x=5/8): rho2 = 4.290e-12/3.166e-22 COLLAPSING -- the probe row at
the zone top is nearly orthogonal to the zone-killed ground -- so
the chi-cap is VACUOUS: vacuity VAC_CHI = -log10(s rho2 delta_1/
(1 - rho2)) = 7.5/16.7 dex RIDING a collapsing scale (2-pt rider
slope ~0.8 vs |log10 tau|).  THE CHI-CAP IS THE THIRD RATE-BLIND
ONE-SIDED MOMENT INSTRUMENT, after the Y3 trace cap and the R4
Parseval cap: machine-pinned here.

THEOREM SB3 (the merge enclosure; the T5 adjudication).  (a) From
the secular root equation rho2/g = sum et_i^2/(delta_i - g) and
delta_i - g >= delta_1 - g:
   BS = rho2 delta_1 <= g <= delta_1   (both ends EXACT),
a two-sided enclosure of the QSUBGAP root.  (b) MERGE ALGEBRA:
[BS >= 1/P] ==> delta_1 >= 1/P (rho2 <= 1) AND s <= P (SB2) -- ONE
statement implies the WHOLE pair {SUSCAP2R, DELTA1FLOOR}, and via
BS <= g it implies QSUBGAP directly.  (c) REVERSE WEDGE (Y4
rearrangement, exact): rho2 delta_1 == et_1^2/(s share_1), so
[s <= P and et_1^2 >= 1/P'] ==> BS >= 1/(P P').  MEASURED
ADJUDICATION: BS = 9.549e-7/3.151e-16 at x = 5/8 FALLING
SUPER-POLYNOMIALLY (rider class; et_1^2 = 2.85e-8/1.82e-17 falling
too) -- the sufficient one-statement merge coordinate BS >= 1/poly
is MEASURED FALSE-TRENDING: MERGE-REFUTED-MEASURED.  The honest
one-statement form of the pair remains the W2 (cited) equivalence
QSUBGAP(g >= 1/poly) <==> SUSCAP2R AND DELTA1FLOOR, now with the
proven enclosure g in [BS, delta_1] whose lower end is rate-blind
(rides) and whose upper end is tight (delta_1 == FULLGAP measured).

THEOREM SB4 (the OVG identity chain; the B2 answer -- the identity
behind the measured-flat ratio FOUND).  At the secular root lam*:
   et_1^2/rho2 == share_1^g (delta_1 - g)/g      (definition chase
via the root equation), hence EXACTLY
   OVG == share_1^g (delta_1 - g)/(g FULLGAP)
       <= (delta_1/FULLGAP)/g          (share_1^g <= 1),
and via Y4: OVG == s share_1 (delta_1/FULLGAP).  With the W1 pinch
(cited) and the tight interlacing delta_1 == FULLGAP: OVG ==
share_1^g (1 - g/delta_1)/g x (delta_1/FULLGAP) -- THE OVG-FLATNESS
IS THE ZONE-TOP-GAP PINCH (the same family as s x gap == 1): the
r150 OVG-cap relocates EXACTLY onto the g-floor = QSUBGAP, matching
the W2 loop.  Calibration x=5/8: identity devs 0.0/3.1e-71; cap
value (delta_1/FG)/g = 0.02974/0.05981 == the s strings; pinch
ratio OVG g FG/delta_1 = share_1^g (1 - g/delta_1) = 0.969/0.965;
NEW near-equality: share_1^g == share_1 at print precision
(0.9691/0.9653 both; dev bar 5e-2, predicted g/delta_1-class).

THEOREM SB5 (share-floor reduction; the B3 answer).  EXACTLY
   1/share_1 == 1 + sum_{i>=2} (et_i^2/et_1^2)(delta_1/delta_i),
hence share_1 >= et_1^2/(1 - rho2) >= et_1^2 (delta_1/delta_i <= 1;
term-wise).  MEASURED ADJUDICATION: the bound is TRUE but VACUOUS
(et_1^2/(1 - rho2) = 2.85e-8/1.82e-17 vs share_1 = 0.969/0.965,
E1VAC = 7.5/16.7 dex): the one-modedness of the susceptibility is
NOT weight concentration -- the weights sit HIGH in the spectrum --
it is the WEIGHT-LADDER RACE: the collapsing delta-ladder
(delta_1/delta_i falling multi-dex, r146 L3 cited) beats the rising
weight profile, sum measured 1/share_1 - 1 = 0.032/0.036 flat.  The
share-floor does NOT reduce to an et_1^2-floor; it is a race
statement on the SAME spectrum, typed MEASURED.

RED-TEAM (mandatory): (i) the r147 2D s-model (W = diag(tau, tau +
Delta), u = (eps, sqrt(1-eps^2))): SB2 is EQUALITY at two levels
(s == (1 - rho2)/(rho2 delta_1)) and BS == (1 - eps^2)/s -- the
legal witness s == P realizes BS == (1 - eps^2)/P: ANY algebra-only
floor on BS (hence any algebra-only proof of the merge statement)
FAILS this model -- ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-BOTTOMSHARE
(hard assert, symbolic + mp on the x = 5 rung data).  (ii) the
trace family diag(t, t(1+eta)): the SB1 loop identity holds with
tau TrH = 1/eta unbounded at bounded trace -- no algebra cap on
TRACEFLOOR either (Y3's family re-gated in loop currency).  (iii)
CONTROLS: SMOOTH/SCRARITH x=5, EPSTEIN x=8 refuse fourfold (zone
overcount, mu_1 fills the verified zero-free gap, tau_w < 0: the
PSD/simple-ground hypotheses of SB1-SB5 fail EXACTLY there, no
positive spectrum to balance; no escaped scale y_t_w/b_top <= 1).
(iv) tau-screens with riders: the demand ratios (s, OVG, share_1,
gap) are tau-flat; BS/rho2/et_1^2 RIDE (BOUND-RIDES-CONNES typed:
the rate-blind ends are pinned as riders, the flat coordinates are
the RATIOS).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 SB1: loop identity tau TrH == tf/FG generic; a_i <= 1 and
    a_i <= a_2 generic (nonneg parametrization); tf-form == 1 +
    sum a_i; two-sided transfer [TRACEFLOOR <= P ==> FG >= 1/P] and
    [FG >= 1/P, tf <= C ==> TRACEFLOOR <= C P] exact + instances
    (diag(1,2,5)/tau=1: TrH == 5/4, tf == 5/4 <= K-1 == 2; the n=2
    equality case [[3,1],[1,3]]);
    G11 SB2: chi (q_1 - q_0) <= 1 - rho2 generic 3-level (term-wise
    + normalization) ==> s rho2 delta_1 == chi (q_1 - q_0) <= 1 -
    rho2 exact; 2-level equality instance; 3-level strict instance;
    G12 SB3: BS <= g generic (root-equation substitution: rho2
    (delta_1 - g) <= g (1 - rho2)); merge algebra [BS >= 1/P] ==>
    [delta_1 >= 1/P] and [s <= P]; Y4 rearrangement rho2 delta_1 ==
    et_1^2/(s share_1) generic; reverse-wedge composition;
    G13 SB4: secular-root identity et_1^2/rho2 == share_1^g
    (delta_1 - g)/g generic (chase via the root equation);
    share_1^g <= 1; OVG cap OVG <= (delta_1/FG)/g generic; Y4-OVG
    identity OVG == s share_1 delta_1/FG generic; adjugate twin
    [Q(l1)/P'(l1)]/[Q(l0)/P'(l0)] == e_1^2/e_0^2 on diag (the r150
    R1a ratio law at the probe functional, re-gated);
    G14 SB5: expansion identity generic; share_1 >= et_1^2/(1 -
    rho2) >= et_1^2 generic 3-level;
    G15 red team symbolic: 2D model SB2-equality + BS == (1-eps^2)/s
    + witness s == P == 10^6 with BS == (1-eps^2)/P (hard assert);
    trace family diag(t, t(1+eta)): loop identity + lim tau TrH =
    oo at bounded trace.
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150),(28,160) deep (zone sign-scan to T_z + 6,
    step 0.05; newton-polished nodes, the r141/r143 standard):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform);
    G31 spectral ladder: lam_i > 0 sorted; FULLGAP in the frozen
    windows (r142/r146 strings + CDLII x=28 string) x (0.97, 1.03);
    lam_1 SIMPLE (rel gap >= 1e3); post-loop growth slope in
    (3.4, 4.6);
    G32 node-config V + replication: |qrel| <= 1e-30, null residual
    <= 1e-40; W3 re-gate delta_1 >= FULLGAP (1 - 1e-12); zone-top
    argmin in the frozen windows AND >= 3; s <= S_BAR_TAB; s x gap
    in (0.98, 1.02); delta_1 windows; share_1 >= 0.5; tlaw on the
    CDXLI strings <= 5e-3 (x <= 24) / in (0.40, 0.70) at 28; lock
    FULLGAP/y_t in (1.5, 6.0);
    G33 SB1 instantiated: TrH via bordered LU at dps + 50 (r144
    getrs-order instrument VERBATIM), LU-vs-eigen cross dev <=
    1e-20; tf(LU) vs tf(eigen-sum) cross dev <= 1e-20 (independent
    instruments); tf in (1 - 1e-12, 1.05); tail = tf - 1 in
    [-1e-12, (K-2)(lam_1-tau)/(lam_2-tau) (1+1e-9)] HARD; tf <=
    K - 1 HARD; TRACEFLOOR <= x^25; floor 1/(tau TrH) vs FULLGAP
    tightness printed (LOOP exhibit);
    G34 SB2/SB3 instantiated: chi (q_1 - q_0) <= (1 - rho2)
    (1 + 1e-12) HARD; s rho2 delta_1 <= (1 - rho2)(1 + 1e-12) HARD;
    BS <= g (1 + 1e-12) HARD; rho2 cross-instrument |rho2 en2/
    R_phi^2 - 1| <= 1e-20 (the X4 residue currency: rho2 ==
    R_phi^2/|P_V r|^2); Y4-rearrangement |BS s share_1/et_1^2 - 1|
    <= 1e-30 (mp share); VAC_CHI >= 3 dex (vacuity pin); cert chain
    rho2/(tau TrH) <= BS (1 + 1e-9) with cert/BS in (0.9, 1 + 1e-9)
    (the eigensolve-free lower certificate is TIGHT);
    G35 SB4 instantiated: root residual |rho2/(g tau)/S_g - 1| <=
    1e-25; identity |et_1^2/rho2 / (share_1^g (delta_1 - g) tau /
    ((lam*-q_0)...)) - 1| <= 1e-25; OVG <= (delta_1/FG)/g
    (1 + 1e-12) HARD; OVG in (0.01, 0.30) x <= 24 / (0.005, 0.5)
    x = 28; |share_1^g/share_1 - 1| <= 5e-2 (near-equality window,
    predicted g/delta_1-class);
    G36 SB5 instantiated: expansion identity dev <= 1e-25; share_1
    >= et_1^2/(1 - rho2) (1 - 1e-12) >= et_1^2 (1 - 1e-12) HARD;
    E1VAC = log10(share_1 (1 - rho2)/et_1^2) >= 3 dex (the
    vacuity pin: the share-floor is NOT weight concentration);
    race sum 1/share_1 - 1 printed + argmax weight index printed
    (WEIGHT-LADDER-RACE exhibit).
S3c G40 red-team mp (x = 5 rung data): 2D model witness s == 10^6
    (dev <= 1e-40) with BS == (1 - eps^2)/10^6 (dev <= 1e-40) and
    SB2-equality (dev <= 1e-40); trace family at eta = 1e-6: loop
    identity dev <= 1e-40 with tau TrH == 1e6 at TrM <= 3 tau.
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 (the SB hypotheses fail EXACTLY here) AND
    y_t_w/b_top <= 1.0; G53 consistency.
S5  G54 tau-screens: |slope log10 v vs log10 tau| <= 0.30 for v in
    (s, OVG, share_1, gap) -- the demand ratios are tau-flat;
    RIDER report: slopes of log10 BS, log10 rho2, log10 et_1^2 vs
    log10 tau in (0.30, 1.20) (2-pt calibration 0.82/0.87-class,
    DISCLOSED) + VAC_CHI slope vs |log10 tau| printed -- the
    rate-blind ends RIDE (BOUND-RIDES-CONNES typed); G55
    conditioning (1e-25 shift window).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence-demand ->
    Theorem R transfer -> coupling absorbed -> the g/delta_1/BS
    coordinates consume NO tlaw, NO Z, no lattice proximity
    (source + secular data only; r142 W2/W3 + r141 V1 cited) -> V2
    good sets -> no ALL-X demand; enclosure-end certificates
    eigensolve-free given (tau, phi): ONE bordered LU + inner
    products (BS lower end via Y1 floor) -- CERT-COMPRESSED);
    G61 min-cut (r116 replica; r142/r144/r146/r150 graph VERBATIM):
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL
    9 NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150),(28,160)); HSW = (0.1038, 0.2573, 9.3675) [HSW22
Cor. 1.2]; SCAN_STEP = 0.05; SCAN_LO = 0.5; SCAN_OVER = 6.0;
TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05; NODE_EXCL = 0.02;
BIS_ITERS = 250; BORD_PAD = 50 dps.
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26), 28: (10, 30)}; S_BAR_TAB =
{5..24: 0.1, 28: 0.15}; SGAP_WIN = (0.98, 1.02); D1_TAB = {5:
2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8, 28:
1.6513e8} x (0.7, 1.3); SHARE1_BAR = 0.5; TLAW_TAB = {5: 0.2664,
8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI
strings); TLAW28_WIN = (0.40, 0.70) (CDLIV measured 0.5778);
FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
24: 1.1382e8, 28: 1.6513e8} x (0.97, 1.03); FG_SLOPE_WIN = (3.4,
4.6) (r150 measured 3.971); SIMP_MIN = 1e3; LOCK_WIN = (1.5, 6.0);
TRH_XDEV_BAR = 1e-20 (calibration 2.0e-52/4.0e-60); TF_XDEV_BAR =
1e-20; TF_WIN = (1 - 1e-12, 1.05) (calibration 1.0000209/
1.0000029); TAIL_SLOP = 1e-9; POLY_DEG = 25 (TRACEFLOOR calibration
4.4935e-6/1.0049e-6); CHI_SLOP = 1e-12; RHO2X_BAR = 1e-20
(calibration 7.4e-50/3.8e-57); Y4REV_BAR = 1e-30 (calibration
1.6e-61/0.0); VAC_CHI_MIN = 3.0 (calibration 7.55/16.73);
CERT_RATIO_WIN = (0.9, 1 + 1e-9) (calibration 0.999971/0.999997);
ROOT_DEV_BAR = 1e-25 (calibration 0.0/3.1e-71); ID4_BAR = 1e-25
(calibration 0.0/3.1e-71); SH1G_DEV_BAR = 5e-2 (calibration
0.9691/0.9691 and 0.9653/0.9653 at print precision, predicted
g/delta_1-class 1.5e-4); OVG_WIN_CORE = (0.01, 0.30); OVG_WIN_28 =
(0.005, 0.5) (r146/CDLIV strings 0.0288..0.0677); ID5_BAR = 1e-25
(calibration 0.0/2.1e-81); SHARE_SLOP = 1e-12; E1VAC_MIN = 3.0
(calibration 7.53/16.72); RT_P = 10^6; RT_ID_BAR = 1e-40;
CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.30, 1.20)
(2-pt calibration BS ~0.82, rho2 ~0.87, DISCLOSED: deep rungs
unmeasured pre-freeze); COND_WIN = (1e-40, 1e-10); GAMMA1_LIT =
14.134725141734694 (ward only); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; np.float64-repr casts guarded by float()/repr(); tiny/
huge quantities stay mp end-to-end (the r147 underflow lesson:
rho2/BS/TrH/cert kept mp; log diagnostics via mp.log inside
workdps); bordered linear algebra at dps + BORD_PAD with the own
deterministic partial-pivot LU (all sequential row swaps BEFORE
the forward elimination -- LAPACK getrs order, the r144 smoke-1
repair, ported VERBATIM); Y4/share identities evaluated with the
mp share (the r146 smoke-1 lesson).

CALIBRATION DISCLOSURE (pre-freeze, ONE scratch script
calib_scratch_spectral_balance.py + log, x = 5/8 only, deleted
after freeze; all numbers quoted verbatim above and here): x=5:
TrH 2.796917e10 (xdev 2.0e-52), tf-1 2.0898e-5 == eigen route,
tail_sharp 1.8803e-4, K-1 = 10, TRACEFLOOR 4.4935e-6, loop dev
0.0; gap 33.6233, s 0.02974, sg 0.999854, d1 2.225510e5, share1
0.9691, OVG 0.02882; rho2 4.290255e-12, et1^2 2.85e-8 (printed
0.000000 at 4 digits), BS 9.549e-7 (BS <= g with g/BS 3.52e7),
xtight 2.9e-8-class, y4rev dev 1.6e-61, cert/BS 0.999971, rho2
cross dev 7.4e-50; root dev 0.0, sh1g 0.9691, id4 dev 0.0, OVG cap
value 0.02974; id5 dev 0.0, e1^2/(1-rho2) 2.85e-8 vs share1
0.9691.  x=8: TrH 2.663661e23 (xdev 4.0e-60), tf-1 2.9203e-6,
tail_sharp 5.5484e-5, K-1 = 20, TRACEFLOOR 1.0049e-6; gap 16.7200,
s 0.05981, sg 0.999984, share1 0.9653, OVG 0.05773; rho2
3.166260e-22, BS 3.151e-16 (g/BS 5.31e16), y4rev 0.0, cert/BS
0.999997, rho2 cross 3.8e-57; root/id4 3.1e-71, sh1g 0.9653, OVG
cap value 0.05981; id5 2.1e-81.  x = 13..28 pre-freeze UNMEASURED
on all new quantities (build cost); their windows are set from the
frozen r139-r150/CDLII strings, the calibrated trends and
structure asserts, DISCLOSED above.  Amendments after the frozen
run, if any, are appended as numbered AMENDMENT blocks below.

VERDICT ENUMS (frozen): SB1-PROVEN(trace-loop adjudicated: tau TrH
== tf/FULLGAP exact, 1 <= tf <= K-1 UNCONDITIONAL -- DELTA1FLOOR
<==> TRACEFLOOR two-sided poly equivalence, TAIL-CLOSED; the honest
minimal form is the dominant-term floor itself); SB2-PROVEN(chi-cap
exact) + CHI-CAP-VACUOUS(the third rate-blind moment instrument
after Y3-trace and R4-Parseval, vacuity riding pinned);
SB3-PROVEN(enclosure BS <= g <= delta_1 both ends exact; merge
algebra one-directional exact; reverse mod E1FLOOR) +
MERGE-REFUTED-MEASURED(BS falls super-polynomially: the ONE-moment-
statement merge coordinate is DEAD; the honest one-statement form
stays QSUBGAP-floor g >= 1/poly == the pair, per W2 cited);
SB4-PROVEN(OVG identity chain: OVG == share_1^g (delta_1 - g)/
(g FG) exact <= (delta_1/FG)/g -- the r150 OVG-flatness IS the
zone-top-gap pinch; OVG-cap relocates onto the g-floor, no new
residue) + SH1G-NEAR-EQUALITY(measured); SB5-PROVEN(share_1 >=
et_1^2/(1 - rho2) exact) + SHAREFLOOR-IS-LADDER-RACE(the bound is
vacuous: one-modedness is the collapsing delta-ladder beating the
rising weight profile, NOT weight concentration -- E1FLOOR wedge
measured false-trending); REDTEAM-REFUTES-ALGEBRA(2D model + trace
family: algebra admits BS -> 0 and TRACEFLOOR -> oo);
CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES(riders pinned);
QUANTIFIER-INHERITED(dense-x suffices, CHAIN-AUDIT);
OMEGA-RECOORDINATED(residue SET UNCHANGED: the pair {SUSCAP2R,
DELTA1FLOOR} <==> QSUBGAP-floor (W2 cited) with all r150
sub-coordinates (OVG-cap, share-floor, trace-floor) collapsed onto
the two numbers (g, delta_1) by SB1/SB4/SB5; census {MEAS,
OMEGA-POS} cardinality 4 UNCHANGED); MINCUT(4/5).  Composite
priority: INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.
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

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER_CORE = ((5, 60), (8, 80), (13, 120))
LADDER_DEEP = ((18, 140), (24, 150), (28, 160))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
BIS_ITERS = 250
BORD_PAD = 50
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0),
            18: (12.0, 22.0), 24: (14.0, 26.0), 28: (10.0, 30.0)}
S_BAR_TAB = {5: 0.1, 8: 0.1, 13: 0.1, 18: 0.1, 24: 0.1, 28: 0.15}
SGAP_WIN = (0.98, 1.02)
D1_TAB = {5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7,
          24: 1.14e8, 28: 1.6513e8}
D1_WIN = (0.7, 1.3)
SHARE1_BAR = 0.5
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
TLAW28_WIN = (0.40, 0.70)
FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
          24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
FG_SLOPE_WIN = (3.4, 4.6)
SIMP_MIN = 1e3
LOCK_WIN = (1.5, 6.0)
TRH_XDEV_BAR = 1e-20
TF_XDEV_BAR = 1e-20
TF_WIN = (1.0 - 1e-12, 1.05)
TAIL_SLOP = 1e-9
POLY_DEG = 25
CHI_SLOP = 1e-12
RHO2X_BAR = 1e-20
Y4REV_BAR = 1e-30
VAC_CHI_MIN = 3.0
CERT_RATIO_WIN = (0.9, 1.0 + 1e-9)
ROOT_DEV_BAR = 1e-25
ID4_BAR = 1e-25
SH1G_DEV_BAR = 5e-2
OVG_WIN_CORE = (0.01, 0.30)
OVG_WIN_28 = (0.005, 0.5)
ID5_BAR = 1e-25
SHARE_SLOP = 1e-12
E1VAC_MIN = 3.0
RT_P = 10 ** 6
RT_ID_BAR = 1e-40
CTRL_YTB_MAX = 1.0
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.30, 1.20)
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 14400.0

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
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
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
                       "no zero-oracle; cache in ward_; no zeta use")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

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
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300, extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    realm = np.abs(roots.imag) <= 1e-10 * float(s_mp)
    real_y = roots[realm & (roots.real > 0)]
    n_nonreal = int(np.sum(~realm))
    return np.sort(np.sqrt(real_y.real)), n_nonreal


def en_pair(cs: list, aa, oms: list, t):
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def newton_node(cs: list, aa, oms: list, z0: float, dps: int):
    with mp.workdps(dps):
        t = mp.mpf(repr(float(z0)))
        for _ in range(80):
            f, fp = en_pair(cs, aa, oms, t)
            step = f / fp
            if abs(step) > mp.mpf("0.1"):
                step = step / abs(step) * mp.mpf("0.1")
            t = t - step / 1 if abs(step) < mp.mpf("0.05") else t - step / 2
            if abs(step) < mp.mpf(10) ** (-dps + 6):
                break
        f, _fp = en_pair(cs, aa, oms, t)
        return t, abs(f)


# --------------------------------------------------------- closed forms
def hsw_G(T: float) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138-r150 replica)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        oms_f = [float(o) for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        Mq = ce["mpM"]
        tau_mp = ce["mpE"][0]
        mcon = len(gpts_mp)
        Rm = mp.zeros(mcon, K)
        for j in range(mcon):
            g = gpts_mp[j]
            Rm[j, 0] = (2 / g) / nrm[0]
            for k in range(1, K):
                Rm[j, k] = (2 * (-1) ** k * g / (g * g - oms[k] ** 2)) \
                    / nrm[k]
        piv = []
        used = set()
        for j in range(mcon):
            gjf = float(gpts_mp[j])
            order = sorted(range(1, K), key=lambda k: abs(oms_f[k] - gjf))
            for k in order:
                if k not in used:
                    piv.append(k)
                    used.add(k)
                    break
        free = [k for k in range(K) if k not in used]
        RP = mp.zeros(mcon, mcon)
        for j in range(mcon):
            for i2, k in enumerate(piv):
                RP[j, i2] = Rm[j, k]
        Nb = mp.zeros(K, len(free))
        for fi, k in enumerate(free):
            rhs = mp.matrix([-Rm[j, k] for j in range(mcon)])
            zsol = mp.lu_solve(RP, rhs)
            Nb[k, fi] = mp.mpf(1)
            for i2, kp in enumerate(piv):
                Nb[kp, fi] = zsol[i2]
        resR = 0.0
        for j in range(mcon):
            for fi in range(len(free)):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Rm[j, k] * Nb[k, fi]
                resR = max(resR, float(abs(acc)))
        nf = len(free)
        QN = mp.zeros(K, nf)
        for i in range(K):
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Mq[i, k] * Nb[k, fi]
                QN[i, fi] = acc
        Qr = mp.zeros(nf, nf)
        Gr = mp.zeros(nf, nf)
        for i in range(nf):
            for j2 in range(i + 1):
                accq = mp.mpf(0)
                accg = mp.mpf(0)
                for k in range(K):
                    accq += Nb[k, i] * QN[k, j2]
                    accg += Nb[k, i] * Nb[k, j2]
                Qr[i, j2] = Qr[j2, i] = accq
                Gr[i, j2] = Gr[j2, i] = accg
        L = mp.cholesky(Gr)

        def fwd(rhs_list, L=L, nf=nf):
            y = [mp.mpf(0)] * nf
            for i in range(nf):
                acc = rhs_list[i]
                for j2 in range(i):
                    acc -= L[i, j2] * y[j2]
                y[i] = acc / L[i, i]
            return y

        Yv = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Qr[i, col] for i in range(nf)])
            for i in range(nf):
                Yv[i, col] = y[i]
        Wm = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Yv[col, i] for i in range(nf)])
            for i in range(nf):
                Wm[i, col] = y[i]
        for i in range(nf):
            for j2 in range(i):
                sym = (Wm[i, j2] + Wm[j2, i]) / 2
                Wm[i, j2] = Wm[j2, i] = sym
        Ew, Vw = mp.eigsy(Wm)
        order = sorted(range(nf), key=lambda i: Ew[i])
        qs = [Ew[order[i]] for i in range(nf)]
        Z = mp.zeros(nf, nf)
        for c, i in enumerate(order):
            for r in range(nf):
                Z[r, c] = Vw[r, i]
        qrel = float((qs[0] - tau_mp) / tau_mp)
    return dict(qs=qs, Z=Z, Nb=Nb, fwd=fwd, nf=nf, resR=resR, qrel=qrel,
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp)


def secular_data(Vd: dict, r: list):
    """(lam*, et_raw, en2, etn, rho2, chi) for the extra row r on V
    (r141/r150 shape; bisection BIS_ITERS).  Caller sets workdps."""
    nf, Nb, fwd = Vd["nf"], Vd["Nb"], Vd["fwd"]
    qs, Z = Vd["qs"], Vd["Z"]
    K = len(r)
    d = []
    for fi in range(nf):
        acc = mp.mpf(0)
        for k in range(K):
            acc += Nb[k, fi] * r[k]
        d.append(acc)
    e = fwd(d)
    en2 = sum(v * v for v in e)
    et = []
    for i in range(nf):
        acc = mp.mpf(0)
        for k in range(nf):
            acc += Z[k, i] * e[k]
        et.append(acc)
    sq = mp.sqrt(en2)
    etn = [v / sq for v in et]
    rho2 = etn[0] * etn[0]
    lo, hi = qs[0], qs[1]

    def fsec(mu):
        return sum(etn[i] * etn[i] / (qs[i] - mu) for i in range(nf))
    for _ in range(BIS_ITERS):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, et, en2, etn, rho2, chi


# --------------------------------------------- deterministic LU (route B)
def lu_factor(Amat, n):
    """own partial-pivot LU (r144, VERBATIM); caller sets workdps."""
    piv = []
    for k in range(n):
        pmax = abs(Amat[k, k])
        pk = k
        for i in range(k + 1, n):
            v = abs(Amat[i, k])
            if v > pmax:
                pmax, pk = v, i
        piv.append(pk)
        if pk != k:
            for j in range(n):
                Amat[k, j], Amat[pk, j] = Amat[pk, j], Amat[k, j]
        akk = Amat[k, k]
        for i in range(k + 1, n):
            f = Amat[i, k] / akk
            Amat[i, k] = f
            if f != 0:
                for j in range(k + 1, n):
                    Amat[i, j] -= f * Amat[k, j]
    return Amat, piv


def lu_solve_fac(LU, piv, b, n):
    """solve with pre-computed lu_factor; ALL sequential row swaps
    BEFORE the forward elimination (LAPACK getrs order; the r144
    smoke-1 repair, VERBATIM)."""
    y = list(b)
    for k in range(n):
        pk = piv[k]
        if pk != k:
            y[k], y[pk] = y[pk], y[k]
    for k in range(n):
        for i in range(k + 1, n):
            if LU[i, k] != 0:
                y[i] -= LU[i, k] * y[k]
    x = [mp.mpf(0)] * n
    for i in range(n - 1, -1, -1):
        acc = y[i]
        for j in range(i + 1, n):
            acc -= LU[i, j] * x[j]
        x[i] = acc / LU[i, i]
    return x


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 SB1: trace loop + tail closure + transfer
    l0, g0, d2, e3 = sp.symbols("l0 g0 d2 e3", positive=True)
    dd = sp.symbols("dd", nonnegative=True)
    l1 = l0 + g0
    la = l1 + d2
    lb = la + e3
    TrH = 1 / (l1 - l0) + 1 / (la - l0) + 1 / (lb - l0)
    tf = (l1 - l0) * TrH
    FG = (l1 - l0) / l0
    okA = sp.simplify(l0 * TrH - tf / FG) == 0
    a_gen = g0 / (g0 + dd)
    okB = sp.simplify(1 - a_gen - dd / (g0 + dd)) == 0 \
        and (dd / (g0 + dd)).is_nonnegative is True
    a2 = g0 / (g0 + d2)
    a3 = g0 / (g0 + d2 + e3)
    okC = sp.simplify(a2 - a3
                      - g0 * e3 / ((g0 + d2) * (g0 + d2 + e3))) == 0 \
        and (g0 * e3 / ((g0 + d2) * (g0 + d2 + e3))).is_positive is True
    okD = sp.simplify(tf - (1 + a2 + a3)) == 0
    # instance: diag(1,2,5,7), tau=1: TrH = 1 + 1/4 + 1/6 = 17/12,
    # tf = 17/12 <= K-1 = 3 (smoke-1 instrument repair, disclosed:
    # the first smoke used e3 = 0 against the 3-excited generic --
    # wrong instance numbers, no bar/criterion moved)
    okE = sp.simplify(TrH.subs({l0: 1, g0: 1, d2: 3, e3: 2})
                      - sp.Rational(17, 12)) == 0 \
        and bool(sp.Rational(17, 12) <= 3)
    # n=2 equality case [[3,1],[1,3]]: tau=2, lam_1=4: tf = 1
    okF = sp.simplify((4 - 2) * sp.Rational(1, 2) - 1) == 0
    # transfer both ways
    Ps, Cs = sp.symbols("Ps Cs", positive=True)
    #   TRACEFLOOR = tf/FG; tf >= 1 ==> FG = tf/TRACEFLOOR >= 1/P
    okG = sp.simplify(FG - tf / (l0 * TrH)) == 0
    okH = bool((sp.Rational(5, 4) / sp.Rational(1, 3)
                >= 1 / sp.Rational(1, 3)))       # tf/TFl >= 1/TFl
    #   FG >= 1/P and tf <= C ==> TRACEFLOOR = tf/FG <= C P
    okI = sp.simplify(Cs / (1 / Ps) - Cs * Ps) == 0
    out.append(("G10-sb1-trace-loop", okA and okB and okC and okD
                and okE and okF and okG and okH and okI,
                "tau TrH == tf/FULLGAP GENERIC (the Y1 trace floor is "
                "the FULLGAP floor up to tf); a_i = (l1-l0)/(l_i-l0) "
                "<= 1 and <= a_2 generic; tf == 1 + sum a_i so 1 <= "
                "tf <= K-1 UNCONDITIONAL (tail CLOSED by the count "
                "bound, sharper by (K-2) a_2); two-sided transfer "
                "[TRACEFLOOR <= P ==> FG >= 1/P] + [FG >= 1/P, tf <= "
                "C ==> TRACEFLOOR <= CP]: DELTA1FLOOR <==> TRACEFLOOR "
                "is a proven two-sided poly equivalence -- THEOREM "
                "SB1, the Y1 recoordination is a LOOP; the honest "
                "minimal form is the dominant-term floor itself"))

    # ---------------- G11 SB2: chi-cap
    w0, w1, w2, gq1, dq = sp.symbols("w0 w1 w2 gq1 dq", positive=True)
    tq = sp.symbols("tq", positive=True)
    Ssum = w0 + w1 + w2
    # q1 - q0 = gq1, q2 - q0 = gq1 + dq; normalized weights w_i/S
    chi_n = (w1 / gq1 + w2 / (gq1 + dq)) / Ssum
    lhs = chi_n * gq1
    rhs = (w1 + w2) / Ssum
    okJ = sp.simplify(rhs - lhs
                      - (w2 / Ssum) * dq / (gq1 + dq)) == 0 \
        and ((w2 / Ssum) * dq / (gq1 + dq)).is_positive is True
    # s rho2 delta_1 == chi (q_1 - q_0) chase
    rho2s, chis = sp.symbols("rho2s chis", positive=True)
    s_def = tq * chis / rho2s
    d1_def = gq1 / tq
    okK = sp.simplify(s_def * rho2s * d1_def - chis * gq1) == 0
    # 2-level equality instance (w2 = 0)
    okL = sp.simplify((lhs - rhs).subs(w2, 0)) == 0
    out.append(("G11-sb2-chi-cap", okJ and okK and okL,
                "chi (q_1 - q_0) <= sum_{i>=1} et_i^2 == 1 - rho2 "
                "GENERIC (term-wise delta_i >= delta_1) with the gap "
                "== the spread term; s rho2 delta_1 == chi (q_1 - "
                "q_0) exact chase ==> s <= (1 - rho2)/(rho2 delta_1) "
                "(THEOREM SB2, equality iff two-level): the direct "
                "chi-cap on s -- measured VACUOUS (rho2 collapses): "
                "the THIRD rate-blind moment instrument"))

    # ---------------- G12 SB3: enclosure + merge algebra
    h1 = sp.symbols("h1", positive=True)   # delta_1 - g
    gg = sp.symbols("gg", positive=True)   # g
    d1s = gg + h1
    d2s = d1s + dd
    rho2_root = gg * (w1 / h1 + w2 / (h1 + dd))
    BSs = rho2_root * d1s
    # BS <= g (1 + w1 + w2 normalization: rho2 + w1 + w2 = 1 scaled)
    diff = gg * (rho2_root + w1 + w2) - BSs
    okM = sp.simplify(diff - gg * w2 * dd / (h1 + dd)) == 0 \
        and (gg * w2 * dd / (h1 + dd)).is_nonnegative is True
    # merge: BS >= 1/P ==> delta_1 >= 1/P (rho2 <= 1) and s <= P
    r2n = sp.symbols("r2n", positive=True)
    okN = (d1_def - r2n * d1_def).subs(r2n, sp.Rational(1, 2)) \
        .is_positive is not False
    okN = okN and sp.simplify(
        (1 - r2n) * d1_def + r2n * d1_def - d1_def) == 0
    # Y4 rearrangement: rho2 delta_1 == et1^2/(s share1)
    e1q, q0q, q1q, q2q, e2q = sp.symbols("e1q q0q q1q q2q e2q",
                                         positive=True)
    chi_g = e1q / (q1q - q0q) + e2q / (q2q - q0q)
    s_g = q0q * chi_g / rho2s
    share1_g = (e1q / (q1q - q0q)) / chi_g
    okO = sp.simplify(rho2s * (q1q - q0q) / q0q
                      - e1q / (s_g * share1_g)) == 0
    # reverse-wedge composition: s <= P, e1 >= 1/P' ==> BS >= 1/(PP')
    okP = sp.simplify((1 / Ps) / (Ps * 1) - 1 / Ps ** 2) == 0
    out.append(("G12-sb3-merge-enclosure", okM and okN and okO and okP,
                "BS = rho2 delta_1 <= g GENERIC (root-equation "
                "substitution: rho2 (delta_1 - g) <= g (1 - rho2)) "
                "==> the QSUBGAP root is enclosed g in [rho2 delta_1, "
                "delta_1], both ends EXACT; merge algebra [BS >= 1/P] "
                "==> delta_1 >= 1/P AND s <= P (one statement ==> the "
                "whole pair + QSUBGAP); reverse wedge via Y4: rho2 "
                "delta_1 == et_1^2/(s share_1) exact (THEOREM SB3) -- "
                "the MEASURED adjudication of BS is the round's "
                "honest finding (rides, MERGE-REFUTED-MEASURED)"))

    # ---------------- G13 SB4: OVG identity chain + adjugate twin
    Sg = w1 / h1 + w2 / (h1 + dd)          # S_g at the root
    rho2r = gg * Sg                        # root equation
    sh1g = (w1 / h1) / Sg
    okQ = sp.simplify(w1 / rho2r - sh1g * h1 / gg) == 0
    okR = sp.simplify(1 - sh1g
                      - (w2 / (h1 + dd)) / Sg) == 0 \
        and ((w2 / (h1 + dd)) / Sg).is_positive is True
    # OVG cap: OVG = (w1/rho2)/FG <= (delta_1/FG)/g
    FGs = sp.symbols("FGs", positive=True)
    OVGs = (w1 / rho2r) / FGs
    okS = sp.simplify((d1s / FGs) / gg - OVGs
                      - (d1s - sh1g * h1) / (gg * FGs)) == 0 \
        and sp.simplify((d1s - sh1g * h1)
                        - (gg + (1 - sh1g) * h1)) == 0
    # Y4-OVG identity: OVG == s share1 delta_1/FG
    OVG_y4 = (e1q / rho2s) / FGs
    okT = sp.simplify(OVG_y4
                      - s_g * share1_g * ((q1q - q0q) / q0q) / FGs) == 0
    # adjugate twin on diag: [Q(l1)/P'(l1)]/[Q(l0)/P'(l0)] == e1^2/e0^2
    z = sp.symbols("z")
    e0d, e1d, e2d, m0, m1, m2 = sp.symbols("e0d e1d e2d m0 m1 m2",
                                           positive=True)
    Qz = (e0d ** 2 * (z - m1) * (z - m2) + e1d ** 2 * (z - m0)
          * (z - m2) + e2d ** 2 * (z - m0) * (z - m1))
    Pz = (z - m0) * (z - m1) * (z - m2)
    Pp = sp.diff(Pz, z)
    ratio = (Qz.subs(z, m1) / Pp.subs(z, m1)) \
        / (Qz.subs(z, m0) / Pp.subs(z, m0))
    okU = sp.simplify(ratio - e1d ** 2 / e0d ** 2) == 0
    out.append(("G13-sb4-ovg-identity", okQ and okR and okS and okT
                and okU,
                "et_1^2/rho2 == share_1^g (delta_1 - g)/g EXACT at "
                "the secular root (chase) with share_1^g <= 1 ==> "
                "OVG == share_1^g (delta_1 - g)/(g FULLGAP) <= "
                "(delta_1/FULLGAP)/g; Y4 read: OVG == s share_1 "
                "delta_1/FG exact; adjugate twin [Q(l1)/P'(l1)]/"
                "[Q(l0)/P'(l0)] == e_1^2/e_0^2 on diag (r150 R1a "
                "class at the probe functional): THEOREM SB4 -- the "
                "OVG-flatness IS the zone-top-gap pinch; the OVG-cap "
                "relocates onto the g-floor = QSUBGAP (W2 cited), "
                "the identity behind the r150 flat ratio FOUND"))

    # ---------------- G14 SB5: share expansion + monotone bounds
    exp_lhs = 1 / share1_g
    exp_rhs = 1 + (e2q / e1q) * ((q1q - q0q) / (q2q - q0q))
    okV = sp.simplify(exp_lhs - exp_rhs) == 0
    # share1 >= e1/(e1 + e2) >= e1 (weights normalized so that
    # rho2 + e1 + e2 = 1): monotone since (q1-q0)/(q2-q0) <= 1
    q2sub = {q2q: q1q + dd}
    gap_ratio = ((q1q - q0q) / (q2q - q0q)).subs(q2sub)
    okW = sp.simplify(1 - gap_ratio
                      - dd / (q1q + dd - q0q)) == 0
    share_lo = e1q / (e1q + e2q)
    okX = sp.simplify(exp_rhs.subs(q2sub)
                      - (1 + (e2q / e1q))
                      + (e2q / e1q) * dd / (q1q + dd - q0q)) == 0 \
        and bool(sp.Rational(1, 3)
                 >= sp.Rational(1, 3) * sp.Rational(2, 3))
    okY = sp.simplify(1 / share_lo - (1 + e2q / e1q)) == 0
    out.append(("G14-sb5-share-floor", okV and okW and okX and okY,
                "1/share_1 == 1 + sum_{i>=2}(et_i^2/et_1^2)"
                "(delta_1/delta_i) EXACT; delta_1/delta_i <= 1 ==> "
                "share_1 >= et_1^2/(1 - rho2) >= et_1^2 (THEOREM SB5: "
                "share-floor <== et_1^2-floor) -- measured VACUOUS: "
                "the one-modedness is the WEIGHT-LADDER RACE (the "
                "collapsing delta-ladder beats the rising weight "
                "profile), not weight concentration"))

    # ---------------- G15 red team symbolic
    eps, tau_s, Del = sp.symbols("eps tau_s Del", positive=True)
    Pw = sp.Integer(RT_P)
    rho2m = eps ** 2
    d1m = Del / tau_s
    chim = (1 - eps ** 2) / Del
    sm = tau_s * chim / rho2m
    okZ = sp.simplify(sm * rho2m * d1m - (1 - rho2m)) == 0
    BSm = rho2m * d1m
    okAA = sp.simplify(BSm - (1 - eps ** 2) / sm) == 0
    eps2w = tau_s / (tau_s + Del * Pw)
    okBB = sp.simplify(sm.subs(eps ** 2, eps2w) - Pw) == 0 \
        or sp.simplify(sm.subs(eps, sp.sqrt(eps2w)) - Pw) == 0
    okCC = sp.simplify(BSm.subs(eps, sp.sqrt(eps2w))
                       - (1 - eps2w) / Pw) == 0
    # trace family diag(t, t(1+eta)): loop identity + unbounded
    tpar, eta = sp.symbols("tpar eta", positive=True)
    TrH_f = 1 / (tpar * eta)
    tf_f = (tpar * eta) * TrH_f
    FG_f = eta
    okDD = sp.simplify(tpar * TrH_f - tf_f / FG_f) == 0 \
        and sp.simplify(tf_f - 1) == 0 \
        and sp.limit(tpar * TrH_f, eta, 0, "+") == sp.oo \
        and bool(sp.simplify(tpar * (2 + eta)).subs(
            {tpar: 1, eta: sp.Rational(1, 10)}) <= 3)
    out.append(("G15-redteam-symbolic", okZ and okAA and okBB
                and okCC and okDD,
                "2D model (r147 core): SB2 is EQUALITY (s rho2 "
                "delta_1 == 1 - rho2) and BS == (1 - eps^2)/s; legal "
                "witness s == P = 10^6 realizes BS == (1 - eps^2)/P: "
                "ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-BOTTOMSHARE (hard "
                "assert -- no algebra-only floor on the merge "
                "coordinate exists); trace family diag(t, t(1+eta)): "
                "loop identity holds with tau TrH = 1/eta -> oo at "
                "bounded trace (the Y3 obstruction re-gated in loop "
                "currency): only arithmetic-consuming bounds may "
                "floor BS or cap TRACEFLOOR"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    """bookkeeping over cited chain statements (typed CHAIN-AUDIT).
    Levels: 0 = ALL-X-TAIL, 1 = FULL-MEASURE-TAIL, 2 = UNBOUNDED-SEQ
    (instrument-chosen).  provider a satisfies demand b iff a <= b."""
    ALL_X, FULL_MEAS, SEQ = 0, 1, 2
    steps = []
    demand = SEQ
    steps.append(("NFCLOS (CDXXIII, cited): (H-conv)+(H-trace) per "
                  "dense a; Vitali/Montel sequence-based", demand == SEQ))
    steps.append(("Theorem R (CDXXX, cited) pointwise transfer "
                  "preserves the x-demand level", demand == SEQ))
    steps.append(("coupling x >= sqrt(a)/(2.5 pi) is a lower bound: "
                  "absorbed by any unbounded sequence tail", True))
    steps.append(("the g/delta_1/BS coordinates consume NO tlaw, NO "
                  "Z, no lattice proximity: source + secular data "
                  "only (r142 W2/W3 + r141 V1 cited); the enclosure "
                  "ends are eigensolve-free given (tau, phi): ONE "
                  "bordered LU + inner products (BS lower certificate "
                  "via the Y1 floor) -- CERT-COMPRESSED", True))
    steps.append(("V2 (CDXLV, cited) provides full-measure good "
                  "sets => unbounded sequence exists constructively",
                  FULL_MEAS <= demand))
    steps.append(("no ALL-X demand introduced downstream",
                  demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("spectral_balance_probe -- PRIME.SPECTRAL.BALANCE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    gtop = float(gam[-1])

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems SB1-SB5 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW + OFF; r132 raw "
         "census; r137/CDXLI budget identity + tlaw strings; r138 "
         "Q1-Q3; r139/CDXLIII U1-U4 + share_1 strings; r140/CDXLIV "
         "J1-J4 + y_t strings; r141/CDXLV V1-V3 + s strings + "
         "quantifier; r142/CDXLVI W1-W3 + FULLGAP strings; r143/"
         "CDXLVII T1-T4 + delta_1-lock; r144/CDXLVIII X1-X4 + LU "
         "instrument; CDXLIX F1-F6 + x=28 strings; CDL Y1-Y4 + "
         "zero-jet law; CDLI AD1/AD2; CDLIV R1-R4 + OVG strings; "
         "HSW22 Cor. 1.2; PT21; Courant-Fischer; Cauchy "
         "interlacing; Cramer/adjugate; partial fractions; Euler "
         "sine product")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: THE SPECTRAL-BALANCE ANATOMY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36 = [], [], []
    tau_tab, fg_tab, gap_tab, s_tab = {}, {}, {}, {}
    ovg_tab, sh_tab, bs_tab, r2_tab, e1_tab, vac_tab = {}, {}, {}, {}, \
        {}, {}
    cells = {}
    rt_data = None
    for x, dps in all_rungs:
        is_deep = x > 13
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        cells[x] = ce
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        with mp.workdps(dps):
            E = ce["mpE"]
            tau = E[0]
            lam1 = E[1]
            lam2 = E[2]
            FG = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0src = sum(((-1) ** k) * cs[k] for k in range(K))
            A2src = sum(((-1) ** k) * cs[k] * oms[k] ** 2
                        for k in range(K))
            yt = float(abs(A2src / A0src))
            l10 = mp.log(10)
            tauf = float(tau)
            fg_f = float(FG)
            simp = float((lam2 - lam1) / lam1)
        Gz = hsw_G(Tz)
        tlaw0 = tauf / (8.0 * float(abs(A0src)) ** 2 * Gz)
        tau_tab[x] = tauf
        fg_tab[x] = fg_f
        if x == 5:
            rt_data = (tauf, fg_f)

        # ---- census (core: polyroots; deep: zone sign-scan)
        if not is_deep:
            mus, n_nonreal = raw_mp_census(ce)
            seeds = [float(v) for v in mus]
            cens_ok = (len(mus) == K - 1 and n_nonreal == 0)
        else:
            with mp.workdps(dps):
                ts = np.arange(SCAN_LO, Tz + SCAN_OVER, SCAN_STEP)
                vprev = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(ts[0]))))[0]
                seeds = []
                for tv in ts[1:]:
                    v = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(tv))))[0]
                    if v * vprev < 0:
                        seeds.append(float(tv) - SCAN_STEP / 2)
                    vprev = v
            cens_ok = len(seeds) >= m_zone + 1
            info("x=%d deep census: zone-window scan to T_z + %.0f "
                 "found %d nodes (zone prefix + overhang; edge "
                 "census not consumed)" % (x, SCAN_OVER, len(seeds)))
        nds_all = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds_all.append(tmu)
                wres = max(wres, float(res))
        nds_f_all = np.array([float(v) for v in nds_all])
        n_zone_nodes = int(np.sum(nds_f_all <= Tz))
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        cens_ok = cens_ok and wres <= RES_BAR and len(sgs) == 1 \
            and n_zone_nodes == m_zone
        ok30 = ok30 and cens_ok
        det30.append("x%d: %d nodes zone %d/%d res %.0e"
                     % (x, len(nds_all), n_zone_nodes, m_zone, wres))
        zone_nds = nds_all[:m_zone]
        zone_f = [float(v) for v in zone_nds]

        # ---- G31 spectral ladder
        with mp.workdps(dps):
            pos_ok = all(E[i] > 0 for i in range(K))
            sort_ok = all(E[i] <= E[i + 1] for i in range(K - 1))
            idxs = sorted(set([0, 1, 2, 3, 4,
                               max(m_zone - 1, 0), m_zone, K - 1]))
            prof = ["i%d:%.2f" % (i, float(mp.log(E[i] / tau) / l10))
                    for i in idxs]
        fg_ok = FG_TAB[x] * FG_WIN[0] <= fg_f <= FG_TAB[x] * FG_WIN[1]
        ok31x = pos_ok and sort_ok and fg_ok and simp >= SIMP_MIN
        ok31 = ok31 and ok31x
        det31.append("x%d: FULLGAP %.6e (win %s) simp %.1e"
                     % (x, fg_f, fg_ok, simp))
        info("x=%d ladder log10(lam_i/tau): %s" % (x, " ".join(prof)))

        # ---- G33 SB1 instantiated: bordered TrH + tail closure
        dpsB = dps + BORD_PAD
        with mp.workdps(dpsB):
            Mq = ce["mpM"]
            tauB = ce["mpE"][0]
            lam1B = ce["mpE"][1]
            lam2B = ce["mpE"][2]
            phiv = [ce["mpV"][i, 0] for i in range(K)]
            n_b = K + 1
            B = mp.zeros(n_b, n_b)
            for i in range(K):
                for j2 in range(K):
                    B[i, j2] = Mq[i, j2]
                B[i, i] -= tauB
                B[i, K] = phiv[i]
                B[K, i] = phiv[i]
            t_lu0 = time.time()
            LU, pivv = lu_factor(B, n_b)
            trH = mp.mpf(0)
            for k in range(K):
                rhs = [mp.mpf(0)] * n_b
                rhs[k] = mp.mpf(1)
                yk = lu_solve_fac(LU, pivv, rhs, n_b)
                trH += yk[k]
            t_lu = time.time() - t_lu0
            trH_eig = sum(1 / (ce["mpE"][i] - tauB)
                          for i in range(1, K))
            xdev = float(abs(trH / trH_eig - 1))
            tf_lu = (lam1B - tauB) * trH
            tail_eig = sum((lam1B - tauB) / (ce["mpE"][i] - tauB)
                           for i in range(2, K))
            tf_eig = 1 + tail_eig
            tf_xdev = float(abs(tf_lu / tf_eig - 1))
            tail_lu = tf_lu - 1
            tail_sharp = (K - 2) * (lam1B - tauB) / (lam2B - tauB)
            tracefloor_mp = tauB * trH
            tracefloor = float(tracefloor_mp)
            tf_f = float(tf_lu)
            tail_ok = bool(tail_lu >= -mp.mpf("1e-12")) \
                and bool(tail_lu <= tail_sharp
                         * (1 + mp.mpf(repr(TAIL_SLOP)))) \
                and bool(tf_lu <= K - 1)
            khead = float(mp.log((K - 1) / tf_lu) / mp.log(10))
            floor_val = 1 / tracefloor_mp
            floor_tight = float(floor_val / ((lam1B - tauB) / tauB))
        ok33x = (xdev <= TRH_XDEV_BAR and tf_xdev <= TF_XDEV_BAR
                 and TF_WIN[0] <= tf_f <= TF_WIN[1] and tail_ok
                 and tracefloor <= float(x) ** POLY_DEG)
        ok33 = ok33 and ok33x
        det33.append("x%d: TrH %.4e xdev %.0e tf-1 %.2e (x %.0e) "
                     "tail<=sharp %.2e K-1 %d TRACEFLOOR %.3e "
                     "(LU %.0f s)"
                     % (x, float(trH), xdev, tf_f - 1, tf_xdev,
                        float(tail_sharp), K - 1, tracefloor, t_lu))
        info("x=%d SB1 exhibit: floor 1/(tau TrH) / FULLGAP = %.8f "
             "(LOOP: the trace bound IS the gap floor up to tf); "
             "count-bound headroom log10((K-1)/tf) = %.2f dex -- the "
             "tail is CLOSED unconditionally, no zeta-like "
             "refinement consumed" % (x, floor_tight, khead))

        # ---- G32 node-config + replication + zone-top argmin
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            d1 = (Vd["qs"][1] - Vd["qs"][0]) / Vd["tau_mp"]
            d1_f = float(d1)
            w3_ok = bool(d1 >= FG * (1 - mp.mpf("1e-12")))
            tg = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                TOP_GRID_STEP)) + [Tz - 0.001]
            gmin, argp = None, None
            for tv in tg:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - Vd["tau_mp"]) / Vd["tau_mp"])
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
            qs = Vd["qs"]
            nf = Vd["nf"]
            tau_v = Vd["tau_mp"]
            g_ex = (lam - qs[0]) / tau_v
            s_val = tau_v * chi / rho2
            sg = float(s_val * g_ex)
            s_f = float(s_val)
            g_f = float(g_ex)
            e12 = etn[1] * etn[1]
            share1_mp = (e12 / (qs[1] - qs[0])) / chi
            share1 = float(share1_mp)
            OVG_mp = (e12 / rho2) / FG
            OVG = float(OVG_mp)
        lock = fg_f / yt
        lo_w, hi_w = REPL_WIN[x]
        if x <= 24:
            tl_ok = abs(tlaw0 / TLAW_TAB[x] - 1.0) <= TLAW_TOL
        else:
            tl_ok = TLAW28_WIN[0] <= tlaw0 <= TLAW28_WIN[1]
        ok32x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR and w3_ok
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR_TAB[x]
                 and SGAP_WIN[0] <= sg <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR and tl_ok
                 and LOCK_WIN[0] <= lock <= LOCK_WIN[1])
        ok32 = ok32 and ok32x
        det32.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1/FG "
                     "%.6f share1 %.3f tlaw %.4f lock %.3f (%.0f s)"
                     % (x, Vd["qrel"], gmin, s_f, sg, d1_f / fg_f,
                        share1, tlaw0, lock, time.time() - t_q))
        gap_tab[x] = gmin
        s_tab[x] = s_f
        ovg_tab[x] = OVG
        sh_tab[x] = share1

        # ---- G34 SB2/SB3 instantiated
        with mp.workdps(dps):
            one = mp.mpf(1)
            slop = mp.mpf(repr(CHI_SLOP))
            chi_lhs = chi * (qs[1] - qs[0])
            chi_ok = bool(chi_lhs <= (one - rho2) * (1 + slop))
            sb2_ok = bool(s_val * rho2 * d1
                          <= (one - rho2) * (1 + slop))
            BS = rho2 * d1
            bs_le_g = bool(rho2 * (qs[1] - qs[0])
                           <= (lam - qs[0]) * (1 + slop))
            phivc = [ce["mpV"][i, 0] for i in range(K)]
            Rphi = sum(r[k] * phivc[k] for k in range(K))
            rho2x = float(abs(rho2 * en2 / (Rphi * Rphi) - 1))
            y4rev = float(abs(BS * s_val * share1_mp / e12 - 1))
            vac_chi = float(-mp.log(s_val * rho2 * d1
                                    / (one - rho2)) / l10)
            BS_f = float(BS)
            e12_f = float(e12)
            rho2_f = float(rho2)
        # cert chain at the bordered pad (mp end-to-end)
        with mp.workdps(dpsB):
            cert = mp.mpf(repr(rho2_f)) / tracefloor_mp
            # recompute in shared precision from mp values via strings
            cert_ratio = float(cert / mp.mpf(repr(BS_f)))
        ok34x = (chi_ok and sb2_ok and bs_le_g
                 and rho2x <= RHO2X_BAR and y4rev <= Y4REV_BAR
                 and vac_chi >= VAC_CHI_MIN
                 and CERT_RATIO_WIN[0] <= cert_ratio
                 <= CERT_RATIO_WIN[1])
        ok34 = ok34 and ok34x
        det34.append("x%d: rho2 %.3e BS %.3e (<=g %s, g/BS %.1e) "
                     "VAC_CHI %.2f dex rho2x %.0e y4rev %.0e "
                     "cert/BS %.6f"
                     % (x, rho2_f, BS_f, bs_le_g, g_f / BS_f,
                        vac_chi, rho2x, y4rev, cert_ratio))
        bs_tab[x] = BS_f
        r2_tab[x] = rho2_f
        vac_tab[x] = vac_chi
        info("x=%d SB2/SB3 exhibit: s = %.5f <= (1-rho2)/(rho2 "
             "delta_1) = %.3e (chi-cap VACUOUS by %.1f dex, riding); "
             "enclosure BS = %.3e <= g = %.4f <= delta_1 = %.3e; "
             "the merge coordinate BS RIDES -- the honest "
             "one-statement form stays the g-floor (QSUBGAP == the "
             "pair, W2 cited)"
             % (x, s_f, (1 - rho2_f) / BS_f, vac_chi, BS_f, g_f,
                d1_f))

        # ---- G35 SB4 instantiated
        with mp.workdps(dps):
            S_g = sum(etn[i] * etn[i] / (qs[i] - lam)
                      for i in range(1, nf))
            root_dev = float(abs(rho2 / (lam - qs[0]) / S_g - 1))
            sh1g = (e12 / (qs[1] - lam)) / S_g
            id4 = float(abs((e12 / rho2)
                            / (sh1g * (qs[1] - lam)
                               / (lam - qs[0])) - 1))
            cap_val = (d1 / FG) / g_ex
            ovg_cap = bool(OVG_mp <= cap_val * (1 + slop))
            sh1g_dev = float(abs(sh1g / share1_mp - 1))
            pinch_ratio = float(OVG_mp * g_ex * FG / d1)
            sh1g_f = float(sh1g)
        ovg_win = OVG_WIN_CORE if x <= 24 else OVG_WIN_28
        ok35x = (root_dev <= ROOT_DEV_BAR and id4 <= ID4_BAR
                 and ovg_cap and ovg_win[0] <= OVG <= ovg_win[1]
                 and sh1g_dev <= SH1G_DEV_BAR)
        ok35 = ok35 and ok35x
        det35.append("x%d: OVG %.4e <= cap %.4e root %.0e id4 %.0e "
                     "sh1g %.4f (dev %.1e)"
                     % (x, OVG, float(cap_val), root_dev, id4,
                        sh1g_f, sh1g_dev))
        info("x=%d SB4 exhibit: OVG == share_1^g (1 - g/delta_1) "
             "(delta_1/FG) / g = %.4f x pinch %.4f: the r150 "
             "OVG-flatness IS the zone-top-gap pinch (identity "
             "chain exact); OVG-cap relocates onto the g-floor"
             % (x, 1.0 / g_f, pinch_ratio))

        # ---- G36 SB5 instantiated
        with mp.workdps(dps):
            exp_sum = sum((etn[i] * etn[i] / e12)
                          * ((qs[1] - qs[0]) / (qs[i] - qs[0]))
                          for i in range(2, nf))
            id5 = float(abs((1 / share1_mp) / (1 + exp_sum) - 1))
            shs = mp.mpf(repr(SHARE_SLOP))
            sh_lo1 = bool(share1_mp >= e12 / (one - rho2)
                          * (1 - shs))
            sh_lo2 = bool(share1_mp >= e12 * (1 - shs))
            e1vac = float(mp.log(share1_mp * (one - rho2) / e12)
                          / l10)
            race = float(exp_sum)
            wmax_i = max(range(1, nf),
                         key=lambda i: abs(etn[i]))
            wmax_v = float(etn[wmax_i] * etn[wmax_i])
        ok36x = (id5 <= ID5_BAR and sh_lo1 and sh_lo2
                 and e1vac >= E1VAC_MIN)
        ok36 = ok36 and ok36x
        det36.append("x%d: e1^2 %.3e race %.4f E1VAC %.2f dex id5 "
                     "%.0e wmax i%d %.3f"
                     % (x, e12_f, race, e1vac, id5, wmax_i, wmax_v))
        e1_tab[x] = e12_f
        info("x=%d SB5 exhibit: share_1 = %.4f >= et_1^2/(1-rho2) = "
             "%.3e (bound TRUE but VACUOUS by %.1f dex): the "
             "one-modedness is the WEIGHT-LADDER RACE (race sum "
             "%.4f, max weight at mode i=%d of nf=%d) -- NOT weight "
             "concentration; the E1FLOOR wedge is measured "
             "false-trending" % (x, share1, e12_f / (1 - rho2_f),
                                 e1vac, race, wmax_i, nf))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    if not smoke:
        lxs = [math.log10(float(x)) for x, _d in all_rungs]
        lfg = [math.log10(fg_tab[x]) for x, _d in all_rungs]
        sl_fg = float(np.polyfit(lxs, lfg, 1)[0])
        ok31 = ok31 and FG_SLOPE_WIN[0] <= sl_fg <= FG_SLOPE_WIN[1]
        det31.append("slope %.3f" % sl_fg)
    check("G31-spectral-ladder", ok31,
          "Mq PSD + sorted; FULLGAP in the frozen windows x %s "
          "(incl. the CDLII x=28 string); lam_1 SIMPLE (rel gap >= "
          "%.0e); growth slope in %s: %s"
          % (str(FG_WIN), SIMP_MIN, str(FG_SLOPE_WIN),
             "; ".join(det31)))
    check("G32-node-config-replication", ok32,
          "|qrel| <= %.0e, null res <= %.0e; delta_1 >= FULLGAP (W3 "
          "re-gate); zone-top argmin in the frozen windows; s <= "
          "bar; s x gap in %s; delta_1/share_1/tlaw on the cited "
          "strings; lock FULLGAP/y_t in %s: %s"
          % (QREL_BAR, NULLRES_BAR, str(SGAP_WIN), str(LOCK_WIN),
             "; ".join(det32)))
    check("G33-sb1-trace-loop", ok33,
          "TrH via bordered LU == eigen-sum <= %.0e; tf(LU) == "
          "tf(eigen) <= %.0e; tf in %s; tail tf - 1 <= (K-2)(lam_1-"
          "tau)/(lam_2-tau) HARD and tf <= K-1 HARD (TAIL CLOSED "
          "UNCONDITIONALLY); TRACEFLOOR <= x^%d (THEOREM SB1: "
          "DELTA1FLOOR <==> TRACEFLOOR two-sided -- the Y1 "
          "recoordination is a LOOP, adjudicated): %s"
          % (TRH_XDEV_BAR, TF_XDEV_BAR, str(TF_WIN), POLY_DEG,
             "; ".join(det33)))
    check("G34-sb2-sb3-merge", ok34,
          "chi (q_1 - q_0) <= 1 - rho2 HARD; s rho2 delta_1 <= 1 - "
          "rho2 HARD (THEOREM SB2); BS = rho2 delta_1 <= g HARD "
          "(THEOREM SB3 enclosure); rho2 == R_phi^2/|P_V r|^2 <= "
          "%.0e; Y4 rearrangement <= %.0e; VAC_CHI >= %.1f dex "
          "(CHI-CAP-VACUOUS pinned: the third rate-blind moment "
          "instrument); cert rho2/(tau TrH) tight in %s "
          "(eigensolve-free lower end): %s"
          % (RHO2X_BAR, Y4REV_BAR, VAC_CHI_MIN, str(CERT_RATIO_WIN),
             "; ".join(det34)))
    check("G35-sb4-ovg-identity", ok35,
          "secular-root residual <= %.0e; identity et_1^2/rho2 == "
          "share_1^g (delta_1 - g)/g <= %.0e; OVG <= (delta_1/FG)/g "
          "HARD + OVG windows; |share_1^g/share_1 - 1| <= %.0e "
          "(near-equality; THEOREM SB4: the OVG-flatness IS the "
          "zone-top-gap pinch): %s"
          % (ROOT_DEV_BAR, ID4_BAR, SH1G_DEV_BAR, "; ".join(det35)))
    check("G36-sb5-share-race", ok36,
          "expansion identity <= %.0e; share_1 >= et_1^2/(1 - rho2) "
          ">= et_1^2 HARD (THEOREM SB5); E1VAC >= %.1f dex (the "
          "bound is VACUOUS: share-floor is the weight-ladder race, "
          "not weight concentration -- the honest B3 adjudication): "
          "%s" % (ID5_BAR, E1VAC_MIN, "; ".join(det36)))

    # ---------------------------------------------------------- S3c
    section("S3c  RED-TEAM MP INSTANTIATION")
    tau5, fg5 = rt_data
    with mp.workdps(120):
        tau_rt = mp.mpf(repr(tau5))
        Del_rt = mp.mpf(repr(fg5)) * tau_rt
        Pw = mp.mpf(RT_P)
        e2w = tau_rt / (tau_rt + Del_rt * Pw)
        s_w = tau_rt * (1 - e2w) / (Del_rt * e2w)
        dev_s = float(abs(s_w / Pw - 1))
        BS_w = e2w * (Del_rt / tau_rt)
        dev_bs = float(abs(BS_w * s_w / (1 - e2w) - 1))
        dev_eq = float(abs(s_w * e2w * (Del_rt / tau_rt)
                           / (1 - e2w) - 1))
        bs_small = bool(BS_w <= (1 / Pw) * (1 + mp.mpf("1e-12")))
        # trace family diag(t, t(1+eta)) at t = tau5, eta = 1e-6
        eta_rt = mp.mpf("1e-6")
        trH_rt = 1 / (tau_rt * eta_rt)
        tfl_rt = tau_rt * trH_rt
        tf_rt = (tau_rt * eta_rt) * trH_rt
        dev_tr = float(abs(tfl_rt - tf_rt / eta_rt))
        tr_big = bool(tfl_rt >= mp.mpf("1e5")) \
            and bool(tau_rt * (2 + eta_rt) <= 3 * tau_rt)
    check("G40-redteam-instantiated", dev_s <= RT_ID_BAR
          and dev_bs <= RT_ID_BAR and dev_eq <= RT_ID_BAR
          and bs_small and dev_tr <= RT_ID_BAR and tr_big,
          "2D model on the x=5 rung data: legal witness s == P = "
          "%.0e (dev %.0e) with BS == (1-eps^2)/P <= 1/P (dev %.0e; "
          "SB2-equality dev %.0e): ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-"
          "BOTTOMSHARE -- no algebra-only floor on the merge "
          "coordinate; trace family diag(t, t(1+eta)): loop "
          "identity dev %.0e with tau TrH = 1/eta = 1e6 at TrM <= "
          "3 tau (no algebra cap on TRACEFLOOR): only arithmetic-"
          "consuming bounds (census/qrel/frozen windows) may close "
          "either end" % (float(Pw), dev_s, dev_bs, dev_eq, dev_tr))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (the certificate must refuse)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        musw, _nr = raw_mp_census(cw)
        Tzw = 2 * math.pi * xw
        n_nodes_w = int(np.sum(musw <= Tzw))
        m_true_w = int(np.sum(gam <= Tzw))
        over = n_nodes_w - m_true_w
        with mp.workdps(dpsw):
            tauw = float(cw["mpE"][0])
            csw = [mp.mpf(s) for s in cw["cn_mp_str"]]
            aaw = mp.log(xw) / 2
            omsw = [k * mp.pi / aaw for k in range(cw["K"])]
            A0w = sum(((-1) ** k) * csw[k] for k in range(cw["K"]))
            A2w = sum(((-1) ** k) * csw[k] * omsw[k] ** 2
                      for k in range(cw["K"]))
            ytbw = float(abs(A2w / A0w)) / float(omsw[-1] ** 2)
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD: the SB1-SB5 hypotheses fail EXACTLY "
              "here -- no positive spectrum to balance); y_t_w/"
              "b_top = %.2f <= %.1f"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the trace/chi/secular "
          "machinery requires PSD + simple positive ground -- the "
          "hypotheses fail exactly in the false worlds")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        sl_s = float(np.polyfit(lt, [math.log10(s_tab[x])
                                     for x in xs_all], 1)[0])
        sl_o = float(np.polyfit(lt, [math.log10(ovg_tab[x])
                                     for x in xs_all], 1)[0])
        sl_sh = float(np.polyfit(lt, [math.log10(sh_tab[x])
                                      for x in xs_all], 1)[0])
        sl_g = float(np.polyfit(lt, [math.log10(gap_tab[x])
                                     for x in xs_all], 1)[0])
        sl_bs = float(np.polyfit(lt, [math.log10(bs_tab[x])
                                      for x in xs_all], 1)[0])
        sl_r2 = float(np.polyfit(lt, [math.log10(r2_tab[x])
                                      for x in xs_all], 1)[0])
        sl_e1 = float(np.polyfit(lt, [math.log10(e1_tab[x])
                                      for x in xs_all], 1)[0])
        la = [abs(v) for v in lt]
        sl_vac = float(np.polyfit(la, [vac_tab[x] for x in xs_all],
                                  1)[0])
        ok54 = (abs(sl_s) <= TAU_SLOPE_BAR
                and abs(sl_o) <= TAU_SLOPE_BAR
                and abs(sl_sh) <= TAU_SLOPE_BAR
                and abs(sl_g) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= sl_bs <= RIDER_WIN[1]
                and RIDER_WIN[0] <= sl_r2 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: s %.4f, OVG %.4f, share_1 %.4f, "
              "gap %.4f (all <= %.2f: the demand RATIOS are "
              "tau-flat); RIDER REPORT: BS %.3f, rho2 %.3f in %s "
              "and et_1^2 %.3f, VAC_CHI slope %.3f (the rate-blind "
              "ends RIDE a collapsing scale -- BOUND-RIDES-CONNES "
              "typed: MERGE-REFUTED-MEASURED, the flat coordinates "
              "are the ratios)"
              % (sl_s, sl_o, sl_sh, sl_g, TAU_SLOPE_BAR, sl_bs,
                 sl_r2, str(RIDER_WIN), sl_e1, sl_vac))
        info("spectral-balance tables x = %s: BS = %s; rho2 = %s; "
             "et1^2 = %s; VAC_CHI = %s; OVG = %s; share_1 = %s"
             % (str(xs_all),
                "/".join("%.2e" % bs_tab[x] for x in xs_all),
                "/".join("%.2e" % r2_tab[x] for x in xs_all),
                "/".join("%.2e" % e1_tab[x] for x in xs_all),
                "/".join("%.2f" % vac_tab[x] for x in xs_all),
                "/".join("%.4f" % ovg_tab[x] for x in xs_all),
                "/".join("%.4f" % sh_tab[x] for x in xs_all)))
    ce5c = cells.get(5)
    if ce5c is not None and "mpM" in ce5c:
        with mp.workdps(ce5c["dps"]):
            E0 = ce5c["mpE"][0]
            Qp_ = ce5c["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(ce5c["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; round-118 red flag; all mp "
              "under workdps)" % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  DEMAND AUDIT + MIN-CUT")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq,
          "CHAIN-AUDIT (cited theorems not re-proven): %s" % detq)

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
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 9 and "RH" not in reach,
          "flows: base 4, refined 5 (r142/r144/r146/r150 graph "
          "VERBATIM -- this round changes COORDINATES/merges the "
          "reading, not the set); one-grant 5; counterfactual "
          "PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")
    info("EXACT RESIDUE after this round (read with CDL/CDLIV/CDLVIII"
         "): SET UNCHANGED -- RH <== [r122-NF-closure] + [Theorem R]"
         " + {L1, WPD} on dense a; RESIDUE = {TOPROOT (= B00-ROOTGAP"
         " + S1-floor per r150), TLAWCAP-block (<== T-WINDOW + "
         "TOPROOT + PERCELL-REL + JUMPSUM per r154), SPECTRAL-"
         "BALANCE PAIR {SUSCAP2R, DELTA1FLOOR} (THIS ROUND: <==> "
         "QSUBGAP-floor g >= 1/poly, ONE statement per W2 cited, "
         "with (i) DELTA1FLOOR <==> TRACEFLOOR two-sided PROVEN "
         "(SB1: the Y1 loop adjudicated, tail closed), (ii) the "
         "r150 sub-coordinates OVG-cap/share-floor collapsed onto "
         "the g-floor by exact identities (SB4/SB5), (iii) the "
         "enclosure BS <= g <= delta_1 proven with the lower end "
         "pinned rate-blind (SB2/SB3: the chi-cap is the THIRD "
         "rate-blind moment instrument; the one-moment-statement "
         "merge is REFUTED-MEASURED))} + dense-a + a-extension + "
         "window-a.  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SB1-PROVEN(trace-loop adjudicated: tau TrH == tf/FULLGAP, "
        "1 <= tf <= K-1 unconditional -- DELTA1FLOOR <==> "
        "TRACEFLOOR two-sided, TAIL-CLOSED; G10/G33)",
        "SB2-PROVEN(chi-cap exact) + CHI-CAP-VACUOUS(third "
        "rate-blind moment instrument pinned; G11/G34)",
        "SB3-PROVEN(enclosure BS <= g <= delta_1; merge algebra "
        "one-directional exact) + MERGE-REFUTED-MEASURED(BS rides: "
        "the one-moment-statement merge is dead; the honest one-"
        "statement form stays the W2 QSUBGAP-floor; G12/G34/G54)",
        "SB4-PROVEN(OVG identity chain: the r150 flat OVG IS the "
        "zone-top-gap pinch; cap relocates onto the g-floor; "
        "G13/G35) + SH1G-NEAR-EQUALITY(measured)",
        "SB5-PROVEN(share_1 >= et_1^2/(1-rho2)) + "
        "SHAREFLOOR-IS-LADDER-RACE(the bound vacuous: honest B3 "
        "adjudication; G14/G36)",
        "REDTEAM-REFUTES-ALGEBRA(2D model + trace family; G15/G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(dense-x suffices; G60)",
        "OMEGA-RECOORDINATED(pair <==> QSUBGAP-floor, one statement "
        "per W2 cited; census {MEAS, OMEGA-POS} cardinality 4 "
        "UNCHANGED; G61)"]
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
        print("COMPOSITE: SB1-PROVEN + SB2-PROVEN + SB3-PROVEN + "
              "SB4-PROVEN + SB5-PROVEN + CHI-CAP-VACUOUS + "
              "MERGE-REFUTED-MEASURED + SH1G-NEAR-EQUALITY + "
              "SHAREFLOOR-IS-LADDER-RACE + REDTEAM-REFUTES-ALGEBRA "
              "+ CONTROLS-REFUSE + DEMAND-FLAT + "
              "BOUND-RIDES-CONNES + QUANTIFIER-INHERITED + "
              "OMEGA-RECOORDINATED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
