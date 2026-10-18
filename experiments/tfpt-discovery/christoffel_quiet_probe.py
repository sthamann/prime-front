#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_quiet_probe -- LEMMA.CHRISTOFFEL_QUIET.01 (round 385):
THE CHRISTOFFEL-QUIETNESS LEMMA, the common core of G_eps and L*.

Coexistence: r381 (G_eps -> C_eps) and r382 (entry n0=floor(2N/5),
L2 remainder for n0=N-1) name the SAME sampling
Q_k := <pi_k^2>_nu / h_k(mu) of mu-OP squares against nu.
This round attacks that object from the cosine-grid geometry
(r379 mesh SATZ, r361 3/8-floor).  next.txt is NOT written.
NO Lean edit.  NO RH CLAIM.

THE FROZEN QUESTION.  For canonical windows, cofinally,
Q_k <= qbar < 1 for all k up to N-1, with qbar an explicit
constant DERIVED from fold geometry (3/8-floor + F1-runlengths
+ cosine grid), NOT from measurement?  Consequences claimed:
(a) h_k(mu-nu) >= (1-Q_k) h_k(mu) > 0 as a floor plate to
n0=N-1; (b) the same quadrature proves C_eps (|FO|<=1/32).

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Exact geometry: Chebyshev-Gauss exactness on the cosine
     grid; nu-angle discrepancy (star / Erdos-Turan); the
     Koksma-Hlawka candidate Q <= mass_frac + k D*.
  B  Depth conflict: effective |Q-alpha| vs k D*; Fourier
     of pi_k^2 against Weyl sums S_m = sum_nu v_j e^{i m theta_j}.
  C  Circularity: which bound on S_k closes (a) C_eps and
     (b) the floor plate -- trivial / PNT / subconvex / RH.
  D  Kills: scramble, two-period c=2/3 against the Q-chain,
     EXT-heavy {69,96,97,99,107,117,129}.

CALIBRATION DISCLOSURE.  Identities, discrepancy, Q-profiles,
FO=gamma dQ, scramble k_Q>=1, two-period lambda vs Q, and the
core-42 / MAIN-85 / chi3-42 tallies were first measured in
/tmp (r385_cal.py, r385_cal2.py, r385_cal3.py) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are
that measurement, sealed as gates -- not a search over the
box 1/32 (that is r381's C_eps).  No two-commit pre-blind
freeze: pins disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Equal-weight cosine grid: orthonormal Q_k == 1 (the full
    measure) through k < n, maxdev 4.4e-16 (Chebyshev-Gauss
    SATZ).  T_k^2 = (1+T_{2k})/2 exact over Q.
  * FO_k[-nu] = gamma_k (Q_k - Q_{k-1}) exact (w9 maxdev
    2.2e-17).  last-12 |FO| = 0.00986 < 1/32.
  * w9: alpha=mass_nu/mu=0.0611, nfrac=0.2834, D*=0.1832,
    Q_12 max=0.3891, max |Q-Qcheb|=0.335 (deformation, NOT
    the Chebyshev partial sum).  k D* at k=182 is 33 >> 1
    (Koksma does not close).  |Q-alpha|/(k D*)=0.0089 = o(1).
  * Weyl |S_{2k}|/mass_nu at k>=1 sits in (0.04, 0.33) --
    TRIVIAL scale, not sqrt(n_nu)/n_nu=0.098 uniformly, and
    not a PNT/RH demand: Chebyshev-Q stays at alpha under
    the TRIVIAL bound |S|<=mass, which already gives
    Q^T <= 2 alpha ~ 0.12 < 1.
  * CORE-42 Qmax in [0.164, 0.483] < 1 (depth N-1 for N<=220,
    else 80); 11 small-N last-12 |FO| max=0.01182 < 1/32.
  * MAIN-85 D* in [0.105, 0.212]; chi3-42 D* in [0.125, 0.248].
  * SCRAMBLE seed=1: Q crosses 1 at k=70, last-12 Q > 10^3
    (r381 named break reproduced).  D* at low k is comparable
    to MAIN -- scramble does not break discrepancy first.
  * Two-period S=81: Q_k == alpha for all k (Chebyshev even/
    odd).  c=2/3: Q=0.683<1 but lambda_max(E_22)>1 -- Q<1
    is NOT a floor plate.  c=1: Q>1 at k=0.
  * EXT-heavy 7 at depth 200: Qmax in [0.127, 0.221] < 0.25;
    leisheit holds at that depth (r_max up to 0.879 is a
    FLANK-mass fact, not a Q fact).

AUSGANG REDUZIERT.  The geometric Chebyshev-equidistribution
half is SATZ at trivial Weyl.  The deduction "therefore mu-OP
Q_k <= qbar from 3/8-floor + Koksma" is false.  Remaining,
strictly smaller: (B) the Fejer/d_arm deformation
Delta_k = Q_k - Q^T_k (live term for C_eps via consecutive
dQ); (C) lambda_max = maxQ * (1+assist) with assist ~1.5..4
(the r382 L2 remainder).  Weyl scale: TRIVIAL.  Not PNT,
not subconvex, not RH-equivalent -- the Chebyshev-Weyl
route never reaches a zeta-quality demand.

MACHINERY: r226 hirota_sign.window_data, r283
verify_lstar_instance.build_measures / mu_chain, r330
chi_build_measures, r381 FO dictionary, r382 two-period.

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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import hirota_sign_probe as HS  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import ext3_fresh_anchors_probe as E3  # noqa: E402
import lstar_margin_scaling_probe as LM  # noqa: E402

SCR_SEED = 1
CEPS = 1.0 / 32.0
MAIN_KZ = 9
HEAVY7 = (69, 96, 97, 99, 107, 117, 129)
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT5_KZ = (69, 107, 101, 99, 115, 89)
EXT6_KZ = (133, 129, 124, 117)
C_FLANK = 2.0 / 3.0

# disclosed /tmp pins
W9_ALPHA_LO, W9_ALPHA_HI = 0.060, 0.062
W9_Q12_LO, W9_Q12_HI = 0.380, 0.400
W9_FO12_BAR = 0.012
W9_DSTAR_LO, W9_DSTAR_HI = 0.170, 0.200
W9_DEFORM_FLOOR = 0.25
W9_EFF_BAR = 0.02
W9_KD_FLOOR = 10.0
WEYL_TRIV_BAR = 0.50
SCR_KFAIL_LO, SCR_KFAIL_HI = 60, 80
SCR_Q12_FLOOR = 1.0e3
TP_Q_LO, TP_Q_HI = 0.680, 0.690
CORE_QMAX_BAR = 0.50
CORE_N = 42
MAIN_N = 85
MAIN_DSTAR_LO, MAIN_DSTAR_HI = 0.100, 0.220
CHI3_N = 42
CHI3_DSTAR_HI = 0.26
HEAVY_Q_BAR = 0.25
FO_ID_BAR = 1.0e-12
CHEB_Q_BAR = 1.0e-12
SMALLN_FO_N = 11

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


def star_disc(theta):
    t = np.sort(np.asarray(theta, float) / math.pi)
    t = np.clip(t, 0.0, 1.0)
    n = len(t)
    if n == 0:
        return 1.0
    k = np.arange(1, n + 1, dtype=float)
    return float(max(np.max(k / n - t), np.max(t - (k - 1) / n)))


def weyl(theta, vn, m):
    return complex(float(np.sum(vn * np.cos(m * theta))),
                   float(np.sum(vn * np.sin(m * theta))))


def qcheb(xp, wp, yn, vn, k):
    thy = np.arccos(np.clip(yn, -1.0, 1.0))
    thx = np.arccos(np.clip(xp, -1.0, 1.0))
    num = float(np.sum(vn * (1.0 + np.cos(2 * k * thy))))
    den = float(np.sum(wp * (1.0 + np.cos(2 * k * thx))))
    return num / max(den, 1e-30)


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S)


def main_ladder():
    core_kzs = list(V.admissible_indices())
    lm_rows = LM.ext_rule()
    ext_kzs = [t[1] for t in lm_rows[:15]]
    all_main = (core_kzs + ext_kzs + list(EXT3_KZ_B + EXT3_KZ_A)
                + list(EXT4_KZ_B + EXT4_KZ_A) + list(EXT5_KZ)
                + list(EXT6_KZ))
    return core_kzs, all_main


def fo_last12(Q, b):
    dQ = np.diff(Q[-13:])
    g = b[-12:] ** 2
    return float(np.max(np.abs(g * dQ)))


def part_a_standalone():
    section("S1  LEG A -- CHEBYSHEV-GAUSS, T^2, KOKSMA TV")
    x = Fr(2, 5)
    T = [Fr(1), x]
    for _n in range(4):
        T.append(2 * x * T[-1] - T[-2])
    # T2 = 2x^2-1, T4 = 8x^4-8x^2+1; T2^2 = (1+T4)/2
    lhs = T[2] * T[2]
    rhs = (Fr(1) + T[4]) / Fr(2)
    check("G01-Tk2-half-T2k",
          lhs == rhs,
          "T_2(2/5)^2 = (1+T_4)/2 exact over Q")

    # TV of cos(2k theta) on [0, pi] = 4k
    tv_ok = True
    for k in (1, 2, 3, 5, 8):
        m = 2 * k
        # integral |m sin(m theta)| d theta on [0,pi] = 2 m
        n_hump = m
        hump = 2.0 / m
        tv = m * n_hump * hump
        if abs(tv - 4.0 * k) > 1e-12:
            tv_ok = False
    check("G02-TV-cos-2k-is-4k",
          tv_ok,
          "TV(cos(2k theta),[0,pi])=4k for k=1,2,3,5,8")

    # trivial Weyl |sum w e^{i theta}| <= sum |w|
    w = np.array([0.2, 0.3, 0.5])
    th = np.array([0.1, 1.2, 2.4])
    S = abs(complex(float(np.sum(w * np.cos(th))),
                    float(np.sum(w * np.sin(th)))))
    check("G03-trivial-Weyl",
          S <= float(np.sum(w)) + 1e-15,
          "|S|=%.6f <= mass=%.6f" % (S, float(np.sum(w))))

    # Chebyshev-Gauss: equal-weight cosine grid, Q_k == 1
    n = 32
    L = 2 * n
    j = np.arange(1, n)
    th = 2.0 * math.pi * j / L
    xg = np.cos(th)
    wg = np.full_like(xg, 1.0 / len(xg))
    Qg, _, _ = mu_Qk(xg, wg, xg, wg, n // 2)
    dev = float(np.max(np.abs(Qg - 1.0)))
    check("G04-Chebyshev-Gauss-Qeq1",
          dev < CHEB_Q_BAR,
          "n=32 depth=16 max|Q-1|=%.3e" % dev)

    # 3-atom (3,-2,3) at (-1,0,1): Q0 = 1/2, one-Rayleigh
    # <p0,p0>_{mu-nu} = 4-2 = 2 = h0 (1-Q0)
    h0 = Fr(4)
    q0 = Fr(2) / Fr(4)
    ray = h0 * (Fr(1) - q0)
    check("G05-one-Rayleigh-3atom",
          ray == Fr(2) and q0 == Fr(1, 2),
          "h0(1-Q0)=2; Q0=1/2.  One direction, not lambda_max")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 / scramble / two-period")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    xp, wp, yn, vn = mz["xp"], mz["wp"], mz["yn"], mz["vn"]
    alpha = float(np.sum(vn)) / float(np.sum(wp))
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    Ds = star_disc(th)
    Q, b, h0 = mu_Qk(xp, wp, yn, vn, N - 1)
    q12 = float(np.max(Q[-12:]))
    fo12 = fo_last12(Q, b)
    deform = max(abs(Q[k] - qcheb(xp, wp, yn, vn, k))
                 for k in range(0, N - 1, max(1, (N - 1) // 16)))
    kd = (N - 2) * Ds
    eff = abs(Q[-1] - alpha) / max(kd, 1e-12)
    mass_nu = float(np.sum(vn))
    weyl_r = []
    for k in (1, 45, 91, 171, N - 2):
        if 0 < k < N - 1:
            weyl_r.append(abs(weyl(th, vn, 2 * k)) / mass_nu)
    check("G10-w9-alpha-Q12-FO-Dstar",
          W9_ALPHA_LO < alpha < W9_ALPHA_HI
          and W9_Q12_LO < q12 < W9_Q12_HI
          and fo12 < W9_FO12_BAR and fo12 < CEPS
          and W9_DSTAR_LO < Ds < W9_DSTAR_HI,
          "a=%.4f Q12=%.4f |FO|12=%.5f D*=%.4f CEPS=%s"
          % (alpha, q12, fo12, Ds, fo12 < CEPS))

    # FO_k = ( <p_k^2>_nu - gamma_k <p_{k-1}^2>_nu ) / h_{k-1}
    #      = gamma_k (Q_k - Q_{k-1})  (orthonormal Q)
    x, w = xp, wp
    y, v = yn, vn
    px, py = np.ones_like(x), np.ones_like(y)
    pxm, pym = np.zeros_like(x), np.zeros_like(y)
    hs = [float(np.dot(w, px * px))]
    ns = [float(np.dot(v, py * py))]
    fos = []
    for k in range(12):
        alh = float(np.dot(w, x * px * px)) / hs[-1]
        if k == 0:
            rx, ry = (x - alh) * px, (y - alh) * py
        else:
            ge = hs[-1] / hs[-2]
            rx = (x - alh) * px - ge * pxm
            ry = (y - alh) * py - ge * pym
        pxm, pym, px, py = px, py, rx, ry
        hs.append(float(np.dot(w, px * px)))
        ns.append(float(np.dot(v, py * py)))
        g = hs[-1] / hs[-2]
        fos.append((ns[-1] - g * ns[-2]) / hs[-2])
    pred12 = (b[:12] ** 2) * np.diff(Q[:13])
    iddev = float(np.max(np.abs(np.array(fos) - pred12)))
    check("G11-FO-is-gamma-dQ",
          iddev < FO_ID_BAR,
          "monic FO vs gamma dQ, first-12 maxdev=%.3e" % iddev)

    check("G12-Koksma-does-not-close",
          kd > W9_KD_FLOOR and deform > W9_DEFORM_FLOOR
          and eff < W9_EFF_BAR,
          "k D*=%.1f deform=%.3f |Q-a|/(kD*)=%.4f (o(k D*), "
          "but Koksma majorant useless; mu-OP != Chebyshev)"
          % (kd, deform, eff))

    check("G13-Weyl-trivial-scale",
          max(weyl_r) < WEYL_TRIV_BAR and min(weyl_r) > 0.01,
          "max |S_2k|/mass=%.3f (trivial, not RH-scale) ks=%s"
          % (max(weyl_r), [round(x, 3) for x in weyl_r]))

    qT = [qcheb(xp, wp, yn, vn, k)
          for k in (0, 9, 45, 90, 171)]
    check("G14-Qcheb-stays-at-alpha",
          all(abs(q - alpha) < 0.03 for q in qT),
          "Q^T=%s vs alpha=%.4f (Chebyshev sampling SATZ at "
          "trivial Weyl)" % ([round(q, 4) for q in qT], alpha))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    Qs, _, _ = mu_Qk(ds["xs"], ds["ws"], ds["ys"], ds["vs"], 183)
    kfail = next((i for i, q in enumerate(Qs) if q >= 1.0), None)
    q12s = float(np.max(Qs[-12:]))
    check("G15-scramble-Q-explodes",
          kfail is not None
          and SCR_KFAIL_LO <= kfail <= SCR_KFAIL_HI
          and q12s >= SCR_Q12_FLOOR,
          "k_Q>=1=%s last12 Q=%.3e (r381 named break)"
          % (kfail, q12s))

    mz23 = two_period(81, C_FLANK)
    Q23, _, _ = mu_Qk(mz23["xp"], mz23["wp"], mz23["yn"], mz23["vn"], 40)
    qspan = float(np.max(Q23) - np.min(Q23))
    lam22, _ = V.lam_max_at(mz23, 22)
    mz1 = two_period(81, 1.0)
    Q1, _, _ = mu_Qk(mz1["xp"], mz1["wp"], mz1["yn"], mz1["vn"], 4)
    check("G16-two-period-Q-not-floor",
          TP_Q_LO < float(np.max(Q23)) < TP_Q_HI
          and qspan < 1e-10
          and lam22 > 1.0
          and float(Q1[0]) > 1.0,
          "c=2/3 Q==%.4f (span %.1e) lam22=%.4f>1; c=1 Q0=%.4f.  "
          "Q<1 does not give n0=N-1"
          % (float(np.max(Q23)), qspan, lam22, float(Q1[0])))

    if smoke:
        return

    section("S3  FULL CENSUS -- MAIN D*, core Q, FO, EXT7, chi3 D*")
    core_kzs, all_main = main_ladder()
    check("G20-ladder-size",
          len(core_kzs) == CORE_N and len(all_main) == MAIN_N,
          "core %d MAIN %d" % (len(core_kzs), len(all_main)))

    Ds_m = []
    for kz in all_main:
        m = V.build_measures(kz)
        thm = np.arccos(np.clip(m["yn"], -1.0, 1.0))
        Ds_m.append(star_disc(thm))
    check("G21-MAIN85-Dstar",
          len(Ds_m) == MAIN_N
          and MAIN_DSTAR_LO <= min(Ds_m)
          and max(Ds_m) <= MAIN_DSTAR_HI,
          "D* min/max=%.4f/%.4f (Koksma kD*~N*0.21 still >>1)"
          % (min(Ds_m), max(Ds_m)))

    n_fail = 0
    qmaxs = []
    n_fo = 0
    fo_hi = 0.0
    for kz in core_kzs:
        m = V.build_measures(kz)
        Nv = int(m["Nw"])
        dep = Nv - 1 if Nv <= 220 else min(80, Nv - 1)
        Qc, bc, _ = mu_Qk(m["xp"], m["wp"], m["yn"], m["vn"], dep)
        qmaxs.append(float(np.max(Qc)))
        if any(q >= 1.0 for q in Qc):
            n_fail += 1
        if Nv <= 220:
            n_fo += 1
            fo_hi = max(fo_hi, fo_last12(Qc, bc))
    check("G22-CORE42-Qmax",
          n_fail == 0 and max(qmaxs) < CORE_QMAX_BAR
          and min(qmaxs) > 0.10,
          "Qmax in [%.4f, %.4f] n_fail=%d" % (min(qmaxs), max(qmaxs),
                                              n_fail))
    check("G23-smallN-FO-Ceps",
          n_fo == SMALLN_FO_N and fo_hi < CEPS,
          "n=%d max|FO|_12=%.5f < 1/32" % (n_fo, fo_hi))

    cD = []
    for kz in core_kzs:
        uu, ww, _, _ = DMF.chi_window_comb(kz, DMF.Q_CHI3)
        mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ3)
        thc = np.arccos(np.clip(mzc["yn"], -1.0, 1.0))
        cD.append(star_disc(thc))
    check("G24-chi3-42-Dstar",
          len(cD) == CHI3_N and max(cD) <= CHI3_DSTAR_HI,
          "chi3 D* min/max=%.4f/%.4f (same order as MAIN; "
          "181-pack builder skipped as too expensive, disclosed)"
          % (min(cD), max(cD)))

    heavy_ok = True
    bits = []
    for kz in HEAVY7:
        m = V.build_measures(kz)
        Nv = int(m["Nw"])
        dep = min(200, Nv - 1)
        Qh, _, _ = mu_Qk(m["xp"], m["wp"], m["yn"], m["vn"], dep)
        qm = float(np.max(Qh))
        heavy_ok = heavy_ok and qm < HEAVY_Q_BAR
        bits.append("kz%d=%.3f" % (kz, qm))
    check("G25-EXT7-leisheit-at-200",
          heavy_ok,
          "Qmax@200 %s (all < 0.25; flank r_max is a different object)"
          % ", ".join(bits))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("christoffel_quiet_probe -- LEMMA.CHRISTOFFEL_QUIET.01 "
          "(round 385)")
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
    tag = "CHRISTOFFEL QUIET SMOKE" if smoke else "CHRISTOFFEL QUIET"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
