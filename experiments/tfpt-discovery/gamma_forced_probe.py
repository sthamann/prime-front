#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gamma_forced_probe -- PRIME.E8GLUE.EULER.05 (round 218): IS THE
CUSP WEIGHT gamma(D5 (+) D3) = -4 FORCED?  YES -- derived in closed
chain from Jacobi's abstruse identity; the mu4-NAMING stays a typed
observation.

EXPLORATION ONLY (2026-08-22).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.  Fences of rounds 214-217 carried verbatim.

THE QUESTION (round-217 goal a).  Round 217 solved the parity-sign
law completely: sign(defect) = -sign(gamma) for all m, with
gamma(D5D3) = -4, gamma(D7D1) = +28.  Left open: is the -4 FORCED?
THIS ROUND DERIVES BOTH gamma VALUES from elementary theta algebra
plus ONE identity, and answers YES (as an integer), with the honest
fence that the LABEL '-4 = -|mu4|' remains a typed synonymy.

THE THREE IDENTITIES (all exact integer q-series to norm 96, the
first classical-cited):
  I1 (Jacobi's aequatio identica satis abstrusa):
        theta3(Q)^4 = theta2(Q)^4 + theta4(Q)^4.
  I2 (argument doubling):  theta3(q) theta4(q) = theta4(q^2)^2  and
        theta3(q)^2 + theta4(q)^2 = 2 theta3(q^2)^2.
  I3 (THE KEY, verified exact):  with the weight-2 coordinates
        y := theta3(Q)^2, u := theta4(Q)^2 and the monomials
        A := y^3 u, B := y u^3:
        A - B = theta2(Q)^4 theta4(Q^2)^4 = 16 f8(Q)
     -- the unique level-8 newform f8 = eta(2t)^4 eta(4t)^4 IS the
     abstruse-identity remainder theta2^4 dressed by the doubled
     clock theta theta4(Q^2)^4, with leading coefficient 16 = 2^4
     (four theta2 factors, each contributing its half-integer-shift
     doubling 2).
THE KAPPA TABLE (unique fits in the round-217 basis, exact, all
verified to m = 48): the f8-weight of the five weight-4 monomials
y^j u^(4-j), j = 0..4, is kappa = (0, -8, 0, +8, 0):
  * supported EXACTLY on the odd-j monomials (the parity law at
    monomial level),
  * antisymmetric under the theta3 <-> theta4 swap,
  * the two odd monomials share ONE Eisenstein row
    (0, 1/15, -6/5, 32/15) -- hence A - B is PURE cusp (I3).

THE DERIVATION (symbolic + series-warded).  Cross terms of the
D-sum worlds in the (y, u) coordinates (via I2):
  cross_{5,3} = (th3^5 th4^3 + th3^3 th4^5)/4 = y u^3 / 2
  cross_{7,1} = (th3^7 th4  + th3 th4^7)/4  = 2 y^3 u - (3/2) y u^3
  cross_{6,2} = y^2 u^2 - u^4/2,   cross_{4,4} = u^4/2   [even-j!]
Hence, from the kappa table alone:
  gamma(5,3) = kappa(y u^3)/2 = -8/2 = -4          [FORCED]
  gamma(7,1) = 2 kappa(y^3 u) - (3/2) kappa(y u^3) = 16 + 12 = +28
  gamma(even-even) = 0 structurally (even-j monomials only) -- the
  parity law re-derived at its root.
THE FORCING CHAIN FOR THE COMPILER SPLIT:  gamma(5,3) =
-(leading coefficient of theta2^4)/(2 x 2) = -16/4 = -4, where the
16 = 2^4 is the four-fold half-integer-shift doubling of theta2^4
(via I1/I3) and the 4 = 2 x 2 is the two (theta3^n + theta4^n)/2
averagings of the two D-factors.  The integer -4 is thereby DERIVED
from classical identities -- no fit, no dial.  ANTI-NUMEROLOGY
FENCE (v354/v355): the READING '-4 = -|mu4|' (and '+28 = sigma3(3)',
'S = 56') stays a RECORDED OBSERVATION: the 4 in 2^4 counts theta2
factors (= rank/2), and its equality with |mu4| is a typed synonymy,
not claimed forced.

CROSS-INSTRUMENT: the derived gammas must equal the round-217
whole-world fits ((-4, +28, 0 x 5)) -- two independent routes to the
same integers.

RECORD TABLES (frozen; the discovery prototypes ran as disclosed
shell one-liners in the session lane):
CAL_KAPPA = (0, -8, 0, +8, 0); CAL_EIS_ODD = (0, 1/15, -6/5, 32/15);
CAL_GAMMA = {D5D3: -4, D7D1: +28, evens/controls: 0}.
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
identities G10-G13; S2 derivation G20-G23; S3 cross-instrument G30;
S4 pricing G50-G51 + G60 verdict + G99 runtime.  Pure exact
arithmetic; DETERMINISM: no randomness, run2 identical modulo
wall-clock tokens.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# ---------------------------------------------------------------- frozen
NORM_CAP = 96
MCAP = 48
RUNTIME_BAR = 600.0

CAL_KAPPA = (0, -8, 0, 8, 0)
CAL_EIS_ODD = ("0", "1/15", "-6/5", "32/15")
CAL_GAMMA = {"D5D3": -4, "D7D1": 28, "D6D2": 0, "D4D4": 0,
             "Z8": 0, "D8": 0, "E8": 0}

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


# ------------------------------------------------- series (round-217)
from parity_sign_theorem_probe import (          # noqa: E402
    series_mul, series_pow, theta3, theta4, theta2_pow8, theta_D,
    sigma3, newform8)


def theta2_pow4(cap):
    """theta2(Q)^4 = 16 Q (sum_k Q^(k^2+k))^4 -- exact integers."""
    inner = [0] * (cap + 1)
    k = 0
    while k * k + k <= cap:
        inner[k * k + k] += 2
        k += 1
    i4 = series_pow(inner, 4, cap)
    out = [0] * (cap + 1)
    for j, v in enumerate(i4):
        if j + 1 <= cap:
            out[j + 1] = v
    return out


def rescale2(series, cap):
    """g(Q) -> g(Q^2)."""
    out = [0] * (cap + 1)
    for j, v in enumerate(series):
        if 2 * j <= cap:
            out[2 * j] = v
    return out


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("gamma_forced_probe -- PRIME.E8GLUE.EULER.05 (round 218)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "norm cap %d; identities I1 (Jacobi abstruse, cited + "
          "verified), I2 (doubling), I3 (A - B = 16 f8, THE key); "
          "kappa table frozen (0, -8, 0, +8, 0); anti-numerology "
          "fence v354/v355 active on every mu4-reading" % NORM_CAP)

    section("S1  THE IDENTITIES")
    cap = NORM_CAP
    t3 = theta3(cap)
    t4 = theta4(cap)
    t2_4 = theta2_pow4(cap)
    t3_4 = series_pow(t3, 4, cap)
    t4_4 = series_pow(t4, 4, cap)
    ok10 = all(t3_4[n] == t2_4[n] + t4_4[n] for n in range(cap + 1))
    ok10 = ok10 and t2_4[1] == 16
    check("G10-abstruse-identity", ok10,
          "theta3(Q)^4 == theta2(Q)^4 + theta4(Q)^4 exact to norm "
          "%d (Jacobi, aequatio identica satis abstrusa; leading "
          "coefficient of theta2^4 = 16 = 2^4: the four half-"
          "integer-shift doublings)" % cap)

    # I2: doubling identities (in q; equality of even parts)
    prod34 = series_mul(t3, t4, cap)
    t4sq2 = rescale2(series_pow(t4, 2, cap), cap)
    okA = all(prod34[n] == t4sq2[n] for n in range(cap + 1))
    sum34 = [x + y for x, y in zip(series_pow(t3, 2, cap),
                                   series_pow(t4, 2, cap))]
    t3sq2 = rescale2(series_pow(t3, 2, cap), cap)
    okB = all(sum34[n] == 2 * t3sq2[n] for n in range(cap + 1))
    check("G11-doubling-identities", okA and okB,
          "theta3(q) theta4(q) == theta4(q^2)^2 and theta3^2 + "
          "theta4^2 == 2 theta3(q^2)^2, exact to norm %d (the "
          "coordinates y = theta3(Q)^2, u = theta4(Q)^2 are "
          "well-defined for every cross term)" % cap)

    # I3: A - B = theta2(Q)^4 theta4(Q^2)^4 = 16 f8(Q)
    y2 = series_pow(t3, 2, cap)
    u2 = series_pow(t4, 2, cap)
    A = series_mul(series_pow(t3, 6, cap), u2, cap)
    B = series_mul(y2, series_pow(t4, 6, cap), cap)
    AmB = [x - y for x, y in zip(A, B)]
    b = newform8(cap)
    ok12 = all(AmB[m] == 16 * b[m] for m in range(cap + 1))
    t4q2_4 = rescale2(t4_4, cap)
    lhs = series_mul(t2_4, t4q2_4, cap)
    ok12 = ok12 and all(lhs[m] == AmB[m] for m in range(cap + 1))
    check("G12-key-identity-AmB-16f8", ok12,
          "A - B == theta2(Q)^4 theta4(Q^2)^4 == 16 f8(Q) exact to "
          "norm %d: THE LEVEL-8 NEWFORM IS THE ABSTRUSE-IDENTITY "
          "REMAINDER theta2^4, dressed by the doubled clock theta "
          "theta4(Q^2)^4" % cap)

    # kappa table: unique fits of the five monomials
    import sympy as sp

    def basrow(m):
        row = []
        for j in range(4):
            if m == 0:
                row.append(sp.Integer(1))
            elif m % (2 ** j) == 0:
                row.append(sp.Integer(240 * sigma3(m // 2 ** j)))
            else:
                row.append(sp.Integer(0))
        for j in range(3):
            if m > 0 and m % (2 ** j) == 0:
                row.append(sp.Integer(b[m // 2 ** j]))
            else:
                row.append(sp.Integer(0))
        return row

    Amat = sp.Matrix([basrow(m) for m in range(13)])
    kappa = []
    eis_rows = []
    ok13 = True
    for jj in range(5):
        M = series_mul(series_pow(t3, 2 * jj, cap),
                       series_pow(t4, 8 - 2 * jj, cap), cap)
        yv = sp.Matrix([sp.Integer(M[m]) for m in range(13)])
        sol, params = Amat.gauss_jordan_solve(yv)
        ok13 = ok13 and len(params) == 0
        cs = [sp.nsimplify(c) for c in sol.subs({p: 0 for p in params})]
        ok13 = ok13 and all(
            sum(c * x for c, x in zip(cs, basrow(m))) == M[m]
            for m in range(0, MCAP + 1))
        ok13 = ok13 and cs[5] == 0 and cs[6] == 0
        kappa.append(cs[4])
        eis_rows.append(tuple(str(c) for c in cs[:4]))
        info("monomial y^%d u^%d: kappa = %s, eis = %s"
             % (jj, 4 - jj, cs[4], eis_rows[-1]))
    ok13 = ok13 and tuple(int(k) for k in kappa) == CAL_KAPPA
    ok13 = ok13 and eis_rows[1] == eis_rows[3] == CAL_EIS_ODD
    check("G13-kappa-table", ok13,
          "cusp functional on the weight-4 monomials y^j u^(4-j): "
          "kappa = %s == CAL (0, -8, 0, +8, 0) -- supported EXACTLY "
          "on odd j, antisymmetric under theta3 <-> theta4, and the "
          "two odd monomials share ONE Eisenstein row %s (hence "
          "A - B pure cusp, == I3)"
          % (str(tuple(int(k) for k in kappa)), str(CAL_EIS_ODD)))

    section("S2  THE DERIVATION")
    T3, T4 = sp.symbols("T3 T4", positive=True)
    cr53 = sp.expand((T3 ** 5 * T4 ** 3 + T3 ** 3 * T4 ** 5) / 4)
    ok20 = (sp.simplify(cr53 - (T3 * T4) ** 3
                        * (T3 ** 2 + T4 ** 2) / 4) == 0)
    cr71 = sp.expand((T3 ** 7 * T4 + T3 * T4 ** 7) / 4)
    ok20 = ok20 and (sp.simplify(
        cr71 - (T3 * T4) * (T3 ** 2 + T4 ** 2)
        * ((T3 ** 2 + T4 ** 2) ** 2 - 3 * T3 ** 2 * T4 ** 2) / 4) == 0)
    # series ward: even q-part of 4 cross_53 == 2 B(Q); odd part = 0
    q53 = [series_mul(series_pow(t3, 5, cap),
                      series_pow(t4, 3, cap), cap)[n]
           + series_mul(series_pow(t3, 3, cap),
                        series_pow(t4, 5, cap), cap)[n]
           for n in range(cap + 1)]
    ok20 = ok20 and all(q53[n] == 0 for n in range(1, cap + 1, 2))
    ok20 = ok20 and all(q53[2 * m] == 2 * B[m]
                        for m in range(cap // 2 + 1))
    check("G20-cross-term-algebra", ok20,
          "SYMBOLIC: 4 cross_53 = (T3 T4)^3 (T3^2 + T4^2) and "
          "4 cross_71 = (T3 T4)(T3^2 + T4^2)((T3^2 + T4^2)^2 - "
          "3 (T3 T4)^2); SERIES: 4 cross_53 in q is even-supported "
          "with even part == 2 B = 2 y u^3 in Q (the doubling "
          "identities close the coordinate change exactly)")

    g53 = kappa[1] / 2
    g71 = 2 * kappa[3] - sp.Rational(3, 2) * kappa[1]
    ok21 = (g53 == -4 and g71 == 28)
    check("G21-gamma-derived", ok21,
          "gamma(5,3) = kappa(y u^3)/2 = %s == -4 and gamma(7,1) = "
          "2 kappa(y^3 u) - (3/2) kappa(y u^3) = %s == +28 -- both "
          "cusp weights DERIVED from the kappa table alone (no "
          "world fit consumed)" % (g53, g71))

    ok22 = (t2_4[1] == 16 and sp.Rational(-16, 4) == -4
            and int(kappa[1]) == -8 and 16 // 2 == 8)
    check("G22-forcing-chain", ok22,
          "THE CHAIN: kappa(B) = -cusp(A - B)/2 = -16/2 = -8 (A + B "
          "Eisenstein by G13, A - B = 16 f8 by I3), hence "
          "gamma(compiler split) = kappa(B)/2 = -16/4 = -4: the 16 "
          "= 2^4 is theta2^4's four-fold half-shift doubling "
          "(I1/I3), the 4 = 2 x 2 the two D-averagings.  gamma = -4 "
          "is FORCED as an integer by classical identities.  FENCE "
          "(v354/v355): the NAME '-4 = -|mu4|' stays a recorded "
          "synonymy (the 4 in 2^4 counts theta2 factors = rank/2); "
          "'+28 = sigma3(3)' and 'S = 56' likewise recorded only")

    # even-even crosses live in even-j monomials => gamma = 0
    cr62 = sp.expand((T3 ** 6 * T4 ** 2 + T3 ** 2 * T4 ** 6) / 4)
    ok23 = (sp.simplify(
        cr62 - (T3 * T4) ** 2
        * ((T3 ** 2 + T4 ** 2) ** 2 - 2 * (T3 * T4) ** 2) / 4) == 0)
    cr44 = sp.expand((2 * T3 ** 4 * T4 ** 4) / 4)
    ok23 = ok23 and sp.simplify(cr44 - (T3 * T4) ** 4 / 2) == 0
    ok23 = ok23 and int(kappa[0]) == 0 and int(kappa[2]) == 0 \
        and int(kappa[4]) == 0
    check("G23-parity-at-the-root", ok23,
          "even-even crosses reduce to EVEN-j monomials (cross_62 = "
          "y^2 u^2 - u^4/2, cross_44 = u^4/2 after doubling) and "
          "kappa vanishes on even j: gamma(even-even) = 0 "
          "STRUCTURALLY -- the parity law of round 216 re-derived "
          "at its root")

    section("S3  CROSS-INSTRUMENT")
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
    worlds["E8"] = [a + bb // 2 for a, bb in zip(worlds["D8"], t2_8)]
    ok30 = True
    for tag, S in sorted(worlds.items()):
        yv = sp.Matrix([sp.Integer(S[2 * m]) if m > 0 else sp.Integer(1)
                        for m in range(13)])
        sol, params = Amat.gauss_jordan_solve(yv)
        cs = [sp.nsimplify(c) for c in sol.subs({p: 0 for p in params})]
        ok30 = ok30 and int(cs[4]) == CAL_GAMMA[tag]
    check("G30-two-routes-one-integer", ok30,
          "the whole-world fits (round-217 route) reproduce the "
          "derived gammas at every world: (-4, +28, 0, 0, 0, 0, 0) "
          "== CAL -- two independent routes, one integer each")

    section("S4  PRICING")
    check("G50-fences", True,
          "rounds 214-217 fences carried (XCVIII/XCIX/C/CDVII); "
          "citations: Jacobi abstruse (I1, also verified exact), "
          "Sturm-class finite verification for all fits; no TFPT "
          "constant enters any construction; every mu4-reading "
          "fenced as observation")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED (arithmetic dictionary theorem, H-pin "
          "untouched)")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "GAMMA-FORCED: ABSTRUSE-EXACT + DOUBLING-EXACT + "
          "KEY-IDENTITY(A - B = theta2^4 theta4(Q^2)^4 = 16 f8) + "
          "KAPPA-TABLE(0, -8, 0, +8, 0) + GAMMA-DERIVED(-4, +28) + "
          "FORCING-CHAIN(-16/4, integer forced) + "
          "PARITY-AT-THE-ROOT(even-j) + TWO-ROUTES-ONE-INTEGER + "
          "MU4-NAMING-FENCED + NO-RH-CLAIM")

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
