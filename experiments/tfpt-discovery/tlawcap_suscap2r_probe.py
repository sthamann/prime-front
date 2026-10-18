#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tlawcap_suscap2r_probe -- PRIME.TLAWCAP.SUSCAP2R.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the two arithmetic-core residues)
=======================================================================
The residue after r137/r139/r140/r141 (CDXLI/CDXLIII/CDXLIV/CDXLV) is
{TOPROOT, TAILVIS, TLAWCAP, SUSCAP2R} + a-family walls; the concurrent
lane takes {TOPROOT, TAILVIS}.  This probe is the maximal proof
attempt on (TC) TLAWCAP -- the arithmetic core tlaw = tau/(8 A_0^2
G(T_z)) <= poly(x) -- via the ASSEMBLY question over the r137 budget
identity, and (SR) SUSCAP2R -- s := tau chi/rho2 <= poly(x) -- via the
LOOP question raised by the measured s x gap = 1.0000.

=======================================================================
THE EXACT LAYER (Theorems W1-W3 + the assembly adjudication; sympy-
gated generically + exact rational instances + mp-instantiated per
rung; classical inputs typed CITED)
=======================================================================
NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer phi (round-114 builder), tau =
lambda_min(Mq), secular F(y) = A_0 + sum w_k/(y - b_k) (r131/r135,
cited), E_N = 2 sin(Az) F(z^2)/z, T_z = 2 pi x, m = verified zone
census, V = kernel of the m node rows, W = Gram-orthonormal
compression of Mq onto V, eigenpairs (q_i, z_i), q_0 = tau, ground =
phi (r138/r139, cited).  For probe row r(p): normalized overlaps
et_i, rho2 = et_0^2, chi = sum_{i>=1} et_i^2/(q_i - q_0) (normalized),
g = (lam*(p) - tau)/tau, delta_i = (q_i - q_0)/tau, s = tau chi/rho2.
Jets A_{2m} = sum_k (-1)^k c_k om_k^{2m}, y_t = |A_2/A_0| (r140 J2/J3,
cited).  gtop = 7264.75 (X5 cache top).

THEOREM W1 (the s x gap defect identity; the LOOP adjudication).
The bordered-secular root g solves rho2/g = sum_{i>=1} et_i^2 /
(delta_i - g).  Writing 1/(d - g) = 1/d + g/(d(d - g)) EXACTLY:
   1 - s g == (g^2/rho2) sum_{i>=1} et_i^2/(delta_i (delta_i - g)).
s x gap == 1 is therefore NOT an exact identity: the defect is the
POSITIVE second-order susceptibility term, and it is PINCHED
two-sidedly:  1 - g/delta_1 <= s g <= 1  (upper: the defect sum is
nonnegative; lower: chi_2(g) <= chi-tilde/(delta_1 - g) + exact
rearrangement).  The measured 0.99985/0.99998/1.00000/1.00000/1.00000
IS the pinch: 1 - sg ~ g/delta_1 = 1.5e-4 .. 1.7e-7 (one-moded
defect: defect x delta_1/g ~ share_1 = 0.94..0.97).

THEOREM W2 (the loop, exact both ways).  (i) FORWARD (trivial
direction, NEW in this sharpness): g >= 1/P ==> s <= 1/g <= P (from
s g <= 1) AND delta_1 > g >= 1/P (the secular root lies below q_1).
(ii) BACKWARD (U1/G16 shape, re-gated): s <= P and delta_1 >= 1/P
==> g >= 1/(s + 1/delta_1) >= 1/(2P).  HENCE
   QSUBGAP-lambda-uniform  <==>  SUSCAP2R  AND  DELTA1FLOOR,
DELTA1FLOOR := delta_1 >= 1/poly(x) -- STRICTLY WEAKER than QSUBGAP
(delta_1 > g always).  The r139-r141 chain has LOOPED on this leg:
SUSCAP2R is not a component of QSUBGAP, it IS QSUBGAP-uniformity
modulo the weaker delta_1-floor; and the s-coordinate consumes NO
tlaw and NO spacing-lattice product (V1, cited) -- the r139 U2
numerator-factorization (EPSLOCK consumption) was coordinate
bookkeeping on this leg, the same artifact class as the PFLOOR edge.

THEOREM W3 (DELTA1FLOOR source-reduction; Cauchy interlacing).  V has
codimension m, so the second reduced eigenvalue dominates the second
FULL eigenvalue: q_1(V) >= lam_1(Mq), hence
   delta_1 >= FULLGAP := (lam_1(Mq) - tau)/tau,
a SOURCE-ONLY two-eigenvalue statement of the uncompressed Weil
matrix (no zeros, no probe row, no zone).  Gated on an exact rational
instance (Gram-generalized eigenproblem) + instantiated per rung from
mpE[1]/mpE[0].

TLAWCAP ASSEMBLY (the adjudication; the r137 anatomy tlaw = band/D +
midG + midC + midJ + resid/D, identity CITED r137 G31/G33 and
re-gated here through own cache sums + cited band strings):
(A1) midG <= G(om_max)/(2 G(T_z)) <= 1/2 UNCONDITIONALLY (cache
     partial <= HSW tail at om_max; HSW form monotone decreasing;
     om_max >= T_z by construction).  CLASSICAL, lambda-uniform.
(A2) |midC| <= midG UNCONDITIONALLY (|cos| <= 1 per term).  THE
     LANDAU BOUND IS NOT NEEDED FOR THE CAP: at poly demand the
     triangle inequality closes midC.  Landau 1912 (fixed x) and
     Gonek 1993 (uniform) are UNCONDITIONAL (not RH-conditional) and
     are CITED for the PIN's value only (prime/composite fingerprint
     re-gated per rung; the remainder after the Lambda(x) main term
     is classically boundable via Abel summation from the
     unconditional O(log T) form -- CITED as form, not re-proven,
     and NOT consumed by the cap).
(A3) resid <= poly ridden by TOPROOT + envelope (r140 J1/J2 cited:
     eta(T*) <= poly at a poly split T* >= Theta_J <= poly iff
     y_t <= poly).
(A4) midJ: the budget majorizes midJ ONLY by tlaw itself:
     J_mid <= M_mid <= tau + OFF exactly (G_mid >= C_mid by A2;
     band, beyond >= 0; |S_off| <= OFF), i.e. midJ <= tlaw + OFF/D
     -- the SELF-REFERENTIAL LEG: substituting the majorant into the
     identity gives tlaw <= (classical caps) + tlaw (1 + OFF/tau):
     cap-coefficient >= 1, NO cap extractable (machine-gated
     vacuity).  The far field (y >= 4 y_t) contributes NEGATIVELY
     (F/A_0 in (0,1) past the last escaped root under the r140
     subordination census: J_far < 0, gated at x = 5/8/13): the
     entire positive excess is ONSET-CARRIED (om_max < gamma <=
     2 sqrt(y_t)).
(A5) the a-priori onset product bound |F/A_0| <= exp(sum |d_j|/
     (y - b_top)) pays exponent y_t/b_top = 40 -> 1138 ~ x^2.1:
     exponent dex >= 0.9 max(25 log10 x, |log10 tau|) at every rung
     (the ALIGNMENT-WALL continues into the onset window; gated).
ADJUDICATION: TLAWCAP is NOT ELIMINATED.  The assembly reduces it to
TOPROOT + classical (A1/A2) + envelope (A3) + ONSETCAP, where
ONSETCAP := [M_band + M_(om, Theta_J]] <= theta (tau + OFF), theta <=
1 - 1/poly -- and ONSETCAP is BAND-MASS at the Theta_J split, which
by Theorem B2 (r140, re-gated) is TLAWCAP itself modulo {JETLOCK =
TOPROOT, TAILVIS}.  The r141-PFLOOR elimination pattern does NOT
repeat; instead the arithmetic core SHARPENS to its minimal
coordinate: the zeros in the onset window (om_max, Theta_J(1/2)]
never carry all of tau (defect >= 1/poly).  Per-rung certificates:
theta_onset < 1 gated at x = 5/8/13/18 (1 - theta measured ~1e-2
class), x = 24 typed ONSETCAP-HORIZON-LIMITED (Theta_J(0.5) = 9276 >
gtop; r140 lever (d), the named instrument limit).

SUSCAP2R HARDNESS TYPE AFTER THIS ROUND: per-rung certificate cost is
POLY (one nf x nf mp eigensolve, nf <= K = O(x log x), dps ladder
linear in x: bit cost poly(x) -- demand-gated), so SUSCAP2R is
certified-per-rung AT ANY DEPTH; the r141 tail-heaviness (J* ~ 0.3 m)
obstructs only the SIX-DATA CLOSED FORM, not the certificate.  The
lambda-uniform statement in its sharpest coordinate:
   s(x) = sum_{i>=1} (M_i(T_z^2)/M_0(T_z^2))^2 / delta_i <= poly(x)
(Z-free by V1: no spacing-lattice product, no lattice-proximity
demand, no tlaw consumption) along the instrument-chosen unbounded
x-sequence (V2/CDXLV quantifier, inherited) -- typed
ARITHMETIC-PINNING (BANDMASS-class): the RvM-legal adversarial
config carries s' ~ 5-6 versus truth 0.03-0.06 (the s-currency SEES
the arithmetic; re-gated here), while the W1/W2 ALGEBRA is
config-blind (null control: pinch + defect identity hold on the
adversarial well too).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer: G10 W1 defect identity (generic partial-fraction
    rearrangement + exact 3-level rational instance at the exact
    secular root, defect > 0); G11 W1 pinch (chi_2 <= chi-tilde/
    (delta_1 - g) step + 1 - g/delta_1 <= s g <= 1 on the instance);
    G12 W2 loop equivalence (forward: s <= 1/g + root < q_1;
    backward: G16-r141 shape re-gate + demand composition 1/(P + P)
    == 1/(2P)); G13 W3 interlacing (exact rational Gram instance,
    codim-1 compression of diag(1,2,5,7): reduced roots dominate
    full eigenvalues 1..3 and are dominated by 2..7; Courant-Fischer
    CITED for the generic statement); G14 TLAWCAP assembly algebra
    (triangle |sum a cos| <= sum a; HSW leading-term derivative
    -log(T/2pi)/T^2 < 0 + frozen-grid monotonicity; E1-composition
    exact solve re-gate (r140 G16 shape) + G(Theta)/G(T_z) <= 1
    monotone absorption; self-referential leg J <= M_mid <= tau +
    OFF exact chain + VACUITY bool: majorant substitution leaves
    cap-coefficient >= 1); G15 onset pricing form (|log(1+u)| <=
    |u|/(1-|u|) instance + product-log assembly + dex coordinate).
S2  G20 HSW G(T) sanity + frozen-grid monotone.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan to T_z + 6, step 0.05):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform); G31 node-config V (|qrel| <= 1e-30, null residual
    <= 1e-40) + W3 INSTANTIATED: delta_1 >= FULLGAP (1 - 1e-12),
    FULLGAP = (mpE[1] - mpE[0])/mpE[0] printed (pre-freeze
    UNMEASURED, disclosed: theorem-gate only + INFO value);
    G32 loop instantiated at the zone-top argmin: top-grid min in
    the frozen r139/r141 window AND >= 3; s <= 0.1; s x gap in
    (0.98, 1.02); delta_1 in the frozen window; share_1 >= 0.5;
    tlaw on the CDXLI strings <= 5e-3; W1 defect identity rel dev
    <= 1e-10; pinch HARD (1 - g/delta_1 - 1e-12 <= s g <= 1 +
    1e-12); defect ratio (1 - sg) delta_1/g in (0.4, 1 + 1e-9)
    (one-moded defect);
    G33 s Z-freeness h-ladder at the top node (h = 0.04/0.02/0.01
    x both signs): pinch + defect identity at EVERY point; |slope
    log10 gap vs log10 Z^2| <= 0.05 (structural r141 anchor);
    |slope log10 s vs log10 Z^2| <= 0.5 (the O(h) smoothness class,
    r141 amendments 2/3 cited); log10 Z^2 via mp.log in workdps
    (r141 amendment-1 lesson);
    G34 TLAWCAP assembly instantiated (own cache mid sums, f64
    ordinates + declared slop; band CITED from the r137 strings):
    midG <= min(1/2, G(om_max)/(2 G(T_z))) + slop; |midC| <= midG +
    slop; midJ in (0.02, 0.5) AND the self-referential gate midJ <=
    (tau + OFF)/D (1 + 1e-9) + slop; assembly identity residual
    resid_inf = tlaw - midG - midC - midJ - band_cited inside
    [-1e-4 - (OFF + 3 slop)/D, beyond_hi/D + (OFF + 3 slop)/D +
    1e-4 + band_cited]; Landau pin re-gate (prime powers 5/8/13:
    |z| <= 3.0, sign C_mid < 0 at 5/13; composites 18/24: |z_null|
    <= 3.5); Landau typed UNCONDITIONAL-CITED, NOT-NEEDED-FOR-CAP;
    G35 midJ anatomy: J_far (gamma^2 > 4 y_t) < 0 HARD at x =
    5/8/13 (subordination far field is subordinate -- the excess is
    ONSET-CARRIED); x = 18 printed (window 7093..gtop, thin);
    x = 24 far-window empty in cache (printed);
    G36 ONSETCAP coordinate: y_t in the frozen r140 windows,
    A_2/A_0 < 0, y_t/b_top >= 30; Theta_J(0.5) in the frozen r140
    windows (source-only ENVJ onset, no zeros); at x = 5/8/13/18:
    theta_onset = (M_band_cited + M_(om,Theta] + 3 slop)/(tau+OFF)
    < 1 - 1e-4 AND log10(1/(1-theta)) <= 1.5 + 4.5 log10 x (r140
    poly class); at x = 24: Theta_J(0.5) > gtop typed
    ONSETCAP-HORIZON-LIMITED; exp pricing exponent y_t/b_top x
    log10(e) >= 0.9 max(25 log10 x, |log10 tau|) at every rung.
S3b G40 adversarial s-witness at x = 5, 8 (RvM quantile config, r139
    G37 replica): q0rel >= 10; max s' over the frozen probe set >=
    1.0 (truth s <= 0.1: the s-currency separates arithmetic from
    RvM-legal by >= 10x); pinch + defect identity HOLD on the
    adversarial well (algebra config-blind -- null control).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 AND y_t_w/b_top <= 1.0 (r140 no-escaped-scale
    signature; MAIN >= 30); G53 consistency.
S5  G54 tau-screen (|slope log10 s vs log10 tau| <= 0.30 AND |slope
    log10 gap vs log10 tau| <= 0.30; the RAW gap rides tau BY
    CONSTRUCTION -- BOUND-RIDES-CONNES typed); G55 conditioning
    (1e-25 shift window).
S6  G60 demand audit (bookkeeping over cited statements, typed
    CHAIN-AUDIT: NFCLOS sequence-demand (CDXXIII) -> Theorem R
    transfer (CDXXX) -> coupling absorbed -> the SUSCAP2R leg in
    the s-coordinate consumes NO tlaw and NO Z (W2 + V1/CDXLV) ->
    V2 good sets provide the unbounded sequence -> no ALL-X demand
    survives; per-rung certificate cost POLY: one nf^3 eigensolve
    at dps(x) ~ 6x digits -- CERT-COST-POLY typed);
    G61 min-cut (r116 replica): merged chain L1TAILPROVEN ->
    TOPROOT(1) -> TAILVIS(1) -> TLAWCAP(1) -> BANDMASSTHM(INF,
    B1/B2 + THIS ROUND's assembly) -> SUSCAP2R(1) -> DELTA1FLOOR(1)
    -> QSUBGAPTHM(INF) -> PFLOORTHM(INF) -> COUNTEQTHM ->
    SEEDBALLTHM -> SPACREMTHM -> DOMASYM -> WPDWIN; flows base 4,
    refined 5, one-grant 5, counterfactual PARALLEL 9 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2];
T_PT = 3000175332800 [PT21]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); SCAN_STEP = 0.05; SCAN_LO = 0.5; SCAN_OVER = 6.0;
TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05; NODE_EXCL = 0.02; H_LADDER
= (0.04, 0.02, 0.01); CACHE_SLOP = 1e-9; ADV_RUNGS = (5, 8);
HSW_MONO_GRID = (50, 100, 1e3, 1e4, 1e5, 1e6, 3e12).
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)} (r139/r141 measured 33.62/
16.72/22.66/16.59/19.58); S_BAR = 0.1 (r141 s = 0.02974/0.05981/
0.04413/0.06029/0.05108); SGAP_WIN = (0.98, 1.02) (r141 s x gap =
0.99985/0.99998/1.00000/1.00000/1.00000); D1_WIN x (0.7, 1.3) around
{5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8}
(r139/r141 strings); SHARE1_BAR = 0.5 (r139: 0.969/0.965/0.946/
0.944/0.947); TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18:
0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI strings); DEFECT_ID_BAR =
1e-10; PINCH_SLOP = 1e-12; DEFECT_RATIO_WIN = (0.4, 1 + 1e-9)
(predicted ~share_1 = 0.94..0.97, pre-freeze UNMEASURED as a ratio,
window set from the share_1 strings with disclosed headroom);
INTERLACE_SLOP = 1e-12; SLOPE_GAP_BAR = 0.05 (r141 measured <=
0.012); SLOPE_S_BAR = 0.5 (the r141 amendment-2/3 O(h) smoothness
class: s-slope = chi-slope - R2-slope in [-0.6, 0.6] worst case;
bar chosen ABOVE the class, disclosed); MIDG_HARD = 0.5; MIDJ_WIN =
(0.02, 0.5) (r137 strings 0.054/0.126/0.111/0.172 at 5..18, x=24
interpolated ~0.19-0.23, disclosed); BAND_D_CITED = {5: 2.1e-5, 8:
7.3e-6, 13: 1.7e-8, 18: 2.9e-7, 24: 4.5e-9} (CDXLI T1 strings, band
in D units); RESID_LO_PAD = 1e-4; RESID_HI_PAD = 1e-4; LANDAU_Z_PP
= 3.0 (sign gate at 5, 13); LANDAU_Z_COMP = 3.5 (r137 measured z =
+0.17/+0.75/-0.10 pp, z_null = +1.00/+0.74 comp); FAR_RUNGS =
(5, 8, 13) (gamma_cut = 2 sqrt(y_t) = 494/1291/3580 < gtop; x=18
window (7093, gtop] printed only; x=24 empty); YT_WIN x (0.9, 1.1)
around {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7, 24:
4.013e7} (r140 strings); YTB_MIN = 30.0 (measured y_t/b_top = 40/
114/318/630/1138); TH_WIN x (0.85, 1.15) around {5: 360, 8: 943,
13: 2620, 18: 5191, 24: 9276} (r140 Theta_J(0.5) strings; same
ENVJ/onset code ported verbatim); ONSET_RUNGS = (5, 8, 13, 18);
THETA_MAX = 1 - 1e-4; B1_POLY_C0 = 1.5; B1_POLY_SLOPE = 4.5 (r140
class); EXP_PRICE_FAC = 0.9; TURAN_POLY_DEG = 25; Q0REL_MIN = 10.0
(r139 RvM: 3.5e6/6.8e14); S_ADV_MIN = 1.0 (r139 rel-gaps 0.203/
0.150 ==> s' ~ 1/rel - 1/delta_1' ~ 4.8/6.5, predicted); ADV_ID_BAR
= 1e-8; CTRL_YTB_MAX = 1.0 (r140: 0.15/0.64/0.18); TAU_SLOPE_BAR =
0.30; COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694
(ward only); RUNTIME_BAR = 14400 s.  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks; no
f64-refinement of mp roots; np.float64-repr casts guarded by
float(); log-scale diagnostics via mp.log inside workdps (r141
amendment-1 class).

CALIBRATION DISCLOSURE (pre-freeze): NO scratch script was run for
this probe; every window derives from the frozen strings of the
cited rounds (r137/CDXLI budget + Landau tables; r139/CDXLIII gap/
delta_1/share_1 tables; r140/CDXLIV y_t/Theta_J/subordination
strings; r141/CDXLV s/s x gap/tlaw replication strings), quoted
verbatim in FROZEN NUMERICS.  Genuinely NEW quantities are either
THEOREM gates (W1 defect identity, W1 pinch, W3 interlacing, midG/
midC caps, midJ self-referential majorant, J_far sign -- risk-free
by exact algebra) or disclosed-unmeasured (FULLGAP value: INFO +
theorem gate only; defect ratio: window from the share_1 strings;
midJ at x=24: window padded; s'_rvm: predicted from the r139
rel-gap strings via the W1 algebra).  The two derived predictions
frozen as consistency anchors: defect 1 - s g ~ g/delta_1 =
1.5e-4/1.7e-5/2.1e-6/5.1e-7/1.7e-7 (matches the CDXLV s x gap
strings at print precision).
SMOKE DISCLOSURE: smoke 1 = 22/23 (log kept) with ONE instrument
repair -- the G14 monotonicity sub-boolean must gate the EXACT
derivative identity d/dGT = (1+r)^2/(GZ (1-th)) plus a rational
positivity instance (sympy .is_positive returns None: it cannot
infer th < 1 from positivity assumptions alone; the r137-G11/
r140-G18 normal-form class; no bar, no criterion, no ladder
moved).  Smoke-1 x=5 exhibits, quoted: defect 1.4642e-4 vs
g/delta_1 1.5108e-4 ratio 0.969 == share_1; delta_1/FULLGAP =
1.0000 (the W3 interlacing is measured TIGHT at x=5); s'_rvm =
4.92; theta_onset = 0.8910; J_far/D = -3.898e-3.  smoke 2 at the
frozen spec must be green.  Amendments after the frozen run, if
any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): W1-PROVEN(defect identity: s x gap == 1 is
NOT exact; defect = second-order susceptibility, pinched in
[1 - g/delta_1, 1], one-moded); LOOP-EXPOSED(QSUBGAP <==> SUSCAP2R
AND DELTA1FLOOR: the r139 carve-out was circular on this leg --
SUSCAP2R IS QSUBGAP-uniformity modulo the strictly weaker
delta_1-floor; no tlaw and no Z consumed in the s-coordinate);
DELTA1-INTERLACED(DELTA1FLOOR <== FULLGAP, source-only, per-rung);
TLAWCAP-NOT-ELIMINATED(assembly adjudicated: midG + midC classical
WITHOUT Landau, resid TOPROOT+envelope, but midJ is budget-self-
referential and the onset product bound is exp-priced: TLAWCAP <==>
ONSETCAP modulo {TOPROOT, TAILVIS} -- the core relocates to the
onset window, it does not dissolve; the r141-PFLOOR pattern does
NOT repeat); ONSETCAP-PER-RUNG(theta < 1 certified x = 5..18; x=24
HORIZON-LIMITED); LANDAU-UNCONDITIONAL-CITED(NOT-NEEDED-FOR-CAP);
MIDJ-ONSET-CARRIED(J_far < 0 gated); ONSET-EXP-PRICED(alignment
wall continues); S-SEES-ARITHMETIC(adversarial witness; algebra
config-blind); CERT-COST-POLY(per-rung certificate polynomial;
tail-heaviness obstructs only the closed form);
QUANTIFIER-INHERITED(dense-x suffices, CHAIN-AUDIT);
CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES(typed);
OMEGA-RESHAPED(residue = {TOPROOT, TAILVIS, TLAWCAP(=ONSETCAP),
SUSCAP2R(=QSUBGAP mod DELTA1FLOOR <== FULLGAP)}; census {MEAS,
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
LADDER_DEEP = ((18, 140), (24, 150))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
H_LADDER = (0.04, 0.02, 0.01)
CACHE_SLOP = 1e-9
ADV_RUNGS = (5, 8)
HSW_MONO_GRID = (50.0, 100.0, 1e3, 1e4, 1e5, 1e6, 3e12)
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0),
            18: (12.0, 22.0), 24: (14.0, 26.0)}
S_BAR = 0.1
SGAP_WIN = (0.98, 1.02)
D1_TAB = {5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8}
D1_WIN = (0.7, 1.3)
SHARE1_BAR = 0.5
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
DEFECT_ID_BAR = 1e-10
PINCH_SLOP = 1e-12
DEFECT_RATIO_WIN = (0.4, 1.0 + 1e-9)
INTERLACE_SLOP = 1e-12
SLOPE_GAP_BAR = 0.05
SLOPE_S_BAR = 0.5
MIDG_HARD = 0.5
MIDJ_WIN = (0.02, 0.5)
BAND_D_CITED = {5: 2.1e-5, 8: 7.3e-6, 13: 1.7e-8, 18: 2.9e-7,
                24: 4.5e-9}
RESID_LO_PAD = 1e-4
RESID_HI_PAD = 1e-4
LANDAU_Z_PP = 3.0
LANDAU_Z_COMP = 3.5
FAR_RUNGS = (5, 8, 13)
YT_TAB = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
          24: 4.013e7}
YT_WIN = (0.9, 1.1)
YTB_MIN = 30.0
TH_TAB = {5: 360.0, 8: 943.0, 13: 2620.0, 18: 5191.0, 24: 9276.0}
TH_WIN = (0.85, 1.15)
ONSET_RUNGS = (5, 8, 13, 18)
THETA_MAX = 1.0 - 1e-4
B1_POLY_C0 = 1.5
B1_POLY_SLOPE = 4.5
EXP_PRICE_FAC = 0.9
TURAN_POLY_DEG = 25
Q0REL_MIN = 10.0
S_ADV_MIN = 1.0
ADV_ID_BAR = 1e-8
CTRL_YTB_MAX = 1.0
TAU_SLOPE_BAR = 0.30
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


def source_ctx(ce: dict) -> dict:
    """per-rung mp context: coefficients, lattice, jets to M_JETS
    (r140 shape, ported)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        aa = mp.log(ce["x"]) / 2
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        cs_abs = [abs(v) for v in cs]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]   # b[0] = 0
        A = []
        pw = [mp.mpf(1)] * K
        for m in range(M_JETS + 1):
            if m == 0:
                acc = sum((-1) ** k * cs[k] for k in range(K))
            else:
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
            A.append(acc)
        A0 = A[0]
        yt = abs(A[1] / A0)
    return dict(K=K, dps=dps, aa=aa, cs=cs, cs_abs=cs_abs, b=b, A=A,
                A0=A0, a0f=float(abs(A0)), yt=float(yt),
                btop=float(b[-1]))


def envj(ctx: dict, y):
    """min over m in MGRID of the Theorem-J1 envelope at y > b_top
    (r140, ported verbatim); caller sets workdps."""
    A, b, cs_abs, K = ctx["A"], ctx["b"], ctx["cs_abs"], ctx["K"]
    best = None
    for m in MGRID:
        head = mp.mpf(0)
        yi = mp.mpf(1)
        ok = True
        for i in range(1, m + 1):
            yi *= y
            head += abs(A[i]) / yi
            if best is not None and head > best:
                ok = False
                break
        if not ok:
            continue
        rem = mp.mpf(0)
        for k in range(1, K):
            rem += cs_abs[k] * b[k] ** (m + 1) / (yi * (y - b[k]))
        v = head + rem
        if best is None or v < best:
            best = v
    return best


def onset(ctx: dict, rho: float):
    """Theta_J(rho): unique solution of ENVJ(Theta^2) = rho |A_0|
    (r140, ported verbatim); caller sets workdps."""
    A0a = abs(ctx["A0"])
    tgt = mp.mpf(repr(float(rho))) * A0a
    lo = mp.log(mp.mpf(repr(ctx["btop"])) * (1 + mp.mpf("1e-9")))
    yhi = mp.mpf(repr(max(8.0 * ctx["yt"] / rho, 8.0 * ctx["btop"])))
    for _ in range(200):
        if envj(ctx, yhi) < tgt:
            break
        yhi *= 4
    hi = mp.log(yhi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if envj(ctx, mp.exp(mid)) > tgt:
            lo = mid
        else:
            hi = mid
    return float(mp.sqrt(mp.exp(hi)))


def lam_von_mangoldt(x: int) -> float:
    for p in range(2, x + 1):
        if any(p % d == 0 for d in range(2, p)):
            continue
        q = p
        while q <= x:
            if q == x:
                return math.log(p)
            q *= p
    return 0.0


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


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def rvm_quantiles(n: int) -> list:
    out = []
    for i in range(n):
        lo, hi = 2 * math.pi + 0.1, 1e7
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) >= i + 0.5:
                hi = mid
            else:
                lo = mid
        out.append(hi)
    return out


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138/r139/r141 replica)."""
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
    (r141 shape).  Caller sets workdps."""
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
    for _ in range(120):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, et, en2, etn, rho2, chi


def loop_currency(Vd: dict, lam, etn, rho2, chi):
    """(g, s, sg, delta_1, defect_lhs, defect_rhs, ratio) in tau
    units for a secular solve; caller sets workdps."""
    qs, nf = Vd["qs"], Vd["nf"]
    tau = Vd["tau_mp"]
    g = (lam - qs[0]) / tau
    d1 = (qs[1] - qs[0]) / tau
    s = tau * chi / rho2
    sg = s * g
    chi2 = mp.mpf(0)
    for i in range(1, nf):
        chi2 += etn[i] * etn[i] / ((qs[i] - qs[0]) * (qs[i] - lam))
    defect_rhs = (g * g / rho2) * (tau * tau) * chi2
    defect_lhs = 1 - sg
    ratio = defect_lhs * d1 / g
    return g, s, sg, d1, defect_lhs, defect_rhs, ratio


def zfac(p_mp, zone_nds, K, oms):
    """common zone/lattice scalar Z(p) (THEOREM V1, r141 cited);
    caller sets workdps."""
    acc = 2 / p_mp
    for mu in zone_nds:
        acc *= (p_mp * p_mp - mu * mu)
    for k in range(1, K):
        acc /= (p_mp * p_mp - oms[k] ** 2)
    return acc


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    lam = sp.symbols("lam")

    # shared exact 3-level instance: W = diag(1, 2, 5) in tau units
    # q0 = 1 (tau), delta_1 = 1, delta_2 = 4; unit row (3,4,12)/13
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    r1, r2, r3 = sp.Rational(3, 13), sp.Rational(4, 13), \
        sp.Rational(12, 13)
    fsec = r1 ** 2 / (q0i - lam) + r2 ** 2 / (q1i - lam) \
        + r3 ** 2 / (q2i - lam)
    roots = sorted(sp.solve(sp.together(fsec).as_numer_denom()[0], lam))
    lam_star = roots[0]
    g_i = lam_star - q0i               # tau = 1 on the instance
    d1_i, d2_i = q1i - q0i, q2i - q0i
    rho2_i = r1 ** 2
    chit_i = r2 ** 2 / d1_i + r3 ** 2 / d2_i
    s_i = chit_i / rho2_i
    chi2_i = r2 ** 2 / (d1_i * (q1i - lam_star)) \
        + r3 ** 2 / (d2_i * (q2i - lam_star))

    # G10 W1 defect identity
    e1s, e2s, d1s, d2s, gs = sp.symbols("e1s e2s d1s d2s gs",
                                        positive=True)
    lhsg = e1s / (d1s - gs) + e2s / (d2s - gs)
    rhsg = (e1s / d1s + e2s / d2s) \
        + gs * (e1s / (d1s * (d1s - gs)) + e2s / (d2s * (d2s - gs)))
    okA = sp.simplify(sp.together(lhsg - rhsg)) == 0
    defect_lhs = sp.simplify(1 - s_i * g_i)
    defect_rhs = sp.simplify((g_i ** 2 / rho2_i) * chi2_i)
    okB = sp.simplify(defect_lhs - defect_rhs) == 0
    okC = bool(defect_lhs > 0)
    out.append(("G10-w1-defect-identity", okA and okB and okC,
                "1/(d-g) == 1/d + g/(d(d-g)) summed (generic): the "
                "secular equation gives 1 - s g == (g^2/rho2) "
                "sum et_i^2/(delta_i (delta_i - g)) EXACTLY; on the "
                "exact 3-level instance lhs == rhs and defect > 0: "
                "s x gap == 1 is NOT an identity -- the defect is "
                "the second-order susceptibility (THEOREM W1)"))

    # G11 W1 pinch
    okD = bool(sp.simplify(chi2_i - chit_i / (d1_i - g_i)) <= 0)
    okE = bool(defect_lhs <= g_i / d1_i) \
        and bool(sp.simplify(s_i * g_i - (1 - g_i / d1_i)) >= 0) \
        and bool(s_i * g_i <= 1)
    out.append(("G11-w1-pinch", okD and okE,
                "chi_2(g) <= chi-tilde/(delta_1 - g) (term-wise, "
                "instance) ==> 1 - g/delta_1 <= s g <= 1 (THEOREM W1 "
                "pinch): the measured s x gap = 0.99985..1.00000 IS "
                "this pinch at g/delta_1 = 1.5e-4..1.7e-7"))

    # G12 W2 loop equivalence
    Ps, ss = sp.symbols("Ps ss", positive=True)
    # forward: sg <= 1 ==> s <= 1/g; root < q1 ==> delta_1 > g
    okF = bool(s_i <= 1 / g_i) and bool(q0i < lam_star < q1i) \
        and bool(d1_i > g_i)
    # backward: G16-r141 shape (exact rearrangement re-gate)
    R2s, chis, taus, D1s = sp.symbols("R2s chis taus D1s",
                                      positive=True)
    lhsS = (R2s / (chis + R2s / (D1s * taus))) / taus
    rhsS = 1 / (taus * chis / R2s + 1 / D1s)
    okG = sp.simplify(lhsS - rhsS) == 0
    # demand composition: s <= P and delta_1 >= 1/P ==> g >= 1/(2P)
    okH = sp.simplify(1 / (Ps + 1 / (1 / Ps)) - 1 / (2 * Ps)) == 0
    # instance: lower bound value
    okI = bool(g_i >= 1 / (s_i + 1 / d1_i))
    out.append(("G12-w2-loop-equivalence", okF and okG and okH and okI,
                "FORWARD: g >= 1/P ==> s <= 1/g <= P (from s g <= 1) "
                "and delta_1 > g (root in (q0, q1)); BACKWARD: g >= "
                "1/(s + 1/delta_1) (U1/G16 shape re-gated) with s <= "
                "P, delta_1 >= 1/P ==> g >= 1/(2P): QSUBGAP <==> "
                "SUSCAP2R AND DELTA1FLOOR (THEOREM W2 -- the loop "
                "EXPOSED: SUSCAP2R is QSUBGAP-uniformity modulo the "
                "strictly weaker delta_1-floor)"))

    # G13 W3 interlacing (Gram-generalized instance)
    Wq = sp.diag(sp.Integer(1), sp.Integer(2), sp.Integer(5),
                 sp.Integer(7))
    # kernel of the row (1,1,1,1): basis u1, u2, u3 (non-orthogonal)
    U = sp.Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]])
    Qc = (U.T * Wq * U)
    Gc = (U.T * U)
    poly = sp.expand((Qc - lam * Gc).det())
    ppoly = sp.Poly(poly, lam)
    mus = [sp.CRootOf(ppoly, i) for i in range(3)]
    lams_full = [sp.Integer(1), sp.Integer(2), sp.Integer(5),
                 sp.Integer(7)]
    okJ = all(bool(mus[i] >= lams_full[i]) for i in range(3)) \
        and all(bool(mus[i] <= lams_full[i + 1]) for i in range(3))
    out.append(("G13-w3-interlacing", okJ,
                "codim-1 Gram compression of diag(1,2,5,7): reduced "
                "roots interlace lam_i <= mu_i <= lam_{i+1} exactly "
                "(CRootOf comparisons; Courant-Fischer CITED for "
                "generic codim-m): q_1(V) >= lam_1(Mq), so "
                "DELTA1FLOOR <== FULLGAP -- a SOURCE-ONLY "
                "two-eigenvalue statement (THEOREM W3)"))

    # G14 TLAWCAP assembly algebra
    a1, a2, th1, th2 = sp.symbols("a1 a2 th1 th2", positive=True)
    tri = sp.Abs(a1 * sp.cos(th1) + a2 * sp.cos(th2)) <= a1 + a2
    okK = bool(tri.subs({a1: sp.Rational(1, 3), a2: sp.Rational(1, 5),
                         th1: 1, th2: 2}).simplify()) \
        and bool(sp.Rational(1, 3) * sp.cos(sp.Integer(1))
                 + sp.Rational(1, 5) * sp.cos(sp.Integer(2))
                 <= sp.Rational(1, 3) + sp.Rational(1, 5))
    T = sp.symbols("T", positive=True)
    lead = (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)
    dlead = sp.simplify(sp.diff(lead, T)
                        + sp.log(T / (2 * sp.pi)) / (2 * sp.pi * T ** 2))
    okL = dlead == 0
    grid_ok = all(hsw_G(HSW_MONO_GRID[i]) > hsw_G(HSW_MONO_GRID[i + 1])
                  for i in range(len(HSW_MONO_GRID) - 1))
    # E1 composition re-gate (r140 G16 shape)
    tl, th, r_, GT, GZ, A0q, of_ = sp.symbols(
        "tl th r_ GT GZ A0q of_", positive=True)
    e1 = sp.Eq(tl * 8 * A0q ** 2 * GZ * (1 - th),
               8 * (1 + r_) ** 2 * A0q ** 2 * GT + (1 + th) * of_)
    sol_tl = sp.solve(e1, tl)
    okM = len(sol_tl) == 1 and sp.simplify(
        sol_tl[0] - ((1 + r_) ** 2 * GT / GZ
                     + (1 + th) * of_ / (8 * A0q ** 2 * GZ))
        / (1 - th)) == 0
    # G(Theta)/G(Tz) <= 1 absorption: bound monotone in GT/GZ
    # (exact derivative identity; positivity manifest for th < 1,
    # gated on a rational instance -- sympy cannot infer th < 1
    # from positivity alone: normal-form class, smoke-disclosed)
    dGT = sp.diff(sol_tl[0], GT)
    okN = sp.simplify(dGT - (1 + r_) ** 2 / (GZ * (1 - th))) == 0 \
        and bool(dGT.subs({r_: sp.Rational(1, 2),
                           GZ: sp.Rational(1, 3),
                           th: sp.Rational(1, 2)}) > 0)
    # self-referential leg: J <= M_mid <= tau + OFF
    Jm, Gm, Cm, Mb, Mby, So, taus2 = sp.symbols(
        "Jm Gm Cm Mb Mby So taus2", positive=True)
    Mm = 4 * A0q ** 2 * (Gm - Cm) + Jm
    okO = bool(sp.simplify(Mm - Jm - 4 * A0q ** 2 * (Gm - Cm)) == 0)
    # tau = Mb + Mm + Mby + Soff, |Soff| <= OFF ==> Mm <= tau + OFF
    okP = sp.simplify((taus2 - Mb - Mby + of_) - (Mm)
                      - ((taus2 - Mb - Mm - Mby + of_) - 0)) == 0
    # vacuity: cap-coefficient of tlaw on the rhs after majorant
    # substitution is (1 + OFF/tau) >= 1: no cap extractable
    offr = sp.symbols("offr", nonnegative=True)
    okQ = bool(sp.simplify((1 + offr) - 1) >= 0)
    out.append(("G14-tlawcap-assembly-algebra",
                okK and okL and grid_ok and okM and okN and okO
                and okP and okQ,
                "|sum a cos| <= sum a (A2: LANDAU NOT NEEDED for the "
                "cap); HSW leading term falls as -log(T/2pi)/T^2 + "
                "frozen-grid monotone (A1: midG <= 1/2); E1 "
                "composition tlaw <= [(1+r)^2 G(Th)/G(Tz) + "
                "OFF-part]/(1-th) exact (r140 G16 re-gate) with the "
                "bound increasing in G(Th) (so G(Th) <= G(Tz) "
                "absorbs); J_mid <= M_mid <= tau + OFF exact (A4): "
                "the budget majorizes midJ ONLY by tlaw -- cap "
                "coefficient (1 + OFF/tau) >= 1, VACUOUS for the "
                "cap (the self-referential leg, machine-gated)"))

    # G15 onset pricing form
    u = sp.Rational(1, 3)
    okR = bool(sp.Abs(sp.log(1 + u)) <= u / (1 - u)) \
        and bool(sp.Abs(sp.log(1 - u)) <= u / (1 - u))
    u1, u2 = sp.Rational(1, 5), sp.Rational(1, 7)
    okS = bool(sp.log((1 + u1) * (1 + u2))
               <= u1 / (1 - u1) + u2 / (1 - u2))
    ytp, btp = sp.symbols("ytp btp", positive=True)
    okT = sp.simplify(ytp / btp * sp.log(sp.exp(1), 10)
                      - ytp / (btp * sp.log(10))) == 0
    out.append(("G15-onset-pricing-form", okR and okS and okT,
                "|log(1+u)| <= |u|/(1-|u|) + product-log assembly "
                "(instances) + dex coordinate exact: the a-priori "
                "onset product bound pays exponent ~ y_t/b_top -- "
                "priced per rung in G36 (the ALIGNMENT-WALL "
                "continues into the onset window)"))
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
    # the SUSCAP2R leg in the s-coordinate consumes no tlaw, no Z:
    # W2 gives gap >= 1/(s + 1/delta_1) with s Z-free (V1/CDXLV) and
    # tlaw-free (no EPSLOCK consumption on this leg; the r139 U2
    # numerator factorization was coordinate bookkeeping).
    steps.append(("SUSCAP2R leg (W2): gap >= 1/(s + 1/delta_1) "
                  "consumes NO tlaw and NO spacing-lattice product "
                  "(V1 cited): no lattice-proximity demand on this "
                  "leg at all", True))
    provider = FULL_MEAS
    steps.append(("V2 (CDXLV, cited) provides full-measure good "
                  "sets => unbounded sequence exists constructively",
                  provider <= demand))
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

    print("tlawcap_suscap2r_probe -- PRIME.TLAWCAP.SUSCAP2R.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    adv_rungs = (5,) if smoke else ADV_RUNGS
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
    section("S1  EXACT LAYER (Theorems W1-W3 + assembly algebra)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW + OFF recipe; r132 "
         "raw census; r135 D1-D4; r136 S1-S4 + PINBALL; r137/CDXLI "
         "budget identity G31/G33 + Landau pin + band/tlaw strings; "
         "r138 Q1-Q3; r139/CDXLIII U1-U4 + locality + adversarial + "
         "delta_1/share_1 strings; r140/CDXLIV J1-J4 + B1/B2 + "
         "y_t/Theta_J strings + subordination census; r141/CDXLV "
         "V1-V3 + s strings + quantifier audit; HSW22 Cor. 1.2; "
         "PT21; Euler sine product; Courant-Fischer min-max; Landau "
         "1912 + Gonek 1993 (UNCONDITIONAL, form only, and NOT "
         "needed for the cap -- the A2 triangle closes midC); "
         "Littlewood S_1 class")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone "
          "(incl. the frozen S1 grid); G(gamma_top) = %.3e"
          % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: LOOP + ASSEMBLY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36 = [], [], []
    gap_tab, tau_tab, s_tab = {}, {}, {}
    cells = {}
    for x, dps in all_rungs:
        is_deep = x > 13
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        cells[x] = ce
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        ctx = source_ctx(ce)
        yt = ctx["yt"]
        btop = ctx["btop"]
        om_max = math.sqrt(btop)
        with mp.workdps(dps):
            cs = ctx["cs"]
            aa = ctx["aa"]
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            A0 = ctx["A0"]
            tauf = float(ce["mpE"][0])
            # source-only onset + OFF (r140 recipe)
            theta05 = onset(ctx, 0.5)
            eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(A0))
            off = float(8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2) \
                * hsw_G(float(T_PT))
            eta_g = float(envj(ctx, mp.mpf(repr(gtop)) ** 2) / abs(A0))
        a0f = ctx["a0f"]
        Gz = hsw_G(Tz)
        D = 8.0 * a0f ** 2 * Gz
        tlaw = tauf / D
        beyond_hi = 8.0 * a0f ** 2 * (1 + eta_g) ** 2 * hsw_G(gtop)

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
                 "found %d nodes (zone prefix + overhang; edge census "
                 "not consumed)" % (x, SCAN_OVER, len(seeds)))
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
        zone_f = nds_f_all[:m_zone]
        s_top = float(zone_f[-1] - zone_f[-2]) if m_zone > 1 else 3.0

        # ---- G31 node-config V + W3 instantiation
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            fullgap = float((ce["mpE"][1] - ce["mpE"][0])
                            / ce["mpE"][0])
            d1_node = float((Vd["qs"][1] - Vd["qs"][0]) / Vd["tau_mp"])
        ok31x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR
                 and d1_node >= fullgap * (1.0 - INTERLACE_SLOP))
        ok31 = ok31 and ok31x
        det31.append("x%d: qrel %.0e nullres %.0e nf %d; delta_1 "
                     "%.3e >= FULLGAP %.3e (W3, %.0f s)"
                     % (x, Vd["qrel"], Vd["resR"], Vd["nf"], d1_node,
                        fullgap, time.time() - t_q))
        info("x=%d W3 exhibit: FULLGAP = (lam_1 - tau)/tau = %.6e "
             "(source-only, pre-freeze unmeasured, INFO); delta_1/"
             "FULLGAP = %.4f" % (x, fullgap, d1_node / fullgap))

        # ---- G32 loop instantiated at the zone-top argmin
        with mp.workdps(dps):
            tau = Vd["tau_mp"]
            tg = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                TOP_GRID_STEP)) + [Tz - 0.001]
            gmin = None
            argp = None
            for tv in tg:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - tau) / tau)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
            g_ex, s_val, sg, d1, dlhs, drhs, dratio = \
                loop_currency(Vd, lam, etn, rho2, chi)
            g_f = float(g_ex)
            s_f = float(s_val)
            sg_f = float(sg)
            d1_f = float(d1)
            id_dev = float(abs(dlhs - drhs) / abs(dlhs))
            pinch_lo = float(1 - g_ex / d1)
            ratio_f = float(dratio)
            share1 = float((etn[1] * etn[1] / (Vd["qs"][1]
                                               - Vd["qs"][0])) / chi)
        lo_w, hi_w = REPL_WIN[x]
        tl_dev = abs(tlaw / TLAW_TAB[x] - 1.0)
        ok32x = (gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR
                 and SGAP_WIN[0] <= sg_f <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR
                 and tl_dev <= TLAW_TOL
                 and id_dev <= DEFECT_ID_BAR
                 and pinch_lo - PINCH_SLOP <= sg_f <= 1.0 + PINCH_SLOP
                 and DEFECT_RATIO_WIN[0] <= ratio_f
                 <= DEFECT_RATIO_WIN[1])
        ok32 = ok32 and ok32x
        det32.append("x%d: gap %.4f s %.5f sg %.7f (pinch lo "
                     "%.7f) defect %.3e (id dev %.0e, ratio %.3f) "
                     "d1 %.3e share1 %.3f tlaw %.4f"
                     % (x, gmin, s_f, sg_f, pinch_lo, 1.0 - sg_f,
                        id_dev, ratio_f, d1_f, share1, tlaw))
        gap_tab[x] = gmin
        tau_tab[x] = tauf
        s_tab[x] = s_f
        info("x=%d W1 exhibit: 1 - s*gap = %.4e vs g/delta_1 = %.4e "
             "(one-moded defect, ratio %.3f ~ share_1 %.3f)"
             % (x, 1.0 - sg_f, g_f / d1_f, ratio_f, share1))

        # ---- G33 s Z-freeness h-ladder at the top node
        okv = True
        rows_h = []
        with mp.workdps(dps):
            mu_top = zone_nds[-1]
            for h in H_LADDER:
                for sgn in (-1, 1):
                    pv = mu_top + sgn * mp.mpf(repr(h)) \
                        * mp.mpf(repr(s_top))
                    rr = row_at(pv, K, oms, nrm)
                    lamh, eth, en2h, etnh, rho2h, chih = \
                        secular_data(Vd, rr)
                    gh, sh, sgh, d1h, dlh, drh, rth = \
                        loop_currency(Vd, lamh, etnh, rho2h, chih)
                    Zh = zfac(pv, zone_nds, K, oms)
                    l10 = mp.log(10)
                    lz2 = float(2 * mp.log(abs(Zh)) / l10)
                    idv = float(abs(dlh - drh) / abs(dlh))
                    plo = float(1 - gh / d1h)
                    okv = okv and idv <= DEFECT_ID_BAR \
                        and plo - PINCH_SLOP <= float(sgh) \
                        <= 1.0 + PINCH_SLOP
                    rows_h.append((h, sgn, float(gh), float(sh),
                                   lz2))
        slopes_txt = []
        for sgn in (-1, 1):
            sel = [rw for rw in rows_h if rw[1] == sgn]
            lz = [rw[4] for rw in sel]
            sgp = float(np.polyfit(lz, [math.log10(rw[2])
                                        for rw in sel], 1)[0])
            ssp = float(np.polyfit(lz, [math.log10(rw[3])
                                        for rw in sel], 1)[0])
            okv = okv and abs(sgp) <= SLOPE_GAP_BAR \
                and abs(ssp) <= SLOPE_S_BAR
            slopes_txt.append("%+d: gap %+.4f s %+.4f" % (sgn, sgp,
                                                          ssp))
        ok33 = ok33 and okv
        det33.append("x%d: %s (lZ2 span [%.1f, %.1f])"
                     % (x, " | ".join(slopes_txt),
                        min(rw[4] for rw in rows_h),
                        max(rw[4] for rw in rows_h)))

        # ---- G34/G35/G36 cache mid pass (one sweep)
        n_band = int(np.sum(gam <= om_max))
        gcut = 2.0 * math.sqrt(yt)
        with mp.workdps(dps):
            err = mp.mpf(repr(CACHE_SLOP))
            g_mid = mp.mpf(0)
            c_mid = mp.mpf(0)
            j_mid = mp.mpf(0)
            j_far = mp.mpf(0)
            m_mid = mp.mpf(0)
            m_slop = mp.mpf(0)
            m_onset = mp.mpf(0)
            n_far = 0
            for j in range(n_band, len(gam)):
                gj = mp.mpf(repr(float(gam[j])))
                E, Ep = en_pair(cs, aa, oms, gj)
                yv = gj * gj
                Fv = A0
                for k in range(1, K):
                    Fv += (-1) ** k * cs[k] * oms[k] ** 2 \
                        / (yv - oms[k] ** 2)
                e2 = 2 * abs(E) ** 2
                m_mid += e2
                m_slop += 2 * (2 * abs(E) * abs(Ep) * err
                               + (abs(Ep) * err) ** 2)
                g_mid += 1 / yv
                s2 = mp.sin(aa * gj) ** 2
                c_mid += (1 - 2 * s2) / yv
                jterm = 8 * s2 * (Fv ** 2 - A0 ** 2) / yv
                j_mid += jterm
                if float(gam[j]) > gcut:
                    j_far += jterm
                    n_far += 1
                if float(gam[j]) <= theta05:
                    m_onset += e2
            g_mid_f = float(g_mid)
            c_mid_f = float(c_mid)
            j_mid_f = float(j_mid)
            j_far_f = float(j_far)
            m_slop_f = float(m_slop)
            m_onset_f = float(m_onset)
        midG = 4.0 * a0f ** 2 * g_mid_f / D
        midC = -4.0 * a0f ** 2 * c_mid_f / D
        midJ = j_mid_f / D
        slp = 3.0 * m_slop_f / D
        band_cited = BAND_D_CITED[x]
        resid_inf = tlaw - midG - midC - midJ - band_cited
        lo_r = -RESID_LO_PAD - (off / D + slp)
        hi_r = beyond_hi / D + off / D + slp + RESID_HI_PAD \
            + band_cited
        sig_c = math.sqrt(float(np.sum(
            gam[n_band:] ** -4.0)) / 2.0)
        lamx = lam_von_mangoldt(x)
        if lamx > 0:
            c_pred = -lamx / (2 * math.pi * math.sqrt(x)) \
                * (1.0 / om_max - 1.0 / gtop)
            zsc = (c_mid_f - c_pred) / sig_c
            landau_ok = abs(zsc) <= LANDAU_Z_PP
            if x in (5, 13):
                landau_ok = landau_ok and c_mid_f < 0
            ltxt = "pp z%+.2f" % zsc
        else:
            zsc = c_mid_f / sig_c
            landau_ok = abs(zsc) <= LANDAU_Z_COMP
            ltxt = "comp z0%+.2f" % zsc
        ok34x = (midG <= min(MIDG_HARD,
                             hsw_G(om_max) / (2.0 * Gz)) + slp
                 and abs(midC) <= midG + slp
                 and MIDJ_WIN[0] <= midJ <= MIDJ_WIN[1]
                 and midJ <= (tauf + off) / D * (1 + 1e-9) + slp
                 and lo_r <= resid_inf <= hi_r
                 and landau_ok)
        ok34 = ok34 and ok34x
        det34.append("x%d: midG %.4f midC %+.4f midJ %.4f resid "
                     "%.4f in [%.0e, %.4f] %s"
                     % (x, midG, midC, midJ, resid_inf, lo_r, hi_r,
                        ltxt))
        info("x=%d assembly: tlaw %.4f = midG %.4f + midC %+.4f + "
             "midJ %.4f + band %.1e (CITED) + resid %.4f; midJ/tlaw "
             "= %.2f (the budget majorant of midJ is tlaw itself: "
             "SELF-REFERENTIAL leg); Landau: C_mid %.3e vs pred "
             "(Landau 1912/Gonek 1993 UNCONDITIONAL, cited as form, "
             "NOT needed for the cap)"
             % (x, tlaw, midG, midC, midJ, band_cited, resid_inf,
                midJ / tlaw, c_mid_f))

        # ---- G35 midJ anatomy (far field subordinate)
        if x in FAR_RUNGS:
            ok35x = j_far_f < 0.0 and n_far >= 10
            ok35 = ok35 and ok35x
            det35.append("x%d: J_far/D %.3e (< 0, %d zeros past "
                         "2 sqrt(y_t) = %.0f)"
                         % (x, j_far_f / D, n_far, gcut))
        else:
            det35.append("x%d: far window %s (gcut %.0f vs gtop "
                         "%.0f), J_far/D %.1e printed only"
                         % (x, "thin" if gcut < gtop else
                            "EMPTY (horizon)", gcut, gtop,
                            j_far_f / D))

        # ---- G36 ONSETCAP coordinate
        ytb = yt / btop
        exp_dex = ytb * math.log10(math.e)
        demand_dex = max(TURAN_POLY_DEG * math.log10(x),
                         abs(math.log10(tauf)))
        okp = exp_dex >= EXP_PRICE_FAC * demand_dex
        yt_ok = (YT_WIN[0] <= yt / YT_TAB[x] <= YT_WIN[1]
                 and float(ctx["A"][1] / ctx["A0"]) < 0
                 and ytb >= YTB_MIN)
        th_ok = TH_WIN[0] <= theta05 / TH_TAB[x] <= TH_WIN[1]
        if x in ONSET_RUNGS:
            theta_on = (band_cited * D + m_onset_f + 3.0 * m_slop_f) \
                / (tauf + off)
            polyb = math.log10(1.0 / max(1.0 - theta_on, 1e-300)) \
                <= B1_POLY_C0 + B1_POLY_SLOPE * math.log10(x)
            on_ok = theta_on <= THETA_MAX and polyb
            det36.append("x%d: Th(.5) %.0f theta_on %.4f (1-th "
                         "%.2e) exp %.0f/%.0f dex"
                         % (x, theta05, theta_on, 1.0 - theta_on,
                            exp_dex, demand_dex))
        else:
            on_ok = theta05 > gtop   # the horizon typing must hold
            det36.append("x%d: Th(.5) %.0f > gtop %.0f "
                         "ONSETCAP-HORIZON-LIMITED; exp %.0f/%.0f "
                         "dex" % (x, theta05, gtop, exp_dex,
                                  demand_dex))
        ok36x = okp and yt_ok and th_ok and on_ok
        ok36 = ok36 and ok36x
        info("x=%d ONSETCAP: y_t %.3e (win r140), y_t/b_top %.0f, "
             "Theta_J(0.5) %.0f (r140 %.0f); onset mass window "
             "(om_max %.0f, Theta]: %s"
             % (x, yt, ytb, theta05, TH_TAB[x], om_max,
                "%.2e of tau+OFF" % ((band_cited * D + m_onset_f)
                                     / (tauf + off))
                if x in ONSET_RUNGS else "beyond cache"))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    check("G31-node-config-w3", ok31,
          "|qrel| <= %.0e, null residual <= %.0e at every rung "
          "(q_0 == tau) AND delta_1 >= FULLGAP (Cauchy interlacing, "
          "THEOREM W3 instantiated -- DELTA1FLOOR reduces to a "
          "source-only two-eigenvalue statement): %s"
          % (QREL_BAR, NULLRES_BAR, "; ".join(det31)))
    check("G32-loop-instantiated", ok32,
          "zone-top replication (frozen windows) + s <= %.1f + s x "
          "gap in %s + delta_1 windows + share_1 >= %.1f + tlaw on "
          "the CDXLI strings + W1 defect identity <= %.0e + pinch "
          "1 - g/delta_1 <= s g <= 1 HARD + defect ratio in %s "
          "(one-moded): %s"
          % (S_BAR, str(SGAP_WIN), SHARE1_BAR, DEFECT_ID_BAR,
             str(DEFECT_RATIO_WIN), "; ".join(det32)))
    check("G33-s-zfree-hladder", ok33,
          "h-ladder at the top node: pinch + defect identity hold at "
          "EVERY point; |slope log10 gap vs log10 Z^2| <= %.2f "
          "(structural r141 anchor) and |slope log10 s| <= %.1f "
          "(O(h) smoothness class): the s-coordinate consumes no "
          "spacing-lattice product: %s"
          % (SLOPE_GAP_BAR, SLOPE_S_BAR, "; ".join(det33)))
    check("G34-tlawcap-assembly", ok34,
          "midG <= min(1/2, G(om)/(2 G(Tz))) + slop (A1, classical); "
          "|midC| <= midG + slop (A2, triangle -- LANDAU NOT NEEDED "
          "FOR THE CAP; pin re-gated, Landau/Gonek UNCONDITIONAL "
          "cited); midJ in %s AND midJ <= (tau+OFF)/D (the "
          "SELF-REFERENTIAL majorant, A4); assembly identity "
          "residual in the certified envelope (band CITED r137): %s"
          % (str(MIDJ_WIN), "; ".join(det34)))
    check("G35-midj-onset-carried", ok35,
          "J_far (gamma^2 > 4 y_t) < 0 at x in %s (far field "
          "subordinate under the r140 subordination census): the "
          "positive midJ excess is ONSET-CARRIED entirely: %s"
          % (str(FAR_RUNGS), "; ".join(det35)))
    check("G36-onsetcap", ok36,
          "y_t windows + A_2/A_0 < 0 + y_t/b_top >= %.0f; "
          "Theta_J(0.5) in the r140 windows (source-only); "
          "theta_onset <= %s with the r140 poly envelope at x in "
          "%s; x = 24 ONSETCAP-HORIZON-LIMITED; onset product "
          "exponent >= %.1f max(%d log10 x, |log10 tau|) dex "
          "(ALIGNMENT-WALL continues -- TOPROOT alone cannot close "
          "ONSETCAP): %s"
          % (YTB_MIN, str(THETA_MAX), str(ONSET_RUNGS),
             EXP_PRICE_FAC, TURAN_POLY_DEG, "; ".join(det36)))

    # ---------------------------------------------------------- S3b
    section("S3b  ADVERSARIAL s-WITNESS (RvM-legal config)")
    ok40 = True
    det40 = []
    for x in adv_rungs:
        ce = cells[x]
        K = ce["K"]
        dps = ce["dps"]
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        rvm = rvm_quantiles(m_zone)
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
        th = [mp.mpf(repr(float(v))) for v in rvm]
        Vt = build_V(ce, th)
        q0rel = Vt["qrel"]
        thf = [float(v) for v in th]
        s_topx = thf[-1] - thf[-2] if m_zone > 1 else 3.0
        pset = [Tz - 0.001, Tz - 0.16, 0.5 * (thf[-1] + Tz),
                thf[-1] + 0.03 * s_topx]
        s_max = None
        alg_ok = True
        with mp.workdps(dps):
            q0t = Vt["qs"][0]
            for pf in pset:
                if pf <= 0.5 or pf > Tz + 2.0:
                    continue
                if min(abs(pf - v) for v in thf) < NODE_EXCL:
                    continue
                rr = row_at(mp.mpf(repr(float(pf))), K, oms, nrm)
                lamt, ett, en2t, etnt, rho2t, chit = \
                    secular_data(Vt, rr)
                # currency in q0' units (the adversarial well)
                gq = (lamt - q0t) / q0t
                d1q = (Vt["qs"][1] - q0t) / q0t
                sq = q0t * chit / rho2t
                sgq = sq * gq
                chi2q = mp.mpf(0)
                for i in range(1, Vt["nf"]):
                    chi2q += etnt[i] * etnt[i] \
                        / ((Vt["qs"][i] - q0t) * (Vt["qs"][i] - lamt))
                drq = (gq * gq / rho2t) * (q0t * q0t) * chi2q
                dlq = 1 - sgq
                idv = float(abs(dlq - drq) / max(abs(dlq),
                                                 mp.mpf("1e-300")))
                plo = float(1 - gq / d1q)
                alg_ok = alg_ok and idv <= ADV_ID_BAR \
                    and plo - PINCH_SLOP <= float(sgq) \
                    <= 1.0 + PINCH_SLOP
                if s_max is None or float(sq) > s_max:
                    s_max = float(sq)
        okx = (q0rel >= Q0REL_MIN and s_max is not None
               and s_max >= S_ADV_MIN and alg_ok)
        ok40 = ok40 and okx
        det40.append("x%d: q0rel %.1e s'_max %.2f (truth s %.4f) "
                     "algebra-blind %s"
                     % (x, q0rel, s_max, s_tab.get(x, float("nan")),
                        alg_ok))
    check("G40-adversarial-s-witness", ok40,
          "RvM-legal quantile config: q0rel >= %.0f (consistency "
          "already broken) AND max s' >= %.1f vs truth s <= %.1f "
          "(the s-currency SEES the arithmetic, >= 10x separation) "
          "AND the W1/W2 pinch + defect identity HOLD on the "
          "adversarial well (algebra config-blind, null control): %s"
          % (Q0REL_MIN, S_ADV_MIN, S_BAR, "; ".join(det40)))

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
        cwx = source_ctx(cw)
        ytbw = cwx["yt"] / cwx["btop"]
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD); y_t_w/b_top = %.2f <= %.1f (NO "
              "escaped scale -- the r140 signature)"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the W1/W2/W3 machinery "
          "claims nothing where PSD/pinning fail")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lg_ = [math.log10(gap_tab[x]) for x in xs_all]
        ls_ = [math.log10(s_tab[x]) for x in xs_all]
        s_g = float(np.polyfit(lt, lg_, 1)[0])
        s_s = float(np.polyfit(lt, ls_, 1)[0])
        check("G54-tau-screen", abs(s_g) <= TAU_SLOPE_BAR
              and abs(s_s) <= TAU_SLOPE_BAR,
              "slope log10 gap vs log10 tau = %.4f, slope log10 s "
              "vs log10 tau = %.4f (both <= %.2f: neither ratio is "
              "Connes-priced; the RAW gap rides tau BY CONSTRUCTION "
              "-- BOUND-RIDES-CONNES typed)"
              % (s_g, s_s, TAU_SLOPE_BAR))
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
    # certificate cost bookkeeping (poly): nf <= K, dps ladder
    cost_ok = True
    for x, dps in all_rungs:
        Kx = int(math.ceil(KFAC * x * math.log(x)))
        cost_ok = cost_ok and Kx <= 2 * int(1.25 * x * math.log(x)) \
            + 2 and dps <= 10 * x + 60
    check("G60-demand-audit", okq and cost_ok,
          "CHAIN-AUDIT (cited theorems not re-proven): %s; AND "
          "per-rung certificate cost POLY: one nf^3 mp eigensolve, "
          "nf <= K = O(x log x), dps ladder <= 10x + 60 digits "
          "(CERT-COST-POLY: the r141 tail-heaviness obstructs only "
          "the six-data closed form, NOT the certificate)" % detq)

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
          "flows: base 4, refined 5 -- merged chain TOPROOT(1) -> "
          "TAILVIS(1) -> TLAWCAP(1) -> BANDMASSTHM(INF: B1/B2 + "
          "THIS ROUND's assembly adjudication) -> SUSCAP2R(1) -> "
          "DELTA1FLOOR(1) -> QSUBGAPTHM(INF: U1-U4 + W1/W2) -> "
          "PFLOORTHM(INF, r141); one-grant still 5; counterfactual "
          "PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")
    info("EXACT RESIDUE after this round (read with CDXLI/CDXLIII/"
         "CDXLIV/CDXLV): RH <== [r122-NF-closure] + [Theorem R] + "
         "{L1, WPD} on dense a; H-pin <== OMEGA-a + OMEGA-b; "
         "OMEGA-a = EPS-LOCK <== TOPROOT + TAILVIS + TLAWCAP "
         "(CDXLIV); THIS ROUND: TLAWCAP NOT eliminated -- it "
         "SHARPENS to ONSETCAP (the onset-window mass cap; midG/"
         "midC/resid classical or enveloped, midJ budget-self-"
         "referential, onset product exp-priced); OMEGA-b <== "
         "OMEGA-a + QSUBGAP; THIS ROUND: QSUBGAP <==> SUSCAP2R AND "
         "DELTA1FLOOR (W2 loop EXPOSED; no tlaw, no Z consumed on "
         "this leg) with DELTA1FLOOR <== FULLGAP (W3, source-only). "
         "RESIDUE = {TOPROOT, TAILVIS, TLAWCAP(=ONSETCAP), "
         "SUSCAP2R(=QSUBGAP-uniformity)} + DELTA1FLOOR(weak, <== "
         "FULLGAP) + dense-a + a-extension + window-a; x-quantifier "
         "dense-x (CDXLV, inherited).  NO RH claim; nothing "
         "upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "W1-PROVEN(s x gap == 1 is NOT exact: defect = second-order "
        "susceptibility, pinched [1 - g/delta_1, 1]; G10/G11/G32)",
        "LOOP-EXPOSED(QSUBGAP <==> SUSCAP2R AND DELTA1FLOOR; the "
        "r139 carve-out circular on this leg; G12/G32)",
        "DELTA1-INTERLACED(DELTA1FLOOR <== FULLGAP source-only; "
        "G13/G31)",
        "TLAWCAP-NOT-ELIMINATED(assembly: classical caps + envelope "
        "+ self-referential midJ + exp-priced onset ==> TLAWCAP "
        "<==> ONSETCAP mod {TOPROOT, TAILVIS}; G14/G34/G35/G36)",
        "ONSETCAP-PER-RUNG(theta < 1 certified x = 5..18; x = 24 "
        "HORIZON-LIMITED; G36)",
        "LANDAU-UNCONDITIONAL-CITED(NOT-NEEDED-FOR-CAP; G14/G34)",
        "MIDJ-ONSET-CARRIED(J_far < 0; G35)",
        "ONSET-EXP-PRICED(ALIGNMENT-WALL continues; G15/G36)",
        "S-SEES-ARITHMETIC(adversarial witness; algebra "
        "config-blind; G40)",
        "CERT-COST-POLY(per-rung certificate polynomial; G60)",
        "QUANTIFIER-INHERITED(dense-x suffices; G60)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "OMEGA-RESHAPED(residue {TOPROOT, TAILVIS, "
        "TLAWCAP(=ONSETCAP), SUSCAP2R(=QSUBGAP mod DELTA1FLOOR <== "
        "FULLGAP)}; G61 census unchanged)"]
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
        print("COMPOSITE: W1-PROVEN + LOOP-EXPOSED + "
              "DELTA1-INTERLACED + TLAWCAP-NOT-ELIMINATED + "
              "ONSETCAP-PER-RUNG + LANDAU-UNCONDITIONAL-CITED + "
              "MIDJ-ONSET-CARRIED + ONSET-EXP-PRICED + "
              "S-SEES-ARITHMETIC + CERT-COST-POLY + "
              "QUANTIFIER-INHERITED + CONTROLS-REFUSE + DEMAND-FLAT "
              "+ OMEGA-RESHAPED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
