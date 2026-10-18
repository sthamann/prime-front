#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_isolation_lemma.py -- machine check of every numbered
lemma in rh/problem/isolation_lemma.tex (round 396, isolation
lemma REFUTED).

PART A (STANDALONE):
  G1  w9 has exactly 2 gap-1 pairs
  G2  folded consecutive integers n=2..64 are not adjacent
  G3  PNT-free packing du<2D is O(n_atom) not o(n_nu)
  G4  wrap(2,3,4) is isolated (pairs=0, maxrun=1)
  G5  Dirichlet hull at sep 2 is still >>1

PART B (CONSTRUCTION PINS):
  G10 wrap234 h=40 is NOT uniformly IN
  G11 wrap(1,2,3) dies on pair density; randF1 pair-rich OUT
  G12 1010 isolated has lambda>1; wrap234 gersh>1
  G13 two-period lam22>1; scramble pair-rich
  G14 inject k=10 OUT; fat tail does not kill

Exit: per-gate PASS/FAIL and the final line
"ISOLATION LEMMA VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named refutation.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import isolation_lemma_probe as I  # noqa: E402
import three_gap_mask_probe as T  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import coherence_assist_probe as CA  # noqa: E402

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
    section("PART A  PAIRS / PACKING / HULL")
    _d, _N, _xf, _w, idx = T.mask_idx(9)
    npair, locs = I.n_pairs_of(idx)
    check("G1-w9-two-pairs",
          npair == 2 and locs == [(13, 14), (67, 68)],
          "pairs=%d locs=%s" % (npair, locs))
    st = I.atom_fold_stats(9)
    adj = I.folded_consec_adj(2, 64, st["L"])
    check("G2-small-n-not-adjacent",
          adj == 0,
          "folded consec n=2..64 adj=%d" % adj)
    check("G3-packing-O-natom",
          st["n_close"] >= I.PACK_CLOSE_FLOOR,
          "du<2D close=%d/%d" % (st["n_close"], st["n_atom"] - 1))
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    m234 = T.wrap_kgap(S40, (2, 3, 4), 7)
    f1, mx = T.f1_of(m234)
    np234, _ = I.n_pairs_of(np.where(m234)[0])
    check("G4-wrap234-isolated",
          f1 and mx <= 1 and np234 == 0,
          "maxrun=%d pairs=%d" % (mx, np234))
    env2 = 1.0 / abs(math.sin(2.0 * math.pi / S40))
    check("G5-hull-still-huge",
          env2 > 5.0,
          "1/sin(dth)=%.2f" % env2)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    n_in = sum(int(T.occ_fejer(
        xf40, wf40, T.wrap_kgap(S40, (2, 3, 4), s), 40)[0])
               for s in range(12))
    check("G10-wrap234-h40-not-uniform",
          n_in <= I.WRAP40_IN_BAR and n_in < 12,
          "IN %d/12" % n_in)

    m123 = T.wrap_kgap(S40, (1, 2, 3), 7)
    mR = T.random_f1_mask(S40, 0.45, 2)
    ok123, _, j123 = T.occ_fejer(xf40, wf40, m123, 40)
    okR, _, jR = T.occ_fejer(xf40, wf40, mR, 40)
    np123 = I.n_pairs_of(np.where(m123)[0])[0]
    npR = I.n_pairs_of(np.where(mR)[0])[0]
    check("G11-pair-rich-OUT",
          (not ok123) and (not okR) and np123 >= 6 and npR >= 10
          and j123 > 0.80 and jR > 0.50,
          "wrap123 pairs=%d j=%.4f; randF1 pairs=%d j=%.4f"
          % (np123, j123, npR, jR))

    m1010 = np.array([i % 2 == 0 for i in range(S40)], bool)
    m234 = T.wrap_kgap(S40, (2, 3, 4), 7)
    n0 = int(2 * ((S40 + 1) // 2) / 5)
    lam10 = T.lam_at(T.mz_from_mask(xf40, wf40, m1010), n0)
    lam234, g234, gA234 = I.gersh_at(T.mz_from_mask(xf40, wf40, m234), n0)
    check("G12-isolated-not-lambda-and-not-gersh",
          lam10 > 1.0 and lam234 < I.ASSIST_234_CEIL
          and g234 > I.GERSH_FLOOR and gA234 > I.GA_FLOOR,
          "1010 lam=%.4f wrap234 lam=%.4f gersh=%.3f gA=%.3f"
          % (lam10, lam234, g234, gA234))

    lam22 = T.lam_at(CA.two_period(81, 2.0 / 3.0), 22)
    _ds, _Ns, _xfs, _ws, idxs = T.mask_idx(9, scramble_seed=3)
    denss = I.n_pairs_of(idxs)[0] / max(len(idxs), 1)
    check("G13-two-period-and-scramble",
          lam22 > 1.0 and denss > I.SCR_DENS_FLOOR,
          "lam22=%.4f scramble dens=%.3f" % (lam22, denss))

    n10 = 0
    j10s = []
    n_fat = n_thin = 0
    for s in range(8):
        m0 = T.wrap_kgap(S40, (2, 3, 4), s)
        m10, _ = I.inject_k_pairs(m0, 10, seed=396 + s)
        ok10, _, j10 = T.occ_fejer(xf40, wf40, m10, 40)
        n10 += int(ok10)
        j10s.append(j10)
        n_fat += int(T.occ_fejer(
            xf40, wf40, I.fattail_isolated(S40, 60, s), 40)[0])
        n_thin += int(T.occ_fejer(xf40, wf40, m0, 40)[0])
    check("G14-inject-and-fattail",
          n10 == 0 and max(j10s) > I.INJ10_J_FLOOR
          and n_fat >= n_thin and n_fat >= 4,
          "k=10 IN %d/8 jmax=%.3f; fattail %d/8 vs thin %d/8"
          % (n10, max(j10s), n_fat, n_thin))


def main():
    print("=" * 72)
    print("verify_isolation_lemma.py -- round 396")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("ISOLATION LEMMA VERIFIED")
        return 0
    print("ISOLATION LEMMA FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
