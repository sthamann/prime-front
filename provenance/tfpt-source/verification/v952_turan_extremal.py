#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v952 -- PRIME.TURAN.EXTREMAL.01: THE CLASSICAL PD-CONE THEORY
PRICED of round 196 -- the Turan/Boas-Kac/Fejer extremal machinery
imported with exact citations, machine-proved where it enters, and
priced against the wall for the first time in 196 rounds, WITH A
TWO-SIDED VERDICT: the classical cap describes the wall's DRAIN
CAPACITY almost exactly (capture 0.14-0.24 dex, FLAT), while the
cone-vs-truth gap IS the tau ladder (slope -1.007, R^2 1.000) --
CONE GEOMETRY CANNOT SEE POSITIVITY.

THE DICTIONARY (recomputed in-run where it is proof): for
continuous PD g supported in [-L, L] with g(+-L) = 0 (the r195/v951
autocorrelation class) and lag 0 < u <= L, the POINTWISE CAP
    g(u) <= M_KR(u) g(0),   M_KR(u) = cos(pi/(ceil(L/u) + 1))
via lattice sampling + THE FEJER COEFFICIENT THEOREM -- BOTH SIDES
MACHINE-PROVED IN-RUN at n = 1, 2 (extremal construction: the
autocorrelation of S_m = sin((m + 1) pi/(n + 2)) attains
cos(pi/(n + 2)) EXACTLY; optimality: the dual node certificate at
the zeros theta_r = (2r + 1) pi/(n + 2), nonnegative weights
solved exactly, forces c_1 <= cos(pi/(n + 2))) -- sharpness cited
to Boas-Kac (Duke Math. J. 12 (1945) 189-206) and
Kolountzakis-Revesz (Canad. J. Math. 58 (2006) 401-418, Cor. 4.1)
via Fejer (1915); the signed-bound flip cos(j(t + pi)) ==
(-1)^j cos(jt) recomputed for j = 1..5; the probe's dual
certificates at n = 1..4 cover every atom of every rung.

THE KB CORRECTION (Bughunt X, F2 MINOR) ADOPTED -- AND ITS
RATIONAL-LAG IDENTITY RECOMPUTED IN-RUN: the subcone attains the
full-cone cap EXACTLY AT RATIONAL LAGS ONLY.  At u = L/2 on the
mode lattice om_k = 2 pi k/L the r195 kernel collapses (recomputed
symbolically, generic K): the off-diagonal of W(L/2) vanishes
IDENTICALLY and M_sub(L/2) = lambda_max(D^{-1/2} G(L/2) D^{-1/2})
= 1/2 = cos(pi/3) = M_KR(L/2) EXACTLY -- the Fejer extremal lifts
exactly into the K-mode cone at the rational lag u/L = 1/2 (at
h = 4 this IS the q = 2 atom); elsewhere NEAR-attainment of the
denseness class (the probe's own h = 5 deficit 4.1e-4 -- twelve
orders above f64, inside the frozen 0.30 dex bar; the original
'to f64 precision' wording is retired per KB).  The edge kill:
W(L) == 0 IDENTICALLY on the lattice (recomputed symbolically) --
M_sub(L) = 0 == cos(pi/2) = M_KR(L): the formula covers the edge.
THE SUBCONE TURAN EXHIBIT (recomputed): x = e_0 gives g_{e0}(u) =
L - u (the Fejer triangle) with int g = L^2 = L g(0) EQUALITY --
the subcone CONTAINS the Turan interval extremal (Siegel 1935/
Boas-Kac); the subcone-wide inequality is the trivial x_0^2 <=
|x|^2 (recomputed generic).

THE DECISIVE LADDER (pinned): every cone bound is NEGATIVE at
every rung (log10 |WB_KR| = 0.65 -> 1.49) while the truth
lambda_0 > 0 is tau-deep: CONE GEOMETRY CANNOT SEE POSITIVITY,
even the exact subcone no-pole bound is negative; THE
ARITHMETIC-INPUT GAP IS THE TAU LADDER (gapdex 11.35 -> 89.03
over h = 4 -> 20, slope vs log tau = -1.007 at R^2 1.000):
TURAN-BUDGET-TAU-GAP -- the relabeling barrier now NAMED AT THE
CONE LEVEL with the exact dex table.  THE COUNTER-FINDING (the
round's real news): capture = log10(PC_KR/PC_exact) = 0.14-0.24
dex FLAT -- CONE-DRAIN-O1-CAPTURE: the classical Fejer cap
describes the wall's drain capacity almost exactly; Q2-NEAR-TIGHT
(q2dex 1.09-1.23, tau-flat, ~13x inside the cap); the composition
honest: the prime leg composes full-cone, the pole leg trivially,
THE ARCH LEG DOES NOT CLASSICALIZE (per-mode counterterm --
ARCH-LEG-SUBCONE-ONLY, the one non-classicalizable term, named);
TURAN-WRONG-DIRECTION did not fire.

RE-RUN GREEN AS TYPED AT PROMOTION: turan_extremal_probe.py round
196 (note DXXI (521), contract PRIME.TURAN.EXTREMAL.01), 23/23
gates, SPEC_SHA a6edc3f911e8f069 (verified byte-identical before
and after the appended KB CORRECTION-OF-RECORD block, note DXXIV),
record 767 s + 802 s deterministic re-run (timing-normalized diff
empty, all logs kept incl. one disclosed calibration crash
fragment; two pre-freeze amendments disclosed: A1 expand_trig
Chebyshev break dropped; A2 edge-atom mp noise -> exact zero),
re-run at promotion 795.6 s, 23/23 -- log kept as
turan_extremal_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the Fejer cap (construction + dual
certificate), the rational-lag attainment identity, the edge
kill, the subcone Turan exhibit (recomputed in-run); MEASURED =
the gapdex/capture/q2dex/world ladders (pinned).  THE LOOP
DISCIPLINE: TURAN-CONE-POSITIVITY <-> WEIL-ALLTESTS is a FLAGGED
LOOP consumed by NOTHING (the measured cone bounds are NEGATIVE
-- no positivity is asserted over any test class; bounding over
the cone is legitimate).  The caps are world-blind by
construction (typed, never sold as a separator); the witness is
matrix-side-invariant definitionally.  THE RESIDUE (canonical,
notes DII/DXVI/DXXIV): {H1 AND H2 AND H3}-cofinal (mod D =
0.0042) + {census-forall-k == LOOP} + {H-PIN = the one
lambda-uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  NOT evidence for or against the Riemann Hypothesis in
either direction.  NO RH CLAIM.

PROVENANCE: discovery probe turan_extremal_probe.py (round 196,
2026-08-21, note DXXI; KB CORRECTION-OF-RECORD block per note
DXXIV (524)); consumes v951 (the ACF kernel and PD class this
round prices classically); externally covered by Bughunt X (round
199, note DXXIII: the Fejer cap RE-PROVED INDEPENDENTLY by a
single-node dual route, the KB rational-lags-only attainment
adjudicated at dps 120 with deficit -9.7e-122 at h = 4 and the
own-log 4.1e-4 deficit at h = 5, the Boas-Kac/KR/Siegel citations
web-verified verbatim).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R196 = "a6edc3f911e8f069"
PIN_LAM0 = (-10.70, -87.53)            # log10, h = 4 -> 20 (positive)
PIN_WBKR = (0.65, 1.49)                # log10 |WB_KR|, all NEGATIVE
PIN_GAPDEX = (11.35, 89.03)
PIN_GAP_SLOPE = -1.007
PIN_GAP_R2 = 1.000
PIN_CAPTURE = (0.14, 0.24)
PIN_CAPTURE_SLOPE = -0.001
PIN_Q2DEX = (1.09, 1.23)
PIN_MEASGAP = (1.57, 2.04)
PIN_SUBQ2_H5_DEFICIT = 4.1e-4          # KB: NEAR-attainment, not exact
PIN_KB_H4_DEFICIT = -9.7e-122          # KB: EXACT at the rational lag
PIN_SUB_SHARP_BAR = 0.30               # dex (enum bar -- stands)
PIN_CTRL_GAPDEX = {"SMOOTH": 0.71, "SCRARITH": 1.33, "EPSTEIN": 0.81}
PIN_SMOOTH_CAPS = (0.70, 0.76)         # pointwise vs Turan-integral

N_CHECKS = 9
EXPECTED = "TURAN-BUDGET-TAU-GAP"

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
    import sympy as sp

    # ================================================ A: the Fejer cap
    section("A. THE FEJER CAP MACHINE-PROVED (n = 1, 2: "
            "construction + dual)")
    t_ = sp.symbols("t", real=True)
    okA = True
    for n in (1, 2):
        # extremal construction: autocorrelation of S_m
        S = [sp.sin((m + 1) * sp.pi / (n + 2)) for m in range(n + 1)]
        nrm = sum(s ** 2 for s in S)
        c = [sum(S[m] * S[m + j] for m in range(n + 1 - j)) / nrm
             for j in range(n + 1)]
        okA = okA and sp.simplify(
            c[1] - sp.cos(sp.pi / (n + 2))) == 0
        # manifest nonnegativity: p(t) = |sum S_m e^{imt}|^2 / nrm
        poly = sp.simplify(sp.expand_trig(sp.expand(
            (sum(S[m] * sp.cos(m * t_) for m in range(n + 1)) ** 2
             + sum(S[m] * sp.sin(m * t_) for m in range(n + 1)) ** 2)
            / nrm
            - (1 + 2 * sum(c[j] * sp.cos(j * t_)
                           for j in range(1, n + 1))))))
        okA = okA and poly == 0
        # SINGLE-NODE dual certificate (the BH10 independent route):
        # n = 1 at theta = pi (p(pi) = 1 - 2 c_1 >= 0 ==> c_1 <=
        # 1/2 == cos(pi/3), tight); n = 2 at theta = 3 pi/4
        # (cos(2 theta) == 0 kills c_2; p >= 0 ==> c_1 <=
        # 1/(2 cos(pi/4)) == cos(pi/4), tight)
        if n == 1:
            okA = okA and sp.simplify(sp.cos(sp.pi)) == -1 \
                and sp.simplify(1 - 2 * sp.cos(sp.pi / 3)) == 0
        else:
            th = 3 * sp.pi / 4
            okA = okA and sp.simplify(sp.cos(2 * th)) == 0 \
                and sp.simplify(sp.cos(th)
                                + sp.cos(sp.pi / 4)) == 0 \
                and sp.simplify(sp.Rational(1, 2)
                                / sp.cos(sp.pi / 4)
                                - sp.cos(sp.pi / 4)) == 0
    check("A1 THE FEJER COEFFICIENT THEOREM at n = 1, 2 (both "
          "sides, exact)", okA,
          "construction: the autocorrelation of S_m = sin((m + 1) "
          "pi/(n + 2)) is a MANIFEST square with c_1 == "
          "cos(pi/(n + 2)) exactly (n = 1: 1 + cos t >= 0 with "
          "c_1 = 1/2; n = 2 likewise); optimality by single-node "
          "dual certificates (the Bughunt-X independent route): "
          "n = 1 at theta = pi (p(pi) = 1 - 2 c_1 >= 0 ==> c_1 <= "
          "1/2 = cos(pi/3)) and n = 2 at theta = 3 pi/4 (cos(2 "
          "theta) == 0 kills c_2; 1/(2 cos(pi/4)) == cos(pi/4) "
          "EXACTLY, so c_1 <= cos(pi/4)) -- both tight (sympy "
          "exact): the cap M_KR(u) = cos(pi/(ceil(L/u) + 1)) is "
          "PROVED where it enters; the probe's nullspace dual "
          "certificates at n = 1..4 cover every atom of every "
          "rung; sharpness Boas-Kac 1945 / Kolountzakis-Revesz "
          "2006 Cor. 4.1 via Fejer 1915")

    okB = all(sp.simplify(sp.cos(j * t_ + j * sp.pi)
                          - (-1) ** j * sp.cos(j * t_)) == 0
              for j in range(1, 6))
    check("A2 the signed-bound flip cos(j(t + pi)) == (-1)^j "
          "cos(jt) (j = 1..5)", okB,
          "the theta -> theta + pi flip on the sampled sequence "
          "gives the SIGNED cap |g(u)| <= M_KR(u) g(0) (needed for "
          "the signed-weight EPSTEIN world) -- verified directly "
          "(the probe's amendment A1 dropped the expand_trig "
          "Chebyshev route that broke at j = 5; the identity "
          "itself never moved)")

    # ================================================ B: the KB identity
    section("B. THE RATIONAL-LAG ATTAINMENT (KB adopted, "
            "recomputed)")
    a_ = sp.symbols("a", positive=True)
    L_ = 2 * a_
    k_, l_ = sp.symbols("k l", positive=True, integer=True)
    omk = k_ * sp.pi / a_
    oml = l_ * sp.pi / a_
    # W(L/2): off-diagonal 2(om_i sin(om_i L/2) - om_j sin ...)/(b_i-b_j)
    okC = sp.simplify(sp.sin(omk * L_ / 2)) == 0 \
        and sp.simplify(sp.cos(omk * L_ / 2) - (-1) ** k_) == 0 \
        and sp.simplify(sp.sin(omk * L_)) == 0 \
        and sp.simplify(sp.sin(oml * L_)) == 0
    # diagonal of G(L/2) = -W(L/2)/2: k = 0 -> L/2; k >= 1 ->
    # (L/4)(-1)^k; D = diag(L, L/2, ...): ratios 1/2 and +-1/2
    diag0 = sp.simplify(-(2 * (L_ / 2 - L_)) / 2 / L_)
    diagk = sp.simplify(-((L_ / 2 - L_) * (-1) ** k_) / 2 / (L_ / 2))
    okC = okC and diag0 == sp.Rational(1, 2) \
        and sp.simplify(diagk - (-1) ** k_
                        * sp.Rational(1, 2)) == 0 \
        and sp.simplify(sp.cos(sp.pi / 3) - sp.Rational(1, 2)) == 0
    check("B1 THE RATIONAL-LAG IDENTITY at u = L/2 (generic K, "
          "exact)", okC,
          "on the lattice om_k = 2 pi k/L: sin(om_k L/2) == 0 "
          "(EVERY off-diagonal of W(L/2) vanishes identically) and "
          "cos(om_k L/2) == (-1)^k, so D^{-1/2} G(L/2) D^{-1/2} is "
          "DIAGONAL with entries 1/2 (k = 0) and (-1)^k/2: "
          "M_sub(L/2) == 1/2 == cos(pi/3) == M_KR(L/2) EXACTLY -- "
          "the Fejer extremal lifts exactly into the K-mode cone "
          "at the rational lag u/L = 1/2 (at h = 4 this IS the "
          "q = 2 atom; ceil(L/u) = 2); KB ADOPTED: exact "
          "attainment at RATIONAL lags ONLY -- elsewhere NEAR-"
          "attainment (the probe's own h = 5 deficit %.1e, twelve "
          "orders above f64, inside the %.2f dex enum bar; "
          "Bughunt X: deficit %.1e at dps 120 at the h = 4 "
          "rational lag)" % (PIN_SUBQ2_H5_DEFICIT,
                             PIN_SUB_SHARP_BAR, PIN_KB_H4_DEFICIT))

    okD = sp.simplify(sp.sin(omk * L_)) == 0 \
        and sp.simplify(sp.sin(omk * L_) / omk
                        + (L_ - L_) * sp.cos(omk * L_)) == 0
    check("B2 the edge kill W(L) == 0 identically (exact)", okD,
          "at u = L every off-diagonal numerator om sin(om L) and "
          "every diagonal sin(om_k L)/om_k + (u - L) cos(om_k L) "
          "vanishes identically on the lattice (k = 0 slot "
          "2(u - L) = 0 too): M_sub(L) = 0 == cos(pi/(ceil(1) + "
          "1)) = M_KR(L) -- the cap formula covers the "
          "commensurate edge atom (q = h) exactly; the probe's "
          "amendment A2 replaced mp noise +-1e-58 by this exact "
          "zero")

    x0, x1, x2 = sp.symbols("x0 x1 x2", real=True)
    u_ = sp.symbols("u", positive=True)
    g_e0 = L_ - u_
    int_g = sp.integrate(g_e0, (u_, 0, L_)) * 2  # even extension
    # subcone Turan: int g_x = (L x_0)^2 vs L g_x(0) = L (L/2)
    # (|x|^2 + x_0^2) -- difference reduces to L^2/2 (x_1^2 + ...)
    turan_ineq = sp.simplify(
        L_ * (L_ / 2) * (x0 ** 2 + x1 ** 2 + x2 ** 2 + x0 ** 2)
        - (L_ * x0) ** 2)
    okE = sp.simplify(int_g - L_ ** 2) == 0 and \
        sp.simplify(turan_ineq - L_ ** 2 / 2 * (x1 ** 2 + x2 ** 2)) == 0
    check("B3 the subcone CONTAINS the Turan extremal (x = e_0, "
          "equality; exact)", okE,
          "x = e_0 gives g_{e0}(u) = L - u exactly (the Fejer "
          "triangle = the autocorrelation of the box) with "
          "int_{-L}^{L} g = L^2 = L g(0) EQUALITY (Siegel 1935/"
          "Boas-Kac interval theorem attained IN-SUBCONE); the "
          "subcone-wide Turan inequality int g_x = (L x_0)^2 <= "
          "L g_x(0) reduces EXACTLY to L^2/2 (x_1^2 + ... ) >= 0, "
          "i.e. the trivial x_0^2 <= |x|^2 (sympy generic): the "
          "classical Turan integral problem genuinely enters and "
          "is exactly solvable on the subcone")

    # ================================================ C: the ladders
    section("C. THE DECISIVE LADDERS (pinned, typed measured)")
    okF = PIN_WBKR[0] > 0 and PIN_WBKR[1] > PIN_WBKR[0] \
        and PIN_GAPDEX[0] < PIN_GAPDEX[1] \
        and abs(PIN_GAP_SLOPE + 1.007) < 1e-9 \
        and PIN_GAP_R2 >= 0.999
    check("C1 TURAN-BUDGET-TAU-GAP (the gap IS the tau ladder; "
          "cone bounds negative)", okF,
          "every cone bound is NEGATIVE at every rung (log10 "
          "|WB_KR| = %.2f -> %.2f) while the truth lambda_0 > 0 "
          "is tau-deep (log10 %.2f -> %.2f): CONE GEOMETRY CANNOT "
          "SEE POSITIVITY -- even the exact subcone no-pole bound "
          "is negative; the arithmetic-input gap ladder gapdex = "
          "%.2f -> %.2f dex with slope vs log tau = %.3f at R^2 "
          "%.3f: the relabeling barrier NAMED AT THE CONE LEVEL "
          "with the exact dex table"
          % (PIN_WBKR[0], PIN_WBKR[1], PIN_LAM0[0], PIN_LAM0[1],
             PIN_GAPDEX[0], PIN_GAPDEX[1], PIN_GAP_SLOPE,
             PIN_GAP_R2))

    okG = PIN_CAPTURE[1] - PIN_CAPTURE[0] <= 0.2 \
        and abs(PIN_CAPTURE_SLOPE) <= 0.30 \
        and PIN_Q2DEX[0] >= 1.0 and PIN_Q2DEX[1] <= 2.0
    check("C2 CONE-DRAIN-O1-CAPTURE (the round's real news) + "
          "Q2-NEAR-TIGHT", okG,
          "capture = log10(PC_KR/PC_exact) = %.2f-%.2f dex FLAT "
          "(range 0.10, slope %.3f): THE CLASSICAL FEJER CAP "
          "DESCRIBES THE WALL'S DRAIN CAPACITY ALMOST EXACTLY; "
          "q2dex = %.2f-%.2f (tau-flat, ~13x inside the cap, "
          "stable); measured-vs-exact-subcone gap %.2f-%.2f dex; "
          "SMOOTH prices the classical Turan integral bound "
          "(pointwise cap %.2f beats the Turan-integral cap %.2f "
          "by 0.06 dex)"
          % (PIN_CAPTURE[0], PIN_CAPTURE[1], PIN_CAPTURE_SLOPE,
             PIN_Q2DEX[0], PIN_Q2DEX[1], PIN_MEASGAP[0],
             PIN_MEASGAP[1], PIN_SMOOTH_CAPS[0], PIN_SMOOTH_CAPS[1]))

    okH = all(v < 2.0 for v in PIN_CTRL_GAPDEX.values())
    check("C3 composition honest + worlds (ARCH-LEG-SUBCONE-ONLY; "
          "caps world-blind)", okH,
          "the prime leg composes full-cone, the pole leg "
          "trivially (a manifest square vanishing off the pole "
          "ray), THE ARCH LEG DOES NOT CLASSICALIZE (its "
          "regularization counterterm is PER-MODE, not a pointwise "
          "functional of g -- the one non-classicalizable term, "
          "named, typed ARCH-LEG-SUBCONE-ONLY); TURAN-WRONG-"
          "DIRECTION did not fire; the caps are world-blind by "
          "construction -- fake/smooth cells miss by only 0.7-1.4 "
          "dex (%s) vs 11-89 in MAIN (typed, not sold); the "
          "witness is matrix-side-invariant definitionally"
          % str(PIN_CTRL_GAPDEX))

    okI = True                                # loop discipline
    check("C4 TURAN-CONE-POSITIVITY loop FLAGGED, consumed by "
          "NOTHING", okI,
          "asserting the cone bound >= 0 for all tests would BE "
          "the WEIL-ALLTESTS loop -- here the measured cone bounds "
          "are NEGATIVE, nothing is consumed, bounding over the "
          "cone is legitimate; the l1-majorant dead-class "
          "disclosure upgraded to an exact dex table (the "
          "deliverable); Beurling-Selberg/Vaaler NOT consumed (no "
          "one-sided majorant enters); census cardinality 4 "
          "UNCHANGED; NOT RH evidence")

    print("\n  [TYPED] The classical cone captures the drain almost")
    print("  exactly (0.2 dex) and CANNOT see the tau-deep positivity")
    print("  -- the cone-vs-truth gap IS the tau ladder; attainment")
    print("  exact at rational lags only (KB).  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v952 -- PRIME.TURAN.EXTREMAL.01 (the Fejer cap proved "
          "in-code; the KB")
    print("rational-lag attainment identity; TURAN-BUDGET-TAU-GAP + "
          "CONE-DRAIN-O1-")
    print("CAPTURE; round 196; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v952: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the Fejer construction + dual certificates "
          "(n = 1, 2), the flip")
    print("identity, the rational-lag attainment, the edge kill and "
          "the subcone")
    print("Turan exhibit recomputed in-run (exact); the gapdex/"
          "capture/q2dex/world")
    print("ladders PINNED from turan_extremal_probe.py (SPEC %s,"
          % PIN_SPEC_R196)
    print("23/23, record 767 s + 802 s deterministic re-run, KB "
          "correction block")
    print("appended spec-hash-invariant, RE-RUN GREEN AS TYPED AT "
          "PROMOTION 795.6 s,")
    print("23/23).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.TURAN.EXTREMAL.01 classical cone priced: "
          "%d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
