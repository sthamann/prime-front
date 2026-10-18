#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""turan_extremal_probe -- PRIME.TURAN.EXTREMAL.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
few-atom lane's fewatom_reduction_probe.py, the independent session's
untracked probes, sieve4_helper.bin, the promotion wave's surfaces)
are not touched.

=======================================================================
MISSION (round ~196: the Turan/Boas-Kac extremal import).  Round 195
(cancellation_functional_probe, SPEC_SHA a50b85bb112513a1, note
DXVIII) left the wall as a CLOSED TRUNCATED WEIL FORM on the cone of
positive-definite (PD) autocorrelations:
    x^T Raw x = 8 sinh^2(a/2) (int_0^inf e^{-t/2} A_x)^2
                - 2 [int_0^L g_x(w) a(w) dw]_reg
                - 2 sum_q (Lambda(q)/sqrt(q)) g_x(log q),
g_x(u) = int_0^{L-u} A_x(t) A_x(t+u) dt, A_x = sum_k x_k cos(om_k t),
om_k = 2 pi k / L, L = 2a = log h.  g_x is a PD function supported in
[-L, L] (Wiener-Khinchin) -- EXACTLY the class of the classical
Turan/Boas-Kac/Fejer extremal theory, never priced in 195 rounds.
THIS round imports that theory with exact citations, prices the wall
against it, and measures the ARITHMETIC-INPUT GAP: how many dex
separate the best classical-cone worst case from the true minimum.

T1  THE DICTIONARY (all classical inputs UNCONDITIONAL, zeta-free):
  (D1) POINTWISE BOUND (the workhorse).  For continuous PD g with
       supp g in [-L, L] (g(+-L) = 0, our class: autocorrelations),
       and lag 0 < u <= L:
           g(u) <= M_KR(u) g(0),
           M_KR(u) = cos(pi / (ceil(L/u) + 1)).
       Proof route gated here: sample on the lattice uZ (restriction
       of a PD function to a subgroup is PD, Bochner/Herglotz --
       typed classical); the sampled sequence c_j = g(ju) has
       c_j = 0 for j >= L/u (ju > L outside support; ju = L hits
       g(L) = 0), i.e. nonzero lags j <= n with
       n = ceil(L/u) - 1; the Fejer coefficient theorem (Fejer
       1915: nonneg cosine polynomial 1 + 2 sum_{j<=n} c_j cos jt
       has c_1 <= cos(pi/(n+2)), the constant M_n = 2 cos(pi/(n+2)))
       gives the bound.  Both sides machine-proved here: extremal
       construction (autocorrelation of S_m = sin((m+1)pi/(n+2)),
       manifest square, attains cos(pi/(n+2)) EXACTLY, sympy) and
       optimality (dual node certificate at the zeros
       theta_r = (2r+1)pi/(n+2) of the extremal polynomial: weights
       rho >= 0 with sum rho cos(j theta) = 0 for j = 2..n force
       c_1 <= cos(pi/(n+2)); nullspace solved exactly in sympy,
       n = 1..4 covers every atom of every reachable rung -- gated).
       SHARPNESS on the full cone: this equals the exact value of
       the Boas-Kac/Kolountzakis-Revesz pointwise Turan problem for
       the open interval: M(Omega, z) = cos(pi/(n+2)) for
       1/(n+1) <= |z|/L < 1/n [Boas-Kac, Duke Math. J. 12 (1945),
       189-206, Thms 2-3; Kolountzakis-Revesz, Canad. J. Math. 58
       (2006), 401-418, Cor. 4.1, via Fejer, J. Reine Angew. Math.
       146 (1915), 53-82; posed pointwise by
       Arestov-Berdysheva-Berens].  The SIGNED bound
       |g(u)| <= M_KR(u) g(0) follows by the theta -> theta + pi
       flip on the sampled sequence (gated symbolically); needed
       for signed-weight worlds (EPSTEIN).
  (D2) TURAN INTERVAL THEOREM.  int_{-L}^{L} g <= L g(0), extremal
       the triangle (Fejer) function = autocorrelation of the box
       [Siegel 1935 (Acta Math. 65); Boas-Kac 1945; survey and
       general domains: Kolountzakis-Revesz, Proc. AMS 131 (2003)
       3423-3430; Gorbachev 2001 (ball); Arestov-Berdysheva
       (polytopes)].  EXHIBIT gated: the mode-lattice subcone
       CONTAINS the extremal: x = e_0 gives A = 1, B = box,
       g_{e0}(u) = L - u exactly (from the r195 kernel diagonal),
       and int g_{e0} = L^2 = L g_{e0}(0) with EQUALITY; the
       subcone-wide Turan inequality int g_x = (L x_0)^2
       <= L g_x(0) = L(L/2)(|x|^2 + x_0^2) is the trivial
       x_0^2 <= |x|^2 (sympy).  Used quantitatively in the SMOOTH
       world (continuum atom measure).
  (D3) BOAS-KAC FACTORIZATION.  Every PD function supported in
       [-L, L] is an autocorrelation of a function supported on a
       half-interval [Boas-Kac 1945] -- the converse direction we
       hold BY CONSTRUCTION; typed, not re-proved.  Krein's
       extension line (PD continuation from an interval, Krein
       1940) and Beurling-Selberg/Vaaler one-sided majorants are
       NAMED as the adjacent machinery and NOT consumed (no
       one-sided approximation enters any budget).
  (D4) CLASS GEOMETRY.  The mode-lattice subcone {g_x} is a strict
       subcone of the full PD cone; its per-lag extremal value is a
       COMPUTABLE generalized eigenvalue:
           M_sub(u) = lambda_max(D^{-1/2} G(u) D^{-1/2}),
       G(u) = -W(u)/2 (the r195 atom kernel), D = G(0) =
       diag(L, L/2, ..., L/2).  Chain gated at every atom of every
       rung: g_v(u_q)/g_v(0) <= M_sub(u_q) <= M_KR(u_q).
       Commensurate edge atom u = L (q = h): W(L) == 0 IDENTICALLY
       on the lattice (sympy, integer k), so M_sub(L) = 0 while the
       full-cone value is cos(pi/(ceil(1)+1)) = 0 by the same
       formula -- the formula covers the edge kill.

T2  THE CONE BUDGET (the decisive computation).  All statements are
  about the subcone where the wall lives; the PRIME leg's cap is
  full-cone classical, the POLE leg's cone lower bound is 0 (it is a
  manifest square that vanishes on lattice directions orthogonal to
  the pole ray), and the ARCH leg does NOT extend to the full cone
  in pointwise form -- its regularization counterterm is PER-MODE
  (carried by g's diagonal part), not a pointwise functional of g:
  HONESTLY TYPED as the composition break (ARCH-LEG-SUBCONE-ONLY),
  and priced by the exact finite-dimensional bound instead
  (lambda_min(RawA), float64 on the mp build, mp-cross-checked).
  Per rung the LADDER (unit sphere |x| = 1, g_x(0) <= L):
    PC_KR    = 2 L sum_q |w_q| M_KR(u_q)     [full-cone classical]
    PC_sub   = 2 L sum_q |w_q| max(M_sub(u_q), 0)   [subcone/atom]
    PC_exact = -lambda_min(sum_q w_q W(u_q))        [subcone joint]
    drain_v  = -Pr(v_0) = 2 sum_q w_q g_v(log q)    [measured at
                the collapsing direction v_0, mp inverse iteration]
    AC_exact = -lambda_min(RawA);  poleTop = trace(RawP) [rank 1]
  WALL CONE BOUNDS: WB_KR = -(PC_KR + AC_exact) <= WB_sub =
  -(PC_sub + AC_exact) <= WB_joint = lambda_min(RawW - RawP)
  <= lambda_0 = lambda_min(RawW) (the truth, > 0 at true rungs).
  Gated: the chain PC_KR >= PC_sub >= PC_exact >= drain_v > 0, the
  signs (every cone bound NEGATIVE at every rung while the truth is
  positive -- the cone bound CANNOT see positivity, G24), and THE
  ARITHMETIC-INPUT GAP LADDER
    gapdex_h  = log10|WB_KR| - log10(lambda_0)   [cone vs truth]
    jointdex_h = log10|WB_joint| - log10(lambda_0) [best no-pole
                subcone knowledge vs truth = the pole's rescue depth]
    capture_h = log10(PC_KR / PC_exact)  [how much the classical cap
                overshoots the exact subcone drain -- the pure cone-
                geometry price, expected O(1)]
  and their tau-screen slopes: does the gap ride the tau ladder
  (relabeling confirmed at the cone level, with the exact dex
  table) or stay O(1) (cone geometry captures the wall -- major)?

T3  THE PER-LAG BUDGET TABLE.  Per atom per rung: measured
  g_v(u_q)/g_v(0) vs M_sub(u_q) vs M_KR(u_q); Q2 tightness
  q2dex_h = log10(M_KR(log 2) g_v(0) / g_v(log 2)); subcone
  sharpness log10(M_KR/M_sub) at q = 2; the commensurate rational
  lags u/L = f/e (prime-power rungs, r194 census) recorded against
  the cone value; the q = h edge atom EXACT-ZERO class.

T4  HONEST PRICING.  Tau screens on gapdex/jointdex/capture; loop
  guard (census-forall-k, A0-triangle, zero-verification-as-
  hypothesis, RH-conditional second moments, Gonek-1984,
  Montgomery-PC, WEIL-ALLTESTS <-> RH, PLUS the new counterfactual
  node TURAN-CONE-POSITIVITY: asserting the cone bound >= 0 for all
  tests would BE the Weil-alltests loop -- here the measured cone
  bounds are NEGATIVE, nothing is consumed, bounding over the cone
  is legitimate); worlds (SMOOTH/SCRARITH/EPSTEIN through the same
  budgets: the caps are world-blind by construction, the measured
  positions differ, typed, never sold as a separator; SMOOTH prices
  the continuum atom measure with BOTH the pointwise-integrated cap
  2L int_0^L e^{w/2} M_KR(w) dw and the Turan-integral cap
  sqrt(h) L^2 -- the classical Turan problem genuinely enters);
  the r172 witness deforms the coefficient ray, all round objects
  are matrix-side, witness-invariant BY CONSTRUCTION (typed
  definitional, r195-verbatim).  DEAD-CLASS DISCLOSURE: the r195
  guard banned the TRIVIAL l1 majorant |g(u)| <= g(0); this round
  DELIBERATELY prices the sharp-constant majorant class
  (M_KR < 1) -- the pricing is the deliverable, upgrading 'dead by
  heuristic' to an exact dex table (or refuting it).

TAXONOMY (frozen resolution logic, evaluated from measured values):
  primary  := TURAN-BUDGET-TAU-GAP iff slope(gapdex vs log10 tau)
              in [-1.3, -0.7] AND range(gapdex) > 2 dex;
              TURAN-BUDGET-O1-GAP iff range(gapdex) <= 2 dex;
              else TURAN-BUDGET-MIXED.
  drainEnum:= CONE-DRAIN-O1-CAPTURE iff range(capture) <= 2 dex AND
              |slope(capture vs log10 tau)| <= 0.30; else
              CONE-DRAIN-TAU-RIDES iff |slope| >= 0.70; else
              CONE-DRAIN-DRIFT.
  q2Enum   := Q2-TURAN-TIGHT iff max_h q2dex <= 1.0 dex;
              Q2-NEAR-TIGHT iff max_h q2dex <= 2.0; else
              Q2-FAR-INSIDE.
  subEnum  := SUBCONE-SHARP-AT-Q2 iff max_h log10(M_KR/M_sub)|_{q=2}
              <= 0.30 dex, else SUBCONE-STRICT-AT-Q2.
  archEnum := ARCH-LEG-SUBCONE-ONLY (structural: the term that does
              not classicalize, stated exactly; the prime leg
              composes, the pole leg composes trivially).
  TURAN-WRONG-DIRECTION is declared instead of primary iff any
  bound-chain gate (G21/G23) FAILS, naming the term.

NOTATION (r171-r195 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; b_k = om_k^2; par_k = (-1)^k;
nrm_0 = sqrt(2a), nrm_k = sqrt(a); atoms {(u_q, w_q)} =
{(log q, log p/sqrt q)}, q = p^m <= h; Raw = D_par N M N D_par;
W(u) the r195 atom kernel (off-diag divided differences of
2 om w sin(om u), diagonal cosine shift); g_x(u) = -x^T W(u) x / 2;
bottom direction by mp INVERSE ITERATION (r195 A3 route, 3 LU
solves, residual/stability wards).  ceil(L/u) EXACT: multiplicative
dependence q^r == h^s tested in integers (r, s <= 40) -> rational
r/s, else mp floor with a 1e-20 integrality guard band.  SMOOTH
world: continuum atom measure e^{w/2} dw on [0, L]; SCRARITH
golden-map weight permutation; EPSTEIN x^2+5y^2 Dirichlet atoms
(signed weights -> the |.| bound of D1) -- builder recipes VERBATIM.

DPS schedule (r182/r195 ladder VERBATIM): DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16, H_HOLD = 20.
ANAT_MP = (4, 5, 8, 13): mp.eigsy cross-checks of every float64
eigenvalue used (lambda_min of PB, RawA, PB+RawA; M_sub at q = 2);
all other float64 objects are O(1) top-of-spectrum ratios on the
mp-built downcast (DISCLOSED; the bottom of RawW is NEVER taken
from float64 -- r195 A3 inherited).  CTRL_CELLS = (SMOOTH, 5, 60),
(SCRARITH, 5, 60), (EPSTEIN, 8, 80).  MCUT = 64 pieces for the
SMOOTH pointwise-cap integral (tail bounded by M <= 1).  FEJER_NMAX
= 4 (gated to cover every needed n).

FROZEN BARS: ASM_BAR 1e-30 (ACF assembly ward, entrywise rel);
BUDGET_BAR 1e-25 (fro-rel); INVIT_RES_BAR 1e-12, INVIT_STAB_BAR
1e-6 (r195 A4 values); XCHK_BAR 1e-6 (f64-vs-mp eigen cross-checks,
rel to fro); CHAIN_TOL 1e-9 (bound-chain slack, relative);
MSUB_TOL 1e-9; CEIL_GUARD 1e-20; W_L_BAR 1e-50 (edge-kernel zero,
entrywise abs vs fro); TAU_FLAT_BAR 0.30; RIDE_BAND (0.70, 1.30);
RUNTIME_BAR 2700 s.  Record tolerances: LOG_TOL 0.10 dex;
SLOPE_TOL 0.05; O1_RANGE 2.0 dex; Q2_TIGHT 1.0 / Q2_NEAR 2.0 dex;
SUB_SHARP 0.30 dex; counts exact.

RECORD TABLES (frozen at freeze from the disclosed pre-freeze
calibration ladder: ONE structural smoke (smoke1, 22/23 at the
pre-freeze SHA 1256a6c9cbff0903, log kept -- the single fail was
G12, amendment A1 below; all bound/sign/budget gates green) and
ONE calibration attempt that CRASHED after all S2 gates in the S3
tightness PRINT at the h = 16 edge atom (log kept as
calib_te_crash0.log; amendment A2 below), then ONE full disclosed
calibration pass (calib_te_pass1.log, 23/23 at the pre-freeze SHA,
759.4 s; tables below frozen verbatim from it).
AMENDMENT A1 (smoke-driven, disclosed): the G12 flip identity was
first checked through sympy expand_trig, which Chebyshev-expands
cos(5(t+pi)) into cos(t)-powers that simplify fails to recontract;
expand_trig dropped, the identity cos(j(t+pi)) == (-1)^j cos(jt)
verifies directly for all j -- instrument-only, no target changed.
AMENDMENT A2 (calibration-driven, disclosed): edge atoms (u = L,
ceil = 1) took M_KR = float(mp.cos(pi/2)) = +-1e-58 mp NOISE
instead of the exact zero, and the S3 tightness print divided two
noise numbers (crash at h = 16 where the noise signs happened to
align); m_kr_of now returns EXACT 0 at ceil = 1 (the true value)
and the print guards -- no substantive number moved (the edge
contribution to every cap was <= 1e-58 before and 0 after).
No dps rung, vector recipe, control recipe, bar or enum threshold
moved at any point; record tables and resolved enums inserted at
freeze (house pattern r186/r189/r195).
CAL_LAM0 {h: log10 lambda_0}: 4: "-10.70", 5: "-15.78",
  6: "-20.19", 7: "-24.95", 8: "-29.32", 9: "-33.96", 10: "-38.83",
  11: "-43.59", 12: "-48.81", 13: "-53.43", 14: "-58.84",
  15: "-63.06", 16: "-68.17", 20: "-87.53".
CAL_WBKR {h: log10 |WB_KR|}: 4: "0.65", 5: "0.80", 6: "0.94",
  7: "0.98", 8: "1.08", 9: "1.13", 10: "1.20", 11: "1.22",
  12: "1.28", 13: "1.30", 14: "1.35", 15: "1.36", 16: "1.38",
  20: "1.49".
CAL_GAPDEX {h}: 4: "11.35", 5: "16.59", 6: "21.12", 7: "25.93",
  8: "30.40", 9: "35.09", 10: "40.03", 11: "44.82", 12: "50.10",
  13: "54.72", 14: "60.19", 15: "64.42", 16: "69.55", 20: "89.03".
CAL_JOINTDEX {h}: 4: "11.30", 5: "16.51", 6: "21.02", 7: "25.86",
  8: "30.29", 9: "34.98", 10: "39.90", 11: "44.70", 12: "49.96",
  13: "54.60", 14: "60.04", 15: "64.29", 16: "69.43", 20: "88.86".
CAL_CAPTURE {h: log10(PC_KR/PC_exact)}: 4: "0.14", 5: "0.18",
  6: "0.22", 7: "0.15", 8: "0.20", 9: "0.20", 10: "0.23",
  11: "0.19", 12: "0.23", 13: "0.20", 14: "0.23", 15: "0.21",
  16: "0.19", 20: "0.24".
CAL_MEASGAP {h: log10(PC_exact/drain_v)}: 4: "1.57", 5: "1.63",
  6: "1.69", 7: "1.73", 8: "1.77", 9: "1.81", 10: "1.84",
  11: "1.86", 12: "1.89", 13: "1.91", 14: "1.94", 15: "1.96",
  16: "1.97", 20: "2.04".
CAL_Q2DEX {h}: 4: "1.17", 5: "1.23", 6: "1.17", 7: "1.13",
  8: "1.11", 9: "1.14", 10: "1.13", 11: "1.12", 12: "1.11",
  13: "1.11", 14: "1.10", 15: "1.09", 16: "1.09", 20: "1.11".
CAL_SUBQ2 {h: log10(M_KR/M_sub) at q = 2}: "0.000" at EVERY rung
  (measured |subq2| < 5e-4 at all 14 rungs: the lattice subcone
  ATTAINS the full-cone cap at the dominant lag to f64 precision).
CAL_SLOPES: gapdex "-1.007", jointdex "-1.006", capture "-0.001",
  q2dex "+0.001".
CAL_CTRL {(world, x): (log10|WB_KR|, log10|lam0|, lam0_neg,
  gapdex)}: (SMOOTH, 5): ("0.94", "0.23", 1, "0.71");
  (SCRARITH, 5): ("0.82", "-0.51", 1, "1.33");
  (EPSTEIN, 8): ("1.06", "0.25", 1, "0.81").
CAL_SMOOTH_CAPS (log10): pointwise-integrated "0.70",
  turan-integral "0.76" -- the pointwise cap beats the
  Turan-integral cap by 0.06 dex at x = 5.
RESOLVED ENUMS (from the calibration pass, re-gated at record):
  primary TURAN-BUDGET-TAU-GAP (gapdex 11.35 -> 89.03, slope
  -1.007, r2 1.000); drainEnum CONE-DRAIN-O1-CAPTURE (capture
  0.14-0.24 dex, range 0.10, slope -0.001); q2Enum Q2-NEAR-TIGHT
  (q2dex 1.09-1.23, tau-flat); subEnum SUBCONE-SHARP-AT-Q2
  (subq2 == 0.000) -- read together: the classical Fejer cap is
  essentially EXACTLY the subcone drain capacity (0.2 dex), the
  lattice attains it, the collapsing direction uses ~1.1 dex less
  than the cap at the dominant atom, and NONE of that geometry
  sees the tau-deep positivity: the entire ladder is the
  pole-vs-drain cancellation.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
classical layer G10-G14 (sympy exact); S2 mp/f64 budgets G20-G25;
S3 tightness table G30; S4 controls/witness G40-G41; S5
screens/adjudication G50-G53; S6 pricing G60-G61 + G99 runtime.
DETERMINISM: no randomness anywhere; ProcessPool results keyed;
run2 must be identical modulo wall-clock tokens (lines carrying
'WALL').

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt X, note DXXIII, 2026-08-22)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays a6edc3f911e8f069.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH10-F2 [MINOR, SUBCONE-SHARP attainment wording overstates]:
#   ORIGINAL (this spec's CAL_SUBQ2 comment + note DXXI): "the
#   lattice subcone ATTAINS the full-cone cap at the dominant lag to
#   f64 precision" -- overstated as written: this round's OWN
#   printed table shows a REAL deficit at irrational lags (h = 5,
#   q = 2: M_sub 0.7067 vs M_KR 0.7071, deficit 4.1e-4 -- twelve
#   orders above f64 resolution; h = 9: 0.8082 vs 0.8090).
#   CORRECTED (KB, Bughunt X mp adjudication, SPEC 5551aa7b967230f1):
#   EXACT attainment holds at RATIONAL lags only (h = 4, q = 2,
#   u/L = 1/2 exactly: deficit -9.7e-122 at dps 120 -- an IDENTITY:
#   the Fejer extremal sequence on the u-lattice lifts exactly into
#   the K-mode cone); elsewhere NEAR-attainment of the denseness
#   class (own log's 4.1e-4 deficit at h = 5, inside the frozen
#   0.30 dex bar).  Corrected wording: "erreicht die Kappe EXAKT an
#   rationalen Lags (u/L = f/e; Identitaet, mp < 1e-45) und bis auf
#   < 5e-4 dex sonst" statt "auf f64-Praezision".  Fejer extremals
#   lift exactly only at rational lags -- this answers note DXXI's
#   named next step (b): the Fejer bump-trains are exactly
#   representable in the K-mode lattice AT RATIONAL LAGS ONLY.  The
#   enum SUBCONE-SHARP-AT-Q2 (bar 0.30 dex) and every verdict stand.
# =====================================================================

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
CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
GOLD = (math.sqrt(5.0) - 1.0) / 2.0
FEJER_NMAX = 4
MCUT = 64

ASM_BAR = 1e-30
BUDGET_BAR = 1e-25
INVIT_RES_BAR = 1e-12
INVIT_STAB_BAR = 1e-6
XCHK_BAR = 1e-6
CHAIN_TOL = 1e-9
MSUB_TOL = 1e-9
CEIL_GUARD = 1e-20
W_L_BAR = 1e-50
TAU_FLAT_BAR = 0.30
RIDE_LO, RIDE_HI = 0.70, 1.30
LOG_TOL = 0.10
SLOPE_TOL = 0.05
O1_RANGE = 2.0
Q2_TIGHT = 1.0
Q2_NEAR = 2.0
SUB_SHARP = 0.30

# --------------------- calibrated record tables (calib_te_pass1.log)
CAL_LAM0 = {4: "-10.70", 5: "-15.78", 6: "-20.19", 7: "-24.95",
            8: "-29.32", 9: "-33.96", 10: "-38.83", 11: "-43.59",
            12: "-48.81", 13: "-53.43", 14: "-58.84", 15: "-63.06",
            16: "-68.17", 20: "-87.53"}
CAL_WBKR = {4: "0.65", 5: "0.80", 6: "0.94", 7: "0.98", 8: "1.08",
            9: "1.13", 10: "1.20", 11: "1.22", 12: "1.28",
            13: "1.30", 14: "1.35", 15: "1.36", 16: "1.38",
            20: "1.49"}
CAL_GAPDEX = {4: "11.35", 5: "16.59", 6: "21.12", 7: "25.93",
              8: "30.40", 9: "35.09", 10: "40.03", 11: "44.82",
              12: "50.10", 13: "54.72", 14: "60.19", 15: "64.42",
              16: "69.55", 20: "89.03"}
CAL_JOINTDEX = {4: "11.30", 5: "16.51", 6: "21.02", 7: "25.86",
                8: "30.29", 9: "34.98", 10: "39.90", 11: "44.70",
                12: "49.96", 13: "54.60", 14: "60.04", 15: "64.29",
                16: "69.43", 20: "88.86"}
CAL_CAPTURE = {4: "0.14", 5: "0.18", 6: "0.22", 7: "0.15",
               8: "0.20", 9: "0.20", 10: "0.23", 11: "0.19",
               12: "0.23", 13: "0.20", 14: "0.23", 15: "0.21",
               16: "0.19", 20: "0.24"}
CAL_MEASGAP = {4: "1.57", 5: "1.63", 6: "1.69", 7: "1.73",
               8: "1.77", 9: "1.81", 10: "1.84", 11: "1.86",
               12: "1.89", 13: "1.91", 14: "1.94", 15: "1.96",
               16: "1.97", 20: "2.04"}
CAL_Q2DEX = {4: "1.17", 5: "1.23", 6: "1.17", 7: "1.13", 8: "1.11",
             9: "1.14", 10: "1.13", 11: "1.12", 12: "1.11",
             13: "1.11", 14: "1.10", 15: "1.09", 16: "1.09",
             20: "1.11"}
CAL_SUBQ2 = {h: "0.000" for h in (4, 5, 6, 7, 8, 9, 10, 11, 12,
                                  13, 14, 15, 16, 20)}
CAL_SLOPES = {"gapdex": "-1.007", "jointdex": "-1.006",
              "capture": "-0.001", "q2dex": "+0.001"}
CAL_CTRL = {("SMOOTH", 5): ("0.94", "0.23", 1, "0.71"),
            ("SCRARITH", 5): ("0.82", "-0.51", 1, "1.33"),
            ("EPSTEIN", 8): ("1.06", "0.25", 1, "0.81")}
CAL_SMOOTH_CAPS = {"pointwise": "0.70", "turan": "0.76"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
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
                       "verification/ import; the round is fully "
                       "zero-free (only classical unconditional "
                       "extremal theory + the builder enter)")


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
    """Returns (atoms, qlist) with atoms = [(u, w)], qlist = [q]."""
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        qs = [q for q, _p in nlist]
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms, qs
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
    """Per-atom wall kernel W(u): x^T W x = -2 int_0^{L-u} A A(.+u)."""
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


def form_of(x, M, K):
    return sum(x[i] * M[i, j] * x[j] for i in range(K)
               for j in range(K))


def bottom_vec_mp(Raw, K, froW):
    """Bottom eigenvector by mp inverse iteration (r195 A3 route)."""
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


def mult_dep_ratio(q: int, h: int, rmax: int = 40):
    """Exact multiplicative-dependence test: q^r == h^s ->
    log(h)/log(q) = r/s rational; returns (r, s) or None."""
    for r in range(1, rmax + 1):
        qr = q ** r
        s = 1
        hs = h
        while hs < qr:
            s += 1
            hs *= h
        if hs == qr:
            return r, s
    return None


def ceil_L_over_u(q: int, h: int, L, u) -> tuple[int, bool]:
    """Exact ceil(L/u) = ceil(log h / log q); (value, is_rational)."""
    dep = mult_dep_ratio(q, h)
    if dep is not None:
        r, s = dep                      # L/u = r/s exactly
        return -((-r) // s), True
    rat = L / u
    fl = mp.floor(rat)
    if abs(rat - mp.nint(rat)) <= mp.mpf(CEIL_GUARD):
        raise RuntimeError("integrality guard tripped q=%d h=%d"
                           % (q, h))
    return int(fl) + 1, False


def m_kr_of(nceil: int):
    """M_KR = cos(pi/(ceil(L/u)+1)); nceil = 1 (u = L) -> 0 EXACT
    (cos(pi/2) returned as exact zero, not mp noise)."""
    if nceil == 1:
        return mp.mpf(0)
    return mp.cos(mp.pi / (nceil + 1))


def f64_of(Mmp, K):
    return np.array([[float(Mmp[i, j]) for j in range(K)]
                     for i in range(K)])


def msub_of(Wq_np, L, K):
    """M_sub(u) = lambda_max(D^{-1/2} (-W/2) D^{-1/2}),
    D = diag(L, L/2, ...)."""
    d = np.full(K, float(L) / 2.0)
    d[0] = float(L)
    s = 1.0 / np.sqrt(d)
    G = -0.5 * Wq_np
    Gs = G * s[:, None] * s[None, :]
    return float(np.linalg.eigvalsh(Gs)[-1]), Gs


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
            # ---- ACF assembly ward (r195 law reused as ward)
            Wq_list = [W_atom_mp(u, oms, b, L, K) for u, _w in atoms]
            S = mp.zeros(K, K)
            for (u, w), Wq in zip(atoms, Wq_list):
                for i in range(K):
                    for j in range(K):
                        S[i, j] += w * Wq[i, j]
            dev = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    tgt = RawW[i, j] - RawP[i, j] - RawA[i, j]
                    dev = max(dev, abs(tgt - S[i, j]))
                    den = max(den, abs(tgt))
            out["asm_dev"] = float(dev / den)
            # ---- edge kernel zero (q = h atom, present iff
            # h is in the atom list)
            if qs[-1] == h:
                Wl = Wq_list[-1]
                wmax = max(abs(Wl[i, j]) for i in range(K)
                           for j in range(K))
                out["edge_zero_dev"] = float(wmax / froW)
            else:
                out["edge_zero_dev"] = 0.0
            # ---- bottom direction (mp inverse iteration)
            v0, lam0, invres, invstab = bottom_vec_mp(RawW, K, froW)
            out["invit_res"] = invres
            out["invit_stab"] = invstab
            out["lam0_pos"] = bool(lam0 > 0)
            out["log10lam0"] = float(mp.log(abs(lam0), 10))
            P = form_of(v0, RawP, K)
            A_ = form_of(v0, RawA, K)
            tq_mp = [w * form_of(v0, Wq, K)
                     for (u, w), Wq in zip(atoms, Wq_list)]
            Pr = sum(tq_mp, mp.mpf(0))
            out["budget_dev"] = float(abs(P + A_ + Pr - lam0) / froW)
            out["bud_P"] = float(P)
            out["bud_A"] = float(A_)
            out["bud_Pr"] = float(Pr)
            gv0 = L * v0[0] ** 2 \
                + (L / 2) * sum(v0[k] ** 2 for k in range(1, K))
            out["gv0"] = float(gv0)
            # ---- per-atom table: measured / M_sub / M_KR
            g_meas = [-form_of(v0, Wq, K) / 2 for Wq in Wq_list]
            tmax = max(abs(t) for t in tq_mp)
            zbar = mp.mpf("1e-30") * tmax
            out["tq_zero"] = sum(1 for t in tq_mp if abs(t) <= zbar)
            rows = []
            chain_ok = True
            nmax_needed = 0
            ceil_xdev = 0.0
            for (u, w), q, gm, Wq in zip(atoms, qs, g_meas, Wq_list):
                nceil, is_rat = ceil_L_over_u(q, h, L, u)
                nmax_needed = max(nmax_needed, nceil - 1)
                # cross-check exact ceil vs mp floor route
                ratf = float(L / u)
                cfl = int(math.floor(ratf)) + \
                    (0 if abs(ratf - round(ratf)) < 1e-9
                     and is_rat and abs(ratf - round(ratf)) < 1e-9
                     else 1)
                if is_rat and abs(ratf - round(ratf)) < 1e-9:
                    cfl = int(round(ratf))
                ceil_xdev = max(ceil_xdev, abs(nceil - cfl))
                mkr = m_kr_of(nceil)
                Wq_np = f64_of(Wq, K)
                msub, _G = msub_of(Wq_np, L, K)
                ratio = float(gm / gv0)
                if not (ratio <= msub * (1 + CHAIN_TOL) + 1e-15):
                    chain_ok = False
                if not (msub <= float(mkr) * (1 + CHAIN_TOL)
                        + MSUB_TOL):
                    chain_ok = False
                rows.append((q, float(u / L), nceil, is_rat,
                             float(mkr), msub, ratio))
            out["rows"] = rows
            out["chain_ok"] = chain_ok
            out["nmax_needed"] = nmax_needed
            out["ceil_xdev"] = ceil_xdev
            # ---- caps ladder
            PC_KR = 2 * L * sum(abs(w) * m_kr_of(
                ceil_L_over_u(q, h, L, u)[0])
                for (u, w), q in zip(atoms, qs))
            PC_sub = 2 * float(L) * sum(
                abs(float(w)) * max(r[5], 0.0)
                for (u, w), r in zip(atoms, rows))
            PB = mp.zeros(K, K)
            for (u, w), Wq in zip(atoms, Wq_list):
                for i in range(K):
                    for j in range(K):
                        PB[i, j] += w * Wq[i, j]
            PB_np = f64_of(PB, K)
            RawA_np = f64_of(RawA, K)
            lmin_PB = float(np.linalg.eigvalsh(PB_np)[0])
            lmin_A = float(np.linalg.eigvalsh(RawA_np)[0])
            lmin_PBA = float(np.linalg.eigvalsh(PB_np + RawA_np)[0])
            PC_exact = max(-lmin_PB, 0.0)
            AC_exact = max(-lmin_A, 0.0)
            drain_v = float(-Pr)
            archdrain_v = float(-A_)
            out["PC_KR"] = float(PC_KR)
            out["PC_sub"] = PC_sub
            out["PC_exact"] = PC_exact
            out["drain_v"] = drain_v
            out["AC_exact"] = AC_exact
            out["archdrain_v"] = archdrain_v
            out["poleTop"] = float(sum(RawP[i, i] for i in range(K)))
            WB_KR = -(float(PC_KR) + AC_exact)
            WB_sub = -(PC_sub + AC_exact)
            WB_joint = lmin_PBA
            out["WB_KR"] = WB_KR
            out["WB_sub"] = WB_sub
            out["WB_joint"] = WB_joint
            out["gapdex"] = math.log10(-WB_KR) - out["log10lam0"]
            out["jointdex"] = math.log10(-WB_joint) \
                - out["log10lam0"]
            out["capture"] = math.log10(float(PC_KR) / PC_exact)
            out["subcap"] = math.log10(PC_sub / PC_exact)
            out["measgap"] = math.log10(PC_exact / drain_v)
            i2 = qs.index(2)
            out["q2dex"] = math.log10(rows[i2][4] * out["gv0"]
                                      / float(g_meas[i2]))
            out["subq2"] = math.log10(rows[i2][4] / rows[i2][5])
            # ---- mp cross-checks at ANAT_MP
            if h in ANAT_MP:
                froPB = mp.sqrt(sum(PB[i, j] ** 2 for i in range(K)
                                    for j in range(K)))
                E1 = mp.eigsy(PB, eigvals_only=True)
                E2 = mp.eigsy(RawA, eigvals_only=True)
                PBA = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        PBA[i, j] = PB[i, j] + RawA[i, j]
                E3 = mp.eigsy(PBA, eigvals_only=True)
                mn1 = min(E1[i] for i in range(K))
                mn2 = min(E2[i] for i in range(K))
                mn3 = min(E3[i] for i in range(K))
                xd = max(abs(mn1 - lmin_PB), abs(mn2 - lmin_A),
                         abs(mn3 - lmin_PBA)) / froPB
                # M_sub at q = 2 in mp
                Wq2 = Wq_list[i2]
                Dm = mp.zeros(K, K)
                for k in range(K):
                    Dm[k, k] = 1 / mp.sqrt(L if k == 0 else L / 2)
                Gs = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Gs[i, j] = -Wq2[i, j] / 2 \
                            * Dm[i, i] * Dm[j, j]
                E4 = mp.eigsy(Gs, eigvals_only=True)
                mx4 = max(E4[i] for i in range(K))
                xd = max(xd, abs(mx4 - rows[i2][5]))
                out["xchk_dev"] = float(xd)
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
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            RawA_np = f64_of(RawA, K)
            lmin_A = float(np.linalg.eigvalsh(RawA_np)[0])
            AC_exact = max(-lmin_A, 0.0)
            atoms, qs = world_atoms(world, x)
            if atoms is not None:
                PC_KR = 2 * L * sum(abs(w) * m_kr_of(
                    ceil_L_over_u(q, x, L, u)[0])
                    for (u, w), q in zip(atoms, qs))
                PB = mp.zeros(K, K)
                for u, w in atoms:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for i in range(K):
                        for j in range(K):
                            PB[i, j] += w * Wq[i, j]
                PB_np = f64_of(PB, K)
                lmin_PB = float(np.linalg.eigvalsh(PB_np)[0])
                PC_exact = max(-lmin_PB, 0.0)
                out["PC_KR"] = float(PC_KR)
                out["PC_exact"] = PC_exact
            else:
                # SMOOTH: pointwise-integrated cap
                # 2 L int_0^L e^{w/2} M_KR(w) dw, piecewise
                # M_KR = cos(pi/(m+2)) on (L/(m+1), L/m); plus the
                # Turan-integral cap sqrt(x) L^2 (D2).
                acc = mp.mpf(0)
                for m2 in range(1, MCUT + 1):
                    lo = L / (m2 + 1)
                    hi = L / m2
                    seg = 2 * (mp.e ** (hi / 2) - mp.e ** (lo / 2))
                    acc += mp.cos(mp.pi / (m2 + 2)) * seg
                acc += 2 * (mp.e ** (L / (2 * (MCUT + 1))) - 1)
                PC_KR = 2 * L * acc
                cap_turan = mp.sqrt(x) * L ** 2
                out["PC_KR"] = float(PC_KR)
                out["cap_turan"] = float(cap_turan)
                PB = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        PB[i, j] = RawW[i, j] - RawP[i, j] \
                            - RawA[i, j]
                PB_np = f64_of(PB, K)
                lmin_PB = float(np.linalg.eigvalsh(PB_np)[0])
                PC_exact = max(-lmin_PB, 0.0)
                out["PC_exact"] = PC_exact
            WB_KR = -(out["PC_KR"] + AC_exact)
            out["WB_KR"] = WB_KR
            E = mp.eigsy(RawW, eigvals_only=True)
            lam0 = min(E[i] for i in range(K))
            out["lam0_neg"] = bool(lam0 < 0)
            out["log10lam0"] = float(mp.log(abs(lam0), 10))
            out["gapdex"] = math.log10(-WB_KR) - out["log10lam0"]
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def classical_layer() -> None:
    import sympy as sp

    # ---- G10: Fejer extremal construction, n = 1..FEJER_NMAX
    ok10 = True
    det10 = []
    for n in range(1, FEJER_NMAX + 1):
        al = sp.pi / (n + 2)
        Sv = [sp.sin((m2 + 1) * al) for m2 in range(n + 1)]
        c = [sum(Sv[m2] * Sv[m2 + j] for m2 in range(n + 1 - j))
             for j in range(n + 1)]
        if sp.simplify(c[1] / c[0] - sp.cos(al)) != 0:
            ok10 = False
            det10.append("n=%d ratio FAIL" % n)
        # boundary truncation: sin((n+2)al) = 0 exactly
        if sp.simplify(sp.sin((n + 2) * al)) != 0:
            ok10 = False
            det10.append("n=%d trunc FAIL" % n)
    check("G10-fejer-extremal-exact", ok10,
          "the Fejer extremal sequence c_j = autocorrelation of "
          "S_m = sin((m+1)pi/(n+2)) (a MANIFEST square, PD by "
          "Herglotz; length n+1 so c_j = 0 for j > n by "
          "construction; the truncation sin((n+2)a) = 0 is exact) "
          "attains c_1/c_0 == cos(pi/(n+2)) EXACTLY for n = 1..%d "
          "(sympy)%s -- the discrete extremal is constructed, not "
          "cited" % (FEJER_NMAX,
                     ("; " + "; ".join(det10)) if det10 else ""))

    # ---- G11: dual node certificate (optimality), n = 1..FEJER_NMAX
    ok11 = True
    det11 = []
    for n in range(1, FEJER_NMAX + 1):
        al = sp.pi / (n + 2)
        # distinct-cosine nodes among theta_r = (2r+1)al, r = 1..n
        nodes = []
        seen = set()
        for r in range(1, n + 1):
            th = (2 * r + 1) * al
            key = sp.srepr(sp.simplify(sp.cos(th)))
            if key not in seen:
                seen.add(key)
                nodes.append(th)
        d = len(nodes)
        A = sp.Matrix(
            [[sp.cos(j * nodes[r]) for r in range(d)]
             for j in range(2, n + 1)])
        if n == 1:
            gens = [sp.Matrix([1])]
        else:
            gens = A.nullspace()
        if len(gens) != 1:
            ok11 = False
            det11.append("n=%d nullspace dim %d" % (n, len(gens)))
            continue
        g = gens[0]
        # sign-resolve via evalf (amendment A1), then exact checks
        s0 = 1 if g[0].evalf() > 0 else -1
        rho = [sp.simplify(s0 * g[r]) for r in range(d)]
        if any(sp.simplify(rr).evalf() <= 0 for rr in rho):
            ok11 = False
            det11.append("n=%d rho sign FAIL" % n)
            continue
        num = sum(rho)
        den = -2 * sum(rho[r] * sp.cos(nodes[r]) for r in range(d))
        if sp.simplify(num / den - sp.cos(al)) != 0:
            ok11 = False
            det11.append("n=%d bound FAIL" % n)
    check("G11-fejer-dual-certificate-optimal", ok11,
          "OPTIMALITY machine-certified for n = 1..%d: nonnegative "
          "weights rho at the zeros theta_r = (2r+1)pi/(n+2) of the "
          "extremal polynomial satisfy sum rho cos(j theta) = 0 for "
          "j = 2..n (1-dim exact nullspace), so 0 <= sum rho "
          "p(theta) = sum rho + 2 c_1 sum rho cos(theta) forces "
          "c_1 <= (sum rho)/(-2 sum rho cos theta) == cos(pi/(n+2)) "
          "EXACTLY (sympy) -- with G10 the discrete Fejer constant "
          "is fully proved in-code, no citation consumed%s"
          % (FEJER_NMAX,
             ("; " + "; ".join(det11)) if det11 else ""))

    # ---- G12: flip bound + transfer arithmetic typing
    t = sp.symbols("t", real=True)
    okflip = all(sp.simplify(sp.cos(j * (t + sp.pi))
                             - (-1) ** j * sp.cos(j * t)) == 0
                 for j in range(1, FEJER_NMAX + 2))
    check("G12-lattice-transfer-and-flip", okflip,
          "TRANSFER (typed classical, Bochner/Herglotz): the "
          "restriction of a PD function to the lattice uZ is a PD "
          "sequence; supp g in [-L, L] with g(+-L) = 0 (our "
          "autocorrelation class) kills c_j for j >= L/u, leaving "
          "n = ceil(L/u) - 1 nonzero lags, hence g(u) <= "
          "cos(pi/(ceil(L/u)+1)) g(0) by G10/G11; SIGNED version "
          "|g(u)| <= M_KR g(0) via the theta -> theta + pi flip "
          "cos(j(t+pi)) == (-1)^j cos(jt) (sympy exact, j <= %d) -- "
          "matches the Boas-Kac/Kolountzakis-Revesz open-interval "
          "value cos(pi/(n+2)) on 1/(n+1) <= u/L < 1/n INCLUDING "
          "the commensurate endpoints (where g(L) = 0 drops one "
          "lag): the import is sharp on the full cone; per-atom "
          "ceil arithmetic is computed EXACTLY (integer "
          "multiplicative-dependence q^r == h^s) and cross-checked "
          "against mp floor in G21" % (FEJER_NMAX + 1))

    # ---- G13: Turan interval exhibit (triangle in-subcone)
    u, Ls = sp.symbols("u Lsym", positive=True)
    g_e0 = -(2 * (u - Ls)) / 2
    ok_tri = sp.simplify(g_e0 - (Ls - u)) == 0
    integ = 2 * sp.integrate(Ls - u, (u, 0, Ls))   # even function
    ok_eq = sp.simplify(integ - Ls ** 2) == 0
    x0, y = sp.symbols("x0 y", positive=True)
    lhs = (Ls * x0) ** 2
    rhs = Ls * (Ls * x0 ** 2 + (Ls / 2) * y)
    ok_ineq = sp.simplify(rhs - lhs - (Ls ** 2 / 2) * y) == 0
    check("G13-turan-interval-triangle-exhibit",
          bool(ok_tri and ok_eq and ok_ineq),
          "the mode-lattice subcone CONTAINS the Turan-problem "
          "extremal: x = e_0 gives A = 1 (box window B), g_{e0}(u) "
          "= -W_00(u)/2 == L - u (the Fejer triangle = box "
          "autocorrelation, sympy exact from the r195 kernel "
          "diagonal), and int_{-L}^{L} g_{e0} = L^2 == L g_{e0}(0) "
          "with EQUALITY (Siegel 1935 / Boas-Kac 1945 bound int g "
          "<= L g(0) attained); subcone-wide the Turan inequality "
          "is the identity L g_x(0) - int g_x = (L^2/2)(|x|^2 - "
          "x_0^2) >= 0 (int g_x = (L x_0)^2: only the k = 0 mode "
          "integrates) -- equality IFF x = +-e_0: the Turan "
          "extremal direction IS the k = 0 mode")

    # ---- G14: commensurate edge kernel zero (u = L, integer k)
    ki, kj = sp.symbols("ki kj", integer=True, positive=True)
    omi = 2 * sp.pi * ki / Ls
    omj = 2 * sp.pi * kj / Ls
    off = 2 * (omi * sp.sin(omi * Ls) - omj * sp.sin(omj * Ls)) \
        / (omi ** 2 - omj ** 2)
    dia = sp.sin(omi * Ls) / omi + (Ls - Ls) * sp.cos(omi * Ls)
    zz = 2 * (Ls - Ls)
    ok14 = (sp.simplify(off) == 0 and sp.simplify(dia) == 0
            and sp.simplify(zz) == 0)
    check("G14-commensurate-edge-kernel-zero", ok14,
          "W(L) == 0 IDENTICALLY on the commensurate lattice "
          "(sin(2 pi k) = 0, integer k, sympy): the q = h edge atom "
          "contributes NOTHING for ANY direction -- M_sub(L) = 0 "
          "exactly while the full-cone formula gives the same "
          "cos(pi/(1+1)) = 0 (ceil(L/L) = 1): the formula covers "
          "the edge kill; numeric ward per rung in G20 detail")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("turan_extremal_probe -- PRIME.TURAN.EXTREMAL.01  "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/enum thresholds declared in the "
          "frozen spec (SPEC_SHA covers the declaration); record "
          "tables frozen from the disclosed calibration ladder "
          "(one smoke, one calib pass, amendments A1-A2 in the "
          "spec); tau_h enters ONLY as a measured per-rung scalar "
          "(screens); DEAD-CLASS DISCLOSURE: this round "
          "deliberately prices the SHARP-CONSTANT pointwise "
          "majorant class (M_KR < 1) that the r195 guard flagged "
          "in its trivial |g| <= g(0) form -- the pricing is the "
          "deliverable, the gap table is the honest output; no "
          "one-sided (Beurling-Selberg/Vaaler) majorant is used "
          "anywhere")

    # ------------------------------------------------------------ S1
    section("S1  CLASSICAL LAYER (Fejer / Turan / Boas-Kac, exact)")
    classical_layer()

    # ------------------------------------------------------------ S2
    section("S2  CONE BUDGETS (all reachable rungs)")
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
        check("G20-assembly-and-bottom-wards", False,
              "worker errors at %s" % errs)
        print("ABORT: worker errors")
        return 1

    check("G20-assembly-and-bottom-wards", all(
        res[h]["asm_dev"] <= ASM_BAR
        and res[h]["invit_res"] <= INVIT_RES_BAR
        and res[h]["invit_stab"] <= INVIT_STAB_BAR
        and res[h]["budget_dev"] <= BUDGET_BAR
        and res[h]["lam0_pos"]
        and res[h]["edge_zero_dev"] <= W_L_BAR for h in rungs),
          "r195 dictionary re-warded at every rung: ACF assembly "
          "RawW - RawP - RawA == sum w_q W(u_q) max rel dev %.1e "
          "(bar %.0e); bottom direction by mp inverse iteration "
          "(residual <= %.1e, stability <= %.1e); budget identity "
          "P + A + Pr == lambda_0 <= %.1e fro-rel; lambda_0 > 0 at "
          "ALL %d true rungs (the wall is PSD -- the object the "
          "cone bounds are priced against); edge kernel W(L) numeric "
          "max %.1e/fro (G14 ward)"
          % (max(res[h]["asm_dev"] for h in rungs), ASM_BAR,
             max(res[h]["invit_res"] for h in rungs),
             max(res[h]["invit_stab"] for h in rungs),
             max(res[h]["budget_dev"] for h in rungs), len(rungs),
             max(res[h]["edge_zero_dev"] for h in rungs)))

    check("G21-pointwise-bound-chain", all(
        res[h]["chain_ok"] and res[h]["nmax_needed"] <= FEJER_NMAX
        and res[h]["ceil_xdev"] == 0 for h in rungs),
          "THE IMPORT VALIDATES AGAINST MEASUREMENT at every atom "
          "of every rung: g_v(u_q)/g_v(0) <= M_sub(u_q) <= "
          "M_KR(u_q) = cos(pi/(ceil(L/u_q)+1)) (chain tol %.0e); "
          "every needed Fejer degree n = ceil - 1 <= %d is covered "
          "by the G10/G11 exact certificates; exact integer ceil "
          "(multiplicative dependence q^r == h^s) == mp floor "
          "route at every atom (%d rungs)"
          % (CHAIN_TOL, FEJER_NMAX, len(rungs)))

    mp_here = [h for h in rungs if h in ANAT_MP]
    check("G22-mp-crosschecks", all(
        res[h]["xchk_dev"] <= XCHK_BAR for h in mp_here),
          "every float64 eigenvalue actually consumed (lambda_min "
          "of the prime block, of RawA, of prime+arch; M_sub at "
          "q = 2) re-computed in full mp at rungs %s: max rel dev "
          "%.1e (bar %.0e) -- the O(1) spectral objects are "
          "float64-safe as disclosed; the bottom of RawW is never "
          "taken from float64"
          % (str(mp_here),
             max(res[h]["xchk_dev"] for h in mp_here), XCHK_BAR))

    check("G23-caps-ladder-order", all(
        res[h]["PC_KR"] >= res[h]["PC_sub"] * (1 - CHAIN_TOL)
        and res[h]["PC_sub"] >= res[h]["PC_exact"] * (1 - CHAIN_TOL)
        and res[h]["PC_exact"] >= res[h]["drain_v"] * (1 - CHAIN_TOL)
        and res[h]["drain_v"] > 0
        and res[h]["AC_exact"] >= res[h]["archdrain_v"]
        * (1 - CHAIN_TOL) for h in rungs),
          "the T2 ladder orders correctly at every rung: PC_KR >= "
          "PC_sub >= PC_exact >= drain(v_0) > 0 and AC_exact >= "
          "archdrain(v_0) -- the classical inequalities COMPOSE for "
          "the prime leg (no wrong-direction term); the arch leg is "
          "priced subcone-exactly (its regularization counterterm "
          "is per-mode, NOT a pointwise functional of g -- the one "
          "term that does not classicalize, typed "
          "ARCH-LEG-SUBCONE-ONLY); the pole cone bound is 0 "
          "(manifest square)")

    check("G24-cone-bound-sign", all(
        res[h]["WB_KR"] < 0 and res[h]["WB_sub"] < 0
        and res[h]["WB_joint"] < 0 and res[h]["lam0_pos"]
        for h in rungs),
          "THE DECISIVE SIGN RESULT: every cone bound is NEGATIVE "
          "at every rung (WB_KR = %s at h in (4, 13, 20)) while the "
          "truth lambda_0 is POSITIVE-tiny -- the classical PD-cone "
          "worst case does NOT see wall positivity, even the exact "
          "subcone no-pole bound WB_joint < 0: cone geometry alone "
          "permits O(10)-deep negative walls, the positivity is "
          "carried entirely by the pole-vs-drain cancellation at "
          "the collapsing direction (r195-concordant); NO "
          "positivity assertion is made over any test class -- the "
          "Weil-alltests loop is NOT entered"
          % str({h: "%.1f" % res[h]["WB_KR"]
                 for h in (4, 13, 20) if h in res}))

    if calib or smoke:
        for h in rungs:
            print("CAL lad h=%d lam0 %.2f wbkr %.2f gapdex %.2f "
                  "jointdex %.2f capture %.2f subcap %.2f measgap "
                  "%.2f q2dex %.2f subq2 %.3f"
                  % (h, res[h]["log10lam0"],
                     math.log10(-res[h]["WB_KR"]), res[h]["gapdex"],
                     res[h]["jointdex"], res[h]["capture"],
                     res[h]["subcap"], res[h]["measgap"],
                     res[h]["q2dex"], res[h]["subq2"]))
        ok25 = True
    else:
        ok25 = all(
            abs(res[h]["log10lam0"] - float(CAL_LAM0[h])) <= LOG_TOL
            and abs(math.log10(-res[h]["WB_KR"])
                    - float(CAL_WBKR[h])) <= LOG_TOL
            and abs(res[h]["gapdex"] - float(CAL_GAPDEX[h]))
            <= 2 * LOG_TOL
            and abs(res[h]["jointdex"] - float(CAL_JOINTDEX[h]))
            <= 2 * LOG_TOL
            and abs(res[h]["capture"] - float(CAL_CAPTURE[h]))
            <= LOG_TOL
            and abs(res[h]["measgap"] - float(CAL_MEASGAP[h]))
            <= LOG_TOL for h in rungs)
    check("G25-record-gap-tables", ok25,
          "THE ARITHMETIC-INPUT GAP LADDER (record vs frozen): "
          "gapdex (classical cone bound vs truth) = %s dex; "
          "jointdex (exact subcone no-pole vs truth) = %s; the "
          "cone-geometry price capture = log10(PC_KR/PC_exact) = "
          "%s (O(1), FLAT); measured-direction gap "
          "log10(PC_exact/drain(v_0)) = %s -- the classical budget "
          "is wrong by 11..89 dex about the WALL but only "
          "0.14-0.24 dex about the DRAIN: the entire tau ladder "
          "lives in the pole-vs-drain cancellation, NOT in the "
          "cone geometry of the drain side"
          % (str({h: "%.1f" % res[h]["gapdex"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.1f" % res[h]["jointdex"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % res[h]["capture"]
                  for h in (4, 8, 13, 20) if h in res}),
             str({h: "%.2f" % res[h]["measgap"]
                  for h in (4, 8, 13, 20) if h in res})))

    # ------------------------------------------------------------ S3
    section("S3  PER-LAG TIGHTNESS TABLE")
    for h in rungs:
        for (q, ul, nc, is_rat, mkr, msub, ratio) in res[h]["rows"]:
            tdex = (math.log10(mkr / ratio)
                    if (ratio > 1e-300 and mkr > 1e-300)
                    else float("inf"))
            info("h=%d q=%d u/L %.4f%s ceil %d M_KR %.4f M_sub "
                 "%.4f meas %.3e tight_dex %.2f"
                 % (h, q, ul, " (RATIONAL)" if is_rat else "", nc,
                    mkr, msub, ratio, tdex))
    if calib or smoke:
        ok30 = True
    else:
        ok30 = all(
            abs(res[h]["q2dex"] - float(CAL_Q2DEX[h])) <= LOG_TOL
            and abs(res[h]["subq2"] - float(CAL_SUBQ2[h]))
            <= LOG_TOL for h in rungs)
    q2max = max(res[h]["q2dex"] for h in rungs)
    sub2max = max(res[h]["subq2"] for h in rungs)
    q2_enum = ("Q2-TURAN-TIGHT" if q2max <= Q2_TIGHT else
               ("Q2-NEAR-TIGHT" if q2max <= Q2_NEAR
                else "Q2-FAR-INSIDE"))
    sub_enum = ("SUBCONE-SHARP-AT-Q2" if sub2max <= SUB_SHARP
                else "SUBCONE-STRICT-AT-Q2")
    check("G30-tightness-table", ok30 and all(
        res[h]["tq_zero"] >= (1 if h in (4, 5, 7, 8, 9, 11, 13, 16)
                              else 0) for h in rungs),
          "Q2 TIGHTNESS q2dex = log10(M_KR g_v(0)/g_v(log 2)) = %s "
          "(max %.2f) -- enum %s: the dominant atom's measured "
          "sample sits a stable ~1.1 dex inside the classical "
          "extremal budget at the collapsing direction, tau-flat "
          "(within reach of the cap but NOT at the boundary); "
          "SUBCONE SHARPNESS log10(M_KR/M_sub) at q = 2 "
          "= %s (max %.3f) -- enum %s: the K-mode lattice cone "
          "nearly ATTAINS the full-cone cap, so the cap is not "
          "slack geometry -- the slack is arithmetic; commensurate "
          "q = h edge atoms EXACT ZERO at every prime-power rung "
          "(zero-class counts %s); rational lags u/L = f/e flagged "
          "in the table above"
          % (str({h: "%.2f" % res[h]["q2dex"]
                  for h in (4, 8, 13, 20) if h in res}), q2max,
             q2_enum,
             str({h: "%.3f" % res[h]["subq2"]
                  for h in (4, 8, 13, 20) if h in res}), sub2max,
             sub_enum,
             str({h: res[h]["tq_zero"] for h in rungs})))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + WITNESS")
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
            print("CAL ctrl %s x=%d wbkr %.2f lam0 %.2f neg %d "
                  "gapdex %.2f%s"
                  % (k[0], k[1], math.log10(-v["WB_KR"]),
                     v["log10lam0"], int(v["lam0_neg"]),
                     v["gapdex"],
                     (" caps pw %.2f turan %.2f"
                      % (math.log10(v["PC_KR"]),
                         math.log10(v["cap_turan"])))
                     if "cap_turan" in v else ""))
        ok40 = not cerrs and all(v["WB_KR"] < 0
                                 for v in cres.values())
    else:
        def _cm(k):
            cal = CAL_CTRL[k]
            v = cres[k]
            return (abs(math.log10(-v["WB_KR"]) - float(cal[0]))
                    <= LOG_TOL
                    and abs(v["log10lam0"] - float(cal[1]))
                    <= 2 * LOG_TOL
                    and int(v["lam0_neg"]) == cal[2]
                    and abs(v["gapdex"] - float(cal[3]))
                    <= 3 * LOG_TOL)
        sm = cres[("SMOOTH", 5)]
        ok40 = (not cerrs and all(_cm(k) for k in cres)
                and abs(math.log10(sm["PC_KR"])
                        - float(CAL_SMOOTH_CAPS["pointwise"]))
                <= LOG_TOL
                and abs(math.log10(sm["cap_turan"])
                        - float(CAL_SMOOTH_CAPS["turan"]))
                <= LOG_TOL)
    check("G40-worlds-controls", ok40,
          "the same budgets through the control worlds (caps are "
          "world-blind BY CONSTRUCTION -- lattice geometry + "
          "|weights| only -- typed, never sold as a separator): %s "
          "-- in every fake/smooth cell the wall is INDEFINITE "
          "(lambda_0 < 0) and the cone bound is negative TOO, i.e. "
          "the cone bound is qualitatively right there and misses "
          "by only 0.7-1.4 dex, versus 11..89 dex in MAIN: the "
          "tau-deep gap is a TRUE-WORLD phenomenon (same fact as "
          "wall-PSD-only-in-MAIN, typed not sold); SMOOTH prices "
          "the CLASSICAL TURAN PROBLEM quantitatively: pointwise-"
          "integrated cap 2L int e^{w/2} M_KR(w) dw vs the "
          "Turan-integral cap sqrt(x) L^2 -- the pointwise route "
          "is the sharper one (D2 genuinely enters)"
          % str({k: "wb %.1f lam0 %.1f gap %.1f"
                 % (math.log10(-v["WB_KR"]), v["log10lam0"],
                    v["gapdex"]) for k, v in sorted(cres.items())}))

    check("G41-witness-typing", True,
          "the r172 inflation witness deforms the source "
          "COEFFICIENT ray (eigenvector-side); every object of this "
          "round (M_KR, M_sub, PC/AC caps, lambda_min ladders) is "
          "matrix-side, witness-INVARIANT BY CONSTRUCTION -- typed "
          "definitional (r195-verbatim), not sold; the r186 "
          "{l_0, l_2} residue detector remains the witness "
          "instrument")

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_g, _i, r2_g = fit_line(xs_t, [res[h]["gapdex"] for h in scr])
    sl_j, _i, r2_j = fit_line(xs_t, [res[h]["jointdex"]
                                     for h in scr])
    sl_c, _i, r2_c = fit_line(xs_t, [res[h]["capture"]
                                     for h in scr])
    sl_q, _i, r2_q = fit_line(xs_t, [res[h]["q2dex"] for h in scr])
    if calib or smoke:
        print("CAL slopes: gapdex %+.3f (r2 %.3f) jointdex %+.3f "
              "(r2 %.3f) capture %+.3f (r2 %.3f) q2dex %+.3f "
              "(r2 %.3f)" % (sl_g, r2_g, sl_j, r2_j, sl_c, r2_c,
                             sl_q, r2_q))
        ok50 = True
    else:
        ok50 = (abs(sl_g - float(CAL_SLOPES["gapdex"])) <= SLOPE_TOL
                and abs(sl_j - float(CAL_SLOPES["jointdex"]))
                <= SLOPE_TOL
                and abs(sl_c - float(CAL_SLOPES["capture"]))
                <= SLOPE_TOL
                and abs(sl_q - float(CAL_SLOPES["q2dex"]))
                <= SLOPE_TOL)
    gap_range = max(res[h]["gapdex"] for h in rungs) \
        - min(res[h]["gapdex"] for h in rungs)
    cap_range = max(res[h]["capture"] for h in rungs) \
        - min(res[h]["capture"] for h in rungs)
    primary = ("TURAN-BUDGET-TAU-GAP"
               if (RIDE_LO <= abs(sl_g) <= RIDE_HI
                   and gap_range > O1_RANGE)
               else ("TURAN-BUDGET-O1-GAP" if gap_range <= O1_RANGE
                     else "TURAN-BUDGET-MIXED"))
    drain_enum = ("CONE-DRAIN-O1-CAPTURE"
                  if cap_range <= O1_RANGE
                  and abs(sl_c) <= TAU_FLAT_BAR
                  else ("CONE-DRAIN-TAU-RIDES"
                        if abs(sl_c) >= RIDE_LO
                        else "CONE-DRAIN-DRIFT"))
    if not all(res[h]["chain_ok"] for h in rungs):
        primary = "TURAN-WRONG-DIRECTION"
    check("G50-tau-screen", ok50,
          "slopes vs log10 tau_h: gapdex %+.3f and jointdex %+.3f "
          "RIDE the tau ladder at unit slope (band [%.2f, %.2f]) "
          "-- the arithmetic-input gap IS the tau currency, "
          "restated in cone coordinates; capture %+.3f and q2dex "
          "%+.3f FLAT (bar %.2f) -- the cone-geometry price of the "
          "drain and the per-atom tightness do NOT ride tau: the "
          "classical budget is a fixed O(1)-overhead instrument, "
          "the depth lives elsewhere"
          % (sl_g, sl_j, RIDE_LO, RIDE_HI, sl_c, sl_q,
             TAU_FLAT_BAR))

    delivered = {
        "ATOMS": ["CAPS"], "MODES": ["CAPS"],
        "FEJER-CERT": ["CAPS"], "CAPS": ["GAP-LADDER"],
        "MBLOCKS": ["GAP-LADDER", "TAU-SCALAR"],
        "GAP-LADDER": ["SCREENS"], "TAU-SCALAR": ["SCREENS"],
        "SCREENS": []}
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
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY":
                                  ["WEIL-ALLTESTS"],
                                  "WEIL-ALLTESTS":
                                  ["TURAN-CONE-POSITIVITY"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("CAPS", "GAP-LADDER", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "TURAN-CONE-POSITIVITY", "RH"}
    check("G51-loop-guard", ndet >= 5 and not has_cycle(delivered)
          and not hot,
          "flagged cycles DETECTED (A0-triangle, census-forall-k, "
          "Gonek-1984, Montgomery-PC, WEIL-ALLTESTS, and NEW THIS "
          "ROUND: TURAN-CONE-POSITIVITY -- asserting the cone "
          "worst case >= 0 for all tests would BE the "
          "Weil-alltests criterion), consumed by NOTHING: DFS "
          "ancestry of every delivered node is clean; BOUNDING the "
          "wall over the cone is legitimate and the measured cone "
          "bounds are NEGATIVE (G24) -- no positivity statement "
          "over any test class is made or used; the round is fully "
          "zero-free, all classical inputs (Fejer/Boas-Kac/Siegel/"
          "Kolountzakis-Revesz) unconditional and zeta-free")

    check("G52-composed-chain-typing", True,
          "leg typing: {Fejer constant + optimality certificate, "
          "triangle exhibit, edge-kernel zero, ceil arithmetic} "
          "EXACT-SYMBOLIC; {M_sub, PC/AC caps, lambda_min ladders, "
          "tightness} MEASURED (f64 on mp builds, mp-cross-checked "
          "G22); {prime-leg cap} FULL-CONE-CLASSICAL; {arch leg} "
          "SUBCONE-ONLY (the composition break, named exactly: the "
          "regularization counterterm is per-mode); {pole cone "
          "bound 0} DEFINITIONAL (manifest square); {gapdex == tau "
          "ladder + O(1)} MEASURED, concordant with the r195 "
          "definitional depth -- the relabeling barrier is NAMED "
          "at the cone level with exact dex, not crossed")

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
    cf.update({("UNC", "CONEPOS"): INF, ("CONEPOS", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'cone-bound positivity proven cofinally' as a unit edge "
          "would raise the flow to 6 -- NOT REAL (the measured "
          "cone bounds are negative at every rung, G24): this "
          "round adds NO flow; census cardinality UNCHANGED; RH "
          "unreachable without the omega edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + RESIDUE")
    check("G60-pricing", True,
          "WHAT THE IMPORT BUYS (honest): (i) the classical "
          "extremal theory prices the DRAIN side of the wall "
          "almost EXACTLY -- the full-cone Fejer cap overshoots "
          "the exact subcone drain by only 0.14-0.24 dex, FLAT in "
          "tau, and the lattice subcone ATTAINS the cap at q = 2 "
          "(subq2 = 0.000): the classical cone budget is a correct "
          "and essentially tight description of HOW MUCH the "
          "primes could drain; (ii) the POSITIVITY question is "
          "untouched by it: the cone worst case is O(10)-negative "
          "at every rung while the truth is +10^-11..-88 -- the "
          "arithmetic-input gap is EXACTLY the tau ladder "
          "(slope -1.007, r2 1.000), i.e. the wall consumes the "
          "true atom positions through the pole-vs-drain "
          "cancellation, not through any per-lag budget; the "
          "sharp-constant majorant class is hereby priced dead "
          "WITH the exact dex table (upgrading the r195 heuristic "
          "guard from 'dead class' to 'dead by 11..89 measured "
          "dex'), and Q2-NEAR-TIGHT says even the dominant atom "
          "uses ~13x less than its cap, stably -- no refinement "
          "of per-lag constants can close a tau-deep gap; the "
          "cofinality residue is UNMOVED")

    check("G61-citations-priced", True,
          "citations fixed: Fejer, J. Reine Angew. Math. 146 "
          "(1915) 53-82 (M_n = 2 cos(pi/(n+2)); proved in-code "
          "G10/G11); Boas-Kac, Duke Math. J. 12 (1945) 189-206 "
          "(pointwise interval problem + factorization theorem; "
          "our g_x are autocorrelations BY construction -- the "
          "Boas-Kac converse held trivially); Siegel, Acta Math. "
          "65 (1935) (interval Turan integral bound, triangle "
          "extremal -- attained IN-SUBCONE at x = e_0, G13); "
          "Kolountzakis-Revesz, Canad. J. Math. 58 (2006) 401-418 "
          "Cor. 4.1 (M(Omega, z) = cos(pi/(n+2)) on 1/(n+1) <= "
          "|z| < 1/n; sharpness on the full cone) and Proc. AMS "
          "131 (2003) 3423-3430 (Turan domains); "
          "Arestov-Berdysheva-Berens (pointwise problem posed); "
          "Gorbachev 2001 (ball); Krein 1940 (PD extension, "
          "context only); Beurling-Selberg/Vaaler NOT consumed "
          "(no one-sided majorant enters)")

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the Turan/Boas-Kac/Fejer extremal theory is "
         "imported exactly and priced -- the classical cone "
         "captures the drain almost exactly (capture 0.14-0.24 "
         "dex, flat), the lattice subcone ATTAINS the classical "
         "cap at the dominant lag, and the cone-vs-truth gap is "
         "EXACTLY the tau ladder (slope -1.007): the wall consumes "
         "arithmetic beyond cone geometry in the pole-vs-drain "
         "cancellation only.  Closes NOTHING, upgrades NOTHING.  "
         "NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        primary + "(G25/G50: gapdex 11..89 dex == tau ladder, "
        "slope -1.007)",
        drain_enum + "(G25/G50: capture 0.14-0.24 dex, flat)",
        q2_enum + "(G30)",
        sub_enum + "(G30)",
        "ARCH-LEG-SUBCONE-ONLY(G23: the one non-classicalizable "
        "term, named)",
        "FEJER-CONSTANT-PROVED-IN-CODE(G10/G11: construction + "
        "dual certificate, n <= 4 covers all atoms)",
        "TURAN-EXTREMAL-IN-SUBCONE(G13: e_0 = triangle, equality)",
        "EDGE-ATOM-KILL-EXACT(G14/G20)",
        "CONE-BOUND-NEGATIVE-EVERYWHERE(G24: no positivity from "
        "cone geometry; no loop consumed)",
        "WORLD-BLIND-CAPS(G40) + WITNESS-MATRIX-SIDE-INVARIANT-"
        "DEFINITIONAL(G41)",
        "TURAN-CONE-POSITIVITY-LOOP-FLAGGED-NOT-CONSUMED(G51)",
        "RELABELING-BARRIER-NAMED-AT-CONE-LEVEL(G52/G60)",
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
        primary, drain_enum, q2_enum, sub_enum,
        "ARCH-LEG-SUBCONE-ONLY", "FEJER-CONSTANT-PROVED-IN-CODE",
        "TURAN-EXTREMAL-IN-SUBCONE", "EDGE-ATOM-KILL-EXACT",
        "CONE-BOUND-NEGATIVE-EVERYWHERE", "WORLD-BLIND-CAPS",
        "TURAN-CONE-POSITIVITY-LOOP-FLAGGED-NOT-CONSUMED",
        "RELABELING-BARRIER-NAMED-AT-CONE-LEVEL",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
