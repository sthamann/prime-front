#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""h1h2_envelope_derivation_probe -- PRIME.PORT.W1.ALLH.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE ALL-H ATTEMPT.  w1_christoffel_floor_
probe (CLXXVII, SPEC-SHA 903714c1..) closed W1 on the surface with
c1 ~ 1 and froze the exact classical statement whose ONLY open half
is the all-h uniformity of two hypotheses about nu_+:
    (H1)  min_i v_i K_h(y_i, y_i) >= a0 > 0      (weight/Christoffel
          floor; measured a med 0.968, flat),
    (H2)  max_i sum_{j!=i} sqrt(v_i v_j) |K_h(y_i, y_j)| <= b0 < a0
          (CD off-diagonal decay; measured b med 0.202, flat),
    ==>   G_core >= (a0 - b0) I  ==>  s_P >= a0 - b0 for EVERY unit
          frame direction (Gershgorin; frame-free by the CLXXVII
          reduction inf_{|v0|=1} s_P = lambda_min(G_core)).
H1/H2 are COARSE regularity statements about the positive folded
measure -- not fine-phase statements.  The corpus owns GLOBAL,
unconditional inputs of exactly that type:
  ENV   the Chebyshev envelope kappa = 0.038821 on psi(x)/x at all
        jump points (KAPPA_REF, verification/v563_paper2_readouts.py
        line 134; re-verified over [100, 1e9] as ward G1.2 of the QF
        modules, verification/v770_qf_spectral_bundle.py lines
        1433-1438 "deep-range Chebyshev envelope ... over all jump
        points of psi(x)/x"; the Buethe sqrt-envelope |psi(x)-x| <
        0.94 sqrt(x), 11 < x <= 1e19, is deployed in
        verification/v594_unconditional_cert.py lines 10-13, 47 --
        cited, not consumed here: the kappa form suffices),
  CHEB  the global bound psi(x) <= B_PSI x = 1.03883 x for all x
        (Chebyshev 1852 / Rosser-Schoenfeld 1962; v563 line 136),
  MASS  the v882-class total-mass laws (sqrt-uniformization of the
        weighted prime measure; v882_port_source_mellin.py) -- here
        derived explicitly from ENV/CHEB by partial summation,
  WCONV the frozen window conventions (D = alpha/M tent grid,
        NU_MAIN = 4 slot rule, CORE_J = (2,...,16), folded
        4 sin^2(theta/2) weights, h = M/2),
  ARCH  the archimedean lag layer c_ar (comb-free, deterministic).
THE QUESTION (frozen): do H1 and H2 FOLLOW, with explicit
constants, from ENV + CHEB + MASS + WCONV + ARCH alone -- i.e. is
W1 an ALL-H THEOREM over the global comb regularity?  Every
derivation step below is an inequality with an explicit constant,
verified numerically per rung (39 surface steps + 27 deep steps),
with the honest slack ladder per step of the chain.  HONESTLY: even
a full derivation would NOT be the wall -- W2 / background
cancellation remain untouched and RH-hard; this is stated in every
verdict path.

(a) THE OBJECTS AS COMB FUNCTIONALS.  Per rung r2 (kz, h, M, D,
alpha), L = 2M - 2, X = e^{2 alpha}: the lag vector is c = c_ar +
c_at with c_at the T115 tent assembly of the von-Mangoldt atoms
mu_n = 2 Lambda(n)/sqrt(n), n <= X; the grid density d_j (j < L) is
the symmetrized FFT of c; nu_+ / nu_- are the +/- folded parts with
weights 4 sin^2(pi j / L)/L per fold pair {j, L-j}; the 8 core
nodes are y_i = cos(2 pi j_i / L), j_i in CORE_J, with nu_- masses
    v_i = (4 sin^2(pi j_i / L)/L) * max(-d_{j_i}, 0)
(exact reconstruction ward V below); m0 = nu_+ total mass; K_h =
CD kernel of the Lanczos chain of nu_+.  So H1/H2 are explicit
functionals of the comb data through the fold, and the derivation
chain must bound them from the global inputs only.

(b) THE DERIVATION CHAIN FOR H1 (each step an inequality with an
explicit constant, verified per rung):
 E3  MASS LAWS (all-h valid, from ENV + CHEB by partial summation
     Sum_{n<=X} Lambda(n)/sqrt(n) = psi(X)/sqrt(X)
       + (1/2) Int_1^X psi(t) t^{-3/2} dt):
       M_at := Sum_n mu_n <= M_up := 2 B_PSI (2 sqrt(X) - 1),
       M_at >= M_lo := 2 (1-kappa)(2 sqrt(X) - 10) - C_LO,
     (C_LO = 2 frozen; the lower form uses the jump-point envelope
     for X >= 100 with the [1,100] segment dropped -- declared).
 I2  DENSITY PERTURBATION (WCONV tent geometry): the tents are a
     partition of unity, per atom Sum_i tent_i(u_n) <= TENT_CAP = 2
     (interior value 1 + reflection), so
       l1_at := Sum_i |c_at[i]| <= (TENT_CAP/2) M_at <= M_up,
       Delta := max_j |d_j - d^ar_j| <= Delta_lag := 2 l1_at
              <= Delta_env := 2 M_up.
 I3  CORE-MASS FLOOR (the decisive rung): for each core fold,
       v_i >= v^env_i := w_i (-d^ar_{j_i} - Delta_env),
     w_i = 4 sin^2(pi j_i/L)/L, with the two sharper tiers
     v^lag_i (Delta_lag) and v^meas_i (measured Delta) that
     localize WHERE the route loses: envelope coarseness (env vs
     lag), L1 -> Linf lag cancellation (lag vs meas), or the arch
     layer not carrying the core-fold sign at all (the fine-phase
     seat: census of sign(d^ar) at CORE_J and of the atom share
     |d - d^ar| / |d| there).
 I1  TRIVIAL CHRISTOFFEL FLOOR (exact algebra, all-h): K_h(y, y)
     = Sum_{k<h} p_k(y)^2 >= p_0^2 = 1/m0, and
       m0 <= m0_up := m0_ar_abs + Delta_env
     (m0_ar_abs = (1/(2L)) Sum_j 4 sin^2 |d^ar_j|, comb-free).
 I4  COMPOSE: a >= a0_env := min_i v^env_i / m0_up.  Slack ladder
     a0_env / a0_lag / a0_meas vs the measured a, per step, bands +
     deficit orders.  The RATIO ANATOMY min_i v_i / m0 (the exact
     content of the trivial floor) is printed as its own ladder --
     if it is flat and positive, the reduced all-h question is a
     RATIO mass law of the fold (named).

(c) THE DERIVATION CHAIN FOR H2:
 J1  CAUCHY-SCHWARZ VALIDITY (exact): b <= max_i sqrt(G_ii) *
     Sum_{j!=i} sqrt(G_jj) -- warded per step.
 J2  THE GLOBAL CLOSURE ATTEMPT (frozen honestly): the frozen
     global input set contains NO upper Christoffel law K_h(y,y)
     <= K_up(global) and NO off-diagonal decay law at separation
     h_sep ~ 1/2 (see MZ below) -- so the sharpest derivable
     global bound is the CS row bound of J1, which cannot beat a.
     J2 therefore MEASURES the minimal missing input: the diagonal
     family chi = max_i G_ii (band + h-trend + tau-screen) and the
     nearest-fold share of the off-row sum (does the off-mass sit
     at adjacent folds -- a local decay law would then suffice).
     Typed H2-SLACK-FAILS(J2-no-global-closure, missing law named)
     unless the measured b >= a somewhere (worse, typed).
 MZ  THE SEPARATION ANSWER (exact, all-h, conventions only): the
     core folds are consecutive even grid points, so
       h_sep == (2h/L) == M/(2M-2) -> 1/2   (h = M/2),
     an IDENTITY of WCONV -- warded per rung (surface + deep)
     against the measured arccos value.  CONSEQUENCE: the CLXXVII
     MZ risk is CLOSED as a convention identity (no separation
     HYPOTHESIS remains to prove), but its value 1/2 sits OUTSIDE
     the MZ/Lubinsky regime (needs >> 1): the classical asymptotic
     route to H2 is structurally unavailable at these nodes; any
     all-h H2 proof must be a non-MZ mechanism.  The derivation
     route does NOT need a separation hypothesis; the envelope
     does not need to control it -- the conventions pin it.

(d) GATES.  TAU-SCREENS (parent bands PASS |s| <= 0.30 / RELOC >=
0.70): measured a, a - b, and the I4 ratio family.  THE ARITHMETIC
SEAT (first-class): the identical density-level chain is run on
the comb-free SMOOTH world (same arch layer, PNT masses): censuses
of sign(d^ar) (shared), the I3 tiers, and the measured battery
a_sm - b_sm (CLXXVII: 26/37) decide WHICH inequality consumes comb
structure -- frozen seat rule: if the I3 tier censuses agree
between worlds while the battery censuses differ, the comb
consumption sits in the measured H1/H2 VALUES (the fine conditioning
of nu_+), not in any envelope-visible mass law; the seat is then
typed at the H2/battery leg with the smooth off-diagonal explosion
as the measured carrier.  ANTI-CIRCULARITY (frozen): no sigma_h, no
forward pivot sign, no target eigendata, no wall positivity (A or
R block) in any DERIVED bound; the wall enters only the W-block
reproduction wards.  CONTROLS (kill if silent): C1 smooth world
refuses the certificate ladder; C2 Epstein + scramble fire (parent
verbatim); C3 scramble core-fold density movement recorded (fires
med rel move >= MOVE_BAR where the scramble core exists; disclosed
skip if dead).

VERDICT (frozen enums, decided by the rules below and nothing else):
  H1-DERIVED(min a0_env) iff every I/E ward passes AND a0_env > 0
    on all surface + deep steps AND the combined h-trend
    |slope(log a0_env)| <= HTREND_FLAT;
  else H1-SLACK-FAILS(tier) with tier = the FIRST failing rung in
    the order I2-envelope (a0_lag > 0 everywhere but a0_env not),
    I2-lag (a0_meas > 0 everywhere but a0_lag not), I3-arch-
    magnitude (arch sign full but a0_meas fails), I3-fine-phase
    (sign census of d^ar at CORE_J not fully negative) -- each with
    the deficit band and the named stronger-but-still-global input.
  H2-DERIVED(b0) iff a global closure bound b0 < min measured a
    exists inside the frozen input set (per J2 this requires an
    upper diagonal law -- absent by construction; the enum exists
    so the rule is falsifiable);
  else H2-SLACK-FAILS(J2-no-global-closure | J1-violated | B-GE-A).
  Headline: W1-ALLH-CANDIDATE(c1 = a0 - b0, gaps named) iff both
    DERIVED; else W1-ALLH-BLOCKED(H1 tier, H2 tier).
  MZ-CLOSED-BY-CONVENTION(n/N wards) always typed.
  SEAT(...) always typed per the frozen rule above.
DEAD overrides (kill anyway): parent reproduction fails, any V/I1/
J1/E3/I2 transcription ward breaks, h_sep identity ward fails.

FROZEN BARS: V_WARD = 1e-9 (rel core-mass reconstruction);
I1_TOL = 1e-12; CS_TOL = 1e-10 (rel); HSEP_WARD = 1e-9 (abs);
C_LO = 2.0; TENT_CAP = 2.0; REPRO_A_MED = 0.968, REPRO_B_MED =
0.202, REPRO_RTOL = 5e-2; HTREND_FLAT = 0.30; slope bands
0.30/0.70 (parent verbatim); MOVE_BAR = 0.05; MIN_DEEP = 10;
KAPPA/TOL_KAPPA/B_PSI from v563 (read-only constants); parent
bars (MINB_REF 0.679, GAP 0.052/0.888, rtol as parent) inherited
verbatim; parent SPEC-SHA warded == 084c9689..; wedge SPEC-SHA
prefix warded == 26855819.  Runtime cap declared: 20 min.  Smoke
mode H1H2_SMOKE=1 restricts the deep block to the 4 shallowest new
rungs (surface + controls always full); any smoke run is disclosed
here before the freeze.

ANTI-CIRCULARITY (frozen, restated): every DERIVED bound consumes
only ENV/CHEB/MASS/WCONV/ARCH; the comb enters the derivation ONLY
through envelope-bounded aggregates (never fine phases, never wall
data); measured H1/H2/K/m0 values appear as the slack ladder's
truth column and as anatomy, never inside a derived constant.  The
smooth battery and all controls are parent-verbatim machinery.

ANTHROPIC NO-GO DECLARATION: the derived route reads total-mass
envelopes and window geometry (two-moment-class global data), and
its measured target is an 8x8 CD-kernel Gram -- strictly beyond
two scalar moments plus bandwidth-1 pair correlation on the
MEASURED side; the derivation attempt failing at the envelope
level is consistent with (and quantifies) the no-go's boundary.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(H1H2_SMOKE=1, 33/33 on the FIRST passage, 9.5 s; deep block on
the 4 shallowest new rungs -> 3 deep steps).  NO bar, band, count,
rule or enum was moved after it; post-smoke changes are this
disclosure block and ONE disclosed amendment A1 (below).  Measured
smoke context the frozen run must confirm: W green (42/41/39, minB
0.6790, gap 0.0520/0.8875, s_P >= mu1 39/39, a med 0.9680, b med
0.2021); E1 kappa 0.038821 both tables; E2 max psi(x)/x 1.03882
<= B_PSI; E3 39/39 + 3/3 deep, mass slack up min/med 1.041/1.048x,
lo min/med 0.773/0.919x (the envelope route is TIGHT at total-mass
level); V ward 2.4e-13; I1 min m0 K = 3.96e4 (the trivial floor is
4 orders above 1 -- the Christoffel sum concentrates); A6 h_sep
identity dev 1.6e-12 on 39/39 + 3/3 deep -- MZ CLOSED BY
CONVENTION; I2 chain 39/39 with the honest surprise Delta_meas med
381 == Delta_lag med 382 (NO L1->Linf cancellation gain: the max
sits at the DC component j = 0 where all tent lags are one-signed)
and Delta_env med 802 (0.3 dex); I3 THE DECISIVE CENSUS: the arch
density DOES carry the core-fold sign (narch med 8/8, min 6/8;
d^ar at CORE_J band -3.14/-0.71/+0.26) but only ~6 percent of the
magnitude -- atom share |d - d^ar|/|d| at CORE_J med 0.94: the
core-fold density values ARE low-frequency prime partial sums, and
the GLOBAL Linf perturbation bound (med 381) sits ~2.5 orders
above the local |d^ar| scale (med 0.71): tier positives a0_env =
a0_lag = a0_meas = 0/39 -- the route loses at the LOCALIZATION of
the density bound to the low-frequency folds, not at the total-
mass envelope; I4 ratio anatomy min v_i/m0 med 9.8e-07, h-trend
-2.07 (R2 0.65) -- the p_0-only floor decays at the mu1 ~ h^-2
scale, 6 orders below the measured a ~ 0.97; J1 CS ward 39/39
(worst b/CS 0.075 -- CS is 13x loose the OTHER way); J2 chi med
0.9799 flat (+0.016), nearest-fold share med 0.153; SEAT: smooth
I3 censuses IDENTICAL (narch med 8, tiers 0/0/0 both worlds),
smooth battery 24/37 vs truth 39/39 -- the comb consumption sits
in the measured H1/H2 VALUES (fine conditioning of nu_+), the
envelope-visible chain is world-identical; D deep 3/3: a med
0.9924, b med 0.0492, narch 8, tiers 0; C1 smooth refuses
(refused 42, usable 0), C2 Epstein + scramble fire, C3 scramble
core dead -> disclosed skip; screens a PASS(-0.007), a-b
PASS(-0.052), v/m0 AMBIG(+0.544, R2 0.539).  Verdicts pinned by
the frozen rules: H1-SLACK-FAILS(last branch), H2-SLACK-FAILS(J2),
headline W1-ALLH-BLOCKED, MZ-CLOSED-BY-CONVENTION.  AMENDMENT A1
(disclosed, print-only): the last H1 branch label as drafted said
"the arch layer does not carry the core-fold sign", which the
smoke's own census contradicts (narch med 8/8; the arch carries
the SIGN, the comb carries ~94 percent of the MAGNITUDE); the
label text is corrected to name the measured seat (low-frequency
magnitude, comb-dominated) and prints narch + atom share.  The
branch CONDITION, order, bars and all decision rules are
unchanged; no census or number moved.  The frozen run repeats
everything on the FULL deep block (27 expected steps); enums move
only as the full data says.

NO RH claim.  Even H1-DERIVED + H2-DERIVED would certify only the
skeleton half of W1 for all h; W2 / background cancellation remain
RH-hard and untouched.  A blocked verdict is itself the finding:
it localizes the all-h gap of W1 to a named non-envelope input.
No marker moves.  Stdout only.
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
import wedge_scale_law_probe as wedge  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
WEDGE_SHA8 = "26855819"
V_WARD = 1.0e-9
I1_TOL = 1.0e-12
CS_TOL = 1.0e-10
HSEP_WARD = 1.0e-9
C_LO = 2.0
TENT_CAP = 2.0
REPRO_A_MED = 0.968
REPRO_B_MED = 0.202
REPRO_RTOL = 5.0e-2
HTREND_FLAT = 0.30
MOVE_BAR = 0.05
MIN_DEEP = 10
CORE_J = base.CORE_J
SMOKE = os.environ.get("H1H2_SMOKE", "") == "1"
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


def battery_split(Gc):
    a = float(np.min(np.diag(Gc)))
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    b = float(np.max(off))
    return a, b


def mass_bounds(X, kappa):
    """The E3 mass laws (explicit constants, all-h)."""
    up = 2.0 * core.B_PSI * (2.0 * math.sqrt(X) - 1.0)
    lo = 2.0 * (1.0 - kappa) * (2.0 * math.sqrt(X) - 10.0) - C_LO
    return up, lo


def chain_data(alpha, M, uu, mm, c_ar):
    """The per-rung derivation data (truth comb)."""
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    d = base.grid_density(c_ar + c_at)
    d_ar = base.grid_density(c_ar)
    L = 2 * M - 2
    X = math.exp(2.0 * alpha)
    M_at = float(np.sum(mm))
    l1_at = float(np.sum(np.abs(c_at)))
    delta_meas = float(np.max(np.abs(d - d_ar)))
    m_up, m_lo = mass_bounds(X, core.KAPPA_REF)
    delta_lag = 2.0 * l1_at
    delta_env = 2.0 * m_up
    jj = np.arange(L)
    w_all = 4.0 * np.sin(math.pi * jj / L) ** 2
    m0_ar_abs = float(np.sum(w_all * np.abs(d_ar))) / (2.0 * L)
    out = dict(L=L, X=X, M_at=M_at, l1_at=l1_at, m_up=m_up,
               m_lo=m_lo, delta_meas=delta_meas, delta_lag=delta_lag,
               delta_env=delta_env, m0_ar_abs=m0_ar_abs)
    rows = []
    for j in CORE_J:
        w_geo = 4.0 * math.sin(math.pi * j / L) ** 2 / L
        rows.append(dict(j=j, w_geo=w_geo, d=float(d[j]),
                         dar=float(d_ar[j])))
    out["core"] = rows
    return out


def tier_floors(cd):
    """(a0_env, a0_lag, a0_meas, narch, min v/m0 numerators)."""
    m0_up = cd["m0_ar_abs"] + cd["delta_env"]
    vals = {}
    for tag, dl in (("env", cd["delta_env"]), ("lag", cd["delta_lag"]),
                    ("meas", cd["delta_meas"])):
        vlo = min(r["w_geo"] * (-r["dar"] - dl) for r in cd["core"])
        vals[tag] = vlo / m0_up
    narch = sum(1 for r in cd["core"] if r["dar"] < 0.0)
    return vals, narch, m0_up


def measured_h1h2(Gc, v_core, m0):
    a, b = battery_split(Gc)
    kdiag = np.diag(Gc) / v_core
    ratio = float(np.min(v_core)) / m0
    return a, b, kdiag, ratio


def cs_bound(Gc):
    sq = np.sqrt(np.diag(Gc))
    tot = float(np.sum(sq))
    return float(np.max(sq * (tot - sq)))


def nn_share(Gc):
    """Nearest-fold share of the worst off-row."""
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    i = int(np.argmax(off))
    n = Gc.shape[0]
    near = 0.0
    for k in (i - 1, i + 1):
        if 0 <= k < n:
            near += abs(Gc[i, k])
    return near / max(off[i], 1e-300)


def hsep_of(y_core, h):
    th = np.arccos(np.clip(y_core, -1.0, 1.0))
    dth = np.abs(th[:, None] - th[None, :])
    np.fill_diagonal(dth, np.inf)
    return float(np.min(dth)) * h / (2.0 * math.pi)


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("H1H2ENV-MEASURED / %s / %s / %s / %s / %s"
                   % (labels.get("h1", "-"), labels.get("h2", "-"),
                      labels.get("mz", "-"), labels.get("seat", "-"),
                      labels.get("head", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every derived constant consumes only the named
  global inputs (kappa envelope, Chebyshev B_PSI, mass laws, window
  conventions, arch layer); every slack number is a statement about
  the float64-computed pipeline objects.  A blocked verdict
  localizes the all-h gap of W1 to a named non-envelope input; a
  derived verdict would still leave W2 / background cancellation
  (the RH-hard wall) untouched.  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.ALLH.01 -- H1/H2 from global comb "
            "regularity: the all-h derivation attempt "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    wedge_sha = hashlib.sha256(
        wedge.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    wedge  SPEC SHA-256 = %s" % wedge_sha)
    print("    NO RH claim.  Global inputs: kappa 0.038821 "
          "(v563:134, v770:1433-1438 G1.2), B_PSI 1.03883 "
          "(v563:136), v882 mass laws, WCONV, ARCH.")
    if SMOKE:
        print("    *** SMOKE MODE: deep on 4 shallowest new rungs ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c wedge SPEC prefix reproduced",
          wedge_sha[:8] == WEDGE_SHA8, wedge_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder + CLXXIV/CLXXVII reproduction")
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
    n_l2 = sum(w["sP"] >= w["mu1"] for w in rows)
    check("W3 CLXXIV reproduction s_P >= mu1",
          n_l2 == len(rows), "%d/%d" % (n_l2, len(rows)), kill="K2")
    for w in rows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    ab = [battery_split(w["Gc"]) for w in rows]
    a_med = float(np.median([x[0] for x in ab]))
    b_med = float(np.median([x[1] for x in ab]))
    check("W4 CLXXVII H1/H2 reproduction (a med %.4f == %.3f, "
          "b med %.4f == %.3f)" % (a_med, REPRO_A_MED, b_med,
                                   REPRO_B_MED),
          abs(a_med / REPRO_A_MED - 1.0) <= REPRO_RTOL
          and abs(b_med / REPRO_B_MED - 1.0) <= REPRO_RTOL,
          kill="K2")
    hs = np.array([float(w["r2"]["h"]) for w in rows])
    taus1 = np.array([w["tau"] for w in rows])

    # ------------------------------------------------------------ E
    section("E -- the global inputs (verified, cited)")
    kap = core.chebyshev_kappa()
    check("E1 Chebyshev envelope kappa = %.6f == KAPPA_REF %.6f "
          "(v563:134; deep-range ward v770:1433-1438 G1.2, "
          "[100, 1e9] class)" % (kap, core.KAPPA_REF),
          kap <= core.KAPPA_REF + core.TOL_KAPPA, kill="K2")
    nn = core._NN.astype(float)
    psi = np.cumsum(core.LAM_TAB[core._NN])
    ratio_max = float(np.max(psi / nn))
    check("E2 global Chebyshev bound max psi(x)/x = %.5f <= "
          "B_PSI = %.5f (v563:136, all x)" % (ratio_max, core.B_PSI),
          ratio_max <= core.B_PSI, kill="K2")

    # -------------------------------------------- per-rung chains
    section("A -- the derivation chains on the 39 surface steps")
    print("    E3 mass laws | I2 density perturbation | I3 core-"
          "mass floor tiers | I1/I4 compose | J1/J2 for H2")
    v_dev = 0.0
    i1_min = float("inf")
    cs_worst = 0.0
    hsep_dev = 0.0
    n_e3 = n_i2 = 0
    slack_up, slack_lo = [], []
    d_orders = []
    tier_pos = dict(env=0, lag=0, meas=0)
    narch_list = []
    atom_share = []
    a0_env_all, ratio_all = [], []
    chi_all, nnsh_all = [], []
    a_all = np.array([x[0] for x in ab])
    b_all = np.array([x[1] for x in ab])
    for w in rows:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        mm = 2.0 * rr["lam"]
        cd = chain_data(rr["alpha"], rr["M"], rr["uu"], mm,
                        rr["c_ar"])
        w["cd"] = cd
        # E3 wards
        ok_up = cd["M_at"] <= cd["m_up"]
        ok_lo = cd["M_at"] >= cd["m_lo"]
        n_e3 += ok_up and ok_lo
        slack_up.append(cd["m_up"] / cd["M_at"])
        slack_lo.append(cd["m_lo"] / cd["M_at"])
        # I2 chain
        n_i2 += (cd["delta_meas"] <= cd["delta_lag"] + 1e-12
                 and cd["delta_lag"] <= cd["delta_env"] + 1e-12)
        d_orders.append((cd["delta_meas"], cd["delta_lag"],
                         cd["delta_env"]))
        # V ward: core masses reconstruct
        for r, vv in zip(cd["core"], r2["v_core"]):
            rec = r["w_geo"] * max(-r["d"], 0.0)
            v_dev = max(v_dev, abs(rec - vv) / max(vv, 1e-300))
        # I3 tiers + seat censuses
        vals, narch, m0_up = tier_floors(cd)
        narch_list.append(narch)
        for tag in ("env", "lag", "meas"):
            if vals[tag] > 0.0:
                tier_pos[tag] += 1
        a0_env_all.append(vals["env"])
        atom_share.append(np.median(
            [abs(r["d"] - r["dar"]) / max(abs(r["d"]), 1e-300)
             for r in cd["core"]]))
        # I1 / I4 measured side
        m0 = r2["chain"][2]
        a, b, kdiag, ratio = measured_h1h2(w["Gc"], r2["v_core"], m0)
        i1_min = min(i1_min, float(np.min(kdiag)) * m0)
        ratio_all.append(ratio)
        # J1 / J2
        csb = cs_bound(w["Gc"])
        cs_worst = max(cs_worst, b / max(csb, 1e-300))
        chi_all.append(float(np.max(np.diag(w["Gc"]))))
        nnsh_all.append(nn_share(w["Gc"]))
        # MZ identity
        hsep_m = hsep_of(r2["y_core"], r2["h"])
        hsep_c = float(r2["h"]) / (rr["M"] - 1.0)
        hsep_dev = max(hsep_dev, abs(hsep_m - hsep_c))
    check("A1 V ward: core-mass reconstruction v_i == "
          "w_geo max(-d_j, 0)", v_dev <= V_WARD,
          "max rel dev %.2e" % v_dev, kill="K2")
    check("A2 E3 mass laws hold on every step (%d/%d); slack "
          "up min/med %.3f/%.3f x, lo min/med %.3f/%.3f x"
          % ((n_e3, len(rows)) + band(np.array(slack_up))[:2]
             + band(np.array(slack_lo))[:2]),
          n_e3 == len(rows), kill="K2")
    check("A3 I2 perturbation chain Delta_meas <= Delta_lag <= "
          "Delta_env on every step (%d/%d)" % (n_i2, len(rows)),
          n_i2 == len(rows), kill="K2")
    dm, dl, de = (np.array([x[0] for x in d_orders]),
                  np.array([x[1] for x in d_orders]),
                  np.array([x[2] for x in d_orders]))
    print("    Delta_meas med %.3g | Delta_lag med %.3g | "
          "Delta_env med %.3g" % (float(np.median(dm)),
                                  float(np.median(dl)),
                                  float(np.median(de))))
    print("    orders lost: lag/meas med %.1f dex, env/lag med "
          "%.1f dex" % (float(np.median(np.log10(dl / dm))),
                        float(np.median(np.log10(de / dl)))))
    check("A4 I1 trivial floor m0 K_h(y,y) >= 1 (exact algebra)",
          i1_min >= 1.0 - I1_TOL, "min %.9f" % i1_min, kill="K2")
    check("A5 J1 Cauchy-Schwarz row bound valid on every step",
          cs_worst <= 1.0 + CS_TOL, "worst b/CS %.3f" % cs_worst,
          kill="K2")
    check("A6 MZ identity h_sep == M/(2M-2) (conventions only)",
          hsep_dev <= HSEP_WARD, "max abs dev %.2e" % hsep_dev,
          kill="K2")

    # ------------------------------------------------------------ I3
    section("I3 -- the decisive census (the arithmetic seat data)")
    narch_arr = np.array(narch_list)
    print("    arch-negative core folds narch: min/med/max "
          "%d/%d/%d of 8" % (int(np.min(narch_arr)),
                             int(np.median(narch_arr)),
                             int(np.max(narch_arr))))
    dar_core = np.array([r["dar"] for w in rows
                         for r in w["cd"]["core"]])
    print("    d^ar at CORE_J: min/med/max %+.4g / %+.4g / %+.4g"
          % band(dar_core))
    print("    atom share |d - d^ar|/|d| at CORE_J (per-step med): "
          "min/med/max %.3g / %.3g / %.3g"
          % band(np.array(atom_share)))
    print("    tier positives: a0_env %d/39, a0_lag %d/39, "
          "a0_meas %d/39" % (tier_pos["env"], tier_pos["lag"],
                             tier_pos["meas"]))
    a0e = np.array(a0_env_all)
    print("    a0_env band %.3g / %.3g / %.3g (measured a med "
          "%.4f)" % (band(a0e) + (a_med,)))
    check("I3 censuses recorded", True)

    # ------------------------------------------------------------ I4
    section("I4 -- ratio anatomy + slack ladder vs measured a")
    rat = np.array(ratio_all)
    sl_r, r2_r = parent.ols_line(np.log(hs), np.log(rat))
    print("    min_i v_i / m0 (exact content of the p_0 floor): "
          "band %.3g / %.3g / %.3g; h-trend %+.3f (R2 %.3f)"
          % (band(rat) + (sl_r, r2_r)))
    print("    measured a band %.4f / %.4f / %.4f; b band "
          "%.4f / %.4f / %.4f" % (band(a_all) + band(b_all)))
    check("I4 slack ladder recorded", True)

    # ------------------------------------------------------------ J2
    section("J2 -- the missing global input for H2 (measured)")
    chi = np.array(chi_all)
    sl_c, r2_c = parent.ols_line(np.log(hs), np.log(chi))
    nnsh = np.array(nnsh_all)
    print("    chi = max_i G_ii: band %.4f / %.4f / %.4f; h-trend "
          "%+.3f (R2 %.3f)" % (band(chi) + (sl_c, r2_c)))
    print("    nearest-fold share of the worst off-row: band "
          "%.3f / %.3f / %.3f" % band(nnsh))
    print("    frozen statement: no upper Christoffel / decay law "
          "exists in the global input set; the CS row bound (J1) "
          "cannot beat a -- the missing law is a LOCAL one at "
          "separation ~1/2 (MZ regime unreachable, see A6).")
    check("J2 missing-input census recorded", True)

    # ------------------------------------------------------------ M
    section("M -- the arithmetic seat (smooth world, identical "
            "density chain)")
    sm_narch, sm_tier, sm_bat = [], dict(env=0, lag=0, meas=0), []
    n_sm = 0
    for w in rows:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        mm = 2.0 * rr["lam"]
        _uu, mm_sm = base.world_smooth(rr["uu"], mm, rr)
        cds = chain_data(rr["alpha"], rr["M"], rr["uu"], mm_sm,
                         rr["c_ar"])
        vals, narch, _m0up = tier_floors(cds)
        sm_narch.append(narch)
        for tag in ("env", "lag", "meas"):
            if vals[tag] > 0.0:
                sm_tier[tag] += 1
        n_sm += 1
    sm_map = {}
    n_smb = n_smc = 0
    for kz in zones:
        r = base.gram_anatomy(kz, world_fn=base.world_smooth,
                              keep_chain=True)
        if isinstance(r, dict):
            sm_map[kz] = r
    for kz, r in sorted(sm_map.items()):
        if not (r.get("core_ok") and "chain" in r
                and "y_core" in r):
            continue
        al, be, m0s = r["chain"]
        Pc = base.eval_chain(al, be, m0s, r["y_core"], r["h"])
        H0 = np.sqrt(r["v_core"])[:, None] * Pc
        Gs = H0 @ H0.T
        a_s, b_s = battery_split(0.5 * (Gs + Gs.T))
        sm_bat.append(a_s - b_s)
        n_smb += 1
        if a_s - b_s > 0.0:
            n_smc += 1
    sm_narch_a = np.array(sm_narch)
    same_i3 = (int(np.median(sm_narch_a)) ==
               int(np.median(narch_arr))
               and sm_tier == tier_pos)
    print("    smooth I3: narch med %d (truth %d); tier positives "
          "env/lag/meas %d/%d/%d (truth %d/%d/%d)"
          % (int(np.median(sm_narch_a)), int(np.median(narch_arr)),
             sm_tier["env"], sm_tier["lag"], sm_tier["meas"],
             tier_pos["env"], tier_pos["lag"], tier_pos["meas"]))
    if sm_bat:
        print("    smooth battery a-b > 0 on %d/%d (truth: %d/39); "
              "a-b band %+.3g / %+.3g / %+.3g"
              % ((n_smc, n_smb,
                  int(np.sum(a_all - b_all > 0.0))) + band(
                      np.array(sm_bat))))
    n_truth_ab = int(np.sum(a_all - b_all > 0.0))
    if same_i3 and n_smc < n_smb and n_truth_ab == len(rows):
        seat = ("ARITH-SEAT(H2-battery: smooth %d/%d vs truth "
                "39/39; envelope-visible chain world-identical)"
                % (n_smc, n_smb))
    else:
        seat = ("ARITH-SEAT(mixed: I3-identical=%s, smooth-battery "
                "%d/%d, truth a-b>0 %d/39)"
                % (same_i3, n_smc, n_smb, n_truth_ab))
    check("M typed: %s" % seat, True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, float level declared)")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(deep.EXT["NN"][:nP], core._NN)
               and np.array_equal(deep.EXT["U"][:nP], core.U_ALL)
               and np.array_equal(deep.EXT["MU"][:nP], core.MU_ALL))
    check("D1 deep-table fidelity: overlap dev %.1e == 0.0, "
          "prefixes bitwise" % dev, dev == 0.0 and ok_pref,
          kill="K2")
    nn_e = deep.EXT["NN"].astype(float)
    psi_e = np.cumsum(lam_ext[deep.EXT["NN"]])
    keep = nn_e >= core.KAPPA_X0
    kap_e = float(np.max(np.abs(psi_e[keep] - nn_e[keep])
                         / nn_e[keep]))
    check("D1b deep-range Chebyshev envelope kappa = %.6f <= "
          "KAPPA_REF + tol (v770 G1.2 class)" % kap_e,
          kap_e <= core.KAPPA_REF + core.TOL_KAPPA, kill="K2")
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
    check("D2 new-rung census %d (>= %d)"
          % (len(order_kz), MIN_DEEP), len(order_kz) >= MIN_DEEP,
          kill="K1")
    if KILLS:
        return finish({})
    if SMOKE:
        order_kz = order_kz[:4]
    grams = []
    for kz in order_kz:
        g = deep.ext_gram(kz)
        if isinstance(g, dict) and g.get("core_ok"):
            grams.append(g)
        print("    deep gram kz %3d: %s  [%.1f s]"
              % (kz, "ok" if isinstance(g, dict)
             and g.get("core_ok") else "unusable",
             time.time() - T0), flush=True)
    grams.sort(key=lambda g: (g["h"], g["kz"]))
    dsteps = []
    for g1, g2 in zip(grams, grams[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        st = wedge.wedge_step(g1, g2)
        if st is not None:
            st["g2"] = g2
            dsteps.append(st)
    print("    %d deep steps (h %s..%s)"
          % (len(dsteps),
             dsteps[0]["h"] if dsteps else "-",
             dsteps[-1]["h"] if dsteps else "-"))
    d_e3 = d_i2 = d_hsep = 0
    d_a, d_b, d_narch = [], [], []
    d_tier = dict(env=0, lag=0, meas=0)
    d_a0env, d_rat, d_chi, d_h = [], [], [], []
    d_i1 = float("inf")
    d_cs = 0.0
    for st in dsteps:
        g2 = st["g2"]
        kz = g2["kz"]
        alpha, Mz, hz, ka = deep.ext_frame(kz)
        uu = deep.EXT["U"][:ka]
        mm = deep.EXT["MU"][:ka]
        c_at, D = core.atom_lags_at(alpha, Mz, uu, mm)
        c_ar = np.asarray(core.arch_lags(Mz, D), float)
        cd = chain_data(alpha, Mz, uu, mm, c_ar)
        d_e3 += (cd["M_at"] <= cd["m_up"]
                 and cd["M_at"] >= cd["m_lo"])
        d_i2 += (cd["delta_meas"] <= cd["delta_lag"] + 1e-12
                 and cd["delta_lag"] <= cd["delta_env"] + 1e-12)
        vals, narch, _m0up = tier_floors(cd)
        d_narch.append(narch)
        for tag in ("env", "lag", "meas"):
            if vals[tag] > 0.0:
                d_tier[tag] += 1
        d_a0env.append(vals["env"])
        Gc = st["Gc"]
        m0 = g2["chain"][2]
        a, b, kdiag, ratio = measured_h1h2(Gc, g2["v_core"], m0)
        d_a.append(a)
        d_b.append(b)
        d_rat.append(ratio)
        d_chi.append(float(np.max(np.diag(Gc))))
        d_h.append(float(st["h"]))
        d_i1 = min(d_i1, float(np.min(kdiag)) * m0)
        d_cs = max(d_cs, b / max(cs_bound(Gc), 1e-300))
        hsep_m = hsep_of(g2["y_core"], g2["h"])
        d_hsep += abs(hsep_m - float(g2["h"]) / (Mz - 1.0)) \
            <= HSEP_WARD
        print("    deep kz %-4d h %-5d a %+.4f b %+.4f narch %d "
              "a0_env %+.3g  [%.1f s]"
              % (kz, g2["h"], a, b, narch, vals["env"],
                 time.time() - T0), flush=True)
    n_d = len(dsteps)
    check("D3 deep E3 mass laws %d/%d, I2 chain %d/%d, I1 floor "
          "min %.9f, J1 worst %.3f"
          % (d_e3, n_d, d_i2, n_d, d_i1, d_cs),
          d_e3 == n_d and d_i2 == n_d and d_i1 >= 1.0 - I1_TOL
          and d_cs <= 1.0 + CS_TOL, kill="K2")
    check("D4 deep MZ identity h_sep == M/(2M-2) on %d/%d"
          % (d_hsep, n_d), d_hsep == n_d, kill="K2")
    dlab = ("DEEP(a med %.4f, b med %.4f, narch med %d, tiers "
            "env/lag/meas %d/%d/%d of %d)"
            % (float(np.median(d_a)) if d_a else float("nan"),
               float(np.median(d_b)) if d_b else float("nan"),
               int(np.median(d_narch)) if d_narch else -1,
               d_tier["env"], d_tier["lag"], d_tier["meas"], n_d))
    check("D5 typed: %s" % dlab, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world fires/refuses" % kind, fired, detail,
              kill="K2")
    rsc = base.gram_anatomy(base.CTRL_KZ, scramble_seed=1,
                            keep_chain=True)
    c3_msg = "scramble core dead -> disclosed skip"
    c3_ok = True
    if isinstance(rsc, dict) and rsc.get("core_ok"):
        rr9 = base.window_of(base.CTRL_KZ)
        rr9s = base.window_of(base.CTRL_KZ, scramble_seed=1)
        mm9 = 2.0 * rr9["lam"]
        cdt = chain_data(rr9["alpha"], rr9["M"], rr9["uu"], mm9,
                         rr9["c_ar"])
        cds = chain_data(rr9s["alpha"], rr9s["M"], rr9s["uu"],
                         2.0 * rr9s["lam"], rr9s["c_ar"])
        moves = [abs(a["d"] - s["d"]) / max(abs(a["d"]), 1e-300)
                 for a, s in zip(cdt["core"], cds["core"])]
        med_mv = float(np.median(moves))
        c3_ok = med_mv >= MOVE_BAR
        c3_msg = "med rel core-fold move %.3f >= %.2f" % (med_mv,
                                                          MOVE_BAR)
    check("C3 scramble core-fold density movement: %s" % c3_msg,
          c3_ok, kill="K2")

    # ---------------------------------------------------- screens
    section("S -- mandatory tau screens")
    scr_a, _ = parent.screen(a_all, taus1)
    scr_ab, _ = parent.screen(a_all - b_all, taus1)
    scr_rt, _ = parent.screen(rat, taus1)
    print("    TAU-SCREEN a        %s" % scr_a)
    print("    TAU-SCREEN a-b      %s" % scr_ab)
    print("    TAU-SCREEN v/m0     %s" % scr_rt)
    check("S screens recorded", True)

    # ---------------------------------------------------- verdict
    all_h = np.concatenate([hs, np.array(d_h)]) if d_h else hs
    a0_comb = np.concatenate([a0e, np.array(d_a0env)]) \
        if d_a0env else a0e
    n_all = len(a0_comb)
    n_env = int(np.sum(a0_comb > 0.0))
    if n_env == n_all:
        pos = a0_comb > 0
        sl_e, _r2e = parent.ols_line(np.log(all_h[pos]),
                                     np.log(a0_comb[pos]))
        flat = np.isfinite(sl_e) and abs(sl_e) <= HTREND_FLAT
    else:
        flat = False
    n_lag = tier_pos["lag"] + d_tier["lag"]
    n_meas = tier_pos["meas"] + d_tier["meas"]
    narch_all = narch_list + d_narch
    arch_full = all(x == 8 for x in narch_all)
    de_med = float(np.median(de))
    dl_med = float(np.median(dl))
    dm_med = float(np.median(dm))
    if n_env == n_all and flat:
        h1 = "H1-DERIVED(min a0_env %.3g)" % float(np.min(a0_comb))
    elif n_lag == n_all:
        h1 = ("H1-SLACK-FAILS(I2-envelope; env/lag med %.1f dex; "
              "fix: sharper global L1->Linf density law)"
              % math.log10(de_med / max(dl_med, 1e-300)))
    elif n_meas == n_all:
        h1 = ("H1-SLACK-FAILS(I2-lag; lag/meas med %.1f dex; fix: "
              "FFT-level cancellation law, discrepancy class)"
              % math.log10(dl_med / max(dm_med, 1e-300)))
    elif arch_full:
        h1 = "H1-SLACK-FAILS(I3-arch-magnitude)"
    else:
        h1 = ("H1-SLACK-FAILS(I3-lowfreq-magnitude: narch med %d/8 "
              "-- the arch carries the core-fold SIGN but the comb "
              "carries the magnitude (atom share med %.2f); the "
              "core-fold density values are low-frequency prime "
              "partial sums; fix: a localized bound on the comb "
              "density at the first folds -- short-interval/"
              "low-frequency prime discrepancy, NOT an envelope)"
              % (int(np.median(narch_all)),
                 float(np.median(atom_share))))
    b_ge_a = int(np.sum(b_all >= a_all)) + int(np.sum(
        np.array(d_b) >= np.array(d_a))) if d_a else int(
        np.sum(b_all >= a_all))
    if cs_worst > 1.0 + CS_TOL:
        h2 = "H2-SLACK-FAILS(J1-violated)"
    elif b_ge_a > 0:
        h2 = "H2-SLACK-FAILS(B-GE-A on %d steps)" % b_ge_a
    else:
        h2 = ("H2-SLACK-FAILS(J2-no-global-closure; missing: local "
              "CD decay/upper-Christoffel law at separation 1/2; "
              "chi med %.3f flat %+.3f, nn-share med %.3f)"
              % (float(np.median(chi)), sl_c,
                 float(np.median(nnsh))))
    mz = ("MZ-CLOSED-BY-CONVENTION(h_sep == M/(2M-2) -> 1/2, "
          "ward %d/%d + deep %d/%d; MZ >> 1 regime unreachable)"
          % (len(rows), len(rows), d_hsep, n_d))
    if h1.startswith("H1-DERIVED") and h2.startswith("H2-DERIVED"):
        head = ("W1-ALLH-CANDIDATE(c1 explicit; gaps named: none "
                "in the frozen input set; W2 remains RH-hard)")
    else:
        head = ("W1-ALLH-BLOCKED(H1: %s; H2: %s)"
                % (h1.split("(")[0], h2.split("(")[0]))
    check("V1 typed: %s" % h1, True)
    check("V2 typed: %s" % h2, True)
    check("V3 typed: %s" % mz, True)
    labels = dict(h1=h1, h2=h2, mz=mz, seat=seat, head=head)
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
