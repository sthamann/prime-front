#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""p1_overload_probe --
PRIME.RDAGGER.P1_OVERLOAD.01 (round 435, reviewer DCCCII
first half of the two-case inertia theorem, source-pure,
no margin).

THE LEMMA (reframe).  n_-(A0) <= 1 on the selected
sequence -- NOT n_- = 1 (the 29 vacuous windows are the
first case of the theorem).  Holds 74/74 + living chi +
dead chi (nC in {0,1}).  The danger class nC >= 2 was
never seen except on destroyed worlds.

QUESTION.  Which source property forbids TWO negative
directions?  Not "why is lambda_min positive".

LEGS.
  A  Depth chain of the mu-only dual CD Gram C(n) on Y,
     n = 1..N_w-3.  Constructor identity: C(n) = B[:,:n]
     B[:,:n]^T so C(n+1)-C(n) = v v^T (rank-1 PSD).
     nC(n) := #{lam(C(n)) < 1} is antitone and drops by
     at most 1 (Cauchy / rankOne_inertia_antitone).
     Dictionary nC(N_w-3) = n_-(A0) (r407/r412).
     NEW COORDINATE: nC(|Y|) vs nC(N_w-3).
  B  Gantmacher-Krein / sign-regularity of the r431
     Cauchy-pi residual D0 = W_Y - S0 at kdim=0.
     Q-exact 2x2 and 3x3: is there a proveable n_- cap?
  C  Adversary mechanism in the same depth coordinate.
  D  Kills: no margin correlations; Q-toys for every
     signature claim; false depth; dead chi consistency.

CALIBRATION.  Q inertias, w9 nC curve, permute/scramble/
two-period, core-42, chi, false-depth first measured in
/tmp (r435_cal.py, r435_cal2.py, r435_cal3.py) on the
r407 chain_C / r409 S0_Q constructors, 2026-08-30.
Frozen floors below are that measurement, sealed as
gates.  Pins disclosed.  Builder fallback NOT taken:
full wall 13.6 s (bar 120 s).  23/23 full / 20/20 smoke.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Q 2x2 r409 toy kdim=0: D0 inertia (1,1,0),
    det = -3740/243 < 0, D11 = -1744/2025; S0 and P_X
    PD; pi'(Y) = (-1/2, 1/2).  Depth 2->3 lifts to
    (2,0,0); D0(3)-D0(2) inertia (1,0,1).
  * Q 2x2 ND witness (mass-imbalanced dual): inertia
    (0,2,0), det = 113/2880000 > 0 -- even 2x2 n_- <= 1
    is NOT a Cauchy-pi identity.
  * Q 3x3 second toy: kdim=0 inertia (1,2,0); depth
    3,4,5 gives nneg 2,1,0 (interlacing lift).
  * w9: nC(1)=104, nC(|Y|)=43, nC(181)=1, hit1=178;
    last six nC = (2,2,1,1,1,1); dictionary nC=nneg=1.
    Rank-1 sample: every tested update rank 1.
  * PERM nC(|Y|)=54 nCend=20 hit1=None; JITTER 19;
    SCRAMBLE 21; 2PER nmax=8 < nY=11 nCend=4.
  * Core-42: 42/42 nCend in {0,1}, P1 28 / VAC 14.
    P1 slack nmax-hit1 <= 6; VAC slack nmax-hit0 <= 3.
  * Dead chi3 nCend in {0,1}; living chi3-9 nCend=0.
  * False depth: N_w-1 nC=0 on MAIN (the leftover
    square is liftable by extra OP).

AUSGANG DEPTH_CHAIN_EXACT / GK_UNIVERSAL_REFUTED /
SAVE_RATE_CENSUS.  SATZ: nested CD is rank-1 Loewner
and nC drops by at most 1.  REFUTED: Cauchy-pi / GK
as a universal n_- <= 1 cap (2x2 ND + 3x3 nneg=2).
REDUZIERT: P1 is the crossing-budget of the mu-CD
chain on Y by degree N_w-3 (the unique interpolant
at d=|Y| still has nC >> 1).  Does not prove the
save-rate.  No RH claim.

MACHINERY: r407 DI chain_C / b_matrix nested Gram;
r409 B.S0_Q / pack_graph / toy_dual; r431 S
dressed_ITT_Q / inertia_fr; r403 P1.reweight;
r398 HM scramble / two_period / chi_mz.

NO RH CLAIM.  Finite identities, one named refutation,
one named census.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
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

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
S_SHA_PREFIX = "64eabb7c"

FLOOR = 1.0 - 1e-12
CORE_N, P1_N, VAC_N = 42, 28, 14
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
CHI4_LIVE_N, CHI4_DEAD_N = 41, 1
W9_NC1, W9_NCY, W9_NCEND, W9_HIT1, W9_NMAX = 104, 43, 1, 178, 181
W9_LAST = (2, 2, 1, 1, 1, 1)
PERM_NCY_LO, PERM_NCEND, JIT_NCEND_LO = 50, 20, 15
SCR_NCEND, TP_NCEND, TP_NMAX, TP_NY = 21, 4, 8, 11
P1_SLACK_MAX, VAC_SLACK_MAX = 6, 3
W9_CMIN_LO, W9_CMIN_HI = 0.85, 0.87
DET_TOY = Fr(-3740, 243)
D11_TOY = Fr(-1744, 2025)
DET_ND = Fr(113, 2880000)
D00_ND = Fr(-257, 14400)
D11_ND = Fr(-1, 72)
TR_ND = Fr(-457, 14400)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("nested_C", "second_toy", "nd_toy")


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
    return (not bad), ("NO zero/prime oracles; nested CD / "
                       "S0_Q / chain_C only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"eigvalsh", "eigh", "svd", "cholesky", "pack_C",
              "pack_graph", "r_nm3", "norm"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ---------- source-pure constructors (AST-audited) ----------
def nested_C(Bm, n):
    """Prefix Gram of the mu-OP matrix.  Only a slice of B."""
    Bn = Bm[:, :n]
    G = Bn @ Bn.T
    return 0.5 * (G + G.T)


def second_toy():
    """Independent 6-node kdim=0 window (r431-audit Q3)."""
    xs = [Fr(-3, 2), Fr(-1), Fr(-1, 3), Fr(1, 5), Fr(2, 3), Fr(3, 2)]
    u = [Fr(1), Fr(4), Fr(9), Fr(16), Fr(25), Fr(36)]
    iX, iY = [0, 2, 5], [1, 3, 4]
    Pprime = []
    for j, xj in enumerate(xs):
        pr = Fr(1)
        for k, xk in enumerate(xs):
            if k != j:
                pr *= (xj - xk)
        Pprime.append(pr)
    ud = [Fr(1) / (u[j] * Pprime[j] * Pprime[j]) for j in range(6)]
    return xs, ud, iX, iY


def nd_toy():
    """Mass-imbalanced 5-node dual, 2 holes, kdim=0."""
    xs = [Fr(-2), Fr(-1), Fr(0), Fr(1), Fr(2)]
    u = [Fr(1), Fr(100), Fr(100), Fr(100), Fr(1)]
    iX, iY = [0, 1, 4], [2, 3]
    Pprime = []
    for j, xj in enumerate(xs):
        pr = Fr(1)
        for k, xk in enumerate(xs):
            if k != j:
                pr *= (xj - xk)
        Pprime.append(pr)
    ud = [Fr(1) / (u[j] * Pprime[j] * Pprime[j]) for j in range(5)]
    return xs, ud, iX, iY


# ---------- measurement (eig allowed) ----------
def nC_at(Bm, n):
    ev = np.linalg.eigvalsh(nested_C(Bm, n))
    return int(np.sum(ev < FLOOR)), ev


def hit_first(Bm, nmax, target_le):
    lo, hi, ans = 1, nmax, None
    while lo <= hi:
        mid = (lo + hi) // 2
        nc, _ = nC_at(Bm, mid)
        if nc <= target_le:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


def ensure_xp(mz):
    if "xp" in mz:
        return mz
    pos = np.asarray(mz["wu"]) > 0
    out = dict(mz)
    out["xp"] = np.asarray(mz["xu"])[pos]
    out["wp"] = np.asarray(mz["wu"])[pos]
    return out


def world_row(mz):
    mz = ensure_xp(mz)
    nmax = int(mz["Nw"]) - 3
    _C, meta = DI.chain_C(mz, n=nmax)
    Bm = meta["B"]
    nY = Bm.shape[0]
    n1, _ = nC_at(Bm, 1)
    nYc, _ = nC_at(Bm, min(nY, nmax))
    nE, evE = nC_at(Bm, nmax)
    last = tuple(nC_at(Bm, n)[0]
                 for n in range(max(1, nmax - 5), nmax + 1))
    rnk_ok, loew_min = True, 0.0
    for n in (2, min(nY, nmax), nmax):
        if n < 2 or n > nmax:
            continue
        dlt = nested_C(Bm, n) - nested_C(Bm, n - 1)
        evd = np.linalg.eigvalsh(0.5 * (dlt + dlt.T))
        loew_min = min(loew_min, float(evd[0]))
        if int(np.sum(evd > 1e-8)) != 1:
            rnk_ok = False
    return dict(Bm=Bm, nY=nY, nmax=nmax, nC1=n1, nCY=nYc, nCend=nE,
                cmin=float(evE[0]),
                c2=float(evE[1]) if len(evE) > 1 else float("nan"),
                hit1=hit_first(Bm, nmax, 1),
                hit0=hit_first(Bm, nmax, 0),
                last=last, rnk_ok=rnk_ok, loew_min=loew_min)


def chi_census(q, lpq, dead, live_n, dead_n):
    live, dead_rows = [], []
    for kz in V.admissible_indices():
        mz = HM.chi_mz(kz, q, lpq)
        if mz is None:
            continue
        r = world_row(mz)
        bucket = dead_rows if kz in dead else live
        bucket.append(r["nCend"])
    okL = (len(live) == live_n
           and all(n in (0, 1) for n in live))
    okD = (len(dead_rows) == dead_n
           and all(n in (0, 1) for n in dead_rows))
    return okL, okD, len(live), len(dead_rows), live, dead_rows


# ---------- parts ----------
def part_satz():
    section("S1  LEG B -- CAUCHY-PI / GK OVER Q")
    xs, u, ud, iX, iY, d0t, _lab = S.prime_toy()
    ys = [xs[i] for i in iY]
    S0k0, D0k0, _I, k0, _ = S.dressed_ITT_Q(xs, ud, iX, iY, 2)
    PX = S.cauchy_pick_Q([xs[i] for i in iX],
                         [ud[i] for i in iX], ys)
    det = D0k0[0][0] * D0k0[1][1] - D0k0[0][1] * D0k0[1][0]
    pi_pr = []
    for j, yj in enumerate(ys):
        pr = Fr(1)
        for k, yk in enumerate(ys):
            if k != j:
                pr *= (yj - yk)
        pi_pr.append(pr)
    check("G1-2x2-toy-one-neg",
          k0 == 0 and S.inertia_fr(D0k0) == (1, 1, 0)
          and S.inertia_fr(S0k0)[1] == 0
          and S.inertia_fr(PX)[1] == 0
          and D0k0[1][1] == D11_TOY and det == DET_TOY
          and pi_pr == [Fr(-1, 2), Fr(1, 2)],
          "inertia (1,1,0) det=%s Delta signs -+" % det)
    _S1, D01, _I1, k1, _ = S.dressed_ITT_Q(xs, ud, iX, iY, 3)
    dlt = B.fr_sub(D01, D0k0)
    check("G2-2x2-depth-lift",
          k1 == 1 and S.inertia_fr(D01) == (2, 0, 0)
          and S.inertia_fr(dlt) == (1, 0, 1),
          "d=3 PD; D0(3)-D0(2) rank-1 PSD")
    xs3, ud3, iX3, iY3 = second_toy()
    inns = []
    for d in (3, 4, 5):
        _S, D, _I, k, _ = S.dressed_ITT_Q(xs3, ud3, iX3, iY3, d)
        inns.append((k, S.inertia_fr(D)[1]))
    check("G3-3x3-GK-fail",
          inns == [(0, 2), (1, 1), (2, 0)],
          "nneg 2,1,0 -- universal n_-<=1 REFUTED at 3x3")
    xsN, udN, iXN, iYN = nd_toy()
    _Sn, D0n, _In, kn, _ = S.dressed_ITT_Q(xsN, udN, iXN, iYN, 2)
    detn = D0n[0][0] * D0n[1][1] - D0n[0][1] * D0n[1][0]
    trn = D0n[0][0] + D0n[1][1]
    check("G4-2x2-ND-witness",
          kn == 0 and S.inertia_fr(D0n) == (0, 2, 0)
          and detn == DET_ND and trn == TR_ND
          and D0n[0][0] == D00_ND and D0n[1][1] == D11_ND,
          "inertia (0,2,0) det=%s -- even 2x2 cap REFUTED" % detn)


def part_w9():
    section("S2  LEG A -- NESTED CD DEPTH CHAIN (w9)")
    mz = V.build_measures(9)
    r = world_row(mz)
    g = B.pack_graph(mz)
    check("G10-nested-rank1",
          r["rnk_ok"] and r["loew_min"] > -1e-10,
          "rank-1 sample; loewmin=%.1e" % r["loew_min"])
    check("G11-w9-nC-curve",
          r["nC1"] == W9_NC1 and r["nCY"] == W9_NCY
          and r["nCend"] == W9_NCEND and r["hit1"] == W9_HIT1
          and r["nmax"] == W9_NMAX and r["hit0"] is None,
          "nC 104 -> 43(|Y|) -> 1(181); hit1=178")
    check("G12-w9-dictionary",
          r["nCend"] == g["nneg"] == 1
          and W9_CMIN_LO <= r["cmin"] <= W9_CMIN_HI,
          "nC=nneg=1 Cmin=%.5f" % r["cmin"])
    check("G13-w9-last-six",
          r["last"] == W9_LAST,
          "n=176..181 nC=%s (2->1 at n=178)" % (r["last"],))
    yn = np.sort(np.asarray(g["yn"], float))
    nY = len(yn)
    sdelta = []
    for j in range(nY):
        d = yn[j] - yn
        d[j] = 1.0
        sdelta.append(int(np.prod(np.sign(d))))
    alt = [(-1) ** (nY - 1 - j) for j in range(nY)]
    check("G32-Delta-alternates",
          sdelta == alt,
          "ordered Y: pi' signs alternate (nY=%d)" % nY)
    return mz, r


def part_adversaries(mz9):
    section("S3  LEG C -- ADVERSARIES IN THE DEPTH COORDINATE")
    rP = world_row(P1.reweight(mz9, "permute", 1000))
    check("G20-permute-stuck",
          rP["nCY"] >= PERM_NCY_LO and rP["nCend"] == PERM_NCEND
          and rP["hit1"] is None and rP["rnk_ok"],
          "PERM nC(|Y|)=%d nCend=%d hit1=None (still dropping)"
          % (rP["nCY"], rP["nCend"]))
    rG = world_row(P1.reweight(mz9, "gauss", 431))
    check("G22-jitter-stuck",
          rG["nCend"] >= JIT_NCEND_LO and rG["hit1"] is None,
          "JITTER nCend=%d" % rG["nCend"])
    rS = world_row(HM.scramble_mz())
    check("G21-scramble-stuck",
          rS["nCend"] == SCR_NCEND and rS["hit1"] is None,
          "SCRAMBLE nY=%d nCend=%d" % (rS["nY"], rS["nCend"]))
    rT = world_row(HM.two_period_mz(21, 2.0 / 3.0))
    check("G23-twoperiod-short",
          rT["nmax"] == TP_NMAX and rT["nY"] == TP_NY
          and rT["nCend"] == TP_NCEND and rT["nmax"] < rT["nY"],
          "2PER nmax=%d < nY=%d nCend=%d (depth before |Y|)"
          % (rT["nmax"], rT["nY"], rT["nCend"]))
    return rP


def part_kills(mz9, r9):
    section("S4  LEG D -- FALSE DEPTH / LIFTABLE SQUARE")
    C2, m2 = DI.chain_C(mz9, n=int(mz9["Nw"]) - 2)
    nC2, ev2 = nC_at(m2["B"], int(mz9["Nw"]) - 2)
    C1, m1 = DI.chain_C(mz9, n=int(mz9["Nw"]) - 1)
    nC1, ev1 = nC_at(m1["B"], int(mz9["Nw"]) - 1)
    C4, m4 = DI.chain_C(mz9, n=int(mz9["Nw"]) - 4)
    nC4, _ = nC_at(m4["B"], int(mz9["Nw"]) - 4)
    check("G30-Nw-1-lifts",
          nC1 == 0 and float(ev1[0]) > 1.0,
          "n=N_w-1 nC=0 cmin=%.5f -- leftover square IS liftable"
          % float(ev1[0]))
    check("G31-object-at-Nm3",
          r9["nCend"] == 1 and nC4 == 1 and nC2 == 1
          and float(ev2[0]) < 1.0,
          "nC=1 at N_w-4,-3,-2; the cutoff N_w-3 is the object")


def part_census():
    section("S5  CORE-42 + CHI -- nC(N_w-3) IN {0,1}")
    core = list(V.admissible_indices())
    n0 = n1 = n_ge = 0
    sl1, sl0 = [], []
    rnk_all = True
    for kz in core:
        r = world_row(V.build_measures(kz))
        rnk_all = rnk_all and r["rnk_ok"]
        if r["nCend"] == 0:
            n0 += 1
            if r["hit0"] is not None:
                sl0.append(r["nmax"] - r["hit0"])
        elif r["nCend"] == 1:
            n1 += 1
            if r["hit1"] is not None:
                sl1.append(r["nmax"] - r["hit1"])
        else:
            n_ge += 1
    check("G40-core42-two-case",
          len(core) == CORE_N and n0 == VAC_N and n1 == P1_N
          and n_ge == 0 and rnk_all
          and (max(sl1) if sl1 else 0) <= P1_SLACK_MAX
          and (max(sl0) if sl0 else 0) <= VAC_SLACK_MAX,
          "42/42 nCend in {0,1}; P1 %d vac %d; slack P1<=%d VAC<=%d"
          % (n1, n0, max(sl1) if sl1 else -1,
             max(sl0) if sl0 else -1))
    okL, okD, nL, nD, live, dead = chi_census(
        DMF.Q_CHI3, DMF.LPQ3, HM.DEAD_CHI3,
        CHI3_LIVE_N, CHI3_DEAD_N)
    check("G41-chi3-live",
          okL, "live chi3 %d/%d nCend in {0,1}" % (nL, CHI3_LIVE_N))
    check("G42-chi3-dead",
          okD, "dead chi3 %d/%d nCend in {0,1} values=%s"
          % (nD, CHI3_DEAD_N, dead))
    okL4, okD4, nL4, nD4, _l4, d4 = chi_census(
        DMF.Q_CHI4, DMF.LPQ4, HM.DEAD_CHI4,
        CHI4_LIVE_N, CHI4_DEAD_N)
    check("G43-chi4",
          okL4 and okD4,
          "chi4 live %d/%d dead %d/%d nCend in {0,1} dead=%s"
          % (nL4, CHI4_LIVE_N, nD4, CHI4_DEAD_N, d4))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("p1_overload_probe -- "
          "PRIME.RDAGGER.P1_OVERLOAD.01 (round 435)")
    print("SPEC_SHA %s   (B %s / DI %s / HM %s / P1 %s / S %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], DI.SPEC_SHA[:16],
             HM.SPEC_SHA[:16], P1.SPEC_SHA[:16], S.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3/chi4)"))
    print("=" * 78)

    section("S0  FIREWALL + TARGET_LEAK")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and S.SPEC_SHA.startswith(S_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / DI %s / HM %s / P1 %s / S %s"
          % (B.SPEC_SHA[:8], DI.SPEC_SHA[:8], HM.SPEC_SHA[:8],
             P1.SPEC_SHA[:8], S.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))
    leak = []
    for fn in CONSTRUCTORS:
        leak.extend(scope_audit(fn))
    check("G00d-constructor-no-target",
          leak == [],
          "nested_C / toys: no eig/SVD/pack_C"
          if not leak else "; ".join(leak))

    part_satz()
    mz9, r9 = part_w9()
    part_adversaries(mz9)
    part_kills(mz9, r9)
    if smoke:
        section("S5  CENSUS skipped (--smoke)")
        check("G40-census-smoke-skip", True, "core/chi deferred")
    else:
        part_census()

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("DEPTH_CHAIN_EXACT / GK_UNIVERSAL_REFUTED / "
            "SAVE_RATE_CENSUS")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("P1 OVERLOAD %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("P1 OVERLOAD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
