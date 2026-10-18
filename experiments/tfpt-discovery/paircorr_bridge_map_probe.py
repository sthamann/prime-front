#!/usr/bin/env python3
"""paircorr_bridge_map_probe -- attack the floor <-> pair-correlation
bridge FROM THE OTHER SIDE: map what the zero-statistics literature
(Montgomery pair correlation and successors) supplies, unconditionally
and conditionally, against the floor's exact quantitative demand.

MAPPING + MEASUREMENT ONLY -- not a proof attempt.  EXPLORATION ONLY
(experiments/): no ledger row, no paper edit, nothing outside
experiments/.  NO RH claim.  Frozen before running.

SCHOLARSHIP CORRECTION (typed prominently, honesty first): the task
premise says Montgomery's F(alpha, T) is known UNCONDITIONALLY for
|alpha| < 1.  That is a common misstatement: Montgomery's theorem
(1973) F(alpha) = T^{-2 alpha} log T + alpha + o(1) on |alpha| <= 1
is proved UNDER RH.  Genuinely unconditional supply is weaker:
one-level RvM density with the Backlund/Trudgian-grade bound
|S(t)| <= a log t + b log log t + c (per-realization), Selberg's
unconditional second moment of S(t) (~ log log T / (2 pi^2),
ensemble-rms grade), and zero-density estimates.  The supply table
below carries the conditionality of every row explicitly.

THE DEMAND LEDGER (exact; from the S0-proven bilinear form of the
alias probe).  Per frame (h, D), with pole direction p-hat:
    tau = L - Ss^2/(4 P0) + O(P0^-2),
    L   = sum_gamma f(gamma),
    f(gamma) = 4 w_gamma [p2h S1(gamma) - p1h S2(gamma)]^2 >= 0
(the pole-perpendicular Dirichlet energy; the Schur term Ss^2/4P0 is
measured <= 1e-9 of tau on the battery -- typed, then dropped).  The
demand is a PER-REALIZATION lower bound on the linear statistic L of
the zeros: L >= L_bar - |dL| with L_bar = int f dN_bar (RvM density,
unconditional) and dL = sum f(gamma_i) - L_bar the fluctuation.
Frozen coarse gate: supply suffices at a rung iff its bound on |dL|
is < MARGIN * L_bar with MARGIN = 1/2 (the factor-2 floor).

THE TRANSLATION (machine-checked): unfold t = theta(gamma)/pi + 1
(unit mean spacing).  Then Montgomery's alpha IS the unfolded
frequency omega (cycles per mean spacing): the |alpha| < 1 window is
exactly omega < 1.  With f-tilde(omega) the unfolded Fourier
transform and P(omega) = |f-tilde|^2 the demand spectrum:
    |dL|^2 = |sum_i g(t_i)|^2  (g = f - trend)  is the double sum
    the form factor controls; rms-grade supply scale for a form
    factor S(omega):  sigma_S^2 = int P(omega) S(omega) d omega,
    S = 1 (Poisson diagonal), S = min(omega, 1) (Montgomery window
    + GUE conjecture), S = omega on omega < 1 only (RH-conditional
    Montgomery window piece alone).
WARDS: Parseval (sigma_{S=1}^2 == int g^2 dt, machine); the GUE
pipeline against the direct R2 = 1 - sinc^2 real-space integral for
a sharp interval (Sigma^2(L = 100), agreement <= 2%; the triangle
form factor FT[sinc^2] = (1 - |omega|)_+ checked by quadrature at 3
points, 1e-6); the grid-quality ward (band-split of f re-summed at
the true zeros vs the exact L, <= 5e-2); the split ward
dL_tr + dL_in + dL_out == dL (exact by linearity for dL_out).
TRANSLATION WARD (the task's): RH is verified far beyond T = 2e4,
so the RH-conditional Montgomery window must be CONSISTENT with
measurement: |dL_in| <= 5 sigma_in on >= 90% of rungs; violation =
translation error (fix before reporting).

THE SUPPLY LEDGER (rows, conditionality typed):
  U0 RvM density + Backlund/Trudgian |S(t)| <= 0.112 log t
     + 0.278 log log t + 2.510 (frozen cited constants, VALUES
     ONLY): deterministic per-realization bound
     |dL| <= BT = |f S|_ends + int |f'(t)| B(gamma(t)) dt.
     UNCONDITIONAL.  tau >= L_bar - BT would be theorem-grade.
  U1 Selberg (1946, unconditional) int_0^T S^2 ~ T log log T /
     (2 pi^2): ensemble-rms grade via Minkowski:
     SELB = int |f'| rms_S dt, rms_S = sqrt(log log g / (2 pi^2)
     + 0.5) (local-rms convention, indicative).
  C2 Montgomery 1973 (UNDER RH): F(alpha) = alpha + T^{-2 alpha}
     log T on |alpha| <= 1: the window piece sigma_in^2 =
     int_{omega<1} P omega d omega (rms-grade).
  C3 Montgomery's conjecture / GUE: F = 1 for |alpha| >= 1:
     sigma_GUE^2 = int P min(omega, 1) d omega (rms-grade,
     CONJECTURAL beyond the window).
  P4 Poisson diagonal sigma_P^2 = int P d omega (model reference).
  (Goldston-Montgomery 1987 equivalence (RH): pair correlation <->
  psi short-interval variance -- the short-interval translation of
  the demand is item 4 below; Goldston-Gonek / Ozluk-Snyder
  F-inequalities are RH-conditional refinements -- typed
  qualitatively, no numeric row.)

THE KEY QUESTION (frozen): does ANY part of the demand's spectral
mass sit inside |alpha| < 1?  mass_in = P(1/64 < omega < 1)/P(omega
> 1/64) per rung; a piece is declared if mass_in >= 0.25 anywhere.

ITEM 4 (short intervals): each lag-read of the comb is a tent-
weighted psi-sum over log n in [v - D, v + D]: relative interval
length 2 sinh(D) ~ 2D at x = e^v <= e^{2 alpha}; Goldston-Montgomery
maps our omega-edge to the F-range; per-interval RH gives only
O(sqrt(x) log^2 x) -- the demand needs the weighted CANCELLATION
across scales, i.e. genuinely pair-type input (typed with numbers).

VERDICT (frozen):
  BRIDGE-TRANSLATION-BLOCKED  iff a translation ward fails.
  BRIDGE-PARTIAL-UNCONDITIONAL iff the UNCONDITIONAL row closes a
       rung: BT < MARGIN * L_bar somewhere (reported prominently,
       verified).
  BRIDGE-FULLY-BEYOND  otherwise: the gap typed in alpha-units
       (omega95 per rung vs the window edge 1), the two-tier
       structure (unconditional insufficiency factor; conditional
       window coverage), and the minimal missing input NAMED: an
       unconditional form-factor bound F(alpha, T) <= C_F(rung) out
       to alpha = omega95(rung), C_F = (MARGIN L_bar)^2 / sigma_1^2.

FIREWALL: parent probes and v-modules READ-ONLY; no RNG anywhere;
zeros to 2e4 by the parent RS scan (open, on-line by computation).
Report only, nothing written.
"""

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
import v684_rank3_zeroside as zp               # noqa: E402 (READ-ONLY)
import prime_lagrange_pair_probe as pp         # noqa: E402 (READ-ONLY)
import floor_envelope_depth_probe as fdp       # noqa: E402 (READ-ONLY)
import prime_envelope_analytic_probe as pe     # noqa: E402 (READ-ONLY)
import prime_alias_second_moment_probe as pa   # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen constants
DGRID = fdp.DGRID
DEEP_MS = (1176, 1326, 1414, 1504, 1588, 1632)
N_GRID = 1 << 22            # unfolded grid (dt ~ 0.0054, Nyq ~ 93)
OMEGA_MIN = 1.0 / 64.0      # trend/density band edge (frozen)
MARGIN = 0.5                # the factor-2 floor gate
MASS_IN_BAR = 0.25          # "a demand piece sits inside the window"
CONS_SIG = 5.0              # translation ward: |dL_in| <= 5 sigma_in
CONS_FRAC = 0.90            # ... on >= 90% of rungs
PIPE_BAR = 0.02             # GUE pipeline spectral-vs-realspace
TRI_BAR = 1.0e-6            # triangle form-factor quadrature ward
PARS_BAR = 1.0e-7   # float accumulation over ~2e6 spectral terms
#                     is O(N eps) ~ 1e-9..1e-8; conditioning-aware
GRIDQ_BAR = 5.0e-2
SPLIT_BAR = 2.0e-2
SIGMA_L = 100.0             # pipeline ward interval length
TRUD = (0.112, 0.278, 2.510)   # |S(t)| <= a log t + b llog t + c
SELB_C = 0.5                # local-rms convention constant (typed)
RUNG_PRINT = (0, 11, 22, 33, 44, 55, 66, 67, 68, 69, 70, 71, 72)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def nbar_of(g):
    return zp.theta_rs(np.asarray(g, float)) / math.pi + 1.0


def run():
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
    for i in RUNG_PRINT:
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
    for i in RUNG_PRINT:
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


if __name__ == "__main__":
    run()
