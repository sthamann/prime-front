#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""high_moment_inertia_probe -- PRIME.LDAGGER.HIGH_MOMENT_INERTIA.01
(round 398): the reviewer-preregistered high-moment kill-test of
P1 = ind_-(R_{N-3} - I/2) <= 1, BEFORE the source-Weyl campaign.

Coexistence: r367/r369 built R_{N-3} (dual CD Gram of the first
N-3 dual OP columns on Y); r373 Haynsworth; DCCLXII set the
R^dagger north star.  This round is the cheap sufficient test
that would reduce P1 to a finite even cycle-moment if it passed.

THE INEQUALITY (finite, pointwise, any 0 ⪯ R ⪯ I):
  1_{r < 1/2}  <=  [2(1-r)]^{2d}
hence
  ind_-(R - I/2)  <=  2^{2d} tr((I-R)^{2d}).
If the right-hand side is < 2 for a FIXED d in {2,3,4,6,8}
on MAIN, Twin and living chi WITH growing reserve in N, P1
is a source cycle-sum (outside the two-moment ceiling class).

HARD STOPS (preregistered, binding): d in {2,3,4,6,8} only
(no d growing with N); NO target margin; NO eigenvectors in the
certificate (traces via even powers); eigenvalues only for the
contraction gate and the post-mortem anatomy of failure.

LEGS.
  A  Build R_{N-3} (r367 cut: Bd[:, :N-3] Bd[:, :N-3].T) on
     core-42 + MAIN-85 sample + Twin + living chi; gate 0 ⪯ R ⪯ I.
  B  2^{2d} tr((I-R)^{2d}) for the five d; verdict KILL_PASS /
     KILL_FAIL / PARTIAL; anatomy # eigs in [1/2 ± δ] for
     δ in {0.01, 0.05, 0.1}.
  C  Cycle-sum formula on a toy; if FAIL, the smallest d that
     would give < 2 (even > 8, diagnosis only) and MAIN vs dead
     chi (two-sided world test).
  D  Kills: scramble (ind_- = 21 must be seen); two-period;
     mutants (2^{2d} dropped; odd power); dead chi sharpness.

CALIBRATION DISCLOSURE.  Moments, near-1/2 counts, scramble
nneg=21, two-period, Twin, living/dead chi were first measured
in /tmp (r398_cal.py, r398_cal2.py) on the same constructors,
2026-08-29.  Frozen floors below are that measurement, sealed
as gates.  No two-commit pre-blind freeze: pins disclosed.
Builder fallback NOT taken: full census wall 5.5 s on
core-42 + MAIN-85 sample + chi3/chi4-42 + Twin (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Fractions: r=2/5, d=2, [2(1-r)]^4 = 1296/625 >= 1;
    nopref (1-r)^4 = 81/625 < 1 (mutant FALSE).
  * Cycle-sum 3x3 k=4: tr(A^4) = walk-sum, dev 6.9e-18.
  * w9 MAIN: 0 ⪯ R ⪯ I, n=104, nneg=1, rmin=0.46153,
    M_d = (33.478, 26.785, 22.749, 18.226, 16.028) for
    d=2,3,4,6,8, ALL >= 2; near-1/2 counts (5, 24, 37);
    FTI A0+I/2 residual 0; min_d M_d at d=11 still 15.06.
  * Core-42: 42/42 contractions, nneg in {0,1}, M2 in
    [33.22, 224.5], Nmin=142 M2=34.86, Nmax=878 M2=224.5
    (reserve SHRINKS).  All five d fail on every row.
  * MAIN-85 sample: kz119 M2=287.9; EXT kz69 N=5690 M2=1079.
  * Twin kz 9/18/52: |d M2| <= 2e-5, nneg identical.
  * Living chi3 37/37 M2 in [28.03, 183.4] all >= 2;
    living chi4 41/41 M2 in [26.90, 178.7] all >= 2.
  * Dead chi3 5/5 M2 in [35.98, 63.55] all >= 2;
    dead chi4-20 M2=33.75 (control holds, test NOT sharp:
    living also >= 2).
  * Scramble seed=1: nneg=21, M2=148, M8=2.65e5 (explodes).
  * Two-period S=21: nneg=4, rmin=0, M2=52.0 (explodes).
  * need_d: NONE on nneg=1 (bound diverges after a min > 2);
    on nneg=0 bulk-only d~512..1024 (grows with 1/gap, forbidden).

AUSGANG KILL_FAIL (the high-moment sufficient test of P1).
SATZ: the pointwise bound, the cycle-sum identity on the toy,
0 ⪯ R_{N-3} ⪯ I on the named census, traces = spectral sums.
REFUTED as a route: a fixed d in {2,3,4,6,8} with RHS < 2
and growing reserve.  Cause: a macroscopic cluster of
eigenvalues of R_{N-3} at 1/2 from above (w9: 36 in [1/2, 3/5]),
each contributing ~1 to the moment; the genuine negative mode
when present sits at rmin~0.39..0.49 so large d diverges.
Cycle-sum is NOT the R399 target.  No RH claim.

MACHINERY: r367 FTI.cut_rung (cross-check only), r356 BDH
dual_weights, r342 PX unused in the certificate, r357 DMF
chi, r331 TR / r289 AKD Twin, r226 V.build_measures,
verify_lstar_instance.mu_chain / b_matrix.

NO RH CLAIM.  Finite identities, a named kill-test, named
kills.  Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_dual_hole_probe as BDH  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import twin_resolution_probe as TR  # noqa: E402
import arch_kernel_diophantine_probe as AKD  # noqa: E402
import minimal_firewall_probe as MF  # noqa: E402
import lstar_margin_scaling_probe as LM  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

DS = (2, 3, 4, 6, 8)
DELTAS = (0.01, 0.05, 0.1)
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
SCR_SEED = 1
SAMPLE_EXT = (119, 35, 70, 109, 42, 72, 69)
WORLD_TWIN = (18, 9, 52)
EXT3_0, EXT4_0, EXT5_0 = 42, 72, 69

W9_M = {2: 33.4777, 3: 26.7851, 4: 22.749, 6: 18.2262, 8: 16.028}
W9_NEAR = {0.01: 5, 0.05: 24, 0.1: 37}
W9_NNEG, W9_N, W9_NW = 1, 104, 184
W9_RMIN = 0.46153
SCR_NNEG = 21
SCR_M2_FLOOR, SCR_M8_FLOOR = 100.0, 1.0e4
TP21_NNEG, TP21_M2_FLOOR = 4, 40.0
CORE_N = 42
CORE_M2_LO, CORE_M2_HI = 30.0, 230.0
NMIN, NMAX = 142, 878
TREND_RATIO = 2.0
CHI3_LIVE_N, CHI4_LIVE_N = 37, 41
CHI3_DEAD_N, CHI4_DEAD_N = 5, 1
TWIN_D_BAR = 5.0e-5
REL = 5.0e-3
CONTRACT_LO, CONTRACT_HI = -1.0e-8, 1.0 + 1.0e-8
FTI_SHA_PREFIX = "e0d79840"
BDH_SHA_PREFIX = "36141c0a"
DMF_SHA_PREFIX = "4bf1a94b"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; dual weights / "
                       "mu_chain / CD Gram / traces only"
                       if not bad else "; ".join(bad))


def allowed_d_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "moments":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(
                        sub.value, int) and sub.value not in (
                            2, 3, 4, 6, 8, 12, 16, 0):
                    if sub.value > 16:
                        hits.append("d=%d@%d" % (sub.value, sub.lineno))
    return hits


# ---- constructors (certificate uses traces, not eigenvectors) ----

def r_nm3(xu, wu, yn, vn, Nw, S, L):
    """R_{N-3} = B_{N-3} B_{N-3}^T, the r367 dual-CD restriction
    to Y.  Consumes the union measure, the hole nodes and the
    half-filling integers only."""
    xu = np.asarray(xu, float)
    wu = np.asarray(wu, float)
    yn = np.asarray(yn, float)
    ud, _lA, _f, _eps, _lp = BDH.dual_weights(xu, np.abs(wu), S, L)
    iY = np.searchsorted(xu, yn)
    ok_map = bool(len(iY) == len(yn) and np.all(iY < len(xu))
                  and np.max(np.abs(xu[iY] - yn)) <= 1e-12)
    ad, bd, h0d = V.mu_chain(xu, ud, Nw)
    Bd = V.b_matrix(ad, bd, h0d, yn, ud[iY], Nw)
    R = Bd[:, :Nw - 3] @ Bd[:, :Nw - 3].T
    R = 0.5 * (R + R.T)
    ok_sup = (S == L // 2) and (S == 2 * Nw - 1) and len(xu) == S
    return R, dict(ok_sup=bool(ok_sup), ok_map=ok_map, Nw=int(Nw),
                   Sm=int(R.shape[0]), S=int(S), Bd=Bd)


def moments(R):
    """Registered even traces: 2^{2d} tr((I-R)^{2d}) for
    d in {2,3,4,6,8}.  Powers by repeated multiply, no eigensolver."""
    n = R.shape[0]
    A = np.eye(n) - R
    A2 = A @ A
    A4 = A2 @ A2
    A6 = A4 @ A2
    A8 = A4 @ A4
    A12 = A8 @ A4
    A16 = A8 @ A8
    pows = {2: A4, 3: A6, 4: A8, 6: A12, 8: A16}
    out = {}
    for d in DS:
        trp = float(np.trace(pows[d]))
        Md = (2.0 ** (2 * d)) * trp
        out[d] = dict(tr=trp, M=Md, reserve=2.0 - Md, pass_=Md < 2.0)
    return out


def anatomy(R):
    """Post-mortem only: eigenvalues for the contraction gate and
    the near-1/2 cluster.  Not an input of the moment certificate."""
    ev = np.linalg.eigvalsh(R)
    return dict(
        evmin=float(ev[0]), evmax=float(ev[-1]),
        contract=(ev[0] >= CONTRACT_LO) and (ev[-1] <= CONTRACT_HI),
        nneg=int(np.sum(ev < 0.5 - 1e-12)),
        near={dlt: int(np.sum(np.abs(ev - 0.5) <= dlt)) for dlt in DELTAS},
        n_halfp=int(np.sum((ev >= 0.5) & (ev <= 0.6))),
        ev=ev,
    )


def pack(R, tag, Nw):
    mom = moments(R)
    an = anatomy(R)
    an.pop("ev")
    return dict(tag=tag, Nw=int(Nw), n=int(R.shape[0]),
                moms=mom, **an)


def row_mz(mz, tag):
    R, meta = r_nm3(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                     mz["Nw"], mz["S"], mz["L"])
    p = pack(R, tag, mz["Nw"])
    p["ok_sup"] = meta["ok_sup"]
    p["ok_map"] = meta["ok_map"]
    p["R"] = R
    return p


def two_period_mz(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    ord_ = np.argsort(x)
    x, w = x[ord_], w[ord_]
    pos = w > 0
    return dict(xu=x, wu=w, yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S, L=2 * S)


def scramble_mz():
    alpha = float(V.U[9])
    _uu, ww, _n, _c = DMF.chi_window_comb(9, DMF.Q_CHI3)
    rng = np.random.default_rng(SCR_SEED)
    u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(ww)))
    return DMF.chi_build_measures(9, u_scr, ww, 1.0, DMF.LPQ3)


def chi_mz(kz, q, lpq):
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    return DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)


def pointwise_holds(r, d):
    lhs = 1.0 if r < 0.5 else 0.0
    rhs = (2.0 * (1.0 - r)) ** (2 * d)
    return lhs <= rhs + 1e-15


def cycle_walk_sum(A, k):
    A = np.asarray(A, float)
    n = A.shape[0]
    acc = 0.0

    def rec(path):
        nonlocal acc
        if len(path) == k:
            w = 1.0
            for t in range(k):
                w *= A[path[t], path[(t + 1) % k]]
            acc += w
            return
        for i in range(n):
            rec(path + [i])

    rec([])
    return acc


def tr_power(A, k):
    P = np.asarray(A, float).copy()
    acc = None
    base = P
    kk = int(k)
    if kk == 0:
        return float(P.shape[0])
    while kk > 0:
        if kk & 1:
            acc = base.copy() if acc is None else acc @ base
        kk >>= 1
        if kk:
            base = base @ base
    return float(np.trace(0.5 * (acc + acc.T)))


# ---- legs ----

def part_a_toy():
    section("S1  LEG A/C -- INEQUALITY, CYCLE-SUM, MUTANTS (TOY)")
    r = Fr(2, 5)
    rhs = (2 * (1 - r)) ** 4
    npr = (1 - r) ** 4
    check("G01-Fractions-bound",
          rhs == Fr(1296, 625) and rhs >= 1,
          "[2(1-2/5)]^4 = %s >= 1" % rhs)
    check("G02-mutant-nopref",
          npr == Fr(81, 625) and npr < 1,
          "nopref (1-r)^4 = %s < 1 -- bound FALSE without 2^{2d}"
          % npr)
    check("G03-pointwise-registered",
          all(pointwise_holds(x, d) for d in DS
              for x in (0.4, 0.5, 0.6, 0.9)),
          "1_{r<1/2} <= [2(1-r)]^{2d} on {0.4,0.5,0.6,0.9} x DS")
    # odd-power mutant: without contraction the odd majorant fails
    r_odd = (Fr(2, 5), Fr(2))
    odd_sum = sum((2 * (1 - ri)) ** 5 for ri in r_odd)
    even_sum = sum((2 * (1 - ri)) ** 4 for ri in r_odd)
    check("G04-mutant-odd",
          odd_sum < 1 and even_sum >= 1,
          "R=diag(2/5,2) odd p=5 sum=%s < 1; even p=4 sum=%s >= 1"
          % (odd_sum, even_sum))
    A = np.array([[0.3, 0.1, 0.05],
                  [0.1, 0.4, 0.02],
                  [0.05, 0.02, 0.2]])
    A = 0.5 * (A + A.T)
    tr4 = tr_power(A, 4)
    walks = cycle_walk_sum(A, 4)
    check("G05-cycle-sum-k4",
          abs(tr4 - walks) <= 1e-14,
          "tr(A^4)=%.12g walks=%.12g dev=%.1e" % (tr4, walks,
                                                  abs(tr4 - walks)))
    A2 = np.array([[Fr(1, 2), Fr(1, 4)],
                   [Fr(1, 4), Fr(1, 3)]], dtype=object)
    tr2 = A2[0, 0] * A2[0, 0] + A2[1, 1] * A2[1, 1] + 2 * A2[0, 1] * A2[1, 0]
    check("G06-Fractions-trA2",
          tr2 == Fr(35, 72),
          "2x2 tr(A^2)=%s = 35/72 (closed walks of length 2)" % tr2)
    check("G07-allowed-d-frozen",
          DS == (2, 3, 4, 6, 8) and not allowed_d_audit(),
          "DS=%s; moments() has no N-growing d" % (DS,))


def part_b_w9():
    section("S2  LEG A/B -- w9 R_{N-3} + MOMENTS + ANATOMY")
    mz = V.build_measures(9)
    p = row_mz(mz, "MAIN-9")
    i1, i2 = PX.pair_select(mz["yn"])
    o = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                      mz["Nw"], mz["S"], mz["L"], i1, i2, keep=True)
    R2 = o["A0"] + 0.5 * np.eye(o["A0"].shape[0])
    dev = float(np.max(np.abs(p["R"] - R2)))
    check("G10-w9-contract",
          p["contract"] and p["ok_sup"] and p["ok_map"]
          and p["n"] == W9_N and p["Nw"] == W9_NW,
          "0 ⪯ R preceq I, n=%d N=%d ev[%.5f, %.5f]"
          % (p["n"], p["Nw"], p["evmin"], p["evmax"]))
    check("G11-w9-fti-R",
          dev == 0.0 and o["nneg"] == W9_NNEG and p["nneg"] == W9_NNEG,
          "R == A0+I/2 residual %.1e; nneg=%d == FTI %d"
          % (dev, p["nneg"], o["nneg"]))
    ok_m = all(abs(p["moms"][d]["M"] / W9_M[d] - 1.0) <= REL
               for d in DS)
    check("G12-w9-moments",
          ok_m and all(not p["moms"][d]["pass_"] for d in DS),
          "M_d=" + ", ".join("%.4g" % p["moms"][d]["M"] for d in DS)
          + "  ALL >= 2")
    check("G13-w9-anatomy",
          p["near"] == dict(W9_NEAR)
          and abs(p["evmin"] - W9_RMIN) <= 2e-4
          and p["n_halfp"] >= 30,
          "nneg=%d rmin=%.5f near %s half+=%d"
          % (p["nneg"], p["evmin"], p["near"], p["n_halfp"]))
    del p["R"]
    return p


def part_d_kills():
    section("S3  LEG D -- SCRAMBLE / TWO-PERIOD / DEAD CHI")
    mz_s = scramble_mz()
    ps = row_mz(mz_s, "SCR")
    i1, i2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                      mz_s["Nw"], mz_s["S"], mz_s["L"], i1, i2)
    check("G20-scramble-nneg21",
          ps["nneg"] == SCR_NNEG and oS["nneg"] == SCR_NNEG
          and ps["contract"],
          "ind_-=%d == 21 (FTI %d); the trace must see this"
          % (ps["nneg"], oS["nneg"]))
    check("G21-scramble-KILL_FAIL",
          ps["moms"][2]["M"] >= SCR_M2_FLOOR
          and ps["moms"][8]["M"] >= SCR_M8_FLOOR
          and ps["moms"][8]["M"] > ps["moms"][2]["M"],
          "M2=%.4g M8=%.4g explodes with d (rmin=%.5f)"
          % (ps["moms"][2]["M"], ps["moms"][8]["M"], ps["evmin"]))
    tp = row_mz(two_period_mz(21, 2.0 / 3.0), "2PER-21")
    check("G22-two-period",
          tp["nneg"] >= TP21_NNEG and tp["moms"][2]["M"] >= TP21_M2_FLOOR
          and all(not tp["moms"][d]["pass_"] for d in DS),
          "S=21 nneg=%d rmin=%.2e M2=%.4g (KILL_FAIL)"
          % (tp["nneg"], tp["evmin"], tp["moms"][2]["M"]))
    mz_d = chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    pd = row_mz(mz_d, "CHI3-15-DEAD")
    check("G23-dead-chi3-15",
          all(not pd["moms"][d]["pass_"] for d in DS)
          and pd["contract"],
          "dead chi3-15 nneg=%d M2=%.4g >= 2 (sharpness control holds)"
          % (pd["nneg"], pd["moms"][2]["M"]))
    return ps, tp, pd


def part_live_smoke():
    section("S4  LEG B -- LIVING CHI + TWIN (SMOKE PINS)")
    p3 = row_mz(chi_mz(9, DMF.Q_CHI3, DMF.LPQ3), "CHI3-9")
    p4 = row_mz(chi_mz(9, DMF.Q_CHI4, DMF.LPQ4), "CHI4-9")
    check("G30-chi3-9-live",
          p3["nneg"] == 0 and p3["moms"][2]["M"] >= 20.0
          and all(not p3["moms"][d]["pass_"] for d in DS),
          "vacuous P1 nneg=0 yet M2=%.4g (cluster, not P1)"
          % p3["moms"][2]["M"])
    check("G31-chi4-9-live",
          p4["nneg"] == 1 and p4["moms"][2]["M"] >= 20.0
          and all(not p4["moms"][d]["pass_"] for d in DS),
          "nneg=1 M2=%.4g" % p4["moms"][2]["M"])
    uuc, mmc = TR.base_comb(9)
    mzD = TR.build_world(9, uuc, mmc)
    gapsc = MF.local_gaps(uuc)
    u2c, m2c, _dn, _du = AKD.twin_rational(
        uuc, mmc, gapsc, mzD["D"], 1.0e-8)
    mzT = TR.build_world(9, u2c, m2c)
    pT = row_mz(mzT, "TWIN-9")
    pM = row_mz(V.build_measures(9), "MAIN-9")
    check("G32-twin-9",
          pT["nneg"] == pM["nneg"]
          and abs(pT["moms"][2]["M"] - pM["moms"][2]["M"]) <= TWIN_D_BAR
          and all(not pT["moms"][d]["pass_"] for d in DS),
          "|dM2|=%.3e nneg T/M %d/%d"
          % (abs(pT["moms"][2]["M"] - pM["moms"][2]["M"]),
             pT["nneg"], pM["nneg"]))
    return p3, p4, pT


def part_full_census():
    section("S5  LEG B -- CORE-42 + MAIN SAMPLE + CHI CENSUS")
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        p = row_mz(V.build_measures(kz), "MAIN-%d" % kz)
        p["kz"] = kz
        rows.append(p)
        del p["R"]
    Ms2 = [r["moms"][2]["M"] for r in rows]
    Ns = [r["Nw"] for r in rows]
    i_lo = int(np.argmin(Ns))
    i_hi = int(np.argmax(Ns))
    all_fail = all(not r["moms"][d]["pass_"] for r in rows for d in DS)
    check("G40-core42-contract",
          len(rows) == CORE_N
          and all(r["contract"] and r["ok_sup"] and r["ok_map"]
                  for r in rows)
          and min(r["nneg"] for r in rows) >= 0
          and max(r["nneg"] for r in rows) <= 1,
          "42/42 contractions, nneg in [%d, %d]"
          % (min(r["nneg"] for r in rows), max(r["nneg"] for r in rows)))
    check("G41-core42-all-fail",
          all_fail
          and CORE_M2_LO <= min(Ms2) <= 36.0
          and max(Ms2) >= 200.0,
          "M2 in [%.4g, %.4g] -- every d fails on every row"
          % (min(Ms2), max(Ms2)))
    check("G42-reserve-shrinks",
          Ns[i_lo] == NMIN and Ns[i_hi] == NMAX
          and Ms2[i_hi] >= TREND_RATIO * Ms2[i_lo],
          "N %d M2=%.4g -> N %d M2=%.4g (grows, reserve shrinks)"
          % (Ns[i_lo], Ms2[i_lo], Ns[i_hi], Ms2[i_hi]))

    ext_fail = True
    ext_n = 0
    for kz in SAMPLE_EXT:
        mz = V.build_measures(kz)
        p = row_mz(mz, "EXT-%d" % kz)
        ext_n += 1
        ext_fail = ext_fail and all(not p["moms"][d]["pass_"] for d in DS)
        print("    EXT-%d N=%d nneg=%d M2=%.4g"
              % (kz, p["Nw"], p["nneg"], p["moms"][2]["M"]), flush=True)
        del p["R"]
    check("G43-main85-sample",
          ext_n == len(SAMPLE_EXT) and ext_fail,
          "%d EXT sample rows, all M_d >= 2" % ext_n)

    live3, dead3, live4, dead4 = [], [], [], []
    for kz in core:
        mz3 = chi_mz(kz, DMF.Q_CHI3, DMF.LPQ3)
        if mz3 is not None:
            p = row_mz(mz3, "C3-%d" % kz)
            del p["R"]
            (dead3 if kz in DEAD_CHI3 else live3).append(p)
        mz4 = chi_mz(kz, DMF.Q_CHI4, DMF.LPQ4)
        if mz4 is not None:
            p = row_mz(mz4, "C4-%d" % kz)
            del p["R"]
            (dead4 if kz in DEAD_CHI4 else live4).append(p)

    def all_ge2(rs):
        return bool(rs) and all(not r["moms"][d]["pass_"]
                                for r in rs for d in DS)

    check("G44-chi3-live",
          len(live3) == CHI3_LIVE_N and all_ge2(live3)
          and all(r["contract"] for r in live3),
          "live chi3 %d/%d M2 [%.4g, %.4g]"
          % (len(live3), CHI3_LIVE_N,
             min(r["moms"][2]["M"] for r in live3),
             max(r["moms"][2]["M"] for r in live3)))
    check("G45-chi3-dead",
          len(dead3) == CHI3_DEAD_N and all_ge2(dead3),
          "dead chi3 %d/%d M2 [%.4g, %.4g] -- control >= 2, "
          "not a separator (living also >= 2)"
          % (len(dead3), CHI3_DEAD_N,
             min(r["moms"][2]["M"] for r in dead3),
             max(r["moms"][2]["M"] for r in dead3)))
    check("G46-chi4-live",
          len(live4) == CHI4_LIVE_N and all_ge2(live4),
          "live chi4 %d/%d M2 [%.4g, %.4g]"
          % (len(live4), CHI4_LIVE_N,
             min(r["moms"][2]["M"] for r in live4),
             max(r["moms"][2]["M"] for r in live4)))
    check("G47-chi4-dead",
          len(dead4) == CHI4_DEAD_N and all_ge2(dead4),
          "dead chi4 %d M2=%.4g" % (
              len(dead4), dead4[0]["moms"][2]["M"] if dead4 else -1))

    tw_ok = True
    for kz in WORLD_TWIN:
        uuc, mmc = TR.base_comb(kz)
        mzD = TR.build_world(kz, uuc, mmc)
        gapsc = MF.local_gaps(uuc)
        u2c, m2c, _dn, _du = AKD.twin_rational(
            uuc, mmc, gapsc, mzD["D"], 1.0e-8)
        pT = row_mz(TR.build_world(kz, u2c, m2c), "T-%d" % kz)
        pM = row_mz(V.build_measures(kz), "M-%d" % kz)
        tw_ok = (tw_ok and pT["nneg"] == pM["nneg"]
                 and abs(pT["moms"][2]["M"] - pM["moms"][2]["M"])
                 <= max(TWIN_D_BAR, 5e-5 * pM["moms"][2]["M"])
                 and all(not pT["moms"][d]["pass_"] for d in DS))
        del pT["R"], pM["R"]
    check("G48-twin-worlds",
          tw_ok, "Twin kz %s nneg+M2 stable, all >= 2" % (WORLD_TWIN,))
    return rows


def verdict_of(smoke_fail, full_rows):
    # KILL_PASS needs < 2 on all living with growing reserve.
    # Smoke already has w9/chi/twin all >= 2; full confirms census.
    if full_rows is not None:
        any_pass = any(r["moms"][d]["pass_"] for r in full_rows
                       for d in DS)
        Ns = [r["Nw"] for r in full_rows]
        i_lo, i_hi = int(np.argmin(Ns)), int(np.argmax(Ns))
        shrinks = all(full_rows[i_hi]["moms"][d]["M"]
                       >= full_rows[i_lo]["moms"][d]["M"]
                       for d in DS)
        if (not any_pass) and shrinks:
            return "KILL_FAIL"
        if any_pass and not shrinks:
            return "PARTIAL"
        return "KILL_FAIL"
    return "KILL_FAIL" if smoke_fail else "PARTIAL"


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("high_moment_inertia_probe -- "
          "PRIME.LDAGGER.HIGH_MOMENT_INERTIA.01 (round 398)")
    print("SPEC_SHA %s   (FTI %s / BDH %s / DMF %s)"
          % (SPEC_SHA[:16], FTI.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             DMF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (core-42 + MAIN-85 sample + chi + Twin)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "FTI %s / BDH %s / DMF %s"
          % (FTI.SPEC_SHA[:8], BDH.SPEC_SHA[:8], DMF.SPEC_SHA[:8]))

    part_a_toy()
    pw9 = part_b_w9()
    ps, tp, pd = part_d_kills()
    p3, p4, pT = part_live_smoke()
    full_rows = None
    if not smoke:
        full_rows = part_full_census()
    else:
        section("S5  FULL CENSUS skipped (--smoke)")

    smoke_fail = all(not pw9["moms"][d]["pass_"] for d in DS)
    verd = verdict_of(smoke_fail, full_rows)
    section("S6  VERDICT")
    check("G50-verdict-KILL_FAIL",
          verd == "KILL_FAIL",
          "preregistered test: %s  (fixed d never yields RHS<2; "
          "reserve shrinks with N; cluster at 1/2)" % verd)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("HIGH MOMENT INERTIA %sVERIFIED" % (
            "SMOKE " if smoke else ""))
        return 0
    print("HIGH MOMENT INERTIA FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
