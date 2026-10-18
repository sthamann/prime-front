#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v831 -- PRIME.FLOOR.ALIASMOMENT.01: the correlation-corrected alias second moment closes the analytic-envelope route at its typed circularity boundary and registers the floor <-> pair-correlation bridge -- the honest typed closure, ONE module from one probe (15 checks with the SEVEN preregistered-honest FAILs S1.SIGN/W2B/W2C/W2D/S4.GEOM/C1/C2 -- the FAIL pattern IS the finding: the frozen premise 'the phases carry the gap' is OVERTURNED by the measurement; discovery probe prime_alias_second_moment_probe.py ALIAS-CORRELATION-PAIRCORR, 2026-08-07, re-run identically at promotion).  THE EXACT BILINEAR FORM (sympy-proven, identity-warded): in the pole frame the correlation-corrected alias second moment is EXACT -- M2 = [[P0 + (S2+Sc)/2, Ss/2], [Ss/2, (S2-Sc)/2]] with tau = lambda_min = (S2 - Sc)/2 - Ss^2/(4 P0) + O(P0^-2), so the correlation combination multiplying the leading term is the coherent phase sum Sc (rotation-invariance ward at the conditioning-aware machine bar on all 73 battery frames; truncated-series dev 3.8e-7).  THE PREMISE OVERTURNED (the round's finding): the AMPLITUDES, not the phases, carry the h^{-2.5} tower gap -- the diagonal (random-phase) part tau_diag = S2/2 does NOT reproduce the derived -1 law but slopes -3.17 (W2B), the phase scramble and the Poissonized zeros land at -3.05/-3.65 not -1 (W2C/W2D), and q = Sc/S2 changes sign across the battery (S1.SIGN: q in [-0.324, 0.552], median 0.19; deep suppression only x1.1) -- the tower law decomposes EXACTLY as -2.505 = amplitude law (-3.172) + fading alignment (+0.668).  THE GUINAND SPLIT (exact, not a regression): by the deployed identity G_Z = (B - Sp - P) + (Sp - S), the smooth share is -994.15 and the prime-fluctuation share +995.15 -- each ~1000x LARGER than the residual, cancelling to |Sc_fluc|/sigma_sqrt = 0.01 of the Poisson-comb square-root scale (SQRT-CANCELLATION REGIME; identity route residue 0.019, soft bar met); the smooth surrogate does NOT carry it (S4.GEOM: residue 0.868, deficit-slope dev 2.274); the comb scramble EXPLODES the coherent sum x2.0e6..1.7e7 and the Epstein x^2+5y^2 comb x5.1e3..1.3e4 -- THE CANCELLATION IS THE ARITHMETIC.  THE TYPED CIRCULARITY BOUNDARY (the honest closure): the suppression exists because the prime-comb fluctuations cancel exactly as far as square-root cancellation allows -- variance-type control; proving the tower tau-law requires bounding an oscillatory prime sum AT its sqrt scale = pair-correlation-equivalent substance (Montgomery-type input on the zero side by the explicit formula), and by Guinand the comb's self-cancellation IS the zero-side floor statement itself -- the required control is even DEEPER than pair-correlation input.  THE ROUTE CLOSURE (deliverable): the analytic-envelope route of PRIME.FLOOR.RATIO.01 is CLOSED HONESTLY at this boundary -- its envelope constant is arithmetic substance equivalent to the target; no further analytic-envelope variants (stop-list entry per house discipline).  THE NAMED CONTRACT: PRIME.FLOOR.PAIRCORR.01 [O] -- the floor <-> pair-correlation bridge.  Controls: the Poissonized-zero and phase-scramble controls C1/C2 restate the overturned premise (typed FAILs); the comb-side fingerprints fire comb-specifically.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe prime_alias_second_moment_probe.py
(2026-08-07, 15 checks with the SEVEN preregistered-honest FAILs
S1.SIGN / W2B / W2C / W2D / S4.GEOM / C1 / C2, verdict
ALIAS-CORRELATION-PAIRCORR, re-run identically at promotion; log in
experiments/tfpt-discovery/).  NO DOWNSCOPING (predeclared): the
probe's measured runtime at promotion is ~0.1 min in-tree (the zero
list is the v823 cache + vectorized RS scan; the 73-frame battery
builds in ~2 s) -- this module runs the full frozen protocol
VERBATIM: the sympy bilinear form, the 73-frame battery, the full
tower h = 588..816 step 4 with all four exponent wards, the
correlation-structure report, the exact Guinand split on all 67 old
frames, the three-candidate identification, and all controls.  The
original probe docstring and frozen protocol live in the probe file
verbatim.  The frozen wards W2B/W2C/W2D and S1.SIGN encode the
OVERTURNED premise (phases-carry-the-gap); their FAILs are the
preregistered-honest signature of the finding and are pattern-gated.

FIREWALL: v563 / v684 / v823 / v829 / v830 READ-ONLY; zero values
used openly (on-line by computation <= 2e4 via the v823 cache + RS
scan; no zetazero()/nzeros() calls in this module); RNG only in the
declared seed-7 controls (Poissonized ordinates + phase scramble,
consumption order frozen).  NO RH claim.
"""
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v684_rank3_zeroside as zp               # noqa: E402 (READ-ONLY)
import v823_prime_lagrange_floor as pp         # noqa: E402 (READ-ONLY)
import v829_prime_floor_depth as fd            # noqa: E402 (READ-ONLY)
import v830_prime_float_budget as fb           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen constants
DGRID = fd.DGRID
ANOMALOUS_H = 1292                 # v563/v818 declaration
DEEP_MS = (1176, 1326, 1414, 1504, 1588, 1632)
TOWER_HS = tuple(range(588, 817, 4))
SEED = 7
IDW_BAR = 1.0e-10
W2A_RANGE = (-2.8, -2.2)
RP_RANGE = (-1.35, -0.65)
W2C_MED = 0.20
W2D_QFRAC = 0.5
IDRES_GATE = 0.30
IDRES_SOFT = 0.15
GEOM_MED = 0.30
GEOM_SLOPE = 0.35
ARITH_SHARE = 0.60
SCALE_BAR = 3.0
CTRL_FRAMES = (0, 33, 66)          # predeclared old-ladder indices
PAIR_BINS = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)
PAIR_OFF_MAX = 160
CELL_BAND = 5
EPSM = float(np.finfo(float).eps)
EXPECTED_FAILS = ("C1", "C2", "S1.SIGN", "S4.GEOM", "W2B", "W2C",
                  "W2D")
EXPECTED_VERDICT = "ALIAS-CORRELATION-PAIRCORR"


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def epstein_counts(Nmax):
    """r_{x^2+5y^2}(n) counts (probe-verbatim control comb)."""
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


def pole_frame(h, D, gam):
    """Closed-form components rotated into the pole frame."""
    Xv, av, bv, p1, p2 = fb.fam_closed(h, D, gam)
    P0 = p1 * p1 + p2 * p2
    r = math.sqrt(P0)
    x = (av * p1 + bv * p2) / r
    y = (av * p2 - bv * p1) / r
    return dict(x=x, y=y, av=av, bv=bv, p1=p1, p2=p2, P0=P0,
                S2=float(x @ x + y @ y), Sc=float(x @ x - y @ y),
                Ss=2.0 * float(x @ y))


def tau_of(fr):
    """Exact tau/lam from the pole-frame sums (and the direct M2)."""
    P0, S2, Sc, Ss = fr["P0"], fr["S2"], fr["Sc"], fr["Ss"]
    Mrot = np.array([[P0 + 0.5 * (S2 + Sc), 0.5 * Ss],
                     [0.5 * Ss, 0.5 * (S2 - Sc)]])
    lam_r, tau_r = fd.eig2(Mrot)
    av, bv, p1, p2 = fr["av"], fr["bv"], fr["p1"], fr["p2"]
    Md = np.array([[float(av @ av) + p1 * p1,
                    float(av @ bv) + p1 * p2],
                   [float(av @ bv) + p1 * p2,
                    float(bv @ bv) + p2 * p2]])
    lam_d, tau_d = fd.eig2(Md)
    # conditioning-aware ward: tau = mid - R cancels ~ lam/tau ulps
    # (family-probe adaptive-identity convention)
    bar = max(IDW_BAR, 200.0 * EPSM * abs(lam_d)
              / max(abs(tau_d), 1e-300))
    idw = (abs(tau_r - tau_d) / max(abs(tau_d), 1e-300)) / bar
    return tau_d, lam_d, idw


def aniso(G, p1, p2):
    """(Sc, Ss)-type anisotropy of a 2x2 block in the pole frame."""
    r = math.hypot(p1, p2)
    e = np.array([p1, p2]) / r
    f = np.array([p2, -p1]) / r
    sc = float(e @ G @ e - f @ G @ f)
    ss = 2.0 * float(e @ G @ f)
    s2 = float(np.trace(G))
    return sc, ss, s2


def theta_invert(targets, x0):
    """Vectorized Newton for theta_rs(g) = target (RvM surrogate)."""
    x = np.array(x0, float)
    for _ in range(60):
        f = zp.theta_rs(x) - targets
        dp = 0.5 * np.log(np.maximum(x, 8.0) / (2.0 * math.pi))
        step = f / np.maximum(dp, 0.05)
        x = np.maximum(x - step, 10.0)
        if float(np.max(np.abs(step))) < 1e-12:
            break
    return x


def slope_fit(hs, ys):
    b, _, r2 = fb.ols_loglog(hs, ys)
    return b, r2


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v831 -- PRIME.FLOOR.ALIASMOMENT.01: the correlation-"
          "corrected alias second moment")
    print("(the honest typed closure of the analytic-envelope route; "
          "the SEVEN premise-")
    print(" overturning FAILs are EXPECTED and pattern-gated; NO RH "
          "claim)")
    print("=" * 78)
    print("""
HONESTY FRAME: the pair structure of alias phases at ordinates
gamma_k is a pair-correlation-type object.  If the derivation
requires zero pair-correlation input (Montgomery-type, conjectural),
that is a TYPED CIRCULARITY BOUNDARY, not a result.  NO RH claim.""")

    # ============================================================== S0
    print("\nS0 -- the exact bilinear form (sympy-checked)")
    import sympy as sp
    P0s, S2s, Scs, Sss = sp.symbols("P0 S2 Sc Ss", positive=True)
    M = sp.Matrix([[P0s + (S2s + Scs) / 2, Sss / 2],
                   [Sss / 2, (S2s - Scs) / 2]])
    tr, dt = sp.trace(M), M.det()
    tau_sym = (tr - sp.sqrt(tr ** 2 - 4 * dt)) / 2
    lead = sp.limit(tau_sym, P0s, sp.oo)
    corr = sp.limit(P0s * (tau_sym - lead), P0s, sp.oo)
    check("S0.B1 lambda_min leading term == (S2 - Sc)/2 (the "
          "correlation combination multiplying the leading term is "
          "the coherent phase sum Sc)",
          sp.simplify(lead - (S2s - Scs) / 2) == 0)
    check("S0.B2 the 1/P0 correction == -Ss^2/4 (tau = (S2 - Sc)/2 "
          "- Ss^2/(4 P0) + O(P0^-2); Schur term exact)",
          sp.simplify(corr + Sss ** 2 / 4) == 0)
    check("S0.B3 det identity: det M2 == (P0 + (S2+Sc)/2)(S2-Sc)/2 "
          "- Ss^2/4 (exact algebra)",
          sp.simplify(dt - ((P0s + (S2s + Scs) / 2)
                            * (S2s - Scs) / 2 - Sss ** 2 / 4)) == 0)

    # ============================================================== S1
    print("\nS1 -- the object on the deployed battery (73 frames)")
    gam, n_rvm = pp.zero_list()
    check("S1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    rows = []
    t0 = time.time()
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(h=rr["h"], M=rr["M"], D=rr["D"],
                         alpha=rr["alpha"], rr=rr, deep=False))
    rows.sort(key=lambda w: w["alpha"])
    for Mz in DEEP_MS:
        rows.append(dict(h=Mz // 2, M=Mz, D=DGRID,
                         alpha=(Mz // 2) * DGRID, rr=None, deep=True))
    worst_idw = 0.0
    for w in rows:
        fr = pole_frame(w["h"], w["D"], gam)
        tau_z, lam_z, idw = tau_of(fr)
        worst_idw = max(worst_idw, idw)
        w.update(fr=fr, tau_z=tau_z, lam_z=lam_z,
                 q=fr["Sc"] / fr["S2"], S2=fr["S2"], Sc=fr["Sc"],
                 Ss=fr["Ss"], P0=fr["P0"])
        w["tau_series"] = (0.5 * (fr["S2"] - fr["Sc"])
                           - fr["Ss"] ** 2 / (4.0 * fr["P0"]))
    print("    built %d frames in %.0f s" % (len(rows),
                                             time.time() - t0))
    check("S1.IDW rotation-invariance ward: tau from (P0, S2, Sc, "
          "Ss) == direct M2 on all 73 frames (worst margin ratio "
          "%.2f <= 1 against the conditioning-aware bar "
          "max(%.0e, 200 eps lam/tau))" % (worst_idw, IDW_BAR),
          worst_idw <= 1.0)
    ser_dev = max(abs(w["tau_series"] - w["tau_z"])
                  / abs(w["tau_z"]) for w in rows)
    print("    the truncated series tau ~ (S2-Sc)/2 - Ss^2/(4P0): "
          "worst rel dev %.1e over 73 frames (typed)" % ser_dev)
    q_all = [w["q"] for w in rows]
    check("S1.SIGN [EXPECTED FAIL -- the premise overturned] the "
          "cancellation coefficient q = Sc/S2 > 0 on all 73 frames "
          "(q = %.4f..%.4f, median %.4f): alignment with the pole "
          "== NEGATIVE perp-channel pair correlation (convention "
          "typed above)"
          % (min(q_all), max(q_all), float(np.median(q_all))),
          min(q_all) > 0.0)
    w_deep = rows[-1]
    print("    deep example M = 1632: S2 = %.4e, Sc = %.4e "
          "(q = %.5f), Ss = %.2e, P0 = %.3e, tau_z = %.3e vs "
          "tau_RP = S2/2 = %.3e (suppression x%.1f)"
          % (w_deep["S2"], w_deep["Sc"], w_deep["q"], w_deep["Ss"],
             w_deep["P0"], w_deep["tau_z"], 0.5 * w_deep["S2"],
             0.5 * w_deep["S2"] / w_deep["tau_z"]))

    # ============================================================== S2
    print("\nS2 -- the split and the exponent wards (tower "
          "h = 588..816, D = 1/64)")
    rng = np.random.default_rng(SEED)
    # RvM-smooth surrogate ordinates (frozen convention k - 3/2)
    kk = np.arange(1, len(gam) + 1, dtype=float)
    g_rvm = theta_invert((kk - 1.5) * math.pi, gam)
    mono = bool(np.all(np.diff(g_rvm) > 0))
    res_th = float(np.max(np.abs(zp.theta_rs(g_rvm)
                                 - (kk - 1.5) * math.pi)))
    check("S2.RVM smooth surrogate ordinates theta(g_k) = "
          "(k - 3/2) pi: monotone %s, residual %.1e, last = %.1f "
          "(true 2e4 window)" % (mono, res_th, g_rvm[-1]),
          mono and res_th < 1e-8 and abs(g_rvm[-1] - 2.0e4) < 6.0)
    # Poissonized zeros: uniform order statistics in theta-space
    th_lo = float(zp.theta_rs(np.array([float(gam[0])]))[0])
    th_hi = float(zp.theta_rs(np.array([2.0e4]))[0])
    uu = np.sort(rng.uniform(th_lo, th_hi, size=len(gam)))
    g0 = np.interp(uu, zp.theta_rs(g_rvm), g_rvm)
    g_poi = theta_invert(uu, g0)
    print("    Poissonized ordinates (seed %d): %d points, "
          "density-matched in theta-space (rigidity killed)"
          % (SEED, len(g_poi)))
    tw = dict(true=[], diag=[], scr=[], poi=[], rvm=[],
              q_true=[], q_poi=[], q_rvm=[])
    for h_t in TOWER_HS:
        fr = pole_frame(h_t, DGRID, gam)
        tau_t, _, _ = tau_of(fr)
        tw["true"].append(tau_t)
        tw["diag"].append(0.5 * fr["S2"])
        tw["q_true"].append(fr["Sc"] / fr["S2"])
        # phase scramble: keep amplitudes, uniform psi
        A2 = fr["x"] ** 2 + fr["y"] ** 2
        psi = rng.uniform(-math.pi, math.pi, size=len(A2))
        S2v = float(np.sum(A2))
        Scv = float(np.sum(A2 * np.cos(2.0 * psi)))
        Ssv = float(np.sum(A2 * np.sin(2.0 * psi)))
        Mr = np.array([[fr["P0"] + 0.5 * (S2v + Scv), 0.5 * Ssv],
                       [0.5 * Ssv, 0.5 * (S2v - Scv)]])
        _, tau_s = fd.eig2(Mr)
        tw["scr"].append(tau_s)
        fp = pole_frame(h_t, DGRID, g_poi)
        tau_p, _, _ = tau_of(fp)
        tw["poi"].append(tau_p)
        tw["q_poi"].append(fp["Sc"] / fp["S2"])
        fv = pole_frame(h_t, DGRID, g_rvm)
        tau_v, _, _ = tau_of(fv)
        tw["rvm"].append(tau_v)
        tw["q_rvm"].append(fv["Sc"] / fv["S2"])
    sl_true, r2t = slope_fit(TOWER_HS, tw["true"])
    sl_diag, _ = slope_fit(TOWER_HS, tw["diag"])
    sl_scr, _ = slope_fit(TOWER_HS, tw["scr"])
    sl_poi, _ = slope_fit(TOWER_HS, tw["poi"])
    sl_1mq, _ = slope_fit(TOWER_HS,
                          [1.0 - q for q in tw["q_true"]])
    sl_1mq_rvm, _ = slope_fit(TOWER_HS,
                              [1.0 - q for q in tw["q_rvm"]])
    check("W2A the full tau_z tower law reproduces h^{-2.5}: slope "
          "%+.3f in [%.1f, %.1f] (R^2 %.2f)"
          % (sl_true, *W2A_RANGE, r2t),
          W2A_RANGE[0] <= sl_true <= W2A_RANGE[1])
    check("W2B [EXPECTED FAIL -- the AMPLITUDES carry the gap] the "
          "DIAGONAL (random-phase) part tau_diag = S2/2 reproduces "
          "the -1 law: slope %+.3f in [%.2f, %.2f] -- the "
          "discrepancy lives in the amplitude law, NOT the phases"
          % (sl_diag, *RP_RANGE),
          RP_RANGE[0] <= sl_diag <= RP_RANGE[1])
    med_scr = float(np.median(np.abs(
        np.array(tw["scr"]) / np.array(tw["diag"]) - 1.0)))
    check("W2C [EXPECTED FAIL] phase scramble (seed %d) restores "
          "the RP law: slope %+.3f in [%.2f, %.2f], median "
          "|tau_scr/tau_diag - 1| = %.3f <= %.2f"
          % (SEED, sl_scr, *RP_RANGE, med_scr, W2C_MED),
          RP_RANGE[0] <= sl_scr <= RP_RANGE[1]
          and med_scr <= W2C_MED)
    q_med_t = float(np.median(tw["q_true"]))
    q_med_p = float(np.median(tw["q_poi"]))
    check("W2D [EXPECTED FAIL] POISSONIZED ZEROS (seed %d): tau "
          "slope %+.3f in [%.2f, %.2f] and median q_poiss = %.4f "
          "<= %.1f x median q_true = %.4f"
          % (SEED, sl_poi, *RP_RANGE, q_med_p, W2D_QFRAC, q_med_t),
          RP_RANGE[0] <= sl_poi <= RP_RANGE[1]
          and q_med_p <= W2D_QFRAC * q_med_t)
    print("    the correlation deficit law: (1 - q_true) ~ h^%+.3f "
          "(the FADING alignment; with the amplitude law %+.3f it "
          "decomposes the tower EXACTLY: %+.3f + %+.3f = %+.3f vs "
          "measured %+.3f); (1 - q_rvm) ~ h^%+.3f (smooth surrogate)"
          % (sl_1mq, sl_diag, sl_diag, sl_1mq, sl_diag + sl_1mq,
             sl_true, sl_1mq_rvm))

    # ============================================================== S3
    print("\nS3 -- the correlation structure (decay, banding, "
          "range)")
    frD = rows[-1]["fr"]
    A2D = frD["x"] ** 2 + frD["y"] ** 2
    psiD = np.arctan2(frD["y"], frD["x"])
    zph = A2D * np.exp(2.0j * psiD)
    m_idx = np.round(gam * DGRID / (2.0 * math.pi)).astype(int)
    m_max = int(m_idx.max())
    z_m = np.zeros(m_max + 1, complex)
    s_m = np.zeros(m_max + 1)
    np.add.at(z_m, m_idx, zph)
    np.add.at(s_m, m_idx, A2D)
    c_m = np.where(s_m > 0, z_m.real / np.maximum(s_m, 1e-300), 0.0)
    print("    cell coherence c_m = Sc_m/S2_m at M = 1632: "
          "median %.3f, min %.3f, max %.3f over %d cells (m >= 1); "
          "m = 0 cell (pre-alias) c_0 = %.3f"
          % (float(np.median(c_m[1:])), float(np.min(c_m[1:])),
             float(np.max(c_m[1:])), m_max, c_m[0]))
    # cross-cell banding via the cell phasors
    zn = z_m[1:] / np.maximum(np.abs(z_m[1:]), 1e-300)
    band = []
    for dm in range(1, CELL_BAND + 1):
        band.append(float(np.mean(
            np.real(zn[dm:] * np.conj(zn[:-dm])))))
    print("    cross-cell phasor coherence <cos 2(Ph_m - Ph_m')>: "
          + ", ".join("dm=%d: %+.3f" % (i + 1, v)
                      for i, v in enumerate(band)))
    # pair statistics binned by ordinate distance (banded)
    nb = len(PAIR_BINS) - 1
    num = np.zeros(nb)
    den = np.zeros(nb)
    for off in range(1, PAIR_OFF_MAX + 1):
        dg = gam[off:] - gam[:-off]
        sel = dg <= PAIR_BINS[-1]
        if not sel.any():
            break
        wpair = np.real(zph[off:] * np.conj(zph[:-off]))
        wnorm = A2D[off:] * A2D[:-off]
        bi = np.searchsorted(PAIR_BINS, dg[sel], side="right") - 1
        np.add.at(num, bi, wpair[sel])
        np.add.at(den, bi, wnorm[sel])
    pair_c = num / np.maximum(den, 1e-300)
    print("    pair coherence <cos 2(psi_i - psi_j)> by |dgamma| "
          "(M = 1632, weights A^2 A^2):")
    for i in range(nb):
        print("      [%6.2f, %6.2f): %+.4f   (pairs wgt %.2e)"
              % (PAIR_BINS[i], PAIR_BINS[i + 1], pair_c[i], den[i]))
    print("    scales: Montgomery 2pi/log(gamma/2pi) ~ 0.8-1.6; "
          "alias period 2pi/D = %.0f -- the range typing above "
          "decides banded vs long-range" % (2.0 * math.pi / DGRID))

    # ============================================================== S4
    print("\nS4 -- the three-candidate identification (old ladder, "
          "exact Guinand split)")
    from mpmath import mp, zeta as _zeta, diff as _diff
    mp.dps = 30
    c_th = float(-2 * _diff(lambda s: _zeta(s), 0.5) / _zeta(0.5))
    u0 = 2.0 * math.log(-c_th / 4.0)
    old = [w for w in rows if not w["deep"]]
    res_id, sh_fluc, sh_smooth, scales, q_pnt = [], [], [], [], []
    t0 = time.time()
    for w in old:
        rr = w["rr"]
        fr = w["fr"]
        p1, p2 = fr["p1"], fr["p2"]
        P_cf = np.array([[p1 * p1, p1 * p2], [p1 * p2, p2 * p2]])
        G_id = rr["Ah"] - P_cf
        sc_id, ss_id, s2_id = aniso(G_id, p1, p2)
        edges, reads = fd.pnt_cells(rr["W11"], rr["W22"],
                                    rr["W12"], rr["D"], rr["M"],
                                    2.0 * rr["alpha"] + 1e-9, u0)
        Sp = fd.pnt_S_of(edges, reads, 2.0 * rr["alpha"])
        G_sm = rr["B"] - Sp - P_cf
        sc_sm, _, s2_sm = aniso(G_sm, p1, p2)
        G_fl = Sp - rr["S"]
        sc_fl, _, _ = aniso(G_fl, p1, p2)
        res_id.append(abs(sc_id / fr["Sc"] - 1.0))
        sh_fluc.append(sc_fl / sc_id)
        sh_smooth.append(sc_sm / sc_id)
        q_pnt.append(sc_sm / s2_sm)
        # the Poisson-comb square-root scale of the fluctuation
        e = np.array([p1, p2]) / math.hypot(p1, p2)
        f = np.array([p2, -p1]) / math.hypot(p1, p2)
        Xn = rr["Xn"]
        an = ((e[0] ** 2 - f[0] ** 2) * Xn[:, 0]
              + (e[1] ** 2 - f[1] ** 2) * Xn[:, 1]
              + 2.0 * (e[0] * e[1] - f[0] * f[1]) * Xn[:, 2])
        sig = math.sqrt(float(np.sum((rr["lam"] * an) ** 2)))
        scales.append(abs(sc_fl) / max(sig, 1e-300))
        w.update(sc_id=sc_id, sc_sm=sc_sm, sc_fl=sc_fl, sig=sig)
    print("    identification pass on %d old frames in %.0f s"
          % (len(old), time.time() - t0))
    med_res = float(np.median(res_id))
    check("S4.IDRES the Guinand identity route Sc_id = "
          "aniso(Ah - P) reproduces the zero-side Sc_true: median "
          "rel residue %.3f <= %.2f (T > 2e4 tail + quadrature; "
          "soft bar %.2f %s)"
          % (med_res, IDRES_GATE, IDRES_SOFT,
             "met" if med_res <= IDRES_SOFT else "MISSED (typed)"),
          med_res <= IDRES_GATE)
    med_fl = float(np.median(sh_fluc))
    med_sm = float(np.median(sh_smooth))
    med_scale = float(np.median(scales))
    print("    THE EXACT SPLIT (Sc_id = Sc_smooth + Sc_fluc, "
          "per-frame medians):")
    print("      smooth (B - Sp - P) share : %+.3f   (q_pnt median "
          "%+.4f vs q_true median %.4f)"
          % (med_sm, float(np.median(q_pnt)),
             float(np.median([w['q'] for w in old]))))
    print("      prime fluctuation (Sp - S): %+.3f" % med_fl)
    print("      fluctuation vs Poisson-comb sqrt scale: median "
          "|Sc_fluc|/sigma_sqrt = %.2f (bar %.1f: %s)"
          % (med_scale, SCALE_BAR,
             "systematic one-point" if med_scale > SCALE_BAR
             else "SQRT-CANCELLATION REGIME"))
    # zero-side smooth surrogate across all 73 (GEOM candidate)
    geo_res = []
    for w in rows:
        fv = pole_frame(w["h"], w["D"], g_rvm)
        w["Sc_rvm"] = fv["Sc"]
        geo_res.append(abs(fv["Sc"] / w["Sc"] - 1.0))
    med_geo = float(np.median(geo_res))
    geom_ok = (med_geo <= GEOM_MED
               and abs(sl_1mq_rvm - sl_1mq) <= GEOM_SLOPE)
    check("S4.GEOM [EXPECTED FAIL] the smooth-surrogate candidate: "
          "median_73 |Sc_rvm/Sc_true - 1| = %.3f (bar %.2f) and "
          "tower deficit-slope dev |%+.3f - %+.3f| = %.3f (bar "
          "%.2f) -- %s"
          % (med_geo, GEOM_MED, sl_1mq_rvm, sl_1mq,
             abs(sl_1mq_rvm - sl_1mq), GEOM_SLOPE,
             "deterministic geometry carries it" if geom_ok
             else "smooth geometry does NOT carry it"),
          geom_ok)
    # controls: comb scramble + Epstein at 3 predeclared frames
    print("    comb-side controls at frames %s:" % (CTRL_FRAMES,))
    for ci in CTRL_FRAMES:
        w = old[ci]
        rr = w["rr"]
        rs = core.build_window(rr["k"], scramble_seed=SEED)
        p1, p2 = w["fr"]["p1"], w["fr"]["p2"]
        P_cf = np.array([[p1 * p1, p1 * p2], [p1 * p2, p2 * p2]])
        sc_scr, _, _ = aniso(rs["Ah"] - P_cf, p1, p2)
        nmax = int(math.exp(2.0 * rr["alpha"]))
        cntE = epstein_counts(nmax)
        nnE = np.nonzero(cntE[2:])[0].astype(np.int64) + 2
        uuE = np.log(nnE.astype(float))
        mE = cntE[nnE].astype(float) / np.sqrt(nnE.astype(float))
        kap = float(np.sum(2.0 * rr["lam"])) / float(np.sum(mE))
        lamE = 0.5 * kap * mE
        XnE = np.empty((len(nnE), 3))
        for i in range(len(nnE)):
            XnE[i, 0] = core.spline_project(rr["W11"], uuE[i],
                                            rr["D"], rr["M"])
            XnE[i, 1] = core.spline_project(rr["W22"], uuE[i],
                                            rr["D"], rr["M"])
            XnE[i, 2] = core.spline_project(rr["W12"], uuE[i],
                                            rr["D"], rr["M"])
        SE = np.array([[float(lamE @ XnE[:, 0]),
                        float(lamE @ XnE[:, 2])],
                       [float(lamE @ XnE[:, 2]),
                        float(lamE @ XnE[:, 1])]])
        sc_ep, _, _ = aniso(rr["B"] - SE - P_cf, p1, p2)
        print("      h = %4d (alpha %.2f): Sc_true %+.3e | scramble "
              "%+.3e (x%+.2f) | Epstein %+.3e (x%+.2f) -- the "
              "fingerprint is comb-specific"
              % (w["h"], w["alpha"], w["Sc"], sc_scr,
                 sc_scr / w["Sc"], sc_ep, sc_ep / w["Sc"]))

    # ============================================================== S5
    print("\nS5 -- sketch or boundary")
    arith_lvl = med_fl >= ARITH_SHARE
    if geom_ok:
        verdict = "ALIAS-CORRELATION-GEOMETRIC"
    elif arith_lvl and med_scale > SCALE_BAR:
        verdict = "ALIAS-CORRELATION-ARITHMETIC"
    elif arith_lvl:
        verdict = "ALIAS-CORRELATION-PAIRCORR"
    else:
        verdict = "ALIAS-MIXED"
    if verdict == "ALIAS-CORRELATION-PAIRCORR":
        print("""
    *** THE FLOOR <-> PAIR-CORRELATION BRIDGE (typed boundary) ***
    The correlation term Sc is carried by the prime-comb
    fluctuation Sp - S sitting AT the Poisson-comb square-root
    scale: the suppression exists because the comb fluctuations
    cancel EXACTLY as far as square-root cancellation allows --
    variance-type control.  Proving the tower tau-law therefore
    requires bounding an oscillatory prime sum at its sqrt scale =
    pair-correlation-equivalent substance (Montgomery-type input on
    the zero side by the explicit formula).  This is the typed
    circularity boundary, NOT a result: the envelope's constant is
    pair-correlation-equivalent arithmetic substance -- the named
    contract PRIME.FLOOR.PAIRCORR.01.""")
    else:
        print("    verdict %s (unexpected -- pattern gate will "
              "refuse)" % verdict)

    # ============================================================== C
    print("\nC -- controls (summary)")
    check("C1 [EXPECTED FAIL -- restates W2D] Poissonized zeros "
          "collapse q and restore the RP law (W2D above)",
          "W2D" not in FAILS)
    check("C2 [EXPECTED FAIL -- restates W2C] phase scramble "
          "restores the diagonal (W2C above)",
          "W2C" not in FAILS)
    print("    C3 comb scramble + Epstein fingerprints typed in S4 "
          "(comb-specific, measured).")

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    print("    the split: smooth share %+.3f | fluctuation share "
          "%+.3f | scale ratio %.2f | geom residue %.3f | deficit "
          "law (1-q) ~ h^%+.2f"
          % (med_sm, med_fl, med_scale, med_geo, sl_1mq))
    print("    THE TYPED CIRCULARITY BOUNDARY: by Guinand the "
          "comb's self-cancellation at the\n    sqrt scale IS the "
          "zero-side floor statement itself -- the analytic-"
          "envelope\n    route is CLOSED at this boundary (no "
          "further variants; stop-list entry).")
    dt = time.time() - T0
    print("-" * 78)
    got_fails = sorted(set(FAILS))
    exp_fails = sorted(set(EXPECTED_FAILS))
    pattern_ok = (got_fails == exp_fails
                  and verdict == EXPECTED_VERDICT)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; the pair-correlation boundary is a typed "
          "boundary -- not a theorem.")
    print("[%s] PATTERN GATE: expected verdict %s with exactly the "
          "SEVEN preregistered-honest premise-overturning FAILs %s "
          "(got %s: %s)"
          % ("PASS" if pattern_ok else "FAIL", EXPECTED_VERDICT,
             ",".join(exp_fails), verdict,
             ",".join(got_fails) if got_fails else "none"))
    return 0 if pattern_ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
