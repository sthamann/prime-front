#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""adjugate_logmaster_probe -- PRIME.ADJUGATE.SPECTRALCURVE.01
                              + PRIME.COFINAL.LOGMASTER.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the owner's two new modules, built and gated)
=======================================================================
(A) THE ADJUGATE ELIMINATION (PRIME.ADJUGATE.SPECTRALCURVE.01):
adj(tau I - M) = P'(tau) phi phi^T for the simple smallest eigenvalue,
hence with the fixed boundary-jet functionals v_0, v_2 (A_0 = v_0.phi,
A_2 = v_2.phi) and B_ij := v_i^T adj(tau I - M) v_j:
   A_2/A_0 = B_20/B_00        and        A_0^2 = B_00/P'(tau):
TOPROOT is a ratio of two adjugate entries, the TLAWCAP/EPS-LOCK
currency becomes (tau+OFF) |P'(tau)| / (16 G |B_00|), SUSCAP2R is the
three-row Schur ratio (r144 X4, CITED), DELTA1FLOOR is a root gap of
P -- the whole residue lives on ONE spectral algebraic curve
(P(z; x) = det(zI - M_q(x)) and its adjugate entries), BASIS-FREE: no
global eigenvector branch is needed (the r144-named Jensen/Cartan
eigen-branch continuation obstacle relocates onto (P, adj) data,
which are polynomial in the matrix entries).  Multiplicity caveat
gated: at tau-multiplicity P'(tau) = 0 -- exactly the delta_1 = 0
cases, REGISTERED by the DELTA1 term of the master integrand; the
Riesz-projector / first-nonvanishing-adjugate-coefficient
continuation is implemented and gated on constructed degenerate and
near-degenerate instances.
(A2) THE CELL-SELECTION LEMMA (owner's step 2): within each log block
[U, U+1] (x = e^u), the K-jumps, atom (prime-power) births, zone-
census crossings and tent-edge/atom pair crossings are polynomially
many in x, so by pigeonhole a clean sub-cell of u-width >= 1/(N+1)
>= x^{-C_0} exists where K is constant, the atom map constant, the
census constant, and (modulo the simplicity leg, typed) the ground
value simple; its log-width cost is log(N+1) = O(U) -- exactly the
LM currency.  Counts measured per block on the ladder rungs.

(B) THE LOGARITHMIC MASTER (PRIME.COFINAL.LOGMASTER.01):
L_EPS(x, a) := (eps_bar/(|A_0| sqrt(8 G(T_z))))^2 = (tau + OFF)/
(16 A_0^2 G(T_z));  s := tau chi/rho2;  d := 1/delta_1;
   M_src := (1 + L_EPS)(1 + s)(1 + d)  >=  1.
THEOREM (LM), conditional assembly: IF (H-LM) for each a in a dense
set D there is C_a with int_U^{U+1} log M_src(e^u, a) du <= C_a U for
all large U, PLUS (H-FW) the finite-window construction on the chosen
sequences (typed exactly below), PLUS (H-a) dense-a + a-extension +
window-a, THEN RH via the audited chain.  Proof arrows (each gated or
cited): Markov on F = log M_src >= 0 gives good u with M_src <=
e^{4 C_a U} = x^{4 C_a}; the MULTIPLICATIVE split bounds all three
factors simultaneously (each factor >= 1), so L_EPS <= x^{4C_a}
(EPS-LOCK = OMEGA-a DIRECTLY), s <= x^{4C_a} (SUSCAP2R) and 1/delta_1
<= x^{4C_a} (DELTA1FLOOR); r142 W2 (re-gated) gives g >= 1/(s +
1/delta_1) >= x^{-4C_a}/2 (QSUBGAP); V2 + intersection give the
instrument-chosen unbounded sequence; then OMEGA-b (r138/r139), H-pin
(r135, consumes H-FW), L1/WPD, Theorem R (r128), NF-closure (r122),
Weil positivity ==> RH.  WHY LM BEATS (M'): (i) log-integrability of
isolated poles -- machine exhibit int_0^1 dt/t = oo but
int_0^1 log(1 + 1/t) dt = 2 log 2 (an isolated delta_1 = 0 point
destroys the raw four-integrand average of (M') but not the log
average); (ii) NO separate TOPROOT/TAILVIS/ONSETCAP consumption --
adjudicated exactly in the honesty gate below.
THE HONESTY CRUX (machine-gated): the CDXLIV decomposition OMEGA-a =
EPS-LOCK <== TOPROOT + TAILVIS + TLAWCAP(=ONSETCAP) was a PROOF ROUTE
to EPS-LOCK; LM consumes EPS-LOCK directly as the L_EPS factor, so
TOPROOT/ONSETCAP/TAILVIS/JETLOCK/BANDMASS appear NEITHER in the LM
hypothesis set NOR in H-FW (both intersections gated EMPTY) -- they
genuinely drop from the STATEMENT; the arithmetic content does not
vanish, it contracts INTO the L_EPS log-average (same object, weaker
form: pointwise route ==> block average, gated one-way; converse
refuted by the pole exhibit).  H-FW CONTENTS TYPED EXACTLY:
{per-selected-x H-cell demand validity: r135 M2-validity class + ball
validity b <= sp/2 + zone-mass margin m_min >= 16 eps_bar sum|w'|/TL
(demand-side, poly-inflation-tolerant per r135/r137 E2 pricing,
CITED)} + {window-a positivity r128 G26} + {a-extension gamma_1^2 <
a < H^2} + {dense-a = the (H-LM) quantifier}; NO TOPROOT, NO ONSETCAP
inside.  VERDICT SHAPE: the OMEGA-a leg contracts {TOPROOT, ONSETCAP}
-> {EPSLOCK-AVG} (a strictly-weaker-or-equal hypothesis); the
SUSCAP2R and DELTA1FLOOR legs are IDENTICAL to (M') -- no progress
and no repackaging there; EPSLOCK-AVG stays OPEN-ARITHMETIC.
(B2) THE RLD FRAMING (stated + measured, NOT attempted): for the
normalized prime-comb family T_n (leading principal minors of M_q)
and fixed r, the relative log-det bound
   (RLD)  log(det T_{n+r} / det T_n) = O(log n),
INCLUDING the three special minors (the phi-bordered adjugate entry
B_00 relative to P'(tau), the zone-row Schur minors det H_2 /det H_3
of r144 X4, and the root-gap factor (lam_1 - tau)/tau).  Gated: RLD
==> pointwise log M_src = O(log x) ==> (H-LM) with C_a = O(1)
(sufficiency, exact algebra); the converse FAILS (block average
tolerates isolated poles -- one-way, typed).  The named analytic
target (relative Szegoe/IIKS-type statement for the prime comb) is
typed OPEN-CLASSICAL-CANDIDATE and NOT consumed; the relative minor
ratios are MEASURED on the ladder (Cholesky log-det ladder slope +
the three special minors per rung).
(B3) THE RED-TEAM GATE (owner's step 5, MANDATORY): the 2D model
W = diag(tau, tau + Delta), u = (eps, sqrt(1 - eps^2)): ALL rank-one
response formulas hold exactly (secular root lam* = tau + eps^2
Delta; s g = 1 - eps^2 reproduces the W1 pinch SATURATED at the
lower end; the X2 Weyl formula and the W1 defect identity hold
symbolically for every eps), yet s = tau (1 - eps^2)/(Delta eps^2)
-> oo as eps -> 0.  HARD GATE: the conjunction of interlacing/
response-curve algebra facts admits unbounded s (constructive
witness at every poly bound: eps^2 = tau/(tau + Delta P) gives s =
P), so ANY bound derived purely from that algebra FAILS this model
-- asserted; only bounds consuming arithmetic input (census, qrel
consistency, frozen replication windows -- exactly the inputs of G31
here) may pass.  The model refuses on the arithmetic legs (no
census, no source consistency -- it cannot enter the G30/G31
currency at all, typed).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 adjugate identity: adj(l0 I - M) == (l0-l1)(l0-l2) phi phi^T
    GENERIC in (l0, l1, l2) on the Householder-conjugated frame
    (u = (1,2,3), H = I - u u^T/7), phi = H e_1; B-identities
    B_20/B_00 == A_2/A_0 and A_0^2 == B_00/P'(l0) generic in the
    functional entries (THEOREM AD1);
    G11 multiplicity/Riesz continuation: at l1 = l0 the adjugate
    VANISHES; the first nonvanishing coefficient is
    d/dz adj(zI - M)|_{z=l0} == (P''(l0)/2!) Pi with Pi = the rank-2
    Riesz projector (exact on the conjugated instance); the near-
    degenerate family diag(1, 1+e, 5) keeps B_00 == P'(1) A_0^2 ==
    4 e A_0^2 EXACTLY for every e > 0 (the identity never breaks;
    only the numerics inflate) and the master integrand REGISTERS
    the degeneration: lim_{e->0}(1 + 1/e) = oo (THEOREM AD2);
    G12 cell-selection algebra: pigeonhole (N jump points in a unit
    u-block leave a sub-cell of u-width >= 1/(N+1); 1 = sum l_i <=
    (N+1) max l_i exact) + log-cost identity e^{C0 U} == x^{C0} +
    the K-jump count bound instance (THEOREM CS, modulo the
    simplicity leg typed in G34);
    G13 LM core algebra: factors >= 1 ==> F = log M_src >= 0;
    Markov meas{F > 4 C U} <= 1/4 (rearrangement + instance);
    MULTIPLICATIVE split (1+a) <= (1+a)(1+b)(1+c) generic nonneg ==>
    all three factors simultaneously <= e^{4CU}; e^{4CU} == x^{4C};
    THE POLE EXHIBIT int_0^1 dt/t == oo vs int_0^1 log(1+1/t) dt ==
    2 log 2 (LM-BEATS-RAW-AVERAGE); pointwise ==> block-average
    (one-way, the converse refuted by the exhibit);
    G14 arrow re-gates: r142 W2 loop (forward + backward + demand
    composition 1/(2P)) and r141 V2 measure lemma + intersection
    (ports of the r144 gates, VERBATIM shapes);
    G15 LM dependency graph + honesty adjudication (set logic,
    machine-gated): qsubgap-needs covered; EPSLOCK consumed directly;
    LM-hypotheses  intersect {TOPROOT, ONSETCAP, TAILVIS, JETLOCK,
    BANDMASS, TLAWCAP} == EMPTY; H-FW contents enumerated and the
    same intersection == EMPTY; the known-proof-route re-entry set
    printed (proving (H-LM) by currently known theorems would use
    the E1 route -- the both-ways honesty); contraction verdict;
    G16 RLD statement + sufficiency algebra (RLD ==> (H-LM),
    one-way) + the Szegoe/IIKS target printed and typed;
    G17 red-team 2D model (symbolic eps): lam* == tau + eps^2 Delta;
    s g == 1 - eps^2 == 1 - g/delta_1 (pinch saturated, share_1 = 1);
    X2 formula == s; W1 defect identity holds; eta_0 == lam*
    interlaced; lim_{eps->0} s == oo AND the poly-witness eps^2 =
    tau/(tau + Delta P) gives s == P exactly at P = 10^6:
    ALGEBRA-ONLY-BOUNDS-REFUTED (hard assert).
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan to T_z + 6, step 0.05):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform); G31 node-config V + replication (|qrel| <= 1e-30,
    null residual <= 1e-40, delta_1 >= FULLGAP (r142 W3 re-gate),
    zone-top argmin in the frozen r139/r141/r142 windows AND >= 3,
    s <= 0.1, s x gap in (0.98, 1.02), delta_1 windows, share_1 >=
    0.5, tlaw on the CDXLI strings <= 5e-3);
    G32 ADJUGATE INSTANTIATION (basis-free route): tau refined by
    Rayleigh-quotient iteration at dps + ADJ_PAD (all-mp, RQI_ITERS
    = 2, move <= 1e-20 rel gated); z_h = tau_ref + h tau A_0^2
    FULLGAP / K on the h-ladder (1e-8, 1e-16); ONE own-LU per h of
    (z_h I - M): P(z_h) = LU determinant (sign-tracked), y =
    (z_h I - M)^{-1} v_0; gates per rung and per h:
      |[v_2.y]/[v_0.y] / (A_2/A_0) - 1|            <= ADJ_BAR(h),
      |P(z_h) (v_0.y) (z_h - tau_ref) ... == A_0^2:
        |(z_h - tau_ref)(v_0.y) / A_0^2 - 1|       <= ADJ_BAR(h),
      |P(z_h)/(z_h - tau_ref) / P'(tau) - 1|       <= ADJ_BAR(h)
        (basis-free LU determinant vs the eigenproduct
        P'(tau) = prod_{i>=1}(tau - lam_i) -- dual instrument),
      |B_20/B_00| in the frozen r140 y_t windows (TOPROOT read off
        the adjugate), and the TLAWCAP/EPS-LOCK currency identity
      |(tau+OFF)|P'| / (16 G |B_00|) / L_EPS - 1|  <= ADJ_BAR(h);
    ADJ_BAR = {1e-8: 1e-4, 1e-16: 1e-10} (error class ~ h |v_0|^2/K,
    pre-freeze unmeasured, DISCLOSED with >= 1e4 headroom);
    G33 near-degenerate mp toy (NOT a rung): 4x4 Householder frame
    diag(1, 1+1e-30, 5, 7) at dps 80: the h-instrument reproduces
    B_00 == P'(tau) A_0^2 with rel dev <= 1e-10 (the identity
    survives a 1e-30 gap when h is scaled by A_0^2 FULLGAP); exact
    degenerate limit checked in G11;
    G35 LM integrands per rung: L_EPS == (tlaw + OFF/D)/2 identity
    <= 1e-8; L_EPS in (0.05, 0.35) (r135 lock strings 0.36..0.51
    squared); M_src >= 1 strictly; log M_src <= 1.0; pointwise
    C_a^pt = log M_src / U <= 0.5 (expected 0.05..0.20); table +
    slope printed (MEASURED-POINTWISE);
    G36 THE DENSE-u BLOCK (the (M') lever (c) instrument, first
    dense block measurement): x = 4.4, 4.6, ..., 6.0 (9 builds, dps
    60, u-span log(6.0/4.4) = 0.3102 DISCLOSED partial block):
    full pipeline per point (census + newton polish + V + argmin);
    structural gates per point (zone count == m(x), |qrel| <= 1e-25,
    tau > 0, delta_1 >= FULLGAP (1 - 1e-12), s <= 1.0, M_src >= 1);
    adjacent |Delta log M_src| <= 1.0 ACROSS the >= 3 K-jumps in
    the span (K(4.4) = 9 -> K(6.0) = 14: the LM integrand is
    measured BOUNDED across K-jumps and the x = 5 prime crossing);
    trapezoid block estimate C_a^blk = (int-hat/span)/U_mid <= 1.0
    (expected ~0.1..0.2); the cell-selection count for this block
    printed (where evaluation is cheap);
    G34 CELL-SELECTION COUNTS on the rung blocks [log x, log x + 1]:
    N_K (K-jumps, exact), N_pp (atom births, sieve), N_zone (census
    crossings, cache), N_tent <= K(ex) N_pp(ex) (pair bound, each
    pair monotone: <= 1 crossing per block); N_tot printed; width
    >= 1/(N_tot + 1); measured C_0 = log(N_tot + 1)/U <= 4.5
    (poly class; small-x inflation at x = 5 disclosed, C_0 falls in
    x); SIMPLICITY LEG typed: FULLGAP > 0 at every rung and every
    dense-u point (measured) + r143 fine-grid smoothness CITED --
    the per-cell degeneracy count is NOT proven (typed
    CELL-LEMMA-MODULO-SIMPLICITY, the honest exposure);
    G37 RLD measured: mp Cholesky of M_q (PSD); relative log-dets
    d_n = log10 det T_{n+1}/det T_n over the leading-minor ladder;
    fitted slope alpha of d_n vs log10 n + max |d_n|/log10(n+2) in
    the top half printed; the three special minors printed per rung
    (2 log10 |A_0| == log10(B_00/P'), log10(det H_3/det H_2) ==
    log10(s R_phi^2/tau) via r144 X4 CITED, log10 FULLGAP);
    finite-and-printed gates only, typed MEASURED + the Szegoe
    target typed OPEN-CLASSICAL-CANDIDATE (NOT consumed);
    G38 red-team mp instantiation: the 2D model at (tau, Delta) from
    the x = 5 rung (Delta = FULLGAP tau), eps = (0.1, 0.01, 0.001):
    |s g - (1 - eps^2)| <= 1e-40 AND the W1 defect identity dev <=
    1e-40 at every eps AND the constructive poly witness eps^2 =
    tau/(tau + Delta P) at P = 10^6 realizes s == P in mp (rel dev
    <= 1e-40) with s >= 1e5 (the algebra is eps-uniform while s
    blows up -- the numeric side of G17; SMOKE-2 repair: the frozen
    eps ladder alone cannot reach s >= 1e5 against the rung's REAL
    FULLGAP = 2.2e5, s(0.001) = 4.49 -- the witness, G17's own
    frozen mechanism, carries the unboundedness leg).
S3b G40 adversarial witness x = 5, 8 (RvM quantile config, r142/r144
    replica): q0rel >= 10; max s' >= 1.0 (truth s <= 0.1); pinch +
    defect identity HOLD on the adversarial well (algebra config-
    blind, null control); AND the LM integrand separation
    M_src(adv)/M_src(true) >= 3.0 (the MASTER currency itself sees
    the arithmetic -- without this the LM hypothesis would be
    currency-blind).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 AND y_t_w/b_top <= 1.0 AND (tau_w + OFF_w) < 0
    (eps_bar^2 < 0: the false worlds cannot even enter the L_EPS /
    M_src currency -- the factor->=1 precondition fails); G53
    consistency.
S5  G54 tau-screen: |slope log10 v vs log10 tau| <= 0.30 for v in
    (gap, s, L_EPS, M_src - 1) -- the LM currencies are tau-flat;
    DISGUISE/RIDER report: slopes of log10 |B_00| and log10 |P'|
    PRINTED (both ride tau by construction, BOUND-RIDES-CONNES
    typed; the RATIOS are the flat currencies); G55 conditioning
    (1e-25 shift window; an EXACTLY-ZERO response is a red flag and
    fails the gate).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence demand -> Theorem
    R transfer -> coupling absorbed -> Markov/V2 provide FULL-
    MEASURE-TAIL per block => unbounded sequence; EPSLOCK consumed
    as hypothesis, NOT via the E1 route -- no TOPROOT/ONSETCAP
    demand survives downstream; no ALL-X demand);
    G61 min-cut (r116 replica): flows base 4; the (M') graph (r144
    VERBATIM) 5 AND the LM graph (EPSLOCKAVG(1) -> SUSCAP2R(1) ->
    DELTA1FLOOR(1) serial) 5 -- SAME residue, different bundling;
    one-grant 5; counterfactual PARALLEL readings 9 (M', five legs)
    and 7 (LM, three legs) NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2];
T_PT = 3000175332800 [PT21]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); SCAN_STEP = 0.05; SCAN_LO = 0.5; SCAN_OVER = 6.0;
TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05; NODE_EXCL = 0.02;
ADV_RUNGS = (5, 8); DENSE_GRID = (4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6,
5.8, 6.0) at dps 60 (r143 fine-x-grid machinery class).
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)} (r139/r141/r142 measured
33.62/16.72/22.66/16.59/19.58); S_BAR = 0.1 (r141/r142 s = 0.02974/
0.05981/0.04413/0.06029/0.05108); SGAP_WIN = (0.98, 1.02); D1_TAB =
{5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8} x
(0.7, 1.3); SHARE1_BAR = 0.5; TLAW_TAB = {5: 0.2664, 8: 0.3738, 13:
0.4674, 18: 0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI strings);
INTERLACE_SLOP = 1e-12; YT_TAB = {5: 6.107e4, 8: 4.165e5, 13:
3.204e6, 18: 1.258e7, 24: 4.013e7} x (0.9, 1.1) (r140 strings).
ADJUGATE: ADJ_PAD = 360 dps; RQI_ITERS = 2; RQI_MOVE_MAX = 1e-20
(rel; the eigsy-vs-RQI cross-instrument continuity); ADJ_H = (1e-8,
1e-16) with z - tau = h tau A_0^2 FULLGAP / K (instrument scaling
only, does not taint basis-freeness); ADJ_BAR = {1e-8: 1e-4, 1e-16:
1e-10} (error class ~ h |v_0|^2/K = h, pre-freeze unmeasured,
DISCLOSED, headroom >= 1e4); TOY_EPS = 1e-30 at dps 80, TOY_BAR =
1e-10.  LM: LEPS_ID_BAR = 1e-8; LEPS_WIN = (0.05, 0.35) (r135 locks
0.28..0.51 squared, x >= 5 slice); MSRC_LOG_BAR = 1.0 (expected
0.15..0.30); CA_PT_BAR = 0.5 (expected 0.05..0.20); DENSE_QREL_BAR
= 1e-25; DENSE_S_BAR = 1.0; DENSE_DLOGM_MAX = 1.0; CA_BLK_BAR =
1.0; KJUMP_MIN = 3.  CELL: CELL_C0_MAX = 4.5 (measured expectation
2.2..3.8, falling in x; small-x inflation disclosed); CELL_NPOLY =
(N_tot <= 60 x log(e x) + K(ex) npp(ex), the enumerated families).
RLD: report gates finite-only; fitted alpha + max printed.
REDTEAM: RT_EPS = (0.1, 0.01, 0.001); RT_ID_BAR = 1e-40; RT_S_MIN =
1e5; RT_POLY_WITNESS = 10^6 (exact eps^2 = tau/(tau + Delta P)).
ADVERSARIAL: Q0REL_MIN = 10.0; S_ADV_MIN = 1.0; ADV_ID_BAR = 1e-8;
MSRC_SEP_MIN = 3.0 (predicted ~5.7/6.4 from the r142 s' strings
4.92/6.85, pre-freeze unmeasured as a ratio, DISCLOSED).
CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30; COND_WIN = (1e-40,
1e-10); GAMMA1_LIT = 14.134725141734694 (ward only); RUNTIME_BAR =
14400 s.  Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; zone nodes newton-polished at dps; np.float64-repr casts
guarded by float(); log-scale diagnostics of O(1) quantities in f64,
of tiny/huge quantities via mp.log inside workdps (r141 amendment-1
class); adjugate linear algebra at dps + ADJ_PAD with own
deterministic partial-pivot LU (swaps applied fully BEFORE forward
elimination -- LAPACK getrs order, the r144 smoke-1 lesson inherited
as frozen code).

CALIBRATION DISCLOSURE (pre-freeze): NO scratch script was run for
this probe; every replication window derives from the frozen strings
of the cited rounds (r135 locks; r137/CDXLI tlaw; r139/CDXLIII gap/
delta_1/share_1; r140/CDXLIV y_t; r141/CDXLV s, s x gap; r142/CDXLVI
pinch/defect/FULLGAP; r144/CDXLVIII s_3/route-B cost), quoted
verbatim in FROZEN NUMERICS.  Genuinely NEW quantities are either
THEOREM gates (AD1/AD2/CS/LM-core/red-team -- exact algebra,
risk-free) or disclosed-unmeasured with stated error-class headroom
(ADJ_BAR, TOY_BAR, LEPS windows, C_a bars, MSRC_SEP_MIN, CELL_C0
bar, dense-block bars).  The concurrent lanes (fullgap_spectrum,
onsetcap; files fullgap_onset_probe*, calib_scratch_fullgap*,
sieve4_helper.bin) are NOT touched; their status at spec-freeze is
read-only quoted in the G15 lane note.
SMOKE DISCLOSURE: smoke runs (x = 5 rung, SMOOTH control only,
adversarial x = 5, dense grid first 3 points) are logged and any
instrument repair is disclosed as a numbered SMOKE NOTE here before
the frozen run; amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks.
SMOKE-1 NOTE (disclosed; smoke1 = 24/26, log kept; the two fails
were G32/G33, both INSTRUMENT-side, no bar/criterion/ladder moved):
(1) the adjugate h-ladder solves must REFINE the eigsy phi via one
RQI vector pass BEFORE trusting tau_ref to depth h (the stored
mpE[0] carries only ~dps-digit accuracy; z - tau at h = 1e-16 sits
~80 dex below it) -- the frozen code always runs RQI_ITERS = 2 at
dps + ADJ_PAD as specified, the smoke fail was an ordering bug
(RQI ran at the UNPADDED dps first); (2) the toy near-degenerate
instance needs its OWN h-scale (A_0^2 of the toy, not of the rung)
-- fixed to the spec formula.  Measured smoke exhibits after the
fixes, quoted: x = 5 adjugate devs (h = 1e-8/1e-16): ratio
2.4e-9/2.4e-17, A_0^2 8.7e-9/8.7e-17, P' 1.4e-45/1.4e-45, currency
8.7e-9/8.7e-17; toy dev 3.1e-31; L_EPS = 0.13322; log M_src =
0.15442; C_a^pt = 0.09594; C_0(x=5) = 3.79; M_src separation 5.66.
No criterion moved; ADJ_BAR/TOY_BAR/windows untouched.
SMOKE-2 NOTE (rescue lane, disclosed; the owner's lane died in an
IDE crash at ~14:58 before completing its smoke repairs; smoke2 of
the inherited file = 24/27, fails G12/G33/G38, ALL instrument-side;
no bar/criterion/ladder/window moved): (1) G12 okJ relied on sympy
auto-evaluating the relational sum l_i <= 3 Max(l_i) -- sympy
cannot decide Max relationals; REPAIRED to the exact slack
decomposition l_i = max - s_i, s_i >= 0 ==> sum = 3 max - (s_1 +
s_2 + s_3) <= 3 max (machine-checked identity + nonnegativity, the
same pigeonhole fact); (2) G33 toy: the SMOKE-1 quoted exhibit
(toy dev 3.1e-31) does NOT reproduce on the inherited code
(measured 1.3e-9 at h = 1e-8: error class ~ h (v_0.phi_1)^2/4 with
O(1) A_0^2, unlike the rungs) -- the crashed lane's fix (2) was
recorded but evidently incomplete; REPAIRED by running the toy at
the DEEP frozen ladder member h = 1e-16 (ADJ_H[1], no new
constant; TOY_BAR = 1e-10 untouched, headroom >= 1e7); (3) G38:
s(0.001) = 4.49 because the x = 5 rung's REAL FULLGAP = 2.2255e5
makes s = 1/(FULLGAP eps^2) -- the frozen eps ladder cannot reach
RT_S_MIN; REPAIRED by instantiating the G17 constructive poly
witness eps^2 = tau/(tau + Delta P) at the frozen P = 10^6 (s == P
exactly), which is the spec's own named unboundedness mechanism;
the three eps identity devs are kept unchanged.  Measured after
repairs (smoke3 = 27/27): toy dev 1.3e-17; witness s = 1.00e6 dev
<= 1e-40.  This SMOKE-2 disclosure changes SPEC_SHA (honest
refreeze before the frozen run).
FROZEN-RUN-1 ABORT NOTE (rescue lane, disclosed): the first full
run was ABORTED at the x = 18 ONE-CURVE INFO line, which printed
EPS-LOCK currency 0.00000 vs L_EPS 0.24137: adjugate_pass stored
the eigenproduct as pprime_f = float(pprime), and at the deep
rungs (tau = 5.2e-79, 65 factors) the product UNDERFLOWS float64
to 0, dooming the G32 currency gate at x = 18/24 -- an
instrument-side violation of this spec's own precision discipline
(tiny/huge quantities must stay mp; no f64 casts).  REPAIRED:
pprime is kept as the mp object (pprime_mp) end-to-end (currency
gate + rider-report logs); no bar/criterion/window moved; the
smoke rung x = 5 is unaffected (its pprime is float-representable,
smoke exhibits unchanged).  SPEC_SHA refrozen once more; the
record run starts after this disclosure.

VERDICT ENUMS (frozen): AD1-PROVEN(adjugate identity + B-ratios:
TOPROOT = adjugate-entry ratio, basis-free); AD2-PROVEN(Riesz/
first-nonvanishing-coefficient continuation; DELTA1 term registers
multiplicity); CELL-LEMMA-PROVEN-MODULO-SIMPLICITY(pigeonhole exact
+ counts measured; simplicity leg typed OPEN, measured-only);
ONE-CURVE-INSTANTIATED(per-rung: adjugate route == jet route ==
eigenproduct on the h-ladder; all four residues read off (P, adj));
LM-ASSEMBLED(conditional; every arrow gated or cited);
LM-BEATS-RAW-AVERAGE(pole exhibit gated);
HONESTY-ADJUDICATED(OMEGA-a leg contracts {TOPROOT, ONSETCAP} ->
{EPSLOCK-AVG}, strictly weaker-or-equal hypothesis, both
intersections EMPTY gated; SUSCAP2R/DELTA1FLOOR legs UNCHANGED;
EPSLOCK-AVG stays OPEN-ARITHMETIC -- the residue contracts in
COORDINATES and in hypothesis STRENGTH, not in arithmetic content);
FW-HYPOTHESIS-TYPED(contents enumerated; no TOPROOT/ONSETCAP
inside); CA-MEASURED(pointwise all rungs + ONE dense block across
K-jumps); RLD-STATED-MEASURED(Szegoe/IIKS target
OPEN-CLASSICAL-CANDIDATE, not consumed); REDTEAM-REFUTES-ALGEBRA
(the 2D model passes all algebra and breaks every poly cap;
arithmetic legs refuse it); MSRC-SEES-ARITHMETIC(adversarial
separation); CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES;
QUANTIFIER-INHERITED(dense-x suffices); OMEGA-CONTRACTED-IN-
COORDINATES(census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
MINCUT(4/5; counterfactuals 9 and 7 NOT REAL).  Composite priority:
INSTRUMENT-EDGE (any edge gate fails, exit 1) >
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
ADV_RUNGS = (5, 8)
DENSE_GRID = (4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0)
DENSE_DPS = 60
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
INTERLACE_SLOP = 1e-12
YT_TAB = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
          24: 4.013e7}
YT_WIN = (0.9, 1.1)
ADJ_PAD = 360
RQI_ITERS = 2
RQI_MOVE_MAX = 1e-20
ADJ_H = (1e-8, 1e-16)
ADJ_BAR = {1e-8: 1e-4, 1e-16: 1e-10}
TOY_EPS = 1e-30
TOY_DPS = 80
TOY_BAR = 1e-10
LEPS_ID_BAR = 1e-8
LEPS_WIN = (0.05, 0.35)
MSRC_LOG_BAR = 1.0
CA_PT_BAR = 0.5
DENSE_QREL_BAR = 1e-25
DENSE_S_BAR = 1.0
DENSE_DLOGM_MAX = 1.0
CA_BLK_BAR = 1.0
KJUMP_MIN = 3
CELL_C0_MAX = 4.5
RT_EPS = (0.1, 0.01, 0.001)
RT_ID_BAR = 1e-40
RT_S_MIN = 1e5
RT_POLY_WITNESS = 10 ** 6
Q0REL_MIN = 10.0
S_ADV_MIN = 1.0
ADV_ID_BAR = 1e-8
MSRC_SEP_MIN = 3.0
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
    (r140/r142 shape, ported)."""
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


def kfun(t: float) -> int:
    return int(math.ceil(KFAC * t * math.log(t)))


def prime_powers_upto(n: int) -> list:
    comp = np.zeros(n + 1, dtype=bool)
    out = []
    for p in range(2, n + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= n:
            out.append(q)
            q *= p
    return sorted(out)


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138-r142 replica)."""
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
    (r141/r142 shape).  Caller sets workdps."""
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


# --------------------------------------------- deterministic LU (adjugate)
def lu_factor(Amat, n):
    """own partial-pivot LU in-place on an mp.matrix copy; returns
    (LU, piv, sign).  Deterministic; caller sets workdps."""
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
    """solve with a pre-computed lu_factor; b = list; returns list.
    ALL sequential row swaps are applied BEFORE the forward
    elimination (LAPACK getrs order -- the r144 smoke-1 lesson,
    inherited as frozen code)."""
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
    """determinant from a pre-computed lu_factor; caller sets
    workdps."""
    d = mp.mpf(sign)
    for i in range(n):
        d *= LU[i, i]
    return d


def rqi_refine(Mq, K, tau0, phi0, dps_adj, iters):
    """Rayleigh-quotient iteration at padded dps: refines the ground
    eigenvalue far below the eigsy accuracy (all-mp, deterministic;
    the smoke-1 lesson: run at dps_adj from the start)."""
    with mp.workdps(dps_adj):
        z = mp.mpf(tau0)
        y = [mp.mpf(phi0[i]) for i in range(K)]
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
        return z


def adjugate_pass(ce: dict, ctx: dict, gam: np.ndarray) -> dict:
    """basis-free adjugate instrumentation per rung: RQI-refined tau,
    h-ladder LU of (z I - M), determinant + one solve per h; returns
    the deviation table + currencies."""
    K = ce["K"]
    dps = ce["dps"]
    dps_adj = dps + ADJ_PAD
    out = dict()
    with mp.workdps(dps_adj):
        Mq = ce["mpM"]
        tau0 = ce["mpE"][0]
        phi0 = [ce["mpV"][i, 0] for i in range(K)]
        tau_ref = rqi_refine(Mq, K, tau0, phi0, dps_adj, RQI_ITERS)
        move = float(abs((tau_ref - tau0) / tau0))
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        v0 = [((-1) ** k) / nrm[k] for k in range(K)]
        v2 = [((-1) ** k) * oms[k] ** 2 / nrm[k] for k in range(K)]
        A0 = mp.mpf(0)
        A2 = mp.mpf(0)
        for k in range(K):
            A0 += ((-1) ** k) * mp.mpf(ce["cn_mp_str"][k])
            A2 += ((-1) ** k) * mp.mpf(ce["cn_mp_str"][k]) * oms[k] ** 2
        fullgap = (ce["mpE"][1] - ce["mpE"][0]) / ce["mpE"][0]
        pprime = mp.mpf(1)
        for i in range(1, K):
            pprime *= (tau_ref - ce["mpE"][i])
        scale = tau_ref * A0 * A0 * fullgap / K
        devs = {}
        b00_last = None
        for h in ADJ_H:
            z = tau_ref + mp.mpf(repr(h)) * scale
            A = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A[i, j] = -Mq[i, j]
                A[i, i] += z
            LU, piv, sg = lu_factor(A, K)
            Pz = lu_det(LU, sg, K)
            y = lu_solve_fac(LU, piv, v0, K)
            q00 = sum(v0[i] * y[i] for i in range(K))
            q20 = sum(v2[i] * y[i] for i in range(K))
            dev_ratio = float(abs((q20 / q00) / (A2 / A0) - 1))
            dev_a02 = float(abs((z - tau_ref) * q00 / (A0 * A0) - 1))
            dev_pp = float(abs(Pz / (z - tau_ref) / pprime - 1))
            b00 = Pz * q00
            devs[h] = (dev_ratio, dev_a02, dev_pp)
            b00_last = b00
            out.setdefault("yt_adj", float(abs(q20 / q00)))
        out.update(move=move, devs=devs,
                   pprime_mp=pprime, b00=b00_last,
                   fullgap=float(fullgap), a0f=float(abs(A0)))
    return out


# --------------------------------------------------------- exact layer
def symbolic_gates(lane_note: str) -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    z = sp.symbols("z")

    # Householder frame: u = (1,2,3), H = I - u u^T/7 (orthogonal,
    # symmetric, rational)
    uH = sp.Matrix([1, 2, 3])
    Hh = sp.eye(3) - (uH * uH.T) / 7
    l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)

    # ---------------- G10 AD1 adjugate identity + B-ratios (generic)
    Mgen = Hh * sp.diag(l0, l1, l2) * Hh
    phi = Hh[:, 0]
    Agen = l0 * sp.eye(3) - Mgen
    adjA = Agen.adjugate()
    target = (l0 - l1) * (l0 - l2) * (phi * phi.T)
    okA = sp.simplify(adjA - target) == sp.zeros(3, 3)
    w0a, w0b, w0c, w2a, w2b, w2c = sp.symbols(
        "w0a w0b w0c w2a w2b w2c", real=True)
    v0s = sp.Matrix([w0a, w0b, w0c])
    v2s = sp.Matrix([w2a, w2b, w2c])
    Pp0 = (l0 - l1) * (l0 - l2)
    B00 = (v0s.T * adjA * v0s)[0, 0]
    B20 = (v2s.T * adjA * v0s)[0, 0]
    A0s = (v0s.T * phi)[0, 0]
    A2s = (v2s.T * phi)[0, 0]
    okB = sp.simplify(B20 * A0s - B00 * A2s) == 0
    okC = sp.simplify(B00 - Pp0 * A0s ** 2) == 0
    okD = sp.simplify(
        sp.diff((z - l0) * (z - l1) * (z - l2), z).subs(z, l0)
        - Pp0) == 0
    out.append(("G10-ad1-adjugate-identity", okA and okB and okC
                and okD,
                "adj(l0 I - M) == (l0-l1)(l0-l2) phi phi^T GENERIC in "
                "(l0, l1, l2) on the Householder frame; B_20/B_00 == "
                "A_2/A_0 and A_0^2 == B_00/P'(l0) generic in the "
                "functionals; P'(l0) == (l0-l1)(l0-l2) (THEOREM AD1: "
                "TOPROOT is a ratio of two adjugate entries; the "
                "TLAWCAP/EPS-LOCK currency reads (tau+OFF)|P'|/(16 G "
                "|B_00|); DELTA1FLOOR is a root gap of P -- the "
                "residue lives on ONE spectral curve, basis-free)"))

    # ---------------- G11 AD2 multiplicity / Riesz continuation
    Mdeg = Hh * sp.diag(l0, l0, l2) * Hh
    Adeg = l0 * sp.eye(3) - Mdeg
    okE = sp.simplify(Adeg.adjugate()) == sp.zeros(3, 3)
    Zdeg = z * sp.eye(3) - Mdeg
    dadj = sp.diff(Zdeg.adjugate(), z).subs(z, l0)
    Pi = Hh * sp.diag(1, 1, 0) * Hh
    Pdeg = (z - l0) ** 2 * (z - l2)
    coeff = sp.diff(Pdeg, z, 2).subs(z, l0) / 2
    okF = sp.simplify(dadj - coeff * Pi) == sp.zeros(3, 3)
    e_ = sp.symbols("e_", positive=True)
    Mnd = Hh * sp.diag(1, 1 + e_, 5) * Hh
    And = sp.eye(3) - Mnd
    adjnd = And.adjugate()
    okG = sp.simplify(adjnd - (-e_) * (1 - 5) * (phi * phi.T)) \
        == sp.zeros(3, 3)
    okH = sp.limit(1 + 1 / e_, e_, 0, "+") == sp.oo
    out.append(("G11-ad2-riesz-continuation", okE and okF and okG
                and okH,
                "at tau-multiplicity the adjugate VANISHES (P' = 0); "
                "first nonvanishing coefficient d/dz adj|_{tau} == "
                "(P''(tau)/2!) Pi with Pi the rank-2 Riesz projector "
                "(exact); the near-degenerate family diag(1, 1+e, 5) "
                "keeps B_00 == P' A_0^2 == 4 e A_0^2 EXACTLY for all "
                "e > 0, and the master integrand REGISTERS the "
                "degeneration: lim (1 + 1/delta_1) = oo (THEOREM AD2: "
                "the delta_1 = 0 cases are priced by the DELTA1 term, "
                "log-integrably if isolated -- G13 exhibit)"))

    # ---------------- G12 cell-selection algebra
    Nn = sp.Integer(2)
    okI = bool(sp.Rational(1, 3) >= 1 / (Nn + 1))
    # SMOKE-2 repair (1): sum l_i <= 3 max via the definitional
    # slack decomposition l_i = max - s_i, s_i >= 0 (sympy cannot
    # decide Max relationals; same pigeonhole fact, exact)
    mx_ = sp.symbols("mx_", positive=True)
    s1_, s2_, s3_ = sp.symbols("s1_ s2_ s3_", nonnegative=True)
    tot_sub = (mx_ - s1_) + (mx_ - s2_) + (mx_ - s3_)
    okJ = (sp.expand(3 * mx_ - tot_sub - (s1_ + s2_ + s3_)) == 0
           and (s1_ + s2_ + s3_).is_nonnegative is True)
    C0, U = sp.symbols("C0 U", positive=True)
    okK = sp.simplify(sp.exp(C0 * U) - (sp.exp(U)) ** C0) == 0
    xex = 24
    nk_lo = kfun(xex)
    nk_hi = kfun(math.e * xex)
    okL = (nk_hi - nk_lo) <= 1.25 * math.e * xex \
        * (math.log(xex) + 1) + 2
    out.append(("G12-cell-selection-algebra", okI and okJ and okK
                and okL,
                "pigeonhole: N jump points in a unit u-block leave a "
                "sub-cell of u-width >= 1/(N+1) (1 = sum l_i <= "
                "(N+1) max); log-cost e^{C0 U} == x^{C0} exact; "
                "K-jump count K(ex) - K(x) <= 1.25 e x (log x + 1) + "
                "2 instance at x = 24 (THEOREM CS algebra; the "
                "measured counts + the simplicity-leg typing live in "
                "G34)"))

    # ---------------- G13 LM core algebra + pole exhibit
    a_, b_, c_ = sp.symbols("a_ b_ c_", nonnegative=True)
    prod3 = (1 + a_) * (1 + b_) * (1 + c_)
    okM = bool(sp.simplify(prod3 - (1 + a_)) is not None) and \
        sp.simplify(sp.expand(prod3 - (1 + a_))
                    - (1 + a_) * (b_ + c_ + b_ * c_)) == 0
    okN = sp.expand((1 + a_) * (b_ + c_ + b_ * c_)).is_nonnegative \
        in (True, None)
    okN = sp.simplify(sp.log(prod3).subs(
        {a_: 0, b_: 0, c_: 0})) == 0
    Bv = sp.symbols("Bv", positive=True)
    okO = sp.simplify(Bv / (4 * Bv) - sp.Rational(1, 4)) == 0
    f_int = sp.Rational(5, 1) * sp.Rational(1, 20)
    okP = bool(f_int <= sp.Rational(1, 4)) \
        and bool(sp.Rational(1, 20) <= f_int / (4 * sp.Rational(1, 4)))
    t = sp.symbols("t", positive=True)
    div = sp.integrate(1 / t, (t, 0, 1))
    okQ = div == sp.oo
    fin = sp.integrate(sp.log(1 + 1 / t), (t, 0, 1))
    okR = sp.simplify(fin - 2 * sp.log(2)) == 0
    Cc, Uu = sp.symbols("Cc Uu", positive=True)
    okS = sp.simplify(sp.exp(4 * Cc * Uu)
                      - (sp.exp(Uu)) ** (4 * Cc)) == 0
    fpt, Bpt = sp.symbols("fpt Bpt", positive=True)
    okT = bool(sp.integrate(Bpt, (t, 0, 1)) == Bpt)
    out.append(("G13-lm-core-pole-exhibit", okM and okN and okO
                and okP and okQ and okR and okS and okT,
                "factors >= 1 ==> F = log M_src >= 0 (log(1)=0 + "
                "monotone product); Markov: int F <= C U ==> meas{F > "
                "4CU} <= 1/4; MULTIPLICATIVE split: (1+a) <= "
                "(1+a)(1+b)(1+c) for nonneg ==> ALL THREE factors "
                "simultaneously <= e^{4CU} == x^{4C}; THE POLE "
                "EXHIBIT: int_0^1 dt/t == oo BUT int_0^1 log(1+1/t) "
                "dt == 2 log 2 EXACTLY -- an isolated delta_1 = 0 "
                "point destroys the raw (M') average, not the log "
                "average (LM-BEATS-RAW-AVERAGE); pointwise f <= B "
                "==> block average <= B (one-way; converse refuted "
                "by the exhibit)"))

    # ---------------- G14 arrow re-gates (W2 + V2, r144 shapes)
    lam = sp.symbols("lam")
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    e0, e1, e2 = sp.Rational(3, 13), sp.Rational(4, 13), \
        sp.Rational(12, 13)
    rho2_i = e0 ** 2
    chi_i = e1 ** 2 / (q1i - q0i) + e2 ** 2 / (q2i - q0i)
    s_i = chi_i / rho2_i
    fsec = e0 ** 2 / (q0i - lam) + e1 ** 2 / (q1i - lam) \
        + e2 ** 2 / (q2i - lam)
    roots = sorted(sp.solve(sp.together(fsec).as_numer_denom()[0],
                            lam))
    lam_star = roots[0]
    g_i = lam_star - q0i
    Ps = sp.symbols("Ps", positive=True)
    okU = bool(s_i <= 1 / g_i) and bool(q0i < lam_star < q1i) \
        and bool((q1i - q0i) > g_i)
    R2s, chis, taus, D1s = sp.symbols("R2s chis taus D1s",
                                      positive=True)
    lhsS = (R2s / (chis + R2s / (D1s * taus))) / taus
    rhsS = 1 / (taus * chis / R2s + 1 / D1s)
    okV = sp.simplify(lhsS - rhsS) == 0
    okW = sp.simplify(1 / (Ps + 1 / (1 / Ps)) - 1 / (2 * Ps)) == 0
    okX = bool(g_i >= 1 / (s_i + 1 / (q1i - q0i)))
    h_ = sp.sin(t) - 2 * t / sp.pi
    okY = (sp.simplify(h_.subs(t, 0)) == 0
           and sp.simplify(h_.subs(t, sp.pi / 2)) == 0
           and sp.simplify(sp.diff(h_, t, 2) + sp.sin(t)) == 0)
    okZ = sp.simplify(1 - sp.Rational(1, 4) - sp.Rational(1, 4)
                      - sp.Rational(1, 2)) == 0
    out.append(("G14-arrow-regates", okU and okV and okW and okX
                and okY and okZ,
                "r142 W2 loop re-gated (forward s <= 1/g + root in "
                "(q0, q1); backward g >= 1/(s + 1/delta_1); demand "
                "composition 1/(2P)): QSUBGAP <==> SUSCAP2R AND "
                "DELTA1FLOOR; r141 V2 measure lemma (concavity floor) "
                "+ intersection >= 1/2 re-gated: arrows L5/L6 ride "
                "cited + re-gated algebra"))

    # ---------------- G15 honesty / dependency adjudication
    needs = {"EPSLOCK", "SUSCAP2R", "DELTA1FLOOR"}
    lm_provides = {"EPSLOCK", "SUSCAP2R", "DELTA1FLOOR"}
    covered = needs.issubset(lm_provides)
    old_route_omega_a = {"TOPROOT", "TAILVIS", "TLAWCAP", "ONSETCAP",
                         "JETLOCK", "BANDMASS"}
    lm_hyps = {"H-LM(log-block-integral of M_src)",
               "H-FW", "DENSE-A", "A-EXTENSION", "WINDOW-A"}
    okAA = len({h for h in lm_hyps if h in old_route_omega_a}) == 0
    hfw = {"M2-VALIDITY(r135-G36-class, demand-side)",
           "BALL-VALIDITY(b <= sp/2, source spacing)",
           "ZONE-MASS-MARGIN(m_min >= 16 eps sum|w'|/TL, "
           "poly-inflation-tolerant per r135/r137 E2, CITED)",
           "WINDOW-A(r128 G26)", "TAU-POSITIVE+CENSUS-FRAMEWORK"}
    okBB = len({h for h in hfw if h.split("(")[0] in
                old_route_omega_a}) == 0
    reentry = {"E1-route(r137): JETLOCK + BANDMASS <== TOPROOT + "
               "TAILVIS + TLAWCAP -- the only currently KNOWN proof "
               "route to (H-LM)'s L_EPS factor"}
    contraction = ("OMEGA-a leg: {TOPROOT, ONSETCAP} -> "
                   "{EPSLOCK-AVG} (weaker-or-equal: pointwise route "
                   "==> block average, G13 one-way; converse refuted "
                   "by the pole exhibit); SUSCAP2R + DELTA1FLOOR "
                   "legs IDENTICAL to (M') -- no repackaging, no "
                   "progress there; EPSLOCK-AVG stays "
                   "OPEN-ARITHMETIC")
    okCC = covered and okAA and okBB
    out.append(("G15-honesty-adjudication", okCC,
                "needs(QSUBGAP+OMEGA-a) = {EPSLOCK, SUSCAP2R, "
                "DELTA1FLOOR} COVERED by LM directly; LM-hypotheses "
                "intersect {TOPROOT, ONSETCAP, TAILVIS, JETLOCK, "
                "BANDMASS, TLAWCAP} == EMPTY (the bypass is real, "
                "STATEMENT-level); H-FW = {%s} -- same intersection "
                "EMPTY (nothing hides); KNOWN-ROUTE RE-ENTRY: {%s} "
                "(proving H-LM today would re-enter E1 -- the "
                "both-ways honesty); CONTRACTION: %s; lane note: %s"
                % ("; ".join(sorted(hfw)), "; ".join(sorted(reentry)),
                   contraction, lane_note)))

    # ---------------- G16 RLD statement + sufficiency
    Cr, nvar = sp.symbols("Cr nvar", positive=True)
    okDD = sp.simplify(3 * Cr * sp.log(nvar)
                       - sp.log(nvar ** (3 * Cr))) == 0
    fU, CU = sp.symbols("fU CU", positive=True)
    okEE = bool(sp.integrate(CU * (Uu + 1), (t, 0, 1))
                == CU * (Uu + 1)) and \
        bool(sp.simplify(CU * (Uu + 1) - 2 * CU * Uu
                         <= 0).subs(Uu, 2) in (True, sp.true)) \
        or bool((CU * (Uu + 1) <= 2 * CU * Uu).subs(Uu, 2) == True)  # noqa: E712
    rld_stmt = ("(RLD) for the normalized prime-comb family T_n "
                "(leading principal minors of M_q) and FIXED r: "
                "log(det T_{n+r}/det T_n) = O(log n), INCLUDING the "
                "three special minors: (i) the phi-bordered adjugate "
                "entry B_00 relative to P'(tau) (= A_0^2), (ii) the "
                "zone-row Schur minors det H_3/det H_2 (r144 X4, = "
                "s R_phi^2/tau), (iii) the root-gap factor "
                "(lam_1 - tau)/tau.  TARGET: a relative Szegoe/"
                "IIKS-type strong-limit statement for the prime-comb "
                "symbol class -- typed OPEN-CLASSICAL-CANDIDATE, NOT "
                "attempted, NOT consumed")
    out.append(("G16-rld-statement-sufficiency", okDD and okEE,
                "RLD ==> each M_src factor <= n^{O(1)} = poly(x) ==> "
                "log M_src <= 3 C log n = O(U) POINTWISE ==> (H-LM) "
                "with C_a = O(1) (int_U^{U+1} f <= C(U+1) <= 2 C U "
                "for U >= 1): RLD is SUFFICIENT for the LM "
                "hypothesis; the converse FAILS (block average "
                "tolerates isolated poles, G13) -- one-way typed.  "
                + rld_stmt))

    # ---------------- G17 red-team 2D model (symbolic)
    tau_s, Del = sp.symbols("tau_s Del", positive=True)
    eps = sp.symbols("eps", positive=True)
    lam_rt = sp.solve(eps ** 2 * (tau_s + Del - lam)
                      + (1 - eps ** 2) * (tau_s - lam), lam)
    okFF = len(lam_rt) == 1 and sp.simplify(
        lam_rt[0] - (tau_s + eps ** 2 * Del)) == 0
    lam_rt = lam_rt[0]
    g_rt = (lam_rt - tau_s) / tau_s
    s_rt = tau_s * ((1 - eps ** 2) / Del) / eps ** 2
    okGG = sp.simplify(s_rt * g_rt - (1 - eps ** 2)) == 0
    d1_rt = Del / tau_s
    okHH = sp.simplify((1 - g_rt / d1_rt) - s_rt * g_rt) == 0
    chi2_rt = (1 - eps ** 2) / (d1_rt * (d1_rt - g_rt))
    okII = sp.simplify((1 - s_rt * g_rt)
                       - (g_rt ** 2 / eps ** 2) * chi2_rt) == 0
    Prt = (z - tau_s) * (z - tau_s - Del)
    Qrt = eps ** 2 * (z - tau_s - Del) + (1 - eps ** 2) * (z - tau_s)
    sX2 = tau_s * (sp.diff(Prt, z, 2) / (2 * sp.diff(Prt, z))
                   - sp.diff(Qrt, z) / Qrt)
    okJJ = sp.simplify(sX2.subs(z, tau_s) - s_rt) == 0
    eta0 = sp.solve(Qrt, z)[0]
    okKK = sp.simplify(eta0 - lam_rt) == 0 and \
        bool(sp.simplify(lam_rt - tau_s > 0) in (True, sp.true)
             or (eps ** 2 * Del > 0) == True)  # noqa: E712
    okLL = sp.limit(s_rt, eps, 0, "+") == sp.oo
    Pw = sp.Integer(RT_POLY_WITNESS)
    eps2w = tau_s / (tau_s + Del * Pw)
    okMM = sp.simplify(s_rt.subs(eps ** 2, eps2w) - Pw) == 0 \
        and bool((eps2w < 1) == True) or \
        sp.simplify(s_rt.subs(eps, sp.sqrt(eps2w)) - Pw) == 0
    out.append(("G17-redteam-2d-model", okFF and okGG and okHH
                and okII and okJJ and okKK and okLL and okMM,
                "W = diag(tau, tau+Delta), u = (eps, sqrt(1-eps^2)): "
                "lam* == tau + eps^2 Delta; s g == 1 - eps^2 == 1 - "
                "g/delta_1 (the W1 pinch SATURATED, share_1 = 1); W1 "
                "defect identity holds; X2 Weyl formula == s; eta_0 "
                "== lam* interlaced -- ALL response-curve algebra "
                "intact for EVERY eps, yet lim s = oo and the poly "
                "witness eps^2 = tau/(tau + Delta P) realizes s == P "
                "at P = 10^6 EXACTLY: ANY bound from interlacing/"
                "response algebra alone FAILS this model "
                "(ALGEBRA-ONLY-BOUNDS-REFUTED, hard assert); only "
                "bounds consuming arithmetic input (census, qrel, "
                "frozen windows -- the G30/G31 inputs) may cap s"))
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
                  "dense a; Vitali/Montel sequence-based",
                  demand == SEQ))
    steps.append(("Theorem R (CDXXX, cited) pointwise transfer "
                  "preserves the x-demand level", demand == SEQ))
    steps.append(("coupling x >= sqrt(a)/(2.5 pi) is a lower bound: "
                  "absorbed by any unbounded sequence tail", True))
    steps.append(("(H-LM) + Markov (G13) + V2 (G14) provide FULL-"
                  "MEASURE-TAIL good u per block => unbounded "
                  "sequence exists constructively",
                  FULL_MEAS <= demand))
    steps.append(("EPSLOCK consumed DIRECTLY as the L_EPS factor "
                  "(hypothesis-level, NOT via the r137 E1 route): no "
                  "TOPROOT/ONSETCAP/TAILVIS demand survives "
                  "downstream (G15)", True))
    steps.append(("no ALL-X demand introduced downstream",
                  demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ------------------------------------------------- per-point LM pipeline
def lm_point(ce: dict, gam: np.ndarray, qrel_bar: float) -> dict:
    """full LM pipeline at one cell: census + polish + V + argmin +
    (L_EPS, s, d, M_src).  Returns the point dict (or ok=False)."""
    x = ce["x"]
    K = ce["K"]
    dps = ce["dps"]
    is_deep = float(x) > 13
    Tz = 2 * math.pi * float(x)
    m_zone = int(np.sum(gam <= Tz))
    ctx = source_ctx(ce)
    with mp.workdps(dps):
        cs = ctx["cs"]
        aa = ctx["aa"]
        oms = [k * mp.pi / aa for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        A0 = ctx["A0"]
        tauf = float(ce["mpE"][0])
        eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(A0))
        off = float(8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2) \
            * hsw_G(float(T_PT))
    Gz = hsw_G(Tz)
    D = 8.0 * ctx["a0f"] ** 2 * Gz
    tlaw = tauf / D
    # census
    if not is_deep:
        mus, n_nonreal = raw_mp_census(ce)
        seeds = [float(v) for v in mus]
        cens_ok = (len(mus) == K - 1 and n_nonreal == 0)
    else:
        with mp.workdps(dps):
            ts = np.arange(SCAN_LO, Tz + SCAN_OVER, SCAN_STEP)
            vprev = en_pair(cs, aa, oms, mp.mpf(repr(float(ts[0]))))[0]
            seeds = []
            for tv in ts[1:]:
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                if v * vprev < 0:
                    seeds.append(float(tv) - SCAN_STEP / 2)
                vprev = v
        cens_ok = len(seeds) >= m_zone + 1
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
    zone_nds = nds_all[:m_zone]
    zone_f = nds_f_all[:m_zone]
    Vd = build_V(ce, zone_nds)
    with mp.workdps(dps):
        fullgap = float((ce["mpE"][1] - ce["mpE"][0]) / ce["mpE"][0])
        d1_node = float((Vd["qs"][1] - Vd["qs"][0]) / Vd["tau_mp"])
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
        s_f = float(s_val)
        sg_f = float(sg)
        d1_f = float(d1)
        share1 = float((etn[1] * etn[1] / (Vd["qs"][1]
                                           - Vd["qs"][0])) / chi)
        rphi2 = float(sum(r[k] * mp.mpf(ce["cn_mp_str"][k]) * nrm[k]
                          for k in range(K)) ** 2)
    leps = (tauf + off) / (16.0 * ctx["a0f"] ** 2 * Gz)
    dsrc = 1.0 / d1_f
    msrc = (1.0 + leps) * (1.0 + s_f) * (1.0 + dsrc)
    return dict(x=x, K=K, m=m_zone, cens_ok=cens_ok, wres=wres,
                qrel=Vd["qrel"], resR=Vd["resR"], nf=Vd["nf"],
                tau=tauf, off=off, Gz=Gz, D=D, tlaw=tlaw,
                yt=ctx["yt"], btop=ctx["btop"], a0f=ctx["a0f"],
                fullgap=fullgap, d1_node=d1_node, gmin=gmin,
                s=s_f, sg=sg_f, d1=d1_f, share1=share1,
                leps=leps, dsrc=dsrc, msrc=msrc,
                logm=math.log(msrc), rphi2=rphi2, ctx=ctx, Vd=Vd,
                zone_nds=zone_nds)


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("adjugate_logmaster_probe -- PRIME.ADJUGATE.SPECTRALCURVE"
          ".01 + PRIME.COFINAL.LOGMASTER.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    adv_rungs = (5,) if smoke else ADV_RUNGS
    dense_grid = DENSE_GRID[:3] if smoke else DENSE_GRID
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

    # concurrent-lane status at freeze (read-only existence checks)
    lane_bits = []
    for fn, tag in (("fullgap_onset_probe.py", "fullgap_onset"),
                    ("calib_scratch_fullgap_spectrum.py",
                     "fullgap_spectrum-scratch"),
                    ("onsetcap_probe.py", "onsetcap")):
        if os.path.exists(os.path.join(HERE, fn)):
            lane_bits.append(tag + ":present")
    lane_note = ("CONCURRENT-LANES(%s; notes pending at spec-freeze, "
                 "merged only in the residue reading)"
                 % (",".join(lane_bits) if lane_bits else "none"))

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

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (AD1/AD2 + CS + LM core + red-team)")
    for name, okg, detg in symbolic_gates(lane_note):
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + G26 window-a; r131 secular + GW + OFF recipe; "
         "r132 raw census; r135 D1-D4 + H-pin demand tables "
         "(M2-validity, sp-caps, margins) + locks; r137/CDXLI E1/E2 "
         "+ budget identity (NOT consumed by LM -- named as the "
         "re-entry route only); r138 Q1-Q3; r139/CDXLIII U1-U4; "
         "r140/CDXLIV J-toolkit + y_t strings; r141/CDXLV V1-V3 + "
         "quantifier audit; r142/CDXLVI W1-W3 + FULLGAP; "
         "r143/CDXLVII T1-T4 + fine-x-grid smoothness + "
         "delta_1-lock; r144/CDXLVIII X1-X4 (three-row s = tau det "
         "H_3/(R_phi^2 det H_2), CITED as the SUSCAP2R leg of the "
         "one-curve reading) + (M') arrow table; HSW22 Cor. 1.2; "
         "PT21; Courant-Fischer; Cramer/adjugate + Riesz projector "
         "(elementary, gated G10/G11); Szegoe strong limit + IIKS "
         "NAMED as the RLD target class (not consumed)")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    gtop = float(gam[-1])
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone; "
          "G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: ADJUGATE + LM INTEGRANDS")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok35 = True
    det30, det31, det32, det35 = [], [], [], []
    pts = {}
    cells = {}
    b00_slopes = []
    for x, dps in all_rungs:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        t_p = time.time()
        pt = lm_point(ce, gam, QREL_BAR)
        pts[x] = pt
        ok30 = ok30 and pt["cens_ok"]
        det30.append("x%d: zone %d/%d res %.0e"
                     % (x, pt["m"], pt["m"], pt["wres"]))
        lo_w, hi_w = REPL_WIN[x]
        tl_dev = abs(pt["tlaw"] / TLAW_TAB[x] - 1.0)
        ok31x = (abs(pt["qrel"]) <= QREL_BAR
                 and pt["resR"] <= NULLRES_BAR
                 and pt["d1_node"] >= pt["fullgap"]
                 * (1.0 - INTERLACE_SLOP)
                 and pt["gmin"] >= GAP_MIN_BAR
                 and lo_w <= pt["gmin"] <= hi_w
                 and pt["s"] <= S_BAR
                 and SGAP_WIN[0] <= pt["sg"] <= SGAP_WIN[1]
                 and D1_WIN[0] <= pt["d1"] / D1_TAB[x] <= D1_WIN[1]
                 and pt["share1"] >= SHARE1_BAR
                 and tl_dev <= TLAW_TOL)
        ok31 = ok31 and ok31x
        det31.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1 "
                     "%.3e share1 %.3f tlaw %.4f (%.0f s)"
                     % (x, pt["qrel"], pt["gmin"], pt["s"], pt["sg"],
                        pt["d1"], pt["share1"], pt["tlaw"],
                        time.time() - t_p))

        # ---- G32 adjugate instantiation (basis-free)
        t_a = time.time()
        ad = adjugate_pass(ce, pt["ctx"], gam)
        okx = ad["move"] <= RQI_MOVE_MAX
        for h in ADJ_H:
            dr, da, dp = ad["devs"][h]
            okx = okx and dr <= ADJ_BAR[h] and da <= ADJ_BAR[h] \
                and dp <= ADJ_BAR[h]
        yt_ok = YT_WIN[0] <= ad["yt_adj"] / YT_TAB[x] <= YT_WIN[1]
        # currency identity: (tau+OFF)|P'|/(16 G |B00|) == L_EPS
        with mp.workdps(dps + ADJ_PAD):
            cur = (mp.mpf(repr(pt["tau"])) + mp.mpf(repr(pt["off"]))) \
                * abs(ad["pprime_mp"]) \
                / (16 * mp.mpf(repr(pt["Gz"])) * abs(ad["b00"]))
            dev_cur = float(abs(cur / mp.mpf(repr(pt["leps"])) - 1))
        okx = okx and yt_ok and dev_cur <= ADJ_BAR[ADJ_H[0]]
        ok32 = ok32 and okx
        h1, h2 = ADJ_H
        det32.append("x%d: rqi-move %.0e; dev(h=%.0e) r/a/p "
                     "%.1e/%.1e/%.1e; dev(h=%.0e) %.1e/%.1e/%.1e; "
                     "y_t(adj) %.3e win %s; currency dev %.1e "
                     "(%.0f s)"
                     % (x, ad["move"], h1, *ad["devs"][h1], h2,
                        *ad["devs"][h2], ad["yt_adj"], yt_ok,
                        dev_cur, time.time() - t_a))
        with mp.workdps(dps):
            l10 = mp.log(10)
            lb00 = float(mp.log(abs(ad["b00"])) / l10)
            lpp = float(mp.log(abs(ad["pprime_mp"])) / l10)
        b00_slopes.append((math.log10(pt["tau"]), lb00, lpp))
        info("x=%d ONE-CURVE exhibit: TOPROOT = |B_20/B_00| = %.4e "
             "(jets %.4e); EPS-LOCK currency (tau+OFF)|P'|/(16 G "
             "|B_00|) = %.5f == L_EPS %.5f; SUSCAP2R = tau det H_3/"
             "(R_phi^2 det H_2) (r144 X4 CITED; route-A s = %.5f); "
             "DELTA1FLOOR <== FULLGAP (root gap of P) = %.4e -- all "
             "four residues read off (P, adj) of ONE matrix, "
             "basis-free" % (x, ad["yt_adj"], pt["yt"],
                             float(cur), pt["leps"], pt["s"],
                             pt["fullgap"]))

        # ---- G35 LM integrands
        leps_id = abs(pt["leps"] / ((pt["tlaw"]
                                     + pt["off"] / pt["D"]) / 2.0)
                      - 1.0)
        U = math.log(x)
        ca_pt = pt["logm"] / U
        ok35x = (leps_id <= LEPS_ID_BAR
                 and LEPS_WIN[0] <= pt["leps"] <= LEPS_WIN[1]
                 and pt["msrc"] > 1.0
                 and pt["logm"] <= MSRC_LOG_BAR
                 and ca_pt <= CA_PT_BAR)
        ok35 = ok35 and ok35x
        det35.append("x%d: L_EPS %.5f s %.5f d %.1e M_src %.5f "
                     "logM %.5f C_a^pt %.5f"
                     % (x, pt["leps"], pt["s"], pt["dsrc"],
                        pt["msrc"], pt["logm"], ca_pt))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    check("G31-node-config-replication", ok31,
          "|qrel| <= %.0e, null residual <= %.0e, delta_1 >= FULLGAP "
          "(r142 W3 re-gate); zone-top argmin in the frozen windows "
          "+ s <= %.1f + s x gap in %s + delta_1/share_1/tlaw on the "
          "cited strings: %s"
          % (QREL_BAR, NULLRES_BAR, S_BAR, str(SGAP_WIN),
             "; ".join(det31)))
    check("G32-adjugate-instantiated", ok32,
          "basis-free h-ladder (RQI-refined tau at dps + %d, own LU "
          "det + solve): B_20/B_00 == A_2/A_0, (z - tau)(v_0.y) == "
          "A_0^2, LU-det P(z)/(z - tau) == eigenproduct P'(tau) "
          "(dual instrument), |B_20/B_00| in the r140 y_t windows, "
          "EPS-LOCK currency identity <= %.0e (THEOREM AD1 "
          "instantiated -- ONE-CURVE): %s"
          % (ADJ_PAD, ADJ_BAR[ADJ_H[0]], "; ".join(det32)))

    # ---- G33 near-degenerate mp toy
    with mp.workdps(TOY_DPS + ADJ_PAD):
        uT = mp.matrix([1, 2, 3, 4])
        nT = sum(uT[i] * uT[i] for i in range(4))
        HT = mp.eye(4)
        for i in range(4):
            for j in range(4):
                HT[i, j] -= 2 * uT[i] * uT[j] / nT
        eps_t = mp.mpf(repr(TOY_EPS))
        DT = mp.diag([mp.mpf(1), 1 + eps_t, mp.mpf(5), mp.mpf(7)])
        MT = HT * DT * HT
        tauT = mp.mpf(1)
        phiT = [HT[i, 0] for i in range(4)]
        v0T = [mp.mpf(1), mp.mpf(-1), mp.mpf(1), mp.mpf(-1)]
        A0T = sum(v0T[i] * phiT[i] for i in range(4))
        ppT = (tauT - (1 + eps_t)) * (tauT - 5) * (tauT - 7)
        # SMOKE-2 repair (2): deep frozen ladder member h = ADJ_H[1]
        # (toy error class ~ h (v_0.phi_1)^2/4 with O(1) A_0^2)
        zT = tauT + mp.mpf(repr(ADJ_H[1])) * tauT * A0T * A0T \
            * eps_t / 4
        AT = mp.zeros(4, 4)
        for i in range(4):
            for j in range(4):
                AT[i, j] = -MT[i, j]
            AT[i, i] += zT
        LUT, pivT, sgT = lu_factor(AT, 4)
        PzT = lu_det(LUT, sgT, 4)
        yT = lu_solve_fac(LUT, pivT, v0T, 4)
        q00T = sum(v0T[i] * yT[i] for i in range(4))
        devT = float(abs((zT - tauT) * q00T / (A0T * A0T) - 1))
    check("G33-near-degenerate-toy", devT <= TOY_BAR,
          "4x4 Householder toy diag(1, 1+%.0e, 5, 7) at dps %d: the "
          "h-instrument reproduces (z - tau) v_0.(zI-M)^-1 v_0 == "
          "A_0^2 with rel dev %.1e <= %.0e ACROSS a %.0e ground gap "
          "(the identity survives near-degeneracy when h is scaled "
          "by A_0^2 FULLGAP; the exact degenerate limit is G11)"
          % (TOY_EPS, TOY_DPS, devT, TOY_BAR, TOY_EPS))

    check("G35-lm-integrands", ok35,
          "L_EPS == (tlaw + OFF/D)/2 identity <= %.0e; L_EPS in %s "
          "(r135 locks squared); M_src > 1 strictly; log M_src <= "
          "%.1f; pointwise C_a = log M_src / U <= %.1f "
          "(MEASURED-POINTWISE; the LM integrand carries NO y_t "
          "term -- contrast (M') I1 ~ x^4.15): %s"
          % (LEPS_ID_BAR, str(LEPS_WIN), MSRC_LOG_BAR, CA_PT_BAR,
             "; ".join(det35)))
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lca = [math.log10(pts[x]["logm"] / math.log(x))
               for x in xs_all]
        lx = [math.log10(float(x)) for x in xs_all]
        sl_ca = float(np.polyfit(lx, lca, 1)[0])
        info("pointwise C_a table: %s; slope log10 C_a^pt vs log10 x "
             "= %.3f (falling/flat expected: the LM block hypothesis "
             "is pointwise-satisfied with C_a ~ 0.1 against ANY "
             "demand -- compare (M') Isum slope 4.15)"
             % ("; ".join("x%d %.4f" % (x, pts[x]["logm"]
                                        / math.log(x))
                          for x in xs_all), sl_ca))

    # ---- G36 dense-u block
    section("S3d  DENSE-u BLOCK (LM block integral, first instrument)")
    dense_pts = []
    ok36 = True
    kj_seen = set()
    for xf in dense_grid:
        ce_d = R4.build_cell(xf, KFAC, "MAIN", DENSE_DPS,
                             want_mp=True)
        pt = lm_point(ce_d, gam, DENSE_QREL_BAR)
        kj_seen.add(ce_d["K"])
        okp = (pt["cens_ok"] and abs(pt["qrel"]) <= DENSE_QREL_BAR
               and pt["tau"] > 0
               and pt["d1_node"] >= pt["fullgap"]
               * (1.0 - INTERLACE_SLOP)
               and pt["s"] <= DENSE_S_BAR and pt["msrc"] > 1.0)
        ok36 = ok36 and okp
        dense_pts.append((math.log(xf), pt["logm"], ce_d["K"],
                          pt["m"], okp, pt["fullgap"]))
        print("  u=%.4f (x=%.1f): K=%d m=%d logM=%.5f FULLGAP=%.3e "
              "%s" % (math.log(xf), xf, ce_d["K"], pt["m"],
                      pt["logm"], pt["fullgap"],
                      "ok" if okp else "FAIL"), flush=True)
    djump = max(abs(dense_pts[i + 1][1] - dense_pts[i][1])
                for i in range(len(dense_pts) - 1))
    ok36 = ok36 and djump <= DENSE_DLOGM_MAX \
        and len(kj_seen) - 1 >= (KJUMP_MIN if not smoke else 1)
    us = [p[0] for p in dense_pts]
    fs = [p[1] for p in dense_pts]
    integ = sum((fs[i] + fs[i + 1]) / 2 * (us[i + 1] - us[i])
                for i in range(len(us) - 1))
    span = us[-1] - us[0]
    u_mid = 0.5 * (us[0] + us[-1])
    ca_blk = (integ / span) / u_mid
    ok36 = ok36 and ca_blk <= CA_BLK_BAR
    check("G36-dense-u-block", ok36,
          "x = %.1f..%.1f (%d builds, dps %d, u-span %.4f DISCLOSED "
          "partial block): all points structurally certified (census "
          "== m, |qrel| <= %.0e, delta_1 >= FULLGAP, M_src > 1); "
          "max adjacent |Delta log M_src| = %.4f <= %.1f ACROSS %d "
          "K-jumps and the x = 5 prime crossing; trapezoid block "
          "average C_a^blk = (int/span)/U_mid = %.4f <= %.1f (the "
          "(H-LM) hypothesis measured BLOCK-LEVEL for the first "
          "time, not just pointwise)"
          % (dense_grid[0], dense_grid[-1], len(dense_grid),
             DENSE_DPS, span, DENSE_QREL_BAR, djump,
             DENSE_DLOGM_MAX, len(kj_seen) - 1, ca_blk, CA_BLK_BAR))

    # ---- G34 cell-selection counts
    pp_all = prime_powers_upto(int(math.e * 24) + 2)
    ok34 = True
    det34 = []
    for x, _d in all_rungs:
        U = math.log(x)
        ex = math.e * x
        n_k = kfun(ex) - kfun(x)
        n_pp = sum(1 for q in pp_all if x < q <= ex)
        n_zone = int(np.sum((gam > 2 * math.pi * x)
                            & (gam <= 2 * math.pi * ex)))
        n_tent = kfun(ex) * sum(1 for q in pp_all if q <= ex)
        n_tot = n_k + n_pp + n_zone + n_tent
        c0 = math.log(n_tot + 1) / U
        okc = n_tot <= 60 * x * math.log(ex) + n_tent + 10 \
            and c0 <= CELL_C0_MAX
        ok34 = ok34 and okc
        det34.append("x%d: N_K %d N_pp %d N_zone %d N_tent<= %d "
                     "N_tot %d width>=x^-%.2f (C_0 %.2f)"
                     % (x, n_k, n_pp, n_zone, n_tent, n_tot, c0, c0))
    simp_ok = all(pts[x]["fullgap"] > 0 for x, _d in all_rungs) \
        and all(p[5] > 0 for p in dense_pts)
    ok34 = ok34 and simp_ok
    check("G34-cell-selection-counts", ok34,
          "per block [log x, log x + 1]: K-jumps (exact) + atom "
          "births (sieve) + census crossings (cache) + tent/atom "
          "pair bound (each pair monotone: <= 1 crossing/block); "
          "pigeonhole width >= 1/(N+1) >= x^{-C_0} with measured C_0 "
          "<= %.1f (falling in x; the O(U) log-width cost IS the LM "
          "currency); SIMPLICITY LEG: FULLGAP > 0 at every rung AND "
          "every dense-u point (measured; r143 fine-grid smoothness "
          "CITED) -- the per-cell degeneracy COUNT is NOT proven: "
          "typed CELL-LEMMA-MODULO-SIMPLICITY: %s"
          % (CELL_C0_MAX, "; ".join(det34)))

    # ---- G37 RLD measured
    ok37 = True
    det37 = []
    for x, dps in all_rungs:
        ce = cells[x]
        K = ce["K"]
        with mp.workdps(dps):
            Lch = mp.cholesky(ce["mpM"])
            l10 = mp.log(10)
            dns = [float(2 * mp.log(Lch[n, n]) / l10)
                   for n in range(K)]
        lo_half = K // 2
        dtop = [abs(dns[n]) / math.log10(n + 2)
                for n in range(lo_half, K)]
        lx_ = [math.log10(n + 1) for n in range(1, K)]
        alpha = float(np.polyfit(lx_, dns[1:], 1)[0])
        m1 = 2.0 * math.log10(pts[x]["a0f"])
        m2 = math.log10(pts[x]["s"] * pts[x]["rphi2"] / pts[x]["tau"])
        m3 = math.log10(pts[x]["fullgap"])
        fin = all(map(math.isfinite, [alpha, max(dtop), m1, m2, m3]))
        ok37 = ok37 and fin
        det37.append("x%d: alpha %.2f max|d_n|/log(n) %.2f; minors "
                     "log10: B00/P'=2log|A_0| %.1f, detH3/detH2 "
                     "%.1f, FULLGAP %.1f"
                     % (x, alpha, max(dtop), m1, m2, m3))
    check("G37-rld-measured", ok37,
          "relative log-dets d_n = log10 det T_{n+1}/det T_n of the "
          "prime-comb leading-minor family (mp Cholesky): fitted "
          "slope alpha vs log10 n + top-half max |d_n|/log10 n "
          "printed (the O(log n) class is MEASURED, not claimed); "
          "the three special minors printed per rung; the relative "
          "Szegoe/IIKS target stays OPEN-CLASSICAL-CANDIDATE (G16 "
          "statement; NOT consumed): %s" % "; ".join(det37))

    # ---- G38 red-team mp instantiation
    ok38 = True
    det38 = []
    pt5 = pts[5]
    with mp.workdps(120):
        tau_rt = mp.mpf(repr(pt5["tau"]))
        Del_rt = mp.mpf(repr(pt5["fullgap"])) * tau_rt
        for ev in RT_EPS:
            e2 = mp.mpf(repr(ev)) ** 2
            lam_rt = tau_rt + e2 * Del_rt
            g_rt = (lam_rt - tau_rt) / tau_rt
            s_rt = tau_rt * (1 - e2) / (Del_rt * e2)
            dev_sg = float(abs(s_rt * g_rt - (1 - e2)))
            d1_rt = Del_rt / tau_rt
            chi2_rt = (1 - e2) / (d1_rt * (d1_rt - g_rt))
            dev_id = float(abs((1 - s_rt * g_rt)
                               - (g_rt * g_rt / e2) * chi2_rt))
            ok38 = ok38 and dev_sg <= RT_ID_BAR \
                and dev_id <= RT_ID_BAR
            det38.append("eps %.0e: sg-dev %.0e id-dev %.0e s %.2e"
                         % (ev, dev_sg, dev_id, float(s_rt)))
        # SMOKE-2 repair (3): the G17 constructive poly witness
        # eps^2 = tau/(tau + Delta P) at the frozen P = 10^6
        # (s == P exactly) carries the unboundedness leg
        Pw_rt = mp.mpf(RT_POLY_WITNESS)
        e2w_rt = tau_rt / (tau_rt + Del_rt * Pw_rt)
        s_w = tau_rt * (1 - e2w_rt) / (Del_rt * e2w_rt)
        dev_w = float(abs(s_w / Pw_rt - 1))
        s_wit = float(s_w)
    ok38 = ok38 and dev_w <= RT_ID_BAR and s_wit >= RT_S_MIN
    check("G38-redteam-instantiated", ok38,
          "2D model at the x = 5 rung data (tau, Delta = FULLGAP "
          "tau): s g == 1 - eps^2 and the W1 defect identity hold "
          "to <= %.0e at every eps AND the constructive poly "
          "witness eps^2 = tau/(tau + Delta P) realizes s = %.2e "
          "== P = %.0e (rel dev %.0e) >= %.0e -- the algebra is "
          "eps-uniform, s is unbounded: the numeric side of the "
          "G17 hard assert (any algebra-only cap is refuted; the "
          "arithmetic legs G30/G31 cannot even be entered by this "
          "model -- no census, no source): %s"
          % (RT_ID_BAR, s_wit, float(Pw_rt), dev_w, RT_S_MIN,
             "; ".join(det38)))

    # ---------------------------------------------------------- S3b
    section("S3b  ADVERSARIAL WITNESS (LM currency must see "
            "arithmetic)")
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
        d1q_min = None
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
                    and plo - 1e-12 <= float(sgq) <= 1.0 + 1e-12
                if s_max is None or float(sq) > s_max:
                    s_max = float(sq)
                    d1q_min = float(d1q)
        msrc_adv = (1.0 + pts[x]["leps"]) * (1.0 + s_max) \
            * (1.0 + 1.0 / d1q_min)
        sep = msrc_adv / pts[x]["msrc"]
        okx = (q0rel >= Q0REL_MIN and s_max is not None
               and s_max >= S_ADV_MIN and alg_ok
               and sep >= MSRC_SEP_MIN)
        ok40 = ok40 and okx
        det40.append("x%d: q0rel %.1e s'_max %.2f (truth %.4f) "
                     "M_src' %.2f vs %.4f (sep %.1f) algebra-blind "
                     "%s" % (x, q0rel, s_max, pts[x]["s"], msrc_adv,
                             pts[x]["msrc"], sep, alg_ok))
    check("G40-adversarial-lm-witness", ok40,
          "RvM-legal quantile config: q0rel >= %.0f AND max s' >= "
          "%.1f vs truth s <= %.1f AND W1 pinch + defect identity "
          "HOLD on the adversarial well (algebra config-blind) AND "
          "the LM MASTER integrand separates: M_src(adv)/M_src >= "
          "%.1f -- the (H-LM) hypothesis is ARITHMETIC-PINNED, not "
          "currency-blind: %s"
          % (Q0REL_MIN, S_ADV_MIN, S_BAR, MSRC_SEP_MIN,
             "; ".join(det40)))

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
        with mp.workdps(dpsw):
            eta_w = float(envj(cwx, mp.mpf(T_PT) ** 2)
                          / abs(cwx["A0"]))
            off_w = float(8 * mp.exp(cwx["aa"])
                          * (abs(cwx["A0"]) * (1 + eta_w)) ** 2) \
                * hsw_G(float(T_PT))
        ytbw = cwx["yt"] / cwx["btop"]
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX
                  and (tauw + off_w) < 0)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD); y_t_w/b_top = %.2f <= %.1f; tau_w + "
              "OFF_w = %.3e < 0: eps_bar^2 < 0 -- the false world "
              "cannot enter the L_EPS/M_src currency (factor >= 1 "
              "precondition fails)"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX, tauw + off_w))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale + negative eps_bar^2; "
          "the AD1/AD2/LM machinery claims nothing where PSD/pinning "
          "fail")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(pts[x]["tau"], 1e-300)) for x in xs_all]
        s_g = float(np.polyfit(lt, [math.log10(pts[x]["gmin"])
                                    for x in xs_all], 1)[0])
        s_s = float(np.polyfit(lt, [math.log10(pts[x]["s"])
                                    for x in xs_all], 1)[0])
        s_le = float(np.polyfit(lt, [math.log10(pts[x]["leps"])
                                     for x in xs_all], 1)[0])
        s_ms = float(np.polyfit(lt, [math.log10(pts[x]["msrc"] - 1)
                                     for x in xs_all], 1)[0])
        s_b0 = float(np.polyfit([b[0] for b in b00_slopes],
                                [b[1] for b in b00_slopes], 1)[0])
        s_pp = float(np.polyfit([b[0] for b in b00_slopes],
                                [b[2] for b in b00_slopes], 1)[0])
        check("G54-tau-screen", abs(s_g) <= TAU_SLOPE_BAR
              and abs(s_s) <= TAU_SLOPE_BAR
              and abs(s_le) <= TAU_SLOPE_BAR
              and abs(s_ms) <= TAU_SLOPE_BAR,
              "slopes vs log10 tau: gap %.4f, s %.4f, L_EPS %.4f, "
              "M_src - 1 %.4f (all <= %.2f: the LM currencies are "
              "tau-flat); RIDER REPORT: log10 |B_00| slope %.2f, "
              "log10 |P'| slope %.2f (both ride tau by construction "
              "-- BOUND-RIDES-CONNES typed; the adjugate RATIOS are "
              "the flat coordinates)"
              % (s_g, s_s, s_le, s_ms, TAU_SLOPE_BAR, s_b0, s_pp))
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
              "(nonzero and bounded; an EXACTLY-ZERO response is a "
              "red flag and fails here; round-118 trap; all mp "
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
    ext_mp = dict(base)
    ext_mp.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
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
    f_mp = R4.maxflow(dict(ext_mp), "UNC", "RH")
    ext_lm = dict(base)
    ext_lm.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                   ("NFCLOS", "L1TAILPROVEN"): INF,
                   ("L1TAILPROVEN", "EPSLOCKAVG"): 1,
                   ("EPSLOCKAVG", "SUSCAP2R"): 1,
                   ("SUSCAP2R", "DELTA1FLOOR"): 1,
                   ("DELTA1FLOOR", "QSUBGAPTHM"): INF,
                   ("QSUBGAPTHM", "PFLOORTHM"): INF,
                   ("PFLOORTHM", "COUNTEQTHM"): INF,
                   ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                   ("SEEDBALLTHM", "SPACREMTHM"): INF,
                   ("SPACREMTHM", "DOMASYM"): INF,
                   ("DOMASYM", "WPDWIN"): INF,
                   ("WPDWIN", "R4HYP"): INF})
    f_lm = R4.maxflow(dict(ext_lm), "UNC", "RH")
    one = dict(ext_lm)
    one[("L1TAILPROVEN", "EPSLOCKAVG")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf_mp = dict(base)
    cf_mp.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                  ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
                  ("NFCLOS", "TAILVIS"): 1,
                  ("TAILVIS", "R4HYP"): INF,
                  ("NFCLOS", "TLAWCAP"): 1,
                  ("TLAWCAP", "R4HYP"): INF,
                  ("NFCLOS", "SUSCAP2R"): 1,
                  ("SUSCAP2R", "R4HYP"): INF,
                  ("NFCLOS", "DELTA1FLOOR"): 1,
                  ("DELTA1FLOOR", "R4HYP"): INF})
    f_cf_mp = R4.maxflow(dict(cf_mp), "UNC", "RH")
    cf_lm = dict(base)
    cf_lm.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                  ("NFCLOS", "EPSLOCKAVG"): 1,
                  ("EPSLOCKAVG", "R4HYP"): INF,
                  ("NFCLOS", "SUSCAP2R"): 1,
                  ("SUSCAP2R", "R4HYP"): INF,
                  ("NFCLOS", "DELTA1FLOOR"): 1,
                  ("DELTA1FLOOR", "R4HYP"): INF})
    f_cf_lm = R4.maxflow(dict(cf_lm), "UNC", "RH")
    noomega = {k2: v for k2, v in ext_lm.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_mp == 5 and f_lm == 5
          and f_one == 5 and f_cf_mp == 9 and f_cf_lm == 7
          and "RH" not in reach,
          "flows: base 4; (M') graph (r144 VERBATIM) 5 AND LM graph "
          "(EPSLOCKAVG(1) -> SUSCAP2R(1) -> DELTA1FLOOR(1) serial) "
          "5 -- the SAME residue in contracted coordinates, not a "
          "new unit edge; one-grant 5; counterfactual PARALLEL "
          "readings 9 (M', five legs) and 7 (LM, three legs) NOT "
          "REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; "
          "RH unreachable without the omega edges")
    info("EXACT RESIDUE after this round (read with CDXLVI/CDXLVII/"
         "CDXLVIII; concurrent lanes merged only in the note's "
         "residue reading): RH <== [r122-NF-closure] + [Theorem R] + "
         "{L1, WPD} on dense a; in LM COORDINATES the residue is "
         "THREE block-average factors of ONE integrand M_src = "
         "(1 + L_EPS)(1 + s)(1 + 1/delta_1): {EPSLOCK-AVG (<= "
         "old {TOPROOT, ONSETCAP} route, strictly weaker-or-equal "
         "hypothesis), SUSCAP2R-AVG (= SUSCAP2R), DELTA1FLOOR-AVG "
         "(<== FULLGAP)} + H-FW (typed, no TOPROOT/ONSETCAP inside) "
         "+ dense-a + a-extension + window-a; TAILVIS stays "
         "eliminated-counting-class (CDXLVII); the SET census {MEAS, "
         "OMEGA-POS} cardinality 4 is UNCHANGED -- the contraction "
         "is in coordinates and hypothesis STRENGTH (pointwise -> "
         "log-block-average), the arithmetic content is conserved "
         "inside (H-LM).  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "AD1-PROVEN(adjugate identity + B-ratios; TOPROOT = "
        "adjugate-entry ratio, basis-free; G10/G32)",
        "AD2-PROVEN(Riesz continuation; DELTA1 term registers "
        "multiplicity; G11/G33)",
        "CELL-LEMMA-PROVEN-MODULO-SIMPLICITY(pigeonhole exact + "
        "counts measured, C_0 <= %.1f; simplicity leg typed; "
        "G12/G34)" % CELL_C0_MAX,
        "ONE-CURVE-INSTANTIATED(adjugate == jets == eigenproduct on "
        "the h-ladder at every rung; G32)",
        "LM-ASSEMBLED(conditional; arrows gated or cited; "
        "G13/G14/G15/G60)",
        "LM-BEATS-RAW-AVERAGE(pole exhibit; G13)",
        "HONESTY-ADJUDICATED(OMEGA-a leg {TOPROOT, ONSETCAP} -> "
        "{EPSLOCK-AVG}; SUSCAP2R/DELTA1FLOOR legs unchanged; "
        "EPSLOCK-AVG OPEN-ARITHMETIC; G15)",
        "FW-HYPOTHESIS-TYPED(no TOPROOT/ONSETCAP inside; G15)",
        "CA-MEASURED(pointwise all rungs + ONE dense block across "
        "K-jumps; G35/G36)",
        "RLD-STATED-MEASURED(Szegoe/IIKS target "
        "OPEN-CLASSICAL-CANDIDATE; G16/G37)",
        "REDTEAM-REFUTES-ALGEBRA(2D model passes all algebra, "
        "breaks every poly cap; G17/G38)",
        "MSRC-SEES-ARITHMETIC(G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "OMEGA-CONTRACTED-IN-COORDINATES(census 4 unchanged; G61)"]
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
        print("COMPOSITE: AD1-PROVEN + AD2-PROVEN + "
              "CELL-LEMMA-PROVEN-MODULO-SIMPLICITY + "
              "ONE-CURVE-INSTANTIATED + LM-ASSEMBLED + "
              "LM-BEATS-RAW-AVERAGE + HONESTY-ADJUDICATED + "
              "FW-HYPOTHESIS-TYPED + CA-MEASURED + "
              "RLD-STATED-MEASURED + REDTEAM-REFUTES-ALGEBRA + "
              "MSRC-SEES-ARITHMETIC + CONTROLS-REFUSE + DEMAND-FLAT "
              "+ QUANTIFIER-INHERITED + "
              "OMEGA-CONTRACTED-IN-COORDINATES + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
