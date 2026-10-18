#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_nstab_transition.py -- machine check of every numbered
lemma in rh/problem/nstab_transition.tex (round 451,
TRANSITION_SMOOTH / RES_MISMATCH / PREFIX_Q_PLATEAU).

PART A (STANDALONE):
  G1  verdict TRANSITION_SMOOTH
  G2  RES_MISMATCH: n_stab/n_res < 0.12 on pins
  G3  PREFIX_Q_PLATEAU: q at n_stab < 1, pin match

PART B (CONSTRUCTION PINS):
  G10 kz17 n_stab=18, n_res=191
  G11 kz17 q-plateau then cliff at n=19
  G12 scramble n_stab collapses, q not plateau

Exit: "NSTAB TRANSITION VERIFIED" iff every gate passed.
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

import nstab_transition_probe as S  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
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
    section("PART A  VERDICT / n_res / PLATEAU")
    check("G1-transition-smooth",
          S.VERDICT == "TRANSITION_SMOOTH"
          and S.VERDICT_RES == "RES_MISMATCH"
          and S.VERDICT_Q == "PREFIX_Q_PLATEAU",
          "verdict=%s / %s / %s" % (S.VERDICT, S.VERDICT_RES, S.VERDICT_Q))
    ratios = [S.NSTAB[kz] / S.NRES[kz] for kz in S.NSTAB]
    check("G2-res-mismatch",
          max(ratios) < 0.12 and min(ratios) > 0.005,
          "n_stab/n_res in [%.4f, %.4f]" % (min(ratios), max(ratios)))
    okq = all(S.Q_NS[kz] < 1.0 for kz in S.Q_NS)
    check("G3-prefix-q-plateau-pins",
          okq and S.Q_NS[17] < 0.79 and S.Q_NS[136] < 0.88,
          "q*(17)=%.6f q*(136)=%.6f all q*<1" % (S.Q_NS[17], S.Q_NS[136]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    ns, nw = S.S449.n_stab(17, S.NEIGH[17], 80)
    nr, ngrid, Nw, mz = S.n_res_of(17)
    check("G10-k5-nstab-nres",
          ns == 18 and nw == 96 and abs(nr - 191.0) < 0.6
          and abs(ngrid - 191.0) < 0.6,
          "n_stab=%d n_res=%.1f N=%d" % (ns, nr, Nw))
    mz = dict(V.build_measures(17))
    mz["kz"] = 17
    border = S445.smooth_border_atoms(17)[:4]
    p18 = S.pack_at(mz, 18, border)
    p19 = S.pack_at(mz, 19, border)
    check("G11-k5-q-cliff",
          abs(p18["qdag"] - S.Q_NS[17]) < 1e-8
          and abs(p19["qdag"] - p18["qdag"]) > 0.04
          and p18["residual"] < 1e-12,
          "q18=%.8f q19=%.8f res=%.1e" % (
              p18["qdag"], p19["qdag"], p18["residual"]))
    mz_s = S.scramble_mz(mz)
    br = S.n_stab_scrambled(mz_s, 18, 80)
    qs = [S.pack_at(mz_s, n, border)["qdag"] for n in (8, 12, 16, 18)]
    import numpy as np
    std = float(np.std(qs))
    check("G12-scramble",
          br <= 3 and std > 0.01,
          "scr n_stab=%d q-std=%.3f" % (br, std))


def main():
    print("=" * 72)
    print("verify_nstab_transition.py -- round 451")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("NSTAB TRANSITION VERIFIED")
        return 0
    print("NSTAB TRANSITION FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
