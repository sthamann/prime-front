#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_plateau_theorem.py -- machine check of every numbered
lemma in rh/problem/plateau_theorem.tex (round 452,
PLATEAU_IDENTITY_PROVED / QSTAR_UNDECIDED).

PART A (STANDALONE):
  G1  verdict PLATEAU_IDENTITY_PROVED / QSTAR_UNDECIDED
  G2  SATZ: q* = M_d/(M_d+5/7) on deep windows
  G3  A(ii) value REFUTED: sister same moments, different q*

PART B (CONSTRUCTION PINS):
  G10 kz17 grade-0 identities (b0, C00, B_w)
  G11 kz17 rho=0 on plateau, rho spike at n=19
  G12 scramble: moments do not latch, plateau dies

Exit: "PLATEAU THEOREM VERIFIED" iff every gate passed.
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

import plateau_theorem_probe as S  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402

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
    section("PART A  VERDICT / SATZ / SISTER")
    check("G1-verdict",
          S.VERDICT == "PLATEAU_IDENTITY_PROVED"
          and S.VERDICT_Q == "QSTAR_UNDECIDED",
          "verdict=%s / %s" % (S.VERDICT, S.VERDICT_Q))
    deep_ok = True
    worst = 0.0
    for kz in S.DEEP:
        w = S.masses_of(kz)
        ed = abs(w["q_deep"] - S.Q_NS[kz])
        worst = max(worst, ed)
        if abs(w["Md"] - w["signed"]) >= 1e-12 or ed >= S.DEEP_BAR:
            deep_ok = False
    check("G2-satz-deep",
          deep_ok and worst < S.DEEP_BAR,
          "max |M_d/(M_d+5/7) - q*| = %.2e on kz>=69" % worst)
    m136, _ = S.S449.load_mom(136, 200)
    m137, _ = S.S449.load_mom(137, 200)
    br = S.S449.agree_from2(m136, m137, 1e-4)
    dq = abs(S.Q_NS[136] - S.Q_NS[137])
    check("G3-sister-aii-refuted",
          br == 175 and dq > 0.02,
          "agree=%d dq*=%.5f (value law is not m>=2)" % (br, dq))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.masses_of(17)
    r8, _ = S.rho_last(w["mz"], w["border"], 8)
    r18, bw18 = S.rho_last(w["mz"], w["border"], 18)
    r19, _ = S.rho_last(w["mz"], w["border"], 19)
    check("G10-kz17-grade0",
          abs(w["q_g0"] - S.Q_NS[17]) < S.SHALLOW_BAR
          and abs(w["C00"] - w["nu0"] / w["mu0"]) < 1e-15,
          "q_g0=%.8f C00=%.5f b0=%.5f" % (w["q_g0"], w["C00"], w["b0"]))
    check("G11-kz17-rho",
          abs(r8) < S.RHO_PLATEAU and abs(r18) < S.RHO_PLATEAU
          and r19 > 0.1
          and abs(bw18 - (w["Md"] + S.B57)) < 0.02,
          "rho_18=%.2e rho_19=%.4f Bw=%.4f" % (r18, r19, bw18))
    mz = dict(S.V.build_measures(17))
    mz_s = S451.scramble_mz(mz, S.SCRAMBLE_SEED)
    m_s = S451.cheb_moments_xy(mz_s["xp"], mz_s["wp"],
                              mz_s["yn"], mz_s["vn"], 40)
    m18, _ = S.S449.load_mom(18, 40)
    br = S.S449.agree_from2(m_s, m18, 1e-4)
    border = S.S445.smooth_border_atoms(17)[:4]
    qs = [S451.pack_at(mz_s, n, border)["qdag"] for n in (8, 12, 18)]
    std = float(__import__("numpy").nanstd(qs))
    check("G12-scramble",
          br <= 3 and std > 0.01,
          "scr n_stab=%d q std=%.3f" % (br, std))


def main():
    print("verify_plateau_theorem -- r452")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("PLATEAU THEOREM VERIFIED")
        return 0
    print("PLATEAU THEOREM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
