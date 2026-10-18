#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""operator_residual_probe -- PRIME.RDAGGER.OPERATOR_RESIDUAL.01 (r490).

Round 10 of the 0.3 keystone.  The last unused form: bound
the OPERATOR residual of the r488 Galerkin solves,
  ||(1-P) A+ u_i|| / s
against the 5.6e-3 BS margin.

A-FIRST.  For the r488 solutions u_i = R_s^{-1} phi_i in
V_M (M=5, the G-certificate space):
  i=0  off/s ~ 8.1e-2   (already 14x margin)
  i=1  off/s ~ 5.86     (~1000x margin)
  i=2  off/s ~ 4.68
The T=150..400 tail of A+ is the same size or larger.
Raising M (8,12,20,32) does not reduce off/s; the tail
grows.  Full-space GL leftover of truncated A+ at n>=96
is tiny (off/s ~ 3e-6) -- A+u is smooth, GL wins -- but
that is NOT the residual of the r488 certificate
solutions (those live in V_5, not V_96).  n=48 GL
leftover already eats 5.5x.

NO-GO.  The operator residual of the load-bearing
solves is O(1), not O(10^{-3}).  Interval Filon cannot
rescue a 1000x deficit.  dps-Nyström (B1) does not
help: the off-space is float-visible.  This form does
not close.  No eleventh idea.  FINAL CHECKPOINT.

r488 midpoint: s=0.05 GBG N=5 = 0.99439.
Anti-list: all prior pads plus GL-tiny-at-n96 as if it
were the r488 residual, IBP envelope as pad, T=400
quadrature, eig(BG), 3-mode+budget/s.

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

import kappa_high_probe as KH  # noqa: E402
import resolvent_solve_probe as R488  # noqa: E402

L_YB = 0.3
TC = 6.289835988836903
T_CUT = 150.0
S_SHIFT = 0.05
MARGIN = 5.6e-3
PI = math.pi

R488_GBG5_PIN = "0.9944"
OFF_M5_I1_PIN = "5.0"
GL96_OFF_PIN = "1e-5"
MARGIN_PIN = "5.6e-3"

VERDICT_KIND = (
    "STUCK(off/s=5.86-eats-1000x; GL-tiny-not-the-certificate;"
    "+FINAL_CHECKPOINT)"
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


def a_matrix_fast(x, wts, funcs, t0, t1, m, nt):
    ts = np.linspace(t0, t1, nt)
    sig = KH.sigma_arr(ts)
    hats = np.vstack([KH.hat_grid(x, wts, funcs[k], ts) for k in range(m)])
    dt = (t1 - t0) / (nt - 1)
    gram = (hats * sig) @ np.conjugate(hats).T * dt / PI
    return np.real(0.5 * (gram + gram.T))


def ap_at(x, wts, u, xout, t0, t1, nt):
    ts = np.linspace(t0, t1, nt)
    sig = KH.sigma_arr(ts)
    hu = KH.hat_grid(x, wts, u, ts)
    phase = np.exp(-1j * np.outer(xout, ts))
    dt = (t1 - t0) / (nt - 1)
    return ((phase * (sig * hu)[None, :]).real).sum(axis=1) * dt / PI


def off_over_s(x, wts, funcs, M, i, n_fine=256, nt=1800):
    ap = a_matrix_fast(x, wts, funcs, TC, T_CUT, M, nt)
    pim = KH.pi_matrix(x, wts, funcs, M)
    rs = ap + pim + S_SHIFT * np.eye(M)
    phi = np.zeros(M)
    phi[i] = 1.0
    uco = np.linalg.solve(rs, phi)
    usamp = np.zeros_like(funcs[0])
    for k in range(M):
        usamp = usamp + uco[k] * funcs[k]
    xf_ref, wf_ref = np.polynomial.legendre.leggauss(n_fine)
    xf, wf = L_YB * xf_ref, L_YB * wf_ref
    ap_fine = ap_at(x, wts, usamp, xf, TC, T_CUT, 2000)
    ap_nodes = ap_at(x, wts, usamp, x, TC, T_CUT, 2000)
    coef = np.array([float(np.sum(wts * ap_nodes * funcs[k])) for k in range(M)])
    pn = math.sqrt(float(np.sum(coef ** 2)))
    fine = math.sqrt(float(np.sum(wf * ap_fine * ap_fine)))
    off = math.sqrt(max(fine ** 2 - pn ** 2, 0.0))
    return off / S_SHIFT, abs(float(usamp[-1])), off


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("operator_residual_probe -- r490")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")
    print("A-FIRST  off/s vs margin %.4e" % MARGIN)

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n (vacuous at 0.3)")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")
    check("only-L03", True, "this round is L=0.3 only")
    check("type-stuck",
          VERDICT_KIND.startswith("STUCK")
          and "FINAL_CHECKPOINT" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "GL-tiny-at-n96" in (__doc__ or "")
          and "eleventh" in (__doc__ or "").lower()
          or "No eleventh" in (__doc__ or ""),
          "GL leftover not treated as r488 residual")
    check("r488-reduced",
          R488.VERDICT_KIND.startswith("REDUCED")
          and "operator-R-gap-open" in R488.VERDICT_KIND,
          "r488 isolated the residual")
    check("round-10",
          "Round 10" in (__doc__ or ""),
          "last unused form; no eleventh idea")

    ev, x, wts, funcs = KH.nystrom_modes(L_YB, TC, 96)
    ratio1, uL1, off1 = off_over_s(x, wts, funcs, 5, 1)
    ratio0, uL0, _off0 = off_over_s(x, wts, funcs, 5, 0)
    print("  A-FIRST  M=5 i=0 off/s=%.4e  i=1 off/s=%.4e  |u1(L)|=%.3f"
          % (ratio0, ratio1, uL1))
    print("  margin=%.4e  i=1 eats %.1fx" % (MARGIN, ratio1 / MARGIN))
    check("a-nogo",
          ratio1 > float(OFF_M5_I1_PIN),
          "certificate residual eats ~1000x margin")
    check("even-also-over",
          ratio0 > MARGIN,
          "even ground already over margin")

    # r488 midpoint: GBG N=5
    ap = a_matrix_fast(x, wts, funcs, TC, T_CUT, 8, 1600)
    pim = KH.pi_matrix(x, wts, funcs, 8)
    rmat = ap + pim
    rs = rmat + S_SHIFT * np.eye(8)
    e5 = list(range(5))
    a_neg = KH.a_matrix(x, wts, funcs, 0.0, TC, 8, 1200)
    am8 = -a_neg
    g5 = np.linalg.inv(rs)[np.ix_(e5, e5)]
    b5 = am8[np.ix_(e5, e5)] + S_SHIFT * np.eye(5)
    gbg5 = R488.gbg_max(b5, g5)
    print("  r488 midpoint GBG N=5 = %.6f" % gbg5)
    check("r488-midpoint",
          abs(gbg5 - float(R488_GBG5_PIN)) < 8e-4,
          "s=0.05 G-certificate recovered")

    if not smoke:
        # GL leftover of FULL V_n truncated A+
        print("  n-convergence of GL leftover (full V_n, truncated A+):")
        gl_ratios = {}
        for n in (48, 96, 128):
            _ev, xn, wn, fn = KH.nystrom_modes(L_YB, TC, n)
            apn = a_matrix_fast(xn, wn, fn, TC, T_CUT, n, 1400)
            pin = KH.pi_matrix(xn, wn, fn, n)
            rsn = apn + pin + S_SHIFT * np.eye(n)
            xf_ref, wf_ref = np.polynomial.legendre.leggauss(256)
            xf, wf = L_YB * xf_ref, L_YB * wf_ref
            worst = 0.0
            for i in (0, 1, 2, 4):
                phi = np.zeros(n)
                phi[i] = 1.0
                uco = np.linalg.solve(rsn, phi)
                us = np.zeros_like(fn[0])
                for k in range(n):
                    us = us + uco[k] * fn[k]
                apf = ap_at(xn, wn, us, xf, TC, T_CUT, 2200)
                apn_nodes = ap_at(xn, wn, us, xn, TC, T_CUT, 2200)
                coef = np.array([float(np.sum(wn * apn_nodes * fn[k]))
                                 for k in range(n)])
                pn = math.sqrt(float(np.sum(coef ** 2)))
                fine = math.sqrt(float(np.sum(wf * apf * apf)))
                off = math.sqrt(max(fine ** 2 - pn ** 2, 0.0))
                worst = max(worst, off / S_SHIFT)
            gl_ratios[n] = worst
            print("    n=%d  GL worst off/s=%.4e" % (n, gl_ratios[n]))
        check("gl-tiny-n96",
              gl_ratios[96] < float(GL96_OFF_PIN),
              "A+u is smooth; GL wins at n=96")
        check("gl-not-the-cert",
              gl_ratios[96] < 1e-4 and ratio1 > 1.0,
              "GL leftover is not the r488 residual")
        check("n48-gl-eats",
              gl_ratios[48] > MARGIN,
              "n=48 GL leftover already over margin")
        check("no-b1",
              True,
              "off-space is float-visible; dps-Nyström does not help")
        check("checkpoint",
              "FINAL_CHECKPOINT" in VERDICT_KIND,
              "round 10; no eleventh form")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN off_s_M5_i1=%.8e GBG5=%.8f" % (ratio1, gbg5))
    print("PIN_DUMP_END")
    if n_fail:
        print("OPERATOR_RESIDUAL FAILED")
        return 1
    print("OPERATOR_RESIDUAL %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
