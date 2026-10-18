#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dual_intertwiner_probe -- PRIME.LDAGGER.DUAL_INTERTWINER.01
(round 407): the transport of the Gram structure through the
dual construction.  Shared named remainder of the R404/R405
north-star lanes (DCCLXXI/DCCLXXII): Euler/Digamma Grams are
exact on the WEIGHT layer, A0 = R_{N-3}-I/2 lives behind the
dual resolvent.  Sought: the exact intertwiner that carries
weight-layer sums of squares to resolvent-layer congruences.

THE CANONICAL TRANSPORT (tested first).  The CD kernel of a
positive measure is the RK of P_n in L^2(mu).  For a SUM of
measures the moment matrix is LINEAR (Hankel = integral) and
the CD kernel is the INVERSE of that Gram.  Candidate:
factor the MOMENT layer (Euler = PSD feature Gram) and
transport order through inversion (Loewner).

THE EXACT FORMULA (Leg A, SATZ).  Let u^vee_j =
(1-x_j)^2/(S |u_j| kappa_j^2) be the Borodin dual (r356;
consumes |u|, not the sign).  Let n = N_w-3, Phi the
Chebyshev-Vandermonde on the hole nodes Y, D = diag(u^vee|_Y),
A = D^{1/2} Phi, G_+ the n x n Chebyshev-Hankel of u^vee on
the mu-nodes, G_nu = A^T A, G = G_+ + G_nu.  Then
    R_{N-3} = A G^{-1} A^T = C (I+C)^{-1},
    C := A G_+^{-1} A^T.
Fractional-linear dictionary: eig(R) = lam(C)/(1+lam(C)),
hence nneg(A0) = #{lam(C) < 1} and P1 <=> lam_2(C) >= 1.
SIGNED: |wu| enters u^vee; the sign mask of wu defines Y.
The SOURCE Hankel of wu is NOT the G that R inverts.

LEGS.
  A  Closed matrix formula R = f(G); machine-exact on toys
     and w9.  Where signed (mu-nu) is consumed vs mu-only.
  B  G(mu-nu) = G(mu_P)+G(mu_A)-G(nu) exact; Euler prime-pos
     blocks = SOURCE_GRAM_EXACT on the moment layer
     (F = T_j(x) sqrt(w); residual 0; not a Cholesky of A0).
  C  nu has N_nu atoms => rank G_nu <= N_nu.  After CD
     compression / Woodbury, is the effective rank ~1
     (post-cap pivots r377)?  If yes, write the identity.
  D  If not: Loewner sandwich of f from G_+ ⪰ G ⪰ G_+-G_nu;
     does it control the 1/2-cluster?
  E  Kills: Lambda-perm of Euler moments; node jitter of
     G(nu); scramble; depth/sign mutants.  Dead chi must
     FULFILL the transport (their death is edge, r401).

CALIBRATION DISCLOSURE.  Formula residuals, C-spectrum,
nu-rank, sandwich direction, Euler Gram residual, kill
table first measured in /tmp (r407_cal.py, r407_cal2.py,
r407_cal3.py) on the same constructors, 2026-08-29.
Frozen floors below are that measurement, sealed as gates
-- not a search over 1/2.  No two-commit pre-blind freeze:
pins disclosed.  Builder fallback NOT taken: full wall
< 5 s (bar 120 s) on core-42 + chi3-42 + Twin-free.

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: Hankel G(mu-nu)=G(mu)-G(nu); two-block
    Euler split; Woodbury 2x2 (eta=5/6, det=11); R=C(I+C)^{-1}
    = I-(I+C)^{-1}; inverse Loewner-antitone; FL dictionary
    nneg(diag(2/3,1/3)-I/2)=1=#{lam(C)<1} for C=diag(2,1/2).
  * Fold linear in lags 3.541e-16 (r404 pin).  SOURCE
    Cheb-Hankel n=12: ||G(wu)-(Gmu-Gnu)||=9.2e-16.
    Euler prime-pos G = F F^T residual 1.55e-16 (class
    SOURCE_GRAM_EXACT on the moment layer).  Dual G vs
    source G rel 141 -- NOT the same Gram.
  * SIGNED: dual via signed wu produces n_neg_ud = |Y|=104
    (chain of a signed measure would break); construction
    uses abs(wu).  |ud_abs - |ud_signed|| = 0.
  * FORMULA: Chebyshev-Hankel A G^{-1} A^T matches the chain
    at small n (7.7e-16 at n=3, 3.1e-15 at n=20).  At working
    depth the stable form is the mu-OP chain (Cholesky of G_+
    in the OP basis): C = B_mu->Y B_mu->Y^T, then
    R = C(I+C)^{-1} matches R_chain at 1.8e-14 (w9) /
    3.6e-14 (kz55, where Hankel cond G = 1.7e11 mis-reads
    the razor).  FL ||sort lam/(1+lam)-eig(R)||=1.5e-13.
  * w9 C: min=0.85712, lam2=1.00018, #<1=1, |Y|=104.
    Cmin/(1+Cmin)=0.46153=rmin(R).  nneg(A0)=1.
  * Leg C REFUTED as rank-1: rank G_nu = 104 = N_nu;
    rank(R-R_mu)=104, r_eff=1.18.  Dual CD tail
    R_{Nw-1}-R_{Nw-3} is rank-2 (r363 SATZ) but
    ||P_tail v_-||=0.83 -- not the A0 defect.
  * Leg D: inv-antitone SATZ; R_mu ⪰ R (wrong direction
    for a lower bound R ⪰ I/2).  R_mu = C has rmin=0.857>1/2
    yet R dips below 1/2 exactly on {lam(C)<1}.
  * Worlds (full depth): chi3-9 nneg=C#<1=0, Cmin=1.0009;
    chi3-15 dead nneg=C#<1=1 (transport HOLDS; death is
    sch>0).  scramble 21=21; permute 20=20.
  * Core-12: nneg=C#<1 on 12/12 (incl. kz16 n=431).
  * Kills: depth n+1 rel 0.031 rank-1; Lambda-perm of
    prime-pos weights source-G rel 0.54; node-jitter of
    G(nu) rel 0.011.  Weight-jitter 1e-3 does NOT flip
    w9 nneg (Cmin 0.85712->0.85718).

AUSGANG INTERTWINER_EXACT / NU_RANK_NOT_ONE -- P1 REDUZIERT
to lam_2(C)>=1 via the fractional-linear dictionary.
SATZ: the formula, the FL dictionary, source Hankel
linearity, Euler moment Gram, signed consumption, inverse
antitone, rank-2 dual tail.  REFUTED: nu-rank ~1 after
compression; Loewner sandwich as a 1/2-threshold; Euler
source Gram as the G that R inverts.  Dead chi fulfill
the transport.  No RH claim.

MACHINERY: r356 BDH.dual_weights, r367/r398 HM.r_nm3,
r226 V.mu_chain / b_matrix / build_measures, r403 P1.reweight,
r404 OG.weights_from_c, r357 DMF chi, r369 mixed form
(Woodbury algebra; Lean r406 woodbury_inv).

NO RH CLAIM.  Finite identities, one named reduction,
named refutations.  Research documentation, not a theorem
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

import borodin_dual_hole_probe as BDH  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import one_defect_gram_probe as OG  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

BDH_SHA_PREFIX = "36141c0a"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
DMF_SHA_PREFIX = "4bf1a94b"
OG_SHA_PREFIX = "c0260053"

W9_NNEG, W9_NC, W9_NY = 1, 1, 104
W9_CMIN, W9_C2_LO = 0.85712, 1.0
W9_RMIN = 0.46153
REL_PIN = 5.0e-4
FORMULA_HI = 1.0e-8
FL_HI = 1.0e-8
FL_PERM_HI = 1.0e-5
SOURCE_LIN_HI = 1.0e-12
EULER_GRAM_HI = 1.0e-12
FOLD_LIN_HI = 1.0e-12
SOURCE_VS_DUAL_LO = 10.0
PERM_G_LO = 0.10
JITTER_G_LO = 1.0e-3
DEPTH_REL_LO = 0.01
SCR_NNEG, PERM_NNEG_LO = 21, 15
CHI9_NNEG, CHI15_NNEG = 0, 1
CORE_N, CHI3_LIVE_N, CHI3_DEAD_N = 42, 37, 5
RANK_REFF_LO = 1.05

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
                       "Chebyshev-Hankel intertwiner / C-spectrum"
                       if not bad else "; ".join(bad))


def chebV(x, n):
    x = np.asarray(x, float)
    V = np.empty((len(x), n), float)
    V[:, 0] = 1.0
    if n > 1:
        V[:, 1] = x
    for k in range(1, n - 1):
        V[:, k + 1] = 2.0 * x * V[:, k] - V[:, k - 1]
    return V


def G_of(x, w, n):
    V = chebV(x, n)
    return V.T @ (np.asarray(w, float)[:, None] * V)


def relres(A, B):
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    return float(np.linalg.norm(A - B)) / (float(np.linalg.norm(B)) + 1e-30)


def numrank(A, rel=1e-8):
    s = np.linalg.svd(np.asarray(A, float), compute_uv=False)
    if len(s) == 0 or s[0] <= 0:
        return 0, 0.0, s
    return (int(np.sum(s > rel * s[0])),
            float(np.sum(s * s) / (s[0] ** 2 + 1e-300)), s)


def R_of_G(G, A):
    X = np.linalg.solve(G, A.T)
    R = A @ X
    return 0.5 * (R + R.T)


def dual_ud(mz):
    xu = np.asarray(mz["xu"], float)
    wu = np.asarray(mz["wu"], float)
    S, L = int(mz["S"]), int(mz["L"])
    ud, *_ = BDH.dual_weights(xu, np.abs(wu), S, L)
    return xu, wu, ud


def hankel_objects(mz, n=None):
    """Chebyshev-Hankel form (closed matrix formula).  Well
    conditioned only at moderate n; the working-depth object
    is chain_C (the OP-Cholesky of the same G_+)."""
    xu, wu, ud = dual_ud(mz)
    yn = np.asarray(mz["yn"], float)
    xp = np.asarray(mz["xp"], float)
    n = int(mz["Nw"]) - 3 if n is None else int(n)
    iY = np.searchsorted(xu, yn)
    iP = np.searchsorted(xu, xp)
    Phi = chebV(yn, n)
    A = np.sqrt(np.maximum(ud[iY], 0.0))[:, None] * Phi
    Gplus = G_of(xp, ud[iP], n)
    G = Gplus + A.T @ A
    C = R_of_G(Gplus, A)
    Rf = R_of_G(G, A)
    return dict(xu=xu, wu=wu, ud=ud, yn=yn, xp=xp, n=n, A=A,
                Gplus=Gplus, G=G, C=C, Rf=Rf, iY=iY, iP=iP)


def R_from_C(C):
    C = 0.5 * (np.asarray(C, float) + np.asarray(C, float).T)
    Ic = np.eye(C.shape[0]) + C
    R = C @ np.linalg.solve(Ic, np.eye(C.shape[0]))
    return 0.5 * (R + R.T)


def chain_C(mz, n=None):
    """C = B B^T from the mu-only dual OP chain, evaluated on
    Y and dressed by sqrt(u^vee|_Y).  This IS the Cholesky of
    G_+ in the OP basis, so C = A G_+^{-1} A^T without
    forming the Hankel."""
    xu, wu, ud = dual_ud(mz)
    yn = np.asarray(mz["yn"], float)
    xp = np.asarray(mz["xp"], float)
    n = int(mz["Nw"]) - 3 if n is None else int(n)
    iY = np.searchsorted(xu, yn)
    iP = np.searchsorted(xu, xp)
    a, b, h0 = V.mu_chain(xp, ud[iP], n)
    B = V.b_matrix(a, b, h0, yn, ud[iY], n)
    C = B @ B.T
    return 0.5 * (C + C.T), dict(xu=xu, wu=wu, ud=ud, yn=yn, xp=xp,
                                 n=n, iY=iY, iP=iP, B=B)


def pack_C(mz):
    C, meta = chain_C(mz)
    R, _ = HM.r_nm3(meta["xu"], meta["wu"], meta["yn"], mz["vn"],
                    int(mz["Nw"]), int(mz["S"]), int(mz["L"]))
    Rf = R_from_C(C)
    evC = np.linalg.eigvalsh(C)
    evR = np.linalg.eigvalsh(R)
    nC = int(np.sum(evC < 1.0 - 1e-12))
    nneg = int(np.sum(evR < 0.5 - 1e-12))
    fl = float(np.linalg.norm(np.sort(evC / (1.0 + evC)) - np.sort(evR)))
    return dict(C=C, R=R, Rf=Rf, evC=evC, evR=evR, nC=nC, nneg=nneg,
                Cmin=float(evC[0]),
                C2=float(evC[1]) if len(evC) > 1 else float("nan"),
                rmin=float(evR[0]), fl=fl,
                formula=relres(Rf, R), NY=len(meta["yn"]),
                meta=meta, n=meta["n"])


def hankel_Q(x, w, n):
    G = []
    for i in range(n):
        row = []
        for k in range(n):
            s = Fr(0)
            for xj, wj in zip(x, w):
                s += wj * (xj ** (i + k))
            row.append(s)
        G.append(row)
    return G


def part_satz():
    section("S1  SATZ -- HANKEL / WOODBURY / FL DICTIONARY OVER Q")
    xs = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    w_mu = [Fr(2), Fr(3), Fr(0), Fr(0), Fr(5)]
    w_nu = [Fr(0), Fr(0), Fr(1), Fr(4), Fr(0)]
    w = [a - b for a, b in zip(w_mu, w_nu)]
    nH = 3
    Gsig = hankel_Q(xs, w, nH)
    Gmu = hankel_Q(xs, w_mu, nH)
    Gnu = hankel_Q(xs, w_nu, nH)
    check("G01-hankel-linear-Q",
          all(Gsig[i][k] == Gmu[i][k] - Gnu[i][k]
              for i in range(nH) for k in range(nH)),
          "G(mu-nu)=G(mu)-G(nu) over Q, G00=%s" % Gsig[0][0])
    w_p2 = [Fr(2), Fr(0), Fr(0), Fr(0), Fr(0)]
    w_p3 = [Fr(0), Fr(3), Fr(0), Fr(0), Fr(5)]
    Gp2, Gp3 = hankel_Q(xs, w_p2, nH), hankel_Q(xs, w_p3, nH)
    check("G02-euler-split-Q",
          all(Gmu[i][k] == Gp2[i][k] + Gp3[i][k]
              for i in range(nH) for k in range(nH)),
          "G(mu)=G(p2)+G(p3) over Q")
    H = [[Fr(2), Fr(0)], [Fr(0), Fr(3)]]
    u = [Fr(1), Fr(1)]
    eta = Fr(1, 2) + Fr(1, 3)
    Huu = [[H[0][0] + 1, Fr(1)], [Fr(1), H[1][1] + 1]]
    det = Huu[0][0] * Huu[1][1] - Huu[0][1] * Huu[1][0]
    inv = [[Huu[1][1] / det, -Huu[0][1] / det],
           [-Huu[1][0] / det, Huu[0][0] / det]]
    Hinv = [[Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 3)]]
    Hiu = [Hinv[0][0] * u[0], Hinv[1][1] * u[1]]
    den = Fr(1) + eta
    W = [[Hinv[0][0] - Hiu[0] * Hiu[0] / den,
          -Hiu[0] * Hiu[1] / den],
         [-Hiu[1] * Hiu[0] / den,
          Hinv[1][1] - Hiu[1] * Hiu[1] / den]]
    check("G03-woodbury-Q",
          W == inv and eta == Fr(5, 6) and det == Fr(11),
          "eta=%s det=%s" % (eta, det))
    Cq = [[Fr(1), Fr(0)], [Fr(0), Fr(2)]]
    Rq = [[Fr(1, 2), Fr(0)], [Fr(0), Fr(2, 3)]]
    via = [[Cq[0][0] / (1 + Cq[0][0]), Fr(0)],
           [Fr(0), Cq[1][1] / (1 + Cq[1][1])]]
    viaI = [[Fr(1) - Fr(1, 2), Fr(0)], [Fr(0), Fr(1) - Fr(1, 3)]]
    check("G04-R-C-formula-Q",
          via == Rq and viaI == Rq,
          "R=C(I+C)^{-1}=I-(I+C)^{-1} over Q")
    Ainv = [Fr(1, 2), Fr(1, 4)]
    Binv = [Fr(1), Fr(1, 3)]
    check("G05-inv-antitone-Q",
          Ainv[0] <= Binv[0] and Ainv[1] <= Binv[1],
          "diag(2,4)^{-1} ≼ diag(1,3)^{-1}")
    # C=diag(2,1/2) => R=diag(2/3,1/3); #<1 of C is 1; nneg(R-I/2)=1
    Cfl = (Fr(2), Fr(1, 2))
    Rfl = tuple(c / (1 + c) for c in Cfl)
    nC = sum(1 for c in Cfl if c < 1)
    nneg = sum(1 for r in Rfl if r < Fr(1, 2))
    check("G06-FL-dictionary-Q",
          nC == 1 and nneg == 1 and Rfl == (Fr(2, 3), Fr(1, 3)),
          "C=(2,1/2) => R=(2/3,1/3); nneg=#{lam C<1}=1")


def part_w9():
    section("S2  LEG A/B/C -- FORMULA, SOURCE GRAM, NU RANK (w9)")
    mz = V.build_measures(9)
    pk = pack_C(mz)
    meta = pk["meta"]
    cP, _ka = V.prime_lags(mz["alpha"], mz["M"], mz["D"])
    cA = V.arch_lags(mz["M"], mz["D"])
    _xP, wP = OG.weights_from_c(9, cP)
    _xA, wA = OG.weights_from_c(9, cA)
    _xF, wF = OG.weights_from_c(9, cP + cA)
    lin = float(np.linalg.norm(wF - (wP + wA))) / (
        float(np.linalg.norm(wF)) + 1e-30)
    check("G10-fold-linear",
          lin <= FOLD_LIN_HI,
          "||w-(wP+wA)||/||w||=%.3e" % lin)

    n12 = 12
    Gsrc = G_of(meta["xu"], meta["wu"], n12)
    Gmu = G_of(meta["xp"], np.asarray(mz["wp"], float), n12)
    Gnu = G_of(meta["yn"], np.asarray(mz["vn"], float), n12)
    slin = relres(Gsrc, Gmu - Gnu)
    check("G11-source-hankel-linear",
          slin <= SOURCE_LIN_HI,
          "||G(wu)-(Gmu-Gnu)||/||G||=%.3e (n=12)" % slin)

    xP, wPraw = OG.weights_from_c(9, cP)
    wPpos = np.maximum(wPraw, 0.0)
    Gp = G_of(xP, wPpos, 8)
    F = chebV(xP, 8) * np.sqrt(wPpos)[:, None]
    eug = relres(Gp, F.T @ F)
    evp = np.linalg.eigvalsh(Gp)
    check("G12-euler-moment-SOURCE_GRAM_EXACT",
          eug <= EULER_GRAM_HI and int(np.sum(evp < -1e-12)) == 0,
          "||G-FF^T||=%.3e lam_min=%.3e (moment layer, not A0)"
          % (eug, float(evp[0])))

    kap = np.where(
        np.rint(np.arccos(np.clip(meta["xu"], -1.0, 1.0)) * int(mz["L"])
                / (2.0 * math.pi)).astype(int) == int(mz["S"]),
        2.0, 1.0)
    ud_s = (1.0 - meta["xu"]) ** 2 / (int(mz["S"]) * meta["wu"] * kap * kap)
    n_neg_ud = int(np.sum(ud_s < 0))
    check("G13-signed-consumed-as-abs",
          n_neg_ud == W9_NY
          and float(np.max(np.abs(meta["ud"] - np.abs(ud_s)))) == 0.0,
          "signed dual n_neg_ud=%d (=|Y|); chain uses abs(wu)"
          % n_neg_ud)

    hk = hankel_objects(mz, n=20)
    a20, b20, h20 = V.mu_chain(meta["xu"], meta["ud"], 20)
    B20 = V.b_matrix(a20, b20, h20, meta["yn"], meta["ud"][meta["iY"]], 20)
    hres = relres(hk["Rf"], B20 @ B20.T)
    check("G14-formula-w9",
          pk["formula"] <= FORMULA_HI and pk["NY"] == W9_NY
          and hres <= FORMULA_HI,
          "chain C(I+C)^{-1} vs R ||=%.3e  n=%d |Y|=%d; "
          "Hankel n=20 vs chain ||=%.3e"
          % (pk["formula"], pk["n"], pk["NY"], hres))
    check("G15-FL-map-w9",
          pk["fl"] <= FL_HI
          and abs(pk["Cmin"] / (1.0 + pk["Cmin"]) - pk["rmin"])
          <= REL_PIN * W9_RMIN,
          "||lam/(1+lam)-eig R||=%.3e  Cmin/(1+Cmin)=%.5f rmin=%.5f"
          % (pk["fl"], pk["Cmin"] / (1.0 + pk["Cmin"]), pk["rmin"]))
    check("G16-C-anatomy-w9",
          pk["nneg"] == W9_NNEG and pk["nC"] == W9_NC
          and abs(pk["Cmin"] - W9_CMIN) <= REL_PIN * W9_CMIN
          and pk["C2"] >= W9_C2_LO
          and abs(pk["rmin"] - W9_RMIN) <= REL_PIN * W9_RMIN,
          "nneg=%d C#<1=%d Cmin=%.5f C2=%.5f rmin=%.5f  "
          "(P1 <=> lam2(C)>=1)"
          % (pk["nneg"], pk["nC"], pk["Cmin"], pk["C2"], pk["rmin"]))

    hkF = hankel_objects(mz)
    rnu, reff, _s = numrank(hkF["A"].T @ hkF["A"], 1e-8)
    Rmu = pk["C"]
    rd, reffd, _sd = numrank(pk["Rf"] - Rmu, 1e-8)
    check("G17-nu-rank-not-one",
          rnu == W9_NY and rd == W9_NY and reffd >= RANK_REFF_LO,
          "rank G_nu=%d rank(R-C)=%d reff=%.2f (=N_nu, not 1)"
          % (rnu, rd, reffd))

    Gdual = G_of(meta["xu"], meta["ud"], n12)
    svd = relres(Gdual, Gsrc)
    check("G18-source-G-is-not-dual-G",
          svd >= SOURCE_VS_DUAL_LO,
          "dual G vs source G n=12 rel=%.1f (R inverts dual, "
          "not Euler-source)" % svd)

    evs = np.linalg.eigvalsh(Rmu - pk["Rf"])
    evRm = np.linalg.eigvalsh(Rmu)
    check("G19-sandwich-wrong-direction",
          float(evs[0]) > -1e-8 and float(evRm[0]) > 0.5
          and pk["rmin"] < 0.5,
          "C ⪰ R (lam_min dR=%.3e); C min=%.4f>1/2 yet "
          "R min=%.4f<1/2 -- Loewner upper-bounds R"
          % (float(evs[0]), float(evRm[0]), pk["rmin"]))
    return dict(mz=mz, pk=pk, Gsrc=Gsrc, Gnu=Gnu, eug=eug)


def part_kills(w9):
    section("S3  LEG E -- MUTANTS / WORLDS")
    mz, pk = w9["mz"], w9["pk"]
    C1, _m1 = chain_C(mz, n=pk["n"] + 1)
    Rf1 = R_from_C(C1)
    drel = relres(Rf1, pk["R"])
    rd, _reff, _s = numrank(Rf1 - pk["R"], 1e-8)
    check("G20-depth-mutant",
          drel >= DEPTH_REL_LO and rd == 1,
          "||R_{n+1}-R_n||/||R||=%.3f rank=%d (wrong depth)"
          % (drel, rd))

    mzP = P1.reweight(mz, "permute", 1000)
    pP = pack_C(mzP)
    check("G21-permute",
          pP["nneg"] >= PERM_NNEG_LO and pP["nC"] == pP["nneg"]
          and pP["fl"] <= FL_PERM_HI,
          "permute nneg=%d C#<1=%d FL=%.3e (kills P1; "
          "transport still holds)" % (pP["nneg"], pP["nC"], pP["fl"]))

    pS = pack_C(HM.scramble_mz())
    check("G22-scramble",
          pS["nneg"] == SCR_NNEG and pS["nC"] == SCR_NNEG
          and pS["fl"] <= FL_HI,
          "scramble nneg=%d C#<1=%d FL=%.3e" % (
              pS["nneg"], pS["nC"], pS["fl"]))

    rng = np.random.default_rng(407)
    cP, _ka = V.prime_lags(mz["alpha"], mz["M"], mz["D"])
    xP, wPraw = OG.weights_from_c(9, cP)
    wPpos = np.maximum(wPraw, 0.0)
    Gp = G_of(xP, wPpos, 8)
    Gp2 = G_of(xP, rng.permutation(wPpos), 8)
    rP = relres(Gp2, Gp)
    check("G23-Lambda-perm-breaks-euler-G",
          rP >= PERM_G_LO,
          "prime-pos weight perm source-G rel=%.3f (moments "
          "tied to p)" % rP)

    yn = pk["meta"]["yn"]
    vn = np.asarray(mz["vn"], float)
    yn_j = np.clip(yn + 1e-3 * rng.normal(0.0, 1.0, size=len(yn)),
                   -0.999, 0.999)
    rJ = relres(G_of(yn_j, vn, 12), w9["Gnu"])
    check("G24-node-jitter-breaks-Gnu",
          rJ >= JITTER_G_LO,
          "G(nu) node-jitter rel=%.3f (node binding)" % rJ)

    pL = pack_C(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    check("G25-chi-live-transport",
          pL["nneg"] == CHI9_NNEG and pL["nC"] == CHI9_NNEG
          and pL["formula"] <= FORMULA_HI and pL["Cmin"] >= 1.0,
          "chi3-9 nneg=%d C#<1=%d Cmin=%.4f formula=%.3e" % (
              pL["nneg"], pL["nC"], pL["Cmin"], pL["formula"]))
    pD = pack_C(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G26-chi-dead-FULFILLS-transport",
          pD["nneg"] == CHI15_NNEG and pD["nC"] == CHI15_NNEG
          and pD["formula"] <= FORMULA_HI,
          "chi3-15 dead nneg=%d C#<1=%d (death is edge, not "
          "a broken intertwiner)" % (pD["nneg"], pD["nC"]))
    return dict(pP=pP, pS=pS, rP=rP, rJ=rJ)


def part_census():
    section("S4  CORE-42 + CHI3 -- nneg(A0) = #{lam(C)<1}")
    core = list(V.admissible_indices())
    n_ag, n_p1, n_vac = 0, 0, 0
    for kz in core:
        d = pack_C(V.build_measures(kz))
        ok = d["nneg"] == d["nC"]
        n_ag += int(ok)
        n_p1 += int(d["nneg"] == 1)
        n_vac += int(d["nneg"] == 0)
        if not ok:
            print("    DIFF kz=%d nneg=%d C#<1=%d" % (
                kz, d["nneg"], d["nC"]), flush=True)
    check("G40-core-FL-dictionary",
          len(core) == CORE_N and n_ag == CORE_N
          and n_p1 + n_vac == CORE_N,
          "core-%d nneg=C#<1 on %d/%d (P1 %d / vacuous %d)"
          % (CORE_N, n_ag, CORE_N, n_p1, n_vac))

    live, dead = [], []
    for kz in core:
        mz3 = HM.chi_mz(kz, DMF.Q_CHI3, DMF.LPQ3)
        if mz3 is None:
            continue
        d = pack_C(mz3)
        row = (kz, d["nneg"], d["nC"], d["nneg"] == d["nC"])
        (dead if kz in HM.DEAD_CHI3 else live).append(row)
    nL = sum(1 for r in live if r[3])
    nD = sum(1 for r in dead if r[3])
    check("G41-chi3-live",
          len(live) == CHI3_LIVE_N and nL == CHI3_LIVE_N,
          "live chi3 %d/%d nneg=C#<1 (transport holds)"
          % (nL, CHI3_LIVE_N))
    check("G42-chi3-dead",
          len(dead) == CHI3_DEAD_N and nD == CHI3_DEAD_N,
          "dead chi3 %d/%d nneg=C#<1 -- transport FULFILLED; "
          "death remains sch>0" % (nD, CHI3_DEAD_N))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("dual_intertwiner_probe -- "
          "PRIME.LDAGGER.DUAL_INTERTWINER.01 (round 407)")
    print("SPEC_SHA %s   (BDH %s / HM %s / P1 %s / DMF %s / OG %s)"
          % (SPEC_SHA[:16], BDH.SPEC_SHA[:16], HM.SPEC_SHA[:16],
             P1.SPEC_SHA[:16], DMF.SPEC_SHA[:16], OG.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and OG.SPEC_SHA.startswith(OG_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "BDH %s / HM %s / P1 %s / DMF %s / OG %s"
          % (BDH.SPEC_SHA[:8], HM.SPEC_SHA[:8], P1.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], OG.SPEC_SHA[:8]))

    part_satz()
    w9 = part_w9()
    part_kills(w9)
    if not smoke:
        part_census()
    else:
        section("S4  CORE/CHI3 census skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-INTERTWINER",
          prev_ok,
          "INTERTWINER_EXACT / NU_RANK_NOT_ONE: R=C(I+C)^{-1} "
          "SATZ; P1 <=> lam2(C)>=1; nu-rank = N_nu; no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "INTERTWINER_EXACT"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("DUAL INTERTWINER %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DUAL INTERTWINER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
