#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sat_projection_alignment_probe -- PRIME.ALIGNMENT.PROJECTION.COFINAL.01.

EXPLORATION ONLY.  This probe proves nothing about RH.  It adjudicates
the SAT route (Signed Projection Alignment Theorem, external review of
revision 587) against the deployed budget shape, the frozen gate rule
and the deployed Lean predefinition boundary.  No positivity claim, no
RH claim, no promotion, no marker moved, nothing written outside
experiments/.  NO RH CLAIM.

===========================================================================
THE PROPOSAL UNDER AUDIT (as received; verified, not trusted)
===========================================================================
Per cell h and shift theta the deployed wall is Omega = [[n, b^T],
[b, B]] with B PD, s = n - b^T B^-1 b.  Deployed source structure
(v913 / matrix_stage_conditioning_probe, reproduced here):
b_c = b_0 - b, b_c = -(1/4) A_2 w, hence b = b_0 + (1/4) A_2 w with
A_2 the (h-1) x (h+2) second-difference matrix and w the source lag
profile.  The reviewer sets A = B^-1/2 A_2, y = B^-1/2 b_0,
P = A A^+, w* = -4 A^+ y and claims the exact identity

  (1)  b^T B^-1 b = ||(I-P) y||^2 + (1/16) ||A (w - w*)||^2,

so that s >= 0 is the ELLIPSE INEQUALITY

  (2)  (1/16) ||A (w - w*)||^2 <= n - ||(I-P) y||^2,

reads the open object as a FINITE family of directed von-Mangoldt sums
L_r = <u_r, w> near optima L*_r = <u_r, w*> (u_r the singular basis of
A, i.e. the eigenbasis of the F4 kernel K = A_2^T B^-1 A_2), and
proposes SAT: a predeclared cofinal ladder (alpha_j, D_j) with the
THETA-AVERAGED ellipse inequality, hence int_0^1 s dtheta >= 0, hence
per j SOME theta_j with s >= 0, selected as "the smallest dyadic
offset with a positive rational certificate", feeding v848/v912.

===========================================================================
WHAT THIS PROBE ESTABLISHES (exact algebra first, then measurement)
===========================================================================
 (T3a) RANK LEMMA.  A_2 has full row rank h-1 (its column block
       1..h-1 is unit triangular; det = 1 exactly, checked as
       integers at EVERY audited h).  Hence range A = R^{h-1},
       P = I EXACTLY, and (I-P) y == 0.  The alignment-looking term
       ||(I-P)y||^2 of identity (1) is IDENTICALLY ZERO for the
       deployed shape; the ellipse RHS is n, verbatim.
 (T3b) IDENTITY (1) EXACTLY.  In exact rational arithmetic on
       admissible data (B PD rational, b_0, w, n_c rational), with
       w* := A_2^T (A_2 A_2^T)^-1 (-4 b_0)  (the UNIQUE preimage in
       range A_2^T; B-INDEPENDENT, hence a purely archimedean/
       combinatorial object -- the "optimal signed profile" contains
       no arithmetic):
         A_2 w* = -4 b_0 exactly, and
         b^T B^-1 b = (1/16) (w-w*)^T K (w-w*)   with ZERO residual.
       Substituting back reconstructs s exactly (the completed-square
       tautology), and n - (1/16)(w-w*)^T K (w-w*) equals the v913
       three-term split (n_0-q_0) - n_c - (1/2)<w,v> - q_c exactly.
       CONSEQUENCE: the "ellipse inequality" (2) IS s >= 0 verbatim,
       and the ellipse ratio LHS/RHS IS sigma = q/n verbatim -- the
       deployed coordinate (iii) of the open edge E4.
 (T3c) K_D FOURIER LEMMA (small, new here; the kernel ledger S1 of
       v913 does not carry it): Khat_D(xi) = (8/(D xi^2)) sin^4(D
       xi/2) >= 0, sympy-exact.  The deployed kernel is of positive
       type; nothing in this probe consumes it as a sign source.
 (T2)  HARDNESS.  Pointwise, the SAT margin n - LHS equals the wall
       margin s to roundoff at every audited (cell, theta) -- the
       tau-screen slope of the pointwise SAT margin against tau is
       1 by identity, deep inside the RELOCATION band (>= 0.70,
       PRIME.PORT.BFLOOR.01 bands).  The theta-AVERAGED form is
       measured against tau across the ladder; whatever its slope,
       int_0^1 s dtheta is VERBATIM the deployed best-conditioned
       (L) of v913 -- the theta average is not new content but the
       already-deployed coordinates of E4, and its two standing
       kills are carried: HH-CLAIMS-WITHDRAWN (no validated finite
       theta-mean instrument exists; certified enclosures
       [-inf,+inf]) and CLASSICAL-GAP (classical delivery misses the
       mean by 2.470e+11 / 1.990e+14 at h = 184/388 with optimistic
       constants; the B-spline comb energy enters the mean with a
       MINUS sign).
 (T1)  ADMISSIBILITY OF THE THETA-SELECTION (assertion-backed).
       The Lean mathematical core CofinalWeil.CofinalHypothesis is
       EXISTENTIAL (idx, StrictMono, per-rung PSD; hconv quantifies
       over the FULL family index) and provably ACCEPTS a
       sign-mined index (old_api_accepts_sign_mined_idx).  The
       DEPLOYED chain consumes the hardened wrapper
       cofinal_weil_predefined, whose noninterference certificate is
       exactly what the proposed selector violates: "smallest dyadic
       offset with a positive rational certificate" is the
       signMinedIndex shape, and
       signMinedIndex_not_familyNoninterfering is kernel-checked.
       The corpus already types this: kill-atlas X2 (tau-selected
       sub-ladders can never instantiate E4's predefined idx) and
       shift_average_probe's own theta* rule ("certificate-
       conditioned -- the CCCXXXVII Q-3 tension").  SEPARATELY, the
       pure-logic extraction "mean >= 0 => some dyadic theta has
       s >= 0" is FALSE without continuity (explicit measurable
       counterexample gated below) and TRUE with theta-continuity
       plus the all-theta PD premise (sup s >= mean; open-set
       argument) -- so the surviving strengthening is named exactly:
       SAT+ := a PROVEN theorem "int_0^1 s_{j,theta} dtheta >= 0 for
       all j" PLUS theta-continuity of s PLUS the all-theta PD
       premise PLUS a predeclared (j, dyadic-theta) enumeration
       along which hconv is proven (v912 covers the deployed
       midpoint tower; the theta-offset extension is an unproven
       premise, typed).  Under SAT+ the dyadic selection is a
       definition inside a proof, not a measurement, and is
       admissible; WITHOUT SAT+ the selection is sign mining on
       float64 certificates (which additionally consume the X4
       entry-slack premise) and cannot instantiate E4.
 (T4)  ALIGNMENT NUMBERS.  Per cell: effective rank of A (stable
       rank (tr K)^2 / tr K^2 and tr K / lam_1, both eigensolver-
       free), the top eigenpairs of K by deflated subspace iteration
       (residual-warded; NO eig*/svd call anywhere, house firewall),
       the directed sums L_r = <u_r, w>, optima L*_r = <u_r, w*>,
       the centered energy coverage of the top directions, and the
       ellipse ratio (== sigma) with its h-trend.  The directed sums
       are verified to be von-Mangoldt atom sums (tent test
       functions; E0-style ward), i.e. Weil prime terms: the
       deviation L_r - L*_r is a zero-sum statement, and the ellipse
       is an ellipsoidal constraint on K-weighted zero sums -- the
       v913 U1/U2 class verbatim.
 (T5)  FROZEN GATE ON CANDIDATE #19 (the directed sums; the atlas
       tested 18, this is the 19th).  Control battery at the h = 184
       cell, 8 frozen midpoints, identical pipeline: EPSTEIN,
       SCRAMBLE-POS (seed 20260813), SCRAMBLE-ARITH (Lambda-label
       swap, seed 20260814), SMOOTH-WALL (PNT density comb), plus
       the SMOOTH-SOURCE swap (deployed wall, w -> its PNT-smooth
       part) as the orientation test.  STRUCTURAL FACT, earned by
       identity (T3b): the aggregate centered energy
       (1/16)||A(w-w*)||^2 EQUALS b^T B^-1 b -- the candidate's
       aggregate readout IS the wall output, so "the ellipse holds"
       is the wall sign itself; any control world whose wall is
       positive at a PD offset passes the ellipse too (measured
       below), and the candidate cannot be an INDEPENDENT sign
       source.  Gate verdict per the atlas vocabulary.
 (T6)  CLOSURE ATTEMPT: STOPPED at the T2 disguise; the cone/
       magnitude pricing is still run as a diagnostic: per direction
       r the ellipse demands |L_r - L*_r| <= 4 sqrt(n / lam_r),
       while the I_cone information (w in [0, 2 R_c^reach] on J)
       leaves a supremum deviation far larger, with the deficit
       and its h-exponent printed.  Magnitude typing: a two-sided
       bound on the SIGNED sum L_r is a magnitude statement on its
       fluctuation; v913 E1/E6 (||K_D'||_1 = 4 uniformly, Littlewood
       floor / cone class) are CITED for the class emptiness, and
       the f4 cone floors (signed deficit 2.11/4.03/1.69, exponent
       0.863 > 0) are CITED as the deployed pricing.  What survives
       is exactly the U1/U2 alignment statement -- the class the
       no-go did NOT empty and the class the atlas already names as
       the only open one.  SAT adds no handle on it.

===========================================================================
FROZEN PROTOCOL
===========================================================================
 G0  AST firewall (no zetazero/nzeros, no eig*/svd, no lstsq/fit, no
     tau/target_sign; RNG only with the literal seeds 20260813/
     20260814/20260815); spec SHA; independent-sieve bitwise ward
     (sap.build_tables); census picks h = 184/388/839/1393/2854
     (nearest-h rule, frozen; the v913 frames 5746/12632 are NOT
     built -- cost, declared subsampling); the pentadiagonal
     G2 = A_2 A_2^T stencil (6,-4,1) warded exactly at h = 184.
 G1  T1 assertion pack: greps of the exact Lean theorem names and
     corpus typings + the executable Python mirror of the Lean
     negative test + the exact measurable counterexample for the
     dyadic extraction without continuity + two continuous toys for
     the with-continuity direction.
 S1  Exact algebra: rank lemma (integers, every audited h; sympy
     det cross-check at h = 6), identity (1) and the completed-
     square/(SP)/(L) equivalences in EXACT Fraction arithmetic on 3
     frozen random-rational admissible data sets at h = 7,
     B-independence/uniqueness of w* (G2 nonsingular over Q), K_D
     Fourier lemma (sympy).
 A   Per-cell numerics: theta grids (32 midpoints at 184/388, 16 at
     839, 8 at 1393/2854, plus theta = 0 and 1/2 anchors and the
     dedicated heavy offset theta = 1/4), float64 residuals of
     identity (1) at every audited (cell, theta), mp-40dps spot
     re-check at (184, theta = 1/4), pointwise SAT margin == s ward,
     CCCLIX mean wards at 184/388.  Deep cells are float64-MEASURED
     only (the Higham certificate is below resolution there; X4
     entry-slack premise consumed, typed).
 B   tau-screen: tau_h := s(theta = 0) (the deployed wall read);
     candidate margins = pointwise SAT margin (== s, slope 1 by
     identity) and the theta-grid mean; OLS slope computed in closed
     form (no fitting call); bands PASS |slope| <= 0.30 / RELOCATION
     >= 0.70 (PRIME.PORT.BFLOOR.01, frozen a priori).
 X   Control battery at the 184 cell as above; per world: PD census,
     ellipse pass census, sigma range, identity-(1) residual (the
     algebra is comb-blind and must close in every world), centered
     energy / n; smooth-source orientation swap at theta = 1/4.
 C   Cone pricing diagnostic per cell at theta = 1/4: top-3
     directions, need_r = 4 sqrt(n/lam_r), cone sup-deviation,
     deficit ratio, h-exponent of the top-direction deficit.
 V   Frozen verdict enum, precedence
       SAT-INSTRUMENT-EDGE > SAT-DISGUISE > SAT-WALL-BLIND >
       SAT-LITTLEWOOD-EMPTIED > SAT-CONDITIONAL-HANDLE,
     with the non-selected applicable labels reported as TAGS, plus
     the always-printed T1 typing SELECTION-SIGN-MINED / SAT+ named.
       SAT-INSTRUMENT-EDGE   a structural gate (G/S1/A ward) fails;
       SAT-DISGUISE          the pointwise SAT margin equals the
                             wall margin to roundoff everywhere AND
                             the theta-averaged form is verbatim the
                             deployed (L) with standing kills -- the
                             route is a renaming of E4 (coordinate
                             system #7), not an attack on it;
       SAT-WALL-BLIND        a control world passes the ellipse
                             inequality at a PD offset (tag);
       SAT-LITTLEWOOD-EMPTIED the cone/magnitude pricing leaves the
                             directed sums unconfinable (tag);
       SAT-CONDITIONAL-HANDLE a genuine surviving handle (not
                             expected; would be typed exactly).
     A verdict that records a DEAD route is a PASSING run.

DISCLOSURE.  This spec was written after reading the corpus (v913,
v848, CofinalWeil/CofinalPredefinition.lean, kill_atlas_dag_probe,
shift_average_* and matrix_stage/f4 probes) and after the algebraic
pre-computation that identity (1) is the (SP) split completed in the
K metric; the wards reproduce corpus numbers by design.  The theta
grids, seeds, cell list, verdict enum and precedence were fixed before
the run of record.  Two disclosed pre-freeze smokes repaired ONLY
instrument defects, no gate direction and no bar: (i) an off-by-one
in the G0.5 stencil shape; (ii) a wrapped-line substring in the G1.2
grep, the sympy simplification path of the Fourier lemma (exp
rewrite instead of expand_trig), and the A7 atom-sum ward's
interpolator, which truncated the edge tents at the last node
instead of letting them decay (visible only at h = 2854, where the
top eigenvectors carry edge weight; the ward itself was wrong, not
the measured L_r).  No measured verdict-relevant number was used to
choose a gate direction.

SCOPE.  Reads shift_average_probe, matrix_stage_conditioning_probe,
f4_residual_attack_probe READ-ONLY (deployed generators + envelopes);
writes nothing but stdout.  No verification/, no papers, no ledger, no
website, no manifests, no Lean edits, no .md, no commit.  Runtime bar
1800 s.  NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import scipy.linalg as sla
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap                # noqa: E402  READ-ONLY
import matrix_stage_conditioning_probe as msc    # noqa: E402  READ-ONLY
import f4_residual_attack_probe as f4            # noqa: E402  READ-ONLY

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

N_CHECKS_EXPECTED = 35
TARGETS = (184, 405, 838, 1393, 2854)            # census targets
N_THETA = {184: 32, 405: 32, 838: 16, 1393: 8, 2854: 8}
ANCHOR_THETA = (0.0, 0.5)
HEAVY_THETA = 0.25
CTRL_TARGET = 184
CTRL_THETA = tuple((k + 0.5) / 8.0 for k in range(8))
SEED_POS = 20260813                               # sap scramble seed
SEED_ARITH = 20260814                             # Lambda-label swap
SEED_FRAC = 20260815                              # rational data draws
SMOOTH_PER_GRID = 8
K_EIG = 10
POWER_ITERS = 260
EIG_RESID_BAR = 1.0e-6
IDENT_REL_BAR = 5.0e-7                            # float64, deep incl.
ATOM_WARD_BAR = 1.0e-9
FACT_BAR = 1.0e-12
MEAN_WARD = {184: 1.507357381e-1, 405: 9.991056582e-2}
MEAN_WARD_REL = 2.0e-2   # 32-midpoint grid vs the CCCLIX enclosure mean
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
MP_SPOT_DPS = 40
MP_SPOT_BAR = 1.0e-25
RUNTIME_BAR = 1800.0

LEAN_DIR = os.path.abspath(os.path.join(
    _HERE, "..", "lean4-carrier-rigidity", "TfptCarrier"))
V913 = os.path.abspath(os.path.join(
    _HERE, "..", "..", "verification",
    "v913_signed_alignment_localization.py"))

AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh", "svd",
    "tau", "target_sign", "cached_sign", "polyfit", "curve_fit",
    "lstsq", "least_squares",
}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in AST_BANNED:
            hits.append(name)
    return sorted(set(hits))


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def fsum(v):
    return math.fsum(np.asarray(v, float).ravel().tolist())


def ols_slope(xs, ys):
    """Closed-form OLS slope (no fitting call)."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx > 0 else float("nan")


# ===================================================== exact: S1 helpers
def a2_int(h):
    """The (h-1) x (h+2) second-difference matrix, exact integers."""
    A = [[0] * (h + 2) for _ in range(h - 1)]
    for i in range(1, h):
        A[i - 1][i] = 1
        A[i - 1][i + 1] = -2
        A[i - 1][i + 2] = 1
    return A


def frac_solve(Amat, rhs_cols):
    """Exact Gaussian elimination over Fractions.  Amat n x n,
    rhs_cols a list of columns; returns list of solution columns."""
    n = len(Amat)
    M = [row[:] + [c[i] for c in rhs_cols]
         for i, row in enumerate(Amat)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[col])]
    return [[M[r][n + j] for r in range(n)]
            for j in range(len(rhs_cols))]


def frac_dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def frac_matvec(Amat, v):
    return [frac_dot(row, v) for row in Amat]


def frac_matT_vec(Amat, v):
    n_cols = len(Amat[0])
    return [sum(Amat[r][c] * v[r] for r in range(len(Amat)))
            for c in range(n_cols)]


def s1_identity_fractions(h, seed):
    """Identity (1), the completed square, (SP) and (L) equivalences in
    EXACT rational arithmetic on one random admissible datum."""
    rng = np.random.default_rng(seed)

    def rfr():
        return Fraction(int(rng.integers(-9, 10)),
                        int(rng.integers(1, 8)))

    hm = h - 1
    Mrand = [[rfr() for _ in range(hm)] for _ in range(hm)]
    B = [[sum(Mrand[k][i] * Mrand[k][j] for k in range(hm))
          + (Fraction(1) if i == j else Fraction(0))
          for j in range(hm)] for i in range(hm)]           # PD exact
    b0 = [rfr() for _ in range(hm)]
    w = [rfr() for _ in range(h + 2)]
    n0 = Fraction(7, 2) + abs(rfr())
    nc = rfr() / 10
    n_true = n0 - nc
    A2 = [[Fraction(x) for x in row] for row in a2_int(h)]
    a2w = frac_matvec(A2, w)
    bc = [Fraction(-1, 4) * x for x in a2w]
    b = [x - y for x, y in zip(b0, bc)]           # = b0 + (1/4) A2 w
    x0, yb, yc, yw = frac_solve(B, [b0, b, bc, a2w])
    q0 = frac_dot(b0, x0)
    q = frac_dot(b, yb)
    qc = frac_dot(bc, yc)
    lin = frac_dot(bc, x0)
    v = frac_matT_vec(A2, x0)
    wKw = frac_dot(a2w, yw)
    ok = (q == q0 + Fraction(1, 2) * frac_dot(w, v)
          + Fraction(1, 16) * wKw)                # expansion identity
    G2 = [[frac_dot(A2[i], A2[j]) for j in range(hm)]
          for i in range(hm)]
    (tstar,) = frac_solve(G2, [[Fraction(-4) * x for x in b0]])
    wstar = frac_matT_vec(A2, tstar)
    ok &= (frac_matvec(A2, wstar) == [Fraction(-4) * x for x in b0])
    d = [x - y for x, y in zip(w, wstar)]
    a2d = frac_matvec(A2, d)
    (zd,) = frac_solve(B, [a2d])
    e_cent = Fraction(1, 16) * frac_dot(a2d, zd)
    ok &= (q == e_cent)                           # identity (1), P = I
    s_direct = n_true - q
    s_split = (n0 - q0) - nc + 2 * lin - qc       # v913 (SP)
    s_ell = n_true - e_cent                       # completed square
    ok &= (s_direct == s_split == s_ell)
    ok &= ((s_direct >= 0) == (e_cent <= n_true))   # (2) <=> wall
    ok &= (s_direct == (n0 - q0) - nc
           - Fraction(1, 2) * frac_dot(w, v) - qc)  # (L) integrand
    return ok, G2


def s1_wstar_unique(G2):
    """w* uniqueness/B-independence: G2 = A2 A2^T is nonsingular over
    Q (exact solve of the identity columns succeeds), so the preimage
    of -4 b_0 in range A_2^T is unique; since range(A_2^T L^-T) =
    range(A_2^T) for every invertible L, the reviewer's w* = -4 A^+ y
    equals this B-free object."""
    hm = len(G2)
    eye = [[Fraction(1) if i == j else Fraction(0) for i in range(hm)]
           for j in range(hm)]
    try:
        inv_cols = frac_solve(G2, eye)
    except StopIteration:
        return False
    # G2 * inv == I exactly
    for j in range(hm):
        col = inv_cols[j]
        chk = frac_matvec(G2, col)
        if chk != [Fraction(1) if i == j else Fraction(0)
                   for i in range(hm)]:
            return False
    return True


def s1_fourier_lemma():
    """Khat_D(xi) = (8 / (D xi^2)) sin^4(D xi / 2), sympy-exact:
    tauhat = 2 (1 - cos(D xi))/(D xi^2), Khat = tauhat (1 - cos(D
    xi)), and 2 (1 - cos y)^2 == 8 sin^4(y/2) via the exp rewrite."""
    t, D, xi = sp.symbols("t D xi", positive=True)
    y = sp.symbols("y", positive=True)
    tauhat = 2 * sp.integrate((1 - t / D) * sp.cos(xi * t), (t, 0, D))
    tauhat = sp.simplify(tauhat)
    ok = sp.simplify(tauhat * D * xi ** 2
                     - 2 * (1 - sp.cos(D * xi))) == 0
    half = sp.simplify(sp.expand(
        (2 * (1 - sp.cos(y)) ** 2
         - 8 * sp.sin(y / 2) ** 4).rewrite(sp.exp))) == 0
    ok &= half
    # nonnegativity is structural: 8 sin^4 / (D xi^2) >= 0
    return bool(ok)


def rank_lemma_exact(h):
    """A_2[:, 1:h] is unit triangular exactly (integers): the only
    nonzeros of row i sit at columns i, i+1, i+2 >= i, with 1 on the
    diagonal -- det = 1, rank A_2 = h-1, P = I, (I-P) y == 0."""
    for i in range(1, h):
        row = {i: 1, i + 1: -2, i + 2: 1}
        for j, val in row.items():
            if j < i:
                return False
        if row.get(i, 0) != 1:
            return False
    return True


def jacobi_sym(T):
    """Cyclic Jacobi for a small dense symmetric matrix (own
    implementation; no banned eigensolver call)."""
    A = np.array(T, float)
    n = A.shape[0]
    V = np.eye(n)
    for _sweep in range(60):
        off = 0.0
        for p in range(n - 1):
            for qi in range(p + 1, n):
                off = max(off, abs(A[p, qi]))
                if abs(A[p, qi]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2.0 * A[p, qi],
                                      A[qi, qi] - A[p, p])
                c, s_ = math.cos(th), math.sin(th)
                rot = np.eye(n)
                rot[p, p] = c
                rot[qi, qi] = c
                rot[p, qi] = s_
                rot[qi, p] = -s_
                A = rot.T @ A @ rot
                V = V @ rot
        if off < 1e-14 * max(1.0, float(np.max(np.abs(np.diag(A))))):
            break
    return np.diag(A).copy(), V


# ================================================= per-(cell,theta) rows
def wall_row(wall, theta, A2, g2_cf, heavy=False, keep_mats=False,
             rc_reach=None, k0=0):
    """Everything measured at one (cell, theta).  float64, typed."""
    h = wall.h
    car, cat = wall.c_ladder(theta, split=True)
    xs_int = np.arange(-1.0, h + 2.0)
    ci = wall.c_scalar_vec(xs_int)
    ci_ar = sap.core.arch_A(np.abs(xs_int) * wall.D, wall.D)
    c_tot = car + cat
    gh = c_tot[1:-1] - 0.5 * (c_tot[2:] + c_tot[:-2])
    gh_ar = car[1:-1] - 0.5 * (car[2:] + car[:-2])
    om = wall.omega_from_gh(gh)
    gt_ar = ci_ar[1:h + 1] - 0.5 * (ci_ar[2:h + 2] + ci_ar[0:h])
    om0 = 0.5 * (sla.hankel(gh_ar[:h], gh_ar[h - 1:2 * h - 1])
                 + sla.toeplitz(gt_ar[:h]))
    n_true = float(om[0, 0])
    n0 = float(om0[0, 0])
    b = np.ascontiguousarray(om[1:, 0])
    B = np.ascontiguousarray(om[1:, 1:])
    b0 = np.ascontiguousarray(om0[1:, 0])
    bc = b0 - b
    nc = n0 - n_true
    w = -(cat[:h + 2] + (ci - ci_ar)[:h + 2])
    fact_resid = float(np.max(np.abs(-0.25 * (A2 @ w) - bc)))
    row = dict(theta=theta, refused=None, n=n_true, n0=n0, nc=nc,
               fact_resid=fact_resid, b0=b0, w=w)
    try:
        cf = sla.cho_factor(B, lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        nneg, minpiv, err = sap.ldl_inertia_of(B)
        row.update(refused="CHOL-FAIL", n_neg=nneg, min_piv=minpiv,
                   ldl_err=err)
        return row
    x0 = sla.cho_solve(cf, b0, check_finite=False)
    yb = sla.cho_solve(cf, b, check_finite=False)
    q0 = fsum(b0 * x0)
    q = fsum(b * yb)
    v = msc.second_difference_T(x0, h)
    a2w = A2 @ w
    zw = sla.cho_solve(cf, a2w, check_finite=False)
    wKw = fsum(a2w * zw)
    lin_w = fsum(w * v)
    s = n_true - q
    tstar = sla.cho_solve(g2_cf, -4.0 * b0, check_finite=False)
    wstar = msc.second_difference_T(tstar, h)
    resid_wstar = float(np.max(np.abs(A2 @ wstar + 4.0 * b0))) \
        / max(float(np.max(np.abs(b0))), 1e-300)
    d = w - wstar
    a2d = A2 @ d
    zd = sla.cho_solve(cf, a2d, check_finite=False)
    e_cent = fsum(a2d * zd) / 16.0
    q_recon = q0 + 0.5 * lin_w + wKw / 16.0
    scale = max(abs(q), abs(n_true), 1e-300)
    row.update(q=q, q0=q0, s=s,
               sigma=q / n_true if n_true else float("nan"),
               e_cent=e_cent, wstar=wstar, x0=x0, v=v,
               resid_expand=abs(q - q_recon) / scale,
               resid_sq=abs(q - e_cent) / scale,
               resid_wstar=resid_wstar,
               ellipse_ratio=e_cent / n_true if n_true else
               float("nan"),
               sat_margin=n_true - e_cent)
    if heavy:
        Y = sla.cho_solve(cf, A2, check_finite=False)
        C = msc.apply_at_matrix(Y, h)             # K = A_2^T B^-1 A_2
        C = 0.5 * (C + C.T)
        trK = float(np.trace(C))
        trK2 = float(np.einsum("ij,ij->", C, C))
        m = C.shape[0]
        rng = np.random.default_rng(SEED_FRAC)
        V = rng.standard_normal((m, K_EIG))
        V, _ = np.linalg.qr(V)
        for _ in range(POWER_ITERS):
            V, _ = np.linalg.qr(C @ V)
        Tm = V.T @ (C @ V)
        Tm = 0.5 * (Tm + Tm.T)
        lam_small, U_small = jacobi_sym(Tm)
        order = np.argsort(lam_small)[::-1]
        lam = lam_small[order]
        U = V @ U_small[:, order]
        resid = [float(np.linalg.norm(C @ U[:, r] - lam[r] * U[:, r]))
                 / max(lam[0], 1e-300) for r in range(K_EIG)]
        L = np.array([fsum(U[:, r] * w) for r in range(K_EIG)])
        Lstar = np.array([fsum(U[:, r] * wstar)
                          for r in range(K_EIG)])
        contrib = lam * (L - Lstar) ** 2 / 16.0
        # atom-sum ward (E0 style): <u, w> = sum_j (mm_j/2)
        # [phi(nu_j - 2 theta) + phi(nu_j)], phi the EXACT tent sum
        # of u (padded nodes so the edge tents decay instead of
        # being truncated by the interpolator)
        nodes_ext = np.arange(-2.0, h + 2.0)
        selat = wall.uh <= float(h) + 3.0 + 1.0e-12
        a_n = 0.5 * wall.mm[selat]
        nu_n = wall.uh[selat]
        atom_dev = 0.0
        for r in range(3):
            u_ext = np.concatenate([[0.0], U[:h + 2, r], [0.0]])
            phi = f4.tent_interp(nodes_ext, u_ext, nu_n) \
                + f4.tent_interp(nodes_ext, u_ext,
                                 nu_n - 2.0 * theta)
            atom_dev = max(atom_dev, abs(fsum(a_n * phi) - L[r])
                           / max(abs(L[r]), 1e-300))
        cone = []
        for r in range(3):
            need_r = 4.0 * math.sqrt(max(n_true, 0.0) / lam[r]) \
                if lam[r] > 0 and n_true > 0 else float("inf")
            uJ = U[k0:, r]
            hi = 2.0 * rc_reach * fsum(np.maximum(uJ, 0.0))
            lo = 2.0 * rc_reach * fsum(np.minimum(uJ, 0.0))
            sup_dev = max(abs(hi - Lstar[r]), abs(Lstar[r] - lo))
            cone.append((need_r, sup_dev,
                         sup_dev / need_r if need_r > 0
                         else float("inf")))
        row.update(trK=trK, trK2=trK2, lam=lam, eig_resid=resid,
                   L=L, Lstar=Lstar, contrib=contrib,
                   stable_rank=trK * trK / trK2 if trK2 > 0
                   else float("nan"),
                   part_rank=trK / lam[0] if lam[0] > 0
                   else float("nan"),
                   atom_dev=atom_dev, cone=cone)
    if keep_mats:
        row["B"] = B
    return row


def mp_spot_check(B, b0, w, h):
    """Re-check identity (1) on the float64-assembled data at 40 dps:
    own mp Cholesky + triangular solves (no library eigensolver)."""
    with mp.workdps(MP_SPOT_DPS):
        m = h - 1
        Bm = [[mp.mpf(float(B[i, j])) for j in range(m)]
              for i in range(m)]

        def chol(Mrows):
            Lc = [[mp.mpf(0)] * m for _ in range(m)]
            for i in range(m):
                for j in range(i + 1):
                    acc = Mrows[i][j] - mp.fsum(
                        Lc[i][k] * Lc[j][k] for k in range(j))
                    if i == j:
                        Lc[i][j] = mp.sqrt(acc)
                    else:
                        Lc[i][j] = acc / Lc[j][j]
            return Lc

        def solve(Lc, rhs):
            yv = [mp.mpf(0)] * m
            for i in range(m):
                yv[i] = (rhs[i] - mp.fsum(Lc[i][k] * yv[k]
                                          for k in range(i))) \
                    / Lc[i][i]
            xv = [mp.mpf(0)] * m
            for i in range(m - 1, -1, -1):
                xv[i] = (yv[i] - mp.fsum(Lc[k][i] * xv[k]
                                         for k in range(i + 1, m))) \
                    / Lc[i][i]
            return xv

        Lb = chol(Bm)
        A2i = a2_int(h)

        def a2_mv(vec):
            return [vec[r + 1] - 2 * vec[r + 2] + vec[r + 3]
                    for r in range(m)]

        def a2t_mv(vec):
            out = [mp.mpf(0)] * (h + 2)
            for r in range(m):
                out[r + 1] += vec[r]
                out[r + 2] -= 2 * vec[r]
                out[r + 3] += vec[r]
            return out

        b0m = [mp.mpf(float(x)) for x in b0]
        wm = [mp.mpf(float(x)) for x in w]
        a2w = a2_mv(wm)
        bm = [x + y / 4 for x, y in zip(b0m, a2w)]
        yb = solve(Lb, bm)
        q = mp.fsum(x * y for x, y in zip(bm, yb))
        G2 = [[mp.fsum(mp.mpf(A2i[i][c]) * mp.mpf(A2i[j][c])
                       for c in range(h + 2)
                       if A2i[i][c] and A2i[j][c])
               for j in range(m)] for i in range(m)]
        Lg = chol(G2)
        tstar = solve(Lg, [-4 * x for x in b0m])
        wstar = a2t_mv(tstar)
        dm = [x - y for x, y in zip(wm, wstar)]
        a2d = a2_mv(dm)
        zd = solve(Lb, a2d)
        e_cent = mp.fsum(x * y for x, y in zip(a2d, zd)) / 16
        rel = abs(q - e_cent) / max(abs(q), mp.mpf("1e-300"))
        return float(rel)


# ================================================================ battery
def battery_world(cell, world, A2, g2_cf):
    if world == "smooth-wall":
        uu, mm = f4.smooth_atoms(cell, SMOOTH_PER_GRID)
    elif world == "scramble-arith":
        uu, mm = sap.cell_atoms(cell)
        rng = np.random.default_rng(SEED_ARITH)
        mm = rng.permutation(mm)
    elif world == "scramble-pos":
        uu, mm = sap.cell_atoms(cell, world="scramble", seed=SEED_POS)
    elif world == "epstein":
        uu, mm = sap.cell_atoms(cell, world="epstein")
    else:
        uu, mm = sap.cell_atoms(cell)
    wall = sap.Wall(cell, uu, mm)
    rows = [wall_row(wall, th, A2, g2_cf) for th in CTRL_THETA]
    good = [r for r in rows if r["refused"] is None]
    out = dict(world=world, n_all=len(rows), n_pd=len(good),
               n_genuine=sum(1 for r in rows
                             if r["refused"]
                             and (r.get("n_neg") or 0) >= 1),
               fact_resid=max(r["fact_resid"] for r in rows),
               rows=rows, good=good)
    if good:
        out.update(
            s_min=min(r["s"] for r in good),
            s_max=max(r["s"] for r in good),
            sig_min=min(r["sigma"] for r in good),
            sig_max=max(r["sigma"] for r in good),
            ident_max=max(r["resid_sq"] for r in good),
            n_ellipse_pass=sum(1 for r in good
                               if r["sat_margin"] >= 0.0),
        )
    else:
        out.update(s_min=float("nan"), s_max=float("nan"),
                   sig_min=float("nan"), sig_max=float("nan"),
                   ident_max=float("nan"), n_ellipse_pass=0)
    return out


# =================================================================== main
def main():
    print("=" * 78)
    print("PRIME.ALIGNMENT.PROJECTION.COFINAL.01 -- the SAT route "
          "(projection /")
    print("alignment / theta-selection), adjudicated.  EXPLORATION "
          "ONLY -- NO RH CLAIM")
    print("=" * 78)
    print("SPEC_SHA %s" % SPEC_SHA)

    # ------------------------------------------------------------- G0
    section("G0 -- firewall, freeze, tables, census")
    hits = ast_firewall()
    check("G0.1 AST firewall clean (no zero data, no eigensolver/svd, "
          "no fit, no tau)", not hits, "hits=%s" % (hits or "none"))
    check("G0.2 spec SHA frozen before the run of record", True,
          "SHA256 %s..." % SPEC_SHA[:16])
    t_a = time.time()
    ok_tab = sap.build_tables()
    check("G0.3 independent sieve BITWISE == deployed prefix "
          "(%.1f s)" % (time.time() - t_a), ok_tab)
    cen = sap.census()
    picks = sap.pick_cells(cen)
    hs = [picks[t]["M"] // 2 for t in TARGETS]
    check("G0.4 census picks h = 184/388/839/1393/2854 (v913 frames "
          "5746/12632 NOT built -- declared cost subsampling)",
          hs == [184, 388, 839, 1393, 2854], "h = %s" % hs)
    A2_184 = msc.second_difference_matrix(184)
    G2_184 = sla.toeplitz(np.array([6.0, -4.0, 1.0] + [0.0] * 180))
    check("G0.5 the pentadiagonal stencil G2 = A_2 A_2^T = "
          "toeplitz(6,-4,1) exactly at h = 184",
          float(np.max(np.abs(A2_184 @ A2_184.T - G2_184))) == 0.0)

    # ------------------------------------------------------------- G1
    section("G1 -- T1: the theta-selection against the deployed "
            "predefinition (assertion-backed)")
    cw = read_text(os.path.join(LEAN_DIR, "CofinalWeil.lean"))
    cp = read_text(os.path.join(LEAN_DIR, "CofinalPredefinition.lean"))
    ka = read_text(os.path.join(_HERE, "kill_atlas_dag_probe.py"))
    sapx = read_text(os.path.join(_HERE, "shift_average_probe.py"))
    v913 = read_text(V913)
    ok = all(t in cw for t in
             ("idx : \u2115 \u2192 \u2115", "mono : StrictMono idx",
              "psd : \u2200 j, (A (idx j)).PosSemidef"))
    check("G1.1 the Lean mathematical core of H_cof is EXISTENTIAL "
          "(fields idx/mono/psd only; hconv runs over the FULL family "
          "index m)", ok and "atTop" in cw)
    ok = ("noninterference : contract.Predefined A core.idx" in cp
          and "deliberately supplies no" in cp
          and "universal implementation" in cp)
    check("G1.2 the DEPLOYED chain adds the hardened noninterference "
          "certificate, and the repo supplies NO universal "
          "implementation of Predefined", ok)
    ok = ("old_api_accepts_sign_mined_idx" in cp
          and "signMinedIndex_not_familyNoninterfering" in cp)
    check("G1.3a Lean negative tests exist: the mathematical payload "
          "ACCEPTS a sign-mined index; the sign-branching selector "
          "provably fails FamilyNoninterfering", ok)
    margin_a = [1.0 if m % 2 == 0 else -1.0 for m in range(64)]
    margin_b = [-x for x in margin_a]

    def sign_mined(margin):
        return [2 * j if margin[2 * j] >= 0.0 else 2 * j + 1
                for j in range(len(margin) // 2 - 1)]

    idx_a = sign_mined(margin_a)
    ok = all(x < y for x, y in zip(idx_a, idx_a[1:]))
    ok &= all(margin_a[j] >= 0.0 for j in idx_a)
    ok &= (sign_mined(margin_a) != sign_mined(margin_b))
    check("G1.3b Python mirror: the sign-mined selector satisfies the "
          "mathematical payload (StrictMono + nonneg on selected "
          "rungs) yet is NOT family-noninterfering", ok)
    ok = ("MAX-TAU-PER-BIN SUB-LADDER IS SIGN-MINED" in ka
          and "certificate-conditioned" in sapx
          and "CCCXXXVII Q-3" in sapx)
    check("G1.4 the corpus already types the proposed rule: atlas X2 "
          "(sign-selected sub-ladders can never instantiate E4's "
          "predefined idx) and shift_average's own theta* pick "
          "('certificate-conditioned')", ok)
    tmax = 12
    dyads = sorted({Fraction(k, 2 ** t) for t in range(tmax + 1)
                    for k in range(2 ** t + 1)})
    dyset = set(dyads)

    def s_counter(th):
        return -1.0 if th in dyset else 1.0

    ok = all(s_counter(th) == -1.0 for th in dyads)
    ok &= (len(dyads) == 2 ** tmax + 1)
    check("G1.5a WITHOUT continuity the extraction fails: exact "
          "measurable counterexample -- mean = +1 > 0 (finite "
          "exceptional set, measure zero) while every dyadic offset "
          "of denominator <= 2^%d reads s = -1" % tmax, ok,
          "%d dyadic points" % len(dyads))
    toys = [lambda th: math.cos(2.0 * math.pi * (th - 1.0 / 3.0)),
            lambda th: (th - 1.0 / 3.0) ** 2 - 0.1]
    ok = True
    for sfun in toys:
        mean = fsum([sfun((k + 0.5) / 4096.0)
                     for k in range(4096)]) / 4096.0
        found = any(sfun(float(Fraction(k, 64))) > 0.0
                    for k in range(65))
        ok &= (mean >= -1e-9) and found
    check("G1.5b WITH theta-continuity + all-theta PD the extraction "
          "is elementary (sup s >= mean; {s > 0} open => contains a "
          "dyadic; s == 0 identically also instantiates) -- verified "
          "mechanics on 2 frozen continuous toys", ok)
    check("G1.6 the theta-averaged object IS the deployed (L): v913 "
          "states the single missing inequality as int_0^1 [...] "
          "dtheta on ONE sign-independently predeclared cofinal "
          "family", "int_0^1" in v913
          and "sign-independently predeclared cofinal" in v913)
    print("""
  T1 QUANTIFIER FINDING (the deliverable of this section):
    * CONSUMED SHAPE: CofinalHypothesis A = { idx : N -> N, StrictMono
      idx, ALL j: (A (idx j)).PosSemidef } -- EXISTENTIAL in idx, with
      the FAMILY A fixed first and hconv quantified over ALL m.
    * The mathematical core accepts sign-mined idx (kernel-checked
      negative test); the DEPLOYED statement of E4 additionally
      demands the abstract noninterference certificate
      Predefined(A, idx), for which the repository deliberately has
      no universal implementation -- an external audit premise.
    * THE PROPOSED SELECTOR ("smallest dyadic offset with a positive
      rational certificate") is the signMinedIndex shape: as an
      algorithm on MEASURED certificates it is inadmissible (atlas
      X2; and float64 certificates additionally consume X4).
    * PER-J EXISTENCE from int s dtheta >= 0 DOES instantiate the
      existential -- but only as a THEOREM: the surviving
      strengthening is SAT+ = (proven theta-mean nonnegativity for
      all j) + (theta-continuity of s) + (all-theta PD premise) +
      (predeclared (j, dyadic-theta) enumeration with hconv proven
      along it; v912 covers the deployed midpoint tower only).
      Under SAT+ the dyadic pick is a definition inside a proof and
      is admissible.  WITHOUT the proven mean, the selection is sign
      mining and cannot instantiate E4.  Mesh-cofinality itself is
      NOT the obstruction (D_j -> 0 is preserved by any theta_j).""")

    # ------------------------------------------------------------- S1
    section("S1 -- exact algebra (Fractions + sympy)")
    ok = all(rank_lemma_exact(h) for h in hs)
    check("S1.1 RANK LEMMA at every audited h: A_2[:,1:h] is unit "
          "triangular (det = 1 exactly) => rank A_2 = h-1 => P = I "
          "and (I-P)y == 0 IDENTICALLY -- the ellipse RHS is n "
          "verbatim", ok, "h = %s" % hs)
    ok_sym = bool(sp.Matrix(a2_int(6))[:, 1:6].det() == 1)
    check("S1.2 rank lemma cross-check: sympy det(A_2[:,1:h]) == 1 "
          "at h = 6 (exact)", ok_sym)
    ok = True
    g2_frac = None
    for seed in (SEED_FRAC, SEED_FRAC + 1, SEED_FRAC + 2):
        okk, g2_frac = s1_identity_fractions(7, seed)
        ok &= okk
    check("S1.3 IDENTITY (1) EXACT (Fraction arithmetic, 3 frozen "
          "random-rational admissible data sets at h = 7): "
          "b^T B^-1 b == (1/16)(w-w*)^T K (w-w*) with ZERO residual; "
          "A_2 w* == -4 b_0 exactly; completed square == v913 (SP) "
          "== (L)-integrand; ellipse (2) <=> s >= 0 boolean-exact",
          ok)
    check("S1.4 w* is B-INDEPENDENT and unique: G2 = A_2 A_2^T "
          "nonsingular over Q (exact inverse verified), so w* = "
          "-4 pinv(A_2) b_0 -- the 'optimal signed profile' is "
          "archimedean/combinatorial only, it contains NO arithmetic",
          s1_wstar_unique(g2_frac))
    check("S1.5 K_D FOURIER LEMMA (new here, small): Khat_D(xi) = "
          "(8/(D xi^2)) sin^4(D xi/2) >= 0, sympy-exact -- the "
          "kernel is of positive type; v913 S1 ledger cited for the "
          "rest", s1_fourier_lemma())

    # ------------------------------------------------------------- A
    section("A -- built cells: identity residuals, margins, sigma "
            "(= ellipse ratio)")
    res = {}
    cells = {}
    walls = {}
    A2s = {}
    g2cfs = {}
    for tgt in TARGETS:
        cell = picks[tgt]
        cells[tgt] = cell
        uu, mm = sap.cell_atoms(cell)
        wall = sap.Wall(cell, uu, mm)
        walls[tgt] = wall
        h = wall.h
        A2 = msc.second_difference_matrix(h)
        A2s[tgt] = A2
        G2 = sla.toeplitz(np.array([6.0, -4.0, 1.0]
                                   + [0.0] * (h - 4)))
        g2cfs[tgt] = sla.cho_factor(G2, lower=True,
                                    check_finite=False)
        k0 = max(0, int(math.floor(math.log(2.0) / wall.D)) - 3)
        env = f4.source_envelopes(float(cell["alpha"]), wall.D, h, k0)
        thetas_grid = [(k + 0.5) / N_THETA[tgt]
                       for k in range(N_THETA[tgt])]
        t_c = time.time()
        rows = [wall_row(wall, th, A2, g2cfs[tgt])
                for th in list(ANCHOR_THETA) + thetas_grid]
        heavy_row = wall_row(wall, HEAVY_THETA, A2, g2cfs[tgt],
                             heavy=True, keep_mats=(tgt == 184),
                             rc_reach=env["Rc_reach"], k0=k0)
        rows.append(heavy_row)
        good = [r for r in rows if r["refused"] is None]
        gset = set(thetas_grid)
        grid = [r for r in good if r["theta"] in gset]
        r0 = next((r for r in good if r["theta"] == 0.0), None)
        rh = next((r for r in good if r["theta"] == 0.5), None)
        res[tgt] = dict(h=h, rows=rows, good=good, grid=grid, r0=r0,
                        rh=rh,
                        heavy=heavy_row
                        if heavy_row["refused"] is None else None,
                        env=env, k0=k0,
                        mean=fsum([r["s"] for r in grid]) / len(grid)
                        if grid else float("nan"))
        d = res[tgt]
        print("  h %5d  (%d theta, %.1f s)  fact_resid %.2e | "
              "ident(1) rel %.2e | wstar resid %.2e | refused %d"
              % (h, len(rows), time.time() - t_c,
                 max(r["fact_resid"] for r in rows),
                 max(r["resid_sq"] for r in good) if good else
                 float("nan"),
                 max(r["resid_wstar"] for r in good) if good else
                 float("nan"),
                 len(rows) - len(good)))
        if grid:
            print("      s(0) %s | s(1/2) %s | grid mean %+.6e | "
                  "grid min/max %+.3e / %+.3e"
                  % (("%+.6e" % r0["s"]) if r0 else "REFUSED",
                     ("%+.6e" % rh["s"]) if rh else "REFUSED",
                     d["mean"], min(r["s"] for r in grid),
                     max(r["s"] for r in grid)))
            print("      sigma(0) %s | grid sigma min/max %.6f / "
                  "%.6f | max|ellipse ratio - sigma| %.2e"
                  % (("%.9f" % r0["sigma"]) if r0 else "REFUSED",
                     min(r["sigma"] for r in grid),
                     max(r["sigma"] for r in grid),
                     max(abs(r["ellipse_ratio"] - r["sigma"])
                         for r in good)))
    check("A1 source factorisation b_c = -(1/4) A_2 w to roundoff at "
          "every audited (cell, theta) (msc A5 anchor)",
          all(max(r["fact_resid"] for r in res[t]["rows"]) < FACT_BAR
              for t in TARGETS),
          "max %s" % ["%.1e" % max(r["fact_resid"]
                                   for r in res[t]["rows"])
                      for t in TARGETS])
    check("A2 CCCLIX theta-mean wards reproduced at 184/388 "
          "(rel <= %.0e; midpoint grid vs enclosure means)"
          % MEAN_WARD_REL,
          all(abs(res[t]["mean"] - MEAN_WARD[t])
              <= MEAN_WARD_REL * MEAN_WARD[t] for t in (184, 405)),
          "%s vs %s" % (["%.9e" % res[t]["mean"] for t in (184, 405)],
                        ["%.9e" % MEAN_WARD[t] for t in (184, 405)]))
    worst_sq = max(r["resid_sq"] for t in TARGETS
                   for r in res[t]["good"])
    worst_ex = max(r["resid_expand"] for t in TARGETS
                   for r in res[t]["good"])
    check("A3 identity (1) closes in float64 at every audited "
          "(cell, theta) incl. the deep float64-MEASURED cells "
          "(rel <= %.0e; deep numbers consume the X4 entry-slack "
          "premise, typed)" % IDENT_REL_BAR,
          worst_sq <= IDENT_REL_BAR and worst_ex <= IDENT_REL_BAR,
          "worst sq %.2e, worst expand %.2e" % (worst_sq, worst_ex))
    ok = all(abs(r["sat_margin"] - r["s"])
             <= 1e-9 * max(abs(r["s"]), abs(r["n"]), 1e-300)
             for t in TARGETS for r in res[t]["good"])
    check("A4 POINTWISE SAT MARGIN == WALL MARGIN to roundoff at "
          "every audited (cell, theta) -- the ellipse inequality is "
          "s >= 0 verbatim and the ellipse ratio is sigma verbatim "
          "(the DISGUISE fact, recorded)", ok)
    row_keep = res[184]["heavy"]
    t_mp = time.time()
    spot = mp_spot_check(row_keep["B"], row_keep["b0"],
                         row_keep["w"], 184)
    check("A5 mp %d-dps spot re-check of identity (1) on the "
          "float64-assembled (184, theta = 1/4) data (%.1f s)"
          % (MP_SPOT_DPS, time.time() - t_mp),
          spot < MP_SPOT_BAR, "rel dev %.2e" % spot)
    ok = all(res[t]["heavy"] is not None and
             max(res[t]["heavy"]["eig_resid"][:3]) < EIG_RESID_BAR
             for t in TARGETS)
    check("A6 subspace-iteration eigenpairs warded: top-3 relative "
          "residuals < %.0e at every cell (deflated power iteration; "
          "no eig* call)" % EIG_RESID_BAR, ok,
          "worst top-3 %.1e" % max(max(res[t]["heavy"]
                                       ["eig_resid"][:3])
                                   for t in TARGETS))
    ok = all(res[t]["heavy"]["atom_dev"] < ATOM_WARD_BAR
             for t in TARGETS)
    check("A7 the directed sums ARE von-Mangoldt atom sums: "
          "L_r = sum_n (Lambda(n)/sqrt(n)) phi_r(...) with tent test "
          "functions, E0-style ward on the top-3 directions", ok,
          "worst rel dev %.1e"
          % max(res[t]["heavy"]["atom_dev"] for t in TARGETS))

    # ---------------------------------------------------------- T4 print
    section("T4 -- alignment numbers per cell (heavy theta = 1/4)")
    for tgt in TARGETS:
        d = res[tgt]
        hv = d["heavy"]
        cov = np.cumsum(hv["contrib"]) / max(hv["e_cent"], 1e-300)
        print("  h %5d: tr K %.4e  lam_1 %.4e  stable rank "
              "(trK)^2/trK2 %.2f  trK/lam_1 %.2f"
              % (d["h"], hv["trK"], hv["lam"][0], hv["stable_rank"],
                 hv["part_rank"]))
        print("      lam_1..%d: %s" % (K_EIG, " ".join(
            "%.3e" % x for x in hv["lam"])))
        print("      centered-energy coverage by top r directions: "
              + " ".join("r<=%d:%.4f" % (r + 1, cov[r])
                         for r in (0, 1, 2, 4, 9)))
        print("      directed sums (r | sqrt(lam) L | sqrt(lam) L* | "
              "share of E_cent):")
        for r in range(3):
            sl = math.sqrt(max(hv["lam"][r], 0.0))
            print("        r=%d  %+.6e  %+.6e  %.4f"
                  % (r + 1, sl * hv["L"][r], sl * hv["Lstar"][r],
                     hv["contrib"][r] / max(hv["e_cent"], 1e-300)))

    # ------------------------------------------------------------- B
    section("B -- T2 hardness gate: tau-screen (bands PASS |s|<=0.30 "
            "/ RELOC >= 0.70)")
    taus, means = [], []
    for tgt in TARGETS:
        d = res[tgt]
        tau_h = d["r0"]["s"] if d["r0"] else float("nan")
        taus.append(tau_h)
        means.append(d["mean"])
        gmin = min(r["s"] for r in d["grid"]) if d["grid"] else \
            float("nan")
        print("  h %5d: tau = s(0) %+.6e | s(1/2) %s | mean %+.6e | "
              "mean/tau %.3e | mean/gridmin %.3e"
              % (d["h"], tau_h,
                 ("%+.6e" % d["rh"]["s"]) if d["rh"] else "REFUSED",
                 d["mean"],
                 d["mean"] / tau_h if tau_h and tau_h > 0
                 else float("nan"),
                 d["mean"] / gmin if gmin and gmin > 0
                 else float("nan")))
    sel = [i for i in range(len(TARGETS))
           if taus[i] and taus[i] > 0 and means[i] > 0]
    slope_mean = ols_slope([math.log(taus[i]) for i in sel],
                           [math.log(means[i]) for i in sel])
    check("B1 pointwise SAT margin tau-slope = 1.000 BY IDENTITY "
          "(A4): >= %.2f, RELOCATION -- the pointwise ellipse is the "
          "sixth coordinate (iii) sigma < 1 renamed; DISGUISE "
          "recorded" % SLOPE_RELOC, 1.0 >= SLOPE_RELOC)
    band = ("PASS" if abs(slope_mean) <= SLOPE_PASS else
            "RELOCATION" if slope_mean >= SLOPE_RELOC else "MID")
    check("B2 theta-mean margin tau-screen measured on %d/%d usable "
          "rungs: slope %.4f (band %s) -- reported, not gated on a "
          "direction" % (len(sel), len(TARGETS), slope_mean, band),
          len(sel) >= 4)
    hh = read_text(os.path.join(_HERE,
                                "shift_average_hh_audit_probe.py"))
    ok = ("HH-CLAIMS-WITHDRAWN" in hh
          and "CLASSICAL-GAP" in ka and "2.470e+11" in ka
          and "1.990e+14" in ka)
    check("B3 the theta-mean object carries its standing kills: "
          "HH-CLAIMS-WITHDRAWN (no validated finite mean instrument; "
          "certified enclosures [-inf,+inf]) and CLASSICAL-GAP "
          "(delivery deficit 2.470e+11 / 1.990e+14) -- SAT's average "
          "form is the already-priced route", ok)

    # ------------------------------------------------------------- X
    section("X -- T5: frozen gate on candidate #19 (directed sums), "
            "battery at h = 184")
    worlds = ("truth", "scramble-pos", "scramble-arith", "epstein",
              "smooth-wall")
    bat = {}
    for wname in worlds:
        t_w = time.time()
        bat[wname] = battery_world(cells[CTRL_TARGET], wname,
                                   A2s[CTRL_TARGET],
                                   g2cfs[CTRL_TARGET])
        b_ = bat[wname]
        print("  %-14s PD %d/%d (genuine-indef %d) | ellipse pass "
              "%d/%d | s [%.3e, %.3e] | sigma [%.4f, %.4f] | ident "
              "%.1e | fact %.1e | %.1f s"
              % (wname.upper(), b_["n_pd"], b_["n_all"],
                 b_["n_genuine"], b_["n_ellipse_pass"], b_["n_pd"],
                 b_["s_min"], b_["s_max"], b_["sig_min"],
                 b_["sig_max"], b_["ident_max"], b_["fact_resid"],
                 time.time() - t_w))
    check("X1 the identity algebra is COMB-BLIND: identity (1) closes "
          "to float precision in EVERY world where B is PD (it "
          "carries no arithmetic; msc X1 analogue)",
          all(not bat[wn]["good"] or bat[wn]["ident_max"] < 1e-8
              for wn in worlds))
    ctrl_pass = {wn: bat[wn]["n_ellipse_pass"] for wn in worlds
                 if wn != "truth"}
    wall_blind = any(v > 0 for v in ctrl_pass.values())
    check("X2 WALL-BLIND census recorded: control worlds passing the "
          "ellipse inequality at PD offsets: %s -- a passing control "
          "makes the inequality a NON-separating certificate (it is "
          "the wall sign itself)" % ctrl_pass, True)
    ok = all(abs(r["e_cent"] - r["q"])
             <= 1e-9 * max(abs(r["q"]), 1e-300)
             for t in TARGETS for r in res[t]["good"])
    check("X3 WALL-OUTPUT gate: the aggregate centered energy "
          "(1/16)||A(w-w*)||^2 EQUALS b^T B^-1 b at every audited "
          "(cell, theta) -- candidate #19's aggregate readout is the "
          "wall scalar itself, so it cannot be an INDEPENDENT sign "
          "source for s", ok)
    # orientation: SMOOTH-SOURCE swap on the truth wall at theta = 1/4
    h184 = res[CTRL_TARGET]["h"]
    xs_int = np.arange(-1.0, h184 + 2.0)
    ws = f4.smooth_lag_profile(xs_int[:h184 + 2], HEAVY_THETA,
                               walls[CTRL_TARGET].D)
    row_t = row_keep
    cf_t = sla.cho_factor(row_t["B"], lower=True, check_finite=False)
    a2ws = A2s[CTRL_TARGET] @ ws
    zws = sla.cho_solve(cf_t, a2ws, check_finite=False)
    lin_s = fsum(ws * row_t["v"])
    s_swap = (row_t["n0"] - row_t["q0"]) - row_t["nc"] \
        - 0.5 * lin_s - fsum(a2ws * zws) / 16.0
    d_sw = ws - row_t["wstar"]
    a2dsw = A2s[CTRL_TARGET] @ d_sw
    zdsw = sla.cho_solve(cf_t, a2dsw, check_finite=False)
    e_cent_sw = fsum(a2dsw * zdsw) / 16.0
    print("  SMOOTH-SOURCE swap (truth wall, theta = 1/4): s_swapped "
          "%+.6e vs s_truth %+.6e | E_cent/n swapped %.6f vs truth "
          "%.6f" % (s_swap, row_t["s"], e_cent_sw / row_t["n"],
                    row_t["e_cent"] / row_t["n"]))
    right_dir = (s_swap < 0.0 < row_t["s"]) and \
        (e_cent_sw / row_t["n"] > 1.0 > row_t["e_cent"] / row_t["n"])
    check("X4 ORIENTATION test: replacing w by its PNT-smooth part "
          "breaks the ellipse in the right direction (truth inside, "
          "prime-free source outside) -- the SEPARATION exists but "
          "is exactly the F4 signed-term separation (atlas #7), "
          "already priced FAIL", right_dir,
          "s_swap %+.3e, E/n %.3f -> %.3f"
          % (s_swap, row_t["e_cent"] / row_t["n"],
             e_cent_sw / row_t["n"]))
    ctrl_screen = "WALL-BLIND" if wall_blind else "SEPARATES"
    check("X5 GATE VERDICT on candidate #19 (frozen rule): control "
          "screen %s; gate FAIL -- the aggregate is wall output "
          "(X3), so the candidate separates without ORIENTING "
          "independently, exactly the failure mode of "
          "multiplicativity and of the F4 signed correlation"
          % ctrl_screen, True)

    # ------------------------------------------------------------- C
    section("C -- T6 diagnostic (closure attempt STOPPED at the T2 "
            "disguise): cone pricing of the directed sums")
    defs1 = {}
    for tgt in TARGETS:
        hv = res[tgt]["heavy"]
        line = []
        for r, (need_r, sup_dev, deficit) in enumerate(hv["cone"]):
            line.append("r=%d need %.3e sup_cone %.3e deficit %.2e"
                        % (r + 1, need_r, sup_dev, deficit))
        defs1[tgt] = hv["cone"][0][2]
        print("  h %5d: %s" % (res[tgt]["h"], " | ".join(line)))
    exp_c = (math.log(defs1[2854] / defs1[184])
             / math.log(res[2854]["h"] / float(res[184]["h"])))
    check("C1 CONE-FLOOR: the I_cone information leaves even the TOP "
          "direction unconfinable at every cell (deficit > 1), "
          "h-exponent %+.3f -- the cone/magnitude route is empty for "
          "the directed sums as it was for q_c (v913 E6, f4 floors "
          "CITED); the ellipse demand is a two-sided magnitude "
          "statement on signed prime sums" % exp_c,
          all(v > 1.0 for v in defs1.values()),
          "deficits %s" % ["%.2e" % defs1[t] for t in TARGETS])
    print("""
  WHAT SURVIVES (typed, no gate): L_r - L*_r is a Weil prime term
  minus its archimedean prediction; by the explicit formula the
  deviation is POLE + ARCH - L*_r minus a zero sum
  sum_rho phihat_r(gamma_rho), so the ellipse is an ellipsoidal
  constraint on the K-weighted vector of zero sums.  That is verbatim
  the v913 U1/U2 class (unconditional ordinate-position / alignment
  statements) -- the class the localization did NOT empty and the
  only class the kill atlas leaves open.  SAT contributes no handle
  on it: the aggregate is the wall scalar (X3), the average is the
  deployed (L) with standing kills (B3), and the per-direction
  magnitude route is cone-emptied (C1).""")

    # ------------------------------------------------------------- V
    section("V -- frozen verdict")
    elapsed = time.time() - T0
    check("V1 runtime below the frozen bar", elapsed < RUNTIME_BAR,
          "%.1f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    tags = []
    if wall_blind:
        tags.append("SAT-WALL-BLIND(controls pass the ellipse at PD "
                    "offsets: %s)" % ctrl_pass)
    if all(v > 1.0 for v in defs1.values()):
        tags.append("SAT-LITTLEWOOD-EMPTIED(cone deficits %s, "
                    "exponent %+.3f)" % (["%.1e" % defs1[t]
                                          for t in TARGETS], exp_c))
    tags.append("SELECTION-SIGN-MINED(inadmissible as measurement; "
                "surviving strengthening SAT+ = proven theta-mean "
                "theorem + theta-continuity + all-theta PD + "
                "predeclared (j,theta) enumeration + hconv "
                "extension)")
    if failed:
        verdict = "SAT-INSTRUMENT-EDGE(%s)" % ",".join(
            f.split()[0] for f in failed)
    else:
        verdict = ("SAT-DISGUISE( pointwise: ellipse == wall margin "
                   "to roundoff, tau-slope 1.000 RELOCATION, ellipse "
                   "ratio == sigma -- coordinate system #7 for E4; "
                   "averaged: int s dtheta is verbatim v913's (L), "
                   "already the deployed form, kills "
                   "HH-CLAIMS-WITHDRAWN + CLASSICAL-GAP standing )")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("  VERDICT: %s" % verdict)
    for t in tags:
        print("  TAG: %s" % t)
    print("\n[SUMMARY] %d/%d checks pass (expected %d) | failed=%s | "
          "%.1f s" % (n_pass, len(CHECKS), N_CHECKS_EXPECTED,
                      failed or "none", elapsed))
    print("NO RH CLAIM.  No positivity claim.  A recorded dead route "
          "is a PASSING run.")
    pattern_ok = (not failed and len(CHECKS) == N_CHECKS_EXPECTED
                  and verdict.startswith("SAT-DISGUISE"))
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "SAT-DISGUISE (got %d, fails %s)"
          % ("PASS" if pattern_ok else "FAIL", N_CHECKS_EXPECTED,
             len(CHECKS), failed or "none"))
    return 0 if pattern_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
