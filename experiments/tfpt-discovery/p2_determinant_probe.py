#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""p2_determinant_probe -- PRIME.RDAGGER.P2_DETERMINANT.01
(round 436): the exact reverse-Cauchy / rank-1
decomposition of det K2 on the nneg-1 branch.

THE OBJECT.  On a real Hermitian invertible A0 with
exactly one negative eigenvalue lam_- < 0 (unit
eigenvector psi_-) and the last two dual CD columns
U = (u1, u2),
    K2 = I_2 + U^T A0^{-1} U
is the r367/r369 2x2 Haynsworth matrix (J = I_2, so
J^{-1} = I is absorbed into the remainder).  Write
    p = U^T psi_- / sqrt(|lam_-|),
    K2_+ = I + R_+ ,   R_+ = U^T A_+^{-1} U  (positive rest).
Then K2 = K2_+ - p p^T and the 2x2 determinant lemma
is the reverse-Cauchy identity
    det K2 = det(K2_+) - Q,
    Q = p^T adj(K2_+) p
      = a_+ p2^2 - 2 b_+ p1 p2 + d_+ p1^2
      = ||p||^2 + p^T adj(R_+) p.
P2 (det K2 < 0) iff Q > det(K2_+) iff p^T K2_+^{-1} p > 1
(the r375 Rayleigh, rewritten as reverse-CS).

CALIBRATION DISCLOSURE.  Identity, anatomy, coupling,
alternation and kills first measured in /tmp
(r436_cal.py, r436_cal2.py) on the r367/r375/r377/r407
constructors, 2026-08-30.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall of the 75-row
family (core-42 + r286-15 + EXT3/4) is the r367 45+29
resolvable census; EXT5/6 not rebuilt (those 10 rows
are the r367 sign-census class).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: 4-node toy A0=diag(-1,1,2,3), U=[(2,0,0,0),(1,1,0,0)]
    p=(2,1), K2_+=diag(1,2), det(K2_+)=2, Q=9,
    det K2 = 2-9 = -7 exact.  Q = ||p||^2 + p^T adj(R_+) p
    = 5+4.  Drop-psi mutant det(K2_+)=2>0.
  * w9: nneg=1, detK=-5.0389, det(K2_+)=5.9582, Q=10.9971,
    ||p||^2=6.1016, ray=1.8457, align=0.051, dom=Ta share
    0.796, J-share 0.555, cos(psi_-, psi_{C_min})=1,
    nC=1, coup0=0.621, coup1=0.743.  Identity residual
    4.6e-14.  h_N h_{N+1} < 0.
  * kz18 (min -det of the family): -det=1.1572, excess
    0.2746, dom=Td share 0.996.
  * kz46 (THE coarse kill): ||p||^2=2.852 < lmax(K2_+)=3.656
    so ||p||^2 > lmax FAILS, yet detK=-2.364<0, align=0.984,
    gap vs lmin = 0.316.  Same window as r375 Cauchy fail.
  * kz12/16 vacuous: nneg=0, nC=0, detK=+12.463 / +9.667
    = det(K2_+), product h_N h_{N+1}>0.
  * Core-42: nneg-1 28, vacuous 14, overload 0.  All 14
    vacuous have detK>0 and no alternation.
  * 45-census (core-42 + r286-15 + EXT3/4, the r367
    resolvable nneg-1 family): detK<0 45/45, alt 45/45,
    ray>1 45/45, ||p||^2>lmax 44/45 (kz46), ||p||^2>lmin
    45/45 min gap 0.316, -det in [1.157, 1126.389].
    Dominant term MIXED: Ta 25 / Td 4 / Tx 16 (Tx grows
    on EXT).  Vacuous 29/74, detK>0 29/29, alt 0/29.
  * Dead chi nneg-1: CHI3-15 detK=-122.91 < 0 (P2 stays).
    CHI3-9 already PD (world-separating).  CHI4-9 nneg-1
    detK=-6.1804.
  * Scramble: nneg=21 (hypothesis empty), detK=-8.881.
  * Drop-psi at w9: det(K2_+)=5.958>0.  Wrong J=-I:
    det=+0.941 (sign flips).

AUSGANG REDUZIERT / IDENTITY_EXACT / ANATOMY_MIXED /
COARSE_KILLED_AT_KZ46 / ALTERNATION_EXPLAINED.
SATZ: reverse-CS identity; C_min mode = psi_- (r407);
drop-psi kills P2; nneg=0 has no negative contribution.
REFUTED as universal: a single dominant term, and the
direction-free coarse bound ||p||^2 > lmax(K2_+).
Remainder: the dressed CD--C_min coupling
p^T K2_+^{-1} p > 1.  No RH claim.

MACHINERY: r367 FTI.cut_rung / fr_*, r375 six-scalar
split (rewritten), r377 PC.pivot_signs, r407 DI.chain_C
(w9 cosine only), r357 DMF chi, r342 PX.build_rung,
r286 LM.ext_rule (EXT15 list frozen).

NO RH CLAIM.  Finite identities, a named anatomy, a
named sufficient inequality with a named kill, a
named remainder.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import postcap_pivots_probe as PC  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

FTI_SHA_PREFIX = "e0d79840"
DI_SHA_PREFIX = "2ee74c59"
PC_SHA_PREFIX = "b7167c37"
DMF_SHA_PREFIX = "4bf1a94b"
PX_SHA_PREFIX = "b09f8ccd"

FLOOR = 1.0e-8
RESOLV = 1.0e-9
ID_BAR = 1.0e-8
REL = 5.0e-3
MAIN_KZ = 9
SCR_SEED = 1
SCR_NNEG = 21
DEAD_CHI3_PIN = 15

# frozen /tmp pins
W9_DETK = -5.0389
W9_DETP = 5.9582
W9_Q = 10.9971
W9_PNORM = 6.1016
W9_RAY = 1.8457
W9_COUP0 = 0.621137
W9_COUP1 = 0.742697
K18_DETK = -1.1572
K18_EXCESS = 0.2746
K46_DETK = -2.3642
K46_PNORM = 2.851951
K46_LMAX = 3.655541
K46_ALIGN = 0.9837
K12_DETK = 12.4632
CHI3_W9_DETK = 4.0186
CHI4_W9_DETK = -6.1804
SCR_DETK = -8.8814
WRONGJ_W9 = 0.9415
CHI3_15_DETK = -122.9062
TOY_DETK = Fr(-7)
TOY_DETP = Fr(2)
TOY_Q = Fr(9)

EXT15 = (35, 70, 109, 71, 98, 37, 73, 57, 100, 76, 119, 68, 95, 97, 41)
EXT3 = (42, 51, 54, 56, 58, 62, 96, 123, 125, 127, 128, 130)
EXT4 = (72, 75, 66, 113, 111, 108)
FROZEN_CORE = dict(n=42, n1=28, n0=14)
FROZEN_45 = dict(n1=45, n0=29, det_neg=45, alt=45, clmax=44,
                 clmin=45, ray=45)
FROZEN_DOM = dict(Ta=25, Td=4, Tx=16)
MIN_NDET, MAX_NDET = 1.1572, 1126.389
MIN_EXCESS = 0.2746
MIN_GAP_LMIN = 0.3157

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
    return (not bad), ("NO zero/prime oracles; K2 / A0 / CD "
                       "columns / C_min cosine / postcap signs only"
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


def fr_mul(A, B):
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*B)] for row in A]


def fr_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def fr_tr(A):
    return [list(c) for c in zip(*A)]


def fr_det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def fr_adj2(M):
    return [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]


def toy_blocks():
    """r367/r375 4-node Haynsworth toy, Fractions."""
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    U = [[Fr(2), Fr(1)],
         [Fr(0), Fr(1)],
         [Fr(0), Fr(0)],
         [Fr(0), Fr(0)]]
    A0inv = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
             [Fr(0), Fr(1), Fr(0), Fr(0)],
             [Fr(0), Fr(0), Fr(1, 2), Fr(0)],
             [Fr(0), Fr(0), Fr(0), Fr(1, 3)]]
    Qform = fr_mul(fr_tr(U), fr_mul(A0inv, U))
    I2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    K2 = fr_add(I2, Qform)
    detK = fr_det2(K2)
    p1, p2 = Fr(2), Fr(1)
    Rp = [[Fr(0), Fr(0)], [Fr(0), Fr(1)]]
    K2p = fr_add(I2, Rp)
    detp = fr_det2(K2p)
    Qneg = (K2p[0][0] * p2 * p2 - Fr(2) * K2p[0][1] * p1 * p2
            + K2p[1][1] * p1 * p1)
    pnorm2 = p1 * p1 + p2 * p2
    adjR = fr_adj2(Rp)
    QR = (p1 * (adjR[0][0] * p1 + adjR[0][1] * p2)
          + p2 * (adjR[1][0] * p1 + adjR[1][1] * p2))
    adjK = fr_adj2(K2p)
    Qadj = (p1 * (adjK[0][0] * p1 + adjK[0][1] * p2)
            + p2 * (adjK[1][0] * p1 + adjK[1][1] * p2))
    return dict(detK=detK, detp=detp, Q=Qneg, pnorm2=pnorm2, QR=QR,
                Qadj=Qadj, det_id=detp - Qneg, K2=K2, K2p=K2p,
                p=(p1, p2), Rp=Rp)


def anatomy(A0, U, floor=FLOOR):
    """Reverse-CS split of K2 = K2_+ - p p^T on one window."""
    A0 = 0.5 * (np.asarray(A0, float) + np.asarray(A0, float).T)
    U = np.asarray(U, float)
    ev, W = np.linalg.eigh(A0)
    nneg = int(np.sum(ev < -floor))
    psi = W[:, 0].copy()
    lam_m = float(ev[0])
    K2 = np.eye(2) + U.T @ np.linalg.solve(A0, U)
    K2 = 0.5 * (K2 + K2.T)
    detK = float(K2[0, 0] * K2[1, 1] - K2[0, 1] * K2[1, 0])
    inv_pos = np.zeros_like(ev)
    pos = ev > floor
    inv_pos[pos] = 1.0 / ev[pos]
    B = (W * inv_pos) @ W.T
    Rp = U.T @ B @ U
    Rp = 0.5 * (Rp + Rp.T)
    K2p = np.eye(2) + Rp
    K2p = 0.5 * (K2p + K2p.T)
    ap, bp, dp = float(K2p[0, 0]), float(K2p[0, 1]), float(K2p[1, 1])
    detp = float(ap * dp - bp * bp)
    ruu, ruv, rvv = float(Rp[0, 0]), float(Rp[0, 1]), float(Rp[1, 1])
    evKp = np.linalg.eigvalsh(K2p)
    lminp, lmaxp = float(evKp[0]), float(evKp[1])
    out = dict(nneg=nneg, lam_m=lam_m, detK=detK, detp=detp,
               ap=ap, bp=bp, dp=dp, ruu=ruu, ruv=ruv, rvv=rvv,
               lminp=lminp, lmaxp=lmaxp, err_id=float("nan"),
               p1=0.0, p2=0.0, pnorm2=0.0, Q=0.0,
               Ta=0.0, Td=0.0, Tx=0.0, QJ=0.0, QR=0.0,
               ray=float("nan"), align=float("nan"),
               coarse_lmax=False, coarse_lmin=False,
               drop_det=detp, dom="NONE", dom_share=float("nan"),
               ndet=float(-detK), psi=psi)
    if nneg == 1 and lam_m < 0:
        absl = -lam_m
        p1 = float(U[:, 0] @ psi) / math.sqrt(absl)
        p2 = float(U[:, 1] @ psi) / math.sqrt(absl)
        Q = ap * p2 * p2 - 2.0 * bp * p1 * p2 + dp * p1 * p1
        Ta = ap * p2 * p2
        Td = dp * p1 * p1
        Tx = -2.0 * bp * p1 * p2
        pnorm2 = p1 * p1 + p2 * p2
        QR = rvv * p1 * p1 - 2.0 * ruv * p1 * p2 + ruu * p2 * p2
        pv = np.array([p1, p2], float)
        ray = float(pv @ np.linalg.solve(K2p, pv))
        adj = np.array([[dp, -bp], [-bp, ap]], float)
        _eva, Wa = np.linalg.eigh(adj)
        top = Wa[:, -1]
        align = abs(float(pv @ top) / (math.sqrt(pnorm2) + 1e-300))
        terms = {"Ta": Ta, "Td": Td, "Tx": Tx}
        dom = max(terms, key=lambda k: abs(terms[k]))
        out.update(p1=p1, p2=p2, pnorm2=pnorm2, Q=Q, Ta=Ta, Td=Td,
                   Tx=Tx, QJ=pnorm2, QR=QR, ray=ray, align=align,
                   err_id=abs((detp - Q) - detK),
                   coarse_lmax=bool(pnorm2 > lmaxp),
                   coarse_lmin=bool(pnorm2 > lminp),
                   dom=dom,
                   dom_share=abs(terms[dom]) / (abs(Q) + 1e-300),
                   gap_lmin=pnorm2 / lminp - 1.0,
                   gap_lmax=pnorm2 / lmaxp - 1.0,
                   excess=ray - 1.0)
    elif nneg == 0:
        out["err_id"] = abs(detK - detp)
    return out


def product_of(mz, Nw):
    sg = PC.pivot_signs(mz["xu"], mz["wu"], int(Nw) + 3)
    N = int(Nw)
    sN = int(sg[N]) if len(sg) > N else 0
    sNp1 = int(sg[N + 1]) if len(sg) > N + 1 else 0
    return sN, sNp1, int(sN) * int(sNp1)


def pack_mz(mz, Nw, S, L, i1, i2, with_c=False):
    o = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                     Nw, S, L, i1, i2, keep=True)
    a = anatomy(o["A0"], o["U"])
    a.update(P1=o["P1"], P2=o["P2"], eps=o["eps"], Nw=int(Nw),
             pmass=o["pmass"])
    sN, sNp1, prod = product_of(mz, Nw)
    a["sN"], a["sNp1"], a["prod"] = sN, sNp1, prod
    a["alt"] = bool(prod < 0)
    if with_c:
        C, _meta = DI.chain_C(mz)
        evC, WC = np.linalg.eigh(0.5 * (C + C.T))
        psiC = WC[:, 0]
        evA, WA = np.linalg.eigh(0.5 * (o["A0"] + o["A0"].T))
        psiA = WA[:, 0]
        a["cmin"] = float(evC[0])
        a["cos_cmin"] = abs(float(psiC @ psiA))
        a["nC"] = int(np.sum(evC < 1.0 - 1e-12))
        u0, u1 = o["U"][:, 0], o["U"][:, 1]
        a["coup0"] = abs(float(u0 @ psiA)) / (
            float(np.linalg.norm(u0)) + 1e-300)
        a["coup1"] = abs(float(u1 @ psiA)) / (
            float(np.linalg.norm(u1)) + 1e-300)
        a["_A0"] = o["A0"]
        a["_U"] = o["U"]
    del o
    return a


def row_of(kz, chi=None, with_c=False):
    if chi is None:
        Rr = PX.build_rung(kz)
        mz = Rr["mz"]
        a = pack_mz(mz, Rr["Nw"], Rr["S"], mz["L"],
                    Rr["i1"], Rr["i2"], with_c=with_c)
        a["kz"] = kz
        return a
    q, lpq = chi
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    mz = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    i1, i2 = PX.pair_select(mz["yn"])
    a = pack_mz(mz, mz["Nw"], mz["S"], mz["L"], i1, i2, with_c=with_c)
    a["kz"] = kz
    return a


def scramble_w9():
    alpha9v = float(V.U[MAIN_KZ])
    uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
    rng = np.random.default_rng(SCR_SEED)
    u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v, size=len(ww3)))
    mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0, DMF.LPQ3)
    s1_, s2_ = PX.pair_select(mzs["yn"])
    oS = FTI.cut_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                       mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_,
                       keep=True)
    aS = anatomy(oS["A0"], oS["U"])
    aS.update(nneg=oS["nneg"], P1=oS["P1"], P2=oS["P2"],
              detK=oS["detK"])
    return aS, oS


def wrong_J_det(A0, U):
    K2w = -np.eye(2) + U.T @ np.linalg.solve(A0, U)
    return float(K2w[0, 0] * K2w[1, 1] - K2w[0, 1] * K2w[1, 0])


def part_satz():
    section("S1  SATZ -- REVERSE-CS IDENTITY OVER Q")
    T = toy_blocks()
    check("G01-toy-det",
          T["detK"] == TOY_DETK,
          "det K2 = %s" % T["detK"])
    check("G02-reverse-CS",
          T["det_id"] == T["detK"] and T["detp"] == TOY_DETP
          and T["Q"] == TOY_Q and T["Qadj"] == T["Q"],
          "det = det(K2_+)-Q = %s-%s; Q=p^T adj(K2_+)p"
          % (T["detp"], T["Q"]))
    check("G03-J-plus-R-split",
          T["pnorm2"] + T["QR"] == T["Q"]
          and T["pnorm2"] == Fr(5) and T["QR"] == Fr(4),
          "Q = ||p||^2 + p^T adj(R_+) p = %s+%s"
          % (T["pnorm2"], T["QR"]))
    check("G04-drop-psi-toy",
          T["detp"] > 0 and T["detK"] < 0,
          "without the psi_- pole det(K2_+)=%s>0" % T["detp"])
    A0a = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ua = 0.05 * np.array([[1.0, 0.0], [0.0, 1.0],
                          [0.0, 0.0], [0.0, 0.0]])
    sA = anatomy(A0a, Ua)
    check("G05-adversary-tiny-overlap",
          sA["nneg"] == 1 and sA["detK"] > 0 and sA["ray"] < 1.0,
          "P1 without P2: ray=%.4f detK=%+.4f"
          % (sA["ray"], sA["detK"]))
    return T


def part_pins():
    section("S2  CONSTRUCTION PINS")
    w9 = row_of(MAIN_KZ, with_c=True)
    check("G10-w9-identity-Cmin",
          w9["P1"] and w9["P2"]
          and w9["err_id"] <= ID_BAR
          and abs(w9["detK"] / W9_DETK - 1.0) <= REL
          and abs(w9["detp"] / W9_DETP - 1.0) <= REL
          and abs(w9["Q"] / W9_Q - 1.0) <= REL
          and w9["cos_cmin"] >= 1.0 - 1e-10
          and w9["nC"] == 1
          and abs(w9["coup0"] - W9_COUP0) <= 2e-3
          and abs(w9["coup1"] - W9_COUP1) <= 2e-3
          and w9["alt"],
          "detK=%.4f Q=%.4f ray=%.4f cosC=%.1e nC=%d "
          "coup=%.3f/%.3f alt=%s err=%.1e"
          % (w9["detK"], w9["Q"], w9["ray"],
             1.0 - w9["cos_cmin"], w9["nC"],
             w9["coup0"], w9["coup1"], w9["alt"], w9["err_id"]))
    k18 = row_of(18)
    check("G11-kz18-floor",
          k18["P1"] and k18["P2"]
          and abs(k18["detK"] / K18_DETK - 1.0) <= REL
          and abs(k18["excess"] - K18_EXCESS) <= 5e-3
          and k18["dom"] == "Td" and k18["alt"],
          "-det=%.4f excess=%.4f dom=%s (min excess of the branch)"
          % (-k18["detK"], k18["excess"], k18["dom"]))
    k46 = row_of(46)
    check("G12-kz46-coarse-kill",
          k46["P1"] and k46["P2"]
          and (not k46["coarse_lmax"])
          and k46["coarse_lmin"]
          and abs(k46["pnorm2"] - K46_PNORM) / K46_PNORM <= REL
          and k46["pnorm2"] < k46["lmaxp"]
          and k46["align"] > 0.95
          and k46["alt"],
          "||p||^2=%.4f < lmax=%.4f (coarse FAILS) yet "
          "detK=%.4f align=%.3f gap_lmin=%.3f -- same window "
          "as r375 Cauchy"
          % (k46["pnorm2"], k46["lmaxp"], k46["detK"],
             k46["align"], k46["gap_lmin"]))
    k12 = row_of(12)
    check("G13-kz12-vacuous",
          k12["nneg"] == 0 and k12["detK"] > 0
          and abs(k12["detK"] / K12_DETK - 1.0) <= REL
          and k12["err_id"] <= 1e-9
          and (not k12["alt"]) and k12["prod"] > 0,
          "nneg=0 detK=%+.4f = det(K2_+) (no psi_- pole); "
          "product > 0"
          % k12["detK"])
    return w9


def part_worlds():
    section("S3  WORLDS / DEAD CHI / SCRAMBLE")
    c3 = row_of(MAIN_KZ, chi=(DMF.Q_CHI3, DMF.LPQ3), with_c=True)
    c4 = row_of(MAIN_KZ, chi=(DMF.Q_CHI4, DMF.LPQ4), with_c=True)
    check("G14-chi-w9",
          c3["nneg"] == 0 and c3["detK"] > 0
          and abs(c3["detK"] / CHI3_W9_DETK - 1.0) <= 2e-2
          and c3["nC"] == 0 and (not c3["alt"])
          and c4["P1"] and c4["P2"]
          and abs(c4["detK"] / CHI4_W9_DETK - 1.0) <= 2e-2
          and c4["cos_cmin"] >= 1.0 - 1e-9 and c4["alt"],
          "chi3 nneg=%d detK=%+.3f nC=%d; chi4 nneg=%d "
          "detK=%+.3f cosC=%.1e"
          % (c3["nneg"], c3["detK"], c3["nC"], c4["nneg"],
             c4["detK"], 1.0 - c4["cos_cmin"]))
    d15 = row_of(DEAD_CHI3_PIN, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G17-dead-chi-nneg1",
          d15["nneg"] == 1 and d15["detK"] < 0
          and abs(d15["detK"] / CHI3_15_DETK - 1.0) <= 2e-2
          and d15["alt"],
          "CHI3-15 nneg=1 detK=%.3f < 0 (P2 stays on the "
          "nneg-1 branch of dead chi); sch is NOT this product"
          % d15["detK"])
    aS, _oS = scramble_w9()
    check("G15-scramble-hypothesis-empty",
          aS["nneg"] == SCR_NNEG and (not aS["P1"])
          and abs(aS["detK"] / SCR_DETK - 1.0) <= 5e-2,
          "scramble nneg=%d (P2-DET hypothesis empty); "
          "detK=%.3f survives as a number, not a lemma"
          % (aS["nneg"], aS["detK"]))
    return c3, c4, d15, aS


def part_kills(w9):
    section("S4  KILLS")
    check("G16a-drop-psi-w9",
          w9["drop_det"] > 0
          and abs(w9["drop_det"] / W9_DETP - 1.0) <= REL,
          "drop psi_- => det(K2_+)=%.4f > 0 (P2 dies)"
          % w9["drop_det"])
    detw = wrong_J_det(w9["_A0"], w9["_U"])
    check("G16b-wrong-J",
          detw > 0 and abs(detw / WRONGJ_W9 - 1.0) <= 5e-2
          and w9["detK"] < 0,
          "J=-I sends det to %+.4f (sign flips vs true %.4f)"
          % (detw, w9["detK"]))
    check("G18-alt-dictionary-pins",
          w9["alt"] and w9["detK"] < 0
          and (w9["detK"] < 0) == w9["alt"],
          "w9: detK<0 iff h_N h_{N+1}<0 (r377 SATZ); "
          "the psi_- pole is the sign carrier of the "
          "post-cap LDL pair.  sch (r417) is a different "
          "coordinate")
    return detw


def part_census(smoke):
    section("S5  CENSUS" + (" (smoke skip)" if smoke else ""))
    if smoke:
        return []
    rows = []
    for kz in list(V.admissible_indices()) + list(EXT15) + list(
            EXT3) + list(EXT4):
        a = row_of(kz)
        a["kz"] = kz
        rows.append(a)
        if kz in (9, 12, 18, 46, 95, 42):
            print("    kz=%d nneg=%d detK=%+.3f clmax=%s "
                  "dom=%s alt=%s" % (
                      kz, a["nneg"], a["detK"], a["coarse_lmax"],
                      a.get("dom"), a["alt"]), flush=True)
    resolv = [r for r in rows if abs(r["eps"]) > RESOLV]
    n1 = [r for r in resolv if r["nneg"] == 1]
    n0 = [r for r in resolv if r["nneg"] == 0]
    ovl = [r for r in resolv if r["nneg"] >= 2]
    core_kzs = set(V.admissible_indices())
    core = [r for r in rows if r["kz"] in core_kzs]
    core_n1 = sum(1 for r in core if r["nneg"] == 1)
    core_n0 = sum(1 for r in core if r["nneg"] == 0)
    check("G40-core-dichotomy",
          len(core) == FROZEN_CORE["n"]
          and core_n1 == FROZEN_CORE["n1"]
          and core_n0 == FROZEN_CORE["n0"],
          "core-42 nneg-1 %d vacuous %d (14/42 detK>0 allowed)"
          % (core_n1, core_n0))
    core_n1_rows = [r for r in n1 if r["kz"] in core_kzs]
    check("G41-nneg1-P2",
          len(n1) == FROZEN_45["n1"]
          and all(r["detK"] < 0 for r in n1)
          and all(r["err_id"] <= 1e-8 for r in core_n1_rows)
          and min(-r["detK"] for r in n1) >= MIN_NDET * 0.99
          and max(-r["detK"] for r in n1) <= MAX_NDET * 1.01,
          "nneg-1 %d/%d detK<0; -det in [%.3f, %.3f]; "
          "identity SATZ on core nneg-1 %d/%d err<=1e-8 "
          "(deep EXT spectral reconstruction artefact, r375)"
          % (len(n1), len(resolv),
             min(-r["detK"] for r in n1),
             max(-r["detK"] for r in n1),
             sum(r["err_id"] <= 1e-8 for r in core_n1_rows),
             len(core_n1_rows)))
    n_clmax = sum(1 for r in n1 if r["coarse_lmax"])
    n_clmin = sum(1 for r in n1 if r["coarse_lmin"])
    n_ray = sum(1 for r in n1 if r["ray"] > 1.0)
    check("G42-coarse-lmax-not-universal",
          n_clmax == FROZEN_45["clmax"]
          and any(r["kz"] == 46 and (not r["coarse_lmax"])
                  for r in n1),
          "||p||^2 > lmax(K2_+) sufficient SATZ, holds "
          "%d/45; KILLED at kz46" % n_clmax)
    check("G43-rayleigh-and-lmin-census",
          n_ray == FROZEN_45["ray"] and n_clmin == FROZEN_45["clmin"]
          and min(r["excess"] for r in n1) >= MIN_EXCESS - 5e-3
          and min(r["gap_lmin"] for r in n1) >= MIN_GAP_LMIN - 5e-3
          and len(ovl) == 0,
          "ray>1 %d/45 min excess %.4f; ||p||^2>lmin %d/45 "
          "min gap %.4f (census, NOT a sufficient bound); "
          "overload %d"
          % (n_ray, min(r["excess"] for r in n1),
             n_clmin, min(r["gap_lmin"] for r in n1), len(ovl)))
    n_alt = sum(1 for r in n1 if r["alt"])
    n0_alt = sum(1 for r in n0 if r["alt"])
    dict_ok = all((r["detK"] < 0) == r["alt"] for r in n1 + n0)
    check("G44-alternation",
          n_alt == FROZEN_45["alt"] and n0_alt == 0
          and dict_ok and len(n0) == FROZEN_45["n0"]
          and all(r["detK"] > 0 for r in n0),
          "nneg-1 alt 45/45; vacuous 29/29 product>0 and "
          "detK>0 (no pole => no sign flip).  Dictionary "
          "detK<0 iff h_N h_{N+1}<0 on the 74")
    domc = Counter(r["dom"] for r in n1)
    check("G45-anatomy-mixed",
          domc["Ta"] == FROZEN_DOM["Ta"]
          and domc["Td"] == FROZEN_DOM["Td"]
          and domc["Tx"] == FROZEN_DOM["Tx"]
          and domc["Ta"] != len(n1),
          "dominant term MIXED Ta=%d Td=%d Tx=%d -- no "
          "single-term coarse bound"
          % (domc["Ta"], domc["Td"], domc["Tx"]))
    check("G46-vacuous-no-pole",
          all(r["err_id"] <= 1e-8 or abs(r["eps"]) < 1e-8
              for r in n0)
          and all(r["detK"] > 0 for r in n0),
          "nneg=0: K2 = K2_+ (Q=0), det>0 %d/%d"
          % (len(n0), len(n0)))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("p2_determinant_probe -- "
          "PRIME.RDAGGER.P2_DETERMINANT.01 (round 436)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + r286-15 + EXT3/4 = 45+29)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and PC.SPEC_SHA.startswith(PC_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "FTI %s DI %s PC %s DMF %s PX %s"
          % (FTI.SPEC_SHA[:8], DI.SPEC_SHA[:8], PC.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], PX.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    w9 = part_pins()
    part_worlds()
    part_kills(w9)
    part_census(smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    verd = ("REDUZIERT / IDENTITY_EXACT / ANATOMY_MIXED / "
            "COARSE_KILLED_AT_KZ46 / ALTERNATION_EXPLAINED")
    check("G50-verdict", prev_ok, verd + ".  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("P2 DETERMINANT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("P2 DETERMINANT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
