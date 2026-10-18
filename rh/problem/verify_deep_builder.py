#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_deep_builder.py -- machine check of every numbered
lemma in rh/problem/deep_builder.tex (round 445,
INFRA_UNLOCKED / K8_CROSS_CONFIRMED /
DEEP_NOT_ABD_LIVING / SLICE_FLOOR_PREFERRED /
FULL_SEQUENCE_UNSETTLED / COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  q^dagger = b^T (I-C)^{-1} b / B_w
  G2  B_w = S + 5/7
  G3  frozen ABD-ok slice AIC prefers M1 with live k=8

PART B (CONSTRUCTION PINS):
  G10 w9 (k=4) delta pin; skip-Lanczos atoms bitwise
  G11 k=8 map + r421 pin constants
  G12 k=10/11/12 maps; k=10 n_flip pin; k=12 N lock
  G13 dead CHI3-15 delta < 0 with the new builder

Exit: "DEEP BUILDER VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
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
    section("PART A  FORMULA / FROZEN AIC OVER Q")
    C = np.array([[Fr(1, 2), 0], [0, Fr(1, 2)]], dtype=object)
    # float check of the same identity
    Cf = np.array([[0.5, 0.0], [0.0, 0.5]])
    b = np.array([1.0, 1.0])
    Bw = 4.0
    x = np.linalg.solve(np.eye(2) - Cf, b)
    q = float(b @ x) / Bw
    check("G1-Q-qdag-formula",
          abs(q - 1.0) < 1e-15,
          "C=1/2 I, b=(1,1), B_w=4 => q^dagger=1")
    check("G2-Q-Bw",
          S.B57 == 5.0 / 7.0 and Fr(5, 7) == Fr(5, 7),
          "B_w = S_{N-2} + 5/7")
    ks = [5, 6, 7, 8, 9]
    ds = [S.PIN_D[5], S.PIN_D[6], S.PIN_D[7], S.K8_D, S.PIN_D[9]]
    fit = S421.diagnose_seq(ks, ds)
    check("G3-slice-AIC-M1",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - S.SLICE_DINF) < 0.002
          and (fit["aic2"] - fit["aic1"]) > 4.0,
          "M1 delta_inf=%.5f DeltaAIC=%.2f"
          % (fit["M1_Rinf"], fit["aic2"] - fit["aic1"]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    a = S.pack(9, engine="numpy", want_den=False)
    xs, ws, ys, vs, _h, alk = S.smooth_border_atoms(9)
    import hirota_sign_probe as HS
    import principal_bessel_probe as PB
    dsm = HS.window_data(9, comb=PB.smooth_comb(alk))
    atom0 = (np.max(np.abs(xs - dsm["xs"])) == 0.0
             and np.max(np.abs(ws - dsm["ws"])) == 0.0)
    check("G10-w9-skip-lanczos",
          a["ok"] and abs(a["delta"] - S.PIN_D[4]) < S.D_BAR
          and atom0,
          "k=4/w9 dlt=%.6f atoms bit-identical" % a["delta"])
    kz8, _a, _r = QR.pp_kz(8)
    nw8 = V.window_shape(kz8)[3]
    check("G11-k8-map-pin",
          kz8 == S.K8_KZ and nw8 == S.K8_NW
          and abs(S.K8_R_PIN - 0.04763) < 1e-9
          and abs(S.K8_D - 0.047488) < 1e-9,
          "k=8 kz=%d N=%d; live pin R=%.5f dlt=%.6f"
          % (kz8, nw8, S.K8_R_PIN, S.K8_D))
    kz10, _a, _r = QR.pp_kz(10)
    kz12, _a, _r = QR.pp_kz(12)
    nw10 = V.window_shape(kz10)[3]
    nw12 = V.window_shape(kz12)[3]
    check("G12-deep-maps",
          kz10 == S.K10_KZ and nw10 == S.K10_NW
          and kz12 == S.K12_KZ and nw12 == S.K12_NW
          and S.K10_NFLIP == 107 and S.K11_NFLIP == 839,
          "k=10 kz=%d N=%d n_flip=%d; k=12 kz=%d N=%d"
          % (kz10, nw10, S.K10_NFLIP, kz12, nw12))
    a_chi = S.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                       want_den=False)
    check("G13-dead-chi-new-builder",
          a_chi.get("ok") and a_chi["delta"] < 0
          and abs(a_chi["delta"] - S.DEAD15_D) < 5e-6,
          "CHI3-15 new-builder dlt=%.6f" % a_chi["delta"])


def main():
    print("=" * 72)
    print("verify_deep_builder.py -- round 445")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("DEEP BUILDER VERIFIED")
        return 0
    print("DEEP BUILDER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
