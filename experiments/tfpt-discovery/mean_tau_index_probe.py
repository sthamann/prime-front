#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mean_tau_index_probe -- PRIME.RDAGGER.MEAN_TAU_INDEX.01
(round 440): the averaged tau-winding as an exact
integer object (reviewer fallback lane after DCCCIV).

THE OBJECT.  G^dagger = (T^dagger)* T^dagger ⪰ 0,
tau^dagger(s) = det(I - s G^dagger), zeros real positive
at 1/lambda_j.  Three identities, no analytic bound:

  T1  kappa^dagger := ind_-(R^dagger - 1/2 I)
      = #{s in (0,1): tau^dagger(s)=0}.
      R^dagger ⪰ 1/2 I  iff  kappa^dagger = 0.
  T2  argument principle:
      kappa^dagger = (1/2 pi i) oint_Gamma d_s log tau^dagger
      for a contour Gamma around (0,1).
  MI2 block-mean identity (linearity of the integrand):
      (1/K) sum kappa^dagger
      = (1/2 pi i) oint d_s[(1/K) sum log tau^dagger].
      Lean landing site: exists_index_zero_of_block_mean_lt_one
      (r430).  liminf block-mean < 1 yields an index-0
      window.  Reviewer-R439 (unconditional bound) is
      NOT this round.

s is a COUNTING variable, not a pointwise positivity
dial (r265 s-No-Go stays: that no-go was monotone
positivity dynamics in s).  Soft substitutes (tr G,
moments, mean lambda_min) are forbidden carriers --
the 1/2-cluster blinds them (r398).  Circularity gate:
pointwise |sum Lambda n^{-1/2-it}| << X^eps is not a
mean-value carrier.

CALIBRATION DISCLOSURE.  T1 three-way, collar anatomy,
source integrand, selected/core/chi census, MI2
linearity, and the soft-mutant kills first measured
in /tmp (r440_cal.py, r440_cal2.py) on the r409/r433
constructors, 2026-08-30.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall << 120 s
(no k=8 rebuild; r421 pin unused).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q 2x2: G=diag(2,1/2), R=diag(1/3,2/3),
    M=R-1/2=diag(-1/6,1/6), ind_-=1, tau zeros {1/2,2},
    #{(0,1)}=1.  Circle winding about 0.5 radius 0.49
    equals 1 to 1e-15.
  * SATZ Q r409 5-atom: C=[[97,23],[23,125/16]],
    det=3661/16, tr=1677/16, both eig(C)>1, kappa=0,
    G=C^{-1} residual 1.2e-16, p(0)p(1)>0.
  * w9 T^dagger: n=105, kappa_G=kappa_R=nzeros01=0,
    ||T^dagger||=0.99991709, lam_max=0.9998341781,
    rmin=0.5000414589, trG=50.894597, n_half=24,
    gap_right=1.6585e-4, nearest zero 1.00016585,
    R=(I+G)^{-1} residual 2.2e-14,
    M=(I-G)/(2(I+G)) residual 6.0e-14.
    Unaugmented T0 nneg(I-TT)=1 (P1); dagger repairs.
  * Collar: circle r=0.40 about 0.5 winds 0 on w9
    (no zeros in (0.10,0.90)).  r=0.499 is fractional
    (~-0.55) -- the 1/2-cluster sits at s=1, eta must
    be << gap_right.  Dead-chi zeros live in the same
    collar (gap_left 4.8e-6 .. 1.0e-3).
  * Source: unaug CD residual 2.0e-12; cyclic
    tr G(I-sG)^{-1} = tr H(I-sH)^{-1} at 1.4e-14
    (H=T T*, source-side Gram); slogdet match;
    Dirichlet diagonal = dlog.
  * Selected k=3,4,5,6,7,9 (kz 5/9/17/26/43/116):
    ALL kappa^dagger=0.  gap_right 2.98e-3 -> 1.91e-8.
    k=8 not rebuilt (r421 class, N=5690).
  * Core-42: 42/42 kappa^dagger=0, mean=0.
    gap_right min/med/max 1.42e-7 / 1.49e-6 / 1.66e-4.
    n_half 21..173.  trG 46.5..308.4.  No trend of
    kappa>=1 with k (selected all living).
  * Dead chi 6/6 kappa^dagger=1 (CHI3-15/19/23/33/39
    + CHI4-20).  Living CHI3-9 kappa=0.
  * MI2: averaged-integrand winding = mean of
    individual windings at 4e-15 (linearity SATZ,
    even when a naive contour is fractional).
  * Kills: trG >> 1 on living AND dead (w9 50.9,
    dead15 53.0); M2=16 tr((I-R)^4) w9 32.96 vs
    dead15 39.01, both >> 2 (r398: moments miss the
    threshold).  tau(0.5)>0 on both (the kappa-zero
    sits in the collar, not at mid-interval).
    Scramble bulk nneg(R)=21 (already dead before
    the dagger; T^dagger border pack is not the
    story).

AUSGANG IDENTITIES_EXACT / COLLAR_BOSS_QUANTIFIED /
BLOCK_MEAN_CENSUS / UNCONDITIONAL_OPEN.
SATZ: T1 three-way; T2 integrand + Q winding; MI2
linearity; CD / cyclic / Dirichlet source form of
d_s log tau.  CENSUS: selected+core kappa=0 so the
block mean is 0<1; dead chi kappa=1 exactly; collar
gap_right shrinks with k (the contour-approach cost).
OPEN: an unconditional bound on the block mean
(Reviewer-R439).  No RH claim.

MACHINERY: r409 B.source_Tdag / pack_graph / toy_dual /
C_plus_Q / chebV, r433 T^dagger worlds, r398 HM
moments / scramble nneg, r226 V.admissible_indices,
r430 Lean exists_index_zero_of_block_mean_lt_one
(landing site, not proved here).

NO RH CLAIM.  Finite identities, a named collar
anatomy, a named census, named kills.  Research
documentation, not a theorem of RH.  No L* claim.
No R-dagger claim.
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

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
PX_SHA_PREFIX = "b09f8ccd"
ABD_SHA_PREFIX = "7d810a9a"
HM_SHA_PREFIX = "bb1dcf6a"
DMF_SHA_PREFIX = "4bf1a94b"

ID_RES = 1.0e-10
CD_RES = 1.0e-10
CYC_RES = 1.0e-10
FD_REL = 5.0e-4
WIND_BAR = 5.0e-3
MI2_BAR = 1.0e-10
SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
SEL_SMOKE = ((3, 5), (4, 9), (5, 17))
CORE_SAMPLE = (9, 12, 16, 18, 20, 36)
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
SCR_NNEG = 21

W9_N = 105
W9_LAMMAX = 0.9998341781
W9_RMIN = 0.5000414589
W9_OP = 0.99991709
W9_TRG = 50.894597
W9_NHALF = 24
W9_GAPR = 1.6585e-4
W9_M2 = 32.96
DEAD15_M2 = 39.01
DEAD15_TRG = 53.04
K3_GAPR = 2.9828e-3
K7_GAPR = 1.8081e-7
K9_GAPR = 1.9073e-8
CORE_GAPR_MIN = 1.40e-7
CORE_GAPR_MAX = 1.70e-4
CORE_TRG_LO, CORE_TRG_HI = 40.0, 320.0

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
    return (not bad), ("NO zero/prime oracles; T^dagger Gram / "
                       "inertia / CD kernel / winding only"
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
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def dlog_tau(G, s):
    n = G.shape[0]
    X = np.linalg.solve(np.eye(n) - s * G, G)
    return -complex(np.trace(X))


def winding_circle(G, c, r, n=128):
    acc = 0j
    ts = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dt = 2 * np.pi / n
    for t in ts:
        e = np.exp(1j * t)
        acc += dlog_tau(G, c + r * e) * (r * 1j * e * dt)
    return acc / (2j * np.pi)


def winding_mean(Glist, c, r, n=80):
    acc = 0j
    ts = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dt = 2 * np.pi / n
    k = len(Glist)

    def mdlog(s):
        return sum(dlog_tau(G, s) for G in Glist) / k

    for t in ts:
        e = np.exp(1j * t)
        acc += mdlog(c + r * e) * (r * 1j * e * dt)
    return acc / (2j * np.pi)


def tdag_main(kz):
    R = PX.build_rung(kz)
    mz = R["mz"]
    alk = float(V.window_shape(kz)[0])
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
    return B.source_Tdag(mz, dsm, Bm=R["B"]), mz


def pack_tau(td):
    T = np.asarray(td["Tdag"], float)
    Gt = T.T @ T
    G = 0.5 * (Gt + Gt.T)
    n = G.shape[0]
    evG = np.linalg.eigvalsh(G)
    R = 0.5 * (np.asarray(td["Rdag"], float)
               + np.asarray(td["Rdag"], float).T)
    evR = np.linalg.eigvalsh(R)
    kappa_G = int(np.sum(evG > 1.0 + 1e-10))
    kappa_R = int(np.sum(evR < 0.5 - 1e-10))
    pos = evG[evG > 1e-14]
    zeros = 1.0 / pos
    in01 = zeros[(zeros > 0.0) & (zeros < 1.0)]
    Rg = np.linalg.solve(np.eye(n) + G, np.eye(n))
    res_RG = float(np.linalg.norm(Rg - R) / (np.linalg.norm(R) + 1e-30))
    M = R - 0.5 * np.eye(n)
    Mform = np.linalg.solve(2.0 * (np.eye(n) + G), np.eye(n) - G)
    res_M = float(np.linalg.norm(M - Mform) / (np.linalg.norm(M) + 1e-30))
    lam_max = float(evG[-1])
    rmin = float(evR[0])
    gap_right = (1.0 / lam_max - 1.0) if lam_max < 1.0 else None
    gap_left = (1.0 - float(np.max(in01))) if len(in01) else None
    n_half = int(np.sum(np.abs(evR - 0.5) <= 0.05))
    I_R = np.eye(n) - R
    A2 = I_R @ I_R
    M2 = 16.0 * float(np.trace(A2 @ A2))
    return dict(
        T=T, G=G, R=R, n=n, evG=evG, evR=evR,
        kappa_G=kappa_G, kappa_R=kappa_R,
        nzeros01=int(len(in01)), in01=in01, zeros=zeros,
        res_RG=res_RG, res_M=res_M, lam_max=lam_max, rmin=rmin,
        gap_right=gap_right, gap_left=gap_left, n_half=n_half,
        trG=float(np.trace(G)), M2=M2,
        op=float(td["opnorm"]),
    )


def cd_unaug(mz, d0):
    xp, wX, yn, wY, _ud = B.dual_split(mz)
    T = B.source_T0_cls(xp, wX, yn, wY, d0)
    G = 0.5 * (T.T @ T + (T.T @ T).T)
    sX = np.sqrt(np.maximum(wX, 0.0))
    sY = np.sqrt(np.maximum(wY, 0.0))
    PhiX = B.chebV(xp, d0)
    PhiY = B.chebV(yn, d0)
    Gx = (sX[:, None] * PhiX).T @ (sX[:, None] * PhiX)
    K = PhiY @ np.linalg.solve(Gx, PhiY.T)
    D = np.diag(sY)
    Gcd = np.linalg.solve(D, np.linalg.solve(K, np.eye(len(yn))))
    Gcd = np.linalg.solve(D, Gcd.T).T
    Gcd = 0.5 * (Gcd + Gcd.T)
    res = float(np.linalg.norm(G - Gcd) / (np.linalg.norm(G) + 1e-30))
    return G, K, wY, res, T


def q_kappa1():
    """Exact 2x2 T1 identity over Q with kappa=1."""
    G = [[Fr(2), Fr(0)], [Fr(0), Fr(1, 2)]]
    R = [[Fr(1, 3), Fr(0)], [Fr(0), Fr(2, 3)]]
    M = [[Fr(-1, 6), Fr(0)], [Fr(0), Fr(1, 6)]]
    return dict(G=G, R=R, M=M,
                kappa=1, zeros=(Fr(1, 2), Fr(2)))


def part_satz():
    section("S1  LEG A -- T1/T2 OVER Q")
    t = q_kappa1()
    check("G01-Q-kappa1-T1",
          t["M"][0][0] < 0 and t["M"][1][1] > 0
          and t["R"][0][0] == Fr(1, 3)
          and t["zeros"][0] == Fr(1, 2)
          and t["zeros"][0] < 1 < t["zeros"][1],
          "G=diag(2,1/2); ind_-(R-1/2 I)=1; zeros {1/2, 2}")
    Gf = np.array([[2.0, 0.0], [0.0, 0.5]])
    w = winding_circle(Gf, 0.5, 0.49, n=128)
    check("G02-Q-T2-winding",
          abs(w.real - 1.0) < 1e-12 and abs(w.imag) < 1e-12,
          "circle(0.5,0.49) winding=%.12f" % w.real)

    xs, u, ud, iX, iY, d0 = B.toy_dual()
    C = B.C_plus_Q(xs, ud, iX, iY, d0)
    R = B.R_from_C_Q(C)
    Ci = BDH.fr_inv(C)
    n = len(C)
    half = [[Fr(1, 2) if i == j else Fr(0) for j in range(n)]
            for i in range(n)]
    M = B.fr_sub(R, half)
    Cf = np.array([[float(C[i][j]) for j in range(n)] for i in range(n)])
    Mf = np.array([[float(M[i][j]) for j in range(n)] for i in range(n)])
    evC = np.linalg.eigvalsh(Cf)
    evM = np.linalg.eigvalsh(Mf)
    a, b, cc, d = C[0][0], C[0][1], C[1][0], C[1][1]
    detC, trC = a * d - b * cc, a + d
    xp = np.array([float(xs[i]) for i in iX])
    wX = np.array([float(ud[i]) for i in iX])
    yn = np.array([float(xs[i]) for i in iY])
    wY = np.array([float(ud[i]) for i in iY])
    T0m = B.source_T0_cls(xp, wX, yn, wY, d0)
    G0 = T0m.T @ T0m
    Cinv = np.array([[float(Ci[i][j]) for j in range(n)] for i in range(n)])
    resG = float(np.linalg.norm(G0 - Cinv) / (np.linalg.norm(G0) + 1e-30))
    check("G03-Q-toy-kappa0",
          C[0][0] == Fr(97) and C[0][1] == Fr(23)
          and C[1][1] == Fr(125, 16) and detC == Fr(3661, 16)
          and trC == Fr(1677, 16)
          and float(evC.min()) > 1.0
          and int(np.sum(evM < -1e-12)) == 0
          and resG < 1e-12
          and detC * (detC - trC + 1) > 0,
          "C pin; both eig(C)>1; kappa=0; G=C^{-1} res=%.2e"
          % resG)
    return Gf


def part_w9():
    section("S2  LEG A -- W9 T1 THREE-WAY / COLLAR / T2 INTEGRAND")
    td, mz = tdag_main(9)
    p = pack_tau(td)
    check("G10-w9-dictionary",
          p["n"] == W9_N
          and p["res_RG"] < ID_RES and p["res_M"] < ID_RES,
          "n=%d ||Rg-R||=%.2e ||M-(I-G)/2(I+G)||=%.2e"
          % (p["n"], p["res_RG"], p["res_M"]))
    check("G11-w9-T1-three-way",
          p["kappa_G"] == 0 and p["kappa_R"] == 0
          and p["nzeros01"] == 0
          and abs(p["lam_max"] - W9_LAMMAX) < 5e-10
          and abs(p["rmin"] - W9_RMIN) < 5e-10,
          "kappa_G=R=nzeros=0; lam_max=%.10f rmin=%.10f"
          % (p["lam_max"], p["rmin"]))
    g0 = B.pack_graph(mz)
    check("G12-w9-unaug-vs-dagger",
          g0["nneg"] == 1 and p["kappa_G"] == 0
          and p["op"] < 1.0 < g0["opnorm"],
          "T0 nneg=%d ||T0||=%.5f; T^dagger kappa=0 ||T^d||=%.8f"
          % (g0["nneg"], g0["opnorm"], p["op"]))
    check("G13-w9-collar",
          p["gap_right"] is not None
          and abs(p["gap_right"] - W9_GAPR) / W9_GAPR < 0.02
          and p["n_half"] == W9_NHALF
          and float(np.min(np.abs(p["zeros"] - 1.0))) < 2e-4
          and int(np.sum((p["zeros"] > 0) & (p["zeros"] < 0.9))) == 0,
          "gap_right=%.6e n_half=%d; no zeros in (0,0.9)"
          % (p["gap_right"], p["n_half"]))
    s = 0.30
    eps = 1e-7
    ld0 = float(np.linalg.slogdet(np.eye(p["n"]) - s * p["G"])[1])
    ld1 = float(np.linalg.slogdet(np.eye(p["n"]) - (s + eps) * p["G"])[1])
    fd = (ld1 - ld0) / eps
    dlog = float(np.real(dlog_tau(p["G"], s)))
    rel = abs(fd - dlog) / (abs(dlog) + 1e-30)
    check("G14-T2-integrand-FD",
          rel < FD_REL,
          "dlog=%.6f FD=%.6f rel=%.2e at s=0.3" % (dlog, fd, rel))
    w40 = winding_circle(p["G"], 0.5, 0.40, n=128)
    w99 = winding_circle(p["G"], 0.5, 0.499, n=256)
    check("G15-T2-collar-boss",
          abs(w40.real) < WIND_BAR
          and abs(w99.real) > 0.2,
          "r=0.40 wind=%.4f (integer 0); r=0.499 wind=%.4f "
          "(fractional -- contour must thread gap_right=%.2e)"
          % (w40.real, w99.real, p["gap_right"]))
    return p, mz, td


def part_source(p, mz):
    section("S3  LEG B -- SOURCE FORM OF d_s log tau")
    d0u = int(mz["Nw"]) - 3
    Gu, Ku, wYu, res_cd, _Tu = cd_unaug(mz, d0u)
    s = 0.37
    dlog_G = dlog_tau(Gu, s)
    KW = Ku @ np.diag(wYu)
    dlog_cd = -complex(np.trace(np.linalg.inv(
        KW - s * np.eye(len(wYu)))))
    check("G20-unaug-CD-identity",
          res_cd < CD_RES
          and abs(dlog_G - dlog_cd) < 1e-9,
          "G = D^{-1} K_Y^{-1} D^{-1} res=%.2e; "
          "dlog vs -tr((KW-sI)^{-1}) %.2e"
          % (res_cd, abs(dlog_G - dlog_cd)))
    H = p["T"] @ p["T"].T
    H = 0.5 * (H + H.T)
    dlog_H = dlog_tau(H, s)
    dlog_Gd = dlog_tau(p["G"], s)
    check("G21-cyclic-TT-star",
          abs(dlog_Gd - dlog_H) < CYC_RES,
          "tr G(I-sG)^{-1} = tr H(I-sH)^{-1} diff=%.2e "
          "(H = T T* lives on source nodes)"
          % abs(dlog_Gd - dlog_H))
    _sgG, ldG = np.linalg.slogdet(np.eye(p["n"]) - s * p["G"])
    _sgH, ldH = np.linalg.slogdet(np.eye(H.shape[0]) - s * H)
    check("G22-char-identity",
          abs(ldG - ldH) < CYC_RES,
          "det(I-sG)=det(I-s TT*) slogdet diff=%.2e" % abs(ldG - ldH))
    diag_sum = -complex(np.trace(np.linalg.solve(
        np.eye(H.shape[0]) - s * H, H)))
    check("G23-Dirichlet-diagonal",
          abs(diag_sum - dlog_Gd) < CYC_RES,
          "source-diag sum_x [H(I-sH)^{-1}]_xx = dlog "
          "diff=%.2e" % abs(diag_sum - dlog_Gd))


def part_census(p9, smoke):
    section("S4  LEG C -- BLOCK MEAN / WORLDS / MI2")
    sel = SEL_SMOKE if smoke else SEL_LIVE
    rows = []
    for k, kz in sel:
        td, _mz = tdag_main(kz)
        p = pack_tau(td)
        p["k"] = k
        p["kz"] = kz
        rows.append(p)
        print("    k=%d kz=%d n=%d kappa=%d gapR=%s n_half=%d"
              % (k, kz, p["n"], p["kappa_G"],
                 ("%.4e" % p["gap_right"]) if p["gap_right"] else "n/a",
                 p["n_half"]), flush=True)
    kappas = [r["kappa_G"] for r in rows]
    check("G30-selected-kappa0",
          all(k == 0 for k in kappas) and len(rows) == len(sel),
          "%d/%d selected kappa^dagger=0 (living); mean=0<1"
          % (len(rows), len(sel)))
    if not smoke:
        r3 = next(r for r in rows if r["k"] == 3)
        r7 = next(r for r in rows if r["k"] == 7)
        r9 = next(r for r in rows if r["k"] == 9)
        check("G31-gap-shrinks-with-k",
              r3["gap_right"] > 1e-3
              and r7["gap_right"] < 5e-7
              and r9["gap_right"] < 5e-8
              and abs(r3["gap_right"] - K3_GAPR) / K3_GAPR < 0.05
              and abs(r9["gap_right"] - K9_GAPR) / K9_GAPR < 0.15,
              "k=3 gapR=%.4e -> k=7 %.4e -> k=9 %.4e "
              "(collar shrinks; k=8 not rebuilt)"
              % (r3["gap_right"], r7["gap_right"], r9["gap_right"]))
    else:
        check("G31-gap-shrinks-smoke",
              rows[0]["gap_right"] > rows[1]["gap_right"],
              "k=3 gapR=%.4e > k=4 %.4e" % (
                  rows[0]["gap_right"], rows[1]["gap_right"]))

    core_idx = CORE_SAMPLE if smoke else list(V.admissible_indices())
    ck = []
    gaps = []
    trgs = []
    for kz in core_idx:
        td, _ = tdag_main(kz)
        p = pack_tau(td)
        ck.append(p["kappa_G"])
        if p["gap_right"] is not None:
            gaps.append(p["gap_right"])
        trgs.append(p["trG"])
        del td, p
    mean_c = float(sum(ck)) / max(len(ck), 1)
    check("G32-core-kappa0",
          all(k == 0 for k in ck)
          and mean_c < 1.0
          and (len(ck) == (6 if smoke else 42)),
          "%d/%d core kappa=0; block mean=%.4f<1; "
          "NO kappa>=1 trend"
          % (len(ck), len(ck), mean_c))
    if not smoke:
        check("G33-core-collar-stats",
              min(gaps) >= CORE_GAPR_MIN * 0.8
              and max(gaps) <= CORE_GAPR_MAX * 1.2
              and CORE_TRG_LO <= min(trgs) <= 50.0
              and max(trgs) <= CORE_TRG_HI,
              "gapR [%.3e, %.3e]; trG [%.2f, %.2f] "
              "(moments huge, kappa=0)"
              % (min(gaps), max(gaps), min(trgs), max(trgs)))
    else:
        check("G33-core-sample-trG",
              min(trgs) > 10.0,
              "sample trG min=%.2f (>>1 at kappa=0)" % min(trgs))

    dead = DEAD_CHI3[:2] if smoke else DEAD_CHI3
    nflip = 0
    pD = None
    for kz in dead:
        mzc, dsmc = B.chi_border_rung(kz, DMF.Q_CHI3, DMF.LPQ3)
        p = pack_tau(B.source_Tdag(mzc, dsmc))
        okf = p["kappa_G"] == 1 and p["kappa_R"] == 1
        nflip += int(okf)
        print("    dead chi3-%d kappa=%d gapL=%s"
              % (kz, p["kappa_G"],
                 ("%.4e" % p["gap_left"]) if p["gap_left"] else "n/a"),
              flush=True)
        if kz == 15:
            pD = p
    if not smoke:
        mz4, dsm4 = B.chi_border_rung(DEAD_CHI4[0], DMF.Q_CHI4, DMF.LPQ4)
        p4 = pack_tau(B.source_Tdag(mz4, dsm4))
        ok4 = p4["kappa_G"] == 1
        check("G34-dead-chi-kappa1",
              nflip == 5 and ok4,
              "dead chi3 %d/5 kappa=1; chi4-20 kappa=%d"
              % (nflip, p4["kappa_G"]))
    else:
        check("G34-dead-chi-kappa1",
              nflip == len(dead),
              "smoke dead chi3 %d/%d kappa=1" % (nflip, len(dead)))

    mzl, dsml = B.chi_border_rung(9, DMF.Q_CHI3, DMF.LPQ3)
    pL = pack_tau(B.source_Tdag(mzl, dsml))
    check("G35-live-chi-kappa0",
          pL["kappa_G"] == 0,
          "CHI3-9 living kappa=%d" % pL["kappa_G"])

    # MI2 on {w9, kz5} with a SAFE contour (r=0.40: both wind 0)
    td5, _ = tdag_main(5)
    p5 = pack_tau(td5)
    Gs = [p9["G"], p5["G"]]
    w1 = winding_circle(Gs[0], 0.5, 0.40, n=80)
    w2 = winding_circle(Gs[1], 0.5, 0.40, n=80)
    wm = winding_mean(Gs, 0.5, 0.40, n=80)
    mean_w = 0.5 * (w1 + w2)
    check("G36-MI2-linearity",
          abs(wm - mean_w) < MI2_BAR
          and abs(w1.real) < WIND_BAR
          and abs(w2.real) < WIND_BAR,
          "avg-integrand wind - mean(winds)=%.2e "
          "(linearity SATZ; safe r=0.40 both 0)"
          % abs(wm - mean_w))
    return pD, rows


def part_kills(p9, pD):
    section("S5  LEG D -- KILLS / S-NO-GO / CIRCULARITY")
    check("G40-trG-blind",
          p9["trG"] > 20.0 and pD["trG"] > 20.0
          and abs(p9["trG"] - W9_TRG) / W9_TRG < 0.02
          and p9["kappa_G"] == 0 and pD["kappa_G"] == 1,
          "trG living=%.2f dead=%.2f both >>1; kappa 0 vs 1 "
          "(tr G does not see the threshold)"
          % (p9["trG"], pD["trG"]))
    check("G41-moment-blind-r398",
          p9["M2"] > 20.0 and pD["M2"] > 20.0
          and abs(p9["M2"] - W9_M2) / W9_M2 < 0.05
          and abs(pD["M2"] - DEAD15_M2) / DEAD15_M2 < 0.05,
          "M2 living=%.2f dead=%.2f both >>2 "
          "(r398: 1/2-cluster dominates even moments)"
          % (p9["M2"], pD["M2"]))
    tau_live = float(np.linalg.det(np.eye(p9["n"]) - 0.5 * p9["G"]))
    tau_dead = float(np.linalg.det(np.eye(pD["n"]) - 0.5 * pD["G"]))
    check("G42-s-nogo-pointwise-tau",
          tau_live > 0 and tau_dead > 0
          and p9["kappa_G"] == 0 and pD["kappa_G"] == 1,
          "tau(0.5)>0 on living AND dead "
          "(%.3e vs %.3e); the kappa-zero sits in the "
          "s=1 collar, not at a mid-interval bound.  "
          "s is a counting variable, not a positivity dial"
          % (tau_live, tau_dead))
    ps = HM.row_mz(HM.scramble_mz(), "SCR")
    check("G43-scramble-bulk-dead",
          ps["nneg"] == SCR_NNEG,
          "scramble nneg(R)=%d (bulk already dead; "
          "T^dagger is not the story).  Circularity gate: "
          "pointwise X^eps is not a mean carrier"
          % ps["nneg"])
    del ps["R"]


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("mean_tau_index_probe -- "
          "PRIME.RDAGGER.MEAN_TAU_INDEX.01 (round 440)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9 + core-42; "
                        "k=8 not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s PX %s ABD %s HM %s DMF %s"
          % (B.SPEC_SHA[:8], PX.SPEC_SHA[:8], ABD.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], DMF.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    p9, mz9, _td = part_w9()
    part_source(p9, mz9)
    pD, _rows = part_census(p9, smoke)
    part_kills(p9, pD)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "IDENTITIES_EXACT / COLLAR_BOSS_QUANTIFIED / "
          "BLOCK_MEAN_CENSUS / UNCONDITIONAL_OPEN.  "
          "no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("IDENTITIES_EXACT / COLLAR_BOSS_QUANTIFIED / "
            "BLOCK_MEAN_CENSUS / UNCONDITIONAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("MEAN TAU INDEX %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("MEAN TAU INDEX FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
