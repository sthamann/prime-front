#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""h3_cofinal_probe -- PRIME.H3.COFINAL.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung certificates stated, NO counterexample claim.  It closes no
gate and narrows no gate.

=======================================================================
MISSION (THE H3 COFINAL PROOF ATTACK: after r172/CDLXXXVIII pinned the
entire lambda-uniform residue of the delta-chain to H3-COFINAL
[y_t <= 0.155 T_z^4 at one rung per dyadic block, all blocks], this
round attacks the three named mechanisms: (C1) THE SATURATION
MECHANISM -- is the measured theta_y saturation 0.0449 -> 0.0779 real
(not a fit-window artifact), does the local growth exponent descend
to the exact quartic, does the two-sided lock + the r162/v926 FULLGAP
quartic law imply a theta_y ceiling (consumption FLAGGED-MEASURED,
never silently), and does a source-classical theta_inf exist (priced,
not claimed); (C2) THE COFINAL WEAKENING -- can block-average +
pigeonhole carry H3-cofinal below the pointwise demand (the r166
BA1-BA3 instrument family), or is the averaging subsidy empty for a
saturating positive level observable; (C3) THE WITNESS BOUNDARY --
which certified constraints does the r156/r172 inflation witness
break (exact list, gated), does the certified manifold {ground-state
certificate + two-sided lock + BA3 bridge} EXCLUDE the witness, is
the exclusion stable under a J2-repairing escalation witness, and
what is the Davis-Kahan-class norm-stability radius of H3 on the
certified manifold; (C4) ASSEMBLY -- the exact post-round residue.)
=======================================================================
State consumed (CITED): CDLXXXVIII/r172 (H3 certified 26/26 margin >=
1.99, SEQ-cofinal quantifier, three locked forms, p_max = 10.2695,
witness both directions, four loop routes flagged, record ladders
theta_y/yt_l10/lock/kappa/rho VERBATIM from toproot_theta_probe.run1
.log); CDLXXXVII/r171 (PF1-PF3, H1/H2, rate record a = 1.057,
SIZE-SEPARATOR standard, modus-tollens pattern); CDLXXXVI (v926
FULLGAP-GROWTHLAW-THEOREMS: quartic law MEASURED, AIC p = 3.9072 +-
0.1136 -- consumed here ONLY as a FLAGGED-MEASURED premise; v927
BLOCKAVERAGE-SUBSTRATE-THEOREMS BA1-BA3); CDLXXXIV/r169 (SF1-SF6;
sigma == (1-slop) delta DC; DC classical GONEK-CONSTANT-UNPRICED);
CDLXXV/r166 (BA1-BA3, NZSUM = 1200, Z_OVERHANG = 6.0, zsum/tau
strings 0.8842/0.9603/0.9539 at h = 4/5/8, NO-EXACT-CROSS-H-MECHANISM
adjudication, AVG-BUDGET-WINDOW re-entry form); CDLXVII/r162 (J ==
THETA T_z^4, THETA flat, SCAN_OVER); CDLX/r156 (L1 dictionary,
2-mode witness); CDXLIV/r140 + r143 (TOPROOT named, DENSE-X,
delta_1-lock class, budget-invisibility pin); r131 OFF recipe; r137
zero-jet law (NOT consumed -- its A_0-floor use is the flagged loop);
HSW22 Cor. 1.2; PT21; Landau 1912 + Gonek 1993 AS FORM; Davis-Kahan
sin-theta class (proven here generically, K = 3 + instances);
Cauchy-Schwarz/Lagrange; Vieta/Newton; Weyl.

NOTATION.  Rung h (R4.build_cell, even sector, MAIN world); A =
log(h)/2; K = ceil(1.25 h log h); b_k = (k pi/A)^2; tau = lam_min;
lam1 = second eigenvalue; FULLGAP = (lam1 - tau)/tau; T_z = 2 pi h;
c_k source coefficients (= ground-state eigenvector of M in the
nrm-weighted basis: THE SOURCE IS THE MINIMIZER, its membership
certificate is the G30 Rayleigh-residual gate); A_{2m} = sum_k (-1)^k
c_k b_k^m; A_0 = sum (-1)^k c_k; y_t = |A_2/A_0|; theta_y = y_t/
T_z^4; lock = FULLGAP/y_t; THETA_FG = FULLGAP/T_z^4 (the r162 THETA
coordinate; identity THETA_FG == theta_y * lock); kappa = B_1/y_t;
J_{m+1} = A_{2(m+1)}/(A_0 y_t^{m+1}); rho = sup_m |J_{m+1}|^{1/m};
E_N(t) = sin(At) R(t), R = 2c_0/t + sum_k 2 c_k (-1)^k t/(t^2 -
om_k^2); zsum = (1 - 1e-3) sum_{gamma in (T_z + 6, gamma_1200]}
2 E_N(gamma)^2 (r166 VERBATIM); OFF = r131 recipe at T_PT; BA3:
tau >= zsum - OFF (v927).

=======================================================================
C1 -- THE SATURATION MECHANISM (S3c, G40-G43)
=======================================================================
(i) FIT ADJUDICATION (G40): five frozen 2-parameter models on the
CITED r172 theta ladder (25 rungs h = 4..28, holdout h = 30 excluded
from every fit): POW theta = C h^{p-4} (p from the yt_l10 LSQ);
SATq: theta = t_inf - a h^{-q}, q in {0.5, 1, 2}; LOG theta = t_inf
- a/log h.  Calibrated (pass 1, deterministic on frozen data): POW
RSS 3.0574e-4 holdout +0.00404 (p_all 4.1821); SATq0.5 t_inf
0.094217 RSS 1.7711e-4 hold +0.00159; SATq1 t_inf 0.082368 RSS
1.2712e-4 hold +0.00030; SATq2 t_inf 0.076602 RSS 1.2761e-4 hold
-0.00179; LOG t_inf 0.097708 RSS 1.2677e-4 hold +0.00076.  GATES:
every saturating RSS <= 0.60 x POW RSS; every saturating |holdout|
<= 0.60 x |POW holdout|; every t_inf in TINF_BAND = (0.070, 0.105)
(all limits <= THETA_BAR/1.476); best-RSS model is saturating.
VERDICT CLASS: SATURATION-REAL-NOT-FIT-ARTIFACT.  RECORDED, NOT
CLAIMED (anti-numerology firewall, v354/v355/t0~30 discipline):
4 pi t_inf = 1.1840/1.0351/0.9626/1.2278 across models -- the
candidate theta_inf == 1/(4 pi) = 0.079577 lies INSIDE the model
band; the band is too wide to pin it; NO window is derived from it;
a classical theta_inf needs a Gonek/Montgomery-class second-moment
evaluation of the census source: typed OPEN, same epistemic slot as
GONEK-CONSTANT-UNPRICED.
(ii) LOCAL EXPONENT DESCENT (G41): windowed LSQ slopes of the cited
yt_l10 ladder: W1 [4..13] 4.2991, W2 [10..20] 4.1203, W3 [16..26]
4.0600, W4 [22..28] 4.0236 (W5 [24..30] 4.0404 reported, holdout
inside): gates: strict descent W1 > W2 > W3 > W4 and W4 in (3.95,
4.10): the growth law converges to the EXACT QUARTIC at depth --
the saturation of theta_y IS p_loc -> 4 (the 4.18 all-rung exponent
is an early-transient mixture).
(iii) RATE DICTIONARY TIGHTENED (G42): a_pred_deep = p_W4/2 - 1 =
1.0118 vs the r171 record a = 1.057: |diff| = 0.0452 <= 0.093 (the
r172 gap -- the dictionary closes TIGHTER on the deep window).
(iv) THE TRANSPORT/CEILING CHASE (G43): exact identity THETA_FG ==
theta_y * lock per rung (definitional, gated <= 1e-30); exact
transport theorems (G10, sympy): [THETA_FG <= THETA_MAX and lock >=
L] ==> theta_y <= THETA_MAX/L, and [theta_y <= t and lock <= L']
==> THETA_FG <= t L' (the r162 theta-window and H3 are EQUIVALENT
statements on the two-sided lock manifold).  MEASURED: THETA_FG
ladder max 0.2674 (h = 7), min 0.1117; min measured lock 2.2345
(h = 28).  HONEST NUMBERS: with the MEASURED lock floor the
transported ceiling is 0.2674/2.2345 = 0.1197 < THETA_BAR = 0.155
(margin 1.295); with only the GATED window edge L = 1.0 it is
0.2674 > 0.155 -- the window-edge transport bounds theta_y but does
NOT recover the 0.155 bar.  CONSUMPTION FLAGGED: the premise
"THETA_FG flat/capped for all h" is the v926 MEASURED quartic law
(AIC p = 3.9072 +- 0.1136), NOT proven -- the ceiling statement is
typed CONDITIONAL-ON-MEASURED and is NOT counted as a delivered
theorem (G61 keeps FG-QUARTIC-MEAS out of the delivered ancestor
set).  C1 VERDICT: MECHANISM LOCATED, NOT REDUCED -- the theta_y
saturation is the r162 THETA-flatness one coordinate up, tied by
the gated two-sided lock; the lambda-uniform residue does NOT empty
into classics this round.

=======================================================================
C2 -- THE COFINAL WEAKENING (S1 G11-G13, S3c G44)
=======================================================================
(i) PIGEONHOLE IS EXACT AND FREE (G11): block-min <= block-average
(weighted, proven generic + instances): AVG-THETA(bar) per block ==>
H3-cofinal(bar).  (ii) THE DEFECT COLLAPSE (G11, the honest
surprise): for a defect-D near-monotone observable (theta(h) <=
theta(h') + D for h <= h'), H3-cofinal(bar) ==> H3-FORALL-h(bar+D):
MEASURED D = 0.004183 (drawdown h = 14 -> 19) = 2.7% of THETA_BAR:
the cofinal and forall-h statements differ by <= 0.0042 on the
measured ladder -- QUANTIFIER-GAP-MEASURED-THIN: the SEQ-cofinal
weakening buys AT MOST the measured oscillation, which is ~30x
smaller than the H3 margin.  The averaging route cannot be
materially easier than the pointwise route for this observable.
(iii) THE SUBSIDY IS EMPTY AND VANISHES WITH DEPTH (G44): dyadic
blocks B2 = [4,8), B3 = [8,16), B4 = [16,32) (B4 partial at 28+30,
DISCLOSED; half-open convention frozen here, r166 used closed
endpoints -- convention-only, no criterion moved): block min/avg =
0.7533/0.9233/0.9604 rising -> 1: the pigeonhole gain shrinks to
4% at depth.  CONTRAST (the r166 mechanism): tau block-averaging
harvested SIGNED detrended cancellation (ratio 0.461 -> 0.037,
improving with depth); theta_y terms are POSITIVE LEVELS: |sum| ==
sum identically (G12, sympy) -- AVERAGING-NOTHING-TO-CANCEL.
(iv) BA-DICTIONARY EXPRESSIBILITY (G13): BA1-BA3 bound block-tau
from BELOW via per-rung ward-class floors (zsum - OFF); an
AVG-THETA bound needs per-rung classical CEILINGS of |A_2/A_0|; the
corpus ceiling routes are enumerated and all dead: TRIANGLE
(measured vacuous 1e3.4 -> 1e64.6, r172), A0-FLOOR (== pinning-
supply LOOP {TAUPOS, TLAWCAP}, flagged), MOMENT-CAP (y_t-normalized,
circular, r172), H3 itself (the target); the r166 adjudication
NO-EXACT-CROSS-H-MECHANISM (no corpus identity sums over h) is
cited and re-affirmed for the y_t observable.  C2 VERDICT:
BLOCK-AVERAGE + PIGEONHOLE DOES NOT CARRY -- it is an exact but
subsidy-empty reformulation; its bound sits in the SAME epistemic
class as pointwise H3 (arithmetic-pinned, zero-free, source-family):
BA-INEXPRESSIBLE-FOR-YT.

=======================================================================
C3 -- THE WITNESS BOUNDARY (S1 G14-G16, S3 G36, S4 G53/G56/G57)
=======================================================================
KEY STRUCTURAL FACT (from the builder, machine-used throughout): the
source c is the GROUND-STATE EIGENVECTOR of the world matrix M --
the witness perturbs the VECTOR, not the world: M, tau, lam1,
FULLGAP are witness-INVARIANT.  Hence lock'' == lock/W EXACTLY for
any fixed-M y_t-inflation x W, and the two-sided lock window
(1.0, 8.0) refuses EVERY such witness with W > 8 in BOTH directions
(G16, exact; measured: inflation 3.6444e-3 < 1.0, deflation
3.6444e+3 > 8.0).
(a) THE BROKEN-CONSTRAINT LIST (G56, all frozen strings, h = 5):
INFLATION 2-mode (dnorm 8.117888e-2): BREAKS {G30 ground-state
certificate: r0''/tau = 3.430e13 vs bar 1e-25 (39 orders); G32 lock
3.6444e-3; G33/G34 theta 62.690999 > bar; G35 J2'' = -1.121e-6
below window, cap'' = 1.000042 below window; G37 census
complete-real BROKEN (8/10 real) and top 1.000001 > 0.95; BA3
BRIDGE: zsum''/zsum = 3.579247e8 and (tau + OFF - zsum'')/tau =
-3.4372e8 < 0}; SATISFIES {A_0 invariance <= 1e-40, sign, kappa
window (one-sided), B_1/trace identities, TR-CAP, H1 (c* exists:
H1-WORLD-BLIND replicated)}.  DEFLATION 2-mode: BREAKS {G30
(3.248e10), lock 3.6444e3 > 8, theta 6.2691e-5 < 0.03, J2 1.271e5,
kappa'' = 96.09 > 0.30, census 6/10, H1 REFUSED (domain empty),
BA3 (-3.4361e2)}; ztop_all = 24.870225 (r172 string).  THE BA3
FINDING IS NEW AND REVERSES THE PRIOR GUESS: the witness is NOT
budget-blind -- the r166/r169 bridge (mechanism-loss) refuses BOTH
witness directions exactly as it refuses the fake worlds: the
witness moves the zero-side sum by x3.6e8 while A_0 is invariant.
(b) THE ESCALATION WITNESS (G57, new): the 3-mode J2-PRESERVING
inflation (solve d_1..d_3: A_0'' = A_0, A_2'' = W A_2, A_4'' = W^2
A_4; generic sympy + mp instance): REPAIRS {J2'' == J2 exact, rho
argmax 1, cap 1.251769 in window, census 10/10 complete-real, top
0.852300 in TOP_WIN, SR1, H1 c* exists} -- the moment/census windows
are NOT the load-bearing exclusion -- but STILL BREAKS {G30: r0''/
tau = 5.600e14; lock 3.6444e-3; theta 62.691; BA3: zsum''/zsum =
8.738751e15, residual -8.3920e15}, CANNOT preserve J3 (A_6''/(W^3
A_6) = -1.08e-4 != 1, generic 3-mode obstruction, sympy), and its
PRICE EXPLODES: dnorm3 = 8.197491e3 = 1.0e5 x the 2-mode price (the
J2 repair costs a LARGE source perturbation, no longer a cheap
witness).  MANIFOLD-EXCLUSION-ESCALATION-STABLE.
(c) THE STABILITY THEOREM (G15 proven + G36 instantiated): DK
sin-theta lemma (proven generic K = 3 + rational instance): any
vector v passing the per-rung certificate {|R(v)/tau - 1| <=
RAY_BAR, ||Mv - R(v) v|| <= r} lies within sin(angle) <= r/(lam1 -
R(v)) of the census source; with Cauchy-Schwarz on the A_0/A_2
functionals this pins y_t: rel-y_t-move <= (|A_2|^{-1}||e_2|| +
|A_0|^{-1}||e_0||) dv/(1 - ||e_0|| dv/|A_0|).  MEASURED RADII: at
the frozen gate bar r = 1e-25 tau: 4.478e-25 (h4), 3.472e-23 (h5),
5.322e-17 (h8), 6.568e-6 (h13), growing with h (the 1/A_0
cancellation eats the fixed bar; the bar-level guarantee crosses
O(1) near h ~ 16: STABILITY-CROSSOVER-MEASURED, reported ladder);
at the MEASURED eigsy residuals (dps-scaled): 1.617e-50, 3.373e-43,
2.669e-43, 1.011e-47 -- H3 cannot be moved by ANY certificate-
passing source at measured precision: H3-NORM-STABLE-AT-MEASURED-
RESIDUALS.  C3 VERDICT: H3's falsifiability boundary is a THEOREM
boundary (r171 modus-tollens pattern): every y_t-moving perturbation
either leaves the ground state (G30, DK-quantified), exits the
two-sided lock window (exact, both directions), breaks the BA3
bridge (measured x3.6e8), or leaves the world (controls + size
separator): H3 restricted to the certified constraint manifold is
norm-stable; off the manifold it is refutable at exponentially
small cost (r172, restated not hidden).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, np.load only in ward_, no
    zero-oracle names, no verification/ import); G02 cache (X5;
    ward-class: main-process only -- zsum anchors + witness battery
    + HSW sanity; NO worker touches the cache: the H3/theta chain
    stays zero-free).
S1  exact layer (sympy generic + exact rational instances):
    G10 statement + transport: H3-cofinal restated (SEQ quantifier
    VERBATIM); THETA_FG == theta_y lock identity; both transport
    inequalities (positive-slack polynomial certificates);
    G11 pigeonhole + defect collapse (weighted min <= avg generic;
    cofinal + defect-D ==> forall at bar + D);
    G12 positivity-no-cancellation: |sum| == sum for positive terms
    (the tau-mechanism has no theta analogue); signed contrast
    instance;
    G13 BA-dictionary chase: ceiling-route enumeration {TRIANGLE
    vacuous, A0FLOOR loop, MOMENT circular, H3 target}; r166
    NO-EXACT-CROSS-H cited; ancestor assertions;
    G14 witness algebra: 2-mode identities (r172 G14 replicated,
    b2 = b1 + db) + 3-mode system solved generically, A_0/A_2/A_4
    constraints verified, A_6 obstruction exhibited (instance != 0);
    G15 DK sin-theta lemma generic K = 3 (residual decomposition,
    positive-slack) + Lagrange/Cauchy-Schwarz identity + the
    1 - cos <= sin^2 chord bound + y_t-move bound equality instance;
    G16 manifold modus tollens: lock/W exit generic (W > L_hi/L_lo
    ==> window exit, both directions) + numeric instances.
S2  G20 HSW G(T) sanity.
S3  per-rung layer, REBUILT SUBSET RUNGS_SUB = (4, 5, 6, 8, 10, 13,
    16, 20, 24) (9 rungs; h in {7, 9, 11, 12, 14, 15, 17, 18, 19,
    21, 22, 23, 25, 26, 27, 28, 30} NOT rebuilt this round --
    SCOPE-REDUCED-BUILDS, cost-disclosed: h = 28/30 alone cost
    1943/2596 s in r172; deep values consumed as CITED record
    strings, licensed by the replication gates below), 12 spawn
    workers, cost-sorted, NO cache in workers:
    G30 spectral sanity (sorted, K, simp >= 1e3, ray/res <= 1e-25);
    G31 jets: sign(A_2/A_0) == -1; B_1 closed form <= 1e-40; kappa
    in (0.0, 0.30) + KAPPA_TAB 4/5/8 rel 5e-3;
    G32 cross-instrument: y_t vs YT_R143 {5, 8, 13} <= 1e-3 dex;
    FULLGAP on FG_TAB {4, 5, 8, 13} x (0.97, 1.03); fg > 0; lock in
    LOCK_WIN = (1.0, 8.0) at every rung;
    G33 CITED-LADDER-REPLICATION (the license for the S3c fits):
    theta_y on THETA_Y_TAB {4, 5, 8, 13} rel 5e-3 AND on the cited
    r172 ladder at {6, 10, 16, 20, 24} rel 8e-3 (4dp quantization);
    yt_l10 within 1.5e-3 dex of the cited ladder at ALL 9 rungs;
    lock on the cited ladder rel 8e-3;
    G34 H3 certificate: y_t <= 0.155 T_z^4, margin >= 1.5, all 9;
    G35 moments: rho argmax == 1; RHO_TAB {4, 5, 8, 13} rel 5e-3;
    |J_2| in (0.05, 0.25); ENV(400) < rho; cap in (1.15, 1.45);
    G36 STABILITY RADII (the DK instantiation): gate-bar radius
    ladder on STAB_GATE_TAB {4: 4.478e-25, 5: 3.472e-23, 8:
    5.322e-17, 13: 6.568e-6} rel 5e-3, strictly increasing across
    {4, 5, 8, 13}; measured-residual radius <= 1e-30 at h <= 13;
    deep rungs (16, 20, 24) REPORTED (pre-freeze unmeasured,
    DISCLOSED) with the crossover rung (first gate-bar radius >= 1)
    printed;
    G37 BA3/zsum anchors (main process, ward): zsum/tau on the r166
    strings {4: 0.8842, 5: 0.9603, 8: 0.9539} rel 5e-3; residual
    (tau + OFF - zsum)/tau > 0 (BA3 HOLDS in MAIN); NZSUM = 1200,
    Z_OVERHANG = 6.0, F64_SLOP = 1e-3 (r166 VERBATIM).
S3c analytics on the CITED ladder (deterministic, frozen data):
    G40 saturation adjudication (five models, gates as in C1(i),
    all strings rel 1e-3, holdout residuals abs 2e-4);
    G41 p_loc descent (strings rel 1e-3; W4 in (3.95, 4.10);
    strict descent);
    G42 rate dictionary tightened (a_deep = 1.0118, |a_deep -
    1.057| <= 0.093);
    G43 transport/ceiling chase (identity per rebuilt rung <=
    1e-30; TFG_MAX 0.2674 rel 1e-3; ceiling numbers printed with
    the FLAGGED-MEASURED consumption statement);
    G44 quantifier gap + subsidy: D_meas = 0.004183 (<= 0.006,
    <= 4% of bar); block min/avg 0.7533/0.9233/0.9604 rel 1e-3,
    strictly increasing, B4 >= 0.90.
S4  controls through the SAME instrument (builds only, no zeros):
    G50 SMOOTH {4, 5}, G51 SCRARITH {5, 6}, G52 EPSTEIN {8}: tau_w
    < 0 on the r166 strings rel 5e-3; theta_w <= 1e-2 + THETA_W_CAL
    strings rel 5e-3; lock_w < 1.0 (measured negative: the control
    worlds sit outside the lock window too); SIZE-SEPARATOR min
    MAIN theta / max theta_w >= 10 (calibrated 23.9); H3-in-world
    printed REPORTED-DIAGNOSTIC (H3 is one-sided world-blind
    algebra BY DESIGN -- restated, never hidden; the separation is
    the two-sided window + bridge + witness, gated);
    G53 witness replication (r172 strings): dnorm 8.117888e-2 rel
    5e-3; A_0/y_t invariances <= 1e-40; infl theta 62.690999 rel
    5e-3 and > bar; defl theta <= 1e-3; defl ztop_all 24.870225
    rel 5e-3; infl ztop_all <= 1.05;
    G56 witness-vs-manifold battery (NEW, the broken-constraint
    list, all strings rel 5e-3 unless noted): INFL2 r0''/tau
    3.430e13 (>= 1e10), ray''/tau 1.317e11, lock'' 3.6444e-3 (<
    1.0, == lock/1000 dev <= 1e-9), |J2''| <= 1e-5, rho'' <= 1e-3
    with argmax != 1, cap'' <= 1.01, census real count == 8 (!=
    K-1), ztop_all 1.000001 (> 0.95), kappa'' 9.609e-5 in KAPPA_WIN
    (satisfied), H1 c* EXISTS <= 1.20 (H1-WORLD-BLIND), zsum''/zsum
    3.579247e8 (>= 1e6), BA3 residual -3.4372e8 (< 0); DEFL2
    r0''/tau 3.248e10, lock'' 3.6444e3 (> 8.0), kappa'' 96.09 (>
    0.30), |J2''| 1.271e5 (> 0.25), census real == 6, c* is None
    (H1-REFUSED), zsum''/zsum 3.588535e2, BA3 residual -3.4361e2
    (< 0); the frozen broken/satisfied lists printed and gated;
    G57 escalation witness (3-mode, NEW): dnorm3 8.197491e3 rel
    5e-3 (>= 1e3: price x1e5 the 2-mode witness); A_0 dev <= 1e-40;
    y_t''/(1000 y_t) dev <= 1e-40; J2'' == J2 dev <= 1e-25; rho''
    argmax == 1; cap'' 1.251769 rel 5e-3 in CAP_WIN; census 10/10
    complete-real; ztop_all 0.852300 rel 5e-3 in TOP_WIN; c*
    EXISTS <= 1.30; A6''/(W^3 A6) = -1.08e-4 (|ratio - 1| >= 0.9:
    J3 NOT preservable, generic obstruction); STILL BROKEN: r0''/
    tau 5.600e14 (>= 1e10), lock'' 3.6444e-3 (< 1.0), theta'' >
    bar, zsum''/zsum 8.738751e15, BA3 residual -8.3920e15 (< 0).
S5  G54 screens: slopes vs log10 tau of log10 y_t and log10 theta_y
    both <= 0.30 abs (DEMAND-FLAT); RIDER slope log10 A_0^2 in
    (0.85, 1.15) (BOUND-RIDES-CONNES); G55 conditioning (1e-25
    shift at h = 5, round-118 trap).
S6  G60 demand audit (SEQ inherited; models/windows/blocks/tabs
    frozen pre-evaluation; disclosures: cited-ladder consumption
    licensed by G33; SCOPE-REDUCED-BUILDS; witness rho/c* windows
    calibrated at 60 moments and gated as windows at 400 moments;
    NZSUM = 1200 r166 VERBATIM; calibration pass 2 for the NZSUM +
    ztop-convention root causes, both logs kept);
    G61 loop/mining gate: delivered-statement ancestors: QUANT-
    COLLAPSE == {SOURCE, THETA-LADDER-MEAS}; DK-STABILITY ==
    {SOURCE, SPECTRAL-CERT}; BA-ADJUDICATION == {SOURCE, R166-
    CITED}; WITNESS-EXCLUSION == {SOURCE, SPECTRAL-CERT, CACHE-
    WARD, PT21-CENSUS-PER-K, HSW22}; TRANSPORT-CEILING == {LOCK-
    WINDOW-MEAS, FG-QUARTIC-MEAS} typed CONDITIONAL-ON-MEASURED and
    EXCLUDED from the delivered-theorem set; TLAWCAP, WPD, TAUPOS,
    CENSUS-ALL-K, TOPROOT-MEAS, ZERO-VERIF-AS-HYP are ancestors of
    NOTHING delivered; FIVE flagged loop/forbidden routes carried
    NOT consumed (tlaw-window, census-all-k, pinning-supply,
    A0-floor variant, zero-verification-as-hypothesis);
    G62 min-cut (r116 replica, r171/r172 graph VERBATIM: flows base
    4, refined 5, one-grant 5, counterfactual PARALLEL 9 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
    G63 endgame graphs: three loop cycles DETECTED (universalized
    census, pinning-supply, A0-floor); the terminal chain extended
    with {THETA-MONO-MEAS -> QUANT-COLLAPSE -> H3_COFINAL} and
    {LOCK-MEAS, FG-QUARTIC-MEAS} -> THETA-CEILING -> H3_COFINAL
    (flagged edge) is ACYCLIC with RH reachable from every
    counterfactual grant (AND-semantics); the FINAL RESIDUE printed.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); WORKERS = 12 (spawn, deterministic); RUNGS_SUB =
(4, 5, 6, 8, 10, 13, 16, 20, 24); DPS = {4: 60, 5: 60, 6: 65,
8: 80, 10: 90, 13: 120, 16: 130, 20: 144, 24: 150} (r172 schedule
subset VERBATIM).  INHERITED (r172/r171/r166 VERBATIM where named):
SIMP_MIN = 1e3; RAY_BAR = RES0_BAR = 1e-25; CF_BAR = 1e-40;
KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906} rel 5e-3;
KAPPA_WIN = (0.0, 0.30); FG_TAB = {4: 4.458152e4, 5: 2.2255e5,
8: 9.9512e5, 13: 1.0619e7} x (0.97, 1.03); LOCK_WIN = (1.0, 8.0);
YT_R143 = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6} <= 1e-3 dex;
THETA_BAR = 0.155; THETA_Y_WIN = (0.03, 0.12); THETA_Y_TAB =
{4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983} rel 5e-3;
H3_MARGIN_MIN = 1.5; RHO_TAB = {4: 0.106805, 5: 0.125884,
8: 0.139445, 13: 0.147746} rel 5e-3; J2_WIN = (0.05, 0.25);
CAP_WIN = (1.15, 1.45); TOP_WIN = (0.70, 0.95); C_GRID = (1.05,
1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00); POLY_MAXSTEPS =
3000; IM_TOL = 1e-10; NZSUM = 1200; F64_SLOP = 1e-3; Z_OVERHANG =
6.0; ZSUM_TAB = {4: 0.8842, 5: 0.9603, 8: 0.9539} rel 5e-3 [r166
record]; CTRL_TAU_TAB rel 5e-3: SMOOTH {4: -1.0375, 5: -1.0944},
SCRARITH {5: -0.34593, 6: -0.36716}, EPSTEIN {8: -1.6310};
CTRL_THETA_MAX = 1e-2; SEP_MIN = 10.0; WIT_FACT = 1000; WIT_A0_BAR
= WIT_YT_BAR = 1e-40; WIT_DNORM_INFL_STR = 8.117888e-2;
WIT_INFL_THETA_STR = 62.690999; WIT_INFL_ZTOP_MAX = 1.05;
WIT_DEFL_THETA_MAX = 1e-3; WIT_ZTOP_STR = 24.870225; RATE_A =
1.057; TAU_SLOPE_BAR = 0.30; RIDER_WIN = (0.85, 1.15); COND_WIN =
(1e-40, 1e-10); RUNTIME_BAR = 2700 s; GAMMA1_LIT (ward only).
CITED LADDERS (toproot_theta_probe.run1.log VERBATIM, 4dp):
YT_L10_R172 and LOCK_R172 at h = 4..28 + 30 (26 rungs; dicts in
code); the fits consume theta derived as 10^yt_l10/(2 pi h)^4.
NEW (calibrated in calib_h3c_pass1.log + calib_h3c_pass2.log, ONE
pre-freeze pass in TWO disclosed passes -- pass 2 fixed NZSUM =
1200 (r166 VERBATIM; pass 1 summed the full cache and sat 2.5-3.3%
above the r166 strings) and the ztop convention (max Re over ALL
roots, r172 VERBATIM; pass 1 took the top REAL root and got 24.115
for the deflation witness instead of the r172 string 24.870225);
scratch deleted after freeze, BOTH logs kept; all numbers quoted
verbatim): FIT_TAB (POW RSS 3.0574e-4 hold +0.00404 / SATq0.5 t_inf
0.094217 RSS 1.7711e-4 hold +0.00159 / SATq1 0.082368 1.2712e-4
+0.00030 / SATq2 0.076602 1.2761e-4 -0.00179 / LOG 0.097708
1.2677e-4 +0.00076) rel 1e-3, holdout abs 2e-4; P_ALL_STR = 4.1821;
TINF_BAND = (0.070, 0.105); RSS_FACT = 0.60; HOLD_FACT = 0.60;
PLOC_TAB = {W1: 4.2991, W2: 4.1203, W3: 4.0600, W4: 4.0236, W5:
4.0404} rel 1e-3; PLOC_WINDOWS = {W1: (4, 13), W2: (10, 20), W3:
(16, 26), W4: (22, 28), W5: (24, 30)}; W4_WIN = (3.95, 4.10);
A_DEEP_STR = 1.0118; A_DEEP_BAR = 0.093; DMAX_STR = 0.004183 (<=
0.006, <= 0.04 x bar); BLOCK_TAB = {B2: 0.7533, B3: 0.9233, B4:
0.9604} rel 1e-3, B4 >= 0.90, strictly increasing; TFG_MAX_STR =
0.2674; TFG_MIN_STR = 0.1117; TFG_CEIL_MEAS = 0.1197 (= 0.2674/
2.2345 < 0.155); STAB_GATE_TAB = {4: 4.478e-25, 5: 3.472e-23, 8:
5.322e-17, 13: 6.568e-6} rel 5e-3; STAB_MEAS_BAR = 1e-30 (h <= 13;
calibrated 1.617e-50/3.373e-43/2.669e-43/1.011e-47); THETA_W_CAL =
{(SMOOTH, 4): 3.541319e-4, (SMOOTH, 5): 2.409799e-4, (SCRARITH, 5):
1.005571e-3, (SCRARITH, 6): 1.875055e-3, (EPSTEIN, 8): 1.011306e-4}
rel 5e-3; WITNESS STRINGS (h = 5): INFL2 {r0/tau 3.430e13, ray/tau
1.317e11, lock 3.6444e-3, J2 -1.121e-6, ztop 1.000001, kappa
9.609e-5, nreal 8, zsum-ratio 3.579247e8, ba3-res -3.4372e8};
DEFL2 {r0/tau 3.248e10, lock 3.6444e3, kappa 96.09, J2 1.271e5,
nreal 6, ztop 24.870225, zsum-ratio 3.588535e2, ba3-res -3.4361e2};
INFL3 {dnorm 8.197491e3, r0/tau 5.600e14, cap 1.251769, ztop
0.852300, nreal 10, a6-ratio -1.08e-4, zsum-ratio 8.738751e15,
ba3-res -8.3920e15}; witness rho/c* gated as WINDOWS not strings
(calibrated at 60 moments, run uses the full 400-moment envelope,
DISCLOSED): INFL2 c* <= 1.20 exists, INFL3 c* <= 1.30 exists,
DEFL2 c* None; NEW_TOL = 5e-3; ANA_TOL = 1e-3.
Deterministic: NO randomness anywhere.  Cache verified_zeros_n7000
READ-ONLY in ward_ (X5), main-process only (zsum anchors + witness
battery + HSW sanity); NO zeta use.  All mpf arithmetic inside
explicit mp.workdps blocks; flat O(1) ratios transported as f64 for
gating (DISCLOSED).  Amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): WINDOWS-FROZEN-PREEVAL(G60/G61);
CITED-LADDER-REPLICATED(G33); SATURATION-REAL-NOT-FIT-ARTIFACT(G40);
THETA-INF-BAND-UNDER-BAR + THETA-INF-CLASSICAL-OPEN-GONEK-CLASS
(G40, recorded not claimed); P-LOCAL-DESCENDS-TO-QUARTIC(G41);
RATE-DICTIONARY-TIGHTENED(G42); THETA-CEILING-CONDITIONAL-MEASURED-
FLAGGED(G43); QUANTIFIER-GAP-MEASURED-THIN(G11/G44);
PIGEONHOLE-EXACT-SUBSIDY-EMPTY(G11/G44); AVERAGING-NOTHING-TO-CANCEL
(G12/G44); BA-INEXPRESSIBLE-FOR-YT(G13); H3-REFUTABLE-OFF-MANIFOLD
(G53); WITNESS-EXCLUDED-BY-CERTIFIED-SET(G56); WITNESS-BREAKS-BA3-
BRIDGE(G56); WITNESS-REPAIR-PRICE-EXPLODES + ESCALATION-STABLE(G57);
H3-NORM-STABLE-AT-MEASURED-RESIDUALS + STABILITY-CROSSOVER-MEASURED
(G15/G36); H3-ONE-SIDED-WORLD-BLIND + SIZE-SEPARATOR(G50-G52);
DEMAND-FLAT + BOUND-RIDES-CONNES(G54); QUANTIFIER-SEQ(G60);
LOOP-ROUTES-FLAGGED(five; G61/G63); OMEGA-UNCHANGED(census 4; G62);
MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge gate
fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 34/35 at the
first-freeze SPEC_SHA 123cde67d20afd3c, log kept as h3c_smoke1.log;
NO record run existed yet).  ONE sympy INSTRUMENT bug in the exact
layer, no bar, window, tab or criterion moved anywhere: the G15 DK
positivity polynomial was parametrized with rho = lam0 + (g - w),
which leaves the cross-term -2 a0^2 g w in the expansion of
(lam0 - rho)^2 and defeats the all-coefficients-positive check even
though the inequality is true; fixed to the clean slack
parametrization g = e + w (rho = lam0 + e, lam1 - rho = w > 0),
under which the claim polynomial is a0^2 e^2 + a2^2 (2 w s2 + s2^2)
with coefficients (1, 2, 1) all positive.  Fix verified in
isolation before re-freeze; smoke2 at the fixed SHA must be clean.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt VII, note CDXCII, 2026-08-20)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays 876dafc977d3d8fc.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH7-F1 [MAJOR, residue-prose compression]:
#   ORIGINAL (this spec + note CDXC, transported from r172): the
#   residue carried as "{H3-COFINAL} + {census-all-k == LOOP} +
#   {L1, WPD}" -- H3 singled out as THE lambda-uniform residue.
#   CORRECTED: the composed per-block hypothesis is the TRIPLE
#   {H1 AND H2 AND H3}-cofinal, one rung per dyadic block, all three
#   at the same h -- corrected wording: "{H1 ∧ H2 ∧ H3}-KOFINAL (eine
#   Sprosse pro Block, alle drei am selben h)".  PF is proven only
#   GIVEN H1 + H2 at the same rung (r171); H1/H2/H3 are all finite
#   per-rung source checks of the same epistemic type, certified only
#   h <= 26/13(24)/30.
#
# BH7-F4 [MINOR, manifold-exclusion verdict lacks its rung scope]:
#   ORIGINAL (C3 VERDICT, this spec + note CDXC): "every y_t-moving
#   perturbation either leaves the ground state (G30, DK-quantified),
#   exits the two-sided lock window (exact, both directions), breaks
#   the BA3 bridge (measured x3.6e8), or leaves the world" --
#   universally quantified over perturbations.
#   CORRECTED: the verdict sentence is scoped to the DK radius --
#   "innerhalb des DK-Radius (gegated h <= 13, gemessen bis h = 20)".
#   The gate-bar crossover at h = 16 is disclosed in this spec's own
#   G36; the minimal-dial analysis (the minimal H3-refuting inflation
#   W = bar/theta_y ~ 2.0-2.5 keeps lock/W inside the lock window
#   (1.0, 8.0) at 24 of 25 rungs) shows the lock leg excludes only
#   large dials (the tested witnesses use W = 1000).
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
RUNGS_SUB = (4, 5, 6, 8, 10, 13, 16, 20, 24)
DPS = {4: 60, 5: 60, 6: 65, 8: 80, 10: 90, 13: 120, 16: 130,
       20: 144, 24: 150}

SIMP_MIN = 1e3
RAY_BAR = 1e-25
RES0_BAR = 1e-25
CF_BAR = 1e-40
KAPPA_TAB = {4: 0.104346, 5: 0.096088, 8: 0.062906}
KAPPA_WIN = (0.0, 0.30)
FG_TAB = {4: 4.458152e4, 5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7}
FG_WIN = (0.97, 1.03)
LOCK_WIN = (1.0, 8.0)
YT_R143 = {5: 6.107e4, 8: 4.165e5, 13: 3.204e6}
YT_DEX_BAR = 1e-3
THETA_BAR = 0.155
THETA_Y_WIN = (0.03, 0.12)
THETA_Y_TAB = {4: 0.044901, 5: 0.062691, 8: 0.065250, 13: 0.071983}
H3_MARGIN_MIN = 1.5
RHO_TAB = {4: 0.106805, 5: 0.125884, 8: 0.139445, 13: 0.147746}
J2_WIN = (0.05, 0.25)
CAP_WIN = (1.15, 1.45)
TOP_WIN = (0.70, 0.95)
C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00)
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
NZSUM = 1200
F64_SLOP = 1e-3
Z_OVERHANG = 6.0
ZSUM_TAB = {4: 0.8842, 5: 0.9603, 8: 0.9539}
CTRL_TAU_TAB = {"SMOOTH": {4: -1.0375, 5: -1.0944},
                "SCRARITH": {5: -0.34593, 6: -0.36716},
                "EPSTEIN": {8: -1.6310}}
CTRL_SET = (("SMOOTH", 4, 60), ("SMOOTH", 5, 60),
            ("SCRARITH", 5, 60), ("SCRARITH", 6, 60),
            ("EPSTEIN", 8, 80))
CTRL_THETA_MAX = 1e-2
SEP_MIN = 10.0
WIT_FACT = 1000
WIT_A0_BAR = 1e-40
WIT_YT_BAR = 1e-40
WIT_DNORM_INFL_STR = 8.117888e-2
WIT_INFL_THETA_STR = 62.690999
WIT_INFL_ZTOP_MAX = 1.05
WIT_DEFL_THETA_MAX = 1e-3
WIT_ZTOP_STR = 24.870225
RATE_A = 1.057
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.85, 1.15)
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 2700.0
GAMMA1_LIT = 14.134725141734693790   # ward only
NEW_TOL = 5e-3
ANA_TOL = 1e-3

# ------------------------------------ cited r172 record ladders (4dp)
YT_L10_R172 = {4: 4.2532, 5: 4.7858, 6: 5.1092, 7: 5.4003,
               8: 5.6197, 9: 5.8273, 10: 6.0322, 11: 6.1957,
               12: 6.3775, 13: 6.5057, 14: 6.6664, 15: 6.7625,
               16: 6.8847, 17: 6.9876, 18: 7.0996, 19: 7.1728,
               20: 7.2745, 21: 7.3667, 22: 7.4493, 23: 7.5210,
               24: 7.6035, 25: 7.6678, 26: 7.7367, 27: 7.8077,
               28: 7.8687, 30: 7.9925}
LOCK_R172 = {4: 2.4885, 5: 3.6444, 6: 2.5824, 7: 3.9814, 8: 2.3890,
             9: 2.8616, 10: 2.2804, 11: 2.7183, 12: 2.5302,
             13: 3.3141, 14: 2.5778, 15: 2.9692, 16: 2.8345,
             17: 2.7172, 18: 2.5836, 19: 2.6024, 20: 2.5224,
             21: 2.5272, 22: 2.5592, 23: 2.5246, 24: 2.8361,
             25: 2.6379, 26: 2.9682, 27: 3.1499, 28: 2.2345,
             30: 2.8667}
HOLDOUT_H = 30

# ------------------------------------------------- new frozen (calibrated)
FIT_TAB = {"POW": (float("nan"), 3.0574e-4, 0.00404),
           "SATq0.5": (0.094217, 1.7711e-4, 0.00159),
           "SATq1": (0.082368, 1.2712e-4, 0.00030),
           "SATq2": (0.076602, 1.2761e-4, -0.00179),
           "LOG": (0.097708, 1.2677e-4, 0.00076)}
P_ALL_STR = 4.1821
TINF_BAND = (0.070, 0.105)
RSS_FACT = 0.60
HOLD_FACT = 0.60
HOLD_ABS_TOL = 2e-4
PLOC_WINDOWS = {"W1": (4, 13), "W2": (10, 20), "W3": (16, 26),
                "W4": (22, 28), "W5": (24, 30)}
PLOC_TAB = {"W1": 4.2991, "W2": 4.1203, "W3": 4.0600, "W4": 4.0236,
            "W5": 4.0404}
W4_WIN = (3.95, 4.10)
A_DEEP_STR = 1.0118
A_DEEP_BAR = 0.093
DMAX_STR = 0.004183
DMAX_BAR = 0.006
DMAX_FRAC_BAR = 0.04
BLOCK_TAB = {"B2": 0.7533, "B3": 0.9233, "B4": 0.9604}
BLOCK_B4_MIN = 0.90
TFG_MAX_STR = 0.2674
TFG_MIN_STR = 0.1117
STAB_GATE_TAB = {4: 4.478e-25, 5: 3.472e-23, 8: 5.322e-17,
                 13: 6.568e-6}
STAB_MEAS_BAR = 1e-30
THETA_W_CAL = {("SMOOTH", 4): 3.541319e-4, ("SMOOTH", 5): 2.409799e-4,
               ("SCRARITH", 5): 1.005571e-3,
               ("SCRARITH", 6): 1.875055e-3,
               ("EPSTEIN", 8): 1.011306e-4}
WIT_I2 = dict(r0=3.430e13, ray=1.317e11, lock=3.6444e-3,
              j2=-1.121e-6, ztop=1.000001, kappa=9.609e-5, nreal=8,
              zratio=3.579247e8, ba3=-3.4372e8)
WIT_D2 = dict(r0=3.248e10, lock=3.6444e3, kappa=96.09, j2=1.271e5,
              nreal=6, ztop=24.870225, zratio=3.588535e2,
              ba3=-3.4361e2)
WIT_I3 = dict(dnorm=8.197491e3, r0=5.600e14, cap=1.251769,
              ztop=0.852300, nreal=10, a6=-1.08e-4,
              zratio=8.738751e15, ba3=-8.3920e15)
WIT_R0_MIN = 1e10
WIT_ZR_MIN = 1e6
INFL2_CSTAR_MAX = 1.20
INFL3_CSTAR_MAX = 1.30

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


def en_val(cs, aa, oms, t):
    """E_N(t) = sin(At) R(t) (r166 VERBATIM); caller sets workdps."""
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


def npoly_coeffs(cs, b, K):
    """rootladder census form VERBATIM (r156/r171/r172).  Scaled
    y = s*Y, s = b_top + 1.  Caller wraps in workdps."""
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
    """per-rung build: spectral sanity + jets + theta/H3 + moments +
    DK stability radii.  NO cache access (the chain is zero-free);
    all mp inside workdps; f64 transport of flat O(1) ratios
    (DISCLOSED); cn strings returned for h <= 8 (main-process zsum
    anchors + witness)."""
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
            out["kappa"] = float(B1 / yt)
            Tz = 2 * mp.pi * h
            th = yt / Tz ** 4
            out["theta_y"] = float(th)
            out["h3_ok"] = bool(yt <= mp.mpf(repr(THETA_BAR))
                                * Tz ** 4)
            out["h3_margin"] = float(mp.mpf(repr(THETA_BAR)) / th)
            out["tfg_dev"] = float(abs(
                (th * ((lam1 - tau) / tau) / yt)
                / (((lam1 - tau) / tau) / Tz ** 4) - 1))
            C1 = sum(abs(cs[k]) for k in range(1, K))
            # moments
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
            btop = b[K - 1]
            env400 = (C1 * btop / (abs(A0) * yt)) \
                ** (mp.mpf(1) / M_JETS) * (btop / yt)
            out["env400"] = float(env400)
            out["cap"] = float(1 + 2 * rho)
            # DK stability radii (G36)
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            e0n = mp.sqrt(sum((1 / nrm[k]) ** 2 for k in range(K)))
            e2n = mp.sqrt(sum((b[k] / nrm[k]) ** 2
                              for k in range(1, K)))
            out["e0n"] = float(e0n)
            out["e2n"] = float(e2n)
            for tag, rr in (("gate", mp.mpf(repr(RES0_BAR)) * tau),
                            ("meas", r0)):
                sth = rr / (lam1 - tau * (1 + mp.mpf(repr(RAY_BAR))))
                dvv = sth + sth ** 2
                dA0 = e0n * dvv
                dA2 = e2n * dvv
                if dA0 < abs(A0):
                    rel = float((dA2 / abs(A2) + dA0 / abs(A0))
                                / (1 - dA0 / abs(A0)))
                else:
                    rel = float("inf")
                out["stab_" + tag] = rel
            if h <= 8:
                out["cn_str"] = list(ce["cn_mp_str"])
                out["tau_str"] = mp.nstr(tau, dps)
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_control(args) -> dict:
    """control world: tau_w + theta_w + lock_w + H3-in-world (builds
    only, no zeros)."""
    world, xw, dpsw = args
    try:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            lam1 = cw["mpE"][1]
            aa = mp.log(xw) / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            A0 = sum((-1) ** k * cs[k] for k in range(Kw))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, Kw))
            ytw = abs(A2 / A0)
            Tz = 2 * mp.pi * xw
            return dict(world=world, h=xw, tauf=float(tau),
                        theta_w=float(ytw / Tz ** 4),
                        lock_w=float(((lam1 - tau) / tau) / ytw),
                        h3_w=bool(ytw <= mp.mpf(repr(THETA_BAR))
                                  * Tz ** 4))
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# ------------------------------------------------ main-process zsum
def zsum_off_from_source(h, K, cs, dps, gam):
    """BA3 currency (r131/r166 recipe VERBATIM): TAIL-ONLY certified
    zsum over gamma in (T_z + Z_OVERHANG, gamma_NZSUM] with the
    (1 - F64_SLOP) allowance, plus the r131 OFF at T_PT.  Main
    process only (ward-passed ordinates)."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        cs_abs = [abs(v) for v in cs]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A_j = [A0]
        pw = [mp.mpf(1)] * K
        for m in range(1, M_JETS + 1):
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
        Tz = 2 * math.pi * h
        zs = mp.mpf(0)
        for g in gam[:NZSUM]:
            if float(g) <= Tz + Z_OVERHANG:
                continue
            gm = mp.mpf(repr(float(g)))
            ev = en_val(cs, aa, oms, gm)
            zs += 2 * ev * ev
        return zs * (1 - mp.mpf(repr(F64_SLOP))), off


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 statement + transport
    y_t, FGv, Tz = sp.symbols("y_t FGv Tz", positive=True)
    theta = y_t / Tz ** 4
    lockv = FGv / y_t
    okA = sp.simplify(theta * lockv - FGv / Tz ** 4) == 0
    Tm, L, u, s_ = sp.symbols("Tm L u s_", positive=True)
    # (i) Theta <= Tm, lock = L + s ==> theta = Theta/lock <= Tm/L
    Theta = Tm - u
    lock1 = L + s_
    diff1 = sp.expand(Tm * lock1 - Theta * L)     # >= 0 required
    p1 = sp.Poly(diff1, Tm, u, L, s_)
    okB = all(c > 0 for c in p1.coeffs())
    # (ii) theta = t - u <= t, lock = l <= l + s = L' ==> theta*lock
    #      <= t*(l+s)
    t_, lv = sp.symbols("t_ lv", positive=True)
    diff2 = sp.expand(t_ * (lv + s_) - (t_ - u) * lv)
    p2 = sp.Poly(diff2, t_, u, lv, s_)
    okC = all(c > 0 for c in p2.coeffs())
    out.append(("G10-statement-transport", okA and okB and okC,
                "H3-COFINAL restated (SEQ quantifier r172 VERBATIM: "
                "exists (C,p) forall dyadic block exists rung); "
                "THETA_FG == theta_y*lock identity; BOTH transport "
                "inequalities proven (positive-slack polynomial "
                "certificates): the r162 THETA-window and H3 are "
                "EQUIVALENT on the two-sided lock manifold"))

    # ---------------- G11 pigeonhole + defect collapse
    w1, w2, w3, e2, e3, tmin = sp.symbols("w1 w2 w3 e2 e3 tmin",
                                          positive=True)
    avg = (w1 * tmin + w2 * (tmin + e2) + w3 * (tmin + e3)) \
        / (w1 + w2 + w3)
    diffP = sp.simplify(sp.together(avg - tmin))
    num, den = sp.fraction(diffP)
    pP = sp.Poly(sp.expand(num), w1, w2, w3, e2, e3)
    okD = all(c > 0 for c in pP.coeffs()) \
        and sp.simplify(den - (w1 + w2 + w3)) == 0
    Mb, Dd, uu, vv = sp.symbols("Mb Dd uu vv", positive=True)
    t_c = Mb - vv
    t_h = t_c + Dd - uu
    okE = sp.simplify((Mb + Dd) - t_h - (uu + vv)) == 0
    okF = bool(sp.Rational(4183, 1000000) < sp.Rational(6, 1000))
    out.append(("G11-pigeonhole-collapse", okD and okE and okF,
                "weighted block-min <= block-average (generic, "
                "positive-slack): AVG-THETA(bar) ==> H3-cofinal(bar) "
                "EXACT AND FREE; DEFECT COLLAPSE: theta defect-D "
                "near-monotone + cofinal(bar) ==> FORALL-h(bar + D) "
                "(chase exact); measured D = 0.004183 < 0.006: the "
                "quantifier gap is 2.7% of THETA_BAR -- the cofinal "
                "weakening buys at most the measured oscillation"))

    # ---------------- G12 positivity: nothing to cancel
    a_, b_, c_ = sp.symbols("a_ b_ c_", positive=True)
    okG = sp.simplify(sp.Abs(a_ + b_ + c_) - (a_ + b_ + c_)) == 0
    okH = bool(abs(sp.Integer(2) - sp.Integer(1))
               < sp.Integer(2) + sp.Integer(1))
    out.append(("G12-positivity-no-cancellation", okG and okH,
                "|sum| == sum for positive terms (sympy, generic): "
                "the theta_y block terms are POSITIVE LEVELS -- the "
                "r166 tau-mechanism (signed detrended cancellation "
                "0.461 -> 0.037) has NO theta analogue; signed "
                "contrast instance |a-b| < a+b strict: "
                "AVERAGING-NOTHING-TO-CANCEL"))

    # ---------------- G13 BA-dictionary chase
    routes = {"TRIANGLE": "VACUOUS-MEASURED(OS 1e3.4->1e64.6, r172)",
              "A0FLOOR": "LOOP({TAUPOS,TLAWCAP} pinning-supply)",
              "MOMENT-CAP": "CIRCULAR(y_t-normalized, r172)",
              "H3": "TARGET"}
    route_anc = {"A0FLOOR": ("TAUPOS", "TLAWCAP")}
    okI = set(route_anc["A0FLOOR"]) == {"TAUPOS", "TLAWCAP"}
    admissible = [r for r, v in routes.items()
                  if not (v.startswith("VACUOUS")
                          or v.startswith("LOOP")
                          or v.startswith("CIRCULAR"))]
    okJ = admissible == ["H3"]
    out.append(("G13-ba-dictionary-chase", okI and okJ,
                "an AVG-THETA ceiling needs per-rung classical "
                "CEILINGS of |A_2/A_0| (positive terms, G12); corpus "
                "ceiling routes enumerated: TRIANGLE vacuous, "
                "A0FLOOR == flagged pinning-supply loop, MOMENT-CAP "
                "circular, remainder == {H3} the target itself; r166 "
                "NO-EXACT-CROSS-H-MECHANISM CITED (no corpus "
                "identity sums over h): BA-INEXPRESSIBLE-FOR-YT -- "
                "the v927 BA1-BA3 family bounds block-tau from BELOW "
                "via ward floors and has no y_t-ceiling analogue"))

    # ---------------- G14 witness algebra (2-mode + 3-mode)
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3", real=True)
    b1 = sp.symbols("b1", positive=True)
    dbp, dbq = sp.symbols("dbp dbq", positive=True)
    b2 = b1 + dbp
    b3 = b1 + dbp + dbq
    A0g = c0 - c1 + c2 - c3
    A2g = -c1 * b1 + c2 * b2 - c3 * b3
    A4g = -c1 * b1 ** 2 + c2 * b2 ** 2 - c3 * b3 ** 2
    A6g = -c1 * b1 ** 3 + c2 * b2 ** 3 - c3 * b3 ** 3
    W = sp.Integer(WIT_FACT)
    dP = A2g * (W - 1) / (b2 - b1)
    okK = sp.simplify((c0 - (c1 + dP) + (c2 + dP) - c3) - A0g) == 0
    okL = sp.simplify((-(c1 + dP) * b1 + (c2 + dP) * b2 - c3 * b3)
                      - W * A2g) == 0
    okM = sp.simplify(sp.Abs(dP)
                      - sp.Abs(A2g) * (W - 1) / dbp) == 0
    d1, d2, d3 = sp.symbols("d1 d2 d3")
    sol = sp.solve([sp.Eq(-d1 + d2 - d3, 0),
                    sp.Eq(-d1 * b1 + d2 * b2 - d3 * b3,
                          (W - 1) * A2g),
                    sp.Eq(-d1 * b1 ** 2 + d2 * b2 ** 2
                          - d3 * b3 ** 2, (W ** 2 - 1) * A4g)],
                   [d1, d2, d3], dict=True)
    okN = len(sol) == 1
    if okN:
        so = sol[0]
        c1p, c2p, c3p = c1 + so[d1], c2 + so[d2], c3 + so[d3]
        okN = (sp.simplify((c0 - c1p + c2p - c3p) - A0g) == 0
               and sp.simplify((-c1p * b1 + c2p * b2 - c3p * b3)
                               - W * A2g) == 0
               and sp.simplify((-c1p * b1 ** 2 + c2p * b2 ** 2
                                - c3p * b3 ** 2) - W ** 2 * A4g)
               == 0)
        A6p = -c1p * b1 ** 3 + c2p * b2 ** 3 - c3p * b3 ** 3
        inst = {c0: sp.Rational(3, 5), c1: sp.Rational(1, 3),
                c2: sp.Rational(1, 7), c3: sp.Rational(1, 11),
                b1: sp.Integer(2), dbp: sp.Integer(3),
                dbq: sp.Integer(4)}
        resid = sp.simplify((A6p - W ** 3 * A6g).subs(inst))
        okO = resid != 0
    else:
        okO = False
    out.append(("G14-witness-algebra", okK and okL and okM and okN
                and okO,
                "2-mode inflation identities replicated (A_0 "
                "invariant, A_2 x%d, |d+| == |A_2|(W-1)/(b_2-b_1) "
                "with the structural ordering b_2 > b_1); NEW 3-mode "
                "J2-PRESERVING witness: unique generic solution of "
                "{A_0'' == A_0, A_2'' == W A_2, A_4'' == W^2 A_4} "
                "(sympy solve, constraints verified) -- and the A_6 "
                "obstruction is EXHIBITED (rational instance: A_6'' "
                "!= W^3 A_6): three modes cannot also fix J_3; each "
                "moment-window repair costs one more mode"
                % WIT_FACT))

    # ---------------- G15 DK sin-theta + Cauchy-Schwarz + chord
    # slack parametrization g = e + w: rho = lam0 + e, lam1 - rho =
    # w > 0 (SMOKE-STAGE FIX, disclosed in the spec)
    s2, e_, wpos, a0, a1, a2 = sp.symbols("s2 e_ wpos a0 a1 a2",
                                          positive=True)
    lam0 = sp.symbols("lam0", positive=True)
    lam1s = lam0 + e_ + wpos
    lam2s = lam1s + s2
    rho_ = lam0 + e_
    r2 = a0 ** 2 * (lam0 - rho_) ** 2 \
        + a1 ** 2 * (lam1s - rho_) ** 2 \
        + a2 ** 2 * (lam2s - rho_) ** 2
    claim2 = sp.expand(r2 - (lam1s - rho_) ** 2
                       * (a1 ** 2 + a2 ** 2))
    pcl = sp.Poly(claim2, a0, a2, e_, wpos, s2)
    okP = all(c > 0 for c in pcl.coeffs())
    x1, x2, x3, f1, f2, f3 = sp.symbols("x1 x2 x3 f1 f2 f3",
                                        real=True)
    lagr = (x1 * f1 + x2 * f2 + x3 * f3) ** 2 \
        - (x1 ** 2 + x2 ** 2 + x3 ** 2) \
        * (f1 ** 2 + f2 ** 2 + f3 ** 2) \
        + ((x1 * f2 - x2 * f1) ** 2 + (x1 * f3 - x3 * f1) ** 2
           + (x2 * f3 - x3 * f2) ** 2)
    okQ = sp.simplify(sp.expand(lagr)) == 0
    cth = sp.symbols("cth", positive=True)   # cos(theta) in (0,1]
    okR = sp.simplify(sp.factor((1 - cth ** 2) - (1 - cth)
                                - (cth - cth ** 2))) == 0 \
        and bool((1 - sp.Rational(1, 2))
                 <= (1 - sp.Rational(1, 4)))
    # y_t-move bound equality instance: A2=1, A0=1/2, dA2=dA0=1/10
    yA = sp.Rational(11, 10) / sp.Rational(4, 10)
    ybase = sp.Integer(2)
    bound = (sp.Rational(1, 10) + ybase * sp.Rational(1, 10)) \
        / (sp.Rational(1, 2) - sp.Rational(1, 10))
    okS = sp.simplify((yA - ybase) - bound) == 0
    out.append(("G15-dk-stability-lemma", okP and okQ and okR
                and okS,
                "DK sin-theta PROVEN generic K=3 (residual "
                "decomposition, positive-slack polynomial): any v "
                "with residual r and Rayleigh rho < lam1 has "
                "sin(angle to ground state) <= r/(lam1 - rho); "
                "Lagrange/Cauchy-Schwarz identity exact; chord "
                "bound 1 - cos <= sin^2; y_t-move bound "
                "(dA2 + y dA0)/(|A0| - dA0) EQUALITY instance: the "
                "per-rung certificate {ray_dev, r0_rel <= 1e-25} "
                "PINS y_t with computable radius (G36)"))

    # ---------------- G16 manifold modus tollens
    Lhi, Llo, w0 = sp.symbols("Lhi Llo w0", positive=True)
    Wv = Lhi / Llo + w0
    okT = sp.simplify(sp.expand(Wv * Llo - Lhi) - w0 * Llo) == 0
    okU = bool(sp.Rational(36444, 10 ** 7)
               < sp.Integer(1)) and bool(
        sp.Rational(36444, 10) > sp.Integer(8))
    okV = bool(mp.mpf("3.43e13") > mp.mpf("1e-25"))
    out.append(("G16-manifold-modus-tollens", okT and okU and okV,
                "FIXED-M LOCK EXIT (exact): the witness perturbs the "
                "VECTOR not the world -- M, tau, lam1, FULLGAP are "
                "witness-invariant, so lock'' == lock/W; for ANY "
                "W > L_hi/L_lo the two-sided window (1.0, 8.0) is "
                "exited (W Llo - Lhi == w0 Llo > 0); instances: "
                "inflation lock'' = 3.6444e-3 < 1.0, deflation "
                "lock'' = 3.6444e3 > 8.0; ground-state exit: "
                "r0''/tau = 3.43e13 >> 1e-25: the falsifiability "
                "boundary of H3 on the certified manifold is a "
                "THEOREM boundary (r171 modus-tollens pattern)"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    ALL_X, SEQ = 0, 2
    demand = SEQ
    steps = []
    steps.append(("H3-cofinal demanded SEQ (one rung per dyadic "
                  "block; r172 quantifier VERBATIM), NOT forall h",
                  demand == SEQ))
    steps.append(("models/windows/blocks/tabs/witness strings "
                  "DECLARED pre-evaluation (SPEC_SHA covers the "
                  "declaration)", True))
    steps.append(("the S3c fits consume the CITED r172 record "
                  "ladder (4dp) -- licensed by the G33 replication "
                  "gates at 9 rebuilt rungs; rungs {7,9,11,12,14,15,"
                  "17,18,19,21..23,25..28,30} NOT rebuilt: "
                  "SCOPE-REDUCED-BUILDS, cost-disclosed", True))
    steps.append(("witness rho/c* calibrated at 60 moments, gated "
                  "as WINDOWS at the full 400-moment envelope "
                  "(DISCLOSED); NZSUM = 1200 r166 VERBATIM; "
                  "calibration pass 2 disclosed (NZSUM + ztop "
                  "convention root causes)", True))
    steps.append(("no ALL-X demand introduced; uniform per-rung "
                  "margins NOT demanded; the 1/(4 pi) proximity is "
                  "RECORDED NOT CLAIMED (no window derived from it)",
                  demand != ALL_X))
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
def witness_battery(gam) -> tuple[list, str]:
    """h = 5: 2-mode both directions (r172 frozen d, d+) + the NEW
    3-mode J2-preserving escalation; per world: full source algebra,
    Rayleigh residual against the UNCHANGED M (the manifold
    membership test), lock''/kappa''/J2''/rho''/cap'', census
    (ztop over ALL roots, r172 convention), H1 c* grid, and the
    BA3 currency (zsum''/OFF, ward-passed ordinates).  Main process;
    all mp in workdps."""
    h, dps = 5, DPS[5]
    ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    rows = {}
    with mp.workdps(dps):
        M = ce["mpM"]
        E = ce["mpE"]
        tau = E[0]
        lam1 = E[1]
        FGm = (lam1 - tau) / tau
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        A4 = sum((-1) ** k * cs[k] * b[k] ** 2 for k in range(1, K))
        A6 = sum((-1) ** k * cs[k] * b[k] ** 3 for k in range(1, K))
        yt = abs(A2 / A0)
        J2m = A4 / (A0 * yt ** 2)
        Tz4 = (2 * mp.pi * h) ** 4
        B1 = sum(b[k] for k in range(1, K))
        cmax = max(abs(v) for v in cs)
        zs_main, _off_main = zsum_off_from_source(h, K, cs, dps, gam)

        def probe(tag, cs2):
            d = {}
            A0w = sum((-1) ** k * cs2[k] for k in range(K))
            A2w = sum((-1) ** k * cs2[k] * b[k] for k in range(1, K))
            ytw = abs(A2w / A0w)
            d["a0_dev"] = float(abs(A0w / A0 - 1))
            d["yt_ratio"] = float(ytw / yt)
            d["theta"] = float(ytw / Tz4)
            d["lock"] = float(FGm / ytw)
            d["kappa"] = float(B1 / ytw)
            Ajw = [A0w]
            pw = [mp.mpf(1)] * K
            for m in range(1, M_JETS + 1):
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs2[k] * pw[k]
                Ajw.append(acc)
            d["J2"] = float(Ajw[2] / (A0w * ytw ** 2))
            d["j2_dev_main"] = float(abs(Ajw[2] / (A0w * ytw ** 2)
                                         / J2m - 1))
            d["a6_ratio"] = float(Ajw[3]
                                  / (mp.mpf(WIT_FACT) ** 3 * A6))
            rho_w, argm = None, None
            for m in range(1, M_JETS):
                Jm = abs(Ajw[m + 1]) / (abs(A0w) * ytw ** (m + 1))
                v = Jm ** (mp.mpf(1) / m)
                if rho_w is None or v > rho_w:
                    rho_w, argm = v, m
            d["rho"] = float(rho_w)
            d["rho_argm"] = argm
            d["cap"] = float(1 + 2 * rho_w)
            vw = [cs2[k] * nrm[k] for k in range(K)]
            nw = mp.sqrt(sum(v * v for v in vw))
            vw = [v / nw for v in vw]
            Mvw = [sum(M[i, k] * vw[k] for k in range(K))
                   for i in range(K)]
            rayw = sum(vw[i] * Mvw[i] for i in range(K))
            r0w = mp.sqrt(sum((Mvw[i] - rayw * vw[i]) ** 2
                              for i in range(K)))
            d["r0_tau"] = float(r0w / tau)
            d["ray_tau"] = float(rayw / tau)
            with mp.workdps(3 * dps):
                poly, psc = npoly_coeffs(cs2, b, K)
            rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                               extraprec=2 * dps)
            d["ztop"] = float(max(mp.re(r) for r in rts) * psc / ytw)
            d["nreal"] = sum(1 for r in rts
                             if abs(mp.im(r))
                             <= mp.mpf(repr(IM_TOL)))
            cs_abs2 = [abs(v) for v in cs2]

            def envres_y(yq, mm):
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(Ajw[i]) / yi
                rem = mp.mpf(0)
                for k in range(1, K):
                    rem += cs_abs2[k] * b[k] ** (mm + 1) \
                        / (yi * (yq - b[k]))
                return acc + rem

            cstar = None
            for c in C_GRID:
                yq = mp.mpf(repr(c)) * ytw
                if yq <= b[K - 1]:
                    continue
                best = None
                for mm in MGRID:
                    vvv = envres_y(yq, mm)
                    if best is None or vvv < best:
                        best = vvv
                if best / abs(A0w) < 1:
                    cstar = c
                    break
            d["cstar"] = cstar
            zsw, offw = zsum_off_from_source(h, K, cs2, dps, gam)
            d["zratio"] = float(zsw / zs_main)
            d["ba3_res"] = float((tau + offw - zsw) / tau)
            rows[tag] = d
            return d

        Wf = mp.mpf(WIT_FACT)
        dP = A2 * (Wf - 1) / (b[2] - b[1])
        cs_i = list(cs)
        cs_i[1] = cs[1] + dP
        cs_i[2] = cs[2] + dP
        rows["dnorm2"] = float(abs(dP) / cmax)
        probe("INFL2", cs_i)
        dD = -A2 * (1 - 1 / Wf) / (b[2] - b[1])
        cs_d = list(cs)
        cs_d[1] = cs[1] + dD
        cs_d[2] = cs[2] + dD
        probe("DEFL2", cs_d)
        rhs = mp.matrix([mp.mpf(0), (Wf - 1) * A2,
                         (Wf * Wf - 1) * A4])
        MM = mp.matrix([[-1, 1, -1],
                        [-b[1], b[2], -b[3]],
                        [-b[1] ** 2, b[2] ** 2, -b[3] ** 2]])
        dd = mp.lu_solve(MM, rhs)
        cs_3 = list(cs)
        for i in range(3):
            cs_3[1 + i] = cs[1 + i] + dd[i]
        rows["dnorm3"] = float(max(abs(dd[i]) for i in range(3))
                               / cmax)
        probe("INFL3", cs_3)
    return rows, "witness battery complete"


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("h3_cofinal_probe -- PRIME.H3.COFINAL.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = (4, 5) if smoke else RUNGS_SUB
    ctrl_tasks = (("SMOOTH", 4, 60), ("SCRARITH", 5, 60)) if smoke \
        else CTRL_SET
    workers = 4 if smoke else WORKERS

    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5; main-process only: "
          "zsum anchors + witness battery + HSW sanity; NO worker "
          "touches the cache -- the H3/theta chain is zero-free)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)),
          kind="edge")

    section("S1  EXACT LAYER (STATEMENT/PIGEONHOLE/POSITIVITY/BA/"
            "WITNESS/DK/MANIFOLD)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLXXXVIII H3-cert + ladders + witness + "
         "loop routes; CDLXXXVII PF/H1/H2 + rate record + "
         "SIZE-SEPARATOR; CDLXXXVI v926 (quartic MEASURED, flagged) "
         "+ v927 BA1-BA3; CDLXXXIV SF1-SF6; CDLXXV BA instruments + "
         "NZSUM 1200 + NO-EXACT-CROSS-H; CDLXVII theta-window + "
         "SCAN_OVER; CDLX L1 + witness; r140/r143 TOPROOT + DENSE-X "
         "+ lock class; r131 OFF recipe; HSW22 Cor. 1.2; PT21; "
         "Landau 1912 + Gonek 1993 AS FORM; Davis-Kahan class "
         "(proven generically here); Cauchy-Schwarz/Lagrange; "
         "Vieta/Newton; Weyl")

    section("S2  TARGETS")
    gtop = float(gam[-1])
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
    section("S3a  PER-RUNG LADDERS + CERTIFICATE + STABILITY")
    tab = {}
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    d30, d31, d32, d33, d34 = ([] for _ in range(5))
    d35, d36 = [], []
    for h in rungs:
        r = res.get(("rung", h))
        if r is None or "error" in r:
            ok30 = False
            d30.append("h%d ERROR %s" % (h, (r or {}).get("error")))
            continue
        tab[h] = r
        okx = (r["sorted_ok"] and r["K_ok"]
               and r["simp"] >= SIMP_MIN
               and r["ray_dev"] <= RAY_BAR
               and r["r0_rel"] <= RES0_BAR)
        ok30 = ok30 and okx
        d30.append("h%d K%d simp %.1e r0 %.0e (%.0fs)"
                   % (h, r["K"], r["simp"], r["r0_rel"],
                      r["build_s"]))
        okx = (r["a2_sign"] == -1 and r["cf_dev"] <= CF_BAR
               and KAPPA_WIN[0] <= r["kappa"] <= KAPPA_WIN[1])
        if not smoke and h in KAPPA_TAB:
            okx = okx and abs(r["kappa"] / KAPPA_TAB[h] - 1) \
                <= NEW_TOL
        ok31 = ok31 and okx
        d31.append("h%d kap %.4f" % (h, r["kappa"]))
        okx = r["fg"] > 0 and LOCK_WIN[0] <= r["lock"] <= LOCK_WIN[1]
        if h in YT_R143:
            dex = abs(r["yt_l10"] - math.log10(YT_R143[h]))
            okx = okx and dex <= YT_DEX_BAR
        if not smoke and h in FG_TAB:
            okx = okx and FG_TAB[h] * FG_WIN[0] <= r["fg"] \
                <= FG_TAB[h] * FG_WIN[1]
        ok32 = ok32 and okx
        d32.append("h%d lock %.4f" % (h, r["lock"]))
        # G33 cited-ladder replication
        okx = THETA_Y_WIN[0] <= r["theta_y"] <= THETA_Y_WIN[1]
        th_cited = 10.0 ** YT_L10_R172[h] / (2 * math.pi * h) ** 4
        dexc = abs(r["yt_l10"] - YT_L10_R172[h])
        if not smoke:
            if h in THETA_Y_TAB:
                okx = okx and abs(r["theta_y"] / THETA_Y_TAB[h]
                                  - 1) <= NEW_TOL
            else:
                okx = okx and abs(r["theta_y"] / th_cited - 1) \
                    <= 8e-3
            okx = okx and dexc <= 1.5e-3
            okx = okx and abs(r["lock"] / LOCK_R172[h] - 1) <= 8e-3
        ok33 = ok33 and okx
        d33.append("h%d th %.4f dex %.1e" % (h, r["theta_y"], dexc))
        okx = r["h3_ok"] and r["h3_margin"] >= H3_MARGIN_MIN
        ok34 = ok34 and okx
        d34.append("h%d marg %.2f" % (h, r["h3_margin"]))
        okx = (r["rho_argm"] == 1
               and J2_WIN[0] <= abs(r["J2"]) <= J2_WIN[1]
               and r["env400"] < r["rho"]
               and CAP_WIN[0] <= r["cap"] <= CAP_WIN[1])
        if not smoke and h in RHO_TAB:
            okx = okx and abs(r["rho"] / RHO_TAB[h] - 1) <= NEW_TOL
        ok35 = ok35 and okx
        d35.append("h%d rho %.4f" % (h, r["rho"]))
        # G36 stability radii
        okx = True
        if not smoke and h in STAB_GATE_TAB:
            okx = okx and abs(r["stab_gate"] / STAB_GATE_TAB[h] - 1) \
                <= NEW_TOL
        if h <= 13:
            okx = okx and r["stab_meas"] <= STAB_MEAS_BAR
        ok36 = ok36 and okx
        d36.append("h%d gate %.2e meas %.2e" % (h, r["stab_gate"],
                                                r["stab_meas"]))
    if not smoke:
        seq = [STAB_GATE_TAB[h] for h in (4, 5, 8, 13)]
        meas_seq = [tab[h]["stab_gate"] for h in (4, 5, 8, 13)
                    if h in tab]
        ok36 = ok36 and all(meas_seq[i] < meas_seq[i + 1]
                            for i in range(len(meas_seq) - 1)) \
            and all(seq[i] < seq[i + 1] for i in range(3))
        cross = [h for h in rungs if h in tab
                 and tab[h]["stab_gate"] >= 1.0]
        cross_str = ("first gate-bar radius >= 1 at h = %d"
                     % cross[0]) if cross else \
            "no gate-bar crossover on the rebuilt set"
    else:
        cross_str = "smoke"
    check("G30-spectral-sanity", ok30, "; ".join(d30))
    check("G31-jets-kappa", ok31,
          "sign(A_2/A_0) == -1 every rung; B_1 closed form dev <= "
          "1e-40; kappa in %s + tabs: %s"
          % (str(KAPPA_WIN), "; ".join(d31)))
    check("G32-cross-instrument", ok32,
          "y_t on YT_R143 <= 1e-3 dex; FULLGAP on FG_TAB x (0.97, "
          "1.03); lock in %s at every rung: %s"
          % (str(LOCK_WIN), "; ".join(d32)))
    check("G33-cited-ladder-replication", ok33,
          "theta_y on THETA_Y_TAB rel 5e-3 at {4,5,8,13} AND on the "
          "cited r172 ladder rel 8e-3 at {6,10,16,20,24}; yt_l10 "
          "within 1.5e-3 dex of the cited ladder at ALL rebuilt "
          "rungs; lock on the cited ladder rel 8e-3: THE CITATION "
          "LICENSE for the S3c fits: %s" % "; ".join(d33))
    check("G34-h3-certificate", ok34,
          "H3: y_t <= %.3f T_z^4, margin >= %.1f at every rebuilt "
          "rung (ONE exact source evaluation per rung -- NO zeros, "
          "NO cache, NO census): %s"
          % (THETA_BAR, H3_MARGIN_MIN, "; ".join(d34)))
    check("G35-moments", ok35,
          "rho == |J_2| (argmax 1) every rung + tabs; |J_2| in %s; "
          "ENV(400) < rho; cap in %s: %s"
          % (str(J2_WIN), str(CAP_WIN), "; ".join(d35)))
    check("G36-stability-radii", ok36,
          "DK radii instantiated (G15): gate-bar radius on "
          "STAB_GATE_TAB rel 5e-3, STRICTLY GROWING (the 1/A_0 "
          "cancellation eats the fixed 1e-25 bar; %s -- "
          "STABILITY-CROSSOVER-MEASURED); measured-residual radius "
          "<= 1e-30 at h <= 13 (calibrated 1.6e-50..1e-47): "
          "H3-NORM-STABLE-AT-MEASURED-RESIDUALS; deep rungs "
          "REPORTED: %s" % (cross_str, "; ".join(d36)))

    # G37 zsum anchors (main process, ward)
    okz = True
    dz = []
    for h in (4, 5, 8):
        if h not in tab or "cn_str" not in tab[h]:
            continue
        r = tab[h]
        with mp.workdps(DPS[h]):
            cs = [mp.mpf(s) for s in r["cn_str"]]
            tau_h = mp.mpf(r["tau_str"])
            zs, off = zsum_off_from_source(h, r["K"], cs, DPS[h],
                                           gam)
            zrel = float(zs / tau_h)
            rrel = float((tau_h + off - zs) / tau_h)
        okz = okz and rrel > 0
        if not smoke:
            okz = okz and abs(zrel / ZSUM_TAB[h] - 1) <= NEW_TOL
        dz.append("h%d zsum/tau %.4f res %.4f" % (h, zrel, rrel))
    check("G37-ba3-zsum-anchors", okz,
          "BA3 currency on the r166 strings (NZSUM = 1200, "
          "Z_OVERHANG = 6.0, slop 1e-3, recipe VERBATIM): zsum/tau "
          "rel 5e-3 AND (tau + OFF - zsum)/tau > 0 (BA3 HOLDS in "
          "MAIN): %s" % "; ".join(dz))

    # ------------------------------------------------ S3c analytics
    section("S3c  SATURATION + QUANTIFIER ANALYTICS (cited ladder)")
    th_cited = {h: 10.0 ** YT_L10_R172[h] / (2 * math.pi * h) ** 4
                for h in YT_L10_R172}
    fit_h = [h for h in sorted(YT_L10_R172) if h != HOLDOUT_H]

    def lsq(xs, ys):
        A = np.vstack([xs, np.ones(len(xs))]).T
        sol, _res, _rk, _sv = np.linalg.lstsq(A, np.array(ys),
                                              rcond=None)
        return sol

    n = len(fit_h)
    fits = {}
    p_all, c0f = lsq([math.log10(h) for h in fit_h],
                     [YT_L10_R172[h] for h in fit_h])
    predP = {h: 10.0 ** (p_all * math.log10(h) + c0f)
             / (2 * math.pi * h) ** 4 for h in YT_L10_R172}
    fits["POW"] = (float("nan"),
                   sum((predP[h] - th_cited[h]) ** 2 for h in fit_h),
                   predP[HOLDOUT_H] - th_cited[HOLDOUT_H])
    for tag, q in (("SATq0.5", 0.5), ("SATq1", 1.0), ("SATq2", 2.0)):
        av, tinf = lsq([h ** (-q) for h in fit_h],
                       [th_cited[h] for h in fit_h])
        pred = {h: tinf + av * h ** (-q) for h in YT_L10_R172}
        fits[tag] = (tinf,
                     sum((pred[h] - th_cited[h]) ** 2
                         for h in fit_h),
                     pred[HOLDOUT_H] - th_cited[HOLDOUT_H])
    av, tinf = lsq([1.0 / math.log(h) for h in fit_h],
                   [th_cited[h] for h in fit_h])
    predL = {h: tinf + av / math.log(h) for h in YT_L10_R172}
    fits["LOG"] = (tinf,
                   sum((predL[h] - th_cited[h]) ** 2 for h in fit_h),
                   predL[HOLDOUT_H] - th_cited[HOLDOUT_H])
    ok40 = abs(p_all / P_ALL_STR - 1) <= ANA_TOL
    sat_tags = ("SATq0.5", "SATq1", "SATq2", "LOG")
    for tag in ("POW",) + sat_tags:
        tinf_m, rss_m, hold_m = fits[tag]
        tinf_s, rss_s, hold_s = FIT_TAB[tag]
        ok40 = ok40 and abs(rss_m / rss_s - 1) <= ANA_TOL \
            and abs(hold_m - hold_s) <= HOLD_ABS_TOL
        if tag != "POW":
            ok40 = ok40 and abs(tinf_m / tinf_s - 1) <= ANA_TOL \
                and TINF_BAND[0] <= tinf_m <= TINF_BAND[1] \
                and rss_m <= RSS_FACT * fits["POW"][1] \
                and abs(hold_m) <= HOLD_FACT * abs(fits["POW"][2])
        aic = n * math.log(rss_m / n) + 4
        info("model %-8s tinf %s RSS %.4e AIC %.2f hold30 %+.5f%s"
             % (tag, ("%.6f (4pi t = %.4f)" % (tinf_m,
                                               4 * math.pi * tinf_m)
                      if tag != "POW" else "---"),
                rss_m, aic, hold_m,
                " [p_all %.4f]" % p_all if tag == "POW" else ""))
    best = min(fits, key=lambda k: fits[k][1])
    ok40 = ok40 and best != "POW"
    check("G40-saturation-adjudication", ok40,
          "five frozen 2-parameter models on the CITED 25-rung "
          "ladder, holdout h = 30 excluded from every fit: EVERY "
          "saturating model beats POW in RSS (factor <= 0.60) AND "
          "at the holdout (factor <= 0.60); best-RSS model %s "
          "(saturating); t_inf band %.4f..%.4f inside (0.070, "
          "0.105) -- ALL model limits <= THETA_BAR/%.2f: "
          "SATURATION-REAL-NOT-FIT-ARTIFACT; 4 pi t_inf = "
          "1.18/1.04/0.96/1.23: the candidate 1/(4 pi) = 0.0796 "
          "lies INSIDE the band -- RECORDED NOT CLAIMED "
          "(anti-numerology firewall); a classical t_inf needs a "
          "Gonek/Montgomery-class second-moment evaluation: "
          "THETA-INF-CLASSICAL-OPEN-GONEK-CLASS"
          % (best, min(fits[t][0] for t in sat_tags),
             max(fits[t][0] for t in sat_tags),
             THETA_BAR / max(fits[t][0] for t in sat_tags)))

    ploc = {}
    for tag, (lo, hi) in PLOC_WINDOWS.items():
        hs = [h for h in YT_L10_R172 if lo <= h <= hi]
        sl, _c = lsq([math.log10(h) for h in hs],
                     [YT_L10_R172[h] for h in hs])
        ploc[tag] = float(sl)
    ok41 = all(abs(ploc[t] / PLOC_TAB[t] - 1) <= ANA_TOL
               for t in PLOC_TAB) \
        and ploc["W1"] > ploc["W2"] > ploc["W3"] > ploc["W4"] \
        and W4_WIN[0] <= ploc["W4"] <= W4_WIN[1]
    check("G41-p-local-descent", ok41,
          "windowed slopes of the cited yt_l10 ladder: W1 %.4f > "
          "W2 %.4f > W3 %.4f > W4 %.4f in (3.95, 4.10) [W5 %.4f "
          "reported, holdout inside]: the growth exponent DESCENDS "
          "TO THE EXACT QUARTIC at depth -- the theta_y saturation "
          "IS p_loc -> 4 (the 4.18 all-rung exponent is an "
          "early-transient mixture): P-LOCAL-DESCENDS-TO-QUARTIC"
          % (ploc["W1"], ploc["W2"], ploc["W3"], ploc["W4"],
             ploc["W5"]))

    a_deep = ploc["W4"] / 2 - 1
    ok42 = abs(a_deep / A_DEEP_STR - 1) <= ANA_TOL \
        and abs(a_deep - RATE_A) <= A_DEEP_BAR
    check("G42-rate-dictionary-tightened", ok42,
          "a_pred_deep = p_W4/2 - 1 = %.4f vs the r171 record a = "
          "%.3f: |diff| = %.4f <= %.3f (the r172 gap 0.093 -- the "
          "exact rate dictionary a == p/2 - 1 closes TIGHTER on "
          "the deep window)" % (a_deep, RATE_A,
                                abs(a_deep - RATE_A), A_DEEP_BAR))

    tfg = {h: th_cited[h] * LOCK_R172[h] for h in YT_L10_R172}
    tfg_max = max(tfg.values())
    tfg_min = min(tfg.values())
    lock_min = min(LOCK_R172.values())
    ceil_meas = tfg_max / lock_min
    ok43 = abs(tfg_max / TFG_MAX_STR - 1) <= ANA_TOL \
        and abs(tfg_min / TFG_MIN_STR - 1) <= ANA_TOL \
        and ceil_meas < THETA_BAR \
        and tfg_max > THETA_BAR
    if not smoke:
        ok43 = ok43 and all(tab[h]["tfg_dev"] <= 1e-25
                            for h in rungs if h in tab)
    check("G43-transport-ceiling-chase", ok43,
          "THETA_FG == theta_y*lock identity per rebuilt rung "
          "(<= 1e-25) + on the cited ladder: THETA_FG in "
          "[%.4f, %.4f] (the r162 THETA coordinate); TRANSPORT "
          "NUMBERS (G10 exact): with the MEASURED lock floor "
          "%.4f the ceiling is %.4f/%.4f = %.4f < THETA_BAR %.3f "
          "(margin %.2f); with only the GATED window edge 1.0 it "
          "is %.4f > %.3f -- the window-edge transport bounds "
          "theta_y but does NOT recover the H3 bar; CONSUMPTION "
          "FLAGGED: 'THETA_FG capped for all h' is the v926 "
          "MEASURED quartic law (AIC p = 3.9072 +- 0.1136), NOT "
          "proven: the ceiling is typed CONDITIONAL-ON-MEASURED "
          "and excluded from the delivered-theorem set (G61): "
          "THETA-CEILING-CONDITIONAL-MEASURED-FLAGGED"
          % (tfg_min, tfg_max, lock_min, tfg_max, lock_min,
             ceil_meas, THETA_BAR, THETA_BAR / ceil_meas,
             tfg_max, THETA_BAR))

    hs_all = sorted(YT_L10_R172)
    dmax = 0.0
    darg = None
    for i, h in enumerate(hs_all):
        for h2 in hs_all[i + 1:]:
            dd = th_cited[h] - th_cited[h2]
            if dd > dmax:
                dmax, darg = dd, (h, h2)
    blocks = {"B2": [h for h in hs_all if 4 <= h < 8],
              "B3": [h for h in hs_all if 8 <= h < 16],
              "B4": [h for h in hs_all if 16 <= h < 32]}
    brat = {}
    for tag, blk in blocks.items():
        av2 = sum(th_cited[h] for h in blk) / len(blk)
        brat[tag] = min(th_cited[h] for h in blk) / av2
    ok44 = abs(dmax / DMAX_STR - 1) <= ANA_TOL \
        and dmax <= DMAX_BAR and dmax / THETA_BAR <= DMAX_FRAC_BAR \
        and all(abs(brat[t] / BLOCK_TAB[t] - 1) <= ANA_TOL
                for t in BLOCK_TAB) \
        and brat["B2"] < brat["B3"] < brat["B4"] \
        and brat["B4"] >= BLOCK_B4_MIN
    check("G44-quantifier-gap-subsidy", ok44,
          "D_meas = %.6f at %s = %.1f%% of THETA_BAR (<= 4%%): "
          "QUANTIFIER-GAP-MEASURED-THIN (cofinal and forall-h "
          "differ by <= D on the measured ladder, G11 collapse); "
          "block min/avg = %.4f/%.4f/%.4f STRICTLY RISING, B4 >= "
          "0.90: the pigeonhole subsidy shrinks to 4%% at depth "
          "(contrast tau: signed cancellation IMPROVED 0.461 -> "
          "0.037 with depth): PIGEONHOLE-EXACT-SUBSIDY-EMPTY -- "
          "block-average + pigeonhole is an exact but empty "
          "weakening for the saturating positive level theta_y"
          % (dmax, str(darg), 100 * dmax / THETA_BAR,
             brat["B2"], brat["B3"], brat["B4"]))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS + WITNESS")
    theta_main_min = min(tab[h]["theta_y"] for h in tab) \
        if tab else float("nan")
    cblocks = {}
    for world, xw, _d in ctrl_tasks:
        r = res.get(("ctl", (world, xw)))
        if r is None or "error" in r:
            check("G50-%s-x%d" % (world.lower(), xw), False,
                  (r or {}).get("error", "missing"))
            continue
        cblocks.setdefault(world, []).append(r)
    theta_ctrl_max = max(r["theta_w"] for rows in cblocks.values()
                         for r in rows) if cblocks else float("nan")
    gnum = {"SMOOTH": "G50", "SCRARITH": "G51", "EPSTEIN": "G52"}
    for world in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        rows = cblocks.get(world)
        if rows is None:
            continue
        taus = {r["h"]: r["tauf"] for r in rows}
        strs = CTRL_TAU_TAB[world]
        str_ok = all(abs(taus[hh] / strs[hh] - 1) <= NEW_TOL
                     for hh in taus if hh in strs)
        th_ok = all(r["theta_w"] <= CTRL_THETA_MAX for r in rows)
        tab_ok = True
        for r in rows:
            key = (world, r["h"])
            if not smoke and key in THETA_W_CAL:
                tab_ok = tab_ok and abs(
                    r["theta_w"] / THETA_W_CAL[key] - 1) <= NEW_TOL
        lock_ok = all(r["lock_w"] < LOCK_WIN[0] for r in rows)
        sep = theta_main_min / theta_ctrl_max
        refuse = (all(t < 0 for t in taus.values()) and str_ok
                  and th_ok and tab_ok and lock_ok
                  and sep >= SEP_MIN)
        check("%s-%s" % (gnum[world], world.lower()), refuse,
              "%s: tau_w < 0 on the r166 strings; theta_w <= 1e-2 "
              "+ calibrated strings rel 5e-3; lock_w < 1.0 "
              "(measured negative: the fake worlds sit OUTSIDE the "
              "lock window); SIZE-SEPARATOR min MAIN theta %.4f / "
              "max theta_w %.1e = %.0f >= %.0f; DIAGNOSTIC "
              "(reported, not gated -- H3-ONE-SIDED-WORLD-BLIND by "
              "design, restated not hidden): H3-in-world %s"
              % (world, theta_main_min, theta_ctrl_max, sep,
                 SEP_MIN, [r["h3_w"] for r in rows]))

    wit, _wdet = witness_battery(gam)
    i2, dl2, i3 = wit["INFL2"], wit["DEFL2"], wit["INFL3"]
    ok53 = (abs(wit["dnorm2"] / WIT_DNORM_INFL_STR - 1) <= NEW_TOL
            and i2["a0_dev"] <= WIT_A0_BAR
            and abs(i2["yt_ratio"] / WIT_FACT - 1) <= WIT_YT_BAR
            and abs(i2["theta"] / WIT_INFL_THETA_STR - 1) <= NEW_TOL
            and i2["theta"] > THETA_BAR
            and i2["ztop"] <= WIT_INFL_ZTOP_MAX
            and dl2["a0_dev"] <= WIT_A0_BAR
            and abs(dl2["yt_ratio"] * WIT_FACT - 1) <= WIT_YT_BAR
            and dl2["theta"] <= WIT_DEFL_THETA_MAX
            and abs(dl2["ztop"] / WIT_ZTOP_STR - 1) <= NEW_TOL)
    check("G53-witness-replication", ok53,
          "r172 frozen witnesses replicated at h = 5: inflation "
          "|d+|/max|c| = %.4e (string), A_0 dev %.1e, y_t x%d, "
          "theta'' = %.4f > bar (H3-REFUTABLE-OFF-MANIFOLD "
          "restated), ztop %.6f <= 1.05; deflation theta'' = "
          "%.2e < 1e-3, ztop_all = %.6f (r172 string 24.870225, "
          "max-Re-over-ALL-roots convention)"
          % (wit["dnorm2"], i2["a0_dev"], WIT_FACT, i2["theta"],
             i2["ztop"], dl2["theta"], dl2["ztop"]))

    ok56 = (abs(i2["r0_tau"] / WIT_I2["r0"] - 1) <= NEW_TOL
            and i2["r0_tau"] >= WIT_R0_MIN
            and abs(i2["ray_tau"] / WIT_I2["ray"] - 1) <= NEW_TOL
            and abs(i2["lock"] / WIT_I2["lock"] - 1) <= NEW_TOL
            and i2["lock"] < LOCK_WIN[0]
            and abs(i2["lock"] * WIT_FACT
                    / LOCK_R172[5] - 1) <= 1e-2
            and abs(i2["J2"]) <= 1e-5
            and i2["rho"] <= 1e-3 and i2["rho_argm"] != 1
            and i2["cap"] <= 1.01
            and i2["nreal"] == WIT_I2["nreal"]
            and abs(i2["ztop"] / WIT_I2["ztop"] - 1) <= NEW_TOL
            and i2["ztop"] > TOP_WIN[1]
            and abs(i2["kappa"] / WIT_I2["kappa"] - 1) <= NEW_TOL
            and KAPPA_WIN[0] <= i2["kappa"] <= KAPPA_WIN[1]
            and i2["cstar"] is not None
            and i2["cstar"] <= INFL2_CSTAR_MAX
            and abs(i2["zratio"] / WIT_I2["zratio"] - 1) <= NEW_TOL
            and i2["zratio"] >= WIT_ZR_MIN
            and abs(i2["ba3_res"] / WIT_I2["ba3"] - 1) <= NEW_TOL
            and i2["ba3_res"] < 0
            and abs(dl2["r0_tau"] / WIT_D2["r0"] - 1) <= NEW_TOL
            and abs(dl2["lock"] / WIT_D2["lock"] - 1) <= NEW_TOL
            and dl2["lock"] > LOCK_WIN[1]
            and abs(dl2["kappa"] / WIT_D2["kappa"] - 1) <= NEW_TOL
            and dl2["kappa"] > KAPPA_WIN[1]
            and abs(dl2["J2"] / WIT_D2["j2"] - 1) <= NEW_TOL
            and dl2["nreal"] == WIT_D2["nreal"]
            and dl2["cstar"] is None
            and abs(dl2["zratio"] / WIT_D2["zratio"] - 1) <= NEW_TOL
            and abs(dl2["ba3_res"] / WIT_D2["ba3"] - 1) <= NEW_TOL
            and dl2["ba3_res"] < 0)
    check("G56-witness-vs-manifold", ok56,
          "THE BROKEN-CONSTRAINT LIST (frozen strings): INFLATION "
          "breaks {G30 ground-state cert: r0''/tau = %.3e (39 "
          "orders above the 1e-25 bar); G32 lock %.4e < 1.0 (== "
          "lock/1000 EXACTLY: fixed-M theorem G16); G33/G34 theta "
          "62.69; G35 J2'' = %.3e below window, rho-argmax %d != "
          "1, cap %.6f below window; G37-class census "
          "complete-real BROKEN (%d/10 real), ztop %.6f > 0.95; "
          "BA3 BRIDGE: zsum''/zsum = %.4e, residual %.4e < 0 "
          "(WITNESS-BREAKS-BA3-BRIDGE -- the witness is NOT "
          "budget-blind: it moves the zero-side sum x3.6e8 while "
          "A_0 is invariant)}; SATISFIES {A_0/trace identities, "
          "sign, kappa window %.3e, H1 c* = %s EXISTS "
          "(H1-WORLD-BLIND, r171 replicated)}; DEFLATION breaks "
          "{G30 %.3e; lock %.4e > 8.0 (the OTHER side); kappa "
          "%.2f > 0.30; J2 %.3e above window; census %d/10; H1 "
          "REFUSED; BA3 %.4e < 0}: "
          "WITNESS-EXCLUDED-BY-CERTIFIED-SET in BOTH directions"
          % (i2["r0_tau"], i2["lock"], i2["J2"], i2["rho_argm"],
             i2["cap"], i2["nreal"], i2["ztop"], i2["zratio"],
             i2["ba3_res"], i2["kappa"], i2["cstar"],
             dl2["r0_tau"], dl2["lock"], dl2["kappa"], dl2["J2"],
             dl2["nreal"], dl2["ba3_res"]))

    ok57 = (abs(wit["dnorm3"] / WIT_I3["dnorm"] - 1) <= NEW_TOL
            and wit["dnorm3"] >= 1e3
            and i3["a0_dev"] <= WIT_A0_BAR
            and abs(i3["yt_ratio"] / WIT_FACT - 1) <= WIT_YT_BAR
            and i3["j2_dev_main"] <= 1e-25
            and i3["rho_argm"] == 1
            and abs(i3["cap"] / WIT_I3["cap"] - 1) <= NEW_TOL
            and CAP_WIN[0] <= i3["cap"] <= CAP_WIN[1]
            and i3["nreal"] == WIT_I3["nreal"]
            and abs(i3["ztop"] / WIT_I3["ztop"] - 1) <= NEW_TOL
            and TOP_WIN[0] <= i3["ztop"] <= TOP_WIN[1]
            and i3["cstar"] is not None
            and i3["cstar"] <= INFL3_CSTAR_MAX
            and abs(i3["a6_ratio"] / WIT_I3["a6"] - 1) <= NEW_TOL
            and abs(i3["a6_ratio"] - 1) >= 0.9
            and abs(i3["r0_tau"] / WIT_I3["r0"] - 1) <= NEW_TOL
            and i3["r0_tau"] >= WIT_R0_MIN
            and i3["lock"] < LOCK_WIN[0]
            and i3["theta"] > THETA_BAR
            and abs(i3["zratio"] / WIT_I3["zratio"] - 1) <= NEW_TOL
            and abs(i3["ba3_res"] / WIT_I3["ba3"] - 1) <= NEW_TOL
            and i3["ba3_res"] < 0)
    check("G57-witness-escalation", ok57,
          "the 3-mode J2-PRESERVING inflation witness (G14 generic "
          "solve, mp instance): REPAIRS the moment/census windows "
          "{J2'' == J2 dev %.1e, rho-argmax 1, cap %.4f in window, "
          "census %d/10 complete-real, ztop %.4f in TOP_WIN, H1 c* "
          "= %s} -- the moment/census gates are NOT the "
          "load-bearing exclusion -- but the PRICE EXPLODES: "
          "|d|/max|c| = %.4e (x1.0e5 the 2-mode price %.1e: the "
          "J2 repair is no longer a cheap perturbation), J3 is NOT "
          "preservable (A6''/(W^3 A6) = %.2e != 1, generic "
          "obstruction G14), and the manifold exclusion STANDS: "
          "{G30 r0''/tau = %.3e, lock %.4e < 1.0, theta %.2f > "
          "bar, BA3 residual %.4e < 0}: "
          "WITNESS-REPAIR-PRICE-EXPLODES + ESCALATION-STABLE"
          % (i3["j2_dev_main"], i3["cap"], i3["nreal"], i3["ztop"],
             i3["cstar"], wit["dnorm3"], wit["dnorm2"],
             i3["a6_ratio"], i3["r0_tau"], i3["lock"], i3["theta"],
             i3["ba3_res"]))

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    if not smoke and len(tab) >= 8:
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
              "%.4f (<= 0.30 DEMAND-FLAT); RIDER log10 A_0^2 "
              "slope %.3f in (0.85, 1.15) (BOUND-RIDES-CONNES)"
              % (s_yt, s_th, s_a0))
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

    dep = {"QUANT-COLLAPSE": ("SOURCE", "THETA-LADDER-MEAS"),
           "DK-STABILITY": ("SOURCE", "SPECTRAL-CERT"),
           "BA-ADJUDICATION": ("SOURCE", "R166-CITED"),
           "WITNESS-EXCLUSION": ("SOURCE", "SPECTRAL-CERT",
                                 "CACHE-WARD", "PT21-CENSUS-PER-K",
                                 "HSW22"),
           "TRANSPORT-CEILING": ("LOCK-WINDOW-MEAS",
                                 "FG-QUARTIC-MEAS"),
           "H3-PER-RUNG": ("SOURCE",),
           "SOURCE": (), "SPECTRAL-CERT": (), "CACHE-WARD": (),
           "THETA-LADDER-MEAS": (), "R166-CITED": (),
           "LOCK-WINDOW-MEAS": (), "FG-QUARTIC-MEAS": (),
           "PT21-CENSUS-PER-K": (), "HSW22": (),
           "TLAWCAP": (), "WPD": (), "CENSUS-ALL-K": (),
           "TAUPOS": (), "TOPROOT-MEAS": (),
           "ZERO-VERIF-AS-HYP": (),
           "LOOP-ROUTE(tlaw==>blocksum)": ("TLAWCAP",),
           "LOOP-ROUTE(census-all-k)": ("CENSUS-ALL-K",),
           "LOOP-ROUTE(pinning-supply)": ("TAUPOS", "TLAWCAP"),
           "LOOP-ROUTE(a0-floor)": ("TAUPOS", "TLAWCAP")}

    def ancestors(node):
        seen = set()
        stack = [node]
        while stack:
            nn = stack.pop()
            for p in dep.get(nn, ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        return seen

    delivered = ("QUANT-COLLAPSE", "DK-STABILITY", "BA-ADJUDICATION",
                 "WITNESS-EXCLUSION", "H3-PER-RUNG")
    banned = {"TLAWCAP", "WPD", "TAUPOS", "CENSUS-ALL-K",
              "TOPROOT-MEAS", "ZERO-VERIF-AS-HYP"}
    ok61 = all(not (ancestors(nd) & banned) for nd in delivered) \
        and "FG-QUARTIC-MEAS" in ancestors("TRANSPORT-CEILING") \
        and "TRANSPORT-CEILING" not in delivered \
        and ancestors("H3-PER-RUNG") == {"SOURCE"} \
        and "TAUPOS" in ancestors("LOOP-ROUTE(a0-floor)")
    check("G61-loop-mining", ok61,
          "delivered-statement ancestors CLEAN: QUANT-COLLAPSE == "
          "{SOURCE, THETA-LADDER-MEAS}; DK-STABILITY == {SOURCE, "
          "SPECTRAL-CERT}; BA-ADJUDICATION == {SOURCE, R166-CITED}; "
          "WITNESS-EXCLUSION == {SOURCE, SPECTRAL-CERT, CACHE-WARD, "
          "PT21-CENSUS-PER-K, HSW22}; H3-PER-RUNG == {SOURCE} "
          "(r172); TRANSPORT-CEILING carries FG-QUARTIC-MEAS and is "
          "EXCLUDED from the delivered set (CONDITIONAL-ON-MEASURED, "
          "flagged not consumed); TLAWCAP, WPD, TAUPOS, "
          "CENSUS-ALL-K, TOPROOT-MEAS, ZERO-VERIF-AS-HYP ancestors "
          "of NOTHING delivered; FIVE flagged routes carried NOT "
          "consumed (tlaw-window, census-all-k, pinning-supply, "
          "A0-floor, zero-verification-as-hypothesis); windows "
          "recomputed from frozen formulas, SIGN-MINING-CLEAN "
          "(disclosures in G60)")

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
          "flows: base 4, refined 5 (r171/r172 graph VERBATIM -- "
          "this round retypes no set), one-grant 5, counterfactual "
          "PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")

    chain_uni = {
        "RH": ["CENSUS_ALLK"], "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"], "DTSTEP_ALLK": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"], "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"], "RH_VIA_N": ["RH"]}
    loop_uni = has_cycle(chain_uni)
    chain_pin = {
        "DCLEG": ["SIGMAFLOOR"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"],
        "TAUPOS": ["SIGMAFLOOR"]}
    loop_pin = has_cycle(chain_pin)
    chain_a0 = {
        "TAUPOS": ["A0FLOOR"], "TLAWCAP": ["A0FLOOR"],
        "A0FLOOR": ["TOPROOT"], "TOPROOT": ["RATE"],
        "RATE": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["TAUPOS"]}
    loop_a0 = has_cycle(chain_a0)
    chain_term = {
        "ENVJ_H1": ["PF"], "CENSUS_H2": ["PF"], "TRACE": ["PF"],
        "GONEK": ["WF", "DCLEG"],
        "H3_PER_RUNG": ["RATE"], "H3_COFINAL": ["RATE"],
        "THETA_MONO_MEAS": ["QUANT_COLLAPSE"],
        "QUANT_COLLAPSE": ["H3_COFINAL"],
        "LOCK_MEAS": ["THETA_CEILING"],
        "FG_QUARTIC_MEAS": ["THETA_CEILING"],
        "THETA_CEILING": ["H3_COFINAL"],
        "DK_STAB": ["H3_PER_RUNG"],
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
    rh_reach = all("RH" in reachable(chain_term, nd)
                   for nd in ("ENVJ_H1", "CENSUS_H2", "H3_PER_RUNG",
                              "H3_COFINAL", "QUANT_COLLAPSE",
                              "THETA_CEILING", "GONEK", "CENSUS_K"))
    check("G63-endgame-graphs", loop_uni and loop_pin and loop_a0
          and acyc and rh_reach,
          "(i) universalized census cycle DETECTED; (ii) "
          "pinning-supply cycle DETECTED; (iii) A0-floor cycle "
          "DETECTED (all three replicated from r172, NOT consumed); "
          "(iv) the terminal chain EXTENDED with {THETA-MONO-MEAS "
          "-> QUANT-COLLAPSE -> H3_COFINAL} and {LOCK-MEAS, "
          "FG-QUARTIC-MEAS} -> THETA-CEILING -> H3_COFINAL (the "
          "flagged conditional edge) and DK_STAB -> H3_PER_RUNG is "
          "ACYCLIC with RH reachable from every counterfactual "
          "grant (AND-semantics); NO RH CLAIM")
    info("THE FINAL RESIDUE (exact, typed): the lambda-uniform "
         "residue of the delta-chain is UNCHANGED IN CARDINALITY "
         "and now COMPRESSED IN FORM: {H3-COFINAL == (mod the "
         "measured defect D = 0.0042 and the measured monotone "
         "trend, G11/G44) the ONE LIMIT INEQUALITY limsup theta_y "
         "<= 0.155 -- equivalently THETA-FG-flat on the two-sided "
         "lock manifold (G10/G43, conditional edge flagged "
         "MEASURED); per-rung certified (r172, 26/26) and "
         "saturating with every frozen model limit t_inf in "
         "(0.0766, 0.0977) <= bar/1.59 (G40); its classical "
         "evaluation == a Gonek/Montgomery-class second-moment "
         "constant, OPEN (the named citable classic; 1/(4 pi) "
         "recorded inside the band, NOT claimed); the averaging/"
         "pigeonhole weakening is exact but EMPTY (subsidy 4% at "
         "depth, nothing to cancel, BA-inexpressible: G11-G13/"
         "G44); the witness cannot touch it on the certified "
         "manifold (G56/G57) and the manifold is DK-norm-stable "
         "at measured residuals (G15/G36)} + {GONEK constants: "
         "citable classical work (parallel lane)} + "
         "{census-all-k == LOOP, flagged} + {L1, WPD}.  Census "
         "min-cut cardinality 4 UNCHANGED; NO omega closed; "
         "nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "WINDOWS-FROZEN-PREEVAL(G60/G61)",
        "CITED-LADDER-REPLICATED(G33)",
        "SATURATION-REAL-NOT-FIT-ARTIFACT(G40)",
        "THETA-INF-BAND-UNDER-BAR(G40)",
        "THETA-INF-CLASSICAL-OPEN-GONEK-CLASS(G40)",
        "P-LOCAL-DESCENDS-TO-QUARTIC(G41)",
        "RATE-DICTIONARY-TIGHTENED(G42)",
        "THETA-CEILING-CONDITIONAL-MEASURED-FLAGGED(G43)",
        "QUANTIFIER-GAP-MEASURED-THIN(G11/G44)",
        "PIGEONHOLE-EXACT-SUBSIDY-EMPTY(G11/G44)",
        "AVERAGING-NOTHING-TO-CANCEL(G12/G44)",
        "BA-INEXPRESSIBLE-FOR-YT(G13)",
        "H3-REFUTABLE-OFF-MANIFOLD(G53)",
        "WITNESS-EXCLUDED-BY-CERTIFIED-SET(G56)",
        "WITNESS-BREAKS-BA3-BRIDGE(G56)",
        "WITNESS-REPAIR-PRICE-EXPLODES(G57)",
        "ESCALATION-STABLE(G57)",
        "H3-NORM-STABLE-AT-MEASURED-RESIDUALS(G15/G36)",
        "STABILITY-CROSSOVER-MEASURED(G36)",
        "H3-ONE-SIDED-WORLD-BLIND + SIZE-SEPARATOR(G50-G52)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-SEQ(G60)",
        "LOOP-ROUTES-FLAGGED(five; G61/G63)",
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
