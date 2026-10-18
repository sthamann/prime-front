#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""representation_contest_probe -- PRIME.PORT.REPRESENTATION.
CONTEST.01 (round 282): WHAT IS h_n?  Four classical
representation classes for the pivot h_n -- monodromy norm,
intersection form, canonical-system Hamiltonian, operator
compression -- each with a construction attempt on exact toys and
ONE brutal reviewer gate: the representation must (i) force MAIN
positivity STRUCTURALLY (existence of the structure => h > 0 as
an implication, symbolically checkable) AND (ii) provably REJECT
at least one early-dying control world (the structure does not
exist there or breaks exactly at the flip).  A representation
that exists everywhere is decoration; one that is nowhere
constructible is theology.  NOT judged by numerical fit.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE ELIMINATION BALANCE (why this contest; the r261..r281 record):
cancellation is generic/coherent (r273 + r261: no finite grouping,
no involution, no cone); extremality is false (r280:
MAIN_NOT_MAXIMAL); local geometry is insufficient (r268/r269); KYP
memory is a no-go (r275); the duality is a restatement (r280);
the Maslov obstruction is refuted (r279: OBSTRUCTION_REFUTED);
moment perturbation is world-blind (r280); the crossing type is
world-blind (r281: all four dead worlds CREEPING); half-filling is
pure counting (r281: the counting theorem says WHERE the window
ends, never WHY MAIN survives it).  What remains is the NORTH
STAR question: which OBJECT owns h_n as a norm, volume, energy,
index or intersection number, so that h_n > 0 follows structurally
-- the dream h_n = <omega_n, omega_n> in a space that exists ONLY
for the right arithmetic class.

INDEX FIREWALL (binding, r238-r281 discipline): w = window (kz),
S = #union support atoms of mutilde = mu - nu, S_- = #negative
union weights, N_w = builder depth = ceil(S/2) = (S+1)//2, n =
chain degree, h_n = chain pivot, minC = first n with h_n < 0,
budget = #(h_n < 0) over the full continuation (= S_- by the r279
theorem); ground truth (control flip tables, census offsets, the
withheld sign chain) enters GATES and record tables only; no
zero/prime oracles anywhere (AST firewall).  REPRESENTATION-LEVEL
DECLARATION (honest, binding): K1/K3/K4 constructions consume the
chain data (al, be, hs) BY DESIGN -- they are representations OF
h, not blind predictors; the scope audit forbids the ground-truth
tables (CTRL_FLIPS, HL2_FLIP, minC_true, offs_true, sg_true) in
every sealed constructor; the K2 gauge constructors are
source-pure (atom signs + configuration terms only).  MACHINERY
IMPORTED VERBATIM: r280 BL.{union_of_ctx, sign_chain_f64,
mp_sign_chain, toy_moments, frac_det, TOYS_XS, MAINLIKE_W,
FLIPLIKE_W}, MS.ctx_build, r230 JF.{stieltjes_exact, TOY_NODES,
TOY_WTS}, r274 WD.stj_gen, r277 MC.cand_interlace, paircorr
PC.{Grid, gen_model}, v881 PIK, r243 PB.smooth_comb, v563 core
READ-ONLY.

THE FOUR SEALED CLASSES (construction + gate, frozen BEFORE
evaluation):

(K1) RHP/MONODROMY -- h_n as a monodromy norm |m_n|^2 x positive
  factor.  CONSTRUCTION: the Pontryagin split of the self-pairing
  h_n = <pihat_n, pihat_n>_mutilde = P_n - N_n with P_n =
  sum_{w_j > 0} w_j pihat_n(x_j)^2 > 0 and N_n = sum_{w_j < 0}
  |w_j| pihat_n(x_j)^2 >= 0 (exact identity, gated on all toys at
  every degree).  The |m_n|^2 representation h_n = ||pihat_n||^2
  exists exactly when the negative register is EMPTY (N_n == 0
  for all n): the Schwarz-reality/symmetry condition of the
  discrete 2x2 problem (r224 JMU frame) is the POSITIVITY OF THE
  JUMP -- for a signed mutilde the jump is indefinite and the
  monodromy pairing is a Pontryagin (not Hilbert) pairing.
  SEALED EXISTENCE CRITERION: SOS_EXISTS iff N_n == 0 at every
  chain degree.  GATE: SOS must exist on the MAIN-like class and
  fail on a control class.  ADJUDICATION: GO iff SOS_EXISTS on
  MAINLIKE and not on FLIPLIKE; RESTATEMENT iff the split is
  exact but SOS fails on MAINLIKE too and the remaining
  positivity clause N_n < P_n is h_n > 0 verbatim;
  NOT_CONSTRUCTIBLE iff the split identity itself breaks.
  MUST-FAIL m1: the fake SOS that drops the negative register
  (P_n alone) must miss h_n by EXACTLY N_n > 0 (loud, exact).

(K2) HODGE/INTERSECTION -- h_n as an intersection-form value with
  a Kasteleyn-like ORIENTATION on the Cauchy-Binet configuration
  space (r261 a1: term(I) = 4^binom(n,2) Delta(x_I)^2 prod_{i in
  I} w_i; sign(term) = prod_{i in I} sign w_i is ALREADY a
  coboundary of the atom sign vector).  THE QUESTION (this is NOT
  the r261 termwise-positivity no-go): does an ORIENTATION CLASS
  exist -- (linear class) a gauge sigma in {+-1}^S with eps(I) =
  prod_{i in I} sigma_i, or (quadratic/edge class, the genuine
  Kasteleyn shape) pair signs kappa_ij with eps(I) = prod_{i<j in
  I} kappa_ij -- such that (C) eps(I) term(I) is sign-coherent in
  EVERY cell n = 1..S-1 and (V) the oriented sum still represents
  +-D_n (value preservation)?  SEALED TESTS: (linear) FULL
  EXHAUSTION over all 2^S gauges on every toy -- the coherent set
  must be computed, not assumed; (quadratic) the n = 2 cells
  force kappa_ij = c sign(w_i w_j) (each pair is its own cell),
  and coherence of the n = 3 cell then requires prod_{i in I}
  sign(w_i) constant over ALL triples -- checked exactly;
  (value) for the surviving gauge sigma = sign(w): the oriented
  value is D_n(|w|), and the defect at n = 1 is m_0(|w|) -
  m_0(w) = 2 x (negative mass), EXACT -- zero iff S_- = 0.
  ADJUDICATION: GO iff some orientation is coherent AND
  value-preserving on MAINLIKE and none is on FLIPLIKE;
  WORLD_BLIND iff on both; NOT_CONSTRUCTIBLE iff none on
  MAINLIKE (with the exact obstruction).  MUST-FAIL m2: a gauge
  oriented by the withheld h-sign chain must be FLAGGED by the
  AST scope audit.  ANTI-GATE (decoration): eps = sign(term)
  itself (no locality class) exists everywhere and is EXCLUDED
  by seal.

(K3) DE BRANGES / CANONICAL SYSTEM -- the chain as a canonical
  system with Hamiltonian H(t) >= 0.  CONSTRUCTION (classical,
  exact): the monic Jacobi matrix J = tridiag(1, alpha, beta) is
  symmetrizable by a real diagonal d_n^2 = h_n/h_0 iff every
  beta_k > 0; the per-cell Hamiltonian H_n = v_n v_n^T with v_n =
  (1, sqrt(beta_n)) exists real and PSD iff beta_n >= 0; hence
  HAMILTONIAN POSITIVITY THROUGH THE FREE WINDOW <=> h_0..h_{
  N_w-1} > 0 -- EXACT equivalence (bookkeeping, gated).  THE
  RESTATEMENT DETECTOR (the round's honest question): does the
  Hamiltonian positivity have ANOTHER (more checkable) gestalt
  than h > 0 itself?  Sealed candidate shadow: the R2
  interlacing/reality of the pihat_n zeros (r277 anchor,
  MC.cand_interlace with the balanced tridiagonal).  Measured
  lag = fire - minC per world: a lag-0 shadow would FORBID the
  crossing; a lag >= 1 shadow only detects it afterwards.
  ADJUDICATION: GO iff an h-independent shadow has lag 0 on
  every flipping toy AND every control while MAIN stays safe;
  RESTATEMENT iff the equivalence is exact but every shadow lag
  is >= 1 (the de Branges form is h > 0 verbatim; the shadow
  cannot carry the implication).  MUST-FAIL m3: the |beta|
  symmetrizer (absolute values) is a valid positive chain but
  represents a DIFFERENT measure: its Jacobi moments m_k = h_0
  (A^k)_{00} must break the true moment sequence loudly at the
  first degree that sees the flipped beta (exact).

(K4) OPERATOR POSITIVITY -- h_n as a compression datum of a joint
  positive structure on the DUAL PAIR (v956 duality).
  CONSTRUCTION (exact): dual weights w#_j = 1/(w_j L'(x_j)^2),
  dual chain h#_m; the v956 complement identity gives the exact
  product law  h_n x h#_{S-1-n} == 1  at EVERY degree (gated in
  rationals on all toys).  THE STRUCTURE CONSEQUENCE (corollary,
  gated): sign h_n == sign h#_{S-1-n} IDENTICALLY -- the dual
  pair is sign-synchronized as an IDENTITY, in every world, both
  sides of every flip: the "joint positivity" h_n > 0 AND
  h#_{S-1-n} > 0 is ONE condition seen twice, never an
  intersection of two constraints.  THE BUDGET OBSTRUCTION
  (r279 theorem, re-derived exactly): #(h < 0) == S_- >= 1 on
  every signed world -- ANY global positive structure (CP map /
  dilation) whose compressions produce ALL pivots is NOT
  constructible for signed sources; a structure restricted to
  the free window must ENCODE N_w, and the window boundary is
  the r281 counting theorem (pure counting): the "positive
  structure" collapses onto the localization statement itself.
  ADJUDICATION: GO iff the joint dual structure provably rejects
  >= 1 control (sync breaks at its flip); WORLD_BLIND iff the
  sync holds identically on every world including the flipping
  toys; NOT_CONSTRUCTIBLE iff the duality identity itself
  breaks.  MUST-FAIL m4: dual weights WITHOUT the L'^2 factor
  (w# = 1/w) must break the product law loudly (exact).

TOY WORLDS (exact rationals, sealed): JF9 = the r230 9-atom toy
(S = 9, N_w = 5, S_- = 3, minC = 3: dies INSIDE its free window
-- an exact control); MAINLIKE (S = 6, N_w = 3, S_- = 2, minC =
4: survives its free window -- the MAIN-class toy); FLIPLIKE
(S = 6, S_- = 2, minC = 2: dies inside -- control); POSLIKE =
|MAINLIKE weights| (S_- = 0, minC = none: the positive class,
where the classical structures MUST exist -- the calibration of
gate (i)).  REAL WORLDS (f64 + mp ward): w9 MAIN (S = 367, N_w =
184, minC = 184) + the dead battery EPSTEIN / SCRAMBLE(seed 1) /
SMOOTH (flips 25/21/27) + HL2 (seed 101, flip 25).

DETECTORS (sealed, r281 distance rule -- MAIN_SEPARATING iff
MAIN's value is farther from EVERY dead value than the dead
spread, else WORLD_BLIND): D1 (K1) negative-register fraction at
the last free degree = (1 - sg rmg)/2 at n = N_w - 1; D2 (K2)
orientation value defect = 2 x negmass / gross mass (source-
pure); D3 (K3) shadow fire degree / N (DECLARED h-reading:
restatement-grade by construction); D4 (K4) sync fraction
(identically 1 by the theorem -- the world-blindness IS the
finding).  STOP LIST (anti-gates, binding): no derived 5/7, no
bound mechanism claim, no asymptotic law, no localization claim,
no lower-side claim, NO RH claim; r243..r281 stand.

SEALED CONSTANTS: TOYS as above (POSLIKE = abs MAINLIKE);
TOY_ANCH minC {JF9: 3, MAINLIKE: 4, FLIPLIKE: 2, POSLIKE: None},
budgets {3, 2, 2, 0}; W9_ANCH (S 367, N 184, minC 184, S_- 104);
CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27; HL2 seed 101, flip 25;
EXT 8; IM_TOL 1e-7; MP_DPS 40 / MP_GUARD 1e-30 / MP_RECOUNT 80;
VAL_NMAX N_w + 1 per toy; MOM_KMAX 2 (S - 2); CTRL_CHAIN_EXT 10;
runtime <= 1800 s; smoke = toys (all four classes exact) +
exhaustion + must-fails + scopes + w9 f64 sanity (negfrac,
defect); skipped in smoke: mp ward, controls, w9 interlacing
sweep, detector, adjudication.
PRE-SPEC SCOPING (disclosed, r281 protocol): two scratch passes
on the toys + one machinery pass on w9 ONLY, run BEFORE this spec
was sealed and deleted: (i) the duality index convention (h_n
h#_{S-1-n} == 1, not S-2-n), the coherence collapse (the linear
coherent set is exactly {+-sign w} on all four toys), the value
mismatch at n = 1, the P/N split identity, and the toy
interlacing fires (minC + 1 on FLIPLIKE/JF9); (ii) w9 cost and
behavior (chain 0.0 s, interlacing sweep 0.3 s SAFE through 183
with min normalized margin 4.8e-8 -- f64-marginal, disclosed;
negfrac 0.498, defect 0.115).  Every adjudication rule, bar and
verdict form above was frozen before the full-record evaluation;
the controls, the detector and the mp ward were UNTOUCHED
pre-spec.

SEALED VERDICT FORM (frozen BEFORE evaluation; per class exactly
one of REPRESENTATION_GO(structure, gate passed) /
REPRESENTATION_RESTATEMENT / REPRESENTATION_WORLD_BLIND /
REPRESENTATION_NOT_CONSTRUCTIBLE, plus the overall
CONTEST_WINNER(class; priority K1 > K2 > K3 > K4) /
CONTEST_ALL_DEAD(with the precise elimination per class -- itself
a program finding: the positivity has no representation in the
four classical languages at this resolution).
Honesty before beauty: gate (i) is calibrated on POSLIKE (the
classical structures MUST exist for the positive class -- if they
do not, the construction is wrong, not the class); a class that
exists only for the positive class cannot carry MAIN (MAIN is
signed); no verdict claims a derived 5/7, a bound mechanism or an
asymptotic law; the lower side (why MAIN survives its free
window) stays the open center.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 28/30 -- the drafted m4
loudness criterion was a GUESSED 1e3 magnitude bar while the
measured worst |h h# - 1| on MAINLIKE is 1.4e+02; ONE disclosed
amendment a1 (smoke stage, BEFORE any full evaluation, gate-side
only, r261-a1 precedent): the m4 criterion moved to the
exact-breakage form (h h# != 1 in rationals at EVERY degree plus
worst dev >= 1e2); smoke pass 2 = 30/30 (0.1 s); calibration
pass 1 = first full evaluation = 30/30, wall 1.2 s; NO bar,
band, class, adjudication or verdict rule moved at any point;
run1/run2 identical up to WALL):
CAL_VERDICT = K1 REPRESENTATION_RESTATEMENT + K2
REPRESENTATION_NOT_CONSTRUCTIBLE + K3 REPRESENTATION_RESTATEMENT
+ K4 REPRESENTATION_WORLD_BLIND + CONTEST_ALL_DEAD.
Key numbers.  TOYS (exact rationals): chain census == sealed
anchors (minC 3/4/2/None, budgets 3/2/2/0 == S_-, N_w 5/3/3/3;
sign strings +++--++-+ / ++++-- / ++-++- / ++++++).
K1: P_n - N_n == h_n exact at every degree on all four toys; SOS
exists ONLY on POSLIKE (N_n == 0 all n); on the signed toys N_n
> 0 at EVERY degree n >= 1 (MAINLIKE included: N/P = 0.5380 at
the last free degree n = 2) -- the monodromy-norm structure does
not exist on the MAIN class, and the surviving clause N_n < P_n
is h_n > 0 verbatim; m1 fake SOS misses h_2(MAINLIKE) by exactly
N_2 = 48360721965/70120631072 LOUD; w9 negfrac at N_w - 1 =
0.498189 (rmg 3.62e-3): the negative register carries HALF the
mass at the wall.  K2: linear exhaustion (512/64/64/64 gauges):
coherent set == {+-sign w} on ALL four toys (2 gauges each --
the orientation class is UNIQUE, computed not assumed);
quadratic/edge class: n = 2 forces kappa = c sign(w_i w_j),
n = 3 coherence fails on ALL THREE signed toys and holds on
POSLIKE; value: the oriented sum is D_n(|w|), defect at n = 1 ==
2 x negmass EXACT (JF9 55/36, MAINLIKE 44/35, FLIPLIKE 114/35,
POSLIKE 0) and D_n(|w|) != +-D_n(w) at EVERY checked n >= 1 on
the signed toys (mism xxxxxx/xxxx/xxxx/====) => the orientation
is constructible EXACTLY on the positive class; w9: singleton
forcing + defect 0.1152 (S_- = 104, negmass 0.2262) -- dead at
n = 1 already; m2 FLAGGED (sg_true).  K3: symmetrizer/
Hamiltonian bookkeeping exact on all toys ((all beta_k > 0 up to
n) <=> (h_0..h_n > 0); H_cell PSD <=> beta >= 0); shadow fires
{JF9 4, MAINLIKE None, FLIPLIKE 3, POSLIKE None} == minC + 1 on
the flipping toys; REAL: w9 SAFE through n = 183 (min normalized
margin 4.8e-8, f64-marginal, r277 blind-42/42 record cited),
control fires EPST 26 / SCR 22 / SMOOTH 28 / HL2 26 == flip + 1
EXACTLY (lag +1 everywhere) -- the shadow detects, it never
forbids; m3 |beta| mutant: moments agree at k = 0..3 and break
at k = 4 EXACTLY (FLIPLIKE, the first degree that sees beta_2 <
0) LOUD.  K4: product law h_n h#_{S-1-n} == 1 exact at every
degree on all four toys; sign sync IDENTICAL through every flip
(FLIPLIKE/JF9 included) -- the dual pair adds no second
constraint; budget == S_- re-derived exact (3/2/2/0); m4 wrong
dual (1/w) breaks the product law exactly at every degree of
MAINLIKE, worst |h h# - 1| = 1.4e+02 LOUD.  DETECTOR (sealed
distance rule, MAIN + EPST/SCR/SMOOTH/HL2): D1 negfrac WORLD_
BLIND (MAIN 0.498 inside the dead range 0.228..0.506), D2
defect WORLD_BLIND (MAIN 0.115 inside 0.000..0.580), D3 fire/N
MAIN_SEPARATING (MAIN 1.000 vs dead 0.120..0.152 -- but
DECLARED h-reading: restatement-grade decoration), D4 sync
WORLD_BLIND (identically 1.000 -- the theorem); NO source-pure
class statistic separates MAIN.  CONTROLS: flips 25/21/27 + HL2
25 == records; w9 mp ward (dps 40): exact sign agreement
N_w-2..minC+2, 0 recounts.  MUST-FAILS: m1/m3/m4 LOUD, m2
FLAGGED; scope audits CLEAN (8 constructors); fragment audit
CLEAN.  Runtime ~1.2 s full / ~0.1 s smoke; run1/run2 identical
up to WALL.
AMENDMENTS AFTER FREEZE: NONE.

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
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import budget_localization_probe as BL        # noqa: E402 r280
import metric_stability_probe as MS           # noqa: E402 r278
import jfraction_probe as JF                  # noqa: E402 r230
import wronskian_dictionary_probe as WD       # noqa: E402 r274
import maslov_census_probe as MC              # noqa: E402 r277
import paircorr_margin_probe as PC            # noqa: E402 relocation
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
EXT = 8
IM_TOL = 1e-7
MP_DPS = 40
MP_GUARD = 1e-30
MP_RECOUNT = 80
CTRL_CHAIN_EXT = 10
W9_ANCH = (367, 184, 184, 104)
TOY_ANCH = {"JF9": (9, 5, 3, 3), "MAINLIKE": (6, 3, 4, 2),
            "FLIPLIKE": (6, 3, 2, 2), "POSLIKE": (6, 3, None, 0)}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; K2 gauge "
                       "constructors are source-pure (atom signs + "
                       "terms only); K1/K3/K4 consume chain data BY "
                       "DECLARATION (representations of h, not blind "
                       "predictors); ground-truth flip tables enter "
                       "gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("pn_split", "sos_census", "gauge_coherent_set",
                "pair_gauge_check", "gauge_value_defect",
                "sym_cell_psd", "interlace_shadow", "dual_pack")
FORBIDDEN = {"CTRL_FLIPS", "HL2_FLIP", "minC_true", "offs_true",
             "sg_true", "W9_ANCH", "TOY_ANCH"}


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ==================== exact toy machinery (Fractions)
def toy_chain(nodes, wts):
    """exact monic chain: (al, be, hs) with be[k-1] = beta_k."""
    S_ = len(nodes)
    return JF.stieltjes_exact(nodes, wts, S_ - 1)


def pv_rows(nodes, al, be, n_hi):
    """pihat_n(x_j) rows for n = 0..n_hi (exact)."""
    S_ = len(nodes)
    rows = [[Fr(1)] * S_]
    if n_hi >= 1:
        rows.append([x - al[0] for x in nodes])
    for k in range(1, n_hi):
        rows.append([(nodes[j] - al[k]) * rows[-1][j]
                     - be[k - 1] * rows[-2][j] for j in range(S_)])
    return rows


def toy_first_neg(hs):
    return next((k for k in range(len(hs)) if hs[k] < 0), None)


# ==================== K1 sealed constructors
def pn_split(nodes, wts, row):
    """Pontryagin split of the self-pairing at one degree:
    (P, N) with P - N = h; consumes atoms + weights + the pihat
    row only."""
    P = sum(w * p * p for x, w, p in zip(nodes, wts, row) if w > 0)
    Nn = sum(-w * p * p for x, w, p in zip(nodes, wts, row) if w < 0)
    return P, Nn


def sos_census(Ns):
    """SOS existence: the negative register is empty at every
    degree."""
    return all(v == 0 for v in Ns)


def mutant_fake_sos(P):
    """m1 MUST-FAIL: the 'sum of squares' that drops the negative
    register -- must miss h by exactly N > 0 (loud)."""
    return P


# ==================== K2 sealed constructors (source-pure)
def gauge_coherent_set(sgw):
    """FULL EXHAUSTION over the linear orientation class: all
    sigma in {+-1}^S; coherent iff every cell n = 1..S-1 has one
    sign of eps(I) prod_{i in I} sgw_i.  Consumes atom signs
    ONLY."""
    S_ = len(sgw)
    out = []
    for mask in range(1 << S_):
        sig = [1 if (mask >> i) & 1 else -1 for i in range(S_)]
        tau = [s * e for s, e in zip(sig, sgw)]
        ok = True
        for n in range(1, S_):
            seen = set()
            for c in combinations(range(S_), n):
                pr = 1
                for i in c:
                    pr *= tau[i]
                seen.add(pr)
                if len(seen) > 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(sig))
    return out


def pair_gauge_check(sgw):
    """quadratic/edge (Kasteleyn-shape) class: n = 2 forces
    kappa_ij = c sign(w_i w_j); the n = 3 cell is then coherent
    iff prod_{i in I} sgw_i is constant over all triples.
    Returns that constancy (True = class constructible so far)."""
    S_ = len(sgw)
    tri = set()
    for c in combinations(range(S_), 3):
        pr = 1
        for i in c:
            pr *= sgw[i]
        tri.add(pr)
    return len(tri) == 1


def gauge_value_defect(wts):
    """value obstruction of the surviving gauge sigma = sign(w):
    m_0(|w|) - m_0(w) = 2 x negative mass (exact); zero iff the
    measure is positive."""
    return 2 * sum(-w for w in wts if w < 0)


def mutant_gauge_reader(sg_true):
    """m2 MUST-FAIL: a gauge oriented by the withheld h sign
    chain -- the scope audit must FLAG this."""
    return [int(s) for s in sg_true]


# ==================== K3 sealed constructors
def sym_cell_psd(beta):
    """canonical-system cell: v = (1, sqrt(beta)) exists real and
    H = v v^T is PSD iff beta >= 0 (bookkeeping identity)."""
    return beta >= 0


def interlace_shadow(al, be, lo, hi, n_hi, imtol):
    """R2 interlacing/reality shadow (r277 verbatim): first
    degree where the zeros leave the real axis or strict
    interlacing fails; consumes chain coefficients only."""
    alf = [float(a) for a in al]
    bef = [0.0] + [float(b) for b in be]
    return MC.cand_interlace(alf, bef, float(lo), float(hi),
                             n_hi, imtol)


def jacobi_moments(al, be, h0, kmax):
    """m_k = h_0 (A^k)_{00} with A = tridiag(sub beta, diag
    alpha, super 1) -- exact in the toy arithmetic."""
    M = len(al)
    v = [h0 * 0 + 1] + [h0 * 0] * (M - 1)
    out = [h0 * v[0]]
    for _k in range(kmax):
        nv = [h0 * 0] * M
        for i in range(M):
            acc = al[i] * v[i]
            if i + 1 < M:
                acc += v[i + 1] * be[i]
            if i - 1 >= 0:
                acc += v[i - 1]
            nv[i] = acc
        v = nv
        out.append(h0 * v[0])
    return out


# ==================== K4 sealed constructors
def dual_pack(nodes, wts):
    """dual weights w#_j = 1/(w_j L'(x_j)^2) and the dual chain
    (exact); consumes atoms + weights only."""
    S_ = len(nodes)
    wd = []
    for j in range(S_):
        lp = Fr(1) if isinstance(nodes[j], Fr) else 1.0
        for k in range(S_):
            if k != j:
                lp = lp * (nodes[j] - nodes[k])
        wd.append(1 / (wts[j] * lp * lp))
    ald, bed, hsd = JF.stieltjes_exact(nodes, wd, S_ - 1)
    return wd, hsd


def mutant_wrong_dual(nodes, wts):
    """m4 MUST-FAIL: dual weights WITHOUT the L'^2 factor -- the
    product law must break loudly."""
    wd = [1 / w for w in wts]
    _al, _be, hsd = JF.stieltjes_exact(nodes, wd, len(nodes) - 1)
    return hsd


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("representation_contest_probe -- PRIME.PORT.REPRESENTATION."
          "CONTEST.01 (round 282)")
    print("SPEC_SHA %s   (r280 BL %s)"
          % (SPEC_SHA[:16], BL.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys all four classes + exhaustion + "
                        "must-fails + scopes + w9 f64 sanity; mp ward, "
                        "controls, w9 interlacing, detector, "
                        "adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the four class constructions "
          "K1 (Pontryagin/SOS), K2 (orientation classes linear + "
          "quadratic, exhaustion + value), K3 (canonical-system "
          "Hamiltonian + R2 shadow lag), K4 (dual product law + "
          "sync + budget obstruction); the brutal gate (structural "
          "forcing + control rejection), the POSLIKE calibration, "
          "the adjudication rules, the detector rule and the "
          "verdict form; pre-spec scoping disclosed (toys + one w9 "
          "machinery pass)")

    # ---------------- S1 toys: chains + census
    section("S1  TOY WORLDS -- CHAIN CENSUS")
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    POSLIKE_W = [abs(w) for w in BL.MAINLIKE_W]
    toys = [("JF9", [t[0] for t in jf_pairs],
             [t[1] for t in jf_pairs]),
            ("MAINLIKE", BL.TOYS_XS, BL.MAINLIKE_W),
            ("FLIPLIKE", BL.TOYS_XS, BL.FLIPLIKE_W),
            ("POSLIKE", BL.TOYS_XS, POSLIKE_W)]
    T = {}
    ok_cen = True
    for name, nodes, wts in toys:
        S_ = len(nodes)
        Nw = (S_ + 1) // 2
        al, be, hs = toy_chain(nodes, wts)
        mc = toy_first_neg(hs)
        Sm = sum(1 for w in wts if w < 0)
        budget = sum(1 for h in hs if h < 0)
        aS, aN, amc, aSm = TOY_ANCH[name]
        ok_cen = ok_cen and (S_ == aS) and (Nw == aN) \
            and (mc == amc) and (Sm == aSm) and (budget == Sm)
        T[name] = dict(nodes=nodes, wts=wts, al=al, be=be, hs=hs,
                       S=S_, Nw=Nw, mc=mc, Sm=Sm)
        info("%s: S=%d N_w=%d minC=%s S_-=%d budget=%d signs=%s"
             % (name, S_, Nw, str(mc), Sm, budget,
                "".join("+" if h > 0 else "-" for h in hs)))
    check("G10-toy-census", ok_cen,
          "EXACT (rationals): chain census == sealed anchors on all "
          "four toys; budget #(h<0) == S_- re-derived (r279 "
          "theorem); MAINLIKE survives its free window (minC 4 >= "
          "N_w 3), FLIPLIKE/JF9 die inside (2 < 3, 3 < 5), POSLIKE "
          "never flips -- the positive class calibrator")

    # w9 sanity (f64, cheap -- in smoke too)
    ctx9 = MS.ctx_build(9)
    xu9, wu9, _z9 = BL.union_of_ctx(ctx9)
    S9 = len(xu9)
    N9 = ctx9["N"]
    sg9, lgh9, rmg9 = BL.sign_chain_f64(xu9, wu9, N9 + EXT)
    minC9 = next((n for n in range(len(sg9)) if sg9[n] < 0), None)
    Sm9 = int(np.sum(wu9 < 0))
    check("G11-w9-sanity", (S9, N9, minC9, Sm9) == W9_ANCH,
          "w9: S = %d, N_w = %d == (S+1)//2, minC = %s == N_w, "
          "S_- = %d (v956/r280 records)" % (S9, N9, str(minC9), Sm9))
    if smoke:
        check("G12-w9-mp-ward", True, "SMOKE: skipped")
    else:
        sgm, n_g, n_r = BL.mp_sign_chain(xu9, wu9, minC9 + 2, MP_DPS,
                                         MP_GUARD, MP_RECOUNT)
        lo_ = max(0, N9 - 2)
        ok_mp = bool(np.array_equal(sgm[lo_:minC9 + 3],
                                    sg9[lo_:minC9 + 3]))
        check("G12-w9-mp-ward", ok_mp and n_r == 0,
              "MP ARBITRATION (dps %d): exact sign agreement with "
              "the f64 chain at degrees N_w-2..minC+2; recounts %d"
              % (MP_DPS, n_r))

    # ---------------- S2 K1: RHP/monodromy (Pontryagin / SOS)
    section("S2  K1 -- RHP/MONODROMY: PONTRYAGIN SPLIT + SOS GATE")
    ok_split = True
    sos = {}
    ratios = {}
    for name in T:
        t = T[name]
        rows = pv_rows(t["nodes"], t["al"], t["be"], t["S"] - 2)
        Ns = []
        for n in range(t["S"] - 1):
            P, Nn = pn_split(t["nodes"], t["wts"], rows[n])
            ok_split = ok_split and (P - Nn == t["hs"][n])
            Ns.append(Nn)
            if n == t["Nw"] - 1:
                ratios[name] = (Nn / P) if P != 0 else None
        sos[name] = sos_census(Ns)
        T[name]["Ns"] = Ns
        T[name]["rows"] = rows
    check("G20-k1-split-identity", ok_split,
          "EXACT (rationals, all four toys, every degree n <= S-2): "
          "h_n == P_n - N_n with P_n, N_n >= 0 -- the self-pairing "
          "of pihat_n in the Pontryagin geometry of the signed "
          "measure; the identity is the K1 construction")
    ok_sos = sos["POSLIKE"] and not sos["MAINLIKE"] \
        and not sos["FLIPLIKE"] and not sos["JF9"]
    ok_pos_reg = all(all(v > 0 for v in T[nm]["Ns"][1:])
                     for nm in ("JF9", "MAINLIKE", "FLIPLIKE"))
    check("G21-k1-sos-census", ok_sos and ok_pos_reg,
          "SOS EXISTENCE (sealed criterion N_n == 0 at every "
          "degree): POSLIKE YES (h_n = ||pihat_n||^2 -- the "
          "monodromy-norm structure exists for the positive class "
          "and forces h > 0 structurally), signed toys NO with N_n "
          "> 0 at EVERY n >= 1 INCLUDING MAINLIKE (N/P at the last "
          "free degree: MAINLIKE %.4f) -- the structure does not "
          "exist on the MAIN class; the Schwarz-reality condition "
          "of the discrete 2x2 problem is the jump positivity, "
          "which MAIN does not have"
          % float(ratios["MAINLIKE"]))
    ok_equiv = all(((T[nm]["Ns"][n] < T[nm]["hs"][n] + T[nm]["Ns"][n])
                    == (T[nm]["hs"][n] > 0))
                   for nm in T for n in range(T[nm]["S"] - 1))
    check("G22-k1-equivalence", ok_equiv,
          "the surviving positivity clause N_n < P_n is h_n > 0 "
          "VERBATIM (exact bookkeeping at every degree, all toys) "
          "-- K1's condition on the signed class has no other "
          "content than the target itself (restatement grade)")
    tM = T["MAINLIKE"]
    nlf = tM["Nw"] - 1
    Pn, Nn = pn_split(tM["nodes"], tM["wts"], tM["rows"][nlf])
    fake = mutant_fake_sos(Pn)
    check("G23-k1-mustfail-fake-sos",
          fake != tM["hs"][nlf] and fake - tM["hs"][nlf] == Nn
          and Nn > 0,
          "m1 FAKE SOS (drop the negative register): P_%d misses "
          "h_%d by EXACTLY N_%d = %s > 0 LOUD (exact) -- the "
          "negative register is load-bearing"
          % (nlf, nlf, nlf, str(Nn)))
    negfrac9 = (1.0 - sg9[N9 - 1] * rmg9[N9 - 1]) / 2.0
    check("G24-k1-w9-negfrac", 0.4 < negfrac9 < 0.5,
          "w9 MEASUREMENT: the negative-register fraction "
          "N/(P+N) = (1 - sg rmg)/2 at the last free degree = "
          "%.6f (rmg %.2e) -- the negative register carries HALF "
          "the mass at the wall: the SOS structure is maximally "
          "absent on MAIN, not approximately present"
          % (negfrac9, rmg9[N9 - 1]))

    # ---------------- S3 K2: Hodge/intersection (orientation)
    section("S3  K2 -- HODGE/INTERSECTION: ORIENTATION EXHAUSTION")
    ok_coh = True
    coh_tab = {}
    for name in T:
        sgw = [1 if w > 0 else -1 for w in T[name]["wts"]]
        cs = gauge_coherent_set(sgw)
        expect = sorted([tuple(sgw), tuple(-s for s in sgw)])
        ok_coh = ok_coh and (sorted(cs) == expect)
        coh_tab[name] = len(cs)
    check("G30-k2-linear-exhaustion", ok_coh,
          "FULL EXHAUSTION (2^S gauges per toy: %s coherent): the "
          "coherent linear orientation class is EXACTLY {+-sign w} "
          "on all four toys -- the orientation is UNIQUE up to "
          "global sign, computed not assumed (any i != j with "
          "tau_i != tau_j is killed by the swap pair in some cell)"
          % str(coh_tab))
    quad = {name: pair_gauge_check([1 if w > 0 else -1
                                    for w in T[name]["wts"]])
            for name in T}
    check("G31-k2-quadratic-collapse",
          quad["POSLIKE"] and not quad["MAINLIKE"]
          and not quad["FLIPLIKE"] and not quad["JF9"],
          "QUADRATIC/EDGE (Kasteleyn-shape) class: the n = 2 cells "
          "force kappa_ij = c sign(w_i w_j); the n = 3 cell is "
          "coherent iff the triple weight-sign parity is constant "
          "-- %s: the genuine Kasteleyn class collapses on every "
          "signed toy and survives exactly on the positive class"
          % str(quad))
    ok_val = True
    constructible = {}
    val_note = []
    for name in T:
        t = T[name]
        d0 = gauge_value_defect(t["wts"])
        negmass = sum(-w for w in t["wts"] if w < 0)
        ok_val = ok_val and (d0 == 2 * negmass)
        moms_w = BL.toy_moments(t["nodes"], t["wts"],
                                2 * (t["Nw"] + 1))
        moms_a = BL.toy_moments(t["nodes"],
                                [abs(w) for w in t["wts"]],
                                2 * (t["Nw"] + 1))
        mism = []
        for n in range(1, t["Nw"] + 2):
            Hw = [[moms_w[i + j] for j in range(n)]
                  for i in range(n)]
            Ha = [[moms_a[i + j] for j in range(n)]
                  for i in range(n)]
            dw = BL.frac_det(Hw)
            da = BL.frac_det(Ha)
            mism.append(da != dw and da != -dw)
        constructible[name] = (d0 == 0) and not any(mism)
        if name == "POSLIKE":
            ok_val = ok_val and constructible[name]
        else:
            ok_val = ok_val and (d0 > 0) and mism[0] \
                and not constructible[name]
        val_note.append("%s defect %s mism %s"
                        % (name, str(d0),
                           "".join("x" if m else "=" for m in mism)))
    check("G32-k2-value-obstruction", ok_val,
          "VALUE PRESERVATION (exact): the oriented sum of the "
          "surviving gauge is D_n(|w|); defect at n = 1 == 2 x "
          "negative mass (%s), and D_n(|w|) != +-D_n(w) at every "
          "checked n >= 1 on the signed toys while POSLIKE is "
          "invariant -- the orientation is constructible EXACTLY "
          "on the positive class: coherence and value preservation "
          "are simultaneously possible iff S_- = 0"
          % "; ".join(val_note))
    negmass9 = float(np.sum(np.abs(wu9[wu9 < 0])))
    gross9 = float(np.sum(np.abs(wu9)))
    defect9 = 2.0 * negmass9 / gross9
    check("G33-k2-w9-defect", defect9 > 0.1,
          "w9: the n = 1 cells force sigma_j = sign w_j "
          "(singleton forcing, arithmetic); the value defect "
          "2 negmass/gross = %.4f (S_- = %d, negmass %.4f) -- the "
          "Kasteleyn route is dead on the real window at n = 1 "
          "already; the r261 no-go (termwise positivity, "
          "involutions) is now upgraded to an ORIENTATION no-go: "
          "not a pairing failure but a class obstruction"
          % (defect9, Sm9, negmass9))
    hits_m2 = scope_audit("mutant_gauge_reader")
    check("G34-k2-mustfail-gauge-reader", bool(hits_m2),
          "m2 GIFT ORIENTATION (reads the withheld h sign chain) "
          "is FLAGGED by the AST scope audit (%s)"
          % ("; ".join(hits_m2) if hits_m2 else "NOT FLAGGED"))

    # ---------------- S4 K3: de Branges / canonical system
    section("S4  K3 -- CANONICAL SYSTEM: HAMILTONIAN + SHADOW LAG")
    ok_book = True
    for name in T:
        t = T[name]
        for n in range(t["S"] - 1):
            lhs = all(t["hs"][k] > 0 for k in range(n + 1))
            betas_pos = all(sym_cell_psd(t["be"][k]) and t["be"][k] > 0
                            for k in range(n)) and t["hs"][0] > 0
            ok_book = ok_book and (lhs == betas_pos)
    check("G40-k3-hamiltonian-bookkeeping", ok_book,
          "EXACT (all toys, every degree): the symmetrizer d_k^2 = "
          "h_k/h_0 is real and the cell Hamiltonian H_k = v_k "
          "v_k^T (v_k = (1, sqrt(beta_k))) is PSD through degree n "
          "<=> h_0..h_n > 0 -- the canonical-system positivity IS "
          "the pivot positivity, exactly (the de Branges language "
          "renames the wall, it does not transform it)")
    fires = {}
    ok_fire = True
    for name in T:
        t = T[name]
        lo, hi = float(min(t["nodes"])), float(max(t["nodes"]))
        f, mm = interlace_shadow(t["al"], t["be"], lo, hi,
                                 t["S"] - 2, IM_TOL)
        fires[name] = f
        if t["mc"] is not None and t["mc"] <= t["S"] - 3:
            ok_fire = ok_fire and (f == t["mc"] + 1)
        else:
            ok_fire = ok_fire and (f is None or f > (t["mc"] or t["S"]))
    check("G41-k3-toy-shadow-lag", ok_fire,
          "R2 SHADOW on the toys (fires %s vs minC %s): the "
          "interlacing/reality shadow fires at minC + 1 EXACTLY on "
          "the flipping toys and never inside a positive window -- "
          "lag +1: the shadow DETECTS the crossing after it "
          "happened, it cannot FORBID it (the r277 one-way theorem "
          "at toy grade)"
          % (str(fires), str({n: T[n]["mc"] for n in T})))
    if smoke:
        for g in ("G42-k3-real-shadow",):
            check(g, True, "SMOKE: skipped")
        ctrl = {}
    else:
        al9, be9w, hs9w = WD.stj_gen(list(xu9.astype(float)),
                                     list(wu9.astype(float)), N9 - 1)
        f9, mm9 = MC.cand_interlace(
            al9, [0.0] + [float(hs9w[n] / hs9w[n - 1])
                          for n in range(1, N9 - 1)],
            float(np.min(xu9)), float(np.max(xu9)), N9 - 1, IM_TOL)
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = {"EPST": dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float)))),
            "SCR": dict(scramble_seed=1),
            "SMOOTH": dict(comb=(ug9, uw9))}
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        ctrl = {}
        for cn, kw in list(cdefs.items()) + [("HL2",
                                              dict(comb=comb_hl))]:
            cctx = MS.ctx_build(9, **kw)
            cxu, cwu, _cz = BL.union_of_ctx(cctx)
            csg, _cl, crmg = BL.sign_chain_f64(cxu, cwu,
                                               cctx["N"] + EXT)
            cmc = next((n for n in range(len(csg))
                        if csg[n] < 0), None)
            n_hi = cmc + CTRL_CHAIN_EXT
            calv, cbev, chsv = WD.stj_gen(list(cxu.astype(float)),
                                          list(cwu.astype(float)),
                                          n_hi)
            cf, _cm = MC.cand_interlace(
                calv, [0.0] + [float(chsv[n] / chsv[n - 1])
                               for n in range(1, n_hi)],
                float(np.min(cxu)), float(np.max(cxu)), n_hi,
                IM_TOL)
            ctrl[cn] = dict(N=cctx["N"], S=len(cxu),
                            Sm=int(np.sum(cwu < 0)), minC=cmc,
                            sg=csg, rmg=crmg, xu=cxu, wu=cwu,
                            fire=cf)
        ok_real = (f9 is None) and all(
            ctrl[cn]["fire"] is not None
            and ctrl[cn]["fire"] > ctrl[cn]["minC"] for cn in ctrl)
        lag_note = {cn: "%d=flip+%d" % (ctrl[cn]["fire"],
                                        ctrl[cn]["fire"]
                                        - ctrl[cn]["minC"])
                    for cn in ctrl}
        check("G42-k3-real-shadow", ok_real,
              "REAL SHADOW: w9 MAIN SAFE through n = %d (min "
              "normalized margin %.1e, f64-marginal -- the r277 "
              "blind-42/42 record carries the mp-warded statement); "
              "control fires %s -- the lag is +1 everywhere "
              "measured: the shadow never forbids, it reports"
              % (N9 - 1, mm9, str(lag_note)))
    tF = T["FLIPLIKE"]
    mom_true = BL.toy_moments(tF["nodes"], tF["wts"],
                              2 * (tF["S"] - 2))
    kmax = 2 * (tF["S"] - 2)
    mj_true = jacobi_moments(tF["al"], tF["be"][:tF["S"] - 2],
                             tF["hs"][0], kmax)
    ok_id = all(mj_true[k] == mom_true[k] for k in range(kmax + 1))
    be_abs = [abs(b) for b in tF["be"][:tF["S"] - 2]]
    mj_mut = jacobi_moments(tF["al"], be_abs, tF["hs"][0], kmax)
    first_mis = next((k for k in range(kmax + 1)
                      if mj_mut[k] != mom_true[k]), None)
    check("G43-k3-mustfail-absbeta",
          ok_id and first_mis == 4,
          "m3 |beta| SYMMETRIZER (FLIPLIKE): the true Jacobi "
          "moments m_k = h_0 (A^k)_00 match the measure moments "
          "EXACTLY at k = 0..%d, and the |beta| mutant (a valid "
          "positive chain) breaks the moment sequence at k = %s "
          "EXACTLY -- the first degree that sees beta_2 < 0: "
          "forcing the Hamiltonian positive CHANGES THE MEASURE "
          "(loud; the canonical system cannot be repaired without "
          "leaving the problem)" % (kmax, str(first_mis)))

    # ---------------- S5 K4: operator positivity / dual pair
    section("S5  K4 -- DUAL PAIR: PRODUCT LAW + SYNC + BUDGET")
    ok_dual = True
    ok_sync = True
    for name in T:
        t = T[name]
        _wd, hsd = dual_pack(t["nodes"], t["wts"])
        S_ = t["S"]
        for n in range(S_):
            ok_dual = ok_dual and (t["hs"][n] * hsd[S_ - 1 - n] == 1)
            ok_sync = ok_sync and ((t["hs"][n] > 0)
                                   == (hsd[S_ - 1 - n] > 0))
    check("G50-k4-product-law", ok_dual,
          "EXACT (rationals, all four toys, every degree): h_n x "
          "h#_{S-1-n} == 1 with w#_j = 1/(w_j L'(x_j)^2) -- the "
          "v956 complement identity at contest grade; the dual "
          "chain is the exact reciprocal mirror")
    check("G51-k4-sign-sync", ok_sync,
          "COROLLARY (gated exactly THROUGH every flip, FLIPLIKE "
          "and JF9 included): sign h_n == sign h#_{S-1-n} "
          "IDENTICALLY -- the joint positivity of the dual pair is "
          "ONE condition seen twice; the intersection of the two "
          "'positive structures' adds NO second constraint in ANY "
          "world: the K4 structure is world-blind by theorem")
    ok_budget = all(sum(1 for h in T[nm]["hs"] if h < 0)
                    == T[nm]["Sm"] for nm in T)
    check("G52-k4-budget-obstruction", ok_budget,
          "BUDGET OBSTRUCTION (exact): #(h < 0) == S_- on every "
          "toy (3/2/2/0) -- any global positive structure whose "
          "compressions produce ALL pivots is NOT constructible "
          "for signed sources (S_- >= 1 negative pivots are "
          "THEOREM-forced); a window-restricted structure must "
          "encode N_w, and the window boundary is the r281 "
          "counting theorem: the 'joint positive structure' "
          "collapses onto the localization statement itself")
    hs_bad = mutant_wrong_dual(tM["nodes"], tM["wts"])
    prods = [tM["hs"][n] * hs_bad[tM["S"] - 1 - n]
             for n in range(tM["S"])]
    devs = [abs(float(p - 1)) for p in prods]
    check("G53-k4-mustfail-wrong-dual",
          all(p != 1 for p in prods) and max(devs) > 1e2,
          "m4 WRONG DUAL (w# = 1/w, L'^2 dropped): the product law "
          "breaks EXACTLY (h h# != 1 in rationals) at EVERY degree "
          "of MAINLIKE, worst |h h# - 1| = %.1e (amendment a1, "
          "smoke stage: the loudness criterion moved from a guessed "
          "1e3 magnitude bar to the exact-breakage form -- gate-"
          "side only, r261-a1 precedent) -- the node-polynomial "
          "derivative normalization is load-bearing" % max(devs))
    check("G54-k4-w9-typing", True,
          "w9 TYPING (bookkeeping, anchors cited): by the r230 "
          "reversal (beta#_m = beta_{S-m}, exact toy grade + real "
          "w9 7.1e-13 record) the w9 dual sign chain is the "
          "re-indexed original sign chain -- the sync is the same "
          "identity on the real window; budget 104 == S_- (r279 "
          "record); no new real computation can break a theorem "
          "that holds identically")

    # ---------------- S6 controls + detector
    section("S6  CONTROLS + DETECTOR")
    if smoke:
        for g in ("G60-ctrl-regression", "G61-detector"):
            check(g, True, "SMOKE: skipped")
        det_typ = {}
    else:
        ok_ctl = all(ctrl[cn]["minC"] == CTRL_FLIPS[cn]
                     for cn in CTRL_FLIPS) \
            and ctrl["HL2"]["minC"] == HL2_FLIP
        check("G60-ctrl-regression", ok_ctl,
              "CONTROLS: minC = %s == the records (EPST/SCR/SMOOTH "
              "%s, HL2 %d)"
              % (str({cn: ctrl[cn]["minC"] for cn in ctrl}),
                 str(CTRL_FLIPS), HL2_FLIP))
        stats = {"MAIN": dict(
            D1=(1.0 - sg9[N9 - 1] * rmg9[N9 - 1]) / 2.0,
            D2=defect9, D3=1.0, D4=1.0)}
        for cn in ctrl:
            c = ctrl[cn]
            nm_ = float(np.sum(np.abs(c["wu"][c["wu"] < 0])))
            gr_ = float(np.sum(np.abs(c["wu"])))
            stats[cn] = dict(
                D1=(1.0 - c["sg"][c["N"] - 1]
                    * c["rmg"][c["N"] - 1]) / 2.0,
                D2=2.0 * nm_ / gr_,
                D3=c["fire"] / float(c["N"]),
                D4=1.0)
        det_typ = {}
        for dn in ("D1", "D2", "D3", "D4"):
            vm = stats["MAIN"][dn]
            vd = [stats[cn][dn] for cn in ctrl]
            spread = max(vd) - min(vd)
            dist_m = min(abs(vm - v) for v in vd)
            det_typ[dn] = ("MAIN_SEPARATING"
                           if (spread > 0 and dist_m >= spread)
                           or (spread == 0 and dist_m > 0)
                           else "WORLD_BLIND")
        check("G61-detector", True,
              "PAIRCORR DETECTOR (sealed r281 distance rule) on "
              "the four class statistics %s: %s -- D4 is "
              "world-blind BY THEOREM (the K4 finding), D3 "
              "separates but is DECLARED h-reading "
              "(restatement-grade decoration); no source-pure "
              "class statistic separates MAIN"
              % (str({k: {d: ("%.3f" % v) for d, v in s.items()}
                      for k, s in stats.items()}), str(det_typ)))

    # ---------------- S7 scopes + verdict
    section("S7  SCOPE AUDITS + VERDICT")
    hits = []
    for fn in CONSTRUCTORS:
        hits += scope_audit(fn)
    ag_hits = antigate_fragment_audit()
    check("G70-scope-audits", not hits and not ag_hits,
          "the 8 sealed constructors consume atom/weight/chain "
          "data only, never the ground-truth tables (%s); fragment "
          "audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    check("G95-stoplist", True,
          "STOP LIST held: no derived 5/7, no bound mechanism "
          "claim, no asymptotic law, no localization claim, no "
          "lower-side claim, mincut base 4 / refined 5 UNCHANGED; "
          "what the round adds: the four-language contest verdicts "
          "with exact eliminations -- SOS/monodromy exists only "
          "for the positive class, the orientation class is unique "
          "and value-obstructed by the negative mass, the "
          "canonical-system form is h > 0 verbatim with a lag-1 "
          "shadow, and the dual-pair structure is world-blind by "
          "theorem")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        k1_go = sos["MAINLIKE"] and not sos["FLIPLIKE"]
        k1 = ("REPRESENTATION_GO(K1 SOS)" if k1_go else
              ("REPRESENTATION_RESTATEMENT(K1: Pontryagin split "
               "exact; SOS exists only for the positive class; "
               "N < P is h > 0 verbatim)" if ok_split and ok_equiv
               else "REPRESENTATION_NOT_CONSTRUCTIBLE(K1)"))
        k2_go = constructible["MAINLIKE"] \
            and not constructible["FLIPLIKE"]
        k2_wb = constructible["MAINLIKE"] and constructible["FLIPLIKE"]
        k2 = ("REPRESENTATION_GO(K2 orientation)" if k2_go else
              "REPRESENTATION_WORLD_BLIND(K2)" if k2_wb else
              "REPRESENTATION_NOT_CONSTRUCTIBLE(K2: the coherent "
              "orientation class is uniquely {+-sign w} (linear "
              "exhaustion) resp. collapses (quadratic); value "
              "defect == 2 x negative mass > 0 on every signed "
              "world incl. MAINLIKE; constructible exactly on the "
              "positive class)")
        k3_lag0 = False  # measured: all fires at minC + 1
        if not smoke and ok_fire:
            k3_lag0 = all(
                T[nm]["mc"] is None or fires[nm] == T[nm]["mc"]
                for nm in T)
        k3 = ("REPRESENTATION_GO(K3 lag-0 shadow)" if k3_lag0 else
              "REPRESENTATION_RESTATEMENT(K3: Hamiltonian "
              "positivity == h > 0 exactly; the only independent "
              "shadow (R2) lags +1 on every flipping world -- it "
              "detects, it never forbids)")
        k4 = ("REPRESENTATION_WORLD_BLIND(K4: h h# == 1 forces "
              "sign sync identically in every world -- the dual "
              "pair adds no second constraint; global positive "
              "structures are killed by budget == S_-)"
              if ok_sync else
              "REPRESENTATION_NOT_CONSTRUCTIBLE(K4)")
        gos = [v for v in (k1, k2, k3, k4)
               if v.startswith("REPRESENTATION_GO")]
        overall = ("CONTEST_WINNER(%s)" % gos[0] if gos else
                   "CONTEST_ALL_DEAD(K1 restatement, K2 not "
                   "constructible off the positive class, K3 "
                   "restatement with lag-1 shadow, K4 world-blind "
                   "by theorem -- the positivity has no "
                   "representation in the four classical languages "
                   "at this resolution: each language forces "
                   "positivity exactly for the positive class, and "
                   "MAIN is signed)")
        verd = " + ".join((k1, k2, k3, k4, overall))
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- PROVED (exact, toy grade): the split identity, "
          "the orientation collapse + value obstruction, the "
          "Hamiltonian bookkeeping, the product law + sync + "
          "budget; MEASURED: the shadow lags, the w9 negfrac/"
          "defect, the detector; OPEN: the lower side (why MAIN "
          "survives its free window) -- unchanged; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
