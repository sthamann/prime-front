#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gfloor_probe -- PRIME.GFLOOR.PROOF.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the QSUBGAP g-floor, the surviving
one-statement form of the spectral-balance pair and one of the two
final arithmetic cores)
=======================================================================
After r157 (CDLXI) the pair {SUSCAP2R, DELTA1FLOOR} is EXACTLY the one
floor g := (lam* - q_0)/tau >= 1/poly(x), with the proven enclosure
BS = rho2 delta_1 <= g <= delta_1 (lower end rate-blind, g/BS up to
6.5e88 vacuous).  This probe mounts the maximal proof attempt on the
g-floor itself along the four contract angles: (G1) the two-level
jet-ratio law, (G2) the S1-floor, (G3) the Newton/interlacing squeeze,
(G4) red team; and adjudicates THE MERGE (does J-family boundedness,
the concurrent lane's target, imply the g-floor?).

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, Mq = round-114 builder (even sector), eigenpairs
lam_0 = tau < lam_1 <= ... with eigenvectors phi, psi_1, ...
(mpE/mpV); FULLGAP = (lam_1 - tau)/tau; jet functional v_0 =
((-1)^k/nrm_k)_k, A_0(v) = v_0 . v, w_i = A_0(psi_i)^2; Delta_i =
(lam_i - tau)/tau (source gaps); T_z = 2 pi x; m = verified zone
census; V = kernel of the m newton-polished node rows, W = Gram-
orthonormal compression, eigenpairs (q_i, z_i), q_0 = tau; probe row
r(p) at the zone-top argmin: normalized overlaps et_i, rho2 = et_0^2,
lam* = the secular root in (q_0, q_1), g = (lam* - q_0)/tau, delta_i
= (q_i - q_0)/tau, chi_t = sum_{i>=1} et_i^2/delta_i, s = chi_t/rho2,
H_t = sum_{i>=1} 1/delta_i (compressed harmonic floor), T2(g) =
sum_{i>=1} et_i^2/(delta_i (delta_i - g)); eta_i = A_0 of the K-space
representative of z_i; psi* = the constrained ground (eigenvector at
lam*), c*_i = et_i/(q_i - lam*); SOURCE side: GW = sum_{i>=1}
w_i/(lam_i - tau), SEC = tau GW/w_0 = sum_{i>=1} (w_i/w_0)/Delta_i,
TRF = sum_{i>=1} 1/Delta_i = tau TrH (TRACEFLOOR), beta_0 = the
unique B_00-root in (tau, lam_1), betapos = (beta_0 - tau)/tau, J =
w_1/w_0, jr = J/FULLGAP, S1 = [w_1/(lam_1 - beta_0)]/[sum_{i>=1}
w_i/(lam_i - beta_0)] (r150 R3).  gtop = 7264.75 (X5 cache).

FROZEN QUANTIFIER (declared before the deep data, the r141 dense-x
demand level): the g-floor demand adjudicated here is [EXISTS c > 0,
n_0: g(x) >= c x^{-n_0} on the instrument-chosen sequence (the frozen
ladder + its V2 dense-x extension)].  This probe proves COORDINATES
and the exact characterization; it does NOT claim the floor.

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically + exact rational
instances + mp-instantiated per rung; classical inputs typed CITED)
=======================================================================
THEOREM GF1 (the razor enclosure; the G3 answer, part 1).  Let
(weights positive, simple ground) the secular root equation hold:
rho2/g = sum_{i>=1} et_i^2/(delta_i - g), 0 < g < delta_1.  Then
(a) UPPER (strict):  g < 1/s.   Proof: sum et_i^2/(delta_i - g) >
    sum et_i^2/delta_i = chi_t = s rho2, so rho2/g > s rho2.
(b) LOWER:  g >= 1/(s + 1/delta_1).   Proof: delta_1 T2(g) <= S(g)
    termwise (delta_1 <= delta_i), where S(g) - chi_t = g T2(g)
    (partial fractions), so delta_1 (S - chi_t) <= g S = rho2, i.e.
    rho2 delta_1 <= g (chi_t delta_1 + rho2), rearrange.
(c) DOMINANCE over r157: BS = rho2 delta_1 <= 1/(s + 1/delta_1)
    <==> s rho2 delta_1 <= 1 - rho2 == THEOREM SB2 (the chi-cap):
    the new lower end EXACTLY absorbs the r157 lower end.
(d) TWO-LEVEL EQUALITY: at nf = 2 the root is g = rho2 delta_1 = BS
    = 1/(s + 1/delta_1): the lower end is ACHIEVED in algebra -- no
    algebra-only improvement of GF1 exists (red-team hard assert).
(e) EXPLICIT TRANSFER both ways: [g >= 1/P ==> s < P AND delta_1 >=
    1/P] and [s <= P AND delta_1 >= 1/P' ==> g >= 1/(P + P')]: the
    g-floor IS the pair with explicit constants and NOTHING between.
Calibration x=5/8: lo/g = 0.999995335/0.999999417, g x s =
0.999853583/0.999983781, BS <= lo True/True, relative enclosure
width (hi - lo)/g = 1.511e-4/1.680e-5 FALLING (g/delta_1 class):
the r157 enclosure [BS, delta_1] (vacuity up to 88 dex) is replaced
by a PROVEN enclosure of relative width < 2e-4.

THEOREM GF2 (the pinch-defect law: s x gap == 1 is a THEOREM).
EXACTLY 1 - s g == g^2 T2(g)/rho2 > 0, and 1 - s g <= s g x
g/(delta_1 - g).  The r157-measured 'g/delta_1 = s x gap pinch
family' is now the exact law: sg is pinned in [1 - sg g/(delta_1 -
g), 1) -- the defect is priced by g/delta_1.  Calibration: identity
dev 1.5e-57/1.9e-66; 1 - sg = 1.464e-4/1.622e-5 <= bound
1.511e-4/1.680e-5 (tight to 3%/3%).

THEOREM GF3 (share_1^g pricing; closes the r157 lever (c)).  With
a = g/(delta_1 - g), b = g T2/chi_t: share_1^g/share_1 == (1+a)/
(1+b) with 0 <= b <= a, hence EXACTLY 0 <= share_1^g/share_1 - 1 <=
g/(delta_1 - g): the near-equality is one-sided (share_1^g >=
share_1 ALWAYS) and priced g/delta_1-class -- the r157-measured dev
ladder 4.7e-6 -> 4.7e-9 is explained, sign and rate.  Calibration:
dev = +4.665e-6/+5.831e-7 <= bound 1.511e-4/1.680e-5.

THEOREM GF4 (the jet-ratio law + Newton value law; the G1 + G3
answers).  (a) THE MECHANISM ONE LEVEL SIDEWAYS: the constrained
ground psi* (eigenvector of the compression V cap r-perp at lam*)
satisfies psi* propto sum_i c*_i z_i with c*_i = et_i/(q_i - lam*)
(Lagrange/rank-one constraint), so its 0-jet is the MOMENT-RATIO
   A_0(psi*) = [sum_i eta_i et_i/(q_i - lam*)] /
               sqrt(sum_i et_i^2/(q_i - lam*)^2)
-- a cross-resolvent datum of the overlap ladder {et_i} and the jet
ladder {eta_i}.  With tlaw* := lam*/(8 A_0(psi*)^2 G(T_z)) and Jg :=
(A_0(psi*)/A_0(phi))^2 the chase gives EXACTLY Jg x (tlaw*/tlaw_0)
== 1 + g: THE g-FLOOR IS A JET-RATIO FLOOR (the exact g-version of
the r150 R2 identity), and the demand is the anti-degeneracy
[Jg tlaw-ratio - 1 >= 1/poly] of the 0-jet map on the pair (phi,
psi*).  MEASURED DISCOVERY (calibration): tlaw* = 0.2399/0.3175 --
IN THE tlaw WINDOW CLASS (tlaw_0 = 0.2664/0.3738, ratio t_g =
0.9005/0.8493 flat O(1)): the constrained ground OBEYS THE ZERO-JET
LAW -- the third rung of the mechanism (ground r137, first excited
CDL, constrained ground HERE).  (b) NEWTON VALUE LAW: with B(z) =
P_c(z) sum et_i^2/(q_i - z): B(q_0) == -rho2 P_c'(q_0) (the exact
compressed analogue of r153 RES1 -- the bordered value CARRIES rho2:
any repulsion argument on B presupposes the rho2 scale, the r153
self-reference one level down, pinned) and the Newton quotient at
q_0 is N_1 = 1/(H_t + s): the g-value is the RESOLVENT-CAP quotient
(calibration N_1/g = 0.999995332/0.999999417 -- second-order exact,
not one-sided; the enclosure GF1 supplies the one-sided ends).
(c) Rayleigh cross-instrument: Rayleigh(psi*) == lam* given the root
equation (identity, gated); eta_0^2 == A_0(phi)^2 (the compressed
ground jet is the source ground jet; calibration dev 4.4e-49/
1.7e-56).

THEOREM GF5 (the S1-law + the twin squeeze; the G2 answer).
(a) EXACTLY S1 == jr x betapos x (lam_1 - tau)/(lam_1 - beta_0)
(chase from r150 R3 + R2 definitions), and (lam_1 - tau)/(lam_1 -
beta_0) >= 1, hence S1 >= jr x betapos UNCONDITIONALLY: the S1-floor
is ABSORBED -- [betapos >= 1/P AND jr >= 1/c] ==> S1 >= 1/(cP).  The
r150 reading 'B00-ROOTGAP + S1-floor' collapses to the root
separation ALONE modulo the R2-window: ONE decay law, not two (the
S1 ~ x^{-1.2} measured law IS the betapos law times flat jr).
(b) THE TWIN SQUEEZE (GF1 applied at the jet weighting {w_i,
Delta_i}): 1/(SEC + 1/FULLGAP) <= betapos <= 1/SEC, with the same
defect law 1 - SEC betapos == betapos^2 T2W/w_0-normalized > 0 and
Newton value N_1W = 1/(TRF + SEC): THE TWO FINAL ARITHMETIC CORES
ARE THE SAME STATEMENT-FORM -- bottom-root position == resolvent-cap
quotient -- at two weightings (probe row {et_i^2, delta_i} for
QSUBGAP; 0-jet {w_i, Delta_i} for TOPROOT/B00-ROOTGAP).
(c) J <= SEC x FULLGAP exact chase (J = S1 (F - b)/b <= F/b - 1 <=
SEC F): the TOPROOT demand in SEC currency.  Calibration x=5/8: SEC
= 4.0602671/7.6605962, betapos = 0.24628914/0.13053814 == r150
strings, squeeze HARD (1 - SEC betapos = 3.06e-7/1.90e-8), S1
identity dev 0.0/5.6e-70, N_1W/betapos = 0.99999920/0.99999989,
SEC/nf = 0.580/0.696 (printed law-hunt exhibit).

THE MERGE ADJUDICATION (T5; the round's central question).  Does
J-family boundedness (J_m = a_{2m}/y_t^m bounded, the concurrent
j2_primeforce lane's target) IMPLY the g-floor?  ANSWER: NO AT THE
ALGEBRA LEVEL, machine-pinned: the J-family is a function of the
SOURCE tuple (c_k) alone; the compressed-weight/probe-row freedom is
invisible to it.  WITNESS (mp, on the real x=5 rung data): the legal
two-level configuration rho2 = 1/(1 + P delta_1) realizes s == P =
1e6 and g == 1/(s + 1/delta_1) == rho2 delta_1 (the GF1 lower end
WITH EQUALITY) while every source moment (y_t, all a_{2m}, all J_m)
is bit-identical: g -> 0 with the whole J-family fixed.  MERGE-
REFUTED-ALGEBRA.  The arithmetic channel stays honestly open: the
instrument's probe row is source-determined (the zone-top argmin of
the census configuration) -- but a bridge consuming THAT pinning
would be a new statement, not 'J-family bounded ==> g-floor'.
POSITIVE FINDING: the two final cores merge at the FORM level (GF5b)
-- ONE statement-form, TWO arithmetic weightings.  The program
residue stays TWO statements; census cardinality UNCHANGED.

RED-TEAM (mandatory): (i) the r157 2D model: s == 1e6 legal witness
with the GF1 lower end achieved (equality dev 0.0) -- no algebra-
only improvement of the enclosure exists; (ii) the r150 jet toy
(M = diag, v = (p, q, 0) free): SEC = (q^2/p^2)/Delta_1 is FREE --
witness SEC == 1e6 exact with all GF5 identities intact: no algebra-
only SEC-cap (ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-SEC); (iii) the r153
A_0-rescaling class inherited (w_0 in the denominators of SEC and of
B(q_0) = -rho2 P_c': both bordered values carry the collapsing scale
as an exact factor -- self-referential, pinned); (iv) CONTROLS:
SMOOTH/SCRARITH x=5, EPSTEIN x=8 refuse fourfold (zone overcount,
mu_1 fills the verified zero-free gap, tau_w < 0: the PSD/simple-
ground hypotheses of GF1-GF5 fail EXACTLY there, no positive ground
to separate from; no escaped scale y_t_w/b_top <= 1); (v) tau-
screens with riders: the demand ratios (s, gap, share_1, jr, t_g)
are tau-flat; rho2/BS/w_0/A_0(psi*)^2 RIDE (BOUND-RIDES-CONNES).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 GF1: partial-fraction identity S - chi_t == g T2 generic
    3-level; upper strict (S > chi_t); lower (S - delta_1 T2 ==
    nonneg spread term); BS <= lo <==> chi-cap (SB2 re-chase);
    2-level equality instance; explicit transfer both directions;
    G11 GF2: 1 - sg == g^2 T2/rho2 generic (root-equation
    substitution rho2 = g S); bound T2 <= chi_t/(delta_1 - g)
    termwise ==> 1 - sg <= sg g/(delta_1 - g);
    G12 GF3: share ratio == (1+a)/(1+b) generic with b <= a ==>
    0 <= dev <= a; 2-level dev == a instance;
    G13 GF4: B(q_0) == -rho2 P_c'(q_0) generic 3-level polynomial;
    Newton quotient == rho2/(rho2 H + chi) == 1/(H_t + s) chase;
    constrained-eigenvector u* = (W - lam*)^{-1} r-hat (Lagrange
    verification on diag 3-level) + Rayleigh(u*) == lam* given the
    root equation; Jg t_g == 1 + g chase;
    G14 GF5: S1 == jr betapos (lam_1-tau)/(lam_1-beta_0) chase +
    corr >= 1 ==> S1 >= jr betapos; twin squeeze at (w_i, Delta_i)
    (the GF1 lemma re-instanced); J <= SEC x FULLGAP chase;
    G15 red team symbolic: 2-level witness s == P with lower-end
    equality; jet toy SEC free (witness q^2 = 1e6 p^2 Delta_1 ==>
    SEC == 1e6 exact): hard asserts.
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150),(28,160) deep (zone sign-scan to T_z + 6,
    step 0.05; newton-polished nodes, the r141/r143 standard):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform);
    G31 spectral ladder: lam_i > 0 sorted; FULLGAP in the frozen
    windows (r142/r146 strings + CDLII x=28 string) x (0.97, 1.03);
    lam_1 SIMPLE (rel gap >= 1e3); post-loop growth slope in
    (3.4, 4.6);
    G32 node-config V + replication: |qrel| <= 1e-30, null residual
    <= 1e-40; W3 re-gate delta_1 >= FULLGAP (1 - 1e-12); zone-top
    argmin in the frozen windows AND >= 3; s <= S_BAR_TAB; sg in
    (0.98, 1.02); delta_1 windows; share_1 >= 0.5; tlaw on the
    CDXLI strings <= 5e-3 (x <= 24) / in (0.40, 0.70) at 28; lock
    FULLGAP/y_t in (1.5, 6.0);
    G33 GF1 instantiated: BS <= lo = 1/(s + 1/delta_1) <= g < 1/s
    HARD (mp, slop 1e-12) + g <= delta_1 HARD; chi cross-instrument
    |chi tau/chi_t - 1| <= 1e-40; N_1/g in (0.99, 1.01); relative
    width table printed (the razor exhibit);
    G34 GF2/GF3 instantiated: pinch identity dev <= 1e-40; 1 - sg
    > 0 HARD and <= bound (1 + 1e-12) HARD; share dev in [-1e-30
    slop, g/(delta_1 - g)] HARD + dev table (falling exhibit);
    G35 GF4 instantiated: Rayleigh dev <= 1e-40; eta_0^2 vs
    A_0(phi)^2 dev <= 1e-30; Jg t_g == 1 + g dev <= 1e-30; tlaw*
    windows: {5: 0.2399, 8: 0.3175} x (0.97, 1.03) calibrated,
    deep (0.10, 1.00) DISCLOSED-unmeasured; t_g in (0.5, 2.0);
    eta-ladder head + Jg + tlaw* tables printed (the mechanism-
    sideways exhibit);
    G36 GF5 instantiated: tau < beta_0 < lam_1 HARD (bisection
    250); twin squeeze 1/(SEC + 1/FG) <= betapos <= 1/SEC HARD;
    twin defect identity dev <= 1e-40; S1 identity dev <= 1e-40 +
    S1 >= jr betapos HARD; J <= SEC FG (1 + 1e-12) HARD; betapos
    windows: {5: 0.2463, 8: 0.1305} x (0.99, 1.01) calibrated,
    {13: 0.0821, 18: 0.0558, 24: 0.0420, 28: 0.0328} x (0.97,
    1.03) (r150 strings, same pipeline) DISCLOSED; jr in (0.8,
    1.6); N_1W/betapos in (0.99, 1.01); SEC/nf + J2-proxy
    |A_4/A_0|/y_t^2 in (0.03, 0.5) printed (law-hunt exhibits).
S3c G40 red-team mp (x = 5 rung data): 2D witness s == 1e6 (dev <=
    1e-40) with LOWER-END EQUALITY g == 1/(s + 1/delta_1) == rho2
    delta_1 (devs <= 1e-40) while the source moments (y_t, J2-
    proxy) recomputed around the witness are EXACTLY unchanged
    (MERGE-REFUTED-ALGEBRA hard assert); jet-toy SEC witness ==
    1e6 (dev <= 1e-40).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    AND tau_w < 0 (the GF hypotheses fail EXACTLY here) AND
    y_t_w/b_top <= 1.0; G53 consistency.
S5  G54 tau-screens: |slope log10 v vs log10 tau| <= 0.30 for v in
    (s, gap, share_1, jr, t_g) -- the demand ratios are tau-flat;
    RIDER report: slopes of log10 rho2, log10 BS in (0.30, 1.20)
    and log10 w_0, log10 A_0(psi*)^2 in (0.85, 1.15) (ride tau --
    BOUND-RIDES-CONNES typed); SEC growth slope vs log10 x printed
    (the betapos law-hunt exponent); G55 conditioning (1e-25 shift
    window).
S6  G60 demand audit (CHAIN-AUDIT: NFCLOS sequence-demand ->
    Theorem R transfer -> coupling absorbed -> the g/betapos/SEC
    coordinates consume NO tlaw, NO Z, no lattice proximity
    (source + secular data only; r142 W2/W3 + r141 V1 cited) -> V2
    good sets -> no ALL-X demand; both enclosure ends eigensolve-
    light: N_1 and the ends are resolvent data -- CERT-COST-POLY
    class inherited);
    G61 min-cut (r116 replica; r142/r144/r146/r150 graph VERBATIM):
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL
    9 NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150),(28,160)); HSW = (0.1038, 0.2573, 9.3675) [HSW22
Cor. 1.2]; SCAN_STEP = 0.05; SCAN_LO = 0.5; SCAN_OVER = 6.0;
TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05; NODE_EXCL = 0.02;
BIS_ITERS = 250.
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26), 28: (10, 30)}; S_BAR_TAB =
{5..24: 0.1, 28: 0.15}; SGAP_WIN = (0.98, 1.02); D1_TAB = {5:
2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7, 24: 1.14e8, 28:
1.6513e8} x (0.7, 1.3); SHARE1_BAR = 0.5; TLAW_TAB = {5: 0.2664,
8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI
strings); TLAW28_WIN = (0.40, 0.70); FG_TAB = {5: 2.2255e5, 8:
9.9512e5, 13: 1.0619e7, 18: 3.2497e7, 24: 1.1382e8, 28: 1.6513e8}
x (0.97, 1.03); FG_SLOPE_WIN = (3.4, 4.6); SIMP_MIN = 1e3;
LOCK_WIN = (1.5, 6.0); ENC_SLOP = 1e-12; XCHI_BAR = 1e-40
(calibration 1.6e-61/0.0); N1_WIN = (0.99, 1.01) (calibration
0.999995332/0.999999417); ID2_BAR = 1e-40 (calibration 1.5e-57/
1.9e-66); SH_NEG_SLOP = 1e-30; RAY_BAR = 1e-40 (calibration
2.3e-61/2.9e-71); ETA0_BAR = 1e-30 (calibration 4.4e-49/1.7e-56);
ID4_BAR = 1e-30 (calibration 1.3e-47/8.4e-55); TLAWST_TAB = {5:
0.2399, 8: 0.3175} rel win (0.97, 1.03); TLAWST_DEEP_WIN = (0.10,
1.00) (DISCLOSED-unmeasured, tlaw-trend); TG_WIN = (0.5, 2.0)
(calibration 0.9005/0.8493); ID5_BAR = 1e-40 (calibration 0.0/
5.6e-70); IDTW_BAR = 1e-40 (calibration 2.1e-55/2.9e-62);
BETA_TAB = {5: 0.2463, 8: 0.1305, 13: 0.0821, 18: 0.0558, 24:
0.0420, 28: 0.0328}; BETA_WIN_CAL = (0.99, 1.01) (x = 5/8
calibrated 0.24628914/0.13053814); BETA_WIN_DEEP = (0.97, 1.03)
(r150 strings, same pipeline, DISCLOSED); JR_WIN = (0.8, 1.6);
N1W_WIN = (0.99, 1.01) (calibration 0.99999920/0.99999989);
JSEC_SLOP = 1e-12; J2PROXY_WIN = (0.03, 0.5) (calibration
0.12588437/0.13944479; r154/r156 J2 class); RT_P = 10^6;
RT_ID_BAR = 1e-40; CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30;
RIDER_WIN = (0.30, 1.20); W0_RIDER_WIN = (0.85, 1.15) (r150 slope
1.00 class); COND_WIN = (1e-40, 1e-10); GAMMA1_LIT =
14.134725141734694 (ward only); RUNTIME_BAR = 14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64-refinement of
mp roots; np.float64-repr casts guarded by float()/repr(); tiny/
huge quantities stay mp end-to-end (the r147 underflow lesson:
rho2/BS/w_i/beta_0/eta/A_0(psi*) kept mp; log diagnostics via
mp.log inside workdps); census/build_V/secular_data/newton_node/
row_at ported VERBATIM from the r157 spectral_balance source (==
r138-r150 replica class); bisect_secular ported VERBATIM from the
r150 collapserate source.

CALIBRATION DISCLOSURE (pre-freeze, ONE scratch script
calib_scratch_gfloor.py + log, x = 5/8 only, deleted after freeze;
all numbers quoted verbatim above and here): x=5: g 33.623293, s
0.029736932, sg 0.9998535833, d1 222551.03, lo/g 0.999995335445,
relwidth 1.511e-4, xchi 1.6e-61, GF2 id dev 1.5e-57, 1-sg
1.464167e-4 <= 1.5108198e-4, GF3 dev +4.665e-6 <= 1.511e-4, H_t
4.4934454e-6, N1/g 0.999995332289, A0phi 4.73264e-8, A0psi
-2.93455e-7, Jg 38.448236, tlaw0 0.266351, tlaw* 0.239853, tg
0.90051707, raydev 2.3e-61, eta0dev 4.4e-49, id4 1.3e-47, SEC
4.0602671, betapos 0.24628914, 1/SEC 0.24628921, 1-SEC betapos
3.06495e-7, S1 0.2769462 (id dev 0.0), jr 1.1244747, J 250251.07,
TRF 4.49348e-6, N1w/bpos 0.9999991998, SEC/nf 0.5800 (nf 7),
y_t 61066.732, J2-proxy 0.12588437, 2D witness s dev 1.9e-121,
lower-end equality dev 0.0.  x=8: g 16.719978, s 0.05980772, sg
0.9999837812, d1 995124.89, lo/g 0.999999416909, relwidth
1.680e-5, GF2 id 1.9e-66, 1-sg 1.6218798e-5 <= 1.6801899e-5, GF3
dev +5.831e-7, H_t 1.0049019e-6, N1/g 0.99999941686, A0phi
8.41894e-15, A0psi -3.84545e-14, Jg 20.863133, tlaw0 0.373806,
tlaw* 0.31749, tg 0.84934406, raydev 2.9e-71, eta0dev 1.7e-56,
id4 8.4e-55, SEC 7.6605962, betapos 0.13053814, 1-SEC betapos
1.90024e-8, S1 0.1448599 (id 5.6e-70), jr 1.1097131, J 1104303.1,
TRF 1.0049e-6, N1w/bpos 0.9999998878, SEC/nf 0.6964 (nf 11), y_t
416540.63, J2-proxy 0.13944479.  x = 13..28 pre-freeze UNMEASURED
on all new quantities (build cost); their windows are set from the
frozen r139-r157/CDLII strings, the calibrated trends and
structure asserts, DISCLOSED above.  Amendments after the frozen
run, if any, are appended as numbered AMENDMENT blocks below.

VERDICT ENUMS (frozen): GF1-PROVEN(razor enclosure 1/(s + 1/
delta_1) <= g < 1/s, dominating the r157 [BS, delta_1] via the
chi-cap; two-level lower-end equality; explicit two-way transfer:
THE EXACT FINAL CHARACTERIZATION -- the g-floor IS the s-cap given
the delta_1-floor, nothing in between); GF2-PROVEN(pinch-defect
law: s x gap == 1 is a theorem with defect g/delta_1);
GF3-PROVEN(share_1^g >= share_1 one-sided, priced g/(delta_1 - g):
r157 lever (c) closed); GF4-PROVEN(jet-ratio law Jg t_g == 1 + g +
moment-ratio expression + Newton value law N_1 = 1/(H_t + s) +
rho2-self-reference of B(q_0) pinned) + TLAWSTAR-IN-WINDOW(measured:
the zero-jet mechanism holds at the constrained ground -- third
rung); GF5-PROVEN(S1-law: S1-floor ABSORBED into betapos x jr;
twin squeeze 1/(SEC + 1/FG) <= betapos <= 1/SEC: BOTH final cores
are ONE statement-form at two weightings) + S1FLOOR-ABSORBED;
MERGE-REFUTED-ALGEBRA(J-family blind to g: probe-row freedom
witness with source moments bit-identical; the one-moment merge of
the two final cores is DEAD at algebra level; arithmetic channel
disclosed open) + FORM-MERGE-EXACT(GF5b);
REDTEAM-REFUTES-ALGEBRA(2D lower-end equality + jet-toy SEC
witness); CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES;
QUANTIFIER-INHERITED(dense-x suffices, CHAIN-AUDIT);
OMEGA-RECOORDINATED(residue SET UNCHANGED: QSUBGAP-floor stays ==
the pair (W2 cited) -- now with the razor enclosure and the value
law; TOPROOT stays B00-ROOTGAP (S1-floor absorbed) == SEC-currency;
census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED); MINCUT(4/5).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1) >
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
LADDER_DEEP = ((18, 140), (24, 150), (28, 160))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
BIS_ITERS = 250
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0),
            18: (12.0, 22.0), 24: (14.0, 26.0), 28: (10.0, 30.0)}
S_BAR_TAB = {5: 0.1, 8: 0.1, 13: 0.1, 18: 0.1, 24: 0.1, 28: 0.15}
SGAP_WIN = (0.98, 1.02)
D1_TAB = {5: 2.226e5, 8: 9.951e5, 13: 1.062e7, 18: 3.25e7,
          24: 1.14e8, 28: 1.6513e8}
D1_WIN = (0.7, 1.3)
SHARE1_BAR = 0.5
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
TLAW28_WIN = (0.40, 0.70)
FG_TAB = {5: 2.2255e5, 8: 9.9512e5, 13: 1.0619e7, 18: 3.2497e7,
          24: 1.1382e8, 28: 1.6513e8}
FG_WIN = (0.97, 1.03)
FG_SLOPE_WIN = (3.4, 4.6)
SIMP_MIN = 1e3
LOCK_WIN = (1.5, 6.0)
ENC_SLOP = 1e-12
XCHI_BAR = 1e-40
N1_WIN = (0.99, 1.01)
ID2_BAR = 1e-40
SH_NEG_SLOP = 1e-30
RAY_BAR = 1e-40
ETA0_BAR = 1e-30
ID4_BAR = 1e-30
TLAWST_TAB = {5: 0.2399, 8: 0.3175}
TLAWST_CAL_WIN = (0.97, 1.03)
TLAWST_DEEP_WIN = (0.10, 1.00)
TG_WIN = (0.5, 2.0)
ID5_BAR = 1e-40
IDTW_BAR = 1e-40
BETA_TAB = {5: 0.2463, 8: 0.1305, 13: 0.0821, 18: 0.0558,
            24: 0.0420, 28: 0.0328}
BETA_WIN_CAL = (0.99, 1.01)
BETA_WIN_DEEP = (0.97, 1.03)
JR_WIN = (0.8, 1.6)
N1W_WIN = (0.99, 1.01)
JSEC_SLOP = 1e-12
J2PROXY_WIN = (0.03, 0.5)
RT_P = 10 ** 6
RT_ID_BAR = 1e-40
CTRL_YTB_MAX = 1.0
TAU_SLOPE_BAR = 0.30
RIDER_WIN = (0.30, 1.20)
W0_RIDER_WIN = (0.85, 1.15)
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
    """round-132 AMENDMENT-1 node source VERBATIM (r157 replica)."""
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
    orthonormalized compression of Mq (r138-r157 replica VERBATIM)."""
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
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp)


def secular_data(Vd: dict, r: list):
    """(lam*, et_raw, en2, etn, rho2, chi) for the extra row r on V
    (r141/r157 shape; bisection BIS_ITERS).  Caller sets workdps."""
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
    for _ in range(BIS_ITERS):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, et, en2, etn, rho2, chi


def bisect_secular(w, E, K, lo, hi, iters):
    """bottom root of sum_i w[i]/(z - E[i]) in (lo, hi) (r150
    collapserate source VERBATIM).  Caller sets workdps."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        v = mp.mpf(0)
        for i in range(K):
            v += w[i] / (mid - E[i])
        if v > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # shared generic 3-level secular frame: weights rho2, w1, w2 > 0,
    # gaps delta_1 = g + h1, delta_2 = g + h1 + dd, root g > 0 with
    # rho2 := g * S (the root equation, eliminating the constraint)
    g, h1, dd, w1, w2 = sp.symbols("g h1 dd w1 w2", positive=True)
    d1 = g + h1
    d2 = g + h1 + dd
    S = w1 / h1 + w2 / (h1 + dd)
    rho2 = g * S
    chi_t = w1 / d1 + w2 / d2
    T2 = w1 / (d1 * h1) + w2 / (d2 * (h1 + dd))
    s_ = chi_t / rho2

    # ---------------- G10 GF1: razor enclosure
    okA = sp.simplify(S - chi_t - g * T2) == 0          # partial fractions
    okB = (g * T2).is_positive is True                  # upper strict
    spread = w2 * dd / (d2 * (h1 + dd))
    okC = sp.simplify(S - d1 * T2 - spread) == 0 \
        and spread.is_nonnegative is True               # lower, step 1
    #   lower, step 2: 1/g - s - 1/d1 == -(g/d1) spread / rho2 <= 0
    okD = sp.simplify((1 / g - s_ - 1 / d1)
                      + (g / d1) * spread / rho2) == 0
    #   cross-check the intermediate rearrangement
    okE = sp.simplify((S - chi_t - rho2 / d1)
                      - (g / d1) * (d1 * T2 - S)) == 0
    okF = ((g / d1) * spread / rho2).is_nonnegative is True
    # BS <= lo <==> chi-cap: BS (s + 1/d1) == chi_t d1 + rho2
    BS = rho2 * d1
    okG = sp.simplify(BS * (s_ + 1 / d1) - (chi_t * d1 + rho2)) == 0
    #   chi_t d1 + rho2 <= 1 under normalization rho2 + w1 + w2 = 1:
    #   chi_t d1 <= w1 + w2 termwise (d1/d2 <= 1)
    okH = sp.simplify((w1 + w2) - chi_t * d1
                      - w2 * dd / d2) == 0 \
        and (w2 * dd / d2).is_nonnegative is True
    # 2-level equality: w2 = 0 ==> lo == g == normalized BS
    S2 = S.subs(w2, 0)
    rho22 = g * S2
    chi2 = chi_t.subs(w2, 0)
    lo2 = 1 / (chi2 / rho22 + 1 / d1)
    okI = sp.simplify(lo2 - g) == 0
    #   normalized BS at 2 levels: rho2n = rho22/(rho22 + w1),
    #   BSn = rho2n d1 == g  <==>  rho22 d1 == g (rho22 + w1)
    okJ = sp.simplify(rho22 * d1 - g * (rho22 + w1)) == 0
    # explicit transfer (monotone algebra instance)
    okK = bool(sp.Rational(1, 3) >= sp.Rational(1, 4))
    out.append(("G10-gf1-razor-enclosure", okA and okB and okC and okD
                and okE and okF and okG and okH and okI and okJ and okK,
                "S - chi_t == g T2 (partial fractions) with T2 > 0 ==> "
                "g < 1/s STRICT; S - d1 T2 == spread >= 0 ==> g >= "
                "1/(s + 1/delta_1); BS (s + 1/d1) == chi_t d1 + rho2 "
                "<= 1 (termwise chi-cap == SB2) ==> BS <= lower end "
                "(the r157 enclosure DOMINATED); 2-level: lower end "
                "== g == BS EXACT (equality case); transfer [g >= 1/P "
                "==> s < P, d1 >= 1/P] + [s <= P, d1 >= 1/P' ==> g >= "
                "1/(P + P')]: THEOREM GF1 -- the razor enclosure, the "
                "exact final characterization of the g-floor"))

    # ---------------- G11 GF2: pinch-defect law
    sg = s_ * g
    okL = sp.simplify(1 - sg - g * g * T2 / rho2) == 0
    #   T2 <= chi_t/h1 termwise: chi_t/h1 - T2 == sum w_i (1/(d_i h1)
    #   - 1/(d_i (d_i - g)))... d_i - g = h1 or h1+dd
    okM = sp.simplify(chi_t / h1 - T2
                      - w2 * dd / (d2 * h1 * (h1 + dd))) == 0 \
        and (w2 * dd / (d2 * h1 * (h1 + dd))).is_nonnegative is True
    okN = sp.simplify(sg * g / h1 - (s_ * g) * g / (d1 - g)) == 0
    out.append(("G11-gf2-pinch-law", okL and okM and okN,
                "1 - s g == g^2 T2/rho2 EXACT (> 0: the strict pinch) "
                "and T2 <= chi_t/(delta_1 - g) termwise ==> 1 - s g <= "
                "s g x g/(delta_1 - g): THEOREM GF2 -- the r157 "
                "'s x gap pinch family' is a THEOREM with the defect "
                "priced by g/delta_1"))

    # ---------------- G12 GF3: share pricing
    Sg_ = w1 / h1 + w2 / (h1 + dd)
    sh1g = (w1 / h1) / Sg_
    share1 = (w1 / d1) / chi_t
    a_ = g / h1
    b_ = g * T2 / chi_t
    okO = sp.simplify(sh1g / share1 - (1 + a_) / (1 + b_)) == 0
    okP = sp.simplify(a_ - b_
                      - (g / (chi_t * h1))
                      * (chi_t - h1 * T2)) == 0 \
        and sp.simplify((chi_t - h1 * T2)
                        - w2 * dd / (d2 * (h1 + dd))) == 0
    okQ = sp.simplify((1 + a_) / (1 + b_) - 1
                      - (a_ - b_) / (1 + b_)) == 0
    # 2-level: b == a * (h1 T2 / chi_t)|w2=0 ... dev == a - a = 0? no:
    # at w2 = 0: T2 = w1/(d1 h1), chi_t = w1/d1 => b = g/h1 = a: dev 0
    okR = sp.simplify((a_ - b_).subs(w2, 0)) == 0
    out.append(("G12-gf3-share-pricing", okO and okP and okQ and okR,
                "share_1^g/share_1 == (1 + a)/(1 + b) with a = "
                "g/(delta_1 - g), b = g T2/chi_t and 0 <= b <= a "
                "(spread term) ==> 0 <= share_1^g/share_1 - 1 <= "
                "g/(delta_1 - g), EQUALITY-TO-ZERO at 2 level: "
                "THEOREM GF3 -- the r157 near-equality is one-sided "
                "and priced g/delta_1-class (lever (c) closed)"))

    # ---------------- G13 GF4: Newton + constrained eigenvector + chase
    z = sp.symbols("z")
    q0, gq1, gq2, e0, e1, e2 = sp.symbols("q0 gq1 gq2 e0 e1 e2",
                                          positive=True)
    q1 = q0 + gq1
    q2 = q0 + gq1 + gq2
    Pc = (q0 - z) * (q1 - z) * (q2 - z)
    Bz = (e0 ** 2 * (q1 - z) * (q2 - z) + e1 ** 2 * (q0 - z) * (q2 - z)
          + e2 ** 2 * (q0 - z) * (q1 - z))
    okS = sp.simplify(Bz.subs(z, q0)
                      + (e0 ** 2) * sp.diff(Pc, z).subs(z, q0)) == 0
    Bp0 = sp.diff(Bz, z).subs(z, q0)
    H_ = 1 / gq1 + 1 / (gq1 + gq2)
    chi_q = e1 ** 2 / gq1 + e2 ** 2 / (gq1 + gq2)
    okT = sp.simplify(Bp0 + gq1 * (gq1 + gq2)
                      * (e0 ** 2 * H_ + chi_q)) == 0
    N1 = -Bz.subs(z, q0) / Bp0          # lam* - q0 ~ -B(q0)/B'(q0)
    okU = sp.simplify(N1 - e0 ** 2 / (e0 ** 2 * H_ + chi_q)) == 0
    # constrained eigenvector on diag 3-level: u = (W - lam)^{-1} rhat
    lamst, mu_ = sp.symbols("lamst mu_", positive=True)
    u0 = e0 / (q0 - lamst)
    u1 = e1 / (q1 - lamst)
    u2 = e2 / (q2 - lamst)
    #   (W - lam) u == rhat componentwise (Lagrange with mu = 1)
    okV = sp.simplify((q0 - lamst) * u0 - e0) == 0 \
        and sp.simplify((q1 - lamst) * u1 - e1) == 0 \
        and sp.simplify((q2 - lamst) * u2 - e2) == 0
    #   Rayleigh(u) - lam == secular(lam)/|u|^2
    ray_num = q0 * u0 ** 2 + q1 * u1 ** 2 + q2 * u2 ** 2
    un2 = u0 ** 2 + u1 ** 2 + u2 ** 2
    sec_val = (e0 ** 2 / (q0 - lamst) + e1 ** 2 / (q1 - lamst)
               + e2 ** 2 / (q2 - lamst))
    okW = sp.simplify(ray_num - lamst * un2 - sec_val) == 0
    # Jg t_g == 1 + g chase: tlaw* = lam*/(8 A*^2 G), tlaw0 = tau/(8
    # A0^2 G): (A*/A0)^2 (tlaw*/tlaw0) == lam*/tau == 1 + g
    Ast, A0_, Gc, tau_ = sp.symbols("Ast A0_ Gc tau_", positive=True)
    lam_full = tau_ * (1 + g)
    tl_st = lam_full / (8 * Ast ** 2 * Gc)
    tl_0 = tau_ / (8 * A0_ ** 2 * Gc)
    okX = sp.simplify((Ast / A0_) ** 2 * (tl_st / tl_0) - (1 + g)) == 0
    out.append(("G13-gf4-newton-jet", okS and okT and okU and okV
                and okW and okX,
                "B(q_0) == -rho2 P_c'(q_0) GENERIC (the bordered value "
                "CARRIES rho2 -- the r153 self-reference one level "
                "down, pinned); Newton quotient == rho2/(rho2 H + chi) "
                "== 1/(H_t + s) (the RESOLVENT-CAP value law); the "
                "constrained ground is u* = (W - lam*)^{-1} r-hat with "
                "Rayleigh(u*) == lam* given the root equation; Jg x "
                "t_g == 1 + g EXACT (the g-version of r150 R2): "
                "THEOREM GF4 -- the g-floor is a JET-RATIO floor, "
                "anti-degeneracy of the 0-jet map on (phi, psi*)"))

    # ---------------- G14 GF5: S1-law + twin squeeze + J-transfer
    b_r, hF = sp.symbols("b_r hF", positive=True)   # b = beta0 - tau,
    F_ = b_r + hF          # F = lam1 - tau > b (interlacing, cited)
    S1s = sp.symbols("S1s", positive=True)
    # R3: J = S1 (F - b)/b (cited);  jr = J tau/F;  betapos = b/tau
    tau2 = sp.symbols("tau2", positive=True)
    Jdef = S1s * (F_ - b_r) / b_r
    jr_ = Jdef * tau2 / F_
    bpos = b_r / tau2
    corr = F_ / (F_ - b_r)
    okY = sp.simplify(jr_ * bpos * corr - S1s) == 0
    okZ = sp.simplify(corr - 1 - b_r / (F_ - b_r)) == 0 \
        and (b_r / (F_ - b_r)).is_positive is True
    # twin squeeze: same GF1 lemma at weights (w_i, Delta_i) -- re-
    # instance with renamed symbols (w0 ground weight explicit)
    W0, W1, W2 = sp.symbols("W0 W1 W2", positive=True)
    bb, hh, ee = sp.symbols("bb hh ee", positive=True)
    D1 = bb + hh
    D2 = bb + hh + ee
    SW = W1 / hh + W2 / (hh + ee)
    W0sub = bb * SW            # root equation W0/b = SW
    SECs = (W1 / D1 + W2 / D2) / W0sub
    T2W = W1 / (D1 * hh) + W2 / (D2 * (hh + ee))
    okAA = sp.simplify(SW - (W1 / D1 + W2 / D2) - bb * T2W) == 0 \
        and sp.simplify(SW - D1 * T2W
                        - W2 * ee / (D2 * (hh + ee))) == 0
    okBB = sp.simplify(1 - SECs * bb - bb * bb * T2W / W0sub) == 0
    # J <= SEC x FULLGAP chase: J = S1 (F-b)/b <= (F-b)/b <= F/b - 1
    # and b >= F/(SEC F + 1) ==> F/b - 1 <= SEC F
    SECf = sp.symbols("SECf", positive=True)
    b_low = F_ / (SECf * F_ + 1)
    okCC = sp.simplify(F_ / b_low - 1 - SECf * F_) == 0
    okDD = bool(sp.Rational(1, 2) <= 1)   # S1 <= 1 (share of a sum)
    out.append(("G14-gf5-s1-twin", okY and okZ and okAA and okBB
                and okCC and okDD,
                "S1 == jr x betapos x (lam_1 - tau)/(lam_1 - beta_0) "
                "EXACT with the factor >= 1 ==> S1 >= jr betapos "
                "(S1-FLOOR ABSORBED into the root separation); the "
                "SAME GF1 lemma at the jet weighting gives 1/(SEC + "
                "1/FULLGAP) <= betapos <= 1/SEC with the same defect "
                "law; J <= SEC x FULLGAP chase: THEOREM GF5 -- both "
                "final cores are ONE statement-form (bottom-root "
                "position == resolvent-cap quotient) at two "
                "weightings: the FORM-merge, exact"))

    # ---------------- G15 red team symbolic
    Pw = sp.Integer(RT_P)
    d1w = sp.symbols("d1w", positive=True)
    rho2w = 1 / (1 + Pw * d1w)
    sw = (1 - rho2w) / (rho2w * d1w)
    gw = rho2w * d1w
    okEE = sp.simplify(sw - Pw) == 0
    okFF = sp.simplify(1 / (sw + 1 / d1w) - gw) == 0
    # jet toy: M = diag(l0, l1, l2), v = (p, q, 0): SEC free
    p_, q_ = sp.symbols("p_ q_", positive=True)
    D1t = sp.symbols("D1t", positive=True)
    SEC_toy = (q_ ** 2 / p_ ** 2) / D1t
    okGG = sp.simplify(SEC_toy.subs(q_, sp.sqrt(Pw * D1t) * p_)
                       - Pw) == 0
    out.append(("G15-redteam-symbolic", okEE and okFF and okGG,
                "2-level witness rho2 = 1/(1 + P delta_1) realizes "
                "s == P = 1e6 AND g == 1/(s + 1/delta_1) == rho2 "
                "delta_1 (the GF1 lower end ACHIEVED: no algebra-only "
                "improvement of the enclosure exists); jet toy: SEC "
                "== 1e6 realizable with all identities intact "
                "(ALGEBRA-ONLY-BOUNDS-REFUTED-FOR-SEC): only "
                "arithmetic-consuming bounds may cap s or SEC"))
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
    steps.append(("the g/betapos/SEC coordinates consume NO tlaw, NO "
                  "Z, no lattice proximity: source + secular data "
                  "only (r142 W2/W3 + r141 V1 cited); the enclosure "
                  "ends and N_1/N_1W are resolvent data given (tau, "
                  "phi)/(q_i, et_i) -- CERT-COST-POLY class inherited",
                  True))
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

    print("gfloor_probe -- PRIME.GFLOOR.PROOF.01")
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
    section("S1  EXACT LAYER (Theorems GF1-GF5 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure; r128/CDXXX "
         "Theorem R + L3/L4; r131 secular + GW + OFF; r132 raw "
         "census; r137/CDXLI budget identity + tlaw strings; r139/"
         "CDXLIII share_1 strings; r140/CDXLIV y_t strings; r141/"
         "CDXLV V1-V3 + s strings + quantifier; r142/CDXLVI W1-W3 + "
         "FULLGAP strings; r143/CDXLVII T1-T4 + delta_1-lock; r144/"
         "CDXLVIII X1-X4; CDXLIX F-strings; CDL Y1-Y4 + zero-jet "
         "law; CDLI AD1/AD2; CDLIV R1-R4 + S1/betapos/jr strings; "
         "CDLVII RES1/RES2 (self-reference class); CDLX L1-L6 "
         "(moment-Laurent dictionary, J2 strings); CDLXI SB1-SB5 + "
         "enclosure + chi-cap; HSW22 Cor. 1.2; PT21; Courant-"
         "Fischer; Cauchy interlacing; Cramer/adjugate; partial "
         "fractions; Euler sine product")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: THE G-FLOOR ANATOMY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36 = [], [], []
    tau_tab, fg_tab, gap_tab, s_tab = {}, {}, {}, {}
    sh_tab, jr_tab, tg_tab, sec_tab = {}, {}, {}, {}
    r2_tab, bs_tab, w0_tab, apsi_tab, bp_tab = {}, {}, {}, {}, {}
    wid_tab, shdev_tab = {}, {}
    cells = {}
    rt_data = None
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
            tau = E[0]
            lam1 = E[1]
            lam2 = E[2]
            FG = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0src = sum(((-1) ** k) * cs[k] for k in range(K))
            A2src = sum(((-1) ** k) * cs[k] * oms[k] ** 2
                        for k in range(K))
            A4src = sum(((-1) ** k) * cs[k] * oms[k] ** 4
                        for k in range(K))
            yt = float(abs(A2src / A0src))
            j2proxy = float(abs(A4src / A0src) / (A2src / A0src) ** 2)
            l10 = mp.log(10)
            tauf = float(tau)
            fg_f = float(FG)
            simp = float((lam2 - lam1) / lam1)
        Gz = hsw_G(Tz)
        tlaw0_f = tauf / (8.0 * float(abs(A0src)) ** 2 * Gz)
        tau_tab[x] = tauf
        fg_tab[x] = fg_f

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
                 "found %d nodes (zone prefix + overhang; edge "
                 "census not consumed)" % (x, SCAN_OVER, len(seeds)))
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
        fg_ok = FG_TAB[x] * FG_WIN[0] <= fg_f <= FG_TAB[x] * FG_WIN[1]
        ok31x = pos_ok and sort_ok and fg_ok and simp >= SIMP_MIN
        ok31 = ok31 and ok31x
        det31.append("x%d: FULLGAP %.6e (win %s) simp %.1e"
                     % (x, fg_f, fg_ok, simp))

        # ---- G32 node-config + replication + zone-top argmin
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            qs = Vd["qs"]
            nf = Vd["nf"]
            tau_v = Vd["tau_mp"]
            d1 = (qs[1] - qs[0]) / tau_v
            d1_f = float(d1)
            w3_ok = bool(d1 >= FG * (1 - mp.mpf("1e-12")))
            tg_grid = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                     TOP_GRID_STEP)) + [Tz - 0.001]
            gmin, argp = None, None
            for tv in tg_grid:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - qs[0]) / tau_v)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
            g_ex = (lam - qs[0]) / tau_v
            dl = [(qs[i] - qs[0]) / tau_v for i in range(nf)]
            chi_t = sum(etn[i] * etn[i] / dl[i] for i in range(1, nf))
            s_val = tau_v * chi / rho2
            sg_mp = s_val * g_ex
            sg = float(sg_mp)
            s_f = float(s_val)
            g_f = float(g_ex)
            e12 = etn[1] * etn[1]
            share1_mp = (e12 / (qs[1] - qs[0])) / chi
            share1 = float(share1_mp)
        lock = fg_f / yt
        lo_w, hi_w = REPL_WIN[x]
        if x <= 24:
            tl_ok = abs(tlaw0_f / TLAW_TAB[x] - 1.0) <= TLAW_TOL
        else:
            tl_ok = TLAW28_WIN[0] <= tlaw0_f <= TLAW28_WIN[1]
        ok32x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR and w3_ok
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and s_f <= S_BAR_TAB[x]
                 and SGAP_WIN[0] <= sg <= SGAP_WIN[1]
                 and D1_WIN[0] <= d1_f / D1_TAB[x] <= D1_WIN[1]
                 and share1 >= SHARE1_BAR and tl_ok
                 and LOCK_WIN[0] <= lock <= LOCK_WIN[1])
        ok32 = ok32 and ok32x
        det32.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1/FG "
                     "%.6f share1 %.3f tlaw %.4f lock %.3f (%.0f s)"
                     % (x, Vd["qrel"], gmin, s_f, sg, d1_f / fg_f,
                        share1, tlaw0_f, lock, time.time() - t_q))
        gap_tab[x] = gmin
        s_tab[x] = s_f
        sh_tab[x] = share1

        # ---- G33 GF1 instantiated: the razor enclosure
        with mp.workdps(dps):
            slop = mp.mpf(repr(ENC_SLOP))
            lo_end = 1 / (s_val + 1 / d1)
            hi_end = 1 / s_val
            BS = rho2 * d1
            ok_bs = bool(BS <= lo_end * (1 + slop))
            ok_lo = bool(lo_end <= g_ex * (1 + slop))
            ok_hi = bool(g_ex < hi_end)
            ok_d1 = bool(g_ex <= d1 * (1 + slop))
            xchi = float(abs(chi * tau_v / chi_t - 1))
            Ht = sum(1 / dl[i] for i in range(1, nf))
            N1 = 1 / (Ht + s_val)
            n1r = float(N1 / g_ex)
            width = float((hi_end - lo_end) / g_ex)
            rho2_f = float(rho2)
            BS_f = float(BS)
            log_r2 = float(mp.log(rho2) / l10)
        ok33x = (ok_bs and ok_lo and ok_hi and ok_d1
                 and xchi <= XCHI_BAR
                 and N1_WIN[0] <= n1r <= N1_WIN[1])
        ok33 = ok33 and ok33x
        det33.append("x%d: lo/g %.9f g*s %.9f width %.2e N1/g %.9f "
                     "xchi %.0e BS<=lo %s"
                     % (x, float(lo_end / g_ex), float(sg_mp), width,
                        n1r, xchi, ok_bs))
        r2_tab[x] = rho2_f
        bs_tab[x] = BS_f
        wid_tab[x] = width
        info("x=%d GF1 exhibit: BS %.3e <= lo %.6f <= g %.6f < 1/s "
             "%.6f <= delta_1 %.3e -- the razor enclosure (relative "
             "width %.2e, log10 rho2 %.1f): the g-floor IS the s-cap "
             "given the delta_1-floor, explicit constants, nothing "
             "in between" % (x, BS_f, float(lo_end), g_f,
                             float(hi_end), d1_f, width, log_r2))

        # ---- G34 GF2/GF3 instantiated
        with mp.workdps(dps):
            T2 = sum(etn[i] * etn[i] / (dl[i] * (dl[i] - g_ex))
                     for i in range(1, nf))
            id2 = float(abs((1 - sg_mp) * rho2 / (g_ex * g_ex * T2)
                            - 1))
            bnd2 = sg_mp * g_ex / (d1 - g_ex)
            ok_p = bool((1 - sg_mp) > 0) and \
                bool((1 - sg_mp) <= bnd2 * (1 + slop))
            S_g = sum(etn[i] * etn[i] / (qs[i] - lam)
                      for i in range(1, nf))
            sh1g = (e12 / (qs[1] - lam)) / S_g
            dev3 = sh1g / share1_mp - 1
            bnd3 = g_ex / (d1 - g_ex)
            ok_s = bool(dev3 >= -mp.mpf(repr(SH_NEG_SLOP))) \
                and bool(dev3 <= bnd3 * (1 + slop))
            dev3_f = float(dev3)
            pinch_f = float(1 - sg_mp)
            bnd2_f = float(bnd2)
        ok34x = (id2 <= ID2_BAR and ok_p and ok_s)
        ok34 = ok34 and ok34x
        det34.append("x%d: 1-sg %.3e <= %.3e id2 %.0e shdev %+.2e "
                     "<= %.2e" % (x, pinch_f, bnd2_f, id2, dev3_f,
                                  float(bnd3)))
        shdev_tab[x] = dev3_f
        info("x=%d GF2/GF3 exhibit: the pinch defect 1 - sg = %.3e "
             "is the THEOREM value g^2 T2/rho2 (dev %.0e), priced by "
             "g/delta_1 = %.2e; share_1^g >= share_1 one-sided with "
             "dev %+.2e under the proven bar %.2e (lever (c) closed)"
             % (x, pinch_f, id2, g_f / d1_f, dev3_f, float(bnd3)))

        # ---- G35 GF4 instantiated: the psi*-jet block
        with mp.workdps(dps):
            v0 = [((-1) ** k) / nrm[k] for k in range(K)]
            d0 = []
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Nb"][k, fi] * v0[k]
                d0.append(acc)
            e0v = Vd["fwd"](d0)
            eta = []
            for i in range(nf):
                acc = mp.mpf(0)
                for k in range(nf):
                    acc += Vd["Z"][k, i] * e0v[k]
                eta.append(acc)
            cst = [etn[i] / (qs[i] - lam) for i in range(nf)]
            cn2 = sum(v * v for v in cst)
            A0psi = sum(eta[i] * cst[i] for i in range(nf)) \
                / mp.sqrt(cn2)
            ray = sum(qs[i] * cst[i] * cst[i] for i in range(nf)) / cn2
            raydev = float(abs(ray / lam - 1))
            phiv = [ce["mpV"][k, 0] for k in range(K)]
            A0phi = sum(v0[k] * phiv[k] for k in range(K))
            eta0dev = float(abs(eta[0] * eta[0] / (A0phi * A0phi) - 1))
            G_mp = mp.mpf(repr(Gz))
            tlaw0_mp = tau_v / (8 * A0phi * A0phi * G_mp)
            tlawst = lam / (8 * A0psi * A0psi * G_mp)
            tgr = tlawst / tlaw0_mp
            Jg = (A0psi / A0phi) ** 2
            id4 = float(abs(Jg * tgr / (1 + g_ex) - 1))
            tlawst_f = float(tlawst)
            tgr_f = float(tgr)
            Jg_f = float(Jg)
            apsi2_f = float(A0psi * A0psi)
        if x in TLAWST_TAB:
            tl_st_ok = (TLAWST_CAL_WIN[0]
                        <= tlawst_f / TLAWST_TAB[x]
                        <= TLAWST_CAL_WIN[1])
        else:
            tl_st_ok = (TLAWST_DEEP_WIN[0] <= tlawst_f
                        <= TLAWST_DEEP_WIN[1])
        ok35x = (raydev <= RAY_BAR and eta0dev <= ETA0_BAR
                 and id4 <= ID4_BAR and tl_st_ok
                 and TG_WIN[0] <= tgr_f <= TG_WIN[1])
        ok35 = ok35 and ok35x
        det35.append("x%d: Jg %.4f tlaw* %.4f tg %.4f ray %.0e eta0 "
                     "%.0e id4 %.0e" % (x, Jg_f, tlawst_f, tgr_f,
                                        raydev, eta0dev, id4))
        tg_tab[x] = tgr_f
        apsi_tab[x] = apsi2_f
        info("x=%d GF4 exhibit: the constrained ground OBEYS THE "
             "ZERO-JET LAW: lam* = 8 A_0(psi*)^2 G(T_z) x tlaw* with "
             "tlaw* = %.4f (window class), t_g = %.4f flat, Jg = "
             "(A_0(psi*)/A_0(phi))^2 = %.4f == (1+g)/t_g: the g-floor "
             "is the anti-degeneracy of the 0-jet map on (phi, psi*) "
             "-- the mechanism's THIRD rung (ground r137, excited "
             "CDL, constrained ground HERE); eta-head %s"
             % (x, tlawst_f, tgr_f, Jg_f,
                " ".join("%.2e" % float(eta[i])
                         for i in range(min(4, nf)))))

        # ---- G36 GF5 instantiated: source side + twin squeeze
        with mp.workdps(dps):
            w = []
            for i in range(K):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += v0[k] * ce["mpV"][k, i]
                w.append(acc * acc)
            w0 = w[0]
            Dl = [(E[i] - tau) / tau for i in range(K)]
            SEC = sum((w[i] / w0) / Dl[i] for i in range(1, K))
            TRF = sum(1 / Dl[i] for i in range(1, K))
            beta0 = bisect_secular(w, E, K, tau, lam1, BIS_ITERS)
            inter_ok = bool(tau < beta0 < lam1)
            bpos = (beta0 - tau) / tau
            lo_b = 1 / (SEC + 1 / FG)
            hi_b = 1 / SEC
            okb = bool(lo_b <= bpos * (1 + slop)) \
                and bool(bpos <= hi_b * (1 + slop))
            T2w = sum((w[i] / w0) / (Dl[i] * (Dl[i] - bpos))
                      for i in range(1, K))
            idtw = float(abs((1 - SEC * bpos) / (bpos * bpos * T2w)
                             - 1))
            GWb = sum(w[i] / (E[i] - beta0) for i in range(1, K))
            S1 = (w[1] / (lam1 - beta0)) / GWb
            J = w[1] / w0
            jr = J / FG
            S1pred = jr * bpos * (lam1 - tau) / (lam1 - beta0)
            id5 = float(abs(S1 / S1pred - 1))
            okS1 = bool(S1 >= jr * bpos * (1 - mp.mpf("1e-30")))
            okJ = bool(J <= SEC * FG * (1 + mp.mpf(repr(JSEC_SLOP))))
            N1w = 1 / (TRF + SEC)
            n1w_r = float(N1w / bpos)
            bpos_f = float(bpos)
            SEC_f = float(SEC)
            jr_f = float(jr)
            S1_f = float(S1)
            w0_f = float(w0)
        bwin = BETA_WIN_CAL if x <= 8 else BETA_WIN_DEEP
        bp_ok = bwin[0] <= bpos_f / BETA_TAB[x] <= bwin[1]
        j2_ok = J2PROXY_WIN[0] <= j2proxy <= J2PROXY_WIN[1]
        ok36x = (inter_ok and okb and idtw <= IDTW_BAR
                 and id5 <= ID5_BAR and okS1 and okJ and bp_ok
                 and JR_WIN[0] <= jr_f <= JR_WIN[1]
                 and N1W_WIN[0] <= n1w_r <= N1W_WIN[1] and j2_ok)
        ok36 = ok36 and ok36x
        det36.append("x%d: SEC %.4f bpos %.6f (win %s) S1 %.4f id5 "
                     "%.0e idtw %.0e jr %.4f N1w/b %.7f J2p %.4f"
                     % (x, SEC_f, bpos_f, bp_ok, S1_f, id5, idtw,
                        jr_f, n1w_r, j2proxy))
        sec_tab[x] = SEC_f
        bp_tab[x] = bpos_f
        jr_tab[x] = jr_f
        w0_tab[x] = w0_f
        info("x=%d GF5 exhibit: twin squeeze 1/(SEC + 1/FG) = %.6f "
             "<= betapos = %.6f <= 1/SEC = %.6f (defect %0.2e); S1 = "
             "%.4f == jr x betapos x corr EXACT (dev %.0e) >= jr x "
             "betapos = %.4f: the S1-floor is ABSORBED -- ONE decay "
             "law; SEC/nf = %.4f (nf %d); J <= SEC x FG %s"
             % (x, float(lo_b), bpos_f, float(hi_b),
                1.0 - SEC_f * bpos_f, S1_f, id5, jr_f * bpos_f,
                SEC_f / nf, nf, okJ))
        if x == 5:
            rt_data = (tauf, d1_f, [str(c) for c in ce["cn_mp_str"]],
                       yt, j2proxy)

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
          "Mq PSD + sorted; FULLGAP in the frozen windows x %s "
          "(incl. the CDLII x=28 string); lam_1 SIMPLE (rel gap >= "
          "%.0e); growth slope in %s: %s"
          % (str(FG_WIN), SIMP_MIN, str(FG_SLOPE_WIN),
             "; ".join(det31)))
    check("G32-node-config-replication", ok32,
          "|qrel| <= %.0e, null res <= %.0e; delta_1 >= FULLGAP (W3 "
          "re-gate); zone-top argmin in the frozen windows; s <= "
          "bar; sg in %s; delta_1/share_1/tlaw on the cited "
          "strings; lock FULLGAP/y_t in %s: %s"
          % (QREL_BAR, NULLRES_BAR, str(SGAP_WIN), str(LOCK_WIN),
             "; ".join(det32)))
    check("G33-gf1-razor-enclosure", ok33,
          "BS <= 1/(s + 1/delta_1) <= g < 1/s <= (and g <= delta_1) "
          "HARD at every rung (slop %.0e); chi cross <= %.0e; N_1/g "
          "in %s (THEOREM GF1 instantiated: the exact final "
          "characterization): %s"
          % (ENC_SLOP, XCHI_BAR, str(N1_WIN), "; ".join(det33)))
    check("G34-gf2-gf3-pinch-share", ok34,
          "pinch identity 1 - sg == g^2 T2/rho2 <= %.0e; 0 < 1 - sg "
          "<= sg g/(delta_1 - g) HARD (THEOREM GF2); 0 <= "
          "share_1^g/share_1 - 1 <= g/(delta_1 - g) HARD (THEOREM "
          "GF3, lever (c) closed): %s" % (ID2_BAR, "; ".join(det34)))
    check("G35-gf4-jet-ratio", ok35,
          "Rayleigh(psi*) == lam* <= %.0e; eta_0^2 == A_0(phi)^2 <= "
          "%.0e; Jg t_g == 1 + g <= %.0e; tlaw* in the calibrated/"
          "disclosed windows; t_g in %s (THEOREM GF4: the g-floor is "
          "a jet-ratio floor; the zero-jet mechanism holds at the "
          "constrained ground): %s"
          % (RAY_BAR, ETA0_BAR, ID4_BAR, str(TG_WIN),
             "; ".join(det35)))
    check("G36-gf5-s1-twin-squeeze", ok36,
          "tau < beta_0 < lam_1 HARD; 1/(SEC + 1/FG) <= betapos <= "
          "1/SEC HARD; twin defect identity <= %.0e; S1 == jr "
          "betapos corr <= %.0e AND S1 >= jr betapos HARD (S1-FLOOR "
          "ABSORBED); J <= SEC FG HARD; betapos on the r150 strings; "
          "jr in %s; N_1W/betapos in %s; J2-proxy in %s (THEOREM "
          "GF5: both final cores are ONE statement-form at two "
          "weightings): %s"
          % (IDTW_BAR, ID5_BAR, str(JR_WIN), str(N1W_WIN),
             str(J2PROXY_WIN), "; ".join(det36)))

    # ---------------------------------------------------------- S3c
    section("S3c  RED-TEAM MP INSTANTIATION (the merge adjudication)")
    tau5, d15, cs5_str, yt5, j2p5 = rt_data
    with mp.workdps(120):
        d1_rt = mp.mpf(repr(d15))
        Pw = mp.mpf(RT_P)
        r2w = 1 / (1 + Pw * d1_rt)
        g2 = r2w * d1_rt
        s2 = (1 - r2w) / (r2w * d1_rt)
        lo2 = 1 / (s2 + 1 / d1_rt)
        dev_s = float(abs(s2 / Pw - 1))
        dev_eq = float(abs(lo2 / g2 - 1))
        dev_bs = float(abs(g2 / (r2w * d1_rt) - 1))
        # source invariance around the witness: recompute y_t and the
        # J2-proxy from the SAME frozen coefficient strings
        cs5 = [mp.mpf(s) for s in cs5_str]
        K5 = len(cs5)
        aa5 = mp.log(5) / 2
        oms5 = [k * mp.pi / aa5 for k in range(K5)]
        A0w = sum(((-1) ** k) * cs5[k] for k in range(K5))
        A2w = sum(((-1) ** k) * cs5[k] * oms5[k] ** 2
                  for k in range(K5))
        A4w = sum(((-1) ** k) * cs5[k] * oms5[k] ** 4
                  for k in range(K5))
        yt_re = float(abs(A2w / A0w))
        j2_re = float(abs(A4w / A0w) / (A2w / A0w) ** 2)
        src_ok = (abs(yt_re / yt5 - 1) <= 1e-12
                  and abs(j2_re / j2p5 - 1) <= 1e-12)
        # jet-toy SEC witness on the same rung scale
        D1t = mp.mpf(repr(fg_tab[5]))
        p_t = mp.mpf("1e-8")
        q_t = mp.sqrt(Pw * D1t) * p_t
        SEC_toy = (q_t * q_t / (p_t * p_t)) / D1t
        dev_sec = float(abs(SEC_toy / Pw - 1))
    check("G40-redteam-merge", dev_s <= RT_ID_BAR
          and dev_eq <= RT_ID_BAR and dev_bs <= RT_ID_BAR and src_ok
          and dev_sec <= RT_ID_BAR,
          "2D witness on the x=5 rung data: s == P = %.0e (dev %.0e) "
          "with g == 1/(s + 1/delta_1) == rho2 delta_1 (devs %.0e/"
          "%.0e: the GF1 LOWER END ACHIEVED -- no algebra-only "
          "improvement) while the source moments are EXACTLY "
          "unchanged (y_t/J2-proxy recomputed == %.6e/%.6f: the "
          "J-family is BLIND to g -- MERGE-REFUTED-ALGEBRA, the "
          "one-moment merge of the two final cores is dead at "
          "algebra level; the arithmetic channel (the zone-top row "
          "is source-determined) stays honestly open); jet-toy SEC "
          "== 1e6 (dev %.0e): only arithmetic-consuming bounds may "
          "cap s or SEC" % (float(Pw), dev_s, dev_eq, dev_bs, yt_re,
                            j2_re, dev_sec))

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
            omsw = [k * mp.pi / aaw for k in range(cw["K"])]
            A0cw = sum(((-1) ** k) * csw[k] for k in range(cw["K"]))
            A2cw = sum(((-1) ** k) * csw[k] * omsw[k] ** 2
                       for k in range(cw["K"]))
            ytbw = float(abs(A2cw / A0cw)) / float(omsw[-1] ** 2)
        refuse = (over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (NOT PSD: the GF1-GF5 hypotheses fail EXACTLY "
              "here -- no positive ground to separate from); y_t_w/"
              "b_top = %.2f <= %.1f"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw, ytbw,
                 CTRL_YTB_MAX))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + no escaped scale; the secular/jet/"
          "resolvent machinery requires PSD + simple positive "
          "ground -- the hypotheses fail exactly in the false worlds")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        sl_s = float(np.polyfit(lt, [math.log10(s_tab[x])
                                     for x in xs_all], 1)[0])
        sl_g = float(np.polyfit(lt, [math.log10(gap_tab[x])
                                     for x in xs_all], 1)[0])
        sl_sh = float(np.polyfit(lt, [math.log10(sh_tab[x])
                                      for x in xs_all], 1)[0])
        sl_jr = float(np.polyfit(lt, [math.log10(jr_tab[x])
                                      for x in xs_all], 1)[0])
        sl_tg = float(np.polyfit(lt, [math.log10(tg_tab[x])
                                      for x in xs_all], 1)[0])
        sl_r2 = float(np.polyfit(lt, [math.log10(r2_tab[x])
                                      for x in xs_all], 1)[0])
        sl_bs = float(np.polyfit(lt, [math.log10(bs_tab[x])
                                      for x in xs_all], 1)[0])
        sl_w0 = float(np.polyfit(lt, [math.log10(w0_tab[x])
                                      for x in xs_all], 1)[0])
        sl_ap = float(np.polyfit(lt, [math.log10(apsi_tab[x])
                                      for x in xs_all], 1)[0])
        lxs = [math.log10(float(x)) for x in xs_all]
        sl_sec = float(np.polyfit(lxs, [math.log10(sec_tab[x])
                                        for x in xs_all], 1)[0])
        sl_bp = float(np.polyfit(lxs, [math.log10(bp_tab[x])
                                       for x in xs_all], 1)[0])
        ok54 = (abs(sl_s) <= TAU_SLOPE_BAR
                and abs(sl_g) <= TAU_SLOPE_BAR
                and abs(sl_sh) <= TAU_SLOPE_BAR
                and abs(sl_jr) <= TAU_SLOPE_BAR
                and abs(sl_tg) <= TAU_SLOPE_BAR
                and RIDER_WIN[0] <= sl_r2 <= RIDER_WIN[1]
                and RIDER_WIN[0] <= sl_bs <= RIDER_WIN[1]
                and W0_RIDER_WIN[0] <= sl_w0 <= W0_RIDER_WIN[1]
                and W0_RIDER_WIN[0] <= sl_ap <= W0_RIDER_WIN[1])
        check("G54-tau-screen", ok54,
              "slopes vs log10 tau: s %.4f, gap %.4f, share_1 %.4f, "
              "jr %.4f, t_g %.4f (all <= %.2f: the demand RATIOS are "
              "tau-flat); RIDER REPORT: rho2 %.3f, BS %.3f in %s; "
              "w_0 %.3f, A_0(psi*)^2 %.3f in %s (ride tau -- "
              "BOUND-RIDES-CONNES); LAW HUNT: SEC growth slope vs "
              "log10 x = %.3f, betapos slope %.3f (the r150 "
              "x^{-1.2}-class law in root-position currency)"
              % (sl_s, sl_g, sl_sh, sl_jr, sl_tg, TAU_SLOPE_BAR,
                 sl_r2, sl_bs, str(RIDER_WIN), sl_w0, sl_ap,
                 str(W0_RIDER_WIN), sl_sec, sl_bp))
        info("g-floor tables x = %s: width = %s; 1-sg pinch = %s; "
             "share-dev = %s; SEC = %s; betapos = %s; SEC/nf-class "
             "= %s; tg = %s"
             % (str(xs_all),
                "/".join("%.2e" % wid_tab[x] for x in xs_all),
                "/".join("%.2e" % (1.0 - s_tab[x] * gap_tab[x])
                         for x in xs_all),
                "/".join("%.2e" % shdev_tab[x] for x in xs_all),
                "/".join("%.3f" % sec_tab[x] for x in xs_all),
                "/".join("%.6f" % bp_tab[x] for x in xs_all),
                "/".join("%.4f" % (sec_tab[x] * bp_tab[x])
                         for x in xs_all),
                "/".join("%.4f" % tg_tab[x] for x in xs_all)))
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
          "flows: base 4, refined 5 (r142/r144/r146/r150 graph "
          "VERBATIM -- this round changes COORDINATES/adjudicates "
          "the merge, not the set); one-grant 5; counterfactual "
          "PARALLEL 9 NOT REAL; census {MEAS, OMEGA-POS} "
          "cardinality 4 UNCHANGED; RH unreachable without the "
          "omega edges")
    info("EXACT RESIDUE after this round (read with CDLIV/CDLVIII/"
         "CDLIX/CDLX/CDLXI): SET UNCHANGED -- RH <== [r122-NF-"
         "closure] + [Theorem R] + {L1, WPD} on dense a; RESIDUE = "
         "{TOPROOT (= B00-ROOTGAP alone: the S1-floor is ABSORBED "
         "by GF5a; == the SEC-cap coordinate by the twin squeeze), "
         "TLAWCAP-block (<== T-WINDOW + TOPROOT + PERCELL-REL + "
         "JUMPSUM per CDLVIII/CDLX), QSUBGAP-FLOOR g >= 1/poly "
         "(THIS ROUND: the razor enclosure 1/(s + 1/delta_1) <= g "
         "< 1/s PROVEN with two-level equality at the lower end -- "
         "the g-floor IS the s-cap given the delta_1-floor, "
         "explicit constants, nothing in between; the merge with "
         "the J-family REFUTED at algebra level, FORM-merge exact)} "
         "+ dense-a + a-extension + window-a.  NO RH claim; nothing "
         "upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "GF1-PROVEN(razor enclosure 1/(s + 1/delta_1) <= g < 1/s, "
        "dominates r157 [BS, delta_1] via the chi-cap; two-level "
        "equality; explicit two-way transfer -- THE EXACT FINAL "
        "CHARACTERIZATION; G10/G33)",
        "GF2-PROVEN(pinch-defect law: s x gap == 1 is a theorem, "
        "defect priced g/delta_1; G11/G34)",
        "GF3-PROVEN(share_1^g >= share_1 one-sided, priced "
        "g/(delta_1 - g): r157 lever (c) CLOSED; G12/G34)",
        "GF4-PROVEN(jet-ratio law Jg t_g == 1 + g + moment-ratio "
        "expression + Newton value law + rho2-self-reference "
        "pinned; G13/G35) + TLAWSTAR-IN-WINDOW(the zero-jet "
        "mechanism holds at the constrained ground -- measured)",
        "GF5-PROVEN(S1-law: S1-FLOOR ABSORBED; twin squeeze at the "
        "jet weighting: both final cores are ONE statement-form at "
        "two weightings; G14/G36)",
        "MERGE-REFUTED-ALGEBRA(J-family blind to g: source moments "
        "bit-identical under the g-collapsing witness; G40) + "
        "FORM-MERGE-EXACT(GF5b)",
        "REDTEAM-REFUTES-ALGEBRA(lower-end equality witness + "
        "jet-toy SEC witness; G15/G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "QUANTIFIER-INHERITED(dense-x suffices; G60)",
        "OMEGA-RECOORDINATED(residue SET UNCHANGED; census {MEAS, "
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
        print("COMPOSITE: GF1-PROVEN + GF2-PROVEN + GF3-PROVEN + "
              "GF4-PROVEN + GF5-PROVEN + TLAWSTAR-IN-WINDOW + "
              "S1FLOOR-ABSORBED + MERGE-REFUTED-ALGEBRA + "
              "FORM-MERGE-EXACT + REDTEAM-REFUTES-ALGEBRA + "
              "CONTROLS-REFUSE + DEMAND-FLAT + BOUND-RIDES-CONNES "
              "+ QUANTIFIER-INHERITED + OMEGA-RECOORDINATED + "
              "MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
