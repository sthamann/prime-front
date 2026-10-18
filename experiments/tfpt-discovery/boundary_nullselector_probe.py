"""BOUNDARY.NULLSELECTOR.01 -- the independent d = 4 forcing through
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


if __name__ == "__main__":
    raise SystemExit(run())
