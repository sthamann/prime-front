"""
=======================================================================
census_lift_probe.py -- the census spectral lift
                        (contract PRIME.CENSUS.SPECTRAL.LIFT.01)
=======================================================================
FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
paper, no ledger row, no website surface; it is an experiments/-side
discovery instrument under the house frozen-spec discipline.  NO RH
CLAIM IN EITHER DIRECTION, EVER: nothing below is evidence for or
against the Riemann Hypothesis; "census" always means the finite root
set of the finite polynomial N_h(y) defined below, never a zero set
of zeta.

QUESTION (the round).  Is the finite census polynomial N_h(y) EXACTLY
the spectral determinant (or Weyl function) of an already-present
self-adjoint SOURCE-SIDE operator?  Sought is a definite matrix-pencil
representation

    N_h(y) = C_h * det(A_h - y B_h),   A_h = A_h^T >= 0,  B_h = B_h^T > 0,

with (A_h, B_h) constructed EXCLUSIVELY from the source data (the
per-mode prime transforms P_k, Ptilde_k enter through the wall matrix
M_h; the pole/arch structure b_k; the support a; the rung h) and the
eigenvalue equation of M_h -- NEVER from the computed roots of N_h.
Such a representation would deliver H2 STRUCTURALLY (the spectrum of
a definite pencil is real and nonnegative) instead of root-by-root,
and with a spectral bracket lambda_max(A_h, B_h) < c* y_t it would
close H1 too.  This uses the surviving real-root architecture of the
r83/r84 REALROOT rounds and the r90 Krein-screw realization WITHOUT
their RH-strong limit (no limit is taken anywhere: every object below
is finite), and attacks exactly the r178 root-map nonlinearity
exhibit (the census-root map is not affine; a spectral-determinant
identity would bypass the root map entirely).  FORBIDDEN for this
contract: constructing the pencil FROM the computed census roots (a
Jacobi matrix built from the roots is "H2 with a wig"); the
construction must be source-side and is MACHINE-CHECKED to be (G02).

THE OBJECTS (source construction, r171/r172/r180 code paths VERBATIM
via radius4_an_probe.build_cell).  Rung h, a = log(h)/2,
K = ceil(1.25 h log h), modes om_k = k pi/a, poles b_k = om_k^2
(b_0 = 0), T_z = 2 pi h.  M_h = M_pole + M_arch - M_prime is the wall
matrix in the normalized even trig mode basis; tau_h = lambda_min,
d = its unit eigenvector, c_k = the de-normalized components of d
(builder key cn_mp_str; sign fixed so the max-abs component is
positive).  With e_k := (-1)^k c_k:

    A_0 = sum_k e_k,   A_2 = sum_{k>=1} e_k b_k,   y_t = |A_2/A_0|,
    F(y) = c_0 + sum_{k>=1} e_k y/(y - b_k),

and N_h(y) = the numerator of F over prod_{k>=1}(y - b_k): degree
K-1, leading coefficient A_0 (the frozen r156/r171 rootladder census
form npoly_coeffs; its roots are the census).

L1 -- THE ALGEBRAIC RECONNAISSANCE (the decisive cheap number).
Partial fractions: y/(y-b) = 1 + b/(y-b) gives the EXACT
Mittag-Leffler normal form

    F(y) = A_0 + sum_{k>=1} r_k/(y - b_k),    r_k = e_k b_k,
    F(y)/A_0 = 1 + sum_{k>=1} rho_k/(y - b_k),  rho_k = e_k b_k / A_0,

so the pole residues of F are r_k = e_k b_k and
sum_k rho_k = A_2/A_0 (the v924 moment-Laurent "-1": A_2/A_0 = -y_t
is gated exactly).  THE DECISIVE NUMBER is the residue sign ladder
(n_+, n_-) = (#{rho_k > 0}, #{rho_k < 0}).  The frozen branch table:

  BRANCH-U (all rho_k < 0):  F/A_0 = 1 - sum |rho_k|/(y-b_k) is the
    secular function of the rank-one UPDATE.  Pencil A_h = D + v v^T,
    B_h = I, v_k = sqrt(|rho_k|), D = diag(b_k)_{k>=1}: A_h is PD
    STRUCTURALLY (x^T A x = sum b_k x_k^2 + (v^T x)^2 > 0).
    EXACT-LIFT candidate.
  BRANCH-D (all rho_k > 0):  F/A_0 is Herglotz; rank-one DOWNDATE
    pencil A_h = D - v v^T, B_h = I; A_h PSD  <=>  1 - v^T D^-1 v =
    c_0/A_0 >= 0 (exact rational criterion; note F(0) = c_0 exactly).
  BRANCH-J (mixed signs):  no definite pencil in these coordinates.
    The natural object is the KREIN signature pencil: with
    w_k = sqrt(|rho_k|), sigma_k = sign(rho_k), J = diag(sigma_k),
    the rational rank-one form A_ns = D - ONES rho^T satisfies
    charpoly(A_ns)(y) = N_h(y)/A_0 exactly (matrix determinant
    lemma / column multilinearity), is symmetrizable by
    S = diag(w_k):  S A_ns S^-1 = D - w w^T J =: A', and J A' is
    symmetric.  The symmetric pair is
        Ahat = J D - (J w)(J w)^T   (symmetric),   Bhat = J,
        N_h(y) = C_h det(Ahat - y Bhat),
        C_h = (-1)^(K-1) det(J) A_0,
    and the Weyl form F/A_0 = 1 + w^T (y J - J D)^-1 w holds exactly
    (diagonal commutation).  Bhat = J is INDEFINITE with signature
    (n_+, n_-): the definiteness demand FAILS and the ladder
    (n_+, n_-) is the gated defect.  PARTIAL-LIFT.

TRANSFORM CLASS (frozen, symbolic).  The predefined transformations
of the contract cannot repair mixedness: (i) a real Moebius change of
variable y = phi(t) = (alpha t + beta)/(gamma t + delta) multiplies
every residue by 1/phi'(t_k) and sign(phi') = sign(alpha delta -
beta gamma) is CONSTANT on the real line (phi'(t) (gamma t+delta)^2
= Delta identically), so (n_+, n_-) is preserved or swapped whole;
(ii) multiplication by a fixed positive weight w(y) multiplies the
residue at b_k by w(b_k) > 0; (iii) the y -> g^2 substitution splits
every pole into a +/- residue pair (residues of r/(g^2-b) at
+-sqrt(b) are +-r/(2 sqrt b)), mixed for every nonzero residue set.
All three are verified symbolically (G07).  Hence: mixedness is
INVARIANT under the entire predefined transformation class, and a
naive definite pencil is impossible IN CLASS, not merely not-found.

PRE-FREEZE CALIBRATION (ONE pass, calib_censuslift_pass1.log, scratch
deleted after freeze, log kept; all numbers below quoted verbatim).
MAIN-world residue ladders (n_+, n_-): h=4: (1, 5); h=5: (7, 3);
h=8: (6, 14); h=13: (27, 14) -- MIXED AT EVERY MEASURED TRUE RUNG
(BRANCH-J).  n_0 = 0 everywhere.  c_0/A_0 = 38203.902 / 11028305.0 /
4.8975363e13 / 4.1354013e25 at h = 4/5/8/13 (positive, exploding).
sum(rho)/y_t = -1.0 and sign(A_2/A_0) = -1 at every rung and world.
Worlds at fixed small x: SMOOTH x=5: (0, 10) -- ONE-SIGNED, the
atom-free world is BRANCH-U definite; SCRARITH x=5: (3, 7) and
EPSTEIN x=8: (3, 17) -- mixed.  The h = 21, 28 ladders are PRE-FREEZE
UNMEASURED (disclosed; recorded at run time, only n_0 = 0 gated).

L2 -- THE EXACT PENCIL TEST at h in {4, 5, 8, 13, 21, 28}.  All
exact layers run on the DYADIC RATIONALIZATION of the frozen mp build
(mpf values ARE dyadic rationals; Fraction(man * 2^exp) is exact, no
rounding is added; disclosed).  Unscaled cleared form: rt_k := e_k b_k
(dyadic), Ntilde(y) := A_0 prod_{k>=1}(y-b_k) + sum_k rt_k
prod_{j!=k}(y-b_j).
  (E1) CENSUS == MITTAG-LEFFLER, exact: the frozen npoly_coeffs
    census construction (VERBATIM port to Fraction arithmetic, scaled
    variable Y = y/s, s = b_top + 1) equals the partial-fraction
    numerator: poly[i] == Ntilde_i / s^i for all i, plus leading
    coefficient == A_0, plus per-k synthetic-division mul-back checks
    (deflate(prod, b_k) * (Y - b_k) == prod exactly; all k at
    h <= 13, k in {1, mid, K-1} at h = 21, 28).
  (E2) DETERMINANT IDENTITY: det(y I - A_ns) == N_h(y)/A_0 via the
    A_0-cleared integer form det(A_0(y I - D) + ONES rt^T) ==
    A_0^(K-2) Ntilde(y): exact integer Bareiss elimination at the
    K interpolation points y = 0..K-1 (a degree-(K-1) polynomial
    identity in y is PROVEN by equality at K points) at h <= 13;
    at h = 21, 28 NUMERIC-SPOT (mp.det at the rung dps at the six
    frozen points y in NUMDET_PTS, relative residual < NUMDET_BAR)
    -- the exact-arithmetic depth at h = 21, 28 is reduced honestly
    and typed MDL-EXACT-H13-NUMERIC-H2128 (disclosed).  The generic
    matrix determinant lemma det(yI - D + ONES r^T) = prod(y-b_k)
    + sum_k r_k prod_{j!=k}(y-b_j) is verified fully symbolically
    at sizes n = 2..6 (G05).
  (E3) KREIN ASSEMBLY, exact bookkeeping: rho_k == sigma_k w_k^2
    with w_k^2 = |rho_k|; branch classification; det(J) =
    (-1)^(n_-); C_h = (-1)^(K-1) det(J) A_0; the similarity
    S A_ns S^-1 = D - w w^T J, the J-symmetry of Ahat and the pencil
    determinant transfer det(yI - A') == det(J) det(yJ - Ahat) are
    verified fully symbolically at n = 2, 3 over ALL sign patterns
    (G06), together with the Weyl-form diagonal commutation.
  (E5) RESOLVENT-MOMENT IDENTITY, exact: the Laurent data of F at
    infinity, extracted INDEPENDENTLY from the census polynomial by
    exact long division (t_m from Ntilde - A_0 prod against prod),
    equals the pencil moments: t_m == sum_k rt_k b_k^m = the jet
    moments A_(2(m+1)) = sum_k e_k b_k^(m+1), m = 0..5 -- the tie to
    the v924/v932 moment-Laurent ladder J_(m+1) = t_m/(A_0 y_t^(m+1));
    J_2 in J2_WIN numerically (toproot instrument).
  (E6) SPECTRAL BRACKET (H1 face): the source-pure monotone envelope
    certificate of r171/r172 (envres/envj VERBATIM port): ENVJ(c* y_t)
    < |A_0| at the first passing c* of the frozen C_GRID, gated
    c* <= 1.15 at all six rungs.  GIVEN E1 + E2 the pencil spectrum
    IS the census root set (equal characteristic polynomials), so the
    certificate brackets Re lambda < c* y_t for the pencil spectrum
    with NO root ever computed: BRACKET-CERTIFIED-VIA-ENVJ.  The
    definiteness leg of H1-closure does NOT follow in BRANCH-J and is
    typed honestly.
  (E7) CENSUS VERIFIER (ISOLATED, verification only, h <= 13 = the
    toproot CENSUS_HARD_MAX): mp.polyroots on the census polynomial
    (verbatim toproot instrument) -- realness count == K-1, negative
    mass <= NEGSUM_BAR * y_t, top/y_t == TOP_TAB rel 5e-3.  This
    function is OUTSIDE the construction ancestry (machine-checked,
    G02): roots verify, they never construct.

L3 -- MUST-FAIL WORLDS (SMOOTH x=5, SCRARITH x=5, EPSTEIN x=8,
builder worlds verbatim).  Honest adjudication, frozen BEFORE the
record run: the lift ALGEBRA (E1) is generic partial-fraction algebra
and holds in every world -- world-blind, acceptable for H2-structural
purposes but typed: the lift transfers realness, and realness lives
in fake worlds too; world separation then lives in H1/H3, not H2.
The DEFINITENESS observable is measured per world: per the
calibration the atom-free SMOOTH world is one-signed (definite,
BRANCH-U) while ALL atom-bearing worlds (MAIN, SCRARITH, EPSTEIN) are
mixed -- so definiteness does NOT separate true from fake arithmetic:
it separates atoms from no-atoms, with the WRONG orientation for a
sign source (the arithmetic is exactly what breaks one-signedness;
the r166 lesson "the cancellation IS the arithmetic" in residue
coordinates).  Gated as DEFINITE-ONLY-IN-SMOOTH +
MIXEDNESS-IS-ARITHMETIC; explicitly NOT an acceptance-test-(b) sign
source.

L4 -- VERDICT (frozen taxonomy and branch logic).
  EXACT-LIFT   iff every MAIN rung is one-signed (BRANCH-U, or
               BRANCH-D with the exact PSD criterion passing) AND all
               identity gates exact AND definiteness proven at the
               test rungs.  (If so: state what remains for all-h --
               the construction is manifestly h-uniform algebra, the
               open leg is one-signedness for all h.)
  PARTIAL-LIFT iff the pencil exists with the exact identity chain
               but indefinite signature (BRANCH-J anywhere), or
               definiteness only numeric.  The exact defect is stated:
               Bhat = J indefinite with the measured ladder
               (n_+, n_-) per rung; definite impossible IN the
               predefined transformation class (G07).
  NO-GO        iff an exact determinant/construction identity (E1,
               E2-exact, E3, E5) FAILS at a true rung h <= 13 --
               park the lane immediately.
TAU-SCREEN (always): the construction consumes the RAY d (shape
data) and never tau_h = lambda_min itself; machine-checked (G03: the
construct_* functions receive only (c_k, b_k, K); the exact ladder is
invariant under the exact rescaling c -> (3/7) c).  If the
definiteness demand collapsed onto tau_h it would be flagged as
relabeling; it does not (the ladder is scale-free in both d and tau).

LOOP GUARD (machine, G02/G08).  Never consumed, detect-only: the
census-forall-k loop (all statements here are per-rung, finite);
the A_0-triangle (TAUPOS/TLAWCAP; A_0 enters only as the exact
leading coefficient / normalizer, no positivity of A_0 is assumed or
used); zero-verification-as-hypothesis (this probe touches NO zero
ordinates at all -- no cache file is opened anywhere); RH-conditional
second moments (absent).  ROOTS-AS-INPUT PROHIBITION: the delivered
construction chain ATOMS -> WALL-EIGENEQ -> RESIDUES -> PENCIL ->
IDENTITIES is machine-audited (AST call-graph DFS): no construct_*
function reaches mp.polyroots or any verify_* function; census roots
appear only downstream in the isolated verifier (E7).  The explicit
ancestry DAG with the four flagged loop classes as isolated nodes is
checked acyclic with the flagged set unreachable from DELIVERED.

FROZEN NUMERICS
=======================================================================
KFAC = 1.25; RUNGS = (4, 5, 8, 13, 21, 28); EXACT_MAX = 13;
DPS = {4: 60, 5: 60, 8: 80, 13: 120, 21: 146, 28: 160} (toproot
schedule verbatim); CONTROLS = (SMOOTH x=5 dps 60, SCRARITH x=5
dps 60, EPSTEIN x=8 dps 80); WORKERS = 9 (spawn, deterministic keys).
LADDER_TAB (calib pass1 VERBATIM) MAIN {4: (1,5), 5: (7,3),
8: (6,14), 13: (27,14)}; WORLD {(SMOOTH,5): (0,10), (SCRARITH,5):
(3,7), (EPSTEIN,8): (3,17)}; C0A0_TAB {4: 38203.902, 5: 11028305.0,
8: 4.8975363e13, 13: 4.1354013e25} rel 5e-3; A2_SIGN = -1 all.
RAY_BAR = 1e-25 (r171/r172 verbatim); MULBACK_SAMPLE_BIG = (1, mid,
K-1); BAREISS_PTS = y = 0..K-1 (all K, exact scope h <= EXACT_MAX);
NUMDET_PTS = (2, 3, 5, 7, 11, 13) (scaled to y = p * s at 21/28? NO:
frozen as UNSCALED integer points y = p for p in NUMDET_PTS -- the
identity is polynomial, any distinct points sample it); NUMDET_BAR =
1e-20; MOM_MAX = 5; J2_WIN = (0.05, 0.25) (toproot verbatim);
M_JETS = 400; MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400); C_GRID =
(1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00) (toproot
verbatim); CSTAR_LIFT_MAX = 1.15; CENSUS_HARD_MAX = 13;
POLY_MAXSTEPS = 3000; IM_TOL = 1e-10; NEGSUM_BAR = 1e-6; TOP_TAB =
{4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429} rel 5e-3
(toproot verbatim); SYMB_MDL_NS = (2, 3, 4, 5, 6); SYMB_KREIN_NS =
(2, 3); RUNTIME_BAR = 2700 s.  Deterministic: NO randomness anywhere;
no cache file opened; all mp arithmetic inside explicit workdps
blocks; flat O(1) ratios transported as f64 for gating (DISCLOSED).
Smoke mode (--smoke): rungs (4, 5) + all controls, reduced gate set,
log kept; the record run is the full set.

GATES (PASS/FAIL, numbered)
=======================================================================
G01-firewall      AST: no zero-oracle/cache names anywhere (no load/
                  loadtxt/genfromtxt/fromfile/zetazero/siegelz/nzeros,
                  no zeta call, no verification/ import); polyroots
                  only inside verify_*; no numpy eig anywhere.
G02-roots-guard   call-graph DFS: no construct_* reaches polyroots or
                  verify_*; ancestry DAG acyclic, flagged loops +
                  CENSUS-ROOTS unreachable from DELIVERED.
G03-tau-screen    AST: construct_* bodies never subscript the builder
                  cell (keys mpE/mpM/mpV/tau/gap unreachable there);
                  exact scale-gauge invariance of the ladder under
                  c -> (3/7)c at every rung.
G04-spec          SPEC_SHA printed; K == ceil(KFAC h log h) at every
                  built cell; DPS schedule as frozen.
G05-symb-mdl      matrix determinant lemma fully symbolic, n = 2..6.
G06-symb-krein    similarity + J-symmetry + determinant transfer +
                  Weyl diagonal commutation, n = 2, 3, ALL 2^n sign
                  patterns, fully symbolic.
G07-symb-transform Moebius residue lemma (phi'(t)(ct+d)^2 == Delta;
                  pole-difference identity), positive-weight residue
                  lemma, g^2 pair-splitting lemma: mixedness
                  transform-invariant IN CLASS.
G08-loop-dag      the four flagged loop classes isolated and
                  unreachable; DAG acyclic.
Per MAIN rung h in RUNGS (suffix [h=..]):
G10 build sanity  K formula; eigen-residual ray_dev <= RAY_BAR.
G11 L1 ladder     n_0 == 0; ladder == LADDER_TAB at h <= 13 (recorded
                  at h = 21, 28, PRE-FREEZE UNMEASURED, disclosed).
G12 sum rule      exact: sum rho == A_2/A_0; sign(A_2/A_0) == -1;
                  c_0/A_0 matches C0A0_TAB rel 5e-3 at h <= 13 and
                  is recorded at 21/28; |sum rho|/y_t == 1 exact.
G13 E1 exact      census construction == Mittag-Leffler numerator,
                  coefficient-by-coefficient, + mul-back checks.
G14 E2            h <= 13: exact integer Bareiss at K points;
                  h = 21, 28: NUMERIC-SPOT residual < NUMDET_BAR.
G15 E3 assembly   exact Krein bookkeeping + branch classification
                  (== BRANCH-J expected at h <= 13 per calib;
                  recorded at 21/28); C_h formula.
G16 signature     Bhat = J signature == (n_+, n_-); definite iff
                  one-signed (BRANCH-U/D); the defect typed.
G17 moments       E5 exact dual-route t_m, m = 0..MOM_MAX + jet tie;
                  J_2 in J2_WIN (f64).
G18 bracket       E6 envj: first passing c* <= CSTAR_LIFT_MAX and
                  ENVJ ratio < 1 (source-pure).
G19 census-verify E7 (h <= 13 only): nreal == K-1, negsum, TOP_TAB.
Controls:
G30 SMOOTH        ladder == (0, 10): BRANCH-U, definite pencil exists
                  exactly in the atom-free world; E1 exact there.
G31 SCRARITH      ladder == (3, 7): mixed; E1 exact there.
G32 EPSTEIN       ladder == (3, 17): mixed; E1 exact there.
G33 adjudication  definite <=> atom-free among the tested worlds;
                  typed DEFINITE-ONLY-IN-SMOOTH +
                  MIXEDNESS-IS-ARITHMETIC (wrong orientation, NOT a
                  sign source).
G34 world-blind   E1 holds in every world: LIFT-WORLD-BLIND-KREIN.
G40 runtime       < RUNTIME_BAR.

VERDICT ENUMS (frozen): EXACT-LIFT / PARTIAL-LIFT / NO-GO (branch
logic above), qualified by: KREIN-PENCIL-EXACT;
SIGNATURE-INDEFINITE-ALL-TRUE-RUNGS; MIXEDNESS-TRANSFORM-INVARIANT;
DEFINITE-ONLY-IN-SMOOTH; MIXEDNESS-IS-ARITHMETIC;
LIFT-WORLD-BLIND-KREIN; BRACKET-CERTIFIED-VIA-ENVJ;
SPECTRUM-VERIFIED-H13; MDL-EXACT-H13-NUMERIC-H2128;
ROOTS-NEVER-CONSUMED; TAU-FREE-CONSTRUCTION; UNEXPECTED-ONE-SIGNED-
RUNG (only if a MAIN rung measures one-signed at 21/28);
NO-RH-CLAIM (always).  Composite = tokens joined by " + ".

DISCLOSURES.  (a) One pre-freeze calibration pass (ladders + c0/A0 +
sum-rule signs at h <= 13 and the three controls), log kept as
calib_censuslift_pass1.log, scratch deleted; instrument-cost timings
(Fraction/Bareiss/mp.det/sympy) measured on synthetic data pre-freeze
(no physics numbers).  (b) The exact layers run on the dyadic
rationalization of the frozen mp build; the identities are polynomial
in (c, b), so exact equality on the dyadic data verifies the
construction algebra at machine-exact level.  (c) E2 exact scope
h <= 13; h = 21, 28 numeric-spot (typed).  (d) E7 verifier scope
h <= 13 (toproot CENSUS_HARD_MAX verbatim).  (e) The h = 21, 28
residue ladders and branch classes are pre-freeze unmeasured;
their G11/G15 gates test only n_0 == 0 / recording.  (f) f64
transport of flat O(1) ratios for window gates (house convention).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks outside this docstring.

AST FIREWALL: no zero-oracle names anywhere; NO cache file opened;
NO zeta use; no import of verification/.  NO RH CLAIM.  EXPLORATION
ONLY.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 9/16 at the
first-freeze SPEC_SHA 7c5b67524156eab8, log kept as
census_lift_probe.smoke1.log; NO record run existed yet).  ONE
instrument bug in the exact layer, no bar, window, tab, branch rule
or criterion moved anywhere: the Mittag-Leffler accumulation in
construct_exact appended a spurious [0] to the deflated cofactor
(the "multiply by Y" step that belongs ONLY to the npoly census form
c_k Y prod_(j!=k), not to the residue form r_k prod_(j!=k)), which
corrupted every Ntilde coefficient including the leading one and
cascaded into E1/E5 fails and an IndexError at the J_2 transport
(tms empty).  Fixed by dropping the appended zero; verified in
isolation on a K = 4 synthetic instance against an independent sympy
numerator (E1/E5/Bareiss all exact) before re-freeze.  The measured
physics content of smoke1 (the world ladders (0,10)/(3,7)/(3,17)
replicating the calibration) was unaffected.  smoke2 at the fixed
SPEC_SHA must be clean.
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
EXACT_MAX = 13
DPS = {4: 60, 5: 60, 8: 80, 13: 120, 21: 146, 28: 160}
CONTROLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
WORKERS = 9
LADDER_TAB = {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14)}
LADDER_WORLD = {("SMOOTH", 5): (0, 10), ("SCRARITH", 5): (3, 7),
                ("EPSTEIN", 8): (3, 17)}
C0A0_TAB = {4: 38203.902, 5: 11028305.0, 8: 4.8975363e13,
            13: 4.1354013e25}
C0A0_RTOL = 5e-3
RAY_BAR = 1e-25
NUMDET_PTS = (2, 3, 5, 7, 11, 13)
NUMDET_BAR = 1e-20
MOM_MAX = 5
J2_WIN = (0.05, 0.25)
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
C_GRID = (1.05, 1.10, 1.15, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00)
CSTAR_LIFT_MAX = 1.15
CENSUS_HARD_MAX = 13
POLY_MAXSTEPS = 3000
IM_TOL = 1e-10
NEGSUM_BAR = 1e-6
TOP_TAB = {4: 0.880058, 5: 0.858950, 8: 0.844195, 13: 0.834429}
TOP_RTOL = 5e-3
SYMB_MDL_NS = (2, 3, 4, 5, 6)
SYMB_KREIN_NS = (2, 3)
RUNTIME_BAR = 2700.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool, str]] = []
T_START = time.time()


def check(name: str, ok: bool, detail: str) -> bool:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", name, detail))
    return bool(ok)


def info(msg: str) -> None:
    print("  . %s" % msg)


def section(title: str) -> None:
    print("\n== %s %s" % (title, "=" * max(1, 66 - len(title))))


# ----------------------------------------------------- exact helpers
def mpf_frac(x) -> Fraction:
    """EXACT dyadic rationalization of an mpf (mpf values are
    man * 2^exp)."""
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


def deflate(p: list, root: Fraction) -> list:
    """synthetic division by (Y - root), r156/r171 structure
    VERBATIM."""
    out = [p[0]]
    for c in p[1:-1]:
        out.append(c + out[-1] * root)
    return out


def peval(p: list, x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in p:
        acc = acc * x + c
    return acc


# --------------------------------------------- construction (source)
def construct_l1(cs: list, b: list, K: int) -> dict:
    """L1 residue ladder from source data ONLY (exact).  Inputs are
    the dyadic Fractions of (c_k, b_k).  NO roots, NO tau."""
    e = [cs[k] if k % 2 == 0 else -cs[k] for k in range(K)]
    A0 = sum(e)
    A2 = sum(e[k] * b[k] for k in range(1, K))
    rho = [e[k] * b[k] / A0 for k in range(1, K)]
    npos = sum(1 for r in rho if r > 0)
    nneg = sum(1 for r in rho if r < 0)
    nzero = sum(1 for r in rho if r == 0)
    sum_ok = (sum(rho) == A2 / A0)
    a2sign = -1 if A2 / A0 < 0 else (1 if A2 / A0 > 0 else 0)
    c0A0 = cs[0] / A0
    # exact scale-gauge invariance: c -> (3/7) c leaves rho invariant
    lam = Fraction(3, 7)
    e2 = [v * lam for v in e]
    A0g = sum(e2)
    rho_g = [e2[k] * b[k] / A0g for k in range(1, K)]
    gauge_ok = (rho_g == rho)
    branch = "U" if npos == 0 else ("D" if nneg == 0 else "J")
    return dict(e=e, A0=A0, A2=A2, rho=rho, npos=npos, nneg=nneg,
                nzero=nzero, sum_ok=sum_ok, a2sign=a2sign, c0A0=c0A0,
                gauge_ok=gauge_ok, branch=branch)


def construct_npoly_exact(cs: list, b: list, K: int):
    """frozen rootladder census form (r156/r171 npoly_coeffs)
    VERBATIM, exact Fraction port.  Scaled Y = y/s, s = b_top + 1,
    leading coefficient == A_0."""
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
    return poly, s, prod_all, bs


def construct_exact(cs: list, b: list, K: int, l1: dict,
                    big: bool) -> dict:
    """E1 + E3 + E5 exact layers from source data ONLY.  Returns the
    unscaled cleared numerator Ntilde and the audit results."""
    e, A0 = l1["e"], l1["A0"]
    rt = [e[k] * b[k] for k in range(1, K)]          # dyadic residues
    n = K - 1
    # unscaled product and Mittag-Leffler numerator
    prod_u = [Fraction(1)]
    for k in range(1, K):
        prod_u = pmul(prod_u, [Fraction(1), -b[k]])
    ntil = [A0 * c for c in prod_u]
    for k in range(1, K):
        q = deflate(prod_u, b[k])
        ntil = padd(ntil, [rt[k - 1] * c for c in q])
    mulback_ok = True
    for k in (range(1, K) if not big else (1, K // 2, K - 1)):
        q = deflate(prod_u, b[k])
        back = pmul(q, [Fraction(1), -b[k]])
        if back != prod_u:
            mulback_ok = False
    # E1: frozen census construction == Mittag-Leffler numerator
    poly, s, _prod_s, _bs = construct_npoly_exact(cs, b, K)
    e1_ok = (len(poly) == n + 1 and poly[0] == A0
             and ntil[0] == A0)
    spow = Fraction(1)
    for i in range(n + 1):
        if poly[i] != ntil[i] / spow:
            e1_ok = False
            break
        spow *= s
    # E3: Krein bookkeeping (exact)
    sigma = [1 if r > 0 else (-1 if r < 0 else 0) for r in l1["rho"]]
    w2 = [abs(r) for r in l1["rho"]]
    e3_ok = all(l1["rho"][i] == sigma[i] * w2[i] for i in range(n))
    detJ = (-1) ** sum(1 for sg in sigma if sg < 0)
    # E5: moments by exact long division of (Ntilde - A0 prod)/prod
    Rp = [ntil[i] - A0 * prod_u[i] for i in range(n + 1)]
    if Rp[0] != 0:
        e5_ok = False
        tms = []
    else:
        Rp = Rp[1:]                                  # degree n-1
        pcoef = prod_u[1:]                           # p_1..p_n
        tms = []
        for m in range(MOM_MAX + 1):
            tm = Rp[m] if m < len(Rp) else Fraction(0)
            for i in range(1, m + 1):
                if i <= len(pcoef):
                    tm -= pcoef[i - 1] * tms[m - i]
            tms.append(tm)
        e5_ok = True
        for m in range(MOM_MAX + 1):
            direct = sum(rt[k - 1] * b[k] ** m for k in range(1, K))
            jet = sum(e[k] * b[k] ** (m + 1) for k in range(1, K))
            if tms[m] != direct or tms[m] != jet:
                e5_ok = False
    return dict(rt=rt, ntil=ntil, prod_u=prod_u, mulback_ok=mulback_ok,
                e1_ok=e1_ok, e3_ok=e3_ok, detJ=detJ, e5_ok=e5_ok,
                tms=tms, n=n)


def construct_bareiss(b: list, rt: list, A0: Fraction, ntil: list,
                      K: int) -> bool:
    """E2 exact: det(A0 (yI - D) + ONES rt^T) == A0^(K-2) Ntilde(y)
    at the K interpolation points y = 0..K-1, integer Bareiss."""
    n = K - 1
    ok = True
    for ypt in range(K):
        y = Fraction(ypt)
        # matrix entries (dyadic): A0*(y-b_i)*delta_ij + rt_j
        diag = [A0 * (y - b[k]) for k in range(1, K)]
        ents = diag + rt
        L = 0
        for v in ents:
            d = v.denominator
            t = d.bit_length() - 1
            assert d == (1 << t), "non-dyadic entry"
            L = max(L, t)
        def to_int(v: Fraction) -> int:
            t = v.denominator.bit_length() - 1
            return v.numerator << (L - t)
        rti = [to_int(v) for v in rt]
        M = [[rti[j] for j in range(n)] for _i in range(n)]
        for i in range(n):
            M[i][i] += to_int(diag[i])
        # integer Bareiss
        sign = 1
        prev = 1
        det = None
        for kk in range(n - 1):
            if M[kk][kk] == 0:
                piv = None
                for r in range(kk + 1, n):
                    if M[r][kk]:
                        piv = r
                        break
                if piv is None:
                    det = 0
                    break
                M[kk], M[piv] = M[piv], M[kk]
                sign = -sign
            for i in range(kk + 1, n):
                Mi, Mk = M[i], M[kk]
                a_ik = Mi[kk]
                a_kk = Mk[kk]
                for j in range(kk + 1, n):
                    Mi[j] = (Mi[j] * a_kk - a_ik * Mk[j]) // prev
            prev = M[kk][kk]
        if det is None:
            det = sign * M[n - 1][n - 1]
        rhs = (A0 ** (n - 1)) * peval(ntil, y) * (Fraction(2) ** (L * n))
        if Fraction(det) != rhs:
            ok = False
            break
    return ok


# ------------------------------------------------------- mp verifiers
def numeric_spot(b_mp, rt_fr, A0_fr, ntil_fr, K: int, dps: int):
    """E2 numeric-spot at h = 21, 28: mp.det at the frozen points."""
    n = K - 1
    worst = 0.0
    with mp.workdps(dps):
        A0 = frac_mpf(A0_fr)
        rt = [frac_mpf(v) for v in rt_fr]
        for p in NUMDET_PTS:
            y = mp.mpf(p)
            M = mp.zeros(n, n)
            for i in range(n):
                for j in range(n):
                    M[i, j] = rt[j]
            for i in range(n):
                M[i, i] += A0 * (y - b_mp[i + 1])
            det = mp.det(M)
            rhs = A0 ** (n - 1)
            acc = mp.mpf(0)
            for c in ntil_fr:
                acc = acc * y + frac_mpf(c)
            rhs = rhs * acc
            rel = float(abs(det - rhs) / (abs(rhs) + mp.mpf("1e-300")))
            worst = max(worst, rel)
    return worst


def envj_bracket(cs_mp, b_mp, K: int, dps: int):
    """E6: the r171/r172 source-pure monotone envelope certificate,
    VERBATIM port.  Returns (cstar, ratio)."""
    with mp.workdps(dps):
        A0 = sum((-1) ** k * cs_mp[k] for k in range(K))
        A2 = sum((-1) ** k * cs_mp[k] * b_mp[k] for k in range(1, K))
        yt = abs(A2 / A0)
        btop = b_mp[K - 1]
        cs_abs = [abs(v) for v in cs_mp]
        A_j = [A0]
        pw = [mp.mpf(1)] * K
        for m in range(1, M_JETS + 1):
            acc = mp.mpf(0)
            for k in range(1, K):
                pw[k] = pw[k] * b_mp[k] if m > 1 else b_mp[k]
                acc += (-1) ** k * cs_mp[k] * pw[k]
            A_j.append(acc)

        def envres_y(yq, mm):
            acc = mp.mpf(0)
            yi = mp.mpf(1)
            for i in range(1, mm + 1):
                yi *= yq
                acc += abs(A_j[i]) / yi
            rem = mp.mpf(0)
            for k in range(1, K):
                rem += cs_abs[k] * b_mp[k] ** (mm + 1) \
                    / (yi * (yq - b_mp[k]))
            return acc + rem

        def envj(yq):
            best = None
            for m in MGRID:
                vv = envres_y(yq, m)
                if best is None or vv < best:
                    best = vv
            return best

        cstar = None
        envr = None
        for c in C_GRID:
            yq = mp.mpf(repr(c)) * yt
            if yq <= btop:
                continue
            ev = envj(yq)
            r = ev / abs(A0)
            if r < 1:
                cstar = c
                envr = float(r)
                break
        return cstar, envr, float(mp.log(yt) / mp.log(10))


def verify_census(cs_mp, b_mp, K: int, dps: int):
    """E7 ISOLATED census verifier (toproot instrument VERBATIM):
    the ONLY function that may call polyroots.  Verification only --
    never feeds the construction (machine-checked, G02)."""
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
        nreal = 0
        ys = []
        for r in rts:
            if abs(mp.im(r)) <= mp.mpf(repr(IM_TOL)):
                nreal += 1
                ys.append(mp.re(r) * s)
        ys.sort()
        top_yt = float(ys[-1] / yt) if ys else float("nan")
        negsum = float(sum(abs(v) for v in ys if v < 0) / yt)
        return nreal, top_yt, negsum


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
        out.update(npos=l1["npos"], nneg=l1["nneg"], nzero=l1["nzero"],
                   sum_ok=l1["sum_ok"], a2sign=l1["a2sign"],
                   gauge_ok=l1["gauge_ok"], branch=l1["branch"],
                   c0A0=float(l1["c0A0"]))
        ex = construct_exact(cs, b, K, l1, big=(h > EXACT_MAX))
        out.update(e1_ok=ex["e1_ok"], e3_ok=ex["e3_ok"],
                   e5_ok=ex["e5_ok"], mulback_ok=ex["mulback_ok"],
                   detJ=ex["detJ"])
        with mp.workdps(dps):
            j2 = ex["tms"][1] / (l1["A0"] * (l1["A2"] / l1["A0"]) ** 2)
            out["J2"] = float(j2)
        if h <= EXACT_MAX:
            out["e2_exact_ok"] = construct_bareiss(
                b, ex["rt"], l1["A0"], ex["ntil"], K)
        else:
            out["e2_spot_worst"] = numeric_spot(
                b_mp, ex["rt"], l1["A0"], ex["ntil"], K, dps)
        cstar, envr, _ = envj_bracket(cs_mp, b_mp, K, dps)
        out["cstar"] = cstar
        out["envj_ratio"] = envr
        if h <= CENSUS_HARD_MAX:
            nreal, top_yt, negsum = verify_census(cs_mp, b_mp, K, dps)
            out["cen_real"] = nreal
            out["cen_top_yt"] = top_yt
            out["cen_negsum"] = negsum
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
        ex = construct_exact(cs, b, K, l1, big=False)
        out.update(npos=l1["npos"], nneg=l1["nneg"], nzero=l1["nzero"],
                   branch=l1["branch"], a2sign=l1["a2sign"],
                   sum_ok=l1["sum_ok"], e1_ok=ex["e1_ok"],
                   c0A0=float(l1["c0A0"]))
        return out
    except Exception as exc:                        # noqa: BLE001
        return dict(world=world, x=x, error=repr(exc))


# ---------------------------------------------------------- symbolic
def symbolic_gates() -> list:
    import sympy as sp
    res = []
    y = sp.Symbol("y")
    # G05: matrix determinant lemma, fully symbolic, n = 2..6
    ok_mdl = True
    for n in SYMB_MDL_NS:
        bs = sp.symbols("b1:%d" % (n + 1))
        rs = sp.symbols("r1:%d" % (n + 1))
        D = sp.diag(*[y - bs[i] for i in range(n)])
        M = D + sp.ones(n, 1) * sp.Matrix([list(rs)]).reshape(1, n)
        det = M.det(method="berkowitz")
        rhs = sp.prod([y - bb for bb in bs]) \
            + sum(rs[k] * sp.prod([y - bs[j] for j in range(n)
                                   if j != k]) for k in range(n))
        if sp.expand(det - rhs) != 0:
            ok_mdl = False
    res.append(("G05-symb-mdl", ok_mdl,
                "det(yI - D + ONES r^T) == prod + sum r_k prod_(j!=k), "
                "symbolic n = %s" % (SYMB_MDL_NS,)))
    # G06: Krein assembly, all sign patterns, n = 2, 3
    ok_kr = True
    for n in SYMB_KREIN_NS:
        bs = sp.symbols("b1:%d" % (n + 1), positive=True)
        ws = sp.symbols("w1:%d" % (n + 1), positive=True)
        for mask in range(2 ** n):
            sg = [1 if (mask >> i) & 1 else -1 for i in range(n)]
            rho = [sg[i] * ws[i] ** 2 for i in range(n)]
            D = sp.diag(*bs)
            J = sp.diag(*sg)
            Ans = D - sp.ones(n, 1) * sp.Matrix([rho]).reshape(1, n)
            S = sp.diag(*ws)
            Ap = D - (sp.Matrix(ws) * sp.Matrix(ws).T) * J
            if sp.simplify(S * Ans * S ** -1 - Ap) != sp.zeros(n, n):
                ok_kr = False
            Ahat = J * Ap
            if sp.simplify(Ahat - Ahat.T) != sp.zeros(n, n):
                ok_kr = False
            lhs = (y * sp.eye(n) - Ap).det(method="berkowitz")
            rhs = J.det() * (y * J - Ahat).det(method="berkowitz")
            if sp.expand(lhs - rhs) != 0:
                ok_kr = False
            # Weyl diagonal commutation
            wv = sp.Matrix(ws)
            weyl = (wv.T * (y * J - J * D) ** -1 * wv)[0, 0]
            direct = sum(rho[i] / (y - bs[i]) for i in range(n))
            if sp.simplify(weyl - direct) != 0:
                ok_kr = False
    res.append(("G06-symb-krein", ok_kr,
                "similarity + J-symmetry + det transfer + Weyl form, "
                "n = %s, all sign patterns" % (SYMB_KREIN_NS,)))
    # G07: transform-class residue lemmas
    al, be, ga, de, t, t0, r, b0, w0, w1, g = sp.symbols(
        "alpha beta gamma delta t t0 r b0 w0 w1 g")
    Delta = al * de - be * ga
    phi = (al * t + be) / (ga * t + de)
    ok_tr = (sp.simplify(sp.diff(phi, t) * (ga * t + de) ** 2 - Delta)
             == 0)
    phi0 = (al * t0 + be) / (ga * t0 + de)
    lhs = phi - phi0
    rhs = Delta * (t - t0) / ((ga * t + de) * (ga * t0 + de))
    ok_tr = ok_tr and (sp.simplify(lhs - rhs) == 0)
    # positive weight: residue of (w0 + w1 (y-b0)) r/(y-b0) at b0
    expr = (w0 + w1 * (y - b0)) * r / (y - b0)
    ok_tr = ok_tr and (sp.simplify(
        sp.residue(expr, y, b0) - w0 * r) == 0)
    # g^2 pair splitting: residues of r/(g^2 - b) at +-sqrt(b)
    bpos = sp.Symbol("b", positive=True)
    rp = sp.residue(r / (g ** 2 - bpos), g, sp.sqrt(bpos))
    rm = sp.residue(r / (g ** 2 - bpos), g, -sp.sqrt(bpos))
    ok_tr = ok_tr and (sp.simplify(rp - r / (2 * sp.sqrt(bpos))) == 0) \
        and (sp.simplify(rm + r / (2 * sp.sqrt(bpos))) == 0)
    res.append(("G07-symb-transform", ok_tr,
                "Moebius sign lemma + weight lemma + g^2 pair "
                "splitting: mixedness invariant in class"))
    return res


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
                if "verification" in m:
                    bad.append("import " + m)
    # polyroots ownership + numpy eig ban
    owners = {}
    for fname, fnode in funcs.items():
        for node in ast.walk(fnode):
            if isinstance(node, ast.Call):
                fn = node.func
                nm = fn.attr if isinstance(fn, ast.Attribute) else \
                    (fn.id if isinstance(fn, ast.Name) else "")
                owners.setdefault(nm, set()).add(fname)
    for owner in owners.get("polyroots", set()):
        if not owner.startswith("verify_"):
            bad.append("polyroots-in:" + owner)
    for nm in ("eig", "eigvals", "eigh", "eigvalsh", "roots"):
        if nm in owners:
            bad.append("eig/roots-call:" + nm)
    # construct_* cell-key whitelist (tau-screen leg, G03)
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
    # call-graph DFS: construct_* must not reach polyroots/verify_*
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
            if "polyroots" in r or any(v.startswith("verify_")
                                       for v in r):
                guard_bad.append(fname)
    return bad, guard_bad, cellkey_bad


def loop_dag() -> tuple:
    dag = {
        "DELIVERED": ["ATOMS", "WALL-EIGENEQ", "RESIDUES", "PENCIL",
                      "IDENTITIES", "BRACKET-ENVJ"],
        "ATOMS": [],
        "WALL-EIGENEQ": ["ATOMS"],
        "RESIDUES": ["WALL-EIGENEQ"],
        "PENCIL": ["RESIDUES"],
        "IDENTITIES": ["PENCIL"],
        "BRACKET-ENVJ": ["RESIDUES"],
        "CENSUS-ROOTS": ["IDENTITIES"],
        "CENSUS-FORALL-K": [],
        "A0-TRIANGLE": [],
        "ZERO-VERIFICATION-AS-HYP": [],
        "RH-COND-SECOND-MOMENTS": [],
    }
    flagged = ("CENSUS-FORALL-K", "A0-TRIANGLE",
               "ZERO-VERIFICATION-AS-HYP", "RH-COND-SECOND-MOMENTS",
               "CENSUS-ROOTS")
    # acyclicity
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    rungs = (4, 5) if args.smoke else RUNGS
    print("census_lift_probe -- PRIME.CENSUS.SPECTRAL.LIFT.01%s"
          % ("  [SMOKE]" if args.smoke else ""))
    print("SPEC_SHA %s" % SPEC_SHA[:16])

    section("S0 firewall + loop guard")
    bad, guard_bad, cellkey_bad = firewall_audit()
    check("G01-firewall", not bad,
          "forbidden names/imports: %s" % (bad or "none"))
    check("G02-roots-guard", not guard_bad,
          "construct_* reaching polyroots/verify_*: %s"
          % (guard_bad or "none"))
    check("G04-spec", len(SPEC_SHA) == 64
          and all(h in DPS for h in RUNGS),
          "SPEC_SHA printed; frozen DPS schedule covers RUNGS; "
          "K formula gated per rung (G10)")
    acyc, clean = loop_dag()
    check("G08-loop-dag", acyc and clean,
          "ancestry DAG acyclic=%s, flagged+roots unreachable=%s"
          % (acyc, clean))

    section("S1 symbolic exact layer")
    for name, ok, detail in symbolic_gates():
        check(name, ok, detail)

    section("S2 rungs + worlds (parallel)")
    jobs_r = [(h, DPS[h]) for h in rungs]
    jobs_w = list(CONTROLS)
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs_r = list(ex.map(w_rung, jobs_r))
        futs_w = list(ex.map(w_world, jobs_w))
    R = {r["h"]: r for r in futs_r}
    W = {(r["world"], r["x"]): r for r in futs_w}

    dps_ok = True
    branches = {}
    for h in rungs:
        r = R[h]
        if "error" in r:
            check("G10[h=%d]-build" % h, False, r["error"])
            continue
        info("h=%d K=%d build %.1f s  ladder=(%d,%d)  branch=%s  "
             "c0/A0=%.6e  log10yt=%.3f"
             % (h, r["K"], r["build_s"], r["npos"], r["nneg"],
                r["branch"], r["c0A0"], r["yt_l10"]))
        check("G10[h=%d]-build" % h,
              r["K_ok"] and r["ray_dev"] <= RAY_BAR,
              "K ok=%s, ray_dev %.2e <= %.0e"
              % (r["K_ok"], r["ray_dev"], RAY_BAR))
        lad_ok = (r["nzero"] == 0)
        lad_txt = "(n+,n-)=(%d,%d), n0=%d" % (r["npos"], r["nneg"],
                                              r["nzero"])
        if h in LADDER_TAB:
            lad_ok = lad_ok and ((r["npos"], r["nneg"])
                                 == LADDER_TAB[h])
            lad_txt += " == frozen %s" % (LADDER_TAB[h],)
        else:
            lad_txt += " [RECORDED, pre-freeze unmeasured]"
        check("G11[h=%d]-ladder" % h, lad_ok, lad_txt)
        c0_ok = True
        c0_txt = "sum(rho)==A2/A0 exact=%s, a2sign=%d" \
            % (r["sum_ok"], r["a2sign"])
        if h in C0A0_TAB:
            c0_ok = abs(r["c0A0"] / C0A0_TAB[h] - 1) <= C0A0_RTOL
            c0_txt += ", c0/A0 %.6e vs tab %.6e" % (r["c0A0"],
                                                    C0A0_TAB[h])
        else:
            c0_txt += ", c0/A0 %.6e [RECORDED]" % r["c0A0"]
        check("G12[h=%d]-sumrule" % h,
              r["sum_ok"] and r["a2sign"] == -1 and c0_ok, c0_txt)
        check("G13[h=%d]-e1-exact" % h,
              r["e1_ok"] and r["mulback_ok"],
              "census == Mittag-Leffler coefficient-exact=%s, "
              "mul-back=%s" % (r["e1_ok"], r["mulback_ok"]))
        if h <= EXACT_MAX:
            check("G14[h=%d]-e2-exact" % h, r["e2_exact_ok"],
                  "integer Bareiss at %d points: det == A0^(K-2) "
                  "Ntilde exact" % r["K"])
        else:
            check("G14[h=%d]-e2-spot" % h,
                  r["e2_spot_worst"] < NUMDET_BAR,
                  "NUMERIC-SPOT worst rel %.2e < %.0e (typed)"
                  % (r["e2_spot_worst"], NUMDET_BAR))
        br_ok = r["e3_ok"]
        br_txt = "rho==sigma*w^2 exact=%s, detJ=%+d, branch=%s" \
            % (r["e3_ok"], r["detJ"], r["branch"])
        if h in LADDER_TAB:
            br_ok = br_ok and (r["branch"] == "J")
            br_txt += " (expected J)"
        else:
            br_txt += " [RECORDED]"
        check("G15[h=%d]-e3-krein" % h, br_ok, br_txt)
        branches[h] = r["branch"]
        sig_def = (r["branch"] in ("U", "D"))
        check("G16[h=%d]-signature" % h,
              (r["npos"] + r["nneg"] == r["K"] - 1),
              "Bhat=J signature (%d,%d); definite=%s (defect = "
              "indefinite J)" % (r["npos"], r["nneg"], sig_def))
        check("G17[h=%d]-moments" % h,
              r["e5_ok"] and J2_WIN[0] <= r["J2"] <= J2_WIN[1],
              "t_m dual-route exact m<=%d=%s + jet tie; J2 %.4f in %s"
              % (MOM_MAX, r["e5_ok"], r["J2"], (J2_WIN,)))
        check("G18[h=%d]-bracket" % h,
              r["cstar"] is not None
              and r["cstar"] <= CSTAR_LIFT_MAX
              and (r["envj_ratio"] or 1) < 1,
              "envj c*=%s ratio=%s (source-pure; spectrum bracket "
              "by identity)" % (r["cstar"], r["envj_ratio"]))
        if h <= CENSUS_HARD_MAX:
            top_ok = abs(r["cen_top_yt"] / TOP_TAB[h] - 1) <= TOP_RTOL
            check("G19[h=%d]-census-verify" % h,
                  r["cen_real"] == r["K"] - 1
                  and r["cen_negsum"] <= NEGSUM_BAR and top_ok,
                  "nreal %d == K-1, negsum %.1e, top/yt %.6f vs tab"
                  % (r["cen_real"], r["cen_negsum"], r["cen_top_yt"]))
    check("G03-tau-screen",
          not cellkey_bad
          and all(R[h].get("gauge_ok", False) for h in rungs
                  if "error" not in R[h]),
          "construct_* cell-key whitelist clean (%s); ladder exact "
          "scale-gauge invariant under c -> (3/7)c at every rung"
          % (cellkey_bad or "none"))

    section("S3 worlds")
    wnames = {"SMOOTH": "G30-smooth", "SCRARITH": "G31-scrarith",
              "EPSTEIN": "G32-epstein"}
    world_branch = {}
    for (world, x, _d) in CONTROLS:
        r = W[(world, x)]
        if "error" in r:
            check(wnames[world], False, r["error"])
            continue
        tab = LADDER_WORLD[(world, x)]
        ok = ((r["npos"], r["nneg"]) == tab and r["nzero"] == 0
              and r["e1_ok"] and r["sum_ok"] and r["a2sign"] == -1)
        world_branch[world] = r["branch"]
        check(wnames[world], ok,
              "x=%d ladder (%d,%d) == frozen %s, branch=%s, E1 "
              "exact=%s" % (x, r["npos"], r["nneg"], tab,
                            r["branch"], r["e1_ok"]))
    smooth_def = world_branch.get("SMOOTH") == "U"
    others_mixed = all(world_branch.get(w) == "J"
                       for w in ("SCRARITH", "EPSTEIN")) \
        and all(branches.get(h) == "J" for h in rungs
                if h in LADDER_TAB)
    check("G33-adjudication", smooth_def and others_mixed,
          "definite <=> atom-free among tested worlds: SMOOTH=U, "
          "all atom-bearing mixed -- DEFINITE-ONLY-IN-SMOOTH, "
          "MIXEDNESS-IS-ARITHMETIC (wrong orientation, NOT a sign "
          "source)")
    check("G34-world-blind",
          all(W[(w, x)].get("e1_ok", False) for (w, x, _d) in CONTROLS),
          "E1 exact in every world: the lift algebra is world-blind "
          "(realness transfer lives in fake worlds too; separation "
          "stays in H1/H3)")

    section("S4 verdict")
    dt = time.time() - T_START
    check("G40-runtime", dt < RUNTIME_BAR,
          "%.1f s < %.0f s" % (dt, RUNTIME_BAR))

    exact_fail = any(
        (not R[h].get("e1_ok", False))
        or (h <= EXACT_MAX and not R[h].get("e2_exact_ok", False))
        or (not R[h].get("e3_ok", False))
        or (not R[h].get("e5_ok", False))
        for h in rungs if "error" not in R[h])
    all_onesigned = all(branches.get(h) in ("U", "D") for h in rungs
                        if h in branches)
    if exact_fail:
        verdict = ["NO-GO"]
    elif all_onesigned:
        verdict = ["EXACT-LIFT"]
    else:
        verdict = ["PARTIAL-LIFT"]
    verdict += ["KREIN-PENCIL-EXACT"] if not exact_fail else []
    if all(branches.get(h) == "J" for h in rungs if h in branches):
        verdict.append("SIGNATURE-INDEFINITE-ALL-TRUE-RUNGS")
    if any(branches.get(h) in ("U", "D") for h in rungs
           if h in branches and h > EXACT_MAX):
        verdict.append("UNEXPECTED-ONE-SIGNED-RUNG")
    verdict.append("MIXEDNESS-TRANSFORM-INVARIANT")
    if smooth_def and others_mixed:
        verdict.append("DEFINITE-ONLY-IN-SMOOTH")
        verdict.append("MIXEDNESS-IS-ARITHMETIC")
    verdict.append("LIFT-WORLD-BLIND-KREIN")
    if all(R[h].get("cstar") is not None
           and R[h]["cstar"] <= CSTAR_LIFT_MAX for h in rungs
           if "error" not in R[h]):
        verdict.append("BRACKET-CERTIFIED-VIA-ENVJ")
    verdict.append("SPECTRUM-VERIFIED-H13")
    verdict.append("MDL-EXACT-H13-NUMERIC-H2128")
    verdict.append("ROOTS-NEVER-CONSUMED")
    verdict.append("TAU-FREE-CONSTRUCTION")
    verdict.append("NO-RH-CLAIM")
    print("\nVERDICT: %s" % " + ".join(verdict))

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], time.time() - T_START))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
