#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mangoldt_ablation_ladder_probe -- MANGOLDT.ABLATION.LADDER.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  EXPLORATORY MECHANISM
ROUND.  This probe writes no verification module, paper, ledger,
website, manifest, Lean file or status marker.  It makes NO RH claim
in any direction and NO numerology claim.  It closes no gate and
narrows no gate.  It is a mechanistic CHARACTERIZATION of the two
arithmetic signatures the prime front measures -- every verdict below
is numbers-only.

=======================================================================
MISSION (mechanism round: MANGOLDT.ABLATION.LADDER.01).  Round 184
(pi_pattern_scan_probe, SPEC 00fc85173fe07470) established that the
mass-location world separator is PRIME-SPECIFIC: all pi-derived combs,
e/sqrt2/phi/Champernowne/Liouville and 80 null seeds land TOP-HEAVY,
while the true von Mangoldt comb TAIL-RIDES (S1, the r181 one-dex-per-
rung signature) and shows extreme D2 spike coherence (S2: C = 131.04
vs INTRAND null max 12.60).  THIS round asks the causal question:
WHICH MINIMAL MATHEMATICAL PROPERTY of the von Mangoldt comb generates
S1 and S2?  We build a property ladder from randomness to Mangoldt,
change ONE property per world, and locate exactly where each signature
switches on -- plus subtractive ablations from the true comb (one
property removed each) for the necessity direction.  PREDEFINITION IS
THE RULE: every construction, seed map, bar and class boundary below
is frozen BEFORE any record evaluation; amendments are disclosed in
the AMENDMENT block at the bottom of this spec.  The headline question
answered with numbers: DOES W4 (Beurling multiplicativity, no true
zero coupling) TAIL-RIDE?  If yes, multiplicativity + the weight
grammar is sufficient and the signature is NOT zero-coupled; if no,
the signature needs the true comb's coupling to the explicit-formula
layer.  Either outcome is typed honestly.
=======================================================================
State consumed (CITED, read-only): r184/DIV pi_pattern_scan_probe
(SPEC 00fc85173fe07470): the ported instrument code paths VERBATIM --
the Mprime/build_cell port (record dev 8.4e-59, port gate 1e-25), the
r182 w_ctrl anchor comparator (record dev <= 0.004), the D1 mass-
location ladder, the D2 Landau-spike instrument, the r182 alt-jet
recipes; and the r184 RECORD NUMBERS this round must replicate as its
transfer-validity anchor: MANGOLDT D1 ladder log10tail (-4.11, -2.26,
-1.41, -0.49, -0.04) class TAIL-RIDING; C_MANG = 131.04 vs INTRAND
null max 12.60; MANGOLDT alt-jets at h=8 (SIGNFLIP -12.84, UNIFORM
-13.08, MAGSCRAM -13.43) vs MAIN -0.04.  r182/D alignment_law_probe
(SPEC e4cdb9a932093196: CTRL-anchor record strings CAL_CTRL_TAIL MAIN
{4: -4.11, 5: -2.26, 8: -0.04}, CAL_CTRL_LOC MAIN topshare/mu_m
{4: (0.0041, -4.1), 5: (0.0098, -8.3), 8: (0.0082, -13.2)}; the law
needs the JOINT exact sign-and-magnitude structure of the ray d).
r181/CDXCIX cbj_subdof_probe (SPEC 2db82c76ce5f067c: the 1e-12
primary cut; the fraction ladder as world separator).  r180/CDXCVII
cbj_frame_probe (the house Gram mu(g) = sin^2(ag)/g^2, psi_k =
g^2/(g^2 - b_k)).  r174 spike instrument class (Landau 1912 Math.
Ann. 71, 548-564: sum_{0<gamma<=T} x^rho = -(T/2pi) Lambda(x) +
O(log T) for fixed x > 1, UNCONDITIONAL; Gonek 1993 Contemp. Math.
143, 395-413).  R4 = radius4_an_probe build_cell (r122 machinery;
MAIN = prime-power atoms (log q, log p/sqrt q), even sector).
CLASSICAL CONSTRUCTIONS CITED: Cramer 1936 random-prime model (Acta
Arith. 2, 23-46): integer n >= 2 kept independently with probability
min(1, 1/ln n) (n = 2 has 1/ln 2 = 1.44 > 1, hence always kept --
disclosed).  Beurling generalized prime systems: Beurling 1937 (Acta
Math. 68, 255-291); Diamond-Zhang, Beurling Generalized Numbers, AMS
Math. Surveys and Monographs 213 (2016).  Random Beurling systems in
this density class generically do NOT inherit the Riemann zero
structure -- their associated Beurling zeta has its own zeros, and
systems with zeros off the critical line exist in the same counting
class (Diamond-Montgomery-Vorhauer, Math. Ann. 334 (2006), 1-36).
The W4 rung therefore carries density + log weights + powers + FULL
multiplicative structure with NO coupling to the Riemann zeros.

NOTATION (r180/r181/r182/r184 conventions VERBATIM).  Rung h; a =
log(h)/2; L2v = 2a; K = ceil(1.25 h log h); om_k = k pi/a; b_k =
om_k^2; even sector.  WALL M = Mpole + March - Mprime where the world
enters ONLY through its comb atoms {(u_j, w_j)} via pj_i = sum_j w_j
sin(om_i u_j) (off-diagonal) and the psi_d diagonal sums (build_cell
even-sector recipe, ported verbatim, PORT-GATED on the MANGOLDT world
at dev <= 1e-25).  Source c = lowest eigenvector of M (sign-fixed,
/nrm); d_k = (-1)^k c_k; A_0 = sum d; J = d/A_0.  GRAM (world-blind):
mu(g) = sin^2(ag)/g^2, psi_k(g) = g^2/(g^2 - b_k), Gm over ward
ordinates in (2 pi h + 6, gamma_CTRL_NZ], CTRL_NZ = 300; D =
sqrt(diag Gm); Gn = D^-1 Gm D^-1; Jn_k = J_k D_k / sqrt(sum mu);
eigsy(Gn) at EIG_DPS = ndig + 30; s_i = v_i . Jn; m_i = lam_i s_i^2;
mass ward <= 1e-6.  OBSERVABLES per world per rung: log10tail at the
primary 1e-12 cut, topshare, mu_m, gmin.  LADDER: HRUNGS = (4, 5, 6,
7, 8); DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80}.  L1 SCALE ANCHOR
(r184): every D1 comb is L1-rescaled to W1_MAIN(h) = sum_{q <= h}
Lambda(q)/sqrt q so every world perturbs the wall in the same
operator-norm regime.  MATCHED SIZES: the stochastic worlds carry
atom counts matched to the true comb's (W0 exactly NPP(h) = #prime
powers <= h; W1-W4 by construction, their density IS the matched
property).  SPIKE DEPTH: positions u in [0.5, 8.0], integer cutoff
X_SPIKE = 2980 = floor(e^8) (the r184 MANGOLDT spike comb VERBATIM).

=======================================================================
THE WORLD REGISTRY (ALL FROZEN; one construction per world; seed maps
below are exhaustive -- no reseeding, no reruns)
=======================================================================
ADDITIVE LADDER (bottom-up, one property added per rung):
  W0 RAND      20 seeds.  D1: rng([300, s, h]); NPP(h) atoms,
               positions uniform(0, L2v), weights N(0, 1).  D2:
               rng([310, s]); N_sp atoms (N_sp = the MANGOLDT spike
               comb size), positions uniform(0.5, 8.0), weights
               N(0, 1).  The null band.
  W1 +DENSITY  Cramer model.  Per seed s the set S_s = {n in
               [2, 2980]: u_n < min(1, 1/ln n)}, u_n from
               rng([500, s]), drawn ONCE per seed at full depth;
               D1 rung h uses S_s intersect [2, h].  Unit weights,
               no powers.  20 seeds.
  W2 +LOGWEIGHT  the SAME sets S_s; weights ln n / sqrt n (the
               Mangoldt weight law on fake positions).
  W3 +POWERS   the SAME sets S_s as fake primes WITH their exact
               power towers: for p in S_s, atoms at q = p^k <=
               cutoff with weight ln p / sqrt q (the full Mangoldt
               weight grammar on fake primes).
  W4 +MULTIPLICATIVITY  Beurling generalized prime systems, 8
               systems t = 0..7.  Generators: inhomogeneous Poisson
               process with intensity 1/ln x on [2, 2980] (per
               integer cell [n-1/2, n+1/2) clamped below at 2.0,
               lam = width/ln n, positions uniform in the cell;
               rng([1000, t])).  Comb = the exact Beurling-Mangoldt
               weights: Lambda_B is supported on generator powers
               (exactly as classical Lambda is supported on prime
               powers): atoms (k ln g, ln g / sqrt(g^k)) for
               g^k <= cutoff.  The full multiplicative semigroup
               enters the construction class and the sanity gate:
               N_B(1000)/1000 in [0.2, 5.0] per system (DFS count of
               all generator-power products <= 1000, cap 12000;
               cap-hit = gate FAIL).  NO Riemann-zero coupling.
  W5 MANGOLDT  the true comb, R4.build_cell MAIN atoms VERBATIM
               (markers -> mp-exact (log q, log p/sqrt q) inside
               assemble_mprime; port gate 1e-25).  THE POSITIVE
               CONTROL; must replicate the r184 record numbers.
SUBTRACTIVE/TRANSPLANT ABLATIONS (top-down from true Mangoldt, one
property removed each):
  A1 -POWERS   true primes only (Lambda restricted to k = 1):
               atoms (ln p, ln p / sqrt p), p prime <= cutoff.
  A2 -LOGWEIGHT  unit weights at the true prime-power positions.
  A3 -POSITIONS  the true Mangoldt weight sequence (in q-order)
               transplanted onto the Cramer positions S_s in
               position order, cycled when sizes differ (w_i =
               w_true[i mod m]; disclosed); 20 seeds (same S_s).
  A4 -SIGNS/-PHASES  the r182 alt-jet battery (SIGNFLIP / UNIFORM /
               MAGSCRAM, golden permutation, projective Dg-recovery
               scal_k = Jn_k A0/d_k) on the TRUE comb at rungs
               (4, 8) -- known to kill; replicated as the anchor.
  A5 GRID-JITTER  true positions jittered: u = ln q + eps_j, eps_j
               uniform(-eps, eps), true weights; EPS = (0.01, 0.05,
               0.20) (three frozen scales; the true-position log-q
               spacing at h = 8 is ~0.13), 5 seeds each;
               rng([400, ei, s, h]) for D1, rng([410, ei, s]) for
               D2; clamped to [0.02, L2v] (D1) / [0.5, 8.0] (D2),
               disclosed.
EMPTY-RUNG RULE (frozen): an instance with zero atoms at any D1 rung
(possible only for W4 at small h: a system may have no generator
<= 4) is excluded from level aggregation and counted in G11.
A0-GUARD RULE: |A0| < 1e-40 -> instance excluded and counted (G11).

=======================================================================
THE DETECTOR BATTERY (frozen bars)
=======================================================================
D1 MASS-LOCATION (primary; r184 verbatim).  Per instance per rung:
log10tail at the 1e-12 cut, topshare, mu_m.  CLASSIFICATION (frozen;
the r184 boundaries plus the NEW predefined INTERMEDIATE class,
because ablation worlds may land between):
  TAIL-RIDING   log10tail(4) >= -6.0 AND log10tail(8) >= -0.5 AND
                ladder non-decreasing with slack 0.05;
  TOP-HEAVY     log10tail(h) <= -8.0 at ALL rungs;
  INTERMEDIATE  anything else (reported with numbers).
LEVEL AGGREGATION (frozen): majority class over valid instances
(strict majority of the valid count); representative numbers = the
medians over valid instances (T8 = median log10tail(8), T4 = median
log10tail(4)).  S1-ON(level) := majority class is TAIL-RIDING.
D2 SPIKE COHERENCE (r174/r184 Landau instrument).  Z(u) = sum_{gamma
in n7000 cache} cos(gamma u) (float64, disclosed); grid 4096 points
on [0.5, 8.0] for mean(Z^2).  Per instance: coherence C = |sum_j w_j
Z(u_j)| / sqrt(sum w_j^2 * mean(Z^2)) against its OWN seeded null
band: 20 scrambles of the SAME positions (magnitudes permuted, signs
randomized; rng([777, code, key, s]) with the frozen family codes
W0..W5 = 0..5, A1 = 11, A2 = 12, A3 = 13, A5e0/1/2 = 15/16/17).
W5's band is the r184 INTRAND recipe VERBATIM (rng(10000 + s)) so the
record null max 12.60 replicates exactly.  For W4 the spike test
points are the system's OWN generator powers (predefined per system).
STATISTIC R = C / max(own band).  S2-ON iff R >= 10.0 (the r184
MANGOLDT-FIRES ratio; the record gives W5 R = 131.04/12.60 = 10.40);
S2-WEAK iff 1.25 <= R < 10.0; S2-OFF else.  Level = median R over
valid instances; S2-ON(level) iff median R >= 10.0.
D3 ALT-JET RESPONSE OF THE FIRST S1 WORLD (cheap, predefined): on the
lowest additive level BELOW W5 that is S1-ON (its first TAIL-RIDING
instance) and on EVERY ablation level that KEEPS S1: the SIGNFLIP
alt-jet at h = 8; the signature "dies like the true comb's" iff the
SIGNFLIP tail <= -8.0.  Vacuous (disclosed as such) if no such level.
DIAGNOSTIC (measured, no bar): for the integer-support worlds
(W1/W2/W3/A3) the fraction of atoms sitting on TRUE prime-power
integers at spike depth, and the rank correlation (Spearman) between
that fraction and R pooled over W1+W2+W3 -- quantifies how much of
any partial S2 response is carried by accidental overlap with the
true support.

=======================================================================
TRANSFER VALIDITY + TRANSITION ADJUDICATION (all frozen)
=======================================================================
TRANSFER VALIDITY (W5 must replicate round 184): (i) G12: the W5 D1
ladder replicates (-4.11, -2.26, -1.41, -0.49, -0.04) within 0.10
abs per rung AND classifies TAIL-RIDING; (ii) G15/G16/G17: the r182
w_ctrl anchor comparator replicates the record strings at x = 4/5/8
(tail tol 0.10, topshare tol 5e-2, mu_m tol 0.2); (iii) G18:
|C_MANG - 131.04| <= 0.5 AND |own-band max - 12.60| <= 0.5;
(iv) G20: the A4 alt-jets all relocate to the top (log10tail <= -8.0
at h = 8 while MAIN >= -0.5).
TRANSITION (per signature Sk): ON-set = {levels with Sk-ON} in the
frozen order W0 < W1 < W2 < W3 < W4 < W5.  LOCATED iff the ON-set is
non-empty and upward-closed (a clean switch level L*).  SHARPNESS:
S1 SHARP iff medT8(L*) - medT8(prev level) >= 6.0 dex, else GRADUAL;
S2 SHARP iff medR(L*) / medR(prev level) >= 10.0, else GRADUAL.
NECESSITY (subtractive): an ablation KILLS S1 iff its majority class
is not TAIL-RIDING; KILLS S2 iff its median R < 10.0.  Tokens
NECESSARY-<POWERS|LOGWEIGHT|POSITIONS|SIGNS|EXACT-POSITIONS(eps)>
are emitted for each ablation that kills (A5: the smallest frozen
eps that kills gives the position-sharpness scale).
HEADLINE: DOES-W4-TAIL-RIDE = YES iff level W4 is S1-ON (with
numbers either way).
PROPERTY NAMES (frozen map): W1 DENSITY, W2 LOGWEIGHT, W3
POWER-GRAMMAR, W4 MULTIPLICATIVITY, W5 TRUE-POSITIONS/ZERO-COUPLING.

HONEST OUTCOME TAXONOMY (frozen adjudication; verdict gates are
DEFINITIONAL/ADJUDICATION per the house convention):
  INSTRUMENT-LIMITED    transfer validity fails (any of G12, G15-17,
                        G18, G20) -- matched-size transfer too
                        shallow; disclosed with depths.
  Per signature Sk:
    Sk-ZERO-COUPLED         ON-set = {W5} and A3 (-POSITIONS) kills:
                            the signature needs the true comb's
                            positions -- an explicit-formula
                            phenomenon on the source side.
    Sk-SUFFICIENT-AT-Wj     located switch at Wj < W5: the property
                            stack up to Wj creates the signature
                            without true zero coupling.
    Sk-DIFFUSE              ON-set not upward-closed (no single
                            property carries it).
  Overall: MECHANISM-LOCATED(S1@<level>, S2@<level>, sharp/gradual
  each) iff both signatures LOCATED; MECHANISM-DIFFUSE otherwise
  (with the per-level table).  Plus the necessity tokens, SHARP/
  GRADUAL adjudications, NO-RH-CLAIM, NO-NUMEROLOGY-CLAIM.
Bars: mass ward <= 1e-6; |A0| >= 1e-40; port gates <= 1e-25; runtime
<= 2700 s.

AMENDMENT BLOCK (disclosed at freeze; house protocol):
  A0 (pre-freeze, disclosed design choices; no alternative evaluated
  before or after freezing): (i) Cramer keeps n = 2 always
  (1/ln 2 > 1); (ii) the W4 comb is the Lambda_B support (generator
  powers) EXACTLY as the classical Lambda is supported on prime
  powers -- the full semigroup enters through the construction class
  and the N_B sanity gate, not through extra comb atoms (Lambda_B
  vanishes off generator powers by definition); (iii) the A3 cycling
  rule w_i = w_true[i mod m] in position order; (iv) the A5 clamp
  windows; (v) matched sizes = the true comb's atom counts (W0
  exact, W1-W4 by density construction); (vi) the seed maps in the
  registry are exhaustive; (vii) no A/B data-halves this round --
  the constructions are not data streams, seed replication (20/8/5
  instances per stochastic level) replaces the holdout; W5/A1/A2
  are deterministic single instances (as in r184's MANGOLDT).
  A1 (at freeze): smoke1 (pre-freeze SPEC_SHA d5a66f2f1104baaf,
  26/26, 13.3 s, log kept) passed with NO code, bar, gate,
  construction, seed or boundary change -- the only edit between
  smoke1 and the record run is THIS disclosure paragraph itself;
  smoke2 re-runs the sealed spec (log kept).  All bars, class
  boundaries, seed maps and the taxonomy rule above stood BEFORE
  smoke1 and were not moved.  Measured smoke note kept for the
  record (no action): at the smoke ladder (h = 4..5) one W3 seed
  and one A3 seed reproduce the true comb exactly (their Cramer set
  intersected with [2, 5] equals the true prime-power set) -- the
  predicted accidental-overlap channel; the full h = 4..8 ladder
  and the seed-majority aggregation are the predefined guards.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import statistics
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
Z_OVERHANG = 6.0
CTRL_NZ = 300
CUT_PRIMARY = "1e-12"
MASS_WARD = 1e-6
A0_GUARD = 1e-40
RUNTIME_BAR = 2700.0
GOLD = 0.6180339887498949
EIG_PAD = 30
NDIG_CAP = 140
PORT_TOL = 1e-25

HRUNGS = (4, 5, 6, 7, 8)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80}
NSEED = 20
NSYS = 8
JIT_EPS = (0.01, 0.05, 0.20)
NJIT = 5
X_SPIKE = 2980                    # floor(e^8), r184 spike cutoff

# r182 anchor record strings (CITED, r184 G17)
ANCHOR_X = (4, 5, 8)
ANCHOR_DPS = 60
CAL_CTRL_TAIL = {4: "-4.11", 5: "-2.26", 8: "-0.04"}
CAL_CTRL_LOC = {4: ("0.0041", "-4.1"), 5: ("0.0098", "-8.3"),
                8: ("0.0082", "-13.2")}
ANCHOR_TAIL_TOL = 0.10
ANCHOR_TOP_TOL = 5e-2
ANCHOR_MUM_TOL = 0.2

# r184 record numbers to replicate (transfer validity)
R184_LADDER = {4: -4.11, 5: -2.26, 6: -1.41, 7: -0.49, 8: -0.04}
R184_LADDER_TOL = 0.10
R184_CMANG = 131.04
R184_INTRAND = 12.60
R184_D2_TOL = 0.5

# D1 classification bars (r184 frozen + INTERMEDIATE)
TAILRIDE_LO4 = -6.0
TAILRIDE_HI8 = -0.5
LADDER_SLACK = 0.05
FAKE_BAR = -8.0

# D2 spike instrument (frozen)
SPIKE_LO, SPIKE_HI = 0.5, 8.0
SPIKE_GRID_N = 4096
S2_ON_RATIO = 10.0
S2_WEAK_RATIO = 1.25
NNULL = 20

# transition adjudication (frozen)
SHARP_DEX = 6.0
SHARP_RATIO = 10.0

# Beurling semigroup sanity (frozen)
SG_X = 1000
SG_CAP = 12000
SG_BAND = (0.2, 5.0)
GEN_BAND = (0.8, 1.2)
CRAMER_BAND = (0.85, 1.15)

# alt-jets (r182 recipes verbatim)
ALT_TAGS = ("SIGNFLIP", "UNIFORM", "MAGSCRAM")
ALT_RUNGS = (4, 8)
ALT_FAKE_BAR = -8.0

LEVELS = ("W0", "W1", "W2", "W3", "W4", "W5")
ABL_LEVELS = ("A1", "A2", "A3", "A5e0", "A5e1", "A5e2")
PROP_NAME = {"W1": "DENSITY", "W2": "LOGWEIGHT", "W3": "POWER-GRAMMAR",
             "W4": "MULTIPLICATIVITY",
             "W5": "TRUE-POSITIONS/ZERO-COUPLING"}
ABL_PROP = {"A1": "POWERS", "A2": "LOGWEIGHT", "A3": "POSITIONS",
            "A5e0": "EXACT-POSITIONS(0.01)",
            "A5e1": "EXACT-POSITIONS(0.05)",
            "A5e2": "EXACT-POSITIONS(0.20)"}
FAM_CODE = {"W0": 0, "W1": 1, "W2": 2, "W3": 3, "W4": 4, "W5": 5,
            "A1": 11, "A2": 12, "A3": 13,
            "A5e0": 15, "A5e1": 16, "A5e2": 17}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")
META_N7000 = os.path.join(HERE, "verified_zeros_n7000_meta.json")

CHECKS: list = []
INFO: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load only in "
                       "ward_; no verification/ import")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_meta_ok() -> bool:
    return os.path.isfile(CACHE_N7000) and os.path.isfile(META_N7000)


# ==================================================== construction layer
def mangoldt_atoms_f(hi: int) -> list:
    """(log q, Lambda(p)/sqrt q) float prime-power atoms, q <= hi."""
    comp = np.zeros(hi + 1, dtype=bool)
    out = []
    for p in range(2, hi + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= hi:
            out.append((math.log(q), math.log(p) / math.sqrt(q)))
            q *= p
    out.sort()
    return out


def primes_upto(hi: int) -> list:
    comp = np.zeros(hi + 1, dtype=bool)
    out = []
    for p in range(2, hi + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        out.append(p)
    return out


def w1_main(h: int) -> float:
    return sum(w for _u, w in mangoldt_atoms_f(int(math.floor(h))))


def cramer_set(s: int) -> list:
    """the frozen Cramer draw at full depth: n in [2, X_SPIKE] kept
    with prob min(1, 1/ln n); rng([500, s])."""
    rng = np.random.default_rng([500, s])
    ns = np.arange(2, X_SPIKE + 1)
    u = rng.random(len(ns))
    keep = u < np.minimum(1.0, 1.0 / np.log(ns))
    return ns[keep].tolist()


def towers(ps: list, cutoff: float) -> list:
    """fake-prime power-tower atoms (ln q, ln p / sqrt q), q = p^k
    <= cutoff."""
    out = []
    for p in ps:
        if p > cutoff:
            break
        q = p
        while q <= cutoff:
            out.append((math.log(q), math.log(p) / math.sqrt(q)))
            q *= p
    out.sort()
    return out


def beurling_gens(t: int) -> list:
    """generators of Beurling system t: inhomogeneous Poisson,
    intensity 1/ln x on [2, X_SPIKE] via integer cells; rng([1000, t])."""
    rng = np.random.default_rng([1000, t])
    gens = []
    for n in range(2, X_SPIKE + 1):
        lo = max(2.0, n - 0.5)
        hi = n + 0.5
        lam = (hi - lo) / math.log(n)
        k = int(rng.poisson(lam))
        for _ in range(k):
            gens.append(lo + float(rng.random()) * (hi - lo))
    gens.sort()
    return gens


def beurling_atoms(gens: list, cutoff: float) -> list:
    """Beurling-Mangoldt comb: atoms (k ln g, ln g / sqrt(g^k)),
    g^k <= cutoff (Lambda_B supported on generator powers)."""
    out = []
    for g in gens:
        if g > cutoff:
            break
        q = g
        k = 1
        while q <= cutoff:
            out.append((k * math.log(g), math.log(g) / math.sqrt(q)))
            q *= g
            k += 1
    out.sort()
    return out


def semigroup_count(gens: list, X: float, cap: int) -> tuple:
    """DFS count of all products of generator powers <= X (multisets
    in nondecreasing index order); returns (count, cap_hit)."""
    gs = [g for g in gens if g <= X]
    cnt = 0
    stack = [(0, 1.0)]
    while stack:
        i, prod = stack.pop()
        for j in range(i, len(gs)):
            v = prod * gs[j]
            if v > X:
                break
            while v <= X:
                cnt += 1
                if cnt >= cap:
                    return cnt, True
                stack.append((j + 1, v))
                v *= gs[j]
    return cnt, False


def l1_rescale(atoms: list, W1: float) -> list:
    s1 = sum(abs(w) for _u, w in atoms)
    if s1 == 0.0:
        return []
    return [(u, w * W1 / s1) for u, w in atoms]


CRAMER: dict = {}
BEURLING: dict = {}
PP_SET: set = set()


def d1_comb(level: str, key: int, h: int):
    """the frozen world -> D1 comb map at rung h; L1-rescaled to
    W1_MAIN(h).  W5 returns port-gated markers."""
    aa = math.log(h) / 2.0
    L2v = 2.0 * aa
    W1 = w1_main(h)
    if level == "W5":
        hi = int(math.floor(h))
        comp = np.zeros(hi + 1, dtype=bool)
        nlist = []
        for p in range(2, hi + 1):
            if comp[p]:
                continue
            comp[p * p:: p] = True
            q = p
            while q <= hi:
                nlist.append((q, p))
                q *= p
        nlist.sort()
        return [("PP", q, p) for q, p in nlist]
    if level == "W0":
        rng = np.random.default_rng([300, key, h])
        npp = len(mangoldt_atoms_f(h))
        us = rng.random(npp) * L2v
        ws = rng.standard_normal(npp)
        atoms = list(zip(us.tolist(), ws.tolist()))
    elif level in ("W1", "W2"):
        ns = [n for n in CRAMER[key] if n <= h]
        atoms = [(math.log(n),
                  1.0 if level == "W1" else math.log(n) / math.sqrt(n))
                 for n in ns]
    elif level == "W3":
        atoms = towers([n for n in CRAMER[key] if n <= h], float(h))
    elif level == "W4":
        atoms = beurling_atoms(BEURLING[key], float(h))
    elif level == "A1":
        atoms = [(math.log(p), math.log(p) / math.sqrt(p))
                 for p in primes_upto(h)]
    elif level == "A2":
        atoms = [(u, 1.0) for u, _w in mangoldt_atoms_f(h)]
    elif level == "A3":
        ns = sorted(n for n in CRAMER[key] if n <= h)
        wt = [w for _u, w in mangoldt_atoms_f(h)]
        atoms = [(math.log(n), wt[i % len(wt)])
                 for i, n in enumerate(ns)]
    elif level.startswith("A5e"):
        ei = int(level[-1])
        eps = JIT_EPS[ei]
        rng = np.random.default_rng([400, ei, key, h])
        base = mangoldt_atoms_f(h)
        js = rng.uniform(-eps, eps, len(base))
        atoms = [(min(max(u + float(e), 0.02), L2v), w)
                 for (u, w), e in zip(base, js)]
    else:
        raise ValueError(level)
    return l1_rescale(atoms, W1)


def d2_comb(level: str, key: int) -> tuple:
    """the frozen world -> spike comb map (positions in [0.5, 8.0])."""
    if level == "W5":
        at = [(u, w) for u, w in
              mangoldt_atoms_f(int(math.floor(math.exp(SPIKE_HI))))
              if SPIKE_LO <= u <= SPIKE_HI]
        return (np.array([u for u, _ in at]),
                np.array([w for _, w in at]))
    if level == "W0":
        rng = np.random.default_rng([310, key])
        nsp = len(d2_comb("W5", 0)[0])
        us = SPIKE_LO + rng.random(nsp) * (SPIKE_HI - SPIKE_LO)
        ws = rng.standard_normal(nsp)
        return (us, ws)
    if level in ("W1", "W2"):
        ns = CRAMER[key]
        us = np.array([math.log(n) for n in ns])
        if level == "W1":
            ws = np.ones(len(ns))
        else:
            ws = np.array([math.log(n) / math.sqrt(n) for n in ns])
        return (us, ws)
    if level == "W3":
        at = towers(CRAMER[key], float(X_SPIKE))
        return (np.array([u for u, _ in at]),
                np.array([w for _, w in at]))
    if level == "W4":
        at = beurling_atoms(BEURLING[key], float(X_SPIKE))
        at = [(u, w) for u, w in at if SPIKE_LO <= u <= SPIKE_HI]
        return (np.array([u for u, _ in at]),
                np.array([w for _, w in at]))
    if level == "A1":
        ps = primes_upto(X_SPIKE)
        return (np.array([math.log(p) for p in ps]),
                np.array([math.log(p) / math.sqrt(p) for p in ps]))
    if level == "A2":
        us, _ws = d2_comb("W5", 0)
        return (us, np.ones(len(us)))
    if level == "A3":
        ns = sorted(CRAMER[key])
        wt = [w for _u, w in mangoldt_atoms_f(X_SPIKE)]
        return (np.array([math.log(n) for n in ns]),
                np.array([wt[i % len(wt)] for i in range(len(ns))]))
    if level.startswith("A5e"):
        ei = int(level[-1])
        eps = JIT_EPS[ei]
        rng = np.random.default_rng([410, ei, key])
        us, ws = d2_comb("W5", 0)
        js = rng.uniform(-eps, eps, len(us))
        return (np.clip(us + js, SPIKE_LO, SPIKE_HI), ws.copy())
    raise ValueError(level)


# ===================================================== wall/gram layer
def rung_shared(h: int, dps: int) -> dict:
    """per-rung shared build (r184 VERBATIM): build_cell(MAIN) once,
    the world-blind Gram at the CTRL_NZ ward window, eigsy at padded
    dps."""
    gam = ward_cache()
    ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    ndig = min(dps - 2, NDIG_CAP)
    out = dict(h=h, dps=dps, K=K, ndig=ndig,
               cn_main=list(ce["cn_mp_str"]))
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        b = [(kk * mp.pi / aa) ** 2 for kk in range(K)]
        Tlo = 2 * math.pi * h + Z_OVERHANG
        Gm = [[mp.mpf(0)] * K for _ in range(K)]
        Smu = mp.mpf(0)
        nz_used = 0
        for g in gam[:CTRL_NZ]:
            gf = float(g)
            if gf <= Tlo:
                continue
            gm = mp.mpf(repr(gf))
            g2 = gm * gm
            s = mp.sin(aa * gm)
            mu = s * s / g2
            Smu += mu
            psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                   for kk in range(K)]
            for kk in range(K):
                pk = mu * psi[kk]
                row = Gm[kk]
                for ll in range(kk + 1):
                    row[ll] += pk * psi[ll]
            nz_used += 1
        for kk in range(K):
            for ll in range(kk):
                Gm[ll][kk] = Gm[kk][ll]
        Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(K)]
        out["nz_used"] = nz_used
        out["dg_str"] = [mp.nstr(Dg[kk], ndig) for kk in range(K)]
        out["smu_str"] = mp.nstr(Smu, ndig)
        out["gn_str"] = [[mp.nstr(Gm[i][j] / (Dg[i] * Dg[j]), ndig)
                          for j in range(K)] for i in range(K)]
        Mgeo = ce["mpPole"] + ce["mpArch"]
        out["mgeo_str"] = [[mp.nstr(Mgeo[i, j], ndig)
                            for j in range(K)] for i in range(K)]
        out["mprime_main_str"] = [[mp.nstr(ce["mpPrime"][i, j], ndig)
                                   for j in range(K)] for i in range(K)]
    dpse = ndig + EIG_PAD
    with mp.workdps(dpse):
        Gn = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                Gn[i, j] = mp.mpf(out["gn_str"][i][j])
        Ev, Q = mp.eigsy(Gn)
        out["lam_str"] = [mp.nstr(Ev[i], dpse - 5) for i in range(K)]
        out["q_str"] = [[mp.nstr(Q[i, j], dpse - 5) for j in range(K)]
                        for i in range(K)]
        out["gmin"] = float(min(Ev[i] for i in range(K)))
    return out


def assemble_mprime(h: int, dps: int, K: int, atoms_f: list):
    """even-sector Mprime from float atoms -- R4.build_cell recipe
    ported VERBATIM (r184); port-gated on the MANGOLDT world."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        L2v = 2 * aa
        oms = [kk * mp.pi / aa for kk in range(K)]
        par = [mp.mpf((-1.0) ** kk) for kk in range(K)]
        dsig = mp.mpf(-1)
        atoms = [(mp.log(a[1]), mp.log(a[2]) / mp.sqrt(a[1]))
                 if (isinstance(a, tuple) and len(a) == 3
                     and a[0] == "PP")
                 else (mp.mpf(repr(a[0])), mp.mpf(repr(a[1])))
                 for a in atoms_f]
        pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
              for o in oms]
        Mp = mp.zeros(K, K)
        for i in range(K):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                od = 2 * sg * (oms[i] * pj[i] - oms[j2] * pj[j2]) / den
                Mp[i, j2] += od
                Mp[j2, i] += od
        for i in range(K):
            o = oms[i]
            if i == 0:
                pdiag = sum((w * (L2v - u) for u, w in atoms), mp.mpf(0))
            else:
                pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                             for u, w in atoms), mp.mpf(0))
            Mp[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if kk == 0 else mp.sqrt(aa)
               for kk in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
        for i in range(K):
            for j2 in range(i):
                sym = (Mp[i, j2] + Mp[j2, i]) / 2
                Mp[i, j2] = sym
                Mp[j2, i] = sym
        return Mp


def world_jet(sh: dict, atoms_f: list) -> dict:
    """wall -> source -> jet for one world at one rung (r184
    VERBATIM)."""
    h, dps, K, ndig = sh["h"], sh["dps"], sh["K"], sh["ndig"]
    Mp = assemble_mprime(h, dps, K, atoms_f)
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        L2v = 2 * aa
        M = mp.matrix(K, K)
        for i in range(K):
            for j in range(K):
                M[i, j] = mp.mpf(sh["mgeo_str"][i][j]) - Mp[i, j]
        E, V = mp.eigsy(M)
        i0 = min(range(K), key=lambda i: E[i])
        nrm = [mp.sqrt(L2v) if kk == 0 else mp.sqrt(aa)
               for kk in range(K)]
        cn = [V[kk, i0] / nrm[kk] for kk in range(K)]
        imax = max(range(K), key=lambda kk: abs(cn[kk]))
        if cn[imax] < 0:
            cn = [-v for v in cn]
        d = [((-1) ** kk) * cn[kk] for kk in range(K)]
        A0 = sum(d)
        if abs(A0) < mp.mpf(repr(A0_GUARD)):
            return dict(error="A0-guard", h=h)
        Dg = [mp.mpf(s) for s in sh["dg_str"]]
        sq = mp.sqrt(mp.mpf(sh["smu_str"]))
        Jn = [(d[kk] / A0) * Dg[kk] / sq for kk in range(K)]
        return dict(h=h, K=K, ndig=ndig,
                    cn_str=[mp.nstr(v, ndig) for v in cn],
                    jn_str=[mp.nstr(v, ndig) for v in Jn])


def mass_location(sh: dict, jn_str: list) -> dict:
    """the D1 observables from the shared eigen-decomposition (r184
    VERBATIM)."""
    K, ndig = sh["K"], sh["ndig"]
    dpse = ndig + EIG_PAD
    with mp.workdps(dpse):
        l10 = mp.log(10)
        lams = [mp.mpf(s) for s in sh["lam_str"]]
        Jn = [mp.mpf(s) for s in jn_str]
        svals = []
        for i in range(K):
            acc = mp.mpf(0)
            for kk in range(K):
                acc += mp.mpf(sh["q_str"][kk][i]) * Jn[kk]
            svals.append(acc)
        tot = mp.mpf(0)
        for i in range(K):
            tot += lams[i] * svals[i] * svals[i]
        quad = mp.mpf(0)
        for i in range(K):
            gi = [mp.mpf(sh["gn_str"][i][j]) for j in range(K)]
            acc = mp.mpf(0)
            for j in range(K):
                acc += gi[j] * Jn[j]
            quad += Jn[i] * acc
        ward = float(abs(tot / quad - 1))
        lmax = max(lams)
        itop = max(range(K), key=lambda i: lams[i])
        cut = mp.mpf(CUT_PRIMARY) * lmax
        sub = mp.mpf(0)
        for i in range(K):
            if lams[i] >= cut:
                sub += lams[i] * svals[i] * svals[i]
        tail = abs(mp.mpf(1) - sub / tot)
        topshare = float(lams[itop] * svals[itop] ** 2 / tot)
        mu_m = mp.mpf(0)
        mpos = mp.mpf(0)
        for i in range(K):
            if lams[i] <= 0:
                continue
            mi = lams[i] * svals[i] * svals[i]
            if mi > 0:
                mu_m += mi * mp.log(lams[i] / lmax) / l10
                mpos += mi
        mu_mf = float(mu_m / mpos) if mpos > 0 else float("nan")
        return dict(log10tail=float(mp.log(tail + mp.mpf("1e-300"))
                                    / l10),
                    topshare=topshare, mu_m=mu_mf, ward=ward)


def alt_jet_tails(sh: dict, cn_str: list, jn_str: list) -> dict:
    """r182 alt-jet dissection VERBATIM (projective Dg-recovery)."""
    K, ndig = sh["K"], sh["ndig"]
    dpse = ndig + EIG_PAD
    out = {}
    with mp.workdps(dpse):
        l10 = mp.log(10)
        lams = [mp.mpf(s) for s in sh["lam_str"]]
        lmax = max(lams)
        Jn = [mp.mpf(s) for s in jn_str]
        cs = [mp.mpf(s) for s in cn_str]
        dmain = [((-1) ** kk) * cs[kk] for kk in range(K)]
        A0m = sum(dmain)
        keys = [math.fmod((kk + 1) * GOLD, 1.0) for kk in range(K)]
        perm = sorted(range(K), key=lambda i: keys[i])
        variants = {
            "SIGNFLIP": list(cs),
            "UNIFORM": [mp.mpf((-1) ** kk) for kk in range(K)],
            "MAGSCRAM": [(mp.mpf(1) if dmain[kk] >= 0 else mp.mpf(-1))
                         * abs(cs[perm[kk]]) for kk in range(K)]}
        scal = [Jn[kk] * A0m / dmain[kk] for kk in range(K)]
        for tag in ALT_TAGS:
            dv = variants[tag]
            Jv = [dv[kk] * scal[kk] for kk in range(K)]
            sv = []
            for i in range(K):
                acc = mp.mpf(0)
                for kk in range(K):
                    acc += mp.mpf(sh["q_str"][kk][i]) * Jv[kk]
                sv.append(acc)
            totv = mp.mpf(0)
            for i in range(K):
                totv += lams[i] * sv[i] * sv[i]
            cut = mp.mpf(CUT_PRIMARY) * lmax
            subv = mp.mpf(0)
            for i in range(K):
                if lams[i] >= cut:
                    subv += lams[i] * sv[i] * sv[i]
            tlv = abs(mp.mpf(1) - subv / totv)
            out[tag] = float(mp.log(tlv + mp.mpf("1e-300")) / l10)
    return out


def anchor_ctrl(xw: int) -> dict:
    """r182 w_ctrl MANGOLDT comparator VERBATIM (dps 60, CTRL_NZ)."""
    gam = ward_cache()
    dpsw = ANCHOR_DPS
    cw = R4.build_cell(xw, KFAC, "MAIN", dpsw, want_mp=True)
    Kw = cw["K"]
    with mp.workdps(dpsw):
        l10 = mp.log(10)
        aa = mp.log(xw) / 2
        oms = [kk * mp.pi / aa for kk in range(Kw)]
        cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
        d = [((-1) ** kk) * cs[kk] for kk in range(Kw)]
        A0 = sum(d)
        b = [o * o for o in oms]
        Tlo = 2 * math.pi * xw + Z_OVERHANG
        Sw = mp.mpf(0)
        Gm = [[mp.mpf(0)] * Kw for _ in range(Kw)]
        for g in gam[:CTRL_NZ]:
            gf = float(g)
            if gf <= Tlo:
                continue
            gm = mp.mpf(repr(gf))
            g2 = gm * gm
            s = mp.sin(aa * gm)
            mu = s * s / g2
            Sw += mu
            psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                   for kk in range(Kw)]
            for kk in range(Kw):
                pk = mu * psi[kk]
                row = Gm[kk]
                for ll in range(kk + 1):
                    row[ll] += pk * psi[ll]
        for kk in range(Kw):
            for ll in range(kk):
                Gm[ll][kk] = Gm[kk][ll]
        Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(Kw)]
        Gn_ = mp.matrix(Kw, Kw)
        for i2 in range(Kw):
            for j2 in range(Kw):
                Gn_[i2, j2] = Gm[i2][j2] / (Dg[i2] * Dg[j2])
        sq = mp.sqrt(Sw)
        Jn = [(d[kk] / A0) * Dg[kk] / sq for kk in range(Kw)]
        Ev, Q = mp.eigsy(Gn_)
        lams = [Ev[i] for i in range(Kw)]
        tot = mp.mpf(0)
        svals = []
        for i in range(Kw):
            acc = mp.mpf(0)
            for kk in range(Kw):
                acc += Q[kk, i] * Jn[kk]
            svals.append(acc)
            tot += lams[i] * acc * acc
        lmax = max(lams)
        itop = max(range(Kw), key=lambda i: lams[i])
        cutp = mp.mpf(CUT_PRIMARY) * lmax
        subp = mp.mpf(0)
        for i in range(Kw):
            if lams[i] >= cutp:
                subp += lams[i] * svals[i] * svals[i]
        tail_w = abs(mp.mpf(1) - subp / tot)
        topshare = float(lams[itop] * svals[itop] ** 2 / tot)
        mu_m = mp.mpf(0)
        mpos = mp.mpf(0)
        for i in range(Kw):
            if lams[i] <= 0:
                continue
            mi = lams[i] * svals[i] * svals[i]
            if mi > 0:
                mu_m += mi * mp.log(lams[i] / lmax) / l10
                mpos += mi
        return dict(x=xw,
                    log10tail=float(mp.log(tail_w + mp.mpf("1e-300"))
                                    / l10),
                    topshare=topshare,
                    mu_m=float(mu_m / mpos) if mpos > 0
                    else float("nan"))


# ======================================================= spike layer
def landau_field(gam: np.ndarray, us: np.ndarray) -> np.ndarray:
    """Z(u) = sum_gamma cos(gamma u) over the full n7000 cache
    (float64 instrument, disclosed)."""
    out = np.zeros(len(us))
    for lo in range(0, len(us), 256):
        blk = us[lo: lo + 256]
        out[lo: lo + len(blk)] = np.cos(np.outer(gam, blk)).sum(axis=0)
    return out


def coherence(gam: np.ndarray, us: np.ndarray, ws: np.ndarray,
              z_ms: float) -> float:
    if len(us) == 0:
        return float("nan")
    z = landau_field(gam, us)
    num = abs(float(np.dot(ws, z)))
    den = math.sqrt(float(np.dot(ws, ws)) * z_ms)
    return num / den


def d2_eval(level: str, key: int, gam: np.ndarray, z_ms: float,
            nnull: int) -> dict:
    """coherence + OWN scramble null band (frozen seed maps)."""
    us, ws = d2_comb(level, key)
    C = coherence(gam, us, ws, z_ms)
    band = []
    for s in range(nnull):
        if level == "W5":
            rng = np.random.default_rng(10000 + s)   # r184 INTRAND
        else:
            rng = np.random.default_rng([777, FAM_CODE[level], key, s])
        mag = rng.permutation(np.abs(ws))
        sgn = rng.choice([-1.0, 1.0], size=len(ws))
        band.append(coherence(gam, us, mag * sgn, z_ms))
    nmax = max(band)
    return dict(C=C, nullmax=nmax,
                R=C / nmax if nmax > 0 else float("inf"),
                natoms=len(us))


# ==================================================== adjudication layer
def classify(tails: list, full: bool) -> str:
    lo, hi = tails[0], tails[-1]
    mono = all(tails[i + 1] >= tails[i] - LADDER_SLACK
               for i in range(len(tails) - 1))
    if full and lo >= TAILRIDE_LO4 and hi >= TAILRIDE_HI8 and mono:
        return "TAIL-RIDING"
    if not full and lo >= TAILRIDE_LO4 and mono \
            and not all(t <= FAKE_BAR for t in tails):
        return "TAIL-RIDING"          # smoke-scoped proxy (disclosed)
    if all(t <= FAKE_BAR for t in tails):
        return "TOP-HEAVY"
    return "INTERMEDIATE"


def spearman(x: list, y: list) -> float:
    def rank(v):
        idx = np.argsort(np.asarray(v))
        r = np.empty(len(v))
        r[idx] = np.arange(len(v))
        return r
    rx, ry = rank(x), rank(y)
    if np.std(rx) == 0 or np.std(ry) == 0:
        return float("nan")
    return float(np.corrcoef(rx, ry)[0, 1])


# ============================================================== main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("mangoldt_ablation_ladder_probe -- MANGOLDT.ABLATION."
          "LADDER.01  (EXPLORATORY MECHANISM)")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16], "  [SMOKE]" if smoke else ""))
    print("=" * 78)

    rungs = (4, 5) if smoke else HRUNGS
    nseed = 3 if smoke else NSEED
    nsys = 2 if smoke else NSYS
    njit = 2 if smoke else NJIT
    nnull = 5 if smoke else NNULL
    full = not smoke

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + WARDS + CONSTRUCTION SELF-CHECKS")
    ok_fw, det = firewall_audit()
    check("G01-firewall-ast", ok_fw, det)
    check("G02-spec-seal", len(__doc__) > 4000,
          "SPEC_SHA %s (sha256 of __doc__)" % SPEC_SHA[:16])
    check("G03-ward-cache", ward_meta_ok(),
          "verified_zeros_n7000.npy + meta present (read-only)")
    gam = ward_cache()
    check("G04-ward-shape", len(gam) == 7000 and gam[0] > 14.13,
          "n = %d, gamma_1 = %.6f, gamma_n = %.2f"
          % (len(gam), gam[0], gam[-1]))

    t0 = time.time()
    for s in range(nseed):
        CRAMER[s] = cramer_set(s)
    for t in range(nsys):
        BEURLING[t] = beurling_gens(t)
    PP_SET.update(int(round(math.exp(u)))
                  for u, _w in mangoldt_atoms_f(X_SPIKE))
    info("constructions: %.1f s (%d Cramer seeds, %d Beurling "
         "systems)" % (time.time() - t0, nseed, nsys))

    e_cr = sum(min(1.0, 1.0 / math.log(n))
               for n in range(2, X_SPIKE + 1))
    cr_ratios = [len(CRAMER[s]) / e_cr for s in range(nseed)]
    check("G05-cramer-density",
          all(CRAMER_BAND[0] <= r <= CRAMER_BAND[1] for r in cr_ratios),
          "Cramer counts / E[count]=%.1f in [%.2f, %.2f]: min %.3f "
          "max %.3f (n=2 always kept, disclosed)"
          % (e_cr, CRAMER_BAND[0], CRAMER_BAND[1],
             min(cr_ratios), max(cr_ratios)))
    e_bg = (0.5 / math.log(2.0)
            + sum(1.0 / math.log(n) for n in range(3, X_SPIKE + 1)))
    bg_ratios = [len(BEURLING[t]) / e_bg for t in range(nsys)]
    check("G06-beurling-gens",
          all(GEN_BAND[0] <= r <= GEN_BAND[1] for r in bg_ratios),
          "Beurling generator counts / E=%.1f in [%.2f, %.2f]: "
          "min %.3f max %.3f (Beurling 1937 / Diamond-Zhang class)"
          % (e_bg, GEN_BAND[0], GEN_BAND[1],
             min(bg_ratios), max(bg_ratios)))
    sg_ok = True
    sg_txt = []
    for t in range(nsys):
        cnt, cap_hit = semigroup_count(BEURLING[t], float(SG_X), SG_CAP)
        r = cnt / SG_X
        sg_txt.append("%.2f" % r)
        sg_ok = sg_ok and (not cap_hit) and SG_BAND[0] <= r <= SG_BAND[1]
    check("G07-beurling-semigroup", sg_ok,
          "N_B(%d)/%d per system = %s in [%.1f, %.1f], DFS cap %d "
          "never hit" % (SG_X, SG_X, sg_txt, SG_BAND[0], SG_BAND[1],
                         SG_CAP))

    # instance registry (frozen)
    insts: list = []
    insts += [("W0", s) for s in range(nseed)]
    insts += [("W1", s) for s in range(nseed)]
    insts += [("W2", s) for s in range(nseed)]
    insts += [("W3", s) for s in range(nseed)]
    insts += [("W4", t) for t in range(nsys)]
    insts += [("W5", 0)]
    insts += [("A1", 0), ("A2", 0)]
    insts += [("A3", s) for s in range(nseed)]
    for ei in range(len(JIT_EPS)):
        insts += [("A5e%d" % ei, s) for s in range(njit)]
    info("instance registry: %d instances x %d rungs"
         % (len(insts), len(rungs)))

    # ------------------------------------------------------------ S1
    section("S1  D1 MASS-LOCATION -- the full ladder battery")
    TAILS: dict = {}
    SKIP: dict = {}
    JETS: dict = {}
    SHS: dict = {}
    port_dev = jet_dev = 0.0
    ward_max = 0.0
    for h in rungs:
        dps = DPS[h]
        t0 = time.time()
        sh = rung_shared(h, dps)
        K = sh["K"]
        if h in ALT_RUNGS:
            SHS[h] = sh
        at_m = d1_comb("W5", 0, h)
        Mp_mine = assemble_mprime(h, dps, K, at_m)
        with mp.workdps(dps):
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    dev = max(dev, abs(Mp_mine[i, j]
                                       - mp.mpf(sh["mprime_main_str"]
                                                [i][j])))
            port_dev = max(port_dev, float(dev))
        jm = world_jet(sh, at_m)
        with mp.workdps(dps):
            devj = max(abs(mp.mpf(a) - mp.mpf(b))
                       for a, b in zip(jm["cn_str"], sh["cn_main"]))
            jet_dev = max(jet_dev, float(devj))
        for (level, key) in insts:
            atoms = d1_comb(level, key, h)
            if not atoms:
                SKIP[(level, key)] = "EMPTY@h%d" % h
                continue
            jr = world_jet(sh, atoms)
            if "error" in jr:
                SKIP[(level, key)] = "A0-guard@h%d" % h
                continue
            ml = mass_location(sh, jr["jn_str"])
            ward_max = max(ward_max, ml["ward"])
            TAILS.setdefault((level, key), {})[h] = ml
            if h in ALT_RUNGS:
                JETS[(level, key, h)] = (jr["cn_str"], jr["jn_str"])
        info("rung h=%d (K=%d, dps=%d, nz=%d, gmin=%.2e): %.1f s"
             % (h, K, dps, sh["nz_used"], sh["gmin"],
                time.time() - t0))

    check("G08-port-mprime", port_dev <= PORT_TOL,
          "my Mprime(MANGOLDT) vs build_cell mpPrime: max dev %.2e "
          "<= 1e-25" % port_dev)
    check("G09-port-jet", jet_dev <= PORT_TOL,
          "ported wall jet vs build_cell cn: max dev %.2e <= 1e-25"
          % jet_dev)
    check("G10-mass-ward", ward_max <= MASS_WARD,
          "max |sum m_i / (Jn^T Gn Jn) - 1| = %.2e <= 1e-6" % ward_max)
    check("G11-skip-audit", True,
          "DEFINITIONAL: excluded instances = %d %s"
          % (len(SKIP), sorted(SKIP.items()) if SKIP else "(none)"))

    # per-instance classification
    CLS: dict = {}
    for (level, key) in insts:
        if (level, key) in SKIP:
            continue
        tl = [TAILS[(level, key)][h]["log10tail"] for h in rungs]
        CLS[(level, key)] = (classify(tl, full), tl)

    def level_rows(level: str) -> list:
        return [CLS[(lv, k)] for (lv, k) in insts
                if lv == level and (lv, k) in CLS]

    def level_agg(level: str) -> dict:
        rows = level_rows(level)
        n = len(rows)
        counts = {c: sum(1 for cc, _ in rows if cc == c)
                  for c in ("TAIL-RIDING", "INTERMEDIATE", "TOP-HEAVY")}
        maj = max(counts, key=lambda c: counts[c])
        s1_on = counts["TAIL-RIDING"] * 2 > n
        t4s = [tl[0] for _c, tl in rows]
        t8s = [tl[-1] for _c, tl in rows]
        return dict(n=n, counts=counts, maj=maj, s1_on=s1_on,
                    medT4=statistics.median(t4s),
                    medT8=statistics.median(t8s),
                    minT8=min(t8s), maxT8=max(t8s))

    AGG = {lv: level_agg(lv) for lv in LEVELS + ABL_LEVELS}
    print("\n  D1 TRANSITION TABLE (log10tail; T4 = h=4, T8 = h=%d)"
          % rungs[-1])
    print("  %-6s %3s  %-32s %8s %8s %18s  %s"
          % ("level", "n", "TR/INT/TH", "medT4", "medT8",
             "[minT8..maxT8]", "majority"))
    for lv in LEVELS + ABL_LEVELS:
        a = AGG[lv]
        print("  %-6s %3d  TR %2d / INT %2d / TH %2d          "
              "%8.2f %8.2f  [%7.2f..%7.2f]  %s%s"
              % (lv, a["n"], a["counts"]["TAIL-RIDING"],
                 a["counts"]["INTERMEDIATE"], a["counts"]["TOP-HEAVY"],
                 a["medT4"], a["medT8"], a["minT8"], a["maxT8"],
                 a["maj"], "  <-- S1-ON" if a["s1_on"] else ""))

    w5_tails = CLS[("W5", 0)][1]
    if full:
        rep_dev = max(abs(w5_tails[i] - R184_LADDER[h])
                      for i, h in enumerate(rungs))
        check("G12-w5-d1-replication",
              rep_dev <= R184_LADDER_TOL
              and CLS[("W5", 0)][0] == "TAIL-RIDING",
              "W5 ladder %s vs r184 record, max dev %.3f <= 0.10, "
              "class %s" % (["%.2f" % t for t in w5_tails], rep_dev,
                            CLS[("W5", 0)][0]))
    else:
        check("G12-w5-d1-replication",
              CLS[("W5", 0)][0] != "TOP-HEAVY",
              "SMOKE-SCOPED: W5 ladder %s class %s"
              % (["%.2f" % t for t in w5_tails], CLS[("W5", 0)][0]))
    check("G13-w0-null-band",
          AGG["W0"]["counts"]["TAIL-RIDING"] == 0,
          "no W0 instance TAIL-RIDING (%d instances; medT8 %.2f)"
          % (AGG["W0"]["n"], AGG["W0"]["medT8"]))
    check("G14-d1-transition-table", True,
          "DEFINITIONAL: table above; S1-ON levels = %s"
          % [lv for lv in LEVELS + ABL_LEVELS if AGG[lv]["s1_on"]])

    # overlap diagnostic at top rung (measured, no bar)
    htop = rungs[-1]
    pp_top = set(int(round(math.exp(u)))
                 for u, _w in mangoldt_atoms_f(htop))
    for lv in ("W1", "W3"):
        ovs = []
        for s in range(nseed):
            if lv == "W1":
                st = set(n for n in CRAMER[s] if n <= htop)
            else:
                st = set(int(round(math.exp(u)))
                         for u, _w in towers(
                             [n for n in CRAMER[s] if n <= htop],
                             float(htop)))
            ovs.append(len(st & pp_top) / max(1, len(st | pp_top)))
        info("D1 overlap diagnostic %s at h=%d: Jaccard with true "
             "prime-power set med %.2f min %.2f max %.2f"
             % (lv, htop, statistics.median(ovs), min(ovs), max(ovs)))

    # ------------------------------------------------------------ S2
    section("S2  D1 ANCHOR -- r182 w_ctrl MANGOLDT comparator "
            "(dps 60, CTRL_NZ 300)")
    anchor_ok = True
    gate_no = 15
    for xw in (ANCHOR_X if not smoke else (4, 5)):
        r = anchor_ctrl(xw)
        dt = abs(r["log10tail"] - float(CAL_CTRL_TAIL[xw]))
        dtop = abs(r["topshare"] - float(CAL_CTRL_LOC[xw][0]))
        dmu = abs(r["mu_m"] - float(CAL_CTRL_LOC[xw][1]))
        ok = (dt <= ANCHOR_TAIL_TOL and dtop <= ANCHOR_TOP_TOL
              and dmu <= ANCHOR_MUM_TOL)
        anchor_ok = anchor_ok and ok
        check("G%02d-anchor-x%d" % (gate_no, xw), ok,
              "tail %.3f (rec %s, dev %.3f) top %.4f (rec %s) "
              "mu_m %.2f (rec %s)"
              % (r["log10tail"], CAL_CTRL_TAIL[xw], dt, r["topshare"],
                 CAL_CTRL_LOC[xw][0], r["mu_m"], CAL_CTRL_LOC[xw][1]))
        gate_no += 1
    while gate_no < 18:            # keep numbering stable in smoke
        gate_no += 1

    # ------------------------------------------------------------ S3
    section("S3  D2 SPIKE COHERENCE -- own-null bands per world")
    t0 = time.time()
    ugrid = SPIKE_LO + (np.arange(1, SPIKE_GRID_N + 1)
                        * (SPIKE_HI - SPIKE_LO) / (SPIKE_GRID_N + 1))
    zgrid = landau_field(gam, ugrid)
    z_ms = float(np.mean(zgrid ** 2))
    info("Landau field: grid rms %.2f over %d points (%.1f s)"
         % (math.sqrt(z_ms), SPIKE_GRID_N, time.time() - t0))

    D2: dict = {}
    t0 = time.time()
    for (level, key) in insts:
        D2[(level, key)] = d2_eval(level, key, gam, z_ms, nnull)
    info("D2 battery: %d instances x %d nulls in %.1f s"
         % (len(insts), nnull, time.time() - t0))

    def d2_agg(level: str) -> dict:
        rows = [D2[(lv, k)] for (lv, k) in insts if lv == level]
        rs = [r["R"] for r in rows]
        cs = [r["C"] for r in rows]
        ns = [r["nullmax"] for r in rows]
        medR = statistics.median(rs)
        state = ("ON" if medR >= S2_ON_RATIO else
                 "WEAK" if medR >= S2_WEAK_RATIO else "OFF")
        return dict(n=len(rows), medC=statistics.median(cs),
                    medN=statistics.median(ns), medR=medR,
                    minR=min(rs), maxR=max(rs), state=state,
                    natoms=rows[0]["natoms"])
    D2A = {lv: d2_agg(lv) for lv in LEVELS + ABL_LEVELS}
    print("\n  D2 TRANSITION TABLE (R = C / max(own 20-scramble "
          "band); ON >= 10, WEAK >= 1.25)")
    print("  %-6s %3s %6s %9s %9s %8s %18s  %s"
          % ("level", "n", "atoms", "medC", "mednull", "medR",
             "[minR..maxR]", "state"))
    for lv in LEVELS + ABL_LEVELS:
        a = D2A[lv]
        print("  %-6s %3d %6d %9.2f %9.2f %8.2f  [%7.2f..%7.2f]  %s"
              % (lv, a["n"], a["natoms"], a["medC"], a["medN"],
                 a["medR"], a["minR"], a["maxR"], a["state"]))

    w5d2 = D2[("W5", 0)]
    if full:
        check("G18-w5-d2-replication",
              abs(w5d2["C"] - R184_CMANG) <= R184_D2_TOL
              and abs(w5d2["nullmax"] - R184_INTRAND) <= R184_D2_TOL,
              "C_MANG = %.2f (rec 131.04), own INTRAND band max "
              "%.2f (rec 12.60), R = %.2f"
              % (w5d2["C"], w5d2["nullmax"], w5d2["R"]))
    else:
        check("G18-w5-d2-replication", w5d2["R"] >= S2_WEAK_RATIO,
              "SMOKE-SCOPED (nnull=%d): C_MANG = %.2f, band max "
              "%.2f, R = %.2f" % (nnull, w5d2["C"], w5d2["nullmax"],
                                  w5d2["R"]))
    check("G19-d2-transition-table", True,
          "DEFINITIONAL: table above; S2-ON levels = %s"
          % [lv for lv in LEVELS + ABL_LEVELS
             if D2A[lv]["state"] == "ON"])

    # overlap-vs-R diagnostic (pooled W1+W2+W3; measured, no bar)
    fr, rr = [], []
    for lv in ("W1", "W2", "W3"):
        for s in range(nseed):
            if lv in ("W1", "W2"):
                st = CRAMER[s]
            else:
                st = [int(round(math.exp(u)))
                      for u, _w in towers(CRAMER[s], float(X_SPIKE))]
            fr.append(sum(1 for n in st if n in PP_SET)
                      / max(1, len(st)))
            rr.append(D2[(lv, s)]["R"])
    rho = spearman(fr, rr)
    info("D2 overlap diagnostic: true-prime-power atom fraction "
         "(W1/W2/W3 pooled) med %.3f; Spearman(frac, R) = %s"
         % (statistics.median(fr),
            "%.2f" % rho if not math.isnan(rho) else "nan"))

    # ------------------------------------------------------------ S4
    section("S4  A4 ALT-JETS ON THE TRUE COMB + D3 RESPONSE")
    alt_ok = True
    alt8 = {}
    for h in (r for r in ALT_RUNGS if r in rungs):
        cn_str, jn_str = JETS[("W5", 0, h)]
        alts = alt_jet_tails(SHS[h], cn_str, jn_str)
        base = TAILS[("W5", 0)][h]["log10tail"]
        print("  h=%d W5(MANGOLDT) MAIN %7.2f | %s"
              % (h, base, "  ".join("%s %7.2f" % (t, alts[t])
                                    for t in ALT_TAGS)))
        if h == max(r for r in ALT_RUNGS if r in rungs):
            alt8 = alts
            alt_ok = all(alts[t] <= ALT_FAKE_BAR for t in ALT_TAGS)
            if full and h == 8:
                alt_ok = alt_ok and base >= TAILRIDE_HI8
    check("G20-a4-altjets-break", alt_ok,
          "A4 (-SIGNS): all alt-jets relocate to top (<= -8) while "
          "MAIN rides the tail%s" % (" [SMOKE-SCOPED]" if smoke else ""))

    # D3: SIGNFLIP on the first additive S1 world below W5 and on
    # every ablation that keeps S1
    d3_targets = []
    for lv in LEVELS[:-1]:
        if AGG[lv]["s1_on"]:
            d3_targets.append(lv)
            break
    for lv in ABL_LEVELS:
        if AGG[lv]["s1_on"]:
            d3_targets.append(lv)
    d3_txt = []
    htop_alt = max(r for r in ALT_RUNGS if r in rungs)
    for lv in d3_targets:
        inst = next(((l, k) for (l, k) in insts
                     if l == lv and (l, k) in CLS
                     and CLS[(l, k)][0] == "TAIL-RIDING"
                     and (l, k, htop_alt) in JETS), None)
        if inst is None:
            d3_txt.append("%s: no TAIL-RIDING instance with stored "
                          "jet" % lv)
            continue
        cn_str, jn_str = JETS[(inst[0], inst[1], htop_alt)]
        alts = alt_jet_tails(SHS[htop_alt], cn_str, jn_str)
        dies = alts["SIGNFLIP"] <= ALT_FAKE_BAR
        d3_txt.append("%s[key=%d] h=%d MAIN %.2f SIGNFLIP %.2f -> %s"
                      % (lv, inst[1], htop_alt,
                         TAILS[inst][htop_alt]["log10tail"],
                         alts["SIGNFLIP"],
                         "DIES-LIKE-TRUE-COMB" if dies
                         else "SURVIVES-SIGNFLIP"))
    check("G21-d3-response", True,
          "DEFINITIONAL: %s"
          % ("; ".join(d3_txt) if d3_txt
             else "VACUOUS -- no S1-ON level below W5 and no "
                  "S1-keeping ablation"))

    # ------------------------------------------------------------ S5
    section("S5  TRANSITION + NECESSITY + HEADLINE (frozen "
            "adjudication)")
    def onset(flag_fn) -> tuple:
        on = [lv for lv in LEVELS if flag_fn(lv)]
        if not on:
            return None, False
        lstar = on[0]
        idx = LEVELS.index(lstar)
        located = on == list(LEVELS[idx:])
        return lstar, located

    s1_star, s1_loc = onset(lambda lv: AGG[lv]["s1_on"])
    s2_star, s2_loc = onset(lambda lv: D2A[lv]["state"] == "ON")

    def sharp_s1() -> str:
        if s1_star is None or s1_star == "W0":
            return "n/a"
        prev = LEVELS[LEVELS.index(s1_star) - 1]
        jump = AGG[s1_star]["medT8"] - AGG[prev]["medT8"]
        return ("SHARP (jump %.2f dex >= %.1f)" % (jump, SHARP_DEX)
                if jump >= SHARP_DEX
                else "GRADUAL (jump %.2f dex < %.1f)"
                % (jump, SHARP_DEX))

    def sharp_s2() -> str:
        if s2_star is None or s2_star == "W0":
            return "n/a"
        prev = LEVELS[LEVELS.index(s2_star) - 1]
        rprev = max(D2A[prev]["medR"], 1e-12)
        rat = D2A[s2_star]["medR"] / rprev
        return ("SHARP (ratio %.1fx >= %.0fx)" % (rat, SHARP_RATIO)
                if rat >= SHARP_RATIO
                else "GRADUAL (ratio %.1fx < %.0fx)"
                % (rat, SHARP_RATIO))

    s1_sharp, s2_sharp = sharp_s1(), sharp_s2()
    check("G22-s1-adjudication", True,
          "DEFINITIONAL: S1 onset %s located=%s %s"
          % (s1_star, s1_loc, s1_sharp))
    check("G23-s2-adjudication", True,
          "DEFINITIONAL: S2 onset %s located=%s %s"
          % (s2_star, s2_loc, s2_sharp))

    # necessity table
    nec_tokens = []
    nec_txt = []
    for lv in ABL_LEVELS:
        kill_s1 = not AGG[lv]["s1_on"]
        kill_s2 = D2A[lv]["medR"] < S2_ON_RATIO
        nec_txt.append("%s(-%s): S1 %s (maj %s, medT8 %.2f) | S2 %s "
                       "(medR %.2f)"
                       % (lv, ABL_PROP[lv],
                          "KILLS" if kill_s1 else "KEEPS",
                          AGG[lv]["maj"], AGG[lv]["medT8"],
                          "KILLS" if kill_s2 else "KEEPS",
                          D2A[lv]["medR"]))
        if kill_s1:
            nec_tokens.append("NECESSARY-%s" % ABL_PROP[lv])
    kill_a4 = alt_ok
    nec_txt.append("A4(-SIGNS): %s (all alt tails <= -8: %s)"
                   % ("KILLS" if kill_a4 else "KEEPS",
                      {t: "%.2f" % v for t, v in alt8.items()}))
    if kill_a4:
        nec_tokens.append("NECESSARY-SIGNS")
    for line in nec_txt:
        print("  " + line)
    check("G24-necessity-table", True,
          "DEFINITIONAL: tokens = %s" % (nec_tokens or "NONE"))

    w4_rides = AGG["W4"]["s1_on"]
    check("G25-w4-headline", True,
          "DEFINITIONAL: DOES-W4-TAIL-RIDE = %s (maj %s, medT8 %.2f, "
          "TR %d/%d systems; Beurling: multiplicativity + weight "
          "grammar, NO Riemann-zero coupling)"
          % ("YES" if w4_rides else "NO", AGG["W4"]["maj"],
             AGG["W4"]["medT8"], AGG["W4"]["counts"]["TAIL-RIDING"],
             AGG["W4"]["n"]))

    # ------------------------------------------------------------ S6
    section("S6  TAXONOMY VERDICT (frozen adjudication)")
    transfer_valid = (CHECKS_OK("G12") and anchor_ok
                      and CHECKS_OK("G18") and alt_ok)

    def sig_token(star, located, kill_pos, tag) -> str:
        if star == "W5" and located and kill_pos:
            return "%s-ZERO-COUPLED" % tag
        if star is not None and located and star != "W5":
            return "%s-SUFFICIENT-AT-%s" % (tag, star)
        return "%s-DIFFUSE" % tag

    a3_kills_s1 = not AGG["A3"]["s1_on"]
    a3_kills_s2 = D2A["A3"]["medR"] < S2_ON_RATIO
    tok_s1 = sig_token(s1_star, s1_loc, a3_kills_s1, "S1")
    tok_s2 = sig_token(s2_star, s2_loc, a3_kills_s2, "S2")
    if not transfer_valid:
        taxonomy = "INSTRUMENT-LIMITED"
    elif s1_loc and s2_loc and not tok_s1.endswith("DIFFUSE") \
            and not tok_s2.endswith("DIFFUSE"):
        taxonomy = ("MECHANISM-LOCATED(S1@%s %s, S2@%s %s)"
                    % (s1_star, "sharp" if "SHARP" in s1_sharp
                       else "gradual",
                       s2_star, "sharp" if "SHARP" in s2_sharp
                       else "gradual"))
    else:
        taxonomy = "MECHANISM-DIFFUSE"
    check("G26-taxonomy", True,
          "DEFINITIONAL: %s (transfer_valid=%s; %s; %s)"
          % (taxonomy, transfer_valid, tok_s1, tok_s2))

    # ------------------------------------------------------------ S7
    section("S7  BOOKKEEPING")
    rt = time.time() - T0_WALL
    check("G27-runtime", rt <= RUNTIME_BAR,
          "runtime %.1f s <= %.0f s" % (rt, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    verdict = []
    if transfer_valid:
        verdict.append("TRANSFER-VALID-W5-REPLICATES-R184")
    verdict += [taxonomy, tok_s1, tok_s2]
    verdict += nec_tokens
    verdict.append("W4-BEURLING-TAIL-RIDES" if w4_rides
                   else "W4-BEURLING-DOES-NOT-TAIL-RIDE")
    verdict += ["NO-RH-CLAIM", "NO-NUMEROLOGY-CLAIM"]
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS" % (npass, ntot))
    print("COMPOSITE VERDICT: " + " + ".join(verdict))
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("RUNTIME %.1f s" % rt)
    print("=" * 78)
    return 0 if npass == ntot else 1


def CHECKS_OK(prefix: str) -> bool:
    return all(ok for nm, ok, _d in CHECKS if nm.startswith(prefix))


if __name__ == "__main__":
    sys.exit(main())
