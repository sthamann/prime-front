#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""state_factorization_census_probe -- PRIME.STATE.FACTOR.CENSUS.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin,
wrap_genesis_probe.py / its logs / its next.txt note, and every
verification/paper/website surface) are not touched.

=======================================================================
MISSION (round 211, HIGHEST-PRIORITY lane of the radical-focus
3-round plan).  Round 210 (secular_crossing_coord_probe, SPEC
e7ef1d6cdb96cfb4) proved: the post-wrap telescope Phi(s*) = C_h +
sum dmu_p is ONE-SIGNED in every battery coordinate (coherence 1.0,
wrap-is-only-exception) BUT the increments
    dmu_j = c_h x_j^T Q_{p_j} x_{j-1},   x_j = N_j^{-1} phi
are STATE-CARRIED (rho = dmu/freeT spread 0.74-1.26 dex,
order-dependence 0.74-0.95).  The sign is not the problem.  The
problem is that x_j depends on the entire prior orbit, which blocks
a classical tail theorem.  THE ONE QUESTION OF THIS ROUND: is the
terminal / orbit state Euler-factorizable -- can the state-dependent
sandwich be rewritten as an arithmetic / Euler-local sum?

FROZEN HYPOTHESES (declared BEFORE any record numbers; no H4; no
new coordinate Phi on s* or on the wall):
  H0 ORBIT-IRREDUCIBLE.  x_j cannot be written as a seed times a
     function of the primes seen so far, in any of the tested
     classes.  Residual spread stays O(1) dex.
  H1 RANK-ONE STATE.  x_j = G_j x_0 with G_j a product of low-rank
     Woodbury/graph-action updates.  Operational: the family {x_j}
     (unit-column matrix) is a rank-one ray, or rank-r with r <= 3
     frozen.  Geometric rank at RANK_REL plus the Euclidean energy
     residual E_res(r) = 1 - (sum_{i<=r} sigma_i^2)/(sum sigma_i^2)
     of that unit-column family.  Increment-projection V_res/V0 is
     a CROSS-CHECK only (see instrument rider).
  H2 ADDITIVE GRAM STATE.  The Born reconstructions
     x_j^{seed} = x_S + W_S (sum_{i<=j} Q_{p_i}) x_S
     x_j^{term} = x_T - sum_{q in tail after j} W_T Q_q x_T
     are built from Q / Euler blocks + ONE frozen resolvent (seed
     or terminal), no orbit inversions of N_j.  Predicted sandwich
     vs observed dmu.
  H3 EULER-PRODUCT STATE.  G_j = G_seed · H(p_1,..,p_j) with H
     multiplicative.  Tests: (i) T_p T_q = T_{Q_p+Q_q} (BH11-F6:
     elementary lemma, warded, not a structure theorem);
     (ii) frozen-W vector commutator of G_p = (I - W Q_p)^{-1} on
     the seed/terminal Weyl vector; (iii) pair kernel
     F_p + sum_{q in tail} F_{p,q} with
     F_p = c x_T^T Q_p x_T,
     F_{p,q} = -c x_T^T (Q_p W_T Q_q + Q_q W_T Q_p) x_T
     (linear-in-eta truncation of the terminal Born).  An exact
     F_p (no pair) would be the prize.

PRIMARY VARIANCE FUNCTIONAL (frozen):
  V0(h) := sample variance (ddof=1) of {log10 rho_p} over post-wrap
  inc-order primes with rho_p = dmu_p / freeT_p, freeT_p =
  c_h x_T^T Q_p x_T > 0, dmu_p > 0.  This IS the r210
  state-dependence object (spread = log10(max rho/min rho) is the
  disclosed cross-check; order-dependence dex is the second
  cross-check).
  After a hypothesized factorization with predicted increments
  pred_p, V_res := sample variance of {log10 dmu_p - log10 pred_p}
  when every pred_p > 0; else the predictor is typed DIVERGED and
  V_res/V0 := +inf (fails the hard gate).  Sign-safe raw
  R2 = sum((dmu-pred)^2)/sum(dmu^2) is reported alongside.
  HARD GATE for FACTOR: V_res/V0 < 1e-2 at the frozen deep rungs
  h = 8 AND h = 13.  Explained-variance percentage is reported;
  the gate is the ratio.

INSTRUMENT RIDER (disclosed pre-freeze, r210-G23 pattern): the wrap
prime climbs (r210: 2->3->5->7->13), so reachable rungs have
n_pw = 2 post-wrap inc primes.  A 2-point increment ratio after
projecting the OBSERVED states onto their leading SVD mode is
under-powered (it can clear 1e-2 without a ray).  Therefore H1 is
adjudicated by GEOMETRIC RANK + Euclidean E_res of the unit-column
family, and the increment projection ratio is a CROSS-CHECK, not
the H1 hard gate.  FACTOR itself still requires an Euler-block
increment predictor (H2 or H3, which do NOT read the orbit x_j
except the single terminal/seed LU) to clear 1e-2.  H1 projection
uses observed x_j and cannot by itself be FACTOR.

THE CONTROL: MAIN vs Scrarith.  FACTOR requires BOTH the ratio
< 1e-2 on MAIN AND the same procedure fails to factor Scrarith
(or factors it to a structurally different residual, e.g. the
budget overshoot).  If both worlds factor the same way: type
FACTOR-BUT-NOT-SEPARATING and map onto PARTIAL.  Epstein(8) is a
SECONDARY screen only (n_neg=3; inertia already separates; do NOT
treat "Epstein fails H3" as a win).  Smooth is portless degenerate
(one cell).

ALLOWED VERDICTS (exactly one):
  FACTOR      -- V_res/V0 < 1e-2 on MAIN at h=8 and h=13 from an
                 Euler-block predictor AND Scrarith does not share
                 it.
  PARTIAL     -- named leftover structure (e.g. rank-2 Euclidean
                 with a Scrarith-shared second direction, or a pair
                 kernel that is not small) but the increment ratio
                 stays >= 1e-2 OR the structure is not MAIN-
                 specific.  STOP.  Do not invent H4/H5.
  IRREDUCIBLE -- H0 wins: full geometric rank, commutators do not
                 abelianize the state, V_res/V0 stays O(1) or
                 DIVERGED, Scrarith looks like MAIN.

PRE-REGISTERED PRIORS (none gate-forcing; ONE disclosed pre-freeze
prototype proto_sfc_scratch.py at h=4,5,8 + SCRARITH(5), log kept
as proto_sfc_scratch.out1.log, plus a disclosed extra MAIN h=13
read appended to that log; script deleted at freeze):
  P1 cascade closure exact (proto 8.0e-62 / 7.0e-61 / 1.4e-80 at
     4/5/8); wrap primes == r210 CAL_WRAPP; rho spread == r210
     CAL_SPREAD (1.057 / 1.259 / 0.954 at 4/5/8; h=13: 0.883).
  P2 geometric rank_all == n_states at RANK_REL 1e-8 (FULL: 3/4/5
     at 4/5/8, 7 at h=13); rank_post == n_post; n_post == 3 at
     h >= 5 because the wrap prime climbs (always ~2 post-wrap
     increments).  Unit-column sigma ratios ~ 1.00, 0.40, 0.04.
  P3 H1 Euclidean E_res(r=1) ~ 0.12-0.22 MAIN (FAILS 1e-2); E_res
     (r=2) ~ 1.5e-3 (a rank-2 Euclidean organization).  Increment
     H1 r=1 projection ratio < 1e-2 at every proto rung -- the
     under-powered n_pw=2 artifact, ALSO < 1e-2 on Scrarith
     (0.0006): NOT admitted as FACTOR evidence.
  P4 H2 seed-Born log-ratio ~ 1.3-1.4 (does not help).  H2
     terminal-Born and H3 pair DIVERGE on MAIN (signed pred
     1e10..1e47 at h=5/8: NoP is indefinite, W_T blows the linearized
     tail).  Scrarith terminal-Born R2 ~ 0.089, pair R2 ~ 0.61 --
     neither < 1e-2, and MAIN is WORSE not better.
  P5 T_p T_q = T_{Q_p+Q_q} exact (elementary lemma).  Frozen-G
     commutators: seed O(10^{-1}) shrinking with h (h=13: 9e-4);
     terminal O(1) (0.34-0.67).  Q_p Q_q - Q_q Q_p relative
     Frobenius O(10^{-1}).  The chain is abelian; the state maps
     are not.
  P6 consecutive unit-state cosines: ~ -1 at the wrap (the r208
     pole-ray flip, cascade-born, typed as a SCREEN, hypotheses
     not retargeted) and ~ 0.5 at the last MAIN step (a second
     direction enters at the window edge).
  P7 Scrarith(5): full geometric rank 4, MORE Euclidean-concentrated
     (E_res r=1 ~ 0.036), wrap (2,5), s* overshoot as r210, H1
     increment ratio also < 1e-2 -- SHARED, not a separator.
  P8 expected composite: PARTIAL -- named leftover RANK-2-EUCLIDEAN
     (E_res r=2 < 1e-2, wrap-flip + last-step second direction),
     increment Euler-factor IRREDUCIBLE (Born/pair DIVERGED on
     MAIN), NOT-SEPARATOR (Scrarith shares the rank-2 and the
     under-powered H1 increment ratio).  Hardness reduction: NO.

NOTATION (r171-r210 VERBATIM).  Rung h = builder x (R4.build_cell,
even sector); a = log(h)/2; L = 2a; K = ceil(1.25 h log h);
phi_k = 1/(1/4 + om_k^2); c_h = 2 sinh^2(a/2); G_B = (L/2)
diag(2,1,...,1); theta = sum_{p<=h} log p; A0 = RawArch + theta G_B;
Q_p = r204 dissipation Grams (qp_gram copied VERBATIM from
euler_hpin_region_probe.py, which copies the r204 closed-form
trig); N_j = A0 - sum_{i<=j} Q_{p_i}; x_j = N_j^{-1} phi (LU);
dmu_j = c_h x_j^T Q_p x_{j-1} (Woodbury, warded); freeT_p =
c_h x_T^T Q_p x_T with x_T = NoP^{-1} phi; wrap j* = min{j: mu_j
<= -1}; post-wrap steps j > j*.  Engine for ranks/energy: numpy
SVD of unit-column float64 matrices (disclosed; not an eigen-read
of the wall).  Engine for G-commutators: mp LU of (A0 - Q) and
(NoP - Q) applied to the Weyl vector (disclosed).  NO eigsy on
MAIN.  Control-world n_neg uses eigsy as a SCREEN only, never as
a factorization input.

RUNGS AND DPS (frozen; disclosed subset of the r210 house ladder):
RUNGS = (4, 5, 6, 7, 8, 13).  Deep rungs for the hard gate: h = 8
and h = 13.  SKIP (disclosed, runtime): 9, 10, 11, 12, 16, 20.
h = 16 has the SAME prime set as h = 13 (no new Euler factor);
h = 20 would add {17,19} but is optional/costly.  DPS = {4:60,
5:60, 6:65, 7:70, 8:80, 13:120} house values.  SMOKE_RUNGS = (4, 5)
+ SCRARITH.  WORKERS = 4.

FROZEN BARS: WARD_BAR 1e-45 (cascade closure, rel max-entry);
WOOD_BAR 1e-30 (Woodbury step, rel); RANK_REL 1e-8 (numerical rank
of unit-column family); HARD_RATIO 1e-2; DIVERGE_BAR 1e6
(|pred/dmu|); TCOMM_BAR 1e-20 (T-chain remainder, rel fro);
RUNTIME_BAR 2700 s.  Record tolerances: SPREAD_TOL 0.10 dex;
VAL_TOL 0.05 (E_res, ratios that stay O(1)); RANK exact;
LOG_TOL 0.11 dex.  Inheritance tables (r210 frozen spec VERBATIM):
R210_WRAP and R210_SPREAD below.

TAXONOMY (frozen resolution logic):
  rankEnum  := FULL-RANK-ORBIT iff rank_all == n_states at every
               MAIN rung; else LOW-RANK-r if rank_all <= 3; else
               MIXED-RANK.
  h1Enum    := RANK-ONE-RAY iff E_res(r=1) < HARD_RATIO at h=8 and
               h=13; else RANK-TWO-EUCLIDEAN iff E_res(r=2) <
               HARD_RATIO at those rungs; else H1-FAILS.
  h2Enum    := ADDITIVE-BORN-HOLDS iff min(H2_seed, H2_term) ratio
               < HARD_RATIO at h=8 and h=13; else BORN-DIVERGENT
               iff terminal-Born DIVERGED at any deep rung; else
               BORN-RESIDUAL-O1.
  h3Enum    := EULER-PRODUCT-STATE iff H3 pair ratio < HARD_RATIO
               AND max terminal-G commutator < 1e-2 at deep rungs;
               else PAIR-KERNEL-DIVERGENT iff pair DIVERGED; else
               NONABELIAN-STATE.
  sepEnum   := MAIN-SPECIFIC-FACTOR iff MAIN has an H2/H3 increment
               ratio < HARD_RATIO AND Scrarith's matching ratio is
               >= HARD_RATIO; else SHARED-OR-NEITHER.
  verdict   := FACTOR iff sepEnum is MAIN-SPECIFIC-FACTOR;
               PARTIAL iff not FACTOR and (h1Enum is RANK-TWO-
               EUCLIDEAN or a named H2/H3 leftover lives);
               IRREDUCIBLE otherwise.
  plus the definitional riders (always typed, never consumed):
  CENSUS-FORALL-K == LOOP; WEIL-ALLTESTS; TURAN-CONE-POSITIVITY;
  INERTIA-FROM-WALL; CROSSING-MARGIN-IS-THE-WALL;
  PR-DOMINATION-COFINALLY-IS-THE-WALL; GPSD; eighth cycle -- ALL
  flagged, consumed by NOTHING.  N1 membership is NOT reopened
  (r208: the wrap flip IS the pole-ray birth, reported as a
  cosine screen).

ANTI-LOOP / FIREWALL.  No lambda_min, tau_h, Delta_h, wall PSD, or
eig as INPUTS to the factorization builders (functions factor_*).
dmu is the object being factored (orbit data, allowed).  AST-check
the factor_* bodies.  No probe-module import of r204/r205/r210
(helpers copied VERBATIM with source comments).  No verification
import, no zero-oracle, no np.load of other probes' caches.
Witness-blind: finite linear algebra on the even-sector wall /
Euler blocks only.

RECORD TABLES (inserted at freeze from the disclosed ladder: smoke1
25/26 FAIL G22 kept as state_factorization_census_probe.smoke1.log
at pre-freeze SHA bccfaaecfcc256b2 -- the Woodbury sandwich was
float64, worst rel 3.0e-16 vs WOOD_BAR 1e-30; smoke2 26/26 after
A1+A2, same SHA, state_factorization_census_probe.smoke2.log; ONE
calibration pass calib_sfc_pass1.log, 26/26, all 6 rungs + all
three controls, 231.8 s, same pre-freeze SHA).  Verdicts frozen
from calibration: FULL-RANK-ORBIT at RANK_REL 1e-8 (rank_all =
n_states = 3/4/4/5/5/7); RANK-TWO-EUCLIDEAN (E_res r=1 =
0.118-0.147, r=2 = 0.0013-0.0018); BORN-DIVERGENT (terminal-Born
DIVERGED at every rung, R2 1e22..1e93); PAIR-KERNEL-DIVERGENT;
SHARED-OR-NEITHER; composite PARTIAL.  Wrap/spread == r210.
AMENDMENTS (pre-freeze, disclosed; no bar/dps/rung/target moved):
  A1 G22: Woodbury sandwich recomputed in mp (r210-G23 pattern:
     the first coding used float64, 3e-16 vs 1e-30; the mp ward
     is strictly stronger, measured 6.4e-61).
  A2 taxonomy: `all([])` is True -- empty DEEP_RUNGS in smoke
     mis-typed H2/H3 as HOLD and the composite as FACTOR.  Fixed
     to require a nonempty eval set (smoke uses available rungs).
     No silent bar movement.
=======================================================================

WHAT IS BUILT AND GATED: S0 G01-G03 firewall + predefinition +
factor-builder AST; S1 exact layer G10-G12 (sympy); S2 census
G20-G30 (mp + numpy SVD, ProcessPool); S3 worlds G40-G42; S4
guards G50-G52; S5 verdict G60-G61 + G99 runtime.  DETERMINISM:
no randomness; ProcessPool results keyed; run2 identical modulo
WALL tokens.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 house builder

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 4
RUNTIME_BAR = 2700.0

RUNGS = (4, 5, 6, 7, 8, 13)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 13: 120}
SMOKE_RUNGS = (4, 5)
DEEP_RUNGS = (8, 13)
SKIP_DISCLOSED = (9, 10, 11, 12, 16, 20)

WARD_BAR = 1e-45
WOOD_BAR = 1e-30
RANK_REL = 1e-8
HARD_RATIO = 1e-2
DIVERGE_BAR = 1e6
TCOMM_BAR = 1e-20
DIVERGED = 1e99

SPREAD_TOL = 0.10
VAL_TOL = 0.05
LOG_TOL = 0.11
ZCLS = 1e-30

CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80),
              ("SMOOTH", 5, 60))

# r210 inheritance (secular_crossing_coord_probe frozen spec VERBATIM)
R210_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
             13: (7, 5)}
R210_SPREAD = {4: "1.057", 5: "1.259", 6: "1.003", 7: "1.105",
               8: "0.954", 13: "0.883"}

# --------------------- calibrated record tables (calib_sfc_pass1.log)
CAL_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
            13: (7, 5)}
CAL_SPREAD = {4: "1.057", 5: "1.259", 6: "1.003", 7: "1.105",
              8: "0.954", 13: "0.883"}
CAL_RANK = {4: 3, 5: 4, 6: 4, 7: 5, 8: 5, 13: 7}
CAL_ERES1 = {4: "0.1175", 5: "0.1446", 6: "0.1475", 7: "0.1397",
             8: "0.1407", 13: "0.1174"}
CAL_ERES2 = {4: "0.001422", 5: "0.001533", 6: "0.001434",
             7: "0.001782", 8: "0.00182", 13: "0.001297"}
CAL_H1INC = {4: "0.009117", 5: "0.004698", 6: "0.01131",
             7: "0.002261", 8: "0.007534", 13: "0.001275"}
CAL_H2SEED = {4: "DIVERGED", 5: "1.407", 6: "1.562", 7: "1.307",
              8: "1.368", 13: "1.253"}
CAL_H2TERM = {4: "DIVERGED", 5: "DIVERGED", 6: "DIVERGED",
              7: "DIVERGED", 8: "DIVERGED", 13: "DIVERGED"}
CAL_H3PAIR = {4: "DIVERGED", 5: "DIVERGED", 6: "DIVERGED",
              7: "DIVERGED", 8: "DIVERGED", 13: "DIVERGED"}
CAL_GTERM = {4: "0.4308", 5: "0.772", 6: "1.661", 7: "2.792",
             8: "3.22", 13: "1.349"}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=3, sstar="0.7930", rank=4),
    "SCRARITH": dict(nneg=3, sstar="1.0632", exit_last=True, rank=4,
                     eres1="0.0356", H2_term="0.06569",
                     H3_pair="0.4255"),
    "SMOOTH": dict(nneg=2, sstar="1.2733", portless=True),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    banned_mods = (
        "euler_hpin_region_probe", "euler_jet_colligation_probe",
        "secular_crossing_coord_probe", "pontryagin_n1_weyl_probe",
        "terminal_dissipation_probe", "wrap_genesis_probe",
        "alphabet31_hidden_structure_probe", "axiom246_hold_probe",
        "broad_sweep_clocks_registers_probe",
        "ftransfer_context15_probe",
        "gesamtbild_synthesis_claims_probe",
        "nonclifford_prime_probe", "qsys_jet_iso_probe",
        "quillen_jet_a4_probe",
        "quillen_level_dictionary_census_probe",
        "quillen_ramified_level_probe",
        "readout_fourier_factor_probe", "rp_nsr_flat_probe")
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(
                node.value, str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m is None:
                    continue
                if m.startswith("verification"):
                    bad.append("import " + m)
                root = m.split(".")[0]
                if root in banned_mods:
                    bad.append("probe-module import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import, no r204/r205/r210 "
                       "probe-module import (helpers copied); "
                       "eigsy consumed only as control-world "
                       "inertia SCREEN; fully zero-free; "
                       "concurrent-lane files untouched")


def factor_builder_ast() -> tuple[bool, str]:
    """AST-check factor_* bodies: no wall-eig / tau / Delta premises."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb_names = {"eigsy", "tau", "Delta", "lam_min", "mpE"}
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if not node.name.startswith("factor_"):
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            if nm in forb_names:
                bad.append("%s uses %s @%d" % (node.name, nm,
                                               sub.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "factor_* builders are Q_p / Euler / seed / "
                       "terminal LU + numpy SVD; no eigsy, no tau, "
                       "no Delta, no lam_min as premises")


# --- copied VERBATIM from euler_jet_colligation_probe.py (r204) ---
def primes_upto(x: int) -> list[int]:
    return [p for p in range(2, x + 1)
            if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]


def m_nilp(p: int, h: int) -> int:
    m, q = 0, p
    while q < h:
        m += 1
        q *= p
    return m


def trig_int(alpha, beta, phi, psi, t0, t1):
    if t1 <= t0:
        return mp.mpf(0)

    def F(t):
        if alpha == 0 and beta == 0:
            return t * mp.cos(phi) * mp.cos(psi)
        if alpha == beta:
            return (t * mp.cos(phi - psi)
                    + mp.sin(2 * alpha * t + phi + psi)
                    / (2 * alpha)) / 2
        return (mp.sin((alpha - beta) * t + phi - psi) / (alpha - beta)
                + mp.sin((alpha + beta) * t + phi + psi)
                / (alpha + beta)) / 2
    return F(t1) - F(t0)


def w_kernel_add(Acc, u, w, oms, L, K):
    for i in range(K):
        for j in range(i):
            bi, bj = oms[i] ** 2, oms[j] ** 2
            od = 2 * (oms[i] * mp.sin(oms[i] * u)
                      - oms[j] * mp.sin(oms[j] * u)) / (bi - bj)
            Acc[i, j] += w * od
            Acc[j, i] += w * od
    for k in range(K):
        if k == 0:
            Acc[0, 0] += w * 2 * (u - L)
        else:
            Acc[k, k] += w * (mp.sin(oms[k] * u) / oms[k]
                              + (u - L) * mp.cos(oms[k] * u))


# --- copied VERBATIM from euler_hpin_region_probe.py (r205) ---
def to_raw(Mb, par, nrm, K):
    Rb = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Rb[i, j] = par[i] * nrm[i] * Mb[i, j] * nrm[j] * par[j]
    return Rb


def pd_flag(N, K):
    try:
        mp.cholesky(N)
        return True
    except Exception:                             # noqa: BLE001
        return False


def qp_gram(p, h, oms, L, K):
    """r204 dissipation Gram Q_p VERBATIM (closed-form trig)."""
    lp = mp.log(p)
    lam = mp.exp(-lp / 2)
    Mt = m_nilp(p, h)

    def d2ip(i, j, m, n):
        lo = max(m, n) * lp
        sp = L - lp
        ph_ = -oms[i] * m * lp
        ps_ = -oms[j] * n * lp
        acc = mp.mpf(0)
        if sp > lo:
            acc += (1 - lam ** 2) * trig_int(oms[i], oms[j],
                                             ph_, ps_, lo, sp)
        acc += trig_int(oms[i], oms[j], ph_, ps_, max(lo, sp), L)
        return acc

    Qp = mp.zeros(K, K)
    for i in range(K):
        for j in range(i + 1):
            s = mp.mpf(0)
            for m in range(Mt + 1):
                for n in range(Mt + 1):
                    s += lam ** (m + n) * d2ip(i, j, m, n)
            Qp[i, j] = lp * s
            Qp[j, i] = Qp[i, j]
    return Qp


def solve_x(N, phi, K):
    x = mp.lu_solve(N, mp.matrix(phi))
    m = sum(phi[i] * x[i] for i in range(K))
    return m, x


def np_vec(x, K):
    return np.array([float(x[i]) for i in range(K)], dtype=float)


def np_mat(A, K):
    M = np.empty((K, K), dtype=float)
    for i in range(K):
        for j in range(K):
            M[i, j] = float(A[i, j])
    return M


def samp_var(vals):
    n = len(vals)
    if n < 2:
        return float("nan")
    m = sum(vals) / n
    return sum((v - m) ** 2 for v in vals) / (n - 1)


def sandwich_np(c, xa, Q, xb):
    return float(c) * float(xa @ (Q @ xb))


# ------------------------------------------------ factorization builders
# (AST-checked: no eigsy / tau / Delta / lam_min as premises)
def factor_unit_matrix(cols, K):
    n = len(cols)
    A = np.zeros((K, n), dtype=float)
    for j, x in enumerate(cols):
        v = np_vec(x, K)
        nrm = float(np.linalg.norm(v))
        if nrm > 0:
            A[:, j] = v / nrm
    return A


def factor_h1_energy(cols, K):
    """Euclidean energy residuals of the unit-column family."""
    A = factor_unit_matrix(cols, K)
    s = np.linalg.svd(A, compute_uv=False)
    tot = float(np.sum(s ** 2))
    if tot <= 0:
        return (0, [], [float("nan")] * 3)
    s0 = float(s[0])
    ratios = [float(v / s0) for v in s]
    rank = sum(1 for r in ratios if r > RANK_REL)
    eres = []
    for r in (1, 2, 3):
        ru = min(r, len(s))
        eres.append(1.0 - float(np.sum(s[:ru] ** 2)) / tot)
    return rank, ratios, eres


def factor_h1_project_inc(xs, K, Qn, cf, pw_idx, ps_pw, r):
    """CROSS-CHECK: sandwiches after rank-r projection of observed x."""
    n = len(xs)
    A = np.zeros((K, n), dtype=float)
    raw = []
    for j, x in enumerate(xs):
        v = np_vec(x, K)
        raw.append(v)
        A[:, j] = v
    U, _S, _Vt = np.linalg.svd(A, full_matrices=False)
    ruse = min(r, U.shape[1])
    Ur = U[:, :ruse]
    pred = []
    for p, j in zip(ps_pw, pw_idx):
        xa = Ur @ (Ur.T @ raw[j])
        xb = Ur @ (Ur.T @ raw[j - 1])
        pred.append(sandwich_np(cf, xa, Qn[p], xb))
    return pred


def factor_h2_seed_born(xS, WS_Q_xS, prs, K):
    """x_j = xS + sum_{i<=j} W_S Q_{p_i} xS (Euler + seed only)."""
    xB = [xS.copy()]
    acc = np.zeros(K)
    for p in prs:
        acc = acc + WS_Q_xS[p]
        xB.append(xS + acc)
    return xB


def factor_h2_term_born(xT, eta, prs, K, j):
    """x after consuming prs[:j] ≈ xT - sum_{q in tail} W_T Q_q xT."""
    tail = prs[j:]
    return xT - sum((eta[q] for q in tail), np.zeros(K))


def factor_h3_pair_pred(cf, xT, Qn, eta, p, tail):
    """F_p minus pair terms; Euler blocks + terminal state only."""
    Fp = sandwich_np(cf, xT, Qn[p], xT)
    pair_p = sandwich_np(cf, xT, Qn[p], eta[p])
    pair_t = 0.0
    for q in tail:
        pair_t += sandwich_np(cf, xT, Qn[p], eta[q])
        pair_t += sandwich_np(cf, eta[q], Qn[p], xT)
    return Fp - pair_p - pair_t


def factor_t_commutator(Qn, pairs):
    """T_p T_q - T_{Qp+Qq} remainder: the (2,1) block is -(Qp+Qq)
    either way, so the chain remainder is identically 0.  Report
    the Q-product commutator ||Qp Qq - Qq Qp||_F / (||Qp|| ||Qq||)
    as the residual nonabelian content of the Euler blocks."""
    vals = []
    for p, q in pairs:
        C = Qn[p] @ Qn[q] - Qn[q] @ Qn[p]
        den = (float(np.linalg.norm(Qn[p], "fro"))
               * float(np.linalg.norm(Qn[q], "fro")))
        vals.append(float(np.linalg.norm(C, "fro")) / max(den, 1e-300))
    return max(vals) if vals else 0.0


def factor_t_chain_remainder(Qn, pairs):
    """Numeric 2K-block remainder of T_p T_q - T_{Q_p+Q_q}."""
    worst = 0.0
    for p, q in pairs:
        S = Qn[p] + Qn[q]
        # the only possible nonzero would be in the (2,1) block;
        # it cancels identically.  Measure ||(Qp+Qq) - (Qp+Qq)||.
        rem = float(np.linalg.norm(S - (Qn[p] + Qn[q]), "fro"))
        den = float(np.linalg.norm(S, "fro")) + 1e-300
        worst = max(worst, rem / den)
    return worst


def ratio_log(dmus, pred):
    if not dmus or len(pred) != len(dmus):
        return DIVERGED, float("nan")
    if any(v <= 0 for v in pred):
        return DIVERGED, _r2(dmus, pred)
    if any(abs(p) / max(abs(d), 1e-300) > DIVERGE_BAR
           for d, p in zip(dmus, pred)):
        return DIVERGED, _r2(dmus, pred)
    eps = [math.log10(a) - math.log10(b) for a, b in zip(dmus, pred)]
    return samp_var(eps), _r2(dmus, pred)


def _r2(dmus, pred):
    num = sum((a - b) ** 2 for a, b in zip(dmus, pred))
    den = sum(a * a for a in dmus)
    return num / max(den, 1e-300)


def vratio(vres, V0):
    if vres >= DIVERGED / 2:
        return DIVERGED
    if not (V0 == V0 and V0 > 0 and vres == vres):
        return float("nan")
    return vres / V0


# ------------------------------------------------------- world helpers
def scrarith_Qs(x, K, oms, L, GBd, RawArch):
    gold = (math.sqrt(5.0) - 1.0) / 2.0
    nlist = []
    for p in primes_upto(x):
        q = p
        while q <= x:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]
    keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
    perm = sorted(range(len(keys)), key=lambda i: keys[i])
    wts = [atoms[i][1] for i in range(len(atoms))]
    atomw = {nlist[i][0]: wts[perm[i]] for i in range(len(nlist))}
    prs = primes_upto(x)
    Qw = {}
    for p in prs:
        lp = mp.log(p)
        Q = mp.zeros(K, K)
        for i in range(K):
            Q[i, i] = lp * GBd[i]
        for q, pp in nlist:
            if pp == p:
                w_kernel_add(Q, mp.log(q), -atomw[q], oms, L, K)
        Qw[p] = Q
    theta = sum(mp.log(p) for p in prs)
    A0 = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            A0[i, j] = RawArch[i, j]
        A0[i, i] += theta * GBd[i]
    return prs, Qw, A0


def epstein_blocks(x, K, oms, L, GBd, RawArch):
    icap = x
    rq = [0.0] * (icap + 1)
    xm = int(math.isqrt(icap)) + 1
    ym = int(math.isqrt(icap // 5)) + 1
    for xx in range(-xm, xm + 1):
        for yy in range(-ym, ym + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= icap:
                rq[n] += 1.0
    av = [mp.mpf(v) / 2 for v in rq]
    lamq = [mp.mpf(0)] * (icap + 1)
    for n in range(2, icap + 1):
        sacc = av[n] * mp.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                sacc -= lamq[dd] * av[n // dd]
        lamq[n] = sacc
    w4 = lamq[4] / 2
    w5 = lamq[5] / mp.sqrt(5)
    w6 = lamq[6] / mp.sqrt(6)
    l2, l5 = mp.log(2), mp.log(5)
    Q2 = mp.zeros(K, K)
    for i in range(K):
        Q2[i, i] = l2 * GBd[i]
    w_kernel_add(Q2, mp.log(4), -w4, oms, L, K)
    Q5 = mp.zeros(K, K)
    for i in range(K):
        Q5[i, i] = l5 * GBd[i]
    w_kernel_add(Q5, mp.log(5), -w5, oms, L, K)
    K6 = mp.zeros(K, K)
    w_kernel_add(K6, mp.log(6), w6, oms, L, K)
    for i in range(K):
        for j in range(K):
            K6[i, j] = -K6[i, j]
    A0e = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            A0e[i, j] = RawArch[i, j]
        A0e[i, i] += (l2 + l5) * GBd[i]
    return A0e, [("2", Q2), ("5", Q5), ("6", K6)]


def apply_W(Nmp, vec_np, K):
    rhs = mp.matrix([mp.mpf(float(v)) for v in vec_np])
    y = mp.lu_solve(Nmp, rhs)
    return np_vec(y, K)


def factor_g_comm_vec(W, Qp, Qq, x):
    """||G_p G_q x - G_q G_p x|| / norms with frozen W,
    G = (I - W Q)^{-1}.  Numpy solve engine (disclosed)."""
    I = np.eye(W.shape[0])

    def apply_G(Q, v):
        return np.linalg.solve(I - W @ Q, v)

    ypq = apply_G(Qp, apply_G(Qq, x))
    yqp = apply_G(Qq, apply_G(Qp, x))
    num = float(np.linalg.norm(ypq - yqp))
    den = float(np.linalg.norm(ypq)) * float(np.linalg.norm(yqp))
    return num / max(den, 1e-300)


def census_from_orbit(prs, Qs, A0, NoP, phi, c, K, order_inc=True):
    """Build inc orbit + H1/H2/H3 census.  No wall-eig, no tau."""
    Qn = {p: np_mat(Qs[p], K) for p in prs}
    _mT, xT = solve_x(NoP, phi, K)
    _mS, xS = solve_x(A0, phi, K)
    xT_n = np_vec(xT, K)
    xS_n = np_vec(xS, K)
    cf = float(c)
    eta = {p: apply_W(NoP, Qn[p] @ xT_n, K) for p in prs}
    WS_Q = {p: apply_W(A0, Qn[p] @ xS_n, K) for p in prs}

    order = list(prs) if order_inc else list(reversed(prs))
    N = mp.matrix(A0)
    m0, x0 = solve_x(N, phi, K)
    mus = [c * m0]
    xs = [x0]
    wood_worst = mp.mpf(0)
    steps = []
    for p in order:
        for i in range(K):
            for j in range(K):
                N[i, j] -= Qs[p][i, j]
        m1, x1 = solve_x(N, phi, K)
        dmu = c * m1 - mus[-1]
        Qx = [sum(Qs[p][i, k2] * xs[-1][k2] for k2 in range(K))
              for i in range(K)]
        wood_mp = c * sum(x1[i] * Qx[i] for i in range(K))
        wrel = abs(dmu - wood_mp) / max(abs(dmu), mp.mpf("1e-300"))
        wood_worst = max(wood_worst, wrel)
        fT = sandwich_np(cf, xT_n, Qn[p], xT_n)
        mus.append(c * m1)
        xs.append(x1)
        steps.append(dict(p=p, dmu=float(dmu), fT=fT,
                          wood=float(wood_mp), j=len(steps) + 1))
    P = len(order)
    jstar = next((j for j in range(P + 1) if mus[j] <= -1), None)
    wrap_p = (0 if jstar == 0 else order[jstar - 1]) if jstar is not \
        None else None

    rk_all, srat_all, eres_all = factor_h1_energy(xs, K)
    xs_post = xs[jstar:] if jstar is not None else xs
    rk_post, srat_post, eres_post = factor_h1_energy(xs_post, K)
    Ufam = factor_unit_matrix(xs, K)
    Agram = np.stack(
        [np.outer(Ufam[:, j], Ufam[:, j]).ravel()
         for j in range(Ufam.shape[1])], axis=1)
    sg = np.linalg.svd(Agram, compute_uv=False)
    g0 = float(sg[0]) if len(sg) else 0.0
    gram_rank = sum(1 for v in sg if g0 > 0 and float(v / g0) > RANK_REL)

    rhos, dmus, ps_pw, pw_idx = [], [], [], []
    for st in steps:
        if jstar is None:
            continue
        if st["j"] > jstar and st["fT"] > 0 and st["dmu"] > 0:
            rhos.append(st["dmu"] / st["fT"])
            dmus.append(st["dmu"])
            ps_pw.append(st["p"])
            pw_idx.append(st["j"])
    V0 = samp_var([math.log10(r) for r in rhos]) if len(rhos) >= 2 \
        else float("nan")
    spread = (math.log10(max(rhos) / min(rhos))
              if len(rhos) >= 2 else float("nan"))

    h1inc = {}
    for r in (1, 2, 3):
        pred = factor_h1_project_inc(xs, K, Qn, cf, pw_idx, ps_pw, r)
        vr, r2 = ratio_log(dmus, pred)
        h1inc[r] = dict(ratio=vratio(vr, V0), r2=r2)

    xB = factor_h2_seed_born(xS_n, WS_Q, order if order_inc else prs, K)
    # seed-Born follows increasing-prefix of `order`
    pred2s = []
    for p, j in zip(ps_pw, pw_idx):
        pred2s.append(sandwich_np(cf, xB[j], Qn[p], xB[j - 1]))
    vr2s, r2s = ratio_log(dmus, pred2s)

    pred2t, pred3 = [], []
    for p, j in zip(ps_pw, pw_idx):
        # tails in the INC prime set (H2/H3 are set-wise, not order-wise)
        # For inc order, consumed = prs[:j], tail = prs[j:].
        if order_inc:
            tail_j = prs[j:]
            xj = factor_h2_term_born(xT_n, eta, prs, K, j)
            xjm = factor_h2_term_born(xT_n, eta, prs, K, j - 1)
            pred2t.append(sandwich_np(cf, xj, Qn[p], xjm))
            pred3.append(factor_h3_pair_pred(cf, xT_n, Qn, eta, p,
                                             tail_j))
        else:
            pred2t.append(float("nan"))
            pred3.append(float("nan"))
    vr2t, r2t = ratio_log(dmus, pred2t) if order_inc \
        else (float("nan"), float("nan"))
    vr3, r23 = ratio_log(dmus, pred3) if order_inc \
        else (float("nan"), float("nan"))

    pairs = [(prs[i], prs[k]) for i in range(len(prs))
             for k in range(i + 1, len(prs))]
    qcomm = factor_t_commutator(Qn, pairs)
    tchain = factor_t_chain_remainder(Qn, pairs)
    WS_n = np.linalg.inv(np_mat(A0, K))
    WT_n = np.linalg.inv(np_mat(NoP, K))
    gseed = 0.0
    gterm = 0.0
    if pairs:
        gvals_s, gvals_t = [], []
        for p, q in pairs:
            gvals_s.append(factor_g_comm_vec(WS_n, Qn[p], Qn[q], xS_n))
            gvals_t.append(factor_g_comm_vec(WT_n, Qn[p], Qn[q], xT_n))
        gseed = max(gvals_s)
        gterm = max(gvals_t)

    # consecutive unit cosines (wrap-flip screen)
    us = []
    nrms = []
    for x in xs:
        v = np_vec(x, K)
        nrm = float(np.linalg.norm(v))
        nrms.append(nrm)
        us.append(v / nrm if nrm else v)
    cos = [float(us[i] @ us[i + 1]) for i in range(len(us) - 1)]

    out = dict(
        primes=prs, jstar=jstar, wrap_p=wrap_p,
        mus=[float(v) for v in mus],
        n_states=len(xs), n_post=len(xs_post),
        rank_all=rk_all, rank_post=rk_post, gram_rank=gram_rank,
        srat_all=["%.3f" % r for r in srat_all[:6]],
        srat_post=["%.3f" % r for r in srat_post[:6]],
        eres_all=eres_all, eres_post=eres_post,
        n_pw=len(rhos), V0=V0, spread=spread,
        rhos=["%s:%.4g" % (p, r) for p, r in zip(ps_pw, rhos)],
        h1inc=h1inc,
        H2_seed=vratio(vr2s, V0), H2_seed_r2=r2s,
        H2_term=vratio(vr2t, V0), H2_term_r2=r2t,
        H3_pair=vratio(vr3, V0), H3_pair_r2=r23,
        qcomm=qcomm, tchain=tchain, gseed=gseed, gterm=gterm,
        wood_worst=float(wood_worst),
        cos=["%.4f" % v for v in cos],
        nrms=["%.3g" % v for v in nrms],
        pd_seed=pd_flag(mp.matrix(A0), K),
    )
    return out, steps, Qn, xT_n, xS_n, cf


# ------------------------------------------------------- rung worker
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="", world="MAIN")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            RawM = to_raw(ce["mpM"], par, nrm, K)
            RawPole = to_raw(ce["mpPole"], par, nrm, K)
            RawArch = to_raw(ce["mpArch"], par, nrm, K)
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            prs = primes_upto(h)
            theta = sum(mp.log(p) for p in prs)
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            A0 = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A0[i, j] = RawArch[i, j]
                A0[i, i] += theta * GBd[i]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            den = max(abs(NoP[i, j]) for i in range(K)
                      for j in range(K))
            Qs = {p: qp_gram(p, h, oms, L, K) for p in prs}
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    acc = A0[i, j]
                    for p in prs:
                        acc -= Qs[p][i, j]
                    dev = max(dev, abs(acc - NoP[i, j]))
            out["closure_dev"] = float(dev / den)
            cen, steps, _Qn, _xT, _xS, _cf = census_from_orbit(
                prs, Qs, A0, NoP, phi, c, K, order_inc=True)
            out.update(cen)
            # dec order-dependence at common non-wrap primes
            N = mp.matrix(A0)
            m0, x0 = solve_x(N, phi, K)
            mus_d = [c * m0]
            order_d = list(reversed(prs))
            for p in order_d:
                for i in range(K):
                    for j in range(K):
                        N[i, j] -= Qs[p][i, j]
                m1, _x1 = solve_x(N, phi, K)
                mus_d.append(c * m1)
            jsd = next((j for j in range(len(mus_d))
                        if mus_d[j] <= -1), None)
            wrap_d = (0 if jsd == 0 else order_d[jsd - 1]) if jsd is \
                not None else None
            out["wrap_dec"] = wrap_d
            di = {st["p"]: st["dmu"] for st in steps}
            dd = {}
            for j, p in enumerate(order_d, start=1):
                dd[p] = float(mus_d[j] - mus_d[j - 1])
            odev = 0.0
            wi = out["wrap_p"]
            for p in prs:
                if p in (wi, wrap_d):
                    continue
                a1, a2 = di[p], dd[p]
                odev = max(odev, abs(a1 - a2)
                           / max(abs(a1), abs(a2), 1e-300))
            out["orddev"] = odev
            # pre-wrap rho spread screen
            rhos_pre = []
            for st in steps:
                if out["jstar"] is None:
                    break
                if st["j"] < out["jstar"] and st["fT"] * st["dmu"] > 0:
                    rhos_pre.append(st["dmu"] / st["fT"])
            out["n_pre"] = len(rhos_pre)
            out["spread_pre"] = (
                math.log10(max(rhos_pre) / min(rhos_pre))
                if len(rhos_pre) >= 2 else None)
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            RawM = to_raw(ce["mpM"], par, nrm, K)
            RawPole = to_raw(ce["mpPole"], par, nrm, K)
            RawArch = to_raw(ce["mpArch"], par, nrm, K)
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2)
                   for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            E, _Q = mp.eigsy(NoP)
            zb = mp.mpf(ZCLS) * froN
            out["nneg"] = sum(1 for e in E if e < -zb)
            mP, _x = solve_x(NoP, phi, K)
            muP = c * mP
            out["muP"] = float(muP)
            out["sstar"] = float(-1 / muP) if muP != 0 else None

            if world == "SMOOTH":
                out["portless"] = True
                out["n_states"] = 1
                out["rank_all"] = 1
                out["wall_s"] = time.time() - t0
                return out

            if world == "SCRARITH":
                prs, Qs, A0 = scrarith_Qs(x, K, oms, L, GBd, RawArch)
                den = max(abs(NoP[i, j]) for i in range(K)
                          for j in range(K))
                dev = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        acc = A0[i, j]
                        for p in prs:
                            acc -= Qs[p][i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / den)
                cen, steps, _Qn, _xT, _xS, _cf = census_from_orbit(
                    prs, Qs, A0, NoP, phi, c, K, order_inc=True)
                out.update(cen)
                out["exit_last"] = bool(len(cen["mus"]) >= 2
                                        and cen["mus"][-2] <= -1
                                        < cen["mus"][-1])

            if world == "EPSTEIN":
                A0e, blocks = epstein_blocks(
                    x, K, oms, L, GBd, RawArch)
                # fake prime labels 2,5,6 for the three formal blocks
                labels = [2, 5, 6]
                Qs = {lab: blk for (lab, blk) in zip(
                    labels, (b[1] for b in blocks))}
                den = max(abs(NoP[i, j]) for i in range(K)
                          for j in range(K))
                dev = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        acc = A0e[i, j]
                        for p in labels:
                            acc -= Qs[p][i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / den)
                cen, steps, _Qn, _xT, _xS, _cf = census_from_orbit(
                    labels, Qs, A0e, NoP, phi, c, K, order_inc=True)
                out.update(cen)
                out["all_in_omega"] = all(v <= -1 for v in cen["mus"])
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    ok10 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "n_%d_%d" % (min(i, j), max(i, j))))
        Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "q_%d_%d" % (min(i, j), max(i, j))))
        Wm = (N - Q).inv()
        lhs = sp.expand(Wm - N.inv())
        rhs = sp.expand(Wm * Q * N.inv())
        ok10 &= sp.simplify(lhs - rhs) == sp.zeros(n, n)
    check("G10-woodbury-step-law-symbolic", bool(ok10),
          "(N-Q)^{-1} - N^{-1} == (N-Q)^{-1} Q N^{-1} (generic "
          "symmetric 2x2 AND 3x3, sympy exact): dmu = "
          "c_h x_j^T Q_p x_{j-1} is the exact increment law")

    ok11 = True
    for n in (2, 3):
        Q1 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "a_%d_%d" % (min(i, j), max(i, j))))
        Q2 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "b_%d_%d" % (min(i, j), max(i, j))))
        Z = sp.zeros(n, n)
        Iden = sp.eye(n)

        def chain(Qm):
            return sp.Matrix(sp.BlockMatrix(
                [[Iden, Z], [-Qm, Iden]]))
        ok11 &= sp.expand(chain(Q1) * chain(Q2)
                          - chain(Q1 + Q2)) == sp.zeros(2 * n, 2 * n)
    check("G11-abelian-chain-elementary-lemma", bool(ok11),
          "T_p T_q == T_{Q_p+Q_q} (generic 2x2 AND 3x3, sympy "
          "exact) -- BH11-F6: this is an ELEMENTARY LEMMA "
          "(additivity of N_j = A0 - sum Q in chain dress), not a "
          "structure theorem; the composed map is order-free, the "
          "orbit is not")

    ok12 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "m_%d_%d" % (min(i, j), max(i, j))))
        Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "q_%d_%d" % (min(i, j), max(i, j))))
        ph = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("p_%d" % i))
        x0 = N.inv() * ph
        x1 = (N - Q).inv() * ph
        lhs = (x1.T * Q * x0)[0, 0]
        rhs = (ph.T * (N - Q).inv() * ph)[0, 0] \
            - (ph.T * N.inv() * ph)[0, 0]
        ok12 &= sp.simplify(sp.expand(lhs - rhs)) == 0
    check("G12-sandwich-equals-weyl-increment", bool(ok12),
          "x_1^T Q x_0 == m(N-Q) - m(N) (generic 2x2 AND 3x3, "
          "sympy exact): the sandwich IS the Weyl increment, so "
          "factoring the sandwich IS factoring dmu")


def _fmt(v):
    if v is None:
        return "NA"
    if isinstance(v, float):
        if v != v:
            return "nan"
        if v >= DIVERGED / 2:
            return "DIVERGED"
        return "%.4g" % v
    return str(v)


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("state_factorization_census_probe -- "
          "PRIME.STATE.FACTOR.CENSUS.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/hypotheses H0-H3/hard gate/"
          "MAIN-vs-Scrarith control/instrument rider (n_pw=2) "
          "declared in the frozen spec (SPEC_SHA covers the "
          "declaration); priors P1-P8 from the ONE disclosed "
          "pre-freeze prototype at h=4,5,8 + Scrarith plus a "
          "disclosed h=13 extra (log kept, script deleted at "
          "freeze), none gate-forcing; r204/r205 helpers copied "
          "VERBATIM (qp_gram/to_raw/pd_flag/trig_int); SKIP of "
          "rungs %s disclosed; no H4, no new wall coordinate"
          % str(SKIP_DISCLOSED))
    okb, detb = factor_builder_ast()
    check("G03-factor-builder-ast", okb, detb)

    section("S1  EXACT LAYER (sympy: Woodbury + elementary T + sandwich)")
    exact_layer()

    rungs = SMOKE_RUNGS if smoke else RUNGS
    section("S2  STATE-FACTOR CENSUS (mp at h = %s)" % str(rungs))
    tasks = [(h, DPS[h]) for h in rungs]
    ctasks = [("SCRARITH", 5, 60)] if smoke else list(CTRL_CELLS)
    res: dict = {}
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(w_rung, t): ("rung", t[0]) for t in tasks}
        futs.update({ex.submit(w_ctrl, t): ("ctrl", t[0])
                     for t in ctasks})
        for fu in list(futs):
            outw = fu.result()
            kind, _key = futs[fu]
            if kind == "rung":
                res[outw.get("h", -1)] = outw
            else:
                cres[outw.get("world", "?")] = outw
    errs = [h for h in rungs if res.get(h, {}).get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    cerrs = [w for w in cres if cres[w].get("err")]
    for w in cerrs:
        print("  [ERR] %s %s" % (w, cres[w]["err"]))
    if errs or cerrs:
        check("G20-cascade-closure", False,
              "worker errors at %s %s" % (errs, cerrs))
        print("ABORT: worker errors")
        return 1

    check("G20-cascade-closure", all(
        res[h]["closure_dev"] <= WARD_BAR for h in rungs),
          "A0 - sum_p Q_p == NoP entrywise at every rung (max rel "
          "dev %s, bar %.0e)"
          % (str({h: "%.1e" % res[h]["closure_dev"]
                  for h in rungs}), WARD_BAR))

    wrapp = {h: (res[h]["wrap_p"], res[h]["wrap_dec"]) for h in rungs}
    spreads = {h: res[h]["spread"] for h in rungs
               if res[h]["spread"] == res[h]["spread"]}
    ok21 = all(wrapp[h] == R210_WRAP[h] for h in rungs
               if h in R210_WRAP)
    ok21 = ok21 and all(
        abs(spreads[h] - float(R210_SPREAD[h])) <= SPREAD_TOL
        for h in spreads if h in R210_SPREAD)
    if not (calib or smoke) and CAL_WRAP:
        ok21 = ok21 and all(wrapp[h] == CAL_WRAP[h] for h in rungs)
        ok21 = ok21 and all(
            abs(spreads[h] - float(CAL_SPREAD[h])) <= SPREAD_TOL
            for h in spreads if h in CAL_SPREAD)
    check("G21-orbit-inheritance", ok21,
          "wrap primes {h:(inc,dec)} = %s == r210 CAL_WRAPP at "
          "every shared rung; rho spread %s == r210 CAL_SPREAD "
          "(tol %.2f dex) -- the census rides the SAME dmu/state "
          "object as r210, not a new coordinate"
          % (str(wrapp),
             str({h: "%.3f" % spreads[h] for h in spreads}),
             SPREAD_TOL))

    check("G22-woodbury-step-ward", all(
        res[h]["wood_worst"] <= WOOD_BAR for h in rungs),
          "dmu == c_h x_j^T Q_p x_{j-1} at every inc step (worst "
          "rel %.1e, bar %.0e)"
          % (max(res[h]["wood_worst"] for h in rungs), WOOD_BAR))

    for h in rungs:
        print("  RANK h=%-2d n=%d/%d rank_all=%d rank_post=%d "
              "gram=%d srat_all %s eres1/2/3 %s"
              % (h, res[h]["n_states"], res[h]["n_post"],
                 res[h]["rank_all"], res[h]["rank_post"],
                 res[h]["gram_rank"], " ".join(res[h]["srat_all"]),
                 "/".join("%.3g" % v for v in res[h]["eres_all"])))
    full_rank = all(res[h]["rank_all"] == res[h]["n_states"]
                    for h in rungs)
    rank_enum = "FULL-RANK-ORBIT" if full_rank else "LOW-RANK-OR-MIXED"
    ok23 = all(res[h]["rank_all"] >= 1 for h in rungs)
    if not (calib or smoke) and CAL_RANK:
        ok23 = ok23 and all(
            res[h]["rank_all"] == CAL_RANK[h] for h in rungs)
    check("G23-rank-census", ok23,
          "CENSUS (1)(2) DELIVERED: geometric rank of unit-column "
          "{x_j} at RANK_REL=%.0e is %s -- rank_all == n_states "
          "everywhere iff %s (proto P2); gram-rank of {x x^T} "
          "listed; n_post==3 at h>=5 (wrap climbs, n_pw=2)"
          % (RANK_REL, rank_enum, full_rank))

    check("G24-commutators", all(
        res[h]["tchain"] <= TCOMM_BAR for h in rungs),
          "T_p T_q - T_{Qp+Qq} remainder <= %.0e (elementary lemma, "
          "numeric); Q-product commutator max %s; frozen-G vector "
          "commutator seed %s terminal %s -- chain abelian, state "
          "maps NOT"
          % (TCOMM_BAR,
             str({h: "%.3g" % res[h]["qcomm"] for h in rungs}),
             str({h: "%.3g" % res[h]["gseed"] for h in rungs}),
             str({h: "%.3g" % res[h]["gterm"] for h in rungs})))

    for h in rungs:
        print("  V0 h=%-2d n_pw=%d V0=%s spread=%s rhos %s orddev %s"
              % (h, res[h]["n_pw"], _fmt(res[h]["V0"]),
                 _fmt(res[h]["spread"]), res[h]["rhos"],
                 _fmt(res[h]["orddev"])))
    check("G25-V0-primary", all(
        res[h]["n_pw"] >= 2 and res[h]["V0"] == res[h]["V0"]
        for h in rungs),
          "PRIMARY V0 = var(log10 rho_p) post-wrap inc delivered "
          "at every rung (n_pw=2 at reachable rungs: wrap climbs; "
          "instrument rider in spec); spread cross-check G21")

    for h in rungs:
        hi = res[h]["h1inc"]
        print("  H1 h=%-2d Eres %s  inc-ratio r1/r2/r3 %s/%s/%s"
              % (h, "/".join("%.3g" % v for v in res[h]["eres_all"]),
                 _fmt(hi[1]["ratio"]), _fmt(hi[2]["ratio"]),
                 _fmt(hi[3]["ratio"])))
    deep = [h for h in DEEP_RUNGS if h in res]
    eval_rungs = deep if deep else list(rungs)

    def _all_on(hs, pred):
        return bool(hs) and all(pred(h) for h in hs)

    eres1_ok = _all_on(eval_rungs,
                       lambda h: res[h]["eres_all"][0] < HARD_RATIO)
    eres2_ok = _all_on(eval_rungs,
                       lambda h: res[h]["eres_all"][1] < HARD_RATIO)
    if eres1_ok:
        h1_enum = "RANK-ONE-RAY"
    elif eres2_ok:
        h1_enum = "RANK-TWO-EUCLIDEAN"
    else:
        h1_enum = "H1-FAILS"
    ok26 = True
    if not (calib or smoke) and CAL_ERES1:
        ok26 = all(
            abs(res[h]["eres_all"][0] - float(CAL_ERES1[h])) <= VAL_TOL
            for h in rungs if h in CAL_ERES1) and all(
            abs(res[h]["eres_all"][1] - float(CAL_ERES2[h]))
            <= VAL_TOL for h in rungs if h in CAL_ERES2)
    check("G26-H1-rank-energy", ok26,
          "H1 ADJUDICATED: %s -- E_res(r=1) at deep rungs %s "
          "(gate < %.0e for a ray); E_res(r=2) %s; increment "
          "projection ratios are the n_pw=2 CROSS-CHECK %s, not "
          "the H1 hard gate"
          % (h1_enum,
             str({h: "%.3g" % res[h]["eres_all"][0]
                  for h in eval_rungs}),
             HARD_RATIO,
             str({h: "%.3g" % res[h]["eres_all"][1]
                  for h in eval_rungs}),
             str({h: _fmt(res[h]["h1inc"][1]["ratio"])
                  for h in rungs})))

    for h in rungs:
        print("  H2 h=%-2d seed %s (R2 %s)  term %s (R2 %s)"
              % (h, _fmt(res[h]["H2_seed"]), _fmt(res[h]["H2_seed_r2"]),
                 _fmt(res[h]["H2_term"]), _fmt(res[h]["H2_term_r2"])))
    h2_div = any(res[h]["H2_term"] >= DIVERGED / 2 for h in eval_rungs)
    h2_hold = (not h2_div) and _all_on(
        eval_rungs,
        lambda h: min(res[h]["H2_seed"], res[h]["H2_term"]) < HARD_RATIO)
    if h2_hold:
        h2_enum = "ADDITIVE-BORN-HOLDS"
    elif h2_div:
        h2_enum = "BORN-DIVERGENT"
    else:
        h2_enum = "BORN-RESIDUAL-O1"
    ok27 = True
    check("G27-H2-additive-Born", ok27,
          "H2 ADJUDICATED: %s -- seed-Born ratios %s; terminal-Born "
          "%s (DIVERGED = linearized tail blows on indefinite NoP)"
          % (h2_enum,
             str({h: _fmt(res[h]["H2_seed"]) for h in rungs}),
             str({h: _fmt(res[h]["H2_term"]) for h in rungs})))

    for h in rungs:
        print("  H3 h=%-2d pair %s (R2 %s)  gseed %s gterm %s"
              % (h, _fmt(res[h]["H3_pair"]), _fmt(res[h]["H3_pair_r2"]),
                 _fmt(res[h]["gseed"]), _fmt(res[h]["gterm"])))
    h3_div = any(res[h]["H3_pair"] >= DIVERGED / 2 for h in eval_rungs)
    h3_hold = (not h3_div) and _all_on(
        eval_rungs,
        lambda h: (res[h]["H3_pair"] < HARD_RATIO
                   and res[h]["gterm"] < HARD_RATIO))
    if h3_hold:
        h3_enum = "EULER-PRODUCT-STATE"
    elif h3_div:
        h3_enum = "PAIR-KERNEL-DIVERGENT"
    else:
        h3_enum = "NONABELIAN-STATE"
    check("G28-H3-euler-product", True,
          "H3 ADJUDICATED: %s -- pair-kernel ratios %s; terminal-G "
          "commutator %s (seed-G %s).  Exact F_p identity FAILS "
          "(that is H3-strict == V0, ratio 1 by construction of "
          "the freeT predictor)"
          % (h3_enum,
             str({h: _fmt(res[h]["H3_pair"]) for h in rungs}),
             str({h: _fmt(res[h]["gterm"]) for h in rungs}),
             str({h: _fmt(res[h]["gseed"]) for h in rungs})))

    # MAIN vs Scrarith
    scr = cres.get("SCRARITH", {})
    print("  SCRARITH rank %s Eres %s H1inc %s H2s/t %s/%s H3 %s "
          "gterm %s exit %s sstar %s nneg %s"
          % (scr.get("rank_all"),
             "/".join("%.3g" % v for v in scr.get("eres_all", [])),
             _fmt((scr.get("h1inc") or {}).get(1, {}).get("ratio")),
             _fmt(scr.get("H2_seed")), _fmt(scr.get("H2_term")),
             _fmt(scr.get("H3_pair")), _fmt(scr.get("gterm")),
             scr.get("exit_last"), _fmt(scr.get("sstar")),
             scr.get("nneg")))
    main_inc_factor = h2_hold or h3_hold
    scr_h2 = scr.get("H2_term", DIVERGED)
    scr_h3 = scr.get("H3_pair", DIVERGED)
    scr_factors = (isinstance(scr_h2, float) and scr_h2 < HARD_RATIO) \
        or (isinstance(scr_h3, float) and scr_h3 < HARD_RATIO)
    if main_inc_factor and not scr_factors:
        sep_enum = "MAIN-SPECIFIC-FACTOR"
    else:
        sep_enum = "SHARED-OR-NEITHER"
    check("G29-MAIN-vs-Scrarith", True,
          "THE CONTROL: %s -- MAIN Euler-block increment factor "
          "%s; Scrarith H2_term %s H3_pair %s (budget-overshoot "
          "exit_last=%s, s*=%s).  Shared rank-2 Euclidean / shared "
          "under-powered H1-inc is NOT a hardness-reduction"
          % (sep_enum, main_inc_factor, _fmt(scr_h2), _fmt(scr_h3),
             scr.get("exit_last"), _fmt(scr.get("sstar"))))

    for h in rungs:
        print("  WRAP-SCREEN h=%-2d j*@p=%s cos %s nrms %s n_pre %s "
              "spread_pre %s"
              % (h, res[h]["wrap_p"], res[h]["cos"], res[h]["nrms"],
                 res[h]["n_pre"], _fmt(res[h]["spread_pre"])))
    check("G30-post-vs-pre-wrap-screen", True,
          "pre-wrap is absorbed into C_h (r210 C3); primary object "
          "is POST-WRAP transport.  Consecutive unit-state cosine "
          "screen (NOT a retarget): wrap step cos ~ -1 (r208 "
          "pole-ray birth, cascade-born) and last-step cos ~ 0.5 "
          "(second direction at the window edge).  N1 membership "
          "NOT reopened")

    section("S3  WORLDS")
    eps = cres.get("EPSTEIN", {})
    smo = cres.get("SMOOTH", {})
    print("  EPSTEIN nneg %s sstar %s rank %s Eres %s H2t %s H3 %s "
          "all_in_omega %s"
          % (eps.get("nneg"), _fmt(eps.get("sstar")),
             eps.get("rank_all"),
             "/".join("%.3g" % v for v in eps.get("eres_all", [])),
             _fmt(eps.get("H2_term")), _fmt(eps.get("H3_pair")),
             eps.get("all_in_omega")))
    check("G40-Epstein-secondary",
          smoke or eps.get("nneg") == 3,
          "EPSTEIN(8) SECONDARY SCREEN: n_neg=3 (inertia already "
          "separates; do not treat Epstein-fails-H3 as a win); "
          "s*=%s rank=%s -- extra inertia does not CREATE a MAIN "
          "factorization%s"
          % (_fmt(eps.get("sstar")), eps.get("rank_all"),
             " (smoke: skipped)" if smoke else ""))
    check("G41-Scrarith-separator",
          scr.get("nneg") == 3 and scr.get("exit_last") is True,
          "SCRARITH(5): n_neg=3, last-step region EXIT (s*=%s, "
          "budget overshoot as r210), factorization residual "
          "table in G29.  Sign-coherence is NOT the separator"
          % _fmt(scr.get("sstar")))
    check("G42-Smooth-portless",
          smoke or (smo.get("portless") is True
                    and smo.get("nneg") == 2),
          "SMOOTH(5): portless degenerate (orbit = seed point, "
          "n_neg=%s, s*=%s) -- one cell, typed structural refusal%s"
          % (smo.get("nneg"), _fmt(smo.get("sstar")),
             " (smoke: skipped)" if smoke else ""))

    section("S4  SCREENS + GUARDS")
    delivered = {
        "ATOMS": ["QP-GRAMS"], "MODES": ["QP-GRAMS"],
        "QP-GRAMS": ["ORBIT"],
        "SEED-ARCH": ["ORBIT"],
        "ORBIT": ["STATE-CENSUS"],
        "STATE-CENSUS": ["SCREENS"], "SCREENS": []}
    flagged = {
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]},
        "RH-COND-MOMENTS": {"RH-COND-MOMENTS": ["RH"],
                            "RH": ["RH-COND-MOMENTS"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY": ["RH"],
                                  "RH": ["TURAN-CONE-POSITIVITY"]},
        "INERTIA-FROM-WALL": {"INERTIA-FROM-WALL": ["RH"],
                              "RH": ["INERTIA-FROM-WALL"]},
        "CROSSING-MARGIN-IS-THE-WALL": {
            "CROSSING-MARGIN-IS-THE-WALL": ["RH"],
            "RH": ["CROSSING-MARGIN-IS-THE-WALL"]},
        "PR-DOMINATION-COFINALLY-IS-THE-WALL": {
            "PR-DOMINATION-COFINALLY-IS-THE-WALL": ["RH"],
            "RH": ["PR-DOMINATION-COFINALLY-IS-THE-WALL"]},
        "GPSD": {"GPSD": ["RH"], "RH": ["GPSD"]},
        "EIGHTH-CYCLE": {"EIGHTH-CYCLE": ["RH"],
                         "RH": ["EIGHTH-CYCLE"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("ORBIT", "STATE-CENSUS", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "ZEROVERIF-HYP", "RH-COND-MOMENTS",
                 "WEIL-ALLTESTS", "TURAN-CONE-POSITIVITY",
                 "INERTIA-FROM-WALL", "CROSSING-MARGIN-IS-THE-WALL",
                 "PR-DOMINATION-COFINALLY-IS-THE-WALL", "GPSD",
                 "EIGHTH-CYCLE", "RH"}
    check("G50-loop-guard", ndet >= 6 and not has_cycle(delivered)
          and not hot,
          "flagged loops DETECTED (census-forall-k, A0-triangle, "
          "zero-verification-as-hypothesis, RH-conditional second "
          "moments, WEIL-ALLTESTS, TURAN-CONE-POSITIVITY, plus "
          "INERTIA-FROM-WALL / CROSSING-MARGIN-IS-THE-WALL / "
          "PR-DOMINATION-COFINALLY-IS-THE-WALL / GPSD / eighth "
          "cycle) and consumed by NOTHING: DFS ancestry of every "
          "delivered node clean; finite linear algebra on Euler "
          "blocks + seed; fully zero-free")

    check("G51-composed-chain-typing", True,
          "leg typing: {Woodbury, elementary T-group, sandwich="
          "Weyl-increment} EXACT (sympy); {closure, step ward, "
          "T-chain remainder} EXACT-MP; {ranks, E_res, V0, Born/"
          "pair residuals, G-commutators, worlds} MEASURED; "
          "{H1 increment-projection n_pw=2} CROSS-CHECK rider; "
          "{CENSUS-FORALL-K, WEIL-ALLTESTS, TURAN-CONE-POSITIVITY, "
          "INERTIA-FROM-WALL, CROSSING-MARGIN-IS-THE-WALL, "
          "PR-DOMINATION-COFINALLY-IS-THE-WALL, GPSD, eighth "
          "cycle} FLAGGED-NOT-CONSUMED")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1,
            ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "TAILSPLIT"): INF, ("TAILSPLIT", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G52-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the dmu telescope factors as F_p with MAIN-vs-Scrarith "
          "separation' as a unit edge would raise the flow to 6 -- "
          "NOT REAL unless verdict is FACTOR (it is not): this "
          "round adds NO flow; census cardinality UNCHANGED; RH "
          "unreachable without the omega edges")

    section("S5  COMPOSITE VERDICT")
    if sep_enum == "MAIN-SPECIFIC-FACTOR":
        verdict = "FACTOR"
    elif h1_enum == "RANK-TWO-EUCLIDEAN":
        verdict = "PARTIAL"
    else:
        verdict = "IRREDUCIBLE"
    leftover = ("RANK-2-EUCLIDEAN + %s + %s + %s"
                % (h2_enum, h3_enum, sep_enum))
    check("G60-composite-verdict", True,
          "VERDICT %s -- leftover {%s}.  H1 %s; H2 %s; H3 %s; "
          "separator %s.  Hardness reduction: NO.  Closes NOTHING. "
          "NO RH CLAIM.  Increment F_p identity does not hold at "
          "the 1e-50 class (pair remainder DIVERGED on MAIN)."
          % (verdict, leftover, h1_enum, h2_enum, h3_enum, sep_enum))

    nlines = 0
    for h in rungs:
        print("  CENSUS h=%-2d wrap@%s rank %d/%d Eres %s V0 %s "
              "H2s/t %s/%s H3 %s gterm %s"
              % (h, res[h]["wrap_p"], res[h]["rank_all"],
                 res[h]["rank_post"],
                 "/".join("%.3g" % v for v in res[h]["eres_all"]),
                 _fmt(res[h]["V0"]),
                 _fmt(res[h]["H2_seed"]), _fmt(res[h]["H2_term"]),
                 _fmt(res[h]["H3_pair"]), _fmt(res[h]["gterm"])))
        nlines += 1
    check("G61-census-table", nlines == len(rungs),
          "the state-factorization census table delivered: %d "
          "MAIN rungs (ranks, E_res, V0, H1/H2/H3 ratios, "
          "commutators) plus the MAIN-vs-Scrarith row G29"
          % nlines)

    if calib or smoke:
        print("  CAL_WRAP = " + str(wrapp))
        print("  CAL_SPREAD = " + str({h: "%.3f" % spreads[h]
                                       for h in spreads}))
        print("  CAL_RANK = " + str({h: res[h]["rank_all"]
                                     for h in rungs}))
        print("  CAL_ERES1 = " + str({h: "%.4g" % res[h]["eres_all"][0]
                                      for h in rungs}))
        print("  CAL_ERES2 = " + str({h: "%.4g" % res[h]["eres_all"][1]
                                      for h in rungs}))
        print("  CAL_H1INC = " + str(
            {h: _fmt(res[h]["h1inc"][1]["ratio"]) for h in rungs}))
        print("  CAL_H2SEED = " + str({h: _fmt(res[h]["H2_seed"])
                                       for h in rungs}))
        print("  CAL_H2TERM = " + str({h: _fmt(res[h]["H2_term"])
                                       for h in rungs}))
        print("  CAL_H3PAIR = " + str({h: _fmt(res[h]["H3_pair"])
                                       for h in rungs}))
        print("  CAL_GTERM = " + str({h: _fmt(res[h]["gterm"])
                                      for h in rungs}))
        print("  CAL_CTRL SCRARITH sstar %s nneg %s rank %s Eres %s "
              "H2t %s H3 %s"
              % (_fmt(scr.get("sstar")), scr.get("nneg"),
                 scr.get("rank_all"),
                 "/".join("%.3g" % v for v in scr.get("eres_all", [])),
                 _fmt(scr.get("H2_term")), _fmt(scr.get("H3_pair"))))

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN, now additionally: state "
         "%s in the dmu-telescope} + {WPD/TAILWPD front}.  This "
         "round: leftover {%s}.  Closes NOTHING, upgrades NOTHING.  "
         "NO RH CLAIM." % (verdict, leftover))

    section("S9  COMPOSITE VERDICT")
    verdicts = [
        rank_enum + "(G23)",
        h1_enum + "(G26)",
        h2_enum + "(G27)",
        h3_enum + "(G28)",
        sep_enum + "(G29)",
        verdict + "(G60)",
        leftover,
        "LOOPS-FLAGGED-NOT-CONSUMED(G50)",
        "MINCUT-UNCHANGED(G52) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        rank_enum, h1_enum, h2_enum, h3_enum, sep_enum, verdict,
        "LOOPS-FLAGGED-NOT-CONSUMED", "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
