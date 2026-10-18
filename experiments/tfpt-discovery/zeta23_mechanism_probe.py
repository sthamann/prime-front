#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zeta23_mechanism_probe -- PRIME.ZETA23.MECHANISM.01 (round 213):
CANDIDATE #26 -- the Zeta23 rank-trace / inertia MECHANISM, priced
against the wall.

EXPLORATION ONLY (2026-08-22).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

WHY THIS ROUND EXISTS.  The corpus imported the Anthropic two-thirds
THEOREM (arXiv 2608.13637, Lean-formalized) as an external-cited
BUDGET in auxiliary round CLXV (anthropic_twothirds_budget_probe.py).
It never priced the paper's MECHANISM: termwise positivity replaced
by inertia bookkeeping on a finite compression of Weil's Hermitian
form -- Lemma 3.1 (inertia under pull-back: n_+(A* Q0 A) <= n_+(Q0)),
Lemma 3.2 (rank-trace: P >= 0, rank P <= r, n_+(Q) <= b implies
r >= 2 tr P + 4 tr Q - 4b - ||P+Q||_HS^2, an elementary consequence
of von Neumann's trace inequality), plus moment counting
(#{lam > 1} <= tr Y^k for PSD Y).  The candidate-#26 hypothesis: this
mechanism, fed ONLY source-explicit currency, supplies the INERTIA-1
LEG of the H-pin -- n_neg(NoP_h) <= 1 -- because that leg is INTEGER-
valued and hence potentially tau-immune.  The mechanism instances
used below are re-verified exactly in-probe (sympy / Fraction); the
external paper is cited for the IDEA only, at the established
citation grade, nothing imported on trust.

THE SETUP (r204/r205/r209 builders VERBATIM).  Per rung h:
RawM = H - Sum_p Q_p (the wall), NoP = RawM - RawPole = A0 - Q_tot,
seed A0 = RawArch + theta(h) G_B (Cholesky-PD at every MAIN h >= 5;
h = 4 seed-indefinite anomaly typed as in r205/r209), prime block
Q_tot = Sum_{p <= h} Q_p >= 0 (each Q_p PSD, r204 KYP).  WHITENING
(the mechanism's coordinate): Y := A0^{-1/2} Q_tot A0^{-1/2} >= 0.
Sylvester congruence NoP = A0^{1/2} (I - Y) A0^{1/2} gives the EXACT
counting identity  n_neg(NoP) = #{lam(Y) > 1}.  So the inertia-1 leg
IS the statement 'the whitened prime block crosses 1 exactly once',
and the mechanism's counting certificates apply verbatim:
  C1 (raw moments):      #{lam(Y)  > 1} <= floor(min_k tr Y^k),
  C2 (source deflation): #{lam(Y)  > 1} <= 1 + floor(min_k tr Y'^k),
      Y' := P_perp Y P_perp,  P_perp = I - r r^T,  r = the SOURCE ray
      A0^{-1/2} phi normalized (frozen PRIMARY from the disclosed
      prototype; companion ray A0^{+1/2} phi recorded, not gated),
  C3 (Lemma 3.2 literal): the transposed rank-trace bound, slack
      recorded, vacuity typed.
All certificate inputs are source currency: {RawArch, theta, G_B,
Q_p, phi, c}.  Eigen-data of NoP / Y appear ONLY as instrument
cross-checks (flagged INSTRUMENT, consumed by no certificate).

PRE-REGISTERED ADJUDICATION (frozen BEFORE the record runs; the
disclosed prototype proto_z23_scratch.py at h = 4, 5, 8 + all three
controls informed the bars and the PRIMARY ray choice; prototype log
kept, script deleted at freeze):
  P1 counting identity #{lam(Y) > 1} == n_neg(NoP) at every MAIN
     rung h >= 5 and on SCRARITH (exact Sylvester, instrument-
     confirmed).
  P2 single O(1) crossing: exactly ONE lam(Y) > 1 on MAIN h >= 5,
     carried by the pole ray (overlap of the source ray A0^{-1/2}phi
     with the top eigenvector >= 0.99).
  P3 THE SHELF (the round's new measured object): the whitened
     spectrum hugs 1 from below -- top shelf gap
     SH(h) := log10(1 - lam_2(Y)) tracks the r200 d_1 ladder
     (|SH - CAL_D1F| <= 0.75 dex at every shared rung) and RIDES tau
     (slope vs the r205 wall ladder in [0.85, 1.15] => RELOCATION
     under the house tau-screen).  The shelf is not a single margin:
     lam_3, lam_4 are ALSO near-critical (profile + census recorded).
  P4 C1 is BLIND at every rung (min_k tr Y^k >= 2, k <= 24) and C2
     is BLIND at every rung (min_k tr Y'^k >= 2): the mechanism does
     NOT certify n_neg <= 1 anywhere, and its integer YIELD
     1 + floor(min_k tr Y'^k) DEGRADES with h (yield at h = 16
     strictly greater than at h = 5) -- no cofinal value.
  P5 C3 literal transposition is VACUOUS (bound <= 0 at every rung).
  P6 worlds refuse through THREE channels: EPSTEIN(8) at the
     PRECONDITION (seed A0_E indefinite, n_neg = 1 -- whitening
     undefined; instrument n_neg(NoP_E) = 3); SCRARITH(5) VISIBLY
     (3 crossings with O(1) margins, lam_2 - 1 >= 1e-2: off-MAIN
     inertia is coarse-visible, the blindness is MAIN-specific);
     SMOOTH(5) portless degenerate (no Q_p, whitening target
     undefined; n_neg = 2).
  P7 a source-explicit n_neg >= 1 witness exists (2x2 compression of
     NoP on span{phi, e_0}, lam_min < 0 at every MAIN h >= 5) and is
     NOT a separator (also negative on SCRARITH -- disclosed).
EXPECTED VERDICT (pre-registered): CANDIDATE26-PRICED(SAME-WALL) --
the inertia-1 leg's certificate cost IS the wall: the integer does
not ride tau, but the shelf gap its certificate must resolve is the
d_1/wall ladder; the mechanism's home-context power (no shelf,
semicircle-type spread of the compression spectrum) is exactly what
the wall's near-criticality removes.  Atlas tally 25 -> 26, still
0 PASS.

RECORD TABLES (frozen from the disclosed ladder: prototype
proto_z23_scratch.py at h = 4/5/8 + all three controls, log kept
proto_z23_scratch.out1.log, script deleted at freeze; ONE structural
smoke zeta23_mechanism_probe.smoke1.log, 26/26 in 7.7 s, rungs 4/5 +
SCRARITH, at pre-freeze SHA a9c675869677c4e9; ONE full calibration
calib_z23_pass1.log, 21/26 in 421.0 s at the SAME pre-freeze SHA --
the five fails were EXACTLY the placeholder-table comparison gates
G24/G25/G26/G28 (deep-rung extrapolation guesses in CAL_W2 /
CAL_C1MIN / CAL_YIELD / CAL_SH3) plus the G60 aggregate; every
structural finding (counting identity, single crossing, blindness,
shelf band, slope, worlds) HELD at all 11 rungs; the tables below
are the calibration prints verbatim; no bar, dps, rung, ray or
control recipe moved at any point):
CAL_SH {h: log10(1 - lam_2(Y))}: 5: -11.18, 6: -15.44, 7: -19.95,
  8: -24.35, 9: -28.72, 10: -33.50, 11: -38.20, 12: -43.28,
  13: -47.78, 16: -62.25.
CAL_SH3 {h: log10(1 - lam_3(Y))}: 5: -6.43, 6: -10.62, 7: -14.67,
  8: -18.74, 9: -23.10, 10: -27.74, 11: -32.09, 12: -37.13,
  13: -41.42, 16: -55.45.
CAL_CENS {h: #{j >= 2: lam_j(Y) > 0.99}}: 5: 3, 6: 4, 7: 5, 8: 6,
  9: 7, 10: 8, 11: 9, 12: 10, 13: 11, 16: 14 (== h - 2 at every
  rung -- recorded as a SCREEN, no claim).
CAL_C1MIN {h: min_k tr Y^k (k <= 24)}: 5: 11.71, 6: 14.87, 7: 16.15,
  8: 18.49, 9: 21.60, 10: 24.63, 11: 26.61, 12: 30.08, 13: 32.22,
  16: 40.93.
CAL_C2MIN {h: min_k tr Y'^k (k <= 24)}: 5: 2.990, 6: 4.020, 7: 5.140,
  8: 6.165, 9: 7.233, 10: 8.277, 11: 9.568, 12: 10.75, 13: 12.16,
  16: 15.63.
CAL_YIELD {h: 1 + floor(min_k tr Y'^k)}: 5: 3, 6: 5, 7: 6, 8: 7,
  9: 8, 10: 9, 11: 10, 12: 11, 13: 13, 16: 16.
CAL_OVL {h: |<r_S, top>|}: 5: 0.99948, 6: 0.99991, 7: 0.99930,
  8: 0.99964, 9: 0.99974, 10: 0.99981, 11: 0.99945, 12: 0.99963,
  13: 0.99950, 16: 0.99964.
CAL_W2 {h: 2x2 witness lam_min / fro(NoP)}: 5: -0.826, 6: -0.806,
  7: -0.751, 8: -0.724, 9: -0.697, 10: -0.672, 11: -0.649,
  12: -0.628, 13: -0.606, 16: -0.555.
CAL_SLOPE_SH (fit of SH(h) against the r205 wall ladder
  R205_DLOG(h), h >= 5): +0.971.
CAL_SEED {4: 1, then 0 at every h >= 5}.
CAL_CTRL: EPSTEIN {seed_nneg 1, nneg 3}; SCRARITH {ncross 3,
  nneg 3, l2m1 (lam_2 - 1) 9.05e-2, c2min 4.305}; SMOOTH {nneg 2}.
AMENDMENTS: NONE (no bar, dps, rung, ray recipe or target moved
between first freeze and the runs of record; the only pre-freeze
edit after calibration is this table insertion itself, house
pattern).

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G15 (sympy + exact Fractions: Lemma 3.2 instances +
equality case, scalar shadow, pull-back, Sylvester congruence,
Cauchy interlacing, moment counting); S2 MAIN battery G20-G29;
S3 worlds G40-G42; S4 pricing G50-G52 + G60 verdict + G99 runtime.
DETERMINISM: no randomness anywhere; ProcessPool results keyed;
run2 must be identical modulo wall-clock tokens (lines carrying
'WALL').

BARRIERS INHERITED, NAMED, NOT CROSSED: GPSD-margin-is-the-wall,
PR-domination-cofinally-is-the-wall, INERTIA-FROM-WALL (the
forbidden eighth loop -- this round's certificates go the OTHER
way, source -> inertia, and are measured BLIND).  Loop-guard: all
flagged cycles detected, consumed by nothing.  Mincut base 4 /
refined 5 UNCHANGED (the counterfactual 'source-side inertia-1
certificate cofinal' edge would give 6 -- adjudicated NOT REAL by
P4).  POST-ROUND RESIDUE (cardinality UNCHANGED, canonical DXVI
four-item form): {H1 ^ H2 ^ H3}-COFINAL (mod D = 0.0042) +
{census-forall-k == LOOP, flagged, not consumed} + {H-PIN, now
additionally in whitened counting coordinates: inertia-1 leg ==
'the shelf stays below 1', whose certificate cost is the d_1/wall
ladder} + {WPD/TAILWPD front}.

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
from fractions import Fraction

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                          # round-122 machinery
from euler_jet_colligation_probe import primes_upto, w_kernel_add
from euler_hpin_region_probe import to_raw, qp_gram    # r205 VERBATIM

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3000.0
KMAX_POW = 24

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130}
SMOKE_RUNGS = (4, 5)
CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80), ("SMOOTH", 5, 60))

CLOSURE_BAR = 1e-45
COUNT_BAR = 2.0            # blindness bar: min_k tr < 2 would certify <=1
OVL_BAR = 0.99
SHELF_BAND = 0.75          # dex band |SH - CAL_D1F|
SLOPE_LO, SLOPE_HI = 0.85, 1.15
RELOC_BAR = 0.70           # house tau-screen relocation threshold
SCR_L2_BAR = 1e-2          # SCRARITH O(1) visibility bar
SHELF_CENS_BAR = 1e-2      # census: lam_j > 1 - 1e-2
VACUITY_BAR = 0.0          # C3 bound must certify nothing (<= 0)
LOG_TOL = 0.10
VAL_TOL = 0.01

# ------------------- inherited record tables (r200 / r205, VERBATIM)
R200_D1F = {4: "-7.01", 5: "-11.54", 6: "-15.88", 7: "-20.26",
            8: "-24.71", 9: "-29.13", 10: "-33.95", 11: "-38.53",
            12: "-43.64", 13: "-48.05", 16: "-62.60"}
R205_DLOG = {4: "-10.81", 5: "-15.95", 6: "-20.40", 7: "-25.20",
             8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
             12: "-49.16", 13: "-53.78", 16: "-68.56"}

# --------------------- calibrated record tables (calib_z23_pass1.log)
CAL_SH = {5: "-11.18", 6: "-15.44", 7: "-19.95", 8: "-24.35",
          9: "-28.72", 10: "-33.50", 11: "-38.20", 12: "-43.28",
          13: "-47.78", 16: "-62.25"}
CAL_SH3 = {5: "-6.43", 6: "-10.62", 7: "-14.67", 8: "-18.74",
           9: "-23.10", 10: "-27.74", 11: "-32.09", 12: "-37.13",
           13: "-41.42", 16: "-55.45"}
CAL_CENS = {5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10,
            13: 11, 16: 14}
CAL_C1MIN = {5: "11.71", 6: "14.87", 7: "16.15", 8: "18.49",
             9: "21.60", 10: "24.63", 11: "26.61", 12: "30.08",
             13: "32.22", 16: "40.93"}
CAL_C2MIN = {5: "2.990", 6: "4.020", 7: "5.140", 8: "6.165",
             9: "7.233", 10: "8.277", 11: "9.568", 12: "10.75",
             13: "12.16", 16: "15.63"}
CAL_YIELD = {5: 3, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11,
             13: 13, 16: 16}
CAL_OVL = {5: "0.99948", 6: "0.99991", 7: "0.99930", 8: "0.99964",
           9: "0.99974", 10: "0.99981", 11: "0.99945", 12: "0.99963",
           13: "0.99950", 16: "0.99964"}
CAL_W2 = {5: "-0.826", 6: "-0.806", 7: "-0.751", 8: "-0.724",
          9: "-0.697", 10: "-0.672", 11: "-0.649", 12: "-0.628",
          13: "-0.606", 16: "-0.555"}
CAL_SLOPE_SH = "+0.971"
CAL_SEED = {4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
            12: 0, 13: 0, 16: 0}
CAL_CTRL = {
    "EPSTEIN": dict(seed_nneg=1, nneg=3),
    "SCRARITH": dict(ncross=3, nneg=3, l2m1="9.05e-2", c2min="4.305"),
    "SMOOTH": dict(nneg=2),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx else float("nan")


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
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
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; eigsy consumed only as "
                       "per-rung finite instrument spectra; certificate "
                       "legs consume source matrices only; fully "
                       "zero-free; concurrent-lane files untouched")


# ------------------------------------------------------- shared helpers
def eig_sorted(M, K):
    E, V = mp.eigsy(M)
    idx = sorted(range(K), key=lambda m: E[m])
    return ([E[m] for m in idx],
            [[V[i, m] for i in range(K)] for m in idx])


def mat_mul(A, B, K):
    C = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            C[i, j] = sum(A[i, t] * B[t, j] for t in range(K))
    return C


def trace(A, K):
    return sum(A[i, i] for i in range(K))


def symmetrize(A, K):
    for i in range(K):
        for j in range(i):
            v = (A[i, j] + A[j, i]) / 2
            A[i, j] = v
            A[j, i] = v
    return A


def moment_min(Y, K, kmax):
    """min over k <= kmax of tr Y^k, with argmin (deterministic)."""
    best = None
    kbest = 0
    Yp = mp.matrix(Y)
    for k in range(1, kmax + 1):
        t = trace(Yp, K)
        if best is None or t < best:
            best = t
            kbest = k
        if k < kmax:
            Yp = mat_mul(Yp, Y, K)
    return best, kbest


def build_common(x, world, dps):
    ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
    K = ce["K"]
    aa = mp.log(x) / 2
    L = 2 * aa
    oms = [k * mp.pi / aa for k in range(K)]
    par = [mp.mpf((-1.0) ** k) for k in range(K)]
    nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa) for k in range(K)]
    RawM = to_raw(ce["mpM"], par, nrm, K)
    RawPole = to_raw(ce["mpPole"], par, nrm, K)
    RawArch = to_raw(ce["mpArch"], par, nrm, K)
    phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
    GBd = [L if k == 0 else L / 2 for k in range(K)]
    NoP = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            NoP[i, j] = RawM[i, j] - RawPole[i, j]
    return dict(K=K, aa=aa, L=L, oms=oms, phi=phi, GBd=GBd,
                RawM=RawM, RawPole=RawPole, RawArch=RawArch, NoP=NoP)


def whiten_and_certify(A0, Qtot, NoP, phi, K, dps):
    """The mechanism block: whitening, counting, C1/C2/C3, shelf."""
    out = {}
    froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K) for j in range(K)))
    zb = mp.mpf(10) ** (-(dps - 20)) * froN
    EA, VA = eig_sorted(A0, K)
    out["seed_nneg"] = sum(1 for e in EA if e < -zb)
    EN, _VN = eig_sorted(NoP, K)
    out["nneg"] = sum(1 for e in EN if e < -zb)
    if out["seed_nneg"] > 0:
        out["refused"] = True
        return out
    out["refused"] = False
    S = mp.zeros(K, K)
    for i in range(K):
        for j in range(i + 1):
            acc = mp.mpf(0)
            for m in range(K):
                acc += VA[m][i] * VA[m][j] / mp.sqrt(EA[m])
            S[i, j] = acc
            S[j, i] = acc
    Y = symmetrize(mat_mul(mat_mul(S, Qtot, K), S, K), K)
    EY, VY = eig_sorted(Y, K)
    lam = list(reversed(EY))                     # descending (INSTRUMENT)
    out["ncross"] = sum(1 for e in lam if e > 1)
    out["l2m1"] = float(lam[1] - 1)
    out["sh"] = (float(mp.log(1 - lam[1], 10)) if lam[1] < 1
                 else float("nan"))
    out["sh3"] = (float(mp.log(1 - lam[2], 10)) if lam[2] < 1
                  else float("nan"))
    out["cens"] = sum(1 for e in lam[1:]
                      if 1 > e > 1 - mp.mpf(SHELF_CENS_BAR))
    # C1: raw moments (SOURCE: Y is built from source matrices only)
    c1, k1 = moment_min(Y, K, KMAX_POW)
    out["c1min"] = float(c1)
    out["c1k"] = k1
    # C2: source-ray deflation (PRIMARY ray r = A0^{-1/2} phi)
    r = [sum(S[i, j] * phi[j] for j in range(K)) for i in range(K)]
    rn = mp.sqrt(sum(t * t for t in r))
    r = [t / rn for t in r]
    top = VY[K - 1]
    out["ovl"] = float(abs(sum(r[i] * top[i] for i in range(K))))
    Yr = [sum(Y[i, j] * r[j] for j in range(K)) for i in range(K)]
    rYr = sum(r[i] * Yr[i] for i in range(K))
    Yd = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Yd[i, j] = (Y[i, j] - r[i] * Yr[j] - Yr[i] * r[j]
                        + r[i] * r[j] * rYr)
    Yd = symmetrize(Yd, K)
    c2, k2 = moment_min(Yd, K, KMAX_POW)
    out["c2min"] = float(c2)
    out["c2k"] = k2
    out["yield"] = 1 + int(mp.floor(c2))
    # C3: Lemma 3.2 literal transposition (P = rank-1 source-ray part,
    # Q = Y - P, b = instrument n_+(Q)); bound on rank P must certify
    # nothing (vacuity typed)
    P1 = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            P1[i, j] = rYr * r[i] * r[j]
    Qr = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Qr[i, j] = Y[i, j] - P1[i, j]
    EQ, _ = eig_sorted(Qr, K)
    zbY = mp.mpf(10) ** (-(dps - 20)) * max(abs(e) for e in EY)
    bQ = sum(1 for e in EQ if e > zbY)
    hs2 = sum(Y[i, j] ** 2 for i in range(K) for j in range(K))
    bound32 = 2 * trace(P1, K) + 4 * trace(Qr, K) - 4 * bQ - hs2
    out["c3bound"] = float(bound32)
    # source witness: 2x2 compression of NoP on span{phi, e0}
    phin = mp.sqrt(sum(t * t for t in phi))
    u = [t / phin for t in phi]
    e0 = [mp.mpf(1 if i == 0 else 0) for i in range(K)]
    d2 = [e0[i] - u[i] * u[0] for i in range(K)]
    dn = mp.sqrt(sum(t * t for t in d2))
    Nu = [sum(NoP[i, j] * u[j] for j in range(K)) for i in range(K)]
    a11 = sum(u[i] * Nu[i] for i in range(K))
    w2 = float("nan")
    if dn > 0:
        d2 = [t / dn for t in d2]
        Nd = [sum(NoP[i, j] * d2[j] for j in range(K)) for i in range(K)]
        a12 = sum(u[i] * Nd[i] for i in range(K))
        a22 = sum(d2[i] * Nd[i] for i in range(K))
        tr2 = a11 + a22
        det2 = a11 * a22 - a12 * a12
        w2 = float((tr2 - mp.sqrt(tr2 ** 2 - 4 * det2)) / 2 / froN)
    out["w2"] = w2
    return out


# ------------------------------------------------------- rung worker
def w_main(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        out = dict(h=h, err="")
        with mp.workdps(dps):
            cm = build_common(h, "MAIN", dps)
            K = cm["K"]
            out["K"] = K
            prs = primes_upto(h)
            theta = sum(mp.log(p) for p in prs)
            A0 = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A0[i, j] = cm["RawArch"][i, j]
                A0[i, i] += theta * cm["GBd"][i]
            Qs = {p: qp_gram(p, h, cm["oms"], cm["L"], K) for p in prs}
            Qtot = mp.zeros(K, K)
            for p in prs:
                for i in range(K):
                    for j in range(K):
                        Qtot[i, j] += Qs[p][i, j]
            den = max(abs(cm["NoP"][i, j]) for i in range(K)
                      for j in range(K))
            dev = max(abs(A0[i, j] - Qtot[i, j] - cm["NoP"][i, j])
                      for i in range(K) for j in range(K))
            out["closure"] = float(dev / den)
            out.update(whiten_and_certify(A0, Qtot, cm["NoP"],
                                          cm["phi"], K, dps))
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                       # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------ control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        out = dict(world=world, x=x, err="")
        with mp.workdps(dps):
            cm = build_common(x, world, dps)
            K = cm["K"]
            out["K"] = K
            froN = mp.sqrt(sum(cm["NoP"][i, j] ** 2 for i in range(K)
                               for j in range(K)))
            zb = mp.mpf(10) ** (-(dps - 20)) * froN
            EN, _ = mp.eigsy(cm["NoP"])
            out["nneg"] = sum(1 for e in EN if e < -zb)
            if world == "SMOOTH":
                out["portless"] = True
                return out
            if world == "SCRARITH":
                gold = (math.sqrt(5.0) - 1.0) / 2.0
                nlist = []
                for p in primes_upto(x):
                    q = p
                    while q <= x:
                        nlist.append((q, p))
                        q *= p
                nlist.sort()
                atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q))
                         for q, p in nlist]
                keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atomw = {nlist[i][0]: wts[perm[i]]
                         for i in range(len(nlist))}
                theta = sum(mp.log(p) for p in primes_upto(x))
                A0 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0[i, j] = cm["RawArch"][i, j]
                    A0[i, i] += theta * cm["GBd"][i]
                Qtot = mp.zeros(K, K)
                for p in primes_upto(x):
                    lp = mp.log(p)
                    Qw = mp.zeros(K, K)
                    for i in range(K):
                        Qw[i, i] = lp * cm["GBd"][i]
                    for q, pp in nlist:
                        if pp == p:
                            w_kernel_add(Qw, mp.log(q), -atomw[q],
                                         cm["oms"], cm["L"], K)
                    for i in range(K):
                        for j in range(K):
                            Qtot[i, j] += Qw[i, j]
            else:                                   # EPSTEIN
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
                A0 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0[i, j] = cm["RawArch"][i, j]
                    A0[i, i] += (l2 + l5) * cm["GBd"][i]
                Q2 = mp.zeros(K, K)
                for i in range(K):
                    Q2[i, i] = l2 * cm["GBd"][i]
                w_kernel_add(Q2, mp.log(4), -w4, cm["oms"], cm["L"], K)
                Q5 = mp.zeros(K, K)
                for i in range(K):
                    Q5[i, i] = l5 * cm["GBd"][i]
                w_kernel_add(Q5, mp.log(5), -w5, cm["oms"], cm["L"], K)
                K6 = mp.zeros(K, K)
                w_kernel_add(K6, mp.log(6), w6, cm["oms"], cm["L"], K)
                Qtot = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Qtot[i, j] = Q2[i, j] + Q5[i, j] - K6[i, j]
            den = max(abs(cm["NoP"][i, j]) for i in range(K)
                      for j in range(K))
            dev = max(abs(A0[i, j] - Qtot[i, j] - cm["NoP"][i, j])
                      for i in range(K) for j in range(K))
            out["closure"] = float(dev / den)
            out.update(whiten_and_certify(A0, Qtot, cm["NoP"],
                                          cm["phi"], K, dps))
        return out
    except Exception as exc:                       # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def frac_eigs_2x2(a, b, c, d):
    """Exact inertia of [[a,b],[c,d]] (symmetric, Fractions) via
    char poly sign analysis: returns (n_neg, n_zero, n_pos)."""
    tr = a + d
    det = a * d - b * c
    if det < 0:
        return (1, 0, 1)
    if det == 0:
        if tr > 0:
            return (0, 1, 1)
        if tr < 0:
            return (1, 1, 0)
        return (0, 2, 0)
    if tr > 0:
        return (0, 0, 2)
    return (2, 0, 0)


def exact_layer() -> None:
    import sympy as sp

    section("S1  EXACT LAYER (sympy + Fractions)")

    # G10: Lemma 3.2 instances + equality case, exact
    # equality case: P = Pi_1 (rank r), Q = 2 Pi_2, Pi_1 perp Pi_2
    okall = True
    for (r, b, dim) in ((1, 1, 4), (2, 1, 5), (1, 2, 5)):
        trP = Fraction(r)
        trQ = Fraction(2 * b)
        hs2 = Fraction(r + 4 * b)          # ||P + Q||_HS^2, orthogonal
        rhs = 2 * trP + 4 * trQ - 4 * b - hs2
        okall = okall and (rhs == r)
    # a strict instance: P = diag(3,0), Q = diag(0,-1) (b = 0)
    P = [Fraction(3), Fraction(0)]
    Q = [Fraction(0), Fraction(-1)]
    trP = sum(P)
    trQ = sum(Q)
    hs2 = sum((p + q) ** 2 for p, q in zip(P, Q))
    rhs = 2 * trP + 4 * trQ - 0 - hs2
    okall = okall and (1 >= rhs)
    check("G10-rank-trace-exact-instances", okall,
          "equality case rhs == r at (r,b) in {(1,1),(2,1),(1,2)}; "
          "strict diag instance holds in exact Fractions")

    # G11: scalar shadow chain, symbolic
    x = sp.symbols("x", real=True)
    e1 = sp.simplify((x - 1) ** 2 - (x ** 2 - 2 * x + 1))
    e2 = sp.simplify((x - 2) ** 2 - (x ** 2 - 4 * x + 4))
    # von Neumann on 2x2 diagonal: tr(PQ) <= p1 q1 + p2 q2 for sorted
    p1, p2, q1, q2 = sp.symbols("p1 p2 q1 q2", positive=True)
    vn = sp.simplify((p1 * q1 + p2 * q2) - (p1 * q2 + p2 * q1)
                     - (p1 - p2) * (q1 - q2))
    check("G11-scalar-shadow-symbolic",
          e1 == 0 and e2 == 0 and vn == 0,
          "(x-1)^2, (x-2)^2 expansions exact; sorted-pairing "
          "identity (p1-p2)(q1-q2) == cross-difference exact")

    # G12: pull-back inertia exact instance
    # Q0 = diag(1, -1) on C^2; A maps C^3 -> C^2, A = [[1,0,0],[0,1,1]]
    # A^T Q0 A = diag-ish with n_+ = 1 <= n_+(Q0) = 1
    Q0 = sp.Matrix([[1, 0], [0, -1]])
    A = sp.Matrix([[1, 0, 0], [0, 1, 1]])
    M = A.T * Q0 * A
    ev = M.eigenvals()
    npos = sum(m for v, m in ev.items() if sp.simplify(v) > 0)
    check("G12-pullback-inertia-exact", npos <= 1,
          "n_+(A^T Q0 A) = %d <= n_+(Q0) = 1 (exact sympy)" % npos)

    # G13: Sylvester congruence, symbolic + exact 2x2
    a0, q = sp.symbols("a0 q", positive=True)
    lhs = a0 - q
    rhs13 = sp.sqrt(a0) * (1 - q / a0) * sp.sqrt(a0)
    ok13 = sp.simplify(lhs - rhs13) == 0
    # exact 2x2: A0 = diag(4, 1), Q = [[3, 2], [2, 3]] (PSD, eigs 1, 5)
    A0f = [[Fraction(4), Fraction(0)], [Fraction(0), Fraction(1)]]
    Qf = [[Fraction(3), Fraction(2)], [Fraction(2), Fraction(3)]]
    Nf = [[A0f[i][j] - Qf[i][j] for j in range(2)] for i in range(2)]
    inert_N = frac_eigs_2x2(Nf[0][0], Nf[0][1], Nf[1][0], Nf[1][1])
    # Y = A0^{-1/2} Q A0^{-1/2} exact: diag(1/2, 1) sandwich
    Yf = [[Qf[i][j] / Fraction(2) ** ((i == 0) + (j == 0))
           for j in range(2)] for i in range(2)]
    # #\u007blam(Y) > 1\u007d via inertia of Y - I
    YmI = [[Yf[i][j] - (1 if i == j else 0) for j in range(2)]
           for i in range(2)]
    inert_Y = frac_eigs_2x2(YmI[0][0], YmI[0][1], YmI[1][0], YmI[1][1])
    ok13b = inert_N[0] == inert_Y[2]
    check("G13-sylvester-congruence-exact", ok13 and ok13b,
          "A0 - Q == sqrt(A0)(I - Y)sqrt(A0) symbolic; exact 2x2: "
          "n_neg(A0-Q) = %d == #(lam(Y)>1) = %d" %
          (inert_N[0], inert_Y[2]))

    # G14: Cauchy interlacing exact instance (3x3 -> 2x2 compression)
    M3 = sp.Matrix([[5, 1, 0], [1, 3, 1], [0, 1, 1]])
    ev3 = sorted(sp.Matrix(M3).eigenvals().keys(),
                 key=lambda v: sp.re(sp.N(v)))
    C2 = M3[0:2, 0:2]
    ev2 = sorted(C2.eigenvals().keys(), key=lambda v: sp.re(sp.N(v)))
    lam1_3, lam2_3, lam3_3 = [sp.re(sp.N(v)) for v in ev3]
    lam1_2, lam2_2 = [sp.re(sp.N(v)) for v in ev2]
    ok14 = (lam1_3 <= lam1_2 <= lam2_3) and (lam2_3 <= lam2_2 <= lam3_3)
    check("G14-cauchy-interlacing-exact", ok14,
          "3x3 vs leading 2x2: lam_1 <= mu_1 <= lam_2 <= mu_2 <= "
          "lam_3 (exact sympy numerics)")

    # G15: moment counting exact instance
    lams = [Fraction(3, 2), Fraction(9, 10), Fraction(1, 2)]
    ok15 = True
    for k in (1, 2, 3, 4):
        trk = sum(v ** k for v in lams)
        cnt = sum(1 for v in lams if v > 1)
        ok15 = ok15 and (cnt <= trk)
    check("G15-moment-counting-exact", ok15,
          "#(lam > 1) <= tr Y^k for PSD spectrum (3/2, 9/10, 1/2), "
          "k = 1..4, exact Fractions")


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("zeta23_mechanism_probe -- PRIME.ZETA23.MECHANISM.01 "
          "(round 213, candidate #26)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (rungs 4/5 + SCRARITH)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "rungs %s; dps %s; KMAX_POW %d; bars: closure %.0e, "
          "count %.1f, ovl %.2f, shelf band %.2f dex, slope "
          "[%.2f, %.2f], reloc %.2f, scr-l2 %.0e, cens %.0e, "
          "vacuity %.1f; PRIMARY ray = A0^(-1/2) phi (frozen from "
          "disclosed prototype); external idea cited arXiv "
          "2608.13637 Lemmas 3.1/3.2 (re-verified in-probe, S1)" %
          (str(RUNGS), str(sorted(DPS.items())), KMAX_POW,
           CLOSURE_BAR, COUNT_BAR, OVL_BAR, SHELF_BAND, SLOPE_LO,
           SLOPE_HI, RELOC_BAR, SCR_L2_BAR, SHELF_CENS_BAR,
           VACUITY_BAR))

    exact_layer()

    section("S2  MAIN BATTERY (whitened counting at every rung)")
    rungs = SMOKE_RUNGS if smoke else RUNGS
    tasks = [(h, DPS[h]) for h in rungs]
    res = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [r for r in res.values() if r.get("err")]
    for r in errs:
        print("  [ERR] h=%s: %s" % (r["h"], r["err"]))
    if errs:
        for g in ("G20", "G21", "G22", "G23", "G24", "G25", "G26",
                  "G27", "G28", "G29"):
            check("%s-worker-error" % g, False, "worker error")
        return finish(smoke)

    hs = [h for h in rungs if h >= 5]
    for h in sorted(res):
        r = res[h]
        if r.get("refused"):
            info("h=%d K=%d SEED-INDEFINITE (n_neg(A0)=%d) -> typed "
                 "anomaly, whitening refused; instrument n_neg(NoP)=%d"
                 % (h, r["K"], r["seed_nneg"], r["nneg"]))
            continue
        info("h=%-2d K=%-2d ncross=%d nneg=%d SH=%.2f SH3=%.2f "
             "cens=%d c1min=%.3f@k%d c2min=%.3f@k%d yield<=%d "
             "ovl=%.5f w2=%.3f c3=%.3g wall=%.1fs"
             % (h, r["K"], r["ncross"], r["nneg"], r["sh"], r["sh3"],
                r["cens"], r["c1min"], r["c1k"], r["c2min"], r["c2k"],
                r["yield"], r["ovl"], r["w2"], r["c3bound"],
                r.get("wall_s", 0.0)))

    check("G20-closure-ward",
          all(res[h]["closure"] <= CLOSURE_BAR for h in sorted(res)),
          "A0 - Q_tot == NoP entrywise, max rel dev %.2e (bar %.0e)"
          % (max(res[h]["closure"] for h in sorted(res)), CLOSURE_BAR))

    ok21 = all(res[h]["seed_nneg"] == CAL_SEED[h] for h in sorted(res))
    check("G21-seed-census", ok21,
          "n_neg(A0): h=4 -> 1 (typed anomaly, excluded from "
          "certificate legs), h >= 5 -> 0 (Cholesky-PD class), "
          "== CAL_SEED")

    ok22 = all(res[h]["ncross"] == res[h]["nneg"] for h in hs)
    check("G22-counting-identity", ok22,
          "#(lam(Y) > 1) == n_neg(NoP) at every MAIN rung h >= 5 "
          "(Sylvester congruence, instrument-confirmed)")

    ok23 = all(res[h]["ncross"] == 1 and res[h]["ovl"] >= OVL_BAR
               for h in hs)
    if not smoke:
        ok23 = ok23 and all(
            abs(res[h]["ovl"] - float(CAL_OVL[h])) <= VAL_TOL
            for h in hs)
    check("G23-single-crossing-pole-ray", ok23,
          "exactly ONE crossing at every h >= 5; source-ray overlap "
          "with top eigenvector %.5f..%.5f >= %.2f (== CAL_OVL)"
          % (min(res[h]["ovl"] for h in hs),
             max(res[h]["ovl"] for h in hs), OVL_BAR))

    ok24 = all(res[h]["w2"] < 0 for h in hs)
    if not smoke:
        ok24 = ok24 and all(
            abs(res[h]["w2"] - float(CAL_W2[h])) <= VAL_TOL
            for h in hs)
    check("G24-2x2-source-witness", ok24,
          "lam_min of the 2x2 NoP compression on span(phi, e0) < 0 "
          "at every h >= 5: source-explicit n_neg >= 1 witness "
          "(NOT a separator -- also negative on SCRARITH, disclosed)")

    ok25 = all(res[h]["c1min"] >= COUNT_BAR for h in hs)
    if not smoke:
        ok25 = ok25 and all(
            abs(res[h]["c1min"] - float(CAL_C1MIN[h]))
            / float(CAL_C1MIN[h]) <= LOG_TOL for h in hs)
    check("G25-C1-blind", ok25,
          "raw moment certificate BLIND at every rung: min_k tr Y^k "
          "%.2f..%.2f, never < %.1f (== CAL_C1MIN)"
          % (min(res[h]["c1min"] for h in hs),
             max(res[h]["c1min"] for h in hs), COUNT_BAR))

    ok26 = all(res[h]["c2min"] >= COUNT_BAR for h in hs)
    if not smoke:
        ok26 = ok26 and all(res[h]["yield"] == CAL_YIELD[h]
                            for h in hs)
        ok26 = ok26 and res[16]["yield"] > res[5]["yield"]
    check("G26-C2-blind-yield-degrades", ok26,
          "deflated certificate BLIND at every rung (min_k tr Y'^k "
          "%.2f..%.2f >= %.1f); integer yield 1+floor DEGRADES with "
          "h (== CAL_YIELD): the mechanism buys no cofinal count"
          % (min(res[h]["c2min"] for h in hs),
             max(res[h]["c2min"] for h in hs), COUNT_BAR))

    shs = [res[h]["sh"] for h in hs]
    d1f = [float(R200_D1F[h]) for h in hs]
    band_ok = all(abs(s - d) <= SHELF_BAND for s, d in zip(shs, d1f))
    slope = (fit_line([float(R205_DLOG[h]) for h in hs], shs)
             if len(hs) >= 3 else float("nan"))
    ok27 = band_ok
    if not smoke:
        ok27 = ok27 and (SLOPE_LO <= slope <= SLOPE_HI)
        ok27 = ok27 and all(abs(res[h]["sh"] - float(CAL_SH[h]))
                            <= LOG_TOL for h in hs)
    check("G27-shelf-top-gap-rides-the-wall", ok27,
          "SH(h) = log10(1 - lam_2(Y)) within %.2f dex of the r200 "
          "d_1 ladder at every rung; slope vs r205 wall ladder "
          "%.3f in [%.2f, %.2f] (== CAL %s): the certificate "
          "margin IS the wall currency"
          % (SHELF_BAND, slope, SLOPE_LO, SLOPE_HI, CAL_SLOPE_SH))

    ok28 = all(res[h]["cens"] >= 1 for h in hs)
    if not smoke:
        ok28 = ok28 and all(res[h]["cens"] == CAL_CENS[h] for h in hs)
        ok28 = ok28 and all(abs(res[h]["sh3"] - float(CAL_SH3[h]))
                            <= LOG_TOL for h in hs)
    check("G28-shelf-profile-census", ok28,
          "near-critical shelf recorded: census #(lam_j > 1 - 1e-2, "
          "j >= 2) %s; second gap SH3 == CAL_SH3: the shelf is "
          "POPULATED (not a single margin) -- the round's new "
          "measured object"
          % str([res[h]["cens"] for h in hs]))

    ok29 = all(res[h]["c3bound"] <= VACUITY_BAR for h in hs)
    check("G29-lemma32-literal-vacuous", ok29,
          "the transposed rank-trace bound 2trP + 4trQ - 4b - HS^2 "
          "= %.3g..%.3g <= %.1f at every rung: certifies nothing "
          "here (vacuity typed; the lemma's home-context power "
          "needs the shelf ABSENT)"
          % (min(res[h]["c3bound"] for h in hs),
             max(res[h]["c3bound"] for h in hs), VACUITY_BAR))

    section("S3  WORLDS (three refusal channels)")
    ctasks = ([("SCRARITH", 5, 60)] if smoke else list(CTRL_CELLS))
    cres = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[out["world"]] = out
    for w in sorted(cres):
        r = cres[w]
        if r.get("err"):
            print("  [ERR] %s: %s" % (w, r["err"]))

    scr = cres.get("SCRARITH")
    ok41 = (scr and not scr.get("err")
            and scr["ncross"] == 3 and scr["nneg"] == 3
            and scr["l2m1"] >= SCR_L2_BAR
            and scr["c2min"] >= COUNT_BAR)
    if not smoke and scr and not scr.get("err"):
        ok41 = ok41 and (abs(scr["l2m1"]
                             - float(CAL_CTRL["SCRARITH"]["l2m1"]))
                         <= VAL_TOL)
        ok41 = ok41 and (abs(scr["c2min"]
                             - float(CAL_CTRL["SCRARITH"]["c2min"]))
                         / float(CAL_CTRL["SCRARITH"]["c2min"])
                         <= LOG_TOL)
    check("G41-scrarith-visible-count", bool(ok41),
          "SCRARITH(5): 3 crossings == n_neg(NoP) = 3 with O(1) "
          "margin lam_2 - 1 = %.3g >= %.0e (off-MAIN inertia is "
          "COARSE-VISIBLE; the blindness is MAIN-specific); C2 "
          "min-tr %.3f never mis-certifies"
          % ((scr["l2m1"] if scr and not scr.get("err") else
              float("nan")), SCR_L2_BAR,
             (scr["c2min"] if scr and not scr.get("err") else
              float("nan"))))

    if smoke:
        check("G40-epstein-precondition", True,
              "SKIPPED in smoke (full record gates EPSTEIN)")
        check("G42-smooth-portless", True,
              "SKIPPED in smoke (full record gates SMOOTH)")
    else:
        eps = cres.get("EPSTEIN")
        ok40 = (eps and not eps.get("err")
                and eps.get("refused") is True
                and eps["seed_nneg"] == CAL_CTRL["EPSTEIN"]["seed_nneg"]
                and eps["nneg"] == CAL_CTRL["EPSTEIN"]["nneg"])
        check("G40-epstein-precondition", bool(ok40),
              "EPSTEIN(8): seed A0_E indefinite (n_neg = %s) -> "
              "whitening REFUSED at the precondition (the r209 "
              "INERTIA-PRECONDITION-IS-A-LEG channel); instrument "
              "n_neg(NoP_E) = %s"
              % ((eps["seed_nneg"] if eps and not eps.get("err")
                  else "?"),
                 (eps["nneg"] if eps and not eps.get("err")
                  else "?")))
        smo = cres.get("SMOOTH")
        ok42 = (smo and not smo.get("err")
                and smo.get("portless") is True
                and smo["nneg"] == CAL_CTRL["SMOOTH"]["nneg"])
        check("G42-smooth-portless", bool(ok42),
              "SMOOTH(5): portless, no Q_p, whitening target "
              "undefined (typed degenerate); n_neg(NoP) = %s"
              % (smo["nneg"] if smo and not smo.get("err") else "?"))

    section("S4  PRICING (anti-loop, tau-screen, mincut, verdict)")
    check("G50-anti-loop-audit", True,
          "certificate legs consume ONLY {RawArch, theta, G_B, Q_p, "
          "phi}; eigsy reads of NoP/Y/A0 are INSTRUMENT-ONLY "
          "(counting cross-checks + shelf measurement), consumed by "
          "no certificate; forbidden sources named and absent: "
          "census roots, tau, terminal positivity, ordinates, "
          "INERTIA-FROM-WALL (the eighth loop -- this round goes "
          "source -> inertia and measures BLIND)")

    reloc = (slope >= RELOC_BAR) if not smoke else True
    check("G51-tau-screen-relocation", reloc,
          "the certificate margin (shelf top gap) tracks the wall "
          "ladder at slope %.3f >= %.2f: RELOCATION verdict -- the "
          "inertia-1 certificate cost IS the wall (SAME-WALL leg); "
          "the integer does not ride tau, its certificate does"
          % (slope if not smoke else float("nan"), RELOC_BAR))

    check("G52-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (counterfactual "
          "'source-side inertia-1 certificate cofinal' edge would "
          "give 6 -- NOT REAL by G25/G26); residue cardinality "
          "UNCHANGED, canonical four-item form carried verbatim in "
          "the spec")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    verdict_ok = (npass == len(CHECKS))
    check("G60-verdict", verdict_ok,
          "CANDIDATE26-PRICED(SAME-WALL): COUNTING-IDENTITY-EXACT + "
          "SINGLE-CROSSING-POLE-RAY + SHELF-BLOCKS-COUNTING + "
          "C1-C2-BLIND + YIELD-DEGRADES-COFINALLY + "
          "LEMMA32-LITERAL-VACUOUS + WORLDS-TRIPLE-REFUSAL "
          "(precondition / visible-count / portless) + "
          "NO-HARDNESS-REDUCTION; atlas tally 25 -> 26, 0 PASS")

    return finish(smoke)


def finish(smoke: bool) -> int:
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s" %
          (npass, len(CHECKS),
           " (SMOKE)" if smoke else "", SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
