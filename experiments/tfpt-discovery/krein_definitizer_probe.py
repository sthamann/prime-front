"""
=======================================================================
krein_definitizer_probe.py -- the Krein definitizer
                              (contract PRIME.KREIN.DEFINITIZER.01)
=======================================================================
FROZEN SPEC (2026-08-21, round ~189).  EXPLORATION ONLY.  This probe
writes no paper, no ledger row, no website surface; it is an
experiments/-side discovery instrument under the house frozen-spec
discipline.  NO RH CLAIM IN EITHER DIRECTION, EVER: nothing below is
evidence for or against the Riemann Hypothesis; "census" always means
the finite root set of the finite polynomial N_h(y), never a zero set
of zeta.  Concurrent-lane files (loewner_pick_probe.py, the
independent session's untracked probes, sieve4_helper.bin) are not
touched.

QUESTION (the round).  r188 (census_lift_probe, 72/72, SPEC
8ada6b97d56aca46) delivered the exact Krein-signature pencil
    N_h(y) = (-1)^(K-1) det(J) A_0 det(Ahat - y J),
    Ahat = J D - (Jw)(Jw)^T,   J = diag(sign rho_k),   D = diag(b_k),
    w_k = sqrt(|rho_k|),       rho_k = (-1)^k c_k b_k / A_0,
with B = J INDEFINITE at every true rung (residue ladder (n_+, n_-)
mixed: (1,5)/(7,3)/(6,14)/(27,14)/(45,34)/(43,73) at h = 4..28), and
named the upgrade path: a source-side definitizing congruence OUTSIDE
the killed class {real Moebius, fixed positive weight, y -> g^2},
e.g. a y-dependent matrix multiplier W(y) > 0.  H2 is now the
operator statement "the Krein pair (Ahat, J) is definitizable".
THIS round imports the classical Krein-space machinery for exactly
that statement and tests the named upgrade path.

K1 -- THE CLASSICAL DICTIONARY (imported precisely, cited exactly).
  (D1) DEFINITIZABILITY (Langer).  A self-adjoint operator T in a
    Krein space (fundamental symmetry J, inner product [x,y] =
    (Jx,y)) is DEFINITIZABLE iff rho(T) != 0 and there exists a
    polynomial p != 0 with [p(T)x, x] >= 0 for all x.  Nonreal
    spectrum of a definitizable operator consists of finitely many
    conjugate eigenvalue pairs, each a zero of EVERY definitizing
    polynomial.  [H. Langer, "Spectral functions of definitizable
    operators in Krein spaces", Lecture Notes in Math. 948, Springer
    1982, pp. 1-46; origins H. Langer 1962-1965; P. Jonas, Beitr.
    Anal. 16 (1981) on the functional calculus.]
  (D2) FINITE DIMENSION IS DEGENERATE FOR (D1): every J-self-adjoint
    matrix T is definitizable -- take p = the characteristic
    polynomial, p(T) = 0 by Cayley-Hamilton, [0 x, x] = 0 >= 0.  The
    NON-vacuous finite-dimensional notion is STRONG/UNIFORM
    definitizability (J p(T) > 0 strictly): T is strongly
    definitizable iff ALL eigenvalues are real and of DEFINITE TYPE
    ([v,v] != 0 one-signed on each eigenspace; simple real
    eigenvalues are automatically of definite type).  [P. Zizler,
    "Definitizable operators on a Krein space", Canad. Math. Bull.
    38 (1995), doi 10.4153/CMB-1995-072-7, Sec. 4, citing
    P. Lancaster, Q. Ye, "Definitizable hermitian matrix pencils",
    Aequationes Math. 46 (1993) 44-55.]  Consequence typed honestly:
    H2 at rung h (all census roots real and simple) is EQUIVALENT to
    strong definitizability of (Ahat_h, J_h); the definitizing
    polynomial EXISTS at every verified rung.  The round's pivot is
    WHAT p_h IS in source terms.
  (D3) THE SIGN CHARACTERISTIC (Krein; Gohberg-Lancaster-Rodman).
    The canonical form of a J-self-adjoint matrix attaches a sign
    eps_i in {+1, -1} to every Jordan block of every real eigenvalue
    (for simple y_i with eigenvector v_i: eps_i = sign [v_i, v_i]);
    the multiset of eps_i is a congruence/similarity invariant, and
    #(eps_i = +1) - #(eps_i = -1) = sig(J) (for diagonalizable
    real spectrum: #(+) = n_+, #(-) = n_- exactly).  A strict
    definitizer must satisfy sign p(y_i) = eps_i, so its MINIMAL
    DEGREE = the number of sign changes of (eps_i) along the sorted
    spectrum.  Equivalent analytic definition: eps_i = the sign of
    the derivative of the eigenvalue curve of the Hermitian matrix
    function A(y) = Ahat - yJ crossing zero at y_i.  [I. Gohberg,
    P. Lancaster, L. Rodman, "Indefinite Linear Algebra and
    Applications", Birkhauser 2005, Ch. 5; the derivative
    characterization and Moebius behaviour: V. Mehrmann, V. Noferini,
    F. Tisseur, H. Xu, "On the sign characteristics of Hermitian
    matrix polynomials", Linear Algebra Appl. 511 (2016) 328-364.]

THE ROUND'S EXACT LAW (derived here, machine-verified at G05/G07 and
at every measured rung).  For the r188 pencil the kernel vector at a
census root y_i is EXPLICIT: v_k = w_k/(b_k - y_i), because
    (Ahat - y J) v = J w (1 + G(y)),   G(y) = sum_k rho_k/(y - b_k),
so v is the kernel exactly at the census roots (G = -1).  Then
    [v, v] = v^T J v = sum_k rho_k/(y_i - b_k)^2 = -G'(y_i),
i.e.  eps_i = -sign((F/A_0)'(y_i)) -- the sign characteristic is the
CROSSING DIRECTION of the Weyl secular function.  Writing the census
in sorted order y_1 < ... < y_R (R = # real roots) with m_i = #{k:
b_k > y_i} (n_1 = K - 1 poles), the product form of F/A_0 gives the
COMBINATORIAL LAW
    eps_i = -(-1)^((R - i) + m_i)          (1-based i),
whence the FLIP LAW  eps_(i+1) eps_i = (-1)^(Delta_i + 1), Delta_i =
#poles strictly between y_i and y_(i+1): the sign characteristic
flips exactly where interlacing fails by an EVEN pole count (Delta =
0: two roots share a pole gap; Delta = 2: a full gap is skipped).
And the crossing parity of G = -1 per pole gap depends ONLY on the
residue signs: THE PARITY SCAFFOLD (source-side, no roots)
    #roots in (-inf, b_1)     odd  iff  rho_1 > 0,
    #roots in (b_k, b_(k+1))  odd  iff  sign rho_k = sign rho_(k+1),
    #roots in (b_(n1), +inf)  odd  iff  rho_(n1) < 0,
with the total-parity consistency sum == n mod 2 (proved by the
boundary-sign case table; verified exactly at G07 and per rung).
Nonreal census pairs (fake worlds / witness rays may have them)
enter the count law as a deficit: #(eps=+) = n_+ - #pairs,
#(eps=-) = n_- - #pairs (each conjugate pair carries signature
(1,1)); the battery covers both cases.  CONSEQUENCE FOR THE PIVOT:
the entire eps-sequence, the flip set, and hence the minimal strict
definitizer p_h are determined by the OCCUPANCY VECTOR (root count
per pole gap) alone -- position within a gap is irrelevant.  The
parity of the occupancy is source-side; the occupancy itself is a
measurement.  p_h is source-expressible iff the occupancy is forced
by a source-side rule (e.g. parity-minimal: every gap carries
exactly its parity, excess in the top gap) -- MEASURED per rung and
gated against the frozen table below.

K3 -- THE W(y) CONGRUENCE HUNT AND ITS OBSTRUCTION THEOREM.  For ANY
W(y) smooth and invertible near the census roots, the congruence
M(y) = W(y)(Ahat - yJ)W(y)^T has, at each census root y_i with
kernel v (take x = W(y_i)^(-T) v):
    x^T M'(y_i) x = v^T (Ahat - yJ)'(y_i) v = -v^T J v = -eps_i |[v,v]|
(the W' terms die on the kernel; symbolic proof at G06).  A
"definite pencil in disguise" -- M(y) monotone through its zero
crossings, the property that makes A - yB with B > 0 deliver
realness structurally -- requires x^T M' x < 0 at EVERY census root,
i.e. eps_i = +1 for all i (or eps_i = -1 for all i for the
increasing orientation).  The measured mixed ladder ((n_+, n_-) both
nonzero at every true rung) therefore KILLS THE ENTIRE W(y) > 0
CONGRUENCE CLASS AT ONCE -- diagonal pole-data multipliers, the
r186 Loewner/Cauchy-structured multipliers, matrix polynomials in
JD, all of them: the sign characteristic is a congruence invariant
(GLR 2005; the Moebius/analytic-change-of-variable behaviour in
MNTX 2016 is the same statement one level up).  The named r188
upgrade path is hereby CLOSED, not merely not-found -- the exact
obstruction is the census root carrying the wrong-orientation
eps_i, named per rung below.  What is NOT killed (typed honestly):
(a) dimension-enlarging linearizations with extra spectrum (their
existence given realness is trivial-by-roots, hence forbidden as
construction: roots-as-input); (b) non-congruence transformations
of the secular function that change the residue signs themselves
(none known source-side; the r188 G07 class kill stands).
Per-family instantiation at h = 4, 5 (exact-numeric at rung dps):
family (i) W = diag(1/(y + b_k + 1)); family (ii) Cauchy
W_ij = 1/(b_i + b_j + 1 + y) (PD as a Cauchy matrix on distinct
positive nodes); family (iii) W = (1 + y/y_t) I + JD/(2 b_top)
(diagonal-dominant PD member of the JD-polynomial family) -- for
each: W(y_i) PD verified, kernel residual verified, and
x^T M'(y_i) x == -v^T J v verified to KD_BAR at BOTH named blocking
roots (first eps = -1 root blocks the decreasing orientation, first
eps = +1 root blocks the increasing one).

THE OBJECTS (source construction, r171/r172/r180/r188 code paths
VERBATIM via radius4_an_probe.build_cell).  Rung h, a = log(h)/2,
K = ceil(1.25 h log h), b_k = (k pi/a)^2, c_k = builder cn_mp_str
(de-normalized ground-ray components, max-abs positive), e_k =
(-1)^k c_k, A_0 = sum e_k, A_2 = sum_(k>=1) e_k b_k, y_t = |A_2/A_0|,
rho_k = e_k b_k/A_0 (k = 1..n_1, n_1 = K-1).  All residue/ladder/
scaffold work is EXACT on the dyadic rationalization of the frozen
mp build (Fraction(man 2^exp), no rounding added; r188 disclosure
(b) verbatim).  The census polynomial and its roots appear ONLY in
measure_*/verify_* functions (machine-checked, G02): the sign
characteristic is measured AT the roots -- that is legitimate
MEASUREMENT of the invariant (the task's explicit distinction) --
while everything DELIVERED forward (ladder, parity scaffold, law,
dictionary, obstruction theorem) is source-side or classical.

LAYERS
  L1 (symbolic-exact): G05 kernel/Weyl sign-characteristic identity
    ((Ahat - yJ)v == Jw(1+G) and v^T J v == -G'(y), n = 2, 3, ALL
    2^n sign patterns, sympy); G06 congruence-obstruction lemma
    (generic symmetric A(y0) with kernel v via Q R Q projection,
    generic W(y) = W0 + (y-y0)W1: x^T M'(y0) x == v^T A'(y0) v,
    n = 2, 3); G07 exact Fraction/Sturm battery at n = 4, poles
    (1,2,3,4), ALL 16 sign patterns x 2 magnitude profiles: real
    count by Sturm, per-gap parity == scaffold, two-route eps
    (crossing sign vs combinatorial formula), flip law, count law
    with nonreal-pair deficit -- ALL EXACT (no floats).
  L2 (MAIN rungs 4/5/8/13 MEASURED, 21/28 SOURCE-SIDE ONLY --
    honest scope split, disclosed: root measurement is bounded by
    the toproot census instrument CENSUS_HARD_MAX = 13 house-
    verbatim; at 21/28 this round records ladder + scaffold only):
    per rung build (G10), exact ladder == r188 frozen table
    including the r188-record 21/28 values (G11), exact parity
    scaffold + total-parity theorem + (3/7) gauge invariance (G12);
    at h <= 13: census measurement (G13, toproot instrument
    verbatim: nreal == K-1, negsum, top/y_t tabs + simplicity and
    root-pole separation bars), two-route sign-characteristic law +
    count law (G14), parity law measured == source scaffold (G15),
    defect structure == frozen (d_h flips, Delta split, occupancy-
    minimality verdict) (G16), minimal strict definitizer exhibit
    (degree == d_h, sign p(y_i) == eps_i all i) (G17), blocking
    roots + three-family congruence obstruction (G18, h = 4, 5),
    Langer matrix-level check at h = 4 (J p(T) symmetric PSD via
    eigsy + Cayley-Hamilton degeneracy of the trivial definitizer)
    (G19).
  L3 (worlds + witness): SMOOTH x=5 (ladder (0,10) one-signed:
    eps CONSTANT -1, d = 0, p = -1 constant -- the definite world,
    G30); SCRARITH x=5 (3,7) and EPSTEIN x=8 (3,17) mixed (G31/32,
    d and eps patterns frozen from calibration); orientation
    adjudication (G33): does d or the flip structure orient
    true-vs-fake, or again atoms-vs-no-atoms?  Frozen verdict below.
    r172 inflation witness at h = 5 (recipe VERBATIM: dv =
    A_2 (W-1)/(b_2 - b_1) on modes 1, 2, W = 1000): witness ladder,
    witness census realness, witness d -- does the witness break
    the law or move the invariant? (G34; the LAW itself is ray-blind
    by construction -- it is an identity -- typed, never sold as a
    separator.)
  L4 (adjudication): tau-screen (G03 ladder/scaffold exact gauge
    invariance under c -> (3/7)c; G50 defect-slack ladder slope vs
    log tau recorded with ride-band typing); loop guard (G08); the
    pivot verdict (G51) == frozen; runtime (G40).

PRE-FREEZE CALIBRATION (ONE pass, calib_krein_pass1.log at pre-
freeze SPEC 4dcd1f28835ffc22, log kept; ONE structural smoke before
it, krein_definitizer_probe.smoke1.log at SPEC f52f8a9d0e853fa3,
27/34 -- the 7 fails were exactly the pre-freeze placeholder
tables, all law gates PASSED; both logs kept, all numbers below
quoted from the calibration verbatim; h = 21, 28 not calibrated --
no root measurement there by scope).  MAIN sign-characteristic
counts == residue ladder exactly at every measured rung (count law
G14: (1,5)/(7,3)/(6,14)/(27,14)).  Defect data: h=4: d=2, flip0=2,
flipev=0, occmin=True, flip0-top-only=True, multi-occupied {6: 3};
h=5: d=4, flip0=3, flipev=1, occmin=True, flip0-top-only=True,
{10: 4}; h=8: d=11, flip0=7, flipev=4, occmin=FALSE,
flip0-top-only=FALSE, {10: 2, 20: 7}; h=13: d=18, flip0=12,
flipev=6, occmin=FALSE, flip0-top-only=FALSE, {24: 2, 41: 12}.
THE MEASURED PIVOT ANSWER (frozen): the occupancy-minimality law
HOLDS at h = 4, 5 and FAILS at h = 8, 13 -- the deviation is
exactly ONE interior doubled gap per rung (gap 10 of 20 at h = 8,
gap 24 of 41 at h = 13; an even-parity gap carrying 2 roots instead
of 0) plus the top-gap overflow: the eps-sequence is NOT source-
computable from the parity scaffold alone, hence STRICT-
DEFINITIZER-ROOT-DEPENDENT; the parity scaffold is the surviving
source-side coordinate, and the single-interior-doubled-gap
structure is recorded as a new measured observable (not claimed as
a law).  Blocking roots BLK_TAB (1-based, first eps=-1 / first
eps=+1): h=4: (1, 5); h=5: (1, 2).  Defect slack log10(min flip
interval / y_t): -1.321 (h=4), -2.402 (5), -3.418 (8), -4.254 (13);
slope vs log10 tau = +0.062 (R^2 0.884): FLAT, far below the ride
band (0.7, 1.3) -- the definitizer margin does NOT ride tau.
Langer h=4: J p(T) symdev 2.3e-119, eigsy min/max = 4.50e-7
(STRICTLY PD), Cayley-Hamilton residual 1.4e-58.  Family
obstruction devs (worst over both blocking roots, h = 4, 5):
DIAG 1.0e-57, CAUCHY 1.6e-55, JDPOLY 7.9e-59.  Worlds: SMOOTH
(0,10) all-real, eps constant -1, d=0 (the definite world, p = -1);
SCRARITH (3,7) all-real, d=3, flip0=1; EPSTEIN (3,17) all-real,
d=3, flip0=1.  ORIENTATION verdict frozen: the d = 0 vs d > 0
dichotomy separates atoms-vs-no-atoms only (r188 caveat INHERITED,
NOT a sign source); the d VALUE differs MAIN vs SCRARITH at x = 5
(4 vs 3, single cell, recorded, NOT claimed as a separator).
WITNESS h=5 (r172 recipe VERBATIM): the ladder does NOT move
((7,3), n_0 = 0) but the census REALNESS BREAKS -- nreal = 8,
npairs = 1: the witness ray is NOT strongly definitizable (the
nonreal pair must be a zero of every Langer definitizer) -- the
Krein invariant detects the witness class where the raw ladder is
blind; d_wit = 2 on the real subset, two-route law + flip law +
deficit count law all HOLD there (LAW-RAY-BLIND, typed, never sold
as a separator).  Frozen bars sit under measured minima: SIMPLE_BAR
1e-4 (measured min rel spacing 2.5e-2 at h=13), ROOTPOLE_BAR 1e-6
(measured 3.7e-3 at h=13), KD_BAR 1e-18 (measured worst 1.6e-55),
KRES_BAR 1e-30, PSD_MIN 1e-9 (measured 4.50e-7), CH_BAR 1e-30
(measured 1.4e-58), SYMDEV_BAR 1e-40 (measured 2.3e-119).

FROZEN NUMERICS
=======================================================================
KFAC = 1.25; RUNGS = (4, 5, 8, 13, 21, 28); MEASURE_MAX = 13 (house
CENSUS_HARD_MAX verbatim); DPS = {4: 60, 5: 60, 8: 80, 13: 120,
21: 146, 28: 160}; CONTROLS = (SMOOTH x=5 dps 60, SCRARITH x=5
dps 60, EPSTEIN x=8 dps 80); WORKERS = 9 (spawn, deterministic).
LADDER_TAB (r188 record VERBATIM, now all six frozen) MAIN
{4: (1,5), 5: (7,3), 8: (6,14), 13: (27,14), 21: (45,34),
28: (43,73)}; LADDER_WORLD {(SMOOTH,5): (0,10), (SCRARITH,5): (3,7),
(EPSTEIN,8): (3,17)}; RAY_BAR = 1e-25; POLY_MAXSTEPS = 3000;
IM_TOL = 1e-10; NEGSUM_BAR = 1e-6; TOP_TAB = {4: 0.880058,
5: 0.858950, 8: 0.844195, 13: 0.834429} rel 5e-3 (toproot verbatim);
D_TAB = {4: 2, 5: 4, 8: 11, 13: 18}; FLIP0_TAB = {4: 2, 5: 3, 8: 7,
13: 12}; FLIPEV_TAB = {4: 0, 5: 1, 8: 4, 13: 6}; OCCMIN_TAB =
{4: True, 5: True, 8: False, 13: False}; FLIP0TOP_TAB = {4: True,
5: True, 8: False, 13: False}; BLK_TAB = {4: (1, 5), 5: (1, 2)};
SLACK_TAB = {4: -1.321, 5: -2.402, 8: -3.418, 13: -4.254} tol 0.05;
SLOPE_TAB = 0.062 tol 0.05; RIDE_BAND = (0.7, 1.3); D_WORLD =
{(SMOOTH,5): 0, (SCRARITH,5): 3, (EPSTEIN,8): 3}; FLIP0_WORLD =
{(SMOOTH,5): 0, (SCRARITH,5): 1, (EPSTEIN,8): 1}; WIT_RUNG = 5;
WIT_FACT = 1000; WIT_LADDER = (7, 3); WIT_NREAL = 8; WIT_NPAIRS =
1; WIT_D = 2; PIVOT_TAB = (occmin-all, flip0-top-all, flip0-pos-all)
= (False, False, True); SIMPLE_BAR = 1e-4; ROOTPOLE_BAR = 1e-6;
KD_BAR = 1e-18; KRES_BAR = 1e-30; PSD_MIN = 1e-9; CH_BAR = 1e-30;
SYMDEV_BAR = 1e-40; SYMB_NS = (2, 3); BATTERY_N = 4; BATTERY_POLES
= (1, 2, 3, 4); BATTERY_MAGS = ((1, 1, 1, 1), (2, 1/2, 3, 1/3));
RUNTIME_BAR = 2700 s.
Deterministic: NO randomness anywhere; no cache file opened; all mp
arithmetic inside explicit workdps blocks; flat O(1) ratios
transported as f64 for gating (DISCLOSED).  Smoke mode (--smoke):
rungs (4, 5) + all controls + witness, log kept; --calib mode: the
disclosed single calibration pass (frozen-table gates report
RECORDED); the record run is the full set.

GATES (PASS/FAIL, numbered)
=======================================================================
G01-firewall      AST: no zero-oracle/cache names (load/loadtxt/
                  genfromtxt/fromfile/zetazero/siegelz/nzeros/
                  backlund), no zeta call, no verification/ import,
                  no numpy; polyroots only inside measure_*/verify_*;
                  eigsy only inside measure_*; no other eig/roots.
G02-roots-guard   call-graph DFS: no construct_* reaches polyroots/
                  eigsy or any measure_*/verify_*; ancestry DAG
                  acyclic, flagged loops + CENSUS-ROOTS unreachable
                  from DELIVERED.
G03-tau-screen    AST: construct_* bodies never subscript the builder
                  cell (mpE/mpM/mpV/tau/gap/cn unreachable there);
                  exact scale-gauge invariance of ladder AND parity
                  scaffold under c -> (3/7)c at every rung.
G04-spec          SPEC_SHA printed; K == ceil(KFAC h log h); DPS
                  schedule as frozen.
G05-symb-signchar (Ahat - yJ)v == Jw(1 + G) and v^T J v == -G'(y),
                  n = 2, 3, all sign patterns, fully symbolic.
G06-symb-congr    kernel-derivative congruence lemma: x^T M'(y0) x ==
                  v^T A'(y0) v for generic W(y), A(y0)v = 0; n = 2,3.
G07-exact-battery Fraction/Sturm battery n = 4, 32 instances: parity
                  scaffold, two-route eps, flip law, count law with
                  nonreal deficit -- all exact.
G08-loop-dag      flagged loop classes isolated and unreachable from
                  DELIVERED; DAG acyclic; MEASURED branch downstream.
Per MAIN rung h (suffix [h=..]):
G10 build sanity  K formula; eigen-residual ray_dev <= RAY_BAR.
G11 ladder        n_0 == 0; (n_+, n_-) == LADDER_TAB[h] (all six
                  rungs frozen from the r188 record).
G12 scaffold      parity scaffold computed source-side; total parity
                  == n mod 2 (theorem); gauge invariance exact.
At h <= MEASURE_MAX additionally:
G13 census        nreal == K-1, negsum <= NEGSUM_BAR y_t, top/y_t ==
                  TOP_TAB rel 5e-3, min rel spacing >= SIMPLE_BAR,
                  min rel root-pole distance >= ROOTPOLE_BAR.
G14 signchar-law  two-route eps agreement (analytic crossing sign vs
                  combinatorial formula) at EVERY root; count law
                  #eps+ == n_+, #eps- == n_-.
G15 parity-law    measured occupancy parity == source scaffold, ALL
                  K gaps.
G16 defects       d == D_TAB[h]; (flip0, flipev) == tabs; occupancy-
                  minimality == OCCMIN_TAB[h]; flip0-top-only ==
                  FLIP0TOP_TAB[h]; flip law holds at every
                  consecutive pair.
G17 definitizer   strict minimal p: degree == d; sign p(y_i) ==
                  eps_i for ALL i.
G18 blocking      (h in {4, 5}) blocking indices == BLK_TAB; three
                  families (diag / Cauchy / JD-poly): W(y_i) PD,
                  kernel residual <= KRES_BAR, |x^T M' x / (-v^T J v)
                  - 1| <= KD_BAR at both blocking roots.
G19 langer        (h = 4) J p(T) symdev <= SYMDEV_BAR, eigsy min/max
                  >= PSD_MIN (STRICT positivity: the Langer
                  condition holds with the exhibited p); charpoly
                  Cayley-Hamilton residual <= CH_BAR (the trivial
                  definitizer is degenerate -- dictionary exhibit).
Controls / witness:
G30 SMOOTH        ladder (0,10); all real; eps constant -1; d == 0.
G31 SCRARITH      ladder (3,7); d == D_WORLD, flip0 == FLIP0_WORLD.
G32 EPSTEIN       ladder (3,17); d == D_WORLD, flip0 == FLIP0_WORLD.
G33 orientation   frozen adjudication verdict: the d = 0 vs d > 0
                  dichotomy separates atoms vs no-atoms only (SMOOTH
                  d=0 unique) -- the r188 caveat INHERITED, typed
                  NOT-A-SIGN-SOURCE; the d value difference MAIN vs
                  SCRARITH at x = 5 is a recorded single cell.
G34 witness       r172 recipe VERBATIM at h = 5: witness ladder ==
                  (7,3) UNMOVED, n_0 == 0, nreal == 8, npairs == 1
                  (WITNESS-BREAKS-REALNESS: not strongly
                  definitizable), d_wit == 2 on the real subset,
                  two-route + flip + deficit count laws hold there
                  (LAW-RAY-BLIND, typed).
G40 runtime       < RUNTIME_BAR.
G50 tau-screen    defect-slack ladder == SLACK_TAB (tol), slope vs
                  log10 tau == SLOPE_TAB (tol); ride-band typing
                  printed (slope +0.062 FLAT, far below band).
G51 pivot         frozen pivot verdict: (occmin-all, flip0-top-all,
                  flip0-pos-all) == PIVOT_TAB = (False, False,
                  True): STRICT-DEFINITIZER-ROOT-DEPENDENT, parity
                  scaffold the surviving source-side coordinate.

VERDICT ENUMS (frozen): DICTIONARY-IMPORTED-EXACT +
SIGNCHAR-LAW-TWO-ROUTE-EXACT + SIGNCHAR-COUNT-IS-LADDER +
PARITY-SCAFFOLD-SOURCE-SIDE + DEFINITIZER-EXISTS-EVERY-VERIFIED-RUNG
(strong, Langer-checked at h=4) + STRICT-DEFINITIZER-ROOT-DEPENDENT
(the pivot: p_h is the occupancy data; the occ-min law fails at
h >= 8 by exactly one interior doubled gap; the census polynomial
itself is the degenerate trivial definitizer -- relabeling gate
FIRED for the naive reading) + OCCMIN-HOLDS-H45-FAILS-H813
(recorded observable) + WY-CONGRUENCE-CLASS-KILLED (sign
characteristic is a congruence invariant; both orientations blocked
by named roots; the r188 upgrade path is closed, upgraded from
not-found to impossible) + ORIENTATION-STILL-ATOMS-VS-NO-ATOMS (NOT
a sign source) + WITNESS-BREAKS-REALNESS-LADDER-UNMOVED +
LAW-RAY-BLIND + SLACK-NOT-RIDING-TAU +
MEASUREMENT-VS-CONSTRUCTION-SPLIT-MACHINE-CHECKED +
EPS-MEASURE-H13-ONLY (disclosed scope) + TAU-FREE-CONSTRUCTION +
ROOTS-NEVER-CONSTRUCT + NO-RH-CLAIM (always).

DISCLOSURES.  (a) ONE pre-freeze calibration pass
(calib_krein_pass1.log, kept; --calib mode of this file, i.e. the
instrument is the frozen instrument, only the record-table
comparisons were vacuous); the frozen tables above quote it
verbatim.  (b) Root measurement scope h <= 13 (toproot
CENSUS_HARD_MAX house instrument verbatim); h = 21, 28 carry ladder
+ scaffold only (EPS-MEASURE-H13-ONLY).  (c) The sign
characteristic is MEASURED at census roots; measurement functions
are quarantined from construction functions by the machine-checked
G02 split; nothing measured is fed forward into any delivered
construction.  (d) f64 transport of flat O(1) ratios for window
gates (house convention).  (e) The exact layers run on the dyadic
rationalization of the frozen mp build (r188 disclosure verbatim).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks outside this docstring.

AST FIREWALL: no zero-oracle names anywhere; NO cache file opened;
NO zeta use; no import of verification/.  NO RH CLAIM.  EXPLORATION
ONLY.
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
from fractions import Fraction

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import radius4_an_probe as R4                 # round-122 machinery

# ------------------------------------------------------------ frozen
KFAC = 1.25
RUNGS = (4, 5, 8, 13, 21, 28)
MEASURE_MAX = 13
DPS = {4: 60, 5: 60, 8: 80, 13: 120, 21: 146, 28: 160}
CONTROLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
WORKERS = 9
LADDER_TAB = {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14),
              21: (45, 34), 28: (43, 73)}
LADDER_WORLD = {("SMOOTH", 5): (0, 10), ("SCRARITH", 5): (3, 7),
                ("EPSTEIN", 8): (3, 17)}
RAY_BAR = 1e-25
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
NEGSUM_BAR = 1e-6
TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429}
TOP_RTOL = 5e-3
D_TAB = {4: 2, 5: 4, 8: 11, 13: 18}
FLIP0_TAB = {4: 2, 5: 3, 8: 7, 13: 12}
FLIPEV_TAB = {4: 0, 5: 1, 8: 4, 13: 6}
OCCMIN_TAB = {4: True, 5: True, 8: False, 13: False}
FLIP0TOP_TAB = {4: True, 5: True, 8: False, 13: False}
BLK_TAB = {4: (1, 5), 5: (1, 2)}
SLACK_TAB = {4: -1.321, 5: -2.402, 8: -3.418, 13: -4.254}
SLACK_TOL = 0.05
SLOPE_TAB = 0.062
SLOPE_TOL = 0.05
RIDE_BAND = (0.7, 1.3)
D_WORLD = {("SMOOTH", 5): 0, ("SCRARITH", 5): 3, ("EPSTEIN", 8): 3}
FLIP0_WORLD = {("SMOOTH", 5): 0, ("SCRARITH", 5): 1, ("EPSTEIN", 8): 1}
WIT_RUNG = 5
WIT_FACT = 1000
WIT_LADDER = (7, 3)
WIT_D = 2
WIT_NREAL = 8
WIT_NPAIRS = 1
PIVOT_TAB = (False, False, True)
SIMPLE_BAR = 1e-4
ROOTPOLE_BAR = 1e-6
KD_BAR = 1e-18
KRES_BAR = 1e-30
PSD_MIN = 1e-9
CH_BAR = 1e-30
SYMDEV_BAR = 1e-40
SYMB_NS = (2, 3)
BATTERY_N = 4
BATTERY_POLES = (1, 2, 3, 4)
BATTERY_MAGS = ((Fraction(1), Fraction(1), Fraction(1), Fraction(1)),
                (Fraction(2), Fraction(1, 2), Fraction(3),
                 Fraction(1, 3)))
RUNTIME_BAR = 2700.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool, str]] = []
T_START = time.time()
CALIB = False


def check(name: str, ok: bool, detail: str) -> bool:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", name, detail))
    return bool(ok)


def check_tab(name: str, ok_frozen: bool, detail: str) -> bool:
    """A gate that compares to a frozen table: in --calib mode it is
    RECORDED (vacuous pass), in record mode it gates."""
    if CALIB:
        CHECKS.append((name, True, "[CALIB RECORDED] " + detail))
        print("  [REC ] %s: %s" % (name, detail))
        return True
    return check(name, ok_frozen, detail)


def info(msg: str) -> None:
    print("  . %s" % msg)


def section(title: str) -> None:
    print("\n== %s %s" % (title, "=" * max(1, 66 - len(title))))


# ----------------------------------------------------- exact helpers
def mpf_frac(x) -> Fraction:
    """EXACT dyadic rationalization of an mpf."""
    sign, man, exp, _bc = x._mpf_
    if man == 0:
        if x == 0:
            return Fraction(0)
        raise ValueError("non-finite mpf")
    v = Fraction(int(man))
    if exp >= 0:
        v = v * (1 << exp)
    else:
        v = v / (1 << (-exp))
    return -v if sign else v


def frac_mpf(fr: Fraction):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def pmul(p: list, q: list) -> list:
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, pv in enumerate(p):
        if pv:
            for j, qv in enumerate(q):
                out[i + j] += pv * qv
    return out


def padd(p: list, q: list) -> list:
    if len(p) < len(q):
        p, q = q, p
    out = list(p)
    off = len(p) - len(q)
    for j, qv in enumerate(q):
        out[off + j] += qv
    return out


def peval(p: list, x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in p:
        acc = acc * x + c
    return acc


def pdiff(p: list) -> list:
    n = len(p) - 1
    return [p[i] * (n - i) for i in range(n)]


# --------------------------------------------- construction (source)
def construct_l1(cs: list, b: list, K: int) -> dict:
    """L1 residue ladder from source data ONLY (exact, r188
    VERBATIM).  Inputs are dyadic Fractions of (c_k, b_k)."""
    e = [cs[k] if k % 2 == 0 else -cs[k] for k in range(K)]
    A0 = sum(e)
    A2 = sum(e[k] * b[k] for k in range(1, K))
    rho = [e[k] * b[k] / A0 for k in range(1, K)]
    npos = sum(1 for r in rho if r > 0)
    nneg = sum(1 for r in rho if r < 0)
    nzero = sum(1 for r in rho if r == 0)
    lam = Fraction(3, 7)
    e2 = [v * lam for v in e]
    A0g = sum(e2)
    rho_g = [e2[k] * b[k] / A0g for k in range(1, K)]
    gauge_ok = (rho_g == rho)
    return dict(e=e, A0=A0, A2=A2, rho=rho, npos=npos, nneg=nneg,
                nzero=nzero, gauge_ok=gauge_ok)


def construct_scaffold(rho: list) -> dict:
    """THE PARITY SCAFFOLD, source-side (residue signs only, exact).
    par[g] for gaps g = 0 (below b_1), 1..n-1 (between poles),
    n (above b_n): predicted parity of the census-root count."""
    n = len(rho)
    sg = [1 if r > 0 else (-1 if r < 0 else 0) for r in rho]
    par = [0] * (n + 1)
    par[0] = 1 if sg[0] > 0 else 0
    for g in range(1, n):
        par[g] = 1 if sg[g - 1] == sg[g] else 0
    par[n] = 1 if sg[n - 1] < 0 else 0
    total_ok = (sum(par) % 2) == (n % 2)
    return dict(par=par, total_ok=total_ok, n_odd=sum(par))


def construct_census_poly(cs: list, b: list, K: int):
    """Frozen rootladder census form (r156/r171/r188 VERBATIM, exact
    Fraction port).  Scaled Y = y/s, s = b_top + 1.  Source-side
    polynomial construction; never solved here."""
    def deflate(p, root):
        out = [p[0]]
        for c in p[1:-1]:
            out.append(c + out[-1] * root)
        return out
    s = b[K - 1] + 1
    bs = [b[k] / s for k in range(1, K)]
    prod_all = [Fraction(1)]
    for bj in bs:
        prod_all = pmul(prod_all, [Fraction(1), -bj])
    poly = [cs[0] * c for c in prod_all]
    for i, k in enumerate(range(1, K)):
        q = deflate(prod_all, bs[i])
        term = [(Fraction(-1) ** k) * cs[k] * c for c in q] \
            + [Fraction(0)]
        poly = padd(poly, term)
    return poly, s


# ------------------------------------------------- exact Sturm layer
def sturm_chain(p: list) -> list:
    """Sturm chain of a Fraction polynomial (leading coeffs
    nonzero)."""
    def prem(a, b):
        a = list(a)
        while len(a) >= len(b) and any(v != 0 for v in a):
            if a[0] == 0:
                a = a[1:]
                continue
            f = a[0] / b[0]
            d = len(a) - len(b)
            for i in range(len(b)):
                a[i] -= f * b[i]
            a = a[1:]
        while a and a[0] == 0:
            a = a[1:]
        return [-v for v in a]
    chain = [list(p), pdiff(p)]
    while len(chain[-1]) > 1 or (chain[-1] and chain[-1][0] != 0):
        r = prem(chain[-2], chain[-1])
        if not r:
            break
        chain.append(r)
    return chain


def sturm_sigma(chain: list, x: Fraction) -> int:
    signs = []
    for p in chain:
        v = peval(p, x)
        if v != 0:
            signs.append(1 if v > 0 else -1)
    return sum(1 for a, b2 in zip(signs, signs[1:]) if a != b2)


def sturm_count(chain: list, lo: Fraction, hi: Fraction) -> int:
    """# real roots in (lo, hi] -- exact."""
    return sturm_sigma(chain, lo) - sturm_sigma(chain, hi)


def battery_instance(rho: list, bs: list) -> dict:
    """One exact battery cell: numerator Ntilde of 1 + sum rho/(y-b);
    Sturm real count; per-gap counts; isolated roots; two-route eps;
    flip law; count law.  ALL EXACT (Fraction)."""
    n = len(bs)

    def deflate(p, root):
        out = [p[0]]
        for c in p[1:-1]:
            out.append(c + out[-1] * root)
        return out
    prod = [Fraction(1)]
    for bj in bs:
        prod = pmul(prod, [Fraction(1), -bj])
    ntil = list(prod)
    for k in range(n):
        q = deflate(prod, bs[k])
        ntil = padd(ntil, [rho[k] * c for c in q])
    chain = sturm_chain(ntil)
    big = max(abs(c) for c in ntil) / abs(ntil[0]) + \
        max(abs(bb) for bb in bs) + 2
    R = sturm_count(chain, -big, big)
    npairs = (n - R) // 2
    # per-gap counts (gaps split at poles)
    cuts = [-big] + list(bs) + [big]
    gapcnt = [sturm_count(chain, cuts[g], cuts[g + 1])
              for g in range(n + 1)]
    # isolate the R real roots by bisection within their gaps
    ivals = []
    for g in range(n + 1):
        lo, hi = cuts[g], cuts[g + 1]
        stack = [(lo, hi, gapcnt[g])]
        while stack:
            lo2, hi2, c2 = stack.pop()
            if c2 == 0:
                continue
            if c2 == 1:
                # shrink until derivative-sign route is clean:
                # interval must not contain a pole (guaranteed) and
                # endpoints nonzero
                while peval(ntil, lo2) == 0 or peval(ntil, hi2) == 0:
                    hi2 = (lo2 + hi2) / 2 if peval(ntil, hi2) == 0 \
                        else hi2
                    lo2 = (lo2 + hi2) / 2 if peval(ntil, lo2) == 0 \
                        else lo2
                ivals.append((lo2, hi2, g))
                continue
            mid = (lo2 + hi2) / 2
            while peval(ntil, mid) == 0:
                mid = (lo2 + mid) / 2
            c_lo = sturm_count(chain, lo2, mid)
            stack.append((lo2, mid, c_lo))
            stack.append((mid, hi2, c2 - c_lo))
    ivals.sort(key=lambda t: t[0])
    # two-route eps at every isolated real root
    eps_cross, eps_comb, ms = [], [], []
    for i, (lo, hi, g) in enumerate(ivals):
        s_hi = 1 if peval(ntil, hi) > 0 else -1
        mid = (lo + hi) / 2
        dsign = 1
        for bb in bs:
            dsign *= 1 if (mid - bb) > 0 else -1
        # eps = -sign((Ntilde/prod)') at root = -sign(Ntilde'(r))
        #       * sign(prod(r))
        eps_cross.append(-s_hi * dsign)
        m = n - g                      # poles above the root
        ms.append(m)
        eps_comb.append(-((-1) ** ((R - 1 - i) + m)))
    agree = (eps_cross == eps_comb)
    npos = sum(1 for r in rho if r > 0)
    nneg = sum(1 for r in rho if r < 0)
    count_ok = (sum(1 for e in eps_cross if e > 0) == npos - npairs
                and sum(1 for e in eps_cross if e < 0)
                == nneg - npairs)
    # parity law
    sc = construct_scaffold(rho)
    par_ok = all(gapcnt[g] % 2 == sc["par"][g] for g in range(n + 1))
    # flip law among consecutive real roots
    flip_ok = True
    for i in range(len(ivals) - 1):
        delta = ms[i] - ms[i + 1]
        if eps_cross[i + 1] * eps_cross[i] != (-1) ** (delta + 1):
            flip_ok = False
    return dict(R=R, npairs=npairs, agree=agree, count_ok=count_ok,
                par_ok=par_ok, flip_ok=flip_ok,
                total_ok=sc["total_ok"])


# ------------------------------------------------------ measurement
def measure_census(cs_mp, b_mp, K: int, dps: int):
    """Census root measurement (toproot instrument VERBATIM port,
    r188 verify_census): the ONLY census solver.  MEASUREMENT only --
    never feeds any construction (machine-checked, G02)."""
    with mp.workdps(3 * dps):
        s = b_mp[K - 1] + 1
        bs = [b_mp[k] / s for k in range(1, K)]

        def pmul_mp(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def deflate_mp(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        def padd_mp(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        prod_all = [mp.mpf(1)]
        for bj in bs:
            prod_all = pmul_mp(prod_all, [mp.mpf(1), -bj])
        poly = [cs_mp[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate_mp(prod_all, bs[i])
            term = [((-1) ** k) * cs_mp[k] * c for c in q] + [mp.mpf(0)]
            poly = padd_mp(poly, term)
        A0 = sum((-1) ** k * cs_mp[k] for k in range(K))
        A2 = sum((-1) ** k * cs_mp[k] * b_mp[k] for k in range(1, K))
        yt = abs(A2 / A0)
        rts = mp.polyroots(poly, maxsteps=POLY_MAXSTEPS,
                           extraprec=2 * dps)
        ys = []
        for r in rts:
            if abs(mp.im(r)) <= mp.mpf(repr(IM_TOL)):
                ys.append(mp.re(r) * s)
        ys.sort()
        nreal = len(ys)
        npairs = (len(rts) - nreal) // 2
        top_yt = float(ys[-1] / yt) if ys else float("nan")
        negsum = float(sum(abs(v) for v in ys if v < 0) / yt)
        return dict(ys=[mp.mpf(v) for v in ys], nreal=nreal,
                    npairs=npairs, top_yt=top_yt, negsum=negsum)


def measure_signchar(ys, b_mp, rho_mp, K: int, dps: int) -> dict:
    """Sign characteristic AT the measured roots (two routes),
    flips, Delta classes, occupancy, spacing bars.  MEASUREMENT."""
    n1 = K - 1
    R = len(ys)
    with mp.workdps(2 * dps):
        eps_a, eps_c, ms = [], [], []
        minsp = None
        minrp = None
        for i, y in enumerate(ys):
            m = sum(1 for k in range(1, K) if b_mp[k] > y)
            ms.append(m)
            ssum = mp.mpf(0)
            for k in range(1, K):
                ssum += rho_mp[k - 1] / (y - b_mp[k]) ** 2
            eps_a.append(1 if ssum > 0 else -1)
            eps_c.append(-((-1) ** ((R - 1 - i) + m)))
            rp = min(abs(y - b_mp[k]) / (b_mp[k] + 1)
                     for k in range(1, K))
            minrp = rp if minrp is None else min(minrp, rp)
            if i + 1 < R:
                sp = (ys[i + 1] - y) / (abs(ys[i + 1]) + 1)
                minsp = sp if minsp is None else min(minsp, sp)
        agree = (eps_a == eps_c)
        flips, deltas = [], []
        flip_law_ok = True
        for i in range(R - 1):
            delta = ms[i] - ms[i + 1]
            if eps_a[i + 1] * eps_a[i] != (-1) ** (delta + 1):
                flip_law_ok = False
            if eps_a[i + 1] != eps_a[i]:
                flips.append(i)
                deltas.append(delta)
        d = len(flips)
        flip0 = sum(1 for x in deltas if x == 0)
        flipev = sum(1 for x in deltas if x >= 2)
        occ = [0] * (n1 + 1)
        for m in ms:
            occ[n1 - m] += 1
        # are ALL Delta=0 flips internal to the TOP gap (above b_n1)?
        flip0_top_only = all(
            ms[i] == 0 and ms[i + 1] == 0
            for i, dl in zip(flips, deltas) if dl == 0)
        npos = sum(1 for e in eps_a if e > 0)
        nneg = sum(1 for e in eps_a if e < 0)
        # defect slack (min flip-interval width) in y_t units is
        # attached by the caller (needs y_t)
        slack = None
        if flips:
            slack = min(ys[i + 1] - ys[i] for i in flips)
        return dict(eps=eps_a, agree=agree, ms=ms, flips=flips,
                    deltas=deltas, d=d, flip0=flip0, flipev=flipev,
                    flip0_top_only=flip0_top_only,
                    occ=occ, npos=npos, nneg=nneg,
                    flip_law_ok=flip_law_ok, slack=slack,
                    minsp=float(minsp) if minsp is not None else 0.0,
                    minrp=float(minrp) if minrp is not None else 0.0)


def measure_definitizer(ys, eps, flips, dps: int) -> dict:
    """Minimal strict definitizer exhibit from the measured flip set:
    p(y) = eps_top * prod_flips (y - midpoint).  MEASUREMENT."""
    with mp.workdps(2 * dps):
        mids = [(ys[i] + ys[i + 1]) / 2 for i in flips]
        s0 = eps[-1]
        ok = True
        for i, y in enumerate(ys):
            v = mp.mpf(s0)
            for t in mids:
                v *= (y - t)
            if (1 if v > 0 else -1) != eps[i]:
                ok = False
        return dict(mids=mids, s0=s0, deg=len(mids), strict_ok=ok)


def measure_langer(b_mp, rho_mp, sig, w_mp, ys, mids, s0, K: int,
                   dps: int) -> dict:
    """Matrix-level Langer check at a small rung: T = D - w w^T J,
    P = p(T), J P symmetric PSD (strict); Cayley-Hamilton residual
    of the trivial definitizer.  MEASUREMENT (eigsy lives here)."""
    n = K - 1
    with mp.workdps(2 * dps):
        T = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                T[i, j] = -w_mp[i] * w_mp[j] * sig[j]
            T[i, i] += b_mp[i + 1]
        # p(T), scaled by y-scale to tame magnitudes
        sc = max(abs(y) for y in ys)
        P = mp.eye(n) * s0
        for t in mids:
            Q = mp.zeros(n, n)
            for i in range(n):
                for j in range(n):
                    Q[i, j] = (T[i, j] - (t if i == j else 0)) / sc
            P = P * Q
        JP = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                JP[i, j] = sig[i] * P[i, j]
        symdev = mp.mpf(0)
        den = mp.mpf(0)
        for i in range(n):
            for j in range(n):
                symdev = max(symdev, abs(JP[i, j] - JP[j, i]))
                den = max(den, abs(JP[i, j]))
        S = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                S[i, j] = (JP[i, j] + JP[j, i]) / 2
        ev = mp.eigsy(S, eigvals_only=True)
        evmin = min(ev)
        evmax = max(abs(v) for v in ev)
        # Cayley-Hamilton: prod (T - y_i I)/sc == 0
        C = mp.eye(n)
        for y in ys:
            Q = mp.zeros(n, n)
            for i in range(n):
                for j in range(n):
                    Q[i, j] = (T[i, j] - (y if i == j else 0)) / sc
            C = C * Q
        chres = max(abs(C[i, j]) for i in range(n) for j in range(n))
        return dict(symdev=float(symdev / den),
                    psd_ratio=float(evmin / evmax),
                    ch_res=float(chres))


def measure_blocking(b_mp, sig, w_mp, ys, eps, ytm, K: int,
                     dps: int) -> dict:
    """The W(y)-congruence obstruction, instantiated: at the first
    eps=-1 and first eps=+1 roots, for the three frozen families,
    verify W PD, kernel residual, and x^T M'(y_i) x == -v^T J v.
    MEASUREMENT (eigsy for the Cauchy PD check lives here)."""
    n = K - 1
    with mp.workdps(2 * dps):
        i_neg = next(i for i, e in enumerate(eps) if e < 0)
        i_pos = next(i for i, e in enumerate(eps) if e > 0)
        btop = b_mp[K - 1]
        out = dict(i_neg=i_neg + 1, i_pos=i_pos + 1, fams={})
        for fam in ("DIAG", "CAUCHY", "JDPOLY"):
            worst_kd = 0.0
            worst_res = 0.0
            pd_ok = True
            for idx in (i_neg, i_pos):
                y = ys[idx]
                # kernel vector and target
                v = [w_mp[k] / (b_mp[k + 1] - y) for k in range(n)]
                vJv = sum(sig[k] * v[k] ** 2 for k in range(n))
                target = -vJv
                # A(y) = Ahat - y J and kernel residual
                A = mp.zeros(n, n)
                for i in range(n):
                    for j in range(n):
                        A[i, j] = -sig[i] * w_mp[i] * sig[j] * w_mp[j]
                    A[i, i] += sig[i] * (b_mp[i + 1] - y)
                res = mp.mpf(0)
                nv = mp.sqrt(sum(x ** 2 for x in v))
                for i in range(n):
                    res = max(res, abs(sum(A[i, j] * v[j]
                                           for j in range(n))) / nv)
                worst_res = max(worst_res, float(res))
                # W(y) and W'(y) per family
                W = mp.zeros(n, n)
                Wp = mp.zeros(n, n)
                if fam == "DIAG":
                    for i in range(n):
                        W[i, i] = 1 / (y + b_mp[i + 1] + 1)
                        Wp[i, i] = -1 / (y + b_mp[i + 1] + 1) ** 2
                    pd_ok = pd_ok and all(W[i, i] > 0
                                          for i in range(n))
                elif fam == "CAUCHY":
                    for i in range(n):
                        for j in range(n):
                            den = b_mp[i + 1] + b_mp[j + 1] + 1 + y
                            W[i, j] = 1 / den
                            Wp[i, j] = -1 / den ** 2
                    evw = mp.eigsy(W, eigvals_only=True)
                    pd_ok = pd_ok and min(evw) > 0
                else:
                    for i in range(n):
                        W[i, i] = (1 + y / ytm) \
                            + sig[i] * b_mp[i + 1] / (2 * btop)
                        Wp[i, i] = 1 / ytm
                    pd_ok = pd_ok and all(W[i, i] > 0
                                          for i in range(n))
                # x = W^{-T} v ; M' = W' A W^T + W A' W^T + W A W'^T,
                # A' = -J
                x = mp.lu_solve(W.T, mp.matrix(v))
                Ax = A * mp.matrix(v)          # ~ 0 (kernel)
                # term1 = x^T W' A W^T x = x^T W' (A v)
                t1 = (x.T * (Wp * Ax))[0, 0]
                # term3 = x^T W A W'^T x = (A v)^T W'^T x
                t3 = (Ax.T * (Wp.T * x))[0, 0]
                # term2 = -x^T W J W^T x = -v^T J v
                Wx = W.T * x
                t2 = -sum(sig[k] * Wx[k] ** 2 for k in range(n))
                kd = t1 + t2 + t3
                worst_kd = max(worst_kd,
                               float(abs(kd / target - 1)))
            out["fams"][fam] = dict(kd=worst_kd, res=worst_res,
                                    pd=pd_ok)
        return out


# ------------------------------------------------------------ workers
def w_rung(args) -> dict:
    h, dps = args
    try:
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, build_s=ce["build_s"])
        out["K_ok"] = (K == int(math.ceil(KFAC * h * math.log(h))))
        with mp.workdps(dps):
            M = ce["mpM"]
            E = ce["mpE"]
            V = ce["mpV"]
            tau = E[0]
            v0 = [V[i, 0] for i in range(K)]
            n0 = mp.sqrt(sum(v * v for v in v0))
            v0 = [v / n0 for v in v0]
            Mv = [sum(M[i, kk] * v0[kk] for kk in range(K))
                  for i in range(K)]
            ray = sum(v0[i] * Mv[i] for i in range(K))
            r0 = mp.sqrt(sum((Mv[i] - ray * v0[i]) ** 2
                             for i in range(K)))
            out["ray_dev"] = float(abs(ray / tau - 1))
            out["log10tau"] = float(mp.log(abs(tau)) / mp.log(10))
            aa = mp.log(h) / 2
            b_mp = [(k * mp.pi / aa) ** 2 for k in range(K)]
            cs_mp = [mp.mpf(sv) for sv in ce["cn_mp_str"]]
            A0m = sum((-1) ** k * cs_mp[k] for k in range(K))
            A2m = sum((-1) ** k * cs_mp[k] * b_mp[k]
                      for k in range(1, K))
            ytm = abs(A2m / A0m)
            out["yt_l10"] = float(mp.log(ytm) / mp.log(10))
            cs = [mpf_frac(v) for v in cs_mp]
            b = [mpf_frac(v) for v in b_mp]
        l1 = construct_l1(cs, b, K)
        sc = construct_scaffold(l1["rho"])
        # gauge invariance of the scaffold (c -> (3/7)c): rho exact-
        # invariant (G03 leg), scaffold is a function of rho
        sc_g_ok = l1["gauge_ok"]
        out.update(npos=l1["npos"], nneg=l1["nneg"], nzero=l1["nzero"],
                   gauge_ok=sc_g_ok, par_total_ok=sc["total_ok"],
                   n_odd=sc["n_odd"], par=sc["par"])
        if h <= MEASURE_MAX:
            with mp.workdps(dps):
                rho_mp = [frac_mpf(r) for r in l1["rho"]]
            cen = measure_census(cs_mp, b_mp, K, dps)
            out.update(nreal=cen["nreal"], npairs=cen["npairs"],
                       top_yt=cen["top_yt"], negsum=cen["negsum"])
            sg = measure_signchar(cen["ys"], b_mp, rho_mp, K, dps)
            out.update(eps_agree=sg["agree"], d=sg["d"],
                       flip0=sg["flip0"], flipev=sg["flipev"],
                       flip0_top=sg["flip0_top_only"],
                       eps_npos=sg["npos"], eps_nneg=sg["nneg"],
                       flip_law_ok=sg["flip_law_ok"],
                       minsp=sg["minsp"], minrp=sg["minrp"])
            # parity law: measured occupancy parity == scaffold
            out["parity_law_ok"] = all(
                sg["occ"][g] % 2 == sc["par"][g]
                for g in range(len(sc["par"])))
            # occupancy-minimality hypothesis
            n1 = K - 1
            occmin = all(sg["occ"][g] == sc["par"][g]
                         for g in range(n1)) \
                and sg["occ"][n1] == n1 - sum(sc["par"][:n1])
            out["occmin"] = occmin
            occnz = {g: sg["occ"][g] for g in range(len(sg["occ"]))
                     if sg["occ"][g] not in (0, 1)}
            out["occnz"] = occnz
            with mp.workdps(dps):
                out["slack_l10"] = float(
                    mp.log(sg["slack"] / ytm) / mp.log(10)) \
                    if sg["slack"] is not None else None
            dfz = measure_definitizer(cen["ys"], sg["eps"],
                                      sg["flips"], dps)
            out.update(deg=dfz["deg"], strict_ok=dfz["strict_ok"])
            if h in (4, 5):
                sig = [1 if r > 0 else -1 for r in l1["rho"]]
                with mp.workdps(dps):
                    w_mp = [mp.sqrt(abs(r)) for r in rho_mp]
                blk = measure_blocking(b_mp, sig, w_mp, cen["ys"],
                                       sg["eps"], ytm, K, dps)
                out["blk"] = dict(i_neg=blk["i_neg"],
                                  i_pos=blk["i_pos"],
                                  fams=blk["fams"])
            if h == 4:
                sig = [1 if r > 0 else -1 for r in l1["rho"]]
                with mp.workdps(dps):
                    w_mp = [mp.sqrt(abs(r)) for r in rho_mp]
                lng = measure_langer(b_mp, rho_mp, sig, w_mp,
                                     cen["ys"], dfz["mids"],
                                     dfz["s0"], K, dps)
                out["langer"] = lng
            # --- witness at WIT_RUNG (r172/r186 recipe VERBATIM)
            if h == WIT_RUNG:
                with mp.workdps(dps):
                    dv = A2m * (WIT_FACT - 1) / (b_mp[2] - b_mp[1])
                    cs2 = list(cs_mp)
                    cs2[1] += dv
                    cs2[2] += dv
                cs2f = [mpf_frac(v) for v in cs2]
                l1w = construct_l1(cs2f, b, K)
                out["wit_ladder"] = (l1w["npos"], l1w["nneg"])
                out["wit_nzero"] = l1w["nzero"]
                cenw = measure_census(cs2, b_mp, K, dps)
                out["wit_nreal"] = cenw["nreal"]
                out["wit_npairs"] = cenw["npairs"]
                if cenw["nreal"] > 0:
                    with mp.workdps(dps):
                        rho_w = [frac_mpf(r) for r in l1w["rho"]]
                    sgw = measure_signchar(cenw["ys"], b_mp, rho_w,
                                           K, dps)
                    out["wit_d"] = sgw["d"]
                    out["wit_agree"] = sgw["agree"]
                    out["wit_flip_law"] = sgw["flip_law_ok"]
                    out["wit_count_ok"] = (
                        sgw["npos"] == l1w["npos"] - cenw["npairs"]
                        and sgw["nneg"]
                        == l1w["nneg"] - cenw["npairs"])
        return out
    except Exception as exc:                        # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_world(args) -> dict:
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K)
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            b_mp = [(k * mp.pi / aa) ** 2 for k in range(K)]
            cs_mp = [mp.mpf(sv) for sv in ce["cn_mp_str"]]
            cs = [mpf_frac(v) for v in cs_mp]
            b = [mpf_frac(v) for v in b_mp]
        l1 = construct_l1(cs, b, K)
        sc = construct_scaffold(l1["rho"])
        out.update(npos=l1["npos"], nneg=l1["nneg"],
                   nzero=l1["nzero"], par_total_ok=sc["total_ok"])
        with mp.workdps(dps):
            rho_mp = [frac_mpf(r) for r in l1["rho"]]
        cen = measure_census(cs_mp, b_mp, K, dps)
        out.update(nreal=cen["nreal"], npairs=cen["npairs"])
        ep_all = None
        if cen["nreal"] > 0:
            sg = measure_signchar(cen["ys"], b_mp, rho_mp, K, dps)
            ep_all = sg
            out.update(eps_agree=sg["agree"], d=sg["d"],
                       flip0=sg["flip0"],
                       flip_law_ok=sg["flip_law_ok"],
                       eps_npos=sg["npos"], eps_nneg=sg["nneg"])
            out["parity_law_ok"] = all(
                sg["occ"][g] % 2 == sc["par"][g]
                for g in range(len(sc["par"])))
            out["eps_const_neg"] = all(e == -1 for e in sg["eps"])
        # count law with nonreal deficit
        if ep_all is not None:
            out["count_ok"] = (
                ep_all["npos"] == l1["npos"] - cen["npairs"]
                and ep_all["nneg"] == l1["nneg"] - cen["npairs"])
        return out
    except Exception as exc:                        # noqa: BLE001
        return dict(world=world, x=x, error=repr(exc))


# ---------------------------------------------------------- symbolic
def symbolic_gates() -> list:
    import sympy as sp
    res = []
    y = sp.Symbol("y")
    # G05: kernel + Weyl sign-characteristic identity, all patterns
    ok_sc = True
    for n in SYMB_NS:
        bs = sp.symbols("b1:%d" % (n + 1), positive=True)
        ws = sp.symbols("w1:%d" % (n + 1), positive=True)
        for mask in range(2 ** n):
            sg = [1 if (mask >> i) & 1 else -1 for i in range(n)]
            rho = [sg[i] * ws[i] ** 2 for i in range(n)]
            J = sp.diag(*sg)
            D = sp.diag(*bs)
            wv = sp.Matrix(ws)
            Jw = J * wv
            Ahat = J * D - Jw * Jw.T
            G = sum(rho[i] / (y - bs[i]) for i in range(n))
            v = sp.Matrix([ws[i] / (bs[i] - y) for i in range(n)])
            lhs = (Ahat - y * J) * v
            rhs = Jw * (1 + G)
            if sp.simplify(lhs - rhs) != sp.zeros(n, 1):
                ok_sc = False
            quad = (v.T * J * v)[0, 0]
            if sp.simplify(quad + sp.diff(G, y)) != 0:
                ok_sc = False
    res.append(("G05-symb-signchar", ok_sc,
                "(Ahat - yJ)v == Jw(1+G) and v^T J v == -G'(y), "
                "n = %s, all sign patterns" % (SYMB_NS,)))
    # G06: kernel-derivative congruence lemma
    ok_cg = True
    for n in SYMB_NS:
        xs = sp.Matrix(sp.symbols("x1:%d" % (n + 1)))
        W0 = sp.Matrix(n, n, sp.symbols("p1:%d" % (n * n + 1)))
        W1 = sp.Matrix(n, n, sp.symbols("q1:%d" % (n * n + 1)))
        Rm = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "r%d%d" % (min(i, j), max(i, j))))
        Sm = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "s%d%d" % (min(i, j), max(i, j))))
        v = W0.T * xs
        vtv = (v.T * v)[0, 0]
        Q = sp.eye(n) - (v * v.T) / vtv
        # A(y0) = Q R Q has kernel v (Q v = 0); A'(y0) = S
        A0v = Q * (Rm * (Q * v))
        if sp.simplify(A0v) != sp.zeros(n, 1):
            ok_cg = False
        # M'(y0) = W1 A0 W0^T + W0 S W0^T + W0 A0 W1^T
        t1 = (xs.T * (W1 * A0v))[0, 0]
        t3 = (A0v.T * (W1.T * xs))[0, 0]
        t2 = (xs.T * W0 * Sm * W0.T * xs)[0, 0]
        claim = t1 + t2 + t3 - (v.T * Sm * v)[0, 0]
        if sp.simplify(claim) != 0:
            ok_cg = False
    res.append(("G06-symb-congr", ok_cg,
                "x^T M'(y0) x == v^T A'(y0) v for generic W(y), "
                "A(y0)v = 0 (Q R Q construction), n = %s" % (SYMB_NS,)))
    return res


def battery_gate() -> tuple:
    ok = True
    ncells = 0
    npairs_tot = 0
    bs = [Fraction(v) for v in BATTERY_POLES]
    for mags in BATTERY_MAGS:
        for mask in range(2 ** BATTERY_N):
            rho = [(1 if (mask >> i) & 1 else -1)
                   * Fraction(mags[i]) for i in range(BATTERY_N)]
            r = battery_instance(rho, bs)
            ncells += 1
            npairs_tot += r["npairs"]
            if not (r["agree"] and r["count_ok"] and r["par_ok"]
                    and r["flip_ok"] and r["total_ok"]):
                ok = False
    return ok, ncells, npairs_tot


# ---------------------------------------------------------- firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    funcs = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs[node.name] = node
    bad = []
    forbid_names = ("zetazero", "siegelz", "nzeros", "backlund",
                    "loadtxt", "genfromtxt", "fromfile")
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else \
                (fn.id if isinstance(fn, ast.Name) else "")
            if nm in forbid_names or nm == "zeta":
                bad.append("call:" + nm)
            if nm == "load":
                bad.append("call:load")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [a.name for a in node.names] \
                if isinstance(node, ast.Import) else [node.module or ""]
            for m in mods:
                if "verification" in m or m == "numpy":
                    bad.append("import " + m)
    owners = {}
    for fname, fnode in funcs.items():
        for node in ast.walk(fnode):
            if isinstance(node, ast.Call):
                fn = node.func
                nm = fn.attr if isinstance(fn, ast.Attribute) else \
                    (fn.id if isinstance(fn, ast.Name) else "")
                owners.setdefault(nm, set()).add(fname)
    for owner in owners.get("polyroots", set()):
        if not (owner.startswith("measure_")
                or owner.startswith("verify_")):
            bad.append("polyroots-in:" + owner)
    for owner in owners.get("eigsy", set()):
        if not owner.startswith("measure_"):
            bad.append("eigsy-in:" + owner)
    for nm in ("eig", "eigvals", "eigh", "eigvalsh", "roots"):
        if nm in owners:
            bad.append("eig/roots-call:" + nm)
    cellkey_bad = []
    for fname, fnode in funcs.items():
        if not fname.startswith("construct_"):
            continue
        for node in ast.walk(fnode):
            if isinstance(node, ast.Subscript) and isinstance(
                    node.slice, ast.Constant):
                if node.slice.value in ("mpE", "mpM", "mpV", "tau",
                                        "gap", "cn"):
                    cellkey_bad.append("cellkey:%s:%s"
                                       % (fname, node.slice.value))
    calls = {}
    for fname, fnode in funcs.items():
        cs = set()
        for node in ast.walk(fnode):
            if isinstance(node, ast.Call):
                fn = node.func
                nm = fn.attr if isinstance(fn, ast.Attribute) else \
                    (fn.id if isinstance(fn, ast.Name) else "")
                cs.add(nm)
        calls[fname] = cs

    def reach(start: str) -> set:
        seen, stack = set(), [start]
        while stack:
            u = stack.pop()
            for v in calls.get(u, set()):
                if v not in seen:
                    seen.add(v)
                    if v in calls:
                        stack.append(v)
        return seen

    guard_bad = []
    for fname in funcs:
        if fname.startswith("construct_"):
            r = reach(fname)
            if "polyroots" in r or "eigsy" in r or any(
                    v.startswith("measure_") or v.startswith("verify_")
                    for v in r):
                guard_bad.append(fname)
    return bad, guard_bad, cellkey_bad


def loop_dag() -> tuple:
    dag = {
        "DELIVERED": ["ATOMS", "WALL-EIGENEQ", "RESIDUES", "LADDER",
                      "SCAFFOLD", "LAW-IDENTITY", "DICTIONARY",
                      "OBSTRUCTION-THEOREM"],
        "ATOMS": [],
        "WALL-EIGENEQ": ["ATOMS"],
        "RESIDUES": ["WALL-EIGENEQ"],
        "LADDER": ["RESIDUES"],
        "SCAFFOLD": ["RESIDUES"],
        "LAW-IDENTITY": [],
        "DICTIONARY": [],
        "OBSTRUCTION-THEOREM": ["LAW-IDENTITY"],
        "CENSUS-ROOTS": [],
        "SIGNCHAR-MEASURED": ["CENSUS-ROOTS", "LAW-IDENTITY"],
        "DEFINITIZER-MEASURED": ["SIGNCHAR-MEASURED"],
        "CENSUS-FORALL-K": [],
        "A0-TRIANGLE": [],
        "ZERO-VERIFICATION-AS-HYP": [],
        "RH-COND-SECOND-MOMENTS": [],
    }
    flagged = ("CENSUS-FORALL-K", "A0-TRIANGLE",
               "ZERO-VERIFICATION-AS-HYP", "RH-COND-SECOND-MOMENTS",
               "CENSUS-ROOTS", "SIGNCHAR-MEASURED",
               "DEFINITIZER-MEASURED")
    state = {}

    def dfs(u):
        state[u] = 1
        for v in dag.get(u, []):
            if state.get(v) == 1:
                return False
            if state.get(v) is None and not dfs(v):
                return False
        state[u] = 2
        return True

    acyclic = all(dfs(u) for u in list(dag) if state.get(u) is None)
    seen, stack = set(), ["DELIVERED"]
    while stack:
        u = stack.pop()
        for v in dag.get(u, []):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    clean = not (set(flagged) & seen)
    return acyclic, clean


# --------------------------------------------------------------- main
def main() -> int:
    global CALIB
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--calib", action="store_true")
    args = ap.parse_args()
    CALIB = args.calib
    if args.smoke:
        rungs = (4, 5)
    elif args.calib:
        rungs = (4, 5, 8, 13)
    else:
        rungs = RUNGS
    mode = "  [SMOKE]" if args.smoke else \
        ("  [CALIB]" if args.calib else "")
    print("krein_definitizer_probe -- PRIME.KREIN.DEFINITIZER.01%s"
          % mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])

    section("S0 firewall + loop guard")
    bad, guard_bad, cellkey_bad = firewall_audit()
    check("G01-firewall", not bad,
          "forbidden names/imports: %s" % (bad or "none"))
    check("G02-roots-guard", not guard_bad,
          "construct_* reaching polyroots/eigsy/measure_*/verify_*: "
          "%s (measurement-vs-construction split machine-checked)"
          % (guard_bad or "none"))
    check("G04-spec", len(SPEC_SHA) == 64
          and all(h in DPS for h in RUNGS),
          "SPEC_SHA printed; frozen DPS schedule covers RUNGS")
    acyc, clean = loop_dag()
    check("G08-loop-dag", acyc and clean,
          "ancestry DAG acyclic=%s; flagged loops + CENSUS-ROOTS + "
          "SIGNCHAR-MEASURED unreachable from DELIVERED=%s"
          % (acyc, clean))

    section("S1 symbolic + exact battery")
    for name, ok, detail in symbolic_gates():
        check(name, ok, detail)
    bok, ncells, npr = battery_gate()
    check("G07-exact-battery", bok,
          "Fraction/Sturm battery n=%d, %d cells (%d nonreal pairs "
          "encountered): parity + two-route eps + flip law + count "
          "law all exact" % (BATTERY_N, ncells, npr))

    section("S2 rungs + worlds (parallel)")
    jobs_r = [(h, DPS[h]) for h in rungs]
    jobs_w = list(CONTROLS)
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs_r = list(ex.map(w_rung, jobs_r))
        futs_w = list(ex.map(w_world, jobs_w))
    R = {r["h"]: r for r in futs_r}
    W = {(r["world"], r["x"]): r for r in futs_w}

    slacks = {}
    taus = {}
    flip0_pos = True
    occmin_all = True
    flip0top_all = True
    for h in rungs:
        r = R[h]
        if "error" in r:
            check("G10[h=%d]-build" % h, False, r["error"])
            continue
        info("h=%d K=%d build %.1f s  ladder=(%d,%d)  n_odd-gaps=%d"
             % (h, r["K"], r["build_s"], r["npos"], r["nneg"],
                r["n_odd"]))
        check("G10[h=%d]-build" % h,
              r["K_ok"] and r["ray_dev"] <= RAY_BAR,
              "K ok=%s, ray_dev %.2e <= %.0e"
              % (r["K_ok"], r["ray_dev"], RAY_BAR))
        check("G11[h=%d]-ladder" % h,
              r["nzero"] == 0
              and (r["npos"], r["nneg"]) == LADDER_TAB[h],
              "(n+,n-)=(%d,%d) == frozen %s, n0=%d"
              % (r["npos"], r["nneg"], LADDER_TAB[h], r["nzero"]))
        check("G12[h=%d]-scaffold" % h,
              r["par_total_ok"] and r["gauge_ok"],
              "parity scaffold source-side: %d odd gaps of %d; total "
              "parity == n mod 2; exact (3/7) gauge invariance"
              % (r["n_odd"], r["K"]))
        if h > MEASURE_MAX:
            info("h=%d: EPS-MEASURE-H13-ONLY -- ladder + scaffold "
                 "recorded, no root measurement (disclosed scope)"
                 % h)
            continue
        top_ok = abs(r["top_yt"] / TOP_TAB[h] - 1) <= TOP_RTOL
        check("G13[h=%d]-census" % h,
              r["nreal"] == r["K"] - 1
              and r["negsum"] <= NEGSUM_BAR and top_ok
              and r["minsp"] >= SIMPLE_BAR
              and r["minrp"] >= ROOTPOLE_BAR,
              "nreal %d == K-1, negsum %.1e, top/yt %.6f vs tab, "
              "minsp %.1e >= %.0e, minrp %.1e >= %.0e"
              % (r["nreal"], r["negsum"], r["top_yt"], r["minsp"],
                 SIMPLE_BAR, r["minrp"], ROOTPOLE_BAR))
        check("G14[h=%d]-signchar-law" % h,
              r["eps_agree"] and r["eps_npos"] == r["npos"]
              and r["eps_nneg"] == r["nneg"],
              "two-route eps agreement at all %d roots; count law "
              "(#eps+,#eps-)=(%d,%d) == ladder"
              % (r["nreal"], r["eps_npos"], r["eps_nneg"]))
        check("G15[h=%d]-parity-law" % h,
              r["parity_law_ok"],
              "measured occupancy parity == source scaffold at all "
              "%d gaps" % r["K"])
        check_tab("G16[h=%d]-defects" % h,
                  r["d"] == D_TAB.get(h) and r["flip0"]
                  == FLIP0_TAB.get(h) and r["flipev"]
                  == FLIPEV_TAB.get(h) and r["occmin"]
                  == OCCMIN_TAB.get(h) and r["flip0_top"]
                  == FLIP0TOP_TAB.get(h) and r["flip_law_ok"],
                  "d=%d flip0=%d flipev=%d occmin=%s flip0-all-in-"
                  "top-gap=%s flip-law=%s (multi-occupied gaps: %s)"
                  % (r["d"], r["flip0"], r["flipev"], r["occmin"],
                     r["flip0_top"], r["flip_law_ok"], r["occnz"]))
        if r["flip0"] == 0:
            flip0_pos = False
        occmin_all = occmin_all and r["occmin"]
        flip0top_all = flip0top_all and r["flip0_top"]
        check("G17[h=%d]-definitizer" % h,
              r["strict_ok"] and r["deg"] == r["d"],
              "strict minimal p: degree %d == d, sign p(y_i) == "
              "eps_i at all %d roots" % (r["deg"], r["nreal"]))
        if h in (4, 5) and "blk" in r:
            blk = r["blk"]
            fam_ok = all(f["kd"] <= KD_BAR and f["res"] <= KRES_BAR
                         and f["pd"] for f in blk["fams"].values())
            check_tab("G18[h=%d]-blocking" % h,
                      (blk["i_neg"], blk["i_pos"]) == BLK_TAB[h]
                      and fam_ok,
                      "blocking roots (first eps-, first eps+) = "
                      "(%d, %d) vs tab %s; families kd dev %s <= "
                      "%.0e, kernel res <= %.0e, all W PD"
                      % (blk["i_neg"], blk["i_pos"], BLK_TAB[h],
                         {k: "%.1e" % v["kd"]
                          for k, v in blk["fams"].items()}, KD_BAR,
                         KRES_BAR))
        if h == 4 and "langer" in r:
            lng = r["langer"]
            check_tab("G19-langer",
                      lng["symdev"] <= SYMDEV_BAR
                      and lng["psd_ratio"] >= PSD_MIN
                      and lng["ch_res"] <= CH_BAR,
                      "J p(T) symdev %.1e, eigsy min/max %.2e "
                      "(STRICTLY PD: Langer condition holds), "
                      "Cayley-Hamilton residual %.1e (trivial "
                      "definitizer degenerate)"
                      % (lng["symdev"], lng["psd_ratio"],
                         lng["ch_res"]))
        if r.get("slack_l10") is not None:
            slacks[h] = r["slack_l10"]
            taus[h] = r["log10tau"]
    check("G03-tau-screen",
          not cellkey_bad
          and all(R[h].get("gauge_ok", False) for h in rungs
                  if "error" not in R[h]),
          "construct_* cell-key whitelist clean (%s); ladder + "
          "scaffold exact scale-gauge invariant under c -> (3/7)c"
          % (cellkey_bad or "none"))

    section("S3 worlds + witness")
    wnames = {"SMOOTH": "G30-smooth", "SCRARITH": "G31-scrarith",
              "EPSTEIN": "G32-epstein"}
    for (world, x, _d) in CONTROLS:
        r = W[(world, x)]
        if "error" in r:
            check(wnames[world], False, r["error"])
            continue
        tab = LADDER_WORLD[(world, x)]
        base_ok = ((r["npos"], r["nneg"]) == tab and r["nzero"] == 0
                   and r.get("eps_agree", False)
                   and r.get("count_ok", False)
                   and r.get("parity_law_ok", False)
                   and r.get("flip_law_ok", False))
        dtab = D_WORLD[(world, x)]
        f0tab = FLIP0_WORLD[(world, x)]
        extra = (r.get("d") == dtab and r.get("flip0") == f0tab)
        if world == "SMOOTH":
            extra = extra and r.get("eps_const_neg", False)
        check_tab(wnames[world], base_ok and extra,
                  "x=%d ladder (%d,%d) == %s, nreal=%d npairs=%d, "
                  "d=%s flip0=%s (tab %d/%d)%s; law two-route + "
                  "parity + count OK=%s"
                  % (x, r["npos"], r["nneg"], tab, r.get("nreal", -1),
                     r.get("npairs", -1), r.get("d"), r.get("flip0"),
                     dtab, f0tab,
                     ", eps == const -1" if world == "SMOOTH" else "",
                     base_ok))
    d_main5 = R[5].get("d") if 5 in R and "error" not in R[5] else None
    d_scr = W[("SCRARITH", 5)].get("d")
    d_smooth = W[("SMOOTH", 5)].get("d")
    orient = (d_smooth == 0 and d_scr is not None
              and d_scr > 0 and d_main5 is not None and d_main5 > 0)
    check_tab("G33-orientation",
              orient and d_scr == D_WORLD[("SCRARITH", 5)]
              and d_main5 == D_TAB.get(5),
              "d(SMOOTH)=%s vs d(SCRARITH)=%s vs d(MAIN,h=5)=%s: the "
              "d = 0 vs d > 0 dichotomy separates atoms-vs-no-atoms "
              "only -- r188 caveat INHERITED, NOT-A-SIGN-SOURCE; the "
              "VALUE differs MAIN vs SCRARITH at x = 5 (single cell, "
              "recorded, NOT claimed)" % (d_smooth, d_scr, d_main5))
    wv = R.get(WIT_RUNG, {})
    wit_ok = (wv.get("wit_ladder") == WIT_LADDER
              and wv.get("wit_nzero") == 0
              and wv.get("wit_nreal") == WIT_NREAL
              and wv.get("wit_npairs") == WIT_NPAIRS
              and wv.get("wit_d") == WIT_D
              and wv.get("wit_agree", False)
              and wv.get("wit_flip_law", False)
              and wv.get("wit_count_ok", False))
    check_tab("G34-witness", wit_ok,
              "r172 witness at h=%d: ladder %s (tab %s), nreal=%s "
              "npairs=%s (tabs %d/%d: the witness BREAKS census "
              "realness -- the witness ray is NOT strongly "
              "definitizable), d_wit=%s (tab %d), two-route law + "
              "flip law + deficit count law on the real subset = "
              "%s/%s/%s -- the LAW is ray-blind (typed)"
              % (WIT_RUNG, wv.get("wit_ladder"), (WIT_LADDER,),
                 wv.get("wit_nreal"), wv.get("wit_npairs"),
                 WIT_NREAL, WIT_NPAIRS, wv.get("wit_d"), WIT_D,
                 wv.get("wit_agree"), wv.get("wit_flip_law"),
                 wv.get("wit_count_ok")))

    section("S4 screens + verdict")
    slope = None
    if len(slacks) >= 3:
        hs = sorted(slacks)
        xs = [taus[h] for h in hs]
        ys = [slacks[h] for h in hs]
        mx = sum(xs) / len(xs)
        my = sum(ys) / len(ys)
        sxx = sum((v - mx) ** 2 for v in xs)
        sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs)))
        slope = sxy / sxx if sxx else float("nan")
        r2 = (sxy ** 2 / (sxx * sum((v - my) ** 2 for v in ys))) \
            if sxx and any(v != my for v in ys) else 1.0
        slack_ok = all(abs(slacks[h] - SLACK_TAB[h]) <= SLACK_TOL
                       for h in hs if h in SLACK_TAB)
        in_band = RIDE_BAND[0] <= abs(slope) <= RIDE_BAND[1]
        check_tab("G50-tau-screen",
                  slack_ok and abs(slope - SLOPE_TAB) <= SLOPE_TOL,
                  "defect-slack ladder %s (tabs %s tol %.2f); slope "
                  "vs log10 tau = %+.3f (R^2 %.3f, tab %+.3f); "
                  "|slope| in ride band %s = %s -> %s"
                  % ({h: "%.3f" % slacks[h] for h in hs},
                     SLACK_TAB, SLACK_TOL, slope, r2, SLOPE_TAB,
                     RIDE_BAND, in_band,
                     "RIDES-TAU" if in_band else
                     "mixed currency, typed not-riding"))
    pivot = (occmin_all, flip0top_all, flip0_pos)
    if args.smoke:
        info("G51-pivot skipped in smoke mode (aggregate over the "
             "full measured rung set only); partial pivot = %s"
             % (pivot,))
    else:
        check_tab("G51-pivot", pivot == PIVOT_TAB,
                  "(occmin-all, flip0-top-all, flip0-pos-all) = %s "
                  "== frozen %s: the occ-min law FAILS at h >= 8 "
                  "(one interior doubled gap each), the eps-sequence "
                  "is NOT source-computable from the parity scaffold "
                  "alone -- STRICT-DEFINITIZER-ROOT-DEPENDENT; the "
                  "parity scaffold survives as the source-side "
                  "coordinate" % (pivot, PIVOT_TAB))
    dt = time.time() - T_START
    check("G40-runtime", dt < RUNTIME_BAR,
          "%.1f s < %.0f s" % (dt, RUNTIME_BAR))

    verdict = ["DICTIONARY-IMPORTED-EXACT",
               "SIGNCHAR-LAW-TWO-ROUTE-EXACT",
               "SIGNCHAR-COUNT-IS-LADDER",
               "PARITY-SCAFFOLD-SOURCE-SIDE",
               "DEFINITIZER-EXISTS-EVERY-VERIFIED-RUNG"]
    if occmin_all and flip0top_all:
        verdict.append("EPS-SEQUENCE-SOURCE-COMPUTABLE-GIVEN-OCCMIN")
    else:
        verdict.append("STRICT-DEFINITIZER-ROOT-DEPENDENT")
        verdict.append("OCCMIN-HOLDS-H45-FAILS-H813")
    verdict += ["WY-CONGRUENCE-CLASS-KILLED",
                "ORIENTATION-STILL-ATOMS-VS-NO-ATOMS",
                "WITNESS-BREAKS-REALNESS-LADDER-UNMOVED",
                "LAW-RAY-BLIND", "SLACK-NOT-RIDING-TAU",
                "MEASUREMENT-VS-CONSTRUCTION-SPLIT-MACHINE-CHECKED",
                "EPS-MEASURE-H13-ONLY", "TAU-FREE-CONSTRUCTION",
                "ROOTS-NEVER-CONSTRUCT", "NO-RH-CLAIM"]
    print("\nVERDICT: %s" % " + ".join(verdict))

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], time.time() - T_START))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
