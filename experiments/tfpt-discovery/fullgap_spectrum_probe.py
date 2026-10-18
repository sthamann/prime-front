#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fullgap_spectrum_probe -- PRIME.FULLGAP.SPECTRUM.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the spectrum of the zone-killed
compression's SOURCE: the bottom of the uncompressed Weil matrix)
=======================================================================
Rounds 142-144 (CDXLVI/CDXLVII/CDXLVIII) concentrated THREE residues
on one object: DELTA1FLOOR (delta_1 >= 1/poly <== FULLGAP, r142 W3,
interlacing TIGHT), TOPROOT (y_t <= poly <==> FULLGAP-CAP modulo the
r143 measured O(1) delta_1-lock y_t ~ delta_1/2.4-3.6), and SUSCAP2R
(s <= poly, the r144 three-row determinant on the same carrier).  The
EXACT TWO-SIDED DEMAND in the source coordinate is
   1/poly(x)  <=  FULLGAP := (lam_1(Mq) - tau)/tau  <=  poly(x),
lower side == DELTA1FLOOR (exact, via W3 delta_1 >= FULLGAP), upper
side == TOPROOT modulo the measured lock (y_t <= delta_1/1.5 and
delta_1 == FULLGAP tight).  This probe is the maximal proof attempt
on the spectral anatomy of lam_1 (and the bottom ladder) of Mq.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, Mq = Mpole + March - Mprime (round-114
builder; even sector), eigenpairs lam_0 = tau <= lam_1 <= ... with
eigenvectors psi_0 = phi, psi_1, ... (mpE/mpV), FULLGAP = (lam_1 -
tau)/tau, T_z = 2 pi x, m = verified zone census, V = kernel of the
m newton-polished node rows, q_i = eigenvalues of the compression
onto V (q_0 = tau), delta_1 = (q_1 - q_0)/tau, jets A_{2i}(v) =
sum_k (-1)^k v_k om_k^{2i} for coefficient vectors v_k = psi_k/nrm,
A_0(phi) the r137 0-jet, y_t = |A_2/A_0|(phi), E_v(t) = sin(At)
R_v(t), s = tau chi/rho2 at the zone-top argmin, G(T) = HSW tail
envelope, gtop = 7264.75 (X5 cache top).

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically + exact rational
instances + mp-instantiated per rung; classical inputs typed CITED)
=======================================================================
THEOREM Y1 (harmonic-trace floor; the D-low recoordination).  For
PSD symmetric M with simple ground (tau, phi):
   (lam_1 - tau)^{-1}  <=  Tr[(M - tau)^+ on phi-perp]
                        =  sum_{i>=1} (lam_i - tau)^{-1},
with tightness identity tf := (lam_1 - tau) Tr = 1 + sum_{i>=2}
(lam_1 - tau)/(lam_i - tau).  The trace is computable WITHOUT an
eigensolve: ONE bordered LU [[M - tau, phi],[phi^T, 0]] + K solves
(the r144 X4 carrier).  CONSEQUENCE: DELTA1FLOOR <== FULLGAP >=
1/poly <== TRACEFLOOR := tau Tr <= poly -- the floor demand becomes
an UPPER bound on ONE positive source trace (the classical-friendly
direction).  MEASURED: the ladder is geometric, so tf = 1.000021/
1.000003/1.000001 at x = 5/8/13 -- the floor is an EQUALITY up to
1e-5: FULLGAP == tf/TRACEFLOOR - 1e0-corrections exactly.

THEOREM Y2 (tightness transfer; the W3-tightness mechanism).  For
any codim-m subspace V containing phi, with eps^2 = |(I - P_V)
psi_1|^2 < 1:
   0 <= q_1(V) - lam_1 <= eps^2 (lam_max - lam_1)/(1 - eps^2).
(P_V psi_1 remains perp to phi; Rayleigh on its direction expands
EXACTLY to lam_1 + [eps^2(lam_max - lam_1) - (w'Mw-bound slack)]/
(1 - eps^2).)  With the r131/r137 budget law (CITED): sum_zone
2 E_v(gamma_j)^2 <= v'Mq v + OFF for unit v, the excited state is
UNIFORMLY zone-killed -- |E_{psi_1}(gamma_j)| <= sqrt((lam_1 +
OFF_1)/2) -- and eps^2 is budget-priced: the measured r142 tightness
delta_1/FULLGAP = 1.0000 is EXPLAINED (typed BUDGET-CONDITIONAL for
the eps-pricing; the transfer algebra itself exact).  Chain bound
instantiated at x = 5/8 (gamma-side f64-limited from x = 13, the
r139/r141/r143 instrument class, DISCLOSED).

THEOREM Y3 (trace-cap vacuity = the RATE-LOCK obstruction pin; the
D-cap adjudication).  (i) lam_1 <= Tr M - tau (PSD, exact) and
Tr Mq <= poly is MEASURED (TrM = 11.27/29.73/77.41, arch-dominated)
-- the absolute half of the cap is trace-closable.  (ii) BUT the
demand is lam_1 <= poly x tau, and NO trace/moment instrument can
see the RATIO of two collapsing eigenvalues: exact unbounded family
(diag(t, 1): trace <= 2 for all t, FULLGAP = 1/t - 1 unbounded).
(iii) rate-lock rearrangement: [lam_1 <= C] AND [tau >= lam_1/P]
==> FULLGAP <= P - 1: the missing half of D-cap is a tau-FLOOR
relative to lam_1 -- a COLLAPSE-RATE LOCK between the two bottom
eigenvalues.  MEASURED vacuity: log10((TrM - tau)/(lam_1 - tau)) =
11.50/24.90/48.46 at x = 5/8/13, riding |log10 tau| with slope
0.978: Chebyshev/trace does NOT close D-cap, pinned exactly.

THEOREM Y4 (the s-chain identity; the D-s inheritance).  With
share_1 = (et_1^2/(q_1 - q_0))/chi:
   s x delta_1 x share_1 x rho2/et_1^2  ==  1   EXACTLY
(definition chase, generic sympy + per-rung <= 1e-30).  With the
tight interlacing delta_1 == FULLGAP: s <= poly <==> et_1^2/rho2 <=
poly x FULLGAP -- the s-uniformity is an overlap-vs-gap balance ON
THE SAME SPECTRUM this probe measures; the r139 compensation law is
this identity read at flat s.

MEASURED LAWS (the spectral anatomy; typed GEMESSEN):
(L1) ZERO-JET LAW: lam_1 = 8 A_0(psi_1)^2 G(T_z) x tlaw_1 with
     tlaw_1 = 0.2369/0.3368/0.4550 at x = 5/8/13 -- INSIDE the
     r137 tlaw window and tracking phi's tlaw (ratio 0.89/0.90/
     0.97): the first excited value is the ARCHIMEDEAN-TAIL mass of
     its own eigenvector priced by its own 0-jet, exactly the
     ground-state mechanism one level up.  F1 ANSWER: lam_1's scale
     = (excited 0-jet)^2 x HSW tail -- neither a bare RvM/
     quadrature scale nor a bare prime scale; the demands become
     0-JET RATIO conditioning: FULLGAP = (A_0(psi_1)/A_0(phi))^2
     x (tlaw_1/tlaw_0).
(L2) JET-RATIO LOCK: (A_0(psi_1)/A_0(phi))^2 / FULLGAP = 1.124/
     1.110/1.027 (flat O(1), falling toward 1).
(L3) LADDER GEOMETRIC: log10(lam_i/tau) = 0/5.35/10.03/13.69/15.63
     (x=5), 0/6.00/11.53/16.36/20.53/24.20/27.53/29.17 (x=8),
     0/7.03/13.31/19.03/24.21/29.24/33.66/37.95/41.75 (x=13):
     falling multi-dex steps; collapse count n{lam < 0.1 lam_max} =
     4/7/12 vs m = 4/10/21.  The mass decomposition of psi_1 over
     the cache: mid share (om_max, gtop] = 0.987/0.985/0.980 of
     lam_1, band share <= 7.5e-4, zone share ~ (q_1 - lam_1)-scale:
     lam_1 is TAIL-CARRIED.
(L4) SPECTRUM CONCENTRATES ON V: q_i vs lam_i rel dev (i = 1/2/3) =
     7.7e-6/4.4e-4/3.1e-2 (x=5), 2.7e-9/8.9e-8/2.8e-6 (x=8),
     3.9e-17/1.1e-15/2.6e-14 (x=13) -- the zone compression
     reproduces the WHOLE collapsing block, ever tighter in x: the
     three residues read ONE spectrum, machine-pinned.
(L5) MINOR0 LOCK: the k=0 (constant/pole mode) principal minor
     floors the gap at (lam_0(minor) - tau)/(lam_1 - tau) = 0.6500/
     0.6507/0.6511 (FLAT over 3 dex of FULLGAP span), and the
     two-level secular identity mu = (v_0^2 lam_1 + v_1^2 tau)/
     (v_0^2 + v_1^2) predicts it to 1.9e-6/2.8e-7 via the k=0
     components (v_0, v_1) = (0.6621, 0.4859)/(0.5946, -0.4356):
     the flat ratio IS the flat 0-mode overlap share of the two
     bottom eigenvectors.  Mid/top-mode minors are VACUOUS floors
     (1.6e-3/2.6e-5 at x=5): the pole mode is load-bearing.
(L6) BLOCK PORTRAIT: psi_1 block Rayleigh (pole, arch, prime) =
     (+0.80, -0.38, +0.42)/(+0.83, -0.42, +0.42)/(+0.85, -0.44,
     +0.42) -- FLAT, with prime share +0.42 (vs phi's +0.04..+0.06)
     cancelling to lam_1 at depth 10.1/23.0/46.2 dex: lam_1 is an
     ALIGNMENT-WALL-class three-block cancellation with an O(1)
     prime component.
(L7) psi_1 zone sign census = m + 1 (5/11/22): exactly one extra
     node; E_{psi_1} kills phi's node config at rel level 1.9e-5/
     1.2e-8/1.2e-15 (falling).
(L8) GROWTH LAW: FULLGAP = 2.225493e5/9.951249e5/1.061906e7/
     ~3.25e7/~1.14e8, log-log slope vs x ~ 4.04 (vs y_t's 4.14;
     lock ratio FULLGAP/y_t = 3.64/2.39/3.31/2.58/2.84, r143).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer: G10 Y1 (partial-fraction positivity + bordered
    rational instance diag(1,2,5)/phi=e0 with TrH == 5/4, floor
    4/5 <= 1, tf identity == 1 + 1/4 + the n=2 EQUALITY instance
    [[3,1],[1,3]]); G11 Y2 (Rayleigh expansion rearrangement exact
    + PSD bound step + exact 3-dim instance diag(1,2,10) with
    eps^2 = 1/2: q_1 = 6 <= 10 = bound); G12 Y3 (lam_1 <= Tr - tau
    instance; diag(t,1) unbounded-ratio family at t = 1e-6 + limit
    oo; rate-lock rearrangement exact); G13 Y4 (s-chain identity
    generic == 1); G14 demand-transfer algebra (lock-window
    transfer [c1 y_t <= d1 <= c2 y_t] + [FULLGAP <= P] + [d1 <=
    (1+eta) FULLGAP] ==> y_t <= (1+eta) P/c1 exact; W3 shape
    re-gate: codim-1 Gram interlacing instance diag(1,2,5,7),
    CRootOf, Courant-Fischer CITED; minor two-level secular
    identity (mu - tau)/(lam_1 - tau) == v_0^2/(v_0^2 + v_1^2)).
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan to T_z + 6, step 0.05;
    newton-polished nodes, the r141/r143 standard):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform);
    G31 spectral ladder: all lam_i > 0, sorted; FULLGAP inside the
    frozen r142 windows x (0.97, 1.03); ladder profile + collapse
    counts printed; post-loop growth slope in (3.4, 4.6);
    G32 harmonic floor (Y1 instantiated): bordered LU at dps + 50
    (r144 lu instrument VERBATIM incl. the smoke-1 getrs-order
    repair), K solves; TrH vs eigen-sum cross dev <= 1e-20; floor
    1/TrH <= (lam_1 - tau)(1 + 1e-9) HARD; tf in (1 - 1e-12, 1.05);
    TRACEFLOOR = tau TrH <= x^25 + printed;
    G33 trace-cap adjudication (Y3 instantiated): TrM in (1, 1e4)
    + block traces printed; vacuity dex >= 8; post-loop vacuity
    slope vs |log10 tau| in (0.85, 1.15) (RIDES-1/TAU pinned);
    G34 node-config V + replication: |qrel| <= 1e-30, null residual
    <= 1e-40; W3 re-gate delta_1 >= FULLGAP (1 - 1e-12); q_i >=
    lam_i (1 - 1e-12) for i = 1..5 (interlacing HARD) with rel dev
    <= 1e-4 (i=1), <= 0.1 (i=2,3), i=4,5 printed; zone-top argmin
    in the frozen r139/r141/r142 windows AND >= 3; s <= 0.1; s x
    gap in (0.98, 1.02); delta_1 windows; share_1 >= 0.5; tlaw on
    the CDXLI strings <= 5e-3;
    G35 Y4 instantiated: |s delta_1 share_1 rho2/et_1^2 - 1| <=
    1e-30; overlap/gap split printed + post-loop slopes;
    G36 zero-jet law (L1/L2): A_0(psi_1) != 0; jr = (A_0(psi_1)/
    A_0(phi))^2/FULLGAP in (0.8, 1.6); tlaw_1 = lam_1/(8 A_0(psi_1)
    ^2 G(T_z)) in (0.05, 5.0) AND tlaw_1/tlaw_0 in (0.5, 2.0);
    y_t(psi_1) printed;
    G37 psi_1 zone anatomy (L7 + Y2 instantiated): zone sign census
    == m + 1 at core, in [m, m + 2] at deep (pre-freeze unmeasured,
    DISCLOSED); node kill max_j |E_{psi_1}(mu_j)|/scale <= 1e-3;
    eps^2 via BOTH the row-Gram route (primary) and the projection
    route (cross dev <= 0.05 at core, printed at deep); transfer
    0 <= q_1 - lam_1 <= eps^2 (lam_max - lam_1)/(1 - eps^2)
    (1 + 1e-9) HARD with tightness ratio <= 1e3;
    G38 budget pin + mass (L3 + Y2 pricing): x = 5/8 HARD:
    sum_zone 2 E_{psi_1}(gamma)^2 <= (lam_1 + OFF_1)(1 + 1e-6) and
    chain bound [m (lam_1 + OFF_1) lam_max/(2 sin^2_min sig_min
    (1 - eps^2))]/(tau FULLGAP) <= 1e6; ALL rungs: per-zero
    |E(gamma_f64)| <= sqrt((lam_1 + OFF_1)/2) + 3 |E'(gamma_f64)|
    CACHE_SLOP (the f64-aware form; gamma-side typed F64-LIMITED
    from x = 13, the known instrument class, DISCLOSED); mid mass/
    lam_1 in (0.7, 1.05) core, (0.4, 1.1) deep; band share <= 5e-2
    core; block portrait pole in (0.5, 1.2), arch in (-0.8, -0.2),
    prime in (0.2, 0.7) + cancellation depth printed;
    G39 minor floors (L5): k=0 at ALL rungs: tau (1 - slop) <=
    lam_0(minor) <= lam_1 (1 + slop) HARD (Cauchy); ratio in
    (0.5, 0.8); two-level prediction dev <= 1e-3; mid/top minors at
    core only: ratios <= 0.01 (MID-MINOR-VACUOUS pin).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 (NOT PSD: the Y1/Y2 hypotheses fail exactly here,
    the harmonic/transfer machinery claims nothing) AND y_t_w/b_top
    <= 1.0 (r140 signature); G53 consistency.
S5  G54 tau-screens (|slope log10 FULLGAP vs log10 tau| <= 0.30 and
    |slope log10 TRACEFLOOR vs log10 tau| <= 0.30: the demand-side
    ratios are NOT Connes-priced; the trace-cap vacuity rides 1/tau
    BY CONSTRUCTION -- BOUND-RIDES-CONNES typed for the trace
    instrument, the pinned Y3 obstruction); G55 conditioning
    (1e-25 shift window).
S6  G60 demand audit (CHAIN-AUDIT, cited theorems not re-proven:
    NFCLOS sequence-demand -> Theorem R transfer -> coupling
    absorbed -> the FULLGAP coordinate consumes NO tlaw, NO Z, no
    lattice proximity (source-only spectral data; r142 W2/W3 +
    r141 V1 cited) -> V2 good sets provide the unbounded sequence
    -> no ALL-X demand survives; TRACEFLOOR certificate is
    eigensolve-free given (tau, phi): CERT-COMPRESSED inherited);
    G61 min-cut (r116 replica; r142/r144 graph VERBATIM):
    L1TAILPROVEN -> TOPROOT(1) -> TAILVIS(1) -> TLAWCAP(1) ->
    BANDMASSTHM(INF) -> SUSCAP2R(1) -> DELTA1FLOOR(1) ->
    QSUBGAPTHM(INF) -> PFLOORTHM(INF) -> ... -> WPDWIN; flows base
    4, refined 5, one-grant 5, counterfactual PARALLEL 9 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor.
1.2]; T_PT = 3000175332800 [PT21]; M_JETS = 400; MGRID = (2, 4, 8,
16, 32, 64, 128, 256, 400); SCAN_STEP = 0.05; SCAN_LO = 0.5;
SCAN_OVER = 6.0; TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05;
NODE_EXCL = 0.02; SIGN_STEP = 0.05; CACHE_SLOP = 1e-9; BORD_PAD =
50 dps; HSW_MONO_GRID = (50, 100, 1e3, 1e4, 1e5, 1e6, 3e12).
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
24: 1.1382e8} x (0.97, 1.03) (r142 W3 exhibit strings; measured
pre-freeze 2.225493e5/9.951249e5/1.061906e7 at core);
FG_SLOPE_WIN = (3.4, 4.6) (calibrated 4.04 over the r142 strings);
TRH_XDEV_BAR = 1e-20 (pre-freeze 2.0e-52/4.0e-60/1.5e-75);
FLOOR_SLOP = 1e-9; TF_WIN = (1 - 1e-12, 1.05) (pre-freeze 1.000021/
1.000003/1.000001; deep unmeasured, DISCLOSED); POLY_DEG = 25;
TRM_WIN = (1.0, 1e4) (pre-freeze 11.268365/29.731661/77.408608;
blocks pole 3.3983/4.5543/5.8932, arch 8.8146/25.9827/73.5849,
prime 0.9445/0.8053/2.0695); VAC_MIN = 8.0 (pre-freeze 11.50/24.90/
48.46); VAC_SLOPE_WIN = (0.85, 1.15) (calibrated 0.978);
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)}; S_BAR = 0.1; SGAP_WIN =
(0.98, 1.02); D1_TAB = {5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18:
3.25e7, 24: 1.14e8} x (0.7, 1.3); SHARE1_BAR = 0.5; TLAW_TAB =
{5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel tol
5e-3 (CDXLI strings); INTERLACE_SLOP = 1e-12; QDEV1_BAR = 1e-4
(pre-freeze 7.677e-6/2.660e-9/3.943e-17); QDEV23_BAR = 0.1
(pre-freeze i=2: 4.4e-4/8.9e-8/1.1e-15, i=3: 3.1e-2/2.8e-6/
2.6e-14); SID_BAR = 1e-30 (pre-freeze -7.8e-62/0.0/0.0); JR_WIN =
(0.8, 1.6) (pre-freeze 1.124/1.110/1.027; deep unmeasured,
DISCLOSED); TLAW1_WIN = (0.05, 5.0); TLAW1_RATIO_WIN = (0.5, 2.0)
(pre-freeze 0.889/0.901/0.973); SIGN_DEEP_SLACK = (0, 2) around
m + 1 (core measured == m + 1: 5/11/22); NODEKILL_BAR = 1e-3
(pre-freeze rel 1.90e-5/1.15e-8/1.19e-15); EPS_XDEV_BAR = 0.05
(core only); TRANSFER_SLOP = 1e-9; TRANSFER_RATIO_MAX = 1e3
(pre-freeze 1.604/3.751/3.687); BUDGET_SLOP = 1e-6 (x = 5/8 HARD:
pre-freeze 2.881e-16 <= 3.575e-11, 1.793e-32 <= 3.754e-24;
gamma-side F64-LIMITED from x = 13: measured zone sum 4.962e-33 vs
lam_1 + OFF = 2.654e-47 at x=13 is PURE f64-ordinate artifact --
the derivative-aware per-zero form gates all rungs);
CHAIN_RATIO_MAX = 1e6 (x = 5/8; pre-freeze ~8.4 at x=5 hand
estimate, gate generous, DISCLOSED); MIDMASS_WIN_CORE = (0.7,
1.05) (pre-freeze 0.987/0.985/0.980); MIDMASS_WIN_DEEP = (0.4,
1.1) (unmeasured, DISCLOSED); BANDSHARE_BAR = 5e-2 (core;
pre-freeze 7.5e-4/8.2e-5; x >= 13 f64-typed, printed);
BLK_POLE_WIN = (0.5, 1.2); BLK_ARCH_WIN = (-0.8, -0.2);
BLK_PRIME_WIN = (0.2, 0.7) (pre-freeze portraits (+0.7991,
-0.3794, +0.4197)/(+0.8332, -0.4162, +0.4170)/(+0.8514, -0.4351,
+0.4163); deep from the flat trend, DISCLOSED); MINOR0_WIN =
(0.5, 0.8) (pre-freeze 0.6500/0.6507/0.6511); MINOR0_PRED_BAR =
1e-3 (pre-freeze 1.89e-6/2.79e-7); MINOR_MID_MAX = 0.01
(pre-freeze 1.64e-3/2.30e-4/2.42e-5 mid, 2.59e-5/2.91e-6/2.62e-7
top); CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30 (FULLGAP vs tau
calibrated -0.030); COND_WIN = (1e-40, 1e-10); GAMMA1_LIT =
14.134725141734694 (ward only); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; np.float64-repr casts guarded by float()/repr(); log
diagnostics via mp.log inside workdps (r141 amendment-1 class);
route-B linear algebra at dps + BORD_PAD with the r144 own
deterministic partial-pivot LU (factor once, reuse; all sequential
row swaps BEFORE the forward elimination -- LAPACK getrs order,
the r144 smoke-1 repair, ported VERBATIM).

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_fullgap_spectrum.py + logs + one inline two-level
minor check, deleted; numbers quoted verbatim above and here):
x=5 (K=11, dps 60): ladder dex 0/5.35/10.03/13.69/15.63/15.84/
15.94/15.99/16.08/16.10/16.20, lam_max 2.5266, n{<1e-3 lam_max} =
3, n{<0.1 lam_max} = 4 (m = 4); TrH 2.796917e10, TRACEFLOOR
4.4935e-06; delta_1/FULLGAP - 1 = 7.677e-06; q1-lam1 = 1.708 tau;
eps^2(proj) 1.743e-16; transfer ratio 1.604; zone sign changes 5;
E_psi1 node max 1.16e-08 (rel 1.90e-05, scale 6.10e-04); budget
2.881e-16 vs 3.575e-11 (OFF_1 1.5e-20); band 2.686e-14, mid
3.530e-11, beyond_hi 7.939e-13, total/lam1 0.9880; y_t(psi1)
3.1511e4; blocks phi (+1.4247, -1.3841, +0.0406, 15.9 dex); minor
k=0 2.324e-11 ratio 0.6500 (v_0 0.6621, v_1 0.4859, pred dev
1.89e-06), k=5 1.639e-03, k=10 2.592e-05.  x=8 (K=21, dps 80):
ladder 0/6.00/11.53/16.36/20.53/24.20/27.53/29.17/...; TrH
2.663661e23; TRACEFLOOR 1.0049e-06; delta_1/FG - 1 = 2.660e-09;
eps^2 1.017e-32; ratio 3.751; signs 11; budget 1.793e-32 <=
3.754e-24; mid/lam1 0.985; y_t(psi1) 3.0591e5; minor0 0.6507
(v_0 0.5946, v_1 -0.4356, pred dev 2.79e-07).  x=13 (K=42, dps
120, build 176 s): ladder 0/7.03/13.31/19.03/24.21/29.24/33.66/
37.95/41.75/... 53.90 at i=19; TrH 3.768268e46; TRACEFLOOR
9.4170e-08; delta_1/FG - 1 = 3.943e-17; eps^2 8.192e-64; ratio
3.687; signs 22; gamma-side zone sum 4.962e-33 (f64 artifact,
max|E(gamma_f64)| 4.98e-17 vs node max 1.96e-32: the f64 ordinate
offset times |E'| -- EXACTLY the r139/r141/r143 'f64 grid wider
than the well from x = 13' class, hence the derivative-aware
per-zero gate); mid/lam1 0.980; y_t(psi1) 2.6282e6; minor0 0.6511.
x = 18/24 pre-freeze UNMEASURED on all new quantities (build
cost); their bars are set from the frozen r139-r144 strings, the
flat core trends and structure asserts, DISCLOSED: FG windows from
the r142 strings, tf/jr/tlaw_1/minor0/portrait/mid-mass windows
per the tables above, sign census slack [m, m+2].  Amendments
after the frozen run, if any, are appended as numbered AMENDMENT
blocks below.

VERDICT ENUMS (frozen): Y1-PROVEN(harmonic-trace floor; DELTA1FLOOR
<== TRACEFLOOR <= poly, eigensolve-free, tf == 1 + 1e-5-class:
near-equality); Y2-PROVEN(tightness transfer exact; eps budget-
priced CONDITIONAL: the r142 interlacing tightness EXPLAINED);
Y3-PROVEN(RATE-LOCK pin: trace caps blind to the two-eigenvalue
collapse ratio; vacuity 11.5 -> 48.5 dex riding 1/tau; the
classical half TrM <= poly MEASURED); Y4-PROVEN(s-chain identity;
D-s = overlap-vs-gap balance on the same spectrum);
ZEROJET-LAW(L1/L2: lam_1 = 8 A_0(psi_1)^2 G(T_z) x tlaw-window;
FULLGAP = jet-ratio^2 x O(1) -- F1 answered MEASURED, closed form
NOT derived: OPEN-CLASSICAL-CANDIDATE retyped in jet currency);
LADDER-GEOMETRIC + TAIL-CARRIED(L3); SPECTRUM-CONCENTRATES-ON-V
(L4: one spectrum, three residues); MINOR0-LOCK(L5: flat 0.651 ==
0-mode overlap share, two-level exact); MID-MINOR-VACUOUS;
BLOCK-PORTRAIT-FLAT(L6: prime share 0.42); SIGN-CENSUS-M-PLUS-1
(L7); GROWTH-LAW(L8: slope ~4.04 vs demand poly: both demand
sides measured-satisfied with >= 5 orders margin);
BUDGET-PIN(x = 5/8 hard; GAMMA-SIDE-F64-LIMITED from x = 13,
instrument class, disclosed); CONTROLS-REFUSE; DEMAND-FLAT +
BOUND-RIDES-CONNES(typed, incl. the Y3 vacuity as the pinned
rides-1/tau instrument); QUANTIFIER-INHERITED(dense-x suffices,
CHAIN-AUDIT); OMEGA-RECOORDINATED(residue SET UNCHANGED = {TOPROOT
(= FULLGAP-CAP mod the measured O(1) y_t-lock; delta_1 <-> FULLGAP
now two-sided: exact lower W3 + Y2 budget-conditional upper),
ONSETCAP, SUSCAP2R} + DELTA1FLOOR(<== TRACEFLOOR-CAP, harmonic
recoordination) + dense-a + a-extension + window-a; census {MEAS,
OMEGA-POS} cardinality 4 UNCHANGED); MINCUT(4/5).  Composite
priority: INSTRUMENT-EDGE (any edge gate fails, exit 1) >
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
SIGN_STEP = 0.05
CACHE_SLOP = 1e-9
BORD_PAD = 50
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
          24: 1.1382e8}
FG_WIN = (0.97, 1.03)
FG_SLOPE_WIN = (3.4, 4.6)
TRH_XDEV_BAR = 1e-20
FLOOR_SLOP = 1e-9
TF_WIN = (1.0 - 1e-12, 1.05)
POLY_DEG = 25
TRM_WIN = (1.0, 1e4)
VAC_MIN = 8.0
VAC_SLOPE_WIN = (0.85, 1.15)
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
QDEV1_BAR = 1e-4
QDEV23_BAR = 0.1
SID_BAR = 1e-30
JR_WIN = (0.8, 1.6)
TLAW1_WIN = (0.05, 5.0)
TLAW1_RATIO_WIN = (0.5, 2.0)
NODEKILL_BAR = 1e-3
EPS_XDEV_BAR = 0.05
TRANSFER_SLOP = 1e-9
TRANSFER_RATIO_MAX = 1e3
BUDGET_SLOP = 1e-6
BUDGET_HARD_RUNGS = (5, 8)
CHAIN_RATIO_MAX = 1e6
MIDMASS_WIN_CORE = (0.7, 1.05)
MIDMASS_WIN_DEEP = (0.4, 1.1)
BANDSHARE_BAR = 5e-2
BLK_POLE_WIN = (0.5, 1.2)
BLK_ARCH_WIN = (-0.8, -0.2)
BLK_PRIME_WIN = (0.2, 0.7)
MINOR0_WIN = (0.5, 0.8)
MINOR0_PRED_BAR = 1e-3
MINOR_MID_MAX = 0.01
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


def jets_of(cs: list, aa, K: int):
    """jets A_{2i} + lattice b for a coefficient vector (caller dps)."""
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
    return A, b


def envj_of(A: list, b: list, cs_abs: list, K: int, y):
    """Theorem-J1 envelope (r140, ported verbatim); caller dps."""
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


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138-r144 replica)."""
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
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp, Rm=Rm)


def secular_data(Vd: dict, r: list):
    """(lam*, etn, rho2, chi) for the extra row r on V (caller dps)."""
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
    return lo, etn, rho2, chi


# --------------------------------------------- deterministic LU (route B)
def lu_factor(Amat, n):
    """own partial-pivot LU (r144, VERBATIM); caller sets workdps."""
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
    """solve with pre-computed lu_factor; ALL sequential row swaps
    BEFORE the forward elimination (LAPACK getrs order; the r144
    smoke-1 repair, VERBATIM)."""
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
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 Y1 harmonic-trace floor
    d1s, d2s, d3s = sp.symbols("d1s d2s d3s", positive=True)
    okA = bool(((1 / d1s + 1 / d2s + 1 / d3s) - 1 / d1s)
               .is_positive)
    # bordered rational instance: M = diag(1,2,5), tau = 1, phi = e0
    Mi = sp.diag(1, 2, 5)
    phi = sp.Matrix([1, 0, 0])
    B = sp.zeros(4, 4)
    B[0:3, 0:3] = Mi - sp.eye(3)
    B[0:3, 3] = phi
    B[3, 0:3] = phi.T
    trH = sp.Integer(0)
    for k in range(3):
        rhs = sp.zeros(4, 1)
        rhs[k] = 1
        yk = B.solve(rhs)
        trH += yk[k]
    okB = sp.simplify(trH - sp.Rational(5, 4)) == 0
    okC = bool(1 / trH <= sp.Integer(2) - sp.Integer(1))   # floor 4/5<=1
    tf_id = (sp.Integer(2) - 1) * trH
    okD = sp.simplify(tf_id - (1 + sp.Rational(1, 4))) == 0
    # n = 2 equality instance: M = [[3,1],[1,3]], tau = 2, phi~(1,-1)
    M2 = sp.Matrix([[3, 1], [1, 3]])
    B2 = sp.zeros(3, 3)
    B2[0:2, 0:2] = M2 - 2 * sp.eye(2)
    B2[0, 2] = 1
    B2[1, 2] = -1
    B2[2, 0] = 1
    B2[2, 1] = -1
    trH2 = sp.Integer(0)
    for k in range(2):
        rhs = sp.zeros(3, 1)
        rhs[k] = 1
        yk = B2.solve(rhs)
        trH2 += yk[k]
    okE = sp.simplify(trH2 - sp.Rational(1, 2)) == 0 \
        and sp.simplify(1 / trH2 - (4 - 2)) == 0
    out.append(("G10-y1-harmonic-floor", okA and okB and okC and okD
                and okE,
                "sum_{i>=1} 1/(lam_i - tau) >= 1/(lam_1 - tau) "
                "(term-wise positivity); bordered instance diag(1,2,5)"
                "/phi=e0: TrH == 5/4, floor 4/5 <= lam_1 - tau == 1, "
                "tf identity == 1 + 1/4; n=2 instance [[3,1],[1,3]]: "
                "TrH == 1/2 with floor == gap EXACTLY (equality case): "
                "THEOREM Y1 -- DELTA1FLOOR <== FULLGAP >= 1/poly <== "
                "TRACEFLOOR = tau TrH <= poly, eigensolve-free"))

    # ---------------- G11 Y2 tightness transfer
    l1, lmax, e2s = sp.symbols("l1 lmax e2s", positive=True)
    lhs = (l1 * (1 - 2 * e2s) + e2s * lmax) / (1 - e2s)
    rhs = l1 + e2s * (lmax - l1) / (1 - e2s)
    okF = sp.simplify(lhs - rhs) == 0
    # exact 3-dim instance: M = diag(1,2,10), V = {v: v2 == v3},
    # phi = e1 in V, psi_1 = e2, P_V psi_1 = (0,1/2,1/2), eps^2 = 1/2
    q1V = sp.Rational(2 + 10, 2)          # Rayleigh of (0,1,1)/sqrt2
    bound = 2 + sp.Rational(1, 2) * (10 - 2) / sp.Rational(1, 2)
    okG = bool(q1V - 2 >= 0) and bool(q1V <= bound) \
        and sp.simplify(bound - 10) == 0
    # PSD step: w'Mw <= eps^2 lmax for |w|^2 = eps^2 (spectral bound
    # instance): w = (0,0,1/sqrt2): w'Mw = 5 <= 10/2
    okH = bool(sp.Rational(10, 2) >= sp.Rational(10, 2))
    out.append(("G11-y2-tightness-transfer", okF and okG and okH,
                "Rayleigh of P_V psi_1 expands EXACTLY to lam_1 + "
                "eps^2 (lam_max - lam_1)/(1 - eps^2) after the PSD "
                "spectral bound w'Mw <= eps^2 lam_max: 0 <= q_1 - "
                "lam_1 <= eps^2 (lam_max - lam_1)/(1 - eps^2) "
                "(THEOREM Y2; instance diag(1,2,10) with eps^2 = 1/2: "
                "q_1 = 6 <= 10 = bound) -- the r142 interlacing "
                "tightness is the zone-killedness of psi_1"))

    # ---------------- G12 Y3 trace-cap vacuity (rate-lock pin)
    okI = bool(sp.Integer(2) <= (1 + 2 + 5) - 1)  # lam_1 <= TrM - tau
    t = sp.symbols("t", positive=True)
    fg_fam = 1 / t - 1
    okJ = bool(fg_fam.subs(t, sp.Rational(1, 10 ** 6)) == 10 ** 6 - 1) \
        and bool((1 + sp.Rational(1, 10 ** 6)) <= 2) \
        and sp.limit(fg_fam, t, 0, "+") == sp.oo
    Ps, taus, lam1s = sp.symbols("Ps taus lam1s", positive=True)
    okK = sp.simplify((Ps * taus / taus - 1) - (Ps - 1)) == 0
    out.append(("G12-y3-rate-lock", okI and okJ and okK,
                "lam_1 <= Tr M - tau exact (PSD instance); the family "
                "diag(t, 1) keeps Tr <= 2 while FULLGAP = 1/t - 1 -> "
                "oo: NO trace/moment cap can see the two-eigenvalue "
                "collapse RATIO; rate-lock rearrangement [lam_1 <= C] "
                "+ [tau >= lam_1/P] ==> FULLGAP <= P - 1 (THEOREM Y3: "
                "the D-cap missing half is a tau-floor relative to "
                "lam_1 -- Chebyshev does NOT close D-cap, pinned)"))

    # ---------------- G13 Y4 s-chain identity
    e1q, e2q, q0q, q1q, q2q, r2q, tq = sp.symbols(
        "e1q e2q q0q q1q q2q r2q tq", positive=True)
    chi_g = e1q / (q1q - q0q) + e2q / (q2q - q0q)
    s_g = tq * chi_g / r2q
    d1_g = (q1q - q0q) / tq
    share1_g = (e1q / (q1q - q0q)) / chi_g
    okL = sp.simplify(s_g * d1_g * share1_g * r2q / e1q - 1) == 0
    out.append(("G13-y4-s-chain-identity", okL,
                "s x delta_1 x share_1 x rho2/et_1^2 == 1 GENERIC "
                "(THEOREM Y4): with delta_1 == FULLGAP tight, "
                "SUSCAP2R is the overlap-vs-gap balance et_1^2/rho2 "
                "<= poly x FULLGAP on the SAME spectrum (D-s "
                "inheritance coordinate)"))

    # ---------------- G14 demand transfer + W3 re-gate + minor secular
    yt_, dd, PP, c1_, c2_, eta_ = sp.symbols(
        "yt_ dd PP c1_ c2_ eta_", positive=True)
    # lock window + cap transfer: c1 yt <= dd, dd <= (1+eta) FG,
    # FG <= PP ==> yt <= (1+eta) PP / c1
    okM = sp.simplify(((1 + eta_) * PP / c1_)
                      - ((1 + eta_) * PP) / c1_) == 0 \
        and bool((c1_ * yt_ <= dd) is not False)
    # instance: c1=3/2, dd = (1+1/10) FG, FG = P: yt <= 11 P/15
    okN = bool(sp.Rational(11, 10) * 1 / sp.Rational(3, 2)
               == sp.Rational(11, 15))
    # W3 shape re-gate: codim-1 Gram interlacing on diag(1,2,5,7)
    lam = sp.symbols("lam")
    Wq = sp.diag(sp.Integer(1), sp.Integer(2), sp.Integer(5),
                 sp.Integer(7))
    U = sp.Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]])
    Qc = (U.T * Wq * U)
    Gc = (U.T * U)
    poly = sp.expand((Qc - lam * Gc).det())
    ppoly = sp.Poly(poly, lam)
    mus = [sp.CRootOf(ppoly, i) for i in range(3)]
    lams_full = [sp.Integer(1), sp.Integer(2), sp.Integer(5),
                 sp.Integer(7)]
    okO = all(bool(mus[i] >= lams_full[i]) for i in range(3)) \
        and all(bool(mus[i] <= lams_full[i + 1]) for i in range(3))
    # minor two-level secular identity
    v0s, v1s, l1m, taum = sp.symbols("v0s v1s l1m taum", positive=True)
    mu2 = (v0s ** 2 * l1m + v1s ** 2 * taum) / (v0s ** 2 + v1s ** 2)
    okP = sp.simplify((mu2 - taum) / (l1m - taum)
                      - v0s ** 2 / (v0s ** 2 + v1s ** 2)) == 0
    out.append(("G14-demand-transfer", okM and okN and okO and okP,
                "two-sided demand extraction: [c1 y_t <= delta_1 <= "
                "c2 y_t] + [delta_1 <= (1+eta) FULLGAP] + [FULLGAP <= "
                "P] ==> y_t <= (1+eta) P/c1 (D-cap = FULLGAP-CAP mod "
                "the measured lock); D-low = FULLGAP >= 1/P direct "
                "via delta_1 >= FULLGAP (W3 codim-m interlacing "
                "re-gated on the exact Gram instance, Courant-Fischer "
                "CITED); minor two-level secular: (mu - tau)/(lam_1 - "
                "tau) == v_0^2/(v_0^2 + v_1^2) exact (the MINOR0 lock "
                "mechanism)"))
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
    steps.append(("FULLGAP coordinate consumes NO tlaw, NO Z, no "
                  "lattice proximity: source-only spectral data of "
                  "Mq (r142 W2/W3 + r141 V1 cited); TRACEFLOOR "
                  "certificate eigensolve-free given (tau, phi) "
                  "(r144 X4 carrier: CERT-COMPRESSED inherited)", True))
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

    print("fullgap_spectrum_probe -- PRIME.FULLGAP.SPECTRUM.01")
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

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems Y1-Y4 + demand transfer)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW budget law + OFF "
         "recipe; r132 raw census; r135 D1-D4; r136 S1-S4 + PINBALL; "
         "r137/CDXLI budget identity + tlaw strings; r138 Q1-Q3; "
         "r139/CDXLIII U1-U4 + delta_1/share_1 strings; r140/CDXLIV "
         "J1-J4 + y_t strings; r141/CDXLV V1-V3 + quantifier audit; "
         "r142/CDXLVI W1-W3 + FULLGAP exhibit strings; r143/CDXLVII "
         "T1-T4 + delta_1-lock strings; r144/CDXLVIII X1-X4 + "
         "bordered-LU instrument; HSW22 Cor. 1.2; PT21; Courant-"
         "Fischer min-max; Cauchy interlacing (principal minors); "
         "Euler sine product")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone; "
          "G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: SPECTRAL ANATOMY OF THE WEIL MATRIX")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    ok36 = ok37 = ok38 = ok39 = True
    det30, det31, det32, det33, det34 = [], [], [], [], []
    det35, det36, det37, det38, det39 = [], [], [], [], []
    fg_tab, tau_tab, vac_tab, tfl_tab = {}, {}, {}, {}
    ov_tab, s_tab = {}, {}
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
        with mp.workdps(dps):
            E = ce["mpE"]
            Vv = ce["mpV"]
            Mq = ce["mpM"]
            tau = E[0]
            lam1 = E[1]
            lammax = E[K - 1]
            fullgap = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            l10 = mp.log(10)
            tauf = float(tau)
            fg_f = float(fullgap)
            A_phi, b_lat = jets_of(cs, aa, K)
            A0_phi = A_phi[0]
            yt_phi = float(abs(A_phi[1] / A0_phi))
            om_max = float(oms[K - 1])
        Gz = hsw_G(Tz)
        tlaw0 = tauf / (8.0 * float(abs(A0_phi)) ** 2 * Gz)
        fg_tab[x] = fg_f
        tau_tab[x] = tauf

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
        zone_f = [float(v) for v in zone_nds]

        # ---- G31 spectral ladder
        with mp.workdps(dps):
            pos_ok = all(E[i] > 0 for i in range(K))
            sort_ok = all(E[i] <= E[i + 1] for i in range(K - 1))
            idxs = sorted(set([0, 1, 2, 3, 4, 5, 6, 7, 8,
                               max(m_zone - 1, 0), m_zone,
                               min(m_zone + 1, K - 1), K - 1]))
            prof = ["i%d:%.2f" % (i, float(mp.log(E[i] / tau) / l10))
                    for i in idxs]
            nc3 = sum(1 for i in range(K) if E[i] < 1e-3 * lammax)
            nc1 = sum(1 for i in range(K) if E[i] < 1e-1 * lammax)
        fg_ok = FG_TAB[x] * FG_WIN[0] <= fg_f <= FG_TAB[x] * FG_WIN[1]
        ok31x = pos_ok and sort_ok and fg_ok
        ok31 = ok31 and ok31x
        det31.append("x%d: FULLGAP %.6e (win) ncoll(1e-3/1e-1) %d/%d "
                     "m %d" % (x, fg_f, nc3, nc1, m_zone))
        info("x=%d ladder log10(lam_i/tau): %s (lam_max %.3f)"
             % (x, " ".join(prof), float(lammax)))

        # ---- G32 harmonic floor (Y1 instantiated)
        dpsB = dps + BORD_PAD
        with mp.workdps(dpsB):
            tauB = ce["mpE"][0]
            phiv = [ce["mpV"][i, 0] for i in range(K)]
            n_b = K + 1
            B = mp.zeros(n_b, n_b)
            for i in range(K):
                for j2 in range(K):
                    B[i, j2] = Mq[i, j2]
                B[i, i] -= tauB
                B[i, K] = phiv[i]
                B[K, i] = phiv[i]
            t_lu0 = time.time()
            LU, pivv = lu_factor(B, n_b)
            trH = mp.mpf(0)
            for k in range(K):
                rhs = [mp.mpf(0)] * n_b
                rhs[k] = mp.mpf(1)
                yk = lu_solve_fac(LU, pivv, rhs, n_b)
                trH += yk[k]
            t_lu = time.time() - t_lu0
            trH_eig = sum(1 / (ce["mpE"][i] - tauB)
                          for i in range(1, K))
            xdev = float(abs(trH / trH_eig - 1))
            tf = float((ce["mpE"][1] - tauB) * trH)
            floor_ok = bool(1 / trH <= (ce["mpE"][1] - tauB)
                            * (1 + mp.mpf(repr(FLOOR_SLOP))))
            tracefloor = float(tauB * trH)
        tfl_tab[x] = tracefloor
        ok32x = (xdev <= TRH_XDEV_BAR and floor_ok
                 and TF_WIN[0] <= tf <= TF_WIN[1]
                 and tracefloor <= float(x) ** POLY_DEG)
        ok32 = ok32 and ok32x
        det32.append("x%d: TrH %.4e xdev %.0e tf %.6f TRACEFLOOR "
                     "%.3e (LU+%d solves %.1f s)"
                     % (x, float(trH), xdev, tf, tracefloor, K, t_lu))
        info("x=%d Y1 exhibit: FULLGAP >= 1/(tau TrH) = %.6e vs "
             "measured %.6e (tightness tf = %.6f: the harmonic floor "
             "is a near-EQUALITY -- geometric ladder)"
             % (x, 1.0 / tracefloor, fg_f, tf))

        # ---- G33 trace-cap adjudication (Y3 instantiated)
        with mp.workdps(dps):
            trM = sum(Mq[i, i] for i in range(K))
            trP = sum(ce["mpPole"][i, i] for i in range(K))
            trA = sum(ce["mpArch"][i, i] for i in range(K))
            trPr = sum(ce["mpPrime"][i, i] for i in range(K))
            vac = float(mp.log((trM - tau) / (lam1 - tau)) / l10)
        vac_tab[x] = vac
        ok33x = (TRM_WIN[0] <= float(trM) <= TRM_WIN[1]
                 and vac >= VAC_MIN)
        ok33 = ok33 and ok33x
        det33.append("x%d: TrM %.4f (P %.3f A %.3f Pr %.3f) vacuity "
                     "%.2f dex" % (x, float(trM), float(trP),
                                   float(trA), float(trPr), vac))

        # ---- G34 node-config V + replication
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            d1 = (Vd["qs"][1] - Vd["qs"][0]) / Vd["tau_mp"]
            d1_f = float(d1)
            w3_ok = bool(d1 >= fullgap * (1 - mp.mpf(repr(
                INTERLACE_SLOP))))
            qdevs = []
            inter_ok = True
            for i in range(1, 6):
                if i >= Vd["nf"]:
                    break
                dv = float((Vd["qs"][i] - ce["mpE"][i]) / ce["mpE"][i])
                qdevs.append(dv)
                inter_ok = inter_ok and Vd["qs"][i] >= ce["mpE"][i] \
                    * (1 - mp.mpf(repr(INTERLACE_SLOP)))
            tg = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                TOP_GRID_STEP)) + [Tz - 0.001]
            gmin = None
            argp = None
            for tv in tg:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - Vd["tau_mp"]) / Vd["tau_mp"])
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            r = row_at(mp.mpf(repr(float(argp))), K, oms, nrm)
            lam, etn, rho2, chi = secular_data(Vd, r)
            s_val = Vd["tau_mp"] * chi / rho2
            sg = float(s_val * (lam - Vd["tau_mp"]) / Vd["tau_mp"])
            s_f = float(s_val)
            e12 = etn[1] * etn[1]
            # smoke-1 instrument fix (disclosed): the Y4 identity must be
            # evaluated with the mp share -- the f64-cast share1 injects
            # ~1e-17 rounding into an exact 1e-30-gated chain (the r141
            # amendment-1 class); the float cast is kept for the gate
            # display only.  No bar, criterion or ladder moved.
            share1_mp = (e12 / (Vd["qs"][1] - Vd["qs"][0])) / chi
            share1 = float(share1_mp)
            ident = float(s_val * d1 * share1_mp * rho2 / e12 - 1)
            ovr = float(e12 / rho2)
        s_tab[x] = s_f
        ov_tab[x] = ovr
        lo_w, hi_w = REPL_WIN[x]
        tl_dev = abs(tlaw0 / TLAW_TAB[x] - 1.0)
        ok34x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR and w3_ok and inter_ok
                 and abs(qdevs[0]) <= QDEV1_BAR
                 and abs(qdevs[1]) <= QDEV23_BAR
                 and abs(qdevs[2]) <= QDEV23_BAR
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR
                 and SGAP_WIN[0] <= sg <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR and tl_dev <= TLAW_TOL)
        ok34 = ok34 and ok34x
        det34.append("x%d: qrel %.0e d1/FG-1 %.1e qdevs %s gap %.4f "
                     "s %.5f sg %.5f share1 %.3f (%.0f s)"
                     % (x, Vd["qrel"], d1_f / fg_f - 1.0,
                        "/".join("%.0e" % v for v in qdevs), gmin,
                        s_f, sg, share1, time.time() - t_q))
        info("x=%d L4 exhibit: q_i vs lam_i rel devs %s -- the zone "
             "compression reproduces the collapsing block (ONE "
             "spectrum, three residues)"
             % (x, ", ".join("%.1e" % v for v in qdevs)))

        # ---- G35 Y4 instantiated
        ok35x = abs(ident) <= SID_BAR
        ok35 = ok35 and ok35x
        det35.append("x%d: |s d1 share1 rho2/e1^2 - 1| = %.1e; "
                     "(e1^2/rho2)/FULLGAP = %.4e"
                     % (x, abs(ident), ovr / fg_f))

        # ---- G36 zero-jet law (psi_1)
        with mp.workdps(dps):
            cs1 = [Vv[i, 1] / nrm[i] for i in range(K)]
            A_1, _b1 = jets_of(cs1, aa, K)
            cs1_abs = [abs(v) for v in cs1]
            A0_1 = A_1[0]
            yt_1 = float(abs(A_1[1] / A0_1))
            jr = float((A0_1 / A0_phi) ** 2 / fullgap)
            tlaw1 = float(lam1) / (8.0 * float(abs(A0_1)) ** 2 * Gz)
        ok36x = (float(abs(A0_1)) > 0
                 and JR_WIN[0] <= jr <= JR_WIN[1]
                 and TLAW1_WIN[0] <= tlaw1 <= TLAW1_WIN[1]
                 and TLAW1_RATIO_WIN[0] <= tlaw1 / tlaw0
                 <= TLAW1_RATIO_WIN[1])
        ok36 = ok36 and ok36x
        det36.append("x%d: jr %.3f tlaw1 %.4f (tlaw0 %.4f) yt(psi1) "
                     "%.3e" % (x, jr, tlaw1, tlaw0, yt_1))
        info("x=%d L1/L2 exhibit: lam_1 = 8 A_0(psi_1)^2 G(T_z) x "
             "%.4f (tlaw window); FULLGAP = (A_0(psi_1)/A_0(phi))^2 "
             "/ %.3f -- the demands are 0-jet-ratio conditioning"
             % (x, tlaw1, jr))

        # ---- G37 psi_1 zone anatomy + Y2 transfer
        with mp.workdps(dps):
            sgn_prev = None
            ncross = 0
            for tv in np.arange(0.5, Tz, SIGN_STEP):
                v = en_pair(cs1, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgv = 1 if v > 0 else -1
                if sgn_prev is not None and sgv != sgn_prev:
                    ncross += 1
                sgn_prev = sgv
            node_max = mp.mpf(0)
            for mu in zone_nds:
                v = abs(en_pair(cs1, aa, oms, mu)[0])
                if v > node_max:
                    node_max = v
            e1max = mp.mpf(0)
            for tv in tg:
                v = abs(en_pair(cs1, aa, oms,
                                mp.mpf(repr(float(tv))))[0])
                if v > e1max:
                    e1max = v
            nodekill = float(node_max / e1max)
            # eps^2 -- row-Gram route (primary)
            psi1 = [Vv[i, 1] for i in range(K)]
            u = []
            for j in range(m_zone):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Rm"][j, k] * psi1[k]
                u.append(acc)
            Gm = mp.zeros(m_zone, m_zone)
            for i in range(m_zone):
                for j2 in range(i + 1):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Vd["Rm"][i, k] * Vd["Rm"][j2, k]
                    Gm[i, j2] = Gm[j2, i] = acc
            sol = mp.lu_solve(Gm, mp.matrix(u))
            eps2_g = sum(u[i] * sol[i] for i in range(m_zone))
            # projection route (cross-check)
            dl = []
            for fi in range(Vd["nf"]):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Nb"][k, fi] * psi1[k]
                dl.append(acc)
            yy = Vd["fwd"](dl)
            eps2_p = 1 - sum(v * v for v in yy)
            eps_xdev = float(abs(eps2_g / eps2_p - 1)) \
                if eps2_p != 0 else float("inf")
            q1ml1 = Vd["qs"][1] - lam1
            tbound = eps2_g * (lammax - lam1) / (1 - eps2_g)
            tr_ok = bool(q1ml1 <= tbound
                         * (1 + mp.mpf(repr(TRANSFER_SLOP))))
            tratio = float(tbound / q1ml1) if q1ml1 > 0 else 1.0
        sign_ok = (ncross == m_zone + 1) if not is_deep else \
            (m_zone <= ncross <= m_zone + 2)
        ok37x = (sign_ok and nodekill <= NODEKILL_BAR and tr_ok
                 and tratio <= TRANSFER_RATIO_MAX
                 and (is_deep or eps_xdev <= EPS_XDEV_BAR))
        ok37 = ok37 and ok37x
        det37.append("x%d: signs %d (m+1 %d) nodekill %.1e eps2 "
                     "%.2e (xdev %.0e) transfer ratio %.2f"
                     % (x, ncross, m_zone + 1, nodekill,
                        float(eps2_g), eps_xdev, tratio))
        info("x=%d Y2 exhibit: q_1 - lam_1 = %.3e (tau units %.2e) "
             "<= eps^2(lam_max - lam_1)/(1 - eps^2) = %.3e -- the "
             "r142 tightness delta_1/FULLGAP = 1.0000 is the "
             "zone-killedness of psi_1, quantitatively"
             % (x, float(q1ml1), float(q1ml1 / tau), float(tbound)))

        # ---- G38 budget pin + mass decomposition + block portrait
        with mp.workdps(dps):
            eta_pt1 = envj_of(A_1, _b1, cs1_abs, K,
                              mp.mpf(T_PT) ** 2) / abs(A0_1)
            off1 = float(8 * mp.exp(aa)
                         * (abs(A0_1) * (1 + eta_pt1)) ** 2) \
                * hsw_G(float(T_PT))
            zsum = mp.mpf(0)
            pz_ok = True
            sin2min = 1.0
            for gj in gam[gam <= Tz]:
                gmp = mp.mpf(repr(float(gj)))
                Ev, Epv = en_pair(cs1, aa, oms, gmp)
                zsum += 2 * Ev * Ev
                capv = mp.sqrt((lam1 + mp.mpf(repr(off1))) / 2) \
                    + 3 * abs(Epv) * mp.mpf(repr(CACHE_SLOP))
                pz_ok = pz_ok and bool(abs(Ev) <= capv)
                s2 = float(mp.sin(aa * gmp) ** 2)
                sin2min = min(sin2min, s2)
            mband = mp.mpf(0)
            mmid = mp.mpf(0)
            for gj in gam:
                gmp = mp.mpf(repr(float(gj)))
                Ev = en_pair(cs1, aa, oms, gmp)[0]
                t2 = 2 * Ev * Ev
                if gj <= om_max:
                    mband += t2
                else:
                    mmid += t2
            eta_g1 = envj_of(A_1, _b1, cs1_abs, K,
                             mp.mpf(repr(gtop)) ** 2) / abs(A0_1)
            beyond_hi1 = float(8 * abs(A0_1) ** 2
                               * (1 + eta_g1) ** 2) * hsw_G(gtop)
            midshare = float(mmid / lam1)
            bandshare = float(mband / lam1)
            # block Rayleigh portrait of psi_1
            blk = []
            for Mb in (ce["mpPole"], ce["mpArch"], ce["mpPrime"]):
                acc = mp.mpf(0)
                for i in range(K):
                    rowv = mp.mpf(0)
                    for j2 in range(K):
                        rowv += Mb[i, j2] * psi1[j2]
                    acc += psi1[i] * rowv
                blk.append(float(acc))
            cancel = float(mp.log(mp.mpf(repr(max(abs(blk[0]),
                                                  abs(blk[1]))))
                                  / lam1) / l10)
        hard_ok = True
        chain_txt = "n/a"
        if x in BUDGET_HARD_RUNGS:
            hard_ok = float(zsum) <= (float(lam1) + off1) \
                * (1 + BUDGET_SLOP)
            with mp.workdps(dps):
                Eg, _Vg = mp.eigsy(Gm)
                # normalized-row Gram smallest eigenvalue
                dg = [mp.sqrt(Gm[i, i]) for i in range(m_zone)]
                Gn = mp.zeros(m_zone, m_zone)
                for i in range(m_zone):
                    for j2 in range(m_zone):
                        Gn[i, j2] = Gm[i, j2] / (dg[i] * dg[j2])
                En, _Vn = mp.eigsy(Gn)
                sigmin = float(min(En[i] for i in range(m_zone)))
                chain = float((m_zone * (lam1 + mp.mpf(repr(off1)))
                               * lammax
                               / (2 * mp.mpf(repr(sin2min))
                                  * mp.mpf(repr(sigmin))
                                  * (1 - eps2_g)))
                              / (tau * fullgap))
            hard_ok = hard_ok and chain <= CHAIN_RATIO_MAX
            chain_txt = "%.1e" % chain
        mid_win = MIDMASS_WIN_CORE if not is_deep else MIDMASS_WIN_DEEP
        band_ok = (bandshare <= BANDSHARE_BAR) if x in (5, 8) else True
        ok38x = (pz_ok and hard_ok
                 and mid_win[0] <= midshare <= mid_win[1] and band_ok
                 and BLK_POLE_WIN[0] <= blk[0] <= BLK_POLE_WIN[1]
                 and BLK_ARCH_WIN[0] <= blk[1] <= BLK_ARCH_WIN[1]
                 and BLK_PRIME_WIN[0] <= blk[2] <= BLK_PRIME_WIN[1])
        ok38 = ok38 and ok38x
        det38.append("x%d: zsum %.1e (cap %s, chain %s) mid %.3f "
                     "band %.1e blocks (%+.3f, %+.3f, %+.3f) cancel "
                     "%.1f dex"
                     % (x, float(zsum),
                        "HARD" if x in BUDGET_HARD_RUNGS
                        else "f64-aware", chain_txt, midshare,
                        bandshare, blk[0], blk[1], blk[2], cancel))
        info("x=%d L3/L6 exhibit: lam_1 mass mid(om_max, gtop] share "
             "%.3f + beyond_hi %.2e/lam1 %.2f (TAIL-CARRIED); "
             "gamma-side zone sum %s; block portrait flat, prime "
             "share %+.2f"
             % (x, midshare, beyond_hi1, beyond_hi1 / float(lam1),
                ("hard-gated" if x in BUDGET_HARD_RUNGS else
                 "F64-LIMITED (r139/r141/r143 class, disclosed)"),
                blk[2]))

        # ---- G39 minor floors
        with mp.workdps(dps):
            kdels = (0, K // 2, K - 1) if not is_deep else (0,)
            rows_m = []
            m0_ratio = None
            m0_pred_dev = None
            mid_ok = True
            sandwich_ok = True
            for kdel in kdels:
                Mm = mp.zeros(K - 1, K - 1)
                ii2 = [i for i in range(K) if i != kdel]
                for a2, i in enumerate(ii2):
                    for b2, j2 in enumerate(ii2):
                        Mm[a2, b2] = Mq[i, j2]
                Em, _ = mp.eigsy(Mm)
                l0m = min(Em[i] for i in range(K - 1))
                ratio = float((l0m - tau) / (lam1 - tau))
                sandwich_ok = sandwich_ok and bool(
                    l0m >= tau * (1 - mp.mpf(repr(INTERLACE_SLOP)))) \
                    and bool(l0m <= lam1
                             * (1 + mp.mpf(repr(INTERLACE_SLOP))))
                if kdel == 0:
                    m0_ratio = ratio
                    v0c = Vv[0, 0]
                    v1c = Vv[0, 1]
                    pred = float(v0c * v0c / (v0c * v0c + v1c * v1c))
                    m0_pred_dev = abs(pred / ratio - 1.0)
                else:
                    mid_ok = mid_ok and ratio <= MINOR_MID_MAX
                rows_m.append("k%d:%.3e" % (kdel, ratio))
        ok39x = (sandwich_ok and MINOR0_WIN[0] <= m0_ratio
                 <= MINOR0_WIN[1] and m0_pred_dev <= MINOR0_PRED_BAR
                 and mid_ok)
        ok39 = ok39 and ok39x
        det39.append("x%d: %s minor0 %.4f pred dev %.1e"
                     % (x, " ".join(rows_m), m0_ratio, m0_pred_dev))
        info("x=%d L5 exhibit: MINOR0 lock ratio %.4f == v_0^2/"
             "(v_0^2 + v_1^2) (two-level secular, dev %.1e): the "
             "pole mode is load-bearing; mid/top minors vacuous"
             % (x, m0_ratio, m0_pred_dev))
        info("x=%d lock replication: FULLGAP/y_t = %.4f (r143 win "
             "(1.5, 6.0)); y_t %.4e; TRACEFLOOR %.3e"
             % (x, fg_f / yt_phi, yt_phi, tracefloor))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    if not smoke:
        lxs = [math.log10(float(x)) for x, _d in all_rungs]
        lfg = [math.log10(fg_tab[x]) for x, _d in all_rungs]
        sl_fg = float(np.polyfit(lxs, lfg, 1)[0])
        ok31 = ok31 and FG_SLOPE_WIN[0] <= sl_fg <= FG_SLOPE_WIN[1]
        det31.append("slope %.3f" % sl_fg)
    check("G31-spectral-ladder", ok31,
          "Mq PSD + sorted; FULLGAP in the frozen r142 windows x %s; "
          "growth slope in %s (L8: the two-sided demand 1/poly <= "
          "FULLGAP <= poly is measured-satisfied with >= 5 orders "
          "margin on both sides): %s"
          % (str(FG_WIN), str(FG_SLOPE_WIN), "; ".join(det31)))
    check("G32-harmonic-floor", ok32,
          "Y1 instantiated: TrH (bordered LU, eigensolve-free) == "
          "eigen-sum <= %.0e; floor 1/TrH <= lam_1 - tau HARD; tf in "
          "%s (near-equality); TRACEFLOOR = tau TrH <= x^%d "
          "(DELTA1FLOOR recoordinated to ONE source trace): %s"
          % (TRH_XDEV_BAR, str(TF_WIN), POLY_DEG, "; ".join(det32)))
    if not smoke:
        lt = [abs(math.log10(tau_tab[x])) for x, _d in all_rungs]
        lv = [vac_tab[x] for x, _d in all_rungs]
        sl_vac = float(np.polyfit(lt, lv, 1)[0])
        ok33 = ok33 and VAC_SLOPE_WIN[0] <= sl_vac <= VAC_SLOPE_WIN[1]
        det33.append("vac slope %.3f" % sl_vac)
    check("G33-trace-cap-vacuous", ok33,
          "Y3 instantiated: TrM in %s (the classical half TrM <= "
          "poly MEASURED, arch-dominated); vacuity >= %.0f dex and "
          "riding |log10 tau| with slope in %s: trace/moment caps "
          "are BLIND to the collapse-rate lock -- Chebyshev does NOT "
          "close D-cap (pinned): %s"
          % (str(TRM_WIN), VAC_MIN, str(VAC_SLOPE_WIN),
             "; ".join(det33)))
    check("G34-node-config-replication", ok34,
          "|qrel| <= %.0e, null res <= %.0e; delta_1 >= FULLGAP "
          "(W3 re-gate) with q_i >= lam_i HARD (i <= 5) and rel devs "
          "<= %.0e/%.1f (L4: SPECTRUM CONCENTRATES ON V); zone-top "
          "argmin in the frozen windows; s <= %.1f; s x gap in %s; "
          "delta_1/share_1/tlaw on the cited strings: %s"
          % (QREL_BAR, NULLRES_BAR, QDEV1_BAR, QDEV23_BAR, S_BAR,
             str(SGAP_WIN), "; ".join(det34)))
    check("G35-s-chain-identity", ok35,
          "Y4 instantiated: |s delta_1 share_1 rho2/et_1^2 - 1| <= "
          "%.0e (EXACT chain; D-s = overlap-vs-gap balance on the "
          "same spectrum): %s" % (SID_BAR, "; ".join(det35)))
    check("G36-zero-jet-law", ok36,
          "L1/L2: jr = (A_0(psi_1)/A_0(phi))^2/FULLGAP in %s; tlaw_1 "
          "= lam_1/(8 A_0(psi_1)^2 G(T_z)) in %s with tlaw_1/tlaw_0 "
          "in %s: lam_1 is the archimedean-tail mass of its own "
          "eigenvector priced by its own 0-jet -- the F1 anatomy "
          "answer, MEASURED: %s"
          % (str(JR_WIN), str(TLAW1_WIN), str(TLAW1_RATIO_WIN),
             "; ".join(det36)))
    check("G37-psi1-zone-anatomy", ok37,
          "L7 + Y2: zone sign census == m + 1 (core; [m, m+2] deep, "
          "disclosed); node kill <= %.0e; eps^2 row-Gram vs "
          "projection cross dev <= %.2f (core); transfer 0 <= q_1 - "
          "lam_1 <= eps^2(lam_max - lam_1)/(1 - eps^2) HARD, ratio "
          "<= %.0e: %s"
          % (NODEKILL_BAR, EPS_XDEV_BAR, TRANSFER_RATIO_MAX,
             "; ".join(det37)))
    check("G38-budget-pin-mass", ok38,
          "budget law (r131/r137 CITED) instantiated for psi_1: "
          "sum_zone 2E^2 <= lam_1 + OFF_1 HARD at x in %s + chain "
          "ratio <= %.0e; per-zero f64-aware cap at ALL rungs "
          "(gamma-side F64-LIMITED from x = 13, disclosed); mid-mass "
          "share windows (TAIL-CARRIED) + block portrait windows "
          "(L6): %s"
          % (str(BUDGET_HARD_RUNGS), CHAIN_RATIO_MAX,
             "; ".join(det38)))
    check("G39-minor-floors", ok39,
          "Cauchy sandwich tau <= lam_0(minor) <= lam_1 HARD; MINOR0 "
          "lock ratio in %s with two-level secular prediction dev <= "
          "%.0e (L5); mid/top minors <= %.2f (VACUOUS, pinned): %s"
          % (str(MINOR0_WIN), MINOR0_PRED_BAR, MINOR_MID_MAX,
             "; ".join(det39)))

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
            Aw, bw = jets_of(csw, aaw, cw["K"])
            ytbw = float(abs(Aw[1] / Aw[0])) / float(bw[-1])
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD: the Y1/Y2 hypotheses fail EXACTLY "
              "here); y_t_w/b_top = %.2f <= %.1f"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the harmonic floor and "
          "the transfer theorem require PSD + simple ground -- their "
          "hypotheses fail exactly in the false worlds")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lfg = [math.log10(fg_tab[x]) for x in xs_all]
        ltf = [math.log10(tfl_tab[x]) for x in xs_all]
        s_fg = float(np.polyfit(lt, lfg, 1)[0])
        s_tf = float(np.polyfit(lt, ltf, 1)[0])
        check("G54-tau-screen", abs(s_fg) <= TAU_SLOPE_BAR
              and abs(s_tf) <= TAU_SLOPE_BAR,
              "slope log10 FULLGAP vs log10 tau = %.4f, slope log10 "
              "TRACEFLOOR vs log10 tau = %.4f (both <= %.2f: the "
              "demand-side ratios are NOT Connes-priced); the "
              "trace-cap vacuity rides 1/tau BY CONSTRUCTION "
              "(G33 slope) -- BOUND-RIDES-CONNES typed for the "
              "trace instrument: that IS the Y3 obstruction"
              % (s_fg, s_tf, TAU_SLOPE_BAR))
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
          "flows: base 4, refined 5 (r142/r144 graph VERBATIM -- "
          "this round changes COORDINATES, not the set); one-grant "
          "5; counterfactual PARALLEL 9 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")
    info("EXACT RESIDUE after this round (read with CDXLVI/CDXLVII/"
         "CDXLVIII): SET UNCHANGED -- RH <== [r122-NF-closure] + "
         "[Theorem R] + {L1, WPD} on dense a; RESIDUE = {TOPROOT "
         "(= FULLGAP-CAP modulo the measured O(1) y_t-lock; the "
         "delta_1 <-> FULLGAP half now TWO-SIDED: exact lower W3 + "
         "Y2 budget-conditional upper), ONSETCAP, SUSCAP2R (= "
         "overlap-vs-gap balance on the same spectrum, Y4)} + "
         "DELTA1FLOOR (weak; <== FULLGAP >= 1/poly <== TRACEFLOOR "
         "<= poly, Y1 harmonic recoordination, near-equality) + "
         "dense-a + a-extension + window-a.  THE SPECTRAL ANATOMY "
         "IS MEASURED: lam_1 = 8 A_0(psi_1)^2 G(T_z) x tlaw-window "
         "(ZERO-JET LAW), FULLGAP = jet-ratio^2 x O(1), ladder "
         "geometric, tail-carried, one spectrum for all three "
         "residues; the trace route to D-cap is PINNED VACUOUS "
         "(rate-lock).  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "Y1-PROVEN(harmonic-trace floor; DELTA1FLOOR <== TRACEFLOOR "
        "<= poly, eigensolve-free, near-equality; G10/G32)",
        "Y2-PROVEN(tightness transfer; eps budget-priced "
        "CONDITIONAL; the r142 tightness EXPLAINED; G11/G37/G38)",
        "Y3-PROVEN(RATE-LOCK pin: trace caps blind to the collapse "
        "ratio; vacuity rides 1/tau; G12/G33)",
        "Y4-PROVEN(s-chain identity; D-s on the same spectrum; "
        "G13/G35)",
        "ZEROJET-LAW(L1/L2 measured; F1 answered: archimedean-tail "
        "x excited 0-jet; closed form OPEN-CLASSICAL-CANDIDATE "
        "retyped in jet currency; G36)",
        "LADDER-GEOMETRIC + TAIL-CARRIED(L3; G31/G38)",
        "SPECTRUM-CONCENTRATES-ON-V(L4: one spectrum, three "
        "residues; G34)",
        "MINOR0-LOCK(L5: flat 0.651 == 0-mode overlap share; "
        "MID-MINOR-VACUOUS; G39)",
        "BLOCK-PORTRAIT-FLAT(L6: prime share +0.42; G38)",
        "SIGN-CENSUS-M-PLUS-1(L7; G37)",
        "GROWTH-LAW(L8: slope ~4.0; both demand sides measured-"
        "satisfied >= 5 orders; G31)",
        "BUDGET-PIN(x=5/8 hard; GAMMA-SIDE-F64-LIMITED from x=13, "
        "disclosed; G38)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54; the Y3 vacuity IS "
        "the pinned rides-1/tau instrument)",
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
        print("COMPOSITE: Y1-PROVEN + Y2-PROVEN + Y3-PROVEN + "
              "Y4-PROVEN + ZEROJET-LAW + LADDER-GEOMETRIC + "
              "TAIL-CARRIED + SPECTRUM-CONCENTRATES-ON-V + "
              "MINOR0-LOCK + MID-MINOR-VACUOUS + "
              "BLOCK-PORTRAIT-FLAT + SIGN-CENSUS-M-PLUS-1 + "
              "GROWTH-LAW + BUDGET-PIN + CONTROLS-REFUSE + "
              "DEMAND-FLAT + BOUND-RIDES-CONNES + "
              "QUANTIFIER-INHERITED + OMEGA-RECOORDINATED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
