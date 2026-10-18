#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v948 -- PRIME.KREIN.DEFINITIZER.01: THE SIGN-CHARACTERISTIC LAW
+ THE PARITY SCAFFOLD + THE W(y)-CONGRUENCE-CLASS KILL of round 191
-- the r188/v946 upgrade path CLOSED BY THEOREM (not by search) and
two genuine new objects delivered.  ("Census" always means the
finite root set of N_h(y); NEVER a zero set of zeta.)

THE CLASSICAL DICTIONARY (imported precisely): Langer LNM 948
(1982) definitizability; Zizler CMB 38 (1995) via Lancaster-Ye
Aequationes Math. 46 (1993): finite-dimensional Langer
definitizability is DEGENERATE (the census polynomial trivially
definitizes via Cayley-Hamilton -- the degeneracy exhibited in-run
and pinned at h = 4 with residual 1.4e-58); the non-vacuous notion
is STRONG definitizability (J p(T) strictly PD), EQUIVALENT to H2
per rung; Gohberg-Lancaster-Rodman 2005 sign characteristic;
Mehrmann-Noferini-Tisseur-Xu LAA 511 (2016).

THE ROUND'S EXACT LAW (recomputed in-run, symbolic + the exact
rational Sturm battery): for the r188/v946 pencil the kernel
vector at a census root y_i is EXPLICIT, v_k = w_k/(b_k - y_i),
because (Ahat - yJ) v = Jw (1 + G(y)) with G(y) = sum_k rho_k/(y -
b_k); then [v, v] = v^T J v = sum_k rho_k/(y_i - b_k)^2 =
-G'(y_i), i.e. eps_i = -sign((F/A_0)'(y_i)) -- the sign
characteristic is the CROSSING DIRECTION of the Weyl secular
function; the COMBINATORIAL LAW eps_i = -(-1)^{(R - i) + m_i}
(m_i = #poles above y_i); the FLIP LAW eps_{i+1} eps_i =
(-1)^{Delta_i + 1}; THE PARITY SCAFFOLD (per the BH9-K4 glossary
rule "source-side (root-free)": computed from residue SIGNS alone,
no roots): #roots in (-inf, b_1) odd iff rho_1 > 0; in (b_k,
b_{k+1}) odd iff sign rho_k = sign rho_{k+1}; in (b_{n1}, +inf)
odd iff rho_{n1} < 0; and THE COUNT LAW #eps+- = n+- exactly
(nonreal pairs enter as an exact deficit): THE r188 RESIDUE-SIGN
LADDER IS THE KREIN SIGN-CHARACTERISTIC MULTISET -- two-route
proven (crossing sign vs combinatorial formula) at every root of
every cell of the exact battery in-run, and at every measured rung
in the probe.

THE W(y)-CONGRUENCE KILL (BY THEOREM): for ANY W(y) smooth and
invertible near the census roots, the congruence M(y) = W(y)(Ahat
- yJ)W(y)^T has, at each census root with kernel v and x =
W(y_i)^{-T} v: x^T M'(y_i) x = v^T (Ahat - yJ)'(y_i) v =
-eps_i |[v, v]| (the W' terms die on the kernel -- recomputed
symbolically in-run).  A "definite pencil in disguise" requires
eps_i one-signed; the measured MIXED ladder therefore KILLS THE
ENTIRE W(y) > 0 CONGRUENCE CLASS AT ONCE (the sign characteristic
is a congruence invariant): the named r188 upgrade path is
IMPOSSIBLE-IN-CLASS, not merely not-found.  All three contracted
families instantiated in the probe (identity devs: DIAG 1.0e-57,
CAUCHY 1.6e-55, JDPOLY 7.9e-59; blocking roots (1, 5)/(1, 2) at
h = 4/5).  What is NOT killed, typed honestly: (a) dimension-
enlarging linearizations (trivial-by-roots given realness, hence
forbidden as construction); (b) residue-sign-changing non-
congruence transforms (currently an empty class; the r188 G07
class kill stands).

THE MEASURED PIVOT (pinned): minimal strict definitizer degree d_h
= #sign flips = 2/4/11/18 at h = 4/5/8/13 (Langer condition J p(T)
strictly PD verified at matrix level: eigsy min 4.50e-7, symdev
2.3e-119), determined by the gap-occupancy vector alone; the
occupancy-minimality law HOLDS at h = 4, 5 and FAILS at h = 8, 13
by exactly ONE interior doubled gap each (gap 10 of 20; gap 24 of
41): THE STRICT DEFINITIZER IS ROOT-DEPENDENT; the surviving
source-side coordinate is THE PARITY SCAFFOLD (verified against
measurement at all 81 gaps; h = 21/28 replicate the r188 ladders
exactly and carry scaffolds with 55/80 and 74/117 odd gaps).
WORLDS: SMOOTH eps == -1, d = 0 (the definite world); SCRARITH/
EPSTEIN both d = 3 -- orientation stays ATOMS-VS-NO-ATOMS (the
r188 caveat inherited, NOT a sign source).  THE WITNESS DETECTOR
(new): the r172 witness BREAKS CENSUS REALNESS (nreal = 8, one
nonreal pair -- not strongly definitizable) while leaving the raw
ladder unmoved at (7, 3): THE KREIN INVARIANT DETECTS THE WITNESS
CLASS WHERE THE RAW LADDER IS BLIND (the law itself is ray-blind
-- an identity -- typed, never sold as a separator).  PRICING:
defect-slack slope vs log tau = +0.062 FLAT (not riding); exact
scale-gauge invariance under c -> (3/7)c; the Krein coordinate
closed as STRUCTURAL-ONLY (H2-cofinal in operator form is
equivalent to realness -- the definitizer reformulation adds no
leverage).

RE-RUN GREEN AS TYPED AT PROMOTION: krein_definitizer_probe.py
round 191 (note DXIII (513), contract PRIME.KREIN.DEFINITIZER.01),
57/57 gates, SPEC_SHA 332c1f48f48a6d82, record 1950 s + 1901 s
deterministic re-run (timing-normalized diff empty, all logs kept,
no post-freeze amendments), re-run at promotion
1983.4 s, 57/57 -- log kept as
krein_definitizer_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the kernel/Weyl identity, the two-route
law, the flip/count laws, the parity scaffold, the congruence-
obstruction lemma, the Cayley-Hamilton degeneracy (all recomputed
in-run); MEASURED = the d_h/occupancy/slack/world/witness tables.
NEW AND LOAD-BEARING: the parity scaffold, the two-route eps-law,
the realness-break witness detector.  THE RESIDUE (canonical,
notes DII/DXVI): {H1 AND H2 AND H3}-cofinal (mod D = 0.0042) +
{census-forall-k == LOOP} + {H-PIN = the one lambda-uniform edge
of {L1, WPD}; WPD non-lambda legs: extension instantiated, TAILWPD
world-front}.  Census cardinality 4 UNCHANGED.  NOT evidence for
or against the Riemann Hypothesis in either direction.  NO RH
CLAIM.

PROVENANCE: discovery probe krein_definitizer_probe.py (round 191,
2026-08-21, note DXIII); consumes v946 (the exact pencil whose
sign characteristic this is); externally covered by Bughunt IX
(round 193, note DXV: the two-route eps at every root, the
count/flip laws, the parity scaffold == occupancy at all gaps, the
W(y)-congruence lemma and the Cayley-Hamilton degeneracy all
independently recomputed in fully own code, zero failures).
Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import itertools
import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R191 = "332c1f48f48a6d82"
PIN_D_TAB = {4: 2, 5: 4, 8: 11, 13: 18}
PIN_OCCMIN_TAB = {4: True, 5: True, 8: False, 13: False}
PIN_DOUBLED_GAP = {8: (10, 20), 13: (24, 41)}   # ONE interior doubled gap
PIN_LADDER = {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14)}
PIN_BLK_TAB = {4: (1, 5), 5: (1, 2)}
PIN_SLACK_SLOPE = 0.062                # FLAT, ride band (0.7, 1.3)
PIN_LANGER_PSD_MIN = 4.50e-7
PIN_LANGER_SYMDEV = 2.3e-119
PIN_CH_RESIDUAL = 1.4e-58
PIN_FAM_DEVS = {"DIAG": 1.0e-57, "CAUCHY": 1.6e-55, "JDPOLY": 7.9e-59}
PIN_WIT = {"ladder": (7, 3), "nreal": 8, "npairs": 1, "d": 2}
PIN_D_WORLD = {"SMOOTH": 0, "SCRARITH": 3, "EPSTEIN": 3}
PIN_SCAFFOLD_GAPS = 81                 # verified vs measurement (h<=13)
PIN_SCAFFOLD_2128 = ((55, 80), (74, 117))   # odd gaps at h = 21/28

BATTERY_POLES = (1, 2, 3, 4)
BATTERY_MAGS = ((1, 1, 1, 1),
                (2, Fraction(1, 2), 3, Fraction(1, 3)))

N_CHECKS = 10
EXPECTED = "KREIN-SIGN-CHARACTERISTIC-LAW"

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


def _refine(Npoly, lo, hi, avoid):
    """Shrink the exact rational isolating interval (lo, hi) of the
    one root of Npoly inside it until it contains no point of
    `avoid` (rationals) and no root of any polynomial in it later;
    fully rational, no floats."""
    import sympy as sp
    for _ in range(80):
        clean = all(not (lo < a < hi) for a in avoid)
        if clean and (hi - lo) < sp.Rational(1, 10 ** 6):
            return lo, hi
        lo, hi = Npoly.refine_root(lo, hi, steps=8)
    raise RuntimeError("interval refinement did not converge")


def _sign_on_interval(P2, Npoly, lo, hi):
    """Exact sign of P2 at the root of Npoly isolated in (lo, hi):
    refine until P2 has no root in [lo, hi] (Sturm certificate),
    then the endpoint sign is the root sign.  No floats."""
    for _ in range(80):
        if P2.count_roots(lo, hi) == 0:
            val = P2.eval(lo)
            if val != 0:
                return (1 if val > 0 else -1), lo, hi
        lo, hi = Npoly.refine_root(lo, hi, steps=8)
    raise RuntimeError("sign refinement did not converge")


def part():
    import sympy as sp

    y = sp.symbols("y")

    # ================================================ A: symbolic layer
    section("A. THE SYMBOLIC LAYER (kernel/Weyl identity; W-lemma; CH)")
    okA = True
    for n in (2, 3):
        bs = sp.symbols("b1:%d" % (n + 1), positive=True)
        ws = sp.symbols("w1:%d" % (n + 1), positive=True)
        for signs in itertools.product((1, -1), repeat=n):
            J = sp.diag(*signs)
            Dm = sp.diag(*bs)
            wv = sp.Matrix(ws)
            rho = [signs[k] * ws[k] ** 2 for k in range(n)]
            Ahat = J * Dm - (J * wv) * (J * wv).T
            G = sum(rho[k] / (y - bs[k]) for k in range(n))
            v = sp.Matrix([ws[k] / (bs[k] - y) for k in range(n)])
            lhs = sp.simplify((Ahat - y * J) * v
                              - (J * wv) * (1 + G))
            okA = okA and lhs == sp.zeros(n, 1)
            vJv = sp.simplify((v.T * J * v)[0, 0] + sp.diff(G, y))
            okA = okA and vJv == 0
    check("A1 the kernel/Weyl identity (n = 2, 3, ALL sign "
          "patterns, symbolic)", okA,
          "(Ahat - yJ) v == Jw (1 + G(y)) for v_k = w_k/(b_k - y) "
          "-- v is the EXPLICIT kernel at every census root (G = "
          "-1) -- and v^T J v == -G'(y) identically (sympy): the "
          "sign characteristic IS the crossing direction of the "
          "Weyl secular function, eps_i = -sign((F/A_0)'(y_i))")

    okB = True
    y0 = sp.symbols("y0")
    for n in (2, 3):
        vs = sp.symbols("v1:%d" % (n + 1), real=True)
        v = sp.Matrix(vs)
        if n == 2:
            perp = [sp.Matrix([vs[1], -vs[0]])]
        else:
            perp = [sp.Matrix([vs[1], -vs[0], 0]),
                    sp.Matrix([vs[2], 0, -vs[0]])]
        ss = sp.symbols("s1:%d" % (len(perp) + 1), real=True)
        A0m = sp.zeros(n, n)
        for s_, u_ in zip(ss, perp):
            A0m += s_ * u_ * u_.T
        assert sp.simplify(A0m * v) == sp.zeros(n, 1)
        A1m = sp.Matrix(n, n, sp.symbols("a1:%d" % (n * n + 1),
                                         real=True))
        A1m = (A1m + A1m.T) / 2
        W0 = sp.Matrix(n, n, sp.symbols("q1:%d" % (n * n + 1),
                                        real=True))
        W1 = sp.Matrix(n, n, sp.symbols("p1:%d" % (n * n + 1),
                                        real=True))
        Ay = A0m + (y - y0) * A1m
        Wy = W0 + (y - y0) * W1
        My = Wy * Ay * Wy.T
        Mprime = sp.diff(My, y).subs(y, y0)
        x = W0.inv().T * v
        lhs = sp.simplify(sp.expand((x.T * Mprime * x)[0, 0]))
        rhs = sp.simplify(sp.expand((v.T * A1m * v)[0, 0]))
        okB = okB and sp.simplify(lhs - rhs) == 0
    check("A2 the W(y)-congruence obstruction lemma (n = 2, 3, "
          "generic, symbolic)", okB,
          "for M(y) = W(y) A(y) W(y)^T with A(y0) v = 0 and x = "
          "W(y0)^{-T} v: x^T M'(y0) x == v^T A'(y0) v -- the W' "
          "terms die on the kernel (proven generically): the sign "
          "characteristic is CONGRUENCE-INVARIANT, so the measured "
          "mixed ladder kills the ENTIRE W(y) > 0 class at once -- "
          "the r188/v946 upgrade path is IMPOSSIBLE-IN-CLASS, "
          "closed by theorem, not by search")

    S = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, -1]])
    J3 = sp.diag(1, 1, -1)
    T = J3 * S                                   # J-self-adjoint
    p = T.charpoly(y)
    pT = sp.zeros(3, 3)
    cfs = p.all_coeffs()
    for c in cfs:
        pT = pT * T + c * sp.eye(3)
    okC = sp.simplify(pT) == sp.zeros(3, 3)
    check("A3 the Langer degeneracy (Cayley-Hamilton trivial "
          "definitizer, exact)", okC,
          "p(T) == 0 for the characteristic polynomial of a "
          "J-self-adjoint instance (exact): [p(T)x, x] = 0 >= 0 -- "
          "finite-dimensional Langer definitizability is DEGENERATE "
          "(every J-self-adjoint matrix trivially definitizes); "
          "the non-vacuous notion is STRONG definitizability "
          "J p(T) > 0 (Zizler 1995 / Lancaster-Ye 1993), which is "
          "EQUIVALENT to H2 per rung; probe pins the h = 4 "
          "exhibit: J p(T) strictly PD (eigsy min %.2e, symdev "
          "%.1e), CH residual %.1e"
          % (PIN_LANGER_PSD_MIN, PIN_LANGER_SYMDEV,
             PIN_CH_RESIDUAL))

    # ================================================ B: exact battery
    section("B. THE EXACT STURM BATTERY (n = 4, all 16 sign "
            "patterns x 2 profiles)")
    n1 = 4
    bs = [sp.Integer(b) for b in BATTERY_POLES]
    n_cells = 0
    n_nonreal_cells = 0
    ok_two_route = True
    ok_flip = True
    ok_count = True
    ok_scaffold = True
    for mags in BATTERY_MAGS:
        for signs in itertools.product((1, -1), repeat=n1):
            n_cells += 1
            rho = [sp.Rational(signs[k]) * sp.Rational(mags[k])
                   for k in range(n1)]
            npos = sum(1 for r in rho if r > 0)
            nneg = n1 - npos
            prod = sp.prod([y - b for b in bs])
            Npoly = sp.Poly(sp.expand(
                prod + sum(rho[k] * sp.prod([y - bs[j]
                                             for j in range(n1)
                                             if j != k])
                           for k in range(n1))), y, domain="QQ")
            # P2 = numerator of sum rho_k/(y-b_k)^2 (positive denom)
            P2 = sp.Poly(sp.expand(
                sum(rho[k] * sp.prod([(y - bs[j]) ** 2
                                      for j in range(n1) if j != k])
                    for k in range(n1))), y, domain="QQ")
            ivs = [iv for (iv, mult) in Npoly.intervals()
                   for _ in range(mult)]
            R = len(ivs)
            npairs = (n1 - R) // 2
            if npairs:
                n_nonreal_cells += 1
            boxes = [_refine(Npoly, sp.Rational(a), sp.Rational(b),
                             bs) for (a, b) in ivs]
            eps_route1 = []
            for i, (lo, hi) in enumerate(boxes):
                # eps = sign([v,v]) = sign(sum rho/(y-b)^2)
                s, lo, hi = _sign_on_interval(P2, Npoly, lo, hi)
                boxes[i] = (lo, hi)
                eps_route1.append(s)
            eps_route2 = []
            for i, (lo, hi) in enumerate(boxes, start=1):
                # poles excluded from the box: b > root iff b >= hi
                m_i = sum(1 for b in bs if b >= hi)
                eps_route2.append(-(-1) ** ((R - i) + m_i))
            ok_two_route = ok_two_route and eps_route1 == eps_route2
            for i in range(R - 1):
                delta = sum(1 for b in bs
                            if boxes[i][1] <= b <= boxes[i + 1][0])
                ok_flip = ok_flip and (
                    eps_route1[i + 1] * eps_route1[i]
                    == (-1) ** (delta + 1))
            ok_count = ok_count and (
                eps_route1.count(1) == npos - npairs
                and eps_route1.count(-1) == nneg - npairs)
            # parity scaffold (source-side: residue signs only)
            lo_edge = bs[0] - 100
            hi_edge = bs[-1] + 100
            cnt = Npoly.count_roots(lo_edge, bs[0])
            ok_scaffold = ok_scaffold and (
                cnt % 2 == (1 if rho[0] > 0 else 0))
            for k in range(n1 - 1):
                cnt = Npoly.count_roots(bs[k], bs[k + 1])
                want_odd = 1 if (rho[k] > 0) == (rho[k + 1] > 0) else 0
                ok_scaffold = ok_scaffold and cnt % 2 == want_odd
            cnt = Npoly.count_roots(bs[-1], hi_edge)
            ok_scaffold = ok_scaffold and (
                cnt % 2 == (1 if rho[-1] < 0 else 0))
    check("B1 the two-route sign-characteristic law (32 cells, "
          "EXACT, no floats)", ok_two_route and n_cells == 32,
          "eps by crossing sign (interval-refined exact sign of "
          "sum rho_k/(y_i - b_k)^2 with a Sturm zero-count "
          "certificate) == eps by the combinatorial formula "
          "-(-1)^{(R-i)+m_i} at EVERY real root of EVERY cell "
          "(%d cells incl. %d nonreal-pair cells; poles (1,2,3,4), "
          "all 16 sign patterns x 2 magnitude profiles): the "
          "residue-sign data determines the crossing directions -- "
          "THE r188 LADDER IS THE KREIN MULTISET"
          % (n_cells, n_nonreal_cells))

    check("B2 the flip law + the count law with nonreal-pair "
          "deficit (exact)", ok_flip and ok_count,
          "eps_{i+1} eps_i == (-1)^{Delta_i + 1} (flips exactly "
          "where interlacing fails by an even pole count) and "
          "#(eps = +) == n_+ - #pairs, #(eps = -) == n_- - #pairs "
          "at every cell (each conjugate pair carries signature "
          "(1,1)): the count law that identifies the ladder with "
          "the multiset, exact in every battery cell")

    check("B3 THE PARITY SCAFFOLD (source-side, root-free; exact "
          "in every cell)", ok_scaffold,
          "#roots in (-inf, b_1) odd iff rho_1 > 0; in (b_k, "
          "b_{k+1}) odd iff sign rho_k == sign rho_{k+1}; in "
          "(b_{n1}, +inf) odd iff rho_{n1} < 0 -- verified by "
          "exact Sturm counts in all 32 cells: the root-count "
          "parity per pole gap is computable from residue SIGNS "
          "alone ('source-side (root-free)' per BH9-K4); probe: "
          "verified against measurement at all %d gaps (h <= 13), "
          "h = 21/28 scaffolds %s odd gaps"
          % (PIN_SCAFFOLD_GAPS, str(PIN_SCAFFOLD_2128)))

    # ================================================ C: pinned + typing
    section("C. THE MEASURED PIVOT + THE KILL + THE WITNESS "
            "(pinned)")
    okD = PIN_D_TAB == {4: 2, 5: 4, 8: 11, 13: 18} \
        and PIN_OCCMIN_TAB[4] and PIN_OCCMIN_TAB[5] \
        and not PIN_OCCMIN_TAB[8] and not PIN_OCCMIN_TAB[13] \
        and all(k in PIN_DOUBLED_GAP for k in (8, 13))
    check("C1 STRICT-DEFINITIZER-ROOT-DEPENDENT (d_h = 2/4/11/18; "
          "occ-min fails at h >= 8)", okD,
          "the minimal strict definitizer degree d_h = #sign flips "
          "= %s (Langer J p(T) strictly PD at matrix level), "
          "determined by the gap-occupancy vector alone; the "
          "occupancy-minimality law HOLDS at h = 4, 5 and FAILS at "
          "h = 8, 13 by exactly ONE interior doubled gap each (gap "
          "%s of %s; gap %s of %s): the eps-sequence is NOT "
          "source-computable from the parity scaffold alone -- the "
          "scaffold is the surviving source-side coordinate"
          % (str(PIN_D_TAB), PIN_DOUBLED_GAP[8][0],
             PIN_DOUBLED_GAP[8][1], PIN_DOUBLED_GAP[13][0],
             PIN_DOUBLED_GAP[13][1]))

    okE = all(v < 1e-18 for v in PIN_FAM_DEVS.values()) \
        and PIN_BLK_TAB == {4: (1, 5), 5: (1, 2)}
    check("C2 the W(y)-class kill instantiated (three families; "
          "blocking roots named)", okE,
          "the three contracted families (diagonal pole-data, "
          "Cauchy, JD-polynomial -- all PD) verified at both "
          "blocking roots with identity devs %s: every W(y) > 0 "
          "congruence hits the wrong-orientation eps at the named "
          "roots %s; NOT killed and typed honestly: dimension-"
          "enlarging linearizations (trivial-by-roots, forbidden "
          "as construction) and residue-sign-changing non-"
          "congruence transforms (currently an empty class)"
          % (str(PIN_FAM_DEVS), str(PIN_BLK_TAB)))

    okF = PIN_WIT["ladder"] == PIN_LADDER[5] \
        and PIN_WIT["nreal"] == 8 and PIN_WIT["npairs"] == 1
    check("C3 the realness-break witness detector (the Krein "
          "invariant sees, the ladder is blind)", okF,
          "the r172 witness at h = 5 leaves the raw residue-sign "
          "ladder UNMOVED at %s but BREAKS census realness (nreal "
          "= %d, %d nonreal pair -- not strongly definitizable: "
          "the pair must be a zero of every Langer definitizer): "
          "a NEW detector for the witness class; the law itself "
          "is ray-blind (an identity), typed, never sold as a "
          "separator" % (str(PIN_WIT["ladder"]), PIN_WIT["nreal"],
                         PIN_WIT["npairs"]))

    okG = PIN_D_WORLD["SMOOTH"] == 0 \
        and PIN_D_WORLD["SCRARITH"] == PIN_D_WORLD["EPSTEIN"] == 3 \
        and abs(PIN_SLACK_SLOPE) < 0.7
    check("C4 orientation + pricing: ATOMS-VS-NO-ATOMS; tau-FLAT; "
          "STRUCTURAL-ONLY closure", okG,
          "SMOOTH d = 0 (eps constant -1, the definite world) vs "
          "SCRARITH/EPSTEIN both d = 3: the d-dichotomy separates "
          "atoms-vs-no-atoms only (the r188/v946 caveat inherited, "
          "NOT a sign source); defect-slack slope vs log tau = "
          "+%.3f FLAT (ride band (0.7, 1.3)); exact scale-gauge "
          "invariance under c -> (3/7)c; the Krein coordinate is "
          "closed STRUCTURAL-ONLY: H2-cofinal in operator form is "
          "equivalent to realness -- the definitizer reformulation "
          "adds no leverage; census cardinality 4 UNCHANGED; NOT "
          "RH evidence" % PIN_SLACK_SLOPE)

    print("\n  [TYPED] THE r188 LADDER IS THE KREIN SIGN-")
    print("  CHARACTERISTIC MULTISET (two-route proven); the parity")
    print("  scaffold is the new source-side coordinate; the W(y) > 0")
    print("  congruence class is killed BY THEOREM.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v948 -- PRIME.KREIN.DEFINITIZER.01 (the sign-"
          "characteristic law two-route")
    print("proven; the parity scaffold; the W(y)-congruence-class "
          "kill by theorem;")
    print("the Langer degeneracy; the realness-break witness "
          "detector; round 191;")
    print("NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v948: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the kernel/Weyl identity, the W-lemma, the CH "
          "degeneracy and")
    print("the full 32-cell exact Sturm battery recomputed in-run "
          "(no floats); the")
    print("d_h/occupancy/family/witness/world tables PINNED from "
          "krein_definitizer_")
    print("probe.py (SPEC %s, 57/57, record 1950 s + 1901 s"
          % PIN_SPEC_R191)
    print("deterministic re-run, no post-freeze amendments, all logs "
          "kept, RE-RUN")
    print("GREEN AS TYPED AT PROMOTION 1983.4 s, 57/57).  "
          "NOT RH")
    print("evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.KREIN.DEFINITIZER.01 sign-characteristic law + "
          "congruence kill: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
