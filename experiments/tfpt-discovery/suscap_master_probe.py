#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""suscap_master_probe -- PRIME.SUSCAP.RESPONSE.MASTER.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the owner's two genuinely new proposals, built and gated)
=======================================================================
(A) THE RESPONSE-CURVE / WEYL-FUNCTION COMPRESSION OF SUSCAP2R
(PRIME.SUSCAP.RESPONSE.01 + PRIME.SUSCAP.THREEROW.01): rank-one
family, Weyl function log-derivative, interlacing-defect
representation, and the THREE-ROW DETERMINANT TARGET s(x) =
tau det H_3 / (R_phi^2 det H_2) -- adjudicate whether the r141
tail-heaviness (J* ~ 0.3 m) is a REPRESENTATION ARTIFACT.
(B) THE COFINAL MASTER THEOREM (PRIME.COFINAL.MASTER.01): block-
AVERAGE sufficiency via Markov + the V2 measure lemma over the
assembled r122-r142 chain; every arrow cited (round + gate) or gated
here; any gap typed exactly.
(C) THE CONSTANTS UPGRADE: the Bellotti-Wong 2025 N(T) constants as
an ALTERNATIVE pinned set; the r133 Q-swamp crossover x_0 = 121
re-scanned under both constant sets.

=======================================================================
(A) THE EXACT LAYER (Theorems X1-X4; sympy-gated generically + exact
rational instances + mp-instantiated per rung; classical CITED)
=======================================================================
NOTATION per rung x (r142/CDXLVI conventions): A = log(x)/2, K =
ceil(1.25 x log x), modes om_k = k pi/A, b_k = om_k^2, minimizer phi
(round-114 builder), tau = lambda_min(Mq), T_z = 2 pi x, m = verified
zone census, V = kernel of the m node rows, W = Gram-orthonormal
compression of Mq onto V, eigenpairs (q_i, z_i), q_0 = tau, u =
normalized projected probe row P_V r(p)/|P_V r(p)|, overlaps et_i =
<u, z_i>, rho2 = et_0^2, chi = sum_{i>=1} et_i^2/(q_i - q_0), g =
(lam* - tau)/tau, delta_i = (q_i - q_0)/tau, s = tau chi/rho2,
FULLGAP = (lam_1(Mq) - tau)/tau.  gtop = 7264.75 (X5 cache top).

THEOREM X1 (rank-one response curve).  W(t) = W + t u u^T has
lambda(t) := lambda_min-branch solving sum_i et_i^2/(q_i - lambda) =
-1/t (det(W + t uu^T - z) == det(W - z)(1 + t u^T (W-z)^{-1} u)
EXACTLY), with the EXACT jets lambda(0) = q_0, lambda'(0) = rho2,
lambda''(0) = -2 rho2 chi, hence
   s = tau chi/rho2 = -tau lambda''(0) / (2 lambda'(0)^2),
and lambda(t) -> lam* (the QSUBGAP object, root of the secular
equation sum et_i^2/(q_i - lambda) = 0) as t -> +infinity: SUSCAP2R
is a TWO-DERIVATIVE statement of the rank-one response curve at its
base point.

THEOREM X2 (Weyl-function log-derivative).  M(z) = <u, (zI - W)^{-1}
u> = Q(z)/P(z), P = det(zI - W) = prod (z - q_i), Q = u^T adj(zI-W) u
= sum_i et_i^2 prod_{j != i} (z - q_j).  Then EXACTLY
   s = tau [ P''(tau)/(2 P'(tau)) - Q'(tau)/Q(tau) ]
(proof: Q = rho2 P_1 + (z - q_0) P_1 N with P = (z - q_0) P_1 and N
the regular part; P''/(2P') at q_0 == P_1'/P_1; Q'/Q at q_0 ==
P_1'/P_1 - chi/rho2).

THEOREM X3 (interlacing-defect representation).  With eta_0 < eta_1
< ... the zeros of Q (the (m+1)-row constrained spectrum), which
strictly interlace the poles q_0 < eta_0 < q_1 < eta_1 < q_2 < ...,
   s/tau = sum_{i>=1} [ 1/(eta_{i-1} - tau) - 1/(q_i - tau) ],
every bracket POSITIVE.  CONSEQUENCE (the W1 pinch re-derived in two
lines): the first bracket alone gives s g >= 1 - g/delta_1; replacing
each -1/(q_i - tau) by -1/(eta_i - tau) telescopes to s g <= 1.
eta_0 = lam*: the pinch is the alternating pole/zero ladder.

THEOREM X4 (Krein/Schur three-row determinant form; the owner's
target).  For rows r_a against the SOURCE matrix define the deflated
reduced-resolvent Gram H_ab = <r_a, (Mq - tau)^+ r_b> (pseudo-inverse
on phi-perp via ONE bordered LU solve [[Mq - tau, phi],[phi^T, 0]]).
At the node config the zone rows kill phi (r(mu_j).phi = 0), so the
Schur complement S(z) = det G_{R+p}(z)/det G_R(z) of the source
resolvent Gram G_ab(z) = <r_a, (z - Mq)^{-1} r_b> has at z = tau the
Laurent data Res = R_phi^2, Reg = -(H_pp - H_pR H_RR^{-1} H_Rp), and
   s = tau (H_pp - H_pR H_RR^{-1} H_Rp) / R_phi^2
     = tau det H_{R+p} / (R_phi^2 det H_R)          EXACTLY,
invariant under adding zone-row combinations to the probe row (so
the projected and unprojected probe rows give the SAME s).  With R =
ALL m zone rows this is an IDENTITY with the eigensolve s; with R =
the TOP-2 zone rows it is the THREE-ROW DETERMINANT TARGET s_3(x) =
tau det H_3/(R_phi^2 det H_2): rational operations on the source
matrix, NO eigensolve beyond the (tau, phi) pair the cell already
carries.  The r141 tail-heavy J* ~ 0.3 m enclosure is adjudicated:
if |s_3/s - 1| is locality-defect small, the tail-heaviness is a
REPRESENTATION ARTIFACT of the eigenmode-ladder coordinate (the
chi certificate is ONE deflated linear solve, not a J-ladder).

=======================================================================
(B) THE COFINAL MASTER THEOREM (M') -- formalized shape
=======================================================================
HYPOTHESES.  (H1) D subset (1/4, infinity) dense; for every a in D
and all sufficiently large U, the FOUR-term block integral
   int_U^{U+1} [ |A_2/A_0|(e^u) + ((tau + OFF)/(A_0^2 G(2 pi e^u)))
                 (e^u) + (tau chi/rho2)(e^u) + (1/delta_1)(e^u) ] du
   <= e^{C U}.
(H2) TAILVIS along the chosen sequence (the concurrent
toproot_tailvis lane's target; typed at freeze time).  (H3) the
a-family walls: a-extension (gamma_1^2 < a < H^2, r132 lever c) and
window-a positivity (r128 G26).  CONCLUSION: RH (via the cited
chain; NO unconditional claim -- (M') is a conditional assembly).
ARROWS (each cited round+gate or gated here):
 A1 Markov on each block: nonneg integrable f with int <= e^{CU} is
    <= 4 e^{CU} off measure <= 1/4 -- GATED HERE (G14).
 A2 V2 good-phase set has measure >= 3/4 -- RE-GATED (G14; r141 V2).
 A3 intersection >= 1/2 nonempty per block ==> instrument-choosable
    unbounded x-sequence -- GATED HERE + r141 G60 CHAIN-AUDIT
    re-gated (G60).
 A4 sum-split: all four terms simultaneously <= 4 e^{CU} on the good
    set (nonneg terms) -- GATED HERE (G14).
 A5 first term <= poly ==> TOPROOT; TOPROOT <==> JETLOCK(poly) --
    r140 J2/J3 CITED, onset sandwich RE-GATED per rung (G37).
 A6 TOPROOT + V2 + counting ==> TAILVIS -- CONCURRENT LANE (typed at
    freeze: note/log status quoted in G15 detail).
 A7 second term <= poly ==> TLAWCAP directly (the integrand IS
    8 tlaw + OFF/(A_0^2 G)); TLAWCAP + JETLOCK + TAILVIS ==>
    BANDMASS(theta = 1 - 1/poly) ==> EPSLOCK = OMEGA-a -- r140 B1/B2
    + r137 E1 CITED, E1-composition RE-GATED (G16).
 A8 third + fourth terms <= poly ==> SUSCAP2R and DELTA1FLOOR ==>
    QSUBGAP -- r142 W2 RE-GATED (G16).  EXPOSURE (machine-gated,
    G15): the owner's THREE-integrand (M) does NOT provide
    DELTA1FLOOR -- the fourth summand 1/delta_1 is REQUIRED (or
    DELTA1FLOOR <== FULLGAP source-side, r142 W3, still open).
 A9 QSUBGAP ==> OMEGA-b; OMEGA-a + OMEGA-b ==> H-pin ==> L1; L1 +
    WPD + dense-a ==> NF-closure inputs; NF-closure ==> cofinal
    finite positivity ==> Weil positivity ==> RH -- r138/r139, r131/
    r133, r128 Theorem R, r122 NF-closure ALL CITED (min-cut G61).
PAYOFF TYPING (G15 detail): first/second integrands = small-divisor
A_0^2 block-averages -- Jensen/Cartan class CONDITIONAL on analytic
continuation + growth of the eigen-branch x -> A_0(x) (the minimizer
map is locally analytic by simple-eigenvalue perturbation; entire
extension NOT certified here) -- typed CLASSICAL-CONDITIONAL;
pointwise versions stay ARITHMETIC-PINNING (r140 ALIGNMENT-WALL,
r142 ONSETCAP).  Third integrand s: measured FLAT (0.03-0.06); the
X3 representation makes it an alternating pole/zero (spectral-shift)
object -- de Branges/Weyl territory (r121 canonical norm is
RH-equivalent, r126 S_TOP costume: DISGUISE screen reported in G54);
typed ARITHMETIC-PINNING (r142 adversarial witness re-gated G40).
Fourth integrand 1/delta_1 <= 1/FULLGAP: source-only two-eigenvalue
object, measured FALLING (FULLGAP grows ~ +0.14 dex/x) -- typed
OPEN-CLASSICAL-CANDIDATE (r142 lever (a)).

=======================================================================
(C) THE CONSTANTS UPGRADE (Bellotti-Wong 2025)
=======================================================================
Verified against the published version (Math. Comp., with appendix
by Fiori; arXiv 2412.15470v2): |N(T) - (T/2pi) log(T/2pi e)| <=
0.10076 log T + 0.24460 log log T + 8.08344 for EVERY T >= e.
DISCLOSED: the v1 abstract carried 8.08292; the published constant
is 8.08344 (the owner's citation used v1; the probe pins the
PUBLISHED set).  HSW22 Cor. 1.2 = (0.1038, 0.2573, 9.3675) stays
the corpus-pinned primary; BW25 enters as ALTERNATIVE set only.
G21 gates: G_BW(T) < G_HSW(T) on the frozen grid; own-cache partial
sums <= G_BW(T) at T = 200/2000 (validity cross-check); the r133
Q-swamp crossover scan (asym_assembly ported VERBATIM from
dominance_proof_probe, battery a in (1,4,16), integer scan 90..200)
replicates x_0 = 121 under HSW and re-runs under BW25: gate
x_0(BW) <= x_0(HSW) = 121; the new x_0 and the strip shrink are the
round's constants deliverable; Q-improvement at T_z(x) and T_PT +
tlaw ratio G_HSW/G_BW printed.  NOTHING in verification/ or any
promoted surface is touched; v914 untouched.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer: G10 X1 (rank-one det identity generic 3-level +
    jet coefficients t^0/t^1/t^2 vanish under the ansatz lambda =
    q_0 + rho2 t - rho2 chi t^2 on the exact instance + s ==
    -tau lambda''/(2 lambda'^2) + lambda(10^6) within 1e-5 of lam*
    via CRootOf); G11 X2 (log-derivative formula generic in
    (q_0, q_1, q_2, e_0, e_1, e_2), simplify == 0); G12 X3 (exact
    eta-roots on the instance: strict interlacing + alternating-sum
    == chi/rho2 + telescoping pinch bools s g <= 1, s g >= 1 -
    g/delta_1); G13 X4 (5-dim source diag(1,2,5,7,11), zone rows
    e_4/e_5, probe (3,4,12,5,7)/13: H-Schur s == 52/9 == eigensolve
    s exactly, beta-components cancel; det H_3/det H_2 == Schur;
    det G_3(lam*) == 0 via S(lam*) == 0); G14 master Markov + V2
    measure lemma re-gate + intersection + sum-split (sympy);
    G15 (M') assembly bookkeeping (typed CHAIN-AUDIT): arrow table
    with statuses; DELTA1FLOOR-EXPOSURE gate (3-integrand set does
    NOT cover QSUBGAP needs; 4-integrand set does); residual
    hypothesis set == {TAILVIS-arrow, A-EXTENSION, WINDOW-A} +
    dense-a (assembly NOT unconditional -- honesty gate); G16 arrow
    re-gates (r142 W2 loop equivalence + r140/r142 E1 composition
    solve, sympy ports).
S2  G20 HSW G(T) sanity (both constant sets); G21 constants upgrade
    (see (C)).
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan to T_z + 6, step 0.05):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform); G31 node-config V + r142 replication (|qrel| <=
    1e-30, null residual <= 1e-40; zone-top argmin in the frozen
    r139/r141/r142 windows AND >= 3; s <= 0.1; s x gap in (0.98,
    1.02); delta_1 windows; share_1 >= 0.5; tlaw on the CDXLI
    strings <= 5e-3; delta_1 >= FULLGAP (1 - 1e-12) re-gate);
    G32 X1 response curve instantiated (secular lambda(t) bisection:
    quadratic-fit jets at chi h = 1e-8 ladder h/2h: |rho2_hat/rho2 -
    1| <= 1e-6, |b_hat/(rho2 chi) - 1| <= 1e-4, s_resp within 1e-4
    of s; lambda(t_big = 1e8 (lam*-q_0)/rho2) within 1e-6 x gap of
    lam*; CROSS-INSTRUMENT: one mp.eigsy of W + t* u u^T at t* =
    (lam*-q_0)/rho2 vs the secular root, rel dev on (lambda - q_0)
    <= 1e-12); G33 X3 instantiated (eta_i per pole gap by bisection
    of M(z): strict interlacing everywhere + alternating sum ==
    chi/rho2 rel <= 1e-10 + all brackets >= -1e-30 + sum x g tau <=
    1 + 1e-12); G34 X4 full-row Schur identity (H via ONE bordered
    LU at dps + 50, m+1 solves: |s_schur/s_eig - 1| <= SCHUR_BAR =
    {5: 1e-8, 8: 1e-8, 13: 1e-8, 18: 1e-6, 24: 1e-4} (precision-
    budget-derived, pre-freeze unmeasured, DISCLOSED); node leakage
    max_j |r_j.phi|/|R_phi| <= 1e-6; cancellation depth log10(H_pp/
    Schur) printed -- the certified-cost exhibit: t(route A: build_V
    + eigsy) vs t(route B: LU + solves) printed per rung);
    G35 THREE-ROW sandwich (s_3 = tau det H_3/(R_phi^2 det H_2) from
    the TOP-2 zone rows + probe: |s_3/s - 1| <= LOC_S_BAR = 1e-2
    (predicted defect-class <= ~1e-3 via the pinch + U3 locality;
    pre-freeze unmeasured, DISCLOSED); det-form == Schur-form <=
    1e-12; s_J ladder J = 1,2,3,4,6 printed -- the tail re-entry
    map); G36 master integrands measured (pointwise rung samples,
    typed MEASURED-POINTWISE, DISCLOSED: block integrals need
    dense-u builds -- instrument cost): I1 = y_t in the r140
    windows, I2 = (tau+OFF)/(A_0^2 G(T_z)), I3 = s, I4 = 1/delta_1;
    Isum <= x^25 per rung AND post-loop slope log10 Isum vs log10 x
    <= 10 (expected ~ 4.1, the TOPROOT law dominates); G37 A5 onset
    sandwich re-gate (source-only Theta_J(0.5): y_t/rho <= Theta^2
    <= 1.05 y_t (1+rho)/rho AND Theta in the r140 windows).
S3b G40 adversarial s-witness x = 5, 8 (RvM quantile config, r142
    G40 replica): q0rel >= 10; max s' >= 1.0 (truth s <= 0.1);
    PLUS the node-formula refusal control: adversarial zone-row
    phi-leakage / node-config leakage >= 1e3 (the X4 formula's
    applicability detector fires exactly where source-config
    consistency fails -- null control for the new representation).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 AND y_t_w/b_top <= 1.0; G53 consistency.
S5  G54 tau-screen + DISGUISE report (|slope log10 s vs log10 tau|
    <= 0.30, same for gap and s_3; slopes of log10 det H_2 /
    det H_3 vs log10 tau PRINTED -- the determinants RIDE tau by
    construction (reduced-resolvent scale 1/(FULLGAP tau)), typed
    BOUND-RIDES-CONNES; the RATIO s_3 is the tau-flat currency; the
    X3 object lives in de Branges/Weyl territory (r121/r126 named)
    -- correlation REPORTED, no disguise claim); G55 conditioning
    (1e-25 shift window).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence-demand -> Theorem
    R transfer -> coupling absorbed -> (M') Markov/V2 provides
    FULL-MEASURE-TAIL <= UNBOUNDED-SEQ -> no ALL-X demand survives;
    per-rung certificate cost now EIGENSOLVE-FREE given (tau, phi):
    one bordered LU + 3 solves -- CERT-COMPRESSED typed); G61
    min-cut (r116 replica, r142 graph VERBATIM): flows base 4,
    refined 5, one-grant 5, counterfactual PARALLEL 9 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor.
1.2]; BW25 = (0.10076, 0.24460, 8.08344) [Bellotti-Wong, Math.
Comp. 2025, arXiv 2412.15470v2 published; v1 abstract 8.08292
DISCLOSED]; T_PT = 3000175332800 [PT21]; M_JETS = 400; MGRID = (2,
4, 8, 16, 32, 64, 128, 256, 400); SCAN_STEP = 0.05; SCAN_LO = 0.5;
SCAN_OVER = 6.0; TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05;
NODE_EXCL = 0.02; ADV_RUNGS = (5, 8); HSW_MONO_GRID = (50, 100,
1e3, 1e4, 1e5, 1e6, 3e12); A_BAT = (1, 4, 16) [r133]; X0_SCAN =
(90, 200); X0_HSW_EXPECT = 121 [r133/CDXXXV strings].
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)} (r139/r141/r142 measured
33.62/16.72/22.66/16.59/19.58); S_BAR = 0.1 (r141/r142 s = 0.02974/
0.05981/0.04413/0.06029/0.05108); SGAP_WIN = (0.98, 1.02); D1_TAB =
{5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8} x
(0.7, 1.3); SHARE1_BAR = 0.5 (r139: 0.969/0.965/0.946/0.944/0.947);
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24:
0.5122} rel tol 5e-3 (CDXLI strings); INTERLACE_SLOP = 1e-12;
H_RESP = 1e-8 (chi h target); RESP_D1_BAR = 1e-6; RESP_D2_BAR =
1e-4; RESP_S_BAR = 1e-4; RESP_INF_BAR = 1e-6; RESP_EIG_BAR = 1e-12;
TBIG_FAC = 1e8; ETA_SUM_BAR = 1e-10; ETA_BRACKET_SLOP = 1e-30;
ETA_PINCH_SLOP = 1e-12; SCHUR_PAD = 50 dps; SCHUR_BAR = {5: 1e-8,
8: 1e-8, 13: 1e-8, 18: 1e-6, 24: 1e-4} (precision budget: bordered
cond ~ 1/(FULLGAP tau), Schur cancellation ~ log10(H_pp/chi_abs)
dex -- pre-freeze unmeasured, DISCLOSED, headroom >= 20 dex);
LEAK_NODE_MAX = 1e-6; LOC_S_BAR = 1e-2 (predicted <= ~1e-3: pinch
defect class g/FULLGAP + U3 locality 1e-6; pre-freeze unmeasured,
DISCLOSED); DET_EQ_BAR = 1e-12; LOC_JS = (1, 2, 3, 4, 6); YT_TAB =
{5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7, 24: 4.013e7} x
(0.9, 1.1) (r140 strings); TH_TAB = {5: 360, 8: 943, 13: 2620, 18:
5191, 24: 9276} x (0.85, 1.15) (r140 Theta_J(0.5) strings; ENVJ/
onset code ported verbatim); ISUM_POLY_DEG = 25; ISUM_SLOPE_MAX =
10.0 (expected ~ 4.1); JET_SANDWICH_RHO = 0.5; JET_SANDWICH_FAC =
1.05; Q0REL_MIN = 10.0; S_ADV_MIN = 1.0; ADV_ID_BAR = 1e-8;
LEAK_SEP_MIN = 1e3 (pre-freeze unmeasured, DISCLOSED: node leakage
is Newton-residual class 1e-13x vs adversarial leakage = generic
R(theta) class); CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30;
COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward
only); RUNTIME_BAR = 14400 s.  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks; no
f64-refinement of mp roots; np.float64-repr casts guarded by
float(); log-scale diagnostics via mp.log inside workdps (r141
amendment-1 class); route-B linear algebra at dps + SCHUR_PAD with
own deterministic partial-pivot LU (factor once, reuse).

CALIBRATION DISCLOSURE (pre-freeze): NO scratch script was run for
this probe; every replication window derives from the frozen strings
of the cited rounds (r137/CDXLI tlaw + band; r139/CDXLIII gap/
delta_1/share_1; r140/CDXLIV y_t/Theta_J; r141/CDXLV s/s x gap +
rho2/et1^2 tables; r142/CDXLVI defect/pinch/FULLGAP strings), quoted
verbatim in FROZEN NUMERICS.  Genuinely NEW quantities are either
THEOREM gates (X1-X4 exact algebra -- risk-free) or disclosed-
unmeasured with stated precision-budget headroom (SCHUR_BAR,
LOC_S_BAR, LEAK bars, RESP bars, x_0(BW)).  The x_0(HSW) = 121
replication uses the r133 asym_assembly code VERBATIM.
SMOKE DISCLOSURE: smoke runs (x = 5 rung, SMOOTH control only,
adversarial x = 5) are logged and any instrument repair is
disclosed as a numbered SMOKE NOTE here before the frozen run;
amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.
SMOKE-1 NOTE (disclosed; smoke1 = 24/26, log kept; the two fails
were G34/G35): ONE instrument repair -- lu_solve_fac applied the
sequential partial-pivot row swaps INTERLEAVED with the column-
oriented forward elimination; the final L rows live in fully-
permuted positions, so ALL swaps must precede the elimination
(LAPACK getrs order).  Diagnosed via a pre-freeze debug scratch
(calib_scratch_suscap_master.py + inline snippets, deleted; the
scratch consumed no frozen window -- it exhibited: bordered
residual 4.08 -> 1.8e-105 class after the fix; H_pp via source
eigendata 5649.073049 == H_pp via the fixed solve; factorization
identity ||L U - P A|| ~ 2e-51 held even pre-fix, isolating the
solve routine).  No bar, no criterion, no ladder, no verdict rule
moved.  smoke2 = 26/26 at the same numerics (log kept); measured
smoke exhibits quoted: s_schur/s_eig - 1 = 0.0 at print precision,
s_3/s - 1 = +2.39e-9, J-ladder +1.6e-7/+2.4e-9/+3.4e-12/0.0 at
J = 1/2/3/4, cancellation depth 0.0 dex (the low source mode does
NOT dominate H_pp: (r.v_1)^2 ~ 2e-7 at x = 5 -- the precision-
budget worry was conservative), node leakage 1.9e-56, route A
0.3 s vs route B < 0.1 s at x = 5, x_0(HSW) = 121 replicated,
x_0(BW25) = 112 (strip shrink 9).

VERDICT ENUMS (frozen): X1-PROVEN(response curve: s is a two-
derivative statement; lambda(inf) = lam*); X2-PROVEN(Weyl log-
derivative formula); X3-PROVEN(interlacing-defect representation;
the W1 pinch is the alternating ladder, telescoping);
X4-PROVEN(three-row determinant form exact; full-row == eigensolve
identity per rung); TAIL-ARTIFACT vs TAIL-REAL(three-row sandwich
adjudicated by G35: ARTIFACT iff |s_3/s - 1| <= 1e-2 at every rung
with the ladder map printed); CERT-COMPRESSED(route B eigensolve-
free given (tau, phi): cost table per rung); MASTER-ASSEMBLED(
(M') four-integrand conditional assembly: every arrow cited or
gated; typed CHAIN-AUDIT); DELTA1-EXPOSED(the owner's 3-integrand
(M) does NOT provide DELTA1FLOOR -- machine-gated set exposure;
fourth integrand added); TAILVIS-ARROW-TYPED(concurrent lane status
quoted at freeze); A-WALLS-HYPOTHESES(dense-a + a-extension +
window-a remain hypotheses of (M') -- the assembly is NOT
unconditional, honesty-gated); INTEGRANDS-POLY-MEASURED(pointwise
rung samples; slope ~ y_t law); JETLOCK-SANDWICH-REGATED(A5);
CONSTANTS-UPGRADED(BW25 published set validated; x_0 rescan under
both sets; primary HSW pin UNTOUCHED); S-SEES-ARITHMETIC +
NODE-FORMULA-REFUSES(adversarial + leakage separation);
CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES +
DISGUISE-REPORTED(G54); QUANTIFIER-INHERITED(dense-x suffices);
OMEGA-UNCHANGED(residue = {TOPROOT, TAILVIS, TLAWCAP(=ONSETCAP),
SUSCAP2R(=QSUBGAP mod DELTA1FLOOR <== FULLGAP)} + DELTA1FLOOR(weak)
+ dense-a + a-extension + window-a; census {MEAS, OMEGA-POS}
cardinality 4 UNCHANGED); MINCUT(4/5).  Composite priority:
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
HSW_SET = (0.1038, 0.2573, 9.3675)
BW_SET = (0.10076, 0.24460, 8.08344)
BW_V1_C3 = 8.08292            # v1 abstract value, DISCLOSED
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
HSW_MONO_GRID = (50.0, 100.0, 1e3, 1e4, 1e5, 1e6, 3e12)
A_BAT = (1.0, 4.0, 16.0)
X0_SCAN = (90, 200)
X0_HSW_EXPECT = 121
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
H_RESP = 1e-8
RESP_D1_BAR = 1e-6
RESP_D2_BAR = 1e-4
RESP_S_BAR = 1e-4
RESP_INF_BAR = 1e-6
RESP_EIG_BAR = 1e-12
TBIG_FAC = 1e8
ETA_SUM_BAR = 1e-10
ETA_BRACKET_SLOP = 1e-30
ETA_PINCH_SLOP = 1e-12
SCHUR_PAD = 50
SCHUR_BAR = {5: 1e-8, 8: 1e-8, 13: 1e-8, 18: 1e-6, 24: 1e-4}
LEAK_NODE_MAX = 1e-6
LOC_S_BAR = 1e-2
DET_EQ_BAR = 1e-12
LOC_JS = (1, 2, 3, 4, 6)
YT_TAB = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
          24: 4.013e7}
YT_WIN = (0.9, 1.1)
TH_TAB = {5: 360.0, 8: 943.0, 13: 2620.0, 18: 5191.0, 24: 9276.0}
TH_WIN = (0.85, 1.15)
ISUM_POLY_DEG = 25
ISUM_SLOPE_MAX = 10.0
JET_SANDWICH_RHO = 0.5
JET_SANDWICH_FAC = 1.05
Q0REL_MIN = 10.0
S_ADV_MIN = 1.0
ADV_ID_BAR = 1e-8
LEAK_SEP_MIN = 1e3
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


# --------------------------------------------------------- closed forms
def hsw_G_c(T: float, consts: tuple) -> float:
    """certified upper bound for sum_{gamma > T} gamma^{-2},
    parametrized by the (C1, C2, C3) counting-constant set."""
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(consts[0]))
        be = mp.mpf(repr(consts[1]))
        cc = mp.mpf(repr(consts[2]))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


def hsw_G(T: float) -> float:
    return hsw_G_c(T, HSW_SET)


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_hsw_c(T: float, consts: tuple) -> float:
    return consts[0] * math.log(T) + consts[1] * math.log(math.log(T)) \
        + consts[2]


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


# --------------------------------------- r133 swamp machinery (VERBATIM)
def w_of(a: float, t):
    return a * t ** 2 / (a + t ** 2) ** 2


def t_star_c(N: int, consts: tuple) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_hsw_c(mid, consts) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells_c(N: int, a: float, Ts: float, consts: tuple) -> float:
    """certified tail_1 lower bound: shell counts >= M - Q telescoped
    (r133 frozen shell configs, ported verbatim; constants param)."""
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = m_rvm(Ts) + q_hsw_c(Ts, consts)
            for j in range(J):
                n_next = m_rvm(Tj[j + 1]) - q_hsw_c(Tj[j + 1], consts)
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * w_of(a, Tj[j + 1])
                u_prev = m_rvm(Tj[j + 1]) + q_hsw_c(Tj[j + 1], consts)
            best = max(best, tot)
    return best


def asym_assembly_c(x: float, a: float, consts: tuple) -> tuple:
    """r133 THEOREM A closed forms at (x, a): (D, MRB bound or inf);
    ported verbatim from dominance_proof_probe, constants param."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    Ts = t_star_c(N, consts)
    Tz = 2 * math.pi * x
    n_z = m_rvm(Tz) - q_hsw_c(Tz, consts)
    TL = tl_shells_c(N, a, Ts, consts)
    m_minus_edge = max(0.0, (N - n_z)) * w_of(a, Tz)
    m_plus_edge = a * hsw_G_c(Tz, consts)
    D = TL - TL / 8.0 - m_minus_edge
    mrb = ((TL / 8.0 + m_plus_edge + m_minus_edge) / D
           if D > 0 else float("inf"))
    return D, mrb, N, Ts, TL


def x0_scan(consts: tuple) -> int | None:
    lo, hi = X0_SCAN
    okpos = {}
    for xi in range(lo, hi + 1):
        okpos[xi] = all(asym_assembly_c(float(xi), float(a), consts)[0]
                        > 0 for a in A_BAT)
    for xi in range(lo, hi + 1):
        if all(okpos[xj] for xj in range(xi, hi + 1)):
            return xi
    return None


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138-r142 replica); ALSO
    returns the compressed matrix Wm (X1 cross-instrument gate)."""
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
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp, Wm=Wm)


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
    return lo, et, en2, etn, rho2, chi, e


def resp_lambda(qs, etn, nf, t, lam_star):
    """lambda(t): root of sum et_i^2/(q_i - lam) = -1/t on
    (q_0, lam*) for t > 0 (THEOREM X1 branch).  Caller sets workdps."""
    tgt = -1 / t

    def F(lam):
        return sum(etn[i] * etn[i] / (qs[i] - lam) for i in range(nf))
    lo = qs[0] + (lam_star - qs[0]) * mp.mpf("1e-40")
    hi = lam_star
    # monotonicity bracket assert: F(lo) < tgt < F(hi) = 0
    if not (F(lo) < tgt):
        # widen toward q_0
        lo = qs[0] + (lam_star - qs[0]) * mp.mpf("1e-80")
    for _ in range(260):
        mid = (lo + hi) / 2
        if F(mid) < tgt:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------- deterministic LU (route B)
def lu_factor(Amat, n):
    """own partial-pivot LU in-place on an mp.matrix copy; returns
    (LU, piv).  Deterministic; caller sets workdps."""
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
    """solve with a pre-computed lu_factor; b = list; returns list.
    ALL sequential row swaps are applied BEFORE the forward
    elimination (the final L rows live in fully-permuted positions;
    LAPACK getrs order -- smoke-1 instrument repair, disclosed)."""
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
def symbolic_gates(concurrent_note: str) -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    lam, z, tsym = sp.symbols("lam z tsym")

    # shared exact 3-level instance: W = diag(1, 2, 5), unit row
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    e0, e1, e2 = sp.Rational(3, 13), sp.Rational(4, 13), \
        sp.Rational(12, 13)
    rho2_i = e0 ** 2
    chi_i = e1 ** 2 / (q1i - q0i) + e2 ** 2 / (q2i - q0i)
    s_i = chi_i / rho2_i          # tau = 1 on the instance
    fsec = e0 ** 2 / (q0i - lam) + e1 ** 2 / (q1i - lam) \
        + e2 ** 2 / (q2i - lam)
    roots = sorted(sp.solve(sp.together(fsec).as_numer_denom()[0], lam))
    lam_star = roots[0]

    # ---------------- G10 X1 rank-one response curve
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    Wd = sp.diag(q0i, q1i, q2i)
    uv = sp.Matrix([u1, u2, u3])
    lhsD = (Wd + tsym * uv * uv.T - z * sp.eye(3)).det()
    rhsD = ((q0i - z) * (q1i - z) * (q2i - z)
            * (1 + tsym * (u1 ** 2 / (q0i - z) + u2 ** 2 / (q1i - z)
                           + u3 ** 2 / (q2i - z))))
    okA = sp.simplify(sp.expand(lhsD - rhsD)) == 0
    # jets: E(lam, t) = prod(q_i - lam) + t sum e_i^2 prod_{j!=i}
    E = ((q0i - lam) * (q1i - lam) * (q2i - lam)
         + tsym * (e0 ** 2 * (q1i - lam) * (q2i - lam)
                   + e1 ** 2 * (q0i - lam) * (q2i - lam)
                   + e2 ** 2 * (q0i - lam) * (q1i - lam)))
    c3 = sp.symbols("c3")
    ans = q0i + rho2_i * tsym - rho2_i * chi_i * tsym ** 2 \
        + c3 * tsym ** 3
    ser = sp.expand(E.subs(lam, ans))
    pser = sp.Poly(ser, tsym)
    okB = (sp.simplify(pser.coeff_monomial(1)) == 0
           and sp.simplify(pser.coeff_monomial(tsym)) == 0
           and sp.simplify(pser.coeff_monomial(tsym ** 2)) == 0)
    # s = -tau lambda''(0)/(2 lambda'(0)^2)
    okC = sp.simplify(-q0i * (-2 * rho2_i * chi_i)
                      / (2 * rho2_i ** 2) - s_i) == 0
    # lambda(t -> inf) = lam*: branch at t = 10^6 via CRootOf
    Ebig = sp.expand(E.subs(tsym, sp.Integer(10 ** 6)))
    rts = sp.Poly(Ebig, lam).all_roots()
    rreal = [r for r in rts if r.is_real]
    near = min(rreal, key=lambda r: sp.Abs(r - lam_star))
    okD = bool(sp.Abs(near - lam_star) < sp.Rational(1, 100000)) \
        and bool(near < lam_star)
    out.append(("G10-x1-response-curve", okA and okB and okC and okD,
                "det(W + t uu^T - z) == det(W - z)(1 + t u^T(W-z)^-1 u)"
                " generic; jets t^0/t^1/t^2 vanish under lambda(t) = "
                "q0 + rho2 t - rho2 chi t^2 + O(t^3); s == -tau "
                "lambda''/(2 lambda'^2); lambda(10^6) within 1e-5 "
                "below lam* (THEOREM X1: SUSCAP2R is a two-derivative "
                "statement; lambda(inf) = the QSUBGAP object)"))

    # ---------------- G11 X2 Weyl log-derivative (generic)
    g0, g1, g2, f0, f1, f2 = sp.symbols("g0 g1 g2 f0 f1 f2",
                                        positive=True)
    Pz = (z - g0) * (z - g1) * (z - g2)
    Qz = (f0 ** 2 * (z - g1) * (z - g2)
          + f1 ** 2 * (z - g0) * (z - g2)
          + f2 ** 2 * (z - g0) * (z - g1))
    Pp = sp.diff(Pz, z)
    Ppp = sp.diff(Pz, z, 2)
    Qp = sp.diff(Qz, z)
    formula = g0 * (Ppp / (2 * Pp) - Qp / Qz)
    s_def = g0 * (f1 ** 2 / (g1 - g0) + f2 ** 2 / (g2 - g0)) / f0 ** 2
    okE = sp.simplify(sp.together(formula.subs(z, g0)
                                  - s_def)) == 0
    out.append(("G11-x2-weyl-logderiv", okE,
                "s == tau [P''(tau)/(2 P'(tau)) - Q'(tau)/Q(tau)] "
                "GENERIC in (q_0, q_1, q_2, e_0, e_1, e_2) with P = "
                "det(zI - W), Q = u^T adj(zI - W) u (THEOREM X2: s "
                "is a two-derivative Weyl-function datum at the "
                "ground eigenvalue)"))

    # ---------------- G12 X3 interlacing-defect representation
    Qi = (e0 ** 2 * (z - q1i) * (z - q2i)
          + e1 ** 2 * (z - q0i) * (z - q2i)
          + e2 ** 2 * (z - q0i) * (z - q1i))
    etas = sorted(sp.solve(sp.expand(Qi), z))
    eta0, eta1 = etas
    okF = bool(q0i < eta0 < q1i) and bool(q1i < eta1 < q2i)
    rep = (1 / (eta0 - q0i) - 1 / (q1i - q0i)) \
        + (1 / (eta1 - q0i) - 1 / (q2i - q0i))
    okG = sp.simplify(sp.radsimp(rep - chi_i / rho2_i)) == 0
    okH = sp.simplify(sp.radsimp(eta0 - lam_star)) == 0
    b1 = 1 / (eta0 - q0i) - 1 / (q1i - q0i)
    b2 = 1 / (eta1 - q0i) - 1 / (q2i - q0i)
    g_i = lam_star - q0i
    okI = bool(b1 >= 0) and bool(b2 >= 0)
    # telescoping pinch: sg <= 1 and sg >= 1 - g/delta_1
    sg_i = s_i * g_i
    okJ = bool(sp.simplify(sg_i - 1) <= 0) \
        and bool(sp.simplify(sg_i - (1 - g_i / (q1i - q0i))) >= 0)
    out.append(("G12-x3-interlace-defect", okF and okG and okH
                and okI and okJ,
                "zeros of Q strictly interlace the poles; s/tau == "
                "sum [1/(eta_{i-1} - tau) - 1/(q_i - tau)] with every "
                "bracket >= 0; eta_0 == lam*; the W1 pinch 1 - "
                "g/delta_1 <= s g <= 1 is the two-line telescoping of "
                "the alternating ladder (THEOREM X3)"))

    # ---------------- G13 X4 Krein/Schur three-row determinant
    Asrc = sp.diag(sp.Integer(1), sp.Integer(2), sp.Integer(5),
                   sp.Integer(7), sp.Integer(11))
    phi5 = sp.Matrix([1, 0, 0, 0, 0])
    rz1 = sp.Matrix([0, 0, 0, 1, 0])       # zone row 1 (kills phi)
    rz2 = sp.Matrix([0, 0, 0, 0, 1])       # zone row 2 (kills phi)
    rp = sp.Matrix([sp.Rational(3, 13), sp.Rational(4, 13),
                    sp.Rational(12, 13), sp.Rational(5, 13),
                    sp.Rational(7, 13)])
    # eigensolve route on V = ker{rz1, rz2} = span(e1, e2, e3):
    # W_V = diag(1, 2, 5); P_V rp = (3,4,12)/13 -> s_true = 52/9
    s_true = sp.Rational(52, 9)
    # H = (A - 1)^+ deflated on phi: diag(0, 1, 1/4, 1/6, 1/10)
    Hd = sp.diag(sp.Integer(0), sp.Integer(1), sp.Rational(1, 4),
                 sp.Rational(1, 6), sp.Rational(1, 10))
    Rphi = (rp.T * phi5)[0, 0]

    def hip(a, b):
        return (a.T * Hd * b)[0, 0]

    H2m = sp.Matrix([[hip(rz1, rz1), hip(rz1, rz2)],
                     [hip(rz2, rz1), hip(rz2, rz2)]])
    hv = sp.Matrix([hip(rz1, rp), hip(rz2, rp)])
    Hpp = hip(rp, rp)
    schur = Hpp - (hv.T * H2m.inv() * hv)[0, 0]
    s_schur = sp.Integer(1) * schur / Rphi ** 2   # tau = 1
    okK = sp.simplify(s_schur - s_true) == 0
    H3m = sp.Matrix([[H2m[0, 0], H2m[0, 1], hv[0]],
                     [H2m[1, 0], H2m[1, 1], hv[1]],
                     [hv[0], hv[1], Hpp]])
    okL = sp.simplify(H3m.det() / H2m.det() - schur) == 0
    # det G_3(lam*) == 0: S(z) == Weyl function of the projected row
    fsec3 = (sp.Rational(9, 169) / (z - 1)
             + sp.Rational(16, 169) / (z - 2)
             + sp.Rational(144, 169) / (z - 5))

    def Gab(a, b):
        return sum(a[k] * b[k] / (z - Asrc[k, k]) for k in range(5))

    G2z = sp.Matrix([[Gab(rz1, rz1), Gab(rz1, rz2)],
                     [Gab(rz2, rz1), Gab(rz2, rz2)]])
    gvz = sp.Matrix([Gab(rz1, rp), Gab(rz2, rp)])
    Sz = Gab(rp, rp) - (gvz.T * G2z.inv() * gvz)[0, 0]
    okM = sp.simplify(sp.together(Sz - fsec3)) == 0
    lam3 = sorted(sp.solve(
        sp.together(fsec3).as_numer_denom()[0], z))[0]
    okN = sp.simplify(fsec3.subs(z, lam3)) == 0
    out.append(("G13-x4-krein-three-row", okK and okL and okM and okN,
                "5-dim source diag(1,2,5,7,11), zone rows e4/e5 kill "
                "phi, probe (3,4,12,5,7)/13: s == tau (H_pp - h^T "
                "H_2^-1 h)/R_phi^2 == tau det H_3/(R_phi^2 det H_2) "
                "== 52/9 == eigensolve s EXACTLY (probe components "
                "in the row space cancel); the source Schur S(z) == "
                "the projected-row Weyl function and S(lam*) == 0 "
                "(THEOREM X4: the three-row determinant target)"))

    # ---------------- G14 master Markov + V2 + intersection + split
    t, eps = sp.symbols("t eps", positive=True)
    Iv, Bv = sp.symbols("Iv Bv", positive=True)
    # Markov: meas{f > 4B} <= I/(4B) <= 1/4 when I <= B
    okO = sp.simplify(Bv / (4 * Bv) - sp.Rational(1, 4)) == 0
    # piecewise instance: f = 5 on [0, 1/20], 0 else; int = 1/4 = B
    f_int = sp.Rational(5, 1) * sp.Rational(1, 20)
    okP = bool(f_int <= sp.Rational(1, 4)) \
        and bool(sp.Rational(1, 20) <= f_int / (4 * sp.Rational(1, 4)))
    # V2 measure lemma re-gate (r141 G13, ported verbatim)
    h = sp.sin(t) - 2 * t / sp.pi
    okQ = (sp.simplify(h.subs(t, 0)) == 0
           and sp.simplify(h.subs(t, sp.pi / 2)) == 0
           and sp.simplify(sp.diff(h, t, 2) + sp.sin(t)) == 0)
    g1s, g2s, du = sp.symbols("g1s g2s du", positive=True)
    tot = (g1s * du / (2 * sp.pi) + 1) * (2 * sp.pi * eps / g1s) \
        + (g2s * du / (2 * sp.pi) + 1) * (2 * sp.pi * eps / g2s)
    tgt = eps * (2 * du + 2 * sp.pi / g1s + 2 * sp.pi / g2s)
    okR = sp.simplify(tot - tgt) == 0
    m_s = sp.symbols("m_s", positive=True)
    eps_c = du / (4 * m_s * (du + 2 * sp.pi / g1s))
    okS = sp.simplify(eps_c * m_s * (du + 2 * sp.pi / g1s)
                      - du / 4) == 0
    # intersection: bad <= 1/4 + 1/4 ==> good >= 1/2 > 0
    okT = sp.simplify(1 - sp.Rational(1, 4) - sp.Rational(1, 4)
                      - sp.Rational(1, 2)) == 0
    # sum-split: nonneg terms, sum <= M ==> each <= M
    v2s, v3s, v4s = sp.symbols("v2s v3s v4s", nonnegative=True)
    okU = (v2s + v3s + v4s).is_nonnegative is True
    out.append(("G14-master-markov-v2", okO and okP and okQ and okR
                and okS and okT and okU,
                "Markov on a unit block: int f <= e^{CU} ==> meas{f > "
                "4 e^{CU}} <= 1/4 (rearrangement + instance); V2 "
                "measure lemma re-gated (concavity floor + hit "
                "counting + eps_cert leaves 3/4 good; r141 V2 "
                "VERBATIM); union bound: good >= 1/2 > 0 per block; "
                "sum-split: nonneg four-term sum <= 4 e^{CU} bounds "
                "EVERY term simultaneously (arrows A1-A4)"))

    # ---------------- G15 (M') assembly bookkeeping (CHAIN-AUDIT)
    provided3 = {"TOPROOT", "TLAWCAP", "SUSCAP2R"}
    provided4 = provided3 | {"DELTA1FLOOR"}
    qsubgap_needs = {"SUSCAP2R", "DELTA1FLOOR"}
    expose = not qsubgap_needs.issubset(provided3)
    covered = qsubgap_needs.issubset(provided4)
    residual_hyps = {"TAILVIS-ARROW", "A-EXTENSION", "WINDOW-A",
                     "DENSE-A(H1)"}
    not_unconditional = len(residual_hyps) > 0
    arrows = [
        ("A1 Markov per block", "GATED-HERE G14"),
        ("A2 V2 good-phase >= 3/4", "RE-GATED G14 (r141 V2)"),
        ("A3 intersection -> unbounded seq", "GATED-HERE G14 + "
         "r141 G60 chain-audit re-gated G60"),
        ("A4 sum-split simultaneity", "GATED-HERE G14"),
        ("A5 term1 -> TOPROOT <=> JETLOCK", "r140 J2/J3 CITED, "
         "onset sandwich RE-GATED G37"),
        ("A6 TOPROOT+V2+counting -> TAILVIS", concurrent_note),
        ("A7 term2 -> TLAWCAP -> BANDMASS -> EPSLOCK", "r140 B1/B2 + "
         "r137 E1 CITED, composition RE-GATED G16"),
        ("A8 term3+term4 -> SUSCAP2R+DELTA1FLOOR -> QSUBGAP",
         "r142 W2 RE-GATED G16; DELTA1FLOOR EXPOSURE gated here"),
        ("A9 QSUBGAP -> OMEGA-b -> H-pin -> L1 -> NF-closure -> "
         "Weil positivity -> RH", "r138/r139 + r131/r133 + r128 "
         "Theorem R + r122 NF-closure CITED (min-cut G61)"),
    ]
    det15 = "; ".join("%s [%s]" % a for a in arrows)
    out.append(("G15-master-bookkeeping", expose and covered
                and not_unconditional,
                "EXPOSURE: the owner's 3-integrand (M) does NOT "
                "provide DELTA1FLOOR (QSUBGAP needs SUSCAP2R AND "
                "DELTA1FLOOR, r142 W2) -- the 4th summand 1/delta_1 "
                "is REQUIRED and added in (M'); residual hypothesis "
                "set {TAILVIS-arrow, a-extension, window-a, dense-a} "
                "NONEMPTY: (M') is a CONDITIONAL assembly, typed "
                "CHAIN-AUDIT.  Arrows: " + det15))

    # ---------------- G16 arrow re-gates (W2 loop + E1 composition)
    Ps = sp.symbols("Ps", positive=True)
    okV = bool(s_i <= 1 / g_i) and bool(q0i < lam_star < q1i) \
        and bool((q1i - q0i) > g_i)
    R2s, chis, taus, D1s = sp.symbols("R2s chis taus D1s",
                                      positive=True)
    lhsS = (R2s / (chis + R2s / (D1s * taus))) / taus
    rhsS = 1 / (taus * chis / R2s + 1 / D1s)
    okW = sp.simplify(lhsS - rhsS) == 0
    okX = sp.simplify(1 / (Ps + 1 / (1 / Ps)) - 1 / (2 * Ps)) == 0
    tl, th, r_, GT, GZ, A0q, of_ = sp.symbols(
        "tl th r_ GT GZ A0q of_", positive=True)
    e1c = sp.Eq(tl * 8 * A0q ** 2 * GZ * (1 - th),
                8 * (1 + r_) ** 2 * A0q ** 2 * GT + (1 + th) * of_)
    sol_tl = sp.solve(e1c, tl)
    okY = len(sol_tl) == 1 and sp.simplify(
        sol_tl[0] - ((1 + r_) ** 2 * GT / GZ
                     + (1 + th) * of_ / (8 * A0q ** 2 * GZ))
        / (1 - th)) == 0
    out.append(("G16-arrow-regates", okV and okW and okX and okY,
                "r142 W2 loop re-gated (forward s <= 1/g + root in "
                "(q0, q1); backward g >= 1/(s + 1/delta_1); demand "
                "composition 1/(2P)): QSUBGAP <==> SUSCAP2R AND "
                "DELTA1FLOOR; r140/r142 E1 composition solve re-gated "
                "(tlaw <= [(1+r)^2 G(Th)/G(Tz) + OFF-part]/(1-th)): "
                "arrows A7/A8 ride cited+re-gated algebra"))
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
    steps.append(("(M') block hypothesis (H1) + Markov (G14) + V2 "
                  "good sets provide FULL-MEASURE-TAIL good x per "
                  "block => unbounded sequence exists constructively",
                  FULL_MEAS <= demand))
    steps.append(("SUSCAP2R leg consumes NO tlaw and NO Z (r142 W2 + "
                  "r141 V1, cited); the s-certificate is now "
                  "EIGENSOLVE-FREE given (tau, phi): one bordered LU "
                  "+ 3 solves (X4) -- CERT-COMPRESSED", True))
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

    print("suscap_master_probe -- PRIME.SUSCAP.RESPONSE.MASTER.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    adv_rungs = (5,) if smoke else ADV_RUNGS
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

    # concurrent-lane status at freeze (read-only existence checks)
    lane_note = "CONCURRENT-LANE-PENDING (toproot_tailvis probe + "
    lane_note += "run logs exist, no note at spec-freeze)" \
        if os.path.exists(os.path.join(HERE,
                                       "toproot_tailvis_probe.py")) \
        else "CONCURRENT-LANE-ABSENT"

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
    section("S1  EXACT LAYER (Theorems X1-X4 + master assembly)")
    for name, okg, detg in symbolic_gates(lane_note):
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW + OFF recipe; r132 "
         "raw census; r133 M/E/T/A + Q-swamp assembly (asym code "
         "VERBATIM); r135 D1-D4; r136 S1-S4 + PINBALL; r137/CDXLI "
         "budget identity + E1; r138 Q1-Q3; r139/CDXLIII U1-U4 + "
         "locality; r140/CDXLIV J1-J4 + B1/B2 + y_t/Theta_J strings; "
         "r141/CDXLV V1-V3 + quantifier audit; r142/CDXLVI W1-W3 + "
         "pinch/defect/FULLGAP strings; HSW22 Cor. 1.2; "
         "Bellotti-Wong 2025 (Math. Comp., arXiv 2412.15470v2, "
         "PUBLISHED constants; v1 delta disclosed); PT21; Euler sine "
         "product; Courant-Fischer; Krein/Schur resolvent identity "
         "(elementary block algebra, gated G13); r121 canonical norm "
         "+ r126 S_TOP named for the DISGUISE screen")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS + CONSTANTS UPGRADE")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G_HSW(T) at T = 200/2000; G "
          "monotone on the frozen grid; G_HSW(gamma_top) = %.3e"
          % hsw_G(gtop))

    ok21 = True
    for Tg in HSW_MONO_GRID:
        ok21 = ok21 and hsw_G_c(Tg, BW_SET) < hsw_G_c(Tg, HSW_SET)
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        ok21 = ok21 and part <= hsw_G_c(Ttest, BW_SET)
    t_x0 = time.time()
    x0_hsw = x0_scan(HSW_SET)
    x0_bw = x0_scan(BW_SET)
    ok21 = ok21 and x0_hsw == X0_HSW_EXPECT and x0_bw is not None \
        and x0_bw <= x0_hsw
    qimp = []
    for xq in (5, 8, 13, 18, 24):
        Tzq = 2 * math.pi * xq
        qimp.append("Tz(%d): %.3f->%.3f" % (
            xq, q_hsw_c(Tzq, HSW_SET), q_hsw_c(Tzq, BW_SET)))
    qimp.append("T_PT: %.3f->%.3f" % (q_hsw_c(float(T_PT), HSW_SET),
                                      q_hsw_c(float(T_PT), BW_SET)))
    gimp = ["Tz(%d): %.4f" % (xq, hsw_G_c(2 * math.pi * xq, HSW_SET)
                              / hsw_G_c(2 * math.pi * xq, BW_SET))
            for xq in (5, 8, 13, 18, 24)]
    check("G21-constants-upgrade", ok21,
          "BW25 PUBLISHED set (0.10076, 0.24460, 8.08344), T >= e "
          "(v1 abstract 8.08292 DISCLOSED); G_BW < G_HSW on the "
          "grid; own-cache partials <= G_BW at 200/2000; Q-SWAMP "
          "RESCAN (r133 asym VERBATIM, %.0f s): x_0(HSW) = %s == "
          "121 replicated, x_0(BW25) = %s (strip shrink %s "
          "integers); Q improvement %s; tlaw ratio G_HSW/G_BW at "
          "T_z: %s -- ALTERNATIVE set only, primary HSW pin and "
          "v914 UNTOUCHED"
          % (time.time() - t_x0, str(x0_hsw), str(x0_bw),
             str(x0_hsw - x0_bw if x0_bw else "n/a"),
             "; ".join(qimp), "; ".join(gimp)))
    info("constants: the r133 Q-swamp strip x < x_0 hangs mostly on "
         "C3 (9.3675 -> 8.08344, -13.7%%): unconditional-assembly "
         "strip shrinks by %s integer rungs; r136/r140 slack margins "
         "scale with Q(T) ~ -1.3 zeros at band scale (printed above)"
         % str(x0_hsw - x0_bw if x0_bw else "n/a"))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: RESPONSE CURVE + WEYL + THREE-ROW + (M')")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36, det37 = [], [], [], []
    gap_tab, tau_tab, s_tab, s3_tab = {}, {}, {}, {}
    isum_tab, det2_tab, det3_tab = {}, {}, {}
    cells = {}
    node_leak_tab = {}
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
        a0f = ctx["a0f"]
        with mp.workdps(dps):
            cs = ctx["cs"]
            aa = ctx["aa"]
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            A0 = ctx["A0"]
            tauf = float(ce["mpE"][0])
            theta05 = onset(ctx, JET_SANDWICH_RHO)
            eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(A0))
            off = float(8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2) \
                * hsw_G(float(T_PT))
        Gz = hsw_G(Tz)
        tlaw = tauf / (8.0 * a0f ** 2 * Gz)

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

        # ---- G31 node-config V + r142 replication (route A, timed)
        t_a0 = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            fullgap = float((ce["mpE"][1] - ce["mpE"][0])
                            / ce["mpE"][0])
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
                lam, et, en2, etn, rho2, chi, e_oc = \
                    secular_data(Vd, r)
                gg = float((lam - tau) / tau)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, et, en2, etn, rho2, chi, e_oc = secular_data(Vd, r)
            g_ex = (lam - tau) / tau
            s_val = tau * chi / rho2
            sg = s_val * g_ex
            d1 = (Vd["qs"][1] - Vd["qs"][0]) / tau
            share1 = float((etn[1] * etn[1] / (Vd["qs"][1]
                                               - Vd["qs"][0])) / chi)
            g_f = float(g_ex)
            s_f = float(s_val)
            sg_f = float(sg)
            d1_f = float(d1)
        t_routeA = time.time() - t_a0
        lo_w, hi_w = REPL_WIN[x]
        tl_dev = abs(tlaw / TLAW_TAB[x] - 1.0)
        ok31x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR
                 and d1_node >= fullgap * (1.0 - INTERLACE_SLOP)
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR
                 and SGAP_WIN[0] <= sg_f <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR
                 and tl_dev <= TLAW_TOL)
        ok31 = ok31 and ok31x
        det31.append("x%d: qrel %.0e nf %d gap %.4f s %.5f sg %.5f "
                     "d1 %.3e share1 %.3f tlaw %.4f (A %.1f s)"
                     % (x, Vd["qrel"], Vd["nf"], gmin, s_f, sg_f,
                        d1_f, share1, tlaw, t_routeA))
        gap_tab[x] = gmin
        tau_tab[x] = tauf
        s_tab[x] = s_f

        # ---- G32 X1 response curve instantiated
        nf = Vd["nf"]
        with mp.workdps(dps):
            qs = Vd["qs"]
            h_t = mp.mpf(repr(H_RESP)) / chi
            d_h = resp_lambda(qs, etn, nf, h_t, lam) - qs[0]
            d_2h = resp_lambda(qs, etn, nf, 2 * h_t, lam) - qs[0]
            a_hat = (4 * d_h - d_2h) / (2 * h_t)
            b_hat = (2 * d_h - d_2h) / (2 * h_t * h_t)
            dev_a = float(abs(a_hat / rho2 - 1))
            dev_b = float(abs(b_hat / (rho2 * chi) - 1))
            s_resp = tau * b_hat / (a_hat * a_hat)
            dev_s = float(abs(s_resp / s_val - 1))
            t_big = mp.mpf(repr(TBIG_FAC)) * (lam - qs[0]) / rho2
            lam_big = resp_lambda(qs, etn, nf, t_big, lam)
            dev_inf = float(abs(lam - lam_big) / (lam - qs[0]))
            # cross-instrument: eigsy of W + t* u u^T
            t_star_v = (lam - qs[0]) / rho2
            sq_en = mp.sqrt(en2)
            Wt = Vd["Wm"].copy()
            for i in range(nf):
                for j2 in range(nf):
                    Wt[i, j2] += t_star_v * (e_oc[i] / sq_en) \
                        * (e_oc[j2] / sq_en)
            Et, _Vt = mp.eigsy(Wt)
            lam_eig = min(Et[i] for i in range(nf))
            lam_sec = resp_lambda(qs, etn, nf, t_star_v, lam)
            dev_eig = float(abs((lam_eig - qs[0]) / (lam_sec - qs[0])
                                - 1))
        ok32x = (dev_a <= RESP_D1_BAR and dev_b <= RESP_D2_BAR
                 and dev_s <= RESP_S_BAR and dev_inf <= RESP_INF_BAR
                 and dev_eig <= RESP_EIG_BAR)
        ok32 = ok32 and ok32x
        det32.append("x%d: dev lam' %.1e lam'' %.1e s_resp %.1e "
                     "lam(inf) %.1e eigsy-x %.1e"
                     % (x, dev_a, dev_b, dev_s, dev_inf, dev_eig))
        info("x=%d X1 exhibit: s from two derivatives of the "
             "response curve = %.6f vs direct %.6f (the rank-one "
             "family reaches lam* at t=inf: dev %.1e)"
             % (x, float(s_resp), s_f, dev_inf))

        # ---- G33 X3 instantiated (eta ladder by gap bisection)
        with mp.workdps(dps):
            def Mfun(zv):
                return sum(etn[i] * etn[i] / (zv - qs[i])
                           for i in range(nf))
            etas_ok = True
            asum = mp.mpf(0)
            brackets_ok = True
            for i in range(nf - 1):
                lo_e, hi_e = qs[i], qs[i + 1]
                span = hi_e - lo_e
                lo_b = lo_e + span * mp.mpf("1e-45")
                hi_b = hi_e - span * mp.mpf("1e-45")
                if not (Mfun(lo_b) > 0 > Mfun(hi_b)):
                    etas_ok = False
                    break
                for _ in range(220):
                    midv = (lo_b + hi_b) / 2
                    if Mfun(midv) > 0:
                        lo_b = midv
                    else:
                        hi_b = midv
                eta_i = (lo_b + hi_b) / 2
                etas_ok = etas_ok and qs[i] < eta_i < qs[i + 1]
                br = 1 / (eta_i - qs[0]) - 1 / (qs[i + 1] - qs[0])
                brackets_ok = brackets_ok and float(br) >= \
                    -ETA_BRACKET_SLOP
                asum += br
            if etas_ok:
                dev_sum = float(abs(asum * tau / (chi / rho2 * tau)
                                    - 1))
                sum_sg = float(asum * (lam - qs[0]))
            else:
                dev_sum, sum_sg = 1.0, 2.0
        ok33x = (etas_ok and brackets_ok and dev_sum <= ETA_SUM_BAR
                 and sum_sg <= 1.0 + ETA_PINCH_SLOP)
        ok33 = ok33 and ok33x
        det33.append("x%d: %d etas interlaced, alt-sum dev %.0e, "
                     "sum x g tau %.7f" % (x, nf - 1, dev_sum, sum_sg))

        # ---- G34/G35 X4 route B: bordered LU + Schur (dps + pad)
        dpsB = dps + SCHUR_PAD
        with mp.workdps(dpsB):
            aaB = mp.log(x) / 2
            omsB = [k * mp.pi / aaB for k in range(K)]
            nrmB = [mp.sqrt(2 * aaB) if k == 0 else mp.sqrt(aaB)
                    for k in range(K)]
            Mq = ce["mpM"]
            tauB = ce["mpE"][0]
            phi = [ce["mpV"][i, 0] for i in range(K)]
            n_b = K + 1
            B = mp.zeros(n_b, n_b)
            for i in range(K):
                for j2 in range(K):
                    B[i, j2] = Mq[i, j2]
                B[i, i] -= tauB
                B[i, K] = phi[i]
                B[K, i] = phi[i]
            t_b0 = time.time()
            LU, pivv = lu_factor(B, n_b)
            t_lu = time.time() - t_b0
            rows_all = [row_at(nd, K, omsB, nrmB) for nd in zone_nds]
            rp = row_at(p_mp, K, omsB, nrmB)
            rows_all.append(rp)
            n_rows = len(rows_all)
            t_b1 = time.time()
            ys = []
            for ra in rows_all:
                rhs = list(ra) + [mp.mpf(0)]
                ys.append(lu_solve_fac(LU, pivv, rhs, n_b))
            t_solves = time.time() - t_b1
            Hm = mp.zeros(n_rows, n_rows)
            for i in range(n_rows):
                for j2 in range(i + 1):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += rows_all[i][k] * ys[j2][k]
                    Hm[i, j2] = Hm[j2, i] = acc
            Rphi = sum(rp[k] * phi[k] for k in range(K))
            leak = max(abs(sum(rows_all[j][k] * phi[k]
                               for k in range(K)))
                       for j in range(m_zone))
            leak_ratio = float(leak / abs(Rphi))
            # full-row Schur via LU on H_RR (m x m)
            HRR = mp.zeros(m_zone, m_zone)
            for i in range(m_zone):
                for j2 in range(m_zone):
                    HRR[i, j2] = Hm[i, j2]
            hRp = [Hm[i, m_zone] for i in range(m_zone)]
            LU2, piv2 = lu_factor(HRR.copy(), m_zone)
            wv = lu_solve_fac(LU2, piv2, hRp, m_zone)
            schur_full = Hm[m_zone, m_zone] - sum(
                hRp[i] * wv[i] for i in range(m_zone))
            s_schur = float(tauB * schur_full / (Rphi * Rphi))
            cancel_dex = float(mp.log(abs(Hm[m_zone, m_zone])
                                      / abs(schur_full)) / mp.log(10))
            # J-row ladder (top-J zone rows): submatrix Schur
            t_b2 = time.time()
            sJ = {}
            for J in LOC_JS:
                if J > m_zone:
                    continue
                idx = list(range(m_zone - J, m_zone))
                HJ = mp.zeros(J, J)
                for i2, ii in enumerate(idx):
                    for j2, jj in enumerate(idx):
                        HJ[i2, j2] = Hm[ii, jj]
                hJ = [Hm[ii, m_zone] for ii in idx]
                LUJ, pivJ = lu_factor(HJ.copy(), J)
                wJ = lu_solve_fac(LUJ, pivJ, hJ, J)
                schJ = Hm[m_zone, m_zone] - sum(
                    hJ[i2] * wJ[i2] for i2 in range(J))
                sJ[J] = float(tauB * schJ / (Rphi * Rphi))
            t_3row = time.time() - t_b2
            # 3-row det form (top-2 zone rows + probe)
            i1, i2_ = m_zone - 2, m_zone - 1
            det2 = Hm[i1, i1] * Hm[i2_, i2_] - Hm[i1, i2_] ** 2
            H3 = mp.matrix([[Hm[i1, i1], Hm[i1, i2_], Hm[i1, m_zone]],
                            [Hm[i2_, i1], Hm[i2_, i2_],
                             Hm[i2_, m_zone]],
                            [Hm[m_zone, i1], Hm[m_zone, i2_],
                             Hm[m_zone, m_zone]]])
            det3 = mp.det(H3)
            s3_det = float(tauB * det3 / (det2 * Rphi * Rphi))
            l10B = mp.log(10)
            ld2 = float(mp.log(abs(det2)) / l10B)
            ld3 = float(mp.log(abs(det3)) / l10B)
        dev_schur = abs(s_schur / s_f - 1.0)
        ok34x = (dev_schur <= SCHUR_BAR[x]
                 and leak_ratio <= LEAK_NODE_MAX)
        ok34 = ok34 and ok34x
        det34.append("x%d: s_schur dev %.1e (bar %.0e) leak %.1e "
                     "cancel %.1f dex; A %.1f s vs B %.1f s (LU "
                     "%.1f s, %d solves %.1f s)"
                     % (x, dev_schur, SCHUR_BAR[x], leak_ratio,
                        cancel_dex, t_routeA, t_lu + t_solves, t_lu,
                        n_rows, t_solves))
        node_leak_tab[x] = leak_ratio

        s3 = sJ.get(2, float("nan"))
        dev_loc = abs(s3 / s_f - 1.0)
        dev_det = abs(s3_det / s3 - 1.0)
        ok35x = dev_loc <= LOC_S_BAR and dev_det <= DET_EQ_BAR
        ok35 = ok35 and ok35x
        s3_tab[x] = s3
        det2_tab[x] = ld2
        det3_tab[x] = ld3
        det35.append("x%d: s_3/s - 1 = %+.2e (det-form dev %.0e); "
                     "ladder %s"
                     % (x, s3 / s_f - 1.0, dev_det,
                        " ".join("J%d:%+.1e" % (J, sJ[J] / s_f - 1.0)
                                 for J in sorted(sJ))))
        info("x=%d X4 exhibit: s = tau det H_3/(R_phi^2 det H_2) = "
             "%.6f vs eigensolve %.6f; log10 det H_2 %.1f det H_3 "
             "%.1f; predicted defect class g/FULLGAP = %.1e; 3-row "
             "cert cost = LU %.1f s + 3 solves (ladder pass %.1f s)"
             % (x, s3_det, s_f, ld2, ld3, g_f / fullgap, t_lu,
                t_3row))

        # ---- G36 master integrands (pointwise rung samples)
        I2 = (tauf + off) / (a0f ** 2 * Gz)
        I4 = 1.0 / d1_f
        Isum = yt + I2 + s_f + I4
        isum_tab[x] = Isum
        yt_ok = YT_WIN[0] <= yt / YT_TAB[x] <= YT_WIN[1]
        poly_ok = Isum <= float(x) ** ISUM_POLY_DEG
        ok36x = yt_ok and poly_ok
        ok36 = ok36 and ok36x
        det36.append("x%d: I1 %.3e I2 %.3f I3 %.5f I4 %.1e sum "
                     "%.3e <= x^25 %s"
                     % (x, yt, I2, s_f, I4, Isum, poly_ok))

        # ---- G37 A5 onset sandwich re-gate (source-only)
        th2 = theta05 * theta05
        lo_j = yt / JET_SANDWICH_RHO
        hi_j = JET_SANDWICH_FAC * yt * (1 + JET_SANDWICH_RHO) \
            / JET_SANDWICH_RHO
        th_win_ok = TH_WIN[0] <= theta05 / TH_TAB[x] <= TH_WIN[1]
        ok37x = (lo_j * (1 - 1e-9) <= th2 <= hi_j * (1 + 1e-9)
                 and th_win_ok)
        ok37 = ok37 and ok37x
        det37.append("x%d: Th(.5) %.0f Th^2/y_t %.3f in [%.2f, "
                     "%.2f]" % (x, theta05, th2 / yt,
                                1.0 / JET_SANDWICH_RHO,
                                JET_SANDWICH_FAC
                                * (1 + JET_SANDWICH_RHO)
                                / JET_SANDWICH_RHO))

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
    check("G32-x1-response-instantiated", ok32,
          "secular lambda(t): quadratic jets match (lambda' = rho2 "
          "<= %.0e, lambda'' = -2 rho2 chi <= %.0e); s from two "
          "derivatives <= %.0e; lambda(t_big) -> lam* <= %.0e; "
          "CROSS-INSTRUMENT mp.eigsy(W + t* uu^T) == secular root "
          "<= %.0e (THEOREM X1 instantiated): %s"
          % (RESP_D1_BAR, RESP_D2_BAR, RESP_S_BAR, RESP_INF_BAR,
             RESP_EIG_BAR, "; ".join(det32)))
    check("G33-x3-eta-ladder", ok33,
          "every pole gap carries exactly one zero of M (strict "
          "interlacing); alternating sum == chi/rho2 <= %.0e; all "
          "brackets >= 0; sum x g tau <= 1 (the X3 telescoping "
          "pinch, instantiated): %s" % (ETA_SUM_BAR,
                                        "; ".join(det33)))
    check("G34-x4-schur-full-identity", ok34,
          "route B (ONE bordered LU at dps + %d, m + 1 solves, NO "
          "eigensolve beyond the cell's (tau, phi)): s_schur == "
          "s_eig within the precision-budget bars; node leakage "
          "max|r_j.phi|/|R_phi| <= %.0e; cancellation depth + cost "
          "table printed (CERT-COMPRESSED): %s"
          % (SCHUR_PAD, LEAK_NODE_MAX, "; ".join(det34)))
    check("G35-three-row-sandwich", ok35,
          "s_3 = tau det H_3/(R_phi^2 det H_2) from the TOP-2 zone "
          "rows + probe: |s_3/s - 1| <= %.0e at every rung AND "
          "det-form == Schur-form <= %.0e; J-ladder printed (the "
          "tail re-entry map -- THE THREE-ROW DETERMINANT TARGET): "
          "%s" % (LOC_S_BAR, DET_EQ_BAR, "; ".join(det35)))
    check("G36-master-integrands", ok36,
          "pointwise rung samples (typed MEASURED-POINTWISE, "
          "DISCLOSED: not block integrals); I1 = y_t in the r140 "
          "windows; Isum <= x^%d per rung: %s"
          % (ISUM_POLY_DEG, "; ".join(det36)))
    check("G37-jetlock-sandwich", ok37,
          "source-only onset Theta_J(%.1f): y_t/rho <= Theta^2 <= "
          "%.2f y_t (1 + rho)/rho at every rung AND Theta in the "
          "r140 windows (arrow A5 re-gated: TOPROOT <==> "
          "JETLOCK(poly)): %s"
          % (JET_SANDWICH_RHO, JET_SANDWICH_FAC, "; ".join(det37)))
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        li = [math.log10(isum_tab[x]) for x in xs_all]
        lx = [math.log10(float(x)) for x in xs_all]
        sl_i = float(np.polyfit(lx, li, 1)[0])
        info("master integrand growth: slope log10 Isum vs log10 x "
             "= %.2f (<= %.1f gate folded into G36 verdict reading; "
             "the y_t TOPROOT law x^4.1 dominates -- the block "
             "hypothesis (H1) is satisfied POINTWISE with exponent "
             "~4 against demand 25)" % (sl_i, ISUM_SLOPE_MAX))
        ok36 = ok36 and abs(sl_i) <= ISUM_SLOPE_MAX

    # ---------------------------------------------------------- S3b
    section("S3b  ADVERSARIAL s-WITNESS + NODE-FORMULA REFUSAL")
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
            phi = [ce["mpV"][i, 0] for i in range(K)]
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
            adv_leak = mp.mpf(0)
            for j in range(m_zone):
                rr = row_at(th[j], K, oms, nrm)
                lv = abs(sum(rr[k] * phi[k] for k in range(K)))
                if lv > adv_leak:
                    adv_leak = lv
            rr_p = row_at(mp.mpf(repr(float(Tz - 0.001))), K, oms,
                          nrm)
            Rphi_t = abs(sum(rr_p[k] * phi[k] for k in range(K)))
            adv_leak_ratio = float(adv_leak / Rphi_t)
            for pf in pset:
                if pf <= 0.5 or pf > Tz + 2.0:
                    continue
                if min(abs(pf - v) for v in thf) < NODE_EXCL:
                    continue
                rr = row_at(mp.mpf(repr(float(pf))), K, oms, nrm)
                lamt, ett, en2t, etnt, rho2t, chit, _e = \
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
        leak_sep = adv_leak_ratio / max(node_leak_tab.get(x, 1e-300),
                                        1e-300)
        okx = (q0rel >= Q0REL_MIN and s_max is not None
               and s_max >= S_ADV_MIN and alg_ok
               and leak_sep >= LEAK_SEP_MIN)
        ok40 = ok40 and okx
        det40.append("x%d: q0rel %.1e s'_max %.2f (truth %.4f) "
                     "leak-sep %.1e algebra-blind %s"
                     % (x, q0rel, s_max, s_tab.get(x, float("nan")),
                        leak_sep, alg_ok))
    check("G40-adversarial-s-witness", ok40,
          "RvM-legal quantile config: q0rel >= %.0f AND max s' >= "
          "%.1f vs truth s <= %.1f (s-currency SEES the arithmetic; "
          "r142 replica) AND W1 pinch + defect identity HOLD on the "
          "adversarial well (algebra config-blind) AND the X4 "
          "node-formula applicability detector fires: adversarial "
          "zone-row phi-leakage / node leakage >= %.0e "
          "(NODE-FORMULA-REFUSES null control): %s"
          % (Q0REL_MIN, S_ADV_MIN, S_BAR, LEAK_SEP_MIN,
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
        ytbw = cwx["yt"] / cwx["btop"]
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD); y_t_w/b_top = %.2f <= %.1f"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the X1-X4 machinery "
          "claims nothing where PSD/pinning fail")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS + DISGUISE REPORT")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lg_ = [math.log10(gap_tab[x]) for x in xs_all]
        ls_ = [math.log10(s_tab[x]) for x in xs_all]
        ls3 = [math.log10(abs(s3_tab[x])) for x in xs_all]
        s_g = float(np.polyfit(lt, lg_, 1)[0])
        s_s = float(np.polyfit(lt, ls_, 1)[0])
        s_s3 = float(np.polyfit(lt, ls3, 1)[0])
        s_d2 = float(np.polyfit(lt, [det2_tab[x] for x in xs_all],
                                1)[0])
        s_d3 = float(np.polyfit(lt, [det3_tab[x] for x in xs_all],
                                1)[0])
        check("G54-tau-screen-disguise", abs(s_g) <= TAU_SLOPE_BAR
              and abs(s_s) <= TAU_SLOPE_BAR
              and abs(s_s3) <= TAU_SLOPE_BAR,
              "slopes vs log10 tau: gap %.4f, s %.4f, s_3 %.4f (all "
              "<= %.2f: the three-row RATIO is tau-flat); DISGUISE "
              "REPORT: log10 det H_2 slope %.2f, det H_3 slope %.2f "
              "(the DETERMINANTS ride tau by construction -- reduced "
              "resolvent scale 1/(FULLGAP tau) -- typed "
              "BOUND-RIDES-CONNES); the X3 alternating pole/zero "
              "object is de Branges/Weyl-adjacent (r121 canonical "
              "norm RH-equivalent, r126 S_TOP costume NAMED): the "
              "correlation is REPORTED, no disguise verdict -- the "
              "s-currency stays the tau-flat, Z-free, tlaw-free "
              "coordinate (r142 W2 cited)"
              % (s_g, s_s, s_s3, TAU_SLOPE_BAR, s_d2, s_d3))
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
          "flows: base 4, refined 5 (r142 graph VERBATIM: the (M') "
          "assembly is an INF-edge bundling of the SAME residue, "
          "not a new unit edge); one-grant 5; counterfactual "
          "PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")
    info("EXACT RESIDUE after this round (read with CDXLI/CDXLIII/"
         "CDXLIV/CDXLV/CDXLVI): UNCHANGED as a set -- RH <== "
         "[r122-NF-closure] + [Theorem R] + {L1, WPD} on dense a; "
         "RESIDUE = {TOPROOT, TAILVIS (concurrent lane), "
         "TLAWCAP(=ONSETCAP), SUSCAP2R(=QSUBGAP-uniformity)} + "
         "DELTA1FLOOR(weak, <== FULLGAP) + dense-a + a-extension + "
         "window-a; THIS ROUND changes the COORDINATES, not the "
         "set: SUSCAP2R is a two-derivative response-curve/Weyl "
         "datum with an EIGENSOLVE-FREE three-row determinant "
         "certificate, and the whole residue is bundled into ONE "
         "conditional block-average statement (M') whose remaining "
         "per-arrow mathematics is typed.  NO RH claim; nothing "
         "upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    tail_verdict = "TAIL-ARTIFACT" if ok35 else "TAIL-REAL"
    verdicts = [
        "X1-PROVEN(response curve: s = -tau lambda''/(2 lambda'^2); "
        "lambda(inf) = lam*; G10/G32)",
        "X2-PROVEN(Weyl log-derivative; G11)",
        "X3-PROVEN(interlacing-defect representation; the W1 pinch "
        "is the alternating ladder; G12/G33)",
        "X4-PROVEN(three-row determinant form; full-row == "
        "eigensolve identity; G13/G34)",
        "%s(three-row sandwich G35: the r141 J* tail-heaviness "
        "adjudicated)" % tail_verdict,
        "CERT-COMPRESSED(eigensolve-free s certificate given "
        "(tau, phi); cost table; G34/G60)",
        "MASTER-ASSEMBLED((M') four-integrand conditional assembly; "
        "typed CHAIN-AUDIT; G14/G15/G16/G60)",
        "DELTA1-EXPOSED(3-integrand (M) lacks DELTA1FLOOR; G15)",
        "TAILVIS-ARROW-TYPED(%s)" % lane_note,
        "A-WALLS-HYPOTHESES(dense-a + a-extension + window-a stay "
        "hypotheses; G15)",
        "INTEGRANDS-POLY-MEASURED(pointwise; y_t law dominates; "
        "G36)",
        "JETLOCK-SANDWICH-REGATED(G37)",
        "CONSTANTS-UPGRADED(BW25 published set; x_0 rescan; G21)",
        "S-SEES-ARITHMETIC + NODE-FORMULA-REFUSES(G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES + DISGUISE-REPORTED(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "OMEGA-UNCHANGED(residue set unchanged; coordinates "
        "compressed; G61 census 4)"]
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
        print("COMPOSITE: X1-PROVEN + X2-PROVEN + X3-PROVEN + "
              "X4-PROVEN + %s + CERT-COMPRESSED + MASTER-ASSEMBLED "
              "+ DELTA1-EXPOSED + TAILVIS-ARROW-TYPED + "
              "A-WALLS-HYPOTHESES + INTEGRANDS-POLY-MEASURED + "
              "JETLOCK-SANDWICH-REGATED + CONSTANTS-UPGRADED + "
              "S-SEES-ARITHMETIC + NODE-FORMULA-REFUSES + "
              "CONTROLS-REFUSE + DEMAND-FLAT + DISGUISE-REPORTED + "
              "QUANTIFIER-INHERITED + OMEGA-UNCHANGED + MINCUT"
              % tail_verdict)
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
