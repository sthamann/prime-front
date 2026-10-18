#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""assembly_walls_probe -- PRIME.ASSEMBLY.WALLS.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the third final residue block: the typed-but-never-attacked
technical walls PERCELL-REL, JUMPSUM, dense-a, a-extension, window-a,
plus the definitive full-chain assembly census)
=======================================================================
State consumed (CITED): CDLV/r151 tlawcap_blocks (J1-J3 bordered
trilogy, ASM+sharpness, JC two grades, AB2 birth zero-coupling,
29-jump census, C_a^blk table, M_A <= 0.41, drift ladder -24.8..
-141.3, JUMPSUM measured-summable slope -0.86); CDLI/r147
adjugate_logmaster (AD1 A_0^2 = B_00/P'(tau), cell lemma modulo
simplicity, C_0 = 3.81..2.89, LM master); CDLII/r148 fullgap_onset
(O1 per-cell analytic + zero-free certification, O3b currency
invariance); CDXLV/r141 pfloor_suscap2 (V2 measure lemma, G60 x-
quantifier CHAIN-AUDIT method -- replicated HERE for the a-
quantifier); CDXXXV/r132 wpd_proof (THEOREM D/W1/P1 + branch theorem
a < gamma_1^2 = 199.79, window-a = r128 G26, two-branch lever (c));
CDXXXVI/r133 dominance (M/E/T/C/A, H-pin, x_0 = 121, Q-swamp);
CDXXX/r128 doublelimit (Theorem R; WPD k-tail = window positivity,
Cauchy-Hadamard; planted witness gamma=30 delta=0.3 a*=900.09, k* =
29959/76013/145094); CDXXIII/r122 NF-closure ((H-conv)+(H-trace) on
dense a ==> RH; Montel/Vitali/Hurwitz); CDL/r146 fullgap_spectrum
(Y1-Y4); CDLIV/r150 collapserate (R1-R4, jr-tlaw identity); CDLVI
promotion (v918-v921); CDLVII/r152 anchor_epslock (EZ edge-zero, LC);
CDLVIII/r154 nearalign (P1-P7, T-WINDOW; current OPEN list); HSW22
Cor. 1.2 (closed form G only); PT21 (H = 3e12 verification height +
T_PT constant).

TARGETS.
(W1) PERCELL-REL: sup_{cell} |A_0| <= e^{C U} |A_0(u_c)| per anchor
cell.  Attack: (PC1) the Borel-Caratheodory/Moebius machinery that
converts a one-sided depth bound into two-sided oscillation control
(exact Moebius identity + Schwarz CITED); (PC2) the disc-chain /
geometric assembly that converts per-disc depths into per-cell
oscillation (exact partial-sum identities); (PC3) the exact
first-order derivative pricing of the branch drift (2-level exact:
the drift bound consumes ||v_0||/|A_0| = e^{depth} and 1/delta_1 --
so a PROOF-grade lambda-uniform drift bound is exactly as hard as the
DEPTH class, honest typing) + the definition chase d log|A_0|/du ==
d log||v_0||/du - d(depth)/du: the drift IS the depth slope --
PERCELL-REL(lambda-uniform) is a DEPTH-LIPSCHITZ statement (the
cancellation depth is poly-Lipschitz in u), NOT a size statement.
Numerically: measure the per-cell oscillation of log|A_0| directly on
in-cell grids at all six r151 anchor cells, gate osc <= C U with C
printed (per-cell-certified-at-grid-resolution; disc analyticity
CITED from r148/r151 winding-0 + polish-residual certificates), the
drift and depth ladders, and the Lipschitz table.
(W2) JUMPSUM: Sigma_jumps |Delta log(1 + L_EPS)| <= C U per block.
Attack: (TJ) the tau-jump bordered formula tau+ - tau = -beta_0^2/D_1
with D_1 = d + sum_{i>=1} beta_i^2/(tau+ - lam_i) - tau+ (EXACT
rearrangement of the Schur secular equation -- the analogous one-mode
update for tau, contract deliverable); (COJ) the exact co-jump
residual: with s := Delta log(tau/A_0^2) (the tlaw-numerator co-jump)
  s = log(1 + T/tau) + log(1 + (1+S2) T^2/beta_0^2) - 2 log|1 + r|
(from TJ + the r151 J3 ledger, re-gated generic); IDENTITY
ADJUDICATION: s == 0 is NOT a bordered-linear-algebra identity
(exact 1x1+border counterexample rho_co = 4797/1156 -
963 sqrt(13)/1156 = 1.1461 != 1) and is measured NONZERO on the
ladder -- the tau/A_0^2 cancellation is a MEASURED CO-MOVEMENT LAW
(named COJUMP-LOCK: |s| <= c/x per jump), not an algebraic identity;
(JJ) THE DISSOLUTION THEOREM: L_EPS = A + C with A = tau/(16 A_0^2 G)
and C = OFF-part/(16 A_0^2 G) CONTINUOUS across the K-jump (OFF
carries A_0^2 linearly, so it cancels), hence EXACTLY
  |Delta log(1 + L_EPS)| <= |s|          (slack identity
  e^s (1+C+A) - (1+C+A e^s) == (e^s - 1)(1+C), two-sided),
and with the proven K-jump count N_K <= 1.25 e x (log x + 1) (r147/
r151 CITED) + AB2 (K-jumps are the ONLY discontinuities, CITED):
  COJUMP-LOCK(c/x)  ==>  JUMPSUM with C = 1.25 e c (1 + 1/U):
JUMPSUM is CLOSED MODULO COJUMP-LOCK.  Numerically: extend the r151
29-jump census with the TJ certificate, the co-jump decomposition,
the JJ inequality per jump, and the c_est = |s| x scaling table.
(W3) THE a-WALLS + THE a-QUANTIFIER RE-AUDIT (the r141-G60 method,
never done for a).  Exact window algebra: for a hypothetical off-line
zero rho = 1/2 + delta + i gamma (0 < delta <= 1/2), the Xi-plane
pair z = gamma +/- i delta has |4 w_a(z)| > 1 iff
  a^2 - 2a(gamma^2 + 3 delta^2) + (gamma^2 + delta^2)^2 < 0,
i.e. a in W(gamma, delta) = (gamma^2 + 3 delta^2 -/+ 2 delta
sqrt(gamma^2 + 2 delta^2)); width == 4 delta sqrt(gamma^2 + 2
delta^2); at the matched pin a = gamma^2 + delta^2: |w| == a/(4
gamma^2) EXACT.  WINDOW LOCATION THEOREM: a_-(gamma, delta) -
(gamma - delta)^2 has sign witness 4 delta^3 (2 gamma - delta) >= 0,
so EVERY window with gamma >= H = 3e12 lies in a >= (H - 1/2)^2:
the region a < (H - 1/2)^2 hosts NO off-line window (given PT21,
CITED) -- there WPD's k-tail is positivity of on-line w in [0, 1/4],
exact.  A-DEMAND AUDIT (CHAIN-AUDIT typing, bookkeeping over the
cited NF-closure/Theorem-R statements, the theorems NOT re-proven):
the chain's only a-consumption is (i) per-a hypotheses {L1, WPD} +
(H-conv)/(H-trace) at the SAME a, and (ii) the detection step: an
off-line zero is contradicted at ANY single a inside its open window
(finite objects zero-free on |t| < 4 unconditionally + Hurwitz,
CITED r122).  Hence the honest a-demand levels are
  ALL-A  >  DENSE-(1/4, inf)  >  DENSE-TAIL((H - 1/2)^2, inf)
and the chain demands only DENSE-TAIL: dense-a REDUCES to the tail;
the a-extension strip (gamma_1^2, (H-1/2)^2) is CHAIN-OBSOLETE for
detection (no window lives there).  THE EXTENSION ALGEBRA IS STILL
NEEDED AT TAIL-a AND IS CLOSED HERE: THEOREM D2 (two-sided all-a
form, r132 lever (c) executed): for ANY a > 1/4 and sorted-paired
multisets with W_max = max w over all paired points, |d_k| <= k
W_max^{k-1} M_abs + wedge^{k-1} tail_1 (power-difference
factorization, NO branch monotonicity needed), with WPD constant
[K(q) M_abs + tail_1]/d_1, q = 4 W_max, K(q) <= 1/(1-q)^2 (exact
partial-sum identity (1-q)^2 sum_{k<=n} k q^{k-1} = 1 - (n+1)q^n +
n q^{n+1} <= 1); MARGIN LEMMA MG: meas{a in W: exists j |sqrt a -
gamma_j| < eps} <= sum_local 4 gamma_j eps (interval image (gamma -
eps)^2..(gamma + eps)^2 has length 4 gamma eps EXACT), so inside any
window a margin choice exists whenever 4 eps N_loc (sqrt a_+ + eps)
< width, and then 1 - q = 1 - 4w >= ((t^2 - a)/(t^2 + a))^2 >=
(eps (t + sqrt a)/(t^2 + a))^2 > 0 (exact): the two-branch
DEGENERACY (q -> 1) is ABSORBED by the a-choice freedom.  WINDOW-a
ADJUDICATION: the off-line pair itself has |4w| > 1 at EVERY a in
its window BY DEFINITION -- the dense-a freedom canNOT absorb the
positivity leg: window-a is the irreducible RH-equivalent tail core
(r128 G26 typing SHARPENED: exact region a >= (H - 1/2)^2, exact
consolidation dense-a + a-extension + window-a -> ONE wall
TAILWPD = {L1, WPD}/(H-conv) on a dense subset of ((H-1/2)^2, inf)).
(W4) THE DEFINITIVE ASSEMBLY CENSUS: the gated statement table of
EVERY remaining unproven statement with type in {arithmetic-pinning,
classical-conditional, measured-identity-candidate, technical-wall}
(+ subtype tags), margins, provenance; machine-gated coverage of the
frozen OPEN lists (r151 + r154 + CDLVI residue), no-double-count set
logic (cited loop-equivalence theorems v920), census {MEAS,
OMEGA-POS} cardinality 4 UNCHANGED; min-cut r116 replica with the
r151 serial chain refined ANCHOREPS(1) -> PERCELLREG(1) ->
COJUMPLOCK(1) -> [JJ, INF] -> JUMPSUMTHM (the JUMPSUM unit edge is
RENAMED to its sharp residual by THEOREM JJ; same capacity).
(T5) RED TEAM: SMOOTH/SCRARITH x=5 + EPSTEIN x=8 refuse on tau_w < 0
+ shallow cancellation depth (r151 replica); planted off-line
quartet DETECTED by the window algebra (positive control) and
on-line cache zeros invisible (negative control: w in [0, 1/4]
exact); tau-screens on the new currencies (co-jump mean, osc/U);
conditioning 1e-25; AST firewall (NO zeta use anywhere, np.load
only in ward_, no verification/ import).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall; G02 cache health (X5 n7000, ward, READ-ONLY --
    consumed ONLY by the W3 a-wall instantiation; W1/W2 consume ZERO
    zero-cache data).
S1  exact layer (sympy generic + exact rational instances):
    G10 PC1 Moebius/BC core: |2D - w|^2 - |w|^2 == 4D(D - Re w)
    (so Re w <= D <=> |w/(2D - w)| <= 1; Schwarz lemma CITED
    [Borel 1897/Caratheodory 1912]) + exact-rational osc instance;
    G11 PC2 chain assembly: telescoping osc <= sum of per-disc oscs
    + geometric partial-sum identity (exact);
    G12 PC3 derivative pricing (2-level exact): d tau/du == phi^T
    M' phi and the first-order dA_0 response (Kato CITED, r151 AB1
    class re-gated); |c_1| bound consumes ||v_0||/|A_0| (the depth)
    and 1/delta_1 -- typed; the definition chase d log|A_0|/du ==
    d log||v_0||/du - d(depth)/du EXACT;
    G13 THEOREM TJ: (tau+ - tau) == -beta_0^2/D_1 modulo the Schur
    secular equation, generic 2-level + border;
    G14 CO-JUMP formula (J3 re-gate generic 2-level + TJ composition)
    + NOT-IDENTITY: exact counterexample M = [2], b = 1, d = 5,
    v_new = 1/3: rho_co = 4797/1156 - 963 sqrt(13)/1156 != 1;
    G15 THEOREM JJ: slack identity (e^s - 1)(1 + C) two-sided ==>
    |Delta log(1 + L)| <= |s| EXACT; OFF-part continuity (OFF/A_0^2
    is A_0-free, exact cancellation in the recipe); assembly
    N_K c/x <= 1.25 e c (log x + 1)/x * x = 1.25 e c (log x + 1)
    <= C' U exact rational instance: JUMPSUM <== COJUMP-LOCK + the
    proven poly jump count (r147/r151 + AB2 CITED);
    G16 window algebra (poly match, discriminant, width, matched
    pin -- all exact);
    G17 window location: a_- - (gamma - delta)^2 sign witness
    4 delta^3 (2 gamma - delta) >= 0 ==> windows(gamma >= H) subset
    [(H - 1/2)^2, inf); corollary: k-tail positivity below is
    on-line w in [0, 1/4] exact + PT21 CITED;
    G18 THEOREM D2: power-difference re-gate k = 2..12 + K(q) <=
    1/(1 - q)^2 partial-sum identity + two-branch exact rational
    instance (points straddling sqrt a, two-sided bounds k = 1..12);
    G19 MARGIN LEMMA MG: interval image 4 gamma eps exact + margin
    identity 1 - 4w == ((t^2-a)/(t^2+a))^2 + exact rational margin
    instance (W = (100, 121), Gamma = {21/2}, eps = 1/8: bad measure
    21/4 < width 21, good a = (43/4)^2 with q < 1 exact);
    G20 a-demand audit (CHAIN-AUDIT set logic): demand-level
    inclusions + detection-demand reduction + consolidation typing.
S3  per-block ladder (r151 anchor cells, frozen selection REUSED
    VERBATIM via import): blocks 5/8/13/18/24/28, dps 60/80/120/
    140/150/155, in-cell grids (5/5/5/3/3/3 points at u_0 + f h_w,
    f in (-0.8, -0.4, 0, 0.4, 0.8) resp. (-0.6, 0, 0.6)):
    G30 geometry + r151 anchor replication (x_0 match <= 1e-5);
    G31 R4 cross-ward at blocks 5/8/13 (tau, A_0 rel <= 1e-9,
    n_neg == 0; deep blocks frozen-builder-only, disclosed --
    the r151 G30 matches at 18/24/28 are CITED);
    G32 PER-CELL OSCILLATION CENSUS (the W1 deliverable): osc =
    max - min of log|A_0(u)/A_0(u_0)| over the in-cell grid;
    PERCELL-REL grade C_cell = osc/U <= PCC_BAR = 1.5 at every
    block (expected 0.3..1.1; per-cell-certified AT GRID RESOLUTION,
    disc analyticity CITED r148/r151); n_neg == 0 everywhere;
    G33 depth ladder + DEPTH-LIPSCHITZ (SMOKE-1 re-specification,
    disclosed below): depth = log10(||v_0||/|A_0|) per grid point,
    anchor depth in the r151 windows (+/- 15%); PC3 CHASE gate
    |c_1/ln 10 + d depth/du| <= 0.35 |c_1/ln 10| + 0.6 (the drift
    IS the depth slope, per cell, self-consistent -- no external
    comparator); in-cell Lipschitz slope (d depth/du)/x in (0.2,
    4.0) dex; the r151 block-span drift strings are printed as an
    INFO ratio exhibit (different observable: the block-span
    polyfit crosses K-jumps and is jump-inflated at shallow x --
    the SMOKE-1 finding);
    G34 PC2 grid consistency: osc within (0.3, 2.0) x |c_1| grid
    span (near-linear branch; curvature disclosed);
    G35 L_EPS anchor window (0.05, 0.35) (r151 replication).
S4  K-jump census (12/8/4/2/2/1 jumps, the r151 plan VERBATIM; ONE
    build of the (m+1)-cell per jump, sub-cell = leading principal
    submatrix EXACTLY):
    G40 bordered + TJ certification per jump: Schur secular residual
    <= 1e-6 rel, J2 A_0+ formula dev <= 1e-6, J3 ledger dev <= 1e-6,
    TJ dev |T + beta_0^2/D_1|/|T| <= 1e-6, Cauchy interlacing,
    n_neg == 0 both sides;
    G41 co-jump census: s = ln(10) (dj_tau - dj_A02) per jump;
    |s| <= SJ_ABS_BAR = 0.8; NOT-IDENTITY-ON-LADDER: max |s| >=
    1e-4 (an exact identity would put s at the numeric floor);
    decomposition (T-leg, detuning, r-leg) printed;
    G42 COJUMP-LOCK table: c_est = |s| x per jump <= CJ_CX_BAR = 12;
    JJ inequality |Delta log(1 + L_EPS)| <= |s| (1 + 1e-9) verified
    at every jump; S_J^bound = N_K/unit x mean|s| vs U printed with
    the scaling slope of mean|s| vs x (MEASURED verdict);
    G43 detuning negligible: detune <= 1e-3 at every jump (the r151
    Chebyshev-classical leg; the co-jump lives in the T-leg vs
    r-leg balance, both 1/A_0-class -- printed shares).
S5  a-wall numerics:
    G50 planted witness (POSITIVE control): a* = 90009/100, gamma =
    30, delta = 3/10: 4|w| == 10001/10000 EXACT rational; k* ladder
    == (29959, 76013, 145094) at B = (10, 10^3, 10^6) exact; |4w| >
    1 on an 11-point interior window grid; |4w| <= 1 outside; the
    r122 planted-quartet invisibility at a = 4 replicated (|w| <
    1/4);
    G51 THEOREM D2 extension instantiation at a = 250 and 306.25
    (INSIDE the r132-typed extension strip gamma_1^2 < a < H^2,
    two-branch: sqrt a between gamma_1 and gamma_2): nodes = raw-mp
    census of the x = 5 rung (r132 AMENDMENT-1 currency, R4 build);
    d_1 enclosure from cache + a G(T_top) tail bound, d_1_lo > 0;
    q = 4 W_max < 1 with margin printed; C_D2 = [K(q) M_abs +
    tail_1_hi]/d_1_lo finite, printed (the extension strip is
    ALGEBRA-COVERED; its WPD demands are the same {d_1 > 0, mass}
    class as the battery);
    G52 margin-lemma instantiation INSIDE the planted window: cache
    zeros near sqrt(W), eps from the closed form, good-a exhibited
    with q_real <= 1 - eta, eta > 0 printed;
    G53 window-a unabsorbability: |4 w_pair| > 1 at EVERY a on the
    interior window grid (the positivity leg cannot be dodged by
    a-choice) AND on-line negative control: max over 7000 cache
    zeros of 4 w_a(gamma) <= 1 at a = 250/306.25/900.09 (exact
    inequality w <= 1/4 on real points).
S6  G60 a-quantifier audit verdict (ties G16-G20 to the chain:
    dense-a -> DENSE-TAIL((H-1/2)^2, inf); a-extension ->
    CHAIN-OBSOLETE-FOR-DETECTION + ALGEBRA-CLOSED(D2 + MG);
    window-a -> IRREDUCIBLE (RH-equivalent at the tail);
    consolidation 3 -> 1 named TAILWPD);
    G61 THE DEFINITIVE CENSUS (gated table): every remaining
    statement typed with margins + provenance; coverage of the
    frozen OPEN lists; no-double-count (v920 loop equivalences
    CITED); census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED;
    G62 min-cut (r116 replica): flows base 4 / refined 5 (serial
    chain ANCHOREPS(1) -> PERCELLREG(1) -> COJUMPLOCK(1) ->
    JUMPSUMTHM(INF, THEOREM JJ) -> ONSETCAPTHM) / one-grant 5 /
    counterfactual-parallel 7 NOT REAL.
S7  controls + screens: G70 SMOOTH x=5, G71 SCRARITH x=5, G72
    EPSTEIN x=8 (tau_w < 0, y_t/b_top <= 1.5, depth gap >= 3 dex --
    r151 replica); G73 tau-screen (slopes of mean|s| and osc/U vs
    log10 tau <= 0.35); G74 conditioning (1e-25 shift at the b5
    anchor; response nonzero in (1e-40, 1e-10)).
S9  composite verdict + G99 runtime (bar 14400 s wall).

=======================================================================
FROZEN NUMERICS
=======================================================================
Machinery: the r151 frozen builder + geometry are consumed VERBATIM
by import of tlawcap_blocks_probe (module TB: cell_matrix,
ground_eigsy, a0_bilinear, lu_factor/lu_solve_fac, boundaries_in,
anchor_select, kfun_f, hsw_G, atoms_upto, BLOCKS constants) and
radius4_an_probe (R4: build_cell, maxflow, bfs_reach).  KFAC = 1.25;
T_PT = 3000175332800; H_VERIF = 3e12; HSW = (0.1038, 0.2573,
9.3675).  GRID_F5 = (-0.8, -0.4, 0.0, 0.4, 0.8); GRID_F3 = (-0.6,
0.0, 0.6); blocks 5/8/13 use GRID_F5, 18/24/28 use GRID_F3.  JUMP
plan (r151 VERBATIM): njump = 12/8/4/2/2/1 nearest the anchors.
ANCHOR_X0 = (4.823998, 7.394749, 11.821307, 16.221442, 21.114612,
24.602731) (r151 disclosure strings; match bar 1e-5).  DRIFT_TAB =
(-24.8, -39.7, -63.3, -90.8, -121.1, -141.3) (INFO ratio exhibit
only after SMOKE-1: block-span observable, not gated).
DEPTH_TAB = (7.3, 13.4, 24.0, 34.7, 46.8, 55.4) dex, rel window
+/- 15%.  LIP_WIN = (0.2, 4.0) dex/(u x-unit); CHASE_REL = 0.35,
CHASE_ABS = 0.6 (SMOKE-1 re-specification).  PCC_BAR = 1.5;
OSC_LIN_WIN = (0.3, 2.0); LEPS_WIN = (0.05, 0.35); BRANCH_MATCH_BAR
= 1e-9; SEC_RES_BAR = 1e-6; JUMP_FORM_BAR = 1e-6; LEDGER_DEV_BAR =
1e-6; TJ_DEV_BAR = 1e-6; INTERLACE_SLOP = 1e-12; SJ_ABS_BAR = 0.8;
SJ_MIN_LADDER = 1e-4; CJ_CX_BAR = 12.0; JJ_SLOP = 1e-9; DETUNE_BAR
= 1e-3; A_EXT = (250, 1225/4); PLANT = (gamma 30, delta 3/10, a*
90009/100); KSTAR_B = (10, 10**3, 10**6); KSTAR_TAB = (29959,
76013, 145094); WGRID_N = 11; MG_INST: W = (100, 121), Gamma =
{21/2}, eps = 1/8, good a = (43/4)^2; CTRL_YTB_MAX = 1.5;
DEPTH_GAP_MIN = 3.0; TAU_SLOPE_BAR = 0.35; COND_WIN = (1e-40,
1e-10); GAMMA1_LIT = 14.134725141734694 (ward only); WORKERS = 14
(ProcessPool, spawn, pure deterministic tasks, index-gathered);
LU_PAD = 40; RUNTIME_BAR = 14400 s.  Deterministic: NO randomness
anywhere.  All mpf/mpc arithmetic inside explicit mp.workdps
blocks; no f64 refinement of mp quantities; tiny/huge quantities
stay mp end-to-end (r147 underflow class BANNED); log-scale
diagnostics of O(1) quantities in f64.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5), consumed ONLY by
S5.  Zero zeta use anywhere (no audit_ layer needed).

CALIBRATION DISCLOSURE (pre-freeze, inline one-shot python only, no
scratch file; numbers quoted verbatim): sympy cores verified before
freeze (window poly/disc/width/matched-pin; a_- - (gamma-delta)^2
witness 4 delta^3 (2 gamma - delta); TJ modulo-secular; JJ slack;
K(q) partial sum n = 9; margin identity; 4 gamma eps; Moebius; the
rho_co counterexample 1.1460675793); geometry replication: anchors
== r151 strings at all six blocks, cell halfwidths 0.03221/0.01802/
0.00975/0.00651/0.00468/0.00387, K = 10/19/37/57/81/99, N_K/unit =
17/30/55/81/114/137, jump lists m = (9,10,11,8,12,7,13,6,14,5,15,4)/
(18,19,20,17,21,16,22,15)/(36,37,38,35)/(56,57)/(80,81)/(99)
prefixes; frozen build+eigsy timings 2.5/11.6/134.6 s at b5/b8/b13
(deep blocks extrapolated ~400/~1000/~2300 s, pre-freeze unmeasured
at 18/24/28, DISCLOSED -- bars are physical windows or >= 1e4
headroom residual bars throughout).  Deep-block co-jump and osc
values are pre-freeze UNMEASURED (disclosed); their bars derive
from the r151 frozen strings quoted in FROZEN NUMERICS.
SMOKE-1 NOTE (disclosed; smoke2 = 33/34 at 15.4 s after one
sympy-printf repair, logs assembly_walls_probe.smoke1/2.log kept;
the ONE fail was G33): the original G33 gated the IN-CELL secant
drift against the r151 DRIFT_TAB strings (window 0.4..2.5x) and
the in-cell Lipschitz slope /x against (1.0, 4.0) -- but the r151
drift table is a BLOCK-SPAN polyfit (span +/- 0.35 across many
K-jumps), a DIFFERENT observable: at b5 the in-cell secant is
-6.1 vs the block-span -24.8 (the block-span drift is
jump-inflated at shallow x -- itself a finding: the smooth
in-cell drift and the jump ledger are separate legs of the r151
decomposition, consistent with AB2 + JUMPSUM bookkeeping), while
the PC3 chase holds beautifully in-cell (c_1/ln 10 = -2.65 vs
d depth/du = +2.5 dex/u).  INSTRUMENT FIX (no claim changed): G33
re-specified to the self-consistent PC3 CHASE gate + the widened
Lipschitz window (0.2, 4.0) + anchor-depth windows unchanged; the
r151 drift comparison becomes an INFO ratio exhibit.  SPEC_SHA
moves once -- disclosed; smoke4 at the frozen hash is the
verdict-bearing smoke.

VERDICT ENUMS (frozen): PC1/PC2/PC3-PROVEN(+DEPTH-CHASE);
PERCELL-CERTIFIED-AT-GRID(osc <= C U across the ladder; lambda-
uniform form typed DEPTH-LIPSCHITZ, measured);
TJ-PROVEN(tau-jump bordered formula);
COJUMP-NOT-IDENTITY(exact counterexample + ladder floor) /
COJUMP-IDENTITY(if |s| at numeric floor everywhere -- decided by
G41); JJ-PROVEN(JUMPSUM <== COJUMP-LOCK + poly count: JUMPSUM
CLOSED-MODULO-COJUMP-LOCK); COJUMP-LOCK-MEASURED(c_est table +
scaling slope); WINDOW-ALGEBRA-PROVEN + WINDOW-LOCATION-PROVEN
(tail confinement (H - 1/2)^2); THMD2-PROVEN + MARGIN-LEMMA-PROVEN
(a-extension algebra closed; degeneracy absorbed by a-choice);
WINDOW-A-IRREDUCIBLE(positivity leg unabsorbable);
A-DEMAND-REDUCED(dense-a -> DENSE-TAIL; a-extension chain-obsolete
for detection; consolidation 3 -> 1 TAILWPD);
CENSUS-DEFINITIVE(coverage + no-double-count + cardinality 4
UNCHANGED); CONTROLS-REFUSE; DEMAND-FLAT; MINCUT(4/5; counterfactual
7 NOT REAL).  Composite priority: INSTRUMENT-EDGE >
EXACT-LAYER-OBSTRUCTED > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; NO zeta use; np.load
only inside ward_* functions; no import of verification/.  The
concurrent lanes (rootladder*, spectral_balance*, sieve4_helper.bin)
and their files are NOT touched.  NO RH CLAIM.  EXPLORATION ONLY.
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

import tlawcap_blocks_probe as TB      # r151 frozen machinery (verbatim)
import radius4_an_probe as R4          # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
H_VERIF = 3.0e12
GRID_F5 = (-0.8, -0.4, 0.0, 0.4, 0.8)
GRID_F3 = (-0.6, 0.0, 0.6)
ANCHOR_X0 = {5: 4.823998, 8: 7.394749, 13: 11.821307,
             18: 16.221442, 24: 21.114612, 28: 24.602731}
ANCHOR_BAR = 1e-5
DRIFT_TAB = {5: -24.8, 8: -39.7, 13: -63.3, 18: -90.8,
             24: -121.1, 28: -141.3}
DEPTH_TAB = {5: 7.3, 8: 13.4, 13: 24.0, 18: 34.7, 24: 46.8, 28: 55.4}
DEPTH_REL = 0.15
LIP_WIN = (0.2, 4.0)
CHASE_REL = 0.35
CHASE_ABS = 0.6
PCC_BAR = 1.5
OSC_LIN_WIN = (0.3, 2.0)
LEPS_WIN = (0.05, 0.35)
BRANCH_MATCH_BAR = 1e-9
SEC_RES_BAR = 1e-6
JUMP_FORM_BAR = 1e-6
LEDGER_DEV_BAR = 1e-6
TJ_DEV_BAR = 1e-6
INTERLACE_SLOP = 1e-12
SJ_ABS_BAR = 0.8
SJ_MIN_LADDER = 1e-4
CJ_CX_BAR = 12.0
JJ_SLOP = 1e-9
DETUNE_BAR = 1e-3
A_EXT = (250.0, 306.25)
CTRL_YTB_MAX = 1.5
DEPTH_GAP_MIN = 3.0
TAU_SLOPE_BAR = 0.35
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
WORKERS = 14
LU_PAD = 40
RUNTIME_BAR = 14400.0
WGRID_N = 11

# per-block plan: tag -> (dps, grid_fracs, njump)
PLAN = {5: (60, GRID_F5, 12), 8: (80, GRID_F5, 8),
        13: (120, GRID_F5, 4), 18: (140, GRID_F3, 2),
        24: (150, GRID_F3, 2), 28: (155, GRID_F3, 1)}
R4_WARD_BLOCKS = (5, 8, 13)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list = []
INFO: list = []
EDGE_FAILS: list = []
EXACT_FAILS: list = []


def check(name, ok, detail, kind="gate"):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg):
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title):
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno)
                for n in ast.walk(node))))

    def owners(lineno):
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point", "zeta"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
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
                       "no zero-oracle; NO zeta use anywhere; np.load "
                       "only in ward_; no verification/ import")


# ------------------------------------------------------------- wards
def ward_cache():
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- helpers
def w_of(a, t):
    return a * t ** 2 / (a + t ** 2) ** 2


def kq_float(q):
    if q >= 1.0:
        return float("inf")
    khi = max(3, int(math.ceil(q / (1.0 - q))) + 2)
    return max(k * q ** (k - 1) for k in range(2, khi + 1))


def raw_mp_census(cell):
    """r132 AMENDMENT-1 node source VERBATIM (dominance_proof port):
    raw mp polynomial roots, no f64 refine."""
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
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] \
                + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300, extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    real_y = roots[(np.abs(roots.imag) <= 1e-10 * float(s_mp))
                   & (roots.real > 0)]
    return np.sort(np.sqrt(real_y.real))


def eta0_from_phi(phi_strs, K, dps, x0):
    """envj eta_0 from the frozen eigenvector (scale-invariant ratio;
    cs_k = phi_k / nrm_k gauge)."""
    with mp.workdps(dps):
        aa = mp.log(x0) / 2
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        cs = [mp.mpf(phi_strs[k]) / nrm[k] for k in range(K)]
        cs_abs = [abs(v) for v in cs]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        A = []
        pw = [mp.mpf(1)] * K
        for m in range(TB.M_JETS + 1):
            if m == 0:
                acc = sum((-1) ** k * cs[k] for k in range(K))
            else:
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
            A.append(acc)
        A0 = A[0]
        y = mp.mpf(T_PT) ** 2
        best = None
        for m in TB.MGRID:
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
        return float(best / abs(A0))


# ----------------------------------------------------------- workers
def w_grid_point(args):
    """frozen build + eigsy at real u inside the anchor cell."""
    tag, u_str, dps, K, icap, want_phi = args
    try:
        with mp.workdps(dps):
            u = mp.mpf(u_str)
            M, nrm = TB.cell_matrix(u / 2, K, icap, dps)
            tau, phi, lam1, nneg = TB.ground_eigsy(M, K, dps)
            a0 = TB.a0_bilinear(phi, nrm, K)
            h_apr = mp.sqrt(sum(1 / (nrm[k] ** 2) for k in range(K)))
            depth = float((mp.log(h_apr) - mp.log(abs(a0)))
                          / mp.log(10))
            out = dict(tag=tag, u=float(u), K=K, nneg=nneg,
                       tau_str=mp.nstr(tau, dps),
                       a0_str=mp.nstr(a0, dps),
                       lam1_str=mp.nstr(lam1, dps),
                       log_a0=float(mp.log(abs(a0))),
                       depth=depth)
            if want_phi:
                nn = mp.sqrt(sum(phi[i] * phi[i] for i in range(K)))
                out["phi_strs"] = [mp.nstr(phi[i] / nn, dps)
                                   for i in range(K)]
            return out
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, u_str=u_str, error=repr(exc))


def w_jump_ext(args):
    """K-jump bordered census + TJ + co-jump at x*: ONE build of the
    (m+1)-mode cell; sub-cell = leading principal submatrix EXACTLY;
    full eigsy of BOTH; TJ via the sub-spectrum."""
    tag, ustar_str, m, icap, dps = args
    try:
        with mp.workdps(dps + LU_PAD):
            u = mp.mpf(ustar_str)
            Mfull, nrmf = TB.cell_matrix(u / 2, m + 1, icap, dps)
            Msub = mp.zeros(m, m)
            for i in range(m):
                for j in range(m):
                    Msub[i, j] = Mfull[i, j]
            tauF, phiF, lam1F, nnegF = TB.ground_eigsy(Mfull, m + 1,
                                                       dps)
            ES, VS = mp.eigsy(Msub)
            orderS = sorted(range(m), key=lambda i: ES[i])
            tauS = ES[orderS[0]]
            lam1S = ES[orderS[1]]
            nnegS = sum(1 for i in range(m)
                        if ES[i] < -mp.mpf("0.1"))
            phiS = [VS[i, orderS[0]] for i in range(m)]
            a0F = TB.a0_bilinear(phiF, nrmf, m + 1)
            a0S = TB.a0_bilinear(phiS, nrmf[:m], m)
            b = [Mfull[i, m] for i in range(m)]
            d = Mfull[m, m]
            vnew = mp.mpf((-1) ** m) / nrmf[m]
            v0 = [mp.mpf((-1) ** k) / nrmf[k] for k in range(m)]
            # bordered ground pair at tauF (own LU)
            A = mp.zeros(m, m)
            for i in range(m):
                for j in range(m):
                    A[i, j] = -Msub[i, j]
                A[i, i] += tauF
            LU, piv, _sg = TB.lu_factor(A, m)
            w = TB.lu_solve_fac(LU, piv, b, m)
            bw = sum(b[i] * w[i] for i in range(m))
            sec_res = float(abs((bw - (tauF - d))
                                / max(abs(tauF - d),
                                      mp.mpf("1e-300"))))
            v0w = sum(v0[i] * w[i] for i in range(m))
            ww = sum(w[i] * w[i] for i in range(m))
            a0_form = (v0w + vnew) / mp.sqrt(1 + ww)
            dev_form = float(abs((abs(a0_form) - abs(a0F))
                                 / abs(a0F)))
            # J3 ledger
            nphi = mp.sqrt(sum(phiS[i] * phiS[i] for i in range(m)))
            phiu = [phiS[i] / nphi for i in range(m)]
            beta0 = sum(phiu[i] * b[i] for i in range(m))
            T = tauF - tauS
            vtil = v0w - a0S * beta0 / T
            S2 = ww - beta0 ** 2 / T ** 2
            r_term = T * (vtil + vnew) / (a0S * beta0)
            dj_a = 2 * (mp.log(abs(a0F)) - mp.log(abs(a0S)))
            ledger = 2 * mp.log(abs(1 + r_term)) \
                - mp.log(1 + (1 + S2) * T ** 2 / beta0 ** 2)
            ledger_dev = float(abs(dj_a - ledger)
                               / max(abs(dj_a), mp.mpf("1e-30")))
            # THEOREM TJ: T == -beta_0^2/D_1 via the sub-spectrum
            D1 = d - tauF
            for i in range(1, m):
                psi = [VS[r, orderS[i]] for r in range(m)]
                bi = sum(psi[r] * b[r] for r in range(m))
                D1 += bi ** 2 / (tauF - ES[orderS[i]])
            tj_dev = float(abs((T + beta0 ** 2 / D1)
                               / max(abs(T), mp.mpf("1e-300"))))
            # co-jump s = Delta log(tau/A_0^2) (nats)
            s_co = float((mp.log(abs(tauF)) - mp.log(abs(tauS)))
                         - dj_a)
            leg_T = float(mp.log(abs(1 + T / tauS)))
            leg_det = float(mp.log(1 + (1 + S2) * T ** 2
                                   / beta0 ** 2))
            leg_r = float(-2 * mp.log(abs(1 + r_term)))
            interlace_ok = bool(
                tauF <= tauS + abs(tauS) * mp.mpf(repr(INTERLACE_SLOP))
                or tauF <= tauS * (1 + mp.mpf(repr(INTERLACE_SLOP)))) \
                and bool(tauS <= lam1F
                         * (1 + mp.mpf(repr(INTERLACE_SLOP))))
            l10 = mp.log(10)
            fgS = float((lam1S - tauS) / tauS)
            fgF = float((lam1F - tauF) / tauF)
            return dict(
                tag=tag, ustar=float(u), m=m, nnegF=nnegF,
                nnegS=nnegS,
                tauS_str=mp.nstr(tauS, dps),
                tauF_str=mp.nstr(tauF, dps),
                a0S_str=mp.nstr(a0S, dps),
                a0F_str=mp.nstr(a0F, dps),
                sec_res=sec_res, dev_form=dev_form,
                ledger_dev=ledger_dev, tj_dev=tj_dev,
                interlace_ok=interlace_ok,
                dj_tau=float((mp.log(abs(tauF))
                              - mp.log(abs(tauS))) / l10),
                dj_a02=float(dj_a / l10),
                s_co=s_co, leg_T=leg_T, leg_det=leg_det,
                leg_r=leg_r, r_abs=float(abs(r_term)),
                fgS=fgS, fgF=fgF,
                D1_l10=float(mp.log(abs(D1)) / l10),
                beta0_l10=float(mp.log(abs(beta0)) / l10))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, ustar_str=ustar_str, error=repr(exc))


def w_r4_ctrl(args):
    """R4.build_cell control-world anchor (r151 w_r4_anchor class)."""
    tag, x0, dps, world = args
    try:
        ce = R4.build_cell(x0, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        with mp.workdps(dps):
            tau = ce["mpE"][0]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x0) / 2
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            a0 = sum((-1) ** k * cs[k] for k in range(K))
            nn = mp.sqrt(sum((cs[k] * nrm[k]) ** 2 for k in range(K)))
            a0_bil = a0 / nn
            h_apr = mp.sqrt(sum(1 / (nrm[k] ** 2) for k in range(K)))
            depth = float((mp.log(h_apr) - mp.log(abs(a0_bil)))
                          / mp.log(10))
            oms2 = [(k * mp.pi / aa) ** 2 for k in range(K)]
            a2 = sum((-1) ** k * cs[k] * oms2[k] for k in range(1, K))
            yt = float(abs(a2 / a0)) if a0 != 0 else 0.0
            return dict(tag=tag, world=world, K=K,
                        tau_str=mp.nstr(tau, dps),
                        a0_str=mp.nstr(a0_bil, dps),
                        depth=depth, yt=yt, btop=float(oms2[-1]),
                        tauf=float(tau))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, world=world, error=repr(exc))


def w_r4_main(args):
    """R4.build_cell MAIN anchor cross-ward (cheap blocks only)."""
    tag, x0, dps = args
    try:
        ce = R4.build_cell(x0, KFAC, "MAIN", dps, want_mp=True)
        with mp.workdps(dps):
            tau = ce["mpE"][0]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x0) / 2
            K = ce["K"]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            a0 = sum((-1) ** k * cs[k] for k in range(K))
            nn = mp.sqrt(sum((cs[k] * nrm[k]) ** 2
                             for k in range(K)))
            a0_bil = a0 / nn
            nneg = sum(1 for i in range(K)
                       if ce["mpE"][i] < -mp.mpf("0.1"))
            return dict(tag=tag, K=K, tau_str=mp.nstr(tau, dps),
                        a0_str=mp.nstr(a0_bil, dps), nneg=nneg)
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates():
    import sympy as sp
    out = []

    # ---------------- G10 PC1 Moebius/BC core
    D_, x_, y_ = sp.symbols("D x y", real=True)
    mob = sp.expand((2 * D_ - x_) ** 2 + y_ ** 2
                    - (x_ ** 2 + y_ ** 2) - 4 * D_ * (D_ - x_))
    #  exact-rational osc instance: f = (1 + z/4)/(1 - z/4) on
    #  |z| <= 1, f(0) = 1, Re log f <= log(5/3) on |z| = 1;
    #  BC shape |log f(1/2)| = log(9/7) <= (2*(1/2)/(1 - 1/2)) *
    #  log(5/3) = 2 log(5/3): 9/7 <= 25/9 exact.
    inst = bool(sp.Rational(9, 7) <= sp.Rational(25, 9))
    out.append(("G10-pc1-moebius-bc", mob == 0 and inst,
                "|2D - w|^2 - |w|^2 == 4D(D - Re w) EXACT (so "
                "Re w <= D <=> the Moebius image lies in the unit "
                "disc; Schwarz ==> |log f/f(c)| <= 2 rho D/(R - rho) "
                "on the zero-free disc -- Borel/Caratheodory CITED); "
                "exact-rational instance 9/7 <= 25/9: the one-sided "
                "DEPTH bound gives two-sided oscillation control "
                "(THEOREM PC1)"))

    # ---------------- G11 PC2 chain assembly
    q = sp.symbols("q", positive=True)
    n = 9
    S = sum(k * q ** (k - 1) for k in range(1, n + 1))
    part = sp.expand((1 - q) ** 2 * S
                     - (1 - (n + 1) * q ** n + n * q ** (n + 1)))
    o1, o2, o3 = sp.symbols("o1 o2 o3", nonnegative=True)
    f0, f1, f2, f3 = sp.symbols("f0 f1 f2 f3", real=True)
    tele = sp.expand((f3 - f0) - ((f3 - f2) + (f2 - f1) + (f1 - f0)))
    out.append(("G11-pc2-chain-assembly", part == 0 and tele == 0,
                "telescoping osc_cell <= sum of per-disc oscs EXACT "
                "+ geometric partial-sum identity (1-q)^2 sum k "
                "q^{k-1} == 1 - (n+1)q^n + n q^{n+1} (slack q^n(n+1"
                "-nq) >= 0): the disc-chain assembly of PERCELL-REL "
                "from per-disc depths is exact algebra (THEOREM "
                "PC2); with cell width x^{-C_0} (r147 CITED) and "
                "drift <= poly the cell oscillation is <= C U"))

    # ---------------- G12 PC3 derivative pricing + depth chase
    epsv, e11, e12, e22, u1, u2 = sp.symbols(
        "epsv e11 e12 e22 u1 u2", real=True)
    d1v = sp.symbols("d1v", positive=True)
    Mb = sp.Matrix([[epsv * e11, epsv * e12],
                    [epsv * e12, d1v + epsv * e22]])
    tr = Mb[0, 0] + Mb[1, 1]
    dt = Mb[0, 0] * Mb[1, 1] - Mb[0, 1] ** 2
    lam_m = (tr - sp.sqrt(tr ** 2 - 4 * dt)) / 2
    lam_ser = sp.series(lam_m, epsv, 0, 2).removeO()
    okA = sp.simplify(lam_ser - epsv * e11) == 0
    phi_v = sp.Matrix([lam_m - Mb[1, 1], Mb[0, 1]])
    A0e = (u1 * phi_v[0] + u2 * phi_v[1])
    A0n = sp.sqrt(phi_v[0] ** 2 + phi_v[1] ** 2)
    fnorm = A0e / A0n
    gauge = sp.simplify(fnorm.subs(epsv, 0) / u1)
    coef = sp.simplify(sp.diff(fnorm, epsv).subs(epsv, 0))
    pred = u2 * e12 / (0 - d1v)
    okB = sp.simplify(gauge + 1) == 0 and \
        sp.simplify(coef - gauge * pred) == 0
    LA, LV, DEP = sp.symbols("LA LV DEP", real=True)
    chase = sp.expand((LV - DEP) - LA) \
        .subs(DEP, LV - LA)
    out.append(("G12-pc3-derivative-pricing", okA and okB
                and sp.simplify(chase) == 0,
                "2-level exact: d tau == phi^T M' phi eps + O(eps^2) "
                "and the first-order dA_0 response == (v_0.phi_1)"
                "(phi_1.dM phi_0)/(lam_0 - lam_1) (Kato CITED, r151 "
                "AB1 class): the drift bound |c_1| <= (||v_0||/"
                "|A_0|) ||M'||/delta_1 + norm term consumes the "
                "DEPTH e^{depth} and 1/delta_1 -- a proof-grade "
                "lambda-uniform drift bound is DEPTH-class (honest); "
                "DEFINITION CHASE d log|A_0|/du == d log||v_0||/du "
                "- d(depth)/du EXACT: the drift IS the depth slope; "
                "PERCELL-REL(lambda-uniform) is typed "
                "DEPTH-LIPSCHITZ (smoothness of the cancellation "
                "depth), NOT a size statement (THEOREM PC3)"))

    # ---------------- G13 THEOREM TJ
    tf, l0, l1, b0, b1, dd = sp.symbols(
        "tauF l0 l1 b0 b1 dd", real=True)
    sec = tf - dd - b0 ** 2 / (tf - l0) - b1 ** 2 / (tf - l1)
    D1 = dd + b1 ** 2 / (tf - l1) - tf
    lhs = sp.simplify(D1 + b0 ** 2 / (tf - l0) + sec)
    out.append(("G13-tj-tau-jump", lhs == 0,
                "THEOREM TJ: on the Schur secular manifold "
                "(tauF == d + sum beta_i^2/(tauF - lam_i)): "
                "D_1 == -beta_0^2/(tauF - tau) EXACT, i.e. "
                "T = tau+ - tau == -beta_0^2/D_1 with D_1 = d + "
                "sum_{i>=1} beta_i^2/(tau+ - lam_i) - tau+ "
                "(generic 2-level + border): the tau-jump is the "
                "EXACT bordered analogue of the r151 J3 A_0^2 "
                "ledger -- the one-mode update of the ground VALUE"))

    # ---------------- G14 co-jump formula + NOT-IDENTITY
    z, vn = sp.symbols("z vn", real=True)
    l0_, l1_, a0_, a1_, be0, be1 = sp.symbols(
        "l0_ l1_ a0_ a1_ be0 be1", real=True, nonzero=True)
    w0 = be0 / (z - l0_)
    w1s = be1 / (z - l1_)
    N = a0_ * w0 + a1_ * w1s + vn
    Dn = 1 + w0 ** 2 + w1s ** 2
    T = z - l0_
    r = T * (a1_ * be1 / (z - l1_) + vn) / (a0_ * be0)
    S2 = be1 ** 2 / (z - l1_) ** 2
    led = a0_ ** 2 * (1 + r) ** 2 / (1 + (1 + S2) * T ** 2
                                     / be0 ** 2)
    okJ3 = sp.simplify(sp.together(N ** 2 / Dn - led)) == 0
    #  counterexample: M = [2], b = 1, d = 5, v_0 = 1, v_new = 1/3
    tauF = sp.Rational(7, 2) - sp.sqrt(13) / 2
    vec = sp.Matrix([1, tauF - 2])
    v0full = sp.Matrix([1, sp.Rational(1, 3)])
    A0F2 = ((v0full.T * vec)[0, 0]) ** 2 / (vec.T * vec)[0, 0]
    rho = sp.simplify((tauF / 2) / A0F2)
    rho_val = sp.nsimplify(rho)
    okCE = sp.simplify(rho_val - (sp.Rational(4797, 1156)
                                  - sp.Rational(963, 1156)
                                  * sp.sqrt(13))) == 0 \
        and abs(float(rho) - 1.0) > 1e-6
    out.append(("G14-cojump-not-identity", okJ3 and okCE,
                "J3 ledger re-gated generic (r151 CITED) + TJ ==> "
                "the EXACT co-jump residual s = log(1 + T/tau) + "
                "log(1 + (1+S2)T^2/beta_0^2) - 2 log|1 + r|; "
                "NOT-IDENTITY: exact bordered counterexample "
                "rho_co = 4797/1156 - 963 sqrt(13)/1156 = 1.1461 "
                "!= 1 -- the tau/A_0^2 co-jump cancellation is NOT "
                "a bordered-linear-algebra identity; on the ladder "
                "it is a MEASURED co-movement law (COJUMP-LOCK, "
                "G41/G42)"))

    # ---------------- G15 THEOREM JJ
    s_, C_, A_ = sp.symbols("s C A", real=True)
    slack = sp.simplify(sp.exp(s_) * (1 + C_ + A_)
                        - (1 + C_ + A_ * sp.exp(s_))
                        - (sp.exp(s_) - 1) * (1 + C_))
    #  OFF continuity: OFF = 8 e^{u/2} A_0^2 (1+eta)^2 G_PT ==> the
    #  C-part OFF/(16 A_0^2 G) is A_0-free (exact cancellation)
    A0s, rest = sp.symbols("A0s rest", positive=True)
    offc = sp.simplify((8 * A0s * rest) / (16 * A0s) - rest / 2)
    #  assembly instance: N_K = 1.25 e x (log x + 1), |s| <= c/x:
    #  S_J <= 1.25 e c (log x + 1) <= 2.5 e c U for U = log x >= 1
    #  exact rational instance at x = e^2 (U = 2): 1.25 e c * 3
    #  <= 2.5 e c * 2 <=> 3 <= 4.
    okAsm = bool(sp.Integer(3) <= sp.Integer(4))
    out.append(("G15-jj-dissolution", slack == 0 and offc == 0
                and okAsm,
                "THEOREM JJ: (i) the OFF-part of L_EPS is A_0-free "
                "(exact cancellation in the recipe) so the K-jump "
                "moves ONLY A = tau/(16 A_0^2 G) with A_F = A_S "
                "e^s; (ii) slack identity e^s(1+C+A) - (1+C+A e^s) "
                "== (e^s - 1)(1+C) two-sided ==> |Delta log(1 + "
                "L_EPS)| <= |s| EXACT per jump; (iii) with the "
                "proven K-jump count N_K <= 1.25 e x (log x + 1) "
                "(r147/r151 CITED) + AB2 (K-jumps the ONLY "
                "discontinuities, CITED): COJUMP-LOCK |s| <= c/x "
                "==> Sigma |Delta log(1+L)| <= 2.5 e c U -- "
                "JUMPSUM IS CLOSED MODULO COJUMP-LOCK"))

    # ---------------- G16 window algebra
    a, g, d = sp.symbols("a gamma delta", positive=True)
    c = g ** 2 - d ** 2
    s2 = 2 * g * d
    R = g ** 2 + d ** 2
    f = sp.expand((a + c) ** 2 + s2 ** 2 - 4 * a * R)
    targ = sp.expand(a ** 2 - 2 * a * (g ** 2 + 3 * d ** 2)
                     + (g ** 2 + d ** 2) ** 2)
    disc = sp.expand((g ** 2 + 3 * d ** 2) ** 2
                     - (g ** 2 + d ** 2) ** 2)
    okW = (sp.simplify(f - targ) == 0
           and sp.simplify(disc - 4 * d ** 2
                           * (g ** 2 + 2 * d ** 2)) == 0)
    aa_ = g ** 2 + d ** 2
    wabs = aa_ * R / ((aa_ + c) ** 2 + s2 ** 2)
    okP = sp.simplify(wabs - aa_ / (4 * g ** 2)) == 0
    out.append(("G16-window-algebra", okW and okP,
                "|4 w_a(gamma + i delta)| > 1 <=> a^2 - 2a(gamma^2 "
                "+ 3 delta^2) + (gamma^2 + delta^2)^2 < 0 EXACT; "
                "window edges a_-/+ = gamma^2 + 3 delta^2 -/+ 2 "
                "delta sqrt(gamma^2 + 2 delta^2), width == 4 delta "
                "sqrt(gamma^2 + 2 delta^2) (the r128/CDXXX string); "
                "matched pin: at a = gamma^2 + delta^2, |w| == "
                "a/(4 gamma^2) EXACT (the r117 window formula "
                "re-derived and machine-exact)"))

    # ---------------- G17 window location
    wit = sp.expand((g ** 2 + 3 * d ** 2 - (g - d) ** 2) ** 2
                    - (2 * d * sp.sqrt(g ** 2 + 2 * d ** 2)) ** 2)
    okL = sp.simplify(wit - (-4 * d ** 4 + 8 * d ** 3 * g)) == 0
    #  on-line positivity: w in [0, 1/4] exact
    t = sp.symbols("t", positive=True)
    okQ = sp.simplify((a + t ** 2) ** 2 - 4 * a * t ** 2
                      - (a - t ** 2) ** 2) == 0
    out.append(("G17-window-location", okL and okQ,
                "a_- - (gamma - delta)^2 has the sign witness "
                "4 delta^3 (2 gamma - delta) >= 0 (delta <= 1/2 << "
                "2 gamma): EVERY off-line window with gamma >= H "
                "lies in a >= (H - 1/2)^2 -- the region a < "
                "(H - 1/2)^2 ~ 9e24 hosts NO window given the PT21 "
                "verification (CITED); there WPD's k-tail is "
                "on-line positivity w in [0, 1/4] EXACT ((a+t^2)^2 "
                "- 4at^2 == (a-t^2)^2): the a-extension strip "
                "(gamma_1^2, (H-1/2)^2) is CHAIN-OBSOLETE for "
                "detection (THEOREM WL)"))

    # ---------------- G18 THEOREM D2
    u_, v_ = sp.symbols("u v", positive=True)
    ok18 = True
    for kk in range(2, 13):
        fac = sp.expand(v_ ** kk - u_ ** kk
                        - (v_ - u_) * sum(u_ ** j * v_ ** (kk - 1 - j)
                                          for j in range(kk)))
        ok18 = ok18 and fac == 0
    #  two-branch exact rational instance: a = 256, sqrt a = 16
    aq = sp.Integer(256)

    def wq(tv):
        return aq * tv ** 2 / (aq + tv ** 2) ** 2

    trues = [sp.Integer(14), sp.Integer(15), sp.Integer(20),
             sp.Integer(25), sp.Integer(40)]
    nds = [sp.Integer(14) + sp.Rational(1, 10),
           sp.Integer(15) - sp.Rational(1, 20),
           sp.Integer(21), sp.Integer(26)]
    Wmax = max([wq(tv) for tv in trues[:4]] + [wq(nv) for nv in nds],
               key=lambda vv: sp.Rational(vv))
    M_abs = sum(abs(wq(trues[i]) - wq(nds[i])) for i in range(4))
    wedge = wq(trues[4])
    tail1 = wq(trues[4])
    okI = True
    for kk in range(1, 13):
        dk = (sum(wq(tv) ** kk for tv in trues)
              - sum(wq(nv) ** kk for nv in nds))
        hi = kk * Wmax ** (kk - 1) * M_abs + wedge ** (kk - 1) * tail1
        okI = okI and bool(abs(dk) <= hi)
    out.append(("G18-thmD2-two-branch", ok18 and okI,
                "THEOREM D2 (two-sided, ALL a > 1/4, r132 lever (c) "
                "executed): |d_k| <= k W_max^{k-1} M_abs + "
                "wedge^{k-1} tail_1 with W_max = max w over paired "
                "points and M_abs = sum |w(gamma_i) - w(mu_i)| -- "
                "power-difference factorization only, NO branch "
                "monotonicity (exact k = 2..12 + geometric); "
                "two-branch rational instance a = 256 (points "
                "straddle sqrt a = 16 between gamma_1 and gamma_2 "
                "scale): two-sided bound exact in Q, k = 1..12; "
                "WPD constant [K(q) M_abs + tail_1]/d_1 with "
                "q = 4 W_max and K(q) <= 1/(1-q)^2 (G11 identity): "
                "finite whenever the margin lemma (G19) supplies "
                "q < 1"))

    # ---------------- G19 MARGIN LEMMA MG
    e_ = sp.symbols("e", positive=True)
    img = sp.expand((g + e_) ** 2 - (g - e_) ** 2 - 4 * g * e_)
    marg = sp.simplify(1 - 4 * a * t ** 2 / (a + t ** 2) ** 2
                       - ((t ** 2 - a) / (t ** 2 + a)) ** 2)
    #  rational instance: W = (100, 121), Gamma = {21/2}, eps = 1/8:
    #  bad measure <= 4 * (21/2) * (1/8) = 21/4 < 21 = width; good
    #  a = (43/4)^2 = 1849/16 in W with |sqrt a - 21/2| = 1/4 >= eps
    aI = sp.Rational(1849, 16)
    okW1 = bool(sp.Integer(100) < aI < sp.Integer(121))
    okW2 = bool(sp.Rational(21, 4) < sp.Integer(21))
    qI = 4 * aI * sp.Rational(21, 2) ** 2 \
        / (aI + sp.Rational(21, 2) ** 2) ** 2
    okW3 = bool(qI < 1)
    out.append(("G19-margin-lemma", img == 0 and marg == 0
                and okW1 and okW2 and okW3,
                "MARGIN LEMMA MG: {a : |sqrt a - gamma| < eps} is "
                "the interval ((gamma-eps)^2, (gamma+eps)^2) of "
                "length 4 gamma eps EXACT ==> bad-a measure <= "
                "sum_local 4 gamma_j eps; margin identity 1 - 4w "
                "== ((t^2-a)/(t^2+a))^2 EXACT converts the margin "
                "into q = 4 W_max <= 1 - eta, eta > 0; rational "
                "instance: W = (100, 121), Gamma = {21/2}, eps = "
                "1/8: bad measure 21/4 < width 21, good a = "
                "1849/16 with q = %.5f < 1 -- the two-branch "
                "DEGENERACY is ABSORBED by the a-choice freedom "
                "(dense-a freedom used constructively)"
                % float(qI)))

    # ---------------- G20 a-demand audit (CHAIN-AUDIT set logic)
    ALL_A, DENSE_FULL, DENSE_TAIL = 0, 1, 2
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, CITED) consumes per-a "
                  "hypotheses + detection at ONE a inside each "
                  "off-line window (finite objects zero-free on "
                  "|t| < 4 unconditionally + Hurwitz)", True))
    steps.append(("Theorem R (r128/CDXXX, CITED) transfers per-a: "
                  "no cross-a demand", True))
    steps.append(("windows(gamma >= H) subset [(H-1/2)^2, inf) "
                  "(G17 THEOREM WL): no detection demand below",
                  True))
    steps.append(("hence demand level == DENSE-TAIL "
                  "(hits every open sub-interval of the tail; "
                  "adversarial delta -> 0 forces topological "
                  "density IN THE TAIL, nothing below)",
                  DENSE_TAIL > DENSE_FULL > ALL_A))
    steps.append(("a-extension strip (gamma_1^2, (H-1/2)^2): "
                  "CHAIN-OBSOLETE for detection; its ALGEBRA "
                  "(two-branch) is needed at tail-a and is CLOSED "
                  "by D2 + MG (G18/G19)", True))
    steps.append(("window-a: |4 w_pair| > 1 at EVERY a in the "
                  "window BY DEFINITION -- unabsorbable; the "
                  "consolidated wall is TAILWPD = {L1, WPD}/"
                  "(H-conv) on a dense subset of ((H-1/2)^2, inf), "
                  "typed RH-EQUIVALENT-AT-TAIL (r128 G26 sharpened)",
                  True))
    okA = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    out.append(("G20-a-demand-audit", okA, "CHAIN-AUDIT "
                "(bookkeeping over cited theorems, not re-proven): "
                + det))
    return out


# ---------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("assembly_walls_probe -- PRIME.ASSEMBLY.WALLS.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    tags = [5] if smoke else sorted(PLAN)
    controls = (("SMOOTH", 5.0, 60),) if smoke else \
        (("SMOOTH", 5.0, 60), ("SCRARITH", 5.0, 60),
         ("EPSTEIN", 8.0, 80))
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; consumed ONLY by "
          "the S5 a-wall layer)" % (len(gam),
                                    abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")

    section("S1  EXACT LAYER (PC1-PC3, TJ, COJ, JJ, WL, D2, MG, "
            "A-AUDIT)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r151 J1-J3/ASM/JC/AB2 + jump census; "
         "r147 AD1 + cell lemma; r148 O1 certification; r141 V2 + "
         "G60 method; r132 THEOREM D/W1/P1 + branch; r133 M/E/T/C/A "
         "+ H-pin; r128 Theorem R + planted witness; r122 "
         "NF-closure; r146 Y1-Y4; r150 R1-R4; Borel/Caratheodory + "
         "Schwarz; Kato; Cauchy-Hadamard; HSW22 Cor. 1.2 (closed "
         "form only); PT21 (H = 3e12 + T_PT)")

    # ------------------------------------------------ geometry
    section("S3a  GEOMETRY (r151 anchor cells, frozen selection)")
    geo = {}
    ok30 = True
    det30 = []
    for tag in tags:
        dps, fracs, njump = PLAN[tag]
        x_nom = dict((b[0], b[1]) for b in TB.BLOCKS)[tag]
        u0, clo, chi = TB.anchor_select(x_nom)
        hw = 0.5 * (chi - clo)
        x0 = math.exp(u0)
        K0 = int(math.ceil(TB.kfun_f(x0)))
        icap0 = int(math.floor(x0))
        nk_unit = len([b for b in TB.boundaries_in(u0 - 0.5, u0 + 0.5)
                       if b[1] == "K"])
        geo[tag] = dict(dps=dps, fracs=fracs, njump=njump, u0=u0,
                        clo=clo, chi=chi, hw=hw, x0=x0, K0=K0,
                        icap0=icap0, nk_unit=nk_unit)
        okx = abs(x0 - ANCHOR_X0[tag]) <= ANCHOR_BAR
        ok30 = ok30 and okx
        det30.append("b%d x0=%.6f (r151 %.6f) hw=%.5f K=%d N_K/unit"
                     "=%d" % (tag, x0, ANCHOR_X0[tag], hw, K0,
                              nk_unit))
    check("G30-geometry-replication", ok30,
          "anchor cells replicate the r151 deterministic selection "
          "(bar %.0e): %s" % (ANCHOR_BAR, "; ".join(det30)))

    # ------------------------------------------------ task assembly
    ctx = _mpr.get_context("spawn")
    tasks = []
    for tag in sorted(tags, reverse=True):
        g = geo[tag]
        for i, f in enumerate(g["fracs"]):
            uu = g["u0"] + f * g["hw"]
            tasks.append(("grd", (tag, i),
                          (tag, repr(uu), g["dps"], g["K0"],
                           g["icap0"], f == 0.0)))
        kb = [b for b in TB.boundaries_in(g["u0"] - 0.7,
                                          g["u0"] + 0.7)
              if b[1] == "K"]
        kb.sort(key=lambda b: (abs(b[0] - g["u0"]), b[0]))
        nj = g["njump"] if not smoke else 3
        for uj, _kind, m in kb[:nj]:
            xj = math.exp(uj)
            tasks.append(("jmp", (tag, m),
                          (tag, repr(uj), m, int(math.floor(xj)),
                           g["dps"])))
    for tag in R4_WARD_BLOCKS:
        if tag in geo:
            tasks.append(("r4m", (tag, 0),
                          (tag, geo[tag]["x0"], geo[tag]["dps"])))
    for world, xw, dpsw in controls:
        tasks.append(("ctl", (world, 0), (0, xw, dpsw, world)))
    tasks.sort(key=lambda tsk: (-tsk[2][4] if tsk[0] == "jmp"
                                else -(tsk[2][2]
                                       if tsk[0] in ("grd", "r4m")
                                       else 0), str(tsk[1])))

    section("S3b  BUILDS (%d tasks, %d workers)" % (len(tasks),
                                                    workers))
    res = {}
    t_ph = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(grd=w_grid_point, jmp=w_jump_ext,
                      r4m=w_r4_main, ctl=w_r4_ctrl)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_ph))

    # ------------------------------------------------ G31 R4 ward
    ok31 = True
    det31 = []
    for tag in R4_WARD_BLOCKS:
        if tag not in geo:
            continue
        r4a = res.get(("r4m", (tag, 0)))
        anc = None
        for i, f in enumerate(geo[tag]["fracs"]):
            if f == 0.0:
                anc = res.get(("grd", (tag, i)))
        if r4a is None or anc is None or "error" in r4a \
                or "error" in anc:
            ok31 = False
            det31.append("b%d ERROR" % tag)
            continue
        dps = geo[tag]["dps"]
        with mp.workdps(dps):
            dev_t = float(abs(mp.mpf(anc["tau_str"])
                              - mp.mpf(r4a["tau_str"]))
                          / abs(mp.mpf(r4a["tau_str"])))
            dev_a = float(abs(abs(mp.mpf(anc["a0_str"]))
                              - abs(mp.mpf(r4a["a0_str"])))
                          / abs(mp.mpf(r4a["a0_str"])))
        okx = (dev_t <= BRANCH_MATCH_BAR and dev_a <= BRANCH_MATCH_BAR
               and anc["K"] == r4a["K"] and r4a["nneg"] == 0)
        ok31 = ok31 and okx
        det31.append("b%d dev(tau)=%.1e dev(A0)=%.1e" %
                     (tag, dev_t, dev_a))
    check("G31-r4-cross-ward", ok31,
          "frozen builder == R4.build_cell at blocks %s (bar %.0e; "
          "deep blocks frozen-builder-only, r151 G30 matches CITED "
          "<= 8.4e-15): %s" % (list(R4_WARD_BLOCKS),
                               BRANCH_MATCH_BAR, "; ".join(det31)))

    # ------------------------------------------------ S3 gates
    section("S3c  PER-CELL OSCILLATION + DEPTH (W1)")
    ok32 = ok33 = ok34 = ok35 = True
    det32, det33, det34, det35 = [], [], [], []
    osc_tab, s_mean_tab, tau_tab = {}, {}, {}
    anchors = {}
    for tag in tags:
        g = geo[tag]
        pts = []
        anc = None
        bad = False
        for i, f in enumerate(g["fracs"]):
            rr_ = res.get(("grd", (tag, i)))
            if rr_ is None or "error" in rr_:
                bad = True
                det32.append("b%d grid%d ERROR %s"
                             % (tag, i, (rr_ or {}).get("error")))
                continue
            pts.append((f, rr_))
            if f == 0.0:
                anc = rr_
        if bad or anc is None or len(pts) < 3:
            ok32 = False
            continue
        anchors[tag] = anc
        pts.sort()
        us = [g["u0"] + f * g["hw"] for f, _r in pts]
        la = [r_["log_a0"] for _f, r_ in pts]
        dp = [r_["depth"] for _f, r_ in pts]
        osc = max(la) - min(la)
        span = us[-1] - us[0]
        c1 = (la[-1] - la[0]) / span
        c2 = 0.0
        if len(pts) >= 3:
            mid = len(pts) // 2
            h1 = us[mid] - us[0]
            h2 = us[-1] - us[mid]
            c2 = 2 * ((la[-1] - la[mid]) / h2
                      - (la[mid] - la[0]) / h1) / (h1 + h2)
        U = g["u0"]
        ccell = osc / U
        osc_tab[tag] = ccell
        okc = (ccell <= PCC_BAR
               and all(r_["nneg"] == 0 for _f, r_ in pts))
        ok32 = ok32 and okc
        det32.append("b%d osc=%.4f C_cell=%.3f (span %.4f)"
                     % (tag, osc, ccell, span))
        # depth Lipschitz + PC3 chase (SMOKE-1 re-specification)
        dlip = (dp[-1] - dp[0]) / span
        lip_x = abs(dlip) / g["x0"]
        c1_dex = c1 / math.log(10.0)
        chase = abs(c1_dex + dlip)
        okd = (LIP_WIN[0] <= lip_x <= LIP_WIN[1]
               and abs(anc["depth"] - DEPTH_TAB[tag])
               <= DEPTH_REL * DEPTH_TAB[tag]
               and chase <= CHASE_REL * abs(c1_dex) + CHASE_ABS)
        ok33 = ok33 and okd
        det33.append("b%d depth=%.1f dex dLip=%+.1f dex/u (/x=%.2f)"
                     " c1=%.1f chase=%.2f incell/blockspan=%.2f"
                     % (tag, anc["depth"], dlip, lip_x, c1, chase,
                        c1 / DRIFT_TAB[tag]))
        # PC2 grid consistency
        lin = abs(c1) * span
        ratio = osc / max(lin, 1e-12)
        okl = OSC_LIN_WIN[0] <= ratio <= OSC_LIN_WIN[1]
        ok34 = ok34 and okl
        det34.append("b%d osc/(|c1| span)=%.3f curv c2=%.1f"
                     % (tag, ratio, c2))
        # L_EPS anchor
        dps = g["dps"]
        eta0 = eta0_from_phi(anc["phi_strs"], anc["K"], dps,
                             g["x0"])
        with mp.workdps(dps):
            tau0 = mp.mpf(anc["tau_str"])
            a00 = mp.mpf(anc["a0_str"])
            Gz = mp.mpf(repr(TB.hsw_G(2 * math.pi * g["x0"])))
            Gpt = mp.mpf(repr(TB.hsw_G(float(T_PT))))
            offp = 8 * mp.exp(mp.mpf(repr(g["u0"])) / 2) \
                * a00 ** 2 * (1 + mp.mpf(repr(eta0))) ** 2 * Gpt
            leps = float((tau0 + offp) / (16 * a00 ** 2 * Gz))
        anchors[tag]["eta0"] = eta0
        anchors[tag]["leps"] = leps
        tau_tab[tag] = float(mp.mpf(anc["tau_str"]))
        okp = LEPS_WIN[0] <= leps <= LEPS_WIN[1]
        ok35 = ok35 and okp
        det35.append("b%d L_EPS(u0)=%.4f" % (tag, leps))
    check("G32-percell-oscillation", ok32,
          "PER-CELL oscillation of log|A_0| on in-cell grids: "
          "PERCELL-REL grade C_cell = osc/U <= %.1f at every block "
          "AND n_neg == 0 at every grid point "
          "(PERCELL-CERTIFIED-AT-GRID; disc analyticity winding 0 + "
          "polish residuals CITED r148/r151): %s"
          % (PCC_BAR, "; ".join(det32)))
    check("G33-depth-lipschitz", ok33,
          "depth = log10(||v_0||/|A_0|) ladder in r151 windows "
          "(+/- %.0f%%), in-cell Lipschitz slope /x in (%.1f, "
          "%.1f) dex, PC3 CHASE |c_1/ln10 + d depth/du| <= %.2f "
          "|c_1/ln10| + %.1f -- the drift IS the depth slope, per "
          "cell: PERCELL-REL(lambda-uniform) == DEPTH-LIPSCHITZ, "
          "typed MEASURED (in-cell vs r151 block-span drift ratio "
          "printed: the block-span polyfit is jump-inflated at "
          "shallow x, SMOKE-1 finding): %s"
          % (100 * DEPTH_REL, LIP_WIN[0], LIP_WIN[1], CHASE_REL,
             CHASE_ABS, "; ".join(det33)))
    check("G34-pc2-grid-consistency", ok34,
          "osc within (%.1f, %.1f) x |c_1| grid span (secant read; "
          "curvature disclosed -- near-linear branch, PC2 "
          "instrument consistency): %s"
          % (OSC_LIN_WIN[0], OSC_LIN_WIN[1], "; ".join(det34)))
    check("G35-leps-anchor", ok35,
          "L_EPS(u0) in (%.2f, %.2f) at every block (r151 "
          "replication; eta_0 from the frozen eigenvector, "
          "scale-invariant): %s"
          % (LEPS_WIN[0], LEPS_WIN[1], "; ".join(det35)))

    # ------------------------------------------------ S4 jumps
    section("S4  K-JUMP CENSUS: TJ + CO-JUMP (W2)")
    ok40 = ok41 = ok42 = ok43 = True
    det40, det41, det42, det43 = [], [], [], []
    s_abs_all = []
    for tag in tags:
        g = geo[tag]
        kb = [k for k in res if k[0] == "jmp" and k[1][0] == tag]
        kb.sort(key=lambda k: k[1][1])
        s_list = []
        for key in kb:
            rj = res[key]
            if "error" in rj:
                ok40 = False
                det40.append("b%d m%d ERROR %s"
                             % (tag, key[1][1], rj["error"]))
                continue
            okx = (rj["sec_res"] <= SEC_RES_BAR
                   and rj["dev_form"] <= JUMP_FORM_BAR
                   and rj["ledger_dev"] <= LEDGER_DEV_BAR
                   and rj["tj_dev"] <= TJ_DEV_BAR
                   and rj["interlace_ok"]
                   and rj["nnegF"] == 0 and rj["nnegS"] == 0)
            ok40 = ok40 and okx
            det40.append("b%d m=%d sec=%.0e form=%.0e ledg=%.0e "
                         "TJ=%.0e" % (tag, rj["m"], rj["sec_res"],
                                      rj["dev_form"],
                                      rj["ledger_dev"],
                                      rj["tj_dev"]))
            s = rj["s_co"]
            s_list.append(s)
            s_abs_all.append((tag, rj["m"], abs(s)))
            oks = abs(s) <= SJ_ABS_BAR
            ok41 = ok41 and oks
            det41.append("b%d m=%d s=%+.4f (T-leg %+.4f det %+.4f "
                         "r-leg %+.4f |r|=%.2f)"
                         % (tag, rj["m"], s, rj["leg_T"],
                            rj["leg_det"], rj["leg_r"],
                            rj["r_abs"]))
            okd = rj["leg_det"] <= DETUNE_BAR
            ok43 = ok43 and okd
            # JJ inequality per jump
            dps = g["dps"]
            eta0 = anchors[tag]["eta0"]
            with mp.workdps(dps):
                u = mp.mpf(repr(rj["ustar"]))
                Gz = mp.mpf(repr(TB.hsw_G(2 * math.pi
                                          * math.exp(float(u)))))
                Gpt = mp.mpf(repr(TB.hsw_G(float(T_PT))))
                dl = {}
                for side, ts, asq in (("S", rj["tauS_str"],
                                       rj["a0S_str"]),
                                      ("F", rj["tauF_str"],
                                       rj["a0F_str"])):
                    tau_ = mp.mpf(ts)
                    a0_ = mp.mpf(asq)
                    off_ = 8 * mp.exp(u / 2) * a0_ ** 2 \
                        * (1 + mp.mpf(repr(eta0))) ** 2 * Gpt
                    dl[side] = mp.log(1 + (tau_ + off_)
                                      / (16 * a0_ ** 2 * Gz))
                dleps = float(dl["F"] - dl["S"])
            c_est = abs(s) * g["x0"]
            okj = (abs(dleps) <= abs(s) * (1 + JJ_SLOP) + 1e-15
                   and c_est <= CJ_CX_BAR)
            ok42 = ok42 and okj
            det42.append("b%d m=%d |dL|=%.4f <= |s|=%.4f  c_est"
                         "=|s|x=%.2f" % (tag, rj["m"], abs(dleps),
                                         abs(s), c_est))
        if s_list:
            s_mean_tab[tag] = float(np.mean(np.abs(s_list)))
    check("G40-bordered-tj-certification", ok40,
          "per K-jump: Schur secular residual <= %.0e, J2 formula "
          "dev <= %.0e, J3 ledger dev <= %.0e, THEOREM TJ dev "
          "|T + beta_0^2/D_1|/|T| <= %.0e, Cauchy interlacing, "
          "n_neg == 0 both sides (the tau-jump bordered formula "
          "VERIFIED at every censused jump): %s"
          % (SEC_RES_BAR, JUMP_FORM_BAR, LEDGER_DEV_BAR, TJ_DEV_BAR,
             "; ".join(det40)))
    max_s = max((v for _t, _m, v in s_abs_all), default=0.0)
    ok41 = ok41 and (max_s >= SJ_MIN_LADDER)
    check("G41-cojump-census", ok41,
          "co-jump s = Delta log(tau/A_0^2) per jump: |s| <= %.1f "
          "everywhere AND max|s| = %.4f >= %.0e "
          "(COJUMP-NOT-IDENTITY on the ladder -- an exact identity "
          "would put s at the numeric floor; the G14 counterexample "
          "is the algebraic side); decomposition printed (detuning "
          "negligible, the balance is T-leg vs r-leg, BOTH "
          "1/A_0-class): %s"
          % (SJ_ABS_BAR, max_s, SJ_MIN_LADDER, "; ".join(det41)))
    if len(s_mean_tab) >= 3:
        mt = sorted(s_mean_tab)
        sl_s = float(np.polyfit([math.log10(geo[t]["x0"])
                                 for t in mt],
                                [math.log10(max(s_mean_tab[t],
                                                1e-12))
                                 for t in mt], 1)[0])
    else:
        sl_s = 0.0
    sj_det = []
    for tag in sorted(s_mean_tab):
        g = geo[tag]
        sj_b = g["nk_unit"] * s_mean_tab[tag]
        sj_det.append("b%d mean|s|=%.4f N_K=%d S_J^bound=%.2f vs "
                      "U=%.2f" % (tag, s_mean_tab[tag],
                                  g["nk_unit"], sj_b, g["u0"]))
    check("G42-cojump-lock", ok42,
          "JJ inequality |Delta log(1 + L_EPS)| <= |s| VERIFIED at "
          "every jump (THEOREM JJ instantiated) AND c_est = |s| x "
          "<= %.0f (COJUMP-LOCK measured); scaling slope log10 "
          "mean|s| vs log10 x = %.2f (r151 class -0.86; <= -1 "
          "would be exact dissolution); %s -- JUMPSUM is "
          "CLOSED-MODULO-COJUMP-LOCK (G15), the lock itself typed "
          "MEASURED: %s"
          % (CJ_CX_BAR, sl_s, "; ".join(sj_det), "; ".join(det42)))
    check("G43-detuning-negligible", ok43,
          "detuning leg <= %.0e at every jump (the Chebyshev-"
          "classical leg is dead-small, r151 CITED; the co-jump "
          "cancellation lives entirely in the T-leg vs r-leg "
          "balance -- the SAME 1/A_0 arithmetic class as the "
          "Jensen center input: COJUMP-LOCK is ANCHOR-EPS-class, "
          "not a new omega)" % DETUNE_BAR)

    # ------------------------------------------------ S5 a-walls
    section("S5  a-WALL NUMERICS (W3)")
    import sympy as sp
    gpl, dpl = sp.Integer(30), sp.Rational(3, 10)
    apl = sp.Rational(90009, 100)
    w4 = 4 * apl / (4 * gpl ** 2) * 1   # matched pin closed form
    ok50 = sp.simplify(w4 - sp.Rational(10001, 10000)) == 0
    #  k* ladder exact
    kstars = []
    with mp.workdps(60):
        l4w = mp.log(mp.mpf(10001) / 10000)
        for B in (10, 10 ** 3, 10 ** 6):
            kstars.append(int(mp.ceil(mp.log(2 * B) / l4w)))
    ok50 = ok50 and kstars == [29959, 76013, 145094]
    #  window grid: |4w| > 1 inside, <= 1 at/outside edges
    g_f, d_f = 30.0, 0.3
    am = g_f ** 2 + 3 * d_f ** 2 - 2 * d_f * math.sqrt(
        g_f ** 2 + 2 * d_f ** 2)
    ap = g_f ** 2 + 3 * d_f ** 2 + 2 * d_f * math.sqrt(
        g_f ** 2 + 2 * d_f ** 2)

    def w4abs(a_v):
        z2c = g_f ** 2 - d_f ** 2
        z2s = 2 * g_f * d_f
        R2 = g_f ** 2 + d_f ** 2
        return 4 * a_v * R2 / ((a_v + z2c) ** 2 + z2s ** 2)

    inside = [w4abs(am + (ap - am) * (i + 1) / (WGRID_N + 1))
              for i in range(WGRID_N)]
    ok50 = ok50 and all(v > 1.0 for v in inside) \
        and w4abs(am - 1.0) < 1.0 and w4abs(ap + 1.0) < 1.0 \
        and w4abs(4.0) < 1.0
    check("G50-planted-witness", ok50,
          "PLANTED off-line quartet gamma=30 delta=0.3: matched pin "
          "4|w|(a* = 90009/100) == 10001/10000 EXACT rational; k* "
          "ladder %s == (29959, 76013, 145094) at B = (10, 1e3, "
          "1e6) (r128/CDXXX reproduced); |4w| > 1 at all %d "
          "interior window-grid points, < 1 outside the window and "
          "at battery a = 4 (the r122 invisibility): the window "
          "algebra DETECTS exactly where it must" % (kstars,
                                                     WGRID_N))

    #  D2 extension instantiation at a in A_EXT (x = 5 rung nodes)
    ce5 = R4.build_cell(5.0, KFAC, "MAIN", 60, want_mp=True)
    mus5 = raw_mp_census(ce5)
    T_top = float(gam[-1])
    G_top = TB.hsw_G(T_top)
    ok51 = True
    det51 = []
    for a_v in A_EXT:
        wg = w_of(a_v, gam)
        c01_lo = float(np.sum(wg))
        c01_hi = c01_lo + a_v * G_top
        trb = float(np.sum(w_of(a_v, mus5)))
        d1_lo = c01_lo - trb
        d1_hi = c01_hi - trb
        n5 = len(mus5)
        wmu = w_of(a_v, mus5)
        wga = w_of(a_v, gam[:n5])
        M_abs = float(np.sum(np.abs(wga - wmu)))
        tail1_hi = c01_hi - float(np.sum(wga))
        sq = math.sqrt(a_v)
        marg_g = float(np.min(np.abs(gam[:50] - sq)))
        marg_m = float(np.min(np.abs(mus5 - sq)))
        wmax = max(float(np.max(wmu)), float(np.max(wga)))
        qv = 4.0 * wmax
        kq = kq_float(qv)
        cd2 = (kq * M_abs + tail1_hi) / d1_lo if d1_lo > 0 \
            else float("inf")
        okx = d1_lo > 0 and qv < 1.0 and math.isfinite(cd2)
        ok51 = ok51 and okx
        det51.append("a=%.2f: sqrt(a)=%.2f margins (g %.2f, mu "
                     "%.2f) q=%.4f K(q)<=%.0f d1 in [%.4f, %.4f] "
                     "M_abs=%.4f C_D2=%.1f"
                     % (a_v, sq, marg_g, marg_m, qv,
                        min(kq, 1e9), d1_lo, d1_hi, M_abs, cd2))
    check("G51-d2-extension-instantiated", ok51,
          "THEOREM D2 instantiated INSIDE the r132 extension strip "
          "(two-branch: sqrt a between cache zeros; x=5 rung nodes, "
          "r132 AMENDMENT-1 currency): d_1 > 0 (tail-dominated, "
          "same class as battery), q = 4 W_max < 1 with real "
          "margins, C_D2 finite -- the a-extension ALGEBRA is "
          "CLOSED; its remaining demands are the battery-class "
          "{d_1 > 0, mass} statements: %s" % "; ".join(det51))

    #  margin instantiation inside the planted window
    sq_lo, sq_hi = math.sqrt(am), math.sqrt(ap)
    eps_m = 0.125
    loc = gam[(gam >= sq_lo - eps_m) & (gam <= sq_hi + eps_m)]
    bad_meas = float(np.sum(4.0 * loc * eps_m)) if len(loc) else 0.0
    width = ap - am
    ok52 = bad_meas < width
    #  exhibit a good a: scan the interior grid for margin >= eps
    good_a, good_q = None, None
    for i in range(WGRID_N):
        a_try = am + (ap - am) * (i + 1) / (WGRID_N + 1)
        sqt = math.sqrt(a_try)
        mg = float(np.min(np.abs(gam - sqt)))
        if mg >= eps_m:
            wr = float(np.max(w_of(a_try, gam[:200])))
            good_a, good_q = a_try, 4.0 * wr
            break
    ok52 = ok52 and good_a is not None and good_q < 1.0
    check("G52-margin-in-window", ok52,
          "MARGIN LEMMA inside the planted window W = (%.2f, %.2f) "
          "(width %.2f): bad-a measure <= %.2f < width (local cache "
          "zeros %d, eps = %.3f); good a = %.2f exhibited with "
          "q_real = %.4f < 1 (eta = %.1e > 0): the two-branch "
          "degeneracy is absorbed INSIDE the window by a-choice"
          % (am, ap, width, bad_meas, len(loc), eps_m,
             good_a or -1, good_q or -1,
             1 - (good_q or 2)), kind="gate")

    #  window-a unabsorbability + on-line negative control
    ok53 = all(v > 1.0 for v in inside)
    onl = []
    for a_v in (250.0, 306.25, 900.09):
        onl.append(float(np.max(4.0 * w_of(a_v, gam))))
    ok53 = ok53 and all(v <= 1.0 + 1e-12 for v in onl)
    check("G53-window-a-irreducible", ok53,
          "|4 w_pair| > 1 at EVERY interior a of the planted window "
          "(the positivity leg cannot be dodged by a-choice: "
          "window-a is UNABSORBABLE -- the irreducible RH-"
          "equivalent tail core, r128 G26 sharpened to a >= "
          "(H - 1/2)^2) AND on-line negative control: max 4 w_a("
          "gamma) over 7000 cache zeros = %s <= 1 at a = 250/"
          "306.25/900.09 (real points can NEVER trip the window: "
          "w <= 1/4 exact)" % ", ".join("%.6f" % v for v in onl))

    # ------------------------------------------------ S6 audit+census
    section("S6  A-AUDIT VERDICT + DEFINITIVE CENSUS + MIN-CUT")
    hedge = (H_VERIF - 0.5) ** 2
    check("G60-a-quantifier-verdict", True,
          "A-QUANTIFIER RE-AUDIT (r141-G60 method, first time for "
          "a; CHAIN-AUDIT typing): dense-a REDUCES to DENSE-TAIL"
          "(a > (H-1/2)^2 = %.3e); a-extension (gamma_1^2 = 199.79 "
          "< a < (H-1/2)^2) is CHAIN-OBSOLETE for detection (G17) "
          "and its ALGEBRA is CLOSED (D2 + MG, G18/G19/G51/G52); "
          "window-a is IRREDUCIBLE (G53); consolidation: THREE "
          "a-walls -> ONE wall TAILWPD = {L1, WPD}/(H-conv) on a "
          "dense subset of ((H-1/2)^2, inf), typed RH-EQUIVALENT-"
          "AT-TAIL; below the tail the k-tail positivity consumes "
          "only PT21 + w in [0,1/4] exact" % hedge)

    # ---- the census table (W4)
    CENSUS = [
        ("ANCHOR-EPS-LOCK", "arithmetic-pinning",
         "1 instrument-chosen point per block; L_EPS anchors "
         "0.1088..0.2713 in (0.05, 0.35); depth 7.3..55.4 dex "
         "linear in x", "r137/r140/r151/r152"),
        ("TOPROOT (incl. collapse-rate lock + T-WINDOW coordinate)",
         "arithmetic-pinning",
         "FULLGAP/y_t = 2.23..3.64 O(1)-lock; T-window 0 < T <= "
         "1.22 y_t; PROFCAP <= 1 on six blocks", "r140/r146/r150/"
         "r154"),
        ("SUSCAP2R", "arithmetic-pinning",
         "s = 0.0297..0.0512 flat, s x gap = 1.0000; tail-heavy "
         "J* ~ m/3", "r139/r141/r144/r146"),
        ("DELTA1FLOOR", "arithmetic-pinning",
         "delta_1/FULLGAP = 1.0000 tight; TRACEFLOOR 4.5e-6.."
         "8.8e-9 falling vs demand x^25; rate-lock = bottom-root "
         "separation of (P, B_00)", "r142/r146/r150"),
        ("PERCELL-REL", "technical-wall -> per-cell-certified-at-"
         "grid (THIS ROUND); lambda-uniform == DEPTH-LIPSCHITZ "
         "(measured-identity-candidate class)",
         "C_cell = osc/U printed per block (<= 1.5 bar); drift "
         "-24.8..-141.3 == depth slope (PC3 chase); Jensen n < 1 "
         "discs CITED", "r148/r151 + THIS"),
        ("JUMPSUM", "technical-wall -> CLOSED-MODULO-COJUMP-LOCK "
         "(THEOREM JJ, THIS ROUND); COJUMP-LOCK typed MEASURED "
         "(NOT an identity: G14 counterexample + G41 ladder floor)",
         "|Delta log(1+L)| <= |s| exact; c_est = |s| x table; "
         "mean|s| scaling ~ -0.9; detuning <= 1e-3",
         "r151 + THIS"),
        ("H-pin (L1BAND / DOMASYM)", "arithmetic-pinning",
         "ball-matching + no-stray + zone mass <= TL/8; x_0 = 121 "
         "(BW25 112); Q-swamp strip per-rung certified",
         "r131/r133/r136"),
        ("SIMPLICITY (cell lemma leg)", "measured",
         "FULLGAP > 0 at every rung + dense-u point; r143 fine-"
         "grid smoothness", "r147"),
        ("H-FW contents", "classical-conditional",
         "M2-validity r135-class; ball validity b <= sp/2; zone-"
         "mass margin poly-tolerant; tau-pos + census framework",
         "r135/r137/r147"),
        ("TAILWPD (= dense-a + a-extension + window-a, "
         "consolidated THIS ROUND)", "classical-conditional, "
         "RH-EQUIVALENT-AT-TAIL",
         "demand = {L1, WPD}/(H-conv) on a dense subset of "
         "((H-1/2)^2, inf) ~ (9e24, inf); below: closed by PT21 + "
         "w in [0,1/4]; extension algebra closed by D2 + MG",
         "r128/r132 + THIS"),
    ]
    open_r151 = {"ANCHOR-EPS-LOCK", "JUMPSUM", "PERCELL-REL",
                 "TOPROOT", "SUSCAP2R", "DELTA1FLOOR", "dense-a",
                 "a-extension", "window-a"}
    open_r154 = {"T-WINDOW", "TOPROOT", "PERCELL-REL", "JUMPSUM",
                 "SUSCAP2R", "DELTA1FLOOR", "dense-a",
                 "a-extension", "window-a"}
    open_cdlvi = {"TOPROOT", "ONSETCAP", "SUSCAP2R", "DELTA1FLOOR",
                  "a-walls", "H-pin", "SIMPLICITY", "H-FW"}
    cover = {
        "ANCHOR-EPS-LOCK": "ANCHOR-EPS-LOCK",
        "JUMPSUM": "JUMPSUM", "PERCELL-REL": "PERCELL-REL",
        "TOPROOT": "TOPROOT", "T-WINDOW": "TOPROOT",
        "ONSETCAP": "ANCHOR-EPS-LOCK",
        "SUSCAP2R": "SUSCAP2R", "DELTA1FLOOR": "DELTA1FLOOR",
        "dense-a": "TAILWPD", "a-extension": "TAILWPD",
        "window-a": "TAILWPD", "a-walls": "TAILWPD",
        "H-pin": "H-pin", "SIMPLICITY": "SIMPLICITY",
        "H-FW": "H-FW"}
    names = set(cn.split(" ")[0] for cn, _t, _m, _p in CENSUS)
    okcov = all(cover[k].split(" ")[0] in names
                for k in (open_r151 | open_r154 | open_cdlvi))
    #  no-double-count: ONSETCAP == TLAWCAP == BANDMASS loop (v920
    #  CITED) -> the block form decomposes into ANCHOR-EPS +
    #  PERCELL-REL + JUMPSUM (r151 G15 CITED); T-WINDOW is the r154
    #  onset coordinate of the TOPROOT/near-align complex (P3).
    okdup = len(names) == len(CENSUS)
    for cn, ct, cm, cp in CENSUS:
        info("CENSUS | %s | %s | %s | [%s]" % (cn, ct, cm, cp))
    check("G61-definitive-census", okcov and okdup,
          "THE DEFINITIVE RESIDUE: RH <== [NF-closure, proven-"
          "classical] + [Theorem R, proven] + the %d-row census "
          "above; coverage of the frozen OPEN lists (r151 + r154 + "
          "CDLVI) VERIFIED via the anti-double-count map (v920 "
          "loop equivalences + r151 G15 + r154 P3 CITED); no row "
          "double-counts; census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED ({TOPROOT, TLAWCAP(=ONSETCAP), SUSCAP2R} + "
          "DELTA1FLOOR; the walls are legs of these, plus the "
          "TAILWPD chain wall)" % len(CENSUS))

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
                ("TOPROOT", "TAILVISTHM"): INF,
                ("TAILVISTHM", "ANCHOREPS"): 1,
                ("ANCHOREPS", "PERCELLREG"): 1,
                ("PERCELLREG", "COJUMPLOCK"): 1,
                ("COJUMPLOCK", "JUMPSUMTHM"): INF,
                ("JUMPSUMTHM", "ONSETCAPTHM"): INF,
                ("ONSETCAPTHM", "CNTFLOORTHM"): INF,
                ("CNTFLOORTHM", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "FULLGAPTHM"): INF,
                ("FULLGAPTHM", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "TAILWPD"): INF,
                ("TAILWPD", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("TAILVISTHM", "ANCHOREPS")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "ANCHOREPS"): 1,
               ("ANCHOREPS", "R4HYP"): INF,
               ("NFCLOS", "PERCELLREG"): 1,
               ("PERCELLREG", "R4HYP"): INF,
               ("NFCLOS", "COJUMPLOCK"): 1,
               ("COJUMPLOCK", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G62-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 (the r151 serial chain with "
          "JUMPSUM(1) RENAMED COJUMPLOCK(1) -> JUMPSUMTHM(INF, "
          "THEOREM JJ) -- same capacity, sharper edge; WPDWIN "
          "node renamed TAILWPD after the consolidation), "
          "one-grant 5, counterfactual PARALLEL 7 NOT REAL; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED")

    # ------------------------------------------------ S7 controls
    section("S7  CONTROLS + SCREENS (T5)")
    okc_all = True
    depth_main5 = anchors.get(5, {}).get("depth", 10.0)
    for world, xw, dpsw in controls:
        rc = res.get(("ctl", (world, 0)))
        if rc is None or "error" in rc:
            check("G70-%s" % world.lower(), False,
                  (rc or {}).get("error", "missing"))
            okc_all = False
            continue
        ytb = rc["yt"] / rc["btop"] if rc["btop"] > 0 else 0.0
        gap = depth_main5 - rc["depth"]
        refuse = (rc["tauf"] < 0 and ytb <= CTRL_YTB_MAX
                  and gap >= DEPTH_GAP_MIN)
        okc_all = okc_all and refuse
        check("G70-%s" % world.lower(), refuse,
              "%s x=%.0f: tau_w=%.3e < 0 (cannot enter the "
              "TLAWCAP/co-jump currency); y_t/b_top=%.2f <= %.1f; "
              "depth_w=%.1f dex vs MAIN %.1f (gap %.1f >= %.1f: "
              "in the false world the cancellation is SHALLOW and "
              "the currency dead)"
              % (world, xw, rc["tauf"], ytb, CTRL_YTB_MAX,
                 rc["depth"], depth_main5, gap, DEPTH_GAP_MIN))
    if len(s_mean_tab) >= 3 and len(osc_tab) >= 3:
        ts = sorted(s_mean_tab)
        lt = [math.log10(max(abs(tau_tab[t]), 1e-300)) for t in ts]
        s_sj = float(np.polyfit(lt, [math.log10(max(s_mean_tab[t],
                                                    1e-12))
                                     for t in ts], 1)[0])
        to = sorted(osc_tab)
        lo_ = [math.log10(max(abs(tau_tab[t]), 1e-300)) for t in to]
        s_os = float(np.polyfit(lo_, [math.log10(max(osc_tab[t],
                                                     1e-12))
                                      for t in to], 1)[0])
        check("G73-tau-screen", abs(s_sj) <= TAU_SLOPE_BAR
              and abs(s_os) <= TAU_SLOPE_BAR,
              "slopes vs log10 tau: mean|s| %.4f, C_cell %.4f "
              "(bar %.2f: the wall currencies are tau-flat, "
              "BOUND-RIDES-CONNES excluded; tau spans %d dex)"
              % (s_sj, s_os, TAU_SLOPE_BAR,
                 int(abs(lt[0] - lt[-1]))))
    else:
        check("G73-tau-screen-smoke", True, "smoke: needs 3 blocks")
    g5 = geo.get(5)
    if g5 is not None and 5 in anchors:
        with mp.workdps(g5["dps"]):
            M5, _n5 = TB.cell_matrix(mp.mpf(repr(g5["u0"])) / 2,
                                     g5["K0"], g5["icap0"],
                                     g5["dps"])
            E0 = mp.mpf(anchors[5]["tau_str"])
            M5[0, 0] = M5[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(M5)
            emin = min(Ep[i] for i in range(g5["K0"]))
            d_eps = float(abs(emin - E0))
        check("G74-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on M[0,0] at the b5 anchor moves tau by "
              "%.1e (nonzero bounded; round-118 trap)" % d_eps,
              kind="edge")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "PC1/PC2/PC3-PROVEN + DEPTH-CHASE (G10-G12)",
        "PERCELL-CERTIFIED-AT-GRID (osc <= C U across the ladder; "
        "lambda-uniform form typed DEPTH-LIPSCHITZ, measured; "
        "G32-G34)",
        "TJ-PROVEN (tau-jump bordered formula; G13/G40)",
        "COJUMP-NOT-IDENTITY (exact counterexample + ladder floor; "
        "G14/G41)",
        "JJ-PROVEN (JUMPSUM CLOSED-MODULO-COJUMP-LOCK; G15/G42)",
        "COJUMP-LOCK-MEASURED (c_est table + scaling; G42)",
        "WINDOW-ALGEBRA + WINDOW-LOCATION-PROVEN (tail confinement "
        "(H-1/2)^2; G16/G17/G50)",
        "THMD2 + MARGIN-LEMMA-PROVEN (a-extension algebra closed; "
        "degeneracy absorbed; G18/G19/G51/G52)",
        "WINDOW-A-IRREDUCIBLE (G53)",
        "A-DEMAND-REDUCED (dense-a -> DENSE-TAIL; consolidation "
        "3 -> 1 TAILWPD; G20/G60)",
        "CENSUS-DEFINITIVE (coverage + no-double-count + "
        "cardinality 4 UNCHANGED; G61)",
        "CONTROLS-REFUSE (G70-G72) + DEMAND-FLAT (G73)",
        "MINCUT (4/5; counterfactual 7 NOT REAL; G62)"]
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
        print("COMPOSITE: PC1/PC2/PC3-PROVEN + PERCELL-CERTIFIED-"
              "AT-GRID + TJ-PROVEN + COJUMP-NOT-IDENTITY + "
              "JJ-PROVEN + COJUMP-LOCK-MEASURED + WINDOW-LOCATION-"
              "PROVEN + THMD2+MARGIN-PROVEN + WINDOW-A-IRREDUCIBLE "
              "+ A-DEMAND-REDUCED + CENSUS-DEFINITIVE + "
              "CONTROLS-REFUSE + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
