#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_evolutionary_cert.py -- machine check of every
numbered lemma in rh/problem/evolutionary_certificate.tex
(round 438, A:NOT_FOUND / B:NOT_FOUND / C:NOT_FOUND).

Pins ONLY for exact / machine-verified identities.
Search trajectories are reported by the probe, not pinned
as theorems.

PART A (STANDALONE OVER Q):
  G1  ONES-Y recovers e_0 residual 0
  G2  r375 factorization det K2=-7 exact
  G3  B2 split Rest=0, nneg=1
  G4  nneg=2 detector fires

PART B (CONSTRUCTION PINS):
  G10 w9 C spectrum + canonical cosines
  G11 INVPY uniform min-cos 0.1010 on train
  G12 train/holdout split: fitness tags MAIN-only
  G13 permute nC>=15, scramble nC=21
  G14 illegal a=0 hybrid nC=3 (control)
  G15 selected k=7 nC=0 (canonical cut)

Exit: "EVOLUTIONARY CERT VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import evolutionary_certificate_probe as S  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402

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
    section("PART A  Q TOYS")
    A = S.toy_A_psi()
    check("G1-ONES-minus-Y",
          A["exact"] and A["cos"] >= 1.0 - 1e-15,
          "cos=%.3e" % A["cos"])
    B = S.toy_B_lp()
    check("G2-r375-Q",
          B["ok"],
          "detK=%s gamma=%s" % (B["detK"], B["gamma"]))
    B2 = S.toy_B2()
    check("G3-B2-Q-split",
          B2["ok"],
          "Rest=%.1e nneg=%d" % (B2["res"], B2["nneg"]))
    okC, n2 = S.toy_C_detector()
    check("G4-nneg2-detector", okC, "nneg=%d" % n2)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w9 = S.pack_main(9)
    c_ones = S.cosabs(w9["ones"], w9["psi"])
    c_nyq = S.cosabs(w9["nyq"], w9["psi"])
    c_vtop = S.cosabs(w9["vtop"], w9["psi"])
    check("G10-w9-C-and-canonical-cos",
          w9["nC"] == 1
          and abs(w9["Cmin"] - S.W9_CMIN) < 5e-6
          and abs(w9["C2"] - S.W9_C2) < 5e-8
          and abs(c_ones - S.W9_ONES) < 5e-4
          and abs(c_nyq - S.W9_NYQ) < 5e-4
          and abs(c_vtop - S.W9_VTOP) < 5e-4,
          "Cmin=%.6f C2=%.10f ones=%.4f nyq=%.4f vtop=%.4f"
          % (w9["Cmin"], w9["C2"], c_ones, c_nyq, c_vtop))
    train = [S.pack_main(kz) for kz in S.TRAIN_KZ]
    inv = ("t", 3)
    f_inv, cs = S.tree_cos(inv, train)
    check("G11-INVPY-uniform",
          abs(f_inv - S.INVPY_MIN) < 5e-3 and f_inv < 0.2,
          "min-cos=%.4f %s" % (f_inv, " ".join("%.4f" % c for c in cs)))
    tags = {d["tag"] for d in train}
    check("G12-train-MAIN-only",
          tags == {"MAIN-9", "MAIN-18", "MAIN-20"},
          str(sorted(tags)))
    mzP = P1.reweight(train[0]["mz"], "permute", 43810)
    dP = S.feat_pack(mzP)
    dS = S.feat_pack(HM.scramble_mz())
    check("G13-kills",
          dP["nC"] >= S.PERM_NC_LO and dS["nC"] == S.SCR_NC,
          "PERM nC=%d SCR nC=%d" % (dP["nC"], dS["nC"]))
    uu, ww, _, _ = DMF.chi_window_comb(9, DMF.Q_CHI3)
    mz_bad = DMF.chi_build_measures(9, uu, ww, 0.0, DMF.LPQ3)
    d_bad = S.feat_pack(mz_bad)
    check("G14-illegal-a0-control",
          d_bad["nC"] == S.CHI3_A0_NC,
          "nC=%d" % d_bad["nC"])
    dsel = S.pack_main(S.HOLDOUT_SEL_KZ)
    check("G15-selected-k7-canonical-nC0",
          dsel["nC"] == 0 and dsel["Cmin"] >= 1.0 - 1e-6,
          "kz=43 nC=%d Cmin=%.8f C2=%.10f"
          % (dsel["nC"], dsel["Cmin"], dsel["C2"]))


def main():
    print("=" * 72)
    print("verify_evolutionary_cert.py -- round 438")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("EVOLUTIONARY CERT VERIFIED")
        return 0
    print("EVOLUTIONARY CERT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
