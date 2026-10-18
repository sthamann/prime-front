#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v807 -- PRIME.LORENTZ.SPINOR.01 (+ the BOUNDARY.NULLSELECTOR addendum to E8.ONEOBJECT.01): null-cone spinor coordinates for the open near-collinearity problem + the independent d = 4 forcing through the rank-one null condition, ONE module from two probes (22 checks / 3 preregistered-honest FAILs + 14/14 checks, ~2 s; discovery probes lorentz_spinor_coords_probe.py LORENTZ-COORDS-REVEAL and boundary_nullselector_probe.py NULLSELECTOR-ALGEBRAIC, both 2026-08-06).  PART 1, THE EXACT OBSERVATIONS [E neu] (sympy-exact): M(5,-3,4) = [[2,4],[4,8]] = 2 (1,2)^T (1,2) -- the compiler triple (g_car, -N_fam, |mu4|) is a rank-one SPINOR SQUARE with spinor (1,2); the Euclid parametrization sends the measured locking direction (2,-1) to (5,-3,4) EXACTLY, with M(Eu(i,j)) = 2 (j,-i)^T (j,-i) identically (the locking direction IS the spinor square root, orthogonal to the spinor); the permuted null triple (5,-4,3) has spinor (1,3), preimage (3,-1) -- the anchoring is direction-specific.  THE REVEAL: the h-ordered trend gates L3.MON/L3.CAUCHY/L3.CR FAIL honestly (monotone fraction 0.591, Kendall 0.613 -- the frozen h-order bars), but the declared REVEAL clause fires (CR chain CV 0.084 <= 0.10): in the ALPHA-ordered ladder the spinor slope r is STRICTLY MONOTONE -- 66/66 increments positive, Kendall tau 1.000, anchored cross-ratio contraction on 1.000 of rungs (CV 0.004) -- the h-oscillation was the alpha-vs-h jitter of the frame-A scan, NOT noise in r.  HONESTY: the approach 2 - r ~ alpha^-0.23 is GLACIAL; the transversal reserve tau > 0 pointwise but decays h^-1.65 (no uniform floor); the named 1D monotonicity candidate is stated as the NEXT contract, not proven.  PART 2, THE NULL SELECTOR (all exact): |v_d|^2_L = det M(v_d) = d(4-d) identically for the functor vector v_d = (d+1, -(d-1), d) (honest RR/Serre arithmetic g = h^0(P^1, O(d)), N = h^1(O(-d))); null/rank-one iff d = 4, where M_4 is exactly the part-1 spinor square and (1,2) = the anchor support of a = (1,1,2) via FOUR exact identities (i+j = N_fam, ij = |Z2|, i^2+j^2 = g_car, 2ij = |mu4|).  THE BRIDGE to the v781 glue census: g^2 - N^2 = 4d = |H|^2 identically, so NULL <=> glue index = d -- independent inputs (rank-one boundary reading vs discriminant evenness/unimodularity), same invariant 4d, same output {4}.  HONEST DOWNGRADE (measured): the deployed boundary machinery has NO d-dependence to vary -- the first boundary reading is rank one/null UNIVERSALLY (every mode pair, U_1 Loewner theorem, defect 3.9e-16; EDGE content only, bulk lags fail rank one at 7.4e-3), so the missing theorem is typed OPEN: why the boundary reading carries the functor vector of the divisor degree.  Rigidity: all three wrong functor assignments have irrational null points, no integer d in 1..12.  Controls fire in both parts (position scramble x5e5, wrong null vector, 200 random-slope sequences).  No marker move, NO positivity theorem, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes lorentz_spinor_coords_probe.py (2026-08-06, 22 checks with the 3 honest h-order FAILs L3.MON/L3.CAUCHY/L3.CR, ~2 s, LORENTZ-COORDS-REVEAL; the declared post-first-run L3b description and the Q4DET conditioning-bar correction carried verbatim in the original docstring below) + boundary_nullselector_probe.py (2026-08-06, 14/14, ~0.1 s, NULLSELECTOR-ALGEBRAIC); both re-run identically at promotion.  Promoted verbatim, part 2 wrapped in a function scope (v789/v795 precedent; the wrap indents part 2's multiline print literals by four spaces -- cosmetic, numbers unchanged; the shared N_CHK/FAILS counters are module-global and reset by each part, part-1 results captured before part 2 runs); module-level _LAST1/_LAST2 verdict captures inserted (v791 precedent); the v563/tfpt_constants imports resolve against the verification directory (the probes' own path loop finds it unchanged); numbers unchanged; run() encodes both patterns incl. the expected part-1 fails (v757 precedent).

Original lorentz_spinor_coords_probe.py docstring (verbatim):
PRIME.LORENTZ.SPINOR.01 -- the null-cone coordinate change for the
open near-collinearity problem (EXPLORATION ONLY, experiments/).

THE NEW EXACT OBSERVATIONS to verify first [E neu]:
  with M(t,x,y) = [[t+x, y],[y, t-x]]  (det = t^2 - x^2 - y^2):
  (1) M(5,-3,4) = [[2,4],[4,8]] = 2 (1,2)^T (1,2) -- the boundary null
      vector (g_car, -N_fam, |mu4|) is a RANK-ONE SPINOR SQUARE with
      spinor (1,2);
  (2) the Euclid parametrization (i,j) |-> (i^2+j^2, -(i^2-j^2), -2ij)
      sends the measured locking direction (2,-1) to exactly (5,-3,4):
      the locking direction IS the spinor square root of the compiler
      vector (M(Eu(i,j)) = 2 (j,-i)^T (j,-i) identically; (j,-i) at
      (2,-1) is (-1,-2) ~ (1,2), orthogonal to (2,-1)).

CORPUS ANCHORS (read-only, cited):
  * T170-TH4 (bilinear_sieve / tfpt_prime_front): the determinant
    polarisation on 2x2 symmetric blocks is the rank-3 form
    [[0,1,0],[1,0,0],[0,0,-2]], signature (1,2) -- Lorentz geometry.
  * v576 C3.1: the leading modes-(1,2) profile [[1,2],[2,4]] has
    Lorentz image L(X) = (X11+X22, X11-X22, 2 X12) = (5,-3,4), the
    Pythagorean triple of (g_car, N_fam, |mu4|), typed COMPRESSION.
  * v586: the pencil locking direction drifts (v2/v1 from -1.73 at
    h = 184 to -1.22 at h = 1445), 1/log h limit -0.551, consistent
    with the (2,-1) null ray (slope -1/2), NOT settled; h = 1292
    anomalous by declaration.
  * v563 build_window / frame_a_zones: the deployed frame-A ladder
    with the near-collinear lock block Ahat = B - S (onem = det/
    (a11 a22) ~ h^-3, T166/T170 -- the NON-UNIFORM raw matrix margin).

THE PROGRAMME (frozen): reparametrize the near-collinear 2x2 blocks
projectively, Ahat = lambda (1,r)^T (1,r)/(1+r^2) + tau P_perp
(eigendecomposition; lambda = lambda_max, r = dominant spinor slope,
tau = lambda_min = transversal energy), plus the Lorentz vector
u = (a11+a22, a11-a22, 2 a12) with Q(u) = t^2-x^2-y^2 = 4 det Ahat
and the projective null-cone distance delta_null = Q/(t^2+x^2+y^2),
and the anchored cross-ratio chain
    q_k = CR(r_k, r_{k+1}; 2, -1/2) = [g(r_{k+1})/g(r_k)],
    g(r) = (r - 2)/(r + 1/2)   (Moebius: boundary spinor slope 2 -> 0,
                                its orthogonal -1/2 -> infinity),
the projective contraction factor per rung.

THE QUESTION (the decider): does the coordinate change turn the
non-uniform matrix estimates into a ONE-DIMENSIONAL monotone
projective quantity?  Measured (frozen, oscillation-aware):
  (a) is r(h) monotone/Cauchy where the raw margins (onem, det) were
      not uniform?
  (b) does the transversal energy tau stay positive on every regular
      rung (the reserve), and what is its decay class?
  (c) does the cross-ratio chain show a stable law (contraction
      q_k < 1 per rung / constant)?

FROZEN BARS AND ENUMS (declared before any number):
  E-part: all integer/symbolic identities EXACT (sympy simplify == 0).
  Q4DET: Q(u) == 4 det Ahat per rung -- the identity is SYMBOLIC
         (E1.1); the float check uses the v692-style conditioning bar
         100 eps (t^2+x^2+y^2)/|4 det| (cancellation-limited quantity)
  BAR_EIG    = 1e-9   rel: eigen-reconstruction residual per rung
  MON_BAR    = 0.90   fraction of increments of r with the majority sign
  KEN_BAR    = 0.80   |Kendall tau| of r vs h
  CAUCHY_BAR = 0.50   range(second half of r) / range(all r)
  FIT_R2     = 0.50   R^2 of the 1/log h fit (v586 convention)
  RHO_TOL    = 0.20   |rho_inf + 1/2| for the null-slope fit (v586 bar)
  R_TOL      = 0.80   |r_inf - 2| for the spinor-slope fit (declared
                      wide: r = -1/rho is nonlinear in the fit variable)
  CR_FRAC    = 0.85   fraction of rungs with strict contraction q_k < 1
  BAR_SCR    = 5.0    scramble must-break factor on |onem| (corpus x49)
  N_RAND     = 200    random-slope control sequences (frozen seed)
  RAND_PCT   = 95     real monotone fraction must exceed this percentile
  Anomalous h = 1292 excluded by declaration (v586); incomplete combs
  (X > ATOM_MAX) flagged and excluded from the trend statistics.

VERDICT ENUM (frozen):
  LORENTZ-COORDS-IMPROVE  -- (a) monotone AND Cauchy AND 1/log h fit
      lands on the spinor axis (rho_inf ~ -1/2 or r_inf ~ 2), (b) tau
      positive on all regular rungs, (c) q_k < 1 on >= CR_FRAC of the
      chain, and all three controls fire.  The named next analytic
      step becomes a 1D monotonicity statement (stated in L5).
  LORENTZ-COORDS-NEUTRAL  -- no improvement: the coordinate change is
      typed decorative.
  LORENTZ-COORDS-REVEAL   -- not IMPROVE, but the new coordinates
      expose a different clean structure (declared: |r - 2| decreasing
      on >= 0.85 of rungs while r itself non-monotone, OR the CR chain
      constant at CV <= 0.10 while monotonicity fails) -- described
      exactly.

HONESTY: this is a COORDINATE-CHANGE DIAGNOSTIC, not a positivity
theorem.  The corpus already states the exact null direction stands
while the measured approach rate (1/log h, v586) misses the success
threshold (v581 transport killed).  The probe decides only whether
the projective coordinates improve the uniformity picture.  NO RH
claim.  Both outcomes are typed.

L3b (POST-FIRST-RUN DESCRIPTION, declared as such -- radical honesty):
the first frozen run (2026-08-06, h-ordered ladder) returned
LORENTZ-COORDS-REVEAL via the declared CV clause (monotone fraction
0.591 / Kendall 0.613 in h-order; anchored-CR CV 0.084 <= 0.10).  Its
per-rung table showed the revealed structure: r appears STRICTLY
MONOTONE in the window width alpha -- the h-order oscillation is the
alpha-vs-h jitter of the frame-A scan.  L3b measures exactly that
(same bars MON_BAR/KEN_BAR/CAUCHY_BAR/CR_FRAC applied to the
alpha-ordered ladder, plus 1/alpha and power-law fits of 2 - r and
the log-linear onem law in alpha).  L3b is the REQUIRED description
of the REVEAL enum, NOT a preregistered discovery, and it does NOT
change the frozen h-order verdict.  Also post-first-run: the Q4DET
float bar was corrected from a mis-specified fixed 1e-9 to the
conditioning-aware bar above (first run measured worst rel 2.1e-9,
exactly the eps ||u||^2 / 4 det cancellation floor; the identity
itself is symbolic).

FIREWALL: v563/v586-machinery imported/reproduced READ-ONLY; no zeta
zero is read anywhere (AST-checked); deterministic (RNG only in the
declared random-slope control, frozen seed); no file outside
experiments/ is touched; no marker moves; the ledger is untouched.

Original boundary_nullselector_probe.py docstring (verbatim):
BOUNDARY.NULLSELECTOR.01 -- the independent d = 4 forcing through
the rank-one null condition (EXPLORATION ONLY, experiments/).

Follow-up to PRIME.LORENTZ.SPINOR.01 (lorentz_spinor_coords_probe.py,
2026-08-06, LORENTZ-COORDS-REVEAL): there the compiler triple
(g_car, -N_fam, |mu4|) = (5,-3,4) was certified as the rank-one spinor
square M(5,-3,4) = 2 (1,2)^T (1,2), with Euclid sending the measured
locking direction (2,-1) to it exactly.

THE CLAIM CHAIN (frozen): for divisor degree d the canonical functors
give
    g    = d + 1   ( = h^0(P^1, O(d)),  Riemann-Roch ),
    N    = d - 1   ( = h^1(P^1, O(-d)) = h^0(O(d-2)), Serre ),
    glue = d,
so the Lorentz vector v_d = (d+1, -(d-1), d) has
    |v_d|^2_L = (d+1)^2 - (d-1)^2 - d^2 = 4d - d^2 = d(4 - d):
v_d is NULL iff d = 4 (for positive d), where v_4 = (5,-3,4) and
    M_d = M(v_d) = [[2, d],[d, 2d]],   det M_d = d(4 - d),
with the rank-one square root at d = 4 being exactly the anchor
content (1,2): M_4 = 2 (1,2)^T (1,2).

CORPUS ANCHORS (read-only, cited):
  * v23_anchor_generator / origin_theory ~L121: the anchor a = (1,1,2)
    is the unique 3-multiset with elementary symmetric functions
    (e1, e2, e3) = (|mu4|, g_car, |Z2|) = (4, 5, 2);
    chi_a(t) = (t-1)^2 (t-2).
  * v499_p2_weights_deligne_bg / p2_weights_bg_deligne_probe: the
    RR/Deligne reading chi(O(d)) = d+1, anchor degree -e1 = -4,
    h^1 discrepancy resolved via h^1(O(-a_i)) = a_i - 1.
  * v576_cheb_loewner_edge C2/C3 (+ tfpt_prime_front T182): the edge
    read w^(ij)_{N-s} is a scaled Loewner matrix of U_{s-1} (rank <=
    s-1; the FIRST boundary reading s = 2 is rank one BY THEOREM);
    the leading modes-(1,2) profile is [[1,2],[2,4]] with Lorentz
    image (5,-3,4) -- typed COMPRESSION.
  * lorentz_spinor_coords_probe E1 (parent, 2026-08-06): the spinor-
    square identities M(5,-3,4) = 2(1,2)^T(1,2), Euclid (2,-1) |->
    (5,-3,4), all sympy-exact.
  * v781_one_object_clock_census (E8.ONEOBJECT.01): THE GLUE CENSUS --
    an even unimodular DIAGONAL glue of A_{d-1} (+) D_{d+1} exists
    iff d = 4 (census d = 2..12, exact Fraction arithmetic); controls:
    dropping evenness opens d = 9, dropping unimodularity opens
    {7, 8, 9, 12}; coarse square layer |H|^2 = 4d passes {4, 9} only.

SLICES (bars and enums declared BEFORE any number):

S1 [THE EXACT ALGEBRA, E neu -- all sympy-exact]:
  S1.1  |v_d|^2_L = d(4-d) symbolically; det M(v_d) = d(4-d) (via the
        parent identity det M(t,x,y) = t^2-x^2-y^2).
  S1.2  d-table d = 1..12: norm, signature type (d < 4 TIMELIKE > 0,
        d = 4 NULL, d > 4 SPACELIKE < 0) -- exact integers.
  S1.3  rank census of M_d, d = 1..12: rank M_d = 2 iff det != 0;
        rank 1 EXACTLY at d = 4, with the factorization
        M_4 = 2 (1,2)^T (1,2) exact.
  S1.4  the functor content is honest cohomology arithmetic:
        h^0(P^1, O(d)) = d+1 and h^1(P^1, O(-d)) = h^0(O(d-2)) = d-1
        (Serre), checked as exact integer functions for d = 1..12.
  S1.5  anchor identification: a = (1,1,2), e_k(a) = (4,5,2) =
        (|mu4|, g_car, |Z2|) (tfpt_constants + v23 convention);
        the spinor (i,j) = (1,2) is the SUPPORT (distinct values) of
        the anchor multiset, and EXACTLY: i*j = e3 = |Z2| = 2,
        i+j = 3 = N_fam, i^2+j^2 = e2 = g_car = 5, 2ij = e1 = |mu4|
        = 4; chi_a(t) = t^3 - e1 t^2 + e2 t - e3.

S2 [THE SEAM-FAMILY QUESTION -- honest feasibility]:
  (a) citations: where (5,-3,4) appears in the boundary analysis
      (v576 C3.1, T182, parent probe E1) -- printed.
  (b) THE FEASIBILITY MEASUREMENT (decides the downgrade): in the
      deployed Chebyshev/comb boundary machinery the free parameters
      are (mode pair (i,j), edge depth s, window h) -- NONE is the
      divisor degree d.  The candidate d-family "rank/null defect of
      the first boundary reading of a d-mark seam" is HONESTLY
      VARIABLE only if the first reading's null defect actually
      varies over the accessible family.  Measured census:
      S2.NULL  the s = 2 edge block for EVERY mode pair (i,j),
               i < j <= 4, at h in {300, 800}: Lorentz null defect
               |Q|/(t^2+x^2+y^2) <= BAR_NULL = 1e-10 and sv2/sv1 <=
               BAR_RANK1 = 1e-12 (v576 C2.2 bar) -- rank one / null
               UNIVERSALLY (by the U_1 Loewner theorem), for every
               pair, not only (1,2).
      S2.SPIN  the spinor slope of the s = 2 block is sin(w_j)/
               sin(w_i) = j/i (1 + O(w^2)): dev <= BAR_SLOPE = 0.02.
      S2.SCEN  the s-census: s = 2, 3, 4 give rank 1, 2, 3
               (sv_{rank+1}/sv_1 <= BAR_RANK1) -- only the FIRST
               reading is rank one.
      S2.CTRL  [must-break] bulk-lag control: the same 2x2 block read
               at interior lags (N/3, N/2, 2N/3) is NOT rank one
               (sv2/sv1 >= BAR_BULK = 1e-3) -- the reading is EDGE
               content, not construction.
      DECISION RULE (frozen): if S2.NULL passes (null defect < 1e-10
      for ALL pairs), the boundary rank-one/null condition is
      UNIVERSAL in the accessible parameters -- a d-indexed rank test
      would pass vacuously for every d, i.e. the deployed
      construction has NO honest d-dependence to vary, and the probe
      DOWNGRADES to the algebraic selector only (the enum
      NULLSELECTOR-FAMILY-TESTED is then unreachable by declaration).
      The missing theorem is typed exactly: WHY the first boundary
      reading's spinor is the anchor content (1,2) -- equivalently
      why the boundary Lorentz image is the functor vector v_d --
      which then forces d(4-d) = 0.

S3 [RELATION TO THE GLUE CENSUS, exact + cited]:
  S3.1  the shared invariant, symbolically: g^2 - N^2 = (d+1)^2 -
        (d-1)^2 = 4d = |disc A_{d-1}| * |disc D_{d+1}| = |H|^2
        (unimodularity budget), so
          null condition   <=>  4d = d^2  <=>  |H| = d  <=>
          glue index = d ( = |mu4| at the fixed point).
  S3.2  the square layer {d in 1..12 : 4d a perfect square} = {1,4,9};
        the null layer = {4}; v781's evenness/isotropy layer kills
        d = 9 (and d = 1 has no A_0/D_2 glue content: |H|^2 = 4 needs
        H in Z1 x (Z2)^2... d = 1 is degenerate, A_0 trivial --
        stated, not recomputed).  CITED, not recomputed: v781 census
        numbers (2 diagonal glues at d = 4; controls open d = 9 resp.
        {7,8,9,12}).
  S3.3  what each mechanism assumes (printed comparison table).

S4 [CONTROLS]:
  S4.1  wrong functor assignments break the null identity: for
        (g, N) in {(d+2, d-1), (d+1, d-2), (d+2, d)} the norm has NO
        integer root in d = 1..12 and its real roots are irrational
        (symbolic discriminant check) -- no null selection anywhere.
  S4.2  the null condition FAILS for every d != 4 in 1..12 (S1.2).
  S4.3  the edge-location control S2.CTRL (bulk lags not rank one).

VERDICT ENUM (frozen):
  NULLSELECTOR-ALGEBRAIC     -- exact algebra certified (S1), seam-
      family theorem typed OPEN with the honest scope statement (S2
      decision rule fired: no honest d-variation exists), controls ok.
  NULLSELECTOR-FAMILY-TESTED -- a d-family was honestly variable and
      selects 4 (unreachable if S2.NULL shows universality).
  NULLSELECTOR-DEAD          -- the algebra fails, a d != 4 is null,
      or a must-break control does not fire.

HONESTY: the null selector is EXACT ALGEBRA on the functor vector; it
does NOT prove that the boundary must carry the functor vector -- that
is the typed-open seam-family theorem.  The glue census (v781) is the
independent arithmetic forcing; this probe only states the precise
relation.  NO new derivation of P1/P2 is claimed or implied.  NO RH
claim.  Nothing outside experiments/ is touched; no marker moves.

FIREWALL: v563 imported READ-ONLY (parity/weight machinery only); no
zeta zero is read anywhere (AST-checked); deterministic, no RNG; the
ledger is untouched.
"""

_LAST1 = {}
_LAST2 = {}

import ast
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core     # noqa: E402  (READ-ONLY)
import tfpt_constants as tc             # noqa: E402  (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
Q4_COND_FAC = 100.0           # v692-style conditioning factor on eps
BAR_EIG = 1.0e-9
MON_BAR = 0.90
KEN_BAR = 0.80
CAUCHY_BAR = 0.50
FIT_R2 = 0.50
RHO_TOL = 0.20
R_TOL = 0.80
CR_FRAC = 0.85
CR_CONST_CV = 0.10
REVEAL_FRAC = 0.85
BAR_SCR = 5.0
N_RAND = 200
RAND_PCT = 95
SEED_RAND = 20260806          # frozen; used ONLY in the random control
SCR_SEEDS = (1, 2, 3)         # v586 D5.1 scramble seeds, verbatim
ANOMALOUS_H = 1292            # v586 declaration
ABS_MU4 = 4                   # |mu4| = |Z/4| (v576 C3.1 / tfpt_1 convention)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                    "zetazero", "nzeros", "second_sheet_zero", "find_zeros"):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros",
                                                    "find_zeros"):
                hits.append(f.id)
    return not hits


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    tot = n * (n - 1) // 2
    return (conc - disc) / max(tot, 1)


def fit_invlog(h, y):
    """y = y_inf + b / log h  (v586 D4.1 convention): (y_inf, b, R^2)."""
    h = np.asarray(h, float)
    y = np.asarray(y, float)
    A = np.column_stack([1.0 / np.log(h), np.ones(len(h))])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    r2 = 1.0 - float((resid ** 2).sum()) \
        / max(float(((y - y.mean()) ** 2).sum()), 1e-300)
    return float(coef[1]), float(coef[0]), r2


def ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def moebius_g(r):
    """g(r) = (r - 2)/(r + 1/2): boundary spinor slope 2 -> 0, its
    orthogonal (the null-ray slope) -1/2 -> infinity."""
    return (r - 2.0) / (r + 0.5)


def spinor_coords(Ah):
    """Projective spinor coordinates of one 2x2 symmetric block."""
    w, V = np.linalg.eigh(Ah)                   # w[0] <= w[1]
    lam, tau = float(w[1]), float(w[0])
    v = V[:, 1].copy()
    if v[0] < 0:
        v = -v
    r = float(v[1] / v[0])
    t = float(Ah[0, 0] + Ah[1, 1])
    x = float(Ah[0, 0] - Ah[1, 1])
    y = float(2.0 * Ah[0, 1])
    Q = t * t - x * x - y * y
    dnull = Q / (t * t + x * x + y * y)
    return dict(lam=lam, tau=tau, r=r, rho=-1.0 / r if r != 0 else
                float("inf"), t=t, x=x, y=y, Q=Q, dnull=dnull)


def _run_part1():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.LORENTZ.SPINOR.01 -- null-cone coordinates for the "
          "near-collinearity (lorentz_spinor_coords_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zeta-zero loader in this module (zetazero/nzeros/"
          "find_zeros absent); zeros are NOT an input of this probe",
          ast_zero_firewall(__file__))

    # ============================================================== E1
    print("\nE1 -- THE NEW EXACT OBSERVATIONS [E neu] (sympy, exact)")
    t_, x_, y_, i_, j_ = sp.symbols("t x y i j", real=True)
    a_, b_, c_ = sp.symbols("a b c", real=True)
    Msym = sp.Matrix([[t_ + x_, y_], [y_, t_ - x_]])
    detM = sp.simplify(Msym.det() - (t_**2 - x_**2 - y_**2))
    q4id = sp.simplify((a_ + c_)**2 - (a_ - c_)**2 - (2 * b_)**2
                       - 4 * (a_ * c_ - b_**2))
    check("E1.1 [E neu] det M(t,x,y) = t^2 - x^2 - y^2 IDENTICALLY for "
          "M = [[t+x, y],[y, t-x]] (residual %s), and inversely "
          "Q(L(A)) = (a+c)^2 - (a-c)^2 - (2b)^2 = 4 det A IDENTICALLY "
          "(residual %s) -- the T170-TH4 signature-(1,2) form IS the "
          "determinant in these coordinates" % (detM, q4id),
          detM == 0 and q4id == 0)

    M534 = Msym.subs({t_: 5, x_: -3, y_: 4})
    spin = sp.Matrix([1, 2])
    dev = sp.simplify(M534 - 2 * spin * spin.T)
    check("E1.2 [E neu] M(5,-3,4) = [[2,4],[4,8]] = 2 (1,2)^T (1,2) "
          "EXACTLY: rank one (det = %s), trace 10 -- the boundary null "
          "vector is a RANK-ONE SPINOR SQUARE with spinor (1,2)"
          % sp.simplify(M534.det()),
          dev == sp.zeros(2, 2) and sp.simplify(M534.det()) == 0
          and M534[0, 0] == 2 and M534[0, 1] == 4 and M534[1, 1] == 8)

    Eu = (i_**2 + j_**2, -(i_**2 - j_**2), -2 * i_ * j_)
    Eu_null = sp.simplify(Eu[0]**2 - Eu[1]**2 - Eu[2]**2)
    Eu21 = tuple(e.subs({i_: 2, j_: -1}) for e in Eu)
    check("E1.3 [E neu] the Euclid parametrization (i,j) |-> (i^2+j^2, "
          "-(i^2-j^2), -2ij) is null IDENTICALLY (residual %s) and "
          "sends the measured locking direction (2,-1) to %s = (5,-3,4) "
          "EXACTLY" % (Eu_null, Eu21),
          Eu_null == 0 and Eu21 == (5, -3, 4))

    MEu = Msym.subs({t_: Eu[0], x_: Eu[1], y_: Eu[2]})
    spin_ij = sp.Matrix([j_, -i_])
    dev_ij = sp.simplify(MEu - 2 * spin_ij * spin_ij.T)
    s21 = spin_ij.subs({i_: 2, j_: -1})           # (-1, -2) ~ (1, 2)
    ortho = 2 * 1 + (-1) * 2                      # (2,-1) . (1,2)
    check("E1.4 [E neu] the SPINOR-SQUARE IDENTITY: M(Eu(i,j)) = "
          "2 (j,-i)^T (j,-i) for ALL (i,j) (residual %s); at (2,-1) the "
          "spinor is %s ~ (1,2) -- the locking direction IS the spinor "
          "square root of the compiler vector, and (2,-1) . (1,2) = %d "
          "(the null ray is EXACTLY orthogonal to the spinor)"
          % (dev_ij, tuple(s21), ortho),
          dev_ij == sp.zeros(2, 2) and tuple(s21) == (-1, -2)
          and ortho == 0)

    X12 = sp.Matrix([[1, 2], [2, 4]])
    Lmap = (X12[0, 0] + X12[1, 1], X12[0, 0] - X12[1, 1], 2 * X12[0, 1])
    LM = tuple(sp.simplify(e) for e in
               (Msym[0, 0] + Msym[1, 1], Msym[0, 0] - Msym[1, 1],
                2 * Msym[0, 1]))
    anchor = (int(tc.g_car), -int(tc.N_fam), ABS_MU4)
    check("E1.5 [E, corpus anchor] conventions agree: the v576 C3.1 "
          "Lorentz map L(X) = (X11+X22, X11-X22, 2 X12) gives "
          "L([[1,2],[2,4]]) = %s and L(M(t,x,y)) = %s = 2 (t,x,y); the "
          "compiler triple (g_car, -N_fam, |mu4|) = %s = (5,-3,4) with "
          "g_car, N_fam from tfpt_constants (5^2 - 3^2 - 4^2 = 0)"
          % (Lmap, LM, anchor),
          Lmap == (5, -3, 4) and LM == (2 * t_, 2 * x_, 2 * y_)
          and anchor == (5, -3, 4)
          and 5 ** 2 - 3 ** 2 - 4 ** 2 == 0)

    M543 = Msym.subs({t_: 5, x_: -4, y_: 3})
    w543, V543 = np.linalg.eigh(np.array(M543.tolist(), float))
    v543 = V543[:, 1] / V543[0, 1]
    check("E1.6 [must-break, wrong null vector] (5,-4,3) is also null "
          "(M(5,-4,3) = [[1,3],[3,9]], det = %s) BUT its spinor is "
          "(1, %.0f) != (1,2): the Euclid preimage is (3,-1), NOT the "
          "measured locking direction (2,-1), and its second entry 4 "
          "!= N_fam = %d -- the spinor-square anchoring BREAKS for the "
          "permuted triple exactly as it must"
          % (sp.simplify(M543.det()), v543[1], int(tc.N_fam)),
          sp.simplify(M543.det()) == 0 and abs(v543[1] - 3.0) < 1e-12
          and int(tc.N_fam) == 3)

    # ============================================================== L2
    print("\nL2 -- the ladder extraction (deployed frame-A windows, "
          "v563 read-only)")
    zones = core.frame_a_zones()
    rows, anom, incomplete = [], [], []
    q4_worst = eig_worst = 0.0
    for kz in zones:
        rr = core.build_window(kz)
        Ah = rr["Ah"]
        sc = spinor_coords(Ah)
        # exact identity Q(u) = 4 det Ahat (symbolic, E1.1); float dev
        # measured against the conditioning bar of the cancellation
        q4dev = abs(sc["Q"] - 4.0 * rr["det"]) \
            / max(abs(4.0 * rr["det"]), 1e-300)
        q4bar = Q4_COND_FAC * np.finfo(float).eps \
            * (sc["t"]**2 + sc["x"]**2 + sc["y"]**2) \
            / max(abs(4.0 * rr["det"]), 1e-300)
        q4 = q4dev / max(q4bar, 1e-300)
        # eigen-reconstruction residual
        v1 = np.array([1.0, sc["r"]])
        v1 /= np.linalg.norm(v1)
        v2 = np.array([-v1[1], v1[0]])
        rec = sc["lam"] * np.outer(v1, v1) + sc["tau"] * np.outer(v2, v2)
        er = float(np.max(np.abs(rec - Ah))) / max(
            float(np.max(np.abs(Ah))), 1e-300)
        complete = math.exp(2.0 * rr["alpha"]) <= core.ATOM_MAX + 0.5
        row = dict(kz=kz, h=rr["h"], alpha=rr["alpha"],
                   a11=rr["a11"], a22=rr["a22"], a12=rr["a12"],
                   det=rr["det"], onem=rr["onem"], complete=complete,
                   dir_raw=rr["a12"] / rr["a11"], **sc)
        if rr["h"] == ANOMALOUS_H:
            anom.append(row)
            continue
        if not complete:
            incomplete.append(row)
            continue
        q4_worst = max(q4_worst, q4)
        eig_worst = max(eig_worst, er)
        rows.append(row)
    rows.sort(key=lambda w: w["h"])
    check("L2.SET the deployed ladder: %d regular complete windows "
          "(h = %d..%d), %d anomalous (h = %d, v586 declaration), %d "
          "incomplete-comb (excluded from trends, listed)"
          % (len(rows), rows[0]["h"], rows[-1]["h"], len(anom),
             ANOMALOUS_H, len(incomplete)),
          len(rows) >= 30)
    check("L2.Q4D the Lorentz norm IS the margin: Q(u) = t^2-x^2-y^2 = "
          "4 det Ahat per rung (symbolic identity E1.1; float dev "
          "within %.3f of the conditioning bar %d eps ||u||^2/|4 det| "
          "on every rung -- cancellation-limited, as declared)"
          % (q4_worst, int(Q4_COND_FAC)), q4_worst <= 1.0)
    check("L2.EIG the projective reparametrization Ahat = lambda "
          "P_(1,r) + tau P_perp is exact per rung (worst eigen-"
          "reconstruction residual %.1e <= %.0e)"
          % (eig_worst, BAR_EIG), eig_worst <= BAR_EIG)

    print("\n    per-rung table (regular complete ladder):")
    print("    %5s %7s | %10s %10s %8s %8s | %10s %10s | %10s %8s"
          % ("h", "alpha", "lambda", "tau", "r", "rho", "dnull",
             "onem", "det", "q_k"))
    rs = [w["r"] for w in rows]
    gs = [moebius_g(r) for r in rs]
    qs = [gs[k + 1] / gs[k] for k in range(len(gs) - 1)]
    for k, w in enumerate(rows):
        print("    %5d %7.3f | %10.3e %10.3e %8.4f %8.4f | %10.3e "
              "%10.3e | %10.3e %8s"
              % (w["h"], w["alpha"], w["lam"], w["tau"], w["r"],
                 w["rho"], w["dnull"], w["onem"], w["det"],
                 ("%8.4f" % qs[k]) if k < len(qs) else "--"))
    for w in anom + incomplete:
        print("    %5d %7.3f | %10.3e %10.3e %8.4f %8.4f | %10.3e "
              "%10.3e | %10.3e %8s   <-- %s"
              % (w["h"], w["alpha"], w["lam"], w["tau"], w["r"],
                 w["rho"], w["dnull"], w["onem"], w["det"], "--",
                 "ANOMALOUS (excluded)" if w["h"] == ANOMALOUS_H
                 else "incomplete comb (excluded)"))

    # corpus anchoring of the extracted coordinates
    dir_dev = max(abs(w["dir_raw"] - w["r"]) for w in rows)
    ang = [math.degrees(math.acos(min(1.0, abs(
        (np.array([1.0, w["rho"]]) / np.linalg.norm([1.0, w["rho"]]))
        @ (np.array([2.0, -1.0]) / math.sqrt(5.0)))))) for w in rows]
    check("L2.ANCH corpus anchoring: near rank-one the raw direction "
          "a12/a11 equals the spinor slope r (max dev %.2e); the null "
          "slope rho = -1/r sits %.1f..%.1f deg from the exact (2,-1) "
          "ray (median %.1f; v577 measured 23.5..33.8 on its surface) "
          "-- same objects, same regime"
          % (dir_dev, min(ang), max(ang), float(np.median(ang))),
          dir_dev < 0.05)

    # ============================================================== L3
    print("\nL3 -- frozen oscillation-aware trend statistics")
    hs = [w["h"] for w in rows]
    dr = np.diff(rs)
    nz = dr[dr != 0.0]
    mon_frac = max(float((nz > 0).mean()), float((nz < 0).mean())) \
        if len(nz) else 0.0
    ktau = kendall_tau(hs, rs)
    half = len(rs) // 2
    rng_full = max(rs) - min(rs)
    rng_half = max(rs[half:]) - min(rs[half:])
    cauchy = rng_half / max(rng_full, 1e-300)
    # Aitken Delta^2 limit census (descriptive)
    aik = []
    for k in range(len(rs) - 2):
        d1, d2 = rs[k + 1] - rs[k], rs[k + 2] - rs[k + 1]
        den = d2 - d1
        if abs(den) > 1e-12:
            aik.append(rs[k + 2] - d2 * d2 / den)
    aik = np.array(aik)
    r_inf, r_b, r_r2 = fit_invlog(hs, rs)
    rhos = [w["rho"] for w in rows]
    rho_inf, rho_b, rho_r2 = fit_invlog(hs, rhos)
    print("    r: min %.4f max %.4f; increments: %d up / %d down; "
          "Aitken limit census median %.3f (IQR %.3f..%.3f, %d pts)"
          % (min(rs), max(rs), int((nz > 0).sum()), int((nz < 0).sum()),
             float(np.median(aik)), float(np.percentile(aik, 25)),
             float(np.percentile(aik, 75)), len(aik)))
    print("    1/log h fits: r_inf = %.3f (b = %.2f, R^2 = %.3f); "
          "rho_inf = %.3f (b = %.2f, R^2 = %.3f)  [v586 quote: -0.551]"
          % (r_inf, r_b, r_r2, rho_inf, rho_b, rho_r2))
    mono_ok = mon_frac >= MON_BAR and abs(ktau) >= KEN_BAR
    cauchy_ok = cauchy <= CAUCHY_BAR
    fit_ok = (rho_r2 >= FIT_R2 and abs(rho_inf + 0.5) <= RHO_TOL) \
        or (r_r2 >= FIT_R2 and abs(r_inf - 2.0) <= R_TOL)
    check("L3.MON (a) MONOTONE: the spinor slope r moves with majority-"
          "sign fraction %.3f (bar %.2f) and Kendall tau %.3f vs h "
          "(bar %.2f) across %d rungs -- %s"
          % (mon_frac, MON_BAR, ktau, KEN_BAR, len(rs),
             "a 1D monotone projective quantity" if mono_ok
             else "NOT monotone at the declared bars"), mono_ok)
    check("L3.CAUCHY (a) CAUCHY/settling: the second-half range of r "
          "is %.3f of the full range (bar <= %.2f); Aitken census "
          "median %.3f" % (cauchy, CAUCHY_BAR, float(np.median(aik))),
          cauchy_ok)
    check("L3.FIT (a) the 1/log h extrapolation lands on the spinor "
          "axis: rho_inf = %.3f vs -1/2 (tol %.2f, R^2 %.3f) / r_inf "
          "= %.3f vs 2 (tol %.2f, R^2 %.3f) -- v586's drift law seen "
          "in the block's OWN eigencoordinates"
          % (rho_inf, RHO_TOL, rho_r2, r_inf, R_TOL, r_r2), fit_ok)

    # comparator: the raw matrix margins (the non-uniform side)
    e_onem, _, r2_onem = ols_loglog(hs, [w["onem"] for w in rows])
    e_det, _, r2_det = ols_loglog(hs, [abs(w["det"]) for w in rows])
    e_dn, _, r2_dn = ols_loglog(hs, [abs(w["dnull"]) for w in rows])
    onems = [w["onem"] for w in rows]
    check("L3.RAW the raw-margin comparator: onem ~ h^%.2f (R^2 %.2f, "
          "max/min = %.1e -- NO uniform floor), det ~ h^%.2f (R^2 "
          "%.2f); the null-cone distance dnull ~ h^%.2f is the SAME "
          "vanishing object (Q = 4 det) -- while r stays in the "
          "bounded interval [%.3f, %.3f]: the coordinate change "
          "separates the bounded projective coordinate from the "
          "vanishing radial one"
          % (e_onem, r2_onem, max(onems) / min(onems), e_det, r2_det,
             e_dn, min(rs), max(rs)), r2_onem > 0.5)

    # (b) the transversal reserve
    taus = [w["tau"] for w in rows]
    tau_pos = all(tt > 0.0 for tt in taus)
    e_tau, _, r2_tau = ols_loglog(hs, taus)
    e_rat, _, r2_rat = ols_loglog(hs, [w["tau"] / w["lam"] for w in rows])
    check("L3.TAU (b) the transversal energy tau = lambda_min is "
          "POSITIVE on all %d regular rungs (min %.3e) -- the reserve "
          "exists pointwise; honest decay class: tau ~ h^%.2f (R^2 "
          "%.2f), tau/lambda ~ h^%.2f (R^2 %.2f) -- %s"
          % (len(rows), min(taus), e_tau, r2_tau, e_rat, r2_rat,
             "NO uniform positive floor (the reserve vanishes along "
             "the ladder; positivity per rung only)" if e_tau < -0.5
             else "bounded"), tau_pos)

    # (c) the cross-ratio chain
    qs_arr = np.array(qs)
    contr_frac = float((qs_arr < 1.0).mean())
    cv_q = float(np.std(qs_arr) / abs(np.mean(qs_arr)))
    tot_contr = float(np.prod(qs_arr))
    cr_ok = contr_frac >= CR_FRAC
    check("L3.CR (c) the anchored cross-ratio chain q_k = CR(r_k, "
          "r_{k+1}; 2, -1/2): strict contraction q_k < 1 on %.3f of "
          "%d rungs (bar %.2f), median %.4f, CV %.3f, total "
          "contraction prod q = %.3f -- %s"
          % (contr_frac, len(qs), CR_FRAC, float(np.median(qs_arr)),
             cv_q, tot_contr,
             "a stable per-rung projective contraction law" if cr_ok
             else "no stable contraction law"), cr_ok)

    # ============================================================== L3b
    print("\nL3b -- the revealed structure, described exactly "
          "(POST-FIRST-RUN description of the REVEAL enum, declared "
          "in the header; same bars, ladder re-parametrized by alpha)")
    arows = sorted(rows, key=lambda w: w["alpha"])
    aas = [w["alpha"] for w in arows]
    ras = [w["r"] for w in arows]
    dra = np.diff(ras)
    nza = dra[dra != 0.0]
    mon_a = max(float((nza > 0).mean()), float((nza < 0).mean())) \
        if len(nza) else 0.0
    n_strict = int((dra > 0).sum())
    ktau_a = kendall_tau(aas, ras)
    halfa = len(ras) // 2
    cauchy_a = (max(ras[halfa:]) - min(ras[halfa:])) \
        / max(max(ras) - min(ras), 1e-300)
    ga = moebius_g(np.array(ras))
    qa = ga[1:] / ga[:-1]
    contr_a = float((qa < 1.0).mean())
    cv_qa = float(np.std(qa) / abs(np.mean(qa)))
    # fits in alpha: r = r_inf + b/alpha; power law 2 - r ~ alpha^s;
    # onem log-linear in alpha
    Aa = np.column_stack([1.0 / np.asarray(aas), np.ones(len(aas))])
    coefa, *_ = np.linalg.lstsq(Aa, np.asarray(ras), rcond=None)
    resa = np.asarray(ras) - Aa @ coefa
    r2_inva = 1.0 - float((resa ** 2).sum()) \
        / float(((np.asarray(ras) - np.mean(ras)) ** 2).sum())
    r_inf_a, b_a = float(coefa[1]), float(coefa[0])
    s_pow, c_pow, r2_pow = ols_loglog(aas, [2.0 - r for r in ras])
    lo_fit = np.polyfit(aas, np.log([w["onem"] for w in arows]), 1)
    lo_pred = np.polyval(lo_fit, aas)
    lo_y = np.log([w["onem"] for w in arows])
    r2_lo = 1.0 - float(((lo_y - lo_pred) ** 2).sum()) \
        / float(((lo_y - lo_y.mean()) ** 2).sum())
    check("L3b.MON [MEASURED, the revealed 1D structure] in the "
          "alpha-ordered ladder the spinor slope r is monotone: "
          "%d/%d increments strictly positive (majority fraction "
          "%.3f, bar %.2f), Kendall tau %.3f vs alpha (bar %.2f) -- "
          "the h-order oscillation of L3.MON is the alpha-vs-h jitter "
          "of the frame-A scan, NOT noise in r"
          % (n_strict, len(dra), mon_a, MON_BAR, ktau_a, KEN_BAR),
          mon_a >= MON_BAR and abs(ktau_a) >= KEN_BAR)
    check("L3b.CR [MEASURED] the anchored cross-ratio chain in alpha "
          "order contracts on %.3f of %d rungs (bar %.2f; median q "
          "%.4f, CV %.3f): the per-rung projective contraction law "
          "the h-order chain missed"
          % (contr_a, len(qa), CR_FRAC, float(np.median(qa)), cv_qa),
          contr_a >= CR_FRAC)
    print("    Cauchy (alpha order): second-half range / full range = "
          "%.3f (h-order was %.3f; the settling is toward the LARGE-"
          "alpha end, approach still slow)" % (cauchy_a, cauchy))
    print("    fits in alpha: r = %.3f %+.3f/alpha (R^2 %.3f); "
          "2 - r ~ %.3f alpha^%.3f (R^2 %.3f); onem ~ %.2e "
          "exp(%.3f alpha) (R^2 %.3f)"
          % (r_inf_a, b_a, r2_inva, c_pow, s_pow, r2_pow,
             math.exp(lo_fit[1]), lo_fit[0], r2_lo))
    print("    HONESTY: the approach 2 - r is GLACIAL (power ~ "
          "alpha^%.2f; the 1/alpha extrapolant %.3f does NOT reach 2 "
          "on this surface) -- the monotone 1D structure exists, the "
          "rate question stays open exactly as the corpus states"
          % (s_pow, r_inf_a))

    # ============================================================== L4
    print("\nL4 -- controls")
    # C1: scramble destroys the rank-one dominance
    kz_mid = rows[len(rows) // 2]["kz"]
    scr_fac, scr_rat = [], []
    w_real = next(w for w in rows if w["kz"] == kz_mid)
    for sd in SCR_SEEDS:
        rr_s = core.build_window(kz_mid, scramble_seed=sd)
        sc_s = spinor_coords(rr_s["Ah"])
        scr_fac.append(abs(rr_s["onem"]) / abs(w_real["onem"]))
        scr_rat.append(abs(sc_s["tau"] / sc_s["lam"])
                       / abs(w_real["tau"] / w_real["lam"]))
    check("L4.C1 [must-break] the position scramble destroys the "
          "rank-one dominance at h = %d: |onem| moves by x%.1f..x%.1f "
          "(bar >= %.0f) and the eccentricity tau/lambda by "
          "x%.1f..x%.1f -- the near-collinearity is REAL placement "
          "content, not a coordinate artifact"
          % (w_real["h"], min(scr_fac), max(scr_fac), BAR_SCR,
             min(scr_rat), max(scr_rat)), min(scr_fac) >= BAR_SCR)
    # C2: the wrong null vector fails the ladder anchoring too
    d2 = abs(float(np.median(aik)) - 2.0)
    d3 = abs(float(np.median(aik)) - 3.0)
    check("L4.C2 [must-break] wrong null vector (5,-4,3): its spinor "
          "slope is 3 (E1.6); the measured ladder extrapolant (Aitken "
          "median %.3f, 1/log h r_inf %.3f) is closer to the TRUE "
          "spinor slope 2 than to 3 (|.-2| = %.3f < |.-3| = %.3f and "
          "|r_inf-2| = %.3f < |r_inf-3| = %.3f)"
          % (float(np.median(aik)), r_inf, d2, d3,
             abs(r_inf - 2.0), abs(r_inf - 3.0)),
          d2 < d3 and abs(r_inf - 2.0) < abs(r_inf - 3.0))
    # C3: random slopes show no cross-ratio law / no monotonicity
    rng = np.random.default_rng(SEED_RAND)
    mon_rand, contr_rand = [], []
    for _ in range(N_RAND):
        rr_seq = rng.uniform(min(rs), max(rs), size=len(rs))
        d = np.diff(rr_seq)
        d = d[d != 0.0]
        mon_rand.append(max(float((d > 0).mean()),
                            float((d < 0).mean())) if len(d) else 0.0)
        gg = moebius_g(rr_seq)
        qq = gg[1:] / gg[:-1]
        contr_rand.append(float((qq < 1.0).mean()))
    mon_p = float(np.percentile(mon_rand, RAND_PCT))
    con_p = float(np.percentile(contr_rand, RAND_PCT))
    check("L4.C3 [must-break] random slopes (N = %d, frozen seed %d, "
          "same range/length): monotone fraction %dth pct = %.3f and "
          "contraction fraction %dth pct = %.3f -- the real h-order "
          "ladder (%.3f / %.3f) exceeds both, and the alpha-order "
          "ladder (%.3f / %.3f) exceeds them massively: the observed "
          "law is not a property of arbitrary slope sequences"
          % (N_RAND, SEED_RAND, RAND_PCT, mon_p, RAND_PCT, con_p,
             mon_frac, contr_frac, mon_a, contr_a),
          mon_frac > mon_p and contr_frac > con_p
          and mon_a > mon_p and contr_a > con_p)

    # ============================================================== L5
    print("\n" + "=" * 78)
    print("L5 -- VERDICT + recommended contract text (chat report is "
          "the deliverable; nothing outside experiments/ is touched)")
    print("=" * 78)
    controls_ok = (min(scr_fac) >= BAR_SCR and d2 < d3
                   and mon_frac > mon_p and contr_frac > con_p)
    improve = (mono_ok and cauchy_ok and fit_ok and tau_pos and cr_ok
               and controls_ok)
    # REVEAL structure (declared): |r - 2| decreasing while r itself
    # non-monotone, or CR chain constant while monotonicity fails
    dabs = np.diff(np.abs(np.array(rs) - 2.0))
    dec_frac = float((dabs[dabs != 0.0] < 0).mean()) if len(dabs) else 0.0
    reveal = (not improve) and (
        (dec_frac >= REVEAL_FRAC and not mono_ok)
        or (cv_q <= CR_CONST_CV and not mono_ok))
    if improve:
        verdict = "LORENTZ-COORDS-IMPROVE"
    elif reveal:
        verdict = "LORENTZ-COORDS-REVEAL"
    else:
        verdict = "LORENTZ-COORDS-NEUTRAL"
    _LAST1["verdict"] = verdict
    print("""
  VERDICT: %s

  EXACT PART [E neu] (E1, all sympy-exact):
    * M(5,-3,4) = 2 (1,2)^T (1,2) -- the compiler triple
      (g_car, -N_fam, |mu4|) is a rank-one SPINOR SQUARE, spinor (1,2).
    * Euclid (2,-1) |-> (5,-3,4) exactly; M(Eu(i,j)) = 2 (j,-i)^T (j,-i)
      identically: the locking direction IS the spinor square root of
      the compiler vector, orthogonal to the (1,2) spinor.
    * The permuted triple (5,-4,3) is null too but its spinor is (1,3),
      preimage (3,-1) != (2,-1): the anchoring is direction-specific.

  MEASURED PART (L2/L3, %d regular rungs h = %d..%d):
    * monotone fraction %.3f, Kendall tau %.3f, Cauchy %.3f;
      1/log h: rho_inf = %.3f (R^2 %.3f), r_inf = %.3f (R^2 %.3f).
    * reserve: tau > 0 on all rungs (min %.2e), decay class h^%.2f --
      pointwise positive, NOT uniformly bounded below.
    * cross-ratio chain: contraction on %.3f of rungs, median q %.4f,
      CV %.3f, total contraction %.3f.
    * raw comparator: onem ~ h^%.2f, det ~ h^%.2f, dnull ~ h^%.2f
      (all vanishing, no uniform floor); dnull = Q/(t^2+x^2+y^2) with
      Q = 4 det EXACT -- the radial coordinate is the old margin.

  HONESTY: coordinate-change diagnostic only.  The exact null
  direction stands; the approach rate along the ladder remains the
  v586 1/log h drift, which misses the previously declared transport
  bar (v581) -- NO positivity theorem, NO RH claim.
""" % (verdict, len(rows), rows[0]["h"], rows[-1]["h"], mon_frac,
       ktau, cauchy, rho_inf, rho_r2, r_inf, r_r2, min(taus), e_tau,
       contr_frac, float(np.median(qs_arr)), cv_q, tot_contr,
       e_onem, e_det, e_dn))
    if improve or reveal:
        print("""  THE REVEALED STRUCTURE (exact description, L3b): the spinor
  slope r is a MONOTONE FUNCTION OF THE WINDOW WIDTH alpha
  (%d/%d strict increments, Kendall tau %.3f, anchored-CR
  contraction on %.3f of alpha-rungs) -- the h-ordered oscillation
  was the alpha-vs-h jitter of the frame-A scan.  The named 1D
  candidate statement (NOT proven, NOT preregistered -- next
  probe's contract): the dominant-eigenvector slope r(alpha) of the
  lock block Ahat is strictly increasing in alpha with the Moebius
  coordinate g(r) = (r-2)/(r+1/2) contracting per rung (equiv.: the
  null slope rho = -1/r increases toward -1/2 along alpha); the
  measured approach is glacial (2 - r ~ alpha^%.2f) -- the rate,
  i.e. WHETHER the limit is reached, remains the open problem the
  corpus already names."""
              % (n_strict, len(dra), ktau_a, contr_a, s_pow))

    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


def _run_part2():
    """Part 2: boundary_nullselector_probe.py, promoted verbatim in a function scope (v789/v795 precedent)."""
    import ast
    import math
    import os
    import sys
    import time

    import numpy as np
    import sympy as sp

    _here = os.path.dirname(os.path.abspath(__file__))
    for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
        if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
            sys.path.insert(0, os.path.abspath(_cand))
            break

    import v563_paper2_readouts as core     # noqa: E402  (READ-ONLY)
    import tfpt_constants as tc             # noqa: E402  (READ-ONLY)

    T0 = time.time()
    FAILS = []
    N_CHK = 0

    # ------------------------------------------------- frozen bars / constants
    D_RANGE = range(1, 13)        # the d-table
    BAR_RANK1 = 1.0e-12           # v576 C2.2 sv-ratio bar
    BAR_NULL = 1.0e-10            # Lorentz null defect of the s=2 block
    BAR_SLOPE = 0.02              # spinor slope vs j/i at h >= 300
    BAR_BULK = 1.0e-3             # bulk-lag control must EXCEED this
    H_SET = (300, 800)            # declared windows (v576 C1.2 convention)
    PAIRS = ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4))
    ABS_MU4 = 4                   # |mu4| (v576 C3.1 / tfpt_1 convention)
    ABS_Z2 = 2                    # |Z2| = e3(a) (v23 convention)


    def check(name, ok, detail=""):
        global N_CHK
        N_CHK += 1
        if not ok:
            FAILS.append(name.split()[0])
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (": " + detail) if detail else ""))


    def ast_zero_firewall(src_path):
        with open(src_path, "r", encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
        hits = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                f = node.func
                if isinstance(f, ast.Attribute) and f.attr in (
                        "zetazero", "nzeros", "second_sheet_zero", "find_zeros"):
                    hits.append(f.attr)
                if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros",
                                                        "find_zeros"):
                    hits.append(f.id)
        return not hits


    def M_of(t, x, y):
        return sp.Matrix([[t + x, y], [y, t - x]])


    def cross_weights_numeric(h, i, j):
        """The v576 polarized cross weights, verbatim recipe (v563 core)."""
        Tb = core.parity_basis(h, max(i, j))
        if i == j:
            return core.lag_weights_from_v(Tb[i - 1].copy(), h)
        W11 = core.lag_weights_from_v(Tb[i - 1].copy(), h)
        W22 = core.lag_weights_from_v(Tb[j - 1].copy(), h)
        Wpp = core.lag_weights_from_v(Tb[i - 1] + Tb[j - 1], h)
        return 0.5 * (Wpp - W11 - W22)


    def null_defect(B):
        """Projective Lorentz null defect of a 2x2 symmetric block."""
        t = B[0, 0] + B[1, 1]
        x = B[0, 0] - B[1, 1]
        y = 2.0 * B[0, 1]
        return abs(t * t - x * x - y * y) / (t * t + x * x + y * y)


    def run():
        global N_CHK, FAILS
        N_CHK = 0
        FAILS = []
        print("=" * 78)
        print("BOUNDARY.NULLSELECTOR.01 -- the independent d = 4 forcing "
              "through the rank-one null condition")
        print("=" * 78)

        # ============================================================== S0
        print("\nS0 -- firewall")
        check("S0.AST no zeta-zero loader in this module (zetazero/nzeros/"
              "find_zeros absent); zeros are NOT an input of this probe",
              ast_zero_firewall(__file__))

        # ============================================================== S1
        print("\nS1 -- THE EXACT ALGEBRA [E neu] (sympy, exact)")
        d_ = sp.Symbol("d", positive=True)
        g_, N_, gl_ = d_ + 1, d_ - 1, d_
        norm = sp.expand(g_**2 - N_**2 - gl_**2)
        Md_sym = M_of(g_, -N_, gl_)
        detMd = sp.expand(Md_sym.det())
        check("S1.1 [E neu] |v_d|^2_L = (d+1)^2 - (d-1)^2 - d^2 = %s = "
              "d(4-d) IDENTICALLY, and M(v_d) = [[2, d],[d, 2d]] "
              "(entries %s) with det M_d = %s = the same d(4-d) -- the "
              "null condition and the rank-one condition are ONE equation"
              % (norm, tuple(Md_sym), detMd),
              sp.simplify(norm - d_ * (4 - d_)) == 0
              and sp.simplify(detMd - d_ * (4 - d_)) == 0
              and Md_sym[0, 0] == 2 and Md_sym[0, 1] == d_
              and Md_sym[1, 1] == 2 * d_)

        print("\n    the d-table (exact integers):")
        print("    %3s %6s %6s %6s | %8s %10s | %6s %6s"
              % ("d", "g=d+1", "N=d-1", "glue", "|v|^2_L", "type",
                 "detM_d", "rankM"))
        tab_ok = True
        null_set = []
        for d in D_RANGE:
            nm = (d + 1)**2 - (d - 1)**2 - d**2
            Md = sp.Matrix([[2, d], [d, 2 * d]])
            dM = int(Md.det())
            rk = Md.rank()
            typ = ("TIMELIKE" if nm > 0 else
                   ("NULL" if nm == 0 else "SPACELIKE"))
            if nm == 0:
                null_set.append(d)
            expect_typ = ("TIMELIKE" if d < 4 else
                          ("NULL" if d == 4 else "SPACELIKE"))
            expect_rk = 1 if d == 4 else 2
            tab_ok = tab_ok and nm == d * (4 - d) and dM == nm \
                and typ == expect_typ and rk == expect_rk
            print("    %3d %6d %6d %6d | %8d %10s | %6d %6d"
                  % (d, d + 1, d - 1, d, nm, typ, dM, rk))
        check("S1.2 the d-table is exact: |v_d|^2 = d(4-d) with d < 4 "
              "TIMELIKE, d = 4 NULL, d > 4 SPACELIKE on d = 1..12; the "
              "null set is %s = {4} EXACTLY" % null_set,
              tab_ok and null_set == [4])

        M4 = sp.Matrix([[2, 4], [4, 8]])
        spin = sp.Matrix([1, 2])
        fac = sp.simplify(M4 - 2 * spin * spin.T)
        check("S1.3 rank census: rank M_d = 2 for every d in 1..12 except "
              "d = 4 (rank 1, det = 0), where the factorization M_4 = "
              "2 (1,2)^T (1,2) is exact (residual %s) -- the rank-one "
              "square root at the null point is EXACTLY the parent "
              "probe's certified spinor square" % fac,
              fac == sp.zeros(2, 2))

        def h0_P1(deg):
            return deg + 1 if deg >= 0 else 0

        def h1_P1(deg):                     # Serre: h^1(O(k)) = h^0(O(-k-2))
            return h0_P1(-deg - 2)

        coh_ok = all(h0_P1(d) == d + 1 and h1_P1(-d) == d - 1
                     for d in D_RANGE)
        check("S1.4 the functor content is honest cohomology arithmetic: "
              "g = h^0(P^1, O(d)) = d+1 (RR) and N = h^1(P^1, O(-d)) = "
              "h^0(O(d-2)) = d-1 (Serre) as exact integer functions on "
              "d = 1..12; at d = 4: (g, N) = (5, 3) = (g_car, N_fam) -- "
              "the v499/Deligne reading (chi(O(d)) = d+1, anchor degree "
              "-4, h^1(O(-a_i)) = a_i - 1)",
              coh_ok and h0_P1(4) == int(tc.g_car)
              and h1_P1(-4) == int(tc.N_fam))

        a_anchor = (1, 1, 2)
        e1 = sum(a_anchor)
        e2 = (a_anchor[0] * a_anchor[1] + a_anchor[0] * a_anchor[2]
              + a_anchor[1] * a_anchor[2])
        e3 = a_anchor[0] * a_anchor[1] * a_anchor[2]
        i_s, j_s = 1, 2                      # the spinor = anchor support
        t_ = sp.Symbol("t")
        chi_a = sp.expand((t_ - 1)**2 * (t_ - 2))
        chi_ref = t_**3 - e1 * t_**2 + e2 * t_ - e3
        check("S1.5 anchor identification: a = (1,1,2) has e_k(a) = "
              "(%d, %d, %d) = (|mu4|, g_car, |Z2|) (v23/origin_theory "
              "convention; chi_a = (t-1)^2(t-2) = %s); the spinor (1,2) "
              "is the SUPPORT (distinct values) of the anchor multiset, "
              "and EXACTLY: i+j = %d = N_fam, i*j = %d = e3 = |Z2|, "
              "i^2+j^2 = %d = e2 = g_car, 2ij = %d = e1 = |mu4| -- "
              "'(1,2) is the nontrivial anchor content' is these four "
              "exact identities"
              % (e1, e2, e3, chi_a, i_s + j_s, i_s * j_s,
                 i_s**2 + j_s**2, 2 * i_s * j_s),
              (e1, e2, e3) == (ABS_MU4, int(tc.g_car), ABS_Z2)
              and sp.simplify(chi_a - chi_ref) == 0
              and sorted(set(a_anchor)) == [1, 2]
              and i_s + j_s == int(tc.N_fam)
              and i_s * j_s == ABS_Z2
              and i_s**2 + j_s**2 == int(tc.g_car)
              and 2 * i_s * j_s == ABS_MU4)

        # ============================================================== S2
        print("\nS2 -- THE SEAM-FAMILY QUESTION (honest feasibility)")
        print("""    (a) where (5,-3,4) appears in the boundary analysis (citations):
          * v576_cheb_loewner_edge.py C2.1/C2.2: the edge read
            w^(ij)_{N-s} = -(2/N) sin wi sin wj U_{s-1}[x_i, x_j] is a
            scaled Loewner matrix of U_{s-1}; rank <= s-1; the FIRST
            boundary reading (s = 2) is rank one BY THEOREM.
          * v576 C3.1 (+ tfpt_prime_front T182 / the 'Pythagorean null
            bridge' item): the leading modes-(1,2) profile [[1,2],[2,4]]
            has Lorentz image (5,-3,4) = (g_car, N_fam, |mu4|)-triple,
            typed COMPRESSION.
          * lorentz_spinor_coords_probe.py E1 (parent, 2026-08-06):
            M(5,-3,4) = 2 (1,2)^T (1,2) and Euclid (2,-1) |-> (5,-3,4),
            sympy-exact; the deployed lock block's spinor slope is
            strictly monotone in alpha toward 2 (REVEAL).""")

        # (b) the feasibility measurement
        nd_worst = 0.0
        r1_worst = 0.0
        sl_worst = 0.0
        for h in H_SET:
            N = 2 * h + 1
            for (i, j) in PAIRS:
                wii = cross_weights_numeric(h, i, i)
                wjj = cross_weights_numeric(h, j, j)
                wij = cross_weights_numeric(h, i, j)
                d_edge = N - 2
                B = np.array([[wii[d_edge], wij[d_edge]],
                              [wij[d_edge], wjj[d_edge]]])
                sv = np.linalg.svd(B, compute_uv=False)
                nd_worst = max(nd_worst, null_defect(B))
                r1_worst = max(r1_worst, sv[1] / sv[0])
                slope = B[0, 1] / B[0, 0]
                sl_worst = max(sl_worst, abs(slope - j / i) / (j / i))
        check("S2.NULL [the decision measurement] the s = 2 (first) "
              "boundary reading is rank one / NULL for EVERY mode pair "
              "(i,j), i < j <= 4, at h in %s: worst Lorentz null defect "
              "%.1e <= %.0e, worst sv2/sv1 %.1e <= %.0e -- the null "
              "condition is UNIVERSAL in the accessible mode parameters "
              "(U_1 is linear, its Loewner matrix is rank one for ANY "
              "pair): it cannot select (1,2), hence cannot select d"
              % (H_SET, nd_worst, BAR_NULL, r1_worst, BAR_RANK1),
              nd_worst <= BAR_NULL and r1_worst <= BAR_RANK1)
        check("S2.SPIN the s = 2 spinor slope is sin(w_j)/sin(w_i) = "
              "j/i (1 + O(w^2)): worst rel dev %.1e <= %.0e -- the "
              "boundary spinor of pair (i,j) is (i,j), so the (1,2) "
              "spinor is selected by WHICH modes are deployed (the two "
              "lowest parity modes = the anchor content), not by the "
              "rank/null condition" % (sl_worst, BAR_SLOPE),
              sl_worst <= BAR_SLOPE)

        h = 300
        N = 2 * h + 1
        Ws = {}
        for i in range(1, 5):
            for j in range(i, 5):
                Ws[(i, j)] = cross_weights_numeric(h, i, j)
        scen_ok = True
        for s_, rk in ((2, 1), (3, 2), (4, 3)):
            d_edge = N - s_
            M4x4 = np.array([[Ws[(min(i, j), max(i, j))][d_edge]
                              for j in range(1, 5)] for i in range(1, 5)])
            sv = np.linalg.svd(M4x4, compute_uv=False)
            if sv[rk] / sv[0] > BAR_RANK1:
                scen_ok = False
        check("S2.SCEN the s-census (v576 C2.2 reproduced): the edge "
              "reads at s = 2, 3, 4 have rank 1, 2, 3 (sv_{r+1}/sv_1 <= "
              "%.0e) -- ONLY the first reading is rank one; the natural "
              "depth family s has rank s-1, not a d = 4 selection"
              % BAR_RANK1, scen_ok)

        bulk_min = float("inf")
        for d_lag in (N // 3, N // 2, 2 * N // 3):
            B = np.array([[Ws[(1, 1)][d_lag], Ws[(1, 2)][d_lag]],
                          [Ws[(1, 2)][d_lag], Ws[(2, 2)][d_lag]]])
            sv = np.linalg.svd(B, compute_uv=False)
            bulk_min = min(bulk_min, sv[1] / sv[0])
        check("S2.CTRL [must-break] bulk-lag control: the same (1,2) "
              "block read at interior lags N/3, N/2, 2N/3 is NOT rank "
              "one (min sv2/sv1 = %.2e >= %.0e) -- the rank-one/null "
              "reading is EDGE content (the boundary), not a property of "
              "the construction at arbitrary lags" % (bulk_min, BAR_BULK),
              bulk_min >= BAR_BULK)

        family_variable = not (nd_worst <= BAR_NULL)   # frozen decision rule
        print("""
        FEASIBILITY DECISION (frozen rule): the deployed construction's
        free parameters are (mode pair, edge depth s, window h) -- none
        is the divisor degree d.  S2.NULL measured the null condition as
        UNIVERSAL over the accessible family%s: a d-indexed rank/null
        test would pass vacuously for every d.  The d-family CANNOT be
        honestly varied inside the deployed boundary machinery; the probe
        DOWNGRADES to the algebraic selector.  THE MISSING THEOREM, typed
        exactly: why the first boundary reading's spinor must be the
        anchor content (1,2) -- equivalently, why the boundary Lorentz
        image must be the functor vector v_d = (d+1, -(d-1), d) of the
        SAME d as the divisor degree -- which then forces d(4-d) = 0,
        i.e. d = 4.  The rank-one/null condition is the LINK, the functor
        identification is the open premise.""" % (
            "" if not family_variable else " -- UNEXPECTED: it varied"))

        # ============================================================== S3
        print("\nS3 -- relation to the glue census (v781, E8.ONEOBJECT.01)")
        discA = d_                       # |disc A_{d-1}| = d
        discD = sp.Integer(4)            # |disc D_{d+1}| = 4 (order; d>=2)
        shared = sp.simplify(g_**2 - N_**2 - discA * discD)
        check("S3.1 [E] the SHARED INVARIANT: g^2 - N^2 = (d+1)^2 - "
              "(d-1)^2 = 4d = |disc A_{d-1}| x |disc D_{d+1}| = |H|^2 "
              "(the v781 unimodularity budget; residual %s) -- hence "
              "NULL <=> 4d = d^2 <=> |H| = d <=> glue index = d: the "
              "null selector says the glue index EQUALS the divisor "
              "degree, which holds iff d = 4 (= |mu4|)" % shared,
              shared == 0 and int(math.isqrt(4 * 4)) == 4)
        sq_layer = [d for d in D_RANGE
                    if math.isqrt(4 * d) ** 2 == 4 * d]
        check("S3.2 the layers on d = 1..12: square layer {d : 4d a "
              "perfect square} = %s; the NULL layer = %s = {4} is "
              "STRICTLY finer; v781's independent evenness/isotropy "
              "layer kills d = 9 (cited: disc(D_10) q-values obstruction)"
              " and d = 1 is degenerate (A_0 trivial) -- both mechanisms "
              "land on {4}" % (sq_layer, null_set),
              sq_layer == [1, 4, 9] and null_set == [4])
        print("""    S3.3 what each mechanism assumes (the comparison):
          GLUE CENSUS (v781, verified arithmetic, cited):
            input:  the lattices A_{d-1} (+) D_{d+1} and the TFPT glue
                    pattern -- isotropic glue group, EVENNESS (q = 0 mod
                    2Z), UNIMODULARITY (|H|^2 = 4d);
            output: an even unimodular diagonal glue exists iff d = 4
                    (controls: no evenness -> d = 9 opens; no
                    unimodularity -> {7,8,9,12} open).
          NULL SELECTOR (this probe, exact algebra):
            input:  the functor assignment (g, N, glue) = (d+1, d-1, d)
                    (RR/Serre on P^1, S1.4) and the requirement that the
                    seam block M(v_d) = [[g-N, glue],[glue, g+N]] be
                    RANK ONE (= the boundary reading is a spinor square,
                    the certified d = 4 content);
            output: d(4-d) = 0, i.e. d = 4 among positive d.
          INDEPENDENCE: the glue census never uses the rank-one boundary
          reading; the null selector never uses discriminant-form
          evenness/isotropy.  SHARED: both compare 4d (= |H|^2 = g^2-N^2)
          against d^2 -- the glue census as an integrality/evenness
          constraint on sqrt(4d), the null selector as the equation
          4d = d^2.
          A JOINT STATEMENT would read: 'for the one boundary object of
          degree d, the seam data (A_{d-1}, D_{d+1}, H) is even-
          unimodularly gluable AND the functor vector (h^0, -h^1, d) is
          null iff d = 4; both conditions express |H| = d = glue index,
          reinforced independently by evenness (kills 9) and by the
          rank-one boundary reading (kills all non-squares).'  The
          missing premise for a THEOREM is S2's typed-open seam-family
          statement.""")

        # ============================================================== S4
        print("\nS4 -- controls")
        ctrl_ok = True
        detail = []
        for (gg, nn, lab) in ((d_ + 2, d_ - 1, "g = d+2"),
                              (d_ + 1, d_ - 2, "N = d-2"),
                              (d_ + 2, d_, "g = d+2, N = d")):
            nrm = sp.expand(gg**2 - nn**2 - d_**2)
            roots = sp.solve(sp.Eq(nrm, 0), d_)
            int_hits = [d for d in D_RANGE
                        if (gg.subs(d_, d))**2 - (nn.subs(d_, d))**2
                        - d**2 == 0]
            irrat = all(not r.is_rational for r in roots)
            ctrl_ok = ctrl_ok and irrat and not int_hits
            detail.append("%s: norm %s, roots %s, integer hits %s"
                          % (lab, nrm, roots, int_hits))
        check("S4.1 [must-break] wrong functor assignments BREAK the null "
              "identity -- all three mutations have irrational null "
              "points and NO integer d in 1..12:\n        %s"
              % "\n        ".join(detail), ctrl_ok)
        check("S4.2 [must-break] the null condition fails for EVERY "
              "d != 4 in the table (S1.2 null set = {4}) and the bulk-"
              "lag boundary control fired (S2.CTRL, min sv2/sv1 = %.2e)"
              % bulk_min, null_set == [4] and bulk_min >= BAR_BULK)

        # ============================================================== S5
        print("\n" + "=" * 78)
        print("S5 -- VERDICT + recommended contract text (chat report is "
              "the deliverable; nothing outside experiments/ is touched)")
        print("=" * 78)
        algebra_ok = not any(f.startswith("S1") for f in FAILS)
        controls_ok = not any(f.startswith("S4") for f in FAILS) \
            and bulk_min >= BAR_BULK
        if not algebra_ok or null_set != [4] or not controls_ok:
            verdict = "NULLSELECTOR-DEAD"
        elif family_variable:
            verdict = "NULLSELECTOR-FAMILY-TESTED"
        else:
            verdict = "NULLSELECTOR-ALGEBRAIC"
        _LAST2["verdict"] = verdict
        print("""
      VERDICT: %s

      THE EXACT ALGEBRA (S1, all exact): |v_d|^2_L = det M(v_d) = d(4-d);
      null/rank-one iff d = 4 among positive d; M_4 = 2 (1,2)^T (1,2)
      with (1,2) = the anchor support of a = (1,1,2) (i+j = N_fam,
      ij = |Z2|, i^2+j^2 = g_car, 2ij = |mu4| -- four exact identities);
      the functors are honest RR/Serre arithmetic (g = h^0(O(d)) = d+1,
      N = h^1(O(-d)) = d-1).

      THE SEAM-FAMILY QUESTION (S2, honest): the deployed boundary
      machinery has NO honest d-dependence to vary -- the first boundary
      reading is rank one / null UNIVERSALLY (every mode pair, by the
      U_1 Loewner theorem; measured to %.1e), so the null condition
      cannot select d inside the construction.  The missing theorem is
      typed OPEN: why the boundary reading must carry the functor vector
      v_d of the divisor degree (equivalently why its spinor is the
      anchor content), WHICH THEN forces d = 4.  What IS boundary content
      (measured): the rank-one reading lives at the EDGE only (bulk
      sv2/sv1 >= %.0e fails rank one), and its spinor is (i,j) for the
      deployed mode pair.

      THE GLUE RELATION (S3, exact + cited): g^2 - N^2 = 4d = |H|^2
      identically; NULL <=> |H| = d <=> glue index = divisor degree.
      v781 forces d = 4 via evenness/unimodularity of the discriminant
      glue; the null selector forces d = 4 via 4d = d^2 on the functor
      vector -- independent inputs, same invariant 4d, same output.
    """ % (verdict, nd_worst, BAR_BULK))

        print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
              % (time.time() - T0, N_CHK, len(FAILS),
                 ("  " + ",".join(FAILS)) if FAILS else ""))
        return 0 if not FAILS else 1


    rc = run()
    # the wrapped probe's check() counts via the MODULE-level N_CHK
    # (its own `global` statement) while appending fails to the
    # wrapper-local FAILS -- read both from where they live:
    return rc, globals()["N_CHK"], list(FAILS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 22
    checks with fails EXACTLY [L3.MON, L3.CAUCHY, L3.CR] and verdict
    LORENTZ-COORDS-REVEAL; part 2 must be 14/14
    (NULLSELECTOR-ALGEBRAIC)."""
    rc1 = _run_part1()
    n1, fails1 = N_CHK, sorted(FAILS)
    v1 = _LAST1.get("verdict", "")
    part1_ok = (rc1 == 1 and n1 == 22
                and fails1 == ["L3.CAUCHY", "L3.CR", "L3.MON"]
                and v1 == "LORENTZ-COORDS-REVEAL")
    print("\n[%s] PART-1 PATTERN GATE: expected 22 checks with fails "
          "exactly [L3.MON, L3.CAUCHY, L3.CR] (the honest h-order "
          "gates) and verdict LORENTZ-COORDS-REVEAL; got %d checks, "
          "fails: %s, verdict: %s"
          % ("PASS" if part1_ok else "FAIL", n1, fails1, v1))
    rc2, n2, fails2 = _run_part2()
    v2 = _LAST2.get("verdict", "")
    part2_ok = (rc2 == 0 and n2 == 14 and not fails2
                and v2 == "NULLSELECTOR-ALGEBRAIC")
    print("\n[%s] PART-2 PATTERN GATE: expected 14/14 "
          "(NULLSELECTOR-ALGEBRAIC); got %d checks, fails: %s, "
          "verdict: %s"
          % ("PASS" if part2_ok else "FAIL", n2, fails2 or "none", v2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- LORENTZ-COORDS-REVEAL + "
          "NULLSELECTOR-ALGEBRAIC: the compiler triple (5,-3,4) is a "
          "rank-one spinor square 2(1,2)^T(1,2) with Euclid (2,-1) |-> "
          "(5,-3,4) exact; the spinor slope is strictly monotone in the "
          "window width alpha (66/66, Kendall 1.000, CR contraction CV "
          "0.004) -- the h-oscillation was alpha-jitter, the approach "
          "2 - r ~ alpha^-0.23 stays glacial and the three h-order "
          "gates fail honestly; the null selector |v_d|^2 = d(4-d) "
          "forces d = 4 on the RR/Serre functor vector, shares the "
          "invariant g^2 - N^2 = 4d = |H|^2 with the v781 glue census "
          "(independent mechanisms, same output {4}), and the "
          "seam-family theorem is typed OPEN (the first boundary "
          "reading is rank-one universally -- measured).  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
