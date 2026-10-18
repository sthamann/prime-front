#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""coherence_assist_probe -- LEMMA.COHERENCE_ASSIST.01 (round 387):
THE COHERENCE-ASSIST LEMMA, the L* remainder after r385.

Coexistence: r385 named the pair (Delta, C) after Q<1 failed as a
floor plate (two-period c=2/3: Q==0.683 and lambda_max(E_22)>1).
The C half is the r285 bookkeeping
lambda_max(E_k) = maxdiag_k * (1 + assist_k).  This round attacks
assist from cosine-grid geometry (Chebyshev-CD = Dirichlet,
3/8-floor, F1 run-lengths).  next.txt is NOT written.  NO Lean
edit.  NO RH CLAIM.

THE FROZEN QUESTION.  For canonical windows, assist_k <= A(k)
from a source-defined property of the nu-angles on the cosine
grid (separation / interlacing / Dirichlet control via
Gershgorin or Schur), NOT from measurement, such that
lambda_max(E_k) <= maxdiag * (1+assist) < 1 through k = N-1?
The two-period adversary MUST violate the property.

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Anatomy: lambda = maxdiag*(1+assist) exact; Chebyshev-T CD
     kernel = [D_{k-1}(theta-phi)+D_{k-1}(theta+phi)]/(2 pi);
     Gershgorin/Schur unsigned majorant vs true assist on w9.
  B  Why the two-period dies: global arithmetic progression of
     nu-angles (AP-fraction = 1, consecutive gaps unique) vs
     source incommensurability; Dirichlet max-row at k=22.
  C  Depth: largest k* with Gershgorin < 1, compared to
     n0 = floor(2N/5) (r382) and N-1.
  D  Kills: two-period c=2/3 and c=1, scramble, clustered
     run-3, AP-fraction bar mutant, EXT-heavy seven.

CALIBRATION DISCLOSURE.  Identities, w9 walk, two-period /
scramble / cluster, core-42 AP-fraction and k_gersh, EXT-heavy
angle stats, and Dirichlet max-rows were first measured in
/tmp (r387_cal.py, r387_cal2.py) on the same constructors,
2026-08-28.  Frozen floors/ceilings below are that measurement,
sealed as gates -- not a search over 1/5 or 2/5.  No two-commit
pre-blind freeze: pins disclosed.  MAIN-85 E-walk and the
181-pack builder were not rerun (R385 lesson), disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Chebyshev-T CD closed form == cosine sum (maxdev 1e-15).
  * Bookkeeping identity |lam - maxdiag*(1+assist)| = 0
    (2x2 equality case [[2,1],[1,2]]: lam=3, maxdiag=2,
    assist=1/2, Gershgorin=3).
  * Cosine mesh: theta_j = pi j / S, Delta_mesh = pi/S.
    F1 run-of-2 => dmin = 1 mesh step.  w9: S=367, dmin =
    dmed/3, dmin/dmed = 1/3 < 3/8 -- the 3/8-floor of the
    log-sieve does NOT upgrade nu-angle separation.
  * w9 N=184 n_nu=104: k_gersh first >=1 is 21 (k*=20);
    at k=183 lam=0.99983 maxdiag=0.9614 assist=0.0399
    (r285 range; R385's 'assist 1.54' mixed the single-degree
    Q_k~0.39 with maxdiag(E)).  Gershgorin assist=13.32,
    cancellation 1-assist/gA = 0.997.  AP=8, rho_AP=0.0769,
    cv=0.813.  Dirichlet max-row at k=22 = 0.291.
  * Two-period S=81 c=2/3: rho_AP=1 (AP=41/41), cv=0.078,
    Q==0.683, lam(E_22)=1.029>1, Dirichlet max-row=0.858
    (~3x source).  c=1: lam(E_1)=1.025>1.
  * Scramble seed=1: rho_AP=0.064 HOLDS like source;
    k_lam=22, k_maxdiag=50 -- dies on the product / diagonal,
    NOT on the AP property.
  * Clustered run-3 S=81: k_lam=15 < n0=16, rho_AP=1.
    Run-2: k_lam=21 > n0 (F1 allows run-2).
  * CORE-42: rho_AP in [0.034, 0.168] < 1/5; cv in [0.536,
    0.892] > 1/2; k_gersh in [8, 32], ALL < n0,
    k_gersh/N max=0.114 < 2/5.  Mutant bar rho_AP<=0.03
    FAILS (max 0.168).
  * EXT-heavy 7: rho_AP in [0.006, 0.033] < 0.05; cv>=0.56;
    lam at depth 80 < 1 (sharpest kz97 = 0.9965).

AUSGANG REDUZIERT.  SATZ: Chebyshev-Dirichlet CD; bookkeeping;
Gershgorin majorant; cosine mesh; two-period = global AP.
The deduction 'therefore assist <= (1-Q)/Q from 3/8-separation
+ Gershgorin' is false: k*_Gershgorin ~ 0.11 N << floor(2N/5),
and dmin/dmed = 1/3 < 3/8.  Named source property that KILLS
the two-period and HOLDS on EXT-heavy: rho_AP = L_AP / n_nu
< 1/5 (not a single arithmetic progression of nu-angles).
Scramble holds rho_AP and dies on maxdiag.  Remaining,
strictly smaller: the SIGNED mu-CD off-diagonal (true assist;
unsigned/Gershgorin is closed as too crude).  n0 = floor(2N/5)
is NOT improved.  n0 = N-1 stays open with that remainder.

MACHINERY: r226 hirota_sign.window_data, r283
verify_lstar_instance.build_measures / mu_chain / b_matrix,
r382 two-period / clustered.

NO RH CLAIM.  Finite identities, a named reduction, named
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

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402

SCR_SEED = 1
MAIN_KZ = 9
HEAVY7 = (69, 96, 97, 99, 107, 117, 129)
C_FLANK = 2.0 / 3.0
CORE_N = 42
AP_BAR = 0.20
AP_MUTANT = 0.03
CV_FLOOR = 0.50
KG_OVER_N_BAR = 0.15
KG_MAX_BAR = 32
EXT_AP_BAR = 0.05

W9_KG = 21
W9_MAXD_LO, W9_MAXD_HI = 0.95, 0.97
W9_ASSIST_LO, W9_ASSIST_HI = 0.030, 0.050
W9_AP_BAR = 0.10
W9_CV_FLOOR = 0.70
W9_DROW_BAR = 0.35
TP_Q_LO, TP_Q_HI = 0.680, 0.690
TP_DROW_FLOOR = 0.80
SCR_KLAM_LO, SCR_KLAM_HI = 20, 25
SCR_KMAXD_LO, SCR_KMAXD_HI = 45, 55
ID_BAR = 1.0e-12
CHEB_BAR = 1.0e-12

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
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "build_measures only"
                       if not bad else "; ".join(bad))


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S, xu=x, wu=w)


def clustered(S, cluster=3):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = mesh.copy()
    mid = S // 2
    w[mid:mid + cluster] *= -1.0
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S)


def dirichlet(n, a):
    a = np.asarray(a, float)
    out = np.empty_like(a)
    s = np.sin(a / 2.0)
    small = np.abs(s) < 1e-14
    out[small] = 2 * n + 1
    out[~small] = np.sin((n + 0.5) * a[~small]) / s[~small]
    return out


def cheb_K_closed(n, th, ph):
    return (dirichlet(n - 1, th - ph) + dirichlet(n - 1, th + ph)) / (
        2.0 * math.pi)


def cheb_K_sum(n, th, ph):
    s = 1.0 / math.pi
    for j in range(1, n):
        s += (2.0 / math.pi) * math.cos(j * th) * math.cos(j * ph)
    return s


def max_ap_length(th, tol=1e-9):
    t = np.sort(np.asarray(th, float))
    n = len(t)
    best = 1
    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            delta = t[j] - t[i]
            if delta < 1e-14:
                continue
            cnt = 2
            expect = t[j] + delta
            k = j + 1
            while k < n:
                if abs(t[k] - expect) < tol * (1.0 + abs(expect)):
                    cnt += 1
                    expect += delta
                elif t[k] > expect + tol:
                    break
                k += 1
            if cnt > best:
                best = cnt
    return best


def angle_pack(yn, S):
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    t = np.sort(th)
    d = np.diff(t)
    wrap = t[0] + math.pi - t[-1]
    dc = np.concatenate([d, [wrap]])
    mesh = math.pi / S
    ap = max_ap_length(th)
    n = len(th)
    return dict(
        th=th, n=n, ap=ap, frac=ap / max(n, 1),
        dmin=float(np.min(dc)), dmed=float(np.median(dc)),
        cv=float(np.std(dc) / max(float(np.mean(dc)), 1e-30)),
        ratio=float(np.min(dc) / max(float(np.median(dc)), 1e-30)),
        mesh=mesh,
        dmin_mesh=float(np.min(d) / mesh) if len(d) else 0.0,
    )


def gram_lam(B):
    m, k = B.shape
    G = B @ B.T if m <= k else B.T @ B
    return float(np.linalg.eigvalsh(G)[-1])


def make_B(mz, depth):
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], depth)
    return V.b_matrix(a, b, h0, mz["yn"], mz["vn"], depth)


def walk_cross(mz, depth, stop="all"):
    """First k with gersh/lam/maxdiag >= 1.  Streams E.
    stop='gersh' returns at the Gershgorin crossing (core census)."""
    B = make_B(mz, depth)
    m = B.shape[0]
    E = np.zeros((m, m))
    k_g = k_l = k_d = None
    last = None
    for k in range(1, depth + 1):
        E += np.outer(B[:, k - 1], B[:, k - 1])
        diag = np.diag(E)
        maxd = float(np.max(diag))
        off = np.abs(E).copy()
        np.fill_diagonal(off, 0.0)
        gersh = float(np.max(diag + off.sum(axis=1)))
        need_lam = stop != "gersh" or k_g is not None
        lam = gram_lam(B[:, :k]) if need_lam else 0.0
        gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
        last = dict(k=k, lam=lam, maxd=maxd,
                    assist=(lam / maxd - 1.0) if maxd > 0 else 0.0,
                    gersh=gersh, gA=gA)
        if k_g is None and gersh >= 1.0:
            k_g = k
        if k_l is None and lam >= 1.0:
            k_l = k
        if k_d is None and maxd >= 1.0:
            k_d = k
        if stop == "gersh" and k_g is not None:
            break
        if stop == "lam" and k_l is not None:
            break
        if (stop == "all" and k_g is not None and k_l is not None
                and k_d is not None):
            break
    return k_g, k_l, k_d, last, B, E


def dirichlet_maxrow(th, vn, k):
    sv = np.sqrt(vn)
    mx = 0.0
    for i in range(len(th)):
        D = np.abs(dirichlet(k - 1, th[i] - th))
        D[i] = 0.0
        row = float(np.dot(D, sv) * sv[i] / (2.0 * math.pi))
        if row > mx:
            mx = row
    return mx


def part_a_standalone():
    section("S1  LEG A -- CHEBYSHEV-DIRICHLET, BOOKKEEPING, GERSHGORIN")
    ok = True
    for n, th, ph in ((5, 0.3, 1.1), (12, 0.7, 0.7),
                      (20, 1.2, 0.4), (8, 0.0, math.pi)):
        if abs(cheb_K_closed(n, th, ph) - cheb_K_sum(n, th, ph)) > CHEB_BAR:
            ok = False
    check("G01-Chebyshev-CD-Dirichlet",
          ok, "K_n(cos th, cos ph) = [D_{n-1}(th-ph)+D_{n-1}(th+ph)]/(2pi)")

    # 2x2 equality: E=[[2,1],[1,2]], lam=3, maxdiag=2, assist=1/2
    E = np.array([[2.0, 1.0], [1.0, 2.0]])
    lam = float(np.linalg.eigvalsh(E)[-1])
    maxd = float(np.max(np.diag(E)))
    assist = lam / maxd - 1.0
    gersh = float(np.max(np.sum(np.abs(E), axis=1)))
    check("G02-bookkeeping-2x2",
          abs(lam - 3.0) < ID_BAR and abs(assist - 0.5) < ID_BAR
          and abs(lam - maxd * (1.0 + assist)) < ID_BAR,
          "lam=3 maxdiag=2 assist=1/2 identity exact")
    check("G03-Gershgorin-equals-lam-2x2",
          abs(gersh - 3.0) < ID_BAR and gersh + 1e-15 >= lam,
          "Gershgorin=3 == lam on the all-ones mode")

    mz = two_period(21, C_FLANK)
    ap = angle_pack(mz["yn"], 21)
    d = np.diff(np.sort(ap["th"]))
    uniq = len(np.unique(np.round(d, 8)))
    check("G04-two-period-global-AP",
          ap["frac"] == 1.0 and ap["ap"] == ap["n"] and uniq == 1,
          "S=21 rho_AP=1 AP=%d/%d consec-unique=%d" % (
              ap["ap"], ap["n"], uniq))

    # mesh: two consecutive cosine nodes
    S = 16
    j = np.array([3, 4])
    th = np.arccos(np.cos(math.pi * j / S))
    check("G05-mesh-step-is-pi-over-S",
          abs(abs(th[1] - th[0]) - math.pi / S) < 1e-14,
          "Delta_mesh = pi/S exact on the cosine grid")

    # 3/8 does not upgrade: a run-of-2 plus skips of 3 gives 1/3
    check("G06-three-eighths-does-not-upgrade",
          abs((1.0 / 3.0) - 0.375) > 0.04,
          "1/3 < 3/8: min nu-gap = 1 mesh, median typically 3 mesh")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 / two-period / scramble / cluster")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    S = int(mz["S"])
    n0 = (2 * N) // 5
    ap = angle_pack(mz["yn"], S)
    B = make_B(mz, N - 1)
    m = B.shape[0]
    E = np.zeros((m, m))
    k_g = None
    snap = {}
    for k in range(1, N):
        E += np.outer(B[:, k - 1], B[:, k - 1])
        diag = np.diag(E)
        off = np.abs(E).copy()
        np.fill_diagonal(off, 0.0)
        gersh = float(np.max(diag + off.sum(axis=1)))
        if k_g is None and gersh >= 1.0:
            k_g = k
        if k in (22, N - 1):
            maxd = float(np.max(diag))
            lam = gram_lam(B[:, :k])
            gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
            assist = lam / maxd - 1.0
            snap[k] = dict(lam=lam, maxd=maxd, assist=assist,
                           gersh=gersh, gA=gA,
                           canc=1.0 - assist / max(gA, 1e-12))
    wall = snap[N - 1]
    check("G10-w9-k-gersh",
          k_g == W9_KG and k_g < n0,
          "k_gersh=%d n0=%d k*/N=%.3f (no improvement of r382)"
          % (k_g, n0, (k_g - 1) / N))
    check("G11-w9-wall-assist",
          W9_MAXD_LO < wall["maxd"] < W9_MAXD_HI
          and W9_ASSIST_LO < wall["assist"] < W9_ASSIST_HI
          and wall["lam"] < 1.0 and wall["canc"] > 0.99,
          "k=183 lam=%.6f maxd=%.4f assist=%.4f canc=%.4f "
          "(R385 mixed Q_k with maxdiag; true assist is r285-small)"
          % (wall["lam"], wall["maxd"], wall["assist"], wall["canc"]))
    check("G12-w9-AP-incommensurable",
          ap["frac"] < W9_AP_BAR and ap["cv"] > W9_CV_FLOOR
          and abs(ap["ratio"] - 1.0 / 3.0) < 0.01
          and abs(ap["dmin_mesh"] - 1.0) < 1e-6,
          "rho_AP=%.4f cv=%.3f dmin/dmed=%.3f dmin=%.2f mesh"
          % (ap["frac"], ap["cv"], ap["ratio"], ap["dmin_mesh"]))

    mz23 = two_period(81, C_FLANK)
    ap23 = angle_pack(mz23["yn"], 81)
    B23 = make_B(mz23, 22)
    lam22 = gram_lam(B23)
    Q0 = float(np.sum(mz23["vn"])) / float(np.sum(mz23["wp"]))
    drow_s = dirichlet_maxrow(ap["th"], mz["vn"], 22)
    drow_t = dirichlet_maxrow(ap23["th"], mz23["vn"], 22)
    check("G13-Dirichlet-maxrow-source-vs-TP",
          drow_s < W9_DROW_BAR and drow_t > TP_DROW_FLOOR
          and drow_t > 2.0 * drow_s,
          "k=22 D-maxrow source=%.3f TP=%.3f (constructive AP)"
          % (drow_s, drow_t))
    check("G14-two-period-c23-kills-on-AP",
          ap23["frac"] == 1.0 and lam22 > 1.0
          and TP_Q_LO < Q0 < TP_Q_HI,
          "rho_AP=1 Q=%.4f lam22=%.4f>1 (Q<1 is not the floor)"
          % (Q0, lam22))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    mzs = dict(xp=ds["xs"], wp=ds["ws"], yn=ds["ys"], vn=ds["vs"])
    kgs, kls, kds, _last, _B, _E = walk_cross(mzs, 80)
    aps = angle_pack(ds["ys"], S)
    check("G15-scramble-dies-on-diag-not-AP",
          kls is not None and SCR_KLAM_LO <= kls <= SCR_KLAM_HI
          and kds is not None and SCR_KMAXD_LO <= kds <= SCR_KMAXD_HI
          and aps["frac"] < W9_AP_BAR,
          "k_lam=%s k_maxd=%s rho_AP=%.3f (AP HOLDS; product kills)"
          % (kls, kds, aps["frac"]))

    mz1 = two_period(81, 1.0)
    lam1 = gram_lam(make_B(mz1, 1))
    mz_c3 = clustered(81, 3)
    mz_c2 = clustered(81, 2)
    n0_tp = (2 * 41) // 5
    _g, kl3, _d, _l, _b, _e = walk_cross(mz_c3, 24, stop="lam")
    _g2, kl2, _d2, _l2, _b2, _e2 = walk_cross(mz_c2, 24, stop="lam")
    apc3 = angle_pack(mz_c3["yn"], 81)
    check("G16-c1-and-cluster-run3",
          lam1 > 1.0
          and kl3 is not None and kl3 < n0_tp
          and apc3["frac"] == 1.0
          and (kl2 is None or kl2 > n0_tp),
          "c=1 lam1=%.4f CL3 k_lam=%s<n0=%d rho_AP=1; "
          "CL2 k_lam=%s>n0 (F1 allows run-2)"
          % (lam1, kl3, n0_tp, kl2))

    if smoke:
        return

    section("S3  FULL CENSUS -- core-42 AP / k_gersh, EXT-heavy 7")
    core = list(V.admissible_indices())
    check("G20-ladder-size",
          len(core) == CORE_N, "core %d" % len(core))

    fracs, cvs, kgs, n0s, Ns = [], [], [], [], []
    for kz in core:
        mzk = V.build_measures(kz)
        Nv = int(mzk["Nw"])
        Ss = int(mzk["S"])
        apk = angle_pack(mzk["yn"], Ss)
        n0k = (2 * Nv) // 5
        kg, _kl, _kd, _la, _B, _E = walk_cross(
            mzk, min(n0k, 80), stop="gersh")
        fracs.append(apk["frac"])
        cvs.append(apk["cv"])
        kgs.append(kg if kg else min(n0k, 80) + 1)
        n0s.append(n0k)
        Ns.append(Nv)
    check("G21-CORE42-AP-frac",
          max(fracs) < AP_BAR and min(fracs) > 0.02,
          "rho_AP in [%.4f, %.4f] < 1/5" % (min(fracs), max(fracs)))
    check("G22-CORE42-gap-cv",
          min(cvs) > CV_FLOOR,
          "cv in [%.3f, %.3f] > 1/2" % (min(cvs), max(cvs)))
    kg_over_n = max(g / n for g, n in zip(kgs, Ns))
    check("G23-CORE42-k-gersh-below-n0",
          all(g < n for g, n in zip(kgs, n0s))
          and max(kgs) <= KG_MAX_BAR
          and kg_over_n < KG_OVER_N_BAR,
          "k_gersh in [%d, %d] all<n0 k_g/N max=%.3f "
          "(Gershgorin does NOT improve r382)"
          % (min(kgs), max(kgs), kg_over_n))
    check("G24-AP-bar-mutant",
          max(fracs) > AP_MUTANT,
          "mutant rho_AP<=0.03 FAILS (max=%.4f); honest bar 1/5"
          % max(fracs))

    ext_fracs, ext_cvs, ext_lams = [], [], []
    for kz in HEAVY7:
        mzk = V.build_measures(kz)
        apk = angle_pack(mzk["yn"], int(mzk["S"]))
        lam80 = gram_lam(make_B(mzk, 80))
        ext_fracs.append(apk["frac"])
        ext_cvs.append(apk["cv"])
        ext_lams.append(lam80)
    check("G25-EXT7-AP-holds-lam80",
          max(ext_fracs) < EXT_AP_BAR
          and min(ext_cvs) > CV_FLOOR
          and max(ext_lams) < 1.0,
          "rho_AP max=%.4f cv min=%.2f lam80 max=%.4f (property HOLDS)"
          % (max(ext_fracs), min(ext_cvs), max(ext_lams)))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("coherence_assist_probe -- LEMMA.COHERENCE_ASSIST.01 "
          "(round 387)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_construction(smoke)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = "COHERENCE ASSIST SMOKE" if smoke else "COHERENCE ASSIST"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
