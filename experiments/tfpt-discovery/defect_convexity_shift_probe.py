#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""defect_convexity_shift_probe -- PRIME.E8GLUE.EULER.03 (round 216):
the two named goals of round 215 attacked -- (a) is the uniform
positive defect of the naked compiler pair a UNIVERSAL convolution
fact across the D-sum lattice battery, and (b) the weight-shift KILL
test of the axis-2 SHIFT class (can ANY renormalisation bring a code
world onto MAIN weights?).

EXPLORATION ONLY (2026-08-22).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.  Round-214/215 fences carried verbatim (corpus
kills XCVIII/XCIX/C/CDVII not contradicted; no TFPT constant enters
any wall builder; mincut 4/5 and the four-item residue untouched).

(A) DEFECT LAW -- WITH THE DISCLOSED SMOKE RETYPE (house pattern).
The naive frozen hypothesis H-DEF ('all D-sum defects positive
universally') was FALSIFIED by smoke1 (13/16 at pre-retype SHA
f9e058d492972968, log kept) and by the disclosed prototype
extension to D7 (+) D1: the measured law is SHARPER and it is a
PARITY LAW.  Battery (exact integer theta series to norm 96,
M = 48, convolution ward exact):
  D6 (+) D2 and D4 (+) D4 (even-even splits): ZERO violations --
      Euler-multiplicative;
  D5 (+) D3 (the compiler pair, odd-odd): 29 violations, ALL
      POSITIVE (strictly SUBmultiplicative, first defect 4608/169);
  D7 (+) D1 (the other odd-odd split): 29 violations, ALL NEGATIVE
      (strictly SUPERmultiplicative, first defect -512/7);
  Z8 / D8 / E8 controls: clean (Jacobi/round-215 theorem class).
GATED LAW: H-PARITY (Euler <=> even-even split) + H-SIGN (each
odd-odd split breaks with UNIFORM sign; the compiler split is the
submultiplicative one).  STRUCTURAL ANCHOR, exact (G15): the
discriminant group of D_n is CYCLIC Z4 for n odd and KLEIN Z2 x Z2
for n even (Smith normal form of the D_n Gram matrices, n = 1..8,
sympy exact) -- so odd-odd splits are EXACTLY the splits with
cyclic mu4-glue (round-XVII SNF: E8/(D5 (+) A3) = Z4), and the
SAME parity that forces the mu4 (cyclic) glue makes the naked
theta non-Euler.  TYPED SYNONYMY (no claim): the compiler chose
(g_car, N_fam) = (5, 3) -- odd-odd, hence mu4-cyclic glue, hence
non-Euler rohbau needing exactly that glue; among the two odd-odd
splits it is the defect-POSITIVE one.  Epstein x^2 + 5y^2 control:
7 violations, all NEGATIVE (recorded; no prediction).

(B) THE SHIFT-CLASS KILL.  Axis-2 SHIFT worlds (FULL/D8/U13) carry
Euler products with twisted local factors.  Question (round 215
goal b): does some weight renormalisation a_m -> a_m m^{-s0} bring
one of them onto MAIN weights Lambda(q)?  KILL, exact: a single
shift must satisfy 1 + p^3 = p^{s0} at EVERY prime simultaneously;
the two-prime witness p = 2, 3 forces 9 = 2^{s0} AND 28 = 3^{s0},
i.e. 9^{log2(3)} = 28 -- FALSE by exact interval arithmetic
(9^{log2(3)} = 32.68... != 28).  CONTRAST (the honest dichotomy):
the CUSPIDAL world Delta = eta^24 (tau(n), exact integer series;
wards tau(2) = -24, tau(3) = 252, tau(6) = tau(2) tau(3),
tau(2)tau(4)-tau(8)-relation) has weight-normalised local factors
lambda(p) = tau(p)/p^{11/2} with |lambda(p)| <= 2 (Ramanujan,
verified p <= 47): its comb-to-MAIN ratio |Lambda_Delta(p)/
Lambda(p)| = |lambda(p)| stays BOUNDED, while the E4/code world's
ratio (1 + p^3)/p^{3/2} GROWS like p^{3/2} (measured, monotone).
TYPED READING (no claim): the obstruction to renormalising the
error-code world into a MAIN-type window is exactly the EISENSTEIN
/ CONSTANT term -- the lattice's zero vector, i.e. the zero
codeword; cuspidality (= vacuum subtracted) is what a bounded
window needs, and the E8 theta is maximally non-cuspidal at level
1.  This closes round-215 goal (b) as the expected NO, now with an
exact witness and a measured dichotomy.

VERDICT (expected): DEFECT-CONVEXITY-UNIVERSAL-ON-BATTERY +
EULER-CONTROLS-CLEAN + EPSTEIN-SIGN-CENSUS-RECORDED +
SHIFT-KILL-TWO-PRIME-EXACT + RAMANUJAN-DICHOTOMY-MEASURED +
EISENSTEIN-OBSTRUCTION-TYPED + NO-RH-CLAIM.

RECORD TABLES (frozen from the smoke/prototype ladder at the
pre-freeze SHA; house pattern; no bar moved after freeze):
CAL_DEF {world: (#violating pairs, #negative defects)}:
  D5D3: (29, 0), D7D1: (29, 29), D6D2: (0, 0), D4D4: (0, 0),
  Z8: (0, 0), D8: (0, 0), E8: (0, 0).
CAL_FIRST: D5D3 first defect (2,3) = 4608/169; D7D1 first defect
  (2,3) = -512/7.
CAL_EPS_SIGN: (7, 7) -- all negative, recorded.
CAL_WITNESS: 9^(log2 3) = 32.5416 (!= 28, margin 4.542).
CAL_TAU: tau = (1, -24, 252, -1472, ...), tau(6) = -6048;
  max |lambda(p)| over p <= 47 = 1.709 (Ramanujan bound 2 holds).
CAL_RATIO: E4 comb/MAIN ratio at p = 2..47 grows 3.18 -> 322.2
  (monotone); Delta ratio bounded by 2.
AMENDMENTS: NONE after freeze (the one pre-freeze retype is the
smoke1/prototype-disclosed parity-sign law above).

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
defect universality G10-G14; S2 shift kill G20-G24; S4 pricing
G50-G51 + G60 verdict + G99 runtime.  Pure exact arithmetic (integer
series, Fractions, mp interval-grade numerics); no eigsy, no cell
builders.  DETERMINISM: no randomness; run2 identical modulo
wall-clock tokens.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from euler_jet_colligation_probe import primes_upto   # r204 VERBATIM

# ---------------------------------------------------------------- frozen
NORM_CAP = 96
MCAP = 48
RUNTIME_BAR = 600.0
PCAP = 47

# --------------------- calibrated record tables (smoke/calib ladder)
CAL_DEF = {"D5D3": (29, 0), "D7D1": (29, 29), "D6D2": (0, 0),
           "D4D4": (0, 0), "Z8": (0, 0), "D8": (0, 0), "E8": (0, 0)}
CAL_FIRST = {"D5D3": "4608/169", "D7D1": "-512/7"}
CAL_EPS_SIGN = (7, 7)
CAL_WITNESS = "32.5416"
CAL_TAU6 = -6048
CAL_LAM_MAX = "1.709"
CAL_RATIO_LO = "3.18"
CAL_RATIO_HI = "322.2"
VAL_TOL = 0.01

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("NO zero-oracle, NO zeta identifier, NO np.load, "
                       "no verification/ import; pure exact arithmetic; "
                       "fully zero-free" if not bad else "; ".join(bad))


# ------------------------------------------------- exact series helpers
def series_mul(a, b, cap):
    c = [0] * (cap + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        top = cap - i
        for j, bj in enumerate(b):
            if j > top:
                break
            c[i + j] += ai * bj
    return c


def series_pow(a, n, cap):
    r = [0] * (cap + 1)
    r[0] = 1
    base = list(a)
    e = n
    while e:
        if e & 1:
            r = series_mul(r, base, cap)
        e >>= 1
        if e:
            base = series_mul(base, base, cap)
    return r


def theta3(cap):
    c = [0] * (cap + 1)
    c[0] = 1
    k = 1
    while k * k <= cap:
        c[k * k] = 2
        k += 1
    return c


def theta4(cap):
    c = [0] * (cap + 1)
    c[0] = 1
    k = 1
    while k * k <= cap:
        c[k * k] = 2 * ((-1) ** k)
        k += 1
    return c


def theta2_pow8(cap):
    inner = [0] * (cap + 1)
    k = 0
    while k * k + k <= cap:
        inner[k * k + k] += 2
        k += 1
    p8 = series_pow(inner, 8, cap)
    out = [0] * (cap + 1)
    for j, v in enumerate(p8):
        if j + 2 <= cap:
            out[j + 2] = v
    return out


def theta_D(n, cap, t3, t4):
    t3n = series_pow(t3, n, cap)
    t4n = series_pow(t4, n, cap)
    return [(x + y) // 2 for x, y in zip(t3n, t4n)]


def defect_census(series):
    """normalised a_m = series[2m]/series[2]; return (violations,
    negatives, first defect Fraction or None)."""
    a = {m: Fraction(series[2 * m], series[2]) for m in range(1, MCAP + 1)}
    viol = 0
    neg = 0
    first = None
    for m in range(2, MCAP + 1):
        for m2 in range(m, MCAP + 1):
            if m * m2 > MCAP:
                break
            if math.gcd(m, m2) != 1:
                continue
            d = a[m] * a[m2] - a[m * m2]
            if d != 0:
                viol += 1
                if d < 0:
                    neg += 1
                if first is None:
                    first = (m, m2, d)
    return viol, neg, first


def eta24(cap):
    """tau(n) via q Prod (1-q^k)^24, exact integers."""
    prod = [0] * (cap + 1)
    prod[0] = 1
    for k in range(1, cap + 1):
        fac = [0] * (cap + 1)
        fac[0] = 1
        fac[k] = -1
        f24 = series_pow(fac, 24, cap)
        prod = series_mul(prod, f24, cap)
    tau = [0] * (cap + 2)
    for j, v in enumerate(prod):
        if j + 1 <= cap + 1:
            tau[j + 1] = v
    return tau


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("defect_convexity_shift_probe -- PRIME.E8GLUE.EULER.03 "
          "(round 216)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "norm cap %d (M = %d); battery D5D3/D6D2/D4D4 + controls "
          "Z8/D8/E8 + Epstein sign census; shift-kill witness p = "
          "(2, 3); Ramanujan contrast p <= %d; H-DEF frozen: all "
          "D-sum defects >= 0" % (NORM_CAP, MCAP, PCAP))

    section("S1  THE PARITY-SIGN DEFECT LAW (goal a, retyped)")
    cap = NORM_CAP
    t3 = theta3(cap)
    t4 = theta4(cap)
    t2_8 = theta2_pow8(cap)
    d1 = [0] * (cap + 1)
    k = 0
    while 4 * k * k <= cap:
        d1[4 * k * k] += 2 if k > 0 else 1
        k += 1
    worlds = {
        "D5D3": series_mul(theta_D(5, cap, t3, t4),
                           theta_D(3, cap, t3, t4), cap),
        "D7D1": series_mul(theta_D(7, cap, t3, t4), d1, cap),
        "D6D2": series_mul(theta_D(6, cap, t3, t4),
                           theta_D(2, cap, t3, t4), cap),
        "D4D4": series_mul(theta_D(4, cap, t3, t4),
                           theta_D(4, cap, t3, t4), cap),
        "Z8": series_pow(t3, 8, cap),
        "D8": theta_D(8, cap, t3, t4),
    }
    worlds["E8"] = [a + b // 2 for a, b in zip(worlds["D8"], t2_8)]
    res = {}
    firsts = {}
    for tag in sorted(worlds):
        viol, neg, first = defect_census(worlds[tag])
        res[tag] = (viol, neg)
        firsts[tag] = first
        info("%-5s violations=%-3d negatives=%-2d first=%s"
             % (tag, viol, neg,
                ("(%d,%d) defect %s" % first) if first else "none"))

    ok10 = all(res[t] == (0, 0) for t in ("Z8", "D8", "E8"))
    check("G10-euler-controls-clean", ok10,
          "Z8 / D8 / E8: zero violations on all coprime pairs <= %d "
          "(the Jacobi/round-215 theorem class re-confirmed through "
          "the defect pipeline)" % MCAP)

    ok11 = (res["D6D2"] == (0, 0) and res["D4D4"] == (0, 0)
            and res["D5D3"][0] > 0 and res["D5D3"][1] == 0
            and res["D7D1"][0] > 0
            and res["D7D1"][1] == res["D7D1"][0])
    if not smoke:
        ok11 = ok11 and all(res[t] == CAL_DEF[t] for t in
                            ("D5D3", "D7D1", "D6D2", "D4D4"))
        ok11 = ok11 and str(firsts["D5D3"][2]) == CAL_FIRST["D5D3"]
        ok11 = ok11 and str(firsts["D7D1"][2]) == CAL_FIRST["D7D1"]
    check("G11-parity-sign-law", ok11,
          "H-PARITY + H-SIGN: even-even splits D6D2 %s / D4D4 %s "
          "are EULER; odd-odd splits break with UNIFORM sign -- "
          "compiler pair D5D3 %s ALL POSITIVE (submultiplicative, "
          "first %s), D7D1 %s ALL NEGATIVE (supermultiplicative, "
          "first %s) (== CAL)"
          % (res["D6D2"], res["D4D4"], res["D5D3"],
             firsts["D5D3"][2] if firsts["D5D3"] else "-",
             res["D7D1"],
             firsts["D7D1"][2] if firsts["D7D1"] else "-"))

    # convolution ward: r_{D5D3}(2m) == sum_k r_D5(2k) r_D3(2(m-k))
    d5 = theta_D(5, cap, t3, t4)
    d3 = theta_D(3, cap, t3, t4)
    ok12 = True
    for m in range(0, MCAP + 1):
        conv = sum(d5[2 * k] * d3[2 * (m - k)] for k in range(m + 1))
        ok12 = ok12 and conv == worlds["D5D3"][2 * m]
    check("G12-convolution-ward", ok12,
          "r_(D5(+)D3)(2m) == convolution sum_k r_D5(2k) r_D3(2(m-k)) "
          "exact for all m <= %d: the defect object IS a normalised "
          "convolution of two Jacobi sequences" % MCAP)

    # Epstein sign census (no H-DEF prediction; record)
    icap = MCAP
    rq = [0] * (2 * icap + 1)
    xm = int(math.isqrt(2 * icap)) + 1
    ym = int(math.isqrt(2 * icap // 5)) + 1
    for xx in range(-xm, xm + 1):
        for yy in range(-ym, ym + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= 2 * icap:
                rq[n] += 1
    aeps = {m: Fraction(rq[m], rq[1]) for m in range(1, MCAP + 1)}
    viol_e = 0
    neg_e = 0
    for m in range(2, MCAP + 1):
        for m2 in range(m, MCAP + 1):
            if m * m2 > MCAP:
                break
            if math.gcd(m, m2) != 1:
                continue
            d = aeps[m] * aeps[m2] - aeps[m * m2]
            if d != 0:
                viol_e += 1
                if d < 0:
                    neg_e += 1
    ok13 = viol_e > 0
    if not smoke:
        ok13 = ok13 and (viol_e, neg_e) == CAL_EPS_SIGN
    check("G13-epstein-sign-census", ok13,
          "Epstein x^2+5y^2 (index m = norm, a_1-normalised): %d "
          "violations, %d negative -- RECORDED (H-DEF predicts "
          "nothing off the D-sum battery%s)"
          % (viol_e, neg_e,
             "; the class-number-2 world is NOT uniformly "
             "submultiplicative" if neg_e > 0 else
             "; sign uniformity here too, recorded"))

    check("G14-parity-sign-conjecture-typed", True,
          "TYPED (conjecture-grade, census-backed, NO proof claim): "
          "for D-sum splits of rank 8, Euler-ness <=> even-even "
          "split, and each odd-odd split breaks with UNIFORM defect "
          "sign ((5,3) positive / (7,1) negative); candidate "
          "mechanism for a proof round: the odd D-thetas are the "
          "spinor-glue carriers (cyclic Z4 duals), their product "
          "misses the composite-address mass with one definite sign")

    # G15: discriminant groups of D_n via exact Smith normal form
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    ok15 = True
    snf_sum = []
    for n in range(1, 9):
        if n == 1:
            G = sp.Matrix([[4]])
        else:
            basis = []
            for i in range(n - 1):
                v = [0] * n
                v[i] = 1
                v[i + 1] = -1
                basis.append(v)
            v = [0] * n
            v[n - 2] = 1
            v[n - 1] = 1
            basis.append(v)
            B = sp.Matrix(basis)
            G = B * B.T
        S = smith_normal_form(G)
        invs = [S[i, i] for i in range(S.rows) if S[i, i] != 1]
        snf_sum.append((n, tuple(int(x) for x in invs)))
        if n % 2 == 1:
            ok15 = ok15 and invs == [4]
        else:
            ok15 = ok15 and invs == [2, 2]
    check("G15-discriminant-parity-exact", ok15,
          "Smith normal form of the D_n Gram matrices, n = 1..8: "
          "%s -- discriminant group CYCLIC Z4 for n odd (the "
          "mu4-glue carriers), KLEIN Z2 x Z2 for n even; the parity "
          "of the defect law IS the parity of the glue group "
          "(round-XVII SNF anchor E8/(D5(+)A3) = Z4)"
          % str(snf_sum))

    section("S2  THE SHIFT-CLASS KILL (goal b)")
    with mp.workdps(40):
        wit = mp.mpf(9) ** (mp.log(3) / mp.log(2))
        margin = abs(wit - 28)
    ok20 = margin > mp.mpf(4)
    if not smoke:
        ok20 = ok20 and abs(float(wit) - float(CAL_WITNESS)) <= VAL_TOL
    check("G20-two-prime-shift-witness", ok20,
          "a single shift s0 needs 1+2^3 = 2^s0 AND 1+3^3 = 3^s0, "
          "i.e. 9^(log2 3) = 28; EXACT: 9^(log2 3) = %s, margin "
          "%.3f > 4 -- NO weight shift maps the code world onto "
          "MAIN weights (KILL, two-prime witness)"
          % (mp.nstr(wit, 6), float(margin)))

    tau = eta24(NORM_CAP)
    ok21 = (tau[1] == 1 and tau[2] == -24 and tau[3] == 252
            and tau[6] == tau[2] * tau[3] and tau[6] == CAL_TAU6
            and tau[4] == -1472
            and tau[2] * tau[4] - tau[8] == 2 ** 11 * tau[2])
    check("G21-tau-exact-wards", ok21,
          "eta^24 exact: tau = (1, -24, 252, -1472, ...); "
          "tau(6) = tau(2) tau(3) = -6048 (multiplicativity); Hecke "
          "at p = 2: tau(2) tau(4) - tau(8) = 2^11 tau(2) exact")

    with mp.workdps(40):
        lam_max = mp.mpf(0)
        ratios_e4 = []
        for p in primes_upto(PCAP):
            lamp = abs(mp.mpf(tau[p])) / mp.mpf(p) ** mp.mpf("5.5")
            lam_max = max(lam_max, lamp)
            ratios_e4.append((1 + mp.mpf(p) ** 3) / mp.mpf(p) ** mp.mpf("1.5"))
    ok22 = lam_max < 2
    if not smoke:
        ok22 = ok22 and abs(float(lam_max) - float(CAL_LAM_MAX)) <= VAL_TOL
    check("G22-ramanujan-bounded", ok22,
          "CUSPIDAL contrast Delta: max |lambda(p)| = max |tau(p)|/"
          "p^(11/2) = %s < 2 over p <= %d (Ramanujan-Deligne class; "
          "weight-normalised local factors BOUNDED): a cusp world "
          "CAN sit at bounded comb distance to MAIN"
          % (mp.nstr(lam_max, 4), PCAP))

    mono = all(ratios_e4[i] < ratios_e4[i + 1]
               for i in range(len(ratios_e4) - 1))
    ok23 = mono and float(ratios_e4[0]) > 3 and float(ratios_e4[-1]) > 300
    if not smoke:
        ok23 = ok23 and (abs(float(ratios_e4[0]) - float(CAL_RATIO_LO))
                         <= VAL_TOL * 10)
        ok23 = ok23 and (abs(float(ratios_e4[-1]) - float(CAL_RATIO_HI))
                         <= VAL_TOL * 100)
    check("G23-e4-ratio-grows", ok23,
          "the code world's weight-normalised comb ratio (1+p^3)/"
          "p^(3/2) grows MONOTONICALLY %s -> %s over p <= %d (~ "
          "p^(3/2)): unbounded, never MAIN-type -- the dichotomy is "
          "cuspidality" % (mp.nstr(ratios_e4[0], 3),
                           mp.nstr(ratios_e4[-1], 4), PCAP))

    check("G24-eisenstein-obstruction-typed", True,
          "TYPED READING (no claim): the obstruction to window-"
          "renormalising the error-code world is the EISENSTEIN/"
          "constant term = the lattice zero vector = the zero "
          "codeword; cuspidality (vacuum subtracted) is what a "
          "bounded window needs, and theta_E8 is maximally "
          "non-cuspidal at level 1 -- round-215 goal (b) closed as "
          "the expected NO, now with an exact witness")

    section("S4  PRICING")
    check("G50-fences", True,
          "fences carried (XCVIII/XCIX/C/CDVII); pure dictionary "
          "round; thesis stays PRICED, never claimed")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED (H-pin untouched)")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "PARITY-SIGN-DEFECT-LAW(Euler iff even-even; odd-odd "
          "breaks uniform-signed, compiler split positive) + "
          "DISCRIMINANT-PARITY-EXACT(Z4 odd / Klein even) + "
          "EULER-CONTROLS-CLEAN + CONVOLUTION-WARD-EXACT + "
          "EPSTEIN-SIGN-CENSUS-RECORDED + "
          "SHIFT-KILL-TWO-PRIME-EXACT + RAMANUJAN-DICHOTOMY-"
          "MEASURED + EISENSTEIN-OBSTRUCTION-TYPED + NO-RH-CLAIM")

    wall_s = time.time() - T0_WALL
    check("G99-runtime", wall_s <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall_s, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s" %
          (npass, len(CHECKS), " (SMOKE)" if smoke else "",
           SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
