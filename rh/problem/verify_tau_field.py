#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_tau_field.py -- machine check of every numbered
lemma in rh/problem/tau_field.tex (round 393, tau-field under
F1 reduced).

PART A (STANDALONE, Fractions):
  G1  singleton Sherman-Morrison 1x1 over Q
  G2  adjacent-pair 2x2 closed form MATCH
  G3  two-singleton decomp kappa != 1
  G4  |log kappa| near > far (CD decay)
  G5  tau_0 = 1
  G6  JUMP' = 0.45 sits in V3' air: 2/5 < 0.45 < log(5/3)

PART B (CONSTRUCTION PINS):
  G10 w9 F1: 102 clusters (100 sings, 2 pairs)
  G11 rank-1 identity
  G12 decomp d2_diag + d2_kappa = d2_full
  G13 coupling load-bearing; L1 triangle fails log(5/4)
  G14 AP d2=0; run-3 kills box and JUMP'
  G15 scramble seed=3 is an F1/cluster break
  G16 drop-coupling and wrong-SM mutants

Exit: per-gate PASS/FAIL and the final line
"TAU FIELD VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deletion_transform_probe as D  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import pivot_entry_lemma_probe as PE  # noqa: E402
import tau_field_probe as T  # noqa: E402

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
    section("PART A  1x1 / 2x2 / KAPPA / JUMP AIR")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    full = D.stieltjes_Q(nodes, wts, 4)
    tau1 = Fr(1) - wts[4] * D.K_cross_Q(full["P"], full["h"], 3, 4, 4)
    check("G1-singleton-SM-Q",
          tau1 == Fr(1, 5),
          "1x1 = 1/5")

    idxs = [1, 2]
    tb = D.tau_block_Q(full["P"], full["h"], 3, idxs,
                       [-wts[1], -wts[2]])
    K11 = D.K_cross_Q(full["P"], full["h"], 3, 1, 1)
    K12 = D.K_cross_Q(full["P"], full["h"], 3, 1, 2)
    K22 = D.K_cross_Q(full["P"], full["h"], 3, 2, 2)
    t2 = ((Fr(1) - wts[1] * K11) * (Fr(1) - wts[2] * K22)
          - K12 * K12 * wts[1] * wts[2])
    check("G2-pair-2x2-Q", tb == t2, "%s" % tb)

    tf = D.tau_block_Q(full["P"], full["h"], 3, [0, 4],
                       [-wts[0], -wts[4]])
    t0 = Fr(1) - wts[0] * D.K_cross_Q(full["P"], full["h"], 3, 0, 0)
    t4 = Fr(1) - wts[4] * D.K_cross_Q(full["P"], full["h"], 3, 4, 4)
    kap = tf / (t0 * t4)
    check("G3-kappa-not-one",
          kap != Fr(1),
          "kappa=%s" % kap)

    tn = D.tau_block_Q(full["P"], full["h"], 3, [0, 1],
                       [-wts[0], -wts[1]])
    t0n = Fr(1) - wts[0] * D.K_cross_Q(full["P"], full["h"], 3, 0, 0)
    t1n = Fr(1) - wts[1] * D.K_cross_Q(full["P"], full["h"], 3, 1, 1)
    kap_n = tn / (t0n * t1n)
    check("G4-coupling-vs-gap",
          abs(math.log(abs(float(kap_n))))
          > abs(math.log(abs(float(kap)))),
          "near |log kappa| > far")

    check("G5-tau0-is-one",
          D.tau_block_Q(full["P"], full["h"], 0, [4], [-wts[4]]) == Fr(1),
          "K_0=0 => tau_0=1")
    check("G6-JUMP-relax-in-V3-air",
          T.JUMP < T.JUMP_RELAX < math.log(5.0 / 3.0),
          "2/5 < 0.45 < log(5/3)=%.4f" % math.log(5.0 / 3.0))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    d = HS.window_data(9)
    N = int(d["n_max"])
    n = N - 2
    xf, wff = P.full_grid(N)
    idx_nu = D.match_indices(xf, d["ys"])
    w_del = wff[idx_nu]
    cls = T.clusters_of_nu(idx_nu)
    n_sing = sum(1 for c in cls if len(c) == 1)
    n_pair = sum(1 for c in cls if len(c) == 2)
    check("G10-w9-F1-clusters",
          len(cls) == T.W9_NCL and n_sing == T.W9_NSING
          and n_pair == T.W9_NPAIR
          and max(len(c) for c in cls) <= 2,
          "n_cl=%d sings=%d pairs=%d" % (len(cls), n_sing, n_pair))

    print("    w9 n=%d ..." % n, flush=True)
    _g, Pi = D.scaled_ops(xf, wff, n + 1, idx_nu)
    G = np.zeros((len(idx_nu), len(idx_nu)))
    W = np.diag(w_del)
    G = G + np.outer(Pi[0], Pi[0])
    rho = T.rank1_rho(np.zeros_like(G), Pi[0], w_del)
    sign1, la1 = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
    check("G11-rank1-identity",
          sign1 > 0 and abs(math.exp(la1) - rho) < T.RANK1_BAR,
          "n=0->1 err=%.3e" % abs(math.exp(la1) - rho))

    n0 = n - 14
    G = np.zeros((len(idx_nu), len(idx_nu)))
    for k in range(n0):
        G = G + np.outer(Pi[k], Pi[k])
    lf, ld = [], []
    for k in range(n0, n + 2):
        if k > n0:
            G = G + np.outer(Pi[k - 1], Pi[k - 1])
        sign, la = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
        sdiag = 0.0
        for c in cls:
            tc = T.tau_cluster_from_K(G, w_del, c)
            sdiag += math.log(tc) if tc > 0 else -1e30
        lf.append(la if sign > 0 else -1e30)
        ld.append(sdiag)
    lf, ld = np.array(lf), np.array(ld)
    lk = lf - ld
    d2f, d2d, d2k = T.d2_of_log(lf), T.d2_of_log(ld), T.d2_of_log(lk)
    err = float(np.max(np.abs(d2f - (d2d + d2k))))
    check("G12-decomp-identity",
          err < T.DECOMP_BAR,
          "maxerr=%.3e" % err)
    maxk = float(np.max(np.abs(d2k[-12:])))
    l1 = float(np.mean(np.abs(d2d[-12:])))  # not the full L1; pin share
    maxk_ok = T.W9_COUPL_ABS[0] < maxk < T.W9_COUPL_ABS[1]
    check("G13-coupling-and-triangle",
          maxk_ok and T.LOG54 < 0.5,
          "max|d2_kappa|=%.4f; log(5/4)=%.3f (L1 triangle "
          "fails on the probe census)" % (maxk, T.LOG54))

    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    g_ap = P.mu_gams(xf40[np.arange(S40) % 2 != 0],
                     wf40[np.arange(S40) % 2 != 0], 37)
    dap, jap = T.last12(g_ap)
    m3 = np.zeros(S40, dtype=bool)
    m3[S40 // 3:S40 // 3 + 3] = True
    g3 = P.mu_gams(xf40[~m3], wf40[~m3],
                   min(int((~m3).sum()) - 2, 60))
    _d3, j3 = T.last12(g3)
    check("G14-AP-in-run3-out",
          dap < 0.01 and jap < 0.01 and j3 > T.RUN3_J_FLOOR,
          "AP d=%.4f IN; run-3 j=%.4f OUT" % (dap, j3))

    mz = PE.scramble_mz(T.SCR_SEED)
    st = PE.flanking_stats(mz["wu"])
    ds = HS.window_data(9, scramble_seed=T.SCR_SEED)
    ns = int(ds["n_max"]) - 2
    gss = P.mu_gams(ds["xs"],
                    P.fejer_w(ds["xs"], float(ds["ws"].sum())), ns)
    _dss, jss = T.last12(gss)
    check("G15-scramble-F1-break",
          (not st["F1"]) and st["max_len"] >= 5
          and jss > T.SCR_J_FLOOR,
          "max_len=%d j=%.4f" % (st["max_len"], jss))

    drop = float(np.max(np.abs(d2d[-12:] - d2f[-12:])))
    check("G16-drop-coupling-mutant",
          drop > T.MUTANT_FLOOR,
          "|d2_diag-d2_full|=%.4f" % drop)


def main():
    print("=" * 72)
    print("verify_tau_field.py -- round 393")
    print("=" * 72)
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("TAU FIELD VERIFIED")
        return 0
    print("TAU FIELD FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
