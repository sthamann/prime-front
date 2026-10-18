#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weyl_energy_probe -- LEMMA.WEYL_ENERGY.01 (round 389):
THE WEYL ENERGY OF CANCELLATION, exact decomposition instead of
a majorant.

Coexistence: four majorant routes died at the same place
(r381 L^inf, r385 Koksma, r387 Gershgorin, r388 osc-Geronimus).
The three open cancellation objects are the signed mu-CD
off-diagonal (assist 0.0399 vs Gershgorin 13.32), terminal
C_eps (|FO|<=1/32 on the last twelve), and Z_loc (median cancel
0.055, not uniform).  This round COMPUTES the cancellation as
weighted Weyl energy of the nu-angles, rather than majorizing it.

THE FROZEN QUESTION.  Is there an exact energy identity
Sigma_{i!=j} v_i v_j K_k(x_i,x_j) = Sigma_q c_q |S_q|^2 - diag
with S_q = Sigma_j v_j e^{i q theta_j}, and does a bound on that
energy at quadratic-mean (Parseval on the cosine grid), PNT, or
sub-quadratic-mean scale close assist / C_eps / Z_loc?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Exact energy identity for (i) Chebyshev-CD assist bilinear
     plus mu-CD remainder, (ii) FO_k, (iii) Z_loc Chebyshev
     proxy.  Fractions on a toy, mpmath on w9.
  B  |S_q|^2 spectrum on core-42 + EXT-heavy + chi: quadratic
     mean vs structured valleys; MAIN vs scramble vs two-period
     pointwise.
  C  Scale adjudication: which bound on Sigma c_q |S_q|^2
     closes (a) assist, (b) |FO|<=1/32, (c) Z_loc uniform.
     Weighted (von Mangoldt) vs equal-weight energy.
  D  Kills: wrong c_q, missing diagonal, two-period comb,
     scramble divergence modes.

CALIBRATION DISCLOSURE.  Identities, w9 energy/Parseval/
spectrum/FO, scramble and two-period spectra, core-42 /
EXT-heavy / chi3-42 tallies, and the wall Rayleigh were first
measured in /tmp (tfpt_r389_cal.py, WALL 2.1 s) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are that
measurement, sealed as gates -- not a search over 1/2 or 1/5.
No two-commit pre-blind freeze: pins disclosed.  No builder
fallback: the spectrum census is O(n_nu * q_max) and finished
in seconds (181-pack E-walks not rerun, disclosed).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Fractions 5-atom: Phi* = M^2 + 2 Sigma C_m^2 equals the
    T-kernel bilinear (Phi*=99); off = Phi - diag = 26.
    Float 6-atom energy rel 0; off rel 3.4e-16.  Mutant
    missing-diag |Phi-off|/|off|=2.78; mutant c_q=1 rel=0.108.
  * Q_k^T = (C_0 + C_{2k})_nu / (C_0 + C_{2k})_mu exact.
    pi_k^2 Weyl via Chebyshev coeffs of the mu-OP: rel 7.8e-16
    on a 5-atom toy.  mpmath dps-30 w9 k=8 energy rel 4.3e-31.
  * Finite-grid Parseval Sigma_{q=0}^{2S-1} |S_q|^2 = 2 S Sigma v_j^2
    ratio = 1 exactly (two-period S=21, w9 nu-only, w9 kept
    union).  THIS is the Parseval balance.
  * w9 spectrum M=400: mean_{m>=1} C_m^2 / (0.5 Sigma v^2) = 0.922
    (quadratic-mean / pseudorandom); max/qm=14.5 at m=208;
    |C|/mass last-12 in [0.0005, 0.179] -- TRIVIAL Weyl, not PNT.
    HHI m=1..80 = 0.053 (random ~0.013).  Wall Chebyshev off of
    v otimes v is NEGATIVE (-0.007); true assist is a Rayleigh
    of E, not the all-ones bilinear (1^T E^T 1 / n_nu = 0.114
    vs lam=0.99983).
  * FO^T last-12 = 0.00496 < 1/32; true FO=0.00978 < 1/32;
    g12=0.276, need |dQ|<=0.113, measured 0.039.  The Chebyshev
    piece of C_eps CLOSES at quadratic-mean.  dDelta=0.049 is
    the live remainder.
  * Two-period S=81: |C_S|/mass=1, HHI=0.727, comb at q=0,1,S-1,S,S+1.
    rho_AP=1 is spectral concentration on a progression.
  * Scramble seed=1: mean/qm=0.947 (QM, holds); HHI=0.0365
    (more uniform than MAIN).  Top |Delta C_m^2| modes
    380, 354, 30, 177, 170, 23.  Named kill of 'nu-Weyl
    concentration separates scramble': it does not.
  * CORE-42 (M=200): mean/qm in [0.661, 1.018]; |C|/mass max
    in [0.229, 0.401]<1/2; HHI in [0.013, 0.097]<0.12.
    Small-N n=11 max|FO|=0.01182, max|FO^T|=0.0165, both <1/32.
    * EXT-heavy 7: |C|/mass max in [0.237, 0.348]<0.40 (QM-class
    |S_q|/mass; HHI 0.16..0.35 is flank-mass, not a two-period
    comb).  CHI3-42 mean/qm in [0.658, 0.909].
  * von Mangoldt vs equal-weight on w9: weighted mean/qm=0.718
    > equal 0.403 -- the weights do NOT buy extra cosine
    cancellation (equal is more cancelled).
  * Sealed gates: 19/19 smoke / 27/27 full.
  * von Mangoldt vs equal-weight on w9: weighted mean/qm=0.718
    > equal 0.403 -- the weights do NOT buy extra cosine
    cancellation (equal is more cancelled).

AUSGANG REDUZIERT.  SATZ: the Chebyshev energy identity, the
off=Phi-diag identity, Q^T as C_{2k} ratio, pi_k^2 Weyl, and
the finite-grid Parseval.  MAIN/chi sit at quadratic-mean
(Parseval + no comb); two-period is the concentrating
adversary (rho_AP=1 <=> energy on a progression).  Scale:
FO^T closes C_eps at quadratic-mean; assist is not the
Chebyshev all-ones energy (need the top mode of E); Z_loc is
not the Chebyshev x T_k^2 proxy (cancel 0.47 vs r386 median
0.055).  Named remainder: Weyl energy of the mu-OP Chebyshev
coefficient Gram -- of phi* (assist), of consecutive alpha_k
(dDelta / C_eps), of the edge-masked drive (Z_loc).
Scramble holds QM and dies on that remainder.

MACHINERY: r226 hirota_sign.window_data, r283
verify_lstar_instance.build_measures / mu_chain / b_matrix,
r330 chi_build_measures, r387 Chebyshev-Dirichlet CD, r385 Q^T.

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
from fractions import Fraction as Fr

import numpy as np
from numpy.polynomial.chebyshev import chebfit, chebval

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

SCR_SEED = 1
CEPS = 1.0 / 32.0
MAIN_KZ = 9
HEAVY7 = (69, 96, 97, 99, 107, 117, 129)
C_FLANK = 2.0 / 3.0
CORE_N = 42
CHI3_N = 42
SMALLN_FO_N = 11
PI = math.pi

# disclosed /tmp pins
ID_BAR = 1.0e-12
MP_BAR = 1.0e-20
PARSEVAL_DEV = 1.0e-10
W9_MEANQM_LO, W9_MEANQM_HI = 0.80, 1.05
W9_FO12_BAR = 0.012
W9_FOT12_BAR = 0.010
W9_ASSIST_LO, W9_ASSIST_HI = 0.030, 0.050
W9_MAXD_LO, W9_MAXD_HI = 0.95, 0.97
W9_PHI_WALL_LO, W9_PHI_WALL_HI = 0.050, 0.070
TP_HHI_FLOOR = 0.50
TP_CS_FLOOR = 0.90
SCR_MEANQM_LO, W9_SCR_MEANQM_HI = 0.80, 1.10
SCR_HHI_BAR = 0.08
SCR_DIV_MODES = (23, 30, 170, 177, 354, 380)
CORE_MEANQM_LO, CORE_MEANQM_HI = 0.50, 1.15
CORE_CMASS_HI = 0.45
CORE_HHI_HI = 0.12
EXT_CMASS_HI = 0.40
CHI_MEANQM_LO, CHI_MEANQM_HI = 0.50, 1.15
SMALLN_FOT_BAR = CEPS
MUT_DIAG_FLOOR = 1.5
MUT_CQ_FLOOR = 0.05
EQ_GAP = 0.10   # weighted mean/qm exceeds equal by this

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
                       "build_measures / chi_build_measures only"
                       if not bad else "; ".join(bad))


def C_cos(th, v, mmax):
    th = np.asarray(th, float)
    v = np.asarray(v, float)
    m = np.arange(mmax + 1)[:, None]
    return (v[None, :] * np.cos(m * th[None, :])).sum(1)


def energy_from_C(C, k):
    if k <= 0:
        return 0.0
    s = float(C[0] * C[0])
    if k > 1:
        s += 2.0 * float(np.dot(C[1:k], C[1:k]))
    return s / PI


def bilinear_K(th, v, k):
    th = np.asarray(th, float)
    v = np.asarray(v, float)
    n = len(v)
    acc = 0.0
    for i in range(n):
        for j in range(n):
            s = 1.0 / PI
            for m in range(1, k):
                s += (2.0 / PI) * math.cos(m * th[i]) * math.cos(m * th[j])
            acc += v[i] * v[j] * s
    return acc


def diag_K(th, v2, k):
    th = np.asarray(th, float)
    v2 = np.asarray(v2, float)
    acc = (k / PI) * float(np.sum(v2))
    if k > 1:
        m = np.arange(1, k)[:, None]
        acc += (1.0 / PI) * float(
            (v2[None, :] * np.cos(2.0 * m * th[None, :])).sum())
    return acc


def parseval_ratio(th, v, Sloc):
    v = np.asarray(v, float)
    th = np.asarray(th, float)
    Qm = 2 * int(Sloc)
    m = np.arange(Qm)[:, None]
    C = (v[None, :] * np.cos(m * th[None, :])).sum(1)
    U = (v[None, :] * np.sin(m * th[None, :])).sum(1)
    acc = float(np.dot(C, C) + np.dot(U, U))
    rhs = 2.0 * Sloc * float(np.dot(v, v))
    return acc / max(rhs, 1e-30)


def hhi(C, k):
    t = np.asarray(C[1:k], float) ** 2
    s = float(np.sum(t))
    if s <= 0:
        return 0.0
    p = t / s
    return float(np.sum(p * p))


def spec_pack(th, v, M=200):
    v = np.asarray(v, float)
    th = np.asarray(th, float)
    mass = float(np.sum(v))
    sumv2 = float(np.dot(v, v))
    C = C_cos(th, v, M)
    tail = C[1:M + 1] ** 2
    qm = 0.5 * sumv2
    return dict(
        C=C, mass=mass, sumv2=sumv2, qm=qm,
        mean_over_qm=float(np.mean(tail)) / max(qm, 1e-30),
        max_over_qm=float(np.max(tail)) / max(qm, 1e-30),
        argmax=int(np.argmax(tail)) + 1,
        hhi=hhi(C, M),
        C_mass_max=float(np.max(np.abs(C[1:M + 1]))) / max(mass, 1e-30),
    )


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S, xu=x, wu=w, j=j, th_full=math.pi * j / S)


def T_fr(x, n):
    t0, t1 = Fr(1), x
    ts = [t0]
    if n >= 1:
        ts.append(t1)
    for _ in range(n - 1):
        t0, t1 = t1, 2 * x * t1 - t0
        ts.append(t1)
    return ts


def mu_Qk(xp, wp, yn, vn, depth):
    a, b, h0 = V.mu_chain(xp, wp, depth)
    u = np.ones_like(yn) / math.sqrt(h0)
    um = np.zeros_like(yn)
    Q = np.empty(depth)
    Q[0] = float(np.dot(vn, u * u))
    for i in range(depth - 1):
        r = (yn - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        Q[i + 1] = float(np.dot(vn, u * u))
    return Q, b, h0


def qcheb_all(xp, wp, yn, vn, depth):
    thy = np.arccos(np.clip(yn, -1.0, 1.0))
    thx = np.arccos(np.clip(xp, -1.0, 1.0))
    ks = np.arange(depth)[:, None]
    num = (vn[None, :] * (1.0 + np.cos(2.0 * ks * thy[None, :]))).sum(1)
    den = (wp[None, :] * (1.0 + np.cos(2.0 * ks * thx[None, :]))).sum(1)
    return num / np.maximum(den, 1e-30)


def part_a_standalone():
    section("S1  LEG A -- ENERGY IDENTITY, PARSEVAL, MUTANTS")
    nodes = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    k = 4
    Ts = [T_fr(x, k - 1) for x in nodes]
    M = sum(wts)
    Cs = [sum(w * t[m] for w, t in zip(wts, Ts)) for m in range(k)]
    Phi_star = M * M + 2 * sum(c * c for c in Cs[1:])
    acc = Fr(0)
    for i, vi in enumerate(wts):
        for j, vj in enumerate(wts):
            ker = Fr(1)
            for m in range(1, k):
                ker += 2 * Ts[i][m] * Ts[j][m]
            acc += vi * vj * ker
    check("G01-Fractions-energy",
          acc == Phi_star,
          "Phi*=%s exact over Q (no 1/pi scale)" % Phi_star)

    diag_star = Fr(0)
    for x, v in zip(nodes, wts):
        t = T_fr(x, 2 * (k - 1))
        ker = Fr(k) + sum(t[2 * m] for m in range(1, k))
        diag_star += v * v * ker
    off_star = Phi_star - diag_star
    check("G02-Fractions-off-is-Phi-minus-diag",
          off_star == Fr(26) and diag_star == Fr(73),
          "off=%s diag=%s" % (off_star, diag_star))

    th_toy = np.array([0.3, 0.7, 1.1, 1.6, 2.1, 2.6])
    v_toy = np.array([0.4, 0.7, 0.2, 0.5, 0.9, 0.3])
    k_toy = 5
    C_toy = C_cos(th_toy, v_toy, k_toy)
    Phi_e = energy_from_C(C_toy, k_toy)
    Phi_d = bilinear_K(th_toy, v_toy, k_toy)
    off_e = Phi_e - diag_K(th_toy, v_toy * v_toy, k_toy)
    off_d = 0.0
    for i in range(len(v_toy)):
        for j in range(len(v_toy)):
            if i == j:
                continue
            s = 1.0 / PI
            for m in range(1, k_toy):
                s += (2.0 / PI) * math.cos(m * th_toy[i]) * math.cos(
                    m * th_toy[j])
            off_d += v_toy[i] * v_toy[j] * s
    check("G03-float-energy-and-off",
          abs(Phi_e - Phi_d) < ID_BAR
          and abs(off_e - off_d) < 1e-14,
          "energy rel=%.3e off rel=%.3e" % (
              abs(Phi_e - Phi_d) / max(abs(Phi_d), 1e-30),
              abs(off_e - off_d) / max(abs(off_d), 1e-30)))

    Phi_mut = (C_toy[0] ** 2 + float(np.dot(C_toy[1:k_toy], C_toy[1:k_toy]))) / PI
    check("G04-mutant-wrong-cq-fails",
          abs(Phi_mut - Phi_d) / max(abs(Phi_d), 1e-30) > MUT_CQ_FLOOR,
          "c_q=1 rel=%.3f" % (abs(Phi_mut - Phi_d) / max(abs(Phi_d), 1e-30)))
    check("G05-mutant-missing-diag-fails",
          abs(Phi_e - off_d) / max(abs(off_d), 1e-30) > MUT_DIAG_FLOOR,
          "|Phi-off|/|off|=%.3f" % (
              abs(Phi_e - off_d) / max(abs(off_d), 1e-30)))

    thx = np.array([0.2, 0.8, 1.3, 1.9, 2.4])
    wx = np.array([0.5, 0.6, 0.7, 0.8, 0.4])
    qt_ok = True
    for kk in (0, 1, 2, 4):
        num = float(np.dot(v_toy, 1.0 + np.cos(2 * kk * th_toy)))
        den = float(np.dot(wx, 1.0 + np.cos(2 * kk * thx)))
        Cn = C_cos(th_toy, v_toy, 2 * kk)
        Cm = C_cos(thx, wx, 2 * kk)
        QT2 = (Cn[0] + (Cn[2 * kk] if kk else Cn[0])) / (
            Cm[0] + (Cm[2 * kk] if kk else Cm[0]))
        if abs(num / den - QT2) > 1e-14:
            qt_ok = False
    check("G06-QT-is-C2k-ratio",
          qt_ok, "Q^T = (C0+C_{2k})_nu / (C0+C_{2k})_mu")

    xa = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    wa = np.array([0.2, 0.3, 0.4, 0.3, 0.2])
    ya = np.array([-0.75, -0.25, 0.25, 0.75])
    va = np.array([0.05, 0.15, 0.12, 0.08])
    a, b, h0 = V.mu_chain(xa, wa, 4)
    deg, npts = 3, 32
    xs = np.cos(PI * (np.arange(npts) + 0.5) / npts)
    u = np.ones_like(xs) / math.sqrt(h0)
    um = np.zeros_like(xs)
    for i in range(deg):
        r = (xs - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
    cf = chebfit(xs, u, deg)
    thy2 = np.arccos(np.clip(ya, -1.0, 1.0))
    pi_y = chebval(ya, cf)
    Q_direct = float(np.dot(va, pi_y * pi_y))
    Cnu = C_cos(thy2, va, 2 * deg)
    Q_w = 0.0
    for p in range(deg + 1):
        for q in range(deg + 1):
            Q_w += cf[p] * cf[q] * 0.5 * (Cnu[p + q] + Cnu[abs(p - q)])
    check("G07-OP-square-Weyl",
          abs(Q_direct - Q_w) / max(abs(Q_direct), 1e-30) < 1e-12,
          "Q_direct=%.8f Weyl=%.8f rel=%.3e" % (
              Q_direct, Q_w,
              abs(Q_direct - Q_w) / max(abs(Q_direct), 1e-30)))

    mz21 = two_period(21, C_FLANK)
    j = np.arange(1, 22)
    th_full = math.pi * j / 21.0
    w21 = np.where(j % 2 == 0,
                   (1.0 - np.cos(th_full)) * (math.pi / 21),
                   -C_FLANK * (1.0 - np.cos(th_full)) * (math.pi / 21))
    v_nu21 = np.where(w21 < 0, -w21, 0.0)
    rat21 = parseval_ratio(th_full, v_nu21, 21)
    check("G08-Parseval-two-period-S21",
          abs(rat21 - 1.0) < PARSEVAL_DEV,
          "sum|S_q|^2 / (2S Sigma v^2) = %.12f" % rat21)


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 / two-period / scramble")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    S = int(mz["S"])
    xp, wp, yn, vn = mz["xp"], mz["wp"], mz["yn"], mz["vn"]
    thn = np.arccos(np.clip(yn, -1.0, 1.0))
    thx = np.arccos(np.clip(xp, -1.0, 1.0))
    k_wall = N - 1
    C_nu = C_cos(thn, vn, max(400, 2 * S))
    Phi8 = energy_from_C(C_nu, 8)
    Phi8d = bilinear_K(thn, vn, 8)
    check("G10-w9-energy-k8",
          abs(Phi8 - Phi8d) / max(abs(Phi8), 1e-30) < 1e-12,
          "k=8 Phi=%.6f rel=%.3e" % (
              Phi8, abs(Phi8 - Phi8d) / max(abs(Phi8), 1e-30)))

    rat = parseval_ratio(thn, vn, S)
    check("G11-w9-Parseval",
          abs(rat - 1.0) < PARSEVAL_DEV,
          "ratio=%.12f (finite-grid Parseval SATZ)" % rat)

    sp = spec_pack(thn, vn, M=400)
    check("G12-w9-quadratic-mean",
          W9_MEANQM_LO < sp["mean_over_qm"] < W9_MEANQM_HI
          and sp["C_mass_max"] < 0.50,
          "mean/qm=%.3f max/qm=%.1f at m=%d |C|/mass max=%.3f "
          "(QM, not a comb, not PNT)" % (
              sp["mean_over_qm"], sp["max_over_qm"], sp["argmax"],
              sp["C_mass_max"]))

    Q, bch, _ = mu_Qk(xp, wp, yn, vn, k_wall)
    QT = qcheb_all(xp, wp, yn, vn, k_wall)
    g = bch ** 2
    fo12 = float(np.max(np.abs(g[-12:] * np.diff(Q[-13:]))))
    fot12 = float(np.max(np.abs(g[-12:] * np.diff(QT[-13:]))))
    check("G13-w9-FO-Chebyshev-closes",
          fo12 < W9_FO12_BAR and fo12 < CEPS
          and fot12 < W9_FOT12_BAR and fot12 < CEPS,
          "FO=%.5f FO^T=%.5f both < 1/32 (Chebyshev piece CLOSES "
          "at QM; dDelta is the live remainder)" % (fo12, fot12))

    aW, bW, h0W = V.mu_chain(xp, wp, k_wall)
    BW = V.b_matrix(aW, bW, h0W, yn, vn, k_wall)
    EW = BW @ BW.T
    lamW = float(np.linalg.eigvalsh(EW)[-1])
    maxdW = float(np.max(np.diag(EW)))
    assistW = lamW / maxdW - 1.0
    Phi_wall = energy_from_C(C_nu, k_wall)
    off_wall = Phi_wall - diag_K(thn, vn * vn, k_wall)
    sv = np.sqrt(vn)
    C_sv = C_cos(thn, sv, k_wall)
    ray_T = energy_from_C(C_sv, k_wall) / len(vn)
    check("G14-w9-wall-assist-not-allones",
          W9_ASSIST_LO < assistW < W9_ASSIST_HI
          and W9_MAXD_LO < maxdW < W9_MAXD_HI
          and lamW < 1.0
          and W9_PHI_WALL_LO < Phi_wall < W9_PHI_WALL_HI
          and off_wall < 0.0
          and ray_T < 0.20,
          "lam=%.6f maxd=%.4f assist=%.4f Phi_wall=%.4f off=%.4f "
          "Cheb-allones Rayleigh=%.4f << lam (wrong quadratic form)"
          % (lamW, maxdW, assistW, Phi_wall, off_wall, ray_T))

    try:
        import mpmath as mp
        mp.mp.dps = 30
        thm = [mp.mpf(float(t)) for t in thn]
        vm = [mp.mpf(float(v)) for v in vn]
        kmp = 8
        Phi_mp = mp.mpf(0)
        for i in range(len(vn)):
            for j in range(len(vn)):
                s = mp.mpf(1) / mp.pi
                for m in range(1, kmp):
                    s += (2 / mp.pi) * mp.cos(m * thm[i]) * mp.cos(
                        m * thm[j])
                Phi_mp += vm[i] * vm[j] * s
        C0 = sum(vm)
        accC = C0 * C0
        for m in range(1, kmp):
            Cm = sum(vm[i] * mp.cos(m * thm[i]) for i in range(len(vn)))
            accC += 2 * Cm * Cm
        Phi_mp2 = accC / mp.pi
        rel_mp = float(abs(Phi_mp - Phi_mp2) / abs(Phi_mp))
        check("G15-w9-mpmath-dps30",
              rel_mp < MP_BAR,
              "k=8 rel=%.3e" % rel_mp)
    except Exception as e:
        check("G15-w9-mpmath-dps30", False, "skip: %s" % e)

    mz23 = two_period(81, C_FLANK)
    th23 = np.arccos(np.clip(mz23["yn"], -1.0, 1.0))
    C_tp = C_cos(th23, mz23["vn"], 160)
    mass_t = float(np.sum(mz23["vn"]))
    h_tp = hhi(C_tp, 80)
    cs = abs(C_tp[81]) / max(mass_t, 1e-30)
    check("G16-two-period-is-a-comb",
          h_tp > TP_HHI_FLOOR and cs > TP_CS_FLOOR
          and abs(abs(C_tp[0]) / mass_t - 1.0) < 1e-12,
          "HHI=%.3f |C_S|/mass=%.3f (rho_AP=1 <=> spectral comb)"
          % (h_tp, cs))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    ths = np.arccos(np.clip(ds["ys"], -1.0, 1.0))
    C_scr = C_cos(ths, ds["vs"], 400)
    sp_s = spec_pack(ths, ds["vs"], M=400)
    dC = C_scr[1:401] ** 2 - C_nu[1:401] ** 2
    topm = int(np.argmax(np.abs(dC))) + 1
    check("G17-scramble-holds-QM-not-comb",
          SCR_MEANQM_LO < sp_s["mean_over_qm"] < W9_SCR_MEANQM_HI
          and sp_s["hhi"] < SCR_HHI_BAR
          and topm in SCR_DIV_MODES,
          "mean/qm=%.3f HHI=%.4f top|dC^2| m=%d (QM holds; "
          "dies on mu-OP remainder, not nu-Weyl concentration)"
          % (sp_s["mean_over_qm"], sp_s["hhi"], topm))

    C_eq = C_cos(thn, np.ones_like(vn), 200)
    qm_eq = 0.5 * float(len(vn))
    mean_eq = float(np.mean(C_eq[1:201] ** 2)) / max(qm_eq, 1e-30)
    sp200 = spec_pack(thn, vn, M=200)
    check("G18-weights-do-not-buy-cancellation",
          sp200["mean_over_qm"] > mean_eq + EQ_GAP,
          "weighted mean/qm=%.3f equal=%.3f (von Mangoldt is "
          "CLOSER to QM than equal weight)" % (
              sp200["mean_over_qm"], mean_eq))

    # Z_loc Chebyshev proxy is NOT the r386 0.055
    kZ = N - 2
    z_full = 0.5 * float(np.dot(
        vn, np.cos(thn) * (1.0 + np.cos(2 * kZ * thn))))
    z_abs = 0.5 * float(np.dot(
        np.abs(vn), np.abs(np.cos(thn) * (1.0 + np.cos(2 * kZ * thn)))))
    zc = abs(z_full) / max(z_abs, 1e-30)
    check("G19-Z-proxy-is-not-uniform-cancel",
          zc > 0.30 and zc < 0.70,
          "Chebyshev x T_k^2 cancel=%.3f != r386 median 0.055 "
          "(Z_loc is the edge-masked drive, not this proxy)"
          % zc)

    if smoke:
        return

    section("S3  FULL CENSUS -- core-42 / EXT-heavy / chi3")
    core = list(V.admissible_indices())
    check("G20-ladder-size",
          len(core) == CORE_N, "core %d" % len(core))

    rows = []
    fo_true, fo_T = [], []
    for kz in core:
        m = V.build_measures(kz)
        th = np.arccos(np.clip(m["yn"], -1.0, 1.0))
        r = spec_pack(th, m["vn"], M=200)
        r["kz"] = kz
        r["N"] = int(m["Nw"])
        rows.append(r)
        Nv = int(m["Nw"])
        if Nv <= 220:
            Qk, bb, _ = mu_Qk(m["xp"], m["wp"], m["yn"], m["vn"], Nv - 1)
            QT_ = qcheb_all(m["xp"], m["wp"], m["yn"], m["vn"], Nv - 1)
            g_ = bb ** 2
            fo_true.append(float(np.max(np.abs(g_[-12:] * np.diff(Qk[-13:])))))
            fo_T.append(float(np.max(np.abs(g_[-12:] * np.diff(QT_[-13:])))))
    moq = [r["mean_over_qm"] for r in rows]
    cm = [r["C_mass_max"] for r in rows]
    hh = [r["hhi"] for r in rows]
    check("G21-CORE42-quadratic-mean",
          CORE_MEANQM_LO <= min(moq) and max(moq) <= CORE_MEANQM_HI,
          "mean/qm in [%.3f, %.3f]" % (min(moq), max(moq)))
    check("G22-CORE42-trivial-Weyl-not-PNT",
          max(cm) < CORE_CMASS_HI,
          "|C|/mass max in [%.3f, %.3f] < 1/2 (trivial Weyl)"
          % (min(cm), max(cm)))
    check("G23-CORE42-HHI-not-a-comb",
          max(hh) < CORE_HHI_HI,
          "HHI in [%.4f, %.4f] < 0.12 (two-period is 0.73)"
          % (min(hh), max(hh)))
    check("G24-smallN-FO-and-FOT-close",
          len(fo_true) == SMALLN_FO_N
          and max(fo_true) < CEPS
          and max(fo_T) < SMALLN_FOT_BAR,
          "n=%d max|FO|=%.5f max|FO^T|=%.5f both < 1/32"
          % (len(fo_true), max(fo_true), max(fo_T)))

    ext_cm, ext_hh = [], []
    for kz in HEAVY7:
        m = V.build_measures(kz)
        th = np.arccos(np.clip(m["yn"], -1.0, 1.0))
        r = spec_pack(th, m["vn"], M=200)
        ext_cm.append(r["C_mass_max"])
        ext_hh.append(r["hhi"])
    check("G25-EXT7-trivial-Weyl",
          max(ext_cm) < EXT_CMASS_HI,
          "|C|/mass max in [%.3f, %.3f] < 0.40; HHI in [%.3f, %.3f] "
          "(flank-mass, not a two-period comb)"
          % (min(ext_cm), max(ext_cm), min(ext_hh), max(ext_hh)))

    cmoq = []
    for kz in core:
        uu, ww, _, _ = DMF.chi_window_comb(kz, DMF.Q_CHI3)
        mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ3)
        thc = np.arccos(np.clip(mzc["yn"], -1.0, 1.0))
        r = spec_pack(thc, mzc["vn"], M=200)
        cmoq.append(r["mean_over_qm"])
    check("G26-CHI3-42-quadratic-mean",
          len(cmoq) == CHI3_N
          and CHI_MEANQM_LO <= min(cmoq)
          and max(cmoq) <= CHI_MEANQM_HI,
          "chi3 mean/qm in [%.3f, %.3f] (same class as MAIN)"
          % (min(cmoq), max(cmoq)))
    check("G27-HHI-mutant-two-period-separates",
          max(hh) < 0.12 and h_tp > 0.50,
          "core HHI max=%.4f << TP %.3f (spectral rho_AP)"
          % (max(hh), h_tp))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("weyl_energy_probe -- LEMMA.WEYL_ENERGY.01 (round 389)")
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
    tag = "WEYL ENERGY SMOKE" if smoke else "WEYL ENERGY"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
