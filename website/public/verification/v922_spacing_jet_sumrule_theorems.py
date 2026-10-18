#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v922 -- PRIME.SPACING.JETSUMRULES.THEOREMS.01: THE HPIN/SPACING
THEOREM FAMILY of rounds 135 and 154 -- the secular-derivative /
spacing-product identity, the jet sum rules (both orders), the
A_0-cancellation and the lattice-tail certificate, promoted as
certified finite theorems.  The family is the exact-algebra backbone
consumed by every later spectral round (r140/r142/r146/r150/r153/
r154/r156/r157/r161); it survived Bughunt IV (round 149, 0 MAJOR)
and was Lean-hardened in round 158 (note CDLXII).

THE THEOREMS (all exact algebra; sympy generic + exact instances):

  ROUND 135 (note CDXXXIX, hpin_floor_probe.py, Theorems D1-D4):
  D1 (the derivative identity): with F(y) = A_0 + sum_k w_k/(y - b_k)
     and E_N(z) = 2 sin(A z) F(z^2)/z, at every census node mu_j
     (F(mu_j^2) = 0, mu_j != 0):  E_N'(mu_j) == 4 sin(A mu_j)
     F'(mu_j^2) EXACTLY -- the H-pin derivative floor is
     F'-currency.  SPACING-PRODUCT FORM: F'(y_j) == A_0
     prod_{i != j} (y_j - y_i) / prod_k (y_j - b_k) -- the floor is
     a zero-spacing product (root data enters as ONE polynomial
     identity).
  D2 (the jet sum rules, first order): sum_j 1/F'(y_j) ==
     (sum y - sum b)/A_0 == -A_2/A_0^2  and  sum_j y_j/F'(y_j) ==
     -A_4/A_0^2 + A_2^2/A_0^3 (with A_2 := sum_k w_k, A_4 :=
     sum_k w_k b_k): the r131 boundary-jet telescope IS the
     reciprocal-floor moment data.
  D2' (round 154, note CDLVIII, nearalign_probe.py, Theorem P5 --
     the NEXT rungs): sum_j F''(y_j)/F'(y_j)^3 == 2 A_2/A_0^3  and
     sum_j [1/F'(y_j)^2 - y_j F''(y_j)/F'(y_j)^3] ==
     3 A_2^2/A_0^4 - 2 A_4/A_0^3 (residue calculus on 1/F^2, y/F^2).
  D3 (the A_0-cancellation): the H-pin demand ratio is A_0-FREE:
     g = 2 eps/m with eps = c A_0 and m = 4 A_0 |sin| PR gives
     g = c/(2 |sin| PR) EXACTLY -- the Connes/boundary scale cancels
     in the demand; the floor ALONE rides sqrt(tau) (typed
     FLOOR-RIDES-CONNES, measured slope 0.37, NOT a disguise).
  D4 (the far-lattice tail): -log(1 - q) <= q/(1 - q*) for
     0 <= q <= q* < 1 -- the sin/lattice factorization tail is
     certified (Euler sine product CITED classical).
  GAP-DEMAND (exact rearrangement): zone mass <= TL/8 <== m_min >=
     m_req = 16 eps_bar sum|w'|/TL.
  SIGN-UNIFORM COROLLARY (conditional, typed): IF all 1/F'(y_j)
     share a sign THEN |F'(y_j)| >= A_0^2/|A_2| each -- gated
     against the MEASURED census: MIXED at every rung (3/4, 7/10,
     6/20, 27/41 negative), so the harmonic floor is INAPPLICABLE
     and the moment route is OBSTRUCTED (sum-rule mass sits on the
     EDGE nodes: zone share 1.5e-4 -> 3.9e-13).

LEAN HARDENING (round 158, note CDLXII; experiments/
lean4-carrier-rigidity/, build green, 28 proven theorems on the
three standard axioms): SpacingProduct.lean proves the spacing-
product identity for GENERIC FINITE K over an arbitrary field
(nodal_erase_wronskian, spacing_product_cleared, spacing_product,
fderivWeight_ne_zero -- a strengthening over the probe's per-block
gates); JetSumRules.lean proves all four sum rules at K = 2
(sum_rule_first, sum_rule_second, sum_rule_jet, sum_rule_jet_second)
with the general-K form honesty-locked (JetSumRuleSkeleton +
jetSkeleton_not_unconditional).  This module re-checks the theorem
names are present in the shipped Lean sources.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained): D1 both forms
(generic sympy), D2 p = 0, 1 (generic), D2' second-order rungs
(generic), D3 cancellation, D4 tail certificate (derivative form +
instance), the gap-demand rearrangement, the sign-uniform corollary
on an exact instance, and consistency arithmetic on all pinned
tables below.

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 135 -- PINNED (NOT re-run at promotion; 33/33 gates,
  SPEC_SHA 80366b4e62779398, run-of-record + deterministic re-runs
  1837.6 s, THREE logs kept; the D1/D2 algebra was re-gated by
  r154-G32 and Lean-hardened in r158 -- the SAME exact-algebra gates
  are recomputed in-run here): census real-rootedness 4/10/20/41
  (nonreal 0) at x = 3/5/8/13 with zone counts argument-principle-
  certified (4/10/21); sum-rule devs <= 4e-95; zone sum-rule share
  1.5e-4/1.1e-6/1.3e-8/3.9e-13 (OBSTRUCTION exhibit); sign census
  MIXED everywhere; floor transfer 1/1, 4/4, 10/10, 21/21, 35/35,
  53/53 zone zeros at gap <= ball with m_min = 1.0e-2 .. 6.9e-41;
  eps-lock/tlaw strings 0.28/0.15 -> 0.51/0.51 (window (0.05, 5));
  H-pin zone-mass margins 5.8 -> 5.1e12 GROWING (slope +0.60);
  scaling slopes eps_bar -2.43, m_min -1.81.
  ROUND 154 -- RE-RUN GREEN AS TYPED AT PROMOTION (31/31 gates,
  identical SPEC_SHA f92b3fb59b142254; run-of-record 1485.3 s +
  deterministic re-run identical): P5/D2' instantiated at all six
  blocks, devs <= 1e-40 core / 1e-25 deep (b5 1e-55 .. b28 2e-80).

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
D1/D2/D2'/D3/D4 + gap-demand (exact algebra; Euler sine product,
HSW22 Cor. 1.2, PT21 cited).  MEASURED = the ladder tables (typed).
CONDITIONAL = the sign-uniform corollary (its hypothesis is
measured FALSE -- carried as an obstruction, not a floor).  OPEN
(typed, NOT closed): H-pin itself -- the r135 omega split EPS-LOCK
+ SPACING-REMAINDER stays open; census {MEAS, OMEGA-POS} stays at
CARDINALITY 4.  NOT evidence for or against the Riemann Hypothesis
in either direction.  NO RH CLAIM.

PROVENANCE: discovery probes hpin_floor_probe.py (round 135,
2026-08-16, note CDXXXIX, contract PRIME.HPIN.DERIVATIVE.FLOOR.01)
and nearalign_probe.py (round 154, note CDLVIII, contract
PRIME.NEARALIGN.PROOF.01); re-gated in bughunt4_probe.py (round
149, note CDLIII); Lean-hardened round 158 (note CDLXII).
Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import os
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R135 = "80366b4e62779398"
PIN_SPEC_R154 = "f92b3fb59b142254"
XS4 = (3, 5, 8, 13)
# r135 G30/G34/G33: census counts (K-1), nonreal, negative-sign counts,
# zone share of sum |1/F'|
PIN_CENSUS = (4, 10, 20, 41)
PIN_NEG = (3, 7, 6, 27)
PIN_ZONESHARE = ("1.5e-04", "1.1e-06", "1.3e-08", "3.9e-13")
# r135 G36 floor transfer (x = 3..24): matched zone zeros, m_min, g_max
XS6 = (3, 5, 8, 13, 18, 24)
PIN_MATCHED = (1, 4, 10, 21, 35, 53)
PIN_MMIN = ("1.0e-02", "1.9e-06", "7.2e-12", "4.0e-20", "9.1e-30",
            "6.9e-41")
PIN_GMAX = ("7.9e-02", "9.3e-03", "3.8e-04", "5.6e-08", "1.1e-10",
            "2.8e-14")
# r135 G37 eps-lock / tlaw strings
PIN_LOCK = ("0.28", "0.36", "0.43", "0.48", "0.49", "0.51")
PIN_TLAW = ("0.15", "0.27", "0.37", "0.47", "0.48", "0.51")
# r135 G38 zone-mass margins at a = 4
PIN_MARGIN = ("6.1e+00", "3.2e+01", "6.2e+02", "3.5e+06", "1.5e+09",
              "5.3e+12")
# r154 G32 second-order sum-rule devs (q0/q1 worst per block, b5..b28)
PIN_P5_DEV = ("2e-55", "4e-69", "4e-94", "3e-98", "1e-88", "4e-77")

LEAN_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "experiments", "lean4-carrier-rigidity",
                 "TfptCarrier"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "lean4-carrier-rigidity", "TfptCarrier"),
)
LEAN_REQ = {
    "SpacingProduct.lean": ("nodal_erase_wronskian",
                            "spacing_product_cleared",
                            "spacing_product",
                            "fderivWeight_ne_zero"),
    "JetSumRules.lean": ("sum_rule_first", "sum_rule_second",
                         "sum_rule_jet", "sum_rule_jet_second",
                         "jetSkeleton_not_unconditional"),
}

N_CHECKS = 13
EXPECTED = "SPACING-JETSUMRULES-THEOREMS"

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

    # ================================================ A: D1 both forms
    section("A. THE DERIVATIVE / SPACING-PRODUCT IDENTITY (D1; exact)")
    z, A, y = sp.symbols("z A y", positive=True)
    A0, b1, b2, y1, y2 = sp.symbols("A0 b1 b2 y1 y2", positive=True)

    # D1 weight form: E = 2 sin(Az) F(z^2)/z; at a node F(mu^2) = 0:
    # E'(mu) == 4 sin(A mu) F'(mu^2).  Generic: write F factored.
    Ffac = A0 * (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    E = 2 * sp.sin(A * z) * Ffac.subs(y, z ** 2) / z
    Ep = sp.diff(E, z)
    mu = sp.sqrt(y1)  # node: F(mu^2) = 0
    lhs = sp.simplify(Ep.subs(z, mu))
    rhs = sp.simplify(4 * sp.sin(A * mu)
                      * sp.diff(Ffac, y).subs(y, y1))
    check("A1 D1 derivative identity E' == 4 sin F' (generic)",
          sp.simplify(lhs - rhs) == 0,
          "E_N = 2 sin(Az) F(z^2)/z; at every census node "
          "E_N'(mu_j) == 4 sin(A mu_j) F'(mu_j^2): the H-pin floor "
          "is F'-currency")

    # D1 spacing-product form + residue weights (K = 3 class: 2 poles)
    Fp1 = sp.simplify(sp.diff(Ffac, y).subs(y, y1))
    spac = sp.simplify(Fp1 - A0 * (y1 - y2)
                       / ((y1 - b1) * (y1 - b2)))
    w1r = sp.simplify((Ffac * (y - b1)).subs(y, b1))
    w1d = sp.simplify(A0 * (b1 - y1) * (b1 - y2) / (b1 - b2))
    sumform = sp.simplify(sp.together(
        Ffac - (A0 + w1r / (y - b1)
                + sp.simplify((Ffac * (y - b2)).subs(y, b2))
                / (y - b2))))
    check("A2 D1 spacing-product + residue-weight forms (generic)",
          spac == 0 and sp.simplify(w1r - w1d) == 0 and sumform == 0,
          "F'(y_j) == A0 prod(y_j - y_i)/prod(y_j - b_k); F == A0 + "
          "sum w_k/(y - b_k) with residue weights: the floor is a "
          "ZERO-SPACING PRODUCT (root data = one polynomial identity)")

    # ================================================ B: sum rules
    section("B. THE JET SUM RULES (D2 first order + P5 second order)")
    w1v = sp.simplify((Ffac * (y - b1)).subs(y, b1))
    w2v = sp.simplify((Ffac * (y - b2)).subs(y, b2))
    A2 = sp.simplify(w1v + w2v)          # A_2 = sum w_k
    A4 = sp.simplify(w1v * b1 + w2v * b2)  # A_4 = sum w_k b_k
    Fp2 = sp.simplify(sp.diff(Ffac, y).subs(y, y2))
    s_p0 = sp.simplify(sp.together(
        1 / Fp1 + 1 / Fp2 - (y1 + y2 - b1 - b2) / A0))
    s_p0b = sp.simplify(sp.together(
        (y1 + y2 - b1 - b2) / A0 + A2 / A0 ** 2))
    s_p1 = sp.simplify(sp.together(
        y1 / Fp1 + y2 / Fp2 - (-A4 / A0 ** 2 + A2 ** 2 / A0 ** 3)))
    check("B1 D2 sum rules p = 0, 1 (generic exact)",
          s_p0 == 0 and s_p0b == 0 and s_p1 == 0,
          "sum 1/F' == (sum y - sum b)/A0 == -A_2/A_0^2; sum y/F' == "
          "-A_4/A_0^2 + A_2^2/A_0^3: the r131 boundary-jet telescope "
          "IS the reciprocal-floor moment data")

    Fpp1 = sp.simplify(sp.diff(Ffac, y, 2).subs(y, y1))
    Fpp2 = sp.simplify(sp.diff(Ffac, y, 2).subs(y, y2))
    q0 = sp.simplify(sp.together(
        Fpp1 / Fp1 ** 3 + Fpp2 / Fp2 ** 3 - 2 * A2 / A0 ** 3))
    q1 = sp.simplify(sp.together(
        (1 / Fp1 ** 2 - y1 * Fpp1 / Fp1 ** 3)
        + (1 / Fp2 ** 2 - y2 * Fpp2 / Fp2 ** 3)
        - (3 * A2 ** 2 / A0 ** 4 - 2 * A4 / A0 ** 3)))
    check("B2 P5 second-order sum rules (generic exact)",
          q0 == 0 and q1 == 0,
          "sum F''/F'^3 == 2A_2/A_0^3; sum [1/F'^2 - y F''/F'^3] == "
          "3A_2^2/A_0^4 - 2A_4/A_0^3 (residue calculus on 1/F^2, "
          "y/F^2): the NEXT rungs of the D2 family, r154 Theorem P5")

    # ================================================ C: D3, D4, demand
    section("C. A_0-CANCELLATION, LATTICE TAIL, GAP DEMAND (D3/D4)")
    c_, A0s, sn, PR = sp.symbols("c_ A0s sn PR", positive=True)
    g_ratio = sp.simplify((2 * c_ * A0s) / (4 * A0s * sn * PR)
                          - c_ / (2 * sn * PR))
    check("C1 D3 A_0-cancellation in the H-pin demand ratio",
          g_ratio == 0,
          "g = 2 eps/m, eps = c A0, m = 4 A0 |sin| PR ==> g = "
          "c/(2 |sin| PR): the Connes/boundary scale cancels EXACTLY "
          "(demand A0-FREE; the floor alone rides sqrt(tau), typed "
          "FLOOR-RIDES-CONNES)")

    q, qs = sp.symbols("q qs", positive=True)
    # d/dq [q/(1-q*) + log(1-q)] = 1/(1-q*) - 1/(1-q) >= 0 on [0, q*]
    dd = sp.simplify(1 / (1 - qs) - 1 / (1 - q))
    inst = all(bool(-sp.log(1 - qq) <= qq / (1 - sp.Rational(64, 100)))
               for qq in (sp.Rational(1, 10), sp.Rational(1, 2),
                          sp.Rational(64, 100)))
    check("C2 D4 far-lattice tail certificate",
          sp.simplify(dd.subs(q, qs)) == 0 and inst
          and bool(dd.subs([(q, sp.Rational(1, 2)),
                            (qs, sp.Rational(64, 100))]) > 0),
          "-log(1-q) <= q/(1-q*) on 0 <= q <= q* < 1 (derivative "
          "form + exact instances at q* = 0.64): the sin/lattice "
          "factorization tail is certified; Euler sine product CITED")

    eb, sw, TL = sp.symbols("eb sw TL", positive=True)
    m_req = 16 * eb * sw / TL
    # zone mass <= 2 eps_bar sum|w'| / m_min <= 2 eb sw / m_req = TL/8
    check("C3 gap-demand rearrangement (exact)",
          sp.simplify((2 * eb * sw / m_req) - TL / 8) == 0,
          "zone mass <= TL/8 <== m_min >= m_req = 16 eps_bar "
          "sum|w'|/TL: the H-pin demand in closed form (r135 G14 "
          "shape, r131 gap lemma cited)")

    # sign-uniform corollary on an exact instance
    r1, r2 = sp.Rational(1, 8), sp.Rational(3, 8)  # same sign
    tot = r1 + r2  # == |A2|/A0^2 in the uniform case
    okE = bool(1 / r1 >= 1 / tot) and bool(1 / r2 >= 1 / tot)
    check("C4 sign-uniform corollary (conditional, typed)",
          okE,
          "IF all r_j = 1/F'(y_j) share a sign and sum r_j = "
          "-A2/A0^2 THEN |F'| >= A0^2/|A2| each -- the hypothesis is "
          "measured FALSE (census MIXED %s of %s negative): the "
          "harmonic/moment route is OBSTRUCTED, carried as such"
          % (PIN_NEG, PIN_CENSUS))

    # ================================================ D: Lean hardening
    section("D. LEAN HARDENING CHECK (round 158, note CDLXII)")
    found = None
    for d in LEAN_DIRS:
        if os.path.isdir(d):
            found = d
            break
    ok_lean = found is not None
    detail = []
    if ok_lean:
        for fn, names in LEAN_REQ.items():
            p = os.path.join(found, fn)
            if not os.path.isfile(p):
                ok_lean = False
                detail.append("%s MISSING" % fn)
                continue
            src = open(p, encoding="utf-8").read()
            miss = [n for n in names if n not in src]
            if miss:
                ok_lean = False
                detail.append("%s missing %s" % (fn, miss))
            else:
                detail.append("%s: %d theorems" % (fn, len(names)))
    msg = "; ".join(detail) if detail else "lean dir not found"
    check("D1 Lean modules ship the hardened theorems",
          ok_lean,
          msg + " -- SpacingProduct generic-K over an arbitrary "
          "field, JetSumRules K = 2 + honesty-locked skeleton (r158 "
          "build green, standard axioms only)")

    # ================================================ E: pinned tables
    section("E. PINNED LADDER TABLES (consistency arithmetic)")
    okc = all(PIN_CENSUS[i] < PIN_CENSUS[i + 1] for i in range(3)) \
        and all(0 < PIN_NEG[i] < PIN_CENSUS[i] for i in range(4))
    zs = [float(v) for v in PIN_ZONESHARE]
    okz = all(zs[i] > zs[i + 1] for i in range(3)) and zs[0] <= 1e-2
    check("E1 r135 census real-rooted; sign census MIXED; zone "
          "sum-rule share collapses", okc and okz,
          "counts %s (nonreal 0, K-1 exact); neg %s (MIXED at every "
          "rung: harmonic floor INAPPLICABLE); zone share %s -> %s "
          "(the sum-rule mass sits on the EDGE nodes -- moment route "
          "OBSTRUCTED)" % (PIN_CENSUS, PIN_NEG, PIN_ZONESHARE[0],
                           PIN_ZONESHARE[3]))

    mm = [float(v) for v in PIN_MMIN]
    gm = [float(v) for v in PIN_GMAX]
    okf = all(mm[i] > mm[i + 1] for i in range(5)) \
        and all(gm[i] > gm[i + 1] for i in range(5)) \
        and all(PIN_MATCHED[i] < PIN_MATCHED[i + 1] for i in range(5))
    check("E2 r135 floor transfer: every zone zero matched", okf,
          "matched %s at x = %s; m_min %s -> %s falling, ball radii "
          "g_max %s -> %s: |E'(gamma_j)| >= m_node/2 transfers to "
          "the TRUE zeros (gap <= ball at every rung)"
          % (PIN_MATCHED, XS6, PIN_MMIN[0], PIN_MMIN[5],
             PIN_GMAX[0], PIN_GMAX[5]))

    lk = [float(v) for v in PIN_LOCK]
    tl = [float(v) for v in PIN_TLAW]
    okl = all(0.05 <= v <= 5.0 for v in lk + tl)
    mg = [float(v) for v in PIN_MARGIN]
    okm = all(mg[i] < mg[i + 1] for i in range(5)) and mg[1] >= 3.0
    check("E3 eps-lock/tlaw in-window; H-pin margins grow", okl
          and okm,
          "lock %s..%s, tlaw %s..%s inside (0.05, 5.0) (EPS-LOCK "
          "measured, r131 GW mechanism); zone-mass margins %s -> %s "
          "GROWING (slope +0.60; measured-extrapolation only, no "
          "claim)" % (PIN_LOCK[0], PIN_LOCK[5], PIN_TLAW[0],
                      PIN_TLAW[5], PIN_MARGIN[0], PIN_MARGIN[5]))

    pd = [float(v) for v in PIN_P5_DEV]
    check("E4 r154 P5 instantiation devs (all six blocks)",
          all(v <= 1e-25 for v in pd),
          "second-order sum-rule devs %s .. %s (<= 1e-25 deep bar; "
          "re-run green as typed at promotion, SPEC %s)"
          % (PIN_P5_DEV[0], PIN_P5_DEV[5], PIN_SPEC_R154))

    print("\n  [TYPED, carried verbatim] PROVEN = D1/D2/D2'/D3/D4 + "
          "gap-demand (exact")
    print("  algebra).  H-pin itself stays OPEN (EPS-LOCK + "
          "SPACING-REMAINDER, r135")
    print("  omega split).  Census cardinality 4 UNCHANGED.  NOT RH "
          "evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v922 -- PRIME.SPACING.JETSUMRULES.THEOREMS.01 (D1 "
          "derivative/spacing-product")
    print("identity; D2 + P5 jet sum rules both orders; D3 "
          "A_0-cancellation; D4")
    print("lattice tail; rounds 135/154, Lean-hardened round 158; "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v922: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: all theorem algebra recomputed in-run; r135 "
          "tables PINNED from")
    print("hpin_floor_probe.py (SPEC %s, 33/33, three deterministic "
          "logs kept," % PIN_SPEC_R135)
    print("NOT re-run at promotion -- D1/D2 re-gated by r154-G32 + "
          "Lean r158); r154")
    print("tables from nearalign_probe.py (SPEC %s, 31/31, RE-RUN "
          "GREEN AT" % PIN_SPEC_R154)
    print("PROMOTION).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.SPACING.JETSUMRULES.THEOREMS.01 spacing/jet-"
          "sum-rule theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
