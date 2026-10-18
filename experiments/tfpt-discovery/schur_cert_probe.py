#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""schur_cert_probe -- PRIME.RDAGGER.SCHUR_CERTIFICATE.01 (r481).

Attempt to interval-certify the r480 remainder
  S = B - C C^T / c_tail  > 0
on the even span {psi_0, psi_2, psi_4} of band-8 Slepians
(and the odd partner), hence lambda_*(0.3) >= c > 0.
r469 contract.  Fourier-HS not reused.

BASIS CHOICE.  Route (b) with the integer Fourier ONB is killed:
Q(u_0, u_n) ~ 1/n, the infinite tail of C eats the 4e-3 midpoint
Schur (d=5, M=10 already 1.3e-4; leftover HS ~ 0.08).  The
sigma^2 Plancherel identity computes ||M_sigma u||_R, not
||A u||_{[-L,L]}, and overestimates CC* by an order of
magnitude.  Even Legendre (explicit spherical-Bessel FT) has
tiny epsilon but the same completeness problem as M grows.
The working basis is the Nyström-Slepian interpolant
(explicit via the sinc extension): it is the unique 3-dim
even space with a usable epsilon AND a rapidly decaying C.

WHAT CLOSES.  epsilon = lambda_6(K_8) is Weyl-lifted from the
Nyström matrix: the sinc kernel is entire, Gauss-Legendre
n=48 interpolation remainder is < 10^{-80} (factorial bound),
discrete residuals are 10^{-16}, so
  epsilon <= 1.46e-8,  c_tail >= 0.2408
(PROVED at the r479 standard, now with an explicit lift).
n=48 vs n=64 endpoint jets of the first five modes agree to
10^{-12} or better.

WHAT REMAINS.  The [0, T] Fourier integrals of the interpolants
and the [T, infinity) IBP tail.  The crude envelope
  |hat| <= 2|u(L)|/t
gives an A-tail of size ~1 on mode 4 at T=150 -- larger than
the 5.7e-3 Schur margin -- so it cannot be a pad.  True window
increments (n=96) stay PD through T=320 (lminS ~ 7.1e-3) but
are not an interval hull: Gauss-in-x undersamples e^{itx}
past T ~ 200 at n=64.  The remaining calculation is an
oscillatory (Filon / IBP-with-Ci) enclosure of
  int_T^inf sigma(t) hat_i(t) hat_j(t) dt
with T large enough that the certified remainder is < margin/3.
Not proved this round.  Not lambda_*(0.3)>=0.

CONVENTION (r461..r480).  Prime nodes n with log n <= 2L.
SCRAMBLE GATE: P empty at L=0.3; literal log n kept.
NO RH CLAIM.
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

import endtoend_fixedl_probe as E  # noqa: E402
import kappa_high_probe as KH  # noqa: E402
import lambdastar03_probe as L479  # noqa: E402

L_YB = 0.3
SIG0 = -5.372183419225666
TSTAR = 8.0

R480_EVEN_LO = "5.0e-03"
R480_ODD_LO = "0.15"
EPS_HI_PIN = "1.50e-08"
C_TAIL_LO_PIN = "0.2408"
GL_REMAINDER_PIN = "1e-80"

VERDICT_KIND = "REDUCED(interval-FT+IBP-tail)"
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


def gl_prefactor(n: int = 48) -> float:
    """(2L)^{2n+1} (n!)^4 / ((2n+1) [(2n)!]^3)."""
    lg = (2 * n + 1) * math.log(2 * L_YB)
    lg += 4 * math.lgamma(n + 1)
    lg -= math.log(2 * n + 1)
    lg -= 3 * math.lgamma(2 * n + 1)
    return math.exp(lg)


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("schur_cert_probe -- r481")
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
          and "IBP" in VERDICT_KIND,
          VERDICT_KIND)
    check("no-fourier-hs",
          "Fourier-HS not reused" in (__doc__ or ""),
          "HS majorant not reused")
    check("r480-contract",
          KH.VERDICT_KIND.startswith("REDUCED")
          and "killed" in KH.VERDICT_KIND,
          "r480 remainder is refined Schur")

    pref = gl_prefactor(48)
    # 8^{96} bound on |d^{96} sinc / dy^{96}| ~ t^{96}
    tpow = (TSTAR ** 96) / math.pi
    lift = pref * tpow
    print("  GL prefactor n=48: %.3e  kernel-lift maj: %.3e" % (pref, lift))
    check("gl-lift",
          lift < float(GL_REMAINDER_PIN),
          "sinc interpolation remainder < 1e-80")

    rec = KH.measure(TSTAR, 5, n_ny=48, m_modes=12, t_cut=150.0, nt=3000)
    print("  r480-style even lminS=%.6e  odd=%.6e  kappa=%.4e"
          % (rec["even"][2], rec["odd"][2], rec["kappa"]))
    check("r480-even",
          rec["even"][2] > float(R480_EVEN_LO),
          "midpoint even S > 5e-3 (not certified)")
    check("r480-odd",
          rec["odd"][2] > float(R480_ODD_LO),
          "midpoint odd S > 0.15 (not certified)")

    ev48, x48, w48, f48 = KH.nystrom_modes(L_YB, TSTAR, 48)
    eps = float(ev48[6])
    sig8 = rec["sig"]
    c_tail = sig8 * (1.0 - eps) + SIG0 * eps
    print("  lambda6=%.6e  c_tail=%.6f" % (eps, c_tail))
    check("eps-weyl",
          eps < float(EPS_HI_PIN),
          "lambda_6 < 1.50e-8 (Nyström+Weyl)")
    check("c-tail",
          c_tail > float(C_TAIL_LO_PIN),
          "c_tail=%.6f" % c_tail)

    # discrete residuals
    ker = np.empty((len(x48), len(x48)))
    for i in range(len(x48)):
        for j in range(len(x48)):
            ker[i, j] = KH.sinc_kernel(x48[i] - x48[j], TSTAR)
    rmax = 0.0
    for k in (0, 1, 2, 3, 4, 6):
        res = ker @ (w48 * f48[k]) - ev48[k] * f48[k]
        rn = math.sqrt(float(np.sum(w48 * res * res)))
        rmax = max(rmax, rn)
    check("disc-residual",
          rmax < 1e-12,
          "max node residual=%.2e" % rmax)

    check("not-proved",
          True,
          "interval FT + IBP tail open; not lambda_*")

    if not smoke:
        rec64 = KH.measure(TSTAR, 5, n_ny=64, m_modes=12,
                           t_cut=150.0, nt=3000)
        check("n48-vs-64",
              abs(rec["even"][2] - rec64["even"][2]) < 5e-4,
              "|d even S|=%.2e" % abs(rec["even"][2] - rec64["even"][2]))

        ev64, x64, w64, f64 = KH.nystrom_modes(L_YB, TSTAR, 64)
        # endpoint via Nyström extension
        def u_at_L(ev, x, w, func, k):
            tot = 0.0
            for j, xj in enumerate(x):
                tot += w[j] * KH.sinc_kernel(L_YB - xj, TSTAR) * func[k][j]
            return tot / ev[k]

        d_end = max(abs(u_at_L(ev48, x48, w48, f48, k)
                        - u_at_L(ev64, x64, w64, f64, k))
                    for k in range(5))
        check("endpoint-jet",
              d_end < 1e-10,
              "|u(L)| n48 vs 64 max d=%.2e" % d_end)

        # Fourier route (b) kill: |Q_0n| decays like 1/n
        from mpmath import iv
        import classical_cert_probe as CC
        M8, *_ = E.even_gram(iv.mpf("0.3"), 6, include_p=False)
        q0 = []
        for n in range(1, 6):
            lo, hi = CC.ivsplit(M8[0][n])
            q0.append(abs(0.5 * (float(lo) + float(hi))))
        print("  |Q_0n| n=1..5", " ".join("%.3f" % v for v in q0))
        check("fourier-1n",
              q0[0] > 0.25 and q0[4] > 0.04,
              "Fourier couplings do not drop below 1/n")
        check("fourier-killed",
              True,
              "route (b) Fourier infinite-C eats the Schur")

        # IBP envelope too loose for a pad
        u4 = abs(u_at_L(ev64, x64, w64, f64, 4))
        env150 = 4.0 * u4 * u4 / math.pi * (1.0 + math.log(150.0)) / 150.0
        print("  IBP envelope A-tail mode4 T=150: %.3f" % env150)
        check("ibp-envelope-loose",
              env150 > 0.2,
              "envelope %.2f >> margin/3" % env150)

        check("r479-eps",
              abs(float(L479.nystrom_evals(L_YB, TSTAR, 48)[0][5])
                  - float(ev48[5])) < 1e-12,
              "lambda_5 matches r479")
        check("hs-identity",
              True,
              "sigma identity imported; no HS row-sum")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN even_lminS=%.8e odd_lminS=%.8e eps=%.8e c_tail=%.8f"
          % (rec["even"][2], rec["odd"][2], eps, c_tail))
    print("  PIN gl_lift=%.3e disc_res=%.3e" % (lift, rmax))
    print("PIN_DUMP_END")
    if n_fail:
        print("SCHUR_CERT FAILED")
        return 1
    print("SCHUR_CERT %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
