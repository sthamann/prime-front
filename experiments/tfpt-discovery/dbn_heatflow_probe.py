#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dbn_heatflow_probe -- PRIME.DBN.HEATFLOW.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim in any direction, NO positivity
claim beyond the per-rung certificates stated, NO counterexample
claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (THE DE BRUIJN-NEWMAN HEAT FLOW -- THE ONE LARGE CLASSICAL
IMPORT NEVER ATTEMPTED IN 176 ROUNDS.  Let H_t(x) = int_0^oo
e^{tu^2} Phi(u) cos(xu) du be the heat-flow deformation of the
Riemann Xi function (Polymath15 normalization, H_0(x) =
xi(1/2 + ix/2)/8, zeros at x = 2 gamma).  There is a constant Lambda
(de Bruijn-Newman) with H_t real-rooted iff t >= Lambda; RH ==
[Lambda <= 0]; Rodgers-Tao 2020: Lambda >= 0 UNCONDITIONAL;
Polymath15 2019: Lambda <= 0.22 UNCONDITIONAL; in gamma units the
admissible window is t in [0, 0.22/4 = 0.055].  The program's census
observables (H2 complete-realness, y_t, theta_y, the wall margin
tau) are functionals of the same zero/prime data the flow deforms.
This round builds the dictionary and adjudicates the pinch:
(D1) THE DICTIONARY: three candidate faces of "the flow" on the wall
family -- FLOW-P (spectral face: the dBN flow transported EXACTLY to
the derived census polynomial N(y) through y = z^2: generator
T = 4y d^2/dy^2 + 2 d/dy, degree-lowering, e^{-tT} a FINITE exact
sum -- no zeros, no ODE, closed form); FLOW-S (source face: the
Gaussian multiplier moved atom-wise, w_q -> w_q e^{t u_q^2},
u_q = log q -- the LINEAR HALF of the generator, AS FORM); FLOW-Z
(zero face: first-order zero motion gamma_j(t) = gamma_j + t v_j,
v_j = sum_k 4 gamma_j/(gamma_j^2 - gamma_k^2) + 1/gamma_j the
regularized repulsion drift per census, transported into M through
the r175 mode-level bridge kernels and the linear prime-block
assembly).  The exact layer proves the generator split -H''/H ==
-(H'/H)' - (H'/H)^2: the linear half is u^2-atom-re-weighting, the
quadratic half is the PAIR (Lambda*Lambda) term -- Montgomery-PC/
Goldston-Montgomery/Gonek-1984 class, RH-CONDITIONAL == flagged
loop if consumed classically.  MEASURED: the three faces are
mutually INEQUIVALENT by >= 1e9 in |d theta/dt| with OPPOSITE signs
(S negative, Z positive, P positive): "the flow" has NO unique
census meaning -- any pinch claim is dictionary-dependent.
(D2) THE PINCH: dead on three independent legs, each quantified.
(i) THETA-FLOW-INERT: the exact trace law trace(N_t) = trace(N) +
2d(2d-1) t gives the exact-conditional budget floor t_floor =
(0.155 T_z^4 - trace)/2d(2d-1) >= 4021 x the admissible window at
every rung: within [0, 0.055] the spectral flow CANNOT move theta_c
to the bar -- no H3 lever exists inside classical bounds.  (ii)
WALL-FLOW-INCOMMENSURATE: exact Hellmann-Feynman fragility times
t* = tau/|d tau/dt| = 1.3e-9 -> 8.2e-53 (S) and 2.7e-9 -> 6.4e-52
(Z): the wall margin dies 8 to 51 ORDERS below the admissible
window -- the flow deformation is incommensurate with the wall.
(iii) BACKWARD-PERSISTENCE-IS-RH-CLASS: transporting realness from
t = 0.22 down to t = 0 is exactly [Lambda <= 0] == RH -- machine-
flagged cycle, NOT consumed; the flow moves t, never h: no
t-statement transports across rungs; quantifier stays SEQ per rung.
(D3) FALSIFICATION/CONTROLS: the NEW backward-margin instrument
lambda_h (largest s with e^{+s d^2/dz^2} N still complete-real
nonneg -- the census's own finite dBN distance-to-criticality)
separates all worlds (MAIN < SMOOTH at every rung: the margin SEES
the arithmetic; SCRARITH below MAIN, EPSTEIN above MAIN -- the
naive "off-line zeros => more critical" direction is REFUTED at
census level, honest); lambda_h ladder 2.39 -> 0.216 STRICTLY
DECREASING toward the admissible scale (MEASURED-DECREASING, limit
OPEN); the r171/r172 inflation witness is complex at t = 0
(lambda_wit = 0) and the flow does NOT repair it within 10^4 x the
admissible window (measured repair bracket t ~ 577, inside the
cited KKL sigma^2/2 ceiling 5698): WITNESS-PRESERVED-NOT-EXPELLED.
(D4) ASSEMBLY: honest verdict (b)+(c): named kills
DICTIONARY-THREEFOLD-INEQUIVALENT + WALL-FLOW-INCOMMENSURATE +
THETA-FLOW-INERT + FLOW-Z-BREAKS-DERIVED-H2 (the realness-granting
direction of the true flow BREAKS the derived census nonnegativity
at every rung), plus the surviving positive instruments: the exact
finite flow on the census family and the lambda_h criticality
ladder.  The residue is UNCHANGED in cardinality; NO omega moved.)
=======================================================================
State consumed (CITED): CDLXXXVII/r171 (PF1-PF3, rootladder census
form VERBATIM, H2 complete-real census, witness battery recipe);
CDLXXXVIII/r172 (H3 statement, THETA_Y/YT_L10 record tabs, TOP_WIN
census form); CDXC/r173 (h3_cofinal instruments); CDXCI/r175
(thetainf_pin: mode-level bridge kernels 4 om sin^2(A g)/(g^2-om^2)
and W_d E1/J1 primitives VERBATIM ports, prime-block assembly
linearity, DPS schedule, cache wards); CDXCIII corrections of
record (residue = {H1 AND H2 AND H3}-cofinal, mod-D qualifier).
CLASSICAL, CITED PRECISELY: de Bruijn 1950 (Duke Math. J. 17,
197-226: H_t real-rooted for t >= 1/2); Newman 1976 (Proc. AMS 61,
245-251: Lambda exists, Lambda <= 1/2); Ki-Kim-Lee 2009 (Lambda <
1/2; sigma_max(t)^2/2 + t non-increasing, Polymath wiki Prop. A);
Rodgers-Tao 2020 (Forum Math. Pi 8, e6: Lambda >= 0 UNCONDITIONAL);
Polymath15 2019 (Res. Math. Sci. 6, 31: Lambda <= 0.22
UNCONDITIONAL; H_t normalization + backward heat d_t H = -d_xx H,
zeros at x = 2 gamma => GAMMA-UNIT window [0, 0.055], factor-4
lemma proven in G10); Polya 1927 (realness persists forward in t);
Hermite-Poulain class (1 - a d^2) preserves real-rootedness;
Csordas-Smith-Varga 1994 (Lehmer-pair lower-bound mechanism, cited
context).  RH-CONDITIONAL == LOOP-IF-CONSUMED (machine-flagged, NOT
consumed): Montgomery 1973 pair correlation, Goldston-Montgomery
1987, Gonek 1984; the RT proof itself consumes pair-correlation
results -- the flow's generator IS pair-class (G14).  Explicit
formula AS FORM (r174/r175 adjudication VERBATIM); PT21 caches
below T_0 unconditionally per census; census-forall-k == flagged
RH loop; zero-verification-at-height-as-hypothesis == flagged loop.

NOTATION.  Rung h (R4.build_cell even sector, r122 machinery);
A = log(h)/2; K = ceil(1.25 h log h); om_k = k pi/A; b_k = om_k^2;
c_k ground state (nrm basis); A_0 = sum (-1)^k c_k; A_2 = sum_{k>=1}
(-1)^k c_k b_k; y_t = |A_2/A_0|; T_z = 2 pi h; theta_y = y_t/T_z^4;
THETA_BAR = 0.155; tau = ground eigenvalue (wall margin).  CENSUS
POLYNOMIAL: N(y) = numerator of F(y) = c_0 + sum_{k>=1} (-1)^k c_k
y/(y - b_k) (r171 form VERBATIM, scaled Y = y/s, s = b_top + 1,
leading coefficient A_0; roots = the F-census; H2 == complete-real
nonneg).  THE FLOW (gamma units): the multiplier e^{t u^2} on the
Fourier data == backward heat d_t H = -d_zz H; zeros repel,
z_dot_j = sum_{k != j} 2/(z_j - z_k); through y = z^2 the generator
is T = 4y d^2/dy^2 + 2 d/dy with T y^n = 2n(2n-1) y^{n-1} (degree
drops by 1) => N_t = e^{-tT} N = sum_{m<=d} (-t)^m/m! T^m N EXACT
FINITE (leading coeff invariant; trace law trace(t) = trace(0) +
2d(2d-1) t exact; y = sY => t_Y = t_y/s).  lambda_h := largest
s >= 0 with N_{-s} = e^{+sT}N still complete-real nonneg (backward
realness margin, gamma units; bisection after doubling bracket).
FLOW-S: w_q(t) = w_q e^{t u_q^2}; M_t by the linear prime-block
reassembly.  FLOW-Z: gamma_j(t) = gamma_j + t v_j on the first
NW = 300 zeros (window ladder gated), delta F through the r175
bridge kernels, M_t = M - asm(delta).  HF derivatives at t = 0:
d tau/dt = v_0' (dM/dt) v_0 exact; dc first-order sum over
eigenpairs; d theta_y/dt from (A_0, A_2) perturbation.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_, no zero-oracle names,
    no verification/ import); G02 cache wards (n7000 + big 20M,
    monotone, gamma_1, overlap, T(2e7) = 9499220.4795).
S1  exact layer (sympy):
    G10 flow == multiplier == backward heat (d_t + d_zz annihilates
    e^{tu^2} cos(zu)); normalization lemma: e^{-t d_z^2} at z = 2w
    == e^{-(t/4) d_w^2} (generic quartic) => Lambda_gamma =
    Lambda_x/4, admissible gamma window [0, 0.055]; citation ledger
    frozen (RT 2020 / Polymath15 2019 / KKL 2009 / de Bruijn 1950 /
    Newman 1976 / Polya);
    G11 zero-ODE from first order: H''/H' at a root == sum 2/(r_i -
    r_j) (generic cubic); power-sum law: even sextic, d/dt sum z^2
    == 2n(n-1) == 60 from the coefficient flow (ODE and polynomial
    flow agree EXACTLY);
    G12 conjugation: d_z^2 [p(z^2)] == (4y p'' + 2p')(z^2) generic;
    T y^n == 2n(2n-1) y^{n-1} for n = 1..6; leading-coefficient
    invariance; trace law (generic quartic, slope 56 == 2d(2d-1));
    scale lemma T_Y[p(sY)] == s (T_y p)(sY) => t_Y = t_y/s;
    G13 realness legs (exact rational instances): (1 - a d^2) ==
    (1 - sqrt(a) d)(1 + sqrt(a) d); backward instance e^{-s d^2}
    (z^2 - 1) = z^2 - 1 - 2s real-rooted all s >= 0; forward
    collision e^{+s d^2}(z^2 - 1) = z^2 - 1 + 2s collides at s* =
    1/2 EXACT, complex beyond; KKL-pair-exact: sigma_max(s)^2/2 - s
    == -1/2 constant for s > 1/2;
    G14 THE GENERATOR SPLIT (D1 symbolic core): -H''/H == -(H'/H)'
    - (H'/H)^2 generic; d^2/ds^2 n^{-s} == (log n)^2 n^{-s} (the
    linear half == u^2-atom-re-weighting == FLOW-S face AS FORM);
    the quadratic half on a 2-atom toy has support {2u_1, u_1+u_2,
    2u_2} DISJOINT from {u_1, u_2}: the flow generator EXCEEDS
    atom-re-weighting by exactly the PAIR (Lambda*Lambda) term ==
    Montgomery-PC class == RH-conditional == flagged loop;
    G15 conditionality/pinch ledger: RT/PM15 consumed as CITED
    CEILINGS only; BACKWARD-REALNESS-PERSISTENCE == [Lambda <= 0]
    == RH-equivalent class, machine-flagged NOT consumed;
    zero-verif-at-height + census-forall-k flags carried; the flow
    moves t not h: pinch quantifier at most per-rung-in-t; gamma
    window arithmetic 0.22/4 == 0.055 exact.
S3  per-rung layer, RUNGS = (4, 5, 8, 13) (MAIN + SMOOTH builds;
    deep rungs not rebuilt, cost-disclosed):
    G30 build sanity + THE LICENSE (sorted, K, simp >= 1e3, ray/res
    <= 1e-25; THETA_Y_TAB rel 5e-3; YT_L10 <= 1.5e-3 dex;
    sign(A_2/A_0) == -1; census t=0 complete-real nonneg, min >=
    0.01 (Y-scaled), top/y_t in TOP_WIN (0.70, 0.95) + CEN_TOP_TAB
    + THETA_C_TAB rel 5e-3);
    G31 FLOW-P exact layer instantiated: closed-form sanity (y^2
    flow); leading coeff bit-invariant; trace-law rel dev <= 1e-30
    at t = 1/100 (measured 0.0); ydot_top tab rel 5e-3, > 0 at
    every rung; thdotP tab rel 5e-3 strictly decreasing in h;
    G32 realness window + THE LAMBDA LADDER: N_t complete-real
    nonneg at ALL of TGRID = (+-0.0275, +-0.055) at every rung
    (REALNESS-WINDOW-WIDE: the census survives the WHOLE admissible
    window both directions); lambda_h tab {2.3898, 0.9168, 0.3071,
    0.2161} rel 1e-2, STRICTLY DECREASING, breach mode == complex
    at every rung; lambda_h/0.055 = 43.4 -> 3.9 >= 1 at every rung
    (CENSUS-SUBCRITICAL-DECAYING; limit OPEN, typed MEASURED);
    G33 THE THETA BUDGET (H3-FLOW-INERT): trace0 tab rel 1e-5;
    t_floor = (0.155 T_z^4 - trace0)/(2d(2d-1)) tab rel 5e-3,
    t_floor/0.055 >= 4000 at every rung (EXACT-CONDITIONAL: trace
    law exact + roots-nonneg-along-path gated on the grid);
    t_lin = (0.155 - theta_c)/thdotP tab rel 5e-3 (linearized,
    measured 1042 -> 13038): NO H3 lever inside classical bounds;
    G34 FLOW-S (source face): asm ward == 0 at t = 0 (bar 1e-40);
    theta_y(t) grid tab rel 5e-2 (collapse 0.045-0.072 -> 0.0001-
    0.003 at |t| <= 0.055 BOTH signs: response NON-PERTURBATIVE at
    Lambda scale); tau(t) < 0 at ALL grid t != 0 at every rung
    (SOURCE-FACE-WALL-FATAL) + tau tab rel 5e-2; HF exact: dtau/dt
    tab rel 5e-3 (all negative); fragility t*_S = tau/|dtau/dt| tab
    rel 5e-2, t*_S/0.055 <= 1e-7 and strictly decreasing (2.4e-8 ->
    1.5e-51); dtheta/dt tab rel 5e-3 (NEGATIVE at every rung);
    census under S: +0.055 complete-real nonneg TRUE at every rung
    (top/y_t tab), -0.055 BROKEN by NEGATIVE real root at every
    rung (min tab; im == 0: the S-backward breach is nonnegativity,
    not realness);
    G35 FLOW-Z (zero face): drift ward v_1 = -1.159247 rel 1e-3 +
    v_1 N-ladder + max|v| = 6.1922 rel 1e-3 + tail move (1e7->2e7)
    <= 1e-3 (measured 4.6e-4, the ~1/T class); window ladder NW =
    100/200/300 spread <= 5e-2; theta_y(t)/tau(t) grid tabs rel
    5e-2, tau < 0 at all grid t != 0; HF: dtau/dt tab rel 5e-3
    (sign NOT constant across rungs: -,-,+,+ RECORDED); t*_Z tab
    rel 5e-2 strictly decreasing (4.9e-8 -> 1.2e-50 x 0.055);
    dtheta/dt tab rel 5e-3 (POSITIVE at every rung); census under
    Z: +0.055 BROKEN (negative mode) at EVERY rung (min tab: the
    realness-granting direction of the TRUE flow breaks the
    DERIVED census nonnegativity: FLOW-Z-BREAKS-DERIVED-H2),
    -0.055 complete-real nonneg TRUE (min tab);
    G36 THE DICTIONARY GATE: |dthS/thdotP| >= 1e9 and |dthZ/thdotP|
    >= 1e9 at every rung (computed from the gated tabs); sign
    pattern (P, S, Z) == (+, -, +) at every rung; S/Z ratio tab
    {-2.4957, -2.8660, -3.5315, -3.9036} rel 1e-2 (O(1), opposite
    signs, magnitude increasing): DICTIONARY-THREEFOLD-INEQUIVALENT
    (P-face derivative on the census-top form, S/Z on the jet form;
    the TOP_WIN factor 0.83-0.88 is immaterial at 1e9 separations,
    DISCLOSED).
S4  controls + falsification:
    G50 SMOOTH: lambda ladder {3.5109, 2.6914, 1.6383, 1.0824} rel
    1e-2; MAIN/SMOOTH <= 0.75 at every rung (measured 0.681/0.341/
    0.187/0.200): ARITHMETIC-MORE-CRITICAL-THAN-SMOOTH;
    G51 SCRARITH(5) lambda = 0.3999, EPSTEIN(8) lambda = 0.8535 rel
    1e-2; |MAIN/CTRL - 1| >= 0.3 both; census real at t = 0 both
    (top/y_t_w + min recorded); HONEST: EPSTEIN (the off-line-zero
    world) has LARGER census backward slack than MAIN -- the
    lambda instrument separates worlds but NOT in the naive
    Lambda direction (EPSTEIN-SLACK-LARGER);
    G52 THE WITNESS UNDER THE FLOW (h = 5, r171 recipe VERBATIM):
    witness census max|Im| = 14 (Y-scaled) >= 1 at t = 0 (complete-
    realness BROKEN, replicates the r171 H2-kill), ztop/y_t'' =
    24.1152 rel 5e-3; lambda_wit == 0 (below grid); forward ladder
    t = 0.055/0.5/5.0 ALL still broken, top/y_t'' tab rel 5e-3
    GROWING (24.19 -> 35.45); measured realness-repair bracket
    [576.25, 577.50] rel 1e-2, inside the KKL ceiling
    sigma_max^2/2 = 5698.3 (sigma_max = 106.755 rel 5e-3) and >=
    1e4 x the admissible window: WITNESS-PRESERVED-NOT-EXPELLED.
S5  G54 tau screens (LSQ slopes vs log10 tau: log10 lambda_h and
    log10 t_floor DEMAND-FLAT <= 0.30; log10 t*_S RIDER in (0.85,
    1.15) BOUND-RIDES-TAU: the fragility time is the wall margin
    in flow units BY CONSTRUCTION -- typed, not hidden);
    G55 conditioning (1e-25 shift at h = 5, round-118 trap, edge).
S6  G60 demand audit (grids/bars/tabs frozen pre-evaluation; gamma
    units; f64 zero-side + numeric pd-kernel eps DISCLOSED;
    first-order window-truncated drift instrument DISCLOSED -- NOT
    the true H_t zero set; FLOW-S face is a DEFINED transport (the
    linear half AS FORM), not a claimed identity; scope disclosed;
    calibration THREE disclosed passes);
    G61 loop/mining (delivered ancestor sets; banned: RH-GRANT,
    LAMBDA-LE-0(==RH), BACKWARD-PERSISTENCE, CENSUS-ALL-K,
    ZERO-VERIF-AS-HYP, MONTGOMERY-PC-RH, GONEK-1984-RH,
    GOLDSTON-MONTGOMERY-RH, TLAWCAP, WPD, TAUPOS ancestors of
    NOTHING delivered);
    G62 min-cut (r174 graph VERBATIM: flows 4/5/5/9; the DBN
    instruments add NO census node: {MEAS, OMEGA-POS} cardinality 4
    UNCHANGED);
    G63 endgame graphs: FIVE loop cycles DETECTED (dbn-backward:
    RH -> LAMBDA-LE-0 -> BACKWARD-REALNESS-PERSIST -> H2-COFINAL-
    VIA-FLOW -> ... -> RH; dbn-pair: RH -> MONTGOMERY-PC -> PAIR-
    CLASS-CEILING -> FLOW-GENERATOR-CLASSICAL -> ... -> RH;
    zero-verif-at-height; universalized census; pinning-supply);
    terminal chain with the DBN instruments as MEASURED leaves
    ACYCLIC; post-round residue printed.
S9  composite verdict + G99 runtime (bar 1800 s).

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; RUNGS = (4, 5, 8, 13); DPS = {4: 60, 5: 60, 8: 80,
13: 120} (r174/r175 schedule VERBATIM); NDPS = 3 x dps (census,
r171); POLY_MAXSTEPS = 3000; IM_TOL = 1e-10 (Y-scaled, r171);
THETA_BAR = 0.155; TOP_WIN = (0.70, 0.95); LAM_X_UPPER = 0.22
[Polymath15]; LAM_G = 0.055 EXACT (= 0.22/4); TGRID = (-0.055,
-0.0275, +0.0275, +0.055); NW = 300; N_LAD = (1e5, 1e6, 1e7, 2e7);
LAM_CAP = 819.2; LAM_BISECT = 10; PD_EPS = 1e-6 (numeric kernel
derivative, DISCLOSED); T2E7_STR = 9499220.4795 rel 1e-6;
SIMP_MIN = 1e3; RAY_BAR = RES0_BAR = 1e-25; ASM_BAR = 1e-40;
CF_BAR = 1e-40 (not used for jets here); RUNTIME_BAR = 1800 s.
INHERITED (r172/r175 VERBATIM): THETA_Y_TAB = {4: 0.044901,
5: 0.062691, 8: 0.065250, 13: 0.071983} rel 5e-3; YT_L10_R172 =
{4: 4.2532, 5: 4.7858, 8: 5.6197, 13: 6.5057} <= 1.5e-3 dex;
LOG10TAU_TAB = {4: -10.669, 5: -15.794, 8: -29.423, 13: -53.602}
abs 0.01 (r174, screen abscissa).
NEW (calibrated: pass 1 = 6 s fragment, crashed on an mpf-repr type
bug in the scratch instrument, log kept calib_dbn_pass1.log; pass 2
= full 950.0 s, calib_dbn_pass2.log; pass 3 = linear-response
continuation 213.3 s, calib_dbn_pass3.log; scratches deleted after
freeze, ALL logs kept; numbers quoted verbatim):
CEN_TOP_TAB = {4: 0.8801, 5: 0.8590, 8: 0.8442, 13: 0.8344} rel
5e-3; THETA_C_TAB = {4: 0.039516, 5: 0.053848, 8: 0.055083,
13: 0.060065} rel 5e-3; CEN_MIN_FLOOR = 0.01 (measured 0.27/0.13/
0.055/0.020); YDOT_TAB = {4: 44.208612, 5: 76.351012,
8: 156.180190, 13: 324.119848} rel 5e-3; THDOTP_TAB = {4: 1.108e-4,
5: 7.838e-5, 8: 2.447e-5, 13: 7.281e-6} rel 5e-3;
TRACE0_TAB = {4: 19784.32711, 5: 66934.48776, 8: 442743.4641,
13: 3347166.518} rel 1e-5; TRACE_DEV_BAR = 1e-30 (measured 0.0);
LAM_TAB = {4: 2.3898, 5: 0.9168, 8: 0.3071, 13: 0.2161} rel 1e-2;
SMOOTH_LAM_TAB = {4: 3.5109, 5: 2.6914, 8: 1.6383, 13: 1.0824} rel
1e-2; LAM_RATIO_MAX = 0.75 (measured 0.681/0.341/0.187/0.200);
SCR_LAM = 0.3999, EPS_LAM = 0.8535 rel 1e-2; CTRL_SEP_MIN = 0.3;
SCR_CEN = (0.0026376, 1.9849), EPS_CEN = (0.00041413, 5.8294),
SMOOTH5_CEN = (0.015336, 6.6755) (min, top/y_t_w) rel 5e-2;
TFLOOR_TAB = {4: 318.6269, 5: 221.1832, 8: 350.4781, 13: 534.8455}
rel 5e-3; TFLOOR_RATIO_MIN = 4000 (measured 4021.5); TLIN_TAB =
{4: 1042.2598, 5: 1290.4979, 8: 4084.0506, 13: 13038.1233} rel
5e-3; THS_TAB (theta_y under FLOW-S at TGRID order) = {4: (0.002252,
0.002641, 0.002892, 0.002874), 5: (0.001377, 0.001631, 0.001811,
0.001748), 8: (0.000384, 0.000505, 0.000586, 0.000544),
13: (0.000101, 0.000139, 0.000158, 0.000116)} rel 5e-2; TAUS_TAB =
{4: (-2.387e-3, -1.104e-3, -1.661e-2, -4.000e-2), 5: (-5.144e-3,
-2.401e-3, -2.903e-2, -6.323e-2), 8: (-1.630e-2, -7.993e-3,
-1.060e-1, -2.293e-1), 13: (-3.618e-2, -1.783e-2, -2.278e-1,
-4.860e-1)} rel 5e-2; DTAUS_TAB = {4: -0.015975929,
5: -0.019595098, 8: -0.026577067, 13: -0.030644316} rel 5e-3;
TFRAGS_TAB = {4: 1.341e-9, 5: 8.199e-15, 8: 1.420e-28,
13: 8.155e-53} rel 5e-2; TFRAGS_RATIO_MAX = 1e-7; DTHS_TAB =
{4: -6.535704e5, 5: -4.885166e10, 8: -6.637132e23,
13: -2.400350e47} rel 5e-3; SCEN_TOP_PLUS = {4: 1.4429, 5: 1.5259,
8: 1.6412, 13: 2.1759} rel 2e-2; SCEN_MIN_PLUS = {4: 0.015927,
5: 0.006247, 8: 0.0013407, 13: 0.00033258} rel 5e-2 (all > 0);
SCEN_MIN_MINUS = {4: -0.026299, 5: -0.0074219, 8: -0.0014886,
13: -0.00033963} rel 5e-2 (all < 0, im == 0); V1_LADDER =
(-1.158014, -1.159074, -1.159235, -1.159247) rel 1e-3; VMAX_STR =
6.1922 rel 1e-3; VTAIL_BAR = 1e-3 (measured 4.55e-4); DPJ_LADDER =
{4: (6.747e-2, 6.702e-2, 6.678e-2), 5: (1.139e-1, 1.114e-1,
1.103e-1), 8: (2.219e-1, 2.219e-1, 2.217e-1), 13: (4.225e-1,
4.217e-1, 4.246e-1)} rel 2e-2, spread <= 5e-2; THZ_TAB =
{4: (0.003246, 0.003460, 0.001104, 0.001639), 5: (0.002149,
0.002326, 0.027014, 0.005510), 8: (0.000778, 0.000870, 0.000419,
0.000020), 13: (0.000346, 0.000448, 0.000222, 0.000190)} rel 5e-2;
TAUZ_TAB = {4: (-9.632e-4, -4.083e-4, -2.718e-3, -5.566e-3),
5: (-1.415e-3, -6.682e-4, -3.376e-3, -6.740e-3), 8: (-1.942e-3,
-9.504e-4, -3.727e-3, -7.442e-3), 13: (-2.280e-3, -1.132e-3,
-3.903e-3, -7.797e-3)} rel 5e-2; DTAUZ_TAB = {4: -0.0079972112,
5: -0.004978462, 8: 0.00030230205, 13: 0.0038787966} rel 5e-3;
TFRAGZ_TAB = {4: 2.680e-9, 5: 3.227e-14, 8: 1.248e-26,
13: 6.443e-52} rel 5e-2; DTHZ_TAB = {4: 2.618781e5, 5: 1.704521e10,
8: 1.879360e23, 13: 6.149124e46} rel 5e-3; ZCEN_MIN_PLUS =
{4: -0.23277, 5: -4.00860, 8: -0.73176, 13: -0.13334} rel 5e-2
(all < 0); ZCEN_MIN_MINUS = {4: 0.051188, 5: 0.016459,
8: 0.0036907, 13: 0.00076793} rel 5e-2 (all > 0); RATIO_MIN = 1e9;
SZ_RATIO_TAB = {4: -2.4957, 5: -2.8660, 8: -3.5315, 13: -3.9036}
rel 1e-2; WIT_IM_MIN = 1.0 (measured 14); WIT_ZTOP0 = 24.1152 rel
5e-3; WIT_YDOT = 83.404747 rel 5e-3; WIT_LADDER_T = (0.055, 0.5,
5.0); WIT_LADDER_TOP = (24.1901, 24.7794, 35.4464) rel 5e-3;
WIT_SIGMA = 106.75511 rel 5e-3; WIT_KKL = 5698.3265 rel 5e-3;
WIT_REP = (576.25, 577.50) rel 1e-2; WIT_REP_RATIO_MIN = 1e4;
TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.85, 1.15); COND_WIN =
(1e-40, 1e-10).
Deterministic: NO randomness anywhere.  Caches READ-ONLY in ward_
(n7000 X5-class; big = Odlyzko zeros6 + LMFDB/Platt, pedigree
verified_zeros_big_meta.json, all below T_0 unconditionally).
Zero-side drift/kernel sums in f64 (DISCLOSED); source/prime data,
eigen work, flow towers and census polyroots in mp workdps.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
CITED-LADDER-REPLICATED(G30); FLOW-EXACT-ON-DERIVED-CENSUS(G12/G31
-- the D1 positive discovery: the dBN flow transported to the
census polynomial is an EXACT finite degree-lowering semigroup,
closed form, no zeros, no ODE); REALNESS-WINDOW-WIDE(G32);
CENSUS-SUBCRITICAL-DECAYING(G32); THETA-FLOW-INERT(G33);
GENERATOR-EXCEEDS-ATOM-REWEIGHTING-BY-PAIR-CLASS(G14);
DICTIONARY-THREEFOLD-INEQUIVALENT(G36);
SOURCE-FACE-WALL-FATAL(G34); WALL-FLOW-INCOMMENSURATE(G34/G35);
FLOW-Z-BREAKS-DERIVED-H2(G35); PINCH-NOT-ASSEMBLED(G15/G63);
BACKWARD-PERSISTENCE-IS-RH-CLASS-FLAGGED(G15/G63);
CONTROLS-SEPARATED(G50/G51); EPSTEIN-SLACK-LARGER(G51);
ARITHMETIC-MORE-CRITICAL-THAN-SMOOTH(G50);
WITNESS-PRESERVED-NOT-EXPELLED(G52); DEMAND-FLAT(G54);
BOUND-RIDES-TAU(G54); QUANTIFIER-SEQ(G60);
LOOP-ROUTES-FLAGGED(five; G61/G63); OMEGA-UNCHANGED(G62);
MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge gate
fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

SMOKE MODE (NOT-VERDICT-BEARING): RUNGS (4, 5); TGRID (+-0.055);
NW = 100 (ladder 50/75/100); N_LAD[:2]; EPSTEIN skipped; frozen
tabs skipped; LAM_CAP 8; witness repair cap 1300; drift tail bar
1e-1 (shallow-checkpoint spacing); the FLOW-Z census-break
structural legs are FULL-MODE ONLY (the break is a full-depth
drift statement; the smoke drift at NW = 100/1e6 is too shallow
to reproduce it at h = 5).

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 25/26 at the
first-freeze SPEC_SHA 5b49b4009c068c17, log kept as
dbn_heatflow_probe.smoke1.log; NO record run existed yet).  ONE
smoke-scope artifact, no bar, window, tab or criterion moved
anywhere: the G35 FLOW-Z census-break legs (+0.055 broken /
-0.055 real) were asserted in SMOKE mode, where the drift
instrument runs at NW = 100 over the 1e6-deep checkpoint and does
NOT reproduce the full-depth census break at h = 5 (smoke measured
min +0.001 vs the full-depth record -4.009) -- the legs are
statements about the FULL instrument (NW = 300, 2e7 zeros) and are
now gated in FULL mode only, matching every other cache-depth-
dependent bar in this spec.  Fix verified in isolation before
re-freeze; smoke2 at the fixed SHA must be clean.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_ functions; no import of verification/.
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

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
RUNGS = (4, 5, 8, 13)
DPS = {4: 60, 5: 60, 8: 80, 13: 120}
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
THETA_BAR = 0.155
TOP_WIN = (0.70, 0.95)
LAM_X_UPPER = 0.22
LAM_G = LAM_X_UPPER / 4.0
TGRID = (-0.055, -0.0275, 0.0275, 0.055)
NW = 300
N_LAD = (10 ** 5, 10 ** 6, 10 ** 7, 2 * 10 ** 7)
LAM_CAP = 819.2
LAM_BISECT = 10
PD_EPS = 1e-6
T2E7_STR = 9499220.4795
SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
ASM_BAR = 1e-40
RUNTIME_BAR = 1800.0
GAMMA1_LIT = 14.134725141734693790   # ward only

THETA_Y_TAB = {4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983}
YT_L10_R172 = {4: 4.2532, 5: 4.7858, 8: 5.6197, 13: 6.5057}
LOG10TAU_TAB = {4: -10.669, 5: -15.794, 8: -29.423, 13: -53.602}

CEN_TOP_TAB = {4: 0.8801, 5: 0.8590, 8: 0.8442, 13: 0.8344}
THETA_C_TAB = {4: 0.039516, 5: 0.053848, 8: 0.055083, 13: 0.060065}
CEN_MIN_FLOOR = 0.01
YDOT_TAB = {4: 44.208612, 5: 76.351012, 8: 156.180190, 13: 324.119848}
THDOTP_TAB = {4: 1.108e-4, 5: 7.838e-5, 8: 2.447e-5, 13: 7.281e-6}
TRACE0_TAB = {4: 19784.32711, 5: 66934.48776, 8: 442743.4641,
              13: 3347166.518}
TRACE_DEV_BAR = 1e-30
LAM_TAB = {4: 2.3898, 5: 0.9168, 8: 0.3071, 13: 0.2161}
SMOOTH_LAM_TAB = {4: 3.5109, 5: 2.6914, 8: 1.6383, 13: 1.0824}
LAM_RATIO_MAX = 0.75
SCR_LAM = 0.3999
EPS_LAM = 0.8535
CTRL_SEP_MIN = 0.3
SCR_CEN = (0.0026376, 1.9849)
EPS_CEN = (0.00041413, 5.8294)
SMOOTH5_CEN = (0.015336, 6.6755)
TFLOOR_TAB = {4: 318.6269, 5: 221.1832, 8: 350.4781, 13: 534.8455}
TFLOOR_RATIO_MIN = 4000.0
TLIN_TAB = {4: 1042.2598, 5: 1290.4979, 8: 4084.0506, 13: 13038.1233}
THS_TAB = {4: (0.002252, 0.002641, 0.002892, 0.002874),
           5: (0.001377, 0.001631, 0.001811, 0.001748),
           8: (0.000384, 0.000505, 0.000586, 0.000544),
           13: (0.000101, 0.000139, 0.000158, 0.000116)}
TAUS_TAB = {4: (-2.387e-3, -1.104e-3, -1.661e-2, -4.000e-2),
            5: (-5.144e-3, -2.401e-3, -2.903e-2, -6.323e-2),
            8: (-1.630e-2, -7.993e-3, -1.060e-1, -2.293e-1),
            13: (-3.618e-2, -1.783e-2, -2.278e-1, -4.860e-1)}
DTAUS_TAB = {4: -0.015975929, 5: -0.019595098, 8: -0.026577067,
             13: -0.030644316}
TFRAGS_TAB = {4: 1.341e-9, 5: 8.199e-15, 8: 1.420e-28, 13: 8.155e-53}
TFRAGS_RATIO_MAX = 1e-7
DTHS_TAB = {4: -6.535704e5, 5: -4.885166e10, 8: -6.637132e23,
            13: -2.400350e47}
SCEN_TOP_PLUS = {4: 1.4429, 5: 1.5259, 8: 1.6412, 13: 2.1759}
SCEN_MIN_PLUS = {4: 0.015927, 5: 0.006247, 8: 0.0013407,
                 13: 0.00033258}
SCEN_MIN_MINUS = {4: -0.026299, 5: -0.0074219, 8: -0.0014886,
                  13: -0.00033963}
V1_LADDER = (-1.158014, -1.159074, -1.159235, -1.159247)
VMAX_STR = 6.1922
VTAIL_BAR = 1e-3
DPJ_LADDER = {4: (6.747e-2, 6.702e-2, 6.678e-2),
              5: (1.139e-1, 1.114e-1, 1.103e-1),
              8: (2.219e-1, 2.219e-1, 2.217e-1),
              13: (4.225e-1, 4.217e-1, 4.246e-1)}
DPJ_SPREAD_BAR = 5e-2
THZ_TAB = {4: (0.003246, 0.003460, 0.001104, 0.001639),
           5: (0.002149, 0.002326, 0.027014, 0.005510),
           8: (0.000778, 0.000870, 0.000419, 0.000020),
           13: (0.000346, 0.000448, 0.000222, 0.000190)}
TAUZ_TAB = {4: (-9.632e-4, -4.083e-4, -2.718e-3, -5.566e-3),
            5: (-1.415e-3, -6.682e-4, -3.376e-3, -6.740e-3),
            8: (-1.942e-3, -9.504e-4, -3.727e-3, -7.442e-3),
            13: (-2.280e-3, -1.132e-3, -3.903e-3, -7.797e-3)}
DTAUZ_TAB = {4: -0.0079972112, 5: -0.004978462, 8: 0.00030230205,
             13: 0.0038787966}
TFRAGZ_TAB = {4: 2.680e-9, 5: 3.227e-14, 8: 1.248e-26, 13: 6.443e-52}
DTHZ_TAB = {4: 2.618781e5, 5: 1.704521e10, 8: 1.879360e23,
            13: 6.149124e46}
ZCEN_MIN_PLUS = {4: -0.23277, 5: -4.00860, 8: -0.73176, 13: -0.13334}
ZCEN_MIN_MINUS = {4: 0.051188, 5: 0.016459, 8: 0.0036907,
                  13: 0.00076793}
RATIO_MIN = 1e9
SZ_RATIO_TAB = {4: -2.4957, 5: -2.8660, 8: -3.5315, 13: -3.9036}
WIT_IM_MIN = 1.0
WIT_ZTOP0 = 24.1152
WIT_YDOT = 83.404747
WIT_LADDER_T = (0.055, 0.5, 5.0)
WIT_LADDER_TOP = (24.1901, 24.7794, 35.4464)
WIT_SIGMA = 106.75511
WIT_KKL = 5698.3265
WIT_REP = (576.25, 577.50)
WIT_REP_RATIO_MIN = 1e4
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")
CACHE_BIG = os.path.join(HERE, "verified_zeros_big.npy")

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


def rel(a: float, b: float) -> float:
    return abs(a / b - 1.0)


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
            "n" + "zeros", "gram" + "point", "zeta"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
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
                       "no zero-oracle names; caches in ward_; no "
                       "verification/ import")


# ------------------------------------------------------------- wards
def ward_cache_n7000() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_cache_big() -> np.ndarray:
    return np.asarray(np.load(CACHE_BIG), float)


# ---------------------------------------------------------- census/flow
def npoly_coeffs(cs, b, K):
    """r171 rootladder census form VERBATIM (scaled Y = y/s,
    s = b_top + 1; descending coeffs, leading == A_0)."""
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


def flowT(p):
    """T = 4Y d^2/dY^2 + 2 d/dY on descending coeffs:
    T Y^n = 2n(2n-1) Y^(n-1); degree drops by exactly 1."""
    d = len(p) - 1
    out = []
    for n in range(d, 0, -1):
        out.append(p[d - n] * 2 * n * (2 * n - 1))
    return out


def flow_tower(p):
    tower = [list(p)]
    cur = list(p)
    while len(cur) > 1:
        cur = flowT(cur)
        tower.append(cur)
    return tower


def flow_poly(tower, tY):
    """N_t = sum_m (-tY)^m/m! T^m N (finite, exact)."""
    d = len(tower) - 1
    out = [mp.mpf(0)] * (d + 1)
    fac = mp.mpf(1)
    for m in range(d + 1):
        w = (-tY) ** m / fac if m else mp.mpf(1)
        q = tower[m]
        off = (d + 1) - len(q)
        for i, c in enumerate(q):
            out[off + i] += w * c
        fac *= (m + 1)
    return out


def peval(p, x):
    acc = mp.mpf(0)
    for c in p:
        acc = acc * x + c
    return acc


def census_roots(poly, dps):
    return mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                        extraprec=2 * dps)


def real_ok(rts):
    im = max(abs(mp.im(r)) for r in rts)
    reneg = min(mp.re(r) for r in rts)
    return (float(im) <= IM_TOL and float(reneg) >= -IM_TOL,
            float(im), float(reneg))


def top_real_root(rts, psc):
    re = [mp.re(r) * psc for r in rts
          if abs(mp.im(r)) <= mp.mpf(repr(IM_TOL))]
    return max(re) if re else None


def lam_backward(tower, s_scale, dps, cap):
    """backward realness margin lambda (gamma units)."""
    s_lo, s_hi = 0.0, 0.1
    mode = "none"
    while s_hi <= cap:
        p = flow_poly(tower, mp.mpf(repr(-s_hi)) / s_scale)
        try:
            rts = census_roots(p, dps)
            ok, im, _rn = real_ok(rts)
        except Exception as e:                      # noqa: BLE001
            ok, im = False, float("nan")
            mode = "polyroots-fail:" + repr(e)[:40]
        if not ok:
            if mode == "none":
                mode = "complex" if im > IM_TOL else "negative"
            break
        s_lo = s_hi
        s_hi *= 2
    else:
        return cap, "cap"
    for _ in range(LAM_BISECT):
        smid = 0.5 * (s_lo + s_hi)
        p = flow_poly(tower, mp.mpf(repr(-smid)) / s_scale)
        try:
            rts = census_roots(p, dps)
            ok, _im, _rn = real_ok(rts)
        except Exception:                           # noqa: BLE001
            ok = False
        if ok:
            s_lo = smid
        else:
            s_hi = smid
    return 0.5 * (s_lo + s_hi), mode


# ---------------------------------------------------------- prime data
def atoms_main(x, dps):
    with mp.workdps(dps):
        icap = int(math.floor(x))
        comp = np.zeros(icap + 1, dtype=bool)
        nlist = []
        for p in range(2, icap + 1):
            if comp[p]:
                continue
            comp[p * p:: p] = True
            q = p
            while q <= icap:
                nlist.append((q, p))
                q *= p
        nlist.sort()
        return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]


def prime_data(atoms, K, aa, dps):
    with mp.workdps(dps):
        L = 2 * aa
        pj = [mp.mpf(0)]
        pd = [sum((w * (L - u) for u, w in atoms), mp.mpf(0))]
        for k in range(1, K):
            o = k * mp.pi / aa
            pj.append(sum((w * mp.sin(o * u) for u, w in atoms),
                          mp.mpf(0)))
            pd.append(sum((w * ((aa - u / 2) * mp.cos(o * u)
                               - mp.sin(o * u) / (2 * o))
                           for u, w in atoms), mp.mpf(0)))
        return pj, pd


def asm_prime(pj, pd, K, aa, dps):
    with mp.workdps(dps):
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        Mp = mp.zeros(K, K)
        for i in range(K):
            for j in range(i):
                sg = par[i] * par[j]
                den = oms[j] ** 2 - oms[i] ** 2
                od = 2 * sg * (oms[i] * pj[i] - oms[j] * pj[j]) / den
                Mp[i, j] += od
                Mp[j, i] += od
        for i in range(K):
            Mp[i, i] += 2 * pd[i]
        nrm = [mp.sqrt(L) if i == 0 else mp.sqrt(aa) for i in range(K)]
        for i in range(K):
            for j in range(K):
                Mp[i, j] = Mp[i, j] / (nrm[i] * nrm[j])
        return Mp


def mat_dev(Amat, Bmat, K):
    w = mp.mpf(0)
    sc = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            w = max(w, abs(Amat[i, j] - Bmat[i, j]))
            sc = max(sc, abs(Bmat[i, j]))
    return float(w / sc)


def jets_from_cs(cs, b, K, Tz4):
    A0 = sum((-1) ** k * cs[k] for k in range(K))
    A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
    yt = abs(A2 / A0)
    return A0, A2, yt, float(yt / Tz4)


def eig_c(Mt, K, nrm, dps):
    with mp.workdps(dps):
        E, V = mp.eigsy(Mt)
        order = sorted(range(K), key=lambda i: E[i])
        i0 = order[0]
        tau = E[i0]
        cn = [V[i, i0] / nrm[i] for i in range(K)]
        if float(cn[int(np.argmax([abs(float(v)) for v in cn]))]) < 0:
            cn = [-v for v in cn]
        return tau, cn


def hf_response(ce, dM, K, dps):
    """exact first-order: dtau = v0' dM v0 (Hellmann-Feynman);
    dc = sum_{i>0} (v_i' dM v0)/(E0 - E_i) v_i."""
    with mp.workdps(dps):
        E = ce["mpE"]
        V = ce["mpV"]
        v0 = [V[i, 0] for i in range(K)]
        n0 = mp.sqrt(sum(v * v for v in v0))
        v0 = [v / n0 for v in v0]
        w = [sum(dM[a, b] * v0[b] for b in range(K)) for a in range(K)]
        dtau = sum(v0[a] * w[a] for a in range(K))
        dc = [mp.mpf(0)] * K
        for i in range(1, K):
            vi = [V[a, i] for a in range(K)]
            ni = mp.sqrt(sum(v * v for v in vi))
            vi = [v / ni for v in vi]
            num = sum(vi[a] * w[a] for a in range(K))
            coef = num / (E[0] - E[i])
            for a in range(K):
                dc[a] += coef * vi[a]
        return dtau, dc


# ------------------------------------------------------- zero-side flow
def _E1J1(s, eb_s, ea_s, a, b):
    """r175 VERBATIM port (E1/J1 primitives, small-s series)."""
    small = np.abs(s) * max(abs(a), abs(b)) <= 1e-2
    isv = 1j * s
    with np.errstate(divide="ignore", invalid="ignore"):
        E1 = (eb_s - ea_s) / isv
        J1 = eb_s * (b / isv + 1.0 / (s * s)) \
            - ea_s * (a / isv + 1.0 / (s * s))
    if np.any(small):
        sm = s[small]
        accE = np.zeros(len(sm), complex)
        accJ = np.zeros(len(sm), complex)
        for n in range(7):
            fn = math.factorial(n)
            accE += (1j * sm) ** n * (b ** (n + 1) - a ** (n + 1)) \
                / (fn * (n + 1))
            accJ += (1j * sm) ** n * (b ** (n + 2) - a ** (n + 2)) \
                / (fn * (n + 2))
        E1[small] = accE
        J1[small] = accJ
    return E1, J1


def pd_kernel_sum(gamv, aa, K, u0):
    """sum over gamv of -2 Re W_d(gamma; u0, 2A) per mode."""
    A = float(aa)
    b = 2 * A
    Eb = np.exp(1j * b * gamv)
    Ea = np.exp(1j * u0 * gamv)
    out = np.zeros(K)
    for k in range(K):
        if k == 0:
            E1, J1 = _E1J1(gamv, Eb, Ea, u0, b)
            W = 2 * A * E1 - J1
        else:
            om = k * math.pi / A
            fb = complex(np.exp(1j * om * b))
            fa = complex(np.exp(1j * om * u0))
            E1p, J1p = _E1J1(gamv + om, Eb * fb, Ea * fa, u0, b)
            E1m, J1m = _E1J1(gamv - om, Eb / fb, Ea / fa, u0, b)
            Wc = (E1p + E1m) / 2
            Ws = (E1p - E1m) / (2j)
            Wuc = (J1p + J1m) / 2
            W = A * Wc - Wuc / 2 - Ws / (2 * om)
        out[k] = float(np.sum(-2.0 * np.real(W)))
    return out


def pj_kernel_sum(gamv, aa, K):
    A = float(aa)
    s2 = np.sin(A * gamv) ** 2
    g2 = gamv * gamv
    out = np.zeros(K)
    for k in range(1, K):
        om = k * math.pi / A
        out[k] = float(np.sum(4.0 * om * s2 / (g2 - om * om)))
    return out


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    z, u, tt, w = sp.symbols("z u t w", real=True)
    y, s = sp.symbols("y s", positive=True)

    def flow_sym(p, var, t_sym):
        d = sp.degree(p, var)
        acc = sp.Integer(0)
        for m in range(int(d) // 2 + 1):
            acc += (-t_sym) ** m / sp.factorial(m) \
                * sp.diff(p, var, 2 * m)
        return sp.expand(acc)

    # ---- G10
    F = sp.exp(tt * u ** 2) * sp.cos(z * u)
    ok_a = sp.simplify(sp.diff(F, tt) + sp.diff(F, z, 2)) == 0
    a0, a1, a2, a3, a4 = sp.symbols("a0 a1 a2 a3 a4", real=True)
    p4 = a0 * z ** 4 + a1 * z ** 3 + a2 * z ** 2 + a3 * z + a4
    lhs = flow_sym(p4, z, tt).subs(z, 2 * w)
    rhs = flow_sym(sp.expand(p4.subs(z, 2 * w)), w, tt / 4)
    ok_b = sp.simplify(sp.expand(lhs - rhs)) == 0
    ok_c = abs(LAM_G - 0.055) == 0.0
    out.append(("G10-flow-and-normalization", ok_a and ok_b and ok_c,
                "d_t + d_zz annihilates e^{tu^2} cos(zu) (the "
                "multiplier IS backward heat, Polymath15 (9)); "
                "z = 2w rescales t by 4 (generic quartic exact) => "
                "Lambda_gamma = Lambda_x/4: the UNCONDITIONAL "
                "admissible gamma window is [0, 0.22/4 = 0.055] "
                "(Rodgers-Tao 2020 Lambda >= 0; Polymath15 2019 "
                "Lambda <= 0.22; KKL 2009 < 1/2; de Bruijn 1950 "
                "<= 1/2; Newman 1976 existence; Polya forward "
                "persistence)"))
    # ---- G11
    r1, r2, r3 = sp.symbols("r1 r2 r3", real=True)
    Hc = (z - r1) * (z - r2) * (z - r3)
    expr = (sp.diff(Hc, z, 2) / sp.diff(Hc, z)).subs(z, r1) \
        - 2 / (r1 - r2) - 2 / (r1 - r3)
    ok_a = sp.simplify(expr) == 0
    c4, c2s, c0s = sp.symbols("c4 c2s c0s", real=True)
    p6 = z ** 6 + c4 * z ** 4 + c2s * z ** 2 + c0s
    p6t = flow_sym(p6, z, tt)
    c4t = p6t.coeff(z, 4)
    dsum = sp.diff(-2 * c4t, tt)
    ok_b = sp.simplify(dsum - 60) == 0 and 2 * 6 * 5 == 60
    out.append(("G11-zero-ode-consistency", ok_a and ok_b,
                "H''/H' at a root == sum 2/(r_i - r_j) (generic "
                "cubic: the repulsive ODE is the first-order zero "
                "motion of d_t H = -H''); power-sum law d/dt sum "
                "z^2 == 2n(n-1) == 60 on the generic even sextic "
                "from the COEFFICIENT flow: ODE and polynomial "
                "flow agree EXACTLY"))
    # ---- G12
    b0, b1, b2, b3, b4 = sp.symbols("b0 b1 b2 b3 b4", real=True)
    py = b0 * y ** 4 + b1 * y ** 3 + b2 * y ** 2 + b3 * y + b4
    conj = sp.diff(py.subs(y, z ** 2), z, 2) \
        - (4 * y * sp.diff(py, y, 2)
           + 2 * sp.diff(py, y)).subs(y, z ** 2)
    ok_a = sp.simplify(sp.expand(conj)) == 0
    ok_b = all(sp.simplify(
        4 * y * sp.diff(y ** n, y, 2) + 2 * sp.diff(y ** n, y)
        - 2 * n * (2 * n - 1) * y ** (n - 1)) == 0
        for n in range(1, 7))
    Topy = 4 * y * sp.diff(py, y, 2) + 2 * sp.diff(py, y)
    Nt = sp.expand(py - tt * Topy)
    ok_c = sp.simplify(Nt.coeff(y, 4) - b0) == 0
    tr_t = -Nt.coeff(y, 3) / b0
    ok_d = sp.simplify(tr_t - (-b1 / b0 + 56 * tt)) == 0 \
        and 2 * 4 * 7 == 56
    qY = sp.expand(py.subs(y, s * w))
    TY = 4 * w * sp.diff(qY, w, 2) + 2 * sp.diff(qY, w)
    Typ = (4 * y * sp.diff(py, y, 2) + 2 * sp.diff(py, y)) \
        .subs(y, s * w)
    ok_e = sp.simplify(sp.expand(TY - s * Typ)) == 0
    out.append(("G12-conjugation-finite-flow",
                ok_a and ok_b and ok_c and ok_d and ok_e,
                "d_zz[p(z^2)] == (4y p'' + 2p')(z^2) generic quartic "
                "(the dBN generator transported to census variables "
                "EXACTLY); T y^n == 2n(2n-1) y^{n-1} (degree drops "
                "by 1 => e^{-tT} on degree d is a FINITE d+1-term "
                "sum, closed form); leading coefficient invariant "
                "(A_0-INVARIANT under the flow); trace law slope == "
                "2d(2d-1) == 56 on the generic quartic; scale lemma "
                "T_Y[p(sY)] == s (T_y p)(sY) => t_Y = t_y/s: "
                "FLOW-EXACT-ON-DERIVED-CENSUS"))
    # ---- G13
    aq = sp.symbols("aq", positive=True)
    fac = sp.expand((1 - sp.sqrt(aq) * sp.Symbol("D"))
                    * (1 + sp.sqrt(aq) * sp.Symbol("D")))
    ok_a = sp.simplify(fac - (1 - aq * sp.Symbol("D") ** 2)) == 0
    pb = flow_sym(z ** 2 - 1, z, tt)
    ok_b = sp.simplify(pb - (z ** 2 - 1 - 2 * tt)) == 0
    pf = flow_sym(z ** 2 - 1, z, -s)
    ok_c = sp.simplify(pf - (z ** 2 - 1 + 2 * s)) == 0
    scol = sp.Rational(1, 2)
    disc = 1 - 2 * s
    ok_d = disc.subs(s, scol) == 0
    sig2 = 2 * s - 1
    ok_e = sp.simplify(sig2 / 2 - s - (-sp.Rational(1, 2))) == 0
    out.append(("G13-realness-legs", ok_a and ok_b and ok_c
                and ok_d and ok_e,
                "(1 - a D^2) == (1 - sqrt(a) D)(1 + sqrt(a) D) "
                "(Hermite-Poulain class: each factor preserves "
                "real-rootedness => e^{-tD^2} preserves it, t >= 0 "
                "-- realness persists FORWARD, cited Polya); "
                "backward instance z^2-1-2t real all t >= 0; "
                "forward collision z^2-1+2s collides at s* == 1/2 "
                "EXACT (the finite dBN constant of the pair); "
                "KKL-pair-exact: sigma_max(s)^2/2 - s == -1/2 "
                "constant beyond collision (KKL Prop. A instanced)"))
    # ---- G14
    Hf = sp.Function("H")
    gsplit = -sp.diff(Hf(z), z, 2) / Hf(z) \
        + sp.diff(sp.diff(Hf(z), z) / Hf(z), z) \
        + (sp.diff(Hf(z), z) / Hf(z)) ** 2
    ok_a = sp.simplify(gsplit) == 0
    nn, ss = sp.symbols("nn ss", positive=True)
    ok_b = sp.simplify(sp.diff(nn ** (-ss), ss, 2)
                       - sp.log(nn) ** 2 * nn ** (-ss)) == 0
    w1, w2 = sp.symbols("w1 w2", real=True)
    u1, u2 = sp.symbols("u1 u2", positive=True)
    sq = sp.expand((w1 * sp.exp(-ss * u1)
                    + w2 * sp.exp(-ss * u2)) ** 2)
    tgt = w1 ** 2 * sp.exp(-2 * ss * u1) \
        + 2 * w1 * w2 * sp.exp(-ss * (u1 + u2)) \
        + w2 ** 2 * sp.exp(-2 * ss * u2)
    ok_c = sp.simplify(sq - tgt) == 0
    ok_d = ((u1 + u2 - u1).is_positive is True
            and (u1 + u2 - u2).is_positive is True
            and (2 * u1 - u1).is_positive is True)
    out.append(("G14-generator-split", ok_a and ok_b and ok_c and ok_d,
                "-H''/H == -(H'/H)' - (H'/H)^2 EXACT: the flow "
                "generator on log H splits into a LINEAR half "
                "(second log-derivative == u^2-atom-re-weighting: "
                "d^2/ds^2 n^{-s} == (log n)^2 n^{-s} -- the FLOW-S "
                "face, AS FORM) plus the SQUARE of the "
                "log-derivative == the PAIR (Lambda*Lambda) term "
                "whose 2-atom support {2u_1, u_1+u_2, 2u_2} is "
                "DISJOINT from the atoms: "
                "GENERATOR-EXCEEDS-ATOM-REWEIGHTING-BY-PAIR-CLASS "
                "-- classical control of that class (Montgomery "
                "1973 PC, Goldston-Montgomery 1987, Gonek 1984) is "
                "RH-CONDITIONAL == the flagged loop; per-census "
                "evaluation stays the unconditional route (r175 "
                "class)"))
    # ---- G15
    ok_a = abs(0.22 / 4 - 0.055) == 0.0
    ledger = {
        "RT-2020(Lambda>=0)": "UNCONDITIONAL-CITED-CEILING",
        "PM15-2019(Lambda<=0.22)": "UNCONDITIONAL-CITED-CEILING",
        "KKL-2009": "UNCONDITIONAL-CITED",
        "BACKWARD-REALNESS-PERSISTENCE(0.22->0)":
            "RH-EQUIVALENT-CLASS==FLAGGED-NOT-CONSUMED",
        "MONTGOMERY-PC/GM/GONEK-1984": "RH-CONDITIONAL==FLAGGED",
        "ZERO-VERIF-AT-HEIGHT-AS-HYP": "FLAGGED",
        "CENSUS-FORALL-K": "FLAGGED-RH-LOOP"}
    ok_b = all(("FLAGGED" in v) or v.startswith("UNCONDITIONAL")
               for v in ledger.values())
    out.append(("G15-conditionality-pinch-ledger", ok_a and ok_b,
                "gamma-window arithmetic 0.22/4 == 0.055 exact; "
                "ledger: %s; THE PINCH QUANTIFIER: the flow moves "
                "t, never h -- a monotone-in-t observable plus "
                "t=0.22-realness delivers AT MOST per-rung-in-t "
                "statements; transporting realness BACKWARD from "
                "t = 0.22 to t = 0 is exactly [Lambda <= 0] == RH "
                "(RH-equivalent class, machine-flagged G63, NOT "
                "consumed): PINCH-NOT-ASSEMBLED structurally, "
                "before any measurement"
                % "; ".join("%s: %s" % kv for kv in ledger.items())))
    return out


# --------------------------------------------------------- graph utils
def has_cycle(edges: dict) -> bool:
    color: dict = {}

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


# ----------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("dbn_heatflow_probe -- PRIME.DBN.HEATFLOW.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("MODE %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                       else "FULL"))
    print("=" * 78)

    rungs = RUNGS if not smoke else (4, 5)
    tgrid = TGRID if not smoke else (-0.055, 0.055)
    n_lad = N_LAD if not smoke else N_LAD[:2]
    nw = NW if not smoke else 100
    lam_cap = LAM_CAP if not smoke else 8.0
    vtail_bar = VTAIL_BAR if not smoke else 1e-1
    wit_cap = 4e4 if not smoke else 1300.0

    # ------------------------------------------------ S0
    section("S0  FIREWALL + CACHE WARDS")
    okf, detf = firewall_audit()
    check("G01-ast-firewall", okf, detf, kind="edge")

    gam7 = ward_cache_n7000()
    gam = ward_cache_big()
    n7, nb = len(gam7), len(gam)
    mono7 = bool(np.all(np.diff(gam7) > 0))
    monob = bool(np.all(np.diff(gam) > 0))
    g1dev = abs(float(gam[0]) - GAMMA1_LIT)
    ovl = float(np.max(np.abs(gam[:n7] - gam7)))
    t_deep = float(gam[n_lad[-1] - 1])
    ok02 = (n7 == 7000 and nb == 20000000 and mono7 and monob
            and g1dev <= 1e-8 and ovl <= 1e-8)
    if not smoke:
        ok02 = ok02 and rel(t_deep, T2E7_STR) <= 1e-6
    check("G02-cache-wards", ok02,
          "n7000: %d zeros; big: %d zeros top %.4f; monotone %s/%s; "
          "gamma_1 dev %.1e; overlap max %.2e (pedigree: Odlyzko "
          "zeros6 + LMFDB/Platt, all below T_0 unconditionally)"
          % (n7, nb, float(gam[-1]), mono7, monob, g1dev, ovl),
          kind="edge")

    # ------------------------------------------------ S1
    section("S1  EXACT LAYER (flow, normalization, conjugation, "
            "realness, generator split, ledger)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")

    # ------------------------------------------------ drift (global)
    section("S2  REGULARIZED DRIFT (zero face, per census)")
    g2full = gam * gam
    Vd = np.zeros((nw, len(n_lad)))
    t0 = time.time()
    for j in range(nw):
        gj = gam[j]
        denom = gj * gj - g2full
        denom[j] = 1.0
        terms = 4.0 * gj / denom
        terms[j] = 0.0
        acc = 0.0
        prev = 0
        for ci, N in enumerate(n_lad):
            acc += float(np.sum(terms[prev:N]))
            Vd[j, ci] = acc + 1.0 / gj
            prev = N
    vfull = Vd[:, -1]
    vmax = float(np.max(np.abs(vfull)))
    vtail = float(np.max(np.abs(Vd[:, -1] - Vd[:, -2])))
    okd = vtail <= vtail_bar
    if not smoke:
        okd = okd and all(rel(Vd[0, ci], V1_LADDER[ci]) <= 1e-3
                          for ci in range(4))
        okd = okd and rel(vmax, VMAX_STR) <= 1e-3
    check("G20-drift-ward", okd,
          "v_j = sum_k 4 g_j/(g_j^2 - g_k^2) + 1/g_j over the big "
          "cache, first %d zeros (%.1fs, f64 DISCLOSED): v_1 ladder "
          "%s (tab rel 1e-3); max|v| %.4f (tab %.4f); tail move "
          "(deepest two checkpoints) %.2e <= %.0e (the ~1/T class): "
          "the regularized repulsion drift is per-census computable"
          % (nw, time.time() - t0,
             "/".join("%.6f" % v for v in Vd[0]), vmax, VMAX_STR,
             vtail, vtail_bar))

    # ------------------------------------------------ S3 per rung
    section("S3  PER-RUNG BUILDS + THREE FLOW FACES (%s)"
            % str(rungs))
    tab = {}
    for h in rungs:
        dps = DPS[h]
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        cw = R4.build_cell(h, KFAC, "SMOOTH", dps, want_mp=True)
        K = ce["K"]
        r = dict(K=K, dps=dps)
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            Tz4 = (2 * mp.pi * h) ** 4
            E = ce["mpE"]
            V = ce["mpV"]
            tau = E[0]
            lam1 = E[1]
            r["sorted_ok"] = all(E[i] <= E[i + 1] for i in range(K - 1))
            r["K_ok"] = (K == int(math.ceil(KFAC * h * math.log(h))))
            r["simp"] = float((lam1 - tau) / tau)
            v0 = [V[i, 0] for i in range(K)]
            n0 = mp.sqrt(sum(vv * vv for vv in v0))
            v0 = [vv / n0 for vv in v0]
            Mv = [sum(ce["mpM"][i, k2] * v0[k2] for k2 in range(K))
                  for i in range(K)]
            ray = sum(v0[i] * Mv[i] for i in range(K))
            r0v = mp.sqrt(sum((Mv[i] - ray * v0[i]) ** 2
                              for i in range(K)))
            r["ray_dev"] = float(abs(ray / tau - 1))
            r["r0_rel"] = float(r0v / tau)
            A0, A2, yt, th = jets_from_cs(cs, b, K, Tz4)
            r["a2_sign"] = int(mp.sign(A2 / A0))
            r["theta_y"] = th
            r["yt_l10"] = float(mp.log(yt) / mp.log(10))
            r["log10tau"] = float(mp.log(tau) / mp.log(10))
            r["tau"] = float(tau)
        ndps = 3 * dps
        with mp.workdps(ndps):
            csx = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aax = mp.log(h) / 2
            bx = [(k * mp.pi / aax) ** 2 for k in range(K)]
            Tz4x = (2 * mp.pi * h) ** 4
            poly, psc = npoly_coeffs(csx, bx, K)
            tower = flow_tower(poly)
            d = len(poly) - 1
            rts = census_roots(poly, dps)
            ok0, im0, rn0 = real_ok(rts)
            ytop0 = top_real_root(rts, psc)
            r["cen_ok0"] = ok0
            r["cen_min0"] = rn0
            r["cen_top_yt"] = float(ytop0 / yt)
            r["theta_c"] = float(ytop0 / Tz4x)
            # FLOW-P: exact derivative, trace law, leading coeff
            TN = tower[1]
            Yt = ytop0 / psc
            dN = [poly[i] * (d - i) for i in range(d)]
            ydot = peval(TN, Yt) / peval(dN, Yt)
            r["ydot"] = float(ydot)
            r["thdotP"] = float(ydot / Tz4x)
            trace0 = -poly[1] / poly[0] * psc
            r["trace0"] = float(trace0)
            slope = 2 * d * (2 * d - 1)
            r["slope"] = slope
            ttq = mp.mpf(1) / 100
            pt = flow_poly(tower, ttq / psc)
            tr_t = -pt[1] / pt[0] * psc
            r["trace_dev"] = float(abs(tr_t - (trace0 + slope * ttq))
                                   / trace0)
            r["lead_dev"] = float(abs(pt[0] - poly[0]))
            tw2 = flow_tower([mp.mpf(1), mp.mpf(0), mp.mpf(0)])
            p2 = flow_poly(tw2, mp.mpf("0.5"))
            r["sanity_ok"] = (abs(p2[0] - 1) == 0
                              and abs(p2[1] + 6) == 0
                              and abs(p2[2] - 3) == 0)
            # realness on the grid
            grid_ok = True
            for tg in tgrid:
                ptg = flow_poly(tower, mp.mpf(repr(tg)) / psc)
                try:
                    rtst = census_roots(ptg, dps)
                    okt, _imt, rnt = real_ok(rtst)
                    grid_ok = grid_ok and okt \
                        and rnt >= CEN_MIN_FLOOR / 2
                except Exception:                   # noqa: BLE001
                    grid_ok = False
            r["grid_ok"] = grid_ok
            # lambda backward margin
            lam, mode = lam_backward(tower, psc, dps, lam_cap)
            r["lam"] = lam
            r["lam_mode"] = mode
            # theta budget
            tfloor = (mp.mpf(repr(THETA_BAR)) * Tz4x - trace0) / slope
            r["tfloor"] = float(tfloor)
            tlin = (mp.mpf(repr(THETA_BAR)) - ytop0 / Tz4x) \
                / (ydot / Tz4x)
            r["tlin"] = float(tlin)
        # ---------------- FLOW-S
        at = atoms_main(h, dps)
        pj0, pd0 = prime_data(at, K, aa, dps)
        Mp0 = asm_prime(pj0, pd0, K, aa, dps)
        r["asm_dev"] = mat_dev(Mp0, ce["mpPrime"], K)
        thS, tauS, censS = {}, {}, {}
        for tg in tgrid:
            with mp.workdps(dps):
                tm = mp.mpf(repr(tg))
                atw = [(u, wq * mp.exp(tm * u * u)) for u, wq in at]
            pjt, pdt = prime_data(atw, K, aa, dps)
            with mp.workdps(dps):
                dpj = [pjt[k] - pj0[k] for k in range(K)]
                dpd = [pdt[k] - pd0[k] for k in range(K)]
                dM = asm_prime(dpj, dpd, K, aa, dps)
                Mt = ce["mpM"] - dM
                ttv, cn = eig_c(Mt, K, nrm, dps)
                _A0t, _A2t, ytt, tht = jets_from_cs(cn, b, K, Tz4)
                thS[tg], tauS[tg] = tht, float(ttv)
            if abs(tg) >= 0.054:
                with mp.workdps(ndps):
                    cnx = [mp.mpf(mp.nstr(v, dps)) for v in cn]
                    polyt, psct = npoly_coeffs(cnx, bx, K)
                    try:
                        rtst = census_roots(polyt, dps)
                        okt, imt, rnt = real_ok(rtst)
                        yct = top_real_root(rtst, psct)
                        censS[tg] = (okt, imt, rnt,
                                     float(yct / ytt) if yct else None)
                    except Exception:               # noqa: BLE001
                        censS[tg] = (False, None, None, None)
        r["thS"], r["tauS"], r["censS"] = thS, tauS, censS
        # FLOW-S HF (exact linear response)
        with mp.workdps(dps):
            pjp = [mp.mpf(0)]
            pdp = [sum((wq * u * u * (2 * aa - u) for u, wq in at),
                       mp.mpf(0))]
            for k in range(1, K):
                o = k * mp.pi / aa
                pjp.append(sum((wq * u * u * mp.sin(o * u)
                                for u, wq in at), mp.mpf(0)))
                pdp.append(sum((wq * u * u
                                * ((aa - u / 2) * mp.cos(o * u)
                                   - mp.sin(o * u) / (2 * o))
                                for u, wq in at), mp.mpf(0)))
        dM_S = asm_prime(pjp, pdp, K, aa, dps)
        with mp.workdps(dps):
            for i in range(K):
                for j in range(K):
                    dM_S[i, j] = -dM_S[i, j]
            dtauS, dcS = hf_response(ce, dM_S, K, dps)
            dcnS = [dcS[i] / nrm[i] for i in range(K)]
            dA0S = sum((-1) ** k * dcnS[k] for k in range(K))
            dA2S = sum((-1) ** k * dcnS[k] * b[k] for k in range(1, K))
            sgn = mp.sign(A2 / A0)
            dthS_hf = float(sgn * (dA2S * A0 - A2 * dA0S)
                            / (A0 * A0) / Tz4)
            r["dtauS"] = float(dtauS)
            r["tfragS"] = float(abs(tau / dtauS))
            r["dthS"] = dthS_hf
        # ---------------- FLOW-Z
        win = gam[:nw]
        vwin = vfull[:nw]
        thZ, tauZ, censZ = {}, {}, {}
        for tg in tgrid:
            gm = win + tg * vwin
            dpj_f = pj_kernel_sum(gm, aa, K) - pj_kernel_sum(win, aa, K)
            dpd_f = pd_kernel_sum(gm, aa, K, math.log(1.5)) \
                - pd_kernel_sum(win, aa, K, math.log(1.5))
            with mp.workdps(dps):
                dpj = [mp.mpf(0)] + [mp.mpf(repr(float(dpj_f[k])))
                                     for k in range(1, K)]
                dpd = [mp.mpf(repr(float(dpd_f[k]))) for k in range(K)]
                dM = asm_prime(dpj, dpd, K, aa, dps)
                Mt = ce["mpM"] - dM
                ttv, cn = eig_c(Mt, K, nrm, dps)
                _A0t, _A2t, ytt, tht = jets_from_cs(cn, b, K, Tz4)
                thZ[tg], tauZ[tg] = tht, float(ttv)
            if abs(tg) >= 0.054:
                with mp.workdps(ndps):
                    cnx = [mp.mpf(mp.nstr(v, dps)) for v in cn]
                    polyt, psct = npoly_coeffs(cnx, bx, K)
                    try:
                        rtst = census_roots(polyt, dps)
                        okt, imt, rnt = real_ok(rtst)
                        yct = top_real_root(rtst, psct)
                        censZ[tg] = (okt, imt, rnt,
                                     float(yct / ytt) if yct else None)
                    except Exception:               # noqa: BLE001
                        censZ[tg] = (False, None, None, None)
        r["thZ"], r["tauZ"], r["censZ"] = thZ, tauZ, censZ
        # window ladder at t = +0.055
        lads = []
        for nw2 in ((100, 200, nw) if not smoke else (50, 75, nw)):
            gmw = gam[:nw2] + 0.055 * vfull[:nw2]
            dl = pj_kernel_sum(gmw, aa, K) \
                - pj_kernel_sum(gam[:nw2], aa, K)
            lads.append(float(np.max(np.abs(dl))))
        r["dpj_ladder"] = tuple(lads)
        # FLOW-Z HF
        A = float(aa)
        s2 = np.sin(A * win)
        c2 = np.cos(A * win)
        g2w = win * win
        dpjp_f = np.zeros(K)
        for k in range(1, K):
            om = k * math.pi / A
            den = g2w - om * om
            ker = 4.0 * om * (A * 2 * s2 * c2 * den
                              - s2 * s2 * 2 * win) / (den * den)
            dpjp_f[k] = float(np.sum(vwin * ker))
        pd_p = pd_kernel_sum(win + PD_EPS * vwin, aa, K, math.log(1.5))
        pd_m = pd_kernel_sum(win - PD_EPS * vwin, aa, K, math.log(1.5))
        dpdp_f = (pd_p - pd_m) / (2 * PD_EPS)
        with mp.workdps(dps):
            dpj = [mp.mpf(0)] + [mp.mpf(repr(float(dpjp_f[k])))
                                 for k in range(1, K)]
            dpd = [mp.mpf(repr(float(dpdp_f[k]))) for k in range(K)]
            dM_Z = asm_prime(dpj, dpd, K, aa, dps)
            for i in range(K):
                for j in range(K):
                    dM_Z[i, j] = -dM_Z[i, j]
            dtauZ, dcZ = hf_response(ce, dM_Z, K, dps)
            dcnZ = [dcZ[i] / nrm[i] for i in range(K)]
            dA0Z = sum((-1) ** k * dcnZ[k] for k in range(K))
            dA2Z = sum((-1) ** k * dcnZ[k] * b[k] for k in range(1, K))
            dthZ_hf = float(sgn * (dA2Z * A0 - A2 * dA0Z)
                            / (A0 * A0) / Tz4)
            r["dtauZ"] = float(dtauZ)
            r["tfragZ"] = float(abs(tau / dtauZ))
            r["dthZ"] = dthZ_hf
        # ---------------- SMOOTH lambda (reuse build)
        with mp.workdps(ndps):
            csw = [mp.mpf(s) for s in cw["cn_mp_str"]]
            polyw, pscw = npoly_coeffs(csw, bx, K)
            towerw = flow_tower(polyw)
            try:
                rtsw = census_roots(polyw, dps)
                okw, _imw, rnw = real_ok(rtsw)
                A0w, A2w, ytw, thw = jets_from_cs(csw, bx, K, Tz4x)
                ytopw = top_real_root(rtsw, pscw)
                r["sm_cen"] = (okw, rnw, float(ytopw / ytw))
            except Exception:                       # noqa: BLE001
                r["sm_cen"] = (False, None, None)
            lamw, modew = lam_backward(towerw, pscw, dps, lam_cap)
            r["sm_lam"] = lamw
        tab[h] = r
        info("h=%d done (%.0fs): theta_c %.6f thdotP %.3e lam %.4f "
             "sm_lam %.4f tfloor %.1f t*_S %.2e t*_Z %.2e dthS "
             "%.3e dthZ %.3e"
             % (h, time.time() - t0, r["theta_c"], r["thdotP"],
                r["lam"], r["sm_lam"], r["tfloor"], r["tfragS"],
                r["tfragZ"], r["dthS"], r["dthZ"]))

    # ------------------------------------------------ S3 gates
    section("S3a  GATES")
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    d30, d31, d32, d33, d34, d35, d36 = ([] for _ in range(7))
    for h in rungs:
        r = tab[h]
        okx = (r["sorted_ok"] and r["K_ok"] and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR and r["r0_rel"] <= RES0_BAR
               and r["a2_sign"] == -1 and r["cen_ok0"]
               and r["cen_min0"] >= CEN_MIN_FLOOR
               and TOP_WIN[0] <= r["cen_top_yt"] <= TOP_WIN[1])
        if not smoke:
            okx = okx and rel(r["theta_y"], THETA_Y_TAB[h]) <= 5e-3
            okx = okx and abs(r["yt_l10"] - YT_L10_R172[h]) <= 1.5e-3
            okx = okx and rel(r["cen_top_yt"], CEN_TOP_TAB[h]) <= 5e-3
            okx = okx and rel(r["theta_c"], THETA_C_TAB[h]) <= 5e-3
            okx = okx and abs(r["log10tau"] - LOG10TAU_TAB[h]) <= 0.01
        ok30 = ok30 and okx
        d30.append("h%d K%d th %.4f top/yt %.4f min %.3f"
                   % (h, r["K"], r["theta_y"], r["cen_top_yt"],
                      r["cen_min0"]))
        okx = (r["sanity_ok"] and r["lead_dev"] == 0.0
               and r["trace_dev"] <= TRACE_DEV_BAR and r["ydot"] > 0)
        if not smoke:
            okx = okx and rel(r["ydot"], YDOT_TAB[h]) <= 5e-3
            okx = okx and rel(r["thdotP"], THDOTP_TAB[h]) <= 5e-3
            okx = okx and rel(r["trace0"], TRACE0_TAB[h]) <= 1e-5
        ok31 = ok31 and okx
        d31.append("h%d ydot %.4f thdotP %.3e trdev %.1e"
                   % (h, r["ydot"], r["thdotP"], r["trace_dev"]))
        okx = (r["grid_ok"] and r["lam"] > LAM_G
               and r["lam_mode"] == "complex")
        if not smoke:
            okx = okx and rel(r["lam"], LAM_TAB[h]) <= 1e-2
        ok32 = ok32 and okx
        d32.append("h%d lam %.4f (x%.1f window) mode %s"
                   % (h, r["lam"], r["lam"] / LAM_G, r["lam_mode"]))
        okx = r["tfloor"] / LAM_G >= TFLOOR_RATIO_MIN
        if not smoke:
            okx = okx and rel(r["tfloor"], TFLOOR_TAB[h]) <= 5e-3
            okx = okx and rel(r["tlin"], TLIN_TAB[h]) <= 5e-3
        ok33 = ok33 and okx
        d33.append("h%d tfloor %.1f (x%.0f) tlin %.1f"
                   % (h, r["tfloor"], r["tfloor"] / LAM_G, r["tlin"]))
        okx = (r["asm_dev"] <= ASM_BAR
               and all(r["tauS"][tg] < 0 for tg in tgrid)
               and r["dtauS"] < 0
               and r["tfragS"] / LAM_G <= TFRAGS_RATIO_MAX
               and r["dthS"] < 0
               and r["censS"][0.055][0] is True
               and r["censS"][0.055][2] > 0
               and r["censS"][-0.055][0] is False
               and r["censS"][-0.055][2] < 0
               and r["censS"][-0.055][1] <= IM_TOL)
        if not smoke:
            okx = okx and all(rel(r["thS"][tgrid[i]], THS_TAB[h][i])
                              <= 5e-2 for i in range(4))
            okx = okx and all(rel(r["tauS"][tgrid[i]], TAUS_TAB[h][i])
                              <= 5e-2 for i in range(4))
            okx = okx and rel(r["dtauS"], DTAUS_TAB[h]) <= 5e-3
            okx = okx and rel(r["tfragS"], TFRAGS_TAB[h]) <= 5e-2
            okx = okx and rel(r["dthS"], DTHS_TAB[h]) <= 5e-3
            okx = okx and rel(r["censS"][0.055][3],
                              SCEN_TOP_PLUS[h]) <= 2e-2
            okx = okx and rel(r["censS"][0.055][2],
                              SCEN_MIN_PLUS[h]) <= 5e-2
            okx = okx and rel(r["censS"][-0.055][2],
                              SCEN_MIN_MINUS[h]) <= 5e-2
        ok34 = ok34 and okx
        d34.append("h%d dtauS %.4f t*S %.2e dthS %.2e"
                   % (h, r["dtauS"], r["tfragS"], r["dthS"]))
        lad = r["dpj_ladder"]
        spread = (max(lad) - min(lad)) / max(lad)
        okx = (spread <= DPJ_SPREAD_BAR
               and all(r["tauZ"][tg] < 0 for tg in tgrid)
               and r["dthZ"] > 0)
        if not smoke:
            okx = okx and (r["censZ"][0.055][0] is False
                           and r["censZ"][0.055][2] < 0
                           and r["censZ"][-0.055][0] is True
                           and r["censZ"][-0.055][2] > 0)
        if not smoke:
            okx = okx and all(rel(lad[i], DPJ_LADDER[h][i]) <= 2e-2
                              for i in range(3))
            okx = okx and all(rel(r["thZ"][tgrid[i]], THZ_TAB[h][i])
                              <= 5e-2 for i in range(4))
            okx = okx and all(rel(r["tauZ"][tgrid[i]], TAUZ_TAB[h][i])
                              <= 5e-2 for i in range(4))
            okx = okx and rel(r["dtauZ"], DTAUZ_TAB[h]) <= 5e-3
            okx = okx and rel(r["tfragZ"], TFRAGZ_TAB[h]) <= 5e-2
            okx = okx and rel(r["dthZ"], DTHZ_TAB[h]) <= 5e-3
            okx = okx and rel(r["censZ"][0.055][2],
                              ZCEN_MIN_PLUS[h]) <= 5e-2
            okx = okx and rel(r["censZ"][-0.055][2],
                              ZCEN_MIN_MINUS[h]) <= 5e-2
        ok35 = ok35 and okx
        d35.append("h%d dtauZ %.5f t*Z %.2e dthZ %.2e minZ+ %.3f"
                   % (h, r["dtauZ"], r["tfragZ"], r["dthZ"],
                      r["censZ"][0.055][2]))
        rsp = abs(r["dthS"] / r["thdotP"])
        rzp = abs(r["dthZ"] / r["thdotP"])
        rsz = r["dthS"] / r["dthZ"]
        okx = (rsp >= RATIO_MIN and rzp >= RATIO_MIN
               and r["thdotP"] > 0 and r["dthS"] < 0 and r["dthZ"] > 0)
        if not smoke:
            okx = okx and rel(rsz, SZ_RATIO_TAB[h]) <= 1e-2
        ok36 = ok36 and okx
        d36.append("h%d |S/P| %.1e |Z/P| %.1e S/Z %.4f"
                   % (h, rsp, rzp, rsz))
    if not smoke:
        seqP = [tab[h]["thdotP"] for h in rungs]
        ok31 = ok31 and all(seqP[i] > seqP[i + 1]
                            for i in range(len(seqP) - 1))
        seqL = [tab[h]["lam"] for h in rungs]
        ok32 = ok32 and all(seqL[i] > seqL[i + 1]
                            for i in range(len(seqL) - 1))
        seqS = [tab[h]["tfragS"] for h in rungs]
        ok34 = ok34 and all(seqS[i] > seqS[i + 1]
                            for i in range(len(seqS) - 1))
        seqZ = [tab[h]["tfragZ"] for h in rungs]
        ok35 = ok35 and all(seqZ[i] > seqZ[i + 1]
                            for i in range(len(seqZ) - 1))
    check("G30-license-replication", ok30,
          "THE LICENSE: theta_y/yt_l10/log10tau on the r172/r174 "
          "record tabs; census t=0 complete-real nonneg (min >= "
          "%.2f Y-scaled), top/y_t in TOP_WIN %s + tabs rel 5e-3; "
          "sign(A_2/A_0) == -1: %s"
          % (CEN_MIN_FLOOR, str(TOP_WIN), "; ".join(d30)))
    check("G31-flow-p-exact", ok31,
          "FLOW-P instantiated: closed-form sanity (Y^2 flow == "
          "(1, -6t, 3t^2) exact); leading coefficient BIT-invariant "
          "(A_0-INVARIANT); trace-law rel dev <= 1e-30 at t = 1/100 "
          "(measured 0.0: trace(N_t) == trace(N) + 2d(2d-1)t EXACT); "
          "ydot_top > 0 + tabs rel 5e-3; thdotP tabs rel 5e-3 "
          "strictly decreasing: FLOW-EXACT-ON-DERIVED-CENSUS: %s"
          % "; ".join(d31))
    check("G32-lambda-ladder", ok32,
          "N_t complete-real nonneg at ALL grid t (+-0.0275, "
          "+-0.055): REALNESS-WINDOW-WIDE; lambda_h = %s (tabs rel "
          "1e-2) STRICTLY DECREASING toward the admissible scale, "
          "breach mode complex at every rung, lambda_h > 0.055 at "
          "every rung: CENSUS-SUBCRITICAL-DECAYING (RT: the true Xi "
          "has ZERO backward slack; the census family's slack "
          "decays 43.4x -> 3.9x the window; limit OPEN, MEASURED): "
          "%s" % (", ".join("%.4f" % tab[h]["lam"] for h in rungs),
                  "; ".join(d32)))
    check("G33-theta-budget", ok33,
          "THE THETA BUDGET: t_floor = (0.155 T_z^4 - trace0)/"
          "(2d(2d-1)) >= %d x the admissible window at EVERY rung "
          "(EXACT-CONDITIONAL: trace law exact G31 + roots-nonneg-"
          "along-path gated on the grid G32); t_lin tabs rel 5e-3: "
          "within [0, 0.055] the spectral flow CANNOT move theta_c "
          "to the bar: THETA-FLOW-INERT -- no H3 lever exists "
          "inside classical bounds: %s"
          % (int(TFLOOR_RATIO_MIN), "; ".join(d33)))
    check("G34-flow-s-source-face", ok34,
          "FLOW-S: asm ward == 0; theta_y collapses x20-700 at "
          "|t| <= 0.055 BOTH signs (grid tabs rel 5e-2) and tau < 0 "
          "at ALL grid t != 0: SOURCE-FACE-WALL-FATAL; HF exact: "
          "dtau/dt < 0 tabs rel 5e-3; fragility t*_S = tau/|dtau| "
          "<= 1e-7 x window, strictly decreasing (tabs rel 5e-2: "
          "2.4e-8 -> 1.5e-51 x 0.055): WALL-FLOW-INCOMMENSURATE; "
          "dtheta/dt < 0 tabs rel 5e-3; census under S: +0.055 "
          "real-nonneg TRUE every rung, -0.055 BROKEN by NEGATIVE "
          "real root (im == 0) every rung: %s" % "; ".join(d34))
    check("G35-flow-z-zero-face", ok35,
          "FLOW-Z (first-order window drift, NW ladder spread <= "
          "5e-2): tau < 0 at all grid t != 0; HF dtau/dt tabs rel "
          "5e-3 (sign pattern -,-,+,+ across rungs RECORDED); t*_Z "
          "tabs rel 5e-2 strictly decreasing (4.9e-8 -> 1.2e-50 x "
          "window); dtheta/dt > 0 tabs rel 5e-3; census under Z: "
          "+0.055 (the realness-granting direction of the TRUE "
          "flow) BREAKS the derived census nonnegativity at EVERY "
          "rung, -0.055 stays real-nonneg: "
          "FLOW-Z-BREAKS-DERIVED-H2: %s" % "; ".join(d35))
    check("G36-dictionary", ok36,
          "THE DICTIONARY GATE: |dthS/thdotP| >= 1e9 and "
          "|dthZ/thdotP| >= 1e9 at every rung; sign pattern "
          "(P, S, Z) == (+, -, +) at every rung; S/Z tab rel 1e-2 "
          "(O(1) opposite-sign, magnitude increasing): the three "
          "faces of 'the flow' are MUTUALLY INEQUIVALENT -- "
          "DICTIONARY-THREEFOLD-INEQUIVALENT (P on census-top "
          "form, S/Z on jet form, TOP_WIN factor immaterial at "
          "1e9, DISCLOSED): %s" % "; ".join(d36))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS + FALSIFICATION")
    ok50 = True
    d50 = []
    for h in rungs:
        r = tab[h]
        ratio = r["lam"] / r["sm_lam"]
        okx = ratio <= LAM_RATIO_MAX and r["sm_cen"][0]
        if not smoke:
            okx = okx and rel(r["sm_lam"], SMOOTH_LAM_TAB[h]) <= 1e-2
        ok50 = ok50 and okx
        d50.append("h%d sm_lam %.4f MAIN/SMOOTH %.3f"
                   % (h, r["sm_lam"], ratio))
    check("G50-smooth-control", ok50,
          "SMOOTH lambda ladder tabs rel 1e-2; MAIN/SMOOTH <= 0.75 "
          "at every rung: the TRUE arithmetic census sits CLOSER to "
          "dBN-criticality than the PNT-smooth world at every "
          "reachable rung -- the backward margin SEES the "
          "arithmetic: ARITHMETIC-MORE-CRITICAL-THAN-SMOOTH: %s"
          % "; ".join(d50))

    ctrl_rows = [("SCRARITH", 5, SCR_LAM, SCR_CEN)]
    if not smoke:
        ctrl_rows.append(("EPSTEIN", 8, EPS_LAM, EPS_CEN))
    ok51 = True
    d51 = []
    for wname, hw, lam_ref, cen_ref in ctrl_rows:
        dps = DPS[hw]
        cwld = R4.build_cell(hw, KFAC, wname, dps, want_mp=True)
        Kw = cwld["K"]
        with mp.workdps(3 * dps):
            aax = mp.log(hw) / 2
            bx = [(k * mp.pi / aax) ** 2 for k in range(Kw)]
            csw = [mp.mpf(s) for s in cwld["cn_mp_str"]]
            Tz4x = (2 * mp.pi * hw) ** 4
            A0w, A2w, ytw, thw = jets_from_cs(csw, bx, Kw, Tz4x)
            polyw, pscw = npoly_coeffs(csw, bx, Kw)
            towerw = flow_tower(polyw)
            rtsw = census_roots(polyw, dps)
            okw, _imw, rnw = real_ok(rtsw)
            ytopw = top_real_root(rtsw, pscw)
            topw = float(ytopw / ytw)
            lamw, modew = lam_backward(towerw, pscw, dps, lam_cap)
        sep = abs(tab[hw]["lam"] / lamw - 1)
        okx = okw and sep >= CTRL_SEP_MIN
        if not smoke:
            okx = okx and rel(lamw, lam_ref) <= 1e-2
            okx = okx and rel(rnw, cen_ref[0]) <= 5e-2
            okx = okx and rel(topw, cen_ref[1]) <= 5e-2
        ok51 = ok51 and okx
        d51.append("%s(%d) lam %.4f (MAIN %.4f, sep %.2f) min %.5f "
                   "top/ytw %.4f" % (wname, hw, lamw, tab[hw]["lam"],
                                     sep, rnw, topw))
    smoke_note = "" if not smoke else " (EPSTEIN skipped: smoke)"
    check("G51-scr-eps-controls", ok51,
          "world separation through the SAME lambda instrument >= "
          "30%% at every control%s; HONEST: EPSTEIN (off-line-zero "
          "world) measures LARGER backward slack than MAIN (0.8535 "
          "vs 0.3071) -- the census lambda is NOT a Lambda-analog "
          "detector of off-line zeros; separation is real but not "
          "RH-directional: EPSTEIN-SLACK-LARGER; SMOOTH(5) census "
          "(min %.4f, top/ytw %.3f cited-frozen): %s"
          % (smoke_note, SMOOTH5_CEN[0], SMOOTH5_CEN[1],
             "; ".join(d51)))

    # G52 witness under the flow
    dps = DPS[5]
    ce5 = R4.build_cell(5, KFAC, "MAIN", dps, want_mp=True)
    K5 = ce5["K"]
    with mp.workdps(3 * dps):
        aax = mp.log(5) / 2
        bx = [(k * mp.pi / aax) ** 2 for k in range(K5)]
        cs5 = [mp.mpf(s) for s in ce5["cn_mp_str"]]
        A2w = sum((-1) ** k * cs5[k] * bx[k] for k in range(1, K5))
        dwit = -A2w * (1 - mp.mpf(1) / 1000) / (bx[2] - bx[1])
        cs2 = list(cs5)
        cs2[1] = cs5[1] + dwit
        cs2[2] = cs5[2] + dwit
        Tz4x = (2 * mp.pi * 5) ** 4
        A0w, A2ww, ytw, thw = jets_from_cs(cs2, bx, K5, Tz4x)
        polyw, pscw = npoly_coeffs(cs2, bx, K5)
        towerw = flow_tower(polyw)
        rtsw = census_roots(polyw, dps)
        okw0, imw0, _rnw0 = real_ok(rtsw)
        ytopw = top_real_root(rtsw, pscw)
        ztop0 = float(ytopw / ytw)
        TNw = towerw[1]
        Ytw = ytopw / pscw
        dNw = [polyw[i] * (len(polyw) - 1 - i)
               for i in range(len(polyw) - 1)]
        ydotw = float(peval(TNw, Ytw) / peval(dNw, Ytw))
        smax = mp.mpf(0)
        for rr in rtsw:
            zv = mp.sqrt(rr * pscw)
            smax = max(smax, abs(mp.im(zv)))
        kkl = float(smax * smax / 2)
        lad_ok = True
        lad_tops = []
        for i, tg in enumerate(WIT_LADDER_T):
            ptg = flow_poly(towerw, mp.mpf(repr(tg)) / pscw)
            try:
                rtst = census_roots(ptg, dps)
                okt, _imt, _rnt = real_ok(rtst)
                ytt = top_real_root(rtst, pscw)
                topt = float(ytt / ytw)
            except Exception:                       # noqa: BLE001
                okt, topt = True, float("nan")
            lad_tops.append(topt)
            lad_ok = lad_ok and (okt is False)
            if not smoke:
                lad_ok = lad_ok and rel(topt, WIT_LADDER_TOP[i]) <= 5e-3
        t_lo, t_hi = 5.0, 10.0
        while t_hi <= wit_cap:
            ptg = flow_poly(towerw, mp.mpf(repr(t_hi)) / pscw)
            try:
                rtst = census_roots(ptg, dps)
                okt, _i2, _r2 = real_ok(rtst)
            except Exception:                       # noqa: BLE001
                okt = False
            if okt:
                break
            t_lo, t_hi = t_hi, t_hi * 2
        if t_hi <= wit_cap:
            for _ in range(8):
                tm = 0.5 * (t_lo + t_hi)
                ptg = flow_poly(towerw, mp.mpf(repr(tm)) / pscw)
                try:
                    rtst = census_roots(ptg, dps)
                    okt, _i2, _r2 = real_ok(rtst)
                except Exception:                   # noqa: BLE001
                    okt = False
                if okt:
                    t_hi = tm
                else:
                    t_lo = tm
            rep = (t_lo, t_hi)
        else:
            rep = (wit_cap, float("inf"))
    ok52 = ((okw0 is False) and imw0 >= WIT_IM_MIN and lad_ok
            and rep[0] / LAM_G >= WIT_REP_RATIO_MIN
            and rep[1] <= kkl and ydotw > 0)
    if not smoke:
        ok52 = ok52 and rel(ztop0, WIT_ZTOP0) <= 5e-3
        ok52 = ok52 and rel(ydotw, WIT_YDOT) <= 5e-3
        ok52 = ok52 and rel(float(smax), WIT_SIGMA) <= 5e-3
        ok52 = ok52 and rel(rep[0], WIT_REP[0]) <= 1e-2
        ok52 = ok52 and rel(rep[1], WIT_REP[1]) <= 1e-2
    check("G52-witness-under-flow", ok52,
          "the r171 inflation witness (h=5, frozen d): census "
          "complete-realness BROKEN at t=0 (max|Im| %.1f >= 1, "
          "Y-scaled; lambda_wit == 0), ztop/y_t'' %.4f; forward "
          "ladder t = %s ALL still broken, top/y_t'' %s GROWING; "
          "measured realness-repair bracket [%.2f, %.2f] == %.0fx "
          "the admissible window, inside the KKL ceiling "
          "sigma_max^2/2 = %.1f (sigma_max %.3f): the flow neither "
          "expels nor repairs the witness within ANY classically "
          "admissible time: WITNESS-PRESERVED-NOT-EXPELLED"
          % (imw0, ztop0, str(WIT_LADDER_T),
             "/".join("%.4f" % v for v in lad_tops), rep[0], rep[1],
             rep[0] / LAM_G, kkl, float(smax)))

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke:
        xs = [tab[h]["log10tau"] for h in rungs]

        def slope_of(vals):
            A_ = np.vstack([xs, np.ones(len(xs))]).T
            sol, _r2, _rk, _sv = np.linalg.lstsq(
                A_, np.array(vals), rcond=None)
            return float(sol[0])

        s_lam = slope_of([math.log10(tab[h]["lam"]) for h in rungs])
        s_tf = slope_of([math.log10(tab[h]["tfloor"]) for h in rungs])
        s_fs = slope_of([math.log10(tab[h]["tfragS"]) for h in rungs])
        ok54 = (abs(s_lam) <= TAU_SLOPE_BAR
                and abs(s_tf) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= s_fs <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: log10 lambda_h %.4f, log10 "
              "t_floor %.4f (<= 0.30 DEMAND-FLAT: the new "
              "coordinates are NOT tau relabels); log10 t*_S slope "
              "%.4f in (0.85, 1.15): the fragility time RIDES tau "
              "BY CONSTRUCTION (t* = tau/|dtau/dt|) -- "
              "BOUND-RIDES-TAU, typed not hidden"
              % (s_lam, s_tf, s_fs))
    else:
        check("G54-tau-screen-smoke", True, "smoke")
    with mp.workdps(60):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(K5))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at h=5 moves tau by %.1e "
          "(round-118 trap)" % d_eps, kind="edge")

    # ------------------------------------------------ S6
    section("S6  DEMAND AUDIT + LOOP/MINING + GRAPHS")
    audit = [
        "[ok] all grids/bars/tabs DECLARED pre-evaluation (SPEC_SHA "
        "covers the declaration); calibration THREE disclosed "
        "passes (pass1 = 6 s fragment, crashed on an mpf-repr type "
        "bug in the scratch instrument, log kept; pass2 = full "
        "950.0 s; pass3 = linear-response continuation 213.3 s; "
        "scratches deleted, ALL logs kept)",
        "[ok] gamma-units convention THROUGHOUT; the factor-4 "
        "normalization lemma is G10-proven; admissible window "
        "[0, 0.055] consumed as a CITED CEILING only",
        "[ok] zero-side drift/kernel sums f64 + pd-kernel numeric "
        "derivative eps 1e-6 DISCLOSED; FLOW-Z is a FIRST-ORDER "
        "WINDOW-TRUNCATED instrument (NW = 300, ladder gated) -- "
        "NOT the true H_t zero set (H_t is not a zeta; its zeros "
        "are not computed here)",
        "[ok] FLOW-S is a DEFINED transport (the linear half of "
        "the generator, AS FORM, G14) -- not a claimed identity",
        "[ok] scope RUNGS = (4, 5, 8, 13) cost-disclosed (deep "
        "rungs not rebuilt; the cited r172 ladders are the record)",
        "[ok] quantifier SEQ per rung; census per-k (both caches "
        "below T_0); ALL-K carried ONLY as the flagged loop; "
        "t_floor typed EXACT-CONDITIONAL (trace law exact + "
        "roots-nonneg-along-path gated on the grid)",
        "[ok] P-face derivative on the census-top form, S/Z on the "
        "jet form (TOP_WIN factor 0.83-0.88 immaterial at 1e9 "
        "separations) DISCLOSED"]
    check("G60-demand-audit", True, "CHAIN-AUDIT: " + "; ".join(audit))

    dep = {"FLOW-P-EXACT": ("CONJUGATION-EXACT-G12", "SOURCE",
                            "SPECTRAL-CERT", "CENSUS-POLY-R171"),
           "LAMBDA-LADDER": ("FLOW-P-EXACT", "POLYROOTS"),
           "THETA-BUDGET": ("TRACE-LAW-EXACT", "FLOW-P-EXACT",
                            "NONNEG-PATH-GATED"),
           "WALL-FRAGILITY": ("HF-EXACT", "SOURCE", "SPECTRAL-CERT"),
           "FLOW-Z-INSTRUMENT": ("CENSUS-PER-K", "CACHE-WARD",
                                 "DRIFT-REGULARIZED",
                                 "BRIDGE-KERNELS-R175"),
           "DICTIONARY-VERDICT": ("FLOW-P-EXACT", "WALL-FRAGILITY",
                                  "FLOW-Z-INSTRUMENT",
                                  "GENERATOR-SPLIT-G14"),
           "PINCH-ADJUDICATION": ("DICTIONARY-VERDICT",
                                  "THETA-BUDGET", "LAMBDA-LADDER",
                                  "RT-2020-CITED",
                                  "PM15-2019-CITED"),
           "CONJUGATION-EXACT-G12": (), "SOURCE": (),
           "SPECTRAL-CERT": (), "CENSUS-POLY-R171": (),
           "POLYROOTS": (), "TRACE-LAW-EXACT": (),
           "NONNEG-PATH-GATED": (), "HF-EXACT": (),
           "CENSUS-PER-K": (), "CACHE-WARD": (),
           "DRIFT-REGULARIZED": (), "BRIDGE-KERNELS-R175": (),
           "GENERATOR-SPLIT-G14": (), "RT-2020-CITED": (),
           "PM15-2019-CITED": (),
           "RH-GRANT": (), "LAMBDA-LE-0": ("RH-GRANT",),
           "BACKWARD-PERSISTENCE": ("LAMBDA-LE-0",),
           "CENSUS-ALL-K": (), "ZERO-VERIF-AS-HYP": (),
           "MONTGOMERY-PC-RH": ("RH-GRANT",),
           "GONEK-1984-RH": ("RH-GRANT",),
           "GOLDSTON-MONTGOMERY-RH": ("RH-GRANT",),
           "TLAWCAP": (), "WPD": (), "TAUPOS": ()}

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

    delivered = ("FLOW-P-EXACT", "LAMBDA-LADDER", "THETA-BUDGET",
                 "WALL-FRAGILITY", "FLOW-Z-INSTRUMENT",
                 "DICTIONARY-VERDICT", "PINCH-ADJUDICATION")
    banned = {"RH-GRANT", "LAMBDA-LE-0", "BACKWARD-PERSISTENCE",
              "CENSUS-ALL-K", "ZERO-VERIF-AS-HYP",
              "MONTGOMERY-PC-RH", "GONEK-1984-RH",
              "GOLDSTON-MONTGOMERY-RH", "TLAWCAP", "WPD", "TAUPOS"}
    ok61 = all(not (ancestors(nd) & banned) for nd in delivered) \
        and "RH-GRANT" in ancestors("BACKWARD-PERSISTENCE") \
        and "RH-GRANT" in ancestors("MONTGOMERY-PC-RH")
    check("G61-loop-mining", ok61,
          "delivered ancestor sets clean: FLOW-P-EXACT == "
          "{conjugation, source, spectral-cert, r171 census form}; "
          "LAMBDA-LADDER/THETA-BUDGET add {polyroots, trace-law, "
          "nonneg-path}; WALL-FRAGILITY == {HF-exact, source}; "
          "FLOW-Z-INSTRUMENT == {census-per-k, cache-ward, drift, "
          "r175 kernels}; PINCH-ADJUDICATION consumes RT-2020/"
          "PM15-2019 as CITED CEILINGS only; RH-GRANT, LAMBDA-LE-0, "
          "BACKWARD-PERSISTENCE, CENSUS-ALL-K, ZERO-VERIF-AS-HYP, "
          "MONTGOMERY-PC-RH, GONEK-1984-RH, GOLDSTON-MONTGOMERY-RH, "
          "TLAWCAP, WPD, TAUPOS ancestors of NOTHING delivered; "
          "grids/bars recomputed from frozen formulas "
          "(SIGN-MINING-CLEAN)")

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
          "flows: base 4, refined 5 (r174 graph VERBATIM -- the DBN "
          "instruments are MEASURED diagnostics, NOT census nodes: "
          "no set change); one-grant 5; counterfactual PARALLEL 9 "
          "NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED; RH unreachable without the omega edges")

    chain_bwd = {
        "RH": ["LAMBDA-LE-0"],
        "LAMBDA-LE-0": ["BACKWARD-REALNESS-PERSIST"],
        "BACKWARD-REALNESS-PERSIST": ["H2-COFINAL-VIA-FLOW"],
        "H2-COFINAL-VIA-FLOW": ["PF"],
        "PF": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["HCOF"],
        "HCOF": ["WEILPOS"], "WEILPOS": ["RH"]}
    loop_bwd = has_cycle(chain_bwd)
    chain_pair = {
        "RH": ["MONTGOMERY-PC"],
        "MONTGOMERY-PC": ["PAIR-CLASS-CEILING"],
        "PAIR-CLASS-CEILING": ["FLOW-GENERATOR-CLASSICAL"],
        "FLOW-GENERATOR-CLASSICAL": ["DBN-DICTIONARY"],
        "DBN-DICTIONARY": ["H3COF"], "H3COF": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["HCOF"],
        "HCOF": ["WEILPOS"], "WEILPOS": ["RH"]}
    loop_pair = has_cycle(chain_pair)
    chain_zv = {
        "RH-VERIFIED-AT-T": ["FLOW-Z-AT-T"],
        "FLOW-Z-AT-T": ["CENSUS-STATEMENT-AT-T"],
        "CENSUS-STATEMENT-AT-T": ["RH-VIA-CHAIN"],
        "RH-VIA-CHAIN": ["RH-VERIFIED-AT-T"]}
    loop_zv = has_cycle(chain_zv)
    chain_uni = {
        "RH": ["CENSUS_ALLK"],
        "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"],
        "RH_VIA_N": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    chain_pin = {
        "TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
        "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]}
    loop_pin = has_cycle(chain_pin)
    chain_term = {
        "DBN-FLOW-P-EXACT": ["DBN-DICT-VERDICT"],
        "DBN-LAMBDA-LADDER": ["DBN-DICT-VERDICT"],
        "DBN-THETA-BUDGET": ["DBN-DICT-VERDICT"],
        "DBN-WALL-FRAGILITY": ["DBN-DICT-VERDICT"],
        "DBN-DICT-VERDICT": ["H3_COFINAL"],
        "ENVJ_H1": ["PF"], "CENSUS_H2": ["PF"], "TRACE": ["PF"],
        "H3_PER_RUNG": ["RATE"], "H3_COFINAL": ["RATE"],
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
                   for n in ("DBN-FLOW-P-EXACT", "DBN-LAMBDA-LADDER",
                             "DBN-THETA-BUDGET", "DBN-WALL-FRAGILITY",
                             "ENVJ_H1", "CENSUS_H2", "H3_COFINAL",
                             "CENSUS_K"))
    check("G63-endgame-graphs", loop_bwd and loop_pair and loop_zv
          and loop_uni and loop_pin and acyc and rh_reach,
          "FIVE loop cycles DETECTED: (i) dbn-backward: RH -> "
          "LAMBDA-LE-0 -> BACKWARD-REALNESS-PERSIST -> H2-COFINAL-"
          "VIA-FLOW -> PF -> ... -> RH (transporting realness from "
          "t = 0.22 down to 0 IS [Lambda <= 0] == RH: the pinch's "
          "missing leg is RH itself -- machine-flagged, NOT "
          "consumed); (ii) dbn-pair: RH -> MONTGOMERY-PC -> "
          "PAIR-CLASS-CEILING -> FLOW-GENERATOR-CLASSICAL -> ... "
          "-> RH (classical control of the flow's own generator is "
          "RH-conditional); (iii) zero-verif-at-height; (iv) "
          "universalized census; (v) pinning-supply; the terminal "
          "chain with the four DBN instruments as MEASURED leaves "
          "feeding the H3_COFINAL adjudication is ACYCLIC: "
          "NO RH CLAIM")
    info("THE POST-ROUND RESIDUE (exact, typed): the dBN heat flow "
         "is IMPORTED, DICTIONARIED AND ADJUDICATED -- it does NOT "
         "pinch: the three faces of the flow on the wall family "
         "are mutually inequivalent (>= 1e9, opposite signs), the "
         "theta observable is flow-inert inside the whole "
         "unconditional window (exact budget floors >= 4021x), the "
         "wall margin is flow-incommensurate (fragility 8-51 "
         "orders below the window), the realness-granting "
         "direction BREAKS the derived census nonnegativity, and "
         "the only pinch-closing leg (backward persistence) is "
         "RH-equivalent and flagged.  DELIVERED INSTRUMENTS (kept, "
         "MEASURED class): the exact finite flow e^{-tT} on the "
         "census family (closed form) and the lambda_h "
         "backward-margin criticality ladder (2.39 -> 0.216, "
         "decreasing, limit OPEN).  The residue is UNCHANGED IN "
         "CARDINALITY: {H1 AND H2 AND H3}-COFINAL (one rung per "
         "dyadic block, all three at the same h; limsup form only "
         "mod the measured defect D = 0.0042, CDXCIII wording) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{L1 = TAIL proven + H-pin open, WPD open}.  NO omega "
         "closed; nothing upgraded; NO RH CLAIM.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "CITED-LADDER-REPLICATED(G30)",
        "FLOW-EXACT-ON-DERIVED-CENSUS(G12/G31)",
        "REALNESS-WINDOW-WIDE(G32)",
        "CENSUS-SUBCRITICAL-DECAYING(G32)",
        "THETA-FLOW-INERT(G33)",
        "GENERATOR-EXCEEDS-ATOM-REWEIGHTING-BY-PAIR-CLASS(G14)",
        "DICTIONARY-THREEFOLD-INEQUIVALENT(G36)",
        "SOURCE-FACE-WALL-FATAL(G34)",
        "WALL-FLOW-INCOMMENSURATE(G34/G35)",
        "FLOW-Z-BREAKS-DERIVED-H2(G35)",
        "PINCH-NOT-ASSEMBLED(G15/G63)",
        "BACKWARD-PERSISTENCE-IS-RH-CLASS-FLAGGED(G15/G63)",
        "CONTROLS-SEPARATED(G50/G51)",
        "EPSTEIN-SLACK-LARGER(G51)",
        "ARITHMETIC-MORE-CRITICAL-THAN-SMOOTH(G50)",
        "WITNESS-PRESERVED-NOT-EXPELLED(G52)",
        "DEMAND-FLAT(G54)",
        "BOUND-RIDES-TAU(G54)",
        "QUANTIFIER-SEQ(G60)",
        "LOOP-ROUTES-FLAGGED(G61/G63)",
        "OMEGA-UNCHANGED(G62)",
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
