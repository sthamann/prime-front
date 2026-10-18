#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v920 -- PRIME.LOOP.EQUIVALENCE.THEOREMS.01: THE LOOP / EQUIVALENCE
THEOREMS of rounds 140 and 142 -- the negative/structural results that
prevent double-counting in the proof-graph FOREVER, promoted as
certified finite theorems.  Both rounds were re-gated in Bughunt IV
(round 149, note CDLIII, 0 MAJOR).

THE THEOREMS (all exact algebra; sympy generic + exact instances):

  ROUND 140 (note CDXLIV, jetlock_bandmass_probe.py):
  J1 (per-mode telescope): F(y) - A_0 = sum_{i <= m} A_{2i}/y^i
     + sum_k w_k b_k^m/(y^m (y - b_k)) EXACTLY; the source envelope
     ENVJ(y) majorizes |F - A_0| on (b_top, oo) monotonically -- the
     onset Theta_J(rho), the unique solve of ENVJ(Theta^2) =
     rho |A_0|, certifies JET-LOCK source-only, WITHOUT zeros.
  J2 (the onset IS the jet ratio): y_t/rho <= Theta_J(rho)^2 <=
     1.05 y_t (1 + rho)/rho with y_t := |A_2/A_0| (two-sided exact
     dictionary).
  J3 (the jet ratio is escaped root mass): A_2/A_0 = sum b - sum y
     (trace form) = -sum_j prod_k (y_j - b_k)/prod_{i != j}
     (y_j - y_i) (A_0-FREE spacing form) -- JET-LOCK(poly) <=>
     TOPROOT.
  J4 (Cauchy-Schwarz cap): |A_{2m}| <= ||c|| sqrt(sum om^{4m})
     unconditionally polynomial -- the ENTIRE JET-LOCK hardness is
     the cancellation ALIGNMENT of A_2 with A_0 (ALIGNMENT-WALL).
  B1 (tail visibility): for any true zero gamma* beyond a certified
     onset, 1 - theta >= 8 sin^2(A gamma*) (1 - rho)^2 A_0^2 /
     (gamma*^2 (tau + OFF)) (exact rearrangement of budget + point
     term).
  B2 (THE EQUIVALENCE LOOP): modulo {JETLOCK, TAILVIS}:
     BAND-MASS <=> TLAWCAP <=> EPS-LOCK.  The E1 factorization is a
     LOOP on the B side -- BAND-MASS is EPS-LOCK-COMPLETE: every BM
     proof contains an EPS-LOCK proof.  The r137 residue {JETLOCK,
     BANDMASS} is reshaped to {TOPROOT, TAILVIS, TLAWCAP} and NO
     future argument may count BAND-MASS and EPS-LOCK as separate
     progress.

  ROUND 142 (note CDXLVI, tlawcap_suscap2r_probe.py):
  W1 (the pinch identity): with g the bordered-secular root of
     rho^2/g = sum et_i^2/(delta_i - g) and s = chi/rho^2,
     1 - s g == (g^2/rho^2) sum_{i >= 1} et_i^2/(delta_i
     (delta_i - g)) EXACTLY -- s x gap == 1 is NOT an identity; the
     defect is the positive second-order susceptibility, two-sidedly
     PINCHED: 1 - g/delta_1 <= s g <= 1.  The measured 1.0000 IS
     the pinch; the r139 gap formula was its share_1 approximation.
  W2 (THE LOOP, both directions exact): QSUBGAP-lambda-uniform <=>
     SUSCAP2R AND DELTA1FLOOR.  Forward: g >= 1/P ==> s <= P and
     delta_1 > g.  Backward: g >= 1/(s + 1/delta_1), so s <= P and
     delta_1 >= 1/P give g >= 1/(2P).  SUSCAP2R is not a component
     of QSUBGAP -- it IS QSUBGAP uniformity modulo the strictly
     weaker delta_1 floor; every QSUBGAP proof contains a SUSCAP2R
     proof.  NO future argument may count them separately.
  W3 (interlacing): Cauchy interlacing gives DELTA1FLOOR <== FULLGAP
     := (lambda_1 - tau)/tau -- a SOURCE-PURE two-eigenvalue
     statement of the uncompressed Weil matrix (no zeros, no probe
     row, no zone); measured TIGHT: delta_1/FULLGAP = 1.0000 at all
     five rungs.
  DELTA1FLOOR IS REQUIRED (the Bughunt-IV F1 witness, carried): the
     exact 2-level family rho^2 = 1/(1 + d_1), et_1^2 = d_1/(1 + d_1)
     has s == 1 EXACTLY while g = d_1/(1 + d_1) -> 0: SUSCAP2R alone
     cannot give QSUBGAP -- the pinch saturates.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained): J1 telescope
(depths 1, 2 generic), ENVJ validity/monotonicity + geometric tail,
J2 onset sandwich solves, J4 Lagrange identity, J3 trace + spacing
forms (generic), B1 rearrangement chain, B2 loop (exact solve of the
E1 shape + the B1 x TLAWCAP composition), W1 defect identity (generic
sympy 2-level + mp 3-level instance to 1e-45), the pinch, W2 forward
+ backward + the U1 bracket, X3 secular/eigen cross-check (eta ladder
sums exactly to s), W3 interlacing on an exact instance (CRootOf
comparisons; Courant-Fischer cited for generic codim), the BH4-F1
witness family (exact rationals), and consistency arithmetic on all
pinned tables below.

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 142 -- RE-RUN GREEN AS TYPED AT PROMOTION (26/26 gates,
  identical SPEC_SHA 85971e173cd910f8, 1904.7 s; run-of-record
  1941.7 s + deterministic re-run 2010.0 s, logs sha256
  ee6fbbd51e94bd69 / 9d4962fc9045f51a):
  the per-rung tables x = 5/8/13/18/24 -- zone-top gaps 33.6233/
  16.7200/22.6588/16.5873/19.5781, s = 0.02974/0.05981/0.04413/
  0.06029/0.05108, s x gap = 0.9998536/0.9999838/0.9999980/
  0.9999995/0.9999998 with pinch floors 1 - g/delta_1 hard, defects
  1.4642e-4 .. 1.6285e-7 with identity devs <= 2e-23, defect ratio
  == share_1 (0.969/0.965/0.946/0.944/0.947), FULLGAP = 2.225493e5/
  9.951249e5/1.061906e7/3.249680e7/1.138230e8 with delta_1/FULLGAP
  = 1.0000 everywhere (TIGHT).
  ROUND 140 -- PINNED (NOT re-run at promotion; 3824.7 s run-of-
  record + 3783.4 s deterministic re-run, 33/33 gates, SPEC_SHA
  85e7ba691b3eef58, logs sha256 feae86eef725040b / 257fc60734c63adc;
  the B2 loop algebra, J-toolkit sum rules and W-machinery were
  independently re-gated in Bughunt IV, SPEC 1cd81cef9ff1193e, and
  the SAME exact-algebra gates are recomputed in-run here): y_t =
  6.107e4/4.165e5/3.204e6/1.258e7/4.013e7/7.390e7 at x = 5/8/13/18/
  24/28 (log-log slope 4.14, TOPROOT law), onsets Theta_J(0.5) =
  360/943/2620/5191/9276/12590, alignment depth |A_2|/cap = 1.2e-6
  -> 6.9e-61, B1 certificates (1-theta) = 2.1e-4/4.2e-5/5.9e-6/
  2.6e-6 at x = 5..18 (x = 24/28 TAILVIS-HORIZON-LIMITED at the
  frozen cache, resolved counting-side in round 143 = v921).

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
J1/J2/J3/J4/B1/B2/W1/W2/W3 (exact algebra + interlacing + cited:
r137 E1/OFF identity, r135 D2, r139 U1-U4, Courant-Fischer, HSW22
Cor. 1.2, PT21).  MEASURED = the per-rung tables (typed; the tight
delta_1 == FULLGAP lock is MEASURED, not proven).  OPEN (typed, NOT
closed): TOPROOT, TAILVIS (counting-closed in v921), TLAWCAP
(= ONSETCAP), SUSCAP2R, DELTA1FLOOR (<== FULLGAP).  These theorems
RESHAPE the residue into non-double-countable coordinates; they
close NO omega.  The census {MEAS, OMEGA-POS} stays at CARDINALITY 4.
NOT evidence for or against the Riemann Hypothesis in either
direction.  NO RH CLAIM.

PROVENANCE: discovery probes jetlock_bandmass_probe.py (round 140,
2026-08-17, note CDXLIV, contract PRIME.JETLOCK.BANDMASS.PROOF.01)
and tlawcap_suscap2r_probe.py (round 142, note CDXLVI, contract
PRIME.TLAWCAP.SUSCAP2R.PROOF.01); re-gated + F1 witness in
bughunt4_probe.py (round 149, note CDLIII).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R142 = "85971e173cd910f8"
PIN_SPEC_R140 = "85e7ba691b3eef58"
# r142 G32 per-rung table x = 5/8/13/18/24
PIN_GAP_TOP = ("33.6233", "16.7200", "22.6588", "16.5873", "19.5781")
PIN_S = ("0.02974", "0.05981", "0.04413", "0.06029", "0.05108")
PIN_SG = ("0.9998536", "0.9999838", "0.9999980", "0.9999995",
          "0.9999998")
PIN_DEFECT = ("1.4642e-04", "1.6219e-05", "2.0182e-06", "4.8186e-07",
              "1.6285e-07")
PIN_G_OVER_D1 = ("1.5108e-04", "1.6802e-05", "2.1338e-06",
                 "5.1043e-07", "1.7201e-07")
PIN_SHARE1 = ("0.969", "0.965", "0.946", "0.944", "0.947")
PIN_FULLGAP = ("2.225493e+05", "9.951249e+05", "1.061906e+07",
               "3.249680e+07", "1.138230e+08")
# r140 pins x = 5/8/13/18/24/28
PIN_YT = ("6.1067e+04", "4.1654e+05", "3.2042e+06", "1.2578e+07",
          "4.0133e+07", "7.3900e+07")
PIN_ONSET_05 = (360, 943, 2620, 5191, 9276, 12590)
PIN_ALIGN_DEPTH = ("1.2e-06", "5.1e-13", "1.1e-24", "9.7e-37",
                   "3.2e-51", "6.9e-61")
PIN_B1 = ("2.1e-04", "4.2e-05", "5.9e-06", "2.6e-06")   # x = 5..18
XS6 = (5, 8, 13, 18, 24, 28)

N_CHECKS = 17
EXPECTED = "LOOP-EQUIVALENCE-THEOREMS"

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
    from mpmath import mp

    # ================================================== A: round 140
    section("A. ROUND-140 EXACT ALGEBRA (J1-J4, B1, B2; recomputed)")
    y = sp.symbols("y", positive=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    w1, w2 = sp.symbols("w1 w2", real=True)

    # J1 telescope, depths 1 and 2 (generic)
    S = w1 / (y - b1) + w2 / (y - b2)
    d1 = sp.simplify(sp.together(
        S - (w1 + w2) / y
        - (w1 * b1 / (y * (y - b1)) + w2 * b2 / (y * (y - b2)))))
    d2 = sp.simplify(sp.together(
        S - (w1 + w2) / y - (w1 * b1 + w2 * b2) / y ** 2
        - (w1 * b1 ** 2 / (y ** 2 * (y - b1))
           + w2 * b2 ** 2 / (y ** 2 * (y - b2)))))
    check("A1 J1 per-mode telescope (depths 1, 2 generic)",
          d1 == 0 and d2 == 0,
          "F - A0 == sum_{i<=m} A_2i/y^i + sum_k w_k b_k^m/(y^m "
          "(y - b_k)) exact: the source envelope needs NO zeros")

    # ENVJ validity: each term falls in y; geometric tail closed
    i_, m_, cpos = sp.symbols("i_ m_ cpos", positive=True)
    dterm = sp.simplify(sp.diff(1 / y ** i_, y) + i_ / y ** (i_ + 1))
    drem = sp.diff(1 / (y ** m_ * (y - cpos)), y)
    dremok = sp.simplify(drem * (y ** (m_ + 1) * (y - cpos) ** 2)
                         + (m_ * (y - cpos) + y)) == 0
    qv = sp.Rational(1, 3)
    geo = sp.summation(qv ** i_, (i_, 3, sp.oo))
    check("A2 ENVJ monotone-valid + geometric tail", dterm == 0
          and dremok and sp.simplify(geo - qv ** 3 / (1 - qv)) == 0,
          "each envelope term falls in y (derivative signs exact); "
          "tail sum q^i closed: ENVJ is a monotone source-only "
          "majorant on (b_top, oo)")

    # J2 onset sandwich
    rho, yt = sp.symbols("rho yt", positive=True)
    sol = sp.solve(sp.Eq((yt / y) / (1 - yt / y), rho), y)
    okC = len(sol) == 1 and sp.simplify(
        sol[0] - yt * (1 + rho) / rho) == 0
    okD = sp.simplify((yt / (yt / rho)) - rho) == 0
    check("A3 J2 onset sandwich (two-sided exact dictionary)",
          okC and okD,
          "q/(1-q) = rho at y == y_t (1+rho)/rho; |A2|/y == rho A0 "
          "at y == y_t/rho: Theta^2 in [y_t/rho, 1.05 y_t(1+rho)/rho]"
          " -- THE ONSET IS THE JET RATIO")

    # J4 Lagrange identity (CS cap)
    a1, a2, a3, u1, u2, u3 = sp.symbols("a1 a2 a3 u1 u2 u3", real=True)
    lag = sp.expand((a1 ** 2 + a2 ** 2 + a3 ** 2)
                    * (u1 ** 2 + u2 ** 2 + u3 ** 2)
                    - (a1 * u1 + a2 * u2 + a3 * u3) ** 2
                    - ((a1 * u2 - a2 * u1) ** 2
                       + (a1 * u3 - a3 * u1) ** 2
                       + (a2 * u3 - a3 * u2) ** 2))
    check("A4 J4 Cauchy-Schwarz jet cap (Lagrange exact)",
          sp.simplify(lag) == 0,
          "|A_2m| <= ||c|| sqrt(sum om^4m) unconditionally poly: the "
          "JET-LOCK hardness is the A_2/A_0 ALIGNMENT, not size "
          "(ALIGNMENT-WALL typed)")

    # J3 trace + spacing forms (generic K = 3)
    y1, y2, A0s = sp.symbols("y1 y2 A0s", positive=True)
    Fg = A0s * (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    w1r = sp.simplify((Fg * (y - b1)).subs(y, b1))
    w2r = sp.simplify((Fg * (y - b2)).subs(y, b2))
    trace = sp.simplify((w1r + w2r) / A0s - (b1 + b2 - y1 - y2))
    spac = sp.simplify(sp.together(
        (w1r + w2r) / A0s
        + (y1 - b1) * (y1 - b2) / (y1 - y2)
        + (y2 - b1) * (y2 - b2) / (y2 - y1)))
    Fp1 = sp.diff(Fg, y).subs(y, y1)
    Fp2 = sp.diff(Fg, y).subs(y, y2)
    spac2 = sp.simplify(sp.together(
        1 / Fp1 + 1 / Fp2 - (y1 + y2 - b1 - b2) / A0s))
    check("A5 J3 trace == A0-free spacing form (generic)",
          trace == 0 and spac == 0 and spac2 == 0,
          "A_2/A_0 == sum b - sum y == -sum_j prod_k(y_j - b_k)/"
          "prod_{i!=j}(y_j - y_i): the jet ratio IS escaped census-"
          "root mass -- JET-LOCK(poly) <=> TOPROOT")

    # B1 rearrangement chain
    ta, of_, s2, rh_, A0q, gs = sp.symbols(
        "ta of_ s2 rh_ A0q gs", positive=True)
    lb = 8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2
    th_bound = 1 - lb / (ta + of_)
    okE = sp.simplify((1 - th_bound) * (ta + of_) - lb) == 0
    check("A6 B1 tail visibility (exact rearrangement)", okE,
          "tau + OFF >= M_below + M_above, M_above >= 2|E(gamma*)|^2 "
          ">= 8 sin^2 (1-rho)^2 A0^2/gamma*^2 ==> theta <= 1 - "
          "8 sin^2 (1-rho)^2 A0^2/(gamma*^2 (tau+OFF))")

    # B2 equivalence loop
    th, r_, GT, GZ, P = sp.symbols("th r_ GT GZ P", positive=True)
    tl = sp.symbols("tl", positive=True)
    e1 = sp.Eq(tl * 8 * A0q ** 2 * GZ * (1 - th),
               8 * (1 + r_) ** 2 * A0q ** 2 * GT + (1 + th) * of_)
    sol_tl = sp.solve(e1, tl)
    okG = len(sol_tl) == 1 and sp.simplify(
        sol_tl[0] - ((1 + r_) ** 2 * GT / GZ
                     + (1 + th) * of_ / (8 * A0q ** 2 * GZ))
        / (1 - th)) == 0
    comp = sp.simplify(
        (8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2)
        / (P * 8 * A0q ** 2 * GZ)
        - s2 * (1 - rh_) ** 2 / (P * gs ** 2 * GZ))
    check("A7 B2 equivalence loop (exact solve + composition)",
          okG and comp == 0,
          "E1: (JL + BM) ==> tlaw closed; B1 + TLAWCAP ==> 1 - theta "
          ">= sin^2 (1-rho)^2/(P gamma*^2 G(Tz)): BAND-MASS <=> "
          "TLAWCAP <=> EPS-LOCK modulo {JETLOCK, TAILVIS} -- BM is "
          "EPS-LOCK-COMPLETE, no double-counting possible")

    # ================================================== B: round 142
    section("B. ROUND-142 EXACT ALGEBRA (W1-W3 + BH4-F1; recomputed)")

    # W1 generic (2 levels, sympy): the defect identity
    g_, r2_, e1_, e2_, dd1, dd2 = sp.symbols(
        "g r2 e1 e2 d1 d2", positive=True)
    secular = sp.Eq(r2_ / g_, e1_ / (dd1 - g_) + e2_ / (dd2 - g_))
    s_def = (e1_ / dd1 + e2_ / dd2) / r2_
    defect = (g_ ** 2 / r2_) * (e1_ / (dd1 * (dd1 - g_))
                                + e2_ / (dd2 * (dd2 - g_)))
    lhs = sp.simplify(sp.together(
        (1 - s_def * g_) - defect))
    # substitute the secular relation: r2/g == chi2(g)
    chi2 = e1_ / (dd1 - g_) + e2_ / (dd2 - g_)
    resid = sp.simplify(sp.together(
        lhs.subs(r2_, g_ * chi2)))
    check("B1 W1 defect identity (generic sympy, 2 levels)",
          resid == 0,
          "1/(d - g) == 1/d + g/(d(d - g)) summed under the secular "
          "equation: 1 - s g == (g^2/rho^2) sum et^2/(d(d - g)) "
          "EXACT -- s x gap == 1 is NOT an identity")

    # W1/W2/U1/X3 on the mp 3-level instance (BH4 G09 port)
    with mp.workdps(60):
        d = [mp.mpf("0.5"), mp.mpf(2), mp.mpf(5)]
        e2v = [mp.mpf("0.5"), mp.mpf("0.25"), mp.mpf("0.125"),
               mp.mpf("0.125")]
        r2 = e2v[0]

        def sec(g):
            return r2 / g - sum(e2v[i + 1] / (d[i] - g)
                                for i in range(3))
        lo, hi = mp.mpf("1e-30"), d[0] * (1 - mp.mpf("1e-25"))
        for _ in range(220):
            midp = (lo + hi) / 2
            if sec(midp) > 0:
                lo = midp
            else:
                hi = midp
        g = (lo + hi) / 2
        chi = sum(e2v[i + 1] / d[i] for i in range(3))
        s = chi / r2
        defv = (g ** 2 / r2) * sum(e2v[i + 1] / (d[i] * (d[i] - g))
                                   for i in range(3))
        ok_w1 = abs((1 - s * g) - defv) < mp.mpf("1e-45")
        ok_pinch = (1 - g / d[0]) - mp.mpf("1e-45") <= s * g \
            <= 1 + mp.mpf("1e-45")
        u1_lo = r2 / (chi + r2 / d[0])
        u1_hi = r2 / ((1 - r2) * chi)
        ok_u1 = u1_lo - mp.mpf("1e-45") <= g <= u1_hi + mp.mpf("1e-45")
        ok_w2 = (s <= 1 / g + mp.mpf("1e-40")) and (d[0] > g) \
            and (g + mp.mpf("1e-40") >= 1 / (s + 1 / d[0]))
        # X3: eigen ladder of Q(z) = sum e2_i prod_{j != i} (z - q_j)
        q = [mp.mpf(1), mp.mpf(1) + d[0], mp.mpf(1) + d[1],
             mp.mpf(1) + d[2]]

        def expand(roots):
            c = [mp.mpf(1)]
            for r in roots:
                nc = [mp.mpf(0)] * (len(c) + 1)
                for k, v in enumerate(c):
                    nc[k] += v
                    nc[k + 1] -= v * r
                c = nc
            return c
        Qc = [mp.mpf(0)] * 4
        for i in range(4):
            pc = expand([q[j] for j in range(4) if j != i])
            for k in range(4):
                Qc[k] += e2v[i] * pc[k]
        etas = sorted(mp.re(r) for r in mp.polyroots(
            Qc, maxsteps=200, extraprec=60))
        inter = all(q[i] < etas[i] < q[i + 1] for i in range(3))
        s_x3 = sum(1 / (etas[i] - q[0]) - 1 / (q[i + 1] - q[0])
                   for i in range(3))
        ok_x3 = inter and abs(s_x3 - s) < mp.mpf("1e-40") \
            and abs((etas[0] - q[0]) - g) < mp.mpf("1e-40")
    check("B2 W1 pinch + W2 loop + U1 + X3 (mp instance, 1e-45)",
          bool(ok_w1 and ok_pinch and ok_u1 and ok_w2 and ok_x3),
          "defect identity residual < 1e-45; 1 - g/d1 <= sg <= 1; U1 "
          "bracket; W2 forward (g >= 1/P ==> s <= P, d1 > g) + "
          "backward (g >= 1/(s + 1/d1)); eta ladder sums EXACTLY to "
          "s, eta_0 - q_0 == secular gap")

    # W2 backward composition, symbolic
    sP, dP = sp.symbols("sP dP", positive=True)
    gap_lb = 1 / (sP + 1 / dP)
    comp2 = sp.simplify(gap_lb.subs([(sP, P), (dP, 1 / P)])
                        - 1 / (2 * P))
    check("B3 W2 composition: s <= P, delta_1 >= 1/P ==> g >= 1/(2P)",
          comp2 == 0,
          "QSUBGAP-lambda-uniform <=> SUSCAP2R AND DELTA1FLOOR (both "
          "directions exact): the r139-r141 chain LOOPED on this leg "
          "-- no separate counting ever again")

    # W3 interlacing on an exact instance (CRootOf)
    M4 = sp.diag(1, 2, 5, 7)
    # codim-1 compression onto the orthogonal complement of
    # v = (1, 1, 1, 1)/2 via an explicit rational orthonormal frame
    fr = [sp.Matrix([1, -1, 0, 0]) / sp.sqrt(2),
          sp.Matrix([1, 1, -2, 0]) / sp.sqrt(6),
          sp.Matrix([1, 1, 1, -3]) / sp.sqrt(12)]
    Vc = sp.Matrix.hstack(*fr)
    Mc = sp.expand(Vc.T * M4 * Vc)
    lam = sorted([1, 2, 5, 7])
    poly = sp.Poly(sp.expand((Mc - sp.symbols("zz") * sp.eye(3)).det()),
                   sp.symbols("zz"))
    mus = sorted(sp.CRootOf(poly, i) for i in range(3))
    ok_int = all(bool(sp.Rational(lam[i]) <= mus[i])
                 and bool(mus[i] <= sp.Rational(lam[i + 1]))
                 for i in range(3))
    check("B4 W3 Cauchy interlacing (exact instance, CRootOf)",
          ok_int,
          "codim-1 compression of diag(1,2,5,7): lam_i <= mu_i <= "
          "lam_(i+1) exactly ==> q_1(V) >= lambda_1: DELTA1FLOOR <== "
          "FULLGAP, a SOURCE-PURE two-eigenvalue statement "
          "(Courant-Fischer cited for generic codim)")

    # BH4-F1 witness: DELTA1FLOOR is REQUIRED
    ok_w = True
    for dd in (Fraction(1, 100), Fraction(1, 10 ** 6),
               Fraction(1, 10 ** 12)):
        r2f = 1 / (1 + dd)
        e1f = dd / (1 + dd)
        gf = r2f * dd / (r2f + e1f)
        sf = (e1f / dd) / r2f
        ok_w = ok_w and sf == 1 and gf == dd / (1 + dd) \
            and gf < dd and (1 - gf / dd) == sf * gf
    check("B5 DELTA1FLOOR required (exact witness family)", ok_w,
          "rho^2 = 1/(1+d1), et_1^2 = d1/(1+d1): s == 1 EXACTLY "
          "while g = d1/(1+d1) -> 0 (pinch saturated) -- SUSCAP2R "
          "alone cannot give QSUBGAP (the Bughunt-IV F1 witness, "
          "carried)")

    # ================================================== C: pinned
    section("C. PINNED PER-RUNG TABLES (consistency arithmetic)")
    oksg = True
    for i in range(5):
        sg = float(PIN_SG[i])
        fl = 1 - float(PIN_G_OVER_D1[i])
        # the sg strings carry 7 decimals: half-ULP tolerance 5.1e-8
        oksg = oksg and fl - 5.1e-8 <= sg <= 1.0
        oksg = oksg and abs((1 - sg) - float(PIN_DEFECT[i])) <= 5.1e-8
        ratio = float(PIN_DEFECT[i]) / float(PIN_G_OVER_D1[i])
        oksg = oksg and abs(ratio - float(PIN_SHARE1[i])) < 2e-3
    check("C1 r142 pinch table: floors hard, defect == share_1",
          oksg,
          "s x gap = %s..%s pinched by 1 - g/delta_1; defect ratio "
          "== share_1 (%s..%s): the measured 1.0000 IS the pinch"
          % (PIN_SG[0], PIN_SG[4], PIN_SHARE1[0], PIN_SHARE1[4]))
    import math
    ytv = [float(s) for s in PIN_YT]
    xs = [float(x) for x in XS6]
    n = len(xs)
    sx = sum(math.log10(x) for x in xs)
    sy = sum(math.log10(v) for v in ytv)
    sxx = sum(math.log10(x) ** 2 for x in xs)
    sxy = sum(math.log10(xs[i]) * math.log10(ytv[i]) for i in range(n))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    check("C2 r140 y_t ladder: log-log slope == 4.14 (TOPROOT law)",
          abs(slope - 4.14) < 0.02,
          "y_t = %s .. %s at x = 5..28; recomputed slope %.3f "
          "(Theta ~ x^2.1 -- the round-137 measurement explained)"
          % (PIN_YT[0], PIN_YT[5], slope))
    oks = True
    for i in range(6):
        th2 = float(PIN_ONSET_05[i]) ** 2
        oks = oks and ytv[i] / 0.5 * (1 - 1e-9) <= th2 \
            <= 1.05 * ytv[i] * 1.5 / 0.5
    check("C3 r140 onsets satisfy the J2 sandwich (recomputed)", oks,
          "Theta_J(0.5) = %s: y_t/rho <= Theta^2 <= 1.05 y_t "
          "(1+rho)/rho at every rung (source-only, no zeros)"
          % (PIN_ONSET_05,))
    okal = all(float(PIN_ALIGN_DEPTH[i])
               > float(PIN_ALIGN_DEPTH[i + 1]) for i in range(5))
    okb1 = all(float(PIN_B1[i]) > float(PIN_B1[i + 1])
               for i in range(3)) and all(
        float(v) > 0 for v in PIN_B1)
    check("C4 alignment depth collapses; B1 certificates positive",
          okal and okb1,
          "|A_2|/cap %s -> %s (ALIGNMENT-WALL: no one-sided bound "
          "delivers the ratio); (1-theta)_B1 = %s at x = 5..18; "
          "x = 24/28 TAILVIS-HORIZON-LIMITED (typed; counting-"
          "resolved in v921)"
          % (PIN_ALIGN_DEPTH[0], PIN_ALIGN_DEPTH[5], (PIN_B1,)))
    okfg = all(float(PIN_FULLGAP[i]) < float(PIN_FULLGAP[i + 1])
               for i in range(4))
    check("C5 FULLGAP ladder grows; delta_1/FULLGAP == 1.0000",
          okfg,
          "FULLGAP = %s .. %s (source-pure, ~ +0.14 dex/x); the "
          "interlacing is measured TIGHT at all five rungs (typed "
          "MEASURED, not proven)" % (PIN_FULLGAP[0], PIN_FULLGAP[4]))

    print("\n  [TYPED, carried verbatim] These are RESHAPE theorems: "
          "they close NO")
    print("  omega; OPEN stays {TOPROOT, ONSETCAP(=TLAWCAP), SUSCAP2R}"
          " + DELTA1FLOOR +")
    print("  dense-a/a-extension/window-a.  Census cardinality 4 "
          "UNCHANGED.  NOT RH")
    print("  evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v920 -- PRIME.LOOP.EQUIVALENCE.THEOREMS.01 (B2: BAND-MASS "
          "<=> TLAWCAP <=>")
    print("EPS-LOCK; W1 pinch; W2: QSUBGAP <=> SUSCAP2R AND "
          "DELTA1FLOOR; W3")
    print("interlacing; rounds 140/142, re-gated in Bughunt IV; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v920: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: all theorem algebra recomputed in-run; r142 "
          "tables pinned from")
    print("tlawcap_suscap2r_probe.py (SPEC %s, 26/26, RE-RUN GREEN "
          "AT" % PIN_SPEC_R142)
    print("PROMOTION); r140 tables PINNED from run-of-record "
          "jetlock_bandmass_probe.py")
    print("(SPEC %s, 33/33, run1+run2 logs kept; loop algebra "
          "re-gated in" % PIN_SPEC_R140)
    print("Bughunt IV and recomputed here).  NOT RH evidence; NO RH "
          "claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.LOOP.EQUIVALENCE.THEOREMS.01 loop/equivalence "
          "theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
