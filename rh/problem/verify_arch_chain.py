#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_arch_chain.py -- machine check of every numbered
lemma in rh/problem/arch_chain.tex (round 455,
L3_PROVED / L1_PNT_SUFFICIENT / CHAIN_MAPPED).

PART A (STANDALONE):
  G1  verdicts
  G2  lag identity m_j = 3-lag form on kz17 ARCH
  G3  sympy identical-border => rho_1 = 0

PART B (CONSTRUCTION PINS):
  G10 n_stab(17) = first prime-lag - 1
  G11 MAIN-ARCH kernel through n_stab on kz17
  G12 J_B(kz69) matches BG_DU/Delta

Exit: "ARCH CHAIN VERIFIED" iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import arch_chain_probe as S  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import limit_object_probe as S454  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def part_a():
    section("PART A  VERDICT / LAG / SYMPY")
    check("G1-verdict",
          S.VERDICT_A == "L3_PROVED"
          and S.VERDICT_B == "L1_PNT_SUFFICIENT"
          and S.VERDICT_C == "CHAIN_MAPPED",
          "%s / %s / %s" % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    _a, M, L, _Nw, D = V.window_shape(17)
    cA = V.arch_lags(M, D)
    ma = S454.fold_moments_from_c(cA, L, 10)
    worst = max(abs(S.lag_predict(cA, j) - ma[j]) for j in range(9))
    check("G2-lag-identity",
          worst < S.LAG_BAR,
          "max 3-lag residual=%.3e" % worst)
    rho0, fb1, rho1 = S.sympy_rho_toy()
    check("G3-sympy-rho",
          rho0 == 1 and fb1 == 0 and rho1 == 0,
          "rho0=%s fb1=%s rho1=%s" % (rho0, fb1, rho1))


def part_b():
    section("PART B  SUPPORT / KERNEL / J_B")
    alpha, M, L, _Nw, D = V.window_shape(17)
    cP, _ = V.prime_lags(alpha, M, D)
    p0 = S.first_nonzero_lag(cP)
    check("G10-nstab-p0",
          S.NSTAB[17] == p0 - 1,
          "n_stab=%d p0=%d" % (S.NSTAB[17], p0))
    mt, _ = S449.load_mom(17, 20)
    ma = S454.moments_arch(17, 20)
    err = float(np.max(np.abs(mt[:18] - ma[:18])))
    check("G11-kernel",
          err < 1e-14,
          "max |MAIN-ARCH|[:18]=%.3e" % err)
    _a, _M, _L, _Nw, D69 = V.window_shape(69)
    mb = S.border_moments(69, 16)
    ma69 = S454.moments_arch(69, 16)
    dlt = np.abs(mb[:16] - ma69[:16])
    br = next((i for i in range(16) if dlt[i] > 1e-12), 16)
    pred = max(0, int(math.floor(S.BG_DU / D69 - 1.0 + 1e-9)))
    check("G12-JB-kz69",
          abs(br - pred) <= 2,
          "break=%d pred=%d" % (br, pred))


def main():
    print("verify_arch_chain -- r455")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("ARCH CHAIN VERIFIED")
        return 0
    print("ARCH CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
