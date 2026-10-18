#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""diag_lifts_loewner_probe --
PRIME.RDAGGER.DIAGONAL_LIFTS_LOEWNER.01
(round 441, reviewer DCCCX, one lemma-first round):
does the source-pure PD diagonal lift all but at
most one negative direction of L_{-m-tilde}, i.e.
n_-(W_Y - K_YY^{-1}) <= 1 on Selected?

LEMMA DIAG_LIFTS (two forms).
  General: n_-(W_Y - K^{-1}) <= 1 on the selected
  sequence.  kdim=0 pair: Delta D0 Delta =
  L_{-m-tilde} + diag(w_Y (P_Y')^2) and the
  diagonal lifts L.

LEGS.
  A  Loewner signature of -m-tilde.  m-tilde is
     Herglotz-like with positive masses at X.
     L_m = C diag(w pi_Y(X)^2) C^T (Gram).  Is
     L_{-m} fully ND, or does X-between-Y change
     the inertia (classical Loewner / interlacing)?
  B  Lift: n_-(L+D) = #{lambda(D^{-1/2} L
     D^{-1/2}) < -1} at kdim=0.  General form
     n_-(W-K^{-1}) = #{lambda(W^{1/2} K W^{1/2}) < 1}.
     Spectrum vs the threshold; gap; kills.
  C  Christoffel: (K^{-1})_ii K_ii >= 1; d_min =
     min_i w_i K_ii (r408 separator) vs the
     one-defect count.
  D  Kills (PERM / jitter / scramble), dead chi,
     kz52 (r438 razor), drop-D mutant.

CALIBRATION DISCLOSURE.  Gram identity, L-inertia,
interlacing count, -1 / <1 spectra, d_min, kz52
and kills first measured in /tmp (r441_cal.py,
r441_cal2.py) on the r439 constructors, 2026-08-30.
Frozen floors below are that measurement, sealed
as gates.  Pins disclosed.  Builder fallback NOT
taken (pack_graph, < 60 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * 5-atom kdim=0: L_m = C Wpi C^T EXACT; L_{-m}
    inertia (0,2,0) ND rank 2; X-in-Yspan = 0;
    pair inertia (1,1,0)=D0; n_below_-1 = 1;
    WK n<1 = 1; d_min = 8461/1120 > 1;
    CS (Kinv_ii K_ii) = 5592721/252000;
    drop-D => n_-(L)=2.
  * 6-node kdim=0: Gram EXACT; L inertia (0,3,0);
    X-in-Yspan = 1 (does NOT change ND);
    pair (1,2,0)=D0; n_below_-1 = 2; WK n<1 = 2;
    d_min = 210157/57600 > 1 AND n_-=2 --
    d_min>1 => n_-<=1 REFUTED as a universal
    implication.  Universal DIAG_LIFTS REFUTED.
  * Windows kdim>0: pair identity FAILS (rel 0.4
    .. 400); L via Cauchy-pi overflows.  Live
    object is WK vs 1: n_-(D0) = n(lambda(WK)<1)
    on every measured window.
  * w9: n_lt1=1 nneg_diag=0 dmin=1.65568
    gap 0.857 .. 1.00018.
    kz15: 1 / 1.248 / 0.816; kz18: 1 / 1.179 / 0.640;
    kz20: 1 / 1.437 / 0.976; kz52: 1 / 1.272 / 0.781
    (r438 razor is a different depth; here n_-=1).
  * PERM n_lt1=20 dmin=0.148 n(wK<1)=7;
    JIT 19 / 0.628 / 2; SCR 21 / 0.367 / 9.
    CHI3-9 n_lt1=0 dmin=1.001 (PD, minλ=1.0009);
    CHI3-15 n_lt1=1 dmin=1.004 gap 0.99816.
  * Core sample: n_lt1 in {0,1}; c22 gap_lo=0.99981
    is the tight Selected slip in this coordinate.
    c38 nneg_diag=9 but n_lt1=1 -- diag(D0) is NOT
    the carrier.

AUSGANG REDUZIERT.
SATZ: L_m is the dressed Cauchy Gram (always PSD);
interlacing does not set L-inertia.  SATZ: the
lift count is #{lambda(W^{1/2} K W^{1/2}) < 1}
(kdim=0: #{lambda(D^{-1/2} L D^{-1/2}) < -1}).
d_min>1 => n_-<=1 REFUTED (6-node).  Bound <=1 on
Selected remains OPEN (census).  No RH claim.

MACHINERY: r439 residual_loewner constructors;
r409 pack_graph / S0_Q; r431 toys; r403/r398
reweight / chi; r226 V.build_measures.

NO RH CLAIM.  Finite identities and a named
reduction.  No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
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

import residual_loewner_probe as RL  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import r431_audit_probe as A  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
P1_SHA_PREFIX = "ba6817f5"
HM_SHA_PREFIX = "bb1dcf6a"

DMIN5 = Fr(8461, 1120)
CS5 = Fr(5592721, 252000)
DMIN6 = Fr(210157, 57600)
W9_DMIN_LO, W9_DMIN_HI = 1.60, 1.71
W9_GAP_LO, W9_GAP_HI = 0.80, 0.90
KZ52_DMIN_LO, KZ52_DMIN_HI = 1.20, 1.35
PERM_DMIN_HI = 0.20
PERM_NLT1_LO, SCR_NLT1 = 15, 21
CHI3_9_NLT1, CHI3_15_NLT1 = 0, 1

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("cauchy_gram_Q", "christoffel_diag_Q",
                "pair_shift_Q")


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
    return (not bad), ("NO zero/prime oracles; Cauchy Gram / "
                       "Christoffel / pair-shift only"
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


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"eigvalsh", "eigh", "svd", "cholesky", "pack_C",
              "chain_C", "pack_graph", "r_nm3", "aug_rung"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def cauchy_gram_Q(xX, wX, ys):
    """L_m-tilde = C diag(w pi_Y(x)^2) C^T.  Only (x,w,Y)."""
    nY, nX = len(ys), len(xX)
    C = [[Fr(1) / (xX[a] - ys[i]) for a in range(nX)]
         for i in range(nY)]
    c = []
    for x, w in zip(xX, wX):
        pi = B.P_Y_Q(x, ys)
        c.append(pi * pi * w)
    Lm = [[Fr(0) for _ in range(nY)] for _ in range(nY)]
    for i in range(nY):
        for j in range(nY):
            s = Fr(0)
            for a in range(nX):
                s += C[i][a] * c[a] * C[j][a]
            Lm[i][j] = s
    return Lm


def christoffel_diag_Q(K, wY):
    """Source diagonals: (K_ii, w_i K_ii).  No eig."""
    n = len(wY)
    kii = [K[i][i] for i in range(n)]
    return kii, [wY[i] * kii[i] for i in range(n)]


def pair_shift_Q(wY, pr):
    """PD pair-diagonal w_Y (P_Y')^2.  Only (w,Y-deriv)."""
    return [wY[i] * pr[i] * pr[i] for i in range(len(wY))]


def x_in_yspan(xX, ys):
    ymin, ymax = min(ys), max(ys)
    return sum(1 for x in xX if ymin < x < ymax)


def n_below_minus1_Q(Lnm, dsh):
    n = len(dsh)
    s = [float(d) ** 0.5 for d in dsh]
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = float(Lnm[i][j]) / (s[i] * s[j])
    ev = np.sort(np.linalg.eigvalsh(M))
    return ev, int(np.sum(ev < -1.0 - 1e-12))


def wk_nlt1_Q(K, wY):
    n = len(wY)
    s = [float(w) ** 0.5 for w in wY]
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = float(K[i][j]) * s[i] * s[j]
    ev = np.sort(np.linalg.eigvalsh(M))
    return ev, int(np.sum(ev < 1.0 - 1e-12))


def wk_row(g):
    ys = np.asarray(g["yn"], float)
    wY = np.asarray(g["wY"], float)
    D0 = np.asarray(g["D0"], float)
    K = RL.kernel_YY_f64(g["xp"], g["wX"], ys, g["d0"])
    s = np.sqrt(np.maximum(wY, 0.0))
    M = (s[:, None] * K) * s[None, :]
    ev = np.sort(np.linalg.eigvalsh(0.5 * (M + M.T)))
    n_lt1 = int(np.sum(ev < 1.0 - 1e-10))
    below = ev[ev < 1.0 - 1e-10]
    above = ev[ev > 1.0 + 1e-10]
    dmin = float(np.min(wY * np.diag(K)))
    nneg = S.nneg_sym(D0, 1e-10)[0]
    nneg_diag = int(np.sum(np.diag(D0) < -1e-12))
    return dict(n=len(ys), n_lt1=n_lt1, nneg=nneg,
                nneg_diag=nneg_diag, dmin=dmin,
                gap_lo=float(below[-1]) if below.size else None,
                gap_hi=float(above[0]) if above.size else None,
                min_ev=float(ev[0]), ev=ev, g=g)


def part_toys():
    section("S1  LEG A/B/C OVER Q -- 5-ATOM + 6-NODE")
    xs, u, ud, iX, iY, d0, _ = S.prime_toy()
    t5 = RL.toy_bundle(xs, ud, iX, iY, 2)
    mt = [RL.m_tilde_Q(t5["xX"], t5["wX"], t5["ys"], y)
          for y in t5["ys"]]
    mtp = [RL.m_tilde_prime_Q(t5["xX"], t5["wX"], t5["ys"], y)
           for y in t5["ys"]]
    Lm = RL.loewner_Q(t5["ys"], mt, mtp)
    Gram = cauchy_gram_Q(t5["xX"], t5["wX"], t5["ys"])
    Lnm = [[-a for a in row] for row in Lm]
    dsh = pair_shift_Q(t5["wY"], t5["pr"])
    check("G01-5atom-gram-ND",
          RL.mat_eq(Lm, Gram) and S.inertia_fr(Lnm) == (0, 2, 0)
          and x_in_yspan(t5["xX"], t5["ys"]) == 0,
          "L_m = C Wpi C^T EXACT; L_{-m} (0,2,0); X-in-Yspan=0")
    evm, nb = n_below_minus1_Q(Lnm, dsh)
    K5 = RL.kernel_YY_Q(t5["xX"], t5["wX"], t5["ys"], 2)
    evw, nlt = wk_nlt1_Q(K5, t5["wY"])
    _kii, wk = christoffel_diag_Q(K5, t5["wY"])
    cs = t5["S0"][0][0] * K5[0][0]
    check("G02-5atom-lift-count",
          nb == 1 and nlt == 1
          and S.inertia_fr(t5["D0"]) == (1, 1, 0)
          and min(wk) == DMIN5 and cs == CS5,
          "n_below_-1=1 = WK n<1=1 = n_-(D0); dmin=%s CS=%s"
          % (DMIN5, CS5))
    check("G03-5atom-dropD",
          S.inertia_fr(Lnm)[1] == 2,
          "drop-D mutant: n_-(L)=2 full ND signature")

    xs2, ud2, iX2, iY2 = A.second_toy()
    t6 = RL.toy_bundle(xs2, ud2, iX2, iY2, 3)
    mt6 = [RL.m_tilde_Q(t6["xX"], t6["wX"], t6["ys"], y)
           for y in t6["ys"]]
    mtp6 = [RL.m_tilde_prime_Q(t6["xX"], t6["wX"], t6["ys"], y)
            for y in t6["ys"]]
    Lm6 = RL.loewner_Q(t6["ys"], mt6, mtp6)
    Gram6 = cauchy_gram_Q(t6["xX"], t6["wX"], t6["ys"])
    Lnm6 = [[-a for a in row] for row in Lm6]
    dsh6 = pair_shift_Q(t6["wY"], t6["pr"])
    nin6 = x_in_yspan(t6["xX"], t6["ys"])
    check("G10-6node-gram-ND-interlace",
          RL.mat_eq(Lm6, Gram6)
          and S.inertia_fr(Lnm6) == (0, 3, 0)
          and nin6 == 1,
          "Gram EXACT; L (0,3,0) despite X-in-Yspan=1 "
          "-- interlacing does NOT set L-inertia")
    evm6, nb6 = n_below_minus1_Q(Lnm6, dsh6)
    K6 = RL.kernel_YY_Q(t6["xX"], t6["wX"], t6["ys"], 3)
    evw6, nlt6 = wk_nlt1_Q(K6, t6["wY"])
    _k6, wk6 = christoffel_diag_Q(K6, t6["wY"])
    check("G11-6node-universal-refuted",
          nb6 == 2 and nlt6 == 2
          and S.inertia_fr(t6["D0"]) == (1, 2, 0)
          and min(wk6) == DMIN6 and DMIN6 > 1,
          "n_-=2 with dmin=%s>1 -- d_min>1 => n_-<=1 "
          "REFUTED; universal DIAG_LIFTS REFUTED" % DMIN6)
    return t5, t6


def part_windows(smoke):
    section("S2  WEIGHTED KERNEL VS 1 -- WINDOWS")
    g9 = B.pack_graph(V.build_measures(9))
    w9 = wk_row(g9)
    check("G20-w9-wk-identity",
          w9["nneg"] == 1 and w9["n_lt1"] == 1
          and w9["nneg_diag"] == 0
          and W9_DMIN_LO <= w9["dmin"] <= W9_DMIN_HI
          and w9["gap_lo"] is not None
          and W9_GAP_LO <= w9["gap_lo"] <= W9_GAP_HI,
          "n_-(D0)=n(WK<1)=1; nneg_diag=0; dmin=%.5f "
          "gap_lo=%.5f .. %.5f" %
          (w9["dmin"], w9["gap_lo"], w9["gap_hi"]))
    if smoke:
        check("G21-extra-windows-smoke-skip", True,
              "kz15/18/52 + c22 deferred")
        return w9
    r15 = wk_row(B.pack_graph(V.build_measures(15)))
    r18 = wk_row(B.pack_graph(V.build_measures(18)))
    check("G21-kz15-kz18-wk",
          r15["n_lt1"] == 1 and r18["n_lt1"] == 1
          and r15["nneg"] == 1 and r18["nneg"] == 1,
          "kz15 n_lt1=1 dmin=%.5f; kz18 n_lt1=1 dmin=%.5f"
          % (r15["dmin"], r18["dmin"]))
    r52 = wk_row(B.pack_graph(V.build_measures(52)))
    check("G22-kz52-survives",
          r52["n_lt1"] == 1 and r52["nneg"] == 1
          and KZ52_DMIN_LO <= r52["dmin"] <= KZ52_DMIN_HI,
          "kz52 n_lt1=1 dmin=%.5f gap_lo=%.5f "
          "(r438 razor is another depth; here one slip)"
          % (r52["dmin"], r52["gap_lo"]))
    r22 = wk_row(B.pack_graph(V.build_measures(22)))
    check("G23-c22-tight-slip",
          r22["n_lt1"] == 1 and r22["gap_lo"] is not None
          and r22["gap_lo"] > 0.999,
          "c22 gap_lo=%.6f -- tightest Selected slip"
          % r22["gap_lo"])
    return w9


def part_kills(w9, smoke):
    section("S3  KILLS / CHI / DIAGONAL IS NOT THE CARRIER")
    if smoke:
        check("G30-kills-smoke-skip", True,
              "permute/scramble/chi deferred")
        return
    mz = V.build_measures(9)
    pP = wk_row(B.pack_graph(P1.reweight(mz, "permute", 1000)))
    pJ = wk_row(B.pack_graph(P1.reweight(mz, "gauss", 431)))
    pS = wk_row(B.pack_graph(HM.scramble_mz()))
    check("G30-kills-spectrum",
          pP["n_lt1"] >= PERM_NLT1_LO and pS["n_lt1"] == SCR_NLT1
          and pJ["n_lt1"] >= 15
          and pP["dmin"] < PERM_DMIN_HI,
          "PERM n_lt1=%d dmin=%.4f; JIT %d / %.3f; "
          "SCR %d / %.3f -- many slips, d_min<1"
          % (pP["n_lt1"], pP["dmin"], pJ["n_lt1"], pJ["dmin"],
             pS["n_lt1"], pS["dmin"]))
    c9 = wk_row(B.pack_graph(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)))
    c15 = wk_row(B.pack_graph(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)))
    check("G31-chi-census",
          c9["n_lt1"] == CHI3_9_NLT1 and c15["n_lt1"] == CHI3_15_NLT1
          and c9["min_ev"] > 1.0,
          "CHI3-9 n_lt1=0 minλ=%.5f (PD); CHI3-15 n_lt1=1 "
          "gap_lo=%.5f -- death is the edge side"
          % (c9["min_ev"], c15["gap_lo"]))
    check("G32-diag-not-carrier",
          w9["nneg_diag"] == 0 and w9["n_lt1"] == 1
          and pP["nneg_diag"] > pP["n_lt1"],
          "MAIN nneg_diag=0 with n_lt1=1; PERM nneg_diag=%d "
          "> n_lt1=%d -- diag(D0) is not the one-defect count"
          % (pP["nneg_diag"], pP["n_lt1"]))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("diag_lifts_loewner_probe -- "
          "PRIME.RDAGGER.DIAGONAL_LIFTS_LOEWNER.01 (round 441)")
    print("SPEC_SHA %s   (B %s / P1 %s / HM %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], P1.SPEC_SHA[:16],
             HM.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (w9 + kz15/18/52 + c22 + kills + chi)"))
    print("=" * 78)

    section("S0  FIREWALL + TARGET_LEAK")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / P1 %s / HM %s"
          % (B.SPEC_SHA[:8], P1.SPEC_SHA[:8], HM.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))
    leak = []
    for fn in CONSTRUCTORS:
        leak.extend(scope_audit(fn))
    check("G00d-constructor-no-target",
          leak == [],
          "Cauchy Gram / Christoffel / pair-shift clean"
          if not leak else "; ".join(leak))

    part_toys()
    w9 = part_windows(smoke)
    part_kills(w9, smoke)

    section("S4  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    verd = "REDUZIERT"
    check("G60-verdict",
          prev_ok,
          verd + ": L is Cauchy Gram (ND); lift count is "
          "#{lambda(W^{1/2} K W^{1/2})<1}; d_min>1 => n_-<=1 "
          "REFUTED; Selected bound OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("DIAG LIFTS %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DIAG LIFTS FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
