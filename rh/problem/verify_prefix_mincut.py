#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_prefix_mincut.py -- machine check of every numbered
lemma in rh/problem/prefix_mincut.tex (round 450,
PREFIX_OBJECT_SPLIT / M2_UNDECIDED / NSTAB_GROWS /
CHI_PREFIX_LIVES / LEAN_IDENT_RFL).

PART A (STANDALONE):
  G1  verdict M2_UNDECIDED
  G2  slice floor still M1
  G3  object-pure n_stab chart is M2
  G4  n_stab growing pin

PART B (CONSTRUCTION PINS):
  G10 kz17 n_stab-pack living, not near full
  G11 CHI3-15 full dead, n=40 living

Exit: "PREFIX MINCUT VERIFIED" iff every gate passed.
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

import prefix_mincut_probe as S  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
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
    section("PART A  VERDICT / FITS / SCALE")
    check("G1-verdict",
          S.VERDICT == "M2_UNDECIDED",
          "verdict=%s" % S.VERDICT)
    sl = S.fit_slice()
    check("G2-slice-M1",
          sl["winner"] == "M1"
          and abs(sl["M1_Rinf"] - S.SLICE_DINF) < 0.002,
          "M1 inf=%.5f" % sl["M1_Rinf"])
    pu = S.fit_pure_a()
    check("G3-pure-M2",
          pu["winner"] == "M2",
          "winner=%s M1=%.5f" % (pu["winner"], pu["M1_Rinf"]))
    mx = S.fit_mixed()
    check("G4-mixed-M2",
          mx["winner"] == "M2",
          "mixed winner=%s" % mx["winner"])
    check("G5-nstab-grows",
          S.SCALE_P > 1.0 and S.NSTAB[500] > S.NSTAB[137],
          "p=%.3f  175 -> %d" % (S.SCALE_P, S.NSTAB[500]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    p = S.pack_nstab(17)
    full = S445.pack(17, engine="numpy", want_den=False)
    check("G10-k5-split",
          p["pos_ok"] and p["n_flip"] == 0
          and abs(p["delta"] - S.D_PRE[17]) < 1e-8
          and abs(p["delta"] - full["delta"]) > 0.05,
          "pre=%.5f full=%.5f" % (p["delta"], full["delta"]))
    chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                        want_den=False)
    c40 = S.pack_chi_at(15, 40)
    check("G11-chi-split",
          chi.get("ok") and chi["n_flip"] == 0
          and abs(chi["qdag"] - S.CHI15_Q_FULL) < 1e-8
          and c40["qdag"] < 1.0,
          "full q=%.6f n40 q=%.6f" % (chi["qdag"], c40["qdag"]))


def main():
    print("=" * 72)
    print("verify_prefix_mincut.py -- round 450")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("PREFIX MINCUT VERIFIED")
        return 0
    print("PREFIX MINCUT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
