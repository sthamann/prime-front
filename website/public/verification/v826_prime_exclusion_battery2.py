#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v826 -- PRIME.EXCLUSION.BATTERY2.01: the preregistered battery v2 and the measurement-range extension -- the exclusion floor of the certified ladder drops from Xi ~ 0.2187 to the uncensored declining Xi_v2 (deepest 0.0816, slope -1.39): the v825 saturation is INSTRUMENT-RELATIVE, not tower-intrinsic, ONE module from two probes (16/16 + 13/13 checks; discovery probes exclusion_battery_v2_probe.py FLOOR-LOWERED and exclusion_range_extension_probe.py RANGE-DECIDES-DECLINE, 2026-08-06, re-run identically 2026-08-07).  THE PREREGISTRATION DISCIPLINE (the round's methodological core): battery v2 was designed a priori from instrument diagnostics ONLY (the per-gamma stall-band localization gamma ~ 18..45 widened to [14, 50]; the growing rank-12 gain fixing the detune axis) and SHA-256-hashed BEFORE any exclusion evaluation (fd39fb42..., re-hashed here as a ward) -- NO measured delta_mb, no exclusion map, and no zeta-zero datum entered the design; v1 (dg = 0) is a SUBSET of v2, so delta_mb(v2) <= delta_mb(v1) pointwise BY CONSTRUCTION and the decision content is the slope and floor level, not the sign of the gain.  THE DESIGN: columns e^{+-delta jD} {cos, sin}((gamma + dg) jD), QR-orthonormalized; detune ladder dg = k pi/(2X), k in {-1,0,1} out-of-band (rank 12) and dg = k pi/(4X), k in {-4..4} in-band (rank 36); criterion, budget and grids UNCHANGED from the deployed v825 instrument.  FLOOR-LOWERED (frozen deep reference): on the same certified rungs X = 18.375..24.81 the v2 exclusion floor is Xi_v2 = 0.1070 / 0.0986 / 0.0967 / 0.0979 / 0.1034 (old grid) vs v1 0.2736..0.2121 -- a 51-61% cut -- but the two deepest medians sat EXACTLY on the frozen grid floor 1/240: the old-grid v2 floor is only an UPPER bound (grid-censoring caveat, typed).  RANGE-DECIDES-DECLINE (frozen deep reference): the measurement-range extension (21 extra grid points at the SAME frozen ratio, one decade down to 4.02e-4; the old grid an EXACT SUBSET so uncensored boundaries reproduce bit-for-bit; bisection 4) uncensors the series -- Xi_v2 = 0.1066 / 0.0982 / 0.0960 / 0.0913 / 0.0816 declining with log-log slope -1.39 over the deepest three rungs (gate R1 <= -0.3 FIRES, recomputed here): the ladder LIVES on the sharper instrument, and the benchmark delta >= 0.001 is excluded at X* = Xi/delta ~ 81.6 (comb cap e^{81.6} ~ 3e35 -- extrapolation, typed as such).  THE SIDE-FINDING (typed, hash-verified non-circular): the uncensored margin-break boundaries rank-correlate -0.872 with the distance to the nearest true ordinate -- near-ordinate rows have LARGER delta_mb (a real zero makes the injected quadruple redundant) -- the seed of the v827 locator.  This module re-runs the COMPLETE two-instrument comparison live at X = 18.375 (hash wards, v1/v2 reproduction, subset ward bit-for-bit, dominance, witness certificates, all controls) and recomputes the frozen deep gates from the recorded series (downscoping predeclared in PROVENANCE).  Controls fire (synthetic quadruple at 2 delta_mb(v2) breaks the full spectrum; the seed-7 scramble destroys the rung PSD; the Epstein swap destroys PSD).  Feeds PRIME.DETECTOR.WINDOW.01 [O].  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes exclusion_battery_v2_probe.py (2026-08-06,
16/16 checks, ~9 min, FLOOR-LOWERED: preregistered battery v2, hash
fd39fb42.., floor 0.2187 -> <= 0.0979 with the grid-censoring caveat
typed) and exclusion_range_extension_probe.py (2026-08-06, 13/13
checks, ~11 min, RANGE-DECIDES-DECLINE: uncensored Xi_v2 declines at
slope -1.39, benchmark delta >= 0.001 at X* ~ 81.6, zero-distance rank
correlation -0.872); both re-run identically at promotion (2026-08-07,
logs in experiments/tfpt-discovery/*.log).  DOWNSCOPING (predeclared):
the suite module re-runs BOTH instruments (v1 rank-4 and preregistered
v2) live at the certified rung X = 18.375 -- hash wards, v1/v2
reproduction against the cited series (rel 1e-2), the exact-subset
grid ward (bit-for-bit), the pointwise dominance ward, witness-Rayleigh
certificates, and all three controls (machinery imported READ-ONLY
from v825); the deep rungs X = 20.72..24.81 enter as FROZEN REFERENCE
series (both grids) with the decision gates V1/V2/V3 (battery probe
S5) and R1/R2/R3 (range probe S3) RECOMPUTED here from the frozen
numbers.  Original probe docstrings and frozen protocols live in the
two probe files verbatim.

FIREWALL: v563/v755/v825 read-only; NO zetazero()/nzeros() calls in
this module (AST-checked); cached RvM ordinates are NOT read here (the
zero-distance correlation is carried as a frozen typed side-finding;
the live legs are zero-free); RNG only in the declared C2 scramble
(seed 7).  NO RH claim.
"""
import hashlib
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

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = xl.DGRID
GAMMAS_GRID = xl.GAMMAS_GRID
EXT_DELTAS = xl.EXT_DELTAS                     # old grid (44 points)
_RATIO = 120.0 ** (1.0 / 43.0)                 # the frozen grid ratio
EXT2_DELTAS = np.concatenate(
    [EXT_DELTAS[0] * _RATIO ** (-np.arange(21, 0, -1.0)), EXT_DELTAS])
N_BISECT_OLD, N_BISECT_EXT = 3, 4
BAND_LO, BAND_HI = 14.0, 50.0
IDENT_BUD = xl.IDENT_BUD
ANCH_REL = 2.0e-2
REPRO_REL = 1.0e-2                             # live-vs-cited series
SEED_SCRAMBLE = 7

BATTERY_V2_DESIGN = (
    "battery-v2|columns exp(+/-delta*j*D)*{cos,sin}((gamma+dg)*j*D),"
    "full support,QR-orthonormalized|out-band: dg=k*pi/(2*X),"
    "k in {-1,0,1} (rank 12)|in-band gamma in [14.0,50.0]: "
    "dg=k*pi/(4*X),k in {-4..4} (rank 36)|criterion unchanged: "
    "subspace lambda_min(T+-Q) < -(1e-8+100*eps*(||T||+M*max|q|))|"
    "grids unchanged: gamma geomspace(2,190,36), delta "
    "geomspace(1/240,1/2,44)+3-step bisection|D=1/64"
)
V2_HASH_CITED = ("fd39fb42ab1beb8137a359ff9c9934475a2467"
                 "7bf305d111b4fe43a4c6ca02c0")

# FROZEN DEEP REFERENCE (probe runs 2026-08-06/07):
XS = (18.375, 20.71875, 22.09375, 23.484375, 24.8125)
XI_V1_REF = {18.375: 0.2736, 20.71875: 0.2179, 22.09375: 0.2187,
             23.484375: 0.2225, 24.8125: 0.2121}
XI_V2_OLD_REF = {18.375: 0.1070, 20.71875: 0.0986, 22.09375: 0.0967,
                 23.484375: 0.0979, 24.8125: 0.1034}   # grid-censored
XI_V2_UNC_REF = {18.375: 0.1066, 20.71875: 0.0982, 22.09375: 0.0960,
                 23.484375: 0.0913, 24.8125: 0.0816}   # uncensored
V1_FLOOR_REF = 0.2187                # the v825 plateau level
GATE_V2_FRAC = 0.95                  # battery probe gate V2 (frozen)
GATE_SLOPE = -0.3                    # range probe gate R1 (frozen)
SLOPE_REF = -1.39                    # cited uncensored slope
SLOPE_TOL = 0.15
ZDIST_CORR_REF = -0.872              # frozen typed side-finding
BENCH_DELTA = 1.0e-3


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def detunes_v2(M, gamma):
    X = M * DGRID
    if BAND_LO <= gamma <= BAND_HI:
        d = math.pi / (4.0 * X)
        return tuple(k * d for k in range(-4, 5))
    d = math.pi / (2.0 * X)
    return tuple(k * d for k in range(-1, 2))


def boundary_v(cT, M, nrmT, g, detunes, grid, bisect):
    """Margin-break boundary with an explicit detune tuple (the v2
    battery path; v1 = detunes (0.0,)).  Returns (delta, witness)."""
    prev = None
    for dl in grid:
        dl = float(dl)
        ql = xl.quad_lags(M, g, dl)[:M]
        Qb, _ = np.linalg.qr(xl.battery_B(M, g, dl, 1.0, detunes))
        bud = xl.bud_of(M, nrmT, float(np.max(np.abs(ql))))
        lam, wit = xl.sub_lam(cT + ql, Qb)
        if lam < -bud:
            hit, w_hit, lo = dl, wit, prev
            for _ in range(bisect):
                if lo is None:
                    break
                mid = math.sqrt(lo * hit)
                qlm = xl.quad_lags(M, g, mid)[:M]
                Qbm, _ = np.linalg.qr(xl.battery_B(M, g, mid, 1.0,
                                                   detunes))
                bm = xl.bud_of(M, nrmT, float(np.max(np.abs(qlm))))
                lm, wm = xl.sub_lam(cT + qlm, Qbm)
                if lm < -bm:
                    hit, w_hit = mid, wm
                else:
                    lo = mid
            return hit, w_hit
        prev = dl
    return float("nan"), None


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v826 -- PRIME.EXCLUSION.BATTERY2.01: preregistered battery "
          "v2 + range extension")
    print("(two probes: FLOOR-LOWERED + RANGE-DECIDES-DECLINE; live at "
          "X = 18.375, deep")
    print(" rungs frozen reference -- downscoping predeclared in "
          "PROVENANCE; NO RH claim)")
    print("=" * 78)

    # ==================================================== S0: freeze
    print("\nS0 -- the preregistration wards")
    check("S0.AST no zeta-zero generator call in this module",
          xl.ast_zero_firewall(__file__))
    v2h = hashlib.sha256(BATTERY_V2_DESIGN.encode()).hexdigest()
    check("S0.V2HASH the frozen battery-v2 design string re-hashes to "
          "the preregistered SHA-256 %s.. (design a priori, no zero "
          "datum, typed information flow)" % V2_HASH_CITED[:16],
          v2h == V2_HASH_CITED)
    sub = np.abs(EXT2_DELTAS[21:] - EXT_DELTAS)
    check("S0.GRID the extended grid contains the old 44-point grid "
          "as an EXACT SUBSET (21 points prepended at the frozen "
          "ratio r = 120^(1/43); new floor %.4e; max embed dev %.1e)"
          % (EXT2_DELTAS[0], float(np.max(sub))),
          float(np.max(sub)) == 0.0
          and abs(EXT2_DELTAS[0] - 4.0214e-4) < 1e-7)

    # ==================================================== S1: live rung
    print("\nS1 -- the live rung X = 18.375 (tower + anchors)")
    cs, cnt, masses_scr, ncap = xl.seg_assemble([1176],
                                                collect_mass_M=1176)
    tower = srp.continuum_lags(1176) + cs[1176]
    cT = tower[:1176]
    T = sla.toeplitz(cT)
    m_of = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
    nrmT = float(sla.norm(T, 2))
    rel = abs(m_of - 3.8825e-6) / 3.8825e-6
    lb, _, _ = xl.chol_cert_lower(T, m_of)
    check("S1.ANCH rung M = 1176 (X = 18.375, %d atoms): lambda_min "
          "= %.4e vs cited 3.8825e-6 (rel %.4f <= %.2f), CERTIFIED "
          ">= %.4e" % (cnt[1176], m_of, rel, ANCH_REL, lb),
          rel <= ANCH_REL and lb is not None and lb > 0.0)

    # ==================================================== S2: v1 vs v2
    print("\nS2 -- both instruments live (36-gamma grid)")
    b_v1o = np.full(len(GAMMAS_GRID), np.nan)
    b_v2o = np.full(len(GAMMAS_GRID), np.nan)
    b_v2u = np.full(len(GAMMAS_GRID), np.nan)
    wit_u = [None] * len(GAMMAS_GRID)
    for ig, g in enumerate(GAMMAS_GRID):
        g = float(g)
        b_v1o[ig], _ = boundary_v(cT, 1176, nrmT, g, (0.0,),
                                  EXT_DELTAS, N_BISECT_OLD)
        det = detunes_v2(1176, g)
        b_v2o[ig], _ = boundary_v(cT, 1176, nrmT, g, det,
                                  EXT_DELTAS, N_BISECT_OLD)
        b_v2u[ig], wit_u[ig] = boundary_v(cT, 1176, nrmT, g, det,
                                          EXT2_DELTAS, N_BISECT_EXT)
    xi_v1 = float(np.median(b_v1o[np.isfinite(b_v1o)])) * 18.375
    xi_v2o = float(np.median(b_v2o[np.isfinite(b_v2o)])) * 18.375
    xi_v2u = float(np.median(b_v2u[np.isfinite(b_v2u)])) * 18.375
    check("S2.V1 the v1 (rank-4) instrument reproduces the cited "
          "series entry: Xi_v1(18.375) = %.4f vs %.4f (rel %.4f <= "
          "%.0e)" % (xi_v1, XI_V1_REF[18.375],
                     abs(xi_v1 / XI_V1_REF[18.375] - 1.0), REPRO_REL),
          abs(xi_v1 / XI_V1_REF[18.375] - 1.0) <= REPRO_REL)
    check("S2.V2 the preregistered v2 instrument reproduces both "
          "cited entries: old grid Xi = %.4f vs %.4f, uncensored Xi "
          "= %.4f vs %.4f (rel <= %.0e)"
          % (xi_v2o, XI_V2_OLD_REF[18.375], xi_v2u,
             XI_V2_UNC_REF[18.375], REPRO_REL),
          abs(xi_v2o / XI_V2_OLD_REF[18.375] - 1.0) <= REPRO_REL
          and abs(xi_v2u / XI_V2_UNC_REF[18.375] - 1.0) <= REPRO_REL)
    dom = np.all(b_v2o[np.isfinite(b_v1o) & np.isfinite(b_v2o)]
                 <= b_v1o[np.isfinite(b_v1o) & np.isfinite(b_v2o)]
                 * (1.0 + 1e-12))
    check("S2.DOM v2 boundary <= v1 boundary pointwise (subset "
          "construction verified on the data, %d/%d rows finite)"
          % (int(np.isfinite(b_v2o).sum()), len(GAMMAS_GRID)),
          bool(dom))
    unc = np.isfinite(b_v2o) & (b_v2o > EXT_DELTAS[0] * (1 + 1e-9))
    sub_ok = np.allclose(b_v2o[unc], b_v2u[unc], rtol=0.15, atol=0.0)
    # bit-for-bit only holds at equal bisection depth: re-scan at 3
    b_v2u3 = np.full(len(GAMMAS_GRID), np.nan)
    for ig, g in enumerate(GAMMAS_GRID):
        b_v2u3[ig], _ = boundary_v(cT, 1176, nrmT, float(g),
                                   detunes_v2(1176, float(g)),
                                   EXT2_DELTAS, N_BISECT_OLD)
    exact = np.array_equal(b_v2o[unc], b_v2u3[unc])
    check("S2.SUBSET rows uncensored on the old grid reproduce "
          "EXACTLY on the extended grid at equal bisection depth "
          "(%d rows, bit-for-bit: %s; the deeper 4-step bisection "
          "only refines downward, max rel move %.3f)"
          % (int(unc.sum()), exact,
             float(np.max(np.abs(b_v2u[unc] / b_v2o[unc] - 1.0)))),
          exact and sub_ok)
    n_cert, n_ok = 0, 0
    for ig in (3, 10, 17, 24, 30, 35):
        b = b_v2u[ig]
        if not np.isfinite(b) or wit_u[ig] is None:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = xl.quad_lags(1176, g, float(b))[:1176]
        bud = xl.bud_of(1176, nrmT, float(np.max(np.abs(ql))))
        ok1, _ = xl.certified_break(cT + ql, 1176, wit_u[ig], bud)
        n_cert += 1
        n_ok += int(ok1)
    check("S2.CERT witness-Rayleigh certificates re-prove %d/%d "
          "sampled uncensored v2 boundary points" % (n_ok, n_cert),
          n_cert >= 5 and n_ok == n_cert)

    # ==================================================== S3: controls
    print("\nS3 -- controls (live)")
    inside_ok, n_in = True, 0
    for ig in (6, 14, 22, 30):
        b = b_v2u[ig]
        if not np.isfinite(b) or 2.0 * b > 0.5:
            continue
        g = float(GAMMAS_GRID[ig])
        ql = xl.quad_lags(1176, g, 2.0 * float(b))[:1176]
        bud = xl.bud_of(1176, nrmT, float(np.max(np.abs(ql))))
        lam = xl.full_min(cT + ql, 1176)
        n_in += 1
        inside_ok = inside_ok and (lam < -bud)
    check("S3.C1a [must-fire] synthetic quadruple at 2 delta_mb(v2) "
          "inside the region breaks the FULL spectrum: %d/%d points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 3)
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    xl.tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    lam_scr = xl.full_min(srp.continuum_lags(1176) + c_scr, 1176)
    check("S3.C2 [must-fire] scramble at M = 1176 (SAME %d masses, "
          "seed %d; battery-independent tower control): lambda_min = "
          "%.3e < 0" % (masses_scr.size, SEED_SCRAMBLE, lam_scr),
          lam_scr < 0.0)
    r1 = xl.lattice_r1(xl.EPSTEIN_CAP)
    lamE = xl.dirichlet_vonmangoldt(np.asarray(r1, float) / 2.0,
                                    xl.EPSTEIN_CAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    cE, _ = core.atom_lags_at(0.5 * 640 * DGRID, 640,
                              np.log(supp.astype(float)),
                              2.0 * lamE[supp]
                              / np.sqrt(supp.astype(float)))
    lam_ep = xl.full_min(srp.continuum_lags(640) + cE, 640)
    check("S3.C3 [must-fire] Epstein swap (reach %d => M = 640, "
          "typed): lambda_min = %.3e < 0" % (xl.EPSTEIN_CAP, lam_ep),
          lam_ep < 0.0)

    # ================================ R: frozen deep gates (recomputed)
    print("\nR -- THE TWO-INSTRUMENT LADDER (frozen deep reference; "
          "gates recomputed)")
    print("  %10s | %9s %9s %9s" % ("X", "Xi(v1)", "Xi(v2,old)",
                                    "Xi(v2,unc)"))
    for X in XS:
        print("  %10.4f | %9.4f %9.4f %9.4f"
              % (X, XI_V1_REF[X], XI_V2_OLD_REF[X], XI_V2_UNC_REF[X]))
    floor_v2 = float(np.median([XI_V2_OLD_REF[X] for X in XS[-3:]]))
    check("R1.V2GATE the battery decision (probe S5, recomputed): "
          "floor_v2 = median over the deepest three rungs = %.4f < "
          "%.2f x %.4f = %.4f => FLOOR-LOWERED (-55%%); the old-grid "
          "floor is an UPPER bound only -- the two deepest medians "
          "sat on the grid floor 1/240 (censoring caveat, typed)"
          % (floor_v2, GATE_V2_FRAC, V1_FLOOR_REF,
             GATE_V2_FRAC * V1_FLOOR_REF),
          floor_v2 < GATE_V2_FRAC * V1_FLOOR_REF)
    lx = np.log(XS[-3:])
    ly = np.log([XI_V2_UNC_REF[X] for X in XS[-3:]])
    slope3 = float(np.polyfit(lx, ly, 1)[0])
    check("R2.R1GATE the range decision (probe S3, recomputed): "
          "log-log slope of the UNCENSORED Xi_v2 over the deepest "
          "three rungs = %.2f <= %.2f (cited %.2f, |dev| <= %.2f) => "
          "RANGE-DECIDES-DECLINE -- the v825 plateau was the "
          "instrument, not the tower"
          % (slope3, GATE_SLOPE, SLOPE_REF, SLOPE_TOL),
          slope3 <= GATE_SLOPE
          and abs(slope3 - SLOPE_REF) <= SLOPE_TOL)
    xstar = XI_V2_UNC_REF[24.8125] / BENCH_DELTA
    print("    depth-to-width benchmark (uncensored deepest "
          "calibration): delta >= %.0e excluded at X* = Xi/delta = "
          "%.1f (comb cap e^{X*} ~ %.1e -- EXTRAPOLATION, typed)"
          % (BENCH_DELTA, xstar, math.exp(xstar)))
    check("R3.BENCH the benchmark arithmetic reproduces the cited "
          "X* ~ 81.6 (got %.1f)" % xstar, abs(xstar - 81.6) <= 1.0)
    print("    SIDE-FINDING (frozen, typed): the uncensored "
          "boundaries rank-correlate %.3f with the distance to the "
          "nearest true ordinate (hash-verified non-circular -- the "
          "design string contains no zero datum; any "
          "zero-correlation in the floor is measured OUTPUT, not "
          "design input) -- the seed of the v827 locator."
          % ZDIST_CORR_REF)

    # ============================================================== V
    print("\n" + "=" * 78)
    verdicts_ok = (floor_v2 < GATE_V2_FRAC * V1_FLOOR_REF
                   and slope3 <= GATE_SLOPE)
    print("V -- verdict pair (recomputed): %s + %s"
          % ("FLOOR-LOWERED" if floor_v2 < GATE_V2_FRAC * V1_FLOOR_REF
             else "?!",
             "RANGE-DECIDES-DECLINE" if slope3 <= GATE_SLOPE
             else "?!"))
    print("=" * 78)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = not FAILS and verdicts_ok
    print("[%s] PATTERN GATE: expected all checks green with the "
          "verdict pair FLOOR-LOWERED + RANGE-DECIDES-DECLINE"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
