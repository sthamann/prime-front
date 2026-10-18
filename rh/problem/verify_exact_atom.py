#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_exact_atom.py -- machine check of every numbered
lemma in rh/problem/exact_atom.tex (round 447,
EXACT_DEAD / ATOM_ULP_ONLY / FLIP_STABLE_3788 /
BAND_ENDS / SLICE_FLOOR_STANDS /
THIS_FAMILY_FREQUENTLY_FALSIFIED).

PART A (STANDALONE):
  G1  verdict EXACT_DEAD, first n=3788
  G2  atom-ulp pins
  G3  r445 slice floor unchanged

PART B (CONSTRUCTION PINS):
  G10 k=5 exact-atom counts + rel
  G11 k=5 exact-atom chain lives
  G12 k=10 float first flip still 3788
  G13 dead CHI3-15

Exit: "EXACT ATOM VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import exact_atom_probe as S  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
import deep_abd_probe as S446  # noqa: E402
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
    section("PART A  VERDICT / SLICE")
    check("G1-exact-dead",
          S.VERDICT == "EXACT_DEAD"
          and S.MP10_FIRST == 3788
          and S.MP10_NFLIP == 115,
          "verdict=%s first=%d n_flip=%d"
          % (S.VERDICT, S.MP10_FIRST, S.MP10_NFLIP))
    check("G2-atom-ulp",
          S.ATOM_REL_X < 1e-15 and S.ATOM_REL_W < 1e-13
          and S.DIV_N == 218,
          "rel_x=%.3e rel_w=%.3e div_n=%d"
          % (S.ATOM_REL_X, S.ATOM_REL_W, S.DIV_N))
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    fit = S421.diagnose_seq(ks, ds)
    check("G3-slice-floor-stands",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - S445.SLICE_DINF) < 0.002,
          "M1 inf=%.5f (r445 slice unchanged)"
          % fit["M1_Rinf"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    pk = S.exact_pack(S.K5_KZ, 50)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(S.K5_KZ)
    rx, nx, nxf = S.rel_max(pk["xp"], xs)
    check("G10-k5-atoms",
          nx == nxf and pk["Nw"] == S.K5_NW and rx < 1e-14,
          "nX=%d rel_x=%.3e" % (nx, rx))
    ch = S.mp_chain_native(*S.pack_as_lists(pk)[:8], Nw, dps=50,
                           progress_every=0)
    check("G11-k5-chain",
          ch["pos_ok"] and ch["n_flip"] == 0,
          "pos_ok=%s n_flip=%d" % (ch["pos_ok"], ch["n_flip"]))
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(S.K10_KZ)
    rows, abort = S446.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    flips = [r for r in rows if r["sg"] < 0]
    check("G12-k10-float-still-3788",
          flips and flips[0]["n"] == 3788 and abort is None,
          "float first=%s n_flip=%d" % (
              flips[0]["n"] if flips else None, len(flips)))
    a_chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                          want_den=False)
    check("G13-dead-chi",
          a_chi.get("ok") and a_chi["delta"] < 0
          and abs(a_chi["delta"] - S445.DEAD15_D) < 5e-6,
          "CHI3-15 dlt=%.6f" % a_chi.get("delta", float("nan")))


def main():
    print("=" * 72)
    print("verify_exact_atom.py -- round 447")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("EXACT ATOM VERIFIED")
        return 0
    print("EXACT ATOM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
