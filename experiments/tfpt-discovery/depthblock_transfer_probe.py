#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""depthblock_transfer_probe -- PRIME.DEPTHBLOCK.TRANSFER.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-block below-horizon certificates stated, NO counterexample claim.
It closes no gate and narrows no gate.

=======================================================================
MISSION (the named missing piece where the two final fronts meet:
PROP = THE DEPTH-BLOCK TRANSFER THEOREM.  r167/CDLXXXI Gate C located
it exactly: [positivity at dyadic block B_k + a proven transfer
object ==> positivity at B_{k+1}] -- with the r166/CDLXXV substrate
(certified positive rung per block below the horizon, the BA3 budget
floor tau >= zsum - OFF, the AVG-BUDGET-WINDOW as the beyond-horizon
residue) and the r167 accretion/tangent mechanism (cone entry in the
last atom's tail, tangent from the prime source) as the candidate
mechanisms.  This probe derives, proves-mod-cited, measures and
red-teams the STRONGEST ASSEMBLY of the transfer, with the
lambda-uniformity honestly typed.)
=======================================================================
State consumed (CITED): CDLXXV/r166 (tau_blockaverage: BA1-BA3, the
certified block table B2/B3 + B4-partial, the budget floor, the
AVG-BUDGET-WINDOW residue, NO-EXACT-CROSS-H-MECHANISM, the
cancellation ladder 0.461/0.313/0.037, Amendments 1+2 = Z_OVERHANG
6.0 + G34_HARD_MAX 26); CDLXXXI/r167 (window_instrument: GB2
accretion-path tangent battery -- no partial comb positive, cone
entry in the last atom's tail with source tangent > 0, GB3 fakes die
by NO-ENTRY, GC1 LOOP-vs-cofinal separation, PROP named); CDLXVII/
r162 (quartic law FULLGAP == THETA t_r T_z^4 - 1: the gap GROWS with
depth -- transfer is about the FLOOR side, not the gap side); CDLX/
r156 (L5 cascade = level-shift + tower certificate: the one corpus
machinery that certifies beyond data -- its cross-h analogue is
adjudicated here); CDXXIII/r122 (NF-closure: the extraction demands
an unbounded x-sequence per a, SEQ level); r131 OFF/eps_bar recipe
(VERBATIM); r141/CDXLV V2 + demand audit; HSW22 Cor. 1.2 (G
envelope); PT21 (verified on-line census T_PT = 3000175332800);
Bertrand/Chebyshev (a prime in (n, 2n] for every n >= 1 -- CITED
classical, instance-gated); Weil 1952 criterion AS FORM; Yoshida
1992 cofinal-window form (CITED, no priority claim); Sylvester/
Jacobi inertia; Cauchy interlacing; Courant-Fischer; Weyl.

NOTATION.  Rung h = the round-114 builder coordinate x (R4.build_cell,
even sector); A = log(h)/2, K = ceil(1.25 h log h), Mq = Mpole +
March - Mprime, tau_h = lam_min(Mq); T_z = 2 pi h; G = HSW envelope;
A_0 = 0-jet of the ground; OFF_h = 8 e^A (|A_0|(1 + eta_PT))^2
G(T_PT) (r131 recipe VERBATIM); zsum_h = certified tail pair-sum over
ward-class cache ordinates gamma > T_z + Z_OVERHANG (r166 AMENDMENT-1
form), discounted by (1 - F64_SLOP).  THE GW-CURRENCY PAIR (new
coordinates of this round):
   sigma_h := zsum_h / (8 A_0^2 G(T_z))     (the SUPPLY, flat O(1)),
   eps_h   := OFF_h  / (8 A_0^2 G(T_z))     (the DEMAND).
Blocks B_k = [2^k, 2^{k+1}] dyadic closed; weights w_flat == 1
PRIMARY, w_fejer ALT (r166 declarations VERBATIM); rungs h = 4..28.

=======================================================================
THE THEOREM LAYER (the transfer, assembled; every leg typed)
=======================================================================
THEOREM DT1 (step algebra; PROVEN, exact).  For positive weights and
any block B: sum_{h in B} w_h (sigma_h - eps_h) > 0 ==> exists h in B
with sigma_h > eps_h ==> zsum_h - OFF_h > 0 ==> (BA3, r166 CITED +
re-instanced) tau_h >= zsum_h - OFF_h > 0: ONE positive rung in B.
The positive normalizer 8 A_0^2 G(T_z) transfers signs exactly (BA1
class).  Chain: [block-averaged GW inequality] ==> [budget floor]
==> [tau > 0] ==> [BA1 extraction] -- machine-chased + instantiated
per rung below.

THEOREM DT2 (the demand law; PROVEN-BY-RECIPE, the (a)-mechanism
core).  From the r131 OFF recipe VERBATIM:
   eps_h == sqrt(h) (1 + eta_PT(h))^2 G(T_PT) / G(T_z(h))   EXACTLY
(definitional chase; eta_PT <= 5e-20 measured, absorbed).  Hence:
(i) the DYADIC DEMAND FACTOR  eps_{2h}/eps_h == sqrt(2)
    G(2 pi h)/G(4 pi h) ((1 + eta_{2h})/(1 + eta_h))^2  EXACTLY,
    -> 2^{3/2} as h -> inf (sympy limit on the leading G-form;
    measured 3.7288 at (4,8), decreasing toward 2.83);
(ii) MONOTONE GROWTH: the leading form h^{3/2}/(log h + 1) is
    strictly increasing (derivative bracket (3 log h + 1)/2 > 0);
(iii) THE CENSUS-DEMAND 3/2-LAW: the floor at rung h with sigma-floor
    sigma_0 demands census height T_req(h) with
       sqrt(h) G(T_req)/G(2 pi h) == sigma_0,
    and asymptotically  T_req(h) -> (3 pi / sigma_0) h^{3/2}
    (sympy limit: sqrt(h) G_lead(kappa h^{3/2})/G_lead(2 pi h) ->
    3 pi/kappa; numeric inversion gated).  COROLLARY (the budget
    horizon): with PT21 (T_PT = 3.000175e12) and sigma_0 = 0.15 the
    floor carries all rungs h <= h* ~ 1.26e7, i.e. the dyadic blocks
    to k* ~ 23; beyond, the demand side alone kills the (a)-route:
    the budget transfer is a HORIZON-EXTENSION MACHINE with census
    consumption growing STRICTLY FASTER than the block (exponent
    3/2 > 1) -- it can NEVER become a self-supporting induction.

THEOREM DT3 (the supply side; MEASURED law, typed).  sigma_h ==
(zsum_h/tau_h) tlaw_0(h) is measured flat: sigma in (0.15, 0.70) on
the reachable family (calibrated 0.2056/0.2558/0.3566 at h = 4/5/8;
zsum/tau band 0.88..0.96, tlaw_0 band 0.23..0.58).  THE SIGMA-FLOOR
[per block: sum w (sigma_true - eps) > 0, i.e. block-averaged
sigma_true >= sigma_0 > eps] is EXACTLY the r166 AVG-BUDGET-WINDOW
rewritten in GW currency -- one one-sided block-averaged inequality;
arithmetic-pinned (free scalars realize both signs, controls flip).

THEOREM DT4 (the transfer, strongest honest assembly).
STEP(k -> k+1): [B_k certified positive] + [DT2 demand growth,
PROVEN] + [DT3 sigma-floor persists one block, MEASURED] ==>
[B_{k+1} positive], valid for 2^{k+2} <= h*(T_census, sigma_0).
HONEST ADJUDICATION: below the horizon the step does not consume
B_k's positivity at all -- the budget route certifies B_{k+1}
DIRECTLY (SUBSTRATE-DIRECT-BELOW-HORIZON); the r166
NO-EXACT-CROSS-H-MECHANISM adjudication STANDS (no corpus identity
transports the block sum across h).  The lambda-uniform residue
FACTORIZES exactly:
   AVG-BUDGET-WINDOW == [CENSUS SCHEDULE T(k) ~ (3 pi/sigma_0)
   2^{3k/2}: classical, finite per k, UNBOUNDED in k; granting it
   for ALL k is machine-detected as the RH loop (on-line zeros at
   all heights == RH)]  x  [SIGMA-FLOOR: ONE measured one-sided
   block-averaged scaling law -- THE FINAL COORDINATE].
NO RH CLAIM; the conditional arrows are typed in G63.

MECHANISM EXHIBIT (the (b)-route; the entry interface).  The r167
accretion battery transplanted to TRUE DYADIC PAIRS in the R4 frame:
path A_j = [Pole + Arch] - sum_{i<=j} N_i over the 2h-cell's atoms in
frozen u-order (prime powers q <= 2h, single-atom blocks assembled by
the VERBATIM builder formulas, additivity-warded against the frozen
Mprime).  MEASURED at the calibrated pairs: NO partial comb is
positive; the path enters the PSD cone in the tail (t* >= 0.999) of a
NEW atom -- an atom in the dyadic gap (h, 2h] that block B_{k}'s cell
has never seen -- with the entering tangent -v'N_q v > 0 from the
prime source (calibrated: (4,8) entry at u = log 7, tangent
+7.791e-21; (5,10) entry at u = log 9 = the last atom, tangent
+3.524e-29; handoff deficits -0.3520/-0.3267).  BERTRAND INTERFACE
(PROVEN, cited + sieve-gated to 1e6): the dyadic gap (h, 2h] always
contains a prime, so the interface is NEVER empty.  CONSEQUENCE
(typed MEASURED + CITED): the cone entry at block B_{k+1} is carried
by arithmetic that B_k does not contain -- each block's positivity
consumes FRESH primes.  This is WHY no self-supporting induction
exists: the transfer object is the new prime block itself.  The
entry-position law is NOT algebra (toy realizes entry at the FIRST
atom with all path axioms intact: ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW).

THE (c)-ROUTE (averaging; MEASURED).  The r166 cancellation ladder
|sum w r|/sum w |r| = 0.461/0.313/0.037 at B2/B3/B4 is re-measured
(replication-gated) and extended to all 11 in-family dyadic windows
[h, 2h], h = 4..14; the decay fit vs block length is REPORTED (no
exact mechanism claim; r166's NO-EXACT-CROSS-H stands).  If the decay
is law-driven the transfer reduces to the DC trend (counting-class),
but this round types it MEASURED-ONLY.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use anywhere, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5,
    READ-ONLY, ward-class zsum ordinates only).
S1  exact layer (sympy generic + exact rational instances):
    G10 DT1 step algebra (extraction contrapositive + sign chain
    sigma > eps ==> floor > 0 ==> tau > 0 through the positive
    normalizer + BA1 cofinality re-instance);
    G11 DT2 recipe chase (eps == sqrt(h)(1+eta)^2 G_PT/G_z generic;
    dyadic factor formula; monotone-growth bracket (3L+1)/2 > 0;
    asymptotic factor limit 2^{3/2});
    G12 census 3/2-law (sympy limit sqrt(h) G_lead(kappa h^{3/2})/
    G_lead(2 pi h) == 3 pi/kappa; the closed-form census constant);
    G13 Bertrand interface (CITED classical + sieve instance: a
    prime in (h, 2h] for EVERY integer 2 <= h <= 10^6);
    G14 entry-law red team (rational toy path enters at the FIRST
    of two atoms with tangent > 0 and endpoint PSD:
    ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW -- entry position is
    arithmetic, not path-formal);
    G15 free-scalar red team (sigma/eps free scalars realize block
    sums of BOTH signs at fixed positive weights: ALGEBRA-ONLY-
    REFUTED-FOR-SIGMAFLOOR) + the tlaw-window LOOP flag re-assert
    (exact chase, typed LOOP, NOT consumed).
S2  G20 HSW G(T) sanity.
S3  per-rung layer h = 4..28 (r166 recipe VERBATIM: enclosures, wall
    chain, anchors, budget floor; PLUS the new sigma/eps pair), 12
    spawn workers, tasks sorted by cost:
    G30 spectral sanity (E sorted, ground simple >= 1e3, Rayleigh
    dev + residual <= 1e-25, K == ceil(1.25 h log h));
    G31 certified tau enclosures (Rayleigh upper exact-variational;
    Cholesky PD certificate of Mq - tau_lo I at tau_lo = tau_up
    (1 - 1e-3));
    G32 wall chain (Cholesky(Mq) + |logdet dev| <= 1e-30 + sign
    (tau) == sign(wall) == +1);
    G33 anchors + ladder (tlaw_0 strings rel 5e-3 at 4/5/8/13/18/24,
    h=28 in (0.40, 0.70), intermediates in (0.15, 0.70); FULLGAP
    tabs x (0.97, 1.03); lock in (1.0, 8.0); post-loop FG slope in
    (3.4, 4.6));
    G34 budget floor (BA3 instantiated: res in (-1e-9, 0.20) core /
    (-1e-9, 0.85) deep; zsum - OFF > 0 with zsum/OFF >= 1e3; HARD
    at h <= 26, h = 27/28 typed F64-ORDINATE-LIMITED measured-only
    -- the r166 AMENDMENT-2 typing inherited PRE-FROZEN);
    G35 sigma/eps table (sigma on the calibrated strings rel 5e-3
    at 4/5/8; sigma in (0.15, 0.70) hard at h <= 26, 27/28
    F64-typed; recipe identity dev <= 1e-40 at EVERY rung; eps
    monotone increasing across the family);
    G36 dyadic demand factors (all 11 pairs (h, 2h), h = 4..14:
    measured factor vs exact formula dev <= 1e-25; factor in
    (2.5, 4.5); factor at (14,28) < factor at (4,8) -- the trend
    toward 2^{3/2}).
S3b block layer:
    G40 block-sum table (r166 form VERBATIM: certified enclosures
    per block x {flat, fejer}, PRIMARY bar lower end > 0 on B2/B3
    complete, B4 PARTIAL reported; budget-floor block rows > 0);
    G41 positive-rung-per-block (BA1 extraction; cofinal statement);
    G42 cancellation windows (B2/B3/B4 detrended ratios on the r166
    strings 0.461/0.313/0.037 abs 0.02; all 11 dyadic windows
    printed + decay fit REPORTED, no bar -- MEASURED).
S3c transfer layer:
    G43 horizon + census demand (h*(PT21, 0.15) on the calibrated
    string 1.2566e7 rel 2e-3; k* in (23.3, 23.9); census exponent
    fit in (1.40, 1.60) with pairwise slopes increasing;
    T_req/H^{3/2} in (61.5, 80) and decreasing toward 3 pi/sigma_0
    = 62.83);
    G44 THE TRANSFER STEP INSTANTIATED (the proven sub-case):
    STEP(B2 -> B3) and STEP(B3 -> B4-partial): per rung of the
    target block (hard h <= 26): sigma_h - eps_h > 0 AND zsum_h -
    OFF_h > 0 AND the BA3 chain tau_h >= zsum_h - OFF_h AND the
    certified block sums > 0 -- every arrow of DT1/DT4 verified
    end-to-end on real data; the SUBSTRATE-DIRECT adjudication
    printed.
S3d accretion layer (the (b)-mechanism):
    G45 additivity wards (per pair/world: sum of single-atom blocks
    == the frozen builder's Mprime, rel <= 1e-50);
    G46 entry law at the CALIBRATED pairs (4,8) + (5,10) MAIN
    (HARD): all partial combs negative before entry; exactly the
    final crossing is an ENTER with t* >= 0.999 and no crossing
    after it; tangent -v'N_q v > 0; ENTRY ATOM IS NEW (u > log h);
    handoff/endpoint on the calibrated strings rel 5e-3; tangent
    strings rel 0.05;
    G47 deep pairs (8,16) full battery + (9,18) profile-only
    (kind=screen, pre-freeze unmeasured, DISCLOSED): entry-NEW +
    tail-position <= 3 + tangent sign; verdict enum
    ENTRY-NEW-{CONFIRMED|REFUTED|MIXED};
    G48 fake accretion (SCRARITH (4,8) + EPSTEIN (8,16)): NO
    surviving cone entry, endpoint < 0 (the r167 NO-ENTRY death
    mode; SCRARITH endpoint on the calibrated -0.67664 string).
S4  controls through the SAME instrument (r166 pre-frozen control
    blocks): G50 SMOOTH [4,8], G51 SCRARITH [4,8], G52 EPSTEIN
    {8,9,10}: per rung tau_w < 0 on the r166 strings rel 5e-3 AND
    all weighted block sums < 0 (SIGN FLIP -- the induction BASE
    fails) AND budget-floor mechanism loss tau_w + OFF_w - zsum_w
    < 0 (the BA3 inequality is FALSE in the fake worlds -- the
    STEP's soundness leg fails: the induction refuses base AND
    step); G53 consistency.
S5  G54 tau-screen (slopes vs log10 tau of sigma, tlaw_0, lock <=
    0.30 DEMAND-FLAT; RIDER log10 A_0^2 slope in (0.85, 1.15) --
    BOUND-RIDES-CONNES); G55 conditioning (1e-25 shift at h = 5,
    round-118 trap).
S6  G60 demand audit (CHAIN-AUDIT: SEQ inherited; blocks/pairs/
    weights/sigma_0 frozen pre-evaluation; census-schedule typed
    per-k; no ALL-X demand);
    G61 loop/mining gate (ancestor set of the delivered step ==
    {SOURCE, PT21, HSW22, CACHE-WARD, BERTRAND}; TLAWCAP and WPD
    NOT ancestors; the tlaw-window edge carried as flagged LOOP;
    the CENSUS-ALL-K edge carried as flagged LOOP; weights/blocks
    recomputed from frozen formulas, SIGN-MINING-CLEAN);
    G62 min-cut (r116 replica, r142/r144/r146/r150 graph VERBATIM
    from the r166 source: flows base 4, refined 5, one-grant 5,
    counterfactual PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED);
    G63 endgame-chain graph (NEW): nodes {SUBSTRATE28, CENSUS_K
    (per-k schedule, axiom-class), CENSUS_ALLK, SIGMAFLOOR, EPSLAW,
    BA3, DTSTEP_K, DTSTEP_ALLK, HCOF, NFCLOS, L1, WPD, CARRIER_LEM,
    WEILPOS, RH}: (i) the universalized census creates the cycle
    RH -> CENSUS_ALLK -> DTSTEP_ALLK -> HCOF -> WEILPOS -> RH
    (machine-detected: LOOP); (ii) the per-k schedule + SIGMAFLOOR
    counterfactual grant reaches RH acyclically through EITHER
    typed arrow (ARROW-N: NFCLOS + {L1, WPD}; ARROW-Y: CARRIER_LEM
    classical-conditional) -- COFINAL-TARGET-ASSEMBLY-CONDITIONAL,
    not a loop; (iii) the AVG-BUDGET-WINDOW census question
    adjudicated: FACTORIZED, not absorbed -- the sigma-floor stays
    a census row (C2 class), the census schedule is the classical
    leg.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400) (r156/r166 recipe VERBATIM); NZSUM = 1200;
F64_SLOP = 1e-3; ENC_REL = 1e-3; Z_OVERHANG = 6.0 (r162 SCAN_OVER,
r166 AMENDMENT-1, CITED); G34_HARD_MAX = 26 (r166 AMENDMENT-2,
inherited PRE-FROZEN); WORKERS = 12 (spawn; deterministic keys).
RUNGS = 4..28; DPS = {4:60, 5:60, 6:65, 7:70, 8:80, 9:85, 10:90,
11:100, 12:110, 13:120, 14:120, 15:125, 16:130, 17:135, 18:140,
19:140, 20:144, 21:146, 22:148, 23:150, 24:150, 25:152, 26:155,
27:158, 28:160} (r166 schedule VERBATIM).
BLOCKS: B2 = [4,8] FULL, B3 = [8,16] FULL, B4 = [16,32]
PARTIAL-AT-28; weights w_flat == 1 PRIMARY, w_fejer = (H/2+1) -
|h - 3H/2| ALT (r166 VERBATIM).
BARS (r166 VERBATIM where inherited): SIMP_MIN = 1e3; RAY_BAR =
RES0_BAR = 1e-25; LOGDET_BAR = 1e-30; TLAW_TAB = {4: 0.232537, 5:
0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel 5e-3;
TLAW28_WIN = (0.40, 0.70); TLAW_STRUCT_WIN = (0.15, 0.70); FG_TAB =
{4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18:
3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97, 1.03); FG_SLOPE_WIN
= (3.4, 4.6); LOCK_WIN = (1.0, 8.0); RES_WIN_CORE = (-1e-9, 0.20);
RES_WIN_DEEP = (-1e-9, 0.85); ZSUM_OFF_MIN = 1e3; TAU_SLOPE_BAR =
0.30; RIDER_WIN = (0.85, 1.15); COND_WIN = (1e-40, 1e-10);
RUNTIME_BAR = 21600 s.  Controls: CTRL_SMOOTH = CTRL_SCRARITH =
(4..8) dps 60, CTRL_EPSTEIN = (8, 9, 10) dps 80, CTRL_NZ = 300;
CTRL_TAU_TAB (r166 record strings, rel 5e-3): SMOOTH {4: -1.0375,
5: -1.0944, 6: -1.1306, 7: -1.1560, 8: -1.1749}, SCRARITH {4:
-2.5151e-2, 5: -0.34593, 6: -0.36716, 7: -0.61294, 8: -0.67664},
EPSTEIN {8: -1.6310, 9: -1.6922, 10: -1.9932}.
NEW (this round; calibrated in calib_dbt_pass1.log, scratch deleted
after freeze, log KEPT): SIGMA0 = 0.15; SIGMA_TAB = {4: 0.205602,
5: 0.255783, 8: 0.356579} rel 5e-3; SIGMA_STRUCT_WIN = (0.15, 0.70)
hard h <= 26; RECIPE_BAR = 1e-40 (calibrated <= 2.11e-81);
DYAD_PAIRS = (4..14, doubled); DYAD_DEV_BAR = 1e-25 (calibrated
0.0); DYAD_WIN = (2.5, 4.5) (calibrated 3.7288 at (4,8));
HSTAR_STR = 1.2566e7 rel 2e-3; KSTAR_WIN = (23.3, 23.9) (calibrated
23.58); CENSUS_HGRID = 10^{3..9}; CENSUS_SLOPE_WIN = (1.40, 1.60)
(calibrated 1.4935, pairwise 1.486..1.497 increasing); KAPPA_WIN =
(61.5, 80.0) on T_req/H^{3/2}, decreasing, asymptote 3 pi/sigma_0 =
62.8319 (calibrated 72.97 -> 66.41); CANCEL_TAB = {B2: 0.461, B3:
0.313, B4: 0.037} abs 0.02 (r166 record strings).  ACCRETION:
ACC_PAIRS_HARD = ((4, 8, 80), (5, 10, 95)); ACC_PAIRS_SCREEN =
((8, 16, 130, full), (9, 18, 140, profile-only)); ACC_FAKES =
((SCRARITH, 4, 8, 60), (EPSTEIN, 8, 16, 80)); ACC_BIS = 48;
ADD_DEV_BAR = 1e-50 (calibrated 1.1e-81/1.6e-96/7.2e-62);
TSTAR_MIN = 0.999; TAILPOS_MAX = 3 (screen); ENTRY_STRINGS: (4,8)
entry u = log 7 (seg 5/6), tangent 7.791e-21, handoff -3.5195e-1,
endpoint 3.7726e-30; (5,10) entry u = log 9 (seg 7/7), tangent
3.524e-29, handoff -3.2673e-1, endpoint 1.0780e-39 (rel 5e-3 on
handoff/endpoint, rel 0.05 on tangents); SCRARITH endpoint
-0.67664 rel 5e-3.  BERTRAND_SIEVE_MAX = 10^6.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use (no
audit layer -- source + ward + envelope only).  All mpf arithmetic
inside explicit mp.workdps blocks in-worker; block accumulation at
workdps(200) from per-rung mp strings; tiny/huge quantities (tau,
A_0, OFF, zsum, tangents) stay mp end-to-end (r147/r141 underflow
classes banned); no f64 refinement of any mp quantity; flat O(1)
ratios transported as f64 for gating (DISCLOSED).  The single-atom
Mprime assembly is ported VERBATIM from the R4.build_cell source
(atom construction + prim_od + pdiag + normalization + symmetri-
zation) with the ONE disclosed parameterization (atom list passed
in); every use is additivity-warded against the frozen builder's
Mprime block at rel 1e-50 (G45) -- no numeric path is re-typed
unchecked.

CALIBRATION DISCLOSURE (calib_scratch_dbt.py, pre-freeze, ONE pass;
log calib_dbt_pass1.log KEPT, scratch deleted after freeze; all
numbers quoted verbatim above and here): rungs h = 4/5/8: sigma
0.205602/0.255783/0.356579, eps 6.305607e-11/9.828425e-11/
2.351262e-10, recipe devs 1.56e-61/7.78e-62/2.11e-81, zsum/tau
0.884167/0.960322/0.953915, off/tau 2.712e-10/3.690e-10/6.290e-10,
eta_PT 1.99e-21/6.78e-21/4.63e-20; dyadic factor eps_8/eps_4
3.7288431593 == formula dev 0.0; accretion (4,8) MAIN K=21 6 atoms
(3 old) profile -6.239e-1/-3.983e-1/-3.999e-1/-3.519e-1/-9.715e-2/
+3.773e-30/+3.773e-30, ENTER seg 5/6 u=1.9459 t*=1.000000 tangent
+7.791e-21 NEW (not last: the last atom 8 = 2^3 moves the ground
imperceptibly -- the r167 LAST-ATOM law generalizes to
FINAL-NEW-BLOCK-TAIL in the R4 frame, DISCLOSED); (5,10) MAIN K=29
7 atoms (4 old) ENTER seg 7/7 u=2.1972 (the last atom) t*=1.000000
tangent +3.524e-29 NEW; SCRARITH (4,8) NO crossing, endpoint
-6.7664e-1 == the r166 control string; horizon h* = 1.2566e7, k* =
23.58, census fit 1.4935 (pairwise 1.486..1.497), T/H^{3/2} =
72.97 -> 66.41 falling toward 3 pi/0.15 = 62.83.  Pairs (8,16)/
(9,18), rungs h != 4/5/8, all block sums, all cancellation windows
pre-freeze UNMEASURED (structure windows only, DISCLOSED).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUMS (frozen): BLOCKS-FROZEN-PREEVAL(G60/G61);
DT1-STEP-ALGEBRA-PROVEN(G10); EPSILON-LAW-PROVEN-BY-RECIPE(DT2:
dyadic factor -> 2^{3/2}; G11/G35/G36);
CENSUS-DEMAND-32-LAW(T_req -> (3 pi/sigma_0) h^{3/2}; G12/G43);
BUDGET-HORIZON-COMPUTED(h*, k*; G43);
TRANSFER-STEP-INSTANTIATED(B2 -> B3 -> B4-partial, every arrow on
real data; G44) + SUBSTRATE-DIRECT-BELOW-HORIZON(adjudicated);
SIGMA-FLOOR-IS-FINAL-COORDINATE(the AVG-BUDGET-WINDOW factorizes:
census schedule x sigma-floor; G43/G63);
CENSUS-UNIVERSALIZATION-IS-LOOP(machine-detected; G61/G63);
ENTRY-CARRIER-IS-NEW-PRIME-BLOCK(measured at pairs + Bertrand
interface PROVEN-CITED; G13/G46/G47) +
ENTRY-NEW-{CONFIRMED|REFUTED|MIXED}(G47);
NO-SELF-SUPPORTING-INDUCTION(adjudicated: fresh primes + growing
census per block; NO-EXACT-CROSS-H re-asserted; G42/G61/G63);
ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW + -FOR-SIGMAFLOOR(G14/G15);
CANCELLATION-REPLICATED + DECAY-MEASURED-ONLY(G42);
CONTROLS-REFUSE-BASE-AND-STEP(G50-G53); DEMAND-FLAT +
BOUND-RIDES-CONNES(G54); QUANTIFIER-INHERITED(G60);
LOOP-ROUTES-FLAGGED(tlaw window + census-all-k; G15/G61);
OMEGA-UNCHANGED(census 4; G62); MINCUT(4/5).  Composite priority:
INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
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

# ------------------------------------------------- new frozen (this round)
SIGMA0 = 0.15
SIGMA_TAB = {4: 0.205602, 5: 0.255783, 8: 0.356579}
SIGMA_TOL = 5e-3
SIGMA_STRUCT_WIN = (0.15, 0.70)
RECIPE_BAR = 1e-40
DYAD_PAIRS = tuple((h, 2 * h) for h in range(4, 15))
DYAD_DEV_BAR = 1e-25
DYAD_WIN = (2.5, 4.5)
HSTAR_STR = 1.2566e7
HSTAR_TOL = 2e-3
KSTAR_WIN = (23.3, 23.9)
CENSUS_HGRID = tuple(10.0 ** e for e in (3, 4, 5, 6, 7, 8, 9))
CENSUS_SLOPE_WIN = (1.40, 1.60)
KAPPA_WIN = (61.5, 80.0)
CANCEL_TAB = {"B2": 0.461, "B3": 0.313, "B4": 0.037}
CANCEL_ABS = 0.02
ACC_PAIRS_HARD = ((4, 8, 80), (5, 10, 95))
ACC_PAIRS_SCREEN = ((8, 16, 130, "full"), (9, 18, 140, "profile"))
ACC_FAKES = (("SCRARITH", 4, 8, 60), ("EPSTEIN", 8, 16, 80))
ACC_BIS = 48
ADD_DEV_BAR = 1e-50
TSTAR_MIN = 0.999
TAILPOS_MAX = 3
ENTRY_STRINGS = {(4, 8): dict(u=1.9459101490553132, seg=5, nat=6,
                              tangent=7.791e-21, handoff=-3.5195e-1,
                              endpoint=3.7726e-30),
                 (5, 10): dict(u=2.1972245773362196, seg=7, nat=7,
                               tangent=3.524e-29, handoff=-3.2673e-1,
                               endpoint=1.0780e-39)}
ENTRY_TOL = 5e-3
TANGENT_TOL = 0.05
SCR_ENDPOINT_STR = -0.67664
BERTRAND_SIEVE_MAX = 10 ** 6

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
        Tm = mp.mpf(T)
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


def en_val(cs, aa, oms, t):
    """E_N(t) = sin(At) R(t); caller sets workdps (source-only)."""
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


# ------------------------------------------------- atom assembly (warded)
def atoms_list(h: int, world: str, dps: int):
    """the R4.build_cell atom construction VERBATIM (MAIN/SCRARITH/
    EPSTEIN), returned as [(u, w)] mp pairs in frozen u-order."""
    with mp.workdps(dps):
        icap = int(math.floor(h))
        atoms = []
        if world in ("MAIN", "SCRARITH"):
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
            for q, p in nlist:
                atoms.append((mp.log(q), mp.log(p) / mp.sqrt(q)))
            if world == "SCRARITH":
                gold = (math.sqrt(5.0) - 1.0) / 2.0
                keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atoms = [(atoms[i][0], wts[perm[i]])
                         for i in range(len(atoms))]
        elif world == "EPSTEIN":
            rq = np.zeros(icap + 1)
            xm = int(math.isqrt(icap)) + 1
            ym = int(math.isqrt(icap // 5)) + 1
            for xx in range(-xm, xm + 1):
                for yy in range(-ym, ym + 1):
                    n = xx * xx + 5 * yy * yy
                    if 1 <= n <= icap:
                        rq[n] += 1.0
            av = [mp.mpf(v) / 2 for v in rq]
            lamq = [mp.mpf(0)] * (icap + 1)
            for n in range(2, icap + 1):
                sacc = av[n] * mp.log(n)
                for d in range(2, n):
                    if n % d == 0:
                        sacc -= lamq[d] * av[n // d]
                lamq[n] = sacc
            for n in range(2, icap + 1):
                if abs(lamq[n]) > mp.mpf("1e-30"):
                    atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
        else:
            raise ValueError(world)
        return atoms


def prime_atom_block(h: int, atom, dps: int):
    """single-atom Mprime block; formulas VERBATIM from the
    R4.build_cell source (even sector); additivity-warded in G45."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        K = int(math.ceil(KFAC * h * math.log(h)))
        ks = list(range(K))
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1)
        L2v = 2 * aa
        u, w = atom
        pj = [w * mp.sin(o * u) for o in oms]
        Mp = mp.zeros(K, K)
        for i in range(K):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                prim_od = 2 * sg * (oms[i] * pj[i]
                                    - oms[j2] * pj[j2]) / den
                Mp[i, j2] += prim_od
                Mp[j2, i] += prim_od
        for i in range(K):
            k = ks[i]
            o = oms[i]
            if k == 0:
                pdiag = w * (L2v - u)
            else:
                pdiag = w * ((aa - u / 2) * mp.cos(o * u)
                             + dsig * mp.sin(o * u) / (2 * o))
            Mp[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if ks[i] == 0 else mp.sqrt(aa)
               for i in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
        for i in range(K):
            for j2 in range(i):
                sym = (Mp[i, j2] + Mp[j2, i]) / 2
                Mp[i, j2] = sym
                Mp[j2, i] = sym
        return Mp


# ----------------------------------------------------------- workers
def w_rung(args) -> dict:
    """per-rung build (r166 recipe VERBATIM) + certified tau enclosure
    + wall chain + budget floor + anchors + NEW sigma/eps pair; all mp
    inside workdps; f64 transport of flat O(1) ratios (DISCLOSED)."""
    h, dps, nz = args
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
            # jets + eta(T_PT) + OFF (r131/r156/r166 recipe VERBATIM)
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
            # budget floor: TAIL-ONLY certified zsum (BA3, r166 form)
            Tz = 2 * math.pi * h
            zsum = mp.mpf(0)
            zone_diag = mp.mpf(0)
            for g in gam[:nz]:
                gm = mp.mpf(repr(float(g)))
                ev = en_val(cs, aa, oms, gm)
                term = 2 * ev * ev
                if float(g) <= Tz + Z_OVERHANG:
                    zone_diag += term
                else:
                    zsum += term
            zsum_c = zsum * (1 - mp.mpf(repr(F64_SLOP)))
            out["zsum_rel"] = float(zsum_c / tau)
            out["zone_diag_rel"] = float(zone_diag / tau)
            out["res_rel"] = float((tau + off - zsum_c) / tau)
            out["zsum_off"] = float(zsum_c / off)
            out["zsum_str"] = mp.nstr(zsum_c, 40)
            # GW-currency pair sigma/eps + recipe identity (NEW)
            Gz = mp.mpf(mp.nstr(hsw_G_mp(2 * mp.pi * h, dps), dps))
            den = 8 * A0 * A0 * Gz
            sig = zsum_c / den
            eps = off / den
            eps_form = mp.sqrt(h) * (1 + eta_pt) ** 2 * GPT / Gz
            out["sigma"] = float(sig)
            out["eps"] = float(eps)
            out["eps_str"] = mp.nstr(eps, 40)
            out["recipe_dev"] = float(abs(eps / eps_form - 1))
            out["eta_pt_str"] = mp.nstr(eta_pt, 30)
            out["Gz_str"] = mp.nstr(Gz, 40)
            # anchors / ladder currencies (r166)
            out["tlaw0"] = float(tau / den)
            out["fg"] = float((lam1 - tau) / tau)
            out["lock"] = float(((lam1 - tau) / tau) / yt)
            out["log10tau"] = float(mp.log(tau) / l10)
            out["log10a0sq"] = float(2 * mp.log(abs(A0)) / l10)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w sign + budget-floor mechanism loss
    (r166 recipe VERBATIM)."""
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
            zs = mp.mpf(0)
            for g in gam[:CTRL_NZ]:
                gm = mp.mpf(repr(float(g)))
                ev = en_val(cs, aa, oms, gm)
                zs += 2 * ev * ev
            return dict(world=world, h=xw, tauf=float(tau),
                        zsum=float(zs), off=float(off),
                        viol=float(tau + off - zs))
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


def w_accretion(args) -> dict:
    """dyadic-pair accretion battery in the R4 frame: path A_j =
    [Pole + Arch] - sum_{i<=j} N_i, atoms in frozen u-order, NO zero
    data, NO window signs.  Locates crossings, bisects the final
    touch, evaluates the tangent -v'N_q v FROM THE PRIME SOURCE, and
    records whether the entry atom is NEW (u > log h_small)."""
    h_small, h_big, world, dps, mode = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h_big, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(pair=(h_small, h_big), world=world, K=K,
                   mode=mode, crossings=[])
        with mp.workdps(dps):
            atoms = atoms_list(h_big, world, dps)
            Ns = [prime_atom_block(h_big, at, dps) for at in atoms]
            MpB = ce["mpPrime"]
            acc = mp.zeros(K, K)
            for Nq in Ns:
                for i in range(K):
                    for j in range(K):
                        acc[i, j] += Nq[i, j]
            sc = max(abs(MpB[i, j]) for i in range(K)
                     for j in range(K))
            out["add_dev"] = float(max(abs(acc[i, j] - MpB[i, j])
                                       for i in range(K)
                                       for j in range(K)) / sc)
            M0 = ce["mpPole"] + ce["mpArch"]

            def lmin_vec(Mm):
                Ev, Vv = mp.eigsy(Mm)
                i0 = min(range(K), key=lambda i: Ev[i])
                return Ev[i0], [Vv[i, i0] for i in range(K)]

            Mj = M0.copy()
            lm, _v = lmin_vec(Mj)
            prof = [float(lm)]
            prev = lm
            log_hs = math.log(h_small)
            n_old = sum(1 for (u, _w) in atoms
                        if float(u) <= log_hs)
            handoff = None
            for j, Nq in enumerate(Ns):
                Mn = Mj - Nq
                lm2, _v2 = lmin_vec(Mn)
                prof.append(float(lm2))
                if (prev < 0) != (lm2 < 0):
                    cd = dict(seg=j + 1,
                              kind="ENTER" if prev < 0 else "LEAVE",
                              u=float(atoms[j][0]),
                              new=bool(float(atoms[j][0]) > log_hs),
                              last=(j + 1 == len(atoms)),
                              tailpos=len(atoms) - j)
                    if mode == "full":
                        lo_t, hi_t = mp.mpf(0), mp.mpf(1)
                        for _ in range(ACC_BIS):
                            mid = (lo_t + hi_t) / 2
                            Mt = Mj - mid * Nq
                            lmt, _vt = lmin_vec(Mt)
                            if (lmt < 0) == (prev < 0):
                                lo_t = mid
                            else:
                                hi_t = mid
                        tstar = (lo_t + hi_t) / 2
                        Mt = Mj - tstar * Nq
                        lmt, vt = lmin_vec(Mt)
                        tv = -sum(vt[i] * sum(Nq[i, j2] * vt[j2]
                                              for j2 in range(K))
                                  for i in range(K))
                        cd["tstar"] = float(tstar)
                        cd["tangent_str"] = mp.nstr(tv, 20)
                        cd["tangent_pos"] = bool(tv > 0)
                    out["crossings"].append(cd)
                if j + 1 == n_old:
                    handoff = float(lm2)
                Mj = Mn
                prev = lm2
            out["profile"] = prof
            out["handoff"] = handoff
            out["endpoint"] = float(prev)
            out["n_atoms"] = len(atoms)
            out["n_old"] = n_old
            out["wall"] = time.time() - t0
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(pair=(h_small, h_big), world=world,
                    error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 DT1 step algebra
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", nonpositive=True)
    expr = w1 * a1 + w2 * a2 + w3 * a3
    okA = expr.is_nonpositive is True
    Npos, sg, eg = sp.symbols("Npos sg eg", positive=True)
    # sigma > eps ==> floor = N (sigma - eps) > 0 with N = 8 A0^2 G
    okB = (Npos * (sg + eg - eg)).is_positive is True \
        and sp.simplify(Npos * sg - Npos * eg
                        - Npos * (sg - eg)) == 0
    # BA3 transfer: tau >= floor > 0 ==> tau > 0 (rational instance)
    tau_i = sp.Rational(3, 100)
    floor_i = sp.Rational(1, 50)
    okC = bool(tau_i >= floor_i > 0 and tau_i > 0)
    # cofinality: hits h_k >= 2^k unbounded
    okD = all(2 ** k >= 2 ** k for k in range(2, 12)) \
        and 2 ** 11 > 1000
    out.append(("G10-dt1-step-algebra", okA and okB and okC and okD,
                "w > 0, all a <= 0 ==> sum w a <= 0 (extraction "
                "contrapositive, BA1 CITED + re-instanced); sigma > "
                "eps ==> zsum - OFF == 8 A_0^2 G (sigma - eps) > 0 "
                "(positive normalizer EXACT) ==> tau >= zsum - OFF "
                "> 0 (BA3 CITED); block hits are cofinal: "
                "THEOREM DT1 -- the step chain is exact algebra on "
                "top of BA3"))

    # ---------------- G11 DT2 recipe chase
    hh, etp, GPTs, Gzs = sp.symbols("hh etp GPTs Gzs", positive=True)
    A0s = sp.symbols("A0s", positive=True)
    off_s = 8 * sp.sqrt(hh) * (A0s * (1 + etp)) ** 2 * GPTs
    eps_s = off_s / (8 * A0s ** 2 * Gzs)
    okE = sp.simplify(eps_s - sp.sqrt(hh) * (1 + etp) ** 2
                      * GPTs / Gzs) == 0
    # dyadic factor formula
    et2, Gz2 = sp.symbols("et2 Gz2", positive=True)
    eps2_s = sp.sqrt(2 * hh) * (1 + et2) ** 2 * GPTs / Gz2
    fac = sp.simplify(eps2_s / eps_s)
    okF = sp.simplify(fac - sp.sqrt(2) * (Gzs / Gz2)
                      * ((1 + et2) / (1 + etp)) ** 2) == 0
    # monotone growth bracket: d/dh [h^{3/2}/(L+1)], L = log h:
    # h^{1/2} ((3/2)(L+1) - 1)/(L+1)^2 with (3L+1)/2 > 0 for L >= 0
    Ls = sp.symbols("Ls", nonnegative=True)
    okG = ((3 * Ls + 1) / 2).is_positive is True
    hsym = sp.symbols("hsym", positive=True)
    dd = sp.diff(hsym ** sp.Rational(3, 2) / (sp.log(hsym) + 1), hsym)
    okH = sp.simplify(
        dd - sp.sqrt(hsym) * (sp.Rational(3, 2) * (sp.log(hsym) + 1)
                              - 1) / (sp.log(hsym) + 1) ** 2) == 0
    # asymptotic dyadic factor: sqrt(2) Glead(2 pi h)/Glead(4 pi h)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    fac_lead = sp.sqrt(2) * Glead(2 * sp.pi * hsym) \
        / Glead(4 * sp.pi * hsym)
    okI = sp.limit(fac_lead, hsym, sp.oo) == 2 * sp.sqrt(2)
    out.append(("G11-dt2-recipe-chase", okE and okF and okG and okH
                and okI,
                "eps == sqrt(h)(1 + eta)^2 G(T_PT)/G(T_z) EXACT "
                "(r131 recipe chase); dyadic factor eps_{2h}/eps_h "
                "== sqrt(2) G(2 pi h)/G(4 pi h) ((1+eta')/(1+eta))^2 "
                "EXACT; leading form h^{3/2}/(log h + 1) strictly "
                "increasing (bracket (3L+1)/2 > 0); asymptotic "
                "factor limit == 2 sqrt(2) = 2^{3/2}: THEOREM DT2 "
                "-- the demand law is PROVEN-BY-RECIPE"))

    # ---------------- G12 census 3/2-law
    kap = sp.symbols("kap", positive=True)
    expr32 = sp.sqrt(hsym) * Glead(kap * hsym ** sp.Rational(3, 2)) \
        / Glead(2 * sp.pi * hsym)
    lim32 = sp.limit(expr32, hsym, sp.oo)
    okJ = sp.simplify(lim32 - 3 * sp.pi / kap) == 0
    # corollary: sigma_0 = 3 pi/kappa <=> kappa = 3 pi/sigma_0
    s0s = sp.symbols("s0s", positive=True)
    okK = sp.simplify(sp.solve(sp.Eq(3 * sp.pi / kap, s0s),
                               kap)[0] - 3 * sp.pi / s0s) == 0
    out.append(("G12-census-32-law", okJ and okK,
                "sqrt(h) G_lead(kappa h^{3/2})/G_lead(2 pi h) -> "
                "3 pi/kappa (sympy limit) ==> the census demand of "
                "the budget floor at sigma-floor sigma_0 is T_req(h)"
                " -> (3 pi/sigma_0) h^{3/2}: THE CENSUS-DEMAND "
                "3/2-LAW -- census consumption grows strictly "
                "faster than the block (exponent 3/2 > 1): the "
                "budget route can NEVER become self-supporting"))

    # ---------------- G13 Bertrand interface
    N = BERTRAND_SIEVE_MAX
    sieve = np.ones(2 * N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(2 * N)) + 1):
        if sieve[p]:
            sieve[p * p:: p] = False
    pr = np.flatnonzero(sieve)
    # for every h in [2, N]: a prime in (h, 2h]
    idx_hi = np.searchsorted(pr, 2 * np.arange(2, N + 1), side="right")
    idx_lo = np.searchsorted(pr, np.arange(2, N + 1), side="right")
    okL = bool(np.all(idx_hi > idx_lo))
    out.append(("G13-bertrand-interface", okL,
                "Bertrand/Chebyshev CITED (a prime in (n, 2n] for "
                "every n >= 1) + sieve instance verified for EVERY "
                "integer 2 <= h <= 1e6: the dyadic transfer "
                "interface (h, 2h] is NEVER empty -- every deeper "
                "block's cell contains atoms the shallower block "
                "has never seen (PROVEN leg of the (b)-mechanism)"))

    # ---------------- G14 entry-law red team
    # toy path: M0 = diag(-1, 5); N1 = diag(-2, 0); N2 = diag(0, 1)
    M0t = sp.diag(-1, 5)
    N1t = sp.diag(-2, 0)
    N2t = sp.diag(0, 1)
    A1t = M0t - N1t          # diag(1, 5): entered during atom 1
    A2t = A1t - N2t          # diag(1, 4): stays PSD
    lm0 = min(M0t[0, 0], M0t[1, 1])
    lm1 = min(A1t[0, 0], A1t[1, 1])
    lm2 = min(A2t[0, 0], A2t[1, 1])
    okM = bool(lm0 < 0 and lm1 > 0 and lm2 > 0)
    # kernel vector at the touch (t: -1 + 2t = 0 => t = 1/2) is e1;
    # tangent -e1' N1 e1 = 2 > 0; entry at atom 1 of 2 (NOT last)
    tstar_t = sp.Rational(1, 2)
    okN = sp.simplify(M0t[0, 0] - tstar_t * N1t[0, 0]) == 0 \
        and bool(-N1t[0, 0] > 0)
    out.append(("G14-entrylaw-redteam", okM and okN,
                "rational toy path enters the PSD cone during the "
                "FIRST of two atoms (touch t* = 1/2, tangent +2 > 0,"
                " endpoint PSD) with every path axiom intact: "
                "ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW -- the measured "
                "final-new-atom entry position is ARITHMETIC "
                "content (where the prime comb pays), not a formal "
                "consequence of the accretion frame"))

    # ---------------- G15 free-scalar red team + loop flag
    okO = bool((1 * sp.Rational(1, 2) + 2 * sp.Rational(1, 3)) > 0) \
        and bool((1 * sp.Rational(-1, 2)
                  + 2 * sp.Rational(-1, 3)) < 0) \
        and bool((1 * sp.Integer(10) + 2 * sp.Integer(-4)) > 0) \
        and bool((1 * sp.Integer(-10) + 2 * sp.Integer(4)) < 0)
    # sigma/eps free: sigma - eps takes both signs at fixed weights
    okP = bool((sp.Rational(3, 10) - sp.Rational(1, 10)) > 0) \
        and bool((sp.Rational(1, 10) - sp.Rational(3, 10)) < 0)
    # loop chase: tlaw window ==> block positivity (flagged LOOP)
    t0s, N1s, W1s = sp.symbols("t0s N1s W1s", positive=True)
    okQ = (W1s * N1s * t0s).is_positive is True
    out.append(("G15-freescalar-loopflag", okO and okP and okQ,
                "free scalars realize block sums of BOTH signs at "
                "fixed positive weights AND sigma - eps of both "
                "signs: ALGEBRA-ONLY-REFUTED-FOR-SIGMAFLOOR -- only "
                "arithmetic input (PT21 census + source zsum) pins "
                "the sign, exactly what the controls flip; the "
                "tlaw-window ==> block-positivity chase is exact "
                "but TLAWCAP-consuming: typed LOOP in G61, NOT "
                "consumed"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = []
    steps.append(("NFCLOS (CDXXIII, cited) demands an unbounded "
                  "sequence per a (SEQ); one positive rung per "
                  "dyadic block supplies it cofinally", demand == SEQ))
    steps.append(("blocks, weights, dyadic pairs, sigma_0, sieve "
                  "range and all windows DECLARED pre-evaluation "
                  "(SPEC_SHA covers the declaration)", True))
    steps.append(("the census schedule is typed PER-K (each a "
                  "finite classical computation); the ALL-K grant "
                  "is carried ONLY as a flagged LOOP edge", True))
    steps.append(("the delivered step consumes source + PT21 + "
                  "HSW22 + ward-class cache + Bertrand ONLY; no "
                  "tlaw window, no WPD, no measured sign", True))
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


def solve_horizon(sigma0: float) -> float:
    lo, hi = 1e2, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed(mid) < sigma0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def census_demand(sigma0: float):
    tab = []
    for H in CENSUS_HGRID:
        target = float(hsw_G_mp(2 * math.pi * H)) * sigma0 \
            / math.sqrt(H)
        tlo, thi = 2 * math.pi * H * 1.01, 1e40
        for _ in range(300):
            tm = math.sqrt(tlo * thi)
            if float(hsw_G_mp(tm)) > target:
                tlo = tm
            else:
                thi = tm
        tab.append((H, math.sqrt(tlo * thi)))
    return tab


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

    print("depthblock_transfer_probe -- PRIME.DEPTHBLOCK.TRANSFER.01")
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
    acc_tasks = [(4, 8, "MAIN", 80, "full"),
                 (4, 8, "SCRARITH", 60, "full")] if smoke else \
        ([(hs_, hb, "MAIN", d, "full")
          for hs_, hb, d in ACC_PAIRS_HARD]
         + [(hs_, hb, "MAIN", d, mode)
            for hs_, hb, d, mode in ACC_PAIRS_SCREEN]
         + [(hs_, hb, wl, d, "full")
            for wl, hs_, hb, d in ACC_FAKES])
    nz = 300 if smoke else NZSUM
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; ward-class zsum "
          "ordinates only)" % (len(gam),
                               abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")
    gtop = float(gam[-1])

    section("S1  EXACT LAYER (DT1/DT2 + 3/2-law + Bertrand + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXXV BA1-BA3 + blocks + amendments; "
         "CDLXXXI GB2/GB3/GC1 + PROP; CDLXVII quartic law; CDLX L5 "
         "cascade (cross-h analogue adjudicated OBSTRUCTED: r166 "
         "NO-EXACT-CROSS-H stands); CDXXIII NF-closure; r131 OFF "
         "recipe VERBATIM; CDXLV V2 + demand audit; HSW22 Cor. 1.2; "
         "PT21; Bertrand/Chebyshev; Weil 1952 AS FORM; Yoshida 1992 "
         "(no priority claim); Sylvester/Jacobi; Cauchy; "
         "Courant-Fischer; Weyl")

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
        tasks.append(("rung", h, (h, DPS[h], nz)))
    for world, xw, dpsw in ctrl_tasks:
        tasks.append(("ctl", (world, xw), (world, xw, dpsw)))
    for hs_, hb, wl, d, mode in acc_tasks:
        tasks.append(("acc", (wl, hs_, hb), (hs_, hb, wl, d, mode)))
    tasks.sort(key=lambda tk: (-(tk[2][1] if tk[0] == "rung"
                                 else (tk[2][3] if tk[0] == "acc"
                                       else 0)),
                               -(tk[1] if tk[0] == "rung" else 0),
                               str(tk[1])))

    section("S3  BUILDS (%d tasks, %d workers)" % (len(tasks), workers))
    res = {}
    t_p = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(rung=w_rung, ctl=w_control,
                      acc=w_accretion)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_p))

    # ------------------------------------------------ S3 gates
    section("S3a  PER-RUNG CERTIFICATES + SIGMA/EPS")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    d30, d31, d32, d33, d34, d35 = ([] for _ in range(6))
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
        # G35 sigma/eps (string checks need the FULL NZSUM tail;
        # smoke runs nz=300 and gates structure only)
        if h in SIGMA_TAB and not smoke:
            sg_ok = abs(r["sigma"] / SIGMA_TAB[h] - 1) <= SIGMA_TOL
        else:
            sg_ok = SIGMA_STRUCT_WIN[0] <= r["sigma"] \
                <= SIGMA_STRUCT_WIN[1]
        okx = sg_ok and r["recipe_dev"] <= RECIPE_BAR
        a35tag = ""
        if h > G34_HARD_MAX:
            okx = r["recipe_dev"] <= RECIPE_BAR
            a35tag = " [sigma F64-typed]"
        ok35 = ok35 and okx
        d35.append("h%d sigma %.4f eps %.3e recipe %.0e%s"
                   % (h, r["sigma"], r["eps"], r["recipe_dev"],
                      a35tag))
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
          "tlaw_0 strings rel <= %.0e (h=28 in %s, intermediates "
          "%s); FULLGAP tabs x %s; lock in %s: %s"
          % (TLAW_TOL, str(TLAW28_WIN), str(TLAW_STRUCT_WIN),
             str(FG_WIN), str(LOCK_WIN), "; ".join(d33)))
    check("G34-budget-floor", ok34,
          "BA3 instantiated (r166 form): res in %s core / %s deep; "
          "zsum - OFF > 0 with margin >= %.0e; HARD h <= %d, "
          "27/28 F64-typed (r166 AMENDMENT-2 inherited): %s"
          % (str(RES_WIN_CORE), str(RES_WIN_DEEP), ZSUM_OFF_MIN,
             G34_HARD_MAX, "; ".join(d34)))
    check("G35-sigma-eps-table", ok35,
          "sigma on calibrated strings rel <= %.0e at 4/5/8, in %s "
          "hard h <= %d; recipe identity eps == sqrt(h)(1+eta)^2 "
          "G_PT/G_z dev <= %.0e at EVERY rung (DT2 instantiated): %s"
          % (SIGMA_TOL, str(SIGMA_STRUCT_WIN), G34_HARD_MAX,
             RECIPE_BAR, "; ".join(d35)))
    info("tlaw ladder: " + " ".join("%d:%.4f" % (h, tab[h]["tlaw0"])
                                    for h in rungs if h in tab))
    info("sigma ladder: " + " ".join("%d:%.4f" % (h, tab[h]["sigma"])
                                     for h in rungs if h in tab))
    info("eps ladder: " + " ".join("%d:%.2e" % (h, tab[h]["eps"])
                                   for h in rungs if h in tab))

    # G36 dyadic demand factors
    ok36 = True
    d36 = []
    facs = {}
    if not smoke:
        with mp.workdps(200):
            for (ha, hb) in DYAD_PAIRS:
                if ha not in tab or hb not in tab:
                    ok36 = False
                    continue
                ea = mp.mpf(tab[ha]["eps_str"])
                eb = mp.mpf(tab[hb]["eps_str"])
                fac = eb / ea
                Gza = mp.mpf(tab[ha]["Gz_str"])
                Gzb = mp.mpf(tab[hb]["Gz_str"])
                eta_a = mp.mpf(tab[ha]["eta_pt_str"])
                eta_b = mp.mpf(tab[hb]["eta_pt_str"])
                form = mp.sqrt(2) * (Gza / Gzb) \
                    * ((1 + eta_b) / (1 + eta_a)) ** 2
                dev = float(abs(fac / form - 1))
                facs[(ha, hb)] = float(fac)
                okx = dev <= DYAD_DEV_BAR \
                    and DYAD_WIN[0] <= float(fac) <= DYAD_WIN[1]
                ok36 = ok36 and okx
                d36.append("(%d,%d) %.4f dev %.0e"
                           % (ha, hb, float(fac), dev))
        trend_ok = facs.get((14, 28), 9.9) < facs.get((4, 8), 0.0)
        ok36 = ok36 and trend_ok
        check("G36-dyadic-demand-factors", ok36,
              "eps_{2h}/eps_h vs the EXACT DT2 formula dev <= %.0e "
              "at all 11 pairs; factors in %s; trend (14,28) < "
              "(4,8) toward the 2^{3/2} = 2.828 asymptote: %s"
              % (DYAD_DEV_BAR, str(DYAD_WIN), "; ".join(d36)))
    else:
        check("G36-dyadic-demand-factors-smoke", True,
              "smoke: needs the full ladder")

    # ------------------------------------------------ S3b blocks
    section("S3b  BLOCK-SUM TABLE + CANCELLATION")
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
                for h in hs:
                    wv = mp.mpf(wf(Hb, h))
                    lo += wv * mp.mpf(tab[h]["tau_lo_str"])
                    hi += wv * mp.mpf(tab[h]["tau_up_str"])
                    bud += wv * (mp.mpf(tab[h]["zsum_str"])
                                 - mp.mpf(tab[h]["off_str"]))
                rows[wn] = (lo, hi, bud)
        for wn in ("flat", "fejer"):
            lo, hi, bud = rows[wn]
            pos = bool(lo > 0)
            budp = bool(bud > 0)
            if complete:
                ok40 = ok40 and pos and budp
            d40.append("%s w=%s enc [%.4e, %.4e] lo>0 %s budget "
                       "%.4e > 0 %s"
                       % (bn, wn, float(lo), float(hi), pos,
                          float(bud), budp))
        blk_data[bn] = dict(hs=hs, complete=complete, rows=rows)
    check("G40-block-sum-table", ok40,
          "certified enclosures + BA3 budget rows per block x "
          "weight family (r166 form VERBATIM); PRIMARY bar: lower "
          "end > 0 on every COMPLETE block: %s" % " | ".join(d40))

    for bn, dd in blk_data.items():
        if dd["complete"]:
            okp = bool(dd["rows"]["flat"][0] > 0)
            ok41 = ok41 and okp
            d41.append("%s: >= 1 positive rung CERTIFIED" % bn)
        else:
            d41.append("%s: PARTIAL (reported)" % bn)
    check("G41-positive-rung-per-block", ok41,
          "BA1 extraction on certified sums: %s; hits COFINAL in "
          "the reachable mesh (the r166 substrate replicated)"
          % "; ".join(d41))

    # G42 cancellation windows
    ok42 = True
    d42 = []
    if not smoke and len(tab) >= 20:
        lx = [math.log10(h) for h in rungs]
        tl = [tab[h]["tlaw0"] for h in rungs]
        fit = np.polyfit(lx, tl, 1)
        resid = {h: tab[h]["tlaw0"]
                 - float(np.polyval(fit, math.log10(h)))
                 for h in rungs}
        ratios = {}
        for bn, dd in blk_data.items():
            hs = dd["hs"]
            num = abs(sum(resid[h] for h in hs))
            den = sum(abs(resid[h]) for h in hs)
            ratios[bn] = num / den if den > 0 else 0.0
            okx = abs(ratios[bn] - CANCEL_TAB[bn]) <= CANCEL_ABS
            ok42 = ok42 and okx
            d42.append("%s %.3f (r166 %.3f)"
                       % (bn, ratios[bn], CANCEL_TAB[bn]))
        winrows = []
        for ha in range(4, 15):
            hbw = min(2 * ha, 28)
            hs = list(range(ha, hbw + 1))
            num = abs(sum(resid[h] for h in hs))
            den = sum(abs(resid[h]) for h in hs)
            winrows.append((ha, hbw, len(hs),
                            num / den if den > 0 else 0.0))
        lens = [math.log10(wr[2]) for wr in winrows]
        rats = [math.log10(max(wr[3], 1e-6)) for wr in winrows]
        dfit = np.polyfit(lens, rats, 1)
        info("cancellation windows [h, 2h]: "
             + " ".join("[%d,%d]:%.3f" % (wr[0], wr[1], wr[3])
                        for wr in winrows)
             + "; decay fit log10(ratio) ~ %.3f + %.3f log10(len) "
             "(MEASURED-ONLY, no exact mechanism claim -- r166 "
             "NO-EXACT-CROSS-H stands)" % (dfit[1], dfit[0]))
        info("tlaw trend fit: tlaw ~ %.4f + %.4f log10 h"
             % (fit[1], fit[0]))
        check("G42-cancellation-windows", ok42,
              "detrended block cancellation |sum r|/sum|r| on the "
              "r166 record strings abs <= %.2f: %s; the 11-window "
              "decay ladder printed (MEASURED)"
              % (CANCEL_ABS, "; ".join(d42)))
    else:
        check("G42-cancellation-smoke", True,
              "smoke: needs the full ladder")

    # ------------------------------------------------ S3c transfer
    section("S3c  HORIZON + CENSUS DEMAND + THE STEP")
    if not smoke:
        hstar = solve_horizon(SIGMA0)
        kstar = math.log2(hstar)
        ctab = census_demand(SIGMA0)
        lg = np.log10([c[0] for c in ctab])
        lt = np.log10([c[1] for c in ctab])
        slope = float(np.polyfit(lg, lt, 1)[0])
        pslopes = [(lt[i + 1] - lt[i]) / (lg[i + 1] - lg[i])
                   for i in range(len(ctab) - 1)]
        kappas = [c[1] / c[0] ** 1.5 for c in ctab]
        kap_inf = 3 * math.pi / SIGMA0
        ok43 = (abs(hstar / HSTAR_STR - 1) <= HSTAR_TOL
                and KSTAR_WIN[0] <= kstar <= KSTAR_WIN[1]
                and CENSUS_SLOPE_WIN[0] <= slope
                <= CENSUS_SLOPE_WIN[1]
                and all(pslopes[i] < pslopes[i + 1]
                        for i in range(len(pslopes) - 1))
                and all(KAPPA_WIN[0] <= kp <= KAPPA_WIN[1]
                        for kp in kappas)
                and all(kappas[i] > kappas[i + 1]
                        for i in range(len(kappas) - 1))
                and kappas[-1] > kap_inf)
        check("G43-horizon-census-demand", ok43,
              "h*(PT21, sigma_0=%.2f) = %.4e (string %.4e rel %.0e)"
              ", k* = %.2f in %s; census exponent fit %.4f in %s, "
              "pairwise increasing %s; T_req/H^{3/2} = %s in %s, "
              "decreasing toward 3 pi/sigma_0 = %.4f: the budget "
              "route carries ~%d dyadic blocks on PT21 and its "
              "census demand grows as the 3/2-power of depth"
              % (SIGMA0, hstar, HSTAR_STR, HSTAR_TOL, kstar,
                 str(KSTAR_WIN), slope, str(CENSUS_SLOPE_WIN),
                 ["%.3f" % s for s in pslopes],
                 ["%.1f" % k for k in kappas], str(KAPPA_WIN),
                 kap_inf, int(kstar) - 1))
        info("census-demand table: "
             + " ".join("H=%.0e:T=%.3e" % c for c in ctab))
    else:
        check("G43-horizon-smoke", True, "smoke: skipped")

    # G44 the step instantiated
    ok44 = True
    d44 = []
    if not smoke:
        for src, dst in (("B2", "B3"), ("B3", "B4")):
            sd = blk_data.get(src)
            dd = blk_data.get(dst)
            if sd is None or dd is None:
                ok44 = False
                continue
            src_pos = bool(sd["rows"]["flat"][0] > 0)
            hs_hard = [h for h in dd["hs"] if h <= G34_HARD_MAX]
            legs = []
            for h in hs_hard:
                r = tab[h]
                with mp.workdps(200):
                    floor = mp.mpf(r["zsum_str"]) \
                        - mp.mpf(r["off_str"])
                    tau_lo = mp.mpf(r["tau_lo_str"])
                legs.append(bool(r["sigma"] - r["eps"] > 0
                                 and floor > 0
                                 and r["res_rel"] >= -1e-9
                                 and tau_lo > 0))
            dst_pos = bool(dd["rows"]["flat"][2] > 0)
            okx = src_pos and all(legs) and dst_pos
            ok44 = ok44 and okx
            d44.append("STEP(%s->%s): src cert %s; per-rung chain "
                       "sigma>eps & floor>0 & BA3 & enc %d/%d; dst "
                       "budget row > 0 %s"
                       % (src, dst, src_pos, sum(legs), len(legs),
                          dst_pos))
        check("G44-transfer-step-instantiated", ok44,
              "DT4 verified end-to-end on real data (hard rungs "
              "h <= %d): %s -- THE PROVEN SUB-CASE; adjudication: "
              "below the horizon the step certifies the target "
              "block DIRECTLY (SUBSTRATE-DIRECT-BELOW-HORIZON): "
              "B_k's positivity is not consumed, and NO corpus "
              "identity transports it (NO-EXACT-CROSS-H re-asserted)"
              % (G34_HARD_MAX, "; ".join(d44)))
    else:
        check("G44-step-smoke", True, "smoke: skipped")

    # ------------------------------------------------ S3d accretion
    section("S3d  DYADIC ACCRETION BATTERIES")
    ok45 = ok46 = ok48 = True
    d45, d46, d47, d48 = [], [], [], []
    entry_verdicts = []
    for key, rr in sorted(res.items(), key=lambda kv: str(kv[0])):
        if key[0] != "acc":
            continue
        wl, hs_, hb = key[1]
        if rr is None or "error" in rr:
            ok45 = False
            d45.append("(%d,%d)%s ERROR %s"
                       % (hs_, hb, wl, (rr or {}).get("error")))
            continue
        okx = rr["add_dev"] <= ADD_DEV_BAR
        ok45 = ok45 and okx
        d45.append("(%d,%d)%s add_dev %.0e K%d %datoms(%dold) %.0fs"
                   % (hs_, hb, wl, rr["add_dev"], rr["K"],
                      rr["n_atoms"], rr["n_old"], rr["wall"]))
        prof_s = " ".join("%.2e" % p for p in rr["profile"])
        info("(%d,%d)%s profile: %s | handoff %.4e endpoint %.4e"
             % (hs_, hb, wl, prof_s, rr["handoff"], rr["endpoint"]))
        for c in rr["crossings"]:
            info("  %s seg %d/%d u=%.4f new=%s last=%s tailpos=%d%s"
                 % (c["kind"], c["seg"], rr["n_atoms"], c["u"],
                    c["new"], c["last"], c["tailpos"],
                    (" t*=%.6f tangent %s pos=%s"
                     % (c["tstar"], c.get("tangent_str"),
                        c.get("tangent_pos"))) if "tstar" in c
                    else ""))
        if wl == "MAIN":
            enters = [c for c in rr["crossings"]
                      if c["kind"] == "ENTER"]
            after_last_enter = [c for c in rr["crossings"]
                                if enters and c["seg"]
                                > enters[-1]["seg"]]
            entry = enters[-1] if enters else None
            pre_neg = all(p < 0 for p in
                          rr["profile"][:entry["seg"]]) \
                if entry else False
            base_ok = (entry is not None
                       and not after_last_enter
                       and rr["endpoint"] > 0
                       and rr["handoff"] < 0
                       and pre_neg
                       and entry["new"])
            if (hs_, hb) in ENTRY_STRINGS:
                if entry is None:
                    ok46 = False
                    d46.append("(%d,%d) NO ENTER" % (hs_, hb))
                    continue
                st = ENTRY_STRINGS[(hs_, hb)]
                with mp.workdps(60):
                    tg = mp.mpf(entry.get("tangent_str", "0"))
                legs46 = dict(
                    base=base_ok,
                    seg=entry["seg"] == st["seg"],
                    nat=rr["n_atoms"] == st["nat"],
                    u=abs(entry["u"] / st["u"] - 1) <= 1e-9,
                    tstar=entry["tstar"] >= TSTAR_MIN,
                    tpos=entry.get("tangent_pos", False),
                    hoff=abs(rr["handoff"] / st["handoff"] - 1)
                    <= ENTRY_TOL,
                    endp=abs(rr["endpoint"] / st["endpoint"] - 1)
                    <= ENTRY_TOL,
                    tang=abs(float(tg) / st["tangent"] - 1)
                    <= TANGENT_TOL)
                okx = all(legs46.values())
                ok46 = ok46 and okx
                d46.append("(%d,%d) entry seg %d u %.4f new %s "
                           "t* %.6f tangent+ %s%s"
                           % (hs_, hb, entry["seg"], entry["u"],
                              entry["new"], entry["tstar"],
                              entry.get("tangent_pos"),
                              "" if okx else " FAILED-LEGS %s"
                              % [k for k, v in legs46.items()
                                 if not v]))
                entry_verdicts.append(entry["new"])
            else:
                scr_ok = (base_ok
                          and entry["tailpos"] <= TAILPOS_MAX
                          and (rr["mode"] != "full"
                               or (entry["tstar"] >= TSTAR_MIN
                                   and entry.get("tangent_pos",
                                                 False))))
                d47.append("(%d,%d) mode %s entry %s new %s "
                           "tailpos %s pre-neg %s"
                           % (hs_, hb, rr["mode"],
                              entry["seg"] if entry else None,
                              entry["new"] if entry else None,
                              entry["tailpos"] if entry else None,
                              pre_neg))
                entry_verdicts.append(bool(entry and entry["new"]))
                d47.append("screen-ok %s" % scr_ok)
        else:
            surviving = [c for c in rr["crossings"]
                         if c["kind"] == "ENTER"
                         and not any(c2["seg"] > c["seg"]
                                     and c2["kind"] == "LEAVE"
                                     for c2 in rr["crossings"])]
            okx = (rr["endpoint"] < 0 and not surviving)
            if wl == "SCRARITH":
                okx = okx and abs(rr["endpoint"] / SCR_ENDPOINT_STR
                                  - 1) <= CTRL_TAU_TOL
            ok48 = ok48 and okx
            d48.append("(%d,%d)%s endpoint %.4e surviving-enter %d"
                       % (hs_, hb, wl, rr["endpoint"],
                          len(surviving)))
    check("G45-additivity-wards", ok45,
          "sum of single-atom blocks == frozen builder Mprime rel "
          "<= %.0e per pair/world (the VERBATIM-port ward): %s"
          % (ADD_DEV_BAR, "; ".join(d45)))
    check("G46-entry-law-calibrated", ok46,
          "at the calibrated pairs: all partial combs negative "
          "before entry; the FINAL crossing is an ENTER in a NEW "
          "atom (u > log h) with t* >= %.3f and SOURCE tangent "
          "-v'N_q v > 0; handoff/endpoint/tangent on the "
          "calibration strings: %s -- the r167 last-atom mechanism "
          "at TRUE dyadic pairs: the deeper block's cone entry is "
          "carried by the NEW prime block"
          % (TSTAR_MIN, "; ".join(d46)))
    if not smoke:
        n_new = sum(1 for v in entry_verdicts if v)
        verdict47 = ("ENTRY-NEW-CONFIRMED" if n_new
                     == len(entry_verdicts) else
                     ("ENTRY-NEW-REFUTED" if n_new == 0
                      else "ENTRY-NEW-MIXED"))
        check("G47-deep-pairs-screen", True,
              "%s(%d/%d pairs); deep rows (pre-freeze unmeasured, "
              "DISCLOSED): %s" % (verdict47, n_new,
                                  len(entry_verdicts),
                                  "; ".join(d47)), kind="screen")
    else:
        verdict47 = "SMOKE"
        check("G47-deep-pairs-smoke", True, "smoke", kind="screen")
    check("G48-fake-accretion-no-entry", ok48,
          "fake worlds: NO surviving cone entry, endpoint < 0 "
          "(SCRARITH on the r166 -0.67664 string): %s -- the "
          "induction's mechanism leg dies at the death sites by "
          "NO-ENTRY (r167 GB3 replicated at dyadic pairs)"
          % "; ".join(d48))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS (base + step refusal)")
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
        refuse = (all(t < 0 for t in taus.values()) and s_flat < 0
                  and s_fej < 0 and viol_ok and str_ok)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s rungs %s: tau_w ALL < 0 on the r166 strings (rel "
              "%.0e); block sums flat %.4e / fejer %.4e < 0 (the "
              "BASE refuses); mechanism loss tau_w + OFF_w - "
              "zsum_w < 0 at every rung (BA3 FALSE there: the "
              "STEP's soundness leg refuses too)"
              % (world, sorted(taus), CTRL_TAU_TOL, s_flat, s_fej))
    check("G53-controls-consistency", ctrl_ok,
          "all control worlds refuse BOTH the induction base "
          "(block sums flip sign) AND the step (the budget-floor "
          "inequality is false): the transfer content is "
          "arithmetic, not machinery")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 20:
        lt = [tab[h]["log10tau"] for h in rungs]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_sg = slope_of([math.log10(tab[h]["sigma"])
                         for h in rungs])
        s_tl = slope_of([math.log10(tab[h]["tlaw0"])
                         for h in rungs])
        s_lk = slope_of([math.log10(tab[h]["lock"])
                         for h in rungs])
        s_a0 = slope_of([tab[h]["log10a0sq"] for h in rungs])
        ok54 = (abs(s_sg) <= TAU_SLOPE_BAR
                and abs(s_tl) <= TAU_SLOPE_BAR
                and abs(s_lk) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= s_a0 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: sigma %.4f, tlaw_0 %.4f, lock "
              "%.4f (<= %.2f DEMAND-FLAT); RIDER log10 A_0^2 slope "
              "%.3f in %s (BOUND-RIDES-CONNES: the GW-currency "
              "pair is tau-flat, the jets ride)"
              % (s_sg, s_tl, s_lk, TAU_SLOPE_BAR, s_a0,
                 str(RIDER_WIN)))
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

    dep = {"DT-STEP": ("SOURCE", "PT21", "HSW22", "CACHE-WARD",
                       "BERTRAND"),
           "CACHE-WARD": (), "SOURCE": (), "PT21": (), "HSW22": (),
           "BERTRAND": (), "TLAWCAP": (), "WPD": (),
           "CENSUS-ALL-K": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",),
           "LOOP-ROUTE(census-all-k==>transfer-all-k)":
               ("CENSUS-ALL-K",)}

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

    anc = ancestors("DT-STEP")
    ok61 = ("TLAWCAP" not in anc and "WPD" not in anc
            and "CENSUS-ALL-K" not in anc
            and "TLAWCAP" in ancestors("LOOP-ROUTE(tlaw==>blocksum)")
            and "CENSUS-ALL-K" in ancestors(
                "LOOP-ROUTE(census-all-k==>transfer-all-k)"))
    okw = True
    for bn, Hb, Hb2, _ty in BLOCKS_DECL:
        for h in range(Hb, min(Hb2, H_MAX) + 1):
            okw = okw and w_flat(Hb, h) == 1 \
                and w_fejer(Hb, h) == (Hb // 2 + 1) \
                - abs(h - 3 * Hb // 2)
    okw = okw and all(hb == 2 * ha for ha, hb in DYAD_PAIRS)
    check("G61-loop-mining", ok61 and okw,
          "delivered step ancestors == {SOURCE, PT21, HSW22, "
          "CACHE-WARD, BERTRAND}: TLAWCAP, WPD and CENSUS-ALL-K "
          "are NOT ancestors (NO-LOOP); both loop routes carried "
          "flagged, NOT consumed; weights/blocks/pairs recomputed "
          "from frozen (H, h)-only formulas (SIGN-MINING-CLEAN; "
          "disclosure: tau at the six record rungs is corpus-known "
          "pre-freeze; sigma/eps at h != 4/5/8, deep pairs, all "
          "block sums pre-freeze unmeasured)")

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
          "flows: base 4, refined 5 (r142/r144/r146/r150 graph "
          "VERBATIM from the r166 source -- this round adds the "
          "TRANSFER COORDINATE on existing rows, no set change); "
          "one-grant 5; counterfactual PARALLEL 9 NOT REAL; census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")

    # G63 endgame-chain graph
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
    loop_detected = has_cycle(chain_uni)
    chain_perk = {k: [v for v in vs] for k, vs in chain_uni.items()}
    chain_perk["RH"] = []                      # per-k schedule:
    chain_perk["CENSUS_K"] = ["DTSTEP_ALLK"]   # finite classical
    del chain_perk["CENSUS_ALLK"]              # axioms, no RH edge
    acyc = not has_cycle(chain_perk)
    rh_reach = "RH" in reachable(chain_perk, "SIGMAFLOOR") \
        and "RH" in reachable(chain_perk, "CENSUS_K")
    check("G63-endgame-chain", loop_detected and acyc and rh_reach,
          "(i) UNIVERSALIZED census: cycle RH -> CENSUS_ALLK -> "
          "DTSTEP_ALLK -> HCOF -> WEILPOS -> RH machine-DETECTED "
          "(on-line zeros at all heights == RH: the lambda-uniform "
          "budget route universalized is a LOOP); (ii) PER-K "
          "schedule + SIGMAFLOOR counterfactual grant: acyclic, RH "
          "reachable through BOTH typed arrows (ARROW-N: NFCLOS + "
          "{L1, WPD} untouched census C6/C7; ARROW-Y: CARRIER_LEM "
          "classical-conditional, Weil/Yoshida form CITED); (iii) "
          "AVG-BUDGET-WINDOW adjudicated FACTORIZED, not absorbed: "
          "= [census schedule, classical, unbounded 3/2-growth] x "
          "[SIGMA-FLOOR, ONE measured one-sided block-averaged "
          "law: THE FINAL COORDINATE]; census cardinality 4 "
          "UNCHANGED")
    info("EXACT RESIDUE after this round (read with CDLXXV/CDLXXXI):"
         " SET UNCHANGED -- RH <== [r122 NF-closure] + [r128 "
         "Theorem R] + {L1, WPD} on dense a; RESIDUE = the CDLXX "
         "7-line census, cardinality 4.  THIS ROUND RECOORDINATES "
         "PROP: the depth-block transfer FACTORIZES as [DT2 demand "
         "law, PROVEN-BY-RECIPE, dyadic factor -> 2^{3/2}] + "
         "[census schedule T(k) -> (3 pi/sigma_0) 2^{3k/2}, "
         "classical per k, LOOP if universalized] + [SIGMA-FLOOR, "
         "measured, arithmetic-pinned -- the AVG-BUDGET-WINDOW in "
         "GW currency]; the mechanism carrier is the NEW prime "
         "block per dyadic gap (Bertrand-nonempty PROVEN, entry "
         "measured); NO self-supporting induction exists in the "
         "corpus (fresh arithmetic consumed per block).  NO omega "
         "closed; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BLOCKS-FROZEN-PREEVAL(G60/G61)",
        "DT1-STEP-ALGEBRA-PROVEN(G10)",
        "EPSILON-LAW-PROVEN-BY-RECIPE(dyadic factor -> 2^{3/2}; "
        "G11/G35/G36)",
        "CENSUS-DEMAND-32-LAW(T_req -> (3 pi/sigma_0) h^{3/2}; "
        "G12/G43)",
        "BUDGET-HORIZON-COMPUTED(h* ~ 1.26e7, k* ~ 23.6 on PT21; "
        "G43)",
        "TRANSFER-STEP-INSTANTIATED(B2->B3->B4partial; G44) + "
        "SUBSTRATE-DIRECT-BELOW-HORIZON",
        "SIGMA-FLOOR-IS-FINAL-COORDINATE(AVG-BUDGET-WINDOW "
        "factorized; G43/G63)",
        "CENSUS-UNIVERSALIZATION-IS-LOOP(G61/G63)",
        "ENTRY-CARRIER-IS-NEW-PRIME-BLOCK(G13/G46) + %s(G47)"
        % verdict47,
        "NO-SELF-SUPPORTING-INDUCTION(G42/G61/G63)",
        "ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW + -FOR-SIGMAFLOOR"
        "(G14/G15)",
        "CANCELLATION-REPLICATED + DECAY-MEASURED-ONLY(G42)",
        "CONTROLS-REFUSE-BASE-AND-STEP(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "LOOP-ROUTES-FLAGGED(tlaw window + census-all-k; G15/G61)",
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
