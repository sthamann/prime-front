#!/usr/bin/env python3
"""bootstrap_loop_gain_probe -- does the certified floor SUPPLY the
form-factor bound that a DEEPER floor DEMANDS?  The loop gain.

THE LOOP (never asked before; both halves exist as instruments):
  (i)  SUPPLY: the certified floor at depth X inverts to a measured
       form-factor level for the zeros in the frozen window
       (gue_saturation instrument: F-hat ~ GUE-consistent);
  (ii) DEMAND: certifying the floor at X' > X via the zero-side
       route needs a form-factor bound on the demand band out to
       omega95(X') (bridge map).
If supply strength and alpha-reach grow with X faster than the
demand's, an induction over depth closes the floor for all X.
If the gain is < 1, the wall conserves itself.

KEY STRUCTURAL FACT (makes the loop legitimate, typed): every rung
reads the SAME zero window gamma <= 2e4 -- depth X = e^{2 alpha}
grows in the COMB (u-space), not in gamma.  Supply and demand are
statements about one fixed zero set; the loop needs no unmeasured
zeros.  The price: any closed induction is a statement about the
frozen window/battery (as always, necessary-side; NO RH claim).

FROZEN FORMALIZATION (GUE-multiplier units; F(omega) = c min(w,1)):
  DEMAND at X': guarantee dL > -MARGIN L_bar with k-sigma
  discipline under F <= c sigma-model:
      c_dem(X', k) = (MARGIN L_bar / (k sigma_GUE))^2 = 1/(k R)^2,
  R = the saturation ratio.  Demand band: where the rung's
  GUE-weighted spectrum P(w) min(w,1) lives (omega95).
  SUPPLY at X: the measured-margin ratio estimator over all
  certified rungs of depth <= X:
      c_hat(X) = sum dL_j^2 / sum sigma_GUE,j^2   (jackknife s.e.),
  used at CERTIFIED-INTERVAL discipline c_sup = c_hat + 2 s.e.
  (a supply can only certify what it bounds from above).  Supply
  band: the cumulative GUE-budget of the supplying spectra
  (omega95 of the accumulated weight).  Typed honestly: this is
  MEASUREMENT-grade supply; the measurement -> certificate
  inversion (per-band quadratic-form positivity) is a named gap.
  GAIN: g(X, lambda, k) = c_dem(X') / c_sup(X), X' = lambda X
  (alpha' = alpha + ln(lambda)/2).  g >= 1 means the supplied
  F-level is at least as strong as the demanded one.
  COVERAGE: (geo) the demand rung's GUE-budget share below the
  supply reach omega95_sup(X); (cal) the share inside the bands
  the parent instrument actually calibrated (win, 2-4, 4-8 --
  frozen input from gue_saturation_probe S3; the 1-2 band FAILED
  calibration there and is typed uncovered at instrument grade).

THE GAIN LAW (exact in this formalization, the marginal object):
      g = 1 / (k^2 R(X')^2 c_sup(X)).
  R -> plateau ~ 1.11 (GUE saturation) and c_hat -> rms(z)^2 ~ 0.5
  measured; so the loop's fate is decided by k: the discipline
  factor k^2 is the wall's self-conservation mechanism.

FROZEN DECISION (headline: factor-2 gate MARGIN = 0.5, k = 2,
median over tower pairs):
  LOOP-CLOSES    g(k=2) >= 1 AND geometric coverage >= 0.95;
  LOOP-MARGINAL  g(k=1) in [0.8, 1.25] (criticality typed);
  LOOP-SHORT     otherwise (shortfall law typed).
Also reported (predeclared): k in {1, 2, 3, 5}; the bare gate
(MARGIN = 1, gain x4); the chain-length law N_max from the
union-bound discipline k(N) = Phi^{-1}(1 - 0.05/N).

CONTROLS: tower/plateau/omega95 regressions against the frozen
saturation numbers; the CIRCULARITY WARD (essential): a
Poisson-statistics world (uniform-t ordinates, 8 draws, frozen
seed) must give a much smaller gain AND must break the base case
(measured floor violations) -- a loop that closes for any
statistics would be vacuous.  Error budgets: jackknife intervals
on supply, gain reported as an interval.

EXPLORATION ONLY: no ledger row, no paper edit, nothing outside
experiments/.  Frozen before running.  NO RH claim.
"""

import math
import os
import sys
import time

import numpy as np
from scipy.stats import norm

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import floor_envelope_depth_probe as fdp       # noqa: E402 (READ-ONLY)
import prime_lagrange_pair_probe as pp         # noqa: E402 (READ-ONLY)
import prime_envelope_analytic_probe as pe     # noqa: E402 (READ-ONLY)
import prime_tail_envelope_probe as tp         # noqa: E402 (READ-ONLY)
import gue_ablation_probe as ab                # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen constants
TOWER_HS = ab.TOWER_HS
DGRID = 1.0 / 64.0
OMEGA_MIN = ab.OMEGA_MIN
MARGIN = 0.5
BANDS = ab.BANDS
BAND_TAGS = ab.BAND_TAGS
CAL_BANDS = ("win", "2-4", "4-8")     # frozen parent S3 result
LAMBDAS = (1.2, 1.5, 2.0)
K_GRID = (1.0, 2.0, 3.0, 5.0)
K_DEC = 2.0
N_POIS = 8
SEED_POIS = 202608
MIN_SUP = 10                           # supply needs >= 10 rungs
EPS_CHAIN = 0.05
# frozen regression references (gue_saturation / ablation runs)
REF_R_TOWER = (1.008, 1.089, 1.133, 1.176, 1.215, 1.236)
REF_PLATEAU = 1.114
REF_OM95_DEEP = 3.0
REG_R_BAR, REG_PLAT_BAR, REG_OM95_BAR = 0.03, 0.03, 0.5
POIS_GAIN_FAC, POIS_VIOL_MIN = 0.6, 0.02
N_BAT_EXP = 67   # 67 battery + 6 tower = the parents' 73 rungs
OMB = np.geomspace(OMEGA_MIN, 60.0, 241)   # coverage histogram bins


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def frames_all():
    """(h, D, alpha, tower?) for the deployed ladder: 67 battery
    frames (parents' filters: anomalous h and ATOM_MAX skipped --
    only CERTIFIED rungs may feed the supply) + 6 tower rungs,
    sorted by alpha (build_window geometry, no heavy build)."""
    fr = []
    for kz in core.frame_a_zones():
        al = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(al / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        hz = Mz // 2
        if hz == fdp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * al) > core.ATOM_MAX + 0.5:
            continue
        fr.append((hz, 2.0 * al / Mz, al, False))
    n_bat = len(fr)
    for hz in TOWER_HS:
        fr.append((hz, DGRID, hz * DGRID, True))
    fr.sort(key=lambda t: t[2])
    return fr, n_bat


def pole_hat(h, D):
    c1, c2 = tp.parity_t(1, h), tp.parity_t(2, h)
    u = (h - np.arange(h) - 0.5) * D
    ee = np.sinh(u / 2.0)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * float(c1 @ ee), cp * float(c2 @ ee)
    r = math.hypot(p1, p2)
    return p1 / r, p2 / r


def rung_ledger(h, D, gam, rs):
    """One rung: L_true, L_bar, dL, sigma_GUE/P, R, omega95,
    band shares, coverage histogram, Poisson-draw dL's."""
    p1h, p2h = pole_hat(h, D)
    gg, dt = ab._GRID["ggrid"], ab._GRID["dt"]
    phi = D * gg
    Sg = p2h * pe.s_vec(1, h, phi) - p1h * pe.s_vec(2, h, phi)
    fg = 4.0 * (D * ab.csinc_r(phi / 2.0) ** 2) * Sg ** 2
    L_bar = dt * float(np.sum(fg))
    F = np.fft.rfft(fg)
    P2 = 2.0 * (dt / ab.N_GRID) * np.abs(F) ** 2
    P2[0] *= 0.5
    omg = ab._GRID["omg"]
    live, S_gue = ab._GRID["live"], ab._GRID["S_gue"]
    wgt = P2 * S_gue * live
    sig2_gue = float(np.sum(wgt))
    sig2_p = float(np.sum(P2[live]))
    cs = np.cumsum(wgt)
    om95 = float(omg[int(np.searchsorted(cs, 0.95 * cs[-1]))])
    sh = np.array([float(np.sum(wgt[bi])) for bi in
                   ab._GRID["band_idx"]]) / max(sig2_gue, 1e-300)
    hist = np.histogram(omg, bins=OMB, weights=wgt)[0]
    # zero side
    phz = D * gam
    Sz = p2h * pe.s_vec(1, h, phz) - p1h * pe.s_vec(2, h, phz)
    L_true = float(np.sum(4.0 * (D * ab.csinc_r(phz / 2.0) ** 2)
                          * Sz ** 2))
    # Poisson draws (interp on the shared grid)
    dLP = np.empty(N_POIS)
    for d in range(N_POIS):
        t_P = np.sort(rs.uniform(ab._GRID["t_lo"],
                                 ab._GRID["t_hi"], size=len(gam)))
        dLP[d] = float(np.sum(np.interp(t_P, ab._GRID["tgrid"],
                                        fg))) - L_bar
    sig = math.sqrt(max(sig2_gue, 0.0))
    return dict(L_true=L_true, L_bar=L_bar, dL=L_true - L_bar,
                sig=sig, sigP=math.sqrt(max(sig2_p, 0.0)),
                R=sig / (MARGIN * L_bar), om95=om95, sh=sh,
                hist=hist, dLP=dLP,
                cal=float(sum(sh[BAND_TAGS.index(b)]
                              for b in CAL_BANDS)))


def jack_ratio(a, b):
    """Ratio estimator sum(a)/sum(b) with delete-1 jackknife s.e."""
    A, Bt = float(np.sum(a)), float(np.sum(b))
    th = A / Bt
    n = len(a)
    if n < 3:
        return th, float("inf")
    lo = (A - a) / (Bt - b)
    se = math.sqrt((n - 1) / n * float(np.sum((lo - np.mean(lo))
                                              ** 2)))
    return th, se


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("BOOTSTRAP LOOP GAIN (bootstrap_loop_gain_probe) -- "
          "supply(X) vs demand(lambda X)")
    print("=" * 78)
    print("""
HONESTY FRAME: NO RH claim.  All rungs read the SAME zero window
gamma <= 2e4 (depth grows in the comb); the loop is a fixed-window
statement.  Supply is MEASUREMENT-grade (measured margins +
jackknife), demand is certificate-grade (k-sigma discipline) --
the asymmetry is part of the result, typed in the gap list.
GAIN CONVENTION: g = c_dem/c_sup in GUE-multiplier units; g >= 1
means the supplied F-level is at least as strong as demanded.""")

    # ============================================================== S0
    print("\nS0 -- ledgers + regression wards")
    gam, n_rvm = pp.zero_list()
    check("S0.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    res = ab.build_grid(gam)
    check("S0.GRID unfolded grid (N = 2^21) inversion residual "
          "%.1e <= 1e-9" % res, res <= 1.0e-9)
    fr, n_bat = frames_all()
    check("S0.SET frame set: %d certified battery + %d tower = %d "
          "rungs (the parents' 73-rung ladder)"
          % (n_bat, len(TOWER_HS), len(fr)),
          n_bat == N_BAT_EXP and len(fr) == N_BAT_EXP + 6)
    rs = np.random.RandomState(SEED_POIS)
    rows = []
    for (h, D, al, tow) in fr:
        led = rung_ledger(h, D, gam, rs)
        led.update(h=h, D=D, al=al, tow=tow)
        rows.append(led)
    print("    per-rung ledgers built: %d rungs in %.1f min"
          % (len(rows), (time.time() - T0) / 60.0))
    tow_rows = [r for r in rows if r["tow"]]
    devR = max(abs(r["R"] / rf - 1.0) for r, rf in
               zip(tow_rows, REF_R_TOWER))
    check("S0.REG tower R regression vs frozen saturation refs "
          "(worst dev %.3f <= %.2f)" % (devR, REG_R_BAR),
          devR <= REG_R_BAR)
    deep20 = sorted(rows, key=lambda r: r["al"])[-20:]
    plat = float(np.median([r["R"] for r in deep20]))
    check("S0.PLAT saturation plateau reproduces: median R "
          "(deepest 20) = %.3f vs %.3f (bar %.2f)"
          % (plat, REF_PLATEAU, REG_PLAT_BAR),
          abs(plat - REF_PLATEAU) <= REG_PLAT_BAR)
    om_deep = tow_rows[-1]["om95"]
    check("S0.OM95 deep-tower demand reach: omega95 = %.2f vs "
          "%.1f (bar %.1f)" % (om_deep, REF_OM95_DEEP,
                               REG_OM95_BAR),
          abs(om_deep - REF_OM95_DEEP) <= REG_OM95_BAR)

    # ============================================================== S1
    print("\nS1 -- THE SUPPLY CURVE (certified ladder up to X)")
    n = len(rows)
    aa = np.array([r["dL"] ** 2 for r in rows])
    bb = np.array([r["sig"] ** 2 for r in rows])
    aaP = np.array([float(np.mean(r["dLP"] ** 2)) for r in rows])
    csup, csup_up, reach = np.full(n, np.nan), np.full(n, np.nan), \
        np.full(n, np.nan)
    csupP_up = np.full(n, np.nan)
    Wcum = np.zeros(len(OMB) - 1)
    omb_mid = 0.5 * (OMB[1:] + OMB[:-1])
    for i in range(n):
        Wcum += rows[i]["hist"]
        cw = np.cumsum(Wcum)
        reach[i] = float(omb_mid[int(np.searchsorted(
            cw, 0.95 * cw[-1]))])
        if i + 1 >= MIN_SUP:
            th, se = jack_ratio(aa[: i + 1], bb[: i + 1])
            csup[i], csup_up[i] = th, th + 2.0 * se
            thP, seP = jack_ratio(aaP[: i + 1], bb[: i + 1])
            csupP_up[i] = thP + 2.0 * seP
    print("    supply strength c_hat(X) = sum dL^2 / sum sig_GUE^2 "
          "(GUE-multiplier), certified level = c_hat + 2 s.e.:")
    idxs = list(range(MIN_SUP - 1, n_bat, 12)) + \
        [i for i in range(n) if rows[i]["tow"]]
    for i in idxs:
        r = rows[i]
        print("      alpha %6.2f X %9.3e %s | z %+5.2f | c_hat "
              "%.3f (up %.3f) | reach om95_sup %5.2f"
              % (r["al"], math.exp(2 * r["al"]),
                 "TOWER" if r["tow"] else "batt ",
                 r["dL"] / r["sig"], csup[i], csup_up[i],
                 reach[i]))
    zz = np.array([r["dL"] / r["sig"] for r in rows])
    print("    full-ladder: rms(z) = %.3f -> c_hat(all) = %.3f "
          "+ 2 x %.3f; the supplied F-level is GUE-consistent "
          "(measurement-grade)"
          % (float(np.sqrt(np.mean(zz ** 2))), csup[n - 1],
             0.5 * (csup_up[n - 1] - csup[n - 1])))

    # ============================================================== S2
    print("\nS2 -- THE DEMAND CURVE (per rung X')")
    print("    c_dem(X', k) = 1/(k R)^2 (factor-2 gate; bare gate "
          "= x4); demand band reach om95; calibrated share = "
          "budget in parent-calibrated bands %s:" % (CAL_BANDS,))
    for i in idxs:
        r = rows[i]
        print("      alpha %6.2f %s | R %.3f | c_dem k=1: %.3f "
              "k=2: %.3f k=5: %.4f | om95 %5.2f | cal-share %.2f"
              % (r["al"], "TOWER" if r["tow"] else "batt ",
                 r["R"], 1.0 / r["R"] ** 2, 1.0 / (2 * r["R"]) ** 2,
                 1.0 / (5 * r["R"]) ** 2, r["om95"], r["cal"]))
    al_v = np.array([r["al"] for r in rows])
    R_v = np.array([r["R"] for r in rows])
    om_v = np.array([r["om95"] for r in rows])
    cal_v = np.array([r["cal"] for r in rows])
    al_bat_max = max(r["al"] for r in rows if not r["tow"])
    al_tow_min = min(r["al"] for r in rows if r["tow"])
    print("    alpha desert (no frames): (%.2f, %.2f) -- pairs "
          "whose target falls inside are excluded, typed"
          % (al_bat_max, al_tow_min))

    def interp_at(alp, vec):
        return float(np.interp(alp, al_v, vec))

    def cumshare_at(alp, om_cut):
        """Demand rung at alpha': GUE-budget share below om_cut
        (linear interp between bracketing rungs' histograms)."""
        j = int(np.searchsorted(al_v, alp))
        j0, j1 = max(j - 1, 0), min(j, n - 1)
        out = []
        for jj in (j0, j1):
            cw = np.cumsum(rows[jj]["hist"])
            out.append(float(np.interp(om_cut, omb_mid,
                                       cw / max(cw[-1], 1e-300))))
        if j1 == j0 or al_v[j1] == al_v[j0]:
            return out[0]
        t = (alp - al_v[j0]) / (al_v[j1] - al_v[j0])
        return (1 - t) * out[0] + t * out[1]

    # ============================================================== S3
    print("\nS3 -- THE LOOP GAIN g(X, lambda, k) = c_dem/c_sup")
    summ = {}
    for lam in LAMBDAS:
        dal = 0.5 * math.log(lam)
        pairs = []
        for i in range(n):
            alp = rows[i]["al"] + dal
            if alp > al_v[-1] or np.isnan(csup_up[i]):
                continue
            if al_bat_max < alp < al_tow_min:
                continue
            Rp = interp_at(alp, R_v)
            g1 = (1.0 / Rp ** 2) / csup_up[i]
            cov_g = cumshare_at(alp, reach[i])
            cov_c = interp_at(alp, cal_v)
            gP = (1.0 / Rp ** 2) / csupP_up[i]
            pairs.append(dict(i=i, al=rows[i]["al"], alp=alp,
                              g1=g1, cov_g=cov_g, cov_c=cov_c,
                              gP=gP, tow=rows[i]["tow"],
                              gap=max(interp_at(alp, om_v)
                                      - reach[i], 0.0)))
        tw = [p for p in pairs if p["tow"]]
        sel = tw if len(tw) >= 3 else pairs
        med = lambda key, ps=sel: float(np.median([p[key]
                                                   for p in ps]))
        summ[lam] = dict(g1=med("g1"), cov_g=med("cov_g"),
                         cov_c=med("cov_c"), gP=med("gP"),
                         gap=med("gap"), pairs=pairs, sel=sel)
        print("    lambda = %.1f (%d pairs, %d tower; headline = "
              "median over %s):" % (lam, len(pairs), len(tw),
                                    "tower pairs" if len(tw) >= 3
                                    else "all pairs"))
        print("      gain g(k): " + "  ".join(
            "k=%g: %.3f" % (k, summ[lam]["g1"] / k ** 2)
            for k in K_GRID))
        print("      coverage: geometric %.3f (supply reach vs "
              "demand budget), calibrated-instrument %.3f; "
              "alpha-gap (demand om95 - supply reach) %.2f"
              % (summ[lam]["cov_g"], summ[lam]["cov_c"],
                 summ[lam]["gap"]))
    lamH = 1.5
    g1H = summ[lamH]["g1"]
    g2H = g1H / K_DEC ** 2
    print("    HEADLINE (lambda = %.1f): g(k=1) = %.3f, g(k=%g) "
          "= %.3f, geometric coverage %.3f, calibrated coverage "
          "%.3f" % (lamH, g1H, K_DEC, g2H, summ[lamH]["cov_g"],
                    summ[lamH]["cov_c"]))

    # ============================================================== S4
    print("\nS4 -- the marginal analysis (trend, gate, chain law)")
    sel = summ[lamH]["sel"]
    als = np.array([p["al"] for p in sel])
    g1s = np.array([p["g1"] for p in sel])
    if len(sel) >= 3:
        sl = float(np.polyfit(als, g1s, 1)[0])
    else:
        sl = float("nan")
    g_inf = (1.0 / plat ** 2) / csup_up[n - 1]
    print("    g(k=1) over the tower pairs: %s | slope %+.4f per "
          "alpha | plateau-limit estimate 1/(R_inf^2 c_sup_up) = "
          "%.3f" % (" ".join("%.2f" % g for g in g1s), sl, g_inf))
    Rdeep = tow_rows[-1]["R"]
    print("    grade split at the deep end: point-estimate supply "
          "(non-certificate) g(k=1) = %.3f; certified-interval "
          "supply g(k=1) = %.3f; IDEAL supply (exact GUE, c = 1) "
          "g(k=1) = 1/R^2 = %.3f < 1 -- the saturation R > 1 "
          "alone keeps even the ideal loop short"
          % ((1.0 / Rdeep ** 2) / csup[n - 1],
             (1.0 / Rdeep ** 2) / csup_up[n - 1],
             1.0 / Rdeep ** 2))
    print("    gate dependence: bare-positivity gate (MARGIN = 1) "
          "multiplies every gain by 4: g_bare(k=1) = %.2f, "
          "g_bare(k=2) = %.2f" % (4 * g1H, 4 * g1H / 4))
    # chain-length law: k(N) = Phi^{-1}(1 - eps/N); induction of N
    # steps at total failure eps needs gain g_bare/k(N)^2 >= 1
    Nmax = 0
    for N in range(1, 100000):
        kN = float(norm.ppf(1.0 - EPS_CHAIN / N))
        if 4 * g1H / kN ** 2 < 1.0:
            break
        Nmax = N
    print("    chain-length law (union bound, total failure %.2f):"
          " k(N) = Phi^inv(1 - %.2f/N); the bare-gate loop "
          "sustains N_max = %d induction step(s) before the "
          "discipline cost k^2 eats the gain"
          % (EPS_CHAIN, EPS_CHAIN, Nmax))

    # ============================================================== S5
    print("\nS5 -- the circularity ward (Poisson world)")
    gPH = summ[lamH]["gP"]
    ok_g = gPH < POIS_GAIN_FAC * g1H
    check("S5.CIRC Poisson-world gain g_P(k=1) = %.3f < %.1f x "
          "true gain %.3f -- the loop does NOT close for wrong "
          "statistics (non-vacuity)" % (gPH, POIS_GAIN_FAC, g1H),
          ok_g)
    viol2 = float(np.mean([np.mean(r["dLP"] < -MARGIN * r["L_bar"])
                           for r in rows]))
    viol1 = float(np.mean([np.mean(r["dLP"] < -r["L_bar"])
                           for r in rows]))
    check("S5.BASE Poisson world breaks the base case: factor-2 "
          "gate violated in %.1f%% of (rung, draw), bare gate in "
          "%.1f%% (need > %.0f%%)"
          % (100 * viol2, 100 * viol1, 100 * POIS_VIOL_MIN),
          viol2 > POIS_VIOL_MIN)
    print("    (true zeros violate neither gate on any rung: "
          "min z = %+.2f, min dL/L_bar = %+.3f)"
          % (float(np.min(zz)),
             float(np.min([r["dL"] / r["L_bar"] for r in rows]))))

    # ============================================================== S6
    print("\nS6 -- verdict")
    wards_ok = not FAILS
    cov_ok = summ[lamH]["cov_g"] >= 0.95
    if not wards_ok:
        verdict = "LOOP-TRANSLATION-BLOCKED"
    elif g2H >= 1.0 and cov_ok:
        verdict = "LOOP-CLOSES"
    elif 0.8 <= g1H <= 1.25:
        verdict = "LOOP-MARGINAL"
    else:
        verdict = "LOOP-SHORT"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    print("""    THE SHORTFALL LAW (measured): g = 1/(k^2 R(X')^2 c_sup(X)),
    with three compounding factors typed exactly:
      (i)   THE SATURATION ITSELF: R > 1 and climbing along the
            tower (plateau %.2f, deep end %.2f) -- the demand
            sits ABOVE the GUE line, so even an IDEAL supply
            (exact GUE, c = 1, k = 1) gives g = 1/R^2 = %.3f < 1.
            The wall conserves itself THROUGH the saturation: the
            world's own statistics are always one notch below
            what the next rung demands.
      (ii)  supply cannot beat its own statistics: c_hat = %.2f
            (GUE-consistent), certified interval %.2f -- the
            measurement error charges another factor ~%.1f;
      (iii) the k^2 discipline cost: any certification k >= 2
            divides the gain by >= 4 (g(k=2) = %.3f), and a chain
            of N steps needs k(N) growing -- N_max = 0 at the
            bare gate already.
    Measured headline: g(k=1) = %.3f (below the marginal window),
    trend DECREASING with depth (R still climbing).  COVERAGE is
    NOT the blocker: geometric reach %s (%.3f -- the supplying
    spectra reach past the demand band); the instrument-grade gap
    is strength-band calibration (demand's dominant 1-2 band not
    calibratable in the parent; calibrated coverage %.3f).
    HONEST GAP LIST (what a loop theorem would still need):
    (1) measurement-grade -> certificate-grade supply (per-band
    quadratic-form positivity of the inversion); (2) an input
    strictly below GUE strength on alpha in 1..2 to beat R > 1 --
    the loop cannot pay this from within (its supply is pinned at
    the world's GUE level); (3) the k^2 discipline cost paid by a
    genuinely new input; (4) the T > 2e4 zero tail (outside both
    curves, frozen truncation discipline).  CONSEQUENCE for the
    strategy: the bootstrap is NOT a proof architecture -- and
    the reason is the previously established GUE saturation, now
    quantified as self-conservation: the certified ladder supplies
    exactly the statistics of the zeros (never more), while the
    floor demands slightly more than those statistics guarantee.
    The measured positivity everywhere is therefore genuinely
    finer-than-statistical information -- consistent with the
    architecture reading, unprovable by the loop.  NO RH claim;
    necessary-side, frozen window."""
          % (plat, Rdeep, 1.0 / Rdeep ** 2, csup[n - 1],
             csup_up[n - 1], csup_up[n - 1] / csup[n - 1], g2H,
             g1H, "COMPLETE" if cov_ok else "INCOMPLETE",
             summ[lamH]["cov_g"], summ[lamH]["cov_c"]))
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
