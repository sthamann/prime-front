#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w1_christoffel_floor_probe -- PRIME.PORT.W1.FLOOR.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS.  wedge_scale_law_probe (CLXXIV, SPEC-SHA
26855819..) froze the two-lemma wedge shape [W1] s_P >= c1 mu1 +
[W2] s >= c2 s_P and measured: s_P is h-FLAT O(1), SATURATES to
1.00000 on all 27 deep steps, and is CHRISTOFFEL-FORM-ONLY -- the
exact identity s_P = 1/(v0* G_core^{-1} v0) holds to 5.6e-16 but no
single node carries it.  The upper half s_P <= 1 - tau is classical
given the wall (G_core is a principal submatrix of the wall Gram).
THE OPEN HALF IS THE LOWER BOUND: s_P >= c1 > 0 uniformly in h.
This probe is the THEOREM-ENGINEERING attempt on that half: make
the object explicit as the prescribed-node Christoffel functional
of the positive folded measure, name the saturation mechanism,
and attempt the floor in increasing strength -- per-rung EXACT
certificates, per-rung INTERVAL-ENCLOSED certificates (ideal
objects, frozen-frame convention), and the exact CLASSICAL
statement whose hypotheses are measurable properties of nu_+.

(a) THE OBJECT MADE EXPLICIT.  Per step (r1, r2): nu_+ / nu_- are
the +/- parts of the folded grid density of the rung's lag vector;
the orthonormal chain p_0..p_{h-1} is Lanczos on nu_+; the 8 core
nodes y_i (folds CORE_J of the NEGATIVE arm) carry masses v_i;
H = [sqrt(v_i) p_k(y_i)] is 8 x h and G_core = H H* =
[sqrt(v_i v_j) K_h(y_i, y_j)] is the weighted CD-kernel Gram of
nu_+ at the core nodes.  v0 = Q e0 is the frozen backward frame
direction (ground eigenvector of r1's core Schur complement --
r1-wall data, NEVER r2 target data).  The CLASSICAL VARIATIONAL
PRINCIPLE (prescribed-node Christoffel functional):

    v0* G_core^{-1} v0
      = min { ||p||^2_{nu+} : deg p < h,
              sqrt(v_i) p(y_i) = (v0)_i, i = 1..8 },

with minimizer p* = sum_k c*_k p_k, c* = H* G_core^{-1} v0, so
s_P = 1/||c*||^2.  Verified numerically PER STEP by three wards:
feasibility ||H c* - v0||_inf <= FEAS_WARD, the energy identity
|s_P ||c*||^2 - 1| <= VAR_WARD, and null-space optimality
|<c*, z>| <= ORTH_WARD for a deterministic feasible-perturbation
direction z (H z = 0) -- plus the two CLXXIV routes (inverse-Gram
INV_WARD, min-norm lstsq LSTSQ_WARD).  KEY REDUCTION (exact
algebra, stated first): inf over UNIT v0 of s_P equals
lambda_min(G_core) -- so the v0-UNIFORM floor statement is
FRAME-FREE: a floor on lambda_min(G_core) implies W1's lower half
for every frame direction, and the frozen v0 drops out of the
lemma entirely.

(b) WHY IT SATURATES (typed, never kill).  Chain (classical given
the wall, warded numerically): s_P <= R <= 1 - tau_2 with
R = v0* G_core v0 (Cauchy-Schwarz + principal-submatrix bound).
Ladders on surface + deep: 1 - s_P; (1 - s_P)/tau_2; (1 - s_P)/mu1;
alignment t_align = cos^2(c*, H* v0) (minimizer == pullback of the
constraint direction iff -> 1); top-eigenvector overlap
(v0 . u_max)^2; lambda_min/max(G_core).  CORRECTION LAW: OLS of
log(1 - s_P) against log h / log tau_2 / log mu1 (combined
surface + deep); typed CORRECTION-LAW(argmax-R^2 name, slope, R2).
Declared candidate mechanism: v0 aligns with a lambda ~ 1 - tau
eigendirection of G_core so the minimizer trivializes and
1 - s_P tracks tau, not mu1 -- decided by the measured R^2 table
and the (1 - s_P)/tau_2 band.

(c) THE FLOOR, in increasing strength:
 F1 EXACT-RATIONAL CENSUS (per step, float-entry level declared,
    v897/round-62 decision class): pd_exact(G_core) (8x8 Sylvester
    LDL in Fractions), exact solve x = G_core^{-1} v0, exact
    q = v0.x, certified c1_step = 1/q; ward |1/q - s_P|/s_P <=
    EXACT_WARD; the BORDERED form [[t, v0*],[v0, G_core]] is
    re-decided PD at t = q (1 + 2^-30) as the Rayleigh-type
    certificate (a transcription ward -- Schur equivalence).
    Same census on every deep step (float-entry level declared).
 F2 THE CLASSICAL ROUTE (v0-uniform): the round-62 G-battery
    best_cert = max(Gershgorin, scaled, Cassini) on G_core, plus
    the raw split a = min_i G_ii, b = max_i off-row-sum, margin;
    s_P >= lambda_min(G_core) >= best_cert verified (counts).
    Census best_cert > 0 on surface AND deep; h-trend of
    log best_cert (combined) with flatness bar HTREND_FLAT.
 F3 THE HYPOTHESES OF THE UNIFORM STATEMENT, measured:
    [W1-STATEMENT] if (H1) min_i v_i K_h(y_i, y_i) >= a0 > 0
    uniformly (weight-vs-Christoffel floor -- exactly the Radau
    finding's w*/lam_h ~ 1 object) and (H2) max_i sum_{j != i}
    sqrt(v_i v_j) |K_h(y_i, y_j)| <= b0 < a0 uniformly (CD-kernel
    off-diagonal decay at separated nodes), then G_core >=
    (a0 - b0) I and s_P >= a0 - b0 for EVERY unit v0.  Classical
    pedigree of H1/H2 at edge-scaled nodes: Mate-Nevai-Totik /
    Lubinsky-class Christoffel + CD-kernel asymptotics under local
    doubling at the edge.  Measured per rung: a, b, a - b bands +
    h-trends; node separation h_sep = min |dtheta| h/(2 pi) (MZ
    regime wants >> 1 -- round-62 measured ~0.5, printed honestly);
    edge-doubling ratios of nu_+ at dyadic scales (band + per-scale
    trend; Szego condition declared UNMEASURABLE at grid scale --
    doubling is the proxy).  Which hypotheses hold numerically and
    which are open is REPORTED, never adjusted.
 F4 INTERVAL-ENCLOSED CERTIFICATES (ideal objects; the
    pg_chain_interval_rollout machinery is imported READ-ONLY):
    on the IVAL_N shallowest steps (budget IVAL_BUDGET_S, honest
    SKIPPED-BUDGET), the enclosed core CD-Gram [Gccm +- Gccr] (+
    one-sided PSD remainder, worst case Loewner-DOWN, allowance
    dn = max row sum of Gccr): exact-rational PD of Gccm - dn I,
    exact q_ub = v0*(Gccm - dn I)^{-1} v0, certified
    c1_iv = 1/q_ub <= s_P(every member incl. the ideal object);
    bordered re-decision at t = q_ub (1 + 2^-30); ladder
    (dps 40, std) -> (dps 40, hi) on REFUSED-WIDTH.  Soundness
    ward: c1_iv <= float s_P.  Frozen-frame convention (Q, v0,
    tau) exactly as the ival probe declares.

(d) GATES.  TAU-SCREENS (parent bands PASS |s| <= 0.30 / RELOC >=
0.70): s_P and best_cert against tau.  ANTI-CIRCULARITY TYPING
(first-class, decisive for the architecture): nu_+ is the positive
part of the folded density of arch lags (comb-free transcendental
layer) PLUS the von-Mangoldt tent atoms -- nu_+ CONTAINS COMB
DATA.  The W1 statement itself is classical (positive measure +
H1/H2 => floor); the comb enters ONLY through whether nu_+
satisfies the measured hypotheses.  The C1b SMOOTH BATTERY decides
the typing: the identical classical battery on the comb-free
smooth world's G_core -- if it certifies there too, the floor
MECHANISM is measure-generic classical algebra (consistent with
CLXXIV's W2-CARRIES-WALL: the wall lives in s, not s_P); typed
W1-MECHANISM-CLASSICAL(n/N) iff all usable smooth rungs certify,
else W1-MECHANISM-PARTIAL(n/N).  CONTROLS (kill if silent): C1
smooth world refuses the certificate ladder, C2 Epstein + scramble
fire (parent verbatim); C3 CONSTRUCTION SENSITIVITY (kill): the
weight-reversal control (v -> reversed v on the same nodes/kernel)
must move s_P: median |log(s_P'/s_P)| >= MOVE_BAR; C3b typed: the
false-chain control (r1's chain at r2's nodes) movement recorded.

VERDICT (frozen enum, decided by the rules below and nothing else):
  W1-THEOREM-CANDIDATE iff F1 exact census 39/39 AND deep exact
    census all/all AND F2 classical battery > 0 on 39/39 surface
    AND all deep steps AND C1b smooth battery all/all usable AND
    F4 attempted >= 1 with ALL attempted CERTIFIED AND the
    combined h-trend |slope| of log best_cert <= HTREND_FLAT AND
    neither tau-screen is RELOC -- every remaining gap NAMED
    (all-h proof of H1/H2 for this nu_+, interval coverage beyond
    the subset, deep float level, frozen-frame convention).
  else W1-CERTIFIED-SURFACE(missing legs) iff F1 39/39;
  else W1-MEASURED-ONLY(named).
DEAD overrides (kill-level anyway): CLXXIV reproduction s_P >= mu1
fails anywhere, or any variational ward breaks.

FROZEN BARS: INV_WARD = 1e-9; LSTSQ_WARD = 1e-6; FEAS_WARD =
1e-10; VAR_WARD = 1e-10; ORTH_WARD = 1e-8; EXACT_WARD = 1e-9;
CHAIN_TOL = 1e-12; HTREND_FLAT = 0.30; SLOPE bands 0.30/0.70
(parent verbatim); MOVE_BAR = 0.05; IVAL_N = 3 shallowest steps;
IVAL_LADDER = ((40, std), (40, hi)); IVAL_BUDGET_S = 420;
MIN_DEEP = 10; DOUBLE_SCALES: dyadic t = 2^-k, k = 1..6, plus the
core-window anchor t_core = 1 - min(y_core) at x2 multipliers
{1, 2, 4}; N_SEATS = 5; parent bars (MINB_REF 0.679, GAP
0.052/0.888, rtol as parent) inherited verbatim; parent SPEC-SHA
warded == 084c9689..; wedge SPEC-SHA prefix warded == 26855819;
ival SPEC-SHA prefix warded == eb68b6ed.  Runtime cap declared:
20 min.  Smoke mode W1FLOOR_SMOKE=1 restricts the deep block to
the 4 shallowest new rungs and the interval block to 2 steps
(surface + controls always full); any smoke run is disclosed here
before the freeze.

ANTI-CIRCULARITY (frozen): every construction consumes ONLY r2's
positive-chain CD data (chain, core nodes, core masses) and the
backward r1 Householder frame; no sigma_h, no forward pivot sign,
no target eigendata of r2 anywhere; mu1 is parity geometry; the
exact-rational LDL / exact solve is the declared v897 decision
class (certificate, not construction); float eigensolves appear
only as measured anatomy next to the certificates.  The interval
branch inherits the ival probe's frozen-frame declaration
verbatim (Q, tau, v0 = frozen exact-rational constants of the
STATEMENT; enclosure covers lags -> density -> folded measures ->
CD-Gram).

ANTHROPIC NO-GO DECLARATION: inputs are the full degree-(h-1)
positive CD evaluation matrix, an 8x8 kernel Gram, its exact
inverse data and interval enclosure -- strictly beyond two scalar
moments plus bandwidth-1 pair correlation; no contradiction with
the two-moment no-go.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(W1FLOOR_SMOKE=1, 34/34 on the FIRST passage, 8.1 s; deep block on
the 4 shallowest new rungs -> 3 deep steps; interval block on 2
steps).  NO bar, band, count, rule or enum was moved after it; the
only post-smoke change is this disclosure block itself.  Measured
smoke context the frozen run must confirm: W green (42/41/39, minB
0.6790, gap 0.0520/0.8875, s_P >= mu1 39/39, half-gap 39/39); A
wards inv 1.2e-15, lstsq 4.8e-15, feas 5.6e-16, energy 1.6e-15,
orth 3.9e-16 -- the variational principle is EXACT on every step;
B chain census s_P <= R <= 1 - tau_2 on 39/39; 1 - s_P band
8.98e-7..4.30e-4 (med 1.90e-5); (1-s_P)/tau_2 band 1.097/7.43/277
(the classical lower bound (1-s_P)/tau_2 >= 1 is nearly SHARP at
the minimum but spreads two decades -- the saturation gap is NOT
literally tau); t_align med 0.99999831, top-overlap med 0.9887 --
the minimizer trivializes to the pullback of the constraint
direction; smoke CORRECTION-LAW(log tau_2, slope +0.461, R2 0.379)
beats mu1/h (R2 0.248 both) but is WEAK -- no clean law, recorded
honestly; F1 exact census 39/39 with min c1 = 0.999570 (== float
s_P to 1.1e-15), bordered re-decision 39/39; F2 battery best_cert
> 0 on 39/39, min/med/max +0.4362/+0.7678/+0.9266, a - b med
+0.767 (a med 0.968, b med 0.202), order s_P >= lam_min >=
best_cert 39/39; F3 h_sep med 0.501 (MZ honest risk stands),
dyadic doubling bands ~3.0..5.2 med ~3.4 at t = 2^-1..2^-4
(h-trends -0.04..-0.13, widening at 2^-5/2^-6: 1.2..18.2),
core-anchor x1 band 1.14/1.44/1.70 trend -0.012 -- doubling
BOUNDED AND FLAT at the core scales; F4 2/2 CERTIFIED at
(40, std): c1_iv 0.999966/0.999570, survival 1.000000, dn
2.9e-9/2.1e-9, lag wards <= 1.3e-14 (3-4 s per step); D fidelity
byte-exact, census 28, smoke deep steps 3/3: exact 3/3 (min c1
0.999988), battery 3/3 (best +0.91..+0.95 -- the deep battery is
STRONGER than the surface), margin 3/3; combined best_cert h-trend
+0.192 (R2 0.448) inside the 0.30 bar; C1 smooth refuses
(refused 42, usable-core-PD 0), Epstein/scramble fire; C1b THE
DECISIVE SMOKE SURPRISE: the smooth battery certifies only 26/37
usable smooth rungs (best_cert min -58.0, a-b min -80.4) -- the
classical certificate is NOT measure-generic, the comb-built nu_+
is BETTER conditioned than the smooth world at 11/37 rungs; under
the frozen enum this pins the smoke verdict at
W1-CERTIFIED-SURFACE(missing: smooth-battery), NOT
theorem-candidate -- the rule is kept exactly as frozen, no
post-smoke upgrade; C3 weight-reversal fires med |dlog s_P| =
0.3488 >= 0.05 (min 0.0595, max 0.6383, n = 39), false-chain med
0.7476 (max 2.75) recorded; screens s_P PASS(-0.000, R2 0.028),
best_cert PASS(-0.050, R2 0.290).  The frozen run repeats this on
the FULL deep block (27 expected steps) and IVAL_N = 3; the enums
move only as the full data says.

NO RH claim.  Even a full THEOREM-CANDIDATE verdict is a
finite-surface + finite-holdout certification with a named
classical route: the all-h proof of H1/H2 for the actual folded
measure (comb-built data) is OPEN; W1 alone does not touch W2 or
the wall.  No marker moves.  Stdout only.
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import wedge_scale_law_probe as wedge  # noqa: E402  (READ-ONLY)
import pg_chain_interval_rollout_probe as ival  # noqa: E402 (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
WEDGE_SHA8 = "26855819"
IVAL_SHA8 = "eb68b6ed"
INV_WARD = 1.0e-9
LSTSQ_WARD = 1.0e-6
FEAS_WARD = 1.0e-10
VAR_WARD = 1.0e-10
ORTH_WARD = 1.0e-8
EXACT_WARD = 1.0e-9
CHAIN_TOL = 1.0e-12
HTREND_FLAT = 0.30
MOVE_BAR = 0.05
IVAL_N = 3
IVAL_LADDER = ((40, "std"), (40, "hi"))
IVAL_BUDGET_S = 420.0
MIN_DEEP = 10
N_SEATS = 5
SMOKE = os.environ.get("W1FLOOR_SMOKE", "") == "1"
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


def solve_fr(Afr, bfr):
    """Exact Fraction Gaussian elimination solve (small systems)."""
    n = len(Afr)
    A = [Afr[i][:] + [bfr[i]] for i in range(n)]
    for k in range(n):
        piv = None
        for i in range(k, n):
            if A[i][k] != 0:
                piv = i
                break
        if piv is None:
            return None
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            if f:
                for j in range(k, n + 1):
                    A[i][j] = A[i][j] - f * A[k][j]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        s = A[i][n]
        for j in range(i + 1, n):
            s = s - A[i][j] * x[j]
        x[i] = s / A[i][i]
    return x


def bordered_pd(t, v0fr, Gfr):
    """Exact PD decision of [[t, v0*],[v0, G]] (9x9 Sylvester)."""
    n = len(Gfr)
    W = [[Fraction(0)] * (n + 1) for _ in range(n + 1)]
    W[0][0] = Fraction(t)
    for i in range(n):
        W[0][i + 1] = v0fr[i]
        W[i + 1][0] = v0fr[i]
        for j in range(n):
            W[i + 1][j + 1] = Gfr[i][j]
    ok, _ = base.pd_exact(W)
    return ok


def exact_floor(Gc, v0):
    """Exact-rational floor certificate on float-entry G_core:
    (pd, q, c1) with q = v0* G^{-1} v0 exact, c1 = 1/q; plus the
    bordered Rayleigh re-decision at t = q (1 + 2^-30)."""
    Gfr = base.mat_fr(np.asarray(Gc, float))
    ok, _ = base.pd_exact(Gfr)
    if not ok:
        return dict(pd=False, q=None, c1=None, bord=False)
    v0fr = [Fraction(float(x)) for x in v0]
    x = solve_fr(Gfr, v0fr)
    q = sum(a * b for a, b in zip(v0fr, x))
    bord = bordered_pd(q * (1 + Fraction(1, 2 ** 30)), v0fr, Gfr)
    return dict(pd=True, q=q, c1=1 / q, bord=bord)


def gc_of_row(w):
    """G_core = H H* (8x8 weighted CD-kernel Gram, unrotated)."""
    Gc = w["H"] @ w["H"].T
    return 0.5 * (Gc + Gc.T)


def battery(Gc):
    """The round-62 classical battery + raw diagonal split."""
    a = float(np.min(np.diag(Gc)))
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    b = float(np.max(off))
    return dict(best=base.best_cert(Gc), gersh=base.gersh_min(Gc),
                a=a, b=b, margin=a - b,
                lmin=float(np.linalg.eigvalsh(Gc)[0]),
                lmax=float(np.linalg.eigvalsh(Gc)[-1]))


def h_sep_of(y_core, h):
    th = np.arccos(np.clip(y_core, -1.0, 1.0))
    dth = np.abs(th[:, None] - th[None, :])
    np.fill_diagonal(dth, np.inf)
    return float(np.min(dth)) * h / (2.0 * math.pi)


def positive_measure_of(kz):
    """nu_+ (xs, ws) of one truth rung -- gram_anatomy pipeline
    head verbatim (READ-ONLY reuse of the base machinery)."""
    rr = base.window_of(kz)
    mm = 2.0 * rr["lam"]
    c_at, _ = core.atom_lags_at(rr["alpha"], rr["M"], rr["uu"], mm)
    d = base.grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * rr["M"] - 2
    xs, ws, _ = base.folded_measure(d, L, +1.0)
    return xs, ws


def doubling_ratios(xs, ws, scales):
    """nu_+([1-2t, 1]) / nu_+([1-t, 1]) per scale (None if the
    denominator is empty -- vacuous, skipped honestly)."""
    out = []
    for t in scales:
        lo = np.sum(ws[xs >= 1.0 - t])
        hi = np.sum(ws[xs >= 1.0 - 2.0 * t])
        out.append(float(hi / lo) if lo > 0.0 else None)
    return out


def sp_of(Gc, v0):
    """Float s_P = 1/(v0* G^{-1} v0); None if G not float-PD."""
    if float(np.linalg.eigvalsh(Gc)[0]) <= 0.0:
        return None
    return 1.0 / float(v0 @ np.linalg.solve(Gc, v0))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("W1FLOOR-MEASURED / %s / %s / %s / %s / %s"
                   % (labels.get("b", "-"), labels.get("f", "-"),
                      labels.get("m", "-"), labels.get("d", "-"),
                      labels.get("head", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every exact certificate is a statement about the
  float64-computed step matrices (v897 float-entry caveat); every
  interval certificate covers the IDEAL objects in the declared
  frozen frame, on the attempted subset only.  The classical route
  is Gershgorin-class given H1/H2; the all-h proof of H1/H2 for
  the actual folded measure is OPEN and nu_+ contains comb data by
  construction.  A THEOREM-CANDIDATE names its gaps; nothing here
  is promoted.  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W1.FLOOR.01 -- the 8-node Christoffel "
            "functional of nu_+: variational identity, saturation "
            "mechanism, floor certificates (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    wedge_sha = hashlib.sha256(
        wedge.__doc__.encode("utf-8")).hexdigest()
    ival_sha = hashlib.sha256(
        ival.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    wedge  SPEC SHA-256 = %s" % wedge_sha)
    print("    ival   SPEC SHA-256 = %s" % ival_sha)
    print("    NO RH claim.  Exact decisions are float-entry level "
          "(declared); interval branch covers ideal objects.")
    if SMOKE:
        print("    *** SMOKE MODE: deep on 4 shallowest new rungs, "
              "interval on 2 steps ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c wedge SPEC prefix reproduced",
          wedge_sha[:8] == WEDGE_SHA8, wedge_sha[:8], kill="K2")
    check("S0d ival SPEC prefix reproduced",
          ival_sha[:8] == IVAL_SHA8, ival_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder + CLXXIV reproduction")
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
    n_hg = sum(w["gap"] >= 0.5 * w["mu1"] for w in rows)
    check("W4 registered half-gap s >= mu1/2 (measurement)",
          n_hg == len(rows), "%d/%d" % (n_hg, len(rows)), kill="K2")

    hs = np.array([float(w["r2"]["h"]) for w in rows])
    taus1 = np.array([w["tau"] for w in rows])
    tau2s = np.array([float(w["r2"]["tau"]) for w in rows])
    sP = np.array([w["sP"] for w in rows])
    mu = np.array([w["mu1"] for w in rows])

    # ------------------------------------------------------------ A
    section("A -- the variational identification (prescribed-node "
            "Christoffel functional of nu_+)")
    print("    v0 = Q e0 = ground eigenvector of r1's core Schur "
          "complement (r1-wall frame data, never r2 target data);")
    print("    s_P = 1 / min{ ||p||^2_{nu+} : deg p < h, "
          "sqrt(v_i) p(y_i) = (v0)_i } -- and inf over unit v0 of "
          "s_P == lambda_min(G_core): the FLOOR is frame-free.")
    inv_dev = ls_dev = feas_dev = var_dev = orth_dev = 0.0
    for w in rows:
        v0 = w["Q"][:, 0]
        Gc = gc_of_row(w)
        w["Gc"] = Gc
        w["v0"] = v0
        s_inv = sp_of(Gc, v0)
        inv_dev = max(inv_dev, abs(s_inv - w["sP"]) / abs(w["sP"]))
        g = np.linalg.lstsq(w["H"], v0, rcond=None)[0]
        ls_dev = max(ls_dev,
                     abs(1.0 / float(g @ g) - w["sP"]) / abs(w["sP"]))
        cstar = w["H"].T @ np.linalg.solve(Gc, v0)
        w["cstar"] = cstar
        feas_dev = max(feas_dev,
                       float(np.max(np.abs(w["H"] @ cstar - v0))))
        var_dev = max(var_dev,
                      abs(w["sP"] * float(cstar @ cstar) - 1.0))
        h = w["H"].shape[1]
        z0 = np.where(np.arange(h) % 2 == 0, 1.0, -1.0) / math.sqrt(h)
        z = z0 - w["H"].T @ np.linalg.solve(Gc, w["H"] @ z0)
        orth_dev = max(orth_dev,
                       abs(float(cstar @ z))
                       / (float(np.linalg.norm(cstar))
                          * max(float(np.linalg.norm(z)), 1e-300)))
    check("A1 inverse-Gram identity s_P == 1/(v0* G^{-1} v0)",
          inv_dev <= INV_WARD, "max rel dev %.2e" % inv_dev,
          kill="K2")
    check("A2 min-norm lstsq route", ls_dev <= LSTSQ_WARD,
          "max rel dev %.2e" % ls_dev, kill="K2")
    check("A3 variational principle: feasibility %.2e (<=%.0e), "
          "energy identity %.2e (<=%.0e), null-space optimality "
          "%.2e (<=%.0e)"
          % (feas_dev, FEAS_WARD, var_dev, VAR_WARD, orth_dev,
             ORTH_WARD),
          feas_dev <= FEAS_WARD and var_dev <= VAR_WARD
          and orth_dev <= ORTH_WARD, kill="K2")

    # ------------------------------------------------------------ B
    section("B -- the saturation mechanism (typed)")
    R_arr, tal_arr, otop_arr, lmin_arr, lmax_arr = [], [], [], [], []
    for w in rows:
        Gc, v0, cstar = w["Gc"], w["v0"], w["cstar"]
        R_arr.append(float(v0 @ Gc @ v0))
        c0 = w["H"].T @ v0
        tal_arr.append(float(cstar @ c0) ** 2
                       / (float(cstar @ cstar) * float(c0 @ c0)))
        ev, U = np.linalg.eigh(Gc)
        otop_arr.append(float(v0 @ U[:, -1]) ** 2)
        lmin_arr.append(float(ev[0]))
        lmax_arr.append(float(ev[-1]))
    R_arr = np.array(R_arr)
    n_chain = int(np.sum((sP <= R_arr + CHAIN_TOL)
                         & (R_arr <= 1.0 - tau2s + CHAIN_TOL)))
    check("B1 chain s_P <= v0*Gv0 <= 1 - tau_2 (classical given "
          "the wall)", n_chain == len(rows),
          "%d/%d" % (n_chain, len(rows)), kill="K2")
    one_m = 1.0 - sP
    print("    1 - s_P        min/med/max %.4g / %.4g / %.4g"
          % band(one_m))
    print("    (1-s_P)/tau_2  min/med/max %.6g / %.6g / %.6g"
          % band(one_m / tau2s))
    print("    (1-s_P)/mu1    min/med/max %.4g / %.4g / %.4g"
          % band(one_m / mu))
    print("    t_align        min/med/max %.8f / %.8f / %.8f"
          % band(np.array(tal_arr)))
    print("    top-eig overlap (v0.u_max)^2 min/med/max "
          "%.6f / %.6f / %.6f" % band(np.array(otop_arr)))
    print("    lam_min(G_core) min/med/max %.4f / %.4f / %.4f; "
          "lam_max %.6f / %.6f / %.6f"
          % (band(np.array(lmin_arr)) + band(np.array(lmax_arr))))
    check("B2 saturation ladders recorded", True)

    # ------------------------------------------------------------ F1
    section("F1 -- exact-rational per-step floor census (float-"
            "entry level declared)")
    n_pd = n_bord = 0
    c1_list = []
    ex_dev = 0.0
    for w in rows:
        r = exact_floor(w["Gc"], w["v0"])
        w["exact"] = r
        if r["pd"]:
            n_pd += 1
            c1f = float(r["c1"])
            ex_dev = max(ex_dev, abs(c1f - w["sP"]) / abs(w["sP"]))
            c1_list.append(c1f)
            if r["bord"]:
                n_bord += 1
    check("F1a exact PD + exact q = v0*G^{-1}v0 on every step",
          n_pd == len(rows), "%d/%d" % (n_pd, len(rows)))
    check("F1b exact c1 == float s_P", ex_dev <= EXACT_WARD,
          "max rel dev %.2e" % ex_dev, kill="K2")
    check("F1c bordered Rayleigh re-decision at t = q(1+2^-30)",
          n_bord == n_pd, "%d/%d" % (n_bord, n_pd), kill="K2")
    c1_min = float(np.min(c1_list)) if c1_list else float("nan")
    print("    certified c1 = 1/q: min/med/max %.6f / %.6f / %.6f"
          % band(np.array(c1_list)))

    # ------------------------------------------------------------ F2
    section("F2 -- the classical v0-uniform route (round-62 "
            "G-battery on G_core)")
    bats = [battery(w["Gc"]) for w in rows]
    best = np.array([b_["best"] for b_ in bats])
    gersh = np.array([b_["gersh"] for b_ in bats])
    a_arr = np.array([b_["a"] for b_ in bats])
    b_arr = np.array([b_["b"] for b_ in bats])
    marg = a_arr - b_arr
    lmin_a = np.array([b_["lmin"] for b_ in bats])
    n_best = int(np.sum(best > 0.0))
    n_ge = int(np.sum(gersh > 0.0))
    n_ord = int(np.sum((sP >= lmin_a - CHAIN_TOL)
                       & (lmin_a >= best - CHAIN_TOL)))
    print("    best_cert  min/med/max %+.4f / %+.4f / %+.4f "
          "(> 0 on %d/%d)" % (band(best) + (n_best, len(rows))))
    print("    gersh-plain min/med/max %+.4f / %+.4f / %+.4f "
          "(> 0 on %d/%d)" % (band(gersh) + (n_ge, len(rows))))
    print("    a = min diag min/med/max %.4f / %.4f / %.4f; "
          "b = max offrow %.4f / %.4f / %.4f; a-b med %+.4f"
          % (band(a_arr) + band(b_arr) + (float(np.median(marg)),)))
    print("    order s_P >= lam_min >= best_cert holds %d/%d"
          % (n_ord, len(rows)))
    check("F2 classical battery recorded (census %d/%d)"
          % (n_best, len(rows)), True)

    # ------------------------------------------------------------ F3
    section("F3 -- hypotheses of the uniform statement (measured)")
    print("    [W1-STATEMENT] (H1) min_i v_i K_h(y_i,y_i) >= a0 > 0"
          " uniformly  AND  (H2) max_i sum_{j!=i} sqrt(v_i v_j)"
          "|K_h(y_i,y_j)| <= b0 < a0 uniformly")
    print("      ==> G_core >= (a0-b0) I ==> s_P >= a0-b0 for EVERY"
          " unit v0 (Gershgorin; MNT/Lubinsky-class edge "
          "asymptotics under local doubling would give H1/H2).")
    hsep = np.array([h_sep_of(w["r2"]["y_core"], w["r2"]["h"])
                     for w in rows])
    print("    node separation h_sep min/med/max %.3f / %.3f / %.3f"
          " (MZ regime wants >> 1 -- honest risk)" % band(hsep))
    dy_scales = [2.0 ** (-k) for k in range(1, 7)]
    dy_tab = {k: [] for k in range(len(dy_scales))}
    co_tab = {m: [] for m in range(3)}
    for w in rows:
        xs, ws = positive_measure_of(w["r2"]["kz"])
        for k, r in enumerate(doubling_ratios(xs, ws, dy_scales)):
            if r is not None:
                dy_tab[k].append((w["r2"]["h"], r))
        t_core = 1.0 - float(np.min(w["r2"]["y_core"]))
        co_sc = [min(t_core * (2.0 ** m), 1.0) for m in range(3)]
        for m, r in enumerate(doubling_ratios(xs, ws, co_sc)):
            if r is not None:
                co_tab[m].append((w["r2"]["h"], r))
    for k, t in enumerate(dy_scales):
        pts = dy_tab[k]
        if len(pts) < 3:
            print("    doubling t=2^-%d: vacuous (n=%d)"
                  % (k + 1, len(pts)))
            continue
        rr = np.array([p[1] for p in pts])
        sl, r2f = parent.ols_line(np.log([p[0] for p in pts]),
                                  np.log(rr))
        print("    doubling t=2^-%d: band %.3f/%.3f/%.3f; h-trend "
              "%+.3f (R2 %.2f)" % ((k + 1,) + band(rr) + (sl, r2f)))
    for m in range(3):
        pts = co_tab[m]
        if len(pts) < 3:
            continue
        rr = np.array([p[1] for p in pts])
        sl, r2f = parent.ols_line(np.log([p[0] for p in pts]),
                                  np.log(rr))
        print("    doubling core-anchor x%d: band %.3f/%.3f/%.3f; "
              "h-trend %+.3f (R2 %.2f)"
              % ((2 ** m,) + band(rr) + (sl, r2f)))
    print("    Szego condition: UNMEASURABLE at grid scale "
          "(discrete folded measure) -- doubling is the proxy.")
    sl_a, r2_a = parent.ols_line(np.log(hs), np.log(a_arr))
    mpos = marg > 0
    sl_m, r2_m = (parent.ols_line(np.log(hs[mpos]),
                                  np.log(marg[mpos]))
                  if int(np.sum(mpos)) >= 3 else (float("nan"),) * 2)
    print("    h-trends: log a slope %+.3f (R2 %.3f); log(a-b) "
          "slope %+.3f (R2 %.3f)" % (sl_a, r2_a, sl_m, r2_m))
    check("F3 hypotheses measured (H1/H2 numeric, all-h OPEN)",
          True)

    # ------------------------------------------------------------ F4
    section("F4 -- interval-enclosed certificates (ideal objects, "
            "frozen frame; %d shallowest steps, budget %.0f s)"
            % ((2 if SMOKE else IVAL_N), IVAL_BUDGET_S))
    t_iv = time.time()
    glx, glw, lemma = ival.gl_nodes_enclosed(ival.GL_N)
    ival._GLX, ival._GLW = glx, glw
    check("F4a GL-%d node-enclosure lemma" % ival.GL_N,
          lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains2"], kill="K2")
    order_h = sorted(range(len(rows)),
                     key=lambda i: (rows[i]["r2"]["h"],
                                    rows[i]["r2"]["kz"]))
    n_ival = 2 if SMOKE else IVAL_N
    iv_res = []
    iv_wards = []
    for idx in order_h[:n_ival]:
        w = rows[idx]
        if time.time() - t_iv > IVAL_BUDGET_S:
            iv_res.append(("SKIPPED-BUDGET", w, None, None))
            continue
        rw = ival.gram_anatomy(w["r2"]["kz"], keep_chain=True)
        outcome = ("REFUSED-WIDTH", w, None, None)
        for dps, tier in IVAL_LADDER:
            enc = ival.enclose_rung(rw, "truth", dps, tier)
            if enc.get("ward") is not None:
                iv_wards.append(enc["ward"])
            if not enc["ok"]:
                outcome = ("REFUSED-WIDTH(%s)" % enc["seat"], w,
                           None, None)
                continue
            dn = ival.rowsum_ub(enc["Gccr"])
            Gfr = ival.shifted_fr(enc["Gccm"], dn)
            okg, _ = base.pd_exact(Gfr)
            if not okg:
                okmid, _ = base.pd_exact(base.mat_fr(enc["Gccm"]))
                outcome = (("REFUSED-WIDTH(PG)" if okmid
                            else "FAILED(PG)"), w, None, None)
                continue
            v0fr = [Fraction(float(x)) for x in w["v0"]]
            x = solve_fr(Gfr, v0fr)
            q_ub = sum(aa * bb for aa, bb in zip(v0fr, x))
            bord = bordered_pd(q_ub * (1 + Fraction(1, 2 ** 30)),
                               v0fr, Gfr)
            c1_iv = 1 / q_ub
            outcome = ("CERTIFIED" if bord else "FAILED(BORD)",
                       w, float(c1_iv), dn)
            break
        iv_res.append(outcome)
        enum, w_, c1v, dnv = outcome
        print("    kz %-3d h %-4d %-22s%s  [%.0f s]"
              % (w_["r2"]["kz"], w_["r2"]["h"], enum,
                 ("  c1_iv %.6f (float s_P %.6f, survival %.6f, "
                  "dn %.1e)" % (c1v, w_["sP"], c1v / w_["sP"], dnv))
                 if c1v is not None else "",
                 time.time() - T0), flush=True)
    n_att = sum(1 for e, *_r in iv_res if e != "SKIPPED-BUDGET")
    n_ivc = sum(1 for e, *_r in iv_res if e == "CERTIFIED")
    sound = all(c1v <= w_["sP"] * (1.0 + 1e-12)
                for e, w_, c1v, _d in iv_res if e == "CERTIFIED")
    check("F4b interval lag wards <= %.0e on enclosed rungs"
          % ival.WARD_REL,
          bool(iv_wards) and max(iv_wards) <= ival.WARD_REL,
          "max %.2e" % (max(iv_wards) if iv_wards else 0.0),
          kill="K2")
    check("F4c soundness c1_iv <= float s_P on every certificate",
          sound, kill="K2")
    check("F4d typed: IVAL(%d/%d certified)" % (n_ivc, n_att), True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, float level declared)")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(deep.EXT["NN"][:nP], core._NN)
               and np.array_equal(deep.EXT["U"][:nP], core.U_ALL)
               and np.array_equal(deep.EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(deep.EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    check("D1 deep-table fidelity: overlap dev %.1e == 0.0, "
          "prefixes bitwise" % dev, dev == 0.0 and ok_pref,
          kill="K2")
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
        tag = ("chain-short" if g is None else
               "core-missing" if not g["core_ok"] else "ok")
        print("    deep gram kz %3d: %s  [%.1f s]"
              % (kz, tag, time.time() - T0), flush=True)
        if isinstance(g, dict) and g.get("core_ok"):
            grams.append(g)
    grams.sort(key=lambda g: (g["h"], g["kz"]))
    dsteps = []
    for g1, g2 in zip(grams, grams[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        st = wedge.wedge_step(g1, g2)
        if st is not None:
            st["tau2"] = float(g2["tau"])
            dsteps.append(st)
    print("    %d deep steps (h %s..%s)"
          % (len(dsteps),
             dsteps[0]["h"] if dsteps else "-",
             dsteps[-1]["h"] if dsteps else "-"))
    d_ex = d_bat = d_marg = d_l2 = 0
    d_c1, d_one, d_ot, d_h, d_t2, d_mu = [], [], [], [], [], []
    print("    kz(r2) h      s_P        1-s_P     (1-sP)/tau2 "
          "best_cert  a-b       exact-c1")
    for st in dsteps:
        Gc = st["Gc"]
        v0 = st["v0"]
        bt = battery(Gc)
        r = exact_floor(Gc, v0)
        ok_ex = r["pd"] and r["bord"] and r["c1"] > 0
        d_ex += ok_ex
        d_bat += bt["best"] > 0.0
        d_marg += bt["margin"] > 0.0
        d_l2 += st["sP"] >= st["mu1"]
        c1f = float(r["c1"]) if ok_ex else float("nan")
        d_c1.append(c1f)
        one = 1.0 - st["sP"]
        d_one.append(one)
        d_ot.append(one / st["tau2"])
        d_h.append(float(st["h"]))
        d_t2.append(st["tau2"])
        d_mu.append(st["mu1"])
        print("    %-6d %-6d %.6f  %.3e  %.4f  %+.4f  %+.4f  %.6f"
              % (st["kz"], st["h"], st["sP"], one, one / st["tau2"],
                 bt["best"], bt["margin"], c1f), flush=True)
    n_d = len(dsteps)
    check("D3 CLXXIV deep reproduction s_P >= mu1",
          d_l2 == n_d, "%d/%d" % (d_l2, n_d), kill="K2")
    dlab = ("DEEP(exact %d/%d, battery %d/%d, margin %d/%d, "
            "min c1 %.6f)"
            % (d_ex, n_d, d_bat, n_d, d_marg, n_d,
               float(np.nanmin(d_c1)) if d_c1 else float("nan")))
    check("D4 typed: %s" % dlab, True)

    # combined correction law + trends (surface + deep)
    one_all = np.concatenate([one_m, np.array(d_one)])
    h_all = np.concatenate([hs, np.array(d_h)])
    t2_all = np.concatenate([tau2s, np.array(d_t2)])
    mu_all = np.concatenate([mu, np.array(d_mu)])
    mask = one_all > 0.0
    fits = {}
    for name, xv in (("log h", np.log(h_all[mask])),
                     ("log tau_2", np.log(t2_all[mask])),
                     ("log mu1", np.log(mu_all[mask]))):
        fits[name] = parent.ols_line(xv, np.log(one_all[mask]))
    print("\n    correction law log(1-s_P) vs (combined, n=%d):"
          % int(np.sum(mask)))
    for name, (sl, r2f) in fits.items():
        print("      %-10s slope %+.3f  R2 %.3f" % (name, sl, r2f))
    best_name = max(fits, key=lambda k: (fits[k][1]
                                         if np.isfinite(fits[k][1])
                                         else -1.0))
    blab = ("CORRECTION-LAW(%s, slope %+.3f, R2 %.3f); "
            "(1-sP)/tau2 med %.4f"
            % (best_name, fits[best_name][0], fits[best_name][1],
               float(np.median(np.concatenate(
                   [one_m / tau2s, np.array(d_ot)])))))
    check("B3 typed: %s" % blab, True)
    best_all = np.concatenate(
        [best, np.array([battery(st["Gc"])["best"]
                         for st in dsteps])])
    hpos = best_all > 0.0
    sl_bc, r2_bc = (parent.ols_line(np.log(h_all[hpos]),
                                    np.log(best_all[hpos]))
                    if int(np.sum(hpos)) >= 3
                    else (float("nan"),) * 2)
    print("    combined h-trend of log best_cert: slope %+.3f "
          "(R2 %.3f; flat bar %.2f)" % (sl_bc, r2_bc, HTREND_FLAT))

    # ------------------------------------------------------------ C
    section("C -- controls + the mechanism typing")
    sm_rungs = {}
    refused = usable_sm = 0
    for kz in zones:
        r = base.gram_anatomy(kz, world_fn=base.world_smooth,
                              keep_chain=True)
        if r is None or not r.get("core_ok") or r.get("negA", 1) > 0 \
                or r.get("negS", 1) > 0:
            refused += 1
        else:
            usable_sm += 1
        if isinstance(r, dict):
            sm_rungs[kz] = r
    check("C1 smooth world refuses the certificate ladder",
          refused > 0 and usable_sm < 39,
          "refused=%d usable-core-PD=%d" % (refused, usable_sm),
          kill="K2")
    for kind in ("epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C2 %s world fires" % kind, fired, detail, kill="K2")
    # C1b: the smooth battery (v0-free classical route on the
    # comb-free world) -- the mechanism typing
    n_smb = n_smc = 0
    sm_best, sm_marg = [], []
    for kz, r in sorted(sm_rungs.items()):
        if not (r.get("core_ok") and "chain" in r
                and "y_core" in r):
            continue
        al, be, m0 = r["chain"]
        Pc = base.eval_chain(al, be, m0, r["y_core"], r["h"])
        H0 = np.sqrt(r["v_core"])[:, None] * Pc
        Gc = H0 @ H0.T
        Gc = 0.5 * (Gc + Gc.T)
        n_smb += 1
        bt = battery(Gc)
        sm_best.append(bt["best"])
        sm_marg.append(bt["margin"])
        if bt["best"] > 0.0:
            n_smc += 1
    mech = ("W1-MECHANISM-CLASSICAL(%d/%d)" % (n_smc, n_smb)
            if n_smb > 0 and n_smc == n_smb
            else "W1-MECHANISM-PARTIAL(%d/%d)" % (n_smc, n_smb))
    if sm_best:
        print("    smooth battery: best_cert min/med/max "
              "%+.4f / %+.4f / %+.4f; a-b min/med "
              "%+.4f / %+.4f"
              % (band(np.array(sm_best))
                 + (float(np.min(sm_marg)),
                    float(np.median(sm_marg)))))
    print("    nu_+ CONTENT (typed): arch layer comb-free; atom "
          "layer = von-Mangoldt tents -> nu_+ CONTAINS COMB DATA; "
          "the statement is classical, the comb enters only "
          "through the measured hypotheses.")
    check("C1b typed: %s" % mech, True)
    # C3: construction sensitivity (kill)
    moves_rev, moves_r1 = [], []
    for w in rows:
        v = w["r2"]["v_core"]
        Pc = w["H"] / np.sqrt(v)[:, None]
        vr = v[::-1]
        Gp = (np.sqrt(vr)[:, None] * (Pc @ Pc.T)
              * np.sqrt(vr)[None, :])
        Gp = 0.5 * (Gp + Gp.T)
        spp = sp_of(Gp, w["v0"])
        if spp is not None and spp > 0.0:
            moves_rev.append(abs(math.log(spp / w["sP"])))
        ch1 = w["r1"].get("chain")
        if ch1 is not None:
            al1, be1, m01 = ch1
            Pc1 = base.eval_chain(al1, be1, m01, w["r2"]["y_core"],
                                  w["r1"]["h"])
            G1 = (np.sqrt(v)[:, None] * (Pc1 @ Pc1.T)
                  * np.sqrt(v)[None, :])
            G1 = 0.5 * (G1 + G1.T)
            sp1 = sp_of(G1, w["v0"])
            if sp1 is not None and sp1 > 0.0:
                moves_r1.append(abs(math.log(sp1 / w["sP"])))
    med_rev = float(np.median(moves_rev)) if moves_rev else 0.0
    check("C3 weight-reversal control fires: med |dlog s_P| = "
          "%.4f >= %.2f (n=%d, min %.4f, max %.4f)"
          % (med_rev, MOVE_BAR, len(moves_rev),
             float(np.min(moves_rev)) if moves_rev else 0.0,
             float(np.max(moves_rev)) if moves_rev else 0.0),
          med_rev >= MOVE_BAR, kill="K2")
    if moves_r1:
        print("    C3b false-chain (r1 at r2 nodes): med "
              "|dlog s_P| %.4f (n=%d, max %.4f) -- recorded"
              % (float(np.median(moves_r1)), len(moves_r1),
                 float(np.max(moves_r1))))
    check("C3b false-chain movement recorded", True)

    # ---------------------------------------------------- screens
    section("S -- mandatory tau screens")
    scr_sp, sl_sp = parent.screen(sP, taus1)
    scr_bc, sl_bc2 = parent.screen(best[best > 0.0],
                                   taus1[best > 0.0])
    print("    TAU-SCREEN s_P       %s" % scr_sp)
    print("    TAU-SCREEN best_cert %s" % scr_bc)
    check("S screens recorded", True)

    # ---------------------------------------------------- verdict
    reloc = (("RELOCATION" in scr_sp)
             or ("RELOCATION" in scr_bc))
    legs = []
    if not (n_pd == len(rows) and n_bord == n_pd):
        legs.append("exact-surface")
    if d_ex != n_d:
        legs.append("exact-deep")
    if int(np.sum(best > 0.0)) != len(rows):
        legs.append("classical-surface")
    if d_bat != n_d:
        legs.append("classical-deep")
    if not (n_smb > 0 and n_smc == n_smb):
        legs.append("smooth-battery")
    if not (n_att >= 1 and n_ivc == n_att):
        legs.append("interval-subset")
    if not (np.isfinite(sl_bc) and abs(sl_bc) <= HTREND_FLAT):
        legs.append("h-trend")
    if reloc:
        legs.append("tau-reloc")
    if not legs:
        head = ("W1-THEOREM-CANDIDATE(min certified c1 = %.6f; "
                "GAPS NAMED: all-h H1/H2 for nu_+, interval "
                "coverage beyond %d steps, deep float level, "
                "frozen-frame convention)" % (c1_min, n_att))
    elif n_pd == len(rows) and n_bord == n_pd:
        head = ("W1-CERTIFIED-SURFACE(min c1 = %.6f; missing: %s)"
                % (c1_min, ",".join(legs)))
    else:
        head = "W1-MEASURED-ONLY(%s)" % ",".join(legs)
    labels = dict(
        b=blab,
        f=("F1(%d/%d, min c1 %.4f) F2(best>0 %d/%d) F4(%d/%d)"
           % (n_pd, len(rows), c1_min, int(np.sum(best > 0.0)),
              len(rows), n_ivc, n_att)),
        m=mech, d=dlab, head=head)
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
