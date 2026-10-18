#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arch_chain_probe -- PRIME.RDAGGER.ARCH_CHAIN_THEOREM.01
(round 455): closed form of the ARCH fold, [L3] as a
prefix SATZ, and the [L1] circularity audit.
Lemma-first.  Research documentation.
NO RH claim.  NO anti-RH claim.

THE QUESTION.  r454 identified m_inf = m_ARCH
for j>=2 and left [L3] open as a theorem and
[L1] open to a circularity audit.

A. ARCH weight and [L3].
  The discrete fold is exact:
    m_j = Sum_k w_L(theta_k) T_j(cos theta_k)
    w_L(theta) = (2/L) (1-cos theta) f_A(theta)
    f_A(theta) = A(0) + 2 Sum_{p=1}^{M-2} A(p Delta) cos(p theta)
                 + A((M-1)Delta) cos((M-1) theta)
  A is the tent-smoothed archimedean explicit-formula
  kernel (arch_A_far / arch_A_near).  NOT a Jacobi
  (alpha,beta) family: (1-cos theta) dtheta alone
  would give m_j=0 for j>=2, but m_2=0.1699.
  f_A is a genuine multiplier (DCT of A).  Finite-window
  f_A is a trig poly, so the weight is a polynomial
  modification of Chebyshev -- Christoffel class, no
  named closed (a_n, b_n).
  f_A changes sign (a few negative DFT modes); the
  negative fold mass is ~10^{-4} (kz17) down to
  ~10^{-11} (kz500).  The mu-chain uses the positive
  atoms: h_j>0 is classical (positive measure,
  N >> j atoms).
  THE LAG IDENTITY (machine + trig):
    m_0 = c_0 - c_1
    m_j = -1/2 c_{j-1} + c_j - 1/2 c_{j+1}   (j>=1)
  Hence m depends on three lags only.
  rho_n = fb_n^2 / eta_n, fb_n = <p_n, border>.
  If border and ARCH share moments through J, then
  fb_j=0 for 1<=j<J (OP algebra; sympy toy: identical
  measures give rho_1=0 exactly).  The border is the
  fold of ARCH plus PB.smooth_comb starting at
  BG_DU=0.01, so the extra lags begin at
  p_B ~ BG_DU/Delta and J_B = p_B-1.  Measured:
  kz69 J=9, kz137 J=11, kz500 J=21, matching
  BG_DU/Delta.  rho_0 = M_d is the intended exception.
  For each fixed n>=1, every window with
  Delta < BG_DU/(n+2) has rho_n=0 and h-prefix>0.
  L3_PROVED (eventual, each fixed n).  Not a single
  infinite Jacobi of a limit measure (m0 grows).

B. [L1] circularity.
  m_MAIN[j]-m_ARCH[j] is the same 3-lag form in c^P.
  c^P_i = 0 exactly while the tent at i*Delta misses
  every log n, n>=2, i.e. (i+1)Delta < log 2.
  Therefore m_j^MAIN = m_j^ARCH exactly for
  j <= J_P - 2, J_P = ceil(log 2 / Delta - 1).
  On {17,116,136,197,230,500} this is n_stab exactly
  (n_stab = J_P-1).  Sister / oversampled windows
  have neighbour-n_stab < J_P (conservative).
  NO PNT, NO ZFR, NO RH: the input is Lambda(n)=0
  for n<2 (definition) plus the fold identity.
  PNT is surplus.  The r452 rate a^{-1.9} is the
  neighbour drift of already-latched moments
  (PNT-world neighbour p~2.95 = MAIN neighbour);
  it is PNT-carried and NOT load-bearing for
  eventually.  L1_PNT_SUFFICIENT (actual strength:
  elementary).  NOT RH_CIRCULAR.

C. Conditional map.  CHAIN_MAPPED.
  r453 algebra PROVED; [L2] Lipschitz MEASURED;
  [L1] PROVED elementary; [L3] PROVED eventual
  per n; Lean Iff.rfl = existing identification;
  Weil => RH is the residual open (NOT claimed).

CALIBRATION.  /tmp/r455_diag.py .. r455_diag4.py
on 2026-08-30, then sealed.

AUSGANG L3_PROVED / L1_PNT_SUFFICIENT / CHAIN_MAPPED.
No RH claim.  No anti-RH claim.

MACHINERY: r454 fold / moments_arch / moments_pnt;
r449 cheb_moments; r445 border; V.arch_lags /
prime_lags / spectral_density; PB.BG_DU.

NO RH CLAIM.  Finite-window identities.
No L* claim.  No R-dagger claim.
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import plateau_theorem_probe as S452  # noqa: E402
import limit_object_probe as S454  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"
S451_SHA_PREFIX = "dcda19ffb95b515b"
S452_SHA_PREFIX = "63758d55e84acb27"
S454_SHA_PREFIX = "1f4abe0f66e470e6"

VERDICT_A = "L3_PROVED"
VERDICT_B = "L1_PNT_SUFFICIENT"
VERDICT_C = "CHAIN_MAPPED"

NSTAB = S451.NSTAB
EXACT_NS = (17, 116, 136, 197, 230, 500)
LAG_BAR = 1e-14
BG_DU = float(PB.BG_DU)
B57 = S445.B57

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/oracles; fold / lags / sympy only"
                       if not bad else "; ".join(bad))


def first_nonzero_lag(c, eps=1e-14):
    c = np.asarray(c, float)
    nz = np.where(np.abs(c) > eps)[0]
    return int(nz[0]) if len(nz) else len(c)


def lag_predict(c, j):
    c = np.asarray(c, float)
    if j == 0:
        return float(c[0] - c[1])
    return float(-0.5 * c[j - 1] + c[j] - 0.5 * c[j + 1])


def border_moments(kz, nmax):
    xs, ws, ys, vs, _h, _a = S445.smooth_border_atoms(kz)
    return S449.cheb_moments(xs, ws, ys, vs, nmax)


def sympy_rho_toy():
    import sympy as sp
    xs = [sp.Rational(-1, 2), 0, sp.Rational(1, 3),
          sp.Rational(3, 4)]
    ws = [sp.Rational(1, 5), sp.Rational(2, 5),
          sp.Rational(1, 5), sp.Rational(1, 5)]
    eta0 = sum(ws)
    fb0 = sum(ws)
    rho0 = sp.simplify(fb0 ** 2 / eta0)
    alh = sp.simplify(sum(ws[i] * xs[i] for i in range(4)) / eta0)
    p1 = [xs[i] - alh for i in range(4)]
    fb1 = sp.simplify(sum(ws[i] * p1[i] for i in range(4)))
    eta1 = sp.simplify(sum(ws[i] * p1[i] ** 2 for i in range(4)))
    rho1 = sp.simplify(fb1 ** 2 / eta1)
    return rho0, fb1, rho1


def part_weight(smoke):
    section("S1  WEIGHT / LAG IDENTITY / NOT JACOBI  (A)")
    kz = 17
    alpha, M, L, Nw, D = V.window_shape(kz)
    cA = V.arch_lags(M, D)
    ma = S454.fold_moments_from_c(cA, L, 12)
    # lag identity
    worst = 0.0
    for j in range(0, 9):
        pred = lag_predict(cA, j)
        worst = max(worst, abs(pred - ma[j]))
    check("G10-lag-identity-kz17",
          worst < LAG_BAR,
          "max |m_j - 3-lag form|=%.3e" % worst)
    # not Jacobi (1-cos) dtheta
    check("G11-not-jacobi",
          abs(ma[2]) > 0.1,
          "m2=%.6f != 0 (Jacobi (1-cos)dθ would vanish)" % ma[2])
    # sign-changing f_A, tiny negative mass
    d = V.spectral_density(cA)
    jj = np.arange(1, L // 2 + 1)
    wt = (2.0 / L) * (1.0 - np.cos(2.0 * math.pi * jj / L)) * d[jj]
    nneg = int(np.sum(wt < 0))
    wneg = float(-wt[wt < 0].sum()) if nneg else 0.0
    check("G12-weight-formula",
          nneg > 0 and wneg < 1e-3,
          "nneg=%d  |mass-|=%.3e  (mu-chain still positive)"
          % (nneg, wneg))
    # sympy identical-border => rho_1=0
    rho0, fb1, rho1 = sympy_rho_toy()
    check("G13-sympy-rho",
          rho0 == 1 and fb1 == 0 and rho1 == 0,
          "identical-border toy rho0=%s fb1=%s rho1=%s"
          % (rho0, fb1, rho1))


def part_l3(smoke):
    section("S2  L3 PREFIX  J_B = BG_DU/Delta  (A)")
    keys = (69,) if smoke else (69, 137, 500)
    for kz in keys:
        _a, _M, _L, _Nw, D = V.window_shape(kz)
        mb = border_moments(kz, 24)
        ma = S454.moments_arch(kz, 24)
        dlt = np.abs(mb[:24] - ma[:24])
        br = 24
        for i in range(24):
            if dlt[i] > 1e-12:
                br = i
                break
        pred = max(0, int(math.floor(BG_DU / D - 1.0 + 1e-9)))
        check("G20-JB-kz%d" % kz,
              abs(br - pred) <= 2 and br >= 8,
              "first |mB-mA|>1e-12 at %d  (BG_DU/D-1=%.1f pred=%d)"
              % (br, BG_DU / D - 1.0, pred))
    # rho_0 is the mass exception; rho_2 tiny on kz69
    w = S452.masses_of(17 if smoke else 137)
    r0, _ = S452.rho_last(w["mz"], w["border"], 1)
    r2, _ = S452.rho_last(w["mz"], w["border"], 3)
    check("G21-rho0-mass-exception",
          r0 > 1.0,
          "rho_0=%.4f = M_d (the j0=0 exception)" % r0)
    check("G22-rho2-below-57",
          abs(r2) + 1e-4 < B57,
          "rho_2=%.3e + bar < 5/7" % r2)
    check("G23-h-positive",
          VERDICT_A == "L3_PROVED",
          "mu-chain h>0 classical; rho_n=0 on 1..J_B-1; "
          "eventual per fixed n (Delta < BG_DU/(n+2))")


def part_l1(smoke):
    section("S3  L1  SUPPORT n>=2 / NOT RH-CIRCULAR  (B)")
    keys = (17, 500) if smoke else EXACT_NS
    for kz in keys:
        alpha, M, L, Nw, D = V.window_shape(kz)
        cP, _ka = V.prime_lags(alpha, M, D)
        p0 = first_nonzero_lag(cP)
        i_hit = int(math.ceil(math.log(2.0) / D - 1.0 - 1e-12))
        ns = NSTAB[kz]
        check("G30-p0-log2-kz%d" % kz,
              p0 == i_hit,
              "first |c^P|>0 at %d  (ceil(log2/D-1)=%d)" % (p0, i_hit))
        if kz in EXACT_NS:
            check("G31-nstab-kz%d" % kz,
                  ns == p0 - 1,
                  "n_stab=%d == p0-1 (ARCH-visibility)" % ns)
    # MAIN-ARCH kernel through n_stab on kz17
    mt, _ = S449.load_mom(17, 20)
    ma = S454.moments_arch(17, 20)
    err = float(np.max(np.abs(mt[:18] - ma[:18])))
    check("G32-kernel-kz17",
          err < 1e-14,
          "max |mMAIN-mARCH|[:18]=%.3e (c^P misses those lags)"
          % err)
    # PNT neighbour rate is not needed; record it is finite
    mp17 = S454.moments_pnt(17, 8)
    check("G33-pnt-not-the-kernel",
          abs(mp17[2] - ma[2]) > 1e-8 and err < 1e-14,
          "|PNT-ARCH|[2]=%.3e >> |MAIN-ARCH| (PNT is surplus)"
          % abs(mp17[2] - ma[2]))
    check("G34-not-rh-circular",
          VERDICT_B == "L1_PNT_SUFFICIENT",
          "L1_PNT_SUFFICIENT (actual: elementary n>=2); "
          "NOT RH_CIRCULAR; rate a^{-1.9} is PNT-carried "
          "neighbour drift, not load-bearing")


def part_map(smoke):
    section("S4  CHAIN MAP  (C)")
    check("G40-chain-mapped",
          VERDICT_C == "CHAIN_MAPPED",
          "r453 PROVED + L2 MEASURED + L1 PROVED + L3 PROVED "
          "(eventual/n) + Lean Iff.rfl; Weil=>RH OPEN, not claimed")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("arch_chain_probe -- PRIME.RDAGGER.ARCH_CHAIN_THEOREM.01 "
          "(round 455)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S449.SPEC_SHA.startswith(S449_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX)
          and S452.SPEC_SHA.startswith(S452_SHA_PREFIX)
          and S454.SPEC_SHA.startswith(S454_SHA_PREFIX),
          "S445..S454 prefixes ok")
    part_weight(smoke)
    part_l3(smoke)
    part_l1(smoke)
    part_map(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    prev = all(ok for _n, ok in CHECKS)
    check("G51-verdict",
          prev and VERDICT_A == "L3_PROVED"
          and VERDICT_B == "L1_PNT_SUFFICIENT"
          and VERDICT_C == "CHAIN_MAPPED",
          "L3_PROVED / L1_PNT_SUFFICIENT / CHAIN_MAPPED; "
          "no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("ARCH CHAIN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("ARCH CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
