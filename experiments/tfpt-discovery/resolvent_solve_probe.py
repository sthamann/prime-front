#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""resolvent_solve_probe -- PRIME.RDAGGER.RESOLVENT_SOLVE.01 (r488).

Route (a) of r486: certified R^{-1} on the enemy modes.
R = A+ + Pi is NOT coercive on L2[-L,L]: lambda_min(R) on
the Nyström space collapses with n (0.336 at n=48/m=16,
0.106 at n=96/m=20, 0.076 at n=128/m=16).  A+ vanishes
on |t|<t_c; Pi lifts only one direction.  Shift is
mandatory: R_s = R + s, A-_s = A- + s, s=0.05.
Coercivity constant of R_s is s (A++Pi succeq 0).

Birman-Schwinger is shift-invariant as an operator
inequality (Q succeq 0 iff BS<=1 for every s).  The
shift only converts residual to inverse error:
  ||R_s u - phi|| <= r  =>  ||u - R_s^{-1} phi|| <= r/s.

s=0 recovers r486: BSE012 = 0.993651.
s=0.05, correct G-certificate
  lambda_max(G^{1/2} B G^{1/2}), G = P_E R_s^{-1} P_E,
  B = A-|_E + s I:
  N=3: 0.99433;  N=5: 0.99439.  Residual in V_n ~ 1e-17.
N=3 plus the crude |sig0|*rest/s budget OVERSHOOTS
(1.078 at s=0.05) -- not a SATZ pad.  N=5 tail is
5.5e-7, budget/s negligible, GBG+tail < 1 with margin
5.6e-3 on the Nyström space.

WHAT THIS DOES NOT CLOSE.  Discrete G is the inverse
of the T=150 Galerkin R, not of the operator R on L2.
The A+ Filon/complement gap (same leftover species as
r483-r485) is open.  eig(B@G) without the symmetric
product is not the BS number (it reads 1.023 and is
anti-listed).  Not lambda_*(0.3) >= c.

ANTI-LIST: Fourier-HS, crude kappa_high, Fourier ONB,
sigma^2 Plancherel, IBP envelope, exp-sum Ci, n=48
leftover, 20x drop, QR-sinc-IBP, flat c_tail as M_inf,
constant minorant, K_8 garbage, T=400 quadrature,
3-mode+|sig0|*rest/s as SATZ pad, eig(BG) as BS.

r469 contract.  L=0.3 only.  P empty.  SCRAMBLE GATE:
literal log n, vacuous.  NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.abspath(os.path.dirname(__file__))
CANDIDATES = [
    HERE,
    os.path.join(HERE, "..", "..", "experiments", "tfpt-discovery"),
    "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery",
]
for path in CANDIDATES:
    path = os.path.abspath(path)
    if os.path.isfile(os.path.join(path, "classical_cert_probe.py")):
        if path not in sys.path:
            sys.path.insert(0, path)
        break

import classical_cert_probe as CC  # noqa: E402
import kappa_high_probe as KH  # noqa: E402
import woodbury_minf_probe as W486  # noqa: E402

L_YB = 0.3
TC = 6.289835988836903
SIG0 = -5.372183419225666
T_CUT = 150.0
S_SHIFT = 0.05
PI = math.pi

R486_BSE_PIN = "0.993651"
LMINR48_PIN = "0.33"
LMINR96_PIN = "0.11"
GBG3_PIN = "0.9943"
GBG5_PIN = "0.9944"
N3_BUDGET_OVER_PIN = "1.07"
HIGHAM5_PIN = "2.3e-3"
RES_PIN = "1e-14"

VERDICT_KIND = (
    "REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; "
    "operator-R-gap-open)"
)
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "P uses literal log n on nodes log n <= 2L.  At L=0.3 "
    "the node set is empty (P=0); scrambling is vacuous here "
    "and becomes live at L=0.8.  Not fold-mode pairing."
)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in forbidden:
            bad.append(node.id)
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            bad.append(node.attr)
    return (not bad), (",".join(sorted(set(bad))) if bad else "")


def split_ar(x, wts, funcs, m, t_cut=T_CUT, nt=2500):
    a_neg = KH.a_matrix(x, wts, funcs, 0.0, TC, m, 2000)
    a_plus = KH.a_matrix(x, wts, funcs, TC, t_cut, m, nt)
    pim = KH.pi_matrix(x, wts, funcs, m)
    return -a_neg, a_plus + pim


def gbg_max(bmat, gmat):
    ev, u = np.linalg.eigh(gmat)
    gh = u @ np.diag(np.sqrt(np.maximum(ev, 0.0))) @ u.T
    return float(np.max(np.linalg.eigvalsh(gh @ bmat @ gh)))


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("resolvent_solve_probe -- r488")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")
    print("shift s=%.3f (coercivity first)" % S_SHIFT)

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n (vacuous at 0.3)")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")
    check("only-L03", True, "this round is L=0.3 only")
    check("type-reduced",
          VERDICT_KIND.startswith("REDUCED")
          and "R-not-coercive" in VERDICT_KIND
          and "operator-R-gap-open" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "3-mode+|sig0|*rest/s" in (__doc__ or "")
          and "eig(BG)" in (__doc__ or ""),
          "false SATZ pads listed")
    check("r486-reduced",
          W486.VERDICT_KIND.startswith("REDUCED")
          and "operator-Rinv-open" in W486.VERDICT_KIND,
          "r486 isolated the resolvent")

    ev48, x48, w48, f48 = KH.nystrom_modes(L_YB, TC, 48)
    am8, r8 = split_ar(x48, w48, f48, 8)
    lmin_r48 = float(np.min(np.linalg.eigvalsh(r8)))
    print("  FIRST  lmin(R) n=48 m=8 = %.6e" % lmin_r48)
    check("lminR-48",
          lmin_r48 > float(LMINR48_PIN),
          "finite-n R still PD")

    # s=0 midpoint = r486
    e3 = [0, 1, 2]
    from scipy.linalg import eigh
    w0 = eigh(am8[np.ix_(e3, e3)], r8[np.ix_(e3, e3)], eigvals_only=True)
    print("  s=0 BSE012=%.6f  r486 pin %s" % (w0[-1], R486_BSE_PIN))
    check("r486-midpoint",
          abs(w0[-1] - float(R486_BSE_PIN)) < 5e-6,
          "s->0 recovers r486")

    rs = r8 + S_SHIFT * np.eye(8)
    ams = am8 + S_SHIFT * np.eye(8)
    g3 = np.linalg.inv(rs)[np.ix_(e3, e3)]
    b3 = ams[np.ix_(e3, e3)]
    gbg3 = gbg_max(b3, g3)
    print("  s=%.3f GBG N=3 = %.6f  margin=%.4e"
          % (S_SHIFT, gbg3, 1.0 - gbg3))
    check("gbg3",
          abs(gbg3 - float(GBG3_PIN)) < 5e-4 and gbg3 < 1.0,
          "3-mode G-certificate < 1")

    tr = 2.0 * L_YB * TC / PI
    bud3 = abs(SIG0) * (tr - float(np.sum(ev48[:3])))
    print("  N=3 |sig0|*rest/s + GBG = %.6f (OVERSHOOT)"
          % (gbg3 + bud3 / S_SHIFT))
    check("n3-budget-kills",
          gbg3 + bud3 / S_SHIFT > float(N3_BUDGET_OVER_PIN),
          "3-mode+crude-tail is not a SATZ")

    # residual of the 3 solves in V_8
    rinv = np.linalg.inv(rs)
    res_max = 0.0
    for i in e3:
        phi = np.zeros(8)
        phi[i] = 1.0
        u = rinv @ phi
        res_max = max(res_max, float(np.linalg.norm(rs @ u - phi)))
    print("  residual V_8 = %.3e  bound r/s = %.3e"
          % (res_max, res_max / S_SHIFT))
    check("residual",
          res_max < float(RES_PIN),
          "discrete solve exact to 1e-14")

    if not smoke:
        ev96, x96, w96, f96 = KH.nystrom_modes(L_YB, TC, 96)
        am20, r20 = split_ar(x96, w96, f96, 20)
        lmin_r96 = float(np.min(np.linalg.eigvalsh(r20)))
        print("  lmin(R) n=96 m=20 = %.6e" % lmin_r96)
        check("r-not-coercive",
              lmin_r96 < float(LMINR96_PIN)
              and lmin_r96 < lmin_r48,
              "lambda_min(R) collapses with n; shift required")

        rs20 = r20 + S_SHIFT * np.eye(20)
        ams20 = am20 + S_SHIFT * np.eye(20)
        e5 = list(range(5))
        g5 = np.linalg.inv(rs20)[np.ix_(e5, e5)]
        b5 = ams20[np.ix_(e5, e5)]
        gbg5 = gbg_max(b5, g5)
        bud5 = abs(SIG0) * (tr - float(np.sum(ev96[:5])))
        print("  s=%.3f GBG N=5 = %.6f  +bud/s=%.6f  margin=%.4e"
              % (S_SHIFT, gbg5, gbg5 + bud5 / S_SHIFT, 1.0 - gbg5))
        check("gbg5",
              abs(gbg5 - float(GBG5_PIN)) < 5e-4
              and gbg5 + bud5 / S_SHIFT < 1.0,
              "5-mode G-certificate + tail < 1")

        q5 = (r20 - am20)[np.ix_(e5, e5)]
        mu = CC.validated_lammin(
            q5, np.full(q5.shape, 2e-4),
            float(np.min(np.linalg.eigvalsh(q5))))
        print("  Higham Q_5 mu=%s" % mu)
        check("higham-q5",
              mu is not None and mu > float(HIGHAM5_PIN),
              "finite 5-mode Q interval-PD")

        # n=128 collapse
        _ev128, x128, w128, f128 = KH.nystrom_modes(L_YB, TC, 128)
        _am16, r16 = split_ar(x128, w128, f128, 16)
        lmin_r128 = float(np.min(np.linalg.eigvalsh(r16)))
        print("  lmin(R) n=128 m=16 = %.6e" % lmin_r128)
        check("r-collapse-128",
              lmin_r128 < lmin_r96,
              "continues toward 0")
        check("not-proved-lambda",
              True,
              "operator R vs Galerkin R gap open")
        check("no-eigBG",
              "eig(BG)" in (__doc__ or ""),
              "asymmetric product is not the BS number")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN lminR48=%.8e s0=%.8f GBG3=%.8f res=%.3e"
          % (lmin_r48, w0[-1], gbg3, res_max))
    print("PIN_DUMP_END")
    if n_fail:
        print("RESOLVENT_SOLVE FAILED")
        return 1
    print("RESOLVENT_SOLVE %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
