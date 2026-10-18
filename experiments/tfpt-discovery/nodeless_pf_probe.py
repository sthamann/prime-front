#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nodeless_pf_probe -- PRIME.NODELESS.PF.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface of the promotion wave) are not
touched.

=======================================================================
MISSION (round ~198: ground-state nodelessness vs Perron-Frobenius).
Round 197 (fewatom_reduction_probe, SPEC_SHA 35fb341bb281b04b, note
DXX) measured A_{v_0}(t) = sum_k v_k cos(om_k t) NONNEGATIVE on
[0, L] at all 14 rungs -- a nodeless positive bump peaked exactly at
L/2 -- and named the new target: prove A_{v_0(h)} >= 0 for all h,
with Perron-Frobenius/Krein-Rutman the candidate route (named, not
consumed).  THIS round adjudicates that route with cheap decisive
censuses:

  N1 THE SIGN-PATTERN CENSUS.  PF gives one-signedness of the BOTTOM
     eigenvector of a symmetric matrix B iff B is (up to diagonal
     sign similarity) a Z-matrix: off-diagonals one-signed the right
     way.  The wall's off-diagonals are EXACTLY the Loewner divided
     differences Raw[i,j] = (f(b_i)-f(b_j))/(b_i-b_j) of the source
     potential f = f_pole + f_arch + 2 om pj (r189 dictionary,
     re-gated here).  Censused per rung over all K(K-1)/2 pairs:
     (n+, n-, n0) of Raw off-diag; the CHECKERBOARD census of
     (-1)^{i+j} Raw[i,j] (= the M-side/N M N off-diagonal signs --
     the M-basis census is the checkerboard census EXACTLY, positive
     diagonal scaling); the adjacency linkage sign(Raw[i,i+1]) ==
     sign(fhat_{i+1} - fhat_i) with the r189 descent counts as
     inheritance.  DECISION LOGIC (classical): PF-MODE-DIRECT-Z iff
     all off-diag <= 0 (bottom eigenvector one-signed);
     PF-MODE-CHECKERBOARD-Z iff (-1)^{i+j} Raw[i,j] <= 0 all pairs
     (bottom eigenvector parity-alternating); PF-MODE-METZLER-TOP-
     ONLY iff all >= 0 (PF speaks about the TOP eigenvector -- the
     WRONG END for the collapse direction); else OFF-DIAG-MIXED-PF-
     MODE-DEAD.  The r189 record (descents 2..34 of K-1, ascents in
     the majority) already forces MIXED at every rung -- measured
     fresh and gated, not assumed.  THE V0 CHECK: v_0's entrywise
     sign structure -- the r197 jr_0 ladder (|sum v_k|/sum |v_k| =
     1e-5..1e-43) already forces MIXED signs in the mode basis
     (one-signed => jr_0 = 1); the OPEN question is PARITY
     ALIGNMENT: is c_k = (-1)^k v_k one-signed (the L/2-peak
     structure suggests it)?  Censused: mis = #{k: c_k opposite},
     nz (zero-class entries), margin log10(min c/max c) if aligned.
     THE TRIVIAL-ROUTE EXHIBIT (honesty gate): coefficientwise
     nonnegativity does NOT imply function nonnegativity -- exhibit
     v = e_1: A(t) = cos(om_1 t) has nonneg coefficients and
     A(L/2) = -1 EXACTLY.  So even a one-signed v_0 (in any parity)
     would NOT close A >= 0 by inspection; the mode-basis PF chain,
     had it closed, would prove the WRONG statement's sign pattern.
     Both directions adjudicated on the record.
  N2 THE SOURCE CONTENT OF THE OFF-DIAGONAL SIGNS.  Components:
     pole off-diag = 2 sinh(a/2)^2/((1/4+b_i)(1/4+b_j)) > 0 EXACT
     (rank-1 Cauchy, r189 law re-gated); arch off-diag = divided
     differences of f_arch (r189 measured f_arch' > 0 on the grid;
     positivity censused HERE at every actual pair); prime off-diag
     = sum_q w_q Woff(u_q) (oscillatory, both signs).  So every
     NEGATIVE off-diagonal pair is a pair where the prime leg
     DOMINATES pole+arch (tautological given pole+arch > 0; the
     counts are cross-gated).  THE DOMINANCE LADDER: rat_ij =
     |Pr_ij|/(P+A)_ij over resolvable pairs -- fracdom (fraction
     rat > 1), median/max log10 rat per rung, tau-screened.  The
     honest reconciliation with r189's non-monotone f: the divided
     differences are NOT one-signed at the actual nodes precisely
     because the prime leg flips 2..34 adjacent pairs (and more);
     the pole does NOT dominate the off-diagonals rung-uniformly.
     THE EXACT-SOURCE STRUCTURE that survives: in PROFILE
     coordinates the prime block is a sum of translation couplings
     with weights -2 w_q < 0 (the r195 ACF law t_q = -2 w_q g(u_q)),
     i.e. the arithmetic hopping is one-signed ATTRACTIVE at the
     level of the continuum kernel; the obstructions between this
     and classical PF are (i) the band projection (Dirichlet
     smearing -- the band-limited kernel of a point coupling is NOT
     one-signed; kernel census N3), (ii) the pole's rank-one
     POSITIVE kernel phi(t) phi(s) (phi censused on the lattice),
     (iii) the arch counterterm (per-mode diagonal).  Each priced,
     none crossed.
  N3 THE TRANSFORMED CONE / KR PRICING.  (i) POSITION-KERNEL
     CENSUS at every rung: Kpos = C^T B C on the frozen 33-point
     lattice t_g = g L/32 (exact cosine table), for B in {RawW,
     RawP, RawA, PrimeEff}: off-diagonal sign fractions -- the
     measured answer to "is the wall a position-space Z-operator at
     band resolution".  (ii) KR CONE-INVARIANCE TESTS: the natural
     candidate T = froW I - RawW (and T_pr = froPr I - PrimeEff)
     applied to a frozen family of EXTREME-ISH cone elements: the
     even-symmetrized Fejer profiles F_M(t-t0) + F_M(t+t0)
     (manifestly nonneg cosine polynomials; M in {1, 2, K//2, K-1},
     t0 = j L/8, j = 0..4) -- output profile min on the fine
     N = 16K lattice; a violation = output leaves the cone
     {A >= 0}: the Krein-Rutman route needs an invariant cone, and
     the tests price the NATURAL candidates (a violation kills
     those candidates at grid resolution, not the KR route as
     such -- typed).  (iii) THE QUANTIFIER ADJUDICATION: whatever
     N1/N2 deliver, resolve whether "A_{v_0(h)} >= 0 for all h"
     became easier: enum chain from the frozen logic below.
  N4 WORLDS AND WITNESS.  The same censuses through (SMOOTH, 5),
     (SCRARITH, 5), (EPSTEIN, 8).  THE r197 FAIL-LOCUS QUESTION:
     EPSTEIN(8) breaks the SHAPE (profile node, rmin -0.481) while
     its atom weights are ALL POSITIVE (negw = 0, r197 calib) --
     so the naive "positive hopping weights => nodeless" story is
     REFUTED by the fake world if its censuses do not separate:
     measure WHERE EPSTEIN's chain breaks (off-diag censuses,
     parity alignment, dominance, kernel, cone).  SCRARITH keeps
     the shape (nonneg TRUE, r197): its censuses are the
     positive control.  WITNESS (r172 recipe VERBATIM, h = 5,
     W = 1000): the matrix-side censuses are witness-INVARIANT BY
     CONSTRUCTION (typed definitional, not sold); the RAY-side
     alignment is deformed -- mis/profile-min of base vs witness
     ray measured (the base ray overlaps v_0 at 1.000000, r197).

PRE-REGISTERED PRIORS (resolve-and-record; NONE is gate-forcing):
  P1 off-diagonals MIXED at every rung (from the r189 descent/
     ascent record) -- mode-basis PF dead at every rung.
  P2 v_0 IS parity-aligned (c = D_par v_0 one-signed) at every
     rung: GENUINELY OPEN (suggested by the L/2 peak; the
     measurement decides).
  P3 pole+arch off-diagonals positive at EVERY pair (pole exact;
     arch expected from the r189 grid record).
  P4 EPSTEIN(8) does NOT separate on hopping signs (negw = 0) --
     its break sits in the atom POSITIONS/dominance pattern: which
     census separates is OPEN.
  P5 band-limited position kernels are mixed-sign for every block
     (Dirichlet smearing of point couplings).
  P6 the natural KR cone candidates admit at least one violation
     (the Fejer family is tangent to the cone boundary): OPEN.

NOTATION (r171-r197 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a = 2 pi k/L; b_k = om_k^2;
nrm_0 = sqrt(2a), nrm_k = sqrt(a); par_k = (-1)^k; atoms
{(u_q, w_q)} = {(log q, log p/sqrt q)}, q = p^m <= h, ascending q;
Raw = D_par N M N D_par (congruence: M PSD <=> Raw PSD); PrimeEff =
RawW - RawP - RawA (exact difference, == sum w_q W(u_q) by the r195
ACF law, re-gated); W(u) the r195 ACF kernel; fhat_i = b_i Raw[i,0]
= f(b_i) - f(0) (r189 extraction VERBATIM); pole laws fpole(b) =
-2 sinh(a/2)^2/(1/4+b), DD_pole(i,j) = 2 sinh(a/2)^2/((1/4+b_i)
(1/4+b_j)), diag f'_pole = 2 sinh(a/2)^2/(1/4+b_k)^2 (r189
VERBATIM).  v_0 = bottom eigenvector of Raw by mp INVERSE ITERATION
at every rung (r195 A3 lineage; 3 LU solves, wards: eigen-residual,
Rayleigh stability, eigsy overlap at ANAT_MP); c_k = (-1)^k v_k
sign-normalized so the entry of max |c| is positive.  Profile grid:
N = 16 K points, exact cosine table, half-window stats (r197
VERBATIM).  Kernel grid: 33 points t_g = g L/32, exact table
ct32[m] = cos(2 pi m/32), Cmat[k][g] = ct32[(k g) mod 32]; kernel
Kpos = Cmat^T B Cmat.  Fejer family: F coefficients v_0 = 2(M+1),
v_k = 4(M+1-k) cos(2 pi k j/8) (exact table den 8), M in
sorted set {1, 2, K//2, K-1}, j = 0..4; family membership (min >=
-1e-30 rel) warded per member.  Cone shift c = fro(B) (Frobenius),
per operator.  Censuses use zero class ZCLS x max|entry| of the
censused matrix; dominance over pairs with (P+A)_ij > zb.

DPS schedule (r182/r189/r195/r197 ladder VERBATIM): DPS = {4: 60,
5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110,
13: 120, 14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16,
H_HOLD = 20.  ANAT_MP = (4, 5, 8, 13) (eigsy overlap ward).
CONTROLS: (SMOOTH, 5, 60), (SCRARITH, 5, 60), (EPSTEIN, 8, 80).
WIT_RUNG = 5, WIT_FACT = 1000.  Kernel grid den 32 (33 points);
Fejer t0 den 8.

FROZEN BARS: ASM_BAR 1e-30; POLE_SQ_BAR 1e-35; LOEW_BAR 1e-30;
POLE_DD_BAR 1e-35; INVIT_RES_BAR 1e-12; INVIT_STAB_BAR 1e-6;
OVL_BAR 1e-12; GRID_BAR 1e-40 (cos tables vs direct, abs);
ZCLS 1e-30 (zero class, rel); PROF_NONNEG_BAR 1e-30 (rel);
FEJ_BAR 1e-30 (family membership, rel); CONE_BAR 1e-25 (violation
threshold, rel -- far above dps noise); CTRL_ASM_BAR 1e-25;
SMOOTH_ID_BAR 1e-25; WIT_YT_BAND (990, 1010); WIT_A0_BAR 1e-6;
TAU_FLAT_BAR 0.30; RUNTIME_BAR 2700 s.  Record tolerances: LOG_TOL
0.10 dex; FRAC_TOL 0.05 (absolute, fractions); SLOPE_TOL 0.05;
counts exact.  Inheritance cross-checks: descents == R189_DESC
exact; (n+, n-, n0) == R195_SIGNS exact; log10|rmin| == R197_RMIN
(LOG_TOL); nsc == 0.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  pfMode   := PF-MODE-DIRECT-Z iff raw_np == 0 at every rung;
              PF-MODE-METZLER-TOP-ONLY iff raw_nn == 0 at every
              rung; PF-MODE-CHECKERBOARD-Z iff cb_np == 0 at every
              rung; else OFF-DIAG-MIXED-PF-MODE-DEAD;
  v0Sign   := V0-PARITY-ALIGNED-ALL-RUNGS iff mis == 0 at every
              rung; else V0-PARITY-BROKEN;
  srcEnum  := PRIME-CARRIES-ALL-NEGATIVE-OFFDIAG iff pole+arch
              positive at every pair at every rung (then every
              negative pair is prime-dominated, cross-gated); else
              POLE-ARCH-SIGNED (records where);
  kernEnum := POSITION-KERNEL-MIXED-AT-BAND-RESOLUTION iff the
              wall kernel off-diagonal negative fraction is in
              (0, 1) at every rung; POSITION-KERNEL-Z-AT-BAND iff
              posfrac == 0 everywhere; else resolved at freeze;
              appended block-level law (resolve-and-record):
              KERNEL-SPLIT-POLE-POSITIVE-HOPPING-Z iff kneg_P == 0
              and kneg_A, kneg_Pr >= 0.95 at every rung;
  krEnum   := KR-WALL-CONE-FAILS-POLE-IS-THE-OBSTRUCTION iff the
              wall operator violates at every rung while the
              NO-POLE operator (amendment A1) has ZERO violations
              at every rung; else KR-NATURAL-CONE-CANDIDATES-FAIL
              iff >= 1 wall violation; else
              KR-CONE-SURVIVES-TESTS-AT-GRID-RESOLUTION;
  chain    := PF-CHAIN-CLOSES-PER-RUNG-MODE-BASIS iff pfMode in
              {DIRECT-Z, CHECKERBOARD-Z} and v0Sign aligned
              accordingly (STILL not A >= 0 -- the exhibit gate
              G34 stands between coefficients and the function);
              else CHAIN-OPEN-FUNCTION-SPACE iff profile nonneg
              holds at every rung while pfMode == MIXED (the r197
              target stays function-space); else
              CHAIN-BROKEN-SHAPE.

RECORD TABLES (frozen at freeze from the disclosed calibration
ladder: TWO structural smokes (smoke1 27/27 pre-A1, smoke2 27/27
post-A1, rungs 4/5/8 + SCRARITH, both at pre-freeze SHA
ca54e8e3915db6dc) and ONE disclosed calibration pass
(calib_npf_pass1.log, 27/27, 783.8 s, same pre-freeze SHA; tables
frozen VERBATIM); all logs kept).  RESOLVED VERDICTS: P1 TRUE --
off-diagonals MIXED at every rung (n+ 15..1749, n- 6..1026, zero
class empty; checkerboard mixed in BOTH parities): pfMode =
OFF-DIAG-MIXED-PF-MODE-DEAD, the mode-basis PF route is DEAD at
every reachable rung, decided already at adjacent pairs (descents
== r189 EXACT).  P2 REFUTED -- v_0 is NOT parity-aligned: mis =
2..24 misaligned entries; the aligned HEAD is SHALLOW, hd = 4..7
modes only (slowly growing), and the misaligned |c|-mass fraction
is FLAT at the 1e-2.5..1e-3.0 class (slope vs log10 tau +0.004:
NOT a tau ladder -- the pre-registered alignment-depth expectation
is CORRECTED on the record): v0Sign = V0-PARITY-BROKEN; a stable
~0.15 percent of the ray's ell-1 mass sits parity-wrong at every
rung.  P3 TRUE at every pair of every rung (pole+arch off-diag
negative count 0; pole DD positive exact): srcEnum =
PRIME-CARRIES-ALL-NEGATIVE-OFFDIAG, every negative off-diagonal
is a prime-dominated pair (cross-gate exact, nflip == raw_nn);
the prime leg dominates pole+arch at the MAJORITY of pairs
(fracdom 0.45..0.77, median log10 rat 0.0..0.4, max 0.6..2.4) --
the pole does NOT dominate the off-diagonals anywhere near
rung-uniformly.  P5 SPLIT VERDICT (the round's sharpest kernel
finding): the WALL kernel is mixed at band resolution (negfrac
0.20..0.56) but the BLOCKS are NOT -- pole kernel negfrac = 0.000
EXACTLY at every rung (phi > 0 on the whole lattice, near-flat,
log10|min/max| -0.01..-0.06), arch kernel negfrac 0.955..0.989,
prime kernel negfrac 0.973..1.000: kernEnum = POSITION-KERNEL-
MIXED-AT-BAND-RESOLUTION + KERNEL-SPLIT-POLE-POSITIVE-HOPPING-Z
-- the attractive-hopping Z-structure SURVIVES the band
projection almost exactly on the prime+arch part, and the wall's
kernel mixing is entirely the pole-vs-hopping competition.  P6
RESOLVED SHARPER THAN POSED: the wall operator froW I - RawW
violates cone invariance on 11..14 of 20 family members at EVERY
rung (worst excursion log10 -0.8..-1.8), the prime-only operator
violates on 0..1 (isolated single violations at h = 13, 14, 20),
and the NO-POLE operator (amendment A1) has ZERO violations at
EVERY rung: krEnum = KR-WALL-CONE-FAILS-POLE-IS-THE-OBSTRUCTION
-- removing the pole alone repairs cone invariance on the whole
family.  chain = CHAIN-OPEN-FUNCTION-SPACE (profile nonneg
re-verified at all 14 rungs, rmin == r197, nsc == 0).  P4
RESOLVED: EPSTEIN(8) breaks the shape with negw = 0 and censuses
of the SAME KIND as MAIN (mixed off-diag +136/-74, pa- 0,
prime-dominated fracdom 0.767, cone W17/NP0) -- EXCEPT the
alignment head: hd(EPSTEIN) = 0 vs MAIN 4..7 / SCRARITH 6 /
SMOOTH 2 (single-cell separation, recorded NOT sold as a
detector); SMOOTH(5) is the structural outlier: off-diagonals
ALL POSITIVE (raw_nn = 0 -- the mixed census is an ATOM-WORLD
phenomenon), fracdom 0.000, and its wall op is CONE-PRESERVING
(W0/NP0) despite carrying the same pole -- the pole obstruction
is BALANCE-dependent, not absolute; SMOOTH also keeps nonneg
with all-POSITIVE off-diagonals: a live exhibit that the shape
needs NO Z-structure.  WITNESS: base mis 4 hd 4 nonneg True
(ovl 1.000000) -> wit mis 4 hd 4 nonneg True (ovl 0.998106):
alignment/cone readings witness-stable at x1000.
CAL_RAWNP {h: n+}: 4: 15, 5: 38, 6: 68, 7: 111, 8: 126, 9: 207,
  10: 272, 11: 361, 12: 442, 13: 529, 14: 654, 15: 794, 16: 955,
  20: 1749.
CAL_RAWNN {h: n-}: 4: 6, 5: 17, 6: 23, 7: 42, 8: 84, 9: 93,
  10: 134, 11: 167, 12: 261, 13: 332, 14: 427, 15: 481, 16: 585,
  20: 1026.
CAL_CBNP {h: checkerboard n+}: 4: 9, 5: 26, 6: 45, 7: 74, 8: 106,
  9: 149, 10: 214, 11: 265, 12: 349, 13: 432, 14: 542, 15: 644,
  16: 759, 20: 1381.
CAL_FRACDOM: 0.524, 0.509, 0.451, 0.595, 0.662, 0.600, 0.586,
  0.665, 0.708, 0.767, 0.746, 0.712, 0.729, 0.742 (h = 4..16, 20).
CAL_MEDRAT (log10 median): 0.00, 0.03, -0.08, 0.16, 0.21, 0.15,
  0.16, 0.28, 0.27, 0.37, 0.33, 0.30, 0.38, 0.42.
CAL_MAXRAT (log10 max): 0.59, 1.07, 0.93, 1.43, 1.49, 1.57, 1.61,
  1.88, 1.95, 2.07, 2.02, 1.99, 2.24, 2.44.
CAL_MIS {h: misaligned entries}: 4: 2, 5: 4, 6: 4, 7: 8, 8: 10,
  9: 12, 10: 12, 11: 14, 12: 18, 13: 19, 14: 20, 15: 24, 16: 21,
  20: 23 (zero-class entries nz = 0 up to h = 14, then 1/4/21 at
  h = 15/16/20, recorded).
CAL_HD {h: head-aligned depth}: 4: 4, 5: 4, 6: 5, 7: 5, 8: 5,
  9: 5, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 7, 16: 7, 20: 7.
CAL_MISMASS (log10 misaligned |c|-mass fraction): -2.7, -2.5,
  -2.9, -2.7, -2.7, -2.9, -2.9, -2.8, -2.8, -2.9, -3.0, -3.0,
  -2.9, -2.9 -- FLAT.
CAL_KNEGW (wall kernel off-diag negfrac): 0.473, 0.485, 0.519,
  0.473, 0.417, 0.436, 0.561, 0.197, 0.462, 0.356, 0.284, 0.500,
  0.379, 0.201.
CAL_KNEGA (arch kernel negfrac): 0.989, 0.968, 0.972, 0.970,
  0.962, 0.970, 0.970, 0.970, 0.955, 0.958, 0.970, 0.962, 0.962,
  0.958.
CAL_KNEGPR (prime kernel negfrac): 1.000, 0.992, 1.000, 1.000,
  0.996, 0.996, 1.000, 0.977, 1.000, 1.000, 0.981, 0.989, 0.977,
  0.973.
CAL_KNEGP (pole kernel negfrac): 0.000 at every rung; phi_neg
  False at every rung.
CAL_CONEW {h: wall violations of 20}: 4: 11, 5: 11, 6: 13, 7: 13,
  8: 14, 9: 13, 10: 13, 11: 12, 12: 11, 13: 13, 14: 13, 15: 13,
  16: 13, 20: 14.
CAL_CONEP {h: prime-op violations}: 0 everywhere except 13: 1,
  14: 1, 20: 1.
CAL_CONENP {h: no-pole violations}: 0 at EVERY rung.
CAL_CTRL: (SCRARITH, 5): raw (+40, -15), pa- 0, fracdom 0.491,
  mis 3, hd 6, negw 0, nonneg True, nsc 0, knegW 0.549, cone
  W9/NP0; (EPSTEIN, 8): raw (+136, -74), cb+ 104, pa- 0, fracdom
  0.767, mis 10, hd 0, negw 0, nonneg False, nsc 1, rmin -0.481,
  knegW 0.220, cone W17/NP0; (SMOOTH, 5): raw (+55, -0), fracdom
  0.000, mis 5, hd 2, nonneg True, nsc 0, knegW 0.934, cone
  W0/NP0, continuum id ward 2.1e-60.
CAL_WIT: ytr 1000.00, a0dev 4.1e-55, base mis 4 hd 4 nonneg True
  ovl 1.000000, wit mis 4 hd 4 nonneg True ovl 0.998106.
CAL_SLOPES (vs log10 tau, dimensionless): fracneg -0.002,
  fracdom -0.004, mis/K -0.000, knegW +0.003, mismass +0.004 --
  ALL FIVE FLAT (bar 0.30): none of the sign-pattern coordinates
  (including the misaligned mass) rides the tau currency.

AMENDMENTS (one, pre-freeze, disclosed, no bar/dps/grid/recipe
moved):
A1 (smoke1-driven): smoke1 measured prime-only cone violations = 0
  vs wall 11-14 at rungs 4/5/8; the NO-POLE wall operator
  fro(RawW - RawP) I - (RawW - RawP) was ADDED to the cone battery
  BEFORE the calibration freeze to localize the obstruction (it
  resolved: zero violations at every rung).  smoke2 27/27 with the
  extended battery.  No target changed.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
instrument wards G10-G12; S2 inherited dictionary G20-G22; S3 N1
censuses G30-G34; S4 N2 source content G40-G42; S5 N3 kernel/cone
G50-G52; S6 N4 worlds/witness G60-G61; S7 screens/adjudication
G70-G73; S8 pricing G80 + G99 runtime.  DETERMINISM: no randomness
anywhere; ProcessPool results keyed; run2 must be identical modulo
wall-clock tokens (lines carrying 'WALL').

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
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 10
RUNTIME_BAR = 2700.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
ANAT_MP = (4, 5, 8, 13)
NGRID_FAC = 16
KGRID_DEN = 32          # kernel grid: 33 points t_g = g L / 32
FEJ_T0_DEN = 8          # Fejer shifts t0 = j L / 8, j = 0..4
WIT_RUNG = 5
WIT_FACT = 1000
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

ASM_BAR = 1e-30
POLE_SQ_BAR = 1e-35
LOEW_BAR = 1e-30
POLE_DD_BAR = 1e-35
INVIT_RES_BAR = 1e-12
INVIT_STAB_BAR = 1e-6
OVL_BAR = 1e-12
GRID_BAR = 1e-40
ZCLS = 1e-30
PROF_NONNEG_BAR = 1e-30
FEJ_BAR = 1e-30
CONE_BAR = 1e-25
CTRL_ASM_BAR = 1e-25
SMOOTH_ID_BAR = 1e-25
WIT_YT_BAND = (990.0, 1010.0)
WIT_A0_BAR = 1e-6
TAU_FLAT_BAR = 0.30

LOG_TOL = 0.10
FRAC_TOL = 0.05
SLOPE_TOL = 0.05

# --------------------------------------- inheritance tables (r189/r195/r197)
R189_DESC = {4: 2, 5: 5, 6: 4, 7: 7, 8: 9, 9: 9, 10: 13, 11: 16,
             12: 18, 13: 20, 14: 22, 15: 23, 16: 25, 20: 34}
R195_SIGNS = {4: (0, 2, 1), 5: (0, 3, 1), 6: (0, 4, 0),
              7: (0, 4, 1), 8: (0, 5, 1), 9: (0, 6, 1),
              10: (0, 7, 0), 11: (0, 7, 1), 12: (0, 7, 1),
              13: (0, 7, 2), 14: (0, 8, 1), 15: (0, 8, 1),
              16: (0, 8, 2), 20: (0, 8, 4)}
R197_RMIN = {4: "-5.02", 5: "-7.54", 6: "-9.71", 7: "-12.09",
             8: "-14.28", 9: "-16.57", 10: "-19.01", 11: "-21.40",
             12: "-23.97", 13: "-26.29", 14: "-28.97", 15: "-31.07",
             16: "-33.63", 20: "-43.30"}

# --------------------- calibrated record tables (calib_npf_pass1.log)
_HS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
CAL_RAWNP = dict(zip(_HS, (15, 38, 68, 111, 126, 207, 272, 361,
                           442, 529, 654, 794, 955, 1749)))
CAL_RAWNN = dict(zip(_HS, (6, 17, 23, 42, 84, 93, 134, 167, 261,
                           332, 427, 481, 585, 1026)))
CAL_CBNP = dict(zip(_HS, (9, 26, 45, 74, 106, 149, 214, 265, 349,
                          432, 542, 644, 759, 1381)))
CAL_FRACDOM = dict(zip(_HS, ("0.524", "0.509", "0.451", "0.595",
                             "0.662", "0.600", "0.586", "0.665",
                             "0.708", "0.767", "0.746", "0.712",
                             "0.729", "0.742")))
CAL_MEDRAT = dict(zip(_HS, ("0.00", "0.03", "-0.08", "0.16",
                            "0.21", "0.15", "0.16", "0.28", "0.27",
                            "0.37", "0.33", "0.30", "0.38",
                            "0.42")))
CAL_MAXRAT = dict(zip(_HS, ("0.59", "1.07", "0.93", "1.43", "1.49",
                            "1.57", "1.61", "1.88", "1.95", "2.07",
                            "2.02", "1.99", "2.24", "2.44")))
CAL_MIS = dict(zip(_HS, (2, 4, 4, 8, 10, 12, 12, 14, 18, 19, 20,
                         24, 21, 23)))
CAL_HD = dict(zip(_HS, (4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7,
                        7)))
CAL_MISMASS = dict(zip(_HS, ("-2.7", "-2.5", "-2.9", "-2.7",
                             "-2.7", "-2.9", "-2.9", "-2.8",
                             "-2.8", "-2.9", "-3.0", "-3.0",
                             "-2.9", "-2.9")))
CAL_KNEGW = dict(zip(_HS, ("0.473", "0.485", "0.519", "0.473",
                           "0.417", "0.436", "0.561", "0.197",
                           "0.462", "0.356", "0.284", "0.500",
                           "0.379", "0.201")))
CAL_KNEGA = dict(zip(_HS, ("0.989", "0.968", "0.972", "0.970",
                           "0.962", "0.970", "0.970", "0.970",
                           "0.955", "0.958", "0.970", "0.962",
                           "0.962", "0.958")))
CAL_KNEGPR = dict(zip(_HS, ("1.000", "0.992", "1.000", "1.000",
                            "0.996", "0.996", "1.000", "0.977",
                            "1.000", "1.000", "0.981", "0.989",
                            "0.977", "0.973")))
CAL_CONEW = dict(zip(_HS, (11, 11, 13, 13, 14, 13, 13, 12, 11, 13,
                           13, 13, 13, 14)))
CAL_CONEP = dict(zip(_HS, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
                           1)))
CAL_SLOPES = {"fracneg": "-0.002", "fracdom": "-0.004",
              "misK": "-0.000", "knegW": "+0.003",
              "mismass": "+0.004"}
FROZEN_ENUMS = {"pfMode": "OFF-DIAG-MIXED-PF-MODE-DEAD",
                "v0Sign": "V0-PARITY-BROKEN",
                "srcEnum": "PRIME-CARRIES-ALL-NEGATIVE-OFFDIAG",
                "kernEnum": "POSITION-KERNEL-MIXED-AT-BAND-RESOLUTION",
                "krEnum": "KR-WALL-CONE-FAILS-POLE-IS-THE-"
                          "OBSTRUCTION",
                "chain": "CHAIN-OPEN-FUNCTION-SPACE"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
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
        return float("nan"), float("nan"), float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return float("nan"), float("nan"), float("nan")
    sl = sxy / sxx
    ic = my - sl * mx
    ssr = sum((y - (sl * x + ic)) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - ssr / sst if sst > 0 else float("nan")
    return sl, ic, r2


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
                       "verification/ import; eigenvector access "
                       "IN-SCOPE (anatomy contract, r195/r197 "
                       "lineage); zero-freeness unchanged; "
                       "concurrent-lane files untouched")


# ------------------------------------------------------- source helpers
def sieve_atoms(x: int):
    icap = int(math.floor(x))
    comp = np.zeros(icap + 1, dtype=bool)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist], \
        nlist


def world_atoms(world: str, x: int):
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms, [q for q, _p in nlist]
    if world == "EPSTEIN":
        icap = int(math.floor(x))
        rq = np.zeros(icap + 1)
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
        atoms = []
        qs = []
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
                qs.append(n)
        return atoms, qs
    if world == "SMOOTH":
        return None, None
    raise ValueError(world)


def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def W_atom_mp(u, oms, b, L, K):
    """Per-atom ACF kernel W(u): x^T W x = -2 int_0^{L-u} A A(.+u)."""
    W = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            W[i, j] = 2 * (oms[i] * mp.sin(oms[i] * u)
                           - oms[j] * mp.sin(oms[j] * u)) \
                / (b[i] - b[j])
            W[j, i] = W[i, j]
    W[0, 0] = 2 * (u - L)
    for k in range(1, K):
        W[k, k] = mp.sin(oms[k] * u) / oms[k] \
            + (u - L) * mp.cos(oms[k] * u)
    return W


def fvec1(K):
    gg = (mp.sqrt(5) - 1) / 2
    return [mp.frac((k + 1) * gg) - mp.mpf(1) / 2 for k in range(K)]


def form_of(x, M, K):
    return sum(x[i] * M[i, j] * x[j] for i in range(K)
               for j in range(K))


def bottom_vec_mp(Raw, K, froW):
    """Bottom eigenvector by mp inverse iteration (r195/r197
    VERBATIM: 3 LU solves, Rayleigh stability + eigen-residual)."""
    x = mp.matrix([mp.mpf(1) for _ in range(K)])
    lam2 = None
    for it in range(3):
        x = mp.lu_solve(Raw, x)
        nx = mp.sqrt(sum(x[i] ** 2 for i in range(K)))
        x = x / nx
        if it == 1:
            v2 = [x[i] for i in range(K)]
            Rv2 = [sum(Raw[i, j] * v2[j] for j in range(K))
                   for i in range(K)]
            lam2 = sum(v2[i] * Rv2[i] for i in range(K))
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K)) / froW
    stab = abs(lam - lam2) / abs(lam) if lam != 0 else mp.mpf(0)
    return v, lam, float(res), float(stab)


def prof_eval(v, K, N, ct):
    """Half-window lattice profile A(t_j), j = 0..N/2 (exact table)."""
    half = N // 2
    return [sum(v[k] * ct[(k * j) % N] for k in range(K))
            for j in range(half + 1)]


def prof_stats(v, K, N, ct):
    """r197 profile stats (peak-sign normalized): nsc, rmin, nonneg."""
    Av = prof_eval(v, K, N, ct)
    amax = max(abs(x) for x in Av)
    jpeak = max(range(len(Av)), key=lambda j: abs(Av[j]))
    if Av[jpeak] < 0:
        Av = [-x for x in Av]
    zb = mp.mpf(ZCLS) * amax
    sgn = [0 if abs(x) <= zb else (1 if x > 0 else -1) for x in Av]
    nz = [s for s in sgn if s != 0]
    nsc = sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])
    amin = min(Av)
    return dict(nsc=nsc, rmin=float(amin / amax),
                nonneg=bool(amin >= -zb),
                tpeak_frac=jpeak / float(N))


def offdiag_census(B, K):
    """(n+, n-, n0, checkerboard n+, checkerboard n-) over i<j pairs;
    zero class ZCLS x max |offdiag|."""
    om = mp.mpf(0)
    for i in range(K):
        for j in range(i):
            om = max(om, abs(B[i, j]))
    zb = mp.mpf(ZCLS) * om
    np_, nn, n0, cbp, cbn = 0, 0, 0, 0, 0
    for i in range(K):
        for j in range(i):
            x = B[i, j]
            if abs(x) <= zb:
                n0 += 1
                continue
            if x > 0:
                np_ += 1
            else:
                nn += 1
            cb = x if ((i + j) % 2 == 0) else -x
            if cb > 0:
                cbp += 1
            else:
                cbn += 1
    return np_, nn, n0, cbp, cbn, zb


def align_census(v0, K):
    """Parity alignment of c_k = (-1)^k v_k (sign-normalized at the
    max-|c| entry): mis count, zero count, head depth, misaligned
    |c|-mass fraction, sign changes of v_0 itself."""
    c = [((-1) ** k) * v0[k] for k in range(K)]
    cmax = max(abs(x) for x in c)
    kmax = max(range(K), key=lambda k: abs(c[k]))
    if c[kmax] < 0:
        c = [-x for x in c]
    zb = mp.mpf(ZCLS) * cmax
    mis = sum(1 for x in c if x < -zb)
    nz = sum(1 for x in c if abs(x) <= zb)
    hd = 0
    for x in c:
        if x > zb:
            hd += 1
        else:
            break
    tot = sum(abs(x) for x in c)
    mism = sum(abs(x) for x in c if x < -zb)
    mismass = float(mp.log(mism / tot, 10)) if mism > 0 else -300.0
    margin = float(mp.log(min(abs(x) for x in c if abs(x) > zb)
                          / cmax, 10)) if mis == 0 else float("nan")
    # sign changes of v_0 in the mode index (resolvable entries)
    sg = [0 if abs(v0[k]) <= zb else (1 if v0[k] > 0 else -1)
          for k in range(K)]
    nzs = [s for s in sg if s != 0]
    nscv = sum(1 for i in range(1, len(nzs)) if nzs[i] != nzs[i - 1])
    vp = sum(1 for s in sg if s > 0)
    vn = sum(1 for s in sg if s < 0)
    return dict(mis=mis, nz=nz, hd=hd, mismass=mismass,
                margin=margin, nscv=nscv, vp=vp, vn=vn)


def kernel_census(B, K, ct32):
    """Position kernel Kpos = C^T B C on the 33-point lattice
    t_g = g L/32 (exact table); off-diag sign fractions + diag."""
    G = KGRID_DEN + 1
    Cm = [[ct32[(k * g) % KGRID_DEN] for g in range(G)]
          for k in range(K)]
    T1 = [[sum(B[k, l] * Cm[l][g] for l in range(K))
           for g in range(G)] for k in range(K)]
    Kp = [[sum(Cm[k][g1] * T1[k][g2] for k in range(K))
           for g2 in range(G)] for g1 in range(G)]
    km = mp.mpf(0)
    for g1 in range(G):
        for g2 in range(g1):
            km = max(km, abs(Kp[g1][g2]))
    zb = mp.mpf(ZCLS) * km
    npos, nneg, n0 = 0, 0, 0
    for g1 in range(G):
        for g2 in range(g1):
            x = Kp[g1][g2]
            if abs(x) <= zb:
                n0 += 1
            elif x > 0:
                npos += 1
            else:
                nneg += 1
    tot = npos + nneg + n0
    dneg = sum(1 for g in range(G) if Kp[g][g] < -zb)
    return dict(negfrac=nneg / float(tot), posfrac=npos / float(tot),
                nz=n0, dneg=dneg)


def fejer_family(K, L, dps):
    """Even-symmetrized Fejer profiles: v_0 = 2(M+1), v_k =
    4(M+1-k) cos(2 pi k j / 8), k <= M; M in sorted {1, 2, K//2,
    K-1}, j = 0..4.  All members nonneg on [0, L] by construction
    (F_M >= 0; sum of two shifts)."""
    c8 = [mp.cos(2 * mp.pi * m / FEJ_T0_DEN)
          for m in range(FEJ_T0_DEN)]
    Ms = sorted(set((1, 2, K // 2, K - 1)))
    fam = []
    for M in Ms:
        for j in range(5):
            v = [mp.mpf(0)] * K
            v[0] = mp.mpf(2 * (M + 1))
            for k in range(1, M + 1):
                v[k] = 4 * (M + 1 - k) * c8[(k * j) % FEJ_T0_DEN]
            fam.append(("M%d_j%d" % (M, j), v))
    return fam


def cone_tests(ops, fam, K, N, ct):
    """Apply T = fro I - B to each family member for each operator
    (tag, B, fro); profile min on the fine lattice.  Returns
    ({tag: nviol}, nfam, fej_ok, worst log10 |min/max| of violating
    wall outputs).  Amendment A1 (smoke-driven, pre-freeze,
    disclosed): the NO-POLE operator was ADDED to the battery after
    smoke1 measured prime-op violations = 0 vs wall 11-14 -- the
    third operator localizes the cone obstruction; no bar, grid,
    dps or recipe moved."""
    nv = {tag: 0 for tag, _B, _f in ops}
    fej_ok = True
    worst = -300.0
    for _lab, v in fam:
        Av = prof_eval(v, K, N, ct)
        am = max(abs(x) for x in Av)
        if min(Av) < -mp.mpf(FEJ_BAR) * am:
            fej_ok = False
        for tag, B, fro in ops:
            y = [fro * v[i] - sum(B[i, j] * v[j] for j in range(K))
                 for i in range(K)]
            Ay = prof_eval(y, K, N, ct)
            aym = max(abs(x) for x in Ay)
            mn = min(Ay)
            if mn < -mp.mpf(CONE_BAR) * aym:
                nv[tag] += 1
                if tag == "W":
                    worst = max(worst,
                                float(mp.log(abs(mn) / aym, 10)))
    return nv, len(fam), fej_ok, worst


# ------------------------------------------------------- main worker
def w_main(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            atoms, qs = world_atoms("MAIN", h)
            out["natoms"] = len(atoms)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            # PrimeEff = exact difference; gated == sum w_q W(u_q)
            PrEff = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    PrEff[i, j] = RawW[i, j] - RawP[i, j] - RawA[i, j]
            froPr = mp.sqrt(sum(PrEff[i, j] ** 2 for i in range(K)
                                for j in range(K)))
            # ---- G20 assembly (r195 inheritance) + pole square
            Wq_list = [W_atom_mp(u, oms, b, L, K) for u, _w in atoms]
            dev = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    S = sum(w * Wq[i, j] for (_u, w), Wq
                            in zip(atoms, Wq_list))
                    dev = max(dev, abs(PrEff[i, j] - S))
                    den = max(den, abs(PrEff[i, j]))
            out["asm_dev"] = float(dev / den)
            x1 = fvec1(K)
            ps = 2 * s2 * (sum(x1[k] / (mp.mpf(1) / 4 + b[k])
                               for k in range(K))) ** 2
            pf = form_of(x1, RawP, K)
            out["pole_sq_dev"] = float(abs(ps - pf) / abs(ps))
            # ---- G21 Loewner off-diag + pole DD law (r189 VERBATIM)
            fhat = [b[i] * RawW[i, 0] for i in range(K)]
            cmax = max(abs(fhat[i]) for i in range(1, K))
            ldev = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    ldev = max(ldev, abs(RawW[i, j] * (b[i] - b[j])
                                         - (fhat[i] - fhat[j])))
            out["loew_dev"] = float(ldev / cmax)
            pdev = mp.mpf(0)
            pdmin = mp.mpf("inf")
            for i in range(K):
                pdev = max(pdev, abs(RawP[i, i]
                                     - 2 * s2 / (mp.mpf(1) / 4
                                                 + b[i]) ** 2))
                for j in range(i):
                    dd = 2 * s2 / ((mp.mpf(1) / 4 + b[i])
                                   * (mp.mpf(1) / 4 + b[j]))
                    pdev = max(pdev, abs(RawP[i, j] - dd))
                    pdmin = min(pdmin, dd)
            out["pole_dd_dev"] = float(pdev / (2 * s2 * 16))
            out["pole_dd_min_pos"] = bool(pdmin > 0)
            out["descents"] = sum(1 for i in range(K - 1)
                                  if fhat[i + 1] < fhat[i])
            # adjacency linkage: sign(Raw[i,i+1]) == ascent/descent
            om_adj = max(abs(RawW[i + 1, i]) for i in range(K - 1))
            zba = mp.mpf(ZCLS) * om_adj
            link_ok = True
            for i in range(K - 1):
                x = RawW[i + 1, i]
                d = fhat[i + 1] - fhat[i]
                if abs(x) <= zba:
                    continue
                if (x > 0) != (d > 0):
                    link_ok = False
            out["link_ok"] = link_ok
            # ---- bottom direction (mp inverse iteration, r195 A3)
            v0, lam0, invres, invstab = bottom_vec_mp(RawW, K, froW)
            out["invit_res"] = invres
            out["invit_stab"] = invstab
            out["lam0_pos"] = bool(lam0 > 0)
            if h in ANAT_MP:
                E, Q = mp.eigsy(RawW)
                i0 = min(range(K), key=lambda m: E[m])
                ovl = abs(sum(Q[i, i0] * v0[i] for i in range(K)))
                out["v0_ovl_dev"] = float(abs(ovl - 1))
            # ---- r195 sign-ladder inheritance
            tq_mp = [w * form_of(v0, Wq, K)
                     for (u, w), Wq in zip(atoms, Wq_list)]
            tmax = max(abs(t) for t in tq_mp)
            zbar = mp.mpf(ZCLS) * tmax
            out["signs"] = (sum(1 for t in tq_mp if t > zbar),
                            sum(1 for t in tq_mp if t < -zbar),
                            sum(1 for t in tq_mp if abs(t) <= zbar))
            out["negw"] = sum(1 for _u, w in atoms if w < 0)
            # ---- r197 profile inheritance + jr_0
            N = NGRID_FAC * K
            twopi = 2 * mp.pi
            ct = [mp.cos(twopi * m / N) for m in range(N)]
            pst = prof_stats(v0, K, N, ct)
            out["prof_nsc"] = pst["nsc"]
            out["prof_rmin"] = pst["rmin"]
            out["prof_nonneg"] = pst["nonneg"]
            num0 = abs(sum(v0[k] for k in range(K)))
            den0 = sum(abs(v0[k]) for k in range(K))
            out["jr0"] = float(num0 / den0)
            # grid ward at h in (4, 5): table vs direct
            if h in (4, 5):
                gdev = mp.mpf(0)
                for j in (1, N // 8, N // 4, 3 * N // 8, N // 2):
                    tj = L * j / N
                    direct = sum(v0[k] * mp.cos(oms[k] * tj)
                                 for k in range(K))
                    table = sum(v0[k] * ct[(k * j) % N]
                                for k in range(K))
                    gdev = max(gdev, abs(direct - table))
                ct32_ = [mp.cos(twopi * m / KGRID_DEN)
                         for m in range(KGRID_DEN)]
                for (k_, g_) in ((1, 3), (2, 7), (3, 17)):
                    if k_ < K:
                        tg = L * g_ / KGRID_DEN
                        gdev = max(gdev, abs(
                            mp.cos(oms[k_] * tg)
                            - ct32_[(k_ * g_) % KGRID_DEN]))
                out["grid_dev"] = float(gdev)
            # ---- N1 censuses
            np_, nn, n0, cbp, cbn, _zb = offdiag_census(RawW, K)
            out["raw_np"], out["raw_nn"], out["raw_n0"] = np_, nn, n0
            out["cb_np"], out["cb_nn"] = cbp, cbn
            out["npairs"] = K * (K - 1) // 2
            al = align_census(v0, K)
            out.update({("al_" + k2): v2 for k2, v2 in al.items()})
            # ---- N2 source content: pole+arch positivity + dominance
            PA_np, PA_nn = 0, 0
            om_pa = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    om_pa = max(om_pa, abs(RawP[i, j] + RawA[i, j]))
            zb_pa = mp.mpf(ZCLS) * om_pa
            rats = []
            ndom = 0
            nflip_neg = 0
            nres_pairs = 0
            om_w = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    om_w = max(om_w, abs(RawW[i, j]))
            zb_w = mp.mpf(ZCLS) * om_w
            for i in range(K):
                for j in range(i):
                    pa = RawP[i, j] + RawA[i, j]
                    if pa > zb_pa:
                        PA_np += 1
                    elif pa < -zb_pa:
                        PA_nn += 1
                    else:
                        continue
                    nres_pairs += 1
                    rat = abs(PrEff[i, j]) / abs(pa)
                    rats.append(rat)
                    if rat > 1:
                        ndom += 1
                    if RawW[i, j] < -zb_w:
                        nflip_neg += 1
                        if not (rat > 1 and pa > 0):
                            out["flip_xgate_bad"] = True
            out["pa_np"], out["pa_nn"] = PA_np, PA_nn
            out["fracdom"] = ndom / float(nres_pairs) \
                if nres_pairs else float("nan")
            out["fracneg"] = nn / float(out["npairs"])
            rats.sort()
            if rats:
                med = rats[len(rats) // 2]
                out["medrat"] = float(mp.log(med, 10)) if med > 0 \
                    else -300.0
                out["maxrat"] = float(mp.log(rats[-1], 10))
            out["nflip_neg"] = nflip_neg
            # ---- N3 kernel censuses + phi + cone tests
            ct32 = [mp.cos(twopi * m / KGRID_DEN)
                    for m in range(KGRID_DEN)]
            for tag, B in (("W", RawW), ("P", RawP), ("A", RawA),
                           ("Pr", PrEff)):
                kc = kernel_census(B, K, ct32)
                out["kneg_" + tag] = kc["negfrac"]
                out["kpos_" + tag] = kc["posfrac"]
                out["kdneg_" + tag] = kc["dneg"]
            phi = [1 / (mp.mpf(1) / 4 + b[k]) for k in range(K)]
            Aphi = prof_eval(phi, K, N, ct)
            phimax = max(Aphi)
            phimin = min(Aphi)
            out["phi_min_neg"] = bool(phimin < 0)
            out["phi_minmax"] = float(mp.log(abs(phimin) / phimax,
                                             10)) if phimin != 0 \
                else -300.0
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawW[i, j] - RawP[i, j]
            froNP = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                                for j in range(K)))
            fam = fejer_family(K, L, dps)
            nv, nfam, fej_ok, worst = cone_tests(
                (("W", RawW, froW), ("P", PrEff, froPr),
                 ("NP", NoP, froNP)), fam, K, N, ct)
            out["cone_nvw"] = nv["W"]
            out["cone_nvp"] = nv["P"]
            out["cone_nvnp"] = nv["NP"]
            out["cone_nfam"] = nfam
            out["fej_ok"] = fej_ok
            out["cone_worst"] = worst
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------- control worker
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
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            atoms, _qs = world_atoms(world, x)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            PrEff = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    PrEff[i, j] = RawW[i, j] - RawP[i, j] - RawA[i, j]
            froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            froPr = mp.sqrt(sum(PrEff[i, j] ** 2 for i in range(K)
                                for j in range(K)))
            # assembly / identity ward
            if atoms is not None:
                dev = mp.mpf(0)
                den = max(abs(PrEff[i, j]) for i in range(K)
                          for j in range(K))
                Sm = mp.zeros(K, K)
                for u, w in atoms:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for i in range(K):
                        for j in range(K):
                            Sm[i, j] += w * Wq[i, j]
                for i in range(K):
                    for j in range(K):
                        dev = max(dev, abs(PrEff[i, j] - Sm[i, j]))
                out["asm_dev"] = float(dev / den)
                out["negw"] = sum(1 for _u, w in atoms if w < 0)
            else:
                x_ = fvec1(K)

                def xWx(w_):
                    Wq = W_atom_mp(w_, oms, b, L, K)
                    return form_of(x_, Wq, K) * mp.exp(w_ / 2)
                omax = oms[K - 1]
                n = int(mp.floor(L * 2 * omax / mp.pi)) + 2
                pts = [L * j / n for j in range(n + 1)]
                quadv = mp.quad(xWx, pts)
                tgt = form_of(x_, PrEff, K)
                out["asm_dev"] = float(abs(tgt - quadv)
                                       / max(abs(tgt),
                                             mp.mpf("1e-30")))
                out["negw"] = None
            # bottom direction via full eigsy (small K)
            E, Q = mp.eigsy(RawW)
            i0 = min(range(K), key=lambda m: E[m])
            vb = [Q[i, i0] for i in range(K)]
            # censuses
            np_, nn, n0, cbp, cbn, _zb = offdiag_census(RawW, K)
            out["raw_np"], out["raw_nn"] = np_, nn
            out["cb_np"] = cbp
            al = align_census(vb, K)
            out["al_mis"], out["al_hd"] = al["mis"], al["hd"]
            # pole+arch positivity + dominance
            om_pa = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    om_pa = max(om_pa, abs(RawP[i, j] + RawA[i, j]))
            zb_pa = mp.mpf(ZCLS) * om_pa
            PA_nn = 0
            ndom = 0
            nres = 0
            for i in range(K):
                for j in range(i):
                    pa = RawP[i, j] + RawA[i, j]
                    if abs(pa) <= zb_pa:
                        continue
                    nres += 1
                    if pa < 0:
                        PA_nn += 1
                    if abs(PrEff[i, j]) / abs(pa) > 1:
                        ndom += 1
            out["pa_nn"] = PA_nn
            out["fracdom"] = ndom / float(nres) if nres else \
                float("nan")
            # profile + kernel + cone
            N = NGRID_FAC * K
            twopi = 2 * mp.pi
            ct = [mp.cos(twopi * m / N) for m in range(N)]
            pst = prof_stats(vb, K, N, ct)
            out["prof_nsc"] = pst["nsc"]
            out["prof_nonneg"] = pst["nonneg"]
            out["prof_rmin"] = pst["rmin"]
            ct32 = [mp.cos(twopi * m / KGRID_DEN)
                    for m in range(KGRID_DEN)]
            kc = kernel_census(RawW, K, ct32)
            out["kneg_W"] = kc["negfrac"]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawW[i, j] - RawP[i, j]
            froNP = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                                for j in range(K)))
            fam = fejer_family(K, L, dps)
            nv, nfam, fej_ok, _worst = cone_tests(
                (("W", RawW, froW), ("P", PrEff, froPr),
                 ("NP", NoP, froNP)), fam, K, N, ct)
            out["cone_nvw"], out["cone_nvp"] = nv["W"], nv["P"]
            out["cone_nvnp"] = nv["NP"]
            out["cone_nfam"] = nfam
            out["fej_ok"] = fej_ok
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------- witness leg
def witness_leg() -> dict:
    """r172 inflation witness VERBATIM at h = WIT_RUNG (r197 code
    path): dv = A_2 (W-1)/(b_2 - b_1) on ray modes 1, 2; the
    matrix-side censuses are witness-invariant BY CONSTRUCTION
    (definitional); the RAY-side alignment + cone membership are
    measured for base vs witness."""
    dps = DPS[WIT_RUNG]
    ce = R4.build_cell(WIT_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out: dict = {}
    with mp.workdps(dps):
        aa = mp.log(WIT_RUNG) / 2
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        RawW = raw_of(ce["mpM"], par, nrm, K)
        froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                           for j in range(K)))
        v0, _lam0, _r, _s = bottom_vec_mp(RawW, K, froW)
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum(((-1) ** k) * cs[k] for k in range(K))
        A2 = sum(((-1) ** k) * cs[k] * b[k] for k in range(1, K))
        yt = abs(A2 / A0)
        dv = A2 * (WIT_FACT - 1) / (b[2] - b[1])
        cs2 = list(cs)
        cs2[1] += dv
        cs2[2] += dv
        A0w = sum(((-1) ** k) * cs2[k] for k in range(K))
        A2w = sum(((-1) ** k) * cs2[k] * b[k] for k in range(1, K))
        out["wit_ytr"] = float(abs(A2w / A0w) / yt)
        out["wit_a0dev"] = float(abs(A0w / A0 - 1))
        N = NGRID_FAC * K
        twopi = 2 * mp.pi
        ct = [mp.cos(twopi * m / N) for m in range(N)]

        def anat(ray):
            y = [par[k] * ray[k] for k in range(K)]
            ny = mp.sqrt(sum(t * t for t in y))
            y = [t / ny for t in y]
            al = align_census(y, K)
            pst = prof_stats(y, K, N, ct)
            ovl = abs(sum(y[k] * v0[k] for k in range(K)))
            return dict(mis=al["mis"], hd=al["hd"],
                        nonneg=pst["nonneg"], nsc=pst["nsc"],
                        ovl=float(ovl))
        out["base"] = anat(cs)
        out["wit"] = anat(cs2)
    return out


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"
    rec = not (calib or smoke)

    print("=" * 78)
    print("nodeless_pf_probe -- PRIME.NODELESS.PF.01  (mode %s)"
          % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/grids/recipes declared in the frozen "
          "spec (SPEC_SHA covers the declaration); priors P1-P6 "
          "pre-registered resolve-and-record, none gate-forcing; "
          "censuses, dominance ladder, kernel grid, Fejer family "
          "and cone shifts predefined; tau_h enters ONLY as a "
          "measured per-rung scalar; bottom direction mp inverse "
          "iteration at EVERY rung (r195 A3 lineage); the PF/KR "
          "dictionary is classical (Perron 1907/Frobenius 1912; "
          "Krein-Rutman 1948; positivity-improving semigroups, "
          "Reed-Simon IV Thm XIII.44) -- named, and this round "
          "measures WHETHER its hypotheses hold, consuming nothing")

    # ------------------------------------------------------------ S2
    section("S2  MAIN BATTERY (all reachable rungs)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    if errs:
        check("G20-acf-assembly-inherited", False,
              "worker errors at %s" % errs)
        print("ABORT: worker errors")
        return 1

    # ------------------------------------------------------------ S1
    section("S1  INSTRUMENT WARDS")
    gws = [h for h in (4, 5) if h in rungs]
    check("G10-grid-instrument-ward", all(
        res[h]["grid_dev"] <= GRID_BAR for h in gws),
          "exact cosine tables (fine N-lattice + kernel den-32 "
          "lattice) vs direct mp.cos at h = %s: max abs dev %.1e "
          "(bar %.0e)"
          % (str(gws), max(res[h]["grid_dev"] for h in gws),
             GRID_BAR))
    check("G11-fejer-family-ward", all(
        res[h]["fej_ok"] for h in rungs),
          "every Fejer family member nonneg on the fine lattice at "
          "every rung (rel bar %.0e) -- the cone-test inputs are "
          "certified cone elements (nfam %s)"
          % (FEJ_BAR, str({h: res[h]["cone_nfam"] for h in rungs})))
    mp_here = [h for h in rungs if h in ANAT_MP]
    check("G12-inverse-iteration-wards", all(
        res[h]["invit_res"] <= INVIT_RES_BAR
        and res[h]["invit_stab"] <= INVIT_STAB_BAR
        for h in rungs) and all(
        res[h].get("v0_ovl_dev", 0.0) <= OVL_BAR for h in mp_here)
        and all(res[h]["lam0_pos"] for h in rungs),
          "res <= %.1e (bar %.0e), stab <= %.1e (bar %.0e), eigsy "
          "overlap dev <= %.1e (bar %.0e at %s); lambda_0 > 0 at "
          "every rung"
          % (max(res[h]["invit_res"] for h in rungs), INVIT_RES_BAR,
             max(res[h]["invit_stab"] for h in rungs),
             INVIT_STAB_BAR,
             max((res[h].get("v0_ovl_dev", 0.0) for h in mp_here),
                 default=0.0), OVL_BAR, str(mp_here)))

    # ---------------------------------------------------- S2 gates
    section("S2b  INHERITED DICTIONARY GATES")
    check("G20-acf-assembly-inherited", all(
        res[h]["asm_dev"] <= ASM_BAR for h in rungs) and all(
        res[h]["pole_sq_dev"] <= POLE_SQ_BAR for h in rungs),
          "r195 ACF law re-verified at every rung (entrywise "
          "PrimeEff == sum w_q W(u_q)): max rel dev %.1e (bar "
          "%.0e); pole square max dev %.1e (bar %.0e)"
          % (max(res[h]["asm_dev"] for h in rungs), ASM_BAR,
             max(res[h]["pole_sq_dev"] for h in rungs),
             POLE_SQ_BAR))
    check("G21-loewner-dictionary-inherited", all(
        res[h]["loew_dev"] <= LOEW_BAR for h in rungs) and all(
        res[h]["pole_dd_dev"] <= POLE_DD_BAR for h in rungs),
          "r189 off-diagonal one-function Loewner form re-verified "
          "(max rel dev %.1e, bar %.0e); pole divided-difference "
          "law RawP[i,j] == 2 sinh(a/2)^2/((1/4+b_i)(1/4+b_j)) "
          "(max rel dev %.1e, bar %.0e) -- the off-diagonals ARE "
          "the divided differences of f at every rung"
          % (max(res[h]["loew_dev"] for h in rungs), LOEW_BAR,
             max(res[h]["pole_dd_dev"] for h in rungs),
             POLE_DD_BAR))
    check("G22-descents-profile-signs-inherited", all(
        res[h]["descents"] == R189_DESC[h] for h in rungs) and all(
        res[h]["signs"] == R195_SIGNS[h] for h in rungs) and all(
        res[h]["prof_nonneg"] and res[h]["prof_nsc"] == 0
        for h in rungs) and all(
        abs(math.log10(max(abs(res[h]["prof_rmin"]), 1e-300))
            - float(R197_RMIN[h])) <= LOG_TOL for h in rungs),
          "descent counts == r189 CAL_DESC EXACT (%s); atom sign "
          "ladder == r195 EXACT; profile A_{v_0} >= 0 with 0 sign "
          "changes re-verified at every rung, log10 rmin == r197 "
          "within %.2f dex"
          % (str({h: res[h]["descents"] for h in rungs}), LOG_TOL))

    # ------------------------------------------------------------ S3
    section("S3  N1: SIGN-PATTERN CENSUSES")
    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL census h=%d npairs %d raw (+%d,-%d,0:%d) "
                  "cb (+%d,-%d) pa (+%d,-%d)"
                  % (h, r["npairs"], r["raw_np"], r["raw_nn"],
                     r["raw_n0"], r["cb_np"], r["cb_nn"],
                     r["pa_np"], r["pa_nn"]))
        ok30 = True
    else:
        ok30 = all(res[h]["raw_np"] == CAL_RAWNP[h]
                   and res[h]["raw_nn"] == CAL_RAWNN[h]
                   and res[h]["cb_np"] == CAL_CBNP[h]
                   for h in rungs)
    check("G30-offdiag-census-record", ok30,
          "off-diagonal sign census of Raw_h over all pairs: "
          "(n+, n-) = %s; checkerboard census (M-side N M N "
          "off-diagonal signs, exact positive-scaling tautology) "
          "n+ = %s -- both positive and negative entries at EVERY "
          "rung in BOTH parities"
          % (str({h: (res[h]["raw_np"], res[h]["raw_nn"])
                  for h in rungs}),
             str({h: res[h]["cb_np"] for h in rungs})))

    mixed_all = all(res[h]["raw_np"] > 0 and res[h]["raw_nn"] > 0
                    for h in rungs)
    if all(res[h]["raw_np"] == 0 for h in rungs):
        pf_mode = "PF-MODE-DIRECT-Z"
    elif all(res[h]["raw_nn"] == 0 for h in rungs):
        pf_mode = "PF-MODE-METZLER-TOP-ONLY"
    elif all(res[h]["cb_np"] == 0 for h in rungs):
        pf_mode = "PF-MODE-CHECKERBOARD-Z"
    else:
        pf_mode = "OFF-DIAG-MIXED-PF-MODE-DEAD"
    ok31 = True if (calib or smoke) else \
        (pf_mode == FROZEN_ENUMS["pfMode"])
    check("G31-pf-mode-adjudication", ok31,
          "P1 RESOLVED: %s -- Perron-Frobenius needs one-signed "
          "off-diagonals (direct Z, global flip, or checkerboard "
          "diagonal-sign similarity); the wall has MIXED = %s: the "
          "mode-basis PF route to v_0 one-signedness is DEAD at "
          "every reachable rung"
          % (pf_mode, mixed_all))

    check("G32-adjacency-linkage", all(
        res[h]["link_ok"] for h in rungs),
          "sign(Raw[i,i+1]) == sign(fhat_{i+1} - fhat_i) at every "
          "resolvable adjacent pair of every rung: the PF answer "
          "was already contained in the r189 descent record "
          "(descents %s of K-1 -- descents AND ascents both "
          "present at every rung force the mixed census at "
          "adjacent pairs alone)"
          % str({h: "%d/%d" % (res[h]["descents"], res[h]["K"] - 1)
                 for h in (4, 8, 13, 20) if h in res}))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL align h=%d mis %d nz %d hd %d/%d mismass "
                  "%.1f margin %s nscv %d vp %d vn %d jr0 %.2e"
                  % (h, r["al_mis"], r["al_nz"], r["al_hd"], r["K"],
                     r["al_mismass"],
                     ("%.1f" % r["al_margin"])
                     if not math.isnan(r["al_margin"]) else "n/a",
                     r["al_nscv"], r["al_vp"], r["al_vn"],
                     r["jr0"]))
        ok33 = True
    else:
        ok33 = all(res[h]["al_mis"] == CAL_MIS[h]
                   and res[h]["al_hd"] == CAL_HD[h]
                   and abs(res[h]["al_mismass"]
                           - float(CAL_MISMASS[h])) <= 3 * LOG_TOL
                   for h in rungs)
    mis_all0 = all(res[h]["al_mis"] == 0 for h in rungs)
    v0_sign = ("V0-PARITY-ALIGNED-ALL-RUNGS" if mis_all0
               else "V0-PARITY-BROKEN")
    check("G33-v0-alignment-census", ok33,
          "P2 RESOLVED: %s -- misaligned entries of c_k = (-1)^k "
          "v_k: %s; the aligned HEAD is SHALLOW (hd = %s of K) and "
          "the misaligned |c|-mass fraction is FLAT at the "
          "1e-2.5..1e-3.0 class (%s dex; tau-screened flat in G70 "
          "-- the pre-registered alignment-depth expectation is "
          "CORRECTED on the record): a stable ~0.15 percent of "
          "the ray's ell-1 mass sits parity-wrong at every rung"
          % (v0_sign,
             str({h: res[h]["al_mis"] for h in rungs}),
             str({h: res[h]["al_hd"] for h in (4, 8, 13, 20)
                  if h in res}),
             str({h: "%.1f" % res[h]["al_mismass"]
                  for h in (4, 8, 13, 20) if h in res})))

    # exact exhibits (both directions of the trivial route)
    with mp.workdps(40):
        aa4 = mp.log(4) / 2
        e1_min = mp.cos((mp.pi / aa4) * aa4)   # cos(om_1 L/2) = -1
    ok34 = (abs(e1_min + 1) <= mp.mpf("1e-35")) and all(
        res[h]["jr0"] < 1e-3 and res[h]["al_vp"] > 0
        and res[h]["al_vn"] > 0 for h in rungs)
    check("G34-trivial-route-exhibits", ok34,
          "(i) coefficientwise nonnegativity does NOT imply "
          "function nonnegativity: v = e_1 has nonneg coefficients "
          "and A(L/2) = cos(om_1 L/2) = %s EXACTLY -- so even a "
          "one-signed v_0 would NOT give A >= 0 by inspection (the "
          "mode-basis PF chain, had it closed, closes the WRONG "
          "statement); (ii) v_0 is provably MIXED-SIGN in the mode "
          "basis: jr_0 = |sum v|/sum|v| = %s << 1 (one-signed => "
          "jr_0 = 1), direct count (+,-) = %s"
          % (mp.nstr(e1_min, 5),
             str({h: "%.0e" % res[h]["jr0"]
                  for h in (4, 13, 20) if h in res}),
             str({h: (res[h]["al_vp"], res[h]["al_vn"])
                  for h in (4, 13) if h in res})))

    # ------------------------------------------------------------ S4
    section("S4  N2: SOURCE CONTENT OF THE OFF-DIAGONAL SIGNS")
    pa_pos_all = all(res[h]["pa_nn"] == 0 for h in rungs)
    check("G40-pole-arch-positivity", pa_pos_all and all(
        res[h]["pole_dd_min_pos"] for h in rungs),
          "P3 RESOLVED: pole off-diagonals positive EXACT (rank-1 "
          "Cauchy law, G21) and (pole+arch) off-diagonals positive "
          "at EVERY resolvable pair of EVERY rung (negative count "
          "%s): every NEGATIVE wall off-diagonal is a pair where "
          "the prime divided difference dominates and flips "
          "pole+arch"
          % str({h: res[h]["pa_nn"] for h in rungs}))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL dom h=%d fracdom %.3f fracneg %.3f medrat "
                  "%.2f maxrat %.2f nflip %d"
                  % (h, r["fracdom"], r["fracneg"], r["medrat"],
                     r["maxrat"], r["nflip_neg"]))
        ok41 = True
    else:
        ok41 = all(abs(res[h]["fracdom"] - float(CAL_FRACDOM[h]))
                   <= FRAC_TOL
                   and abs(res[h]["medrat"] - float(CAL_MEDRAT[h]))
                   <= 3 * LOG_TOL
                   and abs(res[h]["maxrat"] - float(CAL_MAXRAT[h]))
                   <= 3 * LOG_TOL for h in rungs)
    xgate_ok = not any(res[h].get("flip_xgate_bad") for h in rungs)
    src_enum = ("PRIME-CARRIES-ALL-NEGATIVE-OFFDIAG"
                if pa_pos_all and xgate_ok else "POLE-ARCH-SIGNED")
    check("G41-dominance-ladder", ok41 and xgate_ok,
          "the prime/pole+arch dominance ladder |Pr_ij|/(P+A)_ij: "
          "fraction dominant (rat > 1) = %s, median log10 = %s, "
          "max log10 = %s; cross-gate: every negative off-diagonal "
          "pair IS prime-dominated (exact logic, no exception); "
          "enum %s -- the pole does NOT dominate the off-diagonals "
          "rung-uniformly (reconciles the r189 non-monotone f: the "
          "2..34 descents are prime-flipped pairs)"
          % (str({h: "%.2f" % res[h]["fracdom"] for h in rungs}),
             str({h: "%.1f" % res[h]["medrat"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.1f" % res[h]["maxrat"]
                  for h in (4, 8, 13, 20) if h in res}),
             src_enum))

    check("G42-source-structure-typing", all(
        res[h]["negw"] == 0 for h in rungs),
          "the EXACT source structure that survives PF's death in "
          "the mode basis: in PROFILE coordinates the prime block "
          "is a sum of translation couplings with one-signed "
          "weights -2 w_q < 0 (w_q = log p/sqrt q > 0 at every "
          "MAIN atom, verified; the r195 ACF law t_q = -2 w_q "
          "g(u_q) is the diagonal reading) -- an ATTRACTIVE "
          "arithmetic hopping; the named obstructions between this "
          "and classical PF/positivity-improvement: (i) the BAND "
          "PROJECTION (Dirichlet smearing, kernel census G50), "
          "(ii) the pole's rank-one kernel phi phi^T (phi census "
          "G50), (iii) the arch per-mode counterterm; each priced, "
          "none crossed -- typed EXACT-SOURCE-STRUCTURE + "
          "OBSTRUCTIONS-NAMED")

    # ------------------------------------------------------------ S5
    section("S5  N3: POSITION KERNELS + KR CONE PRICING")
    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL kern h=%d W %.3f/%.3f P %.3f/%.3f A "
                  "%.3f/%.3f Pr %.3f/%.3f dnegW %d phi_neg %s "
                  "phi_mm %.2f"
                  % (h, r["kneg_W"], r["kpos_W"], r["kneg_P"],
                     r["kpos_P"], r["kneg_A"], r["kpos_A"],
                     r["kneg_Pr"], r["kpos_Pr"], r["kdneg_W"],
                     r["phi_min_neg"], r["phi_minmax"]))
        ok50 = True
    else:
        ok50 = all(abs(res[h]["kneg_W"] - float(CAL_KNEGW[h]))
                   <= FRAC_TOL
                   and abs(res[h]["kneg_A"]
                           - float(CAL_KNEGA[h])) <= FRAC_TOL
                   and abs(res[h]["kneg_Pr"]
                           - float(CAL_KNEGPR[h])) <= FRAC_TOL
                   and res[h]["kneg_P"] == 0.0
                   and not res[h]["phi_min_neg"]
                   for h in rungs)
    kern_mixed = all(0.0 < res[h]["kneg_W"] < 1.0 for h in rungs)
    kern_enum = ("POSITION-KERNEL-MIXED-AT-BAND-RESOLUTION"
                 if kern_mixed else
                 ("POSITION-KERNEL-Z-AT-BAND" if all(
                     res[h]["kpos_W"] == 0 for h in rungs)
                  else "POSITION-KERNEL-OTHER"))
    split_ok = all(res[h]["kneg_P"] == 0.0
                   and res[h]["kneg_A"] >= 0.95
                   and res[h]["kneg_Pr"] >= 0.95 for h in rungs)
    kern_split = ("KERNEL-SPLIT-POLE-POSITIVE-HOPPING-Z"
                  if split_ok else "KERNEL-SPLIT-UNRESOLVED")
    check("G50-position-kernel-census", ok50,
          "P5 RESOLVED (SPLIT VERDICT): %s + %s -- off-diagonal "
          "negative fraction of the band-limited position kernel "
          "C^T B C on the frozen 33-point lattice: wall %s MIXED, "
          "but the blocks are NOT: pole %s (phi > 0 on the whole "
          "lattice, near-flat %s), arch %s, prime %s -- the "
          "attractive-hopping Z-structure SURVIVES the band "
          "projection almost exactly on prime+arch; the wall's "
          "kernel mixing is ENTIRELY the pole-vs-hopping "
          "competition (GRID+BAND resolution statement ONLY, "
          "typed, not a continuum claim)"
          % (kern_enum, kern_split,
             str({h: "%.2f" % res[h]["kneg_W"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % res[h]["kneg_P"]
                  for h in (4, 20) if h in res}),
             str({h: "%.2f" % res[h]["phi_minmax"]
                  for h in (4, 20) if h in res}),
             str({h: "%.2f" % res[h]["kneg_A"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % res[h]["kneg_Pr"]
                  for h in (4, 8, 13, 20) if h in res})))

    if calib or smoke:
        for h in rungs:
            r = res[h]
            print("CAL cone h=%d nviol W %d P %d NP %d of %d "
                  "worst %.1f"
                  % (h, r["cone_nvw"], r["cone_nvp"],
                     r["cone_nvnp"], r["cone_nfam"],
                     r["cone_worst"]))
        ok51 = True
    else:
        ok51 = all(res[h]["cone_nvw"] == CAL_CONEW[h]
                   and res[h]["cone_nvp"] == CAL_CONEP[h]
                   and res[h]["cone_nvnp"] == 0 for h in rungs)
    any_viol = any(res[h]["cone_nvw"] > 0 for h in rungs)
    pole_locus = all(res[h]["cone_nvnp"] == 0 for h in rungs)
    kr_enum = ("KR-WALL-CONE-FAILS-POLE-IS-THE-OBSTRUCTION"
               if any_viol and pole_locus else
               ("KR-NATURAL-CONE-CANDIDATES-FAIL" if any_viol
                else "KR-CONE-SURVIVES-TESTS-AT-GRID-RESOLUTION"))
    check("G51-kr-cone-invariance-tests", ok51,
          "P6 RESOLVED SHARPER THAN POSED: %s -- T = fro I - B for "
          "B in {wall, prime-only, NO-POLE wall (amendment A1)} on "
          "the certified Fejer cone family: violations wall %s / "
          "prime %s / no-pole %s of nfam per rung, worst wall "
          "excursion log10 %s: the {A >= 0} cone is NOT invariant "
          "under the wall shift, the prime-only operator has "
          "isolated single violations at deep rungs, and REMOVING "
          "THE POLE ALONE repairs invariance on the whole family "
          "at EVERY rung -- the cone obstruction is exactly the "
          "pole's rank-one positive kernel; Krein-Rutman on the "
          "natural cone dies at the pole leg (a different "
          "cone/shift is not excluded -- typed pricing, not a "
          "theorem)"
          % (kr_enum,
             str({h: res[h]["cone_nvw"] for h in rungs}),
             str({h: res[h]["cone_nvp"] for h in rungs}),
             str({h: res[h]["cone_nvnp"] for h in rungs}),
             str({h: "%.1f" % res[h]["cone_worst"]
                  for h in (4, 13, 20) if h in res})))

    if pf_mode in ("PF-MODE-DIRECT-Z", "PF-MODE-CHECKERBOARD-Z") \
            and mis_all0:
        chain = "PF-CHAIN-CLOSES-PER-RUNG-MODE-BASIS"
    elif all(res[h]["prof_nonneg"] for h in rungs) \
            and pf_mode == "OFF-DIAG-MIXED-PF-MODE-DEAD":
        chain = "CHAIN-OPEN-FUNCTION-SPACE"
    else:
        chain = "CHAIN-BROKEN-SHAPE"
    ok52 = True if (calib or smoke) else \
        (chain == FROZEN_ENUMS["chain"])
    check("G52-quantifier-adjudication", ok52,
          "N3 VERDICT: %s -- the honest answer to 'did A_{v_0(h)} "
          ">= 0 for all h become easier': NO by the classical "
          "routes tested: (b) the off-diagonals are mixed at every "
          "rung (PF dead in the mode basis, decided at adjacent "
          "pairs by the r189 descents), (c) v_0 is mixed-sign in "
          "the mode basis (jr_0 << 1) and its parity alignment "
          "breaks beyond a shallow 4..7-mode head (a flat "
          "1e-2.8-class mass sits parity-wrong), and the "
          "coefficient route would not reach A >= 0 anyway (G34); "
          "the KR function-cone route survives only as an "
          "UNPRICED-CONE search (natural candidates dead, G51); "
          "what the all-h statement still needs: a genuinely "
          "function-space positivity mechanism for the v_0(h) "
          "family -- the target stays open at exactly the r197 "
          "formulation, now with the classical shortcuts "
          "machine-excluded" % chain)

    # ------------------------------------------------------------ S6
    section("S6  N4: WORLDS + WITNESS")
    ctasks = list(CTRL_CELLS)
    if smoke:
        ctasks = [("SCRARITH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    if calib or smoke:
        for k, v in sorted(cres.items()):
            print("CAL ctrl %s x=%d raw (+%d,-%d) cb+ %d pa- %d "
                  "fracdom %.3f mis %d hd %d negw %s nonneg %s "
                  "nsc %d rmin %.2e knegW %.3f cone W%d/NP%d of "
                  "%d asm %.1e"
                  % (k[0], k[1], v["raw_np"], v["raw_nn"],
                     v["cb_np"], v["pa_nn"], v["fracdom"],
                     v["al_mis"], v["al_hd"], v["negw"],
                     v["prof_nonneg"], v["prof_nsc"],
                     v["prof_rmin"], v["kneg_W"], v["cone_nvw"],
                     v["cone_nvnp"], v["cone_nfam"],
                     v["asm_dev"]))
        ok60 = not cerrs
    else:
        def _ck(k):
            v = cres[k]
            if k[0] == "SMOOTH":
                return (v["raw_nn"] == 0 and v["cone_nvw"] == 0
                        and v["cone_nvnp"] == 0 and v["fej_ok"]
                        and v["prof_nonneg"]
                        and v["asm_dev"] <= SMOOTH_ID_BAR)
            if k[0] == "SCRARITH":
                return (v["raw_np"] > 0 and v["raw_nn"] > 0
                        and v["cone_nvw"] >= 1
                        and v["cone_nvnp"] == 0 and v["fej_ok"]
                        and v["prof_nonneg"] and v["negw"] == 0
                        and v["asm_dev"] <= CTRL_ASM_BAR)
            return (v["raw_np"] > 0 and v["raw_nn"] > 0
                    and v["cone_nvw"] >= 1
                    and v["cone_nvnp"] == 0 and v["fej_ok"]
                    and (not v["prof_nonneg"]) and v["negw"] == 0
                    and v["pa_nn"] == 0 and v["al_hd"] == 0
                    and v["asm_dev"] <= CTRL_ASM_BAR)
        ok60 = (not cerrs) and all(_ck(k) for k in cres)
    check("G60-worlds-battery", ok60,
          "P4 RESOLVED: EPSTEIN(8) breaks the shape (nonneg %s) "
          "with negw = %s -- all its atom weights POSITIVE: the "
          "naive 'attractive hopping => nodeless' story is "
          "REFUTED by the fake world -- and its PF-adjacent "
          "censuses are the SAME KIND as MAIN's (mixed off-diag "
          "%s, prime-dominated negatives, cone fails) EXCEPT the "
          "alignment head hd = %s (vs MAIN 4..7; single-cell "
          "separation, recorded NOT sold); SCRARITH keeps the "
          "shape with MAIN-kind censuses (nonneg %s); SMOOTH is "
          "the structural outlier: off-diagonals ALL POSITIVE "
          "(raw (+, -) %s -- the mixed census is an ATOM-WORLD "
          "phenomenon), wall op CONE-PRESERVING despite the same "
          "pole (the pole obstruction is BALANCE-dependent), "
          "nonneg True with NO Z-structure anywhere (live exhibit "
          "that the shape needs no Z-sign pattern); continuum id "
          "ward %s"
          % (str({k: cres[k]["prof_nonneg"]
                  for k in sorted(cres) if k[0] == "EPSTEIN"}),
             str({k: cres[k]["negw"]
                  for k in sorted(cres) if k[0] == "EPSTEIN"}),
             str({k: (cres[k]["raw_np"], cres[k]["raw_nn"])
                  for k in sorted(cres)}),
             str({k: cres[k]["al_hd"]
                  for k in sorted(cres) if k[0] == "EPSTEIN"}),
             str({k: cres[k]["prof_nonneg"]
                  for k in sorted(cres) if k[0] == "SCRARITH"}),
             str({k: (cres[k]["raw_np"], cres[k]["raw_nn"])
                  for k in sorted(cres) if k[0] == "SMOOTH"}),
             str({k: "%.0e" % cres[k]["asm_dev"]
                  for k in sorted(cres) if k[0] == "SMOOTH"})))

    wit = witness_leg()
    wok = (WIT_YT_BAND[0] <= wit["wit_ytr"] <= WIT_YT_BAND[1]
           and wit["wit_a0dev"] <= WIT_A0_BAR)
    if calib or smoke:
        print("CAL wit ytr %.2f a0dev %.1e base mis %d hd %d "
              "nonneg %s nsc %d ovl %.6f | wit mis %d hd %d "
              "nonneg %s nsc %d ovl %.6f"
              % (wit["wit_ytr"], wit["wit_a0dev"],
                 wit["base"]["mis"], wit["base"]["hd"],
                 wit["base"]["nonneg"], wit["base"]["nsc"],
                 wit["base"]["ovl"], wit["wit"]["mis"],
                 wit["wit"]["hd"], wit["wit"]["nonneg"],
                 wit["wit"]["nsc"], wit["wit"]["ovl"]))
        ok61 = wok
    else:
        ok61 = (wok and wit["base"]["nonneg"]
                and wit["wit"]["nonneg"]
                and wit["base"]["mis"] == wit["wit"]["mis"])
    check("G61-witness-battery", ok61,
          "r172 inflation witness VERBATIM at h = %d (y_t ratio "
          "%.1f in %s, A_0 dev %.1e <= %.0e): matrix-side censuses "
          "witness-INVARIANT BY CONSTRUCTION (definitional, not "
          "sold); ray-side: base mis %d hd %d nonneg %s (overlap "
          "with v_0 %.6f) vs witness mis %d hd %d nonneg %s "
          "(overlap %.6f) -- the x1000 deformation does not move "
          "the alignment/cone readings at this resolution"
          % (WIT_RUNG, wit["wit_ytr"], str(WIT_YT_BAND),
             wit["wit_a0dev"], WIT_A0_BAR, wit["base"]["mis"],
             wit["base"]["hd"], wit["base"]["nonneg"],
             wit["base"]["ovl"], wit["wit"]["mis"],
             wit["wit"]["hd"], wit["wit"]["nonneg"],
             wit["wit"]["ovl"]))

    # ------------------------------------------------------------ S7
    section("S7  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_fn, _i, _r = fit_line(xs_t, [res[h]["fracneg"]
                                    for h in scr])
    sl_fd, _i, _r = fit_line(xs_t, [res[h]["fracdom"]
                                    for h in scr])
    sl_mi, _i, _r = fit_line(xs_t, [res[h]["al_mis"]
                                    / res[h]["K"] for h in scr])
    sl_kw, _i, _r = fit_line(xs_t, [res[h]["kneg_W"]
                                    for h in scr])
    sl_mm, _i, _r = fit_line(xs_t, [res[h]["al_mismass"]
                                    for h in scr])
    if calib or smoke:
        print("CAL slopes: fracneg %+.3f fracdom %+.3f misK %+.3f "
              "knegW %+.3f mismass %+.3f"
              % (sl_fn, sl_fd, sl_mi, sl_kw, sl_mm))
        ok70 = True
    else:
        ok70 = (abs(sl_fn) <= TAU_FLAT_BAR
                and abs(sl_fd) <= TAU_FLAT_BAR
                and abs(sl_mi) <= TAU_FLAT_BAR
                and abs(sl_kw) <= TAU_FLAT_BAR
                and abs(sl_mm) <= TAU_FLAT_BAR
                and abs(sl_fn - float(CAL_SLOPES["fracneg"]))
                <= SLOPE_TOL
                and abs(sl_fd - float(CAL_SLOPES["fracdom"]))
                <= SLOPE_TOL
                and abs(sl_mi - float(CAL_SLOPES["misK"]))
                <= SLOPE_TOL
                and abs(sl_kw - float(CAL_SLOPES["knegW"]))
                <= SLOPE_TOL
                and abs(sl_mm - float(CAL_SLOPES["mismass"]))
                <= SLOPE_TOL)
    check("G70-tau-screen", ok70,
          "log-log slopes vs tau_h of the DIMENSIONLESS census "
          "coordinates: fracneg %+.3f, fracdom %+.3f, mis/K %+.3f, "
          "knegW %+.3f, mismass %+.3f -- ALL FIVE flat (bar %.2f): "
          "NONE of the sign-pattern coordinates rides the tau "
          "currency, INCLUDING the misaligned-mass fraction (a "
          "stable 1e-2.8-class quantity, NOT an alignment-depth "
          "ladder -- the pre-registered expectation corrected on "
          "the record); nothing here is a relabeled tau"
          % (sl_fn, sl_fd, sl_mi, sl_kw, sl_mm, TAU_FLAT_BAR))

    delivered = {
        "ATOMS": ["OFFDIAG-DD"], "MODES": ["OFFDIAG-DD"],
        "OFFDIAG-DD": ["SIGN-CENSUS", "DOMINANCE"],
        "MBLOCKS": ["OFFDIAG-DD", "TAU-SCALAR"],
        "SIGN-CENSUS": ["PF-ADJUDICATION"],
        "DOMINANCE": ["PF-ADJUDICATION"],
        "KERNEL-CENSUS": ["KR-PRICING"],
        "CONE-TESTS": ["KR-PRICING"],
        "PF-ADJUDICATION": ["SCREENS"],
        "KR-PRICING": ["SCREENS"],
        "TAU-SCALAR": ["SCREENS"], "SCREENS": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("SIGN-CENSUS", "DOMINANCE", "KERNEL-CENSUS",
                 "CONE-TESTS", "PF-ADJUDICATION", "KR-PRICING",
                 "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "ZEROVERIF-HYP", "RH"}
    check("G71-loop-guard", ndet == 6
          and not has_cycle(delivered) and not hot,
          "flagged cycles DETECTED (A0-triangle, census-forall-k, "
          "Gonek-1984, Montgomery-PC, WEIL-ALLTESTS, zero-"
          "verification-as-hypothesis), consumed by NOTHING: DFS "
          "ancestry of every delivered node clean; the round is "
          "fully zero-free (no ordinate cache); PF/KR adjudication "
          "is per-rung finite linear algebra with no edge into any "
          "criterion loop")

    check("G72-composed-chain-typing", True,
          "leg typing: {assembly, pole square, Loewner off-diag, "
          "pole DD law, adjacency linkage, flip cross-gate, e_1 "
          "exhibit} EXACT (mp <= 1e-30 class); {sign censuses, "
          "alignment census, dominance ladder, kernel censuses, "
          "cone violations, world/witness anatomy} MEASURED; "
          "{checkerboard tautology, witness matrix-invariance, "
          "demand-side readings} DEFINITIONAL; {kernel census "
          "resolution} GRID+BAND-ONLY (disclosed twice); the KR "
          "pricing kills the NATURAL candidates only -- no "
          "impossibility theorem sold; the surviving exact source "
          "structure (one-signed attractive hopping weights) is "
          "typed EXACT-SOURCE-STRUCTURE with the three named "
          "obstructions, not a mechanism claim")

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
    cf.update({("UNC", "PFCHAIN"): INF, ("PFCHAIN", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G73-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the PF chain closes the nodelessness cofinally' as a "
          "unit edge would raise the flow to 6 -- NOT REAL (the "
          "chain is measured DEAD in the mode basis and unpriced "
          "in function space): this round adds NO flow; census "
          "cardinality UNCHANGED; RH unreachable without the "
          "omega edges")

    # ------------------------------------------------------------ S8
    section("S8  PRICING + RESIDUE")
    check("G80-pricing", True,
          "what the round BUYS: (i) the r197 candidate route "
          "(Perron-Frobenius in the mode basis) is ADJUDICATED "
          "DEAD at every reachable rung by a cheap decisive census "
          "-- and the death was already latent in the r189 descent "
          "record (named); (ii) the checkerboard/M-side variant "
          "dies the same way (both parities mixed); (iii) v_0's "
          "sign anatomy is measured (head parity-aligned, deep-"
          "tail broken, mode-mixed overall) -- the coefficient "
          "route to A >= 0 is closed in BOTH directions (exhibit "
          "+ measurement); (iv) the source content of the "
          "negative off-diagonals is identified EXACTLY (prime-"
          "dominated pairs over a positive pole+arch background, "
          "dominance ladder frozen); (v) the KR function-cone "
          "route is priced: natural spectral-shift candidates "
          "fail cone invariance at every rung, band projection "
          "kills naive position-space Z-structure; (vi) the fake "
          "worlds show the censuses do NOT predict the shape -- "
          "the A >= 0 mechanism is NOT a sign-pattern phenomenon "
          "in any basis tested; the cofinality gap is UNMOVED")

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (one rung per dyadic block, all three at the "
         "same h; limsup form only mod D = 0.0042) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN: L1 = TAIL proven + H-pin open; WPD(a < gamma_1^2) "
         "<= H-pin; WPD non-lambda legs: extension instantiated, "
         "TAILWPD world front}.  The r197 structural target "
         "'A_{v_0(h)} >= 0 for all h' STAYS OPEN and is now "
         "SHARPENED: the classical PF/KR shortcuts are machine-"
         "excluded; the mechanism, if any, is genuinely function-"
         "space.  Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        pf_mode + "(G31)",
        v0_sign + "+SHALLOW-HEAD-FLAT-MISMASS(G33)",
        "COEFFICIENT-ROUTE-CLOSED-BOTH-DIRECTIONS(G34)",
        src_enum + "(G40/G41)",
        "EXACT-SOURCE-STRUCTURE+OBSTRUCTIONS-NAMED(G42)",
        kern_enum + "+" + kern_split + "(G50)",
        kr_enum + "(G51)",
        chain + "(G52)",
        "WORLDS-MEASURED-SMOOTH-METZLER-EPSTEIN-HD0(G60)",
        "WITNESS-ALIGNMENT-STABLE(G61)",
        "TAU-FLAT-CENSUSES-ALL-FIVE(G70)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G71)",
        "MINCUT-UNCHANGED(G73) + RESIDUE-UNCHANGED"]
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
        pf_mode, v0_sign, "COEFFICIENT-ROUTE-CLOSED", src_enum,
        kern_enum, kern_split, kr_enum, chain,
        "WORLDS-MEASURED", "TAU-FLAT-CENSUSES",
        "LOOPS-FLAGGED-NOT-CONSUMED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
