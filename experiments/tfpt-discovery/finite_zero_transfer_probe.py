#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""finite_zero_transfer_probe -- PRIME.WALL.FINITE_ZERO_TRANSFER.01
(EXPLORATION ONLY, experiments/; round 67 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE ZERO-SUPPLY ECONOMICS OF THE FINISHED
WALL.  The finite wall is closed: W1 67/67 (CLXXXIX, SPEC deea4e1c:
verified-zero supply at the j = 16 seat, surface 39/39 composed with
the CITED CLXXXIV deep 28/28), W2 67/67 + 8/8 (CXCV, SPEC 9cafc26f:
the 20,000,000-ordinate certified cache pays the CXCIII tail price),
and the composed census B ^ W1 ^ W2 holds on 39/39 matched surface +
8/8 deep rungs.  What is NOT yet measured is the ECONOMICS of that
closure: per rung h, WHAT zero-cutoff height T is actually required?
Three futures hang on the answer.  If T_req(h) grows much faster
than the window's own spectral reach pi/D_h, the zero supply is an
EXPENSIVE EXTERNAL BATTERY and the finite engine pays an exploding
import bill per rung.  If T_req(h) / (pi/D_h) is CONSTANT, the
supply is a LOCAL SAMPLING LAW -- each window only ever consumes
zeros out to a fixed multiple of its own reach, and the finite
engine is locally self-pricing (the interesting world: an analytic
per-window bound could then replace the cache class).  If the ratio
FALLS, deeper rungs are relatively cheaper and a bootstrap becomes
conceivable.  This probe measures the four T_req curves on the full
75-rung ladder, inverts them into the transfer law H(T) = maximal
wall depth certified by zeros up to height T, wards H(T) against
the three historic cache sizes, and states the parametrized
transfer theorem with its exact hypotheses.

THE EXACT OBJECTS (machinery of CLXXXIX + CXCV REUSED verbatim, one
new axis: the prefix cutoff).
 (1) T_req^W2(h): per rung and cut (A in HEAD_A + cB, CXCV read set
     verbatim), the CXCIII recomposed certificate
         m_cert(K) = FC + PARITH_hat(K) - TAILB(K),
         PARITH_hat(K) = -zs(K) - TRIV - RAMP_AT + RAMP_CONT
                         + EXT_CONT - EXT_AT,
         zs(K) = -4 J . F_K(v),  F_K(v) = Sum_{k <= K}
                 cos(gamma_k v)/gamma_k^2,
         TAILB(K) = 4 sd Abel[1/g^2; gamma_K -> T0, N = K exact]
                    + 4 e^{vmax/2} sd S2TAIL + ORD_PAD(K)
                    + NUFFT_PAD + TRIV_PAD,
     evaluated at a DECLARED geometric ladder of prefix cutoffs
     K in K_GRID (ratio ~10^{1/8} in K, anchors 7000 / 2,001,052 /
     2e7 mandatory), F_K accumulated by per-chunk banded type-3
     NUFFT (CXCV supply path, eps 1e-14).  A rung closes at K iff
     ANY cut certifies m_cert(K) > 0.  T_req^W2(h) = gamma_K* at
     the smallest STABLE anchor K* (closed at K* and at every
     larger anchor); the first crossing is reported when it
     differs (non-monotone census honestly counted).  Resolution
     is the grid ratio (~0.13 dex), declared, not bisected below.
 (2) T_req^W1(h): per W1 surface rung (39 parent rows), the
     CLXXXIX signed supply with prefix cutoffs K over the 7000
     mpmath cache: per fold j <= 32, zs_j(K) by prefix cumsum of
     the per-ordinate reads, TAILB_j(K) with the CLXXXIX per-rung
     tail grid from gamma_K, DPS_PAD prefix sums, and the CLXXXIV
     chain UNCHANGED (rung_assembly_new: fold domination -> [L2]
     -> [L5] -> FLOOR_new > mu1 and all v_lo_new > 0).  The
     anchor scan is a per-rung BINARY SEARCH for the smallest
     certifying anchor, followed by an explicit stability confirm
     on every anchor above it and a minimality check on the
     anchor below; on any non-monotone witness the full scan is
     run instead (identical T_req definition, only redundant
     negative evaluations are skipped).  Rungs whose ENVELOPE
     tier already certifies (old CLXXXIV cert, 7/39) get
     T_req^W1 = 0 (zero-free, excluded from log fits, counted).
     W1 deep rungs are zero-free by construction (CLXXXIV CITED
     28/28 envelope supply): T_req^W1 = 0.
 (3) T_req^Wall(h) = max(T_req^W1, T_req^W2) on the 39 matched
     surface kz + 8 deep rungs (B-half CLXXVII is zero-free);
     on the 28 W2-only surface rungs the wall face is W2 alone
     (flagged, included in the curve as T_req^W2).
     RATIO(h) = T_req^Wall(h) / (pi/D_h) -- THE deliverable.
 (4) H(T) = max{h : every deployed rung with h' <= h has
     T_req^Wall(h') <= T} (monotone envelope of the cumulative
     max over the h-sorted ladder), reported at the three historic
     cache heights T_7000 = gamma_7000, T_2M = gamma_2001052,
     T_20M = gamma_2e7, with the per-face closed-rung counts.

WHAT IS MEASURED.
 (a) THE FOUR CURVES: compact per-rung table (kz, h, alpha, D,
     T_req^W1, T_req^W2, T_req^Wall, pi/D, RATIO, binding face)
     over 67 surface + 8 deep rungs; fitted laws with jackknife
     slopes: log10 T_req^Wall vs ln h, vs alpha, and log10 RATIO
     vs ln h (residual band printed).
 (b) THE TRANSFER LAW: H(T) at the three historic points, warded
     against the measured censuses -- at N = 7000 the CXCIII
     VERBATIM route (cons.direct_read, per-rung tail grid) must
     reproduce 16/67 + 0/8 EXACTLY (kill); at the 2M prefix the
     uniform route must reproduce the CXCV economy census 65/67 +
     2/8 (kill); at 2e7 the full closure 67/67 + 8/8 (kill).  The
     parametrized theorem draft is printed VERBATIM with its exact
     hypotheses (cache certification battery, tail envelope,
     composition identities, B-floor) and honest typing.
 (c) THE EXTRAPOLATION: the fitted T_req^Wall law extrapolated one
     decade beyond the deployed ladder (h -> 10 h_max), with fit
     quality (R^2, 2SE, worst residual) honestly reported; world
     classification by FROZEN rule on the jackknife slopes
     (natural-log h, dex units, CLXXXV screen convention):
       b_T = slope log10 T_req^Wall vs ln h,
       b_R = slope log10 RATIO vs ln h;
       W-BOUNDED iff b_T <= +0.30; else W-ANALYTIC-REPLACEABLE iff
       b_R <= +0.30; else W-UNBOUNDED-PER-RUNG;
       V3 label: RATIO-CONSTANT iff |b_R| <= 0.30, RATIO-GROWING
       iff b_R > +0.30, RATIO-FALLING iff b_R < -0.30.
     Cross-reference (report only, different objects): CXCIII
     TAILLAW +0.736 dex/ln h; CCI bottom demand +0.60 dex/alpha.
 (d) GATES.  Wards (kill): both cache certifications (census,
     monotone, gamma_1, Rosser corridor per index on all 2e7,
     overlap, T_c < T0); CXCV SPEC prefixes; NUFFT spot ward +
     cumulative-prefix direct ward at sampled anchors; one full
     direct big read (smallest support); THE HEART |PARITH -
     PARITH_hat(K)| <= TAILB(K) on EVERY (read, anchor); soundness
     m_cert(K) <= m everywhere; W1 old-tier census == 7/39 and new
     census == 39/39 at K = 7000; W1 prefix supply == CLXXXIX
     rung_exact at K = 7000 on sample rungs; the three historic
     censuses above.  CONTROLS (must fire, kill): scrambled zero
     supply (ordinates jittered U(-2, 2), seed 1, sorted) must
     break the W2 heart on >= 5 reads at N = 7000 AND break the
     W1 exact heart on >= 5 of 33 folds at the control rung; the
     off-line impostor (gamma_1 -> beta = 0.75, FE-symmetrised,
     CXCV M4 verbatim) must shift PARITH_hat by >= 10x the genuine
     7000 residual.  The scrambled census at 7000 is printed (the
     H(T) ward point must not survive an impostor supply).  TAU
     SCREENS (CLXXXV jackknife, report): log10 T_req^Wall vs ln m
     and log10 RATIO vs ln m -- the expected label is AMBIG/RELOC
     (T_req anti-correlates with m BY CONSTRUCTION: it is the paid
     CXCIII tail law; declared, the label is anatomy not failure).
     ANTI-CIRCULARITY: verified ordinates enter ONLY the supply
     side and are tested against the independent prime side at
     every anchor (the heart ward); measured m appears only as
     truth column, soundness bar and denominator; no wall output
     feeds any bound; T_req is read off the certificate inequality
     only.  RNG: none except the declared jitter control (seed 1).

VERDICT (frozen enums, decided by these rules and nothing else):
  V1 curves: SUPPLY-CURVES-MEASURED(n_res/75 W2-resolved rungs;
     n_env zero-free W1 rungs; grid resolution dex) -- kill wards
     decide validity.
  V2 wards: HISTORIC-WARDS-REPRODUCED(16/67 + 0/8 at 7000 verbatim;
     65 + 2 at 2M; 67 + 8 at 2e7) -- kill wards decide.
  V3 law: RATIO-CONSTANT(b_R, 2SE, R^2) => LOCAL-SAMPLING-LAW /
     RATIO-GROWING(...) => EXTERNAL-BATTERY /
     RATIO-FALLING(...) => BOOTSTRAP-CANDIDATE  (frozen bars).
  V4 world: W-BOUNDED / W-ANALYTIC-REPLACEABLE /
     W-UNBOUNDED-PER-RUNG (frozen rule above) +
     TRANSFER-LAW-STATED(H at T_7000 / T_2M / T_20M).
  V5 gates: DISCRIMINATION-FIRES(scramble W2 n reads, W1 n folds,
     impostor ratio) + SCREENS(labels) /
     DISCRIMINATION-UNRESOLVED(census).
DEAD overrides: K1 PIPELINE-BROKEN / K2 WARD-BROKEN / K3
ALGEBRA-BROKEN as tagged.

FROZEN BARS: caches verified_zeros_n7000.npy (N_Z7 = 7000, CLXXXIX)
and verified_zeros_big.npy (N_ZB = 20,000,000, CXCV builder,
EXTERNAL-CITED pedigree: Odlyzko zeta_tables zeros6 n <= 2,001,052
at 4.5e-9; LMFDB / Platt for the rest at gamma 2^-50; every ordinate
below Platt-Trudgian T0 = 3e12 hence ON the line unconditionally;
Rosser 1941 corridor; Buethe 2018 baseline in the cited censuses);
SPEC prefixes warded: w2 8db29e6e, subgamma c7d8810c, consume
921140fa, j16supply deea4e1c, fullclose 9cafc26f; K_GRID_W2 =
unique(round(geomspace(250, 2e7, 40)) + {7000, 2001052, 2e7});
K_GRID_W1 = unique(round(geomspace(16, 7000, 18)) + {7000});
GEO_BIG = 1.0002 (uniform Abel grid, CXCV verbatim); E_ODLZ =
4.5e-9, E_LMFDB = gamma 2^-50, DPS_ERR = 1e-9 (W1, CLXXXIX
verbatim); NUFFT_EPS = 1e-14, band edges (gamma_1, 1e4, 3e5, seam,
T_c]; F_ERR_BAR = 1e-11 at NW = 16 spots x 4 sampled anchors
(cumulative-prefix direct ward) + full-grid spot ward at N_ZB;
FB_MATCH = 1e-10 (one direct big read, smallest support); heart
tol = CXCIII RECON_TOL scaled, soundness tol = CXCIII SOUND_TOL;
CLOSE7 = (16, 0) exact (verbatim route), ECON2M = (65, 2) exact,
FULLB = (67, 8) exact; W1_OLD_CERT = 7 exact, W1_NEW_CERT = 39/39;
W1_REPRO_RTOL = 1e-9 (prefix supply vs CLXXXIX rung_exact at K =
7000, 3 sample rungs, r_hat and TAILB); UNIFORM7_DEV_MAX = 2 rungs
(|uniform-route census - 16| at the 7000 anchor, soft: the uniform
Abel grid is tighter than the CXCIII per-rung grid, both rigorous;
deviation printed); SCR_MIN = 5 (both controls); IMP_BETA = 0.75,
IMP_RATIO_MIN = 10; SLOPE bars 0.30 / 0.70 (CLXXXV verbatim);
world bars: B_T_BOUND = 0.30, B_R_BOUND = 0.30 dex/ln h; fits on
uncensored rungs only (left-censored rungs at the smallest anchor
counted and flagged); EXTRAP_FACTOR = 10 (one decade in h).
Runtime cap declared: 25 min.  Smoke mode FZT_SMOKE=1 restricts
the surface to kz <= 30, DEEP_MAX = 2, W1 rows to the 6 shallowest,
thins both grids by 2 (anchors kept), and defers the full-only
census wards (disclosed prints); controls always full.

SCOUTING DISCLOSURE (2026-08-11, pre-spec): NO scratch scripts were
run for this probe; the sizing inputs are all cited from frozen
predecessors -- the CXCV builder plan mode (med 1.53e5 / max
1.904e7 ordinates at tail factor 0.9), the CXCIII zeros-needed
anatomy (med 9.8e5 / max 8.5e6 surface at cB) and closability
census (7/34/67 at N <= 1e5/1e6/1e7), the CXCV economy census
(65 + 2 at the 2M prefix) and the CLXXXIX T_c ladder scouting
(three worst W1 rungs need T_c ~ 6500-7000).  No T_req curve, no
H(T) value, no ratio slope was seen before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): the FIRST smoke
attempt (FZT_SMOKE=1) crashed in section C before producing any
result (KeyError: the CLXXXIX classical envelope tables lf.ENV were
not initialized -- a pipeline-setup omission, not a bar); the fix
adds the CLXXXIX section-E initialization verbatim
(deep.build_ext_tables -> lf.table_sups) plus its Buethe kill ward
C1b.  The SECOND smoke run passed: 40/40 checks, exit 0, 24.5 s
(19 surface rungs kz <= 30, 2 deep, W1 rows = 6, grids thinned).
Measured smoke content (subset, not gating): verbatim 7000 census
14/19 + 0/2, uniform-route 15/19 + 0/2 (dev 1 <= 2); prefix-NUFFT
ward 1.85e-15; big direct read 2.0e-17; heart worst scaled excess
-7.2e-09 over 150 x 23 cells, soundness 0; W1 prefix supply ==
rung_exact at K = 7000 to 9.0e-15 / 0.0 rel; W1 6/6 at 7000, old
tier 0/6 (matches the CLXXXIX smoke subset); 3 left-censored at
K = 250, 0 non-monotone; smoke-subset laws b_T +1.115, b_R +0.790,
b_alpha +0.852 (subset, h <= 700 + 2 deep -- the full ladder
decides); H = 364 / 700 / 2806; controls fire (scramble W2 130/150
reads, W1 25/33 folds, impostor 8.2e4 x); screens AMBIG/AMBIG (the
declared anti-correlation).  NO bar, band, count, rule or enum was
moved after the smoke run; the frozen run repeats everything on
the full 67 + 8 + 39 ladder.

HONEST SCOPE (stated once, repeated in the verdict): every T_req
value is a per-rung statement about the DEPLOYED windows, along the
MEASURED critical direction for the W2 face (CLXXXV
DIRECTION-CONDITIONAL caveat verbatim); nothing is uniform in h or
in direction; the deep block is FLOAT-LEVEL as in CLXXXV.  H(T) is
a monotone envelope over the deployed ladder ONLY -- it says
nothing about undeployed h.  The extrapolation is a FIT, not a
theorem; its world label is a fit-quality-weighted diagnosis.  The
inputs are cited verified zeros + unconditional envelopes (Rosser
corridor, Abel, beyond-T0 with beta in [0,1] unassumed) + exact
composition; a finite zero sum can never prove RH.  The all-h,
all-direction Weil-positivity object remains OPEN and RH-hard in
every branch.  NO RH claim in either direction.  No marker moves,
no promotion, no ledger row; stdout only; nothing written outside
experiments/.

Sources (read-only): v563_paper2_readouts (core);
w2_pairing_structure_probe (CLXXXV demand machinery);
w2_verified_supply_consumption_probe (CXCIII translation machinery:
phi_cont_of, direct_read, zsum4re, hat_seg_c, tail_grid,
zeros_needed); w2_full_zero_closure_probe (CXCV read set, NUFFT
supply path, abel_geo, tailb composition -- reimplemented verbatim
here for the prefix axis, SPEC prefix warded);
j16_verified_zero_supply_probe (CLXXXIX W1 supply: rung_exact,
rung_assembly_new, tail_grid, triv_exact IMPORTED and reused);
subgamma_fourier_bound_probe (corridor / Abel / s2_tail / T0);
exterior_pg_schur_probe (build_truth_rows);
bfloor_pg_dominance_probe (window_of);
w1_assembly_certificate_probe (rung_band, rung_assembly).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/finite_zero_transfer_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)
import w2_verified_supply_consumption_probe as cons  # noqa: E402
import w2_full_zero_closure_probe as fzc  # noqa: E402  (READ-ONLY)
import j16_verified_zero_supply_probe as j16  # noqa: E402 (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import w1_assembly_certificate_probe as asm  # noqa: E402 (READ-ONLY)

SMOKE = os.environ.get("FZT_SMOKE", "") == "1"

ZC7_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
ZCB_NPY = os.path.join(_HERE, "verified_zeros_big.npy")
ZCB_META = os.path.join(_HERE, "verified_zeros_big_meta.json")
N_Z7 = 7000
N_ZB = 20_000_000
SEAM_N = 2_001_052
E_ODLZ = 4.5e-9
E_LMFDB_ULP = 2.0 ** -50
GEO_BIG = 1.0002
NUFFT_EPS = 1.0e-14
BAND_EDGES = (1.0e4, 3.0e5)
F_ERR_BAR = 1.0e-11
FB_MATCH = 1.0e-10
NW_SPOTS = 16
NW_ANCH = 4
CORR_EPS = 1.0e-6
CLOSE7 = (16, 0)
ECON2M = (65, 2)
FULLB = (67, 8)
UNIFORM7_DEV_MAX = 2
W1_OLD_CERT = 7
W1_REPRO_RTOL = 1.0e-9
W1_REPRO_N = 3
SCR_MIN = 5
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
B_T_BOUND = 0.30
B_R_BOUND = 0.30
EXTRAP_FACTOR = 10.0
CUT_A = w2.HEAD_A
A_STR = 9
CTRL_KZ = w2.CTRL_KZ
KZ_TOP = 30 if SMOKE else w2.KZMAX
DEEP_MAX = 2 if SMOKE else 8
N_SURF = 67
N_DEEP = 8
W1_ROWS = 6 if SMOKE else 39
PREFIXES = dict(w2="8db29e6e", subgamma="c7d8810c",
                consume="921140fa", j16supply="deea4e1c",
                fullclose="9cafc26f")
TAILLAW_REF = 0.736
CCI_ALPHA_REF = 0.60

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in w2.BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def abel_geo(tc, n_at_tc):
    """CXCV verbatim: rigorous Abel upper bound of
    Sum_{gamma > tc} 1/gamma^2 on the declared geometric grid."""
    ng = int(math.ceil(math.log(subg.T0_RH / tc)
                       / math.log(GEO_BIG))) + 1
    tg = tc * GEO_BIG ** np.arange(ng + 1)
    tg[-1] = subg.T0_RH
    return subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                           n_start=float(n_at_tc))


def f_transform(gam, vu):
    """CXCV verbatim: banded type-3 NUFFT of
    F(v) = Sum_k cos(gamma_k v)/gamma_k^2."""
    import finufft
    w = (1.0 / gam ** 2).astype(np.complex128)
    edges = [float(gam[0])] + list(BAND_EDGES) + [float(gam[-1])]
    out = np.zeros(len(vu), np.complex128)
    for a, b in zip(edges[:-1], edges[1:]):
        lo = int(np.searchsorted(gam, a, side="left"))
        hi = int(np.searchsorted(gam, b, side="right")) \
            if b < float(gam[-1]) else len(gam)
        if hi > lo:
            out += finufft.nufft1d3(gam[lo:hi], w[lo:hi],
                                    np.asarray(vu, float),
                                    eps=NUFFT_EPS, isign=1)
    return out.real


def f_direct(gam, vv, chunk=400_000):
    acc = np.zeros(len(vv))
    for i0 in range(0, len(gam), chunk):
        g = gam[i0:i0 + chunk]
        acc += (np.cos(np.outer(vv, g)) @ (1.0 / g ** 2))
    return acc


def par_hat_from_f(pc, F, vidx):
    zs = -4.0 * float(pc["J"] @ F[vidx])
    return (-zs - pc["triv"] - pc["ramp_at"] + pc["ramp_cont"]
            + pc["ext_cont"] - pc["ext_at"]), zs


def tailb_uniform(pc, abel, s2t, se2, se3):
    """CXCV tailb_of verbatim (segment ORD_PAD + NUFFT_PAD)."""
    sd = pc["sd"]
    ord_pad = 4.0 * sd * (pc["vmax"] * se2 + 2.0 * se3)
    nuf_pad = 4.0 * sd * F_ERR_BAR
    return (4.0 * sd * abel
            + 4.0 * math.exp(0.5 * pc["vmax"]) * sd * s2t
            + ord_pad + nuf_pad
            + 1e-12 * (1.0 + abs(pc["triv"])))


def stable_index(closed):
    """Smallest i with closed[j] True for all j >= i; also the first
    crossing.  Returns (i_stable, i_first) or (None, None)."""
    n = len(closed)
    i_st = None
    for i in range(n - 1, -1, -1):
        if closed[i]:
            i_st = i
        else:
            break
    i_fi = next((i for i in range(n) if closed[i]), None)
    return i_st, i_fi


def ols_fit(x, y):
    """OLS + jackknife slope SE + R^2 + worst |residual| (dex)."""
    b, se, r2 = w2.jack_slope(np.asarray(x, float),
                              np.asarray(y, float))
    xm, ym = float(np.mean(x)), float(np.mean(y))
    a = ym - b * xm
    res = np.asarray(y, float) - (a + b * np.asarray(x, float))
    return a, b, se, r2, float(np.max(np.abs(res))), \
        float(np.median(np.abs(res)))


def main():
    section("PRIME.WALL.FINITE_ZERO_TRANSFER.01 -- the zero-supply "
            "economics of the finished wall (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = dict(
        w2=hashlib.sha256(w2.__doc__.encode("utf-8")).hexdigest(),
        subgamma=hashlib.sha256(
            subg.__doc__.encode("utf-8")).hexdigest(),
        consume=hashlib.sha256(
            cons.__doc__.encode("utf-8")).hexdigest(),
        j16supply=hashlib.sha256(
            j16.__doc__.encode("utf-8")).hexdigest(),
        fullclose=hashlib.sha256(
            fzc.__doc__.encode("utf-8")).hexdigest())
    for tag in sorted(shas):
        print("    %-9s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): Odlyzko zeta_tables "
          "zeros6 (n <= %d, 4e-9); LMFDB / Platt verified zeros "
          "(n <= %d);" % (SEAM_N, N_ZB))
    print("      Platt-Trudgian 2021 T0 = %.1e (every summed zero "
          "ON the line); Rosser 1941 N(T) corridor; Buethe 2018 "
          "(cited baselines)." % subg.T0_RH)
    if SMOKE:
        print("    *** SMOKE MODE: kz <= %d, DEEP_MAX = %d, W1 rows"
              " = %d, grids thinned, full-only wards deferred ***"
              % (KZ_TOP, DEEP_MAX, W1_ROWS))
    check("S0 AST firewall clean (CLXXXV identifier ban)",
          not ast_scan(), kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0b predecessor SPEC prefixes reproduced (%s)"
          % "/".join("%s %s" % (k, PREFIXES[k])
                     for k in sorted(PREFIXES)), ok_pref, kill="K2")
    try:
        import finufft  # noqa: F401
        ok_fin = True
    except Exception:                        # noqa: BLE001
        ok_fin = False
    check("S0c finufft available", ok_fin, kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Z
    section("Z -- both verified-zero caches, wards, prefix sums")
    check("Z0 caches present", os.path.exists(ZC7_NPY)
          and os.path.exists(ZCB_NPY) and os.path.exists(ZCB_META),
          kill="K1")
    if KILLS:
        return finish({})
    gam7 = np.load(ZC7_NPY)
    t_c7 = float(gam7[-1])
    check("Z1 7000-cache census + monotone + gamma_1 (dev %.1e)"
          % abs(gam7[0] - subg.GAMMA1),
          len(gam7) == N_Z7 and bool(np.all(np.diff(gam7) > 0.0))
          and abs(gam7[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    gamb = np.load(ZCB_NPY)
    meta = json.load(open(ZCB_META))
    t_cb = float(gamb[-1])
    check("Z2 big-cache census %d == meta, monotone, T_c = %.1f "
          "< T0" % (len(gamb), t_cb),
          len(gamb) == N_ZB and meta["n_zeros"] == N_ZB
          and bool(np.all(np.diff(gamb) > 0.0))
          and abs(gamb[0] - subg.GAMMA1) <= 2.0e-6
          and t_cb < subg.T0_RH, kill="K2")
    kk = np.arange(1, N_ZB + 1, dtype=float)
    up_r = subg.n_up(gamb + CORR_EPS)
    lo_r = subg.n_lo(gamb + CORR_EPS)
    up_l = subg.n_up(np.maximum(gamb - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gamb - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z3 Rosser corridor per index, both sides (%d/%d)"
          % (n_ok, N_ZB), n_ok == N_ZB, kill="K2")
    del kk, up_r, lo_r, up_l, lo_l
    dev7 = float(np.max(np.abs(gamb[:N_Z7] - gam7)))
    check("Z4 cache overlap (worst %.2e)" % dev7, dev7 <= 5.5e-9,
          kill="K2")
    s2t = subg.s2_tail()
    # W2 prefix cutoff grid (declared)
    kg = np.unique(np.concatenate([
        np.round(np.geomspace(250, N_ZB, 40)).astype(np.int64),
        np.array([N_Z7, SEAM_N, N_ZB], dtype=np.int64)]))
    if SMOKE:
        keep = np.zeros(len(kg), bool)
        keep[::2] = True
        keep[np.isin(kg, (N_Z7, SEAM_N, N_ZB))] = True
        kg = kg[keep]
    K_GRID = [int(k) for k in kg]
    NG = len(K_GRID)
    i_7000 = K_GRID.index(N_Z7)
    i_2m = K_GRID.index(SEAM_N)
    i_big = K_GRID.index(N_ZB)
    t_anch = np.array([float(gamb[k - 1]) for k in K_GRID])
    res_dex = float(np.max(np.diff(np.log10(t_anch))))
    print("    K_GRID: %d anchors, K %d..%d, T %.1f..%.1f, worst "
          "step %.3f dex" % (NG, K_GRID[0], K_GRID[-1], t_anch[0],
                             t_anch[-1], res_dex))
    # prefix scalar sums at the anchors
    e_k = np.empty(N_ZB)
    e_k[:SEAM_N] = E_ODLZ
    e_k[SEAM_N:] = gamb[SEAM_N:] * E_LMFDB_ULP
    idxg = np.array(K_GRID) - 1
    cs = np.cumsum(1.0 / gamb ** 2)
    inv2_a = cs[idxg].copy()
    cs = np.cumsum(e_k / gamb ** 2)
    se2_a = cs[idxg].copy()
    cs = np.cumsum(e_k / gamb ** 3)
    se3_a = cs[idxg].copy()
    del cs, e_k
    inv2_7 = float(np.sum(1.0 / gam7 ** 2))
    inv3_7 = float(np.sum(1.0 / gam7 ** 3))
    abel_a = np.array([abel_geo(t_anch[i], K_GRID[i])
                       for i in range(NG)])
    check("Z5 anchor Abel bases monotone falling (%.3e .. %.3e)"
          % (abel_a[0], abel_a[-1]),
          bool(np.all(np.diff(abel_a) < 0.0)), kill="K3")
    print("    prefix sums + Abel table done  [%.1f s]"
          % (time.time() - T0))

    # ------------------------------------------------------------ W
    section("W -- the CXCV ladder + read set (machinery verbatim)")
    rungs = []
    for kz in range(2, KZ_TOP + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    N = len(rungs)
    check("W1 surface ladder census %d %s" % (N, "== 67"
          if not SMOKE else ">= 8 (smoke)"),
          (N == N_SURF) if not SMOKE else (N >= 8),
          "h %d..%d  [%.1f s]" % (rungs[0]["h"], rungs[-1]["h"],
                                  time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    lam_ext = core.von_mangoldt_table(w2.TAB_EXT)
    check("W2 deep-table prefix byte-exact",
          bool(np.array_equal(lam_ext[:core.ATOM_MAX + 1],
                              core.LAM_TAB)), kill="K2")
    NNx = np.nonzero(lam_ext > 0.0)[0]
    EXT = dict(lam=lam_ext, NN=NNx, U=np.log(NNx.astype(float)),
               MU=2.0 * lam_ext[NNx] / np.sqrt(NNx.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    elig_kz = []
    for kz in range(2, min(w2.KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > w2.TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (w2.H_HOLD[0] <= Mk // 2 <= w2.H_HOLD[1]):
            continue
        elig_kz.append(kz)
    deep_rows = []
    if elig_kz:
        order = sorted(elig_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(DEEP_MAX, len(order)))))
        for ii in pick:
            r = w2.build_rung(order[ii], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    check("W3 deep census %d (eligible %d)"
          % (len(deep_rows), len(elig_kz)),
          len(deep_rows) == DEEP_MAX, kill="K1")
    if KILLS:
        return finish({})
    reads = []
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            tg = cons.tail_grid(r["D"], t_c7)
            r["_abel7"] = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                                          n_start=float(N_Z7))
            for A in CUT_A:
                sp = w2.demand_at_head(r, A)
                if sp is not None:
                    reads.append(dict(r=r, deep=is_deep,
                                      key=("A", A), sp=sp))
            spB = w2.split_at(r, r["ncB"])
            if spB is not None:
                reads.append(dict(r=r, deep=is_deep, key=("cB", 0),
                                  sp=spB))
    for rd in reads:
        rd["pc"] = cons.phi_cont_of(rd["r"], rd["sp"])
    v_all = np.unique(np.concatenate([rd["pc"]["v"]
                                      for rd in reads]))
    for rd in reads:
        rd["vidx"] = np.searchsorted(v_all, rd["pc"]["v"])
        assert bool(np.all(v_all[rd["vidx"]] == rd["pc"]["v"]))
    NR = len(reads)
    print("    %d reads, %d unique jump abscissae  [%.1f s]"
          % (NR, len(v_all), time.time() - T0))

    # ------------------------------------------------------------ A
    section("A -- the CXCIII VERBATIM route at N = 7000 (ward)")
    n_s7v = n_d7v = 0
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            mine = [rd for rd in reads if rd["r"] is r]
            closed = False
            for rd in mine:
                ph7, tb7 = cons.direct_read(
                    r, rd["sp"], rd["pc"], gam7, r["_abel7"], s2t,
                    inv2_7, inv3_7)
                rd["ph7v"], rd["tb7v"] = ph7, tb7
                if rd["sp"]["fc"] + ph7 - tb7 > 0.0:
                    closed = True
            if closed:
                if is_deep:
                    n_d7v += 1
                else:
                    n_s7v += 1
    print("    verbatim census at N = 7000: %d/%d + %d/%d  "
          "[%.1f s]" % (n_s7v, N, n_d7v, len(deep_rows),
                        time.time() - T0))
    if not SMOKE:
        check("A1 CXCIII census reproduced ((%d, %d) == (16, 0))"
              % (n_s7v, n_d7v), (n_s7v, n_d7v) == CLOSE7,
              kill="K2")
    else:
        check("A1 deferred in smoke (disclosed; verbatim census "
              "(%d, %d) on the subset)" % (n_s7v, n_d7v), True)

    # ------------------------------------------------------------ B
    section("B -- W2 prefix supply on the %d-anchor grid" % NG)
    zs_mat = np.zeros((NR, NG))
    F_cum = np.zeros(len(v_all))
    k_prev = 0
    Jv = [(rd["pc"]["J"], rd["vidx"]) for rd in reads]
    for i, K in enumerate(K_GRID):
        F_cum = F_cum + f_transform(gamb[k_prev:K], v_all)
        k_prev = K
        for jr, (J, vidx) in enumerate(Jv):
            zs_mat[jr, i] = -4.0 * float(J @ F_cum[vidx])
        if (i + 1) % 10 == 0:
            print("    ... anchor %d/%d (K = %d)  [%.1f s]"
                  % (i + 1, NG, K, time.time() - T0), flush=True)
    F_big = F_cum
    # cumulative-prefix direct ward at sampled anchors + spots
    sp_idx = np.unique(np.geomspace(1, len(v_all),
                                    NW_SPOTS).astype(int)) - 1
    an_idx = sorted(set(
        int(round(t)) for t in np.geomspace(1, NG, NW_ANCH))
        | {NG})
    fdev = 0.0
    for ia in an_idx:
        K = K_GRID[ia - 1]
        Fd = f_direct(gamb[:K], v_all[sp_idx])
        # rebuild the cumulative F at this anchor from zs is not
        # possible; recompute by chunk NUFFT re-accumulation:
        Fc = np.zeros(len(sp_idx))
        kp = 0
        for i, Kg in enumerate(K_GRID[:ia]):
            Fc = Fc + f_transform(gamb[kp:Kg], v_all[sp_idx])
            kp = Kg
        fdev = max(fdev, float(np.max(np.abs(Fc - Fd))))
    check("B1 cumulative-prefix NUFFT ward: worst |F_cum - "
          "F_direct| %.2e <= %.0e at %d spots x %d anchors"
          % (fdev, F_ERR_BAR, len(sp_idx), len(an_idx)),
          fdev <= F_ERR_BAR, kill="K3")
    rd_min = min(reads, key=lambda rd: len(rd["pc"]["v"]))
    zs_dir = cons.zsum4re(rd_min["pc"]["v"], rd_min["pc"]["J"],
                          gamb)
    jr_min = reads.index(rd_min)
    bdev = abs(zs_mat[jr_min, i_big] - zs_dir) \
        / max(1.0, abs(zs_dir))
    check("B2 one full direct big read (kz %d, %d jumps, dev "
          "%.1e <= %.0e)  [%.1f s]"
          % (rd_min["r"]["kz"], len(rd_min["pc"]["v"]), bdev,
             FB_MATCH, time.time() - T0), bdev <= FB_MATCH,
          kill="K3")
    # m_cert, heart, soundness on every (read, anchor)
    heart = -1e18
    sound = 0
    mcert = np.zeros((NR, NG))
    for jr, rd in enumerate(reads):
        pc, sp, r = rd["pc"], rd["sp"], rd["r"]
        sd = pc["sd"]
        ph = (-zs_mat[jr] - pc["triv"] - pc["ramp_at"]
              + pc["ramp_cont"] + pc["ext_cont"] - pc["ext_at"])
        ord_pad = 4.0 * sd * (pc["vmax"] * se2_a + 2.0 * se3_a)
        tb = (4.0 * sd * abel_a
              + 4.0 * math.exp(0.5 * pc["vmax"]) * sd * s2t
              + ord_pad + 4.0 * sd * F_ERR_BAR
              + 1e-12 * (1.0 + abs(pc["triv"])))
        mcert[jr] = sp["fc"] + ph - tb
        rd["ph_big"] = float(ph[i_big])
        rd["tb_big"] = float(tb[i_big])
        resid = sp["par"] - ph
        tol_a = cons.RECON_TOL * (1.0 + abs(sp["t_int"]))
        heart = max(heart, float(np.max(
            (np.abs(resid) - tb - tol_a)
            / max(1.0, abs(sp["t_int"])))))
        sound += int(np.sum(mcert[jr] > r["m"]
                            * (1.0 + cons.SOUND_TOL) + 1e-15))
    check("B3 THE HEART on every (read, anchor) cell (%d x %d, "
          "worst scaled excess %.1e)" % (NR, NG, heart),
          heart <= 0.0, kill="K2")
    check("B4 soundness m_cert <= m on every cell (%d violations)"
          % sound, sound == 0, kill="K2")

    # per-rung closure curves + censuses at the anchors
    all_r = [(r, False) for r in rungs] + [(r, True)
                                           for r in deep_rows]
    cen_s = np.zeros(NG, int)
    cen_d = np.zeros(NG, int)
    rows_out = []
    n_nonmono = 0
    for r, is_deep in all_r:
        jr_mine = [j for j, rd in enumerate(reads)
                   if rd["r"] is r]
        closed = np.any(mcert[jr_mine] > 0.0, axis=0)
        if is_deep:
            cen_d += closed.astype(int)
        else:
            cen_s += closed.astype(int)
        i_st, i_fi = stable_index(closed)
        if i_st is not None and i_fi is not None \
                and i_st != i_fi:
            n_nonmono += 1
        rows_out.append(dict(r=r, deep=is_deep,
                             i_st=i_st, i_fi=i_fi,
                             t_w2=(t_anch[i_st]
                                   if i_st is not None
                                   else float("inf")),
                             n_w2=(K_GRID[i_st]
                                   if i_st is not None else -1),
                             cens=(i_st == 0)))
    print("    uniform-route censuses: 7000 anchor %d/%d + %d/%d "
          "(verbatim %d + %d); 2M %d + %d; 2e7 %d + %d"
          % (cen_s[i_7000], N, cen_d[i_7000], len(deep_rows),
             n_s7v, n_d7v, cen_s[i_2m], cen_d[i_2m],
             cen_s[i_big], cen_d[i_big]))
    check("B5 uniform-route 7000 census within %d of the verbatim "
          "(dev %d)" % (UNIFORM7_DEV_MAX,
                        abs(int(cen_s[i_7000]) - n_s7v)),
          abs(int(cen_s[i_7000]) - n_s7v) <= UNIFORM7_DEV_MAX
          and int(cen_d[i_7000]) == n_d7v)
    if not SMOKE:
        check("B6 CXCV economy census at the 2M anchor ((%d, %d) "
              "== (65, 2))" % (cen_s[i_2m], cen_d[i_2m]),
              (int(cen_s[i_2m]), int(cen_d[i_2m])) == ECON2M,
              kill="K2")
        check("B7 CXCV full closure at the 2e7 anchor ((%d, %d) "
              "== (67, 8))" % (cen_s[i_big], cen_d[i_big]),
              (int(cen_s[i_big]), int(cen_d[i_big])) == FULLB,
              kill="K2")
    else:
        check("B6 deferred in smoke (2M census (%d, %d))"
              % (cen_s[i_2m], cen_d[i_2m]), True)
        check("B7 smoke closure at 2e7 ((%d, %d) full subset)"
              % (cen_s[i_big], cen_d[i_big]),
              int(cen_s[i_big]) == N
              and int(cen_d[i_big]) == len(deep_rows), kill="K2")
    n_cens = sum(1 for ro in rows_out if ro["cens"])
    n_open = sum(1 for ro in rows_out if ro["i_st"] is None)
    check("B8 every rung W2-resolved on the grid (%d open, %d "
          "left-censored at K = %d, %d non-monotone)"
          % (n_open, n_cens, K_GRID[0], n_nonmono), n_open == 0,
          kill="K2")

    # ------------------------------------------------------------ C
    section("C -- W1 prefix supply on the CLXXXIX chain "
            "(bisected anchors + stability confirm)")
    zones, truth, full, prows = parent.build_truth_rows()
    check("C1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(prows) == 39,
          kill="K1")
    if KILLS:
        return finish({})
    for w in prows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    # classical envelope tables (CLXXXIX section E verbatim)
    lam_w1 = j16.deep.build_ext_tables()
    NN_e = j16.deep.EXT["NN"]
    psi_e = np.cumsum(lam_w1[NN_e])
    j16.lf.ENV.update(j16.lf.table_sups(NN_e, psi_e,
                                        j16.deep.TAB_EXT))
    check("C1b Buethe envelope warded (sup %.4f <= %.2f)"
          % (j16.lf.ENV["BUETHE_SUP"], j16.lf.BUETHE),
          j16.lf.ENV["BUETHE_SUP"] <= j16.lf.BUETHE, kill="K2")
    kw1 = np.unique(np.concatenate([
        np.round(np.geomspace(16, N_Z7, 18)).astype(np.int64),
        np.array([N_Z7], dtype=np.int64)]))
    if SMOKE:
        keep = np.zeros(len(kw1), bool)
        keep[::2] = True
        keep[kw1 == N_Z7] = True
        kw1 = kw1[keep]
    KW1 = [int(k) for k in kw1]
    NW1 = len(KW1)
    tw1 = np.array([float(gam7[k - 1]) for k in KW1])
    print("    W1 anchor grid: %d anchors, K %d..%d, T %.1f..%.1f"
          % (NW1, KW1[0], KW1[-1], tw1[0], tw1[-1]))
    inv2c = np.cumsum(1.0 / gam7 ** 2)
    inv3c = np.cumsum(1.0 / gam7 ** 3)
    use = prows[:W1_ROWS]
    w1_rows = []
    n_old = 0
    repro_rh = 0.0
    repro_tb = 0.0
    n_new7 = 0
    for iw, w in enumerate(use):
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rb = asm.rung_band(rr["alpha"], rr["M"], rr["uu"],
                           2.0 * rr["lam"], rr["c_ar"], s2t,
                           trans_wards=False)
        pa = asm.rung_assembly(rb, r2["y_core"], r2["v_core"],
                               r2["h"], w["Gc"], w["mu1"])
        if pa is None:
            check("C-row kz %d old assembly None" % r2["kz"],
                  False, kill="K1")
            return finish({})
        old_cert = bool(pa["vpos"] and pa["floor"] > w["mu1"])
        n_old += int(old_cert)
        # per-fold precompute (CLXXXIX rung_exact anatomy, prefix)
        alpha, M, D, L = rr["alpha"], rr["M"], rb["D"], rb["L"]
        ph0 = subg.build_phit(alpha, M, D, L, 0)
        E = np.exp(1j * np.outer(gam7, ph0["v"]))
        tail_t0 = 4.0 * math.exp(alpha) * s2t
        vmax = float(ph0["v"][-1])
        folds = {}
        for j in range(0, j16.FBAND + 1):
            ph = subg.build_phit(alpha, M, D, L, j)
            se = ph["pl2"] / (math.log(2.0) - subg.U0)
            main_ext = 2.0 * (2.0 * (math.exp(0.5 * math.log(2.0))
                                     * (ph["pl2"] - 2.0 * se)
                                     - math.exp(0.5 * subg.U0)
                                     * (-2.0 * se)))
            hat_re = (-(E @ ph["J"]) / gam7 ** 2).real
            cum4 = 4.0 * np.cumsum(hat_re)
            folds[j] = dict(ph=ph, main_ext=main_ext,
                            t_ex=j16.triv_exact(ph), cum4=cum4)
        del E

        def ex_at(K):
            tc = float(gam7[K - 1])
            tg = j16.tail_grid(D, tc)
            dps_base = (vmax * float(inv2c[K - 1])
                        + 2.0 * float(inv3c[K - 1])) * j16.DPS_ERR
            ex = {}
            for j, fd in folds.items():
                ph = fd["ph"]
                c = subg.tenv_of(ph, tg[:-1], tg[1:]) \
                    / tg[:-1] ** 2
                zs_tail = subg.abel_upper(tg, c, n_start=float(K))
                tailb = (4.0 * zs_tail + tail_t0 * ph["sd"]
                         + 4.0 * ph["sd"] * dps_base
                         + 1.0e-12 * (1.0 + abs(fd["t_ex"])))
                ex[j] = dict(r_hat=(fd["main_ext"]
                                    - float(fd["cum4"][K - 1])
                                    - fd["t_ex"]),
                             tailb=tailb)
            return ex

        def cert_at(K):
            pn = j16.rung_assembly_new(rb, ex_at(K), r2["y_core"],
                                       r2["v_core"], r2["h"],
                                       w["Gc"], w["mu1"])
            return (pn is not None and pn["cert"]), pn

        # ward vs CLXXXIX rung_exact at K = 7000 (sample rungs)
        c7, pn7 = cert_at(N_Z7)
        n_new7 += int(c7)
        if iw < W1_REPRO_N:
            ex_ref = j16.rung_exact(alpha, M, D, L, gam7, s2t)
            ex_mine = ex_at(N_Z7)
            for j in range(0, j16.FBAND + 1):
                repro_rh = max(repro_rh,
                               abs(ex_mine[j]["r_hat"]
                                   - ex_ref[j]["r_hat"])
                               / (1.0 + abs(ex_ref[j]["r_hat"])))
                repro_tb = max(repro_tb,
                               abs(ex_mine[j]["tailb"]
                                   - ex_ref[j]["tailb"])
                               / abs(ex_ref[j]["tailb"]))
        # T_req^W1: envelope tier => 0; else bisect the anchor grid
        if old_cert:
            t_req = 0.0
            n_req = 0
            i_st = None
        elif not c7:
            t_req = float("inf")
            n_req = -1
            i_st = None
        else:
            lo, hi = 0, NW1 - 1   # cert_at(KW1[hi]) known True
            cache_c = {NW1 - 1: True}
            while hi - lo > 0:
                mid = (lo + hi) // 2
                if mid not in cache_c:
                    cache_c[mid] = cert_at(KW1[mid])[0]
                if cache_c[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            i_st = hi
            # stability confirm above + minimality check below
            for j2 in range(i_st, NW1):
                if j2 not in cache_c:
                    cache_c[j2] = cert_at(KW1[j2])[0]
                if not cache_c[j2]:
                    i_st = None
                    break
            if i_st is not None and i_st > 0:
                if i_st - 1 not in cache_c:
                    cache_c[i_st - 1] = cert_at(KW1[i_st - 1])[0]
                if cache_c[i_st - 1]:
                    i_st = None      # smaller stable index exists
            if i_st is None:
                # non-monotone witness: full scan (honest)
                cl = [cert_at(K)[0] for K in KW1]
                i_st, _ = stable_index(cl)
            t_req = tw1[i_st] if i_st is not None else float("inf")
            n_req = KW1[i_st] if i_st is not None else -1
        w1_rows.append(dict(kz=int(r2["kz"]), h=float(r2["h"]),
                            alpha=float(rr["alpha"]),
                            D=float(rb["D"]), old=old_cert,
                            t_req=t_req, n_req=n_req))
        if (iw + 1) % 6 == 0:
            print("    ... %d/%d W1 rows  [%.1f s]"
                  % (iw + 1, len(use), time.time() - T0),
                  flush=True)
    check("C2 W1 old-tier census %d %s" % (n_old, "== 7"
          if not SMOKE else "(smoke subset)"),
          (n_old == W1_OLD_CERT) if not SMOKE else True,
          kill="K2" if not SMOKE else None)
    check("C3 W1 new census at K = 7000: %d/%d (CLXXXIX 39/39)"
          % (n_new7, len(use)), n_new7 == len(use), kill="K2")
    check("C4 W1 prefix supply == CLXXXIX rung_exact at K = 7000 "
          "(%d rungs: r_hat %.1e, TAILB %.1e rel <= %.0e)"
          % (W1_REPRO_N, repro_rh, repro_tb, W1_REPRO_RTOL),
          repro_rh <= W1_REPRO_RTOL and repro_tb <= W1_REPRO_RTOL,
          kill="K3")
    n_w1_env = sum(1 for x in w1_rows if x["old"])
    n_w1_inf = sum(1 for x in w1_rows
                   if not np.isfinite(x["t_req"]))
    check("C5 every W1 row resolved (%d zero-free envelope tier, "
          "%d unresolved)" % (n_w1_env, n_w1_inf), n_w1_inf == 0,
          kill="K2")

    # ------------------------------------------------------------ D
    section("D -- THE FOUR CURVES (per rung; the deliverable)")
    w1_by_kz = {x["kz"]: x for x in w1_rows}
    w1b_kz = set(int(p["r2"]["kz"]) for p in prows)
    table = []
    for ro in rows_out:
        r = ro["r"]
        kz = int(r["kz"])
        matched = (kz in w1b_kz) and not ro["deep"]
        if ro["deep"]:
            t_w1, face_w1 = 0.0, "cited-env"
        elif matched and kz in w1_by_kz:
            t_w1 = w1_by_kz[kz]["t_req"]
            face_w1 = "env0" if t_w1 == 0.0 else "zeros"
        elif matched:
            t_w1, face_w1 = float("nan"), "unscanned"
        else:
            t_w1, face_w1 = float("nan"), "w2-only"
        t_w2 = ro["t_w2"]
        t_wall = max(t_w2, t_w1 if np.isfinite(t_w1) else 0.0)
        reach = math.pi / r["D"]
        table.append(dict(kz=kz, h=int(r["h"]),
                          alpha=float(r["alpha"]),
                          D=float(r["D"]), deep=ro["deep"],
                          matched=matched, t_w1=t_w1, t_w2=t_w2,
                          t_wall=t_wall, reach=reach,
                          ratio=t_wall / reach,
                          bind=("W1" if (np.isfinite(t_w1)
                                         and t_w1 > t_w2)
                                else "W2"),
                          cens=ro["cens"], m=float(r["m"])))
    table.sort(key=lambda x: (x["h"], x["kz"]))
    print("    kz    h     alpha   T_req^W1   T_req^W2   "
          "T_req^Wall  pi/D      RATIO     face")
    for x in table:
        tw1s = ("   env-0  " if x["t_w1"] == 0.0
                else ("     -    " if not np.isfinite(x["t_w1"])
                      else "%9.3e" % x["t_w1"]))
        print("    %-5d %-5d %6.3f  %s  %9.3e  %9.3e  %8.2e  "
              "%8.3f  %s%s%s"
              % (x["kz"], x["h"], x["alpha"], tw1s, x["t_w2"],
                 x["t_wall"], x["reach"], x["ratio"], x["bind"],
                 " [deep]" if x["deep"] else
                 ("" if x["matched"] else " [W2-only]"),
                 " [<=grid-min]" if x["cens"] else ""))
    n_bind_w1 = sum(1 for x in table if x["bind"] == "W1")
    print("    binding face: W1 on %d/%d rungs (W1 supply is "
          "%s-priced vs W2)" % (n_bind_w1, len(table),
                                "cheap" if n_bind_w1 == 0
                                else "sometimes"))
    nreq = np.array([ro["n_w2"] for ro in rows_out], float)
    print("    measured W2 ordinate demand: med %.3e / max %.3e "
          "(builder plan at f = 0.9: med 1.53e5 / max 1.904e7; "
          "CXCIII cB anatomy med 9.8e5 / max 8.5e6)"
          % (float(np.median(nreq)), float(np.max(nreq))))
    # the fitted laws (uncensored rungs only)
    fit_rows = [x for x in table if not x["cens"]]
    lx_h = np.log([x["h"] for x in fit_rows])
    ly_t = np.log10([x["t_wall"] for x in fit_rows])
    ly_r = np.log10([x["ratio"] for x in fit_rows])
    lx_a = np.array([x["alpha"] for x in fit_rows])
    a_t, b_t, se_t, r2_t, rmax_t, rmed_t = ols_fit(lx_h, ly_t)
    a_r, b_r, se_r, r2_r, rmax_r, rmed_r = ols_fit(lx_h, ly_r)
    a_a, b_a, se_a, r2_a, rmax_a, rmed_a = ols_fit(lx_a, ly_t)
    print("    LAW T:     log10 T_req^Wall = %+.3f %+.3f ln h   "
          "(2SE %.3f, R^2 %.3f, res med/max %.2f/%.2f dex, n=%d)"
          % (a_t, b_t, 2 * se_t, r2_t, rmed_t, rmax_t,
             len(fit_rows)))
    print("    LAW RATIO: log10 RATIO      = %+.3f %+.3f ln h   "
          "(2SE %.3f, R^2 %.3f, res med/max %.2f/%.2f dex)"
          % (a_r, b_r, 2 * se_r, r2_r, rmed_r, rmax_r))
    print("    LAW alpha: log10 T_req^Wall = %+.3f %+.3f alpha  "
          "(2SE %.3f, R^2 %.3f, res med/max %.2f/%.2f dex)"
          % (a_a, b_a, 2 * se_a, r2_a, rmed_a, rmax_a))
    print("    cross-reference (different objects, report only): "
          "CXCIII TAILLAW %+.3f dex/ln h vs b_T %+.3f; CCI bottom "
          "demand %+.2f dex/alpha vs b_alpha %+.3f"
          % (TAILLAW_REF, b_t, CCI_ALPHA_REF, b_a))
    check("D1 curves + laws recorded (%d fit rungs, %d censored)"
          % (len(fit_rows), n_cens), True)

    # ------------------------------------------------------------ E
    section("E -- THE TRANSFER LAW H(T) + the three historic wards")
    hh_sorted = [x for x in table]
    hh_sorted.sort(key=lambda x: (x["h"], x["kz"]))
    hs = np.array([x["h"] for x in hh_sorted], float)
    cmax = np.maximum.accumulate(
        np.array([x["t_wall"] for x in hh_sorted]))
    t_pts = ((t_c7, "T_7000"), (float(gamb[SEAM_N - 1]), "T_2M"),
             (t_cb, "T_20M"))

    def H_of(T):
        ok = cmax <= T
        if not np.any(ok):
            return 0
        idx = int(np.argmin(ok)) - 1 if not np.all(ok) \
            else len(ok) - 1
        return int(hs[idx]) if idx >= 0 else 0

    def counts_of(T):
        ns = sum(1 for x in table
                 if not x["deep"] and x["t_wall"] <= T)
        nd = sum(1 for x in table
                 if x["deep"] and x["t_wall"] <= T)
        return ns, nd

    for T, nm in t_pts:
        ns, nd = counts_of(T)
        print("    %s = %12.1f: H(T) = %-5d closed %d/%d surface "
              "+ %d/%d deep (wall face)"
              % (nm, T, H_of(T), ns, N, nd, len(deep_rows)))
    nsb, ndb = counts_of(t_cb)
    check("E1 H(T) endpoint consistent: all rungs certified at "
          "T_20M (%d + %d)" % (nsb, ndb),
          nsb == N and ndb == len(deep_rows), kill="K2")
    print("""
  %s
  THE PARAMETRIZED FINITE-ZERO TRANSFER LAW (theorem draft, stated
  LOUDLY; deployed ladder ONLY, NO RH CLAIM):

      ZerosCertified(T)  /\\  TailEnvelope(T)
          ==>   M_h > 0 (wall certificate) for EVERY deployed rung
                with h <= H(T),
      with H(T) the measured monotone envelope above
      (H(T_7000) = %d, H(T_2M) = %d, H(T_20M) = %d = full ladder).

  EXACT HYPOTHESES:
    (H1) ZerosCertified(T): a verified-ordinate cache {gamma_k <=
         T}, every ordinate below T0 = 3e12 (Platt-Trudgian 2021,
         hence ON the critical line unconditionally), strictly
         monotone, Rosser-corridor-consistent per index both
         sides, with declared per-ordinate error budgets (Odlyzko
         4.5e-9 / LMFDB gamma 2^-50 pedigree class).
    (H2) TailEnvelope(T): the unconditional tail budget TAILB(T) =
         4 S_Delta Abel[1/gamma^2; T -> T0, N(T) exact] + beyond-
         T0 term with beta in [0,1] UNASSUMED + declared ordinate/
         NUFFT/trivial pads (CXCIII/CXCV constants verbatim).
    (H3) The exact composition identities: the CXCIII translation
         (PARITH_hat recomposition, ramp/extension corrections)
         for the W2 face; the CLXXXIV chain [L1] -> [L2] -> [L5]
         (fold domination, Loewner, v-floor substitution) for the
         W1 face; both machine-checked per rung.
    (H4) The B-half floor (CLXXVII, zero-free, CITED 39/39 + 27/27)
         and, on the deep block, the CITED CLXXXIV W1 deep 28/28
         (envelope supply, zero-free).
  HONEST TYPING: per-rung on the deployed 67 + 8 ladder only; the
  W2 face holds along the MEASURED critical direction (DIRECTION-
  CONDITIONAL, CLXXXV); nothing is uniform in h or direction; no
  all-h statement; a finite zero sum can never prove RH; NO RH
  claim in either direction.  This law replaces millions of
  individual re-computations by ONE certified transfer statement
  parametrized by the cache height T.
  %s""" % ("*" * 72, H_of(t_c7), H_of(float(gamb[SEAM_N - 1])),
           H_of(t_cb), "*" * 72))
    check("E2 transfer law stated with H at the three historic "
          "points", True)

    # ------------------------------------------------------------ F
    section("F -- THE EXTRAPOLATION + world classification "
            "(frozen rule)")
    h_max = max(x["h"] for x in table)
    h_next = EXTRAP_FACTOR * h_max
    t_pred = 10.0 ** (a_t + b_t * math.log(h_next))
    print("    next decade: h = %d -> T_req ~ %.3e (power-law fit;"
          " ~N %.3e main-term ordinates)"
          % (int(h_next), t_pred,
             float(subg.n_main(np.array([min(t_pred,
                                             subg.T0_RH)]))[0])))
    print("    fit quality carried honestly: R^2 %.3f, 2SE %.3f, "
          "worst residual %.2f dex -> the prediction band is "
          "x10^%.2f either way at h = %d"
          % (r2_t, 2 * se_t, rmax_t, rmax_t, int(h_next)))
    if b_t <= B_T_BOUND:
        world = "W-BOUNDED"
    elif b_r <= B_R_BOUND:
        world = "W-ANALYTIC-REPLACEABLE"
    else:
        world = "W-UNBOUNDED-PER-RUNG"
    if abs(b_r) <= B_R_BOUND:
        v3lab = ("RATIO-CONSTANT(%+.3f, 2SE %.3f, R^2 %.3f) => "
                 "LOCAL-SAMPLING-LAW" % (b_r, 2 * se_r, r2_r))
    elif b_r > B_R_BOUND:
        v3lab = ("RATIO-GROWING(%+.3f, 2SE %.3f, R^2 %.3f) => "
                 "EXTERNAL-BATTERY" % (b_r, 2 * se_r, r2_r))
    else:
        v3lab = ("RATIO-FALLING(%+.3f, 2SE %.3f, R^2 %.3f) => "
                 "BOOTSTRAP-CANDIDATE" % (b_r, 2 * se_r, r2_r))
    print("    frozen classification: b_T %+.3f (bar %.2f), b_R "
          "%+.3f (bar %.2f) -> %s / %s"
          % (b_t, B_T_BOUND, b_r, B_R_BOUND, world, v3lab))
    check("F1 extrapolation + classification recorded", True)

    # ------------------------------------------------------------ M
    section("M -- controls (must fire) + tau screens")
    rng = np.random.default_rng(1)
    g_scr = np.sort(gam7 + rng.uniform(-2.0, 2.0, size=N_Z7))
    F7s = f_transform(g_scr, v_all)
    n_broken = 0
    for rd in reads:
        pc, sp = rd["pc"], rd["sp"]
        ph_s, _ = par_hat_from_f(pc, F7s, rd["vidx"])
        tol_a = cons.RECON_TOL * (1.0 + abs(sp["t_int"]))
        if abs(sp["par"] - ph_s) > rd["tb7v"] + tol_a:
            n_broken += 1
    check("M1 CONTROL: scrambled zero supply breaks the W2 heart "
          "on %d/%d reads at N = 7000 (>= %d)"
          % (n_broken, NR, SCR_MIN), n_broken >= SCR_MIN,
          kill="K2")
    # W1 scrambled-supply control at the first scanned row
    w = use[0]
    r2c = w["r2"]
    rrc = base.window_of(r2c["kz"])
    rbc = asm.rung_band(rrc["alpha"], rrc["M"], rrc["uu"],
                        2.0 * rrc["lam"], rrc["c_ar"], s2t,
                        trans_wards=False)
    exs = j16.rung_exact(rrc["alpha"], rrc["M"], rbc["D"],
                         rbc["L"], g_scr, s2t)
    n_w1b = 0
    for j in range(0, j16.FBAND + 1):
        res = abs(rbc["folds"][j]["r_true"] - exs[j]["r_hat"])
        if res > exs[j]["tailb"]:
            n_w1b += 1
    check("M2 CONTROL: scrambled supply breaks the W1 exact heart "
          "on %d/33 folds at kz %d (>= %d)"
          % (n_w1b, r2c["kz"], SCR_MIN), n_w1b >= SCR_MIN,
          kill="K2")
    # scrambled census at the 7000 anchor (the ward point moves)
    n_s_scr = 0
    for r, is_deep in all_r:
        mine = [rd for rd in reads if rd["r"] is r]
        cl = False
        for rd in mine:
            ph_s, _ = par_hat_from_f(rd["pc"], F7s, rd["vidx"])
            if rd["sp"]["fc"] + ph_s - rd["tb7v"] > 0.0:
                cl = True
        n_s_scr += int(cl and not is_deep)
    print("    scrambled-supply census at 7000: %d/%d surface "
          "(genuine %d; the H(T) ward point does not survive an "
          "impostor supply: heart broken on %d reads)"
          % (n_s_scr, N, n_s7v, n_broken))
    # off-line impostor (CXCV M4 verbatim, 7000 residual)
    r9 = next((r for r in rungs if r["kz"] == CTRL_KZ), None)
    rd9 = next(rd for rd in reads if rd["r"] is r9
               and rd["key"] == ("cB", 0))
    pc9 = rd9["pc"]
    g1 = float(gam7[0])
    on_pair = 4.0 * float((-np.sum(
        pc9["J"] * np.exp(1j * g1 * pc9["v"])) / g1 ** 2).real)
    dlt = IMP_BETA - 0.5
    quad = 4.0 * (cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                 pc9["slopes"],
                                 dlt + 1j * g1).real
                  + cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                   pc9["slopes"],
                                   -dlt + 1j * g1).real)
    shift = abs((-quad) - (-on_pair))
    resid9 = abs(rd9["sp"]["par"] - rd9["ph7v"])
    ratio = shift / max(resid9, 1e-300)
    check("M3 CONTROL: off-line impostor (gamma_1 -> beta %.2f) "
          "shifts PARITH_hat by %.4f = %.1e x the genuine 7000 "
          "residual (>= %.0f)" % (IMP_BETA, shift, ratio,
                                  IMP_RATIO_MIN),
          ratio >= IMP_RATIO_MIN, kill="K2")
    # tau screens (report; expected AMBIG/RELOC = the demand law)
    lm = np.log([x["m"] for x in fit_rows])
    scr = []
    lab, tag = w2.screen_label("log10 T_req^Wall vs ln m", lm,
                               np.asarray(ly_t))
    scr.append(("T_req vs m", tag))
    print("    %s" % lab)
    lab, tag = w2.screen_label("log10 RATIO vs ln m", lm,
                               np.asarray(ly_r))
    scr.append(("RATIO vs m", tag))
    print("    %s" % lab)
    print("    (declared: T_req anti-correlates with m by "
          "construction -- it is the paid CXCIII tail law; the "
          "screen label is anatomy, not failure)")
    check("M4 screens recorded", True)

    # ------------------------------------------------------ verdicts
    n_res = len(table) - n_open
    v1 = ("SUPPLY-CURVES-MEASURED(%d/%d W2-resolved; %d W1 "
          "zero-free envelope rungs; grid resolution %.2f dex; "
          "%d left-censored; %d non-monotone)"
          % (n_res, len(table), n_w1_env, res_dex, n_cens,
             n_nonmono))
    v2 = ("HISTORIC-WARDS-REPRODUCED(7000 verbatim %d/%d + %d/%d; "
          "2M %d + %d; 2e7 %d + %d; W1 7000 %d/%d, old tier %d)"
          % (n_s7v, N, n_d7v, len(deep_rows), cen_s[i_2m],
             cen_d[i_2m], cen_s[i_big], cen_d[i_big], n_new7,
             len(use), n_old))
    v3 = v3lab
    v4 = ("%s + TRANSFER-LAW-STATED(H = %d / %d / %d at T = "
          "%.3e / %.3e / %.3e)"
          % (world, H_of(t_c7), H_of(float(gamb[SEAM_N - 1])),
             H_of(t_cb), t_c7, float(gamb[SEAM_N - 1]), t_cb))
    if n_broken >= SCR_MIN and n_w1b >= SCR_MIN \
            and ratio >= IMP_RATIO_MIN:
        v5 = ("DISCRIMINATION-FIRES(scramble W2 %d reads / W1 %d "
              "folds, impostor %.0e x) + SCREENS(%s)"
              % (n_broken, n_w1b, ratio,
                 ", ".join("%s %s" % ab for ab in scr)))
    else:
        v5 = ("DISCRIMINATION-UNRESOLVED(W2 %d, W1 %d, imp %.1f)"
              % (n_broken, n_w1b, ratio))
    check("V1 typed: %s" % v1, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(labels.get(k, "-")
                             for k in ("v1", "v2", "v3", "v4",
                                       "v5"))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: (i) every T_req value is per-rung on the deployed
  67 + 8 (+ 39 W1) ladder; the W2 face holds along the MEASURED
  critical direction (CLXXXV DIRECTION-CONDITIONAL, nothing uniform
  in h or direction, deep block float-level); (ii) H(T) is a
  monotone envelope over the DEPLOYED ladder only -- it says
  nothing about undeployed h; (iii) the extrapolation is a FIT with
  its quality printed, not a theorem; (iv) inputs = cited verified
  zeros (Odlyzko / LMFDB-Platt, all below Platt-Trudgian T0 = 3e12)
  + unconditional envelopes (Rosser corridor, Abel, beyond-T0 with
  beta in [0,1] unassumed) + exact composition; (v) the all-h,
  all-direction Weil-positivity object remains OPEN and RH-hard in
  every branch; NO RH claim in either direction.  No marker moves,
  no promotion, no ledger row; stdout only.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
