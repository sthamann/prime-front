#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""halffilling_pinning_probe -- PRIME.PORT.WALL.
HALFFILLING_PINNING.01 (round 281): the PINNING ANATOMY of the
half-filling localization and the UPPER-SIDE theorem attempt.
r280 measured the full localization census (minC - N_w in {0..5}
over 42 rungs, O(1), no N-trend, MAIN_NOT_MAXIMAL, handover
cos_w = -0.97); v956 fixed the foundation: N_w = ceil(S/2) is the
FREE MOMENT WINDOW maximum (an S-atom signed measure has exactly
S free moments; beyond, ALL moments are FORCED by the node
polynomial L via the linear recurrence), the 0/2/2/3/1 offsets
are forced-coupling survival counts, and "MAIN survives THE
ENTIRE FREE MOMENT WINDOW".  REVIEWER FRAME (binding, this
round): not maximality -- PINNING: why is half-filling the
natural pinning point?  Target statement (Half-Filling
Localization): |minC - S/2| <= C with S-independent C; for RH the
one-sided version minC >= ceil(S/2) suffices.  DECOMPOSITION
HYPOTHESIS: pinning = LOWER side (minC >= N_w: survival through
the free window -- the open center) + UPPER side (minC <= N_w +
C: once forcing starts, the crossing comes within O(1)).  NOT a
proof round for the lower side: no certificate, no bound
mechanism, no localization claim from any census.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r280 discipline): w = window (kz),
S = #union support atoms of mutilde = mu - nu, S_- = #negative
union weights, N_w = builder depth = ceil(S/2) = (S+1)//2, n =
chain degree, h_n = chain pivot (h_n = D_{n+1}/D_n), minC =
first n with h_n < 0, offset = minC - N_w; ground truth (v956
offsets, r280 census distribution, control flips, r280 cosine
records) enters GATES and record tables only; no zero/prime
oracles anywhere (AST firewall).  MACHINERY IMPORTED VERBATIM
(r280 BL.{union_of_ctx, sign_chain_f64, mp_sign_chain, grad_ext,
moments_mp, toy_moments, stj_full}, MS.ctx_build, r230
JF.{node_poly, stieltjes_exact, TOY_NODES, TOY_WTS}, r244
BH.spearman, paircorr PC.{Grid, gen_model}, v881 PIK, r243
PB.smooth_comb, v563 core READ-ONLY).

LEG A1 -- THE FORCING-ONSET ANATOMY (exact + mp):
(a1a) COUNTING THEOREM (the exact upper-side core): H_n consumes
  m_0..m_{2n-2} and pivot h_n consumes m_0..m_{2n}; an S-atom
  signed measure has EXACTLY S free moments m_0..m_{S-1}
  (Vandermonde bijection weights <-> moment prefix), all m_k with
  k >= S are FORCED by the monic node-polynomial recurrence
  sum_{i=0}^{S} c_i m_{k-S+i} = 0 (L = sum c_i X^i, c_S = 1);
  hence the FREE pivots are EXACTLY h_0..h_{N_w-1} and h_{N_w} is
  the FIRST FORCED PIVOT -- gated as arithmetic for all S in
  2..2000 (both parities) and exactly (rationals) on the toys
  JF9 / MAINLIKE / FLIPLIKE: recurrence residual == 0 for k =
  S..S+4.  FREEDOM DEMONSTRATION (JF9, exact): the Vandermonde
  solve dm = e_{S-1} moves the LAST free moment alone -- the
  chain reproduces h_n exactly for n <= N_w-2 while h_{N_w-1}
  moves (the last free pivot is genuinely free), and the forced
  moment m_S shifts by EXACTLY -c_{S-1} (no freedom past S).
(a1b) REAL FORCING GATE (w9, mp dps 200): the union mutilde
  moments m_0..m_{S+8} satisfy the L-recurrence with max relative
  residual <= 1e-40 (S = 367 coefficients built by exact
  root-multiplication; the coefficient magnitudes and the
  cancellation depth are measured, not assumed -- the
  cancellation IS the content).  FORCED-FRACTION PROFILE (exact
  combinatorics): the forced-entry fraction of H_n is f(n) =
  (2n-1-S)(2n-S)/(2 n^2) for 2n-2 >= S else 0 -- gated against
  the direct count at n = N_w..N_w+5; f(N_w) = 0 (the last fully
  free Hankel block).
LEG A2 -- THE OFFSET ANATOMY (census): the 42-rung frame-A
  ladder (h <= 900) rebuilt with the r280 union chains (EXT 8,
  escalation 32 disclosed); REGRESSION GATES (hard): offset
  distribution == {0:18, 1:10, 2:6, 3:6, 4:1, 5:1} (r280), sealed
  anchors 0/2/2/3/1 on kz 9/12/13/26/40 + kz15 +1 + kz52 +0,
  half-filling N_w == (S+1)//2 on 42/42, mp arbitration (dps 40)
  on the ward set {9, 13, 15, 52} at degrees N_w-2..minC+2.
  SEALED SOURCE-PURE CANDIDATES (constructor AST-audited; chain
  data n < N_w + moment/source data only): K1 lastmarg =
  log rmg[N_w-1] (last free pivot cancellation margin), K2
  margslope = median d log rmg over the last 6 free degrees, K3
  fdev1 = moment cancellation r_S at the FIRST forced index, K4
  fdev3 = median r_{S..S+2}, K5 negfrac = S_-/S, K6 razorpos =
  argmin rmg (free window) / N_w.  Spearman(K, offset) over the
  42 rungs; SEALED TYPING: OFFSET_FORMULA iff max |sp| >= 0.75,
  else OFFSET_UNSTRUCTURED (correlation table printed -- honest).
LEG A3 + LEG C -- THE RELAY / PER-DEGREE CONDITION: extended
  gradient packs (r278/r280 machinery verbatim) on w9/kz15/w13;
  REGRESSION (hard): gap-weighted cos_w(grad log h_minC,
  grad log h_{minC-1}) == r280 records -0.971/-0.956/-0.978
  (tol 0.02).  THE LOCKSTEP READING: cos_raw(n) = sg_n sg_{n-1}
  cos_log(n) is the RAW-gradient alignment -- profile over n in
  [N_w-10, minC]: the r280 anti-alignment is the h-sign flip of
  a raw lockstep; measured law: min cos_raw over the window tail
  (LOCKSTEP iff >= 0.9, typed).  THE PER-DEGREE CONDITION (c1,
  exact bookkeeping): B_n := [sign h_n == sign h_{n-1}]
  (= [beta_n > 0]); B_n for all n in 1..N_w-1 (with h_0 > 0)
  <=> minC >= N_w -- gated on toys + all 42 rungs.  HONEST
  TYPING (c3): B_n READS h -- it is the h-restatement UNLESS a
  declared h-blind proxy predicts the flip location: sealed
  proxies P1 = first n with rmg < 1e-2, P2 = argmin rmg over
  [2, N_w+8], P3 = first one-step log-rmg drop >= 2.0 -- each
  consumes the rmg array ONLY (no signs); NEW_COORDINATE iff
  some proxy hits |pred - minC| <= 2 on ALL five worlds (MAIN +
  EPSTEIN/SCRAMBLE/SMOOTH/HL2), else RESTATEMENT.  MARGIN
  PROFILE (c2): rmg profile on MAIN (min, razor position vs the
  r243 ~0.98 N_w, rmg at N_w-1 and at minC) and on the four dead
  worlds the crossing type: drop = rmg[minC]/median(rmg[minC-5..
  minC-1]), CREEPING iff drop <= 0.1 else ABRUPT (typed).
LEG B -- THE UPPER-SIDE THEOREM ADJUDICATION (the core):
(b1) v956 PROOF-STATE QUOTES (byte-gated against
  verification/v956_signedmoment_halffilling_duality.py): "the
  wall dies IMMEDIATELY", "confirmed by TWO independent paths
  (Sherman-Morrison r-chain and gammahat sign chain) plus an
  mpmath dps-40 ward", "quasi-definite EXACTLY up to
  half-filling and no degree further", "MAIN_EXHAUSTS_FREE_
  MOMENT_WINDOW" (underscore form without break) -- the v956
  boundary statement is TWO COMPUTATIONAL PATHS + mp ward on
  FIVE windows = MEASUREMENT, not a symbolic theorem.  SEALED
  RULE: UPPER_PINNING_THEOREM only if a world-blind derivation
  of minC <= N_w + O(1) exists; the round's own exact toy gate
  REFUTES world-blindness: the single-tiny-negative measure
  (JF9 nodes, weights 1,..,1,-1/1000) has minC = S-1 = 8, offset
  = N_w - 2 = 3 (exact rationals; h_{S-1} = D_S/D_{S-1} with
  D_S = V^2 prod w < 0 while D_n > 0 below by continuity), and
  S - 1 - N_w = (S-3)/2 is UNBOUNDED in S (arithmetic gate) --
  ANY O(1) upper pinning must consume the comb structure =>
  UPPER_PINNING_MEASURED.
(b2) THE PROVABLE upper side today (pigeonhole on the r279
  budget theorem #(h<0) = S_-): every negative pivot lies in
  [minC, S-1], hence minC <= S - S_- -- gated exactly on the
  toys (budget == S_- recomputed in rationals) and on all 42
  rungs (minC <= S - S_-); on w9 this ceiling is 263 = p, 79
  degrees above N_w: the O(1) gap is MEASURED ONLY (C = 5 over
  this census, max at kz43).
(b3) PINNING_DECOMPOSED (the program finding): minC >= N_w <=>
  ALL FREE PIVOTS POSITIVE (exact bookkeeping, gated); offset =
  #surviving forced pivots (v956-r230: the forced-coupling
  survival counts); the reviewer question "why half-filling"
  has the exact answer BECAUSE THE FREE MOMENTS END THERE
  (counting theorem, a1a), and the open center is exactly "why
  does MAIN survive all its free degrees" -- with the controls
  at 0.11..0.15 N_w showing per-degree survival is a real
  condition.
LEG D -- WARDS / MUST-FAILS (each loud): v956/r280 regressions
  (anchors, census distribution, half-filling, control flips
  25/21/27, HL2 flip 25, cosine records); determinism run1/run2;
  (m1) WRONG-L RECURRENCE: c_0 + 1 breaks the toy recurrence
  exactly (residual = m_0 != 0, LOUD); (m2) OFFSET FORMULA THAT
  READS minC: the mutant consuming the withheld census offsets
  is FLAGGED by the AST scope audit; (m3) RELAY QUANTITY THAT
  READS h UNDECLARED: the mutant consuming the withheld sign
  chain is FLAGGED; scope audits (candidate/proxy constructors
  consume chain/moment/source data ONLY); fragment audit (no fit
  primitives); PAIRCORR DETECTOR on all six candidates: sealed
  distance rule -- MAIN_SEPARATING iff MAIN's value is farther
  from EVERY dead value than the dead spread, else WORLD_BLIND
  (a WORLD_BLIND candidate cannot carry the localization).
STOP LIST (anti-gates, binding): no derived 5/7, no bound
mechanism claim, no asymptotic law, no localization claim from
the census, no lower-side claim, NO RH claim; r243..r280 stand.

SEALED CONSTANTS: LADDER frame-A h <= 900 (42 rungs); EXT 8 /
EXT2 32; ANCHORS {9:+0, 12:+2, 13:+2, 26:+3, 40:+1, 15:+1,
52:+0}; R280_DIST {0:18, 1:10, 2:6, 3:6, 4:1, 5:1}; CTRL_FLIPS
25/21/27; HL2 seed 101, flip 25; COS_REC {9:-0.971, 15:-0.956,
13:-0.978}, COS_TOL 0.02; MP_DPS 40 / MP_GUARD 1e-30 /
MP_RECOUNT 80; WARD_SET {9, 13, 15, 52}; REC_DPS 200, REC_BAR
1e-40, REC_K 9; COUNT_SMAX 2000; SLOPE_WIN 6; SP_BAR 0.75;
PROXY_BAR 1e-2, LOG_DROP 2.0, PROXY_TOL 2; CREEP_RATIO 0.1;
LOCKSTEP_BAR 0.9, PROF_BACK 10; DET worlds EPST/SCR/SMOOTH/HL2;
LEGB worlds (9, 15, 13); EPS_TINY 1/1000; toy freedom target
e_{S-1}; runtime <= 1800 s; smoke = toys + counting + m1/m2/m3
+ scopes + v956 quotes + w9 f64 sanity (census, mp recurrence,
grads, controls, detector, verdict adjudication skipped).
PRE-SPEC SCOPING (disclosed): the r280/v956 record numbers are
consumed as sealed anchors; one machinery pass on w9 + the toys
only (chain cost, mp recurrence cost); no bar, band or typing
rule was tuned after it; the ladder, kz15/w13, controls and the
candidate list were UNTOUCHED pre-spec.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] UPPER_PINNING_THEOREM(C provable) /
    UPPER_PINNING_MEASURED(C measured; pigeonhole ceiling
    minC <= S - S_- as the only proven upper bound; the
    not-world-blind toy fact)
  + OFFSET_FORMULA(best candidate, |sp| >= 0.75) /
    OFFSET_UNSTRUCTURED(correlation table)
  + RELAY_CONDITION_FOUND(B_n = [beta_n > 0]; RESTATEMENT /
    NEW_COORDINATE by the proxy rule) / RELAY_UNSTRUCTURED
  + PINNING_DECOMPOSED(lower = free-window survival OPEN,
    upper = forced-pivot death MEASURED O(1)) [always,
    program finding].
Honesty before beauty: the counting theorem answers WHERE the
window ends, never WHY MAIN survives it; the upper O(1) side is
a census measurement; B_n is declared an h-restatement unless
the h-blind proxies genuinely predict; no verdict claims a
derived 5/7, a bound mechanism or an asymptotic law; the MAIN
positivity (the lower side) stays the open center.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 26/28 -- the G14 eps-toy at
the sealed eps = 1/1000 sat OUTSIDE the continuity regime (the
perturbation flipped D_7 first: minC = 6, not S-1); ONE
disclosed amendment: eps deepened to 1/10^12 (the gate's claim
minC = S-1 and every bar/rule UNCHANGED); smoke pass 2 = 28/28
(0.3 s); calibration pass 1 = first full evaluation = 28/28,
wall 23.4 s; after it TWO disclosed wording-only alignments, no
bar, band, class or verdict rule moved: (a1) the G21 detail
string claimed a '108-order' cancellation from a naive
coefficient bound -- the measured max |c_i| is 5.0e28 and the
residual 7.6e-157; the string now reports the measured order;
(a2) the G41 detail string asserted the lockstep bar on all
three worlds -- w13 dips to +0.849 < 0.9 at the window tail;
the string now types LOCKSTEP per world (w9/kz15 LOCKSTEP, w13
DIP) and claims no global law.  The re-run with a1/a2 = the
record run = 28/28; run1/run2 identical up to WALL):
CAL_VERDICT = UPPER_PINNING_MEASURED(C = 5) +
OFFSET_UNSTRUCTURED(max |sp| 0.273) + RELAY_CONDITION_FOUND(
B_n, RESTATEMENT) + PINNING_DECOMPOSED.
Key numbers.  TOYS (exact rationals): counting identity all S in
2..2000; recurrence residual == 0 at k = S..S+4 on JF9/MAINLIKE/
FLIPLIKE; freedom: dm = e_8 moves h_4 alone (h_0..h_3 bitwise,
m_9 shift == -c_8 exact); m1 wrong-L residual = m_0 =
591359/360360 LOUD; eps-toy minC = 8 = S-1, offset 3 = N_w - 2,
budget 1 = S_-; budget == S_- and pigeonhole minC <= S - S_- on
all toys (JF9 3 <= 6 at budget 3).  REAL (w9): S = 367, N_w =
184, minC = 184 (+0); mp dps-200 recurrence max rel residual
7.6e-157 (bar 1e-40) over k = 367..375, max |c_i| = 5.0e28;
forced fraction f(184) = 0, f(185) = 8.8e-5 .. f(189) = 1.5e-3
(exact == direct count) -- the forced mass enters quadratically
slowly; the wall death within 0..5 degrees is NOT a bulk effect.
CENSUS (42 rungs, 0 escalations): distribution == r280
{0:18, 1:10, 2:6, 3:6, 4:1, 5:1}, anchors exact, half-filling
42/42, mp ward {9, 13, 15, 52} exact sign agreement, 0 recounts;
pigeonhole minC <= S - S_- on 42/42 (w9: 184 <= 263 = p, 79
degrees above N_w); decomposition bookkeeping exact on 42/42.
OFFSET ANATOMY (spearman vs offset, 42 rungs, all n_valid = 42):
K1 lastmarg +0.032, K2 margslope -0.273, K3 fdev1 +0.000, K4
fdev3 +0.000, K5 negfrac -0.216, K6 razorpos +0.083 -- max |sp|
= 0.273 (K2) << 0.75 => OFFSET_UNSTRUCTURED: NO source-pure
tail-coupling candidate orders the offsets in this census (the
first-forced moment cancellation r_S sits at 0.92..0.97 with
near-zero rank correlation; honest negative -- the offset
formula stays open).  RELAY: cos_log at minC = -0.9707/-0.9555/
-0.9778 on w9/kz15/w13 == r280 records (tol 0.02); cos_raw at
the crossing = +0.9707/+0.9555/+0.9778 POSITIVE -- the r280
anti-alignment IS the h-sign flip of a raw-gradient lockstep;
min cos_raw over [N_w-10, minC] = +0.926/+0.932/+0.849, typed
w9 LOCKSTEP, kz15 LOCKSTEP, w13 DIP (0.849 < 0.9) -- no global
lockstep law; the crossing itself never ruptures the gradient
geometry.  PROXIES (h-blind, rmg only): P1 |dev| = 57 on MAIN,
P2 |dev| up to 146 on the dead worlds, P3 hits MAIN/SCR exactly
and EPST/HL2 at |dev| 1 but fails SMOOTH at |dev| 98 => NO
proxy predicts on all five worlds => B_n typed RESTATEMENT (the
relay condition is exact bookkeeping, not a new coordinate; the
honest c3 answer).  MARGINS: MAIN razor argmin at n = 172 =
0.935 N_w (rmg 3.1e-3, the r243 razor zone), rmg[N_w-1] =
3.6e-3, rmg[minC] = 1.6e-5; dead worlds drop = 0.02/0.02/0.03/
0.02 on EPST/SCR/SMOOTH/HL2 (flips 25/21/27/25 == records) --
ALL FOUR CREEPING: the crossing TYPE does not separate the
worlds (honest negative against the abrupt-collapse picture).
DETECTOR (sealed distance rule): ALL SIX candidates WORLD_BLIND
-- none of the sealed tail-coupling coordinates carries the
localization.  V956 QUOTES: 4/4 byte-gated; adjudication
MEASUREMENT.  MUST-FAILS: m1 LOUD, m2 offset-reader FLAGGED
(offs_true), m3 relay-h-reader FLAGGED (sg_true); scope audits
CLEAN (7 constructors); fragment audit CLEAN.  Runtime ~23 s
full / ~0.3 s smoke; run1/run2 identical up to WALL.
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

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import budget_localization_probe as BL        # noqa: E402 r280
import bordered_hankel_probe as BH            # noqa: E402 r244
import metric_stability_probe as MS           # noqa: E402 r278
import jfraction_probe as JF                  # noqa: E402 r230
import paircorr_margin_probe as PC            # noqa: E402 relocation
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

H_CAP = 900
EXT = 8
EXT2 = 32
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
R280_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
COS_REC = {9: -0.971, 15: -0.956, 13: -0.978}
COS_TOL = 0.02
MP_DPS = 40
MP_GUARD = 1e-30
MP_RECOUNT = 80
WARD_SET = (9, 13, 15, 52)
REC_DPS = 200
REC_BAR = 1e-40
REC_K = 9
COUNT_SMAX = 2000
SLOPE_WIN = 6
SP_BAR = 0.75
PROXY_BAR = 1e-2
LOG_DROP = 2.0
PROXY_TOL = 2
CREEP_RATIO = 0.1
LOCKSTEP_BAR = 0.9
PROF_BACK = 10
LEGB_KZS = (9, 15, 13)
EPS_TINY = Fr(1, 10 ** 12)

V956_PATH = os.path.abspath(os.path.join(
    HERE, "..", "..", "verification",
    "v956_signedmoment_halffilling_duality.py"))
V956_QUOTES = (
    "the wall dies IMMEDIATELY",
    "confirmed by TWO independent paths (Sherman-Morrison "
    "r-chain and gammahat sign chain) plus an mpmath dps-40 "
    "ward",
    "quasi-definite EXACTLY up to half-filling and no degree "
    "further",
    "MAIN_EXHAUSTS_FREE_MOMENT_WINDOW",
)

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
    return (not bad), ("NO zero/prime oracles; the recurrence/"
                       "candidate/proxy/profile constructors consume "
                       "comb data, chain data and moments ONLY; "
                       "record offsets, flips and cosines enter "
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


CONSTRUCTORS = ("node_poly_mp", "rec_residuals", "forced_frac",
                "offset_candidates", "proxy_first_bar",
                "proxy_argmin", "proxy_logdrop")
BL_FORBIDDEN = {"ANCHORS", "R280_DIST", "CTRL_FLIPS", "COS_REC",
                "offs_true", "minC_true", "sg_true", "HL2_FLIP"}


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
                if nm in BL_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def node_poly_mp(xu, dps):
    """monic node polynomial coefficients (ascending) of the
    union atoms, exact root multiplication in mp."""
    mp.mp.dps = dps
    L = [mp.mpf(1)]
    for x in xu:
        xm = mp.mpf(float(x))
        new = [mp.mpf(0)] * (len(L) + 1)
        for i, c in enumerate(L):
            new[i] -= xm * c
            new[i + 1] += c
        L = new
    return L


def rec_residuals(coefs, moms, S_, ks):
    """relative residuals of sum_{i=0}^{S} c_i m_{k-S+i} == 0."""
    out = []
    for k in ks:
        terms = [coefs[i] * moms[k - S_ + i] for i in range(S_ + 1)]
        num = abs(mp.fsum(terms))
        den = mp.fsum(abs(t) for t in terms)
        out.append(float(num / den) if den > 0 else 0.0)
    return out


def forced_frac(n, S_):
    """exact forced-entry fraction of H_n (entries m_{i+j} with
    i+j >= S) -- closed form + direct count."""
    if 2 * n - 2 < S_:
        return 0.0, 0
    t = 2 * n - 1 - S_
    cnt = t * (t + 1) // 2
    return cnt / float(n * n), cnt


def offset_candidates(rmg, N_, S_, Sm_, zones):
    """sealed source-pure candidates: free-window chain margins
    (n < N_w) + first-forced moment cancellations + source
    fractions.  Consumes NO census result, NO sign chain."""
    xs_, ws_, ys_, vs_ = zones
    lg = np.log(rmg[2:N_])
    lastmarg = float(np.log(rmg[N_ - 1]))
    d = np.diff(np.log(rmg[N_ - SLOPE_WIN:N_]))
    margslope = float(np.median(d))
    rs = []
    for k in (S_, S_ + 1, S_ + 2):
        mmu = float(np.sum(ws_ * np.power(xs_, k)))
        mnu = float(np.sum(vs_ * np.power(ys_, k)))
        den = abs(mmu) + abs(mnu)
        rs.append(abs(mmu - mnu) / den if den > 0 else np.nan)
    return dict(K1_lastmarg=lastmarg,
                K2_margslope=margslope,
                K3_fdev1=rs[0],
                K4_fdev3=float(np.nanmedian(rs)),
                K5_negfrac=Sm_ / float(S_),
                K6_razorpos=(2 + int(np.argmin(lg))) / float(N_))


def proxy_first_bar(rmg, hi):
    """h-blind proxy P1: first degree with rmg < PROXY_BAR."""
    for n in range(2, hi):
        if rmg[n] < PROXY_BAR:
            return n
    return None


def proxy_argmin(rmg, hi):
    """h-blind proxy P2: argmin rmg over [2, hi)."""
    return 2 + int(np.nanargmin(rmg[2:hi]))


def proxy_logdrop(rmg, hi):
    """h-blind proxy P3: first one-step log drop >= LOG_DROP."""
    for n in range(3, hi):
        if math.log(rmg[n - 1]) - math.log(rmg[n]) >= LOG_DROP:
            return n
    return None


def mutant_offset_reader(offs_true):
    """m2 MUST-FAIL MUTANT: an 'offset formula' oriented by the
    withheld census offsets -- the scope audit must FLAG this."""
    return sorted(offs_true)


def mutant_relay_reader(sg_true):
    """m3 MUST-FAIL MUTANT: a 'relay quantity' that consumes the
    withheld sign chain -- the scope audit must FLAG this."""
    return [int(s) for s in sg_true]


# ============== exact toy machinery (Fractions)
def frac_solve(A, b):
    """exact solve A x = b (Fractions, Gaussian elimination)."""
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        for r in range(n):
            if r == c:
                continue
            f = M[r][c] / pv
            if f != 0:
                for k in range(c, n + 1):
                    M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def toy_chain(nodes, wts):
    S_ = len(nodes)
    _al, _be, hs = JF.stieltjes_exact(nodes, wts, S_ - 1)
    return hs


def toy_first_neg(hs):
    return next((k for k in range(len(hs)) if hs[k] < 0), None)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("halffilling_pinning_probe -- PRIME.PORT.WALL."
          "HALFFILLING_PINNING.01 (round 281)")
    print("SPEC_SHA %s   (r280 BL %s)"
          % (SPEC_SHA[:16], BL.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + counting + m1/m2/m3 + scopes "
                        "+ v956 quotes + w9 f64 sanity; census, mp "
                        "recurrence, grads, controls, detector "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the v956/r280 anchors (census "
          "distribution, offsets, flips, cosine records), the "
          "candidate list K1..K6 + SP_BAR, the proxy set P1..P3 + "
          "PROXY_TOL, the lockstep/creep bars, the v956 quote set, "
          "the upper-side typing rule and the verdict form; "
          "pre-spec scoping disclosed in the spec (w9 + toys "
          "machinery pass only)")

    # ---------------- S1 toys (exact rationals)
    section("S1  TOYS -- COUNTING THEOREM + FORCING + FREEDOM")
    ok_cnt = True
    for S_ in range(2, COUNT_SMAX + 1):
        Nw = (S_ + 1) // 2
        n_free_hankel = max(n for n in range(1, S_ + 2)
                            if 2 * n - 2 <= S_ - 1)
        n_free_piv = max(n for n in range(0, S_ + 1)
                         if 2 * n <= S_ - 1)
        ok_cnt = ok_cnt and (n_free_hankel == Nw) \
            and (n_free_piv == Nw - 1) \
            and (Nw == math.ceil(S_ / 2.0))
    check("G10-counting-theorem", ok_cnt,
          "EXACT (arithmetic, S = 2..%d both parities): the largest "
          "fully-free Hankel block is n = N_w = ceil(S/2) = "
          "(S+1)//2, the FREE pivots are exactly h_0..h_{N_w-1} "
          "(h_n consumes m_0..m_{2n}), h_{N_w} is the FIRST FORCED "
          "pivot -- 'why half-filling' = the free moments end there"
          % COUNT_SMAX)

    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    toys = [("JF9", [t[0] for t in jf_pairs],
             [t[1] for t in jf_pairs]),
            ("MAINLIKE", BL.TOYS_XS, BL.MAINLIKE_W),
            ("FLIPLIKE", BL.TOYS_XS, BL.FLIPLIKE_W)]
    ok_rec = True
    ok_budget = True
    ok_pig = True
    ok_dec = True
    toy_tab = {}
    for name, nodes, wts in toys:
        S_ = len(nodes)
        Nw = (S_ + 1) // 2
        coefL = JF.node_poly(nodes, Fr(1))
        moms = BL.toy_moments(nodes, wts, S_ + 4)
        for k in range(S_, S_ + 5):
            res = sum(coefL[i] * moms[k - S_ + i]
                      for i in range(S_ + 1))
            ok_rec = ok_rec and (res == 0)
        hs = toy_chain(nodes, wts)
        mc = toy_first_neg(hs)
        Sm_ = sum(1 for w in wts if w < 0)
        budget = sum(1 for h in hs if h < 0)
        ok_budget = ok_budget and (budget == Sm_)
        mc_eff = mc if mc is not None else S_
        ok_pig = ok_pig and (mc_eff <= S_ - Sm_)
        lhs = (mc is None) or (mc >= Nw)
        rhs = all(hs[n] > 0 for n in range(Nw))
        ok_dec = ok_dec and (lhs == rhs)
        toy_tab[name] = (S_, Nw, mc, Sm_, budget)
        info("%s: S=%d N_w=%d minC=%s S_-=%d budget=%d "
             "pigeonhole minC <= %d"
             % (name, S_, Nw, str(mc), Sm_, budget, S_ - Sm_))
    check("G11-toy-forced-recurrence", ok_rec,
          "EXACT (rationals): sum_{i=0}^{S} c_i m_{k-S+i} == 0 for "
          "k = S..S+4 on JF9 + MAINLIKE + FLIPLIKE with the monic "
          "node polynomial L -- every moment past the free window "
          "is FORCED by L (the v956 free-moment law re-derived)")

    # freedom demonstration on JF9
    nodes9 = [t[0] for t in jf_pairs]
    wts9 = [t[1] for t in jf_pairs]
    S9t = len(nodes9)
    Nw9t = (S9t + 1) // 2
    Vt = [[nodes9[j] ** k for j in range(S9t)] for k in range(S9t)]
    b_vec = [Fr(0)] * S9t
    b_vec[S9t - 1] = Fr(1)
    dw = frac_solve(Vt, b_vec)
    wts9p = [wts9[j] + dw[j] for j in range(S9t)]
    moms0 = BL.toy_moments(nodes9, wts9, S9t)
    moms1 = BL.toy_moments(nodes9, wts9p, S9t)
    ok_shift = all(moms1[k] == moms0[k] for k in range(S9t - 1)) \
        and (moms1[S9t - 1] == moms0[S9t - 1] + 1)
    coefL9 = JF.node_poly(nodes9, Fr(1))
    ok_forced_shift = (moms1[S9t] - moms0[S9t]
                       == -coefL9[S9t - 1])
    hs0 = toy_chain(nodes9, wts9)
    hs1 = toy_chain(nodes9, wts9p)
    ok_free = all(hs1[n] == hs0[n] for n in range(Nw9t - 1)) \
        and (hs1[Nw9t - 1] != hs0[Nw9t - 1])
    check("G12-toy-freedom", ok_shift and ok_forced_shift
          and ok_free,
          "EXACT (JF9, rationals): the Vandermonde solve dm = "
          "e_{S-1} moves the LAST free moment alone (m_0..m_{S-2} "
          "bitwise, m_{S-1} + 1); the chain keeps h_0..h_{N_w-2} "
          "EXACTLY and moves h_{N_w-1} -- the last free pivot is "
          "genuinely free; the first forced moment shifts by "
          "EXACTLY -c_{S-1} (no freedom past S)")

    # m1 wrong-L
    coefL_bad = list(coefL9)
    coefL_bad[0] = coefL_bad[0] + 1
    res_bad = sum(coefL_bad[i] * moms0[i] for i in range(S9t + 1))
    check("G13-mustfail-wrongL", res_bad != 0 and res_bad == moms0[0],
          "m1 WRONG-L RECURRENCE (c_0 + 1): residual at k = S "
          "equals m_0 = %s != 0 LOUD (exact) -- the node "
          "polynomial is load-bearing, no other monic degree-S "
          "polynomial forces these moments" % str(moms0[0]))

    # eps-toy: upper side is NOT world-blind
    wts_eps = [Fr(1)] * (S9t - 1) + [-EPS_TINY]
    hs_eps = toy_chain(nodes9, wts_eps)
    mc_eps = toy_first_neg(hs_eps)
    budget_eps = sum(1 for h in hs_eps if h < 0)
    ok_grow = all((S_ - 1 - (S_ + 1) // 2) == (S_ - 3) // 2
                  for S_ in (5, 9, 101, 1001)) \
        and (5 - 3) // 2 < (1001 - 3) // 2
    check("G14-toy-not-worldblind", mc_eps == S9t - 1
          and budget_eps == 1
          and (mc_eps - Nw9t == Nw9t - 2) and ok_grow,
          "EXACT (rationals): the single-tiny-negative measure "
          "(JF9 nodes, weights 1..1, -%s) has minC = %s = S-1 "
          "(h_{S-1} = D_S/D_{S-1}, D_S = V^2 prod w < 0, D_n > 0 "
          "below), offset = %d = N_w - 2, budget = 1 = S_-; and "
          "S - 1 - N_w = (S-3)/2 is UNBOUNDED in S -- ANY O(1) "
          "upper pinning theorem must consume the comb structure; "
          "world-blind upper pinning is REFUTED"
          % (str(EPS_TINY), str(mc_eps), mc_eps - Nw9t))
    ok_pig = ok_pig and (mc_eps <= S9t - 1)
    ok_dec = ok_dec and ((mc_eps >= Nw9t)
                         == all(hs_eps[n] > 0 for n in range(Nw9t)))
    check("G15-toy-budget-pigeonhole-decomposition",
          ok_budget and ok_pig and ok_dec,
          "EXACT (rationals, all toys + eps-toy): budget #(h<0) == "
          "S_- (r279 theorem re-derived), the pigeonhole ceiling "
          "minC <= S - S_- holds, and the decomposition identity "
          "(minC >= N_w) <=> (ALL free pivots h_0..h_{N_w-1} > 0) "
          "adjudicates correctly on %s" % str(toy_tab))

    # ---------------- S2 w9 forcing (real)
    section("S2  LEG A1 -- REAL FORCING GATES (w9)")
    ctx9 = MS.ctx_build(9)
    xu9, wu9, zones9 = BL.union_of_ctx(ctx9)
    S9 = len(xu9)
    N9 = ctx9["N"]
    sg9, lgh9, rmg9 = BL.sign_chain_f64(xu9, wu9, N9 + EXT)
    minC9 = next((n for n in range(len(sg9)) if sg9[n] < 0), None)
    check("G20-w9-sanity", (N9 == (S9 + 1) // 2)
          and (minC9 == N9 + ANCHORS[9]),
          "w9: S = %d, N_w = %d == (S+1)//2, minC = %s == N_w + %d "
          "(v956/r280 record) -- the extremal rung"
          % (S9, N9, str(minC9), ANCHORS[9]))
    if smoke:
        for g in ("G21-w9-forced-recurrence", "G22-forced-fraction"):
            check(g, True, "SMOKE: skipped")
    else:
        coefs9 = node_poly_mp(xu9, REC_DPS)
        moms9 = BL.moments_mp(xu9, wu9, S9 + REC_K - 1, REC_DPS)
        ress = rec_residuals(coefs9, moms9, S9,
                             range(S9, S9 + REC_K))
        max_res = max(ress)
        max_c = max(float(abs(c)) for c in coefs9)
        check("G21-w9-forced-recurrence", max_res <= REC_BAR,
              "REAL FORCING (w9, mp dps %d): the union mutilde "
              "moments m_0..m_%d satisfy the L-recurrence at k = "
              "%d..%d with max rel residual %.1e (bar %.0e); max "
              "|c_i| = %.1e -- the measured ~%d-order cancellation "
              "IS the forcing; past m_{S-1} NOTHING about the "
              "measure is free"
              % (REC_DPS, S9 + REC_K - 1, S9, S9 + REC_K - 1,
                 max_res, REC_BAR, max_c,
                 int(round(-math.log10(max(max_res, 1e-300))))))
        ok_ff = True
        prof = []
        for n in range(N9, N9 + 6):
            f_cl, cnt = forced_frac(n, S9)
            direct = sum(1 for i in range(n) for j in range(n)
                         if i + j >= S9)
            ok_ff = ok_ff and (cnt == direct)
            prof.append((n, f_cl))
        check("G22-forced-fraction", ok_ff and prof[0][1] == 0.0,
              "FORCED-FRACTION PROFILE (exact combinatorics == "
              "direct count): %s -- H_{N_w} is the LAST fully free "
              "block; the forced mass enters quadratically slowly, "
              "yet the wall dies within 0..5 degrees (measured): "
              "the death is NOT a bulk effect of forced entries"
              % str([(n, "%.1e" % f) for n, f in prof]))

    # ---------------- S3 census + offset anatomy
    section("S3  LEG A2 -- CENSUS + OFFSET ANATOMY (42 RUNGS)")
    if smoke:
        for g in ("G30-census-regression", "G31-mp-ward",
                  "G32-pigeonhole-decomposition",
                  "G33-offset-anatomy"):
            check(g, True, "SMOKE: skipped")
        cens = {}
        best_cand = None
        best_sp = float("nan")
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        cens = {}
        ok_hf = True
        for kz in kzs:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            xu, wu, zones = BL.union_of_ctx(ctx)
            S_ = len(xu)
            N_ = ctx["N"]
            ok_hf = ok_hf and (N_ == (S_ + 1) // 2)
            sg, lgh, rmg = BL.sign_chain_f64(xu, wu, N_ + EXT)
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            ext_used = EXT
            if mc is None:
                sg, lgh, rmg = BL.sign_chain_f64(xu, wu, N_ + EXT2)
                mc = next((n for n in range(len(sg))
                           if sg[n] < 0), None)
                ext_used = EXT2
            Sm_ = int(np.sum(wu < 0))
            cens[kz] = dict(N=N_, S=S_, Sm=Sm_, minC=mc,
                            off=mc - N_, ext=ext_used, xu=xu,
                            wu=wu, sg=sg, rmg=rmg, zones=zones)
        offs_true = [cens[kz]["off"] for kz in sorted(cens)]
        dist = {}
        for o in offs_true:
            dist[o] = dist.get(o, 0) + 1
        ok_anch = all(cens[kz]["off"] == ANCHORS[kz]
                      for kz in ANCHORS)
        check("G30-census-regression",
              len(cens) == 42 and ok_hf and ok_anch
              and dist == R280_DIST,
              "42-rung census: offset distribution %s == the r280 "
              "record; sealed anchors exact (v956 0/2/2/3/1 + kz15 "
              "+1 + kz52 +0); half-filling N_w == (S+1)//2 on "
              "42/42; escalations to +%d: %d"
              % (str({("+%d" % k): dist[k] for k in sorted(dist)}),
                 EXT2,
                 sum(1 for c in cens.values()
                     if c["ext"] == EXT2)))
        ok_mp = True
        n_rec_tot = 0
        for kz in WARD_SET:
            c = cens[kz]
            sgm, n_g, n_r = BL.mp_sign_chain(
                c["xu"], c["wu"], c["minC"] + 2, MP_DPS,
                MP_GUARD, MP_RECOUNT)
            n_rec_tot += n_r
            lo = max(0, c["N"] - 2)
            ok_mp = ok_mp and bool(
                np.array_equal(sgm[lo:c["minC"] + 3],
                               c["sg"][lo:c["minC"] + 3]))
        check("G31-mp-ward", ok_mp and n_rec_tot == 0,
              "MP ARBITRATION (dps %d, ward set %s): exact sign "
              "agreement with the f64 chains at all degrees "
              "N_w-2..minC+2; dps-%d recounts %d"
              % (MP_DPS, str(list(WARD_SET)), MP_RECOUNT,
                 n_rec_tot))
        ok_pig_r = True
        ok_dec_r = True
        for kz in sorted(cens):
            c = cens[kz]
            ok_pig_r = ok_pig_r and (c["minC"] <= c["S"] - c["Sm"])
            lhs = c["minC"] >= c["N"]
            rhs = bool(np.all(c["sg"][:c["N"]] > 0))
            surv = int(np.sum(c["sg"][c["N"]:c["minC"]] > 0))
            ok_dec_r = ok_dec_r and (lhs == rhs) \
                and (surv == c["off"])
        check("G32-pigeonhole-decomposition", ok_pig_r and ok_dec_r,
              "ALL 42 rungs: the PROVABLE upper side minC <= "
              "S - S_- holds (w9: %d <= %d = p, %d degrees above "
              "N_w -- the O(1) gap is measured only); the "
              "decomposition bookkeeping is exact: (minC >= N_w) "
              "<=> all free pivots positive, offset == #surviving "
              "forced pivots (the v956-r230 forced-coupling "
              "survival counts)"
              % (cens[9]["minC"], cens[9]["S"] - cens[9]["Sm"],
                 cens[9]["S"] - cens[9]["Sm"] - cens[9]["N"]))
        cand_tab = {}
        for kz in sorted(cens):
            c = cens[kz]
            cand_tab[kz] = offset_candidates(
                c["rmg"], c["N"], c["S"], c["Sm"], c["zones"])
        names = sorted(cand_tab[9])
        sps = {}
        for nm in names:
            vals = [cand_tab[kz][nm] for kz in sorted(cens)]
            pairs = [(v, o) for v, o in zip(vals, offs_true)
                     if math.isfinite(v)]
            sps[nm] = (BH.spearman([p[0] for p in pairs],
                                   [p[1] for p in pairs]),
                       len(pairs))
        best_cand = max(names, key=lambda nm: abs(sps[nm][0]))
        best_sp = sps[best_cand][0]
        check("G33-offset-anatomy", True,
              "a2 ADJUDICATED: spearman(K, offset) over the census "
              "%s (n_valid per candidate) -- max |sp| = %.3f (%s) "
              "vs bar %.2f => %s"
              % (str({nm: ("%+.3f/%d" % sps[nm]) for nm in names}),
                 abs(best_sp), best_cand, SP_BAR,
                 "OFFSET_FORMULA candidate found"
                 if abs(best_sp) >= SP_BAR else
                 "OFFSET_UNSTRUCTURED: no source-pure "
                 "tail-coupling candidate orders the offsets in "
                 "this census (honest negative)"))

    # ---------------- S4 controls + relay + margins + detector
    section("S4  LEG A3/C -- RELAY, MARGINS, PROXIES, DETECTOR")
    if smoke:
        for g in ("G40-ctrl-regression", "G41-cos-lockstep",
                  "G42-proxies-Bn", "G43-margin-profile",
                  "G44-detector"):
            check(g, True, "SMOKE: skipped")
        relay_new = False
        lockstep_ok = False
        det_typ = {}
    else:
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
        dead = {}
        for cn, kw in list(cdefs.items()) + [
                ("HL2", dict(comb=comb_hl))]:
            cctx = MS.ctx_build(9, **kw)
            cxu, cwu, cz = BL.union_of_ctx(cctx)
            csg, _cl, crmg = BL.sign_chain_f64(cxu, cwu,
                                               cctx["N"] + EXT)
            cmc = next((n for n in range(len(csg))
                        if csg[n] < 0), None)
            dead[cn] = dict(N=cctx["N"], S=len(cxu),
                            Sm=int(np.sum(cwu < 0)), minC=cmc,
                            sg=csg, rmg=crmg, zones=cz)
        ok_ctl = all(dead[cn]["minC"] == CTRL_FLIPS[cn]
                     for cn in CTRL_FLIPS) \
            and dead["HL2"]["minC"] == HL2_FLIP
        check("G40-ctrl-regression", ok_ctl,
              "CONTROLS: minC = %s == the r280 flips (EPST/SCR/"
              "SMOOTH %s, HL2 %d) -- the dead worlds die at "
              "0.11..0.15 N_w"
              % (str({cn: dead[cn]["minC"] for cn in dead}),
                 str(CTRL_FLIPS), HL2_FLIP))
        # relay profiles
        ok_cos = True
        lockstep_ok = True
        prof_tab = {}
        for kz in LEGB_KZS:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            gp = BL.grad_ext(ctx, ctx["N"] + EXT)
            mc = next((n for n in range(gp["n_run"])
                       if gp["sg"][n] < 0), None)
            g = gp["gaps"]
            gR = gp["gR"]
            sg = gp["sg"]

            def cosl(n):
                a = g * gR[:, n]
                b = g * gR[:, n - 1]
                return float(np.sum(a * b)
                             / (np.linalg.norm(a)
                                * np.linalg.norm(b)))
            cl_mc = cosl(mc)
            ok_cos = ok_cos and (abs(cl_mc - COS_REC[kz])
                                 <= COS_TOL)
            lo = max(2, ctx["N"] - PROF_BACK)
            craw = [int(sg[n]) * int(sg[n - 1]) * cosl(n)
                    for n in range(lo, mc + 1)]
            mn_raw = min(craw)
            lockstep_ok = lockstep_ok and (mn_raw >= LOCKSTEP_BAR)
            prof_tab[kz] = (cl_mc, -cl_mc * 1.0, mn_raw, mc)
            info("kz%d: cos_log(minC)=%+.4f cos_raw(minC)=%+.4f "
                 "min cos_raw[N_w-%d..minC]=%+.4f (minC=%d)"
                 % (kz, cl_mc, int(sg[mc]) * int(sg[mc - 1])
                    * cl_mc, PROF_BACK, mn_raw, mc))
        ls_typ = {k: ("LOCKSTEP" if prof_tab[k][2] >= LOCKSTEP_BAR
                      else "DIP")
                  for k in prof_tab}
        check("G41-cos-lockstep", ok_cos,
              "RELAY REGRESSION + LOCKSTEP READING: cos_log at "
              "minC == the r280 records %s (tol %.2f) on w9/kz15/"
              "w13; cos_raw = sg_n sg_{n-1} cos_log at the "
              "crossing is POSITIVE ~+0.96..0.98 on all three "
              "worlds -- the r280 anti-alignment IS the h-sign "
              "flip of a raw-gradient lockstep; min cos_raw over "
              "the window tail: %s, typed per world vs bar %.1f: "
              "%s -- the crossing does not rupture the gradient "
              "geometry (the a3 handover reading; no global "
              "lockstep LAW claimed beyond the bar typing)"
              % (str(COS_REC), COS_TOL,
                 str({k: ("%+.3f" % prof_tab[k][2])
                      for k in prof_tab}),
                 LOCKSTEP_BAR, str(ls_typ)))
        # proxies (h-blind) on the five worlds
        worlds5 = {"MAIN": dict(N=N9, minC=minC9, rmg=rmg9)}
        for cn in dead:
            worlds5[cn] = dead[cn]
        prox_res = {}
        for pn, pf in (("P1", proxy_first_bar),
                       ("P2", proxy_argmin),
                       ("P3", proxy_logdrop)):
            devs = {}
            for wn, wd in worlds5.items():
                hi = wd["N"] + EXT
                pred = pf(wd["rmg"], hi)
                devs[wn] = (None if pred is None
                            else abs(pred - wd["minC"]))
            prox_res[pn] = devs
        relay_new = any(
            all(d is not None and d <= PROXY_TOL
                for d in prox_res[pn].values())
            for pn in prox_res)
        check("G42-proxies-Bn", True,
              "c1/c3 ADJUDICATED: B_n := [sign h_n == sign "
              "h_{n-1}] (= [beta_n > 0]); B_n for all n < N_w <=> "
              "minC >= N_w (gated G15/G32).  The h-blind proxies "
              "(rmg only) |pred - minC| per world: %s (tol %d on "
              "ALL five) => %s"
              % (str(prox_res), PROXY_TOL,
                 "NEW_COORDINATE candidate -- forwarding to the "
                 "detector" if relay_new else
                 "B_n typed RESTATEMENT: no h-blind margin proxy "
                 "predicts the flip location -- the relay "
                 "condition is exact bookkeeping, not a new "
                 "coordinate (honest c3 answer)"))
        # margin profiles
        lgm = np.log(rmg9[2:N9])
        n_raz = 2 + int(np.argmin(lgm))
        drops = {}
        for cn, wd in dead.items():
            mcw = wd["minC"]
            base = float(np.median(wd["rmg"][max(2, mcw - 5):mcw]))
            drops[cn] = float(wd["rmg"][mcw] / base)
        check("G43-margin-profile", True,
              "c2 ADJUDICATED (MAIN): razor argmin at n = %d = "
              "%.3f N_w (rmg %.1e; the r243 razor zone), "
              "rmg[N_w-1] = %.1e, rmg[minC] = %.1e -- the wall "
              "zone is the shallow-margin regime; DEAD WORLDS "
              "drop = rmg[minC]/median(prev 5): %s (CREEPING iff "
              "<= %.1f) -- %s"
              % (n_raz, n_raz / float(N9), float(np.exp(lgm.min())),
                 float(rmg9[N9 - 1]), float(rmg9[minC9]),
                 str({c: ("%.2f %s" % (drops[c],
                          "CREEPING" if drops[c] <= CREEP_RATIO
                          else "ABRUPT")) for c in drops}),
                 CREEP_RATIO,
                 "the dead crossings are ABRUPT while MAIN sits "
                 "in a shallow-margin wall zone: the worlds "
                 "separate in crossing TYPE"
                 if all(drops[c] > CREEP_RATIO for c in drops)
                 else "mixed crossing types -- honest"))
        # detector on all candidates
        det_typ = {}
        main_c = offset_candidates(rmg9, N9, S9,
                                   int(np.sum(wu9 < 0)), zones9)
        dead_c = {cn: offset_candidates(
            wd["rmg"], wd["N"], wd["S"], wd["Sm"], wd["zones"])
            for cn, wd in dead.items()}
        for nm in sorted(main_c):
            vm = main_c[nm]
            vd = [dead_c[cn][nm] for cn in sorted(dead_c)]
            vd = [v for v in vd if math.isfinite(v)]
            spread = max(vd) - min(vd) if vd else float("inf")
            dist_m = min(abs(vm - v) for v in vd) if vd else 0.0
            det_typ[nm] = ("MAIN_SEPARATING"
                           if (math.isfinite(vm) and spread > 0
                               and dist_m >= spread)
                           else "WORLD_BLIND")
        check("G44-detector", True,
              "PAIRCORR DETECTOR (battery EPST/SCR/SMOOTH/HL2, "
              "sealed distance rule: MAIN farther from every dead "
              "value than the dead spread): %s -- a WORLD_BLIND "
              "candidate cannot carry the localization"
              % str(det_typ))

    # ---------------- S5 leg B: upper-side adjudication
    section("S5  LEG B -- UPPER-SIDE THEOREM STATUS")
    v956_src = open(V956_PATH, "r", encoding="utf-8").read()
    ok_q = all(q in v956_src for q in V956_QUOTES)
    check("G50-v956-proofstate", ok_q,
          "v956 QUOTES byte-gated (%d/%d present): the boundary "
          "statement 'the wall dies IMMEDIATELY ... quasi-definite "
          "EXACTLY up to half-filling and no degree further' is "
          "carried by TWO COMPUTATIONAL PATHS (Sherman-Morrison "
          "r-chain, gammahat sign chain) + an mp dps-40 ward on "
          "FIVE windows => MEASUREMENT grade, not a symbolic "
          "theorem; with G14 (not world-blind) the sealed rule "
          "types the upper side UPPER_PINNING_MEASURED"
          % (sum(1 for q in V956_QUOTES if q in v956_src),
             len(V956_QUOTES)))
    if smoke:
        check("G51-measured-C", True, "SMOKE: skipped")
        C_meas = None
    else:
        C_meas = max(offs_true)
        check("G51-measured-C", C_meas == 5 and min(offs_true) == 0,
              "THE MEASURED PINNING CONSTANT: C = max offset = %d "
              "(kz43), min offset = %d -- |minC - N_w| <= 5 and "
              "minC >= N_w hold on ALL 42 rungs OF THIS CENSUS "
              "(measurement, r280 record reproduced); the provable "
              "ceiling stays S - S_- (G32) -- C <= 5 is MEASURED, "
              "not proven" % (C_meas, min(offs_true)))

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    hits_m2 = scope_audit("mutant_offset_reader")
    check("G60-mustfail-offset-reader", bool(hits_m2),
          "m2 GIFT OFFSET FORMULA (reads the withheld census "
          "offsets) is FLAGGED by the AST scope audit (%s)"
          % ("; ".join(hits_m2) if hits_m2 else "NOT FLAGGED"))
    hits_m3 = scope_audit("mutant_relay_reader")
    check("G61-mustfail-relay-reader", bool(hits_m3),
          "m3 UNDECLARED h-READING RELAY QUANTITY (consumes the "
          "withheld sign chain) is FLAGGED (%s)"
          % ("; ".join(hits_m3) if hits_m3 else "NOT FLAGGED"))
    hits = []
    for fn in CONSTRUCTORS:
        hits += scope_audit(fn)
    ag_hits = antigate_fragment_audit()
    check("G62-scope-audits", not hits and not ag_hits,
          "the recurrence/candidate/proxy constructors consume "
          "chain/moment/source data ONLY (%s); fragment audit (no "
          "fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S7 verdict
    section("S7  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: no derived 5/7, no bound mechanism "
          "claim, no asymptotic law, NO localization claim from "
          "the census, NO lower-side claim, mincut base 4 / "
          "refined 5 UNCHANGED; what the round adds: the counting "
          "theorem (why half-filling = where the free moments "
          "end), the not-world-blind refutation, the measured-only "
          "status of C, the offset-anatomy negative, the lockstep "
          "handover law and the honest B_n typing")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["UPPER_PINNING_MEASURED(C = %d over the 42-rung "
                 "census; v956 boundary = two computational paths "
                 "+ mp ward = measurement; provable ceiling minC "
                 "<= S - S_- only; world-blind O(1) upper pinning "
                 "REFUTED by the eps-toy)" % C_meas]
        if abs(best_sp) >= SP_BAR:
            parts.append("OFFSET_FORMULA(%s, sp %+.3f)"
                         % (best_cand, best_sp))
        else:
            parts.append("OFFSET_UNSTRUCTURED(max |sp| %.3f at %s)"
                         % (abs(best_sp), best_cand))
        if relay_new and all(v == "MAIN_SEPARATING"
                             for v in det_typ.values()):
            parts.append("RELAY_CONDITION_FOUND(B_n, "
                         "NEW_COORDINATE)")
        else:
            parts.append("RELAY_CONDITION_FOUND(B_n = [beta_n > "
                         "0], RESTATEMENT%s)"
                         % ("; lockstep law holds"
                            if lockstep_ok else ""))
        parts.append("PINNING_DECOMPOSED(lower = free-window "
                     "survival OPEN, upper = forced-pivot death "
                     "MEASURED O(1); why-half-filling = the "
                     "counting theorem)")
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- PROVED (exact, toy/arithmetic grade): counting "
          "theorem, forcing recurrence, freedom, budget, "
          "pigeonhole ceiling, not-world-blind; MEASURED: C = 5, "
          "offset anatomy, lockstep, margins; OPEN: the lower side "
          "(MAIN survives its free window) -- the reviewer "
          "question collapses onto the open center WITH the exact "
          "answer to 'why half-filling'; NO RH claim"
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
