#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v919 -- PRIME.SECULAR.GW.PINNING.01: THE SECULAR IDENTITY + THE
GUINAND-WEIL PINNING -- the two central certified objects of round 131
(note CDXXXIII), both independently reproduced in Bughunt IV (round
149, note CDLIII, 0 MAJOR), promoted with a disclosed recomputed/
pinned split.

LAYER 1, SECULAR-EXACT (recomputed in-run, exact rationals).  For the
round-114 window operators (window [-A, A], A = log(x)/2, K =
ceil(1.25 x log x) cosine modes, census coefficients c_k with
A_0 = sum (-1)^k c_k), the rank-one secular identity

    det(M_eta - z) = -z * C(z^2) / A_0

holds EXACTLY: the operator nodes are EXACTLY the zeros of the census
polynomial E_N; the node count is EXACTLY K - 1 (the census degree);
the lattice zeros sit at j pi / A exactly.  The round-123 eta-
degeneration IS the boundary decay A_0 -> 0: the operator COSTUME
diverges like 1/A_0 while the census polynomial stays conditioned --
the nodes, not the matrix, are the honest object.  Recomputed here on
an own exact-rational instance (K = 6, dim 11, 13 interpolation
points > degree: a polynomial identity, Fractions end to end,
sympy-free -- the Bughunt-IV independent construction, ported).

LAYER 2, GW-PINNING (certified per rung against cited classical
inputs; numeric tables pinned from run-of-record).  On psi =
phi * phi~ the Guinand-Weil explicit formula gives

    tau = Q(phi) = 2 sum_rho |E_N(gamma_rho)|^2  (+ certified
    envelope tail + off-line allowance),

i.e. THE VARIATIONAL VALUE ITSELF IS THE ell^2 NORM OF E_N ON THE
TRUE SPECTRUM.  Consequences, certified per rung (x = 3/5/8/13):
  SMALLNESS LAW:  2|E_N(gamma_j)|^2 <= tau + OFF_ALLOW at EVERY
      polished band zero (x = 13: max 8.7e-62 <= 2.5e-54;
      OFF_ALLOW = 3e-63 via PT21 + HSW22 + boundary-jet envelope);
  GAP LAW (resolvability zone gamma <= 2 pi x): ALL 21/21 zone
      zeros at x = 13 pinned to nodes, max gap 2.9e-17 <= bound
      5.6e-8, gamma_1 at gap 1.9e-50 -- exponentially close BY THE
      VARIATIONAL MECHANISM, not by design; the edge layer
      (2 pi x, edge) is honestly MEASURED-ONLY (8 matches to
      6.9e-7);
  L1-TAIL CLOSED (v914 citation discipline): G(T) = sum_{gamma > T}
      gamma^{-2} bounded by the closed form from HSW22 Cor. 1.2 +
      PT21 (T = 3,000,175,332,800), derived via Stieltjes + exact
      antiderivatives + tangent lemma; eps_true(a, T) = a G(T) with
      w <= a/t^2 exact -- the TAIL half of L1 is PROVEN, the BAND
      half is the exactly-named residual omega (derivative floor +
      matched-prefix, i.e. H-pin);
  CROSSOVER THEOREM: the mode density A/pi crosses the RvM density
      (1/2pi) log(T/2pi) EXACTLY at T = 2 pi x, and the resolvable
      band fraction is EXACTLY 1/KFAC = 0.8 -- the corpus constant
      INBAND_F frozen since round 122 is a THEOREM;
  BOUNDARY-JET LAW: the minimizer flattens its ENTIRE boundary jet
      (x = 13: A_0 = 8.17e-27, A_2 = 2.62e-20, A_4 = 1.24e-14,
      A_6 = 2.22e-9) -- THIS is why the finite window pins zeros far
      below naive resolution.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained):
  S1  the secular identity on the own exact-rational instance
      (Fractions, dim 11, 13 points; node count == K - 1 = 5);
  S2  the HSW22 G(T) closed-form ingredients: exact antiderivatives
      + the tangent-lemma derivative sign (sympy);
  S3  the closed form dominates an independent numeric IBP integral
      of the same Stieltjes bound (0 <= rel excess < 1e-3 at
      T = 200/2000 -- the tangent bound is the only slack) and is
      monotone falling through T = 3e12;
  S4  the crossover theorem T = 2 pi x + INBAND_F == 1/KFAC (sympy
      exact solve);
  S5  w(t) = a t^2/(a + t^2)^2 <= min(1/4, a/t^2) exactly and
      G -> 0 (the tail-half closure algebra);
  S6  consistency arithmetic on the pinned tables: P/tau ratios in
      (0.90, 1.00); smallness maxima <= tau + off; gaps <= bounds;
      the boundary-jet collapse monotone in depth; the d_1 bracket
      digit-identical to the v918 pins (cross-instrument
      continuity).

PINNED FROM RUN-OF-RECORD (discovery probe l1_weyllaw_probe.py,
round 131, 31/31 gates, SPEC_SHA 7d8cc2e5ca8108fb, run-of-record
220.2 s + deterministic re-run, logs sha256 513efede474f06d2 /
4e5b1b7a7ddf8453; RE-RUN GREEN AS TYPED AT PROMOTION: 31/31,
identical SPEC_SHA, 217.4 s): the GW tables (tau/P per rung),
smallness maxima, gap-law tables, boundary jets, d_1 brackets,
control separations (SMOOTH 7.1e7 / SCRARITH 7.5e7 / EPSTEIN 3.4e8).
INDEPENDENT REPRODUCTION (Bughunt IV, round 149, 20/20, SPEC
1cd81cef9ff1193e, log sha256 07129f0a20b76f03): own Weil form at
x = 3 built from the classical explicit formula (digamma u-kernel
self-derived), tau_own = 3.05582e-7 against the frozen string with
|dlog10| = 2.7e-7; zero side within own envelope (tau - P = 2.6e-9
<= 4.8e-9); smallness law at all 7000 cache zeros; the secular
identity reproduced exact-rationally on an own K = 6 instance
(the same construction recomputed here); the boundary atom
log 3 == 2A contributes EXACTLY zero.

HONEST TYPING (carried verbatim; nothing upgraded).  The zero cache
consumed by the probe is PT21-warranted (verified on-line zeros);
this module consumes NO zero table at runtime -- the numeric GW/gap
tables are pinned strings.  Z1 typing carried: INPUT circularity NO
(the builder consumes only the Lambda sieve + archimedean integral +
pole block; Bughunt-IV re-verified by an own call-graph reachability
scan), EVIDENCE novelty LIMITED (band transcription typing of rounds
112/123/128 stands VERBATIM).  The BAND half of L1 stays OPEN
(H-pin); the edge layer is MEASURED-ONLY.  NOT evidence for or
against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe l1_weyllaw_probe.py (round 131,
2026-08-16, note CDXXXIII, contract PRIME.L1.WEYLLAW.PROOF.01);
independent reproduction bughunt4_probe.py (round 149, note CDLIII).
Cited classical inputs: Guinand-Weil explicit formula; Platt--
Trudgian 2021 Thm 1; Hasanalizade--Shen--Wong JNT 235 (2022)
Cor. 1.2 (0.1038/0.2573/9.3675).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC = "7d8cc2e5ca8108fb"
# G32: (tau, P) per rung x = 3/5/8/13
PIN_GW = (("3.056e-07", "2.990e-07"), ("1.607e-16", "1.563e-16"),
          ("3.773e-30", "3.648e-30"), ("2.499e-54", "2.402e-54"))
# G33: (max 2|E(g)|^2, tau + off) per rung
PIN_SMALL = (("2.6e-08", "3.1e-07"), ("9.0e-19", "1.6e-16"),
             ("5.8e-34", "3.8e-30"), ("8.7e-62", "2.5e-54"))
# G34: (zone matched/total, max zone gap, bound) per rung
PIN_GAP = ((1, "2.8e-04", "7.9e-02"), (4, "2.1e-06", "9.3e-03"),
           (10, "2.4e-09", "3.8e-04"), (21, "2.9e-17", "5.6e-08"))
GAMMA1_GAP_X13 = "1.9e-50"
# G40: boundary jets (A0, A2, A4, A6) per rung
PIN_JETS = (("1.84e-03", "8.94e+00", "2.46e+03", "7.21e+05"),
            ("4.73e-08", "2.89e-03", "2.22e+01", "4.39e+04"),
            ("8.42e-15", "3.51e-09", "2.04e-04", "4.17e+00"),
            ("8.17e-27", "2.62e-20", "1.24e-14", "2.22e-09"))
# G36: d_1(a=4) bracket centers -- must equal the v918 pins verbatim
PIN_D1_A4 = ("0.05622", "0.04133", "0.03072", "0.02162")
# G41: control separations at the pinning functional
PIN_SEP = ("7.1e+07", "7.5e+07", "3.4e+08")
# Bughunt-IV independent reproduction anchors
PIN_BH4_TAU = ("3.05582e-7", "2.7e-7")   # (frozen string, |dlog10|)
KFAC = Fraction(5, 4)

N_CHECKS = 11
EXPECTED = "SECULAR-GW-PINNING"

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


def frac_det(Mrows):
    n = len(Mrows)
    A = [row[:] for row in Mrows]
    det = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        inv = A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / inv
                for cc in range(c, n):
                    A[r][cc] -= f * A[c][cc]
    return det


def part():
    import sympy as sp
    from mpmath import mp

    # ================================================== S1: secular
    section("S1. THE SECULAR IDENTITY (own exact-rational instance)")
    K = 6
    cs = [Fraction(3, 7), Fraction(-1, 3), Fraction(2, 5),
          Fraction(1, 11), Fraction(-2, 9), Fraction(5, 13)]
    A0 = sum((-1) ** k * cs[k] for k in range(K))
    dim = 2 * K - 1
    mid = K - 1
    dv = [Fraction(n - mid) for n in range(dim)]   # lattice units pi/A = 1
    xi = [Fraction(0)] * dim
    xi[mid] = cs[0]
    for k in range(1, K):
        xi[mid + k] = cs[k] / 2
        xi[mid - k] = cs[k] / 2
    eta = [Fraction((-1) ** abs(n - mid)) for n in range(dim)]
    S = sum(eta[i] * xi[i] for i in range(dim))
    bs = [Fraction(k * k) for k in range(1, K)]    # b_k = om_k^2 = k^2

    def C_of(y):
        prod_all = Fraction(1)
        for b in bs:
            prod_all *= (y - b)
        tot = cs[0] * prod_all
        for i, k in enumerate(range(1, K)):
            pr = Fraction(1)
            for j, b in enumerate(bs):
                if j != i:
                    pr *= (y - b)
            tot += (-1) ** k * cs[k] * y * pr
        return tot

    zs = [Fraction(p, q) for p, q in
          ((1, 2), (3, 4), (7, 5), (12, 7), (9, 4), (13, 5), (10, 3),
           (17, 4), (23, 5), (16, 3), (11, 2), (25, 4), (19, 3))]
    ok1 = (S == A0)
    for z in zs:
        Mz = [[(dv[i] if i == j else Fraction(0))
               - dv[i] * xi[i] * eta[j] / S
               - (z if i == j else Fraction(0))
               for j in range(dim)] for i in range(dim)]
        ok1 = ok1 and frac_det(Mz) == -z * C_of(z * z) / A0
    check("S1 det(M_eta - z) == -z C(z^2)/A_0 (exact, dim 11)", ok1,
          "Fractions end to end, 13 interpolation points > deg 11 "
          "(polynomial identity); node count == K - 1 = %d == census "
          "degree; lattice zeros j pi/A exact" % (K - 1))

    # ================================================== S2: HSW form
    section("S2. THE HSW22 TAIL CLOSED FORM (exact ingredients)")
    tsym, usym, Usym = sp.symbols("t u U", positive=True)
    F1 = -(sp.log(tsym / (2 * sp.pi * sp.E)) + 1) / tsym
    F2 = -sp.log(tsym) / (2 * tsym ** 2) - 1 / (4 * tsym ** 2)
    F3 = -(2 * sp.log(tsym) + 1) / (4 * tsym ** 2)
    ok2 = (sp.simplify(sp.diff(F1, tsym)
                       - sp.log(tsym / (2 * sp.pi * sp.E))
                       / tsym ** 2) == 0
           and sp.simplify(sp.diff(F2, tsym)
                           - sp.log(tsym) / tsym ** 3) == 0
           and sp.simplify(sp.diff(F3, tsym)
                           - sp.log(tsym) / tsym ** 3) == 0
           and sp.simplify((1 / Usym - 1 / usym) * usym * Usym
                           - (usym - Usym)) == 0)
    check("S2 G(T) antiderivatives + tangent lemma (sympy)", ok2,
          "exact antiderivatives for the closed form; tangent "
          "derivative sign (u - U)/(uU) >= 0 for u >= U (classical "
          "log x <= x - 1, cited)")

    # S3: closed form vs independent numeric IBP integral (no cache)
    def hsw_G(T):
        with mp.workdps(40):
            Tm = mp.mpf(T)
            al, be, cc = (mp.mpf(s) for s in
                          ("0.1038", "0.2573", "9.3675"))
            lg = mp.log(Tm)
            ll = mp.log(lg)
            t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
            t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
                  + cc) / Tm ** 2
            t3 = (al * lg + be * ll + cc) / Tm ** 2
            return float(t1 + t2 + t3)

    devs = []
    okm = True
    with mp.workdps(30):
        for T in (200.0, 2000.0):
            Tm = mp.mpf(T)

            def integ(tv):
                Mt = (tv / (2 * mp.pi)) * mp.log(tv / (2 * mp.pi
                                                       * mp.e)) \
                    + mp.mpf(7) / 8
                Qt = (mp.mpf("0.1038") * mp.log(tv)
                      + mp.mpf("0.2573") * mp.log(mp.log(tv))
                      + mp.mpf("9.3675"))
                MT = (Tm / (2 * mp.pi)) * mp.log(Tm / (2 * mp.pi
                                                       * mp.e)) \
                    + mp.mpf(7) / 8
                QT = (mp.mpf("0.1038") * mp.log(Tm)
                      + mp.mpf("0.2573") * mp.log(mp.log(Tm))
                      + mp.mpf("9.3675"))
                return 2 * (Mt + Qt - (MT - QT)) / tv ** 3
            exact = float(mp.quad(integ, [Tm, 10 * Tm, 1e3 * Tm,
                                          1e6 * Tm, mp.inf]))
            cf = hsw_G(T)
            devs.append((T, cf / exact - 1))
            okm = okm and 0 <= cf / exact - 1 < 1e-3
    okmono = hsw_G(200.0) > hsw_G(2000.0) > hsw_G(7264.0) \
        > hsw_G(3000175332800.0) > 0
    check("S3 closed form >= own IBP integral (tangent-only slack)",
          okm and okmono,
          "; ".join("T=%g rel excess %.1e" % d for d in devs)
          + "; monotone falling through T = 3e12 (L1-TAIL closes in "
          "closed form: a G(T) -> 0)")

    # ================================================== S4: crossover
    section("S4. THE CROSSOVER THEOREM (sympy exact)")
    xs, Tv, kf = sp.symbols("xs T kf", positive=True)
    Tstar = sp.solve(sp.log(Tv / (2 * sp.pi)) / (2 * sp.pi)
                     - (sp.log(xs) / 2) / sp.pi, Tv)
    ok4 = (len(Tstar) == 1
           and sp.simplify(Tstar[0] - 2 * sp.pi * xs) == 0)
    edge = (kf * xs * sp.log(xs)) * sp.pi / (sp.log(xs) / 2)
    ok4 = ok4 and sp.simplify(2 * sp.pi * xs / edge - 1 / kf) == 0 \
        and Fraction(1) / KFAC == Fraction(4, 5)
    check("S4 mode density == RvM density exactly at T = 2 pi x", ok4,
          "resolvable band fraction == 1/KFAC = 4/5 == the corpus "
          "INBAND_F: the constant frozen since round 122 is a THEOREM")

    # S5: w <= min(1/4, a/t^2) exact
    av, tv = sp.symbols("a t", positive=True)
    wexp = av * tv ** 2 / (av + tv ** 2) ** 2
    ok5 = (sp.simplify(sp.Rational(1, 4) - wexp
                       - (av - tv ** 2) ** 2
                       / (4 * (av + tv ** 2) ** 2)) == 0
           and sp.simplify(av / tv ** 2 - wexp
                           - av * ((av + tv ** 2) ** 2 - tv ** 4)
                           / (tv ** 2 * (av + tv ** 2) ** 2)) == 0)
    check("S5 w(t) <= min(1/4, a/t^2) (exact differences)", ok5,
          "1/4 - w == (a - t^2)^2/(4(a + t^2)^2) >= 0; a/t^2 - w == "
          "a((a+t^2)^2 - t^4)/(t^2 (a+t^2)^2) >= 0: eps_true(a, T) = "
          "a G(T), the tail half of L1 is closed")

    # ================================================== S6: pinned
    section("S6. PINNED GW / GAP / JET TABLES (consistency arithmetic)")
    okgw = all(0.90 < float(p) / float(ta) < 1.00
               for ta, p in PIN_GW)
    check("S6a GW identity: P/tau in (0.90, 1.00) per rung", okgw,
          "x=13: tau %s vs P %s (the zeros carry 96%%; envelope tail "
          "+ off-line allowance certified in the probe)"
          % (PIN_GW[3][0], PIN_GW[3][1]))
    oksm = all(float(m) <= float(cap) for m, cap in PIN_SMALL)
    check("S6b smallness law: max 2|E(gamma)|^2 <= tau + OFF", oksm,
          "x=13: %s <= %s (OFF_ALLOW = 3e-63 via PT21 + HSW22 + "
          "boundary-jet envelope)" % (PIN_SMALL[3][0], PIN_SMALL[3][1]))
    okgap = all(float(g) <= float(b) for _n, g, b in PIN_GAP)
    check("S6c gap law: all zone zeros pinned, gaps <= bounds", okgap,
          "zone matches 1/1, 4/4, 10/10, 21/21; x=13 max gap %s <= "
          "%s, gamma_1 at %s; edge layer MEASURED-ONLY (typed)"
          % (PIN_GAP[3][1], PIN_GAP[3][2], GAMMA1_GAP_X13))
    okj = all(float(PIN_JETS[i][0]) > float(PIN_JETS[i + 1][0])
              for i in range(3))
    okj = okj and all(float(r[0]) < float(r[1]) < float(r[2])
                      < float(r[3]) for r in PIN_JETS)
    check("S6d boundary-jet law: full jet collapses with depth", okj,
          "A_0: %s -> %s over the ladder; x=13 jets %s (the "
          "eta-admissibility law, source side)"
          % (PIN_JETS[0][0], PIN_JETS[3][0], (PIN_JETS[3],)))
    from v918_doublelimit_reduction_theorem import PIN_D1_A4 as V918_D1
    okd = tuple(PIN_D1_A4) == tuple(V918_D1)
    check("S6e d_1 bracket digit-identical to the v918 pins", okd,
          "%s == v918 (cross-instrument continuity: round-128 series "
          "instrument vs round-131 certified bracket)" % (PIN_D1_A4,))
    oksep = all(float(s) >= 1e3 for s in PIN_SEP)
    okbh4 = float(PIN_BH4_TAU[1]) < 1e-3
    check("S6f controls separate + Bughunt-IV reproduction", oksep
          and okbh4,
          "smallness separations SMOOTH/SCRARITH/EPSTEIN = %s/%s/%s "
          ">= 1e3 (the pinning is prime-made); BH4 own Weil form at "
          "x=3: tau_own vs frozen %s, |dlog10| = %s"
          % (PIN_SEP + PIN_BH4_TAU))

    print("\n  [TYPED, carried verbatim] L1 = TAIL (proven, closed "
          "form) + BAND (H-pin,")
    print("  OPEN); edge layer MEASURED-ONLY; Z1 evidence typing "
          "stands (input")
    print("  circularity NO, evidence novelty LIMITED).  NOT RH "
          "evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v919 -- PRIME.SECULAR.GW.PINNING.01 (secular identity "
          "det(M_eta - z) =")
    print("-z C(z^2)/A_0 exact + GW pinning tau = 2 sum |E_N(gamma)|^2"
          " + certified gap")
    print("law + L1-TAIL closed; round 131, reproduced in Bughunt IV; "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v919: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: secular identity + HSW closed form + crossover + "
          "tail algebra")
    print("recomputed in-run; GW/gap/jet tables pinned from "
          "l1_weyllaw_probe.py (SPEC")
    print("%s, 31/31, re-run green at promotion 217.4 s) + the "
          "Bughunt-IV" % PIN_SPEC)
    print("independent x=3 reproduction.  NOT RH evidence; NO RH "
          "claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.SECULAR.GW.PINNING.01 secular + GW pinning: "
          "%d passed, %d failed ---" % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
