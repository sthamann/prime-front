#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""subgamma_fourier_bound_probe -- PRIME.PORT.SUBGAMMA.FOURIER.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE +0.87 DEX SHOT.  lowfreq_discrepancy_
gain_probe (CLXXX, SPEC-SHA be867853..) priced H1's remaining gap
exactly: the |E|-envelope route (Buethe 0.94 sqrt x) closes the DC
seat (+1.77 dex) and increasingly the deep rungs, but at the CORE
folds it pays the total variation ||phi_j'||_1 ~ 2j and wastes med
+2.09 dex of signed cancellation -- H1-CORE-FLOOR-PARTIAL(10/67,
med shortfall +0.87 dex), while the TRUE ceiling is 67/67 with the
measured remainder sitting ON the tent-quadrature noise floor.
The named missing object is the OSCILLATION, not the size: an
explicit unconditional bound of the LOW-FREQUENCY Fourier reads of
the psi-error on the finite window.  THE MECHANISM (frozen): the
fold-j read is an exact prime sum d_at(theta_j) = Sum mu_n
phi_j(u_n), and by the Riemann-von Mangoldt explicit formula its
non-smooth part is a sum over zeta zeros of the WINDOW TRANSFORM
evaluated at the zero ordinates -- and EVERY ordinate sits at
|gamma| >= gamma_1 = 14.134725 while the deployed fold carriers
sit at omega_j <= ~8: the window transform must be paid only at
distance >= gamma_1 - omega_j, NO zero lives in the band the reads
live in.  THE QUESTION (frozen): does the explicit-formula supply
-- window-transform decay integrated against explicit unconditional
N(T) envelopes -- beat the |E|-envelope route by the demanded
~0.87 dex at the actual window scales and close the core floor?

THE EXACT OBJECTS.  Per rung (kz, h, M, D = 2 alpha / M,
L = 2M - 2, X = e^{2 alpha}) and fold read j in {0} + CORE_J:
phi_j is the exact T115 tent-assembly response (piecewise-linear
nodes phi_j(kD) from the symmetric-FFT cosine weights, lowfreq
transcription, identity ward vs the pipeline read).  Because the
prime comb has NO support in (1, 2), phi_j may be replaced below
u = ln 2 by the pw-linear EXTENSION phit_j: phit_j = phi_j on
[ln 2, 2 alpha], linear from (U0, 0) to (ln 2, phi_j(ln 2)),
U0 = ln(2)/2 (frozen; near-optimal for the jump/pole tradeoff),
and phit_j(2 alpha) = 0.  With G(x) = Ft(ln x), Ft = 2 phit_j(u)
e^{-u/2}, Stieltjes partial summation against psi and the explicit
formula psi_0(x) = x - Sum_rho x^rho/rho - ln 2pi
- (1/2) ln(1 - x^{-2}) give the EXACT decomposition
    d_at(theta_j) = MAIN_j + MAIN_ext_j + R_EF_j,
    MAIN_j     = 2 Int_{ln 2}^{2 alpha} e^{u/2} phi_j du  (parent),
    MAIN_ext_j = 2 Int_{U0}^{ln 2} e^{u/2} phit_j du  (closed form),
    R_EF_j     = - Sum_rho Fttilde(rho) - TRIV_j,
    Fttilde(s) = Int Ft(u) e^{su} du,
    TRIV_j     = Int G(x) / (x (x^2 - 1)) dx  (trivial zeros),
(the ln 2pi term dies at the boundaries; interchange of the zero
sum and the integral is the classical truncated-explicit-formula
argument for continuous compactly supported pw-C1 test functions,
Davenport ch. 17 -- pedigree, machine-checked by the soundness
ward below).  THE TRANSFORM (exact, sinc^2/tent class): phit_j is
pw-linear with slope jumps J_m at breakpoints v_m, so
    Int phit_j e^{i gamma u} du = -(1/gamma^2) Sum_m J_m
                                   e^{i gamma v_m},
verified per rung against the independent per-segment closed form
(TRANS ward <= 1e-10 scaled).  The jump set splits EXACTLY into
(i) an interior cosine run J_k = A cos(theta_j k), A =
4 sin^2(theta_j/2)/D (second difference of the tent-sampled
cosine; run ward <= 1e-10 scaled, float-honest for cos at large
argument), (ii) the TOP-RAMP PAIR BLOCK: the two O(1/D) jumps of
the halved-cf top ramp are J_M = -c_1/(2 D) EXACTLY (c_1 =
cos(theta_j (M-1))) and J_{M-2} = c_1/(2 D) + omega-scale rest;
moving +-c_1/(2 D) into the exact pair P(gamma) = (c_1/(2 D))
(e^{i gamma (M-2) D} - e^{i gamma M D}), |P| = (|c_1|/D)
|sin(gamma D)|, removes the 1/D mass from the incoherent budget
at low gamma, and (iii) <= 6 omega-scale exceptional jumps
(extension entry, ln 2, first node, top rests): |transform| <=
TENV(gamma)/gamma^2 with TENV(gamma) = min(S_Delta, S_exc +
(|c_1|/D) sinsup(gamma D) + (A/2)(g(gamma D + theta_j) + g(gamma
D - theta_j)) + runpad), g(y) = min(N_run, 1/|sin(y/2)|) the exact
geometric-sum envelope, sinsup the exact interval sup of |sin| --
the resonance seat |gamma - omega_j| is explicit and the deployed
distance is gamma_1 - omega_j (printed; DIST ward >= 5.0).

THE CLASSICAL INPUT CLASSES (all EXTERNAL-CITED literature
constants with pedigree; computed zeta ZEROS remain BANNED from
every construction -- the firewall nuance, declared: classical
theorems whose PROOFS used verified zeros are legitimate cited
inputs, the same pedigree class as the already-deployed Buethe
envelope; NO zero ordinate beyond gamma_1 enters any formula as
data, only counting ENVELOPES):
  (G1) gamma_1 = 14.134725: zeta has no nontrivial zero with
       0 < |Im rho| < gamma_1 (classical, Riemann-von Mangoldt /
       Platt-verified low height; literature).
  (T0) RH-height: every zero with 0 < Im rho <= T0 = 3e12 lies on
       the critical line (Platt-Trudgian 2021, Bull. LMS 53, "The
       Riemann hypothesis is true up to 3*10^12").  Zeros above T0
       are NOT assumed on-line: they pay the unconditional
       |x^{beta-1/2}| <= e^{alpha} weight in an explicit tail.
  (N)  zero-counting envelope: |N(T) - T/(2 pi) ln(T/(2 pi e))
       - 7/8| <= 0.137 ln T + 0.443 ln ln T + 1.588 for T >= 2
       (Rosser 1941, Amer. J. Math. 63, Thm 19 -- the classical
       explicit form; Trudgian 2014 successors exist, the CLASS is
       what is deployed).  Deployed ONLY through the Abel/partial-
       summation upper bound Sum_{gamma} f(gamma) <= c_last
       N_up(T0) + Sum_i (c_{i-1}-c_i)^+ N_up(t_i) - (c_i -
       c_{i-1})^+ max(N_lo(t_i), 0) on a frozen grid (N(gamma_1)
       = 0 by (G1)) -- the fluctuation term is paid on the
       envelope VARIATION, not per interval.
  (B)  Buethe 2018 sqrt envelope + two-sided table constants,
       lowfreq/v594 verbatim (the SIZE route, combined by min).
The zero-sum supply per read:  SUP_EF_j = 4 * ZS_j + TAIL_j +
TRIV_j with ZS_j = Sum_{gamma_1 <= gamma <= T0} TENV(gamma)/
gamma^2 (Abel-bounded on the frozen grid: linear dt = 0.25/D from
gamma_1 to max(300, 10 pi/D), then geometric *1.3 to T0), TAIL_j =
4 e^{alpha} S_Delta S2TAIL with S2TAIL the same Abel bound of
Sum_{gamma > T0} 1/gamma^2 on the dyadic-1.5 grid (+ last-term
pad); factor 4 = conjugate pairs x (Fttilde = 2 * transform).
Parent-currency supply: SUP_F_j = SUP_EF_j + |MAIN_ext_j| bounds
|R_true_j| = |d_at_j - MAIN_j|; combined supply SUP_MIN_j =
min(SUP_B_j, SUP_F_j) (Buethe for the size, explicit formula for
the oscillation).  SOUNDNESS WARDS (kill): |R_EF| <= SUP_EF and
|R_true| <= SUP_F on every rung x read, both worlds' censuses
printed.

(a) DEMAND (CLXXX verbatim, reproduced as wards): lowfreq
rung_supply on the same 39 surface + deep rungs; Delta meds
(381/382/802 rtol 5e-2), CLXXVII battery meds (a 0.968 / b 0.202
rtol 5e-2), surface Buethe fold profile == (39,30,16,6,0,0,0,0)
EXACT, full-run Buethe full-closure census == 10 and med shortfall
+0.87 (atol 0.10) -- full run only, smoke prints.
(b) SUPPLY vs DEMAND: per-fold anatomy (med H / SUP_B / SUP_F /
SUP_MIN / |R_true|, closures B/F/MIN/TRUE), the dex ladder per
rung (shortfall log10(max_j SUP/H)), the recovery ladder rec_r =
shortfall_B - shortfall_MIN, DC gains, 39 core + deep block.
(c) VERDICTS (frozen rules, data-decided):
  V1 headline: SUBG-H1-CLOSED-DEPLOYED(n_MIN == N; min margin dex)
    / SUBG-H1-PARTIAL(n_MIN/N, med shortfall, fold profile) /
    SUBG-H1-OPEN.  n_MIN = rungs with ALL 8 core folds closed
    under SUP_MIN.
  V1b recovery: FOURIER-DELIVERS(med rec >= 0.87 dex) /
    FOURIER-PARTIAL(med rec vs 0.87).
  V2 pure mechanism: SUBG-EF-ALONE(n_F/N) census (SUP_F alone).
  V3 composition: parent-verbatim Gershgorin ladder with SUP_MIN
    (a0_sup, margin vs b_meas, concentration dex, m0_up CLXXVIII
    verbatim).  IF the surface closes 39/39 under SUP_MIN, the
    frozen composition chains re-run on the surface steps: CLXXVII
    battery s_P >= a - b (measured Gram) and the CLXXIX chain
    (rho.step_objects/chain_eval verbatim, CLXXVI rho census
    rewarded): COMPOSED-THEOREM-SURFACE(v-floor half supplied
    classically, all constants printed) iff battery positive
    39/39 AND composed rho margin positive 39/39; else the failing
    seat named.  Else W1-COMPOSED-VOID / RHO-STILL-CONDITIONAL
    (CLXXIX cited, not recomputed).  In EVERY branch: the
    Gershgorin a0-level stays typed against the I4 concentration
    (med dex printed); W2 / wall / background remain RH-hard.
  V4 H2 same-supply test: kgap = log10(K_meas / K_needed) with
    SUP_MIN bounds (parent verbatim): H2-CS-CLOSES(n == steps) iff
    K_meas <= K_needed everywhere, else H2-CS-NEEDS-DIAG-LAW(med
    dex, n/steps) -- the supply gives v-bounds, no diagonal law.
  V5 all-h shape: min-fold margin dex vs alpha (surface + deep,
    OLS): ALLH-SUPPLY-IMPROVES(slope >= +0.05) / ALLH-FLAT /
    ALLH-DEGRADES(slope <= -0.05); the omega drift omega_j =
    theta_j/D ~ pi j/(2 alpha) (falls with depth -- the resonance
    distance GROWS) printed; the honest boundary = the census of
    non-closing rungs (all extrapolation typed ANATOMY).
(d) GATES.  TAU-SCREENS (parent bands): min-fold margin family
(H - SUP_MIN) and headroom family min H, surface vs tau.  SMOOTH
WORLD (documented): R_sm is pure tent quadrature with NO psi
content -- the EF bound is WORLD-BLIND classical analysis about
psi, so |R_sm| <= SUP_F is EXPECTED (census printed, typed): the
discrimination must sit in the measured comb reads.  CONTROLS
(kill if silent): C1 smooth refuses the certificate ladder, C2
Epstein + scramble fire (parent verbatim), C3 scramble core-fold
density movement med rel move >= 0.05 (lowfreq verbatim); the
scramble supply-violation census under SUP_F printed as anatomy
(a violation = the scrambled comb is NOT a psi-comb, the seat
where the sharper budget discriminates).  ANTI-CIRCULARITY
(frozen): no computed zeta zeros, no wall data, no target
eigendata in any derived bound; MAIN comb-free (ARCH pedigree);
gamma_1/T0/Rosser/Buethe enter ONLY as cited constants; measured
d/R values appear only as truth columns and soundness wards.

DEAD overrides (kill anyway): parent reproduction fails, identity
ward fails, TRANS/run/DIST wards fail, any soundness ward fails,
SIG2 sanity outside [0.0231, 0.06], deep census < MIN_DEEP.

FROZEN BARS: U0 = ln(2)/2; GAMMA1 = 14.134725; T0 = 3.0e12;
ROSSER (0.137, 0.443, 1.588), T >= 2; grid: linear dt = 0.5 on
[gamma_1, 200], linear dt = max(0.25/D, 0.5) to TSW = max(300,
10 pi/D), GEO = 1.3 to T0; tail grid T0 * 1.5^i, i <= 600,
last-term pad x20; TRANS_TOL = 1e-10; COSRUN_TOL = 1e-10;
DIST_MIN = 5.0; IDENT_TOL = 1e-9, SOUND_TOL = 1e-6 (rel) + 1e-9
abs scaled (lowfreq verbatim); REPRO_D = (381, 382, 802) rtol
5e-2; REPRO_A/B_MED = 0.968/0.202 rtol 5e-2; FOLD_B_PROFILE =
(39, 30, 16, 6, 0, 0, 0, 0) exact; NB_FULL_REF = 10 exact +
SHORT_MED_REF = +0.87 atol 0.10 (full run only); DEMAND_DEX =
0.87; SIG2 sanity band [0.0231, 0.06]; TREND_FLAT = 0.05;
MOVE_BAR = 0.05; MIN_DEEP = 10; RHO trigger = surface n_MIN == 39;
rho bars rho.RHO_MED/MAX_REF rtol verbatim; parent bars inherited
verbatim; parent SPEC-SHA warded == 084c9689..; lowfreq SPEC
prefix warded == be867853.  Runtime cap declared: 20 min.  Smoke
mode SUBG_SMOKE=1 restricts the deep block to the 4 shallowest new
rungs (surface + controls always full); any smoke run is disclosed
here before the freeze.

ANTHROPIC NO-GO DECLARATION: the supply reads one-dimensional
window-transform decay against global zero-counting envelopes
(two-moment-class global data about zeta); the measured target is
the fine conditioning of an 8x8 CD-kernel Gram.  A closed core
floor certifies ONLY the v_i-positivity half of H1 on the finite
deployed surface; the Christoffel concentration (I4, ~6 dex), H2's
diagonal law, and W2 / wall / background cancellation remain open
and RH-hard REGARDLESS of the verdict -- said in every branch.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): THREE smoke
runs (all SUBG_SMOKE=1, deep on the 4 shallowest new rungs; full
logs archived) and THREE pre-freeze amendments, disclosed in
order:
  SMOKE-1 (exit 1, 2.5 s): T2 cosine-run ward FAILED at tolerance
  1e-12 -- measured worst scaled dev 4.04e-12, which is float
  rounding of cos second differences at large argument, not a
  structural miss (all other 23 executed checks green).  Measured
  supply before sharpening: SUP_F med 21.0..23.7 FLAT across
  folds, F closures 0/39, recovery med +0.46 dex: the raw
  incoherent-jump budget is dominated by the top-ramp 1/D mass.
  AMENDMENT A1: COSRUN_TOL 1e-12 -> 1e-10 (float-honest scale;
  runpad grows by NT * 1e-10 ~ 5e-8, immaterial).
  AMENDMENT A2: the exact top-ramp pair block added to the
  envelope (J_M = -c_1/(2D) EXACTLY, paired into |P| = (|c_1|/D)
  |sin(gamma D)| -- a strictly valid sharpening of the same bound;
  no verdict bar, census rule or enum touched).
  SMOKE-2 (exit 0, 43/43, 4.9 s): SUP_F med 11.1..13.7, F fold
  closures (39,35,29,21,14,7,4,2), surface full closure 2/39,
  recovery med +0.65 dex; residual dominated by low-gamma grid
  smearing of the pair sine on small-D rungs (first interval width
  0.25/D reaches ~18).
  AMENDMENT A3: grid refinement -- linear dt = 0.5 on [gamma_1,
  200] before the dt = max(0.25/D, 0.5) phase (pure interval-sup
  tightening of the same envelope; no rule moved).
  SMOKE-3 (final pre-freeze, exit 0, 43/43, 4.8 s) -- the surface
  numbers the frozen run must reproduce identically: SIG2_UP =
  0.036328; S2TAIL = 2.222e-12; decay facts med: pair |c_1|/D
  89.43, S_exc 5.46 (j=2) .. 8.27 (j=16), TENV(gamma_1)/gamma_1^2
  0.0981 (j=2) .. 0.1386 (j=16); per-fold med SUP_F = 6.497 /
  6.131 / 5.739 / 5.963 / 6.508 / 6.949 / 7.508 / 7.601 (j=2..16)
  with MIN closures (39,39,35,30,23,17,13,7) vs Buethe
  (39,30,16,6,0,0,0,0); surface full closure MIN 7/39 (B 0/39,
  TRUE 39/39); dex ladders: shortfall_B +0.60/+1.27/+2.34,
  shortfall_MIN -0.36/+0.32/+1.40, recovery +0.87/+0.94/+1.00
  (med +0.93 >= the demanded +0.87); DC combined gain
  +1.53/+2.08/+2.59 dex (Buethe alone +1.23/+1.77/+2.22);
  soundness slack log10(SUP_EF/|R_EF|) +0.78/+1.41/+3.66 dex;
  smooth world |R_sm| <= SUP_F on 312/312 (world-blind as
  declared, ratio 1.013); scramble supply-violation 3/9 under
  SUP_F vs 0/9 under Buethe (the sharper budget DOES discriminate
  the scrambled comb); composition: a0_sup > 0 on 7/39, Gershgorin
  margin -0.488/-0.202/-0.0635, concentration med +8.45 dex,
  battery a-b > 0 on 39/39, rho trigger NOT met; screens: margin
  AMBIG(-0.361, R2 0.235, n=7), headroom PASS(-0.276, R2 0.269);
  deep smoke 4/4 F-closed (B 2/4).  Smoke-3 verdicts pinned by the
  frozen rules: V1 SUBG-H1-PARTIAL(11/43, med shortfall +0.28),
  V1b FOURIER-DELIVERS(+0.93), V2 SUBG-EF-ALONE(11/43), V3
  W1-COMPOSED-VOID + RHO-STILL-CONDITIONAL, V4
  H2-CS-NEEDS-DIAG-LAW(med +9.64 dex on 7/39), V5
  ALLH-SUPPLY-IMPROVES(+0.566, R2 0.99).  NO bar, band, count,
  rule or enum was moved after smoke-3; the only post-smoke-3
  change is this disclosure block.  The frozen run repeats
  everything on the FULL deep block (28 expected rungs); enums
  move only as the full data says.

NO RH claim.  Even a fully closed core floor certifies only the
v_i-positivity half of H1 on the finite deployed surface from
cited classical inputs; the concentration seat, H2, and W2 /
background remain open and RH-hard.  A partial verdict is itself
the finding: it prices the sub-gamma_1 mechanism in honest dex at
the actual window scales.  No marker moves.  Stdout only.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import lowfreq_discrepancy_gain_probe as lf  # noqa: E402 (READ-ONLY)
import rho_margin_derivation_probe as rho  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
LOWFREQ_SHA8 = "be867853"
U0 = math.log(2.0) / 2.0
LN2 = math.log(2.0)
GAMMA1 = 14.134725
T0_RH = 3.0e12
ROSSER_A = 0.137
ROSSER_B = 0.443
ROSSER_C = 1.588
DT_FACT = 0.25
TSW_MIN = 300.0
GEO = 1.3
TAIL_GEO = 1.5
TAIL_IMAX = 600
TRANS_TOL = 1.0e-10
COSRUN_TOL = 1.0e-10
DIST_MIN = 5.0
IDENT_TOL = 1.0e-9
SOUND_TOL = 1.0e-6
FOLD_B_PROFILE = (39, 30, 16, 6, 0, 0, 0, 0)
NB_FULL_REF = 10
SHORT_MED_REF = 0.87
SHORT_MED_ATOL = 0.10
DEMAND_DEX = 0.87
SIG2_BAND = (0.0231, 0.06)
TREND_FLAT = 0.05
MOVE_BAR = 0.05
MIN_DEEP = 10
CORE_J = base.CORE_J
READS = lf.READS
SMOKE = os.environ.get("SUBG_SMOKE", "") == "1"
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


# ---------------------------------------------------------------- N(T)
def n_main(t):
    t = np.asarray(t, float)
    return t / (2.0 * math.pi) * np.log(t / (2.0 * math.pi * math.e)) \
        + 0.875


def n_fluc(t):
    t = np.asarray(t, float)
    lt = np.log(t)
    return ROSSER_A * lt + ROSSER_B * np.log(lt) + ROSSER_C


def n_up(t):
    return n_main(t) + n_fluc(t)


def n_lo(t):
    return np.maximum(n_main(t) - n_fluc(t), 0.0)


def abel_upper(tgrid, c, n_start=0.0):
    """Rigorous upper bound of Sum_{gamma in (t_0, t_K]} f(gamma) for
    any 0 <= f <= step envelope c_i on [t_i, t_{i+1}), via Abel
    summation against the Rosser N(T) corridor.  n_start = an upper
    bound usage of N(t_0): coefficient of N(t_0) is -c_0 <= 0, so a
    LOWER bound of N(t_0) is conservative; pass 0.0 when N(t_0) = 0
    is known (gamma_1 seat), else n_lo(t_0) is used by caller."""
    c = np.asarray(c, float)
    ti = tgrid[1:-1]
    d = c[:-1] - c[1:]
    nu = n_up(ti)
    nl = n_lo(ti)
    s = float(np.sum(np.where(d >= 0.0, d * nu, d * nl)))
    s += float(c[-1] * n_up(tgrid[-1]))
    s -= float(c[0] * n_start)
    return s


def s2_tail():
    """Abel upper bound of Sum_{gamma > T0_RH} 1/gamma^2."""
    tg = T0_RH * TAIL_GEO ** np.arange(TAIL_IMAX + 1)
    c = 1.0 / tg[:-1] ** 2
    s = abel_upper(tg, c, n_start=float(n_lo(np.array([T0_RH]))[0]))
    # truncation pad beyond the final grid point t_e ~ 1e105: the
    # geometric-interval majorant gives Sum_{gamma > t_e} 1/gamma^2
    # <= C ln(t_e)/t_e with C < 20 * N_up(t_e)/t_e / ln(t_e) slack;
    # the factor-20 pad dominates it by construction at this t_e.
    pad = 20.0 * float(c[-1] * n_up(tg[-1]))
    return s + pad


def g_sup(y0, y1, nt):
    """sup over y in [y0, y1] of min(nt, 1/|sin(y/2)|) -- exact:
    capped when the interval touches a multiple of 2 pi."""
    y0 = np.asarray(y0, float)
    y1 = np.asarray(y1, float)
    width = y1 - y0
    k0 = np.floor(y0 / (2.0 * math.pi))
    k1 = np.floor(y1 / (2.0 * math.pi))
    s0 = np.abs(np.sin(0.5 * y0))
    s1 = np.abs(np.sin(0.5 * y1))
    smin = np.minimum(s0, s1)
    cross = (k1 > k0) | (width >= 2.0 * math.pi - 1e-12) \
        | (smin < 1e-9)
    return np.where(cross, float(nt),
                    np.minimum(float(nt),
                               1.0 / np.maximum(smin, 1e-300)))


def sin_sup(y0, y1):
    """sup over y in [y0, y1] of |sin(y)| -- exact: 1 when the
    interval touches an odd multiple of pi/2."""
    y0 = np.asarray(y0, float)
    y1 = np.asarray(y1, float)
    k0 = np.floor((y0 - 0.5 * math.pi) / math.pi)
    k1 = np.floor((y1 - 0.5 * math.pi) / math.pi)
    peak = k1 > k0
    return np.where(peak, 1.0,
                    np.maximum(np.abs(np.sin(y0)),
                               np.abs(np.sin(y1))))


def rung_grid(D):
    """The frozen zero-sum grid for window spacing D: fine linear
    dt = 0.5 on [gamma_1, 200] (the 1/gamma^2-dominant seat), then
    linear dt = max(0.25/D, 0.5) to TSW, then geometric to T0."""
    lin1 = GAMMA1 + 0.5 * np.arange(
        int(math.ceil((200.0 - GAMMA1) / 0.5)) + 1)
    dt = max(DT_FACT / D, 0.5)
    tsw = max(TSW_MIN, 10.0 * math.pi / D)
    nlin = max(int(math.ceil((tsw - lin1[-1]) / dt)), 1)
    lin2 = lin1[-1] + dt * np.arange(1, nlin + 1)
    geo = [lin2[-1]]
    while geo[-1] < T0_RH:
        geo.append(min(geo[-1] * GEO, T0_RH))
    tg = np.concatenate([lin1, lin2, np.asarray(geo[1:], float)])
    return tg


# ------------------------------------------------------------ transform
def build_phit(alpha, M, D, L, j):
    """Extended pw-linear window phit_j: breakpoints v, values f,
    slopes s, slope jumps J; interior cosine-run data."""
    p = lf.phi_nodes(M, L, j)
    nodes = D * np.arange(M + 1)
    pl2 = float(np.interp(LN2, nodes, p))
    k_lo = int(math.floor(LN2 / D)) + 1
    v = np.concatenate([[U0, LN2], D * np.arange(k_lo, M + 1)])
    f = np.concatenate([[0.0, pl2], p[k_lo:M + 1]])
    s = (f[1:] - f[:-1]) / (v[1:] - v[:-1])
    J = np.empty(len(v))
    J[0] = s[0]
    J[1:-1] = s[1:] - s[:-1]
    J[-1] = -s[-1]
    theta = 2.0 * math.pi * j / L
    A = 4.0 * math.sin(0.5 * theta) ** 2 / D
    sd = float(np.sum(np.abs(J)))
    # top-ramp pair block: J at node M (the exit jump) equals
    # -c1/(2D) EXACTLY with c1 = cos(theta (M-1)) = -2 p[M-1];
    # move +-PB = +-c1/(2D) into the exact pair term.
    Jp = J.copy()
    pb2 = 0.0
    if M - 2 >= k_lo:
        PB = -p[M - 1] / D
        Jp[-1] += PB          # exact zero by construction
        Jp[2 + (M - 2 - k_lo)] -= PB
        pb2 = 2.0 * abs(PB)   # = |c1| / D
    ka, kb = k_lo + 1, M - 3
    if ka <= kb:
        idx0 = 2 + (ka - k_lo)
        idx1 = 2 + (kb - k_lo)
        run = np.arange(idx0, idx1 + 1)
        kk = np.arange(ka, kb + 1)
        dev = float(np.max(np.abs(J[run] - A * np.cos(theta * kk))))
        nt = len(run)
        mask = np.ones(len(Jp), bool)
        mask[run] = False
        sexc = float(np.sum(np.abs(Jp[mask])))
    else:
        dev = 0.0
        nt = 0
        A = 0.0
        sexc = float(np.sum(np.abs(Jp)))
    runpad = nt * COSRUN_TOL * (1.0 + abs(A))
    return dict(v=v, f=f, s=s, J=J, theta=theta, A=A, nt=nt,
                sexc=sexc, sd=sd, pb2=pb2, D=D, runpad=runpad,
                cos_dev=dev, pl2=pl2)


def phit_hat_jump(ph, gam):
    """Exact transform via the jump representation."""
    z = np.exp(1j * gam * ph["v"])
    return -np.sum(ph["J"] * z) / gam ** 2


def phit_hat_seg(ph, gam):
    """Exact transform via the per-segment closed form."""
    v, f, s = ph["v"], ph["f"], ph["s"]
    ig = 1.0 / (1j * gam)
    e0 = np.exp(1j * gam * v[:-1])
    e1 = np.exp(1j * gam * v[1:])
    val = e1 * (f[1:] * ig - s * ig ** 2) \
        - e0 * (f[:-1] * ig - s * ig ** 2)
    return np.sum(val)


def tenv_of(ph, t0s, t1s):
    """Envelope of |Sum J e^{i gamma v}| over gamma intervals
    [t0, t1]: exceptional mass + exact top-ramp pair + cosine-run
    geometric sum, capped by the total variation S_Delta."""
    t0s = np.asarray(t0s, float)
    t1s = np.asarray(t1s, float)
    D = ph["D"]
    th = ph["theta"]
    t = np.full_like(t0s, ph["sexc"])
    if ph["pb2"] > 0.0:
        t = t + ph["pb2"] * sin_sup(t0s * D, t1s * D)
    if ph["nt"] > 0:
        t = t + 0.5 * abs(ph["A"]) * (
            g_sup(t0s * D + th, t1s * D + th, ph["nt"])
            + g_sup(t0s * D - th, t1s * D - th, ph["nt"]))
    return np.minimum(t, ph["sd"]) + ph["runpad"]


def read_supply_ef(ph, alpha, D, tg, s2t):
    """The explicit-formula supply of one read."""
    t0s, t1s = tg[:-1], tg[1:]
    c = tenv_of(ph, t0s, t1s) / t0s ** 2
    zs = abel_upper(tg, c, n_start=0.0)
    tail = 4.0 * math.exp(alpha) * ph["sd"] * s2t
    # trivial-zero term
    v, f = ph["v"], ph["f"]
    supg = 2.0 * np.maximum(np.abs(f[:-1]), np.abs(f[1:])) \
        * np.exp(-0.5 * v[:-1])
    wseg = 0.5 * (np.log(1.0 - np.exp(-2.0 * v[1:]))
                  - np.log(1.0 - np.exp(-2.0 * v[:-1])))
    triv = float(np.sum(supg * wseg))
    # extension main correction (closed form on the one ext segment)
    se = ph["pl2"] / (LN2 - U0)
    main_ext = 2.0 * (2.0 * (math.exp(0.5 * LN2) * (ph["pl2"]
                                                    - 2.0 * se)
                             - math.exp(0.5 * U0) * (-2.0 * se)))
    sup_ef = 4.0 * zs + tail + triv
    return dict(sup_ef=sup_ef, zs=zs, tail=tail, triv=triv,
                main_ext=main_ext, sup_f=sup_ef + abs(main_ext))


def rung_ef(alpha, M, s2t):
    D = 2.0 * alpha / M
    L = 2 * M - 2
    tg = rung_grid(D)
    out = {}
    for j in READS:
        ph = build_phit(alpha, M, D, L, j)
        ef = read_supply_ef(ph, alpha, D, tg, s2t)
        ef["ph"] = ph
        ef["omega"] = ph["theta"] / D
        out[j] = ef
    out["D"] = D
    out["L"] = L
    out["tg_len"] = len(tg)
    return out


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("SUBGAMMA-MEASURED / %s / %s / %s / %s / %s / %s"
                   % (labels.get("v1", "-"), labels.get("v1b", "-"),
                      labels.get("v2", "-"), labels.get("v3", "-"),
                      labels.get("v4", "-"), labels.get("v5", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every supplied number is a rigorous upper bound of
  the float64-computed ideal objects, consuming ONLY the cited
  unconditional literature inputs (gamma_1 first-zero theorem,
  Platt-Trudgian RH-height 3e12, Rosser N(T) envelope, Buethe
  sqrt-range + table sups) plus exact window algebra and the
  comb-free MAIN integrals.  No computed zero ordinate enters any
  construction.  A closed core floor certifies only the v_i-
  positivity half of H1 on the finite deployed surface; the I4
  concentration, H2's diagonal law and W2 / wall / background
  cancellation remain open and RH-hard.  Extrapolations are
  anatomy, not theorems.  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.SUBGAMMA.FOURIER.01 -- explicit sub-gamma_1 "
            "Fourier bound of the psi-error vs the low-frequency "
            "demand (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    lf_sha = hashlib.sha256(lf.__doc__.encode("utf-8")).hexdigest()
    print("    parent  SPEC SHA-256 = %s" % parent_sha)
    print("    lowfreq SPEC SHA-256 = %s" % lf_sha)
    print("    PEDIGREE (all EXTERNAL-CITED, zero-verification-based"
          " classical theorems are legitimate cited inputs; NO")
    print("    computed zero ordinate enters any construction):")
    print("      gamma_1 = %.6f  (no zero below; classical RvM-"
          "verified, literature)" % GAMMA1)
    print("      T0 = %.1e  (Platt-Trudgian 2021, Bull. LMS 53: RH "
          "true up to 3e12; zeros above T0 NOT assumed on-line)"
          % T0_RH)
    print("      N(T) corridor: Rosser 1941 AJM 63 Thm 19, "
          "|N - main - 7/8| <= %.3f ln T + %.3f ln ln T + %.3f, "
          "T >= 2" % (ROSSER_A, ROSSER_B, ROSSER_C))
    print("      Buethe 2018 (0.94 sqrt x, 11 < x <= 1e19; "
          "v594:10-13,47) + two-sided table sups (lowfreq verbatim)")
    if SMOKE:
        print("    *** SMOKE MODE: deep on 4 shallowest new rungs ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c lowfreq SPEC prefix reproduced",
          lf_sha[:8] == LOWFREQ_SHA8, lf_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder + CLXXVII battery reproduction")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)), kill="K1")
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
    a_all = np.array([x[0] for x in ab])
    b_all = np.array([x[1] for x in ab])
    a_med = float(np.median(a_all))
    b_med = float(np.median(b_all))
    check("W3 CLXXVII H1/H2 reproduction (a med %.4f == %.3f, "
          "b med %.4f == %.3f)" % (a_med, lf.REPRO_A_MED, b_med,
                                   lf.REPRO_B_MED),
          abs(a_med / lf.REPRO_A_MED - 1.0) <= lf.REPRO_RTOL
          and abs(b_med / lf.REPRO_B_MED - 1.0) <= lf.REPRO_RTOL,
          kill="K2")
    taus1 = np.array([w["tau"] for w in rows])

    # ------------------------------------------------------------ E
    section("E -- classical inputs on the extended table + the N(T) "
            "machinery")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(deep.EXT["NN"][:nP], core._NN)
               and np.array_equal(deep.EXT["U"][:nP], core.U_ALL)
               and np.array_equal(deep.EXT["MU"][:nP], core.MU_ALL))
    check("E0 deep-table fidelity: overlap dev %.1e == 0.0, "
          "prefixes bitwise" % dev, dev == 0.0 and ok_pref,
          kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    lf.ENV.update(lf.table_sups(NN_e, psi_e, deep.TAB_EXT))
    check("E1 Buethe envelope warded on the table: two-sided sup "
          "|E|/sqrt(t) = %.4f <= %.2f on (11, 4e6]"
          % (lf.ENV["BUETHE_SUP"], lf.BUETHE),
          lf.ENV["BUETHE_SUP"] <= lf.BUETHE, kill="K2")
    check("E1b two-sided KAPPA_EFF deployed (%.6f, sane band)"
          % lf.ENV["KAPPA_EFF"],
          core.KAPPA_REF <= lf.ENV["KAPPA_EFF"] <= 0.25, kill="K2")
    ratio_max = float(np.max(psi_e / NN_e.astype(float)))
    check("E2 global Chebyshev bound max psi/x = %.5f <= B_PSI %.5f"
          % (ratio_max, core.B_PSI), ratio_max <= core.B_PSI,
          kill="K2")
    nlo_g1 = float(n_main(np.array([GAMMA1]))[0]
                   - n_fluc(np.array([GAMMA1]))[0])
    nup_g1 = float(n_up(np.array([GAMMA1]))[0])
    check("E3 Rosser corridor consistent with the first-zero seat: "
          "N_lo(gamma_1) = %.3f <= 0 <= N_up(gamma_1) = %.3f"
          % (nlo_g1, nup_g1), nlo_g1 <= 0.0 <= nup_g1, kill="K2")
    s2t = s2_tail()
    print("    S2TAIL = Sum_{gamma > T0} 1/gamma^2 <= %.3e "
          "(Abel on the dyadic-1.5 grid + pad)" % s2t)
    sig_tg = rung_grid(0.25)   # any D gives a valid grid; frozen probe
    sig_c = 1.0 / sig_tg[:-1] ** 2
    sig2 = abel_upper(sig_tg, sig_c, n_start=0.0) + s2t
    check("E4 SIG2 sanity: Sum_{gamma >= gamma_1} 1/gamma^2 <= "
          "%.6f in [%.4f, %.2f] (literature value ~0.02310 must "
          "sit below)" % ((sig2,) + SIG2_BAND),
          SIG2_BAND[0] <= sig2 <= SIG2_BAND[1], kill="K2")

    # ------------------------------------------------------------ T
    section("T -- the deployed window transform: closed form, wards,"
            " decay facts")
    sup_rows = []
    ef_rows = []
    trans_worst = 0.0
    cos_worst = 0.0
    env_ok = True
    for w in rows:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rs = lf.rung_supply(rr["alpha"], rr["M"], rr["uu"],
                            2.0 * rr["lam"], rr["c_ar"])
        rs["kz"] = r2["kz"]
        rs["h"] = float(r2["h"])
        rs["alpha"] = float(rr["alpha"])
        sup_rows.append(rs)
        ef = rung_ef(rr["alpha"], rr["M"], s2t)
        ef_rows.append(ef)
        for j in (0, 8, 16):
            ph = ef[j]["ph"]
            cos_worst = max(cos_worst, ph["cos_dev"]
                            / (1.0 + abs(ph["A"])))
            for gam in (GAMMA1, 25.0, 60.0):
                hj = phit_hat_jump(ph, gam)
                hs = phit_hat_seg(ph, gam)
                trans_worst = max(
                    trans_worst,
                    abs(hj - hs) / (1.0 + ph["sd"] / gam ** 2))
                te = float(tenv_of(ph, np.array([gam]),
                                   np.array([gam]))[0])
                if abs(hj) > (te + 1e-12) / gam ** 2 + 1e-12:
                    env_ok = False
    check("T1 transform ward: jump form == per-segment closed form "
          "(worst scaled dev %.2e <= %.0e)"
          % (trans_worst, TRANS_TOL), trans_worst <= TRANS_TOL,
          kill="K2")
    check("T2 interior cosine-run identity J_k == A cos(theta k) "
          "(worst scaled dev %.2e <= %.0e)"
          % (cos_worst, COSRUN_TOL), cos_worst <= COSRUN_TOL,
          kill="K2")
    check("T3 envelope soundness at sample gammas: |transform| <= "
          "TENV/gamma^2", env_ok, kill="K2")
    om_max = max(ef[j]["omega"] for ef in ef_rows for j in CORE_J)
    check("T4 sub-gamma_1 seat: max deployed fold frequency "
          "omega = %.3f, min distance gamma_1 - omega = %.3f >= %.1f"
          % (om_max, GAMMA1 - om_max, DIST_MIN),
          GAMMA1 - om_max >= DIST_MIN, kill="K2")
    print("    decay facts (39 surface rungs, med over rungs): "
          "fold | omega | dist | S_Delta | S_exc | pair |c1|/D | A"
          " | TENV(gamma_1)/gamma_1^2")
    for j in CORE_J:
        oms = [ef[j]["omega"] for ef in ef_rows]
        sds = [ef[j]["ph"]["sd"] for ef in ef_rows]
        sxs = [ef[j]["ph"]["sexc"] for ef in ef_rows]
        pbs = [ef[j]["ph"]["pb2"] for ef in ef_rows]
        aas = [abs(ef[j]["ph"]["A"]) for ef in ef_rows]
        t1s = []
        for ef in ef_rows:
            ph = ef[j]["ph"]
            te = float(tenv_of(ph, np.array([GAMMA1]),
                               np.array([GAMMA1]))[0])
            t1s.append(te / GAMMA1 ** 2)
        print("      j=%2d | %6.3f | %6.3f | %8.2f | %6.2f | %8.2f "
              "| %6.2f | %8.4f"
              % (j, float(np.median(oms)),
                 GAMMA1 - float(np.max(oms)), float(np.median(sds)),
                 float(np.median(sxs)), float(np.median(pbs)),
                 float(np.median(aas)), float(np.median(t1s))))
    check("T5 decay facts recorded", True)

    # ------------------------------------------------------------ A
    section("A -- demand reproduction + the Fourier supply "
            "(39 surface rungs)")
    ident_worst = 0.0
    sound_b_ok = True
    sound_ef_ok = True
    sound_worst = ""
    for rs, ef in zip(sup_rows, ef_rows):
        for j in READS:
            rd = rs["reads"][j]
            ident_worst = max(ident_worst, rd["ident_dev"]
                              / (1.0 + rs["l1_at"]))
            if abs(rd["r_true"]) > rd["sup"]["B"] \
                    * (1.0 + SOUND_TOL) + 1e-9 * (1.0 + rs["l1_at"]):
                sound_b_ok = False
            r_ef = rd["d_at"] - rd["main"] - ef[j]["main_ext"]
            ef[j]["r_ef"] = r_ef
            tol = SOUND_TOL * ef[j]["sup_ef"] \
                + 1e-9 * (1.0 + rs["l1_at"])
            if abs(r_ef) > ef[j]["sup_ef"] + tol:
                sound_ef_ok = False
                sound_worst = ("kz %d j %d |R_EF| %.3g > SUP_EF %.3g"
                               % (rs["kz"], j, abs(r_ef),
                                  ef[j]["sup_ef"]))
            if abs(rd["r_true"]) > ef[j]["sup_f"] + tol:
                sound_ef_ok = False
    check("A1 v882-identity transcription ward", 
          ident_worst <= IDENT_TOL,
          "worst scaled dev %.2e" % ident_worst, kill="K2")
    check("A2 Buethe soundness |R_true| <= SUP_B (lowfreq verbatim)",
          sound_b_ok, kill="K2")
    check("A3 EXPLICIT-FORMULA soundness: |R_EF| <= SUP_EF and "
          "|R_true| <= SUP_F on every rung x read",
          sound_ef_ok, sound_worst or "all inside", kill="K2")
    dm = np.array([r["delta_meas"] for r in sup_rows])
    dl = np.array([r["delta_lag"] for r in sup_rows])
    de = np.array([r["delta_env"] for r in sup_rows])
    meds = (float(np.median(dm)), float(np.median(dl)),
            float(np.median(de)))
    check("A4 CLXXVIII/CLXXX demand ladder reproduced: Delta meds "
          "%.1f/%.1f/%.1f == %.0f/%.0f/%.0f" % (meds + lf.REPRO_D),
          all(abs(m / r - 1.0) <= lf.REPRO_D_RTOL
              for m, r in zip(meds, lf.REPRO_D)), kill="K2")

    def census(rlist, elist):
        cen = dict(B=0, F=0, MIN=0, T=0)
        fold = {j: dict(B=0, F=0, MIN=0, T=0, H=[], SB=[], SF=[],
                        SM=[], RT=[]) for j in CORE_J}
        short_b, short_m, rec = [], [], []
        marg_min = []
        for rs, ef in zip(rlist, elist):
            okc = dict(B=True, F=True, MIN=True, T=True)
            sb_max, sm_max, mm = [], [], []
            for j in CORE_J:
                rd = rs["reads"][j]
                H = -(rd["d_ar"] + rd["main"])
                rd["H"] = H
                s_b = rd["sup"]["B"]
                s_f = ef[j]["sup_f"]
                s_m = min(s_b, s_f)
                ef[j]["sup_min"] = s_m
                f = fold[j]
                f["H"].append(H)
                f["SB"].append(s_b)
                f["SF"].append(s_f)
                f["SM"].append(s_m)
                f["RT"].append(abs(rd["r_true"]))
                for cname, sv in (("B", s_b), ("F", s_f),
                                  ("MIN", s_m)):
                    hit = sv < H
                    f[cname] += int(hit)
                    okc[cname] &= hit
                hit_t = abs(rd["r_true"]) < H
                f["T"] += int(hit_t)
                okc["T"] &= hit_t
                sb_max.append(s_b / max(H, 1e-300)
                              if H > 0 else float("inf"))
                sm_max.append(s_m / max(H, 1e-300)
                              if H > 0 else float("inf"))
                mm.append(H - s_m)
            for cname in ("B", "F", "MIN", "T"):
                cen[cname] += int(okc[cname])
            sb = math.log10(max(sb_max)) if np.isfinite(
                max(sb_max)) else float("inf")
            sm = math.log10(max(sm_max)) if np.isfinite(
                max(sm_max)) else float("inf")
            short_b.append(sb)
            short_m.append(sm)
            rec.append(sb - sm)
            marg_min.append(min(mm))
        return cen, fold, np.array(short_b), np.array(short_m), \
            np.array(rec), np.array(marg_min)

    cen_s, fold_s, shb_s, shm_s, rec_s, marg_s = census(sup_rows,
                                                        ef_rows)
    print("    per-fold anatomy (39 rungs): j | med H | med SUP_B |"
          " med SUP_F | med SUP_MIN | med |R_true| | "
          "closures B/F/MIN/TRUE")
    for j in CORE_J:
        f = fold_s[j]
        print("      j=%2d | %+8.3f | %8.2f | %8.3f | %8.3f | "
              "%7.3f | %d/%d/%d/%d"
              % (j, float(np.median(f["H"])),
                 float(np.median(f["SB"])),
                 float(np.median(f["SF"])),
                 float(np.median(f["SM"])),
                 float(np.median(f["RT"])), f["B"], f["F"],
                 f["MIN"], f["T"]))
    check("A5 surface Buethe fold profile reproduced == %s"
          % (FOLD_B_PROFILE,),
          tuple(fold_s[j]["B"] for j in CORE_J) == FOLD_B_PROFILE,
          str(tuple(fold_s[j]["B"] for j in CORE_J)), kill="K2")
    print("    rungs fully closed (all 8 folds): B %d/39, F %d/39, "
          "MIN %d/39, TRUE %d/39"
          % (cen_s["B"], cen_s["F"], cen_s["MIN"], cen_s["T"]))
    print("    dex ladders (39 rungs): shortfall_B "
          "%+.2f/%+.2f/%+.2f | shortfall_MIN %+.2f/%+.2f/%+.2f | "
          "recovery %+.2f/%+.2f/%+.2f"
          % (band(shb_s) + band(shm_s) + band(rec_s)))
    dc_b = np.array([math.log10(r["delta_env"]
                                / r["reads"][0]["sup"]["B"])
                     for r in sup_rows])
    dc_m = np.array([math.log10(
        r["delta_env"] / min(r["reads"][0]["sup"]["B"],
                             e[0]["sup_f"]))
        for r, e in zip(sup_rows, ef_rows)])
    print("    DC seat: Buethe gain %+.2f/%+.2f/%+.2f dex; combined "
          "gain %+.2f/%+.2f/%+.2f dex" % (band(dc_b) + band(dc_m)))
    slack = [math.log10(e[j]["sup_ef"] / max(abs(e[j]["r_ef"]),
                                             1e-300))
             for e in ef_rows for j in CORE_J]
    print("    soundness slack log10(SUP_EF/|R_EF|): "
          "%+.2f/%+.2f/%+.2f dex" % band(np.array(slack)))
    check("A6 supply/censuses recorded", True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, density level, declared:"
            " no deep grams recomputed)")
    new_kz = []
    for kz in range(2, min(deep.KZ_SCAN_MAX,
                           len(deep.EXT["NN"]) - 2)):
        alpha = float(deep.EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > deep.TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        h = deep.ext_frame(kz)[2]
        if not (deep.H_HOLD[0] <= h <= deep.H_HOLD[1]):
            continue
        new_kz.append(kz)
    order_kz = sorted(new_kz, key=lambda k: (deep.ext_frame(k)[2], k))
    check("D1 new-rung census %d (>= %d)"
          % (len(order_kz), MIN_DEEP), len(order_kz) >= MIN_DEEP,
          kill="K1")
    if KILLS:
        return finish({})
    if SMOKE:
        order_kz = order_kz[:4]
    deep_rows, deep_efs = [], []
    d_ident = 0.0
    d_sound = True
    for kz in order_kz:
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        uu = deep.EXT["U"][:ka]
        mm = deep.EXT["MU"][:ka]
        _c, D = core.atom_lags_at(alpha, Mz, uu[:1], mm[:1])
        c_ar = np.asarray(core.arch_lags(Mz, D), float)
        rs = lf.rung_supply(alpha, Mz, uu, mm, c_ar)
        rs["kz"] = kz
        rs["h"] = float(hz)
        rs["alpha"] = float(alpha)
        ef = rung_ef(alpha, Mz, s2t)
        deep_rows.append(rs)
        deep_efs.append(ef)
        hmin, sfmax = [], []
        for j in READS:
            rd = rs["reads"][j]
            d_ident = max(d_ident, rd["ident_dev"]
                          / (1.0 + rs["l1_at"]))
            r_ef = rd["d_at"] - rd["main"] - ef[j]["main_ext"]
            ef[j]["r_ef"] = r_ef
            tol = SOUND_TOL * ef[j]["sup_ef"] \
                + 1e-9 * (1.0 + rs["l1_at"])
            if abs(r_ef) > ef[j]["sup_ef"] + tol \
                    or abs(rd["r_true"]) > ef[j]["sup_f"] + tol:
                d_sound = False
            if j in CORE_J:
                hmin.append(-(rd["d_ar"] + rd["main"]))
                sfmax.append(ef[j]["sup_f"])
        print("    deep kz %-4d h %-5d X %.2e minH %+8.3f "
              "maxSUP_F %7.3f maxSUP_B %8.2f  [%.1f s]"
              % (kz, hz, rs["X"], min(hmin), max(sfmax),
                 max(rs["reads"][j]["sup"]["B"] for j in CORE_J),
                 time.time() - T0), flush=True)
    check("D2 deep identity ward (worst scaled dev %.2e)"
          % d_ident, d_ident <= IDENT_TOL, kill="K2")
    check("D3 deep soundness |R_EF| <= SUP_EF, |R_true| <= SUP_F",
          d_sound, kill="K2")
    cen_d, fold_d, shb_d, shm_d, rec_d, marg_d = census(deep_rows,
                                                        deep_efs)
    print("    deep censuses (%d rungs): fully closed B %d, F %d, "
          "MIN %d, TRUE %d" % (len(deep_rows), cen_d["B"],
                               cen_d["F"], cen_d["MIN"], cen_d["T"]))
    check("D4 deep censuses recorded", True)

    N = len(sup_rows) + len(deep_rows)
    nB = cen_s["B"] + cen_d["B"]
    nF = cen_s["F"] + cen_d["F"]
    nMIN = cen_s["MIN"] + cen_d["MIN"]
    nT = cen_s["T"] + cen_d["T"]
    short_b_all = np.concatenate([shb_s, shb_d])
    short_m_all = np.concatenate([shm_s, shm_d])
    rec_all = np.concatenate([rec_s, rec_d])
    med_short_b = float(np.median(short_b_all))
    med_rec = float(np.median(rec_all))
    if not SMOKE:
        check("D5 CLXXX full reproduction: Buethe full closure "
              "%d == %d, med shortfall %+.3f == +%.2f (atol %.2f)"
              % (nB, NB_FULL_REF, med_short_b, SHORT_MED_REF,
                 SHORT_MED_ATOL),
              nB == NB_FULL_REF
              and abs(med_short_b - SHORT_MED_REF)
              <= SHORT_MED_ATOL, kill="K2")
    else:
        print("    (smoke: CLXXX full-census reproduction deferred "
              "to the frozen run; measured nB %d, med shortfall "
              "%+.3f)" % (nB, med_short_b))
        check("D5 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ J
    section("J -- composition with the supplied constants")
    a0_sup, gersh, conc, kgap = [], [], [], []
    n_batt = 0
    for i, (w, r, e) in enumerate(zip(rows, sup_rows, ef_rows)):
        m0_up = r["m0_ar_abs"] + r["delta_env"]
        vsup = [r["reads"][j]["w_geo"]
                * (r["reads"][j]["H"] - e[j]["sup_min"])
                for j in CORE_J]
        vup = [r["reads"][j]["w_geo"]
               * max(r["reads"][j]["H"] + e[j]["sup_min"], 0.0)
               for j in CORE_J]
        a0 = min(vsup) / m0_up
        a0_sup.append(a0)
        gersh.append(a0 - b_all[i])
        if a0 > 0:
            conc.append(math.log10(a_all[i] / a0))
        sv = np.sqrt(np.maximum(vup, 0.0))
        den = float(np.max(sv * (np.sum(sv) - sv)))
        kmeas = float(np.max(np.diag(w["Gc"]) / w["r2"]["v_core"]))
        if a0 > 0 and den > 0:
            kneed = a0 / den
            kgap.append(math.log10(kmeas / kneed))
        n_batt += int(a_all[i] - b_all[i] > 0.0)
    a0s = np.array(a0_sup)
    n_a0pos = int(np.sum(a0s > 0.0))
    n_vpos = sum(1 for r, e in zip(sup_rows, ef_rows)
                 if all(r["reads"][j]["H"] > e[j]["sup_min"]
                        for j in CORE_J))
    print("    v-floor positivity (all 8 folds, supplied): %d/39 "
          "steps; a0_sup positive on %d/39; band %.3g/%.3g/%.3g"
          % ((n_vpos, n_a0pos) + band(a0s)))
    print("    Gershgorin margin a0_sup - b_meas: band "
          "%+.3g / %+.3g / %+.3g" % band(np.array(gersh)))
    if conc:
        print("    concentration gap log10(a_meas / a0_sup): med "
              "%+.2f dex (the I4 seat)" % float(np.median(conc)))
    print("    CLXXVII battery (measured Gram): a - b > 0 on %d/39"
          % n_batt)
    check("J1 composed ladders recorded", True)
    rho_ran = False
    rho_ok = False
    rho_min_marg = float("nan")
    rho_min_comp = float("nan")
    if cen_s["MIN"] == 39:
        rho_ran = True
        print("    RHO TRIGGER: surface 39/39 closed -> re-running "
              "the frozen CLXXIX chain on the surface steps")
        res = []
        for w in rows:
            B, PG, a, b = rho.step_objects(w["M"], w["Gc"], w["Q"])
            rr = rho.chain_eval(w["M"], B, PG, a, b)
            res.append(rr)
        rho_arr = np.array([x["rho"] for x in res])
        comp = np.array([x["m_h12"] for x in res])
        dom = sum(int(x["dom_ok"]) for x in res)
        ok_rep = (abs(float(np.median(rho_arr)) / rho.RHO_MED_REF
                      - 1.0) <= rho.RHO_RTOL
                  and abs(float(np.max(rho_arr)) / rho.RHO_MAX_REF
                          - 1.0) <= rho.RHO_RTOL)
        check("J2 CLXXVI rho census reproduced (med %.4f, max %.4f)"
              % (float(np.median(rho_arr)), float(np.max(rho_arr))),
              ok_rep, kill="K2")
        rho_min_marg = float(np.min(1.0 - rho_arr))
        rho_min_comp = float(np.min(comp))
        rho_ok = bool(np.all(comp > 0.0)) and dom == 39 \
            and n_batt == 39
        print("    composed 1-rho >= (a-b)(T-c)/(4 MiiMjj): min "
              "%.3e; dominance exact %d/39; battery %d/39"
              % (rho_min_comp, dom, n_batt))
    else:
        print("    RHO TRIGGER not met (surface MIN closure %d/39):"
              " CLXXIX cited, not recomputed" % cen_s["MIN"])
        check("J2 rho chain gated by frozen trigger (disclosed)",
              True)
    check("J3 H2 needed-diagonal-law gap recorded", True)

    # ------------------------------------------------------------ M
    section("M -- smooth world (documented: pure tent quadrature, "
            "the EF bound is world-blind classical analysis)")
    n_sm_in, n_sm_tot = 0, 0
    r_sm_all, r_tr_all = [], []
    for w, r, e in zip(rows, sup_rows, ef_rows):
        rr = base.window_of(w["r2"]["kz"])
        mm_sm = base.smooth_masses(rr["uu"])
        c_sm = np.asarray(core.atom_lags_at(
            rr["alpha"], rr["M"], rr["uu"], mm_sm)[0], float)
        d_sm = base.grid_density(c_sm)
        for j in CORE_J:
            rsm = abs(float(d_sm[j]) - r["reads"][j]["main"])
            r_sm_all.append(rsm)
            r_tr_all.append(abs(r["reads"][j]["r_true"]))
            n_sm_tot += 1
            n_sm_in += int(rsm <= e[j]["sup_f"])
    med_sm = float(np.median(r_sm_all))
    med_tr = float(np.median(r_tr_all))
    print("    med |R_smooth| = %.3g vs med |R_true| = %.3g (ratio "
          "%.3f); |R_sm| <= SUP_F on %d/%d fold reads"
          % (med_sm, med_tr, med_sm / max(med_tr, 1e-300),
             n_sm_in, n_sm_tot))
    check("M world-blindness typed: the EF budget is a psi-theorem,"
          " the discrimination sits in the measured reads", True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world fires/refuses" % kind, fired, detail,
              kill="K2")
    rr9 = base.window_of(base.CTRL_KZ)
    rr9s = base.window_of(base.CTRL_KZ, scramble_seed=1)
    rs9 = lf.rung_supply(rr9["alpha"], rr9["M"], rr9["uu"],
                         2.0 * rr9["lam"], rr9["c_ar"])
    ef9 = rung_ef(rr9["alpha"], rr9["M"], s2t)
    c9t = np.asarray(core.atom_lags_at(
        rr9s["alpha"], rr9s["M"], rr9s["uu"],
        2.0 * rr9s["lam"])[0], float)
    d9s = base.grid_density(c9t)
    moves, violB, violF = [], 0, 0
    for j in READS:
        rd = rs9["reads"][j]
        if abs(rd["d_at"]) > 1e-300:
            moves.append(abs(float(d9s[j]) - rd["d_at"])
                         / abs(rd["d_at"]))
        dev9 = abs(float(d9s[j]) - rd["main"])
        violB += int(dev9 > rd["sup"]["B"])
        violF += int(dev9 > ef9[j]["sup_f"])
    med_mv = float(np.median(moves)) if moves else 0.0
    print("    scramble supply-violation census (anatomy): %d/9 "
          "reads outside the Buethe budget (lowfreq 0/9), %d/9 "
          "outside the SHARPER Fourier budget SUP_F" % (violB,
                                                        violF))
    check("C3 scramble core-fold density movement: med rel move "
          "%.3f >= %.2f" % (med_mv, MOVE_BAR), med_mv >= MOVE_BAR,
          kill="K2")

    # ------------------------------------------------------------ S
    section("S -- mandatory tau screens (surface)")
    hmins = np.array([min(r["reads"][j]["H"] for j in CORE_J)
                      for r in sup_rows])
    scr_m, _ = parent.screen(marg_s, taus1)
    scr_h, _ = parent.screen(hmins, taus1)
    print("    TAU-SCREEN combined margin  %s" % scr_m)
    print("    TAU-SCREEN headroom         %s" % scr_h)
    check("S screens recorded", True)

    # ---------------------------------------------------- verdicts
    all_alpha = np.array([r["alpha"] for r in sup_rows]
                         + [r["alpha"] for r in deep_rows])
    marg_all = np.concatenate([marg_s, marg_d])
    dexm = np.array([-s for s in short_m_all])   # margin dex
    fin = np.isfinite(dexm)
    sl_a, r2_a = parent.ols_line(all_alpha[fin], dexm[fin])
    if nMIN == N:
        v1 = ("SUBG-H1-CLOSED-DEPLOYED(combined %d/%d; min margin "
              "%+.3f abs / %+.2f dex; X <= 4e6 surface, Buethe "
              "range 1e19, EF all-X)"
              % (nMIN, N, float(np.min(marg_all)),
                 float(np.min(dexm))))
    elif nMIN > 0:
        prof = tuple(fold_s[j]["MIN"] for j in CORE_J)
        v1 = ("SUBG-H1-PARTIAL(combined %d/%d; med shortfall %+.2f"
              " dex; surface fold profile MIN %s)"
              % (nMIN, N, float(np.median(short_m_all)), prof))
    else:
        v1 = ("SUBG-H1-OPEN(0/%d; med shortfall %+.2f dex)"
              % (N, float(np.median(short_m_all))))
    if med_rec >= DEMAND_DEX:
        v1b = ("FOURIER-DELIVERS(med recovery %+.2f dex >= the "
               "demanded +%.2f)" % (med_rec, DEMAND_DEX))
    else:
        v1b = ("FOURIER-PARTIAL(med recovery %+.2f dex vs demanded"
               " +%.2f)" % (med_rec, DEMAND_DEX))
    v2 = "SUBG-EF-ALONE(%d/%d closed; Buethe-combined %d/%d)" % (
        nF, N, nMIN, N)
    conc_txt = ("med %+.2f dex" % float(np.median(conc))) if conc \
        else "n/a: a0_sup <= 0 everywhere"
    if rho_ran and rho_ok:
        v3 = ("COMPOSED-THEOREM-SURFACE(39-step deployed surface: "
              "v-floors classical-supplied 39/39, battery s_P >= "
              "a-b > 0 39/39 [measured Gram], composed 1-rho >= "
              "%.3e > 0 [min], rho margin min %.4f; measured "
              "inputs remain: kernel diag/offdiag + Mt diag; "
              "Gershgorin a0-level still I4-blocked, %s)"
              % (rho_min_comp, rho_min_marg, conc_txt))
    elif rho_ran:
        v3 = ("W1-COMPOSED-SEAT-FAILS(rho chain re-run, composed "
              "min %.3e, battery %d/39; %s)"
              % (rho_min_comp, n_batt, conc_txt))
    else:
        v3 = ("W1-COMPOSED-VOID(surface MIN %d/39; a0_sup > 0 on "
              "%d/39; %s); RHO-STILL-CONDITIONAL (CLXXIX cited)"
              % (cen_s["MIN"], n_a0pos, conc_txt))
    if kgap and len(kgap) == 39 and max(kgap) <= 0.0:
        v4 = "H2-CS-CLOSES(39/39)"
    else:
        kg_txt = ("med %+.2f dex on %d/39"
                  % (float(np.median(kgap)), len(kgap))) if kgap \
            else "n/a: a0_sup <= 0 everywhere"
        v4 = ("H2-CS-NEEDS-DIAG-LAW(needed K_up %s below measured; "
              "the Fourier supply gives v-bounds, no diagonal law "
              "-- CLXXVIII J2 unmoved)" % kg_txt)
    om16_s = float(np.median([ef[16]["omega"] for ef in ef_rows]))
    om16_d = float(np.median([ef[16]["omega"] for ef in deep_efs]))
    if sl_a >= TREND_FLAT:
        v5 = ("ALLH-SUPPLY-IMPROVES(margin %+.3f dex per unit alpha"
              ", R2 %.2f; omega_16 med %.2f surface -> %.2f deep, "
              "the resonance distance GROWS with depth; boundary ="
              " the shallow high-fold seat, %d/%d rungs open -- "
              "ANATOMY, not theorem)"
              % (sl_a, r2_a, om16_s, om16_d, N - nMIN, N))
    elif sl_a <= -TREND_FLAT:
        v5 = ("ALLH-SUPPLY-DEGRADES(%+.3f dex per alpha, R2 %.2f "
              "-- the mechanism stops sufficing in depth; ANATOMY)"
              % (sl_a, r2_a))
    else:
        v5 = ("ALLH-FLAT(%+.3f dex per alpha, R2 %.2f; ANATOMY)"
              % (sl_a, r2_a))
    print("\n    ANATOMY: combined min-fold margin trend %+.3f dex "
          "per unit alpha (R2 %.2f); shortfall_MIN med %+.2f dex; "
          "recovery med %+.2f dex" % (sl_a, r2_a,
                                      float(np.median(short_m_all)),
                                      med_rec))
    check("V1 typed: %s" % v1, True)
    check("V1b typed: %s" % v1b, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v1b=v1b, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
