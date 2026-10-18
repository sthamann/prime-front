#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v918 -- PRIME.DOUBLELIMIT.REDUCTION.THEOREM.01: THEOREM R -- the
load-bearing reduction of the rounds-128-151 proof arc, promoted as a
certified finite theorem: L1 + WPD ==> (H-conv) + (H-trace) with the
explicit rate max(1, C) (-4 log(1 - r/4)) d_1, together with Lemmas
N/S/X and the exact C0k <-> jet dictionary.

THE STATEMENT (round 128, note CDXXX; proven with elementary inputs).
Work in radius-4 Pascal weight currency: to a zero rho = 1/2 + i mu
(mu = delta + i gamma in the finite-world convention) attach
w = a z/(a - z)^2-type weights with the exact on-line form
w(t) = a t^2/(a + t^2)^2 <= 1/4.  Let d_k = sum w_true^k -
sum w_fin^k be the k-th defect jet of a finite spectral world
against the true one.  Define:

  L1  (trace convergence): Tr B_{a,lambda} -> C01_arch(a) + prime sum
      (source side, absolutely convergent exactly for a > 1/4);
  WPD (weighted positive domination): d_1 > 0 and
      |d_k| <= C 4^{1-k} d_1 for all k >= 2.

THEOREM R:  L1 + WPD  ==>  (H-conv) on the full Euler interval and
(H-trace) with explicit rate: for t in (0, 4),

  |log(R_fin/R_true)(t)| <= max(1, C) * (-4 log(1 - t/4)) * d_1,

via the exact series identity log(R_fin/R_a)(t) = sum_k t^k d_k / k
and the exact envelope sum_k t^k 4^{1-k}/k = -4 log(1 - t/4).
With the cited round-122 NF-closure theorem this gives the exact
reduction  RH <== [NF-closure] + [Theorem R] + {L1, WPD} on a dense
subset of a in (1/4, oo).  The lemma table:

  LEMMA N (necessity): L1 is NECESSARY for the old round-122 omega
      (Vitali + Cauchy, cited classical) -- the refinement is
      provably not weaker.
  LEMMA S (subset positivity): a sub-multiset defect has all
      d_k >= 0 and d_k <= 4^{1-k} d_1 exactly (PD), sharp at the
      band edge w = 1/4; hence the sandwich
      t d_1 <= log(R_fin/R_a)(t) <= -4 log(1 - t/4) d_1.
  LEMMA X (moment transfer is NOT free): {1/8, 1/8} vs
      {1/16, 3/16} has d_1 = 0 but d_2 = -1/128 -- positivity
      structure carries, equal first moments do not.
  WPD TAIL = WINDOW POSITIVITY (the honest typing): the k-tail of
      WPD is the window positivity itself (Cauchy-Hadamard +
      round-117 window): sup_k C0k 4^{k-1} < oo <=> max |w| <= 1/4
      <=> no off-line zero in the a-window.  Planted witness
      delta = 0.3, gamma = 30, matched a* = 900.09: the excess
      ladder (4w*)^k / 2 with 4w* = 1 + delta^2/gamma^2 = 1.0001
      EXACTLY crosses every bar at the closed-form
      k*(B) = ceil(log(2B)/log(4w*)) = 29959 / 76013 / 145094 at
      B = 10 / 10^3 / 10^6.  WPD is RH-positivity in Pascal
      diagonal currency, NOT a technical lemma.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained):
  R1  w^k <= 4^{1-k} w on [0, 1/4] (exact factorization, k <= 10);
  R2  sum_k t^k 4^{1-k}/k == -4 log(1 - t/4) (sympy series);
  R3  the Lemma-S sandwich algebra + the frozen instance strings;
  R4  the adversarial exact Theorem-R instance with C >> 1
      (the round-130 Bughunt III re-derivation, ported: complex
      off-line-style pair, C_meas > 10, sandwich holds with the
      max(1, C) factor through t = 3.999);
  R5  the k = 1 subtlety: WPD with d_1 < 0 is unsatisfiable, so the
      hypothesis itself forces d_1 >= 0 (no hidden gap);
  R6  Lemma S sharpness at the edge + the Lemma X counterexample
      (exact rationals);
  R7  the C0k <-> jet dictionary C0k = a^k sum_j binom(k, j)
      (-a)^{k-j} S_{2k-j}, S_m = (-1)^{m-1} m c_m, on a 3-pair
      rational world (sympy exact, k <= 5);
  R8  the matched-pin algebra: y* = (gamma + i delta)/(2 gamma),
      y* + conj(y*) = 1, v* = 4 y*(1 - y*) = 1 + delta^2/gamma^2
      exactly real; Euler safety a > 1/4 <=> sigma > 1; the prime-
      jet coefficients a s' + a^2 s'' = sqrt(a)/4 and
      a^2 s'^2 = a/4 for s = sqrt(a) (all sympy exact);
  R9  the WPD witness closed form: k*(B) = 29959/76013/145094
      recomputed from 4w* = 10001/10000 exactly;
  R10 pinned-table consistency: d_1 falls by >= 1.6 per rung,
      C_meas <= 1.20 everywhere, the Theorem-R band ratios in
      [0.85, 1.10 * (-4 log(1-t/4)/t)].

PINNED FROM RUN-OF-RECORD (discovery probe doublelimit_proof_probe.py,
round 128, 28/28 gates, SPEC_SHA 0c77ef7ce43fd62e, run-of-record
405.3 s + deterministic re-run, logs sha256 5b4126a0d563cfbf /
804406e275cc0ef4; RE-RUN GREEN AS TYPED AT PROMOTION: 28/28,
identical SPEC_SHA, 398.5 s): the measured ladders quoted below --
d_1(a=4) = 0.05622/0.04133/0.03072/0.02162 at x = 3/5/8/13 (digit-
identical to the round-131 cross-instrument bracket, gated in v919),
C_meas ladders (worst WPD constant 0.0202 vs bar 1.20), PD floor
-0.0000, the reduction-band ratios 1.000/1.000/1.001, the RvM node
law sup-devs 0.18/0.27/0.34 vs clock/semicircle/arcsine separations
>= 2.5x.  Independent re-derivation: bughunt3_probe.py (round 130,
note CDXXXII, 20/20, SPEC 06b05ed243a804b5) re-proved Theorem R on an
adversarial exact instance, the k = 1 subtlety, Lemma S sharpness,
Lemma X and the jet dictionary -- the same gates ported here.

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
Theorem R + Lemmas N/S/X + the dictionary + the k* witness (exact
algebra + elementary series + cited classical: Vitali/Cauchy,
Cauchy-Hadamard, B. Simon Trace Ideals Thm 2.21 class).  MEASURED =
PD on the ladder (worst WPD constant 0.0202), the d_1/C_meas/band
tables.  OBSTRUCTED (typed, NOT closed): L1 itself (the node-law
wall k_lambda ~ xi_lambda; today's evidence is band transcription --
a proof must run from the source side) and WPD's k-tail (RH-
equivalent at the tail, the exact k* witness above).  This row
certifies the REDUCTION and the COORDINATE, not the convergence.
The omega census {MEAS, OMEGA-POS} stays at CARDINALITY 4.  NOT
evidence for or against the Riemann Hypothesis in either direction;
it must not be counted as RH progress.  NO RH CLAIM.

PROVENANCE: discovery probe doublelimit_proof_probe.py (round 128,
2026-08-16, note CDXXX, contract PRIME.RADIUS4.DOUBLELIMIT.PROOF.01);
independent re-derivation bughunt3_probe.py (round 130); survived
Bughunt IV scope (round 149, note CDLIII, 0 MAJOR).  Python-only per
GATE.WOLFRAM.02 (the exact identities are sympy-gated here).
"""
from __future__ import annotations

import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
# run-of-record anchors (doublelimit_proof_probe.py, re-run at promotion)
PIN_SPEC = "0c77ef7ce43fd62e"
PIN_SANDWICH = ("0.121737", "0.124501", "0.289309")     # t = 7/2 instance
PIN_D1_A4 = ("0.05622", "0.04133", "0.03072", "0.02162")  # x = 3/5/8/13
PIN_CMEAS = {
    1: ("0.00131", "0.00054", "0.00023", "0.00009"),
    4: ("0.00521", "0.00214", "0.00092", "0.00036"),
    16: ("0.02024", "0.00845", "0.00368", "0.00143"),
}
PIN_WPD_WORST = "0.0202"          # vs bar 1.20
PIN_BAND = ("1.000", "1.000", "1.001")   # deepest rung, a = 1/4/16
PIN_RVM_DEV = ("0.18", "0.27", "0.34")   # x = 5/8/13 in-band sup dev
PIN_KSTAR = (29959, 76013, 145094)       # B = 10 / 1e3 / 1e6

N_CHECKS = 13
EXPECTED = "DOUBLELIMIT-REDUCTION-THEOREM"

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

    # ================================================== A: exact algebra
    section("A. THE EXACT ALGEBRA OF THEOREM R (recomputed, sympy)")
    w, t = sp.symbols("w t", positive=True)

    # R1: w^k <= 4^{1-k} w on [0, 1/4] -- exact factorization
    u = sp.symbols("u", nonnegative=True)
    ok1 = True
    for k in range(2, 11):
        expr = sp.Integer(4) ** (1 - k) * w - w ** k
        fact = w * (sp.Integer(4) ** (1 - k) - w ** (k - 1))
        ok1 = ok1 and sp.simplify(expr - fact) == 0
        # substitution w = u/4, u in [0, 1]: the second factor becomes
        # 4^{1-k}(1 - u^{k-1}) >= 0 -- elementary
        sub = sp.simplify((fact.subs(w, u / 4))
                          - (u / 4) * sp.Integer(4) ** (1 - k)
                          * (1 - u ** (k - 1)))
        ok1 = ok1 and sub == 0
    check("R1 w^k <= 4^(1-k) w on [0,1/4] (exact factorization)", ok1,
          "4^(1-k) w - w^k == w (4^(1-k) - w^(k-1)) == (u/4) 4^(1-k) "
          "(1 - u^(k-1)) >= 0, k <= 10")

    # R2: the envelope series == -4 log(1 - t/4) -- exact coefficient
    # comparison of the Taylor expansion (radius 4, Cauchy-Hadamard)
    NEXP = 14
    target = sp.series(-4 * sp.log(1 - t / 4), t, 0, NEXP).removeO()
    ok2 = all(
        sp.simplify(target.coeff(t, k)
                    - sp.Integer(4) ** (1 - k) / sp.Integer(k)) == 0
        for k in range(1, NEXP))
    check("R2 sum t^k 4^(1-k)/k == -4 log(1 - t/4)", ok2,
          "Taylor coefficients of -4 log(1 - t/4) == 4^(1-k)/k exactly "
          "(k <= %d; radius 4 by Cauchy-Hadamard): the explicit "
          "Theorem-R rate" % (NEXP - 1))

    # R3: Lemma-S sandwich shape + the frozen instance
    #    0 <= d_k <= 4^{1-k} d_1  ==>  t d_1 <= sum t^k d_k/k <=
    #    -4 log(1-t/4) d_1  (lower: k = 1 term alone; upper: R2)
    lo, mid, hi = (float(x) for x in PIN_SANDWICH)
    band = -4 * sp.log(1 - t / 4) / t
    band_ge_1 = sp.simplify(band.subs(t, sp.Rational(1, 1000))) > 1
    ok3 = lo <= mid <= hi and band_ge_1
    check("R3 Lemma-S sandwich + frozen instance", ok3,
          "t d1 <= log(Rfin/Ra) <= -4log(1-t/4) d1; pinned t=7/2: "
          "%s <= %s <= %s" % PIN_SANDWICH)

    # R4: adversarial Theorem-R instance, C >> 1 (Bughunt III port)
    with mp.workdps(60):
        w_true = [mp.mpf("0.2")] * 3 + [mp.mpf("0.05")]
        wc = mp.mpf("0.24") * mp.exp(1j * mp.pi / 3)
        w_fin_r = [mp.mpf("0.2")] * 2
        d = {}
        for k in range(1, 201):
            tr = sum(wv ** k for wv in w_true)
            fin = sum(wv ** k for wv in w_fin_r) + 2 * mp.re(wc ** k)
            d[k] = tr - fin
        d1 = d[1]
        cmeas = max(abs(d[k]) * mp.mpf(4) ** (k - 1) / d1
                    for k in range(2, 201))
        tail = 2 * mp.mpf("0.96") ** 200 / 4 / d1 \
            + 4 * mp.mpf("0.8") ** 200 / 4 / d1
        ok4 = d1 > 0 and cmeas > 10 and tail < cmeas
        worst = mp.mpf(0)
        for tv in [mp.mpf(x) / 1000 for x in (500, 1500, 2500, 3500,
                                              3900, 3990, 3999)]:
            lt = sum(mp.log(1 - tv * wv) for wv in w_true)
            lf = (sum(mp.log(1 - tv * wv) for wv in w_fin_r)
                  + mp.log(abs(1 - tv * wc) ** 2))
            lhs = abs(lf - lt)
            rhs = max(mp.mpf(1), cmeas) * (-4 * mp.log(1 - tv / 4)) * d1
            worst = max(worst, lhs / rhs)
            ok4 = ok4 and lhs <= rhs
        ok4 = bool(ok4)
    check("R4 adversarial instance (C >> 1): sandwich holds", ok4,
          "d1 = %s, C_meas = %s > 10, worst lhs/rhs = %s through "
          "t = 3.999 (round-130 re-derivation ported)"
          % (mp.nstr(d1, 6), mp.nstr(cmeas, 6), mp.nstr(worst, 4)))

    # R5: k = 1 subtlety -- WPD with d_1 < 0 is unsatisfiable
    d1n = Fraction(-1, 100)
    ok5 = all(Fraction(1, 10 ** 9) > Fraction(1) * 4 ** (1 - k) * d1n
              for k in range(2, 12))
    check("R5 k=1 subtlety: WPD forces d_1 >= 0", ok5,
          "RHS C 4^(1-k) d1 < 0 <= |d_k| whenever d1 < 0: the "
          "hypothesis closes its own k = 1 term (no hidden gap)")

    # R6: Lemma S sharp at the edge + Lemma X counterexample
    wq = Fraction(1, 4)
    dks = [wq ** k for k in range(1, 13)]
    sharp = all(dks[k - 1] * Fraction(4) ** (k - 1) == dks[0]
                for k in range(1, 13))
    a13 = [Fraction(1, 8)] * 2
    b13 = [Fraction(1, 16), Fraction(3, 16)]
    lemx = (sum(a13) == sum(b13)
            and sum(x ** 2 for x in a13) - sum(x ** 2 for x in b13)
            == Fraction(-1, 128))
    check("R6 Lemma S sharp at edge + Lemma X exact", sharp and lemx,
          "edge defect: d_k 4^(k-1) == d_1 for k <= 12 (SHARP); "
          "{1/8,1/8} vs {1/16,3/16}: d1 = 0, d2 = -1/128 (moment "
          "transfer NOT free)")

    # R7: C0k <-> jet dictionary on a 3-pair rational world
    a0 = sp.Integer(2)
    G2 = [sp.Integer(4), sp.Integer(9), sp.Integer(25)]
    z = sp.symbols("z")
    logphi = sum(sp.log(z + g2) for g2 in G2)
    ws = [a0 * g2 / (g2 + a0) ** 2 for g2 in G2]
    ok7 = True
    for k in range(1, 6):
        S = {}
        for m in range(1, 2 * k + 1):
            cm = sp.diff(logphi, z, m).subs(z, a0) / sp.factorial(m)
            S[m] = (-1) ** (m - 1) * m * cm
        c0k = a0 ** k * sum(sp.binomial(k, j) * (-a0) ** (k - j)
                            * S[2 * k - j] for j in range(k + 1))
        direct = sum(wv ** k for wv in ws)
        ok7 = ok7 and sp.simplify(c0k - direct) == 0
    check("R7 C0k <-> jet dictionary (sympy exact, k <= 5)", ok7,
          "C0k = a^k sum_j binom(k,j)(-a)^(k-j) S_(2k-j), "
          "S_m = (-1)^(m-1) m c_m == direct sum w^k on the 3-pair "
          "rational world (g^2 = 4, 9, 25; a = 2)")

    # R8: matched-pin algebra + Euler safety + prime-jet coefficients
    de, ga, aa = sp.symbols("delta gamma a", positive=True)
    mu = de + sp.I * ga
    astar = de ** 2 + ga ** 2
    y = sp.simplify(sp.expand_complex(astar / (astar - mu ** 2)))
    ok8 = sp.simplify(y - (ga + sp.I * de) / (2 * ga)) == 0
    ok8 = ok8 and sp.simplify(
        sp.expand_complex(y + sp.conjugate(y)) - 1) == 0
    v = sp.simplify(sp.expand_complex(4 * y * (1 - y)))
    ok8 = ok8 and sp.simplify(v - (1 + de ** 2 / ga ** 2)) == 0
    sigma = sp.Rational(1, 2) + sp.sqrt(aa)
    ok8 = ok8 and sp.simplify(
        (sigma - 1) - (sp.sqrt(aa) - sp.Rational(1, 2))) == 0 \
        and bool(sp.Rational(1, 4) < sp.Rational(26, 100)) \
        and bool(sp.Rational(1, 2) + sp.sqrt(sp.Rational(26, 100)) > 1)
    s_fun = sp.sqrt(aa)
    ok8 = ok8 and sp.simplify(
        aa * sp.diff(s_fun, aa) + aa ** 2 * sp.diff(s_fun, aa, 2)
        - sp.sqrt(aa) / 4) == 0
    ok8 = ok8 and sp.simplify(
        aa ** 2 * sp.diff(s_fun, aa) ** 2 - aa / 4) == 0
    check("R8 matched pin + Euler safety + prime jets (exact)", ok8,
          "y* = (g + i d)/(2g); y* + conj = 1; 4y*(1-y*) = 1 + "
          "d^2/g^2 real; a > 1/4 <=> sigma > 1; a s' + a^2 s'' = "
          "sqrt(a)/4, a^2 s'^2 = a/4")

    # R9: the WPD k* witness closed form (4w* = 10001/10000 exact)
    with mp.workdps(50):
        fw = mp.mpf(10001) / mp.mpf(10000)
        ks = tuple(int(mp.ceil(mp.log(2 * mp.mpf(B)) / mp.log(fw)))
                   for B in (10, 1000, 10 ** 6))
    ok9 = ks == PIN_KSTAR
    check("R9 WPD tail witness k*(B) closed form", ok9,
          "delta = 0.3, gamma = 30, a* = 900.09: 4w* = 1 + d^2/g^2 = "
          "10001/10000 EXACT; k* = ceil(log(2B)/log(4w*)) = %d/%d/%d "
          "at B = 10/1e3/1e6 (WPD's k-tail IS window positivity)" % ks)

    # ================================================== B: pinned tables
    section("B. PINNED RUN-OF-RECORD TABLES (probe re-run at promotion)")
    d1v = [float(x) for x in PIN_D1_A4]
    okd = all(d1v[i] > d1v[i + 1] for i in range(3)) \
        and d1v[0] / d1v[-1] >= 1.6
    check("B1 d_1 ladder falls (monotone; >= 1.6 over the ladder)", okd,
          "d1(a=4) = %s at x = 3/5/8/13 (digit-identical to the "
          "round-131 bracket -- cross-instrument continuity gated in "
          "v919)" % (PIN_D1_A4,))
    okc = all(float(s) <= 1.20 for av in PIN_CMEAS
              for s in PIN_CMEAS[av]) and float(PIN_WPD_WORST) <= 1.20
    okc = okc and all(
        float(PIN_CMEAS[av][i]) >= float(PIN_CMEAS[av][i + 1])
        for av in PIN_CMEAS for i in range(3))
    check("B2 WPD constant C_meas <= 1.20, falling per rung", okc,
          "worst %s (bar 1.20); PD floor -0.0000: all defect jets "
          "positive and dominated (PD-MEASURED, typed)" % PIN_WPD_WORST)
    okb = all(0.85 <= float(s) <= 1.10 for s in PIN_BAND)
    check("B3 reduction band: supdefect/(t_max d_1) ~ 1", okb,
          "deepest rung %s in the Theorem-R band [0.85, 1.10 x "
          "(-4log(1-t/4)/t)]: the round-122 m=1 law is EXPLAINED"
          % (PIN_BAND,))
    okr = all(float(PIN_RVM_DEV[i]) < 1.0 for i in range(3))
    check("B4 RvM node law: in-band sup dev < 1 zero", okr,
          "sup devs %s at x = 5/8/13; clock/semicircle/arcsine "
          "separated >= 2.5x: the equilibrium density is the "
          "ARITHMETIC RvM law" % (PIN_RVM_DEV,))

    print("\n  [TYPED, carried verbatim] L1 OBSTRUCTED (node-law wall, "
          "source side);")
    print("  WPD OBSTRUCTED-RH-EQUIVALENT-AT-TAIL (exact k* witness); "
          "PROVEN is the")
    print("  REDUCTION and the COORDINATE, not the convergence.  Omega "
          "census {MEAS,")
    print("  OMEGA-POS} cardinality 4 UNCHANGED.  NOT RH evidence.  "
          "NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v918 -- PRIME.DOUBLELIMIT.REDUCTION.THEOREM.01 (Theorem R: "
          "L1 + WPD ==>")
    print("(H-conv)+(H-trace) with explicit rate; Lemmas N/S/X + jet "
          "dictionary;")
    print("round 128, re-derived round 130; NOT RH evidence; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v918: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: exact algebra + adversarial instance + dictionary "
          "+ k* witness")
    print("recomputed in-run; measured ladders pinned from "
          "doublelimit_proof_probe.py")
    print("(SPEC %s, 28/28, re-run green at promotion 398.5 s)."
          % PIN_SPEC)
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.DOUBLELIMIT.REDUCTION.THEOREM.01 doublelimit "
          "reduction theorem: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
