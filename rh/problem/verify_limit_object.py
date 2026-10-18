#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_limit_object.py -- machine check of every numbered
lemma in rh/problem/limit_object.tex (round 454,
LIMIT_CLASSICAL / LIMITCHAIN_ALIVE_200 / CHAIN_DOCUMENTED).

PART A (STANDALONE):
  G1  verdicts
  G2  m_inf[2], m_inf[16] pins (kz500)
  G3  MAIN = ARCH through n_stab on kz17

PART B (CONSTRUCTION PINS):
  G10 rho_16(kz500) + 1e-4 < 5/7
  G11 Lipschitz dq/dm_2 < 0.25 on kz17
  G12 drop-500: kz137 m2 already at the pin

Exit: "LIMIT OBJECT VERIFIED" iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import limit_object_probe as S  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import plateau_theorem_probe as S452  # noqa: E402

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
    section("PART A  VERDICT / M_INF / ARCH")
    check("G1-verdict",
          S.VERDICT_A == "LIMIT_CLASSICAL"
          and S.VERDICT_B == "LIMITCHAIN_ALIVE_200"
          and S.VERDICT_C == "CHAIN_DOCUMENTED",
          "%s / %s / %s" % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    m500, _ = S449.load_mom(500, 20)
    check("G2-m-inf-pins",
          abs(m500[2] - S.M2_INF) < 1e-12
          and abs(m500[16] - S.M16_INF) < 1e-12,
          "m2=%.16f m16=%.16f" % (m500[2], m500[16]))
    mt, _ = S449.load_mom(17, 20)
    ma = S.moments_arch(17, 20)
    br = S.first_rel_break(mt, ma, 1e-4)
    check("G3-main-arch-kz17",
          br >= S451.NSTAB[17],
          "MAIN-ARCH break at %d (n_stab=%d)" % (br, S451.NSTAB[17]))


def part_b():
    section("PART B  RHO / LIPSCHITZ / DROP")
    w = S452.masses_of(500)
    rho, _ = S452.rho_last(w["mz"], w["border"], 16)
    check("G10-rho16-alive",
          abs(rho) + S.RHO_BAR < S.B57,
          "kz500 rho_16=%.3e + bar < 5/7" % rho)
    w17 = S452.masses_of(17)
    p0 = S451.pack_at(w17["mz"], 18, w17["border"])
    m0 = S451.cheb_moments_xy(w17["mz"]["xp"], w17["mz"]["wp"],
                              w17["mz"]["yn"], w17["mz"]["vn"], 20)
    import numpy as np
    xs = np.asarray(w17["mz"]["xp"], float)
    ws = np.asarray(w17["mz"]["wp"], float)
    T2 = 2.0 * xs * xs - 1.0
    mz2 = dict(w17["mz"])
    mz2["wp"] = ws + 1e-5 * float(np.mean(np.abs(ws))) * T2
    p = S451.pack_at(mz2, 18, w17["border"])
    mm = S451.cheb_moments_xy(mz2["xp"], mz2["wp"],
                             mz2["yn"], mz2["vn"], 20)
    lip = abs(p["qdag"] - p0["qdag"]) / max(abs(mm[2] - m0[2]), 1e-18)
    check("G11-lipschitz",
          lip < S.LIP_BAR,
          "dq/dm_2=%.3f" % lip)
    m137, _ = S449.load_mom(137, 8)
    check("G12-drop500-m2",
          abs(m137[2] - S.M2_INF) < 1e-10,
          "kz137 m2=%.16f" % m137[2])


def main():
    print("verify_limit_object -- r454")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("LIMIT OBJECT VERIFIED")
        return 0
    print("LIMIT OBJECT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
