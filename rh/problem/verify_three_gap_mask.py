#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_three_gap_mask.py -- machine check of every numbered
lemma in rh/problem/three_gap_mask.tex (round 395, three-gap
mask REFUTED).

PART A (STANDALONE):
  G1  Steinhaus on Z/q: nuniq<=3 for coprime p/q
  G2  additive a+b=c on a witnessed 3-gap (phi)
  G3  thinning a 3-gap set raises nuniq
  G4  integer-log local 3-gap for n0>=512
  G5  small-n log drift nuniq>=4
  G6  3/8 > 1/3 and 8/3 < 23 (the two named shadows fail)

PART B (CONSTRUCTION PINS):
  G10 w9 nuniq=12, gap1=2, dmin/dmed=1/3
  G11 w9 slide12 three-gap is PARTIAL
  G12 tiles 1010/1100 IN; random F1 OUT; wrap(1,2,3) OUT
  G13 scramble seed=3 kills local three-gap
  G14 two-period lam22>1; assist splits randF1 vs wrap(2,3,4)

Exit: per-gate PASS/FAIL and the final line
"THREE GAP MASK VERIFIED" iff every gate passed.

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

import three_gap_mask_probe as T  # noqa: E402
import coherence_assist_probe as CA  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402

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
    section("PART A  STEINHAUS / LOG / SHADOWS")
    ok, nu = T.steinhaus_rational(5, 13, 13)
    check("G1-Steinhaus-Z-q",
          ok and nu <= 3,
          "5/13 full nuniq=%d" % nu)
    a = T.PHI
    pts = np.sort(np.array([((k * a) % 1.0) for k in range(1, 5)]))
    dd = np.diff(pts)
    dd = np.concatenate([dd, [pts[0] + 1.0 - pts[-1]]])
    u = np.unique(np.round(dd, 8))
    check("G2-additive-phi",
          len(u) == 3 and abs(u[0] + u[1] - u[2]) < 1e-7,
          "uniq=%s" % (tuple("%.4f" % x for x in u),))
    q, p = 89, 55
    pts = sorted({(k * p) % q for k in range(40)})
    rng = np.random.default_rng(395)
    sub = sorted(rng.choice(pts, size=20, replace=False).tolist())
    d = [sub[i + 1] - sub[i] for i in range(len(sub) - 1)]
    d.append(q - sub[-1] + sub[0])
    check("G3-thinning-raises-nuniq",
          len(set(d)) > 3,
          "subset nuniq=%d" % len(set(d)))
    check("G4-log-large-n",
          T.log_block_nuniq(512, 64) <= 3,
          "n0=512 M=64 nuniq=%d" % T.log_block_nuniq(512, 64))
    check("G5-log-small-n-census",
          T.log_block_nuniq(16, 32) >= 4,
          "n0=16 M=32 nuniq=%d" % T.log_block_nuniq(16, 32))
    check("G6-shadows-fail",
          T.THREE_EIGHTHS > 1.0 / 3.0
          and T.MEDCAP < 23.0,
          "3/8>1/3 and 8/3<23")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    _d, N, xf, wf, idx = T.mask_idx(9)
    sp = T.spectrum(T.gaps_of(idx, False))
    g1 = sp["counts"][sp["uniq"].index(1)] if 1 in sp["uniq"] else 0
    check("G10-w9-nuniq-12",
          sp["nuniq"] == T.W9_NUNIQ and g1 == T.W9_GAP1
          and abs(sp["ratio"] - 1.0 / 3.0) < 1e-12,
          "nuniq=%d gap1=%d ratio=%.3f" % (sp["nuniq"], g1, sp["ratio"]))
    sl = T.sliding_nuniq(idx, 12)
    f3 = float(np.mean([x <= 3 for x in sl]))
    check("G11-w9-slide-partial",
          T.W9_SL12_3[0] < f3 < T.W9_SL12_3[1],
          "slide12<=3=%.2f" % f3)

    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    m1010 = np.array([i % 2 == 0 for i in range(S40)], bool)
    mR = T.random_f1_mask(S40, 0.45, 2)
    m123 = T.wrap_kgap(S40, (1, 2, 3), 7)
    ok10, _, j10 = T.occ_fejer(xf40, wf40, m1010, 40)
    okR, _, jR = T.occ_fejer(xf40, wf40, mR, 40)
    ok123, _, j123 = T.occ_fejer(xf40, wf40, m123, 40)
    check("G12-discriminator",
          ok10 and (not okR) and (not ok123)
          and jR > T.RAND_F1_J_FLOOR and j123 > T.KGAP123_J_FLOOR,
          "1010 IN j=%.4f; randF1 OUT j=%.4f; wrap123 OUT j=%.4f"
          % (j10, jR, j123))

    _ds, _Ns, _xfs, _ws, idxs = T.mask_idx(9, scramble_seed=T.SCR_SEED)
    sls = T.sliding_nuniq(idxs, 12)
    f3s = float(np.mean([x <= 3 for x in sls])) if sls else 1.0
    check("G13-scramble-local",
          f3s < T.SCR_SL3_BAR,
          "slide12<=3=%.2f" % f3s)

    mz23 = CA.two_period(81, 2.0 / 3.0)
    lam22 = T.lam_at(mz23, 22)
    n0 = int(2 * ((S40 + 1) // 2) / 5)
    lamR = T.lam_at(T.mz_from_mask(xf40, wf40, mR), n0)
    m234 = T.wrap_kgap(S40, (2, 3, 4), 7)
    lam234 = T.lam_at(T.mz_from_mask(xf40, wf40, m234), n0)
    check("G14-assist-split",
          lam22 > 1.0 and lamR > T.ASSIST_RAND_FLOOR
          and lam234 < T.ASSIST_234_CEIL,
          "lam22=%.4f randF1=%.3f wrap234=%.3f"
          % (lam22, lamR, lam234))


def main():
    print("=" * 72)
    print("verify_three_gap_mask.py -- round 395")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("THREE GAP MASK VERIFIED")
        return 0
    print("THREE GAP MASK FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
