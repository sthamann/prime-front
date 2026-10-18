#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weighted_schur_probe -- PRIME.RDAGGER.WEIGHTED_SCHUR.01 (r485).

Last keystone before the 0.3 checkpoint.  r479-r484 used the
FLAT tail floor c_tail = sigma_A(8) ~ 0.2409.  sigma_A grows
like log(t/2pi).  The leftover coupling (op-norm 0.294) pairs
the certified block with the orthocomplement; that complement
has a FREQUENCY-WEIGHTED A-reserve.  The reviewer path-B test
is ||M_inf^{-1/2} C M_00^{-1/2}|| <= 1, i.e. the Schur subtract
C D^{-1} C^T with D = A|_complement, not C C^T / c_tail.

A-FIRST (GO/NO-GO).  On n=96, leftover C of
{psi_0..psi_8} into {psi_10..psi_22}:
  [0,8]   F = 2.74e-10   (epsilon control: almost no band mass)
  [8,20]  F = 4.71e-4
  [20,50] F = 1.68e-1
  [50,150] F = 3.30e-1
  [150,400] F = 4.23e-1
hi-frac [30,150] vs [8,30] = 0.991.  GO: mass is at large t.
Top complement singular vector has Q_A[0,150]/c_tail = 4.49
and hat-energy concentrated on [50,400].

FINITE WEIGHTED SCHUR.  S_w = B - C D^{-1} C^T on the
n=96 even compression.  At T=150:
  S_flat = 5.18e-3,  S_w = 6.38e-3,  Higham mu >= 2.59e-3.
  BUT dmin(D) = 0.152 < c_tail  (missing high-t mass of D).
At T=400: dmin(D) = 1.49, S_w = 7.23e-3, Higham mu >= 3.01e-3.
Odd S_w = 0.221.  n=48 S_flat hits r483 (5.686e-3).

WHAT THIS DOES NOT CLOSE.  Discrete D is a COMPRESSION of
A|_complement, not the operator.  A higher floor sigma(t1)
does not follow from epsilon of K_8 (that only kills [0,8]).
L2 complement of the Nyström space is the same leftover
species as r483/r484.  Not lambda_*(0.3) >= c.

CHECKPOINT.  This is the last structurally new 0.3 idea
(block-extension fell twice).  The note carries the
r479-r485 keystone balance and the standalone problem
statement for the open coupling.

ANTI-LIST: Fourier-HS, crude kappa_high, Fourier ONB,
sigma^2 Plancherel, IBP envelope, exp-sum Ci, n=48 leftover
as SATZ pad, 20x drop, QR-sinc-IBP, FLAT c_tail as if it
were M_inf.

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
import filon_enclosure_probe as F483  # noqa: E402
import kappa_high_probe as KH  # noqa: E402

L_YB = 0.3
TSTAR = 8.0
T_CUT = 150.0
SIG0 = -5.372183419225666
PI = math.pi

R483_EVEN_PIN = "5.685657e-03"
HI_FRAC_PIN = "0.99"
C08_PIN = "3.0e-09"
SW150_PIN = "6.3e-03"
HIGHAM150_PIN = "2.5e-3"
DMIN150_PIN = "0.15"
DMIN400_PIN = "1.49"

VERDICT_KIND = (
    "REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT"
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


def band_c(x, w, funcs, block, rest, t0, t1, nt):
    amat = KH.a_matrix(x, w, funcs, t0, t1, max(block + rest) + 1, nt)
    return amat[np.ix_(block, rest)]


def schur_pair(qmat, block, rest, c_tail):
    bmat = qmat[np.ix_(block, block)]
    cmat = qmat[np.ix_(block, rest)]
    dmat = qmat[np.ix_(rest, rest)]
    evd = np.linalg.eigvalsh(dmat)
    sflat = bmat - cmat @ cmat.T / c_tail
    sw = bmat - cmat @ np.linalg.inv(dmat) @ cmat.T
    return {
        "dmin": float(evd[0]),
        "dmax": float(evd[-1]),
        "cop": float(np.linalg.svd(cmat, compute_uv=False)[0]),
        "lflat": float(np.min(np.linalg.eigvalsh(sflat))),
        "lw": float(np.min(np.linalg.eigvalsh(sw))),
        "sw": sw,
    }


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("weighted_schur_probe -- r485")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n (vacuous at 0.3)")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")
    check("only-L03", True, "this round is L=0.3 only")
    check("type-reduced",
          VERDICT_KIND.startswith("REDUCED")
          and "CHECKPOINT" in VERDICT_KIND
          and "A-GO" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "FLAT c_tail as if it" in (__doc__ or "")
          and "20x drop" in (__doc__ or ""),
          "flat floor not treated as M_inf")
    check("r484-stuck",
          "STUCK" in __import__("block_completion_probe",
                                fromlist=["VERDICT_KIND"]).VERDICT_KIND,
          "block-extension already STUCK")

    rec = KH.measure(TSTAR, 5, n_ny=48, m_modes=12, t_cut=T_CUT, nt=2500)
    print("  r483-style even lminS=%.6e" % rec["even"][2])
    check("r483-midpoint",
          abs(rec["even"][2] - float(R483_EVEN_PIN)) < 5e-6,
          "flat Schur hits r483")

    ev, x, w, funcs = KH.nystrom_modes(L_YB, TSTAR, 96)
    block5 = [0, 2, 4, 6, 8]
    rest5 = list(range(10, 24, 2))
    c08 = band_c(x, w, funcs, block5, rest5, 0.0, 8.0, 400)
    c_lo = band_c(x, w, funcs, block5, rest5, 8.0, 30.0, 800)
    c_hi = band_c(x, w, funcs, block5, rest5, 30.0, 150.0, 1200)
    f08 = float(np.linalg.norm(c08, "fro"))
    f_lo = float(np.linalg.norm(c_lo, "fro"))
    f_hi = float(np.linalg.norm(c_hi, "fro"))
    hi_frac = (f_hi ** 2) / (f_lo ** 2 + f_hi ** 2 + 1e-30)
    print("  A-FIRST  C[0,8]=%.3e  [8,30]=%.4e  [30,150]=%.4e  hi-frac=%.4f"
          % (f08, f_lo, f_hi, hi_frac))
    check("eps-edge",
          f08 < float(C08_PIN),
          "complement has no band mass on [0,8]")
    check("a-go",
          hi_frac > float(HI_FRAC_PIN),
          "hi-frac=%.3f GO" % hi_frac)
    check("not-near-tstar",
          f_lo < 0.05,
          "[8,30] is not the leftover mass")

    sig8 = float(KH.sigma_arr(np.array([TSTAR]))[0])
    ct = sig8 * (1.0 - float(ev[6])) + SIG0 * float(ev[6])
    a150 = KH.a_matrix(x, w, funcs, 0.0, T_CUT, 24, 2500)
    q150 = a150 + KH.pi_matrix(x, w, funcs, 24)
    recw = schur_pair(q150, [0, 2, 4], list(range(6, 24, 2)), ct)
    print("  T=150 S_flat=%.5e S_w=%.5e dmin=%.4f ||C||=%.4f"
          % (recw["lflat"], recw["lw"], recw["dmin"], recw["cop"]))
    check("sw-beats-flat",
          recw["lw"] > recw["lflat"],
          "weighted subtract is smaller")
    check("sw-pd",
          recw["lw"] > float(SW150_PIN),
          "finite S_w PD")
    check("dmin-undershoot",
          recw["dmin"] < ct,
          "D at T=150 undershoots c_tail (edge bookkeeping)")

    mu = CC.validated_lammin(recw["sw"],
                             np.full(recw["sw"].shape, 2e-4),
                             recw["lw"])
    print("  Higham T=150 mu=%s" % mu)
    check("higham-sw",
          mu is not None and mu > float(HIGHAM150_PIN),
          "finite S_w interval-PD")

    if not smoke:
        a400 = KH.a_matrix(x, w, funcs, 0.0, 400.0, 24, 3500)
        q400 = a400 + KH.pi_matrix(x, w, funcs, 24)
        rec4 = schur_pair(q400, [0, 2, 4], list(range(6, 24, 2)), ct)
        print("  T=400 S_flat=%.5e S_w=%.5e dmin=%.4f"
              % (rec4["lflat"], rec4["lw"], rec4["dmin"]))
        check("dmin-400",
              rec4["dmin"] > float(DMIN400_PIN) * 0.9,
              "high-t mass lifts dmin(D) above c_tail")
        mu4 = CC.validated_lammin(rec4["sw"],
                                  np.full(rec4["sw"].shape, 2e-4),
                                  rec4["lw"])
        check("higham-400",
              mu4 is not None and mu4 > 2.5e-3,
              "S_w PD at T=400")

        # odd
        ro = schur_pair(q150, [1, 3, 5], list(range(7, 24, 2)), ct)
        print("  odd T=150 S_w=%.5e dmin=%.4f" % (ro["lw"], ro["dmin"]))
        check("odd-sw", ro["lw"] > 0.15, "odd weighted Schur easy")

        # ratio on top SV
        cfull = q150[np.ix_(block5, rest5)]
        _u, svals, vt = np.linalg.svd(cfull, full_matrices=False)
        coef = vt[0]
        samp = np.zeros_like(funcs[0])
        for a, k in enumerate(rest5):
            samp = samp + coef[a] * funcs[k]
        samp = samp / math.sqrt(max(float(np.sum(w * samp * samp)), 1e-30))
        ts = np.linspace(0.0, T_CUT, 2000)
        sig = KH.sigma_arr(ts)
        hv = KH.hat_grid(x, w, samp, ts)
        qa = float(np.trapezoid(sig * np.abs(hv) ** 2, ts).real) / PI
        print("  top-SV Q_A[0,150]=%.3f  /c_tail=%.2f  s=%.4f"
              % (qa, qa / ct, svals[0]))
        check("top-sv-reserve",
              qa / ct > 3.0,
              "complement reserve is a sigma factor ~4")
        check("not-proved-lambda",
              True,
              "operator M_inf on L2 complement open")
        check("checkpoint",
              "CHECKPOINT" in VERDICT_KIND,
              "last structurally new 0.3 idea")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN hi_frac=%.6f C08=%.6e S_w=%.8e dmin=%.6f"
          % (hi_frac, f08, recw["lw"], recw["dmin"]))
    print("  PIN even_lminS_flat=%.8e" % rec["even"][2])
    print("PIN_DUMP_END")
    if n_fail:
        print("WEIGHTED_SCHUR FAILED")
        return 1
    print("WEIGHTED_SCHUR %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
