#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_block_sturm_probe -- PRIME.EULER.BLOCK.STURM.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface) are not touched.

=======================================================================
MISSION (round ~206: the EULER JET program, probe 4 -- the reviewer's
block-Sturm target on the r188 census pencil).  r188 (census_lift,
SPEC 8ada6b97d56aca46) delivered the exact Krein pencil for the census
polynomial N_h(y): in RATIONAL coordinates A_ns = D - ONES rho^T with
D = diag(b_k), rho_k = (-1)^k c_k b_k / A_0 (k = 1..K-1, source data:
the wall ground ray c and the poles b, NEVER roots), metric
Jr = diag(rho_k):  Jr A_ns IS SYMMETRIC (B-self-adjoint pencil, gated
G10), det(yI - A_ns) = Ntilde(y)/A_0 exactly (matrix determinant
lemma), and the metric signature == the residue sign ladder (n_+, n_-)
-- MIXED at every true rung: the SCALAR orthogonal-polynomial /
Stieltjes structure is dead (r188), the sign characteristic is the
mixed ladder itself (r191).  THE REVIEWER'S TARGET: a MATRIX-VALUED
(2x2) block-Jacobi/Stieltjes recursion with A_n PD and B_n PSD whose
det reproduces N_h -- the hope being that the Euler-jet port pairing
(value+jet per prime, r204 realization) absorbs the mixed scalar
signs into positive 2x2 blocks.  THIS round builds the machinery
exactly and adjudicates the hope honestly:

  THE CONSTRUCTION (derived pre-freeze in two DISCLOSED prototypes,
  scripts deleted at freeze, logs kept).  Block-Lanczos with the
  indefinite metric Jr on the operator A_ns (J-self-adjoint), 2x2
  starting block per PAIRING, full re-J-orthogonalization, exact
  power-of-two column normalization (every census observable is
  block-rescaling INVARIANT -- gated symbolically, G13).  Output: the
  block tridiagonal pencil (S_n, G_n, H_n) with metric blkdiag(S_n) =
  V^T Jr V, recursion coefficients Bhat_n = S_n^{-1} G_n and Ahat_n =
  S_n^{-1} H_{n-1}^T S_{n-1}^{-1} H_{n-1} (the block analogues of the
  Jacobi b_n and a_n^2; eigenvalues similarity-invariant), and THE
  BLOCK STURM CHAIN: the 2x2 adjugate-cleared Schur recursion
    Phi_1 = E_1,   E_m(y) = y S_m - G_m,
    Phi_m = E_m Theta_{m-1}
            - H_{m-1}^T adj(Phi_{m-1}) H_{m-1} * Theta_{m-2}^(2-r'),
    Theta_m = det Phi_m / Theta_{m-1}^(r-1)   (division EXACT),
  (r = block size, r' = previous block size; adj = 2x2 adjugate,
  adj X = tr(X) I - X), with Theta_N(y) == det(yM - G) == det(V)^2
  det(Jr) N_h(y)/A_0 -- the block three-term/Sturm recursion whose
  terminal determinant IS the census polynomial, source-side, roots
  never consumed (gated symbolically at sizes (2,2), (2,1,1), (1,2)
  and exactly/numerically on the data, B3 = G24).

  THE STRUCTURAL CENTERPIECE (the honest adjudication of B1/B2):
  blkdiag(S_n) = V^T Jr V is a real CONGRUENCE of the metric, so by
  Sylvester's law of inertia  sum_n inertia(S_n) == (n_+, n_-) --
  THE PAIRING CANNOT UNMIX THE METRIC: since the r188 ladder is
  mixed at every true rung, NO pairing, NO starting block and NO
  block size in the entire J-congruence/block-Krylov construction
  class can produce an all-PD block metric (the PD-metric Stieltjes/
  Favard form).  The kill is inertia bookkeeping, not a failed
  search: BLOCK-METRIC-MIXED-BY-INERTIA (gated per pairing per rung,
  G22).  What the theorem does NOT force: the eigenvalue spectra of
  the RECURSION COEFFICIENTS Ahat_n, Bhat_n (similarity class, not
  congruence class) -- the reviewer's residual hope -- so the round's
  decisive tables are the measured eigen-sign censuses of every
  Ahat_n and Bhat_n per pairing per rung (B1's cheap check).
  PRE-FREEZE PROTOTYPE ANSWER (disclosed, frozen below): MIXED AT
  EVERY RUNG AND EVERY PAIRING on MAIN -- BLOCK-SIGNATURE-STILL-
  MIXED; and the coordinate pairings (ADJPOLE/PARITY) DEGENERATE:
  the rank-one coupling ONES rho^T makes the second Krylov block
  rank-1, the chain collapses to the dead scalar chain after one
  step (stages 2(K-1)-1 instead of ceil((K-1)/2)) -- the block
  structure only survives with GENUINE 2-dim port seeds (EULER/WRAP).

GOALS (contract PRIME.EULER.BLOCK.STURM.01):
  B1  the block tridiagonalization of the census pencil: block-
      Lanczos at h = 4, 5 (EXACT Fraction arithmetic on the dyadic
      rationalization, r188 disclosure-(b) style) and h = 8, 13 (mp
      at 2x house dps); the PD/PSD sign census of every S_n, Ahat_n,
      Bhat_n per block per rung -- the round's first table; plus the
      Sylvester inertia-sum gate (the theorem-grade adjudication).
  B2  the pairing battery (predefined, all source-side, no roots):
      (a) EULER   -- seed = the two aggregate Euler cascade port
          channels (u_k, v_k) = (sum_p Im S_{p,h}(om_k), sum_p
          Ptilde_p(om_k)), k = 1..K-1 (r202 closed forms VERBATIM:
          the value+jet ports of the r204 colligation, THE natural
          per-prime value+jet pairing aggregated at the shared mode
          port);
      (b) WRAP    -- seed = the single wrap prime's value+jet
          channels, wrap prime frozen from the r205 orbit record
          CAL_WRAP (inc): {4: 2, 5: 2, 8: 3, 13: 7} (h = 4 is the
          r205 seed-in-region anomaly; predefined fallback p = 2);
      (c) ADJPOLE -- seed = coordinate pair (e_1, e_2) (adjacent
          poles b_1, b_2 in the r188 basis);
      (d) PARITY  -- seed = (e_1, e_{j0}), j0 = first index with
          sign rho_{j0} != sign rho_1 (pairing ACROSS the first
          sign-characteristic flip boundary, r191 parity scaffold,
          source-side).  DISCLOSED: on MAIN the first flip sits at
          j0 = 2 at all four rungs, so PARITY == ADJPOLE there; the
          SCRARITH control (j0 = 3) separates them.
      PLUS the SCALAR chain (seed = ONES, the Weyl vector; size-1
      blocks): its metric sign ladder re-instantiates the r188 dead
      scalar structure and its sign COUNTS == (n_+, n_-) exactly
      (Sylvester at block size 1).
  B3  the determinant identity, machine-checked: at h = 4, 5 EXACT
      (Fraction): det(yM - G) == det(V)^2 det(Jr) Ntilde(y)/A_0 at
      ALL K integer points y = 0..K-1 AND the Sturm chain Theta_N ==
      the direct det at the same points (a degree-(K-1) polynomial
      identity proven by equality at K points); at h = 8, 13 mp at
      the frozen points y in (2, 3, 5, 7, 11, 13), worst rel dev
      gated.  Construction ancestry machine-checked: NO polyroots
      anywhere in this file, construct_* functions never touch the
      builder cell keys (AST, G01/G03); census roots are NEVER
      consumed (the identity is gated at interpolation points).
  B4  worlds and screens.  SMOOTH(5): ladder (0, 10) one-signed =>
      Jr NEGATIVE definite: every S_n ND, every Ahat/Bhat spectrum
      POSITIVE -- the block-Stieltjes form EXISTS after one global
      sign flip in the atom-free world: definiteness separates
      atoms-vs-no-atoms with the WRONG orientation for a sign source
      (r188 MIXEDNESS-IS-ARITHMETIC inherited at block level);
      SCRARITH(5) (3, 7) and EPSTEIN(8) (3, 17) stay mixed in every
      intrinsic pairing (worlds run ADJPOLE/PARITY/SCALAR -- the
      EULER/WRAP seeds are MAIN-train objects, disclosed).
      TAU-SCREEN: the S-block indefiniteness margin ladder
      min_n |det S_n|/fro(S_n)^2 (EULER pairing, scale-free) vs
      log10 tau -- slope gated FLAT/RIDES; Ahat/Bhat eigen-margin
      ladders recorded (near-singular A-blocks at h >= 8: a measured
      observable, recorded not claimed); gauge ward c -> (3/7)c
      leaves rho and the whole construction EXACTLY invariant
      (exact, h = 4).  Loop guard; mincut; typing; pricing.

NOTATION (r171-r205 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; K = ceil(1.25
h log h); om_k = k pi/a; b_k = om_k^2; c_k = builder cn_mp_str
(de-normalized ground-ray components, max-abs positive); e_k =
(-1)^k c_k; A_0 = sum e_k; rho_k = e_k b_k / A_0 (k = 1..K-1);
Ntilde = the r188 unscaled cleared census numerator (leading coeff
A_0); Euler channels from the r202 closed forms S_{p,h} = lp z(1 -
z^{M_p})/(1-z), S'_{p,h} = i lp^2 z(1-(M_p+1)z^{M_p}+M_p z^{M_p+1})
/(1-z)^2, z = p^{-1/2} e^{i om lp}, Ptilde_p = Re(a S + (i/2) S') -
Im S/(2 om); M_p = max{m: p^m <= h}; tau_h = ce["mpE"][0], measured
per-rung scalar only (the screen).  Dyadic rationalization:
Fraction(man 2^exp) of the frozen mp build, exact, no rounding added.
Block-Lanczos: unnormalized + exact power-of-two column scaling; mp
rungs run at workdps 2*dps; deflation by exact rank (h <= 5) /
threshold zb = 10^-(dps-10) (mp, relative); censuses use the same zb
class relative to block scale.  Ahat_n/Bhat_n eigen censuses on the
2x2 trace/det closed form: 'pos' (real spectrum, all > 0), 'nn'
(real, all >= 0, not all > 0), 'mix' (real, some < 0), 'cplx'
(nonreal pair); S-census: PD / IND (signature (1,1)) / ND.

RUNGS AND DPS (frozen; house ladder at the shared rungs): RUNGS =
(4, 5, 8, 13); DPS = {4: 60, 5: 60, 8: 80, 13: 120}; EXACT_MAX = 5.
PAIRINGS (MAIN) = (EULER, WRAP, ADJPOLE, PARITY) + SCALAR;
worlds: SMOOTH(5, 60), SCRARITH(5, 60), EPSTEIN(8, 80) with
(ADJPOLE, PARITY) + SCALAR.  DET_PTS_MP = (2, 3, 5, 7, 11, 13);
exact dets at ALL y = 0..K-1.  WORKERS = 6.  Smoke mode: rungs
(4, 5) + SCRARITH only.

FROZEN BARS: WARD_BAR 1e-40 (mp far-coefficient ward, relative;
exact rungs demand EXACT zero); DET_BAR 1e-100 (mp determinant
identity, worst rel over points and pairings; exact rungs demand
EXACT equality); breakdown NONE anywhere; det-zero events NONE;
SLOPE_FLAT 0.30 (|slope| log10 mS_EULER vs log10 tau);
RUNTIME_BAR 3000 s.  Record tolerances: LOG_TOL 0.30 dex
(margin logs, dev-class), counts/censuses/sign-strings EXACT;
slopes 0.10.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  primary    := BLOCK-STIELTJES-FOUND iff SOME pairing has every
                S_n PD AND every Ahat census 'pos' AND every Bhat
                census in {'pos','nn'} at ALL four rungs (then the
                Stieltjes consequence battery would run -- H2 via
                block interlacing etc.; IMPOSSIBLE-GIVEN-MIXED-
                LADDER by the Sylvester gate, kept for logic); else
                BLOCK-SIGNATURE-STILL-MIXED (with the table).
  metricEnum := BLOCK-METRIC-MIXED-BY-INERTIA iff the inertia-sum
                law sum_n inertia(S_n) == (n_+, n_-) holds at every
                (pairing, rung) AND the ladder is mixed at every
                true rung -- the theorem-grade form of the kill: the
                entire J-congruence/Krylov class is closed, not
                merely searched; else INERTIA-LAW-BROKEN(where)
                (would be an arithmetic bug, abort-grade).
  chainEnum  := BLOCK-STURM-CHAIN-EXACT iff G24 passes everywhere
                (the reviewer's determinant identity delivered);
                else CHAIN-OBSTRUCTION(where).
  degEnum    := COORD-PAIRINGS-DEGENERATE-TO-SCALAR iff ADJPOLE and
                PARITY collapse to stage count 2(K-1) - 3 + 1 ...
                measured: stages == 2n/2 forms; frozen per rung in
                CAL_STAGES (the rank-one coupling forces the
                collapse; EULER/WRAP keep genuine 2x2 chains).
  scalarEnum := SCALAR-SIGNS-ARE-KREIN-COUNTS iff the scalar chain
                sign counts == (n_+, n_-) at every rung (Sylvester
                at block size 1; the r188 dead scalar structure
                re-instantiated in Lanczos dress).
  worldEnum  := DEFINITE-ONLY-IN-SMOOTH-BLOCK iff SMOOTH is all-ND
                with all-'pos' coefficient censuses while SCRARITH/
                EPSTEIN stay mixed in every intrinsic pairing --
                MIXEDNESS-IS-ARITHMETIC inherited (wrong
                orientation, NOT a sign source); else WORLD-MIXED.
  screenEnum := BLOCK-MARGIN-TAU-FLAT iff |slope| <= SLOPE_FLAT for
                the EULER mS ladder, else BLOCK-MARGIN-RIDES-TAU
                (the honest distinction demanded by the contract:
                STRUCTURAL-BLOCK-FORM-FOUND-MARGIN-RIDES would need
                chainEnum exact AND rides -- resolved from measured
                values either way).

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing beyond
frozen bars; ALL informed by the TWO DISCLOSED pre-freeze prototypes
proto_blocksturm_scratch.py / proto_blocksturm_symb.py at h = 4, 5,
8, 13 + all three controls, logs kept as
proto_blocksturm_scratch.out*.log / proto_blocksturm_symb.out1.log,
scripts deleted at freeze):
  P1 exact layer: dets EXACT at h = 4, 5 (all pairings, all K
     points, direct AND chain); mp worst rel <= 1.9e-187 at h = 13.
  P2 inertia-sum law holds at every cell; ladders == r188 frozen
     table (4: (1,5), 5: (7,3), 8: (6,14), 13: (27,14)).
  P3 censuses MIXED at every MAIN (pairing, rung); no breakdown;
     EULER/WRAP full 2x2 chains, ADJPOLE/PARITY degenerate to
     near-scalar (stages 5/9/19/40 at h = 4/5/8/13).
  P4 SMOOTH all-ND all-'pos' (block-definite after global flip);
     SCRARITH mixed with PARITY != ADJPOLE (j0 = 3); EPSTEIN mixed.
  P5 scalar sign counts == ladder at every rung and world.
  P6 EULER mS ladder O(1e-2..1e-5), tau-FLAT (prototype: 6.97e-4 /
     1.27e-2 / (h=8 measured at calibration) / 2.02e-4); Ahat
     margins collapse toward 0 at h >= 8 (near-singular A-blocks,
     recorded observable).
  P7 the parity pair is (1, 2) at every MAIN rung (PARITY ==
     ADJPOLE on MAIN, disclosed above).

RECORD TABLES (frozen at freeze from the disclosed prototype ladder
+ ONE structural smoke smoke1 (rungs 4/5 + SCRARITH, 25/25, 16.4 s,
euler_block_sturm_probe.smoke1.log) + ONE calibration pass
calib_ebs_pass1.log (25/25, all four rungs + all three controls,
178.4 s); house pattern identical to r195-r205; no bar, dps, rung,
seed or control recipe moved at any point; record tables inserted at
freeze).  Verdicts frozen from calibration:
CAL_LADDER {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14)} (== r188).
CAL_STAGES {h: {EULER, WRAP, ADJPOLE, PARITY}}: 4: (3, 3, 5, 5),
  5: (5, 5, 9, 9), 8: (10, 10, 19, 19), 13: (21, 21, 40, 40).
CAL_SCEN (S census (pd, ind, nd) per rung per pairing):
  4: E(0,1,2) W(0,1,2) A(0,1,4) P(0,1,4);
  5: E(3,1,1) W(2,3,0) A(6,1,2) P(6,1,2);
  8: E(0,6,4) W(1,4,5) A(5,1,13) P(5,1,13);
  13: E(9,10,2) W(9,10,2) A(26,1,13) P(26,1,13).
CAL_ACEN (Ahat census (pos, nn, mix, cplx)):
  4: E(1,0,1,0) W(1,0,1,0) A(3,0,1,0) P(3,0,1,0);
  5: E(2,0,2,0) W(1,0,2,1) A(4,0,4,0) P(4,0,4,0);
  8: E(2,0,7,0) W(1,0,8,0) A(7,0,11,0) P(7,0,11,0);
  13: E(5,0,12,3) W(2,0,17,1) A(13,0,26,0) P(13,0,26,0).
CAL_BCEN (Bhat census (pos, nn, mix, cplx)):
  4: E(2,0,1,0) W(2,0,1,0) A(4,0,1,0) P(4,0,1,0);
  5: E(3,0,2,0) W(4,0,1,0) A(7,0,2,0) P(7,0,2,0);
  8: E(5,0,5,0) W(7,0,3,0) A(12,0,7,0) P(12,0,7,0);
  13: E(10,1,9,1) W(12,1,8,0) A(30,0,10,0) P(30,0,10,0).
CAL_SSTR (scalar sign strings): 4: "-+----", 5: "-+-+++++-+",
  8: "-+-+-+------+-+-+---",
  13: "-+-+-+-+-+-+++++++-+++++-++-+-++-++-+-+-+".
CAL_MSLOG (EULER log10 mS per rung): 4: "-3.16", 5: "-1.90",
  8: "-3.18", 13: "-3.69".
CAL_MALOG (EULER log10 mA, recorded): 4: "-7.88", 5: "-14.57",
  8: "-22.93", 13: "-450.00" (floor: an Ahat block numerically
  singular -- near-deflation of the port Krylov flag).
CAL_MBLOG (EULER log10 mB, recorded): 4: "-5.52", 5: "-6.93",
  8: "-11.90", 13: "-450.00" (floor).
CAL_SLOPE_MS "+0.0260" (log10 mS_EULER vs log10 tau, 4 rungs:
  tau-FLAT).
CAL_J0 {4: 2, 5: 2, 8: 2, 13: 2} (MAIN parity pair index, 1-based).
CAL_CTRL: SMOOTH {ladder (0, 10), ADJPOLE/PARITY stages 9,
  S (0,0,9), Ahat (8,0,0,0), Bhat (9,0,0,0), scalar "----------"};
  SCRARITH {ladder (3, 7), j0 = 3, ADJPOLE S (2,0,7) A (5,0,3,0)
  B (7,0,2,0); PARITY S (2,1,6) A (4,0,4,0) B (7,0,2,0), scalar
  "--+-----++"}; EPSTEIN {ladder (3, 17), j0 = 2, ADJPOLE ==
  PARITY, S (2,1,16), A (14,0,4,0), B (17,0,2,0), stages 19,
  scalar "-----+---+-------+--"}.
CAL_DET (mp determinant identity, worst rel over pairings/points):
  8: 7.6e-125, 13: 1.9e-187 (h = 4, 5 EXACT at all K points).
AMENDMENTS: NONE at freeze (any post-freeze amendment would be
appended as a numbered block outside this docstring).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition + G03
roots/tau guard; S1 exact layer G10-G14 (sympy + integer instance);
S2 pencil + Lanczos + censuses G20-G26 (per rung, ProcessPool); S3
worlds G40-G42; S4 screens + guards G50-G53; S5 pricing + table
G60-G61 + G99 runtime.  DETERMINISM: no randomness anywhere;
ProcessPool results keyed; run2 must be identical modulo wall-clock
tokens (lines carrying 'WALL').

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
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction

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
EXACT_MAX = 5
WRAP_PRIME = {4: 2, 5: 2, 8: 3, 13: 7}
DET_PTS_MP = (2, 3, 5, 7, 11, 13)
PAIRINGS = ("EULER", "WRAP", "ADJPOLE", "PARITY")
WORLD_PAIRINGS = ("ADJPOLE", "PARITY")
CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
              ("EPSTEIN", 8, 80))

WARD_BAR = 1e-40
DET_BAR = 1e-100
SLOPE_FLAT = 0.30
LOG_TOL = 0.30
SLOPE_TOL = 0.10
MARGIN_FLOOR = -450.0

LADDER_TAB = {4: (1, 5), 5: (7, 3), 8: (6, 14), 13: (27, 14)}
LADDER_WORLD = {"SMOOTH": (0, 10), "SCRARITH": (3, 7),
                "EPSTEIN": (3, 17)}

# --------------------- calibrated record tables (calib_ebs_pass1.log)
CAL_STAGES = {4: (3, 3, 5, 5), 5: (5, 5, 9, 9), 8: (10, 10, 19, 19),
              13: (21, 21, 40, 40)}
CAL_SCEN = {
    4: {"EULER": (0, 1, 2), "WRAP": (0, 1, 2),
        "ADJPOLE": (0, 1, 4), "PARITY": (0, 1, 4)},
    5: {"EULER": (3, 1, 1), "WRAP": (2, 3, 0),
        "ADJPOLE": (6, 1, 2), "PARITY": (6, 1, 2)},
    8: {"EULER": (0, 6, 4), "WRAP": (1, 4, 5),
        "ADJPOLE": (5, 1, 13), "PARITY": (5, 1, 13)},
    13: {"EULER": (9, 10, 2), "WRAP": (9, 10, 2),
         "ADJPOLE": (26, 1, 13), "PARITY": (26, 1, 13)}}
CAL_ACEN = {
    4: {"EULER": (1, 0, 1, 0), "WRAP": (1, 0, 1, 0),
        "ADJPOLE": (3, 0, 1, 0), "PARITY": (3, 0, 1, 0)},
    5: {"EULER": (2, 0, 2, 0), "WRAP": (1, 0, 2, 1),
        "ADJPOLE": (4, 0, 4, 0), "PARITY": (4, 0, 4, 0)},
    8: {"EULER": (2, 0, 7, 0), "WRAP": (1, 0, 8, 0),
        "ADJPOLE": (7, 0, 11, 0), "PARITY": (7, 0, 11, 0)},
    13: {"EULER": (5, 0, 12, 3), "WRAP": (2, 0, 17, 1),
         "ADJPOLE": (13, 0, 26, 0), "PARITY": (13, 0, 26, 0)}}
CAL_BCEN = {
    4: {"EULER": (2, 0, 1, 0), "WRAP": (2, 0, 1, 0),
        "ADJPOLE": (4, 0, 1, 0), "PARITY": (4, 0, 1, 0)},
    5: {"EULER": (3, 0, 2, 0), "WRAP": (4, 0, 1, 0),
        "ADJPOLE": (7, 0, 2, 0), "PARITY": (7, 0, 2, 0)},
    8: {"EULER": (5, 0, 5, 0), "WRAP": (7, 0, 3, 0),
        "ADJPOLE": (12, 0, 7, 0), "PARITY": (12, 0, 7, 0)},
    13: {"EULER": (10, 1, 9, 1), "WRAP": (12, 1, 8, 0),
         "ADJPOLE": (30, 0, 10, 0), "PARITY": (30, 0, 10, 0)}}
CAL_SSTR = {4: "-+----", 5: "-+-+++++-+",
            8: "-+-+-+------+-+-+---",
            13: "-+-+-+-+-+-+++++++-+++++-++-+-++-++-+-+-+"}
CAL_MSLOG = {4: "-3.16", 5: "-1.90", 8: "-3.18", 13: "-3.69"}
CAL_MALOG = {4: "-7.88", 5: "-14.57", 8: "-22.93", 13: "-450.00"}
CAL_MBLOG = {4: "-5.52", 5: "-6.93", 8: "-11.90", 13: "-450.00"}
CAL_SLOPE_MS = "+0.0260"
CAL_J0 = {4: 2, 5: 2, 8: 2, 13: 2}
CAL_CTRL = {
    "SMOOTH": dict(j0=2, stages=9, scen=(0, 0, 9),
                   acen=(8, 0, 0, 0), bcen=(9, 0, 0, 0),
                   sstr="----------"),
    "SCRARITH": dict(j0=3, stages=9,
                     scen_a=(2, 0, 7), acen_a=(5, 0, 3, 0),
                     bcen_a=(7, 0, 2, 0),
                     scen_p=(2, 1, 6), acen_p=(4, 0, 4, 0),
                     bcen_p=(7, 0, 2, 0), sstr="--+-----++"),
    "EPSTEIN": dict(j0=2, stages=19, scen=(2, 1, 16),
                    acen=(14, 0, 4, 0), bcen=(17, 0, 2, 0),
                    sstr="-----+---+-------+--")}

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


def fit_line(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx else float("nan")


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
            "n" + "zeros", "gram" + "point", "poly" + "roots"}
    bad = []
    funcs = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs[node.name] = node
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
                bad.append("z-function use @%d" % node.lineno)
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
    # G03 leg: construct_* bodies never subscript builder-cell keys
    cellkey_bad = []
    for fname, fnode in funcs.items():
        if not fname.startswith("construct_"):
            continue
        for node in ast.walk(fnode):
            if isinstance(node, ast.Subscript) and isinstance(
                    node.slice, ast.Constant):
                if node.slice.value in ("mpE", "mpM", "mpV", "tau",
                                        "gap", "cn", "cn_mp_str"):
                    cellkey_bad.append("cellkey:%s:%s"
                                       % (fname, node.slice.value))
    return (not bad, not cellkey_bad,
            ("; ".join(bad + cellkey_bad) if (bad or cellkey_bad) else
             "NO zero-oracle, NO z-function, NO root extraction "
             "anywhere in this file, NO np.load, no verification/ "
             "import; construct_* functions never touch builder-cell "
             "keys (tau read once, per-rung scalar, screen only); "
             "fully zero-free; concurrent-lane files untouched"))


# ------------------------------------------------------- exact helpers
def mpf_frac(x) -> Fraction:
    sign, man, exp, _bc = x._mpf_
    if man == 0:
        if x == 0:
            return Fraction(0)
        raise ValueError("non-finite mpf")
    v = Fraction(int(man))
    v = v * (1 << exp) if exp >= 0 else v / (1 << (-exp))
    return -v if sign else v


def primes_upto(x: int) -> list:
    return [p for p in range(2, x + 1)
            if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]


def m_cap(p: int, h: int) -> int:
    m, q = 0, p
    while q <= h:
        m += 1
        q *= p
    return m


# --------------------------------------------- construction (source)
def construct_residues(cs, b, K):
    """rho ladder from source data (c_k, b_k) ONLY (exact)."""
    e = [cs[k] if k % 2 == 0 else -cs[k] for k in range(K)]
    A0 = sum(e)
    rho = [e[k] * b[k] / A0 for k in range(1, K)]
    npos = sum(1 for r in rho if r > 0)
    nneg = sum(1 for r in rho if r < 0)
    nzero = sum(1 for r in rho if r == 0)
    return dict(A0=A0, rho=rho, npos=npos, nneg=nneg, nzero=nzero)


def construct_ntilde(cs, b, K):
    """r188 unscaled cleared census numerator (Fraction, exact)."""
    e = [cs[k] if k % 2 == 0 else -cs[k] for k in range(K)]
    A0 = sum(e)
    rt = [e[k] * b[k] for k in range(1, K)]
    prod_u = [Fraction(1)]
    for k in range(1, K):
        new = [Fraction(0)] * (len(prod_u) + 1)
        for i, c in enumerate(prod_u):
            new[i] += c
            new[i + 1] += -b[k] * c
        prod_u = new
    ntil = [A0 * c for c in prod_u]
    for k in range(1, K):
        q = [prod_u[0]]
        for c in prod_u[1:-1]:
            q.append(c + q[-1] * b[k])
        off = len(ntil) - len(q)
        for j, c in enumerate(q):
            ntil[off + j] += rt[k - 1] * c
    return A0, ntil


def construct_channels(h, K, dps, only_p=None):
    """(u_k, v_k) = per-mode Euler value/jet channels, r202 closed
    forms VERBATIM, k = 1..K-1 (source atoms only, no cell data)."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        prs = primes_upto(h) if only_p is None else [only_p]
        u, v = [], []
        im1 = mp.mpc(0, 1)
        for k in range(1, K):
            om = oms[k]
            su = mp.mpf(0)
            sv = mp.mpf(0)
            for p in prs:
                lp = mp.log(p)
                M = m_cap(p, h)
                z = mp.exp(-lp / 2) * mp.exp(im1 * om * lp)
                S = lp * z * (1 - z ** M) / (1 - z)
                Sp = im1 * lp ** 2 * z * (1 - (M + 1) * z ** M
                                          + M * z ** (M + 1)) \
                    / (1 - z) ** 2
                su += mp.im(S)
                sv += mp.re(aa * S + im1 / 2 * Sp) \
                    - mp.im(S) / (2 * om)
            u.append(su)
            v.append(sv)
    return u, v


def mat_vec(A, x, n):
    return [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]


def met_inner(dmet, x, y, n):
    return sum(x[k] * dmet[k] * y[k] for k in range(n))


def inv_small(S):
    r = len(S)
    if r == 1:
        if S[0][0] == 0:
            return None
        one = Fraction(1) if isinstance(S[0][0], Fraction) \
            else mp.mpf(1)
        return [[one / S[0][0]]]
    d = S[0][0] * S[1][1] - S[0][1] * S[1][0]
    if d == 0:
        return None
    return [[S[1][1] / d, -S[0][1] / d],
            [-S[1][0] / d, S[0][0] / d]]


def construct_lanczos(A, dmet, V1, n, exact, zb=None):
    """Block-Lanczos, indefinite metric dmet, operator A; full
    re-J-orthogonalization; exact power-of-two column scaling."""
    Vs, Ss, Sinv, Gs, Hs = [], [], [], [], []
    ward_far = Fraction(0) if exact else 0.0
    breakdown = None
    cur = [list(c) for c in V1]
    total = 0
    stage = 0
    while True:
        red = []
        for c in cur:
            cc = list(c)
            for rcol in red:
                piv = None
                for i in range(n):
                    if (rcol[i] != 0) if exact \
                            else (abs(rcol[i]) > 0):
                        piv = i
                        break
                if piv is None:
                    continue
                f = cc[piv] / rcol[piv]
                cc = [cc[i] - f * rcol[i] for i in range(n)]
            if exact:
                nz = any(x != 0 for x in cc)
            else:
                nrm = mp.sqrt(sum(x * x for x in cc))
                nrm0 = mp.sqrt(sum(x * x for x in c)) + zb
                nz = nrm > zb * (1 + nrm0)
            if nz:
                if exact:
                    mx = max(abs(x) for x in cc if x != 0)
                    ex = mx.numerator.bit_length() \
                        - mx.denominator.bit_length()
                    sc = Fraction(1, 1 << ex) if ex >= 0 \
                        else Fraction(1 << (-ex))
                else:
                    mxv = max(abs(x) for x in cc)
                    ex = int(mp.floor(mp.log(mxv, 2))) \
                        if mxv > 0 else 0
                    sc = mp.mpf(2) ** (-ex)
                red.append([x * sc for x in cc])
        if not red:
            break
        cur = red
        r = len(cur)
        S = [[met_inner(dmet, cur[i], cur[j], n) for j in range(r)]
             for i in range(r)]
        Si = inv_small(S)
        if Si is None:
            breakdown = stage + 1
            break
        Vs.append(cur)
        Ss.append(S)
        Sinv.append(Si)
        total += r
        stage += 1
        W = [mat_vec(A, c, n) for c in cur]
        G = [[met_inner(dmet, cur[i], W[j], n) for j in range(r)]
             for i in range(r)]
        Gs.append(G)
        if total >= n:
            break
        R = [list(w) for w in W]
        for m in range(len(Vs)):
            Vm = Vs[m]
            rm = len(Vm)
            C = [[met_inner(dmet, Vm[i], W[j], n) for j in range(r)]
                 for i in range(rm)]
            Co = [[sum(Sinv[m][i][t] * C[t][j] for t in range(rm))
                   for j in range(r)] for i in range(rm)]
            if m < len(Vs) - 2:
                for i in range(rm):
                    for j in range(r):
                        val = C[i][j]
                        if exact:
                            ward_far = max(ward_far, abs(val))
                        else:
                            wn = mp.sqrt(sum(x * x for x in W[j]))
                            sc2 = max(abs(d2) for d2 in dmet) * wn
                            ward_far = max(
                                ward_far,
                                float(abs(val) / sc2)
                                if sc2 > 0 else float(abs(val)))
            for j in range(r):
                for i in range(n):
                    acc = R[j][i]
                    for t in range(rm):
                        acc -= Vm[t][i] * Co[t][j]
                    R[j][i] = acc
        cur = R
    for m in range(len(Vs) - 1):
        Vm, Vn = Vs[m], Vs[m + 1]
        Wn = [mat_vec(A, c, n) for c in Vn]
        H = [[met_inner(dmet, Vm[i], Wn[j], n)
              for j in range(len(Vn))] for i in range(len(Vm))]
        Hs.append(H)
    return dict(Vs=Vs, Ss=Ss, Sinv=Sinv, Gs=Gs, Hs=Hs,
                ward_far=ward_far, breakdown=breakdown, total=total)


def mat2mul(X, Y):
    rx, cx = len(X), len(X[0])
    cy = len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(cx))
             for j in range(cy)] for i in range(rx)]


def construct_coeffs(Ss, Sinv, Gs, Hs):
    """Bhat_n = Sinv_n G_n; Ahat_n = Sinv_n H^T Sinv_{n-1} H."""
    Bh = [mat2mul(Sinv[i], Gs[i]) for i in range(len(Gs))]
    Ah = []
    for i in range(1, len(Ss)):
        H = Hs[i - 1]
        Ht = [[H[a][b] for a in range(len(H))]
              for b in range(len(H[0]))]
        Ah.append(mat2mul(mat2mul(Sinv[i], Ht),
                          mat2mul(Sinv[i - 1], H)))
    return Bh, Ah


def construct_phi_chain(Ss, Gs, Hs, y, exact):
    """Adjugate-cleared block Sturm chain at point y (spec form)."""
    N = len(Ss)
    one = Fraction(1) if exact else mp.mpf(1)

    def E(m):
        r = len(Ss[m])
        return [[y * Ss[m][i][j] - Gs[m][i][j] for j in range(r)]
                for i in range(r)]

    def adj(X):
        r = len(X)
        if r == 1:
            return [[one]]
        return [[X[1][1], -X[0][1]], [-X[1][0], X[0][0]]]

    def det2(X):
        r = len(X)
        if r == 1:
            return X[0][0]
        return X[0][0] * X[1][1] - X[0][1] * X[1][0]

    Phi = E(0)
    Th_pp = one
    Th = det2(Phi)
    for m in range(1, N):
        H = Hs[m - 1]
        Ht = [[H[a][b] for a in range(len(H))]
              for b in range(len(H[0]))]
        mid = mat2mul(mat2mul(Ht, adj(Phi)), H)
        fac = one if len(Ss[m - 1]) == 2 else Th_pp
        Em = E(m)
        r = len(Em)
        Th_prev = Th
        Phi = [[Em[i][j] * Th_prev - mid[i][j] * fac
                for j in range(r)] for i in range(r)]
        Th = det2(Phi) / (Th_prev ** (r - 1)) if r == 2 \
            else det2(Phi)
        Th_pp = Th_prev
    return Th


def det_dense(M, n, exact):
    A = [list(r) for r in M]
    det = Fraction(1) if exact else mp.mpf(1)
    sgn = 1
    for k in range(n):
        piv = None
        if exact:
            for i in range(k, n):
                if A[i][k] != 0:
                    piv = i
                    break
        else:
            best = -1
            for i in range(k, n):
                v = abs(A[i][k])
                if v > best:
                    best, piv = v, i
            if best == 0:
                piv = None
        if piv is None:
            return det * 0
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            sgn = -sgn
        det *= A[k][k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    return det * sgn


def pencil_dense(Ss, Gs, Hs, y):
    sizes = [len(S) for S in Ss]
    n = sum(sizes)
    off = [0]
    for s in sizes:
        off.append(off[-1] + s)
    Z = [[0] * n for _ in range(n)]
    for m, S in enumerate(Ss):
        r = sizes[m]
        for i in range(r):
            for j in range(r):
                Z[off[m] + i][off[m] + j] = y * S[i][j] - Gs[m][i][j]
    for m, H in enumerate(Hs):
        r0, r1 = sizes[m], sizes[m + 1]
        for i in range(r0):
            for j in range(r1):
                Z[off[m] + i][off[m + 1] + j] = -H[i][j]
                Z[off[m + 1] + j][off[m] + i] = -H[i][j]
    return Z, n


# ---------------------------------------------------------- censuses
def inertia_small(S, exact, zb=None):
    r = len(S)
    if r == 1:
        v = S[0][0]
        if exact:
            return (1, 0) if v > 0 else ((0, 1) if v < 0 else (0, 0))
        return (1, 0) if v > zb else ((0, 1) if v < -zb else (0, 0))
    t = S[0][0] + S[1][1]
    d = S[0][0] * S[1][1] - S[0][1] * S[1][0]
    if exact:
        if d > 0:
            return (2, 0) if t > 0 else (0, 2)
        if d < 0:
            return (1, 1)
        return (1, 0) if t > 0 else ((0, 1) if t < 0 else (0, 0))
    sc = abs(S[0][0]) + abs(S[1][1]) + abs(S[0][1])
    if d > zb * sc * sc:
        return (2, 0) if t > 0 else (0, 2)
    if d < -zb * sc * sc:
        return (1, 1)
    return (1, 0) if t > zb * sc else ((0, 1) if t < -zb * sc
                                       else (0, 0))


def eig_census_small(Mb, exact, zb=None):
    r = len(Mb)
    if r == 1:
        v = Mb[0][0]
        pos = (v > 0) if exact else (v > zb)
        neg = (v < 0) if exact else (v < -zb)
        return "pos" if pos else ("mix" if neg else "nn")
    t = Mb[0][0] + Mb[1][1]
    d = Mb[0][0] * Mb[1][1] - Mb[0][1] * Mb[1][0]
    disc = t * t - 4 * d
    if exact:
        if disc < 0:
            return "cplx"
        if d > 0:
            return "pos" if t > 0 else "mix"
        if d < 0:
            return "mix"
        return "nn" if t >= 0 else "mix"
    sc = abs(Mb[0][0]) + abs(Mb[1][1]) + abs(Mb[0][1]) + abs(Mb[1][0])
    if disc < -zb * sc * sc:
        return "cplx"
    if d > zb * sc * sc:
        return "pos" if t > 0 else "mix"
    if d < -zb * sc * sc:
        return "mix"
    return "nn" if t >= -zb * sc else "mix"


def census_tuple(labels, order=("pos", "nn", "mix", "cplx")):
    c = Counter(labels)
    return tuple(c.get(k, 0) for k in order)


def s_census_tuple(iners):
    npd = sum(1 for i in iners if i in ((2, 0), (1, 0)))
    nind = sum(1 for i in iners if i == (1, 1))
    nnd = sum(1 for i in iners if i in ((0, 2), (0, 1)))
    return (npd, nind, nnd)


def s_margin_log10(Ss, exact):
    worst = None
    for S in Ss:
        r = len(S)
        if r == 1:
            continue
        if exact:
            fro2 = sum(mp.mpf((S[i][j] * S[i][j]).numerator)
                       / mp.mpf((S[i][j] * S[i][j]).denominator)
                       for i in range(r) for j in range(r))
            dd = S[0][0] * S[1][1] - S[0][1] * S[1][0]
            d = mp.mpf(dd.numerator) / mp.mpf(dd.denominator)
        else:
            fro2 = sum(S[i][j] * S[i][j] for i in range(r)
                       for j in range(r))
            d = S[0][0] * S[1][1] - S[0][1] * S[1][0]
        val = abs(d) / fro2 if fro2 > 0 else mp.mpf(0)
        worst = val if worst is None else min(worst, val)
    if worst is None or worst == 0:
        return MARGIN_FLOOR
    return max(float(mp.log(worst, 10)), MARGIN_FLOOR)


def eig_margin_log10(blocks, exact):
    worst = None
    for Mb in blocks:
        r = len(Mb)
        if r == 1:
            continue
        if exact:
            t = mp.mpf((Mb[0][0] + Mb[1][1]).numerator) \
                / mp.mpf((Mb[0][0] + Mb[1][1]).denominator)
            dd = Mb[0][0] * Mb[1][1] - Mb[0][1] * Mb[1][0]
            d = mp.mpf(dd.numerator) / mp.mpf(dd.denominator)
        else:
            t = Mb[0][0] + Mb[1][1]
            d = Mb[0][0] * Mb[1][1] - Mb[0][1] * Mb[1][0]
        disc = t * t - 4 * d
        if disc >= 0:
            sq = mp.sqrt(disc)
            l1, l2 = (t + sq) / 2, (t - sq) / 2
            mx, mn = max(abs(l1), abs(l2)), min(abs(l1), abs(l2))
        else:
            mx = mn = mp.sqrt(t * t / 4 + (-disc) / 4)
        val = mn / mx if mx > 0 else mp.mpf(0)
        worst = val if worst is None else min(worst, val)
    if worst is None:
        return 0.0
    if worst == 0:
        return MARGIN_FLOOR
    return max(float(mp.log(worst, 10)), MARGIN_FLOOR)


# ------------------------------------------------------- cell driver
def run_pairings(cs, b, K, h, dps, pairings, world):
    """The full battery on one cell; returns per-pairing data."""
    n = K - 1
    res = construct_residues(cs, b, K)
    rho, A0 = res["rho"], res["A0"]
    A0x, ntil = construct_ntilde(cs, b, K)
    exact = (h <= EXACT_MAX)
    out = dict(ladder=(res["npos"], res["nneg"]), nzero=res["nzero"])
    s0 = 1 if rho[0] > 0 else -1
    j0 = next((k for k in range(1, n)
               if (1 if rho[k] > 0 else -1) != s0), 1)
    out["j0"] = j0 + 1
    if exact:
        A = [[(b[i + 1] if i == j else Fraction(0)) - rho[j]
              for j in range(n)] for i in range(n)]
        dmet = rho
        zb = None
    else:
        with mp.workdps(2 * dps):
            rho_m = [mp.mpf(r.numerator) / mp.mpf(r.denominator)
                     for r in rho]
            b_m = [mp.mpf(v.numerator) / mp.mpf(v.denominator)
                   for v in b]
            A = [[(b_m[i + 1] if i == j else mp.mpf(0)) - rho_m[j]
                  for j in range(n)] for i in range(n)]
            dmet = rho_m
            zb = mp.mpf(10) ** (-(dps - 10))

    seeds = {}
    for name in pairings:
        if name == "EULER":
            u, v = construct_channels(h, K, dps)
            seeds[name] = (u, v)
        elif name == "WRAP":
            u, v = construct_channels(h, K, dps,
                                      only_p=WRAP_PRIME[h])
            seeds[name] = (u, v)
        elif name == "ADJPOLE":
            ei = [Fraction(0)] * n
            ej = [Fraction(0)] * n
            ei[0] = Fraction(1)
            ej[1] = Fraction(1)
            seeds[name] = (ei, ej)
        elif name == "PARITY":
            ep = [Fraction(0)] * n
            eq = [Fraction(0)] * n
            ep[0] = Fraction(1)
            eq[j0] = Fraction(1)
            seeds[name] = (ep, eq)

    pair_out = {}
    for name in pairings:
        c1, c2 = seeds[name]
        if exact:
            col1 = [x if isinstance(x, Fraction) else mpf_frac(x)
                    for x in c1]
            col2 = [x if isinstance(x, Fraction) else mpf_frac(x)
                    for x in c2]
            lz = construct_lanczos(A, dmet, [col1, col2], n, True)
        else:
            with mp.workdps(2 * dps):
                col1 = [x if not isinstance(x, Fraction)
                        else mp.mpf(x.numerator)
                        / mp.mpf(x.denominator) for x in c1]
                col2 = [x if not isinstance(x, Fraction)
                        else mp.mpf(x.numerator)
                        / mp.mpf(x.denominator) for x in c2]
                lz = construct_lanczos(A, dmet, [col1, col2], n,
                                       False, zb=zb)
        po = dict(breakdown=lz["breakdown"], total=lz["total"])
        if lz["breakdown"] is not None:
            pair_out[name] = po
            continue
        Ss, Sinv, Gs, Hs = lz["Ss"], lz["Sinv"], lz["Gs"], lz["Hs"]
        po["stages"] = len(Ss)
        iners = [inertia_small(S, exact, zb=zb) for S in Ss]
        po["isum"] = (sum(i[0] for i in iners),
                      sum(i[1] for i in iners))
        po["scen"] = s_census_tuple(iners)
        Bh, Ah = construct_coeffs(Ss, Sinv, Gs, Hs)
        po["bcen"] = census_tuple(
            [eig_census_small(Mb, exact, zb=zb) for Mb in Bh])
        po["acen"] = census_tuple(
            [eig_census_small(Mb, exact, zb=zb) for Mb in Ah])
        with mp.workdps(2 * dps):
            po["mS_log10"] = s_margin_log10(Ss, exact)
            po["mA_log10"] = eig_margin_log10(Ah, exact)
            po["mB_log10"] = eig_margin_log10(Bh, exact)
        po["ward_far"] = (lz["ward_far"] == 0) if exact \
            else float(lz["ward_far"])
        # determinant identity
        Vfull = []
        for blk in lz["Vs"]:
            Vfull.extend(blk)
        if exact:
            Vm = [[Vfull[j][i] for j in range(n)] for i in range(n)]
            detV = det_dense(Vm, n, True)
            detJ = Fraction(1)
            for r in dmet:
                detJ *= r
            ok_all = True
            for ypt in range(K):
                y = Fraction(ypt)
                Z, nn = pencil_dense(Ss, Gs, Hs, y)
                dz = det_dense(Z, nn, True)
                rhs = detV * detV * detJ \
                    * _peval_fr(ntil, y) / A0x
                th = construct_phi_chain(Ss, Gs, Hs, y, True)
                ok_all = ok_all and (dz == rhs) and (th == dz)
            po["det_exact_ok"] = ok_all
        else:
            with mp.workdps(2 * dps):
                Vm = mp.zeros(n, n)
                for i in range(n):
                    for j in range(n):
                        Vm[i, j] = Vfull[j][i]
                detV = mp.det(Vm)
                detJ = mp.mpf(1)
                for r in dmet:
                    detJ *= r
                worst = mp.mpf(0)
                zero_events = 0
                for ypt in DET_PTS_MP:
                    y = mp.mpf(ypt)
                    Z, nn = pencil_dense(Ss, Gs, Hs, y)
                    Zm = mp.zeros(nn, nn)
                    for i in range(nn):
                        for j in range(nn):
                            Zm[i, j] = Z[i][j]
                    dz = mp.det(Zm)
                    if dz == 0:
                        zero_events += 1
                        continue
                    ntv = mp.mpf(0)
                    for c in ntil:
                        ntv = ntv * y + (mp.mpf(c.numerator)
                                         / mp.mpf(c.denominator))
                    rhs = detV * detV * detJ * ntv \
                        / (mp.mpf(A0x.numerator)
                           / mp.mpf(A0x.denominator))
                    worst = max(worst, abs(dz - rhs) / abs(rhs))
                    th = construct_phi_chain(Ss, Gs, Hs, y, False)
                    worst = max(worst, abs(th - dz) / abs(dz))
                po["det_worst"] = float(worst)
                po["det_zero_events"] = zero_events
        pair_out[name] = po
    out["pairs"] = pair_out

    # scalar chain (seed ONES)
    if exact:
        lz = construct_lanczos(A, dmet, [[Fraction(1)] * n], n, True)
    else:
        with mp.workdps(2 * dps):
            lz = construct_lanczos(A, dmet, [[mp.mpf(1)] * n], n,
                                   False, zb=zb)
    if lz["breakdown"] is not None:
        out["scalar"] = dict(breakdown=lz["breakdown"])
    else:
        signs = []
        for S in lz["Ss"]:
            v = S[0][0]
            pos = (v > 0) if exact else (v > zb)
            signs.append("+" if pos else "-")
        out["scalar"] = dict(
            breakdown=None, stages=len(lz["Ss"]),
            sstr="".join(signs),
            counts=(sum(1 for s in signs if s == "+"),
                    sum(1 for s in signs if s == "-")))
    # gauge ward (exact rungs only, spec: h = 4): c -> (3/7) c
    if exact and h == 4 and world == "MAIN":
        cs_g = [Fraction(3, 7) * c for c in cs]
        rg = construct_residues(cs_g, b, K)
        out["gauge_ok"] = (rg["rho"] == rho)
    return out


def _peval_fr(p, x):
    acc = Fraction(0)
    for c in p:
        acc = acc * x + c
    return acc


# ------------------------------------------------------- workers
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            b_mp = [(k * mp.pi / aa) ** 2 for k in range(K)]
            cs_mp = [mp.mpf(s) for s in ce["cn_mp_str"]]
            tau = ce["mpE"][0]
            out["tau_log10"] = float(mp.log(abs(tau), 10))
        cs = [mpf_frac(v) for v in cs_mp]
        b = [mpf_frac(v) for v in b_mp]
        out["K_ok"] = (K == int(math.ceil(KFAC * h * math.log(h))))
        out.update(run_pairings(cs, b, K, h, dps, PAIRINGS, "MAIN"))
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
            b_mp = [(k * mp.pi / aa) ** 2 for k in range(K)]
            cs_mp = [mp.mpf(s) for s in ce["cn_mp_str"]]
        cs = [mpf_frac(v) for v in cs_mp]
        b = [mpf_frac(v) for v in b_mp]
        out.update(run_pairings(cs, b, K, x, dps, WORLD_PAIRINGS,
                                world))
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    y = sp.Symbol("y")

    # G10: mdl + metric symmetry, n = 2, 3
    ok10 = True
    for n in (2, 3):
        bs = sp.symbols("b1:%d" % (n + 1))
        rs = sp.symbols("r1:%d" % (n + 1))
        D = sp.diag(*bs)
        A = D - sp.ones(n, 1) * sp.Matrix([list(rs)]).reshape(1, n)
        lhs = (y * sp.eye(n) - A).det(method="berkowitz")
        rhs = sp.prod([y - bb for bb in bs]) \
            + sum(rs[k] * sp.prod([y - bs[j] for j in range(n)
                                   if j != k]) for k in range(n))
        ok10 &= sp.expand(lhs - rhs) == 0
        Jr = sp.diag(*rs)
        ok10 &= sp.expand(Jr * A - (Jr * A).T) == sp.zeros(n, n)
    check("G10-pencil-mdl-metric-symbolic", bool(ok10),
          "the r188 rational-coordinate pencil re-warded (generic "
          "n = 2, 3, sympy exact): det(yI - (D - ONES rho^T)) == "
          "prod(y - b_k) + sum_k rho_k prod_{j != k}(y - b_j) "
          "(matrix determinant lemma -- the census polynomial "
          "Ntilde/A_0 is the char poly of the SOURCE-SIDE operator "
          "A_ns) AND diag(rho) A_ns is SYMMETRIC -- A_ns is "
          "self-adjoint in the indefinite metric Jr = diag(rho): "
          "the block-Lanczos below runs in the exact Krein "
          "geometry of the r188 pencil, no similarity, no sqrt")

    # G11: adjugate-Sturm chain identity, sizes (2,2), (2,1,1), (1,2)
    def adjg(X):
        if X.shape[0] == 1:
            return sp.Matrix([[sp.Integer(1)]])
        return sp.Matrix([[X[1, 1], -X[0, 1]], [-X[1, 0], X[0, 0]]])

    def chain_ok(sizes, tagn):
        S, G, H = [], [], []
        for m, r in enumerate(sizes):
            S.append(sp.Matrix(r, r, lambda i, j: sp.Symbol(
                "%ss%d_%d%d" % (tagn, m, min(i, j), max(i, j)))))
            G.append(sp.Matrix(r, r, lambda i, j: sp.Symbol(
                "%sg%d_%d%d" % (tagn, m, min(i, j), max(i, j)))))
        for m in range(len(sizes) - 1):
            H.append(sp.Matrix(sizes[m], sizes[m + 1],
                               lambda i, j: sp.Symbol(
                                   "%sh%d_%d%d" % (tagn, m, i, j))))
        E = [y * S[m] - G[m] for m in range(len(sizes))]
        N = sum(sizes)
        P = sp.zeros(N, N)
        off = [0]
        for r in sizes:
            off.append(off[-1] + r)
        for m, r in enumerate(sizes):
            P[off[m]:off[m + 1], off[m]:off[m + 1]] = E[m]
        for m in range(len(sizes) - 1):
            P[off[m]:off[m + 1], off[m + 1]:off[m + 2]] = -H[m]
            P[off[m + 1]:off[m + 2], off[m]:off[m + 1]] = -H[m].T
        dP = P.det(method="berkowitz")
        Phi = E[0]
        Th_pp = sp.Integer(1)
        Th = Phi.det()
        for m in range(1, len(sizes)):
            fac = sp.Integer(1) if sizes[m - 1] == 2 else Th_pp
            mid = H[m - 1].T * adjg(Phi) * H[m - 1]
            Th_prev = Th
            Phi = sp.expand(E[m] * Th_prev - mid * fac)
            if sizes[m] == 2:
                num = Phi.det(method="berkowitz")
                quo, rem = sp.div(sp.expand(num),
                                  sp.expand(Th_prev), y)
                if sp.simplify(rem) != 0:
                    return False
                Th = quo
            else:
                Th = Phi[0, 0]
            Th_pp = Th_prev
        return sp.expand(Th - dP) == 0

    ok11 = chain_ok((2, 2), "a") and chain_ok((2, 1, 1), "b") \
        and chain_ok((1, 2), "c")
    # 2x2 adjugate identity adj X = tr(X) I - X
    X = sp.Matrix(2, 2, lambda i, j: sp.Symbol("x_%d%d" % (i, j)))
    ok11 &= sp.expand(adjg(X) - (sp.trace(X) * sp.eye(2) - X)) \
        == sp.zeros(2, 2)
    check("G11-adjugate-sturm-chain-symbolic", bool(ok11),
          "THE DELIVERED RECURSION IS EXACT (generic symmetric "
          "block-tridiagonal pencil, sizes (2,2), (2,1,1), (1,2), "
          "sympy exact incl. exact polynomial division): Phi_1 = "
          "E_1, Phi_m = E_m Theta_{m-1} - H^T adj(Phi_{m-1}) H "
          "Theta_{m-2}^(2-r'), Theta_m = det Phi_m / "
          "Theta_{m-1}^(r-1) ==> Theta_N == det(yM - G) -- the 2x2 "
          "matrix three-term/Sturm recursion (adj X = tr(X) I - X, "
          "gated) whose terminal scalar is the pencil determinant; "
          "with G24 this makes Theta_N == det(V)^2 det(Jr) N_h/A_0 "
          "a per-rung machine-checked identity: THE BLOCK STURM "
          "CHAIN FOR THE CENSUS EXISTS AND IS SOURCE-SIDE -- the "
          "reviewer's determinant target, delivered (positivity is "
          "a separate question, adjudicated by G22/G23)")

    # G12: one-step J-orthogonality (dim 4 generic)
    n = 4
    Jr = sp.diag(*sp.symbols("j1:5"))
    Sy = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "a_%d%d" % (min(i, j), max(i, j))))
    T = Jr.inv() * Sy
    V1 = sp.Matrix(n, 2, lambda i, j: sp.Symbol("w_%d%d" % (i, j)))
    S1 = V1.T * Jr * V1
    W = T * V1
    V2 = W - V1 * (S1.inv() * (V1.T * Jr * W))
    ok12 = sp.simplify(V2.T * Jr * V1) == sp.zeros(2, 2)
    check("G12-lanczos-jorth-step-symbolic", bool(ok12),
          "the block-Lanczos step is a J-orthogonal projection "
          "(generic J-self-adjoint T = Jr^{-1} Sym, generic 4x2 "
          "seed, sympy exact): V_2 = T V_1 - V_1 S_1^{-1} (V_1^T "
          "Jr T V_1) satisfies V_2^T Jr V_1 == 0; the full "
          "three-term property for J-self-adjoint operators is "
          "SOURCE-CLASSICAL (indefinite Lanczos) and is "
          "instantiated MACHINE-EXACTLY on the census data at "
          "h = 4, 5 (G21: far coefficients == 0 in Fraction "
          "arithmetic) and at 1e-40-class in mp (h = 8, 13)")

    # G13: block-rescaling similarity invariance (2x2 generic)
    Sn = sp.Matrix(2, 2, lambda i, j: sp.Symbol(
        "sn_%d%d" % (min(i, j), max(i, j))))
    Sm = sp.Matrix(2, 2, lambda i, j: sp.Symbol(
        "sm_%d%d" % (min(i, j), max(i, j))))
    Hm = sp.Matrix(2, 2, lambda i, j: sp.Symbol("hm_%d%d" % (i, j)))
    Gn = sp.Matrix(2, 2, lambda i, j: sp.Symbol(
        "gn_%d%d" % (min(i, j), max(i, j))))
    Cn = sp.Matrix(2, 2, lambda i, j: sp.Symbol("cn_%d%d" % (i, j)))
    Cm = sp.Matrix(2, 2, lambda i, j: sp.Symbol("cm_%d%d" % (i, j)))
    Bh = Sn.inv() * Gn
    Bh2 = (Cn.T * Sn * Cn).inv() * (Cn.T * Gn * Cn)
    okB = sp.simplify(Bh2 - Cn.inv() * Bh * Cn) == sp.zeros(2, 2)
    Ah = Sn.inv() * Hm.T * Sm.inv() * Hm
    Ah2 = (Cn.T * Sn * Cn).inv() * (Cm.T * Hm * Cn).T \
        * (Cm.T * Sm * Cm).inv() * (Cm.T * Hm * Cn)
    okA = sp.simplify(Ah2 - Cn.inv() * Ah * Cn) == sp.zeros(2, 2)
    check("G13-rescale-similarity-symbolic", bool(okA and okB),
          "the census is WELL-DEFINED (generic 2x2 blocks, sympy "
          "exact): under any block rescaling V_n -> V_n C_n the "
          "coefficients transform by SIMILARITY, Bhat -> C^{-1} "
          "Bhat C and Ahat -> C^{-1} Ahat C -- eigenvalue censuses "
          "and the inertia of S_n (congruence) are invariant: the "
          "probe's exact power-of-two column scaling changes NO "
          "gated observable, and the sign census is a property of "
          "the PAIRING, not of the normalization")

    # G14: fixed integer instance, exact Lanczos wards (dim 6)
    Jr_i = [Fraction(v) for v in (1, 1, -1, 1, -1, -1)]
    Sym_i = [[Fraction(1 + ((i * j + i + j) % 5))
              for j in range(6)] for i in range(6)]
    for i in range(6):
        Sym_i[i][i] += Fraction(7 + i)
    T_i = [[Sym_i[i][j] / Jr_i[i] for j in range(6)]
           for i in range(6)]
    V1_i = [[Fraction(1 if i == 0 else 0) for i in range(6)],
            [Fraction(1 if i == 1 else 0) for i in range(6)]]
    lz = construct_lanczos(T_i, Jr_i, V1_i, 6, True)
    ok14 = lz["breakdown"] is None and lz["ward_far"] == 0 \
        and lz["total"] == 6
    if ok14:
        # metric block-diagonality + det identity at 7 points
        Vfull = []
        for blk in lz["Vs"]:
            Vfull.extend(blk)
        Vm = [[Vfull[j][i] for j in range(6)] for i in range(6)]
        detV = det_dense(Vm, 6, True)
        detJ = Fraction(1)
        for r in Jr_i:
            detJ *= r
        for ypt in range(7):
            yq = Fraction(ypt)
            Z, nn = pencil_dense(lz["Ss"], lz["Gs"], lz["Hs"], yq)
            dz = det_dense(Z, nn, True)
            TmyI = [[(yq if i == j else Fraction(0)) - T_i[i][j]
                     for j in range(6)] for i in range(6)]
            rhs = detV * detV * detJ * det_dense(TmyI, 6, True) \
                * Fraction((-1) ** 6)
            th = construct_phi_chain(lz["Ss"], lz["Gs"], lz["Hs"],
                                     yq, True)
            ok14 = ok14 and (dz == rhs) and (th == dz)
    check("G14-integer-instance-exact", bool(ok14),
          "the implementation itself proven on a FIXED integer "
          "6x6 J-self-adjoint instance (Jr = diag(1,1,-1,1,-1,-1), "
          "integer Sym, seed (e_1, e_2)), pure Fraction "
          "arithmetic: far re-orthogonalization coefficients == 0 "
          "EXACTLY (three-term property), exhaustion 6/6, and "
          "det(yM - G) == det(V)^2 det(Jr) det(yI - T) == Theta_N "
          "at ALL 7 integer points y = 0..6 -- congruence, chain "
          "and determinant transfer machine-exact on a full "
          "instance before any physics data is touched")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("euler_block_sturm_probe -- PRIME.EULER.BLOCK.STURM.01  "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, okc, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/seeds/pairings/control recipes "
          "declared in the frozen spec (SPEC_SHA covers the "
          "declaration); the construction, the pairing battery, "
          "the Sylvester adjudication and ALL priors P1-P7 were "
          "derived in TWO DISCLOSED pre-freeze prototypes "
          "(proto_blocksturm_scratch / proto_blocksturm_symb, logs "
          "kept, scripts deleted at freeze); the WRAP primes are "
          "frozen from the r205 orbit record CAL_WRAP (inc), the "
          "parity seed from the source-side rho sign sequence; "
          "record tables frozen from the disclosed smoke + "
          "calibration ladder (house pattern); exact scope h <= 5 "
          "(Fraction on the dyadic rationalization), mp scope "
          "h = 8, 13 at 2x house dps")
    check("G03-roots-tau-guard", okc,
          "AST: construct_* functions never subscript builder-cell "
          "keys (mpE/mpM/mpV/tau/gap/cn*) -- they consume ONLY "
          "(c_k, b_k, rho_k) and the atom data of the Euler "
          "channels; NO root extraction exists anywhere in this "
          "file (firewall token class); the determinant identity "
          "is gated at INTERPOLATION POINTS, never at roots: the "
          "roots-as-input prohibition is machine-checked, census "
          "roots are never computed, let alone consumed")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy + integer instance)")
    exact_layer()

    # ------------------------------------------------------------ S2
    rungs = (4, 5) if smoke else RUNGS
    section("S2  PENCIL + BLOCK-LANCZOS (h = %s)" % str(rungs))
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
                res[outw["h"]] = outw
            else:
                cres[outw["world"]] = outw
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    cerrs = [w for w in cres if cres[w].get("err")]
    for w in cerrs:
        print("  [ERR] %s %s" % (w, cres[w]["err"]))
    if errs or cerrs:
        check("G20-build-ladder", False,
              "worker errors at %s %s" % (errs, cerrs))
        print("ABORT: worker errors")
        return 1

    check("G20-build-ladder", all(
        res[h]["K_ok"] and res[h]["nzero"] == 0
        and res[h]["ladder"] == LADDER_TAB[h]
        and res[h]["j0"] == CAL_J0[h] for h in rungs),
          "per rung: K == ceil(1.25 h log h); the EXACT residue "
          "ladder (n_+, n_-) == the r188 frozen table %s with "
          "n_0 == 0 (Fraction arithmetic on the dyadic "
          "rationalization -- the metric signature the Sylvester "
          "law must reproduce); parity flip index j0 == %s "
          "(PARITY == ADJPOLE on MAIN, disclosed P7)"
          % (str({h: LADDER_TAB[h] for h in rungs}),
             str({h: CAL_J0[h] for h in rungs})))

    ok21 = True
    det21 = []
    for h in rungs:
        for name in PAIRINGS:
            po = res[h]["pairs"][name]
            if po.get("breakdown") is not None:
                ok21 = False
                det21.append("%d/%s BREAKDOWN@%d"
                             % (h, name, po["breakdown"]))
                continue
            if h <= EXACT_MAX:
                ok21 = ok21 and (po["ward_far"] is True)
            else:
                ok21 = ok21 and po["ward_far"] <= WARD_BAR
            if not (calib or smoke):
                ok21 = ok21 and (po["stages"]
                                 == CAL_STAGES[h][
                                     PAIRINGS.index(name)])
    check("G21-tridiagonality-no-breakdown", ok21,
          "block-Lanczos at every (rung, pairing): NO metric "
          "breakdown anywhere; the three-term property holds "
          "MACHINE-EXACTLY at h <= 5 (far re-orthogonalization "
          "coefficients == 0 in Fraction arithmetic -- the "
          "classical indefinite-Lanczos lemma instantiated "
          "exactly on the census pencil) and to <= %.0e relative "
          "in mp at h = 8, 13; stage counts == frozen %s%s"
          % (WARD_BAR, str({h: CAL_STAGES[h] for h in rungs}),
             ("; " + "; ".join(det21)) if det21 else ""))

    ok22 = all(res[h]["pairs"][name]["isum"] == LADDER_TAB[h]
               for h in rungs for name in PAIRINGS)
    check("G22-sylvester-inertia-sum", ok22,
          "THE STRUCTURAL CENTERPIECE, gated at every (rung, "
          "pairing): sum_n inertia(S_n) == (n_+, n_-) EXACTLY -- "
          "blkdiag(S_n) = V^T Jr V is a real congruence, so "
          "Sylvester's law of inertia (SOURCE-CLASSICAL) forces "
          "the block metric to carry the FULL mixed r188 "
          "signature at every true rung, in EVERY pairing, EVERY "
          "starting block, EVERY block size: the PD-metric block-"
          "Stieltjes/Favard form is IMPOSSIBLE in the entire "
          "J-congruence/block-Krylov construction class -- the "
          "pairing cannot unmix the metric; the kill is inertia "
          "bookkeeping, NOT a failed search (enum "
          "BLOCK-METRIC-MIXED-BY-INERTIA)")

    ok23 = True
    if not (calib or smoke):
        for h in rungs:
            for name in PAIRINGS:
                po = res[h]["pairs"][name]
                ok23 = ok23 and po["scen"] == CAL_SCEN[h][name] \
                    and po["acen"] == CAL_ACEN[h][name] \
                    and po["bcen"] == CAL_BCEN[h][name]
    all_pos = {name: all(
        res[h]["pairs"][name]["scen"][1] == 0
        and res[h]["pairs"][name]["scen"][2] == 0
        and res[h]["pairs"][name]["acen"][2] == 0
        and res[h]["pairs"][name]["acen"][3] == 0
        and res[h]["pairs"][name]["bcen"][2] == 0
        and res[h]["pairs"][name]["bcen"][3] == 0
        for h in rungs) for name in PAIRINGS}
    winner = [name for name, okp in all_pos.items() if okp]
    check("G23-block-sign-census", ok23 and not winner,
          "THE DECISIVE TABLE (B1/B2; the round's first table, "
          "printed as BLOCKCENSUS lines in S5): the eigen-sign "
          "censuses of every S_n / Ahat_n / Bhat_n per pairing "
          "per rung == the frozen record; MIXED AT EVERY MAIN "
          "(pairing, rung) -- no predefined pairing yields "
          "all-PD/PSD blocks at even ONE rung, let alone all "
          "four: the reviewer's residual hope (positive "
          "coefficient spectra despite the indefinite metric) is "
          "measured DEAD on MAIN; the winner set is EMPTY: enum "
          "BLOCK-SIGNATURE-STILL-MIXED (the Stieltjes-consequence "
          "battery (H1/H2/H3 faces) has nothing to run on)")

    ok24 = True
    for h in rungs:
        for name in PAIRINGS:
            po = res[h]["pairs"][name]
            if h <= EXACT_MAX:
                ok24 = ok24 and po.get("det_exact_ok", False)
            else:
                ok24 = ok24 and po.get("det_worst", 1.0) <= DET_BAR \
                    and po.get("det_zero_events", 1) == 0
    check("G24-determinant-identity", ok24,
          "B3 DELIVERED at every (rung, pairing): det(yM - G) == "
          "det(V)^2 det(Jr) Ntilde(y)/A_0 AND the adjugate-Sturm "
          "chain Theta_N == the direct determinant -- EXACT "
          "Fraction equality at ALL K integer points y = 0..K-1 "
          "at h = 4, 5 (a degree-(K-1) polynomial identity is "
          "PROVEN by equality at K points: the block recursion "
          "reproduces the census polynomial COEFFICIENT-EXACTLY, "
          "source-side, roots never computed); mp worst rel dev "
          "%s (bar %.0e, points %s) at h = 8, 13; zero-det "
          "events: none"
          % (str({h: "%.1e" % max(
              res[h]["pairs"][nm].get("det_worst", 0.0)
              for nm in PAIRINGS) for h in rungs
              if h > EXACT_MAX}) or "exact",
             DET_BAR, str(DET_PTS_MP)))

    ok25 = True
    for h in rungs:
        sc = res[h]["scalar"]
        ok25 = ok25 and sc.get("breakdown") is None \
            and sc["counts"] == LADDER_TAB[h]
        if not (calib or smoke):
            ok25 = ok25 and sc["sstr"] == CAL_SSTR[h]
    check("G25-scalar-chain-krein-counts", ok25,
          "the SCALAR chain (seed = ONES, block size 1) at every "
          "rung: metric sign counts == (n_+, n_-) exactly "
          "(Sylvester at block size 1) with the frozen sign "
          "strings -- the r188 'scalar orthogonal-polynomial "
          "structure is dead' re-instantiated in Lanczos dress: "
          "the scalar recursion coefficients alternate sign "
          "exactly as the Krein signature dictates, at every "
          "rung; strings %s"
          % str({h: res[h]["scalar"]["sstr"] for h in rungs
                 if h <= 5}))

    check("G26-gauge-invariance", res[4].get("gauge_ok", False)
          if 4 in res else False,
          "the exact scale gauge at h = 4: c -> (3/7) c leaves "
          "every rho_k IDENTICALLY invariant (Fraction equality; "
          "rho_k = e_k b_k / A_0 is scale-free in the ray) -- the "
          "whole construction consumes the RAY, never tau; "
          "together with G03 this is the tau-screen's "
          "construction leg (r188 G03 scope verbatim)")

    # ------------------------------------------------------------ S3
    section("S3  WORLDS")
    smo = cres.get("SMOOTH")
    scr = cres.get("SCRARITH")
    ep = cres.get("EPSTEIN")
    ok40 = True
    if smo:
        pa = smo["pairs"]["ADJPOLE"]
        pp = smo["pairs"]["PARITY"]
        ok40 = (smo["ladder"] == LADDER_WORLD["SMOOTH"]
                and pa["scen"] == CAL_CTRL["SMOOTH"]["scen"]
                and pa["acen"] == CAL_CTRL["SMOOTH"]["acen"]
                and pa["bcen"] == CAL_CTRL["SMOOTH"]["bcen"]
                and pp["scen"] == CAL_CTRL["SMOOTH"]["scen"]
                and smo["scalar"]["sstr"]
                == CAL_CTRL["SMOOTH"]["sstr"]
                and pa["isum"] == LADDER_WORLD["SMOOTH"])
    check("G40-smooth-definite-block", bool(ok40 and smo) if smo
          else smoke,
          "skipped in smoke mode" if not smo else
          "THE CONTRAST WORLD: SMOOTH(5) has the one-signed "
          "ladder (0, 10) => Jr NEGATIVE DEFINITE, and indeed "
          "EVERY S_n is ND (census %s), EVERY Ahat and Bhat "
          "spectrum POSITIVE (%s / %s), scalar string all-minus "
          "-- after ONE GLOBAL SIGN FLIP the block(and scalar)-"
          "Stieltjes form EXISTS in the atom-free world: "
          "definiteness separates atoms-vs-no-atoms with the "
          "WRONG orientation for a sign source (r188 "
          "MIXEDNESS-IS-ARITHMETIC inherited at block level -- "
          "the arithmetic is exactly what breaks block "
          "positivity, so the block form is NOT a truth "
          "separator and never a positivity lever)"
          % (str(CAL_CTRL["SMOOTH"]["scen"]),
             str(CAL_CTRL["SMOOTH"]["acen"]),
             str(CAL_CTRL["SMOOTH"]["bcen"])))

    ok41 = True
    if scr:
        pa = scr["pairs"]["ADJPOLE"]
        pp = scr["pairs"]["PARITY"]
        ok41 = (scr["ladder"] == LADDER_WORLD["SCRARITH"]
                and scr["j0"] == CAL_CTRL["SCRARITH"]["j0"]
                and pa["scen"] == CAL_CTRL["SCRARITH"]["scen_a"]
                and pa["acen"] == CAL_CTRL["SCRARITH"]["acen_a"]
                and pa["bcen"] == CAL_CTRL["SCRARITH"]["bcen_a"]
                and pp["scen"] == CAL_CTRL["SCRARITH"]["scen_p"]
                and pp["acen"] == CAL_CTRL["SCRARITH"]["acen_p"]
                and pp["bcen"] == CAL_CTRL["SCRARITH"]["bcen_p"]
                and scr["scalar"]["sstr"]
                == CAL_CTRL["SCRARITH"]["sstr"]
                and pa["isum"] == LADDER_WORLD["SCRARITH"]
                and pp["isum"] == LADDER_WORLD["SCRARITH"])
    check("G41-scrarith-mixed-block", bool(ok41 and scr),
          "" if not scr else
          "SCRARITH(5): ladder (3, 7) mixed, and the ONLY control "
          "where the parity pairing SEPARATES from adjacent-pole "
          "(j0 = 3: the first sign flip sits one pole deeper) -- "
          "measured: ADJPOLE census %s vs PARITY census %s "
          "(different S and Ahat censuses, SAME mixed verdict): "
          "the pairing choice moves the mixedness AROUND the "
          "chain but Sylvester pins its total; inertia sums both "
          "== (3, 7)"
          % (str(CAL_CTRL["SCRARITH"]["scen_a"]),
             str(CAL_CTRL["SCRARITH"]["scen_p"])))

    ok42 = True
    if ep:
        pa = ep["pairs"]["ADJPOLE"]
        ok42 = (ep["ladder"] == LADDER_WORLD["EPSTEIN"]
                and pa["scen"] == CAL_CTRL["EPSTEIN"]["scen"]
                and pa["acen"] == CAL_CTRL["EPSTEIN"]["acen"]
                and pa["bcen"] == CAL_CTRL["EPSTEIN"]["bcen"]
                and ep["scalar"]["sstr"]
                == CAL_CTRL["EPSTEIN"]["sstr"]
                and pa["isum"] == LADDER_WORLD["EPSTEIN"])
    check("G42-epstein-mixed-block", bool(ok42 and ep) if ep
          else smoke,
          "skipped in smoke mode" if not ep else
          "EPSTEIN(8): ladder (3, 17) mixed, censuses == frozen "
          "(S %s, Ahat %s, Bhat %s), inertia sum == (3, 17) -- "
          "the fake-arithmetic world fails block positivity "
          "exactly as MAIN does (B4's expected refusal: block "
          "positivity fails in EVERY atom-bearing world; only "
          "the atom-free continuum is block-definite)"
          % (str(CAL_CTRL["EPSTEIN"]["scen"]),
             str(CAL_CTRL["EPSTEIN"]["acen"]),
             str(CAL_CTRL["EPSTEIN"]["bcen"])))

    # ------------------------------------------------------------ S4
    section("S4  TAU-SCREEN + GUARDS")
    xs = [res[h]["tau_log10"] for h in rungs]
    msl = [res[h]["pairs"]["EULER"]["mS_log10"] for h in rungs]
    sl_ms = fit_line(xs, msl) if len(rungs) > 1 else float("nan")
    if calib or smoke:
        for h in rungs:
            po = res[h]["pairs"]["EULER"]
            print("CAL margin h=%d mS %.2f mA %.2f mB %.2f tau %.2f"
                  % (h, po["mS_log10"], po["mA_log10"],
                     po["mB_log10"], res[h]["tau_log10"]))
        print("CAL slope_mS %+.4f" % sl_ms)
        ok50 = True
    else:
        ok50 = abs(sl_ms) <= SLOPE_FLAT and abs(
            sl_ms - float(CAL_SLOPE_MS)) <= SLOPE_TOL
        ok50 = ok50 and all(
            abs(res[h]["pairs"]["EULER"]["mS_log10"]
                - float(CAL_MSLOG[h])) <= LOG_TOL for h in rungs)
    screen_enum = "BLOCK-MARGIN-TAU-FLAT" if abs(sl_ms) \
        <= SLOPE_FLAT else "BLOCK-MARGIN-RIDES-TAU"
    check("G50-tau-screen", ok50,
          "the S-block indefiniteness margin (EULER pairing, "
          "scale-free min_n |det S_n|/fro^2): log10 ladder %s vs "
          "log10 tau %s -- slope %+.3f (bar %.2f): %s -- the "
          "block mixedness is NOT tau currency, it is an O(1)-"
          "class structural fact of the pairing (so the honest "
          "contract distinction resolves to BLOCK-SIGNATURE-"
          "STILL-MIXED with tau-flat margins, NOT to a tau-flat "
          "POSITIVITY -- there is no positivity whose margin "
          "could ride); Ahat/Bhat eigen-margin ladders RECORDED "
          "(mA %s, mB %s): near-singular Ahat blocks at h >= 8 "
          "-- near-deflation of the port Krylov flag, a measured "
          "observable, not claimed as a law"
          % (str({h: "%.1f" % res[h]["pairs"]["EULER"]["mS_log10"]
                  for h in rungs}),
             str({h: "%.1f" % res[h]["tau_log10"] for h in rungs}),
             sl_ms, SLOPE_FLAT, screen_enum,
             str({h: "%.0f" % res[h]["pairs"]["EULER"]["mA_log10"]
                  for h in rungs}),
             str({h: "%.0f" % res[h]["pairs"]["EULER"]["mB_log10"]
                  for h in rungs})))

    delivered = {
        "ATOMS": ["EULER-CHANNELS"], "MODES": ["EULER-CHANNELS"],
        "RAY-RESIDUES": ["KREIN-PENCIL"],
        "EULER-CHANNELS": ["BLOCK-LANCZOS"],
        "KREIN-PENCIL": ["BLOCK-LANCZOS"],
        "BLOCK-LANCZOS": ["STURM-CHAIN", "SIGN-CENSUS"],
        "STURM-CHAIN": ["SCREENS"],
        "SIGN-CENSUS": ["SCREENS"], "SCREENS": []}
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
    for node in ("STURM-CHAIN", "SIGN-CENSUS", "SCREENS"):
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
          "ancestry of every delivered node clean; the round is "
          "per-rung finite linear algebra on source data; fully "
          "zero-free, no ordinate cache, no root ever computed")

    check("G52-composed-chain-typing", True,
          "leg typing: {mdl/metric symmetry, adjugate-Sturm chain "
          "identity, one-step J-orth, rescale similarity} EXACT "
          "(sympy); {integer instance, h <= 5 dets, ladders, "
          "inertia sums, gauge} EXACT-FRACTION; {h = 8, 13 dets, "
          "wards} EXACT-MP (1e-100/1e-40 class); {sign censuses, "
          "margins, stage counts} MEASURED; {Sylvester inertia "
          "law, indefinite-Lanczos three-term} SOURCE-CLASSICAL; "
          "the residual object -- a SOURCE-SIDE PD-metric "
          "realization of the census OUTSIDE the J-congruence/"
          "Krylov class -- remains open and is priced: any "
          "root-side construction is forbidden (roots-as-input), "
          "any congruence-side construction is now CLOSED by "
          "inertia; the wall's mixed signature stays the wall in "
          "block dress: relabeling barrier named, not crossed")

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
    cf.update({("UNC", "BLOCKSTIELTJES"): INF,
               ("BLOCKSTIELTJES", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'a source-side PD block-Stieltjes realization of the "
          "census exists cofinally' as a unit edge would raise "
          "the flow to 6 -- NOT REAL (the Sylvester gate closes "
          "the congruence class; a PD realization would carry H2 "
          "structurally, which is exactly the wall's realness "
          "face): this round adds NO flow; census cardinality "
          "UNCHANGED; RH unreachable without the omega edges")

    # ------------------------------------------------------------ S5
    section("S5  PRICING + BLOCKCENSUS TABLE")
    primary = "BLOCK-STIELTJES-FOUND" if winner \
        else "BLOCK-SIGNATURE-STILL-MIXED"
    check("G60-pricing", True,
          "WHAT THE ROUND BUYS: (i) B3 DELIVERED -- the census "
          "polynomial IS the terminal determinant of an explicit "
          "2x2 block-Jacobi/Sturm three-term recursion (the "
          "adjugate-Sturm chain), source-side, coefficient-exact "
          "at h <= 5, roots never consumed -- the reviewer's "
          "determinant identity exists; (ii) B1/B2 ADJUDICATED AT "
          "THEOREM GRADE: the pairing hope dies not by search but "
          "by Sylvester -- the block metric MUST carry the mixed "
          "r188 signature in every pairing (inertia-sum gate), "
          "and the measured coefficient censuses (the residual "
          "hope outside the congruence argument) are mixed at "
          "every MAIN cell too; (iii) the block margins are "
          "tau-FLAT: the mixedness is an O(1) structural fact, "
          "not a near-collapse artifact; (iv) worlds: only the "
          "atom-free continuum is block-definite (wrong "
          "orientation, inherited) -- what it does NOT buy "
          "(priced): H2/H1/H3 gain NOTHING (no positivity "
          "exists to transfer); the surviving open door is a "
          "PD realization OUTSIDE the congruence class, which "
          "no known source-side construction reaches -- the "
          "{H1 ^ H2 ^ H3}-KOFINAL residue is UNCHANGED")

    nlines = 0
    for h in rungs:
        for name in PAIRINGS:
            po = res[h]["pairs"][name]
            print("  BLOCKCENSUS h=%d pair=%s stages=%d "
                  "S=(%d,%d,%d) isum=(%d,%d) A=(%d,%d,%d,%d) "
                  "B=(%d,%d,%d,%d) mS=%.2f"
                  % ((h, name, po["stages"]) + po["scen"]
                     + po["isum"] + po["acen"] + po["bcen"]
                     + (po["mS_log10"],)))
            nlines += 1
        print("  BLOCKCENSUS h=%d SCALAR stages=%d counts=(%d,%d) "
              "str=%s" % (h, res[h]["scalar"]["stages"],
                          res[h]["scalar"]["counts"][0],
                          res[h]["scalar"]["counts"][1],
                          res[h]["scalar"]["sstr"]))
        nlines += 1
    for w in sorted(cres):
        cw = cres[w]
        for name in WORLD_PAIRINGS:
            po = cw["pairs"][name]
            print("  BLOCKCENSUS world=%s pair=%s stages=%d "
                  "S=(%d,%d,%d) isum=(%d,%d) A=(%d,%d,%d,%d) "
                  "B=(%d,%d,%d,%d)"
                  % ((w, name, po["stages"]) + po["scen"]
                     + po["isum"] + po["acen"] + po["bcen"]))
            nlines += 1
        print("  BLOCKCENSUS world=%s SCALAR counts=(%d,%d) str=%s"
              % (w, cw["scalar"]["counts"][0],
                 cw["scalar"]["counts"][1], cw["scalar"]["sstr"]))
        nlines += 1
    exp_lines = len(rungs) * (len(PAIRINGS) + 1) \
        + len(cres) * (len(WORLD_PAIRINGS) + 1)
    check("G61-blockcensus-table", nlines == exp_lines,
          "the pairing-battery sign census table: %d BLOCKCENSUS "
          "lines (expected %d) -- per (rung, pairing) the stage "
          "count, S-census (pd, ind, nd), the Sylvester inertia "
          "sum, the Ahat/Bhat eigen censuses (pos, nn, mix, cplx) "
          "and the S-margin; per rung the scalar chain; per world "
          "the intrinsic pairings -- the round's decisive data, "
          "delivered as a table as the contract demands"
          % (nlines, exp_lines))

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the census has an exact source-side 2x2 "
         "block-Sturm recursion (determinant identity coefficient-"
         "exact), but NO pairing can make it Stieltjes -- Sylvester "
         "pins the mixed r188 signature into the block metric of "
         "EVERY pairing, and the measured coefficient spectra are "
         "mixed too; margins tau-flat; only the atom-free world is "
         "block-definite.  The r188 scalar death extends to the "
         "block level BY THEOREM within the congruence class.  "
         "Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        primary + "(G23: winner set empty; mixed at every MAIN "
        "cell)",
        "BLOCK-METRIC-MIXED-BY-INERTIA(G22: Sylvester closes the "
        "whole congruence/Krylov class)",
        "BLOCK-STURM-CHAIN-EXACT(G11/G14/G24: det identity "
        "coefficient-exact at h <= 5, 1e-100-class mp)",
        "COORD-PAIRINGS-DEGENERATE-TO-SCALAR(G21 stages: the "
        "rank-one coupling collapses ADJPOLE/PARITY)",
        "SCALAR-SIGNS-ARE-KREIN-COUNTS(G25)",
        "DEFINITE-ONLY-IN-SMOOTH-BLOCK(G40-G42: "
        "MIXEDNESS-IS-ARITHMETIC inherited)",
        screen_enum + "(G50: slope %+.2f)" % sl_ms,
        "ROOTS-NEVER-CONSUMED(G01/G03) + TAU-FREE-CONSTRUCTION"
        "(G26)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51)",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED(G52/G60)",
        "MINCUT-UNCHANGED(G53) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc2, _d in CHECKS if okc2)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc2, _ in CHECKS if not okc2]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        primary, "BLOCK-METRIC-MIXED-BY-INERTIA",
        "BLOCK-STURM-CHAIN-EXACT",
        "COORD-PAIRINGS-DEGENERATE-TO-SCALAR",
        "SCALAR-SIGNS-ARE-KREIN-COUNTS",
        "DEFINITE-ONLY-IN-SMOOTH-BLOCK", screen_enum,
        "ROOTS-NEVER-CONSUMED", "TAU-FREE-CONSTRUCTION",
        "LOOPS-FLAGGED-NOT-CONSUMED",
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
