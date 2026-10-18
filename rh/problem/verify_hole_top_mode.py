#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_hole_top_mode.py -- machine check of every
numbered lemma in rh/problem/hole_top_mode.tex
(round 413, TOP_MODE_REFUTED).

PART A (STANDALONE OVER Q):
  G1  Lagrange identity on deg ≤ q-2, three bases
  G2  GS last = formula π = c/(ω P')
  G3  constructor audit (no eig/SVD/target)
  G4  toy HTM holds (positive control)

PART B (CONSTRUCTION PINS):
  G10 w9 corr(v_top, C-ev0) in (0.65, 0.72), primary FAIL
  G11 leftover σ > 1; QD mass ratio > 1
  G12 permute/scramble break; unsigned P' useless
  G13 chi9 trivial hold / dead-15 razor
  G14 core P1 refuted (hold ≤ 6 of 28)

Exit: per-gate PASS/FAIL and the final line
"HOLE TOP MODE VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named refutation.
"""
from __future__ import annotations

import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import hole_top_mode_probe as H  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
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
    section("PART A  FORMULA / CONSTRUCTOR / TOY OVER Q")
    H.CHECKS.clear()
    H.part_satz()
    oks = dict(H.CHECKS)
    check("G1-lagrange-Q", oks.get("G01-lagrange-identity-three-bases",
                                    False))
    check("G2-GS-formula-Q", oks.get("G02-GS-three-bases-match-formula",
                                     False)
          and oks.get("G03-formula-pi-om-Pprime-is-one", False))
    leak = H.scope_audit("v_top_from_Y")
    check("G3-constructor-clean", leak == [],
          "no eig/SVD/target" if not leak else "; ".join(leak))
    check("G4-toy-HTM", oks.get("G04-toy-HTM-holds", False))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    d = H.pack_htm(mz)
    import dual_intertwiner_probe as DI
    pk = DI.pack_C(mz)
    evC = np.linalg.eigh(pk["C"])[1][:, 0]
    cC = H.corr_abs(d["v"], evC)
    check("G10-w9-corr-and-primary-fail",
          H.W9_CORR_LO <= cC <= H.W9_CORR_HI
          and d["h"]["lmin"] <= H.W9_LMIN_HI
          and d["h"]["n_over"] >= 1
          and H.W9_SMAX_LO <= d["h"]["smax"] <= H.W9_SMAX_HI,
          "corr=%.4f λ_min=%.6f n_over=%d σ_max=%.6f"
          % (cC, d["h"]["lmin"], d["h"]["n_over"], d["h"]["smax"]))
    check("G11-leftover-and-QD-mass",
          d["h"]["smax"] > 1.0
          and H.W9_MASS_LO <= d["mass"] <= H.W9_MASS_HI,
          "σ_max(v^⊥)=%.6f  mass_X/Y=%.6f"
          % (d["h"]["smax"], d["mass"]))
    dP = H.pack_htm(P1.reweight(mz, "permute", 1000))
    dS = H.pack_htm(HM.scramble_mz())
    y = np.asarray(d["g"]["yn"], float)
    D = y[:, None] - y[None, :]
    np.fill_diagonal(D, 1.0)
    logP = np.sum(np.log(np.maximum(np.abs(D), 1e-300)), axis=1)
    logw = 0.5 * np.log(np.maximum(d["g"]["wY"], 1e-300))
    logv = -logw - logP
    logv -= float(np.max(logv))
    v_abs = np.exp(logv)
    v_abs /= np.linalg.norm(v_abs)
    h_abs = H.htm_of(d["g"]["T0"], v_abs)
    check("G12-kills",
          dP["h"]["n_over"] >= H.PERM_NOVER_LO
          and dS["h"]["n_over"] >= H.SCR_NOVER_LO
          and h_abs["smax"] >= d["g"]["opnorm"] - 0.01,
          "PERM n_over=%d SCR n_over=%d |P'| σ_max=%.6f"
          % (dP["h"]["n_over"], dS["h"]["n_over"], h_abs["smax"]))
    dL = H.pack_htm(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = H.pack_htm(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G13-chi",
          H.holds(dL["h"]) and dL["g"]["opnorm"] < 1.0
          and H.holds(dD["h"]) and dD["g"]["opnorm"] > 1.0,
          "chi9 ||T||=%.6f HOLD; dead-15 ||T||=%.6f razor HOLD"
          % (dL["g"]["opnorm"], dD["g"]["opnorm"]))
    p1_hold = p1_n = pd_hold = pd_n = 0
    for kz in V.admissible_indices():
        dd = H.pack_htm(V.build_measures(kz))
        ok = H.holds(dd["h"])
        if dd["g"]["opnorm"] <= 1.0:
            pd_n += 1
            pd_hold += int(ok)
        else:
            p1_n += 1
            p1_hold += int(ok)
    check("G14-core-P1-refuted",
          p1_n + pd_n == H.CORE_N and pd_hold == H.PD_N
          and p1_hold <= H.P1_HOLD_HI
          and (p1_n - p1_hold) >= H.P1_BREAK_LO,
          "P1 hold %d/%d; PD %d/%d"
          % (p1_hold, p1_n, pd_hold, pd_n))


def main():
    print("=" * 72)
    print("verify_hole_top_mode.py -- round 413")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("HOLE TOP MODE VERIFIED")
        return 0
    print("HOLE TOP MODE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
