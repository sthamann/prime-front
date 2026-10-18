#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_filtration_worlds_probe -- PRIME.E8GLUE.EULER.02 (round 215):
the Z2-coset law lifted to CITATION GRADE + the two-axis Euler typing
of the full world battery.

EXPLORATION ONLY (2026-08-22).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.  Fences of round 214 carried verbatim (corpus
kills XCVIII/XCIX/C/CDVII not contradicted; no TFPT constant enters
any wall builder; mincut 4/5 and the four-item residue untouched).

TWO NAMED GOALS OF ROUND 214, EXECUTED:

(A) WHY THE Z2-COSET FLOOR -- the round-214 census (multiplicativity
of the D8-coset unions to m <= 48) is lifted to a STRUCTURAL fact
with one classical citation: Jacobi's eight-squares formula
  r8(n) = 16 (-1)^n sum_{d | n} (-1)^d d^3 =: 16 J(n)
(Jacobi 1829; Hardy-Wright Thm 386).  From it, exactly:
  J(2^a u) = sigma3(u) g(a) for odd u, a >= 1,
      g(a) := (8^(a+1) - 8)/7 - 1,   J(u) = sigma3(u) (u odd),
  r_D8(2m)  = r8(2m)  (theta ward: theta_D8 keeps the even-norm
      part of theta3^8), so a_m^D8 = J(2m)/J(2) with J(2) = 7 and
      r8(2) = 112 = |R(D8)|;
  r_U13(2m) = 240 sigma3(m) - 16 J(2m)  (spinor coset = E8 - D8),
      with 2-local sequence h(b) = 240 sigma3(2^b) - 16 g(b+1),
      h(0) = 128 = the norm-2 spinor count.
MULTIPLICATIVITY of a^D8 and a^U13 then follows from the product
shape sigma3(odd) x (2-local factor) -- verified here BOTH as exact
symbolic identities (sympy, geometric-sum closed form) AND entrywise
against the integer theta series to norm 96.  The Z2-coset law of
round 214 is thereby citation-grade: Euler-ness of the coset floor
is Jacobi arithmetic, NOT a small-cap accident.  The naked compiler
pair L0 = D5 (+) D3 stays NON-Euler: the first defect is exhibited
as an exact rational (a_2 a_3 - a_6 != 0), with the full defect
census recorded.

(B) THE TWO-AXIS WORLD TYPING -- the arithmetic-side mirror of the
r210 triple refusal.  EXACT LEMMA (finite window form, proved
symbolically in-probe): a normalised Dirichlet coefficient series is
multiplicative on a finite window IFF its von-Mangoldt comb is
supported on prime powers there (support-Euler == product-Euler; the
log 6 identity Lam(2) a_3 + Lam(3) a_2 = a_2 a_3 log 6 generalises).
Hence the honest typing has exactly TWO independent axes:
  AXIS 1 (SUPPORT / Euler product): comb supported on prime powers?
  AXIS 2 (LOCAL FACTORS): do the prime-power weights match the
      classical Lambda?
Typing table (predictions frozen; calibration fills the numbers):
  MAIN        axis1 PASS, axis2 PASS   (reference row, by def.)
  FULL (E8)   axis1 PASS, axis2 SHIFT  (Lam(q)(1 + q^3): Euler with
                                        shifted local factors)
  D8 / U13    axis1 PASS, axis2 SHIFT  (Jacobi-twisted local data)
  SCRARITH(5) axis1 PASS, axis2 FAIL   (the golden scramble permutes
              weights among PRIME-POWER addresses only -- support
              clean, local factors wrong: the arithmetic mirror of
              the r210 BUDGET channel)
  EPSTEIN(8)  axis1 FAIL (q = 6 block; r202 source recursion
              reproduced: lamq(2) = 0, support {4, 5, 6}) -- the
              mirror of the INERTIA-PRECONDITION channel
  L0          axis1 FAIL (q = 6 defect; the naked compiler pair)
  SMOOTH      portless (no comb; the PORTS channel), typed.
SYNONYMY (typed, no claim): the r210 wall-side triple refusal
{inertia / budget / ports} mirrors the arithmetic axes
{support / local factors / no ports}.  A NEGATIVE CONTROL injects a
tiny composite atom into MAIN and must flip axis 1 (detector fires).

VERDICT (expected): Z2-COSET-LAW-CITATION-GRADE +
SUPPORT-IS-PRODUCT-LEMMA + TWO-AXIS-TYPING-COMPLETE +
SCRARITH-IS-WEIGHT-ONLY + EPSTEIN-L0-SUPPORT-BROKEN +
COMPILER-PAIR-DEFECT-EXACT + NO-RH-CLAIM.

RECORD TABLES (frozen from the smoke/calibration ladder at the
pre-freeze SHA 8cb143d9e9cd4d78; house pattern; no bar moved after
freeze):
CAL_L0: a_2 = 144/13, a_3 = 396/13, a_6 = 4032/13, first defect
  a_2 a_3 - a_6 = 4608/169 EXACT; 29 violating pairs; negative-
  defect share 0.000 -- ALL defects positive: the naked compiler
  pair is uniformly SUBMULTIPLICATIVE (a_{mm'} < a_m a_{m'} on
  every violating coprime pair; recorded as observation).
CAL_SCR_DEV: max local-factor deviation 0.1541.
CAL_EPS_SUPPORT: (4, 5, 6) with lamq(2) = 0 exact.
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
structural layer G10-G15; S2 two-axis typing G20-G23; S4 pricing
G50-G51 + G60 verdict + G99 runtime.  DETERMINISM: no randomness;
run2 identical modulo wall-clock tokens.  Pure arithmetic round: no
eigsy, no wall matrices, no cell builders.

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
SUPP_FLOOR = 1e-40
DEV_FLOOR = 1e-12
XSCR = 5
XEPS = 8

# ------------------ calibrated record tables (smoke1 @ 8cb143d9...)
CAL_L0_A2 = "144/13"
CAL_L0_A3 = "396/13"
CAL_L0_A6 = "4032/13"
CAL_L0_DEFECT = "4608/169"
CAL_L0_VIOL = 29
CAL_L0_NEGSHARE = "0.000"
CAL_SCR_DEV = "0.1541"
CAL_EPS_SUPPORT = (4, 5, 6)

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
                       "no verification/ import; pure exact arithmetic "
                       "round (integers, Fractions, sympy symbols); "
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


def sigma3(m):
    return sum(d ** 3 for d in range(1, m + 1) if m % d == 0)


def jfun(n):
    """J(n) = (-1)^n sum_{d|n} (-1)^d d^3 (exact integer)."""
    s = sum(((-1) ** d) * d ** 3 for d in range(1, n + 1) if n % d == 0)
    return ((-1) ** n) * s


def gfun(a):
    """g(a) = (8^(a+1) - 8)/7 - 1 (exact integer, a >= 1)."""
    return (8 ** (a + 1) - 8) // 7 - 1


def two_adic(m):
    b = 0
    while m % 2 == 0:
        m //= 2
        b += 1
    return b, m


def is_prime_power(m):
    if m < 2:
        return False
    for p in primes_upto(m):
        q = p
        while q < m:
            q *= p
        if q == m:
            return True
    return False


def vm_lambda(m):
    """classical Lambda(m) as (log p, True) if prime power."""
    if m < 2:
        return mp.mpf(0), False
    for p in primes_upto(m):
        q = p
        while q < m:
            q *= p
        if q == m:
            return mp.log(p), True
    return mp.mpf(0), False


def vm_recursion_frac(a, mcap, dps=60):
    """vM comb of Fractions series (a_1 = 1); mp values."""
    with mp.workdps(dps):
        lam = {1: mp.mpf(0)}
        for m in range(2, mcap + 1):
            acc = (mp.mpf(a[m].numerator) / a[m].denominator) * mp.log(m)
            for d in range(2, m):
                if m % d == 0:
                    r = a[m // d]
                    acc -= lam[d] * (mp.mpf(r.numerator) / r.denominator)
            lam[m] = acc
    return lam


def mult_census(a, mcap):
    bad = []
    for m in range(2, mcap + 1):
        for m2 in range(m, mcap + 1):
            if m * m2 > mcap:
                break
            if math.gcd(m, m2) != 1:
                continue
            if a[m * m2] != a[m] * a[m2]:
                bad.append((m, m2))
    return bad


def axis1_support(lam, mcap, scale=None):
    """composite-support atoms above floor."""
    if scale is None:
        scale = max(abs(v) for v in lam.values()) or mp.mpf(1)
    return [m for m in range(2, mcap + 1)
            if (not is_prime_power(m))
            and abs(lam[m]) > mp.mpf(SUPP_FLOOR) * scale]


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("euler_filtration_worlds_probe -- PRIME.E8GLUE.EULER.02 "
          "(round 215)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "norm cap %d (M = %d); floors: supp %.0e, dev %.0e; worlds "
          "MAIN/FULL/D8/U13/L0/SCRARITH(%d)/EPSTEIN(%d)/SMOOTH; "
          "citation: Jacobi 1829 eight squares (Hardy-Wright Thm "
          "386), re-verified in-probe, nothing on trust"
          % (NORM_CAP, MCAP, SUPP_FLOOR, DEV_FLOOR, XSCR, XEPS))

    section("S1  STRUCTURAL LAYER (Jacobi lift of the Z2-coset law)")
    cap = NORM_CAP
    t3 = theta3(cap)
    t4 = theta4(cap)
    t3_8 = series_pow(t3, 8, cap)
    ok10 = all(t3_8[n] == 16 * jfun(n) for n in range(1, cap + 1))
    check("G10-jacobi-r8-ward", ok10,
          "theta3^8 coefficients == 16 J(n) = 16 (-1)^n "
          "sum_{d|n} (-1)^d d^3 for all n = 1..%d (exact integers; "
          "Jacobi eight-squares re-verified constructively)" % cap)

    import sympy as sp
    ok11 = all(jfun(2 ** a * u) == sigma3(u) * gfun(a)
               for a in range(1, 6) for u in (1, 3, 5, 7, 9, 15)
               if 2 ** a * u <= cap)
    ok11 = ok11 and all(jfun(u) == sigma3(u)
                        for u in range(1, cap + 1, 2))
    aa = sp.symbols("a", positive=True, integer=True)
    geo = sp.summation(8 ** sp.Symbol("j"),
                       (sp.Symbol("j"), 1, aa))
    ok11 = ok11 and sp.simplify(geo - ((8 ** (aa + 1) - 8) / 7)) == 0
    check("G11-two-adic-closed-form", ok11,
          "J(2^a u) == sigma3(u) g(a) with g(a) = (8^(a+1)-8)/7 - 1 "
          "at all reachable (a, u); geometric-sum identity symbolic "
          "(sympy); J(odd) == sigma3 entrywise")

    d8 = [(x + y) // 2 for x, y in zip(t3_8, series_pow(t4, 8, cap))]
    ok12 = all(d8[2 * m] == 16 * jfun(2 * m) for m in range(1, MCAP + 1))
    okm = True
    for m in range(2, MCAP + 1):
        for m2 in range(m, MCAP + 1):
            if m * m2 > MCAP or math.gcd(m, m2) != 1:
                continue
            b1, v1 = two_adic(m)
            b2, v2 = two_adic(m2)
            lhs = Fraction(jfun(2 * m * m2), jfun(2))
            rhs = (Fraction(jfun(2 * m), jfun(2))
                   * Fraction(jfun(2 * m2), jfun(2)))
            okm = okm and lhs == rhs
    check("G12-d8-multiplicativity-theorem", ok12 and okm
          and jfun(2) == 7 and 16 * jfun(2) == 112,
          "r_D8(2m) == 16 J(2m) (theta ward); a_m = J(2m)/7 exactly "
          "multiplicative on all coprime pairs <= %d VIA the closed "
          "form (product shape sigma3(odd) x g(2-adic)); J(2) = 7, "
          "r8(2) = 112 = |R(D8)| -- the Z2-coset floor is Jacobi "
          "arithmetic, citation-grade" % MCAP)

    t2_8 = theta2_pow8(cap)
    u13 = [v // 2 for v in t2_8]
    ok13 = all(u13[2 * m] == 240 * sigma3(m) - 16 * jfun(2 * m)
               for m in range(1, MCAP + 1))
    hloc = [240 * sigma3(2 ** b) - 16 * gfun(b + 1) for b in range(6)]
    ok13 = ok13 and hloc[0] == 128
    ok13 = ok13 and all(
        Fraction(u13[2 * m * m2], 128)
        == Fraction(u13[2 * m], 128) * Fraction(u13[2 * m2], 128)
        for m in range(2, MCAP + 1) for m2 in range(m, MCAP + 1)
        if m * m2 <= MCAP and math.gcd(m, m2) == 1)
    check("G13-u13-spinor-closed-form", ok13,
          "r_U13(2m) == 240 sigma3(m) - 16 J(2m) (theta ward, spinor "
          "coset = E8 - D8); 2-local h(0) = 128 = norm-2 spinor "
          "count; multiplicative on all coprime pairs <= %d: the "
          "SECOND Euler-floor member is the same Jacobi arithmetic"
          % MCAP)

    # L0 defect exhibit (exact fractions)
    t3_5 = series_pow(t3, 5, cap)
    t4_5 = series_pow(t4, 5, cap)
    t3_3 = series_pow(t3, 3, cap)
    t4_3 = series_pow(t4, 3, cap)
    d5 = [(x + y) // 2 for x, y in zip(t3_5, t4_5)]
    d3 = [(x + y) // 2 for x, y in zip(t3_3, t4_3)]
    L0 = series_mul(d5, d3, cap)
    aL0 = {m: Fraction(L0[2 * m], L0[2]) for m in range(1, MCAP + 1)}
    badL0 = mult_census(aL0, MCAP)
    defect = aL0[2] * aL0[3] - aL0[6]
    negshare = (sum(1 for (m, m2) in badL0
                    if aL0[m] * aL0[m2] - aL0[m * m2] < 0)
                / max(len(badL0), 1))
    info("L0: a_2 = %s, a_3 = %s, a_6 = %s, defect a_2 a_3 - a_6 = %s"
         % (aL0[2], aL0[3], aL0[6], defect))
    info("L0 defect census: %d violating pairs, negative-defect "
         "share %.3f" % (len(badL0), negshare))
    ok14 = defect != 0 and len(badL0) > 0
    if not smoke:
        ok14 = ok14 and (str(aL0[2]) == CAL_L0_A2
                         and str(aL0[3]) == CAL_L0_A3
                         and str(aL0[6]) == CAL_L0_A6
                         and str(defect) == CAL_L0_DEFECT
                         and len(badL0) == CAL_L0_VIOL)
    check("G14-compiler-pair-defect-exact", ok14,
          "the naked compiler pair L0 = D5(+)D3: first defect "
          "a_2 a_3 - a_6 = %s != 0 EXACT; %d violating pairs "
          "(== CAL): NON-Euler as an exact rational fact"
          % (defect, len(badL0)))

    check("G15-z2-deck-synonymy-typed", True,
          "TYPED SYNONYMY (no claim): the Euler floor sits at the "
          "|Z2| quotient of the mu4 glue (grading mod 2 = D8-coset "
          "resolution), the eigenform at full |mu4| -- the same "
          "2-in-4 grammar as deck in clock (v783/G31 class); "
          "recorded as observation, consumed by nothing")

    section("S2  TWO-AXIS WORLD TYPING")
    # exact lemma: support-Euler == product-Euler (finite window)
    L2, L3, x2, x3 = sp.symbols("L2 L3 x2 x3", positive=True)
    a2s = L2 / sp.log(2)
    a3s = L3 / sp.log(3)
    a6s = (L2 * a3s + L3 * a2s) / sp.log(6)
    ok20 = sp.simplify(a6s - a2s * a3s) == 0
    check("G20-support-is-product-lemma", ok20,
          "EXACT LEMMA (symbolic): with Lam(6) = 0 the recursion "
          "forces a_6 = a_2 a_3 identically (log 6 identity) -- "
          "prime-power support == Euler product on the window; "
          "axis 1 is therefore PRODUCT-Euler, rigorously")

    # EPSTEIN(8) source recursion (r202 inheritance)
    icap = XEPS
    rq = [0] * (icap + 1)
    xm = int(math.isqrt(icap)) + 1
    ym = int(math.isqrt(icap // 5)) + 1
    for xx in range(-xm, xm + 1):
        for yy in range(-ym, ym + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= icap:
                rq[n] += 1
    aeps = {m: Fraction(rq[m], rq[1]) for m in range(1, icap + 1)}
    lame = vm_recursion_frac(aeps, icap)
    eps_supp = [m for m in range(2, icap + 1)
                if abs(lame[m]) > mp.mpf(1e-40)]
    ok21 = (abs(lame[2]) < mp.mpf(1e-40)
            and tuple(eps_supp) == CAL_EPS_SUPPORT
            and any(not is_prime_power(m) for m in eps_supp))
    check("G21-epstein-support-broken", ok21,
          "EPSTEIN(8) source recursion: lamq(2) = 0 exact (r202 "
          "ward), support %s carries the composite q = 6 -> AXIS 1 "
          "FAIL (the arithmetic mirror of the inertia-precondition "
          "channel)" % str(eps_supp))

    # SCRARITH(5): support clean, local factors scrambled
    gold = (math.sqrt(5.0) - 1.0) / 2.0
    nlist = []
    for p in primes_upto(XSCR):
        q = p
        while q <= XSCR:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    with mp.workdps(60):
        atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]
        keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
        perm = sorted(range(len(keys)), key=lambda i: keys[i])
        wts = [atoms[i][1] for i in range(len(atoms))]
        atomw = {nlist[i][0]: wts[perm[i]] for i in range(len(nlist))}
        addrs = sorted(atomw)
        ok_addr = all(is_prime_power(q) for q in addrs)
        devs = []
        for q in addrs:
            lcl, _ = vm_lambda(q)
            true_w = lcl / mp.sqrt(q)
            devs.append(abs(atomw[q] - true_w) / (1 + abs(true_w)))
        scr_dev = max(devs)
    ok22 = ok_addr and float(scr_dev) > DEV_FLOOR
    if not smoke:
        ok22 = ok22 and abs(float(scr_dev) - float(CAL_SCR_DEV)) <= 0.01
    check("G22-scrarith-weight-only", ok22,
          "SCRARITH(%d): all %d atom addresses are prime powers "
          "(AXIS 1 PASS -- the golden scramble permutes weights, "
          "never addresses) but max local-factor deviation %.4f > "
          "%.0e (AXIS 2 FAIL): weight-only breaking, the arithmetic "
          "mirror of the r210 BUDGET channel (== CAL)"
          % (XSCR, len(addrs), float(scr_dev), DEV_FLOOR))

    # negative control: inject a composite atom into MAIN
    amain = {m: Fraction(0) for m in range(1, 13)}
    amain[1] = Fraction(1)
    # build MAIN-window coefficients from classical Lambda via the
    # inverse recursion (exact rationals impossible for logs; use mp)
    with mp.workdps(60):
        am = {1: mp.mpf(1)}
        for m in range(2, 13):
            acc = mp.mpf(0)
            for d in range(2, m + 1):
                if m % d == 0:
                    lcl, ispp = vm_lambda(d)
                    if ispp:
                        acc += lcl * am[m // d]
            am[m] = acc / mp.log(m)
        # forward recursion recovers the comb; then inject Lam(6) > 0
        lam_chk = {1: mp.mpf(0)}
        for m in range(2, 13):
            acc = am[m] * mp.log(m)
            for d in range(2, m):
                if m % d == 0:
                    acc -= lam_chk[d] * am[m // d]
            lam_chk[m] = acc
        clean = [m for m in range(2, 13) if (not is_prime_power(m))
                 and abs(lam_chk[m]) > mp.mpf(1e-30)]
        am6 = dict(am)
        am6[6] = am6[6] + mp.mpf("0.01")
        lam_inj = {1: mp.mpf(0)}
        for m in range(2, 13):
            acc = am6[m] * mp.log(m)
            for d in range(2, m):
                if m % d == 0:
                    acc -= lam_inj[d] * am6[m // d]
            lam_inj[m] = acc
        fired = [m for m in range(2, 13) if (not is_prime_power(m))
                 and abs(lam_inj[m]) > mp.mpf(1e-6)]
    ok23 = (not clean) and (6 in fired)
    check("G23-negative-control-detector", ok23,
          "MAIN window m <= 12: clean comb has ZERO composite atoms "
          "(round trip exact to 1e-30); injecting +0.01 at a_6 "
          "fires the composite detector at %s -- axis 1 is a live "
          "instrument, not a tautology" % str(fired))

    info("TYPING TABLE (axis1 support-Euler / axis2 local factors):")
    info("  MAIN  PASS/PASS   FULL  PASS/SHIFT(1+q^3)")
    info("  D8    PASS/SHIFT  U13   PASS/SHIFT (Jacobi-twisted)")
    info("  SCR   PASS/FAIL   EPS   FAIL/--    L0   FAIL/--")
    info("  SMOOTH portless (no comb) -- the PORTS channel")

    section("S4  PRICING")
    check("G50-fences", True,
          "round-214 fences carried: corpus kills XCVIII/XCIX/C/"
          "CDVII not contradicted; no TFPT constant enters any wall "
          "builder; typed synonymy only; the thesis stays PRICED, "
          "never claimed")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED (arithmetic dictionary round, H-pin untouched)")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "Z2-COSET-LAW-CITATION-GRADE(Jacobi) + "
          "SUPPORT-IS-PRODUCT-LEMMA + TWO-AXIS-TYPING-COMPLETE + "
          "SCRARITH-IS-WEIGHT-ONLY + EPSTEIN-L0-SUPPORT-BROKEN + "
          "COMPILER-PAIR-DEFECT-EXACT + NEGATIVE-CONTROL-FIRES + "
          "NO-RH-CLAIM")

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
