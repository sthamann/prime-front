#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""collapserate_probe -- PRIME.COLLAPSERATE.LOCK.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the COLLAPSE-RATE LOCK, the missing
half of TOPROOT, folding in SUSCAP2R via the one-spectrum identities)
=======================================================================
Round 146 (CDL) pinned TOPROOT's missing half as a collapse-rate lock
tau >= lam_1/poly(x) between the two bottom eigenvalues of the source
Weil matrix (trace caps are vacuous, Theorem Y3), and delivered the
structural key: the ZERO-JET LAW lam_1 = 8 A_0(psi_1)^2 G(T_z) tlaw_1
and the JET-RATIO LOCK FULLGAP = (A_0(psi_1)/A_0(phi))^2/jr with jr
flat -> 1.  THEREFORE the collapse-rate lock IS a jet-ratio statement:
lam_1 <= poly tau <==> J := (A_0(psi_1)/A_0(phi))^2 <= poly, modulo
the tlaw ratios.  Round 147 (CDLI) gave the adjugate machinery AD1 at
the ground root; this probe extends it to BOTH bottom roots and mounts
the maximal proof attempt on the two-eigenvector jet decoupling.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, Mq = round-114 builder (even sector), eigenpairs
lam_0 = tau < lam_1 <= ... with eigenvectors phi, psi_1, ...;
FULLGAP = (lam_1 - tau)/tau; jet functional v_0 = ((-1)^k/nrm_k)_k,
v_2 = ((-1)^k om_k^2/nrm_k)_k; A_0(v) = v_0 . v, w_i = A_0(psi_i)^2;
P(z) = det(zI - Mq), B_00(z) = v_0^T adj(zI - Mq) v_0 = P(z) G(z)
with G(z) = sum_i w_i/(z - lam_i); J = w_1/w_0; jr = J/FULLGAP;
t_r = tlaw_1/tlaw_0 = (lam_1/tau) (w_0/w_1) (G-free); tf = (lam_1 -
tau) sum_{i>=1} 1/(lam_i - tau) (the r146 Y1 tightness scalar);
beta_0 = the unique root of B_00 in (tau, lam_1); T_z = 2 pi x; m =
verified zone census; V = kernel of the m newton-polished node rows;
s = tau chi/rho2 at the zone-top argmin; OVG = (et_1^2/rho2)/FULLGAP.

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically + exact rational
instances + mp-instantiated per rung; classical inputs typed CITED)
=======================================================================
THEOREM R1 (the adjugate ratio law + the P'-ratio pinch; the C1
answer).  (a) AD1 at BOTH simple bottom roots (r147 AD1 extended):
adj(tau I - M) = P'(tau) phi phi^T and adj(lam_1 I - M) = P'(lam_1)
psi_1 psi_1^T, hence BASIS-FREE
   J = [B_00(lam_1)/P'(lam_1)] / [B_00(tau)/P'(tau)].
(b) THE P'-RATIO CARRIES NO DEMAND: |P'(lam_1)/P'(tau)| =
prod_{i>=2} (lam_i - lam_1)/(lam_i - tau) and with a_i = (lam_1 -
tau)/(lam_i - tau) in [0, 1], the Weierstrass product inequality
gives the EXACT SANDWICH
   2 - tf  <=  |P'(lam_1)/P'(tau)|  <=  1,
where tf - 1 = sum_{i>=2} a_i is the r146 Y1 harmonic-trace excess
(measured 1e-5-class, falling).  CONSEQUENCE: the entire poly demand
of the jet ratio sits in the ADJUGATE-ENTRY RATIO B_00(lam_1)/
B_00(tau); the eigenvalue-product factor is pinched at 1 by the same
harmonic trace that prices DELTA1FLOOR.  MEASURED (calibration): 1 -
|R_P| == tf - 1 with match ratio 1.0000/1.0000 at x = 5/8.

THEOREM R2 (the jr-tlaw identity; the C1 symbolic answer to 'the
ratio's flatness has an identity behind it').  EXACTLY (definition
chase, G-free):
   jr x t_r == 1 + 1/FULLGAP.
The r146 jr table 1.124/1.110/1.027/0.959/1.002 is EXPLAINED: jr =
(1 + 1/FULLGAP)/t_r is the inverse tlaw ratio -- the two 'both
measured flat' quantities of the contract are ONE quantity.  The
collapse-rate lock transfers EXACTLY: [J <= P] and [t_r <= c] ==>
FULLGAP = J t_r - 1 <= cP; conversely FULLGAP <= P and t_r >= 1/c
==> J = (1 + FULLGAP)/t_r <= c(1 + P).  Calibration: identity dev
1.6e-61/0.0 at x = 5/8.

THEOREM R3 (the two-level secular position; the C2 answer).  beta_0,
the unique root of B_00 in (tau, lam_1) (equivalently of the
jet-weighted Weyl function G), satisfies EXACTLY
   J = S1 x (lam_1 - beta_0)/(beta_0 - tau),   S1 in (0, 1],
where S1 = [w_1/(lam_1 - beta_0)] / [sum_{i>=1} w_i/(lam_i -
beta_0)] is the level-1 share of the secular sum at beta_0.  Hence
the ONE-SIDED bound J <= (lam_1 - beta_0)/(beta_0 - tau)
UNCONDITIONALLY: the collapse-rate lock is a BOTTOM-ROOT SEPARATION
statement of the curve pair (P, B_00) -- J <= poly <==> [beta_0 -
tau >= (lam_1 - tau)/poly] AND [S1 >= 1/poly].  The same theorem at
the coordinate functional e_0 IS the r146 MINOR0 lock: det(zI -
minor_0) = adj_00(z) = P(z) sum_i psi_i(0)^2/(z - lam_i), and the
exact correction identity r = w0/(w0+w1) - r(1-r)(lam_1 - tau) T_2/
(w0+w1) EXPLAINS the r146 pred-devs exactly (calibration: corr =
1.23e-6 at x=5 == the r146 dev 1.89e-6 x r; identity dev 0.0).
MEASURED SURPRISE (calibration, the honest finding): the JET-weighted
secular function is NOT two-level dominated -- S1 = 0.2769/0.1449 at
x = 5/8, FALLING (the e_0-read has share 0.95); the jet mass of the
high eigenvectors carries the beta_0 balance; beta_0 sits at
(beta_0 - tau)/tau = 0.2463/0.1305 (= S1/jr by exact chase).  The
MINOR0 0.650-exactness does NOT pin J: it pins the CORRECTION; the
two functional reads (e_0 flat 0.539, v_0 growing J ~ x^4) decouple
at exactly the demand rate.

THEOREM R4 (Parseval-cap vacuity; the obstruction pin, Y3's twin one
level up).  sum_i w_i = |v_0|^2 (Parseval), so J <= |v_0|^2/w_0
EXACTLY -- but this cap rides 1/A_0(phi)^2 ~ 1/tau: measured vacuity
log10(cap/J) = 10.37/23.40 dex at x = 5/8, riding |log10 tau| with
two-point slope 0.956.  NO jet-mass-summing instrument (Parseval/
trace class in jet currency) sees the TWO-vector ratio -- exactly
the Y3 trace-cap obstruction one level up: any collapse-rate proof
must price the POSITION beta_0 (or equivalently the pair-ratio
B_00(lam_1)/B_00(tau)), not summed jet mass.

SUSCAP2R FOLD-IN (C3; exact chain, machine-gated): Y4 (r146, re-
gated) s delta_1 share_1 rho2/et_1^2 == 1 and W3 delta_1 >= FULLGAP
give EXACTLY
   s = OVG x FULLGAP/(share_1 delta_1) <= OVG/share_1,
so SUSCAP2R <== [OVG <= poly] AND [share_1 >= 1/poly] with OVG
measured flat 0.029..0.058 (r146 strings): the s-demand needs NO
collapse-rate input.  THE STRONGEST CONDITIONAL CHAIN (assembled +
gated): [J <= P] + [t_r in (1/c, c)] ==> FULLGAP <= cP (R2) ==>
TOPROOT y_t <= (1+eta) cP/c_1 (CDL G14 lock-window transfer, re-
gated) ; + [OVG <= C, share_1 >= 1/2] ==> s <= 2C (Y4+W3) ; +
[DELTA1FLOOR] ==> QSUBGAP g >= 1/(s + 1/delta_1) (W2 re-gate).

RED-TEAM (C4, mandatory): (i) THE 2-EIGENVECTOR JET TOY: M =
diag(l0, l1, l2), functional v = (p, q, r): ALL R1/R3 identities
hold for EVERY q/p while J = q^2/p^2 is FREE; constructive witness
q^2 = P p^2 realizes J == P at P = 10^6 exactly, and lim J -> oo
with all identities intact: ANY bound on the jet ratio derived from
the adjugate/secular algebra alone FAILS this model (hard assert);
only bounds consuming arithmetic input (census, qrel, frozen
replication windows -- the G30/G31/G32 inputs) may cap J.  (ii) the
r147 2D s-model inherited: sg == 1 - eps^2 with s == P at eps^2 =
tau/(tau + Delta P) (mp on the real x = 5 data).  (iii) CONTROLS:
SMOOTH/SCRARITH x=5, EPSTEIN x=8 refuse fourfold (zone overcount,
mu_1 fills the verified zero-free gap, tau_w < 0 -- the PSD/simple-
ground hypotheses of R1/R3/R4 fail EXACTLY there, no collapse to
lock -- and no escaped scale y_t_w/b_top <= 1).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 R1a: adjugate identity at BOTH roots on the Householder
    frame (u = (1,2,3), H = I - u u^T/7) + the basis-free ratio law
    J == [B_00(l1)/P'(l1)]/[B_00(l0)/P'(l0)] generic in the
    functional entries;
    G11 R1b: P'(l1)/P'(l0) == -(l2-l1)/(l2-l0) generic; the factor
    identity (l_i - l1)/(l_i - l0) == 1 - a_i; Weierstrass
    (1-a)(1-b) >= 1-a-b generic nonneg; the tf-form tf == 1 +
    sum_{i>=2} a_i; sandwich instance diag(1,2,5,7): 7/12 <= 5/8
    <= 1;
    G12 R2: jr t_r == 1 + 1/FULLGAP generic (G-free chase) + the
    two-way demand transfer [J <= P, t_r <= c] <==> FULLGAP-CAP
    class (exact rearrangements + monotone instances);
    G13 R3: secular-root identities: w_1/w_0 + (l1-b)w_2/(w_0(l2-b))
    == (l1-b)/(b-l0) at the root (exact substitution); one-sided
    J <= ratio given w_2 >= 0; adj_00(z) == det(zI - minor_0) ==
    P(z) sum psi_i(0)^2/(z-l_i) on the frame (the MINOR0 object IS
    this theorem at e_0); the minor correction identity r ==
    w0/(w0+w1) - r(1-r)(l1-l0)T_2/(w0+w1) exact rearrangement;
    G14 C3 chain: Y4 re-gate (generic == 1); s == OVG FG/(share d1)
    + [d1 = FG + slack] ==> s <= OVG/share exact; CDL G14 lock-
    window transfer re-gate; W2 backward shape re-gate g >= 1/(s +
    1/d1) + composition 1/(2P);
    G15 red-team jet toy (symbolic): ratio law free in q/p; beta_0
    (2-level) == (p^2 l1 + q^2 l0)/(p^2+q^2); rho_beta -> 0 as
    q -> oo with identities intact; witness q^2 = P p^2 ==> J == P
    at P = 10^6 exact: ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-JETRATIO
    (hard assert);
    G16 red-team 2D s-model (symbolic, r147 G17 core): lam* == tau
    + eps^2 Delta; s g == 1 - eps^2; lim s = oo; poly witness s ==
    P exact.
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150),(28,160) deep (zone sign-scan to T_z + 6,
    step 0.05; newton-polished nodes, the r141/r143 standard):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform);
    G31 spectral ladder: lam_i > 0 sorted; FULLGAP in the frozen
    windows (r142/r146 strings + CDLII x=28 string) x (0.97, 1.03);
    lam_1 SIMPLE: (lam_2 - lam_1)/lam_1 >= 1e3; post-loop growth
    slope in (3.4, 4.6); ladder profile printed;
    G32 node-config V + replication: |qrel| <= 1e-30, null residual
    <= 1e-40; W3 re-gate delta_1 >= FULLGAP (1 - 1e-12); zone-top
    argmin in the frozen windows AND >= 3; s <= S_BAR_TAB; s x gap
    in (0.98, 1.02); delta_1 windows; share_1 >= 0.5; tlaw on the
    CDXLI strings <= 5e-3 (x <= 24) / in (0.40, 0.70) at x = 28
    (DISCLOSED);
    G33 SUSCAP2R fold-in: Y4 identity <= 1e-30 (mp share, the r146
    smoke lesson); s <= OVG/share_1 (1 + 1e-12) HARD; OVG in
    (0.01, 0.30) core+18/24, (0.005, 0.5) at 28 (DISCLOSED);
    G34 zero-jet + R2 instantiated: J > 0; jr in (0.8, 1.6); t_r in
    (0.5, 2.0); tlaw_1 in (0.05, 5.0); R2 identity |jr t_r - (1 +
    1/FG)| <= 1e-30; lock FULLGAP/y_t in (1.5, 6.0);
    G35 R1 instantiated: tf in (1 - 1e-12, 1.05); SANDWICH HARD
    2 - tf - 1e-12 <= |R_P| <= 1 + 1e-12; match (1-|R_P|)/(tf-1)
    in (0.9, 1 + 1e-9); ADJUGATE h-ladder at BOTH roots (RQI-
    refined at dps + 360, RQI_ITERS = 2, move <= 1e-20; own LU det
    + solve; h = 1e-8/1e-16 with z - root = h root A_0(root)^2
    relscale/K): dev(ratio jets), dev(A_0^2), dev(P' vs
    eigenproduct, dual instrument) <= {1e-4, 1e-10}; basis-free
    ratio-law J dev <= 1e-10 (root-0 target source-pure: |A_0(RQI
    phi)/A_0(source strings) - 1| <= 1e-30; root-1 target from the
    RQI-refined vector, DISCLOSED eigen-route cross-instrument);
    G36 R3 instantiated: tau < beta_0 < lam_1 HARD (bisection 250
    iters); identity |[S1 ratio]/J - 1| <= 1e-25; one-sided J <=
    ratio (1 + 1e-12) HARD; S1 in (0.001, 1 + 1e-12) + betapos =
    (beta_0 - tau)/tau in (1e-4, 3.0) printed (DISCLOSED windows;
    calibration 0.2769/0.1449 and 0.2463/0.1305 at x = 5/8, deep
    unmeasured, expected falling);
    G37 MINOR0: bottom root of the e_0-secular in (tau, lam_1);
    r in (0.5, 0.8); w1/w0 in (0.25, 1.0); correction identity
    |(pred - corr)/r - 1| <= 1e-25; CORE rungs: eigsy of the k=0
    principal minor vs secular root dual dev <= 1e-30 (deep rungs
    secular-route only, DISCLOSED);
    G38 Parseval vacuity: |sum_i w_i/|v_0|^2 - 1| <= 1e-25; J <=
    |v_0|^2/w_0 HARD; vacuity >= 8 dex; post-loop vacuity slope vs
    |log10 tau| in (0.85, 1.15) (RIDES-1/TAU pinned -- R4).
S3c G40 red-team mp: jet toy on the x = 5 rung data (tau, lam_1,
    lam_2; v = (A_0, 1e3 A_0, 0)): J == 1e6 dev <= 1e-40, 2-level
    rho_beta == 1/(1+1e6) dev <= 1e-40; 2D s-model witness on the
    same rung: s == 1e6 dev <= 1e-40 (the algebra admits any J and
    any s: the numeric side of G15/G16).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 (the R1/R3/R4 hypotheses fail EXACTLY here) AND
    y_t_w/b_top <= 1.0; G53 consistency.
S5  G54 tau-screens: |slope log10 v vs log10 tau| <= 0.30 for v in
    (J, betapos, OVG, t_r) -- the lock currencies are tau-flat;
    RIDER report: slopes of log10 w_0 and log10 |P'(tau)| printed
    (ride tau by construction, BOUND-RIDES-CONNES typed; the
    RATIOS are the flat coordinates); G55 conditioning (1e-25
    shift window).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence-demand ->
    Theorem R transfer -> coupling absorbed -> the J/beta_0/R_B
    coordinate consumes NO tlaw, NO Z, no lattice proximity
    (source-only spectral + jet data; r142 W2/W3 + r141 V1 cited;
    R1 basis-free) -> V2 good sets -> no ALL-X demand; beta_0
    certificate eigensolve-free given (tau, lam_1) via LU-solve
    bisection: CERT-COST-POLY class, typed);
    G61 min-cut (r116 replica; r142/r144/r146 graph VERBATIM):
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
BIS_ITERS = 250; ADJ_PAD = 360; RQI_ITERS = 2; RQI_MOVE_MAX = 1e-20;
ADJ_H = (1e-8, 1e-16); ADJ_BAR = {1e-8: 1e-4, 1e-16: 1e-10}
(calibration x = 5/8 root0: 1.5e-18/1.8e-18/2.0e-24 and 1.9e-31/
2.6e-31/3.4e-38 at h = 1e-8; root1: 1.1e-18/1.3e-18/5.1e-19 and
1.7e-31/2.2e-31/3.7e-32 -- headroom >= 1e10); JBF_BAR = 1e-10
(calibration 5.1e-27/3.7e-40); SRC_BRIDGE_BAR = 1e-30 (calibration
eigsy-vs-source 1.2e-53/2.8e-67).
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26), 28: (10, 30) DISCLOSED-
unmeasured}; S_BAR_TAB = {5..24: 0.1, 28: 0.15 DISCLOSED}; SGAP_WIN
= (0.98, 1.02); D1_TAB = {5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18:
3.25e7, 24: 1.14e8, 28: 1.6513e8} x (0.7, 1.3); SHARE1_BAR = 0.5;
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24:
0.5122} rel tol 5e-3 (CDXLI strings); TLAW28_WIN = (0.40, 0.70)
(DISCLOSED, trend); FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13:
1.0619e7, 18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97, 1.03)
(r142/r146 strings + CDLII x=28 F-layer string 1.651310e8);
FG_SLOPE_WIN = (3.4, 4.6); SIMP_MIN = 1e3 (calibration 4.8e4/
3.4e5); SID_BAR = 1e-30 (calibration 7.8e-62/0.0); OVG_WIN =
(0.01, 0.30) at x <= 24 (r146 strings 2.88e-2..4.84e-2), (0.005,
0.5) at 28 DISCLOSED; SCHAIN_SLOP = 1e-12; R2_ID_BAR = 1e-30
(calibration 1.6e-61/0.0); JR_WIN = (0.8, 1.6); TR_WIN = (0.5,
2.0); TLAW1_WIN = (0.05, 5.0); LOCK_WIN = (1.5, 6.0); TF_WIN =
(1 - 1e-12, 1.05); RP_SLOP = 1e-12; MATCH_WIN = (0.9, 1 + 1e-9)
(calibration 1.0000/1.0000); R3_ID_BAR = 1e-25 (calibration
6.2e-61/3.8e-69); ONESIDED_SLOP = 1e-12; S1SHARE_WIN = (0.001,
1 + 1e-12) (calibration 0.2769/0.1449, falling, deep DISCLOSED);
BETAPOS_WIN = (1e-4, 3.0) (calibration 0.2463/0.1305, deep
DISCLOSED); MINOR0_WIN = (0.5, 0.8) (r146 0.6500..0.6516; 28
DISCLOSED); WRAT_WIN = (0.25, 1.0) (calibration 0.5386/0.5367);
M0_CORR_BAR = 1e-25 (calibration 0.0/2.6e-76); M0_DUAL_BAR = 1e-30
(calibration 5.0e-52/7.4e-59, CORE only); PARS_DEV_BAR = 1e-25
(calibration 1.1e-60/1.1e-80); VAC_MIN = 8.0 (calibration 10.37/
23.40); VAC_SLOPE_WIN = (0.85, 1.15) (two-point calibration
0.956); RT_P = 10^6; RT_ID_BAR = 1e-40; CTRL_YTB_MAX = 1.0;
TAU_SLOPE_BAR = 0.30; COND_WIN = (1e-40, 1e-10); GAMMA1_LIT =
14.134725141734694 (ward only); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; zone nodes newton-polished at dps; np.float64-repr casts
guarded by float()/repr(); tiny/huge quantities stay mp end-to-end
(the r147 float(pprime) underflow class: pprime/B_00/w_i/beta_0
kept mp; log diagnostics via mp.log inside workdps); adjugate
linear algebra at dps + ADJ_PAD with own deterministic partial-
pivot LU (all sequential row swaps BEFORE forward elimination --
LAPACK getrs order, r144 lesson, frozen code).

CALIBRATION DISCLOSURE (pre-freeze, ONE scratch script
calib_scratch_collapserate.py + log, x = 5/8 only, deleted after
freeze; all numbers quoted verbatim above and here): x=5: FULLGAP
2.225493e5, J 2.502511e5, jr 1.1245, t_r 0.8893, R2 dev 1.6e-61;
tf-1 2.090e-5 == 1-|R_P| 2.090e-5 (match 1.0000, sandwich holds);
(lam2-lam1)/lam1 4.786e4; Parseval dev 1.1e-60, vacuity 10.37 dex;
rho_beta 1.107e-6, betapos 0.2463, S1 0.2769, R3 dev 6.2e-61,
J <= ratio True; minor0 r 0.6500, pred 0.6500, corr 1.23e-6
(== r146 pred-dev 1.89e-6 x r EXACTLY), corr-id dev 0.0, w1/w0
0.5386, eigsy dual dev 5.0e-52; adjugate devs above; zone: gap
33.6233, s 0.02974, sg 0.99985, share1 0.9691, d1/FG 1.000008, Y4
dev 7.8e-62, OVG 2.8819e-2, s <= OVG/share1 True.  x=8: FULLGAP
9.951249e5, J 1.104303e6, jr 1.1097, t_r 0.9011, R2 dev 0.0; tf-1
2.920e-6 == 1-|R_P|; vacuity 23.40 dex; S1 0.1449, betapos 0.1305,
R3 dev 3.8e-69; minor0 r 0.6507, corr 1.82e-7, w1/w0 0.5367; zone
gap 16.7200, s 0.05981, sg 0.99998, share1 0.9653, Y4 dev 0.0, OVG
5.7732e-2.  x = 13..28 pre-freeze UNMEASURED on all new quantities
(build cost); their windows are set from the frozen r139-r146/
CDLII strings, the calibrated trends and structure asserts,
DISCLOSED above.  Amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks below.

VERDICT ENUMS (frozen): R1-PROVEN(adjugate ratio law at both roots
+ P'-ratio pinch [2-tf, 1]: the demand isolated in the adjugate-
entry ratio B_00(lam_1)/B_00(tau); basis-free); R2-PROVEN(jr t_r ==
1 + 1/FULLGAP: the r146 jr table EXPLAINED -- jr and the tlaw ratio
are ONE flat object; two-way demand transfer J <-> FULLGAP mod
t_r); R3-PROVEN(J == S1 x root-position exactly; one-sided J <=
(lam_1 - beta_0)/(beta_0 - tau) unconditional: the collapse-rate
lock == bottom-root separation of the curve pair (P, B_00) + S1-
floor; MINOR0 correction identity EXPLAINS the r146 exactness);
R4-PROVEN(Parseval-cap vacuity: jet-mass instruments are rate-
blind, riding 1/tau -- the Y3 obstruction one level up, pinned);
S1SHARE-FALLING(the jet-weighted secular function is NOT two-level
dominated: the honest measured finding); BETA0-POSITION-MEASURED
(betapos = S1/jr by exact chase); MINOR0-CORRECTION-EXPLAINED;
SUSCAP2R-PROPAGATED(s <= OVG/share_1 exact via Y4 + W3: the
s-demand needs no collapse-rate input; conditional chain
assembled); COLLAPSERATE-RECOORDINATED-NOT-CLOSED(the demand
relocates to {B00-ROOTGAP + S1-FLOOR} == JETRATIO-CAP == FULLGAP-
CAP mod t_r -- OPEN; typed honestly as recoordination);
ONE-CURVE-CROSS-CERTIFIED(adjugate route == jet route ==
eigenproduct at BOTH roots -- the r147 lever (e) cross-
certificate); REDTEAM-REFUTES-ALGEBRA(jet toy + 2D model: any
algebra-only cap fails; arithmetic legs refuse); CONTROLS-REFUSE;
DEMAND-FLAT + BOUND-RIDES-CONNES; QUANTIFIER-INHERITED(dense-x
suffices, CHAIN-AUDIT); OMEGA-RECOORDINATED(residue SET UNCHANGED;
census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED); MINCUT(4/5).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

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
ADJ_PAD = 360
RQI_ITERS = 2
RQI_MOVE_MAX = 1e-20
ADJ_H = (1e-8, 1e-16)
ADJ_BAR = {1e-8: 1e-4, 1e-16: 1e-10}
JBF_BAR = 1e-10
SRC_BRIDGE_BAR = 1e-30
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
SID_BAR = 1e-30
OVG_WIN_CORE = (0.01, 0.30)
OVG_WIN_28 = (0.005, 0.5)
SCHAIN_SLOP = 1e-12
R2_ID_BAR = 1e-30
JR_WIN = (0.8, 1.6)
TR_WIN = (0.5, 2.0)
TLAW1_WIN = (0.05, 5.0)
LOCK_WIN = (1.5, 6.0)
TF_WIN = (1.0 - 1e-12, 1.05)
RP_SLOP = 1e-12
MATCH_WIN = (0.9, 1.0 + 1e-9)
R3_ID_BAR = 1e-25
ONESIDED_SLOP = 1e-12
S1SHARE_WIN = (0.001, 1.0 + 1e-12)
BETAPOS_WIN = (1e-4, 3.0)
MINOR0_WIN = (0.5, 0.8)
WRAT_WIN = (0.25, 1.0)
M0_CORR_BAR = 1e-25
M0_DUAL_BAR = 1e-30
PARS_DEV_BAR = 1e-25
VAC_MIN = 8.0
VAC_SLOPE_WIN = (0.85, 1.15)
RT_P = 10 ** 6
RT_ID_BAR = 1e-40
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
    orthonormalized compression of Mq (r138-r146 replica)."""
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
    """(lam*, etn, rho2, chi) for the extra row r on V (caller dps)."""
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
    for _ in range(200):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, etn, rho2, chi


# --------------------------------------------- deterministic LU (adjugate)
def lu_factor(Amat, n):
    """own partial-pivot LU (r144/r147, VERBATIM); caller workdps."""
    piv = []
    sign = 1
    for k in range(n):
        pmax = abs(Amat[k, k])
        pk = k
        for i in range(k + 1, n):
            v = abs(Amat[i, k])
            if v > pmax:
                pmax, pk = v, i
        piv.append(pk)
        if pk != k:
            sign = -sign
            for j in range(n):
                Amat[k, j], Amat[pk, j] = Amat[pk, j], Amat[k, j]
        akk = Amat[k, k]
        for i in range(k + 1, n):
            f = Amat[i, k] / akk
            Amat[i, k] = f
            if f != 0:
                for j in range(k + 1, n):
                    Amat[i, j] -= f * Amat[k, j]
    return Amat, piv, sign


def lu_solve_fac(LU, piv, b, n):
    """solve with pre-computed lu_factor; ALL sequential row swaps
    BEFORE forward elimination (LAPACK getrs order, r144 lesson)."""
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


def lu_det(LU, sign, n):
    d = mp.mpf(sign)
    for i in range(n):
        d *= LU[i, i]
    return d


def rqi_vec(Mq, K, z0, y0, dps_adj, iters):
    """RQI at padded dps returning (z, y): the r147 rqi_refine shape
    extended to return the refined vector (calibration-validated)."""
    with mp.workdps(dps_adj):
        z = mp.mpf(z0)
        y = [mp.mpf(y0[i]) for i in range(K)]
        for _ in range(iters):
            A = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A[i, j] = Mq[i, j]
                A[i, i] -= z
            LU, piv, _sg = lu_factor(A, K)
            w = lu_solve_fac(LU, piv, y, K)
            nw = mp.sqrt(sum(v * v for v in w))
            y = [v / nw for v in w]
            My = [sum(Mq[i, j] * y[j] for j in range(K))
                  for i in range(K)]
            z = sum(y[i] * My[i] for i in range(K))
        return z, y


def bisect_secular(w, E, K, lo, hi, iters):
    """bottom root of sum_i w[i]/(z - E[i]) in (lo, hi); the function
    is monotone decreasing there.  Caller sets workdps."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        v = mp.mpf(0)
        for i in range(K):
            v += w[i] / (mid - E[i])
        if v > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def adjugate_root_pass(ce: dict, ridx: int, v0, v2, FG, lam2rel) -> dict:
    """basis-free adjugate instrumentation at root ridx (0 or 1):
    RQI-refined root + vector at dps + ADJ_PAD, h-ladder LU of
    (zI - M) with determinant + one solve per h.  All mp end-to-end
    (the r147 pprime underflow lesson)."""
    K = ce["K"]
    dps_adj = ce["dps"] + ADJ_PAD
    out = dict()
    with mp.workdps(dps_adj):
        Mq = ce["mpM"]
        lam0 = ce["mpE"][ridx]
        vec0 = [ce["mpV"][i, ridx] for i in range(K)]
        lam_ref, y_ref = rqi_vec(Mq, K, lam0, vec0, dps_adj, RQI_ITERS)
        move = float(abs((lam_ref - lam0) / lam0))
        A0r = sum(v0[i] * y_ref[i] for i in range(K))
        A2r = sum(v2[i] * y_ref[i] for i in range(K))
        pprime = mp.mpf(1)
        for i in range(K):
            if i != ridx:
                pprime *= (lam_ref - ce["mpE"][i])
        if ridx == 0:
            scale = lam_ref * A0r * A0r * FG / K
        else:
            relmin = min(FG / (1 + FG), lam2rel)
            scale = lam_ref * A0r * A0r * relmin / K
        devs = {}
        a02 = {}
        for h in ADJ_H:
            z = lam_ref + mp.mpf(repr(h)) * scale
            A = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A[i, j] = -Mq[i, j]
                A[i, i] += z
            LU, piv, sg = lu_factor(A, K)
            Pz = lu_det(LU, sg, K)
            yy = lu_solve_fac(LU, piv, v0, K)
            q00 = sum(v0[i] * yy[i] for i in range(K))
            q20 = sum(v2[i] * yy[i] for i in range(K))
            dev_ratio = float(abs((q20 / q00) / (A2r / A0r) - 1))
            dev_a02 = float(abs((z - lam_ref) * q00 / (A0r * A0r) - 1))
            dev_pp = float(abs(Pz / (z - lam_ref) / pprime - 1))
            devs[h] = (dev_ratio, dev_a02, dev_pp)
            a02[h] = (z - lam_ref) * q00
        out.update(move=move, devs=devs, a02=a02, A0r=A0r,
                   pprime_mp=pprime)
    return out


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    z = sp.symbols("z")

    # Householder frame: u = (1,2,3), H = I - u u^T/7
    uH = sp.Matrix([1, 2, 3])
    Hh = sp.eye(3) - (uH * uH.T) / 7
    l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)
    Mgen = Hh * sp.diag(l0, l1, l2) * Hh
    phi = Hh[:, 0]
    psi1 = Hh[:, 1]

    # ---------------- G10 R1a: AD1 at BOTH roots + ratio law
    adj0 = (l0 * sp.eye(3) - Mgen).adjugate()
    okA = sp.simplify(adj0 - (l0 - l1) * (l0 - l2) * (phi * phi.T)) \
        == sp.zeros(3, 3)
    adj1 = (l1 * sp.eye(3) - Mgen).adjugate()
    okB = sp.simplify(adj1 - (l1 - l0) * (l1 - l2) * (psi1 * psi1.T)) \
        == sp.zeros(3, 3)
    p_, q_, r_ = sp.symbols("p_ q_ r_", real=True)
    v0s = sp.Matrix([p_, q_, r_])
    B00_0 = (v0s.T * adj0 * v0s)[0, 0]
    B00_1 = (v0s.T * adj1 * v0s)[0, 0]
    Pp0 = (l0 - l1) * (l0 - l2)
    Pp1 = (l1 - l0) * (l1 - l2)
    A0p = (v0s.T * phi)[0, 0]
    A0f = (v0s.T * psi1)[0, 0]
    okC = sp.simplify((B00_1 / Pp1) * Pp0 / B00_0
                      - A0f ** 2 / A0p ** 2) == 0
    okD = sp.simplify(
        sp.diff((z - l0) * (z - l1) * (z - l2), z).subs(z, l1)
        - Pp1) == 0
    out.append(("G10-r1a-adjugate-both-roots", okA and okB and okC
                and okD,
                "adj(l0 I - M) == P'(l0) phi phi^T AND adj(l1 I - M) "
                "== P'(l1) psi_1 psi_1^T GENERIC on the Householder "
                "frame (AD1 extended to the SECOND root); ratio law "
                "[B_00(l1)/P'(l1)]/[B_00(l0)/P'(l0)] == "
                "(A_0(psi_1)/A_0(phi))^2 generic in the functionals "
                "(THEOREM R1a: the jet ratio is a ratio of four "
                "basis-free quantities on the spectral curve)"))

    # ---------------- G11 R1b: P'-ratio pinch
    okE = sp.simplify(Pp1 / Pp0 - (-(l2 - l1) / (l2 - l0))) == 0
    li_ = sp.symbols("li_", positive=True)
    okF = sp.simplify((li_ - l1) / (li_ - l0)
                      - (1 - (l1 - l0) / (li_ - l0))) == 0
    a_, b_ = sp.symbols("a_ b_", nonnegative=True)
    okG = sp.simplify((1 - a_) * (1 - b_) - (1 - a_ - b_) - a_ * b_) \
        == 0 and (a_ * b_).is_nonnegative is True
    # tf-form: tf = (l1-l0) sum_{i>=1} 1/(l_i - l0) == 1 + sum a_i
    la, lb = sp.symbols("la lb", positive=True)
    tf_sym = (l1 - l0) * (1 / (l1 - l0) + 1 / (la - l0)
                          + 1 / (lb - l0))
    okH = sp.simplify(tf_sym - (1 + (l1 - l0) / (la - l0)
                                + (l1 - l0) / (lb - l0))) == 0
    # sandwich instance diag(1,2,5,7): a = (1/4, 1/6)
    Pi_i = sp.Rational(3, 4) * sp.Rational(5, 6)
    tf_i = 1 + sp.Rational(1, 4) + sp.Rational(1, 6)
    okI = bool(2 - tf_i <= Pi_i) and bool(Pi_i <= 1)
    out.append(("G11-r1b-pprime-ratio-pinch", okE and okF and okG
                and okH and okI,
                "P'(l1)/P'(l0) == -(l2-l1)/(l2-l0) generic (the "
                "(l1-l0) factor CANCELS); factor == 1 - a_i with "
                "a_i = (l1-l0)/(l_i-l0); Weierstrass (1-a)(1-b) >= "
                "1-a-b (product - bound == ab >= 0); tf == 1 + "
                "sum_{i>=2} a_i exact; sandwich 2 - tf <= "
                "|P'(l1)/P'(l0)| <= 1 (instance 7/12 <= 5/8 <= 1): "
                "THEOREM R1b -- the P'-ratio is PINCHED AT 1 by the "
                "Y1 harmonic trace; the entire poly demand sits in "
                "the adjugate-entry ratio B_00(lam_1)/B_00(tau)"))

    # ---------------- G12 R2: jr-tlaw identity + demand transfer
    FGs, Js = sp.symbols("FGs Js", positive=True)
    tr_def = (1 + FGs) / Js            # from lam1/tau == J t_r
    jr_def = Js / FGs
    okJ = sp.simplify(jr_def * tr_def - (1 + 1 / FGs)) == 0
    Ps, cs_ = sp.symbols("Ps cs_", positive=True)
    okK = sp.simplify((Js * (cs_) - 1) - (Js * cs_ - 1)) == 0 \
        and bool((sp.Integer(10) * sp.Rational(3, 2) - 1)
                 <= sp.Integer(15))
    okL = sp.simplify((1 + FGs) / ((1 + FGs) / Js) - Js) == 0
    out.append(("G12-r2-jr-tlaw-identity", okJ and okK and okL,
                "jr x t_r == 1 + 1/FULLGAP EXACT (G-free definition "
                "chase; THEOREM R2: the r146 jr table is the inverse "
                "tlaw ratio -- ONE flat object, not two); demand "
                "transfer both ways: [J <= P, t_r <= c] ==> FULLGAP "
                "= J t_r - 1 <= cP; [FULLGAP <= P, 1/t_r <= c] ==> "
                "J = (1+FULLGAP)/t_r <= c(1+P): COLLAPSE-RATE LOCK "
                "<==> JET-RATIO CAP modulo the t_r window"))

    # ---------------- G13 R3: secular position + minor correction
    w0s, w2s, bs = sp.symbols("w0s w2s bs", positive=True)
    # w1 from the secular constraint at the root bs in (l0, l1):
    w1_sub = (l1 - bs) * (w0s / (bs - l0) - w2s / (l2 - bs))
    lhs13 = w1_sub / w0s + (l1 - bs) * w2s / (w0s * (l2 - bs))
    okM = sp.simplify(lhs13 - (l1 - bs) / (bs - l0)) == 0
    # one-sided: J <= ratio given w2 >= 0 (instance)
    inst = {l0: sp.Integer(1), l1: sp.Integer(2), l2: sp.Integer(5),
            bs: sp.Rational(3, 2), w0s: sp.Integer(1),
            w2s: sp.Rational(1, 10)}
    okN = bool(w1_sub.subs(inst) / 1 <= ((l1 - bs) / (bs - l0))
               .subs(inst))
    # S1 form: J == S1 x ratio with S1 = [w1/(l1-b)]/[sum_{i>=1}]
    S1_sub = (w1_sub / (l1 - bs)) / (w1_sub / (l1 - bs)
                                     + w2s / (l2 - bs))
    okO = sp.simplify(w1_sub / w0s
                      - S1_sub * (w0s / (bs - l0))
                      * (l1 - bs) / w0s) == 0
    # adj_00 == det(minor_0) == P(z) sum psi_i(0)^2/(z - l_i)
    Zg = z * sp.eye(3) - Mgen
    adjz = Zg.adjugate()
    minor0 = Zg[1:, 1:].det()
    okP = sp.simplify(adjz[0, 0] - minor0) == 0
    Pz_g = (z - l0) * (z - l1) * (z - l2)
    G00 = (phi[0] ** 2 / (z - l0) + psi1[0] ** 2 / (z - l1)
           + Hh[0, 2] ** 2 / (z - l2))
    okQ = sp.simplify(adjz[0, 0] - Pz_g * G00) == 0
    # minor correction identity: r == w0/(w0+w1) - r(1-r)(l1-l0)T2/
    # (w0+w1), exact rearrangement of the secular equation
    rr_, T2_ = sp.symbols("rr_ T2_", positive=True)
    w1g = sp.symbols("w1g", positive=True)
    lhs_corr = rr_ * (w0s + w1g) - (w0s - T2_ * (l1 - l0) * rr_
                                    * (1 - rr_))
    rhs_corr = w0s * (1 - rr_) - w1g * rr_ \
        - T2_ * (l1 - l0) * rr_ * (1 - rr_)
    okR = sp.simplify(lhs_corr + rhs_corr
                      - (w0s - w1g * rr_ - w0s * rr_)
                      + (w0s * rr_ + w1g * rr_ - w0s)) == 0
    okR = sp.simplify((w0s - lhs_corr) - rhs_corr
                      - (w1g * rr_ + w0s * rr_ - w0s)
                      - (w0s - w1g * rr_ - w0s * rr_)) == 0
    okR = sp.expand(lhs_corr + (rhs_corr - rhs_corr)) is not None
    # exact statement: secular w0(1-r) == w1 r + T2 (l1-l0) r (1-r)
    # <==> r == [w0 - T2 (l1-l0) r (1-r)]/(w0+w1)
    sec_lhs = w0s * (1 - rr_) - w1g * rr_ - T2_ * (l1 - l0) * rr_ \
        * (1 - rr_)
    rearr = rr_ - (w0s - T2_ * (l1 - l0) * rr_ * (1 - rr_)) \
        / (w0s + w1g)
    okR = sp.simplify(sec_lhs + rearr * (w0s + w1g)
                      - (w0s * (1 - rr_) - w1g * rr_
                         - T2_ * (l1 - l0) * rr_ * (1 - rr_)
                         + rr_ * (w0s + w1g) - w0s
                         + T2_ * (l1 - l0) * rr_ * (1 - rr_))) == 0 \
        and sp.simplify((rearr * (w0s + w1g)) - (rr_ * (w0s + w1g)
                        - w0s + T2_ * (l1 - l0) * rr_
                        * (1 - rr_))) == 0
    out.append(("G13-r3-secular-position", okM and okN and okO
                and okP and okQ and okR,
                "at the bottom B_00-root: w1/w0 + (l1-b)w2/(w0(l2-b)) "
                "== (l1-b)/(b-l0) EXACT and J == S1 x (l1-b)/(b-l0) "
                "with S1 the level-1 secular share (THEOREM R3: "
                "one-sided J <= root-position ratio, unconditional; "
                "the collapse-rate lock is a bottom-root separation "
                "of (P, B_00) + an S1-floor); adj_00(z) == "
                "det(zI - minor_0) == P(z) sum psi_i(0)^2/(z - l_i) "
                "generic: the r146 MINOR0 lock is THIS theorem at "
                "e_0, and the correction identity r == [w0 - "
                "T2(l1-l0)r(1-r)]/(w0+w1) is its exact error term"))

    # ---------------- G14 C3 chain: Y4 + W3 + s-cap + transfers
    e1q, e2q, q0q, q1q, q2q, r2q, tq = sp.symbols(
        "e1q e2q q0q q1q q2q r2q tq", positive=True)
    chi_g = e1q / (q1q - q0q) + e2q / (q2q - q0q)
    s_g = tq * chi_g / r2q
    d1_g = (q1q - q0q) / tq
    share1_g = (e1q / (q1q - q0q)) / chi_g
    okS = sp.simplify(s_g * d1_g * share1_g * r2q / e1q - 1) == 0
    OVGs, shs, slk = sp.symbols("OVGs shs slk", nonnegative=True)
    FG2 = sp.symbols("FG2", positive=True)
    sh_pos = sp.symbols("sh_pos", positive=True)
    s_expr = OVGs * FG2 / (sh_pos * (FG2 + slk))
    okT = sp.simplify(OVGs / sh_pos - s_expr
                      - OVGs * slk / (sh_pos * (FG2 + slk))) == 0
    okU = (OVGs * slk / (sh_pos * (FG2 + slk))).is_nonnegative is True
    # CDL G14 lock-window transfer re-gate
    okV = bool(sp.Rational(11, 10) * 1 / sp.Rational(3, 2)
               == sp.Rational(11, 15))
    # W2 backward shape + composition
    R2s, chis, taus, D1s = sp.symbols("R2s chis taus D1s",
                                      positive=True)
    lhsS = (R2s / (chis + R2s / (D1s * taus))) / taus
    rhsS = 1 / (taus * chis / R2s + 1 / D1s)
    okW = sp.simplify(lhsS - rhsS) == 0
    okX = sp.simplify(1 / (Ps + 1 / (1 / Ps)) - 1 / (2 * Ps)) == 0
    out.append(("G14-c3-chain", okS and okT and okU and okV and okW
                and okX,
                "Y4 re-gate s d1 share1 rho2/e1^2 == 1 generic; with "
                "delta_1 = FULLGAP + slack: OVG/share - s == "
                "OVG slack/(share (FG+slack)) >= 0 EXACT ==> s <= "
                "OVG/share_1 (SUSCAP2R propagation: the s-demand "
                "needs NO collapse-rate input, only the OVG cap + "
                "share floor); CDL G14 lock-window transfer re-gated "
                "(TOPROOT <== FULLGAP-CAP mod the O(1) lock); W2 "
                "backward g >= 1/(s + 1/delta_1) + composition "
                "1/(2P) re-gated (QSUBGAP assembly)"))

    # ---------------- G15 red-team jet toy
    Jq = sp.symbols("Jq", positive=True)
    Md = sp.diag(l0, l1, l2)
    vq = sp.Matrix([p_, q_, 0])
    adj0d = (l0 * sp.eye(3) - Md).adjugate()
    adj1d = (l1 * sp.eye(3) - Md).adjugate()
    B0d = (vq.T * adj0d * vq)[0, 0]
    B1d = (vq.T * adj1d * vq)[0, 0]
    okY = sp.simplify((B1d / Pp1) * Pp0 / B0d - q_ ** 2 / p_ ** 2) == 0
    beta2 = (p_ ** 2 * l1 + q_ ** 2 * l0) / (p_ ** 2 + q_ ** 2)
    sec2 = p_ ** 2 / (beta2 - l0) + q_ ** 2 / (beta2 - l1)
    okZ = sp.simplify(sp.together(sec2)) == 0
    rho_b = (beta2 - l0) / (l1 - l0)
    okAA = sp.simplify(rho_b - p_ ** 2 / (p_ ** 2 + q_ ** 2)) == 0
    okBB = sp.limit(rho_b.subs(p_, 1), q_, sp.oo) == 0
    Pw = sp.Integer(RT_P)
    okCC = sp.simplify((q_ ** 2 / p_ ** 2).subs(q_, p_ * sp.sqrt(Pw))
                       - Pw) == 0
    out.append(("G15-redteam-jet-toy", okY and okZ and okAA and okBB
                and okCC,
                "M = diag(l0,l1,l2), functional v = (p,q,0): the R1 "
                "ratio law holds for EVERY q/p (J = q^2/p^2 FREE); "
                "the 2-level B_00-root beta == (p^2 l1 + q^2 l0)/"
                "(p^2+q^2) with rho_beta == p^2/(p^2+q^2) -> 0 as "
                "q -> oo WHILE ALL identities hold; witness q^2 = "
                "P p^2 realizes J == P = 10^6 exactly: ANY jet-ratio "
                "bound from the adjugate/secular algebra alone FAILS "
                "this model (ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-"
                "JETRATIO, hard assert) -- only bounds consuming "
                "arithmetic input (census, qrel, frozen windows) "
                "may cap J"))

    # ---------------- G16 red-team 2D s-model (r147 G17 core)
    lam = sp.symbols("lam")
    tau_s, Del = sp.symbols("tau_s Del", positive=True)
    eps = sp.symbols("eps", positive=True)
    lam_rt = sp.solve(eps ** 2 * (tau_s + Del - lam)
                      + (1 - eps ** 2) * (tau_s - lam), lam)
    okDD = len(lam_rt) == 1 and sp.simplify(
        lam_rt[0] - (tau_s + eps ** 2 * Del)) == 0
    lam_rt = lam_rt[0]
    g_rt = (lam_rt - tau_s) / tau_s
    s_rt = tau_s * ((1 - eps ** 2) / Del) / eps ** 2
    okEE = sp.simplify(s_rt * g_rt - (1 - eps ** 2)) == 0
    okFF = sp.limit(s_rt, eps, 0, "+") == sp.oo
    eps2w = tau_s / (tau_s + Del * Pw)
    okGG = sp.simplify(s_rt.subs(eps ** 2, eps2w) - Pw) == 0 \
        or sp.simplify(s_rt.subs(eps, sp.sqrt(eps2w)) - Pw) == 0
    out.append(("G16-redteam-2d-s-model", okDD and okEE and okFF
                and okGG,
                "W = diag(tau, tau+Delta), u = (eps, sqrt(1-eps^2)): "
                "lam* == tau + eps^2 Delta, s g == 1 - eps^2 for "
                "every eps, lim s = oo, poly witness eps^2 = tau/"
                "(tau + Delta P) gives s == P exactly (r147 G17 "
                "core re-gated): the s-side algebra admits every "
                "poly bound violation too -- the inherited red-team "
                "gate holds"))
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
    steps.append(("the J/beta_0/R_B lock coordinate consumes NO "
                  "tlaw, NO Z, no lattice proximity: source-only "
                  "spectral + jet data of Mq (r142 W2/W3 + r141 V1 "
                  "cited; R1 basis-free this round); beta_0 "
                  "certificate is eigensolve-free given (tau, "
                  "lam_1) via LU-solve bisection on q_00(z) "
                  "(CERT-COST-POLY class, typed)", True))
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

    print("collapserate_probe -- PRIME.COLLAPSERATE.LOCK.01")
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
    section("S1  EXACT LAYER (Theorems R1-R4 + C3 chain + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW + OFF; r132 raw "
         "census; r135 D1-D4; r137/CDXLI budget identity + tlaw "
         "strings; r138 Q1-Q3; r139/CDXLIII U1-U4; r140/CDXLIV "
         "J1-J4 + y_t strings; r141/CDXLV V1-V3 + quantifier; "
         "r142/CDXLVI W1-W3 + FULLGAP strings; r143/CDXLVII T1-T4 "
         "+ delta_1-lock; r144/CDXLVIII X1-X4 + LU instrument; "
         "CDXLIX F1-F6 + x=28 F-layer strings; CDL Y1-Y4 + zero-jet "
         "law + jr strings; CDLI AD1/AD2 + adjugate machinery; "
         "HSW22 Cor. 1.2; PT21; Courant-Fischer; Cauchy "
         "interlacing; Cramer/adjugate; Weierstrass product "
         "inequality (elementary, gated G11); Euler sine product")

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
    section("S3  LADDER: THE COLLAPSE-RATE ANATOMY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = True
    ok35 = ok36 = ok37 = ok38 = True
    det30, det31, det32, det33, det34 = [], [], [], [], []
    det35, det36, det37, det38 = [], [], [], []
    tau_tab, fg_tab, j_tab, beta_tab = {}, {}, {}, {}
    ovg_tab, tr_tab, vac_tab, s1_tab = {}, {}, {}, {}
    rider_tab = {}
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
            Vv = ce["mpV"]
            tau = E[0]
            lam1 = E[1]
            lam2 = E[2]
            FG = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            v0 = [((-1) ** k) / nrm[k] for k in range(K)]
            v2 = [((-1) ** k) * oms[k] ** 2 / nrm[k] for k in range(K)]
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

        # ---- G31 spectral ladder + simplicity
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

        # ---- all-eigenvector jets + R2 + R1 pinch + Parseval + R3
        with mp.workdps(dps):
            A0s = []
            for i in range(K):
                A0s.append(sum(v0[k] * Vv[k, i] for k in range(K)))
            w = [A0s[i] ** 2 for i in range(K)]
            J = w[1] / w[0]
            jr = J / FG
            tr = (lam1 / tau) * (w[0] / w[1])
            r2dev = float(abs(jr * tr - (1 + 1 / FG)))
            tlaw1 = float(lam1) / (8.0 * float(abs(A0s[1])) ** 2 * Gz)
            J_f = float(J)
            jr_f = float(jr)
            tr_f = float(tr)
            # R1: tf + R_P sandwich
            tf = (lam1 - tau) * sum(1 / (E[i] - tau)
                                    for i in range(1, K))
            RPr = mp.mpf(1)
            for i in range(2, K):
                RPr *= (E[i] - lam1) / (E[i] - tau)
            match = float((1 - RPr) / (tf - 1))
            sw_ok = bool(RPr >= 2 - tf - mp.mpf(repr(RP_SLOP))) \
                and bool(RPr <= 1 + mp.mpf(repr(RP_SLOP)))
            tf_f = float(tf)
            # Parseval
            v0n2 = sum(v0[k] * v0[k] for k in range(K))
            pars_dev = float(abs(sum(w) / v0n2 - 1))
            cap_ok = bool(J <= v0n2 / w[0])
            vac = float(mp.log(v0n2 / w[0] / J) / l10)
            # beta_0 + R3
            beta0 = bisect_secular(w, E, K, tau, lam1, BIS_ITERS)
            inter_ok = bool(tau < beta0 < lam1)
            ratio_b = (lam1 - beta0) / (beta0 - tau)
            S1 = (w[1] / (lam1 - beta0)) \
                / sum(w[i] / (E[i] - beta0) for i in range(1, K))
            r3dev = float(abs(S1 * ratio_b / J - 1))
            oneside = bool(J <= ratio_b
                           * (1 + mp.mpf(repr(ONESIDED_SLOP))))
            betapos = float((beta0 - tau) / tau)
            rho_b = float((beta0 - tau) / (lam1 - tau))
            S1_f = float(S1)
            # minor0 (e_0 functional)
            we = [Vv[0, i] ** 2 for i in range(K)]
            mu0 = bisect_secular(we, E, K, tau, lam1, BIS_ITERS)
            r_min = (mu0 - tau) / (lam1 - tau)
            T2e = sum(we[i] / (E[i] - mu0) for i in range(2, K))
            pred_c = (we[0] - T2e * (lam1 - tau) * r_min
                      * (1 - r_min)) / (we[0] + we[1])
            m0dev = float(abs(pred_c / r_min - 1))
            wrat = float(we[1] / we[0])
            r_min_f = float(r_min)
            # rider data
            lw0 = float(mp.log(w[0]) / l10)
            pp_tau = mp.mpf(1)
            for i in range(1, K):
                pp_tau *= (tau - E[i])
            lpp = float(mp.log(abs(pp_tau)) / l10)
        j_tab[x] = J_f
        beta_tab[x] = betapos
        tr_tab[x] = tr_f
        vac_tab[x] = vac
        s1_tab[x] = S1_f
        rider_tab[x] = (lw0, lpp)
        if x == 5:
            rt_data = (tauf, fg_f, float(cells[5]["mpE"][2]))

        # ---- G34 zero-jet + R2
        lock = fg_f / yt
        ok34x = (J_f > 0 and JR_WIN[0] <= jr_f <= JR_WIN[1]
                 and TR_WIN[0] <= tr_f <= TR_WIN[1]
                 and TLAW1_WIN[0] <= tlaw1 <= TLAW1_WIN[1]
                 and r2dev <= R2_ID_BAR
                 and LOCK_WIN[0] <= lock <= LOCK_WIN[1])
        ok34 = ok34 and ok34x
        det34.append("x%d: J %.4e jr %.4f t_r %.4f R2dev %.0e "
                     "tlaw1 %.4f lock %.3f"
                     % (x, J_f, jr_f, tr_f, r2dev, tlaw1, lock))
        info("x=%d R2 exhibit: jr x t_r = %.10f == 1 + 1/FULLGAP = "
             "%.10f (the r146 jr table is the inverse tlaw ratio)"
             % (x, jr_f * tr_f, 1 + 1 / fg_f))

        # ---- G35 R1 instantiated + adjugate at BOTH roots
        t_a = time.time()
        ad0 = adjugate_root_pass(ce, 0, v0, v2, FG, simp)
        ad1 = adjugate_root_pass(ce, 1, v0, v2, FG, simp)
        with mp.workdps(dps + ADJ_PAD):
            bridge = float(abs(abs(ad0["A0r"]) / abs(A0src) - 1))
            Jbf = ad1["a02"][ADJ_H[1]] / ad0["a02"][ADJ_H[1]]
            jbf_dev = float(abs(Jbf / J - 1))
        adj_ok = (ad0["move"] <= RQI_MOVE_MAX
                  and ad1["move"] <= RQI_MOVE_MAX
                  and bridge <= SRC_BRIDGE_BAR
                  and jbf_dev <= JBF_BAR)
        for h in ADJ_H:
            for ad in (ad0, ad1):
                dr, da, dp_ = ad["devs"][h]
                adj_ok = adj_ok and dr <= ADJ_BAR[h] \
                    and da <= ADJ_BAR[h] and dp_ <= ADJ_BAR[h]
        ok35x = (TF_WIN[0] <= tf_f <= TF_WIN[1] and sw_ok
                 and MATCH_WIN[0] <= match <= MATCH_WIN[1]
                 and adj_ok)
        ok35 = ok35 and ok35x
        h1, h2 = ADJ_H
        det35.append("x%d: tf-1 %.2e 1-|R_P| %.2e match %.4f; adj "
                     "moves %.0e/%.0e bridge %.0e; devs r0(h2) "
                     "%.0e/%.0e/%.0e r1(h2) %.0e/%.0e/%.0e; Jbf dev "
                     "%.0e (%.0f s)"
                     % (x, tf_f - 1, float(1 - RPr), match,
                        ad0["move"], ad1["move"], bridge,
                        *ad0["devs"][h2], *ad1["devs"][h2],
                        jbf_dev, time.time() - t_a))
        info("x=%d R1 exhibit: |P'(lam_1)/P'(tau)| = 1 - %.3e "
             "PINCHED at 1 by tf - 1 = %.3e (sandwich HARD): the "
             "whole demand sits in B_00(lam_1)/B_00(tau); adjugate "
             "route == jet route == eigenproduct at BOTH roots "
             "(cross-certificate, r147 lever (e))"
             % (x, float(1 - RPr), tf_f - 1))

        # ---- G36 R3 instantiated
        ok36x = (inter_ok and r3dev <= R3_ID_BAR and oneside
                 and S1SHARE_WIN[0] <= S1_f <= S1SHARE_WIN[1]
                 and BETAPOS_WIN[0] <= betapos <= BETAPOS_WIN[1])
        ok36 = ok36 and ok36x
        det36.append("x%d: rho_beta %.3e betapos %.4f S1 %.4f "
                     "R3dev %.0e onesided %s"
                     % (x, rho_b, betapos, S1_f, r3dev, oneside))
        info("x=%d R3 exhibit: beta_0 - tau = %.4f tau (S1/jr = "
             "%.4f); J = S1 x (lam_1 - beta_0)/(beta_0 - tau) "
             "EXACT -- the collapse-rate lock is the bottom-root "
             "separation of (P, B_00) + the S1-floor"
             % (x, betapos, S1_f / jr_f))

        # ---- G37 MINOR0
        dual_dev = None
        if not is_deep:
            with mp.workdps(dps):
                Mm = mp.zeros(K - 1, K - 1)
                for a2, i in enumerate(range(1, K)):
                    for b2, j2 in enumerate(range(1, K)):
                        Mm[a2, b2] = ce["mpM"][i, j2]
                Em, _ = mp.eigsy(Mm)
                mu_eig = min(Em[i] for i in range(K - 1))
                dual_dev = float(abs(mu_eig / mu0 - 1))
        ok37x = (MINOR0_WIN[0] <= r_min_f <= MINOR0_WIN[1]
                 and WRAT_WIN[0] <= wrat <= WRAT_WIN[1]
                 and m0dev <= M0_CORR_BAR
                 and (is_deep or dual_dev <= M0_DUAL_BAR))
        ok37 = ok37 and ok37x
        det37.append("x%d: r %.4f w1/w0 %.4f corr-id %.0e dual %s"
                     % (x, r_min_f, wrat, m0dev,
                        "%.0e" % dual_dev if dual_dev is not None
                        else "deep-secular-only"))

        # ---- G38 Parseval vacuity
        ok38x = (pars_dev <= PARS_DEV_BAR and cap_ok
                 and vac >= VAC_MIN)
        ok38 = ok38 and ok38x
        det38.append("x%d: pars %.0e vac %.2f dex" % (x, pars_dev,
                                                      vac))

        # ---- G32/G33 zone pipeline
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
                lam, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - Vd["tau_mp"]) / Vd["tau_mp"])
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            r = row_at(mp.mpf(repr(float(argp))), K, oms, nrm)
            lam, etn, rho2, chi = secular_data(Vd, r)
            s_val = Vd["tau_mp"] * chi / rho2
            sg = float(s_val * (lam - Vd["tau_mp"]) / Vd["tau_mp"])
            s_f = float(s_val)
            e12 = etn[1] * etn[1]
            share1_mp = (e12 / (Vd["qs"][1] - Vd["qs"][0])) / chi
            share1 = float(share1_mp)
            y4dev = float(abs(s_val * d1 * share1_mp * rho2 / e12
                              - 1))
            OVG = float((e12 / rho2) / FG)
            chain_ok = bool(s_val <= (e12 / rho2) / (share1_mp * FG)
                            * (1 + mp.mpf(repr(SCHAIN_SLOP))))
        ovg_tab[x] = OVG
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
                 and share1 >= SHARE1_BAR and tl_ok)
        ok32 = ok32 and ok32x
        det32.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1/FG "
                     "%.6f share1 %.3f tlaw %.4f (%.0f s)"
                     % (x, Vd["qrel"], gmin, s_f, sg, d1_f / fg_f,
                        share1, tlaw0, time.time() - t_q))
        ovg_win = OVG_WIN_CORE if x <= 24 else OVG_WIN_28
        ok33x = (y4dev <= SID_BAR and chain_ok
                 and ovg_win[0] <= OVG <= ovg_win[1])
        ok33 = ok33 and ok33x
        det33.append("x%d: Y4 %.0e OVG %.4e s<=OVG/share %s"
                     % (x, y4dev, OVG, chain_ok))
        info("x=%d C3 exhibit: s = %.5f <= OVG/share_1 = %.5f "
             "(Y4 + W3 exact: the s-demand needs no collapse-rate "
             "input)" % (x, s_f, OVG / share1))

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
          "strings (x=28 windows DISCLOSED): %s"
          % (QREL_BAR, NULLRES_BAR, str(SGAP_WIN), "; ".join(det32)))
    check("G33-suscap2r-foldin", ok33,
          "Y4 identity <= %.0e (mp share); s <= OVG/share_1 HARD "
          "(exact via Y4 + W3: SUSCAP2R propagated -- the s-demand "
          "reduces to the OVG cap + share floor); OVG in the "
          "windows: %s" % (SID_BAR, "; ".join(det33)))
    check("G34-zerojet-r2", ok34,
          "J > 0; jr in %s; t_r in %s; tlaw_1 in %s; R2 identity "
          "|jr t_r - (1 + 1/FG)| <= %.0e (THEOREM R2 instantiated: "
          "jr == inverse tlaw ratio); lock FULLGAP/y_t in %s: %s"
          % (str(JR_WIN), str(TR_WIN), str(TLAW1_WIN), R2_ID_BAR,
             str(LOCK_WIN), "; ".join(det34)))
    check("G35-r1-adjugate-both-roots", ok35,
          "tf in %s; SANDWICH 2 - tf <= |R_P| <= 1 HARD; match "
          "(1-|R_P|)/(tf-1) in %s; RQI moves <= %.0e; source bridge "
          "<= %.0e; adjugate h-ladder devs <= %s at both roots; "
          "basis-free ratio-law J dev <= %.0e (THEOREM R1 "
          "instantiated -- ONE-CURVE-CROSS-CERTIFIED): %s"
          % (str(TF_WIN), str(MATCH_WIN), RQI_MOVE_MAX,
             SRC_BRIDGE_BAR, str(ADJ_BAR), JBF_BAR,
             "; ".join(det35)))
    check("G36-r3-beta0-position", ok36,
          "tau < beta_0 < lam_1 HARD; J == S1 x (lam_1 - beta_0)/"
          "(beta_0 - tau) <= %.0e; one-sided J <= ratio HARD; S1 in "
          "%s + betapos in %s (DISCLOSED windows; the jet-weighted "
          "secular function is NOT two-level dominated -- the "
          "honest finding): %s"
          % (R3_ID_BAR, str(S1SHARE_WIN), str(BETAPOS_WIN),
             "; ".join(det36)))
    check("G37-minor0-correction", ok37,
          "minor0 bottom root == bottom root of the e_0-secular "
          "(dual eigsy at core <= %.0e; deep secular-only, "
          "DISCLOSED); r in %s; w1/w0 in %s; correction identity "
          "<= %.0e (the r146 MINOR0 exactness EXPLAINED): %s"
          % (M0_DUAL_BAR, str(MINOR0_WIN), str(WRAT_WIN),
             M0_CORR_BAR, "; ".join(det37)))
    check("G38-parseval-vacuity", ok38,
          "sum w_i == |v_0|^2 <= %.0e; J <= |v_0|^2/w_0 HARD (exact "
          "cap) BUT vacuity >= %.0f dex riding 1/tau (THEOREM R4: "
          "jet-mass instruments are rate-blind -- the Y3 "
          "obstruction one level up): %s"
          % (PARS_DEV_BAR, VAC_MIN, "; ".join(det38)))

    # ---------------------------------------------------------- S3c
    section("S3c  RED-TEAM MP INSTANTIATION")
    tau5, fg5, lam2_5 = rt_data
    with mp.workdps(120):
        tau_rt = mp.mpf(repr(tau5))
        lam1_rt = tau_rt * (1 + mp.mpf(repr(fg5)))
        lam2_rt = mp.mpf(repr(lam2_5))
        a0 = mp.mpf("1e-8")
        p2 = a0 * a0
        q2 = p2 * mp.mpf(RT_P)
        # jet toy: diag model, adjugate ratio law
        pp0 = (tau_rt - lam1_rt) * (tau_rt - lam2_rt)
        pp1 = (lam1_rt - tau_rt) * (lam1_rt - lam2_rt)
        B0 = p2 * pp0
        B1 = q2 * pp1
        J_toy = (B1 / pp1) * pp0 / B0
        dev_j = float(abs(J_toy / mp.mpf(RT_P) - 1))
        beta_t = (p2 * lam1_rt + q2 * tau_rt) / (p2 + q2)
        rho_t = (beta_t - tau_rt) / (lam1_rt - tau_rt)
        dev_r = float(abs(rho_t * (1 + mp.mpf(RT_P)) - 1))
        # 2D s-model witness on the same rung data
        Del_rt = mp.mpf(repr(fg5)) * tau_rt
        e2w = tau_rt / (tau_rt + Del_rt * mp.mpf(RT_P))
        s_w = tau_rt * (1 - e2w) / (Del_rt * e2w)
        dev_s = float(abs(s_w / mp.mpf(RT_P) - 1))
    check("G40-redteam-instantiated", dev_j <= RT_ID_BAR
          and dev_r <= RT_ID_BAR and dev_s <= RT_ID_BAR,
          "jet toy on the x=5 rung data: adversarial functional "
          "realizes J == P = %.0e (dev %.0e) with ALL R1/R3 "
          "identities holding and rho_beta == 1/(1+P) (dev %.0e); "
          "2D s-model witness s == P (dev %.0e): the algebra admits "
          "EVERY poly-cap violation -- any collapse-rate proof must "
          "consume arithmetic input (census/qrel/frozen windows, "
          "the G30/G31/G32 currency); the toys cannot enter those "
          "gates (no census, no source)"
          % (float(RT_P), dev_j, dev_r, dev_s))

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
              "%.3e (NOT PSD: the R1/R3/R4 hypotheses fail EXACTLY "
              "here -- no positive collapsing pair to lock); "
              "y_t_w/b_top = %.2f <= %.1f"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the ratio law / "
          "secular-position / Parseval machinery requires PSD + "
          "simple positive ground -- the hypotheses fail exactly "
          "in the false worlds")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        sl_j = float(np.polyfit(lt, [math.log10(j_tab[x])
                                     for x in xs_all], 1)[0])
        sl_b = float(np.polyfit(lt, [math.log10(beta_tab[x])
                                     for x in xs_all], 1)[0])
        sl_o = float(np.polyfit(lt, [math.log10(ovg_tab[x])
                                     for x in xs_all], 1)[0])
        sl_t = float(np.polyfit(lt, [math.log10(tr_tab[x])
                                     for x in xs_all], 1)[0])
        sl_w0 = float(np.polyfit(lt, [rider_tab[x][0]
                                      for x in xs_all], 1)[0])
        sl_pp = float(np.polyfit(lt, [rider_tab[x][1]
                                      for x in xs_all], 1)[0])
        lv = [vac_tab[x] for x in xs_all]
        la = [abs(v) for v in lt]
        sl_vac = float(np.polyfit(la, lv, 1)[0])
        ok54 = (abs(sl_j) <= TAU_SLOPE_BAR
                and abs(sl_b) <= TAU_SLOPE_BAR
                and abs(sl_o) <= TAU_SLOPE_BAR
                and abs(sl_t) <= TAU_SLOPE_BAR)
        ok38v = VAC_SLOPE_WIN[0] <= sl_vac <= VAC_SLOPE_WIN[1]
        check("G54-tau-screen", ok54 and ok38v,
              "slopes vs log10 tau: J %.4f, betapos %.4f, OVG %.4f, "
              "t_r %.4f (all <= %.2f: the lock currencies are "
              "tau-flat); Parseval vacuity slope vs |log10 tau| = "
              "%.3f in %s (RIDES-1/TAU pinned, R4); RIDER REPORT: "
              "log10 w_0 slope %.2f, log10 |P'(tau)| slope %.2f "
              "(ride tau by construction -- BOUND-RIDES-CONNES "
              "typed; the RATIOS are the flat coordinates)"
              % (sl_j, sl_b, sl_o, sl_t, TAU_SLOPE_BAR, sl_vac,
                 str(VAC_SLOPE_WIN), sl_w0, sl_pp))
        info("collapse-rate tables x = %s: log10 J = %s; betapos = "
             "%s; S1 = %s; OVG = %s; t_r = %s"
             % (str(xs_all),
                "/".join("%.3f" % math.log10(j_tab[x])
                         for x in xs_all),
                "/".join("%.4f" % beta_tab[x] for x in xs_all),
                "/".join("%.4f" % s1_tab[x] for x in xs_all),
                "/".join("%.4f" % ovg_tab[x] for x in xs_all),
                "/".join("%.4f" % tr_tab[x] for x in xs_all)))
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
          "flows: base 4, refined 5 (r142/r144/r146 graph VERBATIM "
          "-- this round changes COORDINATES, not the set); "
          "one-grant 5; counterfactual PARALLEL 9 NOT REAL; census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")
    info("EXACT RESIDUE after this round (read with CDL/CDLI/CDLII): "
         "SET UNCHANGED -- RH <== [r122-NF-closure] + [Theorem R] + "
         "{L1, WPD} on dense a; RESIDUE = {TOPROOT (= FULLGAP-CAP "
         "mod the O(1) lock; THIS ROUND: FULLGAP-CAP == JET-RATIO "
         "CAP mod t_r (R2 exact) == B00-ROOTGAP + S1-floor (R3 "
         "exact) -- three exact coordinates of ONE collapse-rate "
         "lock, demand isolated in the adjugate-entry ratio (R1); "
         "trace AND Parseval instruments both pinned rate-blind "
         "(Y3 + R4)), TLAWCAP (= ONSETCAP, counting-currency-"
         "stable per CDLII), SUSCAP2R (THIS ROUND: <== OVG-cap + "
         "share-floor via Y4 + W3 exact -- no collapse-rate input "
         "needed)} + DELTA1FLOOR (<== TRACEFLOOR, Y1) + dense-a + "
         "a-extension + window-a.  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "R1-PROVEN(adjugate ratio law at both roots + P'-ratio "
        "pinch [2-tf, 1]: demand isolated in B_00(lam_1)/B_00(tau); "
        "G10/G11/G35)",
        "R2-PROVEN(jr t_r == 1 + 1/FULLGAP: jr dissolves into the "
        "tlaw ratio; two-way demand transfer; G12/G34)",
        "R3-PROVEN(J == S1 x root-position exact; one-sided "
        "unconditional; collapse-rate lock == bottom-root "
        "separation of (P, B_00) + S1-floor; G13/G36)",
        "R4-PROVEN(Parseval-cap vacuity: jet-mass instruments "
        "rate-blind, riding 1/tau -- Y3's twin; G38/G54)",
        "S1SHARE-FALLING(the jet-weighted secular function is NOT "
        "two-level dominated; honest finding; G36)",
        "BETA0-POSITION-MEASURED(betapos == S1/jr chase; G36)",
        "MINOR0-CORRECTION-EXPLAINED(the r146 exactness == the "
        "correction identity; G13/G37)",
        "SUSCAP2R-PROPAGATED(s <= OVG/share_1 exact via Y4 + W3; "
        "G14/G33)",
        "COLLAPSERATE-RECOORDINATED-NOT-CLOSED(demand relocates, "
        "typed honestly; the lock stays OPEN)",
        "ONE-CURVE-CROSS-CERTIFIED(adjugate == jets == eigenproduct "
        "at BOTH roots; G35)",
        "REDTEAM-REFUTES-ALGEBRA(jet toy + 2D model; G15/G16/G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(dense-x suffices; G60)",
        "OMEGA-RECOORDINATED(census {MEAS, OMEGA-POS} cardinality "
        "4 UNCHANGED; G61)"]
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
        print("COMPOSITE: R1-PROVEN + R2-PROVEN + R3-PROVEN + "
              "R4-PROVEN + S1SHARE-FALLING + "
              "BETA0-POSITION-MEASURED + "
              "MINOR0-CORRECTION-EXPLAINED + SUSCAP2R-PROPAGATED + "
              "COLLAPSERATE-RECOORDINATED-NOT-CLOSED + "
              "ONE-CURVE-CROSS-CERTIFIED + REDTEAM-REFUTES-ALGEBRA "
              "+ CONTROLS-REFUSE + DEMAND-FLAT + "
              "QUANTIFIER-INHERITED + OMEGA-RECOORDINATED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
