#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_source_weyl.py -- machine check of every numbered
lemma in rh/problem/source_weyl_energy.tex (round 399,
source-pure Weyl energy, REFUTED as a decay).

PART A (STANDALONE):
  G1  Fractions stencil h0=2/L, h_{pm 1}=-1/L, mass 0
  G2  Circulant convolution = Laplacian / L over Q
  G3  cd_energy_of has no eigvalsh / det / q_N

PART B (CONSTRUCTION PINS):
  G10 w9 dcent = Fejer odot dP, Dirichlet interpolant
  G11 w9 Fejer Laplacian, C0=C1=0, E in pin
  G12 kz18 and kz52 Dirichlet
  G13 scramble E > 1.2 x MAIN
  G14 two-period HHI comb at m=S
  G15 dead chi3-15 and living chi3-9 both O(1)
  G16 selected k=4 E < k=6 E (grows)
  G17 MVT crude/E >= 100 on w9

Exit: per-gate PASS/FAIL and the final line
"SOURCE WEYL VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named refutation.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import source_weyl_energy_probe as H  # noqa: E402
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
    section("PART A  STENCIL / LAPLACIAN / FIREWALL")
    L = 6
    h0, h1 = Fr(2, L), Fr(-1, L)
    check("G1-stencil-Q",
          h0 == Fr(1, 3) and h1 == Fr(-1, 6) and h0 + 2 * h1 == 0,
          "h0=%s h1=%s" % (h0, h1))
    a = [Fr(2), Fr(1), Fr(0), Fr(3), Fr(0), Fr(1)]
    ok = True
    for i in range(L):
        s = h0 * a[i] + h1 * a[(i - 1) % L] + h1 * a[(i + 1) % L]
        lap = 2 * a[i] - a[(i - 1) % L] - a[(i + 1) % L]
        if s - lap / L != 0:
            ok = False
    check("G2-laplacian-Q", ok, "6-cycle convolution = Delta/L")
    okf, det = H.energy_fn_audit()
    check("G3-no-forbidden", okf, det)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    P = H.pack_kz(9)
    ddev = H.dirichlet_maxdev(P)
    check("G10-w9-representation",
          P["dcent_dev"] < H.ID_BAR and ddev < H.DIR_BAR,
          "dcent dev=%.3e Dirichlet dev=%.3e" % (P["dcent_dev"], ddev))
    check("G11-w9-Laplacian-edge-E",
          P["lap_dev"] < H.LAP_BAR
          and abs(P["C0"]) < 1e-12 and abs(P["C1"]) < 1e-12
          and H.W9_E_LO <= P["E_bulk"] <= H.W9_E_HI,
          "lap=%.3e E=%.6g C0=%.3e" % (P["lap_dev"], P["E_bulk"], P["C0"]))
    d18 = H.dirichlet_maxdev(H.pack_kz(18), js=[1, 2, 5])
    d52 = H.dirichlet_maxdev(H.pack_kz(52), js=[1, 2, 5])
    check("G12-two-windows-Dirichlet",
          d18 < 1e-10 and d52 < 1e-10,
          "kz18 %.3e kz52 %.3e" % (d18, d52))
    scr = H.scramble_energy()
    check("G13-scramble",
          scr["E_bulk"] >= H.SCR_RATIO * P["E_bulk"],
          "SCR=%.4g MAIN=%.4g" % (scr["E_bulk"], P["E_bulk"]))
    tp = H.two_period_hhi(21)
    check("G14-two-period",
          tp["hhi"] >= H.TP_HHI_FLOOR and tp["arg"] == 21,
          "HHI=%.3f m=%d" % (tp["hhi"], tp["arg"]))
    dchi = H.chi_energy(15, DMF.Q_CHI3, DMF.LPQ3)
    lchi = H.chi_energy(9, DMF.Q_CHI3, DMF.LPQ3)
    check("G15-chi-both-O1",
          H.CHI_E_LO <= dchi["E_bulk"] <= H.CHI_E_HI
          and H.CHI_E_LO <= lchi["E_bulk"] <= H.CHI_E_HI,
          "dead=%.4g live=%.4g" % (dchi["E_bulk"], lchi["E_bulk"]))
    e4 = H.pack_selected(4)["E_bulk"]
    e6 = H.pack_selected(6)["E_bulk"]
    check("G16-selected-grows",
          e6 > e4 > 0.05,
          "k4=%.4g k6=%.4g" % (e4, e6))
    ratio, xt, s2 = H.mvt_ratio(P)
    check("G17-MVT-short",
          ratio >= H.MVT_RATIO_FLOOR,
          "crude/E=%.4g X/T=%.3g" % (ratio, xt))


def main():
    print("=" * 72)
    print("verify_source_weyl.py -- round 399")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("SOURCE WEYL VERIFIED")
        return 0
    print("SOURCE WEYL FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
