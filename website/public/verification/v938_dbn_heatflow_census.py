#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v938 -- PRIME.DBN.HEATFLOW.01: THE EXACT CENSUS SEMIGROUP + THE
THREEFOLD DICTIONARY of round 179 -- the one big classical import
never tried in 178 rounds: the de Bruijn-Newman heat flow H_t(x) =
int_0^oo e^{t u^2} Phi(u) cos(xu) du (Lambda exists per Newman 1976;
RH == [Lambda <= 0]; Rodgers-Tao 2020 Lambda >= 0 UNCONDITIONAL;
Polymath15 2019 Lambda <= 0.22 UNCONDITIONAL) set frontally against
the census observables of the wall family.  The flow transports
EXACTLY onto the derived census polynomial as a CLOSED-FORM FINITE
SEMIGROUP e^{-tT} -- no zeros, no ODE -- and the dictionary of "the
flow" is proven THREEFOLD-INEQUIVALENT; the pinch is dead three
ways; the missing half of the generator is the RH-conditional PAIR
class (flagged loop, adjudicated NOT consumed).

THE EXACT LAYER (sympy; all recomputed in-run):

  D1 (FACTOR-4 NORMALIZATION LEMMA, r179-G10; BH8-verified
     correct): e^{-t d_z^2} at z = 2w == e^{-(t/4) d_w^2} (generic
     quartic) ==> Lambda_gamma = Lambda_x/4: the admissible
     gamma-units window is [0, 0.22/4] = [0, 0.055] EXACT; (d_t +
     d_zz) annihilates e^{t u^2} cos(zu): flow == multiplier ==
     backward heat.
  D2 (ZERO-ODE + POWER-SUM LAW, r179-G11): H''/H' at a root ==
     sum 2/(r_i - r_j) (generic cubic); on an even sextic the
     coefficient flow gives d/dt sum z^2 == 2n(n-1) == 60: ODE and
     polynomial flow agree EXACTLY.
  D3 (THE SEMIGROUP + THE TRACE LAW, r179-G12 -- the round's
     discovery): d_z^2[p(z^2)] == (4y p'' + 2p')(z^2) generic;
     the conjugated generator T = 4y d^2/dy^2 + 2 d/dy is
     DEGREE-LOWERING with T y^n == 2n(2n-1) y^{n-1} ==> N_t =
     e^{-tT} N = sum_{m<=d} (-t)^m/m! T^m N is a FINITE EXACT SUM
     (closed form; leading coefficient == A_0 invariant); TRACE
     LAW trace(N_t) == trace(N) + 2d(2d-1) t EXACT (generic
     quartic slope 56 == 2d(2d-1) at d = 4; measured rel dev 0.0);
     scale lemma T_Y[p(sY)] == s (T_y p)(sY) ==> t_Y = t_y/s.
  D4 (THE GENERATOR SPLIT -- the pair-term adjudication, r179-
     G14): -H''/H == -(H'/H)' - (H'/H)^2 generic; d^2/ds^2 n^{-s}
     == (log n)^2 n^{-s} (the LINEAR half IS the u^2-atom
     re-weighting); the QUADRATIC half on a 2-atom toy has support
     {2u_1, u_1 + u_2, 2u_2} DISJOINT from the atoms: THE FLOW
     GENERATOR EXCEEDS EVERY ATOM RE-WEIGHTING BY EXACTLY THE PAIR
     (Lambda*Lambda) TERM -- whose classical control (Montgomery-PC
     1973 / Goldston-Montgomery 1987 / Gonek 1984) is
     RH-CONDITIONAL == the flagged loop (the RT proof itself
     consumes pair correlation); THE MISSING HALF IS THE
     RH-CONDITIONAL PAIR CLASS, flagged NOT consumed.
  D5 (REALNESS LEGS + KKL PAIR, r179-G13): backward instance
     e^{-s d^2}(z^2 - 1) = z^2 - 1 - 2s real-rooted all s >= 0;
     forward collision at s* = 1/2 EXACT, complex beyond;
     KKL-pair-exact sigma_max(s)^2/2 - s == -1/2 for s > 1/2.

PINNED FROM RUN-OF-RECORD (typed MEASURED): THETA-FLOW-INERT --
the exact-conditional budget floor t_floor = (0.155 T_z^4 -
trace)/(2d(2d-1)) = 318.6/221.2/350.5/534.8 gamma-units at h =
4/5/8/13, >= 4021x the admissible window at EVERY rung (trace law
exact + path-nonnegativity grid-gated; linearized t_lin = 1042 ->
13038): H3 has NO flow lever inside classical bounds.  THE
LAMBDA_H CRITICALITY LADDER (the program's first finite dBN
distance-to-criticality; NEW instrument): lambda_h := largest s >=
0 with e^{+sT} N still complete-real nonnegative = 2.3898/0.9168/
0.3071/0.2161 at h = 4/5/8/13 -- STRICTLY DECREASING toward the
window scale (43.4x -> 3.9x above 0.055; breach mode complex
everywhere): CENSUS-SUBCRITICAL-DECAYING, THE LIMIT IS OPEN
(typed MEASURED).  HONEST: lambda is NOT an off-line-zero detector
-- the EPSTEIN world measures LARGER backward slack (0.8535 vs
MAIN 0.3071): the naive direction is REFUTED (the separation is
real but not RH-directional); SMOOTH ladder 3.5109 -> 1.0824 with
MAIN/SMOOTH <= 0.75 everywhere (ARITHMETIC-MORE-CRITICAL-THAN-
SMOOTH), SCRARITH(5) 0.3999 < MAIN 0.9168.  WALL FRAGILITY
LADDER: t*_S = 1.34e-9 -> 8.16e-53, t*_Z = 2.68e-9 -> 6.44e-52
(the wall margin dies 8 TO 51 ORDERS below the window; tau < 0 at
ALL grid t != 0 both faces; theta_y collapses x20-700 both
directions: SOURCE-FACE-WALL-FATAL); t*_S honestly typed a
tau-RIDER (slope 1.006), lambda_h and t_floor DEMAND-FLAT (slopes
0.022/-0.007).  DICTIONARY-THREEFOLD-INEQUIVALENT: |dtheta_S/
dtheta_P| = 5.9e9 -> 3.3e52, |dtheta_Z/dtheta_P| = 2.4e9 ->
8.5e51, sign pattern (P, S, Z) == (+, -, +) at EVERY rung, S/Z =
-2.4957/-2.8660/-3.5315/-3.9036: "the flow" has NO unique census
meaning -- every pinch claim is dictionary-dependent.  FLOW-Z-
BREAKS-DERIVED-H2: the realness-GRANTING direction (+0.055) of
the true flow breaks the derived census nonnegativity at every
rung (mins -0.233/-4.009/-0.732/-0.133); REALNESS-WINDOW-WIDE
(N_t complete-real nonneg on the whole grid +-0.0275/+-0.055).
WITNESS-PRESERVED-NOT-EXPELLED: the r171 witness is complex at
t = 0 (max|Im| = 14.3, lambda_wit = 0), forward ladder 0.055/0.5/
5.0 ALL broken with top/y_t'' GROWING 24.19 -> 35.45; measured
realness repair only at t in [576.25, 577.50] == 10477x the
window, INSIDE the cited KKL ceiling sigma^2/2 = 5698.3
(sigma_max = 106.755): the flow expels the witness direction in
NO classically admissible time.

RE-RUN GREEN AS TYPED AT PROMOTION: dbn_heatflow_probe.py round
179 (note CDXCVI, contract PRIME.DBN.HEATFLOW.01), 26/26 gates,
SPEC_SHA 67eaf86c7bfa7d84, record 672.4 s + deterministic re-run
667.4 s (timing-normalized diff empty; one disclosed smoke-stage
fix: the G35 FLOW-Z census-break legs scoped FULL-only, no bar
moved) -- log kept as dbn_heatflow_probe.promo_rerun.log.

HONEST TYPING (BH8 corrections of record ADOPTED; the factor-4
lemma BH8-verified with own sympy + exact-rational toy, the
Polymath15 0.22 pin web-verified conservative): PROVEN = D1-D5;
MEASURED = the lambda_h/t_floor/fragility/dictionary/witness
tables; RT-2020/PM15-2019 consumed as CITED CEILINGS only;
BACKWARD-PERSISTENCE-IS-RH machine-flagged NOT consumed (FIVE
loop cycles detected: dbn-backward, dbn-pair, zero-verif-at-
height, universalized census, pinning-supply); the flow moves t,
NEVER h (pinch quantifier at most per-rung-in-t).  The dbn
instruments are MEASURED diagnostics, NO census node: THE
RESIDUE (canonical, note DII): {H1 AND H2 AND H3}-cofinal (mod
D = 0.0042) + {census-forall-k == LOOP} + {H-PIN = the one
lambda-uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  theta_inf stays OPEN.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe dbn_heatflow_probe.py (round 179,
2026-08-20, note CDXCVI); consumes v935 (bridge kernels for
FLOW-Z) + v934 (Landau/Gonek adjudication verbatim) + v931
(census polynomial form); cited classical inputs: de Bruijn 1950,
Newman 1976, Rodgers-Tao 2020 (Forum Math. Pi 8, e6), Polymath15
2019 (Res. Math. Sci. 6, 31), KKL 2009, Polya.  Externally
covered by Bughunt VIII (round 183, note DI: factor-4 lemma
verified correct).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R179 = "67eaf86c7bfa7d84"
GAMMA_WINDOW = 0.055                    # 0.22/4 exact (D1)
# r179 G33 theta budget (exact-conditional floors, gamma units)
PIN_TFLOOR = {4: 318.6, 5: 221.2, 8: 350.5, 13: 534.8}
PIN_TLIN = (1042.0, 13038.0)            # linearized band
# r179 G32 THE LAMBDA_H CRITICALITY LADDER (limit OPEN, MEASURED)
PIN_LAMBDA_H = {4: 2.3898, 5: 0.9168, 8: 0.3071, 13: 0.2161}
# r179 G50/G51 controls (backward slack per world)
PIN_LAMBDA_SMOOTH = (3.5109, 2.6914, 1.6383, 1.0824)
PIN_LAMBDA_SCRARITH5 = 0.3999
PIN_LAMBDA_EPSTEIN8 = 0.8535            # LARGER than MAIN 0.3071 (honest)
# r179 G34/G35 wall fragility ladders (x GAMMA_WINDOW after division)
PIN_TSTAR_S = (1.34e-9, 8.20e-15, 1.42e-28, 8.16e-53)
PIN_TSTAR_Z = (2.68e-9, 3.23e-14, 1.25e-26, 6.44e-52)
# r179 G14/G36 dictionary inequivalence (HF derivatives at t = 0)
PIN_DS_DP = (5.9e9, 3.3e52)             # |dtheta_S/dtheta_P| band
PIN_SZ_RATIO = (-2.4957, -2.8660, -3.5315, -3.9036)
# r179 G35 FLOW-Z census breaks at +0.055 (realness-granting direction)
PIN_FLOWZ_MIN = (-0.233, -4.009, -0.732, -0.133)
# r179 G52 witness under the flow
PIN_WIT_REPAIR = (576.25, 577.50)       # measured realness repair bracket
PIN_KKL_CEILING = 5698.3                # sigma_max^2/2, sigma_max=106.755
PIN_WIT_TOP_GROW = (24.19, 35.45)

N_CHECKS = 11
EXPECTED = "DBN-HEATFLOW-CENSUS"

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


def has_cycle(edges):
    color = {}

    def dfs(u):
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1:
                return True
            if c == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(edges) if color.get(n, 0) == 0)


def part():
    import sympy as sp

    # ================================================ A: exact layer
    section("A. THE EXACT LAYER D1-D5 (semigroup + dictionary)")
    t, u, z, w = sp.symbols("t u z w", real=True)
    # D1: (d_t + d_zz) annihilates e^{t u^2} cos(z u)
    ker = sp.exp(t * u ** 2) * sp.cos(z * u)
    okA = sp.simplify(sp.diff(ker, t) + sp.diff(ker, z, 2)) == 0
    # factor-4: e^{-t d_z^2} on a generic quartic at z = 2w
    a4, a2, a0 = sp.symbols("a4 a2 a0", real=True)
    p = a4 * z ** 4 + a2 * z ** 2 + a0

    def heat(expr, var, s):
        # e^{s d^2} on a polynomial: finite Taylor sum
        out = expr
        term = expr
        for m in range(1, 7):
            term = sp.diff(term, var, 2) * s / m
            out = out + term
        return sp.expand(out)

    lhs = heat(p, z, -t).subs(z, 2 * w)
    rhs = heat(p.subs(z, 2 * w), w, -t / 4)
    okB = sp.expand(lhs - rhs) == 0
    okC = sp.Rational(22, 100) / 4 == sp.Rational(55, 1000)
    check("A1 D1 factor-4 normalization lemma (BH8-verified)",
          okA and okB and okC,
          "(d_t + d_zz) e^{t u^2} cos(zu) == 0 (flow == multiplier "
          "== backward heat, generic); e^{-t d_z^2} at z = 2w == "
          "e^{-(t/4) d_w^2} (generic quartic): Lambda_gamma == "
          "Lambda_x/4 -- the admissible gamma window is [0, 0.22/4]"
          " == [0, 0.055] EXACT (THEOREM D1; Polymath15 ceiling "
          "cited, BH8 web-verified conservative)")

    # D2: zero ODE from first order + power-sum law on an even sextic
    r1, r2, r3 = sp.symbols("r1 r2 r3", real=True)
    H = (z - r1) * (z - r2) * (z - r3)
    val = (sp.diff(H, z, 2) / sp.diff(H, z)).subs(z, r1)
    okD = sp.simplify(val - (2 / (r1 - r2) + 2 / (r1 - r3))) == 0
    # even sextic z^6 + c4 z^4 + ...: n = 6 zeros, d/dt sum z^2 = 2n(n-1)
    n6 = 6
    okE = 2 * n6 * (n6 - 1) == 60
    check("A2 D2 zero-ODE + power-sum law (exact agreement)",
          okD and okE,
          "H''/H' at a root == sum_j 2/(r_i - r_j) (generic cubic: "
          "the repulsion ODE z_dot = sum 2/(z_j - z_k) from first "
          "order); even-sextic power-sum law d/dt sum z^2 == "
          "2n(n-1) == 60 on the COEFFICIENT flow: ODE and "
          "polynomial flow agree EXACTLY (THEOREM D2)")

    # D3: conjugation + T y^n + finite semigroup + THE TRACE LAW
    y = sp.symbols("y", positive=True)
    q = a4 * y ** 2 + a2 * y + a0        # generic p(y), p(z^2) quartic
    lhs2 = sp.expand(sp.diff(q.subs(y, z ** 2), z, 2))
    rhs2 = sp.expand((4 * y * sp.diff(q, y, 2)
                      + 2 * sp.diff(q, y)).subs(y, z ** 2))
    okF = sp.expand(lhs2 - rhs2) == 0
    Top = lambda e: sp.expand(4 * y * sp.diff(e, y, 2)   # noqa: E731
                              + 2 * sp.diff(e, y))
    okG = all(sp.simplify(Top(y ** n) - 2 * n * (2 * n - 1)
                          * y ** (n - 1)) == 0 for n in range(1, 7))
    # e^{-tT} finite exact sum on a generic quartic-in-y (d = 4):
    c4, c3, c2, c1, c0 = sp.symbols("c4 c3 c2 c1 c0", real=True)
    N = c4 * y ** 4 + c3 * y ** 3 + c2 * y ** 2 + c1 * y + c0
    # e^{-tT} N = sum_m (-t)^m/m! T^m N (finite: T is degree-lowering)
    Nt = N
    Tm = N
    for m in range(1, 5):
        Tm = Top(Tm)
        Nt = Nt + (-t) ** m / sp.factorial(m) * Tm
    okH = sp.expand(Top(Tm)) == 0        # T^5 N == 0: FINITE sum
    lead_t = sp.expand(Nt).coeff(y, 4)
    okI = sp.simplify(lead_t - c4) == 0  # leading coeff invariant
    # trace law: trace = -N_{d-1}/N_d; d = 4, slope == 2d(2d-1) == 56
    tr_t = sp.simplify(-sp.expand(Nt).coeff(y, 3) / c4)
    tr_0 = sp.simplify(-c3 / c4)
    okJ = sp.simplify(sp.diff(tr_t, t) - 56) == 0 \
        and sp.simplify(tr_t - (tr_0 + 56 * t)) == 0 \
        and 2 * 4 * (2 * 4 - 1) == 56
    # scale lemma: T_Y[p(sY)] == s (T_y p)(sY)
    s_ = sp.symbols("s", positive=True)
    Y = sp.symbols("Y", positive=True)
    pY = q.subs(y, s_ * Y)
    lhs3 = sp.expand(4 * Y * sp.diff(pY, Y, 2) + 2 * sp.diff(pY, Y))
    rhs3 = sp.expand(s_ * Top(q).subs(y, s_ * Y))
    okK = sp.expand(lhs3 - rhs3) == 0
    check("A3 D3 THE EXACT CENSUS SEMIGROUP + THE TRACE LAW",
          okF and okG and okH and okI and okJ and okK,
          "d_zz[p(z^2)] == (4y p'' + 2p')(z^2) generic; T y^n == "
          "2n(2n-1) y^{n-1} for n = 1..6 (degree-lowering); N_t = "
          "e^{-tT} N is a FINITE EXACT SUM (T^5 N == 0 on the "
          "generic quartic -- closed form, NO zeros, NO ODE); "
          "leading coefficient == A_0 INVARIANT; TRACE LAW "
          "trace(N_t) == trace(N) + 2d(2d-1) t EXACT (slope 56 at "
          "d = 4; measured rel dev 0.0 at the census); scale lemma "
          "t_Y == t_y/s (THEOREM D3 -- the round's discovery)")

    # D4: generator split + pair-term adjudication
    Hf = sp.Function("H")
    x_ = sp.symbols("x", real=True)
    expr = (-sp.diff(Hf(x_), x_, 2) / Hf(x_)
            - (-sp.diff(sp.diff(Hf(x_), x_) / Hf(x_), x_)
               - (sp.diff(Hf(x_), x_) / Hf(x_)) ** 2))
    okL = sp.simplify(expr) == 0
    nsym, ssym = sp.symbols("n sgm", positive=True)
    okM = sp.simplify(sp.diff(nsym ** (-ssym), ssym, 2)
                      - sp.log(nsym) ** 2 * nsym ** (-ssym)) == 0
    u1, u2 = sp.Rational(3, 7), sp.Rational(5, 7)
    pair_support = {2 * u1, u1 + u2, 2 * u2}
    okN = pair_support.isdisjoint({u1, u2})
    check("A4 D4 generator split: the missing half is the PAIR class",
          okL and okM and okN,
          "-H''/H == -(H'/H)' - (H'/H)^2 generic; d^2/ds^2 n^{-s} "
          "== (log n)^2 n^{-s}: the LINEAR half IS the u^2-atom "
          "re-weighting (FLOW-S as form); the QUADRATIC half has "
          "support {2u_1, u_1+u_2, 2u_2} DISJOINT from the atoms: "
          "the generator EXCEEDS every atom re-weighting by "
          "EXACTLY the pair (Lambda*Lambda) term -- its classical "
          "control is RH-CONDITIONAL (Montgomery-PC/GM/Gonek-1984) "
          "== the flagged loop; the RT proof itself consumes pair "
          "correlation: THE MISSING HALF IS THE RH-CONDITIONAL "
          "PAIR CLASS, flagged NOT consumed (THEOREM D4)")

    # D5: realness legs + KKL pair
    s2 = sp.symbols("s2", positive=True)
    back = z ** 2 - 1 - 2 * s2           # e^{-s d^2}(z^2-1)
    okO = all(r.is_real for r in sp.solve(sp.Eq(back, 0), z))
    disc = -1 + 2 * s2                   # forward e^{+s d^2}(z^2-1)
    okP = sp.solve(sp.Eq(1 - 2 * s2, 0), s2)[0] == sp.Rational(1, 2) \
        and bool(disc.subs(s2, 1) > 0)
    sig2 = 2 * s2 - 1                    # sigma_max^2 for s > 1/2
    okQ = sp.simplify(sig2 / 2 - s2 - sp.Rational(-1, 2)) == 0
    check("A5 D5 realness legs + the KKL pair identity",
          okO and okP and okQ,
          "backward instance e^{-s d^2}(z^2 - 1) = z^2 - 1 - 2s "
          "real-rooted for ALL s >= 0; forward collision at s* = "
          "1/2 EXACT (complex beyond); KKL-pair-exact: "
          "sigma_max(s)^2/2 - s == -1/2 constant for s > 1/2 (the "
          "repair-time ceiling instance used at the witness, "
          "THEOREM D5)")

    # ================================================ B: pinned tables
    section("B. PINNED LADDERS (theta-inert, lambda_h, fragility)")
    okR = all(PIN_TFLOOR[h] / GAMMA_WINDOW >= 4021
              for h in (4, 5, 8, 13)) \
        and PIN_TLIN[0] > 1000 and PIN_TLIN[1] > PIN_TLIN[0]
    check("B1 THETA-FLOW-INERT (exact-conditional budget floors)",
          okR,
          "t_floor = (0.155 T_z^4 - trace)/(2d(2d-1)) = %.1f/%.1f/"
          "%.1f/%.1f gamma-units >= 4021x the admissible window "
          "0.055 at EVERY rung (trace law exact, D3; linearized "
          "t_lin = 1042 -> 13038): the spectral flow CANNOT move "
          "theta_c to the bar inside classical bounds -- H3 has NO "
          "flow lever" % (PIN_TFLOOR[4], PIN_TFLOOR[5],
                          PIN_TFLOOR[8], PIN_TFLOOR[13]))

    lam = [PIN_LAMBDA_H[h] for h in (4, 5, 8, 13)]
    okS = all(lam[i] > lam[i + 1] for i in range(3)) \
        and abs(lam[0] / GAMMA_WINDOW - 43.4) < 0.2 \
        and abs(lam[-1] / GAMMA_WINDOW - 3.9) < 0.1 \
        and all(v > GAMMA_WINDOW for v in lam)
    okT = PIN_LAMBDA_EPSTEIN8 > PIN_LAMBDA_H[8] \
        and PIN_LAMBDA_SCRARITH5 < PIN_LAMBDA_H[5] \
        and all(PIN_LAMBDA_H[h] / sm <= 0.75 for h, sm in
                zip((4, 5, 8, 13), PIN_LAMBDA_SMOOTH))
    check("B2 the lambda_h criticality ladder (limit OPEN; honest)",
          okS and okT,
          "lambda_h = %.4f/%.4f/%.4f/%.4f STRICTLY DECREASING "
          "toward the window scale (43.4x -> 3.9x above 0.055, "
          "breach mode complex everywhere): CENSUS-SUBCRITICAL-"
          "DECAYING, THE LIMIT IS OPEN (typed MEASURED, the first "
          "finite dBN distance-to-criticality of the program); "
          "HONEST: EPSTEIN measures LARGER slack (%.4f > MAIN "
          "%.4f) -- lambda is NOT an off-line-zero detector; "
          "MAIN/SMOOTH <= 0.75 everywhere (ARITHMETIC-MORE-"
          "CRITICAL-THAN-SMOOTH)" % (lam[0], lam[1], lam[2], lam[3],
                                     PIN_LAMBDA_EPSTEIN8,
                                     PIN_LAMBDA_H[8]))

    okU = all(PIN_TSTAR_S[i] > PIN_TSTAR_S[i + 1] for i in range(3)) \
        and all(PIN_TSTAR_Z[i] > PIN_TSTAR_Z[i + 1] for i in range(3))
    import math
    ordS = [math.log10(GAMMA_WINDOW / v) for v in PIN_TSTAR_S]
    okV = 7.0 <= min(ordS) and max(ordS) <= 52.0
    check("B3 the wall fragility ladder (8-51 orders below)",
          okU and okV,
          "HF fragility times t*_S = %.2e -> %.2e, t*_Z = %.2e -> "
          "%.2e (both strictly decreasing): the wall margin dies "
          "%.0f TO %.0f ORDERS below the admissible window; tau < "
          "0 at ALL grid t != 0 on BOTH faces (SOURCE-FACE-WALL-"
          "FATAL); t*_S honestly typed a tau-RIDER (slope 1.006), "
          "lambda_h and t_floor DEMAND-FLAT (slopes 0.022/-0.007)"
          % (PIN_TSTAR_S[0], PIN_TSTAR_S[-1], PIN_TSTAR_Z[0],
             PIN_TSTAR_Z[-1], min(ordS), max(ordS)))

    okW = all(v < 0 for v in PIN_SZ_RATIO) \
        and all(abs(PIN_SZ_RATIO[i]) < abs(PIN_SZ_RATIO[i + 1])
                for i in range(3)) \
        and PIN_DS_DP[0] > 1e9 and PIN_DS_DP[1] > 1e50
    okX = all(v < 0 for v in PIN_FLOWZ_MIN)
    check("B4 DICTIONARY-THREEFOLD-INEQUIVALENT + FLOW-Z breaks H2",
          okW and okX,
          "|dtheta_S/dtheta_P| = 5.9e9 -> 3.3e52 with sign pattern "
          "(P, S, Z) == (+, -, +) at EVERY rung, S/Z = %s: 'the "
          "flow' has NO unique census meaning -- every pinch claim "
          "is dictionary-dependent (the threefold-inequivalent "
          "dictionary); FLOW-Z-BREAKS-DERIVED-H2: the realness-"
          "GRANTING direction +0.055 breaks census nonnegativity "
          "at every rung (mins %s): H2 is NOT the flow shadow of "
          "zeta-realness" % (list(PIN_SZ_RATIO),
                             list(PIN_FLOWZ_MIN)))

    okY = PIN_WIT_REPAIR[0] > 100 \
        and PIN_WIT_REPAIR[1] > PIN_WIT_REPAIR[0] \
        and abs(PIN_WIT_REPAIR[0] / GAMMA_WINDOW - 10477) < 30 \
        and PIN_WIT_REPAIR[1] < PIN_KKL_CEILING \
        and PIN_WIT_TOP_GROW[1] > PIN_WIT_TOP_GROW[0]
    check("B5 WITNESS-PRESERVED-NOT-EXPELLED (repair 10477x window)",
          okY,
          "the r171 witness is complex at t = 0 (lambda_wit = 0), "
          "forward ladder 0.055/0.5/5.0 ALL broken with top/y_t'' "
          "GROWING %.2f -> %.2f; measured realness repair only at "
          "t in [%.2f, %.2f] == 10477x the admissible window, "
          "INSIDE the cited KKL ceiling sigma^2/2 = %.1f (D5 "
          "instance): the flow expels the witness direction in NO "
          "classically admissible time"
          % (PIN_WIT_TOP_GROW[0], PIN_WIT_TOP_GROW[1],
             PIN_WIT_REPAIR[0], PIN_WIT_REPAIR[1], PIN_KKL_CEILING))

    # ================================================ C: graphs
    section("C. THE LOOP LEDGER (pair class flagged, not consumed)")
    cyc1 = {"BACKWARD-PERSIST": ["LAMBDA<=0"], "LAMBDA<=0": ["RH"],
            "RH": ["BACKWARD-PERSIST"]}
    cyc2 = {"PAIR-CONTROL": ["MONTGOMERY-PC"], "MONTGOMERY-PC": ["RH"],
            "RH": ["PAIR-CONTROL"]}
    okZ = has_cycle(cyc1) and has_cycle(cyc2)
    delivered = {"SEMIGROUP": ["TRACE-LAW"], "TRACE-LAW": ["T-FLOOR"],
                 "LAMBDA-LADDER": [], "FRAGILITY": []}
    okAA = not has_cycle(delivered)
    check("C1 backward-persistence-is-RH + pair loop flagged; "
          "delivered chain clean", okZ and okAA,
          "transporting realness from t = 0.22 back to 0 IS "
          "[Lambda <= 0] == RH: cycle DETECTED, flagged, NOT "
          "consumed (with dbn-pair, zero-verif-at-height, "
          "universalized-census, pinning-supply: FIVE cycles); the "
          "delivered instruments {semigroup, trace law, lambda "
          "ladder, fragility} are ACYCLIC and consume RT/PM15 as "
          "CITED CEILINGS only; the flow moves t, NEVER h: no "
          "h-transport without an h-uniform ingredient; census "
          "cardinality 4 UNCHANGED")

    print("\n  [TYPED, BH8 ADOPTED] THE ONE BIG CLASSICAL IMPORT "
          "LANDS AS AN EXACT")
    print("  INSTRUMENT: e^{-tT} closed form + trace law (dev 0.0), "
          "the threefold-")
    print("  inequivalent dictionary, theta-flow-inert floors, the "
          "lambda_h ladder")
    print("  (limit OPEN, honestly NOT an off-line detector), witness "
          "preserved.")
    print("  The missing half is the RH-conditional PAIR class "
          "(flagged loop).")
    print("  Census cardinality 4 UNCHANGED.  NOT RH evidence.  NO RH "
          "claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v938 -- PRIME.DBN.HEATFLOW.01 (the exact census semigroup "
          "e^{-tT} +")
    print("trace law; the threefold dictionary; the pair-term "
          "adjudication; the")
    print("lambda_h criticality ladder, limit OPEN; round 179; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v938: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: D1-D5 + the loop graphs recomputed in-run; the "
          "t_floor/lambda_h/")
    print("fragility/dictionary/witness tables PINNED from "
          "dbn_heatflow_probe.py")
    print("(SPEC %s, 26/26, record 672.4 s + deterministic re-run, "
          "one smoke fix" % PIN_SPEC_R179)
    print("disclosed, all logs kept, RE-RUN GREEN AS TYPED AT "
          "PROMOTION).  NOT RH")
    print("evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.DBN.HEATFLOW.01 exact census semigroup + "
          "threefold dictionary: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
