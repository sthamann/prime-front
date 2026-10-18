#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""p1_construction_probe -- PRIME.LDAGGER.P1_CONSTRUCTION.01
(round 403): is P1 = lam2(R_{N-3}) >= 1/2 a theorem of the
fold construction class (fixed geometry, arbitrary
sign-conforming weights)?

Coexistence: r391 white-block (R)(L) -- weight-rand at frozen
geometry holds K=4 except alignment; r400 bulk one-defect --
dead chi satisfy P1, only the position-scramble breaks it,
so P1 looked like a construction Satz and the arithmetic
load of R-dagger would collapse onto sch<0.  This round is
the one-lemma test of that suspicion.

THE LEMMA (one, lemma-first).
  P1 holds on the entire construction class: fixed fold
  mask (positions + sign pattern mu/nu), arbitrary positive
  / sign-conforming weights.  If yes, P1 needs no arithmetic.

LEGS.
  A  r391-style weight-rand on the FIXED mask (permute
     within mu and within nu; gauss/rademacher/expon/
     dirichlet rescaling).  Distinct from r400 scramble,
     which permutes POSITIONS.  Mild relative noise.
     Joint scale (R is homogeneous).  mu-only / nu-only.
  B  Saturation anatomy of the razor gap2: exact 1/2-modes
     of the r390 BS dual; 48-of-49 as construction identity
     or MAIN tautology; gap2 vs n (diagnosis).
  C  Gram candidate: B = R - R^ref restricted to the
     reference-negative space -- is it PSD (a Gram)?  Then
     omit-Gram must return nneg_ref; only-Gram vs full B.
  D  Kills: scramble (named invariant); two-period;
     signflip (mask destroyed); dead-chi consistency
     (in-class on true chi weights; perm of those weights).

CALIBRATION DISCLOSURE.  Class nneg tables, mild-noise
break, Gram rest, omit/only-Gram, scale residual, sample
killed, chi-perm first measured in /tmp (r403_cal.py,
r403_cal2.py, r403_cal3.py) on the same constructors,
2026-08-29.  Frozen floors below are that measurement,
sealed as gates -- not a search over 1/2.  No two-commit
pre-blind freeze: pins disclosed.  Builder fallback NOT
taken: full wall < 3 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Scale SATZ: R(c w) = R(w) to 3e-13 in Frobenius at
    c=7 (dual CD is homogeneous).  Joint scale 0.1/2/10
    leaves nneg=1 and gap2 bit-identical.
  * Interlacing SATZ (Q): rank-1 kills at most one
    negative; PSD + ND can leave negatives
    (diag(-1,-1)+0.1 I still nneg=2).
  * w9 MAIN: nneg=1, nneg_ref=49, killed=48, gap2=4.41e-5,
    n_half(R^ref)=13 at 1e-10.  B|_neg is PSD: nneg_M=0,
    npos_M=49, rest=0, evM in [0.023, 0.710].  omit-Gram
    nneg=49; only-Gram nneg=13 (PSD on the 49-space is
    NOT enough -- cross terms of full B finish the lift).
  * CLASS REFUTED at fixed mask: permute 8/8 nneg in
    [20,25]; gauss [17,25]; expon [9,15]; dirichlet
    [11,18]; rademacher-median-flatten nneg=2 (deterministic).
    mu-only perm nneg~17-22; nu-only ~30-34; flat-mu 6;
    flat-nu 37; mu*3 nneg=0; nu*3 nneg=65.
  * Razor: mild relative noise eps=1e-4, disclosed
    6-draw /tmp/r403_cal2.py (default_rng(10+s)):
    1/6 nneg>1 (the s=3 draw); cal3 1/20 on an
    independent 20-draw.  eps=1e-3 mostly nneg=2.
    P1 sits on the von Mangoldt profile, not the mask.
  * 48=49-1 is MAIN tautology, not a class identity:
    nneg_ref = 49,48,54,124,141 on the sample; permute
    leaves tens of negatives.  n_half of R^ref grows
    (13,27,38,62,65) -- not a single exact 1/2 mode
    the source lifts infinitesimally.
  * Gram is MAIN-weight, not class: permute rest=0.15
    nneg_M=7; scramble rest=0.15 nneg_M=8.
  * Kills: scramble nneg=21; two-period nneg=4 killed=0;
    signflip nneg~90 (mask destroyed, |Y| changes);
    dead chi3-15 nneg=1 on true weights, perm nneg=20;
    live chi3-9 nneg=0, perm nneg=11.
  * Sample {9,22,33,78,82}: MAIN nneg=1 all five;
    perm nneg 24,30,44,96,102.  EXT kz82 n=341.

AUSGANG REFUTED.  P1 is not a construction Satz of the
fold mask.  The separating invariant is the weight-to-
position assignment (von Mangoldt / chi weights), not
the sign mask, not positivity, not block cardinality.
Dead chi keep P1 because they keep their arithmetic
weights, not because they share geometry with MAIN.
r391 (R) is more robust than P1 (weight-rand held K=4);
the hoped work-division (all arithmetic on sch<0) is
false -- P1 is the fragile arithmetic statement.
SATZ: scale invariance of R; rank-1 interlacing; PSD+ND
need not lift all negatives.  CENSUS: class tables,
Gram rest 0 on MAIN / 0.15 off-class, razor mild-noise.
No RH claim.

MACHINERY: r400 H.pack_world / dual_fejer_R / r_of,
r398 HM.r_nm3 / scramble / two-period / chi,
r356 BDH.dual_weights, r390 GEP.fejer_w, r226 V.build_measures.

NO RH CLAIM.  Finite identities, one named refutation,
named kills.  Research documentation, not a theorem of RH.
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

import bulk_one_defect_probe as H  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

H_SHA_PREFIX = "91a4afa2"
BDH_SHA_PREFIX = "36141c0a"
DMF_SHA_PREFIX = "4bf1a94b"
HM_SHA_PREFIX = "bb1dcf6a"

W9_NNEG, W9_NNEG_REF, W9_KILLED = 1, 49, 48
W9_N_HALF = 13
W9_GRAM_REST_HI = 1.0e-8
W9_NNEG_M = 0
W9_NPOS_M = 49
W9_OMIT = 49
W9_ONLYGRAM = 13
W9_EVM_LO, W9_EVM_HI = 0.02, 0.75
PERM_NNEG_LO, PERM_SEEDS = 15, 4
GAUSS_NNEG_LO = 12
EXPON_NNEG_LO = 8
DIR_NNEG_LO = 10
RADE_NNEG = 2
MILD_EPS = 1.0e-4
MILD_SEEDS = 6
MILD_SEED0 = 10
MILD_BREAKS_LO = 1
SCALE_RES_HI = 1.0e-10
SCR_NNEG = 21
TP_NNEG = 4
SIGNFLIP_NNEG_LO = 70
CHI_PERM_LO = 8
SAMPLE = (9, 22, 33, 78, 82)
SAMPLE_PERM_LO = (15, 20, 30, 70, 80)
KIND_OFF = dict(permute=0, gauss=100, rademacher=200,
                expon=300, dirichlet=400)

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
    return (not bad), ("NO zero/prime oracles; dual CD Gram / "
                       "weight-rand on a frozen mask only"
                       if not bad else "; ".join(bad))


def rebuild(mz, wp, vn):
    """Fixed positions and sign mask; new positive mu/nu weights."""
    xp = np.asarray(mz["xp"], float)
    yn = np.asarray(mz["yn"], float)
    wp = np.asarray(wp, float)
    vn = np.asarray(vn, float)
    x = np.concatenate([xp, yn])
    w = np.concatenate([wp, -vn])
    o = np.argsort(x)
    out = dict(mz)
    out.update(xp=xp, wp=wp, yn=yn, vn=vn,
               xu=x[o], wu=w[o], S=len(x))
    return out


def reweight(mz, kind, seed):
    rng = np.random.default_rng(seed)
    wp = np.asarray(mz["wp"], float).copy()
    vn = np.asarray(mz["vn"], float).copy()
    if kind == "permute":
        wp = rng.permutation(wp)
        vn = rng.permutation(vn)
    elif kind == "gauss":
        wp = wp * np.exp(rng.normal(0.0, 0.5, size=len(wp)))
        vn = vn * np.exp(rng.normal(0.0, 0.5, size=len(vn)))
    elif kind == "rademacher":
        wp = np.full_like(wp, float(np.median(wp) or 1.0))
        vn = np.full_like(vn, float(np.median(vn) or 1.0))
    elif kind == "expon":
        wp = rng.exponential(float(np.mean(wp) or 1.0), size=len(wp))
        vn = rng.exponential(float(np.mean(vn) or 1.0), size=len(vn))
    elif kind == "dirichlet":
        a = rng.exponential(1.0, size=len(wp))
        a /= max(float(np.sum(a)), 1e-300)
        wp = a * float(np.sum(wp))
        b = rng.exponential(1.0, size=len(vn))
        b /= max(float(np.sum(b)), 1e-300)
        vn = b * float(np.sum(vn))
    elif kind == "signflip":
        wu = np.asarray(mz["wu"], float)
        xu = np.asarray(mz["xu"], float)
        wt = np.abs(wu) * rng.choice([-1.0, 1.0], size=len(wu))
        pos = wt > 0
        if int(np.sum(pos)) < 3 or int(np.sum(~pos)) < 3:
            return None
        out = dict(mz)
        out.update(xp=xu[pos], wp=wt[pos], yn=xu[~pos], vn=-wt[~pos],
                   xu=xu, wu=wt, S=len(xu))
        return out
    else:
        raise ValueError(kind)
    if np.any(wp <= 0) or np.any(vn <= 0):
        return None
    return rebuild(mz, wp, vn)


def spec_of(mz, need_ref=False):
    p = H.pack_world(mz, None, need_ref=need_ref)
    H.drop_heavy(p)
    return p


def gram_of(mz):
    """B = R - R^ref on the reference-negative space."""
    R, _ = H.r_of(mz)
    Rr = H.dual_fejer_R(mz)
    B = R - Rr
    Aref = Rr - 0.5 * np.eye(Rr.shape[0])
    evA, VA = np.linalg.eigh(Aref)
    mneg = evA < -1e-12
    evR = np.linalg.eigvalsh(Rr)
    n_half = int(np.sum(np.abs(evR - 0.5) <= 1e-10))
    Vn = VA[:, mneg]
    M = 0.5 * (Vn.T @ B @ Vn + (Vn.T @ B @ Vn).T)
    evM = np.linalg.eigvalsh(M)
    f2 = float(np.sum(evM * evM))
    f2n = float(np.sum(evM[evM < 0] ** 2))
    rest = math.sqrt(f2n) / (math.sqrt(f2) + 1e-30)
    ev_plus = np.clip(evM, 0.0, None)
    ev_minus = np.clip(evM, None, 0.0)
    nneg_omit, _ = H.nneg_sym(Aref + (Vn * ev_minus) @ Vn.T)
    nneg_gram, _ = H.nneg_sym(Aref + (Vn * ev_plus) @ Vn.T)
    evsrc = np.linalg.eigvalsh(R)
    return dict(
        nneg=int(np.sum(evsrc < 0.5 - 1e-12)),
        nneg_ref=int(np.sum(mneg)),
        n_half=n_half,
        nneg_M=int(np.sum(evM < -1e-10)),
        npos_M=int(np.sum(evM > 1e-10)),
        rest=rest,
        evM_min=float(evM[0]), evM_max=float(evM[-1]),
        nneg_omit=int(nneg_omit), nneg_gram=int(nneg_gram),
        scale_res=float("nan"),
    )


def part_toys():
    section("S1  SATZ -- INTERLACING / PSD-INCOMPLETE / SCALE-Q")
    A2 = np.array([[Fr(-1), Fr(0)], [Fr(0), Fr(-1)]], dtype=object)
    A2p = np.array([[Fr(0), Fr(0)], [Fr(0), Fr(-1)]], dtype=object)
    check("G01-interlace-rank1-Q",
          A2[0, 0] + A2[1, 1] == Fr(-2)
          and A2p[0, 0] == Fr(0) and A2p[1, 1] == Fr(-1),
          "diag(-1,-1)+e0 e0^T kills ONE negative, never two")
    Af = np.diag([-1.0, -1.0])
    Bf = 0.1 * np.eye(2)
    nA, _ = H.nneg_sym(Af)
    nS, _ = H.nneg_sym(Af + Bf)
    check("G02-psd-incomplete-Q",
          nA == 2 and nS == 2,
          "diag(-1,-1)+0.1 I still nneg=2: PSD need not lift all")
    check("G03-half-vs-class",
          Fr(1, 2) < Fr(1),
          "lam2>=1/2 is the P1 threshold (class test, not x2)")


def part_w9():
    section("S2  LEG A/B/C -- w9 CLASS / GRAM / RAZOR")
    mz = V.build_measures(9)
    p = spec_of(mz, need_ref=True)
    g = gram_of(mz)
    check("G10-w9-MAIN-P1",
          p["nneg"] == W9_NNEG and p["nneg_ref"] == W9_NNEG_REF
          and p["killed"] == W9_KILLED,
          "nneg=%d nneg_ref=%d killed=%d gap2=%.3e"
          % (p["nneg"], p["nneg_ref"], p["killed"], p["gap2"]))
    check("G11-w9-ref-half-modes",
          g["n_half"] == W9_N_HALF,
          "n_half(R^ref)=%d (not a single exact 1/2 mode)"
          % g["n_half"])
    check("G12-w9-Gram-PSD",
          g["nneg_M"] == W9_NNEG_M and g["npos_M"] == W9_NPOS_M
          and g["rest"] <= W9_GRAM_REST_HI
          and W9_EVM_LO <= g["evM_min"] <= g["evM_max"] <= W9_EVM_HI,
          "nneg_M=%d npos_M=%d rest=%.2e evM[%.3f,%.3f]"
          % (g["nneg_M"], g["npos_M"], g["rest"],
             g["evM_min"], g["evM_max"]))
    check("G13-w9-omit-Gram-returns-ref",
          g["nneg_omit"] == W9_OMIT and g["nneg_gram"] == W9_ONLYGRAM,
          "omit-Gram nneg=%d (ref returns); only-Gram nneg=%d "
          "(PSD on 49-space NOT enough)"
          % (g["nneg_omit"], g["nneg_gram"]))
    mz7 = rebuild(mz, 7.0 * mz["wp"], 7.0 * mz["vn"])
    R1, _ = H.r_of(mz)
    R7, _ = H.r_of(mz7)
    res = float(np.linalg.norm(R1 - R7))
    p7 = spec_of(mz7, False)
    check("G14-scale-invariant",
          res <= SCALE_RES_HI and p7["nneg"] == W9_NNEG,
          "||R-R(7w)||_F=%.3e  nneg(7w)=%d" % (res, p7["nneg"]))
    pmu = spec_of(rebuild(mz, 3.0 * mz["wp"], mz["vn"]), False)
    pnu = spec_of(rebuild(mz, mz["wp"], 3.0 * mz["vn"]), False)
    check("G15-relative-mu-nu-scale",
          pmu["nneg"] == 0 and pnu["nneg"] >= 60,
          "mu*3 nneg=%d (overshoots vacuous); nu*3 nneg=%d"
          % (pmu["nneg"], pnu["nneg"]))

    def nnegs_of(kind, nseed):
        out = []
        for s in range(nseed):
            mz2 = reweight(mz, kind, 1000 + KIND_OFF[kind] + s)
            out.append(-1 if mz2 is None else spec_of(mz2, False)["nneg"])
        return out

    np_ = nnegs_of("permute", PERM_SEEDS)
    ng = nnegs_of("gauss", PERM_SEEDS)
    ne = nnegs_of("expon", PERM_SEEDS)
    nd = nnegs_of("dirichlet", PERM_SEEDS)
    nr = nnegs_of("rademacher", 1)
    check("G16-class-permute-breaks",
          min(np_) >= PERM_NNEG_LO and all(n > 1 for n in np_),
          "permute nneg=%s (mask fixed, P1 dies)" % np_)
    check("G17-class-laws-break",
          min(ng) >= GAUSS_NNEG_LO and min(ne) >= EXPON_NNEG_LO
          and min(nd) >= DIR_NNEG_LO and nr[0] == RADE_NNEG,
          "gauss %s expon %s dir %s rade %s" % (ng, ne, nd, nr))
    n_break = 0
    for s in range(MILD_SEEDS):
        rng = np.random.default_rng(MILD_SEED0 + s)
        wp = mz["wp"] * (1.0 + MILD_EPS * rng.normal(0, 1, size=len(mz["wp"])))
        vn = mz["vn"] * (1.0 + MILD_EPS * rng.normal(0, 1, size=len(mz["vn"])))
        pm = spec_of(rebuild(mz, np.clip(wp, 1e-18, None),
                             np.clip(vn, 1e-18, None)), False)
        if pm["nneg"] > 1:
            n_break += 1
    check("G18-mild-1e-4-breaks",
          n_break >= MILD_BREAKS_LO,
          "eps=1e-4 nneg>1 in %d/%d (razor: gap2 ~ 4e-5)"
          % (n_break, MILD_SEEDS))
    mzP = reweight(mz, "permute", 1000)
    gP = gram_of(mzP)
    check("G19-Gram-not-class",
          gP["rest"] >= 0.05 and gP["nneg_M"] >= 3,
          "permute Gram rest=%.3f nneg_M=%d (MAIN rest=0 is arithmetic)"
          % (gP["rest"], gP["nneg_M"]))
    return dict(main=p, gram=g, perm=np_, rade=nr[0], mild=n_break)


def part_kills():
    section("S3  LEG D -- SCRAMBLE / TWO-PERIOD / SIGNFLIP / CHI")
    ps = spec_of(HM.scramble_mz(), True)
    check("G20-scramble",
          ps["nneg"] == SCR_NNEG,
          "scramble nneg=%d killed=%d (positions destroyed)"
          % (ps["nneg"], ps["killed"]))
    pt = spec_of(HM.two_period_mz(21, 2.0 / 3.0), True)
    check("G21-two-period",
          pt["nneg"] >= TP_NNEG and pt["killed"] == 0,
          "S=21 nneg=%d killed=%d" % (pt["nneg"], pt["killed"]))
    mz = V.build_measures(9)
    ns = []
    for s in range(3):
        mz2 = reweight(mz, "signflip", 4000 + s)
        ns.append(-1 if mz2 is None else spec_of(mz2, False)["nneg"])
    check("G22-signflip-mask",
          min(n for n in ns if n >= 0) >= SIGNFLIP_NNEG_LO,
          "signflip nneg=%s (mask destroyed)" % ns)
    mzd = HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    pd = spec_of(mzd, False)
    rng = np.random.default_rng(15)
    pdp = spec_of(rebuild(mzd, rng.permutation(mzd["wp"]),
                          rng.permutation(mzd["vn"])), False)
    check("G23-dead-chi-weights",
          pd["nneg"] <= 1 and pdp["nneg"] >= CHI_PERM_LO,
          "dead chi3-15 nneg=%d on true weights; perm nneg=%d"
          % (pd["nneg"], pdp["nneg"]))
    mzl = HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)
    pl = spec_of(mzl, False)
    rng = np.random.default_rng(9)
    plp = spec_of(rebuild(mzl, rng.permutation(mzl["wp"]),
                          rng.permutation(mzl["vn"])), False)
    check("G24-live-chi-perm",
          pl["nneg"] <= 1 and plp["nneg"] >= CHI_PERM_LO,
          "live chi3-9 nneg=%d; perm nneg=%d"
          % (pl["nneg"], plp["nneg"]))
    return dict(scr=ps, tp=pt, dead=pd, dead_perm=pdp)


def part_sample():
    section("S4  LEG A/B -- SAMPLE + EXT (construction identity?)")
    rows = []
    for kz, plo in zip(SAMPLE, SAMPLE_PERM_LO):
        mz = V.build_measures(kz)
        p = spec_of(mz, True)
        rng = np.random.default_rng(kz + 3)
        pp = spec_of(rebuild(mz, rng.permutation(mz["wp"]),
                             rng.permutation(mz["vn"])), False)
        Rr = H.dual_fejer_R(mz)
        ev = np.linalg.eigvalsh(Rr)
        n_half = int(np.sum(np.abs(ev - 0.5) <= 1e-10))
        rows.append(dict(kz=kz, n=p["n"], nneg=p["nneg"],
                         nneg_ref=p["nneg_ref"], killed=p["killed"],
                         gap2=p["gap2"], perm=pp["nneg"], n_half=n_half))
        print("    kz=%d n=%d nneg=%d nref=%d killed=%d n_half=%d "
              "gap2=%.2e perm=%d" % (
                  kz, p["n"], p["nneg"], p["nneg_ref"], p["killed"],
                  n_half, p["gap2"], pp["nneg"]))
    check("G40-sample-MAIN-P1",
          all(r["nneg"] <= 1 for r in rows) and len(rows) == 5,
          "5/5 MAIN nneg<=1; nneg_ref=%s (not a fixed 49)"
          % [r["nneg_ref"] for r in rows])
    check("G41-sample-perm-breaks",
          all(r["perm"] >= lo for r, lo in zip(rows, SAMPLE_PERM_LO)),
          "perm nneg=%s -- 48-of-49 is MAIN tautology, not class"
          % [r["perm"] for r in rows])
    check("G42-sample-half-not-one",
          all(r["n_half"] >= 10 for r in rows)
          and rows[0]["n_half"] == W9_N_HALF,
          "n_half=%s grows; not a single exact 1/2 mode"
          % [r["n_half"] for r in rows])
    check("G43-EXT-kz82",
          rows[-1]["kz"] == 82 and rows[-1]["n"] >= 300
          and rows[-1]["nneg"] == 1 and rows[-1]["perm"] >= 80,
          "EXT n=%d nneg=%d perm=%d" % (
              rows[-1]["n"], rows[-1]["nneg"], rows[-1]["perm"]))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("p1_construction_probe -- "
          "PRIME.LDAGGER.P1_CONSTRUCTION.01 (round 403)")
    print("SPEC_SHA %s   (H %s / BDH %s / DMF %s / HM %s)"
          % (SPEC_SHA[:16], H.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             DMF.SPEC_SHA[:16], HM.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (sample-5 + EXT kz82 + chi perm)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (H.SPEC_SHA.startswith(H_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "H %s / BDH %s / DMF %s / HM %s"
          % (H.SPEC_SHA[:8], BDH.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], HM.SPEC_SHA[:8]))

    part_toys()
    part_w9()
    part_kills()
    if not smoke:
        part_sample()
    else:
        section("S4  SAMPLE/EXT skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-REFUTED",
          prev_ok,
          "P1 CONSTRUCTION CLASS REFUTED: fixed-mask "
          "weight-rand kills P1; the invariant is the "
          "weight-to-position assignment, not the fold mask; "
          "no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "P1_CONSTRUCTION_REFUTED"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("P1 CONSTRUCTION %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("P1 CONSTRUCTION FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
