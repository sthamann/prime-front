#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pivot_entry_lemma_probe -- LEMMA.PIVOT_ENTRY.01 (round 382):
THE ENTRY LEMMA OF THE PIVOT BAND, source-arithmetic core.

Coexistence: R377/R378/R379/R380/R381/R383 run in parallel -- this
probe touches NOTHING outside its own file and the strictly additive
rh-sync.  next.txt is NOT written.  NO Lean edit (R384 formalizes).

THE FROZEN QUESTION.  R380 proved rankOne_inertia_antitone and
adaptive_band_from_entry: an entry ind_-(A_{n0}) <= 1 at a
source-defined n0 carries through the rank-1 Loewner band.  Equiv.
(Jacobi): the signed-source pivots h_0..h_{n0} have at most one
sign change.  The strongest form is n0 = N-1 with zero changes
(the floor plate = L* itself).  Any weaker source-defined form
that activates the transport is a reduction.

R377: Sturm alone does not forbid a second prefix return
(scramble first_neg=21, 37 negatives).  The source must enter.
No universal fixed offset from N (the dual-chain first nneg<=1
sits at N-6 on w9 and N-13 on kz42).

THIS ROUND DECIDES by a sealed three-leg attack:
  A  recursion dynamics of (alpha, beta^2) through ~N/2, MAIN vs
     scramble, with named kills;
  B  an interlacing / flank-mass finite theorem of the form
     "max nu-run <= 2 and nu-mass <= (2/3) flanking mu-mass
      => h_k > 0 for k <= floor(2N/5)";
  C  kill battery: scramble drops out at F1 and F2, dead chi
     satisfy both, two-period at c=2/3 sits at ~N/2 (the bound
     2/5 is strictly below that kill), two-period c>=1 and
     clustered run>=3 kill early.

CALIBRATION DISCLOSURE.  Flank ratios, two-period first_neg
table, lambda_max(E_k) at small k, and the 85-window F1/F2
tallies were first measured in /tmp (r382_cal.py, cal2, cal3,
cal4) on the same constructors.  The frozen counts below are
that measurement, sealed as gates -- not a search over the
threshold 2/3 (the threshold is the first rational strictly
above every core-42 rmax, all of which are <= 0.619).

FROZEN TALLIES:
  MAIN 85: F1 (max_len<=2) 85/85; F2 (rmax<1 and n_gt1=0) 85/85;
           F2_23 (rmax<=2/3) 78/85; the seven EXT-heavy
           (rmax in (2/3, 1)) are
           (69, 96, 97, 99, 107, 117, 129).
  CORE 42: F2_23 42/42, nh67=0, max delta_50 = 0.0402.
  DEAD chi: F1+F2_23 on chi3 {15,19,23,33,39} and chi4 {20}.
  SCR w9 seed 1: EARLY, first_neg=21, max_len=5, n_lenge3=9,
           rmax>2, n_gt1=12, first |alpha|>2 at degree 21.
  Two-period cosine S=81 (N=41): c=1/2 first_neg=40;
           c=2/3 first_neg=20; c=1 first_neg=0.
  w9 K_sum (largest k with sum_j nu_j K_k(y_j,y_j) < 1) = 9.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r357
dirichlet_matched_frame (DMF), r286 lstar_margin_scaling (LM),
r-ext3 anchors (E3), r226 hirota_sign (HS),
verify_lstar_instance (V.build_measures).

NO RH CLAIM.  Finite identities, a named sufficient condition,
and a construction census.  Not a theorem of L* or of RH.
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
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import ext3_fresh_anchors_probe as E3  # noqa: E402
import lstar_margin_scaling_probe as LM  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402

MAIN_KZ = 9
SCR_SEED = 1
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT5_KZ = (69, 107, 101, 99, 115, 89)
EXT6_KZ = (133, 129, 124, 117)
HEAVY7 = (69, 96, 97, 99, 107, 117, 129)

C_FLANK = 2.0 / 3.0
KAPPA = 2.0 / 5.0

FROZEN_MAIN_F1 = 85
FROZEN_MAIN_F2 = 85
FROZEN_MAIN_F23 = 78
FROZEN_CORE_NH67 = 0
FROZEN_CORE_D50_MAX = 0.0402
SCR_FIRST, SCR_MAXLEN, SCR_NLENGE3, SCR_NGT1 = 21, 5, 9, 12
W9_KSUM = 9
W9_RMAX_LO, W9_RMAX_HI = 0.568, 0.570
TP81 = {0.5: 40, 2.0 / 3.0: 20, 1.0: 0}

DMF_SHA_PREFIX = "4bf1a94b"
LM_SHA_PREFIX = "0a44ac4e"
E3_SHA_PREFIX = "bbfaf199"
HS_SHA_PREFIX = "d78e236b"

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
    return (not bad), ("NO zero/prime oracles; constructors consume "
                       "measure arrays / positions only"
                       if not bad else "; ".join(bad))


def n0_of(N):
    return int(math.floor(KAPPA * N))


def signed_jacobi(x, w, nmax):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    eta = float(np.dot(w, q * q))
    signs = [int(np.sign(eta)) if eta != 0 else 0]
    alphas = []
    log_s = 0.0
    log_sm = 0.0
    etam = 1.0
    first_big_a = None
    for n in range(nmax):
        if abs(eta) < 1e-300:
            signs.append(0)
            break
        al = float(np.dot(w, x * q * q)) / eta
        alphas.append(al)
        if first_big_a is None and abs(al) > 2.0:
            first_big_a = n
        if n == 0:
            rvec = (x - al) * q
        else:
            coef = math.exp(log_s - log_sm) * (eta / etam)
            rvec = (x - al) * q - coef * qm
        sc = float(np.max(np.abs(rvec)))
        if sc == 0.0:
            signs.append(0)
            break
        qm = q
        q = rvec / sc
        log_sm = log_s
        log_s = log_s + math.log(sc)
        etam, eta = eta, float(np.dot(w, q * q))
        signs.append(int(np.sign(eta)) if eta != 0 else 0)
    fn = next((j for j, s in enumerate(signs) if s < 0), None)
    return dict(signs=signs, alpha=alphas, first_neg=fn,
                first_big_a=first_big_a)


def flanking_stats(wu):
    s = np.sign(wu)
    n = len(s)
    runs = []
    i = 0
    while i < n:
        if s[i] < 0:
            j = i
            while j < n and s[j] < 0:
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1
    rats, lens = [], []
    n_inf = 0
    for a, b in runs:
        nu = float(-np.sum(wu[a:b]))
        fl = 0.0
        if a > 0 and wu[a - 1] > 0:
            fl += float(wu[a - 1])
        if b < n and wu[b] > 0:
            fl += float(wu[b])
        lens.append(b - a)
        if fl <= 0:
            n_inf += 1
            rats.append(np.inf)
        else:
            rats.append(nu / fl)
    finite = [r for r in rats if math.isfinite(r)]
    n_runs = len(runs)
    nh50 = sum(1 for r in finite if r >= 0.5)
    nh67 = sum(1 for r in finite if r >= C_FLANK)
    return dict(
        n_runs=n_runs,
        max_len=max(lens) if lens else 0,
        n_lenge3=sum(1 for L in lens if L >= 3),
        rmax=max(finite) if finite else np.inf,
        rmed=float(np.median(finite)) if finite else np.inf,
        n_gt1=sum(1 for r in finite if r >= 1.0),
        n_inf=n_inf,
        nh50=nh50,
        nh67=nh67,
        d50=(nh50 / n_runs) if n_runs else 0.0,
        F1=bool(lens) and max(lens) <= 2 and n_inf == 0,
        F2=bool(finite) and max(finite) < 1.0 and n_inf == 0
        and (not any(r >= 1.0 for r in finite)),
        F23=bool(finite) and max(finite) <= C_FLANK + 1e-15 and n_inf == 0,
    )


def scramble_mz(seed=SCR_SEED):
    d = HS.window_data(9, scramble_seed=seed)
    xu = np.concatenate([d["xs"], d["ys"]])
    wu = np.concatenate([d["ws"], -d["vs"]])
    o = np.argsort(xu)
    return dict(xu=xu[o], wu=wu[o], Nw=int(d["n_max"]), S=len(xu),
                xp=d["xs"], wp=d["ws"], yn=d["ys"], vn=d["vs"])


def chi_mz(kz, q):
    uu, ww, _, _ = DMF.chi_window_comb(kz, q)
    lpq = DMF.LPQ3 if q == DMF.Q_CHI3 else DMF.LPQ4
    return DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    return dict(xu=x, wu=w, Nw=(S + 1) // 2, S=S)


def clustered(S, cluster=6):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = mesh.copy()
    mid = S // 2
    w[mid:mid + cluster] *= -1.0
    return dict(xu=x, wu=w, Nw=(S + 1) // 2, S=S)


def christoffel_sum(mz, k):
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], k)
    yn, vn = mz["yn"], mz["vn"]
    u = np.ones_like(yn) / math.sqrt(h0)
    um = np.zeros_like(yn)
    Kd = u * u
    for i in range(k - 1):
        r = (yn - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        Kd = Kd + u * u
    return float(np.dot(vn, Kd)), float(np.max(vn * Kd))


def main_ladder():
    core_kzs = list(V.admissible_indices())
    lm_rows = LM.ext_rule()
    ext_kzs = [t[1] for t in lm_rows[:15]]
    all_main = (core_kzs + ext_kzs + list(EXT3_KZ_B + EXT3_KZ_A)
                + list(EXT4_KZ_B + EXT4_KZ_A) + list(EXT5_KZ)
                + list(EXT6_KZ))
    return core_kzs, all_main


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("pivot_entry_lemma_probe -- LEMMA.PIVOT_ENTRY.01 (round 382)")
    print("SPEC_SHA %s   (DMF %s / LM %s / E3 %s / HS %s)"
          % (SPEC_SHA[:16], DMF.SPEC_SHA[:16], LM.SPEC_SHA[:16],
             E3.SPEC_SHA[:16], HS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (pins + two-period + dead chi)"
                        if smoke else "FULL CENSUS 85 MAIN + dead chi"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and HS.SPEC_SHA.startswith(HS_SHA_PREFIX))
    check("G02-import-sha", sha_ok,
          "DMF %s / LM %s / E3 %s / HS %s"
          % (DMF.SPEC_SHA[:8], LM.SPEC_SHA[:8], E3.SPEC_SHA[:8],
             HS.SPEC_SHA[:8]))

    section("S1  SMOKE PINS")
    mz9 = V.build_measures(MAIN_KZ)
    N9 = int(mz9["Nw"])
    fl9 = flanking_stats(mz9["wu"])
    J9 = signed_jacobi(mz9["xu"], mz9["wu"], N9 + 3)
    n09 = n0_of(N9)
    check("G10-w9-flank-entry",
          fl9["F1"] and fl9["F23"] and fl9["F2"]
          and J9["first_neg"] == N9
          and J9["first_neg"] >= n09
          and W9_RMAX_LO < fl9["rmax"] < W9_RMAX_HI
          and n09 == int(math.floor(KAPPA * 184)),
          "N=%d n0=%d first_neg=%s rmax=%.6f max_len=%d F1=%s F23=%s"
          % (N9, n09, J9["first_neg"], fl9["rmax"], fl9["max_len"],
             fl9["F1"], fl9["F23"]))

    a_half = J9["alpha"][:max(1, N9 // 2)]
    check("G11-w9-alpha-mild",
          max(abs(a) for a in a_half) < 1.0
          and J9["first_big_a"] == N9,
          "|a|_half_max=%.4f first_|a|>2=%s"
          % (max(abs(a) for a in a_half), J9["first_big_a"]))

    sb8, md8 = christoffel_sum(mz9, 8)
    lam8, _ = V.lam_max_at(mz9, 8)
    lam22, _ = V.lam_max_at(mz9, 22)
    ksum = 0
    for k in range(1, 16):
        sb, _ = christoffel_sum(mz9, k)
        if sb < 1.0:
            ksum = k
        else:
            break
    check("G12-w9-christoffel-sum",
          ksum == W9_KSUM and sb8 < 1.0 and lam8 < 0.25 and lam22 < 0.70,
          "K_sum=%d sb8=%.4f lam8=%.4f lam22=%.4f md8=%.4f"
          % (ksum, sb8, lam8, lam22, md8))

    mzs = scramble_mz()
    Ns = int(mzs["Nw"])
    fls = flanking_stats(mzs["wu"])
    Js = signed_jacobi(mzs["xu"], mzs["wu"], 40)
    n0s = n0_of(Ns)
    lams22, _ = V.lam_max_at(mzs, 22)
    check("G13-scramble-kill",
          (not fls["F1"]) and (not fls["F2"]) and (not fls["F23"])
          and Js["first_neg"] == SCR_FIRST
          and Js["first_neg"] < n0s
          and fls["max_len"] == SCR_MAXLEN
          and fls["n_lenge3"] == SCR_NLENGE3
          and fls["n_gt1"] == SCR_NGT1
          and fls["rmax"] > 2.5
          and Js["first_big_a"] == SCR_FIRST
          and lams22 > 1.0,
          "first=%s n0=%d max_len=%d n>=3=%d rmax=%.3f n_gt1=%d "
          "first_big_a=%s lam22=%.4f"
          % (Js["first_neg"], n0s, fls["max_len"], fls["n_lenge3"],
             fls["rmax"], fls["n_gt1"], Js["first_big_a"], lams22))

    mz_d = chi_mz(15, DMF.Q_CHI3)
    fld = flanking_stats(mz_d["wu"])
    Jd = signed_jacobi(mz_d["xu"], mz_d["wu"], int(mz_d["Nw"]) + 3)
    check("G14-dead-chi3-15-flank",
          fld["F1"] and fld["F23"]
          and Jd["first_neg"] is not None
          and Jd["first_neg"] >= n0_of(int(mz_d["Nw"])),
          "rmax=%.4f max_len=%d first_neg=%s n0=%d"
          % (fld["rmax"], fld["max_len"], Jd["first_neg"],
             n0_of(int(mz_d["Nw"]))))

    section("S1b  TWO-PERIOD + CLUSTERED KILLS")
    tp_ok = True
    tp_bits = []
    for c, fn_need in ((0.5, 40), (C_FLANK, 20), (1.0, 0)):
        mz = two_period(81, c)
        J = signed_jacobi(mz["xu"], mz["wu"], int(mz["Nw"]) + 2)
        n0 = n0_of(int(mz["Nw"]))
        ok_c = J["first_neg"] == fn_need
        if c == C_FLANK:
            ok_c = ok_c and J["first_neg"] >= n0
        if c == 1.0:
            ok_c = ok_c and J["first_neg"] == 0
        tp_ok = tp_ok and ok_c
        tp_bits.append("c=%.3f fn=%s n0=%d" % (c, J["first_neg"], n0))
    check("G15-two-period-S81", tp_ok, "; ".join(tp_bits))

    mz21 = two_period(21, C_FLANK)
    J21 = signed_jacobi(mz21["xu"], mz21["wu"], int(mz21["Nw"]) + 2)
    n021 = n0_of(int(mz21["Nw"]))
    check("G16-two-period-S21-c23",
          J21["first_neg"] == 5 and J21["first_neg"] >= n021,
          "N=%d fn=%s n0=%d" % (mz21["Nw"], J21["first_neg"], n021))

    mzc = clustered(21, 6)
    Jc = signed_jacobi(mzc["xu"], mzc["wu"], int(mzc["Nw"]) + 2)
    flc = flanking_stats(mzc["wu"])
    check("G17-clustered-run-kill",
          (not flc["F1"]) and Jc["first_neg"] is not None
          and Jc["first_neg"] < n0_of(int(mzc["Nw"])),
          "max_len=%d first_neg=%s n0=%d"
          % (flc["max_len"], Jc["first_neg"], n0_of(int(mzc["Nw"]))))

    if smoke:
        n_fail = sum(1 for _n, ok in CHECKS if not ok)
        print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
              % (len(CHECKS) - n_fail, len(CHECKS),
                 "" if n_fail == 0 else "  ** FAIL **",
                 SPEC_SHA[:16], time.time() - T0))
        print("PIVOT ENTRY SMOKE "
              + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
        return 0 if n_fail == 0 else 1

    section("S2  FULL CENSUS")
    core_kzs, all_main = main_ladder()
    check("G20-ladder-size",
          len(core_kzs) == 42 and len(all_main) == 85,
          "core %d MAIN %d" % (len(core_kzs), len(all_main)))

    n_f1 = n_f2 = n_f23 = 0
    heavy = []
    core_nh67 = 0
    core_d50 = []
    n_entry = 0
    for i, kz in enumerate(all_main):
        mz = V.build_measures(kz)
        fl = flanking_stats(mz["wu"])
        N = int(mz["Nw"])
        if fl["F1"]:
            n_f1 += 1
        if fl["F2"]:
            n_f2 += 1
        if fl["F23"]:
            n_f23 += 1
        else:
            if fl["F1"] and fl["F2"]:
                heavy.append(int(kz))
        if i < 42:
            core_nh67 += fl["nh67"]
            core_d50.append(fl["d50"])
        J = signed_jacobi(mz["xu"], mz["wu"], n0_of(N) + 1)
        fn = J["first_neg"]
        if fn is None or fn > n0_of(N):
            n_entry += 1

    check("G21-MAIN-F1",
          n_f1 == FROZEN_MAIN_F1, "F1 %d/85" % n_f1)
    check("G22-MAIN-F2",
          n_f2 == FROZEN_MAIN_F2, "F2 rmax<1 %d/85" % n_f2)
    check("G23-MAIN-F23",
          n_f23 == FROZEN_MAIN_F23
          and tuple(sorted(heavy)) == tuple(sorted(HEAVY7)),
          "F23 %d/85 heavy7=%s" % (n_f23, tuple(sorted(heavy))))
    check("G24-CORE-quantile",
          core_nh67 == FROZEN_CORE_NH67
          and max(core_d50) <= FROZEN_CORE_D50_MAX + 1e-6,
          "core nh67=%d max d50=%.4f" % (core_nh67, max(core_d50)))
    check("G25-MAIN-entry-2N5",
          n_entry == 85,
          "first_neg > n0=floor(2N/5) on %d/85" % n_entry)

    dead_ok = True
    dead_bits = []
    for kz in DEAD_CHI3:
        mz = chi_mz(kz, DMF.Q_CHI3)
        fl = flanking_stats(mz["wu"])
        J = signed_jacobi(mz["xu"], mz["wu"], int(mz["Nw"]) + 3)
        fn = J["first_neg"]
        okd = fl["F1"] and fl["F23"] and (
            fn is None or fn >= n0_of(int(mz["Nw"])))
        dead_ok = dead_ok and okd
        dead_bits.append("chi3-%d rmax=%.3f fn=%s F23=%s"
                         % (kz, fl["rmax"], fn, fl["F23"]))
    mz4 = chi_mz(DEAD_CHI4[0], DMF.Q_CHI4)
    fl4 = flanking_stats(mz4["wu"])
    J4 = signed_jacobi(mz4["xu"], mz4["wu"], int(mz4["Nw"]) + 3)
    ok4 = fl4["F1"] and fl4["F23"] and (
        J4["first_neg"] is None
        or J4["first_neg"] >= n0_of(int(mz4["Nw"])))
    dead_ok = dead_ok and ok4
    dead_bits.append("chi4-20 rmax=%.3f fn=%s F23=%s"
                     % (fl4["rmax"], J4["first_neg"], fl4["F23"]))
    check("G26-dead-chi-satisfy-B", dead_ok, "; ".join(dead_bits))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    print("PIVOT ENTRY "
          + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
