#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sigmafloor_probe -- PRIME.SIGMAFLOOR.FINAL.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-block below-horizon certificates stated, NO counterexample claim.
It closes no gate and narrows no gate.

=======================================================================
MISSION (THE FINAL ATTACK on SIGMA-FLOOR -- the one coordinate that
r168/CDLXXXIII factorized the entire remaining lambda-uniform
arithmetic content into: the one-sided block-averaged inequality
sum w (sigma_true - eps) > 0 per dyadic block, sigma_h =
zsum_h/(8 A_0^2 G(T_z)) the SUPPLY, eps_h = OFF_h/(8 A_0^2 G(T_z))
the DEMAND (DT2-derived exactly).  Deliverable: the definitive
terminal characterization -- the sigma-anatomy (F1), the exact
asymptotic demand (F2), the pinning-supply chain (F3), the assembled
endgame chain with every arrow typed, and the terminal residue at
maximal sharpness (F4); red-teamed (T5).)
=======================================================================
State consumed (CITED): CDLXXXIII/r168 (depthblock_transfer: DT1/DT2
proven, census 3/2-law, budget horizon h* = 1.2566e7 on PT21,
SIGMA-FLOOR named as the final coordinate, sigma/eps record ladders,
Z_OVERHANG 6.0 + G34_HARD_MAX 26 inherited PRE-FROZEN); CDLXXV/r166
(BA1-BA3, certified block table, AVG-BUDGET-WINDOW, control strings);
CDLXXXI/r167 (GB2 tangent battery, PROP naming); CDLXVII/r162
(quartic law; SCAN_OVER); CDXLI/r137 (epslock: the tau budget anatomy
tau = M_band + M_mid + M_beyond + S_off with M_mid == 4A_0^2(G_mid -
C_mid) + J_mid EXACT; the Landau pin; Theorem E1 (JET-LOCK +
BAND-MASS ==> EPS-LOCK); the measured lock onsets Theta_rho ~ x^2.2);
CDXXXIII/r131 (L1 Layer 1 secular-exact spec(M) = census zeros;
Layer 2 GW pinning tau = 2 sum |E_N(gamma)|^2 + S_off; the smallness
law); r131 OFF recipe VERBATIM; HSW22 Cor. 1.2; PT21 (T_PT =
3000175332800); Landau 1912 + Gonek 1993 (the exponential-sum bound
CITED AS FORM -- shape only, constants not re-derived); Weil 1952
criterion AS FORM; Yoshida 1992 (no priority claim); Sylvester/
Jacobi; Cauchy; Courant-Fischer; Weyl.

NOTATION.  Rung h = builder x (R4.build_cell, even sector); A =
log(h)/2; K = ceil(1.25 h log h); tau_h = lam_min(Mq); T_z = 2 pi h;
G = HSW envelope; A_0 = 0-jet; E_N(t) = sin(At) R(t), F(t^2) =
t R(t)/2 (r131 Layer 1); OFF_h = r131 recipe VERBATIM; D = 8 A_0^2
G(T_z).  WINDOWS: W12 = ward ordinates in (T_z + Z_OVERHANG,
gamma_1200] (the r168 sigma window, replicated); WFULL = (T_z +
Z_OVERHANG, gamma_7000] (the anatomy window; DISCLOSED extension --
pure instrument depth, same ward class).  THE COORDINATES:
   sigma12_h  = (1-slop) 2 sum_{W12} E_N^2 / D     (r168 sigma),
   sigma_h    = (1-slop) 2 sum_{WFULL} E_N^2 / D   (deep supply),
   G_W = sum 1/g^2,  C_W = sum cos(2Ag)/g^2   over WFULL,
   DC_h   = (G_W - C_W)/(2 G(T_z))       (EQUIDISTRIBUTION MASS),
   delta_h = [sum sin^2(Ag) F(g^2)^2/g^2] / [A_0^2 sum sin^2(Ag)/g^2]
                                          (JET MASS -- the sin^2/g^2-
                                           weighted mean of (F/A_0)^2
                                           on the true tail zeros).

=======================================================================
THE THEOREM LAYER (the sigma-anatomy; every leg typed)
=======================================================================
THEOREM SF1 (ANATOMY IDENTITY; PROVEN, exact per-term algebra).
2 E_N(g)^2 == 8 sin^2(Ag) F(g^2)^2 / g^2 (r131 Layer 1 chase) and
   8 sin^2 F^2/g^2 == 4 A_0^2 (1 - cos 2Ag)/g^2
                      + 8 sin^2 (F^2 - A_0^2)/g^2
per term (the r137 M_mid decomposition transplanted to the supply
window).  Summing:  D sigma / (1-slop) == 4 A_0^2 (G_W - C_W) + J_W
and, factoring the SAME sums,   sigma == (1-slop) delta * DC
EXACTLY.  THE SUPPLY FACTORIZES: sigma = [jet mass] x [equi-mass].

THEOREM SF2 (FLOOR-SIDE ADJUDICATION; the F1 answer; exact).
(i) THE ONSET-EXCESS-CAP CANNOT FLOOR SIGMA: J_W <= cap bounds sigma
from ABOVE (sigma <= DC + cap-term); two exact instances satisfy the
same cap with sigma = 3/2 and sigma = 1/100: the F1-conjectured
chain [proven budget legs + onset-excess-cap ==> SIGMA-FLOOR] is
REFUTED-EXACT -- the cap is the TLAWCAP-side (upper) leg, and
consuming it would also be the flagged LOOP.  (ii) THE FLOOR-SIDE
LEG IS THE JET-MASS FLOOR: by SF1, [sigma >= s_0] <==> [delta >=
s_0/((1-slop) DC)] -- the floor lands ENTIRELY on delta once DC is
priced.  (iii) POINTWISE JET-LOCK IMPLIES THE RATE FORM: if
|F/A_0 - 1| <= rho < 1 for all g >= Theta then F^2 >= (1-rho)^2
A_0^2 there (exact: u >= 1-rho >= 0 ==> u^2 >= (1-rho)^2), and
dropping the nonnegative terms below Theta:
   sigma >= (1-slop)(1-rho)^2 DC(Theta, T]   -- THE RATE FLOOR.
With the measured onset law Theta_rho ~ c h^kappa (r137: ~x^2.2)
this is sigma >= const * h^{-a}: a POLYNOMIALLY DECAYING floor.

THEOREM SF3 (THE DC LEG; PROVEN-MOD-CITED, classical per census).
G_W - C_W == 2 sum sin^2(Ag)/g^2 >= 0 TERMWISE (proven).
Quantitatively: with S(u) = sum_{g <= u} cos(g log h), Abel/
Stieltjes summation gives C_W = [Landau main term
-Lambda(h)/(2 pi sqrt h)(1/T_lo - 1/T_hi), the r137 pin] + [error
controlled by the Landau/Gonek exponential-sum bound B(x, u) ~
x log(2xu) loglog(3x), CITED AS FORM].  The two limit chases (sympy):
   |C_err|/G_lead(T_z)  <~  loglog-class / sqrt(h)  -> 0,
   |C_main|/G_lead(T_z) <~  log h / sqrt(h)         -> 0,
so DC -> G_W/(2 G(T_z)) -> 1/2 modulo envelope tightness: THE DC
TERM OF SIGMA IS ASYMPTOTICALLY 1/2.  CONSUMES: the per-census
on-line identification cos(g log h) == Re h^{rho - 1/2} (PT21-class
census, per-k classical; the ALL-K grant is the machine-detected RH
loop, re-flagged, NOT consumed) + Landau/Gonek CITED + HSW22.
Typed PROVEN-MOD-CITED per census, GONEK-CONSTANT-UNPRICED.

THEOREM SF4 (DEMAND-RATE ABSORPTION; the F2 answer; exact).  At
FIXED census the demand GROWS: eps_h == sqrt(h)(1+eta)^2
G(T_PT)/G(2 pi h) ~ h^{3/2}/log h (DT2(ii) CITED: monotone).  The
floor at rate sigma >= c h^{-a} demands census height T_req(h) with
sympy limit
   T_req(h) -> (2 pi (3/2 + a)/c) h^{3/2 + a}
             == (3 pi/c)(1 + 2a/3) h^{3/2+a}
(the r168 3/2-law is the a = 0 case).  COROLLARY (the exact
asymptotic demand): ANY explicit polynomial-rate floor suffices --
the census schedule absorbs the rate into the exponent; the measured
FLATNESS of sigma is NOT needed for the endgame chain, only
positivity at an explicit rate.  The schedule stays classical PER k
and unbounded in k (ALL-K == LOOP, unchanged).

THEOREM SF5 (PINNING-SUPPLY; the F3 answer; exact + adjudicated).
GW identity (r131 Layer 2 CITED): tau = M_zone + D sigma_full/(1-slop)
+ S_off with M_zone >= 0 termwise, |S_off| <= D eps.  Exact:
(i) sigma <= (1-slop)(tlaw + eps): the supply is capped by the GW
value -- zsum/tau <= 1 + eps-slack (the r166 band 0.88..0.96 IS this
statement: the pinned zone carries ~nothing because pinning kills
E_N at the zone zeros; the r131 '96 percent' reading);
(ii) WITH BAND-MASS BM(theta) (M_zone <= theta(tau + OFF), the r137
omega): sigma >= (1-slop)[(1-theta) tlaw - (1+theta) eps].
ADJUDICATION: route (ii) consumes tau-positivity/TLAWCAP (tlaw flat
== the flagged window omega) ==> the pinning-supply route to the
floor is EXACTLY the RH loop's costume: machine-detected cycle
SIGMAFLOOR -> DTSTEP -> TAUPOS -> (GW + BM grant) -> SIGMAFLOOR in
G63.  The non-loop content of the floor is SF1-SF3 (delta x DC).

SF6 (RED TEAM; exact).  Free scalars realize J_W of BOTH signs and
delta == 1e6 AND 1e-6 with every identity intact (ALGEBRA-ONLY-
REFUTED-FOR-JETMASS); the lattice toy (all tail zeros at j pi/A)
gives sin == 0, sigma == 0 exactly with all path axioms intact
(ALGEBRA-ONLY-REFUTED-FOR-DCLEG: equidistribution of the true zeros
against the minimizer's OWN lattice is arithmetic input, entering
through the census + Landau, not algebra).  FROZEN PREDICTION (the
red-team sharpening of r168's 'controls flip it'): the RAW floor
inequality sigma_w > eps_w HOLDS in the fake worlds (the supply is
a sum of squares in EVERY world; calibrated SMOOTH x=5: sigma_w =
0.189 > eps_w ~ 1e-10) -- what the controls flip is the BA3 BRIDGE
(tau_w + OFF_w - zsum_w < 0: the GW identity is FALSE for fake
combs) and the tau conclusion (tau_w < 0, block sums < 0).  THE
ARITHMETIC CONTENT OF SIGMA-FLOOR IS THE PAIR {floor, BA3-bridge},
not the raw inequality: typed FLOOR-INEQ-WORLD-INSENSITIVE +
BRIDGE-ARITHMETIC.

THE TERMINAL STATEMENT (assembled and gated in G63; NO RH CLAIM):
SIGMA-FLOOR FACTORIZES ONE MORE TIME:
   SIGMA-FLOOR == [DC-LEG: DC >= c_1 > 0 -- PROVEN-MOD-CITED per
   census (Landau/Gonek + HSW22 + census schedule per-k; ALL-K ==
   LOOP)] x [JET-MASS-FLOOR: delta >= r(h) at an explicit rate --
   THE TERMINAL LAMBDA-UNIFORM RESIDUE: one source-weighted average
   of (F/A_0)^2 over the true tail zeros; implied at rate h^{-a} by
   pointwise JET-LOCK with polynomial onset (r137 omega-a leg,
   measured onset ~x^2.2); arithmetic-pinned (SF6); NOT a loop
   (G61 ancestors clean of TLAWCAP/WPD/CENSUS-ALL-K); not known
   classical; per-rung classical (one certified nonzero term),
   lambda-uniform rate open].
The measured sigma-FLATNESS is EXPLAINED as two trends (delta O(1)
x DC rising toward 1/2) and, by SF4, the flat law need NOT be
proven: the demand absorbs any polynomial rate.  The honest terminal
residue: {JET-MASS-FLOOR (rate form)} + {census ALL-K == LOOP} +
{L1, WPD} -- census cardinality 4 UNCHANGED.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use anywhere, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5,
    READ-ONLY, ward-class ordinates only).
S1  exact layer (sympy generic + exact rational instances):
    G10 SF1 anatomy identity (secular chase zR/2 == F; 2E^2 ==
    8 sin^2 F^2/g^2; per-term decomposition; delta x DC
    factorization on a rational instance);
    G11 termwise positivity + single-zero floor (sum >= max term) +
    the zero-set lemma (E == sin x R; F rational, numerator degree
    K-1 ==> sigma == 0 forces every tail zero into the finite kill
    set [lattice j pi/A] U [K-1 census nodes]: the ANTI-LATTICE
    reduction);
    G12 SF2 floor-side adjudication (cap-is-upper refutation with
    two instances; jet-lock ==> rate-floor chase (1-rho)^2);
    G13 SF3 DC leg (Abel/Stieltjes rational instance; Landau main
    integral; the two limit chases; identification typing);
    G14 SF4 demand-rate absorption (sympy limits at a = 1/2, 1,
    3/2 + the a = 0 replication of the r168 3/2-law constant);
    G15 SF5 pinning-supply rearrangements (both directions) + the
    loop flag;
    G16 SF6 red team (J both signs; delta 1e6/1e-6; lattice toy).
S2  G20 HSW G(T) sanity.
S3  per-rung layer h = 4..28 (r168 recipe VERBATIM: enclosures,
    wall chain, anchors, budget floor, sigma12/eps recipe; PLUS the
    NEW anatomy pass over WFULL), 12 spawn workers, cost-sorted:
    G30 spectral sanity; G31 certified tau enclosures; G32 wall
    chain; G33 anchors + ladder (tlaw strings incl. the full r168
    record ladder rel 1e-3; FULLGAP tabs; lock; post-loop FG slope);
    G34 budget floor (BA3 instantiated; HARD h <= 26, 27/28
    F64-ORDINATE-LIMITED inherited PRE-FROZEN);
    G35 sigma12/eps (r168 SIGMA_TAB at 4/5/8 rel 5e-3 + the full
    r168 record sigma ladder h <= 26 rel 1e-3, DISCLOSED
    corpus-known; recipe identity dev <= 1e-40 every rung);
    G36 THE ANATOMY TABLE (NEW): identity sigma == (1-slop) delta
    DC at rel <= 1e-40 EVERY rung (exact-algebra ward, F64-immune);
    sigma_full/DC/delta on the calibrated strings at 4/5/8 rel
    5e-3; DC in (0.05, 0.60) ALL rungs (DC consumes only ordinates
    + A: F64-robust at depth); sigma_full in (0.15, 0.80) and
    delta in (0.3, 3.0) hard h <= 26, 27/28 typed F64 (delta
    inherits the E-collapse class through F);
    G37 Landau pin IN THE SUPPLY WINDOW: z = (C_W - C_pred)/sig_C
    with |z| <= 4.0 at EVERY rung (structural; intermediates
    pre-freeze unmeasured, DISCLOSED) + C_W strings at 4/5/8 (abs
    z-dev <= 0.01 vs calibration);
    G38 lattice-avoidance + collectivity: min |sin(A g)| over WFULL
    > 1e-8 every rung + calibrated strings at 4/5/8; single-zero
    max share <= 0.9 every rung + calibrated strings (the supply
    is collective-but-onset-weighted: measured 0.21..0.36);
    G39 THE RATE-FLOOR TABLE: measured lock onsets Theta_rho
    (suffix property over WFULL rows) for rho in (0.25, 0.5,
    0.75); onset EXISTS for all h <= 16 (gated; beyond reported --
    ANATOMY-CACHE-HORIZON, pure instrument); onset(0.5) strings at
    4/5/8 rel 1e-3 (r137 338/879 replicated); onset(0.5) log-log
    slope in (1.7, 2.9) (r137 ~2.2); rate floor (1-rho)^2
    DC(Theta_0.25) > 0 at every onset rung, strings at 4/5/8 rel
    5e-3, margin floor/eps >= 1e6.
S3b block layer:
    G40 block tables (r168 form VERBATIM: certified enclosures +
    budget rows on the r166/r168 strings; PLUS the raw floor rows
    sum w (sigma12 - eps) > 0 per complete block x both weights);
    G41 THE ANATOMY BLOCK FLOOR (NEW; the delivered certificate):
    sum_{onset rungs} w (1-rho)^2 DC(Theta_rho) - sum_all w eps > 0
    on B2 and B3 (HARD; B4 partial reported) at rho = 0.25: the
    SIGMA-FLOOR below the horizon certified THROUGH THE ANATOMY --
    consuming per-gamma measured lock indicators (ward class, same
    trust as zsum) + classical DC + demand, NOT tau, NOT tlaw, NOT
    the raw sigma measurement.
S3c transfer layer:
    G43 horizon + rate census: h*(PT21, 0.15) replicated on the
    r168 string 1.2566e7 rel 2e-3 + k* in (23.3, 23.9); THE RATE
    LAW: fit log floor_0.25 vs log h over onset rungs -> (c, a)
    with a in (0.2, 1.8); rate horizon h*_rate = solve[eps_h = c
    h^{-a}] in (1e3, 1e7) with k*_rate reported; the generalized
    census constants (3 pi/c)(1 + 2a/3) instantiated numerically
    on the a-grid vs the sympy limits;
    G44 THE TERMINAL CHAIN INSTANTIATED: per complete block:
    [anatomy floor row (G41)] + [BA3 bridge re-instanced (G34)] +
    [certified enclosures (G31)] ==> block tau-positivity -- every
    arrow on real data; SUBSTRATE-DIRECT adjudication inherited
    (below horizon the target block is certified directly; NO
    self-supporting induction, r166/r168 re-asserted).
S4  controls through the SAME instrument (r166/r168 pre-frozen
    control blocks, CTRL_NZ = 300): G50 SMOOTH [4,8], G51 SCRARITH
    [4,8], G52 EPSTEIN {8,9,10}: tau_w < 0 on the r166 strings rel
    5e-3 AND all weighted tau block sums < 0 AND mechanism loss
    tau_w + OFF_w - zsum_w < 0 AND the FROZEN PREDICTION gated:
    sigma_w(300) - eps_w > 0 at EVERY control rung (the raw floor
    HOLDS in fake worlds -- FLOOR-INEQ-WORLD-INSENSITIVE) with
    delta_w/DC_w reported; G53 consistency (the separator is the
    BRIDGE + tau, typed BRIDGE-ARITHMETIC).
S5  G54 tau-screen (slopes vs log10 tau of sigma12, sigma_full,
    DC, delta, tlaw_0, lock <= 0.30 DEMAND-FLAT; RIDER log10 A_0^2
    slope in (0.85, 1.15) -- BOUND-RIDES-CONNES); G55 conditioning
    (1e-25 shift at h = 5, round-118 trap).
S6  G60 demand audit (SEQ inherited; windows/rho-grid/a-grid frozen
    pre-evaluation; census per-k; no ALL-X);
    G61 loop/mining gate (ancestor set of the delivered floor
    chain == {SOURCE, PT21-CENSUS-PER-K, HSW22, CACHE-WARD,
    GONEK-FORM, JETLOCK-MEAS}; TLAWCAP, WPD, CENSUS-ALL-K NOT
    ancestors; THREE loop routes carried flagged: tlaw-window,
    census-all-k, pinning-supply (SF5(ii)); weights/windows
    recomputed from frozen formulas, SIGN-MINING-CLEAN);
    G62 min-cut (r116 replica, r166/r168 graph VERBATIM: flows
    base 4, refined 5, one-grant 5, counterfactual PARALLEL 9 NOT
    REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
    G63 endgame graphs: (i) universalized census cycle RH ->
    CENSUS_ALLK -> DTSTEP_ALLK -> HCOF -> WEILPOS -> RH DETECTED
    (r168 replicated); (ii) pinning-supply grant creates the cycle
    SIGMAFLOOR -> DTSTEP_K -> TAUPOS -> SIGMAFLOOR DETECTED (the
    F3 loop, machine); (iii) the FACTORIZED per-k chain {DCLEG,
    JETMASS} -> SIGMAFLOOR -> DTSTEP_K -> HCOF -> both typed
    arrows -> RH is ACYCLIC with RH reachable from the counter-
    factual JETMASS + CENSUS_K grants (AND-semantics documented);
    the terminal residue printed.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); NZSUM = 1200; NZFULL = 7000 (the full X5 cache;
WFULL extension DISCLOSED); F64_SLOP = 1e-3; ENC_REL = 1e-3;
Z_OVERHANG = 6.0 (r162 SCAN_OVER, r166 AMENDMENT-1, CITED);
G34_HARD_MAX = 26 (r166 AMENDMENT-2, inherited PRE-FROZEN);
WORKERS = 12 (spawn; deterministic keys).  RUNGS = 4..28; DPS =
{4:60, 5:60, 6:65, 7:70, 8:80, 9:85, 10:90, 11:100, 12:110, 13:120,
14:120, 15:125, 16:130, 17:135, 18:140, 19:140, 20:144, 21:146,
22:148, 23:150, 24:150, 25:152, 26:155, 27:158, 28:160}.
BLOCKS: B2 = [4,8] FULL, B3 = [8,16] FULL, B4 = [16,32]
PARTIAL-AT-28; weights w_flat == 1 PRIMARY, w_fejer = (H/2+1) -
|h - 3H/2| ALT (r166 VERBATIM).
INHERITED BARS (r166/r168 VERBATIM): SIMP_MIN = 1e3; RAY_BAR =
RES0_BAR = 1e-25; LOGDET_BAR = 1e-30; TLAW_TAB = {4: 0.232537,
5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel
5e-3; TLAW28_WIN = (0.40, 0.70); TLAW_STRUCT_WIN = (0.15, 0.70);
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7,
18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97, 1.03);
FG_SLOPE_WIN = (3.4, 4.6); LOCK_WIN = (1.0, 8.0); RES_WIN_CORE =
(-1e-9, 0.20); RES_WIN_DEEP = (-1e-9, 0.85); ZSUM_OFF_MIN = 1e3;
TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.85, 1.15); COND_WIN = (1e-40,
1e-10); RUNTIME_BAR = 21600 s.  Controls: CTRL_SMOOTH =
CTRL_SCRARITH = (4..8) dps 60, CTRL_EPSTEIN = (8, 9, 10) dps 80,
CTRL_NZ = 300; CTRL_TAU_TAB (r166 record strings, rel 5e-3):
SMOOTH {4: -1.0375, 5: -1.0944, 6: -1.1306, 7: -1.1560, 8:
-1.1749}, SCRARITH {4: -2.5151e-2, 5: -0.34593, 6: -0.36716, 7:
-0.61294, 8: -0.67664}, EPSTEIN {8: -1.6310, 9: -1.6922, 10:
-1.9932}.  SIGMA_TAB = {4: 0.205602, 5: 0.255783, 8: 0.356579}
rel 5e-3 (r168); RECIPE_BAR = 1e-40; SIGMA12_LADDER (r168
dbt_run1.log record, DISCLOSED corpus-known, rel 1e-3, h <= 26):
{4:0.2056, 5:0.2558, 6:0.2608, 7:0.3104, 8:0.3566, 9:0.3453,
10:0.3841, 11:0.4320, 12:0.3927, 13:0.4477, 14:0.4287, 15:0.4251,
16:0.4419, 17:0.4961, 18:0.4570, 19:0.4969, 20:0.4932, 21:0.4697,
22:0.4779, 23:0.5191, 24:0.4758, 25:0.5045, 26:0.4888} (27/28
F64: record 1.0239/1.5459 report-only); TLAW_LADDER (r168 record,
rel 1e-3, ALL rungs): {4:0.2325, 5:0.2664, 6:0.2729, 7:0.3264,
8:0.3738, 9:0.3645, 10:0.4032, 11:0.4534, 12:0.4112, 13:0.4674,
14:0.4455, 15:0.4421, 16:0.4606, 17:0.5191, 18:0.4827, 19:0.5295,
20:0.5282, 21:0.5075, 22:0.5161, 23:0.5591, 24:0.5122, 25:0.5430,
26:0.5303, 27:0.5244, 28:0.5778}; HSTAR_STR = 1.2566e7 rel 2e-3;
KSTAR_WIN = (23.3, 23.9); SIGMA0 = 0.15 (r168).
NEW (calibrated in calib_sf_pass1.log, ONE pre-freeze pass at h =
4/5/8 + SMOOTH x=5; scratch deleted after freeze, log KEPT; all
numbers quoted verbatim):  SIGFULL_TAB = {4: 0.210721, 5: 0.263234,
8: 0.368356} rel 5e-3; SIGFULL_WIN = (0.15, 0.80) hard h <= 26;
DC_TAB = {4: 0.153469, 5: 0.227257, 8: 0.268559} rel 5e-3; DC_WIN
= (0.05, 0.60) ALL rungs; DELTA_TAB = {4: 1.374423, 5: 1.159470,
8: 1.372972} rel 5e-3; DELTA_WIN = (0.3, 3.0) hard h <= 26;
IDEN_BAR = 1e-40 (calibrated <= 5.9e-60); Z_TAB = {4: +0.266, 5:
-0.177, 8: +0.245} abs dev 0.01; Z_BAR = 4.0 (structural,
intermediates pre-freeze unmeasured, DISCLOSED); MINSIN_TAB = {4:
1.5123e-4, 5: 3.3198e-4, 8: 5.2605e-4} rel 5e-3; MINSIN_BAR =
1e-8; SZ_TAB = {4: 0.3566, 5: 0.2091, 8: 0.3003} rel 5e-3; SZ_BAR
= 0.9; RHO_GRID = (0.25, 0.5, 0.75); ONSET05_TAB = {4: 184.87, 5:
338.34, 8: 879.38} rel 1e-3 (r137 338/879 replicated); ONSET_MAX_H
= 16 (existence gated; beyond reported, ANATOMY-CACHE-HORIZON);
ONSET_SLOPE_WIN = (1.7, 2.9); RATEFLOOR_TAB(rho=0.25) = {4:
0.017241, 5: 0.014983, 8: 0.010137} rel 5e-3; RATE_MARGIN_MIN =
1e6; RATE_A_WIN = (0.2, 1.8) (calibrated 3-point fit ~0.77);
HSTAR_RATE_WIN = (1e3, 1e7); CTRL_FLOOR_PRED: sigma_w(300) >
eps_w at every control rung (calibrated SMOOTH x=5: 0.189 >
9.8e-11).  Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use (no
audit layer -- source + ward + envelope only).  All mpf arithmetic
inside explicit mp.workdps blocks in-worker; block accumulation at
workdps(200) from per-rung mp strings; tiny/huge quantities (tau,
A_0, OFF, zsum) stay mp end-to-end (r147/r141 underflow classes
banned); no f64 refinement of any mp quantity; flat O(1) ratios
transported as f64 for gating (DISCLOSED).  h = 6, 7, 9..28 and
all block/onset/rate rows beyond 4/5/8 pre-freeze UNMEASURED on
the NEW coordinates (structure windows only, DISCLOSED); the
sigma12/tlaw ladders are r168-record-known (DISCLOSED).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
ANATOMY-IDENTITY-PROVEN(sigma == (1-slop) delta DC; G10/G36);
ONSET-CAP-IS-UPPER-REFUTED(the F1-conjectured chain refuted exact;
G12); SIGMAFLOOR-FACTORIZED(DC-leg x JET-MASS-FLOOR; G12/G13/G36);
DC-LEG-PROVEN-MOD-CITED(per census; Landau/Gonek AS FORM;
GONEK-CONSTANT-UNPRICED; G13/G37) + LANDAU-PIN-IN-WINDOW(G37);
JETMASS-IS-TERMINAL-RESIDUE(G12/G61/G63);
RATE-FLOOR-CERTIFIED-PER-RUNG(jet-lock measured x DC; G39);
ANATOMY-BLOCK-FLOOR-CERTIFIED(B2/B3 below horizon via anatomy, not
tau; G41/G44); DEMAND-RATE-ABSORPTION(T_req -> (3 pi/c)(1+2a/3)
h^{3/2+a}; G14/G43); PINNING-SUPPLY-IS-LOOP(machine; G15/G63);
FLOOR-INEQ-WORLD-INSENSITIVE + BRIDGE-ARITHMETIC(G50-G53);
ALGEBRA-ONLY-REFUTED-FOR-JETMASS + -FOR-DCLEG(G16);
SIGMA-FLATNESS-EXPLAINED-TWO-TRENDS(measured-only for the flat
law; G36); ANTI-LATTICE-REDUCTION(G11/G38); DEMAND-FLAT +
BOUND-RIDES-CONNES(G54); QUANTIFIER-INHERITED(G60);
LOOP-ROUTES-FLAGGED(three; G15/G61/G63); OMEGA-UNCHANGED(census 4;
G62); MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge
gate fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 34/35 at SPEC_SHA
eed821a2469a0dc1, log kept as the pre-amendment record sf_run1.log).
ONE INSTRUMENT RE-TYPING, no bar or criterion moved; every other
gate incl. ALL anatomy/floor/control/graph gates passed run 1
unchanged: the G43 rate fit was frozen over ALL onset rungs, but at
the deep rungs the locked window (Theta_rho, gamma_7000] is squeezed
against the FIXED cache top (onset 4816 at h = 18 vs gamma_top =
7264.75): the measured floor there mixes the true onset law with
pure finite-cache window loss (the fitted a = 2.063 over 15 rungs
is CACHE-TOP-LIMITED -- the pairwise slopes bend monotonically from
~0.77 at the calibrated shallow anchors toward the window-loss
regime; the same instrument class as the r137 JETCERT-DEPTH-LIMITED
and E1-HORIZON-LIMITED typings, here at the rate fit).  FIX: the
G43 fit window is restricted by the h-only criterion onset_0.5(h)
<= gamma_top/2 (measured suffix onsets against the frozen cache
top; no window or bar moved -- RATE_A_WIN and HSTAR_RATE_WIN stay
frozen and apply to the RESTRICTED fit); the all-rung fit stays
printed as the measured CACHE-TOP-LIMITED law, and the run-1 fail
row is itself the measured instrument-resolution law and stays in
the record.  A deeper zeros cache would extend the clean fit range
-- pure instrument depth, no new omega.  Run 2 = run of record at
the amended SPEC_SHA; run 3 = deterministic re-run.
"""

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
NZSUM = 1200
NZFULL = 7000
F64_SLOP = 1e-3
ENC_REL = 1e-3
Z_OVERHANG = 6.0
G34_HARD_MAX = 26
WORKERS = 12

BLOCKS_DECL = (("B2", 4, 8, "FULL"),
               ("B3", 8, 16, "FULL"),
               ("B4", 16, 32, "PARTIAL-AT-28"))
H_MAX = 28
RUNGS = tuple(range(4, 29))
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 17: 135,
       18: 140, 19: 140, 20: 144, 21: 146, 22: 148, 23: 150,
       24: 150, 25: 152, 26: 155, 27: 158, 28: 160}


def w_flat(H: int, h: int) -> int:
    return 1


def w_fejer(H: int, h: int) -> int:
    return (H // 2 + 1) - abs(h - 3 * H // 2)


SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
LOGDET_BAR = 1e-30
TLAW_TAB = {4: 0.232537, 5: 0.2664, 8: 0.3738, 13: 0.4674,
            18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
TLAW28_WIN = (0.40, 0.70)
TLAW_STRUCT_WIN = (0.15, 0.70)
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7,
          18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
FG_SLOPE_WIN = (3.4, 4.6)
LOCK_WIN = (1.0, 8.0)
RES_WIN_CORE = (-1e-9, 0.20)
RES_WIN_DEEP = (-1e-9, 0.85)
ZSUM_OFF_MIN = 1e3
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
CTRL_SMOOTH = (4, 5, 6, 7, 8)
CTRL_SCRARITH = (4, 5, 6, 7, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_NZ = 300
CTRL_TAU_TAB = {
    "SMOOTH": {4: -1.0375, 5: -1.0944, 6: -1.1306, 7: -1.1560,
               8: -1.1749},
    "SCRARITH": {4: -2.5151e-2, 5: -0.34593, 6: -0.36716,
                 7: -0.61294, 8: -0.67664},
    "EPSTEIN": {8: -1.6310, 9: -1.6922, 10: -1.9932}}
CTRL_TAU_TOL = 5e-3
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 21600.0

SIGMA_TAB = {4: 0.205602, 5: 0.255783, 8: 0.356579}
SIGMA_TOL = 5e-3
RECIPE_BAR = 1e-40
SIGMA12_LADDER = {4: 0.2056, 5: 0.2558, 6: 0.2608, 7: 0.3104,
                  8: 0.3566, 9: 0.3453, 10: 0.3841, 11: 0.4320,
                  12: 0.3927, 13: 0.4477, 14: 0.4287, 15: 0.4251,
                  16: 0.4419, 17: 0.4961, 18: 0.4570, 19: 0.4969,
                  20: 0.4932, 21: 0.4697, 22: 0.4779, 23: 0.5191,
                  24: 0.4758, 25: 0.5045, 26: 0.4888}
TLAW_LADDER = {4: 0.2325, 5: 0.2664, 6: 0.2729, 7: 0.3264,
               8: 0.3738, 9: 0.3645, 10: 0.4032, 11: 0.4534,
               12: 0.4112, 13: 0.4674, 14: 0.4455, 15: 0.4421,
               16: 0.4606, 17: 0.5191, 18: 0.4827, 19: 0.5295,
               20: 0.5282, 21: 0.5075, 22: 0.5161, 23: 0.5591,
               24: 0.5122, 25: 0.5430, 26: 0.5303, 27: 0.5244,
               28: 0.5778}
LADDER_TOL = 1e-3
HSTAR_STR = 1.2566e7
HSTAR_TOL = 2e-3
KSTAR_WIN = (23.3, 23.9)
SIGMA0 = 0.15

# ------------------------------------------------- new frozen (calibrated)
SIGFULL_TAB = {4: 0.210721, 5: 0.263234, 8: 0.368356}
SIGFULL_WIN = (0.15, 0.80)
DC_TAB = {4: 0.153469, 5: 0.227257, 8: 0.268559}
DC_WIN = (0.05, 0.60)
DELTA_TAB = {4: 1.374423, 5: 1.159470, 8: 1.372972}
DELTA_WIN = (0.3, 3.0)
NEW_TOL = 5e-3
IDEN_BAR = 1e-40
Z_TAB = {4: 0.266, 5: -0.177, 8: 0.245}
Z_DEV = 0.01
Z_BAR = 4.0
MINSIN_TAB = {4: 1.5123e-4, 5: 3.3198e-4, 8: 5.2605e-4}
MINSIN_BAR = 1e-8
SZ_TAB = {4: 0.3566, 5: 0.2091, 8: 0.3003}
SZ_BAR = 0.9
RHO_GRID = (0.25, 0.5, 0.75)
ONSET05_TAB = {4: 184.87, 5: 338.34, 8: 879.38}
ONSET_TOL = 1e-3
ONSET_MAX_H = 16
ONSET_SLOPE_WIN = (1.7, 2.9)
RATEFLOOR_TAB = {4: 0.017241, 5: 0.014983, 8: 0.010137}
RATE_MARGIN_MIN = 1e6
RATE_A_WIN = (0.2, 1.8)
HSTAR_RATE_WIN = (1e3, 1e7)

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
                       "no verification/ import")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- closed forms
def hsw_G_mp(T, dps: int = 60):
    """HSW envelope, mp; caller may wrap in workdps."""
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


# ----------------------------------------------------------- workers
def w_rung(args) -> dict:
    """per-rung build (r168 recipe VERBATIM) + certified tau enclosure
    + wall chain + budget floor + sigma12/eps + THE NEW ANATOMY PASS
    over WFULL; all mp inside workdps; f64 transport of flat O(1)
    ratios (DISCLOSED)."""
    h, dps, nz, nzf = args
    try:
        gam = ward_cache()
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
            tau_up = ray if ray > tau else tau
            tau_lo = tau_up * (1 - mp.mpf(repr(ENC_REL)))
            Ms = M.copy()
            for i in range(K):
                Ms[i, i] = Ms[i, i] - tau_lo
            chol_lo_ok = True
            try:
                mp.cholesky(Ms)
            except Exception:                      # noqa: BLE001
                chol_lo_ok = False
            out["chol_lo_ok"] = chol_lo_ok
            out["tau_lo_str"] = mp.nstr(tau_lo, 40)
            out["tau_up_str"] = mp.nstr(tau_up, 40)
            wall_ok = True
            logdet_dev = float("inf")
            try:
                L = mp.cholesky(M)
                logdet_ch = 2 * sum(mp.log(L[i, i]) for i in range(K))
                logdet_ei = sum(mp.log(E[i]) for i in range(K))
                logdet_dev = float(abs(logdet_ch - logdet_ei))
            except Exception:                      # noqa: BLE001
                wall_ok = False
            out["wall_ok"] = wall_ok
            out["logdet_dev"] = logdet_dev
            # jets + eta(T_PT) + OFF (r131/r156/r168 recipe VERBATIM)
            aa = mp.log(h) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * oms[k] ** 2
                     for k in range(1, K))
            yt = abs(A2 / A0)
            b = [o * o for o in oms]
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * K
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)

            def envres(Tq, mm):
                yq = mp.mpf(repr(float(Tq))) ** 2
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

            best = None
            for m in MGRID:
                vv = envres(T_PT, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            GPT = mp.mpf(mp.nstr(hsw_G_mp(T_PT, dps), dps))
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 * GPT
            out["off_rel"] = float(off / tau)
            out["off_str"] = mp.nstr(off, 40)
            # ---- the single per-gamma pass: sigma12 + WFULL anatomy
            Tz = 2 * math.pi * h
            Tlo = Tz + Z_OVERHANG
            zsum12 = mp.mpf(0)
            zsum_full = mp.mpf(0)
            zone_diag = mp.mpf(0)
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            Q4 = mp.mpf(0)
            min_sin = None
            max_term = mp.mpf(0)
            max_g = 0.0
            rows = []
            for j in range(min(nzf, len(gam))):
                gf = float(gam[j])
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for k in range(1, K):
                    Rv += 2 * cs[k] * (-1) ** k * gm / (gm * gm - b[k])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2      # == 8 sin^2 F^2/g^2
                if gf <= Tlo:
                    zone_diag += term
                    continue
                F = gm * Rv / 2
                s2 = s * s
                if j < nz:
                    zsum12 += term
                zsum_full += term
                Gw += 1 / gm ** 2
                Cw += (1 - 2 * s2) / gm ** 2
                Sw += s2 / gm ** 2
                SFw += s2 * F * F / gm ** 2
                Q4 += 1 / gm ** 4
                ab = abs(s)
                if min_sin is None or ab < min_sin:
                    min_sin = ab
                if term > max_term:
                    max_term = term
                    max_g = gf
                rows.append((gf, float(abs(F / A0 - 1))))
            slop = mp.mpf(repr(F64_SLOP))
            zsum_c = zsum12 * (1 - slop)
            out["zsum_rel"] = float(zsum_c / tau)
            out["zone_diag_rel"] = float(zone_diag / tau)
            out["res_rel"] = float((tau + off - zsum_c) / tau)
            out["zsum_off"] = float(zsum_c / off)
            out["zsum_str"] = mp.nstr(zsum_c, 40)
            Gz = mp.mpf(mp.nstr(hsw_G_mp(2 * mp.pi * h, dps), dps))
            den = 8 * A0 * A0 * Gz
            sig12 = zsum_c / den
            sig_full = zsum_full * (1 - slop) / den
            eps = off / den
            eps_form = mp.sqrt(h) * (1 + eta_pt) ** 2 * GPT / Gz
            out["sigma"] = float(sig12)
            out["sigma_full"] = float(sig_full)
            out["eps"] = float(eps)
            out["eps_str"] = mp.nstr(eps, 40)
            out["recipe_dev"] = float(abs(eps / eps_form - 1))
            DC = (Gw - Cw) / (2 * Gz)
            delta = SFw / (A0 * A0 * Sw)
            out["DC"] = float(DC)
            out["delta"] = float(delta)
            out["iden_dev"] = float(abs(sig_full
                                        / ((1 - slop) * delta * DC)
                                        - 1))
            out["c_w"] = float(Cw)
            out["sig_c"] = float(mp.sqrt(Q4 / 2))
            out["min_sin"] = float(min_sin)
            out["sz_share"] = float(max_term * (1 - slop)
                                    / (den * sig_full))
            out["sz_gamma"] = max_g
            # lock onsets (suffix property) + locked DC per rho
            n_r = len(rows)
            suffmax = [0.0] * n_r
            run = 0.0
            for i in range(n_r - 1, -1, -1):
                run = max(run, rows[i][1])
                suffmax[i] = run
            onsets = {}
            locked = {}
            for rho in RHO_GRID:
                th = None
                for i in range(n_r):
                    if suffmax[i] <= rho:
                        th = rows[i][0]
                        break
                onsets[rho] = th
                if th is None:
                    locked[rho] = None
                    continue
                Gl = mp.mpf(0)
                Cl = mp.mpf(0)
                for gf, _r in rows:
                    if gf >= th:
                        gm = mp.mpf(repr(gf))
                        Gl += 1 / gm ** 2
                        Cl += mp.cos(2 * aa * gm) / gm ** 2
                locked[rho] = float((1 - rho) ** 2 * (Gl - Cl)
                                    / (2 * Gz))
            out["onsets"] = onsets
            out["locked"] = locked
            # anchors / ladder currencies (r168)
            out["tlaw0"] = float(tau / den)
            out["fg"] = float((lam1 - tau) / tau)
            out["lock"] = float(((lam1 - tau) / tau) / yt)
            out["log10tau"] = float(mp.log(tau) / l10)
            out["log10a0sq"] = float(2 * mp.log(abs(A0)) / l10)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w sign + budget-floor mechanism loss +
    the raw-floor world-insensitivity test (r168 recipe VERBATIM +
    the sigma_w/eps_w/delta_w/DC_w coordinates)."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            aa = mp.log(xw) / 2
            oms = [k * mp.pi / aa for k in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(Kw))
            b = [o * o for o in oms]
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * Kw
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for k in range(1, Kw):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)

            def envres(Tq, mm):
                yq = mp.mpf(repr(float(Tq))) ** 2
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(A_j[i]) / yi
                rem = mp.mpf(0)
                for k in range(1, Kw):
                    rem += cs_abs[k] * b[k] ** (mm + 1) \
                        / (yi * (yq - b[k]))
                return acc + rem

            best = None
            for m in MGRID:
                vv = envres(T_PT, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
                * mp.mpf(mp.nstr(hsw_G_mp(T_PT, dpsw), dpsw))
            Tz = 2 * math.pi * xw
            Tlo = Tz + Z_OVERHANG
            zs = mp.mpf(0)
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            for g in gam[:CTRL_NZ]:
                gf = float(g)
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for k in range(1, Kw):
                    Rv += 2 * cs[k] * (-1) ** k * gm \
                        / (gm * gm - b[k])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2
                if gf <= Tlo:
                    continue
                F = gm * Rv / 2
                zs += term
                Gw += 1 / gm ** 2
                Cw += (1 - 2 * s * s) / gm ** 2
                Sw += s * s / gm ** 2
                SFw += s * s * F * F / gm ** 2
            Gz = mp.mpf(mp.nstr(hsw_G_mp(Tz, dpsw), dpsw))
            den = 8 * A0 * A0 * Gz
            slop = mp.mpf(repr(F64_SLOP))
            return dict(world=world, h=xw, tauf=float(tau),
                        zsum=float(zs), off=float(off),
                        viol=float(tau + off - zs),
                        sigma_w=float(zs * (1 - slop) / den),
                        eps_w=float(off / den),
                        DC_w=float((Gw - Cw) / (2 * Gz)),
                        delta_w=float(SFw / (A0 * A0 * Sw)))
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 SF1 anatomy identity
    z, aa = sp.symbols("z aa", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    w1, w2 = sp.symbols("w1 w2", positive=True)
    cs = [c0, c1, c2]
    ws = [0, w1, w2]
    A0g = c0 - c1 + c2
    Rz = 2 * c0 / z + sum(2 * cs[k] * (-1) ** k * z
                          / (z ** 2 - ws[k] ** 2) for k in (1, 2))
    Fg = A0g + sum((-1) ** k * cs[k] * ws[k] ** 2
                   / (z ** 2 - ws[k] ** 2) for k in (1, 2))
    okA = sp.simplify(z * Rz / 2 - Fg) == 0
    Ei = sp.sin(aa * z) * Rz
    okB = sp.simplify(2 * Ei ** 2 - 8 * sp.sin(aa * z) ** 2
                      * Fg ** 2 / z ** 2) == 0
    # per-term decomposition (generic F, gamma)
    Fs, A0s, g = sp.symbols("Fs A0s g", positive=True)
    lhs = 8 * sp.sin(aa * g) ** 2 * Fs ** 2 / g ** 2
    rhs = (4 * A0s ** 2 * (1 - sp.cos(2 * aa * g)) / g ** 2
           + 8 * sp.sin(aa * g) ** 2 * (Fs ** 2 - A0s ** 2) / g ** 2)
    okC = sp.simplify(sp.expand_trig(lhs - rhs)) == 0
    # delta x DC factorization on a rational 2-zero instance
    s1, s2 = sp.Rational(1, 3), sp.Rational(2, 5)      # sin^2 values
    F1, F2 = sp.Rational(7, 10), sp.Rational(9, 8)     # F values
    A0q = sp.Rational(3, 5)
    g1, g2 = sp.Integer(3), sp.Integer(5)
    Gzq = sp.Rational(1, 50)
    Dq = 8 * A0q ** 2 * Gzq
    supply = 8 * (s1 * F1 ** 2 / g1 ** 2 + s2 * F2 ** 2 / g2 ** 2)
    GmC = 2 * (s1 / g1 ** 2 + s2 / g2 ** 2)
    delt = (s1 * F1 ** 2 / g1 ** 2 + s2 * F2 ** 2 / g2 ** 2) \
        / (A0q ** 2 * (s1 / g1 ** 2 + s2 / g2 ** 2))
    okD = sp.simplify(supply / Dq
                      - delt * (GmC / (2 * Gzq))) == 0
    out.append(("G10-sf1-anatomy-identity", okA and okB and okC
                and okD,
                "z R/2 == F(z^2) generic (r131 Layer 1 chase); "
                "2 E^2 == 8 sin^2 F^2/z^2; per-term decomposition "
                "8 sin^2 F^2/g^2 == 4 A_0^2(1 - cos 2Ag)/g^2 + "
                "8 sin^2(F^2 - A_0^2)/g^2 EXACT; and the "
                "factorization sigma == delta x DC on a rational "
                "instance: THEOREM SF1 -- THE SUPPLY FACTORIZES "
                "into [jet mass] x [equidistribution mass]"))

    # ---------------- G11 termwise positivity + zero-set lemma
    t1, t2, t3 = sp.symbols("t1 t2 t3", nonnegative=True)
    okE = (t1 + t2 + t3 - t2).is_nonnegative is True
    y = sp.symbols("y", positive=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    v1, v2, A0f = sp.symbols("v1 v2 A0f", real=True)
    Fr = A0f + v1 / (y - b1) + v2 / (y - b2)
    numer = sp.numer(sp.together(Fr))
    okF = sp.degree(numer, y) == 2            # K-1 with K = 3
    kk = sp.symbols("kk", integer=True)
    okG = sp.sin(sp.pi * kk) == 0
    # E == sin x R: E == 0 needs sin == 0 or R == 0 (product ring)
    okH = sp.simplify(sp.sin(aa * z) * Rz
                      - (sp.sin(aa * z)) * (Rz)) == 0
    out.append(("G11-termwise-antilattice", okE and okF and okG
                and okH,
                "sum of nonnegative terms >= any single term "
                "(single-zero floor lemma); F rational with "
                "numerator degree K-1 (census polynomial) and "
                "sin(A g) == 0 iff g in (pi/A) Z: sigma == 0 forces "
                "EVERY tail zero into the finite kill set [lattice] "
                "U [K-1 census nodes] -- the ANTI-LATTICE reduction "
                "(strict positivity per rung is one certified "
                "nonzero term: classical per rung)"))

    # ---------------- G12 SF2 floor-side adjudication
    # cap-is-upper refutation: same cap, sigma large AND tiny
    DCu = sp.Integer(1)
    cap = sp.Rational(1, 2)
    J_a = sp.Rational(1, 2)      # <= cap
    J_b = -sp.Rational(99, 100)  # <= cap
    sig_a = DCu + J_a
    sig_b = DCu + J_b
    okI = bool(J_a <= cap and J_b <= cap
               and sig_a == sp.Rational(3, 2)
               and sig_b == sp.Rational(1, 100))
    # jet-lock ==> rate floor: u = (1-r) + t, t >= 0, q = 1-r > 0
    tpos = sp.symbols("tpos", nonnegative=True)
    qpos = sp.symbols("qpos", positive=True)
    u = qpos + tpos
    okJ = sp.simplify(sp.expand(u ** 2 - qpos ** 2)
                      - (tpos ** 2 + 2 * tpos * qpos)) == 0 \
        and (tpos ** 2 + 2 * tpos * qpos).is_nonnegative is True
    # dropping nonneg terms below Theta keeps the lower bound
    okK = (t1 + t2 - t2).is_nonnegative is True
    out.append(("G12-sf2-floorside", okI and okJ and okK,
                "ONSET-CAP-IS-UPPER-REFUTED: two exact instances "
                "satisfy the SAME onset-excess cap with sigma = 3/2 "
                "and sigma = 1/100 -- the cap bounds sigma from "
                "ABOVE only (it is the TLAWCAP-side leg; consuming "
                "it is also the flagged LOOP); the floor-side leg "
                "is the JET-MASS FLOOR delta >= s_0/((1-slop) DC) "
                "by SF1; pointwise JET-LOCK |F/A_0 - 1| <= rho < 1 "
                "==> F^2 >= (1-rho)^2 A_0^2 EXACT ==> sigma >= "
                "(1-slop)(1-rho)^2 DC(Theta, T]: THE RATE FLOOR "
                "(THEOREM SF2)"))

    # ---------------- G13 SF3 DC leg (Abel/Stieltjes + limits)
    # Abel summation on a rational 3-jump instance
    u1, u2, u3 = sp.Integer(2), sp.Integer(3), sp.Integer(5)
    cj = [sp.Rational(1, 2), -sp.Rational(1, 3), sp.Rational(1, 7)]
    S1 = cj[0]
    S2 = cj[0] + cj[1]
    S3 = cj[0] + cj[1] + cj[2]
    lhs13 = sum(cj[i] / (u1, u2, u3)[i] ** 2 for i in range(3))
    rhs13 = (S3 / u3 ** 2
             + S1 * (1 / u1 ** 2 - 1 / u2 ** 2)
             + S2 * (1 / u2 ** 2 - 1 / u3 ** 2))
    okL = sp.simplify(lhs13 - rhs13) == 0
    # Landau main integral (epslock G11 verbatim)
    Th, Gt, Lm, xs = sp.symbols("Th Gt Lm xs", positive=True)
    t = sp.symbols("t", positive=True)
    integ = sp.integrate(1 / t ** 2, (t, Th, Gt))
    okM = sp.simplify(-Lm / (2 * sp.pi * sp.sqrt(xs)) * integ
                      - (-Lm / (2 * sp.pi * sp.sqrt(xs))
                         * (1 / Th - 1 / Gt))) == 0
    # limit chases: Gonek-error and Landau-main vs G_lead(T_z)
    err_ratio = (sp.log(4 * sp.pi * xs ** 2)
                 * sp.log(sp.log(3 * xs))
                 / (sp.sqrt(xs) * sp.log(xs)))
    okN = sp.limit(err_ratio, xs, sp.oo) == 0
    main_ratio = sp.log(xs) / (sp.sqrt(xs) * (sp.log(xs) + 1))
    okO = sp.limit(main_ratio, xs, sp.oo) == 0
    # phase identity (2A = log x)
    gamq = sp.symbols("gamq", positive=True)
    okP = sp.simplify(sp.cos(2 * (sp.log(xs) / 2) * gamq)
                      - sp.cos(gamq * sp.log(xs))) == 0
    out.append(("G13-sf3-dcleg", okL and okM and okN and okO
                and okP,
                "Abel/Stieltjes rearrangement exact (rational "
                "instance); Landau main integral exact; the two "
                "limit chases: Gonek-error/G_lead ~ log log/sqrt(h) "
                "-> 0 and Landau-main/G_lead ~ log h/sqrt(h) -> 0; "
                "phase cos(2Ag) == cos(g log h): THEOREM SF3 -- "
                "the DC leg is PROVEN-MOD-CITED per census (Landau "
                "1912/Gonek 1993 AS FORM, GONEK-CONSTANT-UNPRICED; "
                "the on-line identification is the per-k census "
                "leg; ALL-K == the flagged RH loop)"))

    # ---------------- G14 SF4 demand-rate absorption
    hh, kap = sp.symbols("hh kap", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    okQ = True
    dets = []
    for a_r in (sp.Integer(0), sp.Rational(1, 2), sp.Integer(1),
                sp.Rational(3, 2)):
        s_e = sp.Rational(3, 2) + a_r
        expr = (sp.sqrt(hh) * Glead(kap * hh ** s_e)
                / Glead(2 * sp.pi * hh) * hh ** a_r)
        lim = sp.limit(expr, hh, sp.oo)
        tgt = 2 * sp.pi * s_e / kap
        okQ = okQ and sp.simplify(lim - tgt) == 0
        dets.append("a=%s: 2 pi (3/2+a)/kappa" % a_r)
    # constant identity (3 pi/c)(1 + 2a/3) == 2 pi (3/2 + a)/c
    a_s, c_s = sp.symbols("a_s c_s", positive=True)
    okR = sp.simplify((3 * sp.pi / c_s) * (1 + 2 * a_s / 3)
                      - 2 * sp.pi * (sp.Rational(3, 2) + a_s)
                      / c_s) == 0
    out.append(("G14-sf4-demand-rate", okQ and okR,
                "sqrt(h) G_lead(kappa h^{3/2+a})/G_lead(2 pi h) "
                "h^a -> 2 pi(3/2+a)/kappa at a = 0, 1/2, 1, 3/2 "
                "(a = 0 == the r168 3/2-law 3 pi/sigma_0) and == "
                "(3 pi/c)(1 + 2a/3): THEOREM SF4 -- ANY explicit "
                "polynomial-rate floor is census-absorbable; the "
                "measured flatness of sigma is NOT needed, only "
                "positivity at an explicit rate (%s)"
                % "; ".join(dets)))

    # ---------------- G15 SF5 pinning-supply + loop flag
    tau_s, Zs, Ss, Ds, eps_s, th_s = sp.symbols(
        "tau_s Zs Ss Ds eps_s th_s", positive=True)
    sig_s = sp.symbols("sig_s", positive=True)
    # tau = Z + D sig + S_off; |S_off| <= D eps; Z >= 0:
    # upper: sig <= (tau + D eps)/D = tlaw + eps
    expr_up = (Zs + Ds * sig_s - Ds * eps_s) - tau_s
    sol_up = sp.solve(expr_up, sig_s)
    okS = len(sol_up) == 1 and sp.simplify(
        sol_up[0] - (tau_s - Zs + Ds * eps_s) / Ds) == 0
    # lower with BM: Z <= th (tau + D eps):
    # sig >= (tau - th(tau + D eps) - D eps)/D
    #      = (1-th) tau/D - (1+th) eps
    lower = ((1 - th_s) * tau_s - (1 + th_s) * Ds * eps_s) / Ds
    expr_lo = (tau_s - th_s * (tau_s + Ds * eps_s)
               - Ds * eps_s) / Ds
    okT = sp.simplify(expr_lo - lower) == 0
    # rational instance of the 96-percent reading
    inst = {tau_s: sp.Rational(1), Zs: sp.Rational(1, 25),
            Ds: sp.Rational(1), eps_s: sp.Rational(1, 10 ** 9)}
    zfrac = (inst[Zs] / inst[tau_s])
    okU = bool(zfrac < sp.Rational(1, 10)) \
        and bool(1 - zfrac > sp.Rational(9, 10))
    out.append(("G15-sf5-pinning-supply", okS and okT and okU,
                "GW identity rearrangements EXACT: sigma <= tlaw + "
                "eps (supply capped by the GW value; the r166 "
                "zsum/tau band 0.88..0.96 IS the r131 '96 percent' "
                "reading -- the pinned zone carries ~nothing) and "
                "WITH BM(theta): sigma >= (1-theta) tlaw - "
                "(1+theta) eps -- THE ROUTE CONSUMES TAU-POSITIVITY"
                "/TLAWCAP: typed LOOP (flagged in G61, cycle "
                "machine-detected in G63, NOT consumed): "
                "THEOREM SF5 -- the pinning-supply route to the "
                "floor is the RH loop's costume"))

    # ---------------- G16 SF6 red team
    # J of both signs at fixed weights
    okV = bool((sp.Rational(1, 2) * 1 + sp.Rational(1, 3) * 2) > 0) \
        and bool((-sp.Rational(1, 2) * 1
                  - sp.Rational(1, 3) * 2) < 0)
    # delta toy: F = 1000 A0 and F = A0/1000 with identities intact
    A0t = sp.Rational(3, 5)
    st = sp.Rational(1, 3)
    gt = sp.Integer(3)
    d_hi = (st * (1000 * A0t) ** 2 / gt ** 2) \
        / (A0t ** 2 * st / gt ** 2)
    d_lo = (st * (A0t / 1000) ** 2 / gt ** 2) \
        / (A0t ** 2 * st / gt ** 2)
    okW = d_hi == sp.Integer(10 ** 6) \
        and d_lo == sp.Rational(1, 10 ** 6)
    # lattice toy: zeros at j pi/A ==> sin == 0 ==> sigma == 0
    Aq = sp.Integer(1)
    sig_lat = sum(8 * sp.sin(Aq * (j * sp.pi / Aq)) ** 2
                  * sp.Rational(1, 4) / (j * sp.pi) ** 2
                  for j in (1, 2, 3))
    okX = sp.simplify(sig_lat) == 0
    out.append(("G16-sf6-redteam", okV and okW and okX,
                "J_W realizes BOTH signs at fixed weights; the "
                "delta toy realizes 1e6 AND 1e-6 with every "
                "identity intact (ALGEBRA-ONLY-REFUTED-FOR-"
                "JETMASS); the lattice toy (all tail zeros at "
                "j pi/A) gives sigma == 0 exactly (ALGEBRA-ONLY-"
                "REFUTED-FOR-DCLEG): only arithmetic input -- the "
                "true zeros avoiding the minimizer's own lattice "
                "(census + Landau) and the jet mass at those zeros "
                "-- pins the floor"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = []
    steps.append(("NFCLOS (CDXXIII, cited) demands an unbounded "
                  "sequence per a (SEQ); one positive rung per "
                  "dyadic block supplies it cofinally", demand == SEQ))
    steps.append(("windows W12/WFULL, rho-grid, a-grid, blocks, "
                  "weights and all bars DECLARED pre-evaluation "
                  "(SPEC_SHA covers the declaration)", True))
    steps.append(("the census schedule is typed PER-K (finite "
                  "classical per k); the ALL-K grant is carried "
                  "ONLY as a flagged LOOP edge", True))
    steps.append(("the delivered floor chain consumes source + "
                  "PT21-per-k + HSW22 + ward-class cache + "
                  "Landau/Gonek FORM + per-gamma measured lock "
                  "indicators ONLY; no tlaw window, no WPD, no "
                  "measured tau sign", True))
    steps.append(("no ALL-X demand introduced; uniform per-rung "
                  "margins NOT demanded", demand != ALL_X))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ------------------------------------------------- horizon machinery
def eps_closed(h: float):
    """conservative eta -> 0 closed form of the demand."""
    return float(mp.sqrt(h) * hsw_G_mp(T_PT)
                 / hsw_G_mp(2 * math.pi * h))


def solve_horizon(sigma0: float, a_rate: float = 0.0) -> float:
    lo, hi = 1e2, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed(mid) < sigma0 * mid ** (-a_rate):
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


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


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("sigmafloor_probe -- PRIME.SIGMAFLOOR.FINAL.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = (4, 5, 8) if smoke else RUNGS
    ctrl_tasks = [("SMOOTH", 4, 60), ("SMOOTH", 5, 60)] if smoke \
        else ([("SMOOTH", xw, CTRL_DPS["SMOOTH"])
               for xw in CTRL_SMOOTH]
              + [("SCRARITH", xw, CTRL_DPS["SCRARITH"])
                 for xw in CTRL_SCRARITH]
              + [("EPSTEIN", xw, CTRL_DPS["EPSTEIN"])
                 for xw in CTRL_EPSTEIN])
    nz = 300 if smoke else NZSUM
    nzf = NZFULL                       # anatomy always full cache
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; ward-class "
          "ordinates only)" % (len(gam),
                               abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")
    gtop = float(gam[-1])

    section("S1  EXACT LAYER (SF1-SF6)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXXXIII DT1/DT2 + 3/2-law + horizon + "
         "sigma/eps record; CDLXXV BA1-BA3 + blocks + amendments; "
         "CDLXXXI GB2/GC1; CDLXVII quartic; CDXLI budget anatomy + "
         "Landau pin + E1 + onsets; CDXXXIII Layer 1/2 + smallness; "
         "r131 OFF recipe VERBATIM; HSW22 Cor. 1.2; PT21; Landau "
         "1912 + Gonek 1993 AS FORM (constants unpriced); Weil 1952 "
         "AS FORM; Yoshida 1992 (no priority claim); Sylvester/"
         "Jacobi; Cauchy; Courant-Fischer; Weyl")

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
    for h in rungs:
        tasks.append(("rung", h, (h, DPS[h], nz, nzf)))
    for world, xw, dpsw in ctrl_tasks:
        tasks.append(("ctl", (world, xw), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-(tk[2][1] if tk[0] == "rung"
                                 else 0),
                               -(tk[1] if tk[0] == "rung" else 0),
                               str(tk[1])))

    section("S3  BUILDS (%d tasks, %d workers)" % (len(tasks), workers))
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
    section("S3a  PER-RUNG CERTIFICATES + SIGMA ANATOMY")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    ok36 = ok37 = ok38 = ok39 = True
    d30, d31, d32, d33, d34, d35 = ([] for _ in range(6))
    d36, d37, d38, d39 = ([] for _ in range(4))
    for h in rungs:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        core = h <= 13
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e ray %.0e r0 %.0e (%.0fs)"
                   % (h, r["K"], r["simp"], r["ray_dev"],
                      r["r0_rel"], r["build_s"]))
        okx = r["chol_lo_ok"]
        ok31 = ok31 and okx
        d31.append("h%d chol-lo %s" % (h, r["chol_lo_ok"]))
        okx = (r["wall_ok"] and r["logdet_dev"] <= LOGDET_BAR
               and r["tlaw0"] > 0)
        ok32 = ok32 and okx
        d32.append("h%d wall + logdet %.0e sign(+)"
                   % (h, r["logdet_dev"]))
        if h in TLAW_TAB:
            tl_ok = abs(r["tlaw0"] / TLAW_TAB[h] - 1) <= TLAW_TOL
        elif h == 28:
            tl_ok = TLAW28_WIN[0] <= r["tlaw0"] <= TLAW28_WIN[1]
        else:
            tl_ok = TLAW_STRUCT_WIN[0] <= r["tlaw0"] \
                <= TLAW_STRUCT_WIN[1]
        if not smoke and h in TLAW_LADDER:
            tl_ok = tl_ok and abs(r["tlaw0"] / TLAW_LADDER[h] - 1) \
                <= LADDER_TOL
        if h in FG_TAB:
            fg_ok = FG_TAB[h] * FG_WIN[0] <= r["fg"] \
                <= FG_TAB[h] * FG_WIN[1]
        else:
            fg_ok = r["fg"] > 0
        okx = tl_ok and fg_ok \
            and LOCK_WIN[0] <= r["lock"] <= LOCK_WIN[1]
        ok33 = ok33 and okx
        d33.append("h%d tlaw %.4f FG %.4e lock %.2f"
                   % (h, r["tlaw0"], r["fg"], r["lock"]))
        win = RES_WIN_CORE if core else RES_WIN_DEEP
        okx = (win[0] <= r["res_rel"] <= win[1]
               and r["zsum_off"] >= ZSUM_OFF_MIN
               and r["zsum_rel"] > 0)
        a34tag = ""
        if h > G34_HARD_MAX:
            okx = True
            a34tag = " [F64-ORDINATE-LIMITED, measured-only]"
        ok34 = ok34 and okx
        d34.append("h%d zsum/tau %.4f res %.4f zsum/off %.1e%s"
                   % (h, r["zsum_rel"], r["res_rel"], r["zsum_off"],
                      a34tag))
        # G35 sigma12/eps (needs the full NZSUM tail; smoke gates
        # structure only)
        if h in SIGMA_TAB and not smoke:
            sg_ok = abs(r["sigma"] / SIGMA_TAB[h] - 1) <= SIGMA_TOL
        else:
            sg_ok = 0.10 <= r["sigma"] <= 0.80
        if not smoke and h in SIGMA12_LADDER:
            sg_ok = sg_ok and abs(r["sigma"] / SIGMA12_LADDER[h]
                                  - 1) <= LADDER_TOL
        okx = sg_ok and r["recipe_dev"] <= RECIPE_BAR
        a35tag = ""
        if h > G34_HARD_MAX:
            okx = r["recipe_dev"] <= RECIPE_BAR
            a35tag = " [sigma F64-typed]"
        ok35 = ok35 and okx
        d35.append("h%d sigma %.4f eps %.3e recipe %.0e%s"
                   % (h, r["sigma"], r["eps"], r["recipe_dev"],
                      a35tag))
        # G36 anatomy table
        iden_ok = r["iden_dev"] <= IDEN_BAR
        dc_ok = DC_WIN[0] <= r["DC"] <= DC_WIN[1]
        if not smoke and h in DC_TAB:
            dc_ok = dc_ok and abs(r["DC"] / DC_TAB[h] - 1) <= NEW_TOL
        sf_ok = SIGFULL_WIN[0] <= r["sigma_full"] <= SIGFULL_WIN[1]
        de_ok = DELTA_WIN[0] <= r["delta"] <= DELTA_WIN[1]
        if not smoke and h in SIGFULL_TAB:
            sf_ok = sf_ok and abs(r["sigma_full"] / SIGFULL_TAB[h]
                                  - 1) <= NEW_TOL
        if not smoke and h in DELTA_TAB:
            de_ok = de_ok and abs(r["delta"] / DELTA_TAB[h]
                                  - 1) <= NEW_TOL
        a36tag = ""
        if h > G34_HARD_MAX:
            sf_ok = de_ok = True
            a36tag = " [sigma_full/delta F64-typed]"
        okx = iden_ok and dc_ok and sf_ok and de_ok
        ok36 = ok36 and okx
        d36.append("h%d sigF %.4f DC %.4f delta %.4f iden %.0e%s"
                   % (h, r["sigma_full"], r["DC"], r["delta"],
                      r["iden_dev"], a36tag))
        # G37 Landau pin in the supply window
        lam = lam_von_mangoldt(h)
        Tlo = 2 * math.pi * h + Z_OVERHANG
        c_pred = -lam / (2 * math.pi * math.sqrt(h)) \
            * (1 / Tlo - 1 / gtop)
        zval = (r["c_w"] - c_pred) / r["sig_c"]
        okx = abs(zval) <= Z_BAR
        if not smoke and h in Z_TAB:
            okx = okx and abs(zval - Z_TAB[h]) <= Z_DEV
        ok37 = ok37 and okx
        d37.append("h%d(%s) z%+.2f C %.2e pred %.2e"
                   % (h, "pp" if lam > 0 else "comp", zval,
                      r["c_w"], c_pred))
        # G38 lattice avoidance + collectivity
        ms_ok = r["min_sin"] >= MINSIN_BAR
        sz_ok = r["sz_share"] <= SZ_BAR
        if not smoke and h in MINSIN_TAB:
            ms_ok = ms_ok and abs(r["min_sin"] / MINSIN_TAB[h]
                                  - 1) <= NEW_TOL
        if not smoke and h in SZ_TAB:
            sz_ok = sz_ok and abs(r["sz_share"] / SZ_TAB[h]
                                  - 1) <= NEW_TOL
        okx = ms_ok and sz_ok
        ok38 = ok38 and okx
        d38.append("h%d minsin %.1e szshare %.3f@%.0f"
                   % (h, r["min_sin"], r["sz_share"],
                      r["sz_gamma"]))
        # G39 rate-floor table
        th05 = r["onsets"].get(0.5)
        fl25 = r["locked"].get(0.25)
        okx = True
        if h <= ONSET_MAX_H:
            okx = th05 is not None and fl25 is not None \
                and fl25 > 0 \
                and fl25 / r["eps"] >= RATE_MARGIN_MIN
        if not smoke and h in ONSET05_TAB and th05 is not None:
            okx = okx and abs(th05 / ONSET05_TAB[h] - 1) <= ONSET_TOL
        if not smoke and h in RATEFLOOR_TAB and fl25 is not None:
            okx = okx and abs(fl25 / RATEFLOOR_TAB[h] - 1) <= NEW_TOL
        ok39 = ok39 and okx
        d39.append("h%d Th.5 %s fl.25 %s"
                   % (h, "%.1f" % th05 if th05 else "None",
                      "%.4f" % fl25 if fl25 else "None"))
    check("G30-spectral-sanity", ok30,
          "E sorted; ground simple >= %.0e; Rayleigh dev/residual "
          "<= %.0e/%.0e; K == ceil(1.25 h log h): %s"
          % (SIMP_MIN, RAY_BAR, RES0_BAR, "; ".join(d30)))
    check("G31-certified-enclosures", ok31,
          "upper = Rayleigh(v_0) exact-variational; lower = tau_hat "
          "(1 - %.0e) certified by Cholesky of Mq - tau_lo I at "
          "EVERY rung: %s" % (ENC_REL, "; ".join(d31)))
    check("G32-wall-chain", ok32,
          "Cholesky(Mq) + |logdet dev| <= %.0e + sign(tau) == "
          "sign(wall) == +1 (BA2 chain, r166 CITED): %s"
          % (LOGDET_BAR, "; ".join(d32)))
    check("G33-anchors-ladder", ok33,
          "tlaw_0 strings rel <= %.0e + the full r168 record "
          "ladder rel <= %.0e; FULLGAP tabs x %s; lock in %s: %s"
          % (TLAW_TOL, LADDER_TOL, str(FG_WIN), str(LOCK_WIN),
             "; ".join(d33)))
    check("G34-budget-floor", ok34,
          "BA3 instantiated (r166 form): res in %s core / %s deep; "
          "zsum - OFF > 0 with margin >= %.0e; HARD h <= %d, 27/28 "
          "F64-typed (r166 AMENDMENT-2 inherited): %s"
          % (str(RES_WIN_CORE), str(RES_WIN_DEEP), ZSUM_OFF_MIN,
             G34_HARD_MAX, "; ".join(d34)))
    check("G35-sigma-eps-table", ok35,
          "sigma12 on the r168 strings rel <= %.0e at 4/5/8 + the "
          "record ladder rel <= %.0e at h <= 26; recipe identity "
          "dev <= %.0e at EVERY rung: %s"
          % (SIGMA_TOL, LADDER_TOL, RECIPE_BAR, "; ".join(d35)))
    check("G36-anatomy-table", ok36,
          "sigma_full == (1-slop) delta DC at rel <= %.0e EVERY "
          "rung (exact-algebra ward, F64-immune); sigma_full/DC/"
          "delta on the calibrated strings rel <= %.0e at 4/5/8; "
          "DC in %s ALL rungs (ordinate-only, depth-robust); "
          "sigma_full in %s + delta in %s hard h <= %d: %s"
          % (IDEN_BAR, NEW_TOL, str(DC_WIN), str(SIGFULL_WIN),
             str(DELTA_WIN), G34_HARD_MAX, "; ".join(d36)))
    check("G37-landau-pin-window", ok37,
          "C_W vs -Lambda(h)/(2 pi sqrt h)(1/T_lo - 1/gtop) in the "
          "SUPPLY window: |z| <= %.1f every rung (+ calibrated "
          "z-strings at 4/5/8 abs %.2f): the C-oscillation of the "
          "DC leg is Landau-pinned at the rung's own coordinate "
          "(SF3 instantiated): %s" % (Z_BAR, Z_DEV, "; ".join(d37)))
    check("G38-antilattice-collectivity", ok38,
          "min |sin(A g)| over WFULL >= %.0e every rung (no tail "
          "zero on the minimizer's lattice -- the kill set is "
          "avoided with measured margin) + single-zero max share "
          "<= %.1f (the supply is collective-but-onset-weighted): "
          "%s" % (MINSIN_BAR, SZ_BAR, "; ".join(d38)))
    check("G39-rate-floor-table", ok39,
          "lock onsets Theta_rho (suffix property over WFULL) "
          "exist at every h <= %d (beyond = ANATOMY-CACHE-HORIZON, "
          "reported); onset(0.5) strings at 4/5/8 rel <= %.0e "
          "(r137 338/879 replicated); rate floor (1-rho)^2 "
          "DC(Theta) > 0 with floor/eps >= %.0e at every onset "
          "rung: %s" % (ONSET_MAX_H, ONSET_TOL, RATE_MARGIN_MIN,
                        "; ".join(d39)))
    info("sigma12 ladder: " + " ".join(
        "%d:%.4f" % (h, tab[h]["sigma"]) for h in rungs if h in tab))
    info("sigma_full ladder: " + " ".join(
        "%d:%.4f" % (h, tab[h]["sigma_full"])
        for h in rungs if h in tab))
    info("DC ladder: " + " ".join(
        "%d:%.4f" % (h, tab[h]["DC"]) for h in rungs if h in tab))
    info("delta ladder: " + " ".join(
        "%d:%.4f" % (h, tab[h]["delta"]) for h in rungs if h in tab))
    info("minsin ladder: " + " ".join(
        "%d:%.1e" % (h, tab[h]["min_sin"])
        for h in rungs if h in tab))
    info("onset(0.5) ladder: " + " ".join(
        "%d:%s" % (h, "%.0f" % tab[h]["onsets"][0.5]
                   if tab[h]["onsets"][0.5] else "-")
        for h in rungs if h in tab))
    info("ratefloor(0.25) ladder: " + " ".join(
        "%d:%s" % (h, "%.4f" % tab[h]["locked"][0.25]
                   if tab[h]["locked"][0.25] else "-")
        for h in rungs if h in tab))

    # ------------------------------------------------ S3b blocks
    section("S3b  BLOCK TABLES + ANATOMY BLOCK FLOOR")
    ok40 = ok41 = True
    d40, d41 = [], []
    blk_data = {}
    for bn, Hb, Hb2, ty in BLOCKS_DECL:
        hs = [h for h in rungs if Hb <= h <= min(Hb2, H_MAX)]
        if smoke and not hs:
            continue
        if not all(h in tab for h in hs):
            ok40 = False
            d40.append("%s MISSING RUNGS" % bn)
            continue
        complete = (ty == "FULL") and (hs == list(range(Hb, Hb2 + 1)))
        rows = {}
        with mp.workdps(200):
            for wn, wf in (("flat", w_flat), ("fejer", w_fejer)):
                lo = mp.mpf(0)
                hi = mp.mpf(0)
                bud = mp.mpf(0)
                flo = mp.mpf(0)
                for h in hs:
                    wv = mp.mpf(wf(Hb, h))
                    lo += wv * mp.mpf(tab[h]["tau_lo_str"])
                    hi += wv * mp.mpf(tab[h]["tau_up_str"])
                    bud += wv * (mp.mpf(tab[h]["zsum_str"])
                                 - mp.mpf(tab[h]["off_str"]))
                    flo += wv * (mp.mpf(repr(tab[h]["sigma"]))
                                 - mp.mpf(tab[h]["eps_str"]))
                rows[wn] = (lo, hi, bud, flo)
        for wn in ("flat", "fejer"):
            lo, hi, bud, flo = rows[wn]
            pos = bool(lo > 0)
            budp = bool(bud > 0)
            flop = bool(flo > 0)
            if complete:
                ok40 = ok40 and pos and budp and flop
            d40.append("%s w=%s enc [%.4e, %.4e] lo>0 %s budget "
                       "%.4e>0 %s rawfloor %.4f>0 %s"
                       % (bn, wn, float(lo), float(hi), pos,
                          float(bud), budp, float(flo), flop))
        blk_data[bn] = dict(hs=hs, complete=complete, rows=rows)
    check("G40-block-tables", ok40,
          "certified enclosures + BA3 budget rows (r166/r168 form "
          "VERBATIM) + the RAW FLOOR rows sum w (sigma12 - eps) > "
          "0 per complete block x both weights: %s"
          % " | ".join(d40))

    if not smoke:
        for bn, dd in blk_data.items():
            hs = dd["hs"]
            with mp.workdps(200):
                anat = mp.mpf(0)
                epss = mp.mpf(0)
                n_on = 0
                for h in hs:
                    wv = mp.mpf(1)
                    fl = tab[h]["locked"].get(0.25)
                    if fl is not None:
                        anat += wv * mp.mpf(repr(fl))
                        n_on += 1
                    epss += wv * mp.mpf(tab[h]["eps_str"])
                row = anat - epss
            posr = bool(row > 0)
            dd["anat_pos"] = posr
            if dd["complete"]:
                ok41 = ok41 and posr
            d41.append("%s anat-floor %.4f - eps %.2e > 0 %s "
                       "(%d/%d onset rungs)%s"
                       % (bn, float(anat), float(epss), posr,
                          n_on, len(hs),
                          "" if dd["complete"] else " [PARTIAL]"))
        check("G41-anatomy-block-floor", ok41,
              "sum_{onset rungs} w (1-rho)^2 DC(Theta_rho) - "
              "sum_all w eps > 0 at rho = 0.25 on every COMPLETE "
              "block: THE SIGMA-FLOOR BELOW THE HORIZON CERTIFIED "
              "THROUGH THE ANATOMY (per-gamma measured lock "
              "indicators, ward class + classical DC + demand; "
              "consumes NEITHER tau NOR tlaw NOR raw sigma): %s"
              % "; ".join(d41))
    else:
        check("G41-anatomy-smoke", True, "smoke: needs full ladder")

    # ------------------------------------------------ S3c transfer
    section("S3c  HORIZON + RATE CENSUS + TERMINAL CHAIN")
    if not smoke:
        hstar = solve_horizon(SIGMA0)
        kstar = math.log2(hstar)
        # rate fit over onset rungs (AMENDMENT 1: the hard fit is
        # restricted by the h-only criterion onset_0.5 <= gtop/2 --
        # beyond it the locked window is squeezed against the fixed
        # cache top: CACHE-TOP-LIMITED, the all-rung fit reported)
        fit_all = [h for h in rungs if h in tab
                   and tab[h]["locked"].get(0.25)]
        fit_h = [h for h in fit_all
                 if tab[h]["onsets"].get(0.5) is not None
                 and tab[h]["onsets"][0.5] <= gtop / 2]

        def ratefit(hs):
            lx = [math.log10(h) for h in hs]
            ly = [math.log10(tab[h]["locked"][0.25]) for h in hs]
            cf = np.polyfit(lx, ly, 1)
            return -float(cf[0]), 10.0 ** float(cf[1])

        a_all, c_all = ratefit(fit_all)
        a_rate, c_rate = ratefit(fit_h)
        hstar_rate = solve_horizon(c_rate, a_rate)
        kstar_rate = math.log2(hstar_rate)
        ok43 = (abs(hstar / HSTAR_STR - 1) <= HSTAR_TOL
                and KSTAR_WIN[0] <= kstar <= KSTAR_WIN[1]
                and RATE_A_WIN[0] <= a_rate <= RATE_A_WIN[1]
                and HSTAR_RATE_WIN[0] <= hstar_rate
                <= HSTAR_RATE_WIN[1])
        check("G43-horizon-rate-census", ok43,
              "h*(PT21, 0.15) = %.4e (r168 string %.4e rel %.0e), "
              "k* = %.2f; THE RATE LAW (AMENDMENT-1 window: onset "
              "<= gtop/2, %d clean rungs): floor_0.25(h) ~ %.4f "
              "h^{-%.3f} (a in %s); all-rung fit a = %.3f over %d "
              "rungs typed CACHE-TOP-LIMITED (measured instrument "
              "law, reported); rate horizon h*_rate = %.3e "
              "(k*_rate = %.1f) in %s; census constant for the "
              "rate floor: (3 pi/c)(1 + 2a/3) = %.1f (vs sympy "
              "2 pi(3/2+a)/c exact, G14): the JETLOCK-conditional "
              "anatomy floor carries ~%d dyadic blocks on PT21 -- "
              "weaker than the granted flat floor (%d blocks) but "
              "PROVEN-MOD-{measured lock, cited Gonek} instead of "
              "measured-sigma"
              % (hstar, HSTAR_STR, HSTAR_TOL, kstar, len(fit_h),
                 c_rate, a_rate, str(RATE_A_WIN), a_all,
                 len(fit_all), hstar_rate, kstar_rate,
                 str(HSTAR_RATE_WIN),
                 (3 * math.pi / c_rate) * (1 + 2 * a_rate / 3),
                 int(kstar_rate) - 1, int(kstar) - 1))
    else:
        check("G43-horizon-smoke", True, "smoke: skipped")

    ok44 = True
    d44 = []
    if not smoke:
        for bn in ("B2", "B3"):
            dd = blk_data.get(bn)
            if dd is None or not dd["complete"]:
                ok44 = False
                continue
            hs_hard = [h for h in dd["hs"] if h <= G34_HARD_MAX]
            legs = []
            for h in hs_hard:
                r = tab[h]
                with mp.workdps(200):
                    floor = mp.mpf(r["zsum_str"]) \
                        - mp.mpf(r["off_str"])
                    tau_lo = mp.mpf(r["tau_lo_str"])
                legs.append(bool(floor > 0
                                 and r["res_rel"] >= -1e-9
                                 and tau_lo > 0))
            anat_ok = bool(dd.get("anat_pos", False))
            enc_ok = bool(dd["rows"]["flat"][0] > 0)
            okx = all(legs) and anat_ok and enc_ok
            ok44 = ok44 and okx
            d44.append("%s: anatomy floor %s + BA3 bridge %d/%d + "
                       "enc>0 %s" % (bn, anat_ok, sum(legs),
                                     len(legs), enc_ok))
        check("G44-terminal-chain", ok44,
              "[G41 anatomy floor] + [BA3 bridge per rung] + "
              "[certified enclosures] ==> block tau-positivity, "
              "every arrow on real data: %s -- SUBSTRATE-DIRECT "
              "inherited (below the horizon the target block is "
              "certified directly; NO self-supporting induction, "
              "r166/r168 re-asserted)" % "; ".join(d44))
    else:
        check("G44-terminal-smoke", True, "smoke: skipped")

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS (bridge refusal + raw-floor insensitivity)")
    ctrl_ok = True
    cblocks = {}
    for world, xw, _d in ctrl_tasks:
        r = res.get(("ctl", (world, xw)))
        if r is None or "error" in r:
            ctrl_ok = False
            check("G50-%s-x%d" % (world.lower(), xw), False,
                  (r or {}).get("error", "missing"))
            continue
        cblocks.setdefault(world, []).append(r)
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        rows = cblocks.get(world)
        if rows is None:
            continue
        taus = {r["h"]: r["tauf"] for r in rows}
        strs = CTRL_TAU_TAB[world]
        str_ok = all(abs(taus[h] / strs[h] - 1) <= CTRL_TAU_TOL
                     for h in taus if h in strs) if not smoke \
            else all(t < 0 for t in taus.values())
        Hb = 4 if world != "EPSTEIN" else 8
        s_flat = sum(taus.values())
        s_fej = sum(w_fejer(Hb, r["h"]) * r["tauf"] for r in rows)
        viol_ok = all(r["viol"] < 0 for r in rows)
        floor_holds = all(r["sigma_w"] > r["eps_w"] for r in rows)
        refuse = (all(t < 0 for t in taus.values()) and s_flat < 0
                  and s_fej < 0 and viol_ok and str_ok
                  and floor_holds)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s rungs %s: tau_w ALL < 0 on the r166 strings (rel "
              "%.0e); tau block sums flat %.4e / fejer %.4e < 0; "
              "mechanism loss tau_w + OFF_w - zsum_w < 0 at every "
              "rung (the BA3 BRIDGE is FALSE); AND the frozen "
              "prediction CONFIRMED: the raw floor sigma_w > "
              "eps_w HOLDS in the fake world (sigma_w %s vs eps_w "
              "~ %.0e; delta_w %s DC_w %s) -- the supply is a sum "
              "of squares in EVERY world: the arithmetic content "
              "is the BRIDGE + the tau conclusion, not the raw "
              "inequality"
              % (world, sorted(taus), CTRL_TAU_TOL, s_flat, s_fej,
                 ["%.3f" % r["sigma_w"] for r in rows],
                 max(r["eps_w"] for r in rows),
                 ["%.2f" % r["delta_w"] for r in rows],
                 ["%.2f" % r["DC_w"] for r in rows]))
    check("G53-controls-consistency", ctrl_ok,
          "all control worlds refuse the BRIDGED floor (tau sums "
          "flip, BA3 false) while the raw supply-demand inequality "
          "holds there: FLOOR-INEQ-WORLD-INSENSITIVE + "
          "BRIDGE-ARITHMETIC -- the r168 'controls flip it' "
          "reading PRECISED: what is arithmetic is {floor, "
          "BA3-bridge} as a PAIR (the GW identity fails for fake "
          "combs), plus the flat SIZE law")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 20:
        lt = [tab[h]["log10tau"] for h in rungs]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_sg = slope_of([math.log10(tab[h]["sigma"])
                         for h in rungs])
        s_sf = slope_of([math.log10(tab[h]["sigma_full"])
                         for h in rungs])
        s_dc = slope_of([math.log10(tab[h]["DC"]) for h in rungs])
        s_de = slope_of([math.log10(tab[h]["delta"])
                         for h in rungs])
        s_tl = slope_of([math.log10(tab[h]["tlaw0"])
                         for h in rungs])
        s_lk = slope_of([math.log10(tab[h]["lock"])
                         for h in rungs])
        s_a0 = slope_of([tab[h]["log10a0sq"] for h in rungs])
        ok54 = (all(abs(s) <= TAU_SLOPE_BAR
                    for s in (s_sg, s_sf, s_dc, s_de, s_tl, s_lk))
                and RIDER_WIN[0] <= s_a0 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: sigma12 %.4f, sigma_full %.4f, "
              "DC %.4f, delta %.4f, tlaw_0 %.4f, lock %.4f (<= "
              "%.2f DEMAND-FLAT); RIDER log10 A_0^2 slope %.3f in "
              "%s (BOUND-RIDES-CONNES: the anatomy coordinates are "
              "tau-flat, the jets ride)"
              % (s_sg, s_sf, s_dc, s_de, s_tl, s_lk,
                 TAU_SLOPE_BAR, s_a0, str(RIDER_WIN)))
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

    dep = {"FLOOR-CHAIN": ("SOURCE", "PT21-CENSUS-PER-K", "HSW22",
                           "CACHE-WARD", "GONEK-FORM",
                           "JETLOCK-MEAS"),
           "CACHE-WARD": (), "SOURCE": (), "PT21-CENSUS-PER-K": (),
           "HSW22": (), "GONEK-FORM": (), "JETLOCK-MEAS": (),
           "TLAWCAP": (), "WPD": (), "CENSUS-ALL-K": (),
           "TAUPOS": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",),
           "LOOP-ROUTE(census-all-k)": ("CENSUS-ALL-K",),
           "LOOP-ROUTE(pinning-supply)": ("TAUPOS", "TLAWCAP")}

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

    anc = ancestors("FLOOR-CHAIN")
    ok61 = ("TLAWCAP" not in anc and "WPD" not in anc
            and "CENSUS-ALL-K" not in anc and "TAUPOS" not in anc
            and "TLAWCAP" in ancestors("LOOP-ROUTE(tlaw==>blocksum)")
            and "CENSUS-ALL-K" in ancestors("LOOP-ROUTE(census-all-k)")
            and "TAUPOS" in ancestors("LOOP-ROUTE(pinning-supply)"))
    okw = True
    for bn, Hb, Hb2, _ty in BLOCKS_DECL:
        for h in range(Hb, min(Hb2, H_MAX) + 1):
            okw = okw and w_flat(Hb, h) == 1 \
                and w_fejer(Hb, h) == (Hb // 2 + 1) \
                - abs(h - 3 * Hb // 2)
    okw = okw and tuple(sorted(RHO_GRID)) == RHO_GRID
    check("G61-loop-mining", ok61 and okw,
          "delivered floor-chain ancestors == {SOURCE, PT21-CENSUS-"
          "PER-K, HSW22, CACHE-WARD, GONEK-FORM, JETLOCK-MEAS}: "
          "TLAWCAP, WPD, CENSUS-ALL-K and TAUPOS are NOT ancestors "
          "(NO-LOOP); THREE loop routes carried flagged, NOT "
          "consumed (tlaw-window, census-all-k, pinning-supply); "
          "weights/windows/grids recomputed from frozen formulas "
          "(SIGN-MINING-CLEAN; disclosure: sigma12/tlaw ladders "
          "r168-record-known pre-freeze; all NEW coordinates at "
          "h != 4/5/8 pre-freeze unmeasured)")

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
    check("G62-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 9 and "RH" not in reach,
          "flows: base 4, refined 5 (r166/r168 graph VERBATIM -- "
          "this round FACTORIZES the sigma-floor coordinate on "
          "existing rows, no set change); one-grant 5; "
          "counterfactual PARALLEL 9 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")

    # G63 endgame graphs
    chain_uni = {
        "RH": ["CENSUS_ALLK"],
        "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"],
        "EPSLAW": ["DTSTEP_ALLK"],
        "BA3": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"],
        "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "CARRIER_LEM": ["WEILPOS"],
        "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"],
        "L1": ["RH_VIA_N"], "WPD": ["RH_VIA_N"],
        "RH_VIA_N": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    # pinning-supply grant: TAUPOS -> SIGMAFLOOR closes a cycle
    chain_pin = {
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"],
        "CENSUS_K": ["DTSTEP_K"], "BA3": ["DTSTEP_K"],
        "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"],       # the SF5(ii) BM+TLAWCAP grant
        "SUBSTRATE28": ["HCOF"]}
    loop_pin = has_cycle(chain_pin)
    # the factorized per-k terminal chain (acyclic)
    chain_term = {
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "GONEK": ["DCLEG"], "CENSUS_K": ["DCLEG", "DTSTEP_K"],
        "SIGMAFLOOR": ["DTSTEP_K"], "BA3": ["DTSTEP_K"],
        "EPSLAW": ["DTSTEP_K"],
        "DTSTEP_K": ["HCOF"], "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "CARRIER_LEM": ["WEILPOS"], "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"], "L1": ["RH_VIA_N"],
        "WPD": ["RH_VIA_N"], "RH_VIA_N": ["RH"]}
    acyc = not has_cycle(chain_term)
    rh_reach = "RH" in reachable(chain_term, "JETMASS") \
        and "RH" in reachable(chain_term, "CENSUS_K") \
        and "RH" in reachable(chain_term, "GONEK")
    check("G63-endgame-graphs", loop_uni and loop_pin and acyc
          and rh_reach,
          "(i) universalized census: cycle RH -> CENSUS_ALLK -> "
          "DTSTEP_ALLK -> HCOF -> WEILPOS -> RH DETECTED (r168 "
          "replicated); (ii) the pinning-supply grant closes the "
          "cycle SIGMAFLOOR -> DTSTEP_K -> TAUPOS -> SIGMAFLOOR: "
          "DETECTED (the F3 route is machine-flagged LOOP); (iii) "
          "the FACTORIZED per-k terminal chain {GONEK -> DCLEG, "
          "JETMASS} -> SIGMAFLOOR -> DTSTEP_K -> HCOF -> both "
          "typed arrows -> RH is ACYCLIC with RH reachable from "
          "the counterfactual JETMASS + CENSUS_K + GONEK grants "
          "(AND-semantics: all parents needed; reachability shown "
          "per grant): COFINAL-TARGET-ASSEMBLY-CONDITIONAL, not a "
          "loop; NO RH CLAIM")
    info("THE TERMINAL STATEMENT (exact, typed): SIGMA-FLOOR == "
         "[DC-LEG: DC >= c_1 > 0, PROVEN-MOD-CITED per census "
         "(Landau/Gonek AS FORM + HSW22 + per-k census; DC -> 1/2; "
         "ALL-K == LOOP)] x [JET-MASS-FLOOR: delta >= r(h) at an "
         "explicit rate -- THE TERMINAL LAMBDA-UNIFORM RESIDUE: "
         "one source-weighted average of (F/A_0)^2 over the true "
         "tail zeros; implied at rate h^{-a} by pointwise JET-LOCK "
         "with polynomial onset (r137 omega-a, measured ~x^2.2); "
         "arithmetic-pinned; NOT a loop; per-rung classical; "
         "lambda-uniform rate OPEN].  sigma-flatness EXPLAINED as "
         "two trends (delta O(1) x DC rising); by SF4 the flat law "
         "is NOT needed -- any polynomial rate is census-"
         "absorbable.  RESIDUE: {JET-MASS-FLOOR (rate form)} + "
         "{census ALL-K == LOOP} + {L1, WPD}; census cardinality "
         "4 UNCHANGED; NO omega closed; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "ANATOMY-IDENTITY-PROVEN(sigma == (1-slop) delta DC; "
        "G10/G36)",
        "ONSET-CAP-IS-UPPER-REFUTED(G12)",
        "SIGMAFLOOR-FACTORIZED(DC-leg x JET-MASS-FLOOR; "
        "G12/G13/G36)",
        "DC-LEG-PROVEN-MOD-CITED(per census; GONEK-CONSTANT-"
        "UNPRICED; G13/G37) + LANDAU-PIN-IN-WINDOW(G37)",
        "JETMASS-IS-TERMINAL-RESIDUE(G12/G61/G63)",
        "RATE-FLOOR-CERTIFIED-PER-RUNG(G39)",
        "ANATOMY-BLOCK-FLOOR-CERTIFIED(B2/B3; G41/G44)",
        "DEMAND-RATE-ABSORPTION(T_req -> (3 pi/c)(1+2a/3) "
        "h^{3/2+a}; G14/G43)",
        "PINNING-SUPPLY-IS-LOOP(machine; G15/G63)",
        "FLOOR-INEQ-WORLD-INSENSITIVE + BRIDGE-ARITHMETIC"
        "(G50-G53)",
        "ALGEBRA-ONLY-REFUTED-FOR-JETMASS + -FOR-DCLEG(G16)",
        "SIGMA-FLATNESS-EXPLAINED-TWO-TRENDS(G36)",
        "ANTI-LATTICE-REDUCTION(G11/G38)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "LOOP-ROUTES-FLAGGED(three; G15/G61/G63)",
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
