#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sign_schur_probe -- LEMMA.SIGN_SCHUR.01 (round 394):
THE SIGN BINDING OF THE UVAROV IMAGE, after r392 named the
99.7% Assist cancellation as the off-diagonal signs of
K^mu[Xi].

Coexistence: r392 proved the Uvarov gamma-ratio and located
cancellation in sign(K^mu[Xi]), not in the positive tau-
quotients.  r387 killed Gershgorin (gA=13.32 vs assist 0.0399)
and named two-period as a global AP.  r389 placed the nu-angles
at quadratic-mean and left the mu-OP Gram as the live object.
This round asks whether that sign pattern is a SOURCE-DEFINED
checkerboard / rank-1 conjugacy (M-matrix / Schur) that forces
lambda_max(E_k) <= maxdiag*(1+o(1)).

THE FROZEN QUESTION.  Does sign(K^mu_k(x_i,x_j)) along the
ordered nu-nodes admit a source-defined sigma with
sigma_i sigma_j K_ij <= 0 for almost all pairs, and does that
conjugation bound lambda_max(E_k) < 1 past the r382 entry
2N/5?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Sign map.  Chebyshev-CD signs on the cosine grid are
     Dirichlet-zonal (SATZ).  Is the nu-node map checkerboard
     in index order?  Does mu-CD inherit Chebyshev signs
     (tau-deformation small, r392)?
  B  Map to a bound.  Rank-1 conjugation D_sigma E D_sigma to
     a Z-matrix; hoped M-matrix bound lambda <= maxdiag.
     Fraction of violating pairs, source vs adversaries.
  C  Theorem attempt.  F1-runs + separation + rho_AP =>
     conjugacy up to a controlled rest => lambda_max < 1 to
     some k* > 2N/5 (would improve r382 entry).
  D  Kills: two-period in-phase off-diagonals; scramble
     (dDelta = 2.16e6, r388); mutant |E| (signs dropped).

CALIBRATION DISCLOSURE.  Dirichlet identities, w9 sign map /
mass-weighted Chebyshev agree / checkerboard / oracle
conjugation / |E| mutant, two-period lag-1, scramble seed=1,
and the core-42 census were first measured in /tmp
(r394_cal.py, r394_cal2.py, r394_cal3.py) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are
that measurement, sealed as gates.  No two-commit pre-blind
freeze: pins disclosed.  Builder fallback: core-42 only
(finished in 1 s; no 181-pack).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Dirichlet sign identity on S=16 n=7: True.
    Envelope |D_n(a)| <= min(2n+1, 1/|sin(a/2)|) exact.
    Chebyshev-K vs difference-Dirichlet sign agree 0.875 on
    that grid (reflected sum term flips ~1/8).
  * 2x2 Z-matrix [[1,-c],[-c,1]] has lambda=1+c > maxdiag:
    conjugation to negative off-diagonals does NOT imply
    lambda <= maxdiag (hoped M-bound FALSE in general).
  * w9 k=183: lam=0.999830 maxd=0.9614 assist=0.0399 gA=13.32
    canc=0.9970 (r387/r392 reproduced).  Chebyshev pair-count
    agree uw=0.721; mass-weighted ww=0.810.  Checkerboard ww
    =0.504 (coin).  NN neg_share=0.468 (not an M-path).
    lambda(|E|)=1.683>1 (unsigned Gershgorin 2.04).
    last-12 Cheb ww in [0.801, 0.829], uw in [0.648, 0.721].
    entry k=73 Cheb ww=0.787, CB ww=0.408, NN neg_share=0.039
    (nearest neighbours CONSTRUCTIVE at entry).
  * Oracle (true top-evec) conjugation at the wall: pos_share
    =0.389, bound_pos=1.90>1 -- even knowing sigma, the
    residual positive remainder does not close lambda<1.
  * Two-period S=81 c=2/3: k=22 NN 40/0 all positive, lam=
    1.0288>1 (in-phase kill).  k=40 Cheb agree=1 and -CB
    agree=1 (perfect anti-checkerboard TOO LATE: maxd=1.317).
  * Scramble seed=1 k=183: Cheb ww=0.788 HOLDS, lam=9.17e6
    (envelope / occupation kill, not a sign-map break).
  * Core-42 wall: 42/42 lam<1; Cheb ww in [0.810, 0.894];
    CB ww in [0.429, 0.512]; NN neg_share in [0.349, 0.543];
    assist in [0.0083, 0.0814].

AUSGANG REDUZIERT.  SATZ: Dirichlet zonal signs and envelope
of Chebyshev-CD on the cosine grid; the 2x2 Z-matrix bound
is false; two-period lag-1 is in-phase.  REFUTED: checkerboard
/ rank-1 conjugability as the Assist mechanism (mass-weighted
agree 1/2 on MAIN and on core-42).  CENSUS: mass-weighted
Chebyshev-sign inheritance 81-89% at the wall (pair-count
only 65-75%: small entries flip).  NOT proved: source-defined
conjugacy => lambda_max<1 to any k*>2N/5; the sign-majorant
crosses 1 at or before the r382 entry.  Remaining: the
Dirichlet/Abel (Weyl) energy of the mu-OP Gram (r389 rest) --
Sign-Schur as a bipartition is the wrong language.  V3' /
F_eps / d2 log tau untouched.

MACHINERY: r226 hirota_sign.window_data, r283
verify_lstar_instance.build_measures / mu_chain / b_matrix,
r387 Chebyshev-Dirichlet CD and two_period, r392 Uvarov image.

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
import coherence_assist_probe as CA  # noqa: E402

PI = math.pi
MAIN_KZ = 9
SCR_SEED = 1
C_FLANK = 2.0 / 3.0
CORE_N = 42

# disclosed /tmp pins
W9_ASSIST_LO, W9_ASSIST_HI = 0.030, 0.050
W9_CANC_FLOOR = 0.99
W9_CHEB_WW = (0.78, 0.85)
W9_CHEB_UW = (0.65, 0.80)
W9_CB_WW = (0.45, 0.56)
W9_NN_NEG = (0.40, 0.55)
W9_LAMABS = (1.50, 1.90)
W9_LAST12_WW_LO = 0.78
W9_ENTRY_WW_LO = 0.75
ORACLE_BND_FLOOR = 1.0
SCR_WW_LO = 0.70
SCR_LAM_FLOOR = 2.0
CORE_CHEB_WW = (0.79, 0.92)
CORE_CB_WW = (0.40, 0.55)
CORE_NN_NEG = (0.30, 0.60)
CORE_ASSIST_HI = 0.10
ENV_BAR = 1.0e-10
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


def dirichlet(n, a):
    a = np.asarray(a, float)
    out = np.empty_like(a, dtype=float)
    s = np.sin(a / 2.0)
    small = np.abs(s) < 1e-14
    out[small] = 2 * n + 1
    out[~small] = np.sin((n + 0.5) * a[~small]) / s[~small]
    return out


def cheb_K_mat(n, th):
    th = np.asarray(th, float)
    dth = th[:, None] - th[None, :]
    sth = th[:, None] + th[None, :]
    return (dirichlet(n - 1, dth) + dirichlet(n - 1, sth)) / (2.0 * PI)


def zone_sign(n, th):
    """sign of the difference-Dirichlet D_{n-1}(theta_i - theta_j)."""
    dth = np.asarray(th)[:, None] - np.asarray(th)[None, :]
    mD = n - 1
    den = np.sin(dth / 2.0)
    num = np.sin((mD + 0.5) * dth)
    S = np.sign(num) * np.sign(den)
    S[np.abs(dth) < 1e-14] = 0.0
    S[np.abs(den) < 1e-14] = np.sign(2 * mD + 1)
    np.fill_diagonal(S, 0.0)
    return S


def checkerboard(m):
    s = np.ones(m)
    s[1::2] = -1.0
    S = np.outer(s, s)
    np.fill_diagonal(S, 0.0)
    return S, s


def mass_agree(E, Spred):
    m = E.shape[0]
    iu = np.triu_indices(m, 1)
    se = np.sign(E[iu])
    sp = np.sign(Spred[iu]) if Spred.ndim == 2 else Spred
    mag = np.abs(E[iu])
    both = (se != 0) & (sp != 0)
    if not np.any(both):
        return float("nan"), float("nan")
    eq = se[both] == sp[both]
    uw = float(np.mean(eq))
    ww = float(np.sum(mag[both] * eq) / np.sum(mag[both]))
    return uw, ww


def order_by_theta(yn, vn, B=None):
    th = np.arccos(np.clip(np.asarray(yn, float), -1.0, 1.0))
    o = np.argsort(th)
    if B is not None:
        B = B[o]
    return th[o], np.asarray(yn, float)[o], np.asarray(vn, float)[o], B


def E_from_B(B, k):
    return B[:, :k] @ B[:, :k].T


def gram_stats(E):
    diag = np.diag(E).copy()
    maxd = float(np.max(diag))
    lam = float(np.linalg.eigvalsh(E)[-1])
    off = np.abs(E).copy()
    np.fill_diagonal(off, 0.0)
    gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
    gersh = float(np.max(diag + off.sum(axis=1)))
    lam_abs = float(np.linalg.eigvalsh(np.abs(E))[-1])
    assist = lam / maxd - 1.0 if maxd > 0 else 0.0
    canc = 1.0 - assist / max(gA, 1e-12)
    return dict(lam=lam, maxd=maxd, assist=assist, gA=gA, gersh=gersh,
                lam_abs=lam_abs, canc=canc)


def nn_neg_share(E):
    m = E.shape[0]
    nn = np.array([E[i, i + 1] for i in range(m - 1)])
    mag = np.abs(nn)
    n_neg = int(np.sum(nn < 0))
    n_pos = int(np.sum(nn > 0))
    share = float(np.sum(np.maximum(-nn, 0.0)) / max(float(np.sum(mag)), 1e-30))
    return n_neg, n_pos, share


def oracle_bound(E):
    w, U = np.linalg.eigh(E)
    sig = np.sign(U[:, -1])
    sig[sig == 0] = 1.0
    A = E * np.outer(sig, sig)
    diag = np.diag(A).copy()
    pos = np.maximum(A, 0.0)
    np.fill_diagonal(pos, 0.0)
    bound = float(np.max(diag + pos.sum(axis=1)))
    abs_off = np.abs(A).copy()
    np.fill_diagonal(abs_off, 0.0)
    pos_share = float(np.sum(pos) / max(float(np.sum(abs_off)), 1e-30))
    return bound, pos_share


def dirichlet_sign_ok(S=16, nK=7):
    j = np.arange(1, S)
    th = PI * j / S
    dth = th[:, None] - th[None, :]
    mD = nK - 1
    Ddiff = dirichlet(mD, dth)
    den = np.sin(dth / 2.0)
    pred = np.sign(np.sin((mD + 0.5) * dth)) * np.sign(den)
    pred[np.abs(den) < 1e-14] = np.sign(2 * mD + 1)
    mask = np.abs(dth) > 1e-12
    return bool(np.all(np.sign(Ddiff)[mask] == pred[mask]))


def dirichlet_envelope_ok():
    mx = 0.0
    for n in (3, 8, 20, 50):
        a = np.linspace(-PI + 1e-3, PI - 1e-3, 400)
        D = dirichlet(n, a)
        env = np.minimum(2 * n + 1, 1.0 / np.abs(np.sin(a / 2.0)))
        if np.any(np.abs(D) > env + ENV_BAR):
            return False, 1.0
        mx = max(mx, float(np.max(np.abs(D) / env - 1.0)))
    return True, mx


def sign_pack(E, th, k):
    """Cheb / CB / NN / gram / oracle on a theta-ordered E."""
    Kc = cheb_K_mat(k, th)
    Scb, _s = checkerboard(E.shape[0])
    uw_c, ww_c = mass_agree(E, Kc)
    uw_b, ww_b = mass_agree(E, Scb)
    n_neg, n_pos, nn_share = nn_neg_share(E)
    gs = gram_stats(E)
    bnd, psh = oracle_bound(E)
    return dict(uw_c=uw_c, ww_c=ww_c, uw_b=uw_b, ww_b=ww_b,
                nn_neg=n_neg, nn_pos=n_pos, nn_share=nn_share,
                gs=gs, oracle_bnd=bnd, oracle_psh=psh)


def part_a_standalone():
    section("S1  LEG A -- DIRICHLET SIGNS, ENVELOPE, Z-MATRIX COUNTER")
    check("G01-Dirichlet-sign-identity",
          dirichlet_sign_ok(16, 7) and dirichlet_sign_ok(12, 5)
          and dirichlet_sign_ok(21, 9),
          "sign(D_m(a)) = sign(sin((m+1/2)a))*sign(sin(a/2)) "
          "on cosine grids S=16,12,21")

    ok_env, mxrel = dirichlet_envelope_ok()
    check("G02-Dirichlet-envelope",
          ok_env and mxrel < ENV_BAR,
          "|D_n| <= min(2n+1, 1/|sin(a/2)|) max(abs/env-1)=%.3e"
          % mxrel)

    ok_cd = True
    for n, th, ph in ((5, 0.3, 1.1), (12, 0.7, 0.7), (8, 0.0, math.pi)):
        if abs(CA.cheb_K_closed(n, th, ph) - CA.cheb_K_sum(n, th, ph)) > CHEB_BAR:
            ok_cd = False
    check("G03-Chebyshev-CD-Dirichlet",
          ok_cd,
          "closed Dirichlet combination = cosine sum (r387)")

    c = 0.4
    A = np.array([[1.0, -c], [-c, 1.0]])
    lam = float(np.linalg.eigvalsh(A)[-1])
    check("G04-Z-matrix-bound-false",
          abs(lam - (1.0 + c)) < 1e-12 and lam > 1.0,
          "[[1,-c],[-c,1]] lambda=1+c=%.2f > maxdiag: hoped "
          "M-bound lambda<=maxdiag is FALSE" % lam)

    E = np.array([[2.0, 1.0], [1.0, 2.0]])
    gs = gram_stats(E)
    check("G05-bookkeeping",
          abs(gs["lam"] - gs["maxd"] * (1.0 + gs["assist"])) < 1e-12,
          "lambda = maxdiag*(1+assist) exact")

    m = 6
    Scb, s = checkerboard(m)
    ok_cb = True
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if Scb[i, j] != s[i] * s[j]:
                ok_cb = False
            if Scb[i, j] != (-1) ** (i - j):
                ok_cb = False
    check("G06-checkerboard-rank1",
          ok_cb,
          "S_ij = sigma_i sigma_j = (-1)^{i-j} (rank-1 signs)")

    S = 16
    j = np.array([3, 4])
    th = np.arccos(np.cos(PI * j / S))
    check("G07-mesh-step-pi-over-S",
          abs(abs(th[1] - th[0]) - PI / S) < 1e-14,
          "Delta_mesh = pi/S exact on the cosine grid")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 map, TP in-phase, scramble, |E|")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    depth = N - 1
    entry = (2 * N) // 5
    print("    w9 N=%d n_nu=%d entry=2N/5=%d ..." % (N, len(mz["yn"]), entry),
          flush=True)
    B = CA.make_B(mz, depth)
    th, yn, vn, B = order_by_theta(mz["yn"], mz["vn"], B)

    Ewall = E_from_B(B, depth)
    pw = sign_pack(Ewall, th, depth)
    gs = pw["gs"]
    check("G10-w9-wall-assist",
          W9_ASSIST_LO < gs["assist"] < W9_ASSIST_HI
          and gs["canc"] > W9_CANC_FLOOR and gs["lam"] < 1.0,
          "lam=%.6f maxd=%.4f assist=%.4f gA=%.2f canc=%.4f"
          % (gs["lam"], gs["maxd"], gs["assist"], gs["gA"], gs["canc"]))
    check("G11-w9-Cheb-mass-agree",
          W9_CHEB_WW[0] < pw["ww_c"] < W9_CHEB_WW[1]
          and W9_CHEB_UW[0] < pw["uw_c"] < W9_CHEB_UW[1],
          "Cheb uw=%.3f ww=%.3f (mass inherits; pair-count is not a SATZ)"
          % (pw["uw_c"], pw["ww_c"]))
    check("G12-w9-checkerboard-coin",
          W9_CB_WW[0] < pw["ww_b"] < W9_CB_WW[1],
          "CB ww=%.3f -- rank-1 checkerboard REFUTED as the sign map"
          % pw["ww_b"])
    check("G13-w9-NN-not-Mpath",
          W9_NN_NEG[0] < pw["nn_share"] < W9_NN_NEG[1],
          "NN neg_share=%.3f (pos/neg=%d/%d) -- not an M-matrix path"
          % (pw["nn_share"], pw["nn_pos"], pw["nn_neg"]))
    check("G14-w9-absE-mutant",
          W9_LAMABS[0] < gs["lam_abs"] < W9_LAMABS[1] and gs["lam_abs"] > 1.0,
          "lambda(|E|)=%.3f > 1 (dropping signs kills Assist; "
          "unsigned Gershgorin=%.2f, relative gA=%.2f is sign-blind)"
          % (gs["lam_abs"], gs["gersh"], gs["gA"]))
    check("G15-w9-oracle-bound-open",
          pw["oracle_bnd"] > ORACLE_BND_FLOOR,
          "oracle bound_pos=%.3f pos_share=%.3f > 1 -- even the "
          "true top-evec conjugation does not close lambda<1"
          % (pw["oracle_bnd"], pw["oracle_psh"]))

    ww12 = []
    for k in range(depth - 11, depth + 1):
        pk = sign_pack(E_from_B(B, k), th, k)
        ww12.append(pk["ww_c"])
    check("G16-w9-last12-Cheb-ww",
          min(ww12) > W9_LAST12_WW_LO,
          "last-12 Cheb ww in [%.4f, %.4f] (robust over k, not a SATZ)"
          % (min(ww12), max(ww12)))

    pe = sign_pack(E_from_B(B, entry), th, entry)
    check("G17-w9-entry-Cheb-not-CB",
          pe["ww_c"] > W9_ENTRY_WW_LO and pe["ww_b"] < 0.50,
          "k=2N/5=%d Cheb ww=%.3f CB ww=%.3f NN neg_share=%.3f "
          "(nearest neighbours CONSTRUCTIVE at entry)"
          % (entry, pe["ww_c"], pe["ww_b"], pe["nn_share"]))

    mz23 = CA.two_period(81, C_FLANK)
    B23 = CA.make_B(mz23, 40)
    th23, yn23, vn23, B23 = order_by_theta(mz23["yn"], mz23["vn"], B23)
    p22 = sign_pack(E_from_B(B23, 22), th23, 22)
    check("G18-two-period-in-phase",
          p22["nn_neg"] == 0 and p22["nn_pos"] == p22["nn_neg"] + p22["nn_pos"]
          and p22["gs"]["lam"] > 1.0 and p22["nn_share"] < 0.01,
          "k=22 NN pos/neg=%d/%d lam=%.4f>1 -- in-phase kill "
          "(conjugation along the chain is impossible)"
          % (p22["nn_pos"], p22["nn_neg"], p22["gs"]["lam"]))

    p40 = sign_pack(E_from_B(B23, 40), th23, 40)
    uw_ncb, ww_ncb = mass_agree(E_from_B(B23, 40),
                                -checkerboard(B23.shape[0])[0])
    check("G19-two-period-antiCB-too-late",
          abs(uw_ncb - 1.0) < 1e-12 and abs(p40["gs"]["maxd"] - 1.317) < 0.02
          and p40["gs"]["lam"] > 1.0,
          "k=40 -CB agree=%.3f maxd=%.3f lam=%.3f -- perfect "
          "anti-checkerboard arrives after maxdiag>1"
          % (uw_ncb, p40["gs"]["maxd"], p40["gs"]["lam"]))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    ns = int(ds["n_max"]) - 1
    a, b, h0 = V.mu_chain(ds["xs"], ds["ws"], ns)
    Bsc = V.b_matrix(a, b, h0, ds["ys"], ds["vs"], ns)
    ths, yns, vns, Bsc = order_by_theta(ds["ys"], ds["vs"], Bsc)
    ksc = min(ns, depth)
    psc = sign_pack(E_from_B(Bsc, ksc), ths, ksc)
    check("G20-scramble-envelope-not-map",
          psc["ww_c"] > SCR_WW_LO and psc["gs"]["lam"] > SCR_LAM_FLOOR,
          "scr-seed=%d Cheb ww=%.3f lam=%.3e -- map of large "
          "entries HOLDS, envelope/occupation kills (r388 dDelta)"
          % (SCR_SEED, psc["ww_c"], psc["gs"]["lam"]))

    if smoke:
        return

    section("S3  FULL CENSUS -- core-42 wall sign map")
    core = list(V.admissible_indices())
    check("G21-ladder-size",
          len(core) == CORE_N,
          "core %d" % len(core))
    cheb_ww, cb_ww, nns, assists, lams = [], [], [], [], []
    for i, kz in enumerate(core):
        mzk = V.build_measures(kz)
        Nk = int(mzk["Nw"])
        Bk = CA.make_B(mzk, Nk - 1)
        thk, ynk, vnk, Bk = order_by_theta(mzk["yn"], mzk["vn"], Bk)
        pk = sign_pack(E_from_B(Bk, Nk - 1), thk, Nk - 1)
        cheb_ww.append(pk["ww_c"])
        cb_ww.append(pk["ww_b"])
        nns.append(pk["nn_share"])
        assists.append(pk["gs"]["assist"])
        lams.append(pk["gs"]["lam"])
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)
    n_ok = sum(1 for x in lams if x < 1.0)
    check("G22-core42-lam-lt-one",
          n_ok == CORE_N,
          "%d/42 lam<1 maxlam=%.8f (census, not a conjugacy theorem)"
          % (n_ok, max(lams)))
    check("G23-core42-Cheb-mass-inherit",
          min(cheb_ww) > CORE_CHEB_WW[0] and max(cheb_ww) < CORE_CHEB_WW[1],
          "Cheb ww in [%.3f, %.3f] -- mass inherits Dirichlet "
          "zones; 11-19 pct residual is tau-deformation + sum term"
          % (min(cheb_ww), max(cheb_ww)))
    check("G24-core42-checkerboard-coin",
          min(cb_ww) > CORE_CB_WW[0] and max(cb_ww) < CORE_CB_WW[1],
          "CB ww in [%.3f, %.3f] -- bipartition REFUTED on the ladder"
          % (min(cb_ww), max(cb_ww)))
    check("G25-core42-NN-and-assist",
          min(nns) > CORE_NN_NEG[0] and max(nns) < CORE_NN_NEG[1]
          and max(assists) < CORE_ASSIST_HI,
          "NN neg_share in [%.3f, %.3f]; assist in [%.4f, %.4f]"
          % (min(nns), max(nns), min(assists), max(assists)))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("sign_schur_probe -- LEMMA.SIGN_SCHUR.01 (round 394)")
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
    tag = "SIGN SCHUR LEMMA SMOKE" if smoke else "SIGN SCHUR LEMMA"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
