#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""postcap_pivots_probe -- LEMMA.POSTCAP_PIVOTS.01 (round 377):
THE TWO-WAY PIVOT CENSUS of the signed source.

Coexistence: R374/R375/R376 and the parallel compose/Sol lanes
run in parallel -- this probe touches NOTHING outside its own
file and the strictly additive rh-sync.  next.txt is NOT written.

THE FROZEN QUESTION.  In the Fable source-pivot coordinate, with
monic Jacobi norms h_j = H_{j+1}(w)/H_j(w) of the original signed
weight w on the cosine grid (S=2N-1):

  P1  <=>  ind_- H_{N+2}(w) <= 1
  P2  <=>  h_N(w) * h_{N+1}(w) < 0

Does the first negative pivot of every canonical window sit in
{h_N, h_{N+1}} (the measured half-filling pinning as a post-cap
location), or does the defect wander?

THIS ROUND DECIDES by a sealed two-way census of 85 MAIN + 84
character-twisted windows, plus a named scramble break.  Lemma
identities live in rh/problem/postcap_pivots.tex and
verify_postcap_steps.py; this probe is the census only.

SEALED BEFORE EVALUATION (construction, not a fit):
  * signed Stieltjes three-term recurrence on (xu, wu) -- the
    unique numerically stable readout of sign(h_j) for signed
    atomic weights (V.mu_chain uses sqrt(w) and is forbidden here);
  * prefix window 0..N+1 for P1 (nneg_pref = # negatives among
    h_0..h_{N+1}); product sN*sNp1 for P2;
  * classes PINNED_N / PINNED_Np1 / LATE / NONE / EARLY / DOUBLE /
    MULTI, with LATE = first_neg in {N+2, N+3} and NONE = no
    sign change by N+3 (hunt to N+16 recorded, class frozen on
    the N+3 window);
  * MAIN ladder = 42 core + 15 r286 ext + 12 EXT3 + 6 EXT4 +
    6 EXT5 + 4 EXT6 = 85; chi = admissible_indices x {chi3, chi4}
    = 84; dead sprouts DEAD_CHI3=(15,19,23,33,39), DEAD_CHI4=(20,);
    scramble = HS.window_data(9, scramble_seed=1).

CALIBRATION DISCLOSURE.  The class tallies were first measured
in /tmp (r377_census.py) on the same constructors.  The frozen
counts below are that measurement, sealed as gates -- not a
search over classification rules.

FROZEN TALLIES (N+3 window):
  MAIN 85: PINNED_N 19, PINNED_Np1 31, LATE 23, NONE 12,
           DOUBLE 0, EARLY 0, MULTI 0;
           P2 50/85, P1 (nneg<=1) 85/85, free window 85/85.
  CHI3 42: PINNED_N 8, PINNED_Np1 13, LATE 18, NONE 3;
           P2 21/42, P1 42/42.
  CHI4 42: PINNED_N 4, PINNED_Np1 15, LATE 23, NONE 0;
           P2 19/42, P1 42/42.
  SCR w9: EARLY, first_neg=21, nneg_pref=37.
  core-42 PINNED_N kzs (18):
    9,14,21,24,27,31,32,34,38,44,46,48,52,55,59,60,78,82
    (the r241 delta=0 set).  Full-85 PINNED_N also includes 109.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r367
final_two_rank_inertia (FTI, dictionary cross-check on smoke
pins only), r357 dirichlet_matched_frame (DMF), r286
lstar_margin_scaling (LM.ext_rule), r-ext3 anchors (E3 constants
copied as frozen kz tuples matching FTI), r226 hirota_sign
(HS.window_data scramble), verify_lstar_instance (V.build_measures),
pair_extremal (PX.pair_select, smoke dictionary only).

NO RH CLAIM.  Finite census of a named construction family.
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
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402

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
CORE_PINNED_N = (9, 14, 21, 24, 27, 31, 32, 34, 38, 44, 46, 48,
                 52, 55, 59, 60, 78, 82)

FROZEN_MAIN = dict(n=85, PINNED_N=19, PINNED_Np1=31, LATE=23, NONE=12,
                   DOUBLE=0, EARLY=0, MULTI=0, P2=50, P1=85, free=85)
FROZEN_CHI3 = dict(n=42, PINNED_N=8, PINNED_Np1=13, LATE=18, NONE=3,
                   P2=21, P1=42)
FROZEN_CHI4 = dict(n=42, PINNED_N=4, PINNED_Np1=15, LATE=23, NONE=0,
                   P2=19, P1=42)
SCR_FIRST, SCR_NNEG = 21, 37
# first_neg on NONE rows (N+16 hunt); offset = first_neg - N in {4,5,8}
FROZEN_NONE_HUNT = {
    43: 844, 50: 845, 73: 1028, 42: 2477, 96: 2393, 72: 3026,
    113: 3117, 107: 5676, 115: 4248, 89: 4242, 133: 7947, 117: 6540,
}

DMF_SHA_PREFIX = "4bf1a94b"
PX_SHA_PREFIX = "b09f8ccd"
LM_SHA_PREFIX = "0a44ac4e"
E3_SHA_PREFIX = "bbfaf199"
FTI_SHA_PREFIX = "e0d79840"

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


def pivot_signs(x, w, nmax):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    eta = float(np.dot(w, q * q))
    signs = [int(np.sign(eta)) if eta != 0 else 0]
    log_s = 0.0
    log_sm = 0.0
    etam = 1.0
    for _n in range(nmax):
        if abs(eta) < 1e-300:
            signs.append(0)
            break
        al = float(np.dot(w, x * q * q)) / eta
        if _n == 0:
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
    return signs


def classify(sg, N):
    first = next((j for j, s in enumerate(sg) if s < 0), None)
    nneg = sum(1 for s in sg[:N + 2] if s < 0)
    sN = sg[N] if len(sg) > N else 0
    sNp1 = sg[N + 1] if len(sg) > N + 1 else 0
    free = all(s > 0 for s in sg[:N])
    if first is None:
        cls = "NONE"
        off = None
    else:
        off = first - N
        if not free:
            cls = "EARLY"
        elif nneg > 1:
            cls = "MULTI"
        elif sN < 0 and sNp1 > 0:
            cls = "PINNED_N"
        elif sN > 0 and sNp1 < 0:
            cls = "PINNED_Np1"
        elif sN < 0 and sNp1 < 0:
            cls = "DOUBLE"
        elif first > N + 1:
            cls = "LATE"
        else:
            cls = "OTHER"
    return dict(cls=cls, first_neg=first, nneg_pref=nneg,
                sN=int(sN), sNp1=int(sNp1), offset=off,
                free=bool(free))


def row_from_mz(tag, kz, mz, nmax_extra=3):
    N = int(mz["Nw"])
    sg = pivot_signs(mz["xu"], mz["wu"], N + nmax_extra)
    c = classify(sg, N)
    c.update(tag=tag, kz=int(kz), N=N, S=int(mz["S"]))
    return c


def main_ladder():
    core_kzs = list(V.admissible_indices())
    lm_rows = LM.ext_rule()
    ext_kzs = [t[1] for t in lm_rows[:15]]
    all_main = (core_kzs + ext_kzs + list(EXT3_KZ_B + EXT3_KZ_A)
                + list(EXT4_KZ_B + EXT4_KZ_A) + list(EXT5_KZ)
                + list(EXT6_KZ))
    return core_kzs, all_main


def tally(rows):
    c = Counter(r["cls"] for r in rows)
    n_p2 = sum(1 for r in rows if r["sN"] * r["sNp1"] < 0)
    n_p1 = sum(1 for r in rows if r["nneg_pref"] <= 1)
    n_free = sum(1 for r in rows if r["free"])
    return dict(n=len(rows), classes=dict(c), P2=n_p2, P1=n_p1,
                free=n_free)


def hunt_first(mz, N, cap=16):
    sg = pivot_signs(mz["xu"], mz["wu"], N + cap)
    first = next((j for j, s in enumerate(sg) if s < 0), None)
    return first


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("postcap_pivots_probe -- LEMMA.POSTCAP_PIVOTS.01 (round 377)")
    print("SPEC_SHA %s   (FTI %s / DMF %s / LM %s / E3 %s / PX %s)"
          % (SPEC_SHA[:16], FTI.SPEC_SHA[:16], DMF.SPEC_SHA[:16],
             LM.SPEC_SHA[:16], E3.SPEC_SHA[:16], PX.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (five pins + scramble + dead chi)"
                        if smoke else "FULL CENSUS 85 MAIN + 84 chi"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX))
    check("G02-import-sha", sha_ok,
          "DMF %s / PX %s / LM %s / E3 %s / FTI %s"
          % (DMF.SPEC_SHA[:8], PX.SPEC_SHA[:8], LM.SPEC_SHA[:8],
             E3.SPEC_SHA[:8], FTI.SPEC_SHA[:8]))

    section("S1  SMOKE PINS")
    mz9 = V.build_measures(MAIN_KZ)
    r9 = row_from_mz("MAIN", MAIN_KZ, mz9)
    j1, j2 = PX.pair_select(mz9["yn"])
    o9 = FTI.cut_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                      mz9["Nw"], mz9["S"], mz9["L"], j1, j2)
    check("G10-w9-PINNED_N",
          r9["cls"] == "PINNED_N" and r9["first_neg"] == r9["N"]
          and r9["nneg_pref"] == 1 and o9["detK"] < 0
          and o9["nneg"] == 1,
          "N=%d first=%s nneg=%d detK=%+.4f nnegA=%d"
          % (r9["N"], r9["first_neg"], r9["nneg_pref"],
             o9["detK"], o9["nneg"]))

    mz12 = V.build_measures(12)
    r12 = row_from_mz("MAIN", 12, mz12)
    j1, j2 = PX.pair_select(mz12["yn"])
    o12 = FTI.cut_rung(mz12["xu"], mz12["wu"], mz12["yn"], mz12["vn"],
                       mz12["Nw"], mz12["S"], mz12["L"], j1, j2)
    check("G11-kz12-LATE",
          r12["cls"] == "LATE" and r12["first_neg"] == r12["N"] + 2
          and r12["sN"] * r12["sNp1"] > 0 and r12["nneg_pref"] == 0
          and o12["nneg"] == 0 and o12["detK"] > 0 and o12["Mpd"],
          "N=%d first=%s detK=%+.4f nnegA=%d Mpd=%s"
          % (r12["N"], r12["first_neg"], o12["detK"],
             o12["nneg"], o12["Mpd"]))

    mz15 = V.build_measures(15)
    r15 = row_from_mz("MAIN", 15, mz15)
    check("G12-kz15-PINNED_Np1",
          r15["cls"] == "PINNED_Np1"
          and r15["first_neg"] == r15["N"] + 1
          and r15["sN"] * r15["sNp1"] < 0,
          "N=%d first=%s sN sN+1=%+d%+d"
          % (r15["N"], r15["first_neg"], r15["sN"], r15["sNp1"]))

    uu, ww, _nn, _ch = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(MAIN_KZ, uu, ww, 1.0, DMF.LPQ3)
    rc3 = row_from_mz("CHI3", MAIN_KZ, mzc)
    check("G13-chi3-w9-LATE",
          rc3["nneg_pref"] == 0 and rc3["first_neg"] == rc3["N"] + 2
          and rc3["cls"] == "LATE",
          "N=%d first=%s nneg=%d cls=%s"
          % (rc3["N"], rc3["first_neg"], rc3["nneg_pref"], rc3["cls"]))

    uu15, ww15, _n15, _c15 = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mz_d = DMF.chi_build_measures(15, uu15, ww15, 1.0, DMF.LPQ3)
    rd = row_from_mz("CHI3", 15, mz_d)
    check("G14-dead-chi3-15",
          rd["nneg_pref"] <= 1 and rd["free"]
          and rd["cls"] == "PINNED_Np1",
          "dead chi3-15 cls=%s nneg=%d first=%s"
          % (rd["cls"], rd["nneg_pref"], rd["first_neg"]))

    d = HS.window_data(9, scramble_seed=SCR_SEED)
    xu = np.concatenate([d["xs"], d["ys"]])
    wu = np.concatenate([d["ws"], -d["vs"]])
    ord_ = np.argsort(xu)
    mz_s = dict(xu=xu[ord_], wu=wu[ord_], Nw=d["n_max"], S=len(xu))
    rs = row_from_mz("SCR", 9, mz_s)
    check("G15-scramble-EARLY",
          rs["cls"] == "EARLY" and rs["first_neg"] == SCR_FIRST
          and rs["nneg_pref"] == SCR_NNEG,
          "first=%s nneg=%d cls=%s" % (rs["first_neg"],
                                       rs["nneg_pref"], rs["cls"]))

    dict_ok = ((o9["detK"] < 0) == (r9["sN"] * r9["sNp1"] < 0)
               and (o12["detK"] < 0) == (r12["sN"] * r12["sNp1"] < 0))
    check("G16-dictionary-smoke", dict_ok,
          "w9 detK%+.3f product_neg=%s; kz12 detK%+.3f product_neg=%s"
          % (o9["detK"], r9["sN"] * r9["sNp1"] < 0,
             o12["detK"], r12["sN"] * r12["sNp1"] < 0))

    if smoke:
        n_fail = sum(1 for _n, ok in CHECKS if not ok)
        print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
              % (len(CHECKS) - n_fail, len(CHECKS),
                 "" if n_fail == 0 else "  ** FAIL **",
                 SPEC_SHA[:16], time.time() - T0))
        print("POSTCAP PIVOTS SMOKE "
              + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
        return 0 if n_fail == 0 else 1

    section("S2  FULL CENSUS")
    core_kzs, all_main = main_ladder()
    check("G20-ladder-size",
          len(core_kzs) == 42 and len(all_main) == 85,
          "core %d MAIN %d" % (len(core_kzs), len(all_main)))

    main_rows = []
    for kz in all_main:
        mz = V.build_measures(kz)
        main_rows.append(row_from_mz("MAIN", kz, mz))
    tm = tally(main_rows)
    cls = tm["classes"]
    check("G21-MAIN-classes",
          cls.get("PINNED_N", 0) == FROZEN_MAIN["PINNED_N"]
          and cls.get("PINNED_Np1", 0) == FROZEN_MAIN["PINNED_Np1"]
          and cls.get("LATE", 0) == FROZEN_MAIN["LATE"]
          and cls.get("NONE", 0) == FROZEN_MAIN["NONE"]
          and cls.get("DOUBLE", 0) == 0
          and cls.get("EARLY", 0) == 0
          and cls.get("MULTI", 0) == 0
          and tm["n"] == 85,
          "classes %s" % cls)
    check("G22-MAIN-P1-P2-free",
          tm["P1"] == 85 and tm["P2"] == 50 and tm["free"] == 85,
          "P1 %d/85  P2 %d/85  free %d/85"
          % (tm["P1"], tm["P2"], tm["free"]))
    core_pn = tuple(r["kz"] for r in main_rows[:42]
                    if r["cls"] == "PINNED_N")
    check("G23-core-PINNED_N-18",
          core_pn == CORE_PINNED_N,
          "core PINNED_N %s" % (core_pn,))

    chi3_rows = []
    for kz in core_kzs:
        uu, ww, _nn, _ch = DMF.chi_window_comb(kz, DMF.Q_CHI3)
        mz = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ3)
        r = row_from_mz("CHI3", kz, mz)
        r["dead"] = kz in DEAD_CHI3
        chi3_rows.append(r)
    t3 = tally(chi3_rows)
    c3 = t3["classes"]
    check("G24-CHI3-classes",
          t3["n"] == 42
          and c3.get("PINNED_N", 0) == FROZEN_CHI3["PINNED_N"]
          and c3.get("PINNED_Np1", 0) == FROZEN_CHI3["PINNED_Np1"]
          and c3.get("LATE", 0) == FROZEN_CHI3["LATE"]
          and c3.get("NONE", 0) == FROZEN_CHI3["NONE"]
          and t3["P1"] == 42 and t3["P2"] == 21,
          "classes %s P1 %d P2 %d" % (c3, t3["P1"], t3["P2"]))

    chi4_rows = []
    for kz in core_kzs:
        uu, ww, _nn, _ch = DMF.chi_window_comb(kz, DMF.Q_CHI4)
        mz = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ4)
        r = row_from_mz("CHI4", kz, mz)
        r["dead"] = kz in DEAD_CHI4
        chi4_rows.append(r)
    t4 = tally(chi4_rows)
    c4 = t4["classes"]
    check("G25-CHI4-classes",
          t4["n"] == 42
          and c4.get("PINNED_N", 0) == FROZEN_CHI4["PINNED_N"]
          and c4.get("PINNED_Np1", 0) == FROZEN_CHI4["PINNED_Np1"]
          and c4.get("LATE", 0) == FROZEN_CHI4["LATE"]
          and c4.get("NONE", 0) == FROZEN_CHI4["NONE"]
          and t4["P1"] == 42 and t4["P2"] == 19,
          "classes %s P1 %d P2 %d" % (c4, t4["P1"], t4["P2"]))

    dead3 = [r for r in chi3_rows if r.get("dead")]
    dead4 = [r for r in chi4_rows if r.get("dead")]
    check("G26-dead-still-P1",
          all(r["nneg_pref"] <= 1 and r["free"] for r in dead3 + dead4)
          and len(dead3) == 5 and len(dead4) == 1,
          "dead chi3 %s; dead chi4 %s"
          % ([(r["kz"], r["cls"]) for r in dead3],
             [(r["kz"], r["cls"]) for r in dead4]))

    none_rows = [r for r in main_rows if r["cls"] == "NONE"]
    hunts = {}
    for r in none_rows:
        mz = V.build_measures(r["kz"])
        hunts[r["kz"]] = hunt_first(mz, r["N"], cap=16)
    hunt_ok = all(h is None or h >= r["N"] + 4
                  for r in none_rows
                  for h in [hunts[r["kz"]]])
    check("G27-NONE-hunt-not-early",
          hunt_ok and len(none_rows) == 12
          and hunts == FROZEN_NONE_HUNT,
          "NONE hunts %s" % hunts)

    nneg1 = [r for r in main_rows if r["nneg_pref"] == 1]
    check("G28-nneg1-branch-alternation",
          len(nneg1) == 50
          and all(r["cls"] in ("PINNED_N", "PINNED_Np1")
                  and r["sN"] * r["sNp1"] < 0
                  for r in nneg1),
          "nneg-1 %d/50 all alternate in {h_N,h_{N+1}}"
          % len(nneg1))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    print("POSTCAP PIVOTS "
          + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
