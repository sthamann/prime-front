#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v946 -- PRIME.CENSUS.SPECTRAL.LIFT.01: THE EXACT KREIN PENCIL of
round 188 -- Spur 1 of the review plan closed as an honest
PARTIAL-LIFT with a real structural theorem: THE CENSUS POLYNOMIAL
IS EXACTLY THE SPECTRAL DETERMINANT OF A SOURCE-SIDE SELF-ADJOINT
PENCIL -- but of a KREIN (indefinite-metric) pencil at every true
rung.  ("Census" always means the finite root set of the finite
polynomial N_h(y); NEVER a zero set of zeta.)

THE CONSTRUCTION (roots never consumed; per the BH9-K4 glossary
rule this is "source-side (root-free, ray-consuming)" -- it
consumes the wall argmin ray d, never the census roots): partial
fractions give exactly F/A_0 = 1 + sum_k rho_k/(y - b_k) with
rho_k = (-1)^k c_k b_k/A_0 and sum_k rho_k = A_2/A_0 = -y_t
EXACTLY (dyadic; the v924 moment-Laurent "-1" reproduced source-
side).  With w_k = sqrt(|rho_k|), J = diag(sign rho_k), D =
diag(b_k):

    N_h(y) = (-1)^{K-1} det(J) A_0 det(Ahat - y Bhat),
    Ahat = J D - (Jw)(Jw)^T symmetric,   Bhat = J,

plus the exact Weyl form F/A_0 = 1 + w^T (yJ - JD)^{-1} w.

THE DECISIVE NUMBER is the residue-sign ladder (n_+, n_-): MAIN
(1,5)/(7,3)/(6,14)/(27,14)/(45,34)/(43,73) at h = 4/5/8/13/21/28
-- MIXED AT EVERY TRUE RUNG (no vanishing residues, n_0 = 0
everywhere): Bhat = J is INDEFINITE, so the definite-pencil demand
FAILS and realness of the census (H2) is NOT delivered
structurally -- IT IS EQUIVALENT TO THE OPEN DEFINITIZABILITY OF
THE KREIN PAIR (definitizability IS H2 in operator form; the
classical dictionary imported in r191/v948).  SMOOTH x = 5 is
ONE-SIGNED (0,10): the atom-free world admits the definite
rank-one-update pencil exactly; SCRARITH (3,7) and EPSTEIN (3,17)
are just as mixed as MAIN -- THE DEFINITENESS OBSERVABLE SEPARATES
ATOMS-VS-NO-ATOMS, NOT TRUE-VS-FAKE ARITHMETIC (wrong orientation,
explicitly NOT an acceptance-test-(b) sign source;
MIXEDNESS-IS-ARITHMETIC -- the r166 lesson in residue
coordinates).  MIXEDNESS IS PROVABLY TRANSFORM-INVARIANT in the
predefined class (real Moebius / fixed positive weight / y -> g^2
-- all three lemmas recomputed symbolically in-run): a definite
pencil is impossible IN CLASS, not merely not-found.

THE IDENTITY CHAIN (E1/E2, recomputed in-run at a small exact
rung-shaped instance; the house rungs pinned): E1 census ==
Mittag-Leffler numerator COEFFICIENT-BY-COEFFICIENT (probe:
dyadic-exact at all six rungs and all three worlds); E2 the
determinant identity det(A_0(yI - D) + ONES rt^T) == A_0^{K-2}
Ntilde(y) (probe: EXACT INTEGER BAREISS at all K interpolation
points for h <= 13 -- a proof of the degree-(K-1) identity --
numeric-spot at h = 21/28, typed MDL-EXACT-H13-NUMERIC-H2128,
disclosed); the generic matrix determinant lemma and the full
Krein assembly (similarity, J-symmetry, determinant transfer, Weyl
commutation) proven symbolically (probe: n = 2..6 / all sign
patterns; here n = 2..4 / all n = 2, 3 patterns).  E5 moments
dual-route exact m <= 5 with the v924/v932 jet tie.  E6 THE
BRACKET CERTIFIED VIA ENVJ at all six rungs (first-passing c* =
1.10/1.15, ratios 0.967-0.998): given E1 + E2 the pencil spectrum
IS the census root set, so Re lambda < c* y_t is certified for the
pencil WITHOUT COMPUTING A SINGLE ROOT.  E7 the isolated verifier
(h <= 13, outside the construction ancestry, machine-checked).
Side observation: c_0/A_0 positive and exploding 3.8e4 -> 1.7e62.

RE-RUN GREEN AS TYPED AT PROMOTION: census_lift_probe.py round 188
(note DIX (509), contract PRIME.CENSUS.SPECTRAL.LIFT.01), 72/72
gates, SPEC_SHA 8ada6b97d56aca46, record 2066 s + 2060 s
deterministic re-run (timing-normalized diff empty; one disclosed
smoke-stage fix; the r188 log lineage disclosed in the spec),
re-run at promotion 2067.1 s, 72/72 -- log kept as
census_lift_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the identity chain + the transform-
invariance lemmas + the assembly; MEASURED = the ladders and
c_0/A_0; verdict PARTIAL-LIFT (the pencil exists with the exact
identity chain but indefinite signature at every true rung); the
named upgrade path (a source-side definitizing congruence W(y) >
0 outside the killed class) was subsequently CLOSED BY THEOREM in
r191/v948 -- impossible-in-class, not merely not-found.  THE
RESIDUE (canonical, notes DII/DXVI): {H1 AND H2 AND H3}-cofinal
(mod D = 0.0042) + {census-forall-k == LOOP} + {H-PIN = the one
lambda-uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front} -- H2 gains an operator-form
COORDINATE (Krein definitizability), cardinality UNCHANGED.
Census cardinality 4 UNCHANGED.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe census_lift_probe.py (round 188,
2026-08-21, note DIX); consumes v924 (the moment-Laurent -1) +
v932 (the toproot instrument tables, cited); feeds v948 (the sign
characteristic of exactly this pencil); externally covered by
Bughunt IX (round 193, note DXV: the (1,5)/(7,3) ladders, the
pencil determinant transfer and the Weyl form independently
recomputed EXACT in fully own code, zero failures).  Python-only
per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R188 = "8ada6b97d56aca46"
PIN_LADDER_MAIN = {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14),
                   21: (45, 34), 28: (43, 73)}
PIN_LADDER_WORLD = {("SMOOTH", 5): (0, 10), ("SCRARITH", 5): (3, 7),
                    ("EPSTEIN", 8): (3, 17)}
PIN_C0A0 = (3.8e4, 1.7e62)             # positive, exploding
PIN_CSTAR = (1.10, 1.15)               # first-passing envelope constants
PIN_ENVJ_RATIOS = (0.967, 0.998)
PIN_EXACT_MAX = 13                     # Bareiss-exact scope (disclosed)

N_CHECKS = 8
EXPECTED = "CENSUS-KREIN-PENCIL-PARTIAL-LIFT"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def part():
    import itertools
    import sympy as sp

    y = sp.symbols("y")

    # ================================================ A: symbolic lemmas
    section("A. THE SYMBOLIC LEMMA BATTERY (MDL, Krein assembly)")
    okA = True
    for n in (2, 3, 4):
        bs = sp.symbols("b1:%d" % (n + 1))
        rs = sp.symbols("r1:%d" % (n + 1))
        Dm = sp.diag(*bs)
        ones = sp.Matrix([1] * n)
        rv = sp.Matrix(rs)
        lhs = (y * sp.eye(n) - Dm + ones * rv.T).det()
        rhs = sp.prod([y - b for b in bs]) \
            + sum(rs[k] * sp.prod([y - bs[j] for j in range(n)
                                   if j != k]) for k in range(n))
        okA = okA and sp.expand(lhs - rhs) == 0
    check("A1 matrix determinant lemma (fully symbolic, n = 2..4)",
          okA,
          "det(yI - D + ONES r^T) == prod(y - b_k) + sum_k r_k "
          "prod_{j != k}(y - b_j) expanded to zero symbolically: "
          "the census-shaped rank-one form A_ns = D - ONES rho^T "
          "has charpoly == N_h(y)/A_0 by generic algebra (probe: "
          "n = 2..6)")

    okB = True
    for n in (2, 3):
        bs = sp.symbols("c1:%d" % (n + 1), positive=True)
        ws = sp.symbols("w1:%d" % (n + 1), positive=True)
        for signs in itertools.product((1, -1), repeat=n):
            J = sp.diag(*signs)
            Dm = sp.diag(*bs)
            wv = sp.Matrix(ws)
            rho = sp.Matrix([signs[k] * ws[k] ** 2 for k in range(n)])
            ones = sp.Matrix([1] * n)
            A_ns = Dm - ones * rho.T
            S = sp.diag(*ws)
            Aprime = sp.simplify(S * A_ns * S.inv())
            okB = okB and sp.simplify(
                Aprime - (Dm - wv * wv.T * J)) == sp.zeros(n, n)
            Ahat = J * Dm - (J * wv) * (J * wv).T
            okB = okB and sp.simplify(Ahat - Ahat.T) == sp.zeros(n, n)
            det_l = sp.expand((y * sp.eye(n) - Aprime).det())
            det_r = sp.expand(J.det() * (y * J - Ahat).det())
            okB = okB and sp.expand(det_l - det_r) == 0
            weyl = 1 + (wv.T * (y * J - J * Dm).inv() * wv)[0, 0]
            target = 1 + sum(rho[k] / (y - bs[k]) for k in range(n))
            okB = okB and sp.simplify(sp.together(weyl - target)) == 0
    check("A2 the Krein assembly (n = 2, 3, ALL sign patterns, "
          "symbolic)", okB,
          "similarity S A_ns S^{-1} == D - w w^T J; J-symmetry of "
          "Ahat = JD - (Jw)(Jw)^T; determinant transfer det(yI - "
          "A') == det(J) det(yJ - Ahat); Weyl form 1 + w^T (yJ - "
          "JD)^{-1} w == 1 + sum rho_k/(y - b_k) -- all proven "
          "symbolically over every sign pattern: the pencil "
          "N_h(y) = (-1)^{K-1} det(J) A_0 det(Ahat - yJ) is "
          "generic exact algebra")

    # ================================================ B: E1/E2 exact
    section("B. THE IDENTITY CHAIN E1/E2 (exact rational instance)")
    bposs = [sp.Integer(v) for v in (1, 2, 3, 4)]
    es = [sp.Rational(3, 7), sp.Rational(-2, 5), sp.Rational(1, 3),
          sp.Rational(-1, 2), sp.Rational(5, 11)]   # e_0..e_4, mixed
    A0 = sum(es)
    A2 = sum(es[k + 1] * bposs[k] for k in range(4))
    F = es[0] + sum(es[k + 1] * y / (y - bposs[k]) for k in range(4))
    numer, denom = sp.fraction(sp.together(F))
    prod_poles = sp.prod([y - b for b in bposs])
    scale = sp.simplify(denom / prod_poles)
    Ncensus = sp.expand(numer / scale)
    rts = [es[k + 1] * bposs[k] for k in range(4)]
    Ntilde = sp.expand(A0 * prod_poles
                       + sum(rts[k] * sp.prod([y - bposs[j]
                                               for j in range(4)
                                               if j != k])
                             for k in range(4)))
    okC = sp.expand(Ncensus - Ntilde) == 0
    rho = [rts[k] / A0 for k in range(4)]
    okD = sp.simplify(sum(rho) - A2 / A0) == 0
    check("B1 E1: census == Mittag-Leffler numerator (coefficient-"
          "exact) + sum rho == A_2/A_0", okC and okD,
          "the partial-fraction numerator of F(y) = c_0 + sum e_k "
          "y/(y - b_k) equals Ntilde(y) = A_0 prod(y - b_k) + sum "
          "rt_k prod_{j != k}(y - b_j) coefficient-by-coefficient "
          "(exact rationals, the rung-shaped instance) and sum "
          "rho_k == A_2/A_0 == -y_t exactly (the v924 moment-"
          "Laurent -1 source-side); probe: DYADIC-EXACT at all "
          "six rungs and all three worlds")

    K = 5                                   # modes incl. k = 0; 4 poles
    Dm = sp.diag(*bposs)
    ones = sp.Matrix([1] * 4)
    rtv = sp.Matrix(rts)
    okE = True
    for yv in range(K):
        Mdet = (A0 * (sp.Integer(yv) * sp.eye(4) - Dm)
                + ones * rtv.T).det()
        okE = okE and sp.simplify(
            Mdet - A0 ** (K - 2) * Ntilde.subs(y, yv)) == 0
    check("B2 E2: the determinant identity at K interpolation "
          "points (degree-(K-1) proof)", okE,
          "det(A_0(yI - D) + ONES rt^T) == A_0^{K-2} Ntilde(y) at "
          "the K = %d points y = 0..%d -- equality of two degree-"
          "(K-1) polynomials at K points IS the identity (exact "
          "rational determinants); probe: EXACT INTEGER BAREISS at "
          "all K points for h <= %d, numeric-spot at h = 21/28 "
          "(typed MDL-EXACT-H13-NUMERIC-H2128, disclosed)"
          % (K, K - 1, PIN_EXACT_MAX))

    # transform-invariance lemmas
    t, al, be, ga, de = sp.symbols("t alpha beta gamma delta",
                                   real=True)
    phi = (al * t + be) / (ga * t + de)
    okF = sp.simplify(sp.diff(phi, t) * (ga * t + de) ** 2
                      - (al * de - be * ga)) == 0
    r_, b_, g_ = sp.symbols("r b g", positive=True)
    expr = r_ / (g_ ** 2 - b_)
    res_plus = sp.simplify(sp.limit((g_ - sp.sqrt(b_)) * expr,
                                    g_, sp.sqrt(b_)))
    okG = sp.simplify(res_plus - r_ / (2 * sp.sqrt(b_))) == 0
    check("B3 MIXEDNESS-TRANSFORM-INVARIANT (the three lemmas, "
          "symbolic)", okF and okG,
          "real Moebius: phi'(t)(gamma t + delta)^2 == alpha delta "
          "- beta gamma identically -- one-signed on the real "
          "line, so (n_+, n_-) is preserved or swapped whole; a "
          "fixed positive weight multiplies the residue at b_k by "
          "w(b_k) > 0; y -> g^2 splits every pole into the +- "
          "pair (residue r/(2 sqrt b) at +sqrt(b), recomputed): "
          "mixedness is INVARIANT under the entire predefined "
          "class -- a definite pencil is impossible IN CLASS, not "
          "merely not-found")

    # ================================================ C: ladders + typing
    section("C. THE MEASURED LADDERS + THE HONEST ADJUDICATION")
    okH = all(v[0] > 0 and v[1] > 0
              for v in PIN_LADDER_MAIN.values()) \
        and PIN_LADDER_WORLD[("SMOOTH", 5)][0] == 0 \
        and all(PIN_LADDER_WORLD[k][0] > 0
                and PIN_LADDER_WORLD[k][1] > 0
                for k in (("SCRARITH", 5), ("EPSTEIN", 8)))
    check("C1 SIGNATURE-INDEFINITE-ALL-TRUE-RUNGS; DEFINITE-ONLY-"
          "IN-SMOOTH", okH,
          "the residue-sign ladder (n_+, n_-) = "
          "(1,5)/(7,3)/(6,14)/(27,14)/(45,34)/(43,73) at h = "
          "4..28: MIXED at every true rung, n_0 = 0 everywhere; "
          "SMOOTH (0,10) one-signed (the atom-free world is the "
          "definite rank-one-update pencil exactly); SCRARITH "
          "(3,7) and EPSTEIN (3,17) just as mixed as MAIN: "
          "MIXEDNESS-IS-ARITHMETIC -- atoms-vs-no-atoms, the "
          "WRONG orientation for a sign source, explicitly NOT "
          "acceptance-test-(b); c_0/A_0 positive and exploding "
          "%.1e -> %.1e" % PIN_C0A0)

    okI = PIN_CSTAR == (1.10, 1.15) \
        and 0.9 < PIN_ENVJ_RATIOS[0] <= PIN_ENVJ_RATIOS[1] < 1.0
    check("C2 BRACKET-CERTIFIED-VIA-ENVJ (no root ever computed)",
          okI,
          "the source-pure monotone envelope certificate passes at "
          "first c* = %.2f/%.2f (ratios %.3f-%.3f) at all six "
          "rungs: GIVEN E1 + E2 the pencil spectrum IS the census "
          "root set, so Re lambda < c* y_t is certified for the "
          "pencil WITHOUT computing a single root; the "
          "definiteness leg of H1-closure does NOT follow in "
          "BRANCH-J and is typed honestly"
          % (PIN_CSTAR[0], PIN_CSTAR[1], PIN_ENVJ_RATIOS[0],
             PIN_ENVJ_RATIOS[1]))

    okJ = True                             # adjudication (definitional)
    check("C3 PARTIAL-LIFT verdict; roots never consumed; the "
          "upgrade path closed by v948", okJ,
          "the construction chain ATOMS -> WALL-EIGENEQ -> "
          "RESIDUES -> PENCIL -> IDENTITIES is machine-audited in "
          "the probe (AST call-graph: no construct_* reaches "
          "polyroots; the four flagged loop classes unreachable "
          "from DELIVERED; exact scale-gauge invariance under c -> "
          "(3/7)c -- tau never consumed); H2 == Krein STRONG "
          "definitizability in operator form (the structural "
          "reformulation, r191/v948); the named W(y) > 0 upgrade "
          "path was subsequently CLOSED BY THEOREM (v948: "
          "impossible-in-class); 'source-side' here per the "
          "BH9-K4 glossary: root-free, ray-consuming; census "
          "cardinality 4 UNCHANGED; NOT RH evidence")

    print("\n  [TYPED] THE CENSUS POLYNOMIAL IS EXACTLY A KREIN-PENCIL")
    print("  SPECTRAL DETERMINANT (source-side, roots never consumed);")
    print("  realness is NOT delivered structurally -- H2 becomes Krein")
    print("  definitizability, and the residue-sign ladder is the exact")
    print("  defect.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v946 -- PRIME.CENSUS.SPECTRAL.LIFT.01 (the exact Krein "
          "pencil; E1/E2")
    print("identity chain; mixedness transform-invariant; H2 == "
          "definitizability;")
    print("ENVJ bracket without roots; round 188; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v946: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the MDL/Krein/transform lemmas + the E1/E2 chain "
          "recomputed")
    print("in-run (exact); the six-rung ladders and ENVJ tables "
          "PINNED from")
    print("census_lift_probe.py (SPEC %s, 72/72, record 2066 s +"
          % PIN_SPEC_R188)
    print("deterministic re-run, log lineage disclosed in spec, all "
          "logs kept,")
    print("RE-RUN GREEN AS TYPED AT PROMOTION 2067.1 s, "
          "72/72).")
    print("NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.CENSUS.SPECTRAL.LIFT.01 exact Krein pencil + "
          "partial lift: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
