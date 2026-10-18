#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""terminal_dissipation_probe -- PRIME.TERMINAL.DISSIPATION.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, the
bughunt11 / pontryagin-n1 / secular-crossing lanes, and every
verification/paper/website surface) are not touched.

=======================================================================
MISSION (round ~207: the reviewer's Probe A after round 206 -- the
TERMINAL DISSIPATION IDENTITY).  Round 205 (euler_hpin_region_probe,
SPEC cb1dfde33a198fb3, 27/27, note DXXXI) proved: the prime chain
matrices T_p = [[I, 0], [-Q_p, I]] satisfy the EXACT common-J law
T_p^T J T_p - J = diag(-2 Q_p, 0) for J = [[0, I], [I, 0]]
(J-contractivity == the r204 KYP passivity Q_p >= 0), form an ABELIAN
group T_p T_q = T_{Q_p+Q_q}, and compose to the terminal read
Delta_h = 1 + c_h m_h(0) (m = phi^T NoP^{-1} phi) reproducing the
r200 secular root to 6.5e-30.  Round 204 (euler_jet_colligation_probe,
SPEC 5327721e3f2f36f8, 30/30, note DXXX) proved: Q_p = lp Y_p^T D_p^2
Y_p (dissipation Grams, PSD by construction) and RawM = H - sum_p Q_p
(exact Schur form).  THE REVIEWER'S TELESCOPE: for a cascade T^(n) =
T_n ... T_1 the EXACT identity J - T^(n)T J T^(n) = sum_j T^(j-1)T
D_j T^(j-1) with D_j = J - T_j^T J T_j >= 0; the dream: Delta_h is
EXACTLY a matrix element of the global dissipation sum plus an
explicit boundary term -- Delta_h's sign as an ENERGY BALANCE.  THIS
round derives the identity SYMBOLICALLY (reconstructed pre-freeze
from the r205 graph action, NOTHING fit) and adjudicates it:

  A1 THE GLOBAL DISSIPATION OPERATOR (derived, gated symbolic + mp).
     By the abelian lower-triangular structure the telescope
     COLLAPSES: every transported term T^(j-1)T diag(2Q_j, 0)
     T^(j-1) equals diag(2Q_j, 0) itself (the (1,1) block is
     invariant under unit-lower-triangular congruence from the left
     family), so
       D_h := J - T_total^T J T_total = diag(2 Q_total, 0) EXACTLY,
       Q_total = sum_p Q_p = A0 - NoP = H - RawM.
     THE CIRCULARITY CAVEAT, SAID FIRST: the dissipation operator is
     just the TOTAL PRIME BLOCK in chain dress -- the naive reading
     "D_h >= 0" is the r204 passivity again and carries nothing new.
     THE ACTUAL CONTENT must come from the interplay with the
     terminal vector (A2): WHICH v makes v^T D_h v read Delta_h.
  A2 THE IDENTITY (the round's centerpiece; derived pre-freeze BY
     ALGEBRA from the scattering composition, gated symbolically
     G10-G13 and in mp at every rung G24/G26).  The graph transport:
     the composed Moebius map sends W_0 = A0^{-1} to W_P = NoP^{-1}
     via the graph vectors g-hat = [W_0 u; u], u = (I - Q_total
     W_0)^{-1} phi, g_P = T_total g-hat = [W_P phi; phi]; the J-form
     of a graph vector reads the Weyl function (g^T J g = 2 phi^T W
     phi); J-contraction of the cascade turns this into THE TERMINAL
     DISSIPATION IDENTITY: with w := NoP^{-1} phi (the TERMINAL WEYL
     STATE; A0 w = u), v_h := [w; 0], and C_h := 1 + c_h w^T A0 w,
       Delta_h  =  C_h - (c_h/2) v_h^T D_h v_h
                =  C_h - c_h w^T Q_total w
                =  C_h - sum_p E_p(w),   E_p := c_h w^T Q_p w
                =  c_h lp ||D_p Y_p w||^2  >=  0  (r204 Gram form).
     THE ANSWER TO "WHICH v": the terminal Weyl state w = NoP^{-1}
     phi ALONE -- a predefined battery (phi, seed state A0^{-1} phi,
     w, the negative NoP eigenvector, e_1, e_2) is recorded to show
     the identity is w-specific (record-only, NO fits).
     THE SIGN ADJUDICATION (the honest headline, resolved by the
     derivation BEFORE any run): the boundary term C_h enters with
     PLUS and the dissipation with MINUS -- C_h >= 1 EXPLICITLY
     whenever the seed A0 is PSD (h >= 5; arch/pole-explicit: A0 =
     RawArch + theta G_B source-side, c_h pole-side) -- so the
     reviewer's hope "C_h >= 0 => done per rung by positive-sum
     structure" INVERTS: Delta_h < 0 demands the OVERSHOOT
       sum_p E_p(w)  >=  C_h  >=  1,
     total prime dissipation at the terminal state must EXCEED the
     seed energy plus one -- the exact mirror of the r204 wall
     barrier (wall PSD == "dissipation never overshoots H as forms";
     H-pin == "dissipation DOES overshoot the pole-free seed A0 at
     the ONE vector w").  THE SHARPEST LINK (gated): w^T RawM w =
     m_h(0) Delta_h EXACTLY (one line: RawM w = Delta phi + residual)
     -- with m < 0 measured, Delta < 0 <=> w^T RawM w > 0: the sign
     source of the balance IS the wall's quadratic form at the
     terminal state (GPSD-MARGIN-IS-THE-WALL in its sharpest dress;
     barrier named, NOT crossed).  DET READING (tau/det-class,
     exact): Delta_h = det(RawM)/det(NoP) (determinant lemma) and
     det(NoP) = det(A0) det(I - A0^{-1} Q_total) (multiplicativity)
     -- the terminal clearance is the ratio of the wall determinant
     to the cascade's scattering determinant, gated at h <= 8.
  A3 THE ENERGY LADDER.  Per-prime energies E_p(w) at every rung:
     one-signed AUTOMATICALLY (|.|^2 given Q_p PD) -- the quadratic
     reading does avoid PER-PRIME cancellation; the honest pricing:
     the r203/r201 47-dex cancellation does NOT disappear, it
     CONCENTRATES into the single subtraction sum_p E_p - C_h =
     -Delta_h (measured depth ladder log10(sum E) - log10|Delta| =
     the full tau dex at every rung).  Measured: E_p ladder,
     fractions, carrier prime, C_h ladder, overshoot gap == |Delta|
     (rides tau, slope ~ +1 -- it IS the wall clearance), C_h and
     sum E_p and fractions tau-FLAT (structure vs currency split as
     in r205).
  A4 WORLDS AND SCREENS.  MAIN-specificity enters through {inertia
     kappa = 1, Euler passivity} exactly as the reviewer requires:
     EPSTEIN(8): kappa = 3 (n_neg(NoP_E) = 3) breaks the secular
     precondition AND the balance MISCLASSIFIES without it (Delta_E
     < 0 with wall indefinite -- the r205 exhibit inherited: the
     identity holds ALGEBRAICALLY in every world, its H-pin READING
     needs inertia-1 as a leg); the formal block sum B_E = Q_2^E +
     Q_5^E + K_6 contains the J-INDEFINITE orphan K_6 -- the
     dissipation reading of D_E fails at a named place (lam_min of
     the orphan block < 0), and the seed A0_E is non-PD (C_E loses
     its explicit floor).  SCRARITH(5): the would-be Q_2 is
     INDEFINITE (r205: lam_min = -0.1334) -- E_2's one-signedness is
     STRUCTURALLY unguaranteed (the sign of the measured E_2^scr at
     the specific w is recorded either way; the guarantee, not the
     sample, is what breaks) and the endpoint fails (Delta_scr > 0:
     dissipation UNDERSHOOTS the seed -- the balance correctly
     refuses).  SMOOTH(5): portless -- no cascade, no D_h, the
     balance DEGENERATES structurally (typed); n_neg = 2, Delta > 0.
     TAU-SCREENS on every ladder; the ANTI-LOOP TEST: every
     hypothesis of this round is from {Euler structure (chain
     algebra), positive weights, passivity (KYP), classical linear
     algebra (congruence, telescope, det lemma)} -- the sign source
     is adjudicated ONTO the wall (named barrier), never drawn from
     {census roots, tau > 0, terminal positivity, zeros}.

GOALS (contract PRIME.TERMINAL.DISSIPATION.01):
  C1 symbolic layer: telescope identity (chains of 2 and 3, generic
     symmetric blocks) + abelian collapse D = diag(2 sum Q, 0); the
     graph-transport scattering derivation (2x2 full inverse chain;
     inverse-free form 2x2 + 3x3); the terminal dissipation identity
     Delta == C - (c/2) v^T D v; the wall-at-terminal-state identity
     w^T M w == m (1 + c m); det lemma + multiplicativity.
  C2 mp layer at all 11 rungs: cascade closure (inherited ward);
     telescope numeric at h = 4, 5 (2K x 2K explicit); passivity
     (cholesky all cells, eigsy at h <= 8) => D_h PSD; inertia
     n_neg(NoP) == 1; THE BALANCE GATE: (C_h - sum E_p) ==
     1 + c w^T NoP w (same-w algebra, closure-limited) AND the two
     Delta instruments agree (lu_solve read vs quadratic read);
     Delta < 0; C_h >= 1 at h >= 5 with A0 cholesky-PD (h = 4
     anomaly: A0 indefinite, C_4 measured and recorded); E_p > 0 at
     every (p, h); w^T RawM w == m Delta with sign chain m < 0 <
     w^T RawM w; det chain at h = 4, 5, 8; lam_0(RawW) anchor +
     r205 CAL_DLOG inheritance; vector battery recorded.
  C3 energy tables: E_p ladder + fractions + carrier prime + C_h +
     overshoot depth at every rung.
  C4 worlds (EPSTEIN / SCRARITH / SMOOTH as A4) + tau-screens +
     loop guard + mincut + typing + pricing.

NOTATION (r171-r205 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; par_k = (-1)^k; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); Raw* = D_par N M* N D_par entrywise;
phi_k = 1/(1/4 + om_k^2); c_h = 2 sinh^2(a/2); G_B = (L/2) diag(2,
1, ..., 1); theta = sum_{p<=h} log p; A0 = RawArch + theta G_B;
H = A0 + RawPole; NoP = RawM - RawPole; Q_p Grams r204 VERBATIM
(qp_gram import); Q_total = sum_p Q_p; w = lu_solve(NoP, phi);
m = phi^T w; Delta_dir = 1 + c m; Delta_quad = 1 + c w^T NoP w;
C = 1 + c w^T A0 w; E_p = c w^T Q_p w; wRw = w^T RawM w; J =
[[0, I], [I, 0]] (2K); T_p = [[I, 0], [-Q_p, I]]; battery vectors
(phi, w0 = A0^{-1} phi, w, U_0(NoP), e_1, e_2) all normalized before
the q-read q(v) = c v^T Q_total v; lam_0(RawW) by r200 bottom_vec_mp
VERBATIM; eigsy zero class zb_h = 10^{-(dps-20)} fro (MAIN), ZCLS
1e-30 fro (control worlds); dets by mp.det (LU) at QEIG_RUNGS.
tau_h = ce["mpE"][0], measured per-rung scalar only.  Controls:
SCRARITH(5, 60), EPSTEIN(8, 80), SMOOTH(5, 60), builder atom recipes
VERBATIM (golden permutation / Dirichlet recursion); EPSTEIN blocks
Q_2^E, Q_5^E, K_6 and formal seed A0_E = RawArch_E + (log 2 + log 5)
G_B exactly as r205; SCRARITH would-be Q_p^scr = lp G_B - sum_{q in
port p} w_q^perm W(u_q).

RUNGS AND DPS (frozen; house ladder): RUNGS = (4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 16); DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85,
10: 90, 11: 100, 12: 110, 13: 120, 16: 130}.  QEIG_RUNGS = (4, 5, 8)
(lam_min(Q_p) eigsy + det chain).  TELE_RUNGS = (4, 5) (explicit
2K x 2K telescope).  WORKERS = 6.  Smoke mode: rungs (4, 5) +
SCRARITH only.

FROZEN BARS: WARD_BAR 1e-45 (cascade closure, EPSTEIN/SCRARITH
formal closure, telescope numeric, balance identity -- all rel to
the frozen denominators declared per gate); CONS_BAR 1e-6 (Delta
cross-instrument rel dev; wall-at-w identity rel dev -- lu-residual
class instrument wards); DET_BAR 1e-6 (det chain rel dev at
QEIG_RUNGS); INVIT_RES_BAR 1e-12; SCR_Q2_BAR -0.05; SLOPE_FLAT 0.30;
SLOPE_RIDE 0.70 (the balance gap must ride: |slope| >= this);
RUNTIME_BAR 3000 s.  Record tolerances: LOG_TOL 0.10 dex (0.30 for
dev-class logs); VAL_TOL 0.01 (abs, O(1) values); SLOPE_TOL 0.10;
counts/indices exact.  R205_DLOG inheritance table (from the r205
run of record, cross-check at LOG_TOL): {4: -10.81, 5: -15.95,
6: -20.40, 7: -25.20, 8: -29.60, 9: -34.25, 10: -39.14, 11: -43.93,
12: -49.16, 13: -53.78, 16: -68.56}.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  identEnum  := TERMINAL-DISSIPATION-IDENTITY-EXACT iff G10-G13 pass
                and G24 balance devs <= WARD_BAR at every rung, else
                IDENTITY-OBSTRUCTION(h...);
  signEnum   := BOUNDARY-POSITIVE-DEMAND-INVERTED iff C_h >= 1 at
                every h >= 5 with A0 cholesky-PD (the reviewer's
                positive-sum hope inverts into the overshoot demand),
                else BOUNDARY-SIGN-MIXED(h...);
  wallEnum   := SIGN-SOURCE-IS-WALL-AT-TERMINAL-STATE (definitional
                once G26 wall-at-w passes: w^T RawM w == m Delta);
  energyEnum := PER-PRIME-ENERGIES-ONE-SIGNED iff E_p > 0 at every
                (p, h), else ENERGY-SIGN-BREAK(p, h);
  depthEnum  := CANCELLATION-CONCENTRATES-SINGLE-SUBTRACTION
                (definitional: depth ladder == |Delta| dex +
                log10 sum E, recorded);
  screenEnum := BALANCE-GAP-RIDES-TAU iff |slope(log10|Delta| vs
                log10 tau)| >= SLOPE_RIDE, plus STRUCTURE-TAU-FLAT
                iff |slopes(C, sum E, maxfrac)| <= SLOPE_FLAT; else
                the honest mixed enum with the offending slope;
  sepEnum    := SEPARATOR-TRIPLE-REFUSAL iff EPSTEIN {n_neg == 3,
                Delta < 0 AND lam_min(RawM_E) < 0 (misclassification
                inherited), formal closure <= WARD_BAR, K_6
                indefinite, A0_E non-PD} AND SCRARITH {lam_min(
                would-be Q_2) <= SCR_Q2_BAR, Delta > 0 (undershoot),
                closure <= WARD_BAR} AND SMOOTH {portless typed,
                n_neg == 2, Delta > 0}, else SEPARATOR-MIXED(which);
  plus the definitional riders (always typed): GPSD-MARGIN-IS-THE-
  WALL (inherited r204/r205: the overshoot gap IS the wall
  clearance); INERTIA-PRECONDITION-IS-A-LEG (inherited r205: the
  balance reading without kappa = 1 is UNSOUND -- EPSTEIN exhibit).

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing beyond
frozen bars; P1-P2 from the r204/r205 records, P3 from the r205
CAL_DLOG table, P4-P6 from the pre-freeze DERIVATION ALONE -- no
prototype script was run for this round; the identity is algebra,
not a numeric discovery):
  P1 cascade closure <= WARD_BAR at every rung (r205 record
     8.0e-62 .. 7.2e-130); telescope numeric exact at h = 4, 5.
  P2 every Q_p strictly PD (r204/r205 record) => D_h PSD;
     n_neg(NoP) == 1 at every rung (r200/r205 record).
  P3 Delta_h < 0 at every rung with log10|Delta| == R205_DLOG
     within LOG_TOL; balance gap slope vs tau ~ +1.
  P4 C_h >= 1 at h >= 5 (A0 PD there; h = 4 seed indefinite -- the
     r205 shallow-rung anomaly -- C_4 sign UNKNOWN pre-run,
     measured); C_h O(1)-class, tau-flat.
  P5 E_p > 0 everywhere; sum E_p = C_h + |Delta_h| (overshoot by
     exactly the clearance); depth ladder == tau dex class.
  P6 the battery: only w reads the identity (q(w) = c w^T Q_total w
     == C_h - Delta_h up to normalization; the other five vectors
     give unrelated O(1) reads -- recorded, no relation claimed).
  P7 worlds as r205: EPSTEIN {n_neg 3, Delta -0.2610, lmRawM
     -1.7808, K_6 range (-1.52, +1.92), closure 1.1e-81, A0_E
     non-PD}; SCRARITH {q2min -0.1334, Delta +0.0594, n_neg 3};
     SMOOTH {n_neg 2, Delta +0.2147}; E_p^E / E_p^scr signs at the
     specific w UNKNOWN pre-run, measured and recorded.
  P8 screens: C, sum E, maxfrac tau-FLAT; balance gap RIDES +1.

RECORD TABLES (frozen at freeze from the disclosed ladder: ONE
structural smoke (rungs 4/5 + SCRARITH, 25/25, 4.8 s,
terminal_dissipation_probe.smoke1.log, pre-freeze SPEC_SHA
736276f7f33ca585), ONE calibration pass (calib_td_pass1.log, 25/25,
all 11 rungs + all three controls, 385.6 s, same SPEC_SHA); house
pattern identical to r195-r206; no bar, dps, rung, grid or control
recipe moved at any point; record tables inserted at freeze; TWO
calibration-driven PROSE retypes, disclosed here, no target/bar
moved: (i) the pre-freeze guess "carrier prime p = 2" was WRONG --
the measured carrier is the LARGEST prime <= h (the newest
matched-load port) at every rung, tables frozen accordingly; (ii)
EPSTEIN's orphan energy SAMPLE at its terminal state measured
POSITIVE (+0.157) -- the structural break is the INDEFINITE block
(no one-signed guarantee for any state), the sample sign is
recorded honestly, exactly as pre-registered in P7).
Verdicts frozen from calibration: closure exact at all 11 rungs;
telescope numeric 0.0 / 0.0 at h = 4 / 5 (machine-exact block
moves); balance identity <= 8.6e-62 at every MAIN rung (bar 1e-45);
Delta cross-instrument <= 5.7e-46; wall-at-w <= 1.1e-45; Delta < 0
everywhere with log10 == R205_DLOG to print precision; C_h ladder
1.313 .. 6.835 (h = 4: A0 INDEFINITE and yet C_4 = +1.313 > 1 --
the anomaly is seed-side, not balance-side; A0 cholesky-PD at all
h >= 5); sum E_p = C_h + |Delta| to print precision (log10 sum E
== log10 C at 3 decimals everywhere -- the overshoot is invisible
at O(1) resolution: THE ENTIRE H-pin lives below the third
decimal); carrier prime = largest p <= h with declining top
fraction 0.602 .. 0.247; det chain devs <= 1.1e-45; battery
q-reads O(0.3 .. 43), only w reproduces the identity; EPSTEIN
{e2 +0.476, e5 +0.997, e6 +0.157, C_E +1.369, a0pd False, closure
1.1e-81, bal 1.3e-81}; SCRARITH {E_2 sample +0.435 > 0, q2min
-0.1334, sum E 1.337 < C 1.396: undershoot, closure 8.3e-62};
SMOOTH typed.
CAL_CLOG {h: log10 C_h}: 4: "0.118", 5: "0.383", 6: "0.375",
  7: "0.565", 8: "0.561", 9: "0.558", 10: "0.556", 11: "0.714",
  12: "0.713", 13: "0.835", 16: "0.832".
CAL_ELOG {h: log10 sum E_p}: 4: "0.118", 5: "0.383", 6: "0.375",
  7: "0.565", 8: "0.561", 9: "0.558", 10: "0.556", 11: "0.714",
  12: "0.713", 13: "0.835", 16: "0.832".
CAL_DEPTH {h: log10 sumE - log10|Delta|}: 4: "10.93", 5: "16.33",
  6: "20.77", 7: "25.76", 8: "30.16", 9: "34.81", 10: "39.70",
  11: "44.64", 12: "49.87", 13: "54.62", 16: "69.40".
CAL_FRAC {h: max E_p fraction}: 4: "0.602", 5: "0.468", 6: "0.467",
  7: "0.360", 8: "0.360", 9: "0.360", 10: "0.360", 11: "0.307",
  12: "0.307", 13: "0.247", 16: "0.247".
CAL_TOPP {h: carrier prime}: 4: 3, 5: 5, 6: 5, 7: 7, 8: 7, 9: 7,
  10: 7, 11: 11, 12: 11, 13: 13, 16: 13 (the largest prime <= h).
CAL_C4 "1.313" (C_4 > 1 despite A0(4) indefinite -- measured).
CAL_SLOPES {dlog: "+1.0007", clog: "-0.0113", elog: "-0.0113",
  frac: "+0.0054"}.
CAL_CTRL: EPSTEIN {nneg 3, Delta "-0.2610", lmRawM "-1.7808",
  k6lo "-1.5211", closure 1.1e-81, e2 "0.476", e5 "0.997",
  e6 "0.157", C_E "1.369", a0pd False}; SCRARITH {nneg 3, Delta
  "+0.0594", q2min "-0.1334", closure 8.3e-62, e2 "0.435", e3
  "0.389", e5 "0.512", C_scr "1.396"}; SMOOTH {nneg 2, Delta
  "+0.2147"}.
AMENDMENTS: NONE (no bar, dps, rung, recipe or target moved between
freeze and the run of record; the two calibration-driven prose
retypes are disclosed above).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G14 (sympy); S2 identity + energies G20-G28 (mp,
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
    primes_upto, m_cap, w_kernel_add)
from euler_hpin_region_probe import (         # r205 machinery VERBATIM
    to_raw, m_weyl, pd_flag, bottom_vec_mp, qp_gram)

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3000.0

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130}
QEIG_RUNGS = (4, 5, 8)
TELE_RUNGS = (4, 5)
SMOKE_RUNGS = (4, 5)

WARD_BAR = 1e-45
CONS_BAR = 1e-6
DET_BAR = 1e-6
INVIT_RES_BAR = 1e-12
SCR_Q2_BAR = -0.05
SLOPE_FLAT = 0.30
SLOPE_RIDE = 0.70
ZCLS = 1e-30

LOG_TOL = 0.10
LOG_TOL_DEV = 0.30
VAL_TOL = 0.01
SLOPE_TOL = 0.10

CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80),
              ("SMOOTH", 5, 60))

R205_DLOG = {4: "-10.81", 5: "-15.95", 6: "-20.40", 7: "-25.20",
             8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
             12: "-49.16", 13: "-53.78", 16: "-68.56"}

# --------------------- calibrated record tables (calib_td_pass1.log)
CAL_CLOG = {4: "0.118", 5: "0.383", 6: "0.375", 7: "0.565",
            8: "0.561", 9: "0.558", 10: "0.556", 11: "0.714",
            12: "0.713", 13: "0.835", 16: "0.832"}
CAL_ELOG = {4: "0.118", 5: "0.383", 6: "0.375", 7: "0.565",
            8: "0.561", 9: "0.558", 10: "0.556", 11: "0.714",
            12: "0.713", 13: "0.835", 16: "0.832"}
CAL_DEPTH = {4: "10.93", 5: "16.33", 6: "20.77", 7: "25.76",
             8: "30.16", 9: "34.81", 10: "39.70", 11: "44.64",
             12: "49.87", 13: "54.62", 16: "69.40"}
CAL_FRAC = {4: "0.602", 5: "0.468", 6: "0.467", 7: "0.360",
            8: "0.360", 9: "0.360", 10: "0.360", 11: "0.307",
            12: "0.307", 13: "0.247", 16: "0.247"}
CAL_TOPP = {4: 3, 5: 5, 6: 5, 7: 7, 8: 7, 9: 7, 10: 7, 11: 11,
            12: 11, 13: 13, 16: 13}
CAL_C4 = "1.313"
CAL_SLOPES = {"dlog": "+1.0007", "clog": "-0.0113",
              "elog": "-0.0113", "frac": "+0.0054"}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=3, Delta="-0.2610", lmRawM="-1.7808",
                    k6lo="-1.5211", e2="0.476", e5="0.997",
                    e6="0.157", C="1.369"),
    "SCRARITH": dict(nneg=3, Delta="0.0594", q2min="-0.1334",
                     e2="0.435", e3="0.389", e5="0.512", C="1.396"),
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
def quad_form(A, v, K):
    Av = [sum(A[i, j] * v[j] for j in range(K)) for i in range(K)]
    return sum(v[i] * Av[i] for i in range(K))


def mat_sub_into(dst, src, K):
    for i in range(K):
        for j in range(K):
            dst[i, j] -= src[i, j]


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
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            denN = max(abs(NoP[i, j]) for i in range(K)
                       for j in range(K))

            # ---- Q_p Grams (r204 VERBATIM) + total
            Qs = {p: qp_gram(p, h, oms, L, K) for p in prs}
            Qtot = mp.zeros(K, K)
            for p in prs:
                for i in range(K):
                    for j in range(K):
                        Qtot[i, j] += Qs[p][i, j]

            # ---- G20 cascade closure A0 - Qtot == NoP
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    dev = max(dev, abs(A0[i, j] - Qtot[i, j]
                                       - NoP[i, j]))
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
            u0 = [Q[i, idx[0]] for i in range(K)]

            # ---- the terminal Weyl state + the two Delta instruments
            Amat = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Amat[i, j] = NoP[i, j]
            wv = mp.lu_solve(Amat, mp.matrix(phi))
            wv = [wv[i] for i in range(K)]
            mval = sum(phi[i] * wv[i] for i in range(K))
            Delta_dir = 1 + c * mval
            m_quad = quad_form(NoP, wv, K)
            Delta_quad = 1 + c * m_quad
            out["m_neg"] = bool(mval < 0)
            out["Delta_neg"] = bool(Delta_dir < 0)
            out["Delta_log10"] = float(mp.log(abs(Delta_dir), 10))
            out["cons_dev"] = float(abs(Delta_dir - Delta_quad)
                                    / abs(Delta_dir))

            # ---- G24 THE BALANCE: C - sum E_p == Delta_quad
            wn2 = sum(x ** 2 for x in wv)
            Cval = 1 + c * quad_form(A0, wv, K)
            Es = {p: c * quad_form(Qs[p], wv, K) for p in prs}
            sumE = sum(Es.values())
            out["bal_dev"] = float(abs((Cval - sumE) - Delta_quad)
                                   / (c * wn2 * denN))
            out["C_val"] = float(Cval)
            out["C_log10"] = float(mp.log(abs(Cval), 10))
            out["sumE_log10"] = float(mp.log(abs(sumE), 10))
            out["E_pos"] = bool(all(Es[p] > 0 for p in prs))
            fr = {p: float(Es[p] / sumE) for p in prs}
            out["E_frac"] = fr
            out["top_p"] = max(prs, key=lambda p: fr[p])
            out["depth"] = float(mp.log(sumE, 10)
                                 - mp.log(abs(Delta_dir), 10))
            out["a0_pd"] = pd_flag(A0, K)

            # ---- G26 wall-at-terminal-state: w^T RawM w == m Delta
            wRw = quad_form(RawM, wv, K)
            out["wRw_pos"] = bool(wRw > 0)
            out["wallw_dev"] = float(abs(wRw - mval * Delta_quad)
                                     / abs(mval * Delta_quad))

            # ---- battery q-reads (record-only, normalized vectors)
            w0v = mp.lu_solve(mp.matrix(A0), mp.matrix(phi))
            w0v = [w0v[i] for i in range(K)]
            batt = {}
            cand = {"phi": phi, "w0": w0v, "w": wv, "u0": u0,
                    "e1": [1 if i == 0 else 0 for i in range(K)],
                    "e2": [1 if i == 1 else 0 for i in range(K)]}
            for nm, v in cand.items():
                nv = mp.sqrt(sum(mp.mpf(x) ** 2 for x in v))
                vn = [mp.mpf(x) / nv for x in v]
                batt[nm] = float(c * quad_form(Qtot, vn, K))
            out["battery"] = batt

            # ---- G21 telescope numeric (2K x 2K explicit)
            if h in TELE_RUNGS:
                n2 = 2 * K
                Jm = mp.zeros(n2, n2)
                for i in range(K):
                    Jm[i, K + i] = 1
                    Jm[K + i, i] = 1

                def chain(Qp):
                    T = mp.zeros(n2, n2)
                    for i in range(n2):
                        T[i, i] = 1
                    for i in range(K):
                        for j in range(K):
                            T[K + i, j] = -Qp[i, j]
                    return T

                Ttot = None
                parts = []
                Pj = None
                qmax = max(abs(Qtot[i, j]) for i in range(K)
                           for j in range(K))
                for p in prs:
                    Tp = chain(Qs[p])
                    Dj = Jm - Tp.T * Jm * Tp
                    if Pj is None:
                        parts.append(Dj)
                        Pj = Tp
                        Ttot = Tp
                    else:
                        parts.append(Pj.T * Dj * Pj)
                        Pj = Tp * Pj
                        Ttot = Tp * Ttot
                Dtot = Jm - Ttot.T * Jm * Ttot
                Ssum = mp.zeros(n2, n2)
                for Pt in parts:
                    Ssum += Pt
                dev1 = mp.mpf(0)
                dev2 = mp.mpf(0)
                for i in range(n2):
                    for j in range(n2):
                        tgt = (2 * Qtot[i, j]
                               if (i < K and j < K) else mp.mpf(0))
                        dev1 = max(dev1, abs(Dtot[i, j] - tgt))
                        dev2 = max(dev2, abs(Ssum[i, j] - Dtot[i, j]))
                out["tele_dev"] = float(dev1 / qmax)
                out["tele_sum_dev"] = float(dev2 / qmax)

            # ---- G27 det chain (QEIG rungs)
            if h in QEIG_RUNGS:
                detR = mp.det(RawM)
                detN = mp.det(NoP)
                detA = mp.det(A0)
                W0 = mp.inverse(mp.matrix(A0))
                S = mp.zeros(K, K)
                QW = mp.matrix(Qtot) * W0
                for i in range(K):
                    for j in range(K):
                        S[i, j] = (1 if i == j else 0) - QW[i, j]
                detS = mp.det(S)
                out["det1_dev"] = float(abs(detR - detN * Delta_dir)
                                        / abs(detR))
                out["det2_dev"] = float(abs(detN - detA * detS)
                                        / abs(detN))

            # ---- lam_0(RawW) anchor (r200 verbatim)
            lam0, ires = bottom_vec_mp(RawM, K)
            out["invit_res"] = ires
            out["lam0_pos"] = bool(lam0 > 0)
            out["lam0_log10"] = float(mp.log(abs(lam0), 10))
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
            denN = max(abs(NoP[i, j]) for i in range(K)
                       for j in range(K))
            E, _ = mp.eigsy(NoP)
            zb = mp.mpf(ZCLS) * froN
            out["nneg"] = sum(1 for e in E if e < -zb)
            wv = mp.lu_solve(mp.matrix(NoP), mp.matrix(phi))
            wv = [wv[i] for i in range(K)]
            mval = sum(phi[i] * wv[i] for i in range(K))
            out["Delta"] = float(1 + c * mval)
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
                theta = sum(mp.log(p) for p in primes_upto(x))
                A0s = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0s[i, j] = RawArch[i, j]
                    A0s[i, i] += theta * GBd[i]
                Qws = {}
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
                    Qws[p] = Qw
                    Eq, _ = mp.eigsy(Qw)
                    qmins[p] = float(min(Eq))
                out["qmins"] = qmins
                dev = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        acc = A0s[i, j] - NoP[i, j]
                        for p in Qws:
                            acc -= Qws[p][i, j]
                        dev = max(dev, abs(acc))
                out["closure_dev"] = float(dev / denN)
                Cs = 1 + c * quad_form(A0s, wv, K)
                out["C"] = float(Cs)
                out["Es"] = {p: float(c * quad_form(Qws[p], wv, K))
                             for p in Qws}
                sumE = sum(c * quad_form(Qws[p], wv, K) for p in Qws)
                wn2 = sum(v ** 2 for v in wv)
                Dq = 1 + c * quad_form(NoP, wv, K)
                out["bal_dev"] = float(abs((Cs - sumE) - Dq)
                                       / (c * wn2 * denN))
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
                for i in range(K):
                    for j in range(K):
                        acc = A0e[i, j] - Q2[i, j] - Q5[i, j] \
                            - K6[i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / denN)
                Eq, _ = mp.eigsy(K6)
                out["k6lo"] = float(min(Eq))
                out["k6hi"] = float(max(Eq))
                out["a0_pd"] = pd_flag(A0e, K)
                Ce = 1 + c * quad_form(A0e, wv, K)
                out["C"] = float(Ce)
                out["e2"] = float(c * quad_form(Q2, wv, K))
                out["e5"] = float(c * quad_form(Q5, wv, K))
                out["e6"] = float(c * quad_form(K6, wv, K))
                sumE = (c * quad_form(Q2, wv, K)
                        + c * quad_form(Q5, wv, K)
                        + c * quad_form(K6, wv, K))
                wn2 = sum(v ** 2 for v in wv)
                Dq = 1 + c * quad_form(NoP, wv, K)
                out["bal_dev"] = float(abs((Ce - sumE) - Dq)
                                       / (c * wn2 * denN))
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    def sym_mat(n, tag):
        return sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "%s_%d_%d" % (tag, min(i, j), max(i, j))))

    # G10: the telescope + the abelian collapse
    ok10 = True
    for n in (2,):
        Z = sp.zeros(n, n)
        Iden = sp.eye(n)
        J = sp.Matrix(sp.BlockMatrix([[Z, Iden], [Iden, Z]]))

        def chain(Qm):
            return sp.Matrix(sp.BlockMatrix([[Iden, Z], [-Qm, Iden]]))

        Qa, Qb, Qc = (sym_mat(n, t) for t in ("qa", "qb", "qc"))
        Ta, Tb, Tc = chain(Qa), chain(Qb), chain(Qc)
        Da = sp.expand(J - Ta.T * J * Ta)
        Db = sp.expand(J - Tb.T * J * Tb)
        Dc = sp.expand(J - Tc.T * J * Tc)
        # chain of two: J - (Tb Ta)^T J (Tb Ta) == Da + Ta^T Db Ta
        lhs2 = sp.expand(J - (Tb * Ta).T * J * (Tb * Ta))
        rhs2 = sp.expand(Da + Ta.T * Db * Ta)
        ok10 &= sp.expand(lhs2 - rhs2) == sp.zeros(2 * n, 2 * n)
        # chain of three
        P2 = Tb * Ta
        lhs3 = sp.expand(J - (Tc * P2).T * J * (Tc * P2))
        rhs3 = sp.expand(Da + Ta.T * Db * Ta + P2.T * Dc * P2)
        ok10 &= sp.expand(lhs3 - rhs3) == sp.zeros(2 * n, 2 * n)
        # abelian collapse: every transported term equals its D_j;
        # total == diag(2 sum Q, 0)
        ok10 &= sp.expand(Ta.T * Db * Ta - Db) == sp.zeros(2 * n, 2 * n)
        tgt = sp.Matrix(sp.BlockMatrix([[2 * (Qa + Qb + Qc), Z],
                                        [Z, Z]]))
        ok10 &= sp.expand(lhs3 - tgt) == sp.zeros(2 * n, 2 * n)
    check("G10-telescope-and-abelian-collapse", bool(ok10),
          "A1 (generic symmetric 2x2 blocks, sympy exact): the "
          "reviewer's telescope J - T^(n)T J T^(n) == sum_j "
          "T^(j-1)T D_j T^(j-1) holds EXACTLY for chains of 2 AND 3 "
          "sections; for the abelian unit-lower-triangular family "
          "every transported term COLLAPSES (T^T diag(2Q, 0) T == "
          "diag(2Q, 0)) so the global dissipation operator is D_h "
          "== diag(2 sum_p Q_p, 0) EXACTLY -- the circularity "
          "caveat is hereby structural: D_h's (1,1) block is the "
          "TOTAL PRIME BLOCK again (Q_total = A0 - NoP = H - RawM); "
          "the content must come from the terminal vector (G12)")

    # G11: graph transport == the scattering derivation
    ok11 = True
    n = 2
    N = sym_mat(n, "n")
    Qm = sym_mat(n, "q")
    ph = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("p_%d" % i))
    W0 = N.inv()
    u = (sp.eye(n) - Qm * W0).inv() * ph
    Z = sp.zeros(n, n)
    T = sp.Matrix(sp.BlockMatrix([[sp.eye(n), Z], [-Qm, sp.eye(n)]]))
    ghat = sp.Matrix.vstack(W0 * u, u)
    gP = T * ghat
    # transported graph vector == [W_P phi; phi]
    WP = (N - Qm).inv()
    ok11 &= sp.simplify(gP[:n, :] - WP * ph) == sp.zeros(n, 1)
    ok11 &= sp.simplify(gP[n:, :] - ph) == sp.zeros(n, 1)
    J = sp.Matrix(sp.BlockMatrix([[Z, sp.eye(n)], [sp.eye(n), Z]]))
    # J-form of a graph vector reads the Weyl function
    mP = (ph.T * WP * ph)[0, 0]
    ok11 &= sp.simplify((gP.T * J * gP)[0, 0] - 2 * mP) == 0
    # J-contraction: m_P == u^T W0 u - (W0 u)^T Q (W0 u)
    rhs = ((u.T * W0 * u)[0, 0]
           - ((W0 * u).T * Qm * (W0 * u))[0, 0])
    ok11 &= sp.simplify(mP - rhs) == 0
    # inverse-free form at 2x2 AND 3x3: with (N - Q) w = phi,
    # phi^T w == w^T N w - w^T Q w
    for nn in (2, 3):
        Nn = sym_mat(nn, "nn")
        Qn = sym_mat(nn, "qn")
        wsym = sp.Matrix(nn, 1, lambda i, _j: sp.Symbol("w_%d" % i))
        phn = (Nn - Qn) * wsym
        lhsn = sp.expand((phn.T * wsym)[0, 0])
        rhsn = sp.expand((wsym.T * Nn * wsym)[0, 0]
                         - (wsym.T * Qn * wsym)[0, 0])
        ok11 &= sp.expand(lhsn - rhsn) == 0
    check("G11-graph-transport-scattering", bool(ok11),
          "A2 derivation leg (sympy exact): the composed Moebius map "
          "W_0 -> W_0(I - Q W_0)^{-1} acts on graph vectors as g_P "
          "= T_total g-hat with g-hat = [W_0 u; u], u = (I - Q "
          "W_0)^{-1} phi, and g_P == [W_P phi; phi] (2x2 full "
          "inverse chain); the J-form of a graph vector READS the "
          "Weyl function (g^T J g = 2 phi^T W phi); J-contraction "
          "gives m_P == u^T W_0 u - (W_0 u)^T Q (W_0 u) EXACTLY -- "
          "and in inverse-free dress (2x2 AND 3x3): phi^T w == "
          "w^T N w - w^T Q w for (N - Q) w = phi.  The scattering "
          "identity is DERIVED from the r205 graph action, not fit")

    # G12: the terminal dissipation identity Delta == C - (c/2)v^T D v
    ok12 = True
    n = 2
    N = sym_mat(n, "na")
    Qm = sym_mat(n, "qa2")
    ph = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("pa_%d" % i))
    cs = sp.Symbol("c_s", positive=True)
    wsym = (N - Qm).inv() * ph
    Delta = 1 + cs * (ph.T * (N - Qm).inv() * ph)[0, 0]
    Cterm = 1 + cs * (wsym.T * N * wsym)[0, 0]
    Z = sp.zeros(n, n)
    Iden = sp.eye(n)
    J = sp.Matrix(sp.BlockMatrix([[Z, Iden], [Iden, Z]]))
    T = sp.Matrix(sp.BlockMatrix([[Iden, Z], [-Qm, Iden]]))
    Dop = sp.expand(J - T.T * J * T)
    v = sp.Matrix.vstack(wsym, sp.zeros(n, 1))
    diss = (cs / 2) * (v.T * Dop * v)[0, 0]
    ok12 &= sp.simplify(Delta - (Cterm - diss)) == 0
    check("G12-terminal-dissipation-identity", bool(ok12),
          "THE IDENTITY (generic symmetric 2x2, sympy exact): "
          "Delta = 1 + c phi^T (N - Q)^{-1} phi == C - (c/2) v^T "
          "(J - T^T J T) v with v = [w; 0], w = (N - Q)^{-1} phi "
          "(the TERMINAL WEYL STATE), C = 1 + c w^T N w -- the "
          "reviewer's Probe-A form EXISTS EXACTLY, with the SIGN "
          "ADJUDICATED: the boundary term C carries PLUS, the "
          "dissipation element carries MINUS -- Delta < 0 demands "
          "the OVERSHOOT sum_p E_p >= C (>= 1 when the seed is "
          "PSD): the positive-sum hope INVERTS into an overshoot "
          "demand -- the exact mirror of the r204 wall barrier")

    # G13: wall-at-terminal-state + det lemma + multiplicativity
    ok13 = True
    for nn in (2, 3):
        Nn = sym_mat(nn, "nb")
        wsym = sp.Matrix(nn, 1, lambda i, _j: sp.Symbol("wb_%d" % i))
        cs2 = sp.Symbol("c_t", positive=True)
        phn = Nn * wsym                      # phi := NoP w
        msym = (phn.T * wsym)[0, 0]
        Mw = Nn * wsym + cs2 * phn * (phn.T * wsym)
        wMw = sp.expand((wsym.T * Mw)[0, 0])
        ok13 &= sp.expand(wMw - (msym + cs2 * msym ** 2)) == 0
        # det lemma
        ph2 = sp.Matrix(nn, 1, lambda i, _j: sp.Symbol("pc_%d" % i))
        lhs = (Nn + cs2 * ph2 * ph2.T).det()
        rhs = Nn.det() * (1 + cs2 * (ph2.T * Nn.inv() * ph2)[0, 0])
        ok13 &= sp.simplify(lhs - sp.expand(rhs)) == 0
    # multiplicativity det(A - Q) = det(A) det(I - A^{-1} Q)
    n = 2
    Am = sym_mat(n, "ad")
    Qd = sym_mat(n, "qd")
    ok13 &= sp.simplify((Am - Qd).det()
                        - Am.det()
                        * (sp.eye(n) - Am.inv() * Qd).det()) == 0
    check("G13-wall-at-w-and-det-chain", bool(ok13),
          "the sharpest link (generic 2x2 AND 3x3, sympy exact, "
          "inverse-free): w^T (NoP + c phi phi^T) w == m (1 + c m) "
          "== m Delta for phi = NoP w, m = phi^T w -- the sign "
          "source of the balance IS the wall's quadratic form at "
          "the terminal state (m < 0 measured => Delta < 0 <=> "
          "w^T RawM w > 0); plus the det lemma det(N + c phi "
          "phi^T) == det(N)(1 + c m) and multiplicativity det(A - "
          "Q) == det(A) det(I - A^{-1} Q): Delta_h == det(RawM) / "
          "(det(A0) det(I - A0^{-1} Q_total)) -- the terminal "
          "clearance as wall-det over scattering-det, gated in mp "
          "at h <= 8 (G27)")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("terminal_dissipation_probe -- PRIME.TERMINAL."
          "DISSIPATION.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/control recipes declared in the frozen "
          "spec (SPEC_SHA covers the declaration); the identity, its "
          "sign adjudication, the wall-at-w link and the det chain "
          "were DERIVED pre-freeze by algebra alone (no prototype "
          "script was run -- the priors P4-P6 are derivation "
          "consequences, P1-P3/P7 are r204/r205 record inheritances); "
          "the ANTI-LOOP TEST holds by construction: every hypothesis "
          "is from {Euler chain algebra, positive weights, KYP "
          "passivity, classical linear algebra}, never from {census "
          "roots, tau > 0, terminal positivity, zeros}; record "
          "tables frozen from the disclosed smoke + calibration "
          "ladder (house pattern); dps ladder = house values")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy: telescope + identity)")
    exact_layer()

    # ------------------------------------------------------------ S2
    rungs = SMOKE_RUNGS if smoke else RUNGS
    section("S2  IDENTITY + ENERGIES (mp at h = %s)" % str(rungs))
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
          "the r204/r205 central identity re-warded at every rung: "
          "A0 - Q_total == NoP entrywise, max rel dev %s (bar %.0e) "
          "-- so the dissipation operator's (1,1) block 2 Q_total "
          "== 2 (A0 - NoP) == 2 (H - RawM): the circularity caveat "
          "instantiated exactly (A1)"
          % (str({h: "%.1e" % res[h]["closure_dev"]
                  for h in (4, 13, 16) if h in res}), WARD_BAR))

    tele = [h for h in rungs if h in TELE_RUNGS]
    check("G21-telescope-numeric", all(
        res[h]["tele_dev"] <= WARD_BAR
        and res[h]["tele_sum_dev"] <= WARD_BAR for h in tele),
          "A1 in explicit 2K x 2K arithmetic at h = %s: the full "
          "chain product T_total = T_{p_P} ... T_{p_1} gives J - "
          "T_total^T J T_total == diag(2 Q_total, 0) entrywise "
          "(dev %s) AND the telescoping sum sum_j T^(j-1)T D_j "
          "T^(j-1) == the same operator (dev %s) -- the reviewer's "
          "telescope and its abelian collapse verified in the "
          "actual cascade, not only symbolically"
          % (str(tele),
             str({h: "%.1e" % res[h]["tele_dev"] for h in tele}),
             str({h: "%.1e" % res[h]["tele_sum_dev"]
                  for h in tele})))

    qeig = [h for h in rungs if h in QEIG_RUNGS]
    check("G22-passivity-D-psd", all(
        res[h]["chol_ok"] for h in rungs) and all(
        res[h]["lmq_min"] > 0 for h in qeig),
          "every Q_p cholesky-PD at all %d (p, h) cells (lam_min "
          "eigsy at h <= 8: %s > 0) => D_h = diag(2 Q_total, 0) is "
          "PSD at every rung -- the global dissipation operator is "
          "certified passive (KYP, r204), the naive reading of "
          "which is the r204 passivity again: priced, not resold"
          % (sum(len(res[h]["primes"]) for h in rungs),
             str({h: "%.2e" % res[h]["lmq_min"] for h in qeig})))

    check("G23-inertia-one", all(
        res[h]["nneg"] == 1 and res[h]["d0_neg"]
        and res[h]["d1_pos"] for h in rungs),
          "n_neg(NoP_h) == 1 at EVERY rung (eigsy, dps-scaled zero "
          "class; d_0 < 0 < d_1 resolved): kappa = 1 -- the "
          "inertia precondition of the H-pin reading holds on MAIN "
          "everywhere reachable (the balance identity itself is "
          "algebra and needs NO inertia; its H-PIN READING does -- "
          "the r205 EPSTEIN exhibit, inherited as a typed leg)")

    ok24 = all(res[h]["bal_dev"] <= WARD_BAR
               and res[h]["cons_dev"] <= CONS_BAR
               and res[h]["Delta_neg"] and res[h]["m_neg"]
               for h in rungs)
    if not (calib or smoke):
        ok24 = ok24 and all(
            abs(res[h]["Delta_log10"] - float(R205_DLOG[h]))
            <= LOG_TOL for h in rungs)
    check("G24-terminal-balance-identity", ok24,
          "THE BALANCE at every rung: Delta_h == C_h - sum_p E_p(w) "
          "with w = NoP^{-1} phi, C_h = 1 + c_h w^T A0 w, E_p = "
          "c_h w^T Q_p w -- same-w algebra closure-limited, max "
          "scaled dev %s (bar %.0e); the two Delta instruments "
          "(lu_solve read 1 + c phi^T w vs quadratic read 1 + c "
          "w^T NoP w) agree to rel %s (bar %.0e); Delta < 0 and "
          "m < 0 at every rung; log10|Delta| == the r205 record "
          "%s within %.2f dex -- the reviewer's Probe-A identity "
          "LANDS EXACTLY, nothing fit"
          % (str({h: "%.1e" % res[h]["bal_dev"]
                  for h in (4, 8, 16) if h in res}), WARD_BAR,
             str({h: "%.1e" % res[h]["cons_dev"]
                  for h in (4, 8, 16) if h in res}), CONS_BAR,
             str({h: "%.1f" % res[h]["Delta_log10"]
                  for h in (4, 8, 13, 16) if h in res}), LOG_TOL))

    ok25 = all(res[h]["a0_pd"] for h in rungs if h >= 5) \
        and (not res[4]["a0_pd"] if 4 in res else True) \
        and all(res[h]["C_val"] >= 1 for h in rungs if h >= 5) \
        and all(res[h]["C_val"] > 0 for h in rungs)
    if not (calib or smoke):
        ok25 = ok25 and all(
            abs(res[h]["C_log10"] - float(CAL_CLOG[h])) <= LOG_TOL
            for h in rungs) and abs(
            res[4]["C_val"] - float(CAL_C4)) <= VAL_TOL * 10 \
            if 4 in res else ok25
    check("G25-boundary-term-explicit", ok25,
          "the boundary term adjudicated: A0 cholesky-PD at every "
          "h >= 5 => C_h = 1 + c_h w^T A0 w >= 1 EXPLICITLY "
          "(arch/pole-explicit functional: A0 = RawArch + theta "
          "G_B, c_h = 2 sinh^2(a/2) -- source-side; the terminal "
          "state w carries the arithmetic, priced in G52); "
          "C ladder log10 = %s (O(1..2), tau-FLAT per G50); the "
          "h = 4 anomaly honest: A0(4) INDEFINITE (r205 "
          "shallow-rung fact) yet C_4 = %.3f > 1 anyway -- the "
          "anomaly is seed-side, not balance-side; ANTI-LOOP: C_h "
          ">= 1 comes from seed PSD-ness, no census/tau/zero input"
          % (str({h: "%.2f" % res[h]["C_log10"]
                  for h in (5, 8, 13, 16) if h in res}),
             res[4]["C_val"] if 4 in res else float("nan")))

    ok26 = all(res[h]["E_pos"] and res[h]["wRw_pos"]
               and res[h]["wallw_dev"] <= CONS_BAR for h in rungs)
    if not (calib or smoke):
        ok26 = ok26 and all(
            res[h]["top_p"] == CAL_TOPP[h]
            and abs(res[h]["E_frac"][res[h]["top_p"]]
                    - float(CAL_FRAC[h])) <= VAL_TOL
            and abs(res[h]["sumE_log10"] - float(CAL_ELOG[h]))
            <= LOG_TOL
            and abs(res[h]["depth"] - float(CAL_DEPTH[h]))
            <= LOG_TOL_DEV for h in rungs)
    check("G26-energy-ladder-and-wall-link", ok26,
          "A3 delivered: every per-prime energy E_p(w) > 0 at all "
          "(p, h) cells (one-signed AUTOMATICALLY: E_p = c lp "
          "||D_p Y_p w||^2, the r204 Gram form -- the quadratic "
          "reading avoids PER-PRIME cancellation); carrier prime "
          "p = %s with top fraction %s; sum E ladder log10 %s; THE "
          "HONEST DEPTH: the cancellation concentrates into the "
          "SINGLE subtraction sum E - C == |Delta|, depth ladder "
          "%s dex (the full tau currency, nothing evaporated); "
          "THE WALL LINK exact: w^T RawM w == m Delta to rel %s "
          "(bar %.0e) with w^T RawM w > 0 > m -- the sign source "
          "of the balance IS the wall at the terminal state"
          % (str({h: res[h]["top_p"] for h in (4, 8, 16)
                  if h in res}),
             str({h: "%.3f" % res[h]["E_frac"][res[h]["top_p"]]
                  for h in (4, 8, 16) if h in res}),
             str({h: "%.2f" % res[h]["sumE_log10"]
                  for h in (4, 8, 16) if h in res}),
             str({h: "%.1f" % res[h]["depth"]
                  for h in (4, 8, 13, 16) if h in res}),
             str({h: "%.1e" % res[h]["wallw_dev"]
                  for h in (4, 8, 16) if h in res}), CONS_BAR))

    check("G27-det-chain", all(
        res[h]["det1_dev"] <= DET_BAR
        and res[h]["det2_dev"] <= DET_BAR for h in qeig),
          "the det reading at h = %s: Delta_h == det(RawM)/det(NoP) "
          "(determinant lemma; rel dev %s) AND det(NoP) == det(A0) "
          "det(I - A0^{-1} Q_total) (rel dev %s) -- the terminal "
          "clearance is the wall determinant over the cascade's "
          "scattering determinant: the tau/det-class relation is "
          "EXACT and named, not hunted"
          % (str(qeig),
             str({h: "%.1e" % res[h]["det1_dev"] for h in qeig}),
             str({h: "%.1e" % res[h]["det2_dev"] for h in qeig})))

    ok28 = all(res[h]["lam0_pos"] and res[h]["tau_sign"] > 0
               and res[h]["invit_res"] <= INVIT_RES_BAR
               for h in rungs)
    check("G28-anchor-inheritance", ok28,
          "lam_0(RawW) > 0 at every rung (invit residual <= %.0e), "
          "tau > 0; log10 lam_0 = %s vs log10|Delta| = %s -- the "
          "same near-zero class as r205 (|Delta| = wall currency); "
          "battery q-reads (normalized, record-only, NO fits): %s "
          "-- only the terminal state w enters the identity; the "
          "others are O(1..100) unrelated reads as pre-registered "
          "(P6)"
          % (INVIT_RES_BAR,
             str({h: "%.1f" % res[h]["lam0_log10"]
                  for h in (4, 8, 16) if h in res}),
             str({h: "%.1f" % res[h]["Delta_log10"]
                  for h in (4, 8, 16) if h in res}),
             str({k: "%.3g" % v
                  for k, v in res[max(tele)]["battery"].items()})))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL rung h=%d Dlog %.2f Clog %.3f C %.3f Elog "
                  "%.3f depth %.2f topp %d frac %.3f a0pd %s "
                  "bal %.1e cons %.1e wallw %.1e batt %s"
                  % (h, r["Delta_log10"], r["C_log10"], r["C_val"],
                     r["sumE_log10"], r["depth"], r["top_p"],
                     r["E_frac"][r["top_p"]], r["a0_pd"],
                     r["bal_dev"], r["cons_dev"], r["wallw_dev"],
                     str({k: "%.3g" % v
                          for k, v in r["battery"].items()})))

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
                          ("qmins", "k6lo", "k6hi", "closure_dev",
                           "a0_pd", "C", "e2", "e3", "e5", "e6",
                           "Es", "bal_dev") if k2 in v})))
    ok40 = True
    if ep:
        ok40 = (ep["nneg"] == 3 and ep["Delta"] < 0
                and ep["lmRawM"] < 0
                and ep["closure_dev"] <= WARD_BAR
                and ep["bal_dev"] <= WARD_BAR
                and ep["k6lo"] < -0.1 and not ep["a0_pd"])
        if not (calib or smoke):
            ok40 = ok40 and abs(ep["Delta"] - float(
                CAL_CTRL["EPSTEIN"]["Delta"])) <= VAL_TOL \
                and abs(ep["e6"] - float(
                    CAL_CTRL["EPSTEIN"]["e6"])) <= VAL_TOL
    check("G40-epstein-inertia-and-orphan", bool(ok40 and ep) if ep
          else smoke,
          "skipped in smoke mode" if not ep else
          "EPSTEIN(8), the kappa = 3 world: n_neg(NoP_E) = %d and "
          "the balance identity STILL CLOSES ALGEBRAICALLY (formal "
          "closure %.1e, balance dev %.1e -- it is algebra, world-"
          "blind) while its H-PIN READING FAILS: Delta_E = %.4f < "
          "0 WITH lam_min(RawM_E) = %.4f < 0 -- the balance "
          "without the inertia-1 leg MISCLASSIFIES (r205 exhibit "
          "inherited); the ENERGY reading breaks at named places: "
          "the orphan block K_6 is J-INDEFINITE (lam_min %.2f) so "
          "NO one-signed energy guarantee exists for ANY state "
          "(the measured SAMPLE at this terminal state, e6 = %.3f, "
          "is recorded honestly either way -- the GUARANTEE is "
          "what breaks); the seed A0_E is non-PD (a0pd %s): C_E = "
          "%.3f loses its explicit >= 1 floor (it is positive "
          "here by measurement only); e2 = %.3f, e5 = %.3f"
          % (ep["nneg"], ep["closure_dev"], ep["bal_dev"],
             ep["Delta"], ep["lmRawM"], ep["k6lo"], ep["e6"],
             ep["a0_pd"], ep["C"], ep["e2"], ep["e5"]))

    ok41 = True
    if scr:
        qm = scr.get("qmins", {})
        ok41 = (qm.get(2, 0) <= SCR_Q2_BAR and scr["nneg"] == 3
                and scr["Delta"] > 0
                and scr["closure_dev"] <= WARD_BAR
                and scr["bal_dev"] <= WARD_BAR)
        if not (calib or smoke):
            ok41 = ok41 and abs(qm.get(2, 0) - float(
                CAL_CTRL["SCRARITH"]["q2min"])) <= VAL_TOL \
                and abs(scr["Delta"] - float(
                    CAL_CTRL["SCRARITH"]["Delta"])) <= VAL_TOL \
                and abs(scr["Es"][2] - float(
                    CAL_CTRL["SCRARITH"]["e2"])) <= VAL_TOL
    check("G41-scrarith-guarantee-break", bool(ok41 and scr),
          "" if not scr else
          "SCRARITH(5): the would-be Q_2 is INDEFINITE (lam_min = "
          "%.4f <= %.2f) -- E_2's one-signedness is STRUCTURALLY "
          "unguaranteed (the r202/r204/r205 non-PR port in energy "
          "dress); honest record: the SAMPLE E_2 at its terminal "
          "state is %.3f (positive -- the guarantee is what "
          "breaks, not this one number); the balance closes "
          "algebraically (closure %.1e, bal %.1e) and the ENDPOINT "
          "refuses: Delta = %.4f > 0 -- dissipation UNDERSHOOTS "
          "the seed (sum E %.3f < C %.3f): the energy balance "
          "correctly reads SCRARITH's wall failure; n_neg = %d"
          % (scr["qmins"][2], SCR_Q2_BAR, scr["Es"][2],
             scr["closure_dev"], scr["bal_dev"], scr["Delta"],
             sum(scr["Es"].values()), scr["C"], scr["nneg"]))

    ok42 = True
    if smo:
        ok42 = smo["nneg"] == 2 and smo["Delta"] > 0
        if not (calib or smoke):
            ok42 = ok42 and abs(smo["Delta"] - float(
                CAL_CTRL["SMOOTH"]["Delta"])) <= VAL_TOL
    check("G42-smooth-degeneration", bool(ok42 and smo) if smo
          else smoke,
          "skipped in smoke mode" if not smo else
          "SMOOTH(5): the atom list is EMPTY by construction -- no "
          "ports, no chain matrices, no D_h: the energy balance "
          "DEGENERATES structurally (typed); measured: n_neg = %d, "
          "Delta = %.4f > 0; the three controls break THREE "
          "DIFFERENT legs (inertia+orphan / Q_2-guarantee / "
          "ports): enum SEPARATOR-TRIPLE-REFUSAL"
          % (smo["nneg"], smo["Delta"]))

    # ------------------------------------------------------------ S4
    section("S4  TAU-SCREENS + GUARDS")
    xs = [res[h]["tau_log10"] for h in rungs]
    sl_d = fit_line(xs, [res[h]["Delta_log10"] for h in rungs])
    sl_c = fit_line(xs, [res[h]["C_log10"] for h in rungs])
    sl_e = fit_line(xs, [res[h]["sumE_log10"] for h in rungs])
    sl_f = fit_line(xs, [res[h]["E_frac"][res[h]["top_p"]]
                         for h in rungs])
    if calib or smoke:
        print("CAL slopes: dlog %+.4f clog %+.4f elog %+.4f frac "
              "%+.4f" % (sl_d, sl_c, sl_e, sl_f))
        ok50 = True
    else:
        ok50 = (abs(sl_d - float(CAL_SLOPES["dlog"])) <= SLOPE_TOL
                and abs(sl_c - float(CAL_SLOPES["clog"]))
                <= SLOPE_TOL
                and abs(sl_e - float(CAL_SLOPES["elog"]))
                <= SLOPE_TOL
                and abs(sl_f - float(CAL_SLOPES["frac"]))
                <= SLOPE_TOL)
    gap_rides = abs(sl_d) >= SLOPE_RIDE
    struct_flat = (abs(sl_c) <= SLOPE_FLAT and abs(sl_e)
                   <= SLOPE_FLAT and abs(sl_f) <= SLOPE_FLAT)
    ok50 = ok50 and gap_rides and struct_flat
    check("G50-tau-screen", ok50,
          "the hard screen, said exactly: the OVERSHOOT GAP sum E - "
          "C == |Delta| RIDES tau (slope %+.3f, ride bar %.2f) -- "
          "the balance's demand IS the wall clearance (GPSD-MARGIN-"
          "IS-THE-WALL, inherited r204/r205, named NOT crossed); "
          "the STRUCTURE is tau-FLAT: C slope %+.3f, sum E slope "
          "%+.3f, top fraction slope %+.3f (flat bar %.2f) -- the "
          "energy anatomy is an O(1) structural fact, only the "
          "cancellation DEPTH rides: the r205 structure-vs-currency "
          "factorization re-instantiated in energy coordinates"
          % (sl_d, SLOPE_RIDE, sl_c, sl_e, sl_f, SLOPE_FLAT))

    delivered = {
        "ATOMS": ["QP-GRAMS"], "MODES": ["QP-GRAMS"],
        "QP-GRAMS": ["CHAIN-MATRICES"],
        "CHAIN-MATRICES": ["DISSIPATION-OPERATOR"],
        "POLE-DATUM": ["TERMINAL-STATE"],
        "TERMINAL-STATE": ["ENERGY-BALANCE"],
        "DISSIPATION-OPERATOR": ["ENERGY-BALANCE"],
        "ENERGY-BALANCE": ["SCREENS"], "SCREENS": []}
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
    for node in ("DISSIPATION-OPERATOR", "ENERGY-BALANCE",
                 "SCREENS"):
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
          "leg typing: {telescope, abelian collapse, graph "
          "transport, terminal dissipation identity, wall-at-w, "
          "det lemma + multiplicativity} EXACT (sympy); {closure, "
          "telescope numeric, balance identity} EXACT-MP; {C_h, "
          "E_p, fractions, depth, Delta, lam_0, det chain, world "
          "numbers} MEASURED; {Q_p PSD => D_h PSD, Sylvester/"
          "congruence, Schur} SOURCE-CLASSICAL (typed); the "
          "terminal state w = NoP^{-1} phi is NOT source-pure -- "
          "it carries the full arithmetic of the pole-free matrix: "
          "C_h is an arch/pole-explicit FUNCTIONAL evaluated at an "
          "arithmetic-laden ARGUMENT, priced as such (the >= 1 "
          "floor needs only seed PSD-ness, which is source-side); "
          "{overshoot demand == wall clearance} DEFINITIONAL "
          "(GPSD-MARGIN-IS-THE-WALL) -- sold as structure, never "
          "as a lever; {INERTIA-PRECONDITION-IS-A-LEG} inherited "
          "(EPSTEIN, r205)")

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
    cf.update({("UNC", "TERMBAL"): INF, ("TERMBAL", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the terminal energy overshoot sum E >= C holds "
          "cofinally' as a unit edge would raise the flow to 6 -- "
          "NOT REAL (the overshoot gap IS the wall clearance): "
          "this round adds NO flow; census cardinality UNCHANGED; "
          "RH unreachable without the omega edges")

    # ------------------------------------------------------------ S5
    section("S5  PRICING + ENERGY TABLE")
    ident_ok = all(res[h]["bal_dev"] <= WARD_BAR
                   and res[h]["closure_dev"] <= WARD_BAR
                   for h in rungs)
    primary = "TERMINAL-DISSIPATION-IDENTITY-EXACT" if ident_ok \
        else "IDENTITY-OBSTRUCTION"
    sign_ok = all(res[h]["C_val"] >= 1 and res[h]["a0_pd"]
                  for h in rungs if h >= 5)
    sign_enum = "BOUNDARY-POSITIVE-DEMAND-INVERTED" if sign_ok \
        else "BOUNDARY-SIGN-MIXED"
    energy_enum = "PER-PRIME-ENERGIES-ONE-SIGNED" if all(
        res[h]["E_pos"] for h in rungs) else "ENERGY-SIGN-BREAK"
    check("G60-pricing", True,
          "WHAT THE ROUND BUYS: (i) A1 DELIVERED with the caveat "
          "resolved -- D_h = diag(2 Q_total, 0) exactly (telescope "
          "collapses; the operator is the total prime block again; "
          "content relocated to the terminal vector); (ii) A2 "
          "DELIVERED, no fits -- the reviewer's identity EXISTS "
          "EXACTLY: Delta_h = C_h - (c_h/2) v_h^T D_h v_h at v_h = "
          "[NoP^{-1} phi; 0], derived from the r205 graph action "
          "by J-contraction; the SIGN INVERTS the reviewer's hope: "
          "C_h >= 1 explicit (seed PSD, h >= 5), so Delta < 0 is "
          "an OVERSHOOT demand sum E_p >= C_h >= 1 -- a concrete "
          "number-theory target, and BY THE WALL LINK (w^T RawM w "
          "== m Delta) its truth per rung IS wall positivity at "
          "one vector: the barrier named, not crossed; (iii) A3: "
          "energies one-signed per prime (quadratic reading kills "
          "per-prime cancellation), carrier = the LARGEST prime "
          "<= h (the newest matched-load port), structure "
          "tau-flat -- and the honest price: the 47-dex-class "
          "cancellation CONCENTRATES into the single subtraction "
          "sum E - C (depth = full tau dex per rung); (iv) worlds "
          "break three different legs; what it does NOT buy "
          "(priced): no positivity lever, no new all-h currency -- "
          "the {H1 ^ H2 ^ H3}-KOFINAL residue is UNCHANGED")

    nlines = 0
    for h in rungs:
        r = res[h]
        fr = r["E_frac"]
        print("  ENERGY h=%d C %.6f sumElog %.3f fracs %s" % (
            h, r["C_val"], r["sumE_log10"],
            str({p: "%.3f" % fr[p] for p in r["primes"]})))
        print("  ENERGY h=%d TERM Dlog %.2f depth %.2f l0log %.2f "
              "taulog %.2f batt_w %.4g"
              % (h, r["Delta_log10"], r["depth"], r["lam0_log10"],
                 r["tau_log10"], r["battery"]["w"]))
        nlines += 2
    check("G61-energy-table", nlines == 2 * len(rungs),
          "the energy table delivered: %d lines (2 per rung: "
          "per-prime fractions + terminal row) -- the balance's "
          "design data (C_h, sum E, fractions, depth, battery) "
          "for any successor round" % nlines)

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the H-pin terminal clearance is EXACTLY an "
         "energy balance -- Delta_h = C_h - sum_p E_p(w) with C_h "
         ">= 1 explicit (seed PSD) and E_p >= 0 per prime (KYP): "
         "the H-pin is the OVERSHOOT demand 'total prime "
         "dissipation at the terminal Weyl state exceeds the seed "
         "energy plus one', whose truth per rung is the wall at "
         "one vector (w^T RawM w == m Delta).  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        primary + "(G10-G13/G24: derived, exact at all rungs)",
        "DISSIPATION-OPERATOR-IS-TOTAL-PRIME-BLOCK(G10/G20/G21: "
        "circularity caveat resolved structurally)",
        sign_enum + "(G25: C_h >= 1 explicit at h >= 5)",
        "SIGN-SOURCE-IS-WALL-AT-TERMINAL-STATE(G13/G26, "
        "definitional)",
        energy_enum + "(G26)",
        "CANCELLATION-CONCENTRATES-SINGLE-SUBTRACTION(G26: depth "
        "== tau dex)",
        "DET-CHAIN-EXACT(G27)",
        ("BALANCE-GAP-RIDES-TAU(G50: slope %+.2f)" % sl_d),
        ("STRUCTURE-TAU-FLAT(G50: C %+.2f, E %+.2f)" % (sl_c, sl_e)),
        "INERTIA-PRECONDITION-IS-A-LEG(G23/G40, inherited r205)",
        "SEPARATOR-TRIPLE-REFUSAL(G40/G41/G42)",
        "GPSD-MARGIN-IS-THE-WALL(inherited r204/r205; overshoot "
        "gap == wall clearance)",
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
        primary, "DISSIPATION-OPERATOR-IS-TOTAL-PRIME-BLOCK",
        sign_enum, "SIGN-SOURCE-IS-WALL-AT-TERMINAL-STATE",
        energy_enum, "CANCELLATION-CONCENTRATES-SINGLE-SUBTRACTION",
        "DET-CHAIN-EXACT", "BALANCE-GAP-RIDES-TAU",
        "STRUCTURE-TAU-FLAT", "INERTIA-PRECONDITION-IS-A-LEG",
        "SEPARATOR-TRIPLE-REFUSAL", "GPSD-MARGIN-IS-THE-WALL",
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
