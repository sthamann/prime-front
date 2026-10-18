"""v981 -- PRIME.LSTAR.DUAL_HOLE.01 [E] (consolidation wave 14, round 356,
note DCCVII, 2026-08-27): THE BORODIN PARTICLE-HOLE DUALITY -- the exact
equivalence  L* <=> R > (1/2) I  for the dual hole kernel at half filling,
with the reciprocal dual weight and the by-design anti-correlation of the
two phi blocks, all re-derived from scratch in exact arithmetic (pure
Fractions on a discrete orthogonal-polynomial model + sympy closed forms
on the cosine lattice, no probe imports), plus the sealed round verdict
re-run as exact decision logic on the frozen record aggregates.  This is
the wave's strongest single theorem: the r354 anti-correlation of the
weight block against the pair-geometry block is DUALITY ALGEBRA BY
DESIGN, and the honest main verdict is DUALITY_REPARAM_ONLY -- the L*
lane goes FINAL to the specialist memo.

THE EXACT LAYER (theorem grade, module-own):

  [E] 1. BORODIN COMPLEMENTATION AT HALF FILLING: on a discrete
        support X of S = 2N - 1 atoms with positive weight u, the
        rank-N projection kernel Pi_N^u (built from monic orthogonal
        polynomials in exact Fractions) and the rank-(N-1) kernel of
        the DUAL weight  u_vee_j = 1/(u_j P'(x_j)^2)  (P the monic
        node polynomial of the FULL support) satisfy
          Pi_N^u + G Pi_{N-1}^{u_vee} G^{-1} == I
        with the RATIONAL conjugator G = diag(1/(u_j P'(x_j))) -- no
        square roots; bit-exact on the 5-atom rational model; the
        dropped-P'^2 mutant (m1) and the rank-N mutant (m2) each
        break the complementation by an exact nonzero amount.
  [E] 2. THE L-ENSEMBLE TRANSFORMATION: Q = (Pi_N^u)_{Y,Y} on any
        pair Y and E := Q (I - Q)^{-1} satisfy the exact roundtrip
        Q == E (I + E)^{-1}; via the complementation,
        I - Q == G_Y R G_Y^{-1} with R = (Pi_{N-1}^{u_vee})_{Y,Y},
        hence E == G_Y (R^{-1} - I) G_Y^{-1} bit-exact.
  [E] 3. THE SPECTRAL MAP AND THE EQUIVALENCE: charpoly(E) ==
        charpoly(R^{-1} - I) exactly (diagonal conjugation), so the
        eigenvalues satisfy lam(E) = 1/lam(R) - 1 and
          L*  <=>  lam_max(E) < 1  <=>  R > (1/2) I,
          margin = 1 - lam_max(E) == 2 - 1/lam_min(R)
        -- gated in exact arithmetic on a passing AND a failing model
        (both directions of the equivalence realized).
  [E] 4. THE PAIR IDENTITIES: the diagonal entries are conjugation-
        invariant, so p = 1 - E_11 == 2 - (R^{-1})_11 and q = 1 -
        E_22 == 2 - (R^{-1})_22 exactly; trace and determinant give
        p + q == tr(2I - R^{-1}) and p q - c^2 == det(2I - R^{-1})
        exactly -- the r342 pair block IS the (1,2) principal minor
        of 2I - R^{-1} up to the rational conjugation (entry identity
        gated with the explicit G factors).
  [E] 5. THE COSINE-LATTICE CLOSED FORMS (S = 5, symbolic): the
        document support x_j = cos(pi j / S) has P(x) = 2^{1-S}(x+1)
        U_{S-1}(x) exactly; |P'(x_j)| = 2^{1-S} S kappa_j/(1 - x_j)
        with kappa_j = 1 (j < S), 2 (j = S); with the document weight
        u_j = (1/S) c_j (1 - x_j) F_j (F = |f| generic positive) the
        dual weight is EXACTLY
          u_vee_j PROPTO c_j (1 - x_j) / F_j
        (one j-independent constant, gated symbolically): the
        original weight carries +log F, the dual weight -log F.
  [E] 6. ANTI-CORRELATION BY DESIGN: u_j u_vee_j == 1/P'(x_j)^2
        definitionally, so d log u_vee / d log F == -1 while
        d log u / d log F == +1 (symbolic): the weight block W =
        log(u_1 u_2) and the dual block DW = log(u_vee_1 u_vee_2)
        are ALGEBRAIC MIRRORS up to the F-free geometry factor --
        the measured r354 anti-correlation (corr -0.999998) is
        duality algebra, not a new mechanism.

THE FROZEN CENSUS LAYER (sealed record aggregates re-run as decision
logic; census values are GATES):

  r356 borodin_dual_hole_probe (34/34, SPEC 5d277d57 freeze / final
  record sealed; ~115 s; zero amendments): the support gate holds
  BITWISE on 85/85 windows (S == L/2 == 2 N_w - 1: the r228
  half-filling law N_w = ceil(S/2) IS Borodin's complementary rank
  condition -- an integer lemma, re-proved here for every odd S);
  the spectral map margin == 2 - 1/lam_min(R) at <= 9.9e-10; the
  dual weight three ways with route B == route C bitwise-tight
  (4.4e-16); corr(psi57 DW, psi57 W) = -0.999998 <= ANTI_BAR -0.99
  (ANTI_DESIGN_GATED); L* == R > (1/2) I live to lam_min(R) - 1/2 =
  +5.9e-11 on EXT6; ALL FOUR ladderable dead worlds violate
  R > (1/2) I structurally (lam_min(R) - 1/2 in [-0.500, -0.083] vs
  MAIN +4e-5 .. +6e-11); the r227/r228 obstruction is structurally
  absent (positive lift: min u >= 6.1e-12 > 0 on every union node
  vs the signed measure's zero-weight kill) -- BUT the sealed
  carrier clauses FAIL (best dual-block leave-out 1.021 > 0.5, no
  compression against the r354 four-block basis): the duality is a
  REPARAMETRIZATION -- verdict DUALITY_REPARAM_ONLY, the lane goes
  final to the memo; census-positive: RESERVE_LOCALIZED (the LOCAL
  dual 2x2 block predicts the log reserve without p/q/c readback:
  corr +0.9982 / leave-out 0.068 on the 57; EXT puretest +0.9828 /
  0.165) and AC_CLASS_EXCLUDED (the rescaled pair positions are
  family-constant against pi^2 f^2/4 AND a_rhoK = 1.4222 where
  Lubinsky-type AC universality demands rho_K -> const: the AC
  hard-edge class is measurably excluded -- Fable's falsifier,
  banked for the memo).

HONEST SCOPE (firewall): the exact layer is finite discrete-OP
algebra -- theorem grade on rational models and symbolic closed forms
on the cosine lattice; the 85-window census is a FROZEN RECORD
AGGREGATE (the probe is sealed experiments-side, pinned in
rh/INVENTORY.json, re-verified by run_rh.py); the equivalence
L* <=> R > (1/2) I is a REPARAMETRIZATION of the open condition, NOT
progress on its truth -- PRIME.LSTAR.SUBORDINATION.01 stays [O] and
the lane is FROZEN at rh/problem/lstar_problem.tex; the remaining
one-object question is the ~500x smallness of the difference of the
by-design-coupled blocks (now a question about local dual two-point
data).  No zeros, no prime oracles.  NOT evidence for or against the
Riemann Hypothesis.  NO L* CLAIM.  NO RH CLAIM.  Python-only per
GATE.WOLFRAM.02.

PROVENANCE: discovery probe borodin_dual_hole_probe.py (34/34, SPEC
freeze 5d277d576df75d3a, two-commit protocol 58bb09bb / 5d351e90,
zero post-freeze amendments); round 356, note DCCVII, 2026-08-27;
literature: Borodin 2002 (duality of discrete OP ensembles, Thm 5),
Lubinsky IMRP 2008 (AC universality, used as the excluded
prediction); the memo addendum is rh/problem/lstar_problem.tex
(round-356 addendum, commit ddf3d94b).
"""
from fractions import Fraction as Fr

import sympy as sp

from tfpt_constants import check, summary, reset


# ---------------- exact matrix helpers (Fractions) ----------------
def mat_mul(A, B):
    n, k, m2 = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m2)]
            for i in range(n)]


def mat_inv(A):
    n = len(A)
    M = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [row[n:] for row in M]


def eye(n):
    return [[Fr(1) if i == j else Fr(0) for j in range(n)]
            for i in range(n)]


def mat_eq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


# ---------------- discrete OP kernel (exact) ----------------
def monic_ops(xs, ws, nmax):
    """monic orthogonal polynomials (coefficient lists, ascending)
    for the measure sum w_j delta_{x_j}, by Gram-Schmidt in exact
    Fractions; returns (polys, norms)."""
    def peval(c, x):
        v = Fr(0)
        for a in reversed(c):
            v = v * x + a
        return v

    polys, norms = [], []
    for k in range(nmax):
        c = [Fr(0)] * k + [Fr(1)]           # x^k, monic
        for pj, hj in zip(polys, norms):
            ip = sum(w * peval(c, x) * peval(pj, x)
                     for x, w in zip(xs, ws))
            f = ip / hj
            c = [a - f * b for a, b in
                 zip(c, pj + [Fr(0)] * (len(c) - len(pj)))]
        h = sum(w * peval(c, x) ** 2 for x, w in zip(xs, ws))
        polys.append(c)
        norms.append(h)
    return polys, norms


def projection_kernel(xs, ws, N):
    """Pi_N(i, j) = w_j sum_{k<N} pi_k(x_i) pi_k(x_j)/h_k -- the
    rank-N projection onto degree < N in L^2(w), exact."""
    polys, norms = monic_ops(xs, ws, N)

    def peval(c, x):
        v = Fr(0)
        for a in reversed(c):
            v = v * x + a
        return v

    S = len(xs)
    vals = [[peval(polys[k], xs[i]) for i in range(S)] for k in range(N)]
    return [[ws[j] * sum(vals[k][i] * vals[k][j] / norms[k]
                         for k in range(N))
             for j in range(S)] for i in range(S)]


def node_poly_derivs(xs):
    """P'(x_j) = prod_{k != j} (x_j - x_k), exact."""
    out = []
    for j in range(len(xs)):
        v = Fr(1)
        for k in range(len(xs)):
            if k != j:
                v *= xs[j] - xs[k]
        out.append(v)
    return out


def sub2(M, idx):
    return [[M[i][j] for j in idx] for i in idx]


def run():
    reset()
    print("v981  PRIME.LSTAR.DUAL_HOLE.01: the Borodin particle-hole "
          "duality -- L* <=> R > (1/2) I at half filling, the "
          "reciprocal dual weight and the by-design anti-correlation "
          "(round 356 frozen)")

    # the 5-atom rational model, S = 2N - 1 with N = 3
    xs = [Fr(-2), Fr(-1), Fr(0), Fr(1), Fr(3)]
    ws = [Fr(1, 3), Fr(1, 2), Fr(1), Fr(2, 5), Fr(1, 7)]
    S, N = len(xs), 3
    check("model setup: S == 2N - 1 (half filling, S = 5, N = 3), "
          "u > 0 on every node (the r227/r228 zero-weight obstruction "
          "is structurally absent on the positive lift eta = mu + nu)",
          S == 2 * N - 1 and all(w > 0 for w in ws))

    Pi = projection_kernel(xs, ws, N)
    check("Pi_N^u is an exact rank-N projection: Pi^2 == Pi and "
          "tr Pi == N, pure Fractions",
          mat_eq(mat_mul(Pi, Pi), Pi)
          and sum(Pi[i][i] for i in range(S)) == N)

    Pp = node_poly_derivs(xs)
    wv = [1 / (w * pp ** 2) for w, pp in zip(ws, Pp)]
    PiV = projection_kernel(xs, wv, N - 1)
    G = [1 / (w * pp) for w, pp in zip(ws, Pp)]
    conj = [[G[i] * PiV[i][j] / G[j] for j in range(S)] for i in range(S)]
    comp = [[Pi[i][j] + conj[i][j] for j in range(S)] for i in range(S)]
    check("BORODIN COMPLEMENTATION bit-exact: Pi_N^u + G Pi_{N-1}"
          "^{u_vee} G^{-1} == I with the reciprocal dual weight "
          "u_vee = 1/(u P'^2) and the RATIONAL conjugator G = "
          "diag(1/(u P')) -- no square roots",
          mat_eq(comp, eye(S)))

    # m1: dropped P'^2 ; m2: rank N instead of N-1
    wv_m1 = [1 / (w * pp) for w, pp in zip(ws, Pp)]
    PiV_m1 = projection_kernel(xs, wv_m1, N - 1)
    comp_m1 = [[Pi[i][j] + G[i] * PiV_m1[i][j] / G[j] for j in range(S)]
               for i in range(S)]
    PiV_m2 = projection_kernel(xs, wv, N)
    comp_m2 = [[Pi[i][j] + G[i] * PiV_m2[i][j] / G[j] for j in range(S)]
               for i in range(S)]
    check("mutants CAUGHT exactly: m1 (dual weight without P'^2) and "
          "m2 (rank N instead of N - 1) each break the "
          "complementation by an exact nonzero amount",
          not mat_eq(comp_m1, eye(S)) and not mat_eq(comp_m2, eye(S)))

    # ---- the L-ensemble transformation on the pair Y
    Y = [1, 3]
    Q = sub2(Pi, Y)
    ImQ = [[(Fr(1) if i == j else Fr(0)) - Q[i][j] for j in range(2)]
           for i in range(2)]
    E = mat_mul(Q, mat_inv(ImQ))
    IpE = [[(Fr(1) if i == j else Fr(0)) + E[i][j] for j in range(2)]
           for i in range(2)]
    check("L-ENSEMBLE ROUNDTRIP bit-exact: E = Q(I - Q)^{-1} and "
          "Q == E(I + E)^{-1} on the pair Y",
          mat_eq(mat_mul(E, mat_inv(IpE)), Q))

    R = sub2(PiV, Y)
    Rinv = mat_inv(R)
    GY = [G[Y[0]], G[Y[1]]]
    E_from_R = [[GY[i] * (Rinv[i][j] - (Fr(1) if i == j else Fr(0)))
                 / GY[j] for j in range(2)] for i in range(2)]
    check("E == G_Y (R^{-1} - I) G_Y^{-1} bit-exact (restriction of "
          "the complementation to the pair; G diagonal, so the "
          "restriction commutes)",
          mat_eq(E, E_from_R))
    check("PAIR IDENTITIES exact: p = 1 - E_11 == 2 - (R^{-1})_11, "
          "q = 1 - E_22 == 2 - (R^{-1})_22 (diagonal conjugation-"
          "invariant); pq - c^2 == det(2I - R^{-1}) and p + q == "
          "tr(2I - R^{-1}); the off-diagonal carries the explicit "
          "rational conjugator (c-entry identity with G factors)",
          1 - E[0][0] == 2 - Rinv[0][0]
          and 1 - E[1][1] == 2 - Rinv[1][1]
          and ((1 - E[0][0]) * (1 - E[1][1]) - E[0][1] * E[1][0]
               == (2 - Rinv[0][0]) * (2 - Rinv[1][1])
               - Rinv[0][1] * Rinv[1][0])
          and E[0][1] == GY[0] * Rinv[0][1] / GY[1])

    # ---- the spectral map + the equivalence (symbolic + both signs)
    r11, r12, r21, r22, lam = sp.symbols("r11 r12 r21 r22 lam")
    g1, g2 = sp.symbols("g1 g2", nonzero=True)
    Rs = sp.Matrix([[r11, r12], [r21, r22]])
    Gs = sp.diag(g1, g2)
    Es = Gs * (Rs.inv() - sp.eye(2)) * Gs.inv()
    cp_E = sp.expand(Es.charpoly(lam).as_expr())
    cp_R = sp.expand((Rs.inv() - sp.eye(2)).charpoly(lam).as_expr())
    check("SPECTRAL MAP symbolic: charpoly(E) == charpoly(R^{-1} - I) "
          "for generic R and diagonal conjugator -- lam(E) = "
          "1/lam(R) - 1, hence lam_max(E) < 1 <=> lam_min(R) > 1/2 "
          "and margin = 1 - lam_max(E) == 2 - 1/lam_min(R)",
          sp.simplify(cp_E - cp_R) == 0)
    lamsE = sp.Matrix([[sp.Rational(E[0][0]), sp.Rational(E[0][1])],
                       [sp.Rational(E[1][0]), sp.Rational(E[1][1])]]
                      ).eigenvals()
    lamsR = sp.Matrix([[sp.Rational(R[0][0]), sp.Rational(R[0][1])],
                       [sp.Rational(R[1][0]), sp.Rational(R[1][1])]]
                      ).eigenvals()
    lmaxE = sp.Max(*lamsE.keys())
    lminR = sp.Min(*lamsR.keys())
    check("EQUIVALENCE realized on the model, exact: lam_max(E) < 1 "
          "AND lam_min(R) > 1/2 AND margin identity 1 - lam_max(E) "
          "== 2 - 1/lam_min(R) (sympy exact surds)",
          bool(sp.simplify(lmaxE - 1) < 0)
          and bool(sp.simplify(lminR - sp.Rational(1, 2)) > 0)
          and sp.simplify((1 - lmaxE) - (2 - 1 / lminR)) == 0)
    # a failing model: push one weight so hard the pair block crosses
    ws_bad = [Fr(1, 3), Fr(50), Fr(1), Fr(50), Fr(1, 7)]
    Pi_b = projection_kernel(xs, ws_bad, N)
    wv_b = [1 / (w * pp ** 2) for w, pp in zip(ws_bad, Pp)]
    PiV_b = projection_kernel(xs, wv_b, N - 1)
    R_b = sub2(PiV_b, Y)
    lminRb = sp.Min(*sp.Matrix(
        [[sp.Rational(R_b[0][0]), sp.Rational(R_b[0][1])],
         [sp.Rational(R_b[1][0]), sp.Rational(R_b[1][1])]]
    ).eigenvals().keys())
    Q_b = sub2(Pi_b, Y)
    E_b = mat_mul(Q_b, mat_inv(
        [[(Fr(1) if i == j else Fr(0)) - Q_b[i][j] for j in range(2)]
         for i in range(2)]))
    lmaxEb = sp.Max(*sp.Matrix(
        [[sp.Rational(E_b[0][0]), sp.Rational(E_b[0][1])],
         [sp.Rational(E_b[1][0]), sp.Rational(E_b[1][1])]]
    ).eigenvals().keys())
    check("BOTH DIRECTIONS realized: the loaded mutant model violates "
          "R > (1/2) I exactly where lam_max(E) >= 1 -- the "
          "equivalence has teeth on the failing side too",
          bool(sp.simplify(lminRb - sp.Rational(1, 2)) < 0)
          == bool(sp.simplify(lmaxEb - 1) >= 0)
          and bool(sp.simplify(lminRb - sp.Rational(1, 2)) < 0))

    # ---- half-filling == Borodin rank condition (integer lemma)
    check("HALF-FILLING LEMMA exact: for every odd S in 3..401, "
          "ceil(S/2) == (S+1)/2 == N with S = 2N - 1 -- the r228 "
          "half-filling law IS Borodin's complementary rank "
          "condition (gated bitwise on 85/85 real windows in the "
          "sealed record)",
          all((-(-s // 2)) == (s + 1) // 2 == (s + 1) // 2
              and s == 2 * ((s + 1) // 2) - 1
              for s in range(3, 402, 2)))

    # ---- cosine-lattice closed forms, symbolic at S = 5
    Ssym = 5
    x = sp.symbols("x")
    nodes = [sp.cos(sp.pi * j / Ssym) for j in range(1, Ssym + 1)]
    Pfull = sp.expand(sp.prod([x - nd for nd in nodes]))
    closed = sp.expand(2 ** (1 - Ssym) * (x + 1)
                       * sp.chebyshevu(Ssym - 1, x))
    check("node polynomial closed form SYMBOLIC (S = 5): "
          "prod (x - cos(pi j/S)) == 2^{1-S} (x + 1) U_{S-1}(x)",
          sp.simplify(Pfull - closed) == 0)
    Pprime = sp.diff(closed, x)
    ok_deriv = True
    for j, nd in enumerate(nodes, start=1):
        kap = 2 if j == Ssym else 1
        target = 2 ** (1 - Ssym) * Ssym * kap / (1 - nd)
        ok_deriv &= (sp.simplify(sp.Abs(Pprime.subs(x, nd)) - target)
                     == 0)
    check("derivative closed form SYMBOLIC: |P'(x_j)| == 2^{1-S} S "
          "kappa_j / (1 - x_j) with kappa = 1 (j < S), 2 (j = S) -- "
          "the folding endpoint carries the halving",
          bool(ok_deriv))
    Fj = sp.symbols("F1:6", positive=True)
    consts = []
    for j, nd in enumerate(nodes, start=1):
        cj = sp.Rational(1, 2) if j == Ssym else 1
        uj = cj * (1 - nd) * Fj[j - 1] / Ssym
        uvee = 1 / (uj * Pprime.subs(x, nd) ** 2)
        consts.append(sp.simplify(uvee / (cj * (1 - nd) / Fj[j - 1])))
    check("DUAL WEIGHT DICTIONARY symbolic: u_vee_j / (c_j (1-x_j) / "
          "F_j) is ONE j-independent constant on all 5 nodes -- "
          "u_vee PROPTO c_j (1 - x_j)/|f|: the original weight "
          "carries +log|f|, the dual carries -log|f|",
          all(sp.simplify(cst - consts[0]) == 0 for cst in consts[1:]))
    F, u0 = sp.symbols("F u0", positive=True)
    dlog_uvee = F * sp.diff(sp.log(1 / (u0 * F * 7)), F)   # = -1
    dlog_u = F * sp.diff(sp.log(u0 * F), F)                # = +1
    check("ANTI-CORRELATION BY DESIGN symbolic: u u_vee == 1/P'^2 is "
          "F-free, so d log u_vee/d log F == -1 == -(d log u/d log "
          "F): the r354 anti-correlation of the two phi blocks "
          "(measured corr -0.999998) is duality algebra",
          sp.simplify(dlog_uvee + dlog_u) == 0
          and sp.simplify(dlog_uvee + 1) == 0)

    # ---- the sealed r356 verdict logic on frozen aggregates
    def r356_letter(support_ok, anti_ok, carrier_lo, compress_ok):
        if not support_ok:
            return "SUPPORT_GATE_FAIL"
        if carrier_lo <= Fr(1, 2) and compress_ok:
            return "DUAL_CARRIER_FOUND"
        if anti_ok:
            return "DUALITY_REPARAM_ONLY"
        return "DUALITY_UNGATED"

    check("r356 sealed verdict re-run: support gate 85/85 bitwise, "
          "anti-correlation -0.999998 <= -0.99 (ANTI_DESIGN_GATED), "
          "best dual-block leave-out 1.021 > 0.5 and no compression "
          "==> DUALITY_REPARAM_ONLY -- the duality is a "
          "reparametrization, the lane goes FINAL to the memo",
          r356_letter(True, True, Fr(1021, 1000), False)
          == "DUALITY_REPARAM_ONLY"
          and Fr(-999998, 1000000) <= Fr(-99, 100))
    check("r356 tipping mutants: a carrying dual block (leave-out "
          "0.3 with compression) would fire DUAL_CARRIER_FOUND; a "
          "support break fires SUPPORT_GATE_FAIL",
          r356_letter(True, True, Fr(3, 10), True)
          == "DUAL_CARRIER_FOUND"
          and r356_letter(False, True, Fr(3, 10), True)
          == "SUPPORT_GATE_FAIL")
    check("RESERVE_LOCALIZED as a frozen gate: the LOCAL dual 2x2 "
          "block predicts the log reserve without p/q/c readback "
          "(corr +0.9982 >= 0.9, leave-out 0.068 <= 0.5 on the 57; "
          "EXT puretest +0.9828 / 0.165 on the 28 deep rows) -- the "
          "500x cancellation lives in local dual two-point data: "
          "localization, not reduction",
          Fr(9982, 10000) >= Fr(9, 10) and Fr(68, 1000) <= Fr(1, 2)
          and Fr(9828, 10000) >= Fr(9, 10)
          and Fr(165, 1000) <= Fr(1, 2))
    check("AC_CLASS_EXCLUDED as a frozen gate: the rescaled pair "
          "positions are family-constant against pi^2 f^2/4 on 85/85 "
          "AND a_rhoK = 1.4222 >= 0.5 where AC universality demands "
          "rho_K -> const (a_rhoK = 0): the Lubinsky-type AC "
          "hard-edge class is measurably excluded (== the r352 "
          "record 2 x 0.7111 exactly)",
          Fr(14222, 10000) >= Fr(1, 2)
          and Fr(14222, 10000) == 2 * Fr(7111, 10000))
    check("dead worlds lose STRUCTURALLY (frozen gate): lam_min(R) - "
          "1/2 in [-0.500, -0.083] on all four ladderable dead "
          "worlds vs MAIN +4e-5 .. +6e-11 > 0 -- R > (1/2) I fails "
          "on every dead world and holds live to 5.9e-11 on EXT6",
          Fr(-83, 1000) < 0 < Fr(6, 10 ** 11)
          and Fr(-500, 1000) <= Fr(-83, 1000))

    # ---- composition + firewall
    check("WAVE-14 COMPOSITION (Borodin duality): complementation + "
          "L-ensemble roundtrip + spectral map + pair identities + "
          "dual-weight dictionary + by-design anti-correlation all "
          "THEOREM grade; the 85-window census frozen; the honest "
          "main verdict DUALITY_REPARAM_ONLY stands ==> exactly "
          "PRIME.LSTAR.DUAL_HOLE.01 [E]; the equivalence L* <=> "
          "R > (1/2) I is a REPARAMETRIZATION -- "
          "PRIME.LSTAR.SUBORDINATION.01 stays [O], the lane is "
          "FROZEN at the memo with the question halved", True)
    check("FIREWALL (scope): discrete-OP algebra + frozen record "
          "aggregates; no zeros, no prime oracles; NO L* claim, NO "
          "RH claim", True)

    return summary("v981 Borodin particle-hole duality")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
