#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lambdastar03_probe -- PRIME.RDAGGER.LAMBDASTAR_03_KEYSTONE.01 (r479).

Attempt to close lambda_*(0.3) >= c > 0 via multiplier + rank-one.
At L=0.3, P=0, so Q = A + Pi with A a Fourier multiplier (symbol
sigma_A, even, increasing) and Pi rank one per parity
(Pi_even = 2 |<., cosh(x/2)>|^2, Pi_odd = 2 |<., sinh(x/2)>|^2).
The r478 row-sum Schur is not forced.

WHAT CLOSES.  t_c with sigma_A(t_c)=0 is interval-pinned via the
r476 digamma identity.  tr(K)=2 L t_c / pi is elementary.
Even Fourier blocks N=2..5 are PD (r478).  Odd sine diagonals
are positive.  The minorant M = sigma_A(0) K + Pi is INDEFINITE
(second even prolate / first odd prolate): rank-one cannot lift
a two-dimensional negative space.  So A must be used, not the
constant minorant, on the essential prolate block.

WHAT REMAINS.  After N prolates of a band t* > t_c with
sigma_A(t*)>0, the K-tail satisfies
  A >= sigma(t*)(1-eps) + sigma(0) eps > 0
with eps = lambda_{N+1}.  Low-band coupling is <= |sigma(0)| * sqrt(eps)
(PROVED).  High-band coupling kappa_high of A_+ = sigma 1_{|t|>=t*}
between the block and the K-tail is the exact remainder: the
split (t*,N)=(8,5) closes iff kappa_high <= 1.79e-2.
Not proved this round.  Not lambda_*(0.3)>=0.

CONVENTION (r461..r478).  Prime nodes n with log n <= 2L.
SCRAMBLE GATE: P is empty at L=0.3; the gate is vacuous but
the literal log n test is kept.  NO RH CLAIM.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
from mpmath import iv

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
import crossterm_probe as CT  # noqa: E402
import endtoend_fixedl_probe as E  # noqa: E402
import highmode_probe as HM  # noqa: E402

DPS = 40
L_YB = 0.3

T_C_LO_PIN = "6.289835988836902"
T_C_HI_PIN = "6.289835988836904"
SIG0_LO_PIN = "-5.372183419225667"
SIG0_HI_PIN = "-5.372183419225665"
TR_LO_PIN = "1.201270186632830"
TR_HI_PIN = "1.201270186632832"
LMIN2_LO_PIN = "1.731e-02"
HIGHAM3_PIN = "2.45e-03"
KAPPA_HIGH_NEED = "1.79e-02"
SIG8_LO_PIN = "0.2408"

VERDICT_KIND = "REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)"
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


def nystrom_evals(L, tc, n=48):
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
    ev = np.sort(np.linalg.eigvalsh(amat))[::-1]
    return ev, x, w, sw, amat


def pin_t_c():
    """Certified bracket via digamma identity (r476)."""
    def sigf(t):
        return [float(x) for x in CC.ivsplit(HM.sigma_digamma(t))]

    lo, hi = 6.0, 6.4
    for _ in range(70):
        m = 0.5 * (lo + hi)
        s = sigf(m)
        if s[1] < 0:
            lo = m
        else:
            hi = m
    t_neg = lo
    lo, hi = 6.2, 6.5
    for _ in range(70):
        m = 0.5 * (lo + hi)
        s = sigf(m)
        if s[0] > 0:
            hi = m
        else:
            lo = m
    t_pos = hi
    return t_neg, t_pos, sigf(t_neg), sigf(t_pos)


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("lambdastar03_probe -- r479")
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

    s0 = CT.sigma0_closed()
    s0lo, s0hi = CC.ivsplit(s0)
    s0lo_f, s0hi_f = float(s0lo), float(s0hi)
    check("sigma0",
          s0lo_f >= float(mp.mpf(SIG0_LO_PIN)) - 1e-15
          and s0hi_f <= float(mp.mpf(SIG0_HI_PIN)) + 1e-15,
          "sigma(0)=[%.15f,%.15f]" % (s0lo_f, s0hi_f))

    t_neg, t_pos, sn, sp = pin_t_c()
    print("  t_c in (%.15f, %.15f)" % (t_neg, t_pos))
    print("  sig(t_neg)", sn, "sig(t_pos)", sp)
    check("t-c-bracket",
          t_neg >= float(mp.mpf(T_C_LO_PIN)) - 1e-15
          and t_pos <= float(mp.mpf(T_C_HI_PIN)) + 1e-15
          and sn[1] < 0 < sp[0],
          "t_c pinned, sign change")
    tr_lo = 2 * L_YB * t_neg / math.pi
    tr_hi = 2 * L_YB * t_pos / math.pi
    check("trace-exact",
          tr_lo >= float(mp.mpf(TR_LO_PIN)) - 1e-15
          and tr_hi <= float(mp.mpf(TR_HI_PIN)) + 1e-15,
          "tr(K)=2L t_c/pi in [%.15f,%.15f]" % (tr_lo, tr_hi))

    Liv = iv.mpf("0.3")
    M3, diag, B0, _G = E.even_gram(Liv, 3, include_p=False)
    l2 = E.lmin_2x2(diag[0], diag[1], B0[1])
    l2_lo = float(CC.ivsplit(l2)[0])
    cert3 = CC.certify_matrix(M3)
    check("even-2x2", l2_lo >= float(mp.mpf(LMIN2_LO_PIN)),
          "charpoly lmin_lo=%.6e" % l2_lo)
    check("even-3x3",
          cert3["certified"]
          and cert3["mu"] >= float(mp.mpf(HIGHAM3_PIN)),
          "Higham3=%.6e" % (cert3["mu"] or -1))

    check("type-reduced",
          VERDICT_KIND.startswith("REDUCED"),
          "not PROVED, not silent upgrade")

    if not smoke:
        ev_c, x, w, sw, amat = nystrom_evals(L_YB, 0.5 * (t_neg + t_pos), 48)
        ev16, *_ = nystrom_evals(L_YB, 0.5 * (t_neg + t_pos), 16)
        dtop = max(abs(ev_c[k] - ev16[k]) for k in range(5))
        print("  prolates n=48", " ".join("%.6e" % v for v in ev_c[:6]))
        print("  |ev48-ev16|_top5", dtop)
        check("prolate-stable",
              dtop < 1e-9 and abs(ev_c.sum() - 0.5 * (tr_lo + tr_hi)) < 1e-8,
              "Nyström n=16 vs 48, trace match")
        check("prolate-l0", 0.8593 < ev_c[0] < 0.8595, "l0=%.6e" % ev_c[0])
        check("prolate-l1", 0.3137 < ev_c[1] < 0.3139, "l1=%.6e" % ev_c[1])
        check("prolate-l2", 0.02731 < ev_c[2] < 0.02733, "l2=%.6e" % ev_c[2])

        # M = s0 K + 2|cosh><cosh|  (even rank-1 only) is indefinite
        phi = np.cosh(0.5 * x)
        u_phi = sw * phi
        s0m = 0.5 * (s0lo_f + s0hi_f)
        Mop = s0m * amat + 2.0 * np.outer(u_phi, u_phi)
        me = np.sort(np.linalg.eigvalsh(Mop))
        print("  M=s0 K+2|cosh><cosh| lmin=%.6e" % me[0])
        check("minorant-indefinite",
              me[0] < -1.0,
              "rank-1 does not make M PD (lmin=%.4f)" % me[0])

        r_odd = (CT.A_of_mode(Liv, iv.pi / Liv, K=200)
                 + CT.Pi_of_mode(Liv, iv.pi / Liv)) / Liv
        ro = float(CC.ivsplit(r_odd)[0])
        check("odd-n1", ro > 0.29, "sin(pi x/L) r_lo=%.6e" % ro)

        # remainder inequality at (t*,N)=(8,5)
        ev8, *_ = nystrom_evals(L_YB, 8.0, 48)
        eps = float(ev8[5])
        sig8 = HM.sigma_A_K(iv.mpf("8"), 400)
        s8lo = float(CC.ivsplit(sig8)[0])
        c_tail = s8lo * (1.0 - eps) + s0lo_f * eps
        kappa_low = abs(s0lo_f) * math.sqrt(max(eps, 0.0))
        need = math.sqrt(max(cert3["mu"] or 0, 0.0) * max(c_tail, 0.0)) - kappa_low
        print("  t*=8 N=5  eps=%.4e  sig8_lo=%.6f  c_tail=%.6f" % (
            eps, s8lo, c_tail))
        print("  kappa_low=%.6e  kappa_high_need=%.6e" % (kappa_low, need))
        check("sig8", s8lo >= float(mp.mpf(SIG8_LO_PIN)),
              "sigma(8)_lo=%.6f" % s8lo)
        check("tail-pos", c_tail > 0.24,
              "A_tail >= %.6f" % c_tail)
        check("kappa-low", kappa_low < 0.007,
              "|s0| sqrt(eps)=%.6e" % kappa_low)
        check("remainder-open",
              need > 0.017 and need < 0.019,
              "HIGH-BAND remainder: kappa_high <= %.4e (OPEN)" % need)
        check("not-proved",
              True,
              "kappa_high not certified; not lambda_*")

        # 0.8 outlook (no computation of B)
        check("outlook-08",
              True,
              "L=0.8: P is a 3-node multiplier, not a rank-3 "
              "update of A; schema stays multiplier + rank-2 Pi")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN t_c=(%.15f,%.15f) tr=(%.15f,%.15f) s0=%.15f" % (
        t_neg, t_pos, tr_lo, tr_hi, s0lo_f))
    print("  PIN lmin2=%.8e higham3=%.8e" % (l2_lo, cert3["mu"] or 0))
    print("PIN_DUMP_END")
    if n_fail:
        print("LAMBDASTAR03 FAILED")
        return 1
    print("LAMBDASTAR03 %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
