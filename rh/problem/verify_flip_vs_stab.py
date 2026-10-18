#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_flip_vs_stab.py -- machine check of every numbered
lemma in rh/problem/flip_vs_stab.tex (round 449,
TAIL_ONLY / PREFIX_LIVE / SLICE_FLOOR_STANDS /
MINCUT_IS_PREFIX).

PART A (STANDALONE):
  G1  verdict TAIL_ONLY
  G2  n_stab < flip on pinned deep windows
  G3  r445 slice floor unchanged

PART B (CONSTRUCTION PINS):
  G10 kz17 n_stab=18 (comb-stab anchor)
  G11 kz197 prefix-80 living
  G12 dead CHI3-15 n_flip=0 q>1

Exit: "FLIP VS STAB VERIFIED" iff every gate passed.
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

import flip_vs_stab_probe as S  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

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
    section("PART A  VERDICT / TABLE / SLICE")
    check("G1-tail-only",
          S.VERDICT == "TAIL_ONLY",
          "verdict=%s" % S.VERDICT)
    ok = all(S.FLIPS[kz] is None or S.FLIPS[kz] > S.NSTAB[kz]
             for kz in S.FLIPS)
    check("G2-flips-past-nstab",
          ok,
          "137:%d<%d 170:%d<%d 197:%d<%d 230:%d<%d 500:%d<%d"
          % (S.NSTAB[137], S.FLIPS[137], S.NSTAB[170], S.FLIPS[170],
             S.NSTAB[197], S.FLIPS[197], S.NSTAB[230], S.FLIPS[230],
             S.NSTAB[500], S.FLIPS[500]))
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    fit = S421.diagnose_seq(ks, ds)
    check("G3-slice-floor-stands",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - S445.SLICE_DINF) < 0.002,
          "M1 inf=%.5f" % fit["M1_Rinf"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    ns, nw = S.n_stab(17, (18, 26), 80)
    check("G10-k5-anchor",
          ns == S.NSTAB[17] and nw == 96,
          "n_stab=%d N=%d" % (ns, nw))
    p = S.pack_prefix80(197)
    check("G11-kz197-prefix80",
          p["pos_ok"] and p["n_flip"] == 0
          and abs(p["delta"] - S.D80[197]) < 1e-5,
          "d=%.5f n_flip=0" % p["delta"])
    chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                        want_den=False)
    check("G12-dead-chi",
          chi.get("ok") and chi["n_flip"] == 0
          and abs(chi["qdag"] - S.CHI15_Q) < 1e-8,
          "CHI3-15 n_flip=0 q=%.6f" % chi.get("qdag", float("nan")))


def main():
    print("=" * 72)
    print("verify_flip_vs_stab.py -- round 449")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("FLIP VS STAB VERIFIED")
        return 0
    print("FLIP VS STAB FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
