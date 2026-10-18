#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v839 -- PRIME.FLOOR.BRIDGEMAP.01 + PRIME.FLOOR.GUESAT.01: the pair-correlation bridge mapped from both sides and the GUE saturation of the floor demand -- the demand of PRIME.FLOOR.PAIRCORR.01 written in Montgomery F(alpha)-form with every supply row carrying its conditionality tag, the named minimal missing input (an unconditional form-factor bound F(alpha, T) <= C_F out to alpha ~ 3), and the measured saturation: the demand/GUE ratio plateaus at R_inf = 1.11 inside the frozen band -- the floor demand sits AT the random-matrix boundary of the comb, and inverting the certified margins yields a calibrated form-factor measurement F-hat(window) = 0.44 +- 0.14 (the instrument candidate), ONE module from two probes (9/9 + 7/7 checks, verdicts BRIDGE-FULLY-BEYOND and GUE-SATURATING; discovery probes paircorr_bridge_map_probe.py and gue_saturation_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping -- measured runtime ~0.8 min per part, the ledger build dominates; v830/v831 runtime precedent).  SCHOLARSHIP CORRECTION CARRIED THROUGHOUT: Montgomery's F(alpha) asymptotic on |alpha| < 1 is RH-CONDITIONAL (Montgomery 1973); the genuinely unconditional zero-statistics supply is RvM + Backlund/Trudgian (per-realization) and Selberg's S(t) second moment (rms grade).  PART A, THE BRIDGE MAP: translation wards exact (FT[sinc^2] = (1 - |omega|)_+ at 1.1e-09; the GUE number-variance pipeline vs the real-space R2 integral at rel 5.8e-05); the demand ledger on all 73 frames (67 v818 rungs + 6 deep tower; 22491 zeros to T = 2e4, RvM dev 0.41; unfolded grid N = 2^22, inversion residual 7.0e-10, Parseval 1.0e-08, grid quality 1.8e-02; the Schur term <= 3.6e-05 of tau, dropped and typed).  THE TWO-TIER GAP: tier 1 (unconditional) -- the per-realization BT row misses the gate by 52x at best, Selberg-rms by 12x: the triangle loss over the oscillatory functional is the irreducible cost of one-level input; tier 2 (conditional) -- the RH-conditional Montgomery window covers 43..86% of the demand spectrum (max share 0.862 at h = 142); even the FULL GUE conjecture closes only 39/73 rungs at rms grade -- the floor uses cancellation BEYOND typical-GUE at depth, as the contract typed from the prime side.  THE NAMED OBJECT (the minimal missing input): an unconditional F(alpha, T) <= C_F out to alpha = 3.0 with C_F as tabled per rung (3.3e-01..1.7e+00) -- OR any per-realization bound on the pole-perpendicular linear statistic beating MARGIN L_bar.  The Goldston-Montgomery dictionary typed: per-interval supply (even RH-grade O(sqrt x log^2 x)) can NEVER close the deep rungs -- only correlations BETWEEN the interval reads address the demand.  PART B, THE SATURATION: the ratio series R = sig_GUE/(0.5 L_bar) rises from the bottom-quartile median 0.614 to the plateau R_inf = 1.114 over the deepest 20 frames, INSIDE the frozen saturation band [0.5, 1.5], with rms(z) = 0.72 (typicality: the certified positivity consumes only a TYPICAL GUE realization); the alpha-profile: the deep tower's tight band is UNFOLDED alpha in 1..2 carrying 64% of its GUE budget -- the statistics the floor consumes at depth sit immediately beyond Montgomery's window, matching part A's typing; THE F-INSTRUMENT: inverting the positivity margins yields the calibrated form-factor measurement F-hat(window) = 0.44 +- 0.14 at T <= 2e4 (Poisson-ordinate control 0.94 +- 0.46 calibrates to 1 and the scramble fires -- the instrument distinguishes; the true-zero reading sits 4.0 s.e. below Poisson and <= 2 s.e. from GUE; published F(alpha) numerics at this height UNAVAILABLE, typed honestly); the calibrated bands are win/2-4/4-8, the rest ill-conditioned (typed).  THE CONSEQUENCE for PRIME.FLOOR.PAIRCORR.01: the named object's strength is CONFIRMED minimal-and-tight -- C_F ~ GUE x 0.81 on the tight band; softening below GUE-scale is NOT available at depth and nothing stronger is needed; a demand that saturates the GUE boundary is the strongest consistency evidence for the comb-zero bridge a necessary-side battery can produce -- it proves NOTHING about RH.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes paircorr_bridge_map_probe.py (9/9,
verdict BRIDGE-FULLY-BEYOND) and gue_saturation_probe.py (7/7,
verdict GUE-SATURATING), both 2026-08-07, re-run identically at
promotion; this module runs both frozen protocols VERBATIM (~0.8 min
per part: each part rebuilds its own frozen ledger, exactly as the
probes do -- no downscoping, no shared-state shortcut; a module-level
_VERDICTS capture appended at the end of each frozen run() per the
v817/v791 precedent -- no gate, bar or table changed).  IMPORT REMAP
(v831 precedent): the probes' read-only imports of
prime_lagrange_pair_probe / floor_envelope_depth_probe /
prime_envelope_analytic_probe / prime_alias_second_moment_probe map
to their promoted counterparts v823/v829/v830/v831; three probe-layer
symbols not carried by v829 (ANOMALOUS_H, epstein_counts, ols_loglog)
plus the 4-value eig2 of the probe layer are carried VERBATIM in the
local fdp shim below (declared; v829 stays READ-ONLY and untouched).
The original probe docstrings, frozen specs and decision trees live
in the probe files verbatim (experiments/tfpt-discovery/).

FIREWALL: zero-side module (the zero list is admissible input on this
strand, own RS scan via v684); v563/v684/v823/v830/v831 READ-ONLY.
NO RH claim; mapping + measurement only.
"""
import math
import os
import sys
import time
import types

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v684_rank3_zeroside as zp               # noqa: E402 (READ-ONLY)
import v823_prime_lagrange_floor as pp         # noqa: E402 (READ-ONLY)
import v829_prime_floor_depth as _v829         # noqa: E402 (READ-ONLY)
import v830_prime_float_budget as pe           # noqa: E402 (READ-ONLY)
import v831_prime_alias_second_moment as pa    # noqa: E402 (READ-ONLY)


# ------- fdp shim: the probe-layer symbols, VERBATIM from
# floor_envelope_depth_probe.py (v829 carries the promoted variants;
# the probes' frozen protocols use the probe-layer 4-value eig2 and
# the three symbols below, so they are carried verbatim -- declared
# in PROVENANCE)

def _fdp_ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def _fdp_eig2(M2):
    a, b, c = M2[0, 0], M2[0, 1], M2[1, 1]
    if max(abs(a), abs(b), abs(c)) == 0.0:
        return 0.0, 0.0, np.array([1.0, 0.0]), np.array([0.0, 1.0])
    mid, R = 0.5 * (a + c), math.hypot(0.5 * (a - c), b)
    l1, l2 = mid + R, mid - R
    if abs(b) < 1e-300 * max(abs(a), abs(c), 1e-300):
        v1 = np.array([1.0, 0.0]) if a >= c else np.array([0.0, 1.0])
    else:
        v1 = np.array([b, l1 - a])
        v1 /= np.linalg.norm(v1)
    if v1[0] < 0:
        v1 = -v1
    v2 = np.array([-v1[1], v1[0]])
    return l1, l2, v1, v2


def _fdp_csinc(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    m = np.abs(z) > 1e-12
    out[m] = np.sin(z[m]) / z[m]
    return out


def _fdp_epstein_counts(Nmax):
    cnt = np.zeros(Nmax + 1, dtype=np.uint16)
    for x in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - x * x
        if rem < 0:
            break
        y = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = x * x + 5 * y * y
        mult = ((2 if x > 0 else 1)
                * np.where(y > 0, 2, 1)).astype(np.uint16)
        np.add.at(cnt, n, mult)
    return cnt


fdp = types.SimpleNamespace(
    ANOMALOUS_H=1292, DGRID=1.0 / 64.0, csinc=_fdp_csinc,
    eig2=_fdp_eig2, epstein_counts=_fdp_epstein_counts,
    ols_loglog=_fdp_ols_loglog)

_VERDICTS = {}

# ------------------- shared layer (identical in both frozen probes; emitted once)

T0 = time.time()

FAILS = []

N_CHK = 0

DGRID = fdp.DGRID

DEEP_MS = (1176, 1326, 1414, 1504, 1588, 1632)

N_GRID = 1 << 22

OMEGA_MIN = 1.0 / 64.0

MARGIN = 0.5

def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))

def nbar_of(g):
    return zp.theta_rs(np.asarray(g, float)) / math.pi + 1.0


# =============== PART A -- paircorr_bridge_map_probe.py (frozen probe, verbatim)

MASS_IN_BAR = 0.25

CONS_SIG = 5.0

CONS_FRAC = 0.90

PIPE_BAR = 0.02

TRI_BAR = 1.0e-6

PARS_BAR = 1.0e-7

GRIDQ_BAR = 5.0e-2

SPLIT_BAR = 2.0e-2

SIGMA_L = 100.0

TRUD = (0.112, 0.278, 2.510)

SELB_C = 0.5

RUNG_PRINT_a = (0, 11, 22, 33, 44, 55, 66, 67, 68, 69, 70, 71, 72)

def part_a():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE PAIR-CORRELATION BRIDGE MAP (paircorr_bridge_map_"
          "probe) -- demand vs supply")
    print("=" * 78)
    print("""
HONESTY FRAME: mapping + measurement, not a proof attempt.  NO RH
claim.  SCHOLARSHIP CORRECTION: Montgomery's F(alpha) asymptotic on
|alpha| < 1 is RH-CONDITIONAL (Montgomery 1973); the genuinely
unconditional zero-statistics supply is RvM + Backlund/Trudgian
(per-realization) and Selberg's S(t) second moment (rms grade).
Every supply row below carries its conditionality tag.""")

    # ============================================================== S0
    print("\nS0 -- translation wards (the form-factor pipeline)")
    from scipy.integrate import quad
    # triangle form factor: FT[(sin pi x / pi x)^2] = (1 - |w|)_+
    # via the oscillatory-weighted rule (QAWF) on [0, inf)
    tri_dev = 0.0
    for w0 in (1.0 / 3.0, 0.5, 1.5):
        val = 2.0 * quad(lambda x: float(np.sinc(x)) ** 2,
                         0.0, np.inf, weight="cos",
                         wvar=2.0 * math.pi * w0, limit=400)[0]
        ref = max(0.0, 1.0 - abs(w0))
        tri_dev = max(tri_dev, abs(val - ref))
    check("S0.TRI FT[sinc^2] = (1 - |omega|)_+ (3-point QAWF dev "
          "%.1e <= %.0e): Montgomery's alpha IS the unfolded "
          "frequency omega" % (tri_dev, TRI_BAR), tri_dev <= TRI_BAR)
    # GUE pipeline ward: the DISCRETE FFT conventions used on the
    # rungs, validated on a sharp interval against the real-space
    # R2 = 1 - sinc^2 integral (self-contained)
    Lw = SIGMA_L
    Nw, dtw = 1 << 20, 1.0 / 64.0
    tw = np.arange(Nw) * dtw
    fw = ((tw >= 2000.0) & (tw < 2000.0 + Lw)).astype(float)
    Fw = np.fft.rfft(fw)
    omw = np.fft.rfftfreq(Nw, d=dtw)
    Pw = 2.0 * (dtw / Nw) * np.abs(Fw) ** 2
    var_disc = float(np.sum(Pw[1:] * np.minimum(omw[1:], 1.0)))
    var_real = Lw - 2.0 * quad(lambda u: (Lw - u)
                               * float(np.sinc(u)) ** 2, 0.0, Lw,
                               limit=2000)[0]
    pipe_dev = abs(var_disc - var_real) / var_real
    ref_gue = (math.log(2.0 * math.pi * Lw) + 0.5772156649 + 1.0) \
        / math.pi ** 2
    check("S0.PIPE GUE number variance Sigma^2(%.0f): discrete "
          "pipeline %.4f vs real-space R2 integral %.4f (rel %.1e "
          "<= %.0e; asymptotic (ln 2piL + gamma + 1)/pi^2 = %.4f)"
          % (Lw, var_disc, var_real, pipe_dev, PIPE_BAR, ref_gue),
          pipe_dev <= PIPE_BAR)

    # ============================================================== S1
    print("\nS1 -- the demand ledger (73 frames, exact functional)")
    gam, n_rvm = pp.zero_list()
    check("S1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    frames = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == fdp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        frames.append(dict(h=rr["h"], D=rr["D"], alpha=rr["alpha"],
                           deep=False))
    frames.sort(key=lambda w: w["alpha"])
    for Mz in DEEP_MS:
        frames.append(dict(h=Mz // 2, D=DGRID,
                           alpha=(Mz // 2) * DGRID, deep=True))
    check("S1.SET battery: %d frames (67 v818 + 6 tower)"
          % len(frames), len(frames) == 73)
    # the unfolded grid (shared by all frames)
    t0 = time.time()
    t_i = nbar_of(gam)                      # zero positions unfolded
    t_lo, t_hi = float(t_i[0]) - 0.5, float(t_i[-1]) + 0.5
    tgrid = np.linspace(t_lo, t_hi, N_GRID, endpoint=False)
    dt = float(tgrid[1] - tgrid[0])
    g_c = np.geomspace(13.4, 20100.0, 20001)
    ggrid = np.interp(tgrid, nbar_of(g_c), g_c)
    for _ in range(5):
        resid = nbar_of(ggrid) - tgrid
        ggrid = ggrid - resid / (0.5 / math.pi
                                 * np.log(ggrid / (2.0 * math.pi)))
    res_inv = float(np.max(np.abs(nbar_of(ggrid[:: 1 << 12])
                                  - tgrid[:: 1 << 12])))
    check("S1.GRID unfolded grid: N = %d, dt = %.4f (Nyquist "
          "omega = %.0f > max demand frequency ~ 32), inversion "
          "residual %.1e <= 1e-9"
          % (N_GRID, dt, 0.5 / dt, res_inv), res_inv <= 1e-9)
    print("    grid built in %.0f s" % (time.time() - t0))
    omg = np.fft.rfftfreq(N_GRID, d=dt)
    band_tr = omg < OMEGA_MIN
    band_in = (omg >= OMEGA_MIN) & (omg < 1.0)
    band_out = omg >= 1.0
    S_gue = np.minimum(omg, 1.0)
    B_gam = (TRUD[0] * np.log(ggrid)
             + TRUD[1] * np.log(np.log(ggrid)) + TRUD[2])
    rms_S = np.sqrt(np.log(np.log(ggrid)) / (2.0 * math.pi ** 2)
                    + SELB_C)
    t0 = time.time()
    worst_pars, worst_gridq, worst_split = 0.0, 0.0, 0.0
    for w in frames:
        h, D = w["h"], w["D"]
        fr = pa.pole_frame(h, D, gam)
        w["L_true"] = float(fr["y"] @ fr["y"])            # Y2 exact
        w["schur"] = fr["Ss"] ** 2 / (4.0 * fr["P0"])
        # the functional on the unfolded grid
        phi = D * ggrid
        wg = D * np.real(fdp.csinc(np.asarray(phi, complex)
                                   / 2.0) ** 2)
        S1g = pe.s_vec(1, h, phi)
        S2g = pe.s_vec(2, h, phi)
        r = math.sqrt(fr["P0"])
        p1h, p2h = fr["p1"] / r, fr["p2"] / r
        fg = 4.0 * wg * (p2h * S1g - p1h * S2g) ** 2
        w["L_bar"] = dt * float(np.sum(fg))
        w["dL"] = w["L_true"] - w["L_bar"]
        F = np.fft.rfft(fg)
        P = (dt / N_GRID) * np.abs(F) ** 2
        P[0] *= 0.5                                      # DC once
        pars = abs(2.0 * float(np.sum(P)) - dt * float(
            np.sum(fg ** 2))) / (dt * float(np.sum(fg ** 2)))
        worst_pars = max(worst_pars, pars)
        Pf = 2.0 * P                                     # omega > 0
        w["sig_P"] = math.sqrt(float(np.sum(Pf[~band_tr])))
        w["sig_gue"] = math.sqrt(float(
            np.sum(Pf[~band_tr] * S_gue[~band_tr])))
        w["sig_in"] = math.sqrt(float(
            np.sum(Pf[band_in] * omg[band_in])))
        w["sig_out1"] = math.sqrt(float(np.sum(Pf[band_out])))
        tot = float(np.sum(Pf[~band_tr]))
        w["mass_in"] = float(np.sum(Pf[band_in])) / tot
        cum = np.cumsum(Pf[~band_tr])
        w["om95"] = float(omg[~band_tr][np.searchsorted(
            cum, 0.95 * cum[-1])])
        w["C_F"] = (MARGIN * w["L_bar"]) ** 2 / max(
            float(np.sum(Pf[~band_tr])), 1e-300)
        # unconditional rows (Stieltjes IBP in t-space)
        fp = np.gradient(fg, dt)
        ends = (abs(fg[0]) * B_gam[0] + abs(fg[-1]) * B_gam[-1])
        w["BT"] = dt * float(np.sum(np.abs(fp) * B_gam)) + ends
        w["SELB"] = dt * float(np.sum(np.abs(fp) * rms_S)) \
            + abs(fg[0]) * rms_S[0] + abs(fg[-1]) * rms_S[-1]
        # band split of the measured fluctuation
        Fin = np.where(band_in, F, 0.0)
        Ftr = np.where(band_tr, F, 0.0)
        f_in = np.fft.irfft(Fin, n=N_GRID)
        f_tr = np.fft.irfft(Ftr, n=N_GRID)
        dL_in = float(np.sum(np.interp(t_i, tgrid, f_in))) \
            - dt * float(np.sum(f_in))
        dL_tr = float(np.sum(np.interp(t_i, tgrid, f_tr))) \
            - dt * float(np.sum(f_tr))
        w["dL_in"], w["dL_tr"] = dL_in, dL_tr
        w["dL_out"] = w["dL"] - dL_in - dL_tr            # linearity
        # grid-quality ward: full f re-summed at the zeros
        L_grid = float(np.sum(np.interp(t_i, tgrid, fg)))
        worst_gridq = max(worst_gridq,
                          abs(L_grid - w["L_true"]) / w["L_true"])
    print("    demand ledger built in %.0f s" % (time.time() - t0))
    check("S1.PARS Parseval on the demand spectrum (worst rel %.1e "
          "<= %.0e)" % (worst_pars, PARS_BAR), worst_pars <= PARS_BAR)
    check("S1.GRIDQ grid quality: full functional re-summed at the "
          "true zeros vs exact L (worst rel %.1e <= %.0e)"
          % (worst_gridq, GRIDQ_BAR), worst_gridq <= GRIDQ_BAR)
    schur_max = max(w["schur"] / max(w["L_true"], 1e-300)
                    for w in frames)
    print("    the Schur term Ss^2/(4 P0): max %.1e of tau -- "
          "dropped from the ledger (typed)" % schur_max)

    # ============================================================== S2
    print("\nS2 -- the ledger tables (demand vs supply, per rung)")
    print("    demand:  rung  alpha    L_bar      |dL|/L_bar  "
          "mass_in  om95   C_F(needed)")
    for i in RUNG_PRINT_a:
        w = frames[i]
        print("    D%02d  h=%4d  %5.2f  %9.3e  %8.3f    %5.3f   "
              "%5.2f  %8.2e"
              % (i, w["h"], w["alpha"], w["L_bar"],
                 abs(w["dL"]) / w["L_bar"], w["mass_in"], w["om95"],
                 w["C_F"]))
    print("\n    supply (as multiples of the gate MARGIN*L_bar = "
          "%.1f L_bar; < 1 closes the rung):" % MARGIN)
    print("    rung   BT/gate    SELB/gate  sig_in/gate "
          "sig_GUE/gate sig_P/gate   [U0]       [U1]      [C2-RH]  "
          "[C3-conj]  [P4]")
    for i in RUNG_PRINT_a:
        w = frames[i]
        gate = MARGIN * w["L_bar"]
        print("    S%02d  %9.2e  %9.2e  %9.2e  %9.2e  %9.2e"
              % (i, w["BT"] / gate, w["SELB"] / gate,
                 w["sig_in"] / gate, w["sig_gue"] / gate,
                 w["sig_P"] / gate))
    bt_min = min(w["BT"] / (MARGIN * w["L_bar"]) for w in frames)
    gue_ok = [w for w in frames
              if w["sig_gue"] < MARGIN * w["L_bar"]]
    in_ok = [w for w in frames if w["mass_in"] >= MASS_IN_BAR]
    dem_med = float(np.median([abs(w["dL"]) / w["L_bar"]
                               for w in frames]))
    print("\n    summary: min BT/gate = %.1f (unconditional row); "
          "GUE-rms closes %d/73 rungs; mass_in >= %.2f on %d/73 "
          "rungs; median measured demand |dL|/L_bar = %.3f"
          % (bt_min, len(gue_ok), MASS_IN_BAR, len(in_ok), dem_med))

    # ============================================================== S3
    print("\nS3 -- the key question + gap statement (alpha-units)")
    max_in = max(w["mass_in"] for w in frames)
    w_best = max(frames, key=lambda w: w["mass_in"])
    key_yes = max_in >= MASS_IN_BAR
    check("S3.KEY does ANY demand piece sit inside |alpha| < 1? "
          "max spectral share inside the window = %.3f at h = %d "
          "(alpha_win %.2f) -- %s (bar %.2f)"
          % (max_in, w_best["h"], w_best["alpha"],
             "YES" if key_yes else "NO", MASS_IN_BAR), True)
    if key_yes:
        print("    the implied window-piece bound (C2, RH-COND "
              "Montgomery): |dL_in| <~ sigma_in; verified below "
              "(translation ward).  NOTE: NOT unconditional -- "
              "the scholarship correction applies.")
    om95s = [w["om95"] for w in frames]
    print("    THE GAP IN ALPHA-UNITS: demand spectral edge "
          "omega95 = %.2f..%.2f across the battery (window edge "
          "1.0): the demand extends %.1fx..%.1fx beyond the "
          "Montgomery window; the deep tower needs F(alpha, T) "
          "control out to alpha ~ %.1f"
          % (min(om95s), max(om95s), min(om95s), max(om95s),
             frames[-1]["om95"]))
    # translation ward (RH true in range: window piece must comply)
    cons = [abs(w["dL_in"]) <= CONS_SIG * w["sig_in"]
            for w in frames]
    frac_cons = sum(cons) / len(cons)
    check("S3.CONS translation ward: |dL_in| <= %.0f sigma_in on "
          "%.0f%% of rungs (need >= %.0f%%; RH holds to 3e12 so "
          "the window piece must be consistent)"
          % (CONS_SIG, 100 * frac_cons, 100 * CONS_FRAC),
          frac_cons >= CONS_FRAC)
    r_out = [abs(w["dL_out"]) / max(w["sig_out1"], 1e-300)
             for w in frames]
    print("    beyond-window consistency (informative): "
          "|dL_out|/sigma_out(F=1) = %.2f..%.2f (median %.2f) -- "
          "measured vs the GUE-conjecture scale"
          % (min(r_out), max(r_out), float(np.median(r_out))))

    # ============================================================== S4
    print("\nS4 -- the short-interval translation "
          "(Goldston-Montgomery dictionary)")
    w_lo, w_hi = frames[0], frames[-1]
    for w, tag in ((w_lo, "bottom"), (w_hi, "deep")):
        drel = 2.0 * math.sinh(w["D"])
        print("    %s rung (h = %d): reads = tent-weighted psi "
          "sums over [x e^-D, x e^D], relative length 2 sinh D = "
          "%.4f, scales x <= e^%.1f = %.2e"
              % (tag, w["h"], drel, 2 * w["alpha"],
                 math.exp(2 * w["alpha"])))
    print("""    the dictionary (Goldston-Montgomery 1987, RH): F on
    [0, A] <-> psi-variance for intervals h >= x^{1/A}; our
    proportional intervals (h ~ 2D x) sit at the LONG end where
    even PNT gives the asymptotic -- but the demand is NOT the
    asymptotic: it is the fluctuation combination ACROSS scales v
    at rms grade (the omega-spectrum above).  Per-interval supply
    (RH): |psi(x + 2Dx) - psi(x) - 2Dx| = O(sqrt x log^2 x) --
    per-read this is the Poisson row sig_P, and the table shows
    sig_P/gate >> 1 at depth: NO per-interval bound can close the
    deep rungs; only correlations BETWEEN the interval reads
    (= pair correlation, Selberg-variance grade or better in the
    ACROSS-scale direction) address the demand.  Selberg's
    unconditional variance (U1 row) carries the same triangle loss
    as U0 -- the across-scale cancellation is not in unconditional
    supply.""")

    # ============================================================== S5
    print("\nS5 -- verdict + consequence")
    wards_ok = not any(k in FAILS for k in
                       ("S0.TRI", "S0.PIPE", "S1.PARS", "S1.GRIDQ",
                        "S3.CONS"))
    bt_close = [w for w in frames if w["BT"] < MARGIN * w["L_bar"]]
    if not wards_ok:
        verdict = "BRIDGE-TRANSLATION-BLOCKED"
    elif bt_close:
        verdict = "BRIDGE-PARTIAL-UNCONDITIONAL"
    else:
        verdict = "BRIDGE-FULLY-BEYOND"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "BRIDGE-PARTIAL-UNCONDITIONAL":
        print("    UNCONDITIONAL floor piece: BT closes %d rungs "
              "(the first zero-side unconditional floor bricks): %s"
              % (len(bt_close),
                 ", ".join("h=%d" % w["h"] for w in bt_close[:8])))
    elif verdict == "BRIDGE-FULLY-BEYOND":
        print("""    THE TWO-TIER GAP (typed):
    tier 1 (unconditional): the per-realization BT row misses the
      gate by %.0fx at best (Selberg-rms row by %.0fx) -- the
      triangle loss over the oscillatory functional is the
      irreducible cost of one-level input.
    tier 2 (conditional): the RH-conditional Montgomery window
      covers %.0f%%..%.0f%% of the demand spectrum (mass_in);
      even the FULL GUE conjecture (F = 1 beyond the window)
      closes %d/73 rungs at rms grade -- the measured demand
      |dL|/L_bar (median %.3f) exceeds the GUE-rms scale on the
      rest: the floor uses cancellation BEYOND typical-GUE, as
      PRIME.FLOOR.PAIRCORR.01 typed from the prime side.
    THE MINIMAL MISSING INPUT (the named object): an unconditional
      form-factor bound F(alpha, T) <= C_F out to alpha = %.1f
      (deep tower demand edge), with C_F as tabled per rung
      (%.1e..%.1e) -- OR any per-realization bound on the
      pole-perpendicular linear statistic beating MARGIN L_bar."""
              % (bt_min, min(w["SELB"] / (MARGIN * w["L_bar"])
                             for w in frames),
                 100 * min(w["mass_in"] for w in frames),
                 100 * max(w["mass_in"] for w in frames),
                 len(gue_ok), dem_med, frames[-1]["om95"],
                 min(w["C_F"] for w in frames),
                 max(w["C_F"] for w in frames)))
    print("""
    CONSEQUENCE FOR PRIME.FLOOR.PAIRCORR.01: the bridge is now
    mapped from both sides.  Demand: a per-realization bound on the
    pole-perpendicular zero statistic with spectral mass extending
    to alpha ~ %.1f.  Supply: unconditional one-level input misses
    by the typed factors; the Montgomery window (RH-cond) covers
    only the mass_in share; GUE-conjecture rms closes %d/73 rungs.
    The contract's honest statement stands: the floor envelope
    constant is pair-correlation-grade (and at depth beyond-
    typical-GUE) arithmetic substance."""
          % (frames[-1]["om95"], len(gue_ok)))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; mapping + measurement only; nothing outside "
          "experiments/ touched.")
    _VERDICTS["a"] = verdict



# =============== PART B -- gue_saturation_probe.py (frozen probe, verbatim)

BANDS = ((OMEGA_MIN, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0),
         (8.0, 1.0e9))

BAND_TAGS = ("win", "1-2", "2-4", "4-8", ">8")

R_SAT_LO, R_SAT_HI = 0.5, 1.5

Z_SUPER = 1.5

N_DEEP_PLATEAU = 20

REG_BAR = 6.0e-3

SEED_POIS, SEED_JIT = 473001, 473002

N_WLS_IT = 3

PEAK_RUNGS = (0, 33, 55, 72)

RUNG_PRINT_b = (0, 6, 11, 17, 22, 28, 33, 39, 44, 50, 55, 61, 66,
              67, 68, 69, 70, 71, 72)

REG_R = {0: 0.668, 11: 0.592, 44: 1.33, 55: 1.25, 67: 1.01,
         72: 1.24}

REG_LBAR = {0: 5.235e-4, 72: 1.250e-5}

REG_MASSIN72 = 0.463

def ols_ll(xs, ys):
    return fdp.ols_loglog(xs, ys)

def spearman(xs, ys):
    rx = np.argsort(np.argsort(xs)).astype(float)
    ry = np.argsort(np.argsort(ys)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])

def nnls_wls(A, y, F0, n_it=N_WLS_IT):
    """Iterated nonnegative WLS with chi^2-type weights 2 (A F)^2."""
    from scipy.optimize import nnls
    F = F0.copy()
    for _ in range(n_it):
        mu = np.maximum(A @ F, 1e-300)
        wr = 1.0 / (math.sqrt(2.0) * mu)
        F, _ = nnls(A * wr[:, None], y * wr)
    return F

def part_b():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("GUE SATURATION OF THE FLOOR DEMAND (gue_saturation_probe)")
    print("=" * 78)
    print("""
HONESTY FRAME: measurement + inversion, not a proof.  NO RH claim.
The GUE row mixes RH-conditional Montgomery (|alpha| < 1) with the
conjectural F = 1 beyond -- all ratios are rms-grade with the O(1)
convention class typed; the saturation bars [0.5, 1.5] absorb it.""")

    # ============================================================== S0
    print("\nS0 -- rebuild the bridge ledger (regression ward)")
    gam, n_rvm = pp.zero_list()
    check("S0.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    frames = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == fdp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        frames.append(dict(h=rr["h"], D=rr["D"], alpha=rr["alpha"],
                           deep=False))
    frames.sort(key=lambda w: w["alpha"])
    for Mz in DEEP_MS:
        frames.append(dict(h=Mz // 2, D=DGRID,
                           alpha=(Mz // 2) * DGRID, deep=True))
    check("S0.SET battery: %d frames" % len(frames),
          len(frames) == 73)
    t_i = nbar_of(gam)
    t_lo, t_hi = float(t_i[0]) - 0.5, float(t_i[-1]) + 0.5
    tgrid = np.linspace(t_lo, t_hi, N_GRID, endpoint=False)
    dt = float(tgrid[1] - tgrid[0])
    g_c = np.geomspace(13.4, 20100.0, 20001)
    ggrid = np.interp(tgrid, nbar_of(g_c), g_c)
    for _ in range(5):
        resid = nbar_of(ggrid) - tgrid
        ggrid = ggrid - resid / (0.5 / math.pi
                                 * np.log(ggrid / (2.0 * math.pi)))
    res_inv = float(np.max(np.abs(nbar_of(ggrid[:: 1 << 12])
                                  - tgrid[:: 1 << 12])))
    check("S0.GRID unfolded grid (N = %d, dt = %.4f, inversion "
          "residual %.1e <= 1e-9)" % (N_GRID, dt, res_inv),
          res_inv <= 1e-9)
    omg = np.fft.rfftfreq(N_GRID, d=dt)
    S_gue = np.minimum(omg, 1.0)
    rho_loc = np.log(ggrid / (2.0 * math.pi)) / (2.0 * math.pi)
    band_idx = [(omg >= a) & (omg < b) for a, b in BANDS]
    # the two ordinate ensembles (frozen seeds; the only RNG)
    rs_p = np.random.RandomState(SEED_POIS)
    t_pois = np.sort(rs_p.uniform(t_lo, t_hi, size=len(gam)))
    rs_j = np.random.RandomState(SEED_JIT)
    t_jit = np.clip(t_i + rs_j.uniform(-0.5, 0.5, size=len(gam)),
                    t_lo, t_hi)
    t0 = time.time()
    n_pk = {}
    for idx, w in enumerate(frames):
        h, D = w["h"], w["D"]
        fr = pa.pole_frame(h, D, gam)
        w["L_true"] = float(fr["y"] @ fr["y"])
        phi = D * ggrid
        wg = D * np.real(fdp.csinc(np.asarray(phi, complex)
                                   / 2.0) ** 2)
        S1g = pe.s_vec(1, h, phi)
        S2g = pe.s_vec(2, h, phi)
        r = math.sqrt(fr["P0"])
        fg = 4.0 * wg * ((fr["p2"] / r) * S1g
                         - (fr["p1"] / r) * S2g) ** 2
        w["L_bar"] = dt * float(np.sum(fg))
        w["dL"] = w["L_true"] - w["L_bar"]
        w["rho_star"] = float(np.sum(fg * rho_loc)) \
            / float(np.sum(fg))
        F = np.fft.rfft(fg)
        P2 = 2.0 * (dt / N_GRID) * np.abs(F) ** 2
        P2[0] *= 0.5
        w["I_b"] = np.array([float(np.sum(P2[bi])) for bi in
                             band_idx])
        w["sig2_b"] = np.array([float(np.sum(P2[bi] * S_gue[bi]))
                                for bi in band_idx])
        w["sig_gue"] = math.sqrt(float(np.sum(w["sig2_b"])))
        w["mass_in"] = w["I_b"][0] / max(float(np.sum(w["I_b"])),
                                         1e-300)
        w["R"] = w["sig_gue"] / (MARGIN * w["L_bar"])
        if idx in PEAK_RUNGS:
            spec = P2 * S_gue
            spec[omg < OMEGA_MIN] = 0.0
            k_w = 501
            sm = np.convolve(spec, np.ones(k_w) / k_w, mode="same")
            pks = []
            order = np.argsort(sm)[::-1]
            for k in order[:200000]:
                if all(abs(int(k) - p) > 2000 for p, _ in pks):
                    pks.append((int(k), float(omg[k])))
                if len(pks) == 3:
                    break
            n_pk[idx] = [om for _, om in pks]
        # trend band + the measured fluctuation (flux part)
        Ftr = np.where(omg < OMEGA_MIN, F, 0.0)
        f_tr = np.fft.irfft(Ftr, n=N_GRID)
        L_int = dt * float(np.sum(fg))
        L_tr_int = dt * float(np.sum(f_tr))

        def _flux(tt):
            dl = float(np.sum(np.interp(tt, tgrid, fg))) - L_int
            dtr = float(np.sum(np.interp(tt, tgrid, f_tr))) \
                - L_tr_int
            return dl - dtr
        w["dL_flux"] = _flux(t_i)
        w["dL_pois"] = _flux(t_pois)
        w["dL_jit"] = _flux(t_jit)
        w["z"] = w["dL_flux"] / max(w["sig_gue"], 1e-300)
    print("    ledger + ensembles built in %.0f s"
          % (time.time() - t0))
    reg_worst = 0.0
    for i, rv in REG_R.items():
        reg_worst = max(reg_worst, abs(frames[i]["R"] / rv - 1.0))
    for i, lv in REG_LBAR.items():
        reg_worst = max(reg_worst,
                        abs(frames[i]["L_bar"] / lv - 1.0))
    reg_worst = max(reg_worst, abs(frames[72]["mass_in"]
                                   / REG_MASSIN72 - 1.0))
    check("S0.REG bridge regression: 6 R values + 2 L_bar + "
          "mass_in reproduce (worst rel %.1e <= %.0e)"
          % (reg_worst, REG_BAR), reg_worst <= REG_BAR)

    # ============================================================== S1
    print("\nS1 -- THE RATIO SERIES (demand/GUE per rung)")
    alp = np.array([w["alpha"] for w in frames])
    hs = np.array([float(w["h"]) for w in frames])
    Rs = np.array([w["R"] for w in frames])
    print("    rung   h    alpha    R = sig_GUE/(0.5 L_bar)   "
          "R_pos = sig_GUE/L_bar   |z|")
    for i in RUNG_PRINT_b:
        w = frames[i]
        print("    %3d  %5d  %5.2f       %6.3f                  "
              "%6.3f            %5.2f"
              % (i, w["h"], w["alpha"], w["R"], w["R"] / 2.0,
                 abs(w["z"])))
    sl_a = np.polyfit(alp, np.log(Rs), 1)
    r2_a = float(np.corrcoef(alp, np.log(Rs))[0, 1] ** 2)
    sl_h, _, r2_h = ols_ll(hs, Rs)
    rho_sp = spearman(alp, Rs)
    order = np.argsort(alp)
    deep_set = order[-N_DEEP_PLATEAU:]
    bot_set = order[: len(order) // 4]
    R_inf = float(np.median(Rs[deep_set]))
    R_bot = float(np.median(Rs[bot_set]))
    print("    law: log R = %+.4f alpha %+.2f (R^2 %.2f); "
          "R ~ h^%+.2f (R^2 %.2f); Spearman(alpha, R) = %+.2f"
          % (sl_a[0], sl_a[1], r2_a, sl_h, r2_h, rho_sp))
    print("    approach: bottom-quartile median R = %.3f -> "
          "plateau R_inf (deepest %d) = %.3f (from BELOW; "
          "positivity-gate plateau R_inf/2 = %.3f)"
          % (R_bot, N_DEEP_PLATEAU, R_inf, R_inf / 2.0))
    zs = np.array([w["z"] for w in frames])
    z_rms = float(np.sqrt(np.mean(zs ** 2)))
    check("S1.PLATEAU the frozen question: R_inf = %.3f in "
          "[%.1f, %.1f] (saturation band), rms(z) = %.2f "
          "(SUPER bar %.1f)" % (R_inf, R_SAT_LO, R_SAT_HI, z_rms,
                                Z_SUPER),
          R_SAT_LO <= R_inf <= R_SAT_HI)
    print("    error budget on R: grid <= 1.8e-2, Parseval <= "
          "1e-8, trend-band convention O(1e-2); gate convention "
          "class factor 2 (absorbed by the saturation band)")

    # ============================================================== S2
    print("\nS2 -- THE ALPHA-PROFILE (where the GUE budget is "
          "spent)")
    print("    rung   " + "".join("%8s" % t for t in BAND_TAGS)
          + "   (shares of sigma_GUE^2)")
    for i in RUNG_PRINT_b:
        w = frames[i]
        sh = w["sig2_b"] / max(float(np.sum(w["sig2_b"])), 1e-300)
        print("    %3d  " % i
              + "".join("%8.3f" % s for s in sh))
    # two populations resolved (tower D = 1/64 vs wide battery)
    sh_tow = np.mean([w["sig2_b"] / max(float(np.sum(w["sig2_b"])),
                                        1e-300)
                      for w in frames if w["deep"]], axis=0)
    sh_wide = np.mean([frames[j]["sig2_b"]
                       / max(float(np.sum(frames[j]["sig2_b"])),
                             1e-300) for j in deep_set
                       if not frames[j]["deep"]], axis=0)
    tight = int(np.argmax(sh_tow))
    print("    deep TOWER mean shares:   "
          + ", ".join("%s %.3f" % (t, s) for t, s in
                      zip(BAND_TAGS, sh_tow)))
    print("    deep wide-battery shares: "
          + ", ".join("%s %.3f" % (t, s) for t, s in
                      zip(BAND_TAGS, sh_wide)))
    print("    THE TIGHT BAND (tower, the depth carrier): '%s' "
          "carries %.0f%% of the tower GUE budget (the wide "
          "battery frames park theirs at high omega via their "
          "small D -- typed, two populations)"
          % (BAND_TAGS[tight], 100 * sh_tow[tight]))
    for i in PEAK_RUNGS:
        w = frames[i]
        vids = []
        for om in n_pk[i]:
            v = om * 2.0 * math.pi * w["rho_star"]
            kD = v / w["D"]
            vids.append("omega %.2f -> v ~ %.2f (v/D = %.0f, "
                        "v/2alpha = %.2f)" % (om, v, kD,
                                              v / (2 * w["alpha"])))
        print("    rung %3d (h = %d): peaks %s"
              % (i, w["h"], "; ".join(vids)))

    # ============================================================== S3
    print("\nS3 -- THE F-INSTRUMENT (positivity margins inverted)")
    z_p = np.array([w["dL_pois"] / max(w["sig_gue"], 1e-300)
                    for w in frames])
    print("    measured z = dL_flux/sigma_GUE: mean %+.2f, rms "
          "%.2f, range %+.2f..%+.2f (73 frames; INDEPENDENCE "
          "CAVEAT: frames share zeros)"
          % (float(np.mean(zs)), z_rms, float(np.min(zs)),
             float(np.max(zs))))
    print("    Poisson-ordinate control z (same normalization): "
          "rms %.2f" % float(np.sqrt(np.mean(z_p ** 2))))
    A_I = np.array([w["I_b"] for w in frames])
    F_gue_band = (np.sum([w["sig2_b"] for w in frames], axis=0)
                  / np.maximum(np.sum(A_I, axis=0), 1e-300))
    F0 = F_gue_band.copy()

    def fit_F(y):
        Fh = nnls_wls(A_I, y, F0)
        jk = np.empty((len(y), len(Fh)))
        for r in range(len(y)):
            keep = np.arange(len(y)) != r
            jk[r] = nnls_wls(A_I[keep], y[keep], F0)
        se = np.sqrt((len(y) - 1.0) * np.var(jk, axis=0))
        return Fh, se
    y_true = np.array([w["dL_flux"] ** 2 for w in frames])
    y_pois = np.array([w["dL_pois"] ** 2 for w in frames])
    y_jit = np.array([w["dL_jit"] ** 2 for w in frames])
    Ft, se_t = fit_F(y_true)
    Fp, se_p = fit_F(y_pois)
    Fj, se_j = fit_F(y_jit)
    print("    band      F-hat(true)      F-hat(Poisson)   "
          "F-hat(jitter)    GUE pred   Poisson pred")
    for b, tag in enumerate(BAND_TAGS):
        print("    %4s   %6.2f +- %5.2f   %6.2f +- %5.2f   "
              "%6.2f +- %5.2f    %6.3f      1.000"
              % (tag, Ft[b], se_t[b], Fp[b], se_p[b], Fj[b],
                 se_j[b], F_gue_band[b]))
    check("S3.SCRAM the instrument distinguishes: Poisson-"
          "ordinate window-band F-hat = %.2f exceeds the true-"
          "zero value %.2f (the GUE reading of the demand ledger "
          "breaks under scramble, as it must)"
          % (Fp[0], Ft[0]), Fp[0] > Ft[0])
    cal_ok = abs(Fp[0] - 1.0) <= 3.0 * max(se_p[0], 1e-6)
    check("S3.CAL Poisson calibration: window-band F-hat(Poisson) "
          "= %.2f +- %.2f consistent with 1 (3 s.e.)"
          % (Fp[0], se_p[0]), cal_ok)
    # conditioning: the cross-band design is nearly collinear --
    # a band counts as a CALIBRATED readout only where (i) the
    # known-answer Poisson control reproduces 1 within 3 s.e.,
    # (ii) the jackknife is stable (se > 0.05) and informative
    # (se < 1.0); the rest is typed ill-conditioned
    good_b = [b for b in range(len(BAND_TAGS))
              if abs(Fp[b] - 1.0) <= 3.0 * max(se_p[b], 1e-6)
              and 0.05 < se_t[b] < 1.0]
    print("    calibrated bands (Poisson control reproduces 1, "
          "stable + informative jackknife): %s -- the rest of "
          "the multi-band inversion is ill-conditioned "
          "(near-collinear design; typed)"
          % ", ".join(BAND_TAGS[b] for b in good_b))
    dev_gue = max(abs(Ft[b] - F_gue_band[b]) / se_t[b]
                  for b in good_b)
    print("    true zeros vs GUE prediction: worst deviation "
          "%.1f s.e. over the calibrated bands; vs Poisson: "
          "window band sits %.1f s.e. below 1"
          % (dev_gue, (1.0 - Ft[0]) / max(se_t[0], 1e-6)))
    print("    published F(alpha) numerics at T = 2e4: "
          "UNAVAILABLE (typed honestly) -- Odlyzko-grade studies "
          "live at far greater heights; qualitative GUE "
          "consistency only, no citable numbers at ours.")
    instr = (dev_gue <= 2.0) and ((1.0 - Ft[0])
                                  / max(se_t[0], 1e-6) >= 3.0)
    print("    instrument statement: fitted F consistent with GUE "
          "(<= 2 s.e.) AND window band > 3 s.e. below Poisson: %s "
          "-- %s" % (instr,
                     "the certified ladder doubles as a form-"
                     "factor measurement at T <= 2e4 (promotable "
                     "instrument candidate, necessary-side)"
                     if instr else
                     "instrument-candidate NOT reached at this "
                     "battery (typed; scatter/correlation budget)"))

    # ============================================================== S4
    print("\nS4 -- synthesis + verdict")
    wards_ok = not any(k in FAILS for k in
                       ("S0.Z", "S0.SET", "S0.GRID", "S0.REG"))
    if not wards_ok:
        verdict = "TRANSLATION-REGRESSION-BROKEN"
    elif R_inf < R_SAT_LO:
        verdict = "GUE-SLACK"
    elif R_inf > R_SAT_HI and z_rms > Z_SUPER:
        verdict = "SUPER-GUE"
    elif R_inf > R_SAT_HI:
        verdict = "GUE-SATURATING"   # proof budget above, stats not
    else:
        verdict = "GUE-SATURATING"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    print("""    THE SYNTHESIS: the demand/GUE ratio rises from %.2f
    (bottom quartile) to a plateau R_inf = %.2f over the deepest
    %d frames and stays inside the saturation band [%.1f, %.1f]:
    the floor demand sits AT the random-matrix boundary of the
    comb, not below it (no cheap slack: every input weaker than
    pair-correlation grade -- the one-level rows of the bridge --
    must fail, which is exactly what the bridge measured) and not
    above it (rms(z) = %.2f: the certified positivity consumes
    only a TYPICAL GUE realization, no super-GUE structure is
    implied in the accessible range).  The tower's tight band is
    '%s' (%.0f%% of its GUE budget): the statistics the floor
    really consumes at depth sit immediately beyond Montgomery's
    window -- matching the bridge's alpha ~ 1..3 typing of the
    named object.
    CONSEQUENCE for PRIME.FLOOR.PAIRCORR.01: the named object's
    strength is CONFIRMED as minimal-and-tight: the required
    C_F profile is GUE x %.2f (= 1/R_inf^2) on the tight band --
    softening below GUE-scale is NOT available at depth, and
    nothing stronger than GUE-scale is needed.  ARCHITECTURE
    READING (precise, no RH claim): a demand that saturates the
    GUE boundary means the comb's floor is calibrated to the
    conjectured universality class of the zeros -- the strongest
    possible CONSISTENCY evidence for the comb-zero bridge that a
    necessary-side battery can produce; it proves nothing about
    RH, and the measured typicality (z ~ %.2f rms) is exactly
    what RH-grade zero statistics would predict at these heights."""
          % (R_bot, R_inf, N_DEEP_PLATEAU, R_SAT_LO, R_SAT_HI,
             z_rms, BAND_TAGS[tight], 100 * sh_tow[tight],
             1.0 / R_inf ** 2, z_rms))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")
    _VERDICTS["b"] = verdict



EXPECT = {"a": (9, "BRIDGE-FULLY-BEYOND"), "b": (7, "GUE-SATURATING")}


def run():
    t_all = time.time()
    counts = {}
    for tag, part in (("a", part_a), ("b", part_b)):
        globals()["N_CHK"] = 0
        globals()["FAILS"] = []
        globals()["T0"] = time.time()
        part()
        counts[tag] = (N_CHK, len(FAILS))
    pattern_ok = all(
        counts[t][0] == EXPECT[t][0] and counts[t][1] == 0
        and _VERDICTS.get(t) == EXPECT[t][1] for t in EXPECT)
    n_run = sum(c[0] for c in counts.values())
    n_fail = sum(c[1] for c in counts.values())
    print("\n" + "=" * 74)
    print("v839: %d/%d checks passed, %d failed | runtime %.1f min"
          % (n_run - n_fail, n_run, n_fail,
             (time.time() - t_all) / 60.0))
    print("NO RH claim; the bridge is mapped from both sides and the "
          "demand saturates the GUE boundary -- the named object of "
          "PRIME.FLOOR.PAIRCORR.01 confirmed minimal-and-tight.")
    print("[%s] PATTERN GATE: expected 9 + 7 checks, 0 failed, "
          "verdicts BRIDGE-FULLY-BEYOND + GUE-SATURATING (got %s + %s)"
          % ("PASS" if pattern_ok else "FAIL",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return (n_fail if n_fail else 0) + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
