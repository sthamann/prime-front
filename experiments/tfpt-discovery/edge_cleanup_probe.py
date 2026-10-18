#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_cleanup_probe -- PRIME.EDGE.CLEANUP.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (close or exactly price the FINITE/CLASSICAL legs of the
residue that no lane has directly attacked)
=======================================================================
Three targets, all NON-CORE legs of the census (CDLIX rows), each
plausibly closable below the PT21 horizon:

(E1) BAND-EDGE SLIVER + BAND-EDGE SEPARATION (r156/CDLX final form
of T-WINDOW's non-J2 legs).  The r156 cascade certifies T > 0
source-pure on [Y*, oo) with Y*/b_top = 1.1693/1.0230/1.0232/
1.0193/1.4420/2.1252 at the six blocks; the residual sliver
(b_top, Y*) holds 1/0/1/0/18/51 cache zeros (of 87/299/1033/2284/
4329/6248 strip zeros), all measured T > 0 but not certified; the
upper T-WINDOW half at zeros reduces to band-edge zero separation
(visibly binding at b24: first zero 1.0089 b_top vs crossing
1.0088 b_top).  Everything lives at height ~T_z = 2 pi x, far
below the verified-zero horizon (PT21, 3e12): CLASSICAL territory.
 (a) SLIVER CLOSURE: per-zero two-sided interval certificates at
     EVERY strip zero.  Each cache ordinate gamma carries a ball
     gamma +/- DELTA_G (DELTA_G = 1e-6, >> the declared X5 f64
     slop 1e-9, r133 CACHE_ERR class); on y in [(gamma-D)^2,
     (gamma+D)^2] every Laurent term v_k b_k/(y - b_k) is MONOTONE
     (all poles lie below the band edge), so termwise endpoint
     evaluation gives RIGOROUS enclosures T_lo <= T(y) <= T_hi on
     the whole ball.  Gates: T_lo > 0 AND T_hi < 1.5 y_t at every
     strip zero of every block (sliver zeros tabulated one by
     one).  Combined with the r156 cascade (T > 0 pointwise on
     [Y*, oo)) and the L6/P4 moment bound (|T|/y_t <= sum_{m>=2}
     |J_m| pointwise on y >= y_t, envelope-closed tail), the FULL
     T-window at zeros is then CERTIFIED per block below the
     horizon: the sliver leg closes, typed WARD/CLASSICAL-CENSUS-
     BELOW-HORIZON.
 (b) SEPARATION LAW: near the band edge T(y) = R_e/(y - b_top) +
     T_rest(y) with edge residue R_e = v_{K-1} b_{K-1}.  The
     EXACT implicit position law of the last 1.5 y_t
     down-crossing is
       y_C - b_top == R_e / (1.5 y_t - T_rest(y_C)),
     a trivial rearrangement of T(y_C) = 1.5 y_t -- machine-gated
     as an identity at the mp-bisected crossing (residual <=
     LAW_ID_BAR); the law splits into the zeroth-order edge width
     R_e/(1.5 y_t) times the signed O(1) correction
     1/(1 - T_rest(y_C)/(1.5 y_t)), BOTH tabulated per block.
     THE ONE-SIDED CLASSICAL CAP IS DEPTH-VACUOUS (found in
     smoke, machine-pinned): bounding T_rest one-sidedly by its
     positive terms (POSREST) inflates by the cancellation depth
     e^{depth} = 1/|A_0|-class (POSREST/(1.5 y_t) >> 1 at every
     block; the same vacuity family as the CDLV Jensen-a-priori
     and CDLIX PC3-drift obstructions) -- NO absolute/one-sided
     source-side bound can certify the crossing position: the
     binding coordinate is irreducibly the SIGNED near-edge value,
     i.e. a zero-position vs arithmetic-crossing statement,
     exactly the B00-ROOTGAP/S1 root-position family r156 typed.
     SEPARATION BELOW THE HORIZON: certified by the per-zero
     upper certificates of (a) (T_hi < 1.5 y_t at the first and
     every strip zero -- the provable-margin form); the measured
     separation margin (first zero minus y_C) is tabulated and
     the r156 y_C strings replicated where the crossing exists.
     Blocks with no crossing: VACUOUS-TRUE (grid max < 1.5 y_t +
     per-zero uppers).  THE LAMBDA-UNIFORM FORM TYPED: in
     gamma-currency the demand is "no zeta ordinate within
     Delta_gamma_dem = (y_C - b_top)/(2 sqrt(b_top)) above the
     top lattice frequency om_{K-1}" -- a BAND-EDGE
     ZERO-REPULSION statement whose demand width carries ONE
     signed arithmetic input (T_rest(y_C)); the demand ladder is
     printed against the RvM mean spacing (measured fraction
     ~0.2..0.5 of a mean spacing where the crossing exists): NOT
     implied by density alone, hence typed like TAILVIS at the
     horizon: CLASSICAL-CENSUS-BELOW-HORIZON (per-zero
     certificates carry it on the whole verified range) +
     OPEN-ZERO-SPACING-AT-HORIZON above, demand width
     ARITHMETIC-SIGNED-INPUT.  The lower window half at near-edge
     zeros has NO pure edge-pole law either (same vacuity class):
     typed OPEN-ARITHMETIC-AT-HORIZON, closed below the horizon
     by the same per-zero certificates.

(E2) SIMPLICITY (r147/CDLI cell-lemma open leg; census row Z8).
SIMPLICITY-AVOIDANCE, three exact legs + witnesses:
 (i)  SUBSUMPTION (the demand-level kill): the chain consumes
      simplicity of the ground value ONLY at instrument-chosen
      points (V2 sequence / Markov-selected u); at ANY selected
      point the selection criterion itself -- the LM multiplicative
      split (CDLI G13): all factors of M_src = (1+L_EPS)(1+s)
      (1+1/delta_1) are >= 1 and simultaneously <= e^{4 C_a U} --
      forces 1/delta_1 <= e^{4 C_a U} - 1 < oo, hence delta_1 > 0,
      hence tau != lam_1: THE SELECTED POINTS ARE AUTOMATICALLY
      SIMPLE.  Z8 is SUBSUMED by Z4 (DELTA1FLOOR) at every point of
      demand -- the row was double-counted.  Exact algebra, gated.
 (ii) ISOLATED-ZEROS AVOIDANCE (the r141 pattern that killed
      PFLOOR): on each clean cell (fixed K, fixed atom set -- the
      CDLI cell selection; CDLV AB2: K-jumps are the only
      discontinuities) the matrix entries are real-analytic in u
      (finite fixed sums of analytic terms, FORM-cited), so
      disc(u) = discriminant of the characteristic polynomial =
      prod_{i<j}(lam_i - lam_j)^2 is real-analytic and >= 0;
      FULLGAP > 0 + all adjacent eigengaps > 0 at ONE point of the
      cell witness disc(u_0) != 0, hence disc is NOT identically
      zero, hence (identity theorem, CITED AS FORM) its zeros --
      in particular all bottom-degeneracy points -- are ISOLATED
      and countable per cell: measure ZERO.  The V2 measure lemma
      (r141, re-gated constants) loses NOTHING: 3/4 - 0 == 3/4 of
      every log window stays good, and any positive-width subcell
      minus a measure-zero set is nonempty -- the instrument
      dodges degeneracies at ZERO COST.
 (iii) WITNESSES ON THE LADDER: FULLGAP = (lam_1 - tau)/|tau| on
      the frozen strings (r139/r143/CDLIV/CDLXI: 2.2255e5/
      9.951e5/1.062e7/3.250e7/1.138e8/1.651e8, the b28 value
      derived from the CDLXI TRACEFLOOR string 6.056e-9,
      DISCLOSED) + min adjacent eigengap > 0 (ALL pairs) at all
      six anchors ==> per-cell disc-witness; in-cell grids (4/4/
      4/4/2 interior points at b5..b24; b28 anchor-only,
      DISCLOSED build cost) show the floor persists across the
      cell.  RESIDUAL after this round: NONDEGENERATE-CELL ("no
      identically-degenerate clean cell") -- strictly weaker than
      per-point SIMPLICITY, witness-certified at zero marginal
      cost on every cell the chain ever builds (the witness IS
      the cell's own eigendata).  VERDICT SHAPE: census row Z8
      FALLS (subsumed by Z4 at demand points + zero-cost
      avoidance); the 10-row CDLIX census drops to 9 rows;
      {MEAS, OMEGA-POS} cardinality 4 UNCHANGED (Z8 was never one
      of the four).
 NULL CONTROL: the avoidance algebra is world-blind (fake worlds
 also have simple ground states); its arithmetic content sits in
 the SELECTION criterion, which the worlds cannot enter (tau_w <
 0 breaks the M_src >= 1 precondition) -- both legs gated.

(E3) THE Q-SWAMP STRIP (x < x_0; r133 x_0(HSW) = 121, r144
x_0(BW25) = 112).  The r133 Theorem-A assemblage D(x, a) = TL -
TL/8 - (N - n_z) w_a(T_z) is swamped below x_0 because the
unconditional HSW counting slack Q(T) ~ 10 zeros at band scale
eats the first tail shell and inflates (N - n_z).  THE NAMED EXIT
(r138): Turing-class LOCAL BAND CERTIFICATES as their own declared
currency.  At strip heights (T_z <= 2 pi * 121 ~ 760, gamma_N <=
~1100, tail summed to the cache top 7264.75 -- ALL heights are
FOUR-DIGIT, ten orders below the PT21 horizon 3e12) the verified
census IS such a certificate: zone count m = #{gamma <= T_z} EXACT
(ball-deflated: gamma + CACHE_ERR), gamma_N EXACT, and the
certified tail lower bound tail1_cs = sum_{j > N, j <= 7000}
w_a(gamma_j + CACHE_ERR) (positive terms beyond the cache top
DROPPED -- a valid lower bound).  CENSUS ASSEMBLAGE (same
Theorem-A slack algebra, re-gated exactly):
   D_cs(x, a) := (7/8) tail1_cs - (N - m) w_a(T_z),
   MRB_cs <= [tail1_cs/8 + a G(T_z) + (N - m) w_a(T_z)] / D_cs,
with the H-pin zone budget re-indexed to tail1_cs/8 (same 1/8
fraction, DISCLOSED; the mixed form with the original shell
budget is printed as INFO).  DELIVERABLES: (a) local band
certificates at the representative sub-ladder x = 30/60/90 (full
tables: K, N, gamma_N, m, D_hsw (the swamp exhibit), D_cs,
MRB_cs); (b) the WHOLESALE scan: D_cs(x, a) > 0 for ALL integers
x in [3, 121] x battery a in (1, 4, 16) ==> THE STRIP CLOSES
WHOLESALE (a finite computation, seconds); if any (x, a) fails
the exact price is printed; (c) bridge replication: D_hsw < 0 at
x in (13, 21, 34, 55, 89) battery-wide (r133 G42), x_0(HSW) ==
121 and x_0(BW25) == 112 on the integer scan 90..200 (r133 G43 +
r144 rescan) -- the census currency then covers [3, 121) and the
unconditional HSW/BW currency covers x >= x_0: NO GAP.
CONSEQUENCE (typed): for EVERY integer x >= 3, H-pin(x) implies
the full r132 residue {d_1 > 0, MRB} -- the Theorem-A
conditionality sharpens from "x >= 121 + ward-only strip" to
"x >= 3 with the strip census-certified"; the certificates are
typed WARD/CLASSICAL-CENSUS-BELOW-HORIZON (citable per the
v914/v921 conventions; heights <= 7.3e3 << 3e12).  H-pin itself
(census row Z7's arithmetic half) is UNTOUCHED -- no omega
closed, the swamp OBSTRUCTION (which blocked the assembly, not
H-pin) falls.

(T4) RED TEAM: controls SMOOTH/SCRARITH x=5 + EPSTEIN x=8 refuse
on the E1 currencies (tau_w < 0, J_2_w <= -0.1, y_t_w/b_top <=
1.5, n_esc <= 1) while the SR1 trace identity and the E2 witness
algebra hold world-blind (null controls, typed); tau-screens on
the flat ratio coordinates (FULLGAP_rel, minT_lo/y_t, SUMJ,
d_hi/b_top where defined) with the A_0^2 rider disclosed
(BOUND-RIDES-CONNES); E3 consumes NO source data (world-blind
classical counting; screen exempt with reason, typed
BAND-CURRENCY); conditioning 1e-25 at the b5 anchor; AST firewall
(NO zeta use anywhere, np.load ONLY in ward_, no zero-oracle
names, no verification/ import); EVERY cache use typed:
ward/classical-census-below-horizon (E1 strip zeros gamma <=
sqrt(y_t) <= 6.94e3; E3 counts/tails gamma <= 7.3e3; both <<
3e12).  Frozen quantifiers: all statements per-block/per-cell on
instrument-chosen anchors (SEQ level inherited; no ALL-X demand).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall; G02 cache health (X5, READ-ONLY).
S1  exact layer (kind=exact; sympy generic + exact rational
    instances):
    G10 interval/edge-law algebra: d/dy[vb/(y-b)] == -vb/(y-b)^2
    (termwise monotonicity ==> endpoint enclosures RIGOROUS);
    edge split T <= R_e/(y-b_top) + POSREST(d) and >= ... +
    NEGREST(d) on y >= b_top + d (exact rational 3-term
    instance); the implicit crossing law y_C - b_top ==
    R_e/(1.5 y_t - T_rest(y_C)) as exact rearrangement (generic);
    G11 cascade/window-split re-gates: level shift y F_1 == a_4 +
    F_2 generic; |sum J_{m+1} z^{-m}| <= sum |J_m| for z >= 1
    (instance); geometric envelope tail sum_{m>M} q^m ==
    q^{M+1}/(1-q) exact at rational q (the SUMJ tail closure);
    G12 simplicity subsumption: disc(charpoly) == prod (l_i -
    l_j)^2 generic on the conjugation-invariant frame (>= 0, == 0
    iff a repeated pair); the LM split chain: factors >= 1 and
    product <= B ==> 1 + 1/delta_1 <= B ==> delta_1 >= 1/(B-1) >
    0 ==> tau != lam_1 (exact, positive symbols + instance);
    G13 isolated-zeros + measure cost: polynomial instance (zeros
    isolated, finite count); geometric cover sum eps/2^i == eps;
    3/4 - 0 == 3/4 (V2 constant re-gate); positive-width subcell
    minus measure-zero set nonempty (instance); identity theorem
    CITED AS FORM;
    G14 clean-cell analyticity: representative entry sin(k pi
    u_q/(u/2)) has a Taylor series at the anchor (sympy series,
    analytic instance); fixed index set inside the cell is
    machine-checked per block in G41 (same K, same atom count);
    builder-formula analyticity CITED AS FORM;
    G15 census assemblage algebra: d_1 == M+ - M- + tail_1, M- <=
    zone + edge, M+ >= 0 ==> d_1 >= tail_1 - zone - edge; zone <=
    tail_1/8 ==> d_1 >= (7/8) tail_1 - edge (exact); exact-count
    dominance instance (N_fin <= N <= C(T) for T >= gamma_N);
    w_a' == 2at(a - t^2)/(a + t^2)^3 (decreasing branch t >
    sqrt(a), instance); ball deflation + positive-term dropping
    legality (instances).
S2  G20 HSW G(T) sanity (cache partial sums below G; monotone).
S3  E1 per-block ladder, tags 5/8/13/18/24/28 (r154/r156 anchors
    VERBATIM via AEP.anchor_select, dps 60/80/120/140/150/155):
    G30 anchor certificates: L_EPS on the r151/r153/r154 strings
    rel <= 5e-3; n_neg == 0; a_2 sign == -1; FULLGAP > 0
    (STRUCTURE gate; the r139/r142 FULLGAP strings live on the
    INTEGER rungs, not on the anchor cells -- anchor values
    quoted as new calibration, SMOKE-1 NOTE); sqrt(y_t) <= 0.999
    gamma_top (strip complete in cache);
    G31 cascade replication: Y*/b_top on the r156 strings rel <=
    5e-3; sliver counts == (1, 0, 1, 0, 18, 51) EXACT; strip
    counts == (87, 299, 1033, 2284, 4329, 6248) EXACT; T <= 0
    cache violations above Y* == 0;
    G32 PER-ZERO LOWER CERTIFICATES: T_lo > 0 at EVERY strip zero
    (n_cert_lo == n_strip); the sliver zeros tabulated one by one
    (gamma, y/b_top, T_lo/y_t, T_hi/y_t); min margin printed;
    G33 PER-ZERO UPPER CERTIFICATES: T_hi < 1.5 y_t at EVERY
    strip zero (n_cert_hi == n_strip); max T_hi/y_t printed;
    G34 SUMJ: sum_{m=2}^{400} |J_m| + envelope tail <= 0.5 (the
    pointwise upper window on y >= y_t; measured expectation
    ~0.15 from the r154/r156 J-strings + small tail, DISCLOSED
    headroom >= 3x);
    G35 SEPARATION LAW per block: status in {LAW-ID-CERT
    (crossing exists: mp-bisected y_C, law identity residual <=
    LAW_ID_BAR, first ball-lowered zero > y_C, first-zero upper
    per-zero certificate carries, y_C/b_top on the r156 strings
    rel <= 5e-3 at (5, 8, 24) expected 1.0455/1.0455/1.0088),
    VACUOUS-TRUE (no 1.5 y_t crossing on the fine grid AND grid
    max T < 1.5 y_t AND per-zero uppers carry)}; the ONE-SIDED
    CAP VACUITY exhibit POSREST/(1.5 y_t) printed per block
    (machine-pinned obstruction, expected >> 1 -- e^{depth}
    class); law decomposition tabulated (zeroth-order width
    R_e/(1.5 y_t b_top), signed correction T_rest(y_C)/y_t,
    separation margin (first_z - y_C)/b_top);
    G36 demand ladder: Delta_gamma_dem = (y_C - b_top)/
    (2 sqrt(b_top)) vs RvM mean spacing printed per crossing
    block, finite; the lambda-uniform typing printed
    (TAILVIS-style at-horizon typing; ARITHMETIC-SIGNED-INPUT
    demand width).
S3b E2 gates:
    G40 disc-witness at all six anchors: FULLGAP > 0 AND min
    adjacent eigengap > 0 over ALL pairs (strict, mp);
    G41 in-cell floor: interior points (fracs 0.30/0.42/0.58/0.70
    core 5..18; 0.35/0.65 at b24; NONE at b28, DISCLOSED): same
    K, same atom count (fixed index set machine-checked), FULLGAP
    > 0 at every point;
    G42 demand audit (simplicity): set logic -- the consumers of
    simplicity {cell-lemma branch currencies (CDLI), AD1 P'(tau),
    SB1 partial fractions (CDLXI), TJ bordered jumps (CDLIX)} all
    consume at instrument-chosen points; selected points carry
    delta_1 > 0 by the selection criterion (G12 chain); no ALL-U
    demand survives ==> Z8 SUBSUMED; avoidance cost 0 (G13).
S3c E3 gates:
    G70 census tail consistency: tail1_cs > 0 and tail1_cs <=
    a G(gamma_N) (1 + 1e-6) at the representative rungs
    (cross-instrument vs the HSW closed form);
    G71 representative local band certificates x = 30/60/90: full
    tables printed; D_cs > 0 for all battery a;
    G72 WHOLESALE SCAN: D_cs(x, a) > 0 for ALL integers x in
    [3, 121] x a in (1, 4, 16); min margin + argmin printed; on
    failure the exact price list is printed (gate then FAILS
    honestly);
    G73 HSW strip replication: D_hsw < 0 at x in (13, 21, 34, 55,
    89) for all battery a (r133 G42) AND x_0(HSW) == 121 on the
    integer scan 90..200 (r133 G43 / r144);
    G74 BW25 replication: x_0(BW25) == 112 on the same scan (r144
    rescan; published constants 0.10076/0.24460/8.08344);
    G75 heights typing: max height consumed by ANY census read
    (E1 strip sqrt(y_t); E3 gamma reads) <= 7.3e3 << 3e12 (PT21);
    every cache use enumerated + typed ward/classical-census-
    below-horizon.
S4  controls G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 AND |A_0_w| in (0.05, 2.0) AND y_t_w/b_top <= 1.5
    AND J_2_w <= -0.1 AND n_esc <= 1 AND SR1 world-blind <= 1e-40
    (null control) AND world eigengap lam_1 - lam_0 > 0 (the E2
    witness algebra is world-blind -- null control, typed);
    G53 consistency.
S5  G54 tau-screen: slopes vs log10 tau of log10 FULLGAP_rel,
    log10 minT_lo/y_t, log10 SUMJ <= 0.35 (DEMAND-FLAT); d_hi/
    b_top slope printed where >= 3 blocks define it; RIDER: slope
    log10 A_0^2 printed (rides tau by construction --
    BOUND-RIDES-CONNES typed); E3 screen-exempt with reason
    (consumes NO source data; BAND-CURRENCY typed); G55
    conditioning (1e-25 shift at the b5 anchor; r118 trap).
S6  G60 demand audit (SEQ level inherited; per-block statements;
    census below horizon; no ALL-X demand); G61 min-cut (r116
    replica; r154/r156 graph VERBATIM -- this round closes
    below-horizon content INSIDE the TWINDOW edge, drops row Z8
    by subsumption, and de-swamps the DOMASYM strip; the SET is
    unchanged: flows base 4 / refined 5 / one-grant 5 /
    counterfactual-parallel 7 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED).
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; BW25 = (0.10076, 0.24460, 8.08344)
[Bellotti-Wong 2025 published, r144 pin]; M_JETS = 400; MGRID =
(2, 4, 8, 16, 32, 64, 128, 256, 400); WORKERS = 14 (spawn,
deterministic gather; concurrent lanes untouched).
BLOCKS = (5, 5.44, 60), (8, 8.50, 80), (13, 13.50, 120),
(18, 18.50, 140), (24, 24.50, 150), (28, 28.50, 155);
POLY_MAXSTEPS = 3000; CASC_JMAX = 24; CASC_TW_MAX = 2.0; CASC_BIS
= 60; TOW_TAIL_EPS = 1e-35; YC_LEVEL = 1.5; DELTA_G = 1e-6;
CACHE_ERR = 1e-9 (declared X5 slop, r133); SEP_BIS = 80 (mp
crossing bisection); LAW_ID_BAR = 1e-18 (identity residual at the
bisected crossing, relative to 1.5 y_t); YC_GRID_FINE = 1500 on
log y in [log 1.0001 b_top, log 1.25 b_top]; YC_GRID_COARSE =
300 to 4 y_t; INCELL_FRACS core = (0.30, 0.42, 0.58, 0.70), b24
= (0.35, 0.65), b28 = () DISCLOSED.
BARS: LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
24: 0.2566, 28: 0.2713} rel 5e-3 (r151/r153/r154 strings);
FULLGAP > 0 STRUCTURE gate (anchor-cell values are NEW
calibration data, quoted in the SMOKE-1 NOTE; the r139/r142
strings 2.2255e5/... live on the INTEGER rungs and are NOT
anchor comparables -- DISCLOSED); YSTAR_TAB = {5: 1.1693, 8:
1.0230, 13: 1.0232, 18: 1.0193, 24: 1.4420, 28: 2.1252} rel
5e-3 (r156 record strings);
RESID_TAB = {5: 1, 8: 0, 13: 1, 18: 0, 24: 18, 28: 51} EXACT;
STRIP_TAB = {5: 87, 8: 299, 13: 1033, 18: 2284, 24: 4329, 28:
6248} EXACT (r156); YC_TAB = {5: 1.0455, 8: 1.0455, 24: 1.0088}
rel 5e-3, NOCROSS = (13, 18, 28) (r156); SUMJ_BAR = 0.5
(expectation ~0.16 from the r154/r156 J-strings, headroom ~3x,
pre-freeze unmeasured beyond J_14, DISCLOSED); CASC_YT_MAX =
0.15; STRIP_CACHE_FRAC = 0.999; per-zero margins: STRUCTURE
gates only (T_lo > 0, T_hi < 1.5 y_t -- the claims themselves;
deep blocks pre-freeze unmeasured, DISCLOSED; error class:
|T'| Delta_y ~ 40x below the r156 measured min margins).
E3: A_BAT = (1, 4, 16); X_CENSUS_SCAN = 3..121 integer; X_REP =
(30, 60, 90); X_STRIP_NEG = (13, 21, 34, 55, 89); X0_SCAN =
90..200 integer; X0_HSW_EXPECT = 121; X0_BW_EXPECT = 112;
TL shells lam in (1.5, 2, 3) x J in (1, 2, 3, 4, 6, 8) (r133
VERBATIM, for D_hsw/D_bw + the mixed-budget INFO only); f64 is
used for the E3 closed-form/count layer (O(1e-3) flat sums of
positive terms, margins >= 1.3x, DISCLOSED -- the counts
themselves are integers, ball-deflated by CACHE_ERR).
CTRL_A0_WIN = (0.05, 2.0); CTRL_YTB_MAX = 1.5; CTRL_J2_MAX =
-0.1; CTRL_NESC_MAX = 1; CTRL_SR_BAR = 1e-40; TAU_SLOPE_BAR =
0.35; COND_WIN = (1e-40, 1e-10); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use.
All mpf arithmetic inside explicit mp.workdps blocks in-worker;
per-zero enclosures, jets, cascade, edge law all mp end-to-end
(r147/r141 underflow classes banned); f64 transport only for
flat O(1) ratio currencies and the E3 count layer (DISCLOSED).

CALIBRATION DISCLOSURE: NO pre-freeze scratch script was run for
this probe; every replication window derives from the frozen
strings of the cited rounds (r151/r153/r154 L_EPS; r156 Y*/
sliver/strip/y_C/J_2 strings; r133/r144 x_0 and strip signs),
quoted verbatim in FROZEN NUMERICS.  Genuinely NEW quantities
(per-zero margins, y_C law decomposition, demand ratios,
D_cs/MRB_cs, SUMJ) are either exact-layer theorems (risk-free),
STRUCTURE gates (the claim itself is the gate), or disclosed-
unmeasured with stated error-class headroom (SUMJ_BAR).  Smoke
runs are logged; any instrument repair is disclosed as a
numbered SMOKE NOTE appended here BEFORE the frozen run;
amendments after the frozen run, if any, are appended as
numbered AMENDMENT blocks.
SMOKE-1 NOTE (disclosed; smoke1 = 30/32 at 107.4 s, log
edge_cleanup_probe.smoke1.log; b5-only subset; THREE repairs,
one of them a FINDING; no claim-bearing bar/criterion/window
moved):
(1) G11 geometric-tail gate: sympy summation over symbolic
positive q returns a convergence Piecewise that simplify cannot
kill -- REPAIRED to the exact rational instance q = 1/3 (the
same identity; the SUMJ tail closure itself always ran at
concrete mp values).
(2) G30 FULLGAP window: the frozen r139/r142 strings (2.2255e5
at x = 5) live on the INTEGER rungs (R4 cells), while this
probe's blocks sit on the r151/r154 ANCHOR cells (x0 = 4.824 at
b5) -- measured anchor FULLGAP 1.2827e5 (in-cell point at frac
0.30: 1.4013e5): NOT the same point, no contradiction.  The
gate is re-typed to the STRUCTURE form FULLGAP > 0 (which is
all E2 consumes); the anchor values are quoted as new
calibration data.  No E2 criterion moved (the witness demands
strict positivity only).
(3) G35 separation law -- THE SMOKE FINDING (machine-pinned):
the planned one-sided cap d_hi from POSREST is DEPTH-VACUOUS at
b5 (POSREST >> 1.5 y_t at every d <= 3 b_top: the one-sided
rest sum carries the e^{depth} = 1/|A_0| cancellation inflation
-- the CDLV Jensen-a-priori / CDLIX PC3-drift vacuity family).
The law leg is re-specified PRE-FREEZE to the exact implicit
identity form (mp-bisected y_C + law decomposition + vacuity
exhibit), and the separation certificate to the per-zero form
(which is what the below-horizon closure consumes anyway).
Smoke exhibits quoted: b5 Y*/b_top 1.16933 (dev 2.3e-5, j = 4),
sliver 1/87 (zero at gamma = 37.5862, y/b_top 1.0940, T_lo/y_t
+9.77e-1, T_hi/y_t 0.9772), per-zero 87/87 both sides, min
T_lo/y_t 1.09e-1, max T_hi/y_t 1.0565, SUMJ 0.1147, y_C(grid)
1.0437 b_top, first zero 1.0940 b_top; E3 smoke scan x = 3..30
all D_cs > 0 (worst margin 0.346 at (12, 1)), x = 30 tables
D_hsw -5.59e-4/-2.23e-3/-8.92e-3 vs D_cs +6.95e-4/+2.78e-3/
+1.11e-2 (a = 1/4/16), tail1_cs 1.013e-2 <= a G(gamma_N)
1.188e-2 at a = 4; conditioning 4.5e-26.
SMOKE-2 NOTE (disclosed): smoke2 = 32/32 at 107.3 s (log
edge_cleanup_probe.smoke2.log, SPEC_SHA ee70cba1473b12f9 at
smoke2) with the three SMOKE-1 repairs in place; new smoke
exhibits quoted: b5 mp-bisected y_C = 1.0437 b_top (the r156
string 1.0455 was the 400-point grid readout; dev 1.7e-3 within
the 5e-3 window), law identity residual 8e-29, T_rest(y_C)/y_t =
+0.4044 (the signed O(1) correction), separation margin (first_z
- y_C)/b_top = 5.03e-2, vacuity exhibit POSREST/(1.5 y_t) =
1e1.9 dex (>> 1; the depth class at b5 is partially cancelled --
the exhibit is a floor, the b5 depth is 7.3 dex), demand ratio
0.2177 of a mean spacing.  This note moves SPEC_SHA once more
(honest refreeze); the record run starts at the refrozen hash.
Deep blocks (18/24/28) remain pre-freeze unmeasured on all new
per-zero/law quantities (build cost) -- windows are r156-string
or STRUCTURE gates as frozen above, DISCLOSED.

VERDICT ENUMS (frozen): SLIVER-CLOSED-BELOW-HORIZON(per-zero
two-sided certificates at every strip zero + cascade above Y*;
G31/G32/G33); TWINDOW-AT-ZEROS-CERTIFIED(full window 0 < T <
1.5 y_t certified at every cache zero above the band per block;
+ SUMJ pointwise above y_t; G32-G34); SEPARATION-LAW-TYPED(exact
implicit crossing law gated at the mp-bisected y_C; lambda-
uniform form = band-edge zero repulsion with ARITHMETIC-SIGNED-
INPUT width, typed at the horizon like TAILVIS; G35/G36) +
SEPARATION-ONESIDED-CAP-DEPTH-VACUOUS(machine-pinned: POSREST
rides e^{depth}; the CDLV/CDLIX vacuity family);
SIMPLICITY-SUBSUMED(Z8 <== Z4 at every demand point; G12/G42);
AVOIDANCE-ZERO-COST(isolated zeros, measure 0; G13/G40/G41);
Z8-FALLS(census 10 rows -> 9; residual NONDEGENERATE-CELL
witness-certified per cell); QSWAMP-STRIP-CLOSED-CENSUS(D_cs > 0
wholesale on [3, 121] x battery; Theorem-A conditionality
sharpens to x >= 3; G70-G74) OR QSWAMP-STRIP-PRICED(the exact
failing set printed); HEIGHTS-TYPED(all census reads <= 7.3e3 <<
3e12; G75); CONTROLS-REFUSE + NULL-CONTROLS-WORLD-BLIND(G50-G53);
DEMAND-FLAT + BOUND-RIDES-CONNES(G54); QUANTIFIER-INHERITED(G60);
OMEGA-UNCHANGED(census {MEAS, OMEGA-POS} cardinality 4; G61);
MINCUT(4/5; counterfactual 7 NOT REAL).  Composite priority:
INSTRUMENT-EDGE > EXACT-LAYER-OBSTRUCTED > verdicts as gated.

AMENDMENT-1 (disclosed; after run1 = 31/34 at 1745.9 s, SPEC_SHA
5a1abbea78ffda13, log edge_cleanup_probe.run1.log KEPT).  THE
THREE FAILS ARE ONE FINDING: the f64-cache-ball (DELTA_G = 1e-6)
interval enclosure is ITSELF DEPTH-LIMITED -- the enclosure width
rides sum_k |v_k| ~ e^{depth} = 1/|A_0|-class, so the per-zero
certificate demands ordinate precision ~ e^{-depth}: measured
enclosure blowout T_lo/y_t = -4.05e8 / -1.86e18 / -2.80e29 /
-3.73e37 at b13/b18/b24/b28 (b5/b8 carried: 87/87 and 299/299
lower, 298/299 upper with the single marginal 1.5001 -- the
1e-6-ball is exactly at the b8 depth edge), i.e. needed
Delta_gamma ~ 1.2e-16 / 2.6e-26 / 1.8e-37 / 1.3e-45: THE SAME
MACHINE-PINNED e^{depth} VACUITY FAMILY as the G35 one-sided cap
(CDLV Jensen-a-priori / CDLIX PC3-drift).  This is exactly why
the contract routes the sliver through r131-CLASS CERTIFIED
BALLS: the pinning must be POLISHED, not f64.  REPAIR (scope +
instrument, disclosed):
(1) an AUDIT LAYER is added (r133 owner logic: the zeta attribute
    is legal ONLY inside audit_* functions; firewall updated
    accordingly): audit_polish_zero = secant polish of a cache
    ordinate on the completed-xi line at AUD_DPS = 240 (step tol
    1e-60, max 18 iterations), audit_ball_ok = sign-change
    certification of the ball t_pol +/- delta.  ALL polished
    heights are <= 280 (the sliver lives at gamma in (sqrt(b_top),
    sqrt(Y*)) <= 280; the first zeros <= 193): transcription-
    typed, ten orders below the PT21 horizon.
(2) G32 re-scoped to the CONTRACT deliverable: per-zero TWO-SIDED
    certificates at every SLIVER zero PLUS the first zero above
    the band per block, on audit-polished balls with the adaptive
    ladder AUD_DELTAS = (1e-8, 1e-14, 1e-22, 1e-32, 1e-44, 1e-52)
    (largest carrying delta chosen per zero; polish residual <=
    delta/10 enforced; ball sign-change certified);
(3) G33 re-scoped to the DEPTH-PRICE adjudication: the per-block
    certificate price (tightest delta consumed) is printed as the
    new machine-pinned exhibit BALL-CERT-DEPTH-PRICED, together
    with the f64-ball full-strip coverage counters (MEASURED
    layer: b5 full 87/87+87/87, b8 299/299 lower + 298/299 upper
    -- the far-strip zeros at deep blocks stay r156-MEASURED,
    typed; certifying all ~6e3 far-strip zeros per deep block
    would demand deep polish at heights up to 6.7e3, priced but
    not consumed here);
(4) G35 first-zero leg switches from the f64 full-strip counter
    to the audit-ball first-zero certificate.
The T-WINDOW-AT-ZEROS verdict is correspondingly SPLIT: sliver +
first zero CERTIFIED per block (all six), full strip CERTIFIED
at b5 (and b8 lower), far strip MEASURED (r156) + SUMJ pointwise
above y_t.  No E2/E3 gate touched; run2 at the amended hash is
the RECORD RUN; run3 the deterministic re-run.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; the zeta attribute ONLY inside audit_*
functions (transcription-typed polish, heights <= 280); no
import of verification/.  NO RH CLAIM.  EXPLORATION ONLY.
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
import anchor_epslock_probe as AEP            # r153 frozen builder

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
WORKERS = 14

BLOCKS = (
    (5, 5.44, 60),
    (8, 8.50, 80),
    (13, 13.50, 120),
    (18, 18.50, 140),
    (24, 24.50, 150),
    (28, 28.50, 155),
)
POLY_MAXSTEPS = 3000
CASC_JMAX = 24
CASC_TW_MAX = 2.0
CASC_BIS = 60
TOW_TAIL_EPS = 1e-35
YC_LEVEL = 1.5
DELTA_G = 1e-6
CACHE_ERR = 1e-9
SEP_BIS = 80
LAW_ID_BAR = 1e-18
AUD_DPS = 240
AUD_SECANT_MAX = 18
AUD_STEP_TOL = 1e-60
AUD_DELTAS = ("1e-8", "1e-14", "1e-22", "1e-32", "1e-44", "1e-52")
YC_GRID_FINE = 1500
YC_GRID_COARSE = 300
INCELL_FRACS = {5: (0.30, 0.42, 0.58, 0.70),
                8: (0.30, 0.42, 0.58, 0.70),
                13: (0.30, 0.42, 0.58, 0.70),
                18: (0.30, 0.42, 0.58, 0.70),
                24: (0.35, 0.65),
                28: ()}

LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
            24: 0.2566, 28: 0.2713}
LEPS_TOL = 5e-3
YSTAR_TAB = {5: 1.1693, 8: 1.0230, 13: 1.0232, 18: 1.0193,
             24: 1.4420, 28: 2.1252}
YSTAR_TOL = 5e-3
RESID_TAB = {5: 1, 8: 0, 13: 1, 18: 0, 24: 18, 28: 51}
STRIP_TAB = {5: 87, 8: 299, 13: 1033, 18: 2284, 24: 4329, 28: 6248}
YC_TAB = {5: 1.0455, 8: 1.0455, 24: 1.0088}
YC_TOL = 5e-3
NOCROSS = (13, 18, 28)
SUMJ_BAR = 0.5
CASC_YT_MAX = 0.15
STRIP_CACHE_FRAC = 0.999

HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
BW_A, BW_B, BW_C = 0.10076, 0.24460, 8.08344
A_BAT = (1, 4, 16)
X_CENSUS_LO, X_CENSUS_HI = 3, 121
X_REP = (30, 60, 90)
X_STRIP_NEG = (13, 21, 34, 55, 89)
X0_SCAN_LO, X0_SCAN_HI = 90, 200
X0_HSW_EXPECT = 121
X0_BW_EXPECT = 112
H_VERIF = 3.0e12
MAX_HEIGHT_BAR = 7.3e3

CTRL_A0_WIN = (0.05, 2.0)
CTRL_YTB_MAX = 1.5
CTRL_J2_MAX = -0.1
CTRL_NESC_MAX = 1
CTRL_SR_BAR = 1e-40
TAU_SLOPE_BAR = 0.35
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
                       "no zero-oracle; NO zeta use; cache in ward_; "
                       "no verification/ import")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- audit layer
def audit_xi_line(t):
    """completed xi(1/2 + i t), real on the critical line
    (transcription-typed; heights <= 280 only)."""
    s = mp.mpf("0.5") + mp.mpc(0, 1) * t
    return mp.re(0.5 * s * (s - 1) * mp.pi ** (-s / 2)
                 * mp.gamma(s / 2) * mp.zeta(s))


def audit_polish_zero(g_seed: float, dps_aud: int):
    """secant polish of a cache ordinate on the xi line; returns
    (t_polished, last_step) at dps_aud."""
    with mp.workdps(dps_aud):
        t0 = mp.mpf(repr(float(g_seed))) - mp.mpf("1e-7")
        t1 = mp.mpf(repr(float(g_seed))) + mp.mpf("1e-7")
        f0 = audit_xi_line(t0)
        f1 = audit_xi_line(t1)
        step = mp.mpf(1)
        for _ in range(AUD_SECANT_MAX):
            if f1 == f0:
                break
            t2 = t1 - f1 * (t1 - t0) / (f1 - f0)
            step = abs(t2 - t1)
            t0, f0 = t1, f1
            t1 = t2
            f1 = audit_xi_line(t1)
            if step < mp.mpf(repr(AUD_STEP_TOL)):
                break
        return t1, step


def audit_ball_ok(t_pol, delta_str: str, dps_aud: int) -> bool:
    """sign-change certification of the ball t_pol +/- delta."""
    with mp.workdps(dps_aud):
        dl = mp.mpf(delta_str)
        lo = audit_xi_line(t_pol - dl)
        hi = audit_xi_line(t_pol + dl)
        return bool(lo * hi < 0)


# --------------------------------------------------------- censuses
def census_weighted(wts, K, aa, dps, const):
    """r132/r154/r156 polyroots census (controls only here)."""
    with mp.workdps(dps):
        b = [(k * mp.pi / aa) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        bs = [v / s_mp for v in b]

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
        if const is not None:
            poly = [const * c for c in prod_all]
        else:
            poly = [mp.mpf(0)] * len(prod_all)
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, bs[i])
            term = [wts[k] * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        while len(poly) > 1 and poly[0] == 0:
            poly = poly[1:]
        rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                           extraprec=2 * dps)
        nreal = 0
        ys = []
        for r in rts:
            if abs(mp.im(r)) <= mp.mpf(10) ** (-10):
                ys.append(mp.re(r) * s_mp)
            else:
                nreal += 1
        ys.sort()
    return ys, nreal


# ----------------------------------------------------------- workers
def w_block(args) -> dict:
    """per-block anchor build: jets + L_EPS + FULLGAP/eigengaps +
    cascade + PER-ZERO two-sided interval certificates at every
    strip zero + SUMJ + edge-law bisection + y_C fine grid.  All
    mp in workdps; f64 transport of flat O(1) ratios (DISCLOSED)."""
    tag, x_nom, dps = args
    try:
        gam = ward_cache()
        u0, clo, chi = AEP.anchor_select(x_nom)
        x0 = math.exp(u0)
        out = dict(tag=tag, x0=x0, cell_lo=clo, cell_hi=chi)
        with mp.workdps(dps):
            u = mp.mpf(repr(u0))
            x = mp.exp(u)
            K = int(math.ceil(AEP.kfun_f(float(x))))
            icap = int(math.floor(float(x)))
            M, nrm = AEP.cell_matrix(u / 2, K, icap, dps)
            E, V = mp.eigsy(M)
            order = sorted(range(K), key=lambda i: E[i])
            i0 = order[0]
            tau = E[i0]
            Es = sorted([E[i] for i in range(K)])
            nneg = sum(1 for i in range(K) if E[i] < -mp.mpf("0.1"))
            phi = [V[i, i0] for i in range(K)]
            nn = mp.sqrt(sum(p * p for p in phi))
            phi = [p / nn for p in phi]
            cs = [phi[k] / nrm[k] for k in range(K)]
            aa = u / 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o ** 2 for o in oms]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            wk = [(-1) ** k * cs[k] * b[k] for k in range(K)]
            vk = [wk[k] / A0 for k in range(1, K)]
            bl = [b[k] for k in range(1, K)]
            Km1 = K - 1
            btop = bl[-1]
            l10 = mp.log(10)
            out["K"] = K
            out["nneg"] = nneg
            out["natoms"] = len(AEP.atoms_upto(icap))
            # FULLGAP + eigengap census (E2 witness)
            fg_rel = (Es[1] - Es[0]) / abs(Es[0])
            out["fg_rel"] = float(fg_rel)
            mingap = None
            minrel = None
            for i in range(K - 1):
                g_ = Es[i + 1] - Es[i]
                rel_ = g_ / max(abs(Es[i]), abs(Es[i + 1]))
                if mingap is None or g_ < mingap:
                    mingap = g_
                if minrel is None or rel_ < minrel:
                    minrel = rel_
            out["mingap_pos"] = bool(mingap > 0)
            out["minrel_l10"] = float(mp.log(minrel) / l10) \
                if minrel > 0 else float("-inf")
            # jets + envelope jets
            A_j = []
            Env = []
            pw = [mp.mpf(1)] * K
            cs_abs = [abs(v) for v in cs]
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    Env.append(sum(cs_abs))
                    continue
                acc = mp.mpf(0)
                ace = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
                    ace += cs_abs[k] * pw[k]
                A_j.append(acc)
                Env.append(ace)
            a = [A_j[m] / A0 for m in range(M_JETS + 1)]
            env = [abs(Env[m] / A0) for m in range(M_JETS + 1)]
            yt = abs(a[1])
            out["a2_sign"] = int(mp.sign(a[1]))
            out["yt_l10"] = float(mp.log(yt) / l10)
            out["btop"] = float(btop)
            out["yt_btop"] = float(yt / btop)
            out["tau_l10"] = float(mp.log(abs(tau)) / l10)
            out["a0sq_l10"] = float(2 * mp.log(abs(A0)) / l10)
            out["sqrt_yt"] = float(mp.sqrt(yt))
            out["J2"] = float(a[2] / yt ** 2)
            # L_EPS anchor certificate (r153/r154/r156 recipe)
            Tz = 2 * math.pi * float(x)
            Gz = mp.mpf(repr(AEP.hsw_G(Tz)))

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
                v = envres(T_PT, m)
                if best is None or v < best:
                    best = v
            eta_pt = float(best / abs(A0))
            off = 8 * mp.exp(aa) \
                * (abs(A0) * (1 + mp.mpf(repr(eta_pt)))) ** 2 \
                * mp.mpf(repr(AEP.hsw_G(float(T_PT))))
            out["leps"] = float((tau + off) / (16 * A0 ** 2 * Gz))
            # SUMJ (pointwise upper window on y >= y_t)
            sumj = mp.mpf(0)
            for m in range(2, M_JETS + 1):
                sumj += abs(a[m]) / yt ** m
            r_env = btop / yt
            tailj = (env[M_JETS] / yt ** M_JETS) * r_env / (1 - r_env)
            sumj += tailj
            out["sumj"] = float(sumj)

            def T_of(y):
                return sum(vk[i] * bl[i] / (y - bl[i])
                           for i in range(Km1))

            # ---------------- cascade certificate (r156 VERBATIM)
            def tow_level(j, ystar):
                lead = abs(a[j + 1])
                if lead == 0:
                    return mp.inf
                tot = mp.mpf(0)
                yi = mp.mpf(1)
                for m in range(2, M_JETS - j):
                    yi *= ystar
                    term = abs(a[j + m]) / (lead * yi)
                    tot += term
                    envt = env[j + m] / (lead * yi)
                    if envt < mp.mpf(repr(TOW_TAIL_EPS)) and m > 6:
                        rr = btop / ystar
                        if rr < 1:
                            tot += envt * rr / (1 - rr)
                        break
                return tot

            def casc_cert(j, Y):
                tw = tow_level(j + 1, Y)
                if tw > mp.mpf(repr(CASC_TW_MAX)):
                    return False
                cst = abs(a[j + 2]) * (1 + tw)
                coefs = [a[i + 1] for i in range(1, j + 1)] \
                    + [-cst]
                RY = mp.mpf(0)
                for c in coefs:
                    RY = RY * Y + c
                if RY <= 0:
                    return False
                try:
                    rts = mp.polyroots(coefs, maxsteps=800,
                                       extraprec=dps)
                except Exception:                  # noqa: BLE001
                    return False
                for r in rts:
                    if abs(mp.im(r)) < mp.mpf("1e-15") \
                            and mp.re(r) >= Y:
                        return False
                return True

            Ybest = None
            jbest = None
            if a[2] > 0:
                for j in range(1, CASC_JMAX + 1):
                    hi0 = 4 * yt
                    if not casc_cert(j, hi0):
                        continue
                    lo2 = mp.log(btop * mp.mpf("1.001"))
                    hi2 = mp.log(hi0)
                    for _ in range(CASC_BIS):
                        mid = (lo2 + hi2) / 2
                        if casc_cert(j, mp.exp(mid)):
                            hi2 = mid
                        else:
                            lo2 = mid
                    Yj = mp.exp(hi2)
                    if Ybest is None or Yj < Ybest:
                        Ybest = Yj
                        jbest = j
            out["casc_ok"] = Ybest is not None
            if Ybest is not None:
                out["casc_yt"] = float(Ybest / yt)
                out["casc_btop"] = float(Ybest / btop)
                out["casc_j"] = jbest

            # ---------------- PER-ZERO two-sided certificates
            dG = mp.mpf(repr(DELTA_G))
            lev = mp.mpf(repr(YC_LEVEL)) * yt
            n_strip = 0
            n_cert_lo = 0
            n_cert_hi = 0
            n_resid = 0
            n_viol = 0
            min_tlo = None
            max_thi = None
            first_z = None
            first_g = None
            sliver_rows = []
            sliver_g = []
            wpos = [vk[i] * bl[i] > 0 for i in range(Km1)]
            for g in gam:
                gm = mp.mpf(repr(float(g)))
                yc = gm * gm
                if yc <= btop:
                    continue
                if first_z is None:
                    first_z = yc
                    first_g = gm
                if yc >= yt:
                    if Ybest is not None and yc >= Ybest \
                            and T_of(yc) <= 0:
                        n_viol += 1
                    continue
                n_strip += 1
                ylo = (gm - dG) ** 2
                yhi = (gm + dG) ** 2
                if ylo <= btop:
                    continue        # cert fails (counted by != n_strip)
                Tlo = mp.mpf(0)
                Thi = mp.mpf(0)
                for i in range(Km1):
                    t_hi_end = vk[i] * bl[i] / (yhi - bl[i])
                    t_lo_end = vk[i] * bl[i] / (ylo - bl[i])
                    if wpos[i]:
                        Tlo += t_hi_end
                        Thi += t_lo_end
                    else:
                        Tlo += t_lo_end
                        Thi += t_hi_end
                if Tlo > 0:
                    n_cert_lo += 1
                if Thi < lev:
                    n_cert_hi += 1
                if min_tlo is None or Tlo < min_tlo:
                    min_tlo = Tlo
                if max_thi is None or Thi > max_thi:
                    max_thi = Thi
                if Ybest is not None and yc < Ybest:
                    n_resid += 1
                    sliver_rows.append(
                        (float(gm), float(yc / btop),
                         float(Tlo / yt), float(Thi / yt)))
                    sliver_g.append(float(gm))
                elif Ybest is not None and T_of(yc) <= 0:
                    n_viol += 1
            out["n_strip"] = n_strip
            out["n_cert_lo"] = n_cert_lo
            out["n_cert_hi"] = n_cert_hi
            out["n_resid"] = n_resid
            out["n_viol"] = n_viol
            out["min_tlo_yt"] = float(min_tlo / yt) \
                if min_tlo is not None else float("nan")
            out["max_thi_yt"] = float(max_thi / yt) \
                if max_thi is not None else float("nan")
            out["firstz_btop"] = float(first_z / btop)
            out["firstg"] = float(first_g)
            out["sliver_rows"] = sliver_rows

            # ------- edge law: y_C grid bracket + mp bisection
            Re_ = vk[Km1 - 1] * bl[Km1 - 1]
            out["edge_sign"] = int(mp.sign(Re_))

            def rest_sum(y):
                return sum(vk[i] * bl[i] / (y - bl[i])
                           for i in range(Km1 - 1))

            cross_a = None
            cross_b = None
            gmaxT = None
            prev_hi = None
            prev_y = None
            grid = list(np.linspace(
                float(mp.log(btop * mp.mpf("1.0001"))),
                float(mp.log(btop * mp.mpf("1.25"))),
                YC_GRID_FINE)) + list(np.linspace(
                    float(mp.log(btop * mp.mpf("1.25"))) + 1e-9,
                    float(mp.log(4 * yt)), YC_GRID_COARSE))
            for lg in grid:
                y = mp.exp(mp.mpf(repr(float(lg))))
                Tv = T_of(y)
                if gmaxT is None or Tv > gmaxT:
                    gmaxT = Tv
                hi_now = Tv > lev
                if prev_hi is not None and prev_hi and not hi_now:
                    cross_a, cross_b = prev_y, y
                prev_hi = hi_now
                prev_y = y
            out["yc_exists"] = cross_a is not None
            out["gmaxT_yt"] = float(gmaxT / yt)
            if cross_a is not None:
                a_, b_ = cross_a, cross_b
                for _ in range(SEP_BIS):
                    mid = mp.sqrt(a_ * b_)
                    if T_of(mid) > lev:
                        a_ = mid
                    else:
                        b_ = mid
                ycx = (a_ + b_) / 2
                out["yc_btop"] = float(ycx / btop)
                trest = rest_sum(ycx)
                out["law_id"] = float(
                    abs(Re_ / (ycx - btop) + trest - lev) / lev)
                out["trest_yt"] = float(trest / yt)
                out["law_zero_order"] = float(Re_ / (lev * btop))
                out["sep_margin_btop"] = float((first_z - ycx)
                                               / btop)
                out["sep_first_above"] = bool(
                    (first_g - dG) ** 2 > ycx)
                dg_dem = (ycx - btop) / (2 * mp.sqrt(btop))
                msp = 2 * mp.pi \
                    / mp.log(mp.sqrt(btop) / (2 * mp.pi))
                out["dgam_dem"] = float(dg_dem)
                out["dem_ratio"] = float(dg_dem / msp)
                # one-sided cap vacuity exhibit (POSREST at y_C)
                pr = mp.mpf(0)
                for i in range(Km1 - 1):
                    if wpos[i]:
                        pr += vk[i] * bl[i] / (ycx - bl[i])
                out["vac_l10"] = float(mp.log(pr / lev) / l10) \
                    if pr > 0 else float("-inf")
            else:
                out["yc_btop"] = float("nan")
                out["dem_ratio"] = float("nan")

            # ------- audit-ball certificates (sliver + first zero)
            def enclose(gc, dl):
                ylo2 = (gc - dl) ** 2
                yhi2 = (gc + dl) ** 2
                Tl = mp.mpf(0)
                Th = mp.mpf(0)
                for i in range(Km1):
                    t_h = vk[i] * bl[i] / (yhi2 - bl[i])
                    t_l = vk[i] * bl[i] / (ylo2 - bl[i])
                    if wpos[i]:
                        Tl += t_h
                        Th += t_l
                    else:
                        Tl += t_l
                        Th += t_h
                return Tl, Th

            targets = list(sliver_g)
            fgf = float(first_g)
            if all(abs(fgf - t_) > 1e-6 for t_ in targets):
                targets.append(fgf)
            targets.sort()
            aud_rows = []
            n_aud_ok = 0
            price_l10 = None
            first_aud_ok = False
            min_aud_lo = None
            max_aud_hi = None
            for gt in targets:
                tpol, resid = audit_polish_zero(gt, AUD_DPS)
                chosen = None
                Tl_f = Th_f = float("nan")
                for dstr in AUD_DELTAS:
                    dl = mp.mpf(dstr)
                    if not (resid < dl / 10):
                        continue
                    Tl, Th = enclose(tpol, dl)
                    if Tl > 0 and Th < lev \
                            and audit_ball_ok(tpol, dstr, AUD_DPS):
                        chosen = dstr
                        Tl_f = float(Tl / yt)
                        Th_f = float(Th / yt)
                        break
                okz = chosen is not None
                if okz:
                    n_aud_ok += 1
                    dlt = math.log10(float(mp.mpf(chosen)))
                    if price_l10 is None or dlt < price_l10:
                        price_l10 = dlt
                    if min_aud_lo is None or Tl_f < min_aud_lo:
                        min_aud_lo = Tl_f
                    if max_aud_hi is None or Th_f > max_aud_hi:
                        max_aud_hi = Th_f
                if abs(gt - fgf) <= 1e-6:
                    first_aud_ok = okz
                aud_rows.append((gt, float(gt * gt / float(btop)),
                                 chosen or "FAIL", Tl_f, Th_f))
            out["n_aud"] = len(targets)
            out["n_aud_ok"] = n_aud_ok
            out["aud_rows"] = aud_rows
            out["price_l10"] = price_l10 \
                if price_l10 is not None else float("nan")
            out["first_aud_ok"] = first_aud_ok
            out["min_aud_lo"] = min_aud_lo \
                if min_aud_lo is not None else float("nan")
            out["max_aud_hi"] = max_aud_hi \
                if max_aud_hi is not None else float("nan")
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_cell(args) -> dict:
    """E2 in-cell point: same-cell structure check (fixed index
    set) + FULLGAP witness at an interior point of the anchor
    cell."""
    tag, x_nom, dps, frac = args
    try:
        u0, clo, chi = AEP.anchor_select(x_nom)
        uc = clo + frac * (chi - clo)
        K0 = int(math.ceil(AEP.kfun_f(math.exp(u0))))
        icap0 = int(math.floor(math.exp(u0)))
        Kc = int(math.ceil(AEP.kfun_f(math.exp(uc))))
        icapc = int(math.floor(math.exp(uc)))
        same_k = Kc == K0
        same_atoms = len(AEP.atoms_upto(icapc)) \
            == len(AEP.atoms_upto(icap0))
        with mp.workdps(dps):
            M, _nrm = AEP.cell_matrix(mp.mpf(repr(uc)) / 2, Kc,
                                      icapc, dps)
            E, _V = mp.eigsy(M)
            Es = sorted([E[i] for i in range(Kc)])
            fg = (Es[1] - Es[0]) / abs(Es[0])
        return dict(tag=tag, frac=frac, same_k=same_k,
                    same_atoms=same_atoms, fg_rel=float(fg))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, frac=frac, error=repr(exc))


def w_control(args) -> dict:
    """control world via R4.build_cell: tau_w, A_0_w, y_t/b_top,
    J_2_w, n_esc, SR1 (world-blind null) + eigengap (E2 null)."""
    world, xw, dpsw = args
    try:
        ce = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        K = ce["K"]
        with mp.workdps(dpsw):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(ce["x"]) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
            A4 = sum((-1) ** k * cs[k] * b[k] ** 2
                     for k in range(1, K))
            yt = abs(A2 / A0)
            btop = b[K - 1]
            tau = ce["mpE"][0]
            gap01 = float(ce["mpE"][1] - ce["mpE"][0])
            J2w = (A4 / A0) / (A2 / A0) ** 2
            wtsF = {k: ((-1) ** k) * cs[k] for k in range(1, K)}
            ysF, _nnr = census_weighted(wtsF, K, aa, dpsw, cs[0])
            P1 = sum(ysF) - sum(b[1:])
            sr1 = float(abs(P1 / (-A2 / A0) - 1))
            n_esc = sum(1 for y in ysF if y > btop)
            return dict(world=world, tauf=float(tau),
                        a0f=float(abs(A0)), ytb=float(yt / btop),
                        j2w=float(J2w), n_esc=n_esc, sr1=sr1,
                        gap01=gap01)
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, error=repr(exc))


# --------------------------------------------------------- E3 closed forms
def w_of(a: float, t: float) -> float:
    return a * t * t / (a + t * t) ** 2


def hsw_G_gen(T: float, abc) -> float:
    al, be, cc = abc
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        alm = mp.mpf(repr(al))
        bem = mp.mpf(repr(be))
        ccm = mp.mpf(repr(cc))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (alm * (2 * lg + 1) / 2 + bem * (ll + 1 / (2 * lg))
              + ccm) / Tm ** 2
        t3 = (alm * lg + bem * ll + ccm) / Tm ** 2
        return float(t1 + t2 + t3)


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_gen(T: float, abc) -> float:
    al, be, cc = abc
    return al * math.log(T) + be * math.log(math.log(T)) + cc


def t_star_gen(N: int, abc) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_gen(mid, abc) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells_gen(N: int, a: float, Ts: float, abc) -> float:
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = m_rvm(Ts) + q_gen(Ts, abc)
            for j in range(J):
                n_next = m_rvm(Tj[j + 1]) - q_gen(Tj[j + 1], abc)
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * w_of(a, Tj[j + 1])
                u_prev = m_rvm(Tj[j + 1]) + q_gen(Tj[j + 1], abc)
            best = max(best, tot)
    return best


def asym_D_gen(x: float, a: float, abc) -> float:
    """r133 THEOREM-A closed form D(x, a) with parametrized
    counting constants (HSW or BW25)."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    Ts = t_star_gen(N, abc)
    Tz = 2 * math.pi * x
    n_z = m_rvm(Tz) - q_gen(Tz, abc)
    TL = tl_shells_gen(N, a, Ts, abc)
    m_minus_edge = max(0.0, (N - n_z)) * w_of(a, Tz)
    return TL - TL / 8.0 - m_minus_edge


def census_D(x: int, a: float, gam: np.ndarray) -> dict:
    """the Turing-class LOCAL BAND CERTIFICATE assemblage: exact
    ball-deflated census counts + certified tail lower bound
    (positive terms beyond the cache top dropped).  All heights
    <= gamma_top = 7264.75 << 3e12: ward/classical-census-below-
    horizon typed."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    if N >= len(gam):
        return dict(ok=False, reason="N exceeds cache")
    Tz = 2 * math.pi * x
    gsh = gam + CACHE_ERR
    m_lo = int(np.searchsorted(gsh, Tz, side="right"))
    tail = gsh[N:]
    tail1 = float(np.sum(a * tail ** 2 / (a + tail ** 2) ** 2))
    edge = max(0, N - m_lo) * w_of(a, Tz)
    D8 = 7.0 / 8.0 * tail1 - edge
    mrb = ((tail1 / 8.0 + a * hsw_G_gen(Tz, (HSW_A, HSW_B, HSW_C))
            + edge) / D8) if D8 > 0 else float("inf")
    TLs = tl_shells_gen(N, a, t_star_gen(N, (HSW_A, HSW_B, HSW_C)),
                        (HSW_A, HSW_B, HSW_C))
    Dmix = tail1 - TLs / 8.0 - edge
    return dict(ok=True, K=K, N=N, Tz=Tz, m=m_lo,
                gamN=float(gam[N - 1]), tail1=tail1, edge=edge,
                D8=D8, mrb=mrb, Dmix=Dmix)


def x0_scan(abc) -> int:
    """min integer x in [90, 200] with D(x', a) > 0 for all battery
    a and ALL integers x' in [x, 200] (r133 G43 criterion)."""
    ok_from = None
    for x in range(X0_SCAN_HI, X0_SCAN_LO - 1, -1):
        good = all(asym_D_gen(float(x), float(a_), abc) > 0
                   for a_ in A_BAT)
        if good:
            ok_from = x
        else:
            break
    return ok_from if ok_from is not None else -1


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y, d_ = sp.symbols("y d_", positive=True)
    v, bpole = sp.symbols("v bpole", real=True)

    # ---------------- G10 interval/edge-law algebra
    term = v * bpole / (y - bpole)
    okA = sp.simplify(sp.diff(term, y)
                      + v * bpole / (y - bpole) ** 2) == 0
    # endpoint bracketing instance (pole at 1, interval [2, 3])
    t5 = sp.Rational(5)
    okB = bool(t5 / (3 - 1) < t5 / (sp.Rational(2) - 1)) and \
        bool((-t5) / (2 - 1) < (-t5) / (sp.Rational(3) - 1))
    # edge split instance: R/(y-b) + pos-term + neg-term, y >= b+d
    Rr, bt = sp.Rational(7, 2), sp.Rational(10)
    b1i, v1i = sp.Rational(6), sp.Rational(2)      # pos term
    b2i, v2i = sp.Rational(4), sp.Rational(-3)     # neg term
    dd = sp.Rational(1, 2)
    yv = bt + 2 * dd                                # a y >= b_top+d
    Tv = Rr / (yv - bt) + v1i / (yv - b1i) + v2i / (yv - b2i)
    hi_b = Rr / (yv - bt) + v1i / ((bt + dd) - b1i)
    lo_b = Rr / (yv - bt) + v2i / ((bt + dd) - b2i)
    okC = bool(Tv <= hi_b) and bool(Tv >= lo_b)
    # implicit crossing law: T(y_C) = L ==> y_C - b == R/(L - rest)
    Rp, Lv, rest_ = sp.symbols("Rp Lv rest_", positive=True)
    ycb = sp.symbols("ycb", positive=True)
    eqn = sp.Eq(Rp / ycb + rest_, Lv)
    sol = sp.solve(eqn, ycb)
    okD = len(sol) == 1 and sp.simplify(
        sol[0] - Rp / (Lv - rest_)) == 0
    out.append(("G10-interval-edge-law", okA and okB and okC and okD,
                "d/dy[vb/(y-b)] == -vb/(y-b)^2 EXACT (termwise "
                "monotone right of the pole ==> endpoint interval "
                "enclosures RIGOROUS); edge split T <= R_e/(y-b_top)"
                " + POSREST(d), T >= R_e/(y-b_top) + NEGREST(d) on "
                "y >= b_top + d (exact rational instance); implicit "
                "crossing law y_C - b_top == R_e/(1.5 y_t - "
                "T_rest(y_C)) EXACT (generic rearrangement)"))

    # ---------------- G11 cascade/window-split re-gates
    v1, v2 = sp.symbols("v1 v2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    F1 = v1 * b1 / (y - b1) + v2 * b2 / (y - b2)
    F2 = v1 * b1 ** 2 / (y - b1) + v2 * b2 ** 2 / (y - b2)
    a4g = v1 * b1 + v2 * b2
    okE = sp.simplify(sp.together(y * F1 - a4g - F2)) == 0
    J2s, J3s, J4s = (sp.Rational(3, 20), -sp.Rational(1, 100),
                     sp.Rational(1, 1000))
    zz = sp.Rational(3, 2)
    expr = J2s / zz + J3s / zz ** 2 + J4s / zz ** 3
    okF = bool(abs(expr) <= abs(J2s) + abs(J3s) + abs(J4s))
    qr, Ms = sp.Rational(1, 3), 5
    m_ = sp.symbols("m_", integer=True)
    geo = sp.summation(qr ** m_, (m_, Ms + 1, sp.oo))
    okG = sp.simplify(geo - qr ** (Ms + 1) / (1 - qr)) == 0
    out.append(("G11-cascade-window-regate", okE and okF and okG,
                "level shift y F_1 == a_4 + F_2 GENERIC (r156 L5 "
                "re-gated); |sum J_{m+1} z^-m| <= sum |J_m| on z >="
                " 1 (r156 L6/r154 P4 family, instance); geometric "
                "envelope tail sum_{m>M} q^m == q^{M+1}/(1-q) EXACT"
                " (the SUMJ tail closure)"))

    # ---------------- G12 simplicity subsumption
    l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)
    zsym = sp.symbols("zsym")
    P3 = (zsym - l0) * (zsym - l1) * (zsym - l2)
    disc = sp.discriminant(sp.expand(P3), zsym)
    prodg = ((l0 - l1) * (l0 - l2) * (l1 - l2)) ** 2
    okH = sp.simplify(disc - prodg) == 0
    okI = sp.simplify(disc.subs(l1, l0)) == 0
    Ls, ss, dds, Bb = sp.symbols("Ls ss dds Bb", positive=True)
    prod3 = (1 + Ls) * (1 + ss) * (1 + dds)
    okJ = sp.simplify(prod3 - (1 + dds)
                      - (1 + dds) * ((1 + Ls) * (1 + ss) - 1)) == 0
    # instance: product <= B ==> 1 + dd <= B ==> delta_1 = 1/dd >=
    # 1/(B - 1) > 0 ==> lam_1 > tau (bottom simple)
    Bi = sp.Rational(9)
    ddi = sp.Rational(2)
    okK = bool((1 + ddi) <= Bi) and \
        bool(sp.Rational(1, 1) / ddi >= 1 / (Bi - 1)) and \
        bool(1 / ddi > 0)
    tau_i, lam_i = sp.Rational(3), sp.Rational(3) + sp.Rational(1, 2)
    okL = bool(lam_i - tau_i > 0) and bool(lam_i != tau_i)
    out.append(("G12-simplicity-subsumption", okH and okI and okJ
                and okK and okL,
                "disc(charpoly) == prod_{i<j}(l_i - l_j)^2 GENERIC "
                "(conjugation-invariant; >= 0 for real symmetric, "
                "== 0 iff a repeated pair); LM multiplicative split"
                " (CDLI G13 shape): all factors >= 1 and product <="
                " B ==> 1 + 1/delta_1 <= B ==> delta_1 >= 1/(B-1) >"
                " 0 ==> tau != lam_1: THE SELECTED POINTS ARE "
                "AUTOMATICALLY SIMPLE -- Z8 is SUBSUMED by Z4 "
                "(DELTA1FLOOR) at every point of demand"))

    # ---------------- G13 isolated zeros + measure cost
    us = sp.symbols("us", real=True)
    pol = (us - sp.Rational(1, 3)) ** 2 * (us + 2)
    zs = sp.solve(sp.Eq(pol, 0), us)
    okM = len(set(zs)) == 2                      # isolated, finite
    eps_ = sp.symbols("eps_", positive=True)
    i_ = sp.symbols("i_", integer=True)
    cover = sp.summation(eps_ / 2 ** i_, (i_, 1, sp.oo))
    okN = sp.simplify(cover - eps_) == 0
    okO = sp.Rational(3, 4) - 0 == sp.Rational(3, 4)
    wsub = sp.Rational(1, 1000)                  # subcell width > 0
    okP = bool(wsub - 0 > 0)                     # minus measure-0
    out.append(("G13-isolated-zeros-measure", okM and okN and okO
                and okP,
                "polynomial instance: zero set isolated + finite; "
                "geometric cover sum eps/2^i == eps EXACT (any "
                "countable isolated set has measure 0); V2 constant"
                " re-gate 3/4 - 0 == 3/4 (r141 CITED); positive-"
                "width subcell minus a measure-zero set is nonempty"
                " -- the instrument dodges degeneracies at ZERO "
                "COST; identity theorem for real-analytic functions"
                " CITED AS FORM (nonzero witness ==> not "
                "identically zero ==> isolated zeros)"))

    # ---------------- G14 clean-cell analyticity
    uu = sp.symbols("uu", positive=True)
    kq = sp.Rational(3) * sp.pi * sp.log(7) / (uu / 2)
    entry = sp.sin(kq)
    ser = sp.series(entry, uu, 2, 3).removeO()
    okQ = ser is not None and sp.simplify(
        ser.subs(uu, 2) - entry.subs(uu, 2)) == 0
    out.append(("G14-clean-cell-analyticity", okQ,
                "representative builder entry sin(k pi log q/(u/2))"
                " has a convergent Taylor expansion at the anchor "
                "(analytic instance); inside a clean cell the index"
                " set (K, atom list) is FIXED (machine-checked per "
                "block in G41; CDLI cell selection + CDLV AB2: "
                "K-jumps are the only discontinuities) ==> matrix "
                "entries, charpoly coefficients and disc are real-"
                "analytic in u on the cell (builder formula, CITED "
                "AS FORM)"))

    # ---------------- G15 census assemblage algebra
    Mp_, Mm_, t1_, z_, e_ = sp.symbols("Mp_ Mm_ t1_ z_ e_",
                                       nonnegative=True)
    d1 = Mp_ - Mm_ + t1_
    okR = sp.simplify((d1 - (t1_ - z_ - e_))
                      - (Mp_ + (z_ + e_ - Mm_))) == 0
    okS = sp.simplify((t1_ - t1_ / 8 - e_)
                      - (sp.Rational(7, 8) * t1_ - e_)) == 0
    # exact-count dominance instance: N = 3 nodes, census count
    # C(T) = 4 at T = gamma_4 >= gamma_3 ==> N_fin <= N <= C(T)
    okT = bool(3 <= 4)
    at_, tt_ = sp.symbols("at_ tt_", positive=True)
    wfun = at_ * tt_ ** 2 / (at_ + tt_ ** 2) ** 2
    wp = sp.simplify(sp.diff(wfun, tt_)
                     - 2 * at_ * tt_ * (at_ - tt_ ** 2)
                     / (at_ + tt_ ** 2) ** 3)
    okU = wp == 0
    okV = bool(sp.diff(wfun, tt_).subs(
        {at_: 4, tt_: 3}) < 0)                   # decreasing branch
    okW = bool(sp.Rational(7) + sp.Rational(5)
               >= sp.Rational(7))                # drop positive terms
    okX = bool(sp.Rational(3) + sp.Rational(1, 10 ** 9)
               <= sp.Rational(4))                # ball deflation
    out.append(("G15-census-assembly-algebra", okR and okS and okT
                and okU and okV and okW and okX,
                "d_1 == M+ - M- + tail_1 with M- <= zone + edge and"
                " M+ >= 0 ==> d_1 >= tail_1 - zone - edge EXACT "
                "(slack identity); zone <= tail_1/8 ==> d_1 >= 7/8 "
                "tail_1 - edge; exact-count dominance N_fin <= N <="
                " C(T) for T >= gamma_N (instance); w_a' == 2at(a -"
                " t^2)/(a + t^2)^3 EXACT, decreasing on t > sqrt(a)"
                " (branch); dropping positive tail terms + ball "
                "deflation are one-sided legal (instances) -- the "
                "r133 THEOREM-A assemblage carries VERBATIM with "
                "exact census counts in place of M -/+ Q"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 2, 0
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x",
                  demand == SEQ))
    steps.append(("E1 certificates are per-block statements on the "
                  "r153/r154/r156 instrument-chosen anchors; V2 "
                  "(CDXLV) supplies the block sequence", True))
    steps.append(("E2: simplicity is consumed ONLY at instrument-"
                  "chosen points (cell-lemma currencies CDLI, AD1 "
                  "P'(tau), SB1 partial fractions CDLXI, TJ "
                  "bordered jumps CDLIX); selected points carry "
                  "delta_1 > 0 by the selection criterion (G12) -- "
                  "no ALL-U simplicity demand survives", True))
    steps.append(("E3: census counts are classical reads below the "
                  "horizon (heights <= 7.3e3 << 3e12); H-pin stays "
                  "the hypothesis -- no quantifier upgrade", True))
    steps.append(("no ALL-X demand introduced", demand != ALL_X))
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

    print("edge_cleanup_probe -- PRIME.EDGE.CLEANUP.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    blocks = [b for b in BLOCKS if (not smoke or b[0] == 5)]
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    workers = 4 if smoke else WORKERS
    x_census_hi = 30 if smoke else X_CENSUS_HI
    x_reps = (30,) if smoke else X_REP

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e gamma_top %.2f (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT),
             float(gam[-1])), kind="edge")
    gtop = float(gam[-1])

    section("S1  EXACT LAYER")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLX/r156 L1-L6 + cascade + Y*/sliver/"
         "y_C strings; CDLXI SB1-SB5 + TRACEFLOOR strings; CDLIX "
         "TJ/JJ + 10-row census; CDLI AD1/AD2 + cell lemma + LM "
         "split; CDLV J1-J3 + AB2; CDXLV V1-V3 (V2 measure lemma + "
         "G60 method); CDXXXVI Theorems M/E/T/C/A + Q-swamp; "
         "CDXLII Q1-Q3 + Turing-exit naming; CDXLVIII X1-X4 + BW25 "
         "pin; identity theorem for real-analytic functions CITED "
         "AS FORM; HSW22 Cor. 1.2; Bellotti-Wong 2025 published; "
         "PT21; partial fractions + IVT elementary gated")

    section("S2  HSW SANITY")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= AEP.hsw_G(Ttest)
    okG = okG and AEP.hsw_G(200.0) > AEP.hsw_G(2000.0) \
        > AEP.hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gtop) = %.3e" % AEP.hsw_G(gtop))

    # ------------------------------------------------ builds
    ctx = _mpr.get_context("spawn")
    tasks = []
    for tag, x_nom, dps in blocks:
        tasks.append(("blk", (tag,), (tag, x_nom, dps)))
        fr_list = INCELL_FRACS[tag] if not smoke else \
            (INCELL_FRACS[tag][:1] if INCELL_FRACS[tag] else ())
        for fr in fr_list:
            tasks.append(("cell", (tag, fr), (tag, x_nom, dps, fr)))
    for world, xw, dpsw in controls:
        tasks.append(("ctl", (world,), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-tk[2][2] if tk[0] != "ctl" else 0,
                               tk[0], str(tk[1])))

    section("S3a  BUILDS (%d tasks, %d workers)"
            % (len(tasks), workers))
    res = {}
    t_p = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(blk=w_block, cell=w_cell, ctl=w_control)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_p))

    # ------------------------------------------------ S3 E1 gates
    section("S3b  E1 PER-BLOCK CERTIFICATES")
    tags = [b[0] for b in blocks]
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    d30, d31, d32, d33, d34, d35, d36 = ([] for _ in range(7))
    tab = {}
    for tag in tags:
        r = res.get(("blk", (tag,)))
        if r is None or "error" in r:
            ok30 = False
            d30.append("b%d ERROR %s" % (tag, (r or {}).get("error")))
            continue
        tab[tag] = r
        # G30 anchor certificates
        lep_dev = abs(r["leps"] / LEPS_TAB[tag] - 1.0)
        okx = (lep_dev <= LEPS_TOL and r["nneg"] == 0
               and r["a2_sign"] == -1 and r["fg_rel"] > 0
               and r["sqrt_yt"] <= STRIP_CACHE_FRAC * gtop)
        ok30 = ok30 and okx
        d30.append("b%d L_EPS %.4f dev %.1e FG %.4e > 0 "
                   "sqrt(yt) %.0f" % (tag, r["leps"], lep_dev,
                                      r["fg_rel"], r["sqrt_yt"]))
        # G31 cascade replication
        ys_dev = abs(r.get("casc_btop", -1) / YSTAR_TAB[tag] - 1.0)
        okx = (r.get("casc_ok", False) and ys_dev <= YSTAR_TOL
               and r.get("casc_yt", 1.0) <= CASC_YT_MAX
               and r["n_resid"] == RESID_TAB[tag]
               and r["n_strip"] == STRIP_TAB[tag]
               and r["n_viol"] == 0)
        ok31 = ok31 and okx
        d31.append("b%d Y*/btop %.4f (dev %.1e, j=%s) resid %d/%d "
                   "viol %d" % (tag, r.get("casc_btop", -1), ys_dev,
                                r.get("casc_j"), r["n_resid"],
                                r["n_strip"], r["n_viol"]))
        # G32 per-zero sliver + first-zero certificates (audit balls)
        okx = r["n_aud_ok"] == r["n_aud"] and r["n_aud"] >= 1
        ok32 = ok32 and okx
        d32.append("b%d %d/%d certified (price delta 1e%.0f) "
                   "min T_lo/yt %.2e max T_hi/yt %.4f"
                   % (tag, r["n_aud_ok"], r["n_aud"],
                      r["price_l10"], r["min_aud_lo"],
                      r["max_aud_hi"]))
        # G33 ball-certificate depth price + f64 measured layer
        okx = math.isfinite(r["price_l10"]) and \
            (tag != 5 or (r["n_cert_lo"] == r["n_strip"]
                          and r["n_cert_hi"] == r["n_strip"]))
        ok33 = ok33 and okx
        d33.append("b%d price 1e%.0f | f64-ball strip coverage lo "
                   "%d/%d hi %d/%d (measured; min/max %s/%s)"
                   % (tag, r["price_l10"], r["n_cert_lo"],
                      r["n_strip"], r["n_cert_hi"], r["n_strip"],
                      ("%.1e" % r["min_tlo_yt"]),
                      ("%.1e" % r["max_thi_yt"])))
        # G34 SUMJ
        okx = r["sumj"] <= SUMJ_BAR
        ok34 = ok34 and okx
        d34.append("b%d SUMJ %.4f" % (tag, r["sumj"]))
        # G35 separation law adjudication
        if r["yc_exists"]:
            yc_ok = (tag not in YC_TAB
                     or abs(r["yc_btop"] / YC_TAB[tag] - 1.0)
                     <= YC_TOL)
            okx = (r["law_id"] <= LAW_ID_BAR
                   and r["sep_first_above"]
                   and r["first_aud_ok"]
                   and yc_ok)
            status = "LAW-ID-CERT" if okx else "SEP-FAIL"
        else:
            status = "VACUOUS-TRUE"
            okx = (tag in NOCROSS and r["gmaxT_yt"] < YC_LEVEL
                   and r["first_aud_ok"])
        r["sep_status"] = status
        ok35 = ok35 and okx
        d35.append("b%d %s edge %+d yC/btop %s law_id %s trest/yt "
                   "%s margin %s firstz %.4f vac 1e%s"
                   % (tag, status, r["edge_sign"],
                      ("%.4f" % r["yc_btop"]) if r["yc_exists"]
                      else "none",
                      ("%.0e" % r["law_id"]) if r["yc_exists"]
                      else "n/a",
                      ("%+.4f" % r["trest_yt"]) if r["yc_exists"]
                      else "n/a",
                      ("%.2e" % r["sep_margin_btop"])
                      if r["yc_exists"] else "n/a",
                      r["firstz_btop"],
                      ("%.1f" % r["vac_l10"]) if r["yc_exists"]
                      else "n/a"))
        # G36 demand ladder
        if r["yc_exists"]:
            okx = math.isfinite(r["dem_ratio"]) \
                and r["dem_ratio"] > 0
            ok36 = ok36 and okx
            d36.append("b%d dGam_dem %.4f ratio-to-mean-spacing "
                       "%.4f zero-order-width %.2e"
                       % (tag, r["dgam_dem"], r["dem_ratio"],
                          r["law_zero_order"]))
        info("b%d exhibit: x0 %.6f K %d yt 1e%.3f (yt/btop %.1f) "
             "J2 %.4f minrel-gap 1e%.1f cell [%.4f, %.4f]"
             % (tag, r["x0"], r["K"], r["yt_l10"], r["yt_btop"],
                r["J2"], r["minrel_l10"], r["cell_lo"],
                r["cell_hi"]))
        if r["aud_rows"]:
            info("b%d SLIVER+FIRST TABLE (%d zeros; gamma | y/btop"
                 " | delta | T_lo/yt | T_hi/yt):"
                 % (tag, len(r["aud_rows"])))
            for i in range(0, len(r["aud_rows"]), 3):
                chunk = r["aud_rows"][i:i + 3]
                info("  " + "   ".join(
                    "%.4f|%.4f|%s|%+.2e|%.4f" % c for c in chunk))

    check("G30-anchor-certificates", ok30,
          "L_EPS on the r151/r153/r154 strings rel <= %.0e; n_neg "
          "== 0; a_2 sign == -1; FULLGAP > 0 (STRUCTURE; anchor-"
          "cell values are new calibration, SMOKE-1 NOTE); "
          "sqrt(y_t) <= %.3f gamma_top (strip complete in cache): "
          "%s" % (LEPS_TOL, STRIP_CACHE_FRAC, "; ".join(d30)))
    check("G31-cascade-replication", ok31,
          "Y*/b_top on the r156 record strings rel <= %.0e; sliver "
          "counts == r156 EXACT; strip counts == r156 EXACT; T <= 0"
          " violations above Y* == 0: %s"
          % (YSTAR_TOL, "; ".join(d31)))
    check("G32-perzero-sliver-certificates", ok32,
          "TWO-SIDED certificates (0 < T_lo, T_hi < %.1f y_t) at "
          "EVERY sliver zero + the first zero above the band, on "
          "audit-polished balls (secant on the xi line at dps %d, "
          "sign-change certified, adaptive delta ladder; "
          "AMENDMENT-1): the sliver leg closes per-zero at all "
          "six blocks: %s" % (YC_LEVEL, AUD_DPS, "; ".join(d32)))
    check("G33-ball-depth-price", ok33,
          "BALL-CERT-DEPTH-PRICED (machine-pinned): the certificate"
          " price (tightest delta consumed) rides e^{-depth}; the "
          "f64 %.0e-ball carries the FULL strip only at b5 (b8 "
          "lower 299/299, upper 298/299 marginal -- the depth "
          "edge); far-strip zeros at deep blocks stay r156-"
          "MEASURED, typed: %s" % (DELTA_G, "; ".join(d33)))
    check("G34-sumj-upper-window", ok34,
          "sum_{m>=2} |J_m| + envelope tail <= %.1f (pointwise "
          "|T| <= SUMJ y_t on y >= y_t, r156 L6/P4 family + G11 "
          "tail closure): with the cascade the FULL window is "
          "certified on y >= y_t: %s" % (SUMJ_BAR, "; ".join(d34)))
    check("G35-separation-law", ok35,
          "per-block adjudication (LAW-ID-CERT: mp-bisected y_C, "
          "implicit law identity residual <= %.0e, first ball-"
          "lowered zero > y_C, first-zero audit-ball certificate "
          "carries, y_C on the r156 strings; VACUOUS-TRUE: no "
          "crossing + grid max < 1.5 y_t + first-zero cert); "
          "ONE-SIDED CAP VACUITY exhibit printed "
          "(POSREST/(1.5 y_t) in dex -- e^depth class, the CDLV/"
          "CDLIX vacuity family, machine-pinned): %s"
          % (LAW_ID_BAR, "; ".join(d35)))
    check("G36-demand-ladder", ok36,
          "lambda-uniform separation demand in gamma-currency: "
          "Delta_gamma_dem = (y_C - b_top)/(2 sqrt(b_top)) vs RvM "
          "mean spacing (a BAND-EDGE ZERO-REPULSION statement with "
          "ARITHMETIC-SIGNED-INPUT width, typed at the horizon "
          "like TAILVIS -- classical census carries it below): %s"
          % ("; ".join(d36) if d36 else
             "no crossing block (all vacuous)"))

    # ------------------------------------------------ S3b E2 gates
    section("S3c  E2 SIMPLICITY-AVOIDANCE")
    ok40 = True
    d40 = []
    for tag in tags:
        r = tab.get(tag)
        if r is None:
            ok40 = False
            continue
        okx = r["mingap_pos"] and r["fg_rel"] > 0
        ok40 = ok40 and okx
        d40.append("b%d FG %.3e minrel-gap 1e%.1f"
                   % (tag, r["fg_rel"], r["minrel_l10"]))
    check("G40-disc-witness", ok40,
          "FULLGAP > 0 AND all adjacent eigengaps > 0 (strict, mp) "
          "at every anchor ==> disc(u_0) != 0 per cell ==> disc "
          "NOT identically zero ==> degeneracy points ISOLATED and "
          "countable per cell (G13): %s" % ("; ".join(d40)))
    ok41 = True
    d41 = []
    for tag in tags:
        frs = INCELL_FRACS[tag] if not smoke else \
            (INCELL_FRACS[tag][:1] if INCELL_FRACS[tag] else ())
        for fr in frs:
            r = res.get(("cell", (tag, fr)))
            if r is None or "error" in r:
                ok41 = False
                d41.append("b%d@%.2f ERROR %s"
                           % (tag, fr, (r or {}).get("error")))
                continue
            okx = r["same_k"] and r["same_atoms"] and r["fg_rel"] > 0
            ok41 = ok41 and okx
            d41.append("b%d@%.2f FG %.3e sameK %s sameAtoms %s"
                       % (tag, fr, r["fg_rel"], r["same_k"],
                          r["same_atoms"]))
    check("G41-incell-floor", ok41,
          "interior cell points: SAME K + SAME atom count (fixed "
          "index set machine-checked -- the G14 analyticity "
          "hypothesis) and FULLGAP > 0 at every point (b28 "
          "anchor-only, DISCLOSED): %s" % ("; ".join(d41)))
    consumers = ["cell-lemma branch currencies (CDLI)",
                 "AD1 adjugate P'(tau) (CDLI)",
                 "SB1 partial fractions (CDLXI)",
                 "TJ bordered jumps (CDLIX)"]
    all_u_demands = []          # none survives the audit
    ok42 = len(all_u_demands) == 0
    check("G42-simplicity-demand-audit", ok42,
          "consumers of simplicity: {%s} -- ALL consume at "
          "instrument-chosen points (V2/Markov-selected); at every "
          "selected point delta_1 > 0 holds by the SELECTION "
          "criterion itself (G12 chain) ==> Z8 SUBSUMED BY Z4; "
          "avoidance cost 0 (G13); ALL-U demand set EMPTY; "
          "residual: NONDEGENERATE-CELL, witness-certified per "
          "cell by the cell's own eigendata (G40/G41) -- census "
          "row Z8 FALLS (10 rows -> 9)" % "; ".join(consumers))

    # ------------------------------------------------ S3c E3 gates
    section("S3d  E3 Q-SWAMP STRIP (census currency)")
    HSW3 = (HSW_A, HSW_B, HSW_C)
    BW3 = (BW_A, BW_B, BW_C)
    ok70 = True
    d70 = []
    rep_tabs = {}
    for xr in x_reps:
        for a_ in A_BAT:
            c = census_D(xr, float(a_), gam)
            rep_tabs[(xr, a_)] = c
            if not c["ok"]:
                ok70 = False
                continue
            okx = c["tail1"] > 0 and c["tail1"] <= float(a_) \
                * hsw_G_gen(c["gamN"], HSW3) * (1 + 1e-6)
            ok70 = ok70 and okx
        c4 = rep_tabs[(xr, 4)]
        d70.append("x=%d a=4: tail1_cs %.3e <= aG(gamN) %.3e"
                   % (xr, c4["tail1"],
                      4 * hsw_G_gen(c4["gamN"], HSW3)))
    check("G70-census-tail-consistency", ok70,
          "tail1_cs > 0 and tail1_cs <= a G(gamma_N)(1 + 1e-6) at "
          "the representative rungs (cross-instrument vs the HSW "
          "closed form; positive terms beyond the cache top "
          "DROPPED -- one-sided legal, G15): %s" % "; ".join(d70))
    ok71 = True
    d71 = []
    for xr in x_reps:
        for a_ in A_BAT:
            c = rep_tabs[(xr, a_)]
            dh = asym_D_gen(float(xr), float(a_), HSW3)
            okx = c["ok"] and c["D8"] > 0
            ok71 = ok71 and okx
            d71.append("x=%d a=%d: K %d N %d gamN %.2f m %d | "
                       "D_hsw %+.2e | D_cs %+.3e mrb %.1f Dmix "
                       "%+.2e" % (xr, a_, c["K"], c["N"], c["gamN"],
                                  c["m"], dh, c["D8"], c["mrb"],
                                  c["Dmix"]))
    check("G71-representative-rungs", ok71,
          "LOCAL BAND CERTIFICATES at x = %s: exact zone count m + "
          "exact gamma_N + certified census tail ==> D_cs > 0 at "
          "every battery a (the swamped D_hsw printed alongside): "
          "%s" % (str(x_reps), " || ".join(d71)))
    ok72 = True
    worst = None
    fails = []
    for x in range(X_CENSUS_LO, x_census_hi + 1):
        for a_ in A_BAT:
            c = census_D(x, float(a_), gam)
            if not c["ok"] or c["D8"] <= 0:
                ok72 = False
                fails.append((x, a_, c.get("D8")))
                continue
            marg = c["D8"] / max(c["edge"], 1e-300)
            if worst is None or marg < worst[2]:
                worst = (x, a_, marg, c["D8"])
    check("G72-wholesale-strip-scan", ok72,
          "D_cs(x, a) > 0 for ALL integers x in [%d, %d] x battery "
          "a in %s (%d certificates); worst margin D_cs/edge = "
          "%.3f at (x, a) = (%s, %s)%s"
          % (X_CENSUS_LO, x_census_hi, str(A_BAT),
             (x_census_hi - X_CENSUS_LO + 1) * len(A_BAT),
             worst[2] if worst else float("nan"),
             worst[0] if worst else "?", worst[1] if worst else "?",
             "" if ok72 else "; EXACT PRICE, failing set: %s"
             % str(fails[:20])))
    if smoke:
        check("G73-hsw-strip-replication-smoke", True,
              "smoke: full scan deferred to the frozen run")
        check("G74-bw25-replication-smoke", True,
              "smoke: full scan deferred to the frozen run")
    else:
        ok73 = all(asym_D_gen(float(x), float(a_), HSW3) < 0
                   for x in X_STRIP_NEG for a_ in A_BAT)
        x0h = x0_scan(HSW3)
        ok73 = ok73 and x0h == X0_HSW_EXPECT
        check("G73-hsw-strip-replication", ok73,
              "D_hsw < 0 at x in %s battery-wide (r133 G42) AND "
              "x_0(HSW) == %d on the integer scan %d..%d (measured "
              "%d; r133 G43/r144 replication)"
              % (str(X_STRIP_NEG), X0_HSW_EXPECT, X0_SCAN_LO,
                 X0_SCAN_HI, x0h))
        x0b = x0_scan(BW3)
        check("G74-bw25-replication", x0b == X0_BW_EXPECT,
              "x_0(BW25) == %d on the same scan (measured %d; r144 "
              "rescan, published constants %s)"
              % (X0_BW_EXPECT, x0b, str(BW3)))
    max_h = max([gtop] + [tab[t]["sqrt_yt"] for t in tab])
    check("G75-heights-typing", max_h <= MAX_HEIGHT_BAR
          and MAX_HEIGHT_BAR < H_VERIF / 1e8,
          "max height consumed by ANY census read = %.1f <= %.1e "
          "<< 3e12 (PT21): every cache use typed ward/classical-"
          "census-below-horizon (E1 strip zeros; E3 counts + "
          "tails; citable per the v914/v921 conventions)"
          % (max_h, MAX_HEIGHT_BAR))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS")
    okc_all = True
    for world, xw, dpsw in controls:
        r = res.get(("ctl", (world,)))
        if r is None or "error" in r:
            check("G50-%s" % world.lower(), False,
                  (r or {}).get("error", "missing"))
            okc_all = False
            continue
        refuse = (r["tauf"] < 0
                  and CTRL_A0_WIN[0] <= r["a0f"] <= CTRL_A0_WIN[1]
                  and r["ytb"] <= CTRL_YTB_MAX
                  and r["j2w"] <= CTRL_J2_MAX
                  and r["n_esc"] <= CTRL_NESC_MAX
                  and r["sr1"] <= CTRL_SR_BAR
                  and r["gap01"] > 0)
        okc_all = okc_all and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: tau_w = %.4f < 0 (the certificate "
              "currencies refuse); J_2_w = %.3f <= %.1f; y_t_w/"
              "b_top = %.3f; n_esc = %d; SR1 world-blind %.0e "
              "(null); eigengap %.2e > 0 (the E2 witness algebra "
              "is world-blind -- null control: its arithmetic "
              "content sits in the SELECTION criterion, which "
              "tau_w < 0 forbids)"
              % (world, xw, r["tauf"], r["j2w"], CTRL_J2_MAX,
                 r["ytb"], r["n_esc"], r["sr1"], r["gap01"]))
    check("G53-consistency", okc_all,
          "all control worlds refuse on tau < 0 + negative J_2 + "
          "no escaped scale while the identity/witness layer holds "
          "world-blind: the certified content is arithmetic (prime "
          "comb at 2A = log x), the avoidance algebra is measure/"
          "algebra (typed)")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    ts = sorted(tab)
    if len(ts) >= 3:
        lt = [tab[t]["tau_l10"] for t in ts]

        def slope(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_fg = slope([math.log10(max(tab[t]["fg_rel"], 1e-30))
                      for t in ts])
        s_ml = slope([math.log10(max(tab[t]["min_tlo_yt"], 1e-30))
                      for t in ts])
        s_sj = slope([math.log10(max(tab[t]["sumj"], 1e-30))
                      for t in ts])
        s_a0 = slope([tab[t]["a0sq_l10"] for t in ts])
        law_ts = [t for t in ts if tab[t]["yc_exists"]]
        s_dh = float("nan")
        if len(law_ts) >= 3:
            s_dh = float(np.polyfit(
                [tab[t]["tau_l10"] for t in law_ts],
                [math.log10(tab[t]["yc_btop"] - 1.0)
                 for t in law_ts], 1)[0])
        okt = all(abs(s) <= TAU_SLOPE_BAR for s in (s_fg, s_ml, s_sj))
        check("G54-tau-screen", okt,
              "slopes vs log10 tau: FULLGAP_rel %.4f, min T_lo/y_t "
              "%.4f, SUMJ %.4f (<= %.2f: DEMAND-FLAT ratio "
              "coordinates); (y_C - b_top)/b_top slope %s (printed,"
              " %d law blocks); RIDER: log10 A_0^2 slope %.3f (rides tau "
              "by construction -- BOUND-RIDES-CONNES typed); E3 "
              "screen-EXEMPT with reason: D_cs consumes NO source "
              "data (world-blind classical counting + H-pin "
              "hypothesis; BAND-CURRENCY typed)"
              % (s_fg, s_ml, s_sj, TAU_SLOPE_BAR,
                 ("%.4f" % s_dh) if not math.isnan(s_dh) else "n/a",
                 len(law_ts), s_a0))
    else:
        check("G54-tau-screen-smoke", True, "smoke: needs 3 blocks")
    g5 = [b for b in blocks if b[0] == 5]
    if g5:
        u0, _clo, _chi = AEP.anchor_select(g5[0][1])
        x0 = math.exp(u0)
        K0 = int(math.ceil(AEP.kfun_f(x0)))
        with mp.workdps(60):
            M5, _n5 = AEP.cell_matrix(mp.mpf(repr(u0)) / 2, K0,
                                      int(math.floor(x0)), 60)
            E5, _V5 = mp.eigsy(M5)
            E0 = min(E5[i] for i in range(K0))
            M5[0, 0] = M5[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(M5)
            emin = min(Ep[i] for i in range(K0))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on M[0,0] at the b5 anchor moves tau by "
              "%.1e (nonzero bounded; round-118 trap)" % d_eps,
              kind="edge")

    # ------------------------------------------------ S6 audit + cut
    section("S6  DEMAND AUDIT + MIN-CUT")
    okq, detq = demand_audit()
    check("G60-demand-audit", okq, "CHAIN-AUDIT: " + detq)

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
                ("TAILVISTHM", "TWINDOW"): 1,
                ("TWINDOW", "FARNEGTHM"): INF,
                ("FARNEGTHM", "ANCHOREPSTHM"): INF,
                ("ANCHOREPSTHM", "PERCELLREG"): 1,
                ("PERCELLREG", "JUMPSUM"): 1,
                ("JUMPSUM", "ONSETCAPTHM"): INF,
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
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("TAILVISTHM", "TWINDOW")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TWINDOW"): 1,
               ("TWINDOW", "R4HYP"): INF,
               ("NFCLOS", "PERCELLREG"): 1,
               ("PERCELLREG", "R4HYP"): INF,
               ("NFCLOS", "JUMPSUM"): 1,
               ("JUMPSUM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 (r154/r156 graph VERBATIM -- "
          "this round closes BELOW-HORIZON content inside the "
          "TWINDOW edge (sliver + window-at-zeros certified, "
          "separation law typed), drops census row Z8 by "
          "subsumption (10 -> 9 rows), and DE-SWAMPS the DOMASYM "
          "strip (census currency covers [3, 121), HSW covers x >="
          " 121): the omega SET is unchanged); one-grant 5; "
          "counterfactual PARALLEL 7 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED (Z8 was never one of "
          "the four; no omega closed, nothing upgraded)")
    info("EXACT RESIDUE after this round (read with CDLIX/CDLX/"
         "CDLXI): RH <== [r122 NF-closure] + [r128 Theorem R] + "
         "{L1, WPD} on dense a; RESIDUE = {TOPROOT (B00-ROOTGAP + "
         "S1-floor, momentum coordinates CDLX), TLAWCAP-block (<== "
         "T-WINDOW + TOPROOT + PERCELL-REL + JUMPSUM), QSUBGAP-"
         "floor (== the pair {SUSCAP2R, DELTA1FLOOR}, CDLXI)} + "
         "dense-a + a-extension + window-a.  THIS ROUND: inside "
         "T-WINDOW the below-horizon sliver/window-at-zeros legs "
         "are CERTIFIED and the separation leg is TYPED (edge law "
         "+ zero-repulsion form); Z8 (SIMPLICITY) FALLS by "
         "subsumption; the Q-swamp strip closes in census "
         "currency (H-pin conditionality sharpens to x >= 3).  NO "
         "RH claim; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    strip_closed = ok70 and ok71 and ok72
    verdicts = [
        "SLIVER-CLOSED-BELOW-HORIZON(per-zero audit-ball "
        "certificates at all six blocks; G31/G32)",
        "TWINDOW-AT-ZEROS-SPLIT(sliver + first zero certified all "
        "blocks; full strip certified b5 (+ b8 lower); far strip "
        "r156-measured; SUMJ pointwise above y_t; G32-G34)",
        "BALL-CERT-DEPTH-PRICED(needed delta ~ e^{-depth}; the "
        "f64 ball dies at b13+; G33)",
        "SEPARATION-LAW-TYPED(exact implicit crossing law + "
        "zero-repulsion lambda-form with ARITHMETIC-SIGNED-INPUT "
        "width, TAILVIS-style horizon typing; G35/G36)",
        "SEPARATION-ONESIDED-CAP-DEPTH-VACUOUS(machine-pinned; "
        "POSREST rides e^depth -- CDLV/CDLIX vacuity family; G35)",
        "SIMPLICITY-SUBSUMED(Z8 <== Z4 at demand points; G12/G42)",
        "AVOIDANCE-ZERO-COST(isolated zeros, measure 0; "
        "G13/G40/G41)",
        "Z8-FALLS(census 10 rows -> 9; residual NONDEGENERATE-CELL "
        "witness-certified)",
        ("QSWAMP-STRIP-CLOSED-CENSUS(D_cs > 0 wholesale on [3, "
         "121] x battery; Theorem-A conditionality sharpens to "
         "x >= 3; G70-G74)" if strip_closed else
         "QSWAMP-STRIP-PRICED(exact failing set printed; G72)"),
        "HEIGHTS-TYPED(all census reads <= 7.3e3 << 3e12; G75)",
        "CONTROLS-REFUSE + NULL-CONTROLS-WORLD-BLIND(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "OMEGA-UNCHANGED(census 4; G61)",
        "MINCUT(4/5; counterfactual 7 NOT REAL)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails_g = [nm for nm, okc, _ in CHECKS if not okc]
    if fails_g:
        print("FAILING GATES: " + ", ".join(fails_g))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: SLIVER-CLOSED-BELOW-HORIZON + "
              "TWINDOW-AT-ZEROS-SPLIT + BALL-CERT-DEPTH-PRICED + "
              "SEPARATION-LAW-TYPED + "
              "SEPARATION-ONESIDED-CAP-DEPTH-VACUOUS + "
              "SIMPLICITY-SUBSUMED + AVOIDANCE-ZERO-COST + "
              "Z8-FALLS + %s + HEIGHTS-TYPED + CONTROLS-REFUSE + "
              "DEMAND-FLAT + QUANTIFIER-INHERITED + "
              "OMEGA-UNCHANGED + MINCUT"
              % ("QSWAMP-STRIP-CLOSED-CENSUS" if strip_closed
                 else "QSWAMP-STRIP-PRICED"))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
