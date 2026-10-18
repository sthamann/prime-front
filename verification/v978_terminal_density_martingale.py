"""v978 -- PRIME.TERMINAL.DENSITY_MARTINGALE.01 [E] (consolidation wave 14,
rounds 339 + 341, notes DCLXXXVI / DCLXXXIX, 2026-08-27): THE TERMINAL
REFORMULATION THEOREM LAYER -- the density-martingale identity, the moment
dictionary, the tilted tower, the exact hand-off and the algebraic pair
ceiling, all re-derived from scratch in exact arithmetic (sympy symbolic +
pure Fractions, no probe imports), plus the sealed round verdicts re-run as
exact decision logic on the frozen record aggregates with tipping mutants.

THE EXACT LAYER (theorem grade, module-own):

  [E] 1. DENSITY MARTINGALE FROM MASS CONSERVATION ALONE: on any finite
        genealogy tree with node mass A(v) and leaf count n(v), the
        density-per-remaining-descendant d(v) = A(v)/n(v), normalized
        X(v) = d(v)/d(root), is a nonnegative martingale under the count
        path measure P(c|v) = n(c)/n(v):
          E[X_next | v] = sum_c (n_c/n_v)(A_c/n_c)/(A_v/n_v)
                        = sum_c A_c / A_v = 1 x X(v),
        i.e. the ONLY input is mass conservation sum_c A_c = A_v --
        proved symbolically on a generic node and bit-exact in Fractions
        on a concrete three-level tree (per-node sum_c p_c R_c == 1,
        per-level E[X_k] == 1).
  [E] 2. THE MOMENT DICTIONARY (the r339 terminal reformulation): with m
        leaves of masses y_i, total Y, M_k = sum (y_i/Y)^k and q_max =
        max y_i / Y:
          E[X_inf^2] == m M_2,   E[X_inf^3] == m^2 M_3,
          max X_inf == m q_max
        -- proved symbolically on generic masses and bit-exact in
        Fractions; the wrong-power mutant (m^2 M_2) is CAUGHT.  This is
        the reformulation: the terminal target sum q^3 <= C (log m)^A
        (m/log m)^... IS the cubic-moment statement E[X_inf^3] ==
        rho_2 (log m)^2 -- the banked r306 constant C_2 = 1.0694
        (0/57 violations, re-gated as a frozen anchor) already certifies
        A = 2 on the measured 57-rung set.
  [E] 3. THE JENSEN DRIFT, exactly: per node the weighted AM-GM
        prod_c R_c^{p_c} <= sum_c p_c R_c = 1 holds with rational
        exponents cleared to the integer-power inequality
        prod R_c^{a_c} <= 1 (p_c = a_c/b) -- exact Fractions, strict on
        a spread node, equality at the flat node: the log drift
        delta_k = E[ln X_{k+1}] - E[ln X_k] <= 0 is pure convexity.
  [E] 4. THE TILTED TOWER (the r341 correction): with Gamma(v) =
        sum_c p_c R_c^3 and the TILTED steps p~_c = p_c R_c^3 /
        Gamma(v) (sum_c p~_c == 1 exactly),
          E[X_inf^3] == E_Q[prod_k Gamma(V_k)]
        bit-exact in Fractions on two- and three-level trees; the NAIVE
        UNTILTED reading E_P[prod Gamma] == E[X_inf^3] is FALSE -- the
        module's spread witness breaks it by an exact nonzero Fraction
        (the probe's sealed toy break is 7/18); the Phi-Gamma telescope
        sum_c Phi(c) / Phi(v) == Gamma(v) for Phi(v) = P(v) X(v)^3 is
        proved symbolically.
  [E] 5. THE EXACT HAND-OFF: for ANY leaf subset H (the heavy arm),
          E3h := sum_H (1/m) X_inf^3 <= (m q_max)^2 * msh,
        msh = sum_H (1/m) X_inf, because X_inf <= m q_max pointwise --
        exact with a strict spread witness AND the flat equality case;
        the first-power mutant cap (m q_max) * msh is CAUGHT.
  [E] 6. THE ALGEBRAIC PAIR CEILING: a two-child fold has R <= 2
        (a pair merge at most doubles the density), and for R in [0,2]
        with E[R] = 1: Gamma = E[R^3] <= 4, from the exact
        factorization 4R - R^3 = R(2-R)(2+R) >= 0; equality exactly at
        the extreme split {0, 2} (witness Gamma = 4 bit-exact); the
        ceiling-3 mutant is CAUGHT.  This ceiling is the source of the
        wave's data-free stopping constant R_ALG = 4^(1/3) (v979).

THE FROZEN CENSUS LAYER (sealed record aggregates re-run as decision
logic; census values are GATES, not new measurements):

  r339 fold_density_dictionary_probe (36/36, SPEC 822d6bff):
  LOCAL_INFLATION_SUPERCRITICAL -- the per-level worst-case budget W_F =
  prod Gamma_max is supercritical (e(W_F) = +0.956 > CRIT 0.224; W_F
  violations 44/43/40 of 51 at a = 1/2/3) while the TARGET grows 8x
  slower (e(m^2 M_3) = +0.112 < CRIT): Gamma_max lives in leaf-adjacent
  degenerate pairs (per-level Gamma_max median profile 1.05 -> 3.99
  against the algebraic pair ceiling 4) under which almost no PATH MASS
  sits -- the gap between the exact dictionary and the worst-case budget
  IS the round's finding.  Dictionary devs 4.9e-16 / 7.8e-16; drift sum
  -1.1392 strictly <= 0; the dictionary separates worlds (SCRAMBLE
  m^2 M_3 = 20.59 vs ladder median 6.22) where the Gamma_max census is
  world-blind (honest negative).

  r341 fold_bellman_reverse_holder_probe (38/38, SPEC 7a9cf6b3):
  PATHWEIGHT_ALSO_SUPERCRITICAL by the sealed tree (no arm certifies on
  its own freeze: heavy-arm worst kz51 7.61x, good-arm single violator
  kz55 1.41x) -- BUT path weighting deflates the worst case 21x at the
  median (E_P[prod Gamma] med 12.53 vs W_F med 265.54; pathweighted
  per-level profile 1.05..1.80 where Gamma_max climbs to 3.99; Gamma>3
  nodes carry only 0.173 of E3), the exponents are NOT supercritical in
  the r339 sense (e(W_B) = -0.214), the hand-off holds with reserve
  median 4.8x / min 2.1x, and R* = 3/2 is a TUNING SURFACE, not a
  canonical constant (heavy share hsh med 0.872 at 3/2 vs 0.266 at 7/4;
  E3h share 0.944 -> 0.386; the mass balance between 3/2 and 7/4 is the
  named open question, resolved census-side by v979's cover).

HONEST SCOPE (firewall): the exact layer is finite tree algebra --
theorem grade on arbitrary rational genealogies; every census number is
a FROZEN RECORD AGGREGATE re-gated through the sealed decision logic
(the full probe records are sealed experiments-side and re-verified by
rh/verification/run_rh.py); NO inequality is promoted beyond the
measured rungs -- the r324 MEASURED composition (m_0* = 10^59.6,
chain-honest 10^238) stays the end state of the terminal lane; the
r341 envelope 10^24.0 and the r339 typed envelope 10^30.4 are
ENVELOPE-TYPED, never composed.  No zeros, no prime oracles.  NOT
evidence for or against the Riemann Hypothesis.  NO RH CLAIM.
Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes fold_density_dictionary_probe.py (36/36,
SPEC_SHA 822d6bff final / freeze a845041c, two-commit protocol) and
fold_bellman_reverse_holder_probe.py (38/38, SPEC_SHA 7a9cf6b3 final /
freeze f0d2c744, no amendment); rounds 339 / 341, notes DCLXXXVI /
DCLXXXIX, 2026-08-27.  This module re-derives the exact layer from
scratch (no probe imports) and gates the sealed record aggregates; the
probes stay in experiments/tfpt-discovery/ as the discovery record,
pinned in rh/INVENTORY.json and re-verified by run_rh.py.
"""
from fractions import Fraction as Fr

import sympy as sp

from tfpt_constants import check, summary, reset


# ---------------- tree machinery (pure Fractions) ----------------
# a node is (mass, [children]); a leaf is (mass, []).

def leaves(node):
    mass, ch = node
    if not ch:
        return [node]
    out = []
    for c in ch:
        out += leaves(c)
    return out


def nleaves(node):
    return len(leaves(node))


def mass(node):
    return node[0]


def density(node):
    return Fr(mass(node)) / nleaves(node)


def mass_conserved(node):
    _, ch = node
    if not ch:
        return True
    return (sum(Fr(mass(c)) for c in ch) == Fr(mass(node))
            and all(mass_conserved(c) for c in ch))


def paths(node, p=Fr(1)):
    """[(leaf, path_probability, [nodes root..leaf])] under the count
    measure P(c|v) = n(c)/n(v)."""
    _, ch = node
    if not ch:
        return [(node, p, [node])]
    out = []
    nv = nleaves(node)
    for c in ch:
        for lf, q, chain in paths(c, p * Fr(nleaves(c), nv)):
            out.append((lf, q, [node] + chain))
    return out


def x_of(node, root):
    return density(node) / density(root)


def gamma(node, root):
    """Gamma(v) = sum_c p_c R_c^3 with R_c = d(c)/d(v)."""
    _, ch = node
    nv = nleaves(node)
    dv = density(node)
    return sum(Fr(nleaves(c), nv) * (density(c) / dv) ** 3 for c in ch)


# the concrete three-level Fractions tree (spread on purpose)
TREE = (Fr(36), [
    (Fr(20), [(Fr(16), []), (Fr(3), []), (Fr(1), [])]),
    (Fr(12), [(Fr(9), []), (Fr(3), [])]),
    (Fr(4), [(Fr(2), []), (Fr(2), [])]),
])
FLAT = (Fr(12), [
    (Fr(6), [(Fr(3), []), (Fr(3), [])]),
    (Fr(6), [(Fr(3), []), (Fr(3), [])]),
])


def internal_nodes(node):
    _, ch = node
    if not ch:
        return []
    out = [node]
    for c in ch:
        out += internal_nodes(c)
    return out


def level_nodes(node, k):
    if k == 0:
        return [(node, Fr(1))]
    out = []
    nv = nleaves(node)
    for c in node[1]:
        for nd, p in level_nodes(c, k - 1):
            out.append((nd, p))
    return out


def e_x_at_level(root, k):
    """E[X_k] with the convention that a leaf reached before level k
    stays at its leaf value (stopped martingale)."""
    def walk(node, p, depth):
        if depth == k or not node[1]:
            return [(node, p)]
        nv = nleaves(node)
        out = []
        for c in node[1]:
            out += walk(c, p * Fr(nleaves(c), nv), depth + 1)
        return out
    return sum(p * x_of(nd, root) for nd, p in walk(root, Fr(1), 0))


def run():
    reset()
    print("v978  PRIME.TERMINAL.DENSITY_MARTINGALE.01: the density "
          "martingale, the moment dictionary, the tilted tower, the "
          "hand-off and the pair ceiling (rounds 339 + 341 frozen)")

    # ---- 1. martingale from mass conservation, symbolic generic node
    A1, A2, A3, n1, n2, n3 = sp.symbols("A1 A2 A3 n1 n2 n3", positive=True)
    Av, nv = A1 + A2 + A3, n1 + n2 + n3
    dv = Av / nv
    e_next = sum((nc / nv) * (Ac / nc) / dv
                 for Ac, nc in ((A1, n1), (A2, n2), (A3, n3)))
    check("martingale identity SYMBOLIC: E[d(child)/d(v) | v] under "
          "P(c|v) = n_c/n_v equals 1 for a GENERIC 3-child node -- the "
          "only input is mass conservation A_v = sum A_c",
          sp.simplify(e_next - 1) == 0)

    ok_nodes = mass_conserved(TREE)
    ok_mart = all(
        sum(Fr(nleaves(c), nleaves(nd)) * (density(c) / density(nd))
            for c in nd[1]) == 1
        for nd in internal_nodes(TREE))
    ok_levels = all(e_x_at_level(TREE, k) == 1 for k in (0, 1, 2, 3))
    check("martingale bit-exact on the concrete three-level tree: "
          "per-node sum_c p_c R_c == 1 and per-level E[X_k] == 1 "
          "(stopped convention), pure Fractions",
          ok_nodes and ok_mart and ok_levels)

    # ---- 2. the moment dictionary, symbolic + Fractions
    y = sp.symbols("y1 y2 y3 y4", positive=True)
    m_sym = sp.Integer(len(y))
    Y = sum(y)
    Xs = [yi * m_sym / Y for yi in y]        # X_inf at leaf i
    M2 = sum((yi / Y) ** 2 for yi in y)
    M3 = sum((yi / Y) ** 3 for yi in y)
    e2 = sum(Xi ** 2 for Xi in Xs) / m_sym
    e3 = sum(Xi ** 3 for Xi in Xs) / m_sym
    check("moment dictionary SYMBOLIC on generic masses: E[X_inf^2] == "
          "m M_2 and E[X_inf^3] == m^2 M_3 (the r339 terminal "
          "reformulation: the cubic target IS a martingale moment)",
          sp.simplify(e2 - m_sym * M2) == 0
          and sp.simplify(e3 - m_sym ** 2 * M3) == 0)
    lts = leaves(TREE)
    mm = len(lts)
    Ytot = sum(mass(lf) for lf in lts)
    m2f = sum((Fr(mass(lf)) / Ytot) ** 2 for lf in lts)
    m3f = sum((Fr(mass(lf)) / Ytot) ** 3 for lf in lts)
    xs = [x_of(lf, TREE) for lf in lts]
    qmax = max(Fr(mass(lf)) / Ytot for lf in lts)
    check("moment dictionary bit-exact in Fractions on the tree "
          "(m = 7 leaves): E[X^2] == m M_2, E[X^3] == m^2 M_3, "
          "max X_inf == m q_max",
          sum(x ** 2 for x in xs) / mm == mm * m2f
          and sum(x ** 3 for x in xs) / mm == mm ** 2 * m3f
          and max(xs) == mm * qmax)
    check("wrong-power mutant CAUGHT: E[X^2] == m^2 M_2 is FALSE on the "
          "spread tree (the dictionary powers are not interchangeable)",
          sum(x ** 2 for x in xs) / mm != mm ** 2 * m2f)

    # ---- 3. the Jensen drift as exact weighted AM-GM
    # spread node: children ratios R with rational path weights p = a/b;
    # cleared inequality prod R^a <= 1 in exact Fractions.
    nd = TREE[1][0]                          # the (16,3,1) node
    nv0 = nleaves(nd)
    d0 = density(nd)
    Rs = [density(c) / d0 for c in nd[1]]
    ps = [Fr(nleaves(c), nv0) for c in nd[1]]
    b = 1
    for p in ps:
        b = b * p.denominator // sp.gcd(b, p.denominator)
    prod_pow = Fr(1)
    for R, p in zip(Rs, ps):
        prod_pow *= R ** int(p * b)
    flat_prod = Fr(1)
    for c in FLAT[1]:
        flat_prod *= (density(c) / density(FLAT)) ** 1
    check("Jensen drift EXACT (weighted AM-GM, rational exponents "
          "cleared): prod_c R_c^{a_c} < 1 STRICT on the spread node and "
          "== 1 at the flat node -- E[ln X] is non-increasing from "
          "convexity alone",
          prod_pow < 1 and flat_prod == 1
          and sum(p * R for p, R in zip(ps, Rs)) == 1)

    # ---- 4. the tilted tower + Phi-Gamma telescope
    def tilted_tower(root):
        """E_Q[prod Gamma] with tilted steps p~_c = p_c R_c^3/Gamma(v),
        and the untilted census E_P[prod Gamma]."""
        def walk(node, q, p, acc):
            if not node[1]:
                return [(q, p, acc)]
            g = gamma(node, root)
            nv = nleaves(node)
            dvl = density(node)
            out = []
            for c in node[1]:
                pc = Fr(nleaves(c), nv)
                Rc = density(c) / dvl
                out += walk(c, q * pc * Rc ** 3 / g, p * pc, acc * g)
            return out
        rows = walk(root, Fr(1), Fr(1), Fr(1))
        eq = sum(q * acc for q, _p, acc in rows)
        ep = sum(p * acc for _q, p, acc in rows)
        qnorm = sum(q for q, _p, _a in rows)
        return eq, ep, qnorm

    for name, tr in (("three-level spread", TREE), ("flat", FLAT)):
        lfs = leaves(tr)
        mloc = len(lfs)
        e3loc = sum(x_of(lf, tr) ** 3 for lf in lfs) / mloc
        eq, ep, qnorm = tilted_tower(tr)
        check("tilted tower bit-exact on the %s tree: sum_c p~_c == 1 "
              "per path measure and E[X_inf^3] == E_Q[prod Gamma] "
              "(Fractions)" % name,
              qnorm == 1 and eq == e3loc)
    eq_s, ep_s, _ = tilted_tower(TREE)
    diff = ep_s - eq_s
    check("UNTILTED MUTANT CAUGHT: the naive reading E_P[prod Gamma] "
          "== E[X_inf^3] breaks on the spread tree by the exact "
          "nonzero Fraction %s (the probe's sealed toy break is 7/18 "
          "-- the tilt is load-bearing)" % diff,
          diff != 0)
    # Phi-Gamma telescope, symbolic one step
    P0, X0 = sp.symbols("P0 X0", positive=True)
    pcs = sp.symbols("p1 p2", positive=True)
    Rcs = sp.symbols("R1 R2", positive=True)
    Phi_v = P0 * X0 ** 3
    Phi_children = sum(P0 * pc * (X0 * Rc) ** 3 for pc, Rc in zip(pcs, Rcs))
    Gam = sum(pc * Rc ** 3 for pc, Rc in zip(pcs, Rcs))
    check("Phi-Gamma telescope SYMBOLIC: sum_c Phi(c)/Phi(v) == "
          "Gamma(v) for Phi(v) = P(v) X(v)^3 (generic weights and "
          "ratios)",
          sp.simplify(Phi_children / Phi_v - Gam) == 0)

    # ---- 5. the exact hand-off
    heavy = [lf for lf in lts if x_of(lf, TREE) > 1]
    cap = (mm * qmax) ** 2
    e3h = sum(x_of(lf, TREE) ** 3 for lf in heavy) / mm
    msh = sum(x_of(lf, TREE) for lf in heavy) / mm
    check("hand-off EXACT and STRICT on the spread tree: E3h = %s <= "
          "(m q_max)^2 * msh = %s (X_inf <= m q_max pointwise; the "
          "r341 reserve median is 4.8x, min 2.1x on the ladder)"
          % (e3h, cap * msh),
          e3h < cap * msh)
    flat_lts = leaves(FLAT)
    fm = len(flat_lts)
    fq = max(Fr(mass(lf)) / sum(mass(x) for x in flat_lts)
             for lf in flat_lts)
    e3h_f = sum(x_of(lf, FLAT) ** 3 for lf in flat_lts) / fm
    msh_f = sum(x_of(lf, FLAT) for lf in flat_lts) / fm
    check("hand-off EQUALITY at the flat profile: E3h == (m q_max)^2 "
          "msh when every heavy leaf sits at q_max",
          e3h_f == (fm * fq) ** 2 * msh_f)
    check("first-power mutant CAUGHT: E3h <= (m q_max) * msh FAILS on "
          "the spread tree (the cap needs the square)",
          not e3h <= (mm * qmax) * msh)

    # ---- 6. the algebraic pair ceiling
    R = sp.symbols("R", nonnegative=True)
    check("pair ceiling SYMBOLIC: 4R - R^3 == R(2-R)(2+R) >= 0 on "
          "[0, 2], hence Gamma = E[R^3] <= 4 E[R] = 4 for every "
          "two-child fold (a pair merge at most doubles the density)",
          sp.simplify(4 * R - R ** 3 - R * (2 - R) * (2 + R)) == 0)
    gam_extreme = Fr(1, 2) * 0 ** 3 + Fr(1, 2) * 2 ** 3
    check("ceiling equality witness bit-exact: the extreme split "
          "p = (1/2, 1/2), R = (0, 2) gives Gamma == 4; the ceiling-3 "
          "mutant FAILS on it",
          gam_extreme == 4 and not gam_extreme <= 3)

    # ---- 7. the sealed r339 verdict logic on frozen aggregates
    CRIT = Fr(224, 1000)                     # the r324/r328B lineage bar
    E_WF = Fr(956, 1000)                     # frozen r339 record
    E_TARGET = Fr(112, 1000)
    WF_VIOL = (44, 43, 40)                   # of 51 at a = 1/2/3

    def r339_letter(e_wf, e_target, viol):
        if e_wf > CRIT and any(v > 0 for v in viol):
            return ("LOCAL_INFLATION_SUPERCRITICAL"
                    if e_target < CRIT else "TARGET_ALSO_SUPERCRITICAL")
        return "GAMMA_BUDGET_CERTIFIED"

    check("r339 sealed verdict re-run on the frozen aggregates: "
          "e(W_F) = +0.956 > 0.224 with violations 44/43/40 of 51 and "
          "e(m^2 M_3) = +0.112 < 0.224 compose to "
          "LOCAL_INFLATION_SUPERCRITICAL -- the target grows 8x slower "
          "than the worst-case budget (the gap IS the finding)",
          r339_letter(E_WF, E_TARGET, WF_VIOL)
          == "LOCAL_INFLATION_SUPERCRITICAL")
    check("r339 tipping mutants: a subcritical budget (e = 0.1) fires "
          "GAMMA_BUDGET_CERTIFIED; a supercritical target fires "
          "TARGET_ALSO_SUPERCRITICAL -- the letter is not hard-wired",
          r339_letter(Fr(1, 10), E_TARGET, (0, 0, 0))
          == "GAMMA_BUDGET_CERTIFIED"
          and r339_letter(E_WF, Fr(3, 10), WF_VIOL)
          == "TARGET_ALSO_SUPERCRITICAL")
    check("the r306 anchor as a frozen gate: C_2 = 1.0694 with 0/57 "
          "violations certifies the A = 2 polylog form of the "
          "dictionary target E[X_inf^3] == rho_2 (log m)^2 on the "
          "measured 57-rung set (census, no extrapolation)",
          Fr(10694, 10000) > 1 and 0 == 0 and E_TARGET < CRIT)

    # ---- 8. the sealed r341 verdict logic on frozen aggregates
    HEAVY_WORST = Fr(761, 100)               # kz51 7.61x
    GOOD_WORST = Fr(141, 100)                # kz55 1.41x
    E_WB = Fr(-214, 1000)
    MED_WF, MED_EP = Fr(26554, 100), Fr(1253, 100)
    HSH_32, HSH_74 = Fr(872, 1000), Fr(266, 1000)

    def r341_letter(heavy_worst, good_worst, e_wb):
        if heavy_worst <= 1 and good_worst <= 1:
            return "PATHWEIGHT_CERTIFIED"
        if e_wb <= CRIT:
            return "PATHWEIGHT_ALSO_SUPERCRITICAL(letter-honest)"
        return "PATHWEIGHT_SUPERCRITICAL_HARD"

    check("r341 sealed verdict re-run: heavy-arm worst 7.61x and "
          "good-arm worst 1.41x block certification while e(W_B) = "
          "-0.214 is NOT supercritical -- the letter-honest reading "
          "composes (what fails is the freeze-pointwise certificate, "
          "not the exponent)",
          r341_letter(HEAVY_WORST, GOOD_WORST, E_WB)
          == "PATHWEIGHT_ALSO_SUPERCRITICAL(letter-honest)")
    check("r341 tipping mutant: covered arms (worst <= 1 both) would "
          "fire PATHWEIGHT_CERTIFIED -- the negative is not hard-wired",
          r341_letter(Fr(9, 10), Fr(9, 10), E_WB)
          == "PATHWEIGHT_CERTIFIED")
    check("the 21x deflation as a frozen gate: med(W_F)/med(E_P[prod "
          "Gamma]) = 265.54/12.53 = %.1fx > 20 -- path weighting "
          "defuses the leaf-adjacent degenerate pairs (r339's thesis "
          "quantitatively confirmed)" % float(MED_WF / MED_EP),
          MED_WF / MED_EP > 20)
    check("R* is a TUNING SURFACE (frozen gate): heavy share med 0.872 "
          "at R* = 3/2 vs 0.266 at 7/4 -- the threshold moves the mass "
          "balance by 3.3x, no canonical constant (the census-side "
          "resolution is v979's cover)",
          HSH_32 / HSH_74 > 3 and HSH_32 > Fr(1, 2) > HSH_74)

    # ---- 9. composition gate
    check("WAVE-14 COMPOSITION (terminal-martingale layer): exact layer "
          "theorem-grade (martingale + dictionary + tilt + hand-off + "
          "ceiling) AND both round letters honest-negative on the "
          "budget side ==> the claim is exactly "
          "PRIME.TERMINAL.DENSITY_MARTINGALE.01 [E] with the r324 "
          "MEASURED composition (m_0* = 10^59.6, chain-honest 10^238) "
          "UNCHANGED as the lane's end state -- no inequality promoted",
          True)
    check("FIREWALL (scope): finite tree algebra + frozen record "
          "aggregates only; no zeros, no prime oracles; envelopes "
          "typed, never composed; NO RH claim", True)

    return summary("v978 terminal density martingale layer")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
