#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""woodbury_minf_probe -- PRIME.RDAGGER.WOODBURY_MINF.01 (r486).

The unused idea for lambda_*(0.3): represent the DANGEROUS
part, not the safe complement.  Q_W = A + Pi is a Fourier
multiplier plus rank one.  Split A = A+ - A- with
A- = |sigma_A| * 1_{|t|<t_c}, t_c ~ 6.2898 the unique zero
of sigma_A.  A- is bounded (||A-|| <= 5.373) and
time-limited-effectively LOW-DIMENSIONAL:
  tr(K_{t_c}) = 2 L t_c / pi ~ 1.201.
Slepian numbers of K_{t_c} drop after n=2
(0.859, 0.314, 0.027, 7.7e-4, ...).  The enemy is
2-3 modes, ALL with large eigenvalues (no garbage).
Birman-Schwinger: A+ + Pi - A- succeq 0 iff
  ||(A++Pi)^{-1/2} A- (A++Pi)^{-1/2}|| <= 1.

ROUTE (b)/(ii) FIRST (mandated).  Float 3-mode enemy
balance is POSITIVE: on n=48/96, T=150,
  BS lmax = 0.99409,  margin 1-lmax = 5.91e-3.
Schur-reducing R = A++Pi against the Nyström rest
does not move the margin (0.99404).  Q on
E={psi_0,psi_1,psi_2} has Higham mu >= 2.87e-3.
r476 Dirichlet midpoint hits (Q=1.178e-2 in
[1.150e-2, 1.192e-2]).  Trace-rest after 012 is
7.81e-4; |sigma(0)|*rest = 4.20e-3.

WHAT THIS DOES NOT CLOSE.  The operator
R^{-1} = (A+ + Pi)^{-1} on L^2[-L,L] is open
(Route (a): invert P_L (sigma_+)(D) P_L, commutator
with P_L).  A+ leftover coupling of E into the
K-complement is still ~0.29, fifty times the Higham
margin -- the same completeness species as r483-r485,
now isolated as a 3-function Woodbury/resolvent.
Not lambda_*(0.3) >= c.  Route (a) is not opened:
(b) did not fail structurally; it reduced the
statement.

ANTI-LIST: Fourier-HS, crude kappa_high, Fourier ONB,
sigma^2 Plancherel, IBP envelope, exp-sum Ci, n=48
leftover as SATZ pad, 20x drop, QR-sinc-IBP, FLAT
c_tail as M_inf, constant minorant sigma(0)K+Pi
(indefinite, r479), garbage modes of K_8, T=400
quadrature (e^{itx} outruns Gauss; Dirichlet Q
jumps to 7).

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
from scipy.linalg import eigh

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

L_YB = 0.3
TC = 6.289835988836903
SIG0 = -5.372183419225666
T_CUT = 150.0
PI = math.pi

T_C_LO_PIN = "6.289835988836902"
TR_LO_PIN = "1.201270186632830"
LAM0_PIN = "0.859391"
LAM1_PIN = "0.313778"
LAM2_PIN = "0.027320"
REST012_PIN = "7.81e-4"
QDIR_LO_PIN = "1.150e-02"
QDIR_HI_PIN = "1.192e-02"
QE_LO_PIN = "6.6e-03"
HIGHAM_PIN = "2.8e-3"
BS_HI_PIN = "0.995"
BS_MARGIN_PIN = "5.8e-3"

VERDICT_KIND = (
    "REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)"
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


def q_split(x, wts, funcs, m, t_cut, nt):
    a_neg = KH.a_matrix(x, wts, funcs, 0.0, TC, m, 2000)
    a_plus = KH.a_matrix(x, wts, funcs, TC, t_cut, m, nt)
    pim = KH.pi_matrix(x, wts, funcs, m)
    aminus = -a_neg
    rmat = a_plus + pim
    qmat = a_plus + a_neg + pim
    return aminus, rmat, qmat


def dirichlet_q(x, wts, t_cut):
    cdir = np.cos(PI * x / (2 * L_YB))
    cdir = cdir / math.sqrt(float(np.sum(wts * cdir * cdir)))
    ts = np.linspace(0.0, t_cut, 2000)
    sig = KH.sigma_arr(ts)
    hv = KH.hat_grid(x, wts, cdir, ts)
    qa = float(np.trapezoid(sig * np.abs(hv) ** 2, ts).real) / PI
    ov = float(np.sum(wts * cdir * np.cosh(0.5 * x)))
    return qa + 2.0 * ov * ov


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("woodbury_minf_probe -- r486")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")
    print("route", "b/ii first (enemy representation)")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n (vacuous at 0.3)")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")
    check("only-L03", True, "this round is L=0.3 only")
    check("type-reduced",
          VERDICT_KIND.startswith("REDUCED")
          and "enemy-3dim" in VERDICT_KIND
          and "operator-Rinv-open" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "constant minorant" in (__doc__ or "")
          and "garbage modes of K_8" in (__doc__ or "")
          and "T=400" in (__doc__ or ""),
          "minorant/garbage/T400 not reused")
    check("route-b-first",
          "ROUTE (b)/(ii) FIRST" in (__doc__ or ""),
          "enemy representation before commutator")

    ev, x, wts, funcs = KH.nystrom_modes(L_YB, TC, 48)
    tr = 2.0 * L_YB * TC / PI
    rest012 = tr - float(np.sum(ev[:3]))
    print("  lambda", " ".join("%.6f" % v for v in ev[:5]))
    print("  tr=%.15f  rest012=%.6e" % (tr, rest012))
    check("t-c-pin",
          abs(TC - float(T_C_LO_PIN)) < 2e-15,
          "t_c from r479")
    check("trace-pin",
          tr >= float(TR_LO_PIN) - 2e-15,
          "tr(K)=2L t_c/pi")
    check("enemy-spectrum",
          abs(ev[0] - float(LAM0_PIN)) < 5e-7
          and abs(ev[1] - float(LAM1_PIN)) < 5e-7
          and abs(ev[2] - float(LAM2_PIN)) < 5e-7
          and ev[0] > 0.8 and ev[1] > 0.3 and ev[2] > 0.02,
          "certified large eigenvalues, no garbage")
    check("trace-rest",
          abs(rest012 - float(REST012_PIN)) < 5e-6,
          "|sig0|*rest=%.4e" % (abs(SIG0) * rest012))

    aminus, rmat, qmat = q_split(x, wts, funcs, 8, T_CUT, 2500)
    e012 = [0, 1, 2]
    qe = qmat[np.ix_(e012, e012)]
    re = rmat[np.ix_(e012, e012)]
    ae = aminus[np.ix_(e012, e012)]
    lmin_qe = float(np.min(np.linalg.eigvalsh(qe)))
    bs = eigh(ae, re, eigvals_only=True)
    bs_lmax = float(bs[-1])
    print("  lmin Q_E012=%.6e  BS lmax=%.6f  1-lmax=%.4e"
          % (lmin_qe, bs_lmax, 1.0 - bs_lmax))
    check("qe-pd",
          lmin_qe > float(QE_LO_PIN),
          "float 3x3 enemy Q PD")
    check("bs-below-one",
          bs_lmax < float(BS_HI_PIN)
          and (1.0 - bs_lmax) > float(BS_MARGIN_PIN),
          "Birman-Schwinger < 1 with margin")

    qdir = dirichlet_q(x, wts, T_CUT)
    print("  Dirichlet Q=%.6e  r476 in [%.4e, %.4e]"
          % (qdir, float(QDIR_LO_PIN), float(QDIR_HI_PIN)))
    check("r476-midpoint",
          float(QDIR_LO_PIN) <= qdir <= float(QDIR_HI_PIN),
          "first Dirichlet hits r476")

    mu = CC.validated_lammin(qe, np.full(qe.shape, 2e-4), lmin_qe)
    print("  Higham Q_E012 mu=%s" % mu)
    check("higham-qe",
          mu is not None and mu > float(HIGHAM_PIN),
          "finite enemy Q interval-PD")

    # leftover A- after 3 modes
    rest = list(range(3, 8))
    cneg = aminus[np.ix_(e012, rest)]
    cneg_op = float(np.linalg.svd(cneg, compute_uv=False)[0])
    print("  ||A-_E,rest||=%.4e  budget |sig0|*rest=%.4e"
          % (cneg_op, abs(SIG0) * rest012))
    check("a-minus-leftover",
          cneg_op < 0.01,
          "enemy captured by 3 modes")

    if not smoke:
        ev96, x96, w96, f96 = KH.nystrom_modes(L_YB, TC, 96)
        dtop = max(abs(ev[k] - ev96[k]) for k in range(5))
        print("  n48 vs n96 dtop5=%.3e" % dtop)
        check("nystrom-stable",
              dtop < 1e-12,
              "Slepian numbers of K_tc stable")
        _am, r96, q96 = q_split(x96, w96, f96, 12, T_CUT, 2500)
        qe96 = q96[np.ix_(e012, e012)]
        check("n96-qe",
              abs(float(np.min(np.linalg.eigvalsh(qe96))) - lmin_qe) < 5e-6,
              "Q_E n-stable")
        am16, r16, q16 = q_split(x, wts, funcs, 16, T_CUT, 2500)
        bs16 = eigh(am16, r16, eigvals_only=True)
        print("  BS_full16 lmax=%.6f" % bs16[-1])
        check("bs-full",
              bs16[-1] < float(BS_HI_PIN),
              "16-mode BS still < 1")
        # Schur-reduced R
        eidx, ridx = e012, list(range(3, 16))
        s_r = (r16[np.ix_(eidx, eidx)]
               - r16[np.ix_(eidx, ridx)]
               @ np.linalg.inv(r16[np.ix_(ridx, ridx)])
               @ r16[np.ix_(eidx, ridx)].T)
        bs_s = eigh(am16[np.ix_(eidx, eidx)], s_r, eigvals_only=True)
        print("  BS_Schur lmax=%.6f  S_R lmin=%.4e"
              % (bs_s[-1], np.min(np.linalg.eigvalsh(s_r))))
        check("bs-schur",
              bs_s[-1] < float(BS_HI_PIN)
              and np.min(np.linalg.eigvalsh(s_r)) > 0.3,
              "worst v_perp does not kill the margin")
        # odd easy
        odd = [1, 3]
        check("odd-easy",
              float(np.min(np.linalg.eigvalsh(q16[np.ix_(odd, odd)]))) > 0.2,
              "odd enemy Q easy")
        check("not-proved-lambda",
              True,
              "operator R^{-1} on L2 open")
        check("no-route-a",
              "Route (a) is not opened" in (__doc__ or ""),
              "(b) reduced, commutator not required this round")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN rest012=%.8e Q_E=%.8e BS=%.8f Qdir=%.8e"
          % (rest012, lmin_qe, bs_lmax, qdir))
    print("PIN_DUMP_END")
    if n_fail:
        print("WOODBURY_MINF FAILED")
        return 1
    print("WOODBURY_MINF %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
