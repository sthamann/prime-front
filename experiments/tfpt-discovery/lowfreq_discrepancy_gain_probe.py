#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lowfreq_discrepancy_gain_probe -- PRIME.PORT.LOWFREQ.GAIN.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE BOTTLENECK ATTACK.  h1h2_envelope_
derivation_probe (CLXXVIII, SPEC-SHA 08e49f41..) localized the ONLY
open all-h seat of the W1 skeleton chain at the LOW-FREQUENCY comb
reads of the first folds: the core-fold atom densities are exact
windowed prime sums (the v882 identity, transcribed below as an
exact per-atom response kernel), the frozen global L-inf
perturbation bound Delta_env med 802 sits ~2.5 orders above the
local |d^ar| scale 0.71, and the named fix is a LOCALIZED bound of
the comb density at the first folds -- short-interval / low-
frequency prime discrepancy, NOT an envelope.  THE QUESTION
(frozen): do explicit unconditional psi-error bounds from the
classical literature -- deployed by exact partial summation against
the ACTUAL lag weights -- deliver that localized bound, i.e. the
~1.8 dex of discrepancy gain the whole program now funnels into?

THE EXACT OBJECTS.  Per rung (kz, h, M, D = 2 alpha / M,
L = 2M - 2, X = e^{2 alpha}): the atom grid density at fold j is
    d_at(theta_j) = Sum_{n <= X} mu_n phi_j(log n),
    mu_n = 2 Lambda(n) / sqrt(n),
where phi_j is the EXACT response of the T115 tent assembly + FFT
symmetrization to a unit atom: the piecewise-linear interpolant of
the node values phi_j(0) = -F_j[0], phi_j(kD) = -F_j[k]/2
(1 <= k <= M-1), phi_j(MD) = 0, with F_j[k] = cf_k cos(2 pi k j/L),
cf_k = 1 at k = 0 and k = M-1, else 2 (grid_density symmetric-FFT
weights; reflection at k = 0 included -- q_read class, transcription
warded per rung to the pipeline read).  The alias frequency of the
fold-j read is omega_j = theta_j / D ~ pi j / (2 alpha): O(1)..O(10)
in u -- LOW (printed per rung).  Writing psi(t) = t + E(t) and
g(t) = 2 t^{-1/2} phi_j(log t), exact Stieltjes partial summation on
[2^-, X] gives (phi_j(2 alpha) = 0 kills the upper boundary):
    d_at(theta_j) = MAIN_j + R_j,
    MAIN_j = 2 Int_{ln 2}^{2 alpha} e^{u/2} phi_j(u) du
             (deterministic, comb-free: ARCH-class pedigree),
    |R_j| <= 2 sqrt(2) |phi_j(ln 2)|
             + 2 Int_{ln 2}^{2 alpha} env(u) |phi_j'(u)
               - phi_j(u)/2| du,
where env(u) is any upper envelope of |E(e^u)| e^{-u/2}.  All
segment integrals are per-segment closed forms (phi_j piecewise
linear); the envelope factor is taken at its per-segment supremum
(each branch monotone), so every supplied number is a rigorous
upper bound of the float-computed ideal objects.

THE CLASSICAL INPUT CLASSES (cited, unconditional, explicit
constants; pedigree block -- zeta ZEROS themselves remain BANNED
from every construction; these are literature CONSTANTS of the
Chebyshev/Buethe class already used by v563/v594):
  (B) BUETHE finite-range sqrt envelope: |psi(x) - x| < 0.94
      sqrt(x) for 11 < x <= 1e19 (Buethe 2018, Math. Comp. 87;
      deployed in verification/v594_unconditional_cert.py lines
      10-13, 47).  Every deployed window has X <= 4e6 -- DEEP
      inside the verified range.  env(u) = 0.94 on u > ln 11.
  (Z) THE EXPLICIT ZFR CLASS: |psi(x) - x| <= ZFR_A x
      (ln x / ZFR_B)^{ZFR_C} exp(-sqrt(ln x / ZFR_B)) for x >= 149
      with ZFR_A = 0.2795, ZFR_B = 6.455, ZFR_C = 0.4912
      (Trudgian 2016, Ramanujan J. 39, 225-234, "Updating the
      error term in the prime number theorem", Thm 1 -- the
      standard explicit zero-free-region form; sharper successors
      (Platt-Trudgian 2021, Fiori-Kadiri-Swidinsky 2023+) exist,
      but the CLASS scaling x exp(-c sqrt(log x)) is what is
      probed).  env(u) = eps_T(u) e^{u/2}.
  (K) the Chebyshev envelope baseline: KAPPA_REF = 0.038821
      (v563:134, jump-point right values); deployed here as the
      TWO-SIDED table supremum KAPPA_EFF = sup_{100 <= t <= 4e6}
      |psi(t) - t| / t (both jump sides, measured on the extended
      table and printed -- the honest |E(t)| <= kappa t form the
      sup-norm bound needs).  env(u) = KAPPA_EFF e^{u/2}.
  Below each validity threshold (t in [2, 11] / [2, 149] /
  [2, 100]) the EXACT small-range supremum of |psi(t) - t| is
  computed from the table (both interval endpoints) and used as a
  constant envelope -- exact, declared.

(a) THE DEMAND (CLXXVIII verbatim, reproduced as a ward): per rung
the perturbation ladder Delta_meas = max_j |d_at_j| /
Delta_lag = 2 Sum |c_at| / Delta_env = 2 M_up (M_up = 2 B_PSI
(2 sqrt(X) - 1)), the arch floor tgt = min_{CORE_J} (-d^ar_j), and
the demanded gain log10(Delta_env / tgt) in dex (med bars 381 /
382 / 802, rtol 5e-2).

(b) THE SUPPLY: per rung, per read j in {0} + CORE_J, per class C
in {B, Z, K}: SUP_C_j as above; the TRUE remainder R_j = d_at_j -
MAIN_j (soundness ward |R_j| <= SUP_C_j per class -- a theorem
about the computed objects, kill on failure); the headroom
H_j = -(d^ar_j + MAIN_j); per-fold closure SUP_C_j < H_j.  The DC
read (j = 0) is the CLXXVIII Delta seat: gain log10(Delta_env /
SUP_B_0) is the direct dex-gain read.

(c) THE VERDICT TABLE (frozen rules, decided by the data alone):
  n_C = rungs (39 surface + deep block) with ALL 8 core folds
  closed under class C; n_true = same census under the measured
  |R_j| (the ceiling of every |E|-envelope route).
  V1 headline: H1-CORE-FLOOR-CLOSED-DEPLOYED(buethe, min margin
    dex; valid X <= 1e19) iff n_B == N; H1-CORE-FLOOR-
    PARTIAL(n_B/N, fold profile) iff 0 < n_B < N; else H1-CORE-
    FLOOR-OPEN(med shortfall dex).
  V1b envelope-vs-identity seat: ENVELOPE-LOSES(med dex) iff
    n_true > n_B (the |E|-sup route wastes the signed
    cancellation); SEAT-DEEPER(folds) iff n_true < N (the
    localized decomposition itself fails somewhere).
  V2 kappa baseline census (CLXXVIII reproduction: expected 0).
  V3 ZFR: census n_Z; if n_Z < N and the fitted shortfall
    log10(SUP_Z/H) vs log10 X has slope > +0.05: ZFR-
    DIVERGES(slope; the class loses to the sqrt(x) demand and
    NEVER closes at any X); envelope-level crossover X* with
    eps_T(X*) = KAPPA_EFF printed (where the ZFR class starts
    beating the linear kappa envelope at all).
  V4 composition (CLXXVII F3 Gershgorin chain with supplied
    constants): v_sup_i = w_i (H_i - SUP_B_i), a0_sup = min_i
    v_sup_i / m0_up (m0_up = m0_ar_abs + Delta_env, CLXXVIII
    verbatim; trivial I1 floor K >= 1/m0): W1-COMPOSED-SEMI iff
    n_B == N and a0_sup > b_meas on every step (still measured-b
    conditional); W1-COMPOSED-BLOCKED(concentration dex = med
    log10(a_meas/a0_sup), H2 named) iff n_B == N otherwise;
    W1-COMPOSED-VOID else.  The CLXXIX rho chain consumes the
    measured battery (a - b): typed RHO-STILL-CONDITIONAL on the
    same two inputs -- no recomputation (cited).
  V5 H2: the same partial-summation supply gives v_i upper bounds
    but NO upper Christoffel law: the CS route needs K_up <
    a0_sup / (max_i sqrt(v_up_i) Sum_{j!=i} sqrt(v_up_j)); typed
    H2-CS-NEEDS-DIAG-LAW with the needed K_up vs the measured
    max_i K_h(y_i,y_i) in dex (the CLXXVIII J2 verdict is NOT
    moved by this supply -- frozen statement).

(d) GATES.  TAU-SCREENS (parent bands PASS |s| <= 0.30 / RELOC >=
0.70): the Buethe margin family min_j (H_j - SUP_B_j) and the
headroom family min_j H_j, surface steps vs tau.  SMOOTH WORLD
(documented, inputs differ BY CONSTRUCTION): the smooth masses are
the Riemann sum of MAIN's integrand, so its remainder R_sm is pure
quadrature error with NO psi content -- the census med |R_sm| vs
med |R_true| is printed and typed; the composed-chain world break
stays at the CLXXVIII battery seat (C1).  CONTROLS (kill if
silent): C1 smooth world refuses the certificate ladder, C2
Epstein + scramble fire (parent verbatim); C3 scramble core-fold
density movement med rel move >= MOVE_BAR where the scramble core
exists (h1h2 verbatim; disclosed skip if dead), with the scramble
supply-violation census printed as anatomy.  ANTI-CIRCULARITY
(frozen): no zeta zeros, no wall data, no target eigendata in any
derived bound; MAIN is comb-free deterministic (ARCH pedigree);
the comb enters derived constants only through the cited
envelopes; measured d/R values appear only as truth columns and
soundness wards.  Extrapolations (Buethe carrying range in X, ZFR
shortfall law) are ANATOMY, not theorems -- typed as such.

DEAD overrides (kill anyway): parent reproduction fails, the
identity (v882 transcription) ward fails, any soundness ward
fails, deep census < MIN_DEEP.

FROZEN BARS: IDENT_TOL = 1e-9 (x (1 + l1_at) abs); SOUND_TOL =
1e-6 (rel) + 1e-9 (x (1 + l1_at) abs); REPRO Delta meds (381,
382, 802) rtol 5e-2; REPRO_A_MED = 0.968, REPRO_B_MED = 0.202,
rtol 5e-2 (h1h2 verbatim); HTREND_FLAT = 0.30; ZFR_DIV_SLOPE =
0.05; MOVE_BAR = 0.05; MIN_DEEP = 10; BUETHE = 0.94 on (11, 1e19]
(v594); ZFR_A/B/C = 0.2795 / 6.455 / 0.4912, x >= 149 (Trudgian
2016); parent bars (MINB_REF 0.679, GAP 0.052/0.888, rtol as
parent) inherited verbatim; parent SPEC-SHA warded == 084c9689..;
h1h2 SPEC-SHA prefix warded == 08e49f41.  Runtime cap declared:
20 min.  Smoke mode LOWFREQ_SMOKE=1 restricts the deep block to
the 4 shallowest new rungs (surface + controls always full); any
smoke run is disclosed here before the freeze.

ANTHROPIC NO-GO DECLARATION: the supplied bounds read one-
dimensional psi-error envelopes against window geometry (two-
moment-class global data); the measured target is the fine
conditioning of an 8x8 CD-kernel Gram.  A partial or blocked
verdict quantifies the no-go boundary; a closed core floor does
NOT touch W2 / background cancellation, which remain RH-hard.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(LOWFREQ_SMOKE=1, 37/37 on the FIRST passage, 4.8 s, exit 0; deep
block on the 4 shallowest new rungs).  NO bar, band, count, rule
or enum was moved after it; post-smoke changes are this disclosure
block and ONE disclosed amendment A1 (print-only: the V5 label
printed 'med +nan dex' when the kgap census is empty because
a0_sup <= 0 everywhere -- the empty case now prints 'n/a: a0_sup
<= 0 everywhere'; no bar, branch condition, census or number
moved).  HONESTY NOTE: the smoke stdout was piped through a
tail(120) and the head (S0/W/E/A1-A4 ward lines) was not
archived; all 37 checks passed (0 failed), and the pipeline is
deterministic -- the frozen run must reproduce the surface numbers
below identically and its full log is archived.  Measured smoke
context the frozen run must confirm (from the retained tail):
per-fold anatomy on 39 surface rungs -- med H / med SUP_B / med
|R_true| / closures B: j=2 +133.251/14.44/0.364/39, j=4
+44.806/20.43/0.341/30, j=6 +21.230/26.20/0.266/16, j=8
+12.305/33.66/0.216/6, j=10..16 0 closures (SUP_B 42.2..67.3 vs H
8.14..3.65), TRUE-ceiling 39/39 at every fold; rungs fully closed
B 0/39, K 0/39, Z 0/39, TRUE 39/39; DC seat gain vs Delta_env
+1.23/+1.77/+2.22 dex (the demanded ~1.8 dex is REAL and
delivered at the DC read); composition a0_sup positive 0/39
(Gershgorin margin -0.488/-0.202/-0.064) -> W1-COMPOSED-VOID;
smooth world med |R_sm| 0.349 vs med |R_true| 0.345 (ratio 1.013
-- the comb's true low-frequency deviation sits WITHIN the tent-
quadrature noise floor: the measured R_true at the core folds is
discretization-dominated, not psi-fluctuation); deep smoke 4/4:
minH +43.5..+106.6 vs maxSUP_B ~65 -> B closes 2/4 in depth,
TRUE 4/4; margin trend +0.579 dex per unit alpha (R2 0.99 -- the
Buethe route closes INCREASINGLY well with depth, the failing
seat is the SHALLOW surface at high folds); ZFR shortfall flat
slope -0.364 (R2 0.93), med +1.73 dex, crossover eps_T = KAPPA_EFF
at X* = 1.06e13; controls C1 refused 42/0, C2 negA 55/37, C3 med
rel move 6.506 fires, scramble supply-violation 0/9 (anatomy: at
the tiny kz-9 control window the Buethe budget is not
discriminating); screens margin VACUOUS(n=0), headroom
PASS(-0.276, R2 0.269).  Smoke verdicts pinned by the frozen
rules: V1 H1-CORE-FLOOR-PARTIAL(buethe 2/43, med shortfall +1.20
dex), V1b ENVELOPE-LOSES(TRUE 43/43 vs buethe 2; med envelope
waste +2.05 dex), V2 KAPPA-BASELINE(0/43, CLXXVIII reproduced),
V3 ZFR-SHORTFALL-FLAT(0/43, slope -0.36, med +1.73 dex), V4
W1-COMPOSED-VOID, V5 H2-CS-NEEDS-DIAG-LAW.  The frozen run
repeats everything on the FULL deep block (28 expected rungs);
enums move only as the full data says.

NO RH claim.  Even a fully closed core floor would certify only
the v_i-positivity half of H1 inside the finite Buethe range; the
Christoffel concentration (I4, ~6 orders), H2, and W2 /
background cancellation remain open and RH-hard.  A blocked
verdict is itself the finding: it prices the bottleneck in the
honest currency (dex vs X) of the classical unconditional
literature.  No marker moves.  Stdout only.
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
import h1h2_envelope_derivation_probe as h1h2  # noqa: E402 (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
H1H2_SHA8 = "08e49f41"
IDENT_TOL = 1.0e-9
SOUND_TOL = 1.0e-6
REPRO_D = (381.0, 382.0, 802.0)
REPRO_D_RTOL = 5.0e-2
REPRO_A_MED = 0.968
REPRO_B_MED = 0.202
REPRO_RTOL = 5.0e-2
HTREND_FLAT = 0.30
ZFR_DIV_SLOPE = 0.05
MOVE_BAR = 0.05
MIN_DEEP = 10
C_LO = 2.0
BUETHE = 0.94
BUETHE_XMIN = 11.0
BUETHE_XMAX = 1.0e19
ZFR_A = 0.2795
ZFR_B = 6.455
ZFR_C = 0.4912
ZFR_XMIN = 149.0
KAPPA_X0 = 100.0
LN2 = math.log(2.0)
CORE_J = base.CORE_J
READS = (0,) + tuple(CORE_J)
SMOKE = os.environ.get("LOWFREQ_SMOKE", "") == "1"
BANNED_IDS = parent.BANNED_IDS

CHECKS = []
KILLS = []
T0 = time.time()

ENV = {}   # envelope constants, filled in section E


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


def battery_split(Gc):
    a = float(np.min(np.diag(Gc)))
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    b = float(np.max(off))
    return a, b


def eps_T(u):
    """The Trudgian 2016 ZFR envelope factor eps(x) with u = ln x."""
    u = np.asarray(u, float)
    return ZFR_A * (u / ZFR_B) ** ZFR_C * np.exp(-np.sqrt(u / ZFR_B))


def phi_nodes(M, L, j):
    """phi_j at the grid nodes k D, k = 0..M (exact, see spec)."""
    k = np.arange(M)
    cf = np.full(M, 2.0)
    cf[0] = 1.0
    cf[M - 1] = 1.0
    F = cf * np.cos(2.0 * math.pi * k * j / L)
    p = np.empty(M + 1)
    p[:M] = -0.5 * F
    p[0] = -F[0]
    p[M] = 0.0
    return p


def env_sup(cls, lo, hi):
    """Per-segment supremum of the class envelope of |E(e^u)| e^{-u/2}
    on [lo, hi] (arrays).  Each branch is monotone: the below-threshold
    constant/sqrt branch decreases (sup at lo), the above-threshold
    branch increases or is constant (sup at hi)."""
    if cls == "B":
        th, esm = math.log(BUETHE_XMIN), ENV["E11"]
        above_hi = np.full_like(hi, BUETHE)
    elif cls == "K":
        th, esm = math.log(KAPPA_X0), ENV["E100"]
        above_hi = ENV["KAPPA_EFF"] * np.exp(0.5 * hi)
    else:
        th, esm = math.log(ZFR_XMIN), ENV["E149"]
        above_hi = eps_T(np.maximum(hi, th)) * np.exp(0.5 * hi)
    below = np.where(lo < th, esm * np.exp(-0.5 * lo), 0.0)
    above = np.where(hi > th, above_hi, 0.0)
    return np.maximum(below, above)


def rung_supply(alpha, M, uu, mm, c_ar):
    """The full demand + supply data of one rung."""
    D = 2.0 * alpha / M
    L = 2 * M - 2
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    d_at = base.grid_density(c_at)
    d_ar = base.grid_density(c_ar)
    l1_at = float(np.sum(np.abs(c_at)))
    X = math.exp(2.0 * alpha)
    m_up = 2.0 * core.B_PSI * (2.0 * math.sqrt(X) - 1.0)
    delta_meas = float(np.max(np.abs(d_at)))
    delta_lag = 2.0 * l1_at
    delta_env = 2.0 * m_up
    jj = np.arange(L)
    w_all = 4.0 * np.sin(math.pi * jj / L) ** 2
    m0_ar_abs = float(np.sum(w_all * np.abs(d_ar))) / (2.0 * L)
    nodes = D * np.arange(M + 1)
    # segments clipped to [ln 2, 2 alpha]
    k = np.arange(M)
    u0 = k * D
    u1 = (k + 1) * D
    keep = u1 > LN2
    u0 = u0[keep]
    u1 = u1[keep]
    lo = np.maximum(u0, LN2)
    out = dict(D=D, L=L, X=X, l1_at=l1_at, delta_meas=delta_meas,
               delta_lag=delta_lag, delta_env=delta_env,
               m0_ar_abs=m0_ar_abs, reads={})
    elo2 = np.exp(0.5 * lo)
    ehi2 = np.exp(0.5 * u1)
    envs = {c: env_sup(c, lo, u1) for c in ("B", "K", "Z")}
    for j in READS:
        p = phi_nodes(M, L, j)
        pk = p[:M][keep]
        b = ((p[1:] - p[:M]) / D)[keep]
        phi_lo = pk + b * (lo - u0)
        phi_hi = pk + b * (u1 - u0)
        # MAIN = 2 Int e^{u/2} phi du (per-segment closed form)
        seg = 2.0 * (ehi2 * (phi_hi - 2.0 * b)
                     - elo2 * (phi_lo - 2.0 * b))
        main = 2.0 * float(np.sum(seg))
        # Int |phi' - phi/2| per segment (exact, linear integrand)
        w_lo = b - 0.5 * phi_lo
        w_hi = b - 0.5 * phi_hi
        width = u1 - lo
        same = w_lo * w_hi >= 0.0
        dw = np.abs(w_lo - w_hi)
        iW = np.where(
            same, 0.5 * np.abs(w_lo + w_hi) * width,
            np.where(dw > 0.0,
                     0.5 * (w_lo ** 2 + w_hi ** 2) * width
                     / np.maximum(dw, 1e-300), 0.0))
        phi_ln2 = float(np.interp(LN2, nodes, p))
        bnd = 2.0 * math.sqrt(2.0) * abs(phi_ln2)
        sup = {c: bnd + 2.0 * float(np.sum(envs[c] * iW))
               for c in ("B", "K", "Z")}
        ident = float(np.dot(mm, np.interp(uu, nodes, p)))
        r_true = float(d_at[j]) - main
        out["reads"][j] = dict(
            omega=2.0 * math.pi * j / (L * D), main=main,
            sup=sup, d_at=float(d_at[j]), d_ar=float(d_ar[j]),
            r_true=r_true, ident_dev=abs(ident - float(d_at[j])),
            w_geo=4.0 * math.sin(math.pi * j / L) ** 2 / L)
    return out


def table_sups(NN, psi, tmax):
    """Two-sided |E| suprema from a table of jumps (NN, psi = cumsum)."""
    NNf = NN.astype(float)
    nxt = np.append(NNf[1:], float(tmax))
    dev_r = np.abs(psi - NNf)          # right value at the jump
    dev_l = np.abs(psi - nxt)          # approach to the next jump
    res = {}
    m = NNf >= KAPPA_X0
    m2 = nxt >= KAPPA_X0
    res["KAPPA_EFF"] = max(float(np.max(dev_r[m] / NNf[m])),
                           float(np.max(dev_l[m2] / nxt[m2])))
    seat = int(np.argmax(np.where(m, dev_r / np.where(m, NNf, 1.0),
                                  0.0)))
    res["KAPPA_SEAT"] = int(NN[seat])
    mb = NNf > BUETHE_XMIN
    mb2 = nxt > BUETHE_XMIN
    res["BUETHE_SUP"] = max(
        float(np.max(dev_r[mb] / np.sqrt(NNf[mb]))),
        float(np.max(dev_l[mb2] / np.sqrt(nxt[mb2]))))
    mz = NNf >= ZFR_XMIN
    mz2 = nxt >= ZFR_XMIN
    res["ZFR_SUP"] = max(
        float(np.max(dev_r[mz] / (eps_T(np.log(NNf[mz])) * NNf[mz]))),
        float(np.max(dev_l[mz2] / (eps_T(np.log(nxt[mz2]))
                                   * nxt[mz2]))))
    for tag, T in (("E11", BUETHE_XMIN), ("E100", KAPPA_X0),
                   ("E149", ZFR_XMIN)):
        ms = NNf <= T
        res[tag] = max(float(np.max(dev_r[ms])),
                       float(np.max(np.abs(psi[ms]
                                           - np.minimum(nxt[ms], T)))))
    return res


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("LOWFREQ-MEASURED / %s / %s / %s / %s / %s / %s"
                   % (labels.get("v1", "-"), labels.get("v1b", "-"),
                      labels.get("v2", "-"), labels.get("v3", "-"),
                      labels.get("v4", "-"), labels.get("v5", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every supplied number is a rigorous upper bound of
  the float64-computed ideal objects, consuming only the cited
  unconditional literature envelopes (Buethe sqrt-range, Trudgian
  ZFR class, two-sided Chebyshev table sup), the window geometry
  and the comb-free MAIN integral.  Extrapolations are anatomy, not
  theorems.  A closed core floor would certify only the v_i-
  positivity half of H1 inside the finite range; concentration, H2
  and W2 / background remain open.  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.LOWFREQ.GAIN.01 -- explicit ZFR/sqrt psi-"
            "bounds vs the low-frequency discrepancy demand "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    h1h2_sha = hashlib.sha256(h1h2.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    h1h2   SPEC SHA-256 = %s" % h1h2_sha)
    print("    NO RH claim.  Cited inputs: Buethe 2018 (0.94 sqrt x,"
          " 11 < x <= 1e19; v594:10-13,47), Trudgian 2016 ZFR "
          "(0.2795, 6.455, 0.4912; x >= 149), Chebyshev table sup.")
    if SMOKE:
        print("    *** SMOKE MODE: deep on 4 shallowest new rungs ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c h1h2 SPEC prefix reproduced",
          h1h2_sha[:8] == H1H2_SHA8, h1h2_sha[:8], kill="K2")

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
    ab = [battery_split(w["Gc"]) for w in rows]
    a_all = np.array([x[0] for x in ab])
    b_all = np.array([x[1] for x in ab])
    a_med = float(np.median(a_all))
    b_med = float(np.median(b_all))
    check("W3 CLXXVII H1/H2 reproduction (a med %.4f == %.3f, "
          "b med %.4f == %.3f)" % (a_med, REPRO_A_MED, b_med,
                                   REPRO_B_MED),
          abs(a_med / REPRO_A_MED - 1.0) <= REPRO_RTOL
          and abs(b_med / REPRO_B_MED - 1.0) <= REPRO_RTOL,
          kill="K2")
    hs = np.array([float(w["r2"]["h"]) for w in rows])
    taus1 = np.array([w["tau"] for w in rows])

    # ------------------------------------------------------------ E
    section("E -- the classical inputs (verified on the extended "
            "table, cited pedigree)")
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
    kap = core.chebyshev_kappa()
    check("E1 Chebyshev right-value kappa = %.6f == KAPPA_REF %.6f "
          "(v563:134)" % (kap, core.KAPPA_REF),
          kap <= core.KAPPA_REF + core.TOL_KAPPA, kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    ENV.update(table_sups(NN_e, psi_e, deep.TAB_EXT))
    print("    KAPPA_EFF (two-sided sup |E|/t on [100, 4e6]) = %.6f"
          " (seat t = %d; right-value ref %.6f)"
          % (ENV["KAPPA_EFF"], ENV["KAPPA_SEAT"], core.KAPPA_REF))
    check("E1b two-sided KAPPA_EFF deployed (%.6f, sane band)"
          % ENV["KAPPA_EFF"],
          core.KAPPA_REF <= ENV["KAPPA_EFF"] <= 0.25, kill="K2")
    ratio_max = float(np.max(psi_e / NN_e.astype(float)))
    check("E2 global Chebyshev bound max psi/x = %.5f <= B_PSI %.5f"
          % (ratio_max, core.B_PSI), ratio_max <= core.B_PSI,
          kill="K2")
    check("E3 Buethe envelope warded on the table: two-sided sup "
          "|E|/sqrt(t) = %.4f <= %.2f on (11, 4e6] (cited range "
          "(11, 1e19], Buethe 2018 / v594)"
          % (ENV["BUETHE_SUP"], BUETHE),
          ENV["BUETHE_SUP"] <= BUETHE, kill="K2")
    check("E4 ZFR envelope warded on the table: sup |E|/(eps_T t) "
          "= %.2e <= 1 on [149, 4e6] (Trudgian 2016)"
          % ENV["ZFR_SUP"], ENV["ZFR_SUP"] <= 1.0, kill="K2")
    lo_u, hi_u = 10.0, 2000.0
    for _ in range(200):
        mid = 0.5 * (lo_u + hi_u)
        if float(eps_T(mid)) > ENV["KAPPA_EFF"]:
            lo_u = mid
        else:
            hi_u = mid
    xstar = math.exp(0.5 * (lo_u + hi_u))
    print("    small-range exact sups |E| on [2,11]/[2,100]/[2,149]"
          " = %.3f / %.3f / %.3f"
          % (ENV["E11"], ENV["E100"], ENV["E149"]))
    print("    envelope-level crossover eps_T(X*) = KAPPA_EFF at "
          "X* = %.2e (the ZFR class beats the linear kappa "
          "envelope only beyond this)" % xstar)
    check("E5 small-range sups + crossover recorded", True)

    # ------------------------------------------------------------ A
    section("A -- demand + supply on the 39 surface steps")
    print("    per rung: demand ladder (CLXXVIII) | headroom "
          "H_j = -(d^ar+MAIN)_j | supply per class")
    sup_rows = []
    ident_worst = 0.0
    sound_ok = True
    sound_worst = ""
    for w in rows:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rs = rung_supply(rr["alpha"], rr["M"], rr["uu"],
                         2.0 * rr["lam"], rr["c_ar"])
        rs["kz"] = r2["kz"]
        rs["h"] = float(r2["h"])
        rs["alpha"] = float(rr["alpha"])
        sup_rows.append(rs)
        w["rs"] = rs
        for j in READS:
            rd = rs["reads"][j]
            ident_worst = max(ident_worst, rd["ident_dev"]
                              / (1.0 + rs["l1_at"]))
            for c in ("B", "K", "Z"):
                tol = SOUND_TOL * rd["sup"][c] \
                    + 1e-9 * (1.0 + rs["l1_at"])
                if abs(rd["r_true"]) > rd["sup"][c] + tol:
                    sound_ok = False
                    sound_worst = ("kz %d j %d cls %s |R| %.3g > "
                                   "SUP %.3g" % (rs["kz"], j, c,
                                                 abs(rd["r_true"]),
                                                 rd["sup"][c]))
    check("A1 v882-identity transcription ward: d_at(theta_j) == "
          "Sum mu_n phi_j(u_n)", ident_worst <= IDENT_TOL,
          "worst scaled dev %.2e" % ident_worst, kill="K2")
    check("A2 soundness: |R_true| <= SUP_class on every rung x "
          "read x class", sound_ok, sound_worst or "all inside",
          kill="K2")
    dm = np.array([r["delta_meas"] for r in sup_rows])
    dl = np.array([r["delta_lag"] for r in sup_rows])
    de = np.array([r["delta_env"] for r in sup_rows])
    meds = (float(np.median(dm)), float(np.median(dl)),
            float(np.median(de)))
    check("A3 CLXXVIII demand ladder reproduced: Delta meds "
          "%.1f/%.1f/%.1f == %.0f/%.0f/%.0f"
          % (meds + REPRO_D),
          all(abs(m / r - 1.0) <= REPRO_D_RTOL
              for m, r in zip(meds, REPRO_D)), kill="K2")
    om2 = np.array([r["reads"][2]["omega"] for r in sup_rows])
    om16 = np.array([r["reads"][16]["omega"] for r in sup_rows])
    print("    alias frequencies on the ladder: omega_2 "
          "%.3f/%.3f/%.3f, omega_16 %.2f/%.2f/%.2f (LOW, O(1)..O(10))"
          % (band(om2) + band(om16)))
    check("A4 fold alias frequencies recorded", True)

    # per-rung table + censuses
    def rung_census(rlist):
        cen = dict(B=0, K=0, Z=0, T=0)
        fold = {j: dict(B=0, K=0, Z=0, T=0, H=[], SB=[], RT=[])
                for j in CORE_J}
        marg = []
        short = []
        hpos = 0
        for r in rlist:
            okc = dict(B=True, K=True, Z=True, T=True)
            mm_r = []
            for j in CORE_J:
                rd = r["reads"][j]
                H = -(rd["d_ar"] + rd["main"])
                rd["H"] = H
                fold[j]["H"].append(H)
                fold[j]["SB"].append(rd["sup"]["B"])
                fold[j]["RT"].append(abs(rd["r_true"]))
                for c in ("B", "K", "Z"):
                    hit = rd["sup"][c] < H
                    fold[j][c] += int(hit)
                    okc[c] &= hit
                hit_t = abs(rd["r_true"]) < H
                fold[j]["T"] += int(hit_t)
                okc["T"] &= hit_t
                if H > 0:
                    mm_r.append(math.log10(H / rd["sup"]["B"]))
                else:
                    mm_r.append(float("-inf"))
            for c in ("B", "K", "Z", "T"):
                cen[c] += int(okc[c])
            hpos += int(all(r["reads"][j]["H"] > 0 for j in CORE_J))
            marg.append(min(mm_r))
            sb = max(r["reads"][j]["sup"]["B"]
                     / max(r["reads"][j]["H"], 1e-300)
                     for j in CORE_J)
            short.append(math.log10(sb))
        return cen, fold, np.array(marg), np.array(short), hpos

    cen_s, fold_s, marg_s, short_s, hpos_s = rung_census(sup_rows)
    print("    rung  kz    h      X       Dmeas   Denv   minH    "
          "maxSUP_B  maxSUP_K  maxSUP_Z  max|R|")
    for i, r in enumerate(sup_rows):
        Hs = [r["reads"][j]["H"] for j in CORE_J]
        print("    %4d %4d %4d  %.2e %7.1f %7.1f %+8.3f %9.2f "
              "%9.1f %9.2f %7.2f"
              % (i, r["kz"], int(r["h"]), r["X"], r["delta_meas"],
                 r["delta_env"], min(Hs),
                 max(r["reads"][j]["sup"]["B"] for j in CORE_J),
                 max(r["reads"][j]["sup"]["K"] for j in CORE_J),
                 max(r["reads"][j]["sup"]["Z"] for j in CORE_J),
                 max(abs(r["reads"][j]["r_true"]) for j in CORE_J)))
    print("    per-fold anatomy (39 rungs): j | med H | med SUP_B |"
          " med |R_true| | closures B/K/Z/TRUE")
    for j in CORE_J:
        f = fold_s[j]
        print("      j=%2d | %+8.3f | %8.2f | %7.3f | %d/%d/%d/%d"
              % (j, float(np.median(f["H"])),
                 float(np.median(f["SB"])),
                 float(np.median(f["RT"])), f["B"], f["K"],
                 f["Z"], f["T"]))
    print("    rungs fully closed (all 8 folds): B %d/39, K %d/39, "
          "Z %d/39, TRUE-ceiling %d/39; all-H-positive rungs %d/39"
          % (cen_s["B"], cen_s["K"], cen_s["Z"], cen_s["T"],
             hpos_s))
    check("A5 supply/headroom censuses recorded", True)
    dc_gain = np.array([math.log10(r["delta_env"]
                                   / r["reads"][0]["sup"]["B"])
                        for r in sup_rows])
    dc_gm = np.array([math.log10(r["delta_meas"]
                                 / r["reads"][0]["sup"]["B"])
                      for r in sup_rows])
    print("    DC seat (j = 0): gain log10(Delta_env / SUP_B_0) "
          "band %+.2f/%+.2f/%+.2f dex; vs Delta_meas "
          "%+.2f/%+.2f/%+.2f dex" % (band(dc_gain) + band(dc_gm)))
    check("A6 DC anatomy recorded (the demanded ~1.8 dex seat)",
          True)

    # ------------------------------------------------------------ J
    section("J -- composition with the supplied constants")
    a0_sup, gersh, conc, kgap = [], [], [], []
    for i, (w, r) in enumerate(zip(rows, sup_rows)):
        m0_up = r["m0_ar_abs"] + r["delta_env"]
        vsup = [r["reads"][j]["w_geo"]
                * (r["reads"][j]["H"] - r["reads"][j]["sup"]["B"])
                for j in CORE_J]
        vup = [r["reads"][j]["w_geo"]
               * max(r["reads"][j]["H"] + r["reads"][j]["sup"]["B"],
                     0.0) for j in CORE_J]
        a0 = min(vsup) / m0_up
        a0_sup.append(a0)
        gersh.append(a0 - b_all[i])
        if a0 > 0:
            conc.append(math.log10(a_all[i] / a0))
        sv = np.sqrt(np.maximum(vup, 0.0))
        den = float(np.max(sv * (np.sum(sv) - sv)))
        kmeas = float(np.max(np.diag(w["Gc"])
                             / w["r2"]["v_core"]))
        if a0 > 0 and den > 0:
            kneed = a0 / den
            kgap.append(math.log10(kmeas / kneed))
    a0s = np.array(a0_sup)
    n_a0pos = int(np.sum(a0s > 0.0))
    print("    a0_sup = min_i v_sup_i / m0_up: positive on %d/39; "
          "band %.3g / %.3g / %.3g" % ((n_a0pos,) + band(a0s)))
    print("    Gershgorin margin a0_sup - b_meas: band "
          "%+.3g / %+.3g / %+.3g" % band(np.array(gersh)))
    if conc:
        print("    concentration gap log10(a_meas / a0_sup): med "
              "%+.2f dex (the I4 seat)"
              % float(np.median(conc)))
    if kgap:
        print("    H2 CS route: needed K_up sits med %+.2f dex "
              "BELOW the measured max K_h(y,y)"
              % float(np.median(kgap)))
    check("J1 composed Gershgorin ladder recorded", True)
    check("J2 H2 needed-diagonal-law gap recorded", True)

    # ------------------------------------------------------------ M
    section("M -- smooth world (documented: inputs differ by "
            "construction)")
    r_sm_all, r_tr_all = [], []
    for w, r in zip(rows, sup_rows):
        rr = base.window_of(w["r2"]["kz"])
        mm_sm = base.smooth_masses(rr["uu"])
        c_sm = np.asarray(core.atom_lags_at(
            rr["alpha"], rr["M"], rr["uu"], mm_sm)[0], float)
        d_sm = base.grid_density(c_sm)
        for j in CORE_J:
            r_sm_all.append(abs(float(d_sm[j])
                                - r["reads"][j]["main"]))
            r_tr_all.append(abs(r["reads"][j]["r_true"]))
    med_sm = float(np.median(r_sm_all))
    med_tr = float(np.median(r_tr_all))
    print("    med |R_smooth| = %.3g (pure quadrature, no psi "
          "content) vs med |R_true| = %.3g -- ratio %.3f"
          % (med_sm, med_tr, med_sm / max(med_tr, 1e-300)))
    check("M smooth-world remainder census typed: the comb's "
          "low-frequency deviation is %s quadrature noise"
          % ("ABOVE" if med_tr > med_sm else "WITHIN"), True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, density level, "
            "declared: no deep grams recomputed)")
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
    deep_rows = []
    d_ident = 0.0
    d_sound = True
    for kz in order_kz:
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        uu = deep.EXT["U"][:ka]
        mm = deep.EXT["MU"][:ka]
        _c, D = core.atom_lags_at(alpha, Mz, uu[:1], mm[:1])
        c_ar = np.asarray(core.arch_lags(Mz, D), float)
        rs = rung_supply(alpha, Mz, uu, mm, c_ar)
        rs["kz"] = kz
        rs["h"] = float(hz)
        rs["alpha"] = float(alpha)
        deep_rows.append(rs)
        for j in READS:
            rd = rs["reads"][j]
            d_ident = max(d_ident, rd["ident_dev"]
                          / (1.0 + rs["l1_at"]))
            for c in ("B", "K", "Z"):
                tol = SOUND_TOL * rd["sup"][c] \
                    + 1e-9 * (1.0 + rs["l1_at"])
                if abs(rd["r_true"]) > rd["sup"][c] + tol:
                    d_sound = False
        Hs = [rs["reads"][j]["H"] if "H" in rs["reads"][j]
              else -(rs["reads"][j]["d_ar"] + rs["reads"][j]["main"])
              for j in CORE_J]
        print("    deep kz %-4d h %-5d X %.2e minH %+8.3f "
              "maxSUP_B %8.2f max|R| %6.2f  [%.1f s]"
              % (kz, hz, rs["X"], min(Hs),
                 max(rs["reads"][j]["sup"]["B"] for j in CORE_J),
                 max(abs(rs["reads"][j]["r_true"])
                     for j in CORE_J), time.time() - T0),
              flush=True)
    check("D2 deep identity ward (worst scaled dev %.2e)"
          % d_ident, d_ident <= IDENT_TOL, kill="K2")
    check("D3 deep soundness |R| <= SUP on every rung x read x "
          "class", d_sound, kill="K2")
    cen_d, fold_d, marg_d, short_d, hpos_d = rung_census(deep_rows)
    print("    deep censuses (%d rungs): fully closed B %d, K %d, "
          "Z %d, TRUE %d; all-H-positive %d"
          % (len(deep_rows), cen_d["B"], cen_d["K"], cen_d["Z"],
             cen_d["T"], hpos_d))
    check("D4 deep censuses recorded", True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world fires/refuses" % kind, fired, detail,
              kill="K2")
    rr9 = base.window_of(base.CTRL_KZ)
    rr9s = base.window_of(base.CTRL_KZ, scramble_seed=1)
    rs9 = rung_supply(rr9["alpha"], rr9["M"], rr9["uu"],
                      2.0 * rr9["lam"], rr9["c_ar"])
    c9t = np.asarray(core.atom_lags_at(
        rr9s["alpha"], rr9s["M"], rr9s["uu"],
        2.0 * rr9s["lam"])[0], float)
    d9s = base.grid_density(c9t)
    moves, viol = [], 0
    for j in READS:
        rd = rs9["reads"][j]
        if abs(rd["d_at"]) > 1e-300:
            moves.append(abs(float(d9s[j]) - rd["d_at"])
                         / abs(rd["d_at"]))
        if abs(float(d9s[j]) - rd["main"]) > rd["sup"]["B"]:
            viol += 1
    med_mv = float(np.median(moves)) if moves else 0.0
    print("    scramble supply-violation census (anatomy): %d/9 "
          "reads outside the Buethe budget" % viol)
    check("C3 scramble core-fold density movement: med rel move "
          "%.3f >= %.2f" % (med_mv, MOVE_BAR), med_mv >= MOVE_BAR,
          kill="K2")

    # ------------------------------------------------------------ S
    section("S -- mandatory tau screens (surface)")
    marg_lin = np.array([10.0 ** m if np.isfinite(m) else -1.0
                         for m in marg_s])
    marg_pos = np.where(marg_lin > 1.0, marg_lin - 1.0, -1.0)
    hmins = np.array([min(r["reads"][j]["H"] for j in CORE_J)
                      for r in sup_rows])
    scr_m, _ = parent.screen(marg_pos, taus1)
    scr_h, _ = parent.screen(hmins, taus1)
    print("    TAU-SCREEN buethe margin  %s" % scr_m)
    print("    TAU-SCREEN headroom       %s" % scr_h)
    check("S screens recorded", True)

    # ---------------------------------------------------- verdicts
    N = len(sup_rows) + len(deep_rows)
    nB = cen_s["B"] + cen_d["B"]
    nK = cen_s["K"] + cen_d["K"]
    nZ = cen_s["Z"] + cen_d["Z"]
    nT = cen_s["T"] + cen_d["T"]
    all_short = np.concatenate([short_s, short_d])
    all_lx = np.log10(np.array([r["X"] for r in sup_rows]
                               + [r["X"] for r in deep_rows]))
    if nB == N:
        all_m = np.concatenate([marg_s, marg_d])
        v1 = ("H1-CORE-FLOOR-CLOSED-DEPLOYED(buethe %d/%d; min "
              "margin %+.2f dex; valid X <= 1e19)"
              % (nB, N, float(np.min(all_m))))
    elif nB > 0:
        v1 = ("H1-CORE-FLOOR-PARTIAL(buethe %d/%d; med shortfall "
              "%+.2f dex)" % (nB, N, float(np.median(all_short))))
    else:
        v1 = ("H1-CORE-FLOOR-OPEN(buethe 0/%d; med shortfall %+.2f "
              "dex vs headroom)" % (N, float(np.median(all_short))))
    fold_true = sum(fold_s[j]["T"] for j in CORE_J) \
        + sum(fold_d[j]["T"] for j in CORE_J)
    fold_tot = 8 * N
    rt_all = np.array([abs(r["reads"][j]["r_true"])
                       for r in sup_rows + deep_rows
                       for j in CORE_J])
    sb_all = np.array([r["reads"][j]["sup"]["B"]
                       for r in sup_rows + deep_rows
                       for j in CORE_J])
    env_waste = float(np.median(np.log10(
        sb_all / np.maximum(rt_all, 1e-300))))
    if nT > nB:
        v1b = ("ENVELOPE-LOSES(TRUE-ceiling %d/%d rungs vs buethe "
               "%d; med envelope waste %+.2f dex)"
               % (nT, N, nB, env_waste))
    elif nT < N:
        v1b = ("SEAT-DEEPER(TRUE-ceiling %d/%d rungs, %d/%d folds:"
               " the comb's true low-frequency deviation exceeds "
               "the arch headroom; envelope waste med %+.2f dex on"
               " top)" % (nT, N, fold_true, fold_tot, env_waste))
    else:
        v1b = "TRUE-CEILING-FULL(%d/%d)" % (nT, N)
    v2 = "KAPPA-BASELINE(%d/%d closed; CLXXVIII %s)" % (
        nK, N, "reproduced" if nK == 0 else "MOVED")
    # shortfall of the ZFR class specifically
    zshort = []
    for r in sup_rows + deep_rows:
        zs = max(r["reads"][j]["sup"]["Z"]
                 / max(r["reads"][j]["H"], 1e-300)
                 for j in CORE_J)
        zshort.append(math.log10(zs))
    slope_z, r2_z = parent.ols_line(all_lx, np.array(zshort))
    if nZ == N:
        v3 = "ZFR-CLOSES-DEPLOYED(%d/%d)" % (nZ, N)
    elif slope_z > ZFR_DIV_SLOPE:
        v3 = ("ZFR-DIVERGES(%d/%d closed; shortfall slope %+.2f "
              "dex per dex X, R2 %.2f -- the exp(-c sqrt(log x)) "
              "class NEVER meets the O(1) demand; crossover vs "
              "kappa only at X* = %.1e)"
              % (nZ, N, slope_z, r2_z, xstar))
    else:
        v3 = ("ZFR-SHORTFALL-FLAT(%d/%d; slope %+.2f, med %+.2f "
              "dex)" % (nZ, N, slope_z,
                        float(np.median(zshort))))
    if nB == N and n_a0pos == 39 and \
            all(g > 0 for g in gersh):
        v4 = "W1-COMPOSED-SEMI(measured-b conditional)"
    elif nB == N:
        v4 = ("W1-COMPOSED-BLOCKED(concentration med %+.2f dex; "
              "H2 upper law absent)"
              % (float(np.median(conc)) if conc else float("nan")))
    else:
        v4 = ("W1-COMPOSED-VOID(core floor not closed; a0_sup > 0 "
              "on %d/39); RHO-STILL-CONDITIONAL (CLXXIX cited)"
              % n_a0pos)
    kgap_txt = ("med %+.2f dex" % float(np.median(kgap))) if kgap \
        else "n/a: a0_sup <= 0 everywhere, no positive CS target"
    v5 = ("H2-CS-NEEDS-DIAG-LAW(needed K_up %s below measured max "
          "K; the supply cannot produce it -- CLXXVIII J2 verdict "
          "unmoved)" % kgap_txt)
    # Buethe carrying-range extrapolation (anatomy)
    all_alpha = np.array([r["alpha"] for r in sup_rows]
                         + [r["alpha"] for r in deep_rows])
    fin = np.isfinite(np.concatenate([marg_s, marg_d]))
    mm_all = np.concatenate([marg_s, marg_d])
    if int(np.sum(fin)) >= 3:
        sl_b, r2_b = parent.ols_line(all_alpha[fin], mm_all[fin])
        print("\n    ANATOMY: buethe min-fold margin trend %+.3f "
              "dex per unit alpha (R2 %.2f)" % (sl_b, r2_b))
    print("    ANATOMY: ZFR shortfall law slope %+.3f dex per dex "
          "X (R2 %.2f); envelope crossover X* = %.2e" % (
              slope_z, r2_z, xstar))
    check("V1 typed: %s" % v1, True)
    check("V1b typed: %s" % v1b, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v1b=v1b, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
