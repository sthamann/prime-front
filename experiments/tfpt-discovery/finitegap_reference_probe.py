#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""finitegap_reference_probe
PRIME.ONEBADMODE.KS.FINITEGAP.01 -- the finite-gap / isospectral-torus
reference for the CCLIX radius corridor

EXPLORATION ONLY.  NO RH claim.  Finite float64 measurements on the
deployed ladder; nothing here is an all-h statement.

THE QUESTION.  The CCLIX radius gate measured D_h = ||J_h - J_star||_HS
against two references that IGNORE the gap structure of the deployed
measure: the arcsine chain ARC (med D_h ~ 7.5e4) and the ladder-median
MED (med D_h ~ 1.0e3), with C_R = 10.07 and delta_star ~ 0.93.  But the
deployed measure is NOT gapless: the mu_- excluded set occupies
~0.26..0.34 of theta (CCXLV/lattice_rhp_szego reading), so the natural
reference class is the FINITE-GAP one -- the isospectral torus of the
band set, the reference class of the Damanik-Killip-Simon theory
(EXTERNAL-CITED: D. Damanik, R. Killip, B. Simon, "Perturbations of
orthogonal polynomials with periodic recursion coefficients", Annals of
Mathematics 171 (2010) 1931-2010: the KS sum-rule distance is measured
to the isospectral torus of the essential spectrum, NOT to the free
chain).  Does a source-only finite-gap J_star matched to the deployed
band set drastically shrink D_h and clean the corridor numbers?

MISSIONS.

A  BAND ANATOMY (mission a).  Per frame-A measure rung kz: the source
   density d(theta) on the CCXLV cosine lattice theta_j = 2 pi j / L
   (grid_density of c_ar + c_at, source-only, mirrored verbatim from
   lattice_rhp_szego_probe.build_coeffs_from_source).  The gap set is
   {j : d_j <= 0} on j = 0..L/2; the band set is its complement.  One
   table: raw band count, excluded theta-fraction, coarse gap count +
   coverage, disagreement to the median profile.  h-STABILITY: each
   rung's sign profile is resampled to a common COMMON_GRID theta grid;
   the median profile is the occupancy >= 1/2 set; per-rung
   disagreement = theta-fraction where the rung differs from the
   median; the drift law (disagreement and excluded fraction vs log h,
   jackknife 2SE) is reported.  If med disagreement > DISAGREE_BAR or
   coarse coverage < COARSE_COVER_MIN, the band structure has no
   h-stable finite-gap skeleton -> FINITEGAP-ILLDEFINED(drift law).

B  THE REFERENCE (mission b).  From the MEDIAN band set (coarse rule:
   maximal excluded runs sorted by theta-width, kept until
   COVER_FRAC of the excluded mass is covered, capped at G_MAX runs;
   bands = complement, mapped x = cos theta into [-1, 1]):
   B1 the equilibrium measure of the band set E = union [lo_i, hi_i]:
      rho(x) = |P(x)| / (pi sqrt(|R(x)|)) with R = prod (x - e_j) over
      all 2B endpoints and P monic of degree g = B-1 fixed by the g
      LINEAR conditions int_{gap_k} P(t)/sqrt|R(t)| dt = 0 (standard
      potential theory; the moduli are fixed SOURCE-ONLY by the band
      geometry, no wall data, no tuning).  WARDS: the linear system
      residual; P has exactly one root in each kept interior gap;
      total mass = 1 within EQ_MASS_TOL; per-band weights printed.
   B2 the finite-gap Jacobi chain: stabilized Lanczos
      (port_tangent_schur lanczos_chain, verbatim) on the per-band
      cosine-substituted quadrature of rho, N_CHAIN coefficients.
      J_star^fg = the FIRST NDIM coefficients, placed on the certified
      window [c_B, L_art] by the SAME declared affine embedding ARC
      uses (x -> (L+c)/2 + ((L-c)/2) x; inherited, disclosed).
   B3 SPECTRUM WARD: eigenvalues of the N_TRUNC x N_TRUNC truncation
      of the chain -- fraction inside E widened by BAND_WIDEN must be
      >= SPEC_MATCH_FRAC, and the per-band eigenvalue fraction must
      match the equilibrium weight within WEIGHT_TOL.
   B4 PERIOD-N READ (typed, never a kill): the tail (n >= TAIL_LO) of
      the chain is scanned for its best period N <= N_PERIOD_MAX
      (periodicity defect printed); the period-N periodic Jacobi
      discriminant Delta(x) = tr prod A_n(x) gives computed bands
      {|Delta| <= 2}; endpoint deviation vs target E typed
      FG-PERIODIC-MATCH (<= FG_BAND_TOL) / FG-PERIODIC-APPROX(dev).
      An approximate finite-gap reference that lands is worth more
      than a perfect one that never lands; the PAYOFF object is the
      chain of B2, the period read is its torus diagnostic.

C  THE PAYOFF (mission c).  The CCLIX framework is imported VERBATIM
   (highpole_relative_ks_radius_probe: ladder, global m=8 filter, C_R
   constant ward, per-step Lanczos wall rows, ARC/MED/EXT candidates,
   Gamma census, screens); J_star^fg enters as ONE MORE CANDIDATE with
   the full census (it consumes NO wall data, like ARC).  FIRST
   delta_fg = 1 - tr R(J_fg) is read (must be > 0; else
   NONPOSITIVE-DELTA and no upgrade).  Then ONE COMPACT TABLE:
   D_h^fg vs ARC/MED (min/med/max, segment-resolved incl. deep),
   Gamma^fg = C_R D_h^fg / delta_fg, the D_h^fg h-law (jackknife 2SE:
   does the exponent resolve flat?).
   VERDICT (frozen rule):
     FINITEGAP-ILLDEFINED(drift)  band skeleton unstable (A) or the
       construction wards of B fail;
     FINITEGAP-UPGRADES(numbers)  delta_fg >= DELTA_FLOOR and
       med D_fg <= D_HALVE * med D_ARC and controls fire and no
       screen RELOC (sub-typed BEATS-MED if med D_fg < med D_MED);
     FINITEGAP-NEUTRAL(reason)    otherwise.

D  GATES (mission d).
   D1 CCLIX shared quantities reproduced (frozen run only): C_R within
      CR_RTOL of 10.07; delta_ARC and delta_MED inside DELTA_BAND;
      med D_ARC / med D_MED within DMED_RTOL of the cited 7.5e4 /
      1.0e3; plus a 3-spot-rung table (first / middle / last census
      step: reserve, D_ARC, D_MED, D_FG).
   D2 tau- and c_h-relocation screens on Gamma^fg (CCLIX screen code
      verbatim; bars inherited).  RELOC blocks the upgrade verdict.
   D3 CONTROL (must fire): the seed-1 scramble world must BREAK the
      band match -- on SCR_SPOT spot rungs the theta sign-profile
      symmetric difference truth-vs-scramble must be >= SCR_FIRE_BAR
      on at least SCR_FIRE_MIN rungs; silence -> CONTROL-SILENT and
      no upgrade.
   D4 anti-circularity: the reference flows from band geometry
      FORWARD (source density -> band set -> equilibrium measure ->
      chain); the builder functions are AST-scanned for wall/tau/
      eigensolver identifiers (AC1) and the whole probe for zero/
      prime oracles; the eigensolver appears ONLY in the B3 ward on
      the reference chain itself and in the inherited labelled c_h
      screen, never in the construction.

FROZEN BARS / CONSTANTS.
  COMMON_GRID=4096; COVER_FRAC=0.85; G_MAX=7; DISAGREE_BAR=0.10;
  COARSE_COVER_MIN=0.60; N_EQ_BAND=2500; N_GAPQ=2000; N_CHAIN=64;
  TAIL_LO=16; N_TRUNC=400; BAND_WIDEN=5e-3; SPEC_MATCH_FRAC=0.97;
  WEIGHT_TOL=5e-2; EQ_MASS_TOL=1e-5; N_PERIOD_MAX=12; FG_BAND_TOL=5e-2;
  D_HALVE=0.5; CR_CITED=10.07; CR_RTOL=5e-3; DELTA_BAND=(0.88,0.98);
  D_ARC_CITED=7.5e4; D_MED_CITED=1.0e3; DMED_RTOL=0.25; SCR_SPOT=3;
  SCR_SEED=1; SCR_FIRE_BAR=2e-2; SCR_FIRE_MIN=2; DELTA_FLOOR and the
  gamma/screen bars inherited verbatim from the CCLIX probe module.
  Runtime cap 25 min.

VERDICT ENUMS (frozen before smoke):
  anatomy:   BANDS-STABLE / BANDS-DRIFT(law)
  reference: FG-CONSTRUCTED / FG-BROKEN(ward)
  period:    FG-PERIODIC-MATCH(N) / FG-PERIODIC-APPROX(N, dev)
  delta:     FEASIBLE / THIN-DELTA / NONPOSITIVE-DELTA (inherited)
  control:   SCRAMBLE-FIRES / CONTROL-SILENT
  final:     FINITEGAP-UPGRADES(numbers) / FINITEGAP-NEUTRAL(reason) /
             FINITEGAP-ILLDEFINED(reason)
The final enum is a finite-ladder reference-engineering diagnostic,
never an RH statement and never an all-h result.

SMOKE DISCLOSURE.
  SPEC v0 (2026-08-12, pre-smoke): all bars, enums, gates and the
  verdict rule frozen before the first run; smoke mode reduces
  resolution (N_EQ_BAND=800, N_GAPQ=600, N_CHAIN=48, N_TRUNC=200,
  band ladder zones[::4], wall ladder 10 surface + 3 deep) and SKIPS
  the D1 shared-quantity gates (a subset census cannot reproduce
  full-ladder medians; typed SMOKE-SKIP, declared pre-smoke).
  SMOKE-1 (SPEC v0, 2.2 s, 11 band rungs, 11 wall steps) ran 28/28
  GREEN, no kills.  Uncensored numbers: the mu_- gap set is
  SCATTERED AT LATTICE RESOLUTION -- raw band count 102..513
  (~ 0.6 h per rung), excluded fraction 0.285..0.342 (h-flat, slope
  +0.005 +/- 0.018), per-rung deviation to the median profile
  0.262..0.305 (med 0.2822 >> DISAGREE_BAR 0.10, h-flat), the
  coarse rule's G_MAX = 7 kept gaps cover only 0.026..0.088 of the
  excluded mass (largest macroscopic gap width ~ 0.002 pi) ->
  BANDS-DRIFT; the median-profile band set (7 bands, coverage
  0.088) gave an equilibrium chain that is arcsine to ~1e-4
  (be head 0.70711, 0.5, 0.5, ...), delta_fg +0.926764 FEASIBLE,
  med D_fg / med D_ARC = 0.999990 (NO gain), med D_MED 1.299e3,
  Gamma_fg max 8.208e5, D_fg h-law +0.004 +/- 0.009 (flat);
  equilibrium wards residual 6.97e-16 / mass dev 2.1e-11 / spectrum
  ward 48/48 in widened E, weight dev 3.5e-2; period read N* = 7,
  tail defect 3.4e-4, discriminant 3 bands, endpoint dev 3.3e-1 ->
  FG-PERIODIC-APPROX (typed); scramble control fired 3/3 (symdiff
  0.353/0.404/0.458); screens tau/c_h PASS for ARC/MED/FG; smoke
  verdict FINITEGAP-ILLDEFINED(band-drift).
  PRE-FREEZE AMENDMENT A2 (disclosed; after SMOKE-1, before SMOKE-2
  and before the freeze): the drift-law report gained the raw
  band-count fit (count vs h, log-log jackknife) and the ILLDEFINED
  verdict string now carries (med dev, count law, coarse coverage);
  NO bar, enum, gate or construction changed.  SMOKE-2 (SPEC v0
  code + A2, 2.2 s) reproduced SMOKE-1 identically and measured the
  count law h^+1.012 +/- 0.069 (R2 0.989).
  SPEC v1 (2026-08-12, FROZEN after the two disclosed smokes): bars,
  enums, gates unchanged; full-resolution constants restored
  (N_EQ_BAND=2500, N_GAPQ=2000, N_CHAIN=64, N_TRUNC=400, full
  ladders); this disclosure paragraph is the only spec-text change,
  hence the frozen-run SPEC SHA differs from v0.  No post-freeze
  amendment is permitted without a new disclosed SPEC version.
  AMENDMENT AFTER FROZEN RUN 1 (SPEC v2, 2026-08-12, disclosed; ONE
  numerical-conditioning fix, no bar, enum, gate, census or verdict
  rule moved).  Frozen run 1 (SPEC v1, 104.9 s, full 42-rung band
  ladder + 68-step wall census) failed exactly ONE check: B1, on the
  full ladder the median kept gaps CLUSTER inside theta/pi <= 0.083
  (all seven within [0.9666, 1.0] in x; median-profile excluded
  fraction 0.056, coverage 0.178), and the gap-polynomial linear
  system in the raw t^m monomial basis is near-collinear on such a
  cluster: one computed P-root left its gap and the equilibrium mass
  came out 1.000236 (|mass-1| = 2.4e-4 vs bar 1e-5).  FIX: the
  system is now solved in the centered-scaled basis u = (t - uc)/us
  on the gap-cluster hull with P(t) = us^g P_u(u) (mathematically
  identical, numerically conditioned); bars EQ_RESID_TOL/EQ_MASS_TOL
  kept.  All 27 other checks of frozen run 1 passed, including D1
  (C_R 10.07 reproduced; med D_ARC 7.4632e4 vs cited 7.5e4, med
  D_MED 1.0204e3 vs cited 1.0e3) and the headline anatomy (med dev
  0.304, count ~ h^+1.003 -> FINITEGAP-ILLDEFINED), which the fix
  cannot touch (A is upstream of B).  Frozen run 2 (SPEC v2) is the
  run of record.

ANTI-CIRCULARITY.  Ladder, filter, wall rows, candidates and screens
are the CCLIX probe module imported READ-ONLY; the band set and the
equilibrium reference are source-only (window geometry forward, no
wall matrix, no tau, no eigensolver in the builders, AST-enforced);
the census is never used to tune the reference; no zero/prime oracle
(AST-scanned); RNG only inside the inherited CCLIX D2 ward seed and
the inherited scramble seed.

NO RH claim.  No marker move, no verification/paper/ledger/website/
manifest edit.  This probe writes NOTHING to disk; the German CCLXXI
line is prepended to experiments/next.txt only after the frozen-run
summary.

Run:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/finitegap_reference_probe.py --smoke
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/finitegap_reference_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import highpole_relative_ks_radius_probe as hp   # noqa: E402 (CCLIX, READ-ONLY)
import port_tangent_schur_probe as pt            # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core              # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
COMMON_GRID = 4096
COVER_FRAC = 0.85
G_MAX = 7
DISAGREE_BAR = 0.10
COARSE_COVER_MIN = 0.60
N_EQ_BAND = 2500
N_GAPQ = 2000
N_CHAIN = 64
TAIL_LO = 16
N_TRUNC = 400
BAND_WIDEN = 5.0e-3
SPEC_MATCH_FRAC = 0.97
WEIGHT_TOL = 5.0e-2
EQ_MASS_TOL = 1.0e-5
EQ_RESID_TOL = 1.0e-10
N_PERIOD_MAX = 12
FG_BAND_TOL = 5.0e-2
D_HALVE = 0.5
CR_CITED = 10.07
CR_RTOL = 5.0e-3
DELTA_BAND = (0.88, 0.98)
D_ARC_CITED = 7.5e4
D_MED_CITED = 1.0e3
DMED_RTOL = 0.25
SCR_SPOT = 3
SCR_SEED = 1
SCR_FIRE_BAR = 2.0e-2
SCR_FIRE_MIN = 2

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
WALL_IDS = ("gram_anatomy", "eigvalsh", "eigh", "svd", "slogdet",
            "tau", "tau_h", "lamS", "negA", "wall_S", "wall_A",
            "schur_scalars", "eigvalsh_tridiagonal",
            "eigh_tridiagonal")
AC1_FUNCS = ("band_profile", "coarse_gaps", "median_band_set",
             "equilibrium_data", "eq_chain")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

if SMOKE:
    N_EQ_BAND = 800
    N_GAPQ = 600
    N_CHAIN = 48
    N_TRUNC = 200


def check(name, ok, kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned, fname=None):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    roots = []
    if fname is None:
        roots = [tree]
    else:
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == fname:
                roots.append(node)
    bad = []
    for root in roots:
        for sub in ast.walk(root):
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            if nm and nm.lower() in tuple(b.lower() for b in banned):
                bad.append(nm)
    return bad


# ================================= A: band anatomy (source-only)
def band_profile(kz, scramble_seed=None):
    """SOURCE-ONLY (AC1-scanned): the sign profile of the CCXLV
    density d(theta_j) on j = 0..L/2 for one frame-A rung.  Mirrors
    lattice_rhp_szego_probe.build_coeffs_from_source up to (and only
    up to) grid_density; no wall matrix, no folding, no chain."""
    rr = pt.window_of(kz, scramble_seed=scramble_seed)
    c_at, _ = core.atom_lags_at(rr["alpha"], rr["M"], rr["uu"],
                                2.0 * rr["lam"])
    c = np.asarray(rr["c_ar"], float) + np.asarray(c_at, float)
    d = pt.grid_density(c)
    L = 2 * rr["M"] - 2
    half = d[:L // 2 + 1]
    sign = half > 0.0
    return dict(kz=kz, h=rr["M"] // 2, L=L, sign=sign,
                excl=1.0 - float(np.mean(sign)))


def runs_of(mask):
    """Maximal True runs of a boolean array -> list of (i0, i1)
    inclusive index pairs."""
    out = []
    i = 0
    n = len(mask)
    while i < n:
        if mask[i]:
            j = i
            while j + 1 < n and mask[j + 1]:
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out


def coarse_gaps(sign, grid_n):
    """SOURCE-ONLY: the kept gap runs of one sign profile on its own
    grid (theta units of pi): excluded maximal runs sorted by width,
    kept until COVER_FRAC of the excluded mass, capped at G_MAX."""
    n = len(sign)
    gaps = runs_of(~np.asarray(sign, bool))
    if not gaps:
        return [], 1.0
    widths = [(i1 - i0 + 1) / float(grid_n) for i0, i1 in gaps]
    total = sum(widths)
    order = sorted(range(len(gaps)), key=lambda k: -widths[k])
    kept, cover = [], 0.0
    for k in order:
        if len(kept) >= G_MAX:
            break
        kept.append(gaps[k])
        cover += widths[k]
        if cover >= COVER_FRAC * total:
            break
    kept.sort()
    return kept, (cover / total if total > 0 else 1.0)


def median_band_set(profiles):
    """SOURCE-ONLY: resample every rung sign profile to the common
    theta grid, median profile = occupancy >= 1/2, then the coarse
    rule; returns the band set in x = cos(theta) plus diagnostics."""
    tt = (np.arange(COMMON_GRID) + 0.5) / COMMON_GRID   # theta / pi
    resampled = []
    for pr in profiles:
        n = len(pr["sign"])
        idx = np.minimum((tt * n).astype(int), n - 1)
        resampled.append(pr["sign"][idx])
    occ = np.mean(np.asarray(resampled, float), axis=0)
    s_med = occ >= 0.5
    disagree = [float(np.mean(rs != s_med)) for rs in resampled]
    kept, cover = coarse_gaps(s_med, COMMON_GRID)
    band_mask = s_med.copy()
    for i0, i1 in kept:
        band_mask[i0:i1 + 1] = False
    # re-open everything NOT in a kept gap (small excluded runs merge
    # into bands)
    coarse_mask = np.ones(COMMON_GRID, bool)
    for i0, i1 in kept:
        coarse_mask[i0:i1 + 1] = False
    bands_theta = [(tt[i0] - 0.5 / COMMON_GRID,
                    tt[i1] + 0.5 / COMMON_GRID)
                   for i0, i1 in runs_of(coarse_mask)]
    # x = cos(pi * t): decreasing; band list re-sorted increasing in x
    bands_x = sorted((math.cos(math.pi * t1), math.cos(math.pi * t0))
                     for t0, t1 in bands_theta)
    return dict(s_med=s_med, occ=occ, disagree=disagree, kept=kept,
                cover=cover, bands_theta=bands_theta, bands_x=bands_x)


# ============================ B: the equilibrium finite-gap reference
def _interval_quad(alo, ahi, npts):
    """Cosine-substituted midpoint nodes on [alo, ahi]: kills the
    inverse-sqrt endpoint singularities; returns (t, dphi, halfw)."""
    mid, hw = 0.5 * (ahi + alo), 0.5 * (ahi - alo)
    phi = (np.arange(npts) + 0.5) * math.pi / npts
    return mid + hw * np.cos(phi), math.pi / npts, hw


def _sqrtR_other(t, endpoints, alo, ahi):
    """sqrt(prod |t - e|) over all endpoints EXCEPT the two local
    ones alo, ahi (whose sqrt factors are absorbed by the cosine
    substitution)."""
    prod = np.ones_like(t)
    for e in endpoints:
        if e == alo or e == ahi:
            continue
        prod *= np.abs(t - e)
    return np.sqrt(prod)


def equilibrium_data(bands):
    """SOURCE-ONLY (AC1-scanned): the equilibrium measure of
    E = union of bands [(lo_i, hi_i)] in [-1, 1].  Returns nodes,
    weights, per-band masses, the monic gap polynomial P and wards."""
    endpoints = sorted([e for b in bands for e in b])
    nb = len(bands)
    g = nb - 1
    gaps = [(bands[i][1], bands[i + 1][0]) for i in range(g)]
    # ---- P monic deg g: int_gap_k P/sqrt|R| = 0, linear in coeffs.
    # A3 (SPEC v2, disclosed): solved in the CENTERED-SCALED basis
    # u = (t - uc)/us on the gap-cluster hull; the raw t^m basis is
    # near-collinear when the kept gaps cluster (frozen run 1), which
    # broke the root locations.  P(t) = us^g * P_u(u), monic in u.
    if g > 0:
        uc = 0.5 * (gaps[0][0] + gaps[-1][1])
        us = max(0.5 * (gaps[-1][1] - gaps[0][0]), 1e-12)
        imat = np.zeros((g, g + 1))
        for k, (glo, ghi) in enumerate(gaps):
            t, dphi, _hw = _interval_quad(glo, ghi, N_GAPQ)
            base = dphi / _sqrtR_other(t, endpoints, glo, ghi)
            u = (t - uc) / us
            for m in range(g + 1):
                imat[k, m] = float(np.sum(u ** m * base))
        coef = np.linalg.solve(imat[:, :g], -imat[:, g])
        resid = float(np.max(np.abs(imat[:, :g] @ coef + imat[:, g])))
        resid /= max(1.0, float(np.max(np.abs(imat))))
        pcoef = np.concatenate([[1.0], coef[::-1]])   # np.roots order
        roots_u = np.roots(pcoef)
        roots = uc + us * roots_u
        roots_ok = (np.max(np.abs(roots.imag)) < 1e-9 * max(1.0, us)
                    and all(any(glo < r < ghi for glo, ghi in gaps)
                            for r in np.sort(roots.real)))
    else:
        uc, us = 0.0, 1.0
        pcoef = np.array([1.0])
        resid, roots_ok = 0.0, True

    def pval(t):
        return (us ** g) * np.polyval(pcoef, (t - uc) / us)

    xs_all, ws_all, band_mass = [], [], []
    for (blo, bhi) in bands:
        t, dphi, _hw = _interval_quad(blo, bhi, N_EQ_BAND)
        w = (np.abs(pval(t)) / (math.pi
                                * _sqrtR_other(t, endpoints, blo, bhi))
             ) * dphi
        xs_all.append(t)
        ws_all.append(w)
        band_mass.append(float(np.sum(w)))
    xs = np.concatenate(xs_all)
    ws = np.concatenate(ws_all)
    return dict(bands=bands, endpoints=endpoints, g=g, gaps=gaps,
                pcoef=pcoef, resid=resid, roots_ok=roots_ok,
                xs=xs, ws=ws, band_mass=band_mass,
                mass=float(np.sum(ws)))


def eq_chain(eq):
    """SOURCE-ONLY (AC1-scanned): the finite-gap Jacobi chain of the
    equilibrium measure (stabilized Lanczos, port_tangent_schur
    verbatim)."""
    al, be, m0, steps = pt.lanczos_chain(eq["xs"], eq["ws"], N_CHAIN)
    return al, be, m0, steps


def ward_spectrum(al, be, eq):
    """B3 ward on the REFERENCE chain itself (labelled eigensolver;
    outside AC1 by design): truncation eigenvalues vs the band set."""
    ev = sla.eigvalsh_tridiagonal(al[:N_TRUNC], be[:N_TRUNC - 1]) \
        if len(al) >= N_TRUNC else \
        sla.eigvalsh_tridiagonal(al, be[:len(al) - 1])
    inside = np.zeros(len(ev), bool)
    frac_per_band = []
    for (blo, bhi) in eq["bands"]:
        hit = (ev >= blo - BAND_WIDEN) & (ev <= bhi + BAND_WIDEN)
        frac_per_band.append(float(np.mean(hit)))
        inside |= hit
    frac_in = float(np.mean(inside))
    wdev = float(np.max(np.abs(np.asarray(frac_per_band)
                               - np.asarray(eq["band_mass"]))))
    return frac_in, wdev, len(ev)


def period_read(al, be, eq):
    """B4: best tail period + discriminant bands (typed only)."""
    tail = np.arange(TAIL_LO, len(be))
    scale = max(float(np.max(np.abs(be))), 1e-300)
    best_n, best_def = 1, float("inf")
    for n in range(1, N_PERIOD_MAX + 1):
        idx = tail[tail + n < len(be)]
        if len(idx) < 4:
            continue
        d = math.sqrt(float(np.mean(
            (al[idx + n] - al[idx]) ** 2
            + (be[idx + n] - be[idx]) ** 2))) / scale
        if d < best_def:
            best_n, best_def = n, d
    n = best_n
    a_per = np.array([float(np.mean(be[TAIL_LO + k:len(be):n]))
                      for k in range(n)])
    b_per = np.array([float(np.mean(al[TAIL_LO + k:len(al):n]))
                      for k in range(n)])
    e_all = eq["endpoints"]
    grid = np.linspace(e_all[0] - 0.05, e_all[-1] + 0.05, 8001)
    disc = np.empty(len(grid))
    for i, x in enumerate(grid):
        m = np.eye(2)
        for k in range(n):
            a_k = a_per[k]
            a_km1 = a_per[k - 1] if k > 0 else a_per[n - 1]
            m = np.array([[(x - b_per[k]) / a_k, -a_km1 / a_k],
                          [1.0, 0.0]]) @ m
        disc[i] = m[0, 0] + m[1, 1]
    comp = runs_of(np.abs(disc) <= 2.0)
    comp_bands = [(grid[i0], grid[i1]) for i0, i1 in comp]
    # endpoint deviation: every target endpoint to the nearest
    # computed band edge
    edges = np.asarray([e for b in comp_bands for e in b])
    dev = (float(np.max([np.min(np.abs(edges - e)) for e in e_all]))
           if len(edges) else float("inf"))
    return n, best_def, comp_bands, dev


# ============================================================ main
def spot(rows, cands, results):
    """D1: the 3-spot-rung shared-quantity table."""
    picks = [0, len(rows) // 2, len(rows) - 1]
    print("    spot rungs (h, kz, seg, reserve, D_ARC, D_MED, D_FG):")
    med_census = set(id(r) for r in cands["MED"]["census"])
    for i in picks:
        r = rows[i]
        d_arc = hp.ks_distance(cands["ARC"]["a"], cands["ARC"]["b"],
                               r["a"], r["b"])
        d_med = (hp.ks_distance(cands["MED"]["a"], cands["MED"]["b"],
                                r["a"], r["b"])
                 if id(r) in med_census else float("nan"))
        d_fg = hp.ks_distance(cands["FG"]["a"], cands["FG"]["b"],
                              r["a"], r["b"])
        print("      h=%-5d kz=%-4d %-6s res=%+.4e  %.4e  %s  %.4e"
              % (int(r["h"]), r["kz"], r["seg"], r["reserve"], d_arc,
                 ("%.4e" % d_med) if math.isfinite(d_med)
                 else "prefix", d_fg))


def main():
    section("PRIME.ONEBADMODE.KS.FINITEGAP.01 -- finite-gap reference "
            "for the CCLIX radius corridor (EXPLORATION ONLY)")
    print("    mode: %s; SPEC-SHA %s"
          % ("SMOKE" if SMOKE else "FROZEN", SPEC_SHA[:8]))
    print("    NO RH claim; experiments/ only; nothing written to "
          "disk.")

    section("G0 -- scope + anti-circularity scans")
    bad = ast_scan(BANNED_IDS)
    check("G0.1 no zero/prime oracle identifiers: %s"
          % (bad if bad else "clean"), not bad, kill="K0")
    ac1 = []
    for fn in AC1_FUNCS:
        ac1 += ast_scan(WALL_IDS, fname=fn)
    check("G0.2 AC1: builder functions %s are source-only (no wall/"
          "tau/eigensolver identifier): %s"
          % (",".join(AC1_FUNCS), ac1 if ac1 else "clean"),
          not ac1, kill="K0")

    # ------------------------------------------------ A: band anatomy
    section("A -- BAND ANATOMY: the mu_- gap set of the deployed "
            "density, per frame-A rung")
    zones = pt.ladder_zones()
    if SMOKE:
        zones = zones[::4]
        print("    SMOKE: %d rungs %s" % (len(zones), zones))
    profiles = [band_profile(kz) for kz in zones]
    check("A1 all %d rung profiles built (L = 2M-2 lattice, "
          "source-only)" % len(profiles),
          all(p is not None for p in profiles), kill="K1")
    med = median_band_set(profiles)
    print("    rung table (kz, h, raw bands, excl frac, coarse gaps, "
          "coverage, dev-to-median):")
    counts = []
    for pr, dis in zip(profiles, med["disagree"]):
        kept, cover = coarse_gaps(pr["sign"], len(pr["sign"]))
        nb_raw = len(runs_of(np.asarray(pr["sign"], bool)))
        counts.append(nb_raw)
        print("      kz %-4d h %-5d bands %-3d excl %.4f  gaps %-2d "
              "cover %.3f  dev %.4f"
              % (pr["kz"], pr["h"], nb_raw, pr["excl"], len(kept),
                 cover, dis))
    hs = np.asarray([p["h"] for p in profiles], float)
    dis = np.asarray(med["disagree"], float)
    exc = np.asarray([p["excl"] for p in profiles], float)
    s1, se1, r21 = hp.jack_slope(np.log(hs), dis)
    s2, se2, r22 = hp.jack_slope(np.log(hs), exc)
    s3, se3, r23 = hp.jack_slope(np.log(hs),
                                 np.log(np.asarray(counts, float)))
    print("    drift law: dev-to-median vs log h slope %+.4f +/- "
          "%.4f (R2 %.3f); excl-frac vs log h slope %+.4f +/- %.4f "
          "(R2 %.3f)" % (s1, 2 * se1, r21, s2, 2 * se2, r22))
    print("    band-count law: raw band count ~ h^%+.4f +/- %.4f "
          "(R2 %.3f) -- a lattice-resolution gap set has NO h-limit "
          "at fixed band count" % (s3, 2 * se3, r23))
    print("    median profile: excl frac %.4f, kept gaps %d, "
          "coverage %.4f" % (1.0 - float(np.mean(med["s_med"])),
                             len(med["kept"]), med["cover"]))
    for (t0, t1) in [(k[0] / COMMON_GRID, (k[1] + 1) / COMMON_GRID)
                     for k in med["kept"]]:
        print("      kept gap theta/pi [%.4f, %.4f] width %.4f"
              % (t0, t1, t1 - t0))
    print("    median band set in x = cos(theta): %d bands"
          % len(med["bands_x"]))
    for (lo, hi) in med["bands_x"]:
        print("      band x [%.6f, %.6f]" % (lo, hi))
    bands_stable = (float(np.median(dis)) <= DISAGREE_BAR
                    and med["cover"] >= COARSE_COVER_MIN)
    check("A2 band skeleton h-stable: med dev %.4f <= %.2f and "
          "median coverage %.3f >= %.2f -> %s"
          % (float(np.median(dis)), DISAGREE_BAR, med["cover"],
             COARSE_COVER_MIN,
             "BANDS-STABLE" if bands_stable else "BANDS-DRIFT"),
          True)   # typed, feeds the final enum; not a kill

    # ------------------------------------- B: the finite-gap reference
    section("B -- THE REFERENCE: equilibrium measure of the median "
            "band set -> finite-gap Jacobi chain")
    eq = equilibrium_data(med["bands_x"])
    print("    B = %d bands, g = %d gaps; gap polynomial residual "
          "%.2e; roots in-gap %s; total mass %.12f; band weights %s"
          % (len(eq["bands"]), eq["g"], eq["resid"], eq["roots_ok"],
             eq["mass"],
             "/".join("%.4f" % m for m in eq["band_mass"])))
    check("B1 equilibrium construction: residual %.2e <= %.0e, "
          "one P-root per kept gap, |mass - 1| = %.2e <= %.0e"
          % (eq["resid"], EQ_RESID_TOL, abs(eq["mass"] - 1.0),
             EQ_MASS_TOL),
          eq["resid"] <= EQ_RESID_TOL and eq["roots_ok"]
          and abs(eq["mass"] - 1.0) <= EQ_MASS_TOL, kill="K2")
    al, be, m0, steps = eq_chain(eq)
    check("B2 finite-gap chain: %d/%d Lanczos steps, all be > 0"
          % (steps, N_CHAIN),
          steps == N_CHAIN and np.all(be > 0), kill="K2")
    print("    chain head al[:8] = %s" % np.array2string(
        al[:8], precision=5))
    print("    chain head be[:7] = %s (arcsine would be 1/sqrt2, "
        "then 1/2)" % np.array2string(be[:7], precision=5))
    frac_in, wdev, nev = ward_spectrum(al, be, eq)
    check("B3 spectrum ward: %.4f of %d truncation eigenvalues in "
          "widened E >= %.2f; per-band weight dev %.2e <= %.0e"
          % (frac_in, nev, SPEC_MATCH_FRAC, wdev, WEIGHT_TOL),
          frac_in >= SPEC_MATCH_FRAC and wdev <= WEIGHT_TOL,
          kill="K2")
    n_per, defect, comp_bands, dev = period_read(al, be, eq)
    per_lab = ("FG-PERIODIC-MATCH(%d)" % n_per
               if (dev <= FG_BAND_TOL
                   and len(comp_bands) == len(eq["bands"]))
               else "FG-PERIODIC-APPROX(%d, dev %.3e, %d bands)"
               % (n_per, dev, len(comp_bands)))
    print("    period read: N* = %d (tail defect %.3e); discriminant "
          "bands %d, endpoint dev %.3e -> %s"
          % (n_per, defect, len(comp_bands), dev, per_lab))
    check("B4 period-N diagnostic typed (never a kill): %s"
          % per_lab, True)

    # --------------------------- C: the CCLIX framework, FG candidate
    section("C -- THE PAYOFF: J_star^fg as one more candidate in the "
            "CCLIX radius framework (imported verbatim)")
    artifact = json.load(open(hp.ARTIFACT, encoding="utf-8"))
    wall_zones, steps_w = hp.build_ladder()
    poles, residues = hp.get_filter(steps_w, artifact)
    c_r_pack = hp.constant_ward(poles, residues)
    rows = hp.wall_rows(steps_w, artifact, poles, residues)
    cands = hp.build_candidates(rows, artifact, poles, residues)

    l_art = float(artifact["filter"]["L"])
    center = 0.5 * (l_art + hp.CB_F)
    half = 0.5 * (l_art - hp.CB_F)
    a_fg = half * np.asarray(be[:hp.NDIM - 1], float)
    b_fg = center + half * np.asarray(al[:hp.NDIM], float)
    jm_fg = hp.jacobi_matrix(a_fg, b_fg)
    phi_fg, _ = hp.trace_r_of(jm_fg, poles, residues)
    delta_fg = 1.0 - phi_fg
    typ_fg = ("FEASIBLE" if delta_fg >= hp.DELTA_FLOOR
              else "THIN-DELTA" if delta_fg > 0.0
              else "NONPOSITIVE-DELTA")
    print("    FG placed on [c_B, L_art] by the inherited ARC affine "
          "embedding (center %.6g, half %.6g)" % (center, half))
    check("C0 FIRST: delta_fg = 1 - tr R(J_fg) = %+.6f > 0 (%s)"
          % (delta_fg, typ_fg), delta_fg > 0.0)
    cands["FG"] = dict(name="FG", a=a_fg, b=b_fg, phi=phi_fg,
                       delta=delta_fg, typ=typ_fg, census=rows)
    gam_cands = {k: cands[k] for k in ("ARC", "MED", "FG")}
    results = hp.gamma_census(gam_cands, c_r_pack, label="fg")

    med_d = {k: float(np.median(results[k]["d"]))
             for k in ("ARC", "MED", "FG")}
    print("    THE PAYOFF TABLE (med D_h):  ARC %.4e   MED %.4e   "
          "FG %.4e" % (med_d["ARC"], med_d["MED"], med_d["FG"]))
    print("    ratios: FG/ARC = %.6f   FG/MED = %.6f"
          % (med_d["FG"] / med_d["ARC"], med_d["FG"] / med_d["MED"]))
    print("    Gamma_fg max %.4e; D_fg h-law h^%+.4f +/- %.4f "
          "(R2 %.3f)" % (results["FG"]["max_gamma"],
                         results["FG"]["d_slope"],
                         results["FG"]["d_2se"],
                         results["FG"]["d_r2"]))

    # ------------------------------------------------------ D: gates
    section("D -- GATES: CCLIX shared quantities, screens, scramble "
            "control")
    if SMOKE:
        check("D1 shared-quantity gates SMOKE-SKIP (subset census "
              "cannot reproduce full-ladder medians; disclosed "
              "amendment A1)", True)
    else:
        ok_cr = abs(c_r_pack["c_r"] - CR_CITED) / CR_CITED <= CR_RTOL
        ok_da = (DELTA_BAND[0] <= cands["ARC"]["delta"]
                 <= DELTA_BAND[1])
        ok_dm = (DELTA_BAND[0] <= cands["MED"]["delta"]
                 <= DELTA_BAND[1])
        ok_ma = abs(med_d["ARC"] / D_ARC_CITED - 1.0) <= DMED_RTOL
        ok_mm = abs(med_d["MED"] / D_MED_CITED - 1.0) <= DMED_RTOL
        check("D1 CCLIX shared quantities reproduced: C_R %.4f "
              "(cited %.2f), delta_ARC %+.4f / delta_MED %+.4f in "
              "[%.2f, %.2f], med D_ARC %.3e vs 7.5e4, med D_MED "
              "%.3e vs 1.0e3"
              % (c_r_pack["c_r"], CR_CITED, cands["ARC"]["delta"],
                 cands["MED"]["delta"], DELTA_BAND[0], DELTA_BAND[1],
                 med_d["ARC"], med_d["MED"]),
              ok_cr and ok_da and ok_dm and ok_ma and ok_mm,
              kill="K3")
    spot(rows, cands, results)

    ch_map = hp.ch_surface_map(rows)
    screen_labels = hp.run_screens(results, ch_map)

    print("    scramble band control (seed %d, %d spot rungs):"
          % (SCR_SEED, SCR_SPOT))
    picks = [zones[0], zones[len(zones) // 2], zones[-1]][:SCR_SPOT]
    fired = 0
    for kz in picks:
        tru = band_profile(kz)
        scr = band_profile(kz, scramble_seed=SCR_SEED)
        sd = float(np.mean(tru["sign"] != scr["sign"]))
        hit = sd >= SCR_FIRE_BAR
        fired += int(hit)
        print("      kz %-4d symdiff %.4f %s"
              % (kz, sd, "FIRES" if hit else "silent"))
    scr_ok = fired >= SCR_FIRE_MIN
    check("D3 scramble breaks the band match on %d/%d spot rungs "
          "(bar %.0e, need >= %d) -> %s"
          % (fired, len(picks), SCR_FIRE_BAR, SCR_FIRE_MIN,
             "SCRAMBLE-FIRES" if scr_ok else "CONTROL-SILENT"),
          scr_ok, kill="K4")

    # ---------------------------------------------------- verdict
    section("V -- VERDICT")
    reloc = any(screen_labels[k][1] == "RELOC"
                for k in ("ARC", "MED", "FG"))
    fg_built = (eq["resid"] <= EQ_RESID_TOL and eq["roots_ok"]
                and abs(eq["mass"] - 1.0) <= EQ_MASS_TOL
                and steps == N_CHAIN and frac_in >= SPEC_MATCH_FRAC
                and wdev <= WEIGHT_TOL)
    if not bands_stable or not fg_built:
        verdict = ("FINITEGAP-ILLDEFINED(%s)"
                   % ("band-drift: med dev %.3f, count ~ h^%+.3f, "
                      "coarse coverage %.3f"
                      % (float(np.median(dis)), s3, med["cover"])
                      if not bands_stable else "construction-ward"))
    elif (delta_fg >= hp.DELTA_FLOOR
          and med_d["FG"] <= D_HALVE * med_d["ARC"]
          and scr_ok and not reloc):
        sub = ("-BEATS-MED" if med_d["FG"] < med_d["MED"] else "")
        verdict = ("FINITEGAP-UPGRADES%s(med D %.3e vs ARC %.3e "
                   "MED %.3e; max Gamma %.3e)"
                   % (sub, med_d["FG"], med_d["ARC"], med_d["MED"],
                      results["FG"]["max_gamma"]))
    else:
        reasons = []
        if delta_fg < hp.DELTA_FLOOR:
            reasons.append("delta")
        if med_d["FG"] > D_HALVE * med_d["ARC"]:
            reasons.append("no-halving(FG/ARC %.4f)"
                           % (med_d["FG"] / med_d["ARC"]))
        if not scr_ok:
            reasons.append("control-silent")
        if reloc:
            reasons.append("screen-reloc")
        verdict = "FINITEGAP-NEUTRAL(%s)" % "+".join(reasons)
    print("    " + verdict)
    check("V1 final verdict typed by the frozen rule", True)

    # ---------------------------------------------------- finish
    section("FINISH")
    all_checks = CHECKS + hp.CHECKS
    all_kills = sorted(set(KILLS + hp.KILLS))
    n_pass = sum(1 for _n, ok in all_checks if ok)
    print("    checks %d/%d passed (this probe %d, CCLIX module %d); "
          "kills: %s"
          % (n_pass, len(all_checks), len(CHECKS), len(hp.CHECKS),
             ",".join(all_kills) if all_kills else "none"))
    print("    ANATOMY: %s (med dev %.4f, excl %s, drift slope "
          "%+.4f)" % ("BANDS-STABLE" if bands_stable
                      else "BANDS-DRIFT", float(np.median(dis)),
                      "%.3f..%.3f" % (float(np.min(exc)),
                                      float(np.max(exc))), s1))
    print("    REFERENCE: %s; %s; delta_fg %+.4f (%s)"
          % ("FG-CONSTRUCTED" if fg_built else "FG-BROKEN",
             per_lab, delta_fg, typ_fg))
    print("    PAYOFF: med D  ARC %.4e  MED %.4e  FG %.4e; "
          "FG h-law h^%+.3f+/-%.3f; max Gamma_fg %.3e"
          % (med_d["ARC"], med_d["MED"], med_d["FG"],
             results["FG"]["d_slope"], results["FG"]["d_2se"],
             results["FG"]["max_gamma"]))
    for k in ("ARC", "MED", "FG"):
        print("    SCREENS %s: %s" % (k, screen_labels[k][0]))
    print("    CONTROL: %s" % ("SCRAMBLE-FIRES" if scr_ok
                               else "CONTROL-SILENT"))
    print("    VERDICT: %s" % verdict)
    print("    NO-RH-CLAIM: finite float64 ladder only")
    print("    runtime %.1f s; SPEC-SHA %s" % (time.time() - T0,
                                               SPEC_SHA[:8]))
    print("    %s" % ("ALL GREEN" if n_pass == len(all_checks)
                      else "RED"))


if __name__ == "__main__":
    main()
