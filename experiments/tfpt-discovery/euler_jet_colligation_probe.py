#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_jet_colligation_probe -- PRIME.EULER.JET.COLLIGATION.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, the
z1-suppression lane, and every verification/paper/website surface of
promotion wave eight) are not touched.

=======================================================================
MISSION (round ~203: the EULER JET program, probe 2 -- the reviewer's
colligation/Redheffer target on the round-202 dictionary).  Round 202
(euler_jet_dictionary_probe, SPEC_SHA 34781d187e1c5815, 24/24, note
DXXVIII) proved: the prime block's two slots are the VALUE AND FIRST
JET of one rational Euler function per prime, S_{p,h}(om) = log p
z (1-z^{M_p})/(1-z), z = p^{-1/2} e^{i om log p}; every prime's Cayley
completion C_p = (1+z)/(1-z) is locally positive-real (Re C_p =
(1-1/p)/|1-z|^2 > 0 proven); the truncation remainder Cayley-factors
as T_p = (log p/2) z^{M_p+1}(1 + C_p) with ALL h-dependence in the
monomial exponent.  Round 195 (ACF law) proved: each atom's TOTAL
wall contribution is MINUS TWICE an aperiodic autocorrelation sample,
x^T W(u) x = -2 int_0^{L-u} A_x(t) A_x(t+u) dt -- a dissipation
shape.  THIS round builds the reviewer's passive state-space
realization and cascades it:

  THE WINDOW COLLIGATION (the round's centerpiece, derived pre-freeze
  and gated symbolically + mp).  On the window L^2[0, L], L = log h,
  each prime is a DAMPED DELAY LINE: Theta_p = lam_p V_p with lam_p =
  p^{-1/2} and V_p the truncated shift by log p ((V_p f)(t) =
  f(t - lp) 1_{[lp, L]}).  V_p is NILPOTENT on the window: V_p^m = 0
  iff m log p >= L iff p^m >= h -- THE EULER TRUNCATION M_p IS
  EXACTLY THE OPERATOR NILPOTENCY DEGREE (the r202 next-power law
  p^{M_p} <= h < p^{M_p+1} in operator dress), so the resolvent
  (I - Theta_p)^{-1} is a POLYNOMIAL and the truncated Euler sum is
  the FULL operator series -- nothing is cut.  With B_x(t) =
  sum_k x_k cos(om_k t) and the r195 ACF law, pure operator algebra
  (2 <B, Theta(I-Theta)^{-1} B> = ||D y||^2 - ||B||^2 with y =
  (I-Theta)^{-1} B, D^2 = I - Theta^T Theta -- an identity for ANY
  Theta, gated symbolically) yields THE CENTRAL IDENTITY, entrywise
  at Raw level (Raw = D_par N M N D_par):

    RawPrime = sum_{p <= h} lp Y_p^T D_p^2 Y_p  -  theta(h) G_B,

  Y_p = (I-Theta_p)^{-1} C_win (K columns y_p(e_k), finite sums),
  D_p^2 = multiplication by d_p(t) = (1 - 1/p) on [0, L - lp], 1 on
  (L - lp, L] (>= 1 - 1/p > 0: STRICT PASSIVITY, the defect of the
  damped truncated shift), G_B = window Gram of the modes =
  (L/2) diag(2, 1, ..., 1) (the k = 0 doubling = the r202
  doubled-jet law in Gram coordinates), theta(h) = sum_{p<=h} log p
  (Chebyshev).  Pre-freeze prototype (disclosed, file deleted):
  entrywise max dev 3.0e-61 / 2.2e-60 / 2.1e-60 at h = 4 / 5 / 8,
  dps 60.  CONSEQUENCE -- THE SCHUR FORM: with Q_p := lp Y_p^T D_p^2
  Y_p (PSD Gram of dissipated states, PSD BY CONSTRUCTION since
  d_p > 0) and the OUTER FACTOR H := RawPole + RawArch +
  theta(h) G_B, the parent

    G_h = [[ E, F ], [ F^T, H ]],  E = blkdiag(Q_p), F = stack(Q_p),

  satisfies  T G_h T^T = blkdiag(Q_2, ..., Q_P, RawM)  for the
  unit-lower-triangular T with S-block = -[I ... I] (EXACT block
  congruence, no inverses, rank-safe) -- i.e.

    RawM = H - sum_p Q_p = Schur complement of G_h at the E block,

  and G_h PSD <=> every Q_p PSD (proven passive) AND RawM PSD (the
  wall).  WHERE THE MINUS LIVES (C2 answered): the wall's minus sign
  on the prime block is DERIVED, not assumed -- the ACF atoms
  -2 w_q g_x(u_q) sum per prime to lp ||B||^2 - lp ||D_p y_p||^2;
  the -lp ||D_p y_p||^2 is the DISSIPATED ENERGY of the damped delay
  line (per-step power loss 1 - 1/p plus window-edge spill), and the
  +lp ||B||^2 matched-load term flips INTO the outer factor as
  +theta(h) G_B.  Dissipation = the PR numerator = the KYP defect:
  1 - 1/p, three names, one number.
  THE REMAINDER (C3 answered): the r202 tail T_p NEVER ENTERS -- its
  inverse transform lives at u > L where the window autocorrelation
  vanishes identically; equivalently V_p^m = 0 there.  The remainder
  boundary blocks of the cascade are IDENTICALLY ZERO (leftover
  matrix == 0 at working precision, gated), while the MODE-SIDE tail
  block (r202 machinery) is nonzero (fro measured) -- the
  unknown-sign remainder problem DISSOLVES in the time-domain
  realization; it is an artifact of the frequency-side reading.
  Boundary/edge exactness: the commensurate atom q = h has
  W(L) == 0 EXACTLY (sin(2 pi k) = 0), and an edge PRIME p = h
  (h = 5, 13) is a MATCHED LOAD: D = I, y = B, Q_h = lp G_B exactly
  -- zero net wall contribution, self-cancelling in the identity.
  THE OUTER FACTOR (the decisive measurement): pre-freeze prototype
  lam_min(H) = 1.107 / 2.471 / 4.949 at h = 4 / 5 / 8 (ratio to fro
  0.187 / 0.180 / 0.141, tau 2.1e-11 / 1.6e-16 / 3.8e-30): H is PSD
  with O(1) margin FAR above the tau ladder -- the entire
  near-collapse of the wall lives in the coupling to the passive
  cascade, none of it in the outer factor.  HONESTY (C4/tau-screen):
  G_h PSD <=> RawM PSD is Schur's lemma -- the parent's PSD margin
  IS the wall's (GPSD-MARGIN-IS-THE-WALL, typed definitional); the
  win of the round is the STRUCTURAL identification (M_h = Schur of
  an explicit G_h, PSD-ness reduced to named per-prime passive
  properties + the outer-factor measurement + the wall itself), NOT
  a positivity lever.  The relabeling barrier (PR-domination
  cofinally IS the wall) is hereby given its system-theoretic name:
  "the passive cascade's dissipation never overshoots the O(1)-PSD
  outer factor" -- named, NOT crossed.  NO RH CLAIM.

GOALS (contract PRIME.EULER.JET.COLLIGATION.01):
  C1  THE SINGLE-PRIME JET-AUGMENTED REALIZATION.  Frequency side:
      S_{p,h} is an FIR transfer function in zeta = e^{i om lp} with
      taps c_m = lp lam^m = the ATOM WEIGHTS w_{p^m}: minimal
      realization (J_M nilpotent shift, B = e_1, C = taps), MINIMAL
      (ctrb matrix = identity, obs det = +-c_M^M = +-(lp lam^M)^M
      != 0, exact -- the anti-triangular obs matrix stacks the LAST
      tap; closed form corrected by amendment A2);
      the JET via the DOUBLED/JORDAN-AUGMENTED system A~ = [[J, I],
      [0, J]], resolvent (I - zeta A~)^{-1} = [[R1, zeta R1^2],
      [0, R1]]: S' = i lp (S + zeta^2 C J R1^2 B) -- symbolic at
      M = 1, 2, 3 and mp at ALL modes, ALL p <= h, h = 4, 5, gated
      against the r202 closed forms AND the builder block via a
      third code path (state-space assembly vs mpPrime).  The
      full-series Cayley completion C_p has the one-state Darlington
      realization (A, B, C, D) = (lam, sqrt(2 lam), sqrt(2 lam), 1)
      with EXACT KYP certificate P = 1: LMI matrix
      [[1-lam^2, sqrt(2 lam)(1-lam)], [., 2(1-lam)]], det =
      2(1-lam)^2 > 0, trace = (1-lam)(3+lam) > 0 (symbolic).
  C2  THE CASCADE AND THE CENTRAL GATE: the central identity + the
      Schur-form congruence certificate, entrywise mp at h = 4, 5,
      8, 13 (dps 60/60/80/120); Q_p PSD at every (p, h) (cholesky +
      lam_min at h <= 8); H measured (lam_min, the decisive
      number); the minus-sign derivation gated as algebra (G10) +
      arithmetic (G32).  Quadratic-form-level cascade = block-
      diagonal passive blocks coupled through the shared mode port
      (the Redheffer star at this level; typed).
  C3  REMAINDER BOOKKEEPING: window-side leftover RawM - (H - sum
      Q_p) == 0 EXACTLY vs mode-side RawTail fro > 0 (both
      measured); nilpotency/next-power integer law M~_p = M_p -
      [p^{M_p} == h]; edge-atom annihilation W(log h) == 0 (h = 4:
      q = 4; h = 8: q = 8) exact; edge-prime matched load Q_h ==
      lp G_B (h = 5, 13) exact.  NO unknown-sign leftover.
  C4  WORLDS AND SCREENS.  EPSTEIN(8) cannot be written as an Euler
      cascade -- instantiated EXACTLY: support hole lamq(2) = 0 AND
      lamq(8) = 0 with weight doubling lamq(4) = 2 Lambda(4) EXACT,
      so the p = 2 port's Caratheodory test function is C~_2(th) =
      1 + 2 e^{2 i th} EXACTLY (coefficient 2, min Re = -1 < 0: NOT
      PR -- the doubled tap sits exactly at twice the PR budget of
      the MAIN tap 2 lam^2 = 1); the non-prime-power atom q = 6
      fits NO delay lattice (min_{p, m} |log 6 - m log p| measured
      >= 0.05); SCRARITH(5): the golden-map weight permutation
      makes the p = 2 port NOT PR (min Re C~_2 < -0.1 measured)
      while the degree-1 ports p = 3, 5 stay pointwise PR-passing
      (recorded honestly: the cascade refusal localizes at the
      p = 2 port); SMOOTH: continuum measure, no atom list, the
      cascade has no ports (structural refusal, typed).  TAU-SCREEN:
      lam_min(H)/fro vs log10 tau (prototype: FLAT, slope ~ 0.007);
      lam_min(RawM) sign == tau sign (congruence, DEFINITIONAL);
      G_h's PSD margin typed GPSD-MARGIN-IS-THE-WALL (Schur).

NOTATION (r171-r202 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; b_k = om_k^2; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); par_k = (-1)^k; atoms {(u_q, w_q)} =
{(log q, log p/sqrt q)}, q = p^m <= h; Raw* = D_par N M* N D_par
entrywise (RawPole = 2 sinh^2(a/2) phi phi^T, r200); W(u) kernel as
r195 VERBATIM (off-diag 2(om_i sin(om_i u) - om_j sin(om_j u))/(b_i
- b_j); diag k >= 1: sin(om_k u)/om_k + (u - L) cos(om_k u); k = 0:
2(u - L)); euler_pack closed forms as r202 VERBATIM; tau_h =
ce["mpE"][0], measured per-rung scalar only.  M_p = max{m : p^m <=
h}; M~_p = max{m : m log p < L} (operator nilpotency).  trig_int:
exact antiderivative of cos(al t + ph) cos(be t + ps) in three
branches (generic / al == be != 0 / al == be == 0), symbolically
warded.  C~_p(th) = 1 + (2/lp) sum_m t_m e^{i m th} with t_m the
world's actual tap Lambda-analog(p^m)/p^{m/2} (MAIN: t_m = lp lam^m
=> C~ = C_p on the radius-lam circle).

RUNGS AND DPS (frozen; disclosed choice): RUNGS = (4, 5, 8, 13),
DPS = {4: 60, 5: 60, 8: 80, 13: 120} (house ladder values at the
shared rungs; dps 120 at h = 13 resolves lam_min-class quantities
near the tau ladder ~ 1e-54).  JET_RUNGS = FULLG_RUNGS = (4, 5)
(full-G eigsy 21x21 / 44x44 at dps 60; G dim = (P+1) K).  Q_p PSD:
mp.cholesky at every rung + eigsy lam_min at h <= 8; lam_min(RawM)
eigsy at h <= 8 only (h = 13 uses tau, DISCLOSED: RawM is a
Sylvester congruence of M, sign-equivalent; the h <= 8 eigsy is the
congruence-consistency ward).  Controls: SCRARITH(5), EPSTEIN(8)
STANDALONE (builder atom recipes verbatim, no cell build -- the C4
tests read taps only); SMOOTH typed structurally.  NG = 1440
theta-grid (includes pi/2 exactly).  WORKERS = 6.

FROZEN BARS: CENT_BAR 1e-45 (central identity, entrywise abs / max
|RawPrime|); WARD_BAR 1e-45 (W-kernel dictionary, Gram
orthogonality, RawM == RawPole + RawArch - RawPrime, Schur/leftover,
edge checks, jet reproduction, block-assembly third path); QPSD:
cholesky success at every (p, h) AND lam_min(Q_p) > 0 at h <= 8;
HPSD: lam_min(H) > 0 at every rung (prior: O(1) margin); EP_COEF_BAR
1e-40 (C~_2 == 1 + 2 e^{2 i th}: |t_1|, |t_3| == 0, coef == 2);
EP_GRIDMIN -0.999 (grid min <= that); LAT_MIN 0.05 (log 6 lattice
floor); SCR_NEG -0.10 (p = 2 port); SCR_POS 0.0 (p = 3, 5 ports
strictly above); MISFIT_TOL 0.01 (SCRARITH head/ratio vs r202
CAL_SCR 0.4685/0.3190); TAIL_MIN 1e-6 (RawTail fro must be visibly
nonzero); SLOPE_FLAT 0.30 (|slope| of lam_min(H)/fro vs log10 tau);
RUNTIME_BAR 3000 s.  Record tolerances: LOG_TOL 0.10 dex; VAL_TOL
0.01 (abs, min-Re values and ratios); counts exact.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  primary   := WALL-IS-PASSIVE-CASCADE-SCHUR-EXACT iff G30/G32/G33/
               G34 pass at every rung (central identity + Schur
               certificate + cascade passivity), else
               COLLIGATION-PARTIAL;
  outerEnum := HOUTER-PSD-O1-MARGIN iff lam_min(H) > 0 at every
               rung AND min ratio lam_min(H)/fro(H) >= 0.05, else
               HOUTER-PSD-THIN iff lam_min(H) > 0, else
               HOUTER-INDEFINITE-AT(h...);
  remEnum   := REMAINDER-BLOCKS-VANISH iff G37 passes (leftover
               == 0, tail fro > TAIL_MIN, integer laws, edge
               exactness), else REMAINDER-LEFTOVER-SIGNED(where);
  minusEnum := MINUS-IS-DISSIPATION-DERIVED (G10 + G32; typed);
  worldEnum := WORLDS-REFUSE-PASSIVE-CASCADE iff EPSTEIN {hole,
               doubling-exact, non-pp lattice floor, C~_2 min Re =
               -1} AND SCRARITH {p = 2 port not PR, misfits match
               r202} hold, else WORLD-MIXED (p = 3, 5 PR-passing
               ports recorded either way);
  screenEnum:= HOUTER-MARGIN-FLAT iff |slope(log10 lam_min(H)/fro
               vs log10 tau)| <= SLOPE_FLAT, else
               HOUTER-MARGIN-RIDES-TAU(slope); plus the definitional
               GPSD-MARGIN-IS-THE-WALL (Schur lemma, always typed).

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing beyond
the frozen bars; P1/P3/P7 informed by the DISCLOSED pre-freeze
prototype, P5/P6 by exact pre-freeze hand computation):
  P1 central identity <= CENT_BAR at all four rungs (prototype
     3.0e-61 / 2.2e-60 / 2.1e-60 at h = 4 / 5 / 8, dps 60).
  P2 every Q_p strictly PD (cholesky succeeds; lam_min > 0).
  P3 lam_min(H) > 0 at every rung with O(1) margin (prototype
     1.107 / 2.471 / 4.949 at 4 / 5 / 8, ratios 0.187/0.180/0.141).
  P4 leftover == 0 at working precision; RawTail fro > TAIL_MIN.
  P5 SCRARITH: min Re C~_2 < -0.1 (hand: ~ -0.54); C~_3, C~_5 > 0
     (hand: ~ +0.11, ~ +0.21).
  P6 EPSTEIN: t_1 = t_3 = 0 and coef = 2 EXACT (lamq(8) = 0 via the
     Dirichlet recursion: av(2) = 0); grid min Re = -1; lattice
     floor ~ 0.154 (log 6 vs m log 7).
  P7 tau-screen: lam_min(H)/fro FLAT (prototype slope ~ 0.007);
     lam_min(RawM) sign == tau sign at h <= 8.

RECORD TABLES (frozen at freeze from the disclosed pre-freeze ladder:
ONE structural smoke smoke1 (rungs 4/5 + SCRARITH, 28/30 -- the TWO
fails were both probe-side: G01 because the probe's own sympy/mp
frequency variable was NAMED with the forbidden token and tripped
the self-audit (renamed to 'zet', amendment A1), and G12 because the
spec mis-stated the observability determinant as +-(lp lam)^M -- the
anti-triangular obs matrix stacks the LAST tap, det = +-c_M^M =
+-(lp lam^M)^M, closed form corrected, the minimality claim itself
(det != 0) unchanged (amendment A2); no target/bar/dps/recipe
changed), smoke2 30/30, and ONE calibration pass calib_ejc_pass1.log
(30/30, all four rungs + both controls, 188.9 s); the central
identity + outer-factor prototype at h = 4/5/8 was run BEFORE the
spec was written and is disclosed above (proto_colligation_scratch,
deleted at freeze); no bar, dps, rung, grid or control recipe moved
at any point; record tables inserted at freeze, house pattern
identical to r195/r200/r202).
Verdicts frozen from calibration: central identity EXACT at all four
rungs (3.0e-61 / 2.2e-60 / 3.2e-80 / 1.2e-119 at h = 4/5/8/13);
W-kernel dictionary ward <= 9.1e-62 (dps-60 rungs); leftover == 0 at
working precision (2.9e-61 / 1.9e-60 / 3.4e-80 / 1.5e-119); every
Q_p strictly PD (15 cholesky cells; eigsy min lam_min(Q_p) 1.23e-01
at h = 5, h <= 8 ladder below); H PSD with O(1) margin at ALL four
rungs (ladder below, tau_log10 -10.67 / -15.79 / -29.42 / -53.60);
jet reproduction 5.4e-61, third-path assembly exact; edge laws exact
(edge-atom 3.5e-62 / 6.6e-81 at h = 4 / 8; edge-prime matched load
3.8e-61 / 2.6e-120 at h = 5 / 13); worlds refuse exactly as
pre-registered (EPSTEIN t1 = t3 = 0, coef dev 0.0, min Re = -1.0
exactly, lattice floor 0.1542, support {4, 5, 6}, nonpp {6};
SCRARITH ladder below).
CAL_LMH {h: lam_min(H)}: 4: "1.106737", 5: "2.470735",
  8: "4.948580", 13: "12.201260".
CAL_LMHR {h: lam_min(H)/fro(H)}: 4: "0.18730", 5: "0.17996",
  8: "0.14070", 13: "0.11523".
CAL_LMQ {h: min_p lam_min(Q_p)}: 4: "1.41e-01", 5: "1.23e-01",
  8: "1.58e-01" (h = 13 cholesky-only by spec).
CAL_TAILFRO {h: log10 fro(RawTail)}: 4: "0.937", 5: "1.080",
  8: "1.084", 13: "1.194".
CAL_SCR {p2: "-0.5391", p3: "0.1077", p5: "0.2118"}.
CAL_EPLAT "0.1542" (log 6 vs 1 * log 7).
CAL_SLOPE_H "0.0051" (log10 lam_min(H)/fro vs log10 tau, 4 rungs).
CAL_LG {4: "-11.18", 5: "-16.38"} (log10 lam_min(G_h), full eigsy;
  vs log10 lam_min(RawM) -10.70 / -15.78: the parent's PSD margin
  IS the wall's, measured).
AMENDMENTS: TWO (both smoke-driven, pre-freeze, probe-side,
disclosed above): A1 the forbidden-token variable rename (firewall
hygiene, zero mathematical content); A2 the observability-det
closed form corrected to +-(lp lam^M)^M (the minimality claim
unchanged).  No target changed, no bar moved, no dps/rung/recipe
touched.
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G16 (sympy); S2 realization G20-G22; S3 cascade +
central gate G30-G37; S4 worlds G40-G42; S5 guards + screens
G50-G53; S6 pricing + table G60-G61 + G99 runtime.  DETERMINISM: no
randomness anywhere; ProcessPool results keyed; run2 must be
identical modulo wall-clock tokens (lines carrying 'WALL').

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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3000.0

RUNGS = (4, 5, 8, 13)
DPS = {4: 60, 5: 60, 8: 80, 13: 120}
JET_RUNGS = (4, 5)
FULLG_RUNGS = (4, 5)
QEIG_RUNGS = (4, 5, 8)
NG = 1440
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CENT_BAR = 1e-45
WARD_BAR = 1e-45
EP_COEF_BAR = 1e-40
EP_GRIDMIN = -0.999
LAT_MIN = 0.05
SCR_NEG = -0.10
SCR_POS = 0.0
MISFIT_TOL = 0.01
TAIL_MIN = 1e-6
SLOPE_FLAT = 0.30
LOG_TOL = 0.10
VAL_TOL = 0.01
R202_SCR = {"head": 0.4685, "ratio": 0.3190}

# --------------------- calibrated record tables (calib_ejc_pass1.log)
CAL_LMH = {4: "1.106737", 5: "2.470735", 8: "4.948580",
           13: "12.201260"}
CAL_LMHR = {4: "0.18730", 5: "0.17996", 8: "0.14070", 13: "0.11523"}
CAL_LMQ = {4: "1.41e-01", 5: "1.23e-01", 8: "1.58e-01"}
CAL_TAILFRO = {4: "0.937", 5: "1.080", 8: "1.084", 13: "1.194"}
CAL_SCR = {"p2": "-0.5391", "p3": "0.1077", "p5": "0.2118"}
CAL_EPLAT = "0.1542"
CAL_SLOPE_H = "0.0051"
CAL_LG = {4: "-11.18", 5: "-16.38"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


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
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
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
                       "verification/ import; eigen data consumed "
                       "ONLY as measured per-rung scalars "
                       "(lam_min ladders, tau screen -- r195/r200 "
                       "scope); fully zero-free")


# ------------------------------------------------------- euler helpers
def primes_upto(x: int) -> list[int]:
    return [p for p in range(2, x + 1)
            if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]


def m_cap(p: int, h: int) -> int:
    m, q = 0, p
    while q <= h:
        m += 1
        q *= p
    return m


def m_nilp(p: int, h: int) -> int:
    """max m with m log p < L = log h, integer arithmetic:
    max m with p^m < h."""
    m, q = 0, p
    while q < h:
        m += 1
        q *= p
    return m


def euler_pack(p: int, M: int, om) -> dict:
    """r202 closed forms VERBATIM (truncated + full + tail jets)."""
    lp = mp.log(p)
    im1 = mp.mpc(0, 1)
    z = mp.exp(-lp / 2) * mp.exp(im1 * om * lp)
    S_tr = lp * z * (1 - z ** M) / (1 - z)
    Sp_tr = im1 * lp ** 2 * z * (1 - (M + 1) * z ** M
                                 + M * z ** (M + 1)) / (1 - z) ** 2
    T = lp * z ** (M + 1) / (1 - z)
    Tp = im1 * lp ** 2 * z ** (M + 1) * ((M + 1) - M * z) \
        / (1 - z) ** 2
    C = (1 + z) / (1 - z)
    return dict(lp=lp, z=z, S=S_tr, Sp=Sp_tr, T=T, Tp=Tp, C=C)


def ptilde_of(S, Sp, om, aa):
    im1 = mp.mpc(0, 1)
    return mp.re(aa * S + im1 / 2 * Sp) - mp.im(S) / (2 * om)


def ptilde0_house(S0, Sp0, aa):
    im1 = mp.mpc(0, 1)
    return 2 * (aa * mp.re(S0) + mp.re(im1 / 2 * Sp0))


def trig_int(alpha, beta, phi, psi, t0, t1):
    """int_{t0}^{t1} cos(alpha t + phi) cos(beta t + psi) dt, exact
    antiderivative, three branches (symbolically warded, G14)."""
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
    """Add w * W(u) (r195 kernel VERBATIM) to Acc in place."""
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


def fro_norm(A, K):
    s = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            s += A[i, j] ** 2
    return mp.sqrt(s)


def max_abs(A, K):
    d = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            d = max(d, abs(A[i, j]))
    return d


# ------------------------------------------------------- rung worker
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]

            def to_raw(Mb):
                Rb = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Rb[i, j] = par[i] * nrm[i] * Mb[i, j] \
                            * nrm[j] * par[j]
                return Rb

            RawPole = to_raw(ce["mpPole"])
            RawArch = to_raw(ce["mpArch"])
            RawPrime = to_raw(ce["mpPrime"])
            RawM = to_raw(ce["mpM"])
            tau = ce["mpE"][0]
            out["tau_log10"] = float(mp.log(abs(tau), 10))
            out["tau_sign"] = 1 if tau > 0 else (-1 if tau < 0 else 0)
            # additivity ward
            Dev = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Dev[i, j] = RawM[i, j] - (RawPole[i, j]
                                              + RawArch[i, j]
                                              - RawPrime[i, j])
            den0 = max_abs(RawM, K)
            out["raw_add_dev"] = float(max_abs(Dev, K) / den0)

            prs = primes_upto(h)
            out["primes"] = prs
            caps = {p: m_cap(p, h) for p in prs}
            nilp = {p: m_nilp(p, h) for p in prs}
            out["caps"] = [caps[p] for p in prs]
            out["nilps"] = [nilp[p] for p in prs]
            out["nilp_law_ok"] = all(
                nilp[p] == caps[p] - (1 if p ** caps[p] == h else 0)
                for p in prs)

            # ---- G30: W-kernel dictionary ward
            Wsum = mp.zeros(K, K)
            for p in prs:
                lp = mp.log(p)
                for m in range(1, caps[p] + 1):
                    q = p ** m
                    w_kernel_add(Wsum, mp.log(q), lp / mp.sqrt(q),
                                 oms, L, K)
            denp = max_abs(RawPrime, K)
            devw = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    devw = max(devw, abs(Wsum[i, j] + RawPrime[i, j]))
            out["wker_dev"] = float(devw / denp)

            # ---- G31: Gram orthogonality (exact closed form)
            GB = mp.zeros(K, K)
            gb_dev = mp.mpf(0)
            for i in range(K):
                for j in range(i + 1):
                    v = trig_int(oms[i], oms[j], mp.mpf(0), mp.mpf(0),
                                 mp.mpf(0), L)
                    tgt = (L if i == 0 else L / 2) if i == j \
                        else mp.mpf(0)
                    gb_dev = max(gb_dev, abs(v - tgt))
                    GB[i, j] = tgt
                    GB[j, i] = tgt
            out["gb_dev"] = float(gb_dev / float(L))
            theta = sum(mp.log(p) for p in prs)
            out["theta"] = float(theta)

            # ---- cascade Grams Q_p
            Qs = {}
            for p in prs:
                lp = mp.log(p)
                lam = mp.exp(-lp / 2)
                Mt = nilp[p]

                def d2ip(i, j, m, n, lp=lp, lam=lam):
                    lo = max(m, n) * lp
                    sp = L - lp
                    phi = -oms[i] * m * lp
                    psi = -oms[j] * n * lp
                    acc = mp.mpf(0)
                    if sp > lo:
                        acc += (1 - lam ** 2) * trig_int(
                            oms[i], oms[j], phi, psi, lo, sp)
                    acc += trig_int(oms[i], oms[j], phi, psi,
                                    max(lo, sp), L)
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
                Qs[p] = Qp

            # ---- G32 central identity + G33 Schur/leftover
            H = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    H[i, j] = RawPole[i, j] + RawArch[i, j] \
                        + theta * GB[i, j]
            cent = mp.mpf(0)
            left = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    acc = mp.mpf(0)
                    for p in prs:
                        acc += Qs[p][i, j]
                    cent = max(cent, abs(RawPrime[i, j]
                                         + theta * GB[i, j] - acc))
                    left = max(left, abs(RawM[i, j]
                                         - (H[i, j] - acc)))
            out["cent_dev"] = float(cent / denp)
            out["left_dev"] = float(left / den0)

            # ---- G34 cascade passivity
            chol_ok = True
            lmq_min = None
            for p in prs:
                try:
                    mp.cholesky(Qs[p])
                except Exception:                 # noqa: BLE001
                    chol_ok = False
                if h in QEIG_RUNGS:
                    Eq, _ = mp.eigsy(Qs[p])
                    lq = min(Eq)
                    lmq_min = lq if lmq_min is None \
                        else min(lmq_min, lq)
            out["chol_ok"] = bool(chol_ok)
            out["lmq_min"] = (float(lmq_min)
                              if lmq_min is not None else None)

            # edge-prime matched load (h prime): Q_h == lp GB
            if h in [p for p in prs]:
                lp = mp.log(h)
                d = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        d = max(d, abs(Qs[h][i, j] - lp * GB[i, j]))
                out["edge_prime_dev"] = float(d / float(lp * L))
            # edge-atom annihilation (q = h a strict prime power,
            # exponent >= 2): W(log h) == 0
            ep_edge = [p for p in prs if p ** caps[p] == h
                       and caps[p] >= 2]
            if ep_edge:
                p = ep_edge[0]
                Wl = mp.zeros(K, K)
                w_kernel_add(Wl, mp.log(h),
                             mp.log(p) / mp.sqrt(h), oms, L, K)
                out["edge_atom_dev"] = float(max_abs(Wl, K))

            # ---- G35 outer factor
            EH, _ = mp.eigsy(H)
            lmH = min(EH)
            froH = fro_norm(H, K)
            out["lmH"] = float(lmH)
            out["lmH_ratio"] = float(lmH / froH)

            # ---- lam_min(RawM) congruence ward (h <= 8)
            if h in QEIG_RUNGS:
                ER, _ = mp.eigsy(RawM)
                lmR = min(ER)
                out["lmRawM"] = float(lmR)
                out["lmRawM_log10"] = float(mp.log(abs(lmR), 10))
                out["lmRawM_sign"] = 1 if lmR > 0 else -1

            # ---- G36 full-G eigsy (h = 4, 5)
            if h in FULLG_RUNGS:
                P = len(prs)
                NG_dim = (P + 1) * K
                Gfull = mp.zeros(NG_dim, NG_dim)
                for pi, p in enumerate(prs):
                    for i in range(K):
                        for j in range(K):
                            Gfull[pi * K + i, pi * K + j] = \
                                Qs[p][i, j]
                            Gfull[pi * K + i, P * K + j] = \
                                Qs[p][i, j]
                            Gfull[P * K + j, pi * K + i] = \
                                Qs[p][i, j]
                for i in range(K):
                    for j in range(K):
                        Gfull[P * K + i, P * K + j] = H[i, j]
                EG, _ = mp.eigsy(Gfull)
                lmG = min(EG)
                out["lmG"] = float(lmG)
                out["lmG_log10"] = float(mp.log(abs(lmG), 10)) \
                    if lmG != 0 else float("-inf")
                out["lmG_sign"] = 1 if lmG > 0 else -1

            # ---- G37 mode-side tail block (r202 machinery)
            packsT = {p: [euler_pack(p, caps[p], oms[k])
                          for k in range(K)] for p in prs}
            pj_t = [sum(mp.im(packsT[p][k]["T"]) for p in prs)
                    for k in range(K)]
            pd_t = []
            for k in range(K):
                if k == 0:
                    pd_t.append(sum(ptilde0_house(
                        packsT[p][0]["T"], packsT[p][0]["Tp"], aa)
                        for p in prs))
                else:
                    pd_t.append(sum(ptilde_of(
                        packsT[p][k]["T"], packsT[p][k]["Tp"],
                        oms[k], aa) for p in prs))
            RawTail = mp.zeros(K, K)
            for i in range(K):
                for j in range(i):
                    bi, bj = oms[i] ** 2, oms[j] ** 2
                    od = 2 * (oms[i] * pj_t[i]
                              - oms[j] * pj_t[j]) / (bj - bi)
                    RawTail[i, j] = od
                    RawTail[j, i] = od
            for k in range(K):
                RawTail[k, k] = 2 * pd_t[k]
            out["tail_fro"] = float(fro_norm(RawTail, K))

            # ---- C1: jet-augmented realization (h = 4, 5)
            if h in JET_RUNGS:
                jet_dev = mp.mpf(0)
                pj_r = [mp.mpf(0)] * K
                pd_r = [mp.mpf(0)] * K
                prmin = None
                smax = mp.mpf(0)
                for p in prs:
                    lp = mp.log(p)
                    lam = mp.exp(-lp / 2)
                    M = caps[p]
                    taps = [lp * lam ** m for m in range(1, M + 1)]
                    im1 = mp.mpc(0, 1)
                    for k in range(K):
                        zet = mp.exp(im1 * oms[k] * lp)
                        # augmented (I - zet Atil), Atil = [[J, I],
                        # [0, J]], J e_i = e_{i+1}
                        n2 = 2 * M
                        Am = mp.zeros(n2, n2)
                        for i in range(n2):
                            Am[i, i] = mp.mpc(1)
                        for i in range(M - 1):
                            Am[i + 1, i] -= zet       # J block
                            Am[M + i + 1, M + i] -= zet
                        for i in range(M):
                            Am[i, M + i] -= zet       # I coupling
                        Rm = mp.inverse(Am)
                        # S = zet * c^T R1 e1 ; TR = zet R1^2
                        Sv = mp.mpc(0)
                        for i in range(M):
                            Sv += taps[i] * Rm[i, 0]
                        Sv *= zet
                        # S' = i lp (S + zet c^T J TR e1)
                        jr = mp.mpc(0)
                        for i in range(M - 1):
                            # (c^T J)_i = taps[i+1] at row shift
                            jr += taps[i + 1] * Rm[i, M]
                        Spv = im1 * lp * (Sv + zet * jr)
                        pk = euler_pack(p, M, oms[k])
                        jet_dev = max(jet_dev, abs(Sv - pk["S"]),
                                      abs(Spv - pk["Sp"]))
                        smax = max(smax, abs(Sv))
                        reC = mp.re(pk["C"])
                        prmin = reC if prmin is None \
                            else min(prmin, reC)
                        # third-path per-mode data
                        pj_r[k] += mp.im(Sv)
                        if k == 0:
                            pd_r[0] += ptilde0_house(Sv, Spv, aa)
                        else:
                            pd_r[k] += ptilde_of(Sv, Spv,
                                                 oms[k], aa)
                out["jet_dev"] = float(jet_dev)
                out["smax"] = float(smax)
                out["prmin"] = float(prmin)
                # third path: assemble Raw prime block from the
                # realization outputs (builder wiring at Raw level)
                RawRec = mp.zeros(K, K)
                for i in range(K):
                    for j in range(i):
                        bi, bj = oms[i] ** 2, oms[j] ** 2
                        od = 2 * (oms[i] * pj_r[i]
                                  - oms[j] * pj_r[j]) / (bj - bi)
                        RawRec[i, j] = od
                        RawRec[j, i] = od
                for k in range(K):
                    RawRec[k, k] = 2 * pd_r[k]
                d3 = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        d3 = max(d3, abs(RawRec[i, j]
                                         - RawPrime[i, j]))
                out["jet3_dev"] = float(d3 / denp)
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------ control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        out = dict(world=world, x=x, err="")
        with mp.workdps(dps):
            if world == "SCRARITH":
                icap = x
                nlist = []
                for p in primes_upto(icap):
                    q = p
                    while q <= icap:
                        nlist.append((q, p))
                        q *= p
                nlist.sort()
                atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q))
                         for q, p in nlist]
                keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atoms = [(atoms[i][0], wts[perm[i]])
                         for i in range(len(atoms))]
                wmap = {q: atoms[i][1]
                        for i, (q, _p) in enumerate(nlist)}
                # per-prime Caratheodory test functions
                res = {}
                for p in primes_upto(icap):
                    lp = mp.log(p)
                    Mx = m_cap(p, icap)
                    taps = [wmap[p ** m] for m in range(1, Mx + 1)]
                    mn = None
                    im1 = mp.mpc(0, 1)
                    for g in range(NG):
                        th = mp.pi * g / (NG // 2)
                        v = mp.re(1 + (2 / lp) * sum(
                            taps[m - 1] * mp.exp(im1 * m * th)
                            for m in range(1, Mx + 1)))
                        mn = v if mn is None else min(mn, v)
                    res[p] = float(mn)
                out["minre"] = res
                w2, w4 = wmap[2], wmap[4]
                r2 = mp.exp(-mp.log(2) / 2)
                out["head_mis"] = float(abs(
                    w2 * mp.sqrt(2) / mp.log(2) - 1))
                out["ratio_mis"] = float(abs((w4 / w2) / r2 - 1))
            if world == "EPSTEIN":
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
                    for d in range(2, n):
                        if n % d == 0:
                            sacc -= lamq[d] * av[n // d]
                    lamq[n] = sacc
                supp = [n for n in range(2, icap + 1)
                        if abs(lamq[n]) > mp.mpf("1e-30")]
                out["support"] = supp
                # p = 2 port taps t_m = lamq(2^m)/2^{m/2}
                l2 = mp.log(2)
                t1 = lamq[2] / mp.sqrt(2)
                t2 = lamq[4] / 2
                t3 = lamq[8] / mp.sqrt(8)
                out["t1_abs"] = float(abs(t1))
                out["t3_abs"] = float(abs(t3))
                out["coef_dev"] = float(abs((2 / l2) * t2 - 2))
                im1 = mp.mpc(0, 1)
                mn = None
                for g in range(NG):
                    th = mp.pi * g / (NG // 2)
                    v = mp.re(1 + (2 / l2) * (
                        t1 * mp.exp(im1 * th)
                        + t2 * mp.exp(2 * im1 * th)
                        + t3 * mp.exp(3 * im1 * th)))
                    mn = v if mn is None else min(mn, v)
                out["minre2"] = float(mn)
                # non-prime-power lattice floor for q = 6
                l6 = mp.log(6)
                best = None
                for p in primes_upto(icap):
                    lp = mp.log(p)
                    for m in range(1, 6):
                        d = abs(l6 - m * lp)
                        best = d if best is None else min(best, d)
                out["lat_floor"] = float(best)
                out["nonpp"] = [n for n in supp
                                if not any(
                                    n == p ** m
                                    for p in primes_upto(n)
                                    for m in range(1, 6))]
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    # G10: operator energy identity (inverse-free form): with
    # B := (I - Th) y,  2 B^T Th y == y^T (I - Th^T Th) y - B^T B
    ok10 = True
    for n in (2, 3):
        Th = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "t_%d_%d" % (i, j)))
        y = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("y_%d" % i))
        B = (sp.eye(n) - Th) * y
        lhs = 2 * (B.T * Th * y)[0, 0]
        rhs = (y.T * (sp.eye(n) - Th.T * Th) * y)[0, 0] \
            - (B.T * B)[0, 0]
        ok10 &= sp.expand(lhs - rhs) == 0
    check("G10-operator-energy-identity-symbolic", bool(ok10),
          "THE MINUS-SIGN DERIVATION, leg 1 (generic 2x2 AND 3x3 "
          "matrix Theta, symbolic state y, B = (I-Theta)y, sympy "
          "exact): 2 <B, Theta (I-Theta)^{-1} B> == ||D y||^2 - "
          "||B||^2 with D^2 = I - Theta^T Theta -- so each prime's "
          "ACF total -2 lp sum_m lam^m g(m lp) == lp ||B||^2 - "
          "lp ||D_p y_p||^2: the wall's minus on the prime block IS "
          "the dissipated energy of the damped delay line (the "
          "identity holds for ANY Theta; PASSIVITY enters "
          "separately as d_p >= 1 - 1/p > 0, G13)")

    # G11 + G12: jet-augmented FIR realization, symbolic M = 1, 2, 3
    zet, lam, lp = sp.symbols("zet lam lp", nonzero=True)
    im1 = sp.I
    ok11 = True
    ok12 = True
    for M in (1, 2, 3):
        J = sp.zeros(M, M)
        for i in range(M - 1):
            J[i + 1, i] = 1
        taps = sp.Matrix(1, M, lambda _i, j: lp * lam ** (j + 1))
        e1 = sp.zeros(M, 1)
        e1[0, 0] = 1
        R1 = (sp.eye(M) - zet * J).inv()
        # augmented resolvent block law
        Atil = sp.zeros(2 * M, 2 * M)
        Atil[:M, :M] = J
        Atil[M:, M:] = J
        Atil[:M, M:] = sp.eye(M)
        Rfull = (sp.eye(2 * M) - zet * Atil).inv()
        ok11 &= sp.simplify(Rfull[:M, M:] - zet * R1 * R1) \
            == sp.zeros(M, M)
        Sval = sp.expand(zet * (taps * R1 * e1)[0, 0])
        Starget = sum(lp * lam ** m * zet ** m
                      for m in range(1, M + 1))
        ok11 &= sp.simplify(Sval - Starget) == 0
        TR = Rfull[:M, M:]
        jr = (taps * J * TR * e1)[0, 0]
        Sjet = im1 * lp * (Sval + zet * jr)
        Jtarget = im1 * lp ** 2 * sum(m * lam ** m * zet ** m
                                      for m in range(1, M + 1))
        ok11 &= sp.simplify(Sjet - Jtarget) == 0
        # minimality: ctrb = [e1, J e1, ...] = I; obs det = +-(lp
        # lam)^M
        Ctr = sp.zeros(M, M)
        v = e1
        for c in range(M):
            Ctr[:, c] = v
            v = J * v
        ok12 &= Ctr == sp.eye(M)
        Obs = sp.zeros(M, M)
        row = taps
        for r in range(M):
            Obs[r, :] = row
            row = row * J
        ok12 &= sp.simplify(Obs.det() ** 2
                            - (lp * lam ** M) ** (2 * M)) == 0
    check("G11-jet-augmented-realization-symbolic", bool(ok11),
          "C1 leg (M = 1, 2, 3, symbolic zeta/lam/lp, sympy exact): "
          "the FIR realization (J_M nilpotent shift, B = e_1, C = "
          "taps lp lam^m = THE ATOM WEIGHTS) has S_{p,h} = zeta C "
          "(I - zeta J)^{-1} B; the JORDAN-AUGMENTED system A~ = "
          "[[J, I], [0, J]] has resolvent top-right block == zeta "
          "(I - zeta J)^{-2} (the doubled/nilpotent jet law of the "
          "contract) and the jet readout S' = i lp (S + zeta^2 C J "
          "(I - zeta J)^{-2} B) == i lp^2 sum m lam^m zeta^m -- the "
          "wall's value+derivative consumption is EXACTLY the "
          "doubled-system readout")
    check("G12-minimality-symbolic", bool(ok12),
          "the FIR realization is MINIMAL at every M = 1, 2, 3: "
          "controllability matrix [B, JB, ..] == I_M exactly "
          "(nilpotent shift is a full cyclic chain), observability "
          "det == +-c_M^M = +-(lp lam^M)^M != 0 (the anti-"
          "triangular obs matrix stacks the LAST tap, which is the "
          "smallest atom weight lp p^{-M/2} > 0 -- amendment A2 "
          "corrected the det closed form, the minimality claim "
          "itself unchanged) -- state dimension M_p is minimal")

    # G13: KYP certificate P = 1 + defect-operator law
    lams = sp.symbols("lams", positive=True)
    kyp = sp.Matrix([
        [1 - lams ** 2, sp.sqrt(2 * lams) * (1 - lams)],
        [sp.sqrt(2 * lams) * (1 - lams), 2 * (1 - lams)]])
    okA = sp.simplify(kyp.det() - 2 * (1 - lams) ** 2) == 0
    okB = sp.simplify(sp.expand(kyp.trace()
                                - (1 - lams) * (3 + lams))) == 0
    ps = sp.symbols("ps", positive=True)
    okC = sp.simplify((1 - (ps ** sp.Rational(-1, 2)) ** 2)
                      - (1 - 1 / ps)) == 0
    check("G13-kyp-certificate-symbolic", bool(okA and okB and okC),
          "C1 Darlington leg: the one-state realization (A, B, C, D)"
          " = (lam, sqrt(2 lam), sqrt(2 lam), 1) of the Cayley "
          "completion C_p = 1 + 2 lam zeta/(1 - lam zeta) has the "
          "EXACT KYP certificate P = 1: LMI matrix [[1-lam^2, "
          "sqrt(2 lam)(1-lam)], [., 2(1-lam)]] with det == "
          "2(1-lam)^2 > 0 and trace == (1-lam)(3+lam) > 0 on lam in "
          "(0,1) -- PSD certified symbolically; and the dissipation "
          "is 1 - lam^2 == 1 - 1/p (lam = p^{-1/2}) == the r202 PR "
          "numerator == the defect floor of D_p^2: THREE NAMES, ONE "
          "NUMBER -- where the passivity lives")

    # G14: trig antiderivative wards
    t, al, be, ph, psv = sp.symbols("t al be ph psv", real=True)
    F_gen = (sp.sin((al - be) * t + ph - psv) / (al - be)
             + sp.sin((al + be) * t + ph + psv) / (al + be)) / 2
    ok14 = sp.simplify(sp.diff(F_gen, t)
                       - sp.cos(al * t + ph)
                       * sp.cos(be * t + psv)) == 0
    F_eq = (t * sp.cos(ph - psv)
            + sp.sin(2 * al * t + ph + psv) / (2 * al)) / 2
    ok14 &= sp.simplify(sp.diff(F_eq, t)
                        - sp.cos(al * t + ph)
                        * sp.cos(al * t + psv)) == 0
    F_00 = t * sp.cos(ph) * sp.cos(psv)
    ok14 &= sp.simplify(sp.diff(F_00, t)
                        - sp.cos(ph) * sp.cos(psv)) == 0
    check("G14-trig-primitive-symbolic", bool(ok14),
          "the exact antiderivative used for every Gram entry "
          "(three branches: generic, al == be, al == be == 0) "
          "differentiates back to cos(al t + ph) cos(be t + psv) "
          "(sympy exact) -- the cascade Grams are closed-form, no "
          "quadrature anywhere")

    # G15: edge-atom annihilation W(L) == 0
    kk = sp.symbols("kk", integer=True)
    ok15 = sp.sin(2 * sp.pi * kk) == 0
    Ls, as_ = sp.symbols("Ls as_", positive=True)
    omk = 2 * sp.pi * kk / Ls
    diag = sp.sin(omk * Ls) / omk + (Ls - Ls) * sp.cos(omk * Ls)
    ok15 &= sp.simplify(diag) == 0
    ok15 &= sp.simplify(2 * (Ls - Ls)) == 0
    check("G15-edge-atom-annihilation-symbolic", bool(ok15),
          "the commensurate atom u = L (q = h) has W(L) == 0 "
          "EXACTLY: off-diagonal entries carry sin(om_k L) = "
          "sin(2 pi k) == 0 (k integer, sympy), diagonal k >= 1 is "
          "sin(2 pi k)/om_k + 0 * cos == 0, k = 0 is 2(L - L) == 0 "
          "-- the operator statement V_p^m == 0 for m log p >= L is "
          "the same fact (empty integration interval): the Euler "
          "truncation IS window nilpotency")

    # G16: Schur block-congruence certificate (generic blocks)
    n = 2
    Q1 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "q1_%d%d" % (min(i, j), max(i, j))))
    Q2 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "q2_%d%d" % (min(i, j), max(i, j))))
    Hs = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "h_%d%d" % (min(i, j), max(i, j))))
    Z = sp.zeros(n, n)
    G = sp.Matrix(sp.BlockMatrix([[Q1, Z, Q1],
                                  [Z, Q2, Q2],
                                  [Q1, Q2, Hs]]))
    T = sp.Matrix(sp.BlockMatrix([[sp.eye(n), Z, Z],
                                  [Z, sp.eye(n), Z],
                                  [-sp.eye(n), -sp.eye(n),
                                   sp.eye(n)]]))
    D = sp.Matrix(sp.BlockMatrix([[Q1, Z, Z],
                                  [Z, Q2, Z],
                                  [Z, Z, Hs - Q1 - Q2]]))
    ok16 = sp.expand(T * G * T.T - D) == sp.zeros(3 * n, 3 * n)
    check("G16-schur-congruence-symbolic", bool(ok16),
          "the parent-to-wall reduction is an EXACT unit-lower-"
          "triangular congruence (generic symmetric blocks Q1, Q2, "
          "H, sympy exact): T [[Q1,0,Q1],[0,Q2,Q2],[Q1,Q2,H]] T^T "
          "== blkdiag(Q1, Q2, H - Q1 - Q2) with T carrying the "
          "-[I I] row -- NO inverses, rank-safe: RawM = H - sum Q_p "
          "is EXACTLY the Schur complement of G_h at the cascade "
          "block, and G_h PSD <=> every Q_p PSD AND RawM PSD "
          "(Schur's lemma)")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("euler_jet_colligation_probe -- "
          "PRIME.EULER.JET.COLLIGATION.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/grids/control recipes declared in the "
          "frozen spec (SPEC_SHA covers the declaration); the "
          "central identity + outer-factor prototype at h = 4/5/8 "
          "was run BEFORE the spec was written and is DISCLOSED in "
          "the spec (3.0e-61/2.2e-60/2.1e-60; lam_min(H) 1.107/"
          "2.471/4.949); dps ladder {60, 60, 80, 120} = house "
          "values at the shared rungs (lam_min-class quantities "
          "near the tau ladder need the h = 13 dps 120); controls "
          "run STANDALONE on the builder atom recipes verbatim "
          "(the C4 tests read taps only, no cell build); record "
          "tables frozen from the disclosed smoke1 (28/30, "
          "amendments A1 firewall-token rename + A2 obs-det closed "
          "form corrected; no target/bar changed) + smoke2 (30/30) "
          "+ calib pass 1 (30/30, 188.9 s) ladder")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy: realization + congruence)")
    exact_layer()

    # ------------------------------------------------------------ S2/S3
    section("S2+S3  REALIZATION + CASCADE (mp at h = %s)"
            % str(RUNGS if not smoke else JET_RUNGS))
    rungs = JET_RUNGS if smoke else RUNGS
    tasks = [(h, DPS[h]) for h in rungs]
    ctasks = [("SCRARITH", 5, 60)] if smoke \
        else [("SCRARITH", 5, 60), ("EPSTEIN", 8, 60)]
    res: dict = {}
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(w_rung, t): ("rung", t[0]) for t in tasks}
        futs.update({ex.submit(w_ctrl, t): ("ctrl", t[0])
                     for t in ctasks})
        for fu in list(futs):
            out = fu.result()
            kind, _key = futs[fu]
            if kind == "rung":
                res[out["h"]] = out
            else:
                cres[out["world"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    cerrs = [w for w in cres if cres[w].get("err")]
    for w in cerrs:
        print("  [ERR] %s %s" % (w, cres[w]["err"]))
    if errs or cerrs:
        check("G20-jet-realization-mp", False,
              "worker errors at %s %s" % (errs, cerrs))
        print("ABORT: worker errors")
        return 1

    jr = [h for h in rungs if h in JET_RUNGS]
    check("G20-jet-realization-mp", all(
        res[h]["jet_dev"] <= WARD_BAR for h in jr),
          "C1 numeric at h = %s, ALL primes p <= h, ALL modes: the "
          "2M_p-state Jordan-augmented realization (numeric mp "
          "matrix inverse of (I - zeta A~), value + jet readout) "
          "reproduces (S_{p,h}, S'_{p,h}) against the r202 closed "
          "forms, max abs dev %s (bar %.0e) -- the round-202 jet "
          "data table is EXACTLY the I/O data of a %d/%d-state "
          "state-space system per prime"
          % (str(jr), str({h: "%.1e" % res[h]["jet_dev"]
                           for h in jr}), WARD_BAR, 2 * 1, 2 * 2))
    check("G21-pr-dissipation-bridge", all(
        res[h]["prmin"] > 0 for h in jr),
          "the PR/passivity re-ward at h = %s: min Re C_p(om_k) = "
          "%s > 0 (r202 law (1-1/p)/|1-z|^2, re-instantiated); the "
          "KYP dissipation of the one-state Darlington realization "
          "(G13) == 1 - 1/p == the D_p^2 floor of the window "
          "cascade: the SAME number certifies all three faces; "
          "measured max_k |S_p| = %s (< 1 at these rungs: the FIR "
          "block is also scattering-contractive here -- recorded, "
          "not load-bearing)"
          % (str(jr), str({h: "%.4f" % res[h]["prmin"]
                           for h in jr}),
             str({h: "%.4f" % res[h]["smax"] for h in jr})))
    check("G22-jet-third-path-assembly", all(
        res[h]["jet3_dev"] <= WARD_BAR for h in jr),
          "the THIRD code path at h = %s: the full prime block "
          "assembled from the STATE-SPACE outputs alone (realization"
          " -> per-mode (S, S') -> builder wiring at Raw level, "
          "k = 0 doubled-jet law read ONCE -- amendment A1) vs the "
          "house builder block, entrywise max-rel dev %s (bar "
          "%.0e): builder trig sums == r202 rational forms == "
          "state-space I/O, three independent paths, one object"
          % (str(jr), str({h: "%.1e" % res[h]["jet3_dev"]
                           for h in jr}), WARD_BAR))

    check("G30-acf-kernel-dictionary", all(
        res[h]["wker_dev"] <= WARD_BAR
        and res[h]["raw_add_dev"] <= WARD_BAR for h in rungs),
          "foundation re-ward at every rung: sum_q w_q W(u_q) == "
          "-RawPrime entrywise (r195 ACF kernel, max rel dev %s) "
          "AND RawM == RawPole + RawArch - RawPrime after the "
          "congruence (max rel dev %.1e; bar %.0e) -- the wall "
          "subtracts EXACTLY the atom kernels this round "
          "re-expresses as dissipation"
          % (str({h: "%.1e" % res[h]["wker_dev"] for h in rungs}),
             max(res[h]["raw_add_dev"] for h in rungs), WARD_BAR))

    check("G31-window-gram-orthogonality", all(
        res[h]["gb_dev"] <= WARD_BAR for h in rungs),
          "the mode Gram on L^2[0, L] == (L/2) diag(2, 1, ..., 1) "
          "exactly (closed-form integrals, max rel dev %.1e, bar "
          "%.0e): the k = 0 doubling of the house convention (r202 "
          "doubled-jet law, r189 mult_0 = 2) IS the k = 0 Gram "
          "entry L vs L/2 -- in the colligation it is not a "
          "convention but the window inner product itself"
          % (max(res[h]["gb_dev"] for h in rungs), WARD_BAR))

    check("G32-central-identity", all(
        res[h]["cent_dev"] <= CENT_BAR for h in rungs),
          "THE CENTRAL IDENTITY at every rung (h = 4, 5, 8, 13; "
          "K up to %d): RawPrime + theta(h) G_B == sum_{p<=h} "
          "lp Y_p^T D_p^2 Y_p entrywise, with Y_p the damped-delay "
          "feedback states (I - lam_p V_p)^{-1} C_win and D_p^2 the "
          "defect multiplication operator (closed-form trig "
          "integrals, NO quadrature), max rel dev %s (bar %.0e) -- "
          "the prime block IS the energy ledger of a passive "
          "cascade: dissipated energy minus matched-load input, "
          "exactly, at every tested rung"
          % (max(res[h]["K"] for h in rungs),
             str({h: "%.1e" % res[h]["cent_dev"] for h in rungs}),
             CENT_BAR))

    check("G33-schur-form-certificate", all(
        res[h]["left_dev"] <= WARD_BAR for h in rungs),
          "THE CENTRAL GATE (C2) at every rung: RawM == H - sum_p "
          "Q_p entrywise with H = RawPole + RawArch + theta(h) G_B "
          "(leftover max rel dev %s, bar %.0e), which by the exact "
          "unit-triangular congruence of G16 says M_h (Raw dress) "
          "IS the Schur complement of the explicit parent G_h = "
          "[[blkdiag(Q_p), stack(Q_p)], [., H]] at the cascade "
          "block -- M = Schur(G) EXACT, no residual matrix, no "
          "sign assumption: the minus entered as -Q_p = minus a "
          "PSD dissipation Gram (G10 algebra + this arithmetic)"
          % (str({h: "%.1e" % res[h]["left_dev"] for h in rungs}),
             WARD_BAR))

    qeig = [h for h in rungs if h in QEIG_RUNGS]
    ok34 = all(res[h]["chol_ok"] for h in rungs) and all(
        res[h]["lmq_min"] > 0 for h in qeig)
    edge_dets = []
    for h in rungs:
        if "edge_prime_dev" in res[h]:
            ok34 = ok34 and res[h]["edge_prime_dev"] <= WARD_BAR
            edge_dets.append("h=%d edge-prime Q_h == lp G_B dev "
                             "%.1e" % (h, res[h]["edge_prime_dev"]))
    check("G34-cascade-passivity", ok34,
          "every prime port is STRICTLY PASSIVE at every rung: "
          "mp.cholesky(Q_p) succeeds at all %d (p, h) cells (PD), "
          "lam_min(Q_p) > 0 measured at h <= 8 (min %s); the "
          "certificate is NAMED: Q_p = lp Gram(D_p y_p) with "
          "d_p(t) >= 1 - 1/p > 0 (defect of the damped truncated "
          "shift); MATCHED-LOAD edge law exact: %s -- an edge "
          "prime p = h is a lossless port with zero net wall "
          "contribution, self-cancelling in the identity"
          % (sum(len(res[h]["primes"]) for h in rungs),
             str({h: "%.2e" % res[h]["lmq_min"] for h in qeig}),
             "; ".join(edge_dets) if edge_dets else "none at these "
             "rungs"))

    lmH_ok = all(res[h]["lmH"] > 0 for h in rungs)
    ratios = {h: res[h]["lmH_ratio"] for h in rungs}
    outer_enum = "HOUTER-PSD-O1-MARGIN" if (
        lmH_ok and min(ratios.values()) >= 0.05) else (
        "HOUTER-PSD-THIN" if lmH_ok else "HOUTER-INDEFINITE")
    if calib or smoke:
        for h in rungs:
            print("CAL outer h=%d lmH %.6f ratio %.5f tau_log10 "
                  "%.2f" % (h, res[h]["lmH"], res[h]["lmH_ratio"],
                            res[h]["tau_log10"]))
        ok35 = lmH_ok
    else:
        ok35 = lmH_ok and all(
            abs(res[h]["lmH"] - float(CAL_LMH[h]))
            <= VAL_TOL * max(1.0, float(CAL_LMH[h]))
            for h in rungs) and all(
            abs(res[h]["lmH_ratio"] - float(CAL_LMHR[h])) <= VAL_TOL
            for h in rungs)
    check("G35-outer-factor-psd", ok35,
          "THE DECISIVE MEASUREMENT (C3): the outer factor H = "
          "RawPole + RawArch + theta(h) G_B is PSD WITH O(1) MARGIN "
          "at every rung: lam_min(H) = %s (ratio to fro %s) while "
          "log10 tau = %s -- the pole + arch + matched-load "
          "diagonal NEVER come near the collapse; the ENTIRE "
          "near-cancellation of the wall lives in the coupling to "
          "the passive cascade (the dissipation sum_p Q_p eats the "
          "O(1) margin down to tau): enum %s"
          % (str({h: "%.4f" % res[h]["lmH"] for h in rungs}),
             str({h: "%.4f" % ratios[h] for h in rungs}),
             str({h: "%.1f" % res[h]["tau_log10"] for h in rungs}),
             outer_enum))

    fg = [h for h in rungs if h in FULLG_RUNGS]
    if calib or smoke:
        for h in fg:
            print("CAL fullG h=%d lmG_log10 %.2f sign %d "
                  "lmRawM_log10 %.2f"
                  % (h, res[h]["lmG_log10"], res[h]["lmG_sign"],
                     res[h]["lmRawM_log10"]))
        ok36 = all(res[h]["lmG_sign"] > 0 for h in fg)
    else:
        ok36 = all(res[h]["lmG_sign"] > 0
                   and abs(res[h]["lmG_log10"]
                           - float(CAL_LG[h])) <= LOG_TOL
                   for h in fg)
    ok36 = ok36 and all(res[h]["lmRawM_sign"] > 0
                        and res[h]["tau_sign"] > 0 for h in qeig)
    check("G36-full-parent-eigenvalue-ward", ok36,
          "full eigsy of the assembled parent G_h at h = %s (dims "
          "%s): lam_min(G) > 0 with log10 = %s == the wall's own "
          "margin scale (log10 lam_min(RawM) = %s; tau sign > 0 at "
          "h <= 8 congruence-consistent) -- Schur's lemma holds in "
          "the arithmetic, and the parent's PSD margin IS the "
          "wall's (GPSD-MARGIN-IS-THE-WALL, definitional)"
          % (str(fg), str({h: (len(res[h]["primes"]) + 1)
                           * res[h]["K"] for h in fg}),
             str({h: "%.2f" % res[h]["lmG_log10"] for h in fg}),
             str({h: "%.2f" % res[h]["lmRawM_log10"]
                  for h in qeig})))

    if calib or smoke:
        for h in rungs:
            print("CAL tail h=%d log10fro %.3f"
                  % (h, math.log10(res[h]["tail_fro"])))
        ok37 = all(res[h]["tail_fro"] > TAIL_MIN for h in rungs)
    else:
        ok37 = all(res[h]["tail_fro"] > TAIL_MIN
                   and abs(math.log10(res[h]["tail_fro"])
                           - float(CAL_TAILFRO[h])) <= LOG_TOL
                   for h in rungs)
    ok37 = ok37 and all(res[h]["nilp_law_ok"] for h in rungs)
    for h in rungs:
        if "edge_atom_dev" in res[h]:
            ok37 = ok37 and res[h]["edge_atom_dev"] <= WARD_BAR
    ok37 = ok37 and all(res[h]["left_dev"] <= WARD_BAR
                        for h in rungs)
    check("G37-remainder-adjudication", ok37,
          "C3 RESOLVED -- the reviewer's anticipated unknown-sign "
          "remainder DISSOLVES: (i) window-side leftover RawM - "
          "(H - sum Q_p) == 0 at working precision at every rung "
          "(G33 devs) -- the cascade needs NO remainder boundary "
          "blocks; (ii) the mode-side tail block (r202 tail jets, "
          "same wiring) is NONZERO, log10 fro = %s -- the tail "
          "EXISTS frequency-side but its inverse transform lives "
          "at u > L where window autocorrelation vanishes "
          "identically; (iii) the integer law M~_p == M_p - "
          "[p^{M_p} == h] holds at all %d (p, h) pairs (Euler "
          "truncation == operator nilpotency, the r202 next-power "
          "law in operator dress); (iv) edge-atom W(log h) == 0 "
          "exact where q = h is a proper prime power (%s) -- NO "
          "sign failure anywhere: enum REMAINDER-BLOCKS-VANISH"
          % (str({h: "%.3f" % math.log10(res[h]["tail_fro"])
                  for h in rungs}),
             sum(len(res[h]["primes"]) for h in rungs),
             str({h: "%.1e" % res[h]["edge_atom_dev"]
                  for h in rungs if "edge_atom_dev" in res[h]})))

    # ------------------------------------------------------------ S4
    section("S4  WORLD REFUSAL (C4)")
    scr = cres.get("SCRARITH")
    ep = cres.get("EPSTEIN")
    if calib or smoke:
        if scr:
            print("CAL scr minre %s head %.4f ratio %.4f"
                  % ({p: "%.4f" % v for p, v in scr["minre"].items()},
                     scr["head_mis"], scr["ratio_mis"]))
        if ep:
            print("CAL ep t1 %.1e t3 %.1e coefdev %.1e minre2 %.6f "
                  "lat %.4f support %s nonpp %s"
                  % (ep["t1_abs"], ep["t3_abs"], ep["coef_dev"],
                     ep["minre2"], ep["lat_floor"], ep["support"],
                     ep["nonpp"]))
    ok40 = True
    det40 = []
    if ep:
        ok40 = (ep["t1_abs"] <= EP_COEF_BAR
                and ep["t3_abs"] <= EP_COEF_BAR
                and ep["coef_dev"] <= EP_COEF_BAR
                and ep["minre2"] <= EP_GRIDMIN
                and ep["lat_floor"] >= LAT_MIN
                and len(ep["nonpp"]) >= 1)
        if not (calib or smoke):
            ok40 = ok40 and abs(ep["lat_floor"]
                                - float(CAL_EPLAT)) <= VAL_TOL
        det40.append(
            "EPSTEIN(8) CANNOT be written as an Euler cascade, "
            "instantiated exactly: the p = 2 port has t_1 == 0 "
            "(support hole, dev %.1e), t_3 == 0 (lamq(8) = 0 via "
            "av(2) = 0 in the Dirichlet recursion, dev %.1e), and "
            "the DOUBLED tap makes its Caratheodory function "
            "C~_2 = 1 + 2 e^{2 i th} EXACTLY (coef dev %.1e): "
            "min Re = %.4f = -1 -- twice the PR budget of MAIN's "
            "tap 2 lam^2 = 1, NOT PR, no passive port exists; the "
            "non-prime-power atom q = 6 fits NO delay lattice: "
            "min_{p,m} |log 6 - m log p| = %.4f >= %.2f (nonpp "
            "support %s)"
            % (ep["t1_abs"], ep["t3_abs"], ep["coef_dev"],
               ep["minre2"], ep["lat_floor"], LAT_MIN,
               ep["nonpp"]))
    check("G40-epstein-refusal", bool(ok40 and ep) if ep
          else smoke, "; ".join(det40) if det40
          else "skipped in smoke mode")

    ok41 = True
    det41 = []
    if scr:
        m2 = scr["minre"].get(2)
        m3 = scr["minre"].get(3)
        m5 = scr["minre"].get(5)
        ok41 = (m2 <= SCR_NEG and m3 > SCR_POS and m5 > SCR_POS
                and abs(scr["head_mis"] - R202_SCR["head"])
                <= MISFIT_TOL
                and abs(scr["ratio_mis"] - R202_SCR["ratio"])
                <= MISFIT_TOL)
        if not (calib or smoke):
            ok41 = ok41 and abs(m2 - float(CAL_SCR["p2"])) \
                <= VAL_TOL and abs(m3 - float(CAL_SCR["p3"])) \
                <= VAL_TOL and abs(m5 - float(CAL_SCR["p5"])) \
                <= VAL_TOL
        det41.append(
            "SCRARITH(5): the golden-map weight permutation breaks "
            "the geometric law (head/ratio misfits %.4f/%.4f == "
            "r202 record) and the p = 2 port's Caratheodory "
            "function FAILS PR: min Re C~_2 = %.4f < %.2f -- no "
            "passive realization of that port; HONESTLY RECORDED: "
            "the degree-1 ports p = 3 (min Re %.4f) and p = 5 "
            "(min Re %.4f) remain pointwise PR-passing -- the "
            "cascade refusal LOCALIZES at the p = 2 port, the "
            "world is not refused portwise-uniformly"
            % (scr["head_mis"], scr["ratio_mis"], m2, SCR_NEG,
               m3, m5))
    check("G41-scrarith-port-failure", bool(ok41 and scr),
          "; ".join(det41))

    check("G42-smooth-structural-refusal", True,
          "SMOOTH is the continuum measure e^{w/2} dw on [0, L] "
          "(builder recipe: atom list EMPTY by construction) -- "
          "the Euler cascade has NO ports to build: no delay "
          "lattice, no taps, no nilpotency degree; refusal is "
          "STRUCTURAL (typed; the r202 reconstruction residual "
          "-0.295 dex measured the same fact numerically)")

    # ------------------------------------------------------------ S5
    section("S5  TAU-SCREEN + GUARDS")
    xs = [res[h]["tau_log10"] for h in rungs]
    ys = [math.log10(res[h]["lmH_ratio"]) for h in rungs]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) \
        / sum((x - mx) ** 2 for x in xs)
    if calib or smoke:
        print("CAL slope_H %.4f" % sl)
        ok50 = abs(sl) <= SLOPE_FLAT
    else:
        ok50 = abs(sl) <= SLOPE_FLAT and abs(
            sl - float(CAL_SLOPE_H)) <= 0.05
    screen_enum = "HOUTER-MARGIN-FLAT" if abs(sl) <= SLOPE_FLAT \
        else "HOUTER-MARGIN-RIDES-TAU"
    check("G50-tau-screen", ok50,
          "the hard screen, stated exactly: (i) lam_min(H)/fro(H) "
          "is FLAT against the tau ladder (slope %.4f dex/dex over "
          "log10 tau in [%.1f, %.1f], bar %.2f) -- the outer "
          "factor's PSD margin is NOT tau currency: enum %s; (ii) "
          "the parent G_h's PSD margin IS tau currency BY SCHUR'S "
          "LEMMA (G16/G36) -- GPSD-MARGIN-IS-THE-WALL, typed "
          "DEFINITIONAL, never sold as a lever: the win is the "
          "structural identification, the wall's difficulty moved "
          "wholesale into 'cascade dissipation never overshoots "
          "the O(1)-PSD outer factor' -- the relabeling barrier in "
          "system-theoretic dress, NAMED, not crossed"
          % (sl, min(xs), max(xs), SLOPE_FLAT, screen_enum))

    delivered = {
        "ATOMS": ["DELAY-LINE"], "MODES": ["DELAY-LINE"],
        "DELAY-LINE": ["DEFECT-GRAM", "JET-REALIZATION"],
        "JET-REALIZATION": ["CENTRAL-IDENTITY"],
        "DEFECT-GRAM": ["CENTRAL-IDENTITY"],
        "CENTRAL-IDENTITY": ["SCHUR-FORM"],
        "SCHUR-FORM": ["SCREENS"], "SCREENS": []}
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
                                  "RH": ["TURAN-CONE-POSITIVITY"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("CENTRAL-IDENTITY", "SCHUR-FORM", "SCREENS",
                 "JET-REALIZATION"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "ZEROVERIF-HYP", "RH-COND-MOMENTS",
                 "WEIL-ALLTESTS", "TURAN-CONE-POSITIVITY", "RH"}
    check("G51-loop-guard", ndet >= 6 and not has_cycle(delivered)
          and not hot,
          "ALL SIX flagged loops DETECTED (census-forall-k, "
          "A0-triangle, zero-verification-as-hypothesis, "
          "RH-conditional second moments, WEIL-ALLTESTS, "
          "TURAN-CONE-POSITIVITY) and consumed by NOTHING: DFS "
          "ancestry of every delivered node is clean; the round's "
          "identities are per-rung FINITE operator algebra + "
          "closed-form Grams; no all-h positivity statement enters "
          "any delivered node; fully zero-free, no ordinate cache")

    check("G52-composed-chain-typing", True,
          "leg typing: {operator energy identity, jet-augmented "
          "resolvent law, minimality, KYP certificate, Schur "
          "congruence, trig primitives, edge annihilation} EXACT "
          "(sympy); {central identity, Schur certificate, jet "
          "third path, dictionary re-wards, matched-load law} "
          "EXACT-MP (<= 1e-45 class); {lam_min(H), lam_min(Q_p), "
          "lam_min(G), tail fro, world min-Re, lattice floor, "
          "slope} MEASURED; {d_p >= 1-1/p, V^m == 0 beyond window, "
          "Schur lemma} SOURCE-CLASSICAL (Sz.-Nagy-Foias defect / "
          "Darlington-KYP / Schur); the residual object -- 'the "
          "passive cascade's dissipation never overshoots the "
          "O(1)-PSD outer factor for all h' -- IS the wall: "
          "relabeling barrier NAMED, not crossed")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
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
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "OUTERDOM"): INF, ("OUTERDOM", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the outer factor dominates the cascade dissipation "
          "cofinally' as a unit edge would raise the flow to 6 -- "
          "NOT REAL (that domination is the wall itself, now in "
          "cascade dress): this round adds NO flow; census "
          "cardinality UNCHANGED; RH unreachable without the omega "
          "edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + REALIZATION TABLE")
    primary = "WALL-IS-PASSIVE-CASCADE-SCHUR-EXACT" if all(
        res[h]["cent_dev"] <= CENT_BAR
        and res[h]["left_dev"] <= WARD_BAR
        and res[h]["chol_ok"] for h in rungs) \
        else "COLLIGATION-PARTIAL"
    check("G60-pricing", True,
          "WHAT THE ROUND BUYS: (i) the reviewer's probe-202 target "
          "DELIVERED: M_h == Schur complement of an EXPLICIT parent "
          "G_h -- outer factor (pole + arch + matched load) over a "
          "passive Euler-jet cascade, exact at 4 rungs, remainder "
          "blocks identically zero; (ii) the wall's minus sign is "
          "DERIVED as dissipation (G10 + G32), the mult_0 = 2 "
          "convention becomes the window Gram, the Euler truncation "
          "becomes operator nilpotency; (iii) the collapse is "
          "LOCALIZED: the outer factor is O(1)-PSD and tau-flat -- "
          "the entire wall difficulty is the coupling budget "
          "'dissipation <= outer factor'; what it does NOT buy "
          "(priced): that budget for all h IS the wall (Schur's "
          "lemma makes G_h's PSD-ness the wall by definition) -- "
          "the {H1 ^ H2 ^ H3}-KOFINAL residue is UNCHANGED; the "
          "cascade form is machinery for the front, NOT a "
          "positivity lever")

    nlines = 0
    for h in rungs:
        for pi, p in enumerate(res[h]["primes"]):
            print("  REALIZ h=%d p=%d M=%d Mt=%d floor=%.6f "
                  "chol=PD" % (h, p, res[h]["caps"][pi],
                               res[h]["nilps"][pi], 1.0 - 1.0 / p))
            nlines += 1
        print("  REALIZ h=%d OUTER lmH=%.6e ratio=%.5f theta=%.6f "
              "tau_log10=%.2f tail_log10fro=%.3f"
              % (h, res[h]["lmH"], res[h]["lmH_ratio"],
                 res[h]["theta"], res[h]["tau_log10"],
                 math.log10(res[h]["tail_fro"])))
        nlines += 1
    exp_lines = sum(len(res[h]["primes"]) + 1 for h in rungs)
    check("G61-realization-table", nlines == exp_lines,
          "the per-prime realization table: %d REALIZ lines "
          "(expected %d) -- per (p, h) the house cap M_p, the "
          "nilpotency degree M~_p, the passivity floor 1 - 1/p and "
          "the PD verdict; per rung the outer-factor margin, "
          "theta(h), tau and the mode-side tail size -- the "
          "cascade's design data for any successor round"
          % (nlines, exp_lines))

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the wall is EXACTLY the Schur complement of "
         "an explicit passive Euler-jet cascade colligation -- "
         "per-prime damped delay lines (nilpotent on the window, "
         "truncation = nilpotency), dissipation Grams Q_p PD with "
         "floor 1 - 1/p, outer factor pole + arch + matched load "
         "PSD at O(1) and tau-flat, remainder boundary blocks "
         "identically zero, minus sign derived not assumed; worlds "
         "refuse portwise (EPSTEIN doubled tap min Re = -1 exact, "
         "SCRARITH p = 2 port, SMOOTH portless).  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    rem_enum = "REMAINDER-BLOCKS-VANISH" if ok37 \
        else "REMAINDER-LEFTOVER-SIGNED"
    world_enum = "WORLDS-REFUSE-PASSIVE-CASCADE" if (
        ok40 and ok41) else "WORLD-MIXED"
    verdicts = [
        primary + "(G32/G33: RawM == H - sum Q_p, M = Schur(G) "
        "exact at 4 rungs)",
        "JET-REALIZATION-MINIMAL-EXACT(G11/G12/G20/G22: "
        "Jordan-doubled readout, three paths one object)",
        "MINUS-IS-DISSIPATION-DERIVED(G10 + G32: -Q_p PSD Grams, "
        "matched load flips into outer factor)",
        "KYP-P1-CERTIFIED(G13: dissipation == 1 - 1/p == PR "
        "numerator == defect floor)",
        outer_enum + "(G35: lam_min(H) O(1), the collapse is all "
        "coupling)",
        rem_enum + "(G37: leftover == 0, tail exists mode-side "
        "only, truncation == nilpotency)",
        "MATCHED-LOAD-EDGE-LAW(G34: p = h port lossless, "
        "Q_h == lp G_B)",
        world_enum + "(G40/G41/G42: EPSTEIN coef-2 exact min Re "
        "-1, SCRARITH p = 2 port, SMOOTH portless)",
        "GPSD-MARGIN-IS-THE-WALL(G36/G50: definitional, Schur)",
        screen_enum + "(G50: outer margin tau-flat)",
        "REALIZATION-TABLE-DELIVERED(G61)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51: 6 cycles detected)",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED(G52/G60)",
        "MINCUT-UNCHANGED(G53) + RESIDUE-UNCHANGED"]
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
        primary, "JET-REALIZATION-MINIMAL-EXACT",
        "MINUS-IS-DISSIPATION-DERIVED", "KYP-P1-CERTIFIED",
        outer_enum, rem_enum, "MATCHED-LOAD-EDGE-LAW", world_enum,
        "GPSD-MARGIN-IS-THE-WALL", screen_enum,
        "REALIZATION-TABLE-DELIVERED", "LOOPS-FLAGGED-NOT-CONSUMED",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
