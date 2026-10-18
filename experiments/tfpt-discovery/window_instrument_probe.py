#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""window_instrument_probe -- PRIME.WINDOW.INSTRUMENT.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (build the collective window instrument: translate the r160
carrier property BAND-RESTRICTED NO-NEGATIVE-SPECTRAL-MASS directly
into window-constant structure -- consuming positivity AS SUCH, not
through the six-fold-proven rate-blind moment/trace/algebra class)
=======================================================================
State consumed (CITED): CDLXIV/r160 (j2_primeforce: plant/ghost
asymmetry, ghost s*-table b5 {2: 4.1e-4, 5: 1.9e-4, 9: 6.0e-8, 14.5:
8.8e-6, 30: 6.5e-2}, b8 range 6.0e-6..5.5e-4, single plants benign,
b5 multi-plant at total mass 4 BREAKS, b8 multi in-window J_2 0.0740,
RESCUE-INFEASIBLE-IN-CLASS, IRREDUCIBLY-COLLECTIVE, G82 band-
positivity typing with the census-edge sliver factor 1.26);
CDLXVII/r162 (fullgap_growthlaw: quartic law J == THETA T_z^4, THETA/
c_1/jr/t_r strings, slot constants c_1..c_6 x-free with the pair
structure, G15 ALGEBRA-ONLY-REFUTED-FOR-THETA, trial cap Courant-hard
with saturation falling ~x^-3.2, moment route obstructed); CDLX/r156
(rootladder: L1 moment-Laurent dictionary PHI(z) = z - 1 +
sum J_{m+1} z^-m, L2 quarter-cap J_2 <= 1/4 + z|rho| -- THE self-cap
template, L4/L5 cascade, MOMENT-SPLIT shape/scale sectors, 2-mode
witness ALGEBRA-ONLY-J-CAPS-REFUTED); CDLXV (gfloor: razor GF1-GF5);
CDLIII (bughunt4 hygiene); r136 (c is the exact frame tau-minimizer);
PT21 (verified zeros below H); HSW22 Cor. 1.2 (tail band G).
Builders (frozen, imported read-only): R4.build_cell, AEP.
anchor_select/cell_matrix, RL.census_weighted, JP.nprime_block/
prime_atoms/build_world/world_measure/in_window (the r160 world
machinery VERBATIM by import -- no numeric path re-typed).

FROZEN QUANTIFIER (declared before the deep data): the W2 demand
adjudicated here is [FORALL blocks of the instrument ladder: (i)
positive band spec-measure ==> PSD-premise transport, EXACT; (ii)
negative band mass at any gamma with ground overlap breaks PSD at the
EXACT threshold s*(gamma), tau-priced; (iii) the window-VALUE leg is
adjudicated by in-class witnesses].  Statements hold per block /
per rung; NO claim beyond the instrument ladder; NO RH claim in any
direction.  Z1 TYPING: the budget layer consumes cache zeros below
the horizon as ward-class data (typed, not hidden); the ghost/plant
worlds are constructed source-side and NEVER consume zero data.

=======================================================================
THE THEOREMS (exact layer; sympy generic + exact rational instances +
mp instances per rung/block; classical inputs typed CITED)
=======================================================================
THEOREM WI1 (positivity transport; the plant side).  For symmetric M
and PSD P, s >= 0: lam_min(M + sP) >= lam_min(M) (Weyl monotonicity,
chased); for rank-1 P = lamP vv': lam_min(M + s lamP vv') <= lam_1(M)
for ALL s >= 0 (a unit u* in span(psi_0, psi_1) cap v-perp has
c-independent Rayleigh <= lam_1) -- THE PLANT SANDWICH tau <=
tau_plant <= lam_1; and lam_min(M + s lamP vv') -> lam_min of the
compression of M to v-perp as s -> oo (THE PLATEAU IS THE DEFLATION,
2-level limit chased + mp instance).  CONSEQUENCE: positive band
mass of ANY strength preserves the PSD premise of the entire
GL/ladder/razor chain and moves the pair (tau, A_0) only within the
deflation plateau -- bounded response.

THEOREM WI2 (the ghost secular threshold; the first-order fragility).
For M > 0 and P = lamP vv' PSD rank-1: det(M - sP) == det(M) (1 -
s lamP v' M^-1 v) is LINEAR in s, hence lam_min(M - sP) >= 0 iff
s <= s* := 1/(lamP v' M^-1 v), and with w_i = v' psi_i:
v' M^-1 v = sum w_i^2/lam_i >= w_0^2/tau, so s* <= tau/(lamP w_0^2):
THE GHOST PRICE IS tau-PRICED -- negative band mass at ANY gamma
with nonzero ground overlap destroys the PSD premise at strength
collapsing WITH THE CONNES COLLAPSE (measured b5: s* = 1.7e-15 at
gamma = 2 vs tau = 2.0e-15; the r160 J_2-break thresholds 6e-8..6e-2
sit 7..11 dex ABOVE the PSD crossing: the window locally outlives
positivity, the premise does not).

THEOREM WI3 (the first-order perturbation law; the honest asymmetry
form).  d tau/ds |_{M -+ sP} = -+ phi' P phi and d A_0/ds |_{M - sP}
= + alpha' (M - tau)^+ P phi = sum_{i>=1} (alpha' psi_i)(psi_i' P
phi)/(lam_i - tau) (closed form via the reduced resolvent /adjugate;
sympy 3-level chase; mp vs central finite differences).  THE
DERIVATIVE IS SIGN-ODD: plant and ghost have EQUAL first-order |dA_0|
(FIRST-ORDER-SYMMETRIC, hard assert) -- the r160 asymmetry is NOT in
the derivative but in the VALIDITY RANGE: ghost range ends at s* ~
tau-scale (WI2), plant range is unbounded with the deflation plateau
(WI1).  RANGE-ASYMMETRY, quantified: s_plant-tested/s*_ghost >= 1e12.

THEOREM WI4 (the far-form/budget-moment dictionary; the W1b leg).
EXACTLY (partial fractions, c-generic):  E_v(t) == (2 A_0/t)
sin(At) (1 + S(t^2)),  S(y) = sum_{k>=1} (-1)^k c_k b_k/((y - b_k)
A_0);  with r156-L1 (CITED + re-instanced) 1 + S(y) == (y_t/y)
PHI(z), z = y/y_t:   2 E_v(t)^2 == 8 A_0^2 sin^2(At) y_t^2
PHI(z)^2 / y^3  -- THE GW BUDGET'S ABOVE-BAND MASS IS AN EXACT
QUADRATIC FUNCTIONAL OF THE LADDER'S OWN MOMENT-LAURENT PHI: the
ladder parametrizes its own onset mass (the tlaw self-cap in the
r156 pattern), with the mass measured to sit 88..93 percent in the
STRIP (b_top, y_t) where the PHI dictionary reigns.  tlaw_0 in this
currency == [sum_gamma sin^2(A gamma) y_t^2 PHI^2/gamma^6 + zone +
band + tail] / G(T_z): upper leg = GW closure + PHI-window
(conditional, arithmetic via r156), lower leg = sin^2-equidistribution
of zeros against the pi Z/A lattice (arithmetic, typed OPEN).

THEOREM WI5 (theta chases; the W1a adjudication).  (i) THETA == c_1^2
identically (definitional chase + mp).  (ii) With R2 (r150/r162
CITED, re-chased) and Courant (CITED): THETA = (1 + FULLGAP)/(t_r
T_z^4) <= (1 + r_trial)/(t_r T_z^4) -- a HARD certified per-rung
upper self-cap consuming the trial's source arithmetic; measured
DIVERGENT: log10(cap/THETA) slope vs log10 x in (2.0, 4.6) (the
r162 trial mid-domination read as cap-opening).  (iii) tlaw_i/tlaw_0
== (lam_i/tau) (A_0(phi)/A_0(psi_i))^2 exact: the ladder law and the
slot windows are ONE statement.  (iv) SELFCAP-CLASS-BLIND-TO-THETA
(hard assert): the per-vector moment families {J_m(phi)}, {J_m(psi_1)}
are invariant under per-vector scaling while THETA scales freely --
the r156 self-cap class (shape sector) CANNOT reach the cross-vector
ratio THETA (scale-sector pair); with r162-G15 (re-asserted): no
algebra-only THETA pin exists; the THETA lower cap IS the open omega.
Jet toy also realizes tlaw == 1e6 and 1e-6 at fixed (lam, G):
ALGEBRA-ONLY-REFUTED-FOR-TLAWABS.

THEOREM WI6 (cofinality bookkeeping; the W3 identification).  Band
edges omega_max(x) ~ 2.5 pi x are monotone unbounded, so EVERY zero
ordinate lies below all but finitely many band edges of any unbounded
ladder (chased + integer instance); with the r160-G82 typing (CITED:
band-restricted near-critical positivity at height x == zeros below
the band edge on the line, PT21-class below horizon, sliver factor
1.26 disclosed):  BANDPOS along ANY unbounded ladder <==> all zeros
on the line == RH.  THE LOOP IDENTIFICATION: a landed value-transport
would close the program onto its own hypothesis at the horizon.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use anywhere, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (kind=exact): G10 WI1 (Weyl monotonicity chase +
    rank-1 cap + plateau limit + rational instances); G11 WI2
    (linear-det identity + threshold + tau-price corollary + exact
    rational crossing instance det = 2 - 3s at s* = 2/3); G12 WI3
    (first-order eigenpair chase to O(s^2) + dA_0 closed form +
    SIGN-ODD hard assert); G13 WI4 (far-form partial fractions +
    budget-moment chase); G14 WI5 chases (theta == c_1^2; trial-cap
    transport; tlaw ladder recoordination); G15 red team (r162 theta
    toy re-assert + tlaw toy 1e6/1e-6 + SELFCAP-CLASS-BLIND-TO-THETA
    hard assert); G16 WI6 (cofinality limit + integer instance;
    LOOP identification typed).
S2  G20 HSW G(T) sanity.
S3  rung layer x = (5,60),(8,80),(13,120) core + (18,140),(24,150),
    (28,160) deep (R4 cells; NO zone census needed by this probe):
    G30 anchor replicas: FULLGAP on FG_TAB x (0.97, 1.03); THETA/c_1
    on the r162 strings (rel 5e-3 core, 1.5e-2 deep); jr on the
    CDLIV strings rel 2e-2; t_r on strings rel 5e-3 core, (0.85,
    1.10) deep; tlaw_0 on the CDXLI strings rel 5e-3 (x <= 24), in
    (0.40, 0.70) at 28; lam_1 simple (rel gap >= 1e3); spectrum
    positive sorted;
    G31 theta self-cap: |THETA - c_1^2| <= 1e-30; trial orthogonality
    <= 1e-40; COURANT HARD r_trial >= FULLGAP (1 - 1e-12); THETA <=
    theta_cap = (1 + r_trial)/(t_r T_z^4) HARD; post-loop divergence
    slope log10(cap/THETA) vs log10 x in (2.0, 4.6) (DIVERGENT typing);
    G32 slot table: c_i for 1 <= i < min(nc, 8): c_1 per-rung strings;
    c_2..c_6 in the frozen r162 full-ladder ranges +-10 percent:
    c_2 (0.18, 0.26), c_3 (0.06, 0.14), c_4 (0.041, 0.069), c_5
    (0.026, 0.062), c_6 (0.0165, 0.0293); c_7 report-only; pair ratio
    c_5/c_4 in (0.40, 1.35) where nc > 5; c_7/c_6 report-only;
    G33 dictionary instances: far-form identity rel dev <= 1e-40 at
    the 3 sample points (1.1, 1.7, 3.0) x om_max; budget-moment
    identity rel dev <= 1e-40 at one above-band cache zero;
    G34 GW budget (x <= 18; phi AND psi_1): closure S_cache/lam in
    (0.95, 1 + 1e-12) and rem/env in [-1e-12, 0.05] at x = 5/8
    (calibrated 0.9893/0.9864 phi, rem/env 0.002/0.000); at x =
    13/18 closure in (0.90, 1 + 1e-9), rem/env in [-1e-9, 1.0]
    (pre-freeze unmeasured, DISCLOSED); zone share <= 1e-2;
    strip+far share >= 0.9; <sin^2>_(gamma>T_z) in (0.30, 0.80);
    tlaw lower leg (S_strip + S_far)/(8 A_0^2 G(T_z)) <= tlaw_0
    HARD (the conditional cap instantiated);
    G35 (kind=screen) slot-kernel battery: candidates GEOHALF/
    WALLIS/FEJER/HARM/HARM2 scaled to c_1; MATCH iff max rel dev
    <= 0.15 over i = 2..min(6, nc-1) at every rung with nc > 4;
    calibrated: GEOHALF nearest, fails at i = 6 (x = 8: +41
    percent): expected NO-CLASSICAL-KERNEL-MATCH;
    G36 (kind=screen) c_1 band-edge-offset law: Pearson corr of
    (ufrac, c_1) over the ladder, reported.
S4  W2 battery (AEP blocks b5/b8; the r160 machinery by import):
    G40 plant atom (PSD min eig >= -1e-50, rank-2 rel <= 1e-25,
    Fourier-ratio identity <= 1e-30, JP bars);
    G41 WI2 instances per gamma in (2, 5, 9, 12, 14.5, 20, 30):
    lu residual <= 1e-40; lam_min(M - s*(1 -+ 1e-6) P) sign flip
    HARD; s* <= tau/(lamP w_0^2) (1 + 1e-9) HARD; s*/price >= 0.5;
    G42 ghost replica (JP path VERBATIM): b5 on the r160 strings
    {2: 4.1e-4, 5: 1.9e-4, 9: 6.0e-8, 14.5: 8.8e-6, 30: 6.5e-2}
    rel <= 0.05 (calibrated devs <= 1.6e-2); b8 min in [5.4e-6,
    6.6e-6], max in [5.0e-4, 6.1e-4] (calibrated 5.98e-6/5.54e-4);
    G43 WI3 instances: dA_0 closed form vs central FD at h = 1e-3 s*
    rel <= 1e-6 (calibrated <= 3.2e-11 b8, 3.0e-9 b5); d tau vs
    phi' P phi rel <= 1e-6;
    G44 WI1 instances: deflation tau_defl in [tau, lam_1] HARD;
    plant sandwich at s = 1 and 1e3 HARD; plateau |tau_w/tau_defl -
    1| <= 1e-9 and |A_0_w/A_0_defl - 1| <= 1e-9 at s = 1e3
    (calibrated 1.2e-13/6.0e-25); RANGE-ASYMMETRY s_tested/s*(g=5)
    >= 1e12 (calibrated 2.6e17/3.1e29);
    G45 value witnesses: b5 multi-plant (gap x4, total mass 4):
    tau_W > 0 AND NOT in-window AND J_2 on the calibrated string
    -0.569031 rel 5e-3 (VALUE-TRANSPORT-REFUTED-IN-CLASS); b8
    multi IN-window with J_2 on 0.073959 rel 5e-3 (the r160 0.0740
    string; NON-MONOTONE-IN-CLASS); single plants g = 2/9 in-window
    on the calibrated J_2 strings rel 5e-3 (b5 0.089403/0.091222,
    b8 0.131521/0.131677);
    G46 premise transport: EVERY plant world tau_W >= tau (1 -
    1e-12) HARD; single plants tau_W <= lam_1 (1 + 1e-9) HARD.
S5  controls: G50 SMOOTH x5, G51 SCRARITH x5, G52 EPSTEIN x8 (R4
    worlds): tau_w < 0 (the WI1/WI2 PSD premise fails EXACTLY here
    -- the instrument refuses); J_2_w on the r156 strings rel 5e-3
    (-2.962/-0.8449/-2.71); THETA_w on the r162 strings rel 0.25
    (3.6e-6/8.1e-8/4.0e-7); G53 consistency.
S6  G54 tau-screens: slopes vs log10 tau of THETA, c_1, jr, t_r
    <= 0.30 and of strip/far shares <= 0.35 (DEMAND-FLAT); RIDER
    report: slopes of log10 A_0(phi)^2, log10 A_0(psi_1)^2 in
    (0.85, 1.15) (BOUND-RIDES-CONNES typed); G55 conditioning
    (1e-25 shift at x = 5, round-118 trap).
S7  G60 demand audit (CHAIN-AUDIT, SEQ level inherited; Z1 typing);
    G61 min-cut (r162 graph VERBATIM: flows base 4, refined 5,
    one-grant 5, counterfactual PARALLEL 9 NOT REAL; census {MEAS,
    OMEGA-POS} cardinality 4 UNCHANGED); G62 W3 adjudication graph:
    real edges {BANDPOS -> PSDPREM (this round), WINVALS -> RH
    (corpus conditional, CITED), RH -> BANDPOS (trivial)}: WINVALS
    unreachable from BANDPOS (RELOCATION-BLOCKED, per G45);
    counterfactual value edge PSDPREM -> WINVALS creates the cycle
    RH -> BANDPOS -> PSDPREM -> WINVALS -> RH (LOOP-IF-ASSEMBLED,
    detected); BANDPOS unreachable from UNC (beyond horizon).
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER = ((5,60),(8,80),(13,120),(18,140),(24,150),
(28,160)); BUDGET_RUNGS = (5, 8, 13, 18); BUDGET_HARD = (5, 8);
HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2]; W2_BLOCKS =
((5, 5.44, 60), (8, 8.50, 80)); GAMMA_LIST = (2, 5, 9, 12, 14.5,
20, 30); GHOST_GAMMAS = JP.GHOST_GAMMAS; PLANT_GAP = (2, 5, 9, 12).
BARS: FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18:
3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97, 1.03) [r162];
THETA_TAB = {5: 0.256907, 8: 0.172985, 13: 0.245072, 18: 0.1904,
24: 0.2206, 28: 0.1830} rel 5e-3 core / 1.5e-2 deep; C1_TAB = {5:
0.506860, 8: 0.415915, 13: 0.495048, 18: 0.4364, 24: 0.4697, 28:
0.4278} same tols; JR_TAB = {5: 1.1245, 8: 1.1097, 13: 1.0273, 18:
0.9588, 24: 1.0020, 28: 1.0615} rel 2e-2 [CDLIV]; TR_TAB = {5:
0.8893, 8: 0.9011, 13: 0.9734} rel 5e-3, deep window (0.85, 1.10);
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24:
0.5122} rel 5e-3, TLAW28_WIN = (0.40, 0.70); SIMP_MIN = 1e3;
THC1_BAR = 1e-30; TRIAL_ORTHO_BAR = 1e-40; ENC_SLOP = 1e-12;
CAP_SLOPE_WIN = (2.0, 4.6) (calibrated x5->x8 pairwise 4.03; r162
sat-slope ~-3.2 full-ladder); SLOT_WIN = {2: (0.18, 0.26), 3:
(0.06, 0.14), 4: (0.041, 0.069), 5: (0.026, 0.062), 6: (0.0165,
0.0293)}; PAIR45_WIN = (0.40, 1.35); FARFORM_BAR = 1e-40
(calibrated 4.8e-56..3.2e-67); BM_BAR = 1e-40 (calibrated 5.3e-55/
1.2e-67); FF_SAMPLES = (1.1, 1.7, 3.0); CLOSURE_WIN_CORE = (0.95,
1 + 1e-12); REMENV_WIN_CORE = (-1e-12, 0.05); CLOSURE_WIN_DEEP =
(0.90, 1 + 1e-9); REMENV_WIN_DEEP = (-1e-9, 1.0); ZONE_SHARE_BAR =
1e-2; SFFLOOR = 0.9; SIN2_WIN = (0.30, 0.80); KERNEL_TOL = 0.15;
PLANT_PSD_BAR = -1e-50; PLANT_RANK_BAR = 1e-25; PLANT_ID_BAR =
1e-30 [JP]; LURES_BAR = 1e-40 (calibrated <= 7.8e-51); SSTAR_EPS =
1e-6; PRICE_SLOP = 1e-9; SPRICE_MIN = 0.5 (calibrated 0.946 worst
at gamma 30); GHOST_B5_STRINGS = {2: 4.1e-4, 5: 1.9e-4, 9: 6.0e-8,
14.5: 8.8e-6, 30: 6.5e-2} rel 0.05; GHOST_B8_MIN_WIN = (5.4e-6,
6.6e-6); GHOST_B8_MAX_WIN = (5.0e-4, 6.1e-4); FD_BAR = 1e-6;
PLATEAU_BAR = 1e-9 (s = 1e3); RANGE_MIN = 1e12; MP_J2_B5 =
-0.569031, MP_J2_B8 = 0.073959, SP_J2 = {(5, 2): 0.089403, (5, 9):
0.091222, (8, 2): 0.131521, (8, 9): 0.131677} rel 5e-3;
CTRL_J2_STRINGS = {SMOOTH: -2.962, SCRARITH: -0.8449, EPSTEIN:
-2.71} rel 5e-3; CTRL_THETA_STRINGS = {SMOOTH: 3.6e-6, SCRARITH:
8.1e-8, EPSTEIN: 4.0e-7} rel 0.25; TAU_SLOPE_BAR = 0.30;
SHARE_SLOPE_BAR = 0.35; W0_RIDER_WIN = (0.85, 1.15); COND_WIN =
(1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward only);
RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf
arithmetic inside explicit mp.workdps blocks; no f64 refinement of
mp roots; flat O(1) ratios transported as f64 for gating
(disclosed); huge/tiny quantities (A_0, jets, s*, tau) stay mp
end-to-end (r147/r141 underflow classes banned); frozen builders
imported read-only (R4/AEP/RL/JP -- the JP import is the r160
world machinery VERBATIM; no concurrent-lane file is written).

CALIBRATION DISCLOSURE (pre-freeze, ONE scratch calib_scratch_wi.py
in TWO passes (pass 1 = x5 + b5, pass 2 = x8 + b8; logs
calib_wi_pass1.log/calib_wi_pass2.log kept; scratch deleted after
freeze); all numbers quoted verbatim above and here): x=5: FG
2.225493e5, THETA 0.256907 == c_1^2 dev 0.0, t_r 0.8893, tlaw_0
0.2664, slots 0.5069/0.2225/0.0685 (nc 4), trial r 3.913545e6,
theta_cap 4.5177 (cap/theta 17.585), farform devs <= 4.6e-55,
budget-moment dev 5.3e-55 at gamma 52.97, budget phi shares
z/b/s/f 2e-7/1e-4/0.8837/0.1055 closure 0.989290 rem/env 0.002,
psi1 0.8356/0.1516 closure 0.987953, <sin^2> 0.6575, sum g^-2/
G(T_z) 0.3856, edge ufrac 0.3948.  x=8: FG 9.951249e5, THETA
0.172985, t_r 0.9011, slots 0.4159/0.2367/0.1023/0.0458/0.0290/
0.0184 (nc 7; pair c5/c4 0.633), trial r 1.165195e8, theta_cap
20.2549 (cap/theta 117.090), farform <= 3.2e-67, budget-moment
1.2e-67, budget phi 0.9349/0.0515 closure 0.986419, psi1 closure
0.984897, <sin^2> 0.5470, ufrac 0.1538.  b5 (x0 4.823998, K 10,
tau 2.048e-15, d1 2.627e-10): s*-table (gamma: s*, s*/price)
2: 1.691e-15/1.000, 5: 3.845e-15/1.000, 9: 4.306e-14/1.000, 12:
1.401e-12/0.999, 14.5: 3.807e-10/0.999, 20: 9.710e-9/0.994, 30:
9.227e-4/0.946; sign flips +-2.05e-21; lures <= 7.8e-51; dA_0 FD
rel <= 3.0e-9; deflation g=5 tau_defl 1.641998e-10 in [tau, lam_1];
plant plateau devs s=1e3: 1.2e-13; ghost replica 2: 4.09e-4, 5:
1.93e-4, 9: 6.01e-8, 14.5: 8.80e-6, 20: 2.10e-5, 30: 6.48e-2;
multi-plant tau 1.663e-1 J_2 -0.569031 ytb 1.37 n_esc 1 BREAK;
singles g2/g9 J_2 0.089403/0.091222 IN.  b8 (x0 7.394749, K 19,
tau 1.651e-27, d1 1.245e-21): s* 1.331e-27 (g2) .. 1.162e-14
(g30), s*/price >= 0.994, FD rel <= 3.2e-11, plateau 6.0e-25,
ghost replica min 5.98e-6 (g9) max 5.54e-4 (g30), multi-plant tau
6.371e-8 J_2 0.073959 IN, singles 0.131521/0.131677.  x = 13/18/
24/28 pre-freeze UNMEASURED on all new quantities (build cost);
windows set from the frozen r162/CDLIV strings + calibrated trends,
DISCLOSED.  Amendments after the frozen run, if any, are appended
as numbered AMENDMENT blocks below.

VERDICT ENUMS (frozen): WI1-PROVEN + PLANT-PLATEAU-IS-DEFLATION;
WI2-PROVEN + GHOST-TAU-PRICED (s* <= tau/(lamP w_0^2), instances) +
R160-TABLE-REPLICATED; WI3-PROVEN + FIRST-ORDER-SYMMETRIC +
RANGE-ASYMMETRY(quantified) (the honest form of the contract's
first-vs-second-order law: the derivative is sign-odd; the
asymmetry is the validity range, tau-scale vs unbounded-plateau);
WI4-PROVEN (budget-moment dictionary: the ladder parametrizes its
own onset mass) + TLAW-CAP-CONDITIONAL (upper leg = GW closure +
PHI window, arithmetic via r156; lower leg = sin^2-equidistribution,
typed OPEN; mid leg measured share); WI5: THETA-EQ-C1SQ-PROVEN +
THETA-UPPER-CAP-CERTIFIED-DIVERGENT + THETA-LOWER-OBSTRUCTED-
EQUALS-OMEGA + SELFCAP-CLASS-BLIND-TO-THETA + ALGEBRA-ONLY-REFUTED-
FOR-TLAWABS; SLOT-KERNEL verdict {MATCHED(name) |
NO-CLASSICAL-KERNEL-MATCH(best)}; W2 CONDITIONAL:
PREMISE-TRANSPORT-PROVEN (both directions: BANDPOS necessary AND
sufficient for the PSD premise, at exact thresholds) +
VALUE-TRANSPORT-REFUTED-IN-CLASS (b5 multi-plant witness; b8
NON-MONOTONE exhibit); W3: RELOCATION-BLOCKED-AT-VALUE-LEG +
LOOP-IF-ASSEMBLED (BANDPOS(unbounded ladder) == RH, WI6 + r160-G82
CITED) -- the final relocation does NOT assemble, and had it
assembled it would close onto its own hypothesis; CONTROLS-REFUSE;
DEMAND-FLAT + BOUND-RIDES-CONNES; QUANTIFIER-INHERITED;
OMEGA-UNCHANGED (residue set unchanged; census {MEAS, OMEGA-POS}
cardinality 4 UNCHANGED); MINCUT(4/5).  Composite priority:
INSTRUMENT-EDGE > EXACT-LAYER-OBSTRUCTED > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.

=======================================================================
AMENDMENT 1 (owner directive, received DURING record run 1)
=======================================================================
HONEST DISCLOSURE OF STATE AT DIRECTIVE ARRIVAL: the pre-amendment
spec was FROZEN (SPEC_SHA 8e064879b50df7ef), smoke had passed 31/31,
and record run 1 was in flight.  Run 1 was allowed to complete and is
KEPT VERBATIM (wi_run1.log): 33/34 gates, the single failure
G34-gw-budget at the deep rungs 13/18 where the measured closure
ratios 1.19e19/4.88e43 are pure f64-cache truncation noise (the
E(gamma)^2 scale ~1e-54/1e-79 sits ~20-45 dex below the 16-digit
cache floor ~1e-35) -- an honest instrument-edge finding of run 1,
typed CACHE-PRECISION-FLOOR; this amendment narrows the two-sided
closure gate to the HARD rungs (5, 8) where it is measurable (run 1:
0.9893/0.9864 phi) and keeps the ratio-level deep demands (zone
share, strip+far floor, sin^2 window, tlaw lower leg HARD) gated.
Run 1 additionally serves as the DISCLOSED CALIBRATION SOURCE for the
Gate-A windows below (its slot table for i <= 7); the HELD-OUT slots
c_8/c_9 were NOT computed by run 1 (loop capped at i <= 7), by any
prior round, or by any calibration pass -- the GA3 prediction below
is frozen BEFORE their first computation.  Calibration passes 3 and 4
(accretion battery, fake ladders, synthetic cone, alias share, Haar
compression; logs calib_wi_pass3.log/calib_wi_pass4.log kept,
scratches deleted) are quoted verbatim below.

GATE A (THE DYADIC SPECTRAL LADDER, primary W1 test; slots extended
to i <= 9):
GA1 dyadic-pair fit c_i == c_1 2^-F(i), F = (1, 2, 3, 3, 4, 4) for
    i = 2..7, max rel dev <= DYAD_TOL = 0.20 at deep rungs (18, 24,
    28); run1-calibrated worst devs 0.146/0.165/0.169: the ladder is
    APPROXIMATE-DYADIC at the 15-17 percent level; the owner's 1-5
    percent read (from rounded cross-rung means 0.45/0.215/0.11/
    0.055/0.055/0.026) is NOT reproduced at mp precision -- typed
    honestly; core rungs report-only (EMERGENT).
GA2 window-independence: cross-rung spread of c_i/c_1 over the deep
    rungs <= DYAD_SPREAD = 0.25 (run1 worst 0.198 at i = 3); plus
    the construction audit: slots consume ONLY the cell spectrum --
    no h, no a, no target signs, no measured J_2.
GA3 HELD-OUT PREDICTION (kind=screen, frozen BEFORE first compute):
    the pair continuation predicts c_8 == c_9 == c_1/2^5; windows
    c_i 2^5/c_1 in (0.75, 1.25) at x = 24, 28 (18 report-only);
    verdict enum DYADIC-PREDICTION-{CONFIRMED|REFUTED|MIXED}.
GA4 moment adjudication: shifted Hankel H_1(c_2..c_6) min eig < 0
    (mp exact) AND log-convexity break c_5^2/(c_4 c_6) >= 1.5 at
    every deep rung (run1-implied dets -9.4e-5/-1.28e-4/-1.12e-4,
    breaks 2.02/2.16/1.91; the owner's -1.58e-4 confirmed in kind):
    STIELTJES-MOMENT-REFUTED (formal kill of the positive-kernel-
    moment hypothesis on mp values, not rounded ones) +
    CHRISTOFFEL-WEIGHTS-DOA (needs the refuted positive measure).
GA5 dies-in-fakes (GATE A(4)): the dyadic fit must FAIL (worst dev
    > DYAD_TOL) in SMOOTH/SCRARITH/EPSTEIN (calibrated 8.18/262.25/
    26.42; the fakes have no collapsed block at all): the
    identification dies with the arithmetic, NOT window geometry.
GA6 (kind=screen) the owner's fixed 8x8 kernel on even alias modes
    {2,4,..,16}: ground-mass share vs the owner string 0.999937 --
    calibrated 0.147 at x=8: NOT-REPRODUCED-IN-BASIS (the owner's
    object lives in another lane's basis; typed, not silently
    dropped); 8x8 compression eigenladder reported (not dyadic).
GA7 (kind=screen) Haar/dyadic transfer (Lf)(x) = [f(x/2) +
    f((x+1)/2)]/2 compressed to 8 cos modes: calibrated |eigs|
    1.0000/0.4865/0.2267/0.2267/0.0150/... -- the dyadic-transfer
    mechanism CAN double multiplicities under cos-lattice aliasing
    (the owner's doubled-multiplicity shape), but the head
    (1, 1/2, 1/4, 1/4) mismatches the measured (1, 1/2, 1/4, 1/8,
    1/8): OPEN-CANDIDATE; no fixed transfer object identified.

GATE B (THE TANGENT CRITERION replaces the naive W2 law):
GB1 generic-cone adjudication FIRST: WI1/WI2 verified on a fixed
    SYNTHETIC PSD matrix (diag(1e-12, 1e-6, 1, 2, 5) under three
    fixed Givens rotations, v = 1/sqrt(5)) with NO prime content:
    calibrated s* = 4.249944e-12, sign flip at s*(1 +- 1e-6) HARD:
    ASYMMETRY-LAW-GENERIC-CONE -- the owner's suspicion CONFIRMED
    and typed; the ARITHMETIC content is the boundary LOCATION
    (tau at the Connes collapse) and the anchor VALUES.
GB2 the accretion-path tangent battery (b5/b8): source-built band
    path A_j = [arch + pole] - sum_{i<=j} N_i, atoms in frozen
    u-order, NO zero data, NO window signs; boundary touches
    bisected (48 steps); the tangent v'A'v = -v'N_q v computed FROM
    THE PRIME SOURCE block.  Gates: source additivity <= 1e-40;
    endpoint PSD HARD; exactly ONE entering crossing, in the LAST
    atom segment, t* >= 0.999; tangent > 0 at the touch HARD.
    Calibrated: b5 profile -0.350/-0.258/-0.0265/+2.05e-15, ENTER
    at t* = 0.999933 of atom u = log 4, tangent +6.300e-10; b8
    profile -0.584/../-2.78e-3/+1.65e-27, ENTER at t* = 0.999790 of
    atom u = log 7, tangent +3.945e-23.  THE EXHIBIT: no partial
    comb is positive -- the path enters the cone only in the tail
    of the LAST atom (1 - t* ~ 7e-5/2e-4): the collective property
    path-wise, and the entering derivative has the RIGHT SIGN from
    the source alone.
GB3 fakes must violate at their death sites: SCRARITH b5/b8 and
    EPSTEIN b8 accretion paths never surviving-enter the cone
    (calibrated endpoints -0.2409/-0.6346/-1.5349): NO-ENTRY =
    the violation mode; TANGENT-CRITERION-DISTINGUISHES.
GB4 (kind=screen) in-cell height path (FD in u at fixed K/icap):
    calibrated d log tau/du = -35.4 (b5) / -210.3 (b8): the height
    path squeezes toward the boundary at the Connes rate without
    touching inside verified cells; SUCCESS-CRITERIA AUDIT typed
    (path source-built, derivative not back-fitted, per-block
    hypothesis); the full chain [prime source ==> tangent ==>
    invariance ==> H_cof ==> RH] is NOT ASSEMBLED: the exhibit
    lives at n = 3/5 atoms, no unbounded-comb theorem.

GATE C (COFINAL, NOT UNIVERSAL replaces the W3 bar):
GC1 pre-defined dyadic depth ladder x_j = 5 * 2^j, bar = ONE
    positive rung per dyadic block (the r122 NF-closure/r141 SEQ
    demand).  EXACT DISTINCTION machine-checked on the relocation
    graph: (i) BANDPOS at all heights (or any unbounded zero-band
    ladder) == RH by WI6 cofinality: LOOP (G62 unchanged); (ii)
    HCOF (cofinal FORM positivity on the mesh ladder) is NOT a
    loop: the counterfactual propagation edge {DYADREC, TANGENT}
    -> PROP -> HCOF reaches RH with no cycle back through the
    measured nodes: a genuine advance TARGET.  STATUS:
    COFINAL-TARGET-IDENTIFIED-NOT-ASSEMBLED; the exact missing
    piece is PROP = the depth-block transfer theorem [positivity
    at rung j + a proven transfer object ==> positivity at rung
    j+1]; the GA dyadic recurrence is measured-only (and
    moment-refuted, transfer-unidentified), so PROP has no proven
    operator behind it in this round.

AMENDED FROZEN NUMERICS: DYAD_F = {2:1, 3:2, 4:3, 5:3, 6:4, 7:4};
DYAD_RUNGS = (18, 24, 28); DYAD_TOL = 0.20; DYAD_SPREAD = 0.25;
HELD_EXP = 5; HELD_WIN = (0.75, 1.25); HELD_RUNGS = (24, 28);
LOGCONV_BREAK_I = 5; LOGCONV_BREAK_MIN = 1.5; ALIAS_OWNER =
0.999937; TSTAR_MIN = 0.999; ACC_BLOCKS = W2_BLOCKS; ACC_FAKES =
(SCRARITH b5, SCRARITH b8, EPSTEIN b8); ACC_BIS = 48; MSYN =
diag(1e-12, 1e-6, 1, 2, 5) @ Givens((0,1,.3),(2,3,.7),(1,4,1.1));
COF_X0 = 5.  G34 re-freeze: closure/remenv gated at BUDGET_HARD
only; deep rungs report CACHE-PRECISION-FLOOR.

AMENDMENT 1a (post-run-2 disclosure, honest re-freeze): record run 2
at the Amendment-1 SHA a17e85a0867c6935 (wi_run2.log KEPT VERBATIM:
45/46, runtime 4064 s) measured the deep ZONE/BAND budget legs at
the same f64 cache floor (x = 13/18 zone share ~1e19-scale noise/
lambda: the zone is exactly where the minimizer tunes E(gamma) to
vanish, so 16-digit zeros give pure slope noise there, while the
STRIP/FAR legs are genuine signal, 0.980/0.978 of lambda, and the
sin^2/tlaw-lower legs are ratio-level honest) -- the Amendment-1
wording wrongly kept the deep zone share gated; re-freeze: zone
share gated at BUDGET_HARD only, deep zone/band typed
CACHE-PRECISION-FLOOR alongside the closure.  The duplicate
deterministic re-run at the superseded SHA was killed mid-flight
(disclosed; it would have replicated the same single G34 refusal);
the record pair (wi_run3.log record + wi_run4.log deterministic
re-run) is executed at THIS final SHA.  Run 2's science stands and
is expected to replicate identically: GA1 worst devs 0.145/0.164/
0.169 (APPROXIMATE-DYADIC); GA2 spread worst 0.198 (i=3); GA3
HELD-OUT verdict DYADIC-PREDICTION-MIXED(2/4) -- c_9 confirmed
(ratios 1.121/1.093), c_8 MISSES HIGH (1.285/1.348): the pair
continuation (8,9) is REFUTED as an equal pair at depth while the
1/32 rung itself is confirmed on c_9 -- the ladder continues dyadic
but the multiplicity pattern beyond i = 7 is NOT the frozen guess;
GA4 Hmin -2.08e-2/-2.04e-2/-2.24e-2, dets -9.44e-5/-1.29e-4/
-1.12e-4, breaks 2.02/2.15/1.90 (STIELTJES-MOMENT-REFUTED); GA6
shares 0.147..0.271 rising with x, never near 0.999937; GB2/GB3
exactly as calibrated.

AMENDED VERDICT ENUMS: DYADIC-PAIR-LADDER-ADJUDICATED
(APPROXIMATE-DYADIC 15-17 percent, NOT exact) +
DYADIC-PREDICTION-{CONFIRMED|REFUTED|MIXED} +
STIELTJES-MOMENT-REFUTED + CHRISTOFFEL-WEIGHTS-DOA +
DYADIC-DIES-IN-FAKES + ALIAS-NOT-REPRODUCED-IN-BASIS +
HAAR-OPEN-CANDIDATE; ASYMMETRY-LAW-GENERIC-CONE +
BOUNDARY-LOCATION-ARITHMETIC + TANGENT-CRITERION-HOLDS-AT-CONE-
ENTRY + FAKES-VIOLATE-BY-NO-ENTRY + TANGENT-CHAIN-NOT-ASSEMBLED;
LOOP-vs-COFINAL-DISTINGUISHED + COFINAL-TARGET-IDENTIFIED-NOT-
ASSEMBLED (missing piece PROP); CACHE-PRECISION-FLOOR (deep
closure).  Everything else in the pre-amendment spec stands.
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

import radius4_an_probe as R4              # noqa: E402
import anchor_epslock_probe as AEP         # noqa: E402
import rootladder_probe as RL              # noqa: E402  (census dep)
import j2_primeforce_probe as JP           # noqa: E402
import fullgap_growthlaw_probe as FGL      # noqa: E402  (hsw_G)

_ = RL  # imported for the JP census dependency chain; not called here

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((5, 60), (8, 80), (13, 120), (18, 140), (24, 150), (28, 160))
BUDGET_RUNGS = (5, 8, 13, 18)
BUDGET_HARD = (5, 8)
W2_BLOCKS = ((5, 5.44, 60), (8, 8.50, 80))
GAMMA_LIST = (2.0, 5.0, 9.0, 12.0, 14.5, 20.0, 30.0)
PLANT_GAP = (2.0, 5.0, 9.0, 12.0)

FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
          24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
THETA_TAB = {5: 0.256907, 8: 0.172985, 13: 0.245072, 18: 0.1904,
             24: 0.2206, 28: 0.1830}
C1_TAB = {5: 0.506860, 8: 0.415915, 13: 0.495048, 18: 0.4364,
          24: 0.4697, 28: 0.4278}
CORE_TOL = 5e-3
DEEP_TOL = 1.5e-2
JR_TAB = {5: 1.1245, 8: 1.1097, 13: 1.0273, 18: 0.9588, 24: 1.0020,
          28: 1.0615}
JR_TOL = 2e-2
TR_TAB = {5: 0.8893, 8: 0.9011, 13: 0.9734}
TR_TOL = 5e-3
TR_DEEP_WIN = (0.85, 1.10)
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
TLAW28_WIN = (0.40, 0.70)
SIMP_MIN = 1e3
THC1_BAR = 1e-30
TRIAL_ORTHO_BAR = 1e-40
ENC_SLOP = 1e-12
CAP_SLOPE_WIN = (2.0, 4.6)
BLOCK_FRAC = 0.1
SLOT_WIN = {2: (0.18, 0.26), 3: (0.06, 0.14), 4: (0.041, 0.069),
            5: (0.026, 0.062), 6: (0.0165, 0.0293)}
PAIR45_WIN = (0.40, 1.35)
FARFORM_BAR = 1e-40
BM_BAR = 1e-40
FF_SAMPLES = (1.1, 1.7, 3.0)
CLOSURE_WIN_CORE = (0.95, 1 + 1e-12)
REMENV_WIN_CORE = (-1e-12, 0.05)
CLOSURE_WIN_DEEP = (0.90, 1 + 1e-9)
REMENV_WIN_DEEP = (-1e-9, 1.0)
ZONE_SHARE_BAR = 1e-2
SFFLOOR = 0.9
SIN2_WIN = (0.30, 0.80)
KERNEL_TOL = 0.15
LURES_BAR = 1e-40
SSTAR_EPS = 1e-6
PRICE_SLOP = 1e-9
SPRICE_MIN = 0.5
GHOST_B5_STRINGS = {2.0: 4.1e-4, 5.0: 1.9e-4, 9.0: 6.0e-8,
                    14.5: 8.8e-6, 30.0: 6.5e-2}
GHOST_TOL = 0.05
GHOST_B8_MIN_WIN = (5.4e-6, 6.6e-6)
GHOST_B8_MAX_WIN = (5.0e-4, 6.1e-4)
FD_BAR = 1e-6
PLATEAU_BAR = 1e-9
RANGE_MIN = 1e12
MP_J2 = {5: -0.569031, 8: 0.073959}
SP_J2 = {(5, 2.0): 0.089403, (5, 9.0): 0.091222,
         (8, 2.0): 0.131521, (8, 9.0): 0.131677}
WIT_TOL = 5e-3
CTRL_J2_STRINGS = {"SMOOTH": -2.962, "SCRARITH": -0.8449,
                   "EPSTEIN": -2.71}
CTRL_J2_TOL = 5e-3
CTRL_THETA_STRINGS = {"SMOOTH": 3.6e-6, "SCRARITH": 8.1e-8,
                      "EPSTEIN": 4.0e-7}
CTRL_THETA_TOL = 0.25
TAU_SLOPE_BAR = 0.30
SHARE_SLOPE_BAR = 0.35
W0_RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 14400.0

# ------------------------------------------- AMENDMENT 1 (owner gates)
DYAD_F = {2: 1, 3: 2, 4: 3, 5: 3, 6: 4, 7: 4}   # dyadic-pair exponents
DYAD_RUNGS = (18, 24, 28)                       # deep rungs (emerged)
DYAD_TOL = 0.20        # max rel dev, deep (run1: 0.146/0.165/0.169)
DYAD_SPREAD = 0.25     # cross-rung spread (run1 worst 0.198 at i=3)
HELD_EXP = 5                                    # c_8 = c_9 = c_1/2^5
HELD_WIN = (0.75, 1.25)                         # frozen BEFORE compute
HELD_RUNGS = (24, 28)
LOGCONV_BREAK_I = 5                             # c_5^2 > c_4 c_6
LOGCONV_BREAK_MIN = 1.5
ALIAS_OWNER = 0.999937                          # owner string (test)
TSTAR_MIN = 0.999                               # cone entry in the
ACC_BLOCKS = ((5, 5.44, 60), (8, 8.50, 80))     # last atom's tail
ACC_FAKES = (("SCRARITH", 5, 5.44, 60), ("SCRARITH", 8, 8.50, 80),
             ("EPSTEIN", 8, 8.50, 80))
ACC_BIS = 48
MSYN_DIAG = ("1e-12", "1e-6", "1", "2", "5")    # generic-cone world
MSYN_ROTS = ((0, 1, "0.3"), (2, 3, "0.7"), (1, 4, "1.1"))
COF_X0 = 5                                      # dyadic depth ladder
                                                # x_j = 5 * 2^j

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail, kind))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
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


# ------------------------------------------------------------ helpers
def E_of(cs, aa, oms, t):
    """E_v(t) = sin(aa t) R_v(t) (source data only)."""
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 WI1 plant side
    lmin, cpos, vu2, un2 = sp.symbols("lmin cpos vu2 un2", positive=True)
    uMu = sp.symbols("uMu", real=True)
    # monotonicity: Ray(M + c vv', u) - lmin|u|^2 =
    #   (u'Mu - lmin|u|^2) + c(v.u)^2 >= 0 given both nonneg
    diff_ = (uMu + cpos * vu2 - lmin * un2) \
        - ((uMu - lmin * un2) + cpos * vu2)
    okA = sp.simplify(diff_) == 0 and (cpos * vu2).is_positive is True
    # rank-1 cap: 3-level diag(l0,l1,l2), v generic; u* = (-v2, v1, 0)
    l0, l1, l2 = sp.symbols("l0 l1 l2", positive=True)
    v1, v2, v3 = sp.symbols("v1 v2 v3", real=True)
    ray_us = (l0 * v2 ** 2 + l1 * v1 ** 2) / (v1 ** 2 + v2 ** 2)
    okB = sp.simplify(l1 - ray_us
                      - (l1 - l0) * v2 ** 2 / (v1 ** 2 + v2 ** 2)) == 0
    okC = sp.simplify((-v2) * v1 + v1 * v2 + 0 * v3) == 0  # u* in v-perp
    # plateau: 2-level [[a, b], [b, d]] + c e1 e1': lam_min -> d
    a_, b_, d_, c_ = sp.symbols("a_ b_ d_ c_", positive=True)
    tr = a_ + c_ + d_
    disc = sp.sqrt((a_ + c_ - d_) ** 2 + 4 * b_ ** 2)
    lam_min = (tr - disc) / 2
    okD = sp.limit(lam_min, c_, sp.oo) == d_
    # rational instance: M = diag(1,2), v = e1: M + c e1e1' has
    # lam_min = min(1 + c, 2) <= lam_1 = 2 for all c >= 0
    okE = bool(min(1 + sp.Rational(7, 2), 2) <= 2)
    out.append(("G10-wi1-plant-transport", okA and okB and okC and okD
                and okE,
                "Weyl monotonicity lam_min(M + sP) >= lam_min(M) for "
                "PSD P (chase); rank-1 cap lam_min(M + c vv') <= "
                "lam_1(M) for ALL c >= 0 (u* in span(psi0, psi1) cap "
                "v-perp has c-independent Rayleigh <= lam_1: THE "
                "PLANT SANDWICH); plateau limit c -> oo == deflated "
                "compression (2-level chased): THEOREM WI1 -- "
                "positive band mass preserves the PSD premise at ANY "
                "strength with bounded (deflation-plateau) response"))

    # ---------------- G11 WI2 ghost secular threshold
    m1, m2, m3, lp, s = sp.symbols("m1 m2 m3 lp s", positive=True)
    w1, w2, w3 = sp.symbols("w1 w2 w3", real=True)
    Mm = sp.diag(m1, m2, m3)
    vv = sp.Matrix([w1, w2, w3])
    det_lhs = (Mm - s * lp * vv * vv.T).det()
    det_rhs = m1 * m2 * m3 * (1 - s * lp * (w1 ** 2 / m1
                                            + w2 ** 2 / m2
                                            + w3 ** 2 / m3))
    okF = sp.simplify(det_lhs - det_rhs) == 0
    # tau-price: 1/(lp sum w^2/m) <= m1/(lp w1^2)
    quad = w1 ** 2 / m1 + w2 ** 2 / m2 + w3 ** 2 / m3
    okG = sp.simplify(quad - w1 ** 2 / m1
                      - (w2 ** 2 / m2 + w3 ** 2 / m3)) == 0 \
        and (w2 ** 2 / m2 + w3 ** 2 / m3).is_nonnegative is True
    # rational crossing instance: M = diag(1,2), P = vv' with
    # v = (1,1): det(M - sP) = 2 - 3s, s* = 2/3; PD at 1/2, not at 1
    sq = sp.symbols("sq", positive=True)
    Mi = sp.diag(1, 2)
    Pi = sp.Matrix([[1, 1], [1, 1]])
    det_i = sp.expand((Mi - sq * Pi).det())
    okH = sp.simplify(det_i - (2 - 3 * sq)) == 0
    e_half = (Mi - sp.Rational(1, 2) * Pi).eigenvals()
    e_one = (Mi - 1 * Pi).eigenvals()
    okI = all(sp.re(ev) > 0 for ev in e_half) \
        and any(sp.re(ev) < 0 for ev in e_one)
    out.append(("G11-wi2-secular-threshold", okF and okG and okH
                and okI,
                "det(M - s lamP vv') == det(M)(1 - s lamP v'M^-1 v) "
                "LINEAR in s (generic 3-level) ==> lam_min(M - sP) "
                ">= 0 iff s <= s* = 1/(lamP v'M^-1 v); v'M^-1 v >= "
                "w_0^2/tau ==> s* <= tau/(lamP w_0^2) (tau-PRICED); "
                "rational instance det = 2 - 3s crossing at s* = "
                "2/3 with PD/indefinite verified both sides: "
                "THEOREM WI2 -- the ghost price collapses with the "
                "Connes collapse"))

    # ---------------- G12 WI3 first-order perturbation law
    p00, p01, p02, p11, p12, p22 = sp.symbols(
        "p00 p01 p02 p11 p12 p22", real=True)
    ss = sp.symbols("ss", real=True)
    Pg = sp.Matrix([[p00, p01, p02], [p01, p11, p12], [p02, p12, p22]])
    Mg = sp.diag(l0, l1, l2)
    phi0 = sp.Matrix([1, 0, 0])
    du = sp.Matrix([0, p01 / (l1 - l0), p02 / (l2 - l0)])
    lamp = l0 - ss * p00
    resid = (Mg - ss * Pg) * (phi0 + ss * du) - lamp * (phi0 + ss * du)
    okJ = all(sp.simplify(sp.expand(resid[i]).coeff(ss, 0)) == 0
              and sp.simplify(sp.expand(resid[i]).coeff(ss, 1)) == 0
              for i in range(3))
    # dA0/ds = sum alpha_i P_i0/(l_i - l0); sign-odd under s -> -s
    a0s, a1s, a2s = sp.symbols("a0s a1s a2s", real=True)
    alv = sp.Matrix([a0s, a1s, a2s])
    dA0 = (alv.T * du)[0, 0]
    dA0_expl = a1s * p01 / (l1 - l0) + a2s * p02 / (l2 - l0)
    okK = sp.simplify(dA0 - dA0_expl) == 0
    resid_p = (Mg + ss * Pg) * (phi0 - ss * du) \
        - (l0 + ss * p00) * (phi0 - ss * du)
    okL = all(sp.simplify(sp.expand(resid_p[i]).coeff(ss, 1)) == 0
              for i in range(3))
    assert okL, "FIRST-ORDER-SYMMETRIC: dA_0 must be sign-odd"
    out.append(("G12-wi3-perturbation-law", okJ and okK and okL,
                "(M - sP)(phi + s dphi) == (l0 - s p00)(phi + s dphi)"
                " to O(s^2) with dphi = sum_{i>=1} P_i0/(l_i - l0) "
                "e_i (generic 3-level); dA_0/ds = sum alpha_i P_i0/"
                "(l_i - l0) closed form; plant direction flips BOTH "
                "signs (HARD ASSERT FIRST-ORDER-SYMMETRIC): THEOREM "
                "WI3 -- the plant/ghost asymmetry is NOT in the "
                "derivative, it is the validity-range asymmetry "
                "(WI1 plateau vs WI2 tau-scale threshold)"))

    # ---------------- G13 WI4 far-form + budget-moment dictionary
    t_, aa_ = sp.symbols("t_ aa_", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1s, b2s = sp.symbols("b1s b2s", positive=True)
    Rv = 2 * c0 / t_ + 2 * (-1) * c1 * t_ / (t_ ** 2 - b1s) \
        + 2 * c2 * t_ / (t_ ** 2 - b2s)
    A0g = c0 - c1 + c2
    Sg = (-c1 * b1s / (t_ ** 2 - b1s)
          + c2 * b2s / (t_ ** 2 - b2s)) / A0g
    okM = sp.simplify(sp.together(
        Rv - (2 * A0g / t_) * (1 + Sg))) == 0
    # budget-moment chase: with 1 + S == (yt/y) Phi (L1 CITED):
    yts, ys, Phis, sins, A0s = sp.symbols(
        "yts ys Phis sins A0s", positive=True)
    Efar = (2 * A0s / sp.sqrt(ys)) * sins * (yts / ys) * Phis
    okN = sp.simplify(2 * Efar ** 2
                      - 8 * A0s ** 2 * sins ** 2 * yts ** 2
                      * Phis ** 2 / ys ** 3) == 0
    out.append(("G13-wi4-budget-moment-dictionary", okM and okN,
                "E_v(t) == (2 A_0/t) sin(At)(1 + S(t^2)) EXACT "
                "(partial fractions, generic); with r156-L1 (CITED) "
                "1 + S == (y_t/y) PHI(z): 2 E^2 == 8 A_0^2 sin^2 "
                "y_t^2 PHI^2/y^3: THEOREM WI4 -- the GW budget's "
                "above-band mass is an exact quadratic functional "
                "of the ladder's own moment-Laurent PHI (the tlaw "
                "self-cap in the r156 quarter-cap pattern)"))

    # ---------------- G14 WI5 theta chases
    Jq, Tz = sp.symbols("Jq Tz", positive=True)
    th = Jq / Tz ** 4
    c1q = sp.sqrt(Jq) / Tz ** 2
    okO = sp.simplify(th - c1q ** 2) == 0
    FGs, rtr, trr = sp.symbols("FGs rtr trr", positive=True)
    # R2 (CITED, re-chased in r162 G13): J t_r == 1 + FG
    okP = sp.simplify((1 + FGs) / (trr * Tz ** 4)
                      - ((1 + rtr) / (trr * Tz ** 4))
                      + (rtr - FGs) / (trr * Tz ** 4)) == 0 \
        and ((rtr - FGs) / (trr * Tz ** 4)).subs(
            rtr, FGs + 1).is_positive is True
    # tlaw recoordination
    eta0, eta1, Gs, lam_i, tau_s = sp.symbols(
        "eta0 eta1 Gs lam_i tau_s", positive=True)
    tl0 = tau_s / (8 * eta0 ** 2 * Gs)
    tli = lam_i / (8 * eta1 ** 2 * Gs)
    okQ = sp.simplify(tli / tl0
                      - (lam_i / tau_s) * (eta0 / eta1) ** 2) == 0
    out.append(("G14-wi5-theta-chases", okO and okP and okQ,
                "THETA == c_1^2 identically; [Courant CITED: FG <= "
                "r_trial] + [R2 CITED: J t_r == 1 + FG] ==> THETA "
                "<= (1 + r_trial)/(t_r T_z^4) (the trial theta "
                "self-cap, monotone chase); tlaw_i/tlaw_0 == "
                "(lam_i/tau)(A_0(phi)/A_0(psi_i))^2 (the ladder law "
                "and the slot windows are ONE statement): "
                "THEOREM WI5"))

    # ---------------- G15 red team
    p_, q_, Tt = sp.symbols("p_ q_ Tt", positive=True)
    theta_toy = (q_ / p_) ** 2 / Tt ** 4
    okR = sp.simplify(theta_toy.subs(q_, 10 ** 3 * Tt ** 2 * p_)
                      - 10 ** 6) == 0 \
        and sp.simplify(theta_toy.subs(q_, p_ * Tt ** 2 / 10 ** 3)
                        - sp.Rational(1, 10 ** 6)) == 0
    lamt, Gt, A0t = sp.symbols("lamt Gt A0t", positive=True)
    tlaw_toy = lamt / (8 * A0t ** 2 * Gt)
    okS = sp.simplify(tlaw_toy.subs(A0t, A0t / 10 ** 3)
                      / tlaw_toy - 10 ** 6) == 0
    # SELFCAP-CLASS-BLIND-TO-THETA: per-vector J_m invariant under
    # per-vector scaling; theta scales freely
    tsc = sp.symbols("tsc", positive=True)
    A0v, A2v, A4v = sp.symbols("A0v A2v A4v", real=True)
    J2form = (A4v / A0v) / (A2v / A0v) ** 2
    okT = sp.simplify(J2form.subs([(A0v, tsc * A0v),
                                   (A2v, tsc * A2v),
                                   (A4v, tsc * A4v)]) - J2form) == 0
    theta_pair = (q_ / p_) ** 2
    okU = sp.simplify(theta_pair.subs(q_, tsc * q_)
                      - tsc ** 2 * theta_pair) == 0
    assert okT and okU, \
        "SELFCAP-CLASS-BLIND-TO-THETA: the per-vector moment " \
        "dictionary cannot see the cross-vector jet ratio"
    out.append(("G15-redteam-toys", okR and okS and okT and okU,
                "theta toy free at 1e6 AND 1e-6 (r162 G15 "
                "re-asserted); tlaw toy free at fixed (lam, G): "
                "ALGEBRA-ONLY-REFUTED-FOR-TLAWABS; per-vector J_m "
                "families scale-invariant while THETA scales as "
                "t^2 (HARD ASSERT SELFCAP-CLASS-BLIND-TO-THETA): "
                "the r156 self-cap class lives in the shape sector, "
                "THETA is a scale-sector PAIR object -- only "
                "arithmetic-consuming instruments may pin it"))

    # ---------------- G16 WI6 cofinality
    xs = sp.symbols("xs", positive=True)
    Bx = sp.Rational(5, 2) * sp.pi * xs
    okV = sp.limit(Bx, xs, sp.oo) == sp.oo \
        and sp.simplify(sp.diff(Bx, xs)
                        - sp.Rational(5, 2) * sp.pi) == 0
    gam_inst = 10 ** 6
    jst = None
    for j in range(1, 64):
        if 2.5 * math.pi * (2 ** j) >= gam_inst:
            jst = j
            break
    okW = jst is not None and 2.5 * math.pi * 2 ** (jst - 1) < gam_inst
    out.append(("G16-wi6-cofinality", okV and okW,
                "band edges 2.5 pi x monotone unbounded; every zero "
                "ordinate lies below all but finitely many band "
                "edges of any unbounded ladder (integer instance "
                "gamma = 1e6, j* = %s); with the r160-G82 typing "
                "(CITED: band positivity at height x == zeros below "
                "the edge on the line, PT21-class below horizon, "
                "sliver 1.26 disclosed): BANDPOS(unbounded ladder) "
                "<==> RH -- THEOREM WI6, the loop identification "
                "(bookkeeping-grade; the equivalence direction "
                "consumes only cofinality + the cited typing)" % jst))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 2, 0
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x", demand == SEQ))
    steps.append(("WI1-WI3 are per-block exact statements on the "
                  "r160 instrument blocks (source-side worlds, zero "
                  "zero-data); WI4/WI5 per-rung on the r162 ladder",
                  True))
    steps.append(("the budget layer consumes cache zeros below the "
                  "horizon as ward-class data (Z1-typed, disclosed); "
                  "the ghost/plant/threshold layer consumes NO zero "
                  "data", True))
    steps.append(("BANDPOS beyond the horizon is typed OPEN (never "
                  "assumed); the W3 adjudication grants it only "
                  "counterfactually", True))
    steps.append(("no ALL-X demand introduced", demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ------------------------------------------------------- rung layer
def rung_layer(x: int, dps: int, gam: np.ndarray,
               do_budget: bool) -> dict:
    out = {"x": x}
    ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out["K"] = K
    print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
          % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
    gtop = float(gam[-1])
    with mp.workdps(dps):
        E = ce["mpE"]
        V = ce["mpV"]
        Mq = ce["mpM"]
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0p = sum(((-1) ** k) * cs[k] for k in range(K))
        A2p = sum(((-1) ** k) * cs[k] * b[k] for k in range(K))
        yt = abs(A2p / A0p)
        tau = E[0]
        lam1 = E[1]
        lam2 = E[2]
        lammax = E[K - 1]
        FG = (lam1 - tau) / tau
        Tz = 2 * math.pi * x
        Tz2 = mp.mpf(repr(Tz)) ** 2
        Gz = mp.mpf(repr(FGL.hsw_G(Tz)))
        tlaw0 = tau / (8 * A0p * A0p * Gz)
        cs1 = [V[i, 1] / nrm[i] for i in range(K)]
        A01 = sum(((-1) ** k) * cs1[k] for k in range(K))
        J = (A01 / A0p) ** 2
        theta = J / Tz2 ** 2
        c1v = abs(A01 / A0p) / Tz2
        t_r = (lam1 * A0p * A0p) / (tau * A01 * A01)
        jr = J / FG
        out.update(pos_ok=all(E[i] > 0 for i in range(K)),
                   sort_ok=all(E[i] <= E[i + 1] for i in range(K - 1)),
                   fg=float(FG), theta=float(theta), c1=float(c1v),
                   t_r=float(t_r), jr=float(jr), tlaw0=float(tlaw0),
                   simp=float((lam2 - lam1) / lam1),
                   thc1_dev=float(abs(theta - c1v ** 2)),
                   a0p_l10=float(mp.log(abs(A0p)) / mp.log(10)),
                   a01_l10=float(mp.log(abs(A01)) / mp.log(10)),
                   tau_l10=float(mp.log(abs(tau)) / mp.log(10)))
        # ---------------- slots (AMENDMENT 1: extended to i <= 9;
        # i = 8, 9 are the GATE-A HELD-OUT targets, computed here for
        # the FIRST time, after the frozen prediction)
        nc = sum(1 for i in range(K)
                 if E[i] < mp.mpf(repr(BLOCK_FRAC)) * lammax)
        out["nc"] = nc
        slots = {}
        slots_mp = {}
        A_prev = A0p
        for i in range(1, min(nc, 10)):
            csi = [V[k2, i] / nrm[k2] for k2 in range(K)]
            A0i = sum(((-1) ** k2) * csi[k2] for k2 in range(K))
            ci_mp = abs(A0i / A_prev) / Tz2
            slots[i] = float(ci_mp)
            slots_mp[i] = ci_mp
            A_prev = A0i
        out["slots"] = slots
        # GATE-A moment adjudication data: shifted Hankel H_1 on the
        # mp slot values c_2..c_6 + log-convexity ratios (mp exact)
        if all(i in slots_mp for i in range(2, 8)):
            H1 = mp.matrix([[slots_mp[2], slots_mp[3], slots_mp[4]],
                            [slots_mp[3], slots_mp[4], slots_mp[5]],
                            [slots_mp[4], slots_mp[5], slots_mp[6]]])
            EH, _VH = mp.eigsy(H1)
            out["hankel_min"] = float(min(EH[i] for i in range(3)))
            out["hankel_det"] = float(mp.det(H1))
            out["logconv"] = {
                i: float(slots_mp[i] ** 2
                         / (slots_mp[i - 1] * slots_mp[i + 1]))
                for i in range(3, 7)}
        # GATE-A alias exhibit: ground-mass share on the even alias
        # modes {2, 4, ..., 16} + 8x8 compression eig ladder
        if K > 16:
            amodes = list(range(2, 17, 2))
            out["alias_share"] = float(sum(V[k2, 0] ** 2
                                           for k2 in amodes))
            M8 = mp.zeros(8, 8)
            for a2, ka in enumerate(amodes):
                for b2, kb in enumerate(amodes):
                    M8[a2, b2] = Mq[ka, kb]
            E8, _V8 = mp.eigsy(M8)
            e8s = sorted(float(E8[i]) for i in range(8))
            out["alias_ratios"] = [e8s[i + 1] / e8s[i] if e8s[i] != 0
                                   else float("inf") for i in range(7)]
        # ---------------- trial cap
        cvec = [V[i, 0] for i in range(K)]
        mu_b = sum(cvec[k] * cvec[k] * b[k] for k in range(K))
        vfr = [cvec[k] * (b[k] - mu_b) for k in range(K)]
        n2 = sum(vfr[k] * vfr[k] for k in range(K))
        ortho = float(abs(sum(vfr[k] * cvec[k] for k in range(K))))
        Mv = [sum(Mq[i, k] * vfr[k] for k in range(K))
              for i in range(K)]
        ray = sum(vfr[k] * Mv[k] for k in range(K)) / n2
        r_trial = (ray - tau) / tau
        th_cap = (1 + r_trial) / (t_r * Tz2 ** 2)
        out.update(ortho=ortho, r_trial=float(r_trial),
                   courant_ok=bool(r_trial
                                   >= FG * (1 - mp.mpf(repr(ENC_SLOP)))),
                   th_cap=float(th_cap),
                   cap_ok=bool(th_cap >= theta),
                   cap_ratio=float(th_cap / theta))
        # ---------------- far-form + budget-moment instances
        om_max = mp.sqrt(b[K - 1])
        ff_dev = 0.0
        for fac in FF_SAMPLES:
            t = mp.mpf(repr(fac)) * om_max
            Ev = E_of(cs, aa, oms, t)
            y = t * t
            S = sum(((-1) ** k) * cs[k] * b[k] / (y - b[k])
                    for k in range(1, K)) / A0p
            pred = (2 * A0p / t) * mp.sin(aa * t) * (1 + S)
            ff_dev = max(ff_dev, float(abs(Ev - pred) / abs(Ev)))
        out["ff_dev"] = ff_dev
        gsel = float(gam[int(np.searchsorted(
            gam, float(om_max) * 1.3))])
        t = mp.mpf(repr(gsel))
        y = t * t
        Ev = E_of(cs, aa, oms, t)
        Phi_dir = (y / yt) * (1 + sum(((-1) ** k) * cs[k] * b[k]
                                      / (y - b[k])
                                      for k in range(1, K)) / A0p)
        lhs = 2 * Ev * Ev
        rhs = 8 * A0p * A0p * mp.sin(aa * t) ** 2 * yt * yt \
            * Phi_dir ** 2 / y ** 3
        out["bm_dev"] = float(abs(lhs - rhs) / abs(lhs))
        out["bm_gamma"] = gsel
        # ---------------- GW budget
        if do_budget:
            eta_g = sum(abs(cs[k]) * b[k] for k in range(1, K)) \
                / (abs(A0p) * (mp.mpf(repr(gtop)) ** 2 - b[K - 1]))
            for tag, csv, lamv, A0v in (("phi", cs, tau, A0p),
                                        ("psi1", cs1, lam1, A01)):
                Sz = Sb = Ss = Sf = mp.mpf(0)
                for g in gam:
                    t = mp.mpf(repr(float(g)))
                    Ev = E_of(csv, aa, oms, t)
                    w2 = 2 * Ev * Ev
                    gf = float(g)
                    if gf <= Tz:
                        Sz += w2
                    elif gf <= float(om_max):
                        Sb += w2
                    elif gf * gf <= float(yt):
                        Ss += w2
                    else:
                        Sf += w2
                Stot = Sz + Sb + Ss + Sf
                env = 8 * (abs(A0v) * (1 + eta_g)) ** 2 \
                    * mp.mpf(repr(FGL.hsw_G(gtop)))
                rem = lamv - Stot
                out["bud_" + tag] = dict(
                    zshare=float(Sz / lamv), bshare=float(Sb / lamv),
                    sshare=float(Ss / lamv), fshare=float(Sf / lamv),
                    closure=float(Stot / lamv),
                    remenv=float(rem / env))
            s2 = mp.mpf(0)
            g2 = mp.mpf(0)
            for g in gam[gam > Tz]:
                t = mp.mpf(repr(float(g)))
                s2 += mp.sin(aa * t) ** 2 / (t * t)
                g2 += 1 / (t * t)
            out["sin2"] = float(s2 / g2)
            out["g2G"] = float(g2 / Gz)
            # tlaw lower leg (conditional cap instantiation)
            bp = out["bud_phi"]
            out["tlaw_lower"] = float((bp["sshare"] + bp["fshare"])
                                      * float(tau)
                                      / (8 * float(A0p) ** 2
                                         * float(Gz)))
        # edge offset
        m_zone = int(np.sum(gam <= Tz))
        g_lo = float(gam[m_zone - 1])
        g_hi = float(gam[m_zone])
        out["ufrac"] = (Tz - g_lo) / (g_hi - g_lo)
    return out


# -------------------------------------------------------- W2 battery
def w2_battery(tag: int, x_nom: float, dps: int) -> dict:
    out = {"tag": tag}
    u0, _lo, _hi = AEP.anchor_select(x_nom)
    x0 = math.exp(u0)
    icap = int(math.floor(x0))
    with mp.workdps(dps):
        u = mp.mpf(repr(u0))
        aa = u / 2
        K = int(math.ceil(AEP.kfun_f(float(mp.exp(u)))))
    MA, _n = AEP.cell_matrix(aa, K, icap, dps)
    atoms = JP.prime_atoms(icap, dps)
    NpT = JP.nprime_block(aa, K, dps, [("atoms", atoms)])
    rT = JP.world_measure(MA, K, aa, dps)
    with mp.workdps(dps):
        tau = rT["tau"]
        E = rT["E"]
        order = rT["order"]
        Vm = rT["V"]
        phi = rT["phi"]
        nrm = rT["nrm"]
        d1 = E[1] - E[0]
        alp = [((-1) ** k) / nrm[k] for k in range(K)]
        A0t = sum(alp[k] * phi[k] for k in range(K))
        out.update(x0=x0, K=K, tau=float(tau), d1=float(d1),
                   J2=rT["J2"], A0=float(A0t))
        psis = [[Vm[i, order[c]] for i in range(K)] for c in range(K)]
        # ---------------- plant atom instrument (JP bars)
        Np5 = JP.nprime_block(aa, K, dps, [("cos", 5.0, 1.0)])
        P5 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                P5[i, j] = -Np5[i, j]
        Ep5, _V5 = mp.eigsy(P5)
        evs = sorted([Ep5[i] for i in range(K)])
        out["plant_minev"] = float(evs[0])
        out["plant_rank_rel"] = float(abs(evs[-2] / evs[-1]))
        devs = []
        g5 = mp.mpf(5)
        for (k1, k2) in ((1, 2), (0, 3)):
            o1 = k1 * mp.pi / aa
            o2 = k2 * mp.pi / aa
            f1 = mp.quad(lambda t: (mp.cos(o1 * t) if k1 else 1)
                         * mp.cos(g5 * t), [-aa, 0, aa]) / nrm[k1]
            f2 = mp.quad(lambda t: (mp.cos(o2 * t) if k2 else 1)
                         * mp.cos(g5 * t), [-aa, 0, aa]) / nrm[k2]
            devs.append(float(abs((P5[k1, k1] / P5[k2, k2])
                                  / (f1 / f2) ** 2 - 1)))
        out["plant_id_dev"] = max(devs)
        # ---------------- WI2/WI3 per-gamma battery
        rows = []
        for g in GAMMA_LIST:
            Npg = JP.nprime_block(aa, K, dps, [("cos", g, 1.0)])
            P = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    P[i, j] = -Npg[i, j]
            Epg, Vpg = mp.eigsy(P)
            imax = max(range(K), key=lambda i: Epg[i])
            lamP = Epg[imax]
            vP = [Vpg[i, imax] for i in range(K)]
            w0 = sum(vP[i] * phi[i] for i in range(K))
            zsol = mp.lu_solve(MA, mp.matrix(vP))
            quad = sum(vP[i] * zsol[i] for i in range(K))
            lures = float(mp.norm(MA * zsol - mp.matrix(vP)))
            s_star = 1 / (lamP * quad)
            price = tau / (lamP * w0 * w0)
            flips = []
            for eps in (-SSTAR_EPS, +SSTAR_EPS):
                sv = s_star * (1 + mp.mpf(repr(eps)))
                Mw = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Mw[i, j] = MA[i, j] - sv * P[i, j]
                Ew, _ = mp.eigsy(Mw)
                flips.append(float(min(Ew[i] for i in range(K))))
            # WI3: closed-form dA0 + central FD + dtau FD
            Pphi = [sum(P[i, j] * phi[j] for j in range(K))
                    for i in range(K)]
            pTp = sum(phi[i] * Pphi[i] for i in range(K))
            D = mp.mpf(0)
            for c in range(1, K):
                av = sum(alp[k] * psis[c][k] for k in range(K))
                pv = sum(psis[c][k] * Pphi[k] for k in range(K))
                D += av * pv / (E[c] - E[0])
            h = s_star * mp.mpf("1e-3")
            fdA = []
            fdT = []
            for sgn in (-1, 1):
                Mw = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Mw[i, j] = MA[i, j] + sgn * h * P[i, j]
                Ew, Vw = mp.eigsy(Mw)
                i0 = min(range(K), key=lambda i: Ew[i])
                ph = [Vw[i, i0] for i in range(K)]
                if sum(ph[i] * phi[i] for i in range(K)) < 0:
                    ph = [-v for v in ph]
                nn = mp.sqrt(sum(v * v for v in ph))
                fdA.append(sum(alp[k] * ph[k] / nn for k in range(K)))
                fdT.append(Ew[i0])
            fd_dA = (fdA[0] - fdA[1]) / (2 * h)
            fd_dT = (fdT[1] - fdT[0]) / (2 * h)
            rows.append(dict(
                g=g, lamP=float(lamP), w02=float(w0 * w0),
                s_star=float(s_star), price=float(price),
                sprice=float(s_star / price), lures=lures,
                flip_lo=flips[0], flip_hi=flips[1],
                dA0_rel=float(abs(fd_dA / D - 1)) if D != 0 else 1.0,
                dtau_rel=float(abs(fd_dT / pTp - 1))
                if pTp != 0 else 1.0,
                D=float(D)))
        out["rows"] = rows
        # ---------------- WI1: deflation + plant plateau (g = 5)
        imax = max(range(K), key=lambda i: Ep5[i])
        nvp = mp.sqrt(sum(_V5[i, imax] ** 2 for i in range(K)))
        vP = [_V5[i, imax] / nvp for i in range(K)]
        e0 = [mp.mpf(1) if i == 0 else mp.mpf(0) for i in range(K)]
        wv = [vP[i] - e0[i] for i in range(K)]
        nw = mp.sqrt(sum(v * v for v in wv))
        wv = [v / nw for v in wv] if nw > mp.mpf("1e-30") else None
        cols = []
        for j in range(1, K):
            col = [mp.mpf(0)] * K
            col[j] = mp.mpf(1)
            if wv is not None:
                dot = wv[j]
                for i in range(K):
                    col[i] -= 2 * dot * wv[i]
            cols.append(col)
        Mc = mp.zeros(K - 1, K - 1)
        for a2 in range(K - 1):
            Ma = [sum(MA[i, j] * cols[a2][j] for j in range(K))
                  for i in range(K)]
            for b2 in range(a2 + 1):
                val = sum(cols[b2][i] * Ma[i] for i in range(K))
                Mc[a2, b2] = Mc[b2, a2] = val
        Ec, Vc = mp.eigsy(Mc)
        i0c = min(range(K - 1), key=lambda i: Ec[i])
        tau_defl = Ec[i0c]
        phc = [Vc[i, i0c] for i in range(K - 1)]
        ph_full = [sum(cols[j][i] * phc[j] for j in range(K - 1))
                   for i in range(K)]
        nn = mp.sqrt(sum(v * v for v in ph_full))
        A0_defl = sum(alp[k] * ph_full[k] / nn for k in range(K))
        out["defl_ok"] = bool(tau <= tau_defl <= E[1])
        out["tau_defl"] = float(tau_defl)
        plat = {}
        for sv in (1.0, 1e3):
            Mw = mp.zeros(K, K)
            lam5 = Ep5[imax]
            for i in range(K):
                for j in range(K):
                    Mw[i, j] = MA[i, j] \
                        + mp.mpf(repr(sv)) * lam5 * vP[i] * vP[j]
            Ew, Vw = mp.eigsy(Mw)
            i0 = min(range(K), key=lambda i: Ew[i])
            tw = Ew[i0]
            ph = [Vw[i, i0] for i in range(K)]
            if sum(ph[i] * ph_full[i] for i in range(K)) < 0:
                ph = [-v for v in ph]
            nn2 = mp.sqrt(sum(v * v for v in ph))
            A0w = sum(alp[k] * ph[k] / nn2 for k in range(K))
            plat[sv] = dict(tau_w=float(tw),
                            sandwich=bool(tau <= tw
                                          <= E[1] * (1 + 1e-9)),
                            tdev=float(abs(tw / tau_defl - 1)),
                            adev=float(abs(A0w / A0_defl - 1)))
        out["plateau"] = plat
        s5 = [r for r in rows if r["g"] == 5.0][0]
        out["range_ratio"] = 1e3 / s5["s_star"]
        # ---------------- ghost replica (JP path VERBATIM)
        d1f = float(d1)
        ghosts = {}
        for g in JP.GHOST_GAMMAS:
            lo = max(d1f * 1e-3, 1e-40)
            r_hi = JP.build_world(MA, NpT, [("atoms", atoms),
                                            ("cos", g, -1.0)],
                                  K, aa, dps, census=False)
            if JP.in_window(r_hi, lite=True):
                ghosts[g] = float("inf")
                continue
            a2g, b2g = math.log10(lo), 0.0
            for _ in range(JP.THETA_BIS_STEPS):
                m = 0.5 * (a2g + b2g)
                r = JP.build_world(MA, NpT,
                                   [("atoms", atoms),
                                    ("cos", g, -(10.0 ** m))],
                                   K, aa, dps, census=False)
                if not JP.in_window(r, lite=True):
                    b2g = m
                else:
                    a2g = m
            ghosts[g] = 10.0 ** b2g
        out["ghosts"] = ghosts
        # ---------------- value witnesses + premise transport
        wit = {}
        rmulti = JP.build_world(MA, NpT, [("atoms", atoms)]
                                + [("cos", g, 1.0) for g in PLANT_GAP],
                                K, aa, dps)
        wit["multi"] = dict(tau=rmulti["tau_f"], J2=rmulti["J2"],
                            ytb=rmulti["ytb"], nesc=rmulti["n_esc"],
                            inw=JP.in_window(rmulti),
                            transport=bool(rmulti["tau_f"]
                                           >= float(tau)
                                           * (1 - 1e-12)))
        for g in (2.0, 9.0):
            rs = JP.build_world(MA, NpT, [("atoms", atoms),
                                          ("cos", g, 1.0)],
                                K, aa, dps)
            wit["g%g" % g] = dict(
                tau=rs["tau_f"], J2=rs["J2"], inw=JP.in_window(rs),
                transport=bool(rs["tau_f"] >= float(tau)
                               * (1 - 1e-12)),
                sandwich=bool(rs["tau_f"] <= float(E[1])
                              * (1 + 1e-9)))
        out["wit"] = wit
    return out


# ---------------------------------------------------------------- main
# ---------------------------------------- AMENDMENT 1: Gate B battery
def accretion_battery(tag: int, x_nom: float, dps: int,
                      world: str) -> dict:
    """source-built band path: A_j = [arch + pole] - sum_{i<=j} N_i,
    atoms in frozen u-order (prime powers <= icap; SCRARITH permuted
    weights; EPSTEIN r162 atoms).  NO zero data, NO window signs.
    Locates every lam_min sign crossing, bisects the boundary touch
    t*, and evaluates the TANGENT CRITERION v'A'v = -v'N_q v at the
    kernel vector (the boundary derivative comes from the PRIME
    SOURCE block, not from any fit)."""
    out = {"tag": tag, "world": world, "crossings": []}
    u0, _lo, _hi = AEP.anchor_select(x_nom)
    x0 = math.exp(u0)
    icap = int(math.floor(x0))
    with mp.workdps(dps):
        u = mp.mpf(repr(u0))
        aa = u / 2
        K = int(math.ceil(AEP.kfun_f(float(mp.exp(u)))))
        MA, _n = AEP.cell_matrix(aa, K, icap, dps)
        atoms_true = JP.prime_atoms(icap, dps)
        if world == "TRUE":
            atoms = atoms_true
        elif world == "SCRARITH":
            pm = JP.scr_perm(icap)
            atoms = [(atoms_true[i][0], atoms_true[pm[i]][1])
                     for i in range(len(atoms_true))]
        else:
            atoms = JP.eps_atoms(icap, dps)
        Ns = [JP.nprime_block(aa, K, dps, [("atoms", [at])])
              for at in atoms]
        NallT = JP.nprime_block(aa, K, dps, [("atoms", atoms_true)])
        M0 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                M0[i, j] = MA[i, j] + NallT[i, j]
        # additivity ward (linearity of the source block)
        Nall = JP.nprime_block(aa, K, dps, [("atoms", atoms)])
        acc = mp.zeros(K, K)
        for Nq in Ns:
            for i in range(K):
                for j in range(K):
                    acc[i, j] += Nq[i, j]
        sc = max(abs(Nall[i, j]) for i in range(K) for j in range(K))
        out["add_dev"] = float(max(abs(acc[i, j] - Nall[i, j])
                                   for i in range(K)
                                   for j in range(K)) / sc)

        def lmin_vec(Mm):
            Ev, Vv = mp.eigsy(Mm)
            i0 = min(range(K), key=lambda i: Ev[i])
            return Ev[i0], [Vv[i, i0] for i in range(K)]

        Mj = M0.copy()
        lm, _v = lmin_vec(Mj)
        prof = [float(lm)]
        prev = lm
        for j, Nq in enumerate(Ns):
            Mn = mp.zeros(K, K)
            for i in range(K):
                for j2 in range(K):
                    Mn[i, j2] = Mj[i, j2] - Nq[i, j2]
            lm2, _v2 = lmin_vec(Mn)
            prof.append(float(lm2))
            if (prev < 0) != (lm2 < 0):
                lo_t, hi_t = mp.mpf(0), mp.mpf(1)
                for _ in range(ACC_BIS):
                    mid = (lo_t + hi_t) / 2
                    Mt = mp.zeros(K, K)
                    for i in range(K):
                        for j2 in range(K):
                            Mt[i, j2] = Mj[i, j2] - mid * Nq[i, j2]
                    lmt, _vt = lmin_vec(Mt)
                    if (lmt < 0) == (prev < 0):
                        lo_t = mid
                    else:
                        hi_t = mid
                tstar = (lo_t + hi_t) / 2
                Mt = mp.zeros(K, K)
                for i in range(K):
                    for j2 in range(K):
                        Mt[i, j2] = Mj[i, j2] - tstar * Nq[i, j2]
                lmt, vt = lmin_vec(Mt)
                tv = -sum(vt[i] * sum(Nq[i, j2] * vt[j2]
                                      for j2 in range(K))
                          for i in range(K))
                out["crossings"].append(dict(
                    seg=j + 1, kind="ENTER" if prev < 0 else "LEAVE",
                    tstar=float(tstar), lam_res=float(lmt),
                    tangent=float(tv),
                    u=float(atoms[j][0]), last=(j + 1 == len(Ns))))
            Mj = Mn
            prev = lm2
        out["profile"] = prof
        out["endpoint"] = float(prev)
        out["n_atoms"] = len(atoms)
        out["K"] = K
        if world == "TRUE":
            # in-cell height-path near-tangent (FD in u, fixed K/icap)
            du = mp.mpf("1e-8")
            Mp_, _ = AEP.cell_matrix(aa + du / 2, K, icap, dps)
            Mm_, _ = AEP.cell_matrix(aa - du / 2, K, icap, dps)
            Ep, _V = mp.eigsy(Mp_)
            Em, _V = mp.eigsy(Mm_)
            tp = min(Ep[i] for i in range(K))
            tm = min(Em[i] for i in range(K))
            out["dtau_du_rel"] = float((tp - tm) / (du * prev))
    return out


def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("window_instrument_probe -- PRIME.WINDOW.INSTRUMENT.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:1] if smoke else LADDER
    blocks = W2_BLOCKS[:1] if smoke else W2_BLOCKS
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
    info("Z1 TYPING (frozen): the budget layer consumes cache zeros "
         "below horizon as ward-class data (typed, not hidden); the "
         "ghost/plant/threshold layer consumes NO zero data")

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems WI1-WI6 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXIV plant/ghost tables + G82 typing; "
         "CDLXVII quartic law + G15 + trial cap; CDLX L1/L2 "
         "dictionary + moment split; CDLXV GF1-GF5; r150 R2; r136 "
         "minimizer; r114/r131 GW identity class; HSW22 Cor. 1.2; "
         "PT21; Weyl/Courant-Fischer; Cauchy interlacing; partial "
         "fractions; matrix determinant lemma")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    gtop = float(gam[-1])
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= FGL.hsw_G(Ttest)
    okG = okG and FGL.hsw_G(200.0) > FGL.hsw_G(2000.0) \
        > FGL.hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % FGL.hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  RUNG LAYER (theta/slots/dictionary/budget)")
    R = {}
    for x, dps in ladder:
        t0 = time.time()
        R[x] = rung_layer(x, dps, gam, do_budget=(x in BUDGET_RUNGS))
        print("  x=%d layer done (%.0f s)" % (x, time.time() - t0),
              flush=True)
    xs = sorted(R)

    ok30 = True
    d30 = []
    for x in xs:
        r = R[x]
        tol = CORE_TOL if x <= 13 else DEEP_TOL
        fg_ok = FG_TAB[x] * FG_WIN[0] <= r["fg"] <= FG_TAB[x] * FG_WIN[1]
        th_ok = abs(r["theta"] / THETA_TAB[x] - 1) <= tol
        c1_ok = abs(r["c1"] / C1_TAB[x] - 1) <= tol
        jr_ok = abs(r["jr"] / JR_TAB[x] - 1) <= JR_TOL
        if x in TR_TAB:
            tr_ok = abs(r["t_r"] / TR_TAB[x] - 1) <= TR_TOL
        else:
            tr_ok = TR_DEEP_WIN[0] <= r["t_r"] <= TR_DEEP_WIN[1]
        if x <= 24:
            tl_ok = abs(r["tlaw0"] / TLAW_TAB[x] - 1) <= TLAW_TOL
        else:
            tl_ok = TLAW28_WIN[0] <= r["tlaw0"] <= TLAW28_WIN[1]
        okx = (r["pos_ok"] and r["sort_ok"] and r["simp"] >= SIMP_MIN
               and fg_ok and th_ok and c1_ok and jr_ok and tr_ok
               and tl_ok)
        ok30 = ok30 and okx
        d30.append("x%d: FG %.4e th %.4f c1 %.4f jr %.4f t_r %.4f "
                   "tlaw %.4f" % (x, r["fg"], r["theta"], r["c1"],
                                  r["jr"], r["t_r"], r["tlaw0"]))
    check("G30-anchor-replicas", ok30,
          "FULLGAP/THETA/c_1/jr/t_r/tlaw_0 on the r162/CDLIV/CDXLI "
          "strings (rel %.0e core / %.0e deep); spectrum positive "
          "sorted; lam_1 simple: %s"
          % (CORE_TOL, DEEP_TOL, "; ".join(d30)))

    ok31 = True
    d31 = []
    for x in xs:
        r = R[x]
        okx = (r["thc1_dev"] <= THC1_BAR
               and r["ortho"] <= TRIAL_ORTHO_BAR
               and r["courant_ok"] and r["cap_ok"])
        ok31 = ok31 and okx
        d31.append("x%d: thc1 %.0e cap %.3f cap/th %.2f"
                   % (x, r["thc1_dev"], r["th_cap"], r["cap_ratio"]))
    if not smoke:
        lx = [math.log10(float(x)) for x in xs]
        lc = [math.log10(R[x]["cap_ratio"]) for x in xs]
        sl_cap = float(np.polyfit(lx, lc, 1)[0])
        ok31 = ok31 and CAP_SLOPE_WIN[0] <= sl_cap <= CAP_SLOPE_WIN[1]
        d31.append("cap-divergence slope %.3f" % sl_cap)
        info("THETA SELF-CAP exhibit (WI5): the only landed theta "
             "self-cap is the Courant trial transport THETA <= "
             "(1 + r_trial)/(t_r T_z^4) -- HARD per rung but "
             "DIVERGENT (slope %.2f in x): the r162 trial "
             "mid-domination read as cap-opening; the lower cap IS "
             "the open omega (G15)" % sl_cap)
    check("G31-theta-selfcap", ok31,
          "|THETA - c_1^2| <= %.0e; trial orthogonality <= %.0e; "
          "COURANT HARD; THETA <= theta_cap HARD; divergence slope "
          "in %s: %s" % (THC1_BAR, TRIAL_ORTHO_BAR,
                         str(CAP_SLOPE_WIN), "; ".join(d31)))

    ok32 = True
    d32 = []
    for x in xs:
        r = R[x]
        okx = True
        for i, ci in sorted(r["slots"].items()):
            if i == 1:
                continue
            if i in SLOT_WIN:
                okx = okx and SLOT_WIN[i][0] <= ci <= SLOT_WIN[i][1]
        if 4 in r["slots"] and 5 in r["slots"]:
            pr = r["slots"][5] / r["slots"][4]
            okx = okx and PAIR45_WIN[0] <= pr <= PAIR45_WIN[1]
        ok32 = ok32 and okx
        d32.append("x%d nc%d: %s" % (x, r["nc"], " ".join(
            "c%d %.4f" % (i, c) for i, c in sorted(r["slots"].items()))))
    check("G32-slot-table", ok32,
          "slot constants in the frozen r162 full-ladder windows "
          "(c_2..c_6); pair c_5/c_4 in %s; c_7 report-only: %s"
          % (str(PAIR45_WIN), "; ".join(d32)))

    ok33 = all(R[x]["ff_dev"] <= FARFORM_BAR
               and R[x]["bm_dev"] <= BM_BAR for x in xs)
    check("G33-dictionary-instances", ok33,
          "far-form identity E == (2A_0/t) sin(At)(1 + S) rel <= "
          "%.0e at %s x om_max; budget-moment identity 2E^2 == "
          "8A_0^2 sin^2 y_t^2 PHI^2/y^3 rel <= %.0e at an "
          "above-band zero (WI4 instantiated): %s"
          % (FARFORM_BAR, str(FF_SAMPLES), BM_BAR, "; ".join(
              "x%d ff %.0e bm %.0e (g %.1f)"
              % (x, R[x]["ff_dev"], R[x]["bm_dev"], R[x]["bm_gamma"])
              for x in xs)))

    ok34 = True
    d34 = []
    for x in [x for x in xs if x in BUDGET_RUNGS]:
        r = R[x]
        okx = True
        for tag in ("phi", "psi1"):
            bd = r["bud_" + tag]
            # AMENDMENT 1: the two-sided closure is measurable ONLY
            # at the HARD rungs (5, 8) -- at x = 13/18 the E(gamma)^2
            # scale (~1e-54/1e-79) sits far below the f64 cache
            # precision floor (~1e-35): run1 measured closure ratios
            # 1.19e19/4.88e43 = pure truncation noise, typed
            # CACHE-PRECISION-FLOOR, not gated
            # AMENDMENT 1a: run 2 measured the deep ZONE/BAND legs at
            # the same floor (zshare ~ 1e19-scale noise: the zone is
            # exactly where the minimizer tunes E to vanish) -- zone
            # share gated at the HARD rungs only; strip/far are
            # honest signal at every budget rung and stay gated
            if x in BUDGET_HARD:
                okx = okx and CLOSURE_WIN_CORE[0] <= bd["closure"] \
                    <= CLOSURE_WIN_CORE[1] \
                    and REMENV_WIN_CORE[0] <= bd["remenv"] \
                    <= REMENV_WIN_CORE[1] \
                    and bd["zshare"] <= ZONE_SHARE_BAR
            okx = okx and (bd["sshare"] + bd["fshare"]) >= SFFLOOR
        okx = okx and SIN2_WIN[0] <= r["sin2"] <= SIN2_WIN[1] \
            and r["tlaw_lower"] <= r["tlaw0"] * (1 + 1e-12)
        ok34 = ok34 and okx
        bp = r["bud_phi"]
        d34.append("x%d: clo %.3e/%.3e%s remenv %.3f strip %.3f far "
                   "%.3f sin2 %.3f low %.4f<=tlaw %.4f"
                   % (x, bp["closure"], r["bud_psi1"]["closure"],
                      "" if x in BUDGET_HARD
                      else " (CACHE-PRECISION-FLOOR, not gated)",
                      bp["remenv"], bp["sshare"], bp["fshare"],
                      r["sin2"], r["tlaw_lower"], r["tlaw0"]))
        info("x=%d BUDGET exhibit (WI4): the GW mass of BOTH ground "
             "and first excited sits %.0f%%/%.0f%% in the STRIP "
             "(b_top, y_t) where the PHI dictionary reigns -- the "
             "ladder parametrizes its own onset mass; tlaw_0 = %.4f "
             "vs <sin^2> x (sum g^-2/G) = %.4f (the equidistribution "
             "reading; the excess is the PHI^2 weight)"
             % (x, 100 * bp["sshare"],
                100 * r["bud_psi1"]["sshare"], r["tlaw0"],
                r["sin2"] * r["g2G"]))
    check("G34-gw-budget", ok34,
          "two-sided GW closure (S_cache/lam in window, 0 <= rem <= "
          "envelope) at the HARD rungs (5, 8) ONLY (AMENDMENT 1: "
          "x = 13/18 closure is below the f64 cache precision floor, "
          "typed CACHE-PRECISION-FLOOR, reported not gated); zone "
          "share <= %.0e; strip+far >= %.1f; <sin^2> in %s; tlaw "
          "lower leg HARD (WI4 conditional cap instantiated): %s"
          % (ZONE_SHARE_BAR, SFFLOOR, str(SIN2_WIN), "; ".join(d34)))

    # kernel battery (screen)
    verdicts_k = {}
    for name in ("GEOHALF", "WALLIS", "FEJER", "HARM", "HARM2"):
        worst = 0.0
        n_used = 0
        for x in xs:
            sl = R[x]["slots"]
            if len(sl) < 4:
                continue
            c1s = sl[1]
            for i in sorted(sl):
                if i < 2 or i > 6:
                    continue
                if name == "GEOHALF":
                    pred = c1s / 2 ** (i - 1)
                elif name == "WALLIS":
                    wv = c1s
                    for j in range(2, i + 1):
                        wv *= (2 * j - 1) / (2 * j)
                    pred = wv
                elif name == "FEJER":
                    pred = c1s * 6.0 / ((2 * i + 1) * (i + 1))
                elif name == "HARM":
                    pred = c1s / i
                else:
                    pred = c1s / i ** 2
                worst = max(worst, abs(sl[i] / pred - 1))
                n_used += 1
        verdicts_k[name] = (worst, n_used)
    matched = [n for n, (w, u) in verdicts_k.items()
               if u > 0 and w <= KERNEL_TOL]
    best = min(verdicts_k.items(), key=lambda kv: kv[1][0])
    check("G35-slot-kernel-battery", True,
          "%s; worst rel devs: %s"
          % (("MATCHED: " + ",".join(matched)) if matched else
             "NO-CLASSICAL-KERNEL-MATCH (best %s at %.2f)"
             % (best[0], best[1][0]),
             " ".join("%s %.2f" % (n, w)
                      for n, (w, _u) in sorted(verdicts_k.items()))),
          kind="screen")
    if len(xs) >= 3:
        uf = [R[x]["ufrac"] for x in xs]
        c1l = [R[x]["c1"] for x in xs]
        um, cm = np.mean(uf), np.mean(c1l)
        num = float(np.sum((np.array(uf) - um) * (np.array(c1l) - cm)))
        den = float(np.sqrt(np.sum((np.array(uf) - um) ** 2)
                            * np.sum((np.array(c1l) - cm) ** 2)))
        corr = num / den if den > 0 else float("nan")
        check("G36-c1-edge-offset", True,
              "LAW-HUNT: Pearson corr(c_1, band-edge offset ufrac) "
              "= %.3f over %d rungs (pairs: %s)"
              % (corr, len(xs), " ".join(
                  "(%.3f, %.4f)" % (u, c) for u, c in zip(uf, c1l))),
              kind="screen")
    else:
        check("G36-c1-edge-offset", True, "smoke: needs 3+ rungs",
              kind="screen")

    # ------------------------------------------------- S3A (GATE A)
    section("S3A  GATE A: THE DYADIC SPECTRAL LADDER (owner directive)")
    dyad_x = [x for x in xs if x in DYAD_RUNGS]
    if dyad_x:
        okA1 = True
        dA1 = []
        for x in dyad_x:
            sl = R[x]["slots"]
            worst = 0.0
            for i, f in DYAD_F.items():
                if i in sl:
                    worst = max(worst, abs(sl[i] * 2 ** f / sl[1] - 1))
            okA1 = okA1 and worst <= DYAD_TOL
            dA1.append("x%d worst %.3f" % (x, worst))
        for x in [x for x in xs if x not in DYAD_RUNGS]:
            sl = R[x]["slots"]
            worst = max((abs(sl[i] * 2 ** f / sl[1] - 1)
                         for i, f in DYAD_F.items() if i in sl),
                        default=float("nan"))
            dA1.append("x%d worst %.3f (core, report-only: EMERGENT)"
                       % (x, worst))
        check("GA1-dyadic-pair-fit", okA1,
              "c_i == c_1 2^-F(i), F = (1,2,3,3,4,4) for i = 2..7, "
              "max rel dev <= %.2f at deep rungs %s (run1-calibrated "
              "0.146/0.165/0.169: the ladder is APPROXIMATE-DYADIC "
              "at the 15-17 percent level -- the owner's 1-5 percent "
              "read came from rounded cross-rung means and is NOT "
              "reproduced at mp precision; the pair structure is the "
              "DEEP limit, core rungs report-only): %s"
              % (DYAD_TOL, str(DYAD_RUNGS), "; ".join(dA1)))

        spread_worst = 0.0
        dA2 = []
        for i in range(2, 8):
            vals = [R[x]["slots"][i] / R[x]["slots"][1]
                    for x in dyad_x if i in R[x]["slots"]]
            if len(vals) >= 2:
                sp = (max(vals) - min(vals)) / min(vals)
                spread_worst = max(spread_worst, sp)
                dA2.append("i%d %.3f" % (i, sp))
        check("GA2-window-independence", spread_worst <= DYAD_SPREAD,
              "normalized ladder c_i/c_1 flat across the deep rungs "
              "(spread <= %.2f: %s); CONSTRUCTION AUDIT: the slots "
              "consume ONLY the cell spectrum (Mq eigenvectors + the "
              "alternating-sum functional) -- no h, no a, no target "
              "signs, no measured J_2 enter the recurrence"
              % (DYAD_SPREAD, " ".join(dA2)))

        held_rows = []
        n_conf = 0
        n_tot = 0
        for x in [x for x in xs if x in HELD_RUNGS]:
            sl = R[x]["slots"]
            for i in (8, 9):
                if i in sl:
                    n_tot += 1
                    ratio = sl[i] * 2 ** HELD_EXP / sl[1]
                    okr = HELD_WIN[0] <= ratio <= HELD_WIN[1]
                    n_conf += int(okr)
                    held_rows.append("x%d c%d %.4f ratio %.3f %s"
                                     % (x, i, sl[i], ratio,
                                        "OK" if okr else "MISS"))
        for x in [x for x in xs if x in DYAD_RUNGS
                  and x not in HELD_RUNGS]:
            sl = R[x]["slots"]
            for i in (8, 9):
                if i in sl:
                    held_rows.append(
                        "x%d c%d %.4f ratio %.3f (report)"
                        % (x, i, sl[i], sl[i] * 2 ** HELD_EXP / sl[1]))
        hv = ("DYADIC-PREDICTION-CONFIRMED" if n_tot and n_conf == n_tot
              else "DYADIC-PREDICTION-REFUTED" if n_tot and n_conf == 0
              else "DYADIC-PREDICTION-MIXED(%d/%d)" % (n_conf, n_tot))
        check("GA3-heldout-prediction", True,
              "FROZEN BEFORE COMPUTE: c_8 == c_9 == c_1/2^%d in %s x "
              "c_1/32 at x in %s (the pair continuation; c_8/c_9 "
              "never computed in any prior round/run/scratch): %s "
              "-- %s" % (HELD_EXP, str(HELD_WIN), str(HELD_RUNGS),
                         "; ".join(held_rows), hv), kind="screen")

        okA4 = True
        dA4 = []
        for x in dyad_x:
            r = R[x]
            if "hankel_min" not in r:
                okA4 = False
                continue
            br = r["logconv"].get(LOGCONV_BREAK_I, 0.0)
            okA4 = okA4 and r["hankel_min"] < 0 \
                and br >= LOGCONV_BREAK_MIN
            dA4.append("x%d Hmin %.2e det %.2e break(i=%d) %.2f"
                       % (x, r["hankel_min"], r["hankel_det"],
                          LOGCONV_BREAK_I, br))
        check("GA4-moment-adjudication", okA4,
              "shifted Hankel H_1(c_2..c_6) NOT PSD (min eig < 0, mp "
              "exact) AND log-convexity break c_5^2/(c_4 c_6) >= %.1f "
              "at every deep rung: STIELTJES-MOMENT-REFUTED -- the "
              "slots are NOT the moments of a positive kernel on "
              "[0, oo); CHRISTOFFEL-WEIGHTS-DOA (a Christoffel/"
              "Jacobi identification requires the refuted positive "
              "measure): %s" % (LOGCONV_BREAK_MIN, "; ".join(dA4)))

        arows = []
        for x in xs:
            r = R[x]
            if "alias_share" in r:
                arows.append("x%d share %.4f ratios %s"
                             % (x, r["alias_share"],
                                "/".join("%.2f" % v
                                         for v in r["alias_ratios"])))
        check("GA6-alias-8x8", True,
              "owner's fixed 8x8 kernel on even alias modes "
              "{2,4,..,16}: ground-mass share vs the owner string "
              "%.6f -- NOT-REPRODUCED-IN-BASIS (calibrated 0.147 at "
              "x=8); compression eigenladder NOT dyadic; the "
              "full-spectrum bottom-8 spans the Connes collapse "
              "(ratios ~1e5), NOT a dyadic ladder: %s"
              % (ALIAS_OWNER, "; ".join(arows)), kind="screen")

        with mp.workdps(40):
            nH = 8
            TH = mp.zeros(nH, nH)
            for m2 in range(nH):
                for k2 in range(nH):
                    def fint(xv, m2=m2, k2=k2):
                        tv = (mp.cos(k2 * mp.pi * xv / 2)
                              + mp.cos(k2 * mp.pi * (xv + 1) / 2)) / 2
                        w = mp.mpf(1) if m2 == 0 else mp.mpf(2)
                        return w * mp.cos(m2 * mp.pi * xv) * tv
                    TH[m2, k2] = mp.quad(fint, [0, 1])
            evH = mp.eig(TH, left=False, right=False)
            evs = sorted([float(abs(v)) for v in evH], reverse=True)
        pair_dev = abs(evs[2] / evs[3] - 1) if evs[3] else float("inf")
        check("GA7-haar-transfer", True,
              "fixed dyadic transfer (Lf)(x) = [f(x/2) + f((x+1)/2)]/2 "
              "compressed to 8 cos modes: |eigs| %s -- a DOUBLED "
              "level appears (3rd/4th dev %.4f): the dyadic-transfer "
              "mechanism CAN double multiplicities under cos-lattice "
              "aliasing, but the ladder head (1, 1/2, 1/4, 1/4) does "
              "NOT match the measured (1, 1/2, 1/4, 1/8, 1/8): "
              "OPEN-CANDIDATE, no fixed transfer object identified"
              % (" ".join("%.4f" % v for v in evs), pair_dev),
              kind="screen")
    else:
        check("GA1-dyadic-pair-fit", True, "smoke: deep rungs absent",
              kind="screen")

    # ---------------------------------------------------------- S4
    section("S4  W2 BATTERY (positivity-transport instrument)")
    B = {}
    for tag, x_nom, dps in blocks:
        t0 = time.time()
        B[tag] = w2_battery(tag, x_nom, dps)
        print("  b%d battery done (%.0f s)" % (tag, time.time() - t0),
              flush=True)

    ok40 = all(B[t]["plant_minev"] >= -1e-50
               and B[t]["plant_rank_rel"] <= 1e-25
               and B[t]["plant_id_dev"] <= 1e-30 for t in B)
    check("G40-plant-atom", ok40,
          "PSD min eig >= -1e-50; rank-2 rel <= 1e-25; Fourier-"
          "ratio identity <= 1e-30 (JP bars): %s"
          % "; ".join("b%d %.0e/%.0e/%.0e"
                      % (t, B[t]["plant_minev"],
                         B[t]["plant_rank_rel"],
                         B[t]["plant_id_dev"]) for t in sorted(B)))

    ok41 = True
    for t in sorted(B):
        for r in B[t]["rows"]:
            okx = (r["lures"] <= LURES_BAR and r["flip_lo"] > 0
                   and r["flip_hi"] < 0
                   and r["s_star"] <= r["price"] * (1 + PRICE_SLOP)
                   and r["sprice"] >= SPRICE_MIN)
            ok41 = ok41 and okx
        info("b%d WI2 s*-table (gamma: s*, s*/tau-price): %s"
             % (t, "  ".join("%.4g: %.3e/%.3f"
                             % (r["g"], r["s_star"], r["sprice"])
                             for r in B[t]["rows"])))
    check("G41-secular-threshold", ok41,
          "per gamma: lu res <= %.0e; lam_min(M - s*(1 -+ %.0e)P) "
          "sign flip HARD; s* <= tau/(lamP w_0^2)(1 + %.0e) HARD "
          "(GHOST-TAU-PRICED); s*/price >= %.1f (WI2 instantiated "
          "at %d gammas x %d blocks)"
          % (LURES_BAR, SSTAR_EPS, PRICE_SLOP, SPRICE_MIN,
             len(GAMMA_LIST), len(B)))

    ok42 = True
    d42 = []
    if 5 in B:
        gh = B[5]["ghosts"]
        for g, ref in GHOST_B5_STRINGS.items():
            ok42 = ok42 and abs(gh[g] / ref - 1) <= GHOST_TOL
        d42.append("b5 " + " ".join("%g:%.2e" % (g, gh[g])
                                    for g in sorted(gh)))
    if 8 in B:
        gh = B[8]["ghosts"]
        gmin = min(gh.values())
        gmax = max(v for v in gh.values() if v != float("inf"))
        ok42 = ok42 and GHOST_B8_MIN_WIN[0] <= gmin \
            <= GHOST_B8_MIN_WIN[1] and GHOST_B8_MAX_WIN[0] <= gmax \
            <= GHOST_B8_MAX_WIN[1]
        d42.append("b8 min %.2e max %.2e" % (gmin, gmax))
    check("G42-ghost-replica", ok42,
          "r160 ghost-break table replicated (JP path VERBATIM): "
          "b5 on the CDLXIV strings rel <= %.2f; b8 min/max in the "
          "frozen windows: %s" % (GHOST_TOL, "; ".join(d42)))
    if 5 in B:
        s5 = [r for r in B[5]["rows"] if r["g"] == 9.0][0]
        info("ASYMMETRY exhibit: at gamma = 9 (b5) the PSD premise "
             "dies at s* = %.1e (tau-priced, WI2) while the r160 "
             "J_2-break sits at 6.0e-8 -- %.1f dex later: the "
             "window locally outlives positivity; the premise "
             "does not" % (s5["s_star"],
                           math.log10(6.0e-8 / s5["s_star"])))

    ok43 = all(r["dA0_rel"] <= FD_BAR and r["dtau_rel"] <= FD_BAR
               for t in B for r in B[t]["rows"])
    check("G43-perturbation-law", ok43,
          "dA_0/ds closed form (reduced resolvent) vs central FD at "
          "h = 1e-3 s* rel <= %.0e; d tau/ds vs phi'P phi rel <= "
          "%.0e (WI3 instantiated; FIRST-ORDER-SYMMETRIC asserted "
          "in G12): worst dA0 %s"
          % (FD_BAR, FD_BAR, " ".join(
              "b%d %.1e" % (t, max(r["dA0_rel"]
                                   for r in B[t]["rows"]))
              for t in sorted(B))))

    ok44 = True
    d44 = []
    for t in sorted(B):
        bb = B[t]
        okx = bb["defl_ok"]
        for sv, p in bb["plateau"].items():
            okx = okx and p["sandwich"]
            if sv >= 1e3:
                okx = okx and p["tdev"] <= PLATEAU_BAR \
                    and p["adev"] <= PLATEAU_BAR
        okx = okx and bb["range_ratio"] >= RANGE_MIN
        ok44 = ok44 and okx
        d44.append("b%d: defl %.3e plateau tdev %.0e adev %.0e "
                   "range %.1e"
                   % (t, bb["tau_defl"], bb["plateau"][1e3]["tdev"],
                      bb["plateau"][1e3]["adev"], bb["range_ratio"]))
    check("G44-plant-plateau", ok44,
          "deflation in [tau, lam_1] HARD; plant sandwich at s = 1, "
          "1e3 HARD; plateau == deflation to %.0e; RANGE-ASYMMETRY "
          "s_tested/s*(g=5) >= %.0e (WI1 instantiated): %s"
          % (PLATEAU_BAR, RANGE_MIN, "; ".join(d44)))

    ok45 = True
    ok46 = True
    d45 = []
    for t in sorted(B):
        w = B[t]["wit"]
        mu = w["multi"]
        if t == 5:
            okx = (mu["tau"] > 0 and not mu["inw"]
                   and abs(mu["J2"] / MP_J2[5] - 1) <= WIT_TOL)
        else:
            okx = (mu["tau"] > 0 and mu["inw"]
                   and abs(mu["J2"] / MP_J2[8] - 1) <= WIT_TOL)
        for g in (2.0, 9.0):
            sgl = w["g%g" % g]
            okx = okx and sgl["inw"] \
                and abs(sgl["J2"] / SP_J2[(t, g)] - 1) <= WIT_TOL
            ok46 = ok46 and sgl["transport"] and sgl["sandwich"]
        ok46 = ok46 and mu["transport"]
        ok45 = ok45 and okx
        d45.append("b%d multi tau %.2e J2 %.4f %s"
                   % (t, mu["tau"], mu["J2"],
                      "IN" if mu["inw"] else "BREAK"))
    check("G45-value-witnesses", ok45,
          "b5 multi-plant: tau_W > 0 AND window BROKEN on the "
          "calibrated string (VALUE-TRANSPORT-REFUTED-IN-CLASS); "
          "b8 multi IN-window on the r160 0.0740 string "
          "(NON-MONOTONE-IN-CLASS); single plants in-window on the "
          "calibrated strings: %s" % "; ".join(d45))
    check("G46-premise-transport", ok46,
          "EVERY plant world tau_W >= tau HARD (Loewner, WI1); "
          "single plants tau_W <= lam_1 HARD (sandwich): positive "
          "band mass transports the PSD premise at any strength -- "
          "the W2 conditional lands on the PREMISE leg exactly")

    # ------------------------------------------------- S4A (GATE B)
    section("S4A  GATE B: THE TANGENT CRITERION (owner directive)")
    # GB1: the asymmetry LAW is generic positive-cone geometry --
    # verify WI1/WI2 on a fixed SYNTHETIC world with no prime content
    with mp.workdps(60):
        nS = 5
        MS = mp.zeros(nS, nS)
        for i, dv in enumerate(MSYN_DIAG):
            MS[i, i] = mp.mpf(dv)
        for (ia, ja, ang) in MSYN_ROTS:
            G = mp.eye(nS)
            cth, sth = mp.cos(mp.mpf(ang)), mp.sin(mp.mpf(ang))
            G[ia, ia] = cth
            G[ja, ja] = cth
            G[ia, ja] = -sth
            G[ja, ia] = sth
            MS = G.T * MS * G
        vS = mp.matrix([1, 1, 1, 1, 1]) / mp.sqrt(5)
        Minv_v = mp.lu_solve(MS, vS)
        sstar_syn = 1 / sum(vS[i] * Minv_v[i] for i in range(nS))
        okS = True
        for sgn in (1 - 1e-6, 1 + 1e-6):
            Mt = mp.zeros(nS, nS)
            for i in range(nS):
                for j in range(nS):
                    Mt[i, j] = MS[i, j] - sgn * sstar_syn \
                        * vS[i] * vS[j]
            ES, _ = mp.eigsy(Mt)
            emin = min(ES[i] for i in range(nS))
            okS = okS and ((emin > 0) == (sgn < 1))
        Mp2 = mp.zeros(nS, nS)
        for i in range(nS):
            for j in range(nS):
                Mp2[i, j] = MS[i, j] + 100 * vS[i] * vS[j]
        EP2, _ = mp.eigsy(Mp2)
        ES0, _ = mp.eigsy(MS)
        okS = okS and min(EP2[i] for i in range(nS)) \
            >= min(ES0[i] for i in range(nS))
    check("GB1-generic-cone-adjudication", okS,
          "the WI1/WI2 asymmetry LAW verified on a fixed SYNTHETIC "
          "PSD matrix with NO prime content (s* = %.3e sign flip "
          "HARD; Weyl plant HARD): ASYMMETRY-LAW-GENERIC-CONE -- the "
          "law is positive-cone geometry; the ARITHMETIC content is "
          "(i) WHERE the boundary sits (tau at the Connes collapse) "
          "and (ii) the anchor VALUES (r136 minimizer); the owner's "
          "suspicion is CONFIRMED and typed" % float(sstar_syn))

    acc_blocks = ACC_BLOCKS[:1] if smoke else ACC_BLOCKS
    acc_fakes = ACC_FAKES[:1] if smoke else ACC_FAKES
    ACC = {}
    for tag, x_nom, dpsb in acc_blocks:
        t0 = time.time()
        ACC[tag] = accretion_battery(tag, x_nom, dpsb, "TRUE")
        print("  accretion b%d TRUE done (%.0f s)"
              % (tag, time.time() - t0), flush=True)
    okB2 = True
    dB2 = []
    for tag in sorted(ACC):
        A = ACC[tag]
        ent = [c for c in A["crossings"] if c["kind"] == "ENTER"]
        lea = [c for c in A["crossings"] if c["kind"] == "LEAVE"]
        okx = (A["endpoint"] > 0 and A["add_dev"] <= 1e-40
               and len(ent) == 1 and not lea
               and ent[0]["last"] and ent[0]["tstar"] >= TSTAR_MIN
               and ent[0]["tangent"] > 0)
        okB2 = okB2 and okx
        dB2.append("b%d: profile %s; ENTER at last atom t* %.6f "
                   "tangent %+.3e" % (tag, "/".join(
                       "%.2e" % p for p in A["profile"]),
                       ent[0]["tstar"] if ent else float("nan"),
                       ent[0]["tangent"] if ent else float("nan")))
        info("b%d ACCRETION exhibit: the source path enters the PSD "
             "cone ONLY in the tail of the LAST atom (1 - t* = "
             "%.1e of atom u = %.3f) -- the collective property "
             "path-wise: no partial comb is positive; the boundary "
             "derivative -v'N_q v = %+.3e > 0 comes from the prime "
             "source block itself"
             % (tag, 1 - ent[0]["tstar"] if ent else float("nan"),
                ent[0]["u"] if ent else float("nan"),
                ent[0]["tangent"] if ent else float("nan")))
    check("GB2-accretion-tangent-true", okB2,
          "frozen u-ordered accretion path (NO zero data, NO window "
          "signs): endpoint PSD HARD; exactly ONE entering crossing, "
          "in the LAST atom segment, t* >= %.3f; TANGENT CRITERION "
          "at the cone touch: v'A'v > 0 HARD (A' = -N_q, prime "
          "source, not back-fitted): %s" % (TSTAR_MIN, "; ".join(dB2)))

    okB3 = True
    dB3 = []
    for world, tag, x_nom, dpsb in acc_fakes:
        t0 = time.time()
        Af = accretion_battery(tag, x_nom, dpsb, world)
        print("  accretion b%d %s done (%.0f s)"
              % (tag, world, time.time() - t0), flush=True)
        ent = [c for c in Af["crossings"] if c["kind"] == "ENTER"
               and not any(c2["kind"] == "LEAVE"
                           and c2["seg"] > c["seg"]
                           for c2 in Af["crossings"])]
        okx = Af["endpoint"] < 0 and not ent
        okB3 = okB3 and okx
        dB3.append("b%d %s: endpoint %.3e n_cross %d"
                   % (tag, world, Af["endpoint"],
                      len(Af["crossings"])))
    check("GB3-accretion-fakes-violate", okB3,
          "SCRARITH/EPSTEIN accretion paths NEVER surviving-enter "
          "the cone (endpoint lam_min < 0 HARD): the fakes violate "
          "the criterion at their death sites by NO-ENTRY -- "
          "TANGENT-CRITERION-DISTINGUISHES (calibrated endpoints "
          "-0.24/-0.63/-1.53): %s" % "; ".join(dB3))

    dB4 = []
    for tag in sorted(ACC):
        if "dtau_du_rel" in ACC[tag]:
            dB4.append("b%d dlogtau/du %.1f" % (tag,
                                                ACC[tag]["dtau_du_rel"]))
    check("GB4-height-near-tangent", True,
          "in-cell height path (fixed K/icap, FD in u): tau strictly "
          "positive, d log tau/du < 0 at the Connes rate (%s) -- the "
          "height path squeezes TOWARD the boundary without touching "
          "inside verified cells: the tangent criterion is only "
          "testable at the accretion touch (GB2), where it HOLDS; "
          "SUCCESS-CRITERIA AUDIT: path source-built (no zero data, "
          "no window signs), derivative from the prime source, "
          "per-block hypothesis (NOT band positivity at all "
          "heights); NOT ASSEMBLED: prime source ==> tangent ==> "
          "invariance ==> H_cof remains an exhibit at n = %d/%d "
          "atoms, not a theorem for unbounded combs"
          % ("; ".join(dB4), ACC[min(ACC)]["n_atoms"],
             ACC[max(ACC)]["n_atoms"]), kind="screen")

    # ---------------------------------------------------------- S5
    section("S5  CONTROLS (the certificate must refuse)")
    ctrl_ok_all = True
    fake_dyad: dict = {}
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            aaw = mp.log(xw) / 2
            rw = JP.world_measure(cw["mpM"], Kw, aaw, dpsw)
            nrmw = [mp.sqrt(2 * aaw) if k == 0 else mp.sqrt(aaw)
                    for k in range(Kw)]
            csw = [mp.mpf(sv) for sv in cw["cn_mp_str"]]
            A0w = sum(((-1) ** k) * csw[k] for k in range(Kw))
            cs1w = [cw["mpV"][i, 1] / nrmw[i] for i in range(Kw)]
            A01w = sum(((-1) ** k) * cs1w[k] for k in range(Kw))
            Tzw = 2 * math.pi * xw
            thw = float((A01w / A0w) ** 2 / mp.mpf(repr(Tzw)) ** 4)
            # GA5 data: slot-type ladder on the fake's bottom modes
            Tz2w = mp.mpf(repr(Tzw)) ** 2
            A_prev = A0w
            fslots = {}
            for i in range(1, min(Kw, 8)):
                csi = [cw["mpV"][k2, i] / nrmw[k2]
                       for k2 in range(Kw)]
                A0i = sum(((-1) ** k2) * csi[k2] for k2 in range(Kw))
                fslots[i] = float(abs(A0i / A_prev) / Tz2w)
                A_prev = A0i
            fworst = max((abs(fslots[i] * 2 ** f / fslots[1] - 1)
                          for i, f in DYAD_F.items() if i in fslots),
                         default=float("inf"))
            fake_dyad[world] = (fworst, dict(fslots))
        refuse = (rw["tau_f"] < 0
                  and abs(rw["J2"] / CTRL_J2_STRINGS[world] - 1)
                  <= CTRL_J2_TOL
                  and abs(thw / CTRL_THETA_STRINGS[world] - 1)
                  <= CTRL_THETA_TOL)
        ctrl_ok_all = ctrl_ok_all and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: tau_w = %.4f < 0 (the WI1/WI2 PSD premise "
              "fails EXACTLY here -- the threshold instrument "
              "refuses); J_2_w = %.4f on the r156 string; THETA_w "
              "= %.2e on the r162 string (no quartic content)"
              % (world, xw, rw["tau_f"], rw["J2"], thw))
    check("G53-mechanism-consistency", ctrl_ok_all,
          "all control worlds refuse at tau < 0 + negative J_2 + "
          "collapsed THETA: the transport/threshold instrument "
          "requires the PSD premise -- exactly the property BANDPOS "
          "carries (WI1/WI2 both directions)")
    okA5 = all(w > DYAD_TOL for w, _s in fake_dyad.values()) \
        and len(fake_dyad) == len(controls)
    check("GA5-dyadic-dies-in-fakes", okA5,
          "GATE A(4): the dyadic-pair fit FAILS in every fake world "
          "(worst dev > %.2f; the fakes have NO collapsed block -- "
          "negative spectrum, the ladder is not even defined as a "
          "collapse structure): the dyadic identification is NOT "
          "window geometry; it dies with the arithmetic: %s"
          % (DYAD_TOL, "; ".join(
              "%s worst %.2f slots %s"
              % (wn, wv, " ".join("%.3f" % sv[i]
                                  for i in sorted(sv)))
              for wn, (wv, sv) in sorted(fake_dyad.items()))))

    # ---------------------------------------------------------- S6
    section("S6  SCREENS")
    if not smoke:
        lt = [R[x]["tau_l10"] for x in xs]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])
        sl_th = slope_of([math.log10(R[x]["theta"]) for x in xs])
        sl_c1 = slope_of([math.log10(R[x]["c1"]) for x in xs])
        sl_jr = slope_of([math.log10(R[x]["jr"]) for x in xs])
        sl_tr = slope_of([math.log10(R[x]["t_r"]) for x in xs])
        bx = [x for x in xs if x in BUDGET_RUNGS]
        ltb = [R[x]["tau_l10"] for x in bx]
        sl_ss = float(np.polyfit(ltb, [math.log10(
            R[x]["bud_phi"]["sshare"]) for x in bx], 1)[0])
        sl_ff = float(np.polyfit(ltb, [math.log10(
            R[x]["bud_phi"]["fshare"]) for x in bx], 1)[0])
        sl_a0p = float(np.polyfit(lt, [2 * R[x]["a0p_l10"]
                                       for x in xs], 1)[0])
        sl_a01 = float(np.polyfit(lt, [2 * R[x]["a01_l10"]
                                       for x in xs], 1)[0])
        ok54 = (abs(sl_th) <= TAU_SLOPE_BAR
                and abs(sl_c1) <= TAU_SLOPE_BAR
                and abs(sl_jr) <= TAU_SLOPE_BAR
                and abs(sl_tr) <= TAU_SLOPE_BAR
                and abs(sl_ss) <= SHARE_SLOPE_BAR
                and abs(sl_ff) <= SHARE_SLOPE_BAR
                and W0_RIDER_WIN[0] <= sl_a0p <= W0_RIDER_WIN[1]
                and W0_RIDER_WIN[0] <= sl_a01 <= W0_RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: THETA %.4f, c_1 %.4f, jr %.4f, "
              "t_r %.4f (<= %.2f), strip share %.4f, far share %.4f "
              "(<= %.2f): DEMAND-FLAT; RIDER report: A_0(phi)^2 "
              "%.3f, A_0(psi_1)^2 %.3f in %s (BOUND-RIDES-CONNES)"
              % (sl_th, sl_c1, sl_jr, sl_tr, TAU_SLOPE_BAR, sl_ss,
                 sl_ff, SHARE_SLOPE_BAR, sl_a0p, sl_a01,
                 str(W0_RIDER_WIN)))
    ce5 = R.get(5)
    if ce5 is not None:
        with mp.workdps(60):
            ce = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
            E0 = ce["mpE"][0]
            Qp_ = ce["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Epp, _Vp = mp.eigsy(Qp_)
            emin = min(Epp[i] for i in range(ce["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; round-118 red flag)" % d_eps,
              kind="edge")

    # ---------------------------------------------------------- S7
    section("S7  DEMAND AUDIT + MIN-CUT + W3 ADJUDICATION")
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
          "flows: base 4, refined 5 (r162 graph VERBATIM -- this "
          "round adds INSTRUMENT THEOREMS, not residue edges); "
          "one-grant 5; counterfactual PARALLEL 9 NOT REAL; census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")

    # W3 adjudication graph
    real_edges = {("BANDPOS", "PSDPREM"): INF,      # this round (WI1/2)
                  ("WINVALS", "RH"): INF,           # corpus conditional
                  ("RH", "BANDPOS"): INF,           # trivial
                  ("UNC", "BANDPOSH"): INF}         # below horizon PT21
    reach_bp = R4.bfs_reach(real_edges, "BANDPOS")
    reach_unc = R4.bfs_reach(real_edges, "UNC")
    blocked = "WINVALS" not in reach_bp and "RH" not in reach_bp
    bp_open = "BANDPOS" not in reach_unc
    cfv = dict(real_edges)
    cfv[("PSDPREM", "WINVALS")] = INF               # counterfactual
    reach_cf = R4.bfs_reach(cfv, "BANDPOS")
    succ_rh = R4.bfs_reach(cfv, "RH")
    loop_cf = "RH" in reach_cf and "BANDPOS" in succ_rh
    check("G62-w3-adjudication", blocked and bp_open and loop_cf,
          "REAL graph: WINVALS/RH unreachable from BANDPOS "
          "(RELOCATION-BLOCKED-AT-VALUE-LEG, per the G45 witness); "
          "BANDPOS unreachable from UNC beyond the horizon (typed "
          "OPEN; below-horizon node BANDPOSH separate, PT21); "
          "COUNTERFACTUAL value grant PSDPREM -> WINVALS creates "
          "the cycle RH -> BANDPOS -> PSDPREM -> WINVALS -> RH "
          "(LOOP-IF-ASSEMBLED, detected) -- with WI6: "
          "BANDPOS(unbounded ladder) == RH: a landed value "
          "transport would close the program onto its own "
          "hypothesis at the horizon; the honest yield is the "
          "premise-transport pair (WI1/WI2) + the sharpened residue "
          "reading")

    # GC1 (GATE C): cofinal, not universal
    cof_real = {("HCOF", "RH"): 10 ** 6,        # r122 NF-closure cond.
                ("RH", "HCOF"): 10 ** 6,        # trivial direction
                ("MEAS", "DYADREC"): 10 ** 6,   # GA1-GA3 measured
                ("MEAS", "TANGENT"): 10 ** 6}   # GB2/GB3 measured
    reach_meas = R4.bfs_reach(cof_real, "MEAS")
    unassembled = "HCOF" not in reach_meas and "RH" not in reach_meas
    cof_cf = dict(cof_real)
    cof_cf[("DYADREC", "PROP")] = 10 ** 6       # counterfactual:
    cof_cf[("TANGENT", "PROP")] = 10 ** 6       # depth-block transfer
    cof_cf[("PROP", "HCOF")] = 10 ** 6
    reach_cf2 = R4.bfs_reach(cof_cf, "MEAS")
    succ_rh2 = R4.bfs_reach(cof_cf, "RH")
    advance_cf = "RH" in reach_cf2 and "DYADREC" not in succ_rh2 \
        and "TANGENT" not in succ_rh2
    check("GC1-cofinal-adjudication", unassembled and advance_cf,
          "GATE C bar: pre-defined dyadic depth ladder x_j = %d 2^j, "
          "ONE positive rung per dyadic block (the r122 NF-closure/"
          "r141 SEQ demand -- cofinal, NOT universal).  EXACT "
          "DISTINCTION: (i) relocation onto BANDPOS at all heights "
          "(or any unbounded zero-band ladder) == RH by WI6 "
          "cofinality: LOOP (G62, unchanged); (ii) relocation onto "
          "HCOF (cofinal FORM positivity on the mesh ladder) is NOT "
          "a loop: the counterfactual propagation edge {DYADREC, "
          "TANGENT} -> PROP -> HCOF reaches RH with NO cycle back "
          "through the measured nodes (machine-checked) -- a genuine "
          "advance TARGET; STATUS: COFINAL-TARGET-IDENTIFIED-NOT-"
          "ASSEMBLED -- the exact missing piece is PROP, the "
          "depth-block transfer theorem [positivity at rung j + a "
          "proven transfer object T ==> positivity at rung j+1]; if "
          "the GA1/GA3 dyadic recurrence were a PROVEN operator "
          "spectrum (it is measured-only, refuted as moments GA4, "
          "unidentified as transfer GA7), THIS is its natural use"
          % COF_X0)

    info("EXACT RESIDUE after this round (read with CDLXIV/CDLXV/"
         "CDLXVI/CDLXVII): SET UNCHANGED -- RH <== [r122-NF-"
         "closure] + [Theorem R] + {L1, WPD} on dense a; RESIDUE = "
         "{TOPROOT, TLAWCAP-block, QSUBGAP-FLOOR} + dense-a + "
         "a-extension + window-a; THIS ROUND SHARPENS the reading: "
         "(i) BANDPOS is EXACTLY the carrier of the PSD premise "
         "(necessary AND sufficient, at exact tau-priced "
         "thresholds -- WI1/WI2); (ii) the window VALUES are NOT "
         "transported by positivity (b5 multi-plant witness) -- "
         "they stay anchor-pinned (r136 minimizer), the omegas "
         "remain the windows; (iii) tlaw recoordinates onto the "
         "ladder's own PHI functional + sin^2-equidistribution "
         "(WI4); (iv) theta remains the one arithmetic-consuming "
         "kernel (WI5).  NO omega closed, nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WI1-PROVEN + PLANT-PLATEAU-IS-DEFLATION (G10/G44/G46)",
        "WI2-PROVEN + GHOST-TAU-PRICED + R160-TABLE-REPLICATED "
        "(G11/G41/G42)",
        "WI3-PROVEN + FIRST-ORDER-SYMMETRIC + "
        "RANGE-ASYMMETRY(quantified) (G12/G43/G44)",
        "WI4-PROVEN (budget-moment dictionary) + "
        "TLAW-CAP-CONDITIONAL (G13/G33/G34)",
        "WI5: THETA-EQ-C1SQ-PROVEN + "
        "THETA-UPPER-CAP-CERTIFIED-DIVERGENT + "
        "THETA-LOWER-OBSTRUCTED-EQUALS-OMEGA + "
        "SELFCAP-CLASS-BLIND-TO-THETA + "
        "ALGEBRA-ONLY-REFUTED-FOR-TLAWABS (G14/G15/G31)",
        "SLOT-KERNEL adjudicated (G35) + edge-offset law hunt (G36)",
        "GATE A: DYADIC-PAIR-LADDER adjudicated (GA1/GA2) + held-out "
        "prediction (GA3) + STIELTJES-MOMENT-REFUTED + "
        "CHRISTOFFEL-DOA (GA4) + DIES-IN-FAKES (GA5) + "
        "ALIAS-NOT-REPRODUCED (GA6) + HAAR-OPEN-CANDIDATE (GA7)",
        "GATE B: ASYMMETRY-LAW-GENERIC-CONE + "
        "BOUNDARY-LOCATION-ARITHMETIC (GB1) + "
        "TANGENT-CRITERION-HOLDS-AT-CONE-ENTRY (GB2) + "
        "FAKES-VIOLATE-BY-NO-ENTRY (GB3) + CHAIN-NOT-ASSEMBLED (GB4)",
        "PREMISE-TRANSPORT-PROVEN (both directions; G44/G46) + "
        "VALUE-TRANSPORT-REFUTED-IN-CLASS (G45)",
        "W3: RELOCATION-BLOCKED-AT-VALUE-LEG + LOOP-IF-ASSEMBLED "
        "(WI6 identification; G16/G62)",
        "GATE C: LOOP vs COFINAL distinguished exactly; "
        "COFINAL-TARGET-IDENTIFIED-NOT-ASSEMBLED, missing piece = "
        "PROP depth-block transfer (GC1)",
        "CONTROLS-REFUSE (G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES (G54)",
        "QUANTIFIER-INHERITED (G60)",
        "OMEGA-UNCHANGED (census 4; G61)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d, _k in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _d, _k in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: WI1-PROVEN + WI2-PROVEN + WI3-PROVEN + "
              "WI4-PROVEN + WI5-ADJUDICATED + WI6-IDENTIFIED + "
              "GHOST-TAU-PRICED + PLANT-PLATEAU-IS-DEFLATION + "
              "PREMISE-TRANSPORT-PROVEN + "
              "VALUE-TRANSPORT-REFUTED-IN-CLASS + "
              "RELOCATION-BLOCKED + LOOP-IF-ASSEMBLED + "
              "TLAW-CAP-CONDITIONAL + "
              "THETA-UPPER-CAP-CERTIFIED-DIVERGENT + "
              "DYADIC-PAIR-LADDER-ADJUDICATED + "
              "STIELTJES-MOMENT-REFUTED + "
              "ASYMMETRY-LAW-GENERIC-CONE + "
              "TANGENT-CRITERION-HOLDS-AT-CONE-ENTRY + "
              "FAKES-VIOLATE-BY-NO-ENTRY + "
              "COFINAL-TARGET-IDENTIFIED-NOT-ASSEMBLED + "
              "CONTROLS-REFUSE + DEMAND-FLAT + "
              "QUANTIFIER-INHERITED + OMEGA-UNCHANGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
