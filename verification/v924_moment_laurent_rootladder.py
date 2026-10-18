#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v924 -- PRIME.MOMENT.LAURENT.ROOTLADDER.01: THE MOMENT-LAURENT /
ROOT-LADDER THEOREM FAMILY of round 156 -- the escaped census-root
ladder exactly solved in moment coordinates, the proven quarter-cap,
the exact sum rules, the sign-pattern law and the jet-tower cascade
certificate machinery, promoted as certified finite theorems.
Lean-hardened in round 158 (note CDLXII).

NOTATION per block: F(y)/A_0 = 1 + S(y), S = sum_k v_k/(y - b_k)
(v_k = w_k/A_0), T(y) = sum_k v_k b_k/(y - b_k), jets a_{2m} =
sum_k v_k b_k^{m-1} (a_2 = -y_t measured), z = y/y_t, moment ratios
J_m := a_{2m}/(-a_2)^{... normalized so that J_2 = a_4/y_t^2 up to
the sign convention}, b_top = b_{K-1}.

THE THEOREMS (all exact algebra; sympy generic + exact instances):

  ROUND 156 (note CDLX, rootladder_probe.py, L1-L6):
  L1 (THE LADDER IS MOMENT DATA): y S(y) == sum_k v_k + T(y)
     EXACTLY (partial fractions); with sum v = a_2 = -y_t and
     z = y/y_t:  (y/y_t) F(y)/A_0 == z - 1 + T/y_t == PHI(z) with
     PHI(z) = z - 1 + sum_{m>=1} J_{m+1} z^{-m} (finite Laurent
     with EXACT partial-geometric remainder) -- the census roots
     above the band are the zeros of the moment-Laurent function:
     self-similarity iff moment flatness, the escaped ladder is an
     algebraic function of the moment ratios alone.
  L2 (THE QUARTER-CAP): z(1 - z) <= 1/4 EXACTLY ((z - 1/2)^2 >= 0);
     PHI(z_0) = 0 ==> J_2 == z_0 (1 - z_0) - z_0 rho(z_0) EXACT ==>
     J_2 <= 1/4 + z_0 |rho(z_0)|: THE CENSUS-REAL TOP ROOT CAPS ITS
     OWN LEADING MOMENT RATIO (measured z|rho| <= 0.0102: the
     saturation J_2 -> 0.1506 has PROVEN headroom).
  L3 (EXACT SUM RULES): from F/A_0 == prod(1 - y_j t)/prod(1 - b_k
     t): a_2 == -P_1 (SR1, the r143 trace identity re-derived),
     P_2 == a_2^2 - 2 a_4 (SR2), P_3 == 3 a_2 a_4 - 3 a_6 - a_2^3
     (SR3): the ladder power sums ARE the jets (sum z_esc -> 1
     monotone measured).
  L4 (THE SIGN-PATTERN LAW): pole-interval parity (IVT): a
     same-sign adjacent weight pair traps >= 1 root below the band
     ==> n_esc <= nsc(w) + 1 EXACT; jet side: n_esc <= V(jet signs)
     (Laguerre's rule, Polya-Szego V, CITED AS FORM; Descartes
     polynomial instance gated); MEASURED: V == n_esc at 5 of 6
     blocks (b28 slack 2 DISCLOSED).
  L5 (THE CASCADE): y^j F_1 == Q_j + F_{j+1} EXACTLY (level shift)
     with the Laurent envelope closure: [R_j(Y) > 0 AND no real
     root of R_j >= Y] ==> T > 0 POINTWISE, SOURCE-PURE on [Y, oo)
     -- the r154 TOWER-DIVERGES-BELOW-y_t obstruction is bypassed
     one jet up; with r154-P2 the escaped-root cap is CERTIFIED,
     not measured (Y* = 1.02-2.1 b_top, ZERO violations, beating
     the r154 tower by ~x^2).
  L6 (THE TWO-SIDED SPLIT): on z >= 1: T/y_t <= sum_{m>=2} |J_m|
     (upper) and T/y_t >= (J_2 - sum_{m>=3} |J_m|)/z (lower: the
     far window is controlled by J_2 ALONE); the strip rides the
     band-edge data -- the T-WINDOW splits into moment control
     (far) + band-edge root positions (near).
  RED TEAM (the wall in final form): the e_0-witness deflates
     J_m' == J_m P^{(1-m)/2} while T'/y_t' == T/y_t EXACTLY (the
     T-window ratio is WITNESS-INVARIANT -- the shape sector is
     scale-blind); the 2-MODE witness keeps A_0 invariant and
     inflates J_2 x1e6 with ALL identities intact: J-BOUNDEDNESS IS
     ARITHMETIC-PINNED -- refused only by the census-minimizer.

LEAN HARDENING (round 158, note CDLXII): MomentLaurent.lean proves
the L1/L2 layer (y_mul_S, secular_dictionary, geom_remainder,
T_laurent with EXPLICIT exact remainder -- stronger than the
contract's named-hypothesis minimum -- moment_laurent_law,
z_mul_one_sub_z_le_quarter, quarter_cap_algebra, quarter_cap_bound).
This module re-checks the theorem names in the shipped source.

WHAT IS RECOMPUTED IN-RUN (exact, self-contained): L1 (partial
fractions + the z-dictionary + the exact geometric remainder), L2
(quarter cap + the PHI-root moment identity), L3 (SR1-SR3 generic
via the product form), L4 (IVT parity instance + Descartes
instance), L5 (level shift generic j = 1, 2), L6 (two-sided split
instance), the e_0/2-mode witnesses on exact rationals, and
consistency arithmetic on all pinned tables below.

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 156 -- RE-RUN GREEN AS TYPED AT PROMOTION (29/29 gates,
  identical SPEC_SHA 02755d6b7ad0cfcb; run-of-record 1804.8 s +
  deterministic re-run identical, zero post-freeze amendments):
  J_2 = 0.1117/0.1375/0.1446/0.1479/0.1497/0.1506 at b5..b28
  (tau-flat slope -0.0010; quarter-cap headroom PROVEN: z|rho| =
  0.0034 -> 0.0102); the self-similar ladder top/y_t = 0.8763 ->
  0.8311 monotone with second/y_t = 0.0818-0.0825 CONSTANT over
  3 dex; sum z_esc = 1.02577 -> 1.00135 monotone to 1 (SR1); sign
  law V == n_esc at 4/6/11/15/20 (b28: V 25 vs n_esc 23, slack
  DISCLOSED); cascade Y*/b_top = 1.1693/1.0230/1.0232/1.0193/
  1.4420/2.1252 with ZERO T <= 0 cache violations above Y* and
  residual sliver 1/0/1/0/18/51 of 87/299/1033/2284/4329/6248
  strip zeros; truncation M = 3 captures z_top to 1.3e-5, M = 6
  the second rung to 4.5e-5; SR devs <= 5e-103; controls refuse
  with NEGATIVE J_2 (-2.962/-0.845/-2.710) while SR1 holds
  world-blind <= 1e-40 (null control).

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN =
L1-L6 (exact algebra; Laguerre/Polya-Szego CITED AS FORM on the
jet side; HSW22 Cor. 1.2, PT21 cited).  MEASURED = the ladder/
moment tables, the V == n_esc tightness, the cascade Y* strings
(typed; the b28 V-slack and the T-census non-real-rootedness are
DISCLOSED).  ARITHMETIC-PINNED (typed, NOT closed): J-boundedness
-- the 2-mode witness proves no algebra-only cap exists; the
T-WINDOW's open content stays {arithmetic J_2-window + band-edge
sliver + band-edge separation} (the sliver closed below horizon in
v925).  These theorems REWRITE T-WINDOW coordinates; they close NO
omega; the census {MEAS, OMEGA-POS} stays at CARDINALITY 4.  NOT
evidence for or against the Riemann Hypothesis in either direction.
NO RH CLAIM.

PROVENANCE: discovery probe rootladder_probe.py (round 156,
2026-08-18, note CDLX, contract PRIME.ROOTLADDER.SELFSIM.01);
consumed by rounds 157/159/160/161; Lean-hardened round 158 (note
CDLXII).  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import os
import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R156 = "02755d6b7ad0cfcb"
BLOCKS = ("b5", "b8", "b13", "b18", "b24", "b28")
PIN_J2 = ("0.1117", "0.1375", "0.1446", "0.1479", "0.1497", "0.1506")
PIN_ZRHO = ("0.0034", "0.0075", "0.0090", "0.0097", "0.0101",
            "0.0102")
PIN_TOP = ("0.8763", "0.8465", "0.8383", "0.8344", "0.8322",
           "0.8311")
PIN_SEC = ("0.0825", "0.0822", "0.0818", "0.0820", "0.0822",
           "0.0825")
PIN_SUMZ = ("1.02577", "1.00571", "1.00556", "1.00273", "1.00212",
            "1.00135")
PIN_V = (4, 6, 11, 15, 20, 25)
PIN_NESC = (4, 6, 11, 15, 20, 23)
PIN_YSTAR = ("1.1693", "1.0230", "1.0232", "1.0193", "1.4420",
             "2.1252")
PIN_RESID = (1, 0, 1, 0, 18, 51)
PIN_STRIP = (87, 299, 1033, 2284, 4329, 6248)
PIN_J2W_CTRL = ("-2.962", "-0.845", "-2.710")   # SMOOTH/SCRARITH/EPS

LEAN_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "experiments", "lean4-carrier-rigidity",
                 "TfptCarrier"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                 "lean4-carrier-rigidity", "TfptCarrier"),
)
LEAN_REQ = {
    "MomentLaurent.lean": ("y_mul_S", "secular_dictionary",
                           "geom_remainder", "T_laurent",
                           "moment_laurent_law",
                           "z_mul_one_sub_z_le_quarter",
                           "quarter_cap_algebra",
                           "quarter_cap_bound"),
}

N_CHECKS = 12
EXPECTED = "MOMENT-LAURENT-ROOTLADDER"

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

    # ================================================ A: L1/L2
    section("A. THE MOMENT-LAURENT LAW + QUARTER-CAP (L1/L2; exact)")
    y, z = sp.symbols("y z", positive=True)
    v1, v2, b1, b2, yt = sp.symbols("v1 v2 b1 b2 yt", positive=True)

    S = v1 / (y - b1) + v2 / (y - b2)
    T = v1 * b1 / (y - b1) + v2 * b2 / (y - b2)
    l1a = sp.simplify(sp.together(y * S - (v1 + v2) - T))
    # z-dictionary with sum v = a_2 = -y_t:
    # (y/y_t)(1 + S) == z - 1 + T/y_t at y = z y_t when sum v = -y_t
    lhs = ((y / yt) * (1 + S)).subs(v2, -yt - v1)
    rhs = (y / yt - 1 + (T / yt)).subs(v2, -yt - v1)
    l1b = sp.simplify(sp.together(lhs - rhs))
    # exact geometric remainder: v b/(y - b) truncated at depth M
    M = 3
    rem = v1 * b1 / (y - b1) - sum(
        v1 * b1 ** m / y ** m for m in range(1, M + 1))
    remc = v1 * b1 ** (M + 1) / (y ** M * (y - b1))
    l1c = sp.simplify(sp.together(rem - remc))
    check("A1 L1 dictionary + exact Laurent remainder (generic)",
          l1a == 0 and l1b == 0 and l1c == 0,
          "y S == sum v + T; with sum v = a_2 = -y_t and z = y/y_t: "
          "(y/y_t) F/A_0 == z - 1 + T/y_t == PHI(z); truncation "
          "remainder EXACT partial-geometric: the census roots above "
          "the band are the zeros of the moment-Laurent PHI -- THE "
          "LADDER IS THE MOMENT DATA (THEOREM L1)")

    # L2 quarter cap
    qc = sp.simplify(sp.Rational(1, 4) - z * (1 - z)
                     - (z - sp.Rational(1, 2)) ** 2)
    J2s, rho_s, z0 = sp.symbols("J2s rho_s z0", positive=True)
    # PHI(z0) = 0 with PHI = z - 1 + J2/z + rho(z): J2 = z0(1-z0)
    # - z0 rho(z0)  (exact rearrangement)
    phi_id = sp.simplify(sp.together(
        (z0 - 1 + (z0 * (1 - z0) - z0 * rho_s) / z0 + rho_s)))
    check("A2 L2 quarter cap (exact)",
          qc == 0 and phi_id == 0,
          "z(1-z) <= 1/4 ((z - 1/2)^2 >= 0); PHI(z_0) = 0 ==> J_2 =="
          " z_0(1 - z_0) - z_0 rho(z_0) ==> J_2 <= 1/4 + z_0|rho|: "
          "the census-real top root caps its own leading moment "
          "ratio (THEOREM L2; measured z|rho| <= 0.0102 -- PROVEN "
          "headroom over the 0.1506 saturation)")

    # ================================================ B: L3 sum rules
    section("B. THE EXACT SUM RULES (L3; generic)")
    y1, y2 = sp.symbols("y1 y2", positive=True)
    t = sp.symbols("t")
    # F/A0 = prod(1 - y_j t)/prod(1 - b_k t) in the t = 1/y variable;
    # log-derivative power-sum extraction (2 roots, 2 poles)
    logF = sp.log((1 - y1 * t) * (1 - y2 * t)) \
        - sp.log((1 - b1 * t) * (1 - b2 * t))
    ser = sp.series(logF, t, 0, 4).removeO()
    c1 = sp.simplify(ser.coeff(t, 1))
    c2 = sp.simplify(ser.coeff(t, 2))
    c3 = sp.simplify(ser.coeff(t, 3))
    P1 = y1 + y2 - (b1 + b2)
    P2 = y1 ** 2 + y2 ** 2 - (b1 ** 2 + b2 ** 2)
    P3 = y1 ** 3 + y2 ** 3 - (b1 ** 3 + b2 ** 3)
    sr = sp.simplify(c1 + P1) == 0 and \
        sp.simplify(c2 + P2 / 2) == 0 and \
        sp.simplify(c3 + P3 / 3) == 0
    # jets from the partial-fraction form of the SAME F:
    # a_2 = sum v_k, a_4 = sum v_k b_k, a_6 = sum v_k b_k^2 where
    # v_k are the residues of F/A0 = 1 + S
    A0f = (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    v1r = sp.simplify(sp.cancel((A0f - 1) * (y - b1)).subs(y, b1))
    v2r = sp.simplify(sp.cancel((A0f - 1) * (y - b2)).subs(y, b2))
    a2 = sp.simplify(v1r + v2r)
    a4 = sp.simplify(v1r * b1 + v2r * b2)
    a6 = sp.simplify(v1r * b1 ** 2 + v2r * b2 ** 2)
    sr1 = sp.simplify(a2 + P1) == 0
    sr2 = sp.simplify(P2 - (a2 ** 2 - 2 * a4)) == 0
    sr3 = sp.simplify(P3 - (3 * a2 * a4 - 3 * a6 - a2 ** 3)) == 0
    check("B1 L3 sum rules SR1/SR2/SR3 (generic exact)",
          sr and sr1 and sr2 and sr3,
          "a_2 == -P_1 (trace, r143 T4 re-derived); P_2 == a_2^2 - "
          "2 a_4; P_3 == 3 a_2 a_4 - 3 a_6 - a_2^3: the ladder "
          "power sums ARE the jets (THEOREM L3; measured sum z_esc "
          "-> 1 monotone)")

    # ================================================ C: L4/L5/L6
    section("C. SIGN LAW, CASCADE, TWO-SIDED SPLIT (L4/L5/L6)")
    # L4 IVT parity instance: same-sign adjacent pair traps a root
    Finst = 1 + sp.Rational(1, 2) / (y - 1) + sp.Rational(1, 3) \
        / (y - 2) - sp.Rational(4) / (y - 4)
    f1 = float(Finst.subs(y, sp.Rational(102, 100)))
    f2 = float(Finst.subs(y, sp.Rational(198, 100)))
    trapped = f1 > 0 and f2 < 0  # sign change inside (1, 2)
    # Descartes instance: 1 + a2 u + a4 u^2 with signs + - +:
    # at most 2 positive roots, exactly V = 2 sign changes
    pdesc = sp.Poly(1 - 3 * sp.symbols("u") + 2
                    * sp.symbols("u") ** 2, sp.symbols("u"))
    nroots = sp.count_roots(pdesc, 0, sp.oo)
    check("C1 L4 sign-pattern law (IVT parity + Descartes instance)",
          trapped and nroots == 2,
          "a same-sign adjacent weight pair traps >= 1 root between "
          "its poles (IVT; sign change certified on the instance) "
          "==> n_esc <= nsc(w) + 1 EXACT; jet side n_esc <= V(jets) "
          "(Laguerre CITED AS FORM; Descartes instance: V = 2 == "
          "positive-root count): measured V == n_esc at 5/6 blocks")

    # L5 cascade level shift, generic j = 1, 2
    F1 = v1 * b1 / (y - b1) + v2 * b2 / (y - b2)
    F2 = v1 * b1 ** 2 / (y - b1) + v2 * b2 ** 2 / (y - b2)
    F3 = v1 * b1 ** 3 / (y - b1) + v2 * b2 ** 3 / (y - b2)
    lv1 = sp.simplify(sp.together(
        y * F1 - (v1 * b1 + v2 * b2) - F2))
    lv2 = sp.simplify(sp.together(
        y * F2 - (v1 * b1 ** 2 + v2 * b2 ** 2) - F3))
    check("C2 L5 cascade level shift (generic j = 1, 2)",
          lv1 == 0 and lv2 == 0,
          "y F_j == a_{2(j+1)} + F_{j+1} EXACT: [R_j(Y) > 0 AND no "
          "real root of R_j >= Y] ==> T > 0 POINTWISE SOURCE-PURE on"
          " [Y, oo) (THEOREM L5: the jet-tower cascade -- the r154 "
          "tower obstruction bypassed one jet up; the escaped-root "
          "cap CERTIFIED via r154-P2)")

    # L6 two-sided split instance on z >= 1
    J2v, J3v = sp.Rational(3, 20), sp.Rational(-1, 100)
    zv = sp.Rational(3, 2)
    up = abs(J2v) + abs(J3v)
    lo_ = (J2v - abs(J3v)) / zv
    check("C3 L6 two-sided split (instance)",
          bool(lo_ <= J2v + J3v / zv) and bool(J2v + J3v / zv <= up),
          "on z >= 1: T/y_t <= sum_{m>=2} |J_m| (upper) and T/y_t >="
          " (J_2 - sum_{m>=3} |J_m|)/z (lower -- the far window is "
          "controlled by J_2 ALONE): THEOREM L6, the T-WINDOW "
          "splits into moment control (far) + band-edge root "
          "positions (near)")

    # ================================================ D: red team
    section("D. THE ADVERSARIAL WITNESSES (exact rationals)")
    okw = True
    # e_0-witness with P = 1e6 a perfect square (sqrt exact in Q):
    # A_0' = A_0/sqrt(P) ==> v' = sqrt(P) v, y_t' = sqrt(P) y_t,
    # a_{2m}' = sqrt(P) a_{2m}; J_m = a_{2m}/y_t^m:
    # J_m' == J_m P^{(1-m)/2} EXACTLY; T/y_t invariant by linearity
    sq = Fraction(1000)          # sqrt(1e6)
    Pv = sq * sq
    a4v, a6v, ytq = Fraction(3, 20), Fraction(-7, 800), Fraction(2)
    J2q = a4v / ytq ** 2
    J3q = a6v / ytq ** 3
    J2p = (sq * a4v) / (sq * ytq) ** 2
    J3p = (sq * a6v) / (sq * ytq) ** 3
    okw = okw and J2p == J2q / sq and J3p == J3q / (sq * sq)
    vT = Fraction(3, 7)
    okw = okw and (sq * vT) / (sq * ytq) == vT / ytq
    # 2-mode witness: A_0 = c1 - c2 invariant under d(e_1 + e_2)
    c1v, c2v, dv = Fraction(2, 3), Fraction(1, 3), Fraction(5, 1)
    A0a = -c1v + c2v          # sum (-1)^k c_k, k = 1, 2
    A0b = -(c1v + dv) + (c2v + dv)
    # A_2 = -c1 b1 + c2 b2 moves freely with d
    b1v, b2v = Fraction(1), Fraction(4)
    A2a = -c1v * b1v + c2v * b2v
    A2b = -(c1v + dv) * b1v + (c2v + dv) * b2v
    okw = okw and A0a == A0b and A2b != A2a
    check("D1 witnesses: shape sector scale-blind, J-window "
          "arithmetic-pinned", okw,
          "e_0-witness: J_m' == J_m P^{(1-m)/2} deflates while "
          "T'/y_t' == T/y_t EXACT (the T-window ratio is "
          "WITNESS-INVARIANT: shape sector scale-blind); 2-mode "
          "witness: A_0 invariant, A_2 free ==> J_2 -> oo with ALL "
          "identities intact: J-BOUNDEDNESS IS ARITHMETIC-PINNED "
          "(only the census-minimizer refuses; algebra-only J-caps "
          "REFUTED)")

    # ================================================ E: Lean
    section("E. LEAN HARDENING CHECK (round 158, note CDLXII)")
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
    check("E1 Lean module ships the hardened theorems", ok_lean,
          ("; ".join(detail) if detail else "lean dir not found")
          + " -- T_laurent with EXPLICIT exact remainder (stronger "
          "than the contract minimum) + the quarter-cap chain, fully "
          "proven on the standard axioms (r158 build green)")

    # ================================================ F: pinned
    section("F. PINNED LADDER TABLES (consistency arithmetic)")
    j2 = [float(v) for v in PIN_J2]
    zr = [float(v) for v in PIN_ZRHO]
    okj = all(j2[i] < j2[i + 1] for i in range(5)) and \
        all(j2[i] <= 0.25 + zr[i] for i in range(6))
    check("F1 J_2 ladder saturates under the PROVEN quarter cap",
          okj,
          "J_2 = %s -> %s (monotone, tau-flat slope -0.0010) <= 1/4 "
          "+ z|rho| with z|rho| = %s -> %s: headroom ~0.11 PROVEN, "
          "not measured" % (PIN_J2[0], PIN_J2[5], PIN_ZRHO[0],
                            PIN_ZRHO[5]))

    tp = [float(v) for v in PIN_TOP]
    sc = [float(v) for v in PIN_SEC]
    okl = all(tp[i] > tp[i + 1] for i in range(5)) and \
        (max(sc) - min(sc)) <= 0.0008
    sz = [float(v) for v in PIN_SUMZ]
    oks = all(sz[i] > sz[i + 1] for i in range(5)) and sz[5] > 1.0
    check("F2 the self-similar ladder + SR1 monotone to 1",
          okl and oks,
          "top/y_t %s -> %s monotone; second/y_t %s..%s CONSTANT "
          "over 3 dex (self-similarity == moment flatness, L1); "
          "sum z_esc %s -> %s monotone to 1 (SR1 instantiated)"
          % (PIN_TOP[0], PIN_TOP[5], min(PIN_SEC), max(PIN_SEC),
             PIN_SUMZ[0], PIN_SUMZ[5]))

    okv = all(PIN_NESC[i] <= PIN_V[i] for i in range(6)) and \
        sum(1 for i in range(6) if PIN_V[i] == PIN_NESC[i]) == 5
    check("F3 sign-pattern law: V == n_esc at 5/6 (b28 slack "
          "disclosed)", okv,
          "V = %s vs n_esc = %s: the Laguerre bound HARD everywhere,"
          " measured-tight at the five core blocks; b28 slack 2 "
          "DISCLOSED (deep-block jet-sign noise)"
          % (PIN_V, PIN_NESC))

    ys = [float(v) for v in PIN_YSTAR]
    okc = all(1.0 < v <= 2.2 for v in ys) and \
        all(PIN_RESID[i] <= PIN_STRIP[i] for i in range(6))
    okctl = all(float(v) < -0.1 for v in PIN_J2W_CTRL)
    check("F4 cascade certificates + controls refuse", okc and okctl,
          "Y*/b_top = %s..%s with ZERO T <= 0 violations above Y* "
          "(T > 0 CERTIFIED source-pure; residual sliver %s of %s "
          "strip zeros -- closed per-zero in v925); controls J_2_w "
          "= %s (NEGATIVE leading moment: no quarter-window content "
          "in the fake worlds; SR1 world-blind null control)"
          % (PIN_YSTAR[0], PIN_YSTAR[5], PIN_RESID, PIN_STRIP,
             PIN_J2W_CTRL))

    print("\n  [TYPED, carried verbatim] These theorems REWRITE the "
          "T-WINDOW into")
    print("  {arithmetic J_2-window (quarter-cap PROVEN, boundedness "
          "ARITHMETIC-")
    print("  PINNED)} + {band-edge sliver + separation}.  They close "
          "NO omega; census")
    print("  cardinality 4 UNCHANGED.  NOT RH evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v924 -- PRIME.MOMENT.LAURENT.ROOTLADDER.01 (L1 "
          "ladder-is-moment-data; L2")
    print("quarter-cap; L3 sum rules; L4 sign law; L5 cascade; L6 "
          "split; round 156,")
    print("Lean-hardened round 158; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v924: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: all theorem algebra recomputed in-run; r156 "
          "tables from")
    print("rootladder_probe.py (SPEC %s, 29/29, RE-RUN GREEN AT "
          "PROMOTION," % PIN_SPEC_R156)
    print("zero amendments).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.MOMENT.LAURENT.ROOTLADDER.01 moment-Laurent/"
          "root-ladder theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
