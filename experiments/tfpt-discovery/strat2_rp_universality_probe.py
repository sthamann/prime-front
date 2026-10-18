#!/usr/bin/env python3
"""strat2_rp_universality_probe.py -- STRATEGY-COUNCIL SLICES (2026-08-03,
second round): three cheap decisive measurements for the LAST WALL
(L1 vague-limit identification / K1b node super-resolution), each the
FIRST machine slice of a strategy candidate that is NOT covered by the
two running workers (K1b symmetry perturbation, L1 moment determinacy).

A [RP -- functional-equation symmetry as positivity source]
   Question: is the parity/KMS structure of the glued object (E3.2b:
   detailed balance M(-u) = e^{-u} M(u), KMS beta = 1) an
   Osterwalder-Schrader REFLECTION positivity source?  OS positivity
   would be a NEW positivity axis (Hankel in the lag variable u,
   test functions supported on u > 0, reflection u -> -u), distinct
   from the deployed Toeplitz/Levinson positivity (Bochner axis).
   Measurement: Hankel readings H_ij = v[(i+j)] of the SAME deployed
   lag vectors, plain and KMS-twisted (v[d] e^{dD/2}), per sector
   (pole cp / arch car / atoms cat / total p).  Expectations from
   closed forms: pole is Hankel-PSD (2cosh((i+j)D/2) = two rank-1
   squares), arch is Hankel-NSD (car_d = -D rho(dD), rho completely
   monotone => Hankel-PSD with the sign flipped) -- so the TOTAL
   should fail plain RP at the UV corner unless cancellation helps.
   Either outcome is decisive for the strategy family "FE symmetry
   as positivity source": if RP fails on truncations, the OS route
   is dead at measurement level (honest kill); if a twisted reading
   survives with stable margin, a new structure exists.

B [UNIV -- universality transfer, the Freud-Levin-Lubinsky route]
   Question: does the measured GUE statistic of E4 come with genuine
   CD-KERNEL universality (bulk sine kernel), which by
   Freud-Levin-Lubinsky (Levin-Lubinsky JAT 2008; Avila-Last-Simon
   APDE 2010; Lubinsky Ann. Math. 2009) implies CLOCK spacing --
   i.e. node rigidity at o(spacing), a THEOREM-grade classical
   mechanism for the K1b super-resolution?  Measurement: the
   correlation-normalized Christoffel-Darboux kernel
   corr(a, b) = K(x_a, x_b)/sqrt(K(x_a,x_a) K(x_b,x_b)) at a GAP
   point and at a PEAK point of the Fejer symbol (both zeta-free),
   in local node-spacing units, against sinc(a - b); fixed measure
   (largest window), K-ladder.  Expected fork: sinc at gap points
   (bulk universality => clock => rigidity), NOT sinc at peak points
   (emergent atoms live in a different (pinning) class -- section C).

C [PIN -- mass-point pinning lab, the classical super-resolution
   mechanism candidate]
   Question: is the ~900x sub-classical node precision of K1b simply
   the classical PINNING of a Gauss node by an (emergent) mass point
   -- a rank-one attractor, not a capture-lemma effect?  Lab: smooth
   background (arch + pole closed lags + minimal PD floor) plus ONE
   Fejer-smoothed positive peak at tau* (mass m, Fejer order W ==
   peak width ~ 2 pi/(W D)); ladder in K (truncation) x W (sharpness)
   x m (mass): |nearest node - tau*| vs local spacing.  If the
   spacing/error ratio reaches the measured super-resolution scale
   (~10^2..10^3) at window-realistic (W, m), the mechanism is
   classical OP theory (zeros near a mass point), and the K1b
   theorem target becomes: peaks of the window symbol ARE emergent
   mass points with quantified sharpness (v669 identity route).

RESULTS (run 2026-08-03, 5/5 PASS, 2 s):
  A: sector anatomy EXACT -- pole Hankel-PSD (mineig/scale >= -8.5e-12,
     two rank-1 squares), arch Hankel-NSD (complete monotonicity of
     rho, negative coupling); TOTAL fails plain AND KMS-twisted RP at
     full scale (mineig/scale = -1.0 on both h = 606 and h = 1433):
     RP-DEAD-ON-TRUNCATIONS.  The naive OS/reflection route is dead at
     measurement level; the deployed positivity lives ONLY on the
     Toeplitz/Bochner axis.  Symmetry-sourced positivity survives only
     in the atom-free support regime (|u| < log 2: the Connes-Consani
     2021 territory) -- the FE symmetry buys exactly that, no more.
  B: gap point tau = 63.955: sinc shape deviation HALVES along the
     K-ladder (0.304 at K = 716 -> 0.150 at K = 1433, local scale fit
     c = 0.95): UNIV-BULK-EMERGING (Freud-Levin-Lubinsky route live).
     Peak point tau = 60.828: deviation 1.04 with the scale fit pegged
     at the boundary -- peaks are NOT in the bulk class.  The two-layer
     picture (rigid quadrature gap layer vs emergent-atom peak layer)
     is now measured at kernel-shape level.
  C: ONE inserted Fejer-smoothed peak at the known gap point of the
     real h = 1433 measure: best node error at K = 1433 is 2.39e-3
     (m = 0.25x real peak mass, W = 716), K-rates -2.5 .. -4.1 (E4
     pure-GNS ladder ~ -3.5), spacing/error up to 211x -- INSIDE the
     measured real-zero range (3e-4 .. 3e-2): PIN-MECHANISM-SUPPORTED.
     Classical mass-point pinning reproduces the super-resolution
     scale AND the superconvergent rate; the remaining ~x10 to the
     first-20-zero precision (3e-4) is the open coherence/sharpness
     question (next slice: coherent peak COMB insertion).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no marker, NO RH claim.
Zeros are never loaded (no comparison targets needed: all three
sections are zeta-free constructions; peaks come from the symbol).
Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/strat2_rp_universality_probe.py
"""

import ast
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402
import moonshot_arch_glue_probe as stage2  # noqa: E402
import moonshot_spectral_probe as e4  # noqa: E402
import z1_jacobi_probe as jac  # noqa: E402

T0 = time.time()
CHECKS = []

BANNED_IDS = ("zetazero", "nzeros", "second_sheet_zero", "isprime",
              "primerange", "nextprime", "primepi", "sympy")

N_HANKEL = 220               # Hankel block size (i, j = 1..N)
BAND_LO = 10.0               # band lower edge (above pole band)
A_GRID = np.arange(-3.0, 3.0 + 1e-9, 0.25)   # sinc comparison grid
PIN_W_LADDER = (256, 716, 1433, 2866)        # Fejer sharpness ladder
PIN_K_LADDER = (358, 716, 1433)              # truncation ladder
PIN_M_RUNGS = (0.25, 1.0, 4.0)   # peak mass in units of real peak mass

BAR_PSD = 1.0e-10            # relative PSD tolerance (sector theory)
BAR_GAUSS = 1.0e-8           # Wheeler moment reconstruction


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def finding(msg):
    print("  FINDING: %s" % msg)


# ------------------------------------------------------------ G0 firewall
def g0():
    print("\nG0 -- firewall")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    attrs = {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    hits = sorted((names | attrs) & set(BANNED_IDS))
    check("G0.1 no zero/prime identifiers in this file", not hits,
          "hits=%s" % hits)


# ------------------------------------------------------- A: RP / Hankel
def hankel_eigs(v, D, n, twist):
    d = np.arange(2, 2 * n + 1)
    row = np.asarray(v)[d].astype(float)
    if twist:
        row = row * np.exp(0.5 * D * d)
    H = sla.hankel(row[:n], row[n - 1:])
    ev = np.linalg.eigvalsh(H)
    return float(ev[0]), float(ev[-1])


def section_a(wins):
    print("\nA -- reflection positivity (Hankel readings of the lags)")
    picks = [wins[len(wins) // 2], wins[-1]]
    pole_psd_ok, arch_nsd_ok = True, True
    for w in picks:
        M, D = w["M"], w["D"]
        n = min(N_HANKEL, (M - 1) // 2)
        print("  window kz=%d  h=%d  D=%.5f  (Hankel N=%d)"
              % (w["kz"], M // 2, D, n))
        for name, vec in (("pole cp", w["cp"]), ("arch car", w["car"]),
                          ("atoms cat", w["cat"]), ("TOTAL p", w["p"])):
            lo_p, hi_p = hankel_eigs(vec, D, n, twist=False)
            lo_t, hi_t = hankel_eigs(vec, D, n, twist=True)
            sc_p = max(abs(lo_p), abs(hi_p))
            sc_t = max(abs(lo_t), abs(hi_t))
            print("    %-9s  plain: mineig/scale %+.3e  "
                  "kms-twist: mineig/scale %+.3e"
                  % (name, lo_p / sc_p, lo_t / sc_t))
            if name == "pole cp":
                pole_psd_ok &= (lo_p >= -BAR_PSD * sc_p)
            if name == "arch car":
                arch_nsd_ok &= (hi_p <= BAR_PSD * sc_p)
    check("A.1 pole sector Hankel-PSD (two rank-1 squares)", pole_psd_ok)
    check("A.2 arch sector Hankel-NSD (complete monotonicity, "
          "negative coupling)", arch_nsd_ok)
    w = wins[-1]
    n = min(N_HANKEL, (w["M"] - 1) // 2)
    lo_p, hi_p = hankel_eigs(w["p"], w["D"], n, twist=False)
    lo_t, hi_t = hankel_eigs(w["p"], w["D"], n, twist=True)
    rp_plain = lo_p >= -BAR_PSD * max(abs(lo_p), abs(hi_p))
    rp_twist = lo_t >= -BAR_PSD * max(abs(lo_t), abs(hi_t))
    finding("plain OS/RP on the deployed measure: %s (mineig/scale %+.3e)"
            % ("HOLDS" if rp_plain else "FAILS",
               lo_p / max(abs(lo_p), abs(hi_p))))
    finding("KMS-twisted OS/RP: %s (mineig/scale %+.3e)"
            % ("HOLDS" if rp_twist else "FAILS",
               lo_t / max(abs(lo_t), abs(hi_t))))
    verdict = ("RP-NEW-STRUCTURE" if (rp_plain or rp_twist)
               else "RP-DEAD-ON-TRUNCATIONS")
    print("  A verdict: %s" % verdict)
    return verdict


# ------------------------------------------- B: CD-kernel universality
def orthonormal_eval(aM, gM, K, xs):
    xs = np.asarray(xs, float)
    pkm1 = np.zeros_like(xs)
    pk = np.full_like(xs, 1.0 / math.sqrt(gM[0]))
    vals = [pk.copy()]
    for k in range(K - 1):
        pk1 = ((xs - aM[k]) * pk - (math.sqrt(gM[k]) * pkm1
                                    if k > 0 else 0.0))
        pk1 = pk1 / math.sqrt(gM[k + 1])
        pkm1, pk = pk, pk1
        vals.append(pk.copy())
    return np.array(vals)


def cd_corr_profile(aM, gM, K, D, tau0, s_loc):
    """Correlation-normalized CD kernel on the local spacing grid;
    scale-fitted sinc comparison (the local unit is only known up to
    O(1), the SHAPE is the universality statement)."""
    taus = tau0 + A_GRID * s_loc
    xs = 2.0 * np.cos(taus * D)
    V = orthonormal_eval(aM, gM, K, xs)
    G = V.T @ V
    dg = np.sqrt(np.diag(G))
    corr = G / np.outer(dg, dg)
    i0 = int(np.argmin(np.abs(A_GRID)))
    prof = corr[i0, :]
    best = (np.inf, 1.0)
    for c in np.arange(0.50, 1.51, 0.01):
        dev = float(np.max(np.abs(prof - np.sinc(c * A_GRID))))
        if dev < best[0]:
            best = (dev, float(c))
    return prof, best[0], best[1]


def section_b(wins):
    print("\nB -- CD-kernel universality at gap vs peak points")
    w = wins[-1]
    M, D, p = w["M"], w["D"], w["p"]
    K = M // 2
    aM, gM, kbad = jac.wheeler(p, K)
    ok_pd = kbad is None
    rec = jac.gauss_reconstruct(aM, gM, p[0], min(2 * K, len(p)))
    dev_rec = float(np.max(np.abs(rec - p[:len(rec)]))
                    / np.max(np.abs(p[:len(rec)])))
    check("B.0 Wheeler PD + moment reconstruction",
          ok_pd and dev_rec < BAR_GAUSS, "dev=%.2e" % dev_rec)
    tau, wts, _, _ = e4.gns_nodes(p, K, D)
    sym = jac.symbol_fejer(p, M)
    tgrid = (2.0 * math.pi * np.arange(len(sym))
             / (2.0 * (len(sym) - 1)) / D)
    band = (tgrid > BAND_LO) & (tgrid < 0.9 * math.pi / D)
    pk_idx = jac.top_peaks(tgrid[band], sym[band], 40, sep=2.0)
    peaks = np.sort(tgrid[band][pk_idx])
    mid = peaks[np.argmin(np.abs(peaks - 60.0))]
    nxt = peaks[peaks > mid][0]
    tau_gap = 0.5 * (mid + nxt)
    print("  window h=%d: peak point tau=%.3f, gap point tau=%.3f"
          % (K, mid, tau_gap))
    devs_gap, dev_pk = [], np.inf
    for KK in (K // 2, K):
        aK, gK, kb = jac.wheeler(p, KK)
        if kb is not None:
            continue
        tK, _, _, _ = e4.gns_nodes(p, KK, D)
        nb = tK[(tK > mid - 8) & (tK < mid + 8)]
        s_loc = float(np.median(np.diff(nb)))
        _, dev_gap, c_gap = cd_corr_profile(aK, gK, KK, D, tau_gap, s_loc)
        _, dev_pk, c_pk = cd_corr_profile(aK, gK, KK, D, mid, s_loc)
        devs_gap.append(dev_gap)
        print("    K=%4d  s_loc %.4f  shape dev vs sinc: "
              "gap %.4f (c=%.2f)   peak %.4f (c=%.2f)"
              % (KK, s_loc, dev_gap, c_gap, dev_pk, c_pk))
    dev_gap = devs_gap[-1]
    univ_meas = dev_gap < 0.10
    univ_trend = (len(devs_gap) >= 2 and dev_gap < 0.20
                  and dev_gap < 0.7 * devs_gap[0])
    finding("bulk (gap) point: sinc shape deviation %.4f (K-trend %s)"
            % (dev_gap, " -> ".join("%.3f" % d for d in devs_gap)))
    finding("peak point: sinc shape deviation %.4f -> %s"
            % (dev_pk, "same class as bulk" if dev_pk < 0.10
               else "DIFFERENT class (pinning candidate)"))
    verdict = ("UNIV-BULK-MEASURED" if univ_meas
               else ("UNIV-BULK-EMERGING" if univ_trend
                     else "UNIV-ABSENT"))
    print("  B verdict: %s" % verdict)
    return verdict, mid, tau_gap


# ------------------------------------------------ C: mass-point pinning
def section_c(wins, tau_ins):
    """Insert ONE synthetic Fejer-smoothed peak at the KNOWN gap point
    tau_ins into the REAL largest-window measure (positive insertion:
    PD is preserved); measure how precisely a Gauss node locks onto it
    as a function of peak mass and sharpness.  The real environment
    supplies the true peak/floor contrast (run-1 lesson: a synthetic
    flat-floor background needs a PD floor of relative size ~1 and has
    no realistic contrast; the insertion design has no floor at all)."""
    print("\nC -- mass-point pinning lab (insertion into the real "
          "window measure)")
    w = wins[-1]
    M, D, p = w["M"], w["D"], w["p"]
    K_full = M // 2
    tau0, wts0, _, _ = e4.gns_nodes(p, K_full, D)
    sym = jac.symbol_fejer(p, M)
    tgrid = (2.0 * math.pi * np.arange(len(sym))
             / (2.0 * (len(sym) - 1)) / D)
    band = (tgrid > BAND_LO) & (tgrid < 0.9 * math.pi / D)
    pk_idx = jac.top_peaks(tgrid[band], sym[band], 200, sep=2.0)
    peaks = np.sort(tgrid[band][pk_idx])
    d_pk = np.min(np.abs(tau0[:, None] - peaks[None, :]), axis=1)
    m_peak = float(np.median(wts0[d_pk < 0.25]))
    nb = tau0[(tau0 > tau_ins - 8) & (tau0 < tau_ins + 8)]
    s_loc0 = float(np.median(np.diff(nb)))
    print("  h=%d  insertion at tau=%.3f  median peak-node mass %.3e  "
          "local spacing %.4f" % (K_full, tau_ins, m_peak, s_loc0))
    check("C.0 real-window baseline valid",
          np.isfinite(m_peak) and m_peak > 0 and s_loc0 > 0)
    d_grid = np.arange(M)
    best_ratio = 0.0
    d_best, rate_best = np.inf, 0.0
    for m_f in PIN_M_RUNGS:
        m = m_f * m_peak
        for W in PIN_W_LADDER:
            if W > M:
                continue
            damp = np.clip(1.0 - d_grid / float(W), 0.0, None)
            pk = m * damp * np.cos(d_grid * D * tau_ins)
            pk[0] = m
            v = p + pk
            row = []
            for K in PIN_K_LADDER:
                tau_n, _, kb, _ = e4.gns_nodes(v, K, D)
                if kb is not None:
                    row.append((K, np.nan, np.nan))
                    continue
                dmin = float(np.min(np.abs(tau_n - tau_ins)))
                nn = tau_n[(tau_n > tau_ins - 8) & (tau_n < tau_ins + 8)]
                s_loc = float(np.median(np.diff(nn)))
                row.append((K, dmin, s_loc / max(dmin, 1e-300)))
            ds = [r[1] for r in row if np.isfinite(r[1])]
            slope = (math.log(ds[-1] / ds[0])
                     / math.log(PIN_K_LADDER[-1] / PIN_K_LADDER[0])
                     if len(ds) == len(PIN_K_LADDER) and ds[0] > 0
                     else float("nan"))
            print("    m=%.2fx W=%4d : " % (m_f, W)
                  + "  ".join("K=%d d=%.2e r=%.0f" % r for r in row)
                  + "   K-rate %+.2f" % slope)
            best_ratio = max(best_ratio,
                             max((r[2] for r in row
                                  if np.isfinite(r[2])), default=0.0))
            if (np.isfinite(row[-1][1]) and row[-1][1] < d_best
                    and math.isfinite(slope)):
                d_best, rate_best = row[-1][1], slope
    finding("best inserted-peak node error at K=1433: %.2e "
            "(measured real-zero range at h=1433: 3e-4 .. 3e-2), "
            "K-rate %+.2f (E4 pure-GNS ladder: ~ -3.5); "
            "max spacing/error %.0fx" % (d_best, rate_best, best_ratio))
    mech_ok = d_best <= 3.0e-2 and rate_best <= -2.0
    verdict = ("PIN-MECHANISM-SUPPORTED" if mech_ok
               else "PIN-INSUFFICIENT")
    print("  C verdict: %s" % verdict)
    return verdict


def run():
    print("=" * 72)
    print("STRAT2 -- strategy slices: RP / universality / pinning")
    print("=" * 72)
    g0()
    wins = e4.family_ext()
    print("\nfamily: %d windows, h = %s"
          % (len(wins), [w["M"] // 2 for w in wins]))
    va = section_a(wins)
    vb, tau_peak, tau_gap = section_b(wins)
    vc = section_c(wins, tau_gap)
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n" + "=" * 72)
    print("CHECKS: %d/%d PASS   verdicts: A=%s  B=%s  C=%s   (%.0f s)"
          % (npass, len(CHECKS), va, vb, vc, time.time() - T0))
    print("=" * 72)


if __name__ == "__main__":
    run()
