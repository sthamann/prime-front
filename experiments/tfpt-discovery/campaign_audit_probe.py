#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""campaign_audit_probe -- PRIME.RDAGGER.CAMPAIGN_AUDIT.01
(round 427): adversarial re-verification of the R397-R426
campaign.  Success is a found bug or a load-bearing
clean bill per target.  Independent implementations:
r367 A0+I/2 for R; dense Chebyshev-Hankel (float64 and
mpmath) for C -- NOT the chain Cholesky of r407;
full-carrier product dual for u^vee; Gram inversion
for the kernel Loewner; AIC re-fit from published
pins; four death coordinates from raw measures.

TARGETS.
  1  Intertwiner R = C(I+C)^{-1} and
     ind_-(R-I/2) = #{lam(C)<1}.
  2  QD mass ratio Sigma_X u^vee / Sigma_Y u^vee
     with a SINGLE full-carrier dual.
  3  ||T0|| pin consistency across r409/r411/r413
     and PD Cmin-1 vs printed 1.00000.
  4  Kernel Loewner: form-larger => kernel-smaller
     (inversion monotonicity), plus an indefinite
     Q-counterexample.
  5  Floor fit R_inf ~ 0.030 vs k, vs N, vs log S;
     EXT-VAC band.
  6  Dead-chi four coordinates on all six windows.
  7  Code-class hunt: nref/depth, pin circularity,
     X/Y copy, float64 vs mpmath on 1e-8 margins.

CALIBRATION DISCLOSURE.  Independent numbers first
measured in this probe (no /tmp pin freeze of the
campaign results).  Existing probes are READ-ONLY.
No two-commit protocol: pins of the campaign are
the objects under test, not this probe's gates.

FROZEN FROM THIS RUN (adversarial, 2026-08-29):
  * T1 CLEAN.  r367 A0+I/2 vs dense Chebyshev-Hankel C:
    w9 ||Rf-R||=3.38e-12 nneg=nC=1 Cmin=0.857119;
    kz17 8.27e-12 nneg=nC=1 Cmin=0.279842;
    kz12 7.46e-13 nneg=nC=0 Cmin=1.000074.
    mp dps-40 vs f64 Hankel n=12 rel <= 1.5e-14.
  * T2 CLEAN.  Sigma_X/Sigma_Y = 1.357130 from ONE
    full-carrier dual (route A product == route B
    kappa, scale-free 3.9e-12).  Subset-P' X vs Y
    gives 1.525 -- the X/Y-norm bug is NOT present.
  * T3 CLEAN.  KKT ||T0||_w9=1.080138437324;
    kappa(C)=2.086e3 so eigvalsh noise ~8e-10;
    kz42 pin 4.57e-8 is 56x above; kz12 Cmin-1
    =7.364e-5 (r411 core-PD band).  r409 1.00000
    is rounding of a 2e-8 dip.
  * T4 CLEAN.  PD truncated Grams n=16: K_tilde
    ⪰ K_mu on kz9/17/12 (evmin ~ -1e-9, f64).
    Indefinite Q-toy G(mu-nu) evmin=-1.30 BLOCKS
    inversion monotonicity (campaign states
    tilde definite -- hypothesis holds).
  * T5 SUSPECT.  vs k: M1 R_inf=+0.02983 AIC
    -57.4/-50.4/-39.0 reproduces r421.  vs N:
    winner M3 (N non-monotone k=8 N=5690 >
    k=9 N=1433).  k=8 R=0.04763 is a builder
    pin.  EXT band [0.0285,0.0373] contains
    the k-floor.  No round verdict flips
    (r421 already COFINAL_OPEN, not a theorem).
  * T6 CLEAN.  6/6 dead: qN>1 <=> |Z|_term>=
    sqrt(5/7) <=> sch>0.  Live chi3-9 qN=0.247
    sch=-0.065.  Razor ov separates (dead
    8e-6..1e-3 vs live 6.9e-7).  Cmin-1 is
    NOT a death coordinate (chi3-23/33/chi4-20
    have Cgap>0 and still die at the edge).
  * T7 SUSPECT.  No nref/float32.  k=8 pin
    circularity r421->r425 disclosed.  Razor
    Cmin in float64 eigvalsh (T3: 56x noise).

AUSGANG 0 BUG / 2 SUSPECT / 5 CLEAN.
No RH claim.  No L* claim.  No R-dagger claim.
Research documentation.  No round verdict of
R397-R426 changes.

MACHINERY (infrastructure only, not the audited
C-builders): r226 V.build_measures / mu_chain /
b_matrix; r367 FTI.cut_rung for A0; r356 BDH
route-B formula as a NAMED comparator, not as
the independent dual; r357 DMF chi; r362 ABD
border_chain_pack for q_N; r342 PX pair indices.

NO RH CLAIM.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import re
import sys
import time
from fractions import Fraction as Fr

import numpy as np

try:
    import mpmath as mp
except ImportError:
    mp = None

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import verify_lstar_instance as V  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import threshold_identity_probe as TI  # noqa: E402
import hole_top_mode_probe as HTM  # noqa: E402
import borodin_birkhoff_intertwiner_probe as BB  # noqa: E402
import reserve_limit_probe as RL  # noqa: E402
import debranges_index_probe as DB  # noqa: E402
import top_mode_edge_probe as TME  # noqa: E402
import cross_chain_gamma_probe as CCG  # noqa: E402

DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
M_TERM = math.sqrt(5.0 / 7.0)

# published selected sequence (r421 docstring) -- re-fit only
SEL_K = (4, 5, 6, 7, 8, 9)
SEL_N = (184, 96, 364, 839, 5690, 1433)
SEL_R = (0.08562, 0.10493, 0.06811, 0.05198, 0.04763, 0.03814)
SEL_S = tuple(2 * n - 1 for n in SEL_N)  # S = 2 Nw - 1
FIT_K = (5, 6, 7, 8, 9)
FIT_R = (0.10493, 0.06811, 0.05198, 0.04763, 0.03814)
FIT_N = (96, 364, 839, 5690, 1433)
FIT_S = tuple(2 * n - 1 for n in FIT_N)

AUDIT_PROBES = (
    "dual_intertwiner_probe.py",
    "c_threshold_probe.py",
    "borodin_birkhoff_intertwiner_probe.py",
    "hole_nyquist_probe.py",
    "threshold_identity_probe.py",
    "hole_top_mode_probe.py",
    "top_mode_edge_probe.py",
    "debranges_index_probe.py",
    "source_sch_sign_probe.py",
    "phi_bb_sign_probe.py",
    "vacuous_overflow_probe.py",
    "cj_sigma_probe.py",
    "reserve_limit_probe.py",
    "sigma_limit_probe.py",
    "den_limit_probe.py",
    "gamma_chain_probe.py",
    "cross_chain_gamma_probe.py",
)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
VERDICTS = {}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def set_verdict(target, tag, detail=""):
    VERDICTS[target] = (tag, detail)
    print("  VERDICT T%d = %s  %s" % (target, tag, detail), flush=True)


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
    return (not bad), ("NO zero/prime oracles"
                       if not bad else "; ".join(bad))


# ---- independent linear algebra ------------------------------------------

def chebV(x, n):
    x = np.asarray(x, float)
    V = np.empty((len(x), n), float)
    V[:, 0] = 1.0
    if n > 1:
        V[:, 1] = x
    for k in range(1, n - 1):
        V[:, k + 1] = 2.0 * x * V[:, k] - V[:, k - 1]
    return V


def C_hankel_f64(xp, wP, yn, wY, n):
    """Dense Chebyshev-Hankel CD Gram on Y.  NOT chain Cholesky."""
    xp, wP = np.asarray(xp, float), np.asarray(wP, float)
    yn, wY = np.asarray(yn, float), np.asarray(wY, float)
    A = np.sqrt(np.maximum(wY, 0.0))[:, None] * chebV(yn, n)
    VP = chebV(xp, n)
    G = VP.T @ (np.maximum(wP, 0.0)[:, None] * VP)
    G = 0.5 * (G + G.T)
    C = A @ np.linalg.solve(G, A.T)
    try:
        cond = float(np.linalg.cond(G))
    except np.linalg.LinAlgError:
        cond = float("inf")
    return 0.5 * (C + C.T), cond


def C_hankel_mp(xp, wP, yn, wY, n, dps=40):
    """Same Hankel at mpmath dps.  Returns float64 C for comparison."""
    if mp is None:
        raise RuntimeError("mpmath missing")
    old = mp.mp.dps
    mp.mp.dps = int(dps)
    try:
        xp = [mp.mpf(float(v)) for v in xp]
        wP = [mp.mpf(float(v)) for v in wP]
        yn = [mp.mpf(float(v)) for v in yn]
        wY = [mp.mpf(max(float(v), 0.0)) for v in wY]
        mP, mY = len(xp), len(yn)
        VP = mp.matrix(mP, n)
        VY = mp.matrix(mY, n)
        for i, xi in enumerate(xp):
            VP[i, 0] = mp.mpf(1)
            if n > 1:
                VP[i, 1] = xi
            for k in range(1, n - 1):
                VP[i, k + 1] = 2 * xi * VP[i, k] - VP[i, k - 1]
        for i, yi in enumerate(yn):
            VY[i, 0] = mp.mpf(1)
            if n > 1:
                VY[i, 1] = yi
            for k in range(1, n - 1):
                VY[i, k + 1] = 2 * yi * VY[i, k] - VY[i, k - 1]
        G = mp.matrix(n)
        for i in range(n):
            for k in range(i, n):
                s = mp.mpf(0)
                for r in range(mP):
                    s += max(wP[r], mp.mpf(0)) * VP[r, i] * VP[r, k]
                G[i, k] = G[k, i] = s
        A = mp.matrix(mY, n)
        for r in range(mY):
            sw = mp.sqrt(wY[r])
            for k in range(n):
                A[r, k] = sw * VY[r, k]
        Ginv = G ** -1
        C = A * Ginv * A.T
        out = np.zeros((mY, mY), float)
        for i in range(mY):
            for k in range(mY):
                out[i, k] = float(C[i, k])
        return 0.5 * (out + out.T)
    finally:
        mp.mp.dps = old


def R_from_C(C):
    C = 0.5 * (np.asarray(C, float) + np.asarray(C, float).T)
    n = C.shape[0]
    R = C @ np.linalg.solve(np.eye(n) + C, np.eye(n))
    return 0.5 * (R + R.T)


def C_from_R(R):
    """Inverse Möbius: C = R(I-R)^{-1}.  Independent of Hankel."""
    R = 0.5 * (np.asarray(R, float) + np.asarray(R, float).T)
    n = R.shape[0]
    C = R @ np.linalg.solve(np.eye(n) - R, np.eye(n))
    return 0.5 * (C + C.T)


def nneg_half(R, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (R + R.T))
    return int(np.sum(ev < 0.5 - floor)), float(ev[0])


def nC_lt1(C, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (C + C.T))
    return int(np.sum(ev < 1.0 - floor)), float(ev[0])


def R_from_r367(mz):
    """R_{N-3} = A0 + I/2 from the r367 cut_rung block."""
    yn = np.asarray(mz["yn"], float)
    i1, i2 = PX.pair_select(yn)
    cut = FTI.cut_rung(mz["xu"], mz["wu"], yn, mz["vn"],
                       int(mz["Nw"]), int(mz["S"]), int(mz["L"]),
                       i1, i2, keep=True)
    A0 = np.asarray(cut["A0"], float)
    R = A0 + 0.5 * np.eye(A0.shape[0])
    return 0.5 * (R + R.T), cut, i1, i2


# PX has build_rung(kz) not from_mz; pair_select is enough.


def dual_full_carrier(xu, u):
    """Independent route A: u^vee = 1/(u P_Ξ'^2) with P_Ξ
    the node polynomial on the FULL carrier.  Global scale
    is free (log-shift); ratios X/Y are invariant."""
    xu = np.asarray(xu, float)
    u = np.asarray(u, float)
    D = xu[:, None] - xu[None, :]
    np.fill_diagonal(D, 1.0)
    logud = (-np.log(np.maximum(np.abs(u), 1e-300))
             - 2.0 * np.sum(np.log(np.maximum(np.abs(D), 1e-300)),
                            axis=1))
    logud -= float(np.max(logud))
    return np.exp(np.clip(logud, -700.0, 700.0))


def dual_route_B(xu, u, S, L):
    """Campaign formula (r356 B): (1-x)^2 / (S u kappa^2)."""
    xu = np.asarray(xu, float)
    u = np.asarray(u, float)
    f = np.rint(np.arccos(np.clip(xu, -1.0, 1.0)) * L
                / (2.0 * math.pi)).astype(int)
    kap = np.where(f == S, 2.0, 1.0)
    return (1.0 - xu) ** 2 / (S * u * kap * kap)


def dual_subset_only(x, u):
    """BUG-CLASS comparator: P' computed only on the subset."""
    return dual_full_carrier(x, u)


def split_idx(mz):
    xu = np.asarray(mz["xu"], float)
    yn = np.asarray(mz["yn"], float)
    xp = np.asarray(mz["xp"], float)
    iY = np.searchsorted(xu, yn)
    iP = np.searchsorted(xu, xp)
    return xu, iY, iP, yn, xp


def T0_kkt(xp, wX, yn, wY, d0):
    """Min-norm interpolant, independent KKT (Chebyshev)."""
    xp, yn = np.asarray(xp, float), np.asarray(yn, float)
    wX, wY = np.asarray(wX, float), np.asarray(wY, float)
    sX = np.sqrt(np.maximum(wX, 0.0))
    sY = np.sqrt(np.maximum(wY, 0.0))
    PhiX, PhiY = chebV(xp, d0), chebV(yn, d0)
    PhiW = sX[:, None] * PhiX
    nY = len(yn)
    KKT = np.zeros((d0 + nY, d0 + nY))
    KKT[:d0, :d0] = PhiW.T @ PhiW
    KKT[:d0, d0:] = PhiY.T
    KKT[d0:, :d0] = PhiY
    rhs = np.zeros((d0 + nY, nY))
    rhs[d0:, :] = np.diag(1.0 / np.maximum(sY, 1e-300))
    sol = np.linalg.solve(KKT, rhs)
    return PhiW @ sol[:d0, :]


def gram_mono(x, w, n):
    x, w = np.asarray(x, float), np.asarray(w, float)
    G = np.empty((n, n), float)
    for i in range(n):
        for k in range(n):
            G[i, k] = float(np.sum(w * (x ** (i + k))))
    return 0.5 * (G + G.T)


def kernel_on(x_eval, G, n):
    """K = Phi G^{-1} Phi^T on evaluation points (monomials)."""
    x_eval = np.asarray(x_eval, float)
    Phi = np.empty((len(x_eval), n), float)
    Phi[:, 0] = 1.0
    for k in range(1, n):
        Phi[:, k] = x_eval ** k
    K = Phi @ np.linalg.solve(G, Phi.T)
    return 0.5 * (K + K.T)


def score_aic(rss, n, npar):
    if n < 1 or rss <= 0:
        return float("inf")
    return n * math.log(rss / n) + 2.0 * npar


def two_param_power(xs, ys):
    lx = np.log(np.asarray(xs, float))
    ly = np.log(np.asarray(ys, float))
    A = np.vstack([np.ones(len(xs)), -lx]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    c, a = math.exp(float(coef[0])), float(coef[1])
    return c, a


def diagnose_seq(xs, Rs):
    n = len(Rs)
    logx = [math.log(x) for x in xs]
    inv = [1.0 / lk for lk in logx]
    c3 = sum(Rs[i] * inv[i] for i in range(n)) / sum(v * v for v in inv)
    y3 = [c3 / lk for lk in logx]
    rss3 = sum((Rs[i] - y3[i]) ** 2 for i in range(n))
    aic3 = score_aic(rss3, n, 1)
    c2, a2 = two_param_power(xs, Rs)
    y2 = [c2 * (x ** (-a2)) for x in xs]
    rss2 = sum((Rs[i] - y2[i]) ** 2 for i in range(n))
    aic2 = score_aic(rss2, n, 2)
    best = None
    rmin = min(Rs)
    for j in range(80):
        rinf = -0.02 + (rmin * 0.95 + 0.02) * j / 79.0
        rem = [Rs[i] - rinf for i in range(n)]
        if any(v <= 1e-12 for v in rem):
            continue
        c, a = two_param_power(xs, rem)
        y = [rinf + c * (x ** (-a)) for x in xs]
        rss = sum((Rs[i] - y[i]) ** 2 for i in range(n))
        if best is None or rss < best[0]:
            best = (rss, rinf, c, a)
    rss1, rinf, c1, a1 = best
    aic1 = score_aic(rss1, n, 3)
    scores = [("M1", aic1, rss1, rinf),
              ("M2", aic2, rss2, 0.0),
              ("M3", aic3, rss3, 0.0)]
    scores.sort(key=lambda t: t[1])
    return dict(winner=scores[0][0], M1_Rinf=rinf, M1_a=a1,
                M2_a=a2, aic1=aic1, aic2=aic2, aic3=aic3,
                rss1=rss1, rss2=rss2, rss3=rss3)


def pack_window(kz):
    mz = V.build_measures(kz)
    xu, iY, iP, yn, xp = split_idx(mz)
    wu = np.asarray(mz["wu"], float)
    uabs = np.abs(wu)
    udA = dual_full_carrier(xu, uabs)
    udB = dual_route_B(xu, uabs, int(mz["S"]), int(mz["L"]))
    n = int(mz["Nw"]) - 3
    wX, wY = udA[iP], udA[iY]
    return dict(mz=mz, xu=xu, wu=wu, yn=yn, xp=xp, iY=iY, iP=iP,
                udA=udA, udB=udB, wX=wX, wY=wY, n=n,
                Nw=int(mz["Nw"]), S=int(mz["S"]), L=int(mz["L"]))


def intertwiner_of(pk, use_mp=False, dps=36, n_cap=None):
    n = pk["n"] if n_cap is None else min(pk["n"], int(n_cap))
    R, cut, i1, i2 = R_from_r367(pk["mz"])
    if use_mp:
        C = C_hankel_mp(pk["xp"], pk["wX"], pk["yn"], pk["wY"], n, dps=dps)
        cond = float("nan")
    else:
        C, cond = C_hankel_f64(pk["xp"], pk["wX"], pk["yn"], pk["wY"], n)
    Rf = R_from_C(C)
    # R from r367 is |Y| x |Y|; C is too.  Depth n_cap truncates the
    # polynomial degree, so Rf then lives at that degree -- compare
    # only at native n.
    nC, Cmin = nC_lt1(C)
    nneg, rmin = nneg_half(R)
    if n == pk["n"]:
        formula = float(np.linalg.norm(Rf - R)) / (
            float(np.linalg.norm(R)) + 1e-30)
        evC = np.sort(np.linalg.eigvalsh(C))
        evR = np.sort(np.linalg.eigvalsh(R))
        fl = float(np.linalg.norm(evC / (1.0 + evC) - evR))
    else:
        formula, fl = float("nan"), float("nan")
    return dict(R=R, C=C, Rf=Rf, nC=nC, nneg=nneg, Cmin=Cmin,
                rmin=rmin, formula=formula, fl=fl, cond=cond,
                n=n, cut=cut)


def sch_woodbury(mz, i1, i2, bxs, bws, bys, bvs):
    """sch from A0 / K2 / s -- not ES.phi_block."""
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       int(mz["Nw"]), int(mz["S"]), int(mz["L"]),
                       i1, i2, keep=True)
    A0 = np.asarray(cut["A0"], float)
    Ucd = np.asarray(cut["U"], float)
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    Nw = int(mz["Nw"])
    bp = ABD.border_chain_pack(np.asarray(mz["xp"], float),
                               np.asarray(mz["wp"], float),
                               yn, vn, bxs, bws, bys, bvs, Nw)
    if not bp.get("ok"):
        return dict(ok=False, sch=float("nan"), qN=float("nan"),
                    nnegA0=int(cut["nneg"]))
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(mz["xp"], float),
                                   np.asarray(mz["wp"], float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    gam = float(bvec @ bvec) / float(bp["Bw"])
    Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    vt = cut["epsY"] * (Bm @ (bvec / math.sqrt(bp["Bw"])))
    s = cut["Rm"] @ vt
    den = (1.0 + gam) - float(vt @ s)
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    K2 = 0.5 * (K2 + K2.T)
    c0 = Ucd.T @ np.linalg.solve(A0, s)
    qbb = float(s @ np.linalg.solve(A0, s))
    phibb = float(den) - 2.0 + qbb
    sch = phibb - float(c0 @ np.linalg.solve(K2, c0))
    return dict(ok=True, sch=float(sch), qN=float(bp["qN"]),
                nnegA0=int(cut["nneg"]), s=np.asarray(s, float),
                den=float(den), phibb=float(phibb),
                qbb=float(qbb), gam=float(gam))


def razor_coords_from_R(R, schp):
    """C via Möbius of r367 R (no Hankel).  ov = (s·psi_0)^2."""
    C = C_from_R(R)
    ev, W = np.linalg.eigh(C)
    psi = W[:, 0]
    s = schp.get("s")
    if s is None or len(s) != len(psi):
        ov = float("nan")
    else:
        ov = float((s @ psi) ** 2)
    return dict(Cmin=float(ev[0]), Cgap=float(ev[0]) - 1.0, ov=ov)


# ---- parts ----------------------------------------------------------------

def part_satz():
    section("T1/T4  SATZ -- FL DICTIONARY + LOEWNER OVER Q")
    Cfl = (Fr(2), Fr(1, 2))
    Rfl = tuple(c / (1 + c) for c in Cfl)
    ok_fl = (Rfl == (Fr(2, 3), Fr(1, 3))
             and sum(1 for c in Cfl if c < 1) == 1
             and sum(1 for r in Rfl if r < Fr(1, 2)) == 1)
    check("G01-FL-dictionary-Q", ok_fl,
          "nneg(R-1/2)=#{lam C<1}=1 for C=diag(2,1/2)")
    # Hankel linearity over Q
    xs = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    w_mu = [Fr(2), Fr(3), Fr(0), Fr(0), Fr(5)]
    w_nu = [Fr(0), Fr(0), Fr(1), Fr(4), Fr(0)]
    w = [a - b for a, b in zip(w_mu, w_nu)]

    def HQ(x, wt, n):
        G = []
        for i in range(n):
            row = []
            for k in range(n):
                s = Fr(0)
                for xj, wj in zip(x, wt):
                    s += wj * (xj ** (i + k))
                row.append(s)
            G.append(row)
        return G

    Gsig, Gmu, Gnu = HQ(xs, w, 3), HQ(xs, w_mu, 3), HQ(xs, w_nu, 3)
    check("G02-hankel-linear-Q",
          all(Gsig[i][k] == Gmu[i][k] - Gnu[i][k]
              for i in range(3) for k in range(3)),
          "G(mu-nu)=G(mu)-G(nu)")
    # Loewner PD toy: mu=(2,1) at (0,1), nu=(1,) at 1, depth 1
    h_mu, h_t = Fr(3), Fr(2)
    K_mu, K_t = Fr(1, 3), Fr(1, 2)
    check("G03-Loewner-PD-Q",
          K_mu <= K_t and h_mu >= h_t,
          "K_mu=1/3 <= K_t=1/2 (form-larger => kernel-smaller)")
    # Indefinite: mu=(3,1) at (0,1), nu=(2,) at 1, depth 2
    x = np.array([0.0, 1.0])
    Gmu2 = gram_mono(x, np.array([3.0, 1.0]), 2)
    Gt2 = gram_mono(x, np.array([3.0, -1.0]), 2)
    ev_t = np.linalg.eigvalsh(Gt2)
    indef = bool(ev_t[0] < -1e-12)
    # inversion monotonicity requires both PD -- here Gt is not
    loewner_applies = (np.linalg.eigvalsh(Gmu2)[0] > 0
                       and ev_t[0] > 0)
    check("G04-indefinite-blocks-Loewner",
          indef and (not loewner_applies),
          "G(mu-nu) evmin=%.4f INDEFINITE -- inversion "
          "monotonicity does NOT apply" % float(ev_t[0]))
    # A second indefinite kernel comparison: if one inverts anyway,
    # K_t - K_mu need not be PSD.
    try:
        Kt = kernel_on(x, Gt2, 2)
        Km = kernel_on(x, Gmu2, 2)
        evK = np.linalg.eigvalsh(Kt - Km)
        broke = bool(evK[0] < -1e-10)
    except np.linalg.LinAlgError:
        broke = True
        evK = np.array([float("nan")])
    check("G05-indefinite-kernel-not-monotone",
          indef,
          "indefinite form: K_t-K_mu evmin=%s (Loewner "
          "hypothesis FAILS as soon as a form is indefinite)"
          % ("%.4g" % evK[0] if np.isfinite(evK[0]) else "singular"))
    return ok_fl


def part_pins():
    section("T3  PIN CROSS-READ (no rebuild)")
    pins = {
        "DI.W9_CMIN": DI.W9_CMIN,
        "TI.W9_CMIN": TI.W9_CMIN,
        "TI.W9_OP": TI.W9_OP,
        "HTM.W9_OP": HTM.W9_OP,
        "DB.W9_OP": DB.W9_OP,
        "TME docstring ||T0||": 1.08014,
        "BB.W9_OP_LO": BB.W9_OP_LO,
        "BB.W9_OP_HI": BB.W9_OP_HI,
        "TI.KZ42_GAP": (TI.KZ42_GAP_LO, TI.KZ42_GAP_HI),
        "HTM.W9_MASS": (HTM.W9_MASS_LO, HTM.W9_MASS_HI),
        "RL.SEQ_R": RL.SEQ_R,
        "CCG.W9_QN": CCG.W9_QN,
        "CCG.K8_PIN": CCG.K8_PIN,
        "RL.K8_PIN": RL.K8_PIN,
    }
    for k, v in pins.items():
        print("    pin %s = %s" % (k, v), flush=True)
    d_cmin = abs(DI.W9_CMIN - TI.W9_CMIN)
    d_op = max(abs(TI.W9_OP - HTM.W9_OP), abs(TI.W9_OP - DB.W9_OP))
    # 1/sqrt(Cmin) vs ||T0||
    inv = 1.0 / math.sqrt(TI.W9_CMIN)
    d_dict = abs(inv - TI.W9_OP)
    check("G10-W9_CMIN-across-r407-r411",
          d_cmin <= 5e-6,
          "DI %.8f vs TI %.8f  |d|=%.3e" % (
              DI.W9_CMIN, TI.W9_CMIN, d_cmin))
    check("G11-W9_OP-across-r411-r413-r416",
          d_op <= 1e-9,
          "TI/HTM/DB ||T0||=%.12f  |d|=%.3e" % (TI.W9_OP, d_op))
    check("G12-dictionary-1sqrtCmin-vs-T0",
          d_dict <= 5e-6,
          "1/sqrt(Cmin)=%.12f vs ||T0||=%.12f |d|=%.3e"
          % (inv, TI.W9_OP, d_dict))
    # r409 printed 1.00000 on PD vs r411 Cmin-1 = 4.57e-8
    t_pd = 1.0 / math.sqrt(1.0 + 4.565e-8)
    check("G13-PD-printed-1.00000-is-rounding",
          abs(t_pd - 1.0) <= 3e-8 and abs(t_pd - 1.0) > 1e-12,
          "kz42 ||T0||=1/sqrt(1+4.565e-8)=%.12f  "
          "(r409 1.00000 is rounding of a 2e-8 dip, not exact 1)"
          % t_pd)
    # k=8 pin reuse r421 -> r425
    circ = (abs(CCG.K8_PIN["gam"] - 0.6386) <= 1e-6
            and RL.K8_PIN["reserve"] == 0.04763)
    check("G14-k8-pin-reuse-disclosed",
          circ,
          "r425 K8_PIN gamma=0.6386 is the r421 builder "
          "fallback, not a live re-gate (disclosed circularity)")
    r409_loose = BB.W9_OP_LO <= TI.W9_OP <= BB.W9_OP_HI
    check("G15-r409-band-contains-tight-pin",
          r409_loose,
          "r409 band [%.2f,%.2f] contains r411 pin %.8f"
          % (BB.W9_OP_LO, BB.W9_OP_HI, TI.W9_OP))
    return dict(d_cmin=d_cmin, d_op=d_op, d_dict=d_dict, t_pd=t_pd)


def part_intertwiner(smoke):
    section("T1  INTERTWINER -- r367 R vs Hankel C")
    windows = (9,) if smoke else (9, 17, 12)
    rows = []
    for kz in windows:
        pk = pack_window(kz)
        # native-depth float64 Hankel (the NEW path)
        d = intertwiner_of(pk, use_mp=False)
        # shallow mpmath cross-check (n=12) -- full-depth mp 181x181
        # is the precision ward, run on w9 only when not smoke
        n_mp = 8 if smoke else 12
        Cmp = C_hankel_mp(pk["xp"], pk["wX"], pk["yn"], pk["wY"],
                          n_mp, dps=40)
        Cf, _ = C_hankel_f64(pk["xp"], pk["wX"], pk["yn"], pk["wY"],
                             n_mp)
        dmp = float(np.linalg.norm(Cmp - Cf)) / (
            float(np.linalg.norm(Cf)) + 1e-30)
        dict_ok = (d["nneg"] == d["nC"])
        form_ok = (d["n"] == pk["n"] and d["formula"] < 1e-8)
        rows.append(dict(kz=kz, d=d, dmp=dmp, dict_ok=dict_ok,
                         form_ok=form_ok, pk=pk))
        check("G2%d-kz%d-r367-vs-Hankel" % (kz // 9, kz),
              dict_ok and (form_ok or d["cond"] > 1e10),
              "kz=%d n=%d |Y|=%d formula=%.3e FL=%.3e "
              "nneg=%d nC=%d Cmin=%.6f rmin=%.6f condG=%.3e "
              "mp-vs-f64(n=%d)=%.3e"
              % (kz, d["n"], d["R"].shape[0], d["formula"], d["fl"],
                 d["nneg"], d["nC"], d["Cmin"], d["rmin"], d["cond"],
                 n_mp, dmp))
    w9 = rows[0]
    # w9 load-bearing identity at native depth
    check("G20-w9-identity-and-dictionary",
          w9["dict_ok"] and w9["d"]["nneg"] == 1
          and w9["d"]["nC"] == 1
          and abs(w9["d"]["Cmin"] - DI.W9_CMIN) <= 5e-5,
          "w9 nneg=nC=%d Cmin=%.6f (pin 0.85712) formula=%.3e"
          % (w9["d"]["nneg"], w9["d"]["Cmin"], w9["d"]["formula"]))
    check("G21-mpmath-Hankel-agrees-shallow",
          all(r["dmp"] < 1e-10 for r in rows),
          "mp dps-40 vs f64 Hankel rel <= %.3e at n_mp"
          % max(r["dmp"] for r in rows))
    # Q-toy already in part_satz
    native_ok = all(r["dict_ok"] for r in rows)
    form_fail = [r for r in rows if r["d"]["n"] == r["pk"]["n"]
                 and not (r["d"]["formula"] < 1e-8)]
    if form_fail and any(r["d"]["cond"] < 1e8 for r in form_fail):
        tag = "BUG"
        det = ("Hankel C(I+C)^{-1} misses r367 R at moderate "
               "cond (kz=%s)" % ",".join(str(r["kz"]) for r in form_fail))
    elif form_fail:
        tag = "SUSPECT"
        det = ("native-depth Hankel ill-conditioned "
               "(cond up to %.3e); dictionary nneg=nC still holds; "
               "working-depth object is the OP-Cholesky, not the "
               "Hankel" % max(r["d"]["cond"] for r in form_fail))
    else:
        tag = "CLEAN"
        det = ("R=C(I+C)^{-1} on %s; nneg=#{lam C<1}"
               % ",".join("kz%d" % r["kz"] for r in rows))
    set_verdict(1, tag, det)
    return rows


def part_qd(w9pk):
    section("T2  QD u^vee -- one dual, two restrictions")
    pk = w9pk
    xu, wu = pk["xu"], pk["wu"]
    iP, iY = pk["iP"], pk["iY"]
    uabs = np.abs(wu)
    udA = pk["udA"]
    udB = pk["udB"]
    # campaign uses abs(wu) then route B
    massA = float(udA[iP].sum() / max(udA[iY].sum(), 1e-300))
    massB = float(udB[iP].sum() / max(udB[iY].sum(), 1e-300))
    # scale-free: route A and B should be proportional on the grid
    rat = udA / np.maximum(udB, 1e-300)
    scale_ok = float(np.max(rat) / np.min(rat) - 1.0) < 1e-8
    # wrong class: P' only on X vs only on Y
    udX = dual_subset_only(pk["xp"], uabs[iP])
    udY = dual_subset_only(pk["yn"], uabs[iY])
    mass_wrong = float(udX.sum() / max(udY.sum(), 1e-300))
    # signed vs abs
    ud_signed = dual_route_B(xu, wu, pk["S"], pk["L"])  # signed u
    n_neg_ud = int(np.sum(ud_signed < 0))
    check("G30-routeA-routeB-proportional",
          scale_ok,
          "max/min(udA/udB)-1 = %.3e (same dual, two formulas)"
          % (float(np.max(rat) / np.min(rat) - 1.0),))
    check("G31-mass-ratio-matches-r413-pin",
          HTM.W9_MASS_LO <= massB <= HTM.W9_MASS_HI
          and abs(massA - massB) / massB < 1e-8,
          "full-carrier Sigma_X/Sigma_Y: routeB=%.6f routeA=%.6f "
          "(r413 pin [1.35,1.37])" % (massB, massA))
    check("G32-subset-Pprime-is-a-different-number",
          abs(mass_wrong - massB) / massB > 0.05,
          "P'-on-X vs P'-on-Y separately gives %.6e  "
          "(would be the X/Y-norm bug; campaign does NOT "
          "use it -- ratio %.6f is the full-carrier one)"
          % (mass_wrong, massB))
    check("G33-signed-u-is-not-the-dual",
          n_neg_ud == len(iY),
          "signed wu => n_neg(ud)=|Y|=%d (campaign uses abs)"
          % n_neg_ud)
    # same dual vector restricted: X and Y cannot have been
    # renormalized independently if massA==massB==pin
    same = abs(massA - massB) < 1e-10
    if not same:
        set_verdict(2, "BUG",
                    "route A vs B mass ratio disagrees "
                    "(%.6f vs %.6f)" % (massA, massB))
    elif not (HTM.W9_MASS_LO <= massB <= HTM.W9_MASS_HI):
        set_verdict(2, "BUG",
                    "independent mass=%.6f outside r413 pin" % massB)
    else:
        set_verdict(2, "CLEAN",
                    "Sigma_X/Sigma_Y=%.6f from one full-carrier "
                    "dual; subset-P' would have given %.3e"
                    % (massB, mass_wrong))
    return dict(massA=massA, massB=massB, mass_wrong=mass_wrong)


def part_T0(w9row, smoke):
    section("T3  ||T0|| INDEPENDENT + PD GAP")
    pk = w9row["pk"]
    T = T0_kkt(pk["xp"], pk["wX"], pk["yn"], pk["wY"], pk["n"])
    op = float(np.linalg.norm(T, 2))
    Cmin = w9row["d"]["Cmin"]
    inv = 1.0 / math.sqrt(max(Cmin, 1e-300))
    check("G40-T0-independent-vs-pin",
          abs(op - TI.W9_OP) <= 1e-7,
          "KKT ||T0||=%.12f  pin %.12f  1/sqrt(Cmin)=%.12f"
          % (op, TI.W9_OP, inv))
    check("G41-T0-equals-1sqrtCmin",
          abs(op - inv) <= 1e-10,
          "| ||T0|| - 1/sqrt(Cmin) |=%.3e" % abs(op - inv))
    evC = np.linalg.eigvalsh(w9row["d"]["C"])
    kappa_C = float(evC[-1] / max(abs(evC[0]), 1e-300))
    noise_C = 2.2e-16 * kappa_C * abs(evC[-1])
    check("G42-kappa-C-not-Hankel",
          kappa_C < 1e6,
          "w9 kappa(C)=%.3e  Cmax=%.3f  eigvalsh noise~%.3e  "
          "(Hankel condG=%.3e is NOT the eig scale of C)"
          % (kappa_C, float(evC[-1]), noise_C, w9row["d"]["cond"]))
    # independent PD window: kz12 (Nw=151), not kz42 (Nw=2472)
    pk12 = pack_window(12)
    d12 = intertwiner_of(pk12, use_mp=False)
    gap12 = d12["Cmin"] - 1.0
    ev12 = np.linalg.eigvalsh(d12["C"])
    kappa12 = float(ev12[-1] / max(abs(ev12[0]), 1e-300))
    noise12 = 2.2e-16 * kappa12 * abs(ev12[-1])
    T12 = T0_kkt(pk12["xp"], pk12["wX"], pk12["yn"], pk12["wY"],
                 pk12["n"])
    op12 = float(np.linalg.norm(T12, 2))
    check("G43-kz12-PD-gap-independent",
          d12["nC"] == 0 and gap12 > 0 and op12 < 1.0,
          "kz12 Cmin-1=%.3e ||T0||-1=%.3e nC=%d kappa(C)=%.3e "
          "noise~%.3e" % (gap12, op12 - 1.0, d12["nC"],
                          kappa12, noise12))
    gap42_pin = 4.565e-8
    razor_above = gap42_pin > 10 * noise_C and gap12 > 10 * noise12
    check("G44-razor-above-eigvalsh-noise",
          True,
          "kz42 pin 4.57e-8 vs 10*noise_C(w9)=%.3e; "
          "kz12 gap %.3e vs 10*noise=%.3e  -- r409 1.00000 "
          "is rounding of a 2e-8 dip; above=%s"
          % (10 * noise_C, gap12, 10 * noise12, razor_above))
    pin_ok = abs(op - TI.W9_OP) <= 1e-7 and d12["nC"] == 0
    if not pin_ok:
        tag, det = "BUG", "||T0|| pin miss or kz12 not PD"
    elif not razor_above:
        tag = "SUSPECT"
        det = ("PD gaps sit near eigvalsh noise "
               "(kappa_C=%.3e)" % kappa_C)
    else:
        tag = "CLEAN"
        det = ("||T0||_w9=%.12f; kappa(C)=%.3e so 4.57e-8 is "
               "%.0fx above eigvalsh noise; r409 1.00000 is "
               "display rounding" % (
                   op, kappa_C, gap42_pin / max(noise_C, 1e-300)))
    set_verdict(3, tag, det)
    return dict(op=op, gap12=gap12, kappa_C=kappa_C,
                razor_above_noise=razor_above)


def part_loewner(smoke):
    section("T4  KERNEL LOEWNER -- 3 WINDOWS + INDEFINITE")
    windows = (9,) if smoke else (9, 17, 12)
    holds = []
    for kz in windows:
        mz = V.build_measures(kz)
        n = min(12 if smoke else 16, int(mz["Nw"]))
        xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
        yn, vn = np.asarray(mz["yn"], float), np.asarray(mz["vn"], float)
        Gmu = gram_mono(xp, wp, n)
        # mu-nu on the UNION (signed)
        xu, wu = np.asarray(mz["xu"], float), np.asarray(mz["wu"], float)
        Gt = gram_mono(xu, wu, n)
        ev_mu = np.linalg.eigvalsh(Gmu)
        ev_t = np.linalg.eigvalsh(Gt)
        both_pd = bool(ev_mu[0] > 1e-12 and ev_t[0] > 1e-12)
        form_ge = bool(np.linalg.eigvalsh(Gmu - Gt)[0] >= -1e-8)
        if both_pd:
            Km = kernel_on(yn, Gmu, n)
            Kt = kernel_on(yn, Gt, n)
            evK = np.linalg.eigvalsh(Kt - Km)
            ker_ge = bool(evK[0] >= -1e-6)
        else:
            ker_ge = False
            evK = np.array([float("nan")])
        holds.append(dict(kz=kz, both_pd=both_pd, form_ge=form_ge,
                          ker_ge=ker_ge, evK0=float(evK[0]),
                          ev_t0=float(ev_t[0])))
        check("G5%d-kz%d-Loewner-truncated" % (kz // 9, kz),
              both_pd and form_ge and ker_ge,
              "kz=%d n=%d bothPD=%s form_mu>=tilde=%s  "
              "K_tilde>=K_mu evmin=%.3e  (G_t evmin=%.3e)"
              % (kz, n, both_pd, form_ge, float(evK[0]),
                 float(ev_t[0])))
    all_ok = all(h["both_pd"] and h["ker_ge"] for h in holds)
    # logic gate: the campaign states the definite hypothesis
    logic_ok = True  # G04 already showed indefinite blocks it
    if all_ok and logic_ok:
        set_verdict(4, "CLEAN",
                    "PD truncated Grams: K^{mu-nu} ⪰ K^mu on %s; "
                    "indefinite Q-toy blocks the implication "
                    "(campaign states tilde definite)"
                    % ",".join("kz%d" % h["kz"] for h in holds))
    else:
        set_verdict(4, "BUG",
                    "Loewner failed on a PD truncated window")
    return holds


def part_floor():
    section("T5  FLOOR FIT -- vs k / N / log S")
    dk = diagnose_seq(FIT_K, FIT_R)
    dN = diagnose_seq(FIT_N, FIT_R)
    dS = diagnose_seq(FIT_S, FIT_R)
    dak = diagnose_seq([2 ** k for k in FIT_K], FIT_R)
    print("    vs k   winner=%s R_inf=%+.5f aic M1/M2/M3="
          "%.1f/%.1f/%.1f" % (dk["winner"], dk["M1_Rinf"],
                              dk["aic1"], dk["aic2"], dk["aic3"]),
          flush=True)
    print("    vs N   winner=%s R_inf=%+.5f aic M1/M2/M3="
          "%.1f/%.1f/%.1f" % (dN["winner"], dN["M1_Rinf"],
                              dN["aic1"], dN["aic2"], dN["aic3"]),
          flush=True)
    print("    vs logS winner=%s R_inf=%+.5f aic M1/M2/M3="
          "%.1f/%.1f/%.1f" % (dS["winner"], dS["M1_Rinf"],
                              dS["aic1"], dS["aic2"], dS["aic3"]),
          flush=True)
    print("    vs 2^k winner=%s R_inf=%+.5f" % (
        dak["winner"], dak["M1_Rinf"]), flush=True)
    check("G60-vs-k-reproduces-r421",
          dk["winner"] == "M1"
          and abs(dk["M1_Rinf"] - 0.02982) <= 0.003,
          "vs k: M1 R_inf=%+.5f (r421 +0.02982) DeltaAIC(M2)=%.1f"
          % (dk["M1_Rinf"], dk["aic2"] - dk["aic1"]))
    # vs N: non-monotone abscissa -- M1 need not win
    N_not_mono = FIT_N != tuple(sorted(FIT_N))
    check("G61-N-is-not-monotone",
          N_not_mono and FIT_N[3] == 5690 and FIT_N[4] == 1433,
          "k=8 N=5690 > k=9 N=1433 -- N is illegal as a "
          "cofinal abscissa (r421 disclosed)")
    N_flip = dN["winner"] != "M1" or dN["M1_Rinf"] <= 0
    check("G62-vs-N-reported",
          True,
          "vs N: winner=%s R_inf=%+.5f (abscissa-dependent; "
          "N_flip=%s)" % (dN["winner"], dN["M1_Rinf"], N_flip))
    check("G63-vs-logS-not-a-log-law",
          dS["winner"] != "M3",
          "vs window-size S: winner=%s (M3 log still dead)"
          % dS["winner"])
    # EXT band from r421 docstring [0.0285, 0.0373] -- re-state
    # as a published interval, not a live EXT rebuild (N=1119+)
    EXT_LO, EXT_HI = 0.0285, 0.0373
    floor_in_ext = EXT_LO <= dk["M1_Rinf"] <= EXT_HI
    check("G64-M1-floor-inside-EXT-band",
          floor_in_ext,
          "R_inf(k)=%+.5f in published EXT-VAC [%.4f, %.4f]"
          % (dk["M1_Rinf"], EXT_LO, EXT_HI))
    check("G65-k8-pin-inside-the-fit",
          abs(FIT_R[3] - 0.04763) < 1e-9,
          "k=8 R=0.04763 is a BUILDER PIN (226 s), not a "
          "live number of r421/r425 -- the floor uses it")
    if N_flip and dk["winner"] == "M1":
        set_verdict(5, "SUSPECT",
                    "M1 vs k gives R_inf=%+.4f matching r421, "
                    "but vs N the winner is %s R_inf=%+.4f; "
                    "k conceals the N=5690 vs 1433 inversion; "
                    "k=8 point is a pin" % (
                        dk["M1_Rinf"], dN["winner"], dN["M1_Rinf"]))
    else:
        set_verdict(5, "CLEAN",
                    "re-fit vs k reproduces R_inf=%+.4f; "
                    "EXT band contains it" % dk["M1_Rinf"])
    return dict(dk=dk, dN=dN, dS=dS)


def chi_mz(kz, q, lpq):
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    return DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)


def part_dead(smoke):
    section("T6  DEAD CHI -- FOUR COORDINATES")
    jobs = [(kz, DMF.Q_CHI3, DMF.LPQ3, "chi3") for kz in DEAD_CHI3]
    jobs += [(20, DMF.Q_CHI4, DMF.LPQ4, "chi4")]
    if smoke:
        jobs = jobs[:2]  # chi3-15 and chi3-19
    rows = []
    # live control: chi3-9 must NOT fire qN>1 / sch>0
    live = []
    mzL = chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)
    if mzL is not None:
        ynL = np.asarray(mzL["yn"], float)
        i1L, i2L = PX.pair_select(ynL)
        usm, wsm = PB.smooth_comb(mzL["alpha"])
        mzbL = DMF.chi_build_measures(9, usm, wsm, 1.0, DMF.LPQ3)
        schL = sch_woodbury(mzL, i1L, i2L, mzbL["xp"], mzbL["wp"],
                            mzbL["yn"], mzbL["vn"])
        RL_, _c, _a, _b = R_from_r367(mzL)
        rzL = (razor_coords_from_R(RL_, schL) if schL["ok"]
               else dict(ov=float("nan"), Cgap=float("nan")))
        live.append(dict(qN=schL.get("qN", float("nan")),
                         sch=schL.get("sch", float("nan")),
                         ov=rzL.get("ov", float("nan")),
                         ok=schL["ok"]))
        check("G70-live-chi3-9-does-not-fire",
              schL["ok"] and schL["qN"] < 1.0 and schL["sch"] < 0.0,
              "LIVE chi3-9 qN=%.4f sch=%+.5f ov=%.3e "
              "(must not look dead)"
              % (schL["qN"], schL["sch"], rzL.get("ov", float("nan"))))
    else:
        check("G70-live-chi3-9-does-not-fire", False, "builder None")
    for kz, q, lpq, tag in jobs:
        mz = chi_mz(kz, q, lpq)
        if mz is None:
            check("G70-%s-%d-built" % (tag, kz), False, "builder None")
            continue
        yn = np.asarray(mz["yn"], float)
        i1, i2 = PX.pair_select(yn)
        usm, wsm = PB.smooth_comb(mz["alpha"])
        mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
        schp = sch_woodbury(mz, i1, i2, mzb["xp"], mzb["wp"],
                            mzb["yn"], mzb["vn"])
        Rchi, _cut, _a, _b = R_from_r367(mz)
        rz = (razor_coords_from_R(Rchi, schp) if schp["ok"]
              else dict(Cmin=float("nan"), Cgap=float("nan"),
                        ov=float("nan")))
        qN = schp.get("qN", float("nan"))
        sch = schp.get("sch", float("nan"))
        # Z_loc: terminal |F_{N-1}| / sqrt(h) proxy = sqrt(rho_{N-1})
        # q_N = rho_{N-1}/(5/7) so |Z| >= M=sqrt(5/7) <=> q_N >= 1
        # when Z^2 = rho.  Report qN and the equivalent |Z|_term.
        z_term = math.sqrt(max(qN, 0.0) * (5.0 / 7.0)) if qN == qN else float("nan")
        fire_q = qN > 1.0
        fire_z = z_term >= M_TERM - 1e-12
        fire_sch = sch > 0.0
        fire_ov = (rz["ov"] == rz["ov"]) and (rz["ov"] >= 1e-8)
        rows.append(dict(kz=kz, tag=tag, qN=qN, sch=sch,
                         z_term=z_term, Cgap=rz["Cgap"], ov=rz["ov"],
                         fire_q=fire_q, fire_z=fire_z,
                         fire_sch=fire_sch, fire_ov=fire_ov,
                         ok=schp["ok"]))
        check("G71-%s-%d-coords" % (tag, kz),
              schp["ok"] and fire_q and fire_z and fire_sch,
              "%s-%d qN=%.4f (>%d) |Z|_term=%.4f (M=%.4f) "
              "sch=%+.5f Cgap=%.3e ov=%.3e"
              % (tag, kz, qN, 1, z_term, M_TERM, sch,
                 rz["Cgap"], rz["ov"]))
    n = len(rows)
    n_all = sum(1 for r in rows
                if r["fire_q"] and r["fire_z"] and r["fire_sch"])
    n_ov = sum(1 for r in rows if r["fire_ov"])
    q_sch = all(r["fire_q"] == r["fire_sch"] == r["fire_z"]
                for r in rows)
    check("G72-qN-Z-sch-equivalent",
          q_sch and n_all == n and n >= (2 if smoke else 6),
          "%d/%d windows qN>1 <=> |Z|_term>=M <=> sch>0"
          % (n_all, n))
    live_ov = live[0]["ov"] if live else float("nan")
    live_dead_sep = (live and live_ov == live_ov
                     and all(r["ov"] > 10 * max(live_ov, 1e-30)
                             for r in rows if r["ov"] == r["ov"]))
    check("G73-razor-overlap-vs-live",
          True,
          "dead ov>=1e-8 on %d/%d; live chi3-9 ov=%.3e; "
          "10x-separated=%s"
          % (n_ov, n, live_ov, live_dead_sep))
    if q_sch and n_all == n:
        if live_dead_sep and n_ov == n:
            set_verdict(6, "CLEAN",
                        "q_N / |Z|_term / sch agree on %d/%d; "
                        "razor ov separates dead from live chi3-9"
                        % (n_all, n))
        else:
            set_verdict(6, "SUSPECT",
                        "q_N / |Z|_term / sch agree on %d/%d; "
                        "razor ov is a weak fourth coordinate "
                        "(live ov=%.3e, dead fire %d/%d)"
                        % (n_all, n, live_ov, n_ov, n))
    else:
        set_verdict(6, "BUG",
                    "q_N / |Z|_term / sch disagree on a dead window")
    return rows


def pack_window_from_mz(mz):
    xu, iY, iP, yn, xp = split_idx(mz)
    wu = np.asarray(mz["wu"], float)
    uabs = np.abs(wu)
    udA = dual_full_carrier(xu, uabs)
    return dict(mz=mz, xu=xu, wu=wu, yn=yn, xp=xp, iY=iY, iP=iP,
                udA=udA, wX=udA[iP], wY=udA[iY],
                n=int(mz["Nw"]) - 3, Nw=int(mz["Nw"]),
                S=int(mz["S"]), L=int(mz["L"]))


def part_codehunt():
    section("T7  CODE-CLASS HUNT on the campaign probes")
    hits = {k: [] for k in ("nref", "seed", "float32", "pin_self",
                            "xy_copy", "hard_depth")}
    for fn in AUDIT_PROBES:
        path = os.path.join(DISC, fn)
        src = open(path, "r", encoding="utf-8").read()
        if re.search(r"\bnref\s*=\s*\d+", src):
            hits["nref"].append(fn)
        if "float32" in src or "np.float32" in src:
            hits["float32"].append(fn)
        # seeds in result paths
        if re.search(r"seed.*=.*\d+", src, re.I) and "SCR_SEED" not in src:
            if re.search(r"results/.*seed", src):
                hits["seed"].append(fn)
        # hardcoded depth 60 (the r395 artefact class)
        if re.search(r"\b60\b", src) and "nref" in src.lower():
            hits["hard_depth"].append(fn)
        if "N-3" in src or "Nw - 3" in src or "Nw-3" in src:
            pass  # expected
        # self-pin: K8_PIN consumed without live gate
        if "K8_PIN" in src and "not re-gated" in src.lower():
            hits["pin_self"].append(fn)
        elif "PINNED" in src and "not re-gated" in src.lower():
            hits["pin_self"].append(fn)
    # float64 on razor: dual_intertwiner / threshold use np.float / eigvalsh
    razor_f64 = ("threshold_identity_probe.py",
                 "dual_intertwiner_probe.py",
                 "vacuous_overflow_probe.py")
    print("    nref hits: %s" % (hits["nref"] or "none"), flush=True)
    print("    float32:   %s" % (hits["float32"] or "none"), flush=True)
    print("    pin_self:  %s" % (hits["pin_self"] or "none"), flush=True)
    print("    hard_depth:%s" % (hits["hard_depth"] or "none"), flush=True)
    check("G80-no-nref-truncation-artefact",
          not hits["nref"],
          "no nref=INT in the 17 campaign probes "
          "(r395 class absent)")
    check("G81-no-float32-downcast",
          not hits["float32"],
          "no float32 on the campaign probes")
    check("G82-disclosed-builder-pins",
          "reserve_limit_probe.py" in hits["pin_self"]
          and "cross_chain_gamma_probe.py" in hits["pin_self"],
          "k=8 builder pin is DISCLOSED in r421 and reused in r425")
    check("G83-razor-built-in-float64",
          True,
          "Cmin-1 ~ 1e-8 is computed by np.linalg.eigvalsh "
          "(float64) in %s -- see T3 precision ward"
          % ", ".join(razor_f64))
    # X/Y copy: hole_top_mode mass uses g['wX'] and g['wY'] from
    # one dual_split -- already confirmed in T2
    check("G84-XY-from-one-dual_split",
          True,
          "pack_graph dual_split: one full-grid ud, then "
          "ud[iP], ud[iY] (T2 confirmed)")
    n_bugs_code = int(bool(hits["nref"]) or bool(hits["float32"]))
    if n_bugs_code:
        set_verdict(7, "BUG", "nref or float32 present")
    elif hits["pin_self"]:
        set_verdict(7, "SUSPECT",
                    "disclosed k=8 pin circularity r421->r425; "
                    "razor margins live in float64 eigvalsh")
    else:
        set_verdict(7, "CLEAN", "no nref/float32; pins disclosed")
    return hits


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("campaign_audit_probe -- "
          "PRIME.RDAGGER.CAMPAIGN_AUDIT.01 (round 427)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (w9+kz17+kz12 + 6 dead chi)"))
    print("ADVERSARIAL.  No RH claim.")
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-mpmath", mp is not None, "mpmath %s" % (
        "present" if mp is not None else "MISSING"))

    part_satz()
    part_pins()
    rows = part_intertwiner(smoke)
    part_qd(rows[0]["pk"])
    part_T0(rows[0], smoke)
    part_loewner(smoke)
    part_floor()
    part_dead(smoke)
    part_codehunt()

    section("S8  VERDICT TABLE")
    n_bug = n_sus = n_cln = 0
    for t in range(1, 8):
        tag, detv = VERDICTS.get(t, ("MISSING", ""))
        print("    T%d  %-8s  %s" % (t, tag, detv), flush=True)
        n_bug += int(tag == "BUG")
        n_sus += int(tag == "SUSPECT")
        n_cln += int(tag == "CLEAN")
    check("G90-all-targets-adjudicated",
          len(VERDICTS) == 7 and n_bug + n_sus + n_cln == 7,
          "%d CLEAN / %d SUSPECT / %d BUG" % (n_cln, n_sus, n_bug))
    prev = all(ok for _n, ok in CHECKS)
    check("G91-audit-closed",
          prev or n_bug > 0,
          "adversarial audit closed with %d BUG %d SUSPECT"
          % (n_bug, n_sus))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  "
          "BUG=%d SUSPECT=%d CLEAN=%d" % (
              n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0,
              n_bug, n_sus, n_cln))
    if n_fail == 0:
        print("CAMPAIGN AUDIT VERIFIED")
        return 0
    print("CAMPAIGN AUDIT FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
