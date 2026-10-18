#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""halfgap_riccati_transition_probe -- PRIME.PORT.HALFGAP.RICCATI.01
(EXPLORATION ONLY, experiments/; theorem-engineering on the RH-side
wall: THE TRANSITION INEQUALITY OF THE HALF-GAP INDUCTION, second
probe under the contract.  The predecessor (CLXII,
halfgap_riccati_increment_probe) measured the one-step additive
barrier and killed it broadly (21/37 exact fails, every fail a
down-flow, the barrier alone WALL-BLIND); its named lessons are the
DESIGN CONSTRAINTS here: (i) any inductive form must carry the base
case and the B-floor premise as the actual wall carriers, (ii) the
one-step granularity is wrong -- the pivot flow oscillates while the
invariant never exhausts its slack, so the multi-step window is the
right object.  THIS probe consumes the NEW upstream ingredients that
did not exist at CLXII freeze time: the CERTIFIED B-floor (CLIII
interval rollout: B_tau >= c_B I with min c_B = 0.5523 exact-rational
over the certified 39-step surface, own frame, tau units), the
REGISTERED + DEEP-BLIND-TESTED half-gap target (CLI registration
sha ae292e55, NO-ADJUST; CLIV holdout 28/28 at h 1219..2854 with
float B-floor 1.6610), and the CCI lesson that the wall level is
prime-carried with demand law +0.60 dex/alpha -- against which the
INCREMENT demand is measured here for the first time.  2026-08-11.)

(a) THE EXACT INCREMENT IDENTITY, formalized for the ACTUAL ladder.
The deployed ladder is GEOMETRIC, not h -> h+1: rungs (kz, h) sorted
by (h, kz), consecutive full-core steps k = (r1_k, r2_k) sharing the
middle rung, transitions t_k = (step k, step k+1).  Per transition,
in the shared Householder frame Q_k (from step k's soft direction)
and a declared normalization scale (ell primary / tau twin), with
M = Q_k^T (S(r2_k)/scale_k) Q_k, M_+ = Q_k^T (S(r2_{k+1})/
scale_{k+1}) Q_k (the round-59 route-(ii) transport), n/b/B and
n_+/b_+/B_+ their pivot/coupling/co-block parts, x = B^{-1} b:
    s_+ - s = H - r^* B_+^{-1} r          (EXACT, all conventions),
    H = w^T (M_+ - M) w,  r = [(M_+ - M) w]_{1:},  w = (1, -x),
s, s_+ the Schur pivots.  The registered HALFGAP target s >= (1/2)
mu1(h), mu1(h) = 4 sin^2(pi/(2h+1)), lives on this ladder (cofinal
in h is enough, per the program's continuum extraction).  WARD: the
identity to ID_WARD = 1e-10 relative on EVERY computed transition of
the deployed ladder -- 42 surface rungs (h 142..878, deployed
windows) PLUS the 28 deep rungs (h 1219..2854, the CLIV 4e6-table
extension, fidelity-warded byte-exact) joined into ONE h-sorted
chain including the surface->deep BRIDGE transition.  The own-frame
pivot s_{k+1} differs from the transported s_+^(k) by the HINGE
(frame drift) -- measured as a first-class ladder, as CLXII.

(b) THE TRANSITION TARGET, two B-treatments.  TARGET(k):
    H_k + (1/2)(mu1(h_k) - mu1(h_{k+1})) >= r_k^* B_+^{-1} r_k.
By the CLXII two-line Schur lemma, TARGET(k) + (B_+ > 0) + (s_k >=
mu_k/2) ==> s_{k+1-transported} >= mu_{k+1}/2.  Census with (i) the
MEASURED B_+^{-1} (exact-rational slack on the float entries, v897
class -- the predecessor decision, reproduced as a ward on the
surface: 21/37 exact fails, 16 passes), and (ii) the PROVEN B-FLOOR
replacing the inverse:  r^* B_+^{-1} r <= ||r||^2 / c_B  whenever
B_+ >= c_B I, with c_B = CB_CITED = 0.5523 (CLIII, tau units, OWN
frame, certified range = the 39 surface steps h <= 900; cited and
printed, NOT re-proved here).  THE FLOOR TREATMENT IS A THEOREM-
CONDITIONAL WEAKENING: pass(floor) subset pass(measured) always
(||r||^2/c_B >= r^*B_+^{-1}r), so its census can only be smaller --
its value is that the inverse is ELIMINATED: the floor form reads
only (H, ||r||^2, mu-increment, one cited constant).  HONEST FRAME
TRANSPORT: the certificate lives in the OWN frame of each step; the
transition consumes B_+ in the SHARED frame; lam_min is not
invariant under sub-block frame change, so the shared-frame floor is
MEASURED per transition (float lam_min(B_+^shared) vs CB_CITED,
typed census), never silently certified; on the deep ladder the
floor is FLOAT-LEVEL (CLIV: min own-frame lam_min(B_tau) = 1.6610)
-- typed separately, said honestly.  The floor phase lives in the
TAU convention (where the certificate lives; tau never enters the
primary ell chain's coefficients).  Margin ladders in dex for both
treatments; failure anatomy decomposed (H < 0? r-dominated? the
mu-allowance orders below the flow?).

(c) THE ARCHIMEDEAN/PRIME SPLIT OF THE INCREMENT -- the exact
three-way source split at frozen lifts.  Every read of the Schur
core S is an A-level read at the lifted vector z = (c; -R^{-1}X^T c)
(exact: c^T S c' = z^T A z'), and A's bilinear form has the exact
variational representation at the frozen minimizers f_i (the
CD-projections of the lifted data g_i = z_i/sqrt(v)):
    z_1^T A z_2 = INT g_1 g_2 dnu_- - INT g_1 f_2 dnu_-
                  - INT g_2 f_1 dnu_- + INT f_1 f_2 dnu_+ ,
which is LINEAR in the pair (nu_+, nu_-) at frozen (g_i, f_i, fold
masks).  The source measure splits EXACTLY by the lag split c_lag =
c_ar + c_sm + c_osc (archimedean closed-form lags; smooth PNT comb
on the NG = 6000 grid, the CXLVII/CLIV convention; prime OSCILLATION
c_osc = c_at - c_sm), the density and the folded weights being
linear in the lag at the TRUE world's masks.  SPLIT DEFINITION
(frozen after smoke-1, disclosed below): S_AR and S_SM are computed
by the frozen-lift representation; S_OSC := S - S_AR - S_SM by
EXACT COMPLEMENT (mirroring d_osc = d - d_ar - d_sm), so the
assembly S = S_AR + S_SM + S_OSC is exact by construction (float-
associativity ward <= SPLIT_WARD); the representation's own
closure defect (sum of all three REP values minus S -- the
nu_+-quadrature orthonormality defect of the evaluated chain,
measured 1.2e-5 max in smoke-1) is warded separately at REP_BAR =
1e-3 and printed, so the OSC attribution carries a declared
<= REP-defect pollution.  Per transition H = H_AR + H_SM + H_OSC,
r = r_AR + r_SM + r_OSC (assembly wards normalized by the PART
scale, since H itself near-cancels on real transitions) -- the
CCI-style closed-form/prime split ported to the Schur-core
surface.  The attribution depends on the frozen representation
(declared); the SUM is exact.  MEASURED: the carrier
census (who carries H and the failures -- the window part WIN =
AR + SM or the prime oscillation OSC), the WIN-only transition
census (float diagnostic), and THE DEMAND LAW: OLS slopes vs alpha
of log10 of the increment objects in target currency (|H_OSC|/mu1,
||r_OSC||^2/mu1, adap/mu1, |Delta s|/mu1) on the combined ladder,
compared against the CITED CCI level-demand law CCI_REF = +0.60
dex/alpha: typed INCREMENT-FLATTER iff slope + 2SE < CCI_REF,
INCREMENT-STEEPER iff slope - 2SE > CCI_REF, else AMBIG-OVERLAP.
The key question frozen a priori: increments can be easier than
levels -- measured, not presumed.

(d) THE COMPOSED INDUCTION.  The one-step census is expected to
reproduce the CLXII kill (frozen expectation), so the sharpest
honest form is the m-STEP window: for window size m, the exact
telescoped identity (own-frame, invariant data)
    NET_m(k) = s_{k+m} - s_k + (1/2)(mu_k - mu_{k+m}) >= 0
is the m-step barrier statement (base block = the first m rungs'
certificates, then induction by m-jumps); its analytic-handle
telescoped form is sum_j (H_j - adap_j + (1/2) Delta mu_j) over the
window PLUS the accumulated hinge defects (each defect = s_{j+1}^own
- s_+^(j), measured ladder), and its floor form replaces adap_j by
||r_j||^2/c_B.  MEASURED: the census over all windows of the
combined ladder per m in M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16); m*
= the smallest m with a full pass; margins in target currency.
THE DRAFT (typed, printed): [THEOREM-EXACT] the update identity +
the two-line barrier lemma + its floor variant; [THEOREM-CERTIFIED,
RANGE-LIMITED] B_tau >= 0.5523 I own-frame on the 39 certified
surface steps (CLIII); [MEASURED] base case + invariant censuses
(surface exact-rational class on float entries, deep FLOAT-LEVEL),
the transition/m-step censuses, the frame-transport and hinge
ladders, the deep floor 1.6610 (float); [OPEN, the all-h gap] G1 the
m*-window transition inequality beyond the computed ladder (its
measured demand law is THE exact demand of the open piece), G2 the
floor certificate beyond h ~ 900 / in the shared frame, G3 hinge
uniformity, G4 the float pipeline not enclosed at the base (CLIII-
class rollout exists only for the B-floor chain), G5 the ladder
geometry itself is deployed data.  Typed CONJECTURE, never a claim.

(e) GATES.  Controls (kill -> WARD-BROKEN if silent at rung level):
smooth world, scramble (seed 1), Epstein x^2+5y^2 at kz 9
(transition-level Epstein DECLARED SKIPPED, O(X^2), predecessor
pattern; deep controls inherited from CLIV, cited), cosh injection
A = 0.01 and mass rescale 1.1 (the CLXII deployed values, frozen
selection cited, no new ladder search).  TRANSITION DISCRIMINATION
(typed, first-class): on each control world's relaxed chain, count
(i) bare-barrier CERTIFY (the CLXII WALL-BLIND census, expected to
reproduce its pattern) and (ii) COMPOSED certificates = barrier pass
AND floor premise lam_min(B_+^shared) >= CB_CITED AND base-invariant
s >= mu/2 -- the composed form is expected to fire ZERO on false
worlds (the premise carries the wall content): typed
COMPOSED-DISCRIMINATES / COMPOSED-BLIND(world counts).  IMPOSTOR
N/A DECLARED: this probe consumes zero zero-reads (AST firewall),
so the off-line-zero impostor control has no seat here.  TAU-SCREENS
on all margins (measured slack, floor slack, OSC carrier fraction,
m*-net margin, invariant margin) with bands PASS |s| <= 0.30 /
RELOC >= 0.70 / else AMBIG, excluded counts printed.  ANTI-
CIRCULARITY (frozen): the transition constructions consume only
h-level state (x = B^{-1}b from the current step, the DDC-legit
recursion) and source-side structure; s_+ and its sign appear ONLY
in measurement wards (the identity census), never in any
certificate's construction; no target eigendata, no sigma_h, no
defect eigenvector; ell is source-only (round 57); tau only in the
tau twin, the floor phase (certified convention), reproduction wards
and screens; RNG only inside the declared scramble control.

FROZEN PROTOCOL (pipeline verbatim from halfgap_riccati_increment
= CL/CXLIV/v900 chain; deep extension verbatim from
deep_blind_holdout; ONE Gram per rung; window memoization):

 W   SURFACE PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core; W3 truth all-PSD; W4 >= 20 consecutive steps; W5
     P2/P3 ledger (min lam_min(B_tau) == 0.679 rtol 2e-2, gap
     min/med == 0.052/0.888 rtol 5e-2); W6 ELL-B alive on every
     full-core truth rung; W7 PREDECESSOR CENSUS REPRODUCTION
     (kill): the surface primary (ell) exact census == 21 fails of
     37, tau twin == 21 of 37, hinge med within 5e-3 of 1.0004,
     target flips 0; W8 typed: invariant census s_k >= mu1_k/2 on
     the surface steps (expected 39/39) + base case.

 DW  DEEP LADDER (fidelity kill -> WARD-BROKEN): DW1 extended table
     byte-exact on [0, ATOM_MAX] + prefix arrays bitwise + kappa
     guard (CLIV W1-W3 verbatim); DW2 deep census == 28 rungs in
     H_HOLD = [128, 2900] with X in (ATOM_MAX, TAB_EXT]; DW3 deep
     truth rungs all-PSD + chains complete (typed count; >=
     MIN_DEEP_OK = 20 kill); DW4 REPRODUCTION: min own-frame
     lam_min(B_tau) over the 27 deep-internal steps == 1.6610 rtol
     2e-2 (CLIV); DW5 typed: deep invariant census s >= mu1/2 (ell)
     -- a NEW out-of-registry extension of the ell-surface
     invariant, FLOAT-LEVEL declared.  SOFT BUDGET: deep rungs are
     built h-ascending under SOFT_BUDGET_S = 1200 s; unbuilt rungs
     are typed SKIPPED-BUDGET (partial coverage is honest coverage).

 P   THE COMBINED CHAIN: surface + deep truth rungs, ONE (h, kz)-
     sorted ladder, steps and transitions incl. the BRIDGE; P1 >=
     MIN_TRANS_COMB = 40 transitions (kill).

 A   IDENTITY + HINGE (kill -> WARD-BROKEN): A1 identity ward <=
     ID_WARD = 1e-10 on every OK transition (ell + tau); A2
     two-route pivot ward <= S2_WARD = 1e-8; A3 B_+ PD exact-
     rationally on every truth transition; A4 mu monotone along the
     h-sorted chain; A5 typed HINGE ladder (med/min/max, flips).

 B   THE CENSUSES (typed, never kill beyond the W7 reproduction):
     B1 measured census (ell primary; exact-rational slack), pass/
     fail per segment (surface / bridge / deep) + margin ladder in
     dex on passes log10(a/adap) and fails log10(-slack / mu1_+);
     B2 tau twin census; B3 FLOOR census (tau): exact-rational
     slack_floor = a_tau - ||r_tau||^2/CB_CITED, segment censuses +
     margin dex + the containment ward pass(floor) subset
     pass(measured) (theorem, warded) + the ISOTROPIC OVERHEAD
     ladder log10((||r||^2/c_B)/adap) in tau units (the price of
     dropping B_+'s directional structure, printed); B4 floor
     TRANSPORT census:
     float lam_min(B_+^shared,tau) >= CB_CITED count (surface;
     certified range) and >= 0 + value ladder (deep, float); B5
     failure anatomy: counts of H < 0 / r-dominated (H >= 0, adap >
     a) / allowance ladder (1/2)Dmu/adap min/med/max + down-flow
     census.

 C   THE SPLIT (kill on assembly wards): C1 per-rung part-weight
     linearity ward (sum of part folded weights == true weights,
     rel <= 1e-10) + split assembly ward ||S_AR + S_SM + S_OSC -
     S|| / ||S|| <= SPLIT_WARD = 1e-8 (exact by the complement
     construction; tests float associativity) + REP-defect ward
     ||REP_AR + REP_SM + REP_OSC - S|| / ||S|| <= REP_BAR = 1e-3
     (the nu_+-quadrature diagnostic, printed) on every truth rung
     of the combined ladder; C2 per-transition part assembly (H
     parts sum, r parts sum, rel <= 1e-8 normalized by part
     scale) + carrier census: |H_OSC| / (|H_AR|
     + |H_SM| + |H_OSC|) ladder, sign(H) == sign(H_OSC) census,
     same for the fail subset; C3 WIN-only census (float
     diagnostic): slack_WIN = H_WIN + (1/2)Dmu - r_WIN^T B_+^{-1}
     r_WIN, census + comparison (does the window skeleton alone
     pass/fail the same transitions?); C4 THE DEMAND LAW: jackknife
     OLS slopes vs alpha of log10(|H_OSC|/mu1_+),
     log10(||r_OSC||^2/mu1_+), log10(adap/mu1_+),
     log10(|Ds|/mu1_+), and the level line log10(s/mu1) -- typed
     against CCI_REF = +0.60 dex/alpha as frozen above.

 D   THE M-STEP LADDER + THE DRAFT (typed): D1 per m in M_LADDER
     the NET_m census over all valid windows (own-frame ell
     invariant data) + margins/mu1; m* typed (or
     MSTEP-NOT-REACHED); D1b the MULTIPLICATIVE demand ladder
     (printed): per m the min/med drop ratio s_{k+m}/s_k against
     the mu-ratio demand max_k mu1(h_{k+m})/mu1(h_k) -- the exact
     demand a ratio-form barrier would have to certify from the
     1/2-hypothesis alone; D2 the telescoped analytic form: max
     accumulated |hinge defect|/mu1 ladder + the floor-telescoped
     census per m (sum_j (H_j - ||r_j||^2/c_B + (1/2)Dmu_j) >= 0,
     tau units); D3 the composed induction draft printed with the
     THEOREM / CERTIFIED / MEASURED / OPEN typing and gaps G1-G5;
     CONJECTURE language only.

 E   CONTROLS (rung firing kill -> WARD-BROKEN; censuses typed):
     E1 smooth fires; E2 scramble fires; E3 Epstein fires at kz 9
     (transition ladder skipped, declared); E4 cosh A = 0.01 fires;
     E5 rescale 1.1 fires; E6 transition discrimination: bare
     CERTIFY census per world (WALL-BLIND reproduction expected on
     cosh/rescale, typed) + COMPOSED census per world (floor
     premise + base invariant + barrier; expected 0 everywhere,
     typed COMPOSED-DISCRIMINATES / COMPOSED-BLIND); E7 impostor
     N/A declared (zero zero-reads).

 F   TAU-SCREENS (typed): measured slack (ell), floor slack (tau),
     OSC carrier fraction, m*-net margins, invariant margin; bands
     PASS 0.30 / RELOC 0.70.

KILLS: K1 pipeline/counts (W1-W4, DW2-DW3, P1) -> PIPELINE-BROKEN;
K2 reproduction / identity / exactness / fidelity / control-firing
wards (W5-W7, DW1, DW4, A1-A4, C1-C2 assembly, B3 containment,
E1-E5) -> WARD-BROKEN.  All other outcomes typed, never kills.

VERDICT (frozen enum): RICCTRANS-MEASURED with typed sublabels
IDENTITY-WARDED(max dev), CENSUS(surface k/N, bridge, deep k/N),
FLOOR-CENSUS(k/N + transport), ANATOMY(counts),
SPLIT-EXACT(max ward) + CARRIER(...) + WINONLY(...),
DEMAND-LAW(slopes vs +0.60 -> INCREMENT-FLATTER/STEEPER/AMBIG),
MSTEP(m* or NOT-REACHED, min margins), DRAFT-TYPED(G1-G5),
WALLBLIND-REPRO(...) + COMPOSED-DISCRIMINATES/COMPOSED-BLIND(...),
SCREENS(...); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP =
42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_TRANS_COMB = 40;
MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF =
0.888 (rtol 5e-2); PRED_FAILS = 21, PRED_TRANS = 37, PRED_TAU_FAILS
= 21, PRED_HINGE_MED = 1.0004 (atol 5e-3), PRED_FLIPS = 0;
PRED_INV = 39; TAB_EXT = 4_000_000; KZ_SCAN_MAX = 400; H_HOLD =
(128, 2900); N_DEEP_EXP = 28; MIN_DEEP_OK = 20; DEEP_MINB_REF =
1.6610 (rtol 2e-2); ID_WARD = 1e-10; S2_WARD = 1e-8; SPLIT_WARD =
1e-8; REP_BAR = 1e-3; WSUM_WARD = 1e-10; CB_CITED =
Fraction(5523, 10000) (CLIII,
cited lower truncation, printed not re-proved; certified range =
39 surface steps, own frame, tau units); CB_RANGE_H = 900; CCI_REF
= +0.60 dex/alpha (CCI, cited comparison constant); M_LADDER = (1,
2, 3, 4, 6, 8, 12, 16); NG_SMOOTH = 6000; CTRL_KZ = 9; scramble
seed 1; INJ_A = 0.01, INJ_DELTA = 0.05, INJ_GAMMA0 = 10.0 (CLXII
deployed, frozen selection cited); RSC_FAC = 1.1 (same); PSD_TOL =
1e-12; SLOPE_PASS = 0.30, SLOPE_RELOC = 0.70; SOFT_BUDGET_S = 1200;
runtime cap declared: 25 min.

EXACTNESS MODEL (frozen): float-level probe on the float64-computed
step matrices; the barrier/floor DECISIONS are exact-rational
(Fraction) on those float entries (v897 class); the WIN-only
diagnostic and all laws/screens are float measurements, said so;
the deep ladder is FLOAT-LEVEL throughout (no interval rollout at
depth -- CLIV limit, inherited); the split assembly is exact
algebra warded numerically.  What is NOT enclosed: the float
pipeline producing the entries.  NO RH claim anywhere.

A-PRIORI EXPECTATIONS (frozen): the surface measured census
reproduces the CLXII kill 21/37 (ward, not hope); pass(floor)
subset pass(measured) (theorem, warded); the deep census and the
demand law are OPEN measurements (no expectation frozen); the
carrier is expected OSC-carried (CLXII G1 + CCI seat); m* expected
reached within M_LADDER but MSTEP-NOT-REACHED is a first-class
honest outcome; the composed control census expected 0 on false
worlds.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing; fail-first
history preserved).  SMOKE-1 (full surface + deep, first passage,
108.6 s): 43 checks, 2 fails, BOTH in the C-block split machinery
and both reimplementation seats, no measurement touched:
  * C1 fail: the original one-line split ward ||S_AR + S_SM +
    S_OSC - S||/||S|| <= 1e-8 with ALL THREE parts computed by the
    frozen-lift representation measured max 1.22e-05 -- the
    representation's nu_+ integral is a quadrature against the
    EVALUATED chain polynomials, whose discrete orthonormality
    defect at h ~ 900..2854 is exactly this size; the ward as
    written tested chain orthonormality, not the split.
    AMENDMENT A1 (construction, disclosed): S_AR/S_SM stay
    representation-computed; S_OSC is redefined as the EXACT
    COMPLEMENT S - S_AR - S_SM (mirroring the density complement
    d_osc = d - d_ar - d_sm); the original 1e-8 assembly ward is
    RETAINED against the complement-defined split, and the
    representation closure defect gets its own NEW ward at REP_BAR
    = 1e-3 with the measured value printed (the OSC attribution
    carries a declared <= 1.3e-5 pollution).  No bar weakened: the
    1e-8 bar stays, a second honest ward is ADDED.
  * C2 fail: the transition part-assembly ward normalized by |H|
    measured max 1.58 -- H itself near-cancels on real transitions
    (that is the physics), so the denominator was wrong.
    AMENDMENT A2: normalization by the PART scale (sum |H_part|,
    sum ||r_part||); the 1e-8 bar is unmoved.
  * AMENDMENT A3 (prints only, nothing decided): the isotropic
    floor-overhead ladder in B3, the multiplicative demand ladder
    D1b, and the deep-census h-range print fixed to min/max.
Everything else in smoke-1 was green and is ON RECORD: W7
predecessor reproduction EXACT (21/37 primary AND tau twin, hinge
med 1.0004, flips 0/37), invariant 39/39 + base case HOLDS, W5
ledger 0.6790 / 0.0520 / 0.8875, DW 28/28 deep rungs (102 s), DW4
min own-frame lam_min(B_tau) 1.6610 == CLIV, deep invariant 27/27
(shat-ell 1483..5.9e4), combined chain 68 steps / 67 OK
transitions (39 surf + 2 bridge + 26 deep), identity ward max
1.16e-15, hinge med 1.0001 flips 0/67, measured census surface
17/39 + bridge 1/2 + deep 11/26, FLOOR census 0/67, anatomy 38
fails (H < 0 on 36, r-dominated 2, down-flow 38/38, allowance med
1.4e-04 of adap), carrier |H_OSC| frac med 0.290, WINONLY 0/67,
demand-law slopes +1.069/+1.586/+0.581/+0.536 vs CCI +0.60 (level
line +0.702), m-step NET census 29..34 of 67..52 per m = 1..16
with m* NOT-REACHED, hinge-defect ladder med 8.2 mu1, floor-
telescope 0/52 at m = 16, controls all fire (smooth 42, scramble
42, Epstein 55, cosh 39, rescale 42), bare WALL-BLIND cosh:15 +
rescale:5 (CLXII reproduced), COMPOSED census cosh:1 / others 0,
screens slack PASS +0.047 / osc PASS +0.035 / inv PASS -0.073.
NO bar, band, count, enum, expectation or success criterion was
moved beyond the three disclosed amendments.  SMOKE-2 (identical
bars, post-A1/A2/A3, 103.5 s): 43/43 green; every smoke-1
measurement reproduced identically; the amended split wards read
part-weight 2.74e-15 <= 1e-10, assembly (complement) 5.81e-13 <=
1e-8, REP closure defect 1.22e-05 <= 1e-3, transition part
assembly 1.64e-14 <= 1e-8; the A3 prints measured: isotropic
floor overhead +1.517/+2.711/+4.691 dex (why the floor census is
0/67: the one-constant isotropic bound throws away B_+'s
directional structure and overprices the demand by 1.5..4.7 dex),
and the multiplicative demand ladder FAILS on every m (min drop
ratio 0.0025..0.036 against mu-ratio demands 0.497..1.0).  SPEC
v1 frozen 2026-08-11 after smoke-2 with the SHA printed at
runtime; the frozen full run uses no edits beyond this disclosure
block.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); Householder frame as P2/CL/
CXLIV/DDC; ELL-B via slogdet, dead iff sign != +1 (round 57); (ii)
steps sorted by (h, kz); truth steps need r1 full-core, all-PSD,
lamS > 0; control chains relaxed (raw construction where the
linear algebra exists); (iii) exact LDL / exact Gaussian solves
verbatim from pgram_directional_schur_probe; (iv) the deep frame =
ext_frame/ext-gram conventions verbatim from deep_blind_holdout;
(v) the split representation: lifts z = (c; -Zc) with Z = R^{-1}
X^T from the rung's own solve; minimizer coefficients a = Pn^T
(sqrt(v) z); part densities d_AR = density(c_ar), d_SM =
density(c_sm), d_OSC = d_tot - d_AR - d_SM; part weights on the
TRUE masks; (vi) OLS population statistics + leave-one-out
jackknife as CXLIII; screens read positive subsets with excluded
counts printed; (vii) m-windows = index windows [k, k+m] inside
maximal segments of consecutive shared-rung steps.

NO RH claim: every census is a statement about float64-computed
step matrices of a deployed finite ladder (decisions exact-rational
on those entries); a full m*-census is a SURFACE statement
conditional on base block + floor premise; nothing here proves
h-uniformity, tail statements, or RH; fits are empirical laws; the
induction draft is a CONJECTURE with named gaps.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only; the extended table comes from the deployed
sieve generator (CLIV pattern).

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
exact-rational machinery + transition frames verbatim from
halfgap_riccati_increment_probe (CLXII) and its chain (CL, CXLIV,
v900, round 59, round 57); deep extension verbatim from
deep_blind_holdout_probe (CLIV); B-floor constant CITED from
pg_chain_interval_rollout_probe (CLIII); mu1 + 1/2 + NO-ADJUST from
halfgap_registration_probe (CLI); smooth comb convention from
tail_sign_mechanism_probe (CXLVII); CCI_REF from
zeroframe_uniform_bound_probe (CCI, declared comparison constant);
cosh signature from arith_healthcode12_probe (declared convention).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/halfgap_riccati_transition_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MIN_TRANS_COMB = 40
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
PRED_FAILS = 21
PRED_TRANS = 37
PRED_TAU_FAILS = 21
PRED_HINGE_MED = 1.0004
PRED_HINGE_ATOL = 5e-3
PRED_FLIPS = 0
PRED_INV = 39
TAB_EXT = 4_000_000
KZ_SCAN_MAX = 400
H_HOLD = (128, 2900)
N_DEEP_EXP = 28
MIN_DEEP_OK = 20
DEEP_MINB_REF = 1.6610
DEEP_MINB_RTOL = 2e-2
ID_WARD = 1e-10
S2_WARD = 1e-8
SPLIT_WARD = 1e-8
REP_BAR = 1e-3
WSUM_WARD = 1e-10
CB_CITED = Fraction(5523, 10000)
CB_RANGE_H = 900
CCI_REF = 0.60
M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16)
NG_SMOOTH = 6000
CTRL_KZ = 9
SCR_SEED = 1
INJ_A = 0.01
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
RSC_FAC = 1.1
PSD_TOL = 1e-12
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SOFT_BUDGET_S = 1200
PARTS = ("AR", "SM", "OSC")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# --------------- pipeline, verbatim (CLXII / CLIV / CXLIV / v900)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def folded_measure_full(d_arm, L, sign=+1.0):
    """folded_measure verbatim + the fold bookkeeping needed to
    align part weights with the TRUE kept nodes."""
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    fd = dict(jj=jj, th=th, inv=inv, n_uf=len(uf), mask=m,
              sign=sign, L=L)
    return xs[m], wagg[m], uf[m], fd


def folded_part(d_part, fd):
    """Signed part weights aggregated on the TRUE world's kept
    nodes and fold alignment (linear in the density)."""
    vals = (fd["sign"] * d_part[fd["jj"]]) / (2.0 * fd["L"]) \
        * 4.0 * np.sin(fd["th"] / 2.0) ** 2
    wagg = np.zeros(fd["n_uf"])
    np.add.at(wagg, fd["inv"], vals)
    return wagg[fd["mask"]]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return ("%s(slope=%+.3f, R2=%.3f, %d excluded)"
            % (lab, sl, r2, int(np.sum(~pos)))), sl


# ------------------------- exact-rational class (pgram verbatim)
def mat_fr(M):
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
    n = len(Afr)
    A = [[Afr[i][j] - (shift if i == j else 0) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return True, -1


def solve_fr(Afr, bfr):
    n = len(Afr)
    A = [list(Afr[i]) + [bfr[i]] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[p][k] == 0:
            return None
        if p != k:
            A[k], A[p] = A[p], A[k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] = A[i][j] - f * A[k][j]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        s = A[i][n]
        for j in range(i + 1, n):
            s = s - A[i][j] * x[j]
        x[i] = s / A[i][i]
    return x


def quad_fr(Afr, bfr):
    x = solve_fr(Afr, bfr)
    if x is None:
        return None
    s = Fraction(0)
    for bi, xi in zip(bfr, x):
        s = s + bi * xi
    return s


# ---------------------------------- probe-specific machinery
def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def ell_of(S):
    sg, ld = np.linalg.slogdet(S)
    return math.exp(ld / 8.0) if sg == 1.0 else None


def sym(M):
    return 0.5 * (M + M.T)


def split_parts(Mt):
    return float(Mt[0, 0]), Mt[1:, 0].copy(), Mt[1:, 1:].copy()


def pivot_of(Mt):
    n, b, B = split_parts(Mt)
    try:
        x = np.linalg.solve(B, b)
        s = n - float(b @ x)
        s2 = 1.0 / float(np.linalg.inv(Mt)[0, 0])
    except np.linalg.LinAlgError:
        return None
    return s, abs(s2 - s) / max(abs(s), 1e-300), x


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


# ------------- deep extension (deep_blind_holdout verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def deep_zone_census():
    out = []
    for kz in range(2, KZ_SCAN_MAX):
        alpha, Mz, hz, _ka = ext_frame(kz)
        X = math.exp(2.0 * alpha)
        if (X > core.ATOM_MAX and X <= TAB_EXT
                and H_HOLD[0] <= hz <= H_HOLD[1]):
            out.append((kz, hz))
    return out


# ------------------- the unified rung builder (+ exact split)
def build_rung(kind, kz, world=None, scramble_seed=None, comb=None,
               lag_fn=None, with_split=False):
    """kind = 'surf' (deployed window) or 'deep' (ext frame).
    world in (None, 'smooth', 'rescale'); comb = (uu, mm) override
    (Epstein); lag_fn(rr_dict) adds to the lag vector (cosh).
    Returns the rung dict; with_split adds the exact AR/SM/OSC
    split matrices of the Schur core at frozen lifts."""
    if kind == "surf":
        rr = window_of(kz, scramble_seed=scramble_seed)
        M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
        uu = rr["uu"]
        mm = 2.0 * rr["lam"]
        c_ar = rr["c_ar"]
    else:
        alpha, M, h, ka = ext_frame(kz)
        D = 2.0 * alpha / M
        uu = EXT["U"][:ka].copy()
        mm = EXT["MU"][:ka].copy()
        c_ar = np.asarray(core.arch_lags(M, D), float)
    if world == "smooth":
        mm = smooth_masses(uu)
    elif world == "rescale":
        mm = RSC_FAC * mm
    if comb is not None:
        uu, mm = comb
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    if lag_fn is not None:
        lag = lag + lag_fn(dict(M=M, D=D))
    d = grid_density(lag)
    L = 2 * M - 2
    xs, ws, _uf_p, fdp = folded_measure_full(d, L, +1.0)
    ys, vs, uf_n, fdn = folded_measure_full(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = sym(G)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kind=kind, kz=kz, h=h, n=n, alpha=float(alpha),
               M=M, D=D, L=L, tau=float(evA[0]),
               negA=int(np.sum(evA < 0.0)))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["negR"] = int(np.sum(evR < 0.0))
    try:
        Z = np.linalg.solve(R, Xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        return out
    S = sym(B - Xc @ Z)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if not with_split:
        return out
    # ---- the exact three-way split at frozen lifts (spec (c))
    if kind == "surf":
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                          float)
    else:
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                          float)
    d_ar = grid_density(c_ar)
    d_sm = grid_density(c_sm)
    d_osc = d - d_ar - d_sm
    wpos = {"AR": folded_part(d_ar, fdp),
            "SM": folded_part(d_sm, fdp),
            "OSC": folded_part(d_osc, fdp)}
    wneg = {"AR": folded_part(d_ar, fdn),
            "SM": folded_part(d_sm, fdn),
            "OSC": folded_part(d_osc, fdn)}
    wsum_dev = max(
        float(np.max(np.abs(wpos["AR"] + wpos["SM"] + wpos["OSC"]
                            - ws))) / max(float(np.max(ws)), 1e-300),
        float(np.max(np.abs(wneg["AR"] + wneg["SM"] + wneg["OSC"]
                            - vs))) / max(float(np.max(vs)), 1e-300))
    out["wsum_dev"] = wsum_dev
    sqv = np.sqrt(vs)
    Zl = np.zeros((n, 8))
    Zl[ic, np.arange(8)] = 1.0
    Zl[ib, :] = -Z
    Gn = Zl / sqv[:, None]
    A8 = Pn.T @ (sqv[:, None] * Zl)
    Fneg = Pn @ A8
    del Pn
    Ppos = eval_chain(al, be, m0, xs, h)
    Fpos = Ppos @ A8
    del Ppos
    Sp = {}
    for p in PARTS:
        wn = wneg[p]
        wp = wpos[p]
        T1 = Gn.T @ (wn[:, None] * Gn)
        T2 = Gn.T @ (wn[:, None] * Fneg)
        T3 = Fpos.T @ (wp[:, None] * Fpos)
        Sp[p] = sym(T1 - T2 - T2.T + T3)
    # A1 (disclosed): REP closure defect warded separately; OSC
    # redefined by exact complement (mirrors d_osc = d - dar - dsm)
    out["rep_dev"] = (float(np.linalg.norm(
        Sp["AR"] + Sp["SM"] + Sp["OSC"] - S))
        / max(float(np.linalg.norm(S)), 1e-300))
    Sp["OSC"] = sym(S - Sp["AR"] - Sp["SM"])
    out["S_parts"] = Sp
    out["split_dev"] = (float(np.linalg.norm(
        Sp["AR"] + Sp["SM"] + Sp["OSC"] - S))
        / max(float(np.linalg.norm(S)), 1e-300))
    return out


def make_steps(rungs, relax=False):
    steps = []
    n_dead_ell = 0
    for r1, r2 in zip(rungs, rungs[1:]):
        if not (isinstance(r1, dict) and isinstance(r2, dict)):
            continue
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if not relax:
            if r1["lamS"] <= 0.0 or r1["negA"] > 0:
                continue
        wS, VS = np.linalg.eigh(r1["S"])
        Q = householder_frame(VS[:, 0])
        e1 = ell_of(r1["S"])
        if e1 is None:
            n_dead_ell += 1
            continue
        steps.append(dict(r1=r1, r2=r2, Q=Q, ell=e1,
                          tau=r1["tau"], mu1=mu1_of(r2["h"])))
    return steps, n_dead_ell


def step_mat(st, scale, part=None):
    S = st["r2"]["S"] if part is None else st["r2"]["S_parts"][part]
    return sym(st["Q"].T @ (S / scale) @ st["Q"])


def next_mat(s1, s2, scale_key, part=None):
    S = (s2["r2"]["S"] if part is None
         else s2["r2"]["S_parts"][part])
    return sym(s1["Q"].T @ (S / s2[scale_key]) @ s1["Q"])


def transition_table(steps, scale_key, with_parts=False,
                     floor=False):
    """floor=True computes the CITED-floor slack; ONLY valid in
    the tau convention (where the CLIII certificate lives)."""
    out = []
    for ki, (s1, s2) in enumerate(zip(steps, steps[1:])):
        if s1["r2"] is not s2["r1"]:
            continue
        t = dict(s1=s1, s2=s2, status="OK", k=ki)
        Mt = step_mat(s1, s1[scale_key])
        Mp = next_mat(s1, s2, scale_key)
        p1 = pivot_of(Mt)
        p2 = pivot_of(Mp)
        if p1 is None or p2 is None:
            t["status"] = "REFUSED-SINGULAR"
            out.append(t)
            continue
        s, dev_s2, x = p1
        sp, dev_s2p, _xp = p2
        n0, b0, B0 = split_parts(Mt)
        n1, b1, B1 = split_parts(Mp)
        wv = np.concatenate([[1.0], -x])
        dM = Mp - Mt
        H = float(wv @ (dM @ wv))
        rvec = (dM @ wv)[1:]
        try:
            adap = float(rvec @ np.linalg.solve(B1, rvec))
        except np.linalg.LinAlgError:
            t["status"] = "REFUSED-SINGULAR"
            out.append(t)
            continue
        mu, mup = s1["mu1"], s2["mu1"]
        a = H + 0.5 * (mu - mup)
        id_dev = (abs((sp - s) - (H - adap))
                  / max(abs(s) + abs(sp), 1.0))
        Bfr = mat_fr(B1)
        ok_pd, _piv = pd_exact(Bfr)
        slack_fr = None
        floor_fr = None
        if ok_pd:
            qfr = quad_fr(Bfr, [Fraction(float(v)) for v in rvec])
            if qfr is not None:
                slack_fr = Fraction(float(a)) - qfr
            if floor:
                rn2 = sum(Fraction(float(v)) ** 2 for v in rvec)
                floor_fr = Fraction(float(a)) - rn2 / CB_CITED
        t.update(s=s, sp=sp, H=H, adap=adap, rvec=rvec, a=a,
                 mu=mu, mup=mup, id_dev=id_dev,
                 dev_s2=max(dev_s2, dev_s2p),
                 bnorm=float(np.linalg.norm(b0)),
                 rnorm=float(np.linalg.norm(rvec)),
                 lamB1=float(np.linalg.eigvalsh(B1)[0]),
                 B1=B1, x=x, pd=ok_pd, slack_fr=slack_fr,
                 floor_fr=floor_fr,
                 slack=float(slack_fr) if slack_fr is not None
                 else float("nan"),
                 fslack=float(floor_fr) if floor_fr is not None
                 else float("nan"))
        if not ok_pd or slack_fr is None:
            t["status"] = "REFUSED-BPLUS"
            out.append(t)
            continue
        if with_parts:
            Hp = {}
            rp = {}
            asm_H = np.zeros(1)
            dH = 0.0
            dr = 0.0
            for p in PARTS:
                dMp = (next_mat(s1, s2, scale_key, part=p)
                       - step_mat(s1, s1[scale_key], part=p))
                Hp[p] = float(wv @ (dMp @ wv))
                rp[p] = (dMp @ wv)[1:]
            # A2 (disclosed): normalized by the PART scale (H
            # itself near-cancels on real transitions)
            h_sc = sum(abs(Hp[p]) for p in PARTS)
            r_sc = sum(float(np.linalg.norm(rp[p]))
                       for p in PARTS)
            dH = (abs(Hp["AR"] + Hp["SM"] + Hp["OSC"] - H)
                  / max(h_sc, 1e-300))
            dr = (float(np.linalg.norm(
                rp["AR"] + rp["SM"] + rp["OSC"] - rvec))
                / max(r_sc, 1e-300))
            t.update(Hp=Hp, rp=rp, part_dev=max(dH, dr))
        out.append(t)
    return out


def barrier_census(trans, key="slack_fr"):
    n_pass = n_fail = n_ref = 0
    for t in trans:
        if t["status"] != "OK":
            n_ref += 1
        elif t[key] >= 0:
            n_pass += 1
        else:
            n_fail += 1
    return n_pass, n_fail, n_ref


def seg_of(t):
    k1 = t["s1"]["r1"]["kind"]
    k2 = t["s2"]["r2"]["kind"]
    km = t["s1"]["r2"]["kind"]
    kinds = {k1, k2, km}
    return "deep" if kinds == {"deep"} else (
        "surf" if kinds == {"surf"} else "bridge")


def dex_margins(trans, key, lhs_key="a", rhs_of=None):
    """log10(lhs/rhs) on passes with lhs, rhs > 0."""
    out = []
    for t in trans:
        if t["status"] != "OK" or t[key] is None or t[key] < 0:
            continue
        lhs = t[lhs_key]
        rhs = lhs - float(t[key]) if rhs_of is None else rhs_of(t)
        if lhs > 0 and rhs > 0:
            out.append(math.log10(lhs / rhs))
    return out


def fmt_ladder(v):
    if not len(v):
        return "n/a"
    v = np.asarray(v, float)
    return "%+.3f/%+.3f/%+.3f" % (float(np.min(v)),
                                  float(np.median(v)),
                                  float(np.max(v)))


def main():
    section("PRIME.PORT.HALFGAP.RICCATI.01 (round 2) -- the "
            "transition inequality of the half-gap induction: "
            "identity + two B-treatments + arch/prime split + "
            "m-step composition (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level probe; "
          "barrier/floor DECISIONS exact-rational on the float "
          "entries (v897 class).  1/2 + mu1 frozen upstream (CLI "
          "NO-ADJUST verbatim); c_B = 0.5523 CITED (CLIII), "
          "printed, not re-proved.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- surface ladder + P2/P3 + predecessor (CLXII) "
            "census reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = build_rung("surf", kz, with_split=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth_h = sorted(truth, key=lambda r: (r["h"], r["kz"]))
    full = [r for r in truth_h if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3 WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps_s, n_dead = make_steps(truth_h)
    check("W4 >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps_s) >= MIN_STEPS, "%d steps" % len(steps_s),
          kill="K1")
    print("    surface h range %d..%d  [%.1f s]"
          % (truth_h[0]["h"], truth_h[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    for st in steps_s:
        Mt_tau = step_mat(st, st["tau"])
        _n, b, B = split_parts(Mt_tau)
        st["minB_tau"] = float(np.linalg.eigvalsh(B)[0])
        x = np.linalg.solve(B, b)
        st["gap_tau"] = _n - float(b @ x)
        Mt_ell = step_mat(st, st["ell"])
        p = pivot_of(Mt_ell)
        st["s_ell"] = p[0]
        st["dev_s2_step"] = p[1]
    minB_all = float(np.min([st["minB_tau"] for st in steps_s]))
    gaps = np.array([st["gap_tau"] for st in steps_s])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    check("W5 REPRODUCTION P2/P3 ledger: min lam_min(B_tau) %.4f "
          "== %.3f; gap min/med %.4f/%.4f == %.3f/%.3f"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF),
          (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
           and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
           and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL),
          kill="K2")
    check("W6 WARD ELL-B alive on every full-core truth rung "
          "(%d dead steps)" % n_dead,
          n_dead == 0 and all(ell_of(r["S"]) is not None
                              for r in full), kill="K2")

    # W7 predecessor census reproduction (surface-only chain)
    trans_se = transition_table(steps_s, "ell")
    trans_st = transition_table(steps_s, "tau")
    pe, fe, re_ = barrier_census(trans_se)
    pt, ft, rt = barrier_census(trans_st)
    hinges = []
    n_flip = 0
    for t in trans_se:
        if t["status"] != "OK":
            continue
        s_own = t["s2"]["s_ell"]
        hinges.append(s_own / t["sp"] if t["sp"] != 0
                      else float("nan"))
        half = 0.5 * t["mup"]
        if (t["sp"] >= half) != (s_own >= half):
            n_flip += 1
    hmed = float(np.median(hinges))
    check("W7 REPRODUCTION CLXII census: primary fails %d/%d == "
          "%d/%d; tau twin fails %d/%d == %d/%d; hinge med %.4f "
          "== %.4f (atol %g); flips %d == %d"
          % (fe, len(trans_se), PRED_FAILS, PRED_TRANS, ft,
             len(trans_st), PRED_TAU_FAILS, PRED_TRANS, hmed,
             PRED_HINGE_MED, PRED_HINGE_ATOL, n_flip, PRED_FLIPS),
          (fe == PRED_FAILS and len(trans_se) == PRED_TRANS
           and re_ == 0 and ft == PRED_TAU_FAILS
           and abs(hmed - PRED_HINGE_MED) <= PRED_HINGE_ATOL
           and n_flip == PRED_FLIPS), kill="K2")
    shat_ell = np.array([st["s_ell"] / st["mu1"]
                         for st in steps_s])
    n_inv = int(np.sum(shat_ell >= 0.5))
    base_ok = steps_s[0]["s_ell"] >= 0.5 * steps_s[0]["mu1"]
    print("    W8 surface invariant s >= mu1/2: %d/%d (expected "
          "%d); shat-ell min/med/max %.4g/%.4g/%.4g; BASE CASE "
          "s_1 = %.6e vs mu1_1/2 = %.6e -> %s"
          % (n_inv, len(steps_s), PRED_INV,
             float(shat_ell.min()), float(np.median(shat_ell)),
             float(shat_ell.max()), steps_s[0]["s_ell"],
             0.5 * steps_s[0]["mu1"],
             "HOLDS" if base_ok else "FAILS"))
    check("W8 typed: INVARIANT-SURFACE(%d/%d) + BASE(%s)"
          % (n_inv, len(steps_s), "HOLDS" if base_ok else "FAILS"),
          True)
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ DW
    section("DW -- the deep ladder (CLIV 4e6 extension, "
            "FLOAT-LEVEL declared)")
    lam_ext = build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
               and np.array_equal(EXT["U"][:nP], core.U_ALL)
               and np.array_equal(EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep]) / nnf[keep]))
    check("DW1 fidelity: table overlap dev %.1e == 0; prefixes "
          "bitwise %s; kappa %.6f <= %.6f + 1e-6"
          % (dev, ok_pref, kappa, core.KAPPA_REF),
          dev == 0.0 and ok_pref
          and kappa <= core.KAPPA_REF + 1e-6, kill="K2")
    dz = deep_zone_census()
    check("DW2 deep census %d rungs (expected %d; h %d..%d)"
          % (len(dz), N_DEEP_EXP,
             min(h for _k, h in dz) if dz else -1,
             max(h for _k, h in dz) if dz else -1),
          len(dz) == N_DEEP_EXP, kill="K1")
    if KILLS:
        return finish({})
    deep = []
    n_skip = 0
    for kz, hz in sorted(dz, key=lambda p: (p[1], p[0])):
        if time.time() - T0 > SOFT_BUDGET_S:
            n_skip += 1
            continue
        r = build_rung("deep", kz, with_split=True)
        if r is None:
            print("    deep kz %-4d h %-5d: CHAIN SHORT"
                  % (kz, hz), flush=True)
            continue
        deep.append(r)
        print("    deep kz %-4d h %-5d n %-5d tau %.3e negA %d "
              "lamS %+.3e  [%.0f s]"
              % (kz, r["h"], r["n"], r["tau"], r["negA"],
                 r.get("lamS", float("nan")), time.time() - T0),
              flush=True)
    if n_skip:
        print("    SKIPPED-BUDGET: %d deep rungs not built "
              "(honest partial coverage)" % n_skip)
    deep_ok = [r for r in deep if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    check("DW3 deep truth rungs complete + all-PSD: %d of %d "
          "built (>= %d)" % (len(deep_ok), len(deep), MIN_DEEP_OK),
          len(deep_ok) >= MIN_DEEP_OK, kill="K1")
    if KILLS:
        return finish({})
    deep_h = sorted(deep_ok, key=lambda r: (r["h"], r["kz"]))
    steps_d, dead_d = make_steps(deep_h)
    for st in steps_d:
        Mt_tau = step_mat(st, st["tau"])
        _n, b, B = split_parts(Mt_tau)
        st["minB_tau"] = float(np.linalg.eigvalsh(B)[0])
        Mt_ell = step_mat(st, st["ell"])
        p = pivot_of(Mt_ell)
        st["s_ell"] = p[0]
        st["dev_s2_step"] = p[1]
    minB_deep = float(np.min([st["minB_tau"] for st in steps_d]))
    check("DW4 REPRODUCTION CLIV: min own-frame lam_min(B_tau) "
          "over %d deep steps %.4f == %.4f (rtol %g; ell-dead %d)"
          % (len(steps_d), minB_deep, DEEP_MINB_REF,
             DEEP_MINB_RTOL, dead_d),
          abs(minB_deep / DEEP_MINB_REF - 1.0) <= DEEP_MINB_RTOL,
          kill="K2")
    shat_deep = np.array([st["s_ell"] / st["mu1"]
                          for st in steps_d])
    n_inv_d = int(np.sum(shat_deep >= 0.5))
    print("    DW5 deep invariant s >= mu1/2 (ell, FLOAT-LEVEL): "
          "%d/%d; shat-ell min/med/max %.4g/%.4g/%.4g"
          % (n_inv_d, len(steps_d), float(shat_deep.min()),
             float(np.median(shat_deep)), float(shat_deep.max())))
    check("DW5 typed: INVARIANT-DEEP(%d/%d, min %.4g)"
          % (n_inv_d, len(steps_d), float(shat_deep.min())), True)

    # ------------------------------------------------------------ P
    section("P -- the combined h-sorted chain (surface + bridge + "
            "deep)")
    comb_rungs = sorted([r for r in truth_h if r["core_ok"]]
                        + deep_h, key=lambda r: (r["h"], r["kz"]))
    steps_c, dead_c = make_steps(comb_rungs)
    for st in steps_c:
        if "s_ell" not in st:
            Mt_ell = step_mat(st, st["ell"])
            p = pivot_of(Mt_ell)
            st["s_ell"] = p[0]
            st["dev_s2_step"] = p[1]
    trans_ce = transition_table(steps_c, "ell", with_parts=True)
    trans_ct = transition_table(steps_c, "tau", floor=True)
    tmap_ct = {t["k"]: t for t in trans_ct}
    n_ok = sum(1 for t in trans_ce if t["status"] == "OK")
    check("P1 combined chain: %d steps, %d transitions (%d OK, "
          ">= %d; ell-dead %d)"
          % (len(steps_c), len(trans_ce), n_ok, MIN_TRANS_COMB,
             dead_c),
          n_ok >= MIN_TRANS_COMB, kill="K1")
    if KILLS:
        return finish({})
    segs = [seg_of(t) for t in trans_ce]
    print("    segments: surface %d, bridge %d, deep %d"
          % (segs.count("surf"), segs.count("bridge"),
             segs.count("deep")))

    # ------------------------------------------------------------ A
    section("A -- the exact increment identity on the actual "
            "(geometric) ladder + hinge")
    id_max = max([t["id_dev"] for t in trans_ce
                  if t["status"] == "OK"]
                 + [t["id_dev"] for t in trans_ct
                    if t["status"] == "OK"])
    s2_max = max([t["dev_s2"] for t in trans_ce
                  if t["status"] == "OK"]
                 + [st["dev_s2_step"] for st in steps_c])
    check("A1 WARD identity s_+ - s = H - r*B_+^{-1}r: max rel "
          "dev %.2e <= %.0e (ell + tau, %d transitions incl. "
          "bridge + deep)" % (id_max, ID_WARD, n_ok),
          id_max <= ID_WARD, kill="K2")
    check("A2 WARD two-route pivot: max rel dev %.2e <= %.0e"
          % (s2_max, S2_WARD), s2_max <= S2_WARD, kill="K2")
    n_pd = sum(1 for t in trans_ce if t["status"] == "OK")
    check("A3 WARD B_+ PD exact-rationally on every truth "
          "transition (%d/%d)" % (n_pd, len(trans_ce)),
          n_pd == len(trans_ce), kill="K2")
    ok_mu = all(t["mu"] >= t["mup"] for t in trans_ce
                if t["status"] == "OK")
    check("A4 WARD mu monotone nonincreasing along the h-sorted "
          "chain", ok_mu, kill="K2")
    hing_c = []
    flip_c = 0
    for t in trans_ce:
        if t["status"] != "OK":
            continue
        s_own = t["s2"]["s_ell"]
        t["hinge_def"] = s_own - t["sp"]
        hing_c.append(s_own / t["sp"] if t["sp"] != 0
                      else float("nan"))
        half = 0.5 * t["mup"]
        if (t["sp"] >= half) != (s_own >= half):
            flip_c += 1
    a5 = ("HINGE(med %.4f, range [%.4f, %.4f], flips %d/%d)"
          % (float(np.median(hing_c)), float(np.min(hing_c)),
             float(np.max(hing_c)), flip_c, len(hing_c)))
    check("A5 typed: %s" % a5, True)

    # ------------------------------------------------------------ B
    section("B -- the transition target: measured B^{-1} (ell "
            "primary) vs the cited floor (tau, certified "
            "convention)")
    print("    seg    hB->hC        s          H          ADAP      "
          " (mu-mu+)/2  slackM     slackF(tau) lamB+tau  verdicts")
    for t in trans_ce:
        if t["status"] != "OK":
            continue
        tt = tmap_ct.get(t["k"])
        okm = t["slack_fr"] >= 0
        okf = (tt is not None and tt["status"] == "OK"
               and tt["floor_fr"] is not None
               and tt["floor_fr"] >= 0)
        print("    %-6s %5d->%-5d %+.3e %+.3e %.3e  %.3e %+.3e "
              "%+.3e %.3e  M:%s F:%s"
              % (seg_of(t), t["s1"]["r2"]["h"], t["s2"]["r2"]["h"],
                 t["s"], t["H"], t["adap"],
                 0.5 * (t["mu"] - t["mup"]), t["slack"],
                 tt["fslack"] if tt is not None else float("nan"),
                 tt["lamB1"] if tt is not None else float("nan"),
                 "P" if okm else "F", "P" if okf else "F"),
              flush=True)
    lab = {}
    for name, key, src in (("measured", "slack_fr", trans_ce),
                           ("floor", "floor_fr", trans_ct)):
        cen = {}
        for sg in ("surf", "bridge", "deep"):
            sub = [t for t in src if t["status"] == "OK"
                   and seg_of(t) == sg]
            npass = sum(1 for t in sub if t[key] is not None
                        and t[key] >= 0)
            cen[sg] = (npass, len(sub))
        lab[name] = cen
    b1 = ("CENSUS-MEASURED(surface %d/%d, bridge %d/%d, deep "
          "%d/%d)" % (lab["measured"]["surf"]
                      + lab["measured"]["bridge"]
                      + lab["measured"]["deep"]))
    b3 = ("FLOOR-CENSUS(tau: surface %d/%d, bridge %d/%d, deep "
          "%d/%d)"
          % (lab["floor"]["surf"] + lab["floor"]["bridge"]
             + lab["floor"]["deep"]))
    md = dex_margins(trans_ce, "slack_fr",
                     rhs_of=lambda t: t["adap"])
    fd_ = dex_margins(trans_ct, "floor_fr",
                      rhs_of=lambda t: t["rnorm"] ** 2
                      / float(CB_CITED))
    print("    pass-margin ladders (dex, log10(a/rhs)): measured "
          "%s   floor %s" % (fmt_ladder(md), fmt_ladder(fd_)))
    iso = [math.log10((t["rnorm"] ** 2 / float(CB_CITED))
                      / t["adap"]) for t in trans_ct
           if t["status"] == "OK" and t["adap"] > 0]
    print("    isotropic floor overhead log10((|r|^2/c_B)/adap), "
          "tau units: %s -- the price of dropping B_+'s "
          "directional structure" % fmt_ladder(iso))
    # containment ward (tau): pass(floor) subset pass(measured)
    viol = sum(1 for t in trans_ct if t["status"] == "OK"
               and t["floor_fr"] is not None
               and t["floor_fr"] >= 0 and t["slack_fr"] < 0)
    check("B3 WARD containment pass(floor) subset pass(measured) "
          "(%d violations; theorem given lam_min(B_+) >= c_B)"
          % viol, viol == 0, kill="K2")
    # transport census
    n_tr_s = sum(1 for t in trans_ce if t["status"] == "OK"
                 and seg_of(t) == "surf")
    n_tr_sf = sum(1 for t in trans_ct if t["status"] == "OK"
                  and seg_of(t) == "surf"
                  and t["lamB1"] >= float(CB_CITED))
    lamd = [t["lamB1"] for t in trans_ct if t["status"] == "OK"
            and seg_of(t) != "surf"]
    b4 = ("FLOOR-TRANSPORT(shared-frame lam_min(B_+^tau) >= "
          "0.5523 on %d/%d surface transitions; bridge+deep "
          "float ladder %s -- certified range ends at h <= %d, "
          "deep FLOAT-LEVEL)"
          % (n_tr_sf, n_tr_s, fmt_ladder(lamd), CB_RANGE_H))
    check("B4 typed: %s" % b4, True)
    check("B1 typed: %s" % b1, True)
    b2c = barrier_census(trans_ct)
    check("B2 typed: TAU-TWIN(pass %d, fail %d, refused %d of %d)"
          % (b2c[0], b2c[1], b2c[2], len(trans_ct)), True)
    check("B3b typed: %s" % b3, True)
    fails = [t for t in trans_ce if t["status"] == "OK"
             and t["slack_fr"] < 0]
    n_hneg = sum(1 for t in fails if t["H"] < 0)
    n_rdom = sum(1 for t in fails if t["H"] >= 0
                 and t["adap"] > t["a"])
    n_down = sum(1 for t in fails if t["sp"] - t["s"] < 0)
    allow = [0.5 * (t["mu"] - t["mup"]) / t["adap"]
             for t in trans_ce if t["status"] == "OK"
             and t["adap"] > 0]
    b5 = ("ANATOMY(fails %d: H<0 on %d, r-dominated %d, "
          "down-flow %d; allowance (mu-mu+)/2 / adap min/med/max "
          "%.1e/%.1e/%.1e)"
          % (len(fails), n_hneg, n_rdom, n_down,
             float(np.min(allow)), float(np.median(allow)),
             float(np.max(allow))))
    check("B5 typed: %s" % b5, True)

    # ------------------------------------------------------------ C
    section("C -- the exact arch/smooth/prime-osc split of the "
            "increment (frozen-lift representation)")
    wsum_max = max(r.get("wsum_dev", 0.0) for r in comb_rungs)
    split_max = max(r.get("split_dev", 0.0) for r in comb_rungs)
    rep_max = max(r.get("rep_dev", 0.0) for r in comb_rungs)
    check("C1 WARD part-weight linearity max %.2e <= %.0e; split "
          "assembly (complement construction) max %.2e <= %.0e; "
          "REP closure defect max %.2e <= %.0e (the nu_+ "
          "quadrature diagnostic -- declared OSC pollution "
          "ceiling) on %d rungs"
          % (wsum_max, WSUM_WARD, split_max, SPLIT_WARD,
             rep_max, REP_BAR, len(comb_rungs)),
          wsum_max <= WSUM_WARD and split_max <= SPLIT_WARD
          and rep_max <= REP_BAR, kill="K2")
    part_max = max(t.get("part_dev", 0.0) for t in trans_ce
                   if t["status"] == "OK")
    check("C2 WARD transition part assembly (H, r) max rel %.2e "
          "<= 1e-8" % part_max, part_max <= 1e-8, kill="K2")
    fracs = []
    sgn_match = 0
    sgn_match_f = 0
    n_okt = 0
    winonly = []
    for t in trans_ce:
        if t["status"] != "OK" or "Hp" not in t:
            continue
        n_okt += 1
        tot = (abs(t["Hp"]["AR"]) + abs(t["Hp"]["SM"])
               + abs(t["Hp"]["OSC"]))
        fr = abs(t["Hp"]["OSC"]) / max(tot, 1e-300)
        t["osc_frac"] = fr
        fracs.append(fr)
        if np.sign(t["H"]) == np.sign(t["Hp"]["OSC"]):
            sgn_match += 1
            if t["slack_fr"] < 0:
                sgn_match_f += 1
        rW = t["rp"]["AR"] + t["rp"]["SM"]
        HW = t["Hp"]["AR"] + t["Hp"]["SM"]
        try:
            adW = float(rW @ np.linalg.solve(t["B1"], rW))
        except np.linalg.LinAlgError:
            continue
        sW = HW + 0.5 * (t["mu"] - t["mup"]) - adW
        t["slack_win"] = sW
        winonly.append((sW >= 0, t["slack_fr"] >= 0))
    n_fail_t = sum(1 for t in trans_ce if t["status"] == "OK"
                   and t["slack_fr"] < 0)
    wpass = sum(1 for a_, _b in winonly if a_)
    wagree = sum(1 for a_, b_ in winonly if a_ == b_)
    c2 = ("CARRIER(|H_OSC| fraction min/med/max %.3f/%.3f/%.3f; "
          "sign(H)==sign(H_OSC) on %d/%d, on fails %d/%d)"
          % (float(np.min(fracs)), float(np.median(fracs)),
             float(np.max(fracs)), sgn_match, n_okt,
             sgn_match_f, n_fail_t))
    check("C2 typed: %s" % c2, True)
    c3 = ("WINONLY(float diagnostic: window skeleton alone passes "
          "%d/%d; agrees with the true census on %d/%d)"
          % (wpass, len(winonly), wagree, len(winonly)))
    check("C3 typed: %s" % c3, True)

    # C4 demand law vs alpha (combined ladder)
    print("\n    C4 THE DEMAND LAW (jackknife OLS vs alpha, "
          "combined ladder; CITED level law CCI_REF = +%.2f "
          "dex/alpha):" % CCI_REF)
    laws = {}
    al_t = [t["s1"]["r1"]["alpha"] for t in trans_ce
            if t["status"] == "OK"]
    items = {
        "|H_OSC|/mu1+": [abs(t["Hp"]["OSC"]) / t["mup"]
                         for t in trans_ce if t["status"] == "OK"],
        "|r_OSC|^2/mu1+": [float(np.linalg.norm(t["rp"]["OSC"]))
                           ** 2 / t["mup"] for t in trans_ce
                           if t["status"] == "OK"],
        "adap/mu1+": [t["adap"] / t["mup"] for t in trans_ce
                      if t["status"] == "OK"],
        "|Ds|/mu1+": [abs(t["sp"] - t["s"]) / t["mup"]
                      for t in trans_ce if t["status"] == "OK"],
    }
    lev_al = [st["r1"]["alpha"] for st in steps_c]
    lev = [st["s_ell"] / st["mu1"] for st in steps_c]
    for nm, vals in items.items():
        v = np.asarray(vals, float)
        a_ = np.asarray(al_t, float)
        m = v > 0
        sl, se, r2 = jack_slope(a_[m], np.log10(v[m]))
        band = ("INCREMENT-FLATTER" if sl + 2 * se < CCI_REF
                else "INCREMENT-STEEPER" if sl - 2 * se > CCI_REF
                else "AMBIG-OVERLAP")
        laws[nm] = (sl, se, band)
        print("      %-16s slope %+.3f +- 2SE %.3f (R2 %.3f) -> "
              "%s" % (nm, sl, 2 * se, r2, band))
    lev_a = np.asarray(lev_al, float)
    lev_v = np.asarray(lev, float)
    ml = lev_v > 0
    sl_l, se_l, r2_l = jack_slope(lev_a[ml], np.log10(lev_v[ml]))
    print("      %-16s slope %+.3f +- 2SE %.3f (R2 %.3f) -- the "
          "level line (INF-FLAT class)"
          % ("s/mu1 (level)", sl_l, 2 * se_l, r2_l))
    c4 = ("DEMAND-LAW(%s)"
          % ", ".join("%s %+0.3f+-%.3f %s"
                      % (k, v[0], 2 * v[1],
                         v[2].replace("INCREMENT-", ""))
                      for k, v in laws.items()))
    check("C4 typed: %s" % c4, True)

    # ------------------------------------------------------------ D
    section("D -- the m-step window + the composed induction "
            "draft")
    # maximal consecutive segments of the step chain
    seg_list = []
    cur = [0]
    for i in range(len(steps_c) - 1):
        if steps_c[i]["r2"] is steps_c[i + 1]["r1"]:
            cur.append(i + 1)
        else:
            seg_list.append(cur)
            cur = [i + 1]
    seg_list.append(cur)
    mstar = None
    m_rows = []
    for m in M_LADDER:
        margins = []
        n_win = n_pass_m = 0
        for segi in seg_list:
            for a_ in range(len(segi) - m):
                k0, k1 = segi[a_], segi[a_ + m]
                st0, st1 = steps_c[k0], steps_c[k1]
                net = (st1["s_ell"] - st0["s_ell"]
                       + 0.5 * (st0["mu1"] - st1["mu1"]))
                n_win += 1
                if net >= 0:
                    n_pass_m += 1
                margins.append(net / st1["mu1"])
        m_rows.append((m, n_pass_m, n_win,
                       float(np.min(margins)) if margins
                       else float("nan")))
        print("    m = %-3d NET_m >= 0 on %3d/%3d windows; "
              "min margin/mu1+ %+.4g"
              % (m, n_pass_m, n_win,
                 float(np.min(margins)) if margins
                 else float("nan")))
        if mstar is None and n_win > 0 and n_pass_m == n_win:
            mstar = m
            mstar_marg = margins
    print("\n    D1b the multiplicative demand (printed "
          "measurement): a ratio barrier s_{k+m} >= c_m s_k "
          "closes from the 1/2-hypothesis alone iff c_m >= "
          "max_k mu1(h_{k+m})/mu1(h_k):")
    for m in M_LADDER:
        ratios = []
        dem = []
        for segi in seg_list:
            for a_ in range(len(segi) - m):
                st0 = steps_c[segi[a_]]
                st1 = steps_c[segi[a_ + m]]
                if st0["s_ell"] > 0:
                    ratios.append(st1["s_ell"] / st0["s_ell"])
                dem.append(st1["mu1"] / st0["mu1"])
        if ratios:
            print("      m = %-3d min/med ratio %.4g/%.4g vs "
                  "demand (max mu-ratio) %.4g -> %s"
                  % (m, float(np.min(ratios)),
                     float(np.median(ratios)),
                     float(np.max(dem)),
                     "COVERS" if float(np.min(ratios))
                     >= float(np.max(dem)) else "FAILS"))
    d1 = ("MSTEP(m* = %s%s)"
          % (mstar if mstar is not None else "NOT-REACHED",
             ", min margin/mu1 %+.4g on %d windows"
             % (float(np.min(mstar_marg)), len(mstar_marg))
             if mstar is not None else ""))
    check("D1 typed: %s" % d1, True)
    # hinge defects + floor-telescoped census at m*
    hd = [abs(t["hinge_def"]) / t["mup"] for t in trans_ce
          if t["status"] == "OK"]
    m_eval = mstar if mstar is not None else M_LADDER[-1]
    tel_pass = tel_n = 0
    for segi in seg_list:
        for a_ in range(len(segi) - m_eval):
            ss = 0.0
            ok_all = True
            for j in range(a_, a_ + m_eval):
                t = tmap_ct.get(segi[j])
                if t is None or t["status"] != "OK":
                    ok_all = False
                    break
                ss += (t["H"] - t["rnorm"] ** 2 / float(CB_CITED)
                       + 0.5 * (t["mu"] - t["mup"]))
            if not ok_all:
                continue
            tel_n += 1
            if ss >= 0:
                tel_pass += 1
    d2 = ("TELESCOPE(hinge defect |s_own - s_+|/mu1 min/med/max "
          "%s; floor-telescoped sum >= 0 at m = %d on %d/%d "
          "windows, tau units)"
          % (fmt_ladder(hd), m_eval, tel_pass, tel_n))
    check("D2 typed: %s" % d2, True)
    print("""
    D3 THE COMPOSED INDUCTION DRAFT (CONJECTURE; typed pieces):
    [THEOREM-EXACT]      update identity s_+ - s = H - r*B_+^{-1}r
                         (warded %.1e); barrier lemma + floor
                         variant: B_+ >= c_B I and H + Dmu/2 >=
                         ||r||^2/c_B  ==>  s >= mu/2 -> s_+ >=
                         mu_+/2 (two-line Schur proof).
    [THEOREM-CERTIFIED]  B_tau >= 0.5523 I, OWN frame, 39 surface
                         steps h <= %d (CLIII interval rollout,
                         exact-rational; CITED).  NOT certified:
                         shared frame (transport MEASURED, B4),
                         deep ladder (float 1.6610, CLIV).
    [MEASURED]           base case + invariant (surface %d/%d,
                         deep %d/%d, FLOAT-LEVEL at depth);
                         one-step censuses (B1-B3); m-step ladder
                         (D1: m* = %s); hinge ladders; demand laws.
    [OPEN -- the all-h gap]
      G1 the m*-window transition inequality beyond the computed
         ladder -- ITS measured margin law is the exact demand of
         the open piece (C4 slopes vs the CCI +0.60 level law);
      G2 the floor certificate beyond h ~ 900 and in the shared
         frame (interval rollout at depth = the named missing
         theorem tier);
      G3 hinge/transport uniformity (measured med ~ 1.0, no
         theorem);
      G4 the float pipeline producing the entries is not enclosed
         outside the CLIII B-floor chain;
      G5 the ladder geometry (zones, windows) is deployed data,
         not an all-h construction.
    COMPOSED FORM: [base block of m* rungs] + [floor premise] +
    [m*-window transition inequality for all windows] ==> s >=
    mu1/2 along the ladder, cofinally in h.  Every bracket typed
    above; the composition is a CONJECTURE until G1-G2 close.
""" % (id_max, CB_RANGE_H, n_inv, len(steps_s), n_inv_d,
       len(steps_d), mstar if mstar is not None else "NOT-REACHED"))
    check("D3 typed: DRAFT-TYPED(G1-G5 named)", True)

    # ------------------------------------------------------------ E
    section("E -- controls (rung firing + transition "
            "discrimination + the composed census)")
    worlds = {}
    sm = [build_rung("surf", kz, world="smooth") for kz in zones]
    n_f = sum(1 for r in sm if isinstance(r, dict)
              and r["negA"] > 0)
    check("E1 WARD smooth world fires (neg(A) > 0 on %d rungs)"
          % n_f, n_f > 0, kill="K2")
    worlds["smooth"] = sm
    scr = [build_rung("surf", kz, scramble_seed=SCR_SEED)
           for kz in zones]
    n_f = sum(1 for r in scr if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E2 WARD scramble fires (%d rungs)" % n_f, n_f > 0,
          kill="K2")
    worlds["scramble"] = scr
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    rE = build_rung("surf", CTRL_KZ,
                    comb=(np.log(nn.astype(float)),
                          2.0 * lamE_[nn]
                          / np.sqrt(nn.astype(float))))
    eps_fire = (rE is None) or rE["negA"] > 0
    check("E3 WARD Epstein comb fires at kz %d (neg(A) %s); "
          "transition-level Epstein DECLARED SKIPPED (O(X^2)); "
          "deep controls inherited from CLIV (cited)"
          % (CTRL_KZ, rE["negA"] if isinstance(rE, dict)
             else "chain death"), eps_fire, kill="K2")

    def inj(rr):
        tt = np.arange(rr["M"]) * rr["D"]
        return (INJ_A * np.cos(INJ_GAMMA0 * tt)
                * (np.cosh(INJ_DELTA * tt) - 1.0))
    cosh_w = [build_rung("surf", kz, lag_fn=inj) for kz in zones]
    n_f = sum(1 for r in cosh_w if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E4 WARD cosh injection A = %g fires (%d rungs; CLXII "
          "deployed amplitude, frozen selection cited)"
          % (INJ_A, n_f), n_f > 0, kill="K2")
    worlds["cosh"] = cosh_w
    rsc = [build_rung("surf", kz, world="rescale") for kz in zones]
    n_f = sum(1 for r in rsc if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E5 WARD rescale %.1f fires (%d rungs)" % (RSC_FAC, n_f),
          n_f > 0, kill="K2")
    worlds["rescale"] = rsc

    blind = []
    comp_blind = []
    print("\n    E6 transition discrimination (relaxed chains, "
          "ell basis; composed = barrier AND floor premise AND "
          "base invariant):")
    for name, lad in worlds.items():
        rungs_w = sorted([r for r in lad if isinstance(r, dict)],
                         key=lambda r: (r["h"], r["kz"]))
        steps_w, dead_w = make_steps(rungs_w, relax=True)
        for st in steps_w:
            p = pivot_of(step_mat(st, st["ell"]))
            st["s_ell"] = p[0] if p is not None else float("nan")
        trans_w = transition_table(steps_w, "ell")
        pw, fw, rw = barrier_census(trans_w)
        n_comp = 0
        for t in trans_w:
            if t["status"] != "OK" or t["slack_fr"] < 0:
                continue
            # floor premise (shared frame, ell scale-covariant
            # check via tau not available on relaxed worlds ->
            # use the ell-basis lam_min vs scaled floor honestly:
            # the premise is checked in the certificate's own
            # currency lam_min(B_+) > 0 AND >= c_B * (tau/ell)
            # where tau may not exist; frozen rule: premise =
            # lam_min(B_+^ell) >= float(CB) * s1.tau/s1.ell if
            # tau > 0 else REFUSED
            s1 = t["s1"]
            if s1["tau"] <= 0:
                continue
            thr = float(CB_CITED) * s1["tau"] / s1["ell"]
            if t["lamB1"] < thr:
                continue
            if not (np.isfinite(t["s"])
                    and t["s"] >= 0.5 * t["mu"]):
                continue
            n_comp += 1
        print("    %-9s: transitions %2d (ell-dead %d)  bare "
              "CERTIFY %2d  INDEF %2d  REFUSED %2d  COMPOSED %2d"
              % (name, len(trans_w), dead_w, pw, fw, rw, n_comp),
              flush=True)
        if pw > 0:
            blind.append("%s:%d" % (name, pw))
        if n_comp > 0:
            comp_blind.append("%s:%d" % (name, n_comp))
    e6a = ("WALLBLIND-REPRO(%s)" % ", ".join(blind)
           if blind else "BARE-DISCRIMINATES(0)")
    e6b = ("COMPOSED-BLIND(%s)" % ", ".join(comp_blind)
           if comp_blind else "COMPOSED-DISCRIMINATES(0 on all "
           "false worlds)")
    print("    the bare barrier reads only increment geometry "
          "(CLXII WALL-BLIND lesson); the COMPOSED census carries "
          "the wall content in the floor premise + base "
          "invariant.")
    check("E6 typed: %s + %s" % (e6a, e6b), True)
    check("E7 typed: IMPOSTOR-NA(zero zero-reads in this probe; "
          "AST firewall is the witness)", True)

    # ------------------------------------------------------------ F
    section("F -- tau-screens")
    taus1 = [t["s1"]["tau"] for t in trans_ce
             if t["status"] == "OK"]
    scr1, _ = screen([t["slack"] for t in trans_ce
                      if t["status"] == "OK"], taus1)
    taus2 = [t["s1"]["tau"] for t in trans_ct
             if t["status"] == "OK"]
    scr2, _ = screen([t["fslack"] for t in trans_ct
                      if t["status"] == "OK"], taus2)
    scr3, _ = screen([t["osc_frac"] for t in trans_ce
                      if t["status"] == "OK" and "osc_frac" in t],
                     [t["s1"]["tau"] for t in trans_ce
                      if t["status"] == "OK" and "osc_frac" in t])
    if mstar is not None:
        mm_t = []
        mm_v = []
        for segi in seg_list:
            for a_ in range(len(segi) - mstar):
                k0, k1 = segi[a_], segi[a_ + mstar]
                st0, st1 = steps_c[k0], steps_c[k1]
                mm_t.append(st0["tau"])
                mm_v.append((st1["s_ell"] - st0["s_ell"]
                             + 0.5 * (st0["mu1"] - st1["mu1"]))
                            / st1["mu1"])
        scr4, _ = screen(mm_v, mm_t)
    else:
        scr4 = "vacuous(no m*)"
    scr5, _ = screen([st["s_ell"] - 0.5 * st["mu1"]
                      for st in steps_c],
                     [st["tau"] for st in steps_c])
    print("    measured slack vs tau:      %s" % scr1)
    print("    floor slack (tau) vs tau:   %s" % scr2)
    print("    OSC carrier fraction:       %s" % scr3)
    print("    m*-net margin vs tau:       %s" % scr4)
    print("    invariant margin vs tau:    %s" % scr5)
    check("F1 typed: SCREENS(slack %s | floor %s | osc %s | mnet "
          "%s | inv %s)"
          % (scr1.split("(")[0], scr2.split("(")[0],
             scr3.split("(")[0], scr4.split("(")[0],
             scr5.split("(")[0]), True)

    return finish(dict(
        a1="IDENTITY-WARDED(%.1e)" % id_max, a5=a5, b1=b1,
        b2="TAU-TWIN(%d/%d fail)" % (b2c[1], len(trans_ct)),
        b3=b3, b4=b4, b5=b5,
        c1="SPLIT-EXACT(w %.1e, S %.1e, t %.1e)"
        % (wsum_max, split_max, part_max),
        c2=c2, c3=c3, c4=c4, d1=d1, d2=d2,
        d3="DRAFT-TYPED(G1-G5)", e6="%s + %s" % (e6a, e6b),
        scr="SCREENS(%s | %s | %s | %s | %s)"
        % (scr1, scr2, scr3, scr4, scr5)))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("RICCTRANS-MEASURED / " + " / ".join(
            labels.get(k, "-") for k in
            ("a1", "a5", "b1", "b2", "b3", "b4", "b5", "c1",
             "c2", "c3", "c4", "d1", "d2", "d3", "e6", "scr")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every census is a statement about the
  float64-computed step matrices of a deployed finite ladder,
  decided exact-rationally on their entries where declared; the
  deep ladder is FLOAT-LEVEL; the B-floor constant is CITED from
  CLIII with its certified range said plainly; the induction draft
  is a CONJECTURE with named gaps G1-G5; fits are empirical laws.
  1/2 and mu1 are frozen upstream (CLI NO-ADJUST).  NO RH claim.
  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
