#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ranktrace_adjudication_probe -- PRIME.PORT.EXTERNAL.
RANKTRACE_CEILING.ADJUDICATION.01 (round 267): adjudication of the
EXTERNAL result arXiv:2608.13637 (Alpoge--Furman, submitted
2026-08-13; argument found by Claude/Anthropic, verified by the
listed authors; Lean 4 formalisation anthropics/zeta-23-lean tag
v1.0, sorry-free, three standard axioms) against our program:
import, congruence, or bypass.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE EXTERNAL RESULT (typed EXTERNAL; every quoted fact below is a
documented constant with source, never recomputed from zeros):
unconditionally >= 2/3 of the zeta zeros are simple and on the
critical line, >= 5/6 distinct (Montgomery--Taylor window: 0.6725 /
0.83625; previous records 5/12 and 0.6603).  MECHANISM: Weil's
Hermitian form W restricted to d ~ N(T,2T) modulated copies of ONE
window psi (Gabor family at critical density 2pi/L, L = log(T/2pi),
Fourier support <= 1 "bandwidth one") gives a real symmetric d x d
matrix Gtilde = P + Q + o(1): each distinct ON-LINE zero a rank-1
PSD atom in P, each OFF-LINE pair {rho, 1-conj(rho)} a signature-
(1,1) block in Q (Sylvester/pull-back, Bombieri's observation).
Unconditional inputs: tr Gtilde = (1+o(1)) N and ||Gtilde||_HS^2 =
(R(psi)+o(1)) N with R(psi) = [int psi^2 + int int |u-v| psi psi]
/ (int psi)^2 (Montgomery's prime-side second moment, bandwidth
<= 1; R(psi_0) = 4/3, R(psi_MT) = 1/2 + (1/sqrt2) cot(1/sqrt2)).
THE RANK--TRACE INEQUALITY (their Lemma 3.2, via von Neumann's
trace inequality; the matrix form of m^2 >= 2m-1): for Hermitian
P >= 0 with rank P <= r and Q with n_+(Q) <= b,
    r >= 2 tr P + 4 tr Q - 4 b - ||P + Q||_HS^2 ,
which yields the single chain N_0^s >= 4 tr G - 2N - ||G||_HS^2 =
(2 - R(psi)) N.  THE BANDWIDTH-ONE CEILING (their section 7.2 +
Lean Zeta23.PairCeiling.ceiling_law256): any certificate consuming
ONLY the first two trace moments against bandwidth-1 test functions
plus the on/off block partition is bounded by p_0 <= 0.6818287
(< 1, RH out of reach of the mechanism); the binding constraint is
X <= T in their Proposition 5.4 -- beyond it the OFF-DIAGONAL PRIME
SUM is no longer dominated by the diagonal and its evaluation would
require Hardy--Littlewood / pair-correlation information for
Fourier support > 1; higher moments tr G^k live only in the
Rudnick--Sarnak range X^k <= T^{2-eps}, so at X ~ T only k = 1:
"unconditionally, higher moments add nothing".  CAVEAT documented:
at tag v1.0 the ceiling's form-factor enclosures (EnclOK) are
certified by interval arithmetic OUTSIDE the Lean kernel; Theorems
A/B themselves are kernel-checked axiom-clean.

OUR SIDE (the comparison objects, all prior rounds): the window
object is the Galerkin compression of the localized Weil operator
on the PRIME/COMB side -- scaled-Chebyshev Gram G_n of the signed
defect measure mutilde on the union grid (r257 world_block basis
convention, sealed), wall = positive definiteness of G_{N_w}
through the free window (half-filling N_w = ceil(S/2), v956);
inertia machinery: v956 inertia theorem + r229 Pontryagin census
(same Sylvester pull-back as their Lemma 3.1); terminal object:
bordered tau pair with the one-inequality reduction q_N < 1 (v959);
measured walls: PAIRCORR (root-scale comb cancellation; r262/r263
d2 demand 1.24/1.73/2.25 decades min/med/max on the 42-rung
ladder) and DEFINITENESS_WALL_EQUIVALENT (r257/r265).

THE FOUR SEALED QUESTIONS:
 q1 Is their finite compression our window object in another
    basis?  ANSWER FRAME (sealed): both are finite compressions of
    the SAME Weil Hermitian form, but on DUAL sides -- theirs
    samples the ZERO side (d Gabor atoms at critical density in d
    dimensions, near-tight frame, per-atom trace <= 1, evaluated
    unconditionally through the prime side), ours compresses the
    PRIME/COMB side (S signed atoms into N = ceil(S/2) dimensions,
    no frame bound).  Leg C measures the structural gap (aspect
    ratio, atom-norm spread in decades, R-analog).
 q2 Is their ceiling our wall?  Two sealed sub-answers adjudicated
    separately: LOCATION (their binding constraint = off-diagonal
    prime-pair cancellation beyond diagonal/absolute-value control
    = the PAIRCORR class; externally PROVEN as a ceiling for their
    certificate class vs ours MEASURED as d2 demand) and SCOPE
    (their theorem quantifies ONLY over bandwidth-one two-moment
    certificates; our coordinate -- full comb data in the chain,
    bordered terminal scalar -- is outside that class, so their
    ceiling does NOT close our lane, and their theorem does NOT
    bound our objects).
 q3 Import: does the rank--trace / Cauchy--Schwarz certificate,
    translated to our window Gram, certify an unconditional
    POSITIVE-DIRECTION PROPORTION n_+(G_N)/N on our ladder?
    Sealed translations (both scale-invariant / scale-optimized):
      f_CS  = (tr G)^2 / (N ||G||_HS^2)      [n_+ >= f_CS N]
      f_RT  = max(0, (A2^2/(4||G||_HS^2) - q)/N),
              A2 = 2 tr GP + 4 tr GQ  (GP/GQ = positive-/negative-
              weight atom parts, n_+(GQ) = 0, rank GQ <= q; Weyl:
              n_+(G) >= rank-certificate - q; the global rescale
              G -> G/c is optimized exactly, c* = 2 HS^2/A2)
      f_import = max(f_CS, f_RT).
    SEALED GO RULE: IMPORT_CERTIFICATE_GO iff f_import >= 0.10 on
    BOTH mains AND median f_import >= 0.10 over the 42-rung ladder
    (smoke: mains only, typed); else NO_IMPORT(FRAME_MISMATCH,
    measured values).
 q4 Inertia crosswalk: their Lemma 3.1 (inertia under pull-back)
    IS our r229 census mechanism; exact-rational gates on the r261
    MAINLIKE instance (n_+(H_n) <= p, n_-(H_n) <= q every degree,
    n_-(H_S) == q sharp at full degree) plus their signature-(1,1)
    pair-block fact; OURS finer locally (exact quasi-definiteness
    boundary, half-filling location), THEIRS adds the quantitative
    trace/HS step (the leg-C import candidate).

SEALED SEPARATION TEST (the q2-scope machine support): does the
two-moment certificate SEE the wall?  On w9 MAIN vs the three r263
controls (EPSTEIN / SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27):
spread(f_CS) < 0.5 x spread(true n_+(G_N)/N)  =>  TWO_MOMENT_BLIND
(the imported certificate class cannot express the wall statement,
consistent with their own "higher moments add nothing" boundary);
else TWO_MOMENT_SEES_WALL.

LEGS:
 A  EXTERNAL FORM RECONSTRUCTION: R(psi_0) == 4/3 and R(psi_MT) ==
    closed form by our own nested Gauss--Legendre quadrature of
    their (5.13) (kink split at u = v, tol 1e-8); certificate
    arithmetic 2 - R and (3 - R)/2 vs the documented constants;
    ordering 5/12 < 2/3 < 0.6725 < p_0 < 1 and R_MT < R_0; von
    Neumann trace inequality property test (seeded).
 B  THE LEMMA REBUILT: equality case exact (orthogonal projections,
    integers); 400-instance seeded property test of the rank-trace
    inequality AND the Cauchy--Schwarz corollary n_+(H) >=
    (tr H)^2/||H||_HS^2 (tr H > 0); scalar shadows m^2 >= 2m-1 and
    m^2 >= 3m-2 with exact equality sets {1} and {1,2}; pair-block
    inertia vv^T + conj(v)conj(v)^T = 2(aa^T - bb^T) with exact
    eigen-census (1,1) (sympy); r261 MAINLIKE exact Hankel inertia
    census (q4 gates).
 C  THE IMPORT TEST: packs BH.wpack mains (9, 13) + r263 controls
    verbatim + full frame-A ladder (42 rungs, h <= 900; skipped in
    smoke); basis ward on w9 vs CT.world_block (slogdet rel 1e-9);
    validity gates (rank-trace on (GP, GQ), CS vs eigh count) on
    every window; the sealed import values and GO rule; the sealed
    separation test; the frame-gap census (aspect ratio S/N,
    atom-norm spread in decades, R_ours vs external 4/3).
 D  CEILING + INERTIA CROSSWALK (typed adjudication, documented
    constants restated, no new computation): LOCATION and SCOPE
    verdicts of q2; the q4 crosswalk typing.

FIREWALL: no zeros, no prime-table oracles (AST scan; the sieve
lives in the frozen upstream builders, consumed as node positions +
signed weights only); EXTERNAL paper facts enter as documented
constants with source strings ONLY (never as data in any gate about
OUR objects); RNG only in the declared seeded property tests (and
the SCRAMBLE control seed 1, r263 verbatim); ground truth (control
flips 25/21/27) enters gates only.  Writes nothing but stdout.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPST/SCR(seed
1)/SMOOTH with flips 25/21/27 (r263 verbatim defs); ladder frame-A
h <= 900, 42 rungs, (N, kz)-sorted; GO_BAR 0.10; SEP_FACTOR 0.5;
QUAD_TOL 1e-8; GL_N 120; PROP_SEED 20260825; N_PROP 400; EIG_TOL
1e-10 (relative); W9_WARD_BAR 1e-9; VALID_EPS 1e-6 (validity
slack); EXT constants table in EXT below (source arXiv:2608.13637
v1 + anthropics/zeta-23-lean v1.0); r263 demand record (1.24, 1.73,
2.25) dec documented; r261 MAINLIKE instance verbatim: atoms (-3/2,
-1, -1/2, 1/4, 3/4, 5/4), weights (2/3, -1/5, 1/2, -3/7, 1, 1/3)
=> p = 4, q = 2, S = 6; runtime <= 1800 s; smoke = legs A/B/D +
mains + controls (ladder skipped, GO typed SMOKE).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  EXTERNAL_FORM_RECONSTRUCTED / EXTERNAL_FORM_BROKEN(typed)
+ CEILING_IS_OUR_WALL(LOCATION: MV-diagonal boundary == PAIRCORR
    root-scale comb cancellation; theirs PROVEN for their class,
    ours MEASURED) / CEILING_LOCATION_MISMATCH(typed)
+ CEILING_ORTHOGONAL(SCOPE: bandwidth-one two-moment certificate
    class does not contain our full-chain coordinate)
+ IMPORT_CERTIFICATE_GO(values) / NO_IMPORT(FRAME_MISMATCH,
    values)
+ TWO_MOMENT_BLIND / TWO_MOMENT_SEES_WALL
+ INERTIA_CROSSWALK(SAME_MECHANISM: their Lemma 3.1 == r229
    census; OURS_EXACT_LOCAL, THEIRS_QUANT_RANKTRACE)
+ SOURCE_NOTE(ENCL_INTERVAL_ARITHMETIC: ceiling constant not
    kernel-checked at tag v1.0; Theorems A/B axiom-clean).
Honesty before beauty: no verdict claims an external proof of OUR
wall, an RH direction, or a derived 5/7; the import decision is a
measurement under sealed translations, honest either way.

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
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import coupledtau_probe as CT                # noqa: E402 r257
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

# ---------------- sealed constants
MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
H_CAP = 900
LADDER_EXPECT = 42
GO_BAR = 0.10
SEP_FACTOR = 0.5
QUAD_TOL = 1e-8
GL_N = 120
PROP_SEED = 20260825
N_PROP = 400
EIG_TOL = 1e-10
W9_WARD_BAR = 1e-9
VALID_EPS = 1e-6
RUNTIME_CAP = 1800.0
R263_DEMAND_DEC = (1.24, 1.73, 2.25)   # min/med/max, r263 record

# EXTERNAL documented constants (source: arXiv:2608.13637v1,
# 2026-08-13, Alpoge--Furman / Claude-Anthropic; Lean repo
# github.com/anthropics/zeta-23-lean tag v1.0).  NEVER recomputed
# from zeros; consumed as documentation + arithmetic-consistency
# gates only.
EXT = dict(
    SRC=("arXiv:2608.13637v1 (2026-08-13; Alpoge--Furman; argument"
         " by Claude/Anthropic) + anthropics/zeta-23-lean tag v1.0"),
    R0=4.0 / 3.0,                       # R(psi_0), their Lemma 5.6
    PROP_SIMPLE=2.0 / 3.0,              # Theorem A(i) = 2 - R0
    PROP_DISTINCT=5.0 / 6.0,            # Theorem A(ii) = (3-R0)/2
    MT_SIMPLE=0.67250,                  # 2 - c_MT^{-1} (5 digits)
    MT_DISTINCT=0.83625,                # (3 - c_MT^{-1})/2
    CEIL_P0=0.6818287,                  # sec 7.2 p_0 upper bound
    PREV_SIMPLE=5.0 / 12.0,             # PRZZ20 record
    PREV_DISTINCT=0.6603,               # Wu15 record
    CEIL_LOCATION=("binding constraint X <= T (their Prop 5.4): "
                   "beyond it the off-diagonal prime sum needs "
                   "Hardy--Littlewood / pair-correlation support "
                   "> 1; higher moments only in Rudnick--Sarnak "
                   "range X^k <= T^{2-eps} -- 'unconditionally, "
                   "higher moments add nothing'"),
    LEAN_STATE=("Theorems A/B kernel-checked, axioms propext/"
                "Classical.choice/Quot.sound, no sorry; ceiling "
                "law256 enclosures (EnclOK) interval-arithmetic "
                "OUTSIDE the kernel at tag v1.0"),
)

# r261 MAINLIKE exact instance (verbatim)
R261_XS = (Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
           Fr(5, 4))
R261_WS = (Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
           Fr(1, 3))

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name,
                               detail), flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r",
               encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; external paper "
                       "facts enter as documented constants only; "
                       "our objects consume node positions + "
                       "signed weights via the frozen builders"
                       if not bad else "; ".join(bad))


# ---------------- leg A helpers: quadrature of their (5.13)
def _gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def _gl_map(x, w, a, b):
    xm = 0.5 * (b - a) * x + 0.5 * (a + b)
    wm = 0.5 * (b - a) * w
    return xm, wm


def r_window(psi):
    """R(psi) by nested Gauss--Legendre; the |u-v| kink is split
    exactly at u = v (inner integral over v < u, doubled)."""
    x, w = _gl(GL_N)
    u, wu = _gl_map(x, w, -0.5, 0.5)
    pu = np.array([psi(t) for t in u])
    i_psi = float(np.sum(wu * pu))
    i_psi2 = float(np.sum(wu * pu * pu))
    dbl = 0.0
    for uk, wk, pk in zip(u, wu, pu):
        v, wv = _gl_map(x, w, -0.5, uk)
        pv = np.array([psi(t) for t in v])
        dbl += wk * pk * float(np.sum(wv * (uk - v) * pv))
    dbl *= 2.0
    return (i_psi2 + dbl) / (i_psi * i_psi)


def inertia_counts(evals, scale=None):
    ev = np.asarray(evals, float)
    sc = scale if scale is not None else float(
        np.max(np.abs(ev))) if len(ev) else 1.0
    tol = EIG_TOL * max(sc, 1e-300)
    return int(np.sum(ev > tol)), int(np.sum(ev < -tol))


# ---------------- leg C helpers: our window Gram, split by sign
def gram_split(p):
    """r257 world_block basis convention VERBATIM (hull over union
    + border atoms, scaled Chebyshev-U), without the slogdet loop;
    the Gram split into positive-weight (GP, PSD) and negative-
    weight (GQ, NSD) atom parts."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, _bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    P = CT.u_matrix(xu, x0, rh, N)
    pos = wu > 0.0
    neg = ~pos
    GP = (P[:, pos] * wu[pos]) @ P[:, pos].T
    GQ = (P[:, neg] * wu[neg]) @ P[:, neg].T
    G = GP + GQ
    anorm = np.abs(wu) * np.sum(P * P, axis=0)
    return dict(N=N, G=G, GP=GP, GQ=GQ, q=int(np.sum(neg)),
                p=int(np.sum(pos)), S=len(wu), anorm=anorm,
                x0=x0, rh=rh)


def import_values(gs):
    """the sealed q3 translations (scale-invariant / scale-
    optimized) + validity data."""
    G, GP, GQ, N, q = gs["G"], gs["GP"], gs["GQ"], gs["N"], gs["q"]
    trG = float(np.trace(G))
    hs2 = float(np.sum(G * G))
    trP = float(np.trace(GP))
    trQ = float(np.trace(GQ))
    ev = np.linalg.eigvalsh(G)
    npos, nneg = inertia_counts(ev)
    f_cs = (trG * trG / hs2 / N) if (trG > 0 and hs2 > 0) else 0.0
    a2 = 2.0 * trP + 4.0 * trQ
    cert = (a2 * a2 / (4.0 * hs2)) if (a2 > 0 and hs2 > 0) else 0.0
    f_rt = max(0.0, (cert - q) / N)
    evP = np.linalg.eigvalsh(GP)
    rankP = int(np.sum(evP > EIG_TOL * max(float(np.max(
        np.abs(evP))), 1e-300)))
    # validity: rank-trace at raw scale (b = 0) and CS vs eigh
    rt_ok = rankP + VALID_EPS >= 2.0 * trP + 4.0 * trQ - hs2
    cs_ok = (trG <= 0) or (npos + VALID_EPS >= trG * trG / hs2)
    return dict(trG=trG, hs2=hs2, trP=trP, trQ=trQ, npos=npos,
                nneg=nneg, f_cs=f_cs, f_rt=f_rt,
                f_import=max(f_cs, f_rt), rankP=rankP,
                rt_ok=rt_ok, cs_ok=cs_ok,
                true_frac=npos / float(N),
                r_ours=(N * hs2 / (trG * trG)) if trG > 0
                else float("inf"))


# ---------------- exact Hankel inertia (q4, exact rationals)
def _det_fr(M):
    """exact Fraction determinant (fraction-free enough here)."""
    M = [row[:] for row in M]
    n = len(M)
    sign = 1
    d = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            sign = -sign
        d *= M[c][c]
        inv = Fr(1) / M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] * inv
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return sign * d


def hankel_inertia_exact(xs, ws, n):
    """inertia of H_n = [m_{i+j}] via exact leading principal
    minors + Jacobi's sign rule (valid: all minors nonzero,
    gated); returns (n_+, n_-, all_minors_nonzero)."""
    mom = [sum(w * x ** k for x, w in zip(xs, ws))
           for k in range(2 * n - 1)]
    minors = []
    for m in range(1, n + 1):
        H = [[mom[i + j] for j in range(m)] for i in range(m)]
        minors.append(_det_fr(H))
    nz = all(dm != 0 for dm in minors)
    seq = [Fr(1)] + minors
    nneg = sum(1 for a, b in zip(seq, seq[1:])
               if (a > 0) != (b > 0))
    return n - nneg, nneg, nz


# ==================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("ranktrace_adjudication_probe -- PRIME.PORT.EXTERNAL."
          "RANKTRACE_CEILING.ADJUDICATION.01 (round 267)")
    print("SPEC_SHA %s  MODE %s" % (SPEC_SHA[:16],
                                    "SMOKE" if smoke else "FULL"))
    print("=" * 78, flush=True)

    # ---------------- S0 firewall + external table
    section("S0  FIREWALL + EXTERNAL CONSTANTS TABLE")
    fw_ok, fw_msg = firewall_audit()
    check("G1-ast-firewall", fw_ok, fw_msg)
    info("EXTERNAL SOURCE: %s" % EXT["SRC"])
    info("EXTERNAL: 2/3 simple+on-line, 5/6 distinct (uncond.); "
         "MT window %.5f / %.5f; ceiling p0 <= %.7f; records "
         "5/12 / %.4f" % (EXT["MT_SIMPLE"], EXT["MT_DISTINCT"],
                          EXT["CEIL_P0"], EXT["PREV_DISTINCT"]))
    info("EXTERNAL ceiling location: %s" % EXT["CEIL_LOCATION"])
    info("EXTERNAL Lean state: %s" % EXT["LEAN_STATE"])
    check("G2-external-typed", True,
          "all external facts above enter as DOCUMENTED constants "
          "with source; no gate on OUR objects consumes them")

    # ---------------- S1 LEG A: external form reconstruction
    section("S1  LEG A -- EXTERNAL FORM RECONSTRUCTION")
    r0 = r_window(lambda t: 1.0)
    check("G3-R-psi0-quadrature", abs(r0 - EXT["R0"]) <= QUAD_TOL,
          "our nested-GL quadrature of their (5.13), indicator "
          "window: R = %.12f vs 4/3 (dev %.1e)"
          % (r0, abs(r0 - EXT["R0"])))
    s2 = 1.0 / math.sqrt(2.0)
    rmt_closed = 0.5 + s2 * (math.cos(s2) / math.sin(s2))
    rmt = r_window(lambda t: math.cos(math.sqrt(2.0) * t))
    check("G4-R-psiMT-quadrature",
          abs(rmt - rmt_closed) <= QUAD_TOL,
          "Montgomery--Taylor window: R = %.12f vs closed form "
          "1/2 + (1/sqrt2)cot(1/sqrt2) = %.12f (dev %.1e)"
          % (rmt, rmt_closed, abs(rmt - rmt_closed)))
    ok5 = (abs((2.0 - r0) - EXT["PROP_SIMPLE"]) <= 1e-12
           and abs((3.0 - r0) / 2.0 - EXT["PROP_DISTINCT"]) <= 1e-12
           and abs((2.0 - rmt_closed) - EXT["MT_SIMPLE"]) <= 5e-6
           and abs((3.0 - rmt_closed) / 2.0
                   - EXT["MT_DISTINCT"]) <= 5e-6)
    check("G5-certificate-arithmetic", ok5,
          "2 - R0 = %.6f == 2/3; (3 - R0)/2 = %.6f == 5/6; "
          "2 - R_MT = %.6f == %.5f; (3 - R_MT)/2 = %.6f == %.5f"
          % (2.0 - r0, (3.0 - r0) / 2.0, 2.0 - rmt_closed,
             EXT["MT_SIMPLE"], (3.0 - rmt_closed) / 2.0,
             EXT["MT_DISTINCT"]))
    ok6 = (EXT["PREV_SIMPLE"] < EXT["PROP_SIMPLE"]
           < EXT["MT_SIMPLE"] < EXT["CEIL_P0"] < 1.0
           and rmt_closed < r0
           and EXT["PREV_DISTINCT"] < EXT["PROP_DISTINCT"])
    check("G6-ordering-and-ceiling-gap", ok6,
          "5/12 < 2/3 < 0.67250 < p0 %.7f < 1 (gap MT->ceiling "
          "%.4f; the method ends strictly below 1: RH out of "
          "reach of the mechanism BY THEIR OWN THEOREM); R_MT "
          "%.5f < R_0 %.5f" % (EXT["CEIL_P0"],
                               EXT["CEIL_P0"] - EXT["MT_SIMPLE"],
                               rmt_closed, r0))
    rng = np.random.default_rng(PROP_SEED)
    vn_worst = -1.0
    for _ in range(N_PROP):
        dd = int(rng.integers(2, 9))
        A = rng.standard_normal((dd, dd))
        A = A @ A.T
        Bm = rng.standard_normal((dd, dd))
        Bm = Bm @ Bm.T
        lhs = float(np.trace(A @ Bm))
        la = np.sort(np.linalg.eigvalsh(A))[::-1]
        lb = np.sort(np.linalg.eigvalsh(Bm))[::-1]
        rhs = float(np.sum(la * lb))
        vn_worst = max(vn_worst, lhs - rhs)
    check("G7-von-neumann-property", vn_worst <= 1e-8,
          "tr(AB) <= sum_i lam_i(A) lam_i(B) on %d seeded PSD "
          "pairs (worst violation %.1e <= 1e-8) -- their proof "
          "engine of Lemma 3.2" % (N_PROP, vn_worst))

    # ---------------- S2 LEG B: the lemma rebuilt
    section("S2  LEG B -- THE RANK--TRACE LEMMA REBUILT")
    d0, r_, b_ = 7, 3, 2
    P0 = np.zeros((d0, d0))
    Q0 = np.zeros((d0, d0))
    for i in range(r_):
        P0[i, i] = 1.0
    for i in range(r_, r_ + b_):
        Q0[i, i] = 2.0
    lhs8 = float(r_)
    rhs8 = (2.0 * np.trace(P0) + 4.0 * np.trace(Q0) - 4.0 * b_
            - float(np.sum((P0 + Q0) ** 2)))
    check("G8-equality-case-exact", abs(lhs8 - rhs8) == 0.0,
          "P = Pi_1 (rank %d), Q = 2 Pi_2 (rank %d) orthogonal: "
          "r = %g == RHS = %g EXACT (their stated equality case)"
          % (r_, b_, lhs8, rhs8))
    rt_worst = -1e9
    cs_worst = -1e9
    for _ in range(N_PROP):
        dd = int(rng.integers(3, 11))
        rr = int(rng.integers(1, dd + 1))
        mm = int(rng.integers(1, dd + 1))
        bb = int(rng.integers(0, mm + 1))
        A = rng.standard_normal((dd, rr))
        Pm = A @ A.T
        Bm = rng.standard_normal((dd, mm))
        sg = np.array([1.0] * bb + [-1.0] * (mm - bb))
        Qm = (Bm * sg) @ Bm.T
        hs = float(np.sum((Pm + Qm) ** 2))
        viol = (2.0 * np.trace(Pm) + 4.0 * np.trace(Qm)
                - 4.0 * bb - hs) - rr
        rt_worst = max(rt_worst, viol)
        H = Pm + Qm
        trH = float(np.trace(H))
        if trH > 0:
            npos, _ = inertia_counts(np.linalg.eigvalsh(H))
            cs_worst = max(cs_worst,
                           trH * trH / float(np.sum(H * H)) - npos)
    check("G9-ranktrace-property", rt_worst <= 1e-9,
          "rank P >= 2trP + 4trQ - 4b - ||P+Q||_HS^2 on %d seeded "
          "instances (worst violation %+.1e)" % (N_PROP, rt_worst))
    check("G10-cauchyschwarz-corollary", cs_worst <= 1e-9,
          "n_+(H) >= (trH)^2/||H||_HS^2 on the same instances "
          "with trH > 0 (worst violation %+.1e) -- the scale-"
          "invariant m=1 certificate imported in leg C"
          % cs_worst)
    eq1 = [m for m in range(1, 13) if m * m == 2 * m - 1]
    eq2 = [m for m in range(1, 13) if m * m == 3 * m - 2]
    ok11 = (all(m * m >= 2 * m - 1 for m in range(1, 13))
            and all(m * m >= 3 * m - 2 for m in range(1, 13))
            and eq1 == [1] and eq2 == [1, 2])
    check("G11-scalar-shadows-exact", ok11,
          "m^2 >= 2m-1 (equality set %s) and m^2 >= 3m-2 "
          "(equality set %s) for m = 1..12 -- the two integrality "
          "levels their (P,Q) / (P1,Q') regroupings matrix-ify"
          % (eq1, eq2))
    a_v = sp.Matrix([1, 2, 0])
    b_v = sp.Matrix([0, 1, 3])
    Mblk = 2 * (a_v * a_v.T - b_v * b_v.T)
    npb = nnb = nzb = 0
    for ev, mult in Mblk.eigenvals().items():
        s = sp.sign(ev)
        npb, nnb, nzb = (npb + (mult if s > 0 else 0),
                         nnb + (mult if s < 0 else 0),
                         nzb + (mult if s == 0 else 0))
    check("G12-pairblock-inertia-exact",
          (npb, nnb, nzb) == (1, 1, 1),
          "vv^T + conj(v)conj(v)^T = 2(aa^T - bb^T) exact inertia "
          "(%d, %d, %d) == (1, 1, 1): the off-line signature-(1,1)"
          " block == the Sylvester pull-back mechanism of our "
          "r229 census" % (npb, nnb, nzb))
    p_cnt = sum(1 for w in R261_WS if w > 0)
    q_cnt = sum(1 for w in R261_WS if w < 0)
    ok13 = True
    census = []
    wall_n = None
    for n in range(1, len(R261_XS) + 1):
        npn, nnn, nz = hankel_inertia_exact(R261_XS, R261_WS, n)
        census.append((n, npn, nnn))
        ok13 = ok13 and nz and (npn <= p_cnt) and (nnn <= q_cnt)
        if nnn == 0:
            wall_n = n
    npS, nnS = census[-1][1], census[-1][2]
    ok13 = ok13 and (nnS == q_cnt) and (npS == p_cnt)
    check("G13-r261-inertia-census-exact", ok13,
          "r261 MAINLIKE (p = %d, q = %d): exact leading minors "
          "all nonzero (Jacobi rule valid), n_+(H_n) <= p and "
          "n_-(H_n) <= q at every degree; SHARP at full degree "
          "(n_-(H_6) = %d == q, n_+(H_6) = %d == p); positive-"
          "definite prefix to n = %s (half-filling ceil(S/2) = 3 "
          "-- toy location printed, no law gate); census %s"
          % (p_cnt, q_cnt, nnS, npS, wall_n, census))

    # ---------------- S3 LEG C: the import test on our windows
    section("S3  LEG C -- IMPORT TEST ON OUR WINDOW OBJECTS")
    packs = {kz: BH.wpack(kz) for kz in MAIN_WINDOWS}
    rr9 = PIK.build_rung(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okC = (all(packs[kz]["nf"] is None for kz in MAIN_WINDOWS)
           and all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl))
    check("G14-census", okC,
          "mains POSITIVE_PREFIX at full depth (N = %s); control "
          "flips re-derived %s == sealed %s"
          % ({kz: packs[kz]["N"] for kz in MAIN_WINDOWS},
             {c: ctrl[c]["nf"] for c in ctrl}, CTRL_FLIPS))

    gs9 = gram_split(packs[9])
    wb9 = CT.world_block(packs[9])
    sgn, lgd = np.linalg.slogdet(gs9["G"])
    ward = abs(lgd - wb9["lg"][gs9["N"]]) / (1.0 + abs(
        wb9["lg"][gs9["N"]]))
    check("G15-basis-ward-w9", (sgn == wb9["sg"][gs9["N"]]
                                and ward <= W9_WARD_BAR),
          "our Gram == r257 world_block basis convention: slogdet "
          "sign %+d == %+d, log|det| rel dev %.1e <= %.0e"
          % (int(sgn), int(wb9["sg"][gs9["N"]]), ward,
             W9_WARD_BAR))

    worlds = [("MAIN9", gram_split(packs[9])),
              ("MAIN13", gram_split(packs[13]))]
    worlds += [(c, gram_split(ctrl[c])) for c in
               ("EPST", "SCR", "SMOOTH")]
    vals = {}
    ok16 = ok17 = True
    for name, gsw in worlds:
        v = import_values(gsw)
        vals[name] = (gsw, v)
        ok16 = ok16 and v["rt_ok"]
        ok17 = ok17 and v["cs_ok"]
        info("%-7s N %4d S %4d (p %4d / q %4d)  trG %+.3e  "
             "HS2 %.3e  n+ %4d n- %3d  f_CS %.4f  f_RT %.4f  "
             "true n+/N %.4f"
             % (name, gsw["N"], gsw["S"], gsw["p"], gsw["q"],
                v["trG"], v["hs2"], v["npos"], v["nneg"],
                v["f_cs"], v["f_rt"], v["true_frac"]))
    check("G16-ranktrace-validity", ok16,
          "rank GP >= 2trGP + 4trGQ - ||G||_HS^2 holds on every "
          "window/world (theorem sanity on the (GP, GQ) split)")
    check("G17-cs-validity-vs-eigh", ok17,
          "n_+(G) >= (trG)^2/||G||_HS^2 vs eigh count on every "
          "window/world (theorem sanity, scale-invariant)")

    if smoke:
        ladder_f = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        lpacks = [BH.wpack(kz) for kz in kzs]
        lpacks.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(lpacks) == LADDER_EXPECT
               and all(p["nf"] is None for p in lpacks))
        ladder_f = []
        for p in lpacks:
            v = import_values(gram_split(p))
            ladder_f.append(v["f_import"])
    f_m9 = vals["MAIN9"][1]["f_import"]
    f_m13 = vals["MAIN13"][1]["f_import"]
    if ladder_f:
        med = float(np.median(ladder_f))
        go = (f_m9 >= GO_BAR and f_m13 >= GO_BAR and med >= GO_BAR
              and okL)
        lad_msg = ("ladder %d rungs f_import min/med/max "
                   "%.4f/%.4f/%.4f"
                   % (len(ladder_f), min(ladder_f), med,
                      max(ladder_f)))
    else:
        med = None
        go = (f_m9 >= GO_BAR and f_m13 >= GO_BAR)
        lad_msg = "ladder SKIPPED (smoke); GO from mains only"
    import_verdict = ("IMPORT_CERTIFICATE_GO(f9 %.4f, f13 %.4f%s)"
                      % (f_m9, f_m13, (", med %.4f" % med)
                         if med is not None else "")) if go else \
        ("NO_IMPORT(FRAME_MISMATCH; f9 %.4f, f13 %.4f%s)"
         % (f_m9, f_m13, (", med %.4f" % med)
            if med is not None else ""))
    check("G18-import-adjudication", True,
          "sealed GO rule (bar %.2f both mains + ladder median): "
          "%s; %s" % (GO_BAR, import_verdict, lad_msg))

    truef = [vals[n][1]["true_frac"] for n in
             ("MAIN9", "EPST", "SCR", "SMOOTH")]
    csf = [vals[n][1]["f_cs"] for n in
           ("MAIN9", "EPST", "SCR", "SMOOTH")]
    spread_t = max(truef) - min(truef)
    spread_c = max(csf) - min(csf)
    blind = spread_c < SEP_FACTOR * spread_t
    sep_verdict = "TWO_MOMENT_BLIND" if blind else \
        "TWO_MOMENT_SEES_WALL"
    check("G19-separation-test", True,
          "sealed rule spread(f_CS) %.4f vs %.2f x spread(true "
          "n+/N) %.4f => %s (true fractions MAIN/EPST/SCR/SMOOTH "
          "= %s; f_CS = %s)"
          % (spread_c, SEP_FACTOR, spread_t, sep_verdict,
             ["%.4f" % t for t in truef],
             ["%.4f" % c for c in csf]))

    frame_msgs = []
    ok20 = True
    for name in ("MAIN9", "MAIN13"):
        gsw, v = vals[name]
        an = gsw["anorm"][gsw["anorm"] > 0]
        spread_dec = math.log10(float(np.max(an))
                                / float(np.min(an)))
        aspect = gsw["S"] / float(gsw["N"])
        ok20 = ok20 and np.isfinite(spread_dec) and v["hs2"] > 0
        frame_msgs.append("%s: aspect S/N %.3f (theirs 1), atom-"
                          "norm spread %.1f dec (theirs 0: uniform"
                          " frame bound), R_ours %.3e (theirs "
                          "4/3)" % (name, aspect, spread_dec,
                                    v["r_ours"]))
    check("G20-frame-gap-census", ok20,
          "the q1 structural gap measured -- " +
          "; ".join(frame_msgs))

    # ---------------- S4 LEG D: ceiling + inertia crosswalk
    section("S4  LEG D -- CEILING + INERTIA CROSSWALK (TYPED)")
    check("G21-ceiling-location-crosswalk", True,
          "LOCATION: their binding constraint (%s) sits exactly "
          "where our PAIRCORR kill rule fires -- the r263 record "
          "demand on the SAME missing input is %.2f/%.2f/%.2f dec "
          "(min/med/max root-scale comb cancellation over the 42-"
          "rung ladder): the external ceiling is the FIRST PROVEN "
          "form of our measured wall, for THEIR certificate "
          "class; SCOPE: their ceiling theorem quantifies ONLY "
          "over bandwidth-one two-moment certificates -- our "
          "coordinate (full comb chain, bordered terminal scalar "
          "Z_w) is outside that class, so their ceiling does NOT "
          "close our lane and their theorem does NOT bound our "
          "objects" % ((EXT["CEIL_LOCATION"],) + R263_DEMAND_DEC))
    check("G22-inertia-crosswalk", True,
          "SAME_MECHANISM: their Lemma 3.1 (inertia under pull-"
          "back) == our r229 Pontryagin census engine (G12/G13 "
          "exact); OURS_EXACT_LOCAL: we hold the exact quasi-"
          "definiteness boundary + half-filling location (v956 "
          "N_w = ceil(S/2)) which their coarse count cannot see; "
          "THEIRS_QUANT_RANKTRACE: they add the trace/HS "
          "quantitative step (proportion from two moments) we "
          "never used -- imported and measured in leg C: %s"
          % import_verdict)

    # ---------------- S5 verdict
    section("S5  VERDICT")
    ext_ok = all(ok for nm, ok, _ in CHECKS if nm in
                 ("G3-R-psi0-quadrature", "G4-R-psiMT-quadrature",
                  "G5-certificate-arithmetic",
                  "G6-ordering-and-ceiling-gap"))
    verdict = " + ".join([
        "EXTERNAL_FORM_RECONSTRUCTED" if ext_ok else
        "EXTERNAL_FORM_BROKEN",
        "CEILING_IS_OUR_WALL(LOCATION: MV-diagonal/paircorr-"
        "support-1 boundary; theirs PROVEN for their class, ours "
        "MEASURED r262/r263)",
        "CEILING_ORTHOGONAL(SCOPE: bandwidth-one two-moment class "
        "does not contain our full-chain coordinate)",
        import_verdict,
        sep_verdict,
        "INERTIA_CROSSWALK(SAME_MECHANISM; OURS_EXACT_LOCAL, "
        "THEIRS_QUANT_RANKTRACE)",
        "SOURCE_NOTE(ENCL_INTERVAL_ARITHMETIC)",
    ])
    print("\nVERDICT: %s" % verdict, flush=True)

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    wall = time.time() - T0_WALL
    check("G23-runtime", wall <= RUNTIME_CAP,
          "wall %.1f s <= %.0f s" % (wall, RUNTIME_CAP))
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print("\nGATES: %d/%d PASS  (SPEC_SHA %s)  wall %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], wall), flush=True)
    print("AMENDMENTS AFTER FREEZE: NONE" if npass == len(CHECKS)
          else "GATE FAILURES PRESENT -- see above", flush=True)
    print("NO RH CLAIM IN EITHER DIRECTION.", flush=True)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
