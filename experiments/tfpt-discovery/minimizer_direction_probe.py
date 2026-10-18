#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""minimizer_direction_probe -- hunt the closed form of the
empirical minimizer limit direction.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256 + FULL candidate list hashed) before running.

CONTEXT (minimizer_profile_probe, PROFILE-DIVERGES): the deployed
2-mode minimizer converges INTERNALLY (deep-third dispersion
0.0217 rad) to the empirical direction (0.6256, -0.7802), slope
r* = v2/v1 ~ -1.247, but matches neither frozen candidate (RAY-
orthogonal 0.45 rad away, arch bottom eigenvector 1.10 rad away).
If r* has a closed form, the exact warded expansion machinery
(the 2x2 Schur identity) applies immediately.

BONFERRONI DISCIPLINE (frozen): one target number, 15 candidates.
A point match near -1.247 alone counts for NOTHING (the tail
slope band is ~ +-0.05, dense with 'nice' constants).  A winner
must (i) have a-priori structural provenance (typed per
candidate), (ii) beat the internal dispersion floor 0.0217 rad on
the deep-tail median angle, and (iii) show a DECREASING angle
trend along the ladder (a true limit is approached, not merely
grazed).

VERDICT (frozen precedence): DIRECTION-BLOCKED (ward fails) /
DIRECTION-TRANSIENT (the tail slope is still drifting: deep-
quarter median shift > 2x tail IQR -- the honest null) /
DIRECTION-CLOSED-FORM (a winner passes all three bars; the
two-term law re-derived in its frame, payoff reported exactly) /
DIRECTION-ARITHMETIC (no winner; the direction's comb-
sensitivity measured -- if it moves under comb thinning or
weight perturbation at fixed arch, the direction IS arithmetic
content and the route closes with that typing).

FIREWALL: prime + archimedean data only (no zeros); sibling
probes READ-ONLY; RNG only in the declared perturbation control;
report only.
"""

import hashlib
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import spectral_flow_pivot_probe as sfp        # noqa: E402 (READ-ONLY)
import minimizer_profile_probe as mp           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
minimizer_direction_probe spec v1 (2026-08-07, frozen before run).
Target: the deployed 2-mode minimizer's limit direction; sharpened
as the sign-aligned entrywise median of v_min over the last 11
rungs (TAIL), band = angle IQR over the tail.  Drift: TRANSIENT
iff |med(r, last quarter) - med(r, previous quarter)| > 2 x
IQR(r, last 11) over the deep half (r = slope v2/v1).
Winner bars: deep-tail (last 11) median angle <= 0.0217 rad AND
trend decreasing (med(angle, last 11) < med(angle, previous 11)
AND polyfit slope of angle vs log h over the deep half < 0).
If several pass, smallest angle wins.  Payoff (winner only,
informational for best otherwise): q22/tau and correction share
in the candidate frame, deep-tail medians.
Comb-sensitivity (no-winner branch): kz deepest + kz 9; thinning
uu[::2] mm[::2]; weight perturbation mm*(1+0.01 N(0,1)) seed
20260808; sensitive iff direction shift > 0.0217 rad.
Census regression: deepest minimizer == (0.625550, -0.780184)
within 1e-5 per component; tail dispersion 0.0217 +- 0.005;
scramble/Epstein contrasts 1.5387 / 0.3079 within 2e-3.
NO RH claim; report only."""

CANDIDATES_TXT = """\
FROZEN CANDIDATE LIST (derivation BEFORE evaluation; slopes are
v2/v1; direction = (1, r)/sqrt(1+r^2) unless stated):
C01 ARCH-BOT-ASY : bottom eigenvector of the tail-median
    Frobenius-normalized arch block Bhat (the asymptotic arch
    direction as the window scales -- the task's leading
    structural candidate; rung-wise arch bottom already failed
    at 1.10 rad, this is the extrapolated limit object).
C02 ARCH-TOP-ASY : top eigenvector of Bhat (B is negative
    definite; its top = least-negative arch direction).
C03 COMB-BOT-ASY : bottom eigenvector of the tail-median
    normalized comb block Chat (density-transversal structure:
    the comb's own soft direction).
C04 COMB-TOP-ASY : top eigenvector of Chat (the comb's stiff
    direction; tau_pnt-structure proxy at U0 order).
C05 r = -5/4       : the compiler null ray (5,-3,4) component
    ratio t/y = 2.5/2 (deployed ray constants only).
C06 r = -sqrt(3/2) : IF a11/a22 -> 3/2 (the integer-scan hit of
    the profile probe) AND det -> 0, the kernel slope is
    -a11/a12 = -sqrt(a11/a22) = -sqrt(3/2).
C07 r = -sqrt(14)/3: slope^2 = 14/9, i.e. a11/a22 -> 14/9 under
    the same kernel reading (provenance CONDITIONAL on the
    measured entry ratio -- typed weak, point-match suspect).
C08 r = -4/pi      : arch/pole read constant (Fejer/Dirichlet
    normalization in the arch integrals).
C09 r = -pi^2/8    : arch integral constant (sum 1/odd^2).
C10 r = -sqrt(pi/2): Gaussian arch normalization constant.
C11 r = -1         : the alternating parity direction (1,-1).
C12 r = -(1+sqrt5)/2: golden ratio (predeclared distant control
    -- expected to FAIL; calibrates the Bonferroni floor).
C13 r = -log(7/2)  : the user's example; provenance WEAK (no
    deployed derivation) -- typed, point-match suspect.
C14 PARITY-UNI     : first two parity-mode coefficients of the
    uniform window direction ones(M) under the deployed
    compression Tb at the deepest rung (image of the natural
    uniform direction).
C15 PARITY-ALT     : same for the alternating window direction
    (-1)^k (image of the natural alternating direction)."""

TAIL = 11
FLOOR = 0.0217
SENS_SEED = 20260808
CENSUS_V = (0.625550, -0.780184)
CENSUS_SCR = 1.5387
CENSUS_EPS = 0.3079


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def slope_dir(r):
    return unit([1.0, r])


def run():
    print("=" * 78)
    print("MINIMIZER DIRECTION (minimizer_direction_probe) -- the "
          "closed form of the limit direction")
    print("=" * 78)
    print("frozen spec sha256      = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("candidate list sha256   = %s  (hashed BEFORE any "
          "evaluation)"
          % hashlib.sha256(CANDIDATES_TXT.encode())
          .hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim; Bonferroni discipline as frozen in
the header -- a point match near -1.247 counts for nothing
without the angle floor AND the decreasing trend.""")

    # ============================================================== S0
    print("\nS0 -- census regression (the target reproduces)")
    rungs = []
    for kz in core.frame_a_zones():
        al = float(core.U_ALL[kz])
        Dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(al / Dk - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if M // 2 == sfp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * al) > core.ATOM_MAX + 0.5:
            continue
        rungs.append(kz)
    tab = []
    for kz in rungs:
        bl = sfp.rung_blocks(kz)
        A2 = (bl["A_arch"] + bl["A_comb"])[:2, :2]
        B2 = bl["A_arch"][:2, :2]
        C2 = bl["A_comb"][:2, :2]
        tau, vmin, lmax, _ = mp.min_eig2(A2)
        if vmin[0] < 0:
            vmin = -vmin
        tab.append(dict(kz=kz, h=bl["h"], M=bl["M"], A2=A2, B2=B2,
                        C2=C2, tau=tau, vmin=vmin, lmax=lmax))
    hs = np.array([float(t_["h"]) for t_ in tab])
    v_deep = tab[-1]["vmin"]
    ok_census = (abs(v_deep[0] - CENSUS_V[0]) <= 1e-5
                 and abs(v_deep[1] - CENSUS_V[1]) <= 1e-5)
    tail_v = np.array([t_["vmin"] for t_ in tab[-TAIL:]])
    v_star = unit(np.median(tail_v, axis=0))
    tail_ang = np.array([mp.ang(t_["vmin"], v_star)
                         for t_ in tab[-TAIL:]])
    third = max(len(tab) // 3, 1)
    disp3 = np.array([mp.ang(t_["vmin"], v_deep)
                      for t_ in tab[-third:]])
    ok_disp = abs(float(np.median(disp3)) - FLOOR) <= 0.005
    check("S0.CEN census regression: deepest minimizer (%.6f, "
          "%.6f) == frozen (%.6f, %.6f) within 1e-5 AND deep-"
          "third dispersion %.4f == %.4f +- 0.005"
          % (v_deep[0], v_deep[1], CENSUS_V[0], CENSUS_V[1],
             float(np.median(disp3)), FLOOR),
          ok_census and ok_disp)
    rr = np.array([t_["vmin"][1] / t_["vmin"][0] for t_ in tab])
    r_star = float(np.median(rr[-TAIL:]))
    r_iqr = float(np.percentile(rr[-TAIL:], 75)
                  - np.percentile(rr[-TAIL:], 25))
    print("    SHARPENED TARGET: tail-median direction v* = "
          "(%.6f, %.6f); slope r* = %.6f, tail IQR %.4f, tail "
          "angle band (IQR) %.4f rad"
          % (v_star[0], v_star[1], r_star, r_iqr,
             float(np.percentile(tail_ang, 75)
                   - np.percentile(tail_ang, 25))))

    # ============================================================== S1
    print("\nS1 -- drift analysis (is r* a transient?)")
    half = len(tab) // 2
    r_half = rr[-half:]
    q_len = half // 2
    r_q4 = r_half[-q_len:]
    r_q3 = r_half[:q_len]
    d_med = float(np.median(r_q4) - np.median(r_q3))
    iqr_tail = float(np.percentile(rr[-TAIL:], 75)
                     - np.percentile(rr[-TAIL:], 25))
    drifting = abs(d_med) > 2.0 * max(iqr_tail, 1e-12)
    sl_h1 = np.polyfit(1.0 / hs[-half:], rr[-half:], 1)
    sl_h12 = np.polyfit(1.0 / np.sqrt(hs[-half:]), rr[-half:], 1)
    print("    deep-half quarters: med(r, Q3) = %.6f -> med(r, "
          "Q4) = %.6f, shift %.6f vs 2x tail IQR %.6f -> %s"
          % (float(np.median(r_q3)), float(np.median(r_q4)),
             d_med, 2.0 * iqr_tail,
             "STILL DRIFTING" if drifting else "settled at this "
             "depth"))
    print("    extrapolations (deep half): r(1/h -> 0) = %.6f "
          "(coef %.3f); r(1/sqrt h -> 0) = %.6f (coef %.3f) -- "
          "the drift law typed"
          % (sl_h1[1], sl_h1[0], sl_h12[1], sl_h12[0]))

    # ============================================================== S2
    print("\nS2 -- the frozen candidate list (derivations above "
          "evaluation)")
    print(CANDIDATES_TXT)
    Bh = np.median(np.array([t_["B2"]
                             / np.linalg.norm(t_["B2"])
                             for t_ in tab[-TAIL:]]), axis=0)
    Ch = np.median(np.array([t_["C2"]
                             / np.linalg.norm(t_["C2"])
                             for t_ in tab[-TAIL:]]), axis=0)
    _, b_bot, _, b_top = mp.min_eig2(0.5 * (Bh + Bh.T))
    _, c_bot, _, c_top = mp.min_eig2(0.5 * (Ch + Ch.T))
    h_d = tab[-1]["h"]
    Tb_d = core.parity_basis(h_d, min(sfp.K_MODES, h_d))
    uni = Tb_d @ np.ones(h_d)
    alt = Tb_d @ np.array([(-1.0) ** k for k in range(h_d)])
    cands = [
        ("C01 ARCH-BOT-ASY", unit(b_bot)),
        ("C02 ARCH-TOP-ASY", unit(b_top)),
        ("C03 COMB-BOT-ASY", unit(c_bot)),
        ("C04 COMB-TOP-ASY", unit(c_top)),
        ("C05 -5/4", slope_dir(-1.25)),
        ("C06 -sqrt(3/2)", slope_dir(-math.sqrt(1.5))),
        ("C07 -sqrt(14)/3", slope_dir(-math.sqrt(14.0) / 3.0)),
        ("C08 -4/pi", slope_dir(-4.0 / math.pi)),
        ("C09 -pi^2/8", slope_dir(-math.pi ** 2 / 8.0)),
        ("C10 -sqrt(pi/2)", slope_dir(-math.sqrt(math.pi / 2.0))),
        ("C11 -1", slope_dir(-1.0)),
        ("C12 -(1+sqrt5)/2", slope_dir(-(1 + math.sqrt(5)) / 2)),
        ("C13 -log(7/2)", slope_dir(-math.log(3.5))),
        ("C14 PARITY-UNI", unit(uni[:2])),
        ("C15 PARITY-ALT", unit(alt[:2])),
    ]

    # ============================================================== S3
    print("\nS3 -- the test: angle floor %.4f rad + decreasing "
          "trend" % FLOOR)
    print("    %-18s %9s %9s %9s %6s %6s"
          % ("candidate", "slope", "tail-med", "prev-med",
             "trend", "PASS"))
    results = []
    for nm, u in cands:
        angs = np.array([mp.ang(t_["vmin"], u) for t_ in tab])
        tail_med = float(np.median(angs[-TAIL:]))
        prev_med = float(np.median(angs[-2 * TAIL:-TAIL]))
        sl = float(np.polyfit(np.log(hs[-half:]), angs[-half:],
                              1)[0])
        trend_ok = (tail_med < prev_med) and (sl < 0)
        passed = (tail_med <= FLOOR) and trend_ok
        results.append((nm, u, tail_med, prev_med, trend_ok,
                        passed))
        print("    %-18s %9.4f %9.4f %9.4f %6s %6s"
              % (nm, u[1] / u[0] if abs(u[0]) > 1e-12
                 else math.inf, tail_med, prev_med,
                 "down" if trend_ok else "no",
                 "PASS" if passed else "-"))
    winners = [r_ for r_ in results if r_[5]]
    winners.sort(key=lambda r_: r_[2])
    best = min(results, key=lambda r_: r_[2])
    check("S3.CAL Bonferroni calibration: the predeclared distant "
          "control C12 does NOT pass (floor+trend bars reject a "
          "non-limit)", not [w for w in winners
                             if w[0].startswith("C12")])
    print("    winners: %s; best (informational): %s at tail-med "
          "%.4f rad"
          % ([w[0] for w in winners] if winners else "NONE",
             best[0], best[2]))

    # ============================================================== S4
    print("\nS4 -- the payoff frame (winner, else best "
          "informational)")
    u2 = winners[0][1] if winners else best[1]
    nm4 = winners[0][0] if winners else best[0] + " (NO WINNER "\
        "-- informational only)"
    q22s, shares, lead_r = [], [], []
    for t_ in tab:
        q11v, q22v, q12v = mp.frame_q(t_["A2"], u2)
        corr = q12v * q12v / (q11v - t_["tau"])
        q22s.append(q22v)
        shares.append(corr / max(q22v, 1e-300))
        lead_r.append(q22v / t_["tau"])
    taus = np.array([t_["tau"] for t_ in tab])
    lmaxs = np.array([t_["lmax"] for t_ in tab])
    print("    frame %s: q22/tau tail med %.3e; correction share "
          "tail med %.6f; criticality check: needed angle "
          "sqrt(tau/lmax) tail med %.3e rad vs achieved tail "
          "angle %.4f rad"
          % (nm4, float(np.median(np.array(lead_r)[-TAIL:])),
             float(np.median(np.array(shares)[-TAIL:])),
             float(np.median(np.sqrt(taus / lmaxs)[-TAIL:])),
             best[2] if not winners else winners[0][2]))

    # ============================================================== S5
    print("\nS5 -- controls + comb-sensitivity")
    al9 = float(core.U_ALL[9])
    ka9 = core.atoms_in(al9)
    rng = np.random.default_rng(mp.SCR_SEED)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * al9, size=ka9))
    bl_s = sfp.rung_blocks(9, uu=uu_s, mm=core.MU_ALL[:ka9])
    _, v_s2, _, _ = mp.min_eig2((bl_s["A_arch"]
                                 + bl_s["A_comb"])[:2, :2])
    v_true9 = tab[[t_["kz"] for t_ in tab].index(9)]["vmin"]
    a_scr = mp.ang(v_s2, v_true9)
    uuE, mmE = mp.epstein_comb()
    bl_e = sfp.rung_blocks(9, uu=uuE, mm=mmE)
    _, v_e2, _, _ = mp.min_eig2((bl_e["A_arch"]
                                 + bl_e["A_comb"])[:2, :2])
    a_eps = mp.ang(v_e2, v_true9)
    check("S5.REG scramble/Epstein contrasts reproduce: %.4f vs "
          "frozen %.4f AND %.4f vs frozen %.4f (within 2e-3)"
          % (a_scr, CENSUS_SCR, a_eps, CENSUS_EPS),
          abs(a_scr - CENSUS_SCR) <= 2e-3
          and abs(a_eps - CENSUS_EPS) <= 2e-3)
    sens = {}
    rng2 = np.random.default_rng(SENS_SEED)
    for tag, kz_s in (("deepest", tab[-1]["kz"]), ("kz9", 9)):
        al_s = float(core.U_ALL[kz_s])
        ka_s = core.atoms_in(al_s)
        uu0 = np.asarray(core.U_ALL[:ka_s], float)
        mm0 = np.asarray(core.MU_ALL[:ka_s], float)
        v_ref = tab[[t_["kz"] for t_ in tab].index(kz_s)]["vmin"]
        bl_t = sfp.rung_blocks(kz_s, uu=uu0[::2], mm=mm0[::2])
        _, v_t, _, _ = mp.min_eig2((bl_t["A_arch"]
                                    + bl_t["A_comb"])[:2, :2])
        bl_p = sfp.rung_blocks(
            kz_s, uu=uu0,
            mm=mm0 * (1.0 + 0.01 * rng2.standard_normal(ka_s)))
        _, v_p, _, _ = mp.min_eig2((bl_p["A_arch"]
                                    + bl_p["A_comb"])[:2, :2])
        sens[tag] = (mp.ang(v_t, v_ref), mp.ang(v_p, v_ref))
        print("    comb-sensitivity (%s): thinning uu[::2] moves "
              "the direction %.4f rad; 1%% weight perturbation "
              "moves it %.4f rad (floor %.4f)"
              % (tag, sens[tag][0], sens[tag][1], FLOOR))

    # ============================================================== S6
    print("\nS6 -- verdict")
    wards_ok = not FAILS
    if not wards_ok:
        verdict = "DIRECTION-BLOCKED"
    elif drifting:
        verdict = "DIRECTION-TRANSIENT"
    elif winners:
        verdict = "DIRECTION-CLOSED-FORM"
    else:
        verdict = "DIRECTION-ARITHMETIC"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "DIRECTION-TRANSIENT":
        print("""    THE HONEST NULL: the tail slope is still drifting (deep-half
    quarter shift %.6f > 2x tail IQR %.6f) -- r* = %.4f is a
    depth-limited snapshot, not a limit.  The extrapolation laws
    (S1) give r(1/h->0) = %.6f and r(1/sqrt h->0) = %.6f; no
    candidate identification is honest at this precision.  The
    census-level fact stands: the minimizer direction is
    internally coherent (dispersion %.4f rad) but its limit is
    not resolved by 67 rungs.  Consequence: the closed-form hunt
    needs deeper rungs or the entry-asymptotics route (the three
    frame coefficients), not a longer candidate list."""
              % (d_med, 2.0 * iqr_tail, r_star, sl_h1[1],
                 sl_h12[1], float(np.median(disp3))))
    elif verdict == "DIRECTION-CLOSED-FORM":
        w = winners[0]
        print("""    WINNER: %s (tail-median angle %.4f rad < floor %.4f,
    trend decreasing).  Payoff (S4): q22/tau tail med %.3e,
    correction share %.6f -- %s"""
              % (w[0], w[2], FLOOR,
                 float(np.median(np.array(lead_r)[-TAIL:])),
                 float(np.median(np.array(shares)[-TAIL:])),
                 "the leading law CARRIES the floor at tau scale"
                 if float(np.median(np.array(shares)[-TAIL:]))
                 <= 0.05 else
                 "the leading law still does NOT carry the floor "
                 "at tau scale (the needed angle is sqrt(tau/"
                 "lmax) ~ 3e-4 rad; the identification is exact "
                 "in the limit but the finite-rung deviation "
                 "keeps the curvature correction dominant -- "
                 "typed)"))
    elif verdict == "DIRECTION-ARITHMETIC":
        print("""    NO WINNER: no predeclared structural candidate reaches the
    dispersion floor %.4f rad with a decreasing trend (best: %s
    at %.4f rad).  Comb-sensitivity (S5): thinning moves the
    direction by %.4f rad (deepest) / %.4f rad (kz9); 1%% weight
    perturbation by %.4f / %.4f rad -- %s.  THE TYPED CLOSURE:
    the limit direction is arithmetic content itself -- it is
    set by the deployed prime comb, not by the arch geometry or
    any deployed constant on the list; the minimizer-profile
    route to an analytic constant closes here with the wall
    localized IN the direction (the same arithmetic that sets
    tau's size sets where the minimizer points)."""
              % (FLOOR, best[0], best[2],
                 sens["deepest"][0], sens["kz9"][0],
                 sens["deepest"][1], sens["kz9"][1],
                 "COMB-SENSITIVE (the direction moves above the "
                 "floor under comb surgery at fixed arch)"
                 if max(sens["deepest"][0], sens["kz9"][0],
                        sens["deepest"][1],
                        sens["kz9"][1]) > FLOOR
                 else "comb-INSENSITIVE at this depth (the "
                 "direction survives comb surgery -- then the "
                 "list, not the arithmetic, is the gap; typed)"))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")


if __name__ == "__main__":
    run()
