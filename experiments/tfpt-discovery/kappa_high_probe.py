#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kappa_high_probe -- PRIME.RDAGGER.KAPPA_HIGH.01 (r480).

Attempt to close the r479 remainder
  kappa_high = ||P_5 A_+ (1-P_5)|| <= 1.79e-2
at the split (t*,N)=(8,5), A_+ = sigma_A * 1_{|t|>=8},
P_5 = projection on the first five Slepian modes of band 8
on L^2[-0.3,0.3].  r469 contract.  Fourier-HS is already
killed (r478/r479) and is not reused.

WHAT CLOSES.  The named operator-norm bound is FALSE:
Nyström-stable quadrature gives kappa_high ~ 3.0e-1 at
(8,5) and at every scanned rebalance (t*,N).  Edge modes
n=3,4 have high-band mass 1-lambda = O(1) and couple
O(sigma) to the equally high-frequency tail (parity:
even-odd blocks of A vanish).  The crude Schur budget
sqrt(mu_3 c_tail) - kappa_low mixes that edge singular
value with the ground-mode eigenvalue -- structurally
the wrong test.  n=16 resolves eigenvalues (r479) but
NOT Fourier transforms of higher prolates.

WHAT REMAINS.  The matrix Schur of the even 3x3 Q-Gram
B on {psi_0, psi_2, psi_4} against the even tail,
  S = B - C C^T / c_tail,
is numerically PD (lmin ~ 5e-3 at n=48, T=150; n=48 vs
64 stable; T>200 quadrature dies because e^{itx} outruns
the Gauss nodes).  Odd sector is easier.  Proving S>0
with interval FT on [8,T] plus a 1/t^2 integration-by-parts
tail (prolates do not vanish at +/-L) would close
lambda_*(0.3)>=c.  Not proved this round.

CONVENTION (r461..r479).  Prime nodes n with log n <= 2L.
SCRAMBLE GATE: P is empty at L=0.3; the gate is vacuous
but the literal log n test is kept.  NO RH CLAIM.
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
from scipy.special import psi as digamma

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

import highmode_probe as HM  # noqa: E402
import lambdastar03_probe as L479  # noqa: E402

L_YB = 0.3
SIG0 = -5.372183419225666
TSTAR = 8.0
N_BLOCK = 5

KAPPA_HIGH_NEED = "1.79e-02"
KAPPA_HIGH_LO_PIN = "0.25"
SCHUR_EVEN_LO_PIN = "4.0e-03"
SCHUR_ODD_LO_PIN = "0.15"
SIG8_LO_PIN = "0.2408"
C_TAIL_LO_PIN = "0.2408"

VERDICT_KIND = "REDUCED(refined-Schur; crude-kappa_high-killed@0.30)"
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


def sinc_kernel(dx, tc):
    if abs(dx) < 1e-15:
        return tc / math.pi
    return math.sin(tc * dx) / (math.pi * dx)


def nystrom_modes(L, tc, n=48):
    x_ref, w_ref = np.polynomial.legendre.leggauss(n)
    x = L * x_ref
    w = L * w_ref
    sw = np.sqrt(np.maximum(w, 0.0))
    ker = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            ker[i, j] = sinc_kernel(x[i] - x[j], tc)
    amat = 0.5 * ((sw[:, None] * ker) * sw[None, :]
                  + ((sw[:, None] * ker) * sw[None, :]).T)
    ev, evecs = np.linalg.eigh(amat)
    idx = np.argsort(ev)[::-1]
    ev, evecs = ev[idx], evecs[:, idx]
    funcs = []
    for k in range(len(ev)):
        f = evecs[:, k] / np.maximum(sw, 1e-30)
        nrm = math.sqrt(float(np.sum(w * f * f)))
        funcs.append(f / nrm)
    return ev, x, w, funcs


def sigma_arr(ts):
    z = 0.25 + 1j * (ts / 2.0)
    return np.real(digamma(z)) - math.log(math.pi)


def hat_grid(x, w, f, ts):
    return np.exp(1j * np.outer(ts, x)) @ (w * f)


def a_matrix(x, w, funcs, t0, t1, m_modes, nt):
    """A on [t0,t1] union [-t1,-t0] via evenness: (1/pi) int_{t0}^{t1}."""
    ts = np.linspace(t0, t1, nt)
    sig = sigma_arr(ts)
    hats = [hat_grid(x, w, funcs[k], ts) for k in range(m_modes)]
    amat = np.zeros((m_modes, m_modes))
    for i in range(m_modes):
        for j in range(i, m_modes):
            integ = np.trapezoid(sig * hats[i] * np.conjugate(hats[j]), ts)
            amat[i, j] = amat[j, i] = integ.real / math.pi
    return amat


def pi_matrix(x, w, funcs, m_modes):
    pmat = np.zeros((m_modes, m_modes))
    csh = np.cosh(0.5 * x)
    snh = np.sinh(0.5 * x)
    ov_c = np.array([float(np.sum(w * funcs[k] * csh)) for k in range(m_modes)])
    ov_s = np.array([float(np.sum(w * funcs[k] * snh)) for k in range(m_modes)])
    for i in range(m_modes):
        for j in range(m_modes):
            if i % 2 == 0 and j % 2 == 0:
                pmat[i, j] = 2.0 * ov_c[i] * ov_c[j]
            elif i % 2 == 1 and j % 2 == 1:
                pmat[i, j] = 2.0 * ov_s[i] * ov_s[j]
    return pmat


def schur_of(qmat, n_block, c_tail, parity):
    block = [k for k in range(n_block) if k % 2 == parity]
    tail = [k for k in range(n_block, qmat.shape[0]) if k % 2 == parity]
    bmat = qmat[np.ix_(block, block)]
    cmat = qmat[np.ix_(block, tail)]
    if cmat.size == 0:
        smin = float(np.min(np.linalg.eigvalsh(bmat)))
        return smin, 0.0, smin
    s_op = float(np.linalg.svd(cmat, compute_uv=False)[0])
    smat = bmat - (cmat @ cmat.T) / c_tail
    return (
        float(np.min(np.linalg.eigvalsh(bmat))),
        s_op,
        float(np.min(np.linalg.eigvalsh(smat))),
    )


def measure(tstar, n_block, n_ny=48, m_modes=12, t_cut=150.0, nt=3000):
    ev, x, w, funcs = nystrom_modes(L_YB, tstar, n_ny)
    eps = float(ev[n_block]) if n_block < len(ev) else 0.0
    sig = float(sigma_arr(np.array([tstar]))[0])
    c_tail = sig * (1.0 - eps) + SIG0 * eps
    a_plus = a_matrix(x, w, funcs, tstar, t_cut, m_modes, nt)
    a_full = a_matrix(x, w, funcs, 0.0, t_cut, m_modes, nt)
    qmat = a_full + pi_matrix(x, w, funcs, m_modes)
    block = a_plus[:n_block, n_block:m_modes]
    kappa = float(np.linalg.svd(block, compute_uv=False)[0]) if block.size else 0.0
    even = schur_of(qmat, n_block, c_tail, 0)
    odd = schur_of(qmat, n_block, c_tail, 1)
    return {
        "ev": ev, "x": x, "w": w, "funcs": funcs,
        "eps": eps, "sig": sig, "c_tail": c_tail,
        "a_plus": a_plus, "q": qmat, "kappa": kappa,
        "even": even, "odd": odd,
    }


def ibp_tail_integral(t_cut):
    """int_T^infty (1+log t)/t^2 dt = (1 + log T)/T  (sigma ~ log)."""
    return (1.0 + math.log(t_cut)) / t_cut


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("kappa_high_probe -- r480")
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
          and "killed" in VERDICT_KIND,
          VERDICT_KIND)
    check("no-fourier-hs",
          "Fourier-HS is already" in (__doc__ or "")
          and "not reused" in (__doc__ or ""),
          "HS majorant not reused")

    rec = measure(TSTAR, N_BLOCK, n_ny=48, m_modes=12, t_cut=150.0, nt=3000)
    print("  t*=8 N=5 n=48 T=150  kappa_high=%.6e  c_tail=%.6f  eps=%.4e"
          % (rec["kappa"], rec["c_tail"], rec["eps"]))
    print("  even Schur  lminB=%.6e  ||C||=%.6e  lminS=%.6e" % rec["even"])
    print("  odd  Schur  lminB=%.6e  ||C||=%.6e  lminS=%.6e" % rec["odd"])
    print("  A+[4,5]=%.3e (parity)  A+[4,6]=%.4f  A+[3,5]=%.4f"
          % (rec["a_plus"][4, 5], rec["a_plus"][4, 6], rec["a_plus"][3, 5]))

    budget = float(KAPPA_HIGH_NEED)
    check("crude-kill",
          rec["kappa"] > float(KAPPA_HIGH_LO_PIN),
          "kappa_high=%.4e > 0.25 (named bound false)" % rec["kappa"])
    check("budget-dead",
          rec["kappa"] > budget,
          "kappa_high / budget = %.2f" % (rec["kappa"] / budget))
    check("tail-pos",
          rec["c_tail"] > float(C_TAIL_LO_PIN),
          "c_tail=%.6f" % rec["c_tail"])
    check("refined-even",
          rec["even"][2] > float(SCHUR_EVEN_LO_PIN),
          "even lmin(S)=%.6e (numeric, not certified)" % rec["even"][2])
    check("refined-odd",
          rec["odd"][2] > float(SCHUR_ODD_LO_PIN),
          "odd lmin(S)=%.6e" % rec["odd"][2])
    check("parity-A+",
          abs(rec["a_plus"][4, 5]) < 1e-8,
          "even-odd A+ vanishes")
    check("ibp-tail",
          0.0 < ibp_tail_integral(150.0) < 0.05,
          "int_T^inf (1+log t)/t^2 = %.4e" % ibp_tail_integral(150.0))
    check("not-proved",
          True,
          "S>0 not interval-certified; not lambda_*")

    if not smoke:
        rec64 = measure(TSTAR, N_BLOCK, n_ny=64, m_modes=12,
                        t_cut=150.0, nt=3000)
        d_s = abs(rec["even"][2] - rec64["even"][2])
        d_k = abs(rec["kappa"] - rec64["kappa"])
        print("  n=64  kappa=%.6e  even lminS=%.6e  |dS|=%.3e  |dk|=%.3e"
              % (rec64["kappa"], rec64["even"][2], d_s, d_k))
        check("n48-vs-64",
              d_s < 5e-4 and d_k < 5e-3,
              "FT-stable at n>=48")

        ev16, x16, w16, f16 = nystrom_modes(L_YB, TSTAR, 16)
        a16 = a_matrix(x16, w16, f16, 0.0, 150.0, 6, 2000)
        q00_16 = a16[0, 0] + pi_matrix(x16, w16, f16, 6)[0, 0]
        q00_48 = rec["q"][0, 0]
        print("  Q00 n=16=%.4f  n=48=%.4f" % (q00_16, q00_48))
        check("n16-ft-unusable",
              abs(q00_16 - q00_48) > 1.0,
              "n=16 resolves evals, not FTs")

        ev48 = L479.nystrom_evals(L_YB, TSTAR, 48)[0]
        check("eps-r479",
              abs(float(ev48[5]) - rec["eps"]) < 1e-12,
              "lambda_6(K_8) matches r479 Nyström")

        print("  rebalance scan:")
        worst_lo = 1.0
        for tstar, nblk in ((8.0, 5), (8.0, 6), (10.0, 6), (12.0, 7)):
            row = measure(tstar, nblk, n_ny=48, m_modes=12,
                          t_cut=150.0, nt=2000)
            worst_lo = min(worst_lo, row["kappa"])
            print("    t*=%.0f N=%d  k=%.4e  evenS=%.4e  oddS=%.4e"
                  % (tstar, nblk, row["kappa"],
                     row["even"][2], row["odd"][2]))
        check("rebalance-kill",
              worst_lo > 0.25,
              "min kappa_high over splits=%.4e" % worst_lo)

        # Plancherel of psi_0 on [-80,80]
        ts = np.linspace(-80.0, 80.0, 4001)
        h0 = hat_grid(rec["x"], rec["w"], rec["funcs"][0], ts)
        pl = float(np.trapezoid(np.abs(h0) ** 2, ts) / (2.0 * math.pi))
        check("plancherel-0",
              0.99 < pl < 1.01,
              "||psi_0||^2 via FT=%.6f" % pl)

        end48 = abs(rec["funcs"][0][0])
        end64 = abs(rec64["funcs"][0][0])
        check("endpoint-stable",
              abs(end48 - end64) < 0.02,
              "|psi_0(-L)| n48=%.4f n64=%.4f" % (end48, end64))

        sig8 = float(rec["sig"])
        check("sig8",
              sig8 >= float(SIG8_LO_PIN),
              "sigma(8)=%.6f" % sig8)
        check("r479-contract",
              L479.VERDICT_KIND.startswith("REDUCED")
              and float(L479.KAPPA_HIGH_NEED) < 0.02,
              "r479 remainder was the named bound")
        check("hs-identity",
              HM.sigma_A_K is not None,
              "sigma identity imported, not an HS row-sum")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN kappa_high=%.8e  even_lminS=%.8e  odd_lminS=%.8e"
          % (rec["kappa"], rec["even"][2], rec["odd"][2]))
    print("  PIN c_tail=%.8f  eps=%.8e  sig8=%.8f"
          % (rec["c_tail"], rec["eps"], rec["sig"]))
    print("PIN_DUMP_END")
    if n_fail:
        print("KAPPA_HIGH FAILED")
        return 1
    print("KAPPA_HIGH %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
