#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""simple_principle_probe -- PRIME.BIGPICTURE.SIMPLE.PRINCIPLE.02

FROZEN SPEC v1 (2026-08-14).  EXPLORATION ONLY, experiments/ only.
NO RH CLAIM in any direction.  Nothing here is load-bearing, nothing is
promoted, no marker moves, no gate of the campaign DAG is closed or
narrowed.  This probe writes no files and imports no earlier probe.

=======================================================================
MANDATE
=======================================================================
Owner directive: "geh in die Vogelperspektive.  Wenn TFPT die Realitaet
beschreibt, sollte sich das einfache Prinzip durchziehen.  Ihr denkt zu
kompliziert."  Task: formulate the ONE simple principle that threads
through everything the corpus has machine-checked, derive from each
candidate reading a PRE-REGISTERED testable consequence with a frozen
pass/fail bar, test it, and type the outcome PRINCIPLE-CONFIRMED /
PATTERN-ONLY / REFUTED under the FOLDCOV standard (CCCLI -> CCCLV): a
principle that only re-describes known facts is PATTERN-ONLY; a
principle that overclaims dies at the gate.

=======================================================================
THE FOUR CANDIDATE READINGS (one sentence each) AND THEIR FROZEN TESTS
=======================================================================
S1  ONE-AXIOM READING.  "TFPT has exactly one positivity axiom, and the
    physics-side positivity certificates (RP/CAR/KMS) and the
    arithmetic wall scalar are THE SAME FUNCTIONAL under the compiler
    dictionary -- equal after normalization, not analogous."
    Pre-registered consequence (strong form): if the equality is more
    than a renaming, the mu4-KMS parent's own normalization must pin at
    least one arithmetic constant that is otherwise DECLARED.  The
    sharpest such constant in the corpus is the archimedean additive
    constant log(pi) (round CCXXXVII: "-log pi bleibt eine DEKLARIERTE
    UV-(Frullani-)Normierung und emergiert NICHT").  Frozen candidate
    list of natural mu4/KMS normalizations, computed exactly:
      N1 = -zeta'(0) of the (+i) mu4 sector spectrum {a_k = 2(k+1/4)}
      N2 = -zeta'(0) of both mu4 sectors {2(k+1/4)} u {2(k+3/4)}
      N3 = log beta_KMS = log(2 pi)
      N4 = (1/2) log(2 pi)      (GNS square-root normalization)
      N5 = N2 - N1              (sector asymmetry)
    HIT bar: |N_i - log pi| <= 1e-20 for some i (dps 50; a true
    identity would sit ~1e-45).  Ward S1a (the equality that DOES hold,
    difference level; round CCXXXVII reproduced): for a_k = 2(k+1/4),
      2 sum_k [a_k/(a_k^2+t0^2) - a_k/(a_k^2+t^2)]
        == Re psi(1/4+it/2) - Re psi(1/4+it0/2)
    at t0 = 6, t in {14.3, 25, 40}, rel <= 1e-12.
    Typing rule (frozen): 0 hits => S1-STRONG-REFUTED; the weak form
    ("emptiness is the prediction") retrodicts PARENT-REALIZABLE-EMPTY
    / HAYNSWORTH-EMPTY and is typed PATTERN-ONLY.  >= 1 hit =>
    S1-PINS-NEW-DIGIT (would be a genuine discovery).

S2  TRANSCRIPTION READING.  "The compiler is an exact transcriber:
    every claimed arithmetic output of the corpus is an exact function
    of compiler-internal integers or a classical theorem restated --
    TFPT adds no arithmetic digit beyond its axioms."
    Pre-registered consequence: the three sharpest claimed arithmetic
    outputs each type TRANSCRIPTION under the frozen criterion; a
    single PREDICTION-typed outcome REFUTES S2.
    Criterion (frozen): PREDICTION iff the output fixes >= 1 digit of
    an arithmetic quantity that is neither an explicit input nor an
    exact function of the inputs via classical identities.
    T1 register head: prod_{p|210}(1-1/p) == 48/210 EXACT (Fraction),
       i.e. the claimed register information head 2.1293 bit (note
       XCIX) == log2(210/48) == log2(35/8), dev <= 5e-5 vs the printed
       2.1293 and <= 1e-12 vs log2(35/8); the forcing census (note
       LXXVIII): {2,3,5,7} is the UNIQUE quadruple of distinct primes
       p <= 49 with prod(p-1) = 48; counterfactual inputs 24 -> empty,
       96 -> {2,3,5,13} only.  Output = exact function of the compiler
       pair (Omega_adm, N) => TRANSCRIPTION.
    T2 Mertens reach: exact -log2 prod_{p<=z}(1-1/p) at z = 1e2..1e6
       vs the corpus prints 3.055/3.627/4.038/4.358/4.621 (abs <=
       2e-3) and vs log2(e^gamma log z) rel <= 2% for z >= 1e4 (the
       corpus's own ward).  Mertens 1874 => TRANSCRIPTION.
    T3 the E''(0) pin (round CCCLXXXII): sum_rho 1/(rho(1-rho)) =
       2 + gamma - log(4 pi).  Zero-side: sum_{gamma>0} 2/(1/4+gamma^2)
       over the 7000-cache plus the RvM tail integral
       (1/pi)(log(T/2pi)+1)/T; |sum + tail - target| <= 1e-4.
       Classical Hadamard-product identity consumed by the corpus as a
       repair input => TRANSCRIPTION.
    Typing rule (frozen): 3/3 TRANSCRIPTION => S2-TRANSCRIPTION-
    CONFIRMED (the reading survived falsification and forbids any
    future compiler-derived arithmetic prediction); any PREDICTION =>
    S2-REFUTED.

S3  FIXED-POINT READING.  "The theory is about fixed points of a
    compression, and the RH seat is the statement that the arithmetic
    seam (the zero measure) is a fixed point of the same compression
    that fixes E8 on the finite side."
    Pre-registered consequence: if the seat is a fixed-point statement
    WITH CONTENT, the compression T (measure -> zeros of the extremal
    minimizer of its evaluation Gram) must CONTRACT toward the true
    measure from a perturbed admissible measure; if T transcribes
    (fixes EVERY fed measure), the fixed-point property carries zero
    seat information and the reading is refuted as a seat principle.
    Instrument (declared): node-Gram extremal channel at x = 5,
    a = log(5)/2, K = ceil(1.25 x log x) = 11 unnormalized basis
    functions B_j(t) = sin(a(t-om_j))/(t-om_j) + sin(a(t+om_j))/(t+om_j),
    om_j = j pi / a, Gram M = 2 sum_{i<2000} B(g_i) B(g_i)^T over the
    first 2000 certified ordinates (X5-typed READ-ONLY cache;
    truncation declared -- the licence is the Z1 identity of round
    CCCLXXXIII: the Galerkin matrix IS this Gram plus tail).  mp dps 60.
    Plants: jitter nodes gamma_1..gamma_6 by signs (+,-,+,-,+,-)*delta,
    delta in {0.1, 0.4}.  Distances: RMS nearest-match on the inner
    band (5, 35) against nodes gamma_1..gamma_5.
    Frozen bars: d_back = d(zeros(T mu_jit), true nodes), d_fed =
    d(zeros(T mu_jit), jittered nodes).  CONTRACTS iff d_back <=
    0.5*delta on 2/2; TRANSCRIBES iff d_fed <= 0.25*delta AND d_back >=
    0.75*delta on 2/2; else MIXED.  Instrument gates: census in (0,30)
    == 3 and baseline tracking RMS <= 0.1, else INSTRUMENT-EDGE.
    Typing rule (frozen): TRANSCRIBES => S3-REFUTED (every admissible
    measure is a fixed point; the reading collapses onto Z1
    transcription and says nothing about the seat).  CONTRACTS =>
    S3-CONFIRMED (a genuinely new handle).

S4  GRAM-SEAT SQUARE LAW (this probe's own reading).  "Every
    load-bearing positivity in TFPT is Gram positivity of node
    evaluations -- a theorem exactly where the nodes are compiler data
    -- and the RH seat is node REALITY itself; therefore every compiler
    instrument prices an off-line node by ONE square law, threshold
    delta_* = sqrt(margin/curvature), while pricing on-line
    MISALIGNMENT at first order: the seat sits one order deeper than
    alignment."
    Pre-registered consequences (frozen):
    (a) on two structurally different instruments whose margins differ
        by >= 4 orders -- channel A = the node-Gram extremal channel at
        x = 5 (margin lam_min(M_dbl), curvature c_A = 4 E_v'(gamma_1)^2,
        multiplicity-preserving double -> off-line-quartet plant at
        gamma_1) and channel B = the linear tent-window Weil functional
        Q = 2 sum_gamma Fhat(gamma), Fhat(t) = A*(sin(At/2)/(At/2))^2,
        A = 3, with the count-preserving merge plant at gamma* = 10 pi
        (the lobe minimum: Fhat(gamma*) = 0, Fhat''(gamma*) > 0; the
        two flanking cache ordinates merge into the quartet
        gamma* +- i delta; margin_B = Q + V(0), curvature c_B =
        2 Fhat''(gamma*)) -- the measured crossing delta_meas must
        match the parameter-free prediction delta_pred =
        sqrt(margin/curvature) within ratio band [1/3, 3], and the
        sub-crossing response must be quadratic: log-log slope in
        [1.85, 2.15] on the grid {0.02, 0.05, 0.1}*delta_pred
        (grid frozen as a RULE scaled by the predicted crossing).
    (b) ORDER SPLIT: on channel B, an on-line jitter of the first 200
        nodes with frozen signs (-1)^i and eps in {0.01, 0.02, 0.05}
        must respond at first order: slope in [0.7, 1.3].
    Typing rule (frozen, FOLDCOV standard): even if (a) and (b) both
    pass, the square law follows from the Gram form by second-order
    perturbation theory, i.e. it re-describes the structure that S2
    already carries => S4 is typed PATTERN-ONLY-EVEN-IF-CONFIRMED,
    with the measured law and the order split reported as the
    campaign-relevant content (why 24 first-order sign-source
    candidates failed; seat precision = sqrt(instrument margin) up to
    curvature, hence the ~1% of MIN-U2 is instrument-margin-specific,
    not universal).  Slope failure on channel A => S4-REFUTED.
    Channel B leaving the ratio band while its small-delta slope
    passes => SQUARELAW-LOCAL-ONLY (the law holds only near
    saturation), reported as such.

=======================================================================
FROZEN CONSTANTS
=======================================================================
X_CELL = 5, A_TYPE = log(5)/2, K_BASIS = 11, N_GRAM = 2000, DPS_A = 60,
DPS_B = 30, DPS_S1 = 50; census scan (0.2, 42) step 0.02, census band
(0, 30), tracking nodes gamma_1..gamma_5, inner match band (5, 35);
jitter signs (+,-,+,-,+,-), deltas {0.1, 0.4}; tent A = 3, gamma* =
10 pi, jitter-nodes 200, eps {0.01, 0.02, 0.05}; slope grid factors
{0.02, 0.05, 0.1}; ratio band [1/3, 3]; slope band A/B-off [1.85, 2.15],
B-jit [0.7, 1.3]; margin separation bar 1e4; cache =
verified_zeros_n7000.npy (X5-typed, READ-ONLY, certified per meta);
runtime bar 1800 s.  All gates counted; exit 0 iff all gates pass.

FIREWALL: AST self-scan bans zetazero/zetazeros/nzeros/primepi/
primerange/isprime/nextprime/factorint; the only zero data is the
declared cache; no verification/ import; no file writes.

DISCLOSURE: component smokes (S1a identity, one Gram column, one
census scan) were run while building; no bar and no gate direction was
moved after seeing a frozen-run number.  AMENDMENT A1 (disclosed): the
first full run (log kept as simple_principle_probe_run1.log) passed
21/22 with the single failure at the INSTRUMENT gate G04 -- mp.diff's
finite-difference step cannot reach the 1e-30 stability bar (measured
6.68e-11, twenty orders above any candidate gap, no verdict touched);
fixed by computing d/ds [2^-s zeta_H(s,a)] structurally via the product
rule with mpmath's exact Hurwitz s-derivative mp.zeta(s, a, 1).  The
bar is unchanged; no gate direction moved in favor of any outcome.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
from mpmath import mp, mpf, mpc

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

_HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")

# ---- frozen constants -------------------------------------------------
X_CELL = 5
K_BASIS = 11
N_GRAM = 2000
DPS_A = 60
DPS_B = 30
DPS_S1 = 50
SCAN_LO, SCAN_HI, SCAN_STEP = 0.2, 42.0, 0.02
CENSUS_HI = 30.0
TRACK_BAND = (5.0, 35.0)
N_TRACK_NODES = 5
JIT_SIGNS = (+1, -1, +1, -1, +1, -1)
JIT_DELTAS = (0.1, 0.4)
TENT_A = 3
GSTAR_FACTOR = 10          # gamma* = 10 pi
N_JIT_NODES = 200
EPS_JIT = (0.01, 0.02, 0.05)
SLOPE_GRID = (0.02, 0.05, 0.1)
RATIO_BAND = (1.0 / 3.0, 3.0)
SLOPE_BAND = (1.85, 2.15)
SLOPE_BAND_JIT = (0.7, 1.3)
MARGIN_SEP_BAR = 1.0e4
RUNTIME_BAR = 1800.0
GAMMA1_REF = 14.134725141734695

AST_BANNED = {"zetazero", "zetazeros", "nzeros", "primepi",
              "primerange", "isprime", "nextprime", "factorint"}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""), flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def lsq_slope(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx)
    mx = sum(lx) / n
    my = sum(ly) / n
    num = sum((a - mx) * (b - my) for a, b in zip(lx, ly))
    den = sum((a - mx) ** 2 for a in lx)
    return num / den


# =======================================================================
# S0  firewall + cache
# =======================================================================

def s0_firewall_and_cache():
    section("S0  FIREWALL + CERTIFIED-ORDINATE CACHE (X5-typed, READ-ONLY)")
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else "")
            if name.lower() in AST_BANNED:
                hits.append(name)
    check("G01 AST-FIREWALL", not hits, "banned calls: %s" % (hits or "none"))

    gam = np.load(CACHE_NPY)
    ok = (gam.shape[0] == 7000
          and bool(np.all(np.diff(gam) > 0))
          and abs(float(gam[0]) - GAMMA1_REF) < 1e-8)
    check("G02 CACHE-WARD", ok,
          "n=%d monotone gamma_1 dev %.2e gamma_N %.4f"
          % (gam.shape[0], abs(float(gam[0]) - GAMMA1_REF), float(gam[-1])))
    return [float(g) for g in gam]


# =======================================================================
# S1  one-axiom reading
# =======================================================================

def s1_one_axiom():
    section("S1  ONE-AXIOM READING -- does the mu4-KMS normalization pin "
            "log pi?")
    mp.dps = DPS_S1

    # S1a difference-level dictionary (exact, reproduces CCXXXVII)
    t0 = mpf("6")
    worst = mpf(0)
    for tt in ("14.3", "25", "40"):
        t = mpf(tt)

        def term(k):
            a = 2 * (k + mpf(1) / 4)
            return a / (a * a + t0 * t0) - a / (a * a + t * t)

        lhs = 2 * mp.nsum(term, [0, mp.inf])
        rhs = (mp.digamma(mpc(mpf(1) / 4, t / 2)).real
               - mp.digamma(mpc(mpf(1) / 4, t0 / 2)).real)
        rel = abs(lhs - rhs) / abs(rhs)
        worst = max(worst, rel)
        print("    t0=6 t=%-5s  lhs %s  rhs %s  rel %s"
              % (tt, mp.nstr(lhs, 15), mp.nstr(rhs, 15), mp.nstr(rel, 3)))
    check("G03 S1-DIFF-DICT", worst < mpf("1e-12"),
          "worst rel %s (bar 1e-12) -- the physics/arithmetic equality is "
          "EXACT on differences" % mp.nstr(worst, 3))

    # S1b zeta-regularized normalization census vs log pi
    # d/ds [2^-s zeta_H(s,a)] at s=0 = -log2 * zeta_H(0,a) + zeta_H'(0,a)
    # (product rule; mp.zeta(s, a, 1) is the exact Hurwitz s-derivative)
    def zreg_neg_zprime0(alphas):
        tot = mpf(0)
        for a in alphas:
            tot += -mp.log(2) * mp.zeta(mpf(0), a) + mp.zeta(mpf(0), a, 1)
        return -tot

    mp.dps = 60
    n1_hi = zreg_neg_zprime0([mpf(1) / 4])
    n2_hi = zreg_neg_zprime0([mpf(1) / 4, mpf(3) / 4])
    mp.dps = 40
    n1_lo = zreg_neg_zprime0([mpf(1) / 4])
    n2_lo = zreg_neg_zprime0([mpf(1) / 4, mpf(3) / 4])
    mp.dps = DPS_S1
    stab = max(abs(n1_hi - n1_lo), abs(n2_hi - n2_lo))
    check("G04 S1-NREG-STABLE", stab < mpf("1e-30"),
          "dps-40/60 agreement %s (bar 1e-30)" % mp.nstr(stab, 3))

    cands = {
        "N1 -zeta'(0) (+i)-sector": n1_hi,
        "N2 -zeta'(0) both sectors": n2_hi,
        "N3 log(2 pi)  [beta_KMS]": mp.log(2 * mp.pi),
        "N4 (1/2) log(2 pi) [GNS]": mp.log(2 * mp.pi) / 2,
        "N5 N2 - N1": n2_hi - n1_hi,
    }
    target = mp.log(mp.pi)
    hits = 0
    print("    target log(pi) = %s" % mp.nstr(target, 25))
    for name, val in cands.items():
        gap = abs(val - target)
        hit = gap < mpf("1e-20")
        hits += int(hit)
        print("    %-28s = %-28s |gap| = %s%s"
              % (name, mp.nstr(val, 20), mp.nstr(gap, 4),
                 "  <-- HIT" if hit else ""))
    check("G05 S1-CENSUS-DONE", all(mp.isfinite(v) for v in cands.values()),
          "5 candidates computed; hits vs log pi: %d" % hits)

    verdict = "S1-PINS-NEW-DIGIT" if hits else "S1-STRONG-REFUTED"
    print("  S1 verdict: %s (weak form 'emptiness is the prediction' is a "
          "retrodiction of PARENT-REALIZABLE-EMPTY -> PATTERN-ONLY)"
          % verdict)
    return verdict


# =======================================================================
# S2  transcription reading
# =======================================================================

def sieve_primes(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if flags[p]:
            flags[p * p::p] = bytearray(len(flags[p * p::p]))
    return [i for i in range(2, limit + 1) if flags[i]]


def s2_transcription(gam):
    section("S2  TRANSCRIPTION READING -- the three sharpest claimed "
            "arithmetic outputs, typed")
    types = {}

    # T1 register head + forcing census
    prod = Fraction(1)
    for p in (2, 3, 5, 7):
        prod *= Fraction(p - 1, p)
    head = -math.log2(float(prod))
    ref = math.log2(35.0 / 8.0)
    ok1 = (prod == Fraction(48, 210) and abs(head - ref) < 1e-12
           and abs(head - 2.1293) < 5e-5)
    check("G06 S2-T1-HEAD-EXACT", ok1,
          "prod(1-1/p) = %s == 48/210; head %.10f bit == log2(35/8) "
          "(claimed 2.1293) -- exact function of (Omega_adm, N)"
          % (prod, head))

    small_primes = sieve_primes(49)
    from itertools import combinations
    census = {}
    for target in (24, 48, 96):
        sols = [q for q in combinations(small_primes, 4)
                if (q[0] - 1) * (q[1] - 1) * (q[2] - 1) * (q[3] - 1) == target]
        census[target] = sols
    ok2 = (census[48] == [(2, 3, 5, 7)] and census[24] == []
           and census[96] == [(2, 3, 5, 13)])
    check("G07 S2-T1-FORCING", ok2,
          "prod(p-1)=48 -> %s unique; 24 -> %s; 96 -> %s (classical census, "
          "input 48 -> output 210)" % (census[48], census[24], census[96]))
    types["T1 register-head"] = "TRANSCRIPTION" if (ok1 and ok2) else \
        "PREDICTION"

    # T2 Mertens reach
    primes = sieve_primes(1_000_000)
    corpus_heads = {100: 3.055, 1000: 3.627, 10_000: 4.038,
                    100_000: 4.358, 1_000_000: 4.621}
    zs = sorted(corpus_heads)
    heads = {}
    acc = 0.0
    zi = 0
    for p in primes:
        while zi < len(zs) and p > zs[zi]:
            heads[zs[zi]] = acc
            zi += 1
        acc += -math.log2(1.0 - 1.0 / p)
    while zi < len(zs):
        heads[zs[zi]] = acc
        zi += 1
    egamma = math.exp(0.5772156649015329)
    ok_t2 = True
    for z in zs:
        mert = math.log2(egamma * math.log(z))
        rel = abs(heads[z] - mert) / heads[z]
        okz = abs(heads[z] - corpus_heads[z]) <= 2e-3 and (
            z < 1e4 or rel <= 0.02)
        ok_t2 &= okz
        print("    z=%-8d head %.4f bit (corpus %.3f)  mertens %.4f  "
              "rel %.4f  register share %.1f%%"
              % (z, heads[z], corpus_heads[z], mert, rel,
                 100.0 * (-math.log2(48.0 / 210.0)) / heads[z]))
    check("G08 S2-T2-MERTENS", ok_t2,
          "heads match corpus prints <= 2e-3 and Mertens 1874 <= 2%% for "
          "z >= 1e4 -- classical throughout")
    types["T2 mertens-reach"] = "TRANSCRIPTION" if ok_t2 else "PREDICTION"

    # T3 the E''(0) pin
    ssum = sum(2.0 / (0.25 + g * g) for g in gam)
    T = gam[-1]
    tail = (1.0 / math.pi) * (math.log(T / (2 * math.pi)) + 1.0) / T
    target = 2.0 + 0.5772156649015329 - math.log(4 * math.pi)
    dev = abs(ssum + tail - target)
    check("G09 S2-T3-PIN", dev <= 1e-4,
          "sum_rho 1/(rho(1-rho)): cache %.9f + tail %.3e = %.9f vs "
          "2+gamma-log(4pi) = %.9f, dev %.2e (Hadamard, classical)"
          % (ssum, tail, ssum + tail, target, dev))
    types["T3 E''(0)-pin"] = "TRANSCRIPTION" if dev <= 1e-4 else "PREDICTION"

    n_tr = sum(1 for v in types.values() if v == "TRANSCRIPTION")
    verdict = ("S2-TRANSCRIPTION-CONFIRMED-3/3" if n_tr == 3
               else "S2-PREDICTION-FOUND")
    print("  S2 typing: %s" % types)
    print("  S2 verdict: %s" % verdict)
    return verdict


# =======================================================================
# channel A instrument (node-Gram extremal channel at x = 5)
# =======================================================================

class GramChannel:
    def __init__(self, gam):
        mp.dps = DPS_A
        self.a = mp.log(X_CELL) / 2
        self.oms = [j * mp.pi / self.a for j in range(K_BASIS)]
        self.nodes = gam[:N_GRAM]
        self.M = self._gram(self.nodes)

    def bvec(self, t):
        a = self.a
        out = []
        for om in self.oms:
            d1 = t - om
            d2 = t + om
            s1 = mp.sin(a * d1) / d1 if abs(d1) > mpf("1e-40") else a
            s2 = mp.sin(a * d2) / d2 if abs(d2) > mpf("1e-40") else a
            out.append(s1 + s2)
        return out

    def _rank1(self, M, u, w):
        for j in range(K_BASIS):
            for k in range(j, K_BASIS):
                v = w * u[j] * u[k]
                M[j, k] += v
                if k != j:
                    M[k, j] += v
        return M

    def _gram(self, nodes):
        M = mp.zeros(K_BASIS, K_BASIS)
        for g in nodes:
            self._rank1(M, self.bvec(mpf(g)), mpf(2))
        return M

    def jittered(self, deltas_by_index):
        M = self.M.copy()
        for idx, d in deltas_by_index.items():
            g_old = mpf(self.nodes[idx])
            self._rank1(M, self.bvec(g_old), mpf(-2))
            self._rank1(M, self.bvec(g_old + d), mpf(2))
        return M

    @staticmethod
    def eig_min(M):
        E, Q = mp.eigsy(M)
        vals = [E[i] for i in range(K_BASIS)]
        imin = min(range(K_BASIS), key=lambda i: vals[i])
        v = [Q[j, imin] for j in range(K_BASIS)]
        return vals[imin], v

    def efun(self, v):
        def E(t):
            b = self.bvec(t)
            return mp.fsum(v[j] * b[j] for j in range(K_BASIS))
        return E

    def census(self, v, lo=SCAN_LO, hi=SCAN_HI, step=SCAN_STEP):
        E = self.efun(v)
        zeros = []
        t_prev = mpf(lo)
        f_prev = E(t_prev)
        n = int((hi - lo) / step)
        for i in range(1, n + 1):
            t = mpf(lo) + i * mpf(step)
            f = E(t)
            if f_prev * f < 0:
                aa, bb = t_prev, t
                fa = f_prev
                for _ in range(60):
                    mid = (aa + bb) / 2
                    fm = E(mid)
                    if fa * fm <= 0:
                        bb = mid
                    else:
                        aa, fa = mid, fm
                zeros.append(float((aa + bb) / 2))
            t_prev, f_prev = t, f
        return zeros


def rms_nearest(points, refs):
    vals = []
    for r in refs:
        vals.append(min(abs(r - z) for z in points) ** 2)
    return math.sqrt(sum(vals) / len(vals))


def s3_fixed_point(chan, gam):
    section("S3  FIXED-POINT READING -- does the compression contract "
            "toward the true measure, or transcribe the fed one?")
    lam0, v0 = chan.eig_min(chan.M)
    zeros0 = chan.census(v0)
    in_census = [z for z in zeros0 if 0 < z < CENSUS_HI]
    true_nodes = gam[:N_TRACK_NODES]
    band_zeros0 = [z for z in zeros0 if TRACK_BAND[0] < z < TRACK_BAND[1]]
    d0 = rms_nearest(band_zeros0, true_nodes) if band_zeros0 else float("inf")
    print("    lam_min(M) = %s ; zeros in (0,42): %d ; census (0,30): %d "
          "(truth: 3) ; baseline tracking RMS %.3e"
          % (mp.nstr(lam0, 6), len(zeros0), len(in_census), d0))
    check("G10 S3-CENSUS-3", len(in_census) == 3,
          "census (0,30) = %d, zeros %s" % (len(in_census),
                                            ["%.4f" % z for z in in_census]))
    check("G11 S3-TRACKING", d0 <= 0.1,
          "baseline RMS %.3e (bar 0.1) on nodes gamma_1..gamma_5" % d0)

    results = []
    ok_ran = True
    for delta in JIT_DELTAS:
        dmap = {i: mpf(JIT_SIGNS[i]) * mpf(str(delta)) for i in range(6)}
        Mj = chan.jittered(dmap)
        lamj, vj = chan.eig_min(Mj)
        zj = chan.census(vj)
        band_zj = [z for z in zj if TRACK_BAND[0] < z < TRACK_BAND[1]]
        jit_nodes = [gam[i] + JIT_SIGNS[i] * delta
                     for i in range(N_TRACK_NODES)]
        d_fed = rms_nearest(band_zj, jit_nodes) if band_zj else float("inf")
        d_back = rms_nearest(band_zj, true_nodes) if band_zj else float("inf")
        ok_ran &= math.isfinite(d_fed) and math.isfinite(d_back)
        results.append((delta, d_fed, d_back))
        print("    delta %.2f : lam_min %s  d_fed %.4e (%.2f*delta)  "
              "d_back %.4e (%.2f*delta)"
              % (delta, mp.nstr(lamj, 4), d_fed, d_fed / delta,
                 d_back, d_back / delta))
    check("G12 S3-PLANTS-RAN", ok_ran, "both jitter censuses complete")

    contracts = all(db <= 0.5 * d for d, _, db in results)
    transcribes = all(df <= 0.25 * d and db >= 0.75 * d
                      for d, df, db in results)
    if len(in_census) != 3 or d0 > 0.1:
        verdict = "S3-INSTRUMENT-EDGE"
    elif contracts:
        verdict = "S3-CONTRACTS"
    elif transcribes:
        verdict = "S3-TRANSCRIBES"
    else:
        verdict = "S3-MIXED"
    print("  S3 verdict: %s" % verdict)
    return verdict


# =======================================================================
# S4  square law + order split
# =======================================================================

def s4_channel_a(chan, gam):
    section("S4A  GRAM CHANNEL (x = 5): off-line quartet plant at gamma_1, "
            "square-law crossing")
    mp.dps = DPS_A
    g1 = mpf(gam[0])
    b1 = chan.bvec(g1)
    Mdbl = chan._rank1(chan.M.copy(), b1, mpf(2))
    lam, v = chan.eig_min(Mdbl)
    E = chan.efun(v)
    Eg1 = E(g1)
    Ep = mp.diff(E, g1)
    curv = 4 * Ep * Ep
    margin = lam
    dpred = mp.sqrt(margin / curv)
    print("    margin_A = lam_min(M_dbl) = %s" % mp.nstr(margin, 8))
    print("    E_v(gamma_1) = %s ; E_v'(gamma_1) = %s ; curvature c_A = %s"
          % (mp.nstr(Eg1, 4), mp.nstr(Ep, 8), mp.nstr(curv, 8)))
    print("    delta_pred_A = sqrt(margin/curv) = %s" % mp.nstr(dpred, 8))
    check("G13 S4A-PSD", lam > mpf("-1e-40"),
          "node-Gram is structurally PSD (fed on-line nodes only); "
          "lam_min %s" % mp.nstr(lam, 4))

    def lam_off(delta):
        z = mpc(g1, delta)
        u = chan.bvec(z)
        Moff = Mdbl.copy()
        for j in range(K_BASIS):
            for k in range(j, K_BASIS):
                re = (u[j] * u[k]).real
                val = 4 * re - 4 * b1[j] * b1[k]
                Moff[j, k] += val
                if k != j:
                    Moff[k, j] += val
        lmin, _ = chan.eig_min(Moff)
        return lmin

    # slope on the frozen grid
    resp = []
    grid = [mpf(str(f)) * dpred for f in SLOPE_GRID]
    for d in grid:
        r = margin - lam_off(d)
        resp.append(float(r))
        print("    delta = %s : lam_min drop %s" % (mp.nstr(d, 4),
                                                    mp.nstr(r, 6)))
    slope = lsq_slope([float(d) for d in grid], resp)
    check("G14 S4A-SLOPE", SLOPE_BAND[0] <= slope <= SLOPE_BAND[1],
          "log-log slope %.4f (band [1.85, 2.15]) -- the -4 delta^2 E'^2 "
          "law" % slope)

    lo, hi = dpred / 10, 10 * dpred
    flo, fhi = lam_off(lo), lam_off(hi)
    if flo <= 0 or fhi >= 0:
        check("G15 S4A-RATIO", False,
              "bisection bracket failed: f(lo) %s f(hi) %s"
              % (mp.nstr(flo, 4), mp.nstr(fhi, 4)))
        return None, float(margin), float(curv), None
    for _ in range(50):
        mid = (lo + hi) / 2
        if lam_off(mid) > 0:
            lo = mid
        else:
            hi = mid
    dmeas = (lo + hi) / 2
    ratio = float(dmeas / dpred)
    check("G15 S4A-RATIO", RATIO_BAND[0] <= ratio <= RATIO_BAND[1],
          "delta_meas %s / delta_pred %s = %.4f (band [1/3, 3])"
          % (mp.nstr(dmeas, 8), mp.nstr(dpred, 8), ratio))
    inv = float(dmeas) * math.sqrt(float(curv) / float(margin))
    print("    cross-channel invariant R_A = delta_meas*sqrt(c/margin) "
          "= %.4f" % inv)
    return float(dmeas), float(margin), float(curv), ratio


def s4_channel_b(gam):
    section("S4B  LINEAR TENT-WINDOW CHANNEL: merge plant at gamma* = 10 pi, "
            "square-law crossing + order split")
    mp.dps = DPS_B
    A = mpf(TENT_A)

    def Fhat(t):
        x = A * t / 2
        return A * (mp.sin(x) / x) ** 2

    gstar = GSTAR_FACTOR * mp.pi
    F_at = Fhat(gstar)
    F2 = mp.diff(Fhat, gstar, 2)
    check("G16 S4B-LOBE", abs(F_at) < mpf("1e-30") and F2 > 0,
          "Fhat(10 pi) = %s, Fhat'' = %s > 0 (lobe minimum)"
          % (mp.nstr(F_at, 3), mp.nstr(F2, 6)))

    Q = 2 * mp.fsum(Fhat(mpf(g)) for g in gam)
    T = mpf(gam[-1])
    env = 2 * (4 / A) * (mp.log(T / (2 * mp.pi)) + 1) / (2 * mp.pi * T) * 2
    check("G17 S4B-QPOS", Q - env > 0,
          "Q = %s, tail envelope %s (Q - env > 0)" % (mp.nstr(Q, 8),
                                                      mp.nstr(env, 3)))

    # flanking ordinates (frozen rule: the two cache nodes nearest gamma*)
    idx = sorted(range(len(gam)), key=lambda i: abs(gam[i] - float(gstar)))
    ga, gb = sorted((gam[idx[0]], gam[idx[1]]))
    print("    merge pair: gamma_a %.6f, gamma_b %.6f -> quartet at "
          "gamma* = %.6f +- i delta" % (ga, gb, float(gstar)))

    def V(delta):
        z = mpc(gstar, delta)
        return (4 * Fhat(z).real - 2 * Fhat(mpf(ga)) - 2 * Fhat(mpf(gb)))

    margin = Q + V(0)
    curv = 2 * F2
    dpred = mp.sqrt(margin / curv)
    print("    margin_B = Q + V(0) = %s ; curvature c_B = 2 Fhat'' = %s ; "
          "delta_pred_B = %s"
          % (mp.nstr(margin, 8), mp.nstr(curv, 6), mp.nstr(dpred, 6)))

    resp = []
    grid = [mpf(str(f)) * dpred for f in SLOPE_GRID]
    for d in grid:
        r = -(V(d) - V(0))
        resp.append(float(r))
        print("    delta = %s : response %s" % (mp.nstr(d, 4),
                                                mp.nstr(r, 6)))
    slope = lsq_slope([float(d) for d in grid], resp)
    check("G18 S4B-SLOPE-OFF", SLOPE_BAND[0] <= slope <= SLOPE_BAND[1],
          "off-line log-log slope %.4f (band [1.85, 2.15])" % slope)

    lo, hi = dpred / 10, 10 * dpred
    ok_br = (Q + V(lo) > 0) and (Q + V(hi) < 0)
    dmeas = None
    ratio = None
    if ok_br:
        for _ in range(60):
            mid = (lo + hi) / 2
            if Q + V(mid) > 0:
                lo = mid
            else:
                hi = mid
        dmeas = float((lo + hi) / 2)
        ratio = dmeas / float(dpred)
    check("G19 S4B-RATIO", ok_br and RATIO_BAND[0] <= ratio <= RATIO_BAND[1],
          "delta_meas %s / delta_pred %s = %s (band [1/3, 3])"
          % (("%.6f" % dmeas) if dmeas else "n/a", mp.nstr(dpred, 6),
             ("%.4f" % ratio) if ratio else "n/a"))
    if dmeas:
        inv = dmeas * math.sqrt(float(curv) / float(margin))
        print("    cross-channel invariant R_B = %.4f" % inv)

    # order split: on-line jitter prices at first order
    nodes = gam[:N_JIT_NODES]
    base = 2 * mp.fsum(Fhat(mpf(g)) for g in nodes)
    jr = []
    for eps in EPS_JIT:
        pert = 2 * mp.fsum(Fhat(mpf(g) + (-1) ** i * mpf(str(eps)))
                           for i, g in enumerate(nodes))
        jr.append(abs(float(pert - base)))
        print("    eps = %.3f : |Delta Q_jit| = %.6e" % (eps, jr[-1]))
    slope_j = lsq_slope(list(EPS_JIT), jr)
    check("G20 S4B-SLOPE-JIT",
          SLOPE_BAND_JIT[0] <= slope_j <= SLOPE_BAND_JIT[1],
          "on-line jitter log-log slope %.4f (band [0.7, 1.3]) -- "
          "ORDER SPLIT: alignment first order, reality second order"
          % slope_j)
    order_split = SLOPE_BAND_JIT[0] <= slope_j <= SLOPE_BAND_JIT[1]
    return dmeas, float(margin), float(curv), ratio, order_split


# =======================================================================
# main
# =======================================================================

def main():
    print("simple_principle_probe -- PRIME.BIGPICTURE.SIMPLE.PRINCIPLE.02")
    print("SPEC_SHA %s" % SPEC_SHA)

    gam = s0_firewall_and_cache()
    v1 = s1_one_axiom()
    v2 = s2_transcription(gam)

    chan = GramChannel(gam)
    v3 = s3_fixed_point(chan, gam)
    dA, mA, cA, ratioA = s4_channel_a(chan, gam)
    dB, mB, cB, ratioB, order_split = s4_channel_b(gam)

    section("VERDICT")
    sep = (mB / mA) if (mA and mA > 0) else float("inf")
    check("G21 MARGIN-SEP", sep >= MARGIN_SEP_BAR,
          "margin_B/margin_A = %.3e (bar 1e4) -- the two channels are "
          "genuinely far apart" % sep)
    rt = time.time() - T0
    check("G22 RUNTIME", rt <= RUNTIME_BAR, "%.1f s (bar %.0f s)"
          % (rt, RUNTIME_BAR))

    okA = ratioA is not None and RATIO_BAND[0] <= ratioA <= RATIO_BAND[1]
    okB = ratioB is not None and RATIO_BAND[0] <= ratioB <= RATIO_BAND[1]
    if okA and okB:
        v4 = "S4-SQUARELAW-BOTH-CHANNELS"
    elif okA and not okB:
        v4 = "S4-SQUARELAW-LOCAL-ONLY"
    else:
        v4 = "S4-SQUARELAW-REFUTED"
    v4 += "+ORDER-SPLIT-MEASURED" if order_split else "+ORDER-SPLIT-ABSENT"

    print("\n  S1 %s" % v1)
    print("  S2 %s" % v2)
    print("  S3 %s" % v3)
    print("  S4 %s" % v4)
    print("\n  FOLDCOV typing (frozen rules):")
    print("    S1 strong REFUTED / weak PATTERN-ONLY"
          if v1 == "S1-STRONG-REFUTED" else "    S1 PRINCIPLE-CONFIRMED (!)")
    print("    S2 %s" % ("PRINCIPLE-CONFIRMED on the trio (falsifiable, "
                         "survived; forbids future compiler-derived "
                         "arithmetic predictions)"
                         if v2.endswith("3/3") else "REFUTED"))
    print("    S3 %s" % ("REFUTED as a seat principle (the compression "
                         "fixes every fed measure)"
                         if v3 == "S3-TRANSCRIBES" else v3))
    print("    S4 PATTERN-ONLY-EVEN-IF-CONFIRMED (second-order perturbation "
          "of the Gram form; measured law + order split reported)")

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\n  GATES %d/%d  runtime %.1f s  SPEC_SHA %s"
          % (n_pass, len(CHECKS), rt, SPEC_SHA[:16]))
    composite = ("SIMPLE-PRINCIPLE-IS-TRANSCRIPTION"
                 if (v1 == "S1-STRONG-REFUTED"
                     and v2.endswith("3/3")
                     and v3 == "S3-TRANSCRIBES")
                 else "SIMPLE-PRINCIPLE-MIXED(%s|%s|%s|%s)"
                 % (v1, v2, v3, v4))
    print("  COMPOSITE VERDICT: %s" % composite)
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
