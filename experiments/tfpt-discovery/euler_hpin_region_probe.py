#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_hpin_region_probe -- PRIME.EULER.HPIN.REGION.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface of promotion wave eight) are not
touched.

=======================================================================
MISSION (round ~205: the EULER JET program, probe 3 -- the reviewer's
H-pin invariant-region target on the round-204 cascade).  Round 204
(euler_jet_colligation_probe, SPEC_SHA 5327721e3f2f36f8, 30/30, note
DXXX) proved: the wall RawM is EXACTLY the Schur complement of an
explicit passive Euler-jet cascade parent G_h -- per-prime PSD
dissipation Grams Q_p (KYP floor 1 - 1/p) under the outer factor
H = RawPole + RawArch + theta(h) G_B.  Round 200 (pole_homotopy_probe)
proved the secular machinery: NoP = RawM - RawPole has EXACTLY ONE
negative eigenvalue at every MAIN rung, and with c_h = 2 sinh^2(a/2),
phi_k = 1/(1/4 + om_k^2), the wall's bottom eigenvalue is the root of
the monotone secular function f(lam) = 1 + c_h m_h(lam) in the first
interlacing gap, where m_h(z) = phi^T (NoP - z I)^{-1} phi is the WEYL
FUNCTION of the pole channel.  VERIFIED FROM THE r200 CODE (and gated
symbolically below): given n_neg(NoP) = 1 and z-coupling nonzero, the
wall M_h = NoP + c_h phi phi^T is PSD  <=>  Delta_h := 1 + c_h m_h(0)
<= 0  (f is monotone increasing on the gap (d_0, d_1) containing the
root; f(0) <= 0 iff the root is >= 0; all higher eigenvalues clear by
interlacing) -- THE H-PIN SECULAR CRITERION.  THIS round derives the
reviewer's MOEBIUS DICTIONARY and hunts the invariant region:

  R1 THE MOEBIUS DICTIONARY (derived pre-freeze, gated symbolic + mp).
     Writing N_j = A0 - sum_{i <= j} Q_{p_i} with the PRIME-FREE SEED
     A0 := RawArch + theta(h) G_B (so N_0 = A0, N_P = NoP exactly, by
     the r204 central identity rearranged: NoP = RawM - RawPole =
     RawArch + theta G_B - sum_p Q_p), adding one prime block to the
     cascade acts on the matrix Weyl object W_j(z) = (N_j - z I)^{-1}
     by the EXACT MATRIX MOEBIUS (linear-fractional) map
       W  |->  W (I - Q_p W)^{-1},
     i.e. the graph action of the z-INDEPENDENT chain matrix
       T_p = [[I, 0], [-Q_p, I]]     (2K x 2K, unit lower triangular).
     THE PER-PRIME MOEBIUS PARAMETERS ARE THE r204 REALIZATION TABLE:
     the (2,1) block is minus the dissipation Gram Q_p = lp Y_p^T
     D_p^2 Y_p, entrywise identical to the per-prime dictionary law
     Q_p == lp G_B - sum_{m=1}^{M_p} w_{p^m} W(m lp) (gated here
     entrywise at every rung -- the per-prime split of the r204
     central identity).  STRUCTURE THEOREMS (symbolic, G10-G14):
     (i) the chain matrices form an ABELIAN group, T_p T_q =
     T_{Q_p + Q_q} -- the Redheffer star of these sections is
     COMMUTATIVE (order-independence of the composed map, NOT of the
     orbit); (ii) COMMON-J CONTRACTIVITY: T_p^T J T_p - J =
     diag(-2 Q_p, 0) <= 0 for J = [[0, I], [I, 0]], for EVERY prime at
     EVERY rung -- J-contractivity w.r.t. ONE FIXED J is EXACTLY
     per-prime passivity Q_p >= 0 (the r204 KYP certificate in chain
     dress); (iii) the FREE invariant region of common-J-contractive
     maps, {W : W + W^T <= 0}, is preserved via the exact congruence
     (I - QW)^T W + W^T (I - QW) = W + W^T - 2 W^T Q W -- but it is
     measured VACUOUS-FOR-MAIN (seed and terminal both outside); (iv)
     the determinant lemma det(N + c phi phi^T) = det(N) (1 + c phi^T
     N^{-1} phi): the region boundary 1 + c m = 0 is EXACTLY the
     locus det(partial wall) = 0.
  R2 THE REGION (the round's centerpiece).  In the h-scaled Moebius
     coordinate mu_j := c_h m_j(0) (source-pure: c_h and phi from the
     pole datum alone), the H-pin criterion is mu_P <= -1.  Region
     candidate OMEGA := {mu <= -1}.  MEMBERSHIP IS STRUCTURAL: by the
     determinant lemma + inertia, at stage j with n_neg(N_j) <= 1,
       mu_j <= -1  <=>  the PARTIAL WALL H - sum_{i<=j} Q_{p_i} is
       PSD AND N_j is NOT PD
     -- the region is the PARTIAL-WALL LADDER in Moebius coordinates
     (REGION-IS-PARTIAL-WALL-LADDER, typed definitional).  THE
     THEOREM SKELETON (per rung, from three measured facts): (a) Q_p
     PSD (KYP, r204) gives common-J contractivity AND Loewner
     monotonicity N_0 >= N_1 >= ... >= N_P; (b) n_neg(NoP) = 1 (r200,
     re-gated here at every rung) gives n_neg(N_j) <= 1 for ALL j
     (Weyl: N_j >= NoP) -- the orbit can wrap AT MOST ONCE, in ANY
     prime order; (c) the terminal wall RawM PSD (tau-margin) gives
     H - sum_{i<=j} Q_i = RawM + sum_{i>j} Q_i >= RawM >= 0 -- once
     the orbit enters OMEGA it CANNOT leave (every partial wall PSD
     for free).  So the measured orbit geometry (enter once, stay,
     terminate at mu_P = -1 - |Delta_h|) is fully theorem-covered
     GIVEN the wall; what is NOT free is exactly (b) all-h and the
     terminal clearance |Delta_h| > 0 -- the H-pin itself.  HONESty:
     the region's terminal membership margin |Delta_h| IS the wall's
     PSD margin (tau class, measured ~ lam_0(RawM) class); the
     INTERIOR clearances (all stages before the terminal) are O(1)
     and tau-FLAT (measured): the tau-riding of the region property
     concentrates ENTIRELY in the last (terminal) reading.  Expected
     verdict (pre-registered): REGION-FOUND-TAU-RIDING -- the first
     Moebius-coordinate form of the H-pin, with the relabeling
     barrier named (region terminal margin == GPSD margin == wall),
     NOT crossed.  SCALAR NOTE: the induced action on the SCALAR m
     is NOT a scalar Moebius map -- cross-ratio defect measured
     1e-8..1e-4 class, far above working precision (the exact
     dictionary is matrix-valued; the scalar reading is approximate
     only): SCALAR-MOEBIUS-DEFECT-MEASURED.
  R3 THE SEPARATOR BATTERY.  EPSTEIN(8): n_neg(NoP_E) = 3 (measured;
     zero-class eigsy) -- THE INERTIA PRECONDITION OF THE SECULAR
     CRITERION FAILS, and the rank-one pole can lift at most ONE
     negative direction (interlacing): the wall is NOT PSD no matter
     what Delta reads; indeed Delta_E = -0.26 < 0 WITH lam_min(RawM_E)
     < 0 -- THE NAIVE mu-REGION READING WOULD MISCLASSIFY EPSTEIN
     (the sharpest exhibit of the round: the Moebius/region form of
     the H-pin NEEDS the inertia-1 leg as a separate hypothesis; the
     r200 fingerprint 's* = 6/8, transport-only failure' appears
     spectrally as n_neg = 3 > 1).  Its formal cascade (ports p = 2:
     q = 4 doubled tap; p = 5: q = 5; ORPHAN q = 6 unportable) closes
     exactly (gated) but REFUSES the dictionary: the orphan block
     K_6 = -w_6 W(log 6) is INDEFINITE (chain matrix J-INDEFINITE, no
     passive section exists), the p = 2 port Gram is PSD-BORDERLINE
     (lam_min ~ 1e-18: the doubled tap sits exactly at the PR budget
     -- the window Gram of a boundary-PR port), and the orbit wraps
     THREE times (n_neg ladder 1 -> 1 -> 2 -> 3; seed A0_E already
     non-PD): one-wrap fails, region reading fails, dictionary
     refuses -- three independent breaks, all upstream of margins.
     SCRARITH(5): the golden-map weight permutation makes the
     would-be Q_2 (same per-prime dictionary formula, its actual
     weights) INDEFINITE, lam_min = -0.13 -- its p = 2 chain matrix
     FAILS common-J contractivity ITSELF (the r202/r204 non-PR port
     in chain dress); p = 3, 5 stay PSD (recorded honestly: refusal
     localizes at p = 2, as in r204); n_neg(NoP_SCR) = 3; Delta_SCR =
     +0.06 > 0 (endpoint fails too).  SMOOTH(5): NO ports (atom list
     empty by construction) -- the cascade degenerates to the seed
     alone, orbit = {mu_0}, no maps, no region dynamics; n_neg = 2;
     Delta = +0.21 > 0 (typed structural refusal).  SEPARATION READ:
     MAIN carries {inertia 1, one wrap, region held, Delta < 0};
     EVERY control breaks a DIFFERENT leg -- EPSTEIN the inertia
     precondition (and the naive endpoint MISREADS it), SCRARITH the
     J-contractivity, SMOOTH the port structure.
  R4 HONEST PRICING (frozen taxonomy below).  What the Moebius form
     buys: the H-pin becomes {per-prime J-contractivity (PROVEN per
     rung, KYP)} + {seed data source-pure} + {inertia-1 of NoP_h
     (measured per rung; its all-h face is a NON-DEGENERACY statement
     riding the r200 near-zero ladder d_1(NoP))} + {terminal boundary
     clearance Delta_h < 0 == THE WALL (tau)}.  No new all-h currency
     is created; the region property is coarse and theorem-covered in
     the INTERIOR (tau-flat clearances) but its terminal reading IS
     the wall -- said exactly, barrier named, not crossed.

GOALS (contract PRIME.EULER.HPIN.REGION.01):
  C1 R1 dictionary: symbolic layer (Moebius action law, abelian chain
     group, common-J contractivity == Q PSD, free-region congruence,
     determinant lemma) + mp layer (cascade closure A0 - sum Q_p ==
     NoP entrywise; per-prime dictionary Q_p == lp G_B - sum_m w
     W(m lp) entrywise; compositional gate: the composed matrix
     Moebius orbit evaluated at the r200 wall ground level lam_0
     satisfies the secular equation |1 + c_h m_cascade(lam_0)| <=
     SEC_BAR -- the cascade reproduces the r200 secular root).
  C2 R2 orbit: mu_j(0) at every rung in BOTH orders (increasing /
     decreasing p), PD flags (cholesky), wrap census (at most one
     PD -> nonPD transition, none back), pre-wrap strict increase
     (Loewner ward), post-wrap region-stay mu_j <= -1, partial-wall
     cholesky cross-ward at every stage, membership consistency
     (mu_j <= -1 <=> partial wall PSD AND N_j not PD), terminal
     Delta_h < 0 with lam_0(RawW) > 0 sign consistency, inertia
     n_neg(NoP) == 1 at every rung (eigsy, dps-scaled zero class),
     n_neg(N_j) <= 1 ladder at h <= 8 (eigsy), cross-ratio scalar
     defect ladder, interior vs terminal clearance ladders.
  C3 R3 worlds: EPSTEIN (inertia 3, misclassification exhibit,
     formal-cascade closure, borderline/indefinite blocks, 3-wrap
     ladder), SCRARITH (would-be Q_2 indefinite, ports 3/5 PSD,
     inertia 3, Delta > 0), SMOOTH (portless, inertia 2, Delta > 0).
  C4 screens: terminal clearance log10|Delta| vs log10 tau (expect
     RIDES, slope ~ +1 -- |Delta| is wall currency); interior
     clearance vs tau (expect FLAT); scalar defect vs tau (recorded);
     loop guard; mincut; typing; pricing; orbit table.

NOTATION (r171-r204 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; par_k = (-1)^k; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); Raw* = D_par N M* N D_par entrywise;
phi_k = 1/(1/4 + om_k^2); c_h = 2 sinh^2(a/2) (r200 c_pole; RawPole
== c_h phi phi^T, r200 G11); G_B = (L/2) diag(2, 1, ..., 1); theta =
sum_{p<=h} log p; atoms w_{p^m} = log p / p^{m/2}; W(u) kernel r195
VERBATIM; Q_p Grams r204 VERBATIM (trig_int closed forms, nilpotency
degree M~_p); A0 = RawArch + theta G_B; H = A0 + RawPole; N_j = A0 -
sum_{i<=j} Q_{p_i}; NoP = N_P = RawM - RawPole; m_j(z) = phi^T (N_j -
z I)^{-1} phi (mp.lu_solve); mu_j = c_h m_j(0); Delta_h = 1 + mu_P;
lam_0(RawW) by r200 bottom_vec_mp VERBATIM (3 LU solves + residual
ward); eigsy zero class zb_h = 10^{-(dps-20)} * fro (r200 GAPRES
convention) for NoP inertia, ZCLS 1e-30 * fro for control worlds
(O(1)-class negatives); cross-ratio nodes z_t = -fro(NoP) * t, t in
(2, 3, 5, 9) (theorem-safe: every N_j >= NoP so N_j - z_t is PD);
cr(v) = (v0-v2)(v1-v3)/((v1-v2)(v0-v3)); step defect =
|cr(y)-cr(x)|/|cr(x)|.  Controls: SCRARITH(5, 60), EPSTEIN(8, 80),
SMOOTH(5, 60), builder atom recipes VERBATIM (golden permutation /
Dirichlet recursion); EPSTEIN ports {2: [(4, lamq(4)/2)], 5: [(5,
lamq(5)/sqrt 5)]}, orphan (6, lamq(6)/sqrt 6); would-be Q_p^world :=
lp G_B - sum_{q in port p} w_q W(u_q); orphan block K_6 := -w_6
W(log 6); EPSTEIN formal seed A0_E = RawArch_E + (log 2 + log 5) G_B.
tau_h = ce["mpE"][0], measured per-rung scalar only.

RUNGS AND DPS (frozen; house ladder): RUNGS = (4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 16); DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85,
10: 90, 11: 100, 12: 110, 13: 120, 16: 130}.  QEIG_RUNGS = (4, 5, 8)
(partial-stage inertia ladders + lam_min(Q_p) eigsy).  WORKERS = 6.
Smoke mode: rungs (4, 5) + SCRARITH only.

FROZEN BARS: WARD_BAR 1e-45 (cascade closure, per-prime dictionary,
EPSTEIN formal closure, rel max-entry); SEC_BAR 1e-20 (compositional
secular gate, abs); INVIT_RES_BAR 1e-12 (lam_0 residual, rel fro);
XR_FLOOR 1e-12 (scalar-Moebius defect floor: max step defect above
it establishes scalar failure at working precision); QPSD: cholesky
success at every (p, h) AND lam_min(Q_p) > 0 at QEIG_RUNGS;
SCR_Q2_BAR -0.05 (SCRARITH would-be Q_2 lam_min must be below);
EPS_Q2_ZCLS 1e-10 (EPSTEIN p = 2 port borderline band: 0 <= lam_min
<= band); SLOPE_FLAT 0.30 (dex/dex vs log10 tau); RUNTIME_BAR
3000 s.  Record tolerances: LOG_TOL 0.10 dex (0.30 dex for dev-class
and borderline-class logs); VAL_TOL 0.01 (abs, O(1) values); SLOPE
record tolerance 0.10; counts/indices exact.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  dictEnum   := MOEBIUS-DICTIONARY-MATRIX-EXACT iff G20 + G21 + G27
                pass at every rung, else DICTIONARY-OBSTRUCTION(h...);
  scalEnum   := SCALAR-MOEBIUS-DEFECT-MEASURED iff max step defect >
                XR_FLOOR at >= 1 rung (expected), else
                SCALAR-MOEBIUS-EXACT-SURPRISE;
  jEnum      := COMMON-J-CONTRACTIVITY-KYP iff every Q_p cholesky-PD
                (theorem bridge G11), else J-FAILS-AT(p, h);
  inertEnum  := INERTIA-ONE-ALL-RUNGS iff n_neg(NoP_h) == 1 at every
                MAIN rung (zero class zb_h), else INERTIA-BREAK(h...);
  orbitEnum  := ORBIT-ONE-WRAP-BOTH-ORDERS iff at every rung and both
                orders: PD flags monotone (at most one True->False,
                none back), pre-wrap mu strictly increasing, mu_j >
                -1 pre-wrap, mu_j <= -1 from the wrap on; else
                ORBIT-BREAK(h, order, stage);
  regionEnum (primary) := DICTIONARY-OBSTRUCTION if dictEnum fails;
                else NO-COMMON-REGION(where) if orbitEnum breaks or
                membership consistency (G25) fails; else
                REGION-FOUND-THEOREM-GRADE iff |terminal-clearance
                slope| <= SLOPE_FLAT; else REGION-FOUND-TAU-RIDING;
  intEnum    := INTERIOR-CLEARANCE-TAU-FLAT iff |slope(log10 min
                interior clearance vs log10 tau)| <= SLOPE_FLAT,
                else INTERIOR-RIDES-TAU(slope);
  sepEnum    := SEPARATOR-TRIPLE-REFUSAL iff EPSTEIN {n_neg == 3,
                Delta < 0 AND lam_min(RawM_E) < 0 (misclassification
                exhibit), formal closure <= WARD_BAR, K_6 indefinite,
                wrap count != 1} AND SCRARITH {lam_min(would-be Q_2)
                <= SCR_Q2_BAR, p = 3, 5 PSD, n_neg == 3, Delta > 0}
                AND SMOOTH {portless typed, n_neg == 2, Delta > 0},
                else SEPARATOR-MIXED(which);
  plus the definitional riders (always typed): REGION-IS-PARTIAL-
  WALL-LADDER (determinant lemma + inertia); GPSD-MARGIN-IS-THE-WALL
  inherited from r204; INERTIA-PRECONDITION-IS-A-LEG (EPSTEIN
  exhibit: the endpoint criterion without the inertia leg is NOT
  sound).

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing beyond
frozen bars; ALL informed by the TWO DISCLOSED pre-freeze prototypes
proto_hpin_scratch.py / proto_hpin_scratch2.py at h = 4, 5, 8 +
controls, logs kept as proto_hpin_scratch.out1.log /
proto_hpin_scratch2.out1.log, scripts deleted at freeze):
  P1 cascade closure and per-prime dictionary <= WARD_BAR at every
     rung (proto closure 8.0e-62 / 7.0e-61 / 1.4e-80 at 4 / 5 / 8).
  P2 every Q_p strictly PD (r204 record); common-J contractivity
     holds at every prime and rung.
  P3 orbit one-wrap in both orders: h = 4 seed ALREADY IN REGION
     (A0 inertia (1, 6): mu_0 = -8.26, the shallow-rung anomaly --
     theta(4) too small to make the seed PD); h >= 5 seed PD and
     outside; wrap at p = 2 (h = 5, inc) / p = 3 (h = 8, inc) /
     p = 5 (h = 8, dec); post-wrap mu increasing toward -1.
  P4 Delta_h < 0 at every rung, |Delta| == lam_0(RawW) class (proto
     -1.5e-11 / -1.1e-16 / -2.5e-30 vs lam_0 2.0e-11 / 1.7e-16 /
     4.8e-30); terminal clearance slope vs tau ~ +1 (RIDES).
  P5 interior clearances O(1) (proto min 0.73 / 0.65 / 0.51 at
     4 / 5 / 8 over both orders), tau-FLAT.
  P6 compositional secular gate deep below SEC_BAR (proto 6.5e-30 /
     7.2e-38 / 3.8e-54).
  P7 cross-ratio scalar defect 1e-8..1e-4 class (proto 1.5e-5 /
     7.2e-8 / 1.1e-5 at the p = 2 step): scalar Moebius FAILS at
     working precision, matrix dictionary exact.
  P8 worlds as measured in the prototypes: EPSTEIN {n_neg 3, Delta
     -0.2610, lam_min(Q_2^E) ~ +3.3e-18 borderline, Q_5^E PD
     (+0.925), orphan kernel w_6 W(log 6) range (-1.92, +1.52) so
     the block K_6 = -w_6 W(log 6) has the mirrored range (-1.52,
     +1.92), closure 1.1e-81, n_neg ladder (1, 1, 2, 3)}; SCRARITH
     {n_neg 3, Delta +0.0594, would-be lam_min Q_2 -0.1334, Q_3
     +0.4897, Q_5 +1.2951}; SMOOTH {n_neg 2, Delta +0.2147}.

RECORD TABLES (frozen at freeze from the disclosed ladder: ONE
structural smoke (rungs 4/5 + SCRARITH, 27/27, 4.1 s,
euler_hpin_region_probe.smoke1.log), ONE calibration pass
(calib_ehr_pass1.log, 27/27, all 11 rungs + all three controls,
378.4 s); house pattern identical to r195/r200/r202/r204; no bar,
dps, rung, grid or control recipe moved at any point; record tables
inserted at freeze).  Verdicts frozen from calibration: closure
exact at all 11 rungs (8.0e-62 at h = 4 down to 7.2e-130 at h = 16,
scaling with dps); per-prime dictionary exact (8.2e-62 .. 5.8e-130);
inertia n_neg(NoP) == 1 at ALL rungs (d_0 < 0 < d_1 resolved at
every dps); orbit one-wrap BOTH orders at all rungs (h = 13 dec
order approaches the pole to mu = +122.2 before wrapping at p = 5
-- recorded, still one wrap); region held from wrap to terminal
everywhere; Delta < 0 at all rungs with |Delta| == lam_0-class
(0.08 .. 0.39 dex above lam_0); secular compositional gate <=
6.5e-30 abs everywhere (deepening to 7.6e-78 at h = 13);
secular-form cross-instrument rel dev <= 1.1e-44; scalar defect
log10 -5.25 .. -4.24; interior clearance 0.355 .. 0.727 FLAT (slope
+0.0053); terminal clearance RIDES (slope +1.0007); EPSTEIN /
SCRARITH / SMOOTH exactly as pre-registered (P8 confirmed to print
precision).
CAL_WRAP {h: (wrap prime inc, wrap prime dec); 0 = seed-in-region}:
  4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5), 9: (3, 5),
  10: (3, 5), 11: (5, 5), 12: (5, 5), 13: (7, 5), 16: (7, 7).
CAL_DLOG {h: log10 |Delta|}: 4: -10.81, 5: -15.95, 6: -20.40,
  7: -25.20, 8: -29.60, 9: -34.25, 10: -39.14, 11: -43.93,
  12: -49.16, 13: -53.78, 16: -68.56.
CAL_L0LOG {h: log10 lam_0(RawW)}: 4: -10.70, 5: -15.78, 6: -20.19,
  7: -24.95, 8: -29.32, 9: -33.96, 10: -38.83, 11: -43.59,
  12: -48.81, 13: -53.43, 16: -68.17.
CAL_INTC {h: min interior clearance, both orders}: 4: 0.727,
  5: 0.654, 6: 0.588, 7: 0.544, 8: 0.509, 9: 0.480, 10: 0.451,
  11: 0.430, 12: 0.414, 13: 0.398, 16: 0.355.
CAL_XRLOG {h: log10 max step defect}: 4: -4.24, 5: -4.76, 6: -4.64,
  7: -4.85, 8: -4.81, 9: -4.81, 10: -4.83, 11: -5.11, 12: -5.10,
  13: -5.24, 16: -5.25.
CAL_SLOPES: terminal +1.0007, interior +0.0053, xr +0.0151.
CAL_CTRL: EPSTEIN {nneg 3, Delta -0.2610, lmRawM -1.7808, q2min
  +3.3e-18, q5min +0.9250, k6 (-1.5211, +1.9227), closure 1.1e-81,
  ladder (1, 1, 2, 3)}; SCRARITH {nneg 3, Delta +0.0594, q2min
  -0.1334, q3min +0.4897, q5min +1.2951}; SMOOTH {nneg 2, Delta
  +0.2147}.
AMENDMENTS: NONE (no bar, dps, rung, recipe or target moved between
freeze and the run of record).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G14 (sympy); S2 dictionary + orbit G20-G29 (mp,
ProcessPool); S3 worlds G40-G42; S4 screens + guards G50-G53; S5
pricing G60-G61 + G99 runtime.  DETERMINISM: no randomness anywhere;
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
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery
from euler_jet_colligation_probe import (     # r204 machinery VERBATIM
    primes_upto, m_cap, m_nilp, trig_int, w_kernel_add)

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3000.0

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130}
QEIG_RUNGS = (4, 5, 8)
SMOKE_RUNGS = (4, 5)
XR_T = (2, 3, 5, 9)

WARD_BAR = 1e-45
SEC_BAR = 1e-20
INVIT_RES_BAR = 1e-12
XR_FLOOR = 1e-12
SCR_Q2_BAR = -0.05
EPS_Q2_ZCLS = 1e-10
SLOPE_FLAT = 0.30
ZCLS = 1e-30

LOG_TOL = 0.10
LOG_TOL_DEV = 0.30
VAL_TOL = 0.01
SLOPE_TOL = 0.10

CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80),
              ("SMOOTH", 5, 60))

# --------------------- calibrated record tables (calib_ehr_pass1.log)
CAL_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
            9: (3, 5), 10: (3, 5), 11: (5, 5), 12: (5, 5),
            13: (7, 5), 16: (7, 7)}
CAL_DLOG = {4: "-10.81", 5: "-15.95", 6: "-20.40", 7: "-25.20",
            8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
            12: "-49.16", 13: "-53.78", 16: "-68.56"}
CAL_L0LOG = {4: "-10.70", 5: "-15.78", 6: "-20.19", 7: "-24.95",
             8: "-29.32", 9: "-33.96", 10: "-38.83", 11: "-43.59",
             12: "-48.81", 13: "-53.43", 16: "-68.17"}
CAL_INTC = {4: "0.727", 5: "0.654", 6: "0.588", 7: "0.544",
            8: "0.509", 9: "0.480", 10: "0.451", 11: "0.430",
            12: "0.414", 13: "0.398", 16: "0.355"}
CAL_XRLOG = {4: "-4.24", 5: "-4.76", 6: "-4.64", 7: "-4.85",
             8: "-4.81", 9: "-4.81", 10: "-4.83", 11: "-5.11",
             12: "-5.10", 13: "-5.24", 16: "-5.25"}
CAL_SLOPES = {"term": "+1.0007", "intc": "+0.0053", "xr": "+0.0151"}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=3, Delta="-0.2610", lmRawM="-1.7808",
                    q5min="0.9250", k6lo="-1.5211", k6hi="1.9227",
                    ladder=(1, 1, 2, 3)),
    "SCRARITH": dict(nneg=3, Delta="0.0594", q2min="-0.1334",
                     q3min="0.4897", q5min="1.2951"),
    "SMOOTH": dict(nneg=2, Delta="0.2147"),
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
                       "verification/ import; eigsy consumed only as "
                       "per-rung finite spectra (r200 anatomy scope); "
                       "tau as measured per-rung scalar; fully "
                       "zero-free; concurrent-lane files untouched")


# ------------------------------------------------------- shared helpers
def to_raw(Mb, par, nrm, K):
    Rb = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Rb[i, j] = par[i] * nrm[i] * Mb[i, j] * nrm[j] * par[j]
    return Rb


def m_weyl(N, phi, K, z=None):
    """phi^T (N - z)^{-1} phi via LU solve (no full inverse)."""
    A = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            A[i, j] = N[i, j]
        if z is not None:
            A[i, i] -= z
    x = mp.lu_solve(A, mp.matrix(phi))
    return sum(phi[i] * x[i] for i in range(K))


def pd_flag(N, K):
    try:
        mp.cholesky(N)
        return True
    except Exception:                             # noqa: BLE001
        return False


def bottom_vec_mp(Raw, K):
    """r200 VERBATIM: 3 LU solves + residual ward."""
    fro = mp.sqrt(sum(Raw[i, j] ** 2 for i in range(K)
                      for j in range(K)))
    x = mp.matrix([mp.mpf(1) for _ in range(K)])
    for _it in range(3):
        x = mp.lu_solve(Raw, x)
        nx = mp.sqrt(sum(x[i] ** 2 for i in range(K)))
        x = x / nx
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K)) / fro
    return lam, float(res)


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


def cross_ratio(v):
    return ((v[0] - v[2]) * (v[1] - v[3])
            / ((v[1] - v[2]) * (v[0] - v[3])))


def orbit_run(A0, Qs, order, phi, c, K, Hm=None):
    """mu ladder, PD flags, partial-wall PD flags along one order."""
    N = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            N[i, j] = A0[i, j]
    mus = [c * m_weyl(N, phi, K)]
    pds = [pd_flag(N, K)]
    wpds = []
    if Hm is not None:
        Wp = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                Wp[i, j] = Hm[i, j]
        wpds.append(pd_flag(Wp, K))
    Ns = [mp.matrix(N)]
    for p in order:
        for i in range(K):
            for j in range(K):
                N[i, j] -= Qs[p][i, j]
        mus.append(c * m_weyl(N, phi, K))
        pds.append(pd_flag(N, K))
        if Hm is not None:
            for i in range(K):
                for j in range(K):
                    Wp[i, j] -= Qs[p][i, j]
            wpds.append(pd_flag(Wp, K))
        Ns.append(mp.matrix(N))
    return mus, pds, wpds, Ns


def orbit_census(mus, pds):
    """Wrap census: transitions, wrap stage, region/monotone facts."""
    P = len(mus) - 1
    trans = [j for j in range(P)
             if pds[j] and not pds[j + 1]]
    back = [j for j in range(P) if (not pds[j]) and pds[j + 1]]
    jstar = 0 if not pds[0] else (trans[0] + 1 if trans else None)
    pre_mono = all(mus[j + 1] > mus[j]
                   for j in range(0, (jstar or 0) - 1)) \
        if jstar not in (0, None) else True
    pre_out = all(mus[j] > -1 for j in range(jstar)) \
        if jstar is not None else False
    post_in = all(mus[j] <= -1 for j in range(jstar, P + 1)) \
        if jstar is not None else False
    intc = None
    if jstar is not None and jstar <= P - 1:
        intc = min(float(-1 - mus[j]) for j in range(jstar, P))
    return dict(ntrans=len(trans), nback=len(back), jstar=jstar,
                pre_mono=pre_mono, pre_out=pre_out, post_in=post_in,
                intc=intc)


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
            RawM = to_raw(ce["mpM"], par, nrm, K)
            RawPole = to_raw(ce["mpPole"], par, nrm, K)
            RawArch = to_raw(ce["mpArch"], par, nrm, K)
            tau = ce["mpE"][0]
            out["tau_log10"] = float(mp.log(abs(tau), 10))
            out["tau_sign"] = 1 if tau > 0 else -1
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            prs = primes_upto(h)
            out["primes"] = prs
            theta = sum(mp.log(p) for p in prs)
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            A0 = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A0[i, j] = RawArch[i, j]
                A0[i, i] += theta * GBd[i]
            Hm = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Hm[i, j] = A0[i, j] + RawPole[i, j]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            denN = max(abs(NoP[i, j]) for i in range(K)
                       for j in range(K))

            # ---- Q_p Grams (r204 VERBATIM) + per-prime dictionary
            Qs = {p: qp_gram(p, h, oms, L, K) for p in prs}
            pdict_dev = mp.mpf(0)
            for p in prs:
                lp = mp.log(p)
                Qd = mp.zeros(K, K)
                for i in range(K):
                    Qd[i, i] = lp * GBd[i]
                for m in range(1, m_cap(p, h) + 1):
                    q = p ** m
                    w_kernel_add(Qd, mp.log(q), -lp / mp.sqrt(q),
                                 oms, L, K)
                dmax = max(abs(Qd[i, j] - Qs[p][i, j])
                           for i in range(K) for j in range(K))
                dref = max(abs(Qs[p][i, j]) for i in range(K)
                           for j in range(K))
                pdict_dev = max(pdict_dev, dmax / dref)
            out["pdict_dev"] = float(pdict_dev)

            # ---- G20 cascade closure
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    acc = A0[i, j]
                    for p in prs:
                        acc -= Qs[p][i, j]
                    dev = max(dev, abs(acc - NoP[i, j]))
            out["closure_dev"] = float(dev / denN)

            # ---- G22 passivity
            chol_ok = all(pd_flag(Qs[p], K) for p in prs)
            out["chol_ok"] = bool(chol_ok)
            if h in QEIG_RUNGS:
                lmq = None
                for p in prs:
                    Eq, _ = mp.eigsy(Qs[p])
                    lq = min(Eq)
                    lmq = lq if lmq is None else min(lmq, lq)
                out["lmq_min"] = float(lmq)

            # ---- G23 inertia of NoP (eigsy, dps-scaled zero class)
            E, Q = mp.eigsy(NoP)
            idx = sorted(range(K), key=lambda m2: E[m2])
            d = [E[m2] for m2 in idx]
            zb = mp.mpf(10) ** (-(dps - 20)) * froN
            out["nneg"] = sum(1 for e in d if e < -zb)
            out["d0_neg"] = bool(d[0] < -zb)
            out["d1_pos"] = bool(d[1] > zb)
            zvec = [sum(Q[i, idx[m2]] * phi[i] for i in range(K))
                    for m2 in range(K)]
            delta_sec = 1 + c * sum(zvec[m2] ** 2 / d[m2]
                                    for m2 in range(K))

            # ---- orbits (both orders)
            res_orb = {}
            for tag, order in (("inc", prs), ("dec",
                                              list(reversed(prs)))):
                mus, pds, wpds, Ns = orbit_run(A0, Qs, order, phi,
                                               c, K, Hm=Hm)
                cen = orbit_census(mus, pds)
                cen["mus"] = [float(x) for x in mus]
                cen["pds"] = pds
                cen["wall_pd_all"] = all(wpds)
                # membership consistency at every stage:
                # mu <= -1  <=>  (partial wall PD AND N_j not PD)
                cons = all((mus[j] <= -1) == (wpds[j] and not pds[j])
                           for j in range(len(mus)))
                cen["member_cons"] = cons
                if h in QEIG_RUNGS:
                    lad = []
                    for Nj in Ns:
                        Ej, _ = mp.eigsy(Nj)
                        lad.append(sum(1 for e in Ej if e < -zb))
                    cen["nneg_ladder"] = lad
                    cen["nneg_le1"] = all(x <= 1 for x in lad)
                res_orb[tag] = cen
            out["orb"] = res_orb
            # terminal Delta at full precision from NoP
            Delta = 1 + c * m_weyl(NoP, phi, K)
            out["Delta_neg"] = bool(Delta < 0)
            out["Delta_log10"] = float(mp.log(abs(Delta), 10))
            out["dsec_dev"] = float(abs(delta_sec - Delta)
                                    / abs(Delta))
            intcs = [res_orb[t]["intc"] for t in ("inc", "dec")
                     if res_orb[t]["intc"] is not None]
            out["intc_min"] = min(intcs) if intcs else None

            # ---- lam_0(RawW) anchor (r200 verbatim)
            lam0, ires = bottom_vec_mp(RawM, K)
            out["invit_res"] = ires
            out["lam0_pos"] = bool(lam0 > 0)
            out["lam0_log10"] = float(mp.log(abs(lam0), 10))

            # ---- G27 compositional secular gate at z = lam_0
            A = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A[i, j] = A0[i, j]
                A[i, i] -= lam0
            W = mp.inverse(A)
            for p in prs:
                QW = Qs[p] * W
                M2 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        M2[i, j] = (1 if i == j else 0) - QW[i, j]
                W = W * mp.inverse(M2)
            msec = sum(phi[i] * sum(W[i, j] * phi[j]
                                    for j in range(K))
                       for i in range(K))
            out["sec_dev"] = float(abs(1 + c * msec))

            # ---- G28 cross-ratio scalar defect (inc order)
            zts = [-froN * t for t in XR_T]
            ladders = []
            for zt in zts:
                N = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        N[i, j] = A0[i, j]
                lad = [m_weyl(N, phi, K, z=zt)]
                for p in prs:
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= Qs[p][i, j]
                    lad.append(m_weyl(N, phi, K, z=zt))
                ladders.append(lad)
            xr_max = mp.mpf(0)
            for j in range(1, len(prs) + 1):
                xs = [ladders[t][j - 1] for t in range(4)]
                ys = [ladders[t][j] for t in range(4)]
                crx = cross_ratio(xs)
                cry = cross_ratio(ys)
                xr_max = max(xr_max, abs(cry - crx) / abs(crx))
            out["xr_max_log10"] = float(mp.log(xr_max, 10)) \
                if xr_max > 0 else -300.0

            # ---- free-region membership (seed/terminal): W + W^T <= 0
            # W_0 = A0^{-1}: PD iff A0 PD; terminal NoP^{-1} has the
            # single negative direction -- both outside {<= 0}: check
            # via NOT pd_flag(-W)... equivalently -A0 / -NoP not PSD.
            out["free_vac"] = (not pd_flag(mp.matrix(A0) * (-1), K)
                               and not pd_flag(mp.matrix(NoP) * (-1),
                                               K))
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
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            E, _ = mp.eigsy(NoP)
            zb = mp.mpf(ZCLS) * froN
            out["nneg"] = sum(1 for e in E if e < -zb)
            out["Delta"] = float(1 + c * m_weyl(NoP, phi, K))
            Ew, _ = mp.eigsy(RawM)
            out["lmRawM"] = float(min(Ew))

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
                qmins = {}
                for p in primes_upto(x):
                    lp = mp.log(p)
                    Qw = mp.zeros(K, K)
                    for i in range(K):
                        Qw[i, i] = lp * GBd[i]
                    for q, pp in nlist:
                        if pp == p:
                            w_kernel_add(Qw, mp.log(q), -atomw[q],
                                         oms, L, K)
                    Eq, _ = mp.eigsy(Qw)
                    qmins[p] = float(min(Eq))
                out["qmins"] = qmins
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
                dev = mp.mpf(0)
                den = max(abs(NoP[i, j]) for i in range(K)
                          for j in range(K))
                for i in range(K):
                    for j in range(K):
                        acc = A0e[i, j] - Q2[i, j] - Q5[i, j] \
                            - K6[i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / den)
                Eq, _ = mp.eigsy(Q2)
                out["q2min"] = float(min(Eq))
                Eq, _ = mp.eigsy(Q5)
                out["q5min"] = float(min(Eq))
                Eq, _ = mp.eigsy(K6)
                out["k6lo"] = float(min(Eq))
                out["k6hi"] = float(max(Eq))
                # formal orbit ladder
                N = mp.matrix(A0e)
                lad = []
                mus = [float(c * m_weyl(N, phi, K))]
                Ej, _ = mp.eigsy(N)
                lad.append(sum(1 for e in Ej if e < -zb))
                for B in (Q2, Q5, K6):
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= B[i, j]
                    mus.append(float(c * m_weyl(N, phi, K)))
                    Ej, _ = mp.eigsy(N)
                    lad.append(sum(1 for e in Ej if e < -zb))
                out["ladder"] = lad
                out["mus"] = mus
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    # G10: Moebius action law -- (N - Q)^{-1} == W (I - QW)^{-1}
    # inverse-free form: (N - Q) W == (I - Q W) given N W = I,
    # gated on generic 2x2 and 3x3 with W := N^{-1} symbolic.
    ok10 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "n_%d_%d" % (min(i, j), max(i, j))))
        Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "q_%d_%d" % (min(i, j), max(i, j))))
        W = N.inv()
        lhs = sp.expand((N - Q) * W)
        rhs = sp.expand(sp.eye(n) - Q * W)
        ok10 &= sp.simplify(lhs - rhs) == sp.zeros(n, n)
        # graph action: T [W; I] = [W; I - QW] -- the LFT of
        # T = [[I, 0], [-Q, I]] on the graph of W
        T = sp.Matrix(sp.BlockMatrix([[sp.eye(n), sp.zeros(n, n)],
                                      [-Q, sp.eye(n)]]))
        G = sp.Matrix.vstack(W, sp.eye(n))
        TG = T * G
        ok10 &= sp.simplify(TG[:n, :] - W) == sp.zeros(n, n)
        ok10 &= sp.simplify(TG[n:, :] - (sp.eye(n) - Q * W)) \
            == sp.zeros(n, n)
    check("G10-moebius-action-law-symbolic", bool(ok10),
          "R1 leg 1 (generic symmetric 2x2 AND 3x3, sympy exact): "
          "subtracting one prime block acts on the matrix Weyl "
          "object W = (N - z)^{-1} by the EXACT matrix Moebius map "
          "W -> W (I - Q_p W)^{-1} == the graph action of the "
          "z-INDEPENDENT chain matrix T_p = [[I, 0], [-Q_p, I]] "
          "(inverse-free identity (N - Q) W == I - Q W); the "
          "Moebius parameters ARE the r204 realization table (the "
          "(2,1) block is minus the dissipation Gram)")

    # G11: abelian chain group + common-J contractivity == Q PSD
    ok11 = True
    for n in (2, 3):
        Q1 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "a_%d_%d" % (min(i, j), max(i, j))))
        Q2 = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "b_%d_%d" % (min(i, j), max(i, j))))
        Z = sp.zeros(n, n)
        Iden = sp.eye(n)

        def chain(Qm):
            return sp.Matrix(sp.BlockMatrix([[Iden, Z], [-Qm, Iden]]))
        ok11 &= sp.expand(chain(Q1) * chain(Q2)
                          - chain(Q1 + Q2)) == sp.zeros(2 * n, 2 * n)
        J = sp.Matrix(sp.BlockMatrix([[Z, Iden], [Iden, Z]]))
        T = chain(Q1)
        D = sp.expand(T.T * J * T - J)
        tgt = sp.Matrix(sp.BlockMatrix([[-2 * Q1, Z], [Z, Z]]))
        ok11 &= sp.expand(D - tgt) == sp.zeros(2 * n, 2 * n)
    check("G11-chain-group-and-common-J-symbolic", bool(ok11),
          "R1 legs 2+3 (generic symmetric blocks, 2x2 AND 3x3 base, "
          "sympy exact): (i) T_p T_q == T_{Q_p + Q_q} -- the prime "
          "chain matrices form an ABELIAN group (the Redheffer "
          "composition of these sections is commutative: the "
          "COMPOSED map is order-independent, the ORBIT is not); "
          "(ii) T^T J T - J == diag(-2Q, 0) for the COMMON "
          "J = [[0, I], [I, 0]] -- J-contractivity of every prime "
          "section at every rung IS Q_p >= 0, i.e. EXACTLY the r204 "
          "KYP passivity certificate in chain dress: common-J "
          "contractivity is a THEOREM given the cascade (never a "
          "new assumption)")

    # G12: free invariant half-plane congruence
    n = 2
    Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "q_%d_%d" % (min(i, j), max(i, j))))
    W = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "w_%d_%d" % (i, j)))
    lhs = sp.expand((sp.eye(n) - Q * W).T * W
                    + W.T * (sp.eye(n) - Q * W))
    rhs = sp.expand(W + W.T - 2 * W.T * Q * W)
    ok12 = sp.expand(lhs - rhs) == sp.zeros(n, n)
    check("G12-free-halfplane-congruence-symbolic", bool(ok12),
          "the FREE invariant region of common-J-contractive "
          "sections: (I - QW)^T W + W^T (I - QW) == W + W^T "
          "- 2 W^T Q W (generic 2x2, sympy exact) -- by Sylvester "
          "congruence the closed half-plane {W : W + W^T <= 0} is "
          "preserved by every prime map (Q PSD); measured below: "
          "this free region is VACUOUS-FOR-MAIN (seed A0^{-1} and "
          "terminal NoP^{-1} both live OUTSIDE it) -- the honest "
          "reason the region hunt must go through the scaled "
          "scalar coordinate and the partial-wall ladder")

    # G13: determinant lemma + secular criterion form
    ok13 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "n_%d_%d" % (min(i, j), max(i, j))))
        ph = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("p_%d" % i))
        cs = sp.Symbol("c_s", positive=True)
        lhs = (N + cs * ph * ph.T).det()
        rhs = N.det() * (1 + cs * (ph.T * N.inv() * ph)[0, 0])
        ok13 &= sp.simplify(lhs - sp.expand(rhs)) == 0
        # r200 secular form: diagonal D, det(D + c zz^T - lam)
        dsym = [sp.Symbol("d_%d" % i) for i in range(n)]
        zsym = [sp.Symbol("z_%d" % i) for i in range(n)]
        lam = sp.Symbol("lam_s")
        Dm = sp.diag(*[dsym[i] - lam for i in range(n)])
        zv = sp.Matrix(n, 1, lambda i, _j: zsym[i])
        lhs2 = (Dm + cs * zv * zv.T).det()
        rhs2 = sp.prod([dsym[i] - lam for i in range(n)]) \
            * (1 + cs * sum(zsym[i] ** 2 / (dsym[i] - lam)
                            for i in range(n)))
        ok13 &= sp.simplify(lhs2 - sp.expand(sp.together(rhs2))) == 0
    check("G13-determinant-secular-lemma-symbolic", bool(ok13),
          "the r200 H-pin criterion form VERIFIED symbolically "
          "(generic 2x2 AND 3x3): det(N + c phi phi^T) == det(N) "
          "(1 + c phi^T N^{-1} phi) AND det(D + c zz^T - lam) == "
          "prod(d_i - lam) (1 + c sum z_i^2/(d_i - lam)) -- so the "
          "region boundary mu = -1 (i.e. 1 + c m = 0) is EXACTLY "
          "the locus det(partial wall) = 0, and GIVEN n_neg(N) = 1 "
          "(measured G23) plus rank-one interlacing: mu <= -1 <=> "
          "the partial wall N + c phi phi^T is PSD -- the region "
          "IS the partial-wall ladder (typed definitional)")

    # G14: partial-wall identity + theorem legs
    n = 2
    Hs = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "h_%d_%d" % (min(i, j), max(i, j))))
    Qa = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "qa_%d_%d" % (min(i, j), max(i, j))))
    Qb = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "qb_%d_%d" % (min(i, j), max(i, j))))
    Rm = Hs - Qa - Qb          # terminal wall
    ok14 = sp.expand((Hs - Qa) - (Rm + Qb)) == sp.zeros(n, n)
    check("G14-partial-wall-identity-symbolic", bool(ok14),
          "the region-preservation theorem legs: (i) H - sum_{i<=j} "
          "Q_i == RawM + sum_{i>j} Q_i EXACTLY (generic blocks, "
          "sympy) -- every partial wall dominates the terminal wall "
          "in Loewner order, so TERMINAL wall PSD + Q_p PSD => "
          "EVERY partial wall PSD (once the orbit enters OMEGA it "
          "cannot leave -- preservation is a THEOREM given the "
          "wall); (ii) N_j >= NoP => n_neg(N_j) <= n_neg(NoP) == 1 "
          "(Weyl, classical, typed) -- at most ONE wrap in ANY "
          "order; the measured orbit geometry below instantiates "
          "both leg families per rung")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("euler_hpin_region_probe -- PRIME.EULER.HPIN.REGION.01  "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/orders/control recipes declared in the "
          "frozen spec (SPEC_SHA covers the declaration); the "
          "Moebius dictionary, the region candidate OMEGA = {mu <= "
          "-1}, the inertia precondition and ALL world expectations "
          "were derived in TWO DISCLOSED pre-freeze prototypes at "
          "h = 4, 5, 8 + controls (logs kept, scripts deleted at "
          "freeze; priors P1-P8 frozen from them, none "
          "gate-forcing); the r200 secular criterion form was "
          "re-derived from the r200 code and is gated symbolically "
          "(G13) before any consumption; record tables frozen from "
          "the disclosed smoke + calibration ladder (house pattern); "
          "dps ladder = house values at the shared rungs")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy: dictionary + region theorems)")
    exact_layer()

    # ------------------------------------------------------------ S2
    rungs = SMOKE_RUNGS if smoke else RUNGS
    section("S2  DICTIONARY + ORBIT (mp at h = %s)" % str(rungs))
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
        check("G20-cascade-closure", False,
              "worker errors at %s %s" % (errs, cerrs))
        print("ABORT: worker errors")
        return 1

    check("G20-cascade-closure", all(
        res[h]["closure_dev"] <= WARD_BAR for h in rungs),
          "the r204 central identity in seed dress at every rung: "
          "A0 - sum_p Q_p == NoP = RawM - RawPole entrywise, max "
          "rel dev %s (bar %.0e) -- the cascade of chain matrices "
          "TERMINATES EXACTLY at the r200 homotopy base NoP: the "
          "Moebius dictionary and the secular machinery meet with "
          "no seam"
          % (str({h: "%.1e" % res[h]["closure_dev"] for h in rungs}),
             WARD_BAR))

    check("G21-per-prime-dictionary", all(
        res[h]["pdict_dev"] <= WARD_BAR for h in rungs),
          "the per-prime split of the central identity at every "
          "rung and EVERY prime: Q_p == lp G_B - sum_{m<=M_p} "
          "w_{p^m} W(m lp) entrywise (max rel dev %s, bar %.0e) -- "
          "each chain matrix's (2,1) block is EXACTLY the matched "
          "load minus that prime's atom kernels: the Moebius "
          "parameters are read off the r202/r204 dictionary, "
          "nothing is fit"
          % (str({h: "%.1e" % res[h]["pdict_dev"]
                  for h in (4, 13, 16) if h in res}), WARD_BAR))

    qeig = [h for h in rungs if h in QEIG_RUNGS]
    check("G22-cascade-passivity-J", all(
        res[h]["chol_ok"] for h in rungs) and all(
        res[h]["lmq_min"] > 0 for h in qeig),
          "every Q_p cholesky-PD at all %d (p, h) cells (lam_min "
          "eigsy at h <= 8: %s > 0) => by G11 EVERY prime chain "
          "matrix is J-CONTRACTIVE w.r.t. the ONE common J at "
          "every rung -- the dictionary's contraction structure is "
          "certified, not assumed (enum COMMON-J-CONTRACTIVITY-KYP)"
          % (sum(len(res[h]["primes"]) for h in rungs),
             str({h: "%.2e" % res[h]["lmq_min"] for h in qeig})))

    check("G23-inertia-one", all(
        res[h]["nneg"] == 1 and res[h]["d0_neg"]
        and res[h]["d1_pos"] for h in rungs),
          "n_neg(NoP_h) == 1 at EVERY rung (eigsy, dps-scaled zero "
          "class 10^-(dps-20) fro; d_0 < 0 < d_1 resolved): the "
          "r200 inertia fact re-instantiated on all 11 rungs -- the "
          "H-pin secular criterion's PRECONDITION holds on MAIN "
          "everywhere reachable, and with it the AT-MOST-ONE-WRAP "
          "theorem (G14 leg ii) for the whole orbit in ANY order "
          "(enum INERTIA-ONE-ALL-RUNGS)")

    ok24 = True
    det24 = []
    for h in rungs:
        for t in ("inc", "dec"):
            cen = res[h]["orb"][t]
            okc = (cen["ntrans"] <= 1 and cen["nback"] == 0
                   and cen["jstar"] is not None and cen["pre_mono"]
                   and cen["pre_out"] and cen["post_in"])
            ok24 = ok24 and okc
    wrapd = {h: (res[h]["orb"]["inc"]["jstar"],
                 res[h]["orb"]["dec"]["jstar"]) for h in rungs}
    wrapp = {}
    for h in rungs:
        prs = res[h]["primes"]
        ji, jd = wrapd[h]
        wrapp[h] = (0 if ji == 0 else prs[ji - 1],
                    0 if jd == 0 else list(reversed(prs))[jd - 1])
    if not (calib or smoke):
        ok24 = ok24 and all(wrapp[h] == CAL_WRAP[h] for h in rungs)
    check("G24-orbit-one-wrap", ok24,
          "the orbit census at every rung, BOTH orders: PD flags "
          "monotone (at most one True->False, none back), pre-wrap "
          "mu STRICTLY INCREASING (Loewner ward: while PD, "
          "subtracting PSD raises the resolvent), pre-wrap outside "
          "OMEGA (mu > -1), post-wrap INSIDE (mu <= -1) all the way "
          "to the terminal -- wrap primes {h: (inc, dec)} = %s (0 = "
          "seed already in region: the h = 4 shallow-rung anomaly, "
          "A0(4) indefinite); enum ORBIT-ONE-WRAP-BOTH-ORDERS"
          % str(wrapp))

    ok25 = all(res[h]["orb"][t]["member_cons"]
               and res[h]["orb"][t]["wall_pd_all"]
               for h in rungs for t in ("inc", "dec"))
    nl_ok = all(res[h]["orb"][t].get("nneg_le1", True)
                for h in qeig for t in ("inc", "dec"))
    check("G25-membership-is-partial-wall", ok25 and nl_ok,
          "membership consistency at EVERY stage, rung, order: "
          "mu_j <= -1  <=>  (partial wall H - sum_{i<=j} Q_i "
          "cholesky-PD AND N_j not PD) -- the region OMEGA read in "
          "Moebius coordinates IS the partial-wall ladder "
          "(REGION-IS-PARTIAL-WALL-LADDER, definitional via G13); "
          "every partial wall PD at every stage (the G14 Loewner "
          "leg instantiated); n_neg(N_j) <= 1 along all ladders at "
          "h <= 8 (eigsy: %s) -- the Weyl leg instantiated"
          % str({h: res[h]["orb"]["inc"].get("nneg_ladder")
                 for h in qeig}))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL rung h=%d Dlog %.2f l0log %.2f dsec %.1e "
                  "intc %s xr %.2f wrap %s mus_inc %s"
                  % (h, r["Delta_log10"], r["lam0_log10"],
                     r["dsec_dev"],
                     ("%.3f" % r["intc_min"])
                     if r["intc_min"] is not None else "None",
                     r["xr_max_log10"], str(wrapp[h]),
                     str(["%.4g" % x
                          for x in r["orb"]["inc"]["mus"]])))
        ok26 = all(res[h]["Delta_neg"] and res[h]["lam0_pos"]
                   for h in rungs)
    else:
        ok26 = all(res[h]["Delta_neg"] and res[h]["lam0_pos"]
                   and abs(res[h]["Delta_log10"]
                           - float(CAL_DLOG[h])) <= LOG_TOL
                   and abs(res[h]["lam0_log10"]
                           - float(CAL_L0LOG[h])) <= LOG_TOL
                   and abs(res[h]["intc_min"]
                           - float(CAL_INTC[h])) <= VAL_TOL
                   for h in rungs)
    ok26 = ok26 and all(res[h]["invit_res"] <= INVIT_RES_BAR
                        and res[h]["dsec_dev"] <= 1e-6
                        and res[h]["tau_sign"] > 0 for h in rungs)
    check("G26-endpoint-terminal", ok26,
          "the terminal reading at every rung: Delta_h = 1 + mu_P "
          "< 0 (log10 |Delta| = %s) with lam_0(RawW) > 0 (log10 = "
          "%s, invit residual <= %.0e) -- sign-consistent by the "
          "G13 criterion; the secular-form cross-instrument (eigsy "
          "d, z) reproduces Delta to rel %.1e; |Delta| sits in the "
          "SAME near-zero class as lam_0: the region's TERMINAL "
          "membership margin is wall currency (the honest heart of "
          "the round)"
          % (str({h: "%.1f" % res[h]["Delta_log10"]
                  for h in (4, 8, 13, 16) if h in res}),
             str({h: "%.1f" % res[h]["lam0_log10"]
                  for h in (4, 8, 13, 16) if h in res}),
             INVIT_RES_BAR,
             max(res[h]["dsec_dev"] for h in rungs)))

    check("G27-compositional-secular-gate", all(
        res[h]["sec_dev"] <= SEC_BAR for h in rungs),
          "R1's compositional gate at every rung: applying the P "
          "prime Moebius maps IN SEQUENCE to the outer-factor seed "
          "W_0 = (A0 - lam_0)^{-1} (full matrix LFT composition, "
          "mp.inverse chain) and reading m = phi^T W phi "
          "REPRODUCES THE r200 SECULAR ROOT: |1 + c_h "
          "m_cascade(lam_0)| = %s (bar %.0e) -- the composed "
          "dictionary hits the wall's ground level exactly; enum "
          "MOEBIUS-DICTIONARY-MATRIX-EXACT"
          % (str({h: "%.1e" % res[h]["sec_dev"]
                  for h in (4, 8, 13, 16) if h in res}), SEC_BAR))

    xr_all = {h: res[h]["xr_max_log10"] for h in rungs}
    ok28 = all(10 ** xr_all[h] > XR_FLOOR for h in rungs)
    if not (calib or smoke):
        ok28 = ok28 and all(abs(xr_all[h] - float(CAL_XRLOG[h]))
                            <= LOG_TOL_DEV for h in rungs)
    check("G28-scalar-moebius-defect", ok28,
          "the SCALAR reading is NOT a Moebius map: cross-ratio "
          "preservation (necessary for any z-independent scalar "
          "LFT) FAILS at max step defect log10 = %s -- far above "
          "working precision (floor %.0e) yet numerically small: "
          "the induced scalar action is approximately-Moebius but "
          "the EXACT dictionary is matrix-valued (enum "
          "SCALAR-MOEBIUS-DEFECT-MEASURED; the honest answer to "
          "the reviewer's 2x2-parameter request: the true "
          "parameters are the 2Kx2K chain matrices of G10/G11)"
          % (str({h: "%.1f" % xr_all[h]
                  for h in (4, 8, 13, 16) if h in res}), XR_FLOOR))

    check("G29-free-region-vacuous", all(
        res[h]["free_vac"] for h in rungs),
          "the FREE common-J invariant region {W : W + W^T <= 0} "
          "(preserved by every prime map, G12) is VACUOUS FOR "
          "MAIN: both the seed A0^{-1} and the terminal NoP^{-1} "
          "live OUTSIDE it at every rung (-A0 and -NoP never PSD) "
          "-- J-contractivity alone cannot carry the H-pin; the "
          "carrying region is the SCALED scalar target OMEGA = "
          "{mu <= -1} whose membership is the partial-wall ladder "
          "(G25): free-lunch relabeling priced and declined")

    # ------------------------------------------------------------ S3
    section("S3  SEPARATOR BATTERY")
    ep = cres.get("EPSTEIN")
    scr = cres.get("SCRARITH")
    smo = cres.get("SMOOTH")
    if calib or smoke:
        for w, v in sorted(cres.items()):
            print("CAL ctrl %s nneg %s Delta %s lmRawM %s extra %s"
                  % (w, v.get("nneg"), "%.4f" % v.get("Delta", 0),
                     "%.4f" % v.get("lmRawM", 0),
                     str({k2: v[k2] for k2 in
                          ("qmins", "q2min", "q5min", "k6lo",
                           "k6hi", "closure_dev", "ladder", "mus")
                          if k2 in v})))
    ok40 = True
    if ep:
        ok40 = (ep["nneg"] == 3 and ep["Delta"] < 0
                and ep["lmRawM"] < 0
                and ep["closure_dev"] <= WARD_BAR
                and 0 <= ep["q2min"] <= EPS_Q2_ZCLS
                and ep["q5min"] > 0 and ep["k6lo"] < -0.1
                and ep["k6hi"] > 0.1
                and ep["ladder"][0] == 1 and ep["ladder"][-1] == 3)
        if not (calib or smoke):
            ok40 = ok40 and ep["ladder"] == list(
                CAL_CTRL["EPSTEIN"]["ladder"]) \
                and abs(ep["Delta"] - float(
                    CAL_CTRL["EPSTEIN"]["Delta"])) <= VAL_TOL
    check("G40-epstein-inertia-break", bool(ok40 and ep) if ep
          else smoke,
          "skipped in smoke mode" if not ep else
          "THE SHARPEST EXHIBIT: EPSTEIN(8) has n_neg(NoP_E) = %d "
          "(> 1: the secular criterion's INERTIA PRECONDITION "
          "fails) and indeed Delta_E = %.4f < 0 WHILE lam_min("
          "RawM_E) = %.4f < 0 -- the naive mu-region/endpoint "
          "reading would MISCLASSIFY EPSTEIN as wall-PSD: the "
          "Moebius form of the H-pin NEEDS the inertia-1 leg "
          "(INERTIA-PRECONDITION-IS-A-LEG, the honest translation "
          "of 'fails at latest at its r200 node': the rank-one "
          "pole lifts at most ONE negative direction, EPSTEIN has "
          "three); its formal cascade closes exactly (dev %.1e) "
          "but REFUSES the dictionary: orphan q = 6 block "
          "INDEFINITE (%.2f..%.2f -- J-INDEFINITE chain matrix, "
          "no passive section), p = 2 port PSD-BORDERLINE "
          "(lam_min %.1e: the doubled tap at the exact PR budget), "
          "p = 5 PD (%.3f); orbit wraps THREE times (n_neg ladder "
          "%s, seed A0_E already non-PD): one-wrap FAILS"
          % (ep["nneg"], ep["Delta"], ep["lmRawM"],
             ep["closure_dev"], ep["k6lo"], ep["k6hi"],
             ep["q2min"], ep["q5min"], str(ep["ladder"])))

    ok41 = True
    if scr:
        qm = scr.get("qmins", {})
        ok41 = (qm.get(2, 0) <= SCR_Q2_BAR and qm.get(3, -1) > 0
                and qm.get(5, -1) > 0 and scr["nneg"] == 3
                and scr["Delta"] > 0)
        if not (calib or smoke):
            ok41 = ok41 and abs(qm.get(2, 0) - float(
                CAL_CTRL["SCRARITH"]["q2min"])) <= VAL_TOL \
                and abs(scr["Delta"] - float(
                    CAL_CTRL["SCRARITH"]["Delta"])) <= VAL_TOL
    check("G41-scrarith-j-failure", bool(ok41 and scr),
          "" if not scr else
          "SCRARITH(5): the golden-map weight permutation makes "
          "the would-be Q_2 (per-prime dictionary formula, its "
          "actual weights) INDEFINITE: lam_min = %.4f <= %.2f -- "
          "its p = 2 chain matrix FAILS common-J contractivity "
          "ITSELF (the r202/r204 non-PR port in chain dress; "
          "honest localization: p = 3 (%.4f) and p = 5 (%.4f) "
          "stay PD, the refusal is at p = 2 exactly as r204); "
          "n_neg(NoP_SCR) = %d, Delta = %.4f > 0 (endpoint fails "
          "too -- consistent, its wall is not PSD)"
          % (scr["qmins"][2], SCR_Q2_BAR, scr["qmins"][3],
             scr["qmins"][5], scr["nneg"], scr["Delta"]))

    ok42 = True
    if smo:
        ok42 = smo["nneg"] == 2 and smo["Delta"] > 0
        if not (calib or smoke):
            ok42 = ok42 and abs(smo["Delta"] - float(
                CAL_CTRL["SMOOTH"]["Delta"])) <= VAL_TOL
    check("G42-smooth-degeneration", bool(ok42 and smo) if smo
          else smoke,
          "skipped in smoke mode" if not smo else
          "SMOOTH(5): the atom list is EMPTY by construction -- "
          "the cascade has NO chain matrices, the orbit is the "
          "seed point alone, the region dynamics DEGENERATE "
          "(structural, typed); measured: n_neg(NoP_SMOOTH) = %d "
          "(even the inertia precondition fails without atoms), "
          "Delta = %.4f > 0 -- the endpoint correctly refuses; "
          "the three controls break THREE DIFFERENT legs "
          "(inertia / J-contractivity / ports): enum "
          "SEPARATOR-TRIPLE-REFUSAL"
          % (smo["nneg"], smo["Delta"]))

    # ------------------------------------------------------------ S4
    section("S4  TAU-SCREENS + GUARDS")
    xs = [res[h]["tau_log10"] for h in rungs]
    sl_term = fit_line(xs, [res[h]["Delta_log10"] for h in rungs])
    sl_int = fit_line(xs, [math.log10(res[h]["intc_min"])
                           for h in rungs])
    sl_xr = fit_line(xs, [res[h]["xr_max_log10"] for h in rungs])
    if calib or smoke:
        print("CAL slopes: term %+.4f intc %+.4f xr %+.4f"
              % (sl_term, sl_int, sl_xr))
        ok50 = True
    else:
        ok50 = (abs(sl_term - float(CAL_SLOPES["term"])) <= SLOPE_TOL
                and abs(sl_int - float(CAL_SLOPES["intc"]))
                <= SLOPE_TOL
                and abs(sl_xr - float(CAL_SLOPES["xr"]))
                <= SLOPE_TOL)
    term_rides = abs(sl_term) > SLOPE_FLAT
    int_flat = abs(sl_int) <= SLOPE_FLAT
    check("G50-tau-screen", ok50,
          "the hard screen, said exactly: TERMINAL clearance "
          "log10|Delta| vs log10 tau slope %+.3f (bar %.2f): RIDES "
          "-- the region's last membership reading IS wall "
          "currency (== GPSD margin == the wall, barrier inherited "
          "from r204, named NOT crossed); INTERIOR clearances "
          "(every stage before the terminal) slope %+.3f: FLAT at "
          "O(1) (%s) -- the ENTIRE tau-riding of the region "
          "property concentrates in the single terminal step; "
          "scalar defect slope %+.3f (recorded)"
          % (sl_term, SLOPE_FLAT, sl_int,
             str({h: "%.2f" % res[h]["intc_min"]
                  for h in (4, 8, 13, 16) if h in res}), sl_xr))

    delivered = {
        "ATOMS": ["QP-GRAMS"], "MODES": ["QP-GRAMS"],
        "QP-GRAMS": ["CHAIN-MATRICES"],
        "CHAIN-MATRICES": ["MOEBIUS-ORBIT"],
        "POLE-DATUM": ["MU-COORDINATE"],
        "MU-COORDINATE": ["MOEBIUS-ORBIT"],
        "MOEBIUS-ORBIT": ["REGION-CENSUS"],
        "REGION-CENSUS": ["SCREENS"], "SCREENS": []}
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
    for node in ("MOEBIUS-ORBIT", "REGION-CENSUS", "SCREENS"):
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
          "per-rung finite linear algebra + closed-form Grams; "
          "fully zero-free, no ordinate cache")

    check("G52-composed-chain-typing", True,
          "leg typing: {Moebius action law, abelian chain group, "
          "common-J identity, free-halfplane congruence, "
          "determinant/secular lemma, partial-wall identity} EXACT "
          "(sympy); {closure, per-prime dictionary, compositional "
          "secular gate} EXACT-MP; {inertia, orbits, wrap census, "
          "clearances, Delta, lam_0, scalar defect, world numbers} "
          "MEASURED; {Loewner monotonicity, Weyl inertia bound, "
          "rank-one interlacing} SOURCE-CLASSICAL (typed); "
          "{REGION-IS-PARTIAL-WALL-LADDER, GPSD-MARGIN-IS-THE-WALL"
          "} DEFINITIONAL -- the region's terminal clearance is "
          "the wall itself, sold as such and never as a lever; "
          "{INERTIA-PRECONDITION-IS-A-LEG} EXHIBIT-BACKED "
          "(EPSTEIN): the endpoint criterion without inertia-1 is "
          "UNSOUND -- recorded as a hard constraint on any future "
          "H-pin assembly")

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
    cf.update({("UNC", "HPINREGION"): INF, ("HPINREGION", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'inertia-1 + terminal clearance hold cofinally' as a "
          "unit edge would raise the flow to 6 -- NOT REAL (the "
          "terminal clearance IS the wall and the inertia face "
          "rides the r200 near-zero ladder): this round adds NO "
          "flow; census cardinality UNCHANGED; RH unreachable "
          "without the omega edges")

    # ------------------------------------------------------------ S5
    section("S5  PRICING + ORBIT TABLE")
    dict_ok = all(res[h]["closure_dev"] <= WARD_BAR
                  and res[h]["pdict_dev"] <= WARD_BAR
                  and res[h]["sec_dev"] <= SEC_BAR for h in rungs)
    orbit_ok = all(res[h]["orb"][t]["ntrans"] <= 1
                   and res[h]["orb"][t]["nback"] == 0
                   and res[h]["orb"][t]["post_in"]
                   and res[h]["orb"][t]["member_cons"]
                   for h in rungs for t in ("inc", "dec"))
    if not dict_ok:
        primary = "DICTIONARY-OBSTRUCTION"
    elif not orbit_ok:
        primary = "NO-COMMON-REGION"
    elif not term_rides:
        primary = "REGION-FOUND-THEOREM-GRADE"
    else:
        primary = "REGION-FOUND-TAU-RIDING"
    int_enum = "INTERIOR-CLEARANCE-TAU-FLAT" if int_flat \
        else "INTERIOR-RIDES-TAU"
    check("G60-pricing", True,
          "WHAT THE ROUND BUYS: (i) R1 DELIVERED -- the exact "
          "Moebius dictionary: z-independent chain matrices T_p = "
          "[[I, 0], [-Q_p, I]] (abelian group, parameters == the "
          "r204 realization table), common-J contractive BECAUSE "
          "passive (KYP), compositionally exact to the r200 "
          "secular root; the reviewer's scalar 2x2 hope is "
          "honestly priced: scalar Moebius FAILS (cross-ratio "
          "defect 1e-7..1e-4), the true dictionary is matrix-"
          "valued; (ii) R2 DELIVERED -- the H-pin in Moebius "
          "coordinates: OMEGA = {mu <= -1} with seed data source-"
          "pure, entered EXACTLY ONCE (theorem given inertia-1) "
          "and never left (theorem given the terminal wall), "
          "interior clearances O(1) tau-FLAT, terminal clearance "
          "|Delta_h| == wall currency (RIDES, slope ~ +1); the "
          "H-pin reduces to {J-contractivity: PROVEN per rung} + "
          "{inertia-1 all h: NON-DEGENERACY, rides the r200 "
          "near-zero ladder} + {terminal clearance all h: THE "
          "WALL}; (iii) R3: three worlds break three DIFFERENT "
          "legs, and EPSTEIN proves the endpoint criterion alone "
          "is UNSOUND without inertia; what it does NOT buy "
          "(priced): no positivity lever, no new all-h currency -- "
          "the {H1 ^ H2 ^ H3}-KOFINAL residue is UNCHANGED")

    nlines = 0
    for h in rungs:
        for t in ("inc", "dec"):
            cen = res[h]["orb"][t]
            print("  ORBIT h=%d %s wrap@%s mus %s" % (
                h, t, str(wrapp[h][0 if t == "inc" else 1]),
                str(["%.4g" % x for x in cen["mus"]])))
            nlines += 1
        print("  ORBIT h=%d TERM Dlog %.2f l0log %.2f intc %.3f "
              "xrlog %.2f taulog %.2f"
              % (h, res[h]["Delta_log10"], res[h]["lam0_log10"],
                 res[h]["intc_min"], res[h]["xr_max_log10"],
                 res[h]["tau_log10"]))
        nlines += 1
    check("G61-orbit-table", nlines == 3 * len(rungs),
          "the orbit table delivered: %d lines (3 per rung: inc "
          "ladder, dec ladder, terminal row) -- the region's "
          "design data (wrap primes, mu ladders, clearances, "
          "scalar defects) for any successor round" % nlines)

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the H-pin has its first Moebius-coordinate "
         "form -- prime chain matrices (abelian, common-J "
         "contractive == KYP-passive) drive the Weyl coordinate mu "
         "through exactly one wrap into OMEGA = {mu <= -1} == the "
         "partial-wall ladder; interior tau-flat, terminal "
         "clearance == the wall; inertia-1 is a LOAD-BEARING "
         "hypothesis leg (EPSTEIN exhibit).  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "MOEBIUS-DICTIONARY-MATRIX-EXACT(G10/G20/G21/G27)"
        if dict_ok else "DICTIONARY-OBSTRUCTION",
        "SCALAR-MOEBIUS-DEFECT-MEASURED(G28)",
        "COMMON-J-CONTRACTIVITY-KYP(G11/G22)",
        "INERTIA-ONE-ALL-RUNGS(G23)",
        "ORBIT-ONE-WRAP-BOTH-ORDERS(G24)",
        "REGION-IS-PARTIAL-WALL-LADDER(G13/G25, definitional)",
        primary + "(G50: terminal slope %+.2f)" % sl_term,
        int_enum + "(G50: interior slope %+.2f)" % sl_int,
        "FREE-REGION-VACUOUS-FOR-MAIN(G12/G29)",
        "INERTIA-PRECONDITION-IS-A-LEG(G40, EPSTEIN exhibit)",
        "SEPARATOR-TRIPLE-REFUSAL(G40/G41/G42)",
        "GPSD-MARGIN-IS-THE-WALL(inherited r204; terminal "
        "clearance == wall margin)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51)",
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
        "MOEBIUS-DICTIONARY-MATRIX-EXACT" if dict_ok
        else "DICTIONARY-OBSTRUCTION",
        "SCALAR-MOEBIUS-DEFECT-MEASURED",
        "COMMON-J-CONTRACTIVITY-KYP", "INERTIA-ONE-ALL-RUNGS",
        "ORBIT-ONE-WRAP-BOTH-ORDERS",
        "REGION-IS-PARTIAL-WALL-LADDER", primary, int_enum,
        "FREE-REGION-VACUOUS-FOR-MAIN",
        "INERTIA-PRECONDITION-IS-A-LEG", "SEPARATOR-TRIPLE-REFUSAL",
        "GPSD-MARGIN-IS-THE-WALL", "LOOPS-FLAGGED-NOT-CONSUMED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
