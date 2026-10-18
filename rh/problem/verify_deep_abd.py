#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_deep_abd.py -- machine check of every numbered
lemma in rh/problem/deep_abd.tex (round 446,
REAL / MESH_DOES_NOT_REPAIR / LAST_LIVE_KZ_136 /
K12_ETA_UNDERFLOW / SLICE_FLOOR_STANDS /
COFINAL_ABD_OPEN).

PART A (STANDALONE):
  G1  ABD.ok is all start-of-step sg>0
  G2  sealed REAL pins (first n, eta, dps identity)
  G3  r445 slice floor unchanged

PART B (CONSTRUCTION PINS):
  G10 k=10 float first flip + rel
  G11 k=12 ETA_UNDERFLOW class
  G12 last-live kz=136 / first-dead kz=137
  G13 dead CHI3-15

Exit: "DEEP ABD VERIFIED" iff every gate passed.
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

import deep_abd_probe as S  # noqa: E402
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
    section("PART A  VERDICT / SLICE OVER Q")
    check("G1-ABD-def",
          S.MP10_VERDICT == "REAL"
          and S.K12_CLASS == "ETA_UNDERFLOW"
          and S.LAST_LIVE_KZ == 136,
          "verdict=%s k12=%s last_live=%d"
          % (S.MP10_VERDICT, S.K12_CLASS, S.LAST_LIVE_KZ))
    check("G2-real-pins",
          S.MP10_FIRST == 3788
          and S.MP10_NFLIP_FULL == 115
          and abs(S.MP10_FIRST_ETA + 7.938908159491412e-14) < 1e-24,
          "first=%d n_flip_full=%d eta=%.6e"
          % (S.MP10_FIRST, S.MP10_NFLIP_FULL, S.MP10_FIRST_ETA))
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
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S.load_atoms(S.K10_KZ)
    rows, abort = S.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    flips = [r for r in rows if r["sg"] < 0]
    first = flips[0] if flips else None
    check("G10-k10-float-flip",
          first is not None and first["n"] == S.K10_NF_FLOAT
          and len(flips) == S.K10_NFLIP_FLOAT and abort is None,
          "n_flip=%d first=%s" % (len(flips),
                                 first["n"] if first else None))
    check("G11-k12-class",
          S.K12_CLASS == "ETA_UNDERFLOW"
          and S.K12_NDONE_FLOAT == 12737,
          "class=%s n_done_pin=%d" % (S.K12_CLASS, S.K12_NDONE_FLOAT))
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S.load_atoms(S.LAST_LIVE_KZ)
    rows_l, abort_l = S.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    live = (abort_l is None and all(r["sg"] > 0 for r in rows_l)
            and len(rows_l) == Nw)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S.load_atoms(S.FIRST_DEAD_KZ)
    rows_d, abort_d = S.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    dead = not (abort_d is None and all(r["sg"] > 0 for r in rows_d)
                and len(rows_d) == Nw)
    check("G12-last-live",
          live and dead,
          "kz%d live; kz%d dead" % (S.LAST_LIVE_KZ, S.FIRST_DEAD_KZ))
    a_chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                          want_den=False)
    check("G13-dead-chi",
          a_chi.get("ok") and a_chi["delta"] < 0
          and abs(a_chi["delta"] - S445.DEAD15_D) < 5e-6,
          "CHI3-15 dlt=%.6f" % a_chi.get("delta", float("nan")))


def main():
    print("=" * 72)
    print("verify_deep_abd.py -- round 446")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("DEEP ABD VERIFIED")
        return 0
    print("DEEP ABD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
