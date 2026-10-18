#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_exact_band.py -- machine check of every numbered
lemma in rh/problem/exact_band.tex (round 448,
NOT_COFINAL / COMMENSURABILITY_REFUTED /
NEXT_ODD_FAILS / ZETA_CHAIN_DEATH /
LAST_LIVE_FLOAT_136).

PART A (STANDALONE):
  G1  band NOT_COFINAL, family NEXT_ODD_FAILS
  G2  kz197 chain-death coordinates
  G3  r445 slice floor unchanged

PART B (CONSTRUCTION PINS):
  G10 kz136 float lives
  G11 kz230 float first=1818
  G12 next-odd k=9 lives, k=10 dies
  G13 dead CHI3-15 positive chain q>1

Exit: "EXACT BAND VERIFIED" iff every gate passed.
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

import exact_band_probe as S  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402

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
    section("PART A  VERDICT / ANATOMY / SLICE")
    check("G1-not-cofinal",
          S.BAND_VERDICT == "NOT_COFINAL"
          and S.FAMILY_STATUS == "NEXT_ODD_FAILS"
          and S.COMMENSURABILITY == "REFUTED"
          and S.KZ197_DEATH == "ZETA_CHAIN_DEATH",
          "band=%s family=%s comm=%s death=%s"
          % (S.BAND_VERDICT, S.FAMILY_STATUS,
             S.COMMENSURABILITY, S.KZ197_DEATH))
    check("G2-kz197-coords",
          S.KZ197_FIRST == 3788
          and S.KZ197_QN_PACK < 0
          and S.KZ197_ZLOC < 0.1
          and S.KZ197_Z > 1.0
          and 0.9 < S.KZ197_NN < 0.95,
          "nf=%d qN=%.4f |Zloc|=%.4f |Z|=%.4f n/N=%.3f"
          % (S.KZ197_FIRST, S.KZ197_QN_PACK,
             S.KZ197_ZLOC, S.KZ197_Z, S.KZ197_NN))
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
    r136 = S.float_first(136)
    check("G10-kz136-live",
          r136["pos_ok"] and r136["Nw"] == S.KZ136_NW,
          "kz136 N=%d pos=%s" % (r136["Nw"], r136["pos_ok"]))
    r230 = S.float_first(230)
    check("G11-kz230-float",
          r230["first"] == S.KZ230_FIRST,
          "float first=%s" % r230["first"])
    kz9, _, _ = QR.pp_kz(9)
    # next-odd k=9, k=10
    zk9, _p9, _ = S.next_odd_after_pow2(9)
    zk10, _p10, _ = S.next_odd_after_pow2(10)
    n9 = S.float_first(zk9)
    n10 = S.float_first(zk10)
    check("G12-next-odd-wall",
          n9["pos_ok"] and (not n10["pos_ok"]),
          "k=9 kz=%d live; k=10 kz=%d first=%s"
          % (zk9, zk10, n10["first"]))
    a_chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                          want_den=False)
    check("G13-dead-chi-positive",
          a_chi.get("ok") and a_chi["n_flip"] == 0
          and a_chi["qdag"] > 1.0
          and abs(a_chi["qdag"] - S.CHI15_QDAG) < 1e-8,
          "CHI3-15 n_flip=0 q=%.6f" % a_chi.get("qdag", float("nan")))
    _ = kz9  # kept for pin surface


def main():
    print("=" * 72)
    print("verify_exact_band.py -- round 448")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("EXACT BAND VERIFIED")
        return 0
    print("EXACT BAND FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
