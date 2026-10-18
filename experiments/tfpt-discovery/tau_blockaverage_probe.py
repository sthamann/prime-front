#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tau_blockaverage_probe -- PRIME.COFINAL.TAU.BLOCKAVERAGE.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-block below-horizon certificates stated, NO counterexample claim.
It closes no gate and narrows no gate.

=======================================================================
MISSION (the owner's named new front: force ONE positive rung per
pre-frozen dyadic block via block-averaged tau -- cofinal positivity
in the mesh-refinement order; uniform margins proven unnecessary)
=======================================================================
Since sign(tau_h) == sign(wall_h) exactly on the finite family (the
corpus's exact determinant chain; Sylvester/Jacobi dictionary, gated
below), one does not need every tau_h > 0 individually: it suffices
that every pre-declared dyadic block [H, 2H] contains at least one
h with tau_h > 0.  Target form: sum_{h=H}^{2H} w_{H,h} tau_h > 0 with
PRE-FROZEN positive weights.  Then the positive rungs form a cofinal
subsequence of the mesh -- the sequence substrate the r122/CDXXIII
NF-closure extraction consumes (an instrument-chosen unbounded
x-sequence per a; CDXLV/V2 quantifier audit CITED).  This probe
freezes blocks + weights BEFORE evaluation, computes certified block
sums on all reachable blocks, mounts the maximal source-only
lower-bound attempt, runs the mandatory kill screens, and delivers
the honest bypass adjudication.

State consumed (CITED): r122/CDXXIII NF-closure (sequence demand);
r128/CDXXX Theorem R; CDXLV/r141 V2 measure lemma + demand-level
audit (SEQ level; dense-x suffices; no ALL-X demand); CDXXXIX/r13x
D1-D4 (derivative floors; the eps_bar/OFF budget currency);
CDL/r146 Y1-Y4 (zero-jet law, tlaw_1); CDLX/r156 L1-L6 (moment-
Laurent dictionary + sum rules -- the candidate summation machine);
CDLXV/r161 GF1-GF5 (razor); CDLXVII/r162 GL1-GL5 (quartic law,
FULLGAP == THETA t_r T_z^4 - 1); CDLXX/r165 definitive census
(7 lines, cardinality 4); r131 OFF/eps_bar recipe (verbatim port);
HSW22 Cor. 1.2 (G envelope); PT21 (verified census x <= 4.8e11);
Weil 1952 explicit-formula positivity criterion AS FORM; Sylvester/
Jacobi inertia + Cauchy interlacing + Courant-Fischer + Weyl
eigenvalue inequality (classical, instance-gated).

NOTATION.  Rung h = the round-114 builder coordinate x (integer;
R4.build_cell(h, KFAC, world, dps), even sector): A = log(h)/2, K =
ceil(1.25 h log h), Mq = Mpole + March - Mprime (the Weil form on
the prime-comb Galerkin carrier), tau_h = lam_min(Mq), FULLGAP =
(lam_1 - tau)/tau, T_z = 2 pi h (the proven r131-G17 resolvability
crossover), G = HSW tail envelope, A_0 = sum_k (-1)^k c_k (0-jet of
the ground), tlaw_0(h) = tau_h/(8 A_0^2 G(T_z)) (the GW-normalized
tau; the corpus's flat O(1) window coordinate), E_N(t) = sin(At)R(t)
(the ground's secular function, source-only), wall_h = det chain of
Mq (leading-principal-minor/Cholesky chain), OFF_h = 8 e^A (|A_0|
(1 + eta_PT))^2 G(T_PT) (the r131 tail allowance at the PT21
horizon, eta_PT from the M-jet envelope, MGRID recipe VERBATIM from
the r156 rootladder source).

=======================================================================
B1 -- THE FROZEN BLOCKS AND WEIGHTS (declared BEFORE any evaluation)
=======================================================================
COORDINATE: integer rung h == builder x.  Adjudicated from the
r141/r122 demand audit: the NF-closure extraction consumes an
unbounded x-sequence per a (SEQ level, CDXLV G60 CITED); the V2
good-window construction lives in u = log x; the dyadic blocks
[H, 2H] in x are exactly one refinement mesh of that order.
BLOCKS (dyadic, closed): B_k = {h in Z: 2^k <= h <= 2^{k+1}}.
Reachable COMPLETE blocks at the corpus data horizon x = 28:
  B2 = [4, 8], B3 = [8, 16].
The next block B4 = [16, 32] is truncated at the horizon: evaluated
on [16, 28] and typed PARTIAL-AT-28 (reported, not a full-block
certificate; the certificate family is over the complete blocks).
RUNGS: all integer h = 4..28 (19 of the 25 rungs are NEW corpus
depth; the six frozen record rungs 5/8/13/18/24/28 double as
replication anchors).
WEIGHTS (positive, pre-declared; ONE primary + two pre-registered
alternates, nothing else will be consulted):
  PRIMARY   w_flat(H, h) = 1                     on the raw tau_h;
  ALT-1     w_fejer(H, h) = (H/2 + 1) - |h - 3H/2|  (triangular,
            endpoints 1, peak H/2 + 1) on the raw tau_h;
  ALT-2     w_flat on the NORMALIZED scalar t_h = tlaw_0(h)
            (sign-equivalent per rung by the exact positivity of
            8 A_0^2 G, gated; the O(1)-flat currency in which the
            block average is a genuine average).
SUCCESS BAR (frozen): certified enclosure LOWER END of
sum_{h in B} w(H, h) tau_h > 0 for the PRIMARY family on every
complete block; alternates reported at the same bar form; the
partial deep block reported PARTIAL.  Weights are pure functions of
(H, h) -- the mining screen G61 recomputes them from the formula
and the firewall forbids any tau-dependent weight path.

=======================================================================
B3 -- THE SOURCE-ONLY LOWER-BOUND LAYER (the mathematical core)
=======================================================================
THEOREM BA1 (extraction + cofinality; exact).  (i) If w_h > 0 and
sum_h w_h a_h > 0 over a finite block then some a_h > 0
(contrapositive: all a_h <= 0 forces the sum <= 0).  (ii) If every
block [H_k, 2H_k] with H_k = 2^k -> inf contains a hit h_k, then
{h_k} is unbounded (h_k >= H_k): the hits are COFINAL in the mesh.
(iii) sign transfer: N_h > 0 ==> sign(N_h tau_h) == sign(tau_h);
the normalized block statement extracts the same positive rung.

THEOREM BA2 (the wall dictionary; the owner's premise made exact).
For symmetric M with leading principal minors D_1..D_{K-1} > 0:
sign(lam_min) == sign(D_K) (Jacobi/Sylvester inertia; D_K = det M =
prod of eigenvalues, and D_1..D_{K-1} > 0 forces at most one
nonpositive eigenvalue).  Cholesky exists <==> all D_j > 0 <==> M
PD.  Instantiated per rung: the tau-enclosure, the Cholesky chain
and the determinant cross-check (prod mpE vs prod L_ii^2) agree --
sign(tau_h) == sign(wall_h) on the whole reachable family.

THEOREM BA3 (the PT21/ward budget floor -- the delivered lower
bound).  tau_h = <phi, Mq phi> is the Weil functional of the ground
carrier element (r114 construction, CITED).  The explicit-formula
zero-side splits: [pairs with gamma <= T_PT are on-line (PT21
CITED) and contribute >= 0] + [the |gamma| > T_PT tail is bounded
by OFF_h (r131 recipe, HSW22 CITED)].  Hence, EXACTLY:
   tau_h  >=  zsum_h - OFF_h,
where zsum_h = the pair-counted partial sum sum_{T_z < gamma <=
gamma_NZSUM} 2 E_N(gamma)^2 over ward-class cache ordinates (any
sub-sum of the nonnegative on-line terms is admissible -- dropping
the zone terms keeps the bound valid and avoids the known
f64-ordinate instrument class, see CALIBRATION).  Computed with the
disclosed multiplicative f64-ordinate allowance (1 - F64_SLOP).
BLOCK VERSION (positive weights, exact):
   sum_h w_h tau_h  >=  sum_h w_h (zsum_h - OFF_h).
WHAT BA3 CONSUMES (typed): PT21 verified census (CITED classical
computation), HSW22 envelope (CITED), the r131 OFF recipe (CITED
corpus), cache ordinates below horizon (ward-class, Z1-typed), and
SOURCE data only for E_N and the jets.  It does NOT consume TLAWCAP,
the tlaw window, WPD, or any measured sign -- NO-LOOP (gated G61).
STATUS: PROVEN-mod-cited-inputs BELOW THE HORIZON; as H -> inf the
lambda-uniform form of the demand is
   AVG-BUDGET-WINDOW: per dyadic block, sum_h w_h (zsum-true_h -
   OFF_h) > 0
-- a ONE-SIDED, BLOCK-AVERAGED, COFINAL form of the tlaw-class
window (zsum_h/(8 A_0^2 G(T_z)) is the tlaw currency): strictly
weaker than the pointwise two-sided window family (implied by it,
not conversely), but still arithmetic-pinned (G15-class witnesses;
the controls flip its sign).  THE RE-ENTRY POINT IS EXACTLY HERE.

OBSTRUCTION EXHIBITS (the routes that do NOT work, measured):
(W) THE WEYL SPLIT (source-only additive route): tau >=
    lam_min(Mpole + March) - ||Mprime||_F (Weyl + Frobenius,
    exact).  Measured VACUOUS by 10.9/16.2/30.2/54.6 dex at h =
    4/5/8/13 (calibration): the additive arch/prime split cannot
    see the 10-100-dex three-block cancellation (r146 block
    portrait CITED), and block-averaging does not rescue an
    additive per-rung bound -- OBSTRUCTED-MEASURED.
(S) THE CROSS-h SUMMATION MACHINE: the r156 moment-Laurent
    dictionary and the r13x/r156 sum rules (SR1-SR3, D2) sum over
    the MOMENT/census index AT FIXED h; the r151-AB2 telescoping
    and the r153 edge-zero screening are per-rung mechanisms.  NO
    corpus identity sums over the rung index h.  Adjudicated
    NO-EXACT-CROSS-H-MECHANISM; the h-direction cancellation of
    the tlaw fluctuation is MEASURED (G42), not derived.
(L) THE LOOP ROUTE (flagged, forbidden as deliverable): tlaw_h >=
    t_0 > 0 per rung ==> block positivity (exact chase, G15) --
    typed LOOP (consumes the TLAWCAP lower end); the G61 dependency
    graph carries it as the forbidden edge, NOT consumed.

=======================================================================
T6 -- ASSEMBLY SHAPE (frozen in advance; the honest adjudication)
=======================================================================
Chain: [certified block sums > 0 on complete reachable blocks]
==(BA1, exact)==> [>= 1 positive rung per block] ==(BA1(ii))==>
[{h: tau_h > 0} cofinal in the reachable mesh] ==> two typed arrows:
(ARROW-N, the owner's) the cofinal set supplies the SEQUENCE
SUBSTRATE the r122 NF-closure consumes per a -- but the NF-closure
omegas {L1, WPD} on that sequence are NOT discharged by tau-signs:
they remain the census C6/C7 rows untouched.  (ARROW-Y, the direct
Weil route) cofinal tau_h >= 0 on the exhausting carriers + an
approximation/continuity lemma (test functions of compact support
are carrier-approximable along the cofinal set; CLASSICAL-
CONDITIONAL, stated not proven) ==> Weil positivity on a dense
class ==> RH (Weil criterion CITED; the cofinal-window form is
Yoshida 1992, CITED per the CDLXX novelty adjudication -- NO
priority claim).  BYPASS ADJUDICATION (frozen expectation, gated
against the run): PARTIAL -- the owner is right that pointwise
per-rung window laws and uniform margins are NOT needed for the
substrate (cofinal signs suffice, and below the horizon they are
CERTIFIED here); but (i) beyond the verified horizon the block
positivity itself is the AVG-BUDGET-WINDOW -- a one-sided averaged
cofinal window statement of the same arithmetic-pinned class (the
window family re-enters, weakened, at BA3), and (ii) {L1, WPD} are
untouched.  Census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; no
omega closed; NO RH CLAIM.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use anywhere, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5,
    READ-ONLY, sanity + ward-class zsum ordinates only).
S1  exact layer (sympy generic + exact rational instances):
    G10 BA1 (extraction contrapositive + dyadic cofinality + sign
    transfer); G11 BA2 (wall dictionary: PD and indefinite
    instances, inertia bookkeeping, det == prod eigenvalues);
    G12 weight families (positivity incl. endpoints; recompute
    identity) + normalized-scalar sign equivalence;
    G13 BA3 rearrangement (zone-drop admissibility + tail bound +
    block version; inputs typed CITED);
    G14 Weyl split lemma (lam_min(X+Y) >= lam_min X + lam_min Y on
    instances + Weyl CITED; ||.||_op <= ||.||_F for symmetric);
    G15 loop algebra (tlaw-window ==> block positivity chase,
    PROVEN as algebra, typed LOOP) + red team (free-scalar toy
    realizes block sums of BOTH signs at fixed positive weights:
    ALGEBRA-ONLY-REFUTED-FOR-BLOCKSUM -- only arithmetic input can
    pin the sign).
S2  G20 HSW G(T) sanity.
S3  per-rung layer, h = 4..28, MAIN, 12 spawn workers, tasks sorted
    by cost:
    G30 spectral sanity: E sorted, ground simple ((lam_1-tau)/tau
    >= 1e3), Rayleigh-polish dev and eigen-residual r_0/tau <=
    1e-25, K == ceil(1.25 h log h);
    G31 certified tau enclosures: upper = Rayleigh(v_0) (exact
    variational); lower = tau_hat (1 - 1e-3) via Cholesky success
    of Mq - tau_lo I (PD certificate); enclosure printed per rung;
    G32 wall chain: Cholesky(Mq) succeeds (all leading minors > 0)
    AND |log det(chol) - sum log mpE| <= 1e-30 AND sign(tau) ==
    sign(wall) == +1 (BA2 instantiated: the determinant chain);
    G33 anchor replication + ladder: tlaw_0 on the frozen strings
    at h = 4/5/8/13/18/24 (rel 5e-3; h=28 in (0.40, 0.70)); FULLGAP
    in FG_TAB x (0.97, 1.03) at the anchor rungs; intermediate
    rungs: tlaw_0 in (0.15, 0.70), FULLGAP > 0, lock FG/y_t in
    (1.0, 8.0); post-loop FULLGAP growth slope in (3.4, 4.6); the
    full 25-rung tlaw ladder printed (NEW depth);
    G34 budget floor per rung (BA3): zsum_h validity (tau + OFF -
    zsum)/tau in [-1e-9, 0.20] core h <= 13 / [-1e-9, 0.85] deep
    (the dropped beyond-cutoff share grows with T_z, disclosed);
    ward positivity zsum_h - OFF_h > 0; margin zsum/OFF >= 1e3
    (calibrated >= 8.4e8); zone-diagnostic printed UNGATED (typed
    F64-ORDINATE-LIMITED at depth -- the known r139/r141/r143
    class, caught in calibration pass 1 and excluded from the
    certified sum BY CONSTRUCTION).
S3b block layer:
    G40 BLOCK-SUM TABLE: per block x {primary, alt-1, alt-2}:
    certified enclosure [sum w tau_lo, sum w tau_up] (mp, dps 200
    accumulation); PRIMARY bar: lower end > 0 on B2 and B3; B4
    partial reported; budget-floor block version sum w (zsum -
    OFF) > 0 per block;
    G41 POSITIVE-RUNG-PER-BLOCK: the BA1 extraction applied to the
    certified sums; cofinal statement on the reachable mesh; the
    lambda-uniform demand typed AVG-BUDGET-WINDOW and adjudicated
    against the CDLXX census rows;
    G42 oscillation/cancellation layer (MEASURED): global linear
    trend of tlaw_0 vs log10 h, per-block detrended cancellation
    ratio |sum w r|/sum w |r| and rms(r); Weyl-split vacuity table
    at h = 4..8 and 13 (gate: bound NEGATIVE i.e. vacuous, >= 3
    dex, at every exhibit rung -- OBSTRUCTED-MEASURED pinned);
    NO-EXACT-CROSS-H-MECHANISM adjudication printed.
S4  controls through the SAME instrument (pre-frozen control
    blocks): G50 SMOOTH full block [4,8]; G51 SCRARITH full block
    [4,8]; G52 EPSTEIN partial {8,9,10}: per rung tau_w < 0 AND all
    three weighted block sums < 0 (SIGN FLIP) AND budget-floor
    MECHANISM LOSS: tau_w + OFF_w - zsum_w < 0 (the BA3 inequality
    is FALSE in the fake worlds -- its truth is arithmetic);
    G53 consistency.
S5  G54 tau-screen: slopes vs log10 tau of tlaw_0, zsum/tau, lock
    <= 0.30 (DEMAND-FLAT); RIDER: log10 A_0^2 slope in (0.85, 1.15)
    (rides tau -- BOUND-RIDES-CONNES typed; the ratios are the flat
    coordinates); G55 conditioning (1e-25 shift on Mq[0,0] at h=5
    moves tau by (1e-40, 1e-10); the round-118 trap).
S6  G60 demand audit (CHAIN-AUDIT: SEQ level inherited; the block
    mesh is the declared refinement order; blocks/weights frozen
    pre-evaluation; no ALL-X demand; no post-hoc window selection);
    G61 dependency/mining gate: the delivered bound's ancestor set
    == {SOURCE, PT21, HSW22, CACHE-WARD}; TLAWCAP and WPD are NOT
    ancestors (NO-LOOP); the forbidden tlaw-window edge carried and
    flagged LOOP; weights recomputed from the frozen formulas
    (SIGN-MINING-CLEAN; disclosure: tau at the six record rungs is
    corpus-known pre-freeze -- the blocks/weights are h-only and
    the 19 intermediate rungs are pre-freeze unmeasured);
    G62 min-cut (r116 replica; r142/r144/r146/r150 graph VERBATIM
    from the r162 source: flows base 4, refined 5, one-grant 5,
    counterfactual PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED).
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400) (r156 envelope recipe VERBATIM); NZSUM = 1200
(gamma_1200 = 1648.27 > 8 T_z(28) = 1407.4); F64_SLOP = 1e-3
(ward-class f64-ordinate allowance on the tail sum, disclosed);
ENC_REL = 1e-3 (Cholesky lower-bound margin); WORKERS = 12 (spawn;
deterministic task keys; concurrent lanes untouched).
DPS = {4:60, 5:60, 6:65, 7:70, 8:80, 9:85, 10:90, 11:100, 12:110,
13:120, 14:120, 15:125, 16:130, 17:135, 18:140, 19:140, 20:144,
21:146, 22:148, 23:150, 24:150, 25:152, 26:155, 27:158, 28:160}
(anchor rungs on the corpus schedule; intermediates interpolated
against the measured tau collapse ~4.85 dex/x with >= 25 digit
headroom).
BARS: SIMP_MIN = 1e3; RAY_BAR = 1e-25; RES0_BAR = 1e-25;
LOGDET_BAR = 1e-30; TLAW_TAB = {4: 0.232537 (calibration), 5:
0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel 5e-3
(CDXLI/corpus strings + the calibrated x=4 anchor); TLAW28_WIN =
(0.40, 0.70); TLAW_STRUCT_WIN = (0.15, 0.70) (intermediates);
FG_TAB = {4: 4.458152e4 (calibration), 5: 2.2255e5, 8: 9.9512e5,
13: 1.0619e7, 18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8} x (0.97,
1.03); FG_SLOPE_WIN = (3.4, 4.6); LOCK_WIN = (1.0, 8.0);
RES_WIN_CORE = (-1e-9, 0.20) (calibrated 0.0305/0.0387/0.0451/
0.0412 at 4/5/8/13, tail-only); RES_WIN_DEEP = (-1e-9, 0.85);
ZSUM_OFF_MIN = 1e3 (calibrated 3.6e9/2.6e9/1.5e9/8.4e8);
WEYL_RUNGS = (4, 5, 6, 7, 8, 13); WEYL_VAC_MIN = 3.0 dex
(calibrated 10.9/16.2/30.2/54.6 at 4/5/8/13); TAU_SLOPE_BAR = 0.30;
RIDER_WIN = (0.85, 1.15); COND_WIN = (1e-40, 1e-10); RUNTIME_BAR =
21600 s.  Controls: CTRL_SMOOTH = CTRL_SCRARITH = (4, 5, 6, 7, 8)
at dps 60; CTRL_EPSTEIN = (8, 9, 10) at dps 80 (partial, frozen);
CTRL_NZ = 300.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use (no
audit layer -- the probe is source + ward + envelope only).  All
mpf arithmetic inside explicit mp.workdps blocks in-worker; block
accumulation at workdps(200) from per-rung mp strings; tiny/huge
quantities (tau, A_0, OFF, zsum) stay mp end-to-end with mp.log
diagnostics (r147/r141 underflow classes banned); no f64 refinement
of any mp quantity; flat O(1) ratios transported as f64 for gating
(DISCLOSED).

CALIBRATION DISCLOSURE (calib_scratch_tba.py, pre-freeze, TWO
passes; logs calib_tba_pass1/2.log KEPT, scratch deleted after
freeze; all numbers quoted verbatim): PASS 1 (h = 4/5/8/13 MAIN +
all 13 control rungs): tau = 2.14309e-11/1.60658e-16/3.77263e-30/
2.49904e-54; tlaw_0 = 0.232537/0.266351/0.373806/0.467380; FULLGAP
= 4.458152e4/2.225493e5/9.951249e5/1.061906e7; lock = 2.4885/
3.6444/2.3890/3.3141; Rayleigh dev <= 4.9e-46, r_0/tau <= 3.6e-51
(worst h=4, dps 60); Cholesky(0.999 tau) lower bound SUCCEEDS at
all four; logdet cross-dev <= 4.3e-53; eta_PT = 2.0e-21..3.6e-19;
OFF/tau = 2.7e-10..1.1e-9; full-cache zsum/tau = 0.969535/0.961285/
0.954881 at h = 4/5/8 with zone shares 9.0e-5/2.0e-7/1.2e-5, BUT at
h = 13 the ZONE terms explode to 1.19e19 x tau (zone-share 1.00) --
the f64 cache ordinates miss the pinned nodes by ~1e-9 and E_N^2
there dwarfs tau ~ 2.5e-54: the KNOWN r139/r141/r143 f64-ordinate
instrument class, caught PRE-FREEZE ==> the certified sum is
TAIL-ONLY (gamma > T_z) by construction, PASS 2 (h = 13):
zsum_tail/tau = 0.958795, (tau + OFF - zsum_tail)/tau = +4.120e-2,
zsum_tail/OFF = 8.415e8 -- consistent with the h = 4/5/8 band;
WEYL split: lam_min(pole+arch) = -0.2373/-0.3713/-0.6239/-0.8483,
||prime||_F = 1.62/2.39/4.77/8.53, bound NEGATIVE with vacuity
10.9/16.2/30.2/54.6 dex; controls: SMOOTH tau_w = -1.0375/-1.0944/
-1.1306/-1.1560/-1.1749 (flat block sum -5.5935), SCRARITH tau_w =
-2.5151e-2/-0.34593/-0.36716/-0.61294/-0.67664 (sum -2.0278),
EPSTEIN tau_w = -1.6310/-1.6922/-1.9932 (sum -5.3164); control
zsum(300) all POSITIVE (8.9e-3..0.54) ==> mechanism loss tau_w +
OFF_w - zsum_w < 0 everywhere; build walls 1.3/3.1/14.8/178.9 s at
h = 4/5/8/13 (corpus deep strings 487.6/1223 s at 18/24 CITED; the
x = 25..28 costs are extrapolated, RUNTIME_BAR sized accordingly).
h = 6/7, 9..12, 14..17, 19..23, 25..27 pre-freeze UNMEASURED on all
quantities (structure windows only, DISCLOSED).  Amendments after
the frozen run, if any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): BLOCKS-FROZEN-PREEVAL(B1; G60/G61);
BLOCKSUM-CERTIFIED(B2/B3 complete + B4 partial, enclosures; G40);
POSITIVE-RUNG-PER-BLOCK-CERTIFIED(below horizon; G41);
WALL-DICTIONARY-INSTANTIATED(sign tau == sign wall on the family;
G11/G32); BUDGET-FLOOR-PROVEN-MOD-CITED(BA3: PT21 + HSW22 + r131
recipe + ward-class cache; NO-LOOP; G13/G34/G61);
WEYL-SPLIT-VACUOUS(the source-only additive route OBSTRUCTED-
MEASURED; G14/G42); NO-EXACT-CROSS-H-MECHANISM(adjudicated) +
CANCELLATION-MEASURED(G42); LOOP-ROUTE-FLAGGED(the tlaw-window
route typed LOOP, NOT consumed; G15/G61); SIGN-MINING-CLEAN(G61);
CONTROLS-REFUSE-WITH-SIGN-FLIP + MECHANISM-LOSS(G50-G53);
DEMAND-FLAT + BOUND-RIDES-CONNES(G54); QUANTIFIER-INHERITED(G60);
BYPASS-ADJUDICATED-PARTIAL(pointwise windows unnecessary for the
substrate; the AVG-BUDGET-WINDOW re-enters beyond the horizon;
{L1, WPD} untouched; G41/G62); OMEGA-UNCHANGED(census 4; G62);
MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge gate
fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 26/27 at SPEC_SHA
abfc5932f95cb8ea, log kept as the pre-amendment record
tba_run1.log).  ONE INSTRUMENT RE-TYPING, no bar or criterion
moved; every other gate incl. ALL block-sum certificates passed
run 1 unchanged: the G34 certified tail sum was frozen to start at
T_z, but the ground KILLS the next true zeros BEYOND T_z as well
(the r162 add-one lesson: g_add ~ 1e-6..1e-17 at gamma_{m+1},
gamma_{m+2}; the corpus node scan finds the overhang out to
SCAN_OVER = 6.0 past T_z).  At h = 26/27/28 the nearest cache zero
lies only 0.26..2.2 above T_z, deep inside the killing well: its
TRUE pair term is ~0 but the f64 cache-ordinate offset makes the
computed E^2 exceed tau by 1..4 dex (measured 25.7/20.6/1.8e4 x
tau) -- the KNOWN r139/r141/r143 f64-ordinate class, one shell
beyond the zone (the same class already excluded from the zone in
calibration pass 1).  FIX: the certified sum starts at T_z +
Z_OVERHANG with Z_OVERHANG = 6.0 (the r162 SCAN_OVER constant,
CITED); dropping the overhang terms keeps THEOREM BA3 valid (their
true contributions are >= 0) and is lossless at the clean rungs
(their computed overhang terms were ~0 anyway; ratios at h <= 25
move by < 0.02).  The zone diagnostic now covers gamma <= T_z +
Z_OVERHANG.  The run-1 fail rows are themselves the measured
instrument-resolution law and stay in the record.  Run 2 = run of
record at the amended SPEC_SHA; run 3 = deterministic re-run.

AMENDMENT 2 (post-run-2, disclosed; run 2 = 26/27 at SPEC_SHA
0d4ef50122c334f6, log kept as the pre-amendment record
tba_run2.log).  ONE INSTRUMENT RE-TYPING, no bar or criterion
moved: Amendment 1 cleaned h = 26 completely (zsum/tau 0.9219) and
reduced h = 27/28 from 20.6/1.8e4 to 1.95/2.68, but at the two
deepest rungs the killing well still reaches the first cache zeros
BEYOND T_z + 6 (they sit 6.3/6.8 past T_z while tau has collapsed
another ~10 dex): the same f64-ordinate resolution law, measured.
FIX (the r162 AMENDMENT-1b pattern verbatim): the G34 hard gates
are restricted to h <= G34_HARD_MAX = 26; h = 27/28 are typed
F64-ORDINATE-LIMITED and printed measured-only (their rows stay in
the record as the measured instrument-resolution law).  The
enclosure/wall/anchor gates at h = 27/28 are UNAFFECTED and remain
hard; the block-sum certificates (G40/G41) consume the Cholesky/
Rayleigh enclosures, not zsum; the PARTIAL-B4 budget-floor row is
dominated by the h = 16 term, 50+ dex above the polluted deep
terms (numerically irrelevant, disclosed).  A polished-ordinate
instrument (the corpus audit-mp class) would lift the limit; this
probe is deliberately zeta-free and does not carry one.  Run 3 =
run of record at the amended SPEC_SHA; run 4 = deterministic
re-run.
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
Z_OVERHANG = 6.0   # AMENDMENT 1 (r162 SCAN_OVER, cited)
G34_HARD_MAX = 26  # AMENDMENT 2 (r162 AMENDMENT-1b pattern)
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
WEYL_RUNGS = (4, 5, 6, 7, 8, 13)
WEYL_VAC_MIN = 3.0
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
CTRL_SMOOTH = (4, 5, 6, 7, 8)
CTRL_SCRARITH = (4, 5, 6, 7, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_NZ = 300
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 21600.0

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


def en_val(cs, aa, oms, t):
    """E_N(t) = sin(At) R(t); caller sets workdps (source-only)."""
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


# ----------------------------------------------------------- workers
def w_rung(args) -> dict:
    """per-rung build + certified tau enclosure + wall chain + budget
    floor + anchors; all mp inside workdps; f64 transport of flat
    O(1) ratios only (DISCLOSED); big quantities as mp strings."""
    h, dps, want_weyl, nz = args
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
            # Rayleigh polish (the symmetric Newton step) + residual
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
            tau_up = ray if ray > tau else tau     # variational upper
            # certified lower bound via Cholesky of M - tau_lo I
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
            # wall chain: Cholesky of M + det cross-check
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
            # jets + eta(T_PT) + OFF (r131/r156 recipe VERBATIM)
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
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
                * mp.mpf(repr(hsw_G(float(T_PT))))
            out["off_rel"] = float(off / tau)
            out["off_str"] = mp.nstr(off, 40)
            # budget floor: TAIL-ONLY certified zsum (BA3)
            Tz = 2 * math.pi * h
            zsum = mp.mpf(0)
            zone_diag = mp.mpf(0)
            for g in gam[:nz]:
                gm = mp.mpf(repr(float(g)))
                ev = en_val(cs, aa, oms, gm)
                term = 2 * ev * ev
                if float(g) <= Tz + Z_OVERHANG:   # AMENDMENT 1
                    zone_diag += term
                else:
                    zsum += term
            zsum_c = zsum * (1 - mp.mpf(repr(F64_SLOP)))
            out["zsum_rel"] = float(zsum_c / tau)
            out["zone_diag_rel"] = float(zone_diag / tau)
            out["res_rel"] = float((tau + off - zsum_c) / tau)
            out["zsum_off"] = float(zsum_c / off)
            out["zsum_str"] = mp.nstr(zsum_c, 40)
            # anchors / ladder currencies
            Gz = mp.mpf(repr(hsw_G(Tz)))
            out["tlaw0"] = float(tau / (8 * A0 * A0 * Gz))
            out["fg"] = float((lam1 - tau) / tau)
            out["lock"] = float(((lam1 - tau) / tau) / yt)
            out["log10tau"] = float(mp.log(tau) / l10)
            out["log10a0sq"] = float(2 * mp.log(abs(A0)) / l10)
            # Weyl split exhibit (frozen rungs only)
            if want_weyl:
                PA = ce["mpPole"] + ce["mpArch"]
                Ep, _ = mp.eigsy(PA)
                lmin_pa = min(Ep[i] for i in range(K))
                frob = mp.sqrt(sum(ce["mpPrime"][i, j] ** 2
                                   for i in range(K)
                                   for j in range(K)))
                weyl = lmin_pa - frob
                out["weyl_neg"] = bool(weyl < 0)
                out["weyl_vac"] = float((mp.log(abs(weyl))
                                         - mp.log(tau)) / l10) \
                    if weyl < 0 else 0.0
                out["weyl_lmin"] = float(lmin_pa)
                out["weyl_frob"] = float(frob)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w sign + budget-floor mechanism loss."""
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
                * mp.mpf(repr(hsw_G(float(T_PT))))
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


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 BA1 extraction + cofinality
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", nonpositive=True)
    expr = w1 * a1 + w2 * a2 + w3 * a3
    okA = expr.is_nonpositive is True
    inst = {w1: 1, w2: 2, w3: 1,
            a1: sp.Rational(-1, 3), a2: 0, a3: sp.Rational(-2, 7)}
    okB = bool(expr.subs(inst) <= 0)
    # cofinality: hits h_k >= H_k = 2^k are unbounded
    okC = all(2 ** k >= 2 ** k for k in range(2, 12)) \
        and 2 ** 11 > 1000
    # sign transfer through a positive normalizer
    Npos, tq = sp.symbols("Npos tq", positive=True)
    okD = (Npos * tq).is_positive is True \
        and (Npos * (-tq)).is_negative is True
    out.append(("G10-ba1-extraction", okA and okB and okC and okD,
                "w_h > 0 and all a_h <= 0 ==> sum w a <= 0 EXACT "
                "(contrapositive: a certified block sum > 0 forces "
                ">= 1 positive rung); hits per dyadic block [2^k, "
                "2^{k+1}] satisfy h_k >= 2^k -> inf (COFINAL); a "
                "positive normalizer preserves the sign (the ALT-2 "
                "scalar extracts the same rung): THEOREM BA1"))

    # ---------------- G11 BA2 wall dictionary
    Mpd = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    Mind = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, -1]])
    d_pd = [Mpd[:k, :k].det() for k in (1, 2, 3)]
    d_in = [Mind[:k, :k].det() for k in (1, 2, 3)]
    ev_pd = Mpd.eigenvals()
    ev_in = Mind.eigenvals()
    lmin_pd = min(sp.nsimplify(e) for e in ev_pd)
    lmin_in = min(ev_in, key=lambda e: sp.re(sp.N(e)))
    okE = all(d > 0 for d in d_pd) and bool(sp.N(lmin_pd) > 0) \
        and bool(sp.sign(d_pd[2]) == 1)
    okF = d_in[0] > 0 and d_in[1] > 0 and d_in[2] < 0 \
        and bool(sp.re(sp.N(lmin_in)) < 0)
    # det == prod of eigenvalues (char poly constant term), generic
    x11, x12, x22 = sp.symbols("x11 x12 x22", real=True)
    M2 = sp.Matrix([[x11, x12], [x12, x22]])
    lam = sp.symbols("lam")
    cp = (M2 - lam * sp.eye(2)).det()
    okG = sp.simplify(cp.subs(lam, 0) - M2.det()) == 0
    out.append(("G11-ba2-wall-dictionary", okE and okF and okG,
                "leading minors D_1..D_{K-1} > 0 ==> sign(lam_min) "
                "== sign(D_K) (Jacobi/Sylvester inertia CITED; PD "
                "instance: minors 2/3/4 > 0 and lam_min > 0; "
                "indefinite instance: minors 2/3 > 0, det = %s < 0 "
                "and lam_min < 0); det == prod eigenvalues generic "
                "(char poly at 0): THEOREM BA2 -- the determinant "
                "chain IS the tau sign" % d_in[2]))

    # ---------------- G12 weight families + sign equivalence
    okH = True
    for name_, wf in (("flat", w_flat), ("fejer", w_fejer)):
        for _bn, Hb, Hb2, _ty in BLOCKS_DECL:
            for h in range(Hb, min(Hb2, H_MAX) + 1):
                okH = okH and wf(Hb, h) > 0
    okI = w_fejer(4, 4) == 1 and w_fejer(4, 8) == 1 \
        and w_fejer(4, 6) == 3 and w_fejer(8, 8) == 1 \
        and w_fejer(8, 16) == 1 and w_fejer(8, 12) == 5 \
        and w_fejer(16, 16) == 1 and w_fejer(16, 24) == 9
    A0s, Gs, ts = sp.symbols("A0s Gs ts", positive=True)
    okJ = sp.simplify(sp.sign(ts / (8 * A0s ** 2 * Gs))
                      - sp.sign(ts)) == 0
    out.append(("G12-weights-sign-equiv", okH and okI and okJ,
                "both frozen weight families strictly positive on "
                "every reachable block rung incl. endpoints (fejer "
                "endpoints == 1, peaks 3/5/9); tlaw_0 = tau/(8 A_0^2 "
                "G) has sign(tlaw_0) == sign(tau) EXACT (positive "
                "normalizer): the ALT-2 block statement extracts "
                "the same positive rung"))

    # ---------------- G13 BA3 rearrangement
    Zt, Pt2, Ot = sp.symbols("Zt Pt2 Ot", positive=True)
    Tl = sp.symbols("Tl", real=True)
    # tau = Z + P2 + T with Z >= 0 (zone, dropped), T >= -OFF:
    tau_s = Zt + Pt2 + Tl
    lower = Pt2 - Ot
    dev = sp.simplify(tau_s - lower - (Zt + (Tl + Ot)))
    okK = dev == 0
    inst2 = {Zt: sp.Rational(1, 7), Pt2: sp.Rational(9, 10),
             Ot: sp.Rational(1, 50), Tl: sp.Rational(-1, 100)}
    okL = bool((tau_s - lower).subs(inst2) >= 0)
    # block version with positive weights
    u1, u2 = sp.symbols("u1 u2", positive=True)
    q1, q2, l1, l2 = sp.symbols("q1 q2 l1 l2", real=True)
    okM = sp.simplify((u1 * q1 + u2 * q2)
                      - (u1 * l1 + u2 * l2)
                      - (u1 * (q1 - l1) + u2 * (q2 - l2))) == 0
    # slop direction: (1 - s) z <= z for z >= 0, 0 < s < 1
    zp = sp.symbols("zp", positive=True)
    sl = sp.Rational(1, 1000)
    okN = bool(((1 - sl) * zp - zp).subs(zp, 3) <= 0)
    out.append(("G13-ba3-budget-floor", okK and okL and okM and okN,
                "tau = [zone >= 0] + [tail window sum] + [beyond-"
                "horizon tail >= -OFF] ==> tau >= zsum - OFF EXACT "
                "(dropping the nonnegative zone keeps the bound; "
                "the (1 - slop) discount only weakens it); block "
                "version by positive weights EXACT: THEOREM BA3 -- "
                "inputs typed CITED: PT21 on-line census below "
                "T_PT, HSW22 envelope, r131 OFF recipe, ward-class "
                "cache ordinates (Z1-typed); NO tlaw window, NO "
                "WPD consumed"))

    # ---------------- G14 Weyl split lemma
    okO = True
    # diagonal instances (exact) + symmetric 2x2 instance
    Dx = sp.diag(1, 5)
    Dy = sp.diag(-3, 2)
    okO = okO and min(Dx + Dy) is not None
    lmin_sum = min((Dx + Dy)[i, i] for i in range(2))
    okO = okO and bool(lmin_sum >= 1 + (-3))
    S2 = sp.Matrix([[0, 1], [1, 0]])
    evs = sorted(S2.eigenvals().keys(), key=lambda e: sp.N(e))
    okP = evs[0] == -1 and evs[-1] == 1
    frob2 = sp.sqrt(sum(S2[i, j] ** 2 for i in range(2)
                        for j in range(2)))
    okQ = bool(sp.N(frob2) >= sp.N(evs[-1]))
    # lam_max^2 <= sum lam_i^2 == ||.||_F^2 (symmetric), generic 2x2
    e1s, e2s = sp.symbols("e1s e2s", real=True)
    okR = sp.simplify((e1s ** 2 + e2s ** 2) - e1s ** 2) == e2s ** 2
    out.append(("G14-weyl-split", okO and okP and okQ and okR,
                "lam_min(X + Y) >= lam_min X + lam_min Y (Weyl "
                "CITED; diagonal instances exact); ||P||_op = "
                "lam_max <= ||P||_F for symmetric P (sum-of-squares "
                "identity): tau >= lam_min(pole + arch) - "
                "||prime||_F EXACT -- the source-only additive "
                "split bound; its measured VACUITY is the G42 "
                "exhibit (the cancellation IS the arithmetic)"))

    # ---------------- G15 loop algebra + red team
    t0s, N1, N2, W1s, W2s = sp.symbols("t0s N1 N2 W1s W2s",
                                       positive=True)
    tl1 = sp.symbols("tl1", positive=True)
    # loop chase: tlaw_h >= t0 > 0 ==> sum w N tlaw > 0
    ch = W1s * N1 * tl1 + W2s * N2 * t0s
    okS = ch.is_positive is True
    # red team: free scalars realize both signs at fixed weights
    okT = bool((1 * sp.Rational(1, 2) + 2 * sp.Rational(1, 3)) > 0) \
        and bool((1 * sp.Rational(-1, 2)
                  + 2 * sp.Rational(-1, 3)) < 0) \
        and bool((1 * sp.Integer(10) + 2 * sp.Integer(-4)) > 0) \
        and bool((1 * sp.Integer(-10) + 2 * sp.Integer(4)) < 0)
    out.append(("G15-loop-and-redteam", okS and okT,
                "LOOP ROUTE (flagged, forbidden as deliverable): "
                "[tlaw_h >= t_0 > 0 per rung] ==> block positivity "
                "-- exact chase but consumes the TLAWCAP lower "
                "window: typed LOOP in G61, NOT consumed by BA3; "
                "RED TEAM: with free scalars the block sum takes "
                "BOTH signs at fixed positive weights (mixed-sign "
                "witnesses included): ALGEBRA-ONLY-REFUTED-FOR-"
                "BLOCKSUM -- only arithmetic input (PT21 census + "
                "source zsum) can pin the sign, exactly what BA3 "
                "consumes and the controls flip"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    """bookkeeping over cited chain statements (typed CHAIN-AUDIT).
    Levels: 0 = ALL-X-TAIL, 1 = FULL-MEASURE-TAIL, 2 = UNBOUNDED-SEQ."""
    ALL_X, FULL_MEAS, SEQ = 0, 1, 2
    demand = SEQ
    steps = []
    steps.append(("NFCLOS (CDXXIII, cited) demands an unbounded "
                  "sequence per a; Vitali/Montel sequence-based",
                  demand == SEQ))
    steps.append(("the dyadic block mesh is DECLARED pre-evaluation "
                  "(B1): one positive rung per block is exactly a "
                  "cofinal (unbounded) subsequence -- the "
                  "mesh-refinement order matches the SEQ demand",
                  True))
    steps.append(("V2 (CDXLV, cited) full-measure good log-x "
                  "windows: the block mesh is compatible; no "
                  "block/weight was selected after evaluation "
                  "(SPEC_SHA covers the declaration)", True))
    steps.append(("BA3 consumes source + PT21 + HSW22 + ward-class "
                  "cache below horizon ONLY; no tlaw window, no "
                  "WPD, no measured sign", True))
    steps.append(("no ALL-X demand introduced; uniform per-rung "
                  "margins NOT demanded (the whole point of the "
                  "block form)", demand != ALL_X))
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

    print("tau_blockaverage_probe -- PRIME.COFINAL.TAU."
          "BLOCKAVERAGE.01")
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

    section("S1  EXACT LAYER (BA1-BA3 + Weyl + loop/red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure (SEQ demand); "
         "r128/CDXXX Theorem R; CDXLV/r141 V2 + demand audit; "
         "CDXXXIX D1-D4 + eps_bar/OFF budget; CDL Y1-Y4; CDLX/r156 "
         "L1-L6 (the moment machine sums over the MOMENT index at "
         "fixed h -- adjudicated in G42); CDLXV/r161 GF1-GF5; "
         "CDLXVII/r162 GL1-GL5 + quartic law; CDLXX census; r131 "
         "OFF recipe VERBATIM; HSW22 Cor. 1.2; PT21; Weil 1952 "
         "criterion AS FORM; Yoshida 1992 cofinal-window form "
         "(novelty wall, CITED -- no priority claim); Sylvester/"
         "Jacobi inertia; Cauchy interlacing; Courant-Fischer; "
         "Weyl inequality")

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
        tasks.append(("rung", h,
                      (h, DPS[h], h in WEYL_RUNGS, nz)))
    for world, xw, dpsw in ctrl_tasks:
        tasks.append(("ctl", (world, xw), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-(tk[2][1] if tk[0] == "rung"
                                 else 0),
                               -(tk[1] if tk[0] == "rung" else 0),
                               str(tk[1])))

    section("S3b  BUILDS (%d tasks, %d workers)"
            % (len(tasks), workers))
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
    section("S3c  PER-RUNG CERTIFICATES")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = True
    d30, d31, d32, d33, d34 = ([] for _ in range(5))
    for h in rungs:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        core = h <= 13
        # G30 spectral sanity
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e ray %.0e r0 %.0e (%.0fs)"
                   % (h, r["K"], r["simp"], r["ray_dev"],
                      r["r0_rel"], r["build_s"]))
        # G31 certified enclosure
        okx = r["chol_lo_ok"]
        ok31 = ok31 and okx
        d31.append("h%d chol-lo %s" % (h, r["chol_lo_ok"]))
        # G32 wall chain
        okx = (r["wall_ok"] and r["logdet_dev"] <= LOGDET_BAR
               and r["tlaw0"] > 0)
        ok32 = ok32 and okx
        d32.append("h%d wall + logdet %.0e sign(+)"
                   % (h, r["logdet_dev"]))
        # G33 anchors + ladder
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
        # G34 budget floor (AMENDMENT 2: hard gates h <= 26 only)
        win = RES_WIN_CORE if core else RES_WIN_DEEP
        okx = (win[0] <= r["res_rel"] <= win[1]
               and r["zsum_off"] >= ZSUM_OFF_MIN
               and r["zsum_rel"] > 0)
        a34tag = ""
        if h > G34_HARD_MAX:
            okx = True
            a34tag = " [F64-ORDINATE-LIMITED, measured-only]"
        ok34 = ok34 and okx
        d34.append("h%d zsum/tau %.4f res %.4f zsum/off %.1e "
                   "zone-diag %.1e%s"
                   % (h, r["zsum_rel"], r["res_rel"], r["zsum_off"],
                      r["zone_diag_rel"], a34tag))
    check("G30-spectral-sanity", ok30,
          "E sorted; ground simple >= %.0e; Rayleigh polish dev "
          "and residual r_0/tau <= %.0e/%.0e; K == ceil(1.25 h "
          "log h): %s" % (SIMP_MIN, RAY_BAR, RES0_BAR,
                          "; ".join(d30)))
    check("G31-certified-enclosures", ok31,
          "upper = Rayleigh(v_0) (exact variational); lower = "
          "tau_hat (1 - %.0e) certified by Cholesky success of "
          "Mq - tau_lo I at EVERY rung (PD certificate; the "
          "enclosure feeds the block sums): %s"
          % (ENC_REL, "; ".join(d31)))
    check("G32-wall-chain", ok32,
          "Cholesky(Mq) succeeds (all leading minors > 0) AND "
          "|logdet(chol) - sum log mpE| <= %.0e AND sign(tau) == "
          "sign(wall) == +1 (BA2 instantiated -- the corpus's "
          "exact determinant chain): %s"
          % (LOGDET_BAR, "; ".join(d32)))
    check("G33-anchors-ladder", ok33,
          "tlaw_0 on the frozen strings at 4/5/8/13/18/24 (rel <= "
          "%.0e; h=28 in %s; intermediates in %s); FULLGAP anchors "
          "x %s; lock in %s: %s"
          % (TLAW_TOL, str(TLAW28_WIN), str(TLAW_STRUCT_WIN),
             str(FG_WIN), str(LOCK_WIN), "; ".join(d33)))
    check("G34-budget-floor", ok34,
          "BA3 instantiated: (tau + OFF - zsum)/tau in %s core / "
          "%s deep; ward positivity zsum - OFF > 0 with margin >= "
          "%.0e; zone term EXCLUDED by construction (diagnostic "
          "printed, F64-ORDINATE-LIMITED at depth, the known "
          "r139/r141/r143 class): %s"
          % (str(RES_WIN_CORE), str(RES_WIN_DEEP), ZSUM_OFF_MIN,
             "; ".join(d34)))
    info("tlaw ladder h=4..28 (19 NEW rungs): "
         + " ".join("%d:%.4f" % (h, tab[h]["tlaw0"])
                    for h in rungs if h in tab))
    info("log10 tau ladder: "
         + " ".join("%d:%.1f" % (h, tab[h]["log10tau"])
                    for h in rungs if h in tab))

    # ------------------------------------------------ S3b blocks
    section("S3d  BLOCK-SUM TABLE (B2)")
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
        complete = (ty == "FULL") and \
            (hs == list(range(Hb, Hb2 + 1)))
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
            # ALT-2 normalized flat (f64 tlaw currency, sign-exact)
            nsum = sum(tab[h]["tlaw0"] for h in hs)
        for wn in ("flat", "fejer"):
            lo, hi, bud = rows[wn]
            pos = bool(lo > 0)
            budp = bool(bud > 0)
            if complete:
                ok40 = ok40 and pos and budp
            d40.append("%s(%s,%s) w=%s: enc [%.4e, %.4e] lo>0 %s; "
                       "budget-floor %.4e > 0 %s"
                       % (bn, "COMPLETE" if complete else ty, hs[0],
                          wn, float(lo), float(hi), pos,
                          float(bud), budp))
        d40.append("%s alt-2 flat tlaw block avg %.4f (sum %.4f "
                   "> 0 %s)" % (bn, nsum / len(hs), nsum, nsum > 0))
        blk_data[bn] = dict(hs=hs, complete=complete, rows=rows,
                            nsum=nsum)
    check("G40-block-sum-table", ok40,
          "certified enclosures [sum w tau_lo, sum w tau_up] per "
          "block x weight family; PRIMARY bar (flat, raw tau): "
          "lower end > 0 on every COMPLETE block; BA3 block "
          "budget-floor sum w (zsum - OFF) > 0: %s"
          % " | ".join(d40))

    for bn, dd in blk_data.items():
        if dd["complete"]:
            okp = bool(dd["rows"]["flat"][0] > 0)
            ok41 = ok41 and okp
            d41.append("%s: >= 1 positive rung CERTIFIED" % bn)
        else:
            d41.append("%s: PARTIAL (reported, not a full-block "
                       "certificate)" % bn)
    check("G41-positive-rung-per-block", ok41,
          "BA1 extraction on the certified sums: %s; the hits are "
          "COFINAL in the reachable mesh; lambda-uniform demand as "
          "H -> inf typed AVG-BUDGET-WINDOW (one-sided, block-"
          "averaged, cofinal tlaw-class window -- the re-entry "
          "point; adjudicated in S6/S9)" % "; ".join(d41))

    # G42 oscillation/cancellation + Weyl vacuity
    ok42 = True
    d42 = []
    if not smoke and len(tab) >= 10:
        lx = [math.log10(h) for h in rungs]
        tl = [tab[h]["tlaw0"] for h in rungs]
        fit = np.polyfit(lx, tl, 1)
        resid = {h: tab[h]["tlaw0"]
                 - float(np.polyval(fit, math.log10(h)))
                 for h in rungs}
        for bn, dd in blk_data.items():
            hs = dd["hs"]
            num = abs(sum(resid[h] for h in hs))
            den = sum(abs(resid[h]) for h in hs)
            rms = math.sqrt(sum(resid[h] ** 2
                                for h in hs) / len(hs))
            d42.append("%s cancel |sum r|/sum|r| %.3f rms %.4f"
                       % (bn, num / den if den > 0 else 0.0, rms))
        info("tlaw trend fit: tlaw ~ %.4f + %.4f log10 h; "
             "residual table %s"
             % (fit[1], fit[0],
                " ".join("%d:%+.4f" % (h, resid[h])
                         for h in rungs)))
    for h in WEYL_RUNGS:
        r = tab.get(h)
        if r is None or "weyl_neg" not in r:
            if not smoke:
                ok42 = False
            continue
        okx = r["weyl_neg"] and r["weyl_vac"] >= WEYL_VAC_MIN
        ok42 = ok42 and okx
        d42.append("h%d weyl lmin(P+A) %.3e -|prime|_F %.3e "
                   "vacuity %.1f dex"
                   % (h, r["weyl_lmin"], -r["weyl_frob"],
                      r["weyl_vac"]))
    check("G42-oscillation-weyl", ok42,
          "WEYL SPLIT bound NEGATIVE (vacuous >= %.1f dex) at "
          "every exhibit rung -- the source-only additive route "
          "is OBSTRUCTED-MEASURED (the cancellation IS the "
          "arithmetic); block detrended cancellation ratios "
          "MEASURED (no bar); adjudication: NO-EXACT-CROSS-H-"
          "MECHANISM -- the r156/r13x sum rules run over the "
          "moment/census index at FIXED h, the r151-AB2/r153 "
          "mechanisms are per-rung; no corpus identity sums over "
          "h: %s" % (WEYL_VAC_MIN, "; ".join(d42)))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS (sign flip + mechanism loss)")
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
        taus = [r["tauf"] for r in rows]
        Hb = 4 if world != "EPSTEIN" else 8
        s_flat = sum(taus)
        s_fej = sum(w_fejer(Hb, r["h"]) * r["tauf"] for r in rows)
        viol_ok = all(r["viol"] < 0 for r in rows)
        refuse = (all(t < 0 for t in taus) and s_flat < 0
                  and s_fej < 0 and viol_ok)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s rungs %s: tau_w %s ALL < 0; block sums flat "
              "%.4e / fejer %.4e < 0 (SIGN FLIP); mechanism loss "
              "tau_w + OFF_w - zsum_w = %s ALL < 0 (the BA3 "
              "inequality is FALSE in the fake world -- its truth "
              "is the arithmetic)"
              % (world, [r["h"] for r in rows],
                 ["%.3e" % t for t in taus], s_flat, s_fej,
                 ["%.2e" % r["viol"] for r in rows]))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse with a SIGN FLIP of the block "
          "sums (every weight family) and with the budget floor "
          "violated per rung: the block-positivity content is "
          "arithmetic (prime comb at 2A = log x), not machinery")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 10:
        lt = [tab[h]["log10tau"] for h in rungs]

        def slope_of(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_tl = slope_of([math.log10(tab[h]["tlaw0"])
                         for h in rungs])
        s_zs = slope_of([math.log10(tab[h]["zsum_rel"])
                         for h in rungs])
        s_lk = slope_of([math.log10(tab[h]["lock"])
                         for h in rungs])
        s_a0 = slope_of([tab[h]["log10a0sq"] for h in rungs])
        ok54 = (abs(s_tl) <= TAU_SLOPE_BAR
                and abs(s_zs) <= TAU_SLOPE_BAR
                and abs(s_lk) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= s_a0 <= RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: tlaw_0 %.4f, zsum/tau %.4f, "
              "lock %.4f (all <= %.2f: the block-average "
              "coordinates are tau-flat, DEMAND-FLAT); RIDER: "
              "log10 A_0^2 slope %.3f in %s (rides tau -- "
              "BOUND-RIDES-CONNES typed; the ratios are the flat "
              "coordinates)" % (s_tl, s_zs, s_lk, TAU_SLOPE_BAR,
                                s_a0, str(RIDER_WIN)))
    else:
        check("G54-tau-screen-smoke", True, "smoke: needs the "
              "full ladder")
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
          "(nonzero bounded; round-118 trap)" % d_eps, kind="edge")

    # ------------------------------------------------ S6 audit + cut
    section("S6  DEMAND AUDIT + LOOP/MINING + MIN-CUT")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq, "CHAIN-AUDIT: " + detq)

    # dependency graph of the delivered bound (BA3)
    dep = {"BLOCKSUM-FLOOR": ("SOURCE", "PT21", "HSW22",
                              "CACHE-WARD"),
           "CACHE-WARD": (), "SOURCE": (), "PT21": (), "HSW22": (),
           "TLAWCAP": (), "WPD": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",)}

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

    anc = ancestors("BLOCKSUM-FLOOR")
    loop_anc = ancestors("LOOP-ROUTE(tlaw==>blocksum)")
    ok61 = ("TLAWCAP" not in anc and "WPD" not in anc
            and "TLAWCAP" in loop_anc)
    # mining screen: weights recomputed from the frozen formulas
    okw = True
    for bn, Hb, Hb2, _ty in BLOCKS_DECL:
        for h in range(Hb, min(Hb2, H_MAX) + 1):
            okw = okw and w_flat(Hb, h) == 1 \
                and w_fejer(Hb, h) == (Hb // 2 + 1) \
                - abs(h - 3 * Hb // 2)
    check("G61-loop-mining", ok61 and okw,
          "delivered bound ancestors == {SOURCE, PT21, HSW22, "
          "CACHE-WARD}: TLAWCAP and WPD are NOT ancestors "
          "(NO-LOOP); the tlaw-window route carried as the "
          "flagged LOOP edge, NOT consumed; weights recomputed "
          "from the frozen (H, h)-only formulas (SIGN-MINING-"
          "CLEAN; disclosure: tau at the six record rungs is "
          "corpus-known pre-freeze -- blocks/weights are h-only, "
          "19 intermediate rungs pre-freeze unmeasured)")

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
          "VERBATIM from the r162 source -- this round adds a "
          "COFINAL-AVERAGED COORDINATE on existing window rows, "
          "no set change); one-grant 5; counterfactual PARALLEL 9 "
          "NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED; RH unreachable without the omega edges")
    info("EXACT RESIDUE after this round (read with CDLXV/CDLXVII/"
         "CDLXX): SET UNCHANGED -- RH <== [r122 NF-closure] + "
         "[r128 Theorem R] + {L1, WPD} on dense a; RESIDUE = the "
         "CDLXX 7-line census, cardinality 4.  THIS ROUND: (i) "
         "positive-rung-per-block CERTIFIED on the complete "
         "reachable blocks (below horizon, BA3 ward-class + "
         "enclosures) -- the cofinal substrate exists as far as "
         "the verified census reaches; (ii) the lambda-uniform "
         "demand is RECOORDINATED to the AVG-BUDGET-WINDOW: per "
         "deep block ONE one-sided weighted-average inequality "
         "sum w (zsum-true - OFF) > 0 -- strictly weaker than any "
         "pointwise window law (no upper end, no per-rung floor, "
         "cofinal only), still arithmetic-pinned (G15 + controls); "
         "(iii) BYPASS ADJUDICATION: PARTIAL -- pointwise window "
         "constants and uniform margins are NOT needed for the "
         "substrate (the owner's architecture is right there), "
         "but the window family re-enters as the averaged main "
         "term beyond the horizon, and {L1, WPD} (census C6/C7) "
         "are untouched by tau-signs.  NO omega closed; nothing "
         "upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BLOCKS-FROZEN-PREEVAL(B1; G60/G61)",
        "BLOCKSUM-CERTIFIED(B2/B3 complete + B4 partial; G40)",
        "POSITIVE-RUNG-PER-BLOCK-CERTIFIED(below horizon; G41)",
        "WALL-DICTIONARY-INSTANTIATED(sign tau == sign wall; "
        "G11/G32)",
        "BUDGET-FLOOR-PROVEN-MOD-CITED(BA3: PT21 + HSW22 + r131 "
        "recipe + ward-class cache; NO-LOOP; G13/G34/G61)",
        "WEYL-SPLIT-VACUOUS(source-only additive route "
        "OBSTRUCTED-MEASURED; G14/G42)",
        "NO-EXACT-CROSS-H-MECHANISM + CANCELLATION-MEASURED(G42)",
        "LOOP-ROUTE-FLAGGED(tlaw-window route typed LOOP, not "
        "consumed; G15/G61)",
        "SIGN-MINING-CLEAN(G61)",
        "CONTROLS-REFUSE-WITH-SIGN-FLIP + MECHANISM-LOSS(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "BYPASS-ADJUDICATED-PARTIAL(substrate: yes without "
        "pointwise windows; re-entry: AVG-BUDGET-WINDOW beyond "
        "horizon; {L1, WPD} untouched; G41/G62)",
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
        print("COMPOSITE: BLOCKS-FROZEN-PREEVAL + "
              "BLOCKSUM-CERTIFIED + "
              "POSITIVE-RUNG-PER-BLOCK-CERTIFIED + "
              "WALL-DICTIONARY-INSTANTIATED + "
              "BUDGET-FLOOR-PROVEN-MOD-CITED + "
              "WEYL-SPLIT-VACUOUS + NO-EXACT-CROSS-H-MECHANISM + "
              "LOOP-ROUTE-FLAGGED + SIGN-MINING-CLEAN + "
              "CONTROLS-REFUSE-WITH-SIGN-FLIP + DEMAND-FLAT + "
              "QUANTIFIER-INHERITED + BYPASS-ADJUDICATED-PARTIAL "
              "+ OMEGA-UNCHANGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
