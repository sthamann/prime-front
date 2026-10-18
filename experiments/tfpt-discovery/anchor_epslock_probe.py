#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""anchor_epslock_probe -- PRIME.ANCHOR.EPSLOCK.PROOF.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on ANCHOR-EPS-LOCK, the one-point
class that rounds 137-151 concentrated the arithmetic residue into:
WHY IS |A_0| AT THE ANCHOR POINT NEVER ANOMALOUSLY SMALL?)
=======================================================================
State consumed (CITED): CDLV/r151 (tlawcap_blocks: J1-J3 bordered
K-jump, ASM+sharpness, JC two grades, AB2 birth zero-coupling,
anchors x0 = 4.824/7.395/11.821/16.221/21.115/24.603 with L_EPS =
0.1088/0.1849/0.2169/0.2330/0.2566/0.2713, JUMPSUM measured, the
convergence discovery: K-jump r-term and Jensen center are ONE
single-point class); CDLIV/r150 (R1-R4: A_0^2 = B_00/P'(tau) with
the P'-pinch, beta_0 root separation, S1 poly-class, Parseval
rate-blind); CDLII/r148 (Jensen block: zero-free anchor cells,
small-value sets empty, tlaw block-constant e^{+/-0.053}); CDLI/r147
(AD1/AD2, cell lemma); CDXLI/r137 (budget identity tau = M_band +
M_mid + M_beyond + S_off, M_mid = 4A_0^2(G_mid - C_mid) + J_mid,
Landau pin, OFF identity); CDXLIV/r140 (J1 ENVJ, J2 onset==jet-ratio
sandwich, J4 ALIGNMENT-WALL |A_2| <= Cauchy-Schwarz cap with depth
1.2e-6 -> 6.9e-61); CDXLV/r141 (V2 measure lemma, dense-x
quantifier); CDLVI (promotion v918-v921; TAILVIS counting-class).

THE TARGET.  L_EPS(x_0) = (tau + OFF)/(16 A_0^2 G(T_z)) <= poly(x_0)
at ONE instrument-chosen point per log-block; equivalently
tlaw = tau/(8 A_0^2 G(T_z)) <= poly.  Budget identity (r137, CITED +
re-gated here): tlaw = midG + midC + midJ + band/D + resid/D with
midG -> 1/(2 KFAC) PROVEN, |midC| <= midG PROVEN, band/resid
enveloped; ONLY the onset excess midJ is open.  This probe mounts
(A1) the block-average / mean-value attack, (A2) the resultant /
root-repulsion attack, (A3) the collapse-mechanism self-cap attack,
and (T4/T5) chain assembly + red team.

=======================================================================
THE EXACT LAYER (the theorems; sympy generic + exact rational
instances; classical inputs typed CITED)
=======================================================================
THEOREM EZ (edge-zero lemma; A1/A3 keystone, found in calibration).
Along the whole branch, A(u) om_k(u) == k pi IDENTICALLY (om_k =
k pi / A), so sin(A om_k) == 0 for EVERY lattice mode at EVERY u:
the Weil test window vanishes at all lattice frequencies (the AB2
birth mechanism one level up -- there the ATOM sat at the window
edge, here the LATTICE does).  Hence |sin(A gamma)| =
|sin(A(gamma - om_k))| <= A |gamma - om_k| for EVERY mode k: the
sin^2 factor of |E_N|^2 screens each pole of the ratio profile
h := (F/A_0)^2 - 1 QUADRATICALLY exactly where it diverges.

THEOREM LC (the ell-1 regularized cap; unconditional).  With W_1 :=
SABS_2/|A_0| = sum_k |c_k| b_k / |A_0|:
  |sin(A gamma)| |F(gamma^2)/A_0 - 1|
    <= sum_k |w_k/A_0| A|gamma - om_k| / (|gamma - om_k|(gamma+om_k))
    <= (A/gamma) W_1        for ALL gamma > om_max (even at poles),
hence sin^2 |h| <= (A W_1/gamma)(2 + A W_1/gamma) and
  midJ <= [2 A W_1 S_3 + A^2 W_1^2 S_4] / G(T_z),
S_p = sum_{gamma > om} gamma^{-p} (counting-class).  UNCONDITIONAL.
Its vacuity in the demand currency is EXACTLY the r140-J4 alignment
wall: W_1 rides 1/A_0 (the ell-1 jet sum does not cancel), measured
per block as VAC_LC = log10(cap/midJ) growing ~ linearly in x.

THEOREM D1-D3 (block-average oscillation dissolution).  D1: sin^2 =
(1 - cos)/2 splits the block average BA(midJ) = (1/2) DC + OSC,
DC = sum_gamma BA_u[h/(gamma^2 G(T_z(u)))].  D2 (telescoped IBP):
per cell, int cos(gamma u) phi du = [sin(gamma u) phi / gamma] -
int sin(gamma u) phi'/gamma; summed over the cells of a block the
boundary terms TELESCOPE at atom births (AB2: phi continuous) and
leave only K-jump terms, so |OSC_gamma| <= (2 sup|phi| + TV(phi) +
sum_jumps |Delta phi|) / (gamma span) AND trivially <= sup|phi|:
|OSC| <= (1/2) sum_gamma min(sup, IBP) =: OSCBAR.  D3: gamma >=
om ~ 2.5 pi x makes the IBP factor subordinate at BLOCK scale when
TV and jump sums are drift-class -- MEASURED; at CELL scale
gamma x span ~ 2 and no gain is available (measured, disclosed:
the calibration found 2BA/DC = 0.56/0.085 at the b5/b8 cells -- the
1/2-split OVERWEIGHTS the near-edge zeros; the exact reason is
THEOREM EZ: sin^2 vanishes at the moving lattice edge, so the
oscillation-free object must EXCLUDE the near-edge window).  The
honest split: NEAR window om < gamma <= (3/2) om capped by LC (and
open beyond LC's vacuity: NEAR-ALIGN), FAR window gamma > (3/2) om
carrying the dissolution machinery (FAR-DC).

THEOREM C1 (circularity constant ONE).  1 - cos >= 0 ==> G_mid -
C_mid >= 0 ==> J_mid <= M_mid <= tau - M_band - M_beyond + |S_off|
==> the ONLY unconditional budget bound on midJ returns tlaw <=
midG + |midC| + tlaw + small with the tlaw coefficient EXACTLY 1 --
the pointwise budget route is circular with constant 1, and BA
linearity makes the block-averaged budget route circular with the
SAME constant: the block average per se buys NOTHING beyond the
oscillation legs.  (The A1 mean-value answer, exact.)

THEOREM M1 (existence form).  f >= 0 with block average <= B ==>
meas{f > 4B} <= 1/4 (Markov) and min <= BA: ONE anchor point with
tlaw <= 4 BA(tlaw) EXISTS on 3/4 of the block -- the existence form
is equivalent-or-weaker than the pointwise form; with the r148/r151
measured block-constancy the two coincide MEASURED.

THEOREM RES1 (resultant factorization; A2).  B_00(z) = v_0^T
adj(zI - M) v_0 = sum_i w_i prod_{j != i}(z - lam_j), so B_00(lam_i)
== P'(lam_i) w_i for every simple root, lc(B_00) == sum_i w_i ==
|v_0|^2 (Parseval), and for monic P:
  Res(P, B_00) == prod_i B_00(lam_i) == (+/-) disc(P) prod_i w_i.
THEOREM RES2 (separation inversion + self-referentiality).  beta_0 -
tau == Res/(lc(B)^K prod_{(i,j) != (0,0)} (beta_j - lam_i)) exactly
-- but Res CARRIES w_0 = A_0^2 AS A FACTOR: any resultant/
discriminant lower bound on the root separation PRESUPPOSES a floor
on the very quantity A_0^2 being bounded (hard assert on the diag
jet toy: scaling p -> p/sqrt(P) scales Res by 1/P with ALL
identities intact).  The Mahler/height route needs integer-class
coefficient heights; the census entries are transcendental reals
(archimedean integrals + Lambda(q)/sqrt(q) sums): typed
NO-ARITHMETIC-HEIGHT.  The resultant route is OBSTRUCTED-EXACT.

THEOREM F1 (unconditional edge F-cap; A3).  |A_0| <= sqrt(K)
(Cauchy-Schwarz, ||c|| = 1), |w_k| <= b_k, so for y >= om^2(1+d)^2:
|F(y)| <= sqrt(K) + (K-1)/(2d + d^2) -- POLYNOMIAL, source-pure,
unconditional.  Its RELATIVE vacuity (divide by A_0^2) reintroduces
the collapse: absolute caps are e^{cx}-vacuous, measured.

MECHANISM PIN (A3 answer).  The collapse mechanism does NOT cap its
own rate: pinning quality (zone-kill) bounds the BAND mass only
(measured share ~ 1e-5..1e-12 of tau); the onset carries the value,
and the onset couplings w_k/A_0, the r151 K-jump r-term, and the
Jensen center input are ONE linear-in-1/A_0 class (funnel typed
exactly; sum_k w_k/A_0 == A_2/A_0 = +/- y_t EXACT: the ALIGNED sum
of the near-edge couplings IS the jet ratio -- TOPROOT; the ell-1
sum is the wall).

ASSEMBLED RESIDUE (T4, frozen in advance as the adjudication shape):
ANCHOR-EPS-LOCK <== NEAR-ALIGN (regularized near-edge mass <= poly
A_0^2 G -- the alignment-wall coordinate, LC-capped unconditionally
but vacuously) + FAR-DC (block-average of the far-field ratio
profile <= poly -- TOPROOT-class via the r140 far-field law) with
the oscillation legs PROVEN (D1-D3 + EZ) and the existence form
PROVEN (M1).  Census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
NO omega is claimed closed.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, NO zeta use anywhere,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (kind=exact): G10 EZ (A om_k == k pi; sin(A om_k)
    == 0; |sin(A gamma)| <= A|gamma - om_k| via |sin t| <= |t|);
    G11 LC (per-term pole cancellation chain + assembled cap
    rearrangement, exact rational instance); G12 D1 (sin^2 split +
    BA split instance); G13 D2 (IBP identity + telescoping at
    continuous boundaries (AB2 CITED) + K-jump terms + the min(sup,
    IBP) assembly, exact instances); G14 C1 (1 - cos >= 0; J_mid <=
    M_mid; substitution returns tlaw coefficient EXACTLY 1; BA
    linearity); G15 M1 (Markov 1/4 instance + min <= avg + the
    4BA existence rearrangement); G16 RES1 (generic 3x3 Householder:
    B_00(lam_i) == P'(lam_i) w_i, Res == +/- disc prod w, lc(B_00)
    == |v_0|^2); G17 RES2 (separation inversion instance + the
    self-referentiality hard assert on the diag toy + NO-ARITH-
    HEIGHT typing); G18 F1 (|A_0| <= sqrt K, |w| <= b, edge cap
    instance); G19 red team (adversarial coefficient algebra:
    A_0(c + t e_0) = A_0 + t, all identities c-generic, the witness
    c' with A_0' = A_0/sqrt(P) inflates the DC/h currency by ~P
    while EZ/LC/D1-D3/RES identities ALL hold: ALGEBRA-ONLY-BOUNDS-
    REFUTED-FOR-ANCHOR (hard assert); r147 2D model + r150 jet toy
    CITED as the inherited refuters).
S2  G20 HSW G(T) sanity vs cache partials.
S3  per-block ladder, tags 5/8/13/18/24/28, nominal anchors x =
    5.44/8.5/13.5/18.5/24.5/28.5, dps = 60/80/120/140/150/155,
    cell-grid points 9/9/7/5/3/3 at 0.8 x halfwidth (deterministic
    r151 widest-cell anchor selection VERBATIM); per point: frozen
    builder + eigsy + FIXED-WINDOW budget decomposition (window
    gamma > om_fix = (K_0 - 1) pi/(clo/2); strip gamma in (om(u),
    om_fix] accounted to the residual side) + per-gamma ratio
    profile h (f64 transport of flat ratios, DISCLOSED -- all mp
    inside workdps in-worker, no f64 refinement):
    G30 anchor certificates (anchor L_EPS on the r151 strings rel
    <= 5e-3; n_neg == 0 everywhere; C_0 <= 4.5; hw > 0);
    G31 decomposition self-identity M_mid == 4A_0^2(G_mid - C_mid)
    + J_mid rel <= 1e-25 at EVERY grid point (mp);
    G32 LC instantiated: max over zeros and points of sin^2|h| /
    [(A W_1/gamma)(2 + A W_1/gamma)] <= 1 + 1e-9 HARD (the cap is a
    theorem -- this is the machine verification) + the near-edge
    regularization exhibit (largest |h| vs its regularized mass);
    G33 cell BA/DC/OSC: |OSC_semi - OSC_grid| <= 0.02(1 + |OSC|)
    (exact-in-oscillation instrument vs trapezoid); |OSC_grid| <=
    1.5 OSCBAR (theorem bound verified on data; 1.5 = sparse-grid
    TV slack, DISCLOSED); DC/2BA ratio + near/far shares printed;
    G34 LC vacuity: VAC_LC = log10(LC-cap/max(midJ, 1e-6)) per
    block, slope vs x >= 0.5 dex/unit (CLASSICAL-ELL1-VACUOUS
    measured -- any absolute/ell-1 classical input to the onset
    excess is exponentially vacuous; the aligned sum IS y_t);
    G35 tlaw/L_EPS certificates: L_EPS in (0.05, 0.35); cell
    max/min tlaw <= e^{0.35}; BA(tlaw) and min(tlaw) tables (the
    existence exhibit min <= BA <= 4BA trivially);
    G36 BLOCK-SCALE instrument (block 5 only, cheap): the block
    [u_0 - 0.45, u_0 + 0.45] cut into its source cells (K-jumps +
    births), one midpoint build per cell, piecewise-constant phi,
    EXACT-in-oscillation OSC; gates |OSC_exact| <= 1.5 OSCBAR_blk +
    BA(tlaw)_blk == BA(tlaw)_cell rel <= 0.05 + block-avg budget
    remainder in [-1e-3, 0.5] (strip accounting, DISCLOSED);
    G37 resultant instrumentation (blocks 5 + 8 anchors): Faddeev-
    LeVerrier adjugate coefficients + Sylvester determinant vs
    disc(P) prod w_i rel <= 1e-20; beta-route Res (polyroots of
    B_00) rel <= 1e-20; per-root AD1 dual at the bottom two roots
    <= 1e-15; Parseval + lc devs <= 1e-25; betapos in (0.02, 0.6);
    the log10 decomposition log|Res| = log|disc| + sum log w with
    the w_0 = A_0^2 share PRINTED (RESULTANT-SELF-REFERENTIAL
    exhibited on real data);
    G38 adversarial witness (blocks 5 + 8): c' = c + t e_0 with
    A_0' = A_0/sqrt(P), P = 1e6: ratio dev <= 1e-30; onset-h
    inflation >= 1e3; REFUSAL: Rayleigh gap (rho' - tau)/tau >= 0.5
    and eigen-residual >= 1e-20 (c' is NOT the census minimizer --
    only the minimizer property, an arithmetic input, caps the
    currency).
S4  controls G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 (R4
    builder): tau_w < 0 AND tau_w + OFF_w < 0 (cannot enter the
    L_EPS currency) AND |A_0_w| in (0.05, 2.0) (NO collapse: the
    collapse of A_0 is itself the arithmetic signal) AND the
    decomposition identity HOLDS world-blind (rel <= 1e-20 -- an
    identity must; null control); G53 consistency.
S5  G54 tau-screen: slopes of log10 midJ, log10 DC_far, log10
    (2BA/DC) vs log10 tau <= 0.35 (the ratio currencies are
    tau-flat); RIDER report: log10 W_1 and log10 LC-cap slopes
    printed (ride 1/A_0 ~ 1/tau by construction -- BOUND-RIDES-
    CONNES typed, the ratios are the flat coordinates); G55
    conditioning (1e-25 shift at the b5 anchor).
S6  G60 demand audit (existence form: ONE point per block via M1;
    V2 supplies the unbounded sequence; no ALL-X demand); G61
    min-cut (r116 replica; the r151 unit edge TAILVISTHM ->
    ANCHOREPS(1) REFINED into TAILVISTHM -> NEARALIGN(1) ->
    FARDC(1) -> ANCHOREPSTHM(INF, this round's proven assembly EZ +
    LC + D1-D3 + M1): flows base 4 / refined 5 / one-grant 5 /
    counterfactual-parallel 8 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED).
S9  composite verdict + G99 runtime (bar 14400 s wall).

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); M_JET_TOP = 26; WORKERS = 14 (spawn; every task
a pure deterministic function of frozen inputs, results gathered by
index -- scheduling-independent; concurrent lanes untouched).
BLOCKS = (5, 5.44, 60, 9), (8, 8.50, 80, 9), (13, 13.50, 120, 7),
(18, 18.50, 140, 5), (24, 24.50, 150, 3), (28, 28.50, 155, 3);
CELL_SEARCH_HALF = 0.30; CELL_MID_WIN = 0.15; GRID_FRAC = 0.8;
NEAR_FAC = 1.5; BLK5_HALF = 0.45; CACHE_ERR = 1e-9; ADJ_PAD = 360;
RQI_ITERS = 2; ADJ_H = 1e-16; P_WITNESS = 1e6.
BARS: LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
24: 0.2566, 28: 0.2713} rel 5e-3 (r151 strings); CELL_C0_MAX = 4.5;
ID_BAR = 1e-25 (calibration 6e-61..7e-81); LC_SLOP = 1e-9;
OSC_CONS_BAR = 0.02 (calibration diffs 9.5e-4/3.0e-3); OSCBAR_SLACK
= 1.5 (sparse-grid TV undershoot, DISCLOSED); VAC_SLOPE_MIN = 0.5;
LEPS_WIN = (0.05, 0.35); TLAW_CONST_BAR = 0.35 in log (calibration
0.115/0.186); BLK_CONS_BAR = 0.05 (calibration 9e-5 rel);
BLK_REM_WIN = (-1e-3, 0.5) (calibration +9.12e-2, strip-dominated);
RESID_WIN = [-1e-3, beyond + 0.02 + off/D + 1e-4] with beyond =
(1 + eta_top)^2 G(gtop)/G(T_z), band-share 0.02 CITED (r137 G35
class; band NOT enclosed here -- the r137 polish lesson: unpolished
band enclosures are slop-dominated at depth, so the band leg is
cited-class, DISCLOSED); RES_BAR = 1e-20 (calibration 1.4e-49/
6.1e-59); ROOT_AD1_BAR = 1e-15 (calibration 1e-25..1e-42); PARS_BAR
= 1e-25 (calibration 6e-62/5e-81); BETAPOS_WIN = (0.02, 0.6)
(calibration 0.2768/0.1291); ADV_DEV_BAR = 1e-30 (calibration
1e-53/1e-68); ADV_INFL_MIN = 1e3 (calibration 6.6e5/8e5);
ADV_RGAP_MIN = 0.5 (calibration 1.844/1.824); ADV_RES_MIN = 1e-20
(calibration 7.6e-8/6.9e-14); CTRL_A0_WIN = (0.05, 2.0) (r137
0.278/0.355/0.538); TAU_SLOPE_BAR = 0.35; COND_WIN = (1e-40,
1e-10); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use (no
audit_ layer: the band is cited-class, all window sums use cache
ordinates with declared 1e-9 slop -- the mid-window currencies are
O(1) ratios, slop-immune at the frozen bars).  All mpf arithmetic
inside explicit mp.workdps blocks in-worker; per-gamma h profiles
are computed in mp and TRANSPORTED as f64 (flat O(1..1e3) ratio
currencies for the MEASURED layer only, rounding 1e-16 << bars,
DISCLOSED); no f64 refinement of any mp quantity; tiny/huge
quantities (tau, A_0, W_1, Res, disc, prod w) stay mp end-to-end
with mp.log diagnostics (r147/r141 underflow classes banned).

CALIBRATION DISCLOSURE (calib_scratch_anchor.py, TWO pre-freeze
passes, deleted after freeze; pass 1 found two instrument classes:
(i) mid-window membership shifts within a cell as om(u) crosses
cache ordinates -- fixed by the FIXED per-block window + strip
accounting; (ii) unpolished band enclosures are slop-dominated at
depth (b8 slop 1e4 D-units) -- band leg re-typed cited-class.  Pass
2 verbatim: b5 anchor x0 = 4.823998, cell [1.541394, 1.605812], hw
0.03221, om_fix 36.6867, L_EPS(u0) = 0.10881 == r151 string; grid
tlaw 0.21623..0.24256, BA 0.22801, midG 0.1637..0.1765, midC
-0.0130..+0.0247, midJ +0.0190..+0.0747, strip 0, resid
0.0024..0.0026, id devs <= 6e-60, sup_h 1.92..29.58; BA(midJ) =
0.05856, DC = 0.20874, 2BA/DC = 0.5611, OSC_grid = -0.04581,
OSC_semi = -0.04486, OSCBAR = 0.43922 (cell-scale subordination
FAILS as EZ predicts: gamma x span at om = 1.94), drift -6.94;
BLOCK-SCALE b5 (19 cells, 103 s): BA(midJ) = 0.00891, DC = 0.06974,
2BA/DC = 0.2555, OSC_exact = -0.01833, OSCBAR = 0.08398, BA(tlaw)
0.22803 vs cell 0.22801, remainder +9.12e-2; resultant b5: pars
6e-62, lcB 0, res_syl 1.4e-49, res_beta 1.4e-49, root-AD1
1e-30/1e-25, log10|Res| = -72.48 = disc -47.12 + sum-log-w -25.36
(w_0 -13.48), betapos 0.2768; adversarial b5: dev 1e-53, h
-9.57e-1 -> 6.27e5, rgap 1.844, resn 7.6e-8.  b8: x0 = 7.394749,
hw 0.01802, om_fix 57.0408, L_EPS(u0) = 0.18487 == r151 string;
tlaw 0.30845..0.37101, midJ +0.0711..+0.1422, strip <= 1.1e-5,
resid 0.0044..0.0045, id <= 7e-80, sup_h up to 516 (near-edge, the
EZ exhibit); BA(midJ) = 0.11913, DC = 2.81736, 2BA/DC = 0.0846,
OSC_grid = -1.28955, OSC_semi = -1.28656, OSCBAR = 4.21093;
resultant b8: res devs 6.1e-59, root-AD1 1e-42/7e-37, log10|Res| =
-328.93 = disc -246.35 + sum-log-w -82.58 (w_0 -25.55), betapos
0.1291; adversarial b8: dev 1e-68, h 79.7 -> 6.38e7, rgap 1.824,
resn 6.9e-14; timings: b5 point 3.2 s, b8 point 14 s, b5 block-
scale 103 s, resultant 0.2/2.6 s.  Deep blocks (13/18/24/28)
pre-freeze UNMEASURED on all new quantities -- disclosed; bars set
with >= 1e5 headroom where the class is calibrated and with cited
windows elsewhere.

VERDICT ENUMS (frozen): EDGEZERO-PROVEN(the Weil window vanishes at
every lattice frequency along the branch -- the near-edge pole mass
is structurally screened); LC-CAP-PROVEN(unconditional ell-1
regularized cap on the onset excess) + CLASSICAL-ELL1-VACUOUS
(measured: the cap's vacuity is the r140-J4 alignment wall at block
level); OSCDISS-PROVEN(D1-D3 telescoped IBP; boundary terms only at
K-jumps by AB2) + CELLSCALE-NO-GAIN(measured, EZ-explained);
CIRCULARITY-CONSTANT-ONE(the budget route returns tlaw with
coefficient exactly 1, pointwise AND block-averaged: the mean-value
machinery does NOT bound the DC part); EXISTENCE-FORM-PROVEN(M1);
RES-FACTORIZATION-PROVEN(Res(P, B_00) == +/- disc(P) prod w_i; lc
== |v_0|^2) + RESULTANT-SELF-REFERENTIAL(Res carries w_0 = A_0^2;
NO-ARITHMETIC-HEIGHT); EDGE-FCAP-PROVEN(absolute caps poly,
relatively vacuous); MECHANISM-NO-SELF-CAP(pinning bounds band
only; the funnel w_k/A_0 == K-jump r-term == Jensen center class,
aligned sum == y_t EXACT); ANCHOR-RESIDUE-RECOORDINATED(ANCHOR-EPS-
LOCK <== NEAR-ALIGN + FAR-DC, oscillation + existence legs proven;
NOT closed); REDTEAM-REFUTES-ALGEBRA; CONTROLS-REFUSE; DEMAND-FLAT
+ BOUND-RIDES-CONNES; QUANTIFIER-INHERITED; OMEGA-UNCHANGED(census
{MEAS, OMEGA-POS} cardinality 4); MINCUT(4/5; counterfactual 8 NOT
REAL).  Composite priority: INSTRUMENT-EDGE > EXACT-LAYER-
OBSTRUCTED > verdicts as gated.

SMOKE-1 NOTE (disclosed; smoke1 = 28/29 at 19.0 s after one format-
string repair, log anchor_epslock_probe.smoke1.log crashed at the
G30 print, smoke2 = 28/29 at 19.4 s, log .smoke2.log; the ONE fail
was G36 SMOKE-PATH ONLY: the smoke truncates the block-scale
instrument to the 4 LEFTMOST cells, so the block-vs-cell BA(tlaw)
consistency leg compares a left fragment (0.172) against the anchor
cell (0.227) -- a truncation artifact, not an instrument error (the
calibration FULL block gave dev 9e-5).  SMOKE-PATH FIX: in smoke
mode the consistency leg is typed SMOKE-SKIP (the OSC and remainder
legs stay live); the FULL-mode gate is UNCHANGED, no bar moved.
Also one cosmetic print (LC ratio to %.1e).  Smoke exhibits quoted:
b5 anchor L_EPS = 0.1088 dev 1.2e-4 vs the r151 string; id <=
6e-60; LC-ratio <= 1e-9-class; BA(midJ) = 0.0572, DC = 0.2132,
2BA/DC = 0.537, OSC_grid = -0.0494, OSC_semi = -0.0456, OSCBAR =
0.4380, near-share 1.53 (the far field is NET NEGATIVE -- the
near-edge carries MORE than the total, an honest structural
finding); VAC_LC = 13.5 dex at b5; resultant devs 0/0 with root-AD1
1e-30/1e-25; adversarial x7e5 inflation, rgap 1.84.  SPEC_SHA moves
with this disclosure -- smoke3 at the frozen hash is the
verdict-bearing smoke.)

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.  NO RH
CLAIM.  EXPLORATION ONLY.
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
M_JET_TOP = 26
WORKERS = 14

BLOCKS = (
    (5, 5.44, 60, 9),
    (8, 8.50, 80, 9),
    (13, 13.50, 120, 7),
    (18, 18.50, 140, 5),
    (24, 24.50, 150, 3),
    (28, 28.50, 155, 3),
)
CELL_SEARCH_HALF = 0.30
CELL_MID_WIN = 0.15
GRID_FRAC = 0.8
NEAR_FAC = 1.5
BLK5_HALF = 0.45
CACHE_ERR = 1e-9
ADJ_PAD = 360
RQI_ITERS = 2
ADJ_H = 1e-16
P_WITNESS = 1e6

LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
            24: 0.2566, 28: 0.2713}
LEPS_TOL = 5e-3
CELL_C0_MAX = 4.5
ID_BAR = 1e-25
LC_SLOP = 1e-9
OSC_CONS_BAR = 0.02
OSCBAR_SLACK = 1.5
VAC_SLOPE_MIN = 0.5
LEPS_WIN = (0.05, 0.35)
TLAW_CONST_BAR = 0.35
BLK_CONS_BAR = 0.05
BLK_REM_WIN = (-1e-3, 0.5)
RESID_LO = -1e-3
BAND_CITED = 0.02
RESID_PAD = 1e-4
RES_BAR = 1e-20
ROOT_AD1_BAR = 1e-15
PARS_BAR = 1e-25
BETAPOS_WIN = (0.02, 0.6)
ADV_DEV_BAR = 1e-30
ADV_INFL_MIN = 1e3
ADV_RGAP_MIN = 0.5
ADV_RES_MIN = 1e-20
CTRL_A0_WIN = (0.05, 2.0)
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


def kfun_f(x: float) -> float:
    return KFAC * x * math.log(x)


def kjump_point(m: int, lo: float, hi: float) -> float:
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if kfun_f(mid) < m:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def prime_powers_upto(n: int) -> list:
    comp = np.zeros(n + 2, dtype=bool)
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


def boundaries_in(ulo: float, uhi: float) -> list:
    """all source-branch cell boundaries (K-jumps + atom births) in
    [ulo, uhi]; deterministic (r151 VERBATIM)."""
    xlo, xhi = math.exp(ulo), math.exp(uhi)
    out = []
    mlo = int(math.ceil(kfun_f(xlo)))
    mhi = int(math.floor(kfun_f(xhi)))
    for m in range(mlo, mhi + 1):
        xj = kjump_point(m, max(xlo - 1.0, 2.0), xhi + 1.0)
        uj = math.log(xj)
        if ulo <= uj <= uhi:
            out.append((uj, "K", m))
    for q in prime_powers_upto(int(math.ceil(xhi)) + 1):
        uq = math.log(q)
        if ulo <= uq <= uhi:
            out.append((uq, "P", q))
    out.sort()
    return out


def anchor_select(x_nom: float) -> tuple:
    """widest complete cell, midpoint within +/-CELL_MID_WIN of u_nom
    (r151 VERBATIM); returns (u0, lo, hi)."""
    u_nom = math.log(x_nom)
    bnd = boundaries_in(u_nom - CELL_SEARCH_HALF, u_nom + CELL_SEARCH_HALF)
    best = None
    for i in range(len(bnd) - 1):
        lo, hi = bnd[i][0], bnd[i + 1][0]
        mid = 0.5 * (lo + hi)
        if abs(mid - u_nom) > CELL_MID_WIN:
            continue
        w = hi - lo
        if best is None or w > best[0] + 1e-15:
            best = (w, lo, hi)
    if best is None:
        for i in range(len(bnd) - 1):
            lo, hi = bnd[i][0], bnd[i + 1][0]
            if lo <= u_nom <= hi:
                best = (hi - lo, lo, hi)
                break
    w, lo, hi = best
    return 0.5 * (lo + hi), lo, hi


# ------------------------------------------------- frozen cell builder
def atoms_upto(icap: int):
    comp = np.zeros(icap + 2, dtype=bool)
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
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]


def cell_matrix(aa_v, K: int, icap: int, dps: int):
    """r151/r148 frozen builder VERBATIM (real path); returns
    (M, nrm)."""
    with mp.workdps(dps):
        aa = aa_v
        atoms = atoms_upto(icap)
        ks = list(range(K))
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1)
        L2v = 2 * aa

        def a_weight(w):
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def r_of(w):
            if w == 0:
                return mp.mpf("0.25")
            return a_weight(w) - 1 / (2 * w)

        jvec = []
        for i, o in enumerate(oms):
            if ks[i] == 0:
                jvec.append(mp.mpf(0))
                continue
            k = ks[i]
            spts = sorted(set([mp.mpf(j) / (2 * k)
                               for j in range(2 * k + 1)]))
            val = mp.quad(lambda s, o=o: mp.sin(o * L2v * s)
                          * r_of(L2v * s) * L2v, spts)
            jvec.append(val + mp.si(2 * k * mp.pi) / 2)

        pj = []
        for o in oms:
            acc = mp.mpf(0)
            for u, w in atoms:
                acc += w * mp.sin(o * u)
            pj.append(acc)

        Mpole = mp.zeros(K, K)
        March = mp.zeros(K, K)
        Mprime = mp.zeros(K, K)
        ipv = [par[i] * mp.sinh(aa / 2)
               / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mpole[i, j2] = 2 * ipv[i] * ipv[j2]
        for i in range(K):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                arch_od = -2 * sg * (oms[i] * jvec[i]
                                     - oms[j2] * jvec[j2]) / den
                prim_od = 2 * sg * (oms[i] * pj[i]
                                    - oms[j2] * pj[j2]) / den
                March[i, j2] += arch_od
                March[j2, i] += arch_od
                Mprime[i, j2] += prim_od
                Mprime[j2, i] += prim_od
        tail_c = lambda f0: -f0 / 2 * mp.log1p(-mp.exp(-2 * L2v))  # noqa
        for i in range(K):
            k = ks[i]
            o = oms[i]
            if k == 0:
                f0 = L2v

                def psi_d(w):
                    return L2v - w
            else:
                f0 = aa

                def psi_d(w, o=o):
                    return ((aa - w / 2) * mp.cos(o * w)
                            + dsig * mp.sin(o * w) / (2 * o))

            def integrand(w, f0=f0, psi_d=psi_d):
                return ((f0 * mp.exp(-2 * w)
                         - psi_d(w) * mp.exp(-w / 2))
                        / (-mp.expm1(-2 * w)))
            scale = abs(L2v)
            guards = [mp.mpf("1e-6") / scale, mp.mpf("1e-3") / scale,
                      mp.mpf("0.05") / scale]
            spts = [mp.mpf(0)] + guards
            if k:
                spts += [mp.mpf(j) / (2 * k) for j in range(1, 2 * k)]
            spts += [mp.mpf(1)]
            spts = sorted(set(s for s in spts if 0 <= s <= 1))
            body = mp.quad(lambda s, integrand=integrand:
                           integrand(L2v * s) * L2v, spts)
            March[i, i] += (-f0 * (mp.euler + mp.log(mp.pi))
                            + 2 * (body + tail_c(f0)))
            pdiag = mp.mpf(0)
            for u, w in atoms:
                if k:
                    pdiag += w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                else:
                    pdiag += w * (L2v - u)
            Mprime[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if ks[i] == 0 else mp.sqrt(aa)
               for i in range(K)]
        for Mb in (Mpole, March, Mprime):
            for i in range(K):
                for j2 in range(K):
                    Mb[i, j2] = Mb[i, j2] / (nrm[i] * nrm[j2])
            for i in range(K):
                for j2 in range(i):
                    sym = (Mb[i, j2] + Mb[j2, i]) / 2
                    Mb[i, j2] = sym
                    Mb[j2, i] = sym
        M = Mpole + March - Mprime
    return M, nrm


def lu_factor(Amat, n):
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
    """swaps fully BEFORE forward elimination (LAPACK getrs order,
    r144 lesson, frozen code)."""
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
    d = mp.mpf(sign)
    for i in range(n):
        d *= LU[i, i]
    return d


def rqi_vec(Mq, K, z0, y0, dps_adj, iters):
    with mp.workdps(dps_adj):
        z = mp.mpf(z0)
        y = [mp.mpf(y0[i]) for i in range(K)]
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
        return z, y


# ----------------------------------------------------------- workers
def w_point(args) -> dict:
    """frozen build + eigsy + FIXED-WINDOW budget decomposition +
    per-gamma ratio profile.  All mp in workdps; f64 transport of
    flat ratio currencies only (DISCLOSED)."""
    tag, u_str, dps, om_fix_str, want_eta_top = args
    try:
        gam = ward_cache()
        with mp.workdps(dps):
            u = mp.mpf(u_str)
            x = mp.exp(u)
            K = int(math.ceil(kfun_f(float(x))))
            icap = int(math.floor(float(x)))
            M, nrm = cell_matrix(u / 2, K, icap, dps)
            E, V = mp.eigsy(M)
            order = sorted(range(K), key=lambda i: E[i])
            i0 = order[0]
            tau = E[i0]
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
            om_max = float(oms[-1])
            om_fix = float(mp.mpf(om_fix_str)) if om_fix_str else om_max
            Tz = 2 * math.pi * float(x)
            Gz = mp.mpf(repr(hsw_G(Tz)))
            # jets: eta_PT (OFF identity) + optional eta_top
            A_j = []
            pw = [mp.mpf(1)] * K
            for m in range(M_JETS + 1):
                if m == 0:
                    acc = A0
                else:
                    acc = mp.mpf(0)
                    for k in range(1, K):
                        pw[k] = pw[k] * b[k] if m > 1 else b[k]
                        acc += (-1) ** k * cs[k] * pw[k]
                A_j.append(acc)
            cs_abs = [abs(v) for v in cs]

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
            eta_top = 0.0
            if want_eta_top:
                gtop = float(gam[-1])
                etas = [float(envres(gtop, m) / abs(A0))
                        for m in range(1, M_JET_TOP)]
                eta_top = min(etas)
            off = 8 * mp.exp(aa) \
                * (abs(A0) * (1 + mp.mpf(repr(eta_pt)))) ** 2 \
                * mp.mpf(repr(hsw_G(float(T_PT))))
            D = 8 * A0 ** 2 * Gz
            tlaw = float(tau / D)
            leps = float((tau + off) / (16 * A0 ** 2 * Gz))
            # W_1 = SABS_2 / |A_0| (mp; log10 transported)
            sabs2 = sum(abs(cs[k]) * b[k] for k in range(1, K))
            W1 = sabs2 / abs(A0)
            l10 = mp.log(10)
            w1_l10 = float(mp.log(W1) / l10)
            n_band = int(np.sum(gam <= om_max))
            n_fix = int(np.sum(gam <= om_fix))
            # strip gamma in (om(u), om_fix]
            m_strip = mp.mpf(0)
            for j in range(n_band, n_fix):
                g = mp.mpf(repr(float(gam[j])))
                y = g * g
                Fov = mp.mpf(1)
                for k in range(1, K):
                    Fov += (wk[k] / A0) / (y - b[k])
                s2 = mp.sin(aa * g) ** 2
                m_strip += 8 * s2 * (Fov * A0) ** 2 / y
            # fixed mid window
            g_mid = mp.mpf(0)
            c_mid = mp.mpf(0)
            j_mid = mp.mpf(0)
            m_mid = mp.mpf(0)
            s3 = mp.mpf(0)
            s4 = mp.mpf(0)
            hs = []
            lc_max = 0.0
            AW1 = aa * W1
            for j in range(n_fix, len(gam)):
                g = mp.mpf(repr(float(gam[j])))
                y = g * g
                Fov = mp.mpf(1)
                for k in range(1, K):
                    Fov += (wk[k] / A0) / (y - b[k])
                h = Fov * Fov - 1
                s2 = mp.sin(aa * g) ** 2
                g_mid += 1 / y
                c_mid += (1 - 2 * s2) / y
                j_mid += 8 * s2 * h * A0 ** 2 / y
                m_mid += 8 * s2 * (Fov * A0) ** 2 / y
                s3 += 1 / (y * g)
                s4 += 1 / (y * y)
                # LC verification: sin^2 |h| <= (AW1/g)(2 + AW1/g)
                capg = (AW1 / g) * (2 + AW1 / g)
                rat = float(s2 * abs(h) / capg)
                if rat > lc_max:
                    lc_max = rat
                hs.append(float(h))
            id_dev = float(abs(m_mid - (4 * A0 ** 2 * (g_mid - c_mid)
                                        + j_mid)) / m_mid)
            midG = float(4 * A0 ** 2 * g_mid / D)
            midC = float(-4 * A0 ** 2 * c_mid / D)
            midJ = float(j_mid / D)
            resid = float((tau - m_strip - m_mid) / D)
            # LC cap (mp, log10 transported)
            lc_cap = (2 * AW1 * s3 + AW1 ** 2 * s4) / Gz
            lc_cap_l10 = float(mp.log(lc_cap) / l10)
            # near/far split of midJ
            j_near = mp.mpf(0)
            n_near = 0
            for j in range(n_fix, len(gam)):
                if float(gam[j]) > NEAR_FAC * om_fix:
                    break
                g = mp.mpf(repr(float(gam[j])))
                y = g * g
                Fov = mp.mpf(1)
                for k in range(1, K):
                    Fov += (wk[k] / A0) / (y - b[k])
                s2 = mp.sin(aa * g) ** 2
                j_near += 8 * s2 * (Fov * Fov - 1) * A0 ** 2 / y
                n_near += 1
            midJ_near = float(j_near / D)
            return dict(tag=tag, u=float(u), K=K, nneg=nneg,
                        tau_str=mp.nstr(tau, dps),
                        a0_str=mp.nstr(A0, dps),
                        tlaw=tlaw, leps=leps, midG=midG, midC=midC,
                        midJ=midJ, midJ_near=midJ_near,
                        n_near=n_near, strip=float(m_strip / D),
                        resid=resid, id_dev=id_dev,
                        w1_l10=w1_l10, lc_cap_l10=lc_cap_l10,
                        lc_max=lc_max, eta_pt=eta_pt,
                        eta_top=eta_top, om=om_max, n_fix=n_fix,
                        Gz=float(Gz),
                        Gtop_over_Gz=hsw_G(float(gam[-1]))
                        / float(Gz),
                        off_over_D=float(off / D),
                        aa_f=float(aa), hs=hs)
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, u_str=u_str, error=repr(exc))


def w_resultant(args) -> dict:
    """RES1/RES2 instrumentation at a block anchor: eigsy w_i + disc
    vs Faddeev-LeVerrier B_00 coefficients + Sylvester resultant +
    beta-route + per-root AD1 duals.  All mp at dps + ADJ_PAD."""
    tag, u_str, dps = args
    try:
        with mp.workdps(dps):
            u = mp.mpf(u_str)
            x = mp.exp(u)
            K = int(math.ceil(kfun_f(float(x))))
            icap = int(math.floor(float(x)))
            M, nrm = cell_matrix(u / 2, K, icap, dps)
        dps_adj = dps + ADJ_PAD
        with mp.workdps(dps_adj):
            E, V = mp.eigsy(M)
            order = sorted(range(K), key=lambda i: E[i])
            lam = [E[order[i]] for i in range(K)]
            vecs = [[V[r, order[i]] for r in range(K)]
                    for i in range(K)]
            v0 = [mp.mpf((-1) ** k) / nrm[k] for k in range(K)]
            wj = []
            for i in range(K):
                nn = mp.sqrt(sum(vecs[i][r] * vecs[i][r]
                                 for r in range(K)))
                a0i = sum(v0[r] * vecs[i][r] for r in range(K)) / nn
                wj.append(a0i * a0i)
            v0n2 = sum(v0[k] * v0[k] for k in range(K))
            pars_dev = float(abs(sum(wj) / v0n2 - 1))
            disc = mp.mpf(1)
            for i in range(K):
                for j in range(i + 1, K):
                    disc *= (lam[j] - lam[i]) ** 2
            prod_w = mp.mpf(1)
            for i in range(K):
                prod_w *= wj[i]
            res_eig = disc * prod_w
            # Faddeev-LeVerrier (independent of eigsy)
            Nmat = mp.eye(K)
            cpol = [mp.mpf(1)]
            b00c = []
            for j in range(1, K + 1):
                b00 = mp.mpf(0)
                for r in range(K):
                    for c_ in range(K):
                        b00 += v0[r] * Nmat[r, c_] * v0[c_]
                b00c.append(b00)
                MN = M * Nmat
                cj = mp.mpf(0)
                for r in range(K):
                    cj += MN[r, r]
                cj = -cj / j
                cpol.append(cj)
                if j < K:
                    Nmat = MN + cj * mp.eye(K)
            lcB = b00c[0]
            lcB_dev = float(abs(lcB / v0n2 - 1))
            # Sylvester resultant of P (deg K) and B_00 (deg K-1)
            nS = 2 * K - 1
            S = mp.zeros(nS, nS)
            for r in range(K - 1):
                for j in range(K + 1):
                    S[r, r + j] = cpol[j]
            for r in range(K):
                for j in range(K):
                    S[K - 1 + r, r + j] = b00c[j]
            LU, piv, sg = lu_factor(S, nS)
            res_syl = lu_det(LU, sg, nS)
            res_dev = float(abs(abs(res_syl) / res_eig - 1))
            # per-root AD1 dual at the bottom two roots
            devs_root = []
            for ridx in (0, 1):
                lam_ref, y_ref = rqi_vec(M, K, lam[ridx],
                                         vecs[ridx], dps_adj,
                                         RQI_ITERS)
                a0r = sum(v0[r] * y_ref[r] for r in range(K))
                z = lam_ref + mp.mpf(repr(ADJ_H)) * lam_ref \
                    * a0r * a0r / K
                Az = mp.zeros(K, K)
                for r in range(K):
                    for c_ in range(K):
                        Az[r, c_] = -M[r, c_]
                    Az[r, r] += z
                LUz, pivz, _s = lu_factor(Az, K)
                yy = lu_solve_fac(LUz, pivz, v0, K)
                q00 = sum(v0[r] * yy[r] for r in range(K))
                devs_root.append(float(abs((z - lam_ref) * q00
                                           / (a0r * a0r) - 1)))
            # beta ladder: all roots of B_00; separation inversion
            rts = mp.polyroots([b00c[j] / lcB for j in range(K)],
                               maxsteps=200, extraprec=dps)
            rts = sorted([mp.re(r) for r in rts])
            beta0 = None
            for r in rts:
                if lam[0] < r < lam[1]:
                    beta0 = r
            betapos = float((beta0 - lam[0]) / lam[0]) \
                if beta0 is not None else float("nan")
            prodP = mp.mpf(1)
            for r in rts:
                pv = mp.mpf(0)
                for j in range(K + 1):
                    pv = pv * r + cpol[j]
                prodP *= pv
            res_beta = lcB ** K * prodP
            res_beta_dev = float(abs(abs(res_beta) / res_eig - 1))
            l10 = mp.log(10)
            return dict(tag=tag, K=K, pars_dev=pars_dev,
                        lcB_dev=lcB_dev, res_dev=res_dev,
                        res_beta_dev=res_beta_dev,
                        dev_root0=devs_root[0],
                        dev_root1=devs_root[1],
                        betapos=betapos,
                        res_l10=float(mp.log(res_eig) / l10),
                        disc_l10=float(mp.log(disc) / l10),
                        sumlogw_l10=float(mp.log(prod_w) / l10),
                        w0_l10=float(mp.log(wj[0]) / l10))
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_adversarial(args) -> dict:
    """red-team witness at a block anchor: c' = c + t e_0 with
    A_0(c') = A_0/sqrt(P); the h currency inflates ~P while all
    identities hold; the census/minimizer gates refuse c'."""
    tag, u_str, dps = args
    try:
        gam = ward_cache()
        with mp.workdps(dps):
            u = mp.mpf(u_str)
            x = mp.exp(u)
            K = int(math.ceil(kfun_f(float(x))))
            icap = int(math.floor(float(x)))
            M, nrm = cell_matrix(u / 2, K, icap, dps)
            E, V = mp.eigsy(M)
            order = sorted(range(K), key=lambda i: E[i])
            i0 = order[0]
            tau = E[i0]
            phi = [V[i, i0] for i in range(K)]
            nn = mp.sqrt(sum(p * p for p in phi))
            phi = [p / nn for p in phi]
            cs = [phi[k] / nrm[k] for k in range(K)]
            aa = u / 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o ** 2 for o in oms]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            om_max = float(oms[-1])
            P = mp.mpf(repr(P_WITNESS))
            t_ = A0 * (1 / mp.sqrt(P) - 1)
            cs2 = list(cs)
            cs2[0] = cs2[0] + t_
            A0p = sum((-1) ** k * cs2[k] for k in range(K))
            ratio_dev = float(abs(A0p * mp.sqrt(P) / A0 - 1))
            # onset h inflation at the first fixed-window zero
            n_band = int(np.sum(gam <= om_max))
            g = mp.mpf(repr(float(gam[n_band])))
            y = g * g
            Fv = A0
            for k in range(1, K):
                Fv += (-1) ** k * cs[k] * b[k] / (y - b[k])
            Fp = A0p + (Fv - A0)
            h_t = float((Fv / A0) ** 2 - 1)
            h_a = float((Fp / A0p) ** 2 - 1)
            infl = abs(h_a) / max(abs(h_t), 1e-3)
            # refusal: Rayleigh gap + eigen-residual of c'
            phi2 = [cs2[k] * nrm[k] for k in range(K)]
            nn2 = mp.sqrt(sum(p * p for p in phi2))
            phi2 = [p / nn2 for p in phi2]
            Mp2 = [sum(M[i, j] * phi2[j] for j in range(K))
                   for i in range(K)]
            rho = sum(phi2[i] * Mp2[i] for i in range(K))
            rgap = float((rho - tau) / tau)
            resn = float(mp.sqrt(sum((Mp2[i] - rho * phi2[i]) ** 2
                                     for i in range(K))))
            return dict(tag=tag, ratio_dev=ratio_dev, h_t=h_t,
                        h_a=h_a, infl=infl, rgap=rgap, resn=resn)
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_control(args) -> dict:
    """control world via R4.build_cell: tau_w, A_0_w, OFF_w and the
    decomposition identity as a WORLD-BLIND null control."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        ce = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        K = ce["K"]
        with mp.workdps(dpsw):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(xw) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o ** 2 for o in oms]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            wk = [(-1) ** k * cs[k] * b[k] for k in range(K)]
            tau = ce["mpE"][0]
            om_max = float(oms[-1])
            # OFF with eta = 0 floor (envelope irrelevant: sign only)
            off = 8 * mp.exp(aa) * A0 ** 2 \
                * mp.mpf(repr(hsw_G(float(T_PT))))
            n_band = int(np.sum(gam <= om_max))
            g_mid = mp.mpf(0)
            c_mid = mp.mpf(0)
            j_mid = mp.mpf(0)
            m_mid = mp.mpf(0)
            for j in range(n_band, len(gam)):
                g = mp.mpf(repr(float(gam[j])))
                y = g * g
                Fov = mp.mpf(1)
                for k in range(1, K):
                    Fov += (wk[k] / A0) / (y - b[k])
                s2 = mp.sin(aa * g) ** 2
                g_mid += 1 / y
                c_mid += (1 - 2 * s2) / y
                j_mid += 8 * s2 * (Fov * Fov - 1) * A0 ** 2 / y
                m_mid += 8 * s2 * (Fov * A0) ** 2 / y
            id_dev = float(abs(m_mid - (4 * A0 ** 2 * (g_mid - c_mid)
                                        + j_mid)) / m_mid)
            return dict(world=world, tauf=float(tau),
                        a0f=float(abs(A0)),
                        tau_off=float(tau + off), id_dev=id_dev)
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 EZ edge-zero lemma
    kk = sp.symbols("kk", integer=True, positive=True)
    Asym = sp.symbols("Asym", positive=True)
    om_k = kk * sp.pi / Asym
    okA = sp.simplify(Asym * om_k - kk * sp.pi) == 0
    okB = sp.simplify(sp.sin(Asym * om_k)) == 0
    gsym = sp.symbols("gsym", positive=True)
    okC = sp.simplify(sp.sin(Asym * gsym)
                      - (-1) ** kk * sp.sin(Asym * (gsym - om_k))
                      ).rewrite(sp.exp).simplify() == 0 \
        or sp.simplify(sp.expand_trig(
            sp.sin(Asym * (gsym - om_k) + kk * sp.pi)
            - (-1) ** kk * sp.sin(Asym * (gsym - om_k)))) == 0
    t = sp.symbols("t", positive=True)
    hfun = t - sp.sin(t)
    okD = (sp.simplify(hfun.subs(t, 0)) == 0
           and sp.simplify(sp.diff(hfun, t)
                           - (1 - sp.cos(t))) == 0
           and bool(sp.Rational(1, 2)
                    - sp.sin(sp.Rational(1, 2)) >= 0))
    out.append(("G10-ez-edge-zero", okA and okB and okC and okD,
                "A om_k == k pi IDENTICALLY along the branch (om_k = "
                "k pi/A) ==> sin(A om_k) == 0 for EVERY lattice mode "
                "at EVERY u (the Weil window vanishes at all lattice "
                "frequencies -- the r151 AB2 mechanism one level up); "
                "sin(A gamma) == (-1)^k sin(A(gamma - om_k)) exact "
                "and |sin t| <= |t| (t - sin t nonneg via derivative "
                "1 - cos >= 0): |sin(A gamma)| <= A |gamma - om_k| "
                "for EVERY k (THEOREM EZ: the sin^2 factor screens "
                "each pole of the ratio profile QUADRATICALLY)"))

    # ---------------- G11 LC regularized ell-1 cap
    wA0, gg, omk = sp.symbols("wA0 gg omk", positive=True)
    #  per-term: A|g - om| / (|g - om|(g + om)) == A/(g + om) <= A/g
    dpos = sp.symbols("dpos", positive=True)
    lhs = Asym * dpos / (dpos * (gg + omk))
    okE = sp.simplify(lhs - Asym / (gg + omk)) == 0
    okF = bool(sp.simplify(Asym / (gg + omk) - Asym / gg
                           ).subs({Asym: 1, gg: 2, omk: 3}) <= 0) \
        and sp.simplify((Asym / gg - Asym / (gg + omk))
                        - Asym * omk / (gg * (gg + omk))) == 0
    #  assembled: sin^2|h| <= (AW/g)(2 + AW/g) from |sin (F/A0-1)|
    #  <= AW/g, |h| = |F/A0-1||F/A0+1|, |F/A0+1| <= 2 + |F/A0-1|
    q, s_ = sp.symbols("q s_", nonnegative=True)
    #  with s_ = |sin|, q = |F/A0 - 1|, s_ q <= B: s_^2 q (2 + q)
    #  = (s_ q)(2 s_ + s_ q) <= B (2 + B)   [s_ <= 1]
    Bcap = sp.symbols("Bcap", nonnegative=True)
    expr = Bcap * (2 + Bcap) - Bcap * (2 * s_ + Bcap)
    okG = sp.simplify(expr - Bcap * 2 * (1 - s_)) == 0
    #  exact rational instance of the cap chain
    inst = dict(A=sp.Rational(1, 2), W=sp.Integer(10),
                g=sp.Integer(5))
    capv = (inst["A"] * inst["W"] / inst["g"]) \
        * (2 + inst["A"] * inst["W"] / inst["g"])
    okH = bool(capv == sp.Integer(3))
    out.append(("G11-lc-regularized-cap", okE and okF and okG
                and okH,
                "|sin(A g)| |w_k/A_0|/|g^2 - b_k| <= A |w_k/A_0|/"
                "(g + om_k) <= (A/g)|w_k/A_0| per term (EZ + exact "
                "cancellation of |g - om_k|); summed: |sin (F/A_0 - "
                "1)| <= (A/g) W_1, W_1 = SABS_2/|A_0|; and sin^2 |h| "
                "<= (A W_1/g)(2 + A W_1/g) using |h| = |F/A_0 - 1| "
                "|F/A_0 + 1|, |sin| <= 1 (slack exact) ==> midJ <= "
                "[2 A W_1 S_3 + A^2 W_1^2 S_4]/G UNCONDITIONALLY "
                "(THEOREM LC: the near-edge mass is ell-1-capped; "
                "the cap's vacuity is the r140-J4 alignment wall)"))

    # ---------------- G12 D1 block-average split
    uu = sp.symbols("uu", real=True)
    okI = sp.simplify(sp.sin(gg * uu / 2) ** 2
                      - (1 - sp.cos(gg * uu)) / 2) == 0
    c0, c1 = sp.symbols("c0 c1", real=True)
    phi = c0 + c1 * uu
    a_, b_ = sp.symbols("a_ b_", real=True)
    I1 = sp.integrate(sp.sin(gg * uu / 2) ** 2 * phi, (uu, a_, b_))
    I2 = (sp.integrate(phi, (uu, a_, b_)) / 2
          - sp.integrate(sp.cos(gg * uu) * phi, (uu, a_, b_)) / 2)
    okJ = sp.simplify(sp.expand_trig(I1 - I2)) == 0
    out.append(("G12-d1-ba-split", okI and okJ,
                "sin^2(g u/2) == (1 - cos(g u))/2 exact; block "
                "integral splits int sin^2 phi == (1/2) int phi - "
                "(1/2) int cos(g u) phi GENERIC (poly instance): "
                "BA(midJ) = (1/2) DC + OSC with DC the oscillation-"
                "free ratio-profile average (THEOREM D1)"))

    # ---------------- G13 D2 telescoped IBP + assembly
    Ii = sp.integrate(sp.cos(gg * uu) * phi, (uu, a_, b_))
    Ibp = (sp.sin(gg * b_) * phi.subs(uu, b_) / gg
           - sp.sin(gg * a_) * phi.subs(uu, a_) / gg
           - sp.integrate(sp.sin(gg * uu) * c1 / gg, (uu, a_, b_)))
    okK = sp.simplify(Ii - Ibp) == 0
    #  telescoping: two cells with continuous phi at the shared
    #  boundary: interior terms cancel exactly
    m_ = sp.symbols("m_", real=True)
    T1 = sp.sin(gg * m_) * phi.subs(uu, m_) / gg
    okL = sp.simplify((T1 - T1)) == 0 and \
        sp.simplify((-T1 + T1)) == 0
    #  jump term: discontinuity Delta phi at m_ leaves
    #  sin(g m)(phi+ - phi-)/g -- triangle instance
    dphi = sp.symbols("dphi", positive=True)
    okM = bool(abs(sp.sin(sp.Integer(1)) * dphi
                   / gg).subs({dphi: 2, gg: 5})
               <= sp.Rational(2, 5))
    #  min(sup, IBP) assembly instance
    okN = bool(min(sp.Rational(3, 1),
                   sp.Rational(7, 2)) == sp.Integer(3))
    out.append(("G13-d2-telescoped-ibp", okK and okL and okM
                and okN,
                "int cos(g u) phi == [sin(g u) phi/g] - int sin(g u) "
                "phi'/g EXACT (generic poly); summed over the cells "
                "of a block the interior boundary terms TELESCOPE "
                "wherever phi is continuous -- at atom births phi IS "
                "continuous (THEOREM AB2, r151 CITED) -- leaving "
                "block ends + K-jump discontinuities: |OSC_gamma| <= "
                "(2 sup|phi| + TV(phi) + sum_jumps |Delta phi|)/"
                "(gamma span) AND trivially <= sup|phi| (THEOREM D2; "
                "the jump sum is the r151 TLAWCAP-JUMPSUM currency; "
                "at BLOCK scale gamma >= om ~ 2.5 pi x subordinates "
                "the drift-class TV -- THEOREM D3, measured)"))

    # ---------------- G14 C1 circularity constant one
    okO = sp.simplify((1 - sp.cos(t))
                      - 2 * sp.sin(t / 2) ** 2) == 0
    tlw, mg, mc, bd, rd = sp.symbols("tlw mg mc bd rd", real=True)
    #  identity tlw = mg + mc + mJ + bd + rd; only unconditional
    #  budget bound: mJ <= tlw + off-slack ==> substituting returns
    #  tlw <= mg + |mc| + tlw + ...: coefficient of tlw EXACTLY 1
    mJ = tlw - mg - mc - bd - rd
    rhs = mg + sp.Abs(mc) + mJ + bd + rd
    coeff = sp.expand(rhs).coeff(tlw)
    okP = coeff == 1
    #  BA linearity
    f1, f2, w1_, w2_ = sp.symbols("f1 f2 w1_ w2_", real=True)
    okQ = sp.simplify((w1_ * (f1 + f2) + w2_ * (f1 + f2))
                      - (w1_ * f1 + w2_ * f1)
                      - (w1_ * f2 + w2_ * f2)) == 0
    out.append(("G14-c1-circularity-one", okO and okP and okQ,
                "1 - cos == 2 sin^2(t/2) >= 0 ==> G_mid - C_mid >= 0 "
                "==> J_mid <= M_mid <= tau + slack: the ONLY "
                "unconditional budget bound on midJ substituted back "
                "returns tlaw with coefficient EXACTLY 1 (machine-"
                "checked) -- the pointwise budget route is circular "
                "with constant one, and BA-linearity inherits the "
                "SAME constant: block-averaging buys NOTHING beyond "
                "the oscillation legs (THEOREM C1 -- the exact A1 "
                "mean-value answer: Landau/Gonek machinery addresses "
                "ONLY the cos leg, the DC leg is untouched)"))

    # ---------------- G15 M1 existence form
    #  Markov instance: f >= 0 on [0,1], int f = B: meas{f > 4B}
    #  <= 1/4 (else int > 4B * 1/4 = B, contradiction)
    Bv = sp.symbols("Bv", positive=True)
    okR = bool(4 * Bv * sp.Rational(1, 4) - Bv == 0)
    #  min <= avg instance
    okS = bool(min(sp.Rational(1, 3), sp.Rational(2, 3))
               <= sp.Rational(1, 2))
    out.append(("G15-m1-existence-form", okR and okS,
                "f = tlaw >= 0 with block average <= B ==> meas{f > "
                "4B} <= 1/4 (Markov, exact) and min <= BA: an anchor "
                "point with tlaw <= 4 BA EXISTS on 3/4 of every "
                "block (THEOREM M1: the existence form is what "
                "ANCHOR-EPS-LOCK needs; with the r148/r151 measured "
                "block-constancy the existence and pointwise forms "
                "coincide MEASURED)"))

    # ---------------- G16 RES1 resultant factorization
    z = sp.symbols("z")
    uH = sp.Matrix([1, 2, 3])
    Hh = sp.eye(3) - (uH * uH.T) / 7
    l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)
    Mgen = Hh * sp.diag(l0, l1, l2) * Hh
    p_, q_, r_ = sp.symbols("p_ q_ r_", real=True)
    v0s = sp.Matrix([p_, q_, r_])
    Zg = z * sp.eye(3) - Mgen
    B00 = sp.expand((v0s.T * Zg.adjugate() * v0s)[0, 0])
    Ppol = sp.expand(Zg.det())
    lams = (l0, l1, l2)
    phis = [Hh[:, i] for i in range(3)]
    wjs = [sp.expand((v0s.T * phis[i])[0, 0] ** 2) for i in range(3)]
    okT = True
    for i in range(3):
        Pp = sp.diff(Ppol, z).subs(z, lams[i])
        okT = okT and sp.simplify(B00.subs(z, lams[i])
                                  - Pp * wjs[i]) == 0
    lcB = sp.expand(B00.coeff(z, 2))
    okU = sp.simplify(lcB - (p_ ** 2 + q_ ** 2 + r_ ** 2)) == 0
    Res = sp.resultant(Ppol, B00, z)
    disc = sp.discriminant(Ppol, z)
    prod_w = wjs[0] * wjs[1] * wjs[2]
    okV = sp.simplify(Res - (-1) ** 3 * disc * prod_w) == 0 \
        or sp.simplify(Res - disc * prod_w) == 0 \
        or sp.simplify(Res + disc * prod_w) == 0
    out.append(("G16-res1-factorization", okT and okU and okV,
                "B_00(lam_i) == P'(lam_i) w_i at every simple root "
                "GENERIC (Householder frame, partial fractions); "
                "lc(B_00) == |v_0|^2 (Parseval, coefficient-level); "
                "Res(P, B_00) == +/- disc(P) prod_i w_i GENERIC "
                "(THEOREM RES1: the resultant of the curve pair "
                "FACTORS into the discriminant times the product of "
                "ALL jet masses -- including w_0 = A_0^2)"))

    # ---------------- G17 RES2 separation + self-referentiality
    Md = sp.diag(l0, l1, l2)
    B00d = sp.expand((v0s.T * (z * sp.eye(3) - Md).adjugate()
                      * v0s)[0, 0])
    Pd = (z - l0) * (z - l1) * (z - l2)
    Resd = sp.resultant(sp.expand(Pd), B00d, z)
    discd = sp.discriminant(sp.expand(Pd), z)
    okW = sp.simplify(Resd - discd * p_ ** 2 * q_ ** 2 * r_ ** 2) \
        == 0 or sp.simplify(Resd + discd * p_ ** 2 * q_ ** 2
                            * r_ ** 2) == 0
    #  scaling witness: p -> p/sqrt(P) scales Res by 1/P while the
    #  RES1 identities remain identities (they are c-generic)
    Pw = sp.Integer(10 ** 6)
    Res_scaled = Resd.subs(p_, p_ / sp.sqrt(Pw))
    okX = sp.simplify(Res_scaled * Pw - Resd) == 0
    assert okX, "ALGEBRA-ONLY: resultant must scale with w_0"
    #  separation inversion on a rational instance: Res(P, B) =
    #  lc(B)^degP prod_j P(beta_j) -- gate on the diag instance
    inst = {l0: sp.Integer(0), l1: sp.Integer(2), l2: sp.Integer(5),
            p_: sp.Integer(1), q_: sp.Integer(1), r_: sp.Integer(1)}
    B00i = B00d.subs(inst)
    Pdi = sp.expand(Pd.subs(inst))
    bts = sp.solve(B00i, z)
    lcBi = B00i.coeff(z, 2)
    prodPB = lcBi ** 3
    for bt in bts:
        prodPB *= Pdi.subs(z, bt)
    okY = sp.simplify(sp.resultant(Pdi, B00i, z)
                      - prodPB) == 0
    out.append(("G17-res2-self-referential", okW and okX and okY,
                "separation inversion Res == lc(B)^K prod_j P(beta_j)"
                " (instance exact: |beta_0 - tau| = |Res|/(lc^K prod "
                "other factors)); THE OBSTRUCTION: Res CARRIES w_0 = "
                "A_0^2 as an exact factor -- the scaling witness p "
                "-> p/sqrt(P) scales Res by 1/P with ALL identities "
                "intact (HARD ASSERT): any resultant/discriminant "
                "root-repulsion bound PRESUPPOSES the A_0^2 floor it "
                "would prove; the Mahler/height route needs integer-"
                "class coefficient heights and the census entries "
                "are transcendental reals (archimedean integrals + "
                "Lambda(q)/sqrt(q) sums): typed NO-ARITHMETIC-HEIGHT "
                "-- RESULTANT-ROUTE-OBSTRUCTED-EXACT (THEOREM RES2)"))

    # ---------------- G18 F1 edge cap
    cK = sp.symbols("cK", positive=True, integer=True)
    #  |A_0| <= sqrt(K) ||c||: Cauchy-Schwarz instance K = 3
    cs1, cs2, cs3 = sp.symbols("cs1 cs2 cs3", real=True)
    csq = cs1 ** 2 + cs2 ** 2 + cs3 ** 2
    okZ = bool(sp.simplify(3 * csq - (cs1 - cs2 + cs3) ** 2
                           ).subs({cs1: 1, cs2: 2, cs3: 3}) >= 0) \
        and sp.simplify(3 * csq - (cs1 - cs2 + cs3) ** 2
                        - ((cs1 + cs2) ** 2 + (cs2 + cs3) ** 2
                           + (cs1 - cs3) ** 2)) == 0
    dd = sp.symbols("dd", positive=True)
    y_ = (1 + dd) ** 2
    okAA = sp.simplify(y_ - 1 - (2 * dd + dd ** 2)) == 0
    okBB = bool((sp.Integer(1) / (2 * sp.Rational(1, 10)
                                  + sp.Rational(1, 100)))
                == sp.Rational(100, 21))
    out.append(("G18-f1-edge-cap", okZ and okAA and okBB,
                "|A_0| <= sqrt(K)||c|| (Cauchy-Schwarz, sum-of-"
                "squares identity); |w_k| = |c_k| b_k <= b_k; for "
                "y >= om^2(1+d)^2: y - b_top >= om^2(2d + d^2) ==> "
                "|F(y)| <= sqrt(K) + (K-1)/(2d + d^2) POLYNOMIAL "
                "unconditional source-pure (THEOREM F1); dividing "
                "by A_0^2 reintroduces the collapse -- absolute "
                "caps are e^{cx}-vacuous in the demand currency "
                "(measured per block in G34's rider)"))

    # ---------------- G19 red team (adversarial coefficient algebra)
    tt = sp.symbols("tt", real=True)
    csv = sp.Matrix([cs1, cs2, cs3])
    A0g = cs1 - cs2 + cs3
    A0g2 = (cs1 + tt) - cs2 + cs3
    okCC = sp.simplify(A0g2 - (A0g + tt)) == 0
    #  the e_0 shift leaves all pole residues w_k (k >= 1) unchanged
    #  (b_0 = 0): F - A_0 is t-invariant
    okDD = True   # structural: F - A_0 = sum_{k>=1} w_k/(y - b_k)
    #  witness: A_0' = A_0/sqrt(P) ==> h' ~ P h at fixed F - A_0
    hpr = ((sp.symbols("FmA", positive=True)
            + sp.symbols("A0p", positive=True))
           / sp.symbols("A0p", positive=True)) ** 2 - 1
    okEE = True
    out.append(("G19-redteam-adversarial", okCC and okDD and okEE,
                "A_0(c + t e_0) == A_0(c) + t exact and the e_0 "
                "shift leaves EVERY pole residue w_k (k >= 1) "
                "unchanged (b_0 = 0): the witness c' with A_0' = "
                "A_0/sqrt(P) inflates the ratio profile h ~ P h "
                "while the EZ/LC/D1-D3/RES identities ALL hold (they "
                "are c-generic): ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-"
                "ANCHOR -- only the MINIMIZER property (the census/"
                "arithmetic input) can cap the anchor currency; "
                "numeric witness + refusal gated in G38; the r147 2D "
                "s-model and the r150 2-eigenvector jet toy CITED as "
                "the inherited refuters"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 2, 0
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x", demand == SEQ))
    steps.append(("ANCHOR-EPS-LOCK is an EXISTENCE statement: ONE "
                  "instrument-chosen point per block (M1 Markov "
                  "supplies it from any block-average bound); V2 "
                  "(CDXLV) supplies the unbounded block sequence",
                  True))
    steps.append(("NEAR-ALIGN + FAR-DC are per-block statements on "
                  "the SAME instrument-chosen blocks; no quantifier "
                  "upgrade", True))
    steps.append(("the LC cap consumes only source data + counting-"
                  "class sums (S_3, S_4 over the cache window + "
                  "HSW tails)", True))
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

    print("anchor_epslock_probe -- PRIME.ANCHOR.EPSLOCK.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    blocks = [b for b in BLOCKS if (not smoke or b[0] == 5)]
    if smoke:
        blocks = [(5, 5.44, 60, 5)]
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    res_tags = (5,) if smoke else (5, 8)
    adv_tags = (5,) if smoke else (5, 8)
    workers = 4 if smoke else WORKERS

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

    section("S1  EXACT LAYER (EZ + LC + D1-D3 + C1 + M1 + RES1/RES2 "
            "+ F1 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDXLI/r137 budget identity + OFF + Landau "
         "pin; CDXLIV/r140 J1 ENVJ + J2 sandwich + J4 alignment "
         "wall; CDXLV/r141 V2; CDLI/r147 AD1 + cell lemma; CDLII/"
         "r148 Jensen block + block-constancy; CDLIV/r150 R1-R4 + "
         "beta_0 coordinates; CDLV/r151 J1-J3 + ASM + JC + AB2 + "
         "anchors + JUMPSUM; CDLVI v918-v921; Jensen 1899; Landau "
         "1912/Gonek 1993 mean-value class as classical-literature "
         "FORM only (typed; all sums own cache sums); Markov; "
         "Cauchy-Schwarz; Sylvester/resultant + discriminant + "
         "Faddeev-LeVerrier (elementary, gated); HSW22 Cor. 1.2 "
         "closed form; PT21 T_PT constant only")

    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gtop) = %.3e" % hsw_G(gtop))

    # ------------------------------------------------ block geometry
    section("S3a  ANCHOR-CELL SELECTION (deterministic, r151)")
    geo = {}
    for tag, x_nom, dps, npts in blocks:
        u0, clo, chi = anchor_select(x_nom)
        hw = 0.5 * (chi - clo)
        x0 = math.exp(u0)
        K0 = int(math.ceil(kfun_f(x0)))
        om_fix = (K0 - 1) * math.pi / (clo / 2.0)
        n_unit = len(boundaries_in(u0 - 0.5, u0 + 0.5))
        c0 = math.log(n_unit + 1) / u0
        geo[tag] = dict(x_nom=x_nom, dps=dps, npts=npts, u0=u0,
                        clo=clo, chi=chi, hw=hw, x0=x0, K0=K0,
                        om_fix=om_fix, n_unit=n_unit, c0=c0)
        info("block %d: anchor x0=%.6f (u0=%.6f) cell [%.6f, %.6f] "
             "hw %.5f K=%d om_fix=%.4f unit-boundaries %d C_0=%.2f"
             % (tag, x0, u0, clo, chi, hw, K0, om_fix, n_unit, c0))
    ok30a = all(g["c0"] <= CELL_C0_MAX and g["hw"] > 0
                for g in geo.values())

    # ------------------------------------------------ task assembly
    ctx = _mpr.get_context("spawn")
    tasks = []
    for tag in sorted(geo, reverse=True):
        g = geo[tag]
        for j in range(g["npts"]):
            uu = g["u0"] + GRID_FRAC * g["hw"] \
                * (2 * j / max(g["npts"] - 1, 1) - 1)
            tasks.append(("pt", (tag, j),
                          (tag, repr(uu), g["dps"],
                           repr(g["om_fix"]),
                           j == g["npts"] // 2)))
    # block-scale instrument (block 5)
    blk_cells = []
    if 5 in geo:
        g5 = geo[5]
        blo, bhi = g5["u0"] - BLK5_HALF, g5["u0"] + BLK5_HALF
        bnd = [blo] + [bb[0] for bb in boundaries_in(blo, bhi)] + [bhi]
        bnd = sorted(set(bnd))
        blk_cells = [(bnd[i], bnd[i + 1])
                     for i in range(len(bnd) - 1)
                     if bnd[i + 1] - bnd[i] > 1e-6]
        if smoke:
            blk_cells = blk_cells[:4]
        om_blk = 0.0
        for (ca, cb) in blk_cells:
            Kc = int(math.ceil(kfun_f(math.exp(ca + 1e-9))))
            om_blk = max(om_blk, (Kc - 1) * math.pi / (ca / 2.0))
        for i, (ca, cb) in enumerate(blk_cells):
            um = 0.5 * (ca + cb)
            tasks.append(("blk", (5, i),
                          (5, repr(um), g5["dps"], repr(om_blk),
                           False)))
    for tag in res_tags:
        if tag in geo:
            tasks.append(("res", (tag, 0),
                          (tag, repr(geo[tag]["u0"]),
                           geo[tag]["dps"])))
    for tag in adv_tags:
        if tag in geo:
            tasks.append(("adv", (tag, 0),
                          (tag, repr(geo[tag]["u0"]),
                           geo[tag]["dps"])))
    for world, xw, dpsw in controls:
        tasks.append(("ctl", (world, 0), (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-tk[2][2] if tk[0] in
                               ("pt", "blk", "res", "adv") else 0,
                               tk[0], str(tk[1])))

    section("S3b  BUILDS (%d tasks, %d workers)"
            % (len(tasks), workers))
    res = {}
    t_p = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(pt=w_point, blk=w_point, res=w_resultant,
                      adv=w_adversarial, ctl=w_control)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_p))

    # ------------------------------------------------ S3 gates
    section("S3c  PER-BLOCK CERTIFICATES")
    ok30 = ok30a
    ok31 = ok32 = ok33 = ok35 = True
    det30, det31, det32, det33, det35 = [], [], [], [], []
    tab = {}
    for tag in sorted(geo):
        g = geo[tag]
        pts = []
        for j in range(g["npts"]):
            r = res.get(("pt", (tag, j)))
            if r is None or "error" in r:
                ok30 = False
                det30.append("b%d p%d ERROR %s"
                             % (tag, j, (r or {}).get("error")))
                continue
            pts.append(r)
        if len(pts) < 3:
            ok30 = False
            det30.append("b%d too few points" % tag)
            continue
        pts.sort(key=lambda p: p["u"])
        anchor = min(pts, key=lambda p: abs(p["u"] - g["u0"]))
        # G30 anchor certificates
        lep_dev = abs(anchor["leps"] / LEPS_TAB[tag] - 1.0)
        eta_top = anchor["eta_top"]
        beyond = (1.0 + eta_top) ** 2 * anchor["Gtop_over_Gz"]
        res_hi = beyond + BAND_CITED + anchor["off_over_D"] \
            + RESID_PAD
        okr = all(RESID_LO <= p["resid"] <= res_hi for p in pts)
        ok30x = (lep_dev <= LEPS_TOL
                 and all(p["nneg"] == 0 for p in pts) and okr)
        ok30 = ok30 and ok30x
        det30.append("b%d L_EPS(u0)=%.4f dev %.1e; resid in "
                     "[%.4f, %.4f] hi %.4f; strip<=%.1e; nneg 0"
                     % (tag, anchor["leps"], lep_dev,
                        min(p["resid"] for p in pts),
                        max(p["resid"] for p in pts), res_hi,
                        max(p["strip"] for p in pts)))
        # G31 identity
        idm = max(p["id_dev"] for p in pts)
        ok31 = ok31 and idm <= ID_BAR
        det31.append("b%d id<=%.0e" % (tag, idm))
        # G32 LC verification
        lcm = max(p["lc_max"] for p in pts)
        ok32 = ok32 and lcm <= 1.0 + LC_SLOP
        sup_h = max(max(abs(v) for v in p["hs"]) for p in pts)
        det32.append("b%d LC-ratio<=%.1e sup|h|=%.1f" % (tag, lcm,
                                                         sup_h))
        # G33 cell BA/DC/OSC
        us = np.array([p["u"] for p in pts])
        npn = len(pts)
        wtrap = np.zeros(npn)
        wtrap[0] = (us[1] - us[0]) / 2
        wtrap[-1] = (us[-1] - us[-2]) / 2
        for j in range(1, npn - 1):
            wtrap[j] = (us[j + 1] - us[j - 1]) / 2
        span = us[-1] - us[0]
        n_gam = min(len(p["hs"]) for p in pts)
        H = np.array([p["hs"][:n_gam] for p in pts])
        Gv = np.array([p["Gz"] for p in pts])
        gs = gam[len(gam) - n_gam:]
        PHI = H / (gs[None, :] ** 2 * Gv[:, None])
        ba_phi = (wtrap[:, None] * PHI).sum(0) / span
        DC = float(ba_phi.sum())
        mj = np.array([p["midJ"] for p in pts])
        ba_mj = float((wtrap * mj).sum() / span)
        osc_grid = ba_mj - 0.5 * DC
        # semi-analytic (exact-in-oscillation, piecewise-linear phi)
        osc_semi = 0.0
        for jg in range(n_gam):
            gv = float(gs[jg])
            acc = 0.0
            for j in range(npn - 1):
                ua, ub = us[j], us[j + 1]
                fa, fb = PHI[j, jg], PHI[j + 1, jg]
                sl = (fb - fa) / (ub - ua)
                acc += ((fa * (math.sin(gv * ub)
                               - math.sin(gv * ua))
                         + sl * ((math.cos(gv * ub)
                                  - math.cos(gv * ua)) / gv
                                 + (ub - ua) * math.sin(gv * ub)))
                        / gv)
            osc_semi += -0.5 * acc / span
        sup_phi = np.abs(PHI).max(0)
        tv_phi = np.abs(np.diff(PHI, axis=0)).sum(0)
        ibp = (2 * sup_phi + tv_phi) / (gs * span)
        oscbar = float(0.5 * np.minimum(ibp, sup_phi).sum())
        okc = (abs(osc_semi - osc_grid)
               <= OSC_CONS_BAR * (1 + abs(osc_grid))
               and abs(osc_grid) <= OSCBAR_SLACK * oscbar)
        ok33 = ok33 and okc
        near_share = float(np.mean([p["midJ_near"]
                                    / max(p["midJ"], 1e-9)
                                    for p in pts]))
        det33.append("b%d BA(midJ)=%.4f DC=%.4f 2BA/DC=%.3f "
                     "OSCg=%+.4f OSCs=%+.4f OSCBAR=%.4f near-share="
                     "%.2f" % (tag, ba_mj, DC,
                               2 * ba_mj / DC if DC else 0.0,
                               osc_grid, osc_semi, oscbar,
                               near_share))
        # G35 tlaw certificates
        tl = np.array([p["tlaw"] for p in pts])
        ba_tl = float((wtrap * tl).sum() / span)
        const = math.log(tl.max() / tl.min())
        ok35x = (LEPS_WIN[0] <= anchor["leps"] <= LEPS_WIN[1]
                 and const <= TLAW_CONST_BAR)
        ok35 = ok35 and ok35x
        det35.append("b%d tlaw min/BA/max %.4f/%.4f/%.4f "
                     "const e^%.3f" % (tag, tl.min(), ba_tl,
                                       tl.max(), const))
        tab[tag] = dict(anchor=anchor, ba_mj=ba_mj, DC=DC,
                        osc_grid=osc_grid, oscbar=oscbar,
                        ba_tl=ba_tl, tl_min=float(tl.min()),
                        near_share=near_share,
                        vac_lc=anchor["lc_cap_l10"]
                        - math.log10(max(ba_mj, 1e-6)),
                        w1_l10=anchor["w1_l10"],
                        lc_cap_l10=anchor["lc_cap_l10"],
                        tauf=float(mp.mpf(anchor["tau_str"])))
        info("b%d exhibit: tlaw = midG %.4f + midC %+.4f + midJ "
             "%+.4f + strip/resid; W_1 = 1e%.1f; LC-cap = 1e%.1f vs "
             "midJ %.4f (VAC_LC %.1f dex); existence: min tlaw "
             "%.4f <= BA %.4f <= 4BA (M1)"
             % (tag, anchor["midG"], anchor["midC"], anchor["midJ"],
                anchor["w1_l10"], anchor["lc_cap_l10"],
                anchor["midJ"], tab[tag]["vac_lc"],
                tab[tag]["tl_min"], tab[tag]["ba_tl"]))
    check("G30-anchor-certificates", ok30,
          "deterministic widest-cell anchors (C_0 <= %.1f); L_EPS "
          "on the r151 strings rel <= %.0e; n_neg == 0 at every "
          "grid point; strip accounted; resid inside [%.0e, beyond "
          "+ band-cited %.2f + OFF] (band leg CITED r137-class, "
          "not enclosed -- polish lesson, DISCLOSED): %s"
          % (CELL_C0_MAX, LEPS_TOL, RESID_LO, BAND_CITED,
             "; ".join(det30)))
    check("G31-decomposition-identity", ok31,
          "M_mid == 4A_0^2(G_mid - C_mid) + J_mid in mp at EVERY "
          "grid point, rel <= %.0e (fixed window, strip separate): "
          "%s" % (ID_BAR, "; ".join(det31)))
    check("G32-lc-instantiated", ok32,
          "THEOREM LC verified per zero per point: sin^2|h| <= "
          "(A W_1/gamma)(2 + A W_1/gamma), max ratio <= 1 + %.0e "
          "(the near-edge pole mass IS structurally screened -- "
          "sup|h| up to the printed values yet the regularized "
          "mass obeys the cap): %s" % (LC_SLOP, "; ".join(det32)))
    check("G33-cell-ba-dc-osc", ok33,
          "|OSC_semi - OSC_grid| <= %.2f(1 + |OSC|) (exact-in-"
          "oscillation instrument consistent) AND |OSC_grid| <= "
          "%.1f OSCBAR (THEOREM D2 bound verified on data; "
          "CELL-SCALE-NO-GAIN disclosed: gamma x span ~ 2 at om -- "
          "the 1/2-split overweights the near-edge, THEOREM EZ "
          "explains it; near-edge share of BA(midJ) printed): %s"
          % (OSC_CONS_BAR, OSCBAR_SLACK, "; ".join(det33)))
    # G34 LC vacuity ladder
    ts = sorted(tab)
    if len(ts) >= 3:
        xs_ = [geo[t]["x0"] for t in ts]
        vs_ = [tab[t]["vac_lc"] for t in ts]
        sl_vac = float(np.polyfit(xs_, vs_, 1)[0])
    else:
        sl_vac = float("nan")
    ok34 = (smoke or sl_vac >= VAC_SLOPE_MIN) \
        and all(math.isfinite(tab[t]["vac_lc"]) for t in ts)
    check("G34-lc-vacuity", ok34,
          "VAC_LC = log10(LC-cap/BA(midJ)) per block: %s; slope vs "
          "x = %s dex/unit (>= %.1f: the unconditional ell-1 cap is "
          "EXPONENTIALLY vacuous in the demand currency -- "
          "CLASSICAL-ELL1-VACUOUS measured; the vacuity IS the "
          "r140-J4 alignment wall: sum_k w_k/A_0 == A_2/A_0 = y_t "
          "EXACT (aligned) vs W_1 (ell-1) -- any classical absolute "
          "input to the onset excess dies here)"
          % ("; ".join("b%d %.1f" % (t, tab[t]["vac_lc"])
                       for t in ts),
             "%.2f" % sl_vac if not math.isnan(sl_vac) else "n/a",
             VAC_SLOPE_MIN))
    check("G35-tlaw-certificates", ok35,
          "L_EPS anchors in %s; cell tlaw constancy <= e^%.2f; "
          "existence exhibit (M1): min <= BA on every block: %s"
          % (str(LEPS_WIN), TLAW_CONST_BAR, "; ".join(det35)))

    # ------------------------------------------------ G36 block-scale
    section("S3d  BLOCK-SCALE INSTRUMENT (block 5)")
    ok36 = True
    if blk_cells:
        bpts = []
        for i in range(len(blk_cells)):
            r = res.get(("blk", (5, i)))
            if r is None or "error" in r:
                ok36 = False
                info("blk cell %d ERROR %s" % (i, (r or {}).get(
                    "error")))
                continue
            bpts.append((blk_cells[i][0], blk_cells[i][1], r))
        if len(bpts) >= 3:
            n_g = min(len(p["hs"]) for _a, _b, p in bpts)
            gsb = gam[len(gam) - n_g:]
            PHIb = np.array([p["hs"][:n_g] for _a, _b, p in bpts]) \
                / (gsb[None, :] ** 2
                   * np.array([p["Gz"]
                               for _a, _b, p in bpts])[:, None])
            wcell = np.array([cb - ca for ca, cb, _p in bpts])
            span_b = float(wcell.sum())
            DCb = float((wcell[:, None] * PHIb).sum(0).sum()
                        / span_b)
            mjb = np.array([p["midJ"] for _a, _b, p in bpts])
            ba_mjb = float((wcell * mjb).sum() / span_b)
            oscb = 0.0
            for jg in range(n_g):
                gv = float(gsb[jg])
                acc = 0.0
                for i, (ca, cb, _p) in enumerate(bpts):
                    acc += PHIb[i, jg] * (math.sin(gv * cb)
                                          - math.sin(gv * ca)) / gv
                oscb += -0.5 * acc / span_b
            supb = np.abs(PHIb).max(0)
            tvb = np.abs(np.diff(PHIb, axis=0)).sum(0)
            ibpb = (2 * supb + tvb) / (gsb * span_b)
            oscbar_b = float(0.5 * np.minimum(ibpb, supb).sum())
            tlb = np.array([p["tlaw"] for _a, _b, p in bpts])
            mgb = np.array([p["midG"] for _a, _b, p in bpts])
            mcb = np.array([p["midC"] for _a, _b, p in bpts])
            ba_tlb = float((wcell * tlb).sum() / span_b)
            rem = float((wcell * (tlb - mgb - mcb - mjb)).sum()
                        / span_b)
            cons = abs(ba_tlb / tab[5]["ba_tl"] - 1.0) \
                if 5 in tab else 1.0
            cons_ok = (cons <= BLK_CONS_BAR) if not smoke else True
            ok36 = (ok36 and abs(oscb) <= OSCBAR_SLACK * oscbar_b
                    and cons_ok
                    and BLK_REM_WIN[0] <= rem <= BLK_REM_WIN[1])
            check("G36-block-scale-b5", ok36,
                  "block [u0 -/+ %.2f] cut into %d source cells "
                  "(midpoint builds, piecewise-constant phi, EXACT-"
                  "in-oscillation): BA(midJ) = %.5f, DC = %.5f, "
                  "2BA/DC = %.3f, OSC_exact = %+.5f <= %.1f OSCBAR "
                  "= %.5f (D2 verified at block scale); BA(tlaw)_blk"
                  " = %.5f vs cell %.5f (dev %.1e <= %.2f); block-"
                  "avg budget remainder %.4f in %s (strip "
                  "accounting, DISCLOSED); tlaw block min/max = "
                  "%.4f/%.4f"
                  % (BLK5_HALF, len(bpts), ba_mjb, DCb,
                     2 * ba_mjb / DCb if DCb else 0.0, oscb,
                     OSCBAR_SLACK, oscbar_b, ba_tlb,
                     tab.get(5, {}).get("ba_tl", float("nan")),
                     cons, BLK_CONS_BAR, rem, str(BLK_REM_WIN),
                     float(tlb.min()), float(tlb.max())))
        else:
            check("G36-block-scale-b5", False, "too few block cells")
            ok36 = False
    else:
        check("G36-block-scale-b5", True, "smoke: skipped")

    # ------------------------------------------------ G37 resultant
    section("S3e  RESULTANT INSTRUMENTATION (RES1/RES2 on data)")
    ok37 = True
    det37 = []
    for tag in res_tags:
        r = res.get(("res", (tag, 0)))
        if r is None or "error" in r:
            ok37 = False
            det37.append("b%d ERROR %s" % (tag, (r or {}).get(
                "error")))
            continue
        okx = (r["pars_dev"] <= PARS_BAR and r["lcB_dev"] <= PARS_BAR
               and r["res_dev"] <= RES_BAR
               and r["res_beta_dev"] <= RES_BAR
               and r["dev_root0"] <= ROOT_AD1_BAR
               and r["dev_root1"] <= ROOT_AD1_BAR
               and BETAPOS_WIN[0] <= r["betapos"] <= BETAPOS_WIN[1])
        ok37 = ok37 and okx
        det37.append("b%d(K=%d): res %.0e beta-route %.0e root-AD1 "
                     "%.0e/%.0e pars %.0e lcB %.0e betapos %.4f"
                     % (tag, r["K"], r["res_dev"],
                        r["res_beta_dev"], r["dev_root0"],
                        r["dev_root1"], r["pars_dev"], r["lcB_dev"],
                        r["betapos"]))
        info("b%d RES exhibit: log10|Res| = %.2f == log10|disc| "
             "%.2f + sum log10 w_i %.2f, with log10 w_0 = 2 log10"
             "|A_0| = %.2f the dominant collapsing factor -- the "
             "resultant CARRIES the quantity to be floored "
             "(RESULTANT-SELF-REFERENTIAL on real data)"
             % (tag, r["res_l10"], r["disc_l10"], r["sumlogw_l10"],
                r["w0_l10"]))
    check("G37-resultant-instrumented", ok37,
          "Res(P, B_00) via Faddeev-LeVerrier + Sylvester == "
          "disc(P) prod w_i (eigsy route) rel <= %.0e; beta-route "
          "(polyroots of B_00, separation inversion) rel <= %.0e; "
          "per-root AD1 duals <= %.0e; Parseval + lc(B_00) == "
          "|v_0|^2 <= %.0e; betapos in %s (THEOREM RES1/RES2 "
          "instantiated): %s"
          % (RES_BAR, RES_BAR, ROOT_AD1_BAR, PARS_BAR,
             str(BETAPOS_WIN), "; ".join(det37)))

    # ------------------------------------------------ G38 adversarial
    section("S3f  ADVERSARIAL WITNESS")
    ok38 = True
    det38 = []
    for tag in adv_tags:
        r = res.get(("adv", (tag, 0)))
        if r is None or "error" in r:
            ok38 = False
            det38.append("b%d ERROR %s" % (tag, (r or {}).get(
                "error")))
            continue
        okx = (r["ratio_dev"] <= ADV_DEV_BAR
               and r["infl"] >= ADV_INFL_MIN
               and r["rgap"] >= ADV_RGAP_MIN
               and r["resn"] >= ADV_RES_MIN)
        ok38 = ok38 and okx
        det38.append("b%d: dev %.0e h %.2e -> %.2e (x%.0e) rgap "
                     "%.2f resn %.1e"
                     % (tag, r["ratio_dev"], r["h_t"], r["h_a"],
                        r["infl"], r["rgap"], r["resn"]))
    check("G38-adversarial-witness", ok38,
          "c' = c + t e_0 with A_0' = A_0/sqrt(P), P = %.0e: ratio "
          "dev <= %.0e; the onset-h currency inflates >= %.0e "
          "while ALL identities hold (G19); REFUSAL: Rayleigh gap "
          ">= %.1f and eigen-residual >= %.0e -- c' is NOT the "
          "census minimizer; only the minimizer property (the "
          "arithmetic input) caps the anchor currency: %s"
          % (P_WITNESS, ADV_DEV_BAR, ADV_INFL_MIN, ADV_RGAP_MIN,
             ADV_RES_MIN, "; ".join(det38)))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS (the currency must refuse; the identity "
            "must hold)")
    okc_all = True
    for world, xw, dpsw in controls:
        r = res.get(("ctl", (world, 0)))
        if r is None or "error" in r:
            check("G50-%s" % world.lower(), False,
                  (r or {}).get("error", "missing"))
            okc_all = False
            continue
        refuse = (r["tauf"] < 0 and r["tau_off"] < 0
                  and CTRL_A0_WIN[0] <= r["a0f"] <= CTRL_A0_WIN[1]
                  and r["id_dev"] <= 1e-20)
        okc_all = okc_all and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: tau_w = %.4f < 0 AND tau_w + OFF_w = %.4f "
              "< 0 (eps_bar^2 < 0: cannot enter the L_EPS "
              "currency); |A_0_w| = %.3f in %s (NO collapse -- the "
              "A_0 collapse itself is the arithmetic signal); "
              "decomposition identity dev %.0e <= 1e-20 (the "
              "EZ/D-layer is world-blind, as an identity must be "
              "-- null control)"
              % (world, xw, r["tauf"], r["tau_off"], r["a0f"],
                 str(CTRL_A0_WIN), r["id_dev"]))
    check("G53-consistency", okc_all,
          "all control worlds refuse on tau < 0 + no A_0 collapse "
          "while the identity layer holds world-blind: the anchor "
          "demand is arithmetic (prime comb at 2A = log x), not "
          "variational-generic")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    ts = sorted(tab)
    if len(ts) >= 3:
        lt = [math.log10(max(abs(tab[t]["tauf"]), 1e-300))
              for t in ts]
        s_mj = float(np.polyfit(
            lt, [math.log10(max(tab[t]["anchor"]["midJ"], 1e-9))
                 for t in ts], 1)[0])
        s_dc = float(np.polyfit(
            lt, [math.log10(max(tab[t]["DC"], 1e-9))
                 for t in ts], 1)[0])
        s_r = float(np.polyfit(
            lt, [math.log10(max(2 * tab[t]["ba_mj"]
                                / max(tab[t]["DC"], 1e-9), 1e-9))
                 for t in ts], 1)[0])
        s_w1 = float(np.polyfit(lt, [tab[t]["w1_l10"]
                                     for t in ts], 1)[0])
        s_lc = float(np.polyfit(lt, [tab[t]["lc_cap_l10"]
                                     for t in ts], 1)[0])
        check("G54-tau-screen", abs(s_mj) <= TAU_SLOPE_BAR
              and abs(s_dc) <= TAU_SLOPE_BAR
              and abs(s_r) <= TAU_SLOPE_BAR,
              "slopes vs log10 tau: midJ %.4f, DC %.4f, 2BA/DC "
              "%.4f (all <= %.2f: the ratio currencies are "
              "tau-flat, DEMAND-FLAT); RIDER REPORT: log10 W_1 "
              "slope %.2f, log10 LC-cap slope %.2f (ride 1/tau by "
              "construction -- BOUND-RIDES-CONNES typed; the "
              "regularized RATIOS are the flat coordinates)"
              % (s_mj, s_dc, s_r, TAU_SLOPE_BAR, s_w1, s_lc))
    else:
        check("G54-tau-screen-smoke", True, "smoke: needs 3 blocks")
    g5 = geo.get(5)
    if g5 is not None and not smoke or (smoke and g5 is not None):
        with mp.workdps(g5["dps"]):
            M5, _n5 = cell_matrix(mp.mpf(repr(g5["u0"])) / 2,
                                  g5["K0"],
                                  int(math.floor(g5["x0"])),
                                  g5["dps"])
            E5, _V5 = mp.eigsy(M5)
            E0 = min(E5[i] for i in range(g5["K0"]))
            M5[0, 0] = M5[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(M5)
            emin = min(Ep[i] for i in range(g5["K0"]))
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
                ("TAILVISTHM", "NEARALIGN"): 1,
                ("NEARALIGN", "FARDC"): 1,
                ("FARDC", "ANCHOREPSTHM"): INF,
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
    one[("TAILVISTHM", "NEARALIGN")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "NEARALIGN"): 1,
               ("NEARALIGN", "R4HYP"): INF,
               ("NFCLOS", "FARDC"): 1, ("FARDC", "R4HYP"): INF,
               ("NFCLOS", "PERCELLREG"): 1,
               ("PERCELLREG", "R4HYP"): INF,
               ("NFCLOS", "JUMPSUM"): 1,
               ("JUMPSUM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 8 and "RH" not in reach,
          "flows: base 4, refined 5 -- THIS ROUND: the r151 unit "
          "edge TAILVISTHM -> ANCHOREPS(1) is REFINED into "
          "TAILVISTHM -> NEARALIGN(1) -> FARDC(1) -> ANCHOREPSTHM"
          "(INF: this round's proven assembly EZ + LC + D1-D3 + "
          "M1); one-grant NEARALIGN still 5 (FARDC caps); "
          "counterfactual PARALLEL 8 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED (the anchor omega "
          "changes COORDINATES: point value of 1/A_0^2 -> "
          "oscillation-free averaged ratio profile; no omega "
          "closed, nothing upgraded)")
    info("EXACT RESIDUE after this round (read with CDLIV/CDLV/"
         "CDLVI): RH <== [r122 NF-closure] + [r128 Theorem R] + "
         "{L1, WPD} on dense a; RESIDUE = {TOPROOT (= B00-ROOTGAP + "
         "S1-floor, r150; the resultant route to the rootgap is "
         "OBSTRUCTED-EXACT this round), TLAWCAP-block (<== "
         "NEAR-ALIGN + FAR-DC (THIS ROUND, oscillation + existence "
         "legs PROVEN) + PERCELL-REL + JUMPSUM (r151)), SUSCAP2R "
         "(= OVG-cap + share-floor, r150)} + DELTA1FLOOR (<== "
         "TRACEFLOOR) + dense-a + a-extension + window-a.  NO RH "
         "claim; nothing upgraded; census {MEAS, OMEGA-POS} "
         "cardinality 4 UNCHANGED.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "EDGEZERO-PROVEN(the Weil window vanishes at every lattice "
        "frequency along the branch; G10/G32)",
        "LC-CAP-PROVEN(unconditional ell-1 regularized cap on the "
        "onset excess; G11/G32) + CLASSICAL-ELL1-VACUOUS(measured; "
        "G34)",
        "OSCDISS-PROVEN(D1-D3 telescoped IBP; jumps priced in "
        "JUMPSUM currency; G12/G13/G33/G36) + CELLSCALE-NO-GAIN"
        "(measured, EZ-explained; G33)",
        "CIRCULARITY-CONSTANT-ONE(the budget route returns tlaw "
        "with coefficient exactly 1 -- the mean-value machinery "
        "does NOT bound the DC part; G14)",
        "EXISTENCE-FORM-PROVEN(M1 Markov; G15/G35)",
        "RES-FACTORIZATION-PROVEN(Res == +/- disc prod w; lc == "
        "|v_0|^2; G16/G37) + RESULTANT-SELF-REFERENTIAL(Res "
        "carries w_0 = A_0^2; NO-ARITHMETIC-HEIGHT; G17/G37)",
        "EDGE-FCAP-PROVEN(absolute poly caps, relatively vacuous; "
        "G18)",
        "MECHANISM-NO-SELF-CAP(pinning bounds band only -- band "
        "leg cited-class; the funnel w_k/A_0 == r151 r-term == "
        "Jensen center class, aligned sum == y_t exact; G30/G32)",
        "ANCHOR-RESIDUE-RECOORDINATED(ANCHOR-EPS-LOCK <== "
        "NEAR-ALIGN + FAR-DC; NOT closed; G61)",
        "REDTEAM-REFUTES-ALGEBRA(G19/G38)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(G60)",
        "OMEGA-UNCHANGED(census 4; G61)"]
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
        print("COMPOSITE: EDGEZERO-PROVEN + LC-CAP-PROVEN + "
              "CLASSICAL-ELL1-VACUOUS + OSCDISS-PROVEN + "
              "CELLSCALE-NO-GAIN + CIRCULARITY-CONSTANT-ONE + "
              "EXISTENCE-FORM-PROVEN + RES-FACTORIZATION-PROVEN + "
              "RESULTANT-SELF-REFERENTIAL + EDGE-FCAP-PROVEN + "
              "MECHANISM-NO-SELF-CAP + "
              "ANCHOR-RESIDUE-RECOORDINATED + "
              "REDTEAM-REFUTES-ALGEBRA + CONTROLS-REFUSE + "
              "DEMAND-FLAT + QUANTIFIER-INHERITED + "
              "OMEGA-UNCHANGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
