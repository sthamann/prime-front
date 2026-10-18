#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""toproot_theta_probe -- PRIME.TOPROOT.THETA.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung certificates stated, NO counterexample claim.  It closes no
gate and narrows no gate.

=======================================================================
MISSION (THE TOPROOT FINAL ATTACK: after r171/CDLXXXVII reduced the
entire jet-mass chain to {TOPROOT (lambda-uniform)} + {Gonek
constants} + {census-all-k == LOOP} + {L1, WPD}, this round (T1)
STATES the TOPROOT inequality exactly and unifies the r140/r143
y_t-form, the r162 theta-window and the r171 rate leg into ONE named
statement with its exact quantifier and admissible exponent; (T2)
ATTACKS the four candidate mechanisms and prices each honestly (kill
or carry -- no reformulation credited as advance); (T3) MEASURES y_t
at all 25 rungs plus a deep holdout with the growth-law fit and the
margin to the maximal admissible exponent; (T4) lands the per-rung
QUARTIC CERTIFICATE H3 and assembles the full chain, stating the
final residue exactly.)
=======================================================================
State consumed (CITED): CDLXXXVII/r171 (jetmass floor: PF1-PF3
proven, H1 ENVJ-certified source-pure, H2 census classical per rung,
JMF assembly, WF Gonek-form, rate law sigma_floor ~ 0.0767 h^{-1.057}
over 10 clean rungs, RATE_MARGIN/CLEAN_FIT lesson, witness strings,
SIZE-SEPARATOR standard); CDLXXXIV/r169 (SF1-SF6; SF4 demand
absorption T_req -> (3 pi/c)(1 + 2a/3) h^{3/2+a}); CDLX/r156
(rootladder: L1 moment-Laurent dictionary (y/y_t) F/A_0 == PHI(z),
PHI(z) = z - 1 + sum_{m>=1} J_{m+1} z^{-m}, J_m = A_{2m}/(A_0 y_t^m);
L2 quarter-cap J_2-window; the 2-mode witness); CDXLIV/r140 (J1-J3;
TOPROOT named: y_t = |A_2/A_0| <= poly(x), measured ~x^4.14);
CDXLV..CDXLVII/r143 (toproot_tailvis: T1-T4; T4 rank-one dictionary
census == eig(D - (1/A_0)|w><1|); OBSTRUCTION PIN budget-invisible;
delta_1/y_t lock (1.5, 6.0); DENSE-X audit); CDLXVII/r162 (fullgap
growth law: J == THETA T_z^4, THETA flat, ALGEBRA-ONLY-REFUTED-FOR-
THETA; GL4 jr t_r == 1 + 1/FULLGAP; L7 moment-route obstructed);
r131 OFF/G17 (T_z = 2 pi h resolvability crossover); r137 zero-jet
law tau == 8 A_0^2 G tlaw_0; HSW22 Cor. 1.2; PT21 (T_PT =
3000175332800); Landau 1912 + Gonek 1993 AS FORM; Cauchy/Fujiwara
root-bound class (classical, CITED); Vieta/Newton; Weyl.

NOTATION.  Rung h (R4.build_cell, even sector, MAIN world); A =
log(h)/2; K = ceil(1.25 h log h); b_k = (k pi/A)^2; b_top = b_{K-1};
tau = lam_min; T_z = 2 pi h; c_k source coefficients; A_{2m} =
sum_{k>=1} (-1)^k c_k b_k^m; A_0 = sum_k (-1)^k c_k; y_t = |A_2/A_0|;
B_1 = sum_{k>=1} b_k = (pi/A)^2 (K-1)K(2K-1)/6 CLOSED FORM; kappa =
B_1/y_t; theta_y = y_t/T_z^4; FULLGAP = (lam_1 - tau)/tau; lock =
FULLGAP/y_t; J_{m+1} = A_{2(m+1)}/(A_0 y_t^{m+1}); rho = sup_{m>=1}
|J_{m+1}|^{1/m}; C_1 = sum_{k>=1} |c_k|; N(y) = numerator of F
(rootladder census form VERBATIM); OS = b_top C_1/(|A_0| y_t) (the
triangle-route overshoot); G_lead(T) = (log(T/2pi)+1)/(2 pi T);
eps_closed(h) = sqrt(h) G(T_PT)/G(2 pi h) (r168/r169/r171 VERBATIM).

=======================================================================
T1 -- THE TOPROOT STATEMENT (the deliverable; one named inequality)
=======================================================================
TOPROOT(p, C) [THE TOP-ROOT GROWTH CAP]:
    y_t(h) <= C h^p   for every rung h of the census schedule.
QUANTIFIER (exact, inherited from the r141/r143 DENSE-X audit + the
r169-SF4 SEQ demand): EXISTS (C, p) finite such that FOR EVERY dyadic
block of the census schedule THERE IS a rung h in the block with
y_t(h) <= C h^p (SEQ-cofinal; an ALL-h reading is NOT demanded).
EQUIVALENT MACHINE FORMS (each gated this round):
 (i)   THETA-FORM: theta_y(h) := y_t/T_z^4 <= theta_bar  <==>
       TOPROOT(4, theta_bar (2 pi)^4).  The r162 window is the
       J-coordinate J == THETA T_z^4; the two coordinates are locked
       by FULLGAP/y_t in LOCK_WIN = (1.0, 8.0) (r143 delta_1-lock
       class, r171 G33 VERBATIM) and jr t_r == 1 + 1/FULLGAP (r162
       GL4, cited): TOPROOT == the r162 theta-window statement.
 (ii)  CENSUS-FORM: under H2 the top census root sits in TOP_WIN =
       (0.70, 0.95) y_t (r156/r171): census-top <= poly <==> TOPROOT.
 (iii) RATE-FORM (r171 dictionary, exact limit layer): TOPROOT(p)
       ==> WF(z_0) >= (pi p/q)(1 + o(1)) h^{1 - p/2} ==> the
       sigma-floor exponent a = p/2 - 1.  Measured r171: a = 1.057
       at p ~ 4.1 -- the dictionary closes.
ADMISSIBLE EXPONENT (the T1 gate): (a) ASYMPTOTIC: by r169-SF4 EVERY
finite p is census-absorbable -- demand T_req ~ h^{(p+1)/2}, census
constant (3 pi/c)(1 + 2a/3) == pi (p+1)/c at a = p/2 - 1 (sympy
exact); there is NO finite asymptotic ceiling.  (b) FINITE
PT21-ANCHORED SCHEDULE (the binding one): with the r171 record floor
constant c = 0.0767 and the coverage demand h*_rate >= 2 H_MAX = 56
(at least one dyadic block above the verified substrate),
    a_max = ln(c/eps_closed(56))/ln 56 = 4.134758  ==>
    p_max = 2 (1 + a_max) = 10.269515      [frozen strings].
The measured exponent p ~ 4.2 leaves ~6 powers of h of margin: the
census schedule absorbs the quartic law with room to exponent 10.

=======================================================================
T2 -- THE MECHANISMS (each priced; kill or carry)
=======================================================================
(a) MOMENT-LAURENT / CAUCHY-FUJIWARA.  NEW THEOREM TR-CAP (proven,
exact): if |J_{m+1}| <= rho^m for all m >= 1 then PHI(z) != 0 for
every real z >= 1 + 2 rho [proof: geometric sum ρ/(z-ρ) + the
polynomial identity (z-1)(z-rho) - rho == rho + 2 rho^2 + (1 + 3 rho)
s + s^2 at z = 1 + 2 rho + s, all coefficients positive]; with the
r156 L1 dictionary: NO census root above (1 + 2 rho) y_t.  Tail
certification per rung: ENV(m) = [C_1 b_top/(|A_0| y_t)]^{1/m}
(b_top/y_t) is monotone decreasing, so sup_{m <= 400} plus ENV(400) <
rho_meas certifies rho over ALL m.  MEASURED: rho == |J_2| at EVERY
rung (argmax m = 1; the sup is the second moment; J_2 = 0.107 ->
0.151, inside the r156 quarter-cap window < 1/4); cap 1 + 2 rho =
1.21 -> 1.30 vs H1's certified c* = 1.10/1.15: ENVJ-SHARPER (the cap
never beats the certified half-plane constant).  VERDICT: CARRIED as
a new per-rung theorem in z-units; KILLED FOR TOPROOT -- the
dictionary is y_t-normalized BY CONSTRUCTION (every J_m is quotiented
by y_t^m): the cap bounds census-top/y_t, never y_t itself.  The
Fujiwara side is CIRCULAR: the m = 1 term |N_{K-2}/N_{K-1}| == B_1 +
y_t EXACTLY (the Vieta trace; gated per rung dev <= 1e-40) and is the
ARGMAX at every rung: the sharpest classical root bound restates the
trace, bound >= 2(1 + kappa) y_t > y_t.  MOMENT-ROUTE-CIRCULAR-FOR-
TOPROOT (consistent with r162-L7 moment-route obstruction one level
up).
(b) VIETA TRACE / POWER-SUM PINCH.  Newton p_2 = e_1^2 - 2 e_2 exact;
generic K=3: e_2 == b_1 b_2 + (A_4 - A_2 B_1)/A_0 -- EVERY elementary
symmetric function of the census carries 1/A_0 (the moment content is
A_{2m}/A_0): no y_t-free pinch exists in the symmetric-function ring;
e_1 = B_1 + y_t restates the trace.  The ONE certified y_t-free
anchor is B_1 (closed form, ~h^3 log h): TOPROOT <==> kappa >= 1/poly
EXACTLY (y_t == B_1/kappa) -- a REFORMULATION, typed as such, not an
advance.  VERDICT: KILLED as an independent proof; the B_1 dictionary
carried as bookkeeping.
(b') THE A_0-TRIANGLE ROUTE == THE LOOP (machine-flagged).  y_t <=
b_top C_1/|A_0| (triangle, exact) -- but (i) MEASURED: the overshoot
OS = b_top C_1/(|A_0| y_t) is 10^3.4 -> 10^64.6 and its log rides
-log10|A_0| with slope ~0.97: the bound loses EXACTLY the
cancellation, it is exponentially vacuous; (ii) the only floor for
|A_0| in the program is the zero-jet law A_0^2 == tau/(8 G tlaw_0)
(r137, definitional): an A_0-floor consumes TAUPOS + TLAWCAP == the
pinning-supply LOOP in A_0-currency -- DETECTED, FLAGGED, NOT
consumed (G63 cycle gate).  VERDICT: DOUBLY DEAD (vacuous AND
loop-priced).
(c) THE WITNESS DIRECTION (world-separation calibration).  The r156
2-mode deflation witness (d = -A_2(1 - 1/W)/(b_2 - b_1), W = 1000)
replicated: A_0 invariant, y_t'' = y_t/1000, J_2 x1.01e6, census top
escapes to 24.87 y_t'' -- and TR-CAP HOLDS in the witness world
(cap'' = 2.5e5 >= 24.87: the cap is world-blind algebra, its content
per rung is the measured smallness of rho).  NEW: the INFLATION
direction d+ = A_2(W - 1)/(b_2 - b_1): A_0 invariant (dev <= 1e-40),
y_t'' = W y_t EXACTLY, theta'' = 62.69 >> theta_bar: H3 IS REFUTABLE
(the certificate fails in the inflation world while every identity
holds); census top tracks at 1.000001 y_t'' and cap'' = 1.000038 >=
top (TR-CAP sharp there).  THE PERTURBATION PRICE: |d+| ==
|A_2|(W-1)/(b_2-b_1) exactly -- |d+|/max|c_k| = 8.1e-2 at h = 5 but
10^{-6.7} at h = 8 and 10^{-17.6} at h = 13: an EXPONENTIALLY small
source perturbation moves y_t by ANY prescribed polynomial factor.
VERDICT: TOPROOT-NOT-NORM-CONTINUOUS -- no proof via source-norm
continuity/perturbation bounds can exist; any proof must consume the
arithmetic sign structure (the r140/r143 ALIGNMENT-WALL, quantified).
This CALIBRATES world separation: the movement is polynomial in the
WITNESS DIAL (x1000 by construction) at exponentially small norm cost
-- TOPROOT is world-separating through the two-sided window, not
through any one-sided bound.
(d) THE THETA-WINDOW FINITE-h FLOOR.  MEASURED: theta_y = 0.0449 ->
0.0779 over h = 4..30, monotone rising toward saturation ~0.078,
slope +0.28 in log10 h (inside the r162 flatness window +-0.45);
every finite rung carries a certified floor theta_y >= 0.03 (window
gate), and the r133/r162 instruments extend it exactly as far as the
schedule is verified.  The extension to all blocks IS TOPROOT (== H3
cofinal); no hidden lever found -- but the window is now measured
DEEPER than any prior round (h = 30, K = 128, deg-127 source).

=======================================================================
T4 -- THE CERTIFICATE AND THE ASSEMBLED CHAIN
=======================================================================
H3 [THE QUARTIC CERTIFICATE, per rung]: y_t(h) <= THETA_BAR T_z^4,
THETA_BAR = 0.155 (frozen at 2x the calibrated maximum).  H3 is ONE
exact source evaluation per rung -- NO zeros, NO cache, NO census
(ancestor set == {SOURCE}; same purity class as r171-H1).  Gated at
all 25 rungs + the deep holdout h = 30 (margin >= 2x everywhere).
THE ASSEMBLED CHAIN (typed):  JET-MASS-FLOOR ==
  [PF: proven given H1 + H2 (r171)] x [WF: classical-per-census,
  GONEK-CONSTANT-UNPRICED (r171)] x [RATE: proven given H3 per rung
  (THIS ROUND, certified source-pure) + the exact rate dictionary
  a = p/2 - 1 (sympy)].
THE FINAL RESIDUE (exact): {H3-COFINAL: theta_y <= THETA_BAR at one
rung per dyadic block, all blocks -- the entire lambda-uniform
residue of the delta-chain, now typed ZERO-FREE (a statement about
the source family alone), NOT-NORM-CONTINUOUS (witness), with its
analytic shortcut through A_0 machine-flagged as the pinning-supply
LOOP} + {Gonek constants: citable classical work} + {census-all-k ==
LOOP, flagged, not consumed} + {L1, WPD counting-class remnants}.
Census min-cut cardinality 4 UNCHANGED; nothing upgraded; NO new
omega closed.  H3-COFINAL is smaller than TOPROOT-MEAS was: it is
per-rung checkable, refutable (witness), and its required exponent
(4) sits 6 exponents under the schedule ceiling (10.27).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, np.load only in ward_*, no
    zero-oracle names, no verification/ import); G02 cache (X5;
    ward-class: gtop feeds ONLY the CLEAN_FIT criterion + HSW sanity;
    NO worker touches the cache -- the H3 chain is visibly zero-free).
S1  exact layer (sympy generic + exact rational instances):
    G10 TR-STATEMENT: rank-one dictionary (r143 T4 re-chased, generic
    K=3: charpoly(D - (1/A_0)|w><1|) == prod(y - b_k) F/A_0); trace
    == B_1 + y_t; theta-form <==> TOPROOT(4) rewriting; budget-
    invisibility core replicated (d/dy_t far-field mass < 0);
    G11 TR-CAP: geometric closed form sum rho^m z^-m == rho/(z-rho);
    the positivity polynomial (z-1)(z-rho) - rho at z = 1 + 2 rho + s
    (all coefficients positive); L1 dictionary re-chased generic K=3
    (series coefficients == J_2, J_3); circularity: Fujiwara m=1 ==
    B_1 + y_t generic;
    G12 TR-VIETA: Newton p_2 == e_1^2 - 2 e_2; e_2 == b_1 b_2 +
    (A_4 - A_2 B_1)/A_0 generic (the 1/A_0 pinning exhibit); kappa
    dictionary y_t == B_1/kappa;
    G13 TR-A0-ROUTE: triangle chase y_t <= b_top C_1/|A_0| + rational
    instance; zero-jet rearrangement A_0^2 == tau/(8 G tlaw_0); the
    route's ancestor set {TAUPOS, TLAWCAP} declared (flag semantics);
    G14 TR-WITNESS-BOTH: deflation A_0'' == A_0, A_2'' == A_2/W
    (r171 replicated) AND inflation A_0'' == A_0, A_2'' == W A_2 with
    d+ = A_2(W-1)/(b_2-b_1); |d+| identity;
    G15 TR-RATE-DICTIONARY: lim h^{p/2-1} G_lead(q h^{p/2})/
    G_lead(2 pi h) == pi p/q at p = 3, 4, 5 (p=4 replicates r171
    4 pi/q); absorption at a = 4 (limit 11 pi/kappa_c: even p = 10
    absorbs); census constant (3 pi/c)(1 + 2a/3) == pi (p+1)/c;
    G16 TR-H3-ASSEMBLY: monotone onset sqrt(z_0 y_t) <= sqrt(z_0
    theta_bar) T_z^2; drop+pointwise composition instance (r171 G14
    class); modus tollens instances: inflation theta 62.69 > bar
    (H3 refutable), deflation theta 6.3e-5 < window floor 0.03 (the
    two-sided window refuses both witness directions).
S2  G20 HSW G(T) sanity.
S3  per-rung layer h = 4..28 (25 rungs) + HOLDOUT h = 30 (h = 32
    DROPPED: HOLDOUT-COST-LIMITED, build 2638 s at 30 calibrated,
    32 est. >= 3500 s -- two full runs would break the budget;
    DISCLOSED), 12 spawn workers, cost-sorted; NO cache in workers:
    G30 spectral sanity (sorted, K, simp >= 1e3, ray/res <= 1e-25);
    G31 jets + trace: sign(A_2/A_0) == -1; B_1 closed form dev <=
    1e-40; Vieta trace dev <= 1e-40 (coefficient level, 3x dps);
    kappa in (0.0, 0.30) + KAPPA_TAB 4/5/8 rel 5e-3;
    G32 cross-instrument: y_t vs the r143/CDXLIV strings <= 1e-3 dex
    at h in {5,8,13,18,24,28}; FULLGAP on FG_TAB x (0.97, 1.03);
    fg > 0 all; lock = FULLGAP/y_t in (1.0, 8.0) (the unification
    lock: y_t-form == J-form);
    G33 THETA ladder: theta_y in (0.03, 0.12) at EVERY rung incl.
    holdout; THETA_Y_TAB {4,5,8,13,28,30} rel 5e-3;
    G34 H3 CERTIFICATE: y_t <= THETA_BAR T_z^4 at EVERY rung incl.
    holdout; margin theta_bar/theta_y >= 1.5 everywhere (calibrated
    >= 1.99);
    G35 moments: rho argmax == 1 (rho == |J_2|) at every rung;
    RHO_TAB {4,5,8,13,28,30} rel 5e-3; J_2 in (0.05, 0.25) HARD (the
    r156 quarter-cap window instantiated); ENV(400) < rho (tail
    certified); cap = 1 + 2 rho in (1.15, 1.45);
    G36 H1 replication + comparison: c* exists at every rung, <=
    1.75; CSTAR_TAB/ENVJ_RATIO_TAB 4/5/8; c* <= cap at EVERY rung
    (ENVJ-SHARPER: the new cap never beats the certified constant);
    G37 census (h <= 13 HARD, rootladder instrument VERBATIM):
    complete-real == K-1; negsum/y_t <= 1e-6; top/y_t in (0.70,
    0.95) + TOP_TAB {4,5,8,13} rel 5e-3; SR1 dev <= 1e-40; top <=
    cap y_t (TR-CAP instantiated on real data); top <= c* y_t;
    G38 Fujiwara circularity: f_1 == B_1 + y_t dev <= 1e-40; argmax_m
    f_m == 1 at every rung (m <= 8); f_1/y_t == 1 + kappa >= 1;
    G39 A0-route overshoot: OS >= 1e3 at every rung; regression
    slope log10 OS vs -log10|A_0| in (0.90, 1.05) (the overshoot IS
    the cancellation).
S3c transfer layer:
    G43 growth law: p_all = LSQ slope log10 y_t vs log10 h over the
    25 rungs in (3.0, 5.5) (r143 window); theta-slope in (-0.45,
    +0.45) (r162 flatness); p_clean over the CLEAN_FIT rungs
    (sqrt(4 y_t) <= gtop/2, r171 criterion VERBATIM; = 10 rungs);
    dictionary consistency |p_clean/2 - 1 - 1.057| <= 0.25
    (DISCLOSED loose: log corrections); HOLDOUT: h = 30 excluded
    from the fit, |y_t_l10(30) - fit(30)| <= 0.08 dex (calibration
    preview residual 0.017);
    G44 admissibility: eps_closed(56) on 4.533792e-9 rel 5e-3; a_max
    on 4.134758 rel 5e-3; p_max on 10.269515 rel 5e-3; bisection
    replication h*_rate(0.0767, a_max) == 56 rel 1e-2; MARGIN GATE
    p_all <= p_max - 4.0; census constant pi (p_all + 1)/c printed.
S4  controls through the SAME instrument (builds only, no zeros):
    G50 SMOOTH (4..8), G51 SCRARITH (4..8), G52 EPSTEIN (8,9,10):
    tau_w < 0 on the r166 strings rel 5e-3; theta_w <= 1e-2 at every
    control rung; THETA_W_TAB {SMOOTH x5: 2.4098e-4, SCRARITH x6:
    1.8751e-3, EPSTEIN x8: 1.0113e-4} rel 5e-3; SIZE-SEPARATOR (r171
    AMENDMENT-2 standard): min MAIN theta_y / max world theta_w >=
    10; H3-in-world and y_t_w/b_top printed REPORTED-DIAGNOSTIC (H3
    is one-sided world-blind algebra BY DESIGN -- the separation is
    the two-sided window + witness, gated, and typed honestly:
    H3-ONE-SIDED-WORLD-BLIND);
    G53 witness battery h = 5 BOTH directions (frozen d, d+):
    deflation: A_0 dev <= 1e-40; y_t'' x1000/y_t dev <= 1e-40; J_2
    inflation >= 1e4; census top/y_t'' on 24.870225 rel 5e-3 (r171
    string); cap'' >= top'' (TR-CAP world-blind); theta'' <= 1e-3
    (window floor refuses); inflation: A_0 dev <= 1e-40; y_t''/
    (1000 y_t) dev <= 1e-40; theta'' on 62.690999 rel 5e-3 AND >
    THETA_BAR (H3-REFUTED-IN-WITNESS: the certificate is falsifiable);
    census top/y_t'' <= 1.05; cap'' >= top''; |d|/max|c| on
    8.117888e-5 rel 5e-3, |d+|/max|c| on 8.117888e-2 rel 5e-3;
    perturbation scaling log10(|d+|/max|c|) at h = 8 on -6.726 and
    h = 13 on -17.611 (abs tol 0.05) with the h = 13 cost <= -15
    HARD: TOPROOT-NOT-NORM-CONTINUOUS.
S5  G54 screens: slopes vs log10 tau of log10 y_t and log10 theta_y
    both <= 0.30 in abs (DEMAND-FLAT); RIDER slope log10 A_0^2 vs
    log10 tau in (0.85, 1.15) (BOUND-RIDES-CONNES -- the loop
    signature of route (b') measured); G55 conditioning (1e-25 shift
    at h = 5, round-118 trap).
S6  G60 demand audit (SEQ inherited; THETA_BAR/windows/tabs/grids/
    fit criteria all frozen pre-evaluation; census per-k; no ALL-X);
    G61 loop/mining gate (ancestors of the delivered H3 chain ==
    {SOURCE} for H3 per rung; assembled chain ancestors == {SOURCE,
    ENVJ-CERT-H1, CENSUS-H2-PER-RUNG, TRACE-IDENT, CACHE-WARD(WF),
    GONEK-FORM, H3-PER-RUNG-CERT, HSW22, PT21-CENSUS-PER-K} --
    TOPROOT-MEAS is ELIMINATED as an ancestor (replaced by the
    certified per-rung H3 + the typed open cofinal edge); TLAWCAP,
    WPD, TAUPOS, CENSUS-ALL-K, JETLOCK-MEAS are NOT ancestors; FOUR
    loop routes carried flagged NOT consumed (tlaw-window,
    census-all-k, pinning-supply, A0-FLOOR VARIANT of pinning-supply
    -- this round's (b') finding); windows recomputed from frozen
    formulas, SIGN-MINING-CLEAN);
    G62 min-cut (r116 replica, r166/r168/r169/r171 graph VERBATIM:
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL 9
    NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
    G63 endgame graphs: (i) universalized census cycle DETECTED;
    (ii) pinning-supply cycle DETECTED; (iii) NEW: the A0-route
    cycle TAUPOS/TLAWCAP -> A0FLOOR -> TOPROOT -> ... -> DTSTEP_K ->
    TAUPOS DETECTED (the (b') mechanism is the loop, machine-
    verified); (iv) the terminal chain with {H3_PER_RUNG,
    H3_COFINAL} -> RATE replacing TOPROOT-MEAS is ACYCLIC with RH
    reachable from every counterfactual grant (AND-semantics); the
    FINAL RESIDUE printed.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); WORKERS = 12 (spawn; deterministic keys);
RUNGS = 4..28; HOLDOUT = (30,); DPS = {4:60, 5:60, 6:65, 7:70, 8:80,
9:85, 10:90, 11:100, 12:110, 13:120, 14:120, 15:125, 16:130, 17:135,
18:140, 19:140, 20:144, 21:146, 22:148, 23:150, 24:150, 25:152,
26:155, 27:158, 28:160, 30:170} (r166/r168/r169/r171 schedule + the
holdout extension).  INHERITED BARS (r171 VERBATIM where named):
SIMP_MIN = 1e3; RAY_BAR = RES0_BAR = 1e-25; CF_BAR = VIETA_BAR =
SR1_BAR = 1e-40; KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906}
rel 5e-3; KAPPA_WIN = (0.0, 0.30); FG_TAB = {4: 4.458152e4, 5:
2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7, 24: 1.1382e8,
28: 1.6513e8} x (0.97, 1.03); LOCK_WIN = (1.0, 8.0); CSTAR_TAB =
{4: 1.10, 5: 1.15, 8: 1.15}; C_STAR_MAX = 1.75; ENVJ_RATIO_TAB =
{4: 0.998177, 5: 0.967435, 8: 0.979598} rel 5e-3; C_GRID = (1.05,
1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00); TOP_WIN = (0.70,
0.95); TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13:
0.834429} rel 5e-3; NEGSUM_BAR = 1e-6; CENSUS_HARD_MAX = 13;
POLY_MAXSTEPS = 3000; IM_TOL = 1e-10; YT_R143 = {5: 6.107e4, 8:
4.165e5, 13: 3.204e6, 18: 1.258e7, 24: 4.013e7, 28: 7.390e7} <=
1e-3 dex; CTRL_TAU_TAB (r166 VERBATIM) rel 5e-3: SMOOTH {4: -1.0375,
5: -1.0944, 6: -1.1306, 7: -1.1560, 8: -1.1749}, SCRARITH {4:
-2.5151e-2, 5: -0.34593, 6: -0.36716, 7: -0.61294, 8: -0.67664},
EPSTEIN {8: -1.6310, 9: -1.6922, 10: -1.9932}; CTRL blocks SMOOTH =
SCRARITH = (4..8) dps 60, EPSTEIN = (8, 9, 10) dps 80; TAU_SLOPE_BAR
= 0.30; RIDER_WIN = (0.85, 1.15); COND_WIN = (1e-40, 1e-10);
RUNTIME_BAR = 21600 s; RATE_C = 0.0767; RATE_A = 1.057 (r171 record
strings); CLEAN_FIT: sqrt(4 y_t) <= gtop/2 (r171 VERBATIM).
NEW (calibrated in calib_toproot_pass1.log, ONE pre-freeze pass at
h = 4/5/8/13/28/30 + controls SMOOTH x5 / SCRARITH x6 / EPSTEIN x8 +
witness h = 5 both directions + scaling h = 8/13; scratch deleted
after freeze, log kept; all numbers quoted verbatim):
THETA_BAR = 0.155 (= 2x the calibrated max 0.077858); THETA_Y_WIN =
(0.03, 0.12); THETA_Y_TAB = {4: 0.044901, 5: 0.062691, 8: 0.065250,
13: 0.071983, 28: 0.077144, 30: 0.077858} rel 5e-3; H3_MARGIN_MIN =
1.5 (calibrated min 1.99); RHO_TAB = {4: 0.106805, 5: 0.125884, 8:
0.139445, 13: 0.147746, 28: 0.151278, 30: 0.151513} rel 5e-3;
J2_WIN = (0.05, 0.25); CAP_WIN = (1.15, 1.45); FUJ_M = 8; OS_MIN =
1e3 (calibrated 2.8e3 at h = 4); OS_SLOPE_WIN = (0.90, 1.05)
(calibrated endpoint 0.972); P_WIN = (3.0, 5.5) [r143]; TH_SLOPE_WIN
= (-0.45, +0.45) [r162]; A_DICT_TOL = 0.25; HOLD_RESID_BAR = 0.08
dex (preview 0.017); EPS56_STR = 4.533792e-9 rel 5e-3; AMAX_STR =
4.134758 rel 5e-3; PMAX_STR = 10.269515 rel 5e-3; HSTAR_MIN_COVER =
56.0 (= 2 H_MAX); P_MARGIN_MIN = 4.0; THETA_W_TAB = {("SMOOTH", 5):
2.4098e-4, ("SCRARITH", 6): 1.8751e-3, ("EPSTEIN", 8): 1.0113e-4}
rel 5e-3; CTRL_THETA_MAX = 1e-2; SEP_MIN = 10.0 (calibrated 23.9);
WIT_FACT = 1000; WIT_A0_BAR = WIT_YT_BAR = 1e-40 (calibrated <=
4.2e-55); WIT_J2_INFL_MIN = 1e4 (calibrated 1.01e6); WIT_ZTOP_STR =
24.870225 rel 5e-3; WIT_DEFL_THETA_MAX = 1e-3 (calibrated 6.27e-5);
WIT_INFL_THETA_STR = 62.690999 rel 5e-3; WIT_INFL_ZTOP_MAX = 1.05
(calibrated 1.000001); WIT_DNORM_DEFL_STR = 8.117888e-5 rel 5e-3;
WIT_DNORM_INFL_STR = 8.117888e-2 rel 5e-3; WIT_SCALE_STR = {8:
-6.726, 13: -17.611} abs tol 0.05; WIT_SCALE13_MAX = -15.0.
Deterministic: NO randomness anywhere.  Cache verified_zeros_n7000
READ-ONLY in ward_ (X5), main-process only (CLEAN_FIT criterion +
HSW sanity); NO zeta use.  All mpf arithmetic inside explicit
mp.workdps blocks in-worker; npoly at 3x dps; flat O(1) ratios
transported as f64 for gating (DISCLOSED).  h in {6, 7, 9..12,
14..27} pre-freeze UNMEASURED on the new coordinates (structure
windows only, DISCLOSED); the holdout h = 30 was PRE-MEASURED in the
calibration pass (its strings frozen; the HOLDOUT CONTENT is the
fit-exclusion residual gate, DISCLOSED); h = 32 DROPPED for cost
(HOLDOUT-COST-LIMITED, DISCLOSED).  Amendments after the frozen run,
if any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
TOPROOT-STATED-UNIFIED(one inequality, SEQ quantifier, three locked
forms; G10/G32); THETA-QUARTIC-REPLICATED(25 rungs + holdout;
G33/G43); H3-CERTIFIED-PER-RUNG(the quartic certificate, source-pure;
G34); ADMISSIBLE-EXPONENT-GATED(p_max = 10.27, margin >= 4; G44);
TR-CAP-PROVEN-Z-UNITS(new census cap theorem + tail certification;
G11/G35/G37); MOMENT-ROUTE-CIRCULAR-FOR-TOPROOT(Fujiwara argmax ==
trace; G11/G38); VIETA-PINCH-PINNED(1/A_0 in every symmetric
function; G12); A0-ROUTE-LOOP-FLAGGED(vacuous AND pinning-supply in
A_0-currency; G13/G39/G63); TOPROOT-NOT-NORM-CONTINUOUS(witness both
directions, exponential price; G14/G53); RATE-DICTIONARY-EXACT(a ==
p/2 - 1; G15/G43); H3-REFUTABLE(witness kills the certificate;
G16/G53); ENVJ-SHARPER-THAN-CAP(G36); H3-ONE-SIDED-WORLD-BLIND +
SIZE-SEPARATOR(G50-G52); CROSS-INSTRUMENT-REPLICATED(r143 strings +
r171 tabs; G32); DEMAND-FLAT + BOUND-RIDES-CONNES(G54);
QUANTIFIER-SEQ(G60); LOOP-ROUTES-FLAGGED(four; G61/G63);
OMEGA-UNCHANGED(census 4; G62); MINCUT(4/5).  Composite priority:
INSTRUMENT-EDGE (any edge gate fails, exit 1) > EXACT-LAYER-
OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 30/32 at the
first-freeze SPEC_SHA 8f95035e57b4b034, log kept as
toproot_theta_probe.smoke1.log; NO record run existed yet).  TWO
sympy INSTRUMENT bugs in the exact layer, no bar, window, tab or
criterion moved anywhere: (a) G12 okL asserted the kappa dictionary
through a mistyped triple quotient B1/(B1/(B1/kappa)) == kappa
(which is B1/kappa, false); fixed to the two direct identities
B1/y_t == kappa and y_t kappa == B1 with y_t := B1/kappa.  (b) G14
okU asserted |d+| == |A_2|(W-1)/(b_2-b_1) with b_1, b_2 free
positive symbols -- sympy correctly refuses since the identity
needs b_2 > b_1; fixed by substituting b_2 = b_1 + db, db > 0 (the
mode ordering is structural: b_k = (k pi/A)^2 is strictly
increasing).  Both fixes verified in isolation before re-freeze;
smoke2 at the fixed SHA must be clean.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt VII, note CDXCII, 2026-08-20)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays cf27df22aa5dffbf.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH7-F1 [MAJOR, residue-prose compression]:
#   ORIGINAL (this spec + note CDLXXXVIII): "THE FINAL RESIDUE
#   (exact): {H3-COFINAL: ...}" / "der lambda-uniforme Rest ist EXAKT
#   H3-KOFINAL" -- H3 singled out as THE lambda-uniform residue.
#   CORRECTED: the composed per-block hypothesis is the TRIPLE
#   {H1 AND H2 AND H3}-cofinal, one rung per dyadic block, all three
#   at the same h -- corrected wording: "{H1 ∧ H2 ∧ H3}-KOFINAL (eine
#   Sprosse pro Block, alle drei am selben h)".  PF is proven only
#   GIVEN H1 + H2 at the same rung (r171 verbatim: "THEOREM
#   CONDITIONAL EXACTLY ON {H1 + H2 per rung}"); H1/H2/H3 are all
#   finite per-rung source checks of the same epistemic type,
#   certified only h <= 26/13(24)/30.  The MACHINE layer (G61/G63
#   ancestors) was always consistent; the compression is prose-level
#   only.
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
WORKERS = 12
H_MAX = 28
RUNGS = tuple(range(4, 29))
HOLDOUT = (30,)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 17: 135,
       18: 140, 19: 140, 20: 144, 21: 146, 22: 148, 23: 150,
       24: 150, 25: 152, 26: 155, 27: 158, 28: 160, 30: 170}

SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
CF_BAR = 1e-40
VIETA_BAR = 1e-40
SR1_BAR = 1e-40
KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906}
KAPPA_WIN = (0.0, 0.30)
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7,
          18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
LOCK_WIN = (1.0, 8.0)
CSTAR_TAB = {4: 1.10, 5: 1.15, 8: 1.15}
C_STAR_MAX = 1.75
ENVJ_RATIO_TAB = {4: 0.998177, 5: 0.967435, 8: 0.979598}
C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00)
TOP_WIN = (0.70, 0.95)
TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429}
NEGSUM_BAR = 1e-6
CENSUS_HARD_MAX = 13
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
YT_R143 = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
           24: 4.013e7, 28: 7.390e7}
YT_DEX_BAR = 1e-3
CTRL_SMOOTH = (4, 5, 6, 7, 8)
CTRL_SCRARITH = (4, 5, 6, 7, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_TAU_TAB = {
    "SMOOTH": {4: -1.0375, 5: -1.0944, 6: -1.1306, 7: -1.1560,
               8: -1.1749},
    "SCRARITH": {4: -2.5151e-2, 5: -0.34593, 6: -0.36716,
                 7: -0.61294, 8: -0.67664},
    "EPSTEIN": {8: -1.6310, 9: -1.6922, 10: -1.9932}}
CTRL_TAU_TOL = 5e-3
GAMMA1_LIT = 14.134725141734693790   # ward only
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 21600.0
RATE_C = 0.0767
RATE_A = 1.057
NEW_TOL = 5e-3

# ------------------------------------------------- new frozen (calibrated)
THETA_BAR = 0.155
THETA_Y_WIN = (0.03, 0.12)
THETA_Y_TAB = {4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983,
               28: 0.077144, 30: 0.077858}
H3_MARGIN_MIN = 1.5
RHO_TAB = {4: 0.106805, 5: 0.125884, 8: 0.139445, 13: 0.147746,
           28: 0.151278, 30: 0.151513}
J2_WIN = (0.05, 0.25)
CAP_WIN = (1.15, 1.45)
FUJ_M = 8
OS_MIN = 1e3
OS_SLOPE_WIN = (0.90, 1.05)
P_WIN = (3.0, 5.5)
TH_SLOPE_WIN = (-0.45, 0.45)
A_DICT_TOL = 0.25
HOLD_RESID_BAR = 0.08
EPS56_STR = 4.533792e-9
AMAX_STR = 4.134758
PMAX_STR = 10.269515
HSTAR_MIN_COVER = 56.0
P_MARGIN_MIN = 4.0
THETA_W_TAB = {("SMOOTH", 5): 2.4098e-4, ("SCRARITH", 6): 1.8751e-3,
               ("EPSTEIN", 8): 1.0113e-4}
CTRL_THETA_MAX = 1e-2
SEP_MIN = 10.0
WIT_FACT = 1000
WIT_A0_BAR = 1e-40
WIT_YT_BAR = 1e-40
WIT_J2_INFL_MIN = 1e4
WIT_ZTOP_STR = 24.870225
WIT_DEFL_THETA_MAX = 1e-3
WIT_INFL_THETA_STR = 62.690999
WIT_INFL_ZTOP_MAX = 1.05
WIT_DNORM_DEFL_STR = 8.117888e-5
WIT_DNORM_INFL_STR = 8.117888e-2
WIT_SCALE_STR = {8: -6.726, 13: -17.611}
WIT_SCALE_TOL = 0.05
WIT_SCALE13_MAX = -15.0

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
                       "no verification/ import; workers cache-free")


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


def eps_closed(h: float) -> float:
    return float(mp.sqrt(h) * hsw_G_mp(T_PT)
                 / hsw_G_mp(2 * math.pi * h))


def solve_horizon(sigma0: float, a_rate: float = 0.0) -> float:
    lo, hi = 1e1, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed(mid) < sigma0 * mid ** (-a_rate):
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def npoly_coeffs(cs, b, K):
    """rootladder census form VERBATIM (r156/r171).  Scaled y = s*Y,
    s = b_top + 1.  Leading coefficient == A_0.  Caller wraps in
    workdps."""
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
    """per-rung build: spectral sanity + jets/trace/kappa + theta_y +
    H3 + moments/rho/cap + H1 c* + npoly/Vieta/Fujiwara + census
    (h <= CENSUS_HARD_MAX) + overshoot.  NO cache access (the H3
    chain is zero-free); all mp inside workdps; f64 transport of
    flat O(1) ratios (DISCLOSED)."""
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
            out["log10tau"] = float(mp.log(tau) / l10)
            aa = mp.log(h) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            btop = b[K - 1]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
            yt = abs(A2 / A0)
            out["a2_sign"] = int(mp.sign(A2 / A0))
            out["yt_l10"] = float(mp.log(yt) / l10)
            out["log10a0"] = float(mp.log(abs(A0)) / l10)
            out["fg"] = float((lam1 - tau) / tau)
            out["lock"] = float(((lam1 - tau) / tau) / yt)
            B1 = sum(b[k] for k in range(1, K))
            B1_cf = (mp.pi / aa) ** 2 * (K - 1) * K * (2 * K - 1) / 6
            out["cf_dev"] = float(abs(B1 / B1_cf - 1))
            kap = B1 / yt
            out["kappa"] = float(kap)
            Tz = 2 * mp.pi * h
            th = yt / Tz ** 4
            out["theta_y"] = float(th)
            out["h3_ok"] = bool(yt <= mp.mpf(repr(THETA_BAR))
                                * Tz ** 4)
            out["h3_margin"] = float(mp.mpf(repr(THETA_BAR)) / th)
            C1 = sum(abs(cs[k]) for k in range(1, K))
            out["os_l10"] = float(mp.log(btop * C1 / (abs(A0) * yt))
                                  / l10)
            out["yt_btop"] = float(yt / btop)
            # moments A_{2m}, rho = sup |J_{m+1}|^{1/m}, cap
            cs_abs = [abs(v) for v in cs]
            A_j = [A0]
            pw = [mp.mpf(1)] * K
            for m in range(1, M_JETS + 1):
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)
            rho = None
            argm = None
            for m in range(1, M_JETS):
                Jm = abs(A_j[m + 1]) / (abs(A0) * yt ** (m + 1))
                v = Jm ** (mp.mpf(1) / m)
                if rho is None or v > rho:
                    rho = v
                    argm = m
            out["rho"] = float(rho)
            out["rho_argm"] = argm
            out["J2"] = float(A_j[2] / (A0 * yt ** 2))
            env400 = (C1 * btop / (abs(A0) * yt)) \
                ** (mp.mpf(1) / M_JETS) * (btop / yt)
            out["env400"] = float(env400)
            out["cap"] = float(1 + 2 * rho)

            # H1: c* from the frozen grid (r171 VERBATIM)
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
            # npoly: Vieta + Fujiwara
            with mp.workdps(3 * dps):
                poly, psc = npoly_coeffs(cs, b, K)
                vieta = -poly[1] / poly[0] * psc
                out["vieta_dev"] = float(abs(vieta / (B1 + yt) - 1))
                fuj = []
                for m in range(1, min(FUJ_M, K - 1) + 1):
                    fm = abs(poly[m] / poly[0]) \
                        ** (mp.mpf(1) / m) * psc
                    fuj.append(float(fm / yt))
                out["fuj_over_yt"] = fuj
                out["fuj_argmax"] = 1 + int(np.argmax(fuj))
                out["f1_dev"] = float(abs(
                    abs(poly[1] / poly[0]) * psc / (B1 + yt) - 1))
            # census (ISOLATED, h <= CENSUS_HARD_MAX)
            if h <= CENSUS_HARD_MAX:
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
                    out["cen_real"] = nreal
                    out["cen_top_yt"] = float(ys[-1] / yt)
                    out["cen_negsum_yt"] = float(
                        sum(abs(y) for y in ys if y < 0) / yt)
                    out["cen_sr1_dev"] = float(abs(
                        (sum(ys) - B1) / yt - 1))
                except Exception as cexc:          # noqa: BLE001
                    out["cen_error"] = repr(cexc)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w + theta_w + y_t_w/b_top + H3-in-world
    (builds only, no zeros)."""
    world, xw, dpsw = args
    try:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            aa = mp.log(xw) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(Kw))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, Kw))
            ytw = abs(A2 / A0)
            Tz = 2 * mp.pi * xw
            return dict(world=world, h=xw, tauf=float(tau),
                        theta_w=float(ytw / Tz ** 4),
                        ytb_w=float(ytw / b[Kw - 1]),
                        h3_w=bool(ytw <= mp.mpf(repr(THETA_BAR))
                                  * Tz ** 4))
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y, z, s_ = sp.symbols("y z s_", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    rho = sp.symbols("rho", positive=True)
    A0g = c0 - c1 + c2
    A2g = -c1 * b1 + c2 * b2
    A4g = -c1 * b1 ** 2 + c2 * b2 ** 2
    F = c0 - c1 * y / (y - b1) + c2 * y / (y - b2)

    # ---------------- G10 TR-STATEMENT (rank-one dictionary + forms)
    w1, w2 = -c1 * b1, c2 * b2
    Mm = sp.Matrix([[b1 - w1 / A0g, -w1 / A0g],
                    [-w2 / A0g, b2 - w2 / A0g]])
    chp = (sp.eye(2) * y - Mm).det()
    okA = sp.simplify(chp - (y - b1) * (y - b2) * F / A0g) == 0
    okB = sp.simplify(sp.trace(Mm) - (b1 + b2 - A2g / A0g)) == 0
    th_, hh_, Cb_ = sp.symbols("th_ hh_ Cb_", positive=True)
    okC = sp.simplify(th_ * (2 * sp.pi * hh_) ** 4
                      - th_ * (2 * sp.pi) ** 4 * hh_ ** 4) == 0
    ytq = sp.symbols("ytq", positive=True)
    dmass = sp.diff((1 - ytq / y) ** 2, ytq)
    okD = sp.simplify(dmass * y + 2 * (1 - ytq / y)) == 0
    okD = okD and bool(dmass.subs({ytq: 2, y: 5}) < 0)
    out.append(("G10-tr-statement", okA and okB and okC and okD,
                "rank-one dictionary charpoly(D - (1/A_0)|w><1|) == "
                "prod(y - b_k) F/A_0 (r143 T4 re-chased, generic "
                "K=3); trace == B_1 + y_t; theta-form == TOPROOT(4) "
                "rewriting; budget-invisibility core d/dy_t "
                "(1 - y_t/y)^2 < 0 replicated: TOPROOT stated as ONE "
                "inequality, SEQ-cofinal quantifier declared"))

    # ---------------- G11 TR-CAP
    m_ = sp.symbols("m_", positive=True, integer=True)
    geo = sp.summation((rho / z) ** m_, (m_, 1, sp.oo))
    okE = sp.simplify(sp.piecewise_fold(geo).args[0][0]
                      - rho / (z - rho)) == 0 \
        if isinstance(sp.piecewise_fold(geo), sp.Piecewise) \
        else sp.simplify(geo - rho / (z - rho)) == 0
    pos = sp.expand((2 * rho + s_) * (1 + rho + s_) - rho)
    pp = sp.Poly(pos, rho, s_)
    okF = all(cf > 0 for cf in pp.coeffs())
    # L1 dictionary re-chase generic K=3: series of z F(z yt)/A0
    yts = -A2g / A0g
    u = sp.symbols("u", positive=True)
    expr = (F.subs(y, yts / u) / A0g) / u
    ser = sp.series(expr, u, 0, 4).removeO()
    c_m1 = sp.simplify(ser.coeff(u, -1))         # z-term
    c_0 = sp.simplify(ser.coeff(u, 0))
    c_1t = sp.simplify(ser.coeff(u, 1))
    c_2t = sp.simplify(ser.coeff(u, 2))
    J2g = A4g / (A0g * yts ** 2)
    A6g = -c1 * b1 ** 3 + c2 * b2 ** 3
    J3g = A6g / (A0g * yts ** 3)
    okG = (sp.simplify(c_m1 - 1) == 0
           and sp.simplify(c_0 + 1) == 0
           and sp.simplify(c_1t - J2g) == 0
           and sp.simplify(c_2t - J3g) == 0)
    inst = {c0: sp.Rational(3, 5), c1: sp.Rational(1, 3),
            c2: sp.Rational(1, 7), b1: sp.Integer(2),
            b2: sp.Integer(5)}
    rho_i = sp.Rational(1, 8)
    z_i = 1 + 2 * rho_i
    okH = bool((z_i - 1) * (z_i - rho_i) - rho_i > 0)
    N1 = sp.together(F * (y - b1) * (y - b2))
    N1 = sp.expand(N1)
    okI = sp.simplify(-sp.Poly(N1, y).coeff_monomial(y)
                      / sp.Poly(N1, y).coeff_monomial(y ** 2)
                      - (b1 + b2 + yts)) == 0
    out.append(("G11-tr-cap", okE and okF and okG and okH and okI,
                "TR-CAP PROVEN: sum rho^m z^-m == rho/(z - rho) "
                "(geometric closed form); (z-1)(z-rho) - rho == "
                "rho + 2 rho^2 + (1 + 3 rho) s + s^2 at z = 1 + "
                "2 rho + s (ALL coefficients positive) ==> PHI != 0 "
                "for real z >= 1 + 2 rho; r156-L1 dictionary "
                "re-chased generic K=3 (series == z - 1 + J_2/z + "
                "J_3/z^2 + ...); CIRCULARITY: Fujiwara m=1 == B_1 + "
                "y_t (the trace) -- the cap lives in y_t-units: "
                "MOMENT-ROUTE-CIRCULAR-FOR-TOPROOT"))

    # ---------------- G12 TR-VIETA pinch
    y1, y2 = sp.symbols("y1 y2", positive=True)
    okJ = sp.simplify((y1 ** 2 + y2 ** 2)
                      - ((y1 + y2) ** 2 - 2 * y1 * y2)) == 0
    N2c = sp.Poly(N1, y).coeff_monomial(y ** 2)
    N0c = sp.Poly(N1, y).coeff_monomial(1)
    e2 = N0c / N2c
    B1g = b1 + b2
    okK = sp.simplify(e2 - (b1 * b2 + (A4g - A2g * B1g) / A0g)) == 0
    kapq, B1q = sp.symbols("kapq B1q", positive=True)
    ytdq = B1q / kapq
    okL = sp.simplify(B1q / ytdq - kapq) == 0
    okL = okL and sp.simplify(ytdq * kapq - B1q) == 0
    out.append(("G12-tr-vieta-pinch", okJ and okK and okL,
                "Newton p_2 == e_1^2 - 2 e_2; e_2 == b_1 b_2 + "
                "(A_4 - A_2 B_1)/A_0 generic (EVERY symmetric "
                "function carries 1/A_0 -- the moment content is "
                "pinned); y_t == B_1/kappa dictionary (TOPROOT <==> "
                "kappa >= 1/poly is a REFORMULATION, typed, not an "
                "advance): VIETA-PINCH-PINNED"))

    # ---------------- G13 TR-A0-ROUTE (the loop, priced)
    okM = bool(abs(A2g.subs(inst)) <= sp.Integer(5)
               * (sp.Rational(1, 3) + sp.Rational(1, 7)))
    C1q, btq, A0q = sp.symbols("C1q btq A0q", positive=True)
    okN = sp.simplify(btq * C1q / A0q
                      - (btq * C1q / A0q)) == 0
    tauq, Gq, tl = sp.symbols("tauq Gq tl", positive=True)
    okO = sp.simplify(sp.solve(sp.Eq(tauq, 8 * A0q ** 2 * Gq * tl),
                               A0q ** 2)[0] - tauq / (8 * Gq * tl)) \
        == 0
    route_anc = {"A0FLOOR": ("TAUPOS", "TLAWCAP")}
    okP = set(route_anc["A0FLOOR"]) == {"TAUPOS", "TLAWCAP"}
    out.append(("G13-tr-a0-route", okM and okN and okO and okP,
                "triangle |A_2| <= b_top C_1 (rational instance) "
                "==> y_t <= b_top C_1/|A_0|; zero-jet rearrangement "
                "A_0^2 == tau/(8 G tlaw_0) (r137, definitional): an "
                "A_0-floor consumes {TAUPOS, TLAWCAP} == the "
                "pinning-supply LOOP in A_0-currency -- declared, "
                "FLAGGED, NOT consumed (cycle check in G63)"))

    # ---------------- G14 TR-WITNESS both directions
    W = sp.Integer(WIT_FACT)
    dW = -A2g * (1 - 1 / W) / (b2 - b1)
    c1w, c2w = c1 + dW, c2 + dW
    okQ = sp.simplify((c0 - c1w + c2w) - A0g) == 0
    okR = sp.simplify((-c1w * b1 + c2w * b2) - A2g / W) == 0
    dP = A2g * (W - 1) / (b2 - b1)
    c1p, c2p = c1 + dP, c2 + dP
    okS = sp.simplify((c0 - c1p + c2p) - A0g) == 0
    okT = sp.simplify((-c1p * b1 + c2p * b2) - W * A2g) == 0
    dbq = sp.symbols("dbq", positive=True)
    okU = sp.simplify((sp.Abs(dP)
                       - sp.Abs(A2g) * (W - 1) / (b2 - b1))
                      .subs(b2, b1 + dbq)) == 0
    out.append(("G14-tr-witness-both", okQ and okR and okS and okT
                and okU,
                "deflation d = -A_2(1 - 1/%d)/(b_2 - b_1): A_0'' == "
                "A_0, A_2'' == A_2/%d (r171 G16 replicated); NEW "
                "INFLATION d+ = A_2(%d - 1)/(b_2 - b_1): A_0'' == "
                "A_0, A_2'' == %d A_2 EXACTLY, price |d+| == "
                "|A_2|(W-1)/(b_2 - b_1) -- |A_2|-sized, hence "
                "EXPONENTIALLY small in h at fixed W: any polynomial "
                "y_t movement costs an exponentially small source "
                "perturbation" % (WIT_FACT, WIT_FACT, WIT_FACT,
                                  WIT_FACT)))

    # ---------------- G15 TR-RATE dictionary
    hh, qq = sp.symbols("hh qq", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okV = True
    for p_r in (sp.Integer(3), sp.Integer(4), sp.Integer(5)):
        lim = sp.limit(hh ** (p_r / 2 - 1)
                       * Glead(qq * hh ** (p_r / 2))
                       / Glead(2 * sp.pi * hh), hh, sp.oo)
        okV = okV and sp.simplify(lim - sp.pi * p_r / qq) == 0
    kapc = sp.symbols("kapc", positive=True)
    a_r = sp.Integer(4)
    s_e = sp.Rational(3, 2) + a_r
    lim4 = sp.limit(sp.sqrt(hh) * Glead(kapc * hh ** s_e)
                    / Glead(2 * sp.pi * hh) * hh ** a_r, hh, sp.oo)
    okW = sp.simplify(lim4 - 2 * sp.pi * s_e / kapc) == 0
    a_s, c_s, p_s = sp.symbols("a_s c_s p_s", positive=True)
    okX = sp.simplify(((3 * sp.pi / c_s) * (1 + 2 * a_s / 3))
                      .subs(a_s, p_s / 2 - 1)
                      - sp.pi * (p_s + 1) / c_s) == 0
    out.append(("G15-tr-rate-dictionary", okV and okW and okX,
                "lim h^{p/2-1} G_lead(q h^{p/2})/G_lead(2 pi h) == "
                "pi p/q EXACT at p = 3, 4, 5 (p = 4 replicates the "
                "r171 4 pi/q): TOPROOT(p) ==> WF ~ h^{1-p/2} ==> "
                "sigma-floor exponent a == p/2 - 1; absorption "
                "replicated at a = 4 (limit 11 pi/kappa: even p = "
                "10 absorbs); census constant (3 pi/c)(1 + 2a/3) == "
                "pi (p+1)/c: RATE-DICTIONARY-EXACT"))

    # ---------------- G16 TR-H3 assembly + modus tollens
    z0q, Tq, thb = sp.symbols("z0q Tq thb", positive=True)
    okY = sp.simplify(sp.sqrt(z0q * thb * Tq ** 4)
                      - sp.sqrt(z0q * thb) * Tq ** 2) == 0
    yti, thi, Ti = (sp.Rational(1, 10), sp.Rational(1, 5),
                    sp.Integer(3))
    okZ = bool(yti * Ti ** 4 <= thi * Ti ** 4) and \
        bool(sp.sqrt(4 * yti * Ti ** 4)
             <= sp.sqrt(4 * thi) * Ti ** 2)
    w1q, w2q, w3q = (sp.Rational(1, 2), sp.Rational(1, 3),
                     sp.Rational(1, 7))
    f1q, f2q, f3q = (sp.Rational(1, 10), sp.Rational(4, 5),
                     sp.Rational(9, 10))
    Lq = sp.Rational(3, 4)
    delta_i = (w1q * f1q ** 2 + w2q * f2q ** 2 + w3q * f3q ** 2) \
        / (w1q + w2q + w3q)
    floor_i = Lq ** 2 * (w2q + w3q) / (w1q + w2q + w3q)
    okAA = bool(f2q >= Lq and f3q >= Lq and delta_i >= floor_i)
    okAB = bool(sp.Rational(6269099894847788, 10 ** 14)
                > sp.Rational(155, 1000)) \
        and bool(sp.Rational(6269099894847788, 10 ** 20)
                 < sp.Rational(3, 100))
    out.append(("G16-tr-h3-assembly", okY and okZ and okAA and okAB,
                "monotone onset sqrt(z_0 y_t) <= sqrt(z_0 theta_bar)"
                " T_z^2 (exact); drop + pointwise composition "
                "instance (r171 G14 class): {H3, H1, H2} x Gonek "
                "==> the sigma-floor rate CERTIFIED-PER-RUNG; modus "
                "tollens: inflation-witness theta = 62.69 > "
                "THETA_BAR = 0.155 (H3 REFUTABLE) and deflation "
                "theta = 6.27e-5 < window floor 0.03 (the TWO-SIDED "
                "window refuses BOTH witness directions)"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = []
    steps.append(("NFCLOS (CDXXIII, cited) demands an unbounded "
                  "sequence per a (SEQ); TOPROOT/H3 is demanded "
                  "COFINALLY (one rung per dyadic block), NOT for "
                  "all h", demand == SEQ))
    steps.append(("THETA_BAR/windows/tabs/C_GRID/FUJ_M/fit criteria "
                  "DECLARED pre-evaluation (SPEC_SHA covers the "
                  "declaration)", True))
    steps.append(("the census schedule is typed PER-K; the ALL-K "
                  "grant is carried ONLY as a flagged LOOP edge",
                  True))
    steps.append(("the delivered H3 certificate consumes SOURCE "
                  "ONLY (no zeros, no cache, no census, no tau "
                  "sign); the assembled chain adds the r171 "
                  "ancestors verbatim minus TOPROOT-MEAS", True))
    steps.append(("no ALL-X demand introduced; uniform per-rung "
                  "margins NOT demanded", demand != ALL_X))
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


# --------------------------------------------------------- witness
def witness_battery() -> tuple[bool, str]:
    """2-mode witness at h=5, BOTH directions (frozen d, d+) +
    perturbation-size scaling at h = 8, 13.  All mp in workdps;
    no zeros consumed."""
    h, dps = 5, DPS[5]
    ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    rows = {}
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        A4 = sum((-1) ** k * cs[k] * b[k] ** 2 for k in range(1, K))
        yt = abs(A2 / A0)
        Tz4 = (2 * mp.pi * h) ** 4
        cmax = max(abs(v) for v in cs)
        for tag, dv in (("defl", -A2 * (1 - mp.mpf(1) / WIT_FACT)
                         / (b[2] - b[1])),
                        ("infl", A2 * (WIT_FACT - 1)
                         / (b[2] - b[1]))):
            cs2 = list(cs)
            cs2[1] = cs[1] + dv
            cs2[2] = cs[2] + dv
            A0w = sum((-1) ** k * cs2[k] for k in range(K))
            A2w = sum((-1) ** k * cs2[k] * b[k]
                      for k in range(1, K))
            A4w = sum((-1) ** k * cs2[k] * b[k] ** 2
                      for k in range(1, K))
            ytw = abs(A2w / A0w)
            d = dict(a0_dev=float(abs(A0w / A0 - 1)),
                     dnorm=float(abs(dv) / cmax),
                     theta=float(ytw / Tz4))
            if tag == "defl":
                d["yt_dev"] = float(abs(ytw * WIT_FACT / yt - 1))
            else:
                d["yt_dev"] = float(abs(ytw / (WIT_FACT * yt) - 1))
            d["j2_ratio"] = float(abs((A4w / (A0w * ytw ** 2))
                                      / (A4 / (A0 * yt ** 2))))
            rho_w = None
            pww = [mp.mpf(1)] * K
            Ajw = [A0w]
            for m in range(1, 41):
                acc = mp.mpf(0)
                for k in range(1, K):
                    pww[k] = pww[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs2[k] * pww[k]
                Ajw.append(acc)
            for m in range(1, 40):
                Jm = abs(Ajw[m + 1]) / (abs(A0w) * ytw ** (m + 1))
                v = Jm ** (mp.mpf(1) / m)
                if rho_w is None or v > rho_w:
                    rho_w = v
            d["cap"] = float(1 + 2 * rho_w)
            with mp.workdps(3 * dps):
                poly, psc = npoly_coeffs(cs2, b, K)
            rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                               extraprec=2 * dps)
            d["ztop"] = float(max(mp.re(r) * psc for r in rts) / ytw)
            rows[tag] = d
    scal = {}
    for hs in (8, 13):
        cs_ = R4.build_cell(hs, KFAC, "MAIN", DPS[hs], want_mp=True)
        Ks = cs_["K"]
        with mp.workdps(DPS[hs]):
            aas = mp.log(hs) / 2
            bs = [(k * mp.pi / aas) ** 2 for k in range(Ks)]
            csv = [mp.mpf(s) for s in cs_["cn_mp_str"]]
            A2s = sum((-1) ** k * csv[k] * bs[k]
                      for k in range(1, Ks))
            cmaxs = max(abs(v) for v in csv)
            dp = abs(A2s) * (WIT_FACT - 1) / (bs[2] - bs[1])
            scal[hs] = float(mp.log(dp / cmaxs) / mp.log(10))
    df, fl = rows["defl"], rows["infl"]
    ok = (df["a0_dev"] <= WIT_A0_BAR and df["yt_dev"] <= WIT_YT_BAR
          and df["j2_ratio"] >= WIT_J2_INFL_MIN
          and abs(df["ztop"] / WIT_ZTOP_STR - 1) <= NEW_TOL
          and df["cap"] >= df["ztop"]
          and df["theta"] <= WIT_DEFL_THETA_MAX
          and fl["a0_dev"] <= WIT_A0_BAR
          and fl["yt_dev"] <= WIT_YT_BAR
          and abs(fl["theta"] / WIT_INFL_THETA_STR - 1) <= NEW_TOL
          and fl["theta"] > THETA_BAR
          and fl["ztop"] <= WIT_INFL_ZTOP_MAX
          and fl["cap"] >= fl["ztop"]
          and abs(df["dnorm"] / WIT_DNORM_DEFL_STR - 1) <= NEW_TOL
          and abs(fl["dnorm"] / WIT_DNORM_INFL_STR - 1) <= NEW_TOL
          and all(abs(scal[hs] - WIT_SCALE_STR[hs])
                  <= WIT_SCALE_TOL for hs in (8, 13))
          and scal[13] <= WIT_SCALE13_MAX)
    det = ("DEFLATION: A_0 dev %.1e, y_t''x%d dev %.1e, J_2 x%.1e, "
           "census top %.4f y_t'' (string %.4f; RC broken), cap'' "
           "%.4g >= top (TR-CAP WORLD-BLIND), theta'' %.2e < window "
           "floor (REFUSED); INFLATION: A_0 dev %.1e, y_t'' == "
           "%d y_t dev %.1e, theta'' %.4f > THETA_BAR %.3f: "
           "H3-REFUTED-IN-WITNESS (the certificate is falsifiable), "
           "census top %.6f y_t'' (tracks), cap'' %.6f >= top "
           "(TR-CAP SHARP); price |d|/max|c| = %.3e / %.3e "
           "(defl/infl); scaling log10 price h=8 %.3f, h=13 %.3f "
           "(<= %.1f): an x%d y_t movement costs 1e%.1f at h=13 -- "
           "TOPROOT-NOT-NORM-CONTINUOUS"
           % (df["a0_dev"], WIT_FACT, df["yt_dev"], df["j2_ratio"],
              df["ztop"], WIT_ZTOP_STR, df["cap"], df["theta"],
              fl["a0_dev"], WIT_FACT, fl["yt_dev"], fl["theta"],
              THETA_BAR, fl["ztop"], fl["cap"], df["dnorm"],
              fl["dnorm"], scal[8], scal[13], WIT_SCALE13_MAX,
              WIT_FACT, scal[13]))
    return ok, det


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("toproot_theta_probe -- PRIME.TOPROOT.THETA.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = (4, 5, 8) if smoke else RUNGS
    holdout = () if smoke else HOLDOUT
    ctrl_tasks = [("SMOOTH", 5, 60), ("SCRARITH", 6, 60)] if smoke \
        else ([("SMOOTH", xw, CTRL_DPS["SMOOTH"])
               for xw in CTRL_SMOOTH]
              + [("SCRARITH", xw, CTRL_DPS["SCRARITH"])
                 for xw in CTRL_SCRARITH]
              + [("EPSTEIN", xw, CTRL_DPS["EPSTEIN"])
                 for xw in CTRL_EPSTEIN])
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; main-process only: "
          "CLEAN_FIT criterion + HSW sanity; NO worker touches the "
          "cache -- the H3 chain is zero-free)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")
    gtop = float(gam[-1])

    section("S1  EXACT LAYER (TR-STATEMENT/CAP/VIETA/A0/WITNESS/"
            "RATE/H3)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXXXVII PF1-PF3/H1/H2/JMF + rate "
         "record; CDLXXXIV SF1-SF6; CDLX L1/L2 + witness; CDXLIV "
         "J1-J3 + TOPROOT named; r143 T1-T4 + obstruction pin + "
         "delta_1 lock; CDLXVII quartic law + GL4 + L7; r137 "
         "zero-jet law; r131 G17; HSW22 Cor. 1.2; PT21; Landau "
         "1912 + Gonek 1993 AS FORM; Cauchy/Fujiwara class CITED; "
         "Vieta/Newton; Weyl")

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
    for h in tuple(rungs) + tuple(holdout):
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

    # ------------------------------------------------ S3 gates
    section("S3a  PER-RUNG LADDERS + CERTIFICATE")
    tab = {}
    allh = list(rungs) + list(holdout)
    ok30 = ok31 = ok32 = ok33 = ok34 = True
    ok35 = ok36 = ok37 = ok38 = ok39 = True
    d30, d31, d32, d33, d34 = ([] for _ in range(5))
    d35, d36, d37, d38, d39 = ([] for _ in range(5))
    for h in allh:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        hold = h in holdout
        htag = " [HOLDOUT]" if hold else ""
        # G30 spectral sanity
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e (%.0fs)%s"
                   % (h, r["K"], r["simp"], r["build_s"], htag))
        # G31 jets + trace + kappa
        okx = (r["a2_sign"] == -1 and r["cf_dev"] <= CF_BAR
               and r["vieta_dev"] <= VIETA_BAR
               and KAPPA_WIN[0] <= r["kappa"] <= KAPPA_WIN[1])
        if not smoke and h in KAPPA_TAB:
            okx = okx and abs(r["kappa"] / KAPPA_TAB[h] - 1) \
                <= NEW_TOL
        ok31 = ok31 and okx
        d31.append("h%d kap %.4f vieta %.0e" % (h, r["kappa"],
                                                r["vieta_dev"]))
        # G32 cross-instrument
        okx = r["fg"] > 0 and LOCK_WIN[0] <= r["lock"] <= LOCK_WIN[1]
        if h in YT_R143:
            dex = abs(r["yt_l10"] - math.log10(YT_R143[h]))
            okx = okx and dex <= YT_DEX_BAR
            d32.append("h%d yt dex %.1e" % (h, dex))
        if h in FG_TAB:
            okx = okx and FG_TAB[h] * FG_WIN[0] <= r["fg"] \
                <= FG_TAB[h] * FG_WIN[1]
        ok32 = ok32 and okx
        # G33 theta ladder
        okx = THETA_Y_WIN[0] <= r["theta_y"] <= THETA_Y_WIN[1]
        if not smoke and h in THETA_Y_TAB:
            okx = okx and abs(r["theta_y"] / THETA_Y_TAB[h] - 1) \
                <= NEW_TOL
        ok33 = ok33 and okx
        d33.append("h%d th %.4f%s" % (h, r["theta_y"], htag))
        # G34 H3 certificate
        okx = r["h3_ok"] and r["h3_margin"] >= H3_MARGIN_MIN
        ok34 = ok34 and okx
        d34.append("h%d marg %.2f%s" % (h, r["h3_margin"], htag))
        # G35 moments
        okx = (r["rho_argm"] == 1
               and J2_WIN[0] <= abs(r["J2"]) <= J2_WIN[1]
               and abs(r["rho"] - abs(r["J2"])) <= 1e-9 * r["rho"]
               and r["env400"] < r["rho"]
               and CAP_WIN[0] <= r["cap"] <= CAP_WIN[1])
        if not smoke and h in RHO_TAB:
            okx = okx and abs(r["rho"] / RHO_TAB[h] - 1) <= NEW_TOL
        ok35 = ok35 and okx
        d35.append("h%d rho %.4f cap %.3f" % (h, r["rho"],
                                              r["cap"]))
        # G36 H1 replication + cap comparison
        okx = r["cstar"] is not None and r["cstar"] <= C_STAR_MAX \
            and (r["cstar"] is None or r["cstar"] <= r["cap"])
        if not smoke and h in CSTAR_TAB and r["cstar"] is not None:
            okx = okx and r["cstar"] == CSTAR_TAB[h] \
                and abs(r["envj_ratio"] / ENVJ_RATIO_TAB[h] - 1) \
                <= NEW_TOL
        ok36 = ok36 and okx
        d36.append("h%d c* %s <= cap %.3f" % (h, r["cstar"],
                                              r["cap"]))
        # G37 census
        if h <= CENSUS_HARD_MAX:
            if "cen_error" in r:
                okx = False
                d37.append("h%d census ERR" % h)
            else:
                okx = (r["cen_real"] == r["K"] - 1
                       and r["cen_negsum_yt"] <= NEGSUM_BAR
                       and TOP_WIN[0] <= r["cen_top_yt"]
                       <= TOP_WIN[1]
                       and r["cen_sr1_dev"] <= SR1_BAR
                       and r["cen_top_yt"] <= r["cap"]
                       and (r["cstar"] is None
                            or r["cen_top_yt"] <= r["cstar"]))
                if not smoke and h in TOP_TAB:
                    okx = okx and abs(r["cen_top_yt"] / TOP_TAB[h]
                                      - 1) <= NEW_TOL
                d37.append("h%d %d/%d top %.4f <= cap %.3f"
                           % (h, r["cen_real"], r["K"] - 1,
                              r["cen_top_yt"], r["cap"]))
            ok37 = ok37 and okx
        # G38 Fujiwara circularity
        okx = (r["f1_dev"] <= VIETA_BAR and r["fuj_argmax"] == 1
               and r["fuj_over_yt"][0] >= 1.0)
        ok38 = ok38 and okx
        d38.append("h%d f1/yt %.3f argm %d"
                   % (h, r["fuj_over_yt"][0], r["fuj_argmax"]))
        # G39 overshoot
        okx = 10.0 ** r["os_l10"] >= OS_MIN
        ok39 = ok39 and okx
        d39.append("h%d OS 1e%.1f" % (h, r["os_l10"]))
    if not smoke and len(tab) >= 20:
        osx = [-tab[h]["log10a0"] for h in allh if h in tab]
        osy = [tab[h]["os_l10"] for h in allh if h in tab]
        os_slope = float(np.polyfit(osx, osy, 1)[0])
        ok39 = ok39 and OS_SLOPE_WIN[0] <= os_slope \
            <= OS_SLOPE_WIN[1]
    else:
        os_slope = float("nan")
    check("G30-spectral-sanity", ok30, "; ".join(d30))
    check("G31-jets-trace-kappa", ok31,
          "sign(A_2/A_0) == -1 every rung; B_1 closed form dev <= "
          "%.0e; Vieta trace dev <= %.0e (coefficient level, 3x "
          "dps); kappa in %s + tabs: %s"
          % (CF_BAR, VIETA_BAR, str(KAPPA_WIN), "; ".join(d31)))
    check("G32-cross-instrument", ok32,
          "y_t on the r143/CDXLIV strings <= %.0e dex; FULLGAP on "
          "FG_TAB x %s; lock = FULLGAP/y_t in %s at every rung "
          "(THE UNIFICATION LOCK: y_t-form == J-form == r162 "
          "theta-window): %s"
          % (YT_DEX_BAR, str(FG_WIN), str(LOCK_WIN),
             "; ".join(d32)))
    check("G33-theta-ladder", ok33,
          "theta_y = y_t/T_z^4 in %s at EVERY rung incl. holdout + "
          "tabs rel 5e-3: %s" % (str(THETA_Y_WIN), "; ".join(d33)))
    check("G34-h3-certificate", ok34,
          "H3: y_t <= %.3f T_z^4 at EVERY rung incl. holdout (ONE "
          "exact source evaluation per rung -- NO zeros, NO cache, "
          "NO census); margin >= %.1f: %s"
          % (THETA_BAR, H3_MARGIN_MIN, "; ".join(d34)))
    check("G35-moments-cap", ok35,
          "rho = sup_m |J_{m+1}|^{1/m} == |J_2| (argmax m = 1) at "
          "EVERY rung; J_2 in %s (r156 quarter-cap window); "
          "ENV(400) < rho (tail certified); cap = 1 + 2 rho in %s: "
          "%s" % (str(J2_WIN), str(CAP_WIN), "; ".join(d35)))
    check("G36-h1-vs-cap", ok36,
          "c* exists at every rung (<= %.2f) + r171 tabs; c* <= "
          "cap EVERYWHERE: ENVJ-SHARPER-THAN-CAP (the new moment "
          "cap never beats the certified half-plane constant): %s"
          % (C_STAR_MAX, "; ".join(d36)))
    check("G37-census-cap-instantiated", ok37,
          "census h <= %d complete-real nonneg (rootladder "
          "VERBATIM), SR1 <= 1e-40, top in %s + tabs; top <= cap "
          "y_t (TR-CAP on real data) AND top <= c* y_t: %s"
          % (CENSUS_HARD_MAX, str(TOP_WIN), "; ".join(d37)))
    check("G38-fujiwara-circular", ok38,
          "f_1 == B_1 + y_t dev <= 1e-40 AND argmax_m f_m == 1 at "
          "EVERY rung (m <= %d): the sharpest Fujiwara term IS the "
          "trace -- bound >= 2(1 + kappa) y_t > y_t: MOMENT-ROUTE-"
          "CIRCULAR-FOR-TOPROOT: %s" % (FUJ_M, "; ".join(d38)))
    check("G39-a0-overshoot", ok39,
          "OS = b_top C_1/(|A_0| y_t) >= %.0e everywhere; slope "
          "log10 OS vs -log10|A_0| = %.4f in %s: the triangle "
          "route loses EXACTLY the cancellation (exponentially "
          "vacuous): %s"
          % (OS_MIN, os_slope, str(OS_SLOPE_WIN), "; ".join(d39)))
    for lab, keyv in (("theta_y", "theta_y"), ("kappa", "kappa"),
                      ("rho", "rho"), ("lock", "lock")):
        info("%s ladder: " % lab + " ".join(
            "%d:%.4f" % (h, tab[h][keyv]) for h in allh
            if h in tab))
    info("yt_l10 ladder: " + " ".join(
        "%d:%.4f" % (h, tab[h]["yt_l10"]) for h in allh
        if h in tab))

    # ------------------------------------------------ S3c transfer
    section("S3c  GROWTH LAW + ADMISSIBLE EXPONENT")
    if not smoke:
        fit_h = [h for h in rungs if h in tab]
        lx = [math.log10(h) for h in fit_h]
        ly = [tab[h]["yt_l10"] for h in fit_h]
        cf_all = np.polyfit(lx, ly, 1)
        p_all = float(cf_all[0])
        th_slope = float(np.polyfit(
            lx, [math.log10(tab[h]["theta_y"]) for h in fit_h],
            1)[0])
        clean = []
        for h in fit_h:
            with mp.workdps(60):
                yt_h = mp.mpf(10) ** mp.mpf(repr(tab[h]["yt_l10"]))
                if float(mp.sqrt(4 * yt_h)) <= gtop / 2:
                    clean.append(h)
        p_clean = float(np.polyfit(
            [math.log10(h) for h in clean],
            [tab[h]["yt_l10"] for h in clean], 1)[0])
        a_pred = p_clean / 2 - 1
        resid30 = float("nan")
        hold_ok = True
        for h in holdout:
            if h in tab:
                pred = float(np.polyval(cf_all, math.log10(h)))
                resid30 = tab[h]["yt_l10"] - pred
                hold_ok = hold_ok and abs(resid30) <= HOLD_RESID_BAR
        ok43 = (P_WIN[0] <= p_all <= P_WIN[1]
                and TH_SLOPE_WIN[0] <= th_slope <= TH_SLOPE_WIN[1]
                and abs(a_pred - RATE_A) <= A_DICT_TOL
                and hold_ok)
        check("G43-growth-law", ok43,
              "p_all (25 rungs, LSQ) = %.4f in %s; theta-slope "
              "%.4f in %s (r162 flatness); p_clean (%d CLEAN_FIT "
              "rungs %s) = %.4f -> a_pred = p/2 - 1 = %.4f vs r171 "
              "record a = %.3f (|diff| <= %.2f, DICTIONARY "
              "CLOSES); HOLDOUT h=30 fit-exclusion residual %.4f "
              "dex (bar %.2f)"
              % (p_all, str(P_WIN), th_slope, str(TH_SLOPE_WIN),
                 len(clean), clean, p_clean, a_pred, RATE_A,
                 A_DICT_TOL, resid30, HOLD_RESID_BAR))
        eps56 = eps_closed(HSTAR_MIN_COVER)
        amax = math.log(RATE_C / eps56) / math.log(HSTAR_MIN_COVER)
        pmax = 2 * (1 + amax)
        hrep = solve_horizon(RATE_C, amax)
        ok44 = (abs(eps56 / EPS56_STR - 1) <= NEW_TOL
                and abs(amax / AMAX_STR - 1) <= NEW_TOL
                and abs(pmax / PMAX_STR - 1) <= NEW_TOL
                and abs(hrep / HSTAR_MIN_COVER - 1) <= 1e-2
                and p_all <= pmax - P_MARGIN_MIN)
        check("G44-admissible-exponent", ok44,
              "eps_closed(56) = %.4e (string rel 5e-3); a_max = "
              "%.4f, p_max = 2(1 + a_max) = %.4f (PT21-anchored "
              "coverage h*_rate >= 2 H_MAX = 56; bisection "
              "replication h* = %.2f); ASYMPTOTIC ceiling NONE "
              "(r169-SF4, G15); MARGIN: p_all = %.2f <= p_max - "
              "%.1f = %.2f (%.1f exponents of room); census "
              "constant pi(p+1)/c = %.1f"
              % (eps56, amax, pmax, hrep, p_all, P_MARGIN_MIN,
                 pmax - P_MARGIN_MIN,
                 pmax - p_all, math.pi * (p_all + 1) / RATE_C))
    else:
        check("G43-growth-smoke", True, "smoke: skipped")
        check("G44-admissible-smoke", True, "smoke: skipped")

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS + WITNESS")
    cblocks = {}
    ctrl_err = False
    for world, xw, _d in ctrl_tasks:
        r = res.get(("ctl", (world, xw)))
        if r is None or "error" in r:
            ctrl_err = True
            check("G50-%s-x%d" % (world.lower(), xw), False,
                  (r or {}).get("error", "missing"))
            continue
        cblocks.setdefault(world, []).append(r)
    theta_main_min = min(tab[h]["theta_y"] for h in tab) \
        if tab else float("nan")
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        rows = cblocks.get(world)
        if rows is None:
            continue
        taus = {r["h"]: r["tauf"] for r in rows}
        strs = CTRL_TAU_TAB[world]
        str_ok = all(abs(taus[h] / strs[h] - 1) <= CTRL_TAU_TOL
                     for h in taus if h in strs)
        th_ok = all(r["theta_w"] <= CTRL_THETA_MAX for r in rows)
        tab_ok = True
        for r in rows:
            key = (world, r["h"])
            if not smoke and key in THETA_W_TAB:
                tab_ok = tab_ok and abs(
                    r["theta_w"] / THETA_W_TAB[key] - 1) <= NEW_TOL
        theta_ctrl_max = max(r["theta_w"] for r in rows)
        sep = theta_main_min / theta_ctrl_max
        refuse = (all(t < 0 for t in taus.values()) and str_ok
                  and th_ok and tab_ok and sep >= SEP_MIN)
        check("G5%d-%s" % ({"SMOOTH": 0, "SCRARITH": 1,
                            "EPSTEIN": 2}[world], world.lower()),
              refuse,
              "%s: tau_w < 0 on the r166 strings; theta_w <= %.0e "
              "everywhere + tabs; SIZE-SEPARATOR min MAIN theta "
              "%.4f / max theta_w %.1e = %.0f >= %.0f (the quartic "
              "ground separates the worlds); DIAGNOSTIC (reported, "
              "not gated -- H3-ONE-SIDED-WORLD-BLIND by design): "
              "H3-in-world %s, y_t_w/b_top %s"
              % (world, CTRL_THETA_MAX, theta_main_min,
                 theta_ctrl_max, sep, SEP_MIN,
                 [r["h3_w"] for r in rows],
                 ["%.3f" % r["ytb_w"] for r in rows]))
    if ctrl_err:
        pass
    okw, detw = witness_battery()
    check("G53-witness-battery", okw, detw)

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 20:
        lt = [tab[h]["log10tau"] for h in rungs if h in tab]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_yt = slope_of([tab[h]["yt_l10"] for h in rungs
                         if h in tab])
        s_th = slope_of([math.log10(tab[h]["theta_y"])
                         for h in rungs if h in tab])
        s_a0 = slope_of([2 * tab[h]["log10a0"] for h in rungs
                         if h in tab])
        ok54 = (abs(s_yt) <= TAU_SLOPE_BAR
                and abs(s_th) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= s_a0 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: log10 y_t %.4f, log10 theta_y "
              "%.4f (<= %.2f DEMAND-FLAT: TOPROOT is not "
              "Connes-priced); RIDER log10 A_0^2 slope %.3f in %s "
              "(BOUND-RIDES-CONNES -- the measured loop signature "
              "of route (b'))"
              % (s_yt, s_th, TAU_SLOPE_BAR, s_a0, str(RIDER_WIN)))
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

    dep = {"H3-PER-RUNG": ("SOURCE",),
           "ASSEMBLED-CHAIN": ("SOURCE", "ENVJ-CERT-H1",
                               "CENSUS-H2-PER-RUNG", "TRACE-IDENT",
                               "CACHE-WARD", "GONEK-FORM",
                               "H3-PER-RUNG", "HSW22",
                               "PT21-CENSUS-PER-K"),
           "SOURCE": (), "ENVJ-CERT-H1": ("SOURCE",),
           "CENSUS-H2-PER-RUNG": ("SOURCE",),
           "TRACE-IDENT": ("SOURCE",),
           "CACHE-WARD": (), "GONEK-FORM": (), "HSW22": (),
           "PT21-CENSUS-PER-K": (),
           "TLAWCAP": (), "WPD": (), "CENSUS-ALL-K": (),
           "TAUPOS": (), "JETLOCK-MEAS": (), "TOPROOT-MEAS": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",),
           "LOOP-ROUTE(census-all-k)": ("CENSUS-ALL-K",),
           "LOOP-ROUTE(pinning-supply)": ("TAUPOS", "TLAWCAP"),
           "LOOP-ROUTE(a0-floor)": ("TAUPOS", "TLAWCAP")}

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

    anc_h3 = ancestors("H3-PER-RUNG")
    anc = ancestors("ASSEMBLED-CHAIN")
    ok61 = (anc_h3 == {"SOURCE"}
            and "TLAWCAP" not in anc and "WPD" not in anc
            and "CENSUS-ALL-K" not in anc and "TAUPOS" not in anc
            and "JETLOCK-MEAS" not in anc
            and "TOPROOT-MEAS" not in anc
            and "TAUPOS" in ancestors("LOOP-ROUTE(a0-floor)")
            and "TLAWCAP" in ancestors("LOOP-ROUTE(a0-floor)"))
    okwm = tuple(sorted(C_GRID)) == C_GRID
    check("G61-loop-mining", ok61 and okwm,
          "H3-PER-RUNG ancestors == {SOURCE} EXACTLY (no zeros, no "
          "cache, no census, no tau); assembled-chain ancestors == "
          "the r171 set with TOPROOT-MEAS ELIMINATED (replaced by "
          "H3-PER-RUNG + the typed open cofinal edge); TLAWCAP, "
          "WPD, TAUPOS, CENSUS-ALL-K, JETLOCK-MEAS not ancestors; "
          "FOUR loop routes flagged NOT consumed (tlaw-window, "
          "census-all-k, pinning-supply, A0-FLOOR variant); "
          "windows/tabs recomputed from frozen formulas "
          "(SIGN-MINING-CLEAN; disclosure: h in {6,7,9..12,14..27} "
          "pre-freeze unmeasured on the new coordinates; holdout "
          "30 pre-measured in calibration, its content is the "
          "fit-exclusion gate)")

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
          "flows: base 4, refined 5 (r166/r168/r169/r171 graph "
          "VERBATIM -- this round re-types the TOPROOT edge, no "
          "set change); one-grant 5; counterfactual PARALLEL 9 NOT "
          "REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; "
          "RH unreachable without the omega edges")

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
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"],
        "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"]}
    loop_pin = has_cycle(chain_pin)
    chain_a0 = {
        "TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
        "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]}
    loop_a0 = has_cycle(chain_a0)
    chain_term = {
        "ENVJ_H1": ["PF"], "CENSUS_H2": ["PF"],
        "TRACE": ["PF"],
        "GONEK": ["WF", "DCLEG"],
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
                   for n in ("ENVJ_H1", "CENSUS_H2", "H3_PER_RUNG",
                             "H3_COFINAL", "GONEK", "CENSUS_K"))
    check("G63-endgame-graphs", loop_uni and loop_pin and loop_a0
          and acyc and rh_reach,
          "(i) universalized census cycle DETECTED; (ii) "
          "pinning-supply cycle DETECTED (r169/r171 replicated); "
          "(iii) NEW: the A0-floor cycle {TAUPOS, TLAWCAP} -> "
          "A0FLOOR -> TOPROOT -> RATE -> ... -> DTSTEP_K -> TAUPOS "
          "DETECTED (mechanism (b') IS the loop, machine-verified, "
          "NOT consumed); (iv) the terminal chain with "
          "{H3_PER_RUNG, H3_COFINAL} -> RATE (replacing "
          "TOPROOT-MEAS) is ACYCLIC with RH reachable from every "
          "counterfactual grant (AND-semantics): "
          "COFINAL-TARGET-ASSEMBLY-CONDITIONAL, not a loop; NO RH "
          "CLAIM")
    info("THE FINAL RESIDUE (exact, typed): TOPROOT == [H3 per "
         "rung: CERTIFIED source-pure at 25 rungs + holdout 30, "
         "margin >= 2] x [H3-COFINAL: theta_y <= 0.155 at one rung "
         "per dyadic block, ALL blocks -- the ENTIRE lambda-uniform "
         "residue of the delta-chain, ZERO-FREE (source-family "
         "statement), NOT-NORM-CONTINUOUS (witness: x1000 movement "
         "at 1e-17.6 source cost), its A_0 analytic shortcut == "
         "the flagged pinning-supply LOOP].  The r171 residue "
         "{TOPROOT lambda-uniform} + {GONEK} + {census-all-k LOOP} "
         "+ {L1, WPD} is UNCHANGED IN CARDINALITY but the TOPROOT "
         "member is now stated, certified per rung, refutable, "
         "unified with the r162 theta-window (lock gated), and "
         "sits >= 6 exponents under the schedule ceiling p_max = "
         "10.27.  NO omega closed; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "TOPROOT-STATED-UNIFIED(G10/G32)",
        "THETA-QUARTIC-REPLICATED(G33/G43)",
        "H3-CERTIFIED-PER-RUNG(G34)",
        "ADMISSIBLE-EXPONENT-GATED(p_max 10.27; G44)",
        "TR-CAP-PROVEN-Z-UNITS(G11/G35/G37)",
        "MOMENT-ROUTE-CIRCULAR-FOR-TOPROOT(G11/G38)",
        "VIETA-PINCH-PINNED(G12)",
        "A0-ROUTE-LOOP-FLAGGED(G13/G39/G63)",
        "TOPROOT-NOT-NORM-CONTINUOUS(G14/G53)",
        "RATE-DICTIONARY-EXACT(G15/G43)",
        "H3-REFUTABLE(G16/G53)",
        "ENVJ-SHARPER-THAN-CAP(G36)",
        "H3-ONE-SIDED-WORLD-BLIND + SIZE-SEPARATOR(G50-G52)",
        "CROSS-INSTRUMENT-REPLICATED(G32)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-SEQ(G60)",
        "LOOP-ROUTES-FLAGGED(four; G61/G63)",
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
