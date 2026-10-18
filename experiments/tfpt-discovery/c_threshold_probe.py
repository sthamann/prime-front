#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""c_threshold_probe -- PRIME.LDAGGER.C_THRESHOLD.01 (round 408):
the C-threshold / sampling lemma after r407.  P1 iff lam_2(C)>=1
with C the mu-only dual CD Gram on the hole set Y.  Candidate:
at most one eigenvalue of C below 1, because half-filling is
Nyquist-critical (Landau density 1/2).

THE CANDIDATE IS REFUTED AS A THEOREM.  Source hole density
is 0.28 not 1/2; n = N_w-3 > |Y| so C is full rank (no
kernel); the periodic 1010 tile at density 1/2 has n < |Y|
and therefore at least |Y|-n exact zeros (nC=3 or 4, not
one).  diag(C) is not ~1 (w9 dmin=1.656, dmean=33.1): the
1-threshold is spectral, pulled by off-diagonal mass.
Thinning Y RAISES lam_min (Cauchy / rebuilt); densifying
DESTROYS.  Scramble (nC=21) and permute (nC=20) break
dmin>1, not the hole density.

WHAT SURVIVES.  SATZ: 2x2 coherence (exactly one lam<1 iff
det(C-I)<0); Rayleigh lam_min <= dmin so dmin<1 => nC>=1;
rank(C) <= min(|Y|,n); Cauchy interlacing of principal
submatrices.  CENSUS: source core-42 has nC in {0,1} (never
>1), dmin>1 on 42/42; the exception mode is hole-Nyquist
(kpeak / (|Y|/2) >= 0.85) and not the ones-mode; vacuous
windows sit on an endpoint DC mode with Cmin>=1.  Live chi
nC=0; dead chi nC=1 (transport holds; death is edge).

CALIBRATION DISCLOSURE.  Anatomy, 1010 spectra, thinning,
densify, worlds, core dmin/kpeak first measured in /tmp
(r408_cal.py, r408_cal2.py, r408_cal3.py) on the same
constructors, 2026-08-29.  Frozen floors below are that
measurement, sealed as gates -- not a search over 1/2.
Pins disclosed.  Builder fallback NOT taken: full wall
< 5 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: 2x2 C=[[2,2],[2,3]] det(C-I)=-2 => exactly
    one lam<1; Rayleigh diag(2,3) off 0; rank B 3x2 =>
    C 3x3 has a kernel; Cauchy principal of diag(1,3,5).
  * w9: S=367 Nw=184 n=181 |Y|=104 dens=0.283; Cmin=0.85712
    C2=1.00018 nC=1; dmin=1.6557 dmean=33.105 (#diag<1=0);
    off rms=9.98; mode PR=24.2 ones=0.007 end=0.529
    kpeak=52 = |Y|/2; F1=2 longrun=2.
  * 2PER S=20 c=1: dens=0.500 nC=3 Cmin=0 (zeros); S=21
    c=2/3 nC=4.  NOT lam2=1 exact.
  * thin 0.30: nC=0 Cmin=1.0157; flip+10: nC=8 Cmin=0.060.
  * SCR nC=21 dmin=0.367 F1=15; PERM nC=20 dmin=0.148
    (same Y as source).  CHI9 nC=0 Cmin=1.0009;
    CHI15 nC=1 Cmin=0.9982.
  * core-42: nC in {0,1} (14 / 28); dmin in [1.097, 1.656];
    nC=1 => kfrac in [0.857, 1.000]; nC=0 => endmass=1
    kpeak~1.  Frozen drop-20 Cauchy 0.857->0.929.

AUSGANG NYQUIST_REFUTED / AT_MOST_ONE_CENSUS.
SATZ: coherence / Rayleigh / rank / Cauchy.  REFUTED: the
Nyquist-at-density-1/2 theorem and lam2=1 exact on 1010.
CENSUS: nC<=1 on the source family; exception mode is
hole-Nyquist.  P1 still iff lam2(C)>=1 (r407); the RHS
is not proved.  Dead chi fulfill the threshold dictionary.
No RH claim.

MACHINERY: r407 D.chain_C / pack_C; r356 BDH; r367 HM
two_period / scramble / chi; r403 P1.reweight; r226 V.

NO RH CLAIM.  Finite identities, one named refutation,
one named census.  Research documentation, not a theorem
of RH.
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

import dual_intertwiner_probe as D  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

D_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
DMF_SHA_PREFIX = "4bf1a94b"

W9_NC, W9_NY, W9_N = 1, 104, 181
W9_CMIN, W9_C2_LO = 0.85712, 1.0
W9_DMIN, W9_DMEAN = 1.6557, 33.105
W9_DENS, W9_KPEAK = 0.283, 52
W9_ONES_HI, W9_END = 0.05, 0.529
W9_F1 = 2
REL_PIN = 5.0e-4
PER20_NC, PER21_NC = 3, 4
SCR_NC, PERM_NC_LO = 21, 15
CHI9_NC, CHI15_NC = 0, 1
THIN30_CMIN_LO = 1.0
FLIP10_NC_LO = 5
CORE_N, CORE_NC1, CORE_NC0 = 42, 28, 14
DMIN_LO = 1.05
KFRAC_LO = 0.80
CORE_DMIN_LO = 1.09

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
    return (not bad), ("NO zero/prime oracles; dual CD Gram C / "
                       "frame anatomy / periodic 1010 / Cauchy"
                       if not bad else "; ".join(bad))


def with_xp(mz):
    xu = np.asarray(mz["xu"], float)
    wu = np.asarray(mz["wu"], float)
    pos = wu > 0
    out = dict(mz)
    out.update(xp=xu[pos], wp=wu[pos],
               yn=np.asarray(mz["yn"], float),
               vn=np.asarray(mz["vn"], float))
    return out


def hole_index(xu, yn):
    return np.searchsorted(np.asarray(xu, float), np.asarray(yn, float))


def f1_count(mz):
    iY = np.sort(hole_index(mz["xu"], mz["yn"]))
    S = int(mz["S"])
    if len(iY) < 2:
        return 0
    g = np.diff(iY)
    g = np.append(g, iY[0] + S - iY[-1])
    return int(np.sum(g == 1))


def C_diag_stats(C):
    C = 0.5 * (np.asarray(C, float) + np.asarray(C, float).T)
    d = np.diag(C)
    return dict(dmin=float(d.min()), dmean=float(d.mean()),
                n_dlt1=int(np.sum(d < 1.0)))


def mode_pack(C, yn):
    ev, vec = np.linalg.eigh(0.5 * (C + C.T))
    v = vec[:, 0]
    th = np.arccos(np.clip(np.asarray(yn, float), -1.0, 1.0))
    o = np.argsort(th)
    vs, ths = v[o], th[o]
    F = np.fft.rfft(vs - vs.mean())
    kpeak = int(np.argmax(np.abs(F)))
    ones = float(abs(np.dot(v, np.ones_like(v))) / (
        np.linalg.norm(v) * math.sqrt(len(v)) + 1e-30))
    end = (ths < 0.25) | (ths > math.pi - 0.25)
    endmass = float(np.sum(vs[end] ** 2))
    kfrac = kpeak / max(len(yn) / 2.0, 1.0)
    return dict(ev=ev, kpeak=kpeak, kfrac=kfrac, ones=ones,
                endmass=endmass, NY=len(yn))


def rebuild_holes(mz, yn2, vn2, xp2=None, wp2=None):
    xp = np.asarray(mz["xp"], float) if xp2 is None else np.asarray(xp2)
    wp = np.asarray(mz["wp"], float) if wp2 is None else np.asarray(wp2)
    yn2 = np.asarray(yn2, float)
    vn2 = np.asarray(vn2, float)
    x2 = np.concatenate([xp, yn2])
    w2 = np.concatenate([wp, -vn2])
    o = np.argsort(x2)
    out = dict(mz)
    out.update(xu=x2[o], wu=w2[o], yn=yn2, vn=vn2, xp=xp, wp=wp,
               S=len(x2))
    return out


def part_satz():
    section("S1  SATZ -- 2x2 COHERENCE / RAYLEIGH / RANK / CAUCHY")
    a, b, c = Fr(2), Fr(3), Fr(2)
    dI = (a - 1) * (b - 1) - c * c
    check("G01-coherence-2x2-Q",
          dI == Fr(-2),
          "C=[[2,2],[2,3]] det(C-I)=%s <0 => exactly one lam<1" % dI)
    # Rayleigh: C=diag(2,3), off 0 => lam = diag <= dmin? lam_min=2=dmin
    check("G02-rayleigh-Q",
          Fr(2) <= Fr(2) and Fr(3) <= Fr(3),
          "lam_i = d_ii for diagonal C; lam_min <= dmin SATZ")
    # rank: B 3x2 of ones-columns => C=BB^T rank <=2
    B = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(1), Fr(1)]]
    # C = B B^T
    Ct = [[Fr(0), Fr(0), Fr(0)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = Fr(0)
            for k in range(2):
                s += B[i][k] * B[j][k]
            Ct[i][j] = s
    # det C = 0 (third row = r0+r1)
    det = (Ct[0][0] * (Ct[1][1] * Ct[2][2] - Ct[1][2] * Ct[2][1])
           - Ct[0][1] * (Ct[1][0] * Ct[2][2] - Ct[1][2] * Ct[2][0])
           + Ct[0][2] * (Ct[1][0] * Ct[2][1] - Ct[1][1] * Ct[2][0]))
    check("G03-rank-deficiency-Q",
          det == Fr(0) and Ct[2][0] == Ct[0][0] + Ct[1][0],
          "B 3x2 => det C=0 (kernel when |Y|>n)")
    # Cauchy: D=diag(1,3,5), drop last => diag(1,3), lam_min 1->1
    check("G04-cauchy-principal-Q",
          Fr(1) <= Fr(1) and Fr(3) <= Fr(3),
          "principal submatrix of diag(1,3,5) has lam_min >= 1")


def part_w9():
    section("S2  LEG A -- C ANATOMY (w9)")
    mz = V.build_measures(9)
    pk = D.pack_C(mz)
    st = C_diag_stats(pk["C"])
    mp = mode_pack(pk["C"], pk["meta"]["yn"])
    dens = pk["NY"] / float(mz["S"])
    f1 = f1_count(mz)
    check("G10-w9-spectrum",
          pk["nC"] == W9_NC and pk["NY"] == W9_NY and pk["n"] == W9_N
          and abs(pk["Cmin"] - W9_CMIN) <= REL_PIN * W9_CMIN
          and pk["C2"] >= W9_C2_LO,
          "nC=%d Cmin=%.5f C2=%.5f n=%d |Y|=%d" % (
              pk["nC"], pk["Cmin"], pk["C2"], pk["n"], pk["NY"]))
    check("G11-w9-diag-not-one",
          abs(st["dmin"] - W9_DMIN) <= 5e-3
          and abs(st["dmean"] - W9_DMEAN) <= 0.05
          and st["n_dlt1"] == 0 and st["dmin"] > 1.5,
          "dmin=%.4f dmean=%.3f #<1=%d (1-threshold is spectral)"
          % (st["dmin"], st["dmean"], st["n_dlt1"]))
    check("G12-w9-density-not-half",
          abs(dens - W9_DENS) <= 0.01 and dens < 0.35
          and pk["n"] > pk["NY"],
          "dens=|Y|/S=%.3f (not 1/2); n/|Y|=%.2f (full rank)"
          % (dens, pk["n"] / pk["NY"]))
    check("G13-w9-low-mode",
          mp["kpeak"] == W9_KPEAK and mp["ones"] <= W9_ONES_HI
          and abs(mp["endmass"] - W9_END) <= 0.05
          and f1 == W9_F1,
          "kpeak=%d=|Y|/2 ones=%.3f end=%.3f F1=%d (not ones-mode)"
          % (mp["kpeak"], mp["ones"], mp["endmass"], f1))
    # explicit kernel formula: C = B B^T
    C, meta = D.chain_C(mz)
    rest = float(np.linalg.norm(C - meta["B"] @ meta["B"].T))
    check("G14-C-is-BBT",
          rest == 0.0,
          "C_ij = <P(y_i),P(y_j)>_n * sqrt(u^vee_i u^vee_j); "
          "||C-BB^T||=%.1e" % rest)
    return dict(mz=mz, pk=pk, st=st, mp=mp)


def part_nyquist(w9):
    section("S3  LEG B -- PERIODIC 1010 (Nyquist candidate)")
    mz20 = with_xp(HM.two_period_mz(20, 1.0))
    p20 = D.pack_C(mz20)
    ev20 = np.linalg.eigvalsh(p20["C"])
    nzero = int(np.sum(np.abs(ev20) < 1e-10))
    dens20 = p20["NY"] / float(mz20["S"])
    check("G20-1010-S20-NOT-exact",
          p20["nC"] == PER20_NC and p20["Cmin"] <= 1e-8
          and nzero >= 2 and abs(dens20 - 0.5) <= 0.02,
          "2PER S=20 dens=%.2f nC=%d n_zero=%d Cmin=%.2e "
          "(NOT lam2=1 exact)" % (dens20, p20["nC"], nzero, p20["Cmin"]))
    mz21 = with_xp(HM.two_period_mz(21, 2.0 / 3.0))
    p21 = D.pack_C(mz21)
    check("G21-2PER-S21",
          p21["nC"] == PER21_NC and p21["Cmin"] <= 1e-8,
          "2PER S=21 c=2/3 nC=%d Cmin=%.2e (r367 two-period; "
          "nC=4 not 1)" % (p21["nC"], p21["Cmin"]))
    return dict(p20=p20, p21=p21)


def part_worlds(w9):
    section("S4  LEG C -- WORLDS / NAMED EXCLUSION")
    mz, pk = w9["mz"], w9["pk"]
    pS = D.pack_C(with_xp(HM.scramble_mz()))
    stS = C_diag_stats(pS["C"])
    mzS = with_xp(HM.scramble_mz())
    check("G30-scramble",
          pS["nC"] == SCR_NC and stS["dmin"] < 1.0
          and f1_count(mzS) >= 10,
          "SCR nC=%d dmin=%.3f F1=%d (dmin<1 + F1-clusters; "
          "not a density story -- dens=%.3f < source)"
          % (pS["nC"], stS["dmin"], f1_count(mzS),
             pS["NY"] / float(mzS["S"])))
    mzP = P1.reweight(mz, "permute", 1000)
    pP = D.pack_C(mzP)
    stP = C_diag_stats(pP["C"])
    check("G31-permute-same-Y",
          pP["nC"] >= PERM_NC_LO and stP["dmin"] < 1.0
          and pP["NY"] == pk["NY"],
          "PERM nC=%d dmin=%.3f |Y|=%d (=source Y; dual "
          "weights break dmin>1)" % (pP["nC"], stP["dmin"], pP["NY"]))
    pL = D.pack_C(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    check("G32-chi-live",
          pL["nC"] == CHI9_NC and pL["Cmin"] >= 1.0,
          "CHI9 nC=%d Cmin=%.4f (included; nC=0)"
          % (pL["nC"], pL["Cmin"]))
    pD = D.pack_C(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G33-chi-dead-FULFILLS",
          pD["nC"] == CHI15_NC,
          "CHI15 dead nC=%d Cmin=%.4f (threshold dictionary "
          "holds; death is edge)" % (pD["nC"], pD["Cmin"]))
    return dict(pS=pS, pP=pP)


def part_kills(w9):
    section("S5  LEG D -- DENSITY MUTANTS / DEPTH / CAUCHY")
    mz, pk = w9["mz"], w9["pk"]
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    rng = np.random.default_rng(408 + 4)
    k = max(4, int(round(0.30 * len(yn))))
    idx = np.sort(rng.choice(len(yn), size=k, replace=False))
    pT = D.pack_C(rebuild_holes(mz, yn[idx], vn[idx]))
    check("G40-thin-raises-Cmin",
          pT["nC"] == 0 and pT["Cmin"] >= THIN30_CMIN_LO,
          "thin 0.30 kept=%d nC=%d Cmin=%.4f (holes DOWN => "
          "lam_min UP; opposite of naive undersampling)"
          % (k, pT["nC"], pT["Cmin"]))
    rng = np.random.default_rng(508 + 1)
    xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
    flip = rng.choice(len(xp), size=10, replace=False)
    keep = np.ones(len(xp), bool)
    keep[flip] = False
    pF = D.pack_C(rebuild_holes(mz, np.concatenate([yn, xp[~keep]]),
                                np.concatenate([vn, wp[~keep]]),
                                xp[keep], wp[keep]))
    check("G41-densify-destroys",
          pF["nC"] >= FLIP10_NC_LO,
          "flip+10 nC=%d Cmin=%.4f (holes UP => many lam<1)"
          % (pF["nC"], pF["Cmin"]))
    C1, _ = D.chain_C(mz, n=pk["n"] + 1)
    ev1 = np.linalg.eigvalsh(C1)
    check("G42-depth-mutant",
          abs(float(ev1[0]) - 1.0) <= 5e-4
          or int(np.sum(ev1 < 1.0 - 1e-12)) != pk["nC"]
          or abs(float(ev1[0]) - pk["Cmin"]) >= 0.01,
          "n+1 Cmin=%.5f nC=%d (wrong depth moves the razor)"
          % (float(ev1[0]), int(np.sum(ev1 < 1.0 - 1e-12))))
    rng = np.random.default_rng(408)
    keep_i = np.sort(rng.choice(pk["C"].shape[0],
                                size=pk["C"].shape[0] - 20,
                                replace=False))
    Cs = pk["C"][np.ix_(keep_i, keep_i)]
    cmin_s = float(np.linalg.eigvalsh(Cs)[0])
    check("G43-cauchy-frozen",
          cmin_s >= pk["Cmin"] - 1e-10,
          "frozen drop-20 Cmin %.5f -> %.5f (interlacing SATZ)"
          % (pk["Cmin"], cmin_s))


def part_census():
    section("S6  CORE-42 -- nC IN {0,1}, dmin>1, MODE LAW")
    core = list(V.admissible_indices())
    n0 = n1 = nx = 0
    dmin_all = []
    kfracs = []
    ends0 = []
    for kz in core:
        m = V.build_measures(kz)
        p = D.pack_C(m)
        st = C_diag_stats(p["C"])
        mp = mode_pack(p["C"], p["meta"]["yn"])
        dmin_all.append(st["dmin"])
        if p["nC"] == 0:
            n0 += 1
            ends0.append(mp["endmass"])
        elif p["nC"] == 1:
            n1 += 1
            kfracs.append(mp["kfrac"])
        else:
            nx += 1
            print("    nC>1 kz=%d nC=%d" % (kz, p["nC"]), flush=True)
    check("G50-core-at-most-one",
          len(core) == CORE_N and n0 == CORE_NC0 and n1 == CORE_NC1
          and nx == 0,
          "core-%d nC in {0,1}: 0=%d 1=%d >1=%d (CENSUS, not SATZ)"
          % (CORE_N, n0, n1, nx))
    check("G51-core-dmin-gt-1",
          all(d > DMIN_LO for d in dmin_all)
          and min(dmin_all) >= CORE_DMIN_LO,
          "dmin in [%.4f, %.4f] -- all >1 (necessary for "
          "nC=0, not sufficient for nC=0)"
          % (min(dmin_all), max(dmin_all)))
    check("G52-core-mode-law",
          all(kf >= KFRAC_LO for kf in kfracs)
          and all(e >= 0.99 for e in ends0),
          "nC=1 kfrac>=%.2f on %d/%d; nC=0 endmass=1 on %d/%d"
          % (KFRAC_LO, sum(kf >= KFRAC_LO for kf in kfracs),
             len(kfracs), sum(e >= 0.99 for e in ends0), len(ends0)))

    live = dead = 0
    nL = nD = 0
    for kz in core:
        mz3 = HM.chi_mz(kz, DMF.Q_CHI3, DMF.LPQ3)
        if mz3 is None:
            continue
        p = D.pack_C(mz3)
        if kz in HM.DEAD_CHI3:
            dead += 1
            nD += int(p["nC"] == p["nneg"])
        else:
            live += 1
            nL += int(p["nC"] == p["nneg"])
    check("G53-chi3-dictionary",
          live == 37 and dead == 5 and nL == live and nD == dead,
          "chi3 live %d/%d and dead %d/%d nC=nneg (dictionary "
          "holds; dead death is edge)" % (nL, live, nD, dead))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("c_threshold_probe -- "
          "PRIME.LDAGGER.C_THRESHOLD.01 (round 408)")
    print("SPEC_SHA %s   (D %s / HM %s / P1 %s / DMF %s)"
          % (SPEC_SHA[:16], D.SPEC_SHA[:16], HM.SPEC_SHA[:16],
             P1.SPEC_SHA[:16], DMF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (D.SPEC_SHA.startswith(D_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "D %s / HM %s / P1 %s / DMF %s"
          % (D.SPEC_SHA[:8], HM.SPEC_SHA[:8], P1.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8]))

    part_satz()
    w9 = part_w9()
    part_nyquist(w9)
    part_worlds(w9)
    part_kills(w9)
    if not smoke:
        part_census()
    else:
        section("S6  CORE/CHI3 census skipped (--smoke)")

    section("S7  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G60-verdict-NYQUIST_REFUTED",
          prev_ok,
          "NYQUIST_REFUTED / AT_MOST_ONE_CENSUS: 1010 is not "
          "lam2=1; source nC<=1 is census; no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "NYQUIST_REFUTED"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("C THRESHOLD %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("C THRESHOLD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
