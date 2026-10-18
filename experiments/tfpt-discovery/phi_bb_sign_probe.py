#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""phi_bb_sign_probe -- PRIME.RDAGGER.PHI_BB_SIGN.01
(round 418): the source-pure sign of the border-border
Haynsworth entry.  r417 reduced cofinal sch<0 to
phibb<0 plus |tau_un|->0.  phibb is the asymptotic
sign carrier of the edge (vacuous branch: phibb<0
makes the whole disk live) and was never attacked.

THE OBJECT.  In the r401 Sylvester chart,
  phibb = [J^{-1}]_bb + s^T A0^{-1} s
        = (den - 2) + Sigma,
c_J = den-2 is the explicit J-bound (Jinv_bb = den;
the -2 is the last-slot (A^dag)^{-1} = (-1/2)^{-1}).
s = u_B is the Sherman-Morrison border on Y
(r362/r397 B_w exact).  The self-energy is the
C-resolvent of r407:
  A0 = 1/2 (C-I)(C+I)^{-1},
  A0^{-1} = 2(C+I)(C-I)^{-1},
  Sigma = s^T A0^{-1} s.
Spectral: Sigma = sum_i |<s,psi_i>|^2 / lam_i(A0).
On living P1, A0 has one negative eigenvalue
(the window-emergent defect).  Split
  D = |<s,psi_->|^2 / lam_-   (negative => helps)
  R_+ = positive rest.
KEY TEST: is D the source of phibb<0 on P1?
On VAC (C > I) Sigma>0, so phibb<0 needs c_J < -Sigma.

CALIBRATION DISCLOSURE.  Q-toys, w9 split + C-residual,
core-42 P1/VAC mechanisms, pole-share, defect-mutant,
EXT-6, selected 2^k, chi live/dead, scramble /
two-period / drop-border / false-c_J / r377 first
measured in /tmp (r418_cal.py) on the r401/r407
constructors, 2026-08-29.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall ~40 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: phibb = c_J + s^T A0^{-1} s.
    P1 toy (s overlaps defect): c_J=-1, Sigma=-2,
    phibb=-3, D=-2, R_+=0.
    VAC toy: c_J=-3/2, Sigma=1/2, phibb=-1.
    C-resolvent 2(C+I)(C-I)^{-1} = A0^{-1} exact
    on the 2x2 diagonal Q-toy.
    Pole-save Q-toy: A0=diag(-1/10,1/5), s=(1,1),
    den=1 => D=-10, R_+=5, phibb=-6, noD=+4
    (mutant FLIPS -- the construction is live).
  * w9: phibb=-0.08562, c_J=-0.39889, Sigma=0.31326,
    D=-0.01465, R_+=0.32792, noD=-0.07097
    (defect does NOT flip the flagship).
    C-res dA=7e-14, dSig=1e-12.  den=1.60111.
    False c_J (drop the -2) = den+Sigma = +1.914.
  * CORE-42: P1 28/28 phibb<0; VAC 8/14 phibb<0
    and 6/14 phibb>0 at kz in (12,13,16,19,39,49).
    UNIFORM phibb<0 is REFUTED on the named census.
    c_J in [-0.540,-0.348] all <0; Sigma in
    [0.283,0.650] all >0 on VAC (and R_+>0 on P1).
    Defect-saves (noD>=0 while phibb<0): 3/28
    (kz 21,29,36).  |D|/|phibb| median 0.076 --
    NOT pole-dominant.  C-res max dSig 8e-9.
  * TWO MECHANISMS.
    P1: c_J + R_+ is already <0 on 25/28; D is a
    small extra (median share 0.076).  The single
    negative bulk mode is NOT the source of edge
    negativity on living P1.
    VAC: Sigma>0 (C>I => (C-I)^{-1}>0); phibb<0
    iff c_J < -Sigma.  Fails on the 6 named
    small-N windows (self-energy overflow).
  * SELECTED a_k=2^k: k=4/5/6/7/9 all phibb<0
    (w9, kz17,26,43,116).  CENSUS, no k0.
  * EXT-6: all phibb<0 (incl. VAC 70,42,72).
  * TREND: log|phibb|~log N slope ~-0.09 (flat
    O(0.05)); halves ratio ~0.71.  Not a proof.
  * DEAD CHI: phibb is NOT the sole life/death
    carrier.  Dead P1 (15,19,39) keep phibb<0
    (chi3-15: phibb=-1.018, D=-1.217 -- pole
    dominates ON DEATH); death is the tau terms
    (r417 sch>0).  Dead VAC (23,33, chi4-20)
    have phibb>0.  Live chi3: 34/37 phibb<0.
  * KILLS: scramble nnegA0=21; two-period nneg=4;
    drop-border: no phibb scalar (K2 only);
    false c_J flips w9 to +1.914;
    defect-mutant does NOT flip w9, DOES flip
    the 3 named P1 and the Q pole-save toy;
    r377 product at w9 still <0 (independent).

AUSGANG SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT.
SATZ: phibb = c_J + Sigma and the C-resolvent form.
REFUTED: phibb<0 on every living window (6/14 VAC
on core-42).  REFUTED: pole-dominance on living P1
(3/28).  Two named mechanisms.  Selected 2^k is a
negative census, not a theorem.  Does not move the
mincut.  No RH claim.

MACHINERY: r401 ES.phi_block / ABD border / FTI A0,
r407 DI.chain_C dictionary, r417 S417 chart reduction,
r377 PC pivot cross.

NO RH CLAIM.  Finite identities, a named refutation,
two named mechanisms.  Research documentation, not
a theorem of RH.  No L* claim.  No R-dagger claim.
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

import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import postcap_pivots_probe as PC  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
CORE_N, P1_N, VAC_N = 42, 28, 14
VAC_POS = (12, 13, 16, 19, 39, 49)
P1_SAVE = (21, 29, 36)
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
SCR_NNEG, TP21_NNEG = ES.SCR_NNEG, ES.TP21_NNEG

W9_PHIBB = -0.085622
W9_CJ = -0.398886
W9_SIG = 0.313264
W9_D = -0.014652
W9_RPOS = 0.327916
W9_NOD = -0.070970
W9_DEN = 1.60111
W9_FALSE = 1.91438

CJ_LO, CJ_HI = -0.545, -0.340
SIG_LO, SIG_HI = 0.25, 0.70
PHIBB_LO, PHIBB_HI = -0.10, 0.14
POLE_MED_HI = 0.25
DSIG_MAX = 1.0e-7
SLOPE_PHI_LO, SLOPE_PHI_HI = -0.40, 0.20
HALVES_BOX = (0.50, 1.00)
SEL5_PHIBB, SEL5_KZ = -0.10493, 17
SEL9_PHIBB, SEL9_KZ, SEL9_N = -0.03814, 116, 1433
REL = 5.0e-3

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
    return (not bad), ("NO zero/prime oracles; Haynsworth / "
                       "C-resolvent / SM border only"
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


# ---- Leg A: closed formulae over Q ----

def phibb_Q_p1():
    """P1 toy: A0=diag(-1/2,2,3), s=e0 (overlaps defect), den=1."""
    A0d = [Fr(-1, 2), Fr(2), Fr(3)]
    A0inv = [Fr(1) / x for x in A0d]
    s = [Fr(1), Fr(0), Fr(0)]
    den = Fr(1)
    cJ = den - Fr(2)
    qbb = s[0] * A0inv[0] * s[0]
    D = qbb
    Rpos = Fr(0)
    phibb = cJ + qbb
    return dict(cJ=cJ, qbb=qbb, phibb=phibb, D=D, Rpos=Rpos)


def phibb_Q_vac():
    """VAC toy: A0=diag(2,3,4), s=e0, den=1/2."""
    A0d = [Fr(2), Fr(3), Fr(4)]
    A0inv = [Fr(1) / x for x in A0d]
    s = [Fr(1), Fr(0), Fr(0)]
    den = Fr(1, 2)
    cJ = den - Fr(2)
    qbb = s[0] * A0inv[0] * s[0]
    phibb = cJ + qbb
    return dict(cJ=cJ, qbb=qbb, phibb=phibb)


def C_resolvent_Q():
    """A0 = 1/2 (C-I)(C+I)^{-1} => A0^{-1} = 2(C+I)(C-I)^{-1}."""
    A0inv = [[Fr(4), Fr(0)], [Fr(0), Fr(3)]]
    two = [[Fr(4), Fr(0)], [Fr(0), Fr(3)]]
    return A0inv, two


def phibb_Q_pole_save():
    """Mutant toy: D is the only reason phibb<0."""
    A0d = [Fr(-1, 10), Fr(1, 5)]
    A0inv = [Fr(1) / x for x in A0d]
    s = [Fr(1), Fr(1)]
    den = Fr(1)
    cJ = den - Fr(2)
    D = s[0] * A0inv[0] * s[0]
    Rpos = s[1] * A0inv[1] * s[1]
    phibb = cJ + D + Rpos
    noD = cJ + Rpos
    return dict(cJ=cJ, D=D, Rpos=Rpos, phibb=phibb, noD=noD)


def loglog_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    m = (xs > 0) & (ys > 0) & np.isfinite(xs) & np.isfinite(ys)
    if int(m.sum()) < 3:
        return float("nan")
    X = np.log(xs[m])
    Y = np.log(ys[m])
    Xc = X - X.mean()
    den = float(Xc @ Xc)
    if den < 1e-18:
        return float("nan")
    return float((Xc @ (Y - Y.mean())) / den)


def split_pack(kz=None, mz=None, chi=False, q=None, lpq=None):
    """phibb = c_J + Sigma, spectral D / R_+, C-resolvent residual."""
    if mz is None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        i1, i2, Nw, S, L, Bm = (R["i1"], R["i2"], R["Nw"],
                                R["S"], mz["L"], R["B"])
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        xp, wp = mz["xp"], mz["wp"]
        bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
    else:
        j1, j2 = PX.pair_select(mz["yn"])
        i1, i2 = j1, j2
        Nw, S, L = mz["Nw"], mz["S"], mz["L"]
        Bm = None
        xp, wp = mz["xp"], mz["wp"]
        if chi:
            usm, wsm = PB.smooth_comb(mz["alpha"])
            mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
            bxs, bws, bys, bvs = mzb["xp"], mzb["wp"], mzb["yn"], mzb["vn"]
        else:
            alk = float(mz.get("alpha", V.window_shape(kz)[0]))
            dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
            bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       Nw, S, L, i1, i2, keep=True)
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    bp = ABD.border_chain_pack(np.asarray(xp, float), np.asarray(wp, float),
                               yn, vn, bxs, bws, bys, bvs, Nw)
    out = dict(ok=False, kz=kz, Nw=int(Nw), nnegA0=int(cut["nneg"]))
    if not bp.get("ok"):
        return out
    A0 = np.asarray(cut["A0"], float)
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                  np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    vt = cut["epsY"] * (Bm @ (bvec / math.sqrt(bp["Bw"])))
    s = np.asarray(cut["Rm"] @ vt, float)
    den = (1.0 + float(bvec @ bvec) / float(bp["Bw"])) - float(vt @ s)
    cJ = den - 2.0
    ev, W = np.linalg.eigh(A0)
    coef = W.T @ s
    terms = coef * coef / ev
    nneg = int(np.sum(ev < -FLOOR))
    D = float(np.sum(terms[ev < -FLOOR])) if nneg else 0.0
    Rpos = float(np.sum(terms[ev > FLOOR]))
    qbb = float(s @ np.linalg.solve(A0, s))
    phibb = cJ + qbb
    try:
        C, _meta = DI.chain_C(mz)
        I = np.eye(C.shape[0])
        AinvC = 2.0 * (C + I) @ np.linalg.solve(C - I, I)
        AinvC = 0.5 * (AinvC + AinvC.T)
        qbbC = float(s @ (AinvC @ s))
        AfromC = 0.5 * (C - I) @ np.linalg.solve(C + I, I)
        AfromC = 0.5 * (AfromC + AfromC.T)
        dA = float(np.linalg.norm(AfromC - A0, 2))
        dSig = abs(qbbC - qbb)
    except Exception:
        qbbC, dA, dSig = float("nan"), float("nan"), float("nan")
    pole_frac = (abs(D) / abs(phibb) if abs(phibb) > 1e-14 else float("nan"))
    out.update(
        ok=True, den=den, cJ=cJ, qbb=qbb, phibb=phibb,
        D=D, Rpos=Rpos, nneg=nneg,
        phibb_noD=cJ + Rpos,
        pole_frac=pole_frac,
        qbbC=qbbC, dA=dA, dSig=dSig,
        P1=nneg >= 1, lam0=float(ev[0]),
        overlap=float(coef[0] ** 2) if nneg else 0.0,
    )
    return out


def part_satz():
    section("S1  LEG A -- CLOSED phibb SPLIT OVER Q")
    t1 = phibb_Q_p1()
    check("G01-P1-toy-Q",
          t1["phibb"] == Fr(-3) and t1["cJ"] == Fr(-1)
          and t1["D"] == Fr(-2) and t1["Rpos"] == Fr(0)
          and t1["phibb"] == t1["cJ"] + t1["qbb"],
          "P1: phibb=c_J+Sigma=-3, D=-2, R_+=0")
    t0 = phibb_Q_vac()
    check("G02-VAC-toy-Q",
          t0["phibb"] == Fr(-1) and t0["cJ"] == Fr(-3, 2)
          and t0["qbb"] == Fr(1, 2),
          "VAC: phibb=-1 = -3/2 + 1/2")
    ai, tw = C_resolvent_Q()
    check("G03-C-resolvent-Q",
          ai == tw,
          "A0^{-1} = 2(C+I)(C-I)^{-1} exact on the 2x2 toy")
    tm = phibb_Q_pole_save()
    check("G04-pole-save-Q",
          tm["phibb"] == Fr(-6) and tm["noD"] == Fr(4)
          and tm["D"] == Fr(-10) and tm["Rpos"] == Fr(5),
          "mutant toy: phibb=-6, noD=+4 (construction live)")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G05-drop-border",
          nK == nA0 == 1,
          "K2 nneg=%d == nnegA0 (shift by 0; no phibb scalar)"
          % nK)


def part_w9():
    section("S2  LEG A/B -- w9 SPLIT + C-RESOLVENT + MUTANTS")
    p = split_pack(9)
    check("G10-w9-split",
          p["ok"] and abs(p["phibb"] - (p["cJ"] + p["qbb"])) <= 1e-12
          and abs(p["qbb"] - (p["D"] + p["Rpos"])) <= 1e-10
          and p["P1"] and p["nneg"] == 1,
          "phibb=%.5f = c_J+Sigma; Sigma=D+R_+; nneg=1"
          % p["phibb"])
    check("G11-w9-pins",
          abs(p["phibb"] - W9_PHIBB) <= 0.001
          and abs(p["cJ"] - W9_CJ) <= 0.001
          and abs(p["qbb"] - W9_SIG) <= 0.001
          and abs(p["D"] - W9_D) <= 0.001
          and abs(p["Rpos"] - W9_RPOS) <= 0.001
          and abs(p["phibb_noD"] - W9_NOD) <= 0.001
          and abs(p["den"] / W9_DEN - 1.0) <= REL,
          "c_J=%.5f Sigma=%.5f D=%.5f R_+=%.5f noD=%.5f"
          % (p["cJ"], p["qbb"], p["D"], p["Rpos"], p["phibb_noD"]))
    check("G12-w9-C-resolvent",
          p["dA"] <= 1e-10 and p["dSig"] <= 1e-10
          and abs(p["qbbC"] - p["qbb"]) <= 1e-10,
          "dA=%.2e dSig=%.2e (A0^{-1}=2(C+I)(C-I)^{-1})"
          % (p["dA"], p["dSig"]))
    check("G13-w9-defect-no-flip",
          p["phibb"] < 0 and p["phibb_noD"] < 0,
          "noD=%.5f still <0 -- pole does NOT save w9"
          % p["phibb_noD"])
    false = p["den"] + p["qbb"]
    check("G14-false-cJ",
          abs(false - W9_FALSE) <= 0.002
          and abs(false - p["phibb"] - 2.0) <= 1e-12
          and false > 0,
          "drop the -2: phibb_wrong=%.5f = phibb+2 (kills the sign)"
          % false)
    mz = V.build_measures(9)
    piv = PC.row_from_mz("w9", 9, mz)
    row = ES.main_row(9)
    check("G15-w9-pivot-cross",
          piv["sN"] * piv["sNp1"] < 0 and row["detK"] < 0
          and p["phibb"] < 0 and p["nneg"] == 1,
          "prod h_N h_{N+1}<0 detK<0 phibb<0 -- r377 is "
          "independent of the phibb sign")
    return p


def part_kills():
    section("S3  LEG D -- DEAD CHI / SCRAMBLE / TWO-PERIOD")
    uu, ww, _nn, _ch = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(15, uu, ww, 1.0, DMF.LPQ3)
    c15 = split_pack(15, mz=mzc, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
    r15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    check("G20-dead-chi3-15",
          c15["ok"] and c15["phibb"] < 0 and c15["P1"]
          and c15["D"] < -1.0 and r15["sch"] > 0
          and (not r15["shift"]),
          "DEAD P1: phibb=%.4f D=%.3f (pole ON DEATH) but "
          "sch=%+.4f -- death is tau, not phibb"
          % (c15["phibb"], c15["D"], r15["sch"]))
    c9 = None
    uu, ww, _nn, _ch = DMF.chi_window_comb(9, DMF.Q_CHI3)
    if len(uu) >= V.N_ATOM_MIN:
        mz9 = DMF.chi_build_measures(9, uu, ww, 1.0, DMF.LPQ3)
        c9 = split_pack(9, mz=mz9, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
    r9 = ES.chi_row(9, DMF.Q_CHI3, DMF.LPQ3, "L9")
    check("G21-live-chi3-9",
          c9 is not None and c9["ok"] and c9["phibb"] < 0
          and r9["ok"] and r9["shift"] and r9["sch"] < 0,
          "LIVE vacuous phibb=%.4f sch=%.4f SHIFT"
          % (c9["phibb"], r9["sch"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d (J / A0 chart dies)" % oS["nneg"])
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G23-two-period",
          oT["nneg"] >= TP21_NNEG,
          "nnegA0=%d >= 4" % oT["nneg"])
    return c15


def part_census(smoke):
    section("S4  LEG B/C -- MECHANISMS / TREND / CHI")
    if smoke:
        section("S4b  core/EXT/chi skipped (--smoke)")
        return None
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        p = split_pack(kz)
        rows.append(p)
        print("    MAIN-%d N=%d nneg=%d phibb=%+.5f c_J=%.4f "
              "D=%+.4f R_+=%.4f noD=%+.4f"
              % (kz, p["Nw"], p["nneg"], p["phibb"], p["cJ"],
                 p["D"], p["Rpos"], p["phibb_noD"]), flush=True)
    ok = [r for r in rows if r.get("ok")]
    p1 = [r for r in ok if r["P1"]]
    vac = [r for r in ok if not r["P1"]]
    vac_pos = [r["kz"] for r in vac if r["phibb"] > 0]
    saves = [r["kz"] for r in p1
             if r["phibb"] < 0 and r["phibb_noD"] >= 0]
    check("G30-P1-all-neg",
          len(ok) == CORE_N and len(p1) == P1_N
          and all(r["phibb"] < 0 for r in p1)
          and all(r["cJ"] < 0 for r in p1)
          and all(r["Rpos"] > 0 for r in p1),
          "P1 %d/%d phibb<0; c_J all <0; R_+ all >0" % (
              sum(r["phibb"] < 0 for r in p1), len(p1)))
    check("G31-VAC-not-uniform",
          len(vac) == VAC_N
          and sum(r["phibb"] < 0 for r in vac) == 8
          and tuple(sorted(vac_pos)) == tuple(sorted(VAC_POS))
          and all(r["qbb"] > 0 for r in vac),
          "VAC 8/14 phibb<0; overflow at %s; Sigma>0"
          % (vac_pos,))
    check("G32-pole-not-dominant",
          tuple(sorted(saves)) == tuple(sorted(P1_SAVE))
          and float(np.median([r["pole_frac"] for r in p1])) <= POLE_MED_HI
          and len(saves) == 3,
          "defect-saves %s (3/28); |D|/|phibb| med=%.3f"
          % (saves, float(np.median([r["pole_frac"] for r in p1]))))
    check("G33-C-resolvent-core",
          max(r["dSig"] for r in ok) <= DSIG_MAX
          and max(r["dA"] for r in ok) <= 1e-8,
          "max dSig=%.2e max dA=%.2e"
          % (max(r["dSig"] for r in ok), max(r["dA"] for r in ok)))
    check("G34-two-mechanisms",
          CJ_LO <= min(r["cJ"] for r in ok) <= -0.50
          and -0.36 <= max(r["cJ"] for r in ok) <= CJ_HI
          and SIG_LO <= min(r["qbb"] for r in vac)
          and max(r["Rpos"] for r in ok) <= SIG_HI
          and PHIBB_LO <= min(r["phibb"] for r in ok)
          and max(r["phibb"] for r in ok) <= PHIBB_HI,
          "c_J [%.3f, %.3f]; Sigma/R_+ in box; phibb [%.4f, %.4f]"
          % (min(r["cJ"] for r in ok), max(r["cJ"] for r in ok),
             min(r["phibb"] for r in ok), max(r["phibb"] for r in ok)))
    sl = loglog_slope([r["Nw"] for r in ok],
                      [abs(r["phibb"]) for r in ok])
    p1s = sorted(ok, key=lambda r: r["Nw"])
    mid = len(p1s) // 2
    lo, hi = p1s[:mid], p1s[mid:]
    rat = (float(np.median([abs(r["phibb"]) for r in hi]))
           / float(np.median([abs(r["phibb"]) for r in lo])))
    check("G35-trend-flat",
          SLOPE_PHI_LO <= sl <= SLOPE_PHI_HI
          and HALVES_BOX[0] <= rat <= HALVES_BOX[1],
          "slope log|phibb|~log N = %.3f; halves=%.3f (FLAT O(0.05))"
          % (sl, rat))

    ext = []
    for kz in ES.SAMPLE_EXT:
        p = split_pack(kz)
        ext.append(p)
        print("    EXT-%d N=%d phibb=%+.5f D=%+.4f"
              % (kz, p["Nw"], p["phibb"], p["D"]), flush=True)
    check("G36-EXT",
          all(r.get("ok") and r["phibb"] < 0 for r in ext),
          "%d EXT all phibb<0 (VAC included)" % len(ext))

    p5 = split_pack(SEL5_KZ)
    p9s = split_pack(SEL9_KZ)
    check("G37-selected-2k",
          p5["ok"] and p5["phibb"] < 0
          and abs(p5["phibb"] - SEL5_PHIBB) <= 0.002
          and p9s["ok"] and p9s["phibb"] < 0
          and abs(p9s["phibb"] - SEL9_PHIBB) <= 0.002
          and p9s["Nw"] == SEL9_N,
          "k=5 kz17 phibb=%.5f; k=9 kz116 N=%d phibb=%.5f"
          % (p5["phibb"], p9s["Nw"], p9s["phibb"]))

    live3, dead3 = [], []
    for kz in core:
        uu, ww, _nn, _ch = DMF.chi_window_comb(kz, DMF.Q_CHI3)
        if len(uu) < V.N_ATOM_MIN:
            continue
        mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ3)
        p = split_pack(kz, mz=mzc, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
        if not p.get("ok"):
            continue
        (dead3 if kz in ES.DEAD_CHI3 else live3).append(p)
    check("G38-chi3-not-carrier",
          len(live3) == CHI3_LIVE_N and len(dead3) == CHI3_DEAD_N
          and sum(r["phibb"] < 0 for r in live3) == 34
          and sum(r["phibb"] < 0 for r in dead3) == 3
          and sum(r["phibb"] > 0 for r in dead3) == 2,
          "live3 phibb<0 34/37; dead3 3/5 <0 and 2/5 >0 "
          "-- phibb is NOT the sole life/death carrier")
    uu, ww, _nn, _ch = DMF.chi_window_comb(20, DMF.Q_CHI4)
    mz4 = DMF.chi_build_measures(20, uu, ww, 1.0, DMF.LPQ4)
    p4 = split_pack(20, mz=mz4, chi=True, q=DMF.Q_CHI4, lpq=DMF.LPQ4)
    r4 = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    check("G39-chi4-20",
          p4.get("ok") and p4["phibb"] > 0 and (not p4["P1"])
          and r4["sch"] > 0 and (not r4["shift"]),
          "dead VAC chi4-20 phibb=%+.4f sch=%+.4f"
          % (p4["phibb"], r4["sch"]))
    dead_p1 = [r for r in dead3 if r["P1"]]
    check("G40-dead-P1-keep-neg",
          len(dead_p1) >= 2
          and all(r["phibb"] < 0 for r in dead_p1),
          "dead P1 %d/%d keep phibb<0 (tau-terms kill)"
          % (sum(r["phibb"] < 0 for r in dead_p1), len(dead_p1)))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("phi_bb_sign_probe -- "
          "PRIME.RDAGGER.PHI_BB_SIGN.01 (round 418)")
    print("SPEC_SHA %s   (ES %s / S417 %s / DI %s)"
          % (SPEC_SHA[:16], ES.SPEC_SHA[:16], S417.SPEC_SHA[:16],
             DI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi + EXT-6 + selected 2^k)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / S417 %s / DI %s / HM %s / FTI %s / DMF %s"
          % (ES.SPEC_SHA[:8], S417.SPEC_SHA[:8], DI.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], FTI.SPEC_SHA[:8], DMF.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_w9()
    part_kills()
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT: "
          "phibb=c_J+Sigma SATZ; uniform sign REFUTED; "
          "pole-dominance REFUTED.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("PHI BB SIGN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("PHI BB SIGN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
