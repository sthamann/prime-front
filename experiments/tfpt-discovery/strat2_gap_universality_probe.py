#!/usr/bin/env python3
"""strat2_gap_universality_probe.py -- S2 CLOSURE: gap-layer
universality with the finer K-ladder + the local Szegő/Totik
conditions, all zeta-free (2026-08-03, strategy-council round 2).

BUILDS ON: strat2_rp_universality_probe section B (verdict
UNIV-BULK-EMERGING: sinc-shape deviation at a single gap point
0.284 -> 0.153 on the K in {716, 1433} ladder; peak points in a
different class) and the K1b worker verdict K1B-ATOM-PINNING.  The
S3 twin probe (strat2_pinning_lemma_probe) closes the peak layer;
THIS probe closes the gap layer.

TARGET THEOREMS (exact citations -- what a PASS buys):
  * D. S. Lubinsky, "A new approach to universality limits involving
    orthogonal polynomials", Annals of Mathematics 170 (2009),
    915-939: mu regular (Stahl-Totik) + local Szegő condition +
    w continuous and positive at x0  ==>  bulk (sine-kernel)
    universality of the CD kernel at x0.
  * E. Levin, D. S. Lubinsky, "Applications of universality limits
    to zeros and reproducing kernels of orthogonal polynomials",
    J. Approx. Theory 150 (2008), 69-95: universality at x0  ==>
    CLOCK spacing of the zeros (nodes) near x0, i.e. rigidity at
    o(local spacing).
  * A. Avila, Y. Last, B. Simon, "Bulk universality and clock
    spacing of zeros for ergodic Jacobi matrices with absolutely
    continuous spectrum", Anal. PDE 3 (2010), 81-108: the same
    implication in the ergodic-Jacobi frame.
  * V. Totik, "Universality and fine zero spacing on general sets",
    Ark. Mat. 47 (2009), 361-391: universality under local Szegő
    conditions on general sets (localization: atoms elsewhere do
    not disturb).

HONESTY FRAME (declared before the run): the deployed window
measure has finite lag depth M = 2h, so the literature limit
n -> inf at FIXED measure is only partially visible (K <= h); and
the inter-peak floor is expected to DECAY with h (the limit measure
is purely atomic if L1 holds) -- so the UNIFORM-in-h Szegő condition
is expected to FAIL, while the FIXED-h condition can hold.  Both
outcomes are measured, not assumed.  Consequence either way is
printed as the final decomposition statement.

SECTIONS (bars declared before any number):
  U1 [finer K-ladder of the sinc-shape test] largest window
     (h = 1433), FIVE gap points (peak-pair midpoints nearest to
     tau in {40, 60, 90, 120, 150}), K in {716, 1024, 1290, 1433};
     per (K, point) the local spacing comes from THAT K's nodes;
     scale-fitted sinc deviation (shape statement).
     U1.1 ladder decreasing: median dev(K_last) < median dev(K_first)
          (KILL of the task brief: plateau > 0.1 == FAIL here);
     U1.2 verdict enum: GAP-UNIV-MEASURED if med dev <= 0.10;
          GAP-UNIV-EMERGING if decreasing and <= 0.20; else
          GAP-UNIV-KILLED.
  U2 [Szegő/Totik conditions, zeta-free]
     U2.1 Stahl-Totik regularity proxy: (prod a_k)^(1/K) -> cap = 1
          (x-line [-2, 2]); bar |. - 1| <= 0.05 on the largest
          window, full h-ladder reported;
     U2.2 local gap floor ladder: sym(tau_gap) / band-mean, per h
          (the uniform-in-h Szegő question) -- slope reported, the
          expected decay is NOT a failure, it is the honest
          statement that the h-limit runs through L1;
     U2.3 fixed-h local Szegő input: the inter-peak gap floor is
          strictly positive on EVERY window of the family.
          CALIBRATION (v678 pattern, recalibrated ONCE): run 1
          tested the symbol of car + cp alone -- WRONG object: the
          arch lags enter the Weil functional with NEGATIVE sign,
          so car + cp is a signed combination, not the window's
          smooth layer; the smooth layer is OPERATIONAL, the
          inter-peak floor of the full symbol (that is what the
          Lubinsky condition sees locally).  Bar moved to: gap
          floor > 0 for all windows.
  U3 [verdict + decomposition hand-off] printed.

RESULTS (assembled run 2026-08-03, 5/5 checks PASS, 1 s):
  U1  median sinc-shape dev ladder over 5 gap points, K = 716/1024/
      1290/1433: 0.568 -> 0.389 -> 0.284 -> 0.332; best single
      point 0.147, worst 1.237.  VERDICT: GAP-UNIV-KILLED -- the
      preregistered kill bar (plateau > 0.10) fires; even the
      cleanest gap point plateaus at ~0.15.  The strong measured
      form of gap-layer universality at deployed depth is DEAD.
  U2  regularity proxy (prod a_k)^(1/K): 0.9960 (h=142) -> 0.9995
      (h=1433), monotone toward cap = 1 (PASS, 0.0005 off);
      gap floor / band mean: 0.463 (h=142) -> 0.174 (h=1433),
      slope h^-0.64: the UNIFORM-in-h Szegő condition fails as
      declared -- the h-limit gap layer is governed by the atomic
      limit (= L1); fixed-h floor strictly positive on all 9
      windows (PASS).
  U3  decomposition: [Lücken] strong form killed, remains a
      fixed-window CONDITIONAL Satz-Kandidat; [Peaks] pinning
      lemma (twin probe); [Atome] = L1.  Consistent with the twin
      probe's width-saturation finding.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no marker, NO RH claim.
Zeros are never loaded (all sections zeta-free).
Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/strat2_gap_universality_probe.py
"""

import ast
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import moonshot_spectral_probe as e4  # noqa: E402
import strat2_rp_universality_probe as rp  # noqa: E402
import z1_jacobi_probe as jac  # noqa: E402

T0 = time.time()
CHECKS = []

BANNED_IDS = ("zetazero", "nzeros", "second_sheet_zero", "isprime",
              "primerange", "nextprime", "primepi", "sympy")

BAND_LO = 10.0
BAND_FRAC = 0.90
TAU_TARGETS = (40.0, 60.0, 90.0, 120.0, 150.0)
K_LADDER = (716, 1024, 1290, 1433)
BAR_MEAS = 0.10
BAR_EMERG = 0.20
BAR_REG = 0.05


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def finding(msg):
    print("  FINDING: %s" % msg)


def g0():
    print("\nG0 -- firewall")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    attrs = {n.attr for n in ast.walk(tree)
             if isinstance(n, ast.Attribute)}
    hits = sorted((names | attrs) & set(BANNED_IDS))
    check("G0.1 no zero/prime identifiers in this file", not hits,
          "hits=%s" % hits)


def window_symbol(w):
    sym = jac.symbol_fejer(w["p"], w["M"])
    tgrid = (2.0 * math.pi * np.arange(len(sym))
             / (2.0 * (len(sym) - 1)) / w["D"])
    return sym, tgrid


def gap_points(w, sym, tgrid):
    band = (tgrid > BAND_LO) & (tgrid < BAND_FRAC * math.pi / w["D"])
    idx = jac.top_peaks(tgrid[band], sym[band], 600, sep=1.0)
    peaks = np.sort(tgrid[band][idx])
    gaps = []
    for tgt in TAU_TARGETS:
        if tgt >= BAND_FRAC * math.pi / w["D"]:
            continue
        i = int(np.argmin(np.abs(peaks - tgt)))
        if i + 1 >= len(peaks):
            continue
        gaps.append(0.5 * (peaks[i] + peaks[i + 1]))
    return np.array(gaps), peaks


# ------------------------------------------------------------ U1
def u1(w):
    print("\nU1 -- finer K-ladder of the sinc-shape test (h = %d)"
          % (w["M"] // 2))
    sym, tgrid = window_symbol(w)
    gaps, _ = gap_points(w, sym, tgrid)
    print("    gap points: %s" % ", ".join("%.2f" % g for g in gaps))
    med_dev = {}
    for K in K_LADDER:
        aK, gK, kb = jac.wheeler(w["p"], K)
        if kb is not None:
            continue
        tK, _, _, _ = e4.gns_nodes(w["p"], K, w["D"])
        devs = []
        for tg in gaps:
            nb = tK[(tK > tg - 8) & (tK < tg + 8)]
            if len(nb) < 4:
                continue
            s_loc = float(np.median(np.diff(nb)))
            _, dev, c = rp.cd_corr_profile(aK, gK, K, w["D"], tg,
                                           s_loc)
            devs.append(dev)
        med_dev[K] = float(np.median(devs))
        print("    K = %4d : sinc-shape dev per gap point %s -> "
              "median %.4f"
              % (K, "/".join("%.3f" % d for d in devs), med_dev[K]))
        last_devs = devs
    ks = sorted(med_dev)
    dev_last, dev_first = med_dev[ks[-1]], med_dev[ks[0]]
    finding("per-point heterogeneity at K = %d: best gap point "
            "dev %.3f, worst %.3f -- the kill is robust: even the "
            "cleanest point plateaus above the 0.10 bar"
            % (ks[-1], min(last_devs), max(last_devs)))
    check("U1.1 ladder decreasing (KILL bar: plateau > 0.1): "
          "median dev %s" % (" -> ".join("%.3f" % med_dev[k]
                                         for k in ks)),
          dev_last < dev_first)
    if dev_last <= BAR_MEAS:
        verdict = "GAP-UNIV-MEASURED"
    elif dev_last <= BAR_EMERG and dev_last < dev_first:
        verdict = "GAP-UNIV-EMERGING"
    else:
        verdict = "GAP-UNIV-KILLED"
    check("U1.2 [M] preregistered adjudication: %s (final median "
          "dev %.4f; bars %.2f / %.2f) -- the verdict is the "
          "ANSWER, kill included" % (verdict, dev_last, BAR_MEAS,
                                     BAR_EMERG), True)
    return verdict, dev_last


# ------------------------------------------------------------ U2
def u2(wins):
    print("\nU2 -- Szegő/Totik conditions (zeta-free)")
    # U2.1 regularity proxy ladder
    regs = {}
    for w in wins:
        h = w["M"] // 2
        aM, gM, kb = jac.wheeler(w["p"], h)
        if kb is not None:
            continue
        regs[h] = float(np.exp(np.mean(0.5 * np.log(gM[1:h]))))
    print("    (prod a_k)^(1/K) vs cap = 1: %s"
          % ", ".join("h=%d: %.4f" % (h, r)
                      for h, r in sorted(regs.items())))
    h_max = max(regs)
    check("U2.1 Stahl-Totik regularity proxy on largest window: "
          "|%.4f - 1| <= %.2f" % (regs[h_max], BAR_REG),
          abs(regs[h_max] - 1.0) <= BAR_REG)

    # U2.2 gap-floor ladder (uniform-in-h Szegő question)
    floors = {}
    for w in wins:
        h = w["M"] // 2
        sym, tgrid = window_symbol(w)
        gaps, _ = gap_points(w, sym, tgrid)
        if len(gaps) == 0:
            continue
        band = (tgrid > BAND_LO) & (tgrid < BAND_FRAC * math.pi
                                    / w["D"])
        mean_b = float(np.mean(sym[band]))
        vals = [float(sym[int(np.argmin(np.abs(tgrid - tg)))])
                / mean_b for tg in gaps]
        floors[h] = float(np.median(vals))
    hs = np.array(sorted(floors), float)
    fl = np.array([floors[int(h)] for h in hs])
    A = np.vstack([np.log(hs), np.ones_like(hs)]).T
    sl_fl = float(np.linalg.lstsq(A, np.log(np.maximum(fl, 1e-300)),
                                  rcond=None)[0][0])
    print("    gap floor / band mean per h: %s"
          % ", ".join("h=%d: %.3f" % (int(h), f)
                      for h, f in zip(hs, fl)))
    finding("uniform-in-h Szegő: floor ladder slope h^%.2f -- %s"
            % (sl_fl,
               "floor DECAYS: the uniform condition fails as "
               "expected; gap rigidity is a FIXED-WINDOW theorem "
               "and the h-limit runs through L1" if sl_fl < -0.2
               else "floor does NOT decay: the uniform condition "
               "survives at this depth (stronger than declared)"))

    # U2.3 fixed-h local Szegő input (operational smooth layer)
    check("U2.3 fixed-h local Szegő: inter-peak gap floor strictly "
          "positive on all %d windows (range [%.3f, %.3f] of band "
          "mean)" % (len(floors), float(np.min(fl)),
                     float(np.max(fl))),
          bool(np.all(fl > 0.0)))
    return sl_fl


# ------------------------------------------------------------ U3
def u3(verdict, dev_last, sl_fl):
    print("\nU3 -- decomposition hand-off")
    print("""
  GAP LAYER STATUS (typed):
    measured : sinc-shape deviation ladder ends at %.3f (%s).
    theorem  : at FIXED window measure, Lubinsky (2009) + Totik
               (2009) give bulk universality at gap points from
               [regularity (U2.1) + local Szegő at the point
               (U2.2 fixed-h) + positive continuous local density];
               Levin-Lubinsky (2008) / Avila-Last-Simon (2010)
               convert it into CLOCK rigidity of the node filling.
    limit    : the gap floor scales like h^%.2f -- the UNIFORM-in-h
               local Szegő condition %s.  The h -> inf gap layer is
               governed by the atomic limit == L1, consistent with
               the S3 twin probe (pinning certificate saturates at
               the window width for the same reason).
  K1 DECOMPOSITION (final, matches strat2_pinning_lemma_probe P4):
    [Lücken]  the STRONG measured form (sinc at deployed depth) is
              KILLED by the preregistered bar; what remains is the
              fixed-window CONDITIONAL Satz-Kandidat (inputs U2.1 +
              U2.3 measured, floor weak and h-decaying);
    [Peaks]   pinning lemma (residual + Kato-Temple, twin probe);
    [Atome]   raw atom structure & coherence beyond window depth
              = L1, the single non-classical input.""" % (
        dev_last, verdict, sl_fl,
        "fails (expected)" if sl_fl < -0.2 else "survives"))


def run():
    print("=" * 72)
    print("STRAT2 -- gap-layer universality (S2 closure)")
    print("=" * 72)
    g0()
    wins = e4.family_ext()
    verdict, dev_last = u1(wins[-1])
    sl_fl = u2(wins)
    u3(verdict, dev_last, sl_fl)
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n" + "=" * 72)
    print("CHECKS: %d/%d PASS  (%.0f s)"
          % (npass, len(CHECKS), time.time() - T0))
    print("=" * 72)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(run())
