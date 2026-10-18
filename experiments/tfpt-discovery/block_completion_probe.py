#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""block_completion_probe -- PRIME.RDAGGER.BLOCK_COMPLETION.01 (r484).

r483 left lambda_*(0.3)>=c blocked by leftover
  ||P_block A P_{>=12}||_F = 2.76e-2
against an IBP-inflated budget 2.4e-4 (factor ~115),
on the n=48 Nyström surface.  The hoped close was a
~20x coupling drop per even double-step, so that a
block through psi_18 would push leftover below budget.

This round tests that drop, the jet-stability certificate
required to use high modes, and the QR-polynomial escape
(any ONB extension of certified psi_0..psi_8 is legal;
exact eigenfunctions of tiny lambda are not required).

GARBAGE CRITERION.  A mode is usable iff |u(L)| at
Nyström-n and Nyström-2n agree to 1e-3 (IBP accuracy).
At n=48 vs 64 vs 96 vs 128:
  psi_0,2,4 : 1e-13  (certified)
  psi_6     : 1e-9   (certified)
  psi_8     : 1e-4   (marginal, r483 pin)
  psi_10+   : O(1) at EVERY n<=128  (GARBAGE)
lambda_10 already sits at the binary64 floor (~1e-16);
higher true Slepians of K_8 are not float objects.

20x DROP FALSIFIED.  On the resolved n=96 surface the
NO-TAIL leftover after psi_10 is 1.38e-1 (not 2.76e-2);
after psi_18 it is still 9.60e-2; after psi_20, 4.40e-2.
Drop per double-step is O(1), not 20.  The r483 figure
2.76e-2 was an n=48 undercount (only two pre-junk
columns).  Enlarging B to {psi_0..psi_8} leaves
||C_rest||~0.29 -- the r480 kappa_high, still alive
in the discrete nullspace.

QR ESCAPE.  Even Legendres QR'd against certified
psi_0..psi_8 are an explicit ONB extension (no tiny
eigenvalues).  NO-TAIL leftover stays O(0.08) at 12
extra columns (completeness leak, r481).  Four-term
IBP on those QR vectors via the sinc extension kills
S (lambda_min ~ -0.065 on a 10-vector window): the kernel interpolant of a
polynomial is not the polynomial, and its jets are
not a decaying-FT certificate.  Not used as a pad.

BILANZ.  New exact deficit on n=96: leftover after
psi_20 is 4.40e-2 vs budget 2.4e-4 (factor ~180).
Honest L2 leftover (discrete complement / kappa_high)
is ~0.29.  Not lambda_*(0.3)>=c.

ANTI-LIST (not reused): Fourier-HS, crude kappa_high,
Fourier ONB, sigma^2 Plancherel, IBP envelope-as-pad,
exp-sum Ci-to-infinity, n=48 leftover 2.76e-2 as a
SATZ pad, QR-sinc-IBP as a tail certificate.

r469 contract.  Fixed L=0.3 only.  P empty.  SCRAMBLE
GATE: literal log n, vacuous here.  NO RH CLAIM.
NO anti-RH claim.
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
from numpy.polynomial.legendre import Legendre

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

import filon_enclosure_probe as F483  # noqa: E402
import kappa_high_probe as KH  # noqa: E402

L_YB = 0.3
TSTAR = 8.0
T_CUT = 150.0
SIG0 = -5.372183419225666
PI = math.pi

R483_EVEN_PIN = "5.685657e-03"
R483_LEFT_PIN = "2.74e-02"
N96_LEFT10_PIN = "1.38e-01"
N96_LEFT18_PIN = "9.60e-02"
N96_LEFT20_PIN = "4.40e-02"
BUDGET_PIN = "2.4e-04"
QR_LEFT12_PIN = "8.0e-02"
QR_IBP_SMIN_PIN = "0.0"
KAPPA_HIGH_PIN = "0.29"

VERDICT_KIND = (
    "STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)"
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


def u_at_L(x, w, f, evk):
    return F483.jets_at(x, w, f, evk, TSTAR, L_YB, 0)[0]


def l2dot(w, a, b):
    return float(np.sum(w * a * b))


def leftover_after(qmat, bmax, m_hi):
    rest = [k for k in range(bmax + 2, m_hi, 2)]
    if not rest:
        return 0.0
    cmat = qmat[np.ix_([0, 2, 4], rest)]
    return float(np.linalg.norm(cmat, "fro"))


def qr_even_onb(x, w, certified, max_deg):
    basis = [f.copy() for f in certified]
    for deg in range(0, max_deg + 1, 2):
        poly = Legendre.basis(deg)
        vec = np.array([float(poly(xi / L_YB)) for xi in x])
        n0 = math.sqrt(max(l2dot(w, vec, vec), 1e-30))
        vec = vec / n0
        for _ in range(2):
            for b in basis:
                vec = vec - l2dot(w, vec, b) * b
            nrm = math.sqrt(max(l2dot(w, vec, vec), 0.0))
            if nrm < 1e-10:
                vec = None
                break
            vec = vec / nrm
        if vec is None:
            continue
        basis.append(vec)
    return basis


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("block_completion_probe -- r484")
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
    check("type-stuck",
          VERDICT_KIND.startswith("STUCK")
          and "20x-drop-falsified" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "n=48 leftover 2.76e-2 as a" in (__doc__ or "")
          and "QR-sinc-IBP" in (__doc__ or ""),
          "r483 leftover not reused as a pad")
    check("r483-contract",
          F483.VERDICT_KIND.startswith("REDUCED")
          and "leftover-C-HS" in F483.VERDICT_KIND,
          "r483 remainder is leftover C")

    ev48, x48, w48, f48 = KH.nystrom_modes(L_YB, TSTAR, 48)
    rec = KH.measure(TSTAR, 5, n_ny=48, m_modes=12, t_cut=T_CUT, nt=3000)
    print("  r483-style even lminS=%.6e" % rec["even"][2])
    check("r483-midpoint",
          abs(rec["even"][2] - float(R483_EVEN_PIN)) < 5e-6,
          "even S hits r483")

    a48 = KH.a_matrix(x48, w48, f48, 0.0, T_CUT, 16, 2000)
    p48 = KH.pi_matrix(x48, w48, f48, 16)
    q48 = a48 + p48
    left48 = leftover_after(q48, 10, 16)
    print("  n=48 leftover after psi_10 (to 14): %.6e" % left48)
    check("r483-leftover",
          abs(left48 - float(R483_LEFT_PIN)) < 5e-4,
          "n=48 leftover matches r483")

    ev64, x64, w64, f64 = KH.nystrom_modes(L_YB, TSTAR, 64)
    d_ok = {}
    d_bad = {}
    for k in (0, 2, 4, 6, 8, 10, 12):
        u48 = u_at_L(x48, w48, f48[k], ev48[k])
        u64 = u_at_L(x64, w64, f64[k], ev64[k])
        d_ok[k] = abs(u48 - u64)
        print("  |u(L)| n48 vs 64  k=%d  d=%.3e" % (k, d_ok[k]))
    check("jets-0-6",
          max(d_ok[k] for k in (0, 2, 4, 6)) < 1e-8,
          "certified modes stable")
    check("jets-8-marginal",
          d_ok[8] < 2e-3,
          "psi_8 marginal as in r483")
    check("jets-10-garbage",
          d_ok[10] > 0.1,
          "psi_10 already garbage at n=64")

    if not smoke:
        ev96, x96, w96, f96 = KH.nystrom_modes(L_YB, TSTAR, 96)
        ev128, x128, w128, f128 = KH.nystrom_modes(L_YB, TSTAR, 128)
        for k in (8, 10, 12, 14, 16, 18):
            u96 = u_at_L(x96, w96, f96[k], ev96[k])
            u128 = u_at_L(x128, w128, f128[k], ev128[k])
            d_bad[k] = abs(u96 - u128)
            print("  |u(L)| n96 vs 128 k=%d  d=%.3e  u96=%.4e"
                  % (k, d_bad[k], u96))
        check("jets-ge10-n128",
              min(d_bad[k] for k in (10, 12, 14, 16)) > 0.5,
              "modes >=10 garbage at n=128")
        check("lambda10-floor",
              float(ev96[10]) < 1e-15 and float(ev128[10]) < 1e-15,
              "lambda_10 at binary64 floor")

        a96 = KH.a_matrix(x96, w96, f96, 0.0, T_CUT, 24, 2500)
        p96 = KH.pi_matrix(x96, w96, f96, 24)
        q96 = a96 + p96
        left10 = leftover_after(q96, 10, 24)
        left18 = leftover_after(q96, 18, 24)
        left20 = leftover_after(q96, 20, 24)
        print("  n=96 leftover after 10/18/20: %.4e / %.4e / %.4e"
              % (left10, left18, left20))
        check("n96-left10",
              abs(left10 - float(N96_LEFT10_PIN)) < 5e-3,
              "leftover after psi_10")
        check("n96-left18",
              abs(left18 - float(N96_LEFT18_PIN)) < 5e-3,
              "leftover after psi_18")
        check("n96-left20",
              abs(left20 - float(N96_LEFT20_PIN)) < 5e-3,
              "leftover after psi_20")
        drop = left10 / max(left18, 1e-30)
        print("  drop 10->18: %.2f  (hoped ~20x per step, ~400x total)"
              % drop)
        check("drop-falsified",
              drop < 3.0,
              "drop is O(1), not 20x")
        check("left20-over-budget",
              left20 > 50.0 * float(BUDGET_PIN),
              "factor ~%.0f vs budget" % (left20 / float(BUDGET_PIN)))

        # enlarge B: leftover ~ kappa_high
        rest = list(range(10, 24, 2))
        c_en = q96[np.ix_([0, 2, 4, 6, 8], rest)]
        kap = float(np.linalg.svd(c_en, compute_uv=False)[0])
        print("  enlarge-B {0..8} leftover op=%.4e" % kap)
        check("kappa-high-lives",
              kap > 0.25,
              "r480 kappa_high still in the complement")

        # QR extension
        certified = [f96[k] for k in (0, 2, 4, 6, 8)]
        onb = qr_even_onb(x96, w96, certified, 28)
        print("  QR ONB size", len(onb))
        a_qr = KH.a_matrix(x96, w96, onb, 0.0, T_CUT, len(onb), 2000)
        p_qr = KH.pi_matrix(x96, w96, onb, len(onb))
        q_qr = a_qr + p_qr
        # 5 certified + 12 QR as C, leftover = further QR
        n_cert = 5
        C = q_qr[:3, 3:3 + 2 + 12]  # psi6,8 + 12 QR
        Cr = q_qr[:3, 3 + 2 + 12:]
        qr_left = float(np.linalg.norm(Cr, "fro")) if Cr.size else 0.0
        print("  QR leftover after 12 extra cols: %.4e" % qr_left)
        check("qr-leftover",
              qr_left > 0.05 and abs(qr_left - float(QR_LEFT12_PIN)) < 0.03,
              "QR completeness leak O(0.08)")

        # QR IBP kill (sinc extension, evk=1)
        n_ibp = 10
        jets = []
        for i, vec in enumerate(onb[:n_ibp]):
            if i < 5:
                jets.append(F483.jets_at(x96, w96, vec, ev96[2 * i],
                                         TSTAR, L_YB, 4))
            else:
                jets.append(F483.jets_at(x96, w96, vec, 1.0,
                                         TSTAR, L_YB, 4))
        tt = np.linspace(T_CUT, 800.0, 4000)
        from scipy.special import psi as digamma
        sg = np.real(digamma(0.25 + 1j * tt / 2.0)) - math.log(math.pi)
        hats = [np.array([F483.hat_ibp_even(j, t, 4) for t in tt])
                for j in jets]
        at = np.zeros((n_ibp, n_ibp))
        for i in range(n_ibp):
            for j in range(i, n_ibp):
                at[i, j] = at[j, i] = (
                    float(np.trapezoid(sg * hats[i] * hats[j], tt)) / PI)
        q_ibp = q_qr[:n_ibp, :n_ibp] + at
        sig8 = float(KH.sigma_arr(np.array([TSTAR]))[0])
        ct = sig8 * (1.0 - float(ev96[6])) + SIG0 * float(ev96[6])
        B, Cib = q_ibp[:3, :3], q_ibp[:3, 3:]
        smin = float(np.min(np.linalg.eigvalsh(B - Cib @ Cib.T / ct)))
        print("  QR+IBP lambda_min(S)=%.4e" % smin)
        check("qr-ibp-kills",
              smin < float(QR_IBP_SMIN_PIN),
              "sinc-IBP of QR makes S negative")
        check("not-a-pad",
              True,
              "uncertified modes / QR-IBP not used as a pad")
        check("not-proved-lambda",
              True,
              "block completion does not assemble lambda_*")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN even_lminS=%.8e leftover48=%.8e" % (rec["even"][2], left48))
    if not smoke:
        print("  PIN n96_left10=%.8e left18=%.8e left20=%.8e"
              % (left10, left18, left20))
        print("  PIN qr_left=%.8e qr_ibp_smin=%.8e kap=%.8e"
              % (qr_left, smin, kap))
    print("PIN_DUMP_END")
    if n_fail:
        print("BLOCK_COMPLETION FAILED")
        return 1
    print("BLOCK_COMPLETION %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
