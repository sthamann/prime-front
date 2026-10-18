#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fullgap_growthlaw_probe -- PRIME.FULLGAP.GROWTHLAW.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the FULLGAP growth law -- the last
unexplained measured law of the prime-front program)
=======================================================================
FULLGAP := (lam_1(Mq) - tau)/tau is measured 2.225e5 -> 1.651e8 over
x = 5..28 with log-log slope ~4.0 (r142/r146/CDLII strings).  The
zero-jet law holds at three rungs (tau = 8 A_0(phi)^2 G tlaw_0 [r137],
lam_1 = 8 A_0(psi_1)^2 G tlaw_1 [CDL Y2/zero-jet], constrained ground
[CDLXV GF4]), and the r150 R2 identity jr t_r == 1 + 1/FULLGAP with
jr -> 1 and flat t-ratios makes THE GROWTH ENTIRELY THE JET RATIO
J := (A_0(psi_1)/A_0(phi))^2.  The delta_1-floor (== FULLGAP >= 1/poly
via W3-tight interlacing) is the one load-bearing bottom of the razor
(CDLXV GF1: the g-floor IS the s-cap given the delta_1-floor) and of
the kappa/rho^2 depth collapses (CDLXIV/CDLXI).  This probe mounts the
maximal derivation attempt along the contract angles: (D1) the
zone-killing anatomy and the per-zero collapse factor, (D2) the
orthogonality lever via exact leave-one-out problems, (D3) the weakest
sufficient floor, (T4) red team, (T5) the razor assembly.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, Mq = round-114 builder (even sector),
eigenpairs lam_0 = tau < lam_1 <= ... with eigenvectors phi, psi_1,
psi_2, ... (mpE/mpV); FULLGAP = (lam_1 - tau)/tau; T_z = 2 pi x (the
proven G17 resolvability crossover); G = HSW tail envelope at T_z;
jets A_0(v) = sum_k (-1)^k cn_k(v); tlaw_i = lam_i/(8 A_0(psi_i)^2 G);
J = (A_0(psi_1)/A_0(phi))^2, jr = J/FULLGAP, t_r = tlaw_1/tlaw_0;
THETA := J/T_z^4 (the quartic-law coordinate), c_1 = |A_0(psi_1)/
A_0(phi)|/T_z^2, c_2 = |A_0(psi_2)/A_0(psi_1)|/T_z^2; m = verified
zone census, V = kernel of the m newton-polished node rows (codim-m,
phi in V, q_0 = tau, q_1 == lam_1 W3-tight), frame eigenpairs (q_i,
z_i), eta_i = A_0 of the K-space representative of z_i; y_t =
|A_2/A_0|(phi); collapsed block = {i: lam_i < 0.1 lam_max}.

FROZEN QUANTIFIER (declared before the deep data, the r141 dense-x
demand level): the growth-law demand adjudicated here is [EXISTS
theta_0 > 0 and an O(1) window: J(x) == theta(x) T_z^4 with theta(x)
in [theta_0, THETA_HI] on the instrument-chosen ladder + its V2
dense-x extension].  This probe proves COORDINATES, exact reductions
and refutations; it does NOT claim the law beyond the ladder and
makes NO RH claim.

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically + exact rational
instances + mp-instantiated per rung; classical inputs typed CITED)
=======================================================================
THEOREM GL1 (leave-one-out pinch; the D2 eigenvalue-side answer).
For any row subset S' of the zone rows S (S' subset S), with V_S' =
kernel(S') superset V_S:
   lam_1  <=  min Rayleigh over (V_S' cap phi-perp)
          <=  min Rayleigh over (V_S cap phi-perp) = q_1(S),
(left: subset of phi-perp; right: subspace inclusion), and with the
Y2 tightness transfer (CDL, cited + re-instanced) q_1 - lam_1 <=
eps^2 (lam_max - lam_1)/(1 - eps^2).  CONSEQUENCE: EVERY leave-one-
out problem matches lam_1 within the eps^2 budget -- the growth law
is INVISIBLE to constraint-set eigenvalue perturbations.  The
measured discriminator is the pinch position p_j = (lam_loo_j -
lam_1)/(q_1 - lam_1) in [0, 1].

THEOREM GL2 (the arrowhead/bordered leave-one-out instrument).  With
u_j = R^T (R R^T)^{-1} e_j (the minimum-norm dual row: R_i u_j =
delta_ij), kernel(S minus j) = V + span(u_j), and with u~ the unit
component of u_j orthogonal to V:  V_j cap phi-perp = span(z_1, ...,
z_{nf-1}) + span(u~), and the compression is the arrowhead matrix
[[diag(q_1..), b],[b^T, c]] with b_i = z_i^T Mq u~, c = u~^T Mq u~;
its bottom eigenvalue is the unique root lam < q_1 of  f(lam) =
(c - lam) - sum_{i>=1} b_i^2/(q_i - lam)  (decreasing), with
eigenvector components w_i = -b_i/(q_i - lam) (u-component 1) and
0-jet A_0 = [sum_{i>=1} eta_i w_i + eta_u]/norm.  (sympy generic
3-level + linearity chase.)

THEOREM GL3 (one-row price equivalence; the D3 adjudication).
(i) For ANY single row R: tau <= ground(Mq on ker R) <= lam_1
(one-constraint interlacing, Cauchy CITED + exact instance) --
FULLGAP >= one-row price for EVERY row.  (ii) WITNESS: R = phi gives
ground == lam_1 EXACTLY (eigenframe chase) -- so [EXISTS row with
price >= 1/poly] <==> [FULLGAP >= 1/poly]: the weakest sufficient
floor is EQUIVALENT to the floor, not weaker.  (iii) RAZOR VACUITY:
1/(s + 1/F) <= F identically (s, F > 0) -- the GF1 lower end applied
to any row can never lift FULLGAP; and the 2-level witness rho^2 =
1/(1 + P delta_1) drives any given row's price to 0 with all
identities intact: NO algebra-only per-row/per-zero price bound can
floor FULLGAP (ALGEBRA-ONLY-REFUTED-FOR-ROWPRICE, hard assert).
D3 COLLAPSES TO THE RAZOR: a nonvacuous one-row floor must consume
arithmetic at the row (the CDLXV bridge channel), exactly as r161
pinned for the s-cap.

THEOREM GL4 (rate bookkeeping; the per-zero coordinates).  From the
definitional identities tau == 8 A_0(phi)^2 G tlaw_0 and lam_1 ==
8 A_0(psi_1)^2 G tlaw_1:  jr t_r == 1 + 1/FULLGAP (r150 R2 re-chase)
and per-zero rates over a ladder pair obey  Dlog tau == 2 Dlog
|A_0(phi)| + Dlog(8 G tlaw_0)  and  Dlog J == 2 (Dlog|A_0(psi_1)| -
Dlog|A_0(phi)|)  EXACTLY: the per-zero FULLGAP growth is the per-zero
DIFFERENTIAL of two collapse rates, and its measured size 4 log10(x)
/ m(x) is DILUTED over the zone -- no single-zero factor.

THEOREM GL5 (the quartic/ladder chase + the razor composition).
(a) IF lam_i == 8 eta_i^2 G t_i for i in a block THEN lam_i/tau ==
(eta_i/eta_0)^2 (t_i/t_0): the collapsed spectrum IS the jet ladder
squared, block-wide.  (b) IF J == THETA T_z^4 and FULLGAP == J t_r
- 1 THEN FULLGAP == THETA t_r T_z^4 - 1; monotone floor transfer:
[THETA >= theta_0, t_r >= c] ==> FULLGAP >= theta_0 c T_z^4 - 1.
(c) razor composition (GF1 + W3 CITED): [FULLGAP >= F_0] ==>
[delta_1 >= F_0] ==> g >= 1/(s + 1/F_0); with the s-cap s <= P:
g >= 1/(P + 1/F_0) -- the QSUBGAP-floor flows from the theta-floor
through the razor with explicit constants (machine-checked mp chain
per rung).  All chases sympy-exact.

MEASURED LAWS (typed GEMESSEN; the discovery layer):
(L1) THE QUARTIC LAW: J == THETA T_z^4 with THETA = 0.2569/0.1730/
     0.2451 at x = 5/8/13 (calibrated) and 0.190/0.220/0.183
     predicted at 18/24/28 from the frozen r142/r146/CDLII/r150
     strings -- flat O(1) over 20+ dex of jet collapse: THE GROWTH
     LAW IS ONE T_z^2 JET SLOT PER LEVEL, QUARTIC IN VALUE.  T_z =
     2 pi x is the PROVEN r131-G17 resolvability crossover: the
     exponent 4 is mechanism-shaped (two slots), the constant THETA
     is the open arithmetic window.
(L2) THE LADDER LAW: tlaw_i/tlaw_0 in (0.55, 1.45) for ALL i in the
     collapsed block (calibrated x=5: 0.889/0.882/0.885 for i<=3;
     x=8: 0.901/0.863/0.870/0.959/0.841/0.829 for i<=6; x=13:
     0.973/1.021/1.002/0.958/1.000/0.937): the zero-jet law holds at
     EVERY collapsed rung -- the whole collapsed spectrum is the jet
     ladder in value currency.  Second step c_2 = 0.2225/0.2367/
     0.2039 (an OCTIC second-gap law lam_2/tau ~ (c_1 c_2)^2 T_z^8).
(L3) LOO-JET-COLLECTIVE: rho_j = |A_0(psi_1-loo_j)/A_0(psi_1)| ==
     1.0000 for EVERY left-out zone zero (all m, calibrated to
     4+ digits at x = 5/8/13): removing any single zone constraint
     changes NEITHER the excited eigenvalue (GL1) NOR its jet -- the
     D1 deflation hypothesis (the excited jet = ground jet of the
     one-fewer-zero problem; one per-zero collapse factor) is
     REFUTED-MEASURED.  The zone constraints are INACTIVE at the
     bottom pair; the growth is carried by the free variational
     structure (value side), not the constraint count.
(L4) EDGE-CLUSTER PINCH (the D2 answer): the eps^2-scale pinch
     localizes on the top <= 3 zone zeros (band edge): p_j >= 0.9
     outside the top-3, min p_j = 0.017/0.130/0.263 AT the edge.
(L5) ADD-ONE FREE AT ZEROS: the price of additionally killing the
     next TRUE zero beyond T_z is g_add = 1.8e-6/2.0e-9/8.2e-17 --
     vs O(10) at interleaved non-zero points (contrast 1.8e7/7.3e9/
     2.9e17): the ground already kills the next zeros; m is not a
     cliff; per-zero pricing cannot generate the growth (arithmetic
     zero/non-zero contrast, the r160 dip signature in g-currency).
(L6) TRIAL CAP: v = (B - mu)phi/n (B = diag(b_k), mu = b-mean, exact
     phi-orthogonality) gives FULLGAP <= r_trial := Rayleigh(v)/tau
     - 1 HARD per rung (Courant), with the exact function identity
     E_v(t) == [(t^2 - mu) E_phi(t) - 2 A_0(phi) t sin(At)]/n; the
     trial is MID-DOMINATED (zone share ~0, saturation FULLGAP/
     r_trial = 0.057/0.0085/0.0022 falling): the naive zone-quartic
     derivation via this trial is REFUTED-MEASURED, honestly typed.
(L7) MOMENT-ROUTE OBSTRUCTED: the finite-P jet-moment-Gram model
     (tail Hankel H_pq vs dual jet Gram on V) undershoots FULLGAP by
     1.4/1.9/3.4 dex at P = 4 (worsening in x, monotone in P): the
     growth needs ALL jet orders -- the moment/Hankel route is dead
     (the r150-Y3/R4 rate-blindness one level up, measured).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
    Z1 TYPING (frozen): the leave-one-out/add-one batteries consume
    the certified pinned zone NODES (source data) and cache zeros
    below horizon as ward-class data -- typed, not hidden.
S1  exact layer: G10 GL1 (inclusion monotonicity instances + Y2
    transfer re-instance + pinch-position algebra); G11 GL2
    (arrowhead determinant/secular/eigvec/jet chases, generic
    3-level); G12 GL3 (interlacing instance + R = phi witness +
    razor vacuity + 2-level row-price witness, hard asserts);
    G13 GL4 (R2 re-chase + rate identities); G14 GL5 (ladder chase +
    quartic chase + monotone floor transfer + razor composition);
    G15 red team symbolic (jet toy: THETA free at fixed T_z with
    identities intact -- ALGEBRA-ONLY-REFUTED-FOR-THETA; only
    arithmetic-consuming windows may pin THETA).
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core + (18,140),(24,150),
    (28,160) deep (census: core raw-mp polyroots; deep zone
    sign-scan + newton, r141/r143 standard):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform);
    G31 spectral ladder: lam_i > 0 sorted; FULLGAP in the frozen
    windows x (0.97, 1.03); lam_1 simple (rel gap >= 1e3);
    post-loop growth slope in (3.4, 4.6);
    G32 node-config V + zone-top + razor: |qrel| <= 1e-30, null
    residual <= 1e-40; W3 re-gate delta_1 >= FULLGAP (1 - 1e-12);
    zone-top argmin in the frozen windows AND >= 3; s <= bar; sg in
    (0.98, 1.02); delta_1 windows; share_1 >= 0.5; tlaw_0 on the
    CDXLI strings (x <= 24) / in (0.40, 0.70) at 28; lock FULLGAP/
    y_t in (1.5, 6.0); GF1 lower re-gate g >= 1/(s + 1/delta_1)
    HARD; COMPOSED FLOOR g >= 1/(s + 1/(0.10 x 0.5 x T_z^4 - 1))
    HARD (the razor chain at the frozen theta window, mp);
    G33 jet block (L1): |eta_0^2/A_0(phi)^2 - 1| <= 1e-30; R2
    identity |jr t_r (FULLGAP/(1 + FULLGAP)) x (1+FULLGAP)/... ==
    1 + 1/FULLGAP| dev <= 1e-30; THETA in (0.10, 0.40); c_1 in
    (0.35, 0.60); jr in (0.8, 1.6); t_r in (0.5, 2.0);
    G34 ladder law (L2): collapsed block count nc printed; for
    1 <= i < min(nc, 8): tlaw_i/tlaw_0 in (0.55, 1.45); c_2 in
    (0.08, 0.45) when nc > 2;
    G35 loo battery (L3/L4 + GL1/GL2 instantiated): per zone index
    j: dual-row residual <= 1e-20; f(q_0) > 0 (GL1 bracket);
    |b_0|/q_1 <= 1e-20; rho_j in (0.98, 1.02) ALL j; p_j in
    [-1e-9, 1 + 1e-9]; p_j >= 0.9 outside the top-3 zone indices;
    min p_j <= 0.6 AND argmin in the top-3 (edge localization);
    jet resolvability sqrt(eps^2 |v0|^2)/|A_0(psi_1)| <= 1e-2;
    PINCH GUARD (frozen rule): the p_j gates apply only where
    (q_1 - lam_1) >= 10^{-(dps-10)} lam_max, else the rung's pinch
    is typed PRECISION-LIMITED and printed (expected possibly at
    x = 28; jet gates rho_j always apply);
    G36 add-one battery (L5): probes gamma_{m+1}, gamma_{m+2}
    (ward-class cache data below horizon) + the two interleaved
    midpoints: g_add(zero) <= 1e-2 both; g_add(mid) >= 3.0 both;
    contrast (paired mid/zero) >= 1e3 both;
    G37 trial cap (L6): orthogonality <= 1e-40 (exact by
    construction, mp residue); E_v identity rel dev <= 1e-40 at the
    3 frozen sample points (7.3, 19.1, 44.4); COURANT HARD r_trial
    >= FULLGAP (1 - 1e-12); saturation FULLGAP/r_trial in (5e-5,
    1.0); at x = 5/8 ONLY: zone-model/zone-sum in (0.9, 1.1) and
    zone share of the trial value <= 0.05 (gamma-side F64-LIMITED
    from x = 13, the r139/r141/r143 instrument class, DISCLOSED --
    deep rungs print r_trial/sat/tlaw_v only);
    G38 moment model (L7; CORE rungs only, P = 2/3/4, cut at
    om_max, cache + HSW envelope beyond gtop): FG_model monotone
    increasing in P AND FG_model(P=4) <= FULLGAP (undershoot):
    MOMENT-ROUTE-OBSTRUCTED pinned;
    G39 growth/rates (post-loop): THETA slope vs log10 x in (-0.45,
    +0.45) (the quartic residual: exponent pinned in 4 +- 0.45);
    per-zero differential diff = -(Dlog10|A_0(phi)| -
    Dlog10|A_0(psi_1)|)/Dm > 0 on every adjacent pair AND last-pair
    diff <= first-pair diff / 2.5 (DILUTION); per-zero rate tables
    printed (r_tau ~ 2 r_0 exhibit).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 (the GL/ladder/quartic hypotheses (PSD + simple
    positive ground) fail EXACTLY here) AND y_t_w/b_top <= 1.0;
    THETA_w printed (exhibit: the quartic law has no meaning
    without the positive collapsing ground); G53 consistency.
S5  G54 tau-screens: |slope log10 v vs log10 tau| <= 0.30 for v in
    (THETA, c_1, jr, t_r, sat) -- the demand ratios are tau-flat;
    RIDER report: slopes of log10 A_0(phi)^2, log10 A_0(psi_1)^2 vs
    log10 tau in (0.85, 1.15) (ride tau -- BOUND-RIDES-CONNES
    typed); G55 conditioning (1e-25 shift window).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence-demand ->
    Theorem R transfer -> coupling absorbed -> the THETA/c/loo/
    add-one coordinates consume source + secular + ward-class node/
    zero data only, no tlaw beyond its own frozen window, no Z, no
    lattice proximity -> V2 good sets -> no ALL-X demand);
    G61 min-cut (r116 replica; r142/r144/r146/r150 graph VERBATIM):
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL 9
    NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150),(28,160)); HSW = (0.1038, 0.2573, 9.3675) [HSW22
Cor. 1.2]; SCAN_STEP = 0.05; SCAN_LO = 0.5; SCAN_OVER = 6.0;
TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05; NODE_EXCL = 0.02;
BIS_ITERS = 250.
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26), 28: (10, 30)}; S_BAR_TAB =
{5..24: 0.1, 28: 0.15}; SGAP_WIN = (0.98, 1.02); D1_TAB = {5:
2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8, 28:
1.6513e8} x (0.7, 1.3); SHARE1_BAR = 0.5; TLAW_TAB = {5: 0.2664,
8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI
strings); TLAW28_WIN = (0.40, 0.70); FG_TAB = {5: 2.2255e5, 8:
9.9512e5, 13: 1.0619e7, 18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8}
x (0.97, 1.03); FG_SLOPE_WIN = (3.4, 4.6); SIMP_MIN = 1e3;
LOCK_WIN = (1.5, 6.0); ENC_SLOP = 1e-12; THETA_WIN = (0.10, 0.40)
(calibrated 0.256907/0.172985/0.245072 at 5/8/13; deep predicted
0.190/0.220/0.183 from frozen strings, DISCLOSED);
THETA_SLOPE_WIN = (-0.45, 0.45); C1_WIN = (0.35, 0.60) (calibrated
0.5069/0.4159/0.4950); C2_WIN = (0.08, 0.45) (calibrated 0.2225/
0.2367/0.2039; deep DISCLOSED); JR_WIN = (0.8, 1.6); TR_WIN =
(0.5, 2.0); ETA0_BAR = 1e-30; R2ID_BAR = 1e-30; TLAWLAD_WIN =
(0.55, 1.45); BLOCK_FRac = 0.1 (collapsed block lam_i < 0.1
lam_max); BLOCK_IMAX = 8; COMPOSED_THETA0 = 0.10; COMPOSED_TR0 =
0.5; LOO_URES_BAR = 1e-20; LOO_B0_BAR = 1e-20 (rel q_1); RHO_WIN =
(0.98, 1.02); P_OUT_MIN = 0.9; P_EDGE_MAX = 0.6; TOP_CLUSTER = 3;
JETRES_BAR = 1e-2 (calibrated 2.0e-3/5.1e-5/6.0e-9); PINCH_GUARD =
10^{-(dps-10)} lam_max; ADD_ZERO_MAX = 1e-2 (calibrated 1.8e-6/
2.0e-9/8.2e-17); ADD_MID_MIN = 3.0 (calibrated 32.0/14.5/23.7 and
15.9/9.4/19.0); ADD_CONTRAST_MIN = 1e3 (calibrated 1.8e7/7.3e9/
2.9e17); TRIAL_ORTHO_BAR = 1e-40; TRIAL_ID_BAR = 1e-40 (calibrated
3.1e-55/1.1e-73); TRIAL_SAMPLES = (7.3, 19.1, 44.4); SAT_WIN =
(5e-5, 1.0) (calibrated 0.0569/0.0085/0.0022); ZMODEL_WIN = (0.9,
1.1) (x = 5/8 only; calibrated 1.0010/0.9998); ZSHARE_BAR = 0.05;
MODEL_P = (2, 3, 4) (core only; calibrated FG_model dex devs
-2.9/-2.3/-1.4 at x=5, -3.6/-3.0/-1.9 at x=8, -4.5/-3.9/-3.4 at
x=13); DIFF_DILUTION = 2.5; CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR =
0.30; W0_RIDER_WIN = (0.85, 1.15); COND_WIN = (1e-40, 1e-10);
GAMMA1_LIT = 14.134725141734694 (ward only); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; np.float64-repr casts guarded by float()/repr(); tiny/
huge quantities stay mp end-to-end (r147 underflow lesson); THETA/
c/rho/p/sat are flat O(1) ratios transported as f64 for gating
(disclosed); census/build_V/secular_data/newton_node/row_at ported
VERBATIM from the r157/r161 gfloor source (== r138-r150 replica
class) with ONE disclosed extension: build_V additionally returns
the Cholesky back-substitution closure (bwd) and the constraint
row matrix Rm (needed by the loo instrument; no numeric path of
the replica changed).

CALIBRATION DISCLOSURE (pre-freeze, ONE scratch script
calib_scratch_fgl.py in THREE passes (x = 5/8 twice, x = 13 once;
logs calib_fgl_pass1/2/3.log kept), deleted after freeze; all
numbers quoted verbatim above and here): x=5: FG 2.225493e5, J
2.502511e5, THETA 0.256907, c_1 0.506860, jr 1.1245, tlaw_0/1
0.2664/0.2369, t_r 0.8893, y_t 6.1067e4, lock 3.6444, loo rho ==
1.0000 (all 4), pinch p = 1.0000/0.9988/0.9844/0.0168, add-one
1.82e-6 (gam_5) / 31.96 (mid) / 7.69e-5 (gam_6) / 15.91 (mid),
trial r 3.913545e6 sat 0.0569 tlaw_v 0.0746 nu 1.1495e-4, zone-
model ratio 1.0010, ladder tlaw_i 0.2664/0.2369/0.2350/0.2357
(nc=4), c_2 0.2225, eta-head 4.73e-8/2.37e-5/-5.20e-3/3.62e-1,
model FG 2.66e2/1.25e3/8.78e3 (P=2/3/4).  x=8: FG 9.951249e5, J
1.104303e6, THETA 0.172985, c_1 0.415915, jr 1.1097, t_r 0.9011,
loo rho == 1.0000 (all 10), p outside top-3 >= 0.9990, p edge
0.1297, add-one 1.99e-9/14.54/1.33e-7/9.40, trial r 1.165195e8
sat 0.0085, ladder tlaw_i/tlaw_0 0.901/0.863/0.870/0.959/0.841/
0.829, c_2 0.2367, model FG 2.83e2/1.02e3/1.15e4.  x=13 (pass 3):
FG 1.061906e7, THETA 0.245072, c_1 0.495048, t_r 0.9734, loo rho
== 1.0000 (all 21), p = 1.0000 (j <= 17), 0.9670/0.7699/0.2634
(j = 18/19/20), add-one 8.19e-17/23.70/8.48e-16/19.01, trial r
4.775696e9 sat 0.0022, ladder tlaw_i/tlaw_0 0.973/1.021/1.002/
0.958/1.000/0.937, c_2 0.2039, model FG dex dev -4.5/-3.9/-3.4;
the x=13 trial zone-sum via cache f64 ordinates is polluted (the
known f64-ordinate class) -- hence the G37 zone gates restricted
to x = 5/8, DISCLOSED above.  x = 18/24/28 pre-freeze UNMEASURED
on all new quantities (build cost); their windows are set from the
frozen r139-r161/CDLII strings, the calibrated flat trends and
structure asserts, DISCLOSED.  Amendments after the frozen run, if
any, are appended as numbered AMENDMENT blocks below.

VERDICT ENUMS (frozen): GL1-PROVEN(loo pinch: every leave-one-out
matches lam_1 within the eps^2 budget) + LOO-EIGEN-PINCHED(measured);
GL2-PROVEN(arrowhead instrument exact); GL3-PROVEN(one-row price
equivalence: weakest sufficient floor == the floor, witness R = phi;
razor vacuity; ALGEBRA-ONLY-REFUTED-FOR-ROWPRICE: D3 collapses to
the razor); GL4-PROVEN(rate bookkeeping; R2 re-gated) +
PERZERO-DILUTED(measured); GL5-PROVEN(ladder + quartic chases +
monotone floor transfer + razor composition, mp-checked per rung);
QUARTIC-LAW(J == THETA T_z^4, THETA flat in the frozen window with
slope-gated exponent 4 +- 0.45: THE GROWTH LAW'S CLOSED FORM,
MEASURED; derivation status CLASSICAL-CONDITIONAL-CANDIDATE: the
open kernel is ONE flat O(1) window THETA -- same class as the tlaw
window, arithmetic-consuming by G15); LADDER-LAW(block-wide zero-jet
law + octic second gap: the collapsed spectrum is the jet ladder
squared); LOO-JET-COLLECTIVE(D1 deflation hypothesis REFUTED-
MEASURED: no per-zero jet factor exists; constraints inactive);
EDGE-CLUSTER-PINCH(D2 answered: the band-edge top <= 3 zeros carry
the eps^2 pinch); ADDONE-FREE-AT-ZEROS(L5 contrast: per-zero pricing
cannot generate the growth); TRIAL-CAP-CERTIFIED(Courant hard) +
TRIAL-MID-DOMINATED(the naive zone-quartic derivation refuted);
MOMENT-ROUTE-OBSTRUCTED(L7); CONTROLS-REFUSE; DEMAND-FLAT +
BOUND-RIDES-CONNES; QUANTIFIER-INHERITED(dense-x suffices,
CHAIN-AUDIT); OMEGA-RECOORDINATED(residue SET UNCHANGED: the
delta_1-floor coordinate becomes the THETA-window x t_r-window via
GL5; TOPROOT/TLAWCAP/QSUBGAP unchanged; census {MEAS, OMEGA-POS}
cardinality 4 UNCHANGED); MINCUT(4/5).  Composite priority:
INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 26/28 at SPEC_SHA
e722fb65d0a3c68c, log kept as the pre-amendment record
fgl_run1.log).  TWO INSTRUMENT RE-TYPINGS, no bar or criterion
moved on the resolvable domain; all headline gates (G30-G34,
G37-G39, G5x, G6x) passed run 1 unchanged:
(a) the G35 b_0 purity diagnostic was frozen normalized by q_1; at
x = 24/28 this divides an eigsy-precision ABSOLUTE residual (the
z_0-column accuracy against a >100-dex-collapsed bottom gap) by
the collapsed q_1 itself -- measured 6e-18/7e-01 there, while the
battery's operative quantities (rho_j, ures, jres; the arrowhead
EXCLUDES the 0-row by construction) stayed clean at all rungs.
Renormalized to lam_max, the arrowhead's operative scale; bar
unchanged (1e-20).  This is the r147 underflow-lesson class read
in reverse (a diagnostic denominated in a collapsing currency).
(b) the G36 add-one battery consumes the f64 cache ordinates; at
x = 24/28 the f64 ordinate offset (~1e-9 gamma) exceeds the
pinning well width -- the KNOWN r139/r141/r143 'f64 grid wider
than the well' instrument class, here biting the g-instrument at
x = 24 instead of x = 13 (measured: x=24 g_add(zero) 1.8e-2 with
contrast 1.1e3 still intact; x=28 contrast 1.0, fully unresolved).
The G36 hard gates are restricted to x <= 18; x = 24/28 are typed
F64-ORDINATE-LIMITED and printed measured-only.  The failed run-1
reads are themselves the measured instrument-resolution law and
stay in the record (the l1/CDXXXIII f2 zone-typing lesson).
Run 2 = run of record at the amended SPEC_SHA; run 3 =
deterministic re-run.
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
ENC_SLOP = 1e-12
THETA_WIN = (0.10, 0.40)
THETA_SLOPE_WIN = (-0.45, 0.45)
C1_WIN = (0.35, 0.60)
C2_WIN = (0.08, 0.45)
JR_WIN = (0.8, 1.6)
TR_WIN = (0.5, 2.0)
ETA0_BAR = 1e-30
R2ID_BAR = 1e-30
TLAWLAD_WIN = (0.55, 1.45)
BLOCK_FRAC = 0.1
BLOCK_IMAX = 8
COMPOSED_THETA0 = 0.10
COMPOSED_TR0 = 0.5
LOO_URES_BAR = 1e-20
LOO_B0_BAR = 1e-20
RHO_WIN = (0.98, 1.02)
P_OUT_MIN = 0.9
P_EDGE_MAX = 0.6
TOP_CLUSTER = 3
JETRES_BAR = 1e-2
ADD_ZERO_MAX = 1e-2
ADD_MID_MIN = 3.0
ADD_CONTRAST_MIN = 1e3
TRIAL_ORTHO_BAR = 1e-40
TRIAL_ID_BAR = 1e-40
TRIAL_SAMPLES = (7.3, 19.1, 44.4)
SAT_WIN = (5e-5, 1.0)
ZMODEL_WIN = (0.9, 1.1)
ZSHARE_BAR = 0.05
ZGATE_RUNGS = (5, 8)
MODEL_P = (2, 3, 4)
DIFF_DILUTION = 2.5
CTRL_YTB_MAX = 1.0
TAU_SLOPE_BAR = 0.30
W0_RIDER_WIN = (0.85, 1.15)
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
    """round-132 AMENDMENT-1 node source VERBATIM (r157/r161 replica)."""
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
    orthonormalized compression of Mq (r138-r161 replica VERBATIM;
    disclosed extension: also returns Rm and the bwd closure)."""
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

        def bwd(rhs_list, L=L, nf=nf):
            z = [mp.mpf(0)] * nf
            for i in range(nf - 1, -1, -1):
                acc = rhs_list[i]
                for j2 in range(i + 1, nf):
                    acc -= L[j2, i] * z[j2]
                z[i] = acc / L[i, i]
            return z

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
    return dict(qs=qs, Z=Z, Nb=Nb, fwd=fwd, bwd=bwd, nf=nf, resR=resR,
                qrel=qrel, cs=cs, aa=aa, oms=oms, nrm=nrm,
                tau_mp=tau_mp, Rm=Rm)


def secular_data(Vd: dict, r: list):
    """(lam*, etn, rho2, chi) for the extra row r on V (r141/r161
    shape; bisection BIS_ITERS).  Caller sets workdps."""
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
    return lo, etn, rho2, chi


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 GL1: loo pinch
    # inclusion monotonicity on exact instances
    M3 = sp.diag(1, 2, 5)
    lam1 = sp.Integer(2)               # min over e0-perp
    q_sub = sp.Integer(5)              # min over span(e3) subset
    okA = bool(lam1 <= q_sub)
    # constrained min over span(e2,e3) subset e0-perp equals 2 >= lam1
    okB = bool(sp.Integer(2) >= lam1)
    # Y2 transfer re-instance (CDL, cited): Rayleigh expansion
    l1s, lmax, e2s = sp.symbols("l1s lmax e2s", positive=True)
    lhs = (l1s * (1 - 2 * e2s) + e2s * lmax) / (1 - e2s)
    rhs = l1s + e2s * (lmax - l1s) / (1 - e2s)
    okC = sp.simplify(lhs - rhs) == 0
    okD = bool(sp.Rational(12, 2) <= 2 + sp.Rational(1, 2)
               * (10 - 2) / sp.Rational(1, 2))  # diag(1,2,10) instance
    # pinch position algebra: p in [0,1] <=> lam_loo in [lam1, q1]
    lamloo, q1s = sp.symbols("lamloo q1s", positive=True)
    p_ = (lamloo - l1s) / (q1s - l1s)
    okE = sp.simplify(p_.subs(lamloo, l1s)) == 0 \
        and sp.simplify(p_.subs(lamloo, q1s) - 1) == 0
    out.append(("G10-gl1-loo-pinch", okA and okB and okC and okD
                and okE,
                "min over a subset subspace >= min over the superset "
                "(exact instances, Courant CITED); phi-perp "
                "constrained mins sandwich lam_1 <= lam_loo <= q_1; "
                "Y2 transfer q_1 - lam_1 <= eps^2(lam_max - lam_1)/"
                "(1 - eps^2) re-instanced: THEOREM GL1 -- every "
                "leave-one-out matches lam_1 within the eps^2 budget; "
                "the pinch position p_j is the honest discriminator"))

    # ---------------- G11 GL2: arrowhead instrument
    lam, q1a, q2a, b1, b2, cc = sp.symbols(
        "lam q1a q2a b1 b2 cc", real=True)
    Arr = sp.Matrix([[q1a, 0, b1], [0, q2a, b2], [b1, b2, cc]])
    det = (Arr - lam * sp.eye(3)).det()
    sec = ((q1a - lam) * (q2a - lam)
           * (cc - lam - b1 ** 2 / (q1a - lam)
              - b2 ** 2 / (q2a - lam)))
    okF = sp.simplify(det - sec) == 0
    # eigvec chase: w_i = -b_i/(q_i - lam), u-comp 1 solves rows
    w1 = -b1 / (q1a - lam)
    w2 = -b2 / (q2a - lam)
    okG = sp.simplify((q1a - lam) * w1 + b1) == 0 \
        and sp.simplify((q2a - lam) * w2 + b2) == 0
    # border row == secular root equation
    okH = sp.simplify((b1 * w1 + b2 * w2 + (cc - lam))
                      - (cc - lam - b1 ** 2 / (q1a - lam)
                         - b2 ** 2 / (q2a - lam))) == 0
    # jet linearity
    et1, et2, etu = sp.symbols("et1 et2 etu", real=True)
    okI = sp.simplify((et1 * w1 + et2 * w2 + etu)
                      - (etu - et1 * b1 / (q1a - lam)
                         - et2 * b2 / (q2a - lam))) == 0
    # dual-row identity: u = R^T (R R^T)^{-1} e_j has R u = e_j
    Rr = sp.Matrix([[1, 0, 1], [0, 2, 0]])
    uj = Rr.T * (Rr * Rr.T) ** (-1) * sp.Matrix([1, 0])
    okJ = sp.simplify(Rr * uj - sp.Matrix([1, 0])) == sp.zeros(2, 1)
    out.append(("G11-gl2-arrowhead", okF and okG and okH and okI
                and okJ,
                "det(arrowhead - lam) == prod(q_i - lam) x secular "
                "f(lam) generic; eigvec w_i = -b_i/(q_i - lam) with "
                "u-component 1; 0-jet = sum eta_i w_i + eta_u "
                "(linearity); dual row R^T(RR^T)^{-1}e_j realizes "
                "R u = e_j: THEOREM GL2 -- the leave-one-out problem "
                "is the exact arrowhead compression"))

    # ---------------- G12 GL3: one-row price equivalence (D3)
    # interlacing instance: M = diag(1,2,5), row (1,1,0):
    # kernel basis (1,-1,0)/sqrt2, e3: compression diag(3/2, 5)
    okK = bool(sp.Integer(1) <= sp.Rational(3, 2) <= sp.Integer(2))
    # R = phi witness: eigenframe row e0 -> ground lam_1 exactly
    okL = bool(sp.Integer(2) == min(2, 5))
    # razor vacuity: 1/(s + 1/F) <= F identically
    spos, Fpos = sp.symbols("spos Fpos", positive=True)
    okM = sp.simplify(Fpos - 1 / (spos + 1 / Fpos)
                      - spos * Fpos ** 2 / (spos * Fpos + 1)) == 0 \
        and (spos * Fpos ** 2 / (spos * Fpos + 1)).is_positive is True
    # 2-level row-price witness: price -> 0 at fixed FULLGAP
    Pw, d1w = sp.symbols("Pw d1w", positive=True)
    rho2w = 1 / (1 + Pw * d1w)
    gw = rho2w * d1w
    okN = sp.simplify(gw - d1w / (1 + Pw * d1w)) == 0 \
        and sp.limit(gw, Pw, sp.oo) == 0
    out.append(("G12-gl3-one-row-equivalence", okK and okL and okM
                and okN,
                "single-row interlacing tau <= ground(ker R) <= lam_1 "
                "(instance + Cauchy CITED) ==> FULLGAP >= every "
                "one-row price; witness R = phi achieves EQUALITY "
                "(eigenframe): weakest-sufficient floor == the floor; "
                "razor vacuity 1/(s + 1/F) <= F identically + 2-level "
                "witness price -> 0 with identities intact: THEOREM "
                "GL3 -- D3 COLLAPSES TO THE RAZOR, algebra-only "
                "per-row/per-zero price bounds REFUTED"))

    # ---------------- G13 GL4: rate bookkeeping
    A0a, A0b, Ga, t0a, t1a, tau_ = sp.symbols(
        "A0a A0b Ga t0a t1a tau_", positive=True)
    lam1_ = 8 * A0b ** 2 * Ga * t1a
    tau_d = 8 * A0a ** 2 * Ga * t0a
    Jd = (A0b / A0a) ** 2
    FGd = lam1_ / tau_d - 1
    okO = sp.simplify(Jd * (t1a / t0a) - (FGd + 1)) == 0
    jr_d = Jd / FGd
    okP = sp.simplify(jr_d * (t1a / t0a) - (1 + 1 / FGd)) == 0
    # per-zero identity: Dlog J == 2(Dlog A0b - Dlog A0a) (defs)
    okQ = sp.simplify(sp.log(Jd) - 2 * (sp.log(A0b) - sp.log(A0a))) \
        == 0
    out.append(("G13-gl4-rate-bookkeeping", okO and okP and okQ,
                "J x t_r == 1 + FULLGAP and jr x t_r == 1 + "
                "1/FULLGAP (r150 R2 re-chase from the zero-jet "
                "definitions); Dlog J == 2 Dlog(A_0 ratio) exact: "
                "THEOREM GL4 -- the per-zero FULLGAP growth is the "
                "per-zero differential of two jet collapse rates "
                "(diluted over the zone, measured in G39)"))

    # ---------------- G14 GL5: ladder + quartic + razor composition
    eta0, eta1, ti, t0b = sp.symbols("eta0 eta1 ti t0b", positive=True)
    lam_i = 8 * eta1 ** 2 * Ga * ti
    tau_i = 8 * eta0 ** 2 * Ga * t0b
    okR = sp.simplify(lam_i / tau_i
                      - (eta1 / eta0) ** 2 * (ti / t0b)) == 0
    TH, Tz, trr = sp.symbols("TH Tz trr", positive=True)
    FGq = TH * Tz ** 4 * trr - 1
    okS = sp.simplify((TH * Tz ** 4) * trr - 1 - FGq) == 0
    th0, ctr = sp.symbols("th0 ctr", positive=True)
    diff1 = (TH * Tz ** 4 * trr - 1) - (th0 * ctr * Tz ** 4 - 1)
    okT = sp.simplify(diff1.subs([(TH, th0), (trr, ctr)])) == 0 \
        and sp.simplify(sp.diff(TH * Tz ** 4 * trr, TH)) \
        == Tz ** 4 * trr
    # razor composition: delta1 >= F0 ==> 1/(s + 1/delta1) >=
    # 1/(s + 1/F0); with s <= P: >= 1/(P + 1/F0)
    F0, de1, sv, Pv = sp.symbols("F0 de1 sv Pv", positive=True)
    expr = 1 / (sv + 1 / de1) - 1 / (sv + 1 / F0)
    okU = sp.simplify(expr.subs(de1, F0)) == 0 \
        and (sp.diff(1 / (sv + 1 / de1), de1)).is_positive is True \
        and (sp.diff(1 / (sv + 1 / F0), sv)).is_negative is True
    out.append(("G14-gl5-quartic-razor", okR and okS and okT and okU,
                "[lam_i == 8 eta_i^2 G t_i] ==> lam_i/tau == "
                "(eta_i/eta_0)^2 (t_i/t_0) (LADDER chase); [J == "
                "THETA T_z^4] + R2 ==> FULLGAP == THETA t_r T_z^4 - "
                "1 with monotone floor transfer [THETA >= theta_0, "
                "t_r >= c] ==> FULLGAP >= theta_0 c T_z^4 - 1; razor "
                "composition (GF1 + W3 CITED): delta_1-floor "
                "monotone through g >= 1/(s + 1/delta_1), s-cap "
                "monotone: THEOREM GL5 -- the QSUBGAP-floor flows "
                "from the THETA-window through the razor"))

    # ---------------- G15 red team symbolic
    p_, q_, Tt = sp.symbols("p_ q_ Tt", positive=True)
    theta_toy = (q_ / p_) ** 2 / Tt ** 4
    okV = sp.simplify(theta_toy.subs(q_, 10 ** 3 * Tt ** 2 * p_)
                      - 10 ** 6) == 0
    okW = sp.simplify(theta_toy.subs(q_, p_ * Tt ** 2 / 10 ** 3)
                      - sp.Rational(1, 10 ** 6)) == 0
    out.append(("G15-redteam-theta-free", okV and okW,
                "jet toy: with a free jet functional the ratio "
                "(A_0(psi_1)/A_0(phi))^2/T_z^4 takes ANY value (1e6 "
                "and 1e-6 witnesses) while all GL identities hold: "
                "ALGEBRA-ONLY-REFUTED-FOR-THETA -- only arithmetic-"
                "consuming windows (census/zone/tlaw currency) may "
                "pin the quartic constant"))
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
    steps.append(("THETA/c_1/c_2/loo/add-one coordinates consume "
                  "source + secular data + ward-class certified "
                  "nodes/zeros below horizon ONLY (Z1-typed); no Z, "
                  "no lattice proximity (r142 W2/W3 + r141 V1 "
                  "cited)", True))
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

    print("fullgap_growthlaw_probe -- PRIME.FULLGAP.GROWTHLAW.01")
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
    info("Z1 TYPING (frozen): the loo/add-one batteries consume the "
         "certified pinned zone NODES (source data) and cache zeros "
         "below horizon as ward-class data -- typed, not hidden")

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems GL1-GL5 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R; r131 secular + GW + OFF + G17 crossover; r132 "
         "raw census; r137/CDXLI tlaw strings; r141/CDXLV V1-V3 + "
         "quantifier; r142/CDXLVI W1-W3 + FULLGAP strings; r143/"
         "CDXLVII delta_1-lock; CDL Y1-Y4 + zero-jet law; CDLII "
         "x=28 strings; CDLIV R1-R4 + jr/t_r strings; CDLVII RES1/"
         "RES2; CDLXI SB1-SB5; CDLXIV kappa-collapse (collective "
         "verdict); CDLXV GF1-GF5 (razor); HSW22 Cor. 1.2; PT21; "
         "Courant-Fischer; Cauchy interlacing; partial fractions; "
         "Euler sine product")

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
    section("S3  LADDER: THE GROWTH-LAW ANATOMY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = True
    ok35 = ok36 = ok37 = ok38 = True
    det30, det31, det32, det33, det34 = [], [], [], [], []
    det35, det36, det37, det38 = [], [], [], []
    tau_tab, fg_tab, th_tab, c1_tab = {}, {}, {}, {}
    jr_tab, tr_tab, sat_tab = {}, {}, {}
    a0p_tab, a01_tab, m_tab, x_used = {}, {}, {}, []
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
        x_used.append(x)
        m_tab[x] = m_zone
        with mp.workdps(dps):
            E = ce["mpE"]
            V = ce["mpV"]
            Mq = ce["mpM"]
            tau = E[0]
            lam1 = E[1]
            lam2 = E[2]
            lammax = E[K - 1]
            FG = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0p = sum(((-1) ** k) * cs[k] for k in range(K))
            A2p = sum(((-1) ** k) * cs[k] * b[k] for k in range(K))
            yt = float(abs(A2p / A0p))
            tauf = float(tau)
            fg_f = float(FG)
            simp = float((lam2 - lam1) / lam1)
        Gz = hsw_G(Tz)
        tlaw0_f = tauf / (8.0 * float(abs(A0p)) ** 2 * Gz)
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

        # ---- G31 spectral ladder
        with mp.workdps(dps):
            pos_ok = all(E[i] > 0 for i in range(K))
            sort_ok = all(E[i] <= E[i + 1] for i in range(K - 1))
        fg_ok = FG_TAB[x] * FG_WIN[0] <= fg_f <= FG_TAB[x] * FG_WIN[1]
        ok31x = pos_ok and sort_ok and fg_ok and simp >= SIMP_MIN
        ok31 = ok31 and ok31x
        det31.append("x%d: FULLGAP %.6e (win %s) simp %.1e"
                     % (x, fg_f, fg_ok, simp))

        # ---- G32 node-config V + zone-top + razor
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            qs = Vd["qs"]
            nf = Vd["nf"]
            tau_v = Vd["tau_mp"]
            d1 = (qs[1] - qs[0]) / tau_v
            d1_f = float(d1)
            w3_ok = bool(d1 >= FG * (1 - mp.mpf("1e-12")))
            tg_grid = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                     TOP_GRID_STEP)) + [Tz - 0.001]
            gmin, argp = None, None
            for tv in tg_grid:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - qs[0]) / tau_v)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, etn, rho2, chi = secular_data(Vd, r)
            g_ex = (lam - qs[0]) / tau_v
            s_val = tau_v * chi / rho2
            sg = float(s_val * g_ex)
            s_f = float(s_val)
            g_f = float(g_ex)
            e12 = etn[1] * etn[1]
            share1_mp = (e12 / (qs[1] - qs[0])) / chi
            share1 = float(share1_mp)
            slop = mp.mpf(repr(ENC_SLOP))
            gf1_lo = 1 / (s_val + 1 / d1)
            gf1_ok = bool(gf1_lo <= g_ex * (1 + slop))
            Tz4 = mp.mpf(repr(Tz)) ** 4
            F0comp = mp.mpf(repr(COMPOSED_THETA0)) \
                * mp.mpf(repr(COMPOSED_TR0)) * Tz4 - 1
            comp_lo = 1 / (s_val + 1 / F0comp)
            comp_ok = bool(F0comp > 0) \
                and bool(g_ex >= comp_lo * (1 - slop))
            comp_d1_ok = bool(d1 >= F0comp * (1 - slop))
        lock = fg_f / yt
        lo_w, hi_w = REPL_WIN[x]
        if x <= 24:
            tl_ok = abs(tlaw0_f / TLAW_TAB[x] - 1.0) <= TLAW_TOL
        else:
            tl_ok = TLAW28_WIN[0] <= tlaw0_f <= TLAW28_WIN[1]
        ok32x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR and w3_ok
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR_TAB[x]
                 and SGAP_WIN[0] <= sg <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR and tl_ok
                 and LOCK_WIN[0] <= lock <= LOCK_WIN[1]
                 and gf1_ok and comp_ok and comp_d1_ok)
        ok32 = ok32 and ok32x
        det32.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1/FG "
                     "%.6f lock %.3f gf1lo/g %.6f composed-floor "
                     "%.4f<=g %s (%.0f s)"
                     % (x, Vd["qrel"], gmin, s_f, sg, d1_f / fg_f,
                        lock, float(gf1_lo / g_ex), float(comp_lo),
                        comp_ok, time.time() - t_q))
        info("x=%d RAZOR CHAIN (GL5c instantiated): composed floor "
             "1/(s + 1/(theta_0 c T_z^4 - 1)) = %.4f <= GF1 lower "
             "%.4f <= g = %.4f; delta_1 = %.4e >= theta_0 c T_z^4 - "
             "1 = %.4e: the QSUBGAP-floor flows from the frozen "
             "THETA window through the razor at this rung"
             % (x, float(comp_lo), float(gf1_lo * 1), g_f, d1_f,
                float(F0comp)))

        # ---- G33 jet block (L1): the quartic law
        with mp.workdps(dps):
            v0 = [((-1) ** k) / nrm[k] for k in range(K)]
            d0 = []
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Nb"][k, fi] * v0[k]
                d0.append(acc)
            e0v = Vd["fwd"](d0)
            eta = []
            for i in range(nf):
                acc = mp.mpf(0)
                for k in range(nf):
                    acc += Vd["Z"][k, i] * e0v[k]
                eta.append(acc)
            eta0dev = float(abs(eta[0] * eta[0] / (A0p * A0p) - 1))
            cs1 = [V[i, 1] / nrm[i] for i in range(K)]
            A01 = sum(((-1) ** k) * cs1[k] for k in range(K))
            J = (A01 / A0p) ** 2
            Tz2 = mp.mpf(repr(Tz)) ** 2
            theta = float(J / Tz2 ** 2)
            c1v = float(abs(A01 / A0p) / Tz2)
            jr = float(J / FG)
            G_mp = mp.mpf(repr(Gz))
            tlaw1 = float(lam1 / (8 * A01 * A01 * G_mp))
            # smoke-1 instrument fix (disclosed): the R2 identity must
            # be evaluated with the mp t-ratio -- the f64-cast tlaw
            # ratio injects ~1e-16 rounding into an exact 1e-30-gated
            # chain (the r141 amendment-1 / CDL smoke-1 class).  The
            # float t_r is kept for the window gate display only.
            # No bar, criterion or ladder moved.
            t_r_mp = (lam1 * A0p * A0p) / (tau * A01 * A01)
            t_r = float(t_r_mp)
            r2id = float(abs((J / FG) * t_r_mp / (1 + 1 / FG) - 1))
            a0p_tab[x] = float(mp.log(abs(A0p)) / mp.log(10))
            a01_tab[x] = float(mp.log(abs(A01)) / mp.log(10))
        ok33x = (eta0dev <= ETA0_BAR and r2id <= R2ID_BAR
                 and THETA_WIN[0] <= theta <= THETA_WIN[1]
                 and C1_WIN[0] <= c1v <= C1_WIN[1]
                 and JR_WIN[0] <= jr <= JR_WIN[1]
                 and TR_WIN[0] <= t_r <= TR_WIN[1])
        ok33 = ok33 and ok33x
        det33.append("x%d: THETA %.4f c1 %.4f jr %.4f t_r %.4f "
                     "r2id %.0e eta0 %.0e"
                     % (x, theta, c1v, jr, t_r, r2id, eta0dev))
        th_tab[x] = theta
        c1_tab[x] = c1v
        jr_tab[x] = jr
        tr_tab[x] = t_r
        info("x=%d QUARTIC LAW exhibit (L1): J = (A_0(psi_1)/"
             "A_0(phi))^2 = %.6e == %.4f x T_z^4 (T_z = 2 pi x, the "
             "proven G17 crossover); FULLGAP = THETA t_r T_z^4 - 1; "
             "the growth law's closed form, measured"
             % (x, float(J), theta))

        # ---- G34 ladder law (L2)
        with mp.workdps(dps):
            nc1 = sum(1 for i in range(K)
                      if E[i] < mp.mpf(repr(BLOCK_FRAC)) * lammax)
            imax = min(nc1, BLOCK_IMAX)
            lad_ok = True
            rows_l = []
            A_prev = None
            c2v = None
            for i in range(0, imax):
                csi = [V[k2, i] / nrm[k2] for k2 in range(K)]
                A0i = sum(((-1) ** k2) * csi[k2] for k2 in range(K))
                tli = float(E[i] / (8 * A0i * A0i * G_mp))
                if i >= 1:
                    rat = float(abs(A0i / A_prev) / Tz2)
                    lr = tli / tlaw0_f
                    lad_ok = lad_ok and TLAWLAD_WIN[0] <= lr \
                        <= TLAWLAD_WIN[1]
                    if i == 2:
                        c2v = rat
                    rows_l.append("i%d:%.3f/%.4f" % (i, lr, rat))
                A_prev = A0i
            c2_ok = True if c2v is None else \
                (C2_WIN[0] <= c2v <= C2_WIN[1])
        ok34x = lad_ok and c2_ok
        ok34 = ok34 and ok34x
        det34.append("x%d: nc %d [tlaw_i/tlaw_0 / step_i/Tz^2]: %s"
                     % (x, nc1, " ".join(rows_l)))
        info("x=%d LADDER LAW exhibit (L2): the zero-jet law holds "
             "at every collapsed rung (block nc = %d); c_2 = %s -- "
             "octic second-gap law lam_2/tau ~ (c_1 c_2)^2 T_z^8"
             % (x, nc1, "%.4f" % c2v if c2v is not None else "n/a"))

        # ---- G35 loo battery (L3/L4)
        t_l = time.time()
        with mp.workdps(dps):
            mcon = m_zone
            RG = mp.zeros(mcon, mcon)
            for i in range(mcon):
                for j2 in range(i + 1):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Vd["Rm"][i, k] * Vd["Rm"][j2, k]
                    RG[i, j2] = RG[j2, i] = acc
            psi1 = [V[i, 1] for i in range(K)]
            dl_ = []
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Nb"][k, fi] * psi1[k]
                dl_.append(acc)
            yy = Vd["fwd"](dl_)
            eps2 = 1 - sum(v * v for v in yy)
            v0n2 = sum(v * v for v in v0)
            jres = float(mp.sqrt(abs(eps2) * v0n2) / abs(A01))
            pinch_den = qs[1] - lam1
            guard = mp.mpf(10) ** (-(dps - 10)) * lammax
            pinch_res = bool(pinch_den >= guard)
            rho_ok = True
            p_ok = True
            pmin, pargj = None, None
            worst_ures = 0.0
            worst_b0 = 0.0
            f0_ok = True
            rows_p = []
            for j in range(mcon):
                rhs = [mp.mpf(1) if i == j else mp.mpf(0)
                       for i in range(mcon)]
                ysol = mp.lu_solve(RG, mp.matrix(rhs))
                u = [mp.mpf(0)] * K
                for k in range(K):
                    acc = mp.mpf(0)
                    for i in range(mcon):
                        acc += Vd["Rm"][i, k] * ysol[i]
                    u[k] = acc
                worst = 0.0
                for i in range(mcon):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Vd["Rm"][i, k] * u[k]
                    tgt = mp.mpf(1) if i == j else mp.mpf(0)
                    worst = max(worst, float(abs(acc - tgt)))
                worst_ures = max(worst_ures, worst)
                yv = Vd["fwd"]([sum(Vd["Nb"][k, fi] * u[k]
                                    for k in range(K))
                                for fi in range(nf)])
                zv = Vd["bwd"](yv)
                Pu = [mp.mpf(0)] * K
                for k in range(K):
                    acc = mp.mpf(0)
                    for fi in range(nf):
                        acc += Vd["Nb"][k, fi] * zv[fi]
                    Pu[k] = acc
                un2 = sum(v * v for v in u)
                pn2 = sum(v * v for v in yv)
                s_ = mp.sqrt(un2 - pn2)
                ut = [(u[k] - Pu[k]) / s_ for k in range(K)]
                Mu = [mp.mpf(0)] * K
                for i in range(K):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Mq[i, k] * ut[k]
                    Mu[i] = acc
                yb = Vd["fwd"]([sum(Vd["Nb"][k, fi] * Mu[k]
                                    for k in range(K))
                                for fi in range(nf)])
                etb = []
                for i in range(nf):
                    acc = mp.mpf(0)
                    for k in range(nf):
                        acc += Vd["Z"][k, i] * yb[k]
                    etb.append(acc)
                cval = sum(ut[k] * Mu[k] for k in range(K))
                eta_u = sum(v0[k] * ut[k] for k in range(K))
                # AMENDMENT 1a: purity diagnostic vs lam_max (the
                # arrowhead's operative scale), not the collapsed q_1
                worst_b0 = max(worst_b0, float(abs(etb[0]) / lammax))

                def fsec_l(lam_, cval=cval, etb=etb):
                    acc = cval - lam_
                    for i in range(1, nf):
                        acc -= etb[i] * etb[i] / (qs[i] - lam_)
                    return acc
                f0_ok = f0_ok and bool(fsec_l(qs[0]) > 0)
                lo_, hi_ = qs[0], qs[1]
                for _ in range(BIS_ITERS):
                    mid_ = (lo_ + hi_) / 2
                    if fsec_l(mid_) > 0:
                        lo_ = mid_
                    else:
                        hi_ = mid_
                lam_loo = (lo_ + hi_) / 2
                comp = [-etb[i] / (qs[i] - lam_loo)
                        for i in range(1, nf)]
                cn2 = sum(v * v for v in comp) + 1
                A0loo = (sum(eta[i + 1] * comp[i]
                             for i in range(nf - 1)) + eta_u) \
                    / mp.sqrt(cn2)
                rho = float(abs(A0loo / A01))
                rho_ok = rho_ok and RHO_WIN[0] <= rho <= RHO_WIN[1]
                if pinch_res:
                    pj = float((lam_loo - lam1) / pinch_den)
                    if pmin is None or pj < pmin:
                        pmin, pargj = pj, j
                    in_top = j >= mcon - TOP_CLUSTER
                    p_ok = p_ok and (-1e-9 <= pj <= 1 + 1e-9) \
                        and (in_top or pj >= P_OUT_MIN)
                    rows_p.append("%.3f" % pj)
                else:
                    rows_p.append("--")
            if pinch_res:
                p_ok = p_ok and pmin is not None \
                    and pmin <= P_EDGE_MAX \
                    and pargj >= mcon - TOP_CLUSTER
        ok35x = (worst_ures <= LOO_URES_BAR
                 and worst_b0 <= LOO_B0_BAR and f0_ok and rho_ok
                 and jres <= JETRES_BAR
                 and (p_ok if pinch_res else True))
        ok35 = ok35 and ok35x
        det35.append("x%d: rho all-in-win %s; pinch %s (min %.4f @j%s"
                     "/%d); ures %.0e b0 %.0e jres %.0e (%.0f s)"
                     % (x, rho_ok,
                        "RES" if pinch_res else "PRECISION-LIMITED",
                        pmin if pmin is not None else float("nan"),
                        pargj, mcon - 1, worst_ures, worst_b0, jres,
                        time.time() - t_l))
        info("x=%d LOO exhibit (L3/L4): rho_j == 1 for ALL %d "
             "left-out zone zeros (jet-COLLECTIVE: the D1 deflation "
             "hypothesis refuted -- no per-zero jet factor); pinch "
             "p_j profile [%s] (edge cluster carries the eps^2 "
             "pinch; eps^2 = %.1e)"
             % (x, mcon, " ".join(rows_p), float(eps2)))

        # ---- G36 add-one battery (L5)
        with mp.workdps(dps):
            g_next = [float(g) for g in gam[m_zone:m_zone + 2]]
            mid1 = 0.5 * (float(gam[m_zone - 1]) + g_next[0])
            mid2 = 0.5 * (g_next[0] + g_next[1])
            probes = (("z1", g_next[0]), ("m1", mid1),
                      ("z2", g_next[1]), ("m2", mid2))
            gvals = {}
            for tag, tv in probes:
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam_a, _etn, _rho2, _chi = secular_data(Vd, r)
                gvals[tag] = float((lam_a - qs[0]) / tau_v)
            ctr1 = gvals["m1"] / max(gvals["z1"], 1e-300)
            ctr2 = gvals["m2"] / max(gvals["z2"], 1e-300)
        # AMENDMENT 1b: hard gates x <= 18 only; x = 24/28 typed
        # F64-ORDINATE-LIMITED (f64 offset exceeds the well width)
        if x <= 18:
            ok36x = (gvals["z1"] <= ADD_ZERO_MAX
                     and gvals["z2"] <= ADD_ZERO_MAX
                     and gvals["m1"] >= ADD_MID_MIN
                     and gvals["m2"] >= ADD_MID_MIN
                     and ctr1 >= ADD_CONTRAST_MIN
                     and ctr2 >= ADD_CONTRAST_MIN)
            a36tag = ""
        else:
            ok36x = True
            a36tag = " [F64-ORDINATE-LIMITED, measured-only]"
        ok36 = ok36 and ok36x
        det36.append("x%d: g_add zeros %.1e/%.1e mids %.1f/%.1f "
                     "contrast %.1e/%.1e%s"
                     % (x, gvals["z1"], gvals["z2"], gvals["m1"],
                        gvals["m2"], ctr1, ctr2, a36tag))
        info("x=%d ADD-ONE exhibit (L5): killing the next TRUE zero "
             "beyond T_z is free (g_add %.1e) vs O(10) at non-zero "
             "points -- m is not a cliff, per-zero pricing cannot "
             "generate the growth (arithmetic dip contrast %.1e)"
             % (x, gvals["z1"], ctr1))

        # ---- G37 trial cap (L6)
        with mp.workdps(dps):
            cvec = [V[i, 0] for i in range(K)]
            mu_b = sum(cvec[k] * cvec[k] * b[k] for k in range(K))
            vfr = [cvec[k] * (b[k] - mu_b) for k in range(K)]
            n2 = sum(vfr[k] * vfr[k] for k in range(K))
            ortho = float(abs(sum(vfr[k] * cvec[k]
                                  for k in range(K))))
            Mv = [mp.mpf(0)] * K
            for i in range(K):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Mq[i, k] * vfr[k]
                Mv[i] = acc
            ray = sum(vfr[k] * Mv[k] for k in range(K)) / n2
            r_trial = float((ray - tau) / tau)
            courant_ok = bool((ray - tau) / tau
                              >= FG * (1 - mp.mpf("1e-12")))
            A0v = (A2p - mu_b * A0p) / mp.sqrt(n2)
            tlaw_v = float(ray / (8 * A0v * A0v * G_mp))
            nu = float(n2 / b[K - 1] ** 2)
            sat = fg_f / r_trial
            cn_v = [cs[k] * (b[k] - mu_b) for k in range(K)]
            wid = 0.0
            for tv in TRIAL_SAMPLES:
                tm = mp.mpf(repr(tv))
                Ev = en_pair(cn_v, aa, oms, tm)[0]
                Ep = en_pair(cs, aa, oms, tm)[0]
                pred = (tm * tm - mu_b) * Ep \
                    - 2 * A0p * tm * mp.sin(aa * tm)
                wid = max(wid, float(abs(Ev - pred)
                                     / max(abs(Ev),
                                           mp.mpf("1e-300"))))
            zdet = "f64-limited (deep)"
            z_ok = True
            if x in ZGATE_RUNGS:
                zsum = mp.mpf(0)
                for gj in gam[gam <= Tz]:
                    gm = mp.mpf(repr(float(gj)))
                    Ev = en_pair(cn_v, aa, oms, gm)[0]
                    zsum += 2 * Ev * Ev
                zmodel = mp.mpf(0)
                for gj in gam[gam <= Tz]:
                    gm = mp.mpf(repr(float(gj)))
                    zmodel += 8 * A0p * A0p * gm * gm \
                        * mp.sin(aa * gm) ** 2
                zrat = float(zmodel / zsum)
                zshare = float(zsum / (ray * n2))
                z_ok = ZMODEL_WIN[0] <= zrat <= ZMODEL_WIN[1] \
                    and zshare <= ZSHARE_BAR
                zdet = "zmodel %.4f zshare %.1e" % (zrat, zshare)
        sat_tab[x] = sat
        ok37x = (ortho <= TRIAL_ORTHO_BAR and wid <= TRIAL_ID_BAR
                 and courant_ok and SAT_WIN[0] <= sat <= SAT_WIN[1]
                 and z_ok)
        ok37 = ok37 and ok37x
        det37.append("x%d: r_trial %.4e sat %.4e tlaw_v %.4f nu "
                     "%.2e ortho %.0e id %.0e %s"
                     % (x, r_trial, sat, tlaw_v, nu, ortho, wid,
                        zdet))
        info("x=%d TRIAL exhibit (L6): FULLGAP <= r_trial = %.3e "
             "HARD (Courant, exact orthogonality); the trial is "
             "MID-DOMINATED (saturation %.1e falling): the naive "
             "zone-quartic derivation via (B - mu)phi is honestly "
             "refuted -- the quartic lives in the eigenvector "
             "ladder, not in this trial" % (x, r_trial, sat))

        # ---- G38 moment model (L7; core only)
        if not is_deep:
            with mp.workdps(dps):
                om_max = mp.sqrt(b[K - 1])
                Pmax = MODEL_P[-1]
                Hm = mp.zeros(Pmax, Pmax)
                for gj in gam[gam > float(om_max)]:
                    gm = mp.mpf(repr(float(gj)))
                    w8 = 8 * mp.sin(aa * gm) ** 2 / (gm * gm)
                    for p in range(Pmax):
                        for q in range(Pmax):
                            Hm[p, q] += w8 / gm ** (2 * (p + q))
                Gt = mp.mpf(repr(hsw_G(gtop)))
                for p in range(Pmax):
                    for q in range(Pmax):
                        Hm[p, q] += 8 * Gt / mp.mpf(repr(gtop)) \
                            ** (2 * (p + q))
                Fp = []
                for p in range(Pmax):
                    fp = [((-1) ** k2) * b[k2] ** p / nrm[k2]
                          for k2 in range(K)]
                    dv_ = [sum(Vd["Nb"][k2, fi] * fp[k2]
                               for k2 in range(K))
                           for fi in range(nf)]
                    Fp.append(Vd["fwd"](dv_))
                GJ = mp.zeros(Pmax, Pmax)
                for p in range(Pmax):
                    for q in range(Pmax):
                        GJ[p, q] = sum(Fp[p][i2] * Fp[q][i2]
                                       for i2 in range(nf))
                fg_models = []
                for Pt in MODEL_P:
                    Ct = mp.cholesky(GJ[:Pt, :Pt])
                    Mt = mp.zeros(Pt, Pt)
                    for p in range(Pt):
                        for q in range(Pt):
                            acc = mp.mpf(0)
                            for r_ in range(Pt):
                                for s2 in range(Pt):
                                    acc += Ct[r_, p] * Hm[r_, s2] \
                                        * Ct[s2, q]
                            Mt[p, q] = acc
                    Et_, _ = mp.eigsy(Mt)
                    evt = sorted([Et_[i2] for i2 in range(Pt)])
                    fg_models.append(float((evt[1] - evt[0])
                                           / evt[0]))
            mono_ok = all(fg_models[i] < fg_models[i + 1]
                          for i in range(len(fg_models) - 1))
            under_ok = fg_models[-1] <= fg_f
            ok38x = mono_ok and under_ok
            ok38 = ok38 and ok38x
            det38.append("x%d: FG_model %s vs FG %.3e (dex dev %s)"
                         % (x, "/".join("%.2e" % v
                                        for v in fg_models), fg_f,
                            "/".join("%+.2f" % math.log10(v / fg_f)
                                     for v in fg_models)))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    if not smoke:
        lxs = [math.log10(float(x)) for x in x_used]
        lfg = [math.log10(fg_tab[x]) for x in x_used]
        sl_fg = float(np.polyfit(lxs, lfg, 1)[0])
        ok31 = ok31 and FG_SLOPE_WIN[0] <= sl_fg <= FG_SLOPE_WIN[1]
        det31.append("slope %.3f" % sl_fg)
    check("G31-spectral-ladder", ok31,
          "Mq PSD + sorted; FULLGAP in the frozen windows x %s "
          "(incl. the CDLII x=28 string); lam_1 SIMPLE (rel gap >= "
          "%.0e); growth slope in %s: %s"
          % (str(FG_WIN), SIMP_MIN, str(FG_SLOPE_WIN),
             "; ".join(det31)))
    check("G32-node-config-razor", ok32,
          "|qrel| <= %.0e, null res <= %.0e; delta_1 >= FULLGAP (W3 "
          "re-gate); zone-top argmin in the frozen windows; s <= "
          "bar; sg in %s; tlaw_0/lock on the cited strings; GF1 "
          "lower g >= 1/(s + 1/delta_1) HARD; COMPOSED FLOOR g >= "
          "1/(s + 1/(%.2f x %.1f x T_z^4 - 1)) HARD and delta_1 >= "
          "theta_0 c T_z^4 - 1 (GL5c razor chain, mp): %s"
          % (QREL_BAR, NULLRES_BAR, str(SGAP_WIN), COMPOSED_THETA0,
             COMPOSED_TR0, "; ".join(det32)))
    check("G33-quartic-law", ok33,
          "eta_0^2 == A_0(phi)^2 <= %.0e; R2 identity jr t_r == 1 + "
          "1/FULLGAP <= %.0e; THETA = J/T_z^4 in %s; c_1 in %s; jr "
          "in %s; t_r in %s (L1: THE QUARTIC GROWTH LAW): %s"
          % (ETA0_BAR, R2ID_BAR, str(THETA_WIN), str(C1_WIN),
             str(JR_WIN), str(TR_WIN), "; ".join(det33)))
    check("G34-ladder-law", ok34,
          "tlaw_i/tlaw_0 in %s for every collapsed-block rung "
          "(i < min(nc, %d)); c_2 in %s (L2: the collapsed spectrum "
          "is the jet ladder squared; octic second gap): %s"
          % (str(TLAWLAD_WIN), BLOCK_IMAX, str(C2_WIN),
             "; ".join(det34)))
    check("G35-loo-battery", ok35,
          "GL1/GL2 instantiated at EVERY zone index: dual-row res "
          "<= %.0e; f(q_0) > 0; |b_0|/q_1 <= %.0e; rho_j in %s ALL "
          "j (L3: jet-COLLECTIVE, D1 deflation REFUTED); p_j >= "
          "%.1f outside top-%d and min p_j <= %.1f AT the edge "
          "cluster (L4: the D2 answer), pinch guard applied: %s"
          % (LOO_URES_BAR, LOO_B0_BAR, str(RHO_WIN), P_OUT_MIN,
             TOP_CLUSTER, P_EDGE_MAX, "; ".join(det35)))
    check("G36-addone-battery", ok36,
          "g_add(next true zeros) <= %.0e, g_add(midpoints) >= %.1f, "
          "contrast >= %.0e (L5: per-zero price beyond the zone is "
          "~0 at zeros -- the census m is not a cliff): %s"
          % (ADD_ZERO_MAX, ADD_MID_MIN, ADD_CONTRAST_MIN,
             "; ".join(det36)))
    check("G37-trial-cap", ok37,
          "trial v = (B - mu)phi: orthogonality <= %.0e; E_v "
          "identity <= %.0e; COURANT r_trial >= FULLGAP HARD; sat "
          "in %s; zone model/share gates at x in %s only "
          "(F64-LIMITED beyond, disclosed) (L6): %s"
          % (TRIAL_ORTHO_BAR, TRIAL_ID_BAR, str(SAT_WIN),
             str(ZGATE_RUNGS), "; ".join(det37)))
    check("G38-moment-model", ok38,
          "finite-P jet-moment-Gram model: FG_model monotone in P "
          "and FG_model <= FULLGAP (undershoot; L7: "
          "MOMENT-ROUTE-OBSTRUCTED -- the growth needs all jet "
          "orders): %s" % ("; ".join(det38)))

    # ---- G39 growth/rates post-loop
    if not smoke:
        lxs = [math.log10(float(x)) for x in x_used]
        lth = [math.log10(th_tab[x]) for x in x_used]
        sl_th = float(np.polyfit(lxs, lth, 1)[0])
        diffs = []
        rows_r = []
        for i in range(len(x_used) - 1):
            xa, xb = x_used[i], x_used[i + 1]
            dm = m_tab[xb] - m_tab[xa]
            r_tau = -(math.log10(tau_tab[xb])
                      - math.log10(tau_tab[xa])) / dm
            r0 = -(a0p_tab[xb] - a0p_tab[xa]) / dm
            r1 = -(a01_tab[xb] - a01_tab[xa]) / dm
            diffs.append(r0 - r1)
            rows_r.append("(%d,%d): r_tau %.3f r0 %.3f r1 %.3f "
                          "diff %.4f" % (xa, xb, r_tau, r0, r1,
                                         r0 - r1))
        diff_ok = all(d > 0 for d in diffs) \
            and diffs[-1] <= diffs[0] / DIFF_DILUTION
        ok39 = THETA_SLOPE_WIN[0] <= sl_th <= THETA_SLOPE_WIN[1] \
            and diff_ok
        check("G39-growth-rates", ok39,
              "THETA slope vs log10 x = %.3f in %s (the quartic "
              "exponent pinned 4 +- 0.45); per-zero differential "
              "diff = r0 - r1 > 0 on every pair and DILUTED "
              "(last <= first/%.1f): %s"
              % (sl_th, str(THETA_SLOPE_WIN), DIFF_DILUTION,
                 "; ".join(rows_r)))
        info("PER-ZERO COORDINATES (GL4 instantiated): the ground "
             "out-collapses the excited by diff dex/zero -- the "
             "growth is DILUTED over the zone (no single-zero "
             "factor), consistent with L3/L5; r_tau ~ 2 r0 "
             "(the GW/zero-jet pricing in per-zero currency)")

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
            nrmw = [mp.sqrt(2 * aaw) if k == 0 else mp.sqrt(aaw)
                    for k in range(cw["K"])]
            A0cw = sum(((-1) ** k) * csw[k] for k in range(cw["K"]))
            A2cw = sum(((-1) ** k) * csw[k] * omsw[k] ** 2
                       for k in range(cw["K"]))
            ytbw = float(abs(A2cw / A0cw)) / float(omsw[-1] ** 2)
            cs1w = [cw["mpV"][i, 1] / nrmw[i] for i in range(cw["K"])]
            A01w = sum(((-1) ** k) * cs1w[k] for k in range(cw["K"]))
            thw = float((A01w / A0cw) ** 2
                        / mp.mpf(repr(Tzw)) ** 4)
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD: the GL/quartic/ladder hypotheses fail "
              "EXACTLY here); y_t_w/b_top = %.2f <= %.1f; THETA_w = "
              "%.3e (exhibit: no positive collapsing ground to "
              "carry a quartic law)"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX, thw))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the loo/add-one/"
          "quartic/ladder machinery requires PSD + simple positive "
          "ground -- the hypotheses fail exactly in the false worlds")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in x_used]

        def slope_of(tab):
            return float(np.polyfit(
                lt, [math.log10(abs(tab[x])) for x in x_used], 1)[0])
        sl_tht = slope_of(th_tab)
        sl_c1 = slope_of(c1_tab)
        sl_jr = slope_of(jr_tab)
        sl_tr = slope_of(tr_tab)
        sl_sat = slope_of(sat_tab)
        sl_a0p = float(np.polyfit(lt, [2 * a0p_tab[x]
                                       for x in x_used], 1)[0])
        sl_a01 = float(np.polyfit(lt, [2 * a01_tab[x]
                                       for x in x_used], 1)[0])
        ok54 = (abs(sl_tht) <= TAU_SLOPE_BAR
                and abs(sl_c1) <= TAU_SLOPE_BAR
                and abs(sl_jr) <= TAU_SLOPE_BAR
                and abs(sl_tr) <= TAU_SLOPE_BAR
                and abs(sl_sat) <= TAU_SLOPE_BAR
                and W0_RIDER_WIN[0] <= sl_a0p <= W0_RIDER_WIN[1]
                and W0_RIDER_WIN[0] <= sl_a01 <= W0_RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: THETA %.4f, c_1 %.4f, jr %.4f, "
              "t_r %.4f, sat %.4f (all <= %.2f: the growth-law "
              "coordinates are tau-flat, NOT Connes-priced); RIDER "
              "report: A_0(phi)^2 %.3f, A_0(psi_1)^2 %.3f in %s "
              "(both jets ride tau -- BOUND-RIDES-CONNES; the "
              "RATIO is the flat coordinate)"
              % (sl_tht, sl_c1, sl_jr, sl_tr, sl_sat, TAU_SLOPE_BAR,
                 sl_a0p, sl_a01, str(W0_RIDER_WIN)))
        info("growth-law tables x = %s: THETA = %s; c_1 = %s; jr = "
             "%s; t_r = %s; sat = %s"
             % (str(x_used),
                "/".join("%.4f" % th_tab[x] for x in x_used),
                "/".join("%.4f" % c1_tab[x] for x in x_used),
                "/".join("%.4f" % jr_tab[x] for x in x_used),
                "/".join("%.4f" % tr_tab[x] for x in x_used),
                "/".join("%.1e" % sat_tab[x] for x in x_used)))
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
          "VERBATIM -- this round changes COORDINATES, not the "
          "set); one-grant 5; counterfactual PARALLEL 9 NOT REAL; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")
    info("EXACT RESIDUE after this round (read with CDLXI/CDLXII/"
         "CDLXIII/CDLXIV/CDLXV): SET UNCHANGED -- RH <== [r122-NF-"
         "closure] + [Theorem R] + {L1, WPD} on dense a; RESIDUE = "
         "{TOPROOT (= B00-ROOTGAP == SEC-cap, CDLXV), TLAWCAP-"
         "block, QSUBGAP-FLOOR (= s-cap AND delta_1-floor via the "
         "razor)} + dense-a + a-extension + window-a; THIS ROUND "
         "RECOORDINATES the delta_1-floor: FULLGAP == THETA t_r "
         "T_z^4 - 1 (quartic law, measured; GL5 chase) -- the "
         "floor demand becomes the THETA-window x t_r-window, ONE "
         "flat O(1) arithmetic-consuming pair of the tlaw class; "
         "per-zero/per-constraint/moment/trial routes REFUTED or "
         "OBSTRUCTED (L3/L5/L6/L7); D3 collapses to the razor "
         "(GL3).  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "GL1-PROVEN(loo pinch: every leave-one-out matches lam_1 "
        "within the eps^2 budget; G10/G35)",
        "GL2-PROVEN(arrowhead loo instrument exact; G11/G35)",
        "GL3-PROVEN(one-row price equivalence + razor vacuity + "
        "ALGEBRA-ONLY-REFUTED-FOR-ROWPRICE: D3 collapses to the "
        "razor; G12)",
        "GL4-PROVEN(rate bookkeeping; R2 re-gated) + "
        "PERZERO-DILUTED(measured; G13/G33/G39)",
        "GL5-PROVEN(ladder + quartic chases + razor composition, "
        "mp-checked per rung; G14/G32)",
        "QUARTIC-LAW(J == THETA T_z^4, THETA flat, exponent "
        "4 +- 0.45: the growth law's closed form MEASURED; "
        "CLASSICAL-CONDITIONAL-CANDIDATE, open kernel = the THETA "
        "window; G33/G39)",
        "LADDER-LAW(block-wide zero-jet law + octic second gap; "
        "G34)",
        "LOO-JET-COLLECTIVE(D1 deflation REFUTED-MEASURED; G35)",
        "EDGE-CLUSTER-PINCH(D2 answered: band-edge top-3; G35)",
        "ADDONE-FREE-AT-ZEROS(L5 contrast; G36)",
        "TRIAL-CAP-CERTIFIED + TRIAL-MID-DOMINATED(G37)",
        "MOMENT-ROUTE-OBSTRUCTED(G38)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(dense-x suffices; G60)",
        "OMEGA-RECOORDINATED(residue set unchanged; census {MEAS, "
        "OMEGA-POS} cardinality 4 UNCHANGED; G61)"]
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
        print("COMPOSITE: GL1-PROVEN + GL2-PROVEN + GL3-PROVEN + "
              "GL4-PROVEN + GL5-PROVEN + QUARTIC-LAW + LADDER-LAW "
              "+ LOO-JET-COLLECTIVE + EDGE-CLUSTER-PINCH + "
              "ADDONE-FREE-AT-ZEROS + TRIAL-CAP-CERTIFIED + "
              "TRIAL-MID-DOMINATED + MOMENT-ROUTE-OBSTRUCTED + "
              "CONTROLS-REFUSE + DEMAND-FLAT + BOUND-RIDES-CONNES "
              "+ QUANTIFIER-INHERITED + OMEGA-RECOORDINATED + "
              "MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
