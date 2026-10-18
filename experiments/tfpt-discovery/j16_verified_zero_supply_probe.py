#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""j16_verified_zero_supply_probe -- PRIME.PORT.W1.J16SUPPLY.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE LAST GATE OF THE W1 ASSEMBLY.  The
CLXXXIV marriage (w1_assembly_certificate_probe, SPEC-SHA 37a5e259..)
proved the composition LOSSLESS (n_cert == n_vpos) and certified
35/67 = 7/39 surface + 28/28 deep; ALL 32 open rungs hang on the
j = 16 v-floor, where the CLXXXI envelope supply SUP_MIN_16 exceeds
the demand H_16 by med +0.46 dex (max +1.40), and the two priced
1:1 knobs (pair -0.42, Rosser -0.10) close at best 6/32.  The named
missing object is a NEW input class in the same currency.

THE NEW INPUT CLASS -- VERIFIED ZEROS AS EXACT DATA.  Below gamma_1
= 14.134725 there is no nontrivial zero, and every zero with
0 < Im rho <= T0 = 3e12 lies ON the critical line (Platt-Trudgian
2021, Bull. LMS 53, "The Riemann hypothesis is true up to 3*10^12"
-- EXTERNAL-CITED).  The CLXXXI/CLXXXIV supply bounded the zero sum
of the explicit formula by |transform| <= TENV/gamma^2 integrated
against the Rosser N(T) corridor -- an ENVELOPE, wasting the signed
cancellation.  This probe instead sums the first N_Z = 7000 zeros
EXACTLY (ordinates gamma_1..gamma_N, T_c = gamma_N ~ 7290, computed
locally by mpmath.zetazero at dps 15 into verified_zeros_n7000.npy
by the disclosed builder j16_zero_cache_build.py) and pays the
envelope only on the tail gamma > T_c.  DECLARED PARADIGM CHANGE:
the CLXXXI ban on computed zero ordinates as data is DELIBERATELY
LIFTED for this probe -- the ordinates ARE the new input class,
with pedigree (all below T0, hence on-line unconditionally), their
own wards (Rosser-corridor consistency per index, monotonicity,
gamma_1 identity, independent |zeta(1/2 + i gamma)| spot checks)
and their own kill controls (scramble must break the prime-side
ward; a synthetic off-line impostor must shift the supply).  The
AST firewall keeps the parent identifier ban (this source contains
no zeta/prime fetch call; the cache builder is a separate disclosed
file); wall data and target eigendata remain banned everywhere.

THE EXACT OBJECTS (CLXXXI machinery verbatim).  Per rung and fold
j <= 32, with the extended pw-linear window phit_j (breakpoints v,
slope jumps J) and Ft = 2 phit_j(u) e^{-u/2}:
    d_at_j = MAIN_j + MAIN_ext_j + R_true_j,
    R_true_j = - Sum_rho Fttilde(rho) - TRIV_j,
    Fttilde(1/2 + i gamma) = 2 phit_hat(gamma),
    phit_hat(gamma) = -(1/gamma^2) Sum_m J_m e^{i gamma v_m},
so with the verified zeros (conjugate pairs, on-line):
    R_hat_j  = MAIN_ext_j - 4 Sum_{gamma <= T_c} Re phit_hat(gamma)
               - TRIV_exact_j,
    |R_true_j - R_hat_j| <= TAILB_j
    TAILB_j  = 4 * Abel[TENV_j(gamma)/gamma^2; T_c -> T0,
                        N(T_c) = N_Z exact]
               + 4 e^alpha S_Delta_j S2TAIL          (beyond T0)
               + DPS_PAD_j + TRIV_PAD                (declared),
TRIV_exact_j = Int 2 phit_j(u) e^{-u/2}/(e^{2u} - 1) du by 24-pt
Gauss-Legendre per segment (analytic integrand; warded against the
CLXXXI trivial-zero envelope), DPS_PAD_j = 4 Sum_k (S_Delta (v_max
gamma_k + 2)/gamma_k^3) * 1e-9 the ordinate-perturbation pad
(generous vs dps-15 accuracy ~1e-11), tail grid: linear dt =
max(0.25/D, 0.5) from T_c to max(300, 10 pi/D, 2 T_c) then
geometric *1.3 to T0 (phase step 0.25 in gamma D; sin_sup/g_sup
interval sups exact, subgamma verbatim).  The supply is SIGNED:
    -d_j >= H_j - R_hat_j - TAILB_j,
    v_lo_new_j = w_geo_j (H_j - min(SUP_MIN_j, R_hat_j + TAILB_j)),
    S_new_f    = min(S_f, |MAIN_f + R_hat_f| + TAILB_f)   (band),
and the CLXXXIV chain runs UNCHANGED: fold-wise domination =>
[L2] Loewner => [L5] v-floor substitution => FLOOR_new =
lambda_min(V_lo_new^{1/2} K^{S_new} V_lo_new^{1/2}); CERTIFIED iff
all 8 v_lo_new > 0 AND FLOOR_new > mu1(h).

WHAT IS MEASURED.
(a) DEMAND REPRODUCTION (wards, full run): the CLXXXIV surface
    verbatim -- old cert census == 7/39, old v-closure profile ==
    (39, 39, 35, 30, 23, 17, 13, 7), Buethe profile, SUP_F med
    profile, Delta meds (381, 382, 802), ENV budget med +1.55 > mu1
    39/39, CLXXVI rho census, and the j16 seat shortfall on the 32
    open rungs med +0.462 / max +1.404 dex (atol 0.05).
(b) THE HEART WARD (kill, every rung x fold f <= 32): the exact
    formula against the primes.  (i) |R_true_j - R_hat_j| <=
    TAILB_j -- the truncated explicit formula with exact verified
    zeros must land inside its rigorous tail budget at every read;
    (ii) an INDEPENDENT prime-power sieve (built in this source,
    no pipeline arrays) reproduces the pipeline read d_at_j at the
    sampled folds to <= 1e-9 scaled; (iii) transform wards (jump ==
    per-segment closed form, complex-s form == jump form at delta
    = 0, envelope soundness at sample gammas); (iv) |TRIV_exact| <=
    CLXXXI trivial-zero envelope.  The achieved agreement is
    printed honestly in dex and against the 1e-6-relative target
    census (per cell vs |d_at_j|, and on the DC read j = 0); the
    tail-truncation convergence (N_Z/2 vs N_Z residuals) is printed
    as anatomy.
(c) THE CLOSURE CENSUS: new v-closure profile, new vpos/cert
    censuses, per-rung j16 table on the 32 previously open rungs
    (H_16, s_new, seat margin dex, FLOOR_new/mu1 dex, cert), the
    composed count out of 67 with the deep half 28/28 CITED from
    the CLXXXIV frozen run (NOT recomputed -- declared); if the
    surface closes 39/39 the composed statement is printed with
    every constant; the supplied rho chain (a, b) = (FLOOR_new, 0)
    re-runs on every certified surface rung (CLXXIX objects
    verbatim, soundness ward m_sup <= measured margin).
(d) BANDWIDTH GENERALISATION: the same verified-zero supply on all
    folds f <= 32 -- the new c-ladder c_eff = S_new/dev per fold
    and band med f <= 16 / f <= 32 vs the CLXXXIV envelope ladder
    (1.49 / 3.25), the j16 seat med vs 3.88.
(e) GATES: tau screens (parent verbatim) on the new composed margin
    and the new v-seat margin; parent controls smooth / Epstein /
    scramble (kill); C3 scramble density movement (kill); NEW
    CONTROLS (kill, controls-must-fire): (C-i) the scrambled comb
    must break the exact prime-side ward |d_scr - (MAIN + R_hat)|
    <= TAILB on >= 5 of the 33 band folds at the control window --
    the exact formula is a statement about the psi-comb and MUST
    refuse an impostor comb; (C-ii) a synthetic off-line zero
    (gamma_1 moved to beta = 0.75, FE-symmetrised quadruple) must
    shift R_hat_16 by >= 10x the genuine residual at the control
    window -- the construction is measurably sensitive to
    on-line-ness.  Smooth-world composition reproduction stays the
    declared world-blind outcome (sampled, printed).  ANTI-
    CIRCULARITY: no wall data, no target eigendata in any supplied
    number; the verified ordinates enter ONLY the supply side and
    are tested AGAINST the independent prime side -- the explicit
    formula is exactly this zeros-against-primes duality; measured
    d/R/v values appear only as truth columns, soundness wards and
    anatomy denominators.  RNG: none except the declared scramble
    control (seed 1, parent verbatim).

VERDICT (frozen enums, decided by these rules and nothing else;
n = 39 surface rungs, n_cert_new = newly certified):
  V1 headline: J16SUPPLY-SURFACE-CLOSED(39/39; min seat margin dex;
    composed with the CITED deep half: W1 assembly 67/67) iff
    n_cert_new == 39; J16SUPPLY-PARTIAL(n_cert_new/39, was 7;
    residual j16 census dex; the limiting seat named) iff
    7 < n_cert_new < 39; J16SUPPLY-VOID(n_cert_new <= 7) else.
  V2 heart: FORMULA-EXACT-WARDED(worst scaled excess; med slack
    dex; sieve dev; 1e-6-relative census) -- kill wards decide.
  V3 ladder: C-LADDER-SHARPENED(new band meds vs CLXXXIV 1.49/
    3.25, j16 med vs 3.88) / C-LADDER-UNMOVED (med32 within 5%).
  V4 shape: v-seat margin trend vs alpha (OLS) + tau screen labels
    (ANATOMY, typed).
  V5 seat: DISCRIMINATION-FIRES(scramble n/33 >= 5, impostor ratio
    >= 10, smooth composition reproduces on sampled rungs) /
    DISCRIMINATION-UNRESOLVED(census).
DEAD overrides: K1 PIPELINE-BROKEN / K2 WARD-BROKEN / K3
ALGEBRA-BROKEN as tagged.

ANTHROPIC NO-GO + HONEST SCOPE (stated once, repeated in the
verdict): a certified rung is a FINITE statement -- the W1
v-positivity + floor half on the deployed window from the cited
inputs (gamma_1, Platt-Trudgian T0 = 3e12 for the on-line status of
the summed zeros AND the tail split, Rosser 1941 N(T), Buethe 2018,
B_PSI, the verified ordinate data with its declared error budget)
plus exact window algebra and the exact composition [L1/L2/L5].
The deep half of the composed count is CITED from the CLXXXIV
frozen run, not recomputed here.  The rho consumption keeps the
CLXXIX measured inputs (Mt diagonals, exact half-dominance).  The
composition is world-blind by construction and is NOT a wall
certificate; W2 / wall / background cancellation remain RH-hard and
untouched in EVERY branch.  A finite verified-zero sum can never
prove RH -- it prices the finite surface exactly.  NO RH claim.
No marker moves, no promotion; stdout only.

FROZEN BARS: N_Z = 7000 (cache verified_zeros_n7000.npy; T_c =
gamma_N; sized PRE-FREEZE by the tail-bound requirement TAILB <
H_16 - R_16 on the three worst rungs, see scouting disclosure);
DPS_ERR = 1e-9/ordinate; ZETA_TOL = 1e-6 at NS = 24 spot checks
(dps 20); CORR_EPS = 1e-6; FBAND = 32; TSAMP = (0, 8, 16, 24, 32);
GL_N = 24; EXACT_ABS = 1e-9 (1 + l1_at); SIEVE_TOL = 1e-9; HATC_TOL
= 1e-12; TRANS_TOL = 1e-10; DOM_TOL = 1e-12; L2_TOL = 1e-9; L5_TOL
= 1e-9; GRID_TOL = 1e-9; VLO_TOL = 1e-6 rel; FLOOR_TOL = 1e-9;
OLD_CERT_REF = 7 exact; SH16_MED_REF = +0.462, SH16_MAX_REF =
+1.404, SH16_ATOL = 0.05; predecessor reproduction bars CLXXXIV
verbatim (REPRO_D, SUPF_MED_REF, FOLD_MIN_PROFILE, FOLD_B_PROFILE,
VHEAD_BUD_REF, RHO_MED/MAX_REF, SIG2_BAND, REPRO_A/B_MED); SCR_MIN
= 5; IMP_BETA = 0.75; IMP_RATIO_MIN = 10; MOVE_BAR = 0.05;
REL_TARGET = 1e-6; DEEP_CITED = 28; TREND_FLAT = 0.05; CTRL_NKZ =
2; C-ladder refs (CLXXXIV): band16/32 = 1.49/3.25, j16 = 3.88,
LADDER_RTOL = 5e-2; parent SPEC-SHA == 084c9689.. full; prefix
wards: subgamma c7d8810c, monocomp bed53f23, vhead 9ffe771d,
lowfreq be867853, rho 6c5474bf, assembly 37a5e259.  Runtime cap
declared: 25 min (measured ~3 min).  Smoke mode J16VZ_SMOKE=1
restricts the surface to the 6 shallowest steps and defers the
full-only reproduction wards (disclosed prints); controls always
full.

SCOUTING DISCLOSURE (2026-08-11, pre-spec, before any probe run):
three throwaway scratch scripts (deleted) sized the mechanism with
the pre-existing 2000-zero cache (zero_comb_cache_n2000.json, dps
15): (1) six sample rungs -- exact-supply residual |R_true - R_hat|
med ~5e-4, TAILB(2515) med ~0.45, all core folds closed on all six;
(2) the full 39-rung scan -- old demand reproduced EXACTLY (7 cert,
profile (39,39,35,30,23,17,13,7), j16 shortfall med +0.462 / max
+1.404), NEW closure 36/39 with the three failing rungs kz 13/15/16
failing ONLY on TAILB (true margins H_16 - R_true = 0.407/0.217/
0.289 vs TAILB ~ 0.42/0.42/0.53); (3) the T_c ladder on those three
rungs -- TAILB < min margin 0.217 needs T_c ~ 6500-7000, hence the
frozen N_Z = 7000 (T_c ~ 7290, TAILB ~ 0.17 there, headroom 1.3x).
Scramble broke the exact ward on 30/33 band folds, the impostor
shifted R_hat_16 by 0.16 vs genuine residual ~3e-3, the independent
sieve matched to 7e-14.  ALL bars above were frozen after this
scouting and before the first probe run; the probe's own smoke +
frozen runs are disclosed below.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): TWO smoke runs
(both J16VZ_SMOKE=1, 6 shallowest surface steps, controls full; the
second only to capture the full log, numerically identical) and NO
amendment: exit 0, 43/43 checks, 4.8 s.  Measured content the
frozen run must be consistent with (6 shallowest steps): zero cache
warded (7000 ordinates, corridor 7000/7000 both sides, gamma_1 dev
1.4e-07 vs the truncated constant, worst |zeta| spot 1.7e-12 at 23
sampled ordinates, T_c = 7264.7482); heart wards -- worst scaled
excess -3.13e-04 (every read inside TAILB), slack +1.98/+2.82/
+4.79 dex, sieve dev worst 7.65e-14, TAILB_16 med 0.1535,
1e-6-relative census 8/198 band cells (med rel 1.4e-04) and 4/6 DC
reads (med 7.0e-07), truncation convergence med 1.75; old tier
reproduced on the subset (v-profile (6,6,3,1,0,0,0,0), cert 0/6,
j16 shortfall med +0.883 / max +1.404); NEW closure -- v-profile
(6,6,6,6,6,6,6,6), certified 6/6 (was 0/6), composed margins
+2.12/+2.49/+2.80 dex, v-floor cost med -0.04 dex, kz 12 shows a
NEGATIVE signed supply s_new_16 = -0.038 (the exact formula beats
the zero bound); new c_eff med f<=16 1.027 / f<=32 1.169 / j16
1.170; rho supplied-chain positive 6/6 (min 1.370e-05); controls
scramble breaks the exact ward 32/33, impostor shift 0.1615 =
1328x the genuine residual, C3 move 4.994, smooth reproduces 2/2;
screens composed AMBIG(+0.414, R2 0.414, n=6), v-seat
RELOCATION(+0.842, R2 0.332, n=6) -- the smoke subset is
h-monotone, the full-surface screens decide.  No bar, band, count,
rule or enum was moved after the smoke; the only post-smoke change
is this disclosure block.  The frozen run repeats everything on the
full 39-step surface; enums move only as the full data says.

NO RH claim.  A partial verdict is itself the finding: it prices
the verified-zero input class rung by rung in honest dex.  No
marker moves.  Stdout only.
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
import w1_assembly_certificate_probe as asm  # noqa: E402 (READ-ONLY)
import monotone_composition_probe as mono  # noqa: E402  (READ-ONLY)
import vfloor_headroom_probe as vhead  # noqa: E402  (READ-ONLY)
import rho_margin_derivation_probe as rho  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
PREFIXES = dict(subgamma="c7d8810c", monocomp="bed53f23",
                vhead="9ffe771d", lowfreq="be867853",
                rho="6c5474bf", assembly="37a5e259")

ZC_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
N_Z = 7000
DPS_ERR = 1.0e-9
ZETA_TOL = 1.0e-6
NS_ZETA = 24
CORR_EPS = 1.0e-6
FBAND = 32
TSAMP = (0, 8, 16, 24, 32)
GL_N = 24
EXACT_ABS = 1.0e-9
SIEVE_TOL = 1.0e-9
HATC_TOL = 1.0e-12
TRANS_TOL = 1.0e-10
DOM_TOL = 1.0e-12
L2_TOL = 1.0e-9
L5_TOL = 1.0e-9
GRID_TOL = 1.0e-9
VLO_TOL = 1.0e-6
FLOOR_TOL = 1.0e-9
OLD_CERT_REF = 7
SH16_MED_REF = 0.462
SH16_MAX_REF = 1.404
SH16_ATOL = 0.05
SCR_MIN = 5
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
MOVE_BAR = 0.05
REL_TARGET = 1.0e-6
DEEP_CITED = 28
TREND_FLAT = 0.05
CTRL_NKZ = 2
LADDER_REF = dict(band16=1.49, band32=3.25, j16=3.88)
LN2 = math.log(2.0)
CORE_J = base.CORE_J
SMOKE = os.environ.get("J16VZ_SMOKE", "") == "1"
BANNED_IDS = parent.BANNED_IDS

CHECKS = []
KILLS = []
T0 = time.time()
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


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


# ------------------------------------------------- exact-supply algebra
def tail_grid(D, tc):
    """Fine linear grid from T_c (phase step 0.25 in gamma D), then
    geometric *1.3 to T0 (subgamma grid class, shifted seat)."""
    dt = max(0.25 / D, 0.5)
    tsw = max(300.0, 10.0 * math.pi / D, 2.0 * tc)
    nlin = max(int(math.ceil((tsw - tc) / dt)), 1)
    lin = tc + dt * np.arange(nlin + 1)
    geo = [lin[-1]]
    while geo[-1] < subg.T0_RH:
        geo.append(min(geo[-1] * 1.3, subg.T0_RH))
    return np.concatenate([lin, np.asarray(geo[1:], float)])


def triv_exact(ph):
    """Int 2 phit(u) e^{-u/2} / (e^{2u} - 1) du, GL_N per segment
    (analytic integrand on [U0, 2 alpha], U0 > 0)."""
    v, f, s = ph["v"], ph["f"], ph["s"]
    tot = 0.0
    for a, b, fa, sl in zip(v[:-1], v[1:], f[:-1], s):
        mid = 0.5 * (a + b)
        half = 0.5 * (b - a)
        u = mid + half * _GLX
        phi = fa + sl * (u - a)
        tot += half * float(np.dot(
            _GLW, 2.0 * phi * np.exp(-0.5 * u) / np.expm1(2.0 * u)))
    return tot


def triv_bound(ph):
    """CLXXXI trivial-zero envelope (subgamma verbatim algebra)."""
    v, f = ph["v"], ph["f"]
    supg = 2.0 * np.maximum(np.abs(f[:-1]), np.abs(f[1:])) \
        * np.exp(-0.5 * v[:-1])
    wseg = 0.5 * (np.log(1.0 - np.exp(-2.0 * v[1:]))
                  - np.log(1.0 - np.exp(-2.0 * v[:-1])))
    return float(np.sum(supg * wseg))


def hat_c(ph, s):
    """Exact transform Int phit(u) e^{s u} du for complex s (per-
    segment closed form; s = i gamma reproduces the jump form)."""
    v, f, sl = ph["v"], ph["f"], ph["s"]
    ig = 1.0 / s
    e0 = np.exp(s * v[:-1])
    e1 = np.exp(s * v[1:])
    val = e1 * (f[1:] * ig - sl * ig ** 2) \
        - e0 * (f[:-1] * ig - sl * ig ** 2)
    return complex(np.sum(val))


def rung_exact(alpha, M, D, L, gam, s2t):
    """Verified-zero supply of one rung: R_hat_f, TAILB_f and the
    half-truncation zero sums for folds 0..FBAND."""
    tc = float(gam[-1])
    nz = len(gam)
    nh = nz // 2
    ph0 = subg.build_phit(alpha, M, D, L, 0)
    E = np.exp(1j * np.outer(gam, ph0["v"]))
    tg = tail_grid(D, tc)
    tail_t0 = 4.0 * math.exp(alpha) * s2t
    vmax = float(ph0["v"][-1])
    inv2 = np.sum(1.0 / gam ** 2)
    inv3 = np.sum(1.0 / gam ** 3)
    out = {}
    for j in range(0, FBAND + 1):
        ph = subg.build_phit(alpha, M, D, L, j)
        se = ph["pl2"] / (LN2 - subg.U0)
        main_ext = 2.0 * (2.0 * (math.exp(0.5 * LN2)
                                 * (ph["pl2"] - 2.0 * se)
                                 - math.exp(0.5 * subg.U0)
                                 * (-2.0 * se)))
        hat_re = (-(E @ ph["J"]) / gam ** 2).real
        zs_full = 4.0 * float(np.sum(hat_re))
        zs_half = 4.0 * float(np.sum(hat_re[:nh]))
        t_ex = triv_exact(ph)
        t_bd = triv_bound(ph)
        c = subg.tenv_of(ph, tg[:-1], tg[1:]) / tg[:-1] ** 2
        zs_tail = subg.abel_upper(tg, c, n_start=float(nz))
        dps_pad = 4.0 * ph["sd"] * (vmax * inv2 + 2.0 * inv3) \
            * DPS_ERR
        triv_pad = 1.0e-12 * (1.0 + abs(t_ex))
        tailb = 4.0 * zs_tail + tail_t0 * ph["sd"] + dps_pad \
            + triv_pad
        out[j] = dict(r_hat=main_ext - zs_full - t_ex,
                      r_hat_half=main_ext - zs_half - t_ex,
                      tailb=tailb, main_ext=main_ext,
                      triv_ex=t_ex, triv_bd=t_bd,
                      zs_full=zs_full, ph=ph)
    return out


def rung_assembly_new(rb, ex, y_core, v_core, h, Gc, mu1):
    """The CLXXXIV composed chain with the verified-zero supply."""
    L = rb["L"]
    f, wg, xg = mono.fold_grid(L)
    daf = np.abs(rb["d_ar"][f])
    dfv = rb["d_tot"][f]
    v_core = np.asarray(v_core, float)
    dd = np.full(len(f), rb["de_env"])
    nn = min(FBAND + 1, len(dd))
    for j in range(nn):
        fd = rb["folds"][j]
        s_dir = abs(fd["main"] + ex[j]["r_hat"]) + ex[j]["tailb"]
        dd[j] = min(fd["S"], s_dir)
    out = dict(dom_new=float(np.max(np.maximum(dfv, 0.0)
                                    - (daf + dd))),
               truth=float(np.linalg.eigvalsh(Gc)[0]))
    K = mono.kernel_of(xg, wg * (daf + dd), y_core, h)
    if K is None:
        return None
    Gom = np.sqrt(v_core)[:, None] * K * np.sqrt(v_core)[None, :]
    dif = Gc - 0.5 * (Gom + Gom.T)
    out["loewner"] = (float(np.linalg.eigvalsh(
        0.5 * (dif + dif.T))[0])
        / max(float(np.linalg.norm(Gc, 2)), 1e-300))
    out["l5_id"] = vhead.spectrum_identity(K, v_core)[0]
    v_lo = np.array([rb["folds"][j]["w_geo"]
                     * (rb["folds"][j]["H"]
                        - min(rb["folds"][j]["sup_min"],
                              ex[j]["r_hat"] + ex[j]["tailb"]))
                     for j in CORE_J])
    out["v_lo"] = v_lo
    out["vlo_excess"] = float(np.max(v_lo - v_core
                                     * (1.0 + VLO_TOL) - 1e-15))
    out["vpos"] = bool(np.all(v_lo > 0.0))
    out["floor"] = vhead.bnd(K, v_lo) if out["vpos"] else 0.0
    out["b_sup_new"] = vhead.bnd(K, v_core)
    out["mu1"] = mu1
    out["cert"] = bool(out["vpos"] and out["floor"] > mu1)
    return out


def own_sieve(nmax):
    """Independent prime-power comb (this source only; no pipeline
    arrays): positions ln n, masses 2 Lambda(n)/sqrt(n)."""
    sv = np.ones(nmax + 1, bool)
    sv[:2] = False
    for q in range(2, int(math.isqrt(nmax)) + 1):
        if sv[q]:
            sv[q * q::q] = False
    lam = np.zeros(nmax + 1)
    for p in np.nonzero(sv)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= nmax:
            lam[q] = lp
            q *= p
    nn = np.nonzero(lam > 0.0)[0]
    return np.log(nn.astype(float)), \
        2.0 * lam[nn] / np.sqrt(nn.astype(float))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join([labels.get(k, "-")
                              for k in ("v1", "v2", "v3", "v4",
                                        "v5")])
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: a certified rung is a FINITE statement -- the W1
  v-positivity + floor half on the deployed window from the cited
  inputs (gamma_1, Platt-Trudgian T0 = 3e12 [on-line status of the
  summed zeros AND the tail split], Rosser 1941 N(T), Buethe 2018,
  B_PSI, verified ordinates with declared error budget) plus exact
  window algebra and the exact composition [L1/L2/L5].  The deep
  28/28 in any composed count is CITED from the CLXXXIV frozen run,
  not recomputed.  The rho consumption keeps the CLXXIX measured
  inputs.  The composition is world-blind and is NOT a wall
  certificate; W2 / wall / background cancellation remain RH-hard
  and untouched.  A finite verified-zero sum can never prove RH.
  NO RH claim; no marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.J16SUPPLY.01 -- the verified-zero exact "
            "supply at the j = 16 seat (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = {}
    for tag, mod in (("parent", parent), ("subgamma", subg),
                     ("monocomp", mono), ("vhead", vhead),
                     ("lowfreq", lf), ("rho", rho),
                     ("assembly", asm)):
        shas[tag] = hashlib.sha256(
            mod.__doc__.encode("utf-8")).hexdigest()
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED):")
    print("      gamma_1 = %.6f (first-zero theorem, classical "
          "literature)" % subg.GAMMA1)
    print("      T0 = %.1e (Platt-Trudgian 2021, Bull. LMS 53: RH "
          "true up to 3e12 -> every summed zero is ON the critical"
          " line; zeros above T0 NOT assumed on-line)" % subg.T0_RH)
    print("      Rosser 1941 AJM 63 Thm 19 N(T) corridor "
          "(%.3f, %.3f, %.3f), T >= 2 -- tail only"
          % (subg.ROSSER_A, subg.ROSSER_B, subg.ROSSER_C))
    print("      Buethe 2018 (0.94 sqrt x, 11 < x <= 1e19) + table"
          " sups; B_PSI = %.5f (all x)" % core.B_PSI)
    print("      NEW INPUT CLASS (declared): verified zero "
          "ordinates n = 1..%d, mpmath.zetazero dps 15 (builder "
          "j16_zero_cache_build.py, disclosed), warded below; the "
          "CLXXXI zero-data ban is LIFTED for this probe BY DESIGN."
          % N_Z)
    if SMOKE:
        print("    *** SMOKE MODE: 6 surface steps, full-only "
              "wards deferred ***")
    check("S0 AST firewall clean (parent identifier ban kept)",
          not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced",
          shas["parent"] == PARENT_SHA, kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0c predecessor SPEC prefixes reproduced (%s)"
          % "/".join(PREFIXES[k] for k in sorted(PREFIXES)),
          ok_pref, kill="K2")

    # ------------------------------------------------------------ Z
    section("Z -- the verified-zero cache and its wards")
    check("Z0 cache present (%s)" % os.path.basename(ZC_NPY),
          os.path.exists(ZC_NPY), kill="K1")
    if KILLS:
        return finish({})
    gam = np.load(ZC_NPY)
    t_c = float(gam[-1])
    check("Z1 census %d == %d, strictly increasing, first == "
          "gamma_1 (dev %.1e)"
          % (len(gam), N_Z, abs(gam[0] - subg.GAMMA1)),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(gam[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    kk = np.arange(1, N_Z + 1, dtype=float)
    up_r = subg.n_up(gam + CORR_EPS)
    lo_r = subg.n_lo(gam + CORR_EPS)
    up_l = subg.n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z2 Rosser-corridor consistency per index (%d/%d both "
          "sides)" % (n_ok, N_Z), n_ok == N_Z, kill="K2")
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gam[i])))))
                  for i in idx)
    check("Z3 independent zeta spot check |zeta(1/2 + i gamma)| <= "
          "%.0e at %d sampled ordinates (worst %.1e)"
          % (ZETA_TOL, len(idx), worst_z), worst_z <= ZETA_TOL,
          kill="K2")
    print("    T_c = gamma_%d = %.4f << T0 = %.1e: every summed "
          "zero on-line unconditionally (Platt-Trudgian)"
          % (N_Z, t_c, subg.T0_RH))
    check("Z4 T_c below T0", t_c < subg.T0_RH, kill="K2")

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
    check("W3 CLXXVII reproduction (a med %.4f, b med %.4f)"
          % (a_med, b_med),
          abs(a_med / asm.REPRO_A_MED - 1.0) <= asm.REPRO_RTOL
          and abs(b_med / asm.REPRO_B_MED - 1.0) <= asm.REPRO_RTOL,
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
    check("E0 deep-table fidelity (overlap dev %.1e)" % dev,
          ok_tab, kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    lf.ENV.update(lf.table_sups(NN_e, psi_e, deep.TAB_EXT))
    check("E1 Buethe envelope warded (sup %.4f <= %.2f)"
          % (lf.ENV["BUETHE_SUP"], lf.BUETHE),
          lf.ENV["BUETHE_SUP"] <= lf.BUETHE, kill="K2")
    ratio_max = float(np.max(psi_e / NN_e.astype(float)))
    check("E2 global Chebyshev max psi/x = %.5f <= B_PSI %.5f"
          % (ratio_max, core.B_PSI), ratio_max <= core.B_PSI,
          kill="K2")
    s2t = subg.s2_tail()
    sig_tg = subg.rung_grid(0.25)
    sig2 = subg.abel_upper(sig_tg, 1.0 / sig_tg[:-1] ** 2,
                           n_start=0.0) + s2t
    check("E3 SIG2 sanity %.6f in [%.4f, %.2f]"
          % ((sig2,) + asm.SIG2_BAND),
          asm.SIG2_BAND[0] <= sig2 <= asm.SIG2_BAND[1], kill="K2")
    ce = vhead.loewner_counterexample()
    check("E4 Loewner counterexample FIRES (min eig %+.4f)" % ce,
          ce <= -asm.CE_MARGIN, kill="K3")

    # ------------------------------------------------------------ A
    section("A -- the surface: demand, old tier, verified-zero "
            "supply, heart wards")
    use = rows[:6] if SMOKE else rows
    alphas = [float(base.window_of(w["r2"]["kz"])["alpha"])
              for w in use]
    uu_s, mm_s = own_sieve(int(math.floor(
        math.exp(2.0 * max(alphas)) + 1.0e-9)))
    pay = []
    exact_worst = -1e18
    sieve_worst = 0.0
    hatc_worst = 0.0
    sound_old = -1e18
    tworst = 0.0
    env_ok = True
    triv_ok = True
    n_dom_o = n_loe_o = n_l5_o = n_grid_o = n_vlo_o = n_fs_o = 0
    n_dom_n = n_loe_n = n_l5_n = n_vlo_n = n_fs_n = 0
    slack = []
    rel_cells = []
    rel_dc = []
    conv = []
    for w in use:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rb = asm.rung_band(rr["alpha"], rr["M"], rr["uu"],
                           2.0 * rr["lam"], rr["c_ar"], s2t,
                           trans_wards=True)
        pa = asm.rung_assembly(rb, r2["y_core"], r2["v_core"],
                               r2["h"], w["Gc"], w["mu1"])
        ex = rung_exact(rr["alpha"], rr["M"], rb["D"], rb["L"],
                        gam, s2t)
        pn = rung_assembly_new(rb, ex, r2["y_core"], r2["v_core"],
                               r2["h"], w["Gc"], w["mu1"])
        if pa is None or pn is None:
            continue
        sound_old = max(sound_old, asm.fold_sound(rb))
        tworst = max(tworst, rb["tworst"])
        env_ok = env_ok and rb["env_ok"]
        tol_abs = EXACT_ABS * (1.0 + rb["l1_at"])
        keep_s = uu_s <= 2.0 * rr["alpha"] + 1e-14
        nodes = rb["D"] * np.arange(rr["M"] + 1)
        for j in range(0, FBAND + 1):
            fd = rb["folds"][j]
            res = abs(fd["r_true"] - ex[j]["r_hat"])
            exact_worst = max(exact_worst,
                              (res - ex[j]["tailb"] - tol_abs)
                              / (1.0 + rb["l1_at"]))
            slack.append(math.log10(ex[j]["tailb"]
                                    / max(res, 1e-300)))
            rel = res / max(abs(fd["d_at"]), 1e-300)
            rel_cells.append(rel)
            if j == 0:
                rel_dc.append(rel)
            resh = abs(fd["r_true"] - ex[j]["r_hat_half"])
            conv.append(resh / max(res, 1e-300))
            if abs(ex[j]["triv_ex"]) > ex[j]["triv_bd"] \
                    * (1.0 + 1e-9) + 1e-15:
                triv_ok = False
        for j in TSAMP:
            p = lf.phi_nodes(rr["M"], rb["L"], j)
            dsv = float(np.dot(mm_s[keep_s],
                               np.interp(uu_s[keep_s], nodes, p)))
            sieve_worst = max(sieve_worst,
                              abs(dsv - rb["folds"][j]["d_at"])
                              / (1.0 + abs(rb["folds"][j]["d_at"])))
        ph16 = ex[16]["ph"]
        hc = hat_c(ph16, 1j * 25.0)
        hj = subg.phit_hat_jump(ph16, 25.0)
        hatc_worst = max(hatc_worst, abs(hc - hj)
                         / (1.0 + ph16["sd"] / 625.0))
        n_dom_o += int(pa["dom_sup"] <= DOM_TOL)
        n_loe_o += int(pa["loewner"] >= -L2_TOL)
        n_l5_o += int(pa["l5_id"] <= L5_TOL)
        n_grid_o += int(pa["grid_dev"] <= GRID_TOL)
        n_vlo_o += int(pa["vlo_excess"] <= 0.0)
        n_fs_o += int(pa["floor"] <= pa["truth"]
                      * (1.0 + FLOOR_TOL) + 1e-15)
        n_dom_n += int(pn["dom_new"] <= DOM_TOL)
        n_loe_n += int(pn["loewner"] >= -L2_TOL)
        n_l5_n += int(pn["l5_id"] <= L5_TOL)
        n_vlo_n += int(pn["vlo_excess"] <= 0.0)
        n_fs_n += int(pn["floor"] <= pn["truth"]
                      * (1.0 + FLOOR_TOL) + 1e-15)
        pay.append(dict(kz=r2["kz"], h=float(r2["h"]),
                        alpha=float(rr["alpha"]), tau=w["tau"],
                        rb=rb, pa=pa, pn=pn, ex=ex, w=w))
        if len(pay) % 10 == 0:
            print("    ... %d rungs  [%.1f s]"
                  % (len(pay), time.time() - T0), flush=True)
    n = len(pay)
    check("A1 old-tier fold soundness (CLXXXIV verbatim; worst "
          "scaled excess %.2e)" % sound_old, sound_old <= 0.0,
          kill="K2")
    check("A2 THE HEART: |R_true - R_hat| <= TAILB on every rung x"
          " fold f <= %d (worst scaled excess %.2e)"
          % (FBAND, exact_worst), exact_worst <= 0.0, kill="K2")
    check("A3 THE HEART: independent sieve reproduces the pipeline"
          " reads (worst scaled dev %.2e <= %.0e)"
          % (sieve_worst, SIEVE_TOL), sieve_worst <= SIEVE_TOL,
          kill="K2")
    check("A4 transform wards: jump == segment (worst %.2e <= "
          "%.0e), complex-s form at delta = 0 (worst %.2e <= "
          "%.0e), envelope sound at sample gammas"
          % (tworst, TRANS_TOL, hatc_worst, HATC_TOL),
          tworst <= TRANS_TOL and hatc_worst <= HATC_TOL
          and env_ok, kill="K2")
    check("A5 trivial-zero term: |TRIV_exact| <= CLXXXI envelope "
          "on every rung x fold", triv_ok, kill="K2")
    check("A6 old-tier chain wards (dom/Loewner/L5/grid/v_lo/"
          "floor)", n_dom_o == n and n_loe_o == n and n_l5_o == n
          and n_grid_o == n and n_vlo_o == n and n_fs_o == n,
          "%d/%d each" % (min(n_dom_o, n_loe_o, n_l5_o, n_grid_o,
                              n_vlo_o, n_fs_o), n), kill="K3")
    check("A7 NEW-tier chain wards (dom/Loewner/L5/v_lo/floor)",
          n_dom_n == n and n_loe_n == n and n_l5_n == n
          and n_vlo_n == n and n_fs_n == n,
          "%d/%d each" % (min(n_dom_n, n_loe_n, n_l5_n, n_vlo_n,
                              n_fs_n), n), kill="K3")
    slack = np.array(slack)
    rel_cells = np.array(rel_cells)
    rel_dc = np.array(rel_dc)
    tails16 = np.array([p["ex"][16]["tailb"] for p in pay])
    print("    heart anatomy: soundness slack log10(TAILB/|resid|)"
          " %+.2f/%+.2f/%+.2f dex; TAILB_16 med %.4f"
          % (band(slack) + (float(np.median(tails16)),)))
    print("    1e-6-relative target census: |resid|/|d_at| <= "
          "%.0e on %d/%d band cells (med rel %.1e); DC reads "
          "%d/%d (med %.1e)"
          % (REL_TARGET, int(np.sum(rel_cells <= REL_TARGET)),
             len(rel_cells), float(np.median(rel_cells)),
             int(np.sum(rel_dc <= REL_TARGET)), len(rel_dc),
             float(np.median(rel_dc))))
    print("    truncation convergence (anatomy): med "
          "|resid(N_Z/2)| / |resid(N_Z)| = %.2f over %d cells"
          % (float(np.median(np.array(conv))), len(conv)))
    check("A8 heart anatomy recorded", True)

    # ------------------------------------------------------------ B
    section("B -- CLXXXIV demand reproduction")
    dm = np.array([p["rb"]["delta_meas"] for p in pay])
    dl = np.array([p["rb"]["delta_lag"] for p in pay])
    de = np.array([p["rb"]["de_env"] for p in pay])
    meds = (float(np.median(dm)), float(np.median(dl)),
            float(np.median(de)))
    supf_med = tuple(float(np.median(
        [p["rb"]["folds"][j]["sup_f"] for p in pay]))
        for j in CORE_J)
    prof_old = tuple(sum(1 for p in pay
                         if p["rb"]["folds"][j]["H"]
                         > p["rb"]["folds"][j]["sup_min"])
                     for j in CORE_J)
    prof_b = tuple(sum(1 for p in pay
                       if p["rb"]["folds"][j]["sup_b"]
                       < p["rb"]["folds"][j]["H"])
                   for j in CORE_J)
    bud_env = np.array([math.log10(p["pa"]["b_env"] / p["pa"]["mu1"])
                        for p in pay])
    n_envpos = sum(1 for p in pay
                   if p["pa"]["b_env"] > p["pa"]["mu1"])
    old_cert = sum(1 for p in pay if p["pa"]["cert"])
    open_old = [p for p in pay if not p["pa"]["cert"]]
    sh16 = [math.log10(p["rb"]["folds"][16]["sup_min"]
                       / p["rb"]["folds"][16]["H"])
            for p in open_old if p["rb"]["folds"][16]["H"] > 0]
    print("    old v-profile %s | Buethe %s | old cert %d/%d | "
          "open %d" % (prof_old, prof_b, old_cert, n,
                       len(open_old)))
    if sh16:
        print("    old j16 shortfall med %+.3f max %+.3f dex "
              "(CLXXXIV: +0.462 / +1.404)"
              % (float(np.median(sh16)), float(np.max(sh16))))
    if not SMOKE:
        check("B1 Delta meds %.1f/%.1f/%.1f == 381/382/802" % meds,
              all(abs(m / r - 1.0) <= asm.REPRO_D_RTOL
                  for m, r in zip(meds, asm.REPRO_D)), kill="K2")
        check("B2 CLXXXI SUP_F fold-med profile reproduced",
              all(abs(m / r - 1.0) <= asm.SUPF_RTOL
                  for m, r in zip(supf_med, asm.SUPF_MED_REF)),
              str(tuple(round(x, 3) for x in supf_med)),
              kill="K2")
        check("B3 old v-closure profile == %s"
              % (asm.FOLD_MIN_PROFILE,),
              prof_old == asm.FOLD_MIN_PROFILE, str(prof_old),
              kill="K2")
        check("B4 Buethe profile == %s" % (asm.FOLD_B_PROFILE,),
              prof_b == asm.FOLD_B_PROFILE, str(prof_b),
              kill="K2")
        check("B5 ENV budget med %+.2f == +%.2f (atol %.2f), > mu1"
              " on %d/39"
              % (float(np.median(bud_env)), asm.VHEAD_BUD_REF,
                 asm.VHEAD_BUD_ATOL, n_envpos),
              abs(float(np.median(bud_env)) - asm.VHEAD_BUD_REF)
              <= asm.VHEAD_BUD_ATOL and n_envpos == 39, kill="K2")
        check("B6 CLXXXIV demand seat reproduced: old cert %d == "
              "%d, j16 shortfall med %+.3f == +%.3f / max %+.3f =="
              " +%.3f (atol %.2f)"
              % (old_cert, OLD_CERT_REF, float(np.median(sh16)),
                 SH16_MED_REF, float(np.max(sh16)), SH16_MAX_REF,
                 SH16_ATOL),
              old_cert == OLD_CERT_REF
              and abs(float(np.median(sh16)) - SH16_MED_REF)
              <= SH16_ATOL
              and abs(float(np.max(sh16)) - SH16_MAX_REF)
              <= SH16_ATOL, kill="K2")
    else:
        print("    (smoke: B1-B6 full-surface reproduction wards "
              "deferred to the frozen run -- disclosed)")
        check("B1-B6 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ C
    section("C -- THE CLOSURE CENSUS (verified-zero supply)")
    prof_new = tuple(sum(1 for p in pay
                         if p["rb"]["folds"][j]["H"]
                         > min(p["rb"]["folds"][j]["sup_min"],
                               p["ex"][j]["r_hat"]
                               + p["ex"][j]["tailb"]))
                     for j in CORE_J)
    n_vpos_new = sum(1 for p in pay if p["pn"]["vpos"])
    n_cert_new = sum(1 for p in pay if p["pn"]["cert"])
    print("    new v-closure profile %s (old %s)"
          % (prof_new, prof_old))
    print("    NEW: v_lo > 0 on %d/%d, CERTIFIED %d/%d (old %d)"
          % (n_vpos_new, n, n_cert_new, n, old_cert))
    cm_new = [math.log10(p["pn"]["floor"] / p["pn"]["mu1"])
              for p in pay if p["pn"]["floor"] > 0.0]
    if cm_new:
        print("    composed margin log10(FLOOR_new/mu1) band "
              "%+.2f/%+.2f/%+.2f dex (n=%d)"
              % (band(np.array(cm_new)) + (len(cm_new),)))
    print("    per-rung j16 table on the %d previously open rungs:"
          % len(open_old))
    print("      kz    h     H_16    s_new_16  seat dex  "
          "FLOOR/mu1  cert")
    seat_m = []
    for p in sorted(open_old, key=lambda q: q["h"]):
        fd = p["rb"]["folds"][16]
        sn = p["ex"][16]["r_hat"] + p["ex"][16]["tailb"]
        sm = math.log10(fd["H"] / sn) if sn > 0 and fd["H"] > 0 \
            else float("inf")
        seat_m.append(sm)
        print("      %-4d  %-4d %+8.3f %+9.4f  %+7.2f   %+7.2f   "
              "%s" % (p["kz"], p["h"], fd["H"], sn, sm,
                      math.log10(p["pn"]["floor"] / p["pn"]["mu1"])
                      if p["pn"]["floor"] > 0 else float("nan"),
                      p["pn"]["cert"]))
    still = [p for p in pay if not p["pn"]["cert"]]
    if still:
        resc = [-math.log10(p["rb"]["folds"][16]["H"]
                            / (p["ex"][16]["r_hat"]
                               + p["ex"][16]["tailb"]))
                for p in still
                if p["rb"]["folds"][16]["H"] > 0
                and p["ex"][16]["r_hat"] + p["ex"][16]["tailb"] > 0]
        print("    residual census: %d rungs still open, j16 "
              "shortfall %s dex" % (len(still),
                                    ["%+.2f" % x for x in resc]))
    loss_v = [math.log10(p["pn"]["floor"] / p["pn"]["b_sup_new"])
              for p in pay if p["pn"]["floor"] > 0.0]
    if loss_v:
        print("    v-floor substitution cost med %+.2f dex"
              % float(np.median(loss_v)))
    if not SMOKE and n_cert_new == n:
        print("\n  " + "*" * 72)
        print("  THE COMPOSED RESULT (finite, stated with its "
              "constants):")
        print("  SURFACE 39/39 CERTIFIED from cited inputs + "
              "verified-zero data:")
        print("  gamma_1 = 14.134725; Platt-Trudgian 2021 T0 = "
              "3e12 (on-line status of")
        print("  the %d summed zeros, T_c = %.1f, AND the tail "
              "split); Rosser 1941" % (N_Z, t_c))
        print("  N(T) (0.137, 0.443, 1.588) on the tail only; "
              "Buethe 2018; B_PSI;")
        print("  exact window algebra + explicit formula + exact "
              "composition L1/L2/L5.")
        print("  WITH THE DEEP HALF 28/28 CITED from the CLXXXIV "
              "frozen run (37a5e259..):")
        print("  the W1 assembly criterion is met on 67/67 -- the "
              "FULL deployed surface")
        print("  + depth.  FINITE statement: W1 v-positivity + "
              "floor half only; W2 /")
        print("  wall / background remain RH-hard and untouched.  "
              "NO RH claim.")
        print("  " + "*" * 72)
    check("C1 closure census recorded", True)

    # ------------------------------------------------------------ D
    section("D -- the bandwidth c-ladder (CLXXXIII currency)")
    print("    fold | med dev | med S_old | med S_new | med c_eff"
          " old | new")
    for j in (2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32):
        devs, so, sn_l = [], [], []
        for p in pay:
            fd = p["rb"]["folds"][j]
            devs.append(fd["dev"])
            so.append(fd["S"])
            sn_l.append(min(fd["S"], abs(fd["main"]
                                         + p["ex"][j]["r_hat"])
                            + p["ex"][j]["tailb"]))
        devs = np.array(devs)
        so = np.array(so)
        sn_l = np.array(sn_l)
        print("      f=%2d | %7.3f | %9.3f | %9.3f | %8.2f | %6.2f"
              % (j, float(np.median(devs)), float(np.median(so)),
                 float(np.median(sn_l)),
                 float(np.median(so / np.maximum(devs, 1e-300))),
                 float(np.median(sn_l / np.maximum(devs,
                                                   1e-300)))))
    ce16, ce32, cj16 = [], [], []
    for p in pay:
        for j in range(1, FBAND + 1):
            fd = p["rb"]["folds"][j]
            sn = min(fd["S"], abs(fd["main"] + p["ex"][j]["r_hat"])
                     + p["ex"][j]["tailb"])
            cev = sn / max(fd["dev"], 1e-300)
            if j <= 16:
                ce16.append(cev)
            ce32.append(cev)
            if j == 16:
                cj16.append(cev)
    med16 = float(np.median(np.array(ce16)))
    med32 = float(np.median(np.array(ce32)))
    medj = float(np.median(np.array(cj16)))
    print("    NEW band c_eff: f <= 16 med %.3f (CLXXXIV %.2f) | "
          "f <= 32 med %.3f (%.2f) | j16 seat med %.3f (%.2f)"
          % (med16, LADDER_REF["band16"], med32,
             LADDER_REF["band32"], medj, LADDER_REF["j16"]))
    check("D1 c-ladder recorded", True)

    # ------------------------------------------------------------ R
    section("R -- the rho chain on the new certified set")
    res_meas = []
    for p in pay:
        w = p["w"]
        B, PG, a, b = rho.step_objects(w["M"], w["Gc"], w["Q"])
        rm = rho.chain_eval(w["M"], B, PG, a, b)
        p["rho_obj"] = (B, PG)
        res_meas.append(rm)
    rho_arr = np.array([r["rho"] for r in res_meas])
    if not SMOKE:
        check("R1 CLXXVI rho census reproduced (med %.4f, max "
              "%.4f)" % (float(np.median(rho_arr)),
                         float(np.max(rho_arr))),
              abs(float(np.median(rho_arr)) / asm.RHO_MED_REF
                  - 1.0) <= asm.RHO_RTOL
              and abs(float(np.max(rho_arr)) / asm.RHO_MAX_REF
                      - 1.0) <= asm.RHO_RTOL, kill="K2")
    else:
        print("    (smoke: rho census med %.4f max %.4f on %d "
              "steps -- full ward deferred)"
              % (float(np.median(rho_arr)),
                 float(np.max(rho_arr)), n))
        check("R1 deferred in smoke (disclosed)", True)
    certs = [p for p in pay if p["pn"]["cert"]]
    n_rho_pos = 0
    m_sup_min = float("inf")
    sound_rho = True
    for p in certs:
        B, PG = p["rho_obj"]
        rs = rho.chain_eval(p["w"]["M"], B, PG,
                            p["pn"]["floor"], 0.0)
        if rs["m_h12"] > 0.0:
            n_rho_pos += 1
            m_sup_min = min(m_sup_min, rs["m_h12"])
        if rs["m_h12"] > rs["margin"] + 1e-12:
            sound_rho = False
    if certs:
        print("    supplied-floor chain (a, b) = (FLOOR_new, 0) on"
              " the %d certified rungs: composed 1-rho margin "
              "positive on %d/%d (min %.3e)"
              % (len(certs), n_rho_pos, len(certs),
                 m_sup_min if n_rho_pos else float("nan")))
        check("R2 supplied-chain soundness m_sup <= measured",
              sound_rho, kill="K2")
    else:
        check("R2 no certified seat (disclosed)", True)

    # ------------------------------------------------------------ M
    section("M -- controls (must fire)")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("M1 %s world fires/refuses" % kind, fired, detail,
              kill="K2")
    rr9 = base.window_of(base.CTRL_KZ)
    rr9s = base.window_of(base.CTRL_KZ, scramble_seed=1)
    rb9 = asm.rung_band(rr9["alpha"], rr9["M"], rr9["uu"],
                        2.0 * rr9["lam"], rr9["c_ar"], s2t)
    ex9 = rung_exact(rr9["alpha"], rr9["M"], rb9["D"], rb9["L"],
                     gam, s2t)
    c9t = np.asarray(core.atom_lags_at(
        rr9s["alpha"], rr9s["M"], rr9s["uu"],
        2.0 * rr9s["lam"])[0], float)
    d9s = base.grid_density(c9t)
    nf9 = min(FBAND, rr9["M"] - 1)
    moves = []
    viol = 0
    for j in range(0, nf9 + 1):
        fd = rb9["folds"][j]
        if abs(fd["d_at"]) > 1e-300:
            moves.append(abs(float(d9s[j]) - fd["d_at"])
                         / abs(fd["d_at"]))
        if abs(float(d9s[j]) - (fd["main"] + ex9[j]["r_hat"])) \
                > ex9[j]["tailb"]:
            viol += 1
    med_mv = float(np.median(moves)) if moves else 0.0
    check("M2 scramble density movement med %.3f >= %.2f"
          % (med_mv, MOVE_BAR), med_mv >= MOVE_BAR, kill="K2")
    check("M3 CONTROL C-i: scramble breaks the exact prime-side "
          "ward on %d/%d band folds (>= %d)"
          % (viol, nf9 + 1, SCR_MIN), viol >= SCR_MIN, kill="K2")
    ph9 = ex9[16]["ph"]
    g1 = float(gam[0])
    on_pair = 4.0 * float((-(np.exp(1j * g1 * ph9["v"])
                             @ ph9["J"]) / g1 ** 2).real)
    dlt = IMP_BETA - 0.5
    quad = 2.0 * (hat_c(ph9, dlt + 1j * g1).real
                  + hat_c(ph9, -dlt + 1j * g1).real)
    r_hat9 = ex9[16]["r_hat"]
    r_imp = r_hat9 + on_pair - quad
    res9 = abs(rb9["folds"][16]["r_true"] - r_hat9)
    ratio = abs(r_imp - r_hat9) / max(res9, 1e-300)
    check("M4 CONTROL C-ii: off-line impostor (gamma_1 -> beta = "
          "%.2f) shifts R_hat_16 by %.4f = %.1e x the genuine "
          "residual (>= %.0f)"
          % (IMP_BETA, abs(r_imp - r_hat9), ratio, IMP_RATIO_MIN),
          ratio >= IMP_RATIO_MIN, kill="K2")
    n_sm_use = n_sm_rep = 0
    for w in [p["w"] for p in
              pay[::max(1, len(pay) // CTRL_NKZ)][:CTRL_NKZ]]:
        kz = w["r2"]["kz"]
        g = base.gram_anatomy(kz, world_fn=base.world_smooth,
                              keep_chain=True)
        if not isinstance(g, dict) or not g.get("core_ok"):
            print("    smooth kz %-4d refused (no seat)" % kz)
            continue
        rrw = base.window_of(kz)
        uu_w, mm_w = base.world_smooth(rrw["uu"],
                                       2.0 * rrw["lam"], rrw)
        rb_s = asm.rung_band(rrw["alpha"], rrw["M"], uu_w, mm_w,
                             rrw["c_ar"], s2t)
        Pc = base.eval_chain(g["chain"][0], g["chain"][1],
                             g["chain"][2], g["y_core"], g["h"])
        Gw = np.sqrt(g["v_core"])[:, None] * (Pc @ Pc.T) \
            * np.sqrt(g["v_core"])[None, :]
        pa_s = asm.rung_assembly(rb_s, g["y_core"], g["v_core"],
                                 g["h"], 0.5 * (Gw + Gw.T),
                                 4.0 * math.sin(
                                     math.pi
                                     / (2 * g["h"] + 1)) ** 2)
        n_sm_use += 1
        ok_rep = pa_s is not None and pa_s["dom_sup"] <= DOM_TOL \
            and pa_s["loewner"] >= -L2_TOL
        n_sm_rep += int(ok_rep)
        print("    smooth kz %-4d composition %s (declared world-"
              "blind outcome)"
              % (kz, "REPRODUCES" if ok_rep else "breaks"))
    check("M5 discrimination seat recorded (composition world-"
          "blind; the prime consumption sits in the exact supply)",
          True)

    # ------------------------------------------------------------ S
    section("S -- tau screens (surface)")
    taus = np.array([p["tau"] for p in pay])
    fl = np.array([p["pn"]["floor"] / p["pn"]["mu1"] for p in pay])
    vseat = np.array([p["rb"]["folds"][16]["H"]
                      - (p["ex"][16]["r_hat"]
                         + p["ex"][16]["tailb"]) for p in pay])
    lab_f, _sf = parent.screen(fl, taus)
    lab_v, _sv = parent.screen(vseat, taus)
    print("    TAU-SCREEN new composed margin  %s" % lab_f)
    print("    TAU-SCREEN new v-seat margin    %s" % lab_v)
    check("S1 screens recorded", True)

    # ------------------------------------------------------ verdicts
    seat_pos = [(p["alpha"],
                 math.log10(p["rb"]["folds"][16]["H"]
                            / (p["ex"][16]["r_hat"]
                               + p["ex"][16]["tailb"])))
                for p in pay
                if p["rb"]["folds"][16]["H"] > 0
                and p["ex"][16]["r_hat"] + p["ex"][16]["tailb"]
                > 0]
    if len(seat_pos) >= 3:
        sl_s, r2_s = parent.ols_line(
            np.array([x[0] for x in seat_pos]),
            np.array([x[1] for x in seat_pos]))
    else:
        sl_s, r2_s = float("nan"), float("nan")
    print("\n    ALL-H ANATOMY: new v-seat margin trend %+.3f "
          "dex/alpha (R2 %.2f, n=%d)" % (sl_s, r2_s,
                                         len(seat_pos)))
    if n_cert_new == n and not SMOKE:
        v1 = ("J16SUPPLY-SURFACE-CLOSED(39/39 certified, was 7; "
              "min seat margin %+.2f dex, min composed margin "
              "%+.2f dex; W1 assembly criterion 39/39 + 28/28 "
              "deep CITED = 67/67)"
              % (min(x[1] for x in seat_pos),
                 float(np.min(np.array(cm_new)))))
    elif n_cert_new == n:
        v1 = ("J16SUPPLY-SMOKE-CLOSED(%d/%d on the smoke subset; "
              "the frozen run decides)" % (n_cert_new, n))
    elif n_cert_new > OLD_CERT_REF:
        v1 = ("J16SUPPLY-PARTIAL(%d/%d certified, was %d; new "
              "v-profile %s; %d rungs still open, limiter = "
              "TAILB(T_c = %.0f) vs the true seat margins)"
              % (n_cert_new, n, old_cert, prof_new, len(still),
                 t_c))
    else:
        v1 = "J16SUPPLY-VOID(%d/%d, was %d)" % (n_cert_new, n,
                                                old_cert)
    v2 = ("FORMULA-EXACT-WARDED(worst excess %.1e; med slack "
          "%+.2f dex; sieve %.1e; rel target %.0e met on %d/%d "
          "cells, DC %d/%d)"
          % (exact_worst, float(np.median(slack)), sieve_worst,
             REL_TARGET, int(np.sum(rel_cells <= REL_TARGET)),
             len(rel_cells), int(np.sum(rel_dc <= REL_TARGET)),
             len(rel_dc)))
    if med32 <= LADDER_REF["band32"] * 0.95:
        v3 = ("C-LADDER-SHARPENED(f <= 32 med %.2f vs %.2f; "
              "f <= 16 %.2f vs %.2f; j16 %.2f vs %.2f)"
              % (med32, LADDER_REF["band32"], med16,
                 LADDER_REF["band16"], medj, LADDER_REF["j16"]))
    else:
        v3 = "C-LADDER-UNMOVED(f <= 32 med %.2f)" % med32
    v4 = ("SEAT-TREND(%+.3f dex/alpha, R2 %.2f; screens composed "
          "%s, v-seat %s -- ANATOMY)"
          % (sl_s, r2_s, lab_f.split("(")[0], lab_v.split("(")[0]))
    if viol >= SCR_MIN and ratio >= IMP_RATIO_MIN \
            and n_sm_use > 0 and n_sm_rep == n_sm_use:
        v5 = ("DISCRIMINATION-FIRES(scramble %d/%d, impostor "
              "%.0fx, smooth reproduces %d/%d)"
              % (viol, nf9 + 1, ratio, n_sm_rep, n_sm_use))
    else:
        v5 = ("DISCRIMINATION-UNRESOLVED(scramble %d/%d, impostor"
              " %.1f, smooth %d/%d)"
              % (viol, nf9 + 1, ratio, n_sm_rep, n_sm_use))
    check("V1 typed: %s" % v1, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
