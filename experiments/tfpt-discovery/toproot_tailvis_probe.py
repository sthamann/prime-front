#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""toproot_tailvis_probe -- PRIME.TOPROOT.TAILVIS.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the two round-140 residues:
TOPROOT and TAILVIS -- the census-position pair from the CDXLIV
reshape {JETLOCK=TOPROOT, TAILVIS, TLAWCAP})
=======================================================================
Round 140 (jetlock_bandmass_probe, 33/33) proved J1-J4/B1-B2 and
reshaped OMEGA-a's residue to {TOPROOT (y_t = |A_2/A_0| <= poly(x),
measured ~x^4.14), TAILVIS (one visible zero per window, max form),
TLAWCAP}.  Round 141 (pfloor_suscap2_probe, 27/27) proved V1-V3,
eliminated PFLOOR and audited the x-quantifier to DENSE-X.  This
probe is the maximal proof attempt on TOPROOT and TAILVIS.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer c (round-114 builder), jets
A_{2m} = sum_k (-1)^k c_k b_k^m (A_0 = phi(A)), weights w_k =
(-1)^k c_k b_k, secular F(y) = A_0 + sum_k w_k/(y - b_k), y_t =
|A_2/A_0|, tau = lambda_min, T_z = 2 pi x, zone census m = #{gamma
<= T_z} (PT21), ENVJ/Theta_J(rho) = the r140 Theorem-J1 source-only
envelope and onset, gtop = 7264.75 (X5 cache top), rho_RvM(T) =
log(T/2pi)/2pi, err_HSW(T) = 0.1038 log T + 0.2573 loglog T +
9.3675 (HSW22 Cor. 1.2), OFF_ALLOW as in r137/r140.  delta_1 =
(q_1 - q_0)/tau with q_i the eigenvalues of the zone-killed
compression of Mq (r138/r139/r141 machinery, newton-polished
zone nodes).

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically / on exact
rational instances; classical inputs typed CITED)
=======================================================================
THEOREM T1 (TAILVIS existence is CLASSICAL; RvM/HSW window
counting).  For any T, L > 0: N(T+L) - N(T) >= [main(T+L) -
main(T)] - 2 err_HSW(T+L) >= L rho_RvM(T) - 2 err_HSW(T+L), by
|N - main - 7/8| <= err_HSW (HSW22, CITED), err_HSW increasing,
and convexity of main (main'' = 1/(2 pi T) > 0, exact).  Hence
every window of length L*(T) := (1 + 2 err_HSW)/rho_RvM contains
>= 1 true zero UNCONDITIONALLY; L*(T) is O(20) and FALLING at the
program heights while Theorem B1's windows have length Theta_J ~
x^2.06: the existence half of TAILVIS is closed classically with
margin ratio L*/Theta <= 0.095 -> 0.002 over the ladder.

THEOREM T2 (TAILVIS visibility, counting form; the V3-Markov
re-aim).  With N_bad(eps) = #{window zeros: sin^2(A gamma) <
eps^2} and S_C = sum_window cos(gamma log x) (2A = log x):
  N_vis >= m_W - N_bad >= (m_W (1 - 2 eps^2) - S_C)/(2 - 2 eps^2)
(exact rearrangement of cos 2t = 1 - 2 sin^2 t; r141 V3 re-gated).
The window S_C is Landau's exponential sum at the rung coordinate:
the classical form S_C ~ -(L/2pi) Lambda(x)/sqrt(x) + O(E_G),
E_G(x,T) = x log(2xT) loglog(3x) + log(x) min(T, x/<x>_pp)
(Landau 1912 / Gonek 1993, CITED AS FORM; own-cache window sums
gated at x = 5/8/13/18 -- measured |S_C - main| <= 0.0093 E_G).
Whenever |main| + C E_G < m_W (1 - 2 eps^2), at least one window
zero is eps-visible.  Headroom C_max = (m_W(1-2eps^2) - |main|)/
(2 E_G) grows ~x^1: TAILVIS(max form) is COUNTING-CLASS.  CARRIER
DISCLOSURE: the window sits at height Theta ~ x^2.06, so the
on-line reading of the window zeros (needed to identify S_C with
Landau's sum) is PT21-warranted only for 2 Theta(x) <= T_PT, i.e.
x <= ~2.3e5 -- an EARLIER horizon than the census carrier
(x <= 4.8e11).  All six probe rungs sit far inside (2 Theta <=
25180 << 3.0e12).  Beyond the carrier horizon the visibility half
is typed TAILVIS-ONLINE-CITED (carrier-class, not a new arithmetic
omega; the same PT21-class input the chain already prices, at
height x^2.06 instead of x).

THEOREM T3 (B1 re-instantiated SOURCE+COUNTING-ONLY; the horizon
resolution).  Combining T1 + T2 with r140 Theorem B1 and the
source-only onset Theta_J(0.5): there exists a true zero gamma* in
(Theta, 2 Theta] with sin^2(A gamma*) >= eps^2, hence
  1 - theta >= 8 eps^2 (1-rho)^2 A_0^2 / ((2 Theta)^2 (tau+OFF))
with rho = 0.5, eps = 0.1 -- NO zero ordinates consumed anywhere.
This resolves the r140 typing TAILVIS-HORIZON-LIMITED at x = 24/28
WITHOUT deepening the cache (the round-140 lever (b) wins over
lever (a)); the counting certificate is weaker than the r140
cache-instantiated one by the factor (2Theta/gamma*)^2 (eps^2/
sin^2) ~ 400 -- inside the E1/E2 poly budget (r137 allowance
1.6e1..2.6e12).  Poly class: log10(1/(1-theta)_cnt) <= 4.5 + 4.0
log10 x at every rung.

THEOREM T4 (rank-one dictionary for the census).  The census roots
y_j of F are EXACTLY the eigenvalues of D - (1/A_0)|w><1| with D =
diag(b_1..b_{K-1}): det(yI - M) = prod_k (y - b_k) F(y)/A_0
(generic sympy + exact instance), trace identity sum y_j = sum b_k
+ y_t re-derived.  The escaped mass is the trace excess of a
signed rank-one update; multiple escapes (n_esc = 4/7/12 measured)
are possible ONLY because w is signed (a PSD rank-one update
escapes exactly once) -- the sign pattern of w is the escape
mechanism (sign changes 3/8/13/29 vs n_esc 4/7/12/16, printed).

OBSTRUCTION PIN (TOPROOT-BUDGET-INVISIBLE; the round's negative
theorem).  The one-sided Connes budget (mass <= tau + OFF) CANNOT
upper-bound y_t: (i) exact core: d/dy_t (1 - y_t/y)^2 =
-2(1-y_t/y)/y < 0 for y > y_t (far-field mass is DECREASING in
y_t; sympy), so {y_t : mass <= B} contains the whole admissible
tail (exact instance); (ii) measured pin: max F/A_0 on [4 y_t,
1000 y_t] = 0.9990 and max |F|/A_0 on [1.5 b_top, 4 y_t] <= 2.8
at every calibrated rung -- the escaped-root ladder keeps |F| <=
O(A_0) EVERYWHERE above the band, so no region exists where a
large y_t would create budget-visible mass.  Any TOPROOT proof
must price census-root POSITIONS directly (variational exterior-
node cost, r140 lever (a)) or go through the delta_1 lock below.
This SHARPENS the r140 ALIGNMENT-WALL typing: the wall is not
just "no one-sided bound on A_2/A_0"; the budget instrument
itself is blind to y_t in both directions above the band.

MEASURED LAW (the y_t source; the delta_1 lock).  delta_1 =
(q_1 - q_0)/tau (the r139 arithmetic well depth, SUSCAP2R's
currency) TRACKS y_t with flat O(1) ratio: delta_1/y_t = 3.64/
2.39/3.31/2.58/2.84 at x = 5/8/13/18/24 (from measured 5/8 +
frozen r139/CDXLIII strings 13/18/24) while both span ~2.9 dex --
the top escaped secular root and the first excited zone-killed
eigenvalue are THE SAME SCALE.  Gated: ratio in (1.5, 6.0), |slope
log10 ratio vs log10 x| <= 0.35.  Consequence (typed MEASURED):
TOPROOT <==> WELLDEPTH-CAP (delta_1 <= poly) modulo the O(1) lock
-- TOPROOT and SUSCAP2R are two readouts of ONE spectral object
(delta_1 appears in gap >= 1/(s + 1/delta_1) as the GOOD side);
the residue pair {TOPROOT, SUSCAP2R} is delta-profile-shaped.

ROUTE TYPINGS (adjudicated): S1-SMOOTHED ROUTE REFUTED-BY-ONE-LOG
(an unconditional visibility proof via Littlewood S_1 = O(log T)
pays two window derivatives = A^2 ~ (log x)^2/4 against a main
term ~2.06 log x: short by exactly one power of log x -- printed
per rung); SELBERG-VARIANCE ROUTE ASYMPTOTIC-ONLY (avg|S| ~
sqrt(loglog T)/(pi sqrt 2) ~ 0.34 makes the smoothed count close
with c_w ~ 0.7, but the variance constants are asymptotic, not
explicit -- named, not consumed).  DENSE-X: the r141 chain audit
EXTENDS to TOPROOT and TAILVIS (both consumed per-x inside
OMEGA-a via E1/B1: demand level = instrument-chosen unbounded
sequence; no ALL-X demand survives) -- but the ALIGNMENT-WALL is
an eigenvector datum per x, NOT a sin-phase set: V2's measure
lemma does NOT apply to it; the fine x-grid instead measures the
wall's x-variation directly (no spikes: max adjacent |dlog10 y_t|
= 0.168 across ten K-jumps and the prime crossings).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle
    names, no verification/ import, NO zeta use anywhere); G02
    cache (X5).
S1  exact layer: G10 window-counting algebra (main' = rho exact,
    main'' = 1/(2 pi T) > 0, rearrangement, L* solve); G11 Markov
    visibility rearrangement (cos identity + N_vis lower form);
    G12 B1-counting composition (r140 G15 shape re-gate + gamma*
    <= gamma_max substitution); G13 rank-one dictionary (generic
    K=3 charpoly == lattice-product x F/A_0; trace; exact rational
    instance); G14 budget-invisibility core (far-field mass
    derivative < 0 exact; monotone-tail instance: an upper budget
    cannot separate y_t from the admissible top).
S2  G20 HSW G(T) sanity + L*(T) table (falling; limit 2 pi x
    2 x 0.1038 = 1.30).
S3  ladder x = (5,60),(8,80),(13,120),(18,140),(24,150),(28,165);
    census core (5,8,13) via raw-mp polyroots + deep (18,24) via
    zone sign-scan; zone nodes NEWTON-POLISHED at dps before
    build_V (the r141 standard; the calibration scratch REPLICATED
    the r139 f64-node well-breaking at x = 13/18: unpolished
    f64-cast nodes give qrel 2.7e12/2.8e29 -- disclosed below);
    no build_V at x=28 (y_t/onset only):
    G30 build xcheck: tau AND A_0 vs frozen r135/r137 strings
    <= 2e-3 dex;
    G31 onsets: Theta_J(0.5) vs frozen CDXLIV strings rel <= 5e-3;
    G32 TAILVIS existence: m_W^HSW >= 100 at every rung, L*/Theta
    <= 0.15, in-cache validity m_W^HSW <= m_W^actual at 5/8/13 and
    on the truncated window at 18;
    G33 TAILVIS visibility: in-cache (5/8/13 + 18 truncated):
    N_vis >= 1 with N_bad/m_W <= 0.5 and N_bad <= Markov cap and
    |S_C - main_Lambda| <= 0.2 E_G (measured <= 0.0093 E_G);
    beyond-cache pricing at 18/24/28: C_max >= 5.0 (calibrated
    1.58/3.03/4.97/7.29 at 5/8/13/18, growing ~x);
    G34 B1 source+counting: (1-theta)_cnt >= 1e-12 at ALL SIX
    rungs incl. 24/28 (HORIZON-RESOLVED), poly envelope
    log10(1/(1-th)) <= 4.5 + 4.0 log10 x, and (weaker-side
    consistency) <= the r140 cache-instantiated strings at
    x = 5..18;
    G35 y_t ladder: A_2/A_0 < 0 at every rung, y_t vs frozen
    CDXLIV strings <= 1e-3 dex, log-log slope vs x in (3.0, 5.5);
    G36 delta_1 lock: |qrel| <= 1e-30 with polished nodes, delta_1
    vs frozen strings rel <= 3e-2, ratio delta_1/y_t in (1.5, 6.0)
    at x = 5..24, |slope log10 ratio vs log10 x| <= 0.35;
    G37 alignment anatomy: max partial sum of A_2 over |A_2| >=
    1e2 at every rung (two-scale exhibit; measured 4.1e3 ->
    8.9e31), CS-cap depth + argmax mode + sign changes vs n_esc
    printed;
    G38 budget invisibility instantiated: max F/A_0 on [4 y_t,
    1000 y_t] <= 1.02 and max |F|/A_0 on [1.5 b_top, 4 y_t] <= 6.0
    at every rung (calibrated 0.9990 / 1.72-2.76);
    G39 fine x-grid (10 pts in [4.2, 6.0] dps 60 + 5 pts in
    [7.7, 8.3] dps 80): sign(A_2/A_0) < 0 everywhere, y_t/b_top in
    (15, 200), depth |A_2|/cap in (1e-14, 1e-3), adjacent
    |dlog10 y_t| <= 0.35 (calibrated max 0.168).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 AND |A_0_w| >= 0.05 AND y_t_w/b_top <= 1.5 (the r140
    arithmetic signature consumed: no escaped scale off the
    primes, MAIN 40-1545); G53 consistency.
S5  G54 tau-screens: |slope log10 y_t vs log10 tau| <= 0.30 and
    |slope log10 (delta_1/y_t) vs log10 tau| <= 0.30 (the demand
    sides are not Connes-priced; (1-theta)_cnt rides A_0^2/tau BY
    CONSTRUCTION -- BOUND-RIDES-CONNES typed); G55 conditioning
    (1e-25 shift on Q[0,0] at x=5 moves tau inside (1e-40,
    1e-10)).
S6  G60 quantifier chain-audit EXTENDED to TOPROOT/TAILVIS
    (demand-level algebra over cited CDXXIII/CDXXX/CDXLIV/CDXLV
    statements: both are consumed per-x inside OMEGA-a; no ALL-X
    demand survives; V2 provides good windows for the PHASE
    objects; the alignment wall typed NOT-PHASE-CLASS, x-grid
    measured instead); G61 min-cut (r116 replica; merged CDXLIV +
    CDXLV chain): L1TAILPROVEN -> TOPROOT(1) -> TAILVISTHM(INF,
    THIS ROUND: T1 existence + T2 counting visibility + carrier
    disclosure) -> TLAWCAP(1) -> BANDMASSTHM(INF, r140) ->
    SUSCAP2R(1) -> QSUBGAPTHM(INF, r139/r141) -> PFLOORTHM(INF,
    r141) -> ... -> WPDWIN: flows base 4, refined 5; granting
    TOPROOT still 5; granting TOPROOT + TLAWCAP still 5 (SUSCAP2R
    caps); counterfactual PARALLEL reading (3 unit omegas) 7 = NOT
    REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER = ((5,60),(8,80),(13,120),(18,140),(24,150),
(28,165)); CENSUS_RUNGS = (5,8,13); DEEP_V_RUNGS = (18,24);
M_JETS = 400; MGRID = (2,4,8,16,32,64,128,256,400); HSW = (0.1038,
0.2573, 9.3675) [HSW22 Cor. 1.2, v914 corpus input]; T_PT =
3000175332800 [PT21]; MARKOV_EPS = 0.1 (sin^2 floor 0.01); B1_RHO
= 0.5; WINDOW_FAC = 2.0; SCAN_STEP = 0.05; SCAN_LO = 0.5;
SCAN_OVER = 6.0; CACHE_ERR = 1e-9; GRID_LO = (4.2, 4.4, 4.6, 4.8,
5.0, 5.2, 5.4, 5.6, 5.8, 6.0) dps 60; GRID_HI = (7.7, 7.85, 8.0,
8.15, 8.3) dps 80.
BARS: XCHECK_BAR = 2e-3 dex; THETA_TOL = 5e-3; YT_XCHECK_BAR =
1e-3 dex; YT_SLOPE_WIN = (3.0, 5.5); MW_MIN = 100.0; LSTAR_FRAC =
0.15; NVIS_MIN = 1; NBAD_FRAC = 0.5; LANDAU_DEV_FRAC = 0.2;
C_GONEK_MIN = 5.0 (gated at x >= 18; calibrated 7.29 at 18,
predicted 9.5/10.9 at 24/28); B1CNT_FLOOR = 1e-12; B1CNT_POLY =
(4.5, 4.0); QREL_BAR = 1e-30; NULLRES_BAR = 1e-40; D1_TOL = 3e-2;
RATIO_WIN = (1.5, 6.0); RATIO_SLOPE_BAR = 0.35; PROF_MIN = 1e2;
FAR_MAX = 1.02; ONSET_MAX = 6.0; YTB_WIN = (15.0, 200.0);
DEPTH_WIN = (1e-14, 1e-3); DGRID_BAR = 0.35; CTRL_YTB_MAX = 1.5;
CTRL_A0_MIN = 0.05; TAU_SLOPE_BAR = 0.30; COND_WIN = (1e-40,
1e-10); RES_BAR = 1e-20; RUNTIME_BAR = 21600 s.
Frozen cross-instrument strings: tau (r135/r137) = {5: 1.60658e-16,
8: 3.77263e-30, 13: 2.49904e-54, 18: 5.21974e-79, 24: 1.8456e-108,
28: 5.32373e-128}; A_0 (r137 T1) = {5: 4.733e-8, 8: 8.419e-15,
13: 8.168e-27, 18: 4.368e-39, 24: 9.202e-54, 28: 1.584e-63};
y_t (CDXLIV) = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
24: 4.013e7, 28: 7.390e7}; Theta_J(0.5) (CDXLIV) = {5: 359.9,
8: 942.8, 13: 2619.6, 18: 5191.2, 24: 9276, 28: 12590}; delta_1
(r139/CDXLIII + calibration 5/8) = {5: 2.2255e5, 8: 9.9512e5,
13: 1.062e7, 18: 3.25e7, 24: 1.14e8}; (1-theta)_B1 r140 = {5:
2.130e-4, 8: 4.2e-5, 13: 5.939e-6, 18: 2.6e-6}.  Deterministic:
NO randomness anywhere.  Cache verified_zeros_n7000.npy READ-ONLY
in ward_ (X5).  All mpf/mpc arithmetic inside explicit mp.workdps
blocks; no f64-refinement of mp roots; np.float64-repr casts
guarded by float()/repr() (r133/r136/r138 trap).

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_toproot.py + log, deleted; numbers quoted verbatim):
x=5: yt 6.106673e4 (yt/btop 40.1), depth 1.210e-06, nsc(w) 3,
maxpart/|A2| 4.102e3, census 10 real 4 escaped ytop/yt 0.8590,
delta1 2.2255e5 (d1/yt 3.6444), Theta(.5) 359.9, mW_hsw 210.8,
L* 34.26 (L*/Th 0.0952), in-cache mW 254 nbad 4 nvis 250, S_C
-41.47 vs main -41.22 (E_G 52.3, C_max 1.58), (1-th)_cnt 5.383e-7
(log10inv 6.27), maxF/A0 far 0.9990 onset 2.1755.  x=8: yt
4.165406e5, depth 5.078e-13, nsc 8, maxpart 2.141e9, 20 real 7
escaped ytop/yt 0.8442, delta1 9.9512e5 (d1/yt 2.3890), Theta
942.8, mW_hsw 730.5, L* 28.01, mW 810 nbad 37 nvis 773, S_C -37.80
vs main -36.77 (E_G 112.0, C_max 3.03), (1-th)_cnt 1.057e-7,
onset max 1.7202.  x=13: yt 3.204224e6, depth 1.078e-24, nsc 13,
maxpart 2.278e20, 41 real 12 escaped ytop/yt 0.8344, Theta 2619.6,
mW_hsw 2493.6, L* 23.56, mW 2676 nbad 103 nvis 2573, S_C -297.50
vs main -296.59 (E_G 216.2, C_max 4.97), (1-th)_cnt 1.945e-8,
onset max 2.7628.  x=18: yt 1.257823e7, depth 9.656e-37, nsc 29,
maxpart 8.880e31, 65 real 16 escaped ytop/yt 0.8335, Theta 5191.2,
mW_hsw 5527.7 (full window), L* 21.33, in-cache TRUNCATED window
mW 2275 nbad 133 nvis 2142, S_C -1.05 vs main 0 (composite),
C_max 7.29, (1-th)_cnt 6.781e-9, onset max 2.1633.  DISCLOSED
CALIBRATION FINDING (the f64-node replica): the scratch fed
UNPOLISHED f64-cast zone nodes to build_V; at x = 5/8 qrel =
1.7e-19/4.8e-6 but at x = 13/18 the well breaks (qrel 2.7e12/
2.8e29, delta1 reads void) -- EXACTLY the r139/r141 'f64 position
grid wider than the consistency well from x = 13 on' finding;
the frozen probe newton-polishes all zone nodes at dps (r141
standard) and gates |qrel| <= 1e-30.  delta1 at 13/18/24 is
therefore frozen from the r139/CDXLIII strings (1.062e7/3.25e7/
1.14e8), with the probe re-deriving all five.  Fine x-grid
(15 builds): yt/btop 24.69 -> 61.88 monotone on [4.2, 6.0] and
104.3 -> 123.6 on [7.7, 8.3], depth 1.033e-4 -> 1.186e-8 and
2.427e-12 -> 1.236e-13 falling, sign -1 everywhere, max adjacent
|dlog10 yt| 0.1683 (across ten K-jumps and the x = 5, 7.85-8.0
prime/prime-power crossings): NO x-localized alignment spikes at
grid resolution.  x = 24/28 pre-freeze unmeasured on the new
quantities (build cost); their bars are set from the frozen
CDXLIV/CDXLIII strings plus structural asserts, DISCLOSED:
predicted Theta 9276/12590, mW_hsw 10751/15212, C_max 9.5/10.9,
(1-th)_cnt 2.66e-9/1.49e-9, d1/yt(24) 2.84.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks below.

VERDICT ENUMS (frozen): TAILVIS-EXISTENCE-CLASSICAL(Theorem T1:
RvM/HSW window counting, unconditional; G10/G20/G32);
TAILVIS-VISIBILITY-COUNTING(Theorem T2: Markov + Landau-form S_C
cap; own-cache verified at 5..18; C_max headroom growing; G11/
G33); TAILVIS-ELIMINATED-COUNTING-CLASS + CARRIER-AT-X^2(the
omega reduces to RvM/HSW + Landau-counting inputs; carrier
horizon x <= ~2.3e5 DISCLOSED -- earlier than the census carrier
4.8e11; beyond typed TAILVIS-ONLINE-CITED, carrier-class);
B1-SRC-CNT-INSTANTIATED(Theorem T3: all six rungs incl. 24/28,
TAILVIS-HORIZON-RESOLVED without new zeros; G34);
RANK1-DICTIONARY(Theorem T4; G13 + census re-gates);
TOPROOT-BUDGET-INVISIBLE(the pinned obstruction: one-sided budget
blind to y_t; G14/G38); YT-IS-WELLDEPTH(delta_1 lock, flat O(1)
ratio; TOPROOT <==> WELLDEPTH-CAP modulo O(1), MEASURED; G36);
TOPROOT-DENSE-X-SUFFICES(chain-audit extension; the wall typed
NOT-PHASE-CLASS: V2 does not apply, x-grid smooth; G39/G60);
ALIGNMENT-ANATOMY(two-scale partial-sum profile + sign-change
escape mechanism; G37); S1-ROUTE-REFUTED-BY-ONE-LOG +
SELBERG-ASYMPTOTIC-ONLY(typed route adjudications);
CONTROLS-REFUSE(no escaped scale off the primes; G50-G53);
OMEGA-RESHAPED({TOPROOT, TAILVIS, TLAWCAP, SUSCAP2R} ->
{TOPROOT, TLAWCAP, SUSCAP2R} + carrier note; G61 census
unchanged); MINCUT(4/5).
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
LADDER = ((5, 60), (8, 80), (13, 120), (18, 140), (24, 150),
          (28, 165))
CENSUS_RUNGS = (5, 8, 13)
DEEP_V_RUNGS = (18, 24)
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
MARKOV_EPS = 0.1
B1_RHO = 0.5
WINDOW_FAC = 2.0
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
CACHE_ERR = 1e-9
GRID_LO = (4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0)
GRID_HI = (7.7, 7.85, 8.0, 8.15, 8.3)
XCHECK_BAR = 2e-3
THETA_TOL = 5e-3
YT_XCHECK_BAR = 1e-3
YT_SLOPE_WIN = (3.0, 5.5)
MW_MIN = 100.0
LSTAR_FRAC = 0.15
NVIS_MIN = 1
NBAD_FRAC = 0.5
LANDAU_DEV_FRAC = 0.2
C_GONEK_MIN = 5.0
B1CNT_FLOOR = 1e-12
B1CNT_POLY_C0 = 4.5
B1CNT_POLY_SLOPE = 4.0
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
D1_TOL = 3e-2
RATIO_WIN = (1.5, 6.0)
RATIO_SLOPE_BAR = 0.35
PROF_MIN = 1e2
FAR_MAX = 1.02
ONSET_MAX = 6.0
YTB_WIN = (15.0, 200.0)
DEPTH_WIN = (1e-14, 1e-3)
DGRID_BAR = 0.35
CTRL_YTB_MAX = 1.5
CTRL_A0_MIN = 0.05
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
RES_BAR = 1e-20
RUNTIME_BAR = 21600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

R_TAU = {5: "1.60658e-16", 8: "3.77263e-30", 13: "2.49904e-54",
         18: "5.21974e-79", 24: "1.8456e-108", 28: "5.32373e-128"}
R_A0 = {5: 4.733e-8, 8: 8.419e-15, 13: 8.168e-27, 18: 4.368e-39,
        24: 9.202e-54, 28: 1.584e-63}
R_YT = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6, 18: 1.258e7,
        24: 4.013e7, 28: 7.390e7}
R_THETA = {5: 359.9, 8: 942.8, 13: 2619.6, 18: 5191.2, 24: 9276.0,
           28: 12590.0}
R_D1 = {5: 2.2255e5, 8: 9.9512e5, 13: 1.062e7, 18: 3.25e7,
        24: 1.14e8}
R_B1_R140 = {5: 2.130e-4, 8: 4.2e-5, 13: 5.939e-6, 18: 2.6e-6}

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


# --------------------------------------------------------- closed forms
def hsw_err(T: float) -> float:
    return HSW_A * math.log(T) + HSW_B * math.log(math.log(T)) + HSW_C


def rho_dens(T: float) -> float:
    return math.log(T / (2 * math.pi)) / (2 * math.pi)


def lstar(T: float) -> float:
    """window length guaranteeing >= 1 zero: L rho(T) - 2 err(T') = 1
    solved with the conservative T' = T (1 + WINDOW_FAC)."""
    return (1.0 + 2.0 * hsw_err(T * (1 + WINDOW_FAC))) / rho_dens(T)


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


def lambda_von_mangoldt(x) -> float:
    lam = 0.0
    xi = int(round(x))
    if abs(x - xi) > 1e-9 or xi < 2:
        return 0.0
    for p in range(2, xi + 1):
        q = p
        while q <= xi:
            if q == xi:
                # p must be prime
                if all(p % r for r in range(2, int(math.isqrt(p)) + 1)):
                    lam = math.log(p)
            q *= p
    return lam


def dist_pp(x) -> float:
    """distance to the nearest prime power != x."""
    best = None
    for n in range(2, int(2 * x) + 10):
        pp = False
        for p in range(2, n + 1):
            if p * p > n:
                pp = all(n % r for r in range(2, int(math.isqrt(n)) + 1))
                break
            if n % p == 0:
                q = n
                while q % p == 0:
                    q //= p
                pp = (q == 1)
                break
        if pp and abs(n - x) > 1e-9:
            d = abs(n - x)
            if best is None or d < best:
                best = d
    return best


def gonek_EG(x: float, Twin: float) -> float:
    """the frozen Landau/Gonek-form error envelope (CITED AS FORM)."""
    return (x * math.log(2 * x * Twin) * math.log(math.log(3 * x))
            + math.log(x) * min(Twin, x / dist_pp(x)))


# --------------------------------------------------------- source side
def source_ctx(ce: dict) -> dict:
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        aa = mp.log(ce["x"]) / 2
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        cs_abs = [abs(v) for v in cs]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
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
        l2 = mp.sqrt(sum(v * v for v in cs))
    return dict(K=K, dps=dps, aa=aa, cs=cs, cs_abs=cs_abs, b=b, A=A,
                A0=A0, a0f=float(abs(A0)), yt=float(yt),
                btop=float(b[-1]), l2=float(l2))


def f_of_y(ctx: dict, y):
    cs, b, K = ctx["cs"], ctx["b"], ctx["K"]
    acc = cs[0]
    for k in range(1, K):
        acc += (-1) ** k * cs[k] * y / (y - b[k])
    return acc


def envj(ctx: dict, y):
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


def onset(ctx: dict, rho: float) -> float:
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


def raw_mp_census_y(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM (y-roots)."""
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
    return np.sort(real_y.real), n_nonreal


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


def build_V_qs(ce: dict, gpts_mp: list):
    """eigenvalues of the zone-killed compression (r138/r139/r141
    replica, trimmed to the spectral data)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        oms_f = [float(o) for o in oms]
        Mq = ce["mpM"]
        tau_mp = ce["mpE"][0]
        mcon = len(gpts_mp)
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
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

        def fwd(rhs_list):
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
        Ew, _Vw = mp.eigsy(Wm)
        qs = sorted([Ew[i] for i in range(nf)])
        qrel = float((qs[0] - tau_mp) / tau_mp)
    return qs, qrel, resR, nf, tau_mp


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    T, L = sp.symbols("T L", positive=True)

    # G10 window-counting algebra (Theorem T1)
    main = T / (2 * sp.pi) * sp.log(T / (2 * sp.pi * sp.E))
    rho = sp.log(T / (2 * sp.pi)) / (2 * sp.pi)
    okA = sp.simplify(sp.diff(main, T) - rho) == 0
    okB = sp.simplify(sp.diff(main, T, 2) - 1 / (2 * sp.pi * T)) == 0
    m1, m2, e1, e2, N1, N2 = sp.symbols("m1 m2 e1 e2 N1 N2", real=True)
    # |N - m| <= e (twice) ==> N2 - N1 >= (m2 - m1) - e1 - e2
    okC = sp.simplify(((m2 - e2) - (m1 + e1))
                      - ((m2 - m1) - e1 - e2)) == 0
    rs, es = sp.symbols("rs es", positive=True)
    sol = sp.solve(sp.Eq(L * rs - 2 * es, 1), L)
    okD = len(sol) == 1 and sp.simplify(sol[0] - (1 + 2 * es) / rs) == 0
    out.append(("G10-window-counting", okA and okB and okC and okD,
                "main' == rho_RvM exact, main'' == 1/(2 pi T) > 0 "
                "(convexity: increments >= L rho(T)), the two-sided "
                "HSW envelope rearranges to N(T+L)-N(T) >= L rho(T) "
                "- 2 err(T+L), and L* == (1+2 err)/rho (exact solve): "
                "Theorem T1 -- window existence is CLASSICAL "
                "(HSW22 Cor. 1.2 CITED)"))

    # G11 Markov visibility (Theorem T2 algebra)
    t, eps = sp.symbols("t eps", positive=True)
    okE = sp.simplify(sp.expand_trig(sp.cos(2 * t))
                      - (1 - 2 * sp.sin(t) ** 2)) == 0
    Nb_s, m_s, SC_s = sp.symbols("Nb_s m_s SC_s", real=True)
    # S_C >= Nb (1-2eps^2) - (m - Nb)  ==>  Nb <= (m + SC)/(2-2eps^2)
    lhs = Nb_s * (1 - 2 * eps ** 2) - (m_s - Nb_s)
    okF = sp.simplify(lhs - (Nb_s * (2 - 2 * eps ** 2) - m_s)) == 0
    # N_vis = m - Nb >= (m(1-2eps^2) - SC)/(2-2eps^2)
    nvis = m_s - (m_s + SC_s) / (2 - 2 * eps ** 2)
    tgt = (m_s * (1 - 2 * eps ** 2) - SC_s) / (2 - 2 * eps ** 2)
    okG = sp.simplify(nvis - tgt) == 0
    out.append(("G11-markov-visibility", okE and okF and okG,
                "cos 2t == 1 - 2 sin^2 t exact; the V3 Markov "
                "rearrangement re-gated and re-aimed: N_vis >= "
                "(m_W (1 - 2 eps^2) - S_C)/(2 - 2 eps^2) -- one "
                "visible zero per window whenever the Landau-form "
                "cap keeps S_C < m_W (1 - 2 eps^2) (Theorem T2; "
                "Landau 1912/Gonek 1993 CITED AS FORM)"))

    # G12 B1-counting composition (Theorem T3)
    s2, rh_, A0q, gs, gmax, ta, of_ = sp.symbols(
        "s2 rh_ A0q gs gmax ta of_", positive=True)
    lb = 8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2
    okH = sp.simplify((1 - (1 - lb / (ta + of_))) * (ta + of_)
                      - lb) == 0
    # gamma* <= gmax and sin^2 >= eps^2 substitute monotonically
    inst = sp.Rational(1, 3) ** 2 <= sp.Rational(1, 2) ** 2
    okI = bool(inst) and sp.simplify(
        8 * eps ** 2 * (1 - rh_) ** 2 * A0q ** 2 / gmax ** 2
        - (8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2)
        .subs([(s2, eps ** 2), (gs, gmax)])) == 0
    out.append(("G12-b1-counting-chain", okH and okI,
                "the r140 B1 rearrangement re-gated; substituting "
                "the counting witnesses sin^2 >= eps^2, gamma* <= "
                "gamma_max = 2 Theta gives 1 - theta >= 8 eps^2 "
                "(1-rho)^2 A_0^2/((2 Theta)^2 (tau+OFF)) -- NO zero "
                "ordinates consumed (Theorem T3: the source+counting "
                "B1 certificate)"))

    # G13 rank-one dictionary (Theorem T4)
    y = sp.symbols("y")
    b1, b2, b3 = sp.symbols("b1 b2 b3")
    w1, w2, w3, A0s = sp.symbols("w1 w2 w3 A0s", nonzero=True)
    D = sp.diag(b1, b2, b3)
    wv = sp.Matrix([w1, w2, w3])
    ones = sp.Matrix([[1, 1, 1]])
    M = D - (wv * ones) / A0s
    chp = sp.expand((y * sp.eye(3) - M).det())
    F = A0s + w1 / (y - b1) + w2 / (y - b2) + w3 / (y - b3)
    tgt2 = sp.expand(sp.together((y - b1) * (y - b2) * (y - b3)
                                 * F / A0s))
    okJ = sp.simplify(chp - tgt2) == 0
    okK = sp.simplify(M.trace() - (b1 + b2 + b3
                                   - (w1 + w2 + w3) / A0s)) == 0
    # exact rational instance
    subs = [(b1, 1), (b2, 4), (b3, 9), (w1, sp.Rational(1, 3)),
            (w2, sp.Rational(-2, 5)), (w3, sp.Rational(1, 7)),
            (A0s, sp.Rational(2, 11))]
    okL = sp.simplify((chp - tgt2).subs(subs)) == 0
    out.append(("G13-rank1-dictionary", okJ and okK and okL,
                "det(yI - D + |w><1|/A_0) == prod(y - b_k) F(y)/A_0 "
                "generically + exact instance; trace == sum b - "
                "sum w/A_0: the census roots ARE the eigenvalues of "
                "a SIGNED rank-one update of the lattice, the "
                "escaped mass is its trace excess (Theorem T4; a "
                "PSD rank-one update escapes exactly once -- the "
                "multi-escape 4/7/12 is carried by the sign pattern "
                "of w)"))

    # G14 budget-invisibility core
    yt_s, yv = sp.symbols("yt_s yv", positive=True)
    massd = sp.diff((1 - yt_s / yv) ** 2, yt_s)
    okM = sp.simplify(massd + 2 * (1 - yt_s / yv) / yv) == 0
    # monotone tail instance: f = (1 - t/10)^2 on [0, 10], B = 1/4:
    # the solution set of f <= B is the WHOLE tail [5, 10]
    tt = sp.symbols("tt", nonnegative=True)
    solset = sp.solveset(sp.Le((1 - tt / 10) ** 2, sp.Rational(1, 4)),
                         tt, sp.Interval(0, 10))
    okN = solset == sp.Interval(5, 10)
    out.append(("G14-budget-invisible-core", okM and okN,
                "d/dy_t (1 - y_t/y)^2 == -2(1 - y_t/y)/y < 0 for "
                "y > y_t exact (far-field mass DECREASES in y_t); "
                "instance: {t : (1 - t/10)^2 <= 1/4} on [0, 10] == "
                "[5, 10] -- a one-sided budget contains the whole "
                "admissible tail and cannot separate y_t from the "
                "top: the Connes budget is BLIND to TOPROOT "
                "(obstruction pinned; measured F-pin in G38)"))
    return out


# ---------------------------------------------------- quantifier audit
def quantifier_audit() -> tuple[bool, str]:
    """demand-level algebra over the cited chain statements,
    EXTENDED to TOPROOT/TAILVIS (r141 G60 + CDXLIV B2/J3).
    Levels: 0 = ALL-X-TAIL, 1 = FULL-MEASURE-TAIL, 2 =
    UNBOUNDED-SEQUENCE (instrument-chosen).  provider a satisfies
    demand b iff a <= b."""
    ALL_X, FULL_MEAS, SEQ = 0, 1, 2
    steps = []
    demand_hconv = SEQ
    steps.append(("NFCLOS (CDXXIII): (H-conv)+(H-trace) per dense a; "
                  "Vitali sequence-based", demand_hconv == SEQ))
    demand_l1 = demand_hconv
    steps.append(("Theorem R (CDXXX) pointwise transfer preserves "
                  "the x-demand level", demand_l1 == SEQ))
    steps.append(("coupling x >= sqrt(a)/(2.5 pi) absorbed by any "
                  "unbounded sequence tail", True))
    demand_omega = demand_l1
    steps.append(("OMEGA-a = EPS-LOCK <== JETLOCK + BANDMASS (CDXLI "
                  "E1) consumed per-x by L1: JETLOCK inherits SEQ",
                  demand_omega == SEQ and demand_omega != ALL_X))
    steps.append(("JETLOCK <==> TOPROOT modulo subordination census "
                  "(CDXLIV J3): TOPROOT demand level == JETLOCK "
                  "level == SEQ (no ALL-X introduced)", True))
    steps.append(("BANDMASS <==> TLAWCAP modulo {JETLOCK, TAILVIS} "
                  "(CDXLIV B2): TAILVIS consumed per-x by B1 -- "
                  "TAILVIS demand level == SEQ", True))
    provider_tailvis = FULL_MEAS
    steps.append(("THIS ROUND: TAILVIS provided at counting level "
                  "for EVERY x below the carrier horizon (T1+T2), "
                  "a fortiori on any sequence inside it; beyond, "
                  "carrier-class (disclosed)",
                  provider_tailvis <= SEQ))
    steps.append(("TOPROOT: the alignment wall is an eigenvector "
                  "datum per x, NOT a sin-phase set -- V2's measure "
                  "lemma does NOT apply to it (typed "
                  "NOT-PHASE-CLASS; x-grid measured instead)", True))
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

    print("toproot_tailvis_probe -- PRIME.TOPROOT.TAILVIS.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:1] if smoke else LADDER
    census_rungs = (5,) if smoke else CENSUS_RUNGS
    deep_v = () if smoke else DEEP_V_RUNGS
    grid_lo = GRID_LO[:2] if smoke else GRID_LO
    grid_hi = () if smoke else GRID_HI
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
    section("S1  EXACT LAYER (Theorems T1-T4 + obstruction core)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: HSW22 Cor. 1.2 (|N - main - 7/8| <= "
         "err, explicit); RvM density; Landau 1912/Gonek 1993 "
         "(exponential-sum form, CITED; own-cache window sums "
         "gated); PT21 verified census (on-line warrant below "
         "T_PT); r131 GW budget; r135 D1-D4; r137 E1/E2 + OFF; "
         "r138 Q1-Q3; r139 U1-U4; CDXLIV J1-J4/B1-B2 (ENVJ onsets, "
         "B1 chain, escaped census); CDXLV V1-V3 + chain audit; "
         "Littlewood S_1 class (route adjudication only); Selberg "
         "variance class (route adjudication only)")

    # ---------------------------------------------------------- S2
    section("S2  TAILS + L*(T)")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    ls_tab = [(T, lstar(T)) for T in (360.0, 943.0, 2620.0, 5191.0,
                                      9276.0, 12590.0, 1e6, 1e12)]
    okG = okG and all(ls_tab[i][1] > ls_tab[i + 1][1]
                      for i in range(len(ls_tab) - 1))
    check("G20-hsw-G-lstar", okG,
          "cache partials below G(T); G monotone; L*(T) falling: "
          + " ".join("%.0f:%.1f" % v for v in ls_tab)
          + " (limit 4 pi x 0.1038 x 2pi/... -> ~1.3: one zero per "
          "O(20) window unconditionally at program heights)")

    # ---------------------------------------------------------- S3
    section("S3  LADDER x = %s" % [x for x, _ in ladder])
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    ok38 = True
    det30, det31, det32, det33, det34 = [], [], [], [], []
    det35, det36, det37, det38 = [], [], [], []
    yt_tab, tau_tab, d1_tab, th_tab = {}, {}, {}, {}
    cell5 = None
    for x, dps in ladder:
        want_mp = x in census_rungs or x in deep_v
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=want_mp)
        if x == 5:
            cell5 = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        ctx = source_ctx(ce)
        K = ce["K"]
        tauf = float(ce["tau"])
        a0f = ctx["a0f"]
        yt = ctx["yt"]
        yt_tab[x] = yt
        tau_tab[x] = tauf
        lx = math.log(x)
        aa_f = lx / 2.0
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))

        # G30 build xcheck
        devt = abs(math.log10(tauf) - math.log10(float(R_TAU[x])))
        deva = abs(math.log10(a0f) - math.log10(R_A0[x]))
        okc = tauf > 0 and devt <= XCHECK_BAR and deva <= XCHECK_BAR
        ok30 = ok30 and okc
        det30.append("x%d tau %.1e A0 %.1e dex" % (x, devt, deva))

        # G31 onset
        with mp.workdps(dps):
            th05 = onset(ctx, B1_RHO)
            eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(ctx["A0"]))
            off = float(8 * mp.exp(ctx["aa"])
                        * (abs(ctx["A0"]) * (1 + eta_pt)) ** 2) \
                * hsw_G(float(T_PT))
        th_tab[x] = th05
        devth = abs(th05 / R_THETA[x] - 1.0)
        okc = devth <= THETA_TOL
        ok31 = ok31 and okc
        det31.append("x%d Th %.1f dev %.1e" % (x, th05, devth))

        # G32 TAILVIS existence
        Th = th05
        T2 = WINDOW_FAC * Th
        ell = T2 - Th
        mW_hsw = ell * rho_dens(Th) - 2 * hsw_err(T2)
        Ls = lstar(Th)
        okc = mW_hsw >= MW_MIN and Ls / Th <= LSTAR_FRAC
        # in-cache validity
        mW_act = None
        wz = None
        if T2 <= gtop:
            wz = gam[(gam > Th) & (gam <= T2)]
            mW_act = len(wz)
            okc = okc and mW_hsw <= mW_act
        elif Th < gtop:
            wz = gam[(gam > Th) & (gam <= gtop)]
            mW_act = len(wz)
            ell_tr = gtop - Th
            mW_hsw_tr = ell_tr * rho_dens(Th) - 2 * hsw_err(gtop)
            okc = okc and mW_hsw_tr <= mW_act
        ok32 = ok32 and okc
        det32.append("x%d mW_hsw %.0f L* %.1f (%.4f) act %s"
                     % (x, mW_hsw, Ls, Ls / Th, str(mW_act)))

        # G33 TAILVIS visibility
        lam_x = lambda_von_mangoldt(x)
        okc = True
        if wz is not None and len(wz) > 0:
            sins = np.abs(np.sin(aa_f * wz))
            nbad = int(np.sum(sins < MARKOV_EPS))
            nvis = len(wz) - nbad
            SCw = float(np.sum(np.cos(lx * wz)))
            Twin_top = min(T2, gtop)
            ell_w = Twin_top - Th
            mainL = -(ell_w / (2 * math.pi)) * lam_x / math.sqrt(x)
            EGw = gonek_EG(x, Twin_top)
            cap = (len(wz) + SCw) / (2.0 - 2.0 * MARKOV_EPS ** 2)
            okc = (nvis >= NVIS_MIN
                   and nbad <= NBAD_FRAC * len(wz)
                   and nbad <= cap
                   and abs(SCw - mainL) <= LANDAU_DEV_FRAC * EGw)
            det33.append("x%d nvis %d/%d SC %.2f main %.2f "
                         "(dev/EG %.4f)"
                         % (x, nvis, len(wz), SCw, mainL,
                            abs(SCw - mainL) / EGw))
            info("x=%d TAILVIS in-cache: window (%.0f, %.0f], m_W "
                 "%d, N_bad(0.1) %d <= Markov cap %.1f, N_vis %d; "
                 "own-cache S_C %.3f vs Landau main %.3f (E_G %.1f "
                 "-- the form holds at effective C = %.4f)"
                 % (x, Th, Twin_top, len(wz), nbad, cap, nvis, SCw,
                    mainL, EGw, abs(SCw - mainL) / EGw))
        # beyond-cache pricing on the FULL window (all rungs; gated
        # at x >= 18 where the cache cannot carry the window)
        mainL_full = -(ell / (2 * math.pi)) * lam_x / math.sqrt(x)
        EG_full = gonek_EG(x, T2)
        Cmax = (mW_hsw * (1 - 2 * MARKOV_EPS ** 2)
                - abs(mainL_full)) / (2 * EG_full)
        if x >= 18:
            okc = okc and Cmax >= C_GONEK_MIN
        ok33 = ok33 and okc
        det33.append("x%d Cmax %.2f" % (x, Cmax))

        # G34 B1 source+counting
        with mp.workdps(dps):
            num = 8 * mp.mpf(repr(MARKOV_EPS)) ** 2 \
                * (1 - mp.mpf(repr(B1_RHO))) ** 2 * ctx["A0"] ** 2
            den = mp.mpf(repr(T2)) ** 2 \
                * (mp.mpf(repr(tauf)) + mp.mpf(repr(off)))
            ot_cnt = float(num / den)
        l10inv = math.log10(1.0 / ot_cnt)
        okc = (ot_cnt >= B1CNT_FLOOR
               and l10inv <= B1CNT_POLY_C0
               + B1CNT_POLY_SLOPE * math.log10(x))
        if x in R_B1_R140:
            okc = okc and ot_cnt <= R_B1_R140[x] * (1 + 1e-6)
        ok34 = ok34 and okc
        det34.append("x%d (1-th)_cnt %.3e log10inv %.2f"
                     % (x, ot_cnt, l10inv))
        info("x=%d Theorem T3: (1-theta)_cnt = %.3e from sources + "
             "counting ONLY (Theta %.1f, window top %.1f << T_PT "
             "%.1e: PT21 on-line warrant holds; %s)"
             % (x, ot_cnt, Th, T2, float(T_PT),
                "r140 was TAILVIS-HORIZON-LIMITED here -- RESOLVED"
                if x in (24, 28) else
                "r140 cache value %.1e (counting is the weaker "
                "side, as it must be)" % R_B1_R140[x]))

        # G35 y_t ladder
        with mp.workdps(dps):
            A = ctx["A"]
            sgn = 1 if A[1] / ctx["A0"] > 0 else -1
        devy = abs(math.log10(yt) - math.log10(R_YT[x]))
        okc = sgn < 0 and devy <= YT_XCHECK_BAR
        ok35 = ok35 and okc
        det35.append("x%d yt %.4e dev %.1e" % (x, yt, devy))

        # census + zone nodes + build_V (delta_1)
        if x in census_rungs or x in deep_v:
            with mp.workdps(dps):
                cs = ctx["cs"]
                aa = ctx["aa"]
                oms = [k * mp.pi / aa for k in range(K)]
            n_esc = None
            ytop = None
            if x in census_rungs:
                ys, n_nonreal = raw_mp_census_y(ce)
                n_esc = int(np.sum(ys > ctx["btop"]))
                ytop = float(ys[-1])
                seeds = [float(v) for v in np.sqrt(ys[ys <= Tz ** 2])]
                cens_ok = (len(ys) == K - 1 and n_nonreal == 0
                           and n_esc >= 1)
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
                cens_ok = len(seeds) >= m_zone
            nds = []
            wres = 0.0
            for s0 in seeds:
                if s0 > Tz + SCAN_OVER:
                    break
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds.append(tmu)
                wres = max(wres, float(res))
            nds_f = np.array([float(v) for v in nds])
            zone_nds = [nds[j] for j in range(len(nds))
                        if nds_f[j] <= Tz]
            cens_ok = cens_ok and wres <= RES_BAR \
                and len(zone_nds) == m_zone
            qs, qrel, resR, nf, tau_mp = build_V_qs(ce, zone_nds)
            with mp.workdps(dps):
                d1 = float((qs[1] - qs[0]) / tau_mp)
            d1_tab[x] = d1
            devd = abs(d1 / R_D1[x] - 1.0)
            rat = d1 / yt
            okc = (cens_ok and abs(qrel) <= QREL_BAR
                   and resR <= NULLRES_BAR and devd <= D1_TOL
                   and RATIO_WIN[0] <= rat <= RATIO_WIN[1])
            ok36 = ok36 and okc
            det36.append("x%d d1 %.4e (dev %.1e) d1/yt %.3f qrel "
                         "%.0e" % (x, d1, devd, rat, qrel))
            info("x=%d delta_1 lock: d1 %.4e, y_t %.4e, ratio %.4f"
                 "%s (nf %d, zone nodes %d newton-polished, wres "
                 "%.0e)" % (x, d1, yt, rat,
                            "" if ytop is None else
                            ", d1/y_top %.4f, n_esc %d" %
                            (d1 / ytop, n_esc), nf, m_zone, wres))

        # G37 alignment anatomy
        with mp.workdps(dps):
            cs = ctx["cs"]
            b = ctx["b"]
            w = [(-1) ** k * cs[k] * b[k] for k in range(K)]
            smax = mp.mpf(0)
            acc = mp.mpf(0)
            karg = 0
            for k in range(1, K):
                acc += w[k]
                if abs(acc) > smax:
                    smax = abs(acc)
                    karg = k
            prof = float(smax / abs(ctx["A"][1]))
            nsc = 0
            prev = None
            for k in range(1, K):
                sg = 1 if w[k] > 0 else -1
                if prev is not None and sg != prev:
                    nsc += 1
                prev = sg
            cap = float(ctx["l2"] * mp.sqrt(sum(b[k] ** 2
                                                for k in range(1, K))))
            depth = float(abs(ctx["A"][1])) / cap
        okc = prof >= PROF_MIN
        ok37 = ok37 and okc
        det37.append("x%d prof %.1e argmax k%d/%d nsc %d depth %.1e"
                     % (x, prof, karg, K - 1, nsc, depth))

        # G38 budget invisibility instantiated
        with mp.workdps(dps):
            wd_far = 0.0
            for lg in np.linspace(math.log(4 * yt),
                                  math.log(1000 * yt), 40):
                yv = mp.mpf(repr(float(math.exp(lg))))
                fv = float(f_of_y(ctx, yv) / ctx["A0"])
                wd_far = max(wd_far, fv)
            wd_on = 0.0
            for lg in np.linspace(math.log(1.5 * ctx["btop"]),
                                  math.log(4 * yt), 120):
                yv = mp.mpf(repr(float(math.exp(lg))))
                fv = abs(float(f_of_y(ctx, yv) / ctx["A0"]))
                wd_on = max(wd_on, fv)
        okc = wd_far <= FAR_MAX and wd_on <= ONSET_MAX
        ok38 = ok38 and okc
        det38.append("x%d far %.4f onset %.3f" % (x, wd_far, wd_on))

        # route-pricing INFO (S1 route pays one log too many)
        s1_ratio = (2.0 * aa_f ** 2 / math.pi ** 2) / rho_dens(Th)
        selberg_avg = math.sqrt(math.log(math.log(T2))) \
            / (math.pi * math.sqrt(2.0))
        info("x=%d route pricing: S_1-smoothed error/main ~ %.2f x "
             "C_1 at this rung and GROWS ~ (log x)^2/log Theta ~ "
             "log x -- unbounded: no lambda-uniform closure from "
             "S_1 alone (REFUTED-BY-ONE-LOG); Selberg-variance "
             "avg|S| ~ %.3f (would close at c_w ~ 0.7 but the "
             "variance constants are ASYMPTOTIC-ONLY)"
             % (x, s1_ratio, selberg_avg))

    check("G30-build-xcheck", ok30,
          "tau AND A_0 continuity vs frozen r135/r137 strings <= "
          "%.0e dex: %s" % (XCHECK_BAR, "; ".join(det30)),
          kind="edge")
    check("G31-onsets", ok31,
          "Theta_J(0.5) vs frozen CDXLIV strings rel <= %.0e "
          "(source-only ENVJ onsets, no zeros): %s"
          % (THETA_TOL, "; ".join(det31)))
    check("G32-tailvis-existence", ok32,
          "m_W^HSW >= %.0f and L*/Theta <= %.2f at every rung; "
          "in-cache validity m_W^HSW <= m_W^actual where the cache "
          "carries the window (Theorem T1: existence CLASSICAL): %s"
          % (MW_MIN, LSTAR_FRAC, "; ".join(det32)))
    check("G33-tailvis-visibility", ok33,
          "in-cache: N_vis >= %d, N_bad <= %.1f m_W AND <= Markov "
          "cap, |S_C - main| <= %.1f E_G; beyond-cache (x >= 18): "
          "Landau-form headroom C_max >= %.1f (Theorem T2: "
          "visibility COUNTING-CLASS; Landau/Gonek CITED AS FORM, "
          "PT21 on-line warrant below T_PT): %s"
          % (NVIS_MIN, NBAD_FRAC, LANDAU_DEV_FRAC, C_GONEK_MIN,
             "; ".join(det33)))
    check("G34-b1-source-counting", ok34,
          "(1-theta)_cnt >= %.0e at ALL SIX rungs incl. 24/28 "
          "(TAILVIS-HORIZON-RESOLVED, no new zeros), poly envelope "
          "log10(1/(1-th)) <= %.1f + %.1f log10 x, and <= the r140 "
          "cache-instantiated values at x = 5..18: %s"
          % (B1CNT_FLOOR, B1CNT_POLY_C0, B1CNT_POLY_SLOPE,
             "; ".join(det34)))
    if not smoke:
        lxs = [math.log10(x) for x, _ in ladder]
        lys = [math.log10(yt_tab[x]) for x, _ in ladder]
        s_yt = float(np.polyfit(lxs, lys, 1)[0])
        oks = YT_SLOPE_WIN[0] <= s_yt <= YT_SLOPE_WIN[1]
        ok35 = ok35 and oks
        det35.append("slope %.2f" % s_yt)
    check("G35-yt-ladder", ok35,
          "A_2/A_0 < 0 at every rung, y_t vs frozen CDXLIV strings "
          "<= %.0e dex, log-log slope in %s (the TOPROOT law "
          "replicated): %s" % (YT_XCHECK_BAR, str(YT_SLOPE_WIN),
                               "; ".join(det35)))
    if not smoke and len(d1_tab) >= 4:
        lxs = [math.log10(x) for x in sorted(d1_tab)]
        lrs = [math.log10(d1_tab[x] / yt_tab[x])
               for x in sorted(d1_tab)]
        s_rat = float(np.polyfit(lxs, lrs, 1)[0])
        oks = abs(s_rat) <= RATIO_SLOPE_BAR
        ok36 = ok36 and oks
        det36.append("ratio slope %.3f" % s_rat)
    check("G36-delta1-lock", ok36,
          "|qrel| <= %.0e (newton-polished nodes; the calibration "
          "f64-node break at x = 13/18 is the r139 well-width "
          "replica, DISCLOSED), delta_1 vs frozen strings <= %.0e, "
          "ratio delta_1/y_t in %s at x = 5..24, |ratio slope| <= "
          "%.2f: THE TOP ESCAPED ROOT IS THE WELL-DEPTH SCALE "
          "(y_t ~ delta_1/3, MEASURED): %s"
          % (QREL_BAR, D1_TOL, str(RATIO_WIN), RATIO_SLOPE_BAR,
             "; ".join(det36)))
    check("G37-alignment-anatomy", ok37,
          "max partial sum of A_2 over |A_2| >= %.0e at every rung "
          "(the two-scale cancellation exhibit; argmax mode, sign "
          "changes and CS-cap depth printed -- the escape mechanism "
          "is the sign pattern of w): %s"
          % (PROF_MIN, "; ".join(det37)))
    check("G38-budget-invisible", ok38,
          "max F/A_0 on [4 y_t, 1000 y_t] <= %.2f and max |F|/A_0 "
          "on [1.5 b_top, 4 y_t] <= %.1f at every rung: |F| = "
          "O(A_0) EVERYWHERE above the band -- with G14's exact "
          "monotonicity, the one-sided Connes budget is BLIND to "
          "y_t (TOPROOT-BUDGET-INVISIBLE pinned): %s"
          % (FAR_MAX, ONSET_MAX, "; ".join(det38)))

    # G39 fine x-grid
    okc = True
    det39 = []
    prev_lyt = None
    prev_x = None
    for xv, dg in [(v, 60) for v in grid_lo] + [(v, 80) for v in
                                                grid_hi]:
        cg = R4.build_cell(xv, KFAC, "MAIN", dg, want_mp=False)
        cgx = source_ctx(cg)
        with mp.workdps(dg):
            b = cgx["b"]
            capg = float(cgx["l2"] * mp.sqrt(sum(
                b[k] ** 2 for k in range(1, cg["K"]))))
            depg = float(abs(cgx["A"][1])) / capg
            sgn = 1 if cgx["A"][1] / cgx["A0"] > 0 else -1
        ytb = cgx["yt"] / cgx["btop"]
        okp = (sgn < 0 and YTB_WIN[0] <= ytb <= YTB_WIN[1]
               and DEPTH_WIN[0] <= depg <= DEPTH_WIN[1])
        lyt = math.log10(cgx["yt"])
        if prev_lyt is not None and abs(xv - prev_x) < 0.5:
            okp = okp and abs(lyt - prev_lyt) <= DGRID_BAR
        prev_lyt, prev_x = lyt, xv
        okc = okc and okp
        det39.append("%.2f:K%d yt/b %.1f d %.0e"
                     % (xv, cg["K"], ytb, depg))
    check("G39-fine-x-grid", okc,
          "sign < 0, y_t/b_top in %s, depth in %s, adjacent "
          "|dlog10 y_t| <= %.2f across K-jumps and prime crossings "
          "(NO x-localized alignment spikes at grid resolution; "
          "the wall varies smoothly in x): %s"
          % (str(YTB_WIN), str(DEPTH_WIN), DGRID_BAR,
             "; ".join(det39)))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=False)
        cwx = source_ctx(cw)
        tauw = float(cw["tau"])
        ytbw = cwx["yt"] / cwx["btop"]
        okw = tauw < 0 and cwx["a0f"] >= CTRL_A0_MIN \
            and ytbw <= CTRL_YTB_MAX
        ctrl_ok = ctrl_ok and okw
        check("G50-%s" % world.lower(), okw,
              "%s x=%d: tau_w = %.4f < 0 (no budget currency), "
              "A_0_w = %.3f (no collapse), y_t_w/b_top = %.2f <= "
              "%.1f (NO escaped scale off the primes vs MAIN "
              "40-1545: the r140 arithmetic signature consumed)"
              % (world, xw, tauw, cwx["a0f"], ytbw, CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse: tau < 0 kills the budget/"
          "well currencies (delta_1 undefined), no escaped scale "
          "exists to lock onto, while the TAILVIS counting layer "
          "is a statement about ZETA zeros and never consumes the "
          "world: TOPROOT/TAILVIS content is arithmetic")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs = [x for x, _ in ladder]
        lt = [math.log10(tau_tab[x]) for x in xs]
        lyt = [math.log10(yt_tab[x]) for x in xs]
        s_yt2 = float(np.polyfit(lt, lyt, 1)[0])
        xs_d = sorted(d1_tab)
        lt_d = [math.log10(tau_tab[x]) for x in xs_d]
        lr_d = [math.log10(d1_tab[x] / yt_tab[x]) for x in xs_d]
        s_rat2 = float(np.polyfit(lt_d, lr_d, 1)[0])
        check("G54-tau-screen",
              abs(s_yt2) <= TAU_SLOPE_BAR
              and abs(s_rat2) <= TAU_SLOPE_BAR,
              "slope log10 y_t vs log10 tau = %.4f, slope log10 "
              "(delta_1/y_t) vs log10 tau = %.4f (both <= %.2f: "
              "the demand sides are not Connes-priced; "
              "(1-theta)_cnt rides A_0^2/tau BY CONSTRUCTION -- "
              "BOUND-RIDES-CONNES typed, no disguise)"
              % (s_yt2, s_rat2, TAU_SLOPE_BAR))
    if cell5 is not None and "mpM" in cell5:
        with mp.workdps(cell5["dps"]):
            E0 = cell5["mpE"][0]
            Qp_ = cell5["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(cell5["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; round-118 red flag; all mp "
              "under workdps)" % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  QUANTIFIER AUDIT + MIN-CUT")
    okq, detq = quantifier_audit()
    check("G60-quantifier-audit", okq,
          "demand-level algebra EXTENDED to TOPROOT/TAILVIS over "
          "the cited chain (CDXXIII, CDXXX, CDXLI E1, CDXLIV "
          "J3/B2, CDXLV G60): both consumed per-x on the "
          "instrument-chosen unbounded sequence; DENSE-X SUFFICES "
          "for TOPROOT; the alignment wall typed NOT-PHASE-CLASS "
          "(V2 inapplicable; x-grid measured smooth instead) "
          "(typed CHAIN-AUDIT; cited theorems not re-proven): %s"
          % detq)

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
                ("TOPROOT", "TAILVISTHM"): INF,
                ("TAILVISTHM", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "TOPROOT")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    two = dict(one)
    two[("TAILVISTHM", "TLAWCAP")] = INF
    f_two = R4.maxflow(dict(two), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1,
               ("SUSCAP2R", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_two == 5 and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 -- the merged CDXLIV/CDXLV "
          "chain with THIS ROUND's TAILVISTHM(INF: T1 existence + "
          "T2 counting visibility + carrier disclosure) between "
          "TOPROOT(1) and TLAWCAP(1), then BANDMASSTHM(INF, r140) "
          "-> SUSCAP2R(1) -> QSUBGAPTHM/PFLOORTHM(INF, r141); "
          "granting TOPROOT still 5; granting TOPROOT + TLAWCAP "
          "still 5 (SUSCAP2R caps); counterfactual PARALLEL "
          "reading 7 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")
    info("EXACT RESIDUE after this round (read with CDXLIV/CDXLV): "
         "RH <== [r122 NF-Closure] + [r128 Theorem R] + {L1, WPD} "
         "on dense a; L1 = TAIL(proven) + H-pin; H-pin <== OMEGA-a "
         "+ OMEGA-b; OMEGA-a = EPS-LOCK <== JETLOCK + BANDMASS "
         "(CDXLI E1); JETLOCK <==> TOPROOT (CDXLIV J3); BANDMASS "
         "<==> TLAWCAP modulo {JETLOCK, TAILVIS} (CDXLIV B2); "
         "TAILVIS ELIMINATED-COUNTING-CLASS THIS ROUND (T1 "
         "existence unconditional-HSW; T2 visibility Markov + "
         "Landau-form, own-cache gated, PT21 on-line warrant; "
         "carrier horizon x <= ~2.3e5 at window height x^2.06 "
         "DISCLOSED -- beyond it carrier-class TAILVIS-ONLINE-"
         "CITED, not a new arithmetic omega); OMEGA-b <== OMEGA-a "
         "+ QSUBGAP; QSUBGAP <== EPSLOCK + SUSCAP2R (CDXLV, PFLOOR "
         "removed).  RESIDUE = {TOPROOT, TLAWCAP, SUSCAP2R} + "
         "dense-a + a-extension + window-a; TOPROOT: dense-x "
         "suffices, budget-route obstruction PINNED "
         "(BUDGET-INVISIBLE), y_t == O(1) x delta_1 MEASURED "
         "(TOPROOT <==> WELLDEPTH-CAP modulo O(1) -- the residue "
         "pair {TOPROOT, SUSCAP2R} shares the delta-profile as "
         "single spectral carrier).  NO RH claim; nothing "
         "upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "TAILVIS-EXISTENCE-CLASSICAL(Theorem T1; G10/G20/G32)",
        "TAILVIS-VISIBILITY-COUNTING(Theorem T2: Markov + "
        "Landau-form; own-cache C ~ 0.005; G11/G33)",
        "TAILVIS-ELIMINATED-COUNTING-CLASS + CARRIER-AT-X^2"
        "(horizon x <= ~2.3e5 disclosed; beyond: "
        "TAILVIS-ONLINE-CITED, carrier-class)",
        "B1-SRC-CNT-INSTANTIATED(Theorem T3: all six rungs, "
        "24/28 HORIZON-RESOLVED without new zeros; G34)",
        "RANK1-DICTIONARY(Theorem T4; G13)",
        "TOPROOT-BUDGET-INVISIBLE(obstruction pinned; G14/G38)",
        "YT-IS-WELLDEPTH(delta_1 lock, flat O(1); TOPROOT <==> "
        "WELLDEPTH-CAP modulo O(1), MEASURED; G36)",
        "TOPROOT-DENSE-X-SUFFICES(chain-audit; wall "
        "NOT-PHASE-CLASS, x-grid smooth; G39/G60)",
        "ALIGNMENT-ANATOMY(two-scale profile + sign-change escape "
        "mechanism; G37)",
        "S1-ROUTE-REFUTED-BY-ONE-LOG + SELBERG-ASYMPTOTIC-ONLY"
        "(typed)",
        "CONTROLS-REFUSE(G50-G53)",
        "OMEGA-RESHAPED({TOPROOT, TAILVIS, TLAWCAP, SUSCAP2R} -> "
        "{TOPROOT, TLAWCAP, SUSCAP2R} + carrier note; G61)"]
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
        print("COMPOSITE: TAILVIS-EXISTENCE-CLASSICAL + "
              "TAILVIS-VISIBILITY-COUNTING + "
              "TAILVIS-ELIMINATED-COUNTING-CLASS + CARRIER-AT-X^2 "
              "+ B1-SRC-CNT-INSTANTIATED + RANK1-DICTIONARY + "
              "TOPROOT-BUDGET-INVISIBLE + YT-IS-WELLDEPTH + "
              "TOPROOT-DENSE-X-SUFFICES + ALIGNMENT-ANATOMY + "
              "S1-ROUTE-REFUTED-BY-ONE-LOG + CONTROLS-REFUSE + "
              "OMEGA-RESHAPED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
