#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_border_mass.py -- machine check of every numbered
lemma in rh/problem/border_mass.tex (round 453,
BOUND_PROVED / MASS_CLASSICAL_REDUCED_GROWING / RACE_WON).

PART A (STANDALONE):
  G1  verdicts
  G2  exact identity q = S_{n-1}/B_w on kz17 plateau + cliff
  G3  sister cliff predicted by g = rho/B_w

PART B (CONSTRUCTION PINS):
  G10 M_d = signed MAIN on kz136/137; sister split is N
  G11 race n=20 on-plateau err << margin
  G12 scramble: border M_d definition stands

Exit: "BORDER MASS VERIFIED" iff every gate passed.
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

import border_mass_probe as S  # noqa: E402
import plateau_theorem_probe as S452  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402

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
    section("PART A  VERDICT / IDENTITY / CLIFF")
    check("G1-verdict",
          S.VERDICT_A == "BOUND_PROVED"
          and S.VERDICT_B == "MASS_CLASSICAL_REDUCED_GROWING"
          and S.VERDICT_C == "RACE_WON",
          "%s / %s / %s" % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    w = S452.masses_of(17)
    d18 = S.schur_bits(w["mz"], w["border"], 18)
    d19 = S.schur_bits(w["mz"], w["border"], 19)
    check("G2-kz17-identity",
          abs(d18["q"] - d18["q_S"]) < S.ID_BAR
          and abs(d19["q"] - d19["q_S"]) < S.ID_BAR
          and abs(d19["dlt"] - d19["dlt_id"]) < S.ID_BAR,
          "n=18/19 |q-S/Bw| < 1e-12")
    w136 = S452.masses_of(136)
    d176 = S.schur_bits(w136["mz"], w136["border"], 176)
    g = d176["rhoN"] / d176["Bw"]
    dq = d176["q"] - S.Q_NS[136]
    check("G3-sister-cliff-g",
          abs(dq - g) < 1e-5 and d176["rhoN"] > 0.02,
          "kz136 n=176 dq=%.6f g=%.6f rho=%.4f" % (dq, g, d176["rhoN"]))


def part_b():
    section("PART B  MASS / RACE / SCRAMBLE")
    w136, w137 = S452.masses_of(136), S452.masses_of(137)
    check("G10-sister-mass-N",
          abs(w136["Md"] - w136["signed"]) < 1e-12
          and abs(w137["Md"] - w137["signed"]) < 1e-12
          and w137["N"] > 4 * w136["N"]
          and w137["Md"] - w136["Md"] > 1.5,
          "Md 136/137=%.4f/%.4f N=%d/%d"
          % (w136["Md"], w137["Md"], w136["N"], w137["N"]))
    w = S452.masses_of(136)
    d = S.schur_bits(w["mz"], w["border"], 20)
    err = abs(d["rhoN"]) / d["Bw"]
    marg = S.B57 / (w["Md"] + S.B57)
    check("G11-race-n20",
          err / marg < S.RACE_ON_BAR,
          "err/margin=%.2e" % (err / marg))
    mz = dict(S.V.build_measures(17))
    mz_s = S451.scramble_mz(mz, S.SCRAMBLE_SEED)
    border = S.S445.smooth_border_atoms(17)[:4]
    import numpy as np
    bxs, bws, bys, bvs = (np.asarray(x, float) for x in border)
    Md = float(bws.sum() - bvs.sum())
    sig_s = float(np.asarray(mz_s["wp"]).sum()
                  - np.asarray(mz_s["vn"]).sum())
    check("G12-scramble-mass",
          abs(Md - S452.masses_of(17)["Md"]) < 1e-12
          and abs(sig_s) > 0.5,
          "Md=%.4f scr-signed=%.4f" % (Md, sig_s))


def main():
    print("verify_border_mass -- r453")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("BORDER MASS VERIFIED")
        return 0
    print("BORDER MASS FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
