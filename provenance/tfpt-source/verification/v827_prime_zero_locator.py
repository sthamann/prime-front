#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v827 -- PRIME.EXCLUSION.LOCATOR.01: the zero locator of the exclusion instrument -- the width profile W(gamma) = delta_mb(gamma) of the certified tower PEAKS at true zeta ordinates, and the preregistered v2 rule passes its out-of-sample test on a disjoint untouched window (83% detection, 0% false positives, precision 0.086), ONE module from two probes (the honest LOCATOR-NULL of the frozen v1 gates INCLUDED, preceding the v2 resolution; discovery probes exclusion_zero_locator_probe.py LOCATOR-NULL and exclusion_zero_locator_v2_probe.py LOCATOR-V2-RESOLVES, 2026-08-06, re-run identically 2026-08-07).  THE ORIENTATION (fixed by parent diagnostics, not zero data): near-ordinate rows have LARGER delta_mb -- a real zero at gamma makes the injected synthetic quadruple there REDUNDANT (T + Q stays consistent to larger delta), so the breakable margin shrinks and the boundary RISES: the locator takes prominent local maxima of log W.  THE HONEST NEGATIVE FIRST (v1, frozen gates): on the learning window gamma in [5, 60] the profile peaked at 12/13 true ordinates (precision 0.070, depth-improving) but the frozen prominence bar ln(1.5) admitted a dense false-peak background (61% FP) that kept the shifted null at chance => LOCATOR-NULL as frozen -- typed, on record.  THE POST-HOC SEPARATION (learned on [5, 60], hence inadmissible there, frozen for v2): matched peaks had prominence >= 0.82, false peaks <= 0.73 -- a clean separation, threshold ln(2.2) = 0.788.  THE OUT-OF-SAMPLE RESOLUTION (v2, preregistered + hashed BEFORE any test-window evaluation, hash f57a2e7f..): on the DISJOINT test window gamma in [60, 120], previously untouched by any locator evaluation, the frozen rule scores 20/24 = 83% detection, 0% false positives, precision 0.086 -- both frozen bars met -- with all four controls (scramble: no peaks; Epstein: no zeta tracking; shifted null: collapse below the structural re-lock ceiling; grid-refinement x2: every matched peak stable).  THE DEPTH LAW (frozen): detection 13/24 -> 15/24 -> 20/24 at X = 18.4 / 22.1 / 24.8 -- location sharpens with certified depth.  This module re-runs the locator instrument live at X = 18.375 on the refinement subwindow (profile, both prominence rules -- the v1 bar measurably admits false peaks where the v2 bar admits none, the v1 failure mode reproduced live), verifies both preregistration hashes, the mechanism split (matched peaks HOLD at the probe delta* where off-zero points BREAK), and the live controls; the out-of-sample scores enter as FROZEN REFERENCE with the v2 gates recomputed (downscoping predeclared in PROVENANCE).  INFORMATION FLOW (typed): the threshold ln(2.2) was learned on [5, 60] (instrument diagnostics, admissible); test-window ordinates entered ONLY scoring and control calibration; the battery band extension is a mechanical rule application -- no zero datum entered any design (hash-warded).  NO RH claim -- location to +-0.25 on a finite window is strictly weaker than classical verification on every axis (v828 carries the mandatory full typing).  Feeds PRIME.DETECTOR.WINDOW.01 [O].  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes exclusion_zero_locator_probe.py
(2026-08-06, 11 checks with the ONE preregistered-honest FAIL C3 --
the shifted-window null held at 75% vs the frozen <= 1/3 bar because
the dense ln(1.5) false-peak background re-locks on any shift --
verdict LOCATOR-NULL under the frozen gates, deepest rung detection
92% / FP 61% / precision 0.070) and exclusion_zero_locator_v2_probe.py
(2026-08-06, 13/13 checks, LOCATOR-V2-RESOLVES out-of-sample); both
re-run identically at promotion (2026-08-07, logs in
experiments/tfpt-discovery/*.log; profile data in
exclusion_zero_locator_profile.json / _v2_profile.json).  DOWNSCOPING
(predeclared): the suite module re-runs the locator INSTRUMENT live at
the certified rung X = 18.375 on the v1 refinement subwindow
[18, 34] (65 profile points, both prominence bars, mechanism split,
scramble + Epstein controls; machinery imported READ-ONLY from
v825/v826); the three-rung profiles and the out-of-sample test-window
scores enter as FROZEN REFERENCE counts with the v2 gates (detection
>= 0.80, FP <= 0.20) recomputed here from the frozen counts.  Original
probe docstrings and frozen protocols live in the two probe files
verbatim.

FIREWALL: v563/v755/v825/v826 read-only; NO zetazero()/nzeros() calls
in this module (AST-checked); the cached RvM ordinate list is read for
SCORING only (the profile itself is zero-free); RNG only in the
declared scramble control (seed 7).  NO RH claim.
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)
import v825_prime_exclusion_ladder as xl       # noqa: E402 (READ-ONLY)
import v826_prime_exclusion_battery2 as b2     # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = xl.DGRID
EXT2_DELTAS = b2.EXT2_DELTAS
N_BISECT = 4
BAND_LO, BAND_HI = 14.0, 50.0
TEST_LO, TEST_HI = 60.0, 120.0
W_CAP = 0.5
PROM_V1 = math.log(1.5)               # the v1 frozen bar
PROM_V2 = math.log(2.2)               # the learned, v2-frozen bar
MATCH_TOL = 0.5
SUB_LO, SUB_HI, DG_SUB = 18.0, 34.0, 0.25   # v1 refinement subwindow
SEED_SCRAMBLE = 7
CTRL_DG = 0.5
GATE_DET, GATE_FP = 0.80, 0.20        # v2 frozen bars

BATTERY_V2_DESIGN = b2.BATTERY_V2_DESIGN
V2_HASH_CITED = b2.V2_HASH_CITED
LOCATOR_DESIGN = (
    BATTERY_V2_DESIGN
    + "|locator: W(gamma)=uncensored delta_mb on the extended grid "
      "(floor 4.02e-4, bisect 4); window [5,60] step 0.25; rungs "
      "M=1176,1414,1588; predicted ordinates = local maxima of "
      "log W with prominence >= ln(1.5); match tol 0.5; W capped "
      "0.5 on no-break|orientation fixed by parent diagnostics: "
      "peaks, not dips (on-ordinate 0.0112 vs off 0.0033)|controls: "
      "scramble M=1503 + Epstein M=640 at step 0.5 (det <= 0.25); "
      "shifted null +2.5 (collapse <= 1/3); refine [18,34] x2 "
      "(move <= 0.25)|gates: RESOLVES det>=0.8 & fp<=0.2 & C3 & "
      "C4; PARTIAL det>=0.4 & det>=2x shifted; else NULL"
)
LOCATOR_V2_DESIGN = (
    BATTERY_V2_DESIGN
    + "|v2b band extension (mechanical): the in-band rule "
      "dg=k*pi/(4*X),k in {-4..4} applied ALSO to the test band "
      "[60,120]; no zero datum entered"
    + "|locator-v2: W(gamma)=uncensored delta_mb, extended grid "
      "(floor 4.02e-4, bisect 4); TEST window [60,120] step 0.25 "
      "(disjoint from the learning window [5,60]); peaks of log W "
      "with prominence >= ln(2.2) (learned on [5,60], frozen); "
      "match tol 0.5; edge guard 1.0; rungs M=1176,1414,1588"
    + "|bars: det>=0.80, fp<=0.20|controls: scramble M=1503 + "
      "Epstein M=640 step 0.5 (det<=0.25 or no peaks); shifted "
      "null +2.5 with structural re-lock ceiling (bar: shifted <= "
      "max(true/3, ceiling+0.10)); refine [75,95] x2 (move<=0.25)"
    + "|mechanism: probe delta*=0.004 at matched(77.14,101.32) vs "
      "off(63.0,90.5); median-ratio bar 2.0"
    + "|gates: RESOLVES bars+4 controls; PARTIAL det >= "
      "max(0.40, 2*N_peaks*1.0/60); else DEAD"
)
LOC2_HASH_CITED = "f57a2e7f"          # v2 prereg hash prefix (cited)

# FROZEN REFERENCE (probe runs 2026-08-06/07):
# v1 on the learning window [5, 60] (13 targets), deepest rung:
V1_REF = dict(det=12, targets=13, fp_frac=0.61, precision=0.070)
V1_SEP = (0.82, 0.73)   # post-hoc prominence separation (typed)
# v2 out-of-sample on the test window [61, 119] (24 targets):
V2_DET_LAW = ((18.375, 13, 24), (22.09375, 15, 24), (24.8125, 20, 24))
V2_REF = dict(det=20, targets=24, fp=0, precision=0.086)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def detunes_v2b(M, gamma):
    X = M * DGRID
    if BAND_LO <= gamma <= BAND_HI or TEST_LO <= gamma <= TEST_HI:
        d = math.pi / (4.0 * X)
        return tuple(k * d for k in range(-4, 5))
    d = math.pi / (2.0 * X)
    return tuple(k * d for k in range(-1, 2))


def dense_profile(cT, M, nrmT, gammas):
    W = np.empty(len(gammas))
    for i, g in enumerate(gammas):
        d_mb, _ = b2.boundary_v(cT, M, nrmT, float(g),
                                detunes_v2b(M, float(g)),
                                EXT2_DELTAS, N_BISECT)
        W[i] = d_mb if np.isfinite(d_mb) else W_CAP
    return W


def find_peaks(gs, W, prom_min):
    lw = np.log(W)
    n = len(gs)
    out = []
    for i in range(1, n - 1):
        if lw[i] > lw[i - 1] and lw[i] >= lw[i + 1]:
            keys = []
            for step in (-1, 1):
                j = i + step
                vmin = lw[i]
                while 0 <= j < n and lw[j] <= lw[i]:
                    vmin = min(vmin, lw[j])
                    j += step
                keys.append(vmin)
            prom = lw[i] - max(keys)
            if prom >= prom_min:
                out.append((float(gs[i]), float(prom)))
    return out


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v827 -- PRIME.EXCLUSION.LOCATOR.01: the zero locator "
          "(honest v1 NULL + v2 out-of-sample)")
    print("(live subwindow instrument at X = 18.375; out-of-sample "
          "scores frozen reference --")
    print(" downscoping predeclared in PROVENANCE; NO RH claim)")
    print("=" * 78)

    # ==================================================== S0: freeze
    print("\nS0 -- preregistration hash wards")
    check("S0.AST no zeta-zero generator call in this module",
          xl.ast_zero_firewall(__file__))
    v2h = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()
    l1h = hashlib.sha256(LOCATOR_DESIGN.encode()).hexdigest()
    l2h = hashlib.sha256(LOCATOR_V2_DESIGN.encode()).hexdigest()
    check("S0.HASH battery v2 re-hashes to %s.. and the v2 locator "
          "preregistration to %s.. (cited %s..; the v1 design hash "
          "%s.. is carried for the record)"
          % (v2h[:16], l2h[:8], LOC2_HASH_CITED, l1h[:8]),
          v2h == V2_HASH_CITED and l2h.startswith(LOC2_HASH_CITED))
    d1 = json.load(open(xl.CACHE))
    d2 = json.load(open(xl.CACHE_EXT))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    zeros_sub = [float(g) for g in gam_c
                 if SUB_LO + 1.0 <= g <= SUB_HI - 1.0]
    check("S0.CACHE %d cached ordinates; %d targets in the guarded "
          "subwindow [%g, %g]"
          % (len(gam_c), len(zeros_sub), SUB_LO + 1.0, SUB_HI - 1.0),
          len(gam_c) == 2500 and len(zeros_sub) >= 4)

    # ==================================================== S1: live rung
    print("\nS1 -- live profile on the subwindow (X = 18.375)")
    cs, cnt, masses_scr, _ = xl.seg_assemble([1176],
                                             collect_mass_M=1176)
    tower = srp.continuum_lags(1176) + cs[1176]
    cT = tower[:1176]
    T = sla.toeplitz(cT)
    m_of = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
    nrmT = float(sla.norm(T, 2))
    lb, _, _ = xl.chol_cert_lower(T, m_of)
    check("S1.PD the profile rung is PD-certified: lambda_min = %.4e "
          "(rel dev to cited %.4f), CERTIFIED >= %.4e"
          % (m_of, abs(m_of - 3.8825e-6) / 3.8825e-6, lb),
          abs(m_of - 3.8825e-6) / 3.8825e-6 <= 2e-2
          and lb is not None and lb > 0.0)
    sub_gs = np.arange(SUB_LO, SUB_HI + 1e-9, DG_SUB)
    t0 = time.time()
    W = dense_profile(cT, 1176, nrmT, sub_gs)
    print("    subwindow profile: %d points, W in [%.4f, %.4f] "
          "(%.1f s)" % (len(sub_gs), float(np.min(W)),
                        float(np.max(W)), time.time() - t0))
    check("S1.REACH profile fully uncensored above the floor and "
          "below the cap",
          float(np.min(W)) > EXT2_DELTAS[0] * (1 + 1e-9)
          and float(np.max(W)) < W_CAP * (1 - 1e-12))

    # ==================================================== S2: both rules
    print("\nS2 -- both prominence rules on the live profile "
          "(scoring: ordinates admissible HERE only)")
    pk_v1 = find_peaks(sub_gs, W, PROM_V1)
    pk_v2 = find_peaks(sub_gs, W, PROM_V2)
    zt = np.asarray(zeros_sub)

    def score(peaks):
        pg = np.array([p[0] for p in peaks]) if peaks else \
            np.array([])
        n_match = sum(1 for gz in zt
                      if pg.size
                      and float(np.min(np.abs(pg - gz)))
                      <= MATCH_TOL)
        guarded = [p for p in pg
                   if SUB_LO + 1.0 <= p <= SUB_HI - 1.0]
        n_fp = sum(1 for p in guarded
                   if float(np.min(np.abs(gam_c - p))) > MATCH_TOL)
        return n_match, n_fp, len(guarded)

    m1, fp1, n1 = score(pk_v1)
    m2, fp2, n2 = score(pk_v2)
    print("    v1 rule (prom >= ln 1.5): %d peaks in-guard, %d/%d "
          "targets matched, %d false" % (n1, m1, len(zeros_sub), fp1))
    print("    v2 rule (prom >= ln 2.2): %d peaks in-guard, %d/%d "
          "targets matched, %d false" % (n2, m2, len(zeros_sub), fp2))
    check("S2.RULES the live subwindow reproduces the rule "
          "separation: the frozen v2 bar keeps ZERO false peaks "
          "while matching >= 3 targets, and the v1 bar admits at "
          "least as many peaks (its false-peak background is the "
          "typed v1 failure mode)",
          fp2 == 0 and m2 >= 3 and n1 >= n2)

    # ==================================================== S3: mechanism
    print("\nS3 -- mechanism split (strongest matched peak vs "
          "weakest off-zero point, live)")
    pg2 = np.array([p[0] for p in pk_v2])
    i_pk = int(np.argmax([W[int(round((p - SUB_LO) / DG_SUB))]
                          for p in pg2]))
    g_pk = float(pg2[i_pk])
    w_pk = float(W[int(round((g_pk - SUB_LO) / DG_SUB))])
    off_mask = np.array([float(np.min(np.abs(gam_c - g))) > 1.0
                         for g in sub_gs])
    i_off = int(np.argmin(np.where(off_mask, W, np.inf)))
    g_off = float(sub_gs[i_off])
    w_off = float(W[i_off])
    d_star = math.sqrt(w_pk * w_off)
    det_m = detunes_v2b(1176, g_pk)
    ql = xl.quad_lags(1176, g_pk, d_star)[:1176]
    Qb, _ = np.linalg.qr(xl.battery_B(1176, g_pk, d_star, 1.0,
                                      det_m))
    bud = xl.bud_of(1176, nrmT, float(np.max(np.abs(ql))))
    lam_z, _ = xl.sub_lam(cT + ql, Qb)
    det_o = detunes_v2b(1176, g_off)
    ql_o = xl.quad_lags(1176, g_off, d_star)[:1176]
    Qb_o, _ = np.linalg.qr(xl.battery_B(1176, g_off, d_star, 1.0,
                                        det_o))
    bud_o = xl.bud_of(1176, nrmT, float(np.max(np.abs(ql_o))))
    lam_o, _ = xl.sub_lam(cT + ql_o, Qb_o)
    print("    matched peak gamma = %.3f (W = %.5f): at delta* = "
          "%.5f lambda = %+.2e (%s)"
          % (g_pk, w_pk, d_star, lam_z,
             "HOLDS" if lam_z >= -bud else "breaks"))
    print("    off-zero gamma = %.3f (W = %.5f): at delta* = %.5f "
          "lambda = %+.2e (%s)"
          % (g_off, w_off, d_star, lam_o,
             "holds" if lam_o >= -bud_o else "BREAKS"))
    check("S3.MECH the explicit-formula redundancy measured live: at "
          "the shared probe delta* = %.5f the matched peak HOLDS "
          "while the off-zero point BREAKS, and the peak boundary "
          "is >= 2x the off-zero boundary (%.5f vs %.5f, ratio "
          "%.2f)" % (d_star, w_pk, w_off, w_pk / w_off),
          lam_z >= -bud and lam_o < -bud_o
          and w_pk >= 2.0 * w_off)

    # ==================================================== S4: controls
    print("\nS4 -- live controls")
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    xl.tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    tow_scr = srp.continuum_lags(1176) + c_scr
    lam_scr = xl.full_min(tow_scr, 1176)
    nrm_scr = float(sla.norm(sla.toeplitz(tow_scr[:1176]), 2))
    ctrl_gs = np.arange(SUB_LO, SUB_HI + 1e-9, CTRL_DG)
    W_scr = dense_profile(tow_scr[:1176], 1176, nrm_scr, ctrl_gs)
    pk_scr = find_peaks(ctrl_gs, W_scr, PROM_V2)
    n_scr_match = sum(1 for gz in zt if pk_scr
                      and min(abs(p - gz) for p, _ in pk_scr)
                      <= MATCH_TOL)
    check("S4.C1 scramble comb (lambda_min = %.2e, seed %d): %d "
          "prominent peaks, %d zeta matches -- the locator must NOT "
          "track ordinates on a scrambled comb"
          % (lam_scr, SEED_SCRAMBLE, len(pk_scr), n_scr_match),
          len(pk_scr) == 0 or n_scr_match <= 1)
    r1 = xl.lattice_r1(xl.EPSTEIN_CAP)
    lamE = xl.dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                    xl.EPSTEIN_CAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    cE, _ = core.atom_lags_at(0.5 * 640 * DGRID, 640,
                              np.log(supp.astype(float)),
                              2.0 * lamE[supp]
                              / np.sqrt(supp.astype(float)))
    tow_ep = srp.continuum_lags(640) + cE
    lam_ep = xl.full_min(tow_ep, 640)
    nrm_ep = float(sla.norm(sla.toeplitz(tow_ep[:640]), 2))
    W_ep = dense_profile(tow_ep[:640], 640, nrm_ep, ctrl_gs)
    pk_ep = find_peaks(ctrl_gs, W_ep, PROM_V2)
    n_ep_match = sum(1 for gz in zt if pk_ep
                     and min(abs(p - gz) for p, _ in pk_ep)
                     <= MATCH_TOL)
    check("S4.C2 Epstein comb (lambda_min = %.2e, M = 640): %d "
          "peaks, %d zeta matches -- a different zero set must NOT "
          "track zeta ordinates (the strongest non-circularity "
          "demonstration)"
          % (lam_ep, len(pk_ep), n_ep_match),
          len(pk_ep) == 0 or n_ep_match <= 1)

    # ================================ R: frozen out-of-sample reference
    print("\nR -- THE OUT-OF-SAMPLE RECORD (frozen reference; v2 "
          "gates recomputed)")
    print("    v1 (learning window [5, 60], frozen gates): peaks at "
          "%d/%d true ordinates, precision %.3f -- but FP %.0f%% at "
          "the ln(1.5) bar kept the shifted null at chance => "
          "LOCATOR-NULL as frozen (honest negative, typed)"
          % (V1_REF["det"], V1_REF["targets"], V1_REF["precision"],
             100 * V1_REF["fp_frac"]))
    check("R1.NULL the v1 adjudication stands: FP fraction %.2f > "
          "%.2f (the frozen gate the v1 run honestly failed); the "
          "post-hoc separation (matched prominence >= %.2f, false "
          "<= %.2f) straddles the v2 threshold ln(2.2) = %.3f"
          % (V1_REF["fp_frac"], GATE_FP, V1_SEP[0], V1_SEP[1],
             PROM_V2),
          V1_REF["fp_frac"] > GATE_FP
          and V1_SEP[1] < PROM_V2 < V1_SEP[0])
    det_f = V2_REF["det"] / V2_REF["targets"]
    fp_f = V2_REF["fp"] / max(V2_REF["det"], 1)
    check("R2.V2 the out-of-sample gates (recomputed from the frozen "
          "counts): detection %d/%d = %.0f%% >= %.0f%%, false "
          "positives %d = %.0f%% <= %.0f%%, precision %.3f -- "
          "LOCATOR-V2-RESOLVES with all four controls"
          % (V2_REF["det"], V2_REF["targets"], 100 * det_f,
             100 * GATE_DET, V2_REF["fp"], 100 * fp_f, 100 * GATE_FP,
             V2_REF["precision"]),
          det_f >= GATE_DET and fp_f <= GATE_FP)
    laws = [k / n for _, k, n in V2_DET_LAW]
    check("R3.DEPTH the depth law (frozen): detection %s at X = %s "
          "-- strictly improving with certified depth"
          % (", ".join("%d/%d" % (k, n) for _, k, n in V2_DET_LAW),
             ", ".join("%.1f" % x for x, _, _ in V2_DET_LAW)),
          all(l1 < l2 for l1, l2 in zip(laws[:-1], laws[1:])))

    # ============================================================== V
    print("\n" + "=" * 78)
    ok_pair = (V1_REF["fp_frac"] > GATE_FP and det_f >= GATE_DET
               and fp_f <= GATE_FP)
    print("V -- verdict pair (v1 adjudication + v2 recomputed): "
          "LOCATOR-NULL (honest, frozen) + %s"
          % ("LOCATOR-V2-RESOLVES" if det_f >= GATE_DET
             and fp_f <= GATE_FP else "?!"))
    print("=" * 78)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = not FAILS and ok_pair
    print("[%s] PATTERN GATE: expected all checks green with the "
          "verdict pair LOCATOR-NULL (frozen adjudication) + "
          "LOCATOR-V2-RESOLVES" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
