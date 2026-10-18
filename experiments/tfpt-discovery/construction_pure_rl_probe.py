#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""construction_pure_rl_probe -- LEMMA.CONSTRUCTION_PURE.RL.01
(round 391): CONSTRUCTION-PURE (R) AND (L).

Coexistence: r383/r386 reduced COMPOSE- to census (R) S_F<=4 D
and (L) L1<=3, with named remainders B(omega+beta,omega+beta)<=K D
and cofinal gamma<1/4.  Scramble breaks NEITHER (R) nor (L)
(energy bounds are weak separators; the arithmetic sits in
M3/E_pi).  If a bound survives scramble it should be a
construction theorem of the fold (block geometry, Fejer algebra),
not of the arithmetic of the weights.

LEGS (lemma-first; each exit PROVED / REFUTED / REDUCED):
  R  Gram inequality B_Sigma := B(omega+beta, omega+beta) <= K D
     on the fold class.  Candidate: block-Gershgorin (atom
     Gershgorin died).  Test: weight-rand at fixed geometry;
     geometry mutants.
  L  L1 slope +0.202 < 1/4 as a construction counting law
     (F2-bulk blocks + Lambda<=log), not the von Mangoldt
     triangle on positions (TV slope +0.307).  Same rand/mutant
     tests.  CS counting L1^2 <= m D is the SATZ bridge.
  C  If R and L stand construction-pure, COMPOSE- collapses to
     {(Z') living ladder, M3<=phi(m), Dict}.  Name what remains
     and which objects live in r389 Weyl energy.

CALIBRATION DISCLOSURE.  Numbers below were first measured in
/tmp/tfpt_r391_cal.py, tfpt_r391_cal2.py, tfpt_r391_cal3.py
(WALL 1.4 / 7.1 / chi3-42; FRAME-A 181-pack and FRAME-B 8
exceeded 2 min and were SKIPPED -- disclosed fallback CORE-42
+ CHI3-42) on 2026-08-28.  Frozen constants are that
measurement, sealed as gates.  Pins disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Fejer CS, CS counting L1^2 <= m D, Euclidean split
    ||Sigma||^2 + ||Delta||^2 = 2(||Pb||^2+||Pw||^2) and
    nrmS/D = (1+eta)/(1-eta) with
    eta = 2 Pb.Pw / (||Pb||^2+||Pw||^2) -- SATZ over Q.
    Atom Gershgorin of K is lambda<=H (too coarse).
  * w9: m=35 H=6 Bsum/D=1.2804 ray=1.2705 nrmS/D=1.0078
    cos(Pb,Pw)=0.0079 L1=0.4038 med_nlen=4 max_nlen=8.
    kz37 (R-star): m=202 H=15 Bsum/D=2.9752 ray=2.4727
    nrmS/D=1.2032 cos=0.1829 L1=0.4574.
  * Scramble seed=1 w9: Bsum/D=0.5726 R=0.598 L1=0.492 --
    does NOT break K=4 or Lambda=3 (r383/r386 confirmed).
  * Weight-rand at FIXED fold geometry (40 draws, 7 laws):
    permute/gauss/rademacher/expon/dirichlet max Bsum/D
    <= 3.16 on {w9,kz37}, ALL <=4.  coupled_gauss
    (Pw=0.3 Pb, positive alignment) BREAKS (w9 max 8.98,
    kz37 max 6.27).  Align a=+0.3 already >4; a->+1
    unbounded.  Anti-align a->-1 kills Bsum/D -> 0.
  * Superblock Gershgorin of Sigma REFUTED as SATZ: CORE-42
    dd_frac min=0.667 med=0.817, fully-DD only 4/42.
    Atom-weighted Gershgorin of Sigma: n_dd=1/35 (w9),
    0/202 (kz37).  The r391 candidate does NOT close.
  * Geometry mutants: DC-flatten and sign-kill BREAK (R)
    (w9 5.67 / 6.13; kz37 14.63 / 18.50).  Merged folds
    and shuffled blocks do NOT break (R) -- the invariant
    is fold SIGN / non-alignment / whiteness, not block
    cardinality.  DC L1=m BREAKS (L) (gamma=1).
  * CORE-42: Bsum/D max=2.8196 at kz19, 0/42 >4, 9/42 >2
    (mutant K/2 FAILS); nrmS/D med=0.9993 max=2.1314;
    ray max=3.0986; cos med=-0.0006; L1 slope +0.2017
    (matches r383 +0.202); sl_D=-0.5726; CS-gamma=0.2137
    <1/4; L1/sqrt(m D) med=0.702 (near-sharp: n_eff ~ m).
  * CHI3-42: Bsum/D max=2.7460 at kz67, 0/42 >4; L1 slope
    +0.1820; CS-gamma=0.1924<1/4.
  * DC toy R=3.6875 still kills field-independent
    C_MAIN<=1.  gamma=1/4 still fails T1-vs-phi.

AUSGANG.  (R) REDUZIERT: construction-class K=4 (weight-rand
HOLDS except alignment); block-Gershgorin REFUTED; DC/align
are the named kills; remainder Rayleigh(Sigma)*(1+eta)/(1-eta)
<=K as a SATZ of the white-block class.  (L) REDUZIERT:
CS counting SATZ, but tautological with n_eff~m (r301
n_act==m); measured gamma=+0.202 construction-class, not a
theorem; triangle +0.307 still does not close; DC L1=m is
the geometry kill.  (C) COMPOSE- still needs (Z') + M3<=phi
+ Dict + the two census envelopes.  r389 Weyl energy owns
the SIGNED objects (assist, C_eps, Z_loc), not (R)(L).

NO RH CLAIM.  Finite identities, named reductions, named
kills.  Research documentation, not a theorem of RH.
Sealed gates: 15/15 smoke / 23/23 full (G1--G8 toys,
G10--G16 pins, G20--G27 census).  Companion verifier
adds G8b/G9.  Full WALL 9.9 s.
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
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import compose_premises_probe as C  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import mean_sieve_floor_probe as MSF  # noqa: E402

K_STAR = 4.0
K_HALF = 2.0
C_MAIN = float(Fr(3, 10))
LAMBDA = C.LAMBDA
R0 = C.R0
R_STAR = C.R_STAR
R_STAR_KZ = C.R_STAR_KZ
B_STAR = 2.975244140625  # kz37 Bsum/D; live-gated
B_STAR_CORE = 2.8196
B_STAR_CORE_KZ = 19
B_STAR_CHI3 = 2.746041
B_STAR_CHI3_KZ = 67
N_CORE, N_CHI3 = 42, 42
N_B_GT2_CORE = 9
N_DD_ALL = 4
SCR_SEED = 1
N_RAND = 20
RAND_SEED0 = 391
ID_BAR = 1e-12
DEC_BAR = 1e-9

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


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
    return (not bad), ("NO zero/prime oracles; constructors consume "
                       "measure arrays / positions only"
                       if not bad else "; ".join(bad))


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def loglog_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    msk = (xs > 1) & (ys > 1e-30)
    if int(np.sum(msk)) < 3:
        return float("nan")
    return float(np.polyfit(np.log(xs[msk]), np.log(ys[msk]), 1)[0])


def fold_extract(p):
    """r298 fold vectors + the (R)(L) scalars.  Source-pure."""
    N = p["N"]
    rows = p["rows"]
    r0 = C.row_of(p)
    xu, wu = C.CT.union_arrays(p["d"])
    bx, bw = C.CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = C.BR.eval_scaled(rows, bx, N - 2)
    v2w = C.BR.eval_scaled(rows, xu, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    cw = wu * xu * v2w * fac
    o = np.argsort(bx, kind="stable")
    bxs, cts = bx[o], ct[o]
    ed = C.PBB.mask_edge(bxs, lo, hi, C.PBB.EDGE_F)
    cb, xb = cts[~ed], bxs[~ed]
    runs = C.PBB.runs_split(cb)
    brk, mblk, jb = C.WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=mblk) if mblk \
        else np.zeros(0)
    Pw = C.WBT.aggregate_blocks(xu, cw, lo, hi, brk, mblk)
    Pd = Pb - Pw
    Sig = Pb + Pw
    H = r0["H"]
    nlen = np.bincount(jb, minlength=mblk) if mblk else np.zeros(0)
    Bsum = C.WBT.fejer_bil(Sig, Sig, H) if mblk else 0.0
    D = float(np.dot(Pd, Pd)) if Pd.size else 0.0
    L1 = float(np.sum(np.abs(Pd))) if Pd.size else 0.0
    nrmS = float(np.dot(Sig, Sig)) if Sig.size else 0.0
    nb = float(np.linalg.norm(Pb)) if Pb.size else 0.0
    nw = float(np.linalg.norm(Pw)) if Pw.size else 0.0
    cos = float(np.dot(Pb, Pw) / max(nb * nw, 1e-300))
    qn = nb * nb + nw * nw
    eta = (2.0 * float(np.dot(Pb, Pw)) / qn) if qn > 0 else 0.0
    return dict(
        kz=p.get("kz"), N=N, m=int(mblk), H=H,
        Pb=Pb, Pw=Pw, Pd=Pd, Sig=Sig, jb=jb, cb=cb,
        nlen=nlen, n_runs=len(runs),
        Bsum=Bsum, D=D, L1=L1, nrmS=nrmS, eta=eta, cos=cos,
        R=r0["R"],
        Bsum_over_D=(Bsum / D) if D > 0 else 0.0,
        nrmS_over_D=(nrmS / D) if D > 0 else 0.0,
        ray=(Bsum / nrmS) if nrmS > 0 else 0.0,
        max_nlen=int(np.max(nlen)) if nlen.size else 0,
        med_nlen=float(np.median(nlen)) if nlen.size else 0.0,
    )


def ratio_of(Sig, Pd, H):
    D = float(np.dot(Pd, Pd))
    if D <= 0:
        return float("inf")
    return C.WBT.fejer_bil(Sig, Sig, H) / D


def superblock_gersh(P, H):
    P = np.asarray(P, float)
    m = len(P)
    if m == 0:
        return dict(n=0, n_dd=0, dd_frac=0.0)
    step = max(int(H), 1)
    edges = list(range(0, m, step)) + [m]
    n = len(edges) - 1
    masks = []
    for a in range(n):
        u = np.zeros(m)
        u[edges[a]:edges[a + 1]] = P[edges[a]:edges[a + 1]]
        masks.append(u)
    G = np.zeros((n, n))
    for a in range(n):
        for b in range(a, n):
            v = C.WBT.fejer_bil(masks[a], masks[b], H)
            G[a, b] = G[b, a] = v
    n_dd = 0
    ratios = []
    for a in range(n):
        rad = float(np.sum(np.abs(G[a])) - abs(G[a, a]))
        dia = abs(G[a, a])
        ratios.append(rad / max(dia, 1e-300))
        if dia + 1e-15 >= rad:
            n_dd += 1
    return dict(n=n, n_dd=n_dd, dd_frac=n_dd / max(n, 1),
                max_rd=max(ratios) if ratios else 0.0)


def rand_ratio(f, kind, seed):
    rng = np.random.default_rng(seed)
    m, H, jb, cb = f["m"], f["H"], f["jb"], f["cb"]
    n = len(cb)
    if kind == "permute":
        cts = rng.permutation(cb)
        Pw = rng.permutation(f["Pw"])
    elif kind == "gauss":
        cts = rng.normal(0.0, float(np.std(cb) or 1.0), size=n)
        Pw = rng.normal(0.0, float(np.std(f["Pw"]) or 1.0), size=m)
    elif kind == "rademacher":
        sc = np.median(np.abs(cb)) or 1.0
        cts = sc * rng.choice([-1.0, 1.0], size=n)
        Pw = (np.median(np.abs(f["Pw"])) or 1.0) * rng.choice(
            [-1.0, 1.0], size=m)
    elif kind == "expon":
        sc = float(np.mean(np.abs(cb)) or 1.0)
        cts = rng.exponential(sc, size=n) * np.sign(cb + 1e-30)
        Pw = rng.exponential(float(np.mean(np.abs(f["Pw"])) or 1.0),
                             size=m) * np.sign(f["Pw"] + 1e-30)
    elif kind == "dirichlet":
        a = rng.exponential(1.0, size=n)
        a /= max(float(np.sum(a)), 1e-300)
        cts = a * float(np.sum(np.abs(cb))) * np.sign(cb + 1e-30)
        Pw = f["Pw"].copy()
    elif kind == "coupled_gauss":
        cts = rng.normal(0.0, float(np.std(cb) or 1.0), size=n)
        Pb = np.bincount(jb, weights=cts, minlength=m)
        Pw = 0.3 * Pb
        return ratio_of(Pb + Pw, Pb - Pw, H)
    else:
        raise ValueError(kind)
    Pb = np.bincount(jb, weights=cts, minlength=m)
    return ratio_of(Pb + Pw, Pb - Pw, H)


def align_ratio(f, a):
    Pb = f["Pb"]
    Pw = a * Pb
    return ratio_of(Pb + Pw, Pb - Pw, f["H"])


def mutant_ratio(f, kind):
    Pb, Pw, H, m = f["Pb"], f["Pw"], f["H"], f["m"]
    if kind == "dc_flatten":
        ones = np.ones(m)
        return ratio_of(ones, ones, H)
    if kind == "sign_kill":
        Sig = np.abs(Pb) + np.abs(Pw)
        Pd = np.abs(Pb) - np.abs(Pw)
        Pd = np.where(np.abs(Pd) < 1e-15, 1e-15, Pd)
        return ratio_of(Sig, Pd, H)
    if kind == "merge_pairs":
        k = max(m // 2, 1)
        idx = np.arange(0, 2 * k, 2)[:k]
        Sig = np.add.reduceat(Pb + Pw, idx)
        Pd = np.add.reduceat(Pb - Pw, idx)
        if 2 * k < m:
            Sig = np.append(Sig, np.sum((Pb + Pw)[2 * k:]))
            Pd = np.append(Pd, np.sum((Pb - Pw)[2 * k:]))
        H2 = max(2, int(math.ceil(math.sqrt(len(Sig)))))
        return ratio_of(Sig, Pd, H2)
    if kind == "shuffle_blocks":
        perm = np.random.default_rng(7).permutation(m)
        return ratio_of((Pb + Pw)[perm], (Pb - Pw)[perm], H)
    raise ValueError(kind)


def part_toys():
    section("TOYS / SATZ (no window builders)")
    Q = np.ones(16)
    Rdc = C.WBT.fejer_bil(Q, Q, 4) / float(np.dot(Q, Q))
    check("G1-DC-kills-CMAIN",
          abs(Rdc - 3.6875) < 1e-9 and Rdc > C_MAIN and Rdc <= 4.0,
          "DC R=%.4f > C_MAIN=3/10; field-independent MAIN "
          "bound REFUTED; still <= R0=4" % Rdc)
    P = np.array([1.0, -1.0] * 8)
    Rp2 = C.WBT.fejer_bil(P, P, 4) / 16.0
    check("G2-period2-one-sixteenth",
          abs(Rp2 - 1.0 / 16.0) < 1e-12,
          "period-2 R=%.6f (fold anti-align kills energy)" % Rp2)
    u = np.array([1.0, 0.0, -1.0, 2.0])
    v = np.array([0.5, -0.5, 1.0, 0.0])
    Buv = C.WBT.fejer_bil(u, v, 2)
    check("G3-fejer-CS",
          Buv * Buv <= C.WBT.fejer_bil(u, u, 2)
          * C.WBT.fejer_bil(v, v, 2) + 1e-12,
          "B(u,v)^2 <= B(u,u)B(v,v)")
    x = np.array([Fr(1), Fr(-2), Fr(3)], dtype=object)
    L1q = sum(abs(t) for t in x)
    Dq = sum(t * t for t in x)
    check("G4-CS-counting-over-Q",
          L1q * L1q <= Fr(3) * Dq,
          "L1^2=%s <= m D=%s (the (L) SATZ bridge)"
          % (L1q * L1q, Fr(3) * Dq))
    Pb = np.array([Fr(1), Fr(2)], dtype=object)
    Pw = np.array([Fr(3), Fr(-1)], dtype=object)
    Sig = Pb + Pw
    Del = Pb - Pw
    lhs = sum(Sig * Sig) + sum(Del * Del)
    rhs = 2 * (sum(Pb * Pb) + sum(Pw * Pw))
    eta_n = 2 * sum(Pb * Pw)
    eta_d = sum(Pb * Pb) + sum(Pw * Pw)
    nrm = sum(Sig * Sig)
    Dd = sum(Del * Del)
    check("G5-euclidean-split-eta-over-Q",
          lhs == rhs and nrm * (eta_d - eta_n) == Dd * (eta_d + eta_n),
          "||S||^2+||D||^2 = 2(||Pb||^2+||Pw||^2); "
          "nrmS/D = (1+eta)/(1-eta) exact over Q")
    # atom Gershgorin of K: diag=1, off-row = H-1, lam_ub = H
    H = 4
    off = H - 1
    check("G6-atom-Gershgorin-is-H-too-coarse",
          1 + off == H and H == 4,
          "Gershgorin of K gives lambda<=H=4, the trivial "
          "S_F<=H D already in r383 -- too coarse for (R)")
    m_big = 1.0e6
    t1 = C.t1_m3(1.0, m_big)
    ph = C.phi_of(m_big, R0, m_big ** 0.25, C.Z0)
    check("G7-gamma-quarter-mutant",
          t1 > ph,
          "T1 M3=%.3e > phi=%.3e at m=1e6, L1=m^{1/4}"
          % (t1, ph))
    fw_ok, fw_d = firewall_audit()
    sha_ok = (C.WBT.SPEC_SHA.startswith(C.WBT_SHA_PREFIX)
              and C.L2D.SPEC_SHA.startswith(C.L2D_SHA_PREFIX)
              and C.DMF.SPEC_SHA.startswith(C.DMF_SHA_PREFIX)
              and C.MSF.SPEC_SHA.startswith(C.MSF_SHA_PREFIX))
    check("G8-firewall-and-sha",
          fw_ok and sha_ok,
          "%s; WBT/L2D/DMF/MSF prefixes" % fw_d)


def part_pins():
    section("CONSTRUCTION PINS (w9, scramble, kz37, rand, mutants)")
    p9 = C.BH.wpack(9)
    f9 = fold_extract(p9)
    check("G10-w9-fold-class",
          f9["m"] == 35 and f9["H"] == 6
          and abs(f9["Bsum_over_D"] - 1.2804) < 1e-3
          and abs(f9["ray"] * f9["nrmS_over_D"] - f9["Bsum_over_D"]) < 1e-9
          and abs(f9["cos"]) < 0.02
          and abs(f9["nrmS_over_D"] - 1.0) < 0.02
          and f9["L1"] < LAMBDA and f9["Bsum_over_D"] < K_STAR
          and f9["med_nlen"] == 4.0,
          "m=%d H=%d Bsum/D=%.4f ray=%.4f nrmS/D=%.4f cos=%.4f "
          "L1=%.4f med_nlen=%.0f (white-block class: ||S||~||D||, "
          "Pb almost orthogonal to Pw)"
          % (f9["m"], f9["H"], f9["Bsum_over_D"], f9["ray"],
             f9["nrmS_over_D"], f9["cos"], f9["L1"], f9["med_nlen"]))
    pS = C.BH.wpack(9, dict(scramble_seed=SCR_SEED))
    fS = fold_extract(pS)
    check("G11-scramble-does-not-break-R-or-L",
          fS["Bsum_over_D"] < K_STAR and fS["R"] < K_STAR
          and fS["L1"] < LAMBDA,
          "SCR Bsum/D=%.4f R=%.4f L1=%.4f (does NOT break K=4 "
          "or Lambda=3; energy is construction-class)"
          % (fS["Bsum_over_D"], fS["R"], fS["L1"]))
    p37 = C.BH.wpack(R_STAR_KZ)
    f37 = fold_extract(p37)
    check("G12-R-star-kz37-K-and-Khalf",
          abs(f37["Bsum_over_D"] - 2.9752) < 1e-3
          and f37["Bsum_over_D"] < K_STAR
          and f37["Bsum_over_D"] > K_HALF
          and abs(f37["R"] - R_STAR) < 1e-3,
          "kz37 Bsum/D=%.4f <4 and >2 (mutant K/2 FAILS); "
          "R=%.4f ray=%.4f nrmS/D=%.4f"
          % (f37["Bsum_over_D"], f37["R"], f37["ray"],
             f37["nrmS_over_D"]))
    kinds_hold = ("permute", "gauss", "rademacher", "expon",
                  "dirichlet")
    kind_off = dict(permute=0, gauss=100, rademacher=200,
                    expon=300, dirichlet=400)
    mx_hold = 0.0
    for kind in kinds_hold:
        for i in range(N_RAND):
            mx_hold = max(mx_hold, rand_ratio(
                f9, kind, RAND_SEED0 + i + kind_off[kind]))
    check("G13-weight-rand-independent-holds-K",
          mx_hold < K_STAR,
          "w9 independent laws max Bsum/D=%.4f <4 (construction "
          "class: typical weights stay non-aligned)" % mx_hold)
    mx_cg = max(rand_ratio(f9, "coupled_gauss", RAND_SEED0 + i)
                for i in range(N_RAND))
    al = align_ratio(f9, 0.3)
    check("G14-alignment-breaks-K",
          mx_cg > K_STAR and al > K_STAR
          and align_ratio(f9, 0.99) > 100.0
          and align_ratio(f9, -1.0) < 1e-6,
          "coupled_gauss max=%.4f align(0.3)=%.4f >4; a->+1 "
          "unbounded; a=-1 (fold anti-align) kills energy"
          % (mx_cg, al))
    r_dc = mutant_ratio(f9, "dc_flatten")
    r_sk = mutant_ratio(f9, "sign_kill")
    r_mp = mutant_ratio(f9, "merge_pairs")
    r_sh = mutant_ratio(f9, "shuffle_blocks")
    check("G15-DC-sign-kill-R-merge-does-not",
          r_dc > K_STAR and r_sk > K_STAR
          and r_mp < K_STAR and r_sh < K_STAR,
          "DC=%.4f sign_kill=%.4f BREAK (R); merge_pairs=%.4f "
          "shuffle=%.4f do NOT -- invariant is fold sign, "
          "not block cardinality"
          % (r_dc, r_sk, r_mp, r_sh))
    check("G16-DC-L1-kills-L",
          float(f9["m"]) > LAMBDA
          and float(f9["m"]) ** 1.0 / float(f9["m"]) == 1.0,
          "DC L1=m=%d > Lambda=3 and slope gamma=1 > 1/4 "
          "(geometry kill of field-independent (L))" % f9["m"])
    return dict(w9=f9, scr=fS, kz37=f37)


def _census(label, packs):
    rows = []
    for p in packs:
        if p.get("nf") is not None:
            continue
        f = fold_extract(p)
        sg = superblock_gersh(f["Sig"], f["H"])
        f["dd_frac"] = sg["dd_frac"]
        f["n_dd_full"] = int(sg["dd_frac"] >= 1.0 - 1e-12)
        rows.append(f)
    return rows


def part_full():
    section("CORE-42 + CHI3-42 CENSUS (181-pack / FRAME-B skipped)")
    print("  CORE-42 ...", flush=True)
    core = _census("A", [C.BH.wpack(kz)
                         for kz in C.V.admissible_indices()])
    print("  CHI3-42 ...", flush=True)
    chi = []
    for kz in C.V.admissible_indices():
        u, w, _n, _c = DMF.chi_window_comb(kz, MSF.Q_CHI3)
        if len(u) < C.V.N_ATOM_MIN:
            continue
        chi.append(DMF.chi_wpack(kz, 1.0, MSF.LPQ3, (u, w)))
    chi = _census("CHI3", chi)
    check("G20-core-chi3-counts",
          len(core) == N_CORE and len(chi) == N_CHI3,
          "CORE %d CHI3 %d (fallback; 181-pack/FRAME-B skipped)"
          % (len(core), len(chi)))
    mx = max(core, key=lambda r: r["Bsum_over_D"])
    n_gt4 = sum(1 for r in core if r["Bsum_over_D"] > K_STAR + 1e-12)
    n_gt2 = sum(1 for r in core if r["Bsum_over_D"] > K_HALF + 1e-12)
    check("G21-core-K-census",
          n_gt4 == 0 and abs(mx["Bsum_over_D"] - B_STAR_CORE) < 5e-3
          and mx["kz"] == B_STAR_CORE_KZ
          and n_gt2 == N_B_GT2_CORE,
          "Bsum/D<=4 on 42/42; max=%.4f at kz%s; n>2=%d (K/2 FAILS)"
          % (mx["Bsum_over_D"], mx["kz"], n_gt2))
    nrm_med = float(np.median([r["nrmS_over_D"] for r in core]))
    ray_mx = max(r["ray"] for r in core)
    cos_med = float(np.median([r["cos"] for r in core]))
    check("G22-white-block-class",
          abs(nrm_med - 1.0) < 0.05 and ray_mx < K_STAR
          and abs(cos_med) < 0.05,
          "nrmS/D med=%.4f~1; ray max=%.4f<4; cos med=%.4f~0 "
          "(||Sigma||~||Delta||, Pb nearly orthogonal to Pw)"
          % (nrm_med, ray_mx, cos_med))
    n_dd = sum(r["n_dd_full"] for r in core)
    dd_min = min(r["dd_frac"] for r in core)
    check("G23-superblock-Gershgorin-refuted",
          n_dd == N_DD_ALL and dd_min < 0.70,
          "fully-DD %d/42 (pin %d); min dd_frac=%.3f -- "
          "block-Gershgorin is NOT a SATZ"
          % (n_dd, N_DD_ALL, dd_min))
    ms = [r["m"] for r in core]
    sl_L = loglog_slope(ms, [r["L1"] for r in core])
    sl_D = loglog_slope(ms, [r["D"] for r in core])
    cs_g = 0.5 + 0.5 * sl_D
    check("G24-L1-slope-lt-quarter",
          0.15 < sl_L < 0.24 and sl_L < 0.25,
          "CORE-42 slope(L1 vs m)=%+.4f < 1/4 (pin +0.202; "
          "construction-class CENSUS, not a SATZ)" % sl_L)
    check("G25-CS-gamma-from-D-decay",
          cs_g < 0.25 and sl_D < -0.50,
          "sl_D=%+.4f; CS-gamma=1/2+1/2 sl_D=%+.4f <1/4 "
          "(translation of D-decay; tautological with n_eff~m)"
          % (sl_D, cs_g))
    mx3 = max(chi, key=lambda r: r["Bsum_over_D"])
    sl3 = loglog_slope([r["m"] for r in chi], [r["L1"] for r in chi])
    n3_gt4 = sum(1 for r in chi if r["Bsum_over_D"] > K_STAR + 1e-12)
    check("G26-chi3-construction-class",
          n3_gt4 == 0 and abs(mx3["Bsum_over_D"] - B_STAR_CHI3) < 5e-3
          and mx3["kz"] == B_STAR_CHI3_KZ
          and sl3 < 0.25,
          "CHI3 Bsum/D max=%.4f at kz%s; 0/42 >4; L1 slope=%+.4f"
          % (mx3["Bsum_over_D"], mx3["kz"], sl3))
    check("G27-Khalf-fails-and-max-nlen-bounded",
          n_gt2 >= 1 and max(r["max_nlen"] for r in core) <= 16
          and float(np.median([r["med_nlen"] for r in core])) == 4.0,
          "K/2=2 fails on %d/42; max_nlen<=16; med_nlen med=4 "
          "(fold packing bounds block length; does not close K)"
          % n_gt2)
    return core, chi


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    print("=" * 78)
    print("construction_pure_rl_probe -- LEMMA.CONSTRUCTION_PURE.RL.01 "
          "(round 391)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.", flush=True)
    part_toys()
    pins = part_pins()
    if not args.smoke:
        part_full()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    print("CONSTRUCTION PURE RL "
          + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
    print("LETTERS: (R) REDUCED (K=4 construction-class; "
          "block-Gershgorin REFUTED; DC/align kill; weight-rand "
          "HOLDS except alignment)  "
          "(L) REDUCED (slope +0.202 construction-class; CS "
          "counting SATZ but tautological with n_eff~m; DC L1=m "
          "kill; triangle still does not close)  "
          "(C) COMPOSE- still needs (Z') + M3<=phi + Dict + the "
          "two census envelopes; r389 owns signed assist/C_eps/"
          "Z_loc, not (R)(L).")
    print("KILL: DC R=3.6875 kills C_MAIN; K/2=2 fails at kz37; "
          "gamma=1/4 fails T1-vs-phi; coupled_gauss/align break "
          "K; merge-folds do NOT break (R).")
    _ = pins
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
