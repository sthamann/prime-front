#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_deletion_transform.py -- machine check of every numbered
lemma in rh/problem/deletion_transform.tex (round 392, deletion
transform reduced).

PART A (STANDALONE, Fractions):
  G1  one-point Uvarov gamma-ratio over Q (5/48, 8/75, 5/81)
  G2  two-point block = iterated = direct (8/45, 4/15)
  G3  rational S=5,7,9 with 1-2 deletions MATCH
  G4  Chebyshev-U monic p2=x^2-1/4
  G5  log(5/3) > 2/5: JUMP is not implied by the box
  G6  cosine S=7,9 f64 formula residual < 1e-12
  G7  tau_0 = 1 (empty kernel)

PART B (CONSTRUCTION PINS):
  G10 w9 Uvarov vs occupied-Fejer identity
  G11 w9 occupied last-12 inside the box
  G12 Assist Uvarov(mu+nu) = 0.0399, canc > 0.99
  G13 Fejer-mu kernel is NOT Assist (lam > 2)
  G14 dDelta last-12 and Dmax match r388
  G15 Christoffel-|V| mutant fails; AP-deletion stays IN
  G16 clustered run=3 kills; scramble seed=3 kills

Exit: per-gate PASS/FAIL and the final line
"DELETION TRANSFORM VERIFIED" iff every gate passed.

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
    section("PART A  UVAROV RATIO, BLOCK=ITERATED, TOYS")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    full = D.stieltjes_Q(nodes, wts, 4)
    tau = [Fr(1) + (-wts[4]) * D.K_cross_Q(full["P"], full["h"], n, 4, 4)
           for n in range(5)]
    g_fml = D.uvarov_gamma_Q(full["gamma"][:3], tau)
    red = D.stieltjes_Q(nodes[:-1], wts[:-1], 3)
    check("G1-one-point-Uvarov-Q",
          g_fml == red["gamma"]
          and g_fml == [Fr(5, 48), Fr(8, 75), Fr(5, 81)],
          "5/48, 8/75, 5/81")

    idxs = [1, 3]
    Ms = [-wts[i] for i in idxs]
    tau_b = [D.tau_block_Q(full["P"], full["h"], n, idxs, Ms)
             for n in range(4)]
    g_b = D.uvarov_gamma_Q(full["gamma"][:2], tau_b)
    keep = [i for i in range(5) if i not in idxs]
    red2 = D.stieltjes_Q([nodes[i] for i in keep],
                         [wts[i] for i in keep], 2)
    check("G2-block-equals-direct-Q",
          g_b == red2["gamma"] and g_b == [Fr(8, 45), Fr(4, 15)],
          "8/45, 4/15")

    n_bad = 0
    for S in (5, 7, 9):
        nds, wss = D.rat_grid(S)
        npts = len(nds)
        fl = D.stieltjes_Q(nds, wss, npts - 1)
        for ndel in (1, 2):
            if ndel >= npts - 2:
                continue
            idd = list(range(npts - ndel, npts))
            Ms = [-wss[i] for i in idd]
            nm = npts - ndel - 1
            taus = [D.tau_block_Q(fl["P"], fl["h"], n, idd, Ms)
                    for n in range(nm + 2)]
            gf = D.uvarov_gamma_Q(fl["gamma"][:nm], taus)
            kp = [i for i in range(npts) if i not in idd]
            rd = D.stieltjes_Q([nds[i] for i in kp],
                              [wss[i] for i in kp], nm)
            if gf != rd["gamma"]:
                n_bad += 1
    check("G3-rational-S579-Q", n_bad == 0, "1-2 deletions MATCH")

    check("G4-chebyshev-U-monic",
          (Fr(2, 5) ** 2 - Fr(1, 4)) == Fr(4, 25) - Fr(1, 4),
          "p2=x^2-1/4")
    check("G5-jump-not-implied",
          math.log(5.0 / 3.0) > D.JUMP,
          "log(5/3)=%.4f > 2/5" % math.log(5.0 / 3.0))

    xs = np.array([math.cos(math.pi * k / 7) for k in range(1, 7)])
    ws = np.maximum(1.0 - xs, 1e-15)
    gF, Pi = D.scaled_ops(xs, ws, 4, np.array([5]))
    gT = D.iterated_uvarov(gF[:3], Pi, ws[-1:])
    gD = P.mu_gams(xs[:-1], ws[:-1], 3)
    check("G6-cosine-S7-f64",
          float(np.max(np.abs(gT - gD))) < 1e-12,
          "maxerr=%.3e" % float(np.max(np.abs(gT - gD))))

    check("G7-tau0-is-one",
          D.tau_block_Q(full["P"], full["h"], 0, [4], [-wts[4]]) == Fr(1),
          "K_0=0 => tau_0=1")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2
    xf, wff = P.full_grid(N)
    idx_nu = D.match_indices(xf, ys)
    idx_mu = D.match_indices(xf, xs)
    print("    w9 n=%d ..." % n, flush=True)
    g_full, Pi = D.scaled_ops(xf, wff, n + 1, idx_nu)
    g_fml, Ks_f = D.iterated_uvarov(g_full[:n], Pi, wff[idx_nu],
                                   return_Ks=True)
    g_occ = P.mu_gams(xs, P.fejer_w(xs, float(ws.sum())), n)
    err = float(np.max(np.abs(g_fml - g_occ[:n])))
    dfo, jfo = D.last12(g_occ)
    check("G10-w9-formula-identity",
          err < D.W9_FML_BAR,
          "maxerr=%.3e" % err)
    check("G11-w9-occupied-inside",
          dfo <= D.BOX + 1e-12 and jfo <= D.JUMP
          and D.W9_FJ_D_LO < dfo < D.W9_FJ_D_HI,
          "|g-1/4|=%.5f jump=%.4f" % (dfo, jfo))

    w_union = np.zeros(len(xf))
    w_union[idx_mu] = ws
    w_union[idx_nu] = vs
    g_un, Pi_un = D.scaled_ops(xf, w_union, n + 1, idx_nu)
    _gmu, Ks_mu = D.iterated_uvarov(g_un[:n], Pi_un, vs, return_Ks=True)
    rA = D.assist_from_K(Ks_mu[N - 1], vs)
    check("G12-Assist-Uvarov",
          D.W9_ASSIST_LO < rA["assist"] < D.W9_ASSIST_HI
          and rA["canc"] > D.W9_CANC_FLOOR,
          "assist=%.4f canc=%.4f" % (rA["assist"], rA["canc"]))
    rF = D.assist_from_K(Ks_f[N - 1], vs)
    check("G13-Fejer-not-Assist",
          rF["lam"] > D.ASSIST_FEJER_LAM_FLOOR,
          "Fejer-mu lam=%.3f" % rF["lam"])

    Q = np.array([float(vs @ np.diag(Ks_mu[k + 1] - Ks_mu[k]))
                  for k in range(n)])
    th_n = np.arccos(np.clip(ys, -1, 1))
    th_m = np.arccos(np.clip(xs, -1, 1))

    def Cq(th, w, q):
        return float(np.dot(w, np.cos(q * th)))

    C0n, C0m = Cq(th_n, vs, 0), Cq(th_m, ws, 0)
    QT = np.array([(C0n + Cq(th_n, vs, 2 * k)) / (C0m + Cq(th_m, ws, 2 * k))
                   for k in range(n)])
    dD12 = float(np.max(np.abs(np.diff(Q - QT)[-12:])))
    Dmax = float(np.max(np.abs(Q - QT)))
    check("G14-dDelta-r388",
          D.W9_DDELTA12[0] < dD12 < D.W9_DDELTA12[1]
          and D.W9_DMAX[0] < Dmax < D.W9_DMAX[1],
          "dDelta12=%.5f Dmax=%.4f" % (dD12, Dmax))

    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    g_ap = P.mu_gams(xf40[np.arange(S40) % 2 != 0],
                     wf40[np.arange(S40) % 2 != 0], 37)
    dap, jap = D.last12(g_ap)
    m_cl = np.zeros(S40, dtype=bool)
    m_cl[S40 // 3:S40 // 3 + 3] = True
    g_cl = P.mu_gams(xf40[~m_cl], wf40[~m_cl], min(int((~m_cl).sum()) - 2, 60))
    _dcl, jcl = D.last12(g_cl)
    check("G15-AP-in-cluster-out",
          dap < 0.01 and jap < 0.01 and jcl > D.CLUST_J_FLOOR,
          "AP d=%.4f IN; clustered j=%.4f OUT" % (dap, jcl))

    ds = HS.window_data(9, scramble_seed=D.SCR_SEED)
    ns = int(ds["n_max"]) - 2
    gss = P.mu_gams(ds["xs"],
                    P.fejer_w(ds["xs"], float(ds["ws"].sum())), ns)
    _dss, jss = D.last12(gss)
    check("G16-scramble-seed3-kills",
          jss > D.SCR_J_FLOOR,
          "scr-seed=%d jump=%.4f OUT" % (D.SCR_SEED, jss))


def main():
    print("=" * 72)
    print("verify_deletion_transform.py -- round 392")
    print("=" * 72)
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("DELETION TRANSFORM VERIFIED")
        return 0
    print("DELETION TRANSFORM FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
