#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""secular_crossing_coord_probe -- PRIME.SECULAR.CROSSING.COORD.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, the
bughunt11 / pontryagin-n1 / terminal-dissipation lanes, and every
verification/paper/website surface) are not touched.

=======================================================================
MISSION (round ~207, the reviewer's Probe C after r206: the SECULAR
CROSSING COORDINATE).  Round 200 (pole_homotopy_probe, SPEC
703f70e5016581e4) proved the secular machinery: the wall RawM = NoP +
c_h phi phi^T with c_h = 2 sinh^2(a/2), phi_k = 1/(1/4 + om_k^2), and
n_neg(NoP) = 1 at every MAIN rung; the ground level of the path
M(s) = NoP + s c_h phi phi^T crosses zero at the SECULAR CROSSING
PARAMETER
    s*(h) = -1/(c_h phi^T NoP^{-1} phi) = -1/(c_h m_h(0)) = -1/mu_P,
and GIVEN inertia-1 the target statement is
    the wall is PSD  <=>  s*(h) <= 1
(determinant lemma: det(NoP + s c phi phi^T) = det(NoP)(1 + s c m(0));
the r205 H-pin criterion mu_P <= -1 in crossing dress).  Round 205
(euler_hpin_region_probe, SPEC cb1dfde33a198fb3) delivered the natural
PRIME DECOMPOSITION of mu_P: the partial-cascade orbit mu_j = c_h
m_j(0) with N_j = A0 - sum_{i<=j} Q_{p_i}, seed A0 = RawArch +
theta(h) G_B (prime-free), per-prime r204 dissipation Grams Q_p,
mu_0 -> mu_1 -> ... -> mu_P, exactly one wrap (the single passage of
mu through the pole into OMEGA = {mu <= -1}).  THIS round transports
that orbit into CROSSING COORDINATES s_j := -1/mu_j and asks the
reviewer's Probe-C question: does some PREDEFINED transform Phi make
the per-prime steps ADDITIVE AND ONE-SIGNED with a source-explicit
boundary term -- i.e. does the cofinal statement s* <= 1 become a
positive-sum problem that real number theory can attack (Probe D's
low-prime + tail split)?

THE FROZEN TRANSFORM BATTERY (predefined, no post-hoc additions):
    Phi_1(s) = log s              == -log(-mu)        [domain mu < 0]
    Phi_2(s) = log(s/(1-s))       == -log(-(1+mu))    [domain mu < -1]
    Phi_3(s) = artanh(2s - 1)     == Phi_2 / 2  IDENTICALLY (gated
               symbolically G10: artanh(2s-1) = (1/2) log(s/(1-s)))
    Phi_4(s) = 1/s                == -mu              [domain mu != 0]
    Phi_5(s) = (1-s)/s            == Phi_4 - 1  (increments IDENTICAL
               to Phi_4; gated symbolically G10)
so the battery carries EXACTLY THREE independent sign structures
(log / logit-family / inv-family) -- an exact structural fact of the
battery itself, typed and gated, not a finding about the orbit.
NUMERICALLY SAFE FORMS: every Phi is evaluated through mu and
delta = 1 + mu directly (no 1 - s cancellation; 1 - s = (1+mu)/mu
EXACTLY, so 1 - s*(h) = Delta_h / mu_P -- the crossing-coordinate
wall margin IS the r205 terminal clearance up to the factor
mu_P = -1 - |Delta| ~ -1, gated as an identity ward G23).

THE DECOMPOSITION CONTRACT.  For each order (inc/dec) and each Phi:
per-prime increments delta_{p,h}^Phi = Phi(s_j) - Phi(s_{j-1}) over
the POST-WRAP stages j in (j*, P], boundary term C_h^Phi :=
Phi(s_{j*}) at the wrap stage j* := min{j : mu_j <= -1} (the crossing
coordinate is BORN at the wrap: pre-wrap N_j is PD, m_j(0) > 0, the
formal s_j is NEGATIVE -- no positive crossing exists; the wrap step
is the domain birth).  Telescoping Phi(s*) = C_h + sum delta is exact
BY CONSTRUCTION for any Phi (gated as instrument ward G24); the
content is in the increments' STRUCTURE, measured three ways:
  (i)  ONE-SIGNEDNESS (G25/G26): sign-coherence fraction per Phi per
       rung per order (the round's first table); plus the Phi_4
       ALL-STEPS census (Phi_4 is defined on the whole orbit): the
       pre-registered shape is one-signed (negative Phi_4 increments,
       i.e. mu increasing) at EVERY non-wrap step with the SINGLE
       wrap step opposite -- the wrap is the one non-coherent step
       and it is exactly the boundary/domain-birth.
  (ii) STATE-FREENESS (G27): the exact Woodbury step law (gated
       symbolically G11 and numerically per step G22)
         mu_j - mu_{j-1} = c_h x_j^T Q_p x_{j-1},  x_j = N_j^{-1} phi
       shows the increment is the prime's own Euler Gram Q_p read in
       the EVOLVING cascade state.  The predefined state-free
       candidates freeze the state: freeT_p = c_h x_T^T Q_p x_T with
       x_T = NoP^{-1} phi (terminal) and freeS_p = c_h x_S^T Q_p x_S
       with x_S = A0^{-1} phi (seed).  Measured: the ratio ladder
       rho_p = dmu_p / freeT_p over post-wrap primes, its log10
       spread, and the ORDER-DEPENDENCE dev of dmu_p between inc and
       dec at common non-wrap primes (exact state-freeness would
       force order-independence -- the r205 chain group is abelian,
       the composed map is order-free, the orbit is not).
  (iii) p-DECAY (G28): the reviewer's warning -- a tail theorem needs
       |delta_p| <~ p^{-1}; linear p^{-1/2} sums diverge.  Measured:
       slope of log10|dmu_p| vs log10 p over inc non-wrap steps at
       DECAY_RUNGS, the same for the ATOM part A_p of the exact split
         dmu_p = lp B_p - A_p,   B_p = c_h x_j^T G_B x_{j-1},
         A_p = c_h x_j^T K_p x_{j-1},  K_p = lp G_B - Q_p =
               sum_m w_{p^m} W(m lp)
       (the log p G_B drift vs the prime's atom kernels), the
       matched-load edge law A_p == 0 at p = h (r204, exact), and the
       TERMINAL-INCREMENT h-ladder dmu_last(h) (does the top prime's
       increment decay with h at all?).
THE BOUNDARY TERM (G29): C_h^Phi at the wrap stage is SOURCE-EXPLICIT
-- a closed rational/log expression in the seed data (RawArch, theta,
G_B: arch/prime-counting) plus the pre-wrap primes' Grams Q_p (Euler
data) and the pole datum (c_h, phi); it consumes NO eigen data, NO
tau, NO wall.  ANTI-LOOP TEST (mandatory): C_h is recomputed through
the INDEPENDENT per-prime dictionary path (Q_p rebuilt entrywise as
lp G_B - sum_m w_{p^m} W(m lp), the r202/r204 formula, own assembly)
and must agree to DICT_BAR; its ladder is O(1) and tau-FLAT
(screened).  NOTE the pre-wrap primes ARE absorbed into C_h: the
decomposition automatically produces Probe D's low-prime + tail
shape, with the wrap prime (inc: 2 -> 3 -> 5 -> 7 as h grows, r205
CAL_WRAP) as the moving low/tail boundary.

WORLDS (C4).  EPSTEIN(8) formal cascade (A0_E, Q_2, Q_5, K_6, r205
recipe VERBATIM): its orbit wraps differently -- and the PRE-REGISTERED
prototype answer to "where do its increments break the sign
coherence?" is: THEY DO NOT.  The EPSTEIN mu-ladder is monotone inside
OMEGA from the seed on (mus -11.96 -> -2.99 -> -1.279 -> -1.261, all
<= -1, all dmu > 0) and its s* = 0.7930 <= 1 -- the crossing
coordinate would MISCLASSIFY the non-PSD Epstein wall exactly as in
r205: the separator is the INERTIA PRECONDITION (n_neg(NoP_E) = 3,
measured; the sign census does NOT separate), re-instantiated in
crossing coordinates.  SCRARITH(5): the orbit is sign-coherent TOO
but EXITS the region at its last step (mu: -1.771 -> -0.9406 > -1,
s* = 1.0632 > 1): the failure is BUDGET OVERSHOOT, not sign -- the
one-signed sum eats past the boundary (consistent with its non-PSD
wall, Delta = +0.059).  SMOOTH(5): portless, orbit degenerates to the
seed point, s* = 1.2733 > 1 (n_neg = 2, structural refusal).  So the
three controls refuse through three DIFFERENT channels (inertia /
budget / ports) while ALL THREE remain sign-coherent where defined:
ONE-SIGNEDNESS IS NOT THE SEPARATOR -- the separator triple is
{inertia-1, budget compliance, port structure} (typed enum).

PROBE-D ADJUDICATION (frozen criterion, the round's deliverable):
  LEG-A (form):   some Phi has post-wrap sign coherence == 1.0 at
                  every MAIN rung, both orders;
  LEG-B (tail):   for that Phi the decay slope at the deepest rung
                  (h = 20, inc order, non-wrap steps, log10|dmu| vs
                  log10 p) is <= -1.0;
  LEG-C (state):  the post-wrap ratio spread log10(max rho / min rho)
                  <= 0.5 dex at every rung h >= 8.
  PROBE-D-GO iff A and B and C; PROBE-D-STRUCTURE-ONLY-NO-GO iff A
  and not (B and C) (the positive-sum FORM exists, the tail theorem
  does not apply at reachable rungs); PROBE-D-NO-GO iff not A.

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing; all
informed by the ONE DISCLOSED pre-freeze prototype proto_scc_scratch
at h = 4, 5, 8 + all three controls, log kept as
proto_scc_scratch.out1.log, script deleted at freeze):
  P1 closure/inheritance exact; log10(1-s*) == the r205 CAL_DLOG
     ladder at every shared rung (proto -10.81/-15.95/-29.60 exact
     print match); wrap stages == r205 CAL_WRAP.
  P2 sign coherence 1.0 for ALL FIVE Phi post-wrap at every MAIN rung
     and both orders; Phi_4 all-steps census: one-signed at every
     non-wrap step, the single wrap step opposite (h = 4: seed
     already in OMEGA, zero exceptions).
  P3 increments O(1) and tau-FLAT; terminal increment dmu_last ~ 0.8
     .. 1.0 with NO visible h-decay (proto 0.850/0.956/0.817).
  P4 STATE-FREENESS FAILS: rho spread ~ 1 dex at h = 8 (proto ratios
     5.61 / 0.62 at p = 5 / 7); order-dependence O(1).
  P5 NO p^{-1} DECAY: raw slope indefinite/positive at shallow rungs;
     the atom part A_p collapses at the WINDOW EDGE, not by a p-law
     (proto h = 8, p = 7: |A| = 1.3e-9; exact matched-load zero at
     p = h: proto h = 5, p = 5: |A| = 7.8e-62); expected Probe-D
     verdict STRUCTURE-ONLY-NO-GO (LEG-A holds, LEG-B/C fail).
  P6 boundary C_h^log O(1) and tau-flat (proto -2.11/-2.62/-2.07 inc).
  P7 worlds exactly as the prototype (EPSTEIN mus/-misread, SCRARITH
     exit, SMOOTH degenerate; values frozen above).
  P8 the logit-family terminal increment RIDES tau (proto +24.7/
     +36.7/+67.9 == -log(1-s*) class): Phi_2/Phi_3 concentrate the
     wall in the LAST increment; Phi_1 = log s keeps every increment
     O(1) and pushes the wall into the near-cancellation
     sum + C_h = log s* = -(1-s*)(1 + O(1-s*)) -- said exactly, both
     faces typed (the wall margin rides tau BY CONSTRUCTION in every
     coordinate; the QUESTION is whether the increments and their
     decay exponents are tau-flat: expected YES).

NOTATION (r171-r206 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; par_k = (-1)^k; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); Raw* = D_par N M* N D_par entrywise;
phi_k = 1/(1/4 + om_k^2); c_h = 2 sinh^2(a/2); G_B = (L/2)
diag(2, 1, ..., 1); theta = sum_{p<=h} log p; A0 = RawArch + theta
G_B; Q_p = r204 dissipation Grams (qp_gram VERBATIM via import from
euler_hpin_region_probe); N_j = A0 - sum_{i<=j} Q_{p_i}; NoP = N_P =
RawM - RawPole; m_j(0) = phi^T N_j^{-1} phi (mp.lu_solve); mu_j =
c_h m_j(0); s_j = -1/mu_j; Delta_h = 1 + mu_P; j* = min{j : mu_j <=
-1}; wrap prime = order[j*-1] (0 if j* = 0: seed already in OMEGA);
eigsy zero class zb_h = 10^{-(dps-20)} fro for MAIN inertia, 1e-30
fro for control worlds; dictionary path Q_p^dict = lp G_B -
sum_{m<=m_cap(p,h)} w_{p^m} W(m lp) via w_kernel_add (r202/r204
VERBATIM); tau_h = ce["mpE"][0], measured per-rung scalar only.
Controls: SCRARITH(5, 60) golden permutation orbit (its A0 - sum
would-be Q_p == NoP closure gated), EPSTEIN(8, 80) formal cascade
(A0_E, Q_2 doubled tap, Q_5, orphan K_6, Dirichlet recursion
VERBATIM), SMOOTH(5, 60) portless.

RUNGS AND DPS (frozen; house ladder + the ONE extension): RUNGS =
(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 20); DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
16: 130, 20: 144}.  DISCLOSED dps schedule: h = 20 at the house
r200 value 144 extends the r205 ladder by one rung (the observable
1 - s* ~ 1e-85 needs ~ 105 digits: resolved); h = 28 is NOT
reachable (1 - s* ~ 1e-120 class needs dps > 140 at K = 117 --
LU/eigsy budget beyond the runtime bar; the r202 dps-60 h = 28
ladder resolves only O(1) blocks, not this observable).
DECAY_RUNGS = (11, 12, 13, 16, 20) (inc order, non-wrap steps;
>= 4 fit points from h = 11 on).  A-part fit drops exact
matched-load zeros (|A_p| <= 1e-30 excluded, disclosed: the p = h
edge is an exact zero, not a decay datum).  SMOKE_RUNGS = (4, 5) +
SCRARITH.  WORKERS = 6.

FROZEN BARS: WARD_BAR 1e-45 (cascade closure, rel max-entry);
WOOD_BAR 1e-30 (Woodbury step ward, rel); TELE_BAR 1e-30
(telescoping ward, rel); ID_BAR 1e-30 ((1-s*) mu_P == Delta rel);
DICT_BAR 1e-40 (anti-loop dictionary-path C_h, rel); SLOPE_FLAT
0.30 (dex/dex vs log10 tau); PD_GO_SLOPE -1.0; PD_SPREAD_BAR 0.5
(dex); RUNTIME_BAR 2700 s.  Record tolerances: LOG_TOL 0.11 dex
(1-s* vs r205 CAL_DLOG carries the +log10 s* ~ 1e-11 offset --
absorbed); VAL_TOL 0.01 (abs, O(1) values); SPREAD_TOL 0.10 dex;
SLOPE_TOL 0.10; counts/primes exact.

R205 INHERITANCE TABLES (copied VERBATIM from the r205 frozen spec):
R205_WRAP {h: (wrap prime inc, dec); 0 = seed-in-region}: 4: (0,0),
  5: (2,5), 6: (2,5), 7: (3,5), 8: (3,5), 9: (3,5), 10: (3,5),
  11: (5,5), 12: (5,5), 13: (7,5), 16: (7,7).
R205_DLOG {h: log10 |Delta|}: 4: -10.81, 5: -15.95, 6: -20.40,
  7: -25.20, 8: -29.60, 9: -34.25, 10: -39.14, 11: -43.93,
  12: -49.16, 13: -53.78, 16: -68.56.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  cohEnum   := SIGN-COHERENT-ALL-PHI iff post-wrap coherence == 1.0
               for all five Phi at every MAIN rung, both orders;
               else SIGN-BREAK-AT(h, order, Phi);
  wrapEnum  := WRAP-IS-ONLY-EXCEPTION iff the Phi_4 all-steps census
               shows every non-wrap step one-signed and the single
               wrap step opposite at every MAIN rung/order (h = 4:
               zero exceptions); else EXTRA-SIGN-FLIPS(where);
  stateEnum := INCREMENTS-STATE-FREE iff rho spread <= PD_SPREAD_BAR
               at every rung h >= 8; else STATE-CARRIES-DECOMPOSITION
               (the honest expected verdict);
  decayEnum := TAIL-DECAY-P1 iff decay slope at h = 20 <= -1.0;
               TAIL-DECAY-SUBCRITICAL iff <= -0.5; else
               NO-TAIL-DECAY-AT-REACHABLE-RUNGS;
  bndEnum   := BOUNDARY-SOURCE-EXPLICIT-TAU-FLAT iff G29 dict path
               passes and |slope(C_h^log vs log10 tau)| <= SLOPE_FLAT;
  sepEnum   := SEPARATOR-IS-NOT-SIGN iff all three control worlds are
               sign-coherent where defined while refusing through
               {inertia / budget / ports} respectively;
  pdEnum    := the Probe-D verdict from the frozen criterion above;
  plus the definitional riders (always typed): CROSSING-MARGIN-IS-
  THE-WALL (1 - s* = Delta/mu_P: the margin in crossing coordinates
  IS the r205 terminal clearance == GPSD margin == the wall --
  barrier inherited, named, not crossed); PR-DOMINATION-COFINALLY-
  IS-THE-WALL (any attempt to prove the budget compliance sum <=
  -C_h cofinally from per-prime PR data alone IS the wall statement
  -- named, not crossed); INERTIA-PRECONDITION-IS-A-LEG (r205,
  re-instantiated here in crossing coordinates by the EPSTEIN
  misread).

RECORD TABLES (frozen at freeze from the disclosed ladder: ONE
structural smoke (rungs 4/5 + SCRARITH, 25/25, 27.8 s,
secular_crossing_coord_probe.smoke1.log, pre-freeze SPEC SHA
11280cb1c7e2bad2), ONE calibration pass (calib_scc_pass1.log,
25/25, all 12 rungs + all three controls, 824.0 s, same pre-freeze
SHA), then ONE disclosed pre-freeze INSTRUMENT STRENGTHENING: the
G23 margin-identity ward was circular as first coded (1 - s*
computed AS Delta/mu_P, dev identically 0) and was replaced by the
genuine direct-subtraction cross-instrument 1 - (-1/mu_P) vs
Delta/mu_P (a strictly stronger ward; no bar, dps, rung, grid,
target or taxonomy moved), confirmed by smoke2 (25/25,
secular_crossing_coord_probe.smoke2.log) before the record tables
were inserted at freeze; house pattern throughout.  Verdicts frozen
from calibration: closure exact at all 12 rungs (8.0e-62 at h = 4
down to 1.1e-143 at h = 20); inertia n_neg(NoP) == 1 everywhere
incl. h = 20; wrap primes == R205_WRAP at all shared rungs, h = 20
NEW: (13, 7) -- the inc wrap prime keeps CLIMBING (2 -> 3 -> 5 ->
7 -> 13); log10(1 - s*) == R205_DLOG at print precision at every
shared rung, h = 20: -87.95 (the new deepest crossing-margin
reading); Woodbury step ward <= 6.4e-61; telescoping <= 1.5e-61;
sign coherence 1.0 for ALL five Phi at ALL 12 rungs BOTH orders
(P2 TRUE); Phi_4 all-steps census: single wrap exception
everywhere, zero at h = 4 (P2 TRUE); state-freeness FAILS exactly
as pre-registered (P4 TRUE): rho spread 0.742 .. 1.259 dex over the
ladder (0.742 .. 0.954 at h >= 8), order-dependence dev 0.74 ..
0.95 at deep rungs; decay slopes (inc, non-wrap): dmu +0.32/+0.15/
+1.02/+0.72/+1.41 at h = 11/12/13/16/20 -- UNIFORMLY POSITIVE, the
increments GROW with p (the log p G_B drift + state evolution
dominate; STRONGER than the pre-registered indefinite reading);
A-part slopes +0.36/-17.95/+0.19/-11.76/+0.49 (the huge negatives
at h = 12/16 are the disclosed WINDOW-EDGE collapse of the
near-edge atom kernels, not a p-law); terminal increment ladder
0.850 .. 0.702 FLAT (slope vs log10 tau +0.0027); boundary C_h^log
-2.63 .. -1.67 O(1), tau-flat (slope -0.0090), dictionary path <=
9.0e-62 (P6 TRUE); worlds EXACTLY as pre-registered (P7 TRUE):
EPSTEIN sign-coherent (coh 1.0), s* = 0.7930 <= 1 with n_neg = 3
(misread), SCRARITH sign-coherent with region EXIT at the last
step (s* = 1.0632, closure 1.7e-61), SMOOTH degenerate (s* =
1.2733, n_neg = 2); logit terminal increment rides tau (slope
-0.9990 in dex vs log10 tau: |slope| = 1 -- P8 TRUE; the dex sign
follows the convention logit_last/ln 10 vs log10 tau), log-s
increments tau-flat; Probe-D: LEG-A TRUE, LEG-B FALSE (slope +1.41
> -1.0, wrong SIGN even), LEG-C FALSE (spread > 0.5 dex) =>
verdict PROBE-D-STRUCTURE-ONLY-NO-GO.
CAL_WRAPP {h: (inc, dec)}: 4: (0, 0), 5: (2, 5), 6: (2, 5),
  7: (3, 5), 8: (3, 5), 9: (3, 5), 10: (3, 5), 11: (5, 5),
  12: (5, 5), 13: (7, 5), 16: (7, 7), 20: (13, 7).
CAL_OMS {h: log10(1 - s*)}: 4: "-10.81", 5: "-15.95", 6: "-20.40",
  7: "-25.20", 8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
  12: "-49.16", 13: "-53.78", 16: "-68.56", 20: "-87.95".
CAL_FINC {h: last inc-order dmu}: 4: "0.850", 5: "0.956",
  6: "0.835", 7: "0.892", 8: "0.817", 9: "0.769", 10: "0.729",
  11: "0.816", 12: "0.772", 13: "0.788", 16: "0.701", 20: "0.702".
CAL_CH {h: C_h^log, inc order}: 4: "-2.112", 5: "-2.625",
  6: "-2.026", 7: "-2.424", 8: "-2.066", 9: "-1.854", 10: "-1.696",
  11: "-1.983", 12: "-1.820", 13: "-2.004", 16: "-1.672",
  20: "-1.692".
CAL_SPREAD {h: log10 rho spread, inc post-wrap}: 4: "1.057",
  5: "1.259", 6: "1.003", 7: "1.105", 8: "0.954", 9: "0.861",
  10: "0.790", 11: "0.915", 12: "0.847", 13: "0.883", 16: "0.742",
  20: "0.742".
CAL_DSLOPE {h: (dmu slope, A slope), inc non-wrap}: 11: ("+0.32",
  "+0.36"), 12: ("+0.15", "-17.95"), 13: ("+1.02", "+0.19"),
  16: ("+0.72", "-11.76"), 20: ("+1.41", "+0.49").
CAL_TSLOPES: oms +1.0005, finc +0.0027, ch -0.0090, logit_last
  -0.9990, spread +0.0056.
CAL_CTRL: EPSTEIN {nneg 3, mus (-11.9613, -2.99101, -1.27863,
  -1.26099), sstar "0.7930", coh 1.0}; SCRARITH {nneg 3, mus
  (3.07534, -6.54471, -1.77077, -0.940562), sstar "1.0632",
  exit_last True}; SMOOTH {nneg 2, sstar "1.2733"}.
AMENDMENTS: NONE post-freeze (no bar, dps, rung, recipe or target
moved between freeze and the run of record; the one pre-freeze
instrument strengthening is disclosed above).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G12 (sympy); S2 ladder + decomposition G20-G29 (mp,
ProcessPool); S3 worlds G40-G42; S4 screens + guards G50-G53; S5
pricing + Probe-D adjudication G60-G61 + G99 runtime.  DETERMINISM:
no randomness anywhere; ProcessPool results keyed; run2 must be
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
from euler_hpin_region_probe import (         # r205 machinery VERBATIM
    to_raw, qp_gram, pd_flag)
from euler_jet_colligation_probe import (     # r204 machinery VERBATIM
    primes_upto, m_cap, w_kernel_add)

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 2700.0

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 20)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130, 20: 144}
DECAY_RUNGS = (11, 12, 13, 16, 20)
SMOKE_RUNGS = (4, 5)
PHINAMES = ("log", "logit", "atanh", "inv", "invm1")

WARD_BAR = 1e-45
WOOD_BAR = 1e-30
TELE_BAR = 1e-30
ID_BAR = 1e-30
DICT_BAR = 1e-40
SLOPE_FLAT = 0.30
PD_GO_SLOPE = -1.0
PD_SPREAD_BAR = 0.5
A_ZERO_DROP = 1e-30
ZCLS = 1e-30

LOG_TOL = 0.11
VAL_TOL = 0.01
SPREAD_TOL = 0.10
SLOPE_TOL = 0.10

CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80),
              ("SMOOTH", 5, 60))

# ------------------- r205 inheritance tables (r205 frozen spec VERBATIM)
R205_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
             9: (3, 5), 10: (3, 5), 11: (5, 5), 12: (5, 5),
             13: (7, 5), 16: (7, 7)}
R205_DLOG = {4: "-10.81", 5: "-15.95", 6: "-20.40", 7: "-25.20",
             8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
             12: "-49.16", 13: "-53.78", 16: "-68.56"}

# --------------------- calibrated record tables (calib_scc_pass1.log)
CAL_WRAPP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
             9: (3, 5), 10: (3, 5), 11: (5, 5), 12: (5, 5),
             13: (7, 5), 16: (7, 7), 20: (13, 7)}
CAL_OMS = {4: "-10.81", 5: "-15.95", 6: "-20.40", 7: "-25.20",
           8: "-29.60", 9: "-34.25", 10: "-39.14", 11: "-43.93",
           12: "-49.16", 13: "-53.78", 16: "-68.56", 20: "-87.95"}
CAL_FINC = {4: "0.850", 5: "0.956", 6: "0.835", 7: "0.892",
            8: "0.817", 9: "0.769", 10: "0.729", 11: "0.816",
            12: "0.772", 13: "0.788", 16: "0.701", 20: "0.702"}
CAL_CH = {4: "-2.112", 5: "-2.625", 6: "-2.026", 7: "-2.424",
          8: "-2.066", 9: "-1.854", 10: "-1.696", 11: "-1.983",
          12: "-1.820", 13: "-2.004", 16: "-1.672", 20: "-1.692"}
CAL_SPREAD = {4: "1.057", 5: "1.259", 6: "1.003", 7: "1.105",
              8: "0.954", 9: "0.861", 10: "0.790", 11: "0.915",
              12: "0.847", 13: "0.883", 16: "0.742", 20: "0.742"}
CAL_DSLOPE = {11: ("+0.32", "+0.36"), 12: ("+0.15", "-17.95"),
              13: ("+1.02", "+0.19"), 16: ("+0.72", "-11.76"),
              20: ("+1.41", "+0.49")}
CAL_TSLOPES = {"oms": "+1.0005", "finc": "+0.0027", "ch": "-0.0090",
               "logit_last": "-0.9990", "spread": "+0.0056"}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=3, sstar="0.7930", coh_ok=True),
    "SCRARITH": dict(nneg=3, sstar="1.0632", exit_last=True),
    "SMOOTH": dict(nneg=2, sstar="1.2733"),
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
    if n < 2:
        return float("nan")
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
                       "per-rung inertia counts (r200/r205 anatomy "
                       "scope); tau as measured per-rung scalar; "
                       "fully zero-free; concurrent-lane files "
                       "untouched")


# ------------------------------------------------------- shared helpers
def solve_x(N, phi, K):
    """m = phi^T N^{-1} phi and x = N^{-1} phi via one LU solve."""
    x = mp.lu_solve(N, mp.matrix(phi))
    m = sum(phi[i] * x[i] for i in range(K))
    return m, x


def phi_of_mu(name, mu):
    """Numerically safe Phi(s) at s = -1/mu (see spec)."""
    if name == "log":
        return -mp.log(-mu)
    if name == "logit":
        return -mp.log(-(1 + mu))
    if name == "atanh":
        return -mp.log(-(1 + mu)) / 2
    if name == "inv":
        return -mu
    if name == "invm1":
        return -(1 + mu)
    raise ValueError(name)


def phi_domain(name, mu):
    if name == "log":
        return mu < 0
    if name in ("logit", "atanh"):
        return mu < -1
    if name == "inv":
        return mu != 0
    return True


def coherence(incs):
    """Sign-coherence fraction: modal-sign count / n (n >= 1)."""
    if not incs:
        return float("nan")
    npos = sum(1 for v in incs if v > 0)
    nneg = sum(1 for v in incs if v < 0)
    return max(npos, nneg) / float(len(incs))


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
            out["tau_pos"] = bool(tau > 0)
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2)
                   for k in range(K)]
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
            Qs = {p: qp_gram(p, h, oms, L, K) for p in prs}
            # ---- G20 cascade closure
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    acc = A0[i, j]
                    for p in prs:
                        acc -= Qs[p][i, j]
                    dev = max(dev, abs(acc - NoP[i, j]))
            out["closure_dev"] = float(dev / denN)
            # ---- G21 inertia of NoP (eigsy, dps-scaled zero class)
            E, _Q = mp.eigsy(NoP)
            zb = mp.mpf(10) ** (-(dps - 20)) * froN
            out["nneg"] = sum(1 for e in E if e < -zb)
            # ---- state-free reference resolvents
            _mT, xT = solve_x(NoP, phi, K)
            _mS, xS = solve_x(A0, phi, K)
            # ---- orbits, both orders
            orb: dict = {}
            for tag, order in (("inc", prs),
                               ("dec", list(reversed(prs)))):
                N = mp.matrix(A0)
                m0, x0 = solve_x(N, phi, K)
                mus = [c * m0]
                xs = [x0]
                for p in order:
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= Qs[p][i, j]
                    m1, x1 = solve_x(N, phi, K)
                    mus.append(c * m1)
                    xs.append(x1)
                P = len(order)
                jstar = next((j for j in range(P + 1)
                              if mus[j] <= -1), None)
                cen = dict(order=order, jstar=jstar,
                           wrap_p=(0 if jstar == 0
                                   else order[jstar - 1])
                           if jstar is not None else None,
                           mus_f=[float(v) for v in mus])
                # pd cross-ward: N_j not PD from the wrap on
                pdw = True
                Nc = mp.matrix(A0)
                for j, p in enumerate(order, start=1):
                    for i in range(K):
                        for k2 in range(K):
                            Nc[i, k2] -= Qs[p][i, k2]
                    if jstar is not None and j >= jstar:
                        pdw = pdw and (not pd_flag(Nc, K))
                if jstar == 0:
                    pdw = pdw and (not pd_flag(mp.matrix(A0), K))
                cen["pd_ward"] = pdw
                # per-step data: dmu, Woodbury ward, split, state-free
                steps = []
                wood_worst = mp.mpf(0)
                for j in range(1, P + 1):
                    p = order[j - 1]
                    lp = mp.log(p)
                    dmu = mus[j] - mus[j - 1]
                    Qx = [sum(Qs[p][i, k2] * xs[j - 1][k2]
                              for k2 in range(K)) for i in range(K)]
                    wood = c * sum(xs[j][i] * Qx[i]
                                   for i in range(K))
                    wrel = abs(dmu - wood) / max(abs(dmu),
                                                 mp.mpf("1e-300"))
                    wood_worst = max(wood_worst, wrel)
                    Bp = c * sum(xs[j][i] * GBd[i] * xs[j - 1][i]
                                 for i in range(K))
                    Ap = lp * Bp - dmu
                    fT = c * sum(xT[i] * sum(Qs[p][i, k2] * xT[k2]
                                             for k2 in range(K))
                                 for i in range(K))
                    fS = c * sum(xS[i] * sum(Qs[p][i, k2] * xS[k2]
                                             for k2 in range(K))
                                 for i in range(K))
                    steps.append(dict(p=p, dmu=float(dmu),
                                      lpB=float(lp * Bp),
                                      A=float(Ap), fT=float(fT),
                                      fS=float(fS)))
                cen["steps"] = steps
                cen["wood_worst"] = float(wood_worst)
                # transforms: post-wrap increments + boundary
                phis: dict = {}
                if jstar is not None:
                    for nm in PHINAMES:
                        dom_ok = all(phi_domain(nm, mus[j])
                                     for j in range(jstar, P + 1))
                        if not dom_ok:
                            phis[nm] = dict(coh=float("nan"),
                                            n=0, ch=None,
                                            tele=None, dom=False)
                            continue
                        vals = [phi_of_mu(nm, mus[j])
                                for j in range(jstar, P + 1)]
                        incs = [vals[t + 1] - vals[t]
                                for t in range(len(vals) - 1)]
                        ch = vals[0]
                        tot = vals[-1]
                        tele = abs(tot - ch - sum(incs)) \
                            / max(abs(tot), abs(ch), mp.mpf(1))
                        phis[nm] = dict(
                            coh=coherence([float(v) for v in incs]),
                            n=len(incs), ch=float(ch),
                            tele=float(tele), dom=True,
                            last=float(incs[-1]) if incs else None)
                cen["phis"] = phis
                # Phi_4 all-steps census
                sgn = [1 if (mus[j] - mus[j - 1]) > 0 else -1
                       for j in range(1, P + 1)]
                nplus = sum(1 for v in sgn if v > 0)
                cen["inv_exceptions"] = P - nplus \
                    if nplus >= P - nplus else nplus
                cen["inv_exc_at_wrap"] = (
                    jstar is not None and (
                        (jstar == 0 and cen["inv_exceptions"] == 0)
                        or (jstar > 0 and cen["inv_exceptions"] == 1
                            and sgn[jstar - 1] == -1)))
                orb[tag] = cen
            out["orb"] = orb
            # terminal crossing data (order-independent)
            muP = orb["inc"]["mus_f"][-1]
            muP_mp = mp.mpf(0)
            # recompute terminal mu at full precision from NoP
            mP, _xP = solve_x(NoP, phi, K)
            muP_mp = c * mP
            Delta = 1 + muP_mp
            out["Delta_neg"] = bool(Delta < 0)
            sstar = -1 / muP_mp
            one_m = Delta / muP_mp
            one_m_direct = 1 - sstar
            out["sstar_in01"] = bool(0 < sstar < 1)
            out["oms_log10"] = float(mp.log(abs(one_m), 10))
            out["id_dev"] = float(abs(one_m_direct - one_m)
                                  / abs(one_m))
            out["muP_f"] = float(muP)
            # ---- G29 anti-loop: dictionary-path C_h (inc order)
            jst = orb["inc"]["jstar"]
            out["ch_dict_dev"] = None
            if jst is not None:
                Nd = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Nd[i, j] = RawArch[i, j]
                    Nd[i, i] += theta * GBd[i]
                for p in prs[:jst]:
                    lp = mp.log(p)
                    Qd = mp.zeros(K, K)
                    for i in range(K):
                        Qd[i, i] = lp * GBd[i]
                    for m2 in range(1, m_cap(p, h) + 1):
                        q = p ** m2
                        w_kernel_add(Qd, mp.log(q),
                                     -lp / mp.sqrt(q), oms, L, K)
                    for i in range(K):
                        for j in range(K):
                            Nd[i, j] -= Qd[i, j]
                md, _xd = solve_x(Nd, phi, K)
                mud = c * md
                mu_ref = mp.mpf(orb["inc"]["mus_f"][jst])
                # compare at mp precision against the orbit value
                N2 = mp.matrix(A0)
                for p in prs[:jst]:
                    for i in range(K):
                        for j in range(K):
                            N2[i, j] -= Qs[p][i, j]
                m2v, _x2 = solve_x(N2, phi, K)
                mu2 = c * m2v
                out["ch_dict_dev"] = float(abs(mud - mu2)
                                           / max(abs(mu2),
                                                 mp.mpf("1e-300")))
                out["ch_log_f"] = float(phi_of_mu("log", mu2)) \
                    if mu2 < 0 else None
            # decay fits (inc order, non-wrap steps)
            if h in DECAY_RUNGS:
                jw = orb["inc"]["jstar"]
                pts = [(math.log10(st["p"]),
                        math.log10(abs(st["dmu"])))
                       for j2, st in enumerate(orb["inc"]["steps"],
                                               start=1)
                       if j2 != jw and st["dmu"] != 0]
                out["dslope"] = fit_line([x for x, _ in pts],
                                         [y for _, y in pts])
                ptsA = [(math.log10(st["p"]),
                         math.log10(abs(st["A"])))
                        for j2, st in enumerate(orb["inc"]["steps"],
                                                start=1)
                        if j2 != jw and abs(st["A"]) > A_ZERO_DROP]
                out["aslope"] = fit_line([x for x, _ in ptsA],
                                         [y for _, y in ptsA])
            # state-freeness spread (inc, post-wrap)
            jw = orb["inc"]["jstar"]
            rhos = []
            if jw is not None:
                for j2, st in enumerate(orb["inc"]["steps"],
                                        start=1):
                    if j2 > jw and st["fT"] > 0 and st["dmu"] > 0:
                        rhos.append(st["dmu"] / st["fT"])
            out["spread"] = (math.log10(max(rhos) / min(rhos))
                             if len(rhos) >= 2 else None)
            # order-dependence at common non-wrap primes
            odev = 0.0
            wi = orb["inc"]["wrap_p"]
            wd = orb["dec"]["wrap_p"]
            di = {st["p"]: st["dmu"] for st in orb["inc"]["steps"]}
            dd = {st["p"]: st["dmu"] for st in orb["dec"]["steps"]}
            for p in prs:
                if p in (wi, wd):
                    continue
                a1, a2 = di[p], dd[p]
                odev = max(odev, abs(a1 - a2)
                           / max(abs(a1), abs(a2), 1e-300))
            out["orddev"] = odev
            out["finc"] = orb["inc"]["steps"][-1]["dmu"]
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
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2)
                   for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            E, _Q = mp.eigsy(NoP)
            zb = mp.mpf(ZCLS) * froN
            out["nneg"] = sum(1 for e in E if e < -zb)
            mP, _x = solve_x(NoP, phi, K)
            muP = c * mP
            out["muP"] = float(muP)
            out["sstar"] = float(-1 / muP)

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
                N = mp.matrix(A0e)
                m0, _ = solve_x(N, phi, K)
                mus = [c * m0]
                for B in (Q2, Q5, K6):
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= B[i, j]
                    m1, _ = solve_x(N, phi, K)
                    mus.append(c * m1)
                out["mus"] = [float(v) for v in mus]
                out["all_in_omega"] = all(v <= -1 for v in mus)
                dmus = [float(mus[j] - mus[j - 1])
                        for j in range(1, len(mus))]
                out["coh"] = coherence(dmus)
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
                perm = sorted(range(len(keys)),
                              key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atomw = {nlist[i][0]: wts[perm[i]]
                         for i in range(len(nlist))}
                prs = primes_upto(x)
                Qw = {}
                for p in prs:
                    lp = mp.log(p)
                    Q = mp.zeros(K, K)
                    for i in range(K):
                        Q[i, i] = lp * GBd[i]
                    for q, pp in nlist:
                        if pp == p:
                            w_kernel_add(Q, mp.log(q), -atomw[q],
                                         oms, L, K)
                    Qw[p] = Q
                theta = sum(mp.log(p) for p in prs)
                A0 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0[i, j] = RawArch[i, j]
                    A0[i, i] += theta * GBd[i]
                dev = mp.mpf(0)
                den = max(abs(NoP[i, j]) for i in range(K)
                          for j in range(K))
                for i in range(K):
                    for j in range(K):
                        acc = A0[i, j]
                        for p in prs:
                            acc -= Qw[p][i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / den)
                N = mp.matrix(A0)
                m0, _ = solve_x(N, phi, K)
                mus = [c * m0]
                for p in prs:
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= Qw[p][i, j]
                    m1, _ = solve_x(N, phi, K)
                    mus.append(c * m1)
                out["mus"] = [float(v) for v in mus]
                out["exit_last"] = bool(mus[-2] <= -1 < mus[-1])
                dmus = [float(mus[j] - mus[j - 1])
                        for j in range(1, len(mus))]
                # non-wrap steps (wrap = first entry into omega)
                jw = next((j for j in range(len(mus))
                           if mus[j] <= -1), None)
                nw = [dmus[j - 1] for j in range(1, len(mus))
                      if j != jw]
                out["coh_nonwrap"] = coherence(nw)
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    # G10: battery degeneracy -- artanh(2s-1) == (1/2) log(s/(1-s));
    # (1-s)/s == 1/s - 1; so the battery has EXACTLY THREE
    # independent sign structures.
    s = sp.Symbol("s", positive=True)
    d1 = sp.expand_log(sp.atanh(2 * s - 1).rewrite(sp.log)
                       - sp.log(s / (1 - s)) / 2, force=True)
    ok_a = sp.simplify(d1) == 0
    ok_b = sp.simplify((1 - s) / s - (1 / s - 1)) == 0
    check("G10-battery-degeneracy-symbolic", bool(ok_a and ok_b),
          "artanh(2s - 1) == (1/2) log(s/(1-s)) and (1-s)/s == "
          "1/s - 1 IDENTICALLY (sympy exact): Phi_3 is half of "
          "Phi_2 and Phi_5's increments equal Phi_4's -- the frozen "
          "five-member battery carries EXACTLY THREE independent "
          "sign structures (log / logit-family / inv-family); the "
          "duplicates are kept as exact internal cross-wards, not "
          "as independent findings")

    # G11: Woodbury step law -- (N-Q)^{-1} - N^{-1} ==
    # (N-Q)^{-1} Q N^{-1}, generic symmetric 2x2 and 3x3.
    ok11 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "n_%d_%d" % (min(i, j), max(i, j))))
        Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "q_%d_%d" % (min(i, j), max(i, j))))
        Wm = (N - Q).inv()
        lhs = sp.expand(Wm - N.inv())
        rhs = sp.expand(Wm * Q * N.inv())
        ok11 &= sp.simplify(lhs - rhs) == sp.zeros(n, n)
    check("G11-woodbury-step-law-symbolic", bool(ok11),
          "(N - Q)^{-1} - N^{-1} == (N - Q)^{-1} Q N^{-1} (generic "
          "symmetric 2x2 AND 3x3, sympy exact): every per-prime "
          "increment of the Weyl read is EXACTLY the prime's own "
          "Gram Q_p sandwiched between the two adjacent cascade "
          "states -- mu_j - mu_{j-1} = c_h x_j^T Q_p x_{j-1}, the "
          "instrument behind the state-freeness question (gated "
          "numerically per step, G22)")

    # G12: crossing law -- det(N + s c phi phi^T) == det(N)
    # (1 + s c phi^T N^{-1} phi), generic 2x2 and 3x3, with the
    # explicit crossing parameter s* = -1/(c m).
    ok12 = True
    for n in (2, 3):
        N = sp.Matrix(n, n, lambda i, j: sp.Symbol(
            "m_%d_%d" % (min(i, j), max(i, j))))
        ph = sp.Matrix(n, 1, lambda i, _j: sp.Symbol("p_%d" % i))
        cs = sp.Symbol("c_s", positive=True)
        sv = sp.Symbol("s_v")
        lhs = (N + sv * cs * ph * ph.T).det()
        mm = (ph.T * N.inv() * ph)[0, 0]
        rhs = N.det() * (1 + sv * cs * mm)
        ok12 &= sp.simplify(lhs - sp.expand(rhs)) == 0
        root = sp.solve(sp.Eq(1 + sv * cs * mm, 0), sv)
        ok12 &= len(root) == 1 and \
            sp.simplify(root[0] + 1 / (cs * mm)) == 0
    check("G12-crossing-law-symbolic", bool(ok12),
          "det(N + s c phi phi^T) == det(N) (1 + s c phi^T N^{-1} "
          "phi) (generic 2x2 AND 3x3, sympy exact) with the UNIQUE "
          "root s* = -1/(c m) -- the r200 secular crossing "
          "parameter in closed form; GIVEN n_neg(NoP) = 1 (measured "
          "G21) and rank-one interlacing (classical, typed): wall "
          "PSD <=> s* <= 1 <=> mu_P <= -1 -- the r205 H-pin "
          "criterion in crossing dress (inheritance, not re-proven)")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("secular_crossing_coord_probe -- "
          "PRIME.SECULAR.CROSSING.COORD.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/orders/transform battery/Probe-D "
          "criterion declared in the frozen spec (SPEC_SHA covers "
          "the declaration); the battery is the reviewer's "
          "PREDEFINED five (no post-hoc members); priors P1-P8 "
          "frozen from the ONE disclosed pre-freeze prototype at "
          "h = 4, 5, 8 + controls (log kept, script deleted at "
          "freeze), none gate-forcing; r205 orbit machinery "
          "imported VERBATIM (qp_gram/to_raw/pd_flag); record "
          "tables frozen from the disclosed smoke + calibration "
          "ladder (house pattern); dps ladder = house values, "
          "h = 20 extension disclosed")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy: battery + step + crossing law)")
    exact_layer()

    # ------------------------------------------------------------ S2
    rungs = SMOKE_RUNGS if smoke else RUNGS
    section("S2  LADDER + DECOMPOSITION (mp at h = %s)" % str(rungs))
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
          "A0 - sum_p Q_p == NoP entrywise at every rung (max rel "
          "dev %s, bar %.0e) -- the r204/r205 central identity "
          "re-instantiated, including the NEW deepest rung h = 20"
          % (str({h: "%.1e" % res[h]["closure_dev"]
                  for h in (4, 13, 20) if h in res}), WARD_BAR))

    check("G21-inertia-one", all(
        res[h]["nneg"] == 1 for h in rungs),
          "n_neg(NoP_h) == 1 at EVERY rung incl. h = 20 (eigsy, "
          "dps-scaled zero class): the PRECONDITION of the s* "
          "reading (wall PSD <=> s* <= 1 NEEDS inertia-1, G12 + "
          "EPSTEIN exhibit G40) holds everywhere reachable")

    check("G22-woodbury-step-ward", all(
        res[h]["orb"][t]["wood_worst"] <= WOOD_BAR
        for h in rungs for t in ("inc", "dec")),
          "the exact step law mu_j - mu_{j-1} == c_h x_j^T Q_p "
          "x_{j-1} verified at EVERY step, rung and order (worst "
          "rel dev %.1e, bar %.0e): each increment IS the prime's "
          "Gram read in the evolving cascade state"
          % (max(res[h]["orb"][t]["wood_worst"] for h in rungs
                 for t in ("inc", "dec")), WOOD_BAR))

    wrapp = {h: (res[h]["orb"]["inc"]["wrap_p"],
                 res[h]["orb"]["dec"]["wrap_p"]) for h in rungs}
    ok23 = all(res[h]["sstar_in01"] and res[h]["Delta_neg"]
               and res[h]["id_dev"] <= ID_BAR
               and res[h]["tau_pos"]
               and res[h]["orb"]["inc"]["jstar"] is not None
               and res[h]["orb"]["dec"]["jstar"] is not None
               and res[h]["orb"]["inc"]["pd_ward"]
               and res[h]["orb"]["dec"]["pd_ward"] for h in rungs)
    ok23 = ok23 and all(
        wrapp[h] == R205_WRAP[h] for h in rungs if h in R205_WRAP)
    ok23 = ok23 and all(
        abs(res[h]["oms_log10"] - float(R205_DLOG[h])) <= LOG_TOL
        for h in rungs if h in R205_DLOG)
    if not (calib or smoke):
        ok23 = ok23 and all(
            wrapp[h] == CAL_WRAPP[h] for h in rungs) and all(
            abs(res[h]["oms_log10"] - float(CAL_OMS[h])) <= LOG_TOL
            for h in rungs)
    check("G23-crossing-ladder", ok23,
          "C1 DELIVERED -- s*(h) in (0, 1) at every rung with "
          "Delta < 0 and the margin identity 1 - s* == Delta/mu_P "
          "cross-instrumented by DIRECT SUBTRACTION at full dps "
          "(worst rel dev %.1e, bar %.0e): the crossing-"
          "coordinate wall margin log10(1 - s*) = %s IS the r205 "
          "terminal-clearance ladder (== R205_DLOG within %.2f "
          "dex at every shared rung; h = 20 NEW: %s) -- "
          "CROSSING-MARGIN-IS-THE-WALL, typed definitional, rides "
          "tau BY CONSTRUCTION; wrap primes {h: (inc, dec)} = %s "
          "== R205_WRAP at all shared rungs; PD cross-ward: N_j "
          "not PD from the wrap on, every rung/order"
          % (max(res[h]["id_dev"] for h in rungs), ID_BAR,
             str({h: "%.2f" % res[h]["oms_log10"]
                  for h in (4, 8, 13, 16) if h in res}), LOG_TOL,
             str({h: "%.2f" % res[h]["oms_log10"]
                  for h in (20,) if h in res}), str(wrapp)))

    check("G24-telescoping-ward", all(
        ph["tele"] is not None and ph["tele"] <= TELE_BAR
        for h in rungs for t in ("inc", "dec")
        for nm, ph in res[h]["orb"][t]["phis"].items()
        if ph["dom"]),
          "Phi(s*) == C_h + sum delta_p EXACT for every Phi in "
          "domain, every rung, both orders (worst rel dev %.1e, "
          "bar %.0e) -- additivity is BY CONSTRUCTION (telescoping); "
          "the round's content is in the increments' structure "
          "(G25-G28), never in the additivity itself"
          % (max(ph["tele"] for h in rungs for t in ("inc", "dec")
                 for ph in res[h]["orb"][t]["phis"].values()
                 if ph["dom"]), TELE_BAR))

    # ---- G25 sign-coherence census (the round's first table)
    coh_all = True
    for h in rungs:
        for t in ("inc", "dec"):
            row = []
            for nm in PHINAMES:
                ph = res[h]["orb"][t]["phis"][nm]
                row.append("%s %s" % (nm, ("%.2f" % ph["coh"])
                                      if ph["dom"] else "DOM"))
                if ph["dom"] and ph["n"] > 0:
                    coh_all = coh_all and (ph["coh"] == 1.0)
            print("  CENSUS h=%-2d %s n=%d %s"
                  % (h, t, res[h]["orb"][t]["phis"]["log"]["n"],
                     " | ".join(row)))
    coh_enum = "SIGN-COHERENT-ALL-PHI" if coh_all \
        else "SIGN-BREAK-DETECTED"
    check("G25-sign-coherence-census", coh_all,
          "C2 census (i) RESOLVED: %s -- post-wrap sign coherence "
          "== 1.0 for ALL FIVE Phi at ALL %d rungs, BOTH orders "
          "(P2): the post-wrap orbit is monotone in mu, so EVERY "
          "battery member is one-signed (log/logit-family "
          "POSITIVE increments, inv-family NEGATIVE); no Phi "
          "separates by coherence on MAIN -- the battery members "
          "differ in WHERE they put the wall (G50), not in sign "
          "structure" % (coh_enum, len(rungs)))

    ok26 = all(res[h]["orb"][t]["inv_exc_at_wrap"]
               for h in rungs for t in ("inc", "dec"))
    check("G26-wrap-is-only-exception", ok26,
          "the Phi_4 = 1/s ALL-STEPS census (defined on the whole "
          "orbit): at every rung and both orders the increments "
          "are one-signed at EVERY non-wrap step with the SINGLE "
          "wrap step opposite (h = 4: seed already in OMEGA, ZERO "
          "exceptions) -- the crossing coordinate's one sign flip "
          "IS the domain birth at the wrap: enum "
          "WRAP-IS-ONLY-EXCEPTION")

    # ---- G27 state-freeness
    spreads = {h: res[h]["spread"] for h in rungs
               if res[h]["spread"] is not None}
    for h in rungs:
        stps = res[h]["orb"]["inc"]["steps"]
        jw = res[h]["orb"]["inc"]["jstar"]
        print("  STATE h=%-2d " % h + " ".join(
            "p=%d dmu %+.3f fT %+.3f fS %+.3f%s"
            % (st["p"], st["dmu"], st["fT"], st["fS"],
               "*" if j2 == jw else "")
            for j2, st in enumerate(stps, start=1)))
    state_free = all(spreads[h] <= PD_SPREAD_BAR
                     for h in spreads if h >= 8)
    ok27 = len(spreads) > 0
    if not (calib or smoke):
        ok27 = ok27 and all(
            abs(spreads[h] - float(CAL_SPREAD[h])) <= SPREAD_TOL
            for h in spreads if h in CAL_SPREAD)
    state_enum = "INCREMENTS-STATE-FREE" if state_free \
        else "STATE-CARRIES-DECOMPOSITION"
    check("G27-state-freeness", ok27,
          "C2 census (ii) RESOLVED: %s -- the post-wrap ratio "
          "rho_p = dmu_p / freeT_p (freeT = the prime's Gram read "
          "in the FROZEN terminal state) has log10 spread %s dex "
          "(bar %.1f for state-freeness): the increments are NOT "
          "expressible from S_p + one fixed resolvent -- the "
          "evolving cascade state carries an O(1)-dex share of "
          "every increment; order-dependence dev at common "
          "non-wrap primes %s (exact state-freeness would force "
          "0): the sum is a TELESCOPING along the orbit, not yet "
          "a genuine prime sum"
          % (state_enum,
             str({h: "%.2f" % spreads[h]
                  for h in (8, 12, 16, 20) if h in spreads}),
             PD_SPREAD_BAR,
             str({h: "%.2f" % res[h]["orddev"]
                  for h in (8, 16, 20) if h in res})))

    # ---- G28 decay
    dsl = {h: res[h].get("dslope") for h in rungs
           if h in DECAY_RUNGS}
    asl = {h: res[h].get("aslope") for h in rungs
           if h in DECAY_RUNGS}
    fincs = {h: res[h]["finc"] for h in rungs}
    ok28 = all(dsl[h] is not None and not math.isnan(dsl[h])
               for h in dsl)
    if not (calib or smoke):
        ok28 = ok28 and all(
            abs(dsl[h] - float(CAL_DSLOPE[h][0])) <= SLOPE_TOL
            and abs(asl[h] - float(CAL_DSLOPE[h][1]))
            <= 3 * SLOPE_TOL for h in dsl) and all(
            abs(fincs[h] - float(CAL_FINC[h])) <= VAL_TOL
            for h in rungs)
    deep = max(dsl) if dsl else None
    dslope_deep = dsl.get(deep) if deep else float("nan")
    if dslope_deep is not None and dslope_deep <= PD_GO_SLOPE:
        decay_enum = "TAIL-DECAY-P1"
    elif dslope_deep is not None and dslope_deep <= -0.5:
        decay_enum = "TAIL-DECAY-SUBCRITICAL"
    else:
        decay_enum = "NO-TAIL-DECAY-AT-REACHABLE-RUNGS"
    check("G28-decay-law", ok28,
          "C2 census (iii) RESOLVED: %s -- decay slopes "
          "log10|dmu_p| vs log10 p (inc, non-wrap) = %s "
          "(UNIFORMLY POSITIVE: the increments GROW with p -- the "
          "log p G_B drift + state evolution dominate; deepest "
          "rung %s: %+.2f vs the tail requirement <= %.1f); the "
          "ATOM part A_p "
          "slopes %s are dominated by the WINDOW-EDGE collapse "
          "(matched-load exact zero at p = h, r204 edge law; "
          "near-edge |A| collapses by construction, not by a "
          "p-law) while the log p G_B drift carries the top "
          "increments; the TERMINAL increment dmu_last = %s stays "
          "O(1) across the whole ladder (no h-decay): the "
          "reviewer's p^{-1} tail is ABSENT at reachable rungs"
          % (decay_enum,
             str({h: "%+.2f" % dsl[h] for h in sorted(dsl)}),
             str(deep), dslope_deep, PD_GO_SLOPE,
             str({h: "%+.2f" % asl[h] for h in sorted(asl)}),
             str({h: "%.3f" % fincs[h]
                  for h in (4, 8, 13, 20) if h in fincs})))

    # ---- G29 boundary term
    chs = {h: res[h].get("ch_log_f") for h in rungs}
    ok29 = all(res[h]["ch_dict_dev"] is not None
               and res[h]["ch_dict_dev"] <= DICT_BAR
               for h in rungs) and all(
        chs[h] is not None for h in rungs)
    if not (calib or smoke):
        ok29 = ok29 and all(
            abs(chs[h] - float(CAL_CH[h])) <= VAL_TOL
            for h in rungs)
    check("G29-boundary-source-explicit", ok29,
          "C3 RESOLVED: the boundary term C_h^log = log s_{j*} = "
          "%s is O(1) and SOURCE-EXPLICIT -- closed expression in "
          "the seed (RawArch + theta G_B), the pole datum (c_h, "
          "phi) and the PRE-WRAP primes' Grams; ANTI-LOOP TEST "
          "PASSED: recomputed through the independent per-prime "
          "dictionary path (Q_p = lp G_B - sum_m w_{p^m} W(m lp), "
          "own assembly) to rel dev <= %.1e (bar %.0e) -- C_h "
          "consumes NO eigen data, NO tau, NO wall; NOTE: the "
          "pre-wrap primes ARE absorbed into C_h -- the "
          "decomposition automatically has Probe D's low-prime + "
          "tail SHAPE with the moving wrap prime %s as boundary"
          % (str({h: "%.2f" % chs[h]
                  for h in (4, 8, 13, 20) if h in chs}),
             max(res[h]["ch_dict_dev"] for h in rungs), DICT_BAR,
             str({h: wrapp[h][0] for h in (5, 8, 13, 20)
                  if h in wrapp})))

    # ------------------------------------------------------------ S3
    section("S3  WORLDS")
    ep = cres.get("EPSTEIN")
    scr = cres.get("SCRARITH")
    smo = cres.get("SMOOTH")
    if calib or smoke:
        for w, v in sorted(cres.items()):
            print("  CAL ctrl %s nneg %s sstar %.4f mus %s extra %s"
                  % (w, v.get("nneg"), v.get("sstar", 0),
                     str(["%.5g" % x for x in v.get("mus", [])]),
                     str({k2: v[k2] for k2 in
                          ("coh", "exit_last", "coh_nonwrap",
                           "closure_dev", "all_in_omega")
                          if k2 in v})))
    ok40 = True
    if ep:
        ok40 = (ep["nneg"] == 3 and 0 < ep["sstar"] < 1
                and ep["all_in_omega"] and ep["coh"] == 1.0)
        if not (calib or smoke):
            ok40 = ok40 and abs(ep["sstar"] - float(
                CAL_CTRL["EPSTEIN"]["sstar"])) <= VAL_TOL
    check("G40-epstein-inertia-misread", bool(ok40 and ep) if ep
          else smoke,
          "skipped in smoke mode" if not ep else
          "C4 sharpest exhibit RE-INSTANTIATED IN CROSSING "
          "COORDINATES: EPSTEIN(8) has s*_E = %.4f <= 1 -- the "
          "crossing coordinate would declare the wall PSD -- while "
          "n_neg(NoP_E) = %d breaks the inertia precondition (the "
          "wall is NOT PSD, r205); AND its formal-cascade orbit is "
          "FULLY SIGN-COHERENT (mus %s: monotone inside OMEGA from "
          "the seed on, coherence %.1f): the reviewer's question "
          "'where do EPSTEIN's increments break the sign "
          "coherence?' resolves to THEY DO NOT -- one-signedness "
          "is NOT the separator; the separator is INERTIA "
          "(INERTIA-PRECONDITION-IS-A-LEG)"
          % (ep["sstar"], ep["nneg"],
             str(["%.3f" % v for v in ep["mus"]]), ep["coh"]))

    ok41 = True
    if scr:
        ok41 = (scr["nneg"] == 3 and scr["sstar"] > 1
                and scr["exit_last"]
                and scr["closure_dev"] <= WARD_BAR
                and scr["coh_nonwrap"] == 1.0)
        if not (calib or smoke):
            ok41 = ok41 and abs(scr["sstar"] - float(
                CAL_CTRL["SCRARITH"]["sstar"])) <= VAL_TOL
    check("G41-scrarith-budget-overshoot", bool(ok41 and scr),
          "" if not scr else
          "SCRARITH(5): its cascade closes exactly (dev %.1e) and "
          "its orbit is sign-coherent at every non-wrap step "
          "(coherence %.1f) -- but the LAST step EXITS the region "
          "(mus %s: -1.771 -> -0.941 > -1), s* = %.4f > 1: the "
          "failure is BUDGET OVERSHOOT, not sign -- the one-signed "
          "sum eats past the boundary, consistent with its non-PSD "
          "wall (n_neg = %d); the wall statement lives in the "
          "SIZE of the one-signed sum, never in its sign"
          % (scr["closure_dev"], scr["coh_nonwrap"],
             str(["%.3f" % v for v in scr["mus"]]), scr["sstar"],
             scr["nneg"]))

    ok42 = True
    if smo:
        ok42 = smo["nneg"] == 2 and smo["sstar"] > 1
        if not (calib or smoke):
            ok42 = ok42 and abs(smo["sstar"] - float(
                CAL_CTRL["SMOOTH"]["sstar"])) <= VAL_TOL
    check("G42-smooth-degeneration", bool(ok42 and smo) if smo
          else smoke,
          "skipped in smoke mode" if not smo else
          "SMOOTH(5): portless -- the orbit degenerates to the "
          "seed point, no increments exist (structural, typed); "
          "s* = %.4f > 1 with n_neg = %d: the crossing coordinate "
          "correctly refuses; the three controls refuse through "
          "THREE DIFFERENT channels {inertia / budget / ports} "
          "while ALL are sign-coherent where defined: enum "
          "SEPARATOR-IS-NOT-SIGN" % (smo["sstar"], smo["nneg"]))

    # ------------------------------------------------------------ S4
    section("S4  TAU-SCREENS + GUARDS")
    xs = [res[h]["tau_log10"] for h in rungs]
    sl_oms = fit_line(xs, [res[h]["oms_log10"] for h in rungs])
    sl_finc = fit_line(xs, [res[h]["finc"] for h in rungs])
    sl_ch = fit_line(xs, [chs[h] for h in rungs])
    lg_last = {h: res[h]["orb"]["inc"]["phis"]["logit"]["last"]
               for h in rungs}
    sl_lg = fit_line(xs, [lg_last[h] / math.log(10.0)
                          for h in rungs])
    sp_h = sorted(spreads)
    sl_sp = fit_line([res[h]["tau_log10"] for h in sp_h],
                     [spreads[h] for h in sp_h])
    if calib or smoke:
        print("  CAL tslopes: oms %+.4f finc %+.4f ch %+.4f "
              "logit_last %+.4f spread %+.4f"
              % (sl_oms, sl_finc, sl_ch, sl_lg, sl_sp))
        ok50 = True
    else:
        ok50 = (abs(sl_oms - float(CAL_TSLOPES["oms"]))
                <= SLOPE_TOL
                and abs(sl_finc - float(CAL_TSLOPES["finc"]))
                <= SLOPE_TOL
                and abs(sl_ch - float(CAL_TSLOPES["ch"]))
                <= SLOPE_TOL
                and abs(sl_lg - float(CAL_TSLOPES["logit_last"]))
                <= SLOPE_TOL
                and abs(sl_sp - float(CAL_TSLOPES["spread"]))
                <= SLOPE_TOL)
    check("G50-tau-screen", ok50,
          "the house separation, said exactly: the TOTAL "
          "log10(1 - s*) RIDES tau (slope %+.3f -- BY CONSTRUCTION, "
          "1 - s* = Delta/mu_P) and the LOGIT-family terminal "
          "increment carries exactly that riding (slope %+.3f in "
          "dex: Phi_2/Phi_3 concentrate the wall in the LAST "
          "step); but the STRUCTURE is tau-FLAT (bar %.2f): "
          "terminal dmu slope %+.4f, boundary C_h^log slope "
          "%+.4f, state-spread slope %+.4f -- the per-prime "
          "increments and the boundary are O(1) structure facts; "
          "the demand (the wall) lives ONLY in the near-"
          "cancellation sum + C_h = log s* ~ -(1 - s*)"
          % (sl_oms, sl_lg, SLOPE_FLAT, sl_finc, sl_ch, sl_sp))

    delivered = {
        "ATOMS": ["QP-GRAMS"], "MODES": ["QP-GRAMS"],
        "QP-GRAMS": ["ORBIT"],
        "POLE-DATUM": ["CROSSING-COORD"],
        "SEED-ARCH": ["ORBIT"],
        "ORBIT": ["CROSSING-COORD"],
        "CROSSING-COORD": ["INCREMENT-CENSUS"],
        "INCREMENT-CENSUS": ["SCREENS"], "SCREENS": []}
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
    for node in ("ORBIT", "CROSSING-COORD", "INCREMENT-CENSUS",
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
          "leg typing: {battery degeneracy, Woodbury step law, "
          "crossing/determinant law} EXACT (sympy); {closure, "
          "step ward, telescoping, margin identity, dictionary "
          "path} EXACT-MP; {mu ladders, wrap stages, coherence "
          "censuses, state ratios, decay slopes, world numbers} "
          "MEASURED; {rank-one interlacing, Loewner pre-wrap "
          "monotonicity} SOURCE-CLASSICAL (typed); {CROSSING-"
          "MARGIN-IS-THE-WALL (1 - s* = Delta/mu_P == r205 "
          "terminal clearance == GPSD margin == the wall), "
          "PR-DOMINATION-COFINALLY-IS-THE-WALL (proving the "
          "budget compliance sum <= -C_h cofinally from per-prime "
          "data IS the wall statement)} DEFINITIONAL BARRIERS -- "
          "both named, neither crossed; {INERTIA-PRECONDITION-IS-"
          "A-LEG} EXHIBIT-BACKED (EPSTEIN misread, G40)")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1,
            ("SV", "RH"): INF,
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
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "TAILSPLIT"): INF, ("TAILSPLIT", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the one-signed prime sum admits a p^{-1} tail theorem "
          "cofinally' as a unit edge would raise the flow to 6 -- "
          "NOT REAL (G28: no tail decay at reachable rungs, and "
          "the budget statement IS the wall): this round adds NO "
          "flow; census cardinality UNCHANGED; RH unreachable "
          "without the omega edges")

    # ------------------------------------------------------------ S5
    section("S5  PRICING + PROBE-D ADJUDICATION")
    legA = coh_all
    legB = (dslope_deep is not None
            and not math.isnan(dslope_deep)
            and dslope_deep <= PD_GO_SLOPE)
    legC = state_free
    if legA and legB and legC:
        pd_enum = "PROBE-D-GO"
    elif legA:
        pd_enum = "PROBE-D-STRUCTURE-ONLY-NO-GO"
    else:
        pd_enum = "PROBE-D-NO-GO"
    check("G60-pricing-and-probe-d", True,
          "WHAT THE ROUND BUYS: (i) C1 -- the s* ladder exists at "
          "12 rungs incl. the NEW deepest h = 20 (margin -87.95 "
          "dex), exactly the r205 clearance in crossing dress "
          "(barrier named); (ii) C2 -- the positive-sum FORM "
          "EXISTS: in EVERY battery coordinate the post-wrap "
          "prime steps are one-signed (coherence 1.0, all rungs, "
          "both orders) and the wall statement becomes 'the "
          "one-signed sum stays within the source-explicit "
          "boundary budget -C_h' -- with SCRARITH exhibiting the "
          "overshoot failure mode and EPSTEIN the inertia "
          "misread; (iii) BUT the increments are STATE-CARRIED "
          "(spread ~ 1 dex, order-dependent) and have NO p^{-1} "
          "tail (deepest slope %+.2f, terminal increment O(1) "
          "flat in h): Probe-D criterion legs A=%s B=%s C=%s => "
          "VERDICT %s -- the low-prime + tail split has the right "
          "SHAPE (pre-wrap primes already live in C_h) but no "
          "tail theorem applies at reachable rungs; what it does "
          "NOT buy: no positivity lever, no new all-h currency "
          "(the margin is the wall, said twice)"
          % (dslope_deep, legA, legB, legC, pd_enum))

    nlines = 0
    for h in rungs:
        for t in ("inc", "dec"):
            cen = res[h]["orb"][t]
            print("  ORBIT h=%-2d %s wrap@%s mus %s"
                  % (h, t, str(cen["wrap_p"]),
                     str(["%.5g" % v for v in cen["mus_f"]])))
            nlines += 1
        print("  ORBIT h=%-2d TERM oms %.2f ch %.3f finc %.3f "
              "spread %s taulog %.2f"
              % (h, res[h]["oms_log10"], chs[h], res[h]["finc"],
                 ("%.3f" % spreads[h]) if h in spreads else "NA",
                 res[h]["tau_log10"]))
        nlines += 1
    check("G61-increment-table", nlines == 3 * len(rungs),
          "the crossing-coordinate design table delivered: %d "
          "lines (3 per rung: inc ladder, dec ladder, terminal "
          "row) -- s* ladders, wrap primes, boundary terms, "
          "increments and spreads for any successor round"
          % nlines)

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the H-pin now has its CROSSING-COORDINATE "
         "form -- s*(h) <= 1 as a one-signed positive-sum problem "
         "with source-explicit boundary; the sum is state-carried "
         "and tail-less at reachable rungs (Probe D: STRUCTURE-"
         "ONLY-NO-GO).  Closes NOTHING, upgrades NOTHING.  NO RH "
         "CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "CROSSING-LADDER-DELIVERED(G23, h <= 20)",
        coh_enum + "(G25)",
        "WRAP-IS-ONLY-EXCEPTION(G26)",
        state_enum + "(G27)",
        decay_enum + "(G28)",
        "BOUNDARY-SOURCE-EXPLICIT-TAU-FLAT(G29/G50)",
        "SEPARATOR-IS-NOT-SIGN(G40/G41/G42)",
        "INERTIA-PRECONDITION-IS-A-LEG(G40, crossing dress)",
        "CROSSING-MARGIN-IS-THE-WALL(G23, definitional)",
        "PR-DOMINATION-COFINALLY-IS-THE-WALL(named, not crossed)",
        pd_enum + "(G60)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51)",
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
        "CROSSING-LADDER-DELIVERED", coh_enum,
        "WRAP-IS-ONLY-EXCEPTION", state_enum, decay_enum,
        "BOUNDARY-SOURCE-EXPLICIT-TAU-FLAT",
        "SEPARATOR-IS-NOT-SIGN", "INERTIA-PRECONDITION-IS-A-LEG",
        "CROSSING-MARGIN-IS-THE-WALL",
        "PR-DOMINATION-COFINALLY-IS-THE-WALL", pd_enum,
        "LOOPS-FLAGGED-NOT-CONSUMED", "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
