#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zero_window_bootstrap_probe -- PRIME.ZERO.WINDOW.BOOTSTRAP.01
(EXPLORATION ONLY, experiments/; 2026-08-12).

WHY THIS PROBE EXISTS -- THE CHEAP GO/NO-GO FOR THE ZERO-WINDOW
BOOTSTRAP ROUTE.  CCV measured the supply curve H(T) = maximal wall
depth certified by verified zeros up to height T (H = 254 / 1256 /
2806 at the three historic cache heights) and the external-battery
law (zero demand ~ h^2.8, outrunning the window reach ~ h^2).  The
LAST hope for an engine that climbs to infinity on finite fuel is a
BOOTSTRAP: RH verified to T => wall positivity to depth H(T) =>
the certified-positive windows act as OFF-LINE-ZERO DETECTORS and
exclude off-line zeros up to a height D(H(T)) -- if D(H(T)) > T the
verified frontier advances and iterates.  This probe computes the
ONE number family that decides it: D(H(T)) / T.  KILL CRITERION
(frozen): if even the most favorable (single-violator, envelope-
level) D stays below T at every anchor, bigger caches are finite
verification only and the bootstrap route is buried.

THE EXACT OBJECTS (machinery CCV / CXCV / CXCIII / CLXXXIX reused
verbatim; ONE new axis: the detector reading of the certified
identity).
 (1) H(T): per rung the W2 closure at a DECLARED anchor ladder of
     prefix cutoffs K (uniform CXCV route: m_cert(K) = FC +
     PARITH_hat(K) - TAILB(K) > 0 on any cut), W1 face 39/39 at the
     7000 cache (CLXXXIX chain verbatim; CCV measured max
     T_req^W1 = 5350 < gamma_7000, CITED -- the wall face at every
     anchor here is W2-decided), deep W1 zero-free (CLXXXIV CITED).
     H(T_j) = max h such that EVERY deployed rung with h' <= h is
     closed at anchor j (CCV envelope, 0 non-monotone measured).
     WARDS (kill): H(T_7000) = 254, H(T_2M) = 1256, H(T_20M) =
     2806; censuses (16, 0) verbatim route / (65, 2) / (67, 8).
 (2) D(H): the DETECTOR.  Per deployed W2 read (rung, cut) the
     certified explicit-formula identity (the CCV heart) gives
         PARITH  =  PARITH_hat(K) + R,
     with PARITH prime-side computed (NO zeros), PARITH_hat(K)
     consuming the verified cache <= gamma_K = T, and R the exact
     total contribution of all zeros ABOVE T.  R is therefore a
     MEASURED number: r_meas = |PARITH - PARITH_hat(K)| (+ declared
     numeric pads).  A hypothetical zero quadruple at (beta = 1/2 +
     delta, gamma) with gamma > T contributes
         q(delta, gamma) = -4 Re[ hhat(delta + i gamma)
                                 + hhat(-delta + i gamma) ],
     hhat(s) = Int phi(u) e^{su} du (cons.hat_seg_c closed form,
     the CXCV M4 impostor transform).  EXCLUSION: (delta, gamma) is
     impossible iff |q(delta, gamma)| > r_meas + pads + MASK, where
     MASK bounds the rest-of-zeros contribution:
       NAIVE (single violator): all other unverified zeros ON the
       line -> MASK_n = 4 sd (Abel[1/g^2; T -> T0] + s2_tail)
       (Rosser corridor, unconditional counting);
       GUARDED (worst-case masking): other zeros anywhere in the
       strip -> MASK_g = 4 sd e^{vmax/2} (Abel + s2_tail).
     Per-zero envelope (rigorous, phi vanishing at both support
     ends => hhat(s) = (1/s^2) Sum J e^{s v}):
         |q| <= 4 (e^{delta vmax} + 1)(sd / g^2 + |fend| / g),
     sd = Sum |J|; the |fend| term covers reads with a nonzero
     endpoint value (deep table, typed).  THREE frontiers, all
     reported per anchor at the delta grid:
       D_env  = envelope crossing (OPTIMISTIC upper bound: the
                largest gamma where exclusion could possibly fire),
       D_fire = largest actually-firing point on the declared
                gamma > T scan grid (the honest frontier),
       D_grip = largest firing point on the full-range grid
                gamma in [50, 4 D_env] IGNORING the gamma > T
                restriction (instrument sensitivity profile: where
                the detector loses grip; sub-T grip is NOT new
                exclusion, typed).
     D(H(T_j)) uses reads of rungs with h <= H(T_j) only (the
     depth-H window family; declared).  THE MULTI-VIOLATOR CAVEAT
     is handled by computing BOTH: D_naive (single-violator) and
     D_guard (MASK_g); if only the naive D is nonempty, the missing
     First-Violator-Isolation lemma is SPEC'D verbatim (below).
     STRICT-D TYPING: exclusion always has a delta floor
     delta_min(gamma) > 0 (|q| -> on-line reading as delta -> 0,
     never above threshold) -- the window form NEVER forces zeros
     ONTO the line, only far-off-line quadruples out; D_strict = 0
     identically and the bootstrap product "RH to D" is really
     "no zeros with delta >= delta_min up to D"; typed loudly.
 (3) THE RATIO: the table T / H(T) / D_env(H(T)) / D_env / T at the
     six declared anchors (three historic + three intermediate),
     the fitted frontier law log10 D_env vs log10 T (jackknife),
     and the Platt-Trudgian extrapolation: H(T0) from the CITED CCV
     law log10 T_req = -3.045 + 1.228 ln h (2SE 0.094, resmax 0.90
     dex), vmax(h) fitted on the deployed ladder, D_env(T0) =
     sqrt((e^{vmax(H(T0))/2} + 1) / s2_tail) (sd cancels; r_meas
     at the T0 frontier unknowable, set 0 = FAVORABLE, typed),
     with honest error bands carried through both fits.
 (4) SELF-CONTAINEDNESS AUDIT (anti-circularity, the hidden-input
     check): the deployed TAILB assumes zeros in (T, T0] ON the
     line via the Platt-Trudgian CITATION -- legitimate for the
     published-baseline reading, NOT for a self-contained bootstrap
     stage at frontier T < T0.  The self-contained certificate
     m_sc = FC + PARITH_hat(K) - TAILB_sc(K) with the beta-
     unassumed tail 4 sd e^{vmax/2} (Abel + s2_tail) from T is
     computed per read; the self-contained closure census and
     H_sc(T_j) are reported (W2 face; the W1 face would need the
     same treatment, so H_sc is an UPPER bound on the self-
     contained wall depth, typed).

WHAT IS MEASURED.
 (a) the sensitivity profile per anchor: D_env / D_fire / D_grip at
     delta in {0.05, 0.1, 0.25, 0.5}; the measured |q| peak vs the
     sd envelope (incoherence gap); delta_min at the grip height;
     local coverage fraction + max gap on a fine grid at the grip
     height (exclusion is pointwise-in-gamma on declared grids,
     NOT interval-certified, typed);
 (b) THE TABLE (the deliverable): T, H(T), H_sc(T), D_env, D_fire,
     D_env/T, D_guard, max window reach pi/D_h among closed rungs;
     the frontier law slope p in log10 D_env = p log10 T + c;
 (c) the T0 = 3.0001753328e12 row: H(T0), D_env(H(T0)),
     D_env(H(T0))/T0 with bands;
 (d) the verdict (frozen rules below) with the kill criterion.
GATES.
 WARDS (kill): both cache certifications (census, monotone,
 gamma_1, Rosser corridor per index, overlap, T_c < T0); SPEC
 prefixes of the five predecessors + CCV; verbatim CXCIII route at
 7000 == (16, 0); 2M == (65, 2); 2e7 == (67, 8); uniform-7000 dev
 <= 2; H wards 254 / 1256 / 2806; W1 39/39 at 7000 + old tier 7;
 Buethe envelope; NUFFT spot ward + one full direct big read; THE
 HEART on every (read, anchor) cell; soundness m_cert <= m;
 transform convention ward |q(delta -> 0)/2 - onpair| ~ 0;
 envelope soundness |q| <= env at sampled (read, delta, gamma).
 CONTROLS (must fire, kill): scrambled zero supply (jitter U(-2,2),
 seed 1) breaks the W2 heart on >= 5 reads at N = 7000 (the
 residual r_meas that thresholds the detector is heart-guarded);
 the CXCV M4 off-line impostor (gamma_1 -> beta 0.75) shifts
 PARITH_hat by >= 10x the genuine 7000 residual; CATCH: a fresh
 64-point grid at 0.45 D_grip (delta = 0.5, best read, lowest
 anchor) must fire >= 1 point; MISS: a fresh grid at 4 D_env must
 fire 0 points; NO-FALSE-ALARM: the on-line reading |q(0, gamma)|
 at gamma = 1.01 T must stay below threshold on every deployed
 read.  ANTI-CIRCULARITY: the sensitivity q(delta, gamma) is
 cache-free (pure window transform); the threshold consumes ONLY
 the declared bootstrap inputs (prime side, verified cache <= T,
 unconditional envelopes); every exclusion target satisfies
 gamma > T; the hidden T0-citation input in the POSITIVITY leg is
 not hidden but audited (H_sc above).  RNG: none except the
 declared jitter control (seed 1).

THE MISSING LEMMA (spec'd, printed in the verdict): FVI (First-
Violator Isolation).  For every deployed certified read (window
phi, measured direction) and every gamma* > T: if rho* = 1/2 +
delta* + i gamma* is the lowest off-line zero, then the total
contribution of all OTHER zeros to the read exceeds -eps(gamma*)
with eps(gamma*) <= |q(delta*, gamma*)| - r_meas - MASK_n.
Sufficient pointwise form: Re[hhat(beta + i gamma) +
hhat(1 - beta + i gamma)] >= 0 for all beta in [0, 1], gamma >=
gamma* -- strip-positivity of the deployed window transform OFF
the critical line.  This is NOT implied by the certified wall
positivity (which is an aggregate statement at the on-line
reading); it is Weil-cone membership off the line, RH-hard
flavor, OPEN.  Without FVI only D_guard counts, and D_guard is
measured below.

VERDICT (frozen enums, decided by these rules and nothing else):
  V1 supply: SUPPLY-WARDS-REPRODUCED(H 254/1256/2806; censuses;
     W1 39/39 + old 7) -- kill wards decide validity.
  V2 detector: DETECTOR-PROFILE-MEASURED(D_grip / D_fire / D_env
     at the declared deltas; incoherence gap; delta_min; coverage).
  V3 THE RATIO (kill criterion): with ratio_j = max D_env over
     closed reads at anchor j divided by T_j:
       BOOTSTRAP-DEAD  iff ratio_j < 1 at EVERY anchor (even the
         optimistic envelope frontier never reaches the verified
         height; state the fitted law and the T0 ratio, bury);
       BOOTSTRAP-CONDITIONAL iff ratio_j > 1 at some anchor AND
         the guarded ratio <= 1 there (FVI spec is the price);
       BOOTSTRAP-OPEN  iff the GUARDED ratio > 1 at the top anchor
         AND the fitted slope p >= 1 (state the iteration yield).
  V4 guard + audit: GUARD-EMPTY(sup margin) / GUARD-NONEMPTY(D) +
     SELF-CONTAINED-POSITIVITY(H_sc censuses at the anchors).
  V5 controls: DISCRIMINATION-FIRES(scramble reads, impostor x,
     catch, miss, no-false-alarm) / DISCRIMINATION-UNRESOLVED.
DEAD overrides: K1 PIPELINE-BROKEN / K2 WARD-BROKEN / K3
ALGEBRA-BROKEN as tagged.

FROZEN BARS: caches verified_zeros_n7000.npy (N_Z7 = 7000,
CLXXXIX) and verified_zeros_big.npy (N_ZB = 20,000,000, CXCV
builder, EXTERNAL-CITED pedigree: Odlyzko zeta_tables zeros6
n <= 2,001,052 at 4.5e-9; LMFDB / Platt for the rest at gamma
2^-50; every ordinate below the PUBLISHED Platt-Trudgian 2021
height T0_PUB = 3.0001753328e12 hence ON the line unconditionally;
the repo constant subg.T0_RH = 3.0e12 <= T0_PUB is the
conservative frozen envelope boundary and is used throughout,
warded; Rosser 1941 corridor; Buethe 2018 baselines).  SPEC
prefixes warded: w2 8db29e6e, subgamma c7d8810c, consume 921140fa,
j16supply deea4e1c, fullclose 9cafc26f, fzt(CCV) 40a7b5c3.
K_ANCH = (7000, 70000, 700000, 2001052, 7000000, 20000000);
H_WARDS = {7000: 254, 2001052: 1256, 2e7: 2806}; CLOSE7 = (16, 0)
exact (verbatim route), ECON2M = (65, 2), FULLB = (67, 8),
UNIFORM7_DEV_MAX = 2, W1_OLD_CERT = 7 exact; GEO_BIG = 1.0002,
E_ODLZ = 4.5e-9, E_LMFDB = gamma 2^-50, NUFFT_EPS = 1e-14, band
edges (gamma_1, 1e4, 3e5, seam, T_c], F_ERR_BAR = 1e-11 (16 spots,
2 anchors: K = 7000 direct + full big direct spot ward), FB_MATCH
= 1e-10 (one full direct big read, smallest support); heart tol =
CXCIII RECON_TOL scaled, soundness tol = CXCIII SOUND_TOL;
DL_GRID = (0.05, 0.10, 0.25, 0.50); Q0_TOL = 1e-6 rel (transform
convention ward at delta = 1e-9); ENV_INFL = 1 + 1e-6 (envelope
soundness at 8 sampled reads x 4 deltas x 12 gammas in
geomspace(50, 1e8)); FIRE_N = 481 points geomspace(T, 1.05 D_env)
on the top-3 reads by D_env per anchor; GRIP_N = 2001 points
geomspace(50, max(4 D_env, 2 T)) on the best read per anchor;
COV_STEP = 0.02, COV_WIDTH = 25.0 (one fine window at 0.4 D_grip,
delta = 0.25, union over the top-8 closed reads); DMIN_GRID = 64
log points 1e-4..0.5; CATCH_FRAC = 0.45, MISS_FRAC = 4.0,
CTRL_NPT = 64, ctrl grid width 4 pi / vmax; SCR_MIN = 5, IMP_BETA
= 0.75, IMP_RATIO_MIN = 10; RATIO_BAR = 1.0, SLOPE_OPEN = 1.0;
CCV_LAW = (-3.045, 1.228, 0.094, 0.90) CITED (log10 T_req vs
ln h: intercept, slope, 2SE, worst residual dex); T0 extrapolation
carries the CCV band + the vmax-fit band (2SE + resmax, added in
dex, declared conservative).  Runtime cap declared: 25 min.
Smoke mode ZWB_SMOKE=1 restricts the surface to kz <= 30,
DEEP_MAX = 2, W1 rows to the 6 shallowest, K_ANCH to the three
historic anchors, and defers the full-only census/H wards
(disclosed prints); controls always full.

SCOUTING DISCLOSURE (2026-08-12, pre-spec): NO scratch scripts
were run for this probe; every sizing input is cited from frozen
predecessors -- the CCV H(T) points and laws (note CCV), the CXCV
M4 impostor mechanics and 8.2e4x shift, the CXCIII heart/residual
anatomy, and the locator lane (CLXXX-CLXXXI region probes,
exclusion_zero_locator_probe LOCATOR-NULL on-sample,
exclusion_zero_locator_v2_probe LOCATOR-V2-RESOLVES out-of-sample
to gamma = 120): the Toeplitz-comb detector is hard-capped by its
lag grid at pi * 64 ~ 201, i.e. it can NEVER reach T-scale heights
regardless of cache size (CITED, why the window-transform detector
is the only scalable lane).  No D value, no frontier, no ratio was
seen before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-12, before freezing): the FIRST
smoke run (ZWB_SMOKE=1) passed 40/40 (exit 0, 24.3 s; 19 surface
rungs kz <= 30, 2 deep, W1 rows = 6, three historic anchors) but
exposed TWO pre-freeze defects, both fixed before the freeze and
disclosed: (i) the T0 extrapolation carried a spurious extra
division by log10(e) in ln H(T0) = (log10 T0 - a)/b, inflating
H(T0) to 4.4e12 and the band to x5.4 (algebra bug, not a bar; the
vmax-fit band was also re-centered on the fit mean abscissa);
(ii) the delta_min probe point 0.5 D_grip was clamped to a floor
ABOVE the smoke grip frontier (nan read); the clamp floor moved
to 20 (gamma_1 scale).  The SECOND smoke run passed 40/40 (exit
0, 27.6 s).  Measured smoke content (subset, not gating):
verbatim 7000 census 14/19 + 0/2; smoke H envelope 364/700/2806;
envelope-soundness worst ratio 0.449; convention ward 5.6e-17;
lowest-anchor D_env 647 (delta 0.5, ratio 8.9e-2), D_fire EMPTY
above T at every anchor, D_grip 64, incoherence gap 10x; guard
sup margin -3.3e-7 < 0 (GUARD-EMPTY); H_sc 0/490/700; T0 row
H(T0) = 3.1e5, ratio 8.0e-5 [4.9e-6..1.3e-3]; controls fire
(scramble 130/150, impostor 8.2e4x, catch 49/64, miss 0/64,
no-false-alarm 0.00); smoke verdict BOOTSTRAP-DEAD.  NO bar,
band, count, rule or enum was moved after the smoke run; the
frozen run repeats everything on the full 67 + 8 + 39 ladder
with all six anchors.

HONEST AMENDMENT (2026-08-12, after frozen run 1, disclosed): the
FIRST frozen run passed 39/40 with every kill ward green (verbatim
16/67 + 0/8, uniform 17/65 + 2/67 + 8, H = 254/1256/2806, heart,
soundness, W1 39/39 + old 7, all detector wards) and FAILED only
the M3 catch control: the synthetic off-line zero was placed BLIND
at 0.45 D_grip = 131.7 on a 64-point window of width 4 pi / vmax,
and the full-ladder grip set is SPARSE (fire fraction below grip
0.05, itself a reported deliverable) -- the window fell in a quiet
stretch (the delta_min probe at 0.5 D_grip read nan for the same
placement reason).  AMENDED RULE (bars unchanged, >= 1 fire on a
fresh 64-point local grid): the catch zero and the delta_min probe
are placed at the MEASURED strongest firing point g_best = argmax
|q|/thr of the declared grip scan (delta 0.5, best read, lowest
anchor; g_best < D_grip by construction, i.e. "below its measured
D" as the catch semantics demand); the fresh local grid around
g_best does not reuse the scan points.  Nothing else moved; the
frozen run was repeated in full.

HONEST SCOPE (stated once, repeated in the verdict): every number
is per-read on the DEPLOYED ladder along the MEASURED critical
direction (CLXXXV DIRECTION-CONDITIONAL verbatim); H(T) and D(H)
say nothing about undeployed windows; exclusion is pointwise on
declared grids (not interval-certified) and always carries a
delta floor > 0 -- the window form never forces zeros ONTO the
line, so even a favorable D would not deliver "RH to D" but only
a far-off-line exclusion strip; the naive D assumes a single
violator (FVI lemma OPEN); the T0 row is a FIT-over-FIT
extrapolation with its bands printed, not a theorem; the
positivity leg below T0 consumes the Platt-Trudgian citation
(audited via H_sc).  A finite zero sum can never prove RH.  NO RH
claim in either direction.  No marker moves, no promotion, no
ledger row; stdout + one JSON data artefact
(zero_window_bootstrap_profile.json) inside experiments/ only.

Sources (read-only): finite_zero_transfer_probe (CCV: anchors,
H(T), heart/censuses machinery -- helper functions reimplemented
verbatim, SPEC prefix warded); w2_pairing_structure_probe (CLXXXV
ladder); w2_verified_supply_consumption_probe (CXCIII: phi_cont_of,
direct_read, hat_seg_c, zsum4re, tail_grid);
w2_full_zero_closure_probe (CXCV read set / NUFFT supply path);
j16_verified_zero_supply_probe (CLXXXIX W1 supply);
subgamma_fourier_bound_probe (corridor / Abel / s2_tail / T0);
exterior_pg_schur_probe, bfloor_pg_dominance_probe,
w1_assembly_certificate_probe (W1 assembly);
exclusion_zero_locator_probe / _v2 (CITED comb-detector lane).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zero_window_bootstrap_probe.py
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
import finite_zero_transfer_probe as ccv  # noqa: E402  (READ-ONLY)

SMOKE = os.environ.get("ZWB_SMOKE", "") == "1"

ZC7_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
ZCB_NPY = os.path.join(_HERE, "verified_zeros_big.npy")
ZCB_META = os.path.join(_HERE, "verified_zeros_big_meta.json")
OUT_JSON = os.path.join(_HERE, "zero_window_bootstrap_profile.json")
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
CORR_EPS = 1.0e-6
T0_PUB = 3.0001753328e12
K_ANCH_FULL = (7000, 70000, 700000, SEAM_N, 7_000_000, N_ZB)
K_ANCH_SMOKE = (7000, SEAM_N, N_ZB)
H_WARDS = {7000: 254, SEAM_N: 1256, N_ZB: 2806}
CLOSE7 = (16, 0)
ECON2M = (65, 2)
FULLB = (67, 8)
UNIFORM7_DEV_MAX = 2
W1_OLD_CERT = 7
DL_GRID = (0.05, 0.10, 0.25, 0.50)
Q0_TOL = 1.0e-6
ENV_INFL = 1.0 + 1.0e-6
ENV_READS = 8
ENV_GAMMAS = 12
FIRE_N = 481
FIRE_TOP = 3
GRIP_N = 2001
GRIP_LO = 50.0
COV_STEP = 0.02
COV_WIDTH = 25.0
COV_READS = 8
DMIN_N = 64
CATCH_FRAC = 0.45
MISS_FRAC = 4.0
CTRL_NPT = 64
SCR_MIN = 5
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
RATIO_BAR = 1.0
SLOPE_OPEN = 1.0
CCV_LAW = (-3.045, 1.228, 0.094, 0.90)
CUT_A = w2.HEAD_A
CTRL_KZ = w2.CTRL_KZ
KZ_TOP = 30 if SMOKE else w2.KZMAX
DEEP_MAX = 2 if SMOKE else 8
N_SURF = 67
N_DEEP = 8
W1_ROWS = 6 if SMOKE else 39
K_ANCH = K_ANCH_SMOKE if SMOKE else K_ANCH_FULL
PREFIXES = dict(w2="8db29e6e", subgamma="c7d8810c",
                consume="921140fa", j16supply="deea4e1c",
                fullclose="9cafc26f", fzt="40a7b5c3")

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


def hat_vec(pc, s_arr):
    """cons.hat_seg_c vectorized over an array of complex s
    (Int phi(u) e^{su} du, per-segment closed form)."""
    edges = pc["edges"]
    fvals = pc["fvals"]
    slopes = pc["slopes"]
    s = np.asarray(s_arr, complex)[:, None]
    iz = 1.0 / s
    val = (np.exp(s * edges[1:])
           * (fvals[1:] * iz - slopes * iz ** 2)
           - np.exp(s * edges[:-1])
           * (fvals[:-1] * iz - slopes * iz ** 2))
    return val.sum(axis=1)


def q_add(pc, dl, gam_arr):
    """Contribution of a hypothetical zero quadruple at
    (1/2 + dl, gamma) to PARITH (orientation of the CXCV M4
    impostor); the detector consumes |q_add|."""
    g = np.asarray(gam_arr, float)
    return -4.0 * (hat_vec(pc, dl + 1j * g)
                   + hat_vec(pc, -dl + 1j * g)).real


def env_q(pc, dl, gam_arr):
    """Rigorous per-quadruple envelope: |q| <= 4 (e^{dl vmax} + 1)
    (sd / g^2 + |fend| / g)."""
    g = np.asarray(gam_arr, float)
    amp = 4.0 * (math.exp(dl * pc["vmax"]) + 1.0)
    return amp * (pc["sd"] / g ** 2 + abs(pc["fend"]) / g)


def d_env_of(pc, dl, thr):
    """Envelope crossing gamma: solve amp (sd/g^2 + fend/g) = thr
    (positive root; the OPTIMISTIC frontier bound)."""
    amp = 4.0 * (math.exp(dl * pc["vmax"]) + 1.0)
    fe = abs(pc["fend"])
    disc = (amp * fe) ** 2 + 4.0 * thr * amp * pc["sd"]
    return (amp * fe + math.sqrt(disc)) / (2.0 * thr)


def jack_fit(x, y):
    b, se, r2 = w2.jack_slope(np.asarray(x, float),
                              np.asarray(y, float))
    a = float(np.mean(y)) - b * float(np.mean(x))
    res = np.asarray(y, float) - (a + b * np.asarray(x, float))
    return a, b, se, r2, float(np.max(np.abs(res)))


def main():
    section("PRIME.ZERO.WINDOW.BOOTSTRAP.01 -- D(H(T))/T, the "
            "go/no-go for the zero-window bootstrap (EXPLORATION "
            "ONLY)")
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
            fzc.__doc__.encode("utf-8")).hexdigest(),
        fzt=hashlib.sha256(ccv.__doc__.encode("utf-8")).hexdigest())
    for tag in sorted(shas):
        print("    %-9s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): Odlyzko zeta_tables "
          "zeros6 (n <= %d, 4.5e-9); LMFDB / Platt (n <= %d, "
          "gamma 2^-50);" % (SEAM_N, N_ZB))
    print("      Platt-Trudgian 2021 T0_PUB = %.10e (published "
          "verification height; repo envelope boundary T0_RH = "
          "%.4e <= T0_PUB, conservative);" % (T0_PUB, subg.T0_RH))
    print("      Rosser 1941 N(T) corridor; Buethe 2018 (cited "
          "baselines).  Comb-detector lane CITED: locator v2 "
          "grip to gamma = 120, lag-grid cap pi*64 ~ 201.")
    if SMOKE:
        print("    *** SMOKE MODE: kz <= %d, DEEP_MAX = %d, W1 "
              "rows = %d, anchors = %s, full-only wards deferred "
              "***" % (KZ_TOP, DEEP_MAX, W1_ROWS, list(K_ANCH)))
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
    check("S0d repo T0 boundary below the published height "
          "(%.4e <= %.10e)" % (subg.T0_RH, T0_PUB),
          subg.T0_RH <= T0_PUB, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Z
    section("Z -- both verified-zero caches, wards, anchor table")
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
    K_GRID = [int(k) for k in K_ANCH]
    NG = len(K_GRID)
    i_7000 = K_GRID.index(N_Z7)
    i_2m = K_GRID.index(SEAM_N)
    i_big = K_GRID.index(N_ZB)
    t_anch = np.array([float(gamb[k - 1]) for k in K_GRID])
    print("    anchors: %s" % ", ".join(
        "K=%d T=%.4e" % (K_GRID[i], t_anch[i]) for i in range(NG)))
    e_k = np.empty(N_ZB)
    e_k[:SEAM_N] = E_ODLZ
    e_k[SEAM_N:] = gamb[SEAM_N:] * E_LMFDB_ULP
    idxg = np.array(K_GRID) - 1
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
    print("    prefix error sums + Abel table done  [%.1f s]"
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
    fe_max = max(abs(rd["pc"]["fend"]) for rd in reads)
    print("    %d reads, %d unique jump abscissae, max |fend| = "
          "%.2e  [%.1f s]" % (NR, len(v_all), fe_max,
                              time.time() - T0))

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
    section("B -- W2 prefix supply at the %d anchors" % NG)
    zs_mat = np.zeros((NR, NG))
    F_cum = np.zeros(len(v_all))
    k_prev = 0
    Jv = [(rd["pc"]["J"], rd["vidx"]) for rd in reads]
    F_at = {}
    for i, K in enumerate(K_GRID):
        F_cum = F_cum + f_transform(gamb[k_prev:K], v_all)
        k_prev = K
        if K in (N_Z7, N_ZB):
            F_at[K] = F_cum.copy()
        for jr, (J, vidx) in enumerate(Jv):
            zs_mat[jr, i] = -4.0 * float(J @ F_cum[vidx])
        print("    ... anchor %d/%d (K = %d)  [%.1f s]"
              % (i + 1, NG, K, time.time() - T0), flush=True)
    sp_idx = np.unique(np.geomspace(1, len(v_all),
                                    NW_SPOTS).astype(int)) - 1
    fdev = 0.0
    for K in (N_Z7, N_ZB):
        Fd = f_direct(gamb[:K], v_all[sp_idx])
        fdev = max(fdev, float(np.max(np.abs(
            F_at[K][sp_idx] - Fd))))
    check("B1 NUFFT spot ward: worst |F_cum - F_direct| %.2e <= "
          "%.0e at %d spots x 2 anchors (K = 7000, 2e7)"
          % (fdev, F_ERR_BAR, len(sp_idx)), fdev <= F_ERR_BAR,
          kill="K3")
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
    heart = -1e18
    sound = 0
    mcert = np.zeros((NR, NG))
    mc_sc = np.zeros((NR, NG))
    r_meas = np.zeros((NR, NG))
    thr_n = np.zeros((NR, NG))
    thr_g = np.zeros((NR, NG))
    for jr, rd in enumerate(reads):
        pc, sp, r = rd["pc"], rd["sp"], rd["r"]
        sd = pc["sd"]
        evh = math.exp(0.5 * pc["vmax"])
        ph = (-zs_mat[jr] - pc["triv"] - pc["ramp_at"]
              + pc["ramp_cont"] + pc["ext_cont"] - pc["ext_at"])
        ord_pad = 4.0 * sd * (pc["vmax"] * se2_a + 2.0 * se3_a)
        pads = ord_pad + 4.0 * sd * F_ERR_BAR \
            + cons.RECON_TOL * (1.0 + abs(sp["t_int"])) \
            + 1e-12 * (1.0 + abs(pc["triv"]))
        tb = (4.0 * sd * abel_a + 4.0 * evh * sd * s2t
              + ord_pad + 4.0 * sd * F_ERR_BAR
              + 1e-12 * (1.0 + abs(pc["triv"])))
        tb_sc = (4.0 * sd * evh * (abel_a + s2t)
                 + ord_pad + 4.0 * sd * F_ERR_BAR
                 + 1e-12 * (1.0 + abs(pc["triv"])))
        mcert[jr] = sp["fc"] + ph - tb
        mc_sc[jr] = sp["fc"] + ph - tb_sc
        r_meas[jr] = np.abs(sp["par"] - ph)
        thr_n[jr] = r_meas[jr] + pads + 4.0 * sd * (abel_a + s2t)
        thr_g[jr] = r_meas[jr] + pads + 4.0 * sd * evh \
            * (abel_a + s2t)
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
    all_r = [(r, False) for r in rungs] + [(r, True)
                                           for r in deep_rows]
    cen_s = np.zeros(NG, int)
    cen_d = np.zeros(NG, int)
    cen_s_sc = np.zeros(NG, int)
    cen_d_sc = np.zeros(NG, int)
    closed_of = {}
    for r, is_deep in all_r:
        jr_mine = [j for j, rd in enumerate(reads)
                   if rd["r"] is r]
        closed = np.any(mcert[jr_mine] > 0.0, axis=0)
        closed_sc = np.any(mc_sc[jr_mine] > 0.0, axis=0)
        closed_of[id(r)] = closed
        if is_deep:
            cen_d += closed.astype(int)
            cen_d_sc += closed_sc.astype(int)
        else:
            cen_s += closed.astype(int)
            cen_s_sc += closed_sc.astype(int)
    print("    uniform censuses: 7000 %d + %d (verbatim %d + %d); "
          "2M %d + %d; 2e7 %d + %d"
          % (cen_s[i_7000], cen_d[i_7000], n_s7v, n_d7v,
             cen_s[i_2m], cen_d[i_2m], cen_s[i_big],
             cen_d[i_big]))
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

    # ------------------------------------------------------------ C
    section("C -- W1 face at the 7000 cache (CLXXXIX chain)")
    zones, truth, full, prows = parent.build_truth_rows()
    check("C1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(prows) == 39,
          kill="K1")
    if KILLS:
        return finish({})
    for w in prows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    lam_w1 = j16.deep.build_ext_tables()
    NN_e = j16.deep.EXT["NN"]
    psi_e = np.cumsum(lam_w1[NN_e])
    j16.lf.ENV.update(j16.lf.table_sups(NN_e, psi_e,
                                        j16.deep.TAB_EXT))
    check("C1b Buethe envelope warded (sup %.4f <= %.2f)"
          % (j16.lf.ENV["BUETHE_SUP"], j16.lf.BUETHE),
          j16.lf.ENV["BUETHE_SUP"] <= j16.lf.BUETHE, kill="K2")
    use = prows[:W1_ROWS]
    n_old = 0
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
        n_old += int(bool(pa["vpos"] and pa["floor"] > w["mu1"]))
        ex = j16.rung_exact(rr["alpha"], rr["M"], rb["D"],
                            rb["L"], gam7, s2t)
        pn = j16.rung_assembly_new(rb, ex, r2["y_core"],
                                   r2["v_core"], r2["h"],
                                   w["Gc"], w["mu1"])
        n_new7 += int(pn is not None and pn["cert"])
        if (iw + 1) % 10 == 0:
            print("    ... %d/%d W1 rows  [%.1f s]"
                  % (iw + 1, len(use), time.time() - T0),
                  flush=True)
    check("C2 W1 old-tier census %d %s" % (n_old, "== 7"
          if not SMOKE else "(smoke subset)"),
          (n_old == W1_OLD_CERT) if not SMOKE else True,
          kill="K2" if not SMOKE else None)
    check("C3 W1 new census at K = 7000: %d/%d (CLXXXIX 39/39)"
          % (n_new7, len(use)), n_new7 == len(use), kill="K2")
    print("    W1 T_req: CITED CCV max 5350 <= gamma_7000 = %.1f "
          "< every anchor; deep W1 zero-free (CLXXXIV CITED "
          "28/28); wall closure at the anchors is W2-decided."
          % t_c7)

    # ------------------------------------------------------------ H
    section("H -- the transfer curve H(T) + the self-contained "
            "audit H_sc(T)")
    hh = sorted(all_r, key=lambda t: (t[0]["h"], t[0]["kz"]))

    def envelope_h(col, mat_closed):
        hmax = 0
        for r, _d in hh:
            if mat_closed[id(r)][col]:
                hmax = int(r["h"])
            else:
                break
        return hmax

    closed_sc_of = {}
    for r, is_deep in all_r:
        jr_mine = [j for j, rd in enumerate(reads)
                   if rd["r"] is r]
        closed_sc_of[id(r)] = np.any(mc_sc[jr_mine] > 0.0, axis=0)
    H_j = [envelope_h(i, closed_of) for i in range(NG)]
    Hsc_j = [envelope_h(i, closed_sc_of) for i in range(NG)]
    for i in range(NG):
        print("    T = %.4e (K = %8d): H = %-5d closed %2d + %d | "
              "H_sc = %-5d closed_sc %2d + %d"
              % (t_anch[i], K_GRID[i], H_j[i], cen_s[i], cen_d[i],
                 Hsc_j[i], cen_s_sc[i], cen_d_sc[i]))
    if not SMOKE:
        ok_h = all(H_j[K_GRID.index(k)] == H_WARDS[k]
                   for k in H_WARDS)
        check("H1 CCV H(T) points reproduced (254 / 1256 / 2806)",
              ok_h, "measured %s" % [H_j[K_GRID.index(k)]
                                     for k in sorted(H_WARDS)],
              kill="K2")
    else:
        check("H1 deferred in smoke (H envelope %s on the subset)"
              % H_j, True)
    print("    SELF-CONTAINED AUDIT: the deployed TAILB assumes "
          "zeros in (T, T0] ON the line (Platt-Trudgian CITED); "
          "a bootstrap stage at frontier T may not -- H_sc above "
          "is the beta-unassumed-closure depth (W2 face; upper "
          "bound, W1 face untreated).")

    # ------------------------------------------------------------ D
    section("D -- the detector: sensitivity, frontiers, guard")
    rd9 = next(rd for rd in reads if rd["r"]["kz"] == CTRL_KZ
               and rd["key"] == ("cB", 0))
    pc9 = rd9["pc"]
    g1 = float(gam7[0])
    q0 = float(q_add(pc9, 1.0e-9, [g1])[0])
    onp = 4.0 * float((-np.sum(
        pc9["J"] * np.exp(1j * g1 * pc9["v"])) / g1 ** 2).real)
    dev_q0 = abs(0.5 * q0 - (-onp)) / max(1.0, abs(onp))
    check("D1 transform convention ward |q(1e-9)/2 - onpair| = "
          "%.1e rel <= %.0e (J-form vs hat_seg form at gamma_1)"
          % (dev_q0, Q0_TOL), dev_q0 <= Q0_TOL, kill="K3")
    idx_env = np.unique(np.geomspace(1, NR, ENV_READS).astype(int)
                        ) - 1
    genv = np.geomspace(GRIP_LO, 1.0e8, ENV_GAMMAS)
    worst_env = 0.0
    for je in idx_env:
        pc = reads[je]["pc"]
        for dl in DL_GRID:
            ratio = np.abs(q_add(pc, dl, genv)) \
                / env_q(pc, dl, genv)
            worst_env = max(worst_env, float(np.max(ratio)))
    check("D2 envelope soundness |q| <= env (worst ratio %.6f <= "
          "%.6f at %d reads x %d deltas x %d gammas)"
          % (worst_env, ENV_INFL, len(idx_env), len(DL_GRID),
             ENV_GAMMAS), worst_env <= ENV_INFL, kill="K3")
    # per-anchor frontiers over reads of rungs with h <= H(T_j)
    tab = []
    prof_json = []
    for i in range(NG):
        Tj = float(t_anch[i])
        elig = [(jr, rd) for jr, rd in enumerate(reads)
                if rd["r"]["h"] <= H_j[i]
                and closed_of[id(rd["r"])][i]]
        if not elig:
            tab.append(dict(T=Tj, H=H_j[i], i=i, empty=True))
            continue
        best = {}
        for dl in DL_GRID:
            d_env = [(d_env_of(rd["pc"], dl, thr_n[jr, i]), jr)
                     for jr, rd in elig]
            d_env.sort(reverse=True)
            best[dl] = d_env
        dl_star = 0.50
        d_top = best[dl_star][0][0]
        jr_top = best[dl_star][0][1]
        # guarded frontier: envelope vs guarded threshold beyond T
        g_sup = -1e18
        d_guard = 0.0
        for jr, rd in elig:
            pc = rd["pc"]
            m0 = float(env_q(pc, 0.5, [Tj * 1.0001])[0]) \
                - thr_g[jr, i]
            g_sup = max(g_sup, m0)
            dg = d_env_of(pc, 0.5, thr_g[jr, i])
            d_guard = max(d_guard, dg if dg > Tj else 0.0)
        # fire scan above T (top reads by D_env)
        d_fire = 0.0
        n_fire = 0
        for de, jr in best[dl_star][:FIRE_TOP]:
            pc = reads[jr]["pc"]
            hi = max(1.05 * de, 1.01 * Tj)
            gg = np.geomspace(Tj * 1.0001, hi, FIRE_N)
            fires = np.abs(q_add(pc, dl_star, gg)) > thr_n[jr, i]
            n_fire += int(np.sum(fires))
            if np.any(fires):
                d_fire = max(d_fire, float(np.max(gg[fires])))
        # grip scan (full range, instrument sensitivity)
        pc_t = reads[jr_top]["pc"]
        gg = np.geomspace(GRIP_LO, max(4.0 * d_top, 2.0 * Tj),
                          GRIP_N)
        fg = np.abs(q_add(pc_t, dl_star, gg)) > thr_n[jr_top, i]
        d_grip = float(np.max(gg[fg])) if np.any(fg) else 0.0
        frac_g = float(np.mean(fg[gg <= max(d_grip, GRIP_LO)])) \
            if np.any(fg) else 0.0
        reach = max(math.pi / rd["r"]["D"] for _jr, rd in elig)
        tab.append(dict(T=Tj, K=K_GRID[i], H=H_j[i], i=i,
                        Hsc=Hsc_j[i], d_env=d_top,
                        d_fire=d_fire, n_fire=n_fire,
                        d_grip=d_grip, frac_g=frac_g,
                        d_guard=d_guard, g_sup=g_sup,
                        jr_top=jr_top, reach=reach,
                        ratio=d_top / Tj, empty=False,
                        d_env_by_dl={dl: best[dl][0][0]
                                     for dl in DL_GRID}))
        prof_json.append(dict(T=Tj, K=K_GRID[i], H=H_j[i],
                              Hsc=Hsc_j[i], d_env=d_top,
                              d_fire=d_fire, d_grip=d_grip,
                              d_guard=d_guard,
                              ratio=d_top / Tj))
    row0 = next(x for x in tab if not x.get("empty"))
    pc0 = reads[row0["jr_top"]]["pc"]
    i0 = row0["i"]
    thr0 = float(thr_n[row0["jr_top"], i0])
    # measured strongest firing point of the grip scan (AMENDED
    # placement for the delta_min probe and the M3 catch control)
    gg0 = np.geomspace(GRIP_LO, max(4.0 * row0["d_env"],
                                    2.0 * row0["T"]), GRIP_N)
    rat0 = np.abs(q_add(pc0, 0.5, gg0)) / thr0
    g_best = float(gg0[int(np.argmax(rat0))])
    # delta_min profile at the strongest grip point
    g_at = g_best
    wdt = 4.0 * math.pi / pc0["vmax"]
    gg_c = np.linspace(g_at - 0.5 * wdt, g_at + 0.5 * wdt,
                       CTRL_NPT)
    dl_fine = np.geomspace(1.0e-4, 0.5, DMIN_N)
    dmin = float("nan")
    for dl in dl_fine:
        if np.any(np.abs(q_add(pc0, float(dl), gg_c)) > thr0):
            dmin = float(dl)
            break
    # local coverage at the grip height (union of top reads)
    cov_lo = max(0.4 * row0["d_grip"], GRIP_LO)
    gg_cov = np.arange(cov_lo, cov_lo + COV_WIDTH, COV_STEP)
    covered = np.zeros(len(gg_cov), bool)
    elig0 = [(jr, rd) for jr, rd in enumerate(reads)
             if rd["r"]["h"] <= H_j[i0]
             and closed_of[id(rd["r"])][i0]]
    for jr, rd in sorted(
            elig0, key=lambda t: -t[1]["pc"]["vmax"])[:COV_READS]:
        covered |= (np.abs(q_add(rd["pc"], 0.25, gg_cov))
                    > thr_n[jr, i0])
    cov_frac = float(np.mean(covered))
    gaps = np.flatnonzero(~covered)
    max_gap = 0.0
    if len(gaps):
        brk = np.flatnonzero(np.diff(gaps) > 1)
        seg = np.split(gaps, brk + 1)
        max_gap = max(len(s) for s in seg) * COV_STEP
    print("    SENSITIVITY PROFILE (lowest anchor T = %.4e, best "
          "read kz %d, vmax %.2f, sd %.3e):"
          % (row0["T"], reads[row0["jr_top"]]["r"]["kz"],
             pc0["vmax"], pc0["sd"]))
    for dl in DL_GRID:
        print("      delta = %.2f: D_env = %.4e  (D_env/T = "
              "%.3e)" % (dl, row0["d_env_by_dl"][dl],
                         row0["d_env_by_dl"][dl] / row0["T"]))
    print("      D_grip (measured, delta 0.5) = %.4e; fire "
          "fraction below grip %.2f; incoherence gap D_env/"
          "D_grip = %.1f" % (row0["d_grip"], row0["frac_g"],
                             row0["d_env"]
                             / max(row0["d_grip"], 1.0)))
    print("      strongest grip point g_best = %.1f (|q|/thr = "
          "%.1f); delta_min there: %.4f (fine grid 1e-4..0.5) -- "
          "the exclusion has a delta floor at gamma > T (M5); "
          "D_strict = 0 identically (typed: the window form "
          "never forces zeros ONTO the line)"
          % (g_best, float(np.max(rat0)), dmin))
    print("      local coverage at the grip height (delta 0.25, "
          "%d reads, %.0f wide, step %.2f): %.1f%% covered, max "
          "gap %.2f -- exclusion is pointwise, NOT an interval "
          "certificate" % (COV_READS, COV_WIDTH, COV_STEP,
                           100 * cov_frac, max_gap))
    check("D3 frontiers measured at every anchor "
          "(guard sup margin %.2e %s 0 at the top anchor)"
          % (tab[-1]["g_sup"],
             "<" if tab[-1]["g_sup"] < 0 else ">="), True)

    # ------------------------------------------------------------ T
    section("T -- THE TABLE: T / H(T) / D(H(T)) / ratio + the T0 "
            "extrapolation")
    print("    %12s %6s %6s %11s %11s %11s %9s %11s %9s"
          % ("T", "H", "H_sc", "D_env", "D_fire", "D_grip",
             "ratio", "D_guard", "reach"))
    for x in tab:
        if x.get("empty"):
            print("    %12.4e %6d  (no closed rungs)"
                  % (x["T"], x["H"]))
            continue
        print("    %12.4e %6d %6d %11.4e %11.4e %11.4e %9.2e "
              "%11.4e %9.2e"
              % (x["T"], x["H"], x["Hsc"], x["d_env"],
                 x["d_fire"], x["d_grip"], x["ratio"],
                 x["d_guard"], x["reach"]))
    rows_fit = [x for x in tab if not x.get("empty")]
    lx = np.log10([x["T"] for x in rows_fit])
    ly = np.log10([x["d_env"] for x in rows_fit])
    a_p, b_p, se_p, r2_p, rmax_p = jack_fit(lx, ly)
    print("    frontier law: log10 D_env = %+.3f %+.3f log10 T  "
          "(2SE %.3f, R^2 %.3f, resmax %.2f dex, n = %d)"
          % (a_p, b_p, 2 * se_p, r2_p, rmax_p, len(rows_fit)))
    print("    ratio law: D_env/T ~ T^%+.3f -- %s"
          % (b_p - 1.0, "FALLING (the frontier loses ground)"
             if b_p < 1.0 else "growing"))
    # vmax growth on the deployed ladder (all reads, best per rung)
    vm_h = {}
    for rd in reads:
        h = int(rd["r"]["h"])
        vm_h[h] = max(vm_h.get(h, 0.0), rd["pc"]["vmax"])
    lh = np.log(sorted(vm_h))
    vv = np.array([vm_h[h] for h in sorted(vm_h)])
    a_v, b_v, se_v, r2_v, rmax_v = jack_fit(lh, vv)
    print("    window growth: vmax = %+.3f %+.3f ln h  (2SE %.3f, "
          "R^2 %.3f, resmax %.2f)" % (a_v, b_v, 2 * se_v, r2_v,
                                      rmax_v))
    # T0 extrapolation (CITED CCV law + measured vmax law)
    ca, cb, c2se, cres = CCV_LAW
    lnH0 = (math.log10(T0_PUB) - ca) / cb
    dlnH = cres / cb
    H0 = math.exp(lnH0)
    vm0 = a_v + b_v * lnH0
    dvm = (2 * se_v) * abs(lnH0 - float(np.mean(lh))) \
        + rmax_v + b_v * dlnH
    d0 = math.sqrt((math.exp(0.5 * vm0) + 1.0) / s2t)
    d0_hi = math.sqrt((math.exp(0.5 * (vm0 + dvm)) + 1.0) / s2t)
    d0_lo = math.sqrt((math.exp(0.5 * max(vm0 - dvm, 0.0)) + 1.0)
                      / s2t)
    print("    T0 row (Platt-Trudgian %.10e):" % T0_PUB)
    print("      H(T0) = %.3e (CCV law, band x/%.1f..x%.1f); "
          "vmax(H(T0)) = %.2f +- %.2f"
          % (H0, math.exp(dlnH), math.exp(dlnH), vm0, dvm))
    print("      D_env(H(T0)) = %.3e (band %.3e .. %.3e; r_meas "
          "-> 0 FAVORABLE, sd cancels)" % (d0, d0_lo, d0_hi))
    print("      D_env(H(T0)) / T0 = %.3e (band %.3e .. %.3e)"
          % (d0 / T0_PUB, d0_lo / T0_PUB, d0_hi / T0_PUB))
    ratio_max = max(x["ratio"] for x in rows_fit)
    check("T1 table + laws + T0 extrapolation recorded "
          "(max measured ratio %.3e, T0 ratio %.3e)"
          % (ratio_max, d0 / T0_PUB), True)
    with open(OUT_JSON, "w") as fh:
        json.dump(dict(anchors=prof_json,
                       frontier_law=dict(a=a_p, b=b_p,
                                         se2=2 * se_p, r2=r2_p),
                       vmax_law=dict(a=a_v, b=b_v, se2=2 * se_v),
                       t0=dict(T0=T0_PUB, H0=H0, d_env=d0,
                               band=[d0_lo, d0_hi],
                               ratio=d0 / T0_PUB),
                       ratio_max=ratio_max,
                       spec_sha=hashlib.sha256(
                           __doc__.encode()).hexdigest()), fh)
    print("    profile data -> zero_window_bootstrap_profile.json")

    # ------------------------------------------------------------ M
    section("M -- controls (must fire)")
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
          "on %d/%d reads at N = 7000 (>= %d) -- r_meas is "
          "heart-guarded" % (n_broken, NR, SCR_MIN),
          n_broken >= SCR_MIN, kill="K2")
    dlt = IMP_BETA - 0.5
    on_pair = 4.0 * float((-np.sum(
        pc9["J"] * np.exp(1j * g1 * pc9["v"])) / g1 ** 2).real)
    quad = 4.0 * (cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                 pc9["slopes"],
                                 dlt + 1j * g1).real
                  + cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                   pc9["slopes"],
                                   -dlt + 1j * g1).real)
    shift = abs((-quad) - (-on_pair))
    resid9 = abs(rd9["sp"]["par"] - rd9["ph7v"])
    ratio_i = shift / max(resid9, 1e-300)
    check("M2 CONTROL: off-line impostor (gamma_1 -> beta %.2f) "
          "shifts PARITH_hat by %.4f = %.1e x the genuine 7000 "
          "residual (>= %.0f)" % (IMP_BETA, shift, ratio_i,
                                  IMP_RATIO_MIN),
          ratio_i >= IMP_RATIO_MIN, kill="K2")
    gg_cat = np.linspace(g_best - 0.5 * wdt, g_best + 0.5 * wdt,
                         CTRL_NPT)
    n_cat = int(np.sum(np.abs(q_add(pc0, 0.5, gg_cat)) > thr0))
    check("M3 CONTROL: synthetic off-line zero (delta 0.5) at "
          "the measured grip point g_best = %.1f (< D_grip = "
          "%.1f) caught on %d/%d fresh grid points (>= 1)"
          % (g_best, row0["d_grip"], n_cat, CTRL_NPT), n_cat >= 1,
          kill="K2")
    g_mis = MISS_FRAC * row0["d_env"]
    gg_mis = np.linspace(g_mis - 0.5 * wdt, g_mis + 0.5 * wdt,
                         CTRL_NPT)
    n_mis = int(np.sum(np.abs(q_add(pc0, 0.5, gg_mis))
                       > thr_n[row0["jr_top"], i0]))
    check("M4 CONTROL: beyond the envelope frontier (4 D_env = "
          "%.3e) fires %d/%d (== 0)" % (g_mis, n_mis, CTRL_NPT),
          n_mis == 0, kill="K2")
    worst_fa = 0.0
    for jr, rd in enumerate(reads):
        for i in range(NG):
            fa = abs(float(q_add(rd["pc"], 0.0,
                                 [1.01 * t_anch[i]])[0])) \
                / thr_n[jr, i]
            worst_fa = max(worst_fa, fa)
    check("M5 CONTROL: no false alarm on the on-line reading at "
          "gamma = 1.01 T (worst |q(0)|/thr = %.3f < 1 over %d x "
          "%d cells)" % (worst_fa, NR, NG), worst_fa < 1.0,
          kill="K2")

    # ------------------------------------------------------ verdicts
    v1 = ("SUPPLY-WARDS-REPRODUCED(H %s; 7000 verbatim %d + %d; "
          "2M %d + %d; 2e7 %d + %d; W1 %d/%d + old %d)"
          % ("/".join(str(h) for h in H_j), n_s7v, n_d7v,
             cen_s[i_2m], cen_d[i_2m], cen_s[i_big], cen_d[i_big],
             n_new7, len(use), n_old))
    v2 = ("DETECTOR-PROFILE-MEASURED(top anchor: D_env %.3e / "
          "D_fire %.3e / D_grip %.3e at delta 0.5; incoherence "
          "gap %.0f; delta_min %.3f; coverage %.0f%%, max gap "
          "%.2f)" % (tab[-1]["d_env"], tab[-1]["d_fire"],
                     tab[-1]["d_grip"],
                     row0["d_env"] / max(row0["d_grip"], 1.0),
                     dmin, 100 * cov_frac, max_gap))
    guard_top = tab[-1]["d_guard"] / tab[-1]["T"]
    if all(x["ratio"] < RATIO_BAR for x in rows_fit):
        v3 = ("BOOTSTRAP-DEAD(max ratio %.3e < 1 at every anchor; "
              "law D_env ~ T^%+.3f i.e. ratio ~ T^%+.3f; T0 ratio "
              "%.3e [%.1e..%.1e]; the kill criterion fires: even "
              "the optimistic single-violator envelope frontier "
              "never reaches the verified height -- bigger caches "
              "are finite verification only, the route is buried)"
              % (ratio_max, b_p, b_p - 1.0, d0 / T0_PUB,
                 d0_lo / T0_PUB, d0_hi / T0_PUB))
    elif guard_top > RATIO_BAR and b_p >= SLOPE_OPEN:
        v3 = ("BOOTSTRAP-OPEN(guarded ratio %.3e > 1 at the top "
              "anchor, slope %+.3f >= 1: iterating RH(T) -> "
              "H(T) -> D > T would advance the frontier)"
              % (guard_top, b_p))
    else:
        v3 = ("BOOTSTRAP-CONDITIONAL(naive ratio %.3e > 1 "
              "somewhere but guarded %.3e <= 1: the route needs "
              "the FVI lemma spec'd in the header -- strip-"
              "positivity of the deployed window transform off "
              "the line, RH-hard flavor, OPEN)"
              % (ratio_max, guard_top))
    v4 = ("%s + SELF-CONTAINED-POSITIVITY(H_sc %s: the deployed "
          "positivity leg consumes the T0 citation below T0)"
          % (("GUARD-EMPTY(sup margin %.2e < 0 beyond T)"
              % tab[-1]["g_sup"]) if tab[-1]["d_guard"] <= 0.0
             else "GUARD-NONEMPTY(D_guard %.3e)"
             % tab[-1]["d_guard"],
             "/".join(str(h) for h in Hsc_j)))
    if n_broken >= SCR_MIN and ratio_i >= IMP_RATIO_MIN \
            and n_cat >= 1 and n_mis == 0 and worst_fa < 1.0:
        v5 = ("DISCRIMINATION-FIRES(scramble %d reads, impostor "
              "%.0e x, catch %d/%d, miss 0, no-false-alarm %.2f)"
              % (n_broken, ratio_i, n_cat, CTRL_NPT, worst_fa))
    else:
        v5 = ("DISCRIMINATION-UNRESOLVED(scr %d, imp %.1f, catch "
              "%d, miss %d, fa %.2f)"
              % (n_broken, ratio_i, n_cat, n_mis, worst_fa))
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
  HONEST SCOPE: (i) per-read, deployed 67 + 8 (+ 39 W1) ladder,
  MEASURED critical direction (CLXXXV DIRECTION-CONDITIONAL);
  (ii) exclusion is pointwise on declared grids, never interval-
  certified, and always carries a delta floor > 0: the window form
  never forces zeros ONTO the line, so even a favorable D would
  deliver a far-off-line exclusion strip, not "RH to D";
  (iii) the naive D assumes a SINGLE violator -- without the FVI
  lemma (spec in header, RH-hard flavor, OPEN) only the guarded D
  counts; (iv) H(T) below T0 consumes the Platt-Trudgian citation
  (audited: H_sc); (v) the T0 row is a fit-over-fit extrapolation
  with printed bands, not a theorem; (vi) inputs = cited verified
  zeros + unconditional envelopes (Rosser corridor, Abel,
  beta-unassumed beyond T0) + exact composition; a finite zero sum
  can never prove RH; the all-h, all-direction Weil-positivity
  object remains OPEN and RH-hard in every branch; NO RH claim in
  either direction.  No marker moves, no promotion, no ledger row;
  stdout + one JSON artefact inside experiments/ only.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
