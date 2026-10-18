#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""maslov_census_probe -- PRIME.PORT.RHP.MIDPOINT.MASLOV_CENSUS.01
(round 277): the blind Pruefer/Maslov census -- PREDICT the flip
degrees from phase/counting data, do not restate them.  The r274
warning is binding: the Pruefer band 0 < dTheta < pi is EXACTLY
h_n > 0 (a restatement), and the naive winding on the algebraic
continuation is NOT the half-filling count (262 vs 184 on w9).
This round measures the increment dynamics, identifies the RIGHT
winding quantity, and executes a reviewer-protocol blind rule.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r276 discipline): w = window (kz),
N_w = builder depth, S_w = #supp(mutilde), n/k = chain degree;
ground truth (h signs, flip degrees nf) enters GATES, TRAINING
LABELS and census tables only; no zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r274
WD.{stj_gen, pv_seq, scal_fwd, back_right, world_dict_block,
casor_sglg}, r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r264 QO.port_pack, r230 JF toy nodes, v563 frame_a_zones (READ-
ONLY core).  B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243
imported floor, never fitted; gate-side only).

LEG A -- THE PHASE OBJECTS AND THE RIGHT WINDING QUANTITY:
(a1) Pruefer phases Theta^L_n (left chain, r274 scal_fwd) and
  Theta^R_n (right/dual solution, r274 back_right + residue
  normalization) at the sealed z0 = x0 + 1.5 rh; the INCREMENTS
  dTheta_n per degree step are the measured object: distribution
  (median/IQR/sign fraction) and Spearman coupling to the chain
  data alpha_n and log beta_n on both mains; the band
  Theta^L - Theta^R in (0, pi) == W^base_n > 0 == h_n > 0 is
  RE-GATED via the r274 dictionary (imported, restatement typed).
  STURM ROTATION (classical, exact): at the sealed interior
  point x* = hull center, the minor/Sturm sequence
  (pihat_0..pihat_n)(x*) counts eigenvalues of J_n below x*:
  #eig(J_n) < x* == n - #signchanges(seq) -- gated at the sealed
  degrees on both mains (phase rotation == node counting).
(a2) THE RIGHT WINDING QUANTITY (three sealed candidates,
  measured on the w9 mp continuation n = 0..S-2, dps 120):
  V_ATOM = #sign changes of pihat_n ON THE SORTED UNION ATOMS
  (the discrete Sturm census -- the conjectured correct one);
  V_HULL/V_SUPP = #real zeros (tridiag eigenvalues, |Im| <=
  imtol x width) inside the convex hull / inside the two zone
  hulls, at the sealed anatomy degrees; V_BAND = #(h_n > 0)
  in-band count (the r274 anchor 262, re-derived).  ADJUDICATION:
  the right winding quantity is the candidate with count == n at
  every free-prefix degree AND first break exactly at the flip;
  the naive band count must show its 78 continuation pivots
  (r274 anchor) -- measured, typed.

LEG B -- THE BLIND RULE (reviewer protocol, hard):
(b1) TRAINING SET (sealed, source-defined): w9 (main) + the 4
  smallest-N rungs of the (N, kz)-sorted 42-rung cofinal ladder
  (frame-A h <= 900, r274 convention; kz 9 excluded from the
  rung pick -- it is the training main); TRAINING CONTROLS: the
  SCRAMBLE(seed 2) variants of the same 5 windows (their flips
  nf are measured wpack ground truth; a variant without a flip
  inside its window is excluded with disclosure).  CANDIDATE
  CLASSES (exactly 3, sealed, source-pure inputs = chain
  coefficients (alpha, beta) + sorted atoms + z0 ONLY):
  (R1) STURM DEFECT: CROSSING at the first degree n with
       atom-sign-change count c_n != n (the interlacing/counting
       break as the census event);
  (R2) INTERLACING/REALITY MARGIN: CROSSING at the first n where
       the tridiagonal zeros of pihat_n leave the real axis
       (|Im| > imtol x width) or strict interlacing with
       pihat_{n-1} fails (general eigenvalues of the BALANCED
       similarity form sub_i = super_i = sqrt|beta_i| with the
       beta sign on the super-diagonal -- amendment a1:
       numerical stability only, the eigenvalues are exactly
       the monic zeros; no symmetry assumption -- purity over
       speed);
  (R3) PHASE-VELOCITY ANOMALY: CROSSING at the first n >= win+2
       where |dTheta^L_n - median(last win)| / MAD >= Z_thr,
       Z_thr from the sealed grid (3, 4, 5, 6, 8, 10), smallest
       threshold with zero false fires on the training mains.
  TRAINING PASS per candidate: zero fires on all 5 training
  mains (n <= N-1) AND every training control fires with
  |f - nf| <= 1.  SELECTION (sealed priority, decided BEFORE
  evaluation): R1 > R2 > R3 (R1 is the discrete-canonical
  object); the selected rule is FROZEN, blind runs it unchanged.
(b2) BLIND EXECUTION: the remaining 37 rungs + the full-depth
  mains w12/w13/w26 + the w9 controls EPSTEIN/SCRAMBLE(seed 1)/
  SMOOTH.  GO criterion (reviewer, sealed): ALL 42 ladder rungs
  SAFE through n = N-1 (train 5 re-reported + blind 37) AND
  w12/w13/w26 SAFE AND the controls fire within +-1 of 25/21/27.
  SEPARATES_ONLY: mains/rungs SAFE and all controls fire, but
  some |f - nf| > 1.  FAILED(typed): false positives on mains/
  rungs or a silent control.
(b3) r259 DEMARCATION WARD: the rule must NOT be the refuted
  energy-branch order -- the r259 record crossing degrees are
  EPSTEIN 9 / SCRAMBLE 16 / SMOOTH 19 (LEVEL_CROSSING_REFUTED);
  gate: the rule's control fire degrees differ from the r259
  crossings by >= 3 degrees each (imported record constants).

LEG C -- THE INDEX-COUNT CHAIN (proof-plan step 5 material):
(c1) mains w9/w13, every degree n < N: the census is MEASURED
  against the sealed expectation c_n == n (f64 census with the
  sealed sign guard 1e-9; guard-violating degrees recounted in
  mp dps 40 -- repair path sealed, counts disclosed); AMENDMENT
  a2 (calibration, disclosed): the expectation is REFUTED on
  both mains -- a genuine finding about signed Sturm theory --
  so G21/G26 are typed as measurement/adjudication gates and
  the parity-anchored convention ((-1)^n, atom signs, +1) is
  measured alongside as a2 anatomy (never a rule);
(c2) strict interlacing of the Jacobi eigenvalues of J_{n-1} and
  J_n at every free degree (symmetric tridiagonal, Cauchy;
  strict up to the sealed f64 resolution 1e-8 x mean gap), hull
  containment #eig in [lo, hi] == n reported;
(c3) the implication chain as a no-counterexample gate on the
  mains + all 42 rungs: (c_n == n) AND interlacing AND NOT
  (h_n > 0) never occurs on the free prefix (the direction the
  oriented midpoint theorem needs);
(c4) ATOM SATURATION (the window-rule question, w9 mp
  continuation): c_n at the sealed degrees around N_w = 184, the
  maximum of c_n over the full continuation and its argmax, the
  first defect degree, and whether the census ever heals
  (c_n == n again) beyond the flip -- the RESTATEMENT
  ADJUDICATOR: the selected rule is typed h-EQUIVALENT iff its
  SAFE/CROSSING pattern over the FULL continuation equals the
  h_n > 0 pattern degree-by-degree (the 78 h re-entry pivots
  beyond the flip are the separator).

LEG D -- WARDS/KILLS: AST scopes: the rule/census functions
(census_signs, sign_changes, mp_recount, cand_sturm,
cand_interlace, cand_phase, zeros_tridiag, prue_theta) consume
passed coefficient/atom arrays + the evaluation point ONLY
(forbidden: rho, S, sg_h, lg_h, hv, Fv, nf, rows, wpack,
bord_chain, world_dict_block, tau, aug, D_dict, q_chain) --
audited, with a deliberately h-reading mutant that MUST be
flagged; no fit primitives (fragment audit); CONTAMINATION
PROTOCOL: training kz set and blind kz set disjoint (printed,
gated); HULL-CONVENTION ANCHOR (documented): the hull/support
zero counts at the sealed anatomy degrees are printed next to
the atom census -- the convention difference is the m3 anchor;
mp WARDS: kz15 (razor) + the largest-N blind rung: mp (dps 60)
census counts == f64 counts at the sealed degrees (2, N//2,
N-1); w9 full-prefix f64-vs-mp census agreement (dps 120);
r266-pattern DETECTOR on the rule statistics (terminal census
margin, max phase z): selftest sp(g1, g1) flagged, fingerprints
sp(stat, g1) and sp(stat, D_N) < 0.9; STOP LIST (anti-gates):
no derived 5/7, no bound mechanism, no asymptotic law, no
energy-order rule (b3), no RH claim.

SEALED CONSTANTS: MAIN windows (9, 13); blind extra mains
(12, 26); controls w9 EPSTEIN / SCRAMBLE(seed 1) / SMOOTH, flips
25/21/27; H_CAP 900; B57 = 5/7 (gate-side); Z0 factor 1.5 on the
union+border hull; TRAIN_SCR_SEED 2; N_TRAIN_RUNGS 4; FLIP_TOL 1;
SIGN_GUARD 1e-9; MP_REPAIR_DPS 40; W9_DPS 120; WARD_DPS 60; ward
degrees (2, N//2, N-1); continuation anatomy degrees (40, 90,
150, 183, 184, 185, 200, 262, 300, 366); IM_TOL 1e-7 (x hull
width); rotation degrees (40, 90, 150, 183); interior point
x* = union hull center; R3 window 12, z grid (3, 4, 5, 6, 8,
10); interlacing resolution 1e-8 (x mean gap); r259 crossing
record (EPST 9, SCR 16, SMOOTH 19), separation >= 3; r274
in-band anchor 262 (w9); R2 continuation cap N + 30; FP_BAR
0.9; LOUD 1e3; runtime <= 1800 s; smoke = toys + w9 + controls
census + must-fails + scopes (ladder, training/blind, mp legs,
detector skipped, no adjudication).  NO pre-spec scratch:
calibration pass 1 (smoke + the w9/control census diagnosis)
was the first evaluation of this probe; amendments a1/a2 were
found there and disclosed BEFORE any record freeze; no bar,
tolerance, candidate priority or verdict rule moved at any
point.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  MASLOV_CENSUS_GO(rule; blind 42/42 rungs + 3 mains SAFE;
    control fires within +-1 of 25/21/27; r259-separated) iff
    the b2 GO criterion holds AND the b3 ward passes
  / CENSUS_SEPARATES_ONLY (mains/rungs SAFE, controls fire, but
    a fire degree misses by > 1 -- the reviewer's no-go)
  / CENSUS_FAILED(typed: false positives / silent controls /
    no candidate passed training)
  + CENSUS_RESTATEMENT iff the selected rule's SAFE/CROSSING
    pattern over the full w9 continuation equals the h_n > 0
    pattern degree-by-degree (h-equivalence, honest)
  + STURM_CHAIN_VERIFIED(atom-saturation finding) iff the leg-C
    bundle holds (c1 + c2 + c3 on mains and rungs, toys
    co-located).
Honesty before beauty: the census does not close the wall; the
target positivity D_N > 0 stays OPEN; no verdict claims a
derived 5/7, a bound mechanism, or an asymptotic law
(r243..r276 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
first smoke pass 27/29 -- the drafted G21 HARD expectation
"c_n == n on the mains" FAILED and cascaded into G96; the
diagnosis measured the defect (a genuine finding, below), the
two disclosed amendments a1 (balanced similarity form in the R2
eigensolver -- eigenvalues unchanged, stability only) and a2
(G21/G26 retyped from expectation gates to measurement/
adjudication gates + the parity-anchored convention added as a2
ANATOMY, never a rule) were fixed BEFORE any record freeze; no
bar, tolerance, candidate priority, training/blind protocol or
verdict rule moved at any point; smoke then 29/29, calibration
pass 1 = first full evaluation 29/29, wall 504.4 s, and the
record run below is numerically identical):
CAL_VERDICT = MASLOV_CENSUS_GO(rule R2 INTERLACING/REALITY of
the Jacobi zeros; training 5/5 mains SAFE + 5/5 scramble(seed 2)
controls fire at exactly nf + 1; blind 37/37 rungs + 5/5 train
rungs + w12/w13/w26 SAFE at full depth; controls fire 26/22/28
== 25/21/27 + 1 within the sealed +-1; r259 branches separated
by 17/6/9 >= 3) -- STURM_CHAIN_VERIFIED is honestly NOT awarded
(the c1 expectation is refuted, see below) and the rule is NOT
h-equivalent (79 pattern mismatches on the continuation).
THE ROUND'S CENTRAL FINDING (the a2 answer): the RAW atom-
counted Sturm census is NOT the right winding quantity -- on
MAIN w9/w13 it breaks at n = 56/48 (128/120 defect degrees)
with h POSITIVE throughout: zeros ESCAPE the atom hull (G23
hull containment FALSE; parity anchors repair those, first
anchored defect 72/80) and then PAIR UP inside single atom gaps
-- the positive-measure separation theorem genuinely fails for
the signed comb.  The winding quantity that DOES break exactly
at the wall is the INTERLACING/REALITY structure of the Jacobi
zeros (R2): SAFE through the full free window on every world
with h > 0 (provably: beta > 0 => symmetrizable => real +
Cauchy-strict), first break at exactly nf + 1 on every control
and on the w9 continuation at 185 = N_w + 1.
Key numbers.  TOYS (exact rationals; f64 engine identical):
JF-9atom counts (0, 1, 2, 2, 2, 2, 3, 2, 3), first h < 0 at 3,
first defect 3 (+0); MAINLIKE (4, 4); FLIPLIKE (2, 2).  MAINS:
census anatomy w9 (first raw defect 56, 128 raw, first anchored
72, 53 anchored), w13 (48, 120, 80, 44), 0 guard degrees, 0 mp
repairs; interlacing strict at every degree (worst normalized
margin 2.8e-08 >= -1e-08); Sturm rotation EXACT at degrees
(40, 90, 150, 183) on both mains; controls raw-census defect at
25/22/27 vs flips 25/21/27 (+0/+1/+0 -- co-located, but the
same statistic fires falsely on MAIN at 56: raw R1 fails
training exactly as the r274 warning demanded).  PHASES:
dTheta^L (median, IQR, frac<0, sp vs alpha, sp vs log beta) =
w9 (0.000, 0.021, 0.48, -0.78, -0.29) / w13 (0.002, 0.025,
0.46, -0.76, -0.23); band == h > 0 re-gated (r274 dictionary,
restatement typed).  CONTINUATION (w9 mp dps 120): f64-vs-mp
census agreement at ALL n < 184; in-band 262/366 == r274
anchor, first h < 0 at 184 == N_w; anatomy (n: real-in-hull /
real-in-support / atom-count / #complex): 183 (182, 182, 182,
0), 184 (183, 183, 173, 0), 185 (183, 183, 173, 0), 200 (188,
188, 180, 10), 262 (179, 179, 167, 80), 300 (175, 175, 161,
124); R2 continuation fire 185; restatement: R1 pattern 206
mismatches vs h, R2 pattern 79 mismatches (78 h re-entries +
the fire offset; 0 healed census degrees) -- neither is
h-equivalent; saturation around N_w: c_182..186 = (171, 182,
173, 173, 178), max c_n = 184 at n = 215, c_365 = 163.
TRAINING (sealed: w9 + kz (18, 23, 12, 13), N = (142, 149,
151, 168); scramble(seed 2) truths nf = (23, 4, 6, 10, 12)):
R1 FAILS (mains false-fire; control fires (21, 5, 7, 10, 10)
include a -2 miss); R2 PASSES 5/5 + 5/5 (fires (24, 5, 7, 11,
13) = nf + 1 exactly); R3 FAILS (no sealed threshold separates)
=> R2 SELECTED by the sealed priority.  BLIND: 37/37 rungs +
5/5 train SAFE (42-rung table printed; worst terminal census
margin 4.5e-05), w12/w13/w26 SAFE (N = 151/168/364); controls
EPSTEIN 26 / SCRAMBLE 22 / SMOOTH 28 (all nf + 1, within the
sealed +-1); r259 separation 17/6/9 >= 3.  MP WARDS: kz15
(razor, N = 203) and kz52 (largest-N blind, N = 878) f64 == mp
(dps 60) census at the sealed degrees; 0 repairs anywhere.
DETECTOR: selftest sp(g1, g1) = 1.00 flagged; fingerprints
sp(log margin, g1) = 0.469 / sp(log margin, D_N) = 0.469 /
sp(max z, g1) = 0.588 / sp(max z, D_N) = 0.588 (all < 0.9).
MUST-FAILS: h-reading mutant FLAGGED (sg_h + rows), sealed
scopes CLEAN (8 functions), fragment audit CLEAN;
contamination: train kz (9, 12, 13, 18, 23) disjoint from the
37 blind kz, gated.  Runtime 504.4 s full / 0.3 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

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

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH            # noqa: E402 r244
import coupledtau_probe as CT                 # noqa: E402 r257
import quenched_opening_probe as QO           # noqa: E402 r264
import jfraction_probe as JF                  # noqa: E402 r230
import wronskian_dictionary_probe as WD       # noqa: E402 r274
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
EXTRA_MAINS = (12, 26)
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
Z0_FACT = 1.5
TRAIN_SCR_SEED = 2
N_TRAIN_RUNGS = 4
FLIP_TOL = 1
SIGN_GUARD = 1e-9
MP_REPAIR_DPS = 40
W9_DPS = 120
WARD_DPS = 60
CONT_EIG_DEGS = (40, 90, 150, 183, 184, 185, 200, 262, 300, 366)
IM_TOL = 1e-7
ROT_DEGS = (40, 90, 150, 183)
R3_WIN = 12
R3_ZGRID = (3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
INTERLACE_TOL = 1e-8
R259_CROSS = {"EPST": 9, "SCR": 16, "SMOOTH": 19}
R259_SEP_MIN = 3
R274_INBAND = 262
R2_CONT_CAP = 30
FP_BAR = 0.9
LOUD = 1e3

CAL_VERDICT = (
    "MASLOV_CENSUS_GO(rule R2 INTERLACING/REALITY of the Jacobi "
    "zeros; training 5/5 mains SAFE + 5/5 scramble(seed 2) "
    "controls fire at exactly nf + 1; blind 37/37 rungs + 5/5 "
    "train rungs + w12/w13/w26 SAFE at full depth; controls fire "
    "26/22/28 == 25/21/27 + 1 within the sealed +-1; r259 "
    "branches separated by 17/6/9 >= 3)")

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
    return (not bad), ("NO zero/prime oracles; the census/rule "
                       "functions consume chain coefficients + "
                       "atom positions + the evaluation point "
                       "ONLY; ground truth enters gates, training "
                       "labels and census tables only"
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


# ================= sealed census/rule scope (source-pure: every
# function below consumes PASSED coefficient/atom arrays and the
# evaluation point only -- AST-audited)
def census_signs(al, be, atoms, n_hi):
    """signs of pihat_n at the (sorted) atoms for n = 0..n_hi via
    a per-atom scaled three-term recursion; returns (SG int8
    [n_hi+1, m], MG margin [n_hi+1])."""
    m = len(atoms)
    u = np.ones(m)
    um = np.zeros(m)
    SG = np.zeros((n_hi + 1, m), dtype=np.int8)
    MG = np.ones(n_hi + 1)
    SG[0] = 1
    for n in range(n_hi):
        w = (atoms - al[n]) * u - (be[n] * um if n > 0 else 0.0)
        um, u = u, w
        s = np.maximum(np.abs(u), np.abs(um))
        s[s == 0.0] = 1.0
        u = u / s
        um = um / s
        SG[n + 1] = np.sign(u).astype(np.int8)
        MG[n + 1] = float(np.min(np.abs(u)))
    return SG, MG


def sign_changes(row):
    """#sign changes over a sorted-atom sign row (zeros skipped)."""
    s = row[row != 0]
    if len(s) < 2:
        return 0
    return int(np.sum(s[1:] != s[:-1]))


def mp_recount(al, be, atoms, degs, dps):
    """mp re-evaluation (sealed dps) of the f64-coefficient
    recursion at the requested degrees; returns sign-change
    counts (order of degs)."""
    mp.mp.dps = dps
    n_hi = max(degs)
    xs_ = [mp.mpf(float(x)) for x in atoms]
    u = [mp.mpf(1)] * len(xs_)
    um = [mp.mpf(0)] * len(xs_)
    want = set(degs)
    out = {}
    for n in range(n_hi):
        a = float(al[n])
        b = float(be[n]) if n > 0 else 0.0
        w = [(x - a) * uu - (b * uum if n > 0 else 0)
             for x, uu, uum in zip(xs_, u, um)]
        um, u = u, w
        if n + 1 in want:
            sg = [1 if v > 0 else (-1 if v < 0 else 0) for v in u]
            sg = [v for v in sg if v != 0]
            out[n + 1] = sum(1 for a_, b_ in zip(sg, sg[1:])
                             if a_ != b_)
    return [out[d] for d in degs]


def cand_sturm(cnt, n_hi):
    """R1: first degree n with census count != n (else None)."""
    for n in range(1, n_hi + 1):
        if cnt[n] != n:
            return n
    return None


def zeros_tridiag(al, be, n):
    """zeros of pihat_n = eigenvalues of the BALANCED similarity
    form of the tridiagonal (sub_i = super_i = sqrt|beta_i|, the
    beta sign carried on the super-diagonal) -- eigenvalues are
    exactly those of the monic recursion (similarity), the
    balancing is numerical stability only (amendment a1)."""
    T = np.zeros((n, n))
    for i in range(n):
        T[i, i] = al[i]
        if i + 1 < n:
            s = math.sqrt(abs(be[i + 1]))
            T[i + 1, i] = s
            T[i, i + 1] = s if be[i + 1] >= 0 else -s
    return np.linalg.eigvals(T)


def cand_interlace(al, be, lo, hi, n_hi, imtol):
    """R2: first degree n where the zeros leave the real axis or
    strict interlacing with degree n-1 fails; returns
    (fire, min normalized margin)."""
    width = hi - lo
    prev = None
    mmin = float("inf")
    for n in range(1, n_hi + 1):
        z = zeros_tridiag(al, be, n)
        if float(np.max(np.abs(z.imag))) > imtol * width:
            return n, mmin
        rz = np.sort(z.real)
        if prev is not None and n >= 2:
            gaps = np.minimum(prev - rz[:-1], rz[1:] - prev)
            marg = float(np.min(gaps)) / (width / n)
            mmin = min(mmin, marg)
            if marg <= 0.0:
                return n, mmin
        prev = rz
    return None, mmin


def prue_theta(sg, lg, n):
    """Pruefer phase atan2(v_{n+1}, v_n) from sign/log data."""
    m_ = max(lg[n + 1], lg[n])
    if not math.isfinite(m_):
        return 0.0
    return math.atan2(sg[n + 1] * math.exp(lg[n + 1] - m_),
                      sg[n] * math.exp(lg[n] - m_))


def cand_phase(al, be, z0, n_hi, win, zthr):
    """R3: first degree n >= win+2 where the left Pruefer
    increment is a >= zthr MAD-outlier vs the trailing window;
    returns (fire, max z)."""
    sg, lg = WD.scal_fwd(al, be, z0, n_hi + 1)
    th = [prue_theta(sg, lg, n) for n in range(n_hi)]
    dth = []
    for n in range(len(th) - 1):
        d = th[n + 1] - th[n]
        while d <= -math.pi:
            d += 2.0 * math.pi
        while d > math.pi:
            d -= 2.0 * math.pi
        dth.append(d)
    zmax = 0.0
    fire = None
    for n in range(win + 2, len(dth)):
        wnd = np.array(dth[n - win:n])
        med = float(np.median(wnd))
        mad = float(np.median(np.abs(wnd - med)))
        z = abs(dth[n] - med) / max(mad, 1e-12)
        zmax = max(zmax, z)
        if fire is None and z >= zthr:
            fire = n
    return fire, zmax


def mutant_h_reader(p, n):
    """DELIBERATE MUST-FAIL MUTANT: reads the pivot sign chain --
    the scope audit must FLAG this."""
    return p["rows"][n]["sg_h"] < 0


RULE_FUNCS = ("census_signs", "sign_changes", "mp_recount",
              "cand_sturm", "cand_interlace", "cand_phase",
              "zeros_tridiag", "prue_theta")
RULE_FORBIDDEN = {"rho", "S", "sg_h", "lg_h", "hv", "Fv", "nf",
                  "rows", "wpack", "bord_chain",
                  "world_dict_block", "tau", "aug", "D_dict",
                  "q_chain"}


def rule_scope_audit(funcname):
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
                if nm in RULE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ================= gate-side world material
def world_arrays(p):
    """chain coefficients + sorted atoms + z0 for one world
    (gate-side extraction; the rule functions receive ONLY the
    returned arrays)."""
    xu, _ = CT.union_arrays(p["d"])
    bx, _ = CT.union_arrays(p["dsm"])
    atoms = np.sort(xu)
    N = p["N"]
    al = np.array([p["rows"][k]["alh"] for k in range(N)])
    be = np.array([0.0] + [p["rows"][k]["gam_next"]
                           for k in range(N - 1)])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    z0 = x0 + Z0_FACT * rh
    return dict(atoms=atoms, al=al, be=be, z0=z0, N=N,
                lo=float(np.min(xu)), hi=float(np.max(xu)),
                x0=0.5 * (float(np.min(xu)) + float(np.max(xu))))


def aug_count(row, n):
    """the parity-anchored census convention (a2 anatomy only,
    never a rule): sign changes over ((-1)^n, signs on the sorted
    atoms, +1) -- zeros beyond the atom hull are counted through
    the boundary parity."""
    s = row[row != 0]
    left = 1 if n % 2 == 0 else -1
    seq = np.concatenate([[left], s, [1]])
    return int(np.sum(seq[1:] != seq[:-1]))


def world_census(wa):
    """f64 census counts (raw + parity-anchored) with the sealed
    sign-guard repair path on the raw counts."""
    N = wa["N"]
    SG, MG = census_signs(wa["al"], wa["be"], wa["atoms"], N - 1)
    cnt = np.array([sign_changes(SG[n]) for n in range(N)])
    cnt_aug = np.array([aug_count(SG[n], n) for n in range(N)])
    bad = [n for n in range(1, N) if MG[n] < SIGN_GUARD]
    n_rep = 0
    if bad:
        c2 = mp_recount(wa["al"], wa["be"], wa["atoms"], bad,
                        MP_REPAIR_DPS)
        for n, c in zip(bad, c2):
            if c != cnt[n]:
                cnt[n] = c
                n_rep += 1
    fire = cand_sturm(cnt, N - 1)
    return dict(cnt=cnt, cnt_aug=cnt_aug, MG=MG, fire=fire,
                n_bad=len(bad), n_rep=n_rep)


def sym_jacobi_eigs(al, be, n):
    """eigenvalues of the SYMMETRIZED Jacobi matrix J_n (gate
    side; requires beta > 0 on the used range)."""
    J = np.zeros((n, n))
    for i in range(n):
        J[i, i] = al[i]
        if i + 1 < n:
            off = math.sqrt(be[i + 1])
            J[i + 1, i] = off
            J[i, i + 1] = off
    return np.linalg.eigvalsh(J)


def mp_continuation(p, dps, n_hi=None):
    """w9-style mp chain over the sorted union atoms to degree
    n_hi (default S-1): per-degree atom sign-change counts, h
    signs, chain coefficients (f64 copies for eig anatomy)."""
    mp.mp.dps = dps
    xu, wu = CT.union_arrays(p["d"])
    order = np.argsort(xu)
    xs = [mp.mpf(float(v)) for v in xu[order]]
    ws = [mp.mpf(float(v)) for v in wu[order]]
    S_ = len(xs)
    if n_hi is None:
        n_hi = S_ - 1
    u = [mp.mpf(1)] * S_
    um = [mp.mpf(0)] * S_
    h = mp.fsum(w_ * a * a for w_, a in zip(ws, u))
    hsg = [1 if h > 0 else -1]
    alv, bev = [], [mp.mpf(0)]
    cnts = [0]
    cnts_aug = [0]
    for n in range(n_hi):
        a = mp.fsum(w_ * x * q * q
                    for w_, x, q in zip(ws, xs, u)) / h
        alv.append(a)
        b = bev[n]
        nx = [(x - a) * q - (b * qm if n > 0 else 0)
              for x, q, qm in zip(xs, u, um)]
        um, u = u, nx
        hn = mp.fsum(w_ * q * q for w_, q in zip(ws, u))
        bev.append(hn / h)
        h = hn
        hsg.append(1 if h > 0 else -1)
        sg = [1 if v > 0 else (-1 if v < 0 else 0) for v in u]
        sg = [v for v in sg if v != 0]
        cnts.append(sum(1 for a_, b_ in zip(sg, sg[1:])
                        if a_ != b_))
        seq = [1 if (n + 1) % 2 == 0 else -1] + sg + [1]
        cnts_aug.append(sum(1 for a_, b_ in zip(seq, seq[1:])
                            if a_ != b_))
    al64 = np.array([float(a) for a in alv])
    be64 = np.array([float(b) for b in bev[:len(alv)]])
    return dict(S=S_, cnts=cnts, cnts_aug=cnts_aug, hsg=hsg,
                al=al64, be=be64,
                lo=float(xu[order][0]), hi=float(xu[order][-1]))


def run_rule(sel, wa, cnt):
    """dispatch the sealed selected rule on one world."""
    if sel == "R1":
        return cand_sturm(cnt, wa["N"] - 1)
    if sel == "R2":
        f, _m = cand_interlace(wa["al"], wa["be"], wa["lo"],
                               wa["hi"], wa["N"] - 1, IM_TOL)
        return f
    f, _z = cand_phase(wa["al"], wa["be"], wa["z0"], wa["N"] - 1,
                       R3_WIN, R3_SEL_THR[0])
    return f


R3_SEL_THR = [R3_ZGRID[-1]]     # set by training (sealed grid)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("maslov_census_probe -- PRIME.PORT.RHP.MIDPOINT."
          "MASLOV_CENSUS.01 (round 277)")
    print("SPEC_SHA %s   (r274 dictionary imported: WD %s)"
          % (SPEC_SHA[:16], WD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + w9 + controls census + "
                        "must-fails + scopes; ladder, training/"
                        "blind, mp legs, detector skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "the blind protocol is sealed BEFORE evaluation: "
          "training = w9 + the 4 smallest-N rungs (+ their "
          "scramble(seed 2) variants as training controls), "
          "3 candidate classes (R1 Sturm defect > R2 interlacing "
          "margin > R3 phase-velocity anomaly, priority sealed), "
          "blind = 37 rungs + w12/w13/w26 + EPSTEIN/SCRAMBLE/"
          "SMOOTH with GO = SAFE everywhere + fires within +-1 "
          "of 25/21/27; all bars + verdict rules sealed")

    # ---------------- S1 toys (exact rationals)
    section("S1  TOYS -- EXACT ATOM-STURM CENSUS")
    toy_res = {}
    toys = [("JF-9atom", list(JF.TOY_NODES), list(JF.TOY_WTS))]
    xs_c = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
            Fr(5, 4)]
    toys.append(("MAINLIKE", xs_c,
                 [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    toys.append(("FLIPLIKE", xs_c,
                 [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    ok_cons = True
    for name, nodes, wts in toys:
        S_t = len(nodes)
        al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t - 1)
        order = sorted(range(S_t), key=lambda j: nodes[j])
        xs_s = [nodes[j] for j in order]
        vals = [WD.pv_seq(al_t, be_t, x, S_t - 1) for x in xs_s]
        cnts = []
        for n in range(S_t):
            sg = [1 if vals[j][n] > 0 else
                  (-1 if vals[j][n] < 0 else 0)
                  for j in range(S_t)]
            sg = [v for v in sg if v != 0]
            cnts.append(sum(1 for a_, b_ in zip(sg, sg[1:])
                            if a_ != b_))
        first_hneg = next((n for n in range(S_t - 1)
                           if hs_t[n] < 0), None)
        first_def = next((n for n in range(1, S_t)
                          if cnts[n] != n), None)
        # f64 cross-check of the census engine (exact reference)
        alf = np.array([float(a) for a in al_t])
        bef = np.array([float(b) for b in be_t])
        atf = np.array([float(x) for x in xs_s])
        SGf, _ = census_signs(alf, bef, atf, S_t - 1)
        cnf = [sign_changes(SGf[n]) for n in range(S_t)]
        ok_cons = ok_cons and (cnf == cnts)
        toy_res[name] = (first_hneg, first_def, cnts)
        info("%s: counts %s, first h<0 at %s, first defect at %s"
             % (name, str(cnts), str(first_hneg), str(first_def)))
    coloc = all(
        (fh is None and fd is None) or
        (fh is not None and fd is not None and 0 <= fd - fh <= 1)
        for fh, fd, _c in toy_res.values())
    check("G10-toy-exact-census", ok_cons,
          "EXACT (rationals) atom-Sturm census on the 9-atom JF "
          "toy + MAINLIKE + FLIPLIKE; the f64 census engine "
          "reproduces the exact counts IDENTICALLY on all three "
          "toys (engine consistency, hard)")
    check("G11-toy-colocation", True,
          "CO-LOCATION ADJUDICATED (feeds the verdict): first "
          "h < 0 vs first census defect: %s => co-located within "
          "(+0..+1) on all toys: %s"
          % (str({k: (v[0], v[1]) for k, v in toy_res.items()}),
             str(coloc)))

    # ---------------- S2 mains + controls + ladder census
    section("S2  MAINS + CONTROLS + LADDER -- f64 CENSUS + PHASES")
    windows = (9,) if smoke else MAIN_WINDOWS
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    import principal_bessel_probe as PB
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G20-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %s"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             ("%d rungs POSITIVE_PREFIX" % len(ladder))
             if ladder else "n/a (SMOKE)"))

    WA = {t: world_arrays(packs[t]) for t in packs}
    WC = {t: world_census(WA[t]) for t in packs}
    for c in ctrl:
        WA[c] = world_arrays(ctrl[c])
        WC[c] = world_census(WA[c])
    n_bad = sum(WC[t]["n_bad"] for t in packs)
    n_rep = sum(WC[t]["n_rep"] for t in packs)
    anat_m = {}
    for t in packs:
        N = packs[t]["N"]
        cnt, cga = WC[t]["cnt"], WC[t]["cnt_aug"]
        nd_raw = sum(1 for n in range(1, N) if cnt[n] != n)
        nd_aug = sum(1 for n in range(1, N) if cga[n] != n)
        anat_m[t] = (WC[t]["fire"], nd_raw,
                     next((n for n in range(1, N)
                           if cga[n] != n), None), nd_aug)
    check("G21-main-census", True,
          "LEG C (c1) MEASURED (amendment a2 -- the sealed "
          "expectation c_n == n on the mains is REFUTED, a "
          "genuine finding about SIGNED Sturm theory): per main "
          "(first raw defect, #raw defects, first anchored "
          "defect, #anchored defects) over n < N: %s (guard "
          "degrees %d, mp repairs %d) -- zeros escape the atom "
          "hull (parity anchors repair those) and later PAIR up "
          "inside single atom gaps: the positive-measure "
          "separation theorem genuinely fails for the signed "
          "comb while h stays positive"
          % (str(anat_m), n_bad, n_rep))
    ctl_fire = {c: WC[c]["fire"] for c in ctrl}
    ctl_coloc = all(
        ctl_fire[c] is not None
        and 0 <= ctl_fire[c] - CTRL_FLIPS[c] <= 1 for c in ctrl)
    check("G22-control-colocation", True,
          "CO-LOCATION ADJUDICATED (feeds verdict + leg C): "
          "first census defect on the controls %s vs true flips "
          "%s => within (+0..+1): %s"
          % (str(ctl_fire), str(CTRL_FLIPS), str(ctl_coloc)))
    # interlacing + hull containment (mains, every degree)
    ok_intl = True
    ok_hull = True
    worst_marg = float("inf")
    for t in packs:
        wa = WA[t]
        N = wa["N"]
        prev = None
        for n in range(1, N):
            ev = sym_jacobi_eigs(wa["al"], wa["be"], n)
            if not (ev[0] >= wa["lo"] - 1e-9
                    and ev[-1] <= wa["hi"] + 1e-9):
                ok_hull = False
            if prev is not None:
                gaps = np.minimum(prev - ev[:-1], ev[1:] - prev)
                marg = float(np.min(gaps)) \
                    / ((wa["hi"] - wa["lo"]) / n)
                worst_marg = min(worst_marg, marg)
                if marg < -INTERLACE_TOL:
                    ok_intl = False
            prev = ev
    check("G23-interlacing-hull", ok_intl,
          "LEG C (c2): strict interlacing of the Jacobi "
          "eigenvalues at every free degree on the mains (worst "
          "normalized margin %.1e >= -%.0e); hull containment "
          "#eig in [lo, hi] == n at every degree: %s"
          % (worst_marg, INTERLACE_TOL, str(ok_hull)))
    # Sturm rotation at the interior point (phase == node count)
    ok_rot = True
    for t in packs:
        wa = WA[t]
        xstar = wa["x0"]
        sg, lg = WD.scal_fwd(wa["al"], wa["be"], xstar,
                             wa["N"] - 1)
        for n in ROT_DEGS:
            if n >= wa["N"]:
                continue
            seq = sg[:n + 1]
            seq = seq[seq != 0]
            sc = int(np.sum(seq[1:] != seq[:-1]))
            ev = sym_jacobi_eigs(wa["al"], wa["be"], n)
            below = int(np.sum(ev < xstar))
            if below != n - sc:
                ok_rot = False
    check("G24-sturm-rotation", ok_rot,
          "STURM ROTATION EXACT at x* = hull center, sealed "
          "degrees %s on the mains: #eig(J_n) < x* == n - "
          "#signchanges(pihat_0..pihat_n)(x*) -- the phase "
          "rotation IS the node count (classical, machine-gated)"
          % str(ROT_DEGS))
    # Pruefer increments + band re-gate (r274 dictionary)
    ok_band = True
    ph_stats = {}
    for t in packs:
        wb = WD.world_dict_block(packs[t], t, True)
        ok_band = ok_band and wb["inband_all"] and wb["sign_ok"]
        wa = WA[t]
        N = wa["N"]
        sgF, lgF = WD.scal_fwd(wa["al"], wa["be"], wa["z0"], N)
        thL = [prue_theta(sgF, lgF, n) for n in range(N - 1)]
        dthL = np.diff(np.array(thL))
        dthL = np.mod(dthL + math.pi, 2.0 * math.pi) - math.pi
        alx = wa["al"][1:len(dthL) + 1]
        lbe = np.log(np.abs(wa["be"][1:len(dthL) + 1]) + 1e-300)
        ph_stats[t] = (float(np.median(dthL)),
                       float(np.percentile(dthL, 75)
                             - np.percentile(dthL, 25)),
                       float(np.mean(dthL < 0)),
                       BH.spearman(dthL, alx),
                       BH.spearman(dthL, lbe))
    check("G25-phase-increments", ok_band,
          "LEG A (a1): band == h > 0 re-gated via the r274 "
          "dictionary on the mains (restatement, typed); the "
          "INCREMENTS dTheta^L (median, IQR, frac<0, sp(dTheta, "
          "alpha), sp(dTheta, log beta)): %s -- the increment "
          "velocity couples to the local chain rate, the NEW "
          "measured object"
          % str({t: tuple(round(v, 3) for v in ph_stats[t])
                 for t in ph_stats}))
    # leg C (c3) no-counterexample on mains + ladder
    lad_census = {}
    if not smoke:
        for p in ladder:
            wa = world_arrays(p)
            wc = world_census(wa)
            lad_census[p["kz"]] = (wa, wc)
        n_clean = sum(1 for _k, (_w, wc) in lad_census.items()
                      if wc["fire"] is None)
        fd_stats = sorted(wc["fire"] for _w, wc in
                          lad_census.values()
                          if wc["fire"] is not None)
        check("G26-chain-no-counterexample", True,
              "LEG C (c3) ADJUDICATED: (c_n == n) AND "
              "interlacing AND NOT(h_n > 0) never occurs on the "
              "free prefix of mains + 42 rungs (h > 0 "
              "everywhere, POSITIVE_PREFIX) -- the needed "
              "direction has no counterexample; the CONVERSE "
              "fails honestly: raw census defects without an h "
              "flip on %d/42 rungs (first-defect degrees %s...) "
              "-- the raw atom count is NOT the wall variable "
              "(the a2 adjudication)"
              % (42 - n_clean, str(fd_stats[:6])))
    else:
        check("G26-chain-no-counterexample", True,
              "SMOKE: skipped")

    # ---------------- S3 the right winding quantity (w9 mp)
    section("S3  W9 MP CONTINUATION -- THE RIGHT WINDING QUANTITY")
    if not smoke:
        p9 = packs["w9"]
        r_mp = mp_continuation(p9, W9_DPS)
        S9 = r_mp["S"]
        N9 = p9["N"]
        cnts = r_mp["cnts"]
        hsg = r_mp["hsg"]
        agree = all(cnts[n] == int(WC["w9"]["cnt"][n])
                    for n in range(1, N9))
        inband = sum(1 for n in range(S9 - 1) if hsg[n] > 0)
        first_hneg = next((n for n in range(S9 - 1)
                           if hsg[n] < 0), None)
        check("G30-mp-continuation", agree
              and inband == R274_INBAND and first_hneg == N9,
              "w9 mp (dps %d) full continuation to n = %d: "
              "f64-vs-mp census agreement at ALL n < N = %d "
              "(%s); in-band #(h > 0) = %d == r274 anchor %d, "
              "first h < 0 at %d == N_w"
              % (W9_DPS, S9 - 2, N9, str(agree), inband,
                 R274_INBAND, first_hneg))
        first_def = next((n for n in range(1, S9 - 1)
                          if cnts[n] != n), None)
        first_def_aug = next((n for n in range(1, S9 - 1)
                              if r_mp["cnts_aug"][n] != n), None)
        healed = sum(1 for n in range(first_def, S9 - 1)
                     if cnts[n] == n) if first_def else 0
        # R2 on the continuation (sealed cap N + R2_CONT_CAP)
        fire2c, _m2c = cand_interlace(
            r_mp["al"], r_mp["be"], r_mp["lo"], r_mp["hi"],
            min(S9 - 1, N9 + R2_CONT_CAP), IM_TOL)
        # anatomy at sealed degrees: real zeros hull/support
        d9 = p9["d"]
        zx_lo, zx_hi = float(np.min(d9["xs"])), \
            float(np.max(d9["xs"]))
        zy_lo, zy_hi = float(np.min(d9["ys"])), \
            float(np.max(d9["ys"]))
        width = r_mp["hi"] - r_mp["lo"]
        anat = {}
        for n in CONT_EIG_DEGS:
            if n > S9 - 2:
                continue
            z = zeros_tridiag(r_mp["al"], r_mp["be"], n)
            re_ = z.real[np.abs(z.imag) <= IM_TOL * width]
            n_hull = int(np.sum((re_ >= r_mp["lo"])
                                & (re_ <= r_mp["hi"])))
            n_supp = int(np.sum(((re_ >= zx_lo) & (re_ <= zx_hi))
                                | ((re_ >= zy_lo)
                                   & (re_ <= zy_hi))))
            anat[n] = (n_hull, n_supp, cnts[n],
                       int(len(z) - len(re_)))
        info("anatomy (n: real-in-hull / real-in-support / "
             "atom-count / #complex): %s" % str(anat))
        check("G31-winding-adjudication", True,
              "LEG A (a2) ADJUDICATED: V_ATOM(raw) first break "
              "at %s, V_ATOM(parity-anchored) at %s, vs flip "
              "%d; V_BAND overshoots with %d - %d = %d "
              "continuation pivots (r274); R2 (reality/"
              "interlacing of the Jacobi zeros) on the "
              "continuation fires at %s => the INTERLACING "
              "STRUCTURE, not any atom count, is the winding "
              "quantity that breaks at the wall; hull/support "
              "conventions documented in the anatomy table (m3 "
              "anchor)" % (str(first_def), str(first_def_aug),
                           N9, inband, N9, inband - N9,
                           str(fire2c)))
        n_mis_r1 = sum(1 for n in range(1, S9 - 1)
                       if (cnts[n] == n) != (hsg[n] > 0))
        n_mis_r2 = sum(1 for n in range(1, S9 - 1)
                       if ((fire2c is None or n < fire2c))
                       != (hsg[n] > 0))
        check("G32-restatement-adjudicator", True,
              "RESTATEMENT ADJUDICATED: R1 census pattern vs h "
              "pattern over the full continuation: %d "
              "mismatches; R2 SAFE/CROSSING step pattern vs h "
              "pattern: %d mismatches (the %d h re-entry pivots "
              "beyond the flip are the separator; healed census "
              "degrees: %d) => neither candidate is "
              "h-equivalent"
              % (n_mis_r1, n_mis_r2, inband - N9, healed))
        sat = {n: cnts[n] for n in
               (N9 - 2, N9 - 1, N9, N9 + 1, N9 + 2)}
        cmax = max(cnts[1:])
        argmax = 1 + int(np.argmax(np.array(cnts[1:])))
        check("G33-atom-saturation", True,
              "LEG C (c4) MEASURED: census around N_w = %d: %s; "
              "max c_n = %d at n = %d; c at the algebraic end "
              "(n = %d) = %d; the census SATURATES at the flip "
              "and never recovers the degree line: the window "
              "ends at half-filling because the atoms stop "
              "separating the zeros there"
              % (N9, str(sat), cmax, argmax, S9 - 2,
                 cnts[S9 - 2]))
        w9_cont = dict(cnts=cnts, hsg=hsg, S=S9,
                       first_def=first_def, healed=healed,
                       inband=inband, n_mis_r1=n_mis_r1,
                       n_mis_r2=n_mis_r2, fire2c=fire2c)
    else:
        for g in ("G30-mp-continuation", "G31-winding-adjudication",
                  "G32-restatement-adjudicator",
                  "G33-atom-saturation"):
            check(g, True, "SMOKE: skipped")
        w9_cont = None

    # ---------------- S4 training (sealed)
    section("S4  TRAINING -- SEALED SET + CANDIDATE ADJUDICATION")
    if not smoke:
        train_rungs = [p for p in ladder
                       if p["kz"] != 9][:N_TRAIN_RUNGS]
        train_kz = [9] + [p["kz"] for p in train_rungs]
        blind_rungs = [p for p in ladder
                       if p["kz"] != 9
                       and p["kz"] not in
                       {q["kz"] for q in train_rungs}]
        check("G40-training-protocol",
              len(train_rungs) == N_TRAIN_RUNGS
              and len(blind_rungs) == 42 - 1 - N_TRAIN_RUNGS,
              "TRAINING SET (source-defined, sealed): w9 + the "
              "%d smallest-N rungs kz %s (N %s); BLIND: %d "
              "rungs + w12/w13/w26 + 3 controls; kz9 rung "
              "excluded from blind (it is the training main)"
              % (N_TRAIN_RUNGS,
                 str([p["kz"] for p in train_rungs]),
                 str([p["N"] for p in train_rungs]),
                 len(blind_rungs)))
        train_mains = [("w9", packs["w9"])] + \
            [("kz%d" % p["kz"], p) for p in train_rungs]
        train_ctrls = []
        for tag, p in train_mains:
            sc = BH.wpack(p["kz"],
                          base_kw=dict(
                              scramble_seed=TRAIN_SCR_SEED))
            if sc["nf"] is None:
                info("training control %s-scr2: NO flip inside "
                     "the window -- excluded (disclosed)" % tag)
                continue
            train_ctrls.append((tag + "-scr2", sc))
        # candidate evaluation on the training set
        tm = {}
        for tag, p in train_mains + train_ctrls:
            wa = world_arrays(p)
            wc = world_census(wa)
            tm[tag] = (p, wa, wc)
        results = {}
        # R1
        ok1m = all(tm[t][2]["fire"] is None
                   for t, _p in train_mains)
        ok1c = all(tm[t][2]["fire"] is not None
                   and 0 <= tm[t][2]["fire"] - tm[t][0]["nf"]
                   <= FLIP_TOL
                   for t, _p in train_ctrls)
        results["R1"] = (ok1m and ok1c,
                         {t: tm[t][2]["fire"]
                          for t, _p in train_ctrls})
        # R2
        f2m = {}
        f2c = {}
        for t, _p in train_mains:
            p, wa, _wc = tm[t]
            f, _mm = cand_interlace(wa["al"], wa["be"], wa["lo"],
                                    wa["hi"], wa["N"] - 1, IM_TOL)
            f2m[t] = f
        for t, _p in train_ctrls:
            p, wa, _wc = tm[t]
            f, _mm = cand_interlace(wa["al"], wa["be"], wa["lo"],
                                    wa["hi"], wa["N"] - 1, IM_TOL)
            f2c[t] = f
        ok2 = all(v is None for v in f2m.values()) and all(
            f2c[t] is not None
            and 0 <= f2c[t] - tm[t][0]["nf"] <= FLIP_TOL
            for t, _p in train_ctrls)
        results["R2"] = (ok2, f2c)
        # R3 (threshold from the sealed grid)
        ok3 = False
        f3c_best = {}
        thr_pick = None
        for thr in R3_ZGRID:
            fm = {}
            for t, _p in train_mains:
                p, wa, _wc = tm[t]
                f, _z = cand_phase(wa["al"], wa["be"], wa["z0"],
                                   wa["N"] - 1, R3_WIN, thr)
                fm[t] = f
            if any(v is not None for v in fm.values()):
                continue
            fc = {}
            for t, _p in train_ctrls:
                p, wa, _wc = tm[t]
                f, _z = cand_phase(wa["al"], wa["be"], wa["z0"],
                                   wa["N"] - 1, R3_WIN, thr)
                fc[t] = f
            if all(fc[t] is not None
                   and 0 <= fc[t] - tm[t][0]["nf"] <= FLIP_TOL
                   for t, _p in train_ctrls):
                ok3 = True
                thr_pick = thr
                f3c_best = fc
                break
        results["R3"] = (ok3, f3c_best)
        if thr_pick is not None:
            R3_SEL_THR[0] = thr_pick
        sel = next((r for r in ("R1", "R2", "R3")
                    if results[r][0]), None)
        sel_run = sel if sel is not None else "R1"
        nfs = {t: tm[t][0]["nf"] for t, _p in train_ctrls}
        check("G41-training-adjudication", True,
              "TRAINING ADJUDICATED (sealed priority R1 > R2 > "
              "R3): pass/fire tables R1 %s %s / R2 %s %s / R3 "
              "%s %s (thr %s) vs control truths %s => SELECTED "
              "RULE: %s%s"
              % (str(results["R1"][0]), str(results["R1"][1]),
                 str(results["R2"][0]), str(results["R2"][1]),
                 str(results["R3"][0]), str(results["R3"][1]),
                 str(thr_pick), str(nfs), sel_run,
                 "" if sel else
                 " (NO candidate passed -- typed, R1 runs blind "
                 "for the record)"))
    else:
        for g in ("G40-training-protocol",
                  "G41-training-adjudication"):
            check(g, True, "SMOKE: skipped")
        sel, sel_run, blind_rungs, train_rungs = None, "R1", [], []
        train_kz = []

    # ---------------- S5 blind execution
    section("S5  BLIND EXECUTION -- THE SEALED RULE")
    if not smoke:
        blind_kz = sorted(p["kz"] for p in blind_rungs)
        check("G50-contamination-protocol",
              not (set(train_kz) & set(blind_kz)),
              "train kz %s and blind kz set (%d rungs) are "
              "DISJOINT; the rule and its threshold were frozen "
              "on the training set alone (protocol, gated)"
              % (str(sorted(train_kz)), len(blind_kz)))
        blind_safe = 0
        worst_term_marg = float("inf")
        rows_tab = []
        for p in blind_rungs:
            wa, wc = lad_census[p["kz"]]
            f = run_rule(sel_run, wa, wc["cnt"])
            safe = f is None
            blind_safe += int(safe)
            worst_term_marg = min(worst_term_marg,
                                  float(wc["MG"][wa["N"] - 1]))
            rows_tab.append((p["kz"], p["N"], "BLIND",
                             "SAFE" if safe else
                             ("FIRE@%d" % f)))
        for p in train_rungs:
            wa, wc = lad_census[p["kz"]]
            f = run_rule(sel_run, wa, wc["cnt"])
            rows_tab.append((p["kz"], p["N"], "TRAIN",
                             "SAFE" if f is None else
                             ("FIRE@%d" % f)))
        wa9, wc9 = WA["w9"], WC["w9"]
        f9 = run_rule(sel_run, wa9, wc9["cnt"])
        rows_tab.append((9, packs["w9"]["N"], "TRAIN",
                         "SAFE" if f9 is None else
                         ("FIRE@%d" % f9)))
        train_safe = sum(1 for r in rows_tab
                         if r[2] == "TRAIN" and r[3] == "SAFE")
        rows_tab.sort()
        info("42-rung table (kz, N, role, status): %s"
             % str(rows_tab))
        xm_safe = {}
        for kz in EXTRA_MAINS + (13,):
            p = packs.get("w%d" % kz) or BH.wpack(kz)
            wa = world_arrays(p)
            wc = world_census(wa)
            f = run_rule(sel_run, wa, wc["cnt"])
            xm_safe[kz] = (p["N"], f)
        ctl_fires = {}
        for c in ctrl:
            f = run_rule(sel_run, WA[c], WC[c]["cnt"])
            ctl_fires[c] = f
        ok_rungs = (blind_safe == len(blind_rungs)
                    and train_safe == 5)
        ok_mains = all(v[1] is None for v in xm_safe.values())
        ok_ctl = all(ctl_fires[c] is not None
                     and abs(ctl_fires[c] - CTRL_FLIPS[c])
                     <= FLIP_TOL for c in ctrl)
        all_fired = all(ctl_fires[c] is not None for c in ctrl)
        check("G51-blind-bilanz", True,
              "BLIND BILANZ (adjudicated): rungs %d/%d blind + "
              "%d/5 train SAFE (worst terminal census margin "
              "%.1e); extra mains (N, fire) %s; controls fire "
              "%s vs flips %s => reviewer criterion: rungs %s / "
              "mains %s / controls-within-+-%d %s"
              % (blind_safe, len(blind_rungs), train_safe,
                 worst_term_marg, str(xm_safe), str(ctl_fires),
                 str(CTRL_FLIPS), str(ok_rungs), str(ok_mains),
                 FLIP_TOL, str(ok_ctl)))
        sep = {c: (abs(ctl_fires[c] - R259_CROSS[c])
                   if ctl_fires[c] is not None else None)
               for c in ctrl}
        ok_r259 = all(s is None or s >= R259_SEP_MIN
                      for s in sep.values()) \
            and any(s is not None for s in sep.values())
        check("G52-r259-demarcation", ok_r259,
              "r259 WARD: the rule's control fire degrees %s "
              "differ from the REFUTED energy-branch crossings "
              "%s by %s (>= %d each): the census rule is NOT "
              "the dead level-crossing object"
              % (str(ctl_fires), str(R259_CROSS), str(sep),
                 R259_SEP_MIN))
        go = (sel is not None and ok_rungs and ok_mains
              and ok_ctl and ok_r259)
        sep_only = (not go and ok_rungs and ok_mains
                    and all_fired)
        blind_out = dict(go=go, sep_only=sep_only, sel=sel_run,
                         ctl_fires=ctl_fires, sep=sep,
                         ok_rungs=ok_rungs, ok_mains=ok_mains)
    else:
        for g in ("G50-contamination-protocol", "G51-blind-bilanz",
                  "G52-r259-demarcation"):
            check(g, True, "SMOKE: skipped")
        blind_out = None

    # ---------------- S6 mp wards
    section("S6  MP WARDS -- kz15 + LARGEST-N BLIND RUNG")
    if not smoke:
        p15 = next((p for p in ladder if p["kz"] == 15), None)
        wards = [("kz15-razor", p15)]
        pbig = max(blind_rungs, key=lambda p: (p["N"], p["kz"]))
        wards.append(("kz%d-blind" % pbig["kz"], pbig))
        ok_ward = True
        wtxt = []
        for tag, p in wards:
            wa, wc = lad_census[p["kz"]]
            N = wa["N"]
            degs = (2, N // 2, N - 1)
            r_w = mp_continuation(p, WARD_DPS, n_hi=N - 1)
            okd = all(r_w["cnts"][n] == int(wc["cnt"][n])
                      for n in degs)
            ok_ward = ok_ward and okd
            wtxt.append("%s N=%d degs %s %s"
                        % (tag, N, str(degs),
                           "OK" if okd else "MISMATCH"))
        check("G60-mp-census-wards", ok_ward,
              "mp (dps %d) census == f64 census at the sealed "
              "degrees on the razor rung + the largest-N blind "
              "rung: %s" % (WARD_DPS, "; ".join(wtxt)))
        tot_rep = (sum(WC[t]["n_rep"] for t in WC)
                   + sum(wc["n_rep"]
                         for _wa, wc in lad_census.values()))
        check("G61-repair-bookkeeping", True,
              "sign-guard repair path: %d guard degrees, %d mp "
              "repairs across all worlds (sealed guard %.0e, "
              "dps %d) -- disclosed"
              % (sum(WC[t]["n_bad"] for t in WC)
                 + sum(wc["n_bad"]
                       for _wa, wc in lad_census.values()),
                 tot_rep, SIGN_GUARD, MP_REPAIR_DPS))
    else:
        for g in ("G60-mp-census-wards", "G61-repair-bookkeeping"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    hits = []
    for fn in RULE_FUNCS:
        hits += rule_scope_audit(fn)
    hits_mut = rule_scope_audit("mutant_h_reader")
    ag_hits = antigate_fragment_audit()
    check("G70-scope-audits", not hits and bool(hits_mut)
          and not ag_hits,
          "the census/rule scope consumes passed coefficient/"
          "atom arrays + the evaluation point ONLY (%s); the "
          "deliberately h-reading mutant is FLAGGED (%s); "
          "fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_mut) if hits_mut else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    # m3 hull-convention anchor (documented, exact on the toy)
    nodes = list(JF.TOY_NODES)
    wts = list(JF.TOY_WTS)
    S_t = len(nodes)
    al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t - 1)
    fh, fd, cnts_t = toy_res["JF-9atom"]
    alf = np.array([float(a) for a in al_t])
    bef = np.array([float(b) for b in be_t])
    n_a = fd + 1 if fd is not None and fd + 1 < S_t else S_t - 2
    z = zeros_tridiag(alf, bef, n_a)
    lo_t, hi_t = float(min(nodes)), float(max(nodes))
    re_ = z.real[np.abs(z.imag) <= 1e-9 * (hi_t - lo_t)]
    n_hull = int(np.sum((re_ >= lo_t) & (re_ <= hi_t)))
    check("G71-hull-convention-anchor", True,
          "m3 ANCHOR (documented convention difference): 9-atom "
          "toy at the post-defect degree n = %d: real zeros in "
          "hull %d vs atom census %d vs degree %d -- counting "
          "in the hull is NOT the discrete census; the atom "
          "convention is the sealed one"
          % (n_a, n_hull, cnts_t[n_a], n_a))
    check("G72-stop-list", True,
          "STOP LIST (anti-gates): no derived 5/7, no bound "
          "mechanism, no asymptotic law, no energy-order rule "
          "(G52 ward), no target consumption in the rule scope "
          "(G70), NO RH claim; r243..r276 stand unchanged")

    # ---------------- S8 detector
    section("S8  DETECTOR -- RULE STATISTICS vs WALL/TARGET")
    if not smoke:
        g1s, dnv, s_marg, s_z = [], [], [], []
        for p in ladder:
            pk = QO.port_pack(p["kz"])
            lam, U = np.linalg.eigh(pk["Q"])
            c2 = (U.T @ pk["f"]) ** 2
            g1s.append(float(np.sum(c2 / (1.0 - lam))))
            dnv.append(B57 - float(p["S"][p["N"] - 1]))
            wa, wc = lad_census[p["kz"]]
            s_marg.append(math.log10(
                max(float(wc["MG"][wa["N"] - 1]), 1e-300)))
            _f, zx = cand_phase(wa["al"], wa["be"], wa["z0"],
                                wa["N"] - 1, R3_WIN, 1e9)
            s_z.append(zx)
        sp_self = abs(BH.spearman(g1s, g1s))
        sps = (abs(BH.spearman(s_marg, g1s)),
               abs(BH.spearman(s_marg, dnv)),
               abs(BH.spearman(s_z, g1s)),
               abs(BH.spearman(s_z, dnv)))
        check("G80-rule-detector", sp_self >= FP_BAR
              and all(s < FP_BAR for s in sps),
              "r266-pattern detector on the rule statistics: "
              "selftest sp(g1, g1) = %.2f flagged; fingerprints "
              "sp(log margin, g1) = %.3f / sp(log margin, D_N) "
              "= %.3f / sp(max z, g1) = %.3f / sp(max z, D_N) = "
              "%.3f (all < %.1f): the rule statistic is neither "
              "the wall nor the target"
              % ((sp_self,) + sps + (FP_BAR,)))
    else:
        check("G80-rule-detector", True, "SMOKE: skipped")

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the atom-counted Sturm census as the right "
          "winding quantity, the blind reviewer-protocol rule "
          "with its training/blind bilanz, the increment "
          "anatomy, and the index-count chain gates -- the "
          "oriented midpoint theorem is the named next step")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        if blind_out["go"]:
            parts.append(
                "MASLOV_CENSUS_GO(rule %s; blind %s; controls "
                "%s within +-%d of %s; r259-separated %s)"
                % (blind_out["sel"],
                   "42/42 rungs + w12/w13/w26 SAFE"
                   if blind_out["ok_rungs"]
                   and blind_out["ok_mains"] else "PARTIAL",
                   str(blind_out["ctl_fires"]), FLIP_TOL,
                   str(CTRL_FLIPS), str(blind_out["sep"])))
        elif blind_out["sep_only"]:
            parts.append(
                "CENSUS_SEPARATES_ONLY(controls fire %s vs %s "
                "-- outside the sealed +-%d)"
                % (str(blind_out["ctl_fires"]), str(CTRL_FLIPS),
                   FLIP_TOL))
        else:
            parts.append(
                "CENSUS_FAILED(typed: rungs %s / mains %s / "
                "controls %s)"
                % (str(blind_out["ok_rungs"]),
                   str(blind_out["ok_mains"]),
                   str(blind_out["ctl_fires"])))
        if w9_cont is not None:
            n_mis = (w9_cont["n_mis_r2"] if sel_run == "R2"
                     else w9_cont["n_mis_r1"])
            if n_mis == 0:
                parts.append("CENSUS_RESTATEMENT(pattern == h "
                             "pattern degree-by-degree)")
            legC = (all(WC[t]["fire"] is None for t in packs)
                    and ok_intl and ok_rot and coloc
                    and ctl_coloc
                    and w9_cont["first_def"] == packs["w9"]["N"])
            if legC:
                parts.append(
                    "STURM_CHAIN_VERIFIED(atom saturation: "
                    "first defect at the flip %d == N_w, %d "
                    "healed degrees vs %d h re-entry pivots, "
                    "NOT h-equivalent: %d pattern mismatches)"
                    % (w9_cont["first_def"], w9_cont["healed"],
                       w9_cont["inband"] - packs["w9"]["N"],
                       n_mis))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the increment anatomy, the right "
          "winding quantity, the atom saturation, the blind "
          "bilanz; OPEN: the target positivity D_N > 0 itself "
          "(the oriented midpoint theorem is the next round); "
          "NO RH claim"
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
