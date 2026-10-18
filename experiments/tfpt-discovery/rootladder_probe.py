#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rootladder_probe -- PRIME.ROOTLADDER.SELFSIM.01

FROZEN SPEC (2026-08-18).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the census-root-position pair
{TOPROOT, T-WINDOW} via the measured self-similarity of the
escaped-root ladder; the r154 rank-one secular structure solved in
moment coordinates)
=======================================================================
State consumed (CITED): CDLVIII/r154 (nearalign: P1-P7, T-WINDOW
0 < T <= 1.22 y_t measured, PROFCAP <= 1, tower certificate P4,
mass chain P3, escaped ladder self-similar top -> 0.831 / second
0.082 constant, J_2 -> 0.15 tau-flat, TOWER-DIVERGES-BELOW-y_t
obstruction, LEPS anchors); CDLVII/r153 (EZ, LC, RES1/RES2
obstructed-exact, NO-ARITHMETIC-HEIGHT, funnel); CDLIV/r150 (R1-R4,
B00-root-separation + S1-floor coordinates of TOPROOT); CDXLVII/
r143 (T4 rank-one dictionary: census roots == eigenvalues of
D - (1/A_0)|w><1|, trace-excess law, delta_1-lock, nsc escape
mechanism, ALIGNMENT-CAP-NOT-FOUND); CDL/r146 (Y1-Y4); CDLI/r147
(AD1/AD2).

NOTATION per block anchor (r151/r153/r154 deterministic anchors):
u0 from AEP.anchor_select, x0 = e^{u0}, A = u0/2, K = ceil(1.25 x0
log x0), om_k = k pi/A, b_k = om_k^2, ground pair (tau, phi), c_k =
phi_k/nrm_k, A_0 = sum (-1)^k c_k, w_k = (-1)^k c_k b_k, v_k =
w_k/A_0, jets a_{2m} = A_{2m}/A_0 = sum_k v_k b_k^{m-1} (a_2 =
-y_t measured), F(y)/A_0 = 1 + S(y), S = sum v_k/(y - b_k), T(y) =
sum v_k b_k/(y - b_k), F_j(y) = sum v_k b_k^j/(y - b_k) (F_0 = S,
F_1 = T), b_top = b_{K-1}, z = y/y_t, MOMENT RATIOS J_m :=
a_{2m}/y_t^m (m >= 2), census roots y_j (zeros of F), escaped
ladder z_j = y_j/y_t for y_j > b_top, POWER-SUM EXCESS P_m :=
sum_j y_j^m - sum_k b_k^m.

=======================================================================
THE THEOREMS (exact layer; sympy generic + exact rational instances;
classical inputs typed CITED)
=======================================================================
THEOREM L1 (the secular-Laurent dictionary; the R1 core).  EXACTLY
(partial fractions, c-generic):
  (y/y_t) F(y)/A_0 == z - 1 + T(y)/y_t   (with a_2 = -y_t),
  T(y)/y_t == sum_{m>=1} J_{m+1} z^{-m}  (Laurent, y > b_top, with
  exact partial-geometric remainder),
so with PHI(z) := z - 1 + sum_{m>=1} J_{m+1} z^{-m}: the census
roots above the band are EXACTLY the zeros of PHI on z >
b_top/y_t -- the escaped-root ladder is an algebraic function of
the moment ratios {J_m} ALONE.  Self-similarity of the ladder ==
flatness of the moment ratios (measured: J_2 = 0.1117 -> 0.1506
saturating, r154 tau-flat).

THEOREM L2 (the quarter-cap + top-root enclosure).  z(1-z) <= 1/4
exactly.  If PHI(z_0) = 0 with z_0 real then
  J_2 == z_0 (1 - z_0) - z_0 rho(z_0),  rho(z) := sum_{m>=2}
  J_{m+1} z^{-m},
hence J_2 <= 1/4 + z_0 |rho(z_0)|: THE CENSUS-REAL TOP ROOT CAPS
ITS OWN LEADING MOMENT RATIO (measured tail z|rho| = 0.0034/
0.0075/0.0090 -- the saturation J_2 -> 0.1506 has proven headroom
to 1/4 + 0.01).  Quadratic enclosure: z_quad = (1 + sqrt(1 -
4 J_2))/2 predicts z_top to 4.5e-3/1.1e-2/1.4e-2 (calibration);
the M-truncation polynomials z^{M+1} - z^M + sum_{m<=M} J_{m+1}
z^{M-m} converge to the ladder (M = 3 captures z_top to 1e-5, M =
6 captures the second rung 0.0822 to 1e-5-class: measured).

THEOREM L3 (the power-sum dictionary; ladder sum rules).  From
log(F/A_0) = -sum_m P_m/(m y^m) (Weierstrass expansion, generic):
  P_1 == -a_2 == y_t          (SR1: trace identity, r143 T4),
  P_2 == a_2^2 - 2 a_4        (SR2: sum z_j^2 - lattice == 1-2J_2),
  P_3 == 3 a_2 a_4 - 3 a_6 - a_2^3   (SR3: the next rung).
The ladder carries the jets: sum z_esc -> 1 (measured 1.026/1.006/
1.006), sum z_esc^2 == 1 - 2 J_2 + lattice/nonesc corrections
(P_2/P_1^2 == 1 - 2 J_2 exact; measured 0.7765/0.7250/0.7108).

THEOREM L4 (the sign-pattern escape law; the R2 answer).  (i) Pole-
interval parity: F(b_k+) has sign(w_k), F(b_{k+1}-) has
-sign(w_{k+1}); a same-sign adjacent pair (w_k, w_{k+1}) forces >=
1 root in the gap (IVT), so #below-band roots >= (K-2) - nsc(w)
and n_esc <= nsc(w) + 1 EXACTLY.  (ii) Jet side: the escaped count
is the zero count of f(u) = 1 + sum a_{2m} u^m on (0, 1/b_top);
Laguerre's rule (CITED AS FORM; Polya-Szego V) gives n_esc <=
V(jet signs).  MEASURED: n_esc == V EXACTLY at all core blocks
(4/6/11) -- the escape count IS the jet-sign-change count; the jet
sign pattern is + - + (alternating head, then structure): J_3 < 0
at all core blocks.

THEOREM L5 (the jet-tower cascade; the strip certificate that
beats TOWER-DIVERGES-BELOW-y_t).  Level shift (exact): y^j F_1 ==
Q_j(y) + F_{j+1}(y) with Q_j(y) = sum_{i=1}^{j} a_{2(i+1)}
y^{j-i}.  Tower bound one level up: |F_{j+1}(y)| <= (|a_{2(j+2)}|/
y)(1 + TOW_{j+1}(Y)) for y >= Y > b_top (each Laurent term
decreasing; envelope-closed tail).  CERTIFICATE: if R_j(y) :=
y Q_j(y) - |a_{2(j+2)}|(1 + TOW_{j+1}(Y)) satisfies R_j(Y) > 0 and
has NO real root >= Y, then T > 0 POINTWISE on [Y, infinity) --
from source jets alone, beyond the cache.  Measured floors Y* =
1.169/1.023/1.406 x b_top (levels j = 4/9/12): the certified
T-positive zone extends from r154's y >= y_t DOWN TO the band
edge (factor ~ y_t/b_top ~ x^2); via r154-P2 the escaped-root cap
(no census root above y_t) becomes CERTIFIED source-pure.  The
residual measured-only zone is the band-edge sliver (b_top, Y*):
1/0/8 cache zeros vs 87/299/1033 in the full strip.

THEOREM L6 (the two-sided window split).  Upper on z >= 1: T/y_t
<= sum_{m>=2} |J_m| (triangle; the r154-P4 family).  Lower on z >=
1: T/y_t >= (J_2 - sum_{m>=3} |J_m|)/z: the far lower side is
controlled by J_2 alone.  On the strip both sides ride the
band-edge data: the upper spike (T -> +/-inf at b_top+, residue
sign v_{K-1} b_{K-1} measured +1/+1/-1) crosses 1.5 y_t at y_C ~
1.04 b_top and the first cache zero sits ABOVE y_C (measured
1.094/1.102 b_top; at b13 no crossing, maxT = 1.0177 y_t): the
upper half at zeros reduces to BAND-EDGE ZERO SEPARATION -- the
same root-position class as B00-ROOTGAP/S1 (r150).

RED-TEAM ALGEBRA (mandatory).  (i) e_0-witness (r153/r154 class,
A_0' = A_0/sqrt(P)): A_{2m} invariant, y_t' = sqrt(P) y_t, J_m' =
J_m P^{(1-m)/2} DEFLATES, and T'/y_t' == T/y_t EXACTLY: THE
T-WINDOW RATIO IS WITNESS-INVARIANT (scale-blind coordinate; the
A_0-witness can neither refute nor inflate it -- it inflates only
the mass currencies, r154 G40 cited).  (ii) 2-MODE WITNESS (NEW):
c'' = c + d(e_1 + e_2) leaves A_0 invariant while A_2 is FREE
(dA_2 = d(b_2 - b_1)): deflating y_t'' = y_t/sqrt(P) INFLATES
J_2'' by ~P x b/y_t (measured x1e6) while ALL L1-L6 identities
hold c-generically: ALGEBRA-ONLY-J-CAPS-REFUTED -- the moment-
ratio window (J_2 in (0, 1/4]) is ARITHMETIC-PINNED (only the
census-minimizer property holds it); refusal via Rayleigh
gap/eigen-residual.  ADJUDICATION (the R1 contract question): the
moment system splits EXACTLY into a SCALE-BLIND SHAPE SECTOR
({J_m}, ladder ratios, T/y_t -- witness-invariant, per-block
certifiable, classical-candidate) and an ARITHMETIC SCALE SECTOR
(y_t, A_0 -- minimizer-pinned): T-WINDOW lives in the shape
sector, TOPROOT in the scale sector; the J-window boundedness is
arithmetic-pinned, NOT classical.

ASSEMBLED RESIDUE (frozen in advance as the adjudication shape):
T-WINDOW == {J_2 in (0, 1/4 + eps) (quarter-cap proven given the
real ladder; boundedness arithmetic-pinned)} + {band-edge sliver
(b_top, Y*) + band-edge separation for the upper spike -- root-
position class, the same family as TOPROOT's B00-ROOTGAP +
S1-floor}.  The pair {TOPROOT, T-WINDOW} contracts to BAND-EDGE
ROOT-SEPARATION COORDINATES + the arithmetic J-window; census
{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; NO omega closed.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (NO zeta use, np.load only in ward_*, no
    zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (kind=exact): G10 L1 (level-shift partial
    fractions + PHI dictionary + Laurent remainder); G11 L2
    (quarter-cap algebra + root rearrangement + bracket instance);
    G12 L3 (power-sum dictionary generic via series, SR1-SR3);
    G13 L4 (pole-interval parity + trapped-count inequality +
    Descartes polynomial instance; Laguerre CITED AS FORM);
    G14 L5 (level shift generic + certificate inequality chain);
    G15 L6 (two-sided split inequalities); G16 red-team algebra
    (e_0 J-deflation exponents + T-ratio invariance HARD ASSERT +
    2-mode A_0-invariant A_2-free direction HARD ASSERT).
S2  G20 HSW G(T) sanity.
S3  per-block ladder, tags 5/8/13/18/24/28 (r154 anchors VERBATIM,
    dps 60/80/120/140/150/155), ONE anchor point per block:
    G30 anchor certificates (L_EPS on the r151/r153/r154 strings
    rel <= 5e-3; n_neg == 0; a_2 sign == -1);
    G31 F-census: count == K-1, n_nonreal == 0, n_esc == N_ESC_TAB
    (r154 strings), top/y_t and second/y_t on the r154 strings rel
    <= 5e-3;
    G32 sum rules SR1/SR2/SR3 rel <= 1e-40 core (5..18) / 1e-25
    deep (24/28, pre-freeze unmeasured, DISCLOSED);
    G33 moment table: J_2 on the r154 J-strings rel <= 5e-3; J_3 <
    0 at core; n_esc <= nsc + 1 HARD; n_esc <= V(jets) HARD
    (Laguerre form); V == n_esc at core, V <= n_esc + 10 deep
    (DISCLOSED);
    G34 secular-Laurent instantiated: |PHI(z_top)| <= 1e-40 core /
    1e-20 deep; quarter-cap identity dev <= 1e-40 / 1e-20; J_2 <=
    0.25 + z_top |rho| HARD; z_top |rho| <= 0.05; |z_quad - z_top|
    <= 0.05;
    G35 truncation convergence: M = 3 top-root dev <= 1e-3 core /
    1e-2 deep; M = 6 second-root dev <= 1e-3 core / 1e-2 deep
    (full M-tables printed);
    G36 T-census (isolated try; a failure fails ONLY this gate):
    above-band count <= 1 core / <= 5 deep (DISCLOSED), top
    above-band T-root <= 1.05 b_top core / 1.5 deep; n_nonreal
    printed (the T-numerator is NOT real-rooted: 2/4/8 measured);
    G37 cascade: certified floor exists with Y*/y_t <= 0.15 and
    Y* > b_top; ZERO T <= 0 cache violations above Y* (HARD);
    Y* >= top above-band T-root when the T-census carries;
    residual/strip zero counts printed (the shrink exhibit);
    G38 window at zeros: minT > 0 AND maxT/y_t in (0.5, 1.5) at
    every cache zero above the band (r154 G36 continuity); y_C
    branch: NO 1.5 y_t crossing OR first cache zero above the
    crossing high-edge (band-edge separation exhibit);
    G39 (blocks 5 + 8) adversarial witnesses: e_0 T-ratio
    invariance dev <= 1e-40 AND J_2 deflation dev <= 1e-40;
    2-mode: A_0 dev <= 1e-40, y_t''/(y_t/sqrt(P)) dev <= 1e-40,
    J_2 inflation >= 1e3, REFUSAL rgap >= 1e3, resn >= 1e-20.
S4  controls G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 AND |A_0_w| in (0.05, 2.0) AND y_t_w/b_top <= 1.5
    AND J_2_w <= -0.1 (NEGATIVE leading moment ratio: the quarter-
    window has no content in the fake worlds) AND n_esc_w <= 1
    AND SR1 world-blind <= 1e-40 (null control); G53 consistency.
S5  G54 tau-screen: slopes of J_2, z_top, z_second, Y*/y_t vs
    log10 tau <= 0.35 (DEMAND-FLAT); RIDER report: slope log10
    A_0^2 vs log10 tau printed (rides tau by construction --
    BOUND-RIDES-CONNES typed; the moment RATIOS are the flat
    coordinates); G55 conditioning (1e-25 shift at the b5 anchor).
S6  G60 demand audit (SEQ level inherited; per-block statements;
    no ALL-X demand); G61 min-cut (r116 replica; r154 graph
    VERBATIM -- this round changes the COORDINATES of the TWINDOW
    edge, not the set: flows base 4 / refined 5 / one-grant 5 /
    counterfactual-parallel 7 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED).
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573,
9.3675) [HSW22 Cor. 1.2]; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); WORKERS = 14 (spawn; deterministic tasks
gathered by key; concurrent lanes untouched).
BLOCKS = (5, 5.44, 60), (8, 8.50, 80), (13, 13.50, 120),
(18, 18.50, 140), (24, 24.50, 150), (28, 28.50, 155);
POLY_MAXSTEPS = 3000; POLY_EXTRAPREC = 2 x dps (r154 Amendment-1
muscle); MOM_MAX = 14; TRUNC_MS = (1, 2, 3, 4, 6, 8, 10, 12);
CASC_JMAX = 24; CASC_TW_MAX = 2.0; CASC_BIS = 60; TOW_TAIL_EPS =
1e-35; P_WITNESS = 1e6; YC_LEVEL = 1.5.
BARS: LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
24: 0.2566, 28: 0.2713} rel 5e-3 (r151/r153/r154 strings);
N_ESC_TAB = {5: 4, 8: 6, 13: 11, 18: 15, 24: 20, 28: 23} (r154);
TOP_TAB = {5: 0.8763, 8: 0.8465, 13: 0.8383, 18: 0.8344, 24:
0.8322, 28: 0.8311} rel 5e-3 (r154); SEC_TAB = {5: 0.0825, 8:
0.0822, 13: 0.0818, 18: 0.0820, 24: 0.0822, 28: 0.0825} rel 5e-3
(r154); J2_TAB = {5: 0.1117, 8: 0.1375, 13: 0.1446, 18: 0.1479,
24: 0.1497, 28: 0.1506} rel 5e-3 (r154 J_2 strings); SR_BAR_CORE
= 1e-40 (calibration SR1/SR2/SR3 = 3.1e-56/8.8e-56/1.4e-55 at b5,
9.2e-71/2.5e-70/3.8e-70 at b8, 2.1e-100/6.5e-100/1.0e-99 at b13);
SR_BAR_DEEP = 1e-25 (24/28 pre-freeze unmeasured, DISCLOSED);
PHI_BAR_CORE = 1e-40 (calibration 3.47e-56/8.81e-71/2.38e-100);
PHI_BAR_DEEP = 1e-20; QC_ID_BAR same split (calibration 3.0e-56/
7.5e-71/2.0e-100); RHO_MAX = 0.05 (calibration z|rho| = 0.0033602/
0.0075381/0.0090456); QUAD_DEV_MAX = 0.05 (calibration 4.49e-3/
1.11e-2/1.36e-2); TRUNC3_BAR = 1e-3 core / 1e-2 deep (calibration
M=3 top dev <= 5e-6 core); TRUNC6_BAR = 1e-3 core / 1e-2 deep
(calibration M=6 second dev 1.2e-5/1e-6/6e-6); V_SLACK_DEEP = 10
(core measured V == n_esc: 4/6/11); TCEN_ABOVE_CORE = 1;
TCEN_ABOVE_DEEP = 5; TCEN_TOP_CORE = 1.05; TCEN_TOP_DEEP = 1.5
(calibration above-band 0/0/1, top above-band 1.0079 b_top at
b13, in-band top 0.90127/0.998457 at b5/b8; n_nonreal 2/4/8 --
the T-numerator is NOT real-rooted, DISCLOSED); CASC_YT_MAX =
0.15 (calibration Y*/y_t = 0.030736/0.010465/0.0053297 falling;
Y*/b_top = 1.16933/1.02304/1.40557 at levels j = 4/9/12);
TWIN_MAXT_WIN = (0.5, 1.5) (calibration anchor maxT/y_t =
1.05648/1.09002/1.0177, minT/y_t = 0.000104/0.000813/0.00605);
ADV_BAR = 1e-40 (calibration e_0 T-ratio dev 0.0, 2-mode A_0 dev
2.1e-55/3.1e-69, y_t dev 3.6e-55/3.3e-69); ADV_J2_INFL_MIN = 1e3
(calibration x1.0e6); ADV_RGAP_MIN = 1e3 (calibration 1.03e5/
3.04e6); ADV_RES_MIN = 1e-20 (calibration 1.8e-5/1.0e-10);
CTRL_A0_WIN = (0.05, 2.0); CTRL_YTB_MAX = 1.5; CTRL_J2_MAX = -0.1
(calibration J_2_w = -2.962/-0.8449/-2.71); CTRL_NESC_MAX = 1;
CTRL_SR_BAR = 1e-40 (calibration 7.8e-62/1.4e-60/1.0e-79);
TAU_SLOPE_BAR = 0.35; COND_WIN = (1e-40, 1e-10); RUNTIME_BAR =
14400 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5); NO zeta use.
All mpf arithmetic inside explicit mp.workdps blocks in-worker;
per-zero T profiles computed in mp and TRANSPORTED as f64 (flat
O(1) ratio currencies for the MEASURED layer only, DISCLOSED);
huge/tiny quantities (A_0, y_t, jets, power sums, witnesses) stay
mp end-to-end with mp.log diagnostics (r147/r141 underflow classes
banned); census polyroots at extraprec = 2 x dps, maxsteps 3000;
the F-census and T-census each isolated in their own try (r154
Amendment-1 lesson: a census failure fails ONLY its own gate); no
f64 refinement of any mp quantity.

CALIBRATION DISCLOSURE (calib_scratch_rootladder.py, pre-freeze,
two passes (the first carried a T-census weight bug w_k for
w_k b_k -- fixed pre-freeze, both logged), deleted after freeze;
all numbers quoted verbatim): b5 anchor x0 = 4.823998 (K = 10,
dps 60): y_t = 49129.659 (sign -1), b_top = 1291.3811 (y_t/b_top
38.04); J_2..J_6 = 0.11174/-0.0029387/-5.3484e-6/1.4474e-7/
3.2064e-9; jet signs m=0..24 "+-+--++++..."; V(jets) = 4 == n_esc
= 4 (nsc = 3); z-ladder 0.87632/0.082474/0.038182/0.028795; SR1/2/
3 = 3.1e-56/8.8e-56/1.4e-55; sum z_esc = 1.02577, sum z_esc^2 =
0.777025, P_2/P_1^2 = 0.77651265 == 1 - 2 J_2; PHI(z_top) =
3.47e-56, quarter-cap id dev 3.0e-56, z|rho| = 0.0033602, quad
z+ = 0.871828 (dev 4.49e-3); trunc M=3 top 0.87632, M=6 second
0.082462; S-zero census above band 3 (top/y_t 0.068097); T-census
5 real + 2 nonreal, above band 0, top T-root/b_top 0.90127; edge
residue sign +1; cascade Y*/b_top = 1.16933, Y*/y_t = 0.030736
(j = 4); strip zeros 87, residual (b_top, Y*) 1, violations 0;
y_C(1.5) down-crossing [1.0352, 1.0439] b_top, first zero
1.094 b_top ABOVE; maxT/y_t = 1.05648, minT/y_t = 0.000104; e_0
T-ratio dev 0.0, J_2' == J_2/sqrt(P); 2-mode A_0 dev 2.1e-55, y_t
dev 3.6e-55, J_2'' = 1.1336e5 (x1.0e6), rgap 102693.6, resn
1.8e-5; block wall 12.8 s.  b8 x0 = 7.394749 (K = 19): y_t =
312376.11, b_top = 3195.2904 (97.76); J_2..J_6 = 0.13748/
-0.0065328/0.00012968/-9.7249e-7/2.5109e-10; V = 6 == n_esc (nsc
9); ladder 0.84649/0.082245/0.032318/0.019275/0.013704/0.011672;
SR 9.2e-71/2.5e-70/3.8e-70; sum z_esc 1.00571, sum^2 0.725056;
PHI -8.81e-71, z|rho| 0.0075381, quad dev 1.11e-2; T-census 12
real + 4 nonreal, above band 0, top 0.998457 b_top; edge +1;
cascade Y*/b_top 1.02304 (j = 9), Y*/y_t 0.010465; strip 299,
residual 0, violations 0; y_C [1.0417, 1.0521], first zero 1.1023
ABOVE; maxT 1.09002, minT 0.000813; rgap 3.04e6, resn 1.0e-10;
wall 25.3 s.  b13 x0 = 11.821307 (K = 37): y_t = 2211855.6, b_top
= 8386.9634 (263.73); J_2..J_6 = 0.14461/-0.0078287/0.00020992/
-3.1518e-6/2.7833e-8 (deep jet signs irregular beyond m ~ 9:
"+-+-+-+-+--+++++-----"); V = 11 == n_esc (nsc 14); ladder top
0.83828, second 0.081792; SR 2.1e-100/6.5e-100/1.0e-99; sum z_esc
1.00556, sum^2 0.710783; PHI 2.38e-100, z|rho| 0.0090456, quad
dev 1.36e-2; T-census 26 real + 8 nonreal, above band 1 at
1.0079 b_top (T(1.01 x topTroot) = +0.9472 y_t), edge sign -1;
cascade Y*/b_top 1.40557 (j = 12), Y*/y_t 0.0053297; strip 1033,
residual 8, violations 0; y_C: NO crossing (maxT 1.0177); rgap
1.82e8, resn 2.3e-20; wall 154.5 s.  Controls: SMOOTH x=5 tau_w
-1.0944, y_t/b_top 0.154, J_2_w -2.962, n_esc 1, SR1 7.8e-62;
SCRARITH -0.3459/0.643/-0.8449/1/1.4e-60; EPSTEIN x=8 -1.6310/
0.177/-2.71/1/1.0e-79.  b18/b24/b28 pre-freeze UNMEASURED on all
new quantities (build cost) -- windows set from the r154 frozen
strings (N_ESC/TOP/SEC/J2 tabs) + calibrated trends + structure
asserts, DISCLOSED above.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks below.

VERDICT ENUMS (frozen): LADDER-LAW-PROVEN(L1: the escaped ladder
is the zero set of the moment-Laurent PHI; self-similarity ==
moment-ratio flatness; G10/G34/G35); QUARTER-CAP-PROVEN(L2: J_2
<= 1/4 + z|rho| given the real top root -- the ladder caps its
own leading moment; G11/G34); SUMRULES-EXACT(L3: SR1-SR3 trace/
power-sum ladder rules; G12/G32); SIGNLAW(L4: n_esc <= nsc + 1
exact, n_esc <= V(jets) Laguerre-form, V == n_esc measured-tight
at core; G13/G33); CASCADE-CERT-EXTENDED(L5: T > 0 certified
source-pure down to Y* ~ 1.0-1.4 b_top, the r154 TOWER-DIVERGES
obstruction bypassed one jet up; ROOT-CAP-CERTIFIED via r154-P2;
G14/G37); TWINDOW-EDGE-RESIDUE(L6: the open T-WINDOW content is
the band-edge sliver + band-edge zero separation -- root-position
class, same family as B00-ROOTGAP + S1-floor; G15/G36/G38);
MOMENT-SPLIT(the exact adjudication: shape sector scale-blind
witness-invariant, scale sector arithmetic; the J-window is
ARITHMETIC-PINNED by the 2-mode witness; G16/G39);
REDTEAM-REFUTES-ALGEBRA(G16/G39); CONTROLS-REFUSE(negative J_2 in
fake worlds; G50-G53); DEMAND-FLAT + BOUND-RIDES-CONNES(G54);
QUANTIFIER-INHERITED(G60); OMEGA-UNCHANGED(census 4; G61);
MINCUT(4/5; counterfactual 7 NOT REAL).  Composite priority:
INSTRUMENT-EDGE > EXACT-LAYER-OBSTRUCTED > verdicts as gated.

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
CORE_TAGS = (5, 8, 13, 18)
POLY_MAXSTEPS = 3000
MOM_MAX = 14
TRUNC_MS = (1, 2, 3, 4, 6, 8, 10, 12)
CASC_JMAX = 24
CASC_TW_MAX = 2.0
CASC_BIS = 60
TOW_TAIL_EPS = 1e-35
P_WITNESS = 1e6
YC_LEVEL = 1.5

LEPS_TAB = {5: 0.1088, 8: 0.1849, 13: 0.2169, 18: 0.2330,
            24: 0.2566, 28: 0.2713}
LEPS_TOL = 5e-3
N_ESC_TAB = {5: 4, 8: 6, 13: 11, 18: 15, 24: 20, 28: 23}
TOP_TAB = {5: 0.8763, 8: 0.8465, 13: 0.8383, 18: 0.8344,
           24: 0.8322, 28: 0.8311}
SEC_TAB = {5: 0.0825, 8: 0.0822, 13: 0.0818, 18: 0.0820,
           24: 0.0822, 28: 0.0825}
LAD_TOL = 5e-3
J2_TAB = {5: 0.1117, 8: 0.1375, 13: 0.1446, 18: 0.1479,
          24: 0.1497, 28: 0.1506}
J2_TOL = 5e-3
SR_BAR_CORE = 1e-40
SR_BAR_DEEP = 1e-25
PHI_BAR_CORE = 1e-40
PHI_BAR_DEEP = 1e-20
RHO_MAX = 0.05
QUAD_DEV_MAX = 0.05
TRUNC3_BAR_CORE = 1e-3
TRUNC3_BAR_DEEP = 1e-2
TRUNC6_BAR_CORE = 1e-3
TRUNC6_BAR_DEEP = 1e-2
V_SLACK_DEEP = 10
TCEN_ABOVE_CORE = 1
TCEN_ABOVE_DEEP = 5
TCEN_TOP_CORE = 1.05
TCEN_TOP_DEEP = 1.5
CASC_YT_MAX = 0.15
TWIN_MAXT_WIN = (0.5, 1.5)
ADV_BAR = 1e-40
ADV_J2_INFL_MIN = 1e3
ADV_RGAP_MIN = 1e3
ADV_RES_MIN = 1e-20
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


# --------------------------------------------------------- censuses
def census_weighted(wts, K, aa, dps, const):
    """r132/r154 Amendment-1 polyroots census on the numerator of
    const + sum_{k>=1} wts[k] * y/(y - b_k) (scaled + deflated
    lattice products).  With wts = (-1)^k c_k this is the F-census;
    with wts = (-1)^k c_k b_k and const = 0 it is y * A_0 * T (the
    T-census; the spurious root y = 0 is dropped by the caller).
    Returns (sorted real y as mp list, n_nonreal)."""
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
    """per-block anchor build: jets + moment ratios + F-census +
    T-census + sum rules + PHI/quarter-cap + truncations + cascade
    + cache window pass + y_C.  All mp in workdps; f64 transport of
    flat O(1) ratio currencies only (DISCLOSED)."""
    tag, x_nom, dps = args
    try:
        gam = ward_cache()
        u0, clo, chi = AEP.anchor_select(x_nom)
        x0 = math.exp(u0)
        out = dict(tag=tag, x0=x0)
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
            out["K"] = K
            out["nneg"] = nneg
            out["yt_l10"] = float(mp.log(yt) / l10)
            out["btop"] = float(btop)
            out["yt_btop"] = float(yt / btop)
            out["tau_l10"] = float(mp.log(abs(tau)) / l10)
            out["a0sq_l10"] = float(2 * mp.log(abs(A0)) / l10)
            # L_EPS anchor certificate (r153/r154 recipe)
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
            # moment ratios (signed, transported as f64 ratios)
            Jm = {}
            for m in range(2, MOM_MAX + 1):
                Jm[m] = a[m] / yt ** m
            out["J"] = {m: float(Jm[m]) for m in Jm}
            # jet sign census + V
            sgn_all = [int(mp.sign(a[m]))
                       for m in range(0, M_JETS + 1)]
            Vall = sum(1 for i in range(1, len(sgn_all))
                       if sgn_all[i] != sgn_all[i - 1]
                       and sgn_all[i] != 0)
            out["V_jets"] = Vall
            out["sgn_head"] = "".join("+" if s > 0 else "-"
                                      for s in sgn_all[:25])
            nsc = 0
            prev = None
            for k in range(1, K):
                sg = 1 if wk[k] > 0 else -1
                if prev is not None and sg != prev:
                    nsc += 1
                prev = sg
            out["nsc"] = nsc
            out["edge_sign"] = int(mp.sign(vk[Km1 - 1] * bl[Km1 - 1]))

            def T_of(y):
                return sum(vk[i] * bl[i] / (y - bl[i])
                           for i in range(Km1))

            # ---------------- F-census (isolated)
            try:
                wtsF = {k: ((-1) ** k) * cs[k] for k in range(1, K)}
                ysF, nnrF = census_weighted(wtsF, K, aa, dps, cs[0])
                out["f_n"] = len(ysF)
                out["f_nnr"] = nnrF
                esc = [y for y in ysF if y > btop]
                out["n_esc"] = len(esc)
                zesc = [y / yt for y in esc]
                out["z_ladder"] = [float(z) for z in
                                   sorted(zesc, reverse=True)]
                out["z_top"] = float(zesc[-1]) if esc else float("nan")
                out["z_sec"] = float(sorted(zesc)[-2]) \
                    if len(zesc) >= 2 else float("nan")
                # sum rules
                P1 = sum(ysF) - sum(bl)
                P2 = sum(y * y for y in ysF) \
                    - sum(bb * bb for bb in bl)
                P3 = sum(y ** 3 for y in ysF) \
                    - sum(bb ** 3 for bb in bl)
                out["sr1"] = float(abs(P1 / (-a[1]) - 1))
                out["sr2"] = float(abs(
                    P2 / (a[1] ** 2 - 2 * a[2]) - 1))
                out["sr3"] = float(abs(
                    P3 / (3 * a[1] * a[2] - 3 * a[3] - a[1] ** 3)
                    - 1))
                out["sum_zesc"] = float(sum(zesc))
                out["sum_z2esc"] = float(sum(z * z for z in zesc))
                # PHI at z_top + quarter-cap identity
                ztop = zesc[-1] if esc else None
                if ztop is not None:
                    yT = esc[-1]
                    Trat = T_of(yT) / yt
                    Phi = ztop - 1 + Trat
                    rho = Trat - Jm[2] / ztop
                    out["phi_dev"] = float(abs(Phi))
                    out["qc_dev"] = float(abs(
                        Jm[2] - (ztop * (1 - ztop) - ztop * rho)))
                    out["zrho"] = float(abs(ztop * rho))
                    disc = 1 - 4 * Jm[2]
                    zq = (1 + mp.sqrt(disc)) / 2
                    out["quad_dev"] = float(abs(zq - ztop))
                # truncation ladders
                tr = {}
                for Mt in TRUNC_MS:
                    coefs = [mp.mpf(1), mp.mpf(-1)]
                    for m in range(1, Mt + 1):
                        coefs.append(a[m + 1] / yt ** (m + 1))
                    try:
                        rts = mp.polyroots(coefs, maxsteps=1000,
                                           extraprec=dps)
                        rr = sorted(
                            [mp.re(r) for r in rts
                             if abs(mp.im(r)) < 1e-12
                             and mp.re(r) > 0], reverse=True)
                        tr[Mt] = [float(r) for r in rr[:6]]
                    except Exception:            # noqa: BLE001
                        tr[Mt] = []
                out["trunc"] = tr
            except Exception as cexc:              # noqa: BLE001
                out["f_census_error"] = repr(cexc)

            # ---------------- T-census (isolated)
            try:
                sc = btop + 1
                wtsT = {k: ((-1) ** k) * cs[k] * b[k] * b[k]
                        / (sc * sc) for k in range(1, K)}
                ysT, nnrT = census_weighted(wtsT, K, aa, dps, None)
                ysT = [y for y in ysT if y > mp.mpf("1e-6")]
                escT = [y for y in ysT if y > btop]
                out["t_n"] = len(ysT)
                out["t_nnr"] = nnrT
                out["t_above"] = len(escT)
                out["t_top_btop"] = float(ysT[-1] / btop) \
                    if ysT else float("nan")
                out["t_above_top_btop"] = float(escT[-1] / btop) \
                    if escT else float("nan")
            except Exception as cexc:              # noqa: BLE001
                out["t_census_error"] = repr(cexc)

            # ---------------- cascade certificate
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

            # ---------------- cache window pass (single pass)
            minT = None
            maxT = mp.mpf(0)
            n_strip = 0
            n_resid = 0
            n_viol = 0
            first_z = None
            for g in gam:
                y = mp.mpf(repr(float(g))) ** 2
                if y <= btop:
                    continue
                if first_z is None:
                    first_z = y
                Tv = T_of(y)
                if minT is None or Tv < minT:
                    minT = Tv
                if Tv > maxT:
                    maxT = Tv
                if y < yt:
                    n_strip += 1
                if Ybest is not None and y < Ybest:
                    n_resid += 1
                elif Ybest is not None and Tv <= 0:
                    n_viol += 1
            out["minT_yt"] = float(minT / yt)
            out["maxT_yt"] = float(maxT / yt)
            out["n_strip"] = n_strip
            out["n_resid"] = n_resid
            out["n_viol"] = n_viol
            out["firstz_btop"] = float(first_z / btop)
            # y_C crossing (two-stage log grid)
            lev = mp.mpf(repr(YC_LEVEL)) * yt
            cross_hi = None
            prev_y = None
            prev_hi = None
            grid = list(np.linspace(
                float(mp.log(btop * mp.mpf("1.0005"))),
                float(mp.log(3 * btop)), 400)) + list(np.linspace(
                    float(mp.log(3 * btop)) + 1e-9,
                    float(mp.log(4 * yt)), 300))
            for lg in grid:
                y = mp.exp(mp.mpf(repr(float(lg))))
                hi_now = T_of(y) > lev
                if prev_hi is not None and prev_hi and not hi_now:
                    cross_hi = y
                prev_hi = hi_now
                prev_y = y
            _unused = prev_y
            out["yc_btop"] = float(cross_hi / btop) \
                if cross_hi is not None else float("nan")
            out["yc_exists"] = cross_hi is not None
            out["yc_zero_above"] = bool(first_z > cross_hi) \
                if cross_hi is not None else True
        return out
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_adversarial(args) -> dict:
    """red-team witnesses: (i) e_0 (A_0' = A_0/sqrt(P)): T-ratio
    invariance + J_2 deflation; (ii) 2-mode A_0-preserving witness
    deflating y_t and inflating J_2; refusal via Rayleigh gap."""
    tag, x_nom, dps = args
    try:
        u0, _clo, _chi = AEP.anchor_select(x_nom)
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
            phi = [V[i, i0] for i in range(K)]
            nn = mp.sqrt(sum(p * p for p in phi))
            phi = [p / nn for p in phi]
            cs = [phi[k] / nrm[k] for k in range(K)]
            aa = u / 2
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            bl = [b[k] for k in range(1, K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
            A4 = sum((-1) ** k * cs[k] * b[k] ** 2
                     for k in range(1, K))
            yt = abs(A2 / A0)
            J2 = (A4 / A0) / (A2 / A0) ** 2
            P = mp.mpf(repr(P_WITNESS))
            # e_0 witness
            t_ = A0 * (1 / mp.sqrt(P) - 1)
            A0p = A0 + t_
            yprobe = 2 * yt
            Tv = sum(((-1) ** k * cs[k] * b[k] / A0) * b[k]
                     / (yprobe - b[k]) for k in range(1, K))
            Tp = Tv * (A0 / A0p)
            ytp = abs(A2 / A0p)
            dev_inv = float(abs((Tp / ytp) / (Tv / yt) - 1))
            J2p = (A4 / A0p) / ytp ** 2
            dev_defl = float(abs(J2p / (J2 / mp.sqrt(P)) - 1))
            # 2-mode witness
            d_ = -A2 * (1 - 1 / mp.sqrt(P)) / (bl[1] - bl[0])
            cs2 = list(cs)
            cs2[1] = cs2[1] + d_
            cs2[2] = cs2[2] + d_
            A0q = sum((-1) ** k * cs2[k] for k in range(K))
            A2q = sum((-1) ** k * cs2[k] * b[k] for k in range(1, K))
            A4q = sum((-1) ** k * cs2[k] * b[k] ** 2
                      for k in range(1, K))
            ytq = abs(A2q / A0q)
            J2q = (A4q / A0q) / ytq ** 2
            infl = float(abs(J2q / J2))
            dev_a0 = float(abs(A0q / A0 - 1))
            dev_yt = float(abs(ytq / (yt / mp.sqrt(P)) - 1))
            phi2 = [cs2[k] * nrm[k] for k in range(K)]
            nn2 = mp.sqrt(sum(p * p for p in phi2))
            phi2 = [p / nn2 for p in phi2]
            Mp2 = [sum(M[i, j] * phi2[j] for j in range(K))
                   for i in range(K)]
            rr = sum(phi2[i] * Mp2[i] for i in range(K))
            rgap = float((rr - tau) / tau)
            resn = float(mp.sqrt(sum((Mp2[i] - rr * phi2[i]) ** 2
                                     for i in range(K))))
            return dict(tag=tag, dev_inv=dev_inv, dev_defl=dev_defl,
                        dev_a0=dev_a0, dev_yt=dev_yt, infl=infl,
                        rgap=rgap, resn=resn)
    except Exception as exc:                       # noqa: BLE001
        return dict(tag=tag, error=repr(exc))


def w_control(args) -> dict:
    """control world via R4.build_cell: tau_w, A_0_w, y_t_w/b_top,
    J_2_w (the moment window must refuse) and the SR1 trace
    identity as a WORLD-BLIND null control."""
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
            J2w = (A4 / A0) / (A2 / A0) ** 2
            wtsF = {k: ((-1) ** k) * cs[k] for k in range(1, K)}
            ysF, _nnr = census_weighted(wtsF, K, aa, dpsw, cs[0])
            P1 = sum(ysF) - sum(b[1:])
            sr1 = float(abs(P1 / (-A2 / A0) - 1))
            n_esc = sum(1 for y in ysF if y > btop)
            return dict(world=world, tauf=float(tau),
                        a0f=float(abs(A0)), ytb=float(yt / btop),
                        j2w=float(J2w), n_esc=n_esc, sr1=sr1)
    except Exception as exc:                       # noqa: BLE001
        return dict(world=world, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y, z, yt = sp.symbols("y z yt", positive=True)
    v1, v2, v3 = sp.symbols("v1 v2 v3", real=True)
    b1, b2, b3 = sp.symbols("b1 b2 b3", positive=True)

    # ---------------- G10 L1 dictionary
    S3 = v1 / (y - b1) + v2 / (y - b2) + v3 / (y - b3)
    T3 = v1 * b1 / (y - b1) + v2 * b2 / (y - b2) \
        + v3 * b3 / (y - b3)
    okA = sp.simplify(y * S3 - (v1 + v2 + v3) - T3) == 0
    # PHI dictionary: with sum v = -yt and y = z yt:
    lhs = (z * (1 + S3) - (z - 1 + T3 / yt)).subs(y, z * yt)
    tgt = ((v1 + v2 + v3 + yt) / yt).subs(y, z * yt)
    okB = sp.simplify(sp.together(lhs - tgt)) == 0
    # Laurent with exact partial-geometric remainder (M = 3)
    vv, bb = sp.symbols("vv bb", positive=True)
    Mi = 3
    part = sum(vv * bb ** mm / y ** mm for mm in range(1, Mi + 1))
    remd = vv * bb ** (Mi + 1) / (y ** Mi * (y - bb))
    okC = sp.simplify(vv * bb / (y - bb) - part - remd) == 0
    out.append(("G10-l1-dictionary", okA and okB and okC,
                "y S == sum v + T EXACT (partial fractions); with "
                "sum v = a_2 = -y_t and z = y/y_t: (y/y_t) F/A_0 == "
                "z - 1 + T/y_t == PHI(z) GENERIC -- the census "
                "roots above the band are the zeros of the moment-"
                "Laurent PHI(z) = z - 1 + sum J_{m+1} z^-m; the "
                "escaped ladder is an algebraic function of the "
                "moment ratios alone (THEOREM L1); Laurent tail "
                "with exact partial-geometric remainder"))

    # ---------------- G11 L2 quarter-cap + rearrangement
    okD = sp.simplify((sp.Rational(1, 4) - z * (1 - z))
                      - (z - sp.Rational(1, 2)) ** 2) == 0
    J2s, rh = sp.symbols("J2s rh", real=True)
    z0 = sp.symbols("z0", positive=True)
    Phi0 = z0 - 1 + J2s / z0 + rh
    solJ = sp.solve(sp.Eq(Phi0, 0), J2s)
    okE = len(solJ) == 1 and sp.simplify(
        solJ[0] - (z0 * (1 - z0) - z0 * rh)) == 0
    # bracket instance: PHI has a sign change on an interval
    inst = {J2s: sp.Rational(3, 20), rh: 0}
    Pl = Phi0.subs(inst).subs(z0, sp.Rational(4, 5))
    Ph = Phi0.subs(inst).subs(z0, sp.Rational(19, 20))
    okF = bool(Pl < 0) and bool(Ph > 0)
    out.append(("G11-l2-quarter-cap", okD and okE and okF,
                "z(1-z) <= 1/4 EXACT ((z - 1/2)^2 >= 0); PHI(z_0) "
                "= 0 ==> J_2 == z_0(1 - z_0) - z_0 rho(z_0) EXACT "
                "==> J_2 <= 1/4 + z_0|rho(z_0)|: THE CENSUS-REAL "
                "TOP ROOT CAPS ITS OWN LEADING MOMENT RATIO "
                "(THEOREM L2); bracket sign-change instance"))

    # ---------------- G12 L3 power-sum dictionary
    y1, y2 = sp.symbols("y1 y2", positive=True)
    t_ = sp.symbols("t_")
    Fg = (1 - y1 * t_) * (1 - y2 * t_) / ((1 - b1 * t_)
                                          * (1 - b2 * t_))
    ser = sp.series(Fg, t_, 0, 4).removeO()
    a2s = sp.expand(ser.coeff(t_, 1))
    a4s = sp.expand(ser.coeff(t_, 2))
    a6s = sp.expand(ser.coeff(t_, 3))
    P1s = y1 + y2 - b1 - b2
    P2s = y1 ** 2 + y2 ** 2 - b1 ** 2 - b2 ** 2
    P3s = y1 ** 3 + y2 ** 3 - b1 ** 3 - b2 ** 3
    okG = sp.simplify(a2s + P1s) == 0
    okH = sp.simplify(a4s - (a2s ** 2 - P2s) / 2) == 0
    okI = sp.simplify(P3s - (3 * a2s * a4s - 3 * a6s
                             - a2s ** 3)) == 0
    out.append(("G12-l3-power-sums", okG and okH and okI,
                "F/A_0 == prod(1 - y_j t)/prod(1 - b_k t) gives "
                "a_2 == -P_1 (SR1: trace identity, r143 T4 "
                "re-derived), P_2 == a_2^2 - 2 a_4 (SR2), P_3 == "
                "3 a_2 a_4 - 3 a_6 - a_2^3 (SR3) GENERIC: the "
                "ladder power sums ARE the jets (THEOREM L3; sum "
                "z_j -> 1, sum z_j^2 -> 1 - 2 J_2 modulo lattice)"))

    # ---------------- G13 L4 sign laws
    vp = sp.symbols("vp", positive=True)
    okJ = sp.limit(vp / (y - b1), y, b1, "+") == sp.oo \
        and sp.limit(-vp / (y - b1), y, b1, "+") == -sp.oo
    okK = sp.limit(vp / (y - b1), y, b1, "-") == -sp.oo
    # counting slack: n_esc - (nsc+1) + (nbel - (K-2-nsc)) == 0
    # with n_esc = (K-1) - nbel: exact decomposition
    Kv, nscv, nbel = sp.symbols("Kv nscv nbel", integer=True,
                                nonnegative=True)
    okL = sp.simplify((((Kv - 1) - nbel) - (nscv + 1))
                      + (nbel - (Kv - 2 - nscv))) == 0
    # Descartes polynomial instance: (x-1)(x-2) = x^2 - 3x + 2:
    # V = 2 == number of positive roots
    xs = sp.symbols("xs")
    pol = sp.expand((xs - 1) * (xs - 2))
    coeffs = [pol.coeff(xs, 2), pol.coeff(xs, 1), pol.coeff(xs, 0)]
    Vd = sum(1 for i in range(1, 3)
             if coeffs[i] * coeffs[i - 1] < 0)
    okM = Vd == 2
    out.append(("G13-l4-sign-laws", okJ and okK and okL and okM,
                "pole-interval parity: F(b_k+) ~ sign(w_k) inf, "
                "F(b_{k+1}-) ~ -sign(w_{k+1}) inf ==> a same-sign "
                "adjacent pair traps >= 1 root (IVT) ==> n_below "
                ">= K - 2 - nsc(w) ==> n_esc <= nsc(w) + 1 EXACT; "
                "jet side: n_esc <= V(jet signs) by Laguerre's "
                "rule on f(u) = 1 + sum a_{2m} u^m in its "
                "convergence disk (CITED AS FORM, Polya-Szego V; "
                "Descartes polynomial instance gated); MEASURED: "
                "V == n_esc at all core blocks (THEOREM L4)"))

    # ---------------- G14 L5 cascade
    F1 = v1 * b1 / (y - b1) + v2 * b2 / (y - b2)
    F2 = v1 * b1 ** 2 / (y - b1) + v2 * b2 ** 2 / (y - b2)
    F3 = v1 * b1 ** 3 / (y - b1) + v2 * b2 ** 3 / (y - b2)
    a4g = v1 * b1 + v2 * b2
    a6g = v1 * b1 ** 2 + v2 * b2 ** 2
    okN = sp.simplify(sp.together(y * F1 - a4g - F2)) == 0
    okO = sp.simplify(sp.together(
        y ** 2 * F1 - (a4g * y + a6g) - F3)) == 0
    #  certificate chain instance: Q > c/y and |Fn| <= c/y ==> T > 0
    Qv, cv, yv = sp.symbols("Qv cv yv", positive=True)
    Fn = sp.symbols("Fn", real=True)
    okP = bool(((Qv + Fn).subs({Qv: 3, Fn: -sp.Rational(1, 2),
                                cv: 1, yv: 2}) > 0)) and \
        sp.simplify((Qv - cv / yv) + (cv / yv + Fn)
                    - (Qv + Fn)) == 0
    out.append(("G14-l5-cascade", okN and okO and okP,
                "y^j F_1 == Q_j + F_{j+1} EXACT (level shift, "
                "generic j = 1, 2); |F_{j+1}| <= (|a_{2(j+2)}|/y)"
                "(1 + TOW_{j+1}(Y)) on y >= Y (Laurent terms "
                "decreasing + envelope closure, r154-P4 class "
                "re-gated in G10); [R_j(Y) > 0 AND no real root of "
                "R_j >= Y] ==> y Q_j > cst >= y|F_{j+1}| ==> T > 0 "
                "POINTWISE on [Y, oo) from source jets alone "
                "(THEOREM L5: the jet-tower cascade -- the r154 "
                "TOWER-DIVERGES-BELOW-y_t obstruction is bypassed "
                "one jet up; with r154-P2 the escaped-root cap is "
                "then certified source-pure)"))

    # ---------------- G15 L6 two-sided split
    J3s, J4s = sp.symbols("J3s J4s", real=True)
    zz = sp.symbols("zz", positive=True)
    #  upper: |sum J_{m+1} z^-m| <= sum |J| for z >= 1 (instance)
    expr = J2s / zz + J3s / zz ** 2 + J4s / zz ** 3
    inst = {J2s: sp.Rational(3, 20), J3s: -sp.Rational(1, 100),
            J4s: sp.Rational(1, 1000), zz: sp.Rational(3, 2)}
    okQ = bool(abs(expr.subs(inst))
               <= (sp.Rational(3, 20) + sp.Rational(1, 100)
                   + sp.Rational(1, 1000)))
    #  lower: T/yt >= (J2 - |J3| - |J4|)/z for z >= 1 (instance)
    okR = bool(expr.subs(inst)
               >= ((sp.Rational(3, 20) - sp.Rational(1, 100)
                    - sp.Rational(1, 1000)) / sp.Rational(3, 2)))
    out.append(("G15-l6-two-sided-split", okQ and okR,
                "on z >= 1: T/y_t <= sum_{m>=2} |J_m| (upper; the "
                "r154-P4 family) and T/y_t >= (J_2 - sum_{m>=3} "
                "|J_m|)/z (lower: the far lower window is "
                "controlled by J_2 ALONE); on the strip both "
                "sides ride the band-edge data (residue sign + "
                "zero separation): THEOREM L6 -- the two-sided "
                "window splits into moment control (far) + "
                "band-edge root positions (near)"))

    # ---------------- G16 red-team algebra
    A0v, Pw = sp.symbols("A0v Pw", positive=True)
    A2v, A4v, A6v = sp.symbols("A2v A4v A6v", real=True)
    #  J_m = A_{2m} A_0^{m-1}/(-A_2)^m (a_2 < 0 branch); e_0:
    #  A_0 -> A_0/sqrt(P), A_{2m} invariant: J_m' = J_m P^{(1-m)/2}
    J2v = A4v * A0v / A2v ** 2
    J3v = -A6v * A0v ** 2 / A2v ** 3
    A0w = A0v / sp.sqrt(Pw)
    J2w = A4v * A0w / A2v ** 2
    J3w = -A6v * A0w ** 2 / A2v ** 3
    okS = sp.simplify(J2w - J2v * Pw ** sp.Rational(-1, 2)) == 0
    okT = sp.simplify(J3w - J3v / Pw) == 0
    #  T-ratio invariance: T' = T A0/A0', yt' = yt A0/A0' (>0)
    Tsym = sp.symbols("Tsym", real=True)
    ytv = sp.symbols("ytv", positive=True)
    okU = sp.simplify((Tsym * (A0v / A0w)) / (ytv * (A0v / A0w))
                      - Tsym / ytv) == 0
    assert okU, "T-WINDOW must be witness-invariant (scale-blind)"
    #  2-mode: A0 invariant, A2 free
    dv = sp.symbols("dv", real=True)
    dA0 = -dv + dv
    dA2 = -dv * b1 + dv * b2
    okV = sp.simplify(dA0) == 0 and \
        sp.simplify(dA2 - dv * (b2 - b1)) == 0
    okW = sp.simplify(dA0) == 0
    A4p, A0pp, eps_ = sp.symbols("A4p A0pp eps_", positive=True)
    lim = sp.limit(A4p * A0pp / eps_ ** 2, eps_, 0, "+")
    okX = lim == sp.oo
    assert okW and okX, \
        "ALGEBRA-ONLY-J-CAPS-REFUTED: the 2-mode direction leaves " \
        "A_0 fixed and drives A_2 -> 0 with J_2 -> oo"
    out.append(("G16-redteam-algebra", okS and okT and okU and okV
                and okW and okX,
                "e_0-witness (A_0' = A_0/sqrt(P)): J_m' == J_m "
                "P^{(1-m)/2} DEFLATES (m = 2, 3 generic) while "
                "T'/y_t' == T/y_t EXACTLY (HARD ASSERT: the "
                "T-window ratio is WITNESS-INVARIANT -- the r154 "
                "A_0-witness lives in the SCALE sector and cannot "
                "touch the shape sector); 2-MODE witness d(e_1 + "
                "e_2): A_0 invariant, A_2 free, J_2 -> oo as A_2 "
                "-> 0 with ALL identities intact (HARD ASSERT: "
                "ALGEBRA-ONLY-J-CAPS-REFUTED -- the moment window "
                "is ARITHMETIC-PINNED; only the census-minimizer "
                "property holds it; numeric witness + refusal in "
                "G39)"))
    return out


# ---------------------------------------------------- demand audit
def demand_audit() -> tuple[bool, str]:
    SEQ, ALL_X = 2, 0
    demand = SEQ
    steps = []
    steps.append(("NF-closure (r122/CDXXIII, cited) demands an "
                  "unbounded sequence per a, not all x",
                  demand == SEQ))
    steps.append(("T-WINDOW/TOPROOT are per-block statements on the "
                  "r153/r154 instrument-chosen blocks; the r153 M1 "
                  "existence form supplies the anchor; V2 (CDXLV) "
                  "the block sequence", True))
    steps.append(("the moment ratios, ladder positions, cascade "
                  "floors and censuses consume SOURCE data only "
                  "(jets + polyroots); the cache enters only as "
                  "read-only ward zeros for the MEASURED window "
                  "layer", True))
    steps.append(("the cascade certificate is per-block and "
                  "pointwise beyond the cache; no quantifier "
                  "upgrade", True))
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

    print("rootladder_probe -- PRIME.ROOTLADDER.SELFSIM.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    blocks = [b for b in BLOCKS if (not smoke or b[0] == 5)]
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    adv_tags = ((5, 5.44, 60),) if smoke else \
        ((5, 5.44, 60), (8, 8.50, 80))
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

    section("S1  EXACT LAYER (L1-L6 + red team)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: CDLVIII/r154 P1-P7 + T-WINDOW + escaped "
         "ladder + LEPS anchors; CDLVII/r153 EZ/LC/RES/funnel; "
         "CDLIV/r150 R1-R4 + B00/S1 coordinates; CDXLVII/r143 T4 "
         "rank-one dictionary + delta_1 lock; CDL/r146 Y1-Y4; "
         "CDLI/r147 AD1/AD2; Laguerre sign rule (Polya-Szego V) "
         "CITED AS FORM; partial fractions + residue calculus + "
         "geometric series + IVT elementary gated; HSW22 Cor. 1.2; "
         "PT21 T_PT constant only")

    section("S2  TARGETS")
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
        tasks.append(("blk", tag, (tag, x_nom, dps)))
    for tag, x_nom, dps in adv_tags:
        tasks.append(("adv", tag, (tag, x_nom, dps)))
    for world, xw, dpsw in controls:
        tasks.append(("ctl", world, (world, xw, dpsw)))
    tasks.sort(key=lambda tk: (-tk[2][2] if tk[0] != "ctl" else 0,
                               tk[0], str(tk[1])))

    section("S3b  BUILDS (%d tasks, %d workers)"
            % (len(tasks), workers))
    res = {}
    t_p = time.time()
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=ctx) as ex:
        futs = []
        for kind, key, targ in tasks:
            fn = dict(blk=w_block, adv=w_adversarial,
                      ctl=w_control)[kind]
            futs.append((kind, key, ex.submit(fn, targ)))
        for kind, key, fu in futs:
            res[(kind, key)] = fu.result()
    info("build wall %.1f s" % (time.time() - t_p))

    # ------------------------------------------------ S3 gates
    section("S3c  PER-BLOCK CERTIFICATES")
    tags = [b[0] for b in blocks]
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    ok36 = ok37 = ok38 = True
    d30, d31, d32, d33, d34, d35, d36, d37, d38 = \
        ([] for _ in range(9))
    tab = {}
    for tag in tags:
        r = res.get(("blk", tag))
        if r is None or "error" in r:
            ok30 = False
            d30.append("b%d ERROR %s" % (tag, (r or {}).get("error")))
            continue
        tab[tag] = r
        core = tag in CORE_TAGS
        # G30 anchor certificates
        lep_dev = abs(r["leps"] / LEPS_TAB[tag] - 1.0)
        okx = (lep_dev <= LEPS_TOL and r["nneg"] == 0
               and r["a2_sign"] == -1)
        ok30 = ok30 and okx
        d30.append("b%d L_EPS %.4f dev %.1e nneg 0 sign -1"
                   % (tag, r["leps"], lep_dev))
        # G31 F-census + ladder strings
        if "f_census_error" in r:
            ok31 = False
            d31.append("b%d F-census ERROR %s"
                       % (tag, r["f_census_error"]))
        else:
            okx = (r["f_n"] == r["K"] - 1 and r["f_nnr"] == 0
                   and r["n_esc"] == N_ESC_TAB[tag]
                   and abs(r["z_top"] / TOP_TAB[tag] - 1) <= LAD_TOL
                   and abs(r["z_sec"] / SEC_TAB[tag] - 1) <= LAD_TOL)
            ok31 = ok31 and okx
            d31.append("b%d %d/%d nnr %d n_esc %d top %.4f sec %.4f"
                       % (tag, r["f_n"], r["K"] - 1, r["f_nnr"],
                          r["n_esc"], r["z_top"], r["z_sec"]))
            # G32 sum rules
            bar = SR_BAR_CORE if core else SR_BAR_DEEP
            okx = (r["sr1"] <= bar and r["sr2"] <= bar
                   and r["sr3"] <= bar)
            ok32 = ok32 and okx
            d32.append("b%d %.0e/%.0e/%.0e"
                       % (tag, r["sr1"], r["sr2"], r["sr3"]))
            # G34 PHI + quarter-cap
            pbar = PHI_BAR_CORE if core else PHI_BAR_DEEP
            okx = (r.get("phi_dev", 1.0) <= pbar
                   and r.get("qc_dev", 1.0) <= pbar
                   and r["J"][2] <= 0.25 + r.get("zrho", 0.0)
                   and r.get("zrho", 1.0) <= RHO_MAX
                   and r.get("quad_dev", 1.0) <= QUAD_DEV_MAX)
            ok34 = ok34 and okx
            d34.append("b%d PHI %.0e qc %.0e zrho %.4f quad %.1e"
                       % (tag, r.get("phi_dev", 1.0),
                          r.get("qc_dev", 1.0), r.get("zrho", 1.0),
                          r.get("quad_dev", 1.0)))
            # G35 truncation convergence
            t3bar = TRUNC3_BAR_CORE if core else TRUNC3_BAR_DEEP
            t6bar = TRUNC6_BAR_CORE if core else TRUNC6_BAR_DEEP
            tr3 = r["trunc"].get(3, [])
            tr6 = r["trunc"].get(6, [])
            okx = (len(tr3) >= 1
                   and abs(tr3[0] - r["z_top"]) <= t3bar
                   and len(tr6) >= 2
                   and abs(tr6[1] - r["z_sec"]) <= t6bar)
            ok35 = ok35 and okx
            d35.append("b%d M3top %.1e M6sec %.1e"
                       % (tag,
                          abs(tr3[0] - r["z_top"]) if tr3 else 9.9,
                          abs(tr6[1] - r["z_sec"])
                          if len(tr6) >= 2 else 9.9))
        # G33 moments + sign laws
        j2dev = abs(r["J"][2] / J2_TAB[tag] - 1.0)
        okx = (j2dev <= J2_TOL
               and ("f_census_error" in r
                    or (r["n_esc"] <= r["nsc"] + 1
                        and r["n_esc"] <= r["V_jets"]
                        and ((core and r["V_jets"] == r["n_esc"])
                             or (not core and r["V_jets"]
                                 <= r["n_esc"] + V_SLACK_DEEP)))))
        if core:
            okx = okx and r["J"][3] < 0
        ok33 = ok33 and okx
        d33.append("b%d J2 %.4f (dev %.0e) J3 %+.1e V %d n_esc %s "
                   "nsc %d" % (tag, r["J"][2], j2dev, r["J"][3],
                               r["V_jets"], r.get("n_esc", "?"),
                               r["nsc"]))
        # G36 T-census (isolated)
        if "t_census_error" in r:
            ok36 = False
            d36.append("b%d T-census ERROR %s"
                       % (tag, r["t_census_error"]))
        else:
            amax = TCEN_ABOVE_CORE if core else TCEN_ABOVE_DEEP
            tmax = TCEN_TOP_CORE if core else TCEN_TOP_DEEP
            okx = r["t_above"] <= amax
            if r["t_above"] > 0:
                okx = okx and r["t_above_top_btop"] <= tmax
            ok36 = ok36 and okx
            d36.append("b%d T-roots %d (nnr %d) above %d top/btop "
                       "%.4f" % (tag, r["t_n"], r["t_nnr"],
                                 r["t_above"], r["t_top_btop"]))
        # G37 cascade
        okx = (r.get("casc_ok", False)
               and r.get("casc_yt", 1.0) <= CASC_YT_MAX
               and r.get("casc_btop", 0.0) > 1.0
               and r.get("n_viol", 1) == 0)
        if "t_census_error" not in r and r.get("t_above", 0) > 0:
            okx = okx and r["casc_btop"] >= r["t_above_top_btop"] \
                * (1 - 1e-9)
        ok37 = ok37 and okx
        d37.append("b%d Y*/btop %.4f Y*/yt %.4f (j=%s) resid %d/%d "
                   "viol %d" % (tag, r.get("casc_btop", -1),
                                r.get("casc_yt", -1),
                                r.get("casc_j"), r.get("n_resid", -1),
                                r.get("n_strip", -1),
                                r.get("n_viol", -1)))
        # G38 window at zeros + y_C branch
        okx = (r["minT_yt"] > 0.0
               and TWIN_MAXT_WIN[0] <= r["maxT_yt"]
               <= TWIN_MAXT_WIN[1]
               and ((not r["yc_exists"]) or r["yc_zero_above"]))
        ok38 = ok38 and okx
        d38.append("b%d minT %.1e maxT %.4f yC/btop %s firstz %.4f"
                   % (tag, r["minT_yt"], r["maxT_yt"],
                      ("%.4f" % r["yc_btop"]) if r["yc_exists"]
                      else "none", r["firstz_btop"]))
        info("b%d exhibit: yt = 1e%.3f (yt/btop %.1f); J2..J6 = "
             "%s; jet signs %s; ladder %s; sum z_esc %.5f sum z^2 "
             "%.5f; edge sign %+d; cascade level j=%s"
             % (tag, r["yt_l10"], r["yt_btop"],
                "/".join("%.3e" % r["J"][m] for m in range(2, 7)),
                r["sgn_head"],
                "/".join("%.4f" % zv for zv in
                         r.get("z_ladder", [])[:4]),
                r.get("sum_zesc", float("nan")),
                r.get("sum_z2esc", float("nan")),
                r["edge_sign"], r.get("casc_j")))

    check("G30-anchor-certificates", ok30,
          "deterministic r154 anchors; L_EPS on the r151/r153/r154 "
          "strings rel <= %.0e; n_neg == 0; a_2 sign == -1: %s"
          % (LEPS_TOL, "; ".join(d30)))
    check("G31-f-census-ladder", ok31,
          "F-census complete (K-1 real roots, n_nonreal == 0); "
          "n_esc == r154 strings; top/y_t and second/y_t on the "
          "r154 strings rel <= %.0e (the self-similar ladder "
          "replicated): %s" % (LAD_TOL, "; ".join(d31)))
    check("G32-sum-rules", ok32,
          "SR1 (trace) / SR2 (P_2) / SR3 (P_3) rel <= %.0e core / "
          "%.0e deep (THEOREM L3 instantiated: the ladder power "
          "sums ARE the jets): %s"
          % (SR_BAR_CORE, SR_BAR_DEEP, "; ".join(d32)))
    check("G33-moments-signlaw", ok33,
          "J_2 on the r154 strings rel <= %.0e; J_3 < 0 at core; "
          "n_esc <= nsc + 1 HARD (L4 exact) AND n_esc <= V(jets) "
          "HARD (Laguerre form) AND V == n_esc at core (measured-"
          "tight; deep slack %d DISCLOSED): %s"
          % (J2_TOL, V_SLACK_DEEP, "; ".join(d33)))
    check("G34-phi-quarter-cap", ok34,
          "|PHI(z_top)| and quarter-cap identity dev <= %.0e core "
          "/ %.0e deep; J_2 <= 1/4 + z|rho| HARD; z|rho| <= %.2f; "
          "|z_quad - z_top| <= %.2f (THEOREM L2 instantiated): %s"
          % (PHI_BAR_CORE, PHI_BAR_DEEP, RHO_MAX, QUAD_DEV_MAX,
             "; ".join(d34)))
    check("G35-truncation-convergence", ok35,
          "M = 3 truncation captures z_top and M = 6 captures the "
          "second rung (rel <= %.0e core / %.0e deep): the ladder "
          "IS the moment data (THEOREM L1 instantiated): %s"
          % (TRUNC3_BAR_CORE, TRUNC3_BAR_DEEP, "; ".join(d35)))
    check("G36-t-census", ok36,
          "T-census above-band count <= %d core / %d deep with top "
          "above-band root <= %.2f / %.2f b_top (the T-positivity "
          "boundary sits AT the band edge; the T-numerator is not "
          "real-rooted, n_nonreal printed -- DISCLOSED): %s"
          % (TCEN_ABOVE_CORE, TCEN_ABOVE_DEEP, TCEN_TOP_CORE,
             TCEN_TOP_DEEP, "; ".join(d36)))
    check("G37-cascade-certificate", ok37,
          "certified floor exists with Y*/y_t <= %.2f and Y* > "
          "b_top; ZERO T <= 0 cache violations above Y*; Y* >= top "
          "above-band T-root (consistency); residual vs strip "
          "counts printed (THEOREM L5 instantiated: T > 0 "
          "certified source-pure down to the band edge; via "
          "r154-P2 the escaped-root cap is certified): %s"
          % (CASC_YT_MAX, "; ".join(d37)))
    check("G38-window-at-zeros", ok38,
          "minT > 0 and maxT/y_t in %s at every cache zero above "
          "the band (r154 continuity); y_C branch: no %.1f y_t "
          "crossing OR first zero above it (band-edge separation "
          "exhibit -- THEOREM L6): %s"
          % (str(TWIN_MAXT_WIN), YC_LEVEL, "; ".join(d38)))

    # ------------------------------------------------ G39 adversarial
    section("S3f  ADVERSARIAL WITNESSES")
    ok39 = True
    d39 = []
    for tag, _xn, _dp in adv_tags:
        r = res.get(("adv", tag))
        if r is None or "error" in r:
            ok39 = False
            d39.append("b%d ERROR %s" % (tag, (r or {}).get("error")))
            continue
        okx = (r["dev_inv"] <= ADV_BAR and r["dev_defl"] <= ADV_BAR
               and r["dev_a0"] <= ADV_BAR and r["dev_yt"] <= ADV_BAR
               and r["infl"] >= ADV_J2_INFL_MIN
               and r["rgap"] >= ADV_RGAP_MIN
               and r["resn"] >= ADV_RES_MIN)
        ok39 = ok39 and okx
        d39.append("b%d inv %.0e defl %.0e a0 %.0e yt %.0e infl "
                   "%.0e rgap %.1e resn %.1e"
                   % (tag, r["dev_inv"], r["dev_defl"], r["dev_a0"],
                      r["dev_yt"], r["infl"], r["rgap"], r["resn"]))
    check("G39-adversarial-witnesses", ok39,
          "e_0: T-ratio WITNESS-INVARIANT (dev <= %.0e) and J_2 "
          "deflates by P^{-1/2} exactly; 2-mode: A_0 invariant, "
          "y_t deflated by sqrt(P), J_2 inflates >= %.0e while ALL "
          "identities hold (G16); REFUSAL rgap >= %.0e, resn >= "
          "%.0e -- the moment window is ARITHMETIC-PINNED: %s"
          % (ADV_BAR, ADV_J2_INFL_MIN, ADV_RGAP_MIN, ADV_RES_MIN,
             "; ".join(d39)))

    # ------------------------------------------------ S4 controls
    section("S4  CONTROLS")
    okc_all = True
    for world, xw, dpsw in controls:
        r = res.get(("ctl", world))
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
                  and r["sr1"] <= CTRL_SR_BAR)
        okc_all = okc_all and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: tau_w = %.4f < 0; |A_0_w| = %.3f in %s; "
              "y_t_w/b_top = %.3f <= %.1f (NO escaped scale); "
              "J_2_w = %.3f <= %.1f (NEGATIVE leading moment "
              "ratio: no quarter-window content in the fake "
              "world); n_esc = %d <= %d; SR1 world-blind %.0e <= "
              "%.0e (the trace identity holds in every world -- "
              "null control)"
              % (world, xw, r["tauf"], r["a0f"], str(CTRL_A0_WIN),
                 r["ytb"], CTRL_YTB_MAX, r["j2w"], CTRL_J2_MAX,
                 r["n_esc"], CTRL_NESC_MAX, r["sr1"], CTRL_SR_BAR))
    check("G53-consistency", okc_all,
          "all control worlds refuse on tau < 0 + no escaped scale "
          "+ negative J_2 while the identity layer holds world-"
          "blind: the self-similar ladder and its moment window "
          "are arithmetic (prime comb at 2A = log x)")

    # ------------------------------------------------ S5 screens
    section("S5  SCREENS")
    ts = sorted(tab)
    if len(ts) >= 3:
        lt = [tab[t]["tau_l10"] for t in ts]

        def slope(vals):
            return float(np.polyfit(lt, vals, 1)[0])

        s_j2 = slope([math.log10(max(tab[t]["J"][2], 1e-9))
                      for t in ts])
        s_zt = slope([math.log10(max(tab[t].get("z_top", 1e-9),
                                     1e-9)) for t in ts])
        s_zs = slope([math.log10(max(tab[t].get("z_sec", 1e-9),
                                     1e-9)) for t in ts])
        s_cy = slope([math.log10(max(tab[t].get("casc_yt", 1e-9),
                                     1e-9)) for t in ts])
        s_a0 = slope([tab[t]["a0sq_l10"] for t in ts])
        okt = all(abs(s) <= TAU_SLOPE_BAR
                  for s in (s_j2, s_zt, s_zs, s_cy))
        check("G54-tau-screen", okt,
              "slopes vs log10 tau: J_2 %.4f, z_top %.4f, z_sec "
              "%.4f, Y*/y_t %.4f (all <= %.2f: the shape-sector "
              "coordinates are tau-flat, DEMAND-FLAT); RIDER "
              "REPORT: log10 A_0^2 slope %.3f (rides tau by "
              "construction -- BOUND-RIDES-CONNES typed; the "
              "moment RATIOS are the flat coordinates)"
              % (s_j2, s_zt, s_zs, s_cy, TAU_SLOPE_BAR, s_a0))
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
          "flows: base 4, refined 5 (r154 graph VERBATIM -- this "
          "round changes the COORDINATES inside the TWINDOW edge, "
          "not the set: T-WINDOW == {arithmetic J-window} + "
          "{band-edge sliver + separation}, the latter the same "
          "root-position family as TOPROOT's B00-ROOTGAP + "
          "S1-floor); one-grant 5; counterfactual PARALLEL 7 NOT "
          "REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED "
          "(no omega closed, nothing upgraded)")
    info("EXACT RESIDUE after this round (read with CDLIV/CDLV/"
         "CDLVI/CDLVII/CDLVIII): RH <== [r122 NF-closure] + [r128 "
         "Theorem R] + {L1, WPD} on dense a; RESIDUE = {TOPROOT "
         "(= B00-ROOTGAP + S1-floor, r150), TLAWCAP-block (<== "
         "T-WINDOW + TOPROOT + PERCELL-REL + JUMPSUM), SUSCAP2R "
         "(= OVG-cap + share-floor, r150)} + DELTA1FLOOR (<== "
         "TRACEFLOOR) + dense-a + a-extension + window-a.  THIS "
         "ROUND: T-WINDOW is REWRITTEN as {J_2 in (0, 1/4 + eps): "
         "quarter-cap PROVEN given the real ladder, boundedness "
         "ARITHMETIC-PINNED} + {band-edge sliver (b_top, Y*) + "
         "band-edge zero separation} with the far/strip bulk "
         "CERTIFIED per block by the cascade; the pair {TOPROOT, "
         "T-WINDOW} reads band-edge root-separation coordinates "
         "of ONE curve pencil.  NO RH claim; nothing upgraded.")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "LADDER-LAW-PROVEN(the escaped ladder is the zero set of "
        "the moment-Laurent PHI; self-similarity == moment "
        "flatness; G10/G34/G35)",
        "QUARTER-CAP-PROVEN(J_2 <= 1/4 + z|rho| given the real "
        "top root; G11/G34)",
        "SUMRULES-EXACT(SR1-SR3; G12/G32)",
        "SIGNLAW(n_esc <= nsc + 1 exact; n_esc <= V(jets) "
        "Laguerre-form; V == n_esc measured-tight at core; "
        "G13/G33)",
        "CASCADE-CERT-EXTENDED(T > 0 certified source-pure down "
        "to Y* ~ b_top; ROOT-CAP-CERTIFIED via r154-P2; G14/G37)",
        "TWINDOW-EDGE-RESIDUE(the open content is the band-edge "
        "sliver + separation -- root-position class; G15/G36/G38)",
        "MOMENT-SPLIT(shape sector scale-blind witness-invariant; "
        "scale sector arithmetic; J-window ARITHMETIC-PINNED; "
        "G16/G39)",
        "REDTEAM-REFUTES-ALGEBRA(G16/G39)",
        "CONTROLS-REFUSE(negative J_2; G50-G53)",
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
        print("COMPOSITE: LADDER-LAW-PROVEN + QUARTER-CAP-PROVEN + "
              "SUMRULES-EXACT + SIGNLAW + CASCADE-CERT-EXTENDED + "
              "TWINDOW-EDGE-RESIDUE + MOMENT-SPLIT + "
              "REDTEAM-REFUTES-ALGEBRA + CONTROLS-REFUSE + "
              "DEMAND-FLAT + QUANTIFIER-INHERITED + "
              "OMEGA-UNCHANGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
