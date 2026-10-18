#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_delta_floor.py -- machine check of every numbered
lemma in rh/problem/delta_floor.tex (round 443,
REDUZIERT / CHART_EXACT / SLICE_FLOOR_PREFERRED /
FULL_SEQUENCE_UNSETTLED / KZ16_SELECTED_SPECIFIC /
DEEP_LOCKED / COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  P1 chart: sch = -2/3
  G2  VAC chart: sch = -7/6
  G3  AIC on the frozen k=5,6,7,9 delta pins prefers M1

PART B (CONSTRUCTION PINS):
  G10 w9 (k=4) chart residual 0; delta pin
  G11 kz16 below the slice floor
  G12 dead CHI3-15 delta < 0; k=10 map locked

Exit: "DELTA FLOOR VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import delta_floor_probe as S  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
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
    section("PART A  CHART / FROZEN AIC OVER Q")
    p1 = S417.sch_woodbury_Q_p1()
    vac = S417.sch_woodbury_Q_vac()
    check("G1-Q-P1",
          p1["sch"] == Fr(-2, 3) and p1["sch"] == p1["sch_ch"],
          "sch=-2/3")
    check("G2-Q-VAC",
          vac["sch"] == Fr(-7, 6) and vac["sch"] == vac["sch_ch"],
          "sch=-7/6")
    ks = [5, 6, 7, 9]
    ds = [S.PIN_D[k] for k in ks]
    fit = S421.diagnose_seq(ks, ds)
    check("G3-slice-AIC-M1",
          fit["winner"] == "M1" and fit["M1_Rinf"] > 0.02
          and abs(fit["M1_Rinf"] - S.SLICE_DINF) < 0.001,
          "M1 delta_inf=%.5f DeltaAIC=%.1f"
          % (fit["M1_Rinf"], fit["aic2"] - fit["aic1"]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    a = S.pack(9)
    check("G10-w9-chart",
          a["ok"] and a["chart_err"] < S.CHART_BAR
          and abs(a["delta"] - S.PIN_D[4]) < S.D_BAR,
          "k=4/w9 dlt=%.6f err=%.1e" % (a["delta"], a["chart_err"]))
    a16 = S.pack(16)
    check("G11-kz16-below",
          a16["delta"] < 0.005 and a16["R"] < 0
          and abs(a16["delta"] - S.KZ16_D) < S.D_BAR,
          "kz16 dlt=%.6f R=%.4f" % (a16["delta"], a16["R"]))
    pD = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "CHI3-15")
    kz10, _a, _r = QR.pp_kz(10)
    check("G12-dead-and-deep",
          -float(pD["sch"]) < 0 and kz10 == S.K10_KZ
          and V.window_shape(kz10)[3] == S.K10_NW,
          "dead dlt=%.6f; k=10 kz=%d N=%d locked"
          % (-float(pD["sch"]), kz10, S.K10_NW))


def main():
    print("=" * 72)
    print("verify_delta_floor.py -- round 443")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("DELTA FLOOR VERIFIED")
        return 0
    print("DELTA FLOOR FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
