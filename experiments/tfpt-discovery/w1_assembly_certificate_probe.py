#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w1_assembly_certificate_probe -- PRIME.PORT.W1.ASSEMBLY.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE ASSEMBLY.  Two independently frozen
halves now exist and have never been run against each other:
  (I)  the SUPPLY (CLXXXI, subgamma_fourier_bound_probe, SPEC-SHA
       c7d8810c..): the explicit sub-gamma_1 Fourier bound of the
       psi-error delivers, per rung and per fold read, the
       unconditional classical bound  |d_at_f - MAIN_f| = |R_true_f|
       <= SUP_F_f  (fold-flat med 5.7..7.6), combined by min with
       the Buethe finite-range route SUP_B_f (lowfreq verbatim);
       at the 8 core folds this closes the v-floor H_f > SUP_MIN_f
       on 7/39 surface + 28/28 deep rungs.
  (II) the COMPOSITION (CLXXXII/CLXXXIII, monotone_composition_
       probe SPEC-SHA bed53f23.. + vfloor_headroom_probe SPEC-SHA
       9ffe771d..): lambda_min(G_core) >= lambda_min(V^{1/2}
       K^omega V^{1/2}) by the dual/Loewner measure inequality
       [L2] (composition price +0.29 dex), the bound is v-monotone
       [L5] so a v-floor substitutes with ZERO further loss, and
       the DEMAND TABLE says a per-fold bound c|d_f - d^ar_f| on
       folds f <= 32 buys +2.00 dex at c = 1 (+1.19 at c = 10)
       of the residual +2.58 dex envelope price; the entire
       first-order v-demand sits on the single highest core fold
       j = 16.
THE MARRIAGE (frozen): instantiate (I) as EXACTLY the per-fold
input that (II) consumes, per rung, per fold f = 0..32:
    |d_f - d^ar_f| = |d_at_f| <= S_f
                   := min( |MAIN_f| + min(SUP_B_f, SUP_F_f),
                           Delta_env ),
(MAIN_f is the comb-free ARCH-pedigree closed-form integral --
exact, classical; SUP_B/SUP_F are the cited-input bounds of the
remainder; Delta_env = 2 M_up = the CLXXVIII mass-envelope tier,
itself a valid all-h bound of the deviation, so the min is a valid
bound), and the v-floor at the 8 core folds
    v_i >= v_i^lo := w_geo_j (H_j - SUP_MIN_j),
    H_j = -(d^ar_j + MAIN_j),  SUP_MIN_j = min(SUP_B_j, SUP_F_j),
(soundness: -d_j = H_j - R_true_j >= H_j - SUP_MIN_j, and
v_i = w_geo_j (-d_j) by the CLXXVIII core-mass reconstruction --
warded against the pipeline v_core per rung).  The COMPOSED
CERTIFICATE per rung, every step exact or cited:
    s_P >= lambda_min(G_core)                      [CLXXVII exact]
        >= lambda_min(V^{1/2} K^{omega_S} V^{1/2}) [L2 + fold-wise
                                                    domination]
        >= lambda_min(V_lo^{1/2} K^{omega_S} V_lo^{1/2}) =: FLOOR
                                                   [L5]
with omega_S,f = w_f (|d^ar_f| + S_f) for f <= 32 and w_f (|d^ar_f|
+ Delta_env) beyond; CERTIFIED iff all 8 v_i^lo > 0 AND FLOOR >
mu1(h) (the registered target).  On certified surface steps the
CLXXIX rho chain consumes the supplied floor directly: chain_eval
with (a, b) = (FLOOR, 0) -- P_G >= lambda_min(G_core) I >= FLOOR I
by rotation invariance -- giving the composed skeleton margin
1 - rho >= (FLOOR/2)(T - c)/(2 Mt_ii Mt_jj) with the CLXXIX
measured inputs (Mt diagonals, exact half-dominance) unchanged and
honestly named.

RESONANCE HONESTY (declared in advance): the sub-gamma_1 SEAT
(gamma_1 - omega >= 5) holds only for the core folds; on the
extended band f <= 32 the alias frequency omega_f ~ pi f/(2 alpha)
crosses gamma_1 = 14.134725 on shallow rungs.  The Fourier
envelope TENV/gamma^2 remains a VALID upper bound at every gamma
(the geometric-sum envelope caps at the run length, the pair sup
at 1) -- it merely degrades near resonance, where the min with
Buethe and the Delta_env cap take over.  The resonance census
(folds with omega_f > gamma_1 - 5) is printed as anatomy; the
KILL ward is soundness |R_true_f| <= SUP_F_f on every rung x fold,
not distance.

WHAT IS MEASURED.
(a) THE SUPPLY-vs-DEMAND c-LADDER in the CLXXXIII currency: per
    fold the effective sharpness c_eff_f = S_f / |d_f - d^ar_f|
    (dev = exact deviation, anatomy denominator), med per core
    fold and per band f <= 16 / 32, the census of cells with
    c_eff <= c for c in SHARP_C = (1, 2, 5, 10, 30), and the
    j = 16 seat specifically; next to it the DIRECT payoff
    log10(bound_S / bound_ENV) with the measured v (what the
    supplied band actually buys, not the uniform-c proxy).
(b) THE COMPOSED CENSUS: surface 39 + deep block (gram level,
    shallowest-first, DEEP_CAP): per rung v_lo positivity (8
    folds), FLOOR, FLOOR/mu1 dex, certification; the decomposition
    gain_omega = log10(bound_S/bound_ENV) at measured v and
    loss_v = log10(FLOOR/bound_S(v_meas)); for open rungs the
    shortfall at the named seat log10(SUP_MIN_16/H_16) and the
    TWO-KNOB anatomy at j = 16 (both knobs pay 1:1 into SUP_F):
    (K-a) pair-budget knob: SUP_F recomputed with the top-ramp
    pair mass integrated coherently to zero (pb2 = 0; the best
    case of the CLXXXI-named signed Abel treatment) -- ANATOMY;
    (K-b) Rosser low-T knob: the zero-sum Abel bound recomputed
    on the fluctuation-free corridor N = N_main (the best case of
    any N(T)-class improvement at small T) -- ANATOMY; censuses
    of open rungs that would close under (K-a)/(K-b)/both.
(c) THE ALL-H TREND: OLS of the composed margin log10(FLOOR/mu1)
    vs alpha on FLOOR-positive rungs, and of the v-seat margin
    log10(H_16/SUP_MIN_16) vs alpha on all rungs (CLXXXI measured
    +0.525 dex/alpha for the supply side); the CONJECTURE form
    stated with the theorem/anatomy split (Rosser N(T): all
    T >= 2; B_PSI: all x; window algebra + L1/L2/L5: exact all-h;
    Buethe: X <= 1e19; Platt-Trudgian: fixed T0 = 3e12; the
    OPEN part: the shallow-fold supply at the j = 16 seat).
(d) GATES: tau-screens (parent verbatim) on the composed margin
    and the v-seat margin; parent controls smooth/Epstein/scramble
    (kill); C3 scramble core-fold density movement (lowfreq
    verbatim, kill); the DISCRIMINATION SEAT verified: the
    composition is world-blind BY CONSTRUCTION (declared, CLXXXII
    verbatim -- smooth reproduces it), so the prime consumption
    must sit in the SUPPLY: the scramble-comb violation census of
    |d_scr_f - MAIN_f| <= SUP_F_f over the f <= 32 band at the
    control window (CLXXXI saw 3/9 on the 9 reads), and the
    smooth-world composition reproduction on CTRL_NKZ sampled
    rungs.  ANTI-CIRCULARITY (frozen): no computed zeta zero, no
    wall data, no target eigendata in any supplied number;
    gamma_1 / T0 / Rosser / Buethe / B_PSI enter only as cited
    constants (EXTERNAL-CITED pedigree block printed); measured
    d/R/v values appear only as truth columns, soundness wards
    and anatomy denominators.  RNG: none except the declared
    scramble control (seed 1, parent verbatim).

REPRODUCTION WARDS (kill; full run only where marked): parent
census 42/41/39 + v901 minB/gap + CLXXVII battery meds a/b =
0.968/0.202 rtol 5e-2 + s_P >= mu1 39/39; CLXXVIII/CLXXX demand
meds (381, 382, 802) rtol 5e-2; CLXXXI per-fold med SUP_F profile
(6.497, 6.131, 5.739, 5.963, 6.508, 6.949, 7.508, 7.601) rtol
5e-2 [full], surface MIN-closure fold profile (39, 39, 35, 30,
23, 17, 13, 7) exact [full], Buethe fold profile (39, 30, 16, 6,
0, 0, 0, 0) exact [full]; CLXXXIII surface ENV budget med +1.55
dex atol 0.10 [full] and ENV > mu1 on 39/39 surface [full];
CLXXVI rho census med/max 0.918/0.957 rtol 5e-2 [full]; SIG2
sanity band [0.0231, 0.06]; Loewner counterexample must FIRE
(vhead verbatim).  Per-rung kill wards: fold soundness |R_true_f|
<= SUP_B_f and <= SUP_F_f and |d_at_f| <= S_f (SOUND_TOL);
fold-wise domination (d_f)_+ <= |d^ar_f| + Delta_f (DOM_TOL);
Loewner ward on the S tier (L2_TOL); L5 spectrum identity
(L5_TOL); v_lo <= v_core (VLO_TOL); FLOOR <= lambda_min(G_core)
(FLOOR_TOL); transform jump-vs-segment ward on sampled folds
(TRANS_TOL) and envelope soundness at sample gammas.

VERDICT (frozen enums, decided by these rules and nothing else;
N = surface + deep census, n_cert = certified rungs, n_vpos =
rungs with all 8 v_lo > 0):
  V1 headline:
    W1-ASSEMBLY-CERTIFIED(N/N; min composed margin dex; the
      composed theorem stated with every constant) iff n_cert == N;
    W1-ASSEMBLY-BLOCKED(seat) iff n_cert < n_vpos (the marriage
      loses a rung that the supply half had already closed);
    W1-ASSEMBLY-PARTIAL(n_cert/N; v-fold profile; med j16
      shortfall dex; knob censuses) iff 0 < n_cert < N;
    W1-ASSEMBLY-OPEN otherwise.
  V2 rho: RHO-COMPOSED-SURFACE(min composed margin) iff surface
    n_cert == 39 AND supplied-chain m > 0 on 39/39 AND the CLXXVI
    census reproduces; RHO-COMPOSED-PARTIAL(n_pos/n_cert_s on the
    certified subset; the rest CLXXIX-conditional, cited) iff
    surface n_cert > 0; else RHO-STILL-CONDITIONAL (CLXXIX cited,
    the measured-battery chain is still re-run as a ward).
  V3 all-h: ALLH-COMPOSED-IMPROVES(slope >= +0.05) / ALLH-FLAT /
    ALLH-DEGRADES(<= -0.05) on the composed-margin trend; the
    conjecture text is always printed and typed ANATOMY.
  V4 sharpness: SUPPLY-SHARP(med c_eff on f <= 32 cells <= 10,
    the CLXXXIII c-ladder seat) / SUPPLY-LOOSE(med c_eff).
  V5 seat: DISCRIMINATION-IN-SUPPLY(scramble band violations >= 1
    AND smooth reproduces the composition on all usable sampled
    rungs) / DISCRIMINATION-UNRESOLVED(census).
DEAD overrides: any kill ward -> PIPELINE-BROKEN / WARD-BROKEN /
ALGEBRA-BROKEN as tagged.

ANTHROPIC NO-GO + HONEST SCOPE (stated once, repeated in the
verdict): a certified rung is a FINITE statement -- the W1
v-positivity + floor half on the deployed window from cited
classical inputs (gamma_1 first-zero, Platt-Trudgian T0 = 3e12,
Rosser 1941 N(T), Buethe 2018 sqrt-range X <= 1e19, B_PSI all-x)
plus exact window algebra and the exact composition [L1/L2/L5];
the CLXXIX rho consumption keeps its measured inputs (Mt
diagonals, exact half-dominance) exactly as CLXXIX declared them.
The composition is world-blind by construction and is NOT a wall
certificate; W2 / wall / background cancellation remain RH-hard
and untouched in EVERY branch.  NO RH claim.  No marker moves,
no promotion; stdout only.

FROZEN BARS: FBAND = 32; SHARP_C = (1, 2, 5, 10, 30) (vhead
verbatim); C_MED_BAR = 10.0; TSAMP = (0, 8, 16, 24, 32);
SOUND_TOL = 1e-6 rel + 1e-9 (1 + l1_at) abs (lowfreq verbatim);
DOM_TOL = 1e-12; L2_TOL = 1e-9; L5_TOL = 1e-9; GRID_TOL = 1e-9;
VLO_TOL = 1e-6 rel + 1e-15 abs; FLOOR_TOL = 1e-9 rel; TRANS_TOL =
1e-10; CE_MARGIN = 1e-6; SUPF_MED_REF = (6.497, 6.131, 5.739,
5.963, 6.508, 6.949, 7.508, 7.601) rtol 5e-2; FOLD_MIN_PROFILE =
(39, 39, 35, 30, 23, 17, 13, 7) exact; FOLD_B_PROFILE = (39, 30,
16, 6, 0, 0, 0, 0) exact; REPRO_D = (381, 382, 802) rtol 5e-2;
REPRO_A/B_MED = 0.968/0.202 rtol 5e-2; VHEAD_BUD_REF = +1.55 atol
0.10; RHO_MED/MAX_REF = 0.918/0.957 rtol 5e-2; SIG2_BAND =
[0.0231, 0.06]; TREND_FLAT = 0.05; MOVE_BAR = 0.05; DEEP_CAP = 28
(all available in H_HOLD, shallowest-first, declared runtime
cap); MIN_DEEP = 10; CTRL_NKZ = 2 (declared runtime-bounded
smooth/scramble composition sample); parent SPEC-SHA == 084c9689
(full); prefix wards: subgamma c7d8810c, monocomp bed53f23,
vhead 9ffe771d, lowfreq be867853, rho 6c5474bf.  Runtime cap
declared: 20 min.  Smoke mode W1ASM_SMOKE=1 restricts the surface
to the 6 shallowest steps and the deep block to 2 rungs and defers
the full-only reproduction wards (disclosed prints).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): TWO smoke
runs (both W1ASM_SMOKE=1: 6 shallowest surface steps + 2 deep
rungs) and ONE amendment, disclosed in order:
  SMOKE-1 (exit 1, 7.9 s, 42/43): the ONLY fail was B1 -- the
  CLXXVIII/CLXXX demand-ladder ward read Delta meds 137.1/137.9/
  295.0 against the published refs (381, 382, 802), which are
  39-step surface medians and scale with sqrt(X): on the 6
  SHALLOWEST steps the ward is not defined (same class as the
  MONOCOMP disclosed smoke-fails O1/N2).  All other 42 checks
  green.
  AMENDMENT A1: B1 gated to the full run (where the 39-step
  median exists), exactly like B2-B5/R1; the ward VALUES (381,
  382, 802, rtol 5e-2) are untouched and the frozen run must pass
  them.  No bar, band, count, rule or enum moved.
  SMOKE-1 measured content the frozen run must be consistent with
  (6 shallowest steps -- NOT the published 39-step medians, the
  frozen run decides all full-surface numbers): kill wards green
  (fold soundness worst excess 0.0, transform 1.07e-16, ident
  3.68e-15, domination 6/6, Loewner min rel +0.390, L5 worst
  2.89e-15, grid 4.76e-14, v_lo recon 3.08e-14, FLOOR <= truth
  6/6 + 2/2); resonance census 71/198 cells beyond gamma_1 - 5
  (10 beyond gamma_1), envelope sound throughout; c-ladder med
  c_eff f <= 16 = 3.06, f <= 32 = 8.63, j16 seat med 8.92;
  direct payoff gain_omega +1.32/+1.51/+1.65 dex; v-closure
  profile (6, 6, 3, 1, 0, 0, 0, 0) on the shallowest 6 (the
  CLXXXI seat); ENV budget med +0.56 (min +0.28) > mu1 on 6/6;
  deep kz 177/243 certify at +4.52/+4.61 dex composed margin,
  v-floor cost med -0.02 dex; open-rung j16 shortfall med +0.88
  dex, knobs close 0/6 (pair med -0.28 dex, Rosser -0.13 dex);
  scramble violates SUP_F on 5/33 band folds, smooth reproduces
  2/2 -> DISCRIMINATION-IN-SUPPLY; v-seat trend +0.578 dex/alpha
  (R2 0.98) vs CLXXXI +0.525; smoke verdicts pinned by the frozen
  rules: V1 W1-ASSEMBLY-PARTIAL(2/8), V2 RHO-STILL-CONDITIONAL,
  V3 ALLH-UNMEASURED(n=2), V4 SUPPLY-SHARP(8.63), V5
  DISCRIMINATION-IN-SUPPLY.
  SMOKE-2 (after A1, expected 43/43): the confirmation pass; its
  numbers must equal SMOKE-1 on every measured quantity.
No bar, band, count, rule or enum was moved after SMOKE-2; the
only post-smoke changes are amendment A1 and this disclosure
block.  The frozen run repeats everything on the full 39-step
surface + full deep block; enums move only as the full data says.

NO RH claim.  A partial verdict is itself the finding: it prices
the assembled chain rung by rung in honest dex against the two
named 1:1 knobs.  No marker moves.  Stdout only.
"""

import ast
import hashlib
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
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import lowfreq_discrepancy_gain_probe as lf  # noqa: E402 (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)
import monotone_composition_probe as mono  # noqa: E402  (READ-ONLY)
import vfloor_headroom_probe as vhead  # noqa: E402  (READ-ONLY)
import rho_margin_derivation_probe as rho  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
SUBG_SHA8 = "c7d8810c"
MONO_SHA8 = "bed53f23"
VHEAD_SHA8 = "9ffe771d"
LOWFREQ_SHA8 = "be867853"
RHO_SHA8 = "6c5474bf"

FBAND = 32
SHARP_C = (1, 2, 5, 10, 30)
C_MED_BAR = 10.0
TSAMP = (0, 8, 16, 24, 32)
SOUND_TOL = 1.0e-6
DOM_TOL = 1.0e-12
L2_TOL = 1.0e-9
L5_TOL = 1.0e-9
GRID_TOL = 1.0e-9
VLO_TOL = 1.0e-6
FLOOR_TOL = 1.0e-9
TRANS_TOL = 1.0e-10
CE_MARGIN = 1.0e-6
SUPF_MED_REF = (6.497, 6.131, 5.739, 5.963, 6.508, 6.949, 7.508,
                7.601)
SUPF_RTOL = 5.0e-2
FOLD_MIN_PROFILE = (39, 39, 35, 30, 23, 17, 13, 7)
FOLD_B_PROFILE = (39, 30, 16, 6, 0, 0, 0, 0)
REPRO_D = (381.0, 382.0, 802.0)
REPRO_D_RTOL = 5.0e-2
REPRO_A_MED = 0.968
REPRO_B_MED = 0.202
REPRO_RTOL = 5.0e-2
VHEAD_BUD_REF = 1.55
VHEAD_BUD_ATOL = 0.10
RHO_MED_REF = 0.918
RHO_MAX_REF = 0.957
RHO_RTOL = 5.0e-2
SIG2_BAND = (0.0231, 0.06)
TREND_FLAT = 0.05
MOVE_BAR = 0.05
DEEP_CAP = 28
MIN_DEEP = 10
CTRL_NKZ = 2
LN2 = math.log(2.0)
CORE_J = base.CORE_J
SMOKE = os.environ.get("W1ASM_SMOKE", "") == "1"
BANNED_IDS = parent.BANNED_IDS

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
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def abel_nofluc(tg, c):
    """ANATOMY ONLY (declared): the Abel sum against the
    fluctuation-free corridor N == N_main -- the best case of any
    N(T)-class improvement at small T.  NOT a bound."""
    c = np.asarray(c, float)
    ti = tg[1:-1]
    d = c[:-1] - c[1:]
    nm = subg.n_main(ti)
    s = float(np.sum(d * nm))
    s += float(c[-1] * subg.n_main(np.array([tg[-1]]))[0])
    return s


def rung_band(alpha, M, uu, mm, c_ar, s2t, trans_wards=False):
    """Per-fold classical supply on folds 0..FBAND for one rung:
    the marriage input.  Buethe route = lowfreq verbatim algebra;
    Fourier route = subgamma verbatim machinery."""
    D = 2.0 * alpha / M
    L = 2 * M - 2
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c_ar = np.asarray(c_ar, float)
    d_at = base.grid_density(c_at)
    d_ar = base.grid_density(c_ar)
    d_tot = base.grid_density(c_ar + c_at)
    X = math.exp(2.0 * alpha)
    m_up = 2.0 * core.B_PSI * (2.0 * math.sqrt(X) - 1.0)
    de_env = 2.0 * m_up
    l1_at = float(np.sum(np.abs(c_at)))
    nodes = D * np.arange(M + 1)
    k = np.arange(M)
    u0 = k * D
    u1 = (k + 1) * D
    keep = u1 > LN2
    u0k = u0[keep]
    u1k = u1[keep]
    lo = np.maximum(u0k, LN2)
    elo2 = np.exp(0.5 * lo)
    ehi2 = np.exp(0.5 * u1k)
    envB = lf.env_sup("B", lo, u1k)
    tg = subg.rung_grid(D)
    folds = {}
    tworst = 0.0
    env_ok = True
    knob = None
    for j in range(0, FBAND + 1):
        p = lf.phi_nodes(M, L, j)
        pk = p[:M][keep]
        b = ((p[1:] - p[:M]) / D)[keep]
        phi_lo = pk + b * (lo - u0k)
        phi_hi = pk + b * (u1k - u0k)
        seg = 2.0 * (ehi2 * (phi_hi - 2.0 * b)
                     - elo2 * (phi_lo - 2.0 * b))
        main = 2.0 * float(np.sum(seg))
        w_lo = b - 0.5 * phi_lo
        w_hi = b - 0.5 * phi_hi
        width = u1k - lo
        same = w_lo * w_hi >= 0.0
        dw = np.abs(w_lo - w_hi)
        iW = np.where(
            same, 0.5 * np.abs(w_lo + w_hi) * width,
            np.where(dw > 0.0,
                     0.5 * (w_lo ** 2 + w_hi ** 2) * width
                     / np.maximum(dw, 1e-300), 0.0))
        phi_ln2 = float(np.interp(LN2, nodes, p))
        sup_b = 2.0 * math.sqrt(2.0) * abs(phi_ln2) \
            + 2.0 * float(np.sum(envB * iW))
        ph = subg.build_phit(alpha, M, D, L, j)
        ef = subg.read_supply_ef(ph, alpha, D, tg, s2t)
        sup_f = ef["sup_f"]
        sup_min = min(sup_b, sup_f)
        dev = abs(float(d_at[j]))
        S = min(abs(main) + sup_min, de_env)
        folds[j] = dict(main=main, sup_b=sup_b, sup_f=sup_f,
                        sup_min=sup_min, dev=dev, S=S,
                        d_at=float(d_at[j]), d_ar=float(d_ar[j]),
                        r_true=float(d_at[j]) - main,
                        H=-(float(d_ar[j]) + main),
                        omega=ph["theta"] / D,
                        w_geo=4.0 * math.sin(math.pi * j / L) ** 2
                        / L)
        if trans_wards and j in TSAMP:
            for gam in (subg.GAMMA1, 25.0, 60.0):
                hj = subg.phit_hat_jump(ph, gam)
                hs = subg.phit_hat_seg(ph, gam)
                tworst = max(tworst, abs(hj - hs)
                             / (1.0 + ph["sd"] / gam ** 2))
                te = float(subg.tenv_of(ph, np.array([gam]),
                                        np.array([gam]))[0])
                if abs(hj) > (te + 1e-12) / gam ** 2 + 1e-12:
                    env_ok = False
        if j == 16:
            ph_np = dict(ph)
            ph_np["pb2"] = 0.0
            c_np = subg.tenv_of(ph_np, tg[:-1], tg[1:]) \
                / tg[:-1] ** 2
            zs_np = subg.abel_upper(tg, c_np, n_start=0.0)
            sup_np = 4.0 * zs_np + ef["tail"] + ef["triv"] \
                + abs(ef["main_ext"])
            c0 = subg.tenv_of(ph, tg[:-1], tg[1:]) / tg[:-1] ** 2
            zs_nf = abel_nofluc(tg, c0)
            sup_nf = 4.0 * zs_nf + ef["tail"] + ef["triv"] \
                + abs(ef["main_ext"])
            zs_b2 = abel_nofluc(tg, c_np)
            sup_both = 4.0 * zs_b2 + ef["tail"] + ef["triv"] \
                + abs(ef["main_ext"])
            knob = dict(sup_np=sup_np, sup_nf=sup_nf,
                        sup_both=sup_both)
    return dict(D=D, L=L, X=X, l1_at=l1_at, de_env=de_env,
                d_at=d_at, d_ar=d_ar, d_tot=d_tot, folds=folds,
                delta_meas=float(np.max(np.abs(d_at))),
                delta_lag=2.0 * l1_at, knob=knob,
                tworst=tworst, env_ok=env_ok)


def rung_assembly(rb, y_core, v_core, h, Gc, mu1):
    """Kernels, floors and per-rung wards of the composed chain."""
    L = rb["L"]
    f, wg, xg = mono.fold_grid(L)
    daf = np.abs(rb["d_ar"][f])
    dfv = rb["d_tot"][f]
    v_core = np.asarray(v_core, float)
    dd_env = np.full(len(f), rb["de_env"])
    dd_sup = dd_env.copy()
    nn = min(FBAND + 1, len(dd_sup))
    dd_sup[:nn] = np.array([rb["folds"][j]["S"] for j in range(nn)])
    out = dict(
        dom_sup=float(np.max(np.maximum(dfv, 0.0)
                             - (daf + dd_sup))),
        truth=float(np.linalg.eigvalsh(Gc)[0]))
    K_env = mono.kernel_of(xg, wg * (daf + dd_env), y_core, h)
    K_sup = mono.kernel_of(xg, wg * (daf + dd_sup), y_core, h)
    K_grid = mono.kernel_of(xg, wg * np.maximum(dfv, 0.0),
                            y_core, h)
    if K_env is None or K_sup is None or K_grid is None:
        return None
    out["b_env"] = vhead.bnd(K_env, v_core)
    out["b_sup"] = vhead.bnd(K_sup, v_core)
    out["grid_dev"] = abs(vhead.bnd(K_grid, v_core) / out["truth"]
                          - 1.0)
    Gom = np.sqrt(v_core)[:, None] * K_sup \
        * np.sqrt(v_core)[None, :]
    dif = Gc - 0.5 * (Gom + Gom.T)
    out["loewner"] = (float(np.linalg.eigvalsh(
        0.5 * (dif + dif.T))[0])
        / max(float(np.linalg.norm(Gc, 2)), 1e-300))
    out["l5_id"] = vhead.spectrum_identity(K_sup, v_core)[0]
    v_lo = np.array([rb["folds"][j]["w_geo"]
                     * (rb["folds"][j]["H"]
                        - rb["folds"][j]["sup_min"])
                     for j in CORE_J])
    v_rec = np.array([rb["folds"][j]["w_geo"]
                      * (-(rb["folds"][j]["d_ar"]
                           + rb["folds"][j]["d_at"]))
                      for j in CORE_J])
    out["v_lo"] = v_lo
    out["vrec_dev"] = float(np.max(np.abs(v_rec - v_core)
                                   / np.maximum(v_core, 1e-300)))
    out["vlo_excess"] = float(np.max(v_lo - v_core
                                     * (1.0 + VLO_TOL) - 1e-15))
    out["vpos"] = bool(np.all(v_lo > 0.0))
    out["floor"] = vhead.bnd(K_sup, v_lo) if out["vpos"] else 0.0
    out["mu1"] = mu1
    out["cert"] = bool(out["vpos"] and out["floor"] > mu1)
    return out


def fold_sound(rb):
    """Worst scaled soundness excess over the f <= FBAND band."""
    worst = 0.0
    for j in range(0, FBAND + 1):
        fd = rb["folds"][j]
        tol = 1e-9 * (1.0 + rb["l1_at"])
        for sup in (fd["sup_b"], fd["sup_f"]):
            ex = abs(fd["r_true"]) - sup * (1.0 + SOUND_TOL) - tol
            worst = max(worst, ex / (1.0 + rb["l1_at"]))
        ex = fd["dev"] - fd["S"] * (1.0 + SOUND_TOL) - tol
        worst = max(worst, ex / (1.0 + rb["l1_at"]))
    return worst


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join([labels.get("v1", "-"),
                              labels.get("v2", "-"),
                              labels.get("v3", "-"),
                              labels.get("v4", "-"),
                              labels.get("v5", "-")])
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: a certified rung is a FINITE statement -- the W1
  v-positivity + floor half of the deployed window from the cited
  unconditional inputs (gamma_1, Platt-Trudgian T0 = 3e12, Rosser
  1941 N(T), Buethe 2018 sqrt-range, B_PSI) plus exact window
  algebra and the exact composition [L1/L2/L5]; the rho
  consumption keeps the CLXXIX measured inputs (Mt diagonals,
  exact half-dominance) and stays conditional on them.  The
  composition is world-blind by construction and is not a wall
  certificate; W2 / wall / background cancellation remain RH-hard
  and untouched.  Extrapolations and knob values are ANATOMY.
  NO RH claim; no marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.ASSEMBLY.01 -- the sub-gamma_1 Fourier "
            "supply married to the monotone composition "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = {}
    for tag, mod in (("parent", parent), ("subgamma", subg),
                     ("monocomp", mono), ("vhead", vhead),
                     ("lowfreq", lf), ("rho", rho)):
        shas[tag] = hashlib.sha256(
            mod.__doc__.encode("utf-8")).hexdigest()
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (all EXTERNAL-CITED; no computed zero "
          "ordinate enters any construction):")
    print("      gamma_1 = %.6f (first-zero theorem, classical "
          "literature)" % subg.GAMMA1)
    print("      T0 = %.1e (Platt-Trudgian 2021, Bull. LMS 53; "
          "zeros above T0 NOT assumed on-line)" % subg.T0_RH)
    print("      Rosser 1941 AJM 63 Thm 19 N(T) corridor "
          "(%.3f, %.3f, %.3f), T >= 2"
          % (subg.ROSSER_A, subg.ROSSER_B, subg.ROSSER_C))
    print("      Buethe 2018 (0.94 sqrt x, 11 < x <= 1e19; "
          "v594:10-13,47) + two-sided table sups")
    print("      B_PSI = %.5f (all x, v563:136); window algebra + "
          "ARCH main integrals exact" % core.B_PSI)
    if SMOKE:
        print("    *** SMOKE MODE: 6 surface steps, 2 deep rungs, "
              "full-only wards deferred ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced",
          shas["parent"] == PARENT_SHA, kill="K2")
    ok_pref = (shas["subgamma"][:8] == SUBG_SHA8
               and shas["monocomp"][:8] == MONO_SHA8
               and shas["vhead"][:8] == VHEAD_SHA8
               and shas["lowfreq"][:8] == LOWFREQ_SHA8
               and shas["rho"][:8] == RHO_SHA8)
    check("S0c predecessor SPEC prefixes reproduced (c7d8810c/"
          "bed53f23/9ffe771d/be867853/6c5474bf)", ok_pref,
          kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder + CLXXVII battery reproduction")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)),
          kill="K1")
    if KILLS:
        return finish({})
    minb = min(float(np.linalg.eigvalsh(w["B"])[0]) for w in rows)
    gaps = np.array([w["gap"] for w in rows])
    check("W2 v901 reproduction",
          abs(minb / parent.MINB_REF - 1.0) <= parent.MINB_RTOL
          and abs(float(np.min(gaps)) / parent.GAPMIN_REF - 1.0)
          <= parent.GAP_RTOL
          and abs(float(np.median(gaps)) / parent.GAPMED_REF - 1.0)
          <= parent.GAP_RTOL,
          "minB %.4f gap %.4f/%.4f"
          % (minb, float(np.min(gaps)), float(np.median(gaps))),
          kill="K2")
    for w in rows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    ab = [lf.battery_split(w["Gc"]) for w in rows]
    a_med = float(np.median([x[0] for x in ab]))
    b_med = float(np.median([x[1] for x in ab]))
    check("W3 CLXXVII H1/H2 reproduction (a med %.4f, b med %.4f)"
          % (a_med, b_med),
          abs(a_med / REPRO_A_MED - 1.0) <= REPRO_RTOL
          and abs(b_med / REPRO_B_MED - 1.0) <= REPRO_RTOL,
          kill="K2")
    n_sp = sum(w["sP"] >= w["mu1"] for w in rows)
    check("W4 CLXXIV reproduction s_P >= mu1",
          n_sp == len(rows), "%d/%d" % (n_sp, len(rows)),
          kill="K2")

    # ------------------------------------------------------------ E
    section("E -- classical inputs on the extended table")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_tab = (dev == 0.0
              and np.array_equal(deep.EXT["NN"][:nP], core._NN)
              and np.array_equal(deep.EXT["U"][:nP], core.U_ALL)
              and np.array_equal(deep.EXT["MU"][:nP], core.MU_ALL))
    check("E0 deep-table fidelity (overlap dev %.1e, prefixes "
          "bitwise)" % dev, ok_tab, kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    lf.ENV.update(lf.table_sups(NN_e, psi_e, deep.TAB_EXT))
    check("E1 Buethe envelope warded on the table (sup %.4f <= "
          "%.2f)" % (lf.ENV["BUETHE_SUP"], lf.BUETHE),
          lf.ENV["BUETHE_SUP"] <= lf.BUETHE, kill="K2")
    ratio_max = float(np.max(psi_e / NN_e.astype(float)))
    check("E2 global Chebyshev bound max psi/x = %.5f <= B_PSI "
          "%.5f" % (ratio_max, core.B_PSI),
          ratio_max <= core.B_PSI, kill="K2")
    nlo_g1 = float(subg.n_main(np.array([subg.GAMMA1]))[0]
                   - subg.n_fluc(np.array([subg.GAMMA1]))[0])
    nup_g1 = float(subg.n_up(np.array([subg.GAMMA1]))[0])
    check("E3 Rosser corridor vs the first-zero seat "
          "(N_lo %.3f <= 0 <= N_up %.3f)" % (nlo_g1, nup_g1),
          nlo_g1 <= 0.0 <= nup_g1, kill="K2")
    s2t = subg.s2_tail()
    sig_tg = subg.rung_grid(0.25)
    sig2 = subg.abel_upper(sig_tg, 1.0 / sig_tg[:-1] ** 2,
                           n_start=0.0) + s2t
    check("E4 SIG2 sanity %.6f in [%.4f, %.2f]"
          % ((sig2,) + SIG2_BAND),
          SIG2_BAND[0] <= sig2 <= SIG2_BAND[1], kill="K2")
    ce = vhead.loewner_counterexample()
    check("E5 Loewner counterexample FIRES (naive v-route dead, "
          "vhead verbatim)", ce <= -CE_MARGIN,
          "min eig %+.4f" % ce, kill="K3")

    # ------------------------------------------------------------ A
    section("A -- the assembled chain on the surface")
    use = rows[:6] if SMOKE else rows
    pay = []
    sound_worst = -1e18
    tworst = 0.0
    env_ok = True
    ident_worst = 0.0
    n_dom = n_loew = n_l5 = n_grid = n_vlo = n_fs = 0
    for w in use:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rb = rung_band(rr["alpha"], rr["M"], rr["uu"],
                       2.0 * rr["lam"], rr["c_ar"], s2t,
                       trans_wards=True)
        rs = lf.rung_supply(rr["alpha"], rr["M"], rr["uu"],
                            2.0 * rr["lam"], rr["c_ar"])
        for j in lf.READS:
            ident_worst = max(ident_worst,
                              rs["reads"][j]["ident_dev"]
                              / (1.0 + rs["l1_at"]))
        pa = rung_assembly(rb, r2["y_core"], r2["v_core"],
                           r2["h"], w["Gc"], w["mu1"])
        if pa is None:
            continue
        pa.update(kz=r2["kz"], h=float(r2["h"]),
                  alpha=float(rr["alpha"]), tau=w["tau"], rb=rb,
                  w=w)
        sound_worst = max(sound_worst, fold_sound(rb))
        tworst = max(tworst, rb["tworst"])
        env_ok = env_ok and rb["env_ok"]
        n_dom += int(pa["dom_sup"] <= DOM_TOL)
        n_loew += int(pa["loewner"] >= -L2_TOL)
        n_l5 += int(pa["l5_id"] <= L5_TOL)
        n_grid += int(pa["grid_dev"] <= GRID_TOL)
        n_vlo += int(pa["vlo_excess"] <= 0.0)
        n_fs += int(pa["floor"] <= pa["truth"] * (1.0 + FLOOR_TOL)
                    + 1e-15)
        pay.append(pa)
        if len(pay) % 10 == 0:
            print("    ... %d rungs  [%.1f s]"
                  % (len(pay), time.time() - T0), flush=True)
    n = len(pay)
    check("A1 fold soundness |R_true| <= SUP_B, SUP_F and "
          "|d_at| <= S on every rung x fold f <= %d" % FBAND,
          sound_worst <= 0.0,
          "worst scaled excess %.2e" % sound_worst, kill="K2")
    check("A2 transform ward jump == segment form on sampled "
          "folds (worst %.2e <= %.0e)" % (tworst, TRANS_TOL),
          tworst <= TRANS_TOL, kill="K2")
    check("A3 envelope soundness at sample gammas", env_ok,
          kill="K2")
    check("A4 v882 transcription ward at the reads (worst %.2e)"
          % ident_worst, ident_worst <= 1.0e-9, kill="K2")
    check("A5 fold-wise domination of omega_S (truth world)",
          n_dom == n, "%d/%d" % (n_dom, n), kill="K3")
    check("A6 Loewner ward on the S tier", n_loew == n,
          "%d/%d (min rel %.3e)"
          % (n_loew, n, min(p["loewner"] for p in pay)), kill="K3")
    check("A7 L5 spectrum identity on K_S", n_l5 == n,
          "%d/%d (worst %.2e)"
          % (n_l5, n, max(p["l5_id"] for p in pay)), kill="K3")
    check("A8 grid rebuild of nu_+ reproduces the pipeline "
          "(worst %.2e)" % max(p["grid_dev"] for p in pay),
          n_grid == n, "%d/%d" % (n_grid, n), kill="K3")
    check("A9 v_lo soundness v_lo <= v_core (recon dev worst "
          "%.2e)" % max(p["vrec_dev"] for p in pay),
          n_vlo == n, "%d/%d" % (n_vlo, n), kill="K2")
    check("A10 composed floor soundness FLOOR <= lambda_min("
          "G_core)", n_fs == n, "%d/%d" % (n_fs, n), kill="K3")
    reso = sum(1 for p in pay for j in range(FBAND + 1)
               if p["rb"]["folds"][j]["omega"] > subg.GAMMA1 - 5.0)
    reso_x = sum(1 for p in pay for j in range(FBAND + 1)
                 if p["rb"]["folds"][j]["omega"] > subg.GAMMA1)
    print("    resonance census (anatomy, declared): %d/%d "
          "(rung, fold) cells with omega > gamma_1 - 5, %d with "
          "omega > gamma_1 (the envelope stays sound; the min "
          "with Buethe and the Delta_env cap take over there)"
          % (reso, n * (FBAND + 1), reso_x))

    # ------------------------------------------------------- B repro
    section("B -- predecessor reproduction on the surface")
    dm = np.array([p["rb"]["delta_meas"] for p in pay])
    dl = np.array([p["rb"]["delta_lag"] for p in pay])
    de = np.array([p["rb"]["de_env"] for p in pay])
    meds = (float(np.median(dm)), float(np.median(dl)),
            float(np.median(de)))
    if not SMOKE:
        check("B1 CLXXVIII/CLXXX demand ladder reproduced "
              "(%.1f/%.1f/%.1f)" % meds,
              all(abs(m / r - 1.0) <= REPRO_D_RTOL
                  for m, r in zip(meds, REPRO_D)), kill="K2")
    else:
        print("    (smoke: Delta meds %.1f/%.1f/%.1f on the 6 "
              "shallowest steps -- the published refs are 39-step"
              " medians; B1 deferred, amendment A1)" % meds)
        check("B1 deferred in smoke (disclosed, amendment A1)",
              True)
    supf_med = tuple(float(np.median(
        [p["rb"]["folds"][j]["sup_f"] for p in pay]))
        for j in CORE_J)
    prof_min = tuple(sum(1 for p in pay
                         if p["rb"]["folds"][j]["H"]
                         > p["rb"]["folds"][j]["sup_min"])
                     for j in CORE_J)
    prof_b = tuple(sum(1 for p in pay
                       if p["rb"]["folds"][j]["sup_b"]
                       < p["rb"]["folds"][j]["H"])
                   for j in CORE_J)
    print("    med SUP_F per core fold: %s"
          % str(tuple(round(x, 3) for x in supf_med)))
    print("    v-closure fold profile (H > SUP_MIN): %s | Buethe "
          "profile: %s" % (prof_min, prof_b))
    bud_env = np.array([math.log10(p["b_env"] / p["mu1"])
                        for p in pay])
    n_envpos = int(np.sum(np.array([p["b_env"] for p in pay])
                          > np.array([p["mu1"] for p in pay])))
    print("    CLXXXIII ENV budget log10(b_ENV/mu1) med %+.2f "
          "(min %+.2f), > mu1 on %d/%d"
          % (float(np.median(bud_env)), float(np.min(bud_env)),
             n_envpos, n))
    if not SMOKE:
        check("B2 CLXXXI SUP_F fold-med profile reproduced",
              all(abs(m / r - 1.0) <= SUPF_RTOL
                  for m, r in zip(supf_med, SUPF_MED_REF)),
              str(tuple(round(x, 3) for x in supf_med)),
              kill="K2")
        check("B3 CLXXXI v-closure profile == %s"
              % (FOLD_MIN_PROFILE,), prof_min == FOLD_MIN_PROFILE,
              str(prof_min), kill="K2")
        check("B4 CLXXX Buethe profile == %s" % (FOLD_B_PROFILE,),
              prof_b == FOLD_B_PROFILE, str(prof_b), kill="K2")
        check("B5 CLXXXIII ENV budget med %+.2f == +%.2f "
              "(atol %.2f), > mu1 on %d/39"
              % (float(np.median(bud_env)), VHEAD_BUD_REF,
                 VHEAD_BUD_ATOL, n_envpos),
              abs(float(np.median(bud_env)) - VHEAD_BUD_REF)
              <= VHEAD_BUD_ATOL and n_envpos == 39, kill="K2")
    else:
        print("    (smoke: B2-B5 full-surface reproduction wards "
              "deferred to the frozen run -- disclosed)")
        check("B2-B5 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ C
    section("C -- the supply-vs-demand c-ladder (CLXXXIII "
            "currency)")
    print("    per fold: med dev = |d_f - d^ar_f| | med S_f "
          "(supplied) | med c_eff = S/dev | med SUP_MIN | med H")
    for j in (2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32):
        devs = np.array([p["rb"]["folds"][j]["dev"] for p in pay])
        Ss = np.array([p["rb"]["folds"][j]["S"] for p in pay])
        sm = np.array([p["rb"]["folds"][j]["sup_min"]
                       for p in pay])
        Hs = np.array([p["rb"]["folds"][j]["H"] for p in pay])
        ce_j = Ss / np.maximum(devs, 1e-300)
        print("      f=%2d | %8.3f | %8.3f | %8.2f | %8.3f | "
              "%+9.3f"
              % (j, float(np.median(devs)), float(np.median(Ss)),
                 float(np.median(ce_j)), float(np.median(sm)),
                 float(np.median(Hs))))
    cells16, cells32 = [], []
    for p in pay:
        for j in range(1, FBAND + 1):
            fd = p["rb"]["folds"][j]
            ce_c = fd["S"] / max(fd["dev"], 1e-300)
            if j <= 16:
                cells16.append(ce_c)
            cells32.append(ce_c)
    cells16 = np.array(cells16)
    cells32 = np.array(cells32)
    med16 = float(np.median(cells16))
    med32 = float(np.median(cells32))
    print("    band c_eff: f <= 16 med %.2f | f <= 32 med %.2f "
          "(CLXXXIII: c = 1 buys +2.00 dex on f <= 32, c = 10 "
          "+1.19, f <= 16 only +0.73)" % (med16, med32))
    for cbar in SHARP_C:
        print("      cells with c_eff <= %-3d: f <= 16 %5.1f%% | "
              "f <= 32 %5.1f%%"
              % (cbar,
                 100.0 * float(np.mean(cells16 <= cbar)),
                 100.0 * float(np.mean(cells32 <= cbar))))
    c16 = np.array([p["rb"]["folds"][16]["S"]
                    / max(p["rb"]["folds"][16]["dev"], 1e-300)
                    for p in pay])
    print("    the j = 16 v-demand seat: med c_eff %.2f; H_16 > "
          "SUP_MIN_16 on %d/%d rungs"
          % (float(np.median(c16)),
             sum(1 for p in pay if p["rb"]["folds"][16]["H"]
                 > p["rb"]["folds"][16]["sup_min"]), n))
    gain_om = np.array([math.log10(p["b_sup"]
                                   / max(p["b_env"], 1e-300))
                        for p in pay])
    print("    DIRECT payoff of the supplied band at measured v: "
          "gain_omega = log10(b_S/b_ENV) %+.2f/%+.2f/%+.2f dex"
          % band(gain_om))
    check("C1 c-ladder + direct payoff recorded", True)

    # ------------------------------------------------------------ D
    section("D -- deep block (gram level, shallowest-first, cap "
            "%d)" % DEEP_CAP)
    cand = []
    for kz in range(2, min(deep.KZ_SCAN_MAX,
                           len(deep.EXT["NN"]) - 2)):
        alpha = float(deep.EXT["U"][kz])
        if math.exp(2.0 * alpha) > deep.TAB_EXT:
            break
        if math.exp(2.0 * alpha) <= core.ATOM_MAX:
            continue
        hz = deep.ext_frame(kz)[2]
        if not (deep.H_HOLD[0] <= hz <= deep.H_HOLD[1]):
            continue
        cand.append(kz)
    cand = sorted(cand, key=lambda k: (deep.ext_frame(k)[2], k))
    cand = cand[:2] if SMOKE else cand[:DEEP_CAP]
    print("    %d deep candidate rungs" % len(cand))
    dpay = []
    d_sound = -1e18
    d_dom = d_loew = d_l5 = d_grid = d_vlo = d_fs = 0
    for kz in cand:
        g = deep.ext_gram(kz)
        if not isinstance(g, dict) or not g.get("core_ok") \
                or "chain" not in g:
            print("    deep kz %-4d unusable  [%.1f s]"
                  % (kz, time.time() - T0), flush=True)
            continue
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        _c, Dz = core.atom_lags_at(alpha, Mz,
                                   deep.EXT["U"][:1],
                                   deep.EXT["MU"][:1])
        c_ar = np.asarray(core.arch_lags(Mz, Dz), float)
        rb = rung_band(alpha, Mz, deep.EXT["U"][:ka],
                       deep.EXT["MU"][:ka], c_ar, s2t)
        Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                             g["chain"][2], g["y_core"], g["h"])
        Gd = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
            * np.sqrt(g["v_core"])[None, :]
        Gd = 0.5 * (Gd + Gd.T)
        mu = 4.0 * math.sin(math.pi / (2 * g["h"] + 1)) ** 2
        pa = rung_assembly(rb, g["y_core"], g["v_core"], g["h"],
                           Gd, mu)
        if pa is None:
            print("    deep kz %-4d chain refused  [%.1f s]"
                  % (kz, time.time() - T0), flush=True)
            continue
        pa.update(kz=kz, h=float(g["h"]), alpha=float(alpha),
                  rb=rb)
        d_sound = max(d_sound, fold_sound(rb))
        d_dom += int(pa["dom_sup"] <= DOM_TOL)
        d_loew += int(pa["loewner"] >= -L2_TOL)
        d_l5 += int(pa["l5_id"] <= L5_TOL)
        d_grid += int(pa["grid_dev"] <= GRID_TOL)
        d_vlo += int(pa["vlo_excess"] <= 0.0)
        d_fs += int(pa["floor"] <= pa["truth"] * (1.0 + FLOOR_TOL)
                    + 1e-15)
        dpay.append(pa)
        print("    deep kz %-4d h %-5d FLOOR %.3e  mu1 %.2e  "
              "margin %+.2f dex  vpos %s  cert %s  [%.1f s]"
              % (kz, g["h"], pa["floor"], mu,
                 math.log10(pa["floor"] / mu)
                 if pa["floor"] > 0 else float("-inf"),
                 pa["vpos"], pa["cert"], time.time() - T0),
              flush=True)
    nd = len(dpay)
    check("D1 deep census >= %d" % MIN_DEEP,
          nd >= MIN_DEEP or SMOKE, "%d" % nd, kill="K1")
    check("D2 deep fold soundness", d_sound <= 0.0,
          "worst scaled excess %.2e" % d_sound, kill="K2")
    check("D3 deep chain wards (dom/Loewner/L5/grid/v_lo/floor)",
          nd and d_dom == nd and d_loew == nd and d_l5 == nd
          and d_grid == nd and d_vlo == nd and d_fs == nd,
          "%d/%d each" % (min(d_dom, d_loew, d_l5, d_grid,
                              d_vlo, d_fs), nd), kill="K3")

    # ------------------------------------------------------ census
    section("CEN -- the composed census")
    allp = pay + dpay
    N = len(allp)
    n_cert_s = sum(1 for p in pay if p["cert"])
    n_cert_d = sum(1 for p in dpay if p["cert"])
    n_cert = n_cert_s + n_cert_d
    n_vpos_s = sum(1 for p in pay if p["vpos"])
    n_vpos_d = sum(1 for p in dpay if p["vpos"])
    n_vpos = n_vpos_s + n_vpos_d
    print("    v_lo all-positive: surface %d/%d, deep %d/%d"
          % (n_vpos_s, n, n_vpos_d, nd))
    print("    CERTIFIED (v_lo > 0 AND FLOOR > mu1): surface "
          "%d/%d, deep %d/%d -- total %d/%d"
          % (n_cert_s, n, n_cert_d, nd, n_cert, N))
    cm = [math.log10(p["floor"] / p["mu1"]) for p in allp
          if p["floor"] > 0.0]
    if cm:
        print("    composed margin log10(FLOOR/mu1) on FLOOR-"
              "positive rungs (%d): %+.2f/%+.2f/%+.2f dex"
              % ((len(cm),) + band(np.array(cm))))
    loss_v = [math.log10(p["floor"] / p["b_sup"]) for p in allp
              if p["floor"] > 0.0]
    if loss_v:
        print("    decomposition: v-floor cost log10(FLOOR/b_S("
              "v_meas)) med %+.2f dex | omega gain med %+.2f dex"
              % (float(np.median(loss_v)),
                 float(np.median(gain_om))))
    open_p = [p for p in allp if not p["cert"]]
    sh16 = []
    for p in open_p:
        fd = p["rb"]["folds"][16]
        if fd["H"] > 0:
            sh16.append(math.log10(fd["sup_min"] / fd["H"]))
    if sh16:
        print("    open rungs %d: j16 seat shortfall log10("
              "SUP_MIN_16/H_16) med %+.2f, max %+.2f dex (H_16 "
              "<= 0 on %d)"
              % (len(open_p), float(np.median(sh16)),
                 float(np.max(sh16)),
                 sum(1 for p in open_p
                     if p["rb"]["folds"][16]["H"] <= 0.0)))
    # knob anatomy on open rungs
    k_np = k_nf = k_bt = 0
    red_np, red_nf = [], []
    for p in open_p:
        fd = p["rb"]["folds"][16]
        kn = p["rb"]["knob"]
        red_np.append(math.log10(kn["sup_np"] / fd["sup_f"]))
        red_nf.append(math.log10(kn["sup_nf"] / fd["sup_f"]))
        othr = all(p["rb"]["folds"][j]["H"]
                   > p["rb"]["folds"][j]["sup_min"]
                   for j in CORE_J if j != 16)
        if othr and fd["H"] > min(fd["sup_b"], kn["sup_np"]):
            k_np += 1
        if othr and fd["H"] > min(fd["sup_b"], kn["sup_nf"]):
            k_nf += 1
        if othr and fd["H"] > min(fd["sup_b"], kn["sup_both"]):
            k_bt += 1
    if open_p:
        print("    KNOB ANATOMY (declared, best cases, j16 seat):"
              " pair-knob reduction med %+.2f dex, Rosser-knob "
              "med %+.2f dex" % (float(np.median(red_np)),
                                 float(np.median(red_nf))))
        print("      open rungs whose v-seat would close: "
              "pair-knob %d/%d | Rosser-knob %d/%d | both %d/%d"
              % (k_np, len(open_p), k_nf, len(open_p), k_bt,
                 len(open_p)))
    check("CEN census recorded", True)

    # ------------------------------------------------------------ R
    section("R -- the rho chain (CLXXIX verbatim objects)")
    res_meas = []
    for p in pay:
        w = p["w"]
        B, PG, a, b = rho.step_objects(w["M"], w["Gc"], w["Q"])
        rm = rho.chain_eval(w["M"], B, PG, a, b)
        p["rho_meas"] = rm
        p["rho_obj"] = (B, PG)
        res_meas.append(rm)
    rho_arr = np.array([r["rho"] for r in res_meas])
    ok_rho = (abs(float(np.median(rho_arr)) / RHO_MED_REF - 1.0)
              <= RHO_RTOL
              and abs(float(np.max(rho_arr)) / RHO_MAX_REF - 1.0)
              <= RHO_RTOL)
    if not SMOKE:
        check("R1 CLXXVI rho census reproduced (med %.4f, max "
              "%.4f)" % (float(np.median(rho_arr)),
                         float(np.max(rho_arr))), ok_rho,
              kill="K2")
    else:
        print("    (smoke: rho census med %.4f max %.4f on 6 "
              "steps -- full ward deferred)"
              % (float(np.median(rho_arr)),
                 float(np.max(rho_arr))))
        check("R1 deferred in smoke (disclosed)", True)
    certs = [p for p in pay if p["cert"]]
    n_rho_pos = 0
    m_sup_min = float("inf")
    sound_rho = True
    for p in certs:
        B, PG = p["rho_obj"]
        rs = rho.chain_eval(p["w"]["M"], B, PG, p["floor"], 0.0)
        p["rho_sup"] = rs
        if rs["m_h12"] > 0.0:
            n_rho_pos += 1
            m_sup_min = min(m_sup_min, rs["m_h12"])
        if rs["m_h12"] > rs["margin"] + 1e-12:
            sound_rho = False
    if certs:
        print("    supplied-floor chain on the %d certified "
              "surface rungs: composed 1-rho margin positive on "
              "%d/%d (min %.3e)"
              % (len(certs), n_rho_pos, len(certs),
                 m_sup_min if n_rho_pos else float("nan")))
        check("R2 supplied-chain soundness m_sup <= measured "
              "margin", sound_rho, kill="K2")
    else:
        print("    no certified surface rung -> the supplied rho "
              "chain has no seat; CLXXIX stays cited")
        check("R2 supplied rho chain gated (disclosed)", True)

    # ------------------------------------------------------------ M
    section("M -- world controls + the discrimination seat")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("M1 %s world fires/refuses" % kind, fired, detail,
              kill="K2")
    rr9 = base.window_of(base.CTRL_KZ)
    rr9s = base.window_of(base.CTRL_KZ, scramble_seed=1)
    rb9 = rung_band(rr9["alpha"], rr9["M"], rr9["uu"],
                    2.0 * rr9["lam"], rr9["c_ar"], s2t)
    c9t = np.asarray(core.atom_lags_at(
        rr9s["alpha"], rr9s["M"], rr9s["uu"],
        2.0 * rr9s["lam"])[0], float)
    d9s = base.grid_density(c9t)
    moves, violF = [], 0
    nf9 = min(FBAND, rr9["M"] - 1)
    for j in range(0, nf9 + 1):
        fd = rb9["folds"][j]
        if abs(fd["d_at"]) > 1e-300:
            moves.append(abs(float(d9s[j]) - fd["d_at"])
                         / abs(fd["d_at"]))
        if abs(float(d9s[j]) - fd["main"]) > fd["sup_f"]:
            violF += 1
    med_mv = float(np.median(moves)) if moves else 0.0
    check("M2 scramble core-fold density movement med %.3f >= "
          "%.2f" % (med_mv, MOVE_BAR), med_mv >= MOVE_BAR,
          kill="K2")
    print("    scramble supply-violation census over the band: "
          "%d/%d folds outside SUP_F at the control window "
          "(the scrambled comb is NOT a psi-comb -- the sharper "
          "budget discriminates)" % (violF, nf9 + 1))
    n_sm_use = n_sm_rep = 0
    for w in use[::max(1, len(use) // CTRL_NKZ)][:CTRL_NKZ]:
        kz = w["r2"]["kz"]
        g = base.gram_anatomy(kz, world_fn=base.world_smooth,
                              keep_chain=True)
        if not isinstance(g, dict) or not g.get("core_ok"):
            print("    smooth kz %-4d refused (composition has "
                  "no seat)" % kz)
            continue
        rrw = base.window_of(kz)
        uu_s, mm_s = base.world_smooth(rrw["uu"],
                                       2.0 * rrw["lam"], rrw)
        rb_s = rung_band(rrw["alpha"], rrw["M"], uu_s, mm_s,
                         rrw["c_ar"], s2t)
        Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                             g["chain"][2], g["y_core"], g["h"])
        Gw = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
            * np.sqrt(g["v_core"])[None, :]
        pa_s = rung_assembly(rb_s, g["y_core"], g["v_core"],
                             g["h"], 0.5 * (Gw + Gw.T),
                             4.0 * math.sin(
                                 math.pi / (2 * g["h"] + 1)) ** 2)
        n_sm_use += 1
        ok_rep = pa_s is not None and pa_s["dom_sup"] <= DOM_TOL \
            and pa_s["loewner"] >= -L2_TOL
        n_sm_rep += int(ok_rep)
        print("    smooth kz %-4d composition %s (declared world-"
              "blind outcome)" % (kz, "REPRODUCES" if ok_rep
                                  else "breaks"))
    check("M3 discrimination seat recorded (composition world-"
          "blind, consumption in the supply)", True)

    # ------------------------------------------------------------ S
    section("S -- tau screens (surface)")
    taus = np.array([p["tau"] for p in pay])
    fl = np.array([p["floor"] / p["mu1"] for p in pay])
    vseat = np.array([p["rb"]["folds"][16]["H"]
                      - p["rb"]["folds"][16]["sup_min"]
                      for p in pay])
    lab_f, sl_f = parent.screen(fl, taus)
    lab_v, sl_v = parent.screen(vseat, taus)
    print("    TAU-SCREEN composed margin  %s" % lab_f)
    print("    TAU-SCREEN v-seat margin    %s" % lab_v)
    check("S1 screens recorded", True)

    # ------------------------------------------------------ verdicts
    if n_cert == N:
        mmin = min(math.log10(p["floor"] / p["mu1"])
                   for p in allp)
        v1 = ("W1-ASSEMBLY-CERTIFIED(%d/%d; min composed margin "
              "%+.2f dex)" % (n_cert, N, mmin))
        print("\n  " + "*" * 72)
        print("  THE COMPOSED THEOREM (finite, per deployed rung,"
              " stated with its constants):")
        print("  inputs: gamma_1 = 14.134725 (first-zero), "
              "Platt-Trudgian 2021 T0 = 3e12,")
        print("  Rosser 1941 N(T) (0.137, 0.443, 1.588; T >= 2), "
              "Buethe 2018 0.94 sqrt x on")
        print("  (11, 1e19], B_PSI = %.5f (all x), exact window "
              "algebra + ARCH integrals." % core.B_PSI)
        print("  chain: per fold f <= 32, |d_f - d^ar_f| <= S_f "
              "(printed) => nu_+ <= omega_S")
        print("  fold-wise => lambda_min(G_core) >= lambda_min("
              "V_lo^{1/2} K^S V_lo^{1/2}) = FLOOR")
        print("  > mu1(h) with v_lo = w_geo (H - SUP_MIN) > 0 => "
              "s_P >= mu1 on every rung.")
        print("  validity: the finite deployed surface + deep "
              "block, X <= 4e6 << 1e19; the")
        print("  rho consumption keeps the CLXXIX measured "
              "inputs; W2 / wall / background")
        print("  remain RH-hard and untouched.  NO RH claim.")
        print("  " + "*" * 72)
    elif n_cert < n_vpos:
        v1 = ("W1-ASSEMBLY-BLOCKED(%d certified < %d v-closed: "
              "the composition loses a supply-closed rung)"
              % (n_cert, n_vpos))
    elif n_cert > 0:
        v1 = ("W1-ASSEMBLY-PARTIAL(%d/%d: surface %d/%d + deep "
              "%d/%d; v-profile %s; j16 shortfall med %+.2f dex; "
              "knobs close pair %d / rosser %d / both %d of %d "
              "open)"
              % (n_cert, N, n_cert_s, n, n_cert_d, nd,
                 prof_min,
                 float(np.median(sh16)) if sh16 else float("nan"),
                 k_np, k_nf, k_bt, len(open_p)))
    else:
        v1 = "W1-ASSEMBLY-OPEN(0/%d)" % N
    if n_cert_s == n and certs and n_rho_pos == len(certs) \
            and ok_rho:
        v2 = ("RHO-COMPOSED-SURFACE(min composed margin %.3e; "
              "measured inputs: Mt diag + exact half-dominance, "
              "CLXXIX verbatim)" % m_sup_min)
    elif certs:
        v2 = ("RHO-COMPOSED-PARTIAL(%d/%d positive on the "
              "certified subset; the rest RHO-STILL-CONDITIONAL, "
              "CLXXIX cited)" % (n_rho_pos, len(certs)))
    else:
        v2 = "RHO-STILL-CONDITIONAL(CLXXIX cited; no certified seat)"
    alph = np.array([p["alpha"] for p in allp])
    cmv = np.array([math.log10(p["floor"] / p["mu1"])
                    if p["floor"] > 0 else float("nan")
                    for p in allp])
    fin = np.isfinite(cmv)
    if int(np.sum(fin)) >= 3:
        sl_c, r2_c = parent.ols_line(alph[fin], cmv[fin])
    else:
        sl_c, r2_c = float("nan"), float("nan")
    vs_all = []
    for p in allp:
        fd = p["rb"]["folds"][16]
        if fd["H"] > 0 and fd["sup_min"] > 0:
            vs_all.append((p["alpha"],
                           math.log10(fd["H"] / fd["sup_min"])))
    if len(vs_all) >= 3:
        sl_s, r2_s = parent.ols_line(
            np.array([x[0] for x in vs_all]),
            np.array([x[1] for x in vs_all]))
    else:
        sl_s, r2_s = float("nan"), float("nan")
    print("\n    ALL-H ANATOMY: composed margin trend %+.3f "
          "dex/alpha (R2 %.2f, n=%d); v-seat trend %+.3f "
          "dex/alpha (R2 %.2f; CLXXXI: +0.525)"
          % (sl_c, r2_c, int(np.sum(fin)), sl_s, r2_s))
    print("    CONJECTURE FORM (ANATOMY, typed): the composed "
          "chain holds for all h provided the two classical "
          "supplies persist; already all-h THEOREM: Rosser N(T) "
          "(T >= 2), B_PSI (all x), window algebra + L1/L2/L5 "
          "(exact); finite-range: Buethe (X <= 1e19), Platt-"
          "Trudgian (T0 = 3e12); OPEN: the shallow-fold supply "
          "at the j = 16 seat (the two 1:1 knobs).")
    if np.isnan(sl_c):
        v3 = "ALLH-UNMEASURED(n < 3)"
    elif sl_c >= TREND_FLAT:
        v3 = ("ALLH-COMPOSED-IMPROVES(%+.3f dex/alpha, R2 %.2f "
              "-- ANATOMY, not theorem)" % (sl_c, r2_c))
    elif sl_c <= -TREND_FLAT:
        v3 = ("ALLH-COMPOSED-DEGRADES(%+.3f dex/alpha, R2 %.2f "
              "-- ANATOMY)" % (sl_c, r2_c))
    else:
        v3 = "ALLH-COMPOSED-FLAT(%+.3f, R2 %.2f; ANATOMY)" \
            % (sl_c, r2_c)
    v4 = ("SUPPLY-SHARP(med c_eff %.2f <= %.0f on f <= 32)"
          % (med32, C_MED_BAR)) if med32 <= C_MED_BAR else \
        ("SUPPLY-LOOSE(med c_eff %.2f > %.0f on f <= 32)"
         % (med32, C_MED_BAR))
    if violF >= 1 and n_sm_use > 0 and n_sm_rep == n_sm_use:
        v5 = ("DISCRIMINATION-IN-SUPPLY(scramble violates SUP_F "
              "on %d/%d band folds; smooth reproduces the "
              "composition %d/%d -- the prime consumption sits "
              "in the supply soundness at the measured reads)"
              % (violF, nf9 + 1, n_sm_rep, n_sm_use))
    else:
        v5 = ("DISCRIMINATION-UNRESOLVED(scramble %d/%d, smooth "
              "%d/%d)" % (violF, nf9 + 1, n_sm_rep, n_sm_use))
    check("V1 typed: %s" % v1, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
